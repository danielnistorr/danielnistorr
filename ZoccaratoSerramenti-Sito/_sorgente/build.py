# -*- coding: utf-8 -*-
"""
Genera tutto il materiale del sito a partire da contenuti.py (prefisso e nome da c.PREFISSO e c.NOME_SITO):
  elementor-json/   template importabili da Template > Template salvati > Importa template
  html-fallback/    una sezione per file, da incollare in un widget HTML di Elementor
  anteprima/        le pagine complete in HTML, da aprire nel browser

Uso:
  python3 build.py                       immagini servite dal sito pubblico (vedi BASE_PREDEFINITA)
  python3 build.py --base URL --out DIR  immagini da un'altra base (per esempio il WordPress di test)
"""
import argparse
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motore as m          # noqa: E402
import contenuti as c       # noqa: E402

PX = getattr(c, 'PREFISSO', 'bvg')            # prefisso di file, classi e ancore
NOME = getattr(c, 'NOME_SITO', 'Benvegnù')     # prefisso dei titoli dei template

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)

PAROLE_VIETATE = [
    'eccellenza', 'passione', 'a 360', 'soluzioni innovative', 'innovativ', 'leader', 'all\'avanguardia',
    'sinergi', 'know-how', 'mission', 'vision', 'qualità senza compromessi', 'top di gamma', 'unico nel suo genere',
    'customer experience', 'best-in-class', 'eccezional', 'straordinari', 'rivoluzionari',
]


def controlla_testi(testo, dove):
    problemi = []
    if '\u2014' in testo:
        problemi.append(f'{dove}: trattino lungo (U+2014)')
    if re.search(r'\s–\s', testo):
        problemi.append(f'{dove}: trattino medio usato come lineetta (U+2013)')
    low = testo.lower()
    for p in PAROLE_VIETATE:
        if p in low:
            problemi.append(f'{dove}: parola da evitare "{p}"')
    return problemi


def testi_visibili(node):
    out = []
    p = node.p
    for k in ('text', 'html', 'alt'):
        if isinstance(p.get(k), str):
            out.append(re.sub(r'<[^>]+>', ' ', p[k]))
    for ch in node.children:
        out.extend(testi_visibili(ch))
    return out


def link_annidati(node, dentro=False, dove=''):
    """Un contenitore-link non può contenere altri link: il browser chiude il primo <a> e la griglia si rompe."""
    out = []
    ha_link = bool(node.p.get('link') or node.p.get('url') or node.kind in ('navmenu', 'posts', 'map')
                   or '<a ' in str(node.p.get('html', '')) or '<a ' in str(node.p.get('text', '')))
    if dentro and ha_link:
        out.append(f'{dove}: link dentro un blocco già cliccabile ({node.kind})')
    entra = dentro or (node.kind == 'container' and bool(node.p.get('link')))
    for ch in node.children:
        out.extend(link_annidati(ch, entra, dove))
    return out


def alt_immagini(node, out):
    if node.kind == 'image':
        out[node.p['src'].rsplit('/', 1)[-1]] = node.p.get('alt', '')
    for ch in node.children:
        alt_immagini(ch, out)
    return out


def immagini(node):
    out = []
    for k in ('src', 'img'):
        if node.p.get(k):
            out.append(node.p[k])
    for ch in node.children:
        out.extend(immagini(ch))
    return out


