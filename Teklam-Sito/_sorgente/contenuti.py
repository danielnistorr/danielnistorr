# -*- coding: utf-8 -*-
"""
Contenuti della home di Tek.Lam per WordPress + Elementor: la home statica approvata ("Il foglio annidato",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: testata (segno, nome, menu di Ultimate Addons, telefono),
  titolo inciso sulla lastra, riga sotto il foglio, frase, titoli e testi della distinta, foto a tutta larghezza
  (SG6, saldatura TIG, piegatrice) con le didascalie, racconto, persone, settori e note, contatti, sede, piede.
- Widget HTML (nodo RAW del motore) solo per le parti che Elementor gratuito non fa: la tavola della prima
  schermata (il letto del laser e le tre lastre SVG con i sei pezzi), il cartellino del pezzo scelto, le sei
  sagome della distinta, l'interruttore Ferro, Inox, Alluminio. Markup e script sono quelli della pagina statica,
  copiati da estrai_statica.py (foglio.html, cartellino.html, foglio.js, spessori.html, spessori.js, sagome.json).
- L'impaginazione (griglia a 12 colonne, misure fluide, punti di rottura 1180, 900, 699 e 359 px della statica)
  è il foglio di stile della pagina statica, con le classi tkl-, dentro i nodi RAW: vale uguale per il template
  Elementor e per il fallback HTML.

Testi e dati: tutti dalla home statica (verificati in 01-analisi.md). Nessun dato nuovo.
"""
import json
import os

import motore as m
from motore import C, H, T, I, RAW, MENU

QUI = os.path.dirname(os.path.abspath(__file__))

PREFISSO = 'tkl'
NOME_SITO = 'Tek.Lam'

# ---------------------------------------------------------------------------------------------
# Tema: i colori e i caratteri della home statica
# ---------------------------------------------------------------------------------------------
NERO = '#0b0907'           # il fondo del letto del laser
GRAFITE = '#15130f'        # testata, riga sotto il foglio, frase, contatti, piede
BIANCO = '#f4f1ea'         # la luce della scintilla, non bianco puro
GRIGIO_SCURO = '#a59e93'   # testo secondario sul grafite
CARTA = '#efece6'          # lamiera zincata appena passata
INCHIOSTRO = '#16130f'
GRIGIO = '#625b52'         # testo secondario sul chiaro
TESTO2 = '#3d3832'         # paragrafi sulla carta
PAGLIA = '#e2b46c'         # prima tinta di rinvenimento dell'acciaio
BRONZO = '#8a5a2b'         # la tinta che viene dopo, più vicina al taglio
FILO = 'rgba(244,241,234,.2)'
FILO_CHIARO = 'rgba(22,19,15,.18)'

