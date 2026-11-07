# -*- coding: utf-8 -*-
"""
Contenuti del sito Gardens Pav S.r.l. (Legnaro, PD): tema, testata, piede e pagine.

Fonte dei testi: la home finale del 13 ottobre 2026 (_prova/home-finale/proto.html), che prende ogni dato da
01-analisi-sito-attuale.md; specifica completa in _prova/spec.md (token al paragrafo 2, testata e piede al 3, home al 5).
Ciò che non è verificabile è segnato nel LEGGIMI tra le cose da confermare.

Come è fatta una pagina: ogni sezione è un contenitore Elementor con widget gratuiti (Titolo, Testo, Immagine, HTML,
Shortcode). Le foto e i render stanno sempre in widget Immagine, così Elementor le scarica nella libreria media all'import.
Le griglie e i passaggi a 1340, 1100, 900 px (che Elementor non ha) vengono da classi gpv-* e da un foglio di stile che sta
nella testata (CSS_SITO) e in ogni sezione (CSS_<sezione>): le stesse regole valgono per il JSON di Elementor e per il
fallback HTML, perché i selettori puntano alle classi messe sugli elementi, non alla struttura interna di Elementor.
I disegni in sezione sono SVG scritti qui dai dati (nessun file da caricare) dentro widget HTML.
"""
import os
from urllib.parse import quote

import motore as m
from motore import C, H, T, I, RAW, SHORTCODE

QUI = os.path.dirname(os.path.abspath(__file__))
PREFISSO = 'gpv'
NOME_SITO = 'Gardens Pav'

# ---------------------------------------------------------------------------------------------
# Tema (specifica, paragrafo 2)
# ---------------------------------------------------------------------------------------------
CARTA = '#FFFFFF'         # fondo di quasi tutte le pagine
SCHEDA = '#F2F1EE'        # schede, riquadro del modulo, piede
SCHEDA_H = '#E6E4DE'      # scheda al passaggio, riga richiamata
LINEA = '#D9D7D0'         # filetti delle tabelle, bordo della testata, riga legale (decorativo)
CLS = '#CFD0CC'           # manufatti nei disegni in sezione
TERRA = '#F0ECE5'         # terreno a tratteggio, fondo delle didascalie sul terreno
TESTO = '#23221F'         # testo, titoli, bottone al passaggio (15,91:1 su bianco)
TESTO2 = '#57554F'        # testo secondario (7,45:1 su bianco, 6,60:1 su #F2F1EE)
ARANCIO = '#F38239'       # arancio del logo: tubi dei disegni, bottoni pieni, sottolineatura al passaggio; mai testo
BORDO_CAMPI = '#8A877F'   # bordo di campi e caselle (3,59:1 su bianco, 3,18:1 su #F2F1EE)
SEGNAPOSTO = '#6F6D67'    # testo d'esempio nei campi (5,17:1)
SOTTOLINEA = '#A9A79F'    # sottolineatura a riposo delle didascalie e di "Chiedi un'offerta"

OVERPASS = 'Overpass'
FONT_CSS = "'Overpass',Arial,sans-serif"


def _st(w, s, lh, ls=0.0):
    return dict(f=OVERPASS, w=w, s=s, lh=lh, ls=ls, up=False)


# scala tipografica (px a desktop, tablet, mobile); spaziatura in px per il desktop, in em nel CSS (classi gpv-tit*)
STILI = {
    'display':    _st('600', (52, 44, 31), 1.06, -1.04),
    'h1':         _st('600', (44, 38, 29), 1.08, -0.88),
    'h2':         _st('600', (40, 34, 27), 1.1, -0.6),
    'h2m':        _st('600', (34, 30, 25), 1.1, -0.51),
    'h2s':        _st('600', (30, 28, 24), 1.1, -0.45),
    'h3b':        _st('700', (22, 22, 19), 1.25),
    'h3':         _st('700', (19, 19, 17), 1.25),
    'h3p':        _st('700', (15, 15, 15), 1.25),
    'apertura':   _st('400', (18, 18, 16), 1.5),
    'body':       _st('400', (17, 17, 16), 1.55),
    'testo16':    _st('400', (16, 16, 15), 1.55),
    'recapiti':   _st('400', (16, 16, 16), 1.6),
    'nota':       _st('400', (15.5, 15.5, 15.5), 1.5),
    'small':      _st('400', (15, 15, 15), 1.5),
    'num':        _st('400', (15, 15, 14.5), 1.45),
    'didascalia': _st('400', (14, 14, 14), 1.4),
    'link':       _st('600', (14, 14, 14), 1.4),
    'tutti':      _st('600', (15, 15, 15), 1.3),
    'tel':        _st('700', (30, 30, 30), 1.15),
    'piede':      _st('400', (15, 15, 15), 1.8),
    'legale':     _st('400', (13.5, 13.5, 13.5), 1.55),
    'nav':        _st('600', (15, 15, 15), 1.2),
    'btn':        _st('700', (15, 15, 15), 1.2),
    'h3_motore':  _st('700', (19, 19, 17), 1.25),
}
STILI['h3x'] = STILI['h3']

# una sola scala: 4, 8, 12, 16, 24, 32, 48, 64, 88 (più il margine laterale della pagina, 40/32/16)
SPAZI = {
    '0':       (0, 0, 0),
    'micro':   (4, 4, 4),
    'xs':      (8, 8, 8),
    's':       (12, 12, 12),
    'm':       (16, 12, 8),
    'l':       (24, 24, 16),
    'xl':      (32, 32, 24),
    'xxl':     (48, 32, 32),
    'blocco':  (64, 64, 64),
    'sezione': (88, 88, 64),
    'lato':    (40, 32, 16),
}

TEMA = {
    'nome': 'Sezione',
    'fondo': CARTA, 'superficie': CARTA, 'inchiostro': TESTO, 'testo2': TESTO2, 'accento': ARANCIO,
    'filetto': LINEA, 'filetto_scuro': TESTO2, 'su_scuro2': SCHEDA,
    'scuro': TESTO, 'su_scuro': CARTA, 'su_accento': TESTO,
    'font_titoli': OVERPASS, 'font_testo': OVERPASS, 'larghezza': 1280,
    'google_fonts': 'https://fonts.googleapis.com/css2?family=Overpass:wght@400;600;700&display=swap',
    'stili': STILI,
    'spazi': SPAZI,
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): pieno arancio, al passaggio pieno grafite
    'bottoni': {'primario': (TESTO, ARANCIO, ARANCIO, CARTA, TESTO, TESTO)},
    'bottone': {'raggio': 2, 'pad': (12, 18, 12, 18), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)
m.STILI['h3'] = STILI['h3']       # il widget "Articoli" del motore usa 'h3' e 'small': restano nella scala

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/GardensPav-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (01, dati societari; un solo posto da aggiornare)
# ---------------------------------------------------------------------------------------------
NB = ' '                 # spazio indivisibile: numeri e unità, telefoni
WJ = '⁠'                 # word joiner: il trattino degli intervalli non va a capo


def R(a, b):
    return f'{a}{WJ}-{WJ}{b}'


TEL = f'049{NB}641591'
TEL_LINK = 'tel:+39049641591'
FAX = f'049{NB}641913'
EMAIL = 'info@gardenspav.it'
PEC = 'gardenspav@legalmail.it'
INDIRIZZO = f'Via Romea 154/A, 35020 Legnaro{NB}(PD)'
ORARI_BREVE = f'lun{WJ}-{WJ}ven {R(8, 12)} e {R(14, 18)}'          # [DA CONFERMARE: orari presi da Google]
ORARI = f'Da lunedì a venerdì, {R(8, 12)} e {R(14, 18)}.'
LEGALE = (f'Gardens Pav S.r.l., sede legale e operativa Via Romea 154/A, 35020 Legnaro (PD). P.IVA e C.F. 03963070283. '
          f'Registro Imprese di Padova, REA PD{WJ}-{WJ}351148. Capitale sociale 100.000 euro. PEC {PEC}')
OFFERTA = '/contatti/#richiesta'     # destinazione di "Chiedi un'offerta" fuori dalla home (lo script la adatta)

VOCI_MENU = [('Piattaforme per autolavaggi', '/piattaforme-autolavaggi/'), ('Vasche', '/vasche/'),
             ('Depurazione', '/depurazione/'), ('Realizzazioni', '/realizzazioni/'), ('Azienda', '/azienda/'),
             ('Contatti', '/contatti/')]


# ---------------------------------------------------------------------------------------------
# Foglio di stile comune (in tutti e due i formati: sta nella testata, che è su ogni pagina)
# ---------------------------------------------------------------------------------------------
CSS_SITO = (
    # carattere e numeri; nessun corsivo inventato dal browser
    f'.gpv-raw{{font-family:{FONT_CSS};color:{TESTO};font-synthesis:none;-webkit-font-smoothing:antialiased}}'
    '.gpv-raw *,.gpv-raw *::before,.gpv-raw *::after{box-sizing:border-box}'
    '.gpv-raw h2,.gpv-raw h3,.gpv-raw p,.gpv-raw ul,.gpv-raw ol,.gpv-raw figure,figure.gpv-raw{margin:0;padding:0}'
    '.gpv-raw figcaption,figure.gpv-raw figcaption{font-style:normal}'
    '.gpv-raw ul,.gpv-raw ol{list-style:none}'
    'em,i,cite{font-style:normal}'
    'html{scroll-padding-top:96px}'
    '@media (max-width:767px){html{scroll-padding-top:80px}body{padding-bottom:64px}}'
    '@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'
    # titoli: spaziatura in em (Elementor la scrive in px uguale su tutti i formati), a capo bilanciato
    '.gpv-tit .elementor-heading-title,.gpv-w.gpv-tit{letter-spacing:-.015em!important}'
    '.gpv-tit-d .elementor-heading-title,.gpv-w.gpv-tit-d{letter-spacing:-.02em!important}'
    '@media (max-width:767px){.gpv-tit-d .elementor-heading-title,.gpv-w.gpv-tit-d{line-height:1.1!important}}'
    '.elementor-heading-title{text-wrap:balance}.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-bottom:0!important;margin-block-end:0!important}'
    # cifre tabellari dove ci sono misure, pesi e orari
    '.gpv-cifre,.gpv-cifre p,.gpv-cifre .elementor-heading-title{font-variant-numeric:tabular-nums lining-nums}'
    # link nel testo: grafite, sottolineatura 1 px; al passaggio arancio da 2 px (mai testo arancio)
    f'a.gpv-a{{color:{TESTO}!important;text-decoration:underline!important;text-decoration-thickness:1px!important;'
    'text-underline-offset:3px!important}'
    f'a.gpv-a:hover{{text-decoration-color:{ARANCIO}!important;text-decoration-thickness:2px!important}}'
    f'a.gpv-tutti{{color:{TESTO}!important;font-weight:600;white-space:nowrap;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:4px!important}'
    f'a.gpv-tutti:hover{{text-decoration-color:{ARANCIO}!important;text-decoration-thickness:2px!important}}'
    f'a.gpv-chiedi{{color:{TESTO}!important;text-decoration:underline!important;text-decoration-color:{SOTTOLINEA}!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:3px!important}'
    f'a.gpv-chiedi:hover{{text-decoration-color:{ARANCIO}!important;text-decoration-thickness:2px!important}}'
    f'a.gpv-pl{{color:{TESTO}!important;text-decoration:none!important}}'
    f'a.gpv-pl:hover{{text-decoration:underline!important;text-decoration-color:{ARANCIO}!important;text-underline-offset:3px!important}}'
    f'a.gpv-a:focus-visible,a.gpv-tutti:focus-visible,a.gpv-chiedi:focus-visible,a.gpv-pl:focus-visible,'
    f'.gpv-raw a:focus-visible,.gpv-raw button:focus-visible,.gpv-raw summary:focus-visible,.gpv-raw input:focus-visible,'
    f'.gpv-raw select:focus-visible,.gpv-raw textarea:focus-visible,.gpv-modulo input:focus-visible,.gpv-modulo select:focus-visible,'
    f'.gpv-modulo textarea:focus-visible,.gpv-modulo button:focus-visible,.gpv-logo a:focus-visible'
    f'{{outline:2px solid {TESTO}!important;outline-offset:2px}}'
    # bottone pieno: arancio con testo grafite, al passaggio grafite con testo bianco; mai opacità
    f'.gpv-btn,a.gpv-btn,button.gpv-btn,input.gpv-btn{{display:inline-block;background:{ARANCIO}!important;color:{TESTO}!important;'
    f'font:700 15px/1.2 {FONT_CSS};text-decoration:none!important;padding:12px 18px;border:0!important;border-radius:2px!important;'
    'white-space:nowrap;cursor:pointer;box-shadow:none!important;text-transform:none;letter-spacing:0}'
    f'.gpv-btn:hover,.gpv-btn:focus-visible,a.gpv-btn:hover,button.gpv-btn:hover,input.gpv-btn:hover{{background:{TESTO}!important;color:{CARTA}!important}}'
    f'.gpv-btn:disabled,.gpv-btn[disabled]{{background:{SCHEDA_H}!important;color:{TESTO2}!important;cursor:progress}}'
    # schede cliccabili: un solo link (sul titolo) che copre la scheda; "Chiedi un'offerta" sta sopra
    '.gpv-scheda{position:relative;transition:none!important}'
    f'.gpv-scheda:hover{{background-color:{SCHEDA_H}!important}}'
    '.gpv-scheda .elementor-widget{position:static}'
    f'.gpv-scheda h3 a{{color:{TESTO}!important;text-decoration:none!important}}'
    '.gpv-scheda h3 a::after{content:"";position:absolute;inset:0;z-index:0}'
    '.gpv-scheda h3 a:focus-visible{outline:0}'
    f'.gpv-scheda:has(h3 a:focus-visible){{outline:2px solid {TESTO};outline-offset:2px}}'
    '.gpv-scheda .gpv-s-chiedi{position:relative;z-index:1;align-self:flex-start}'
    '.gpv-s-sotto p{min-height:2.8em}'
    '.gpv-s-num{margin-top:auto!important}'
    '.gpv-s-img img{width:100%;height:auto;display:block}'
    # griglie (Elementor non ha i passaggi a 1100 e 900 px)
    '.gpv-g4.gpv-g4{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px!important}'
    '.gpv-g4 > *{width:auto!important;max-width:none!important;min-width:0}'
    '@media (max-width:1100px){.gpv-g4.gpv-g4{gap:12px!important}}'
    '@media (max-width:900px){.gpv-g4.gpv-g4{grid-template-columns:repeat(2,minmax(0,1fr))}}'
    '@media (max-width:767px){.gpv-g4.gpv-g4{gap:8px!important}.gpv-g4.gpv-schede{grid-template-columns:1fr}}'
    # scheda di famiglia: padding 24/24/16 (16 sotto 1100); sotto 900 è una riga con l'immagine di 116 px a sinistra
    '.gpv-scheda.gpv-scheda{padding:24px 24px 16px!important}'
    '@media (max-width:1100px){.gpv-scheda.gpv-scheda{padding:16px 16px 16px!important}}'
    '@media (max-width:900px){'
    '.gpv-scheda.gpv-scheda{display:grid!important;grid-template-columns:116px minmax(0,1fr);'
    'grid-template-areas:"img nome" "img sotto" "img num" "img chiedi";column-gap:16px!important;row-gap:0!important;align-content:start;'
    'padding:12px 12px 12px 8px!important}'
    '.gpv-s-nome{grid-area:nome}.gpv-s-sotto{grid-area:sotto;margin-top:4px!important}'
    '.gpv-s-img{grid-area:img;align-self:center;margin:0!important}'
    '.gpv-s-num{grid-area:num;margin-top:8px!important}.gpv-s-chiedi{grid-area:chiedi;margin-top:8px!important}'
    '.gpv-s-sotto p{min-height:0}'
    '.gpv-s-nome .elementor-heading-title,.gpv-w.gpv-s-nome{font-size:17px!important}'
    # Elementor scrive l'interlinea in em sul contenitore del widget: la riscrivo insieme al corpo
    '.gpv-s-sotto p{font-size:13.5px!important;line-height:1.4!important}.gpv-s-num p{font-size:14.5px!important;line-height:1.45!important}}'
    # testata di sezione: titolo e testo nella stessa colonna, il link in basso a destra
    '.gpv-testa-t{max-width:782px}'
    # didascalie delle foto
    '.gpv-fig img{width:100%;height:auto;display:block}'
    # contorno dei campi di Contact Form 7 e del fallback: stessi stili (vedi CSS_MODULO)
)

