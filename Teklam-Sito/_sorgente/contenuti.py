# -*- coding: utf-8 -*-
"""
Contenuti della home di Tek.Lam per WordPress + Elementor: la home statica approvata ("Scintilla e spessore",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: testata (segno e scritta del marchio, menu di Ultimate Addons,
  telefono), titolo e anno dell'apertura con la foto, i testi della sezione dello spessore, la fascia della
  piegatrice, i sette passi del percorso, settori e note, famiglia con la foto della saldatura e le persone,
  telefono, invito e recapiti dei contatti, piede.
- Widget HTML (nodo RAW del motore) solo per le parti che Elementor gratuito non fa: l'interruttore Ferro, Inox,
  Alluminio e la sezione della lamiera in millimetri veri (lettura, legenda, scala, guide, tratteggio), con lo
  script della pagina statica; il fondo decorativo dei contatti (un <picture> senza testo alternativo, come nella
  statica).
- L'impaginazione (griglia a 12 colonne, misure fluide con clamp, punti di rottura 1180, 1100, 820 e 640 px della
  statica) è il foglio di stile della pagina statica, con le classi tkl-, dentro i nodi RAW: vale uguale per il
  template Elementor e per il fallback HTML.

Testi e dati: tutti dalla home statica (verificati in 01-analisi.md). Nessun dato nuovo.
La versione per la home precedente ("Il foglio annidato", bocciata) è in _prova/wp-vecchio-foglio/.
"""
import motore as m
from motore import C, H, T, I, RAW, MENU

PREFISSO = 'tkl'
NOME_SITO = 'Tek.Lam'

# ---------------------------------------------------------------------------------------------
# Tema: i colori e il carattere della home statica
# ---------------------------------------------------------------------------------------------
NERO = '#050403'           # il nero della foto d'apertura
FUMO = '#1b1916'
BIANCO = '#f4f1ea'         # luce della scintilla, non bianco puro
GRIGIO_SCURO = '#a59e93'   # testo secondario sul nero
CHIARO = '#efece6'         # lamiera zincata appena passata
INCHIOSTRO = '#16130f'
GRIGIO = '#625b52'         # testo secondario sul chiaro
BRONZO = '#8a5a1c'         # la paglia scurita per il fondo chiaro
PAGLIA = '#e2b46c'         # prima tinta di rinvenimento: solo dati e il gesto
FILO = 'rgba(244,241,234,.22)'
FILO_CHIARO = 'rgba(22,19,15,.18)'