DISP = 'Big Shoulders Display'     # titoli ed etichette dei pezzi
TESTO = 'Sofia Sans'               # paragrafi, didascalie, dati, telefono
# Sono gli stessi file woff2 della pagina statica (stesso md5 dei file latin di Google Fonts): da Google con l'API css2,
# oppure dal sito stesso con build.py --caratteri-locali (vedi caratteri_html).
GOOGLE_FONTS = ('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@100..900'
                '&family=Sofia+Sans:wght@1..1000&display=swap')


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# misure (1440, 1024, 390): quelle della pagina statica a quelle larghezze. Le misure fluide (clamp, vw, cqw) e i
# punti di rottura della statica sono nel foglio di stile e prevalgono sui valori del pannello di Elementor.
TEMA = {
    'nome': 'Foglio annidato',
    'fondo': GRAFITE, 'superficie': CARTA, 'inchiostro': INCHIOSTRO, 'testo2': TESTO2, 'accento': BRONZO,
    'filetto': FILO_CHIARO, 'filetto_scuro': FILO, 'su_scuro2': GRIGIO_SCURO,
    'scuro': GRAFITE, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': DISP, 'font_testo': TESTO, 'larghezza': 1440,
    'google_fonts': GOOGLE_FONTS,
    'stili': {
        'marchio':  _st(DISP, '700', (22, 22, 20), 1.0, 0.66),
        'nav':      _st(TESTO, '500', (16, 16, 16), 1.0),
        'tel':      _st(TESTO, '500', (16, 16, 15), 1.0),
        'h1':       _st(TESTO, '500', (26, 25.6, 17.2), 1.15, -0.08),
        'riga':     _st(TESTO, '400', (17, 17, 16), 1.45),
        'frase':    _st(DISP, '300', (108, 76.8, 46), 0.98, -1.3),
        'h2':       _st(DISP, '300', (88, 62.5, 48), 0.95, -1.06),
        'body':     _st(TESTO, '400', (18, 18, 17), 1.55),
        'num':      _st(DISP, '400', (24, 24, 20), 1.4),
        'nome':     _st(DISP, '500', (40, 34, 30), 1.0, -0.12),
        'dati':     _st(TESTO, '400', (18, 18, 16), 1.45),
        'didascalia': _st(TESTO, '400', (14, 14, 13), 1.4),
        'didascalia2': _st(TESTO, '400', (15, 15, 15), 1.45),
        'racconto': _st(TESTO, '400', (20, 20, 18), 1.55),
        'persone':  _st(TESTO, '400', (17, 17, 17), 1.45),
        'elenco':   _st(DISP, '300', (78, 55.3, 34), 1.06, -0.62),
        'note':     _st(TESTO, '400', (16, 16, 16), 1.5),
        'telefono': _st(TESTO, '200', (120, 86, 48.4), 0.9, -4.2),
        'invito':   _st(TESTO, '400', (22, 22, 19), 1.42),
        'h3':       _st(TESTO, '600', (15, 15, 15), 1.3),
        'recapiti': _st(TESTO, '400', (17, 17, 16), 1.5),
        'piede':    _st(TESTO, '400', (14, 14, 14), 1.6),
        'btn':      _st(TESTO, '600', (15, 15, 15), 1.2),
    },
    'spazi': {'sezione': (120, 120, 72), 'lato': (64, 40, 16), 'm': (24, 24, 12), 's': (12, 12, 12), '0': (0, 0, 0)},
    'bottoni': {},
    'bottone': {'raggio': 0, 'pad': (0, 0, 0, 0), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# Le immagini dei widget HTML (letto, lastra, ritagli dei pezzi del cartellino) restano a questo indirizzo:
# per non dipendere da GitHub si carica assets/web/ sul sito e si rigenera con build.py --base.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Teklam-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


# Caratteri: da Google Fonts (predefinito) oppure, con build.py --caratteri-locali, dai file di assets/web/fonts/
# caricati sul sito insieme alle immagini (alla base delle immagini), senza nessuna chiamata a Google.
CARATTERI_LOCALI = False


def imposta_caratteri_locali():
    global CARATTERI_LOCALI
    CARATTERI_LOCALI = True
    m.CARATTERI_HTML = caratteri_html()


def caratteri_html(preconnect=True):
    if not CARATTERI_LOCALI:
        pre = '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' if preconnect else ''
        return f'{pre}<link rel="stylesheet" href="{GOOGLE_FONTS}">'
    # le stesse @font-face della pagina statica (con il nome di famiglia di Google)
    latin = ('U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,'
             'U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD')
    ext = ('U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+20A0-20AB,U+20AD-20C0,U+2113,'
           'U+2C60-2C7F,U+A720-A7FF')
    return ('<style>'
            f'@font-face{{font-family:"Big Shoulders Display";src:url({img("fonts/bsd-latin.woff2")}) format("woff2");'
            'font-weight:100 900;font-display:swap}'
            f'@font-face{{font-family:"Sofia Sans";src:url({img("fonts/sofia-latin.woff2")}) format("woff2");'
            f'font-weight:1 1000;font-display:swap;unicode-range:{latin}}}'
            f'@font-face{{font-family:"Sofia Sans";src:url({img("fonts/sofia-latin-ext.woff2")}) format("woff2");'
            f'font-weight:1 1000;font-display:swap;unicode-range:{ext}}}'
            '</style>')


def img(nome):
    return BASE + nome


def leggi(nome):
    """Un pezzo della pagina statica (vedi estrai_statica.py), con la base delle immagini."""
    return open(os.path.join(QUI, nome), encoding='utf-8').read().strip().replace('%BASE%', BASE)


# ---------------------------------------------------------------------------------------------
# Dati aziendali (come nella home statica; le cose da confermare sono nel LEGGIMI)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}980{NBSP}14{NBSP}86'
TEL_LINK = 'tel:+390499801486'
UFFTEC = 'ufftec@teklam.it'

# voci del menu: in WordPress è il menu "Menu Tek.Lam" (link personalizzati verso le ancore della home)
VOCI_MENU = [('Lavorazioni', '/#lavorazioni'), ('Chi siamo', '/#storia'), ('Settori', '/#settori'), ('Contatti', '/#contatti')]


# Nei widget Testo il colore al passaggio del mouse (link_hover) è uguale a quello del link: Elementor lo usa anche
# per il fuoco, la statica no. Il colore al passaggio del mouse sta nei fogli di stile, con :hover.


def ap(html):
    """Apostrofo diritto come nella statica: WordPress (wptexturize) lo farebbe tipografico nei widget Testo."""
    return html.replace("'", '&#39;')


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def interno(sel):
    """Il contenuto di un widget: in Elementor può esserci .elementor-widget-container in mezzo, nel fallback no."""
    return f'{sel},{sel}>.elementor-widget-container'


# ---------------------------------------------------------------------------------------------
# Foglio di stile comune: variabili della pagina statica, caratteri, regole di base.
# Ogni sezione lo porta con sé (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
CSS_VARIABILI = (
    ':root{--nero:#0b0907;--grafite:#15130f;--bianco:#f4f1ea;--grigio-scuro:#a59e93;--carta:#efece6;--inchiostro:#16130f;'
    '--grigio:#625b52;--paglia:#e2b46c;--bronzo:#8a5a2b;--rosso:#e0281c;--filo:rgba(244,241,234,.2);'
    '--filo-chiaro:rgba(22,19,15,.18);--disp:"Big Shoulders Display","Arial Narrow",sans-serif;'
    '--f:"Sofia Sans",system-ui,sans-serif;--m:64px;--g:24px}'
    '@media (max-width:1180px){:root{--m:40px}}'
    '@media (max-width:900px){:root{--m:32px}}'
    '@media (max-width:699px){:root{--m:16px;--g:12px}}'
    # Elementor rende morbido lo scorrimento verso le ancore; la statica no
    'html{-webkit-text-size-adjust:100%;scroll-behavior:auto}'
)

# regole che valgono per tutto il sito: stanno nella testata (Elementor) e nella testata del fallback
CSS_SITO = (
    'body{margin:0;background:var(--grafite)!important;color:var(--bianco);font:400 18px/1.55 var(--f);font-kerning:normal;'
    'font-synthesis:none;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}'
    '@media (max-width:699px){body{font-size:17px}}'
    '.tkl-sito,.tkl-sito *,.tkl-sito *::before,.tkl-sito *::after{box-sizing:border-box}'
    '.tkl-sito .num{font-variant-numeric:tabular-nums lining-nums;white-space:nowrap}'
    '.tkl-sito .vh,.tkl-sito .tkl-vh,.tkl-sito .tkl-vh .elementor-heading-title{position:absolute!important;width:1px!important;'
    'height:1px!important;overflow:hidden!important;clip:rect(0 0 0 0)!important;white-space:nowrap!important;margin:0!important;padding:0!important}'
    '@media (prefers-reduced-motion:reduce){.tkl-sito .su,.tkl-sito .sp-a{transition:none!important}}'
)


def css_testi(scope):
    """Regole di base dei widget dentro una sezione, come le regole generali della statica: margini del tema e di
    Elementor azzerati, link del colore del testo (il tema Hello li colora di rosa), fuoco come nella statica."""
    s = f'.{scope}'
    return (
        f'{s}{{font-family:var(--f);font-size:18px;line-height:1.55;font-weight:400;font-synthesis:none;'
        '-webkit-font-smoothing:antialiased}'
        f'@media (max-width:699px){{{s}{{font-size:17px}}}}'
        f'{s} h1,{s} h2,{s} h3,{s} p,{s} ol,{s} ul,{s} dl,{s} dd,{s} figure,{s} blockquote,{s} .elementor-heading-title{{margin:0}}'
        f'{s} .elementor-widget-text-editor p,{s} :where(.tkl-w) p{{margin:0!important}}'
        f'{s} ol,{s} ul{{padding:0;list-style:none}}'
        # il fallback del motore bilancia titoli e paragrafi: la statica no (lo fa solo dove serve, più sotto)
        f'{s} h1,{s} h2,{s} h3,{s} p,{s} .elementor-heading-title{{text-wrap:wrap}}'
        f'{s} .elementor-widget:not(:last-child){{margin-block-end:0}}'
        f'{s} .elementor-widget{{margin:0}}'
        f'{s} a{{color:inherit;text-decoration:underline;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}}'
        f'{s} a:hover,{s} a:focus,{s} a:active{{color:inherit}}'
        # il reset del tema Hello aggiunge ai link a fuoco un anello: qui il fuoco della statica
        f'{s} :focus-visible{{outline:2px solid var(--paglia);outline-offset:3px}}'
        f'{s} a:focus-visible,{s} button:focus-visible{{box-shadow:none}}'
        f'{s} img{{display:block;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}'
    )


def contenitore(scope):
    """Un contenitore di Elementor (o del fallback) che si comporta come un blocco della statica."""
    return f'{scope}{{width:100%!important;max-width:none!important;margin:0!important;padding:0!important;gap:0!important;min-height:0!important}}'


WRAP = ('max-width:1440px!important;width:100%!important;margin:0 auto!important;padding:0 var(--m)!important;')
GRIGLIA = 'display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--g)!important;row-gap:0!important;'
# la riga di una griglia: i widget prendono la colonna dal foglio di stile, non dal contenitore flex di Elementor
FIGLI = '{s}>*{{width:auto!important;max-width:none!important;min-width:0}}'

CSS_COMUNE = (
    ':where(.tkl-sito) .tkl-wrap{' + WRAP + '}'
    ':where(.tkl-sito) .tkl-griglia{' + GRIGLIA + '}'
    + FIGLI.format(s=':where(.tkl-sito .tkl-griglia)') +
    # una foto a tutta larghezza (widget Immagine): il taglio verticale solo sul telefono, come <picture> nella statica
    ':where(.tkl-sito) .tkl-largo img,:where(.tkl-sito) .tkl-stretto img{width:100%!important;height:auto!important;max-width:none!important}'
    ':where(.tkl-sito) .tkl-stretto{display:none!important}'
    '@media (max-width:699px){:where(.tkl-sito) .tkl-largo{display:none!important}:where(.tkl-sito) .tkl-stretto{display:block!important}}'
    # il tema Hello scrive le didascalie in corsivo, grigie, a 16 px
    ':where(.tkl-sito) figcaption{font-style:normal;font-weight:400}'
)


# =============================================================================================
# TESTATA (template "Tek.Lam: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_MARCHIO = (
    '.tkl-sito .tkl-marchio{display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;align-items:center!important;'
    'gap:12px!important;text-decoration:none!important;color:var(--bianco)!important;padding:0!important;width:auto!important;'
    'min-height:0!important;margin:0!important}'
    '.tkl-sito .tkl-marchio>*{width:auto!important;flex:0 0 auto!important;max-width:none!important}'
    '.tkl-sito .tkl-marchio img{height:34px!important;width:auto!important;max-width:none!important;display:block}'
    + ht('.tkl-sito .tkl-marchio-nome') + '{font:700 22px/1 var(--disp)!important;letter-spacing:.03em!important;'
    'color:var(--bianco)!important;text-transform:none!important;white-space:nowrap}'
    '.tkl-sito .tkl-marchio-nome b{font-weight:800}.tkl-sito .tkl-marchio-nome span{font-weight:300}'
    '@media (max-width:699px){.tkl-sito .tkl-marchio img{height:30px!important}'
    + ht('.tkl-sito .tkl-marchio-nome') + '{font-size:20px!important}}'
)

CSS_TESTATA = (
    '.tkl-testa{height:56px!important;display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;'
    'align-items:center!important;gap:40px!important;padding:0 var(--m)!important;background:var(--grafite)!important;'
    'width:100%!important;max-width:none!important;margin:0!important;position:relative;color:var(--bianco);min-height:0!important}'
    '.tkl-testa>*{flex:0 0 auto!important;width:auto!important;max-width:none!important}'
    '.tkl-testa>.tkl-fuori{position:absolute!important;left:0;top:0;width:0!important;height:0!important;padding:0!important;'
    'overflow:visible;margin:0!important}'
    + CSS_MARCHIO +
    # menu: Ultimate Addons (Elementor) e il menu del fallback, a vista uguali al menu della pagina statica
    '.tkl-testa .tkl-menu{margin-left:auto!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.tkl-menu .tkl-nav-l{display:flex;flex-wrap:nowrap;gap:30px!important}'
    '.tkl-menu .hfe-nav-menu>li.menu-item{margin:0!important}'
    # il clearfix di Ultimate Addons (::before e ::after) diventerebbe una voce vuota della riga, con il suo spazio
    '.tkl-menu .hfe-nav-menu::before,.tkl-menu .hfe-nav-menu::after{display:none!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item,.tkl-menu .tkl-nav-l a{display:block!important;'
    'padding:8px 0!important;font:500 16px/1 var(--f)!important;letter-spacing:0!important;text-transform:none!important;'
    'color:var(--bianco)!important;text-decoration:none!important;white-space:nowrap;border:0!important;'
    'border-bottom:1px solid transparent!important;transition:border-color .15s,color .15s;background:none!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item:hover,.tkl-menu .tkl-nav-l a:hover{'
    'border-bottom-color:currentColor!important;color:var(--paglia)!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::before,.tkl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::after,'
    '.tkl-menu .hfe-pointer__underline a.hfe-menu-item::after{display:none!important}'
    '.tkl-menu .tkl-nav-l a[aria-current]{border-bottom-width:1px!important;padding-bottom:8px!important}'
    '.tkl-menu .tkl-nav-l a[aria-current]:not(:hover){border-bottom-color:transparent!important}'
    '.tkl-menu details,.tkl-menu .hfe-nav-menu__toggle{display:none!important}'
    # Ultimate Addons e il fallback passano al menu a scomparsa a 1024 px; la statica a 900 toglie il menu: fino a 901 resta in riga
    '@media (min-width:901px){'
    '.tkl-menu .hfe-nav-menu__layout-horizontal,.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu{visibility:visible!important;'
    'opacity:1!important;height:auto!important;position:static!important;display:flex!important;background:none!important;'
    'border:0!important;box-shadow:none!important;width:auto!important;left:auto!important;top:auto!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal li.menu-item{width:auto!important;background:none!important;border:0!important}'
    '.tkl-menu .tkl-nav-l{display:flex!important}}'
    '.tkl-testa .tkl-tel{margin-left:14px!important}'
    '.tkl-testa .tkl-tel p{margin:0!important}'
    '.tkl-testa .tkl-tel a{display:block;font:500 16px/1 var(--f)!important;color:var(--bianco)!important;text-decoration:none!important;'
    'padding:8px 0;border-bottom:1px solid transparent;transition:border-color .15s,color .15s;font-variant-numeric:tabular-nums!important;white-space:nowrap}'
    '.tkl-testa .tkl-tel a:hover{border-bottom-color:currentColor;color:var(--paglia)!important}'
    '@media (max-width:1180px){.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.tkl-menu .tkl-nav-l{gap:22px!important}}'
    '@media (max-width:900px){.tkl-testa .tkl-menu{display:none!important}.tkl-testa .tkl-tel{margin-left:auto!important}}'
    '@media (max-width:699px){.tkl-testa{height:52px!important;gap:16px!important}.tkl-testa .tkl-tel a{font-size:15px!important}}'
)

CSS_TESTATA_ELEMENTOR = (
    '#masthead{position:static}'
    '.hfe-skip-link{display:none!important}'
    '.tkl-menu .hfe-nav-menu li.current-menu-item>a.hfe-menu-item:not(:hover){color:var(--bianco)!important}'
)


def marchio():
    return C(I(img('logo-segno.png'), alt='Segno del marchio Tek.Lam'),
             H('<b>TEK</b>.<span>LAM</span>', level='div', style='marchio', color=BIANCO, css='tkl-marchio-nome'),
             dir='row', align='center', gap=12, boxed=False, link='/', css='tkl-marchio')


def header():
    menu = MENU(VOCI_MENU, colore=BIANCO, colore_hover=PAGLIA, accento=PAGLIA, fondo_menu=GRAFITE, linea=FILO,
                stile='nav', spazio=30, pad_h=0, pad_v=8, distanza=12, align_menu='right', slug='menu-tek-lam', css='tkl-menu')
    tel = T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='tel', color=BIANCO, link_color=BIANCO, link_hover=BIANCO,
            sottolinea=False, css='tkl-tel')
    globali = RAW('', css=CSS_VARIABILI + CSS_SITO + CSS_COMUNE + css_testi('tkl-testa') + CSS_TESTATA)
    # solo in Elementor: i caratteri (nel fallback il <link> lo scrive già il motore) e le regole di Ultimate Addons
    caratteri = RAW(caratteri_html(), css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    fuori = C(globali, caratteri, boxed=False, css='tkl-fuori')
    return C(fuori, marchio(), menu, tel, dir='row', align='center', gap=40, boxed=False, pad=0, tag='header', bg=GRAFITE,
             css='tkl-testa tkl-sito')


# =============================================================================================
# PIEDE (template "Tek.Lam: Footer")
# =============================================================================================
CSS_PIEDE = (
    contenitore('.tkl-piede') +
    '.tkl-piede{background:var(--grafite)!important;color:var(--grigio-scuro);padding:40px 0 44px!important;font-size:14px;'
    'line-height:1.6;border-top:1px solid var(--filo)!important;display:block!important}'
    '.tkl-piede .tkl-griglia{row-gap:20px!important;align-items:start!important}'
    '.tkl-piede .tkl-marchio{grid-column:1/4}'
    '.tkl-piede .tkl-soc{grid-column:4/9}'
    '.tkl-piede .tkl-soc,.tkl-piede .tkl-soc p,.tkl-piede .tkl-link-piede,.tkl-piede .tkl-link-piede p{font:400 14px/1.6 var(--f)!important;'
    'color:var(--grigio-scuro)!important}'
    '.tkl-piede .tkl-soc b{color:var(--bianco);font-weight:600}'
    '.tkl-piede .tkl-link-piede{grid-column:9/13}'
    '.tkl-piede .tkl-link-piede p{display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:flex-end}'
    '.tkl-piede .tkl-link-piede a{text-decoration:none!important;color:var(--bianco)!important}'
    '.tkl-piede .tkl-link-piede a:hover{color:var(--paglia)!important;text-decoration:underline!important}'
    '@media (max-width:900px){.tkl-piede .tkl-marchio{grid-column:1/13}.tkl-piede .tkl-soc{grid-column:1/8}'
    '.tkl-piede .tkl-link-piede{grid-column:8/13}}'
    '@media (max-width:699px){.tkl-piede .tkl-soc,.tkl-piede .tkl-link-piede{grid-column:1/13}'
    '.tkl-piede .tkl-link-piede p{justify-content:flex-start}}'
)


def footer():
    soc = T('<p><b>TEK.LAM S.R.L.</b>, carpenteria in lamiera conto terzi<br>Via del Lavoro 68, zona artigianale Tombelle, '
            '30030 Vigonovo (VE)<br>C.F. e P.IVA <span class="num">04595530272</span></p>',
            style='piede', color=GRIGIO_SCURO, css='tkl-soc')
    link = T('<p>'
             '<a href="https://www.facebook.com/Tek.lamsrl/">Facebook</a> '
             '<a href="https://www.instagram.com/teklam_srl/">Instagram</a> '
             '<a href="https://www.linkedin.com/company/tek-lam-srl">LinkedIn</a> '
             '<a href="http://www.teklam.it/privacy-contatti/">Privacy</a> '
             '<a href="http://www.teklam.it/cookie/">Cookie</a></p>',
             style='piede', color=BIANCO, link_color=BIANCO, link_hover=BIANCO, sottolinea=False, css='tkl-link-piede')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + CSS_MARCHIO + css_testi('tkl-piede') + CSS_PIEDE)
    riga = C(marchio(), soc, link, boxed=False, css='tkl-wrap tkl-griglia')
    return C(stile, riga, tag='footer', boxed=False, pad=0, bg=GRAFITE, css='tkl-piede tkl-sito')