# ---------------------------------------------------------------------------------------------
# Componenti riutilizzabili (home e pagine interne)
# ---------------------------------------------------------------------------------------------


def testo(html, stile='body', colore=TESTO, **p):
    """Widget Testo: link grafite anche al passaggio (l'arancio non è mai colore di testo)."""
    return T(html, style=stile, color=colore, link_color=TESTO, link_hover=TESTO, **p)


def titolo(t, livello='h2', stile='h2', **p):
    classi = 'gpv-tit-d' if stile in ('display', 'h1') else ('gpv-tit' if stile.startswith('h2') else '')
    css = (classi + ' ' + p.pop('css', '')).strip()
    return H(t, livello, style=stile, color=TESTO, **({'css': css} if css else {}), **p)


def sezione(*figli, pad=('sezione', 'lato', '0', 'lato'), anchor=None, css='', **p):
    """Fascia di pagina: fondo bianco, contenuto largo 1280 (boxed), spazio sopra dalla scala."""
    return C(*figli, pad=pad, tag='section', bg=CARTA, anchor=anchor, css=('gpv-sez ' + css).strip(), gap='0', **p)


def testa(titolo_testo, frase, link=None, stile='h2', livello='h2', **p):
    """Testata di sezione: titolo e frase nella stessa colonna, link "Tutte le ..." in basso a destra."""
    col = C(titolo(titolo_testo, livello, stile), testo(f'<p>{frase}</p>', colore=TESTO2, mt='xs', max_w=782),
            grow=True, gap='0', css='gpv-testa-t')
    figli = [col]
    if link:
        figli.append(testo(f'<p><a class="gpv-tutti" href="{link[1]}">{link[0]}</a></p>', stile='tutti', fisso=True))
    return C(*figli, dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap=('xxl', 'xl', 's'),
             mb='l', css='gpv-testa', **p)


def chiedi(prodotto, ancora='#contatti', base=''):
    """Link "Chiedi un'offerta" che porta al modulo con il prodotto già scelto (data-prodotto per lo script)."""
    return (f'<p><a class="gpv-chiedi" href="{base}?prodotto={quote(prodotto)}{ancora}" data-prodotto="{prodotto}" '
            f'aria-label="Chiedi un’offerta: {prodotto[0].lower() + prodotto[1:] if not prodotto.startswith(("Depuratori", "Dissabbiatore")) else prodotto}">'
            'Chiedi un’offerta</a></p>')


def scheda_famiglia(foto, nome, sotto, numeri, href, alt, prodotto, ancora='#contatti', base=''):
    """Scheda di famiglia (specifica 2.6.1): nome che porta alla scheda, sottoprodotti, render, due righe di numeri veri,
    "Chiedi un'offerta". Il fondo cambia al passaggio; il link del titolo copre tutta la scheda."""
    return C(
        titolo(nome, 'h3', 'h3', link=href, css='gpv-s-nome'),
        testo(f'<p>{sotto}</p>', 'didascalia', TESTO2, css='gpv-s-sotto', mt='xs'),
        I(img(foto), alt, css='gpv-s-img', mt='s', mb='s'),
        testo(f'<p>{numeri[0]}<br>{numeri[1]}</p>', 'num', css='gpv-s-num gpv-cifre'),
        testo(chiedi(prodotto, ancora, base), 'link', css='gpv-s-chiedi', mt='s'),
        bg=SCHEDA, pad=('l', 'l', 'm', 'l'), gap='0', css='gpv-scheda')


def griglia(*figli, css='', **p):
    """Griglia a 4 colonne (2 sotto 900 px, 1 o 2 a mobile secondo la classe): CSS grid dalla classe gpv-g4."""
    return C(*figli, gap='m', css=('gpv-g4 ' + css).strip(), **p)


def figura(foto, alt, didascalia, css='', **p):
    """Foto con didascalia sotto (14 px, testo secondario)."""
    return C(I(img(foto), alt), testo(f'<p>{didascalia}</p>', 'didascalia', TESTO2, mt='xs'), gap='0',
             css=('gpv-fig ' + css).strip(), **p)


# ---------------------------------------------------------------------------------------------
# Testata e piede (Ultimate Addons for Elementor: template "Header" e "Footer", su tutto il sito)
# ---------------------------------------------------------------------------------------------
CSS_TESTATA = (
    # la testata resta in alto: in WordPress è il <header id="masthead"> di Ultimate Addons, nel fallback la sezione
    f'#masthead,.gpv-header{{position:sticky;top:0;z-index:40;background:{CARTA}}}'
    '.gpv-testata{overflow-x:clip}'
    'a.hfe-skip-link{display:none!important}'
    '.gpv-salta{position:absolute;left:-9999px;top:8px;z-index:50;padding:8px 12px;background:#FFFFFF;'
    f'color:{TESTO}!important;font:600 15px/1.2 {FONT_CSS};text-decoration:underline}}'
    '.gpv-salta:focus{left:8px}'
    '.gpv-logo img{display:block;width:172px;height:auto}'
    '.gpv-nav{display:flex;align-items:center;gap:32px;width:100%}'
    '.gpv-menu{display:flex;gap:24px;margin-right:auto}'
    f'.gpv-menu a{{font:600 15px/1.2 {FONT_CSS};color:{TESTO}!important;text-decoration:none!important;white-space:nowrap;'
    'padding:6px 0;border-bottom:2px solid transparent}'
    f'.gpv-menu a:hover{{border-bottom-color:{ARANCIO}}}'
    f'.gpv-menu a[aria-current=page]{{border-bottom-color:{TESTO}}}'
    f'.gpv-menu a[aria-current=page]:hover{{border-bottom-color:{ARANCIO}}}'
    f'.gpv-tel{{display:flex;flex-direction:column;text-decoration:none!important;line-height:1.2;white-space:nowrap;color:{TESTO}!important}}'
    '.gpv-tel b{font-weight:700;font-size:19px;font-variant-numeric:tabular-nums}'
    f'.gpv-tel span{{font-size:13px;color:{TESTO2}}}'
    f'.gpv-tel:hover b{{text-decoration:underline;text-decoration-color:{ARANCIO};text-decoration-thickness:2px;text-underline-offset:3px}}'
    '.gpv-hamb{display:none;position:relative}'
    f'.gpv-hamb summary{{list-style:none;cursor:pointer;font:700 15px/1.2 {FONT_CSS};color:{TESTO};padding:10px 12px;'
    f'border:1px solid {TESTO};border-radius:2px}}'
    '.gpv-hamb summary::-webkit-details-marker{display:none}'
    f'.gpv-hamb[open] summary{{background:{TESTO};color:#FFFFFF}}'
    f'.gpv-tendina{{position:absolute;right:0;top:calc(100% + 13px);background:#FFFFFF;border:1px solid {LINEA};'
    'width:300px;max-width:calc(100vw - 32px);padding:8px 0 16px;box-shadow:0 8px 24px rgba(35,34,31,.12);z-index:45}'
    f'.gpv-tendina nav a{{display:block;padding:10px 18px;font:600 15px/1.35 {FONT_CSS};color:{TESTO}!important;text-decoration:none!important}}'
    f'.gpv-tendina nav a:hover{{background:{SCHEDA}}}'
    f'.gpv-tendina nav a[aria-current=page]{{font-weight:700;background:{SCHEDA}}}'
    '.gpv-cerca{display:flex;margin:12px 18px 0;position:relative}'
    '.gpv-cerca label{position:absolute;left:-9999px}'
    f'.gpv-cerca input{{flex:1;min-width:0;height:42px;border:1px solid {BORDO_CAMPI};border-right:0;border-radius:2px 0 0 2px;'
    f'padding:0 12px;font:400 16px/1.2 {FONT_CSS};color:{TESTO};background:#FFFFFF;margin:0}}'
    f'.gpv-cerca input::placeholder{{color:{SEGNAPOSTO};opacity:1}}'
    f'.gpv-cerca button{{height:42px;padding:0 14px;border:1px solid {TESTO};background:{TESTO};color:#FFFFFF;'
    f'font:700 15px/1 {FONT_CSS};border-radius:0 2px 2px 0;cursor:pointer;margin:0}}'
    f'.gpv-cerca button:hover{{background:{ARANCIO};border-color:{ARANCIO};color:{TESTO}}}'
    '@media (max-width:1340px){.gpv-menu{display:none}.gpv-hamb{display:block}.gpv-tel{margin-left:auto}}'
    '@media (max-width:767px){.gpv-logo img{width:136px}.gpv-nav{gap:12px}.gpv-tel span{display:none}.gpv-tel b{font-size:16px}'
    '.gpv-btn--testata{display:none!important}.gpv-hamb summary{padding:8px 10px;font-size:14px}.gpv-tendina{right:-4px}}'
)

# voce attiva (una per pagina, dall'indirizzo); tendina chiusa con Esc e con un clic fuori; "Chiedi un'offerta" porta
# al modulo della pagina se c'è (home: #contatti, Contatti: #richiesta), altrimenti a /contatti/#richiesta
JS_TESTATA = (
    "(function(){var p=location.pathname.replace(/index\\.html$/,'');"
    "var file=p.split('/').pop();"
    "document.querySelectorAll('.gpv-menu a,.gpv-tendina nav a').forEach(function(a){"
    "var h=a.getAttribute('href');if(h===p||(file&&a.pathname.split('/').pop()===file&&file.indexOf('.html')>0))a.setAttribute('aria-current','page')});"
    "var qui=document.getElementById('contatti')?'#contatti':(document.getElementById('richiesta')?'#richiesta':null);"
    "if(qui)document.querySelectorAll('a.gpv-offerta').forEach(function(a){a.setAttribute('href',qui)});"
    "var d=document.querySelector('.gpv-hamb');if(!d)return;"
    "document.addEventListener('keydown',function(e){if(e.key==='Escape'&&d.open){d.open=false;d.querySelector('summary').focus()}});"
    "document.addEventListener('click',function(e){if(d.open&&!d.contains(e.target))d.open=false})})();"
)