TESTO = 'Sofia Sans'       # una famiglia sola: 200 titoli e numeri grandi, 400 testo, 600 macchine e intestazioni
# Sono gli stessi file woff2 della pagina statica (stesso md5 dei file latin di Google Fonts): da Google con l'API css2,
# oppure dal sito stesso con build.py --caratteri-locali (vedi caratteri_html).
GOOGLE_FONTS = 'https://fonts.googleapis.com/css2?family=Sofia+Sans:wght@1..1000&display=swap'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# misure (1440, 1024, 390): quelle della pagina statica a quelle larghezze. Le misure fluide (clamp, vw) e i punti di
# rottura della statica sono nel foglio di stile e prevalgono sui valori del pannello di Elementor.
TEMA = {
    'nome': 'Scintilla e spessore',
    'fondo': NERO, 'superficie': CHIARO, 'inchiostro': INCHIOSTRO, 'testo2': GRIGIO, 'accento': BRONZO,
    'filetto': FILO_CHIARO, 'filetto_scuro': FILO, 'su_scuro2': GRIGIO_SCURO,
    'scuro': NERO, 'su_scuro': BIANCO, 'su_accento': NERO,
    'font_titoli': TESTO, 'font_testo': TESTO, 'larghezza': 1440,
    'google_fonts': GOOGLE_FONTS,
    'stili': {
        'nav':      _st(TESTO, '400', (16, 16, 16), 1.55),
        'tel':      _st(TESTO, '400', (16, 16, 15), 1.55),
        'h1':       _st(TESTO, '200', (168.5, 119.8, 67.9), 0.88, -5.9),
        'anno':     _st(TESTO, '200', (168.5, 119.8, 67.9), 0.88, -6.7),
        'sotto':    _st(TESTO, '400', (21, 21, 18), 1.42),
        'piccolo':  _st(TESTO, '400', (15, 15, 15), 1.55),
        'h2':       _st(TESTO, '200', (72, 51.2, 40), 0.96, -2.2),
        'h2sp':     _st(TESTO, '200', (77.8, 55.3, 42), 0.96, -2.3),
        'body':     _st(TESTO, '400', (18, 18, 17), 1.55),
        'n':        _st(TESTO, '200', (60, 44, 30), 1.0, -1.8),
        'passo':    _st(TESTO, '400', (21, 21, 20), 1.2, -0.21),
        'mac':      _st(TESTO, '600', (15, 15, 15), 1.4),
        'mis':      _st(TESTO, '400', (15, 15, 15), 1.4),
        'h2p':      _st(TESTO, '600', (17, 17, 17), 1.55),
        'elenco':   _st(TESTO, '200', (63.4, 45, 32), 1.08, -1.6),
        'note':     _st(TESTO, '400', (15, 15, 15), 1.42),
        'storia':   _st(TESTO, '400', (20, 20, 18), 1.5),
        'didascalia': _st(TESTO, '400', (14, 14, 14), 1.45),
        'persone':  _st(TESTO, '400', (15, 15, 15), 1.45),
        'telefono': _st(TESTO, '200', (158.4, 112.6, 56), 0.9, -6.3),
        'invito':   _st(TESTO, '400', (21, 21, 19), 1.42),
        'recapiti': _st(TESTO, '400', (16, 16, 15), 1.5),
        'piede':    _st(TESTO, '400', (14, 14, 14), 1.55),
        'btn':      _st(TESTO, '400', (17, 17, 17), 1.2),
    },
    'spazi': {'sezione': (148, 102, 88), 'lato': (64, 46, 20), 'm': (24, 17, 16), 's': (12, 12, 12), '0': (0, 0, 0)},
    'bottoni': {},
    'bottone': {'raggio': 0, 'pad': (0, 0, 0, 0), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# Le immagini dei widget HTML (il fondo dei contatti) restano a questo indirizzo: per non dipendere da GitHub
# si carica assets/web/ sul sito e si rigenera con build.py --base.
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
    # le stesse @font-face della pagina statica
    latin = ('U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,'
             'U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD')
    ext = ('U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,U+20A0-20AB,U+20AD-20C0,U+2113,'
           'U+2C60-2C7F,U+A720-A7FF')
    return ('<style>'
            f'@font-face{{font-family:"Sofia Sans";src:url({img("fonts/sofia-latin.woff2")}) format("woff2");'
            f'font-weight:1 1000;font-display:swap;unicode-range:{latin}}}'
            f'@font-face{{font-family:"Sofia Sans";src:url({img("fonts/sofia-latin-ext.woff2")}) format("woff2");'
            f'font-weight:1 1000;font-display:swap;unicode-range:{ext}}}'
            '</style>')


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (come nella home statica; le cose da confermare sono nel LEGGIMI)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}980{NBSP}14{NBSP}86'
TEL_LINK = 'tel:+390499801486'

# voci del menu: in WordPress è il menu "Menu Tek.Lam" (link personalizzati verso le ancore della home)
VOCI_MENU = [('Lavorazioni', '/#percorso'), ('Settori', '/#settori'), ('Famiglia Volpato', '/#famiglia'), ('Contatti', '/#contatti')]


# Nei widget Testo il colore al passaggio del mouse (link_hover) è uguale a quello del link: Elementor lo usa anche
# per il fuoco, la statica no. Il colore al passaggio del mouse sta nei fogli di stile, con :hover.


def ap(html):
    """Apostrofo diritto come nella statica: WordPress (wptexturize) lo farebbe tipografico nei widget Testo."""
    return html.replace("'", '&#39;')


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def senza_scatola(sel):
    """Un contenitore con dentro un widget HTML che non fa scatola (display:contents): il markup della statica
    sta direttamente nella griglia o nella sezione, come nella pagina statica."""
    return (f'{sel},{sel}>.elementor-widget-html,{sel}>.elementor-widget-html>.elementor-widget-container,'
            f'{sel}>.tkl-w{{display:contents!important}}')


# ---------------------------------------------------------------------------------------------
# Foglio di stile comune: variabili della pagina statica e regole di base.
# Ogni sezione lo porta con sé (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
CSS_VARIABILI = (
    ':root{--nero:#050403;--fumo:#1b1916;--bianco:#f4f1ea;--grigio-scuro:#a59e93;--chiaro:#efece6;--inchiostro:#16130f;'
    '--grigio:#625b52;--bronzo:#8a5a1c;--paglia:#e2b46c;--filo:rgba(244,241,234,.22);--filo-chiaro:rgba(22,19,15,.18);'
    '--m:clamp(20px,4.45vw,64px);--gap:clamp(16px,1.67vw,24px);--f:"Sofia Sans",system-ui,sans-serif}'
    # Elementor rende morbido lo scorrimento verso le ancore; la statica no
    'html{-webkit-text-size-adjust:100%;scroll-behavior:auto}'
)

# regole che valgono per tutto il sito: stanno nella testata (Elementor) e nella testata del fallback
CSS_SITO = (
    'body{margin:0;background:var(--nero)!important;color:var(--bianco);font-family:var(--f);font-weight:400;font-size:18px;'
    'line-height:1.55;font-kerning:normal;font-synthesis:none;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}'
    '@media (max-width:640px){body{font-size:17px}}'
    '.tkl-sito,.tkl-sito *,.tkl-sito *::before,.tkl-sito *::after{box-sizing:border-box}'
    '.tkl-sito .num{font-variant-numeric:tabular-nums lining-nums}'
    '.tkl-sito .nb{white-space:nowrap}'
    '@media (prefers-reduced-motion:reduce){.tkl-sito .sezione,.tkl-sito .legenda li,.tkl-sito .scelta button{transition:none!important}}'
)


def css_testi(scope, chiaro=False):
    """Regole di base dei widget dentro una sezione, come le regole generali della statica: margini del tema e di
    Elementor azzerati, link del colore del testo (il tema Hello li colora di rosa), fuoco come nella statica."""
    s = f'.{scope}'
    hover = 'var(--bronzo)' if chiaro else 'var(--paglia)'
    return (
        f'{s}{{font-family:var(--f);font-size:18px;line-height:1.55;font-weight:400;font-synthesis:none;'
        '-webkit-font-smoothing:antialiased}'
        f'@media (max-width:640px){{{s}{{font-size:17px}}}}'
        f'{s} h1,{s} h2,{s} h3,{s} p,{s} ol,{s} ul,{s} dl,{s} dd,{s} figure,{s} .elementor-heading-title{{margin:0}}'
        f'{s} .elementor-widget-text-editor p,{s} :where(.tkl-w) p{{margin:0!important}}'
        f'{s} ol,{s} ul{{padding:0;list-style:none}}'
        # il fallback del motore bilancia titoli e paragrafi: la statica no (lo fa solo dove serve, più sotto)
        f'{s} h1,{s} h2,{s} h3,{s} p,{s} .elementor-heading-title{{text-wrap:wrap}}'
        f'{s} .elementor-widget:not(:last-child){{margin-block-end:0}}'
        f'{s} .elementor-widget{{margin:0}}'
        f'{s} a{{color:inherit;text-decoration:underline;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}}'
        f'{s} a:focus,{s} a:active{{color:inherit}}'
        f'{s} a:hover{{color:{hover}!important}}'
        # il reset del tema Hello aggiunge ai link a fuoco un anello: qui il fuoco della statica
        f'{s} :focus-visible{{outline:2px solid {hover};outline-offset:3px}}'
        f'{s} a:focus-visible,{s} button:focus-visible{{box-shadow:none}}'
        f'{s} img{{display:block;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}'
    )


def contenitore(scope):
    """Un contenitore di Elementor (o del fallback) che si comporta come un blocco della statica."""
    return f'{scope}{{width:100%!important;max-width:none!important;margin:0!important;padding:0!important;gap:0!important;min-height:0!important}}'


GRIGLIA = ('display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--gap)!important;row-gap:0!important;'
           'padding:0 var(--m)!important;width:100%!important;max-width:none!important;margin:0!important;min-height:0!important;')
# la riga di una griglia: i widget prendono la colonna dal foglio di stile, non dal contenitore flex di Elementor
FIGLI = '{s}>*{{width:auto!important;max-width:none!important;min-width:0}}'

CSS_COMUNE = (
    ':where(.tkl-sito) .tkl-griglia{' + GRIGLIA + '}'
    + FIGLI.format(s=':where(.tkl-sito .tkl-griglia)') +
    ht(':where(.tkl-sito) .tkl-titolo-sez') + '{font:200 clamp(40px,5vw,72px)/.96 var(--f)!important;letter-spacing:-.03em!important;'
    'text-wrap:balance!important;text-transform:none!important;color:inherit!important}'
    # una foto con il taglio verticale solo sul telefono (widget Immagine), come <picture> nella statica
    ':where(.tkl-sito) .tkl-stretto{display:none!important}'
    '@media (max-width:640px){:where(.tkl-sito) .tkl-largo{display:none!important}:where(.tkl-sito) .tkl-stretto{display:block!important}}'
    # il tema Hello scrive le didascalie in corsivo, grigie, a 16 px
    ':where(.tkl-sito) figcaption{font-style:normal;font-weight:400}'
)


# =============================================================================================
# TESTATA (template "Tek.Lam: Header", da mettere su tutto il sito con Ultimate Addons): sopra la foto d'apertura
# =============================================================================================
CSS_MARCHIO = (
    '.tkl-sito .tkl-marchio{display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;align-items:center!important;'
    'gap:14px!important;text-decoration:none!important;padding:0!important;width:auto!important;min-height:0!important;margin:0!important}'
    '.tkl-sito .tkl-marchio>*{width:auto!important;flex:0 0 auto!important;max-width:none!important;margin:0!important}'
    '.tkl-sito .tkl-marchio img{height:auto!important;max-width:none!important;display:block}'
    '.tkl-sito .tkl-segno img{width:46px!important}.tkl-sito .tkl-scritta img{width:124px!important}'
    '@media (max-width:640px){.tkl-sito .tkl-segno img{width:38px!important}.tkl-sito .tkl-scritta img{width:104px!important}}'
)

CSS_TESTATA = (
    '.tkl-testa{position:absolute!important;top:0;left:0;right:0;z-index:5;display:flex!important;flex-direction:row!important;'
    'flex-wrap:nowrap!important;align-items:center!important;gap:40px!important;padding:26px var(--m) 0!important;'
    'width:100%!important;max-width:none!important;margin:0!important;color:var(--bianco);background:none!important;min-height:0!important}'
    '.tkl-testa>*{flex:0 0 auto!important;width:auto!important;max-width:none!important}'
    '.tkl-testa>.tkl-fuori{position:absolute!important;left:0;top:0;width:0!important;height:0!important;padding:0!important;'
    'overflow:visible;margin:0!important}'
    + CSS_MARCHIO +
    # menu: Ultimate Addons (Elementor) e il menu del fallback, a vista uguali al menu della pagina statica
    '.tkl-testa .tkl-menu{margin-left:auto!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.tkl-menu .tkl-nav-l{display:flex;flex-wrap:nowrap;gap:32px!important}'
    '.tkl-menu .hfe-nav-menu>li.menu-item{margin:0!important}'
    # il clearfix di Ultimate Addons (::before e ::after) diventerebbe una voce vuota della riga, con il suo spazio
    '.tkl-menu .hfe-nav-menu::before,.tkl-menu .hfe-nav-menu::after{display:none!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item,.tkl-menu .tkl-nav-l a{display:block!important;'
    'padding:0!important;font:400 16px/1.55 var(--f)!important;letter-spacing:0!important;text-transform:none!important;'
    'color:var(--bianco)!important;text-decoration:none!important;white-space:nowrap;border:0!important;background:none!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item:hover,.tkl-menu .tkl-nav-l a:hover{color:var(--paglia)!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::before,.tkl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::after,'
    '.tkl-menu .hfe-pointer__underline a.hfe-menu-item::after{display:none!important}'
    '.tkl-menu .tkl-nav-l a[aria-current]{border:0!important;padding:0!important}'
    '.tkl-menu details,.tkl-menu .hfe-nav-menu__toggle{display:none!important}'
    # Ultimate Addons e il fallback passano al menu a scomparsa a 1024 px; la statica a 820 toglie il menu: fino a 821 resta in riga
    '@media (min-width:821px){'
    '.tkl-menu .hfe-nav-menu__layout-horizontal,.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu{visibility:visible!important;'
    'opacity:1!important;height:auto!important;position:static!important;display:flex!important;background:none!important;'
    'border:0!important;box-shadow:none!important;width:auto!important;left:auto!important;top:auto!important}'
    '.tkl-menu .hfe-nav-menu__layout-horizontal li.menu-item{width:auto!important;background:none!important;border:0!important}'
    '.tkl-menu .tkl-nav-l{display:flex!important}}'
    '.tkl-testa .tkl-tel p{margin:0!important}'
    '.tkl-testa .tkl-tel,.tkl-testa .tkl-tel p{font:400 16px/1.55 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-testa .tkl-tel a{color:var(--bianco)!important;text-decoration:none!important;font-variant-numeric:tabular-nums;white-space:nowrap}'
    '.tkl-testa .tkl-tel a:hover{color:var(--paglia)!important}'
    '@media (max-width:1100px){.tkl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.tkl-menu .tkl-nav-l{gap:22px!important}}'
    '@media (max-width:820px){.tkl-testa .tkl-menu{display:none!important}.tkl-testa .tkl-tel{margin-left:auto!important}}'
    '@media (max-width:640px){.tkl-testa{padding-top:18px!important}'
    '.tkl-testa .tkl-tel,.tkl-testa .tkl-tel p{font-size:15px!important}}'
)

CSS_TESTATA_ELEMENTOR = (
    # la testata sta sopra la foto d'apertura (posizione assoluta), come nella statica
    '#masthead{position:static}'
    '.hfe-skip-link{display:none!important}'
    '.tkl-menu .hfe-nav-menu li.current-menu-item>a.hfe-menu-item:not(:hover){color:var(--bianco)!important}'
)


def marchio():
    """Il segno e la scritta del marchio, ritagliati dal PNG del loro sito; il link porta all'inizio della home."""
    return C(I(img('logo-segno.png'), alt='Segno del marchio Tek.Lam', css='tkl-segno'),
             I(img('logo-scritta-chiara.png'), alt='Tek.Lam', css='tkl-scritta'),
             dir='row', align='center', gap=14, boxed=False, link='/', css='tkl-marchio')


def header():
    menu = MENU(VOCI_MENU, colore=BIANCO, colore_hover=PAGLIA, accento=PAGLIA, fondo_menu=NERO, linea=FILO,
                stile='nav', spazio=32, pad_h=0, pad_v=0, distanza=12, align_menu='right', slug='menu-tek-lam', css='tkl-menu')
    tel = T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='tel', color=BIANCO, link_color=BIANCO, link_hover=BIANCO,
            sottolinea=False, css='tkl-tel')
    globali = RAW('', css=CSS_VARIABILI + CSS_SITO + CSS_COMUNE + css_testi('tkl-testa') + CSS_TESTATA)
    # solo in Elementor: i caratteri (nel fallback il <link> lo scrive già il motore) e le regole di Ultimate Addons
    caratteri = RAW(caratteri_html(), css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    fuori = C(globali, caratteri, boxed=False, css='tkl-fuori')
    return C(fuori, marchio(), menu, tel, dir='row', align='center', gap=40, boxed=False, pad=0, tag='header',
             css='tkl-testa tkl-sito')


# =============================================================================================
# PIEDE (template "Tek.Lam: Footer")
# =============================================================================================
CSS_PIEDE = (
    contenitore('.tkl-piede') +
    '.tkl-piede{background:var(--nero)!important;color:var(--grigio-scuro);padding:40px 0 36px!important;font-size:14px;'
    'line-height:1.55;border-top:1px solid var(--filo)!important;display:block!important}'
    '.tkl-piede .tkl-griglia{row-gap:24px!important;align-items:start!important}'
    '.tkl-piede .tkl-marchio{grid-column:1/4}'
    '.tkl-piede .tkl-soc{grid-column:4/9}'
    '.tkl-piede .tkl-soc,.tkl-piede .tkl-soc p,.tkl-piede .tkl-link-piede,.tkl-piede .tkl-link-piede p{font:400 14px/1.55 var(--f)!important;'
    'color:var(--grigio-scuro)!important}'
    '.tkl-piede .tkl-soc b{color:var(--bianco);font-weight:600}'
    '.tkl-piede .tkl-link-piede{grid-column:9/13}'
    '.tkl-piede .tkl-link-piede p{display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:flex-end}'
    '.tkl-piede .tkl-link-piede a{text-decoration:none!important;color:inherit!important}'
    '.tkl-piede .tkl-link-piede a:hover{color:var(--bianco)!important;text-decoration:underline!important}'
    '@media (max-width:1100px){.tkl-piede .tkl-marchio{grid-column:1/13}.tkl-piede .tkl-soc{grid-column:1/8}'
    '.tkl-piede .tkl-link-piede{grid-column:8/13}}'
    '@media (max-width:640px){.tkl-piede .tkl-soc,.tkl-piede .tkl-link-piede{grid-column:1/13}'
    '.tkl-piede .tkl-link-piede p{justify-content:flex-start}}'
)


def footer():
    soc = T('<p><b>TEK.LAM S.R.L.</b>, carpenteria in lamiera<br>Via del Lavoro 68, 30030 Vigonovo (VE)<br>'
            'C.F. e P.IVA <span class="num">04595530272</span></p>', style='piede', color=GRIGIO_SCURO, css='tkl-soc')
    link = T('<p>'
             '<a href="https://www.facebook.com/Tek.lamsrl/">Facebook</a> '
             '<a href="https://www.instagram.com/teklam_srl/">Instagram</a> '
             '<a href="https://www.linkedin.com/company/tek-lam-srl/">LinkedIn</a> '
             '<a href="http://www.teklam.it/privacy-contatti/">Privacy</a> '
             '<a href="http://www.teklam.it/cookie/">Cookie</a></p>',
             style='piede', color=GRIGIO_SCURO, link_color=GRIGIO_SCURO, link_hover=GRIGIO_SCURO, sottolinea=False,
             css='tkl-link-piede')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + CSS_MARCHIO + css_testi('tkl-piede') + CSS_PIEDE)
    riga = C(marchio(), soc, link, boxed=False, css='tkl-griglia')
    return C(stile, riga, tag='footer', boxed=False, pad=0, bg=NERO, css='tkl-piede tkl-sito')


