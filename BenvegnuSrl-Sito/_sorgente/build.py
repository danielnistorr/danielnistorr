# -*- coding: utf-8 -*-
"""
Genera tutto il materiale del sito Benvegnù a partire da contenuti.py:
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

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)

PAROLE_VIETATE = [
    'eccellenza', 'passione', 'a 360', 'soluzioni innovative', 'innovativ', 'leader', 'all\'avanguardia',
    'sinergi', 'know-how', 'mission', 'vision', 'qualità senza compromessi', 'top di gamma', 'unico nel suo genere',
    'customer experience', 'best-in-class', 'eccezional', 'straordinari', 'rivoluzionari',
]


def controlla_testi(testo, dove):
    problemi = []
    if '—' in testo:
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


def immagini(node):
    out = []
    for k in ('src', 'img'):
        if node.p.get(k):
            out.append(node.p[k])
    for ch in node.children:
        out.extend(immagini(ch))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=c.BASE_PREDEFINITA, help='URL base delle immagini (con / finale)')
    ap.add_argument('--out', default=RADICE, help='cartella di uscita')
    a = ap.parse_args()
    c.imposta_base(a.base)

    dirs = {k: os.path.join(a.out, k) for k in ('elementor-json', 'html-fallback', 'anteprima')}
    for d in dirs.values():
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)

    problemi, tutte_img = [], []
    header, footer = c.header(), c.footer()
    m.assegna_id(header, 'bvg-header')
    m.assegna_id(footer, 'bvg-footer')

    def scrivi_fallback(cartella, nome, sezione, scope):
        os.makedirs(os.path.join(dirs['html-fallback'], cartella), exist_ok=True)
        with open(os.path.join(dirs['html-fallback'], cartella, nome + '.html'), 'w', encoding='utf-8') as f:
            f.write(m.sezione_html(sezione, scope) + '\n')

    # header e footer: template di tipo "section", importabili anche senza Elementor Pro
    for nodo, slug, titolo in ((header, '00-header', 'Benvegnu - Header'), (footer, '99-footer', 'Benvegnu - Footer')):
        with open(os.path.join(dirs['elementor-json'], f'bvg-{slug}.json'), 'w', encoding='utf-8') as f:
            f.write(m.json_dump(m.template_json(titolo, [nodo], kind='section')))
        scrivi_fallback(slug, f'01-{slug[3:]}', nodo, f'bvg-{slug[3:]}')
        problemi += controlla_testi(' '.join(testi_visibili(nodo)), slug)
        tutte_img += immagini(nodo)

    header_html = m.sezione_html(header, 'bvg-header', fonts=False)
    footer_html = m.sezione_html(footer, 'bvg-footer', fonts=False)

    for pg in c.PAGINE:
        sezioni = pg['sezioni']()
        for i, (nome, s) in enumerate(sezioni):
            m.assegna_id(s, f'bvg-{pg["slug"]}-{nome}')
        page_settings = {'template': 'elementor_header_footer', 'hide_title': 'yes'}
        tpl = m.template_json(f'Benvegnu - {pg["titolo"]}', [s for _, s in sezioni], kind='page', page_settings=page_settings)
        with open(os.path.join(dirs['elementor-json'], f'bvg-{pg["slug"]}.json'), 'w', encoding='utf-8') as f:
            f.write(m.json_dump(tpl))
        blocchi = [header_html]
        for i, (nome, s) in enumerate(sezioni, 1):
            scope = f'bvg-{pg["slug"][3:]}-{nome}'
            scrivi_fallback(pg['slug'], f'{i:02d}-{nome}', s, scope)
            blocchi.append(m.sezione_html(s, scope, fonts=False))
            problemi += controlla_testi(' '.join(testi_visibili(s)), f'{pg["slug"]}/{nome}')
            tutte_img += immagini(s)
        blocchi.append(footer_html)
        with open(os.path.join(dirs['anteprima'], f'{pg["slug"]}.html'), 'w', encoding='utf-8') as f:
            f.write(m.pagina_html(f'{pg["titolo_seo"]}', blocchi, pg.get('descrizione', '')))

    # la stessa verifica sui file scritti, per sicurezza
    for root, _, files in os.walk(a.out):
        if '_sorgente' in root or 'assets' in root or 'screenshot' in root:
            continue
        for fn in files:
            if fn.endswith(('.json', '.html')):
                txt = open(os.path.join(root, fn), encoding='utf-8').read()
                if '—' in txt or '\\u2014' in txt:
                    problemi.append(f'{fn}: trattino lungo nel file')

    if problemi:
        print('PROBLEMI:')
        print('\n'.join(sorted(set(problemi))))
        sys.exit(1)
    print(f'ok: {len(c.PAGINE) + 2} template, immagini referenziate: {len(tutte_img)} ({len(set(tutte_img))} diverse), nessun trattino lungo')


if __name__ == '__main__':
    main()