def nav_html():
    voci = ''.join(f'<a href="{u}">{t}</a>' for t, u in VOCI_MENU)
    return (
        '<div class="gpv-raw gpv-nav">'
        f'<nav class="gpv-menu" aria-label="Menu principale">{voci}</nav>'
        f'<a class="gpv-tel" href="{TEL_LINK}"><b>{TEL}</b><span>Ufficio tecnico, {ORARI_BREVE}</span></a>'
        f'<a class="gpv-btn gpv-btn--testata gpv-offerta" href="{OFFERTA}">Chiedi un’offerta</a>'
        '<details class="gpv-hamb"><summary>Menu</summary><div class="gpv-tendina">'
        f'<nav aria-label="Menu principale, versione compatta">{voci}</nav>'
        '<form class="gpv-cerca" action="/" method="get" role="search">'
        '<label for="gpv-cerca-t">Cerca per nome o taglia</label>'
        '<input id="gpv-cerca-t" name="s" type="search" placeholder="Nome o taglia" autocomplete="off">'
        '<button type="submit">Cerca</button></form></div></details>'
        f'</div><script>{JS_TESTATA}</script>'
    )


def header():
    logo = I(img('logo-gardens-pav.png'), 'Gardens Pav, opere in calcestruzzo', link='/', w_img=(172, 172, 136), fisso=True,
             css='gpv-logo', link_label='Gardens Pav, pagina iniziale')
    riga = C(logo, RAW(nav_html(), grow=True), dir='row', align='center', gap=('xl', 'xl', 's'), min_h=(76, 76, 62),
             pad=('0', 'lato'), boxed=True)
    # il link "Vai al contenuto" e il foglio di stile stanno fuori dalla riga: non occupano posto tra logo e menu
    salta = RAW('<a class="gpv-salta" href="#contenuto">Vai al contenuto</a>', css=CSS_SITO + CSS_TESTATA)
    return C(salta, riga, pad='0', boxed=False, gap='0', bg=CARTA, border_bottom=1, border_color=LINEA, css='gpv-testata')


CSS_PIEDE = (
    '.gpv-piede-in.gpv-piede-in{display:grid!important;grid-template-columns:minmax(0,4fr) minmax(0,3fr) minmax(0,2fr) minmax(0,3fr);'
    'gap:48px!important}'
    '.gpv-piede-in > *{width:auto!important;min-width:0}'
    '@media (max-width:1100px){.gpv-piede-in.gpv-piede-in{grid-template-columns:1fr 1fr;gap:32px 48px!important}}'
    '@media (max-width:767px){.gpv-piede-in.gpv-piede-in{grid-template-columns:1fr;gap:24px!important}}'
    '.gpv-piede .gpv-logo img{width:172px}'
    # barra del telefono in basso, fino a 767 px
    '.gpv-barra{display:none}'
    '@media (max-width:767px){.gpv-barra{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:35;background:#FFFFFF;'
    f'border-top:1px solid {LINEA};padding:8px 12px;gap:8px}}'
    f'.gpv-barra a{{flex:1;text-align:center;font:700 15px/1.2 {FONT_CSS};text-decoration:none!important;padding:11px 8px;'
    f'border-radius:2px;color:{TESTO}!important}}'
    f'.gpv-barra a:first-child{{border:1px solid {TESTO}}}'
    f'.gpv-barra a:last-child{{background:{ARANCIO};border:1px solid {ARANCIO}}}'
    f'.gpv-barra a:hover{{background:{TESTO};border-color:{TESTO};color:#FFFFFF!important}}}}'
)


def footer():
    def colonna(nome, righe):
        return C(titolo(nome, 'h3', 'h3p', mb='xs'),
                 testo('<p>' + '<br>'.join(righe) + '</p>', 'piede', css='gpv-cifre'), gap='0')
    pl = lambda t, u: f'<a class="gpv-pl" href="{u}">{t}</a>'
    marchio = C(I(img('logo-gardens-pav.png'), 'Gardens Pav, opere in calcestruzzo', link='/', w_img=(172, 172, 172),
                  css='gpv-logo', link_label='Gardens Pav, pagina iniziale'),
                testo('<p>Manufatti in calcestruzzo armato vibrato per il trattamento delle acque e piattaforme prefabbricate per '
                      'autolavaggi, da Legnaro (PD).</p>', 'small', TESTO2, mt='s'), gap='0')
    colonne = C(
        marchio,
        colonna('Prodotti', [pl('Piattaforme per autolavaggi', '/piattaforme-autolavaggi/'), pl('Vasche monoblocco', '/vasche/'),
                             pl('Depurazione', '/depurazione/'), pl('Realizzazioni', '/realizzazioni/')]),
        colonna('Azienda', [pl('Chi siamo', '/azienda/'), pl('Contatti', '/contatti/'), pl('Privacy', '/privacy/'),
                            pl('Cookie', '/cookie/')]),
        colonna('Ufficio tecnico', [pl(TEL, TEL_LINK), ORARI_BREVE, pl(EMAIL, f'mailto:{EMAIL}')]),
        gap='xxl', css='gpv-piede-in')
    legale = C(testo(f'<p>{LEGALE}</p>', 'legale', TESTO2), border_top=1, border_color=LINEA, pad=('m', '0', '0', '0'), mt='xl')
    barra = RAW(f'<div class="gpv-raw gpv-barra"><a href="{TEL_LINK}">Chiama {TEL}</a>'
                f'<a class="gpv-offerta" href="{OFFERTA}">Chiedi un’offerta</a></div>', css=CSS_PIEDE)
    return C(colonne, legale, barra, pad=(48, 'lato', 32, 'lato'), bg=SCHEDA, tag='footer', gap='0', css='gpv-piede')


# ---------------------------------------------------------------------------------------------
# Disegno in sezione del piazzale (home, H1): SVG scritto dai dati, unità del viewBox = centimetri.
# Le didascalie sopra terra stanno in una fascia HTML alta 170 px (160 sotto 1340, 195 sotto 1180); i loro richiami
# sono elementi HTML dentro il riquadro del disegno (altezza in px fino alla fascia più una percentuale fino al pezzo).
# Sotto i 1025 px il disegno si divide in due figure intere, ognuna con le sue voci in elenco.
# ---------------------------------------------------------------------------------------------
SX0, SW = -40, 1350              # x da -40 a 1310 cm
SYT, S_TERRA = -16, 236          # da 16 cm sopra il piano di campagna al fondo del terreno
SYB = S_TERRA + 2
SH = SYB - SYT                   # 254 cm
NS = 'vector-effect="non-scaling-stroke"'

# (chiave, x della linea, y del pezzo, riga, allineamento, larghezza %, nome, dato, link)
SEZ_FASCIA = [
    ('a', 40, 10, 1, 'l', 30.8, f'Piattaforma per pista self Mod.{NB}450',
     f'450×650{NB}cm, 2{NB}pannelli da 5,90{NB}t, spessore 20{NB}cm', '/piattaforme-autolavaggi/#mod-450'),
    ('b', 480, 2, 1, 'l', 23.5, 'Grigliato in vetroresina PRFV',
     f'moduli 200×100{NB}cm, antiscivolo al quarzo', '/piattaforme-autolavaggi/#fornitura'),
    ('f', 1170, 8, 1, 'r', 23.5, 'Separatore oli con filtro a coalescenza',
     f'da 3 a 30{NB}l/s, UNI{NB}EN{NB}858-1; scarico in acque superficiali, Tab.{NB}3, All.{NB}5, D.Lgs.{NB}152/2006',
     '/depurazione/#separatore-oli'),
    ('d', 170, 7, 2, 'l', 21.2, 'Supporti portagriglia',
     'acciaio zincato, staffe e viti inox, giuntoplasto sul bordo della vasca', '/piattaforme-autolavaggi/#fornitura'),
    ('e', 560, 10, 2, 'l', 21.9, 'Tubazioni predisposte',
     'dentro i pannelli, per pluviali, lance e cavi elettrici', '/piattaforme-autolavaggi/#fornitura'),
    ('c', 880, 8, 2, 'l', 19.7, 'Dissabbiatore statico',
     f'da Ø{NB}148×206{NB}h, 2,30{NB}m³: sabbie e fanghi restano sul fondo', '/depurazione/#dissabbiatore'),
]
# (chiave, x, y del pezzo, y del bordo alto della didascalia, larghezza %, nome, dato, link, escluso)
SEZ_TERRENO = [
    ('h', 330, 124, 146, 26.0, 'Vasca sottopista', f'400×100×110{NB}h, compresa con la piattaforma',
     '/piattaforme-autolavaggi/#mod-450', False),
    ('g', 590, 30, 54, 13.3, 'Opere edili, escluse', f'scavo, pietrisco 4/8 da 20{NB}cm, cordolo perimetrale e magrone',
     '/piattaforme-autolavaggi/#fornitura', True),
]


def _px(x):
    return f'{(x - SX0) / SW * 100:.3f}%'


def _py(y):
    return f'{(y - SYT) / SH * 100:.3f}%'