# =============================================================================================
# HOME
# =============================================================================================

# --- 1. Apertura: la foto del taglio laser, titolo e anno, la riga sotto
CSS_APERTURA = (
    contenitore('.tkl-apertura') +
    '.tkl-apertura{position:relative!important;min-height:max(100svh,720px)!important;display:flex!important;flex-direction:column!important;'
    'justify-content:flex-end!important;overflow:hidden!important;background:var(--nero)!important;flex-wrap:nowrap!important}'
    # la foto: due widget Immagine (largo e, solo sul telefono, verticale) in un contenitore steso sulla sezione
    '.tkl-apertura .tkl-ap-foto{position:absolute!important;inset:-13% 0 0 0;width:auto!important;height:auto!important;display:block!important;'
    'padding:0!important;margin:0!important;min-height:0!important}'
    '.tkl-ap-foto>*,.tkl-ap-foto>*>.elementor-widget-container{height:100%!important;width:100%!important}'
    '.tkl-ap-foto img{width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;object-position:50% 0}'
    '.tkl-apertura .tkl-griglia{position:relative;padding-bottom:clamp(28px,4vh,48px)!important;row-gap:28px!important;align-items:end!important}'
    '.tkl-apertura .tkl-titolo{grid-column:1/9;margin-left:-.05em!important}'
    + ht('.tkl-apertura .tkl-titolo') + '{font:200 clamp(64px,11.7vw,170px)/.88 var(--f)!important;letter-spacing:-.035em!important;'
    'color:var(--bianco)!important;text-transform:none!important}'
    '.tkl-apertura .tkl-anno{grid-column:9/13;justify-self:end}'
    '.tkl-apertura .tkl-anno,.tkl-apertura .tkl-anno p{text-align:right;font:200 clamp(64px,11.7vw,170px)/.88 var(--f)!important;'
    'letter-spacing:-.04em!important;font-variant-numeric:lining-nums!important;color:var(--bianco)!important}'
    '.tkl-apertura .tkl-anno small{display:block;font-size:16px;line-height:1.3;letter-spacing:0;font-weight:400;color:var(--grigio-scuro);'
    'margin-top:18px;font-variant-numeric:normal}'
    '.tkl-apertura .tkl-riga-sotto{grid-column:1/13;display:grid!important;grid-template-columns:subgrid;align-items:end!important;'
    'padding:24px 0 0!important;border-top:1px solid var(--filo)!important;margin:0!important;gap:0!important;column-gap:var(--gap)!important;'
    'width:auto!important;max-width:none!important;min-height:0!important}'
    + FIGLI.format(s='.tkl-apertura .tkl-riga-sotto') +
    '.tkl-apertura .tkl-sotto{grid-column:1/7;max-width:31em!important}'
    '.tkl-apertura .tkl-sotto,.tkl-apertura .tkl-sotto p{font:400 21px/1.42 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-apertura .tkl-ind{grid-column:7/13;justify-self:end}'
    '.tkl-apertura .tkl-ind,.tkl-apertura .tkl-ind p{font:400 15px/1.55 var(--f)!important;color:var(--grigio-scuro)!important}'
    '.tkl-apertura .tkl-ind p{display:flex;gap:28px;align-items:baseline}'
    '.tkl-apertura .tkl-ind a{color:var(--bianco)!important}'
    '.tkl-apertura .tkl-ind a:hover{color:var(--paglia)!important}'
    '@media (max-width:1100px){'
    '.tkl-apertura .tkl-titolo{grid-column:1/10}'
    '.tkl-apertura .tkl-anno{grid-column:10/13}'
    '.tkl-apertura .tkl-sotto{grid-column:1/8}'
    '.tkl-apertura .tkl-ind{grid-column:8/13}'
    '.tkl-apertura .tkl-ind p{flex-direction:column;gap:6px;align-items:flex-end}}'
    '@media (max-width:820px){'
    '.tkl-apertura .tkl-titolo{grid-column:1/13}'
    '.tkl-apertura .tkl-anno{grid-column:1/13;justify-self:start}'
    '.tkl-apertura .tkl-anno p{display:flex;align-items:baseline;gap:20px}'
    '.tkl-apertura .tkl-anno,.tkl-apertura .tkl-anno p{text-align:left}'
    '.tkl-apertura .tkl-anno small{margin-top:0}'
    '.tkl-apertura .tkl-riga-sotto{display:flex!important;flex-direction:column!important;align-items:flex-start!important;gap:14px!important}'
    '.tkl-apertura .tkl-ind{justify-self:start}'
    '.tkl-apertura .tkl-ind p{align-items:flex-start;flex-direction:row;flex-wrap:wrap;gap:6px 24px}}'
    '@media (max-width:640px){'
    '.tkl-apertura{min-height:0!important;display:block!important}'
    '.tkl-apertura .tkl-ap-foto{position:relative!important;inset:auto;height:min(64svh,560px)!important}'
    '.tkl-ap-foto img{object-position:50% 30%}'
    '.tkl-apertura .tkl-griglia{margin-top:-64px!important;row-gap:22px!important;padding-bottom:28px!important}'
    + ht('.tkl-apertura .tkl-titolo') + '{font-size:clamp(56px,17.4vw,76px)!important;line-height:.9!important;letter-spacing:-.04em!important}'
    '.tkl-apertura .tkl-anno,.tkl-apertura .tkl-anno p{font-size:clamp(56px,17.4vw,76px)!important}'
    '.tkl-apertura .tkl-anno small{font-size:14px}'
    '.tkl-apertura .tkl-sotto,.tkl-apertura .tkl-sotto p{font-size:18px!important}'
    '.tkl-apertura .tkl-riga-sotto{padding-top:18px!important}}'
)