# =============================================================================================
# HOME
# =============================================================================================

# --- 1. Il foglio: la tavola (widget HTML), il titolo inciso (widget Titolo), il cartellino (widget HTML)
CSS_APERTURA = (
    contenitore('.tkl-apertura') +
    '.tkl-apertura{display:block!important;background:var(--grafite)!important;color:var(--bianco)}'
    '.tkl-apertura .tkl-foglio{position:relative!important;display:block!important;width:min(100%,calc((100svh - 56px) * 2))!important;'
    'max-width:none!important;margin:0 auto!important;padding:0!important;aspect-ratio:2/1;background:#1b140d!important;'
    'container-type:inline-size;min-height:0!important}'
    # i due widget HTML non fanno scatola: tavola e cartellino si posizionano nel foglio, come nella statica
    '.tkl-foglio>.elementor-widget-html,.tkl-foglio>.elementor-widget-html>.elementor-widget-container,.tkl-foglio>.tkl-w{display:contents!important}'
    '.tkl-foglio .tavola{position:absolute;inset:0;overflow:hidden}'
    '.tkl-foglio .letto{position:absolute;inset:0}'
    '.tkl-foglio .letto img{width:100%;height:100%;object-fit:cover;max-width:100%;display:block}'
    '.tkl-foglio svg{position:absolute;inset:0;width:100%;height:100%;display:block}'
    '.tkl-foglio .foglio-m,.tkl-foglio .foglio-v{display:none}'
    '.tkl-foglio .foglio-h,.tkl-foglio .foglio-m{--l1x:-6px;--l1y:-10px;--l2x:-21px;--l2y:-33px}'
    '.tkl-foglio .foglio-h{--o1:url(#alza-h);--o2:url(#solleva-h)}'
    '.tkl-foglio .foglio-m{--o1:url(#alza-m);--o2:url(#solleva-m)}'
    '.tkl-foglio .foglio-v{--l1x:-8px;--l1y:-12px;--l2x:-16px;--l2y:-26px;--o1:url(#alza-v);--o2:url(#solleva-v)}'
    '.tkl-foglio .t-paglia{fill:none;stroke:var(--paglia);stroke-opacity:.24;stroke-linejoin:round}'
    '.tkl-foglio .t-bronzo{fill:none;stroke:var(--bronzo);stroke-opacity:.46;stroke-linejoin:round}'
    '.tkl-foglio .piega{fill:none;stroke:#3a342c;stroke-opacity:.75}'
    '.tkl-foglio .rosso{fill:none;stroke:var(--rosso);stroke-linejoin:round;opacity:0}'
    '.tkl-foglio .presa{fill:transparent;pointer-events:all}'
    '.tkl-foglio .pz{cursor:pointer;outline:none;-webkit-tap-highlight-color:transparent}'
    '.tkl-foglio .pz.on .rosso{opacity:1}'
    '.tkl-foglio .su{transform-box:view-box;transition:transform .22s cubic-bezier(.2,.7,.2,1)}'
    '.tkl-foglio .pz:hover .su,.tkl-foglio .pz:focus-visible .su{transform:translate(var(--l1x),var(--l1y));filter:var(--o1)}'
    '.tkl-foglio .pz.on .su{transform:translate(var(--l2x),var(--l2y));filter:var(--o2)}'
    '.tkl-foglio .pz:focus-visible{outline:none}'
    '.tkl-foglio .et{font:600 33.4px var(--disp);fill:#1d1914;letter-spacing:.01em;text-rendering:geometricPrecision}'
    '.tkl-foglio .et-n{font-weight:400;fill:#4a4239}'
    '.tkl-foglio .pz:focus-visible .et{text-decoration:underline;text-decoration-thickness:3px}'
    '.tkl-foglio .foglio-m .et{font-size:44px}'
    '.tkl-foglio .foglio-v .et{font-size:56px}'
    '.tkl-foglio .quota path{fill:none;stroke:rgba(29,25,20,.55)}'
    '.tkl-foglio .quota text{font:500 27px var(--f);font-variant-numeric:tabular-nums lining-nums;fill:rgba(29,25,20,.75);letter-spacing:.04em}'
    # il titolo inciso: widget Titolo nativo, nel foglio come l'h1 della statica (fra 700 e 1180 px la tavola
    # è alta 1500/2400 del foglio: la stessa posizione scritta in cqw)
    '.tkl-foglio .tkl-incisione{position:absolute!important;z-index:2;pointer-events:none;left:4.43%;top:40.5%;width:72%!important;'
    'max-width:none!important;margin:0!important;padding:0!important;display:block!important;min-height:0!important}'
    + ht('.tkl-foglio .tkl-incisione h1') + '{font:500 calc(100cqw * 54.2 / 3000)/1.15 var(--f)!important;letter-spacing:-.003em!important;'
    'color:rgba(26,22,17,.9)!important;text-wrap:balance!important;text-transform:none!important;margin:0!important}'
    # il cartellino del pezzo scelto: inciso sul resto del foglio, senza riquadro
    '.tkl-foglio .cartellino{position:absolute;z-index:3;left:77.4%;top:6.2%;width:20.5%;color:#1f1a14;'
    'text-shadow:0 1px 0 rgba(250,246,238,.42);font-size:max(13px,1.0417cqw);line-height:1.4}'
    '.tkl-foglio .c-vano{display:block;position:relative;background:var(--nero);box-shadow:0 0 0 1.5px rgba(138,90,43,.6),'
    '0 0 0 3.5px rgba(226,180,108,.2),1px 1px 0 3.5px rgba(244,241,234,.5),-1px -1px 0 3.5px rgba(23,18,12,.55)}'
    '.tkl-foglio .c-vano::after{content:"";position:absolute;inset:0;box-shadow:inset 2px 3px 7px rgba(8,5,2,.7),'
    'inset 0 0 0 1px rgba(10,7,4,.9);pointer-events:none}'
    '.tkl-foglio .c-vano img{width:100%;aspect-ratio:1.45;object-fit:cover;display:block;max-width:100%;height:auto}'
    '.tkl-foglio .c-cap{margin-top:12px;font-size:max(12.5px,.903cqw);line-height:1.38;color:#2f2922}'
    '.tkl-foglio .c-testo{margin-top:max(14px,1.25cqw);padding-top:max(10px,.9cqw);border-top:1px solid rgba(31,26,20,.28)}'
    '.tkl-foglio .c-nome{font:600 max(26px,2.222cqw)/1 var(--disp);letter-spacing:.005em;color:inherit;margin:0}'
    '.tkl-foglio .c-dato{margin-top:8px!important}'
    '.tkl-foglio .c-link{display:inline-block;margin-top:max(8px,.76cqw);font-weight:600;text-underline-offset:4px!important;padding:2px 0}'
    '.tkl-foglio .c-link:hover{color:var(--bronzo)}'
    '.tkl-foglio .c-dato a{font-weight:600}'
    # la riga sotto il foglio
    '.tkl-apertura .tkl-piede-foglio{' + GRIGLIA + 'align-items:start!important;padding:28px var(--m) 32px!important;'
    'width:100%!important;max-width:none!important;margin:0!important}'
    + FIGLI.format(s='.tkl-apertura .tkl-piede-foglio') +
    '.tkl-piede-foglio .tkl-pf,.tkl-piede-foglio .tkl-pf p{font:400 17px/1.45 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-piede-foglio .tkl-pf-chi{grid-column:1/6}'
    '.tkl-piede-foglio .tkl-pf-dove{grid-column:6/10}'
    '.tkl-piede-foglio .tkl-pf-dove,.tkl-piede-foglio .tkl-pf-dove p{color:var(--grigio-scuro)!important}'
    '.tkl-piede-foglio .tkl-pf-primo{grid-column:10/13;justify-self:end;text-align:right}'
    '.tkl-piede-foglio .tkl-pf-primo p{font-weight:600!important;text-align:right}'
    '.tkl-piede-foglio .tkl-pf-primo a{color:var(--paglia)!important;text-underline-offset:5px!important;padding:2px 0;'
    'transition:background-color .15s,color .15s,box-shadow .15s}'
    '.tkl-piede-foglio .tkl-pf-primo a:hover{background:var(--paglia);color:var(--nero)!important;box-shadow:0 0 0 6px var(--paglia);'
    'text-decoration:none!important}'
    '@media (max-width:1180px){'
    '.tkl-apertura .tkl-foglio{aspect-ratio:auto;background:var(--grafite)!important}'
    '.tkl-foglio .tavola{position:relative;aspect-ratio:2400/1500}'
    '.tkl-foglio .foglio-h{display:none}.tkl-foglio .foglio-m{display:block}'
    '.tkl-foglio .tkl-incisione{left:5.54%;top:25.3125cqw;width:90%!important}'
    + ht('.tkl-foglio .tkl-incisione h1') + '{font-size:calc(100cqw * 60 / 2400)!important}'
    '.tkl-foglio .cartellino{position:static;width:auto;display:grid;grid-template-columns:240px minmax(0,1fr);column-gap:32px;'
    'align-items:start;padding:28px var(--m) 30px;color:var(--bianco);text-shadow:none;font-size:16px;min-height:294px}'
    '.tkl-foglio .c-vano{box-shadow:none}'
    '.tkl-foglio .c-vano::after{box-shadow:inset 0 0 0 1px rgba(244,241,234,.12)}'
    '.tkl-foglio .c-cap{color:var(--grigio-scuro);font-size:14px}'
    '.tkl-foglio .c-testo{margin-top:0;padding-top:0;border-top:0;max-width:34em}'
    '.tkl-foglio .c-nome{font-size:34px}'
    '.tkl-foglio .c-link:hover{color:var(--paglia)}'
    '.tkl-apertura .tkl-piede-foglio{border-top:1px solid var(--filo)!important}'
    '.tkl-piede-foglio .tkl-pf-chi{grid-column:1/6}'
    '.tkl-piede-foglio .tkl-pf-dove{grid-column:6/13}'
    '.tkl-piede-foglio .tkl-pf-primo{grid-column:6/13;justify-self:start;text-align:left;margin-top:10px!important}'
    '.tkl-piede-foglio .tkl-pf-primo p{text-align:left}'
    '.tkl-piede-foglio .a-capo{display:none}}'
    '@media (max-width:900px){'
    '.tkl-foglio .cartellino{grid-template-columns:200px minmax(0,1fr);column-gap:24px;min-height:268px}'
    '.tkl-apertura .tkl-piede-foglio{row-gap:12px!important}'
    '.tkl-piede-foglio .tkl-pf-chi,.tkl-piede-foglio .tkl-pf-dove,.tkl-piede-foglio .tkl-pf-primo{grid-column:1/13}'
    '.tkl-piede-foglio .tkl-pf-primo{margin-top:0!important}}'
    '@media (max-width:699px){'
    '.tkl-apertura .tkl-foglio{width:100%!important;aspect-ratio:1/2;background:#1b140d!important}'
    '.tkl-foglio .tavola{position:absolute;inset:0;aspect-ratio:auto}'
    '.tkl-foglio .foglio-m{display:none}.tkl-foglio .foglio-v{display:block}'
    '.tkl-foglio .tkl-incisione{left:4.27%;top:38.4%;width:91%!important}'
    + ht('.tkl-foglio .tkl-incisione h1') + '{font-size:calc(100cqw * 66 / 1500)!important;line-height:1.22!important}'
    '.tkl-foglio .cartellino{position:absolute;left:4.27%;right:4.27%;top:85.2%;bottom:1.6%;width:auto;padding:0;'
    'grid-template-columns:34% minmax(0,1fr);grid-template-rows:auto auto 1fr;column-gap:12px;align-items:start;'
    'color:#1f1a14;text-shadow:0 1px 0 rgba(250,246,238,.42);font-size:14px;min-height:0}'
    '.tkl-foglio .cartellino figure,.tkl-foglio .cartellino .c-testo{display:contents}'
    '.tkl-foglio .c-vano{grid-column:1;grid-row:1/4;align-self:center;box-shadow:0 0 0 1.5px rgba(138,90,43,.6),'
    '0 0 0 3px rgba(226,180,108,.2),1px 1px 0 3px rgba(244,241,234,.5),-1px -1px 0 3px rgba(23,18,12,.55)}'
    '.tkl-foglio .c-vano::after{box-shadow:inset 2px 3px 6px rgba(8,5,2,.7),inset 0 0 0 1px rgba(10,7,4,.9)}'
    '.tkl-foglio .c-nome{grid-column:2;grid-row:1;font-size:24px;align-self:start}'
    '.tkl-foglio .c-cap{grid-column:2;grid-row:2;margin-top:4px;font-size:13px;line-height:1.3;color:#2f2922;display:-webkit-box;'
    '-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}'
    '.tkl-foglio .c-dato,.tkl-foglio .c-fonte{display:none}'
    '.tkl-foglio .c-link{grid-column:2;grid-row:3;align-self:end;margin-top:2px;font-size:14px;padding:6px 0}'
    '.tkl-foglio .c-link:hover{color:var(--bronzo)}'
    '.tkl-apertura .tkl-piede-foglio{display:block!important;padding:22px var(--m) 26px!important;border-top:0!important}'
    '.tkl-piede-foglio .tkl-pf,.tkl-piede-foglio .tkl-pf p{font-size:16px!important}'
    '.tkl-piede-foglio .tkl-pf-dove{margin-top:8px!important}'
    '.tkl-piede-foglio .tkl-pf-primo{margin-top:0!important}}'
    '@media (max-width:359px){'
    '.tkl-foglio .c-cap{font-size:12.5px;line-height:1.25}'
    '.tkl-foglio .c-nome{font-size:21px}'
    '.tkl-foglio .c-link{padding:3px 0;font-size:13.5px}}'
)