def anteprima_locale(html, base, immagini_relative):
    """L'anteprima si apre con un doppio clic (o da un server locale): link tra le pagine verso i file .html accanto,
    immagini dalla cartella assets/web del repository invece che dal web."""
    pagine = {('/' if p['slug'].endswith('home') else f'/{p["slug"][3:]}/'): f'{p["slug"]}.html' for p in c.PAGINE}

    def sost(mo):
        f = pagine.get(mo.group(1))
        return f'href="{f}{mo.group(2) or ""}"' if f else mo.group(0)
    html = re.sub(r'href="(/[a-z-]*/?)(#[^"]*)?"', sost, html)
    if immagini_relative:
        html = html.replace(base, '../assets/web/')
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=c.BASE_PREDEFINITA, help='URL base delle immagini (con / finale)')
    ap.add_argument('--out', default=RADICE, help='cartella di uscita')
    ap.add_argument('--url-sito', default='', help='dominio finale (es. https://www.benvegnusrl.it): rende assoluti i link interni')
    a = ap.parse_args()
    c.imposta_base(a.base)
    m.SITO = a.url_sito

    dirs = {k: os.path.join(a.out, k) for k in ('elementor-json', 'html-fallback', 'anteprima')}
    for d in dirs.values():
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)

    problemi, tutte_img = [], []
    header, footer = c.header(), c.footer()
    m.assegna_id(header, f'{PX}-header')
    m.assegna_id(footer, f'{PX}-footer')

    def scrivi_fallback(cartella, nome, sezione, scope):
        os.makedirs(os.path.join(dirs['html-fallback'], cartella), exist_ok=True)
        with open(os.path.join(dirs['html-fallback'], cartella, nome + '.html'), 'w', encoding='utf-8') as f:
            f.write(m.sezione_html(sezione, scope) + '\n')

    # header e footer: template di tipo "section", importabili anche senza Elementor Pro
    for nodo, slug, titolo in ((header, '00-header', f'{NOME}: Header'), (footer, '99-footer', f'{NOME}: Footer')):
        with open(os.path.join(dirs['elementor-json'], f'{PX}-{slug}.json'), 'w', encoding='utf-8') as f:
            f.write(m.json_dump(m.template_json(titolo, [nodo], kind='section')))
        scrivi_fallback(slug, f'01-{slug[3:]}', nodo, f'{PX}-{slug[3:]}')
        problemi += controlla_testi(' '.join(testi_visibili(nodo)), slug)
        tutte_img += immagini(nodo)

    header_html = m.sezione_html(header, f'{PX}-header', fonts=False)
    footer_html = m.sezione_html(footer, f'{PX}-footer', fonts=False)

    for pg in c.PAGINE:
        sezioni = pg['sezioni']()
        for i, (nome, s) in enumerate(sezioni):
            m.assegna_id(s, f'{PX}-{pg["slug"]}-{nome}')
        page_settings = {'template': 'elementor_header_footer', 'hide_title': 'yes'}
        tpl = m.template_json(f'{NOME}: {pg["titolo"]}', [s for _, s in sezioni], kind='page', page_settings=page_settings)
        with open(os.path.join(dirs['elementor-json'], f'{PX}-{pg["slug"]}.json'), 'w', encoding='utf-8') as f:
            f.write(m.json_dump(tpl))
        # variante per chi non ha Elementor Pro: header e footer dentro la pagina, modello Canvas
        completa = m.template_json(f'{NOME}: {pg["titolo"]} (pagina completa)', [header] + [s for _, s in sezioni] + [footer],
                                   kind='page', page_settings={'template': 'elementor_canvas', 'hide_title': 'yes'})
        os.makedirs(os.path.join(dirs['elementor-json'], 'pagine-complete-senza-pro'), exist_ok=True)
        with open(os.path.join(dirs['elementor-json'], 'pagine-complete-senza-pro', f'{PX}-{pg["slug"]}-completa.json'), 'w',
                  encoding='utf-8') as f:
            f.write(m.json_dump(completa))
        blocchi = [header_html]
        for i, (nome, s) in enumerate(sezioni, 1):
            scope = f'{PX}-{pg["slug"][3:]}-{nome}'
            scrivi_fallback(pg['slug'], f'{i:02d}-{nome}', s, scope)
            blocchi.append(m.sezione_html(s, scope, fonts=False))
            problemi += controlla_testi(' '.join(testi_visibili(s)), f'{pg["slug"]}/{nome}')
            problemi += link_annidati(s, dove=f'{pg["slug"]}/{nome}')
            tutte_img += immagini(s)
        blocchi.append(footer_html)
        with open(os.path.join(dirs['anteprima'], f'{pg["slug"]}.html'), 'w', encoding='utf-8') as f:
            pagina = m.pagina_html(f'{pg["titolo_seo"]}', blocchi, pg.get('descrizione', ''))
            # nel repository le immagini sono in ../assets/web: l'anteprima funziona anche senza internet
            f.write(anteprima_locale(pagina, c.BASE, os.path.abspath(a.out) == os.path.abspath(RADICE)))

    # index.html: aprendo la cartella dell'anteprima (o http://localhost:8000/anteprima/) si arriva alla Home
    with open(os.path.join(dirs['anteprima'], 'index.html'), 'w', encoding='utf-8') as f:
        f.write('<!doctype html><html lang="it"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=01-home.html">'
                f'<title>{NOME}: anteprima</title></head><body><a href="01-home.html">Apri la Home</a></body></html>\n')

    # la stessa verifica sui file scritti, per sicurezza, più i controlli tecnici sul formato
    for root, _, files in os.walk(os.path.join(a.out, 'elementor-json')):
        for fn in files:
            txt = open(os.path.join(root, fn), encoding='utf-8').read()
            for vietato in ('__globals__', '"_animation"', '"animation"', 'custom_css', 'motion_fx', '"sticky"'):
                if vietato in txt:
                    problemi.append(f'{fn}: chiave vietata {vietato}')
            if re.search(r'"(size|top|right|bottom|left|column|row)": "?[a-z]{1,3}"?[,}]', txt.replace('"size": "md"', '')):
                problemi.append(f'{fn}: valore di spaziatura non numerico')
    for root, _, files in os.walk(os.path.join(a.out, 'html-fallback')):
        for fn in files:
            if re.search(r':[a-z]+px', open(os.path.join(root, fn), encoding='utf-8').read()):
                problemi.append(f'{fn}: valore CSS non numerico')
    for root, _, files in os.walk(a.out):
        # solo i file generati: fuori i sorgenti, le immagini, gli screenshot e le prove (_prova contiene pagine scaricate)
        if os.path.relpath(root, a.out).split(os.sep)[0] in ('_sorgente', 'assets', 'screenshot', '_prova'):
            continue
        for fn in files:
            if fn.endswith(('.json', '.html')):
                txt = open(os.path.join(root, fn), encoding='utf-8').read()
                if '\u2014' in txt or '\\u2014' in txt:
                    problemi.append(f'{fn}: trattino lungo nel file')

    # elenco dei testi alternativi: Elementor li perde all'import, vanno compilati nella libreria media
    alts = {}
    for nodo in (header, footer):
        alt_immagini(nodo, alts)
    for pg in c.PAGINE:
        for _, sez in pg['sezioni']():
            alt_immagini(sez, alts)
    with open(os.path.join(dirs['elementor-json'], 'testi-alternativi-immagini.txt'), 'w', encoding='utf-8') as f:
        f.write('Testo alternativo da compilare nella libreria media dopo l\'import (Elementor non lo importa)\n\n')
        for nome in sorted(alts):
            f.write(f'{nome}: {alts[nome]}\n')
            if not alts[nome]:
                problemi.append(f'{nome}: immagine senza testo alternativo')

    if problemi:
        print('PROBLEMI:')
        print('\n'.join(sorted(set(problemi))))
        sys.exit(1)
    print(f'ok: {len(c.PAGINE) + 2} template, immagini referenziate: {len(tutte_img)} ({len(set(tutte_img))} diverse), nessun trattino lungo')


if __name__ == '__main__':
    main()