def apertura():
    alt = 'Testa di taglio laser su una lamiera, con due ventagli di scintille.'
    foto = C(I(img('apertura-2400.jpg'), alt=alt, css='tkl-largo'), I(img('apertura-v-1280.jpg'), alt=alt, css='tkl-stretto'),
             boxed=False, css='tkl-ap-foto')
    riga = C(
        T('<p>Progettiamo, tagliamo, punzoniamo, pieghiamo e saldiamo lamiera sul disegno del cliente. Officina a Tombelle di '
          'Vigonovo, tra Padova e Venezia.</p>', style='sotto', color=BIANCO, css='tkl-sotto'),
        T('<p><span>Foto indicativa</span> <a href="#spessore">Fino a che spessore tagliamo</a></p>', style='piccolo',
          color=GRIGIO_SCURO, link_color=BIANCO, link_hover=BIANCO, sottolinea=True, css='tkl-ind'),
        boxed=False, css='tkl-riga-sotto')
    griglia = C(
        H('Lamiera<br>conto terzi', level='h1', style='h1', color=BIANCO, css='tkl-titolo'),
        T('<p>1978<small>la famiglia Volpato<br>in officina, da allora</small></p>', style='anno', color=BIANCO, css='tkl-anno'),
        riga, boxed=False, css='tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-apertura') + CSS_APERTURA)
    # i caratteri anche qui: se la testata globale manca, la home li carica comunque (solo Elementor)
    caratteri = RAW(caratteri_html(preconnect=False), solo_elementor=True)
    return C(stile, caratteri, foto, griglia, boxed=False, pad=0, tag='section', bg=NERO, css='tkl-apertura tkl-sito')


# --- 2. Lo spessore, a grandezza vera: il gesto (interruttore e sezione in millimetri veri, widget HTML)
CSS_SPESSORE = (
    contenitore('.tkl-spessore') +
    '.tkl-spessore{padding:clamp(88px,10vw,148px) 0 clamp(88px,10vw,140px)!important;background:var(--nero)!important;display:block!important}'
    '.tkl-spessore .tkl-griglia{row-gap:40px!important;align-items:start!important}'
    '.tkl-spessore .tkl-sp-testo{grid-column:1/6;display:block!important;padding:0!important;margin:0!important;min-height:0!important}'
    + ht('.tkl-spessore .tkl-sp-h2') + '{font:200 clamp(42px,5.4vw,78px)/.96 var(--f)!important;letter-spacing:-.03em!important;'
    'text-wrap:balance!important;color:var(--bianco)!important;text-transform:none!important}'
    '.tkl-spessore .tkl-sp-p{margin-top:28px!important;max-width:25em!important}'
    '.tkl-spessore .tkl-sp-p,.tkl-spessore .tkl-sp-p p{font:400 18px/1.55 var(--f)!important;color:var(--grigio-scuro)!important}'
    '.tkl-spessore .tkl-sp-p strong{color:var(--bianco);font-weight:500}'
    + senza_scatola('.tkl-spessore .tkl-scelta-box') + senza_scatola('.tkl-spessore .tkl-figura-box') +
    '.tkl-spessore .scelta{display:flex;margin-top:40px;border:1px solid var(--filo);width:max-content;max-width:100%}'
    '.tkl-spessore .scelta button,.tkl-spessore .scelta button:hover,.tkl-spessore .scelta button:focus{appearance:none;-webkit-appearance:none;'
    'font:inherit;font-size:17px;color:var(--bianco);background:transparent;border:0;border-radius:0;padding:14px 22px 15px;cursor:pointer;'
    'display:flex;gap:10px;align-items:baseline;min-height:48px;transition:background-color .15s,color .15s;text-transform:none;letter-spacing:0;'
    'box-shadow:none;margin:0;white-space:nowrap;width:auto;line-height:1.55;text-align:left;font-weight:400}'
    '.tkl-spessore .scelta button+button{border-left:1px solid var(--filo)}'
    '.tkl-spessore .scelta button span{font-variant-numeric:tabular-nums;color:var(--grigio-scuro);font-size:15px}'
    '.tkl-spessore .scelta button:hover{background:var(--fumo)}'
    '.tkl-spessore .scelta button[aria-checked="true"]{background:var(--paglia);color:var(--nero)}'
    '.tkl-spessore .scelta button[aria-checked="true"] span{color:var(--nero)}'
    '.tkl-spessore .scelta button:focus-visible{outline:2px solid var(--bianco);outline-offset:-4px;box-shadow:none}'
    '.tkl-spessore .sp-figura{grid-column:7/13;margin:0 calc(var(--m) * -1) 0 0;--t:20}'
    '.tkl-spessore .lettura{display:flex;align-items:baseline;gap:18px;padding-right:var(--m)}'
    '.tkl-spessore .lettura output{font-weight:200;font-size:clamp(120px,15vw,216px);line-height:.8;letter-spacing:-.05em;'
    'font-variant-numeric:tabular-nums lining-nums;color:var(--bianco)}'
    '.tkl-spessore .lettura .u{font-weight:200;font-size:clamp(36px,3.6vw,52px);letter-spacing:-.02em}'
    '.tkl-spessore .lettura .mat{margin-left:auto;font-size:16px;color:var(--grigio-scuro);text-align:right;line-height:1.35}'
    '.tkl-spessore .lettura .mat b{display:block;color:var(--bianco);font-weight:500}'
    '.tkl-spessore .tavola{position:relative;margin-top:64px;height:27mm;--l:150px}'
    '.tkl-spessore .legenda{position:absolute;left:0;bottom:0;width:calc(var(--l) - 24px);height:100%;margin:0;padding:0;list-style:none}'
    '.tkl-spessore .legenda li{position:absolute;right:0;transform:translateY(50%);font-size:14px;line-height:1;color:var(--grigio-scuro);'
    'white-space:nowrap;transition:color .15s;margin:0;padding:0;border:0}'
    '.tkl-spessore .legenda li b{font-weight:400;font-variant-numeric:tabular-nums;display:inline-block;min-width:1.4em;text-align:right;margin-left:6px}'
    '.tkl-spessore .legenda li.su{color:var(--bianco)}'
    '.tkl-spessore .legenda li.su b{font-weight:600;color:var(--paglia)}'
    '.tkl-spessore .scala{position:absolute;left:calc(var(--l) - 16px);bottom:0;width:12px;height:25mm;color:var(--grigio-scuro)}'
    '.tkl-spessore .scala::before{content:"";position:absolute;right:0;bottom:0;width:5px;height:100%;'
    'background:repeating-linear-gradient(to top,currentColor 0 1px,transparent 1px 1mm)}'
    '.tkl-spessore .scala::after{content:"";position:absolute;right:0;bottom:0;width:12px;height:100%;'
    'background:repeating-linear-gradient(to top,currentColor 0 1px,transparent 1px 5mm)}'
    '.tkl-spessore .sezione{position:absolute;left:var(--l);right:0;bottom:0;height:calc(var(--t) * 1mm);border:1.5px solid var(--bianco);'
    'border-right:0;background-color:#14120f;transition:height .22s cubic-bezier(.3,.7,.2,1)}'
    '.tkl-spessore .sp-figura[data-mat="ferro"] .sezione{background-image:repeating-linear-gradient(-45deg,var(--paglia) 0 1px,transparent 1px 1.6mm)}'
    '.tkl-spessore .sp-figura[data-mat="inox"] .sezione{background-image:repeating-linear-gradient(-45deg,var(--paglia) 0 1px,transparent 1px .7mm,'
    'var(--paglia) .7mm calc(.7mm + 1px),transparent calc(.7mm + 1px) 2.6mm)}'
    '.tkl-spessore .sp-figura[data-mat="alluminio"] .sezione{background-image:repeating-linear-gradient(-45deg,var(--paglia) 0 1px,transparent 1px 2.8mm),'
    'repeating-linear-gradient(45deg,rgba(226,180,108,.45) 0 1px,transparent 1px 2.8mm)}'
    '.tkl-spessore .guide{position:absolute;left:var(--l);right:0;bottom:0;height:100%;pointer-events:none}'
    '.tkl-spessore .guide i{position:absolute;left:0;right:0;height:0;border-top:1px dashed rgba(244,241,234,.34)}'
    '.tkl-spessore .guide i.su{border-color:transparent}'
    '.tkl-spessore .sp-figura figcaption{margin-top:22px;padding-left:150px;padding-right:var(--m);font-size:14px;line-height:1.45;'
    'color:var(--grigio-scuro);max-width:46em}'
    '.tkl-spessore .sp-figura figcaption b{color:var(--bianco);font-weight:600}'
    '@media (max-width:1100px){'
    '.tkl-spessore .tkl-sp-testo{grid-column:1/13;display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--gap)}'
    + FIGLI.format(s='.tkl-spessore .tkl-sp-testo') +
    '.tkl-spessore .tkl-sp-h2,.tkl-spessore .tkl-sp-p{grid-column:1/9}'
    '.tkl-spessore .scelta{grid-column:1/13}'
    '.tkl-spessore .sp-figura{grid-column:1/13}}'
    '@media (max-width:640px){'
    '.tkl-spessore .tkl-sp-h2,.tkl-spessore .tkl-sp-p{grid-column:1/13}'
    '.tkl-spessore .tkl-sp-p,.tkl-spessore .tkl-sp-p p{font-size:17px!important}'
    '.tkl-spessore .scelta{width:100%}'
    '.tkl-spessore .scelta button,.tkl-spessore .scelta button:hover,.tkl-spessore .scelta button:focus{flex:1;flex-direction:column;gap:2px;'
    'align-items:flex-start;padding:12px 14px}'
    '.tkl-spessore .lettura{flex-wrap:wrap}'
    '.tkl-spessore .lettura .mat{margin-left:0;width:100%;text-align:left;order:3}'
    '.tkl-spessore .tavola{--l:112px}'
    '.tkl-spessore .sp-figura figcaption{padding-left:0}}'
)