def apertura():
    tavola = RAW(leggi('foglio.html'))
    titolo = C(H('Lamiera tagliata, punzonata, piegata e saldata per conto terzi, a Vigonovo', level='h1', style='h1',
                 color='rgba(26,22,17,.9)'),
               boxed=False, anchor='titolo-foglio', css='tkl-incisione')
    cartellino = RAW(leggi('cartellino.html') + '<script>' + leggi('foglio.js') + '</script>',
                     css=CSS_VARIABILI + css_testi('tkl-apertura') + CSS_APERTURA)
    foglio = C(tavola, titolo, cartellino, boxed=False, css='tkl-foglio')
    riga = C(
        T(ap("<p>Tek.Lam S.r.l., carpenteria in lamiera conto terzi.<br class=\"a-capo\"> L'esperienza dei fondatori, dal&nbsp;1978.</p>"),
          style='riga', color=BIANCO, css='tkl-pf tkl-pf-chi'),
        T('<p>Zona artigianale di Tombelle, Vigonovo (VE),<br class="a-capo"> vicino al casello A13 di Padova Interporto.</p>',
          style='riga', color=GRIGIO_SCURO, css='tkl-pf tkl-pf-dove'),
        T(f'<p><a href="mailto:{UFFTEC}">Mandaci il disegno:<br class="a-capo"> {UFFTEC}</a></p>',
          style='riga', color=PAGLIA, link_color=PAGLIA, link_hover=PAGLIA, css='tkl-pf tkl-pf-primo'),
        boxed=False, css='tkl-piede-foglio')
    # i caratteri anche qui: se la testata globale manca, la home li carica comunque (solo Elementor)
    caratteri = RAW(caratteri_html(preconnect=False), solo_elementor=True)
    return C(foglio, riga, caratteri, boxed=False, pad=0, tag='section', bg=GRAFITE, css='tkl-apertura tkl-sito')


