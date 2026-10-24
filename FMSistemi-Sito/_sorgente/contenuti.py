# -*- coding: utf-8 -*-
"""
Contenuti della home di F.M. Sistemi per WordPress + Elementor: la home statica approvata ("Dalla A alla Z",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: testata (logo, menu di Ultimate Addons, telefono), titolo
  "Dalla A alla Z", riga sotto il titolo, didascalia della T, bottone "Telefonate" e "o scrivete", titoli, testi,
  le otto righe dei mestieri (indice, capolettera, nome, testo, "Nella foto", striscia), foto del collettore e della
  parete d'inverno, il 17 e la scheda, la frase, i contatti, il piede.
- Widget HTML (nodo RAW del motore) solo per le parti che Elementor gratuito non fa: il raccordo a T dell'apertura
  (il <picture> della statica con il taglio del telefono, posato con la geometria della pagina: barra sotto il
  titolo, gambo sull'asse della T dell'alfabeto, sfumatura nella calce) e l'alfabeto delle 21 lettere, con le otto
  accese che portano alla riga del loro mestiere. La pagina statica non ha JavaScript: neanche qui, a parte una riga
  che raccoglie le sezioni in <main> come nella statica.
- L'impaginazione (griglia a 12 colonne, misure fluide con clamp e con le unità del contenitore, colori) è il foglio
  di stile della pagina statica, con le classi fms-, dentro i nodi RAW: vale uguale per il template Elementor e per il
  fallback. Il segno di rame sotto la capolettera della riga scelta è il :target della statica sull'ancora della riga.

Testi e dati: tutti dalla home statica (fonti in 01-analisi.md, dati da confermare nel LEGGIMI). Nessun dato nuovo.
"""
import motore as m
from motore import C, H, T, B, I, RAW, MENU

PREFISSO = 'fms'
NOME_SITO = 'FM Sistemi'

# ---------------------------------------------------------------------------------------------
# Tema: i colori e i caratteri della home statica
# ---------------------------------------------------------------------------------------------
# palette chiara: calce, grafite, rame; il blu FM solo nel logo e nel segno del fuoco
FONDO = '#EDE7DE'          # calce, uguale al fondo della foto d'apertura
TESTO = '#23201C'          # grafite, 13,2:1
TESTO2 = '#5C554C'         # secondario, 6,0:1
SPENTO = '#857C70'         # lettere spente dell'alfabeto, solo in grande
PIETRA = '#E3DBCE'         # il piede
FILETTO = '#D3CABD'
RAME = '#B4703A'           # bottone e segni sotto le lettere
RAME_TESTO = '#8F4F1F'     # rame per il testo: lettere accese, capolettera, inizio della riga, passaggio del mouse
NERO_RAME = '#1A1714'      # testo del bottone
BLU = '#046EA2'            # blu FM: segno del fuoco da tastiera

DISPLAY = 'Funnel Display'
SANS = 'Funnel Sans'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# misure (1440, 1024, 390) della pagina statica: valgono per il pannello di Elementor;
# le misure vere, fluide e con i breakpoint della statica (1100, 860, 600, 360), sono nel foglio di stile
STILI = {
    'h1':     _st(DISPLAY, '400', (160, 143, 82), 0.9, -7.2),
    'h2':     _st(DISPLAY, '400', (56, 40, 34), 1.04, -1.68),
    'h3':     _st(DISPLAY, '400', (28, 24, 24), 1.05, -0.56),
    'h3col':  _st(SANS, '500', (15, 15, 15), 1.3),
    'cap':    _st(DISPLAY, '400', (152, 112, 80), 0.74, -3),
    'cifra':  _st(DISPLAY, '400', (216, 154, 120), 0.8, -10.8),
    'frase':  _st(DISPLAY, '400', (56, 40, 32), 1.08, -1.68),
    'telg':   _st(DISPLAY, '400', (92, 66, 44), 1.0, -3.2),
    'riga':   _st(SANS, '400', (17, 18, 17), 1.35),
    'intro':  _st(SANS, '400', (20, 20, 18), 1.55),
    'body':   _st(SANS, '400', (18, 18, 17), 1.55),
    't17':    _st(SANS, '400', (17, 17, 16), 1.45),
    'dt':     _st(SANS, '400', (16, 16, 16), 1.5),
    'dd':     _st(SANS, '400', (18, 18, 18), 1.5),
    'col':    _st(SANS, '400', (17, 17, 17), 1.55),
    'fig':    _st(SANS, '400', (14, 14, 14), 1.55),
    'piede':  _st(SANS, '400', (14, 14, 14), 1.6),
    'nella':  _st(SANS, '400', (13, 13, 13), 1.45),
    'idx':    _st(SANS, '400', (14, 14, 13), 1.0),
    'nav':    _st(SANS, '400', (16, 16, 16), 1.55),
    'tel':    _st(SANS, '500', (16, 16, 15), 1.0),
    'btn':    _st(SANS, '500', (17, 17, 17), 1.0),
}

TEMA = {
    'nome': 'Dalla A alla Z',
    'fondo': FONDO, 'superficie': FONDO, 'inchiostro': TESTO, 'testo2': TESTO2, 'accento': RAME_TESTO,
    'filetto': FILETTO, 'filetto_scuro': FILETTO, 'su_scuro2': TESTO2,
    'scuro': FONDO, 'su_scuro': TESTO, 'su_accento': NERO_RAME,
    'font_titoli': DISPLAY, 'font_testo': SANS, 'larghezza': 1440,
    'stili': STILI,
    'spazi': {'sezione': (160, 160, 96), 'lato': (64, 46, 20), 'm': (24, 24, 24), 's': (12, 12, 12), '0': (0, 0, 0)},
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): l'hover cambia colore pieno, mai opacità
    'bottoni': {'rame': (NERO_RAME, RAME, RAME, FONDO, TESTO, TESTO)},
    'bottone': {'raggio': 0, 'pad': (13.5, 22, 13.5, 22), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# Il raccordo a T (widget HTML) e i caratteri restano a questo indirizzo: per non dipendere da GitHub
# si carica assets/web/ sul sito e si rigenera con build.py --base (vedi LEGGIMI).
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/FMSistemi-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'
    # i caratteri sono serviti dalla stessa base delle immagini (assets/web/fonts/*.woff2), con le @font-face scritte
    # nel foglio di stile di ogni sezione (css_variabili). Niente foglio dei caratteri a parte: raw.githubusercontent
    # serve i .css come text/plain con nosniff e il browser li scarta (ERR_BLOCKED_BY_ORB), mentre i woff2 li carica.
    # Il motore scrive comunque un <link rel=stylesheet> verso questo indirizzo nel fallback e nell'anteprima: foglio vuoto.
    m.GOOGLE_FONTS = 'data:text/css,'


imposta_base(BASE_PREDEFINITA)


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (come nella home statica; da confermare quelli elencati nel LEGGIMI)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}8305354'
TEL_LINK = 'tel:+390498305354'
MAIL_SOPRALLUOGO = 'mailto:commerciale@fmsistemisrl.it?subject=Richiesta%20di%20sopralluogo'
MAIL_PREVENTIVO = 'mailto:commerciale@fmsistemisrl.it?subject=Richiesta%20di%20preventivo'
VIESSMANN = 'https://fm-sistemi-srl.partner-viessmann.it/'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Via+del+Lavoro+37+30030+Vigonovo+VE'
FACEBOOK = 'https://www.facebook.com/FM-Sistemi-SRL-865904943478639'