SCELTA = ('<div class="scelta" role="radiogroup" aria-label="Metallo">'
          '<button type="button" role="radio" aria-checked="true" tabindex="0" data-mat="ferro" data-t="20">Ferro <span>20</span></button>'
          '<button type="button" role="radio" aria-checked="false" tabindex="-1" data-mat="inox" data-t="15">Inox <span>15</span></button>'
          '<button type="button" role="radio" aria-checked="false" tabindex="-1" data-mat="alluminio" data-t="10">Alluminio <span>10</span></button>'
          '</div>')

FIGURA = ('<figure class="sp-figura" id="figura" data-mat="ferro">'
          '<div class="lettura"><output id="lettura" for="figura" aria-live="polite">20</output><span class="u">mm</span>'
          '<p class="mat"><b id="nome-mat">Ferro</b>spessore massimo di taglio</p></div>'
          '<div class="tavola" aria-hidden="true"><ol class="legenda">'
          '<li data-q="20" class="su" style="bottom:20mm">ferro<b>20</b></li>'
          '<li data-q="15" style="bottom:15mm">inox<b>15</b></li>'
          '<li data-q="10" style="bottom:10mm">alluminio<b>10</b></li>'
          '<li style="bottom:0">mm<b>0</b></li></ol>'
          '<div class="scala"></div>'
          '<div class="guide"><i data-q="20" class="su" style="bottom:20mm"></i><i data-q="15" style="bottom:15mm"></i>'
          '<i data-q="10" style="bottom:10mm"></i></div>'
          '<div class="sezione"></div></div>'
          '<figcaption><b>Scala 1:1.</b> La lamiera in sezione, tratteggiata come in un disegno tecnico. È disegnata in millimetri: '
          'su uno schermo a densità standard è spessa quanto il foglio vero.</figcaption></figure>')

# lo script della pagina statica, invariato
SCRIPT_SPESSORE = r"""(function(){
  var gruppo=document.querySelector('.scelta');
  var bottoni=[].slice.call(gruppo.querySelectorAll('[role=radio]'));
  var figura=document.getElementById('figura');
  var lettura=document.getElementById('lettura');
  var nome=document.getElementById('nome-mat');
  var quote=[].slice.call(figura.querySelectorAll('[data-q]'));
  function scegli(b,fuoco){
    bottoni.forEach(function(x){var on=x===b;x.setAttribute('aria-checked',on);x.tabIndex=on?0:-1;});
    var t=b.dataset.t;
    figura.dataset.mat=b.dataset.mat;
    figura.style.setProperty('--t',t);
    lettura.textContent=t;
    nome.textContent=b.firstChild.textContent.trim();
    quote.forEach(function(q){q.classList.toggle('su',q.dataset.q===t);});
    if(fuoco)b.focus();
  }
  bottoni.forEach(function(b,i){
    b.addEventListener('click',function(){scegli(b,false);});
    b.addEventListener('keydown',function(e){
      var k=e.key,j=null;
      if(k==='ArrowRight'||k==='ArrowDown')j=(i+1)%bottoni.length;
      else if(k==='ArrowLeft'||k==='ArrowUp')j=(i-1+bottoni.length)%bottoni.length;
      else if(k==='Home')j=0;else if(k==='End')j=bottoni.length-1;
      if(j!==null){e.preventDefault();scegli(bottoni[j],true);}
    });
  });
})();"""


def spessore():
    testo = C(
        H('Lo spessore,<br>a grandezza vera', level='h2', style='h2sp', color=BIANCO, css='tkl-sp-h2'),
        T('<p>Il laser è un <strong>Bystronic Byspeed da 4400&nbsp;W</strong> con carico e scarico automatici e dispositivo '
          'antigraffio. Taglia fogli fino a <span class="num nb">3000 × 1500&nbsp;mm</span>. Lo spessore massimo cambia col '
          'metallo: sceglilo e guarda la sezione.</p>', style='body', color=GRIGIO_SCURO, css='tkl-sp-p'),
        C(RAW(SCELTA), boxed=False, css='tkl-scelta-box'),
        boxed=False, css='tkl-sp-testo')
    figura = C(RAW(FIGURA + '<script>' + SCRIPT_SPESSORE + '</script>'), boxed=False, css='tkl-figura-box')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-spessore') + CSS_SPESSORE)
    return C(stile, C(testo, figura, boxed=False, css='tkl-griglia'), boxed=False, pad=0, tag='section', anchor='spessore', bg=NERO,
             css='tkl-spessore tkl-sito')


# --- 3. Il percorso del pezzo: la fascia della piegatrice, poi i sette passi su una riga di quota (fondo chiaro)
CSS_CHIARO = (
    '.tkl-chiaro{background:var(--chiaro)!important;color:var(--inchiostro)}'
)