# --- 2. La frase
CSS_FRASE = (
    contenitore('.tkl-frase') +
    '.tkl-frase{padding:120px 0 132px!important;display:block!important;background:var(--grafite)!important;color:var(--bianco)}'
    '.tkl-frase .tkl-frase-testo,.tkl-frase .tkl-frase-testo p{font:300 clamp(46px,7.5vw,108px)/.98 var(--disp)!important;'
    'letter-spacing:-.012em!important;color:var(--bianco)!important}'
    '.tkl-frase .tkl-frase-testo p{max-width:13.4em;text-wrap:balance!important}'
    '@media (max-width:699px){.tkl-frase{padding:72px 0 80px!important}'
    '.tkl-frase .tkl-frase-testo,.tkl-frase .tkl-frase-testo p{font-size:46px!important;line-height:1!important}}'
)


def frase():
    testo = T('<p>Non vendiamo un prodotto nostro: facciamo i pezzi del prodotto degli altri.</p>', style='frase', color=BIANCO,
              css='tkl-frase-testo')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-frase') + CSS_FRASE)
    return C(stile, C(testo, boxed=False, css='tkl-wrap'), boxed=False, pad=0, tag='section', bg=GRAFITE,
             css='tkl-frase tkl-sito')


# --- 3. Dal foglio al pezzo finito: la distinta, con la SG6 a tutta larghezza dopo la riga 02
CSS_CARTA = (
    '.tkl-carta{background:var(--carta)!important;color:var(--inchiostro)}'
    '.tkl-carta a:hover{color:var(--bronzo)!important}'
    + ht('.tkl-carta .tkl-titolo') + '{font:300 clamp(48px,6.1vw,88px)/.95 var(--disp)!important;letter-spacing:-.012em!important;'
    'color:var(--inchiostro)!important;text-transform:none!important}'
    '.tkl-carta .tkl-titolo{grid-column:1/10}'
    '.tkl-carta .tkl-didascalia,.tkl-carta .tkl-didascalia p{font:400 14px/1.4 var(--f)!important;color:var(--grigio)!important}'
    '@media (max-width:900px){.tkl-carta .tkl-titolo{grid-column:1/13}}'
    '@media (max-width:699px){' + ht('.tkl-carta .tkl-titolo') + '{font-size:48px!important}}'
)