# voci del menu: in WordPress è il menu "Menu FM Sistemi" (link personalizzati, li crea l'installatore)
VOCI_MENU = [('Lavori', '/#lavori'), ('Chi siamo', '/#chi'), ('Contatti', '/#contatti')]

# i mestieri nell'ordine del cantiere: lettera, nome, riga, didascalia della foto, testo alternativo della striscia
MESTIERI = [
    ('r', 'Ristrutturazioni', 'Ristrutturazioni edili: si apre il muro e, a impianti finiti, lo si richiude.',
     'Nella foto: cazzuola con la malta.', 'Mano con una cazzuola carica di malta'),
    ('t', 'Termoidraulica', 'Riscaldamento e acqua calda sanitaria: tubi, raccordi e collettori.',
     'Nella foto: raccordo a T in rame.', 'Raccordo a T in rame, la barra e l’attacco del gambo'),
    ('e', 'Elettrico', "Impianti elettrici, dal quadro all'ultima presa.",
     'Nella foto: morsetti di un quadro e cavi in parallelo.', 'Morsetti di una fila di interruttori e cavi pettinati in parallelo'),
    ('a', 'Acqua', "Trattamento dell'acqua che arriva a caldaia e rubinetti.",
     'Nella foto: gocce d’acqua su una superficie chiara.', 'Gocce d’acqua fitte su una superficie chiara'),
    ('p', 'Pompe di calore', 'Pompe di calore e sistemi ibridi, come partner Viessmann.',
     'Nella foto: griglia del ventilatore di un’unità esterna.', 'Griglia a spirale del ventilatore di un’unità esterna'),
    ('c', 'Clima', "Climatizzatori e trattamento dell'aria.",
     'Nella foto: griglia di aerazione.', 'Griglia bianca di aerazione'),
    ('f', 'Fotovoltaico', 'Fotovoltaico residenziale, sul tetto di casa.',
     'Nella foto: celle di un modulo fotovoltaico.', 'Moduli fotovoltaici, la griglia delle celle'),
    ('m', 'Mobilità elettrica', "Punti di ricarica per l'auto elettrica.",
     'Nella foto: presa di ricarica di un’auto.', 'Presa di ricarica di un’auto elettrica'),
]

# l'alfabeto: ventuno lettere, accese solo quelle che hanno un lavoro (nome breve sotto la lettera)
ACCESE = {'A': 'Acqua', 'C': 'Clima', 'E': 'Elettrico', 'F': 'Fotovoltaico', 'M': 'Mobilità', 'P': 'Pompe di calore',
          'R': 'Ristrutturazioni', 'T': 'Termoidraulica'}
ALFABETO = 'ABCDEFGHILMNOPQRSTUVZ'


def dritto(html):
    """Apostrofo diritto come nella statica: WordPress trasforma ' in quello tipografico nei widget Testo, &#39; resta diritto."""
    return html.replace("'", '&#39;')


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def bt(sel):
    """Il bottone vero (link): in Elementor .elementor-button, nel fallback l'unico <a> del widget."""
    return f'{sel} a'


# ---------------------------------------------------------------------------------------------
# Foglio di stile comune: variabili della pagina statica (con il prefisso --fm-: Elementor usa già --display),
# regole di base. Ogni sezione lo porta con sé (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
def css_variabili():
    """Le @font-face della statica (stessi woff2, dalla base delle immagini) e le variabili della pagina."""
    return (
        '@font-face{font-family:"Funnel Display";src:url(' + img('fonts/funnel-display-latin.woff2') + ') format("woff2");'
        'font-weight:300 800;font-style:normal;font-display:swap}'
        '@font-face{font-family:"Funnel Sans";src:url(' + img('fonts/funnel-sans-latin.woff2') + ') format("woff2");'
        'font-weight:300 800;font-style:normal;font-display:swap}'
        + CSS_VARIABILI)


CSS_VARIABILI = (
    ':root{--fm-fondo:#EDE7DE;--fm-testo:#23201C;--fm-testo-2:#5C554C;--fm-spento:#857C70;--fm-pietra:#E3DBCE;'
    '--fm-filetto:#D3CABD;--fm-rame:#B4703A;--fm-rame-testo:#8F4F1F;--fm-nero-rame:#1A1714;--fm-blu:#046EA2;'
    '--fm-margine:clamp(20px,4.45vw,64px);--fm-gola:24px;--fm-passo:160px;'
    '--fm-display:"Funnel Display",system-ui,sans-serif;--fm-sans:"Funnel Sans",system-ui,sans-serif}'
    '@media (max-width:600px){:root{--fm-passo:96px}}'
    # Elementor rende morbido lo scorrimento verso le ancore (html{scroll-behavior:smooth}); la statica salta subito
    'html{scroll-behavior:auto}'
)

# regole della pagina (corpo, fondo calce): in ogni sezione, così vale anche il fallback incollato a pezzi
CSS_SITO = (
    'html{-webkit-text-size-adjust:100%;text-size-adjust:100%}'
    'body{margin:0;background:var(--fm-fondo);color:var(--fm-testo);font:400 18px/1.55 var(--fm-sans);font-kerning:normal;'
    '-webkit-font-smoothing:antialiased;font-synthesis:none;overflow-x:clip}'
    '@media (max-width:600px){body{font-size:17px}}'
)


def css_base(scope):
    """Regole di base dei widget nativi dentro una sezione: caratteri del corpo (le misure vere le scrive il foglio
    della sezione), margini del tema e di Elementor azzerati, link che prendono il colore del testo
    (il tema Hello li colora di rosa), fuoco visibile in blu FM come nella statica."""
    s = f'.{scope}'
    w = f':where({s}) :where(.elementor-widget-text-editor,.elementor-widget-heading,.elementor-heading-title,.fms-w)'
    return (
        f'{s},{s} *,{s} *::before,{s} *::after{{box-sizing:border-box}}'
        f'{w}{{font-family:var(--fm-sans)!important;font-size:18px!important;line-height:1.55!important;font-weight:400!important;'
        'letter-spacing:0!important;text-transform:none!important;font-style:normal!important}'
        f'@media (max-width:600px){{{w}{{font-size:17px!important}}}}'
        f':where({s}) :where(.elementor-widget){{margin-block:0!important}}'
        f':where({s}) :where(p,h1,h2,h3,blockquote,figure){{margin:0!important}}'
        f'{s} p,{s} h1,{s} h2,{s} h3{{text-wrap:wrap}}'
        f'{s} a{{color:inherit;text-decoration:underline;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}}'
        f'{s} a:hover{{color:var(--fm-rame-testo)}}'
        # il motore colora di rame anche i link con il fuoco (a:focus); nella statica il fuoco dà solo il contorno blu
        f'{s} .fms-scrivi a:focus:not(:hover),{s} .fms-scheda-p a:focus:not(:hover),{s} .fms-tel-grande a:focus:not(:hover),'
        f'{s} .fms-col-p a:focus:not(:hover){{color:var(--fm-testo)!important}}'
        f'{s} :focus-visible,{s} a:focus-visible{{outline:2px solid var(--fm-blu);outline-offset:3px;box-shadow:none}}'
        f'{s} .num{{font-variant-numeric:tabular-nums lining-nums}}'
        f'{s} .nowrap{{white-space:nowrap}}'
        f'{s} img{{display:block!important;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}'
        # foto doppie: la versione per computer e tablet e il taglio del telefono (nella statica un <picture>)
        f'{s} .fms-m{{display:none!important}}'
        f'@media (max-width:600px){{{s} .fms-d{{display:none!important}}{s} .fms-m{{display:block!important}}}}'
    )