CSS_PERCORSO = (
    contenitore('.tkl-percorso') +
    '.tkl-percorso{padding:0 0 clamp(64px,6.5vw,92px)!important;display:block!important}'
    '.tkl-percorso .tkl-banda{position:relative!important;background:var(--nero)!important;display:block!important;padding:0!important;'
    'margin:0!important;min-height:0!important}'
    '.tkl-banda .tkl-largo img{width:100%!important;height:clamp(200px,25vw,400px)!important;max-width:none!important;object-fit:cover;'
    'object-position:50% 50%}'
    '.tkl-banda .tkl-stretto img{width:100%!important;height:auto!important;max-width:none!important;aspect-ratio:1000/625}'
    '.tkl-banda .tkl-ind-foto{position:absolute!important;right:var(--m);bottom:12px;width:auto!important}'
    '.tkl-banda .tkl-ind-foto,.tkl-banda .tkl-ind-foto p{font:400 13px/1.55 var(--f)!important;color:var(--grigio-scuro)!important}'
    '.tkl-percorso .tkl-capo{padding-top:clamp(48px,4.6vw,66px)!important;row-gap:20px!important;align-items:end!important}'
    '.tkl-percorso .tkl-capo .tkl-titolo-sez{grid-column:1/7}'
    '.tkl-percorso .tkl-capo-p{grid-column:8/13;max-width:28em!important}'
    '.tkl-percorso .tkl-capo-p,.tkl-percorso .tkl-capo-p p{font:400 18px/1.5 var(--f)!important;color:var(--grigio)!important}'
    '.tkl-percorso .tkl-passi{display:grid!important;grid-template-columns:repeat(7,minmax(0,1fr));grid-auto-rows:auto;column-gap:0!important;'
    'row-gap:0!important;margin:clamp(40px,4vw,56px) var(--m) 0!important;padding:0!important;width:auto!important;max-width:none!important;'
    'min-height:0!important}'
    '.tkl-passi>.tkl-passo{display:grid!important;grid-row:span 4;grid-template-rows:subgrid;position:relative!important;gap:0!important;'
    'padding:0!important;margin:0!important;width:auto!important;max-width:none!important;min-width:0;min-height:0!important}'
    '.tkl-passo>*{padding-right:var(--gap)!important;width:auto!important;max-width:none!important;min-width:0}'
    '.tkl-passo .tkl-n{padding-bottom:14px!important}'
    '.tkl-passo .tkl-n,.tkl-passo .tkl-n p{font:200 clamp(44px,4.2vw,60px)/1 var(--f)!important;letter-spacing:-.03em!important;'
    'color:#9b9286!important;font-variant-numeric:tabular-nums lining-nums!important}'
    '.tkl-passo .tkl-passo-h{position:relative!important;padding-top:20px!important;margin-bottom:12px!important;border-top:1px solid var(--inchiostro);'
    'background:repeating-linear-gradient(90deg,rgba(22,19,15,.42) 0 1px,transparent 1px 8px) left top/100% 6px no-repeat}'
    + ht('.tkl-passo .tkl-passo-h') + '{font:400 21px/1.2 var(--f)!important;letter-spacing:-.01em!important;color:var(--inchiostro)!important;'
    'text-transform:none!important}'
    # la tacca lunga all'inizio di ogni passo, come una quota, e la tacca di chiusura dopo l'ultimo passo
    '.tkl-passo .tkl-passo-h::before{content:"";position:absolute;left:0;top:-15px;width:1px;height:15px;background:var(--inchiostro)}'
    '.tkl-passo:last-child .tkl-passo-h::after{content:"";position:absolute;right:0;top:-15px;width:1px;height:15px;background:var(--inchiostro)}'
    '.tkl-passo .tkl-mac,.tkl-passo .tkl-mac p{font:600 15px/1.4 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-passo .tkl-mis{margin-top:3px!important}'
    '.tkl-passo .tkl-mis,.tkl-passo .tkl-mis p{font:400 15px/1.4 var(--f)!important;color:var(--grigio)!important;'
    'font-variant-numeric:tabular-nums lining-nums!important}'
    '@media (max-width:1180px){.tkl-percorso .tkl-passi{grid-template-columns:repeat(4,minmax(0,1fr))}'
    '.tkl-passi>.tkl-passo:nth-child(n+5) .tkl-n{padding-top:44px!important}}'
    '@media (max-width:1100px){.tkl-percorso .tkl-capo .tkl-titolo-sez{grid-column:1/13}.tkl-percorso .tkl-capo-p{grid-column:1/10}}'
    '@media (max-width:640px){'
    '.tkl-banda .tkl-ind-foto{bottom:8px}'
    '.tkl-percorso .tkl-capo .tkl-titolo-sez,.tkl-percorso .tkl-capo-p{grid-column:1/13}'
    '.tkl-percorso .tkl-capo-p,.tkl-percorso .tkl-capo-p p{font-size:17px!important}'
    # i passi in colonna: numero a sinistra
    '.tkl-percorso .tkl-passi{display:block!important;margin-top:36px!important}'
    '.tkl-passi>.tkl-passo{display:grid!important;grid-template-columns:56px minmax(0,1fr);grid-template-rows:none;column-gap:0!important;'
    'padding:14px 0 16px!important;border-top:1px solid var(--filo-chiaro)!important}'
    '.tkl-passi>.tkl-passo:last-child{border-bottom:1px solid var(--filo-chiaro)!important}'
    '.tkl-passo>*{padding-right:0!important;grid-column:2}'
    '.tkl-passo .tkl-n,.tkl-passi>.tkl-passo:nth-child(n+5) .tkl-n{grid-column:1;grid-row:1 / span 3;padding:2px 0 0!important}'
    '.tkl-passo .tkl-n,.tkl-passo .tkl-n p{font-size:30px!important}'
    '.tkl-passo .tkl-passo-h{grid-row:1;border-top:0;background:none;padding-top:0!important;margin-bottom:4px!important}'
    + ht('.tkl-passo .tkl-passo-h') + '{font-size:20px!important}'
    '.tkl-passo .tkl-passo-h::before,.tkl-passo:last-child .tkl-passo-h::after{display:none}'
    '.tkl-passo .tkl-mac{grid-row:2}'
    '.tkl-passo .tkl-mis{grid-row:3;margin-top:0!important}}'
)

PASSI = [
    ('Progettazione 3D', 'Ufficio tecnico interno', 'rendering e prototipo'),
    ('Taglio laser', 'Bystronic Byspeed 4400&nbsp;W', 'campo <span class="nb">3000 × 1500&nbsp;mm</span>'),
    ('Punzonatura e cesoia', 'Finn-Power SG6', 'pezzo già separato e impilato'),
    ('Piegatura CNC', 'Finn-Power 8 assi e Warcom', 'lunghezza utile <span class="nb">3100&nbsp;mm</span>'),
    ('Saldatura', 'MIG e TIG', 'ferro, inox, alluminio'),
    ('Tubi e profili', 'OMES, Ercolina, Pedrazzoli', 'curvatura fino a <span class="nb">20 × 20 × 3</span>'),
    ('Montaggio e consegna', 'Due autocarri propri', 'centinato da 50&nbsp;q e <span class="nb">con gru</span>'),
]


def percorso():
    alt = 'Una mano con il guanto accompagna la lamiera sotto gli utensili della piegatrice; a sinistra la linea rossa del laser di riferimento.'
    banda = C(I(img('piega-2400.jpg'), alt=alt, css='tkl-largo'), I(img('piega-m-1000.jpg'), alt=alt, css='tkl-stretto'),
              T('<p>Foto indicativa</p>', style='piccolo', color=GRIGIO_SCURO, css='tkl-ind-foto'),
              boxed=False, css='tkl-banda')
    capo = C(H('Il percorso del pezzo', level='h2', style='h2', color=INCHIOSTRO, css='tkl-titolo-sez'),
             T(ap("<p>Dal file al camion, in un'officina sola. Verniciatura, cromatura, sabbiatura e zincatura le seguiamo noi su "
                  "impianti esterni collegati.</p>"), style='body', color=GRIGIO, css='tkl-capo-p'),
             boxed=False, css='tkl-griglia tkl-capo')

    def passo(i, nome, mac, mis):
        return C(T(f'{i:02d}', style='n', color='#9b9286', css='tkl-n'),
                 H(nome, level='h3', style='passo', color=INCHIOSTRO, css='tkl-passo-h'),
                 T(f'<p>{mac}</p>', style='mac', color=INCHIOSTRO, css='tkl-mac'),
                 T(f'<p>{mis}</p>', style='mis', color=GRIGIO, css='tkl-mis'),
                 boxed=False, css='tkl-passo')
    passi = C(*[passo(i, *p) for i, p in enumerate(PASSI, 1)], boxed=False, css='tkl-passi')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-percorso', chiaro=True) + CSS_CHIARO + CSS_PERCORSO)
    return C(stile, banda, capo, passi, boxed=False, pad=0, tag='section', anchor='percorso', bg=CHIARO,
             css='tkl-percorso tkl-chiaro tkl-sito')