CSS_LAVORAZIONI = (
    contenitore('.tkl-lavorazioni') +
    '.tkl-lavorazioni{padding:120px 0 0!important;display:block!important}'
    '.tkl-lavorazioni .tkl-intro{grid-column:1/7;margin-top:28px!important;max-width:34em!important}'
    '.tkl-lavorazioni .tkl-intro,.tkl-lavorazioni .tkl-intro p{font:400 18px/1.55 var(--f)!important;color:#3d3832!important}'
    '.tkl-lavorazioni .tkl-distinta{margin-top:80px!important;display:block!important}'
    '.tkl-distinta .tkl-riga{' + GRIGLIA + 'padding:28px 0 30px!important;border-top:1px solid var(--filo-chiaro)!important;'
    'scroll-margin-top:24px;width:100%!important;max-width:none!important;margin:0!important;min-height:0!important}'
    + FIGLI.format(s='.tkl-distinta .tkl-riga') +
    '.tkl-riga .tkl-d-n{grid-column:1/2}'
    '.tkl-riga .tkl-d-n,.tkl-riga .tkl-d-n p{font:400 24px/1.4 var(--disp)!important;color:var(--grigio)!important}'
    '.tkl-riga .tkl-d-sag{grid-column:2/3;padding:4px 0 0!important;display:block!important;min-height:0!important}'
    '.tkl-riga .tkl-d-sag>*{display:block}'
    '.tkl-riga .sagoma{display:block;width:auto;max-width:64px;height:auto;max-height:76px;overflow:visible}'
    '.tkl-riga .sagoma path{fill:#3a342d}'
    '.tkl-riga .sagoma .bp{fill:none;stroke:var(--carta);stroke-width:.8;stroke-dasharray:2 1.5}'
    '.tkl-riga .tkl-d-nome{grid-column:3/7}'
    + ht('.tkl-riga .tkl-d-nome') + '{font:500 40px/1 var(--disp)!important;letter-spacing:-.003em!important;'
    'color:var(--inchiostro)!important;text-transform:none!important}'
    '.tkl-riga .tkl-d-m{grid-column:7/13}'
    '.tkl-riga .tkl-d-m ul{margin:0!important;padding:0!important;list-style:none!important}'
    '.tkl-riga .tkl-d-m li{display:flex;justify-content:space-between;gap:24px;padding:3px 0!important;margin:0!important;border:0!important;'
    'font:400 18px/1.45 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-riga .tkl-d-m li span:last-child{text-align:right;color:#3d3832;font-variant-numeric:tabular-nums lining-nums}'
    '.tkl-riga .tkl-d-testo{grid-column:7/13;max-width:36em!important}'
    '.tkl-riga .tkl-d-testo,.tkl-riga .tkl-d-testo p{font:400 18px/1.55 var(--f)!important;color:#3d3832!important}'
    '.tkl-distinta .tkl-d-chiudi{border-bottom:1px solid var(--filo-chiaro)!important}'
    # l'interruttore degli spessori, nella riga 01
    '.tkl-riga .tkl-d-sp{grid-column:7/13;margin-top:18px!important;max-width:420px!important;display:block!important;padding:0!important;'
    'min-height:0!important}'
    '.tkl-riga .tkl-d-sp>*{display:block}'
    '.tkl-riga .sp-scelta{display:flex;border:1px solid rgba(22,19,15,.35)}'
    '.tkl-riga .sp-scelta button,.tkl-riga .sp-scelta button:hover,.tkl-riga .sp-scelta button:focus{flex:1;appearance:none;-webkit-appearance:none;'
    'border:0;border-radius:0;background:transparent;font:500 15px/1 var(--f);color:var(--inchiostro);padding:10px 6px;min-height:44px;'
    'cursor:pointer;transition:background-color .15s,color .15s;text-transform:none;letter-spacing:0;box-shadow:none;margin:0;'
    'white-space:nowrap}'
    '.tkl-riga .sp-scelta button+button{border-left:1px solid rgba(22,19,15,.35)}'
    '.tkl-riga .sp-scelta button:hover{background:#e3ddd1}'
    '.tkl-riga .sp-scelta button[aria-checked="true"]{background:var(--inchiostro);color:var(--paglia)}'
    '.tkl-riga .sp-scelta button:focus-visible{outline:2px solid var(--bronzo);outline-offset:-4px;box-shadow:none}'
    '.tkl-riga .sp-tavola{position:relative;height:20mm;margin-top:18px}'
    '.tkl-riga .sp-scala{position:absolute;left:0;bottom:0;width:9px;height:20mm;color:#8b8378}'
    '.tkl-riga .sp-scala::before{content:"";position:absolute;right:0;bottom:0;width:4px;height:100%;'
    'background:repeating-linear-gradient(to top,currentColor 0 1px,transparent 1px 1mm)}'
    '.tkl-riga .sp-scala::after{content:"";position:absolute;right:0;bottom:0;width:9px;height:100%;'
    'background:repeating-linear-gradient(to top,currentColor 0 1px,transparent 1px 5mm)}'
    '.tkl-riga .sp-a{position:absolute;left:18px;right:0;bottom:0;height:calc(var(--a) * 1mm);border:1.5px solid var(--inchiostro);'
    'background-color:#e2dccf;background-image:repeating-linear-gradient(-45deg,var(--bronzo) 0 1px,transparent 1px 1.6mm);'
    'transition:height .22s cubic-bezier(.3,.7,.2,1)}'
    '.tkl-riga .sp-cap{margin-top:10px!important;font-size:15px;line-height:1.45;color:var(--grigio)}'
    '.tkl-riga .sp-cap output{color:var(--inchiostro);font-weight:600}'
    # la SG6 a tutta larghezza
    '.tkl-lavorazioni .tkl-striscia{margin:20px 0 0!important;display:block!important;padding:0!important}'
    '.tkl-lavorazioni .tkl-striscia .tkl-didascalia{padding:10px var(--m) 0!important;text-align:right}'
    '.tkl-lavorazioni .tkl-striscia .tkl-didascalia p{text-align:right}'
    # nella statica i margini si fondono: 48 px sotto la foto, 80 sopra la distinta, resta il più grande
    '.tkl-lavorazioni .tkl-distinta+.tkl-striscia+.tkl-distinta,.tkl-lavorazioni .tkl-distinta-2{margin-top:80px!important}'
    '@media (max-width:1180px){' + ht('.tkl-riga .tkl-d-nome') + '{font-size:34px!important}}'
    '@media (max-width:900px){'
    '.tkl-lavorazioni .tkl-intro{grid-column:1/13}'
    '.tkl-riga .tkl-d-nome{grid-column:3/13}'
    '.tkl-riga .tkl-d-m,.tkl-riga .tkl-d-testo,.tkl-riga .tkl-d-sp{grid-column:3/13;margin-top:14px!important}'
    '.tkl-riga .tkl-d-sp{margin-top:20px!important}}'
    '@media (max-width:699px){'
    '.tkl-lavorazioni{padding-top:72px!important}'
    '.tkl-lavorazioni .tkl-intro,.tkl-lavorazioni .tkl-intro p{font-size:17px!important}'
    '.tkl-lavorazioni .tkl-distinta{margin-top:44px!important}'
    '.tkl-lavorazioni .tkl-distinta-2{margin-top:48px!important}'
    '.tkl-distinta .tkl-riga{padding:22px 0!important;grid-template-columns:28px minmax(0,1fr) 56px;column-gap:10px!important}'
    '.tkl-riga .tkl-d-n{grid-column:1;grid-row:1}'
    '.tkl-riga .tkl-d-n,.tkl-riga .tkl-d-n p{font-size:20px!important;line-height:1.5!important}'
    '.tkl-riga .tkl-d-nome{grid-column:2;grid-row:1;align-self:start}'
    + ht('.tkl-riga .tkl-d-nome') + '{font-size:30px!important}'
    '.tkl-riga .tkl-d-sag{grid-column:3;grid-row:1/3;justify-self:end}'
    '.tkl-riga .sagoma{max-width:48px;max-height:56px}'
    '.tkl-riga .tkl-d-m,.tkl-riga .tkl-d-testo,.tkl-riga .tkl-d-sp{grid-column:1/3;grid-row:2;margin-top:12px!important}'
    '.tkl-riga .tkl-d-sp{grid-column:1/4;grid-row:3;margin-top:18px!important;max-width:none!important}'
    '.tkl-riga .tkl-d-m li{display:block;font-size:16px!important;padding:5px 0!important}'
    # nella statica il testo della riga eredita il corpo, che sul telefono è di 17 px
    '.tkl-riga .tkl-d-testo,.tkl-riga .tkl-d-testo p{font-size:17px!important}'
    '.tkl-riga .tkl-d-m li>span{display:block}'
    '.tkl-riga .tkl-d-m li>span:last-child{text-align:left;color:var(--grigio)}'
    '.tkl-lavorazioni .tkl-striscia .tkl-didascalia,.tkl-lavorazioni .tkl-striscia .tkl-didascalia p{text-align:left!important;font-size:13px!important}}'
)

SAGOME = json.loads(open(os.path.join(QUI, 'sagome.json'), encoding='utf-8').read())


def riga(n, nome, dati=None, testo=None, extra=None, chiudi=False):
    """Una riga della distinta: numero, sagoma, nome, macchine e misure (o un testo)."""
    figli = []
    if n:
        figli.append(T(f'{n:02d}', style='num', color=GRIGIO, css='tkl-d-n'))
        figli.append(C(RAW(SAGOME[n - 1]), boxed=False, css='tkl-d-sag'))
    figli.append(H(nome, level='h3', style='nome', color=INCHIOSTRO, css='tkl-d-nome'))
    if dati:
        voci = ''.join(f'<li><span>{a}</span><span>{b}</span></li>' for a, b in dati)
        figli.append(T(ap(f'<ul>{voci}</ul>'), style='dati', color=INCHIOSTRO, css='tkl-d-m'))
    if testo:
        figli.append(T(ap(f'<p>{testo}</p>'), style='body', color=TESTO2, css='tkl-d-testo'))
    if extra:
        figli.append(extra)
    return C(*figli, boxed=False, anchor=f'l-{n:02d}' if n else None,
             css='tkl-riga' + (' tkl-d-chiudi' if chiudi else ''))


def foto_larga(largo, stretto, alt, didascalia, css, stile_didascalia='didascalia'):
    """Una foto a tutta larghezza: due widget Immagine (il taglio largo e, solo sul telefono, quello verticale)
    e la didascalia, come il <figure> con il <picture> della statica."""
    # le proporzioni del file originale: WordPress serve anche le sue misure ridotte, con l'altezza arrotondata
    proporzioni = RAW('', css=''.join(f'.tkl-sito .tkl-f-{n.split(".")[0]} img{{aspect-ratio:{DIM[n][0]}/{DIM[n][1]}}}'
                                      for n in (largo, stretto)))
    return C(proporzioni, I(img(largo), alt=alt, css='tkl-largo tkl-f-' + largo.split('.')[0]),
             I(img(stretto), alt=alt, css='tkl-stretto tkl-f-' + stretto.split('.')[0]),
             T(f'<p>{didascalia}</p>', style=stile_didascalia, color=GRIGIO, css='tkl-didascalia'),
             boxed=False, css=css)


# misure dei file delle foto a tutta larghezza (assets/web)
DIM = {'punzonatura-1330.jpg': (1330, 376), 'punzonatura-m-514.jpg': (514, 385), 'officina-1330.jpg': (1330, 633),
       'officina-m-861.jpg': (861, 646), 'piega-1330.jpg': (1330, 605), 'piega-v-516.jpg': (516, 645)}


def lavorazioni():
    num = '<span class="num">{}</span>'
    capo = C(
        H('Dal foglio al pezzo finito', level='h2', style='h2', color=INCHIOSTRO, css='tkl-titolo'),
        T('<p>Gli stessi sei pezzi del foglio, con le macchine che li fanno e le misure che contano quando ci mandi un disegno. '
          'Verniciatura e trattamenti passano da impianti esterni collegati, e li seguiamo noi.</p>',
          style='body', color=TESTO2, css='tkl-intro'),
        boxed=False, css='tkl-griglia tkl-capo')
    spessori = C(RAW(leggi('spessori.html') + '<script>' + leggi('spessori.js') + '</script>'), boxed=False, css='tkl-d-sp')
    prima = C(
        riga(1, 'Taglio laser', [('Bystronic Byspeed 4400&nbsp;W, carico e scarico automatico, dispositivo antigraffio',
                                  num.format('3000&nbsp;×&nbsp;1500') + '&nbsp;mm')], extra=spessori),
        riga(2, 'Punzonatura e cesoiatura',
             [('Finn-Power SG6, punzonatrice con cesoia angolare: il pezzo esce separato e impilato',
               num.format('3000&nbsp;×&nbsp;1500') + '&nbsp;mm'),
              ('Cesoia Gasparini per il taglio della lamiera', 'fino a ' + num.format('3000') + '&nbsp;mm')]),
        boxed=False, css='tkl-distinta')
    sg6 = foto_larga('punzonatura-1330.jpg', 'punzonatura-m-514.jpg',
                     "La lamiera punzonata esce sul banco della Finn-Power SG6, nell'officina Tek.Lam",
                     'La SG6 in officina, a Tombelle.', 'tkl-striscia')
    seconda = C(
        riga(3, 'Piegatura', [('Piegatrice Finn-Power a 8 assi, bombatura Wila', num.format('3100') + '&nbsp;mm'),
                              ('Piegatrice Warcom a CN, bombatura idraulica', num.format('3100') + '&nbsp;mm')]),
        riga(4, 'Saldatura e assemblaggio', [('A filo continuo, a elettrodo e TIG', 'ferro, inox, alluminio'),
                                             ('Assemblaggio di particolari su disegno, carpenterie medie e leggere', '')]),
        riga(5, 'Tubi e profili',
             [('Curvatubi Pedrazzoli idraulica', 'tondo ' + num.format('Ø&nbsp;32&nbsp;×&nbsp;2,2') + ', quadro '
               + num.format('20&nbsp;×&nbsp;20&nbsp;×&nbsp;3')),
              ('Calandra a rulli Ercolina a CN, tubolari di piccole sezioni', ''),
              ('Troncatrice automatica OMES', 'fino a ' + num.format('120') + '&nbsp;mm, barre da ' + num.format('2000') + '&nbsp;mm')]),
        riga(6, 'Progettazione 3D', testo='Studio del prodotto e sviluppo dei pezzi nel nostro ufficio tecnico, con rendering e '
             'prototipazione grafica prima di tagliare un foglio. «Il nostro punto di forza è il servizio di progettazione.»'),
        riga(0, 'Verniciatura e consegna', testo='Verniciatura a polveri epossidiche o a liquido, cromatura, sabbiatura e zincatura '
             'su impianti esterni collegati, coordinati da noi. Consegna con un autocarro centinato da 50&nbsp;quintali di portata '
             'utile e un autocarro con gru.', chiudi=True),
        boxed=False, css='tkl-distinta tkl-distinta-2')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-lavorazioni') + CSS_CARTA + CSS_LAVORAZIONI)
    return C(stile, C(capo, prima, boxed=False, css='tkl-wrap'), sg6, C(seconda, boxed=False, css='tkl-wrap'),
             boxed=False, pad=0, tag='section', anchor='lavorazioni', bg=CARTA, css='tkl-lavorazioni tkl-carta tkl-sito')