GRIGLIA = ('display:grid!important;grid-template-columns:repeat(12,1fr);column-gap:var(--fm-gola)!important;row-gap:0!important;'
           'padding:0 var(--fm-margine)!important;')

# contenitori di Elementor (e del fallback) riportati a blocchi semplici, come i <div> della statica
BLOCCO = 'display:block!important;padding:0!important;margin:0!important;width:auto!important;max-width:none!important;min-height:0!important;'

CSS_COMUNE = (
    '.fms-griglia{' + GRIGLIA + 'margin:0;width:auto!important;max-width:none!important;min-height:0!important}'
    '.fms-griglia>*{width:auto!important;max-width:none!important;min-width:0}'
    f'{ht(".fms-h2")}{{font:400 clamp(34px,3.9vw,56px)/1.04 var(--fm-display)!important;letter-spacing:-.03em!important;'
    'text-wrap:balance!important}'
    '.fms-sezione{' + BLOCCO + 'margin-top:var(--fm-passo)!important}'
)


# =============================================================================================
# TESTATA (template "FM Sistemi: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_TESTATA = (
    # sopra l'apertura, come nella statica (dove è il primo elemento della pagina, in posizione assoluta)
    '.fms-testa{position:absolute!important;inset:0 0 auto 0;z-index:5;display:flex!important;flex-direction:row!important;'
    'flex-wrap:nowrap!important;align-items:center!important;justify-content:flex-start!important;gap:40px!important;'
    'padding:24px var(--fm-margine) 0!important;margin:0!important;width:auto!important;max-width:none!important;min-height:0!important;'
    'background:none!important;border:0!important}'
    '.fms-testa>*{flex:0 0 auto!important;width:auto!important;max-width:none!important;margin:0!important}'
    '.fms-testa>.fms-fuori{position:absolute!important;left:0;top:0;width:0!important;height:0!important;padding:0!important;'
    'overflow:visible!important;display:block!important}'
    '.fms-marchio a{display:block}'
    '.fms-marchio img{width:190px!important;max-width:none!important;height:auto!important}'
    '.fms-nav{display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;align-items:center!important;gap:32px!important;'
    'margin-left:auto!important;padding:0!important;font-size:16px}'
    '.fms-nav>*{flex:0 0 auto!important;width:auto!important;max-width:none!important;margin:0!important}'
    # il menu: Ultimate Addons (Elementor) e il menu del fallback, a vista uguali ai link della statica
    '.fms-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.fms-menu .fms-nav-l{display:flex!important;flex-wrap:nowrap!important;'
    'gap:32px!important;margin:0!important;padding:0!important;list-style:none}'
    '.fms-menu .hfe-nav-menu::before,.fms-menu .hfe-nav-menu::after{display:none!important}'
    '.fms-menu li,.fms-menu .hfe-nav-menu li.menu-item{display:block!important;margin:0!important;padding:0!important;border:0!important;background:none!important}'
    '.fms-menu .hfe-nav-menu a.hfe-menu-item,.fms-menu .fms-nav-l a{display:inline-flex!important;align-items:center!important;min-height:44px;'
    'padding:0!important;font-family:var(--fm-sans)!important;font-size:16px!important;font-weight:400!important;line-height:1.55!important;'
    'letter-spacing:0!important;text-transform:none!important;color:var(--fm-testo)!important;text-decoration:none!important;'
    'border:0!important;white-space:nowrap;background:none!important}'
    '.fms-menu .hfe-nav-menu a.hfe-menu-item:hover,.fms-menu .fms-nav-l a:hover{color:var(--fm-rame-testo)!important;'
    'text-decoration:underline!important;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}'
    '.fms-menu .hfe-nav-menu a.hfe-menu-item::before,.fms-menu .hfe-nav-menu a.hfe-menu-item::after{display:none!important}'
    '.fms-menu details,.fms-menu .hfe-nav-menu__toggle{display:none!important}'
    '.fms-tel p{margin:0!important;display:flex}'
    '.fms-tel a{display:inline-flex!important;align-items:center;min-height:44px;font:500 16px/1 var(--fm-sans)!important;'
    'padding-left:32px;border-left:1px solid var(--fm-filetto);color:var(--fm-testo)!important;text-decoration:none!important;white-space:nowrap}'
    '.fms-tel a:hover{color:var(--fm-rame-testo)!important;text-decoration:underline!important}'
    # "Salta ai lavori": primo elemento della pagina, come nella statica
    '.fms-sito a.fms-salta{position:absolute;left:-9999px;font:400 18px/1.55 var(--fm-sans)}'
    '.fms-sito a.fms-salta:focus{left:var(--fm-margine);top:8px;z-index:9;background:var(--fm-testo);color:var(--fm-fondo);padding:8px 12px}'
    '@media (max-width:1100px){.fms-nav,.fms-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.fms-menu .fms-nav-l{gap:22px!important}}'
    # Ultimate Addons e il fallback passano al menu a scomparsa a 1024 px; la statica non ne ha: tra 861 e 1024 resta in riga
    '@media (min-width:861px) and (max-width:1024px){'
    '.fms-menu .hfe-nav-menu__layout-horizontal,.fms-menu nav.hfe-dropdown{display:block!important;visibility:visible!important;'
    'opacity:1!important;height:auto!important;position:static!important;transform:none!important;width:auto!important;'
    'background:none!important;border:0!important;box-shadow:none!important;margin:0!important;padding:0!important}'
    '.fms-menu nav.hfe-dropdown .hfe-nav-menu{display:flex!important;gap:22px!important;background:none!important;border:0!important;'
    'visibility:visible!important;opacity:1!important;max-height:none!important;transform:none!important}'
    '.fms-menu nav.hfe-dropdown li.menu-item,.fms-menu nav.hfe-dropdown a.hfe-menu-item{width:auto!important;border:0!important;'
    'background:none!important;visibility:visible!important;opacity:1!important}'
    '.fms-menu .fms-nav-l{display:flex!important}}'
    '@media (max-width:860px){.fms-menu{display:none!important}.fms-tel a{border-left:0;padding-left:0}}'
    '@media (max-width:600px){.fms-testa{padding-top:14px!important}.fms-marchio img{width:138px!important}'
    '.fms-tel a{font-size:15px!important;padding:0 0 0 12px}}'
)

CSS_TESTATA_ELEMENTOR = (
    '#masthead{position:static}'
    '.hfe-skip-link{display:none!important}'
    '.fms-menu .hfe-nav-menu__toggle:focus-visible{outline:2px solid var(--fm-blu);outline-offset:3px}'
)