# --- 4. Dove finiscono i nostri pezzi: una frase sola con le note numerate
CSS_SETTORI = (
    contenitore('.tkl-settori') +
    '.tkl-settori{padding:clamp(64px,7vw,104px) 0 clamp(72px,7.5vw,108px)!important;border-top:1px solid var(--filo-chiaro)!important;'
    'display:block!important}'
    '.tkl-settori .tkl-settori-h{grid-column:1/13;margin-bottom:24px!important}'
    + ht('.tkl-settori .tkl-settori-h') + '{font:600 17px/1.55 var(--f)!important;color:var(--inchiostro)!important;text-transform:none!important;'
    'letter-spacing:0!important}'
    '.tkl-settori .tkl-elenco{grid-column:1/13}'
    '.tkl-settori .tkl-elenco,.tkl-settori .tkl-elenco p{font:200 clamp(32px,4.4vw,64px)/1.08 var(--f)!important;letter-spacing:-.025em!important;'
    'color:var(--inchiostro)!important}'
    '.tkl-settori .tkl-elenco p{text-wrap:pretty!important}'
    '.tkl-settori .tkl-elenco sup{font-size:max(.28em,12px);font-weight:500;letter-spacing:0;vertical-align:top;position:relative;top:.5em;'
    'margin-left:.06em;color:var(--bronzo);font-variant-numeric:tabular-nums;line-height:inherit}'
    '.tkl-settori .tkl-note{grid-column:1/13;margin-top:clamp(36px,4vw,56px)!important}'
    '.tkl-settori .tkl-note ol{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));column-gap:var(--gap);row-gap:16px;margin:0!important;'
    'padding:0!important;list-style:none!important}'
    '.tkl-settori .tkl-note li{display:flex;gap:10px;margin:0!important;padding:0!important;border:0!important;'
    'font:400 15px/1.42 var(--f)!important;color:var(--grigio)!important}'
    '.tkl-settori .tkl-note li b{color:var(--bronzo);font-weight:500;font-variant-numeric:tabular-nums;min-width:10px}'
    '@media (max-width:1100px){.tkl-settori .tkl-note ol{grid-template-columns:repeat(3,minmax(0,1fr))}}'
    '@media (max-width:640px){.tkl-settori .tkl-note ol{grid-template-columns:1fr 1fr;row-gap:14px}}'
)


def settori():
    elenco = T(ap("<p>Elettromedicale ed elettronica<sup>1</sup>, arredo medicale e odontoiatrico<sup>2</sup>, refrigerazione "
                  "commerciale<sup>3</sup>, trattamento dell'aria e dei fluidi<sup>4</sup>, macchine agricole e movimento "
                  "terra<sup>5</sup>, meccanica leggera<sup>6</sup></p>"), style='elenco', color=INCHIOSTRO, css='tkl-elenco')
    note = ['Case metallici per gli apparecchi.', 'Semilavorati per studi medici e dentistici.', 'Telai in tubolare per i banchi frigo.',
            'Semilavorati coibentati, con guarnizioni e chiusure.', 'Particolari complessi.',
            'Carpenteria leggera, per qualsiasi settore meccanico.']
    lista = T('<ol>' + ''.join(f'<li><b>{i}</b>{t}</li>' for i, t in enumerate(note, 1)) + '</ol>', style='note', color=GRIGIO,
              css='tkl-note')
    griglia = C(H('Dove finiscono i nostri pezzi', level='h2', style='h2p', color=INCHIOSTRO, css='tkl-settori-h'), elenco, lista,
                boxed=False, css='tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-settori', chiaro=True) + CSS_CHIARO + CSS_SETTORI)
    return C(stile, griglia, boxed=False, pad=0, tag='section', anchor='settori', bg=CHIARO, css='tkl-settori tkl-chiaro tkl-sito')


# --- 5. Dal ferro battuto alla lamiera: la storia, la loro foto della saldatura, le persone
CSS_FAMIGLIA = (
    contenitore('.tkl-famiglia') +
    '.tkl-famiglia{padding:clamp(64px,7vw,104px) 0 clamp(72px,8vw,116px)!important;border-top:1px solid var(--filo-chiaro)!important;'
    'display:block!important}'
    '.tkl-famiglia .tkl-griglia{row-gap:0!important;align-items:start!important}'
    '.tkl-famiglia .tkl-titolo-sez{grid-column:1/7}'
    '.tkl-famiglia .tkl-storia{grid-column:1/7;margin-top:28px!important;max-width:30em!important}'
    '.tkl-famiglia .tkl-storia,.tkl-famiglia .tkl-storia p{font:400 20px/1.5 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-famiglia .tkl-doc{grid-column:4/13;margin:clamp(40px,4.5vw,64px) calc(var(--m) * -1) 0 0!important}'
    '.tkl-famiglia .tkl-doc img{width:100%!important;height:auto!important;max-width:none!important;aspect-ratio:1330/560}'
    '.tkl-famiglia .tkl-piede-doc{grid-column:4/13;display:grid!important;grid-template-columns:repeat(9,minmax(0,1fr));column-gap:var(--gap)!important;'
    'row-gap:0!important;padding:14px 0 0!important;margin:0!important;width:auto!important;max-width:none!important;min-height:0!important}'
    + FIGLI.format(s='.tkl-famiglia .tkl-piede-doc') +
    '.tkl-famiglia .tkl-didascalia{grid-column:1/5}'
    '.tkl-famiglia .tkl-didascalia,.tkl-famiglia .tkl-didascalia p{font:400 14px/1.45 var(--f)!important;color:var(--grigio)!important}'
    '.tkl-famiglia .tkl-persone{grid-column:6/10;display:grid!important;grid-template-columns:1fr 1fr;column-gap:var(--gap)}'
    '.tkl-famiglia .tkl-persone>.elementor-widget-container{display:contents!important}'
    '.tkl-famiglia .tkl-persone,.tkl-famiglia .tkl-persone p{font:400 15px/1.45 var(--f)!important;color:var(--inchiostro)!important}'
    '.tkl-famiglia .tkl-persone b{display:block;font-weight:600;font-size:17px}'
    '.tkl-famiglia .tkl-persone span{color:var(--grigio)}'
    '@media (max-width:1100px){'
    '.tkl-famiglia .tkl-titolo-sez{grid-column:1/13}'
    '.tkl-famiglia .tkl-storia{grid-column:1/11}'
    '.tkl-famiglia .tkl-doc{grid-column:1/13;margin-left:calc(var(--m) * -1)!important}'
    '.tkl-famiglia .tkl-piede-doc{grid-column:1/13;grid-template-columns:repeat(12,minmax(0,1fr))}'
    '.tkl-famiglia .tkl-didascalia{grid-column:1/7}'
    '.tkl-famiglia .tkl-persone{grid-column:7/13}}'
    '@media (max-width:640px){'
    '.tkl-famiglia .tkl-storia,.tkl-famiglia .tkl-storia p{font-size:18px!important}'
    '.tkl-famiglia .tkl-storia{grid-column:1/13}'
    '.tkl-famiglia .tkl-didascalia,.tkl-famiglia .tkl-persone{grid-column:1/13}'
    '.tkl-famiglia .tkl-persone{margin-top:22px!important}}'
)