# --- 4. Dal ferro battuto alla lamiera: la saldatura TIG a tutta larghezza, il racconto sotto
CSS_STORIA = (
    contenitore('.tkl-storia') +
    # nella statica 96 px di margine sopra, sulla carta: qui è spazio interno, così resta carta
    '.tkl-storia{padding:96px 0 128px!important;display:block!important}'
    '.tkl-storia .tkl-doc{display:block!important;padding:0!important;margin:0!important}'
    '.tkl-storia .tkl-doc .tkl-didascalia{padding:12px var(--m) 0!important;max-width:1440px!important;margin:0 auto!important}'
    '.tkl-storia .tkl-doc .tkl-didascalia,.tkl-storia .tkl-doc .tkl-didascalia p{font-size:15px!important;line-height:1.45!important}'
    '.tkl-storia .tkl-griglia{margin-top:80px!important}'
    '.tkl-storia .tkl-racconto{grid-column:1/7;margin-top:40px!important;max-width:31em!important}'
    '.tkl-storia .tkl-racconto,.tkl-storia .tkl-racconto p{font:400 20px/1.55 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-storia .tkl-racconto p+p{margin-top:18px!important;font-size:18px!important;color:#3d3832!important}'
    '.tkl-storia .tkl-persone{grid-column:8/13;margin-top:46px!important;align-self:start;padding-top:16px!important;'
    'border-top:1px solid var(--filo-chiaro)!important}'
    + interno('.tkl-storia .tkl-persone') + '{display:grid!important;grid-template-columns:1fr 1fr;column-gap:var(--g)}'
    '.tkl-storia .tkl-persone>.elementor-widget-container{display:contents!important}'
    '.tkl-storia .tkl-persone,.tkl-storia .tkl-persone p{font:400 17px/1.45 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-storia .tkl-persone b{display:block;font-weight:600;font-size:18px}'
    '.tkl-storia .tkl-persone span{display:block;color:var(--grigio)}'
    '@media (max-width:900px){.tkl-storia .tkl-racconto,.tkl-storia .tkl-persone{grid-column:1/13}'
    '.tkl-storia .tkl-persone{margin-top:40px!important}}'
    '@media (max-width:699px){.tkl-storia{padding:64px 0 80px!important}'
    '.tkl-storia .tkl-griglia{margin-top:48px!important}'
    '.tkl-storia .tkl-racconto,.tkl-storia .tkl-racconto p{font-size:18px!important}'
    '.tkl-storia .tkl-racconto{margin-top:28px!important}'
    '.tkl-storia .tkl-racconto p+p{font-size:17px!important}'
    + interno('.tkl-storia .tkl-persone') + '{grid-template-columns:1fr;row-gap:14px}'
    '.tkl-storia .tkl-persone>.elementor-widget-container{display:contents!important}'
    '.tkl-storia .tkl-doc .tkl-didascalia,.tkl-storia .tkl-doc .tkl-didascalia p{text-align:left;font-size:15px!important}}'
)


def storia():
    doc = foto_larga('officina-1330.jpg', 'officina-m-861.jpg', 'Saldatura TIG su un cassone inox ancora coperto dal film protettivo stampato',
                     'In officina a Tombelle: saldatura TIG su un cassone inox, con il film protettivo ancora addosso.', 'tkl-doc',
                     stile_didascalia='didascalia2')
    racconto = T(ap('<p>Tek.Lam nasce come carpenteria di piccoli manufatti in ferro battuto, nella zona artigianale di Tombelle. '
                    'Nel 2020 la «storica» FDS Volpato S.n.c. passa il testimone a Tek.Lam S.r.l.: l\'esperienza dei fondatori, '
                    'dal 1978, continua nella lavorazione della lamiera per conto terzi.</p>'
                    '<p>Il principio è rimasto quello: seguire il cliente dall\'idea alla realizzazione finale, con l\'ufficio '
                    'tecnico in casa.</p>'), style='racconto', color=INCHIOSTRO, css='tkl-racconto')
    persone = T('<p><b>Sandro Volpato</b><span>Responsabile ufficio tecnico</span><a href="mailto:sandro@teklam.it">sandro@teklam.it</a></p>'
                '<p><b>Dimitri Volpato</b><span>Responsabile commerciale</span><a href="mailto:dimitri@teklam.it">dimitri@teklam.it</a></p>',
                style='persone', color=INCHIOSTRO, link_color=INCHIOSTRO, link_hover=INCHIOSTRO, css='tkl-persone')
    griglia = C(H('Dal ferro battuto alla lamiera', level='h2', style='h2', color=INCHIOSTRO, css='tkl-titolo'), racconto, persone,
                boxed=False, css='tkl-wrap tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-storia') + CSS_CARTA + CSS_STORIA)
    return C(stile, doc, griglia, boxed=False, pad=0, tag='section', anchor='storia', bg=CARTA, css='tkl-storia tkl-carta tkl-sito')


# --- 5. La piegatrice a tutta larghezza, sul nero
CSS_FASCIA = (
    contenitore('.tkl-fascia') +
    '.tkl-fascia{display:block!important;background:var(--nero)!important}'
    '.tkl-fascia .tkl-didascalia{padding:10px var(--m) 14px!important;text-align:right}'
    '.tkl-fascia .tkl-didascalia,.tkl-fascia .tkl-didascalia p{font:400 14px/1.4 var(--f)!important;color:var(--grigio-scuro)!important;text-align:right}'
    '@media (max-width:699px){.tkl-fascia .tkl-didascalia,.tkl-fascia .tkl-didascalia p{text-align:left!important;font-size:13px!important}}'
)


def fascia():
    f = foto_larga('piega-1330.jpg', 'piega-v-516.jpg', "Una mano porta la lamiera sotto gli utensili della piegatrice, nell'officina Tek.Lam",
                   'In piegatura, a Tombelle.', 'tkl-fascia-foto')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-fascia') + CSS_FASCIA)
    return C(stile, f, boxed=False, pad=0, tag='section', bg=NERO, css='tkl-fascia tkl-sito')


# --- 6. Per chi lavoriamo: una frase sola con le note numerate
CSS_SETTORI = (
    contenitore('.tkl-settori') +
    '.tkl-settori{padding:112px 0 140px!important;display:block!important}'
    '.tkl-settori .tkl-elenco{grid-column:1/13}'
    '.tkl-settori .tkl-elenco,.tkl-settori .tkl-elenco p{font:300 clamp(34px,5.4vw,78px)/1.06 var(--disp)!important;'
    'letter-spacing:-.008em!important;color:var(--inchiostro)!important}'
    '.tkl-settori .tkl-elenco p{text-wrap:pretty!important}'
    '.tkl-settori .tkl-elenco sup{font:500 max(.26em,13px)/1 var(--f);vertical-align:top;position:relative;top:.42em;margin-left:.08em;'
    'color:var(--bronzo);font-variant-numeric:tabular-nums}'
    '.tkl-settori .tkl-note{grid-column:1/13;margin-top:64px!important}'
    '.tkl-settori .tkl-note ol{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:var(--g);row-gap:22px;margin:0!important;'
    'padding:0!important;list-style:none!important}'
    '.tkl-settori .tkl-note li{display:flex;gap:12px;margin:0!important;padding:0!important;border:0!important;'
    'font:400 16px/1.5 var(--f)!important;color:var(--grigio)!important}'
    '.tkl-settori .tkl-note li b{color:var(--bronzo);font-weight:600;font-variant-numeric:tabular-nums;min-width:12px}'
    '@media (max-width:900px){.tkl-settori .tkl-note ol{grid-template-columns:repeat(2,minmax(0,1fr))}}'
    '@media (max-width:699px){.tkl-settori{padding:72px 0 88px!important}'
    '.tkl-settori .tkl-elenco,.tkl-settori .tkl-elenco p{font-size:34px!important;line-height:1.1!important}'
    '.tkl-settori .tkl-note ol{grid-template-columns:1fr}.tkl-settori .tkl-note{margin-top:40px!important}}'
)