def svg_sezione(vista, richiami, etichetta, idp):
    """Il piazzale in sezione: pista self Mod. 450 sul pietrisco, vasca sottopista, dissabbiatore, separatore oli.
    idp: prefisso degli id dei motivi (ogni SVG nella pagina ha i suoi: uno nascosto non deve togliere i motivi all'altro)."""
    vx0, vx1 = vista
    vw = vx1 - vx0
    L = []
    a = L.append
    a(f'<svg class="gpv-sez-svg" viewBox="{vx0} {SYT} {vw} {SH}" width="{vw}" height="{SH}" role="img" aria-label="{etichetta}" '
      'xmlns="http://www.w3.org/2000/svg">')
    a('<defs>'
      f'<pattern id="{idp}-terra" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'
      f'<rect width="14" height="14" fill="{TERRA}"/><line x1="0" y1="0" x2="0" y2="14" stroke="#D6CDBD" stroke-width="1.6"/></pattern>'
      f'<pattern id="{idp}-pietrisco" width="9" height="9" patternUnits="userSpaceOnUse">'
      '<rect width="9" height="9" fill="#E7E3DA"/><circle cx="2" cy="2.5" r="1.3" fill="#8F897D"/>'
      '<circle cx="6.5" cy="6.5" r="1.1" fill="#8F897D"/></pattern>'
      f'<pattern id="{idp}-opere" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
      '<rect width="6" height="6" fill="#E2DFD8"/><line x1="0" y1="0" x2="0" y2="6" stroke="#8E897E" stroke-width="1.6"/></pattern>'
      '</defs>')
    a(f'<rect x="{vx0}" y="0" width="{vw}" height="{S_TERRA}" fill="url(#{idp}-terra)"/>')
    a(f'<line x1="{vx0}" y1="{S_TERRA}" x2="{vx1}" y2="{S_TERRA}" stroke="#C9BFAE" stroke-width="1" {NS}/>')
    # opere edili: pietrisco sotto i pannelli, cordoli, magrone sotto la vasca
    a(f'<rect x="25" y="20" width="600" height="20" fill="url(#{idp}-pietrisco)" stroke="#6E6A61" stroke-width="1" {NS}/>')
    a(f'<rect x="0" y="20" width="25" height="26" fill="url(#{idp}-opere)" stroke="#6E6A61" stroke-width="1" {NS}/>')
    a(f'<rect x="625" y="20" width="25" height="26" fill="url(#{idp}-opere)" stroke="#6E6A61" stroke-width="1" {NS}/>')
    a(f'<rect x="113" y="130" width="424" height="11" fill="url(#{idp}-opere)" stroke="#6E6A61" stroke-width="1" {NS}/>')
    # vasca sottopista 400 x 100 x 110 h con l'acqua sul fondo, grigliato e supporti
    a(f'<path d="M125 20 H525 V130 H125 Z M137 20 V118 H513 V20 Z" fill-rule="evenodd" fill="{CLS}" stroke="#3E3D39" stroke-width="1.2" {NS}/>')
    a('<rect x="137" y="20" width="376" height="98" fill="#FFFFFF"/>')
    a('<rect x="137" y="102" width="376" height="16" fill="#DCE4E5"/>')
    a(f'<line x1="137" y1="102" x2="513" y2="102" stroke="#8FA3A8" stroke-width="1" {NS}/>')
    a(f'<rect x="137" y="0" width="376" height="20" fill="#F0F0EE" stroke="#A9A9A4" stroke-width="1" stroke-dasharray="4 3" {NS}/>')
    for x in (167, 257, 347, 437):
        a(f'<rect x="{x}" y="4" width="6" height="6" fill="#A7ACAE" stroke="#3E3D39" stroke-width="1" {NS}/>')
    a(f'<rect x="137" y="0" width="376" height="4" fill="#3E8A5C" stroke="#1F4A31" stroke-width="1" {NS}/>')
    for x0, x1 in ((0, 137), (513, 650)):
        a(f'<rect x="{x0}" y="0" width="{x1 - x0}" height="20" fill="{CLS}" stroke="#3E3D39" stroke-width="1.2" {NS}/>')
    a(f'<circle cx="560" cy="10" r="6.5" fill="{ARANCIO}" stroke="#3E3D39" stroke-width="1" {NS}/>')

    def tubo(punti, w=10):
        d = 'M' + ' L'.join(f'{x} {y}' for x, y in punti)
        a(f'<path d="{d}" fill="none" stroke="#7A3E14" stroke-width="{w + 2.4}" stroke-linejoin="round"/>')
        a(f'<path d="{d}" fill="none" stroke="{ARANCIO}" stroke-width="{w}" stroke-linejoin="round"/>')

    def pozzo(x):
        a(f'<path d="M{x} 20 H{x + 148} V226 H{x} Z M{x + 12} 20 V211 H{x + 136} V20 Z" fill-rule="evenodd" '
          f'fill="{CLS}" stroke="#3E3D39" stroke-width="1.2" {NS}/>')
        a(f'<rect x="{x + 12}" y="20" width="124" height="191" fill="#FFFFFF"/>')
        a(f'<rect x="{x}" y="0" width="148" height="20" fill="{CLS}" stroke="#3E3D39" stroke-width="1.2" {NS}/>')
        a(f'<rect x="{x + 56}" y="0" width="36" height="3.5" fill="#5F5E59"/>')

    tubo([(519, 108), (802, 114)])
    xd = 790                                   # dissabbiatore statico Ø 148 x 206 h: sabbie sul fondo
    pozzo(xd)
    a(f'<rect x="{xd + 12}" y="112" width="124" height="99" fill="#DCE4E5"/>')
    a(f'<line x1="{xd + 12}" y1="112" x2="{xd + 136}" y2="112" stroke="#8FA3A8" stroke-width="1" {NS}/>')
    a(f'<path d="M{xd + 12} 211 V193 C{xd + 40} 186 {xd + 70} 197 {xd + 100} 189 S{xd + 128} 186 {xd + 136} 190 V211 Z" fill="#C7B597"/>')
    tubo([(xd, 114), (xd + 30, 114), (xd + 30, 160)])
    tubo([(xd + 136, 122), (1052, 128)])
    xs = 1040                                  # separatore oli con filtro a coalescenza
    pozzo(xs)
    a(f'<rect x="{xs + 12}" y="120" width="124" height="91" fill="#DCE4E5"/>')
    a(f'<rect x="{xs + 12}" y="120" width="124" height="5" fill="#8C7647"/>')
    tubo([(xs, 128), (xs + 26, 128), (xs + 26, 165)])
    a(f'<rect x="{xs + 70}" y="136" width="40" height="60" fill="#EEF2F3" stroke="#3E3D39" stroke-width="1" {NS}/>')
    for k in range(1, 6):
        a(f'<line x1="{xs + 70 + k * 6.7:.1f}" y1="136" x2="{xs + 70 + k * 6.7:.1f}" y2="196" stroke="#7E8C92" stroke-width="1" {NS}/>')
    tubo([(xs + 136, 134), (1320, 140)])
    a(f'<line x1="{vx0}" y1="0" x2="{vx1}" y2="0" stroke="{TESTO}" stroke-width="1.5" {NS}/>')
    if richiami:
        for k, x, y, top, *_ in SEZ_TERRENO:
            a(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{top}" stroke="{TESTO}" stroke-width="1" {NS}/>')
        for k, x, y, *_ in SEZ_FASCIA + SEZ_TERRENO:
            a(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{TESTO}" stroke="#FFFFFF" stroke-width="1" {NS}/>')
    a('</svg>')
    return ''.join(L)


def _voce(nome, dato, href, escl, cls):
    return (f'<a class="{cls}{" " + cls + "--escl" if escl else ""}" href="{href}"><span class="gpv-dida-n">{nome}</span>'
            f'<span class="gpv-dida-d">{dato}</span></a>')


def html_sezione():
    fascia, richiami, terreno = [], [], []
    for k, x, y, riga, al, larg, nome, dato, href in SEZ_FASCIA:
        pos = f'left:{_px(x)};' if al == 'l' else f'right:{(SX0 + SW - x) / SW * 100:.3f}%;'
        cls = f'gpv-dida gpv-dida--r{riga}' + (' gpv-dida--dx' if al == 'r' else '')
        fascia.append(f'<a class="{cls}" style="{pos}max-width:{larg}%" href="{href}"><span class="gpv-dida-n">{nome}</span>'
                      f'<span class="gpv-dida-d">{dato}</span></a>')
        richiami.append(f'<span class="gpv-richiamo gpv-richiamo--r{riga}" style="left:{_px(x)};--y:{_py(y)}" aria-hidden="true"></span>')
    for k, x, y, top, larg, nome, dato, href, escl in SEZ_TERRENO:
        dx = k == 'h'      # la vasca sottopista ha a sinistra tutto il terreno libero: didascalia allineata a destra
        cls = 'gpv-dida gpv-dida--t' + (' gpv-dida--escl' if escl else '') + (' gpv-dida--tdx' if dx else '')
        pos = f'right:{(SX0 + SW - x) / SW * 100:.3f}%;' if dx else f'left:{_px(x)};'
        terreno.append(f'<a class="{cls}" style="{pos}top:{_py(top)};max-width:{larg}%" href="{href}">'
                       f'<span class="gpv-dida-n">{nome}</span><span class="gpv-dida-d">{dato}</span></a>')
    voci = {d[0]: (d[6], d[7], d[8], False) for d in SEZ_FASCIA}
    voci.update({d[0]: (d[5], d[6], d[7], d[8]) for d in SEZ_TERRENO})

    def lista(chiavi):
        return ''.join(f'<li>{_voce(*voci[k], "gpv-voce")}</li>' for k in chiavi)

    sw_opere = ('<svg class="gpv-sw" viewBox="0 0 16 16" aria-hidden="true"><defs><pattern id="gpv-sw-opere" width="4" height="4" '
                'patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="4" height="4" fill="#E2DFD8"/>'
                '<line x1="0" y1="0" x2="0" y2="4" stroke="#8E897E" stroke-width="1.3"/></pattern></defs>'
                '<rect x=".5" y=".5" width="15" height="15" fill="url(#gpv-sw-opere)" stroke="#6E6A61"/></svg>')
    sw_terra = ('<svg class="gpv-sw" viewBox="0 0 16 16" aria-hidden="true"><defs><pattern id="gpv-sw-terra" width="6" height="6" '
                f'patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="6" height="6" fill="{TERRA}"/>'
                '<line x1="0" y1="0" x2="0" y2="6" stroke="#C9BFAE" stroke-width="1.2"/></pattern></defs>'
                '<rect x=".5" y=".5" width="15" height="15" fill="url(#gpv-sw-terra)" stroke="#C9BFAE"/></svg>')
    sw_cls = (f'<svg class="gpv-sw" viewBox="0 0 16 16" aria-hidden="true"><rect x=".5" y=".5" width="15" height="15" fill="{CLS}" '
              'stroke="#3E3D39"/></svg>')
    return (
        '<figure class="gpv-raw gpv-sez-fig">'
        '<div class="gpv-sez-intero">'
        f'<div class="gpv-sez-fascia">{"".join(fascia)}</div>'
        '<div class="gpv-sez-img">'
        + svg_sezione((SX0, SX0 + SW), True, 'Sezione di una pista self Mod. 450: pannelli, grigliato e vasca sottopista sopra il '
                      'piano di posa; a destra dissabbiatore e separatore oli collegati dal tubo di scarico', 'gpv-si')
        + ''.join(richiami) + ''.join(terreno) + '</div></div>'
        '<div class="gpv-sez-diviso">'
        '<div class="gpv-sez-parte">'
        + svg_sezione((-40, 700), False, 'Sezione della pista self Mod. 450: due pannelli da 20 cm sul pietrisco, grigliato verde '
                      'e vasca sottopista sul magrone', 'gpv-sp')
        + f'<ul class="gpv-sez-lista">{lista(["a", "b", "d", "e", "h", "g"])}</ul></div>'
        '<div class="gpv-sez-parte">'
        + svg_sezione((700, 1310), False, 'Sezione del dissabbiatore statico e del separatore oli con filtro a coalescenza, '
                      'collegati dal tubo che arriva dalla vasca sottopista', 'gpv-sv')
        + f'<ul class="gpv-sez-lista">{lista(["c", "f"])}</ul></div>'
        '</div>'
        '<figcaption class="gpv-sez-nota">'
        '<div><p>Sezione lungo l’asse di una pista self Mod.&nbsp;450 e della linea che tratta l’acqua di lavaggio. Pezzi in scala, '
        'misure in centimetri; la posizione delle vasche è indicativa.</p>'
        f'<ul class="gpv-legenda"><li>{sw_cls}Manufatti Gardens Pav</li><li>{sw_opere}Opere edili dell’impresa</li>'
        f'<li>{sw_terra}Terreno</li></ul></div>'
        '<div><h3>Compreso con la piattaforma</h3><p>Posa in cantiere con il nostro personale. Vasca sottopista, grigliato, supporti '
        'zincati, giuntoplasto, staffe e viti inox, tubazioni nei pannelli. Disegno con le fasi di posa, relazione strutturale, '
        'scheda tecnica e piano di manutenzione.</p></div>'
        '<div><h3>Su richiesta</h3><p>Trasporto con o senza gru, noleggio dell’autogru.</p>'
        '<h3>Escluso</h3><p>Scavo, sbancamento, piano di posa, cordolo perimetrale e relazioni di calcolo delle opere edili.</p></div>'
        '</figcaption></figure>'
    )


CSS_SEZIONE = (
    '.gpv-sez-fig{--r2b:26px;--r1b:102px;--fascia:170px}'
    '.gpv-sez-svg{display:block;width:100%;height:auto}'
    '.gpv-sez-fascia{position:relative;height:var(--fascia)}'
    '.gpv-sez-img{position:relative}'
    f'.gpv-dida{{position:absolute;display:block;width:max-content;text-decoration:none!important;color:{TESTO}!important;line-height:1.25}}'
    '.gpv-dida--r1{bottom:var(--r1b);margin-left:8px}'
    '.gpv-dida--r2{bottom:var(--r2b);margin-left:8px}'
    '.gpv-dida--dx{margin-left:0;margin-right:8px;text-align:right}'
    f'.gpv-dida--t{{margin-left:-8px;padding:4px 8px 8px;background:{TERRA}}}'
    '.gpv-dida--tdx{margin-left:0;margin-right:-8px;text-align:right}'
    f'.gpv-dida-n{{display:block;font-weight:700;font-size:15px;text-decoration:underline;text-decoration-color:{SOTTOLINEA};'
    'text-decoration-thickness:1px;text-underline-offset:3px}'
    f'.gpv-dida-d{{display:block;font-size:14px;color:{TESTO2};margin-top:4px;font-variant-numeric:tabular-nums;text-wrap:pretty}}'
    f'.gpv-dida:hover .gpv-dida-n,.gpv-voce:hover .gpv-dida-n{{text-decoration-color:{ARANCIO};text-decoration-thickness:2px}}'
    f'.gpv-dida--escl .gpv-dida-n,.gpv-voce--escl .gpv-dida-n{{color:{TESTO2}}}'
    f'.gpv-richiamo{{position:absolute;width:1px;margin-left:-.5px;background:{TESTO};pointer-events:none}}'
    '.gpv-richiamo--r1{top:calc(-1 * var(--r1b));height:calc(var(--r1b) + var(--y))}'
    '.gpv-richiamo--r2{top:calc(-1 * var(--r2b));height:calc(var(--r2b) + var(--y))}'
    '.gpv-sez-diviso{display:none}'
    '.gpv-sez-lista{margin-top:16px!important;display:grid;gap:12px}'
    f'.gpv-voce{{display:block;text-decoration:none!important;color:{TESTO}!important;line-height:1.3}}'
    '.gpv-sez-nota{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:48px;padding:24px 0 0;font-size:15px;line-height:1.5}'
    '.gpv-sez-nota h3{font-size:15px;font-weight:700;line-height:1.3;margin-bottom:4px}'
    '.gpv-sez-nota p+h3{margin-top:12px}'
    f'.gpv-legenda{{margin-top:8px!important;display:flex;flex-wrap:wrap;gap:8px 16px;color:{TESTO2}}}'
    '.gpv-legenda li{display:flex;align-items:center;gap:8px}'
    '.gpv-sw{display:block;width:16px;height:16px;flex:none}'
    '@media (max-width:1340px){.gpv-sez-fig{--r1b:96px;--fascia:160px}.gpv-dida-n{font-size:14px}.gpv-dida-d{font-size:13px}}'
    '@media (max-width:1180px){.gpv-sez-fig{--fascia:195px}}'
    '@media (max-width:1024px){.gpv-sez-intero{display:none}'
    '.gpv-sez-diviso{display:grid;grid-template-columns:minmax(0,740fr) minmax(0,610fr);gap:32px;margin-top:16px}'
    '.gpv-sez-nota{grid-template-columns:1fr 1fr;gap:24px 32px;padding-top:32px}'
    '.gpv-sez-nota > :first-child{grid-column:1 / -1}}'
    '@media (max-width:767px){.gpv-sez-diviso{grid-template-columns:1fr;gap:32px}.gpv-sez-nota{grid-template-columns:1fr;gap:16px}}'
)


# ---------------------------------------------------------------------------------------------
# Le quattro fasi di posa (home, H4): la pista self Mod. 450 in sezione, il pezzo nuovo in grigio pieno
# ---------------------------------------------------------------------------------------------
FVB = (-44, -76, 576, 228)
F_SCURO = f'fill="{CLS}" stroke="#2A2926" stroke-width="1.5"'
F_CHIARO = 'fill="#EEEDEA" stroke="#B3B1AB" stroke-width="1"'
SCAVO = 'M-30 0 V40 H165 V140 H285 V40 H480 V0 Z'


def _f_defs(n):
    return (f'<defs><pattern id="gpv-f{n}-ter" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">'
            f'<rect width="14" height="14" fill="{TERRA}"/><line x1="0" y1="0" x2="0" y2="14" stroke="#D6CDBD" stroke-width="1.6"/></pattern>'
            f'<pattern id="gpv-f{n}-pie" width="9" height="9" patternUnits="userSpaceOnUse">'
            '<rect width="9" height="9" fill="#EEEDEA"/><circle cx="2.5" cy="2.5" r="1.5" fill="#B3B1AB"/><circle cx="7" cy="6.5" r="1.2" fill="#C2C0BA"/></pattern>'
            f'<pattern id="gpv-f{n}-pies" width="9" height="9" patternUnits="userSpaceOnUse">'
            '<rect width="9" height="9" fill="#D9D6CE"/><circle cx="2.5" cy="2.5" r="1.8" fill="#4E4C47"/><circle cx="7" cy="6.5" r="1.5" fill="#6B6964"/></pattern>'
            f'<pattern id="gpv-f{n}-gri" width="4" height="4" patternUnits="userSpaceOnUse">'
            '<rect width="4" height="4" fill="#2E7A4C"/><rect x="1.3" y="0" width="1.4" height="4" fill="#3F9861"/></pattern></defs>')


def _quota(x1, x2, y, t):
    return (f'<g><line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<line x1="{x1}" y1="{y - 6}" x2="{x1}" y2="{y + 6}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<line x1="{x2}" y1="{y - 6}" x2="{x2}" y2="{y + 6}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<text x="{(x1 + x2) / 2}" y="{y - 8}" text-anchor="middle">{t}</text></g>')


def _quota_v(x, y1, y2, t):
    return (f'<g><line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<line x1="{x - 5}" y1="{y1}" x2="{x + 5}" y2="{y1}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<line x1="{x - 5}" y1="{y2}" x2="{x + 5}" y2="{y2}" stroke="#2A2926" stroke-width="1" {NS}/>'
            f'<text x="{x + 9}" y="{(y1 + y2) / 2 + 8}" text-anchor="start">{t}</text></g>')


def _f_terreno(n, scavato):
    x, y, w, h = FVB
    s = f'<rect x="{x}" y="0" width="{w}" height="{h + y}" fill="url(#gpv-f{n}-ter)"/>'
    if scavato:
        s += f'<path d="{SCAVO}" fill="#FFFFFF"/>'
        s += f'<path d="M{x} 0 H-30 V40 H165 V140 H285 V40 H480 V0 H{x + w}" fill="none" stroke="#B3B1AB" stroke-width="1" {NS}/>'
    else:
        s += f'<line x1="{x}" y1="0" x2="{x + w}" y2="0" stroke="#6F6D67" stroke-width="1.2" {NS}/>'
    return s


def _f_vasca(stile):
    return (f'<rect x="165" y="130" width="120" height="10" {F_CHIARO} {NS}/>'
            f'<path d="M175 20 H185 V120 H265 V20 H275 V130 H175 Z" {stile} {NS}/>'
            f'<rect x="275" y="86" width="40" height="12" {stile} {NS}/>')


def _f_cordoli(n, scuro):
    pie = f'url(#gpv-f{n}-pies)' if scuro else f'url(#gpv-f{n}-pie)'
    st = F_SCURO if scuro else F_CHIARO
    pst = 'stroke="#2A2926" stroke-width="1.5"' if scuro else 'stroke="#B3B1AB" stroke-width="1"'
    return (f'<path d="M165 40 V140 H175 V40 Z M275 40 V140 H285 V40 Z" fill="url(#gpv-f{n}-pie)" stroke="none"/>'
            f'<rect x="10" y="20" width="165" height="20" fill="{pie}" {pst} {NS}/>'
            f'<rect x="275" y="20" width="165" height="20" fill="{pie}" {pst} {NS}/>'
            f'<rect x="-30" y="20" width="40" height="20" {st} {NS}/>'
            f'<rect x="440" y="20" width="40" height="20" {st} {NS}/>')


def _f_pannelli(n):
    return (f'<path d="M-10 0 L185 3 V23 L-10 20 Z" {F_SCURO} {NS}/>'
            f'<path d="M460 0 L265 3 V23 L460 20 Z" {F_SCURO} {NS}/>'
            f'<rect x="185" y="3" width="80" height="5" fill="url(#gpv-f{n}-gri)" stroke="#1E5434" stroke-width="1" {NS}/>'
            f'<path d="M185 8 H193 V14 M265 8 H257 V14" fill="none" stroke="#2A2926" stroke-width="1.5" {NS}/>')


def svg_fasi():
    def svg(n, corpo, etichetta):
        x, y, w, h = FVB
        return (f'<svg class="gpv-raw gpv-fase-svg" viewBox="{x} {y} {w} {h}" role="img" aria-label="{etichetta}" '
                f'xmlns="http://www.w3.org/2000/svg">{_f_defs(n)}{corpo}</svg>')
    c1 = _f_terreno(1, False)
    c1 += ('<rect x="-33" y="-36" width="6" height="50" fill="#2A2926"/><rect x="447" y="-36" width="6" height="50" fill="#2A2926"/>'
           f'<line x1="-30" y1="-28" x2="450" y2="-28" stroke="#2A2926" stroke-width="1.5" stroke-dasharray="6 4" {NS}/>'
           f'<path d="{SCAVO}" fill="none" stroke="#9D9B95" stroke-width="1" stroke-dasharray="5 5" {NS}/>')
    c1 += _quota(-30, 450, -46, '450')
    c2 = _f_terreno(2, True) + _f_vasca(F_SCURO) + _quota(175, 275, 6, '100') + _quota_v(330, 20, 130, '110 h')
    c3 = _f_terreno(3, True) + _f_vasca(F_CHIARO) + _f_cordoli(3, True) + _quota_v(486, 20, 40, '20')
    c4 = (_f_terreno(4, True) + _f_vasca(F_CHIARO) + _f_cordoli(4, False) + _f_pannelli(4)
          + _quota(-10, 460, -18, '450') + _quota_v(486, 0, 20, '20'))
    return [svg(1, c1, 'Tracciatura dei contorni della piazzola larga 450 cm'),
            svg(2, c2, 'Posa della vasca sottopista 400 per 100 per 110 cm sul magrone'),
            svg(3, c3, 'Cordoli perimetrali di magrone e pietrisco 4/8 da 20 cm'),
            svg(4, c4, 'Posa dei due pannelli da 20 cm e del grigliato in vetroresina')]


# ---------------------------------------------------------------------------------------------
# Dati della home (01: schede dei prodotti, punti 26-31; cantieri, punto 40; tabelle-pulite.json)
# ---------------------------------------------------------------------------------------------
# (immagine, nome, sottoprodotti, due righe di numeri, link, alt, voce del modulo)
SCHEDE_PIATTAFORME = [
    ('scheda-pista-self.jpg', 'Piste self', f'Mod.{NB}450, Mod.{NB}500, Mod.{NB}500 doppia griglia',
     [f'450×650 o 500×650{NB}cm', f'2{NB}pannelli da 5,90 o 6,70{NB}t'],
     '/piattaforme-autolavaggi/#piste-self', 'Pista self esplosa: due pannelli, vasca sottopista e grigliato', 'Piste self'),
    ('scheda-portali.jpg', 'Portali', f'Mod.{NB}1, Mod.{NB}2, Mod.{NB}3 lavaggio chassis, Mod.{NB}4 prelavaggio, Mod.{NB}5',
     [f'da 500×1100 a 500×1800{NB}cm', f'4 o 6 pannelli a incastro da 20{NB}cm'],
     '/piattaforme-autolavaggi/#portali', 'Piattaforma per portale Mod. 5 in assonometria', 'Portali'),
    ('scheda-isola.jpg', 'Isola di aspirazione e trave di rialzo', 'piastra per l’aspiratore, trave rovescia per le strutture in acciaio',
     [f'piastra da 25{NB}cm, 2,50{NB}t', f'trave da 30{NB}cm, 3,20{NB}t'],
     '/piattaforme-autolavaggi/#accessori', 'Isola di aspirazione prefabbricata', 'Isola di aspirazione o trave di rialzo'),
    ('scheda-colori.jpg', 'Personalizzazione', 'calcestruzzo colorato, riscaldamento a pavimento, tubazioni predisposte',
     ['4 colori con ossidi di ferro', 'rosso, verde, giallo, marrone'],
     '/piattaforme-autolavaggi/#personalizzazione', 'Pianta di una pista self 450×650 in calcestruzzo colorato rosso',
     'Piattaforma colorata o riscaldata'),
]
SCHEDE_ACQUA = [
    ('scheda-rettangolari.jpg', 'Vasche rettangolari', 'acqua piovana, prima pioggia, antincendio, con resine epossidiche',
     [f'11 misure, da 2,40 a 50{NB}m³', f'la più grande 1050×243×263{NB}h, 27{NB}t'],
     '/vasche/#rettangolari', 'Vasca rettangolare monoblocco con coperchio', 'Vasche rettangolari'),
    ('scheda-circolari.jpg', 'Vasche circolari', f'Ø{NB}148, 196 e 242, con resine epossidiche',
     [f'6 misure, da 2,30 a 9,80{NB}m³', f'da 1,80 a 4,80{NB}t di vasca'],
     '/vasche/#circolari', 'Vasca circolare monoblocco con coperchio', 'Vasche circolari'),
    ('scheda-prima-pioggia.jpg', 'Prima pioggia', f'pozzetto scolmatore, accumulo per 48{NB}ore, separatore oli',
     [f'17 taglie, da 400 a 10.000{NB}m²', f'in uscita oli non oltre 5{NB}mg/l'],
     '/depurazione/#prima-pioggia', 'Impianto di prima pioggia in proiezione', 'Prima pioggia'),
    ('scheda-dissabbiatore.jpg', 'Dissabbiatore statico', 'circolare o rettangolare, deflettore in PVC',
     [f'15 misure, da 2,30 a 50{NB}m³', f'da Ø{NB}148×206{NB}h a 1050×243×263{NB}h'],
     '/depurazione/#dissabbiatore', 'Dissabbiatore statico rettangolare in sezione', 'Dissabbiatore statico'),
    ('scheda-separatore-oli.jpg', 'Separatore oli', f'filtro a coalescenza, UNI{NB}EN{NB}858-1, per autorimesse',
     [f'5 taglie, da 3 a 30{NB}l/s', 'autorimesse fino a 450 posti auto'],
     '/depurazione/#separatore-oli', 'Separatore oli rettangolare in sezione', 'Separatore oli'),
    ('scheda-separatore-grassi.jpg', 'Separatore grassi', f'UNI{NB}EN{NB}1825-1, cucine, mense, macellerie',
     [f'5 taglie, da 3 a 38{NB}l/s', f'da Ø{NB}148×206{NB}h a 550×243×260{NB}h'],
     '/depurazione/#separatore-grassi', 'Separatore grassi circolare in sezione', 'Separatore grassi'),
    ('scheda-imhoff.jpg', 'Vasca Imhoff', 'acque nere domestiche, sedimentazione e digestione',
     [f'7 taglie, da 5 a 70{NB}AE', f'da 2,40 a 18,50{NB}t di vasca'],
     '/depurazione/#imhoff', 'Vasca Imhoff in sezione', 'Vasca Imhoff'),
    ('scheda-biologici.jpg', 'Depuratori biologici', 'ossidazione totale a fanghi attivi, dove non arriva la fognatura',
     [f'BIO7{WJ}-{WJ}BIO20, da 7 a 20{NB}AE', f'BIO5L{WJ}-{WJ}BIO15L per la Laguna di Venezia'],
     '/depurazione/#biologici', 'Depuratore biologico in sezione', 'Depuratori biologici'),
]

CONSEGNA = [
    ('consegna-autogru.jpg', 'Vasca rettangolare sull’autocarro, sotto l’autogru',
     'Vasca rettangolare caricata sull’autocarro, accanto all’autogru, con il logo Gardens Pav'),
    ('consegna-calata.jpg', 'Vasca a più comparti calata nello scavo con le catene',
     'Vasca rettangolare a più comparti appesa alle catene sopra lo scavo'),
    ('consegna-lunga.jpg', 'Vasca rettangolare lunga e pozzetto circolare, in cantiere',
     'Vasca rettangolare lunga con coperchio e pozzetto circolare posati nello scavo'),
    ('consegna-batteria.jpg', 'Vasche rettangolari in batteria, in cantiere', 'Vasche rettangolari aperte, affiancate in batteria'),
]

# modelli di piattaforma (01, punto 31): nome, piazzola, pannelli, peso del pannello, vasche di raccolta
MODELLI = [
    (f'Mod.{NB}450', '450×650', '2 da 228×650', '5,90', '1'),
    (f'Mod.{NB}500', '500×650', '2 da 253×650', '6,70', '1'),
    (f'Mod.{NB}500 doppia griglia', '500×650', '2 da 253×650', '6,70', '2'),
    (f'Mod.{NB}1', '500×1200', '4 da 253×600', '6,70', '1'),
    (f'Mod.{NB}2', '500×1100', '4 da 253×550', '6,00', 'pozzetto escluso'),
    (f'Mod.{NB}3 lavaggio chassis', '500×1200', '4 da 253×600', '6,70', '2'),
    (f'Mod.{NB}4 area prelavaggio', '500×1300/<wbr>1800', '6, misure variabili', 'secondo le misure', 'da confermare'),
    (f'Mod.{NB}5', '500×1300/<wbr>1800', '6, misure variabili', 'secondo le misure', '1'),
]

# (immagine, alt, testo della fase, didascalia della foto); l'ordine è quello del disegno con le fasi (01, punto 30)
FASI = [
    ('posa-1-tracciatura.jpg', 'Controllo delle misure e delle quote sul piano di posa', 'Tracciatura della piazzola',
     f'Si segnano a terra i contorni della piazzola, 450×650{NB}cm per la pista self Mod.{NB}450.',
     'San Giovanni in Persiceto (BO), controllo di misure e quote'),
    ('posa-2-vasca.jpg', 'Vasche sottopista posate nel piano di posa di due piste self', 'Posa della vasca',
     f'Vasca sottopista 400×100×110{NB}h sul magrone d’appoggio. La vasca è compresa nella fornitura.',
     'Abano Terme (PD), piano di posa delle piste self'),
    ('posa-3-cordoli.jpg', 'Cordoli di magrone e pietrisco intorno alle vasche di tre piste self', 'Cordoli perimetrali',
     f'Cordolo di magrone e pietrisco 4/8 da 20{NB}cm. Sono opere edili, escluse dalla fornitura.',
     'Biella, piano di posa delle piste self'),
    ('posa-4-pannelli.jpg', 'Pannello calato con le catene accanto alla vasca sottopista', 'Posa dei pannelli',
     f'Due pannelli da 5,90{NB}t con l’autogru, poi il grigliato sui supporti zincati. Li posa il nostro personale.',
     f'Grugliasco (TO), pista self Mod.{NB}450'),
]

# mosaico: luogo e modelli come li scrive il sito attuale (01, punto 40); nessun nome di cliente
MOSAICO = [
    ('abano-terme', 'Abano Terme (PD)', f'portale Mod.{NB}1 e piste self'),
    ('aosta', 'Aosta', ''),
    ('pistoia', 'Pistoia', ''),
    ('lucenec', 'Lučenec, Slovacchia', 'piste self riscaldate'),
    ('grugliasco', 'Grugliasco (TO)', f'piste self Mod.{NB}450 e portale'),
    ('cesena', 'Cesena (FC)', f'portale Mod.{NB}2 e piste self'),
    ('crema', 'Crema (CR)', f'concessionaria, portale Mod.{NB}1'),
    ('milano', 'Milano', ''),
    ('ponsacco', 'Ponsacco (PI)', f'portale Mod.{NB}1 e piste self Mod.{NB}500'),
    ('vezza-d-oglio', 'Vezza d’Oglio (BS)', 'autofficina, pista self'),
    ('san-marino', 'San Marino', ''),
    ('mottola', 'Mottola (TA)', 'piste self'),
    ('piacenza', 'Piacenza', f'portali Mod.{NB}1 e Mod.{NB}3, piste self'),
    ('rubano', 'Rubano (PD)', f'portale Mod.{NB}3 con lavachassis e piste self'),
    ('poschiavo', 'Poschiavo, Svizzera', 'autofficina, pista self'),
    ('tivoli-terme', 'Tivoli Terme (RM)', f'portale Mod.{NB}1'),
]

LUOGHI = [
    ('Veneto', 'Abano Terme, Altivole, Alonte, Rovigo, Rubano, Verona (2)'),
    ('Lombardia', 'Borgosatollo, Cornate d’Adda, Crema, Gavardo, Milano, Vezza d’Oglio'),
    ('Piemonte e Valle d’Aosta', 'Aosta, Biella, Grugliasco, Montanera, Rivalta di Torino'),
    ('Emilia-Romagna', 'Budrio, Cesena, Piacenza, San Giovanni in Persiceto, San Lazzaro di Savena, San Mauro Pascoli'),
    ('Toscana, Lazio, Puglia', 'Livorno, Pistoia, Ponsacco, Viareggio, Tivoli Terme, Avetrana, Mottola'),
    ('Fuori dall’Italia', 'Poschiavo (Svizzera), Lučenec (Slovacchia), due centri di lavaggio in Francia, San Marino'),
]

# voci del modulo (specifica 14): le stesse del modulo Contact Form 7 "Richiesta d'offerta"
PRODOTTI_MODULO = ['Piste self', 'Portali', 'Isola di aspirazione o trave di rialzo', 'Piattaforma colorata o riscaldata',
                   'Vasche rettangolari', 'Vasche circolari', 'Vasche con resine epossidiche', 'Prima pioggia',
                   'Dissabbiatore statico', 'Separatore oli', 'Separatore oli per autorimesse', 'Separatore grassi',
                   'Vasca Imhoff', 'Depuratori biologici', 'Altro']
TRASPORTO = ['Con automezzo con gru', 'Con automezzo senza gru', 'Da decidere al telefono']


# ---------------------------------------------------------------------------------------------
# Modulo "Richiesta d'offerta" (specifica 14): Contact Form 7 in WordPress, lo stesso modulo in HTML nel fallback
# (senza Contact Form 7 la richiesta parte come email già compilata dal programma di posta)
# ---------------------------------------------------------------------------------------------
CF7_TITOLO = 'Richiesta d’offerta'
CF7_SHORTCODE = f'[contact-form-7 title="{CF7_TITOLO}"]'


def modulo_cf7():
    """Testo della scheda "Modulo" di Contact Form 7: senza a capo tra i campi (Contact Form 7 non aggiunge <p> e <br>)."""
    prodotti = ' '.join(f'"{p}"' for p in PRODOTTI_MODULO)
    trasporto = ' '.join(f'"{t}"' for t in TRASPORTO)
    return (
        '<div class="gpv-campi">'
        f'<label class="gpv-campo gpv-campo--l">Che cosa vi serve [select* prodotto first_as_label "Scegliete il prodotto" {prodotti}]</label>'
        '<label class="gpv-campo">Il vostro dato [text dato placeholder "10 AE, 5 l/s, 2.000 m²"]</label>'
        '<label class="gpv-campo">Quantità [text quantita]</label>'
        '<label class="gpv-campo">Comune di posa [text* comune]</label>'
        f'<label class="gpv-campo">Trasporto [select trasporto {trasporto}]</label>'
        '<label class="gpv-campo">Nome e cognome [text* nome autocomplete:name]</label>'
        '<label class="gpv-campo">Azienda [text azienda autocomplete:organization]</label>'
        '<label class="gpv-campo">Telefono [tel* telefono autocomplete:tel]</label>'
        '<label class="gpv-campo">Email [email* email autocomplete:email]</label>'
        '<label class="gpv-campo gpv-campo--l">Note [textarea note]</label>'
        '</div>'
        '<div class="gpv-consenso">[acceptance privacy] Ho letto l’<a href="/privacy/">informativa sulla privacy</a> e accetto il '
        'trattamento dei dati per ricevere l’offerta. [/acceptance]</div>'
        '[submit class:gpv-btn "Invia la richiesta"]'
    )


def modulo_html():
    """Lo stesso modulo in HTML, per il fallback e l'anteprima."""
    opz = '<option value="">Scegliete il prodotto</option>' + ''.join(f'<option>{p}</option>' for p in PRODOTTI_MODULO)
    tra = ''.join(f'<option>{t}</option>' for t in TRASPORTO)
    return (
        f'<form class="gpv-raw gpv-form" action="mailto:{EMAIL}" method="post" enctype="text/plain">'
        '<div class="gpv-campi">'
        f'<label class="gpv-campo gpv-campo--l">Che cosa vi serve<select name="prodotto" required>{opz}</select></label>'
        '<label class="gpv-campo">Il vostro dato<input type="text" name="dato" placeholder="10 AE, 5 l/s, 2.000 m²"></label>'
        '<label class="gpv-campo">Quantità<input type="text" name="quantita"></label>'
        '<label class="gpv-campo">Comune di posa<input type="text" name="comune" required></label>'
        f'<label class="gpv-campo">Trasporto<select name="trasporto">{tra}</select></label>'
        '<label class="gpv-campo">Nome e cognome<input type="text" name="nome" autocomplete="name" required></label>'
        '<label class="gpv-campo">Azienda<input type="text" name="azienda" autocomplete="organization"></label>'
        '<label class="gpv-campo">Telefono<input type="tel" name="telefono" autocomplete="tel" required></label>'
        '<label class="gpv-campo">Email<input type="email" name="email" autocomplete="email" required></label>'
        '<label class="gpv-campo gpv-campo--l">Note<textarea name="note"></textarea></label>'
        '</div>'
        '<div class="gpv-consenso"><label><input type="checkbox" name="privacy" required><span>Ho letto l’<a class="gpv-a" '
        'href="/privacy/">informativa sulla privacy</a> e accetto il trattamento dei dati per ricevere l’offerta.</span></label></div>'
        '<button class="gpv-btn" type="submit">Invia la richiesta</button>'
        '</form>'
    )


CSS_MODULO = (
    '.gpv-modulo form{margin:0}'
    # Contact Form 7 avvolge i campi in un <p>: per la griglia non deve esistere
    '.gpv-campi > p,.gpv-campi > br{display:contents}'
    '.gpv-modulo form > p,.gpv-consenso > p{margin:0}'
    '.gpv-campi{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px}'
    f'.gpv-campo{{display:flex!important;flex-direction:column;gap:4px;font:600 14px/1.3 {FONT_CSS};color:{TESTO};margin:0;'
    'vertical-align:top}'
    '.gpv-campo--l{grid-column:1 / -1}'
    '.gpv-campo .wpcf7-form-control-wrap{display:block}'
    f'.gpv-campo input,.gpv-campo select,.gpv-campo textarea{{font:400 16px/1.3 {FONT_CSS}!important;padding:10px 12px!important;'
    f'border:1px solid {BORDO_CAMPI}!important;border-radius:2px!important;background:#FFFFFF!important;color:{TESTO}!important;'
    'width:100%!important;margin:0!important;box-shadow:none!important;height:auto;min-height:44px}'
    f'.gpv-campo input::placeholder,.gpv-campo textarea::placeholder{{color:{SEGNAPOSTO};opacity:1}}'
    '.gpv-campo textarea{min-height:92px;height:92px;resize:vertical}'
    f'.gpv-consenso{{font:400 14px/1.4 {FONT_CSS};color:{TESTO};margin-top:16px}}'
    '.gpv-consenso label{display:flex!important;gap:12px;align-items:flex-start;line-height:1.4;margin:0}'
    '.gpv-consenso .wpcf7-list-item{display:block;margin:0}'
    f'.gpv-consenso input[type=checkbox]{{margin:2px 0 0;width:18px;height:18px;flex:none;accent-color:{TESTO}}}'
    f'.gpv-consenso a{{color:{TESTO}!important;text-decoration:underline!important;text-underline-offset:3px}}'
    '.gpv-modulo .gpv-btn{margin-top:16px;font-size:16px!important;padding:14px 22px!important}'
    '.gpv-modulo .wpcf7-spinner{margin:16px 0 0 12px}'
    # errori: bordo grafite da 2 px e messaggio in testo, nessun rosso
    f'.gpv-modulo .wpcf7-not-valid{{border:2px solid {TESTO}!important}}'
    f'.gpv-modulo .wpcf7-not-valid-tip{{color:{TESTO};font:400 14px/1.4 {FONT_CSS};margin-top:4px}}'
    '.gpv-modulo .wpcf7-not-valid-tip::before{content:"Manca: "}'
    f'.gpv-modulo .wpcf7-response-output{{border:1px solid {TESTO}!important;background:#FFFFFF;color:{TESTO};margin:16px 0 0!important;'
    f'padding:12px 16px!important;font:400 15px/1.5 {FONT_CSS}}}'
    '@media (max-width:1100px){.gpv-campi{grid-template-columns:1fr}}'
    '@media (min-width:768px) and (max-width:1024px){.gpv-campi{grid-template-columns:1fr 1fr}}'
)

# precompila il prodotto (e il dato) dall'indirizzo; in home i link "Chiedi un'offerta" scrivono il prodotto e scendono al
# modulo senza ricaricare; nel fallback l'invio apre il programma di posta con la richiesta già scritta
JS_MODULO = (
    "(function(){var s=document.querySelector('.gpv-modulo select[name=\"prodotto\"]');if(!s)return;"
    "var d=document.querySelector('.gpv-modulo input[name=\"dato\"]');"
    "function imposta(v){if(!v)return;for(var i=0;i<s.options.length;i++){if(s.options[i].value===v||s.options[i].text===v){s.selectedIndex=i;return}}}"
    "try{var q=new URLSearchParams(location.search);imposta(q.get('prodotto'));if(d&&!d.value&&q.get('dato'))d.value=q.get('dato')}catch(e){}"
    "var dove=document.getElementById('contatti')||document.getElementById('richiesta');"
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-prodotto]');if(!a||!dove)return;"
    "e.preventDefault();imposta(a.getAttribute('data-prodotto'));dove.scrollIntoView();"
    "try{history.replaceState(null,'',a.getAttribute('href'))}catch(e2){}s.focus({preventScroll:true})});"
    "document.querySelectorAll('form.gpv-form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();"
    "var r=[];f.querySelectorAll('select,input,textarea').forEach(function(x){if(x.type==='checkbox')return;"
    "var l=x.closest('label');r.push((l?l.firstChild.textContent.trim():x.name)+': '+x.value)});"
    f"location.href='mailto:{EMAIL}?subject='+encodeURIComponent('Richiesta d\\u2019offerta: '+f.prodotto.value+', '+f.comune.value)"
    "+'&body='+encodeURIComponent(r.join('\\n'))})})})();"
)


# ---------------------------------------------------------------------------------------------
# HOME (specifica 5): la home finale del 13 ottobre, stessi testi e stesso ordine
# ---------------------------------------------------------------------------------------------
def h_apertura():
    return sezione(
        titolo('Piattaforme per autolavaggi e vasche per il trattamento delle acque', 'h1', 'display', max_w=(1248, 1056, 1000)),
        testo('<p>Prefabbricati in calcestruzzo armato vibrato Rck 45, prodotti a Legnaro (PD). Sopra, la pista che posiamo noi; '
              'sotto, le vasche che raccolgono e trattano l’acqua.</p>', 'apertura', mt='s', max_w=(558, 558, 496)),
        RAW(html_sezione(), css=CSS_SEZIONE, mt='micro'),
        pad=('xl', 'lato', '0', 'lato'), anchor='contenuto')


def h_linee():
    consegna = C(
        titolo('In consegna e in cantiere', 'h3', 'h3b'),
        testo(f'<p>Ogni vasca arriva in un pezzo solo. Calcestruzzo C35/45 (Rck 45{NB}N/mm²) per le classi di esposizione XC4, '
              f'XS1-XD2, XF1 e XA2, acciaio B450C, copriferro 3{NB}cm.</p>', colore=TESTO2, mt='xs', max_w=1054),
        griglia(*[figura(f, alt, cap) for f, cap, alt in CONSEGNA], mt='m'),
        gap='0', mt=48)
    return sezione(
        testa('Piattaforme per autolavaggi', 'Pannelli a incastro già maturati in stabilimento. Quando pozzetto, scarichi e '
              'sottofondo sono pronti, la pista si posa in poche ore.', ('Modelli e forniture', '/piattaforme-autolavaggi/')),
        griglia(*[scheda_famiglia(*s) for s in SCHEDE_PIATTAFORME], css='gpv-schede'),
        testo(f'<p>Brevetto per invenzione industriale depositato n°{NB}275.271. Superficie a rombi con attrito 0,88 sul bagnato, '
              f'dove il D.M.{NB}236/1989 chiede più di 0,40. Posate in <a class="gpv-a" href="#realizzazioni">36 cantieri</a> in Italia, '
              'Svizzera, Slovacchia, Francia e San Marino.</p>', 'testo16', mt='l'),
        testa('Vasche e impianti per l’acqua', 'Monoblocchi in calcestruzzo armato vibrato, a tenuta idraulica. Si scelgono sul '
              'dato del progetto: metri cubi, litri al secondo, abitanti equivalenti (AE), metri quadri di piazzale.',
              ('Tutte le schede', '/depurazione/'), mt='sezione'),
        griglia(*[scheda_famiglia(*s) for s in SCHEDE_ACQUA], css='gpv-schede'),
        consegna)


CSS_PERCORSO = (
    '.gpv-percorso-in.gpv-percorso-in{display:grid!important;grid-template-columns:minmax(0,5fr) minmax(180px,1fr);'
    'gap:32px!important;align-items:end!important}'
    '.gpv-percorso-in > *{width:auto!important;min-width:0}'
    '.gpv-percorso-img img{width:100%;height:auto;display:block}'
    '.gpv-passi.gpv-passi{display:grid!important;grid-template-columns:19fr 34fr 31fr 16fr;gap:24px!important}'
    '.gpv-passi > *{width:auto!important;min-width:0}'
    '.gpv-dato{font-weight:600;font-variant-numeric:tabular-nums}'
    f'.gpv-esempio{{font-size:15px;line-height:1.45;padding-bottom:4px}}'
    '.gpv-esempio h3{font-size:16px;font-weight:700;line-height:1.3;margin-bottom:8px}'
    f'.gpv-esempio li{{padding:8px 0;border-top:1px solid {LINEA};font-variant-numeric:tabular-nums}}'
    '.gpv-esempio li b{display:block;font-weight:600}'
    '@media (max-width:1024px){.gpv-percorso-in.gpv-percorso-in{grid-template-columns:1fr;gap:24px!important}'
    '.gpv-esempio ul{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 16px}}'
    '@media (max-width:767px){.gpv-passi.gpv-passi{grid-template-columns:1fr 1fr;gap:24px 16px!important}'
    '.gpv-esempio ul{gap:0 12px}.gpv-esempio li{font-size:14px}}'
)


def h_percorso():
    passi = [
        ('Smistare', f'<b class="gpv-dato">Pozzetto scolmatore 98×98×106{NB}h.</b> La tubazione più bassa manda al trattamento i '
                     f'primi 5{NB}mm; la seconda pioggia esce dal troppo pieno.'),
        ('Accumulare', '<b class="gpv-dato">Separatore fanghi e accumulo.</b> L’acqua resta ferma 48 ore e sabbie e fanghi vanno '
                       'sul fondo, poi il timer avvia l’elettropompa sommergibile.'),
        ('Disoleare', f'<b class="gpv-dato">Separatore oli UNI{NB}EN{NB}858-1.</b> Le gocce più piccole si uniscono nel filtro a '
                      'coalescenza e risalgono; con la camera oli piena il galleggiante chiude lo scarico.'),
        ('Scaricare', f'In uscita oli minerali e idrocarburi <b class="gpv-dato">entro 5{NB}mg/l.</b>'),
    ]
    esempio = (f'<div class="gpv-raw gpv-esempio"><h3>Per 2.000{NB}m² di piazzale</h3><ul>'
               f'<li><b>Pozzetto scolmatore</b>98×98×106{NB}h</li><li><b>Accumulo</b>300×240×205{NB}h</li>'
               f'<li><b>Separatore oli</b>Ø{NB}148×206{NB}h</li></ul></div>')
    sinistra = C(
        I(img('prima-pioggia-percorso.jpg'), 'Impianto di prima pioggia in sezione: pozzetto scolmatore, vasca di accumulo con '
          'elettropompa, separatore oli con filtro a coalescenza, pozzetto di uscita', css='gpv-percorso-img'),
        C(*[C(titolo(t, 'h3', 'h3'), testo(f'<p>{p}</p>', 'nota', mt='xs'), gap='0') for t, p in passi],
          css='gpv-passi', mt='micro'),
        gap='0')
    return sezione(
        testa('Prima pioggia, dal piazzale allo scarico', f'Sui piazzali scoperti i primi 5{NB}mm di pioggia portano via oli, '
              'idrocarburi e sabbie. L’impianto si sceglie sui metri quadri di superficie scolante, da 400 a 10.000.',
              ('Tutte le taglie', '/depurazione/#prima-pioggia'), stile='h2m'),
        C(sinistra, RAW(esempio, css=CSS_PERCORSO), css='gpv-percorso-in'))


CSS_MODELLI = (
    '.gpv-modelli-in.gpv-modelli-in{display:grid!important;grid-template-columns:minmax(0,4fr) minmax(0,8fr);gap:48px!important;'
    'align-items:start!important}'
    '.gpv-modelli-in > *{width:auto!important;min-width:0}'
    '.gpv-fatti p{margin:0 0 12px!important}.gpv-fatti p:last-child{margin-bottom:0!important}'
    '.gpv-fatti b{font-weight:700}'
    # tabella dei modelli: l'unica della home, 4 righe di dati
    '.gpv-tabmod{width:100%;border-collapse:collapse;table-layout:fixed;margin:0;font-variant-numeric:tabular-nums lining-nums;'
    f'font-family:{FONT_CSS};color:{TESTO};border:0}}'
    # il tema Hello colora le righe dispari e borda le celle: qui nessuna riga a strisce, filetti solo sotto
    f'.gpv-tabmod th,.gpv-tabmod td{{text-align:left;padding:12px 12px 12px 0;border:0!important;border-bottom:1px solid {LINEA}!important;'
    'vertical-align:top;font-size:16px;line-height:1.35;background:transparent!important}'
    '.gpv-tabmod col.gpv-c0{width:14%}'
    f'.gpv-tabmod thead th{{font-weight:700;font-size:15px;vertical-align:bottom;border-bottom:2px solid {TESTO}!important}}'
    f'.gpv-tabmod thead tr:first-child th{{font-weight:600;font-size:15px;color:{TESTO2};border-bottom:0!important;padding-bottom:4px}}'
    '.gpv-tabmod thead tr:first-child td{border-bottom:0!important}'
    f'.gpv-tabmod tbody th{{font-weight:400;color:{TESTO2};font-size:15px}}'
    f'.gpv-tabmod thead tr:last-child td{{border-bottom:2px solid {TESTO}!important}}'
    f'.gpv-tabmod .gpv-gr{{border-left:1px solid {LINEA}!important;padding-left:12px}}'
    f'.gpv-tenue{{color:{TESTO2}}}'
    '.gpv-modlista{display:none}'
    # le quattro fasi
    '.gpv-fasi.gpv-fasi{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px!important}'
    '.gpv-fasi > *{width:auto!important;min-width:0}'
    '.gpv-fase-svg{display:block;width:100%;height:auto;overflow:visible;margin:0 0 12px}'
    f".gpv-fase-svg text{{font-family:{FONT_CSS};font-weight:600;font-size:27px;fill:#2A2926;font-variant-numeric:tabular-nums lining-nums}}"
    '.gpv-fase-p p{min-height:4.5em}'
    '@media (max-width:1100px){.gpv-modelli-in.gpv-modelli-in{gap:32px!important}}'
    '@media (max-width:1024px){.gpv-modelli-in.gpv-modelli-in{grid-template-columns:1fr;gap:48px!important}'
    '.gpv-tabmod{display:none}'
    '.gpv-modlista{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0 24px}'
    f'.gpv-modlista li{{font-size:15px;line-height:1.45;padding:12px 0 16px;border-top:1px solid {LINEA};font-variant-numeric:tabular-nums}}'
    '.gpv-modlista b{display:block;font-weight:700;font-size:16px;margin-bottom:4px}'
    f'.gpv-modlista b span{{font-weight:400;color:{TESTO2}}}'
    '.gpv-fasi.gpv-fasi{grid-template-columns:repeat(2,minmax(0,1fr));gap:32px 24px!important}'
    '.gpv-fase.gpv-fase{display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:16px!important;row-gap:0!important;'
    'grid-template-areas:"disegno disegno" "foto testo";align-content:start}'
    '.gpv-fase > *{width:auto!important;min-width:0}'
    '.gpv-fase-d{grid-area:disegno}.gpv-fase-t{grid-area:testo}.gpv-fase-f{grid-area:foto;margin-top:0!important}'
    '.gpv-fase-t .elementor-heading-title,.gpv-fase-t h3.gpv-w{font-size:17px!important}'
    '.gpv-fase-p p{font-size:14.5px!important;line-height:1.5!important;min-height:0}}'
    '@media (max-width:767px){.gpv-modlista{grid-template-columns:1fr 1fr;gap:0 16px}.gpv-modlista li{font-size:14.5px}'
    '.gpv-modlista b{font-size:15px}.gpv-fasi.gpv-fasi{grid-template-columns:1fr;gap:32px!important}}'
)


def html_modelli():
    testa_t = ''.join(f'<th scope="col">{mo[0]}</th>' for mo in MODELLI)

    def cella(v):
        return f'<td class="gpv-tenue">{v}</td>' if v[0].isalpha() else f'<td>{v}</td>'
    righe = [('Piazzola, cm', 1), ('Pannelli a incastro, cm', 2), ('Peso del pannello, t', 3),
             (f'Vasche di raccolta 400×100×110{NB}h', 4)]
    corpo = ''.join(f'<tr><th scope="row">{nome}</th>' + ''.join(cella(mo[i]) for mo in MODELLI) + '</tr>' for nome, i in righe)
    lista = []
    for k, mo in enumerate(MODELLI):
        tipo = 'pista self' if k < 3 else 'portale'
        pann = (f'{mo[2].split(" da ")[0]} pannelli {mo[2].split(" da ")[1]}{NB}cm, {mo[3]}{NB}t l’uno' if ' da ' in mo[2]
                else '6 pannelli di misure variabili')
        vasche = {'1': '1 vasca di raccolta', '2': '2 vasche di raccolta', 'pozzetto escluso': 'pozzetto di raccolta escluso',
                  'da confermare': 'vasche di raccolta da confermare'}[mo[4]]
        lista.append(f'<li><b>{mo[0]} <span>{tipo}</span></b>{mo[1].replace("<wbr>", "")}{NB}cm<br>{pann}<br>{vasche}</li>')
    return ('<div class="gpv-raw"><table class="gpv-tabmod"><colgroup><col class="gpv-c0"><col span="3"><col span="5"></colgroup>'
            '<thead><tr><td></td><th scope="colgroup" colspan="3">Pista self</th><th scope="colgroup" colspan="5" class="gpv-gr">Portale</th></tr>'
            f'<tr><td></td>{testa_t}</tr></thead><tbody>{corpo}</tbody></table>'
            f'<ul class="gpv-modlista">{"".join(lista)}</ul></div>')


def h_modelli():
    fatti = (
        f'<p><b>Superficie a rombi.</b> Coefficiente d’attrito 0,88 sul bagnato con gomma 4S e 0,89 con cuoio; il D.M.{NB}236/1989 '
        'chiede più di 0,40.</p>'
        f'<p><b>Grigliato.</b> Vetroresina PRFV verde, antiscivolo al quarzo; nelle piste self moduli 200×100{NB}cm, maglia '
        f'3,8×3,8×3,8{NB}h.</p>'
        '<p><b>Tubazioni.</b> Predisposte dentro i pannelli per pluviali, lance e cavi elettrici.</p>'
        f'<p><b>Brevetto.</b> Per invenzione industriale, depositato n°{NB}275.271, domanda PD2011A000169.</p>'
        '<p><b>Smontaggio.</b> La piattaforma si smonta e si rimonta.</p>')
    alto = C(
        C(titolo('Misure, pesi e posa delle piattaforme', 'h2', 'h2s'),
          testo(f'<p>Pannelli a incastro in calcestruzzo Rck 45, spessore 20{NB}cm, posati sulla vasca di raccolta '
                f'400×100×110{NB}h. Non servono casseforme in cantiere.</p>', mt='s'),
          testo(fatti, 'testo16', mt='m', css='gpv-fatti'),
          gap='0'),
        figura('pista-portale.jpg', 'Pista finita sotto il portale di lavaggio, con grigliato verde e superficie a rombi',
               'Pista sotto il portale di lavaggio: grigliato in vetroresina e superficie antiscivolo a rombi.'),
        css='gpv-modelli-in')
    modelli = C(
        titolo('Gli otto modelli', 'h3', 'h3b'),
        testo('<p>Misure in centimetri, larghezza per lunghezza. Tutti i pannelli hanno 20 cm di spessore.</p>', colore=TESTO2,
              mt='xs', max_w=1054),
        RAW(html_modelli(), css=CSS_MODELLI, mt='m'),
        gap='0', mt=48)
    fasi = []
    for (foto, alt, nome, frase, cap), disegno in zip(FASI, svg_fasi()):
        fasi.append(C(
            C(RAW(disegno), gap='0', css='gpv-fase-d'),
            C(titolo(nome, 'h3', 'h3'), testo(f'<p>{frase}</p>', 'nota', mt='xs', css='gpv-fase-p'), gap='0', css='gpv-fase-t'),
            figura(foto, alt, cap, css='gpv-fase-f', mt='s'),
            gap='0', css='gpv-fase'))
    posa = C(
        titolo('La posa in quattro fasi', 'h3', 'h3b'),
        testo('<p>Con la fornitura arriva il disegno delle fasi. Qui la pista self Mod.&nbsp;450 in sezione, con il pezzo nuovo in '
              'grigio pieno e quelli già fatti in chiaro; sotto, lo stesso passaggio in un cantiere.</p>', colore=TESTO2, mt='xs',
              max_w=1054),
        C(*fasi, css='gpv-fasi', mt='l'),
        gap='0', mt=48)
    return sezione(alto, modelli, posa, anchor='piattaforme')


CSS_CANTIERI = (
    '.gpv-mosaico.gpv-mosaico{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px 16px!important}'
    '.gpv-mosaico > *{width:auto!important;min-width:0}'
    f'.gpv-mosaico b{{color:{TESTO};font-weight:600}}'
    '.gpv-cantieri-sotto.gpv-cantieri-sotto{display:grid!important;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:48px!important;'
    'align-items:start!important}'
    '.gpv-cantieri-sotto > *{width:auto!important;min-width:0}'
    '.gpv-luoghi.gpv-luoghi{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 48px!important}'
    '.gpv-luoghi > *{width:auto!important;min-width:0}'
    f'.gpv-luoghi b{{display:block;color:{TESTO};font-weight:700}}'
    '@media (max-width:1100px){.gpv-cantieri-sotto.gpv-cantieri-sotto{gap:32px!important}}'
    '@media (max-width:1024px){.gpv-cantieri-sotto.gpv-cantieri-sotto{grid-template-columns:1fr}}'
    '@media (max-width:900px){.gpv-mosaico.gpv-mosaico{grid-template-columns:repeat(2,minmax(0,1fr))}}'
    '@media (max-width:767px){.gpv-mosaico.gpv-mosaico{gap:16px 8px!important}.gpv-mosaico > :nth-child(n+9){display:none!important}'
    '.gpv-luoghi.gpv-luoghi{grid-template-columns:1fr}}'
)


def h_cantieri():
    mosaico = C(*[figura(f'cantiere-{c}.jpg', f'Piattaforme posate a {luogo}',
                         f'<b>{luogo}</b>{(", " + mod) if mod else ""}') for c, luogo, mod in MOSAICO],
                css='gpv-mosaico')
    luoghi = C(*[testo(f'<p><b>{reg}</b> {txt}</p>', 'small', TESTO2) for reg, txt in LUOGHI], css='gpv-luoghi', mt='m')
    sotto = C(
        C(titolo('I 36 cantieri, per regione', 'h3', 'h3b'), luoghi, gap='0'),
        figura('avetrana-posa.jpg', 'Posatori che montano supporti zincati e grigliato verde sulle vasche di una pista',
               'Avetrana (TA), posa di griglie e supporti.'),
        css='gpv-cantieri-sotto', mt=48)
    return sezione(
        testa('Piattaforme posate in 36 cantieri', 'Autolavaggi self service, stazioni di servizio, concessionarie, officine e '
              'autotrasportatori, in Italia, Svizzera, Slovacchia, Francia e San Marino.',
              ('Tutte le realizzazioni', '/realizzazioni/'), stile='h2m'),
        mosaico, sotto, RAW('', css=CSS_CANTIERI),
        anchor='realizzazioni')


CSS_CONTATTO = (
    '.gpv-contatto-in.gpv-contatto-in{display:grid!important;grid-template-columns:minmax(0,6fr) minmax(0,6fr);'
    'grid-template-areas:"dati modulo" "foto modulo";grid-template-rows:auto 1fr;gap:0 64px!important;align-items:start!important}'
    '.gpv-contatto-in > *{width:auto!important;min-width:0}'
    '.gpv-contatto-dati{grid-area:dati}.gpv-contatto-foto{grid-area:foto}.gpv-modulo{grid-area:modulo}'
    '.gpv-ingressi.gpv-ingressi{display:grid!important;grid-template-columns:1fr 1fr;gap:24px 32px!important}'
    '.gpv-ingressi > *{width:auto!important;min-width:0}'
    f'.gpv-telg a{{color:{TESTO}!important;text-decoration:none!important;white-space:nowrap}}'
    f'.gpv-telg a:hover{{text-decoration:underline!important;text-decoration-color:{ARANCIO}!important;text-decoration-thickness:3px!important;'
    'text-underline-offset:5px!important}'
    '@media (max-width:1100px){.gpv-contatto-in.gpv-contatto-in{column-gap:32px!important}.gpv-ingressi.gpv-ingressi{grid-template-columns:1fr}}'
    '@media (max-width:1024px){.gpv-contatto-in.gpv-contatto-in{grid-template-columns:1fr;grid-template-areas:"dati" "modulo" "foto";'
    'grid-template-rows:auto;gap:32px!important}.gpv-contatto-foto{margin-top:0!important}'
    '.gpv-ingressi.gpv-ingressi{grid-template-columns:1fr 1fr}}'
    '@media (max-width:767px){.gpv-ingressi.gpv-ingressi{grid-template-columns:1fr;gap:24px!important}}'
)


def ingresso(nome, frase):
    return C(titolo(nome, 'h3', 'h3'),
             H(TEL, 'p', style='tel', color=TESTO, link=TEL_LINK, css='gpv-telg gpv-cifre', mt='xs'),
             testo(f'<p>{frase}</p>', 'nota', TESTO2, mt='xs'), gap='0')


def blocco_modulo(ancora_modulo=None):
    """Riquadro "Richiesta d'offerta": Contact Form 7 in WordPress, lo stesso modulo in HTML nel fallback."""
    return C(
        titolo('Richiesta d’offerta', 'h3', 'h3b'),
        testo('<p>Scrivete il dato che avete e l’ufficio tecnico vi ricontatta con la taglia.</p>', 'small', TESTO2, mt='xs'),
        SHORTCODE(CF7_SHORTCODE, alternativa_html=modulo_html()),
        RAW(f'<script>{JS_MODULO}</script>', css=CSS_MODULO),
        bg=SCHEDA, pad=('xl', 'xl', 'xl', 'xl'), gap='0', css='gpv-modulo', anchor=ancora_modulo)


def h_contatto():
    dati = C(
        titolo('Prezzo e consegna, dall’ufficio tecnico', 'h2', 'h2m'),
        testo(f'<p>{ORARI}</p>', mt='xs', css='gpv-cifre'),
        C(ingresso('Piattaforme per autolavaggi', 'Tenete pronti il tipo di impianto, pista self o portale, e le misure dell’area.'),
          ingresso('Vasche e impianti', 'Tenete pronto il dato del progetto: AE, l/s, m² di piazzale, m³ o posti auto. Per portate '
                   'superiori, l’ufficio tecnico dimensiona l’impianto con voi.'),
          css='gpv-ingressi', mt='l'),
        testo(f'<p><a class="gpv-a" href="mailto:{EMAIL}">{EMAIL}</a>, fax {FAX}<br>PEC <a class="gpv-a" href="mailto:{PEC}">{PEC}</a>'
              f'<br>{INDIRIZZO}</p>', 'recapiti', mt='l'),
        gap='0', css='gpv-contatto-dati')
    foto = figura('vasche-circolari-piazzale.jpg', 'Vasche circolari in calcestruzzo affiancate sul piazzale',
                  'Vasche circolari sul piazzale.', css='gpv-contatto-foto', mt='xl')
    # il widget con il foglio di stile sta fuori dalla griglia: dentro occuperebbe una cella
    return sezione(C(dati, foto, blocco_modulo(), css='gpv-contatto-in'), RAW('', css=CSS_CONTATTO),
                   pad=('sezione', 'lato', 'sezione', 'lato'), anchor='contatti')


def home():
    return [('apertura', h_apertura()), ('piattaforme-e-vasche', h_linee()), ('prima-pioggia', h_percorso()),
            ('misure-e-posa', h_modelli()), ('cantieri', h_cantieri()), ('contatto', h_contatto())]


# ---------------------------------------------------------------------------------------------
# Pagine (in questa fase solo la home; testata e menu hanno già tutte le voci)
# ---------------------------------------------------------------------------------------------
PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Gardens Pav: piattaforme per autolavaggi, vasche e impianti per l’acqua',
     'descrizione': 'Piattaforme prefabbricate per autolavaggi e vasche monoblocco in calcestruzzo armato vibrato per il '
                    f'trattamento delle acque, prodotte a Legnaro (PD). Ufficio tecnico {TEL}.'},
]