def famiglia():
    storia = T(ap("<p>La famiglia Volpato lavora il metallo dal 1978: prima piccoli manufatti in ferro battuto come FDS Volpato S.n.c., "
                  "dal 2020 lamiera come Tek.Lam S.r.l. L'ufficio tecnico è in casa e segue il pezzo dall'idea alla consegna.</p>"),
               style='storia', color=INCHIOSTRO, css='tkl-storia')
    doc = I(img('officina-1330.jpg'), alt='Saldatura TIG su un cassone inox ancora coperto dal film protettivo stampato.', css='tkl-doc')
    piede = C(T('<p>Saldatura TIG su un cassone inox, con il film protettivo ancora addosso.</p>', style='didascalia', color=GRIGIO,
                css='tkl-didascalia'),
              T('<p><b>Sandro Volpato</b><span>Ufficio tecnico</span></p><p><b>Dimitri Volpato</b><span>Commerciale</span></p>',
                style='persone', color=INCHIOSTRO, css='tkl-persone'),
              boxed=False, css='tkl-piede-doc')
    griglia = C(H('Dal ferro battuto<br>alla lamiera', level='h2', style='h2', color=INCHIOSTRO, css='tkl-titolo-sez'), storia, doc, piede,
                boxed=False, css='tkl-griglia')
    stile = RAW('', css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-famiglia', chiaro=True) + CSS_CHIARO + CSS_FAMIGLIA)
    return C(stile, griglia, boxed=False, pad=0, tag='section', anchor='famiglia', bg=CHIARO, css='tkl-famiglia tkl-chiaro tkl-sito')


# --- 6. Contatti: il telefono grande sulla foto dell'ugello
CSS_CONTATTI = (
    contenitore('.tkl-contatti') +
    '.tkl-contatti{position:relative!important;padding:clamp(88px,9vw,132px) 0 clamp(64px,6vw,88px)!important;overflow:hidden!important;'
    'background:var(--nero)!important;display:block!important}'
    + senza_scatola('.tkl-contatti .tkl-fondo') +
    '.tkl-contatti .fondo{position:absolute;inset:0}'
    '.tkl-contatti .fondo img{width:100%;height:100%;max-width:none;object-fit:cover;object-position:40% 60%}'
    '.tkl-contatti .tkl-griglia{position:relative;row-gap:36px!important}'
    '.tkl-contatti .tkl-contatti-h{grid-column:1/13}'
    + ht('.tkl-contatti .tkl-contatti-h') + '{font:600 17px/1.55 var(--f)!important;color:var(--bianco)!important;text-transform:none!important;'
    'letter-spacing:0!important}'
    '.tkl-contatti .tkl-telefono{grid-column:1/13;width:max-content!important;max-width:100%!important;margin-left:-.04em!important}'
    + ht('.tkl-contatti .tkl-telefono') + '{font:200 clamp(56px,11vw,160px)/.9 var(--f)!important;letter-spacing:-.04em!important;'
    'font-variant-numeric:tabular-nums lining-nums!important;color:var(--bianco)!important;text-transform:none!important}'
    '.tkl-contatti .tkl-telefono a{display:block;color:inherit!important;text-decoration:none!important}'
    '.tkl-contatti .tkl-telefono a:hover{color:var(--paglia)!important}'
    '.tkl-contatti .tkl-invito{grid-column:1/8;max-width:30em!important}'
    '.tkl-contatti .tkl-invito,.tkl-contatti .tkl-invito p{font:400 21px/1.42 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-contatti .tkl-invito a{color:var(--paglia)!important}'
    '.tkl-contatti .tkl-invito a:hover{color:var(--bianco)!important}'
    '.tkl-contatti .tkl-recapiti{grid-column:1/13;display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:var(--gap)!important;'
    'row-gap:28px!important;padding:26px 0 0!important;border-top:1px solid var(--filo)!important;margin:0!important;width:auto!important;'
    'max-width:none!important;min-height:0!important}'
    + FIGLI.format(s='.tkl-contatti .tkl-recapiti') +
    '.tkl-recapiti .tkl-r,.tkl-recapiti .tkl-r p{font:400 16px/1.5 var(--f)!important;color:var(--bianco)!important}'
    '.tkl-recapiti .tkl-r b{display:block;font-weight:600;margin-bottom:4px}'
    '.tkl-recapiti .tkl-r span{color:#c9c1b5}'
    '.tkl-recapiti .tkl-r a{overflow-wrap:anywhere;color:inherit!important}'
    '.tkl-recapiti .tkl-r a:hover{color:var(--paglia)!important}'
    '@media (max-width:1100px){.tkl-contatti .tkl-recapiti{grid-template-columns:repeat(2,minmax(0,1fr))}'
    '.tkl-contatti .tkl-invito{grid-column:1/13}}'
    '@media (max-width:640px){'
    '.tkl-contatti .tkl-recapiti{grid-template-columns:repeat(2,minmax(0,1fr));column-gap:16px!important}'
    '.tkl-recapiti .tkl-r,.tkl-recapiti .tkl-r p{font-size:15px!important}'
    '.tkl-recapiti .tkl-r:last-child{grid-column:1/3}'
    '.tkl-contatti .tkl-invito,.tkl-contatti .tkl-invito p{font-size:19px!important}}'
)


def contatti():
    # il fondo è decorativo, senza testo alternativo, come nella statica: un <picture> in un widget HTML
    fondo = C(RAW('<picture class="fondo"><source media="(max-width:640px)" srcset="' + img('contatti-m-800.jpg') + '">'
                  f'<img src="{img("contatti-1600.jpg")}" srcset="{img("contatti-1000.jpg")} 1000w, {img("contatti-1600.jpg")} 1600w, '
                  f'{img("contatti-2400.jpg")} 2400w" sizes="100vw" width="2400" height="1000" loading="lazy" alt=""></picture>'),
              boxed=False, css='tkl-fondo')

    def recapito(html):
        return T(ap(f'<p>{html}</p>'), style='recapiti', color=BIANCO, link_color=BIANCO, link_hover=BIANCO, css='tkl-r')
    recapiti = C(
        recapito('<b>Ufficio tecnico</b>Sandro Volpato<br><a href="mailto:sandro@teklam.it">sandro@teklam.it</a>'),
        recapito('<b>Commerciale</b>Dimitri Volpato<br><a href="mailto:dimitri@teklam.it">dimitri@teklam.it</a><br>'
                 '<a href="mailto:commerciale@teklam.it">commerciale@teklam.it</a>'),
        recapito('<b>Informazioni</b><a href="mailto:info@teklam.it">info@teklam.it</a><br>'
                 '<span>Fax <span class="num">+39&nbsp;049&nbsp;982&nbsp;90&nbsp;91</span></span>'),
        recapito("<b>Officina</b>Via del Lavoro 68, zona artigianale Tombelle, 30030 Vigonovo (VE)<br><span>Vicino al casello Padova "
                 "Interporto dell'A13.</span> <a href=\"https://www.google.com/maps/search/?api=1&amp;query=Via+del+Lavoro+68+Vigonovo+VE\">"
                 'Mappa</a>'),
        boxed=False, css='tkl-recapiti')
    griglia = C(
        H('Contatti', level='h2', style='h2p', color=BIANCO, css='tkl-contatti-h'),
        H(TEL, level='div', style='telefono', color=BIANCO, link=TEL_LINK, css='tkl-telefono'),
        T(ap("<p>Per un preventivo mandate il disegno o il file 3D all'ufficio tecnico, "
             '<a href="mailto:ufftec@teklam.it">ufftec@teklam.it</a>.</p>'), style='invito', color=BIANCO, link_color=PAGLIA,
          link_hover=PAGLIA, sottolinea=True, css='tkl-invito'),
        recapiti, boxed=False, css='tkl-griglia')
    # come nella statica, le sezioni dall'apertura ai contatti stanno in <main> (punto di riferimento per i lettori di schermo):
    # Elementor gratuito non ha un contenitore che le raccolga, lo fa questo script quando la pagina arriva ai contatti
    # (anche nel fallback; mai nell'editor di Elementor, che ha bisogno dei suoi elementi al loro posto). Come in Paraga Pelli.
    principale = ("<script>(function(){var a=document.querySelector('.tkl-apertura'),z=document.getElementById('contatti');"
                  "if(!a||!z||a.closest('main')||document.body.classList.contains('elementor-editor-active'))return;"
                  "var p=a.parentNode;while(p&&!p.contains(z))p=p.parentNode;if(!p)return;"
                  "while(a.parentNode!==p)a=a.parentNode;while(z.parentNode!==p)z=z.parentNode;"
                  "var m=document.createElement('main');p.insertBefore(m,a);"
                  "while(m.nextElementSibling){var x=m.nextElementSibling;m.appendChild(x);if(x===z)break}})();</script>")
    stile = RAW(principale, css=CSS_VARIABILI + CSS_COMUNE + css_testi('tkl-contatti') + CSS_CONTATTI)
    return C(stile, fondo, griglia, boxed=False, pad=0, tag='section', anchor='contatti', bg=NERO, css='tkl-contatti tkl-sito')


def home():
    return [('apertura', apertura()), ('spessore', spessore()), ('percorso', percorso()), ('settori', settori()),
            ('famiglia', famiglia()), ('contatti', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Tek.Lam, lamiera conto terzi a Vigonovo',
     'descrizione': 'Carpenteria in lamiera conto terzi a Tombelle di Vigonovo (VE): progettazione 3D, taglio laser, punzonatura, '
                    'piegatura CNC, saldatura, tubi e profili. La famiglia Volpato dal 1978.'},
]