def settori():
    elenco = T(ap("<p>Elettromedicale ed elettronica<sup>1</sup>, arredo medicale e odontoiatrico<sup>2</sup>, refrigerazione "
                  "commerciale<sup>3</sup>, trattamento dell'aria e dei fluidi<sup>4</sup>, macchine agricole e movimento "
                  "terra<sup>5</sup>, carpenteria leggera per la meccanica<sup>6</sup></p>"),
               style='elenco', color=INCHIOSTRO, css='tkl-elenco')
    note = [
        "Case metallici per apparecchi elettromedicali e per l'industria elettronica.",
        'Semilavorati in lamiera per gli arredi degli studi medici e dentistici.',
        'Telai in tubolare quadro e tondo, tagliati, calandrati e piegati, per i banchi frigo.',
        'Semilavorati con coibentazione, guarnizioni e chiusure, pronti per il montaggio.',
        'Particolari complessi in lamiera per macchine agricole e movimento terra.',
        'Carpenteria leggera per qualsiasi settore della meccanica.',
    ]
    lista = T(ap('<ol>' + ''.join(f'<li><b>{i}</b>{t}</li>' for i, t in enumerate(note, 1)) + '</ol>'),
              style='note', color=GRIGIO, css='tkl-note')
    griglia = C(H('Per chi lavoriamo', level='h2', style='h2', color=INCHIOSTRO, css='tkl-vh'), elenco, lista,
                boxed=False, css='tkl-wrap tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-settori') + CSS_CARTA + CSS_SETTORI)
    return C(stile, griglia, boxed=False, pad=0, tag='section', anchor='settori', bg=CARTA, css='tkl-settori tkl-carta tkl-sito')


# --- 7. Contatti: sul grafite, con la loro sede
CSS_CONTATTI = (
    contenitore('.tkl-contatti') +
    '.tkl-contatti{padding:120px 0 104px!important;background:var(--grafite)!important;color:var(--bianco);display:block!important}'
    '.tkl-contatti .tkl-griglia{row-gap:36px!important;grid-template-rows:auto 1fr auto}'
    '.tkl-contatti .tkl-telefono{grid-row:1;grid-column:1/9;width:max-content!important;max-width:100%!important}'
    + ht('.tkl-contatti .tkl-telefono') + '{font:200 clamp(56px,8.4vw,120px)/.9 var(--f)!important;letter-spacing:-.035em!important;'
    'font-variant-numeric:tabular-nums lining-nums!important;color:var(--bianco)!important;text-transform:none!important}'
    '.tkl-contatti .tkl-telefono a{display:block;color:inherit!important;text-decoration:none!important;transition:color .15s}'
    '.tkl-contatti .tkl-telefono a:hover{color:var(--paglia)!important}'
    '.tkl-contatti .tkl-invito{grid-row:2;align-self:start;grid-column:1/8;max-width:30em!important}'
    '.tkl-contatti .tkl-invito,.tkl-contatti .tkl-invito p{font:400 22px/1.42 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-contatti .tkl-invito a{color:var(--paglia)!important;font-weight:600}'
    '.tkl-contatti .tkl-invito a:hover{color:var(--bianco)!important}'
    '.tkl-contatti .tkl-sede{grid-column:9/13;grid-row:1/3;margin:0!important;align-self:start;display:block!important;padding:0!important}'
    '.tkl-contatti .tkl-sede img{width:100%!important;aspect-ratio:470/360;object-fit:cover;height:auto!important}'
    '.tkl-contatti .tkl-sede .tkl-didascalia{margin-top:10px!important}'
    '.tkl-contatti .tkl-sede .tkl-didascalia,.tkl-contatti .tkl-sede .tkl-didascalia p{font:400 14px/1.4 var(--f)!important;'
    'color:var(--grigio-scuro)!important}'
    '.tkl-contatti .tkl-recapiti{grid-row:3;grid-column:1/13;display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));'
    'column-gap:var(--g)!important;row-gap:32px!important;margin-top:20px!important;padding:28px 0 0!important;border-top:1px solid var(--filo)!important}'
    + FIGLI.format(s='.tkl-contatti .tkl-recapiti') +
    '.tkl-recapiti .tkl-recapito{display:block!important;padding:0!important}'
    + ht('.tkl-recapiti .tkl-recapito h3') + ',' + ht('.tkl-recapiti .tkl-r-titolo') +
    '{font:600 15px/1.3 var(--f)!important;color:var(--grigio-scuro)!important;text-transform:none!important;letter-spacing:0!important}'
    '.tkl-recapiti .tkl-r-titolo{margin-bottom:8px!important}'
    '.tkl-recapiti .tkl-r-testo,.tkl-recapiti .tkl-r-testo p{font:400 17px/1.5 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-recapiti .tkl-r-testo span{color:#c9c1b5}'
    '.tkl-recapiti .tkl-r-testo a{overflow-wrap:anywhere;color:var(--bianco)!important}'
    '.tkl-recapiti .tkl-r-testo a:hover{color:var(--paglia)!important}'
    '@media (max-width:900px){'
    '.tkl-contatti .tkl-telefono,.tkl-contatti .tkl-invito{grid-column:1/13}'
    '.tkl-contatti .tkl-sede{grid-column:1/8}'
    '.tkl-contatti .tkl-griglia{grid-template-rows:none}'
    '.tkl-contatti .tkl-telefono,.tkl-contatti .tkl-invito,.tkl-contatti .tkl-sede,.tkl-contatti .tkl-recapiti{grid-row:auto}'
    '.tkl-contatti .tkl-recapiti{grid-template-columns:repeat(2,minmax(0,1fr))}}'
    '@media (max-width:699px){.tkl-contatti{padding:80px 0 72px!important}'
    + ht('.tkl-contatti .tkl-telefono') + '{font-size:12.4vw!important}'
    '.tkl-contatti .tkl-invito,.tkl-contatti .tkl-invito p{font-size:19px!important}'
    '.tkl-contatti .tkl-sede{grid-column:1/13}'
    '.tkl-contatti .tkl-recapiti{grid-template-columns:1fr}'
    '.tkl-recapiti .tkl-r-testo,.tkl-recapiti .tkl-r-testo p{font-size:16px!important}}'
)


def contatti():
    def recapito(titolo, testo):
        return C(H(titolo, level='h3', style='h3', color=GRIGIO_SCURO, css='tkl-r-titolo'),
                 T(ap(f'<p>{testo}</p>'), style='recapiti', color=BIANCO, link_color=BIANCO, link_hover=BIANCO, sottolinea=True,
                   css='tkl-r-testo'),
                 boxed=False, css='tkl-recapito')
    sede = C(I(img('sede-470.jpg'), alt="La palazzina della sede Tek.Lam con l'acero rosso davanti"),
             T('<p>La sede, in via del Lavoro 68.</p>', style='didascalia', color=GRIGIO_SCURO, css='tkl-didascalia'),
             boxed=False, css='tkl-sede')
    recapiti = C(
        recapito('Ufficio tecnico', f'Sandro Volpato<br><a href="mailto:{UFFTEC}">{UFFTEC}</a>'),
        recapito('Telefono e fax', f'<a href="{TEL_LINK}">+39&nbsp;049&nbsp;980&nbsp;14&nbsp;86</a><br>'
                 '<span>Fax <span class="num">+39&nbsp;049&nbsp;982&nbsp;90&nbsp;91</span></span>'),
        recapito('Commerciale e informazioni', 'Dimitri Volpato<br><a href="mailto:commerciale@teklam.it">commerciale@teklam.it</a><br>'
                 '<a href="mailto:info@teklam.it">info@teklam.it</a>'),
        recapito('Dove', "Via del Lavoro 68, zona artigianale Tombelle<br>30030 Vigonovo (VE)<br><span>Vicino al casello Padova "
                 "Interporto dell'A13.</span> <a href=\"https://www.google.com/maps/search/?api=1&amp;query=Via+del+Lavoro+68+Vigonovo+VE\">"
                 'Apri la mappa</a>'),
        boxed=False, css='tkl-recapiti')
    griglia = C(
        H('Contatti', level='h2', style='h2', color=BIANCO, css='tkl-vh'),
        H(TEL, level='div', style='telefono', color=BIANCO, link=TEL_LINK, css='tkl-telefono'),
        T(f'<p>Per un preventivo mandaci il disegno o il file 3D: <a href="mailto:{UFFTEC}">{UFFTEC}</a></p>', style='invito',
          color=BIANCO, link_color=PAGLIA, link_hover=PAGLIA, css='tkl-invito'),
        sede, recapiti, boxed=False, css='tkl-wrap tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-contatti') + CSS_CONTATTI)
    return C(stile, griglia, boxed=False, pad=0, tag='section', anchor='contatti', bg=GRAFITE, css='tkl-contatti tkl-sito')


def home():
    return [('apertura', apertura()), ('frase', frase()), ('lavorazioni', lavorazioni()), ('storia', storia()),
            ('fascia', fascia()), ('settori', settori()), ('contatti', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Tek.Lam, lavorazione lamiera conto terzi a Vigonovo',
     'descrizione': "Taglio laser, punzonatura, piegatura, saldatura, tubi e profili, progettazione 3D per conto terzi. "
                    "Tek.Lam S.r.l., Tombelle di Vigonovo (VE), l'esperienza dei fondatori dal 1978."},
]