def header():
    # il nome del link ("F.M. Sistemi, inizio") lo scrive lo script della testata: Elementor divide gli attributi
    # personalizzati alla virgola e ne farebbe aria-label="F.M. Sistemi" più un attributo "inizio"
    marchio = I(img('logo.png'), 'FM Sistemi', link='/', css='fms-marchio')
    menu = MENU(VOCI_MENU, colore=TESTO, colore_hover=RAME_TESTO, accento=RAME_TESTO, fondo_menu=FONDO, linea=FILETTO,
                stile='nav', stile_mobile='nav', spazio=32, pad_h=0, pad_v=0, distanza=12, align_menu='right',
                slug='menu-fm-sistemi', css='fms-menu')
    tel = T(f'<p><a class="tel num" href="{TEL_LINK}">{TEL}</a></p>', style='tel', color=TESTO, link_color=TESTO,
            link_hover=RAME_TESTO, sottolinea=False, css='fms-tel')
    nav = C(menu, tel, dir='row', align='center', gap=32, boxed=False, css='fms-nav')
    # il menu si chiama "Principale" e il logo "F.M. Sistemi, inizio", come nella statica; testata e piede non si
    # ripetono come punti di riferimento dentro quelli di Ultimate Addons
    # (Elementor gratuito non dà attributi ai widget del menu; vedi sopra per il logo)
    globali = RAW('<a class="fms-salta" href="#lavori">Salta ai lavori</a>'
                  "<script>document.addEventListener('DOMContentLoaded',function(){"
                  "document.querySelectorAll('nav.fms-menu,.fms-menu nav').forEach(function(n){n.setAttribute('aria-label','Principale')});"
                  "document.querySelectorAll('.fms-marchio a').forEach(function(a){a.setAttribute('aria-label','F.M. Sistemi, inizio')});"
                  # Ultimate Addons mette testata e piede dentro il proprio <header> e <footer>: un punto di riferimento solo
                  "document.querySelectorAll('.fms-testa,.fms-piede').forEach(function(e){"
                  "if(e.parentElement&&e.parentElement.closest('header,footer'))e.setAttribute('role','none')})})</script>",
                  css=css_variabili() + CSS_SITO + css_base('fms-testa') + CSS_TESTATA)
    stile_el = RAW('', css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    # i widget HTML stanno fuori dalla riga (posizione assoluta, misura zero): non aggiungono spazio tra le voci.
    # Vengono per primi: "Salta ai lavori" è la prima fermata del tasto Tab, come nella statica
    fuori = C(globali, stile_el, boxed=False, css='fms-fuori')
    return C(fuori, marchio, nav, dir='row', align='center', gap=40, boxed=False, pad=0, tag='header',
             css='fms-testa fms-sito')


# =============================================================================================
# PIEDE (template "FM Sistemi: Footer")
# =============================================================================================
CSS_PIEDE = (
    '.fms-piede{' + BLOCCO + 'margin-top:var(--fm-passo)!important;background:var(--fm-pietra)!important;border:0!important;'
    'padding:48px 0 56px!important;font-size:14px;line-height:1.6;color:var(--fm-testo-2)}'
    '.fms-piede .fms-griglia{align-items:start!important}'
    '.fms-piede p{font-size:14px;line-height:1.6;color:var(--fm-testo-2)}'
    '.fms-piede-logo{grid-column:1/span 3}'
    '.fms-piede-logo img{width:150px!important;max-width:100%!important}'
    '.fms-dati{grid-column:5/span 5}'
    '.fms-link{grid-column:10/span 3}'
    '.fms-link p{text-align:right!important}'
    '.fms-link a{color:var(--fm-testo-2)!important}'
    '.fms-link a:hover{color:var(--fm-rame-testo)!important}'
    '@media (max-width:860px){.fms-dati{grid-column:1/span 12;margin-top:24px!important}'
    '.fms-link{grid-column:1/span 12;margin-top:12px!important}.fms-link p{text-align:left!important}}'
    '@media (max-width:600px){.fms-piede-logo{grid-column:1/span 12}}'
)


def footer():
    logo = I(img('logo.png'), 'FM Sistemi', css='fms-piede-logo')
    dati = T('<p class="num">F.M. Sistemi S.r.l., via del Lavoro 37, 30030 Vigonovo (VE)<br>'
             'Partita IVA e codice fiscale 03807720283<br>'
             f'PEC fmsistemisrl@legalmail.it, telefono +39{NBSP}049{NBSP}8305354</p>',
             style='piede', color=TESTO2, css='fms-dati')
    link = T(f'<p><a href="{FACEBOOK}">Facebook</a></p>', style='piede', color=TESTO2, link_color=TESTO2,
             link_hover=RAME_TESTO, css='fms-link')
    griglia = C(logo, dati, link, boxed=False, css='fms-griglia')
    return C(griglia, RAW('', css=css_variabili() + CSS_SITO + css_base('fms-piede') + CSS_COMUNE + CSS_PIEDE),
             boxed=False, pad=0, tag='footer', css='fms-piede fms-sito')


# =============================================================================================
# HOME
# =============================================================================================
# Apertura. Il raccordo a T in rame attraversa lo schermo; il titolo poggia sulla barra; il gambo scende,
# sfuma nella calce e diventa la T accesa dell'alfabeto. Geometria della statica: la foto è larga 100cqw + 80px;
# il gambo sta al 79,207 % della sua larghezza, l'asse della barra al 33,537 % della larghezza dal bordo alto,
# mezzo spessore della barra = 5,122 % della larghezza.
CSS_APERTURA = (
    '.fms-apertura{position:relative!important;container-type:inline-size;--fm-h:clamp(720px,100vh,980px);--fm-striscia:112px;'
    'height:var(--fm-h)!important;' + BLOCCO + 'width:100%!important;gap:0!important;overflow:visible!important}'
    '.fms-apertura>*{--fm-k:calc(100cqw + 80px);--fm-mezza:calc(var(--fm-k) * .05122);--fm-barra:calc(var(--fm-h) * .5);'
    '--fm-base:calc(var(--fm-barra) - var(--fm-mezza) - 40px);'
    '--fm-asse:calc(var(--fm-margine) + (100cqw - 2 * var(--fm-margine)) * 17.5 / 21);'
    '--fm-fs:clamp(64px,calc((100cqw - 2 * var(--fm-margine) - 430px) / 5.32),160px);'
    '--fm-col:min(440px,calc(100cqw - 2 * var(--fm-margine) - 5.32 * var(--fm-fs) - 40px))}'
    # la tavola: contenitore con il widget HTML del <picture>; il widget non fa da riferimento alla foto
    '.fms-tavola{position:absolute!important;inset:0 0 var(--fm-striscia) 0!important;' + BLOCCO + 'height:auto!important;'
    'overflow:hidden!important;z-index:auto!important;'
    '-webkit-mask-image:linear-gradient(to bottom,#000 calc(100% - 56px),transparent);mask-image:linear-gradient(to bottom,#000 calc(100% - 56px),transparent)}'
    '.fms-tavola>*,.fms-tavola .elementor-widget-container,.fms-tavola picture{position:static!important;margin:0!important}'
    '.fms-tavola img{position:absolute!important;max-width:none!important;width:var(--fm-k)!important;height:auto!important;'
    'left:calc(var(--fm-asse) - var(--fm-k) * .79207);top:calc(var(--fm-barra) - var(--fm-k) * .33537)}'
    # il titolo
    '.fms-h1{position:absolute!important;inset:0!important;z-index:2!important;margin:0!important;pointer-events:none;'
    'width:auto!important;max-width:none!important}'
    '.fms-h1 .elementor-widget-container{position:static}'
    # in Elementor l'h1 sta dentro il widget .fms-h1; nel fallback è il widget stesso e resta in posizione assoluta
    '.fms-h1 h1{margin:0!important;position:static!important;text-wrap:wrap!important}'
    '.fms-apertura h1.fms-h1{margin:0!important;text-wrap:wrap!important}'
    '.fms-apertura .h1-grande{position:absolute;left:var(--fm-margine);top:calc(var(--fm-base) - .825em);margin-left:-.045em;'
    'font:400 var(--fm-fs)/.9 var(--fm-display);letter-spacing:-.045em;white-space:nowrap;color:var(--fm-testo)}'
    '.fms-apertura .h1-grande .z{letter-spacing:0}'
    # la riga cresce verso l'alto dal bottone: il bordo basso del bottone resta sulla linea di base del titolo
    '.fms-h1-riga{position:absolute!important;right:var(--fm-margine);width:var(--fm-col)!important;max-width:none!important;'
    'bottom:calc(var(--fm-h) - var(--fm-base) + 44px + 22px);margin:0!important;z-index:2!important;'
    'font-size:17px!important;line-height:1.35!important;color:var(--fm-testo)}'
    '.fms-h1-riga p{text-wrap:pretty}'
    '.fms-h1-riga .conta{color:var(--fm-rame-testo)}'
    '.fms-azione{position:absolute!important;right:var(--fm-margine);width:var(--fm-col)!important;max-width:none!important;'
    'bottom:calc(var(--fm-h) - var(--fm-base));display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;'
    'align-items:baseline!important;justify-content:flex-start!important;gap:0!important;padding:0!important;margin:0!important;'
    'min-height:0!important;z-index:2!important}'
    '.fms-azione>*{flex:0 0 auto!important;width:auto!important;max-width:none!important;margin:0!important}'
    f'{bt(".fms-bottone")}{{display:inline-block!important;background:var(--fm-rame)!important;color:var(--fm-nero-rame)!important;'
    'text-decoration:none!important;font:500 17px/1 var(--fm-sans)!important;letter-spacing:0!important;text-transform:none!important;'
    'padding:13.5px 22px!important;border:0!important;border-radius:0!important;box-shadow:none!important;min-height:0!important;'
    'transition:background-color .12s!important;font-variant-numeric:tabular-nums lining-nums;text-align:left!important}'
    f'{bt(".fms-bottone")}:hover{{background:var(--fm-testo)!important;color:var(--fm-fondo)!important}}'
    # il fuoco del bottone come nella statica (il fallback del motore lo farebbe di 3 px color rame)
    f'{bt(".fms-bottone")}:focus-visible{{outline:2px solid var(--fm-blu)!important;outline-offset:3px!important}}'
    '.fms-bottone .elementor-button-content-wrapper,.fms-bottone .elementor-button-text{display:inline!important}'
    '.fms-bottone .elementor-button-wrapper{display:block}'
    '.fms-scrivi a{margin-left:18px;font-size:16px;white-space:nowrap}'
    # la voce della T sotto la barra
    '.fms-didascalia{position:absolute!important;left:0;bottom:var(--fm-striscia);width:calc(var(--fm-margine) + 400px)!important;'
    'max-width:none!important;padding:28px 36px 30px var(--fm-margine)!important;background:none!important;'
    'margin:0!important;z-index:2!important}'
    '.fms-didascalia .voce{display:block;font:400 30px/1.05 var(--fm-display);letter-spacing:-.02em;margin-bottom:10px}'
    '.fms-didascalia .voce b{font-weight:400;color:var(--fm-rame-testo);margin-right:.3em}'
    '.fms-didascalia .cosa{display:block;font-size:17px;line-height:1.45;color:var(--fm-testo);text-wrap:pretty}'
    # l'alfabeto: ventuno lettere, accese solo quelle che hanno un lavoro
    '.fms-alfa{position:absolute!important;left:0;right:0;bottom:0;height:var(--fm-striscia)!important;' + BLOCCO +
    'padding:0 var(--fm-margine)!important;z-index:2!important}'
    '.fms-alfa>*,.fms-alfa .elementor-widget-container{height:100%;margin:0!important}'
    '.fms-alfabeto{display:grid;grid-template-columns:repeat(21,1fr);height:100%;margin:0;padding:0}'
    '.fms-alfabeto>span,.fms-alfabeto a{display:flex;justify-content:center;align-items:flex-start;padding:22px 0 0;margin:0;'
    'font:400 46px/1 var(--fm-display);letter-spacing:0;color:var(--fm-spento);text-decoration:none!important}'
    '.fms-alfabeto a{color:var(--fm-testo);transition:color .12s;-webkit-tap-highlight-color:transparent}'
    '.fms-alfabeto .l{position:relative;display:block}'
    '.fms-alfabeto .l::before{content:"";position:absolute;left:50%;top:-22px;width:24px;margin-left:-12px;height:3px;'
    'background:transparent;transition:background-color .12s}'
    '.fms-alfabeto a:hover{color:var(--fm-rame-testo)}'
    '.fms-alfabeto a.qui{color:var(--fm-rame-testo)}'
    '.fms-alfabeto a.qui .l::before{background:var(--fm-rame)}'
    '.fms-alfabeto .nome{position:absolute;left:0;top:calc(100% + 9px);font:400 13px/1 var(--fm-sans);color:var(--fm-testo-2);white-space:nowrap}'
    # da 601 a 1100: in colonna; riga e bottone subito sotto la foto, poi l'alfabeto
    '@media (max-width:1100px){'
    '.fms-apertura{height:auto!important;display:flex!important;flex-direction:column!important;flex-wrap:nowrap!important;'
    'align-items:stretch!important;justify-content:flex-start!important;--fm-striscia:0px}'
    '.fms-apertura>*{--fm-fs:clamp(64px,14cqw,150px);--fm-base:calc(118px + .9 * var(--fm-fs));'
    '--fm-barra:calc(var(--fm-base) + 40px + var(--fm-mezza))}'
    '.fms-tavola{position:relative!important;inset:auto!important;height:calc(var(--fm-barra) + var(--fm-mezza) + 40px)!important;'
    'order:1!important;flex:0 0 auto!important;width:auto!important}'
    '.fms-h1{position:static!important;order:2!important;pointer-events:auto}'
    '.fms-h1-riga{position:static!important;display:block!important;width:auto!important;max-width:36em!important;'
    'padding:20px var(--fm-margine) 0!important;font-size:18px!important;line-height:1.4!important;order:2!important}'
    '.fms-azione{position:static!important;width:auto!important;padding:20px var(--fm-margine) 0!important;order:3!important}'
    '.fms-alfa{position:static!important;height:auto!important;order:4!important;padding-top:28px!important}'
    '.fms-alfabeto>span,.fms-alfabeto a{font-size:30px;padding:16px 0 12px;min-height:58px}'
    '.fms-alfabeto .l::before{top:-16px}'
    '.fms-alfabeto .nome{display:none}'
    '.fms-didascalia{position:static!important;width:auto!important;order:5!important;padding:16px var(--fm-margine) 0!important;'
    'background:none!important}'
    '.fms-didascalia .voce{display:inline;font-size:26px;margin:0 .45em 0 0}'
    '.fms-didascalia .cosa{display:inline;font-size:17px}}'
    # telefono
    '@media (max-width:600px){'
    '.fms-tavola{height:auto!important;aspect-ratio:390 / 550}'
    '.fms-tavola img{left:0!important;top:0!important;width:100%!important;height:100%!important;object-fit:cover}'
    '.fms-apertura .h1-grande{top:calc(64.1cqw - 22px - 1.725em);font-size:clamp(52px,21cqw,88px);white-space:normal;margin-left:-.04em}'
    '.fms-apertura .h1-grande .a-capo{display:block}'
    '.fms-h1-riga{padding-top:4px!important;font-size:17px!important;line-height:1.38!important}'
    '.fms-azione{padding-top:16px!important}'
    '.fms-scrivi a{margin-left:14px}'
    '.fms-alfa{padding-top:24px!important}'
    '.fms-didascalia{padding-top:14px!important}'
    '.fms-didascalia .voce{display:block;font-size:26px;margin:0 0 4px}'
    '.fms-didascalia .cosa{display:block;font-size:16px}'
    '.fms-alfabeto{grid-template-columns:repeat(7,1fr)}'
    '.fms-alfabeto>span,.fms-alfabeto a{font-size:28px;padding:10px 0 0;min-height:48px;height:48px}'
    '.fms-alfabeto .l::before{top:auto;bottom:-7px}}'
    '@media (max-width:360px){.fms-azione{flex-wrap:wrap!important}.fms-scrivi a{display:inline-block;margin:14px 0 0}}'
)


def _alfabeto():
    voci = []
    for l in ALFABETO:
        if l in ACCESE:
            qui = ' class="qui"' if l == 'T' else ''
            voci.append(f'<a href="#lavoro-{l.lower()}"{qui}><span class="l">{l}<span class="nome">{ACCESE[l]}</span></span></a>')
        else:
            voci.append(f'<span aria-hidden="true">{l}</span>')
    return f'<nav class="fms-alfabeto" aria-label="I nostri lavori, dalla A alla Z">{"".join(voci)}</nav>'


def apertura():
    h1 = H('<span class="h1-grande">Dalla A <span class="a-capo">alla <span class="z">Z</span></span></span>',
           level='h1', style='h1', color=TESTO, css='fms-h1')
    riga = T('<p><span class="conta">Otto mestieri su ventuno lettere:</span> impianti elettrici e termoidraulici, clima, '
             'pompe di calore Viessmann, fotovoltaico e ristrutturazioni. Una squadra di <span class="num">17</span> '
             'persone a&nbsp;Vigonovo, un numero solo.</p>', style='riga', color=TESTO, css='fms-h1-riga')
    picture = (
        '<picture><source media="(max-width:600px)" '
        f'srcset="{img("tavola-t-m-780.jpg")} 780w, {img("tavola-t-m-1170.jpg")} 1170w" sizes="100vw">'
        f'<img src="{img("tavola-t-2000.jpg")}" srcset="{img("tavola-t-1600.jpg")} 1600w, {img("tavola-t-2000.jpg")} 2000w, '
        f'{img("tavola-t-2560.jpg")} 2560w" sizes="calc(100vw + 80px)" width="2000" height="1761" '
        'alt="Raccordo a T in rame su fondo chiaro, ruotato fino a disegnare una T maiuscola"></picture>')
    # i caratteri: le @font-face sono nel foglio di stile di ogni sezione (css_variabili), anche senza la testata globale
    tavola = C(RAW(picture), boxed=False, tag='figure', css='fms-tavola')
    didascalia = T('<p><span class="voce"><b>T</b>Termoidraulica</span> '
                   '<span class="cosa">Riscaldamento e acqua calda sanitaria: tubi, raccordi e collettori.</span></p>',
                   style='body', color=TESTO, css='fms-didascalia')
    alfa = C(RAW(_alfabeto(), css=css_variabili() + CSS_SITO + css_base('fms-apertura') + CSS_APERTURA),
             boxed=False, css='fms-alfa')
    azione = C(B(f'Telefonate allo 049{NBSP}8305354', TEL_LINK, variant='rame', css='fms-bottone'),
               T(f'<p><a class="scrivi" href="{MAIL_SOPRALLUOGO}">o scrivete</a></p>', style='body', color=TESTO,
                 link_color=TESTO, link_hover=RAME_TESTO, css='fms-scrivi'),
               dir='row', align='baseline', boxed=False, css='fms-azione')
    return C(h1, riga, tavola, didascalia, alfa, azione, boxed=False, pad=0, tag='section', css='fms-apertura fms-sito')


# Una casa dalla A alla Z: i mestieri nell'ordine del cantiere, una striscia di materiale per riga
CSS_LAVORI = (
    '.fms-lavori-h2{grid-column:1/span 8}'
    '.fms-intro{grid-column:1/span 6;margin:28px 0 0!important}'
    '.fms-intro p{font-size:20px;line-height:1.55;text-wrap:pretty}'
    '.fms-cantiere{' + BLOCCO + 'margin:88px 0 0!important;border-bottom:1px solid var(--fm-filetto)!important}'
    '.fms-riga{display:grid!important;grid-template-columns:repeat(12,1fr);column-gap:var(--fm-gola)!important;row-gap:0!important;'
    'padding:0 var(--fm-margine)!important;margin:0!important;border-top:1px solid var(--fm-filetto)!important;scroll-margin-top:32px;'
    'width:auto!important;max-width:none!important;min-height:0!important}'
    '.fms-riga>*{width:auto!important;max-width:none!important;min-width:0}'
    '.fms-idx{grid-column:1;grid-row:1;padding-top:30px!important;font-size:14px!important;line-height:1!important;color:var(--fm-testo-2)}'
    '.fms-cap-l{grid-column:2/span 2;grid-row:1;position:relative!important;align-self:start;margin-top:26px!important;'
    'font:400 152px/.74 var(--fm-display)!important;letter-spacing:-.02em!important;color:var(--fm-rame-testo)}'
    '.fms-cap-l::after{content:"";position:absolute;left:4px;bottom:-22px;width:32px;height:3px;background:transparent}'
    '.fms-riga:target .fms-cap-l::after{background:var(--fm-rame)}'
    '.fms-t{grid-column:4/span 3;grid-row:1;' + BLOCCO.replace('padding:0!important;', '') + 'padding:26px 0 24px!important}'
    f'{ht(".fms-h3")}{{font:400 28px/1.05 var(--fm-display)!important;letter-spacing:-.02em!important}}'
    '.fms-t .fms-h3{margin:0 0 12px!important}'
    '.fms-t p{font-size:17px;line-height:1.45;text-wrap:pretty}'
    '.fms-t .fms-nella{margin-top:12px!important}'
    '.fms-t .fms-nella p{font-size:13px;color:var(--fm-testo-2)}'
    '.fms-striscia{grid-column:7/span 6;grid-row:1;' + BLOCCO + 'margin-right:calc(-1 * var(--fm-margine))!important}'
    '.fms-striscia img{width:100%!important;aspect-ratio:3.5;object-fit:cover;height:auto!important}'
    '@media (max-width:1100px){'
    '.fms-riga{grid-template-columns:40px 112px minmax(0,1fr)}'
    '.fms-idx{grid-column:1;padding-top:30px!important}'
    '.fms-cap-l{grid-column:2;font-size:112px!important;margin:28px 0 30px!important}'
    '.fms-t{grid-column:3;padding:28px 0 28px!important;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1fr);'
    'column-gap:var(--fm-gola)!important;row-gap:0!important;align-items:baseline!important}'
    f'{ht(".fms-h3")}{{font-size:24px!important}}'
    '.fms-t .fms-h3{margin:0!important}'
    '.fms-t .fms-nella{grid-column:2}'
    '.fms-striscia{grid-column:1/-1;grid-row:2;margin:0 calc(-1 * var(--fm-margine))!important}}'
    '@media (max-width:600px){'
    '.fms-intro p{font-size:18px}'
    '.fms-lavori-h2,.fms-intro{grid-column:1/span 12}'
    '.fms-cantiere{margin-top:56px!important}'
    '.fms-riga{grid-template-columns:24px 72px minmax(0,1fr);column-gap:12px!important}'
    '.fms-cap-l{font-size:80px!important;margin:22px 0 24px!important}'
    '.fms-cap-l::after{bottom:-14px}'
    '.fms-idx{padding-top:22px!important;font-size:13px!important}'
    '.fms-t{display:block!important;padding:20px 0 22px!important}'
    f'{ht(".fms-h3")}{{font-size:24px!important}}'
    '.fms-t .fms-h3{margin:0 0 8px!important}'
    '.fms-t p{font-size:16px}'
    '.fms-t .fms-nella p{font-size:13px}'
    '.fms-striscia img{aspect-ratio:2.6}}'
)


def _riga(i, lettera, nome, testo, nella, alt):
    return C(
        T(f'<p class="num">{i:02d}</p>', style='idx', color=TESTO2, css='fms-idx'),
        T(f'<p aria-hidden="true">{lettera.upper()}</p>', style='cap', color=RAME_TESTO, css='fms-cap-l'),
        C(H(nome, level='h3', style='h3', color=TESTO, css='fms-h3'),
          T(f'<p>{dritto(testo)}</p>', style='t17', color=TESTO, css='fms-cosa'),
          T(f'<p>{nella}</p>', style='nella', color=TESTO2, css='fms-nella'),
          boxed=False, css='fms-t'),
        C(I(img(f'lavoro-{lettera}-1440.jpg'), alt, css='fms-d'), I(img(f'lavoro-{lettera}-m-1170.jpg'), alt, css='fms-m'),
          boxed=False, css='fms-striscia'),
        boxed=False, anchor=f'lavoro-{lettera}', css='fms-riga')


def lavori():
    testa = C(
        H('Una casa dalla A alla Z', level='h2', style='h2', color=TESTO, css='fms-h2 fms-lavori-h2'),
        T(dritto("<p>Chi rifà casa di solito chiama tre ditte: il muratore, l'idraulico, l'elettricista. Qui il cantiere ha un "
                 "numero solo, e i mestieri arrivano nell'ordine in cui servono.</p>"), style='intro', color=TESTO, css='fms-intro'),
        boxed=False, css='fms-griglia')
    cantiere = C(*[_riga(i, *ms) for i, ms in enumerate(MESTIERI, 1)], boxed=False, css='fms-cantiere')
    return C(testa, cantiere,
             RAW('', css=css_variabili() + CSS_SITO + css_base('fms-lavori') + CSS_COMUNE + CSS_LAVORI),
             boxed=False, pad=0, anchor='lavori', tag='section', css='fms-sezione fms-lavori fms-sito')


# Chi siamo: la foto tecnica, il 17 e la scheda
CSS_CHI = (
    '.fms-nascosto{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;'
    'clip-path:inset(50%);white-space:nowrap;margin:0!important;padding:0!important}'
    '.fms-foto{' + BLOCCO + '}'
    '.fms-foto img{width:100%!important;aspect-ratio:2;object-fit:cover;height:auto!important}'
    '.fms-figcaption{padding:14px var(--fm-margine) 0!important}'
    '.fms-figcaption p{font-size:14px;color:var(--fm-testo-2);text-align:right}'
    '.fms-chi-griglia{margin-top:96px!important;align-items:start!important}'
    '.fms-cifra{grid-column:1/span 4}'
    '.fms-cifra b{display:block;font:400 clamp(120px,15vw,216px)/.8 var(--fm-display);letter-spacing:-.05em}'
    '.fms-cifra p>span{display:block;margin-top:24px;font-size:17px;color:var(--fm-testo-2)}'
    '.fms-scheda{grid-column:6/span 7;' + BLOCCO + '}'
    '.fms-dl{' + BLOCCO + 'border-top:1px solid var(--fm-filetto)!important}'
    '.fms-dl-riga{display:grid!important;grid-template-columns:9em 1fr;gap:var(--fm-gola)!important;padding:18px 0!important;'
    'border-bottom:1px solid var(--fm-filetto)!important;margin:0!important;width:auto!important;max-width:none!important;min-height:0!important}'
    '.fms-dl-riga>*{width:auto!important;max-width:none!important;min-width:0}'
    '.fms-dt p{color:var(--fm-testo-2);font-size:16px;line-height:1.5}'
    '.fms-dd p{font-size:18px;line-height:1.5}'
    '.fms-scheda-p p{margin:28px 0 0!important;max-width:36em;text-wrap:pretty}'
    '@media (max-width:1100px){.fms-scheda{grid-column:5/span 8}.fms-cifra{grid-column:1/span 4}}'
    '@media (max-width:860px){.fms-cifra{grid-column:1/span 12}.fms-scheda{grid-column:1/span 12;margin-top:48px!important}}'
    '@media (max-width:600px){'
    '.fms-foto img{aspect-ratio:.8}'
    '.fms-figcaption p{text-align:left}'
    '.fms-chi-griglia{margin-top:56px!important}'
    '.fms-dl-riga{grid-template-columns:1fr;gap:4px!important;padding:16px 0!important}}'
)


def chi():
    alt = 'Collettore del riscaldamento a pavimento con i flussimetri e i tubi dei circuiti'
    foto = C(I(img('collettore-1920.jpg'), alt, css='fms-d'), I(img('collettore-m-1170.jpg'), alt, css='fms-m'),
             T('<p>Collettore del riscaldamento a pavimento, otto circuiti.</p>', style='fig', color=TESTO2,
               css='fms-figcaption'),
             boxed=False, tag='figure', css='fms-foto')
    cifra = T('<p><b class="num">17</b><span>persone nella squadra, nel <span class="num">2025</span></span></p>',
              style='body', color=TESTO, css='fms-cifra')
    voci = [('Mestieri', '<span class="num">8</span>, con un solo numero da chiamare'),
            ('Partner', 'Viessmann, per pompe di calore e sistemi ibridi'),
            ('Sede', 'Via del Lavoro <span class="num">37</span>, zona artigianale, Vigonovo')]
    dl = C(*[C(T(f'<p>{k}</p>', style='dt', color=TESTO2, css='fms-dt'), T(f'<p>{v}</p>', style='dd', color=TESTO, css='fms-dd'),
               dir='row', boxed=False, css='fms-dl-riga') for k, v in voci],
           boxed=False, css='fms-dl')
    scheda = C(dl, T('<p>Lavoriamo per privati, aziende ed enti pubblici. Con Viessmann installiamo anche gli impianti '
                     f'commerciali: <a href="{VIESSMANN}">la nostra pagina di partner</a>.</p>', style='body', color=TESTO,
                     link_color=TESTO, link_hover=RAME_TESTO, css='fms-scheda-p'),
               boxed=False, css='fms-scheda')
    griglia = C(cifra, scheda, boxed=False, css='fms-griglia fms-chi-griglia')
    return C(H('Chi siamo', level='h2', style='h2', color=TESTO, css='fms-nascosto'), foto, griglia,
             RAW('', css=css_variabili() + CSS_SITO + css_base('fms-chi') + CSS_COMUNE + CSS_CHI),
             boxed=False, pad=0, anchor='chi', tag='section', css='fms-sezione fms-chi fms-sito')


# La parete d'inverno: il momento caldo, la foto del risultato
CSS_INVERNO = (
    '.fms-inverno{position:relative!important;' + BLOCCO + 'margin:var(--fm-passo) 0 0!important}'
    '.fms-inverno img{width:100%!important;aspect-ratio:2;object-fit:cover;height:auto!important;'
    '-webkit-mask-image:linear-gradient(to bottom,#000 30%,transparent 86%);mask-image:linear-gradient(to bottom,#000 30%,transparent 86%)}'
    '.fms-blockquote{position:absolute!important;left:0;right:0;bottom:0;margin:0!important}'
    '.fms-frase{grid-column:1/span 8}'
    '.fms-frase p{font:400 clamp(32px,3.9vw,56px)/1.08 var(--fm-display);letter-spacing:-.03em;color:var(--fm-testo);text-wrap:balance}'
    '@media (max-width:1100px){.fms-frase{grid-column:1/span 10}}'
    '@media (max-width:600px){.fms-inverno img{aspect-ratio:.66}.fms-frase{grid-column:1/span 12}}'
)


def inverno():
    alt = 'Luce calda del pomeriggio che passa da una tapparella e disegna righe su un angolo di parete'
    frase = T('<blockquote><p>Il lavoro migliore è quello che a cantiere chiuso non si vede più. In casa resta la temperatura '
              'giusta.</p></blockquote>', style='frase', color=TESTO, css='fms-frase')
    return C(I(img('inverno-1920.jpg'), alt, css='fms-d'), I(img('inverno-m-1170.jpg'), alt, css='fms-m'),
             C(frase, boxed=False, css='fms-griglia fms-blockquote'),
             RAW('', css=css_variabili() + CSS_SITO + css_base('fms-inverno') + CSS_COMUNE + CSS_INVERNO),
             boxed=False, pad=0, tag='figure', css='fms-inverno fms-sito')


# Contatti
CSS_CONTATTI = (
    '.fms-contatti-h2{grid-column:1/span 9}'
    '.fms-tel-grande{grid-column:1/span 12;margin:56px 0 0!important}'
    '.fms-tel-grande p{font:400 clamp(44px,6.4vw,92px)/1 var(--fm-display);letter-spacing:-.035em}'
    '.fms-tel-grande a{text-decoration:none!important}'
    '.fms-col{grid-column:span 4;' + BLOCCO + 'margin-top:56px!important}'
    f'{ht(".fms-col-h")}{{font:500 15px/1.3 var(--fm-sans)!important;color:var(--fm-testo-2)}}'
    '.fms-col .fms-col-h{margin:0 0 10px!important}'
    '.fms-col p{font-size:17px;margin:0 0 6px!important}'
    '@media (max-width:860px){.fms-col{grid-column:span 6}}'
    '@media (max-width:600px){.fms-contatti-h2{grid-column:1/span 12}.fms-col{grid-column:1/span 12;margin-top:36px!important}}'
)

# come nella statica, le sezioni dall'apertura ai contatti stanno in <main> (punto di riferimento per i lettori di schermo):
# Elementor gratuito non ha un contenitore che le raccolga, lo fa questo script quando la pagina arriva ai contatti.
# Lo stesso script dà i nomi dei punti di riferimento della statica (Elementor gratuito non dà attributi ai contenitori):
# "Apertura", le sezioni con il testo del loro titolo, i contenitori figura (in Elementor sono <div>) con il ruolo
# "figure", "La casa a cantiere chiuso" alla parete d'inverno, la didascalia come nome della foto del collettore,
# l'elenco dei mestieri (ruoli list e listitem) e la scheda (ruoli term e definition)
PRINCIPALE = ("<script>(function(){var q=function(s){return document.querySelector(s)},"
              "a=q('.fms-apertura'),z=document.getElementById('contatti'),v=q('.fms-inverno.fms-sito'),o=q('.fms-foto'),"
              "t=q('.fms-tavola');if(a)a.setAttribute('aria-label','Apertura');"
              # le sezioni con il nome del loro titolo, come gli aria-labelledby della statica
              "['lavori','chi','contatti'].forEach(function(i){var s=document.getElementById(i),h=s&&s.querySelector('h2');"
              "if(h)s.setAttribute('aria-label',h.textContent.trim())});"
              # in Elementor i contenitori "figure" escono come <div>: il ruolo e il nome della statica
              "[t,o,v].forEach(function(e){if(e&&e.tagName!=='FIGURE')e.setAttribute('role','figure')});"
              "if(v)v.setAttribute('aria-label','La casa a cantiere chiuso');"
              "var c=o&&o.querySelector('.fms-figcaption p');if(c&&!o.querySelector('figcaption')){c.id='fms-didascalia-foto';"
              "o.setAttribute('aria-labelledby',c.id)}"
              # l'elenco dei mestieri e la scheda: nella statica <ol> e <dl>, qui contenitori e widget Testo
              "var k=q('.fms-cantiere');if(k){k.setAttribute('role','list');[].forEach.call(k.querySelectorAll('.fms-riga'),"
              "function(r){r.setAttribute('role','listitem')})}"
              "[].forEach.call(document.querySelectorAll('.fms-dt p'),function(e){e.setAttribute('role','term')});"
              "[].forEach.call(document.querySelectorAll('.fms-dd p'),function(e){e.setAttribute('role','definition')});"
              "if(!a||!z||a.closest('main'))return;while(a.parentNode&&!a.parentNode.contains(z))a=a.parentNode;"
              "while(z.parentNode!==a.parentNode)z=z.parentNode;var m=document.createElement('main');a.parentNode.insertBefore(m,a);"
              "while(m.nextSibling){var x=m.nextSibling;m.appendChild(x);if(x===z)break}})();</script>")


def contatti():
    def colonna(titolo, html):
        return C(H(titolo, level='h3', style='h3col', color=TESTO2, css='fms-col-h'),
                 T(html, style='col', color=TESTO, link_color=TESTO, link_hover=RAME_TESTO, css='fms-col-p'),
                 boxed=False, css='fms-col')
    griglia = C(
        H('In via del Lavoro 37, nella zona artigianale di Vigonovo', level='h2', style='h2', color=TESTO,
          css='fms-h2 fms-contatti-h2'),
        T(f'<p class="num"><a href="{TEL_LINK}">{TEL}</a></p>', style='telg', color=TESTO, link_color=TESTO,
          link_hover=RAME_TESTO, sottolinea=False, css='fms-tel-grande'),
        colonna('Orari', '<p class="num">Dal lunedì al sabato, <span class="nowrap">8.30-19.00</span></p><p>Domenica chiuso</p>'),
        colonna('Scrivere', '<p><a href="mailto:info@fmsistemisrl.it">info@fmsistemisrl.it</a></p>'
                f'<p><a href="{MAIL_PREVENTIVO}">commerciale@fmsistemisrl.it</a>, per preventivi e sopralluoghi</p>'),
        colonna('Venire', '<p class="num">Via del Lavoro 37, 30030 Vigonovo (VE)</p>'
                f'<p><a href="{MAPS}">Apri in Google Maps</a></p>'),
        boxed=False, css='fms-griglia')
    return C(griglia, RAW(PRINCIPALE, css=css_variabili() + CSS_SITO + css_base('fms-contatti') + CSS_COMUNE + CSS_CONTATTI),
             boxed=False, pad=0, anchor='contatti', tag='section', css='fms-sezione fms-contatti fms-sito')


def home():
    return [('apertura', apertura()), ('lavori', lavori()), ('chi-siamo', chi()), ('inverno', inverno()),
            ('contatti', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'F.M. Sistemi, impianti dalla A alla Z a Vigonovo',
     'descrizione': 'Impianti elettrici e termoidraulici, clima, pompe di calore, fotovoltaico, mobilità elettrica e '
                    'ristrutturazioni edili. F.M. Sistemi, via del Lavoro 37, Vigonovo (VE). Telefono 049 8305354.'},
]
