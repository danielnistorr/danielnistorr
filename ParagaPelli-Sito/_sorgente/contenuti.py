# -*- coding: utf-8 -*-
"""
Contenuti della home di Paraga Pelli per WordPress + Elementor: la home statica approvata ("La mazzetta",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: testata (nome, menu di Ultimate Addons, telefono, lingue),
  titoli, testi, bottoni, foto (drappo, magazzino, squadra, box-campionario), tabella LWG, recapiti, piede.
- Widget HTML (nodo RAW del motore) solo per le parti che Elementor gratuito non fa: nome e codice del colore,
  cartellino, mazzetta, dorsi dei 27 articoli, nomi degli usi che aprono le cartelle, filo della pelle sotto il
  magazzino, fila dei dorsi nel piede. Lo script è quello della pagina statica (_sorgente/mazzetta.js), senza librerie.
- L'impaginazione (griglia a 12 colonne, misure fluide con clamp, colore del campione scelto) è il foglio di stile
  della pagina statica, con le classi ppl-, dentro i nodi RAW: vale uguale per il template Elementor e per il fallback.

Testi e dati: tutti dalla home statica (verificati in 01-analisi.md). Nessun dato nuovo.
"""
import json
import os

import motore as m
from motore import C, H, T, B, I, RAW, MENU

QUI = os.path.dirname(os.path.abspath(__file__))

PREFISSO = 'ppl'
NOME_SITO = 'Paraga Pelli'

# ---------------------------------------------------------------------------------------------
# Tema: i colori e i caratteri della home statica
# ---------------------------------------------------------------------------------------------
CARTA = '#ECEBE7'          # fondo della pagina
CARTONCINO = '#F7F6F2'     # cartellino e box
INCHIOSTRO = '#1A1817'
GRIGIO = '#5E5A56'         # testo secondario
FILETTO = 'rgba(26,24,23,.18)'
CHIARO = '#F6F3EE'         # testo chiaro sopra il colore scelto
PIEDE_TESTO = '#D9D5CF'
PIEDE_CHIARO = '#F4F1EC'
PIEDE_GRIGIO = '#A9A39B'
# colore del campione scelto: lo cambia lo script della mazzetta (variabili CSS su <html>)
TONO = 'var(--tono)'
BASE_TONO = 'var(--base)'
SU_TONO = 'var(--su-tono)'
SU_TONO_2 = 'var(--su-tono-2)'

NOME = 'Libre Caslon Display'      # nomi delle linee
TESTO = 'Mona Sans'                # tutto il resto
# Libre Caslon Display è nell'elenco Google di Elementor; Mona Sans no (e serve con l'asse della larghezza):
# i due caratteri si caricano da Google Fonts con l'API css2 (gli stessi file woff2 della pagina statica),
# oppure dal sito stesso con build.py --caratteri-locali (vedi caratteri_html).
GOOGLE_FONTS = 'https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Mona+Sans:wdth,wght@75..125,200..900&display=swap'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# misure (1440, 1024, 390): quelle della pagina statica a quelle larghezze; le misure fluide (clamp) sono nel foglio di stile
TEMA = {
    'nome': 'Mazzetta',
    'fondo': CARTA, 'superficie': CARTA, 'inchiostro': INCHIOSTRO, 'testo2': GRIGIO, 'accento': INCHIOSTRO,
    'filetto': FILETTO, 'filetto_scuro': 'rgba(244,241,236,.18)', 'su_scuro2': PIEDE_GRIGIO,
    'scuro': INCHIOSTRO, 'su_scuro': PIEDE_CHIARO, 'su_accento': CHIARO,
    'font_titoli': NOME, 'font_testo': TESTO, 'larghezza': 1440,
    'google_fonts': GOOGLE_FONTS,
    'stili': {
        'marchio':  _st(TESTO, '560', (19, 19, 17), 1.2, 0.19),
        'nav':      _st(TESTO, '400', (15, 15, 15), 1.2),
        'nav_m':    _st(TESTO, '400', (19, 19, 19), 1.2),
        'lingue':   _st(TESTO, '400', (13, 13, 13), 1.2),
        'h1':       _st(TESTO, '420', (29, 21, 19), 1.28, -0.23),
        'h2':       _st(TESTO, '400', (56, 40, 34), 1.04, -1.23),
        'h3':       _st(TESTO, '560', (17, 17, 17), 1.35),
        'h3nome':   _st(NOME, '400', (30, 30, 30), 1.05, -0.3),
        'attacco':  _st(TESTO, '400', (19, 17, 17), 1.58),
        'body':     _st(TESTO, '400', (17, 17, 16), 1.6),
        'luogo':    _st(TESTO, '400', (17, 17, 17), 1.55),
        'dati':     _st(TESTO, '400', (15, 15, 15), 1.55),
        'tab':      _st(TESTO, '400', (15, 15, 14), 1.4),
        'tabd':     _st(TESTO, '520', (15, 15, 14), 1.4),
        'link':     _st(TESTO, '400', (15, 15, 15), 1.6),
        'nota':     _st(TESTO, '400', (14, 14, 14), 1.5),
        'fam':      _st(TESTO, '400', (13, 13, 13), 1.35),
        'didascalia': _st(TESTO, '400', (13, 13, 13), 1.6),
        'piede':    _st(TESTO, '400', (13, 13, 13), 1.6),
        'btn':      _st(TESTO, '560', (15, 15, 15), 1.6),
    },
    'spazi': {'sezione': (136, 92, 80), 'lato': (64, 46, 17), 'm': (24, 24, 12), 's': (12, 12, 12), '0': (0, 0, 0)},
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): l'hover cambia colore pieno, mai opacità
    'bottoni': {
        # sopra il drappo: il bottone prende il colore del testo, il testo il tono; in hover inchiostro (carta sui toni chiari)
        'apertura': (BASE_TONO, SU_TONO, SU_TONO, 'var(--ppl-bht)', 'var(--ppl-bh)', 'var(--ppl-bh)'),
        # nel box-campionario: inchiostro, in hover il colore del campione scelto
        'box': (CHIARO, INCHIOSTRO, INCHIOSTRO, SU_TONO, TONO, TONO),
    },
    'bottone': {'raggio': 0, 'pad': (12, 24, 12, 24), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# Le scansioni dei campioni e i dorsi (usati dallo script della mazzetta) restano a questo indirizzo:
# per non dipendere da GitHub si caricano assets/web/ sul sito e si rigenera con build.py --base.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/ParagaPelli-Sito/assets/web/'
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
    return ('<style>'
            f'@font-face{{font-family:"Mona Sans";src:url({img("fonts/mona-sans-latin.woff2")}) format("woff2");'
            'font-weight:200 900;font-stretch:75% 125%;font-display:swap}'
            f'@font-face{{font-family:"Libre Caslon Display";src:url({img("fonts/libre-caslon-display-latin.woff2")}) format("woff2");'
            'font-weight:400;font-display:swap}'
            '</style>')


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (come nella home statica; forma giuridica e civico sono da confermare, vedi LEGGIMI)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}983{NBSP}2030'
TEL_LINK = 'tel:+390499832030'
FAX = f'049{NBSP}983{NBSP}3050'
INDIRIZZO = 'Via del Lavoro, 30030 Tombelle di Vigonovo (VE)'
PIVA = '03748440272'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Paraga+Pelli+Via+del+Lavoro+Tombelle+di+Vigonovo'
LWG = 'https://www.leatherworkinggroup.com/get-involved/our-community/certified-suppliers/paraga-pelli-srl/'
FACEBOOK = 'https://www.facebook.com/ParagaPelli'
BOX_MAIL = 'mailto:info@paragapelli.com?subject=Richiesta%20box-campionario'
EMAIL = {'info': 'info@paragapelli.com', 'ordini': 'ordini@paragapelli.com',
         'amministrazione': 'amministrazione@paragapelli.com', 'sales': 'sales@paragapelli.com'}

CATALOGO = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
ARTICOLI = CATALOGO['articoli']
N_COLORI = sum(len(a['c']) for a in ARTICOLI)          # 403

# voci del menu: in WordPress è il menu "Menu principale" (link personalizzati, li crea l'installatore);
# le ultime sei compaiono solo nel menu a scomparsa del telefono, come nella pagina statica
VOCI_MENU = [
    ('Pelle', '/#catalogo'), ('Ecopelle', '/#catalogo'), ('Tessuti', '/#catalogo'), ('Pelle auto', '/#catalogo'),
    ('Azienda', '/#azienda'), ('Contatti', '/#contatti'),
    (f'Telefono <span class="num">{TEL}</span>', TEL_LINK),
    ('IT', '#'), ('EN', '#'), ('DE', '#'), ('FR', '#'), ('PL', '#'),
]


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def bt(sel):
    """Il bottone vero (link): in Elementor .elementor-button, nel fallback l'unico <a> del widget."""
    return f'{sel} a'


# ---------------------------------------------------------------------------------------------
# Foglio di stile comune: variabili della pagina statica, caratteri, regole di base.
# Ogni sezione lo porta con sé (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
CSS_VARIABILI = (
    ':root{--carta:#ECEBE7;--cartoncino:#F7F6F2;--inchiostro:#1A1817;--grigio:#5E5A56;--filetto:rgba(26,24,23,.18);'
    '--tono:#993b1d;--base:#993b1d;--drappo-op:1;--su-tono:#F6F3EE;--su-tono-2:rgba(246,243,238,.8);'
    '--m:clamp(16px,4.45vw,64px);--g:24px;--nome:"Libre Caslon Display",Georgia,serif;--testo:"Mona Sans",system-ui,sans-serif;'
    '--t:.26s;--ppl-bh:#1A1817;--ppl-bht:#F6F3EE}'
    '.ppl-tema-chiaro{--ppl-bh:#F6F3EE;--ppl-bht:#1A1817}'
    '@media (max-width:600px){:root{--g:12px}}'
)

# regole che valgono per tutto il sito: stanno nella testata (Elementor) e nella testata del fallback
CSS_SITO = (
    'body{background:var(--carta);color:var(--inchiostro);font-family:var(--testo);font-synthesis:none;'
    '-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:hidden}'
    '.ppl-sito,.ppl-sito *{box-sizing:border-box}'
    '.ppl-sito .num,.ppl-num{font-variant-numeric:lining-nums proportional-nums}'
    # "Vai al catalogo": primo elemento della pagina, come nella statica (testo del corpo, inchiostro, sottolineato)
    '.ppl-sito a.ppl-salta,.ppl-sito a.ppl-salta:hover{position:absolute;left:-9999px;top:8px;z-index:20;background:var(--carta);'
    'color:var(--inchiostro)!important;padding:8px 12px;font:400 17px/1.6 var(--testo)!important;font-stretch:100%;white-space:nowrap;'
    'text-decoration:underline!important;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}'
    '.ppl-sito a.ppl-salta:hover{text-decoration-thickness:2px!important}'
    '.ppl-sito a.ppl-salta:focus{left:var(--m)}'
    '@media (prefers-reduced-motion:reduce){.ppl-sito *,.ppl-sito{transition:none!important;scroll-behavior:auto!important}}'
)


def css_testi(scope):
    """Regole di base dei widget nativi dentro una sezione: margini del tema e di Elementor azzerati,
    link che prendono il colore del testo (il tema Hello li colora di rosa), fuoco visibile."""
    s = f'.{scope}'
    return (
        f'{s}{{font-family:var(--testo);font-size:17px;line-height:1.6;font-weight:400;font-synthesis:none;-webkit-font-smoothing:antialiased}}'
        f'@media (max-width:600px){{{s}{{font-size:16px}}}}'
        f'{s} .elementor-widget-text-editor p,{s} .ppl-w p{{margin:0!important;text-wrap:pretty}}'
        f'{s} h1,{s} h2,{s} h3,{s} .elementor-heading-title{{margin:0;text-wrap:balance}}'
        f'{s} .elementor-widget:not(:last-child){{margin-block-end:0}}'
        f'{s} a{{color:inherit;text-decoration:underline;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}}'
        f'{s} a:hover,{s} a:focus,{s} a:active{{color:inherit}}'
        f'{s} a:hover{{text-decoration-thickness:2px!important}}'
        # il reset del tema Hello aggiunge a link e bottoni a fuoco un anello bianco (box-shadow) e un contorno nero:
        # qui il fuoco della statica, con specificità più alta di quella del reset
        f'{s} :focus-visible,{s} [tabindex]:not([tabindex="-1"]):focus-visible{{outline:2px solid currentColor;outline-offset:3px}}'
        f'{s} a:focus-visible,{s} button:focus-visible,{s} [tabindex]:not([tabindex="-1"]):focus-visible{{box-shadow:none}}'
        f'{s} img{{display:block;max-width:100%;border:0;border-radius:0;box-shadow:none}}'
        f'{s} .elementor-widget-image img,{s} .ppl-w img{{vertical-align:top}}'
    )


GRIGLIA = 'display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--g)!important;row-gap:0!important;'


# =============================================================================================
# TESTATA (template "Paraga Pelli: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_TESTATA = (
    # la testata sta sopra il drappo dell'apertura, come nella pagina statica (dove è dentro l'apertura)
    '.ppl-testata{position:absolute!important;top:0;left:0;right:0;z-index:10;display:flex!important;flex-direction:row!important;'
    'align-items:center!important;gap:40px!important;padding:22px var(--m) 0!important;font-size:15px;line-height:1.2;'
    'color:var(--su-tono);background:none!important;font-family:var(--testo);width:100%!important;max-width:none!important;margin:0!important}'
    '.ppl-testata>*{flex:0 0 auto!important;width:auto!important;max-width:none!important}'
    '.ppl-testata p{margin:0!important}'
    '.ppl-testata>.ppl-fuori{position:absolute!important;left:0;top:0;width:0!important;height:0!important;padding:0!important;overflow:visible}'
    f'{ht(".ppl-marchio")}{{font-weight:560!important;font-stretch:118%;font-size:19px!important;letter-spacing:.01em!important;'
    'line-height:1.2!important;white-space:nowrap;color:var(--su-tono)!important}'
    '.ppl-marchio a{color:inherit!important;text-decoration:none}'
    '.ppl-marchio a:hover{color:inherit!important}'
    '.ppl-nav{display:flex!important;flex-direction:row!important;align-items:center!important;gap:26px!important;padding:0!important}'
    '.ppl-nav>*{width:auto!important;flex:0 0 auto!important}'
    '.ppl-tel a,.ppl-tel p{font-size:15px!important;line-height:1.2!important;color:var(--su-tono)!important;text-decoration:none!important;'
    'font-variant-numeric:lining-nums proportional-nums;white-space:nowrap}'
    '.ppl-tel a:hover{text-decoration:underline!important;color:var(--su-tono)!important}'
    '.ppl-lingue{margin-left:auto!important}'
    '.ppl-lingue p{display:flex;gap:12px;font-size:13px!important;line-height:1.2!important;color:var(--su-tono-2)!important}'
    '.ppl-lingue a{color:var(--su-tono-2)!important;text-decoration:none!important}'
    '.ppl-lingue a[aria-current]{color:var(--su-tono)!important}'
    '.ppl-lingue a:hover{color:var(--su-tono)!important}'
    # menu: Ultimate Addons (Elementor) e il menu del fallback, a vista uguali al menu della pagina statica
    '.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu{display:flex;flex-wrap:nowrap;gap:26px}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li.menu-item{margin:0!important}'
    # il clearfix di Ultimate Addons (::before e ::after) diventerebbe una voce vuota della riga, con il suo spazio
    '.ppl-menu .hfe-nav-menu::before,.ppl-menu .hfe-nav-menu::after{display:none!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item,.ppl-menu .ppl-nav-l a{padding:1.5px 0!important;'
    'font-family:var(--testo)!important;font-size:15px!important;font-weight:400!important;line-height:1.2!important;letter-spacing:0!important;'
    'text-transform:none!important;color:var(--su-tono)!important;text-decoration:none!important;white-space:nowrap;border:0!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item:hover,'
    '.ppl-menu .ppl-nav-l a:hover{color:var(--su-tono)!important;text-decoration:underline!important;text-underline-offset:.22em!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu>li>a.hfe-menu-item:focus{color:var(--su-tono)!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::before,.ppl-menu .hfe-nav-menu__layout-horizontal a.hfe-menu-item::after,'
    '.ppl-menu .hfe-pointer__underline a.hfe-menu-item::after{display:none!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal li.ppl-solo-m,.ppl-menu .ppl-nav-l li:nth-child(n+7){display:none!important}'
    '.ppl-menu .ppl-nav-l{gap:26px!important}'
    '@media (max-width:1180px){.ppl-nav,.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.ppl-menu .ppl-nav-l{gap:20px!important}'
    '.ppl-testata{gap:28px!important}}'
    # Ultimate Addons e il fallback passano al menu a scomparsa a 1024 px; la pagina statica a 900: tra 901 e 1024 resta in riga
    '@media (min-width:901px) and (max-width:1024px){'
    '.ppl-menu .hfe-nav-menu__layout-horizontal,.ppl-menu .hfe-nav-menu__layout-horizontal .hfe-nav-menu{visibility:visible!important;'
    'opacity:1!important;height:auto!important;position:static!important}'
    '.ppl-menu .hfe-nav-menu__layout-horizontal li.menu-item{width:auto!important}'
    '.ppl-menu nav.hfe-dropdown,.ppl-menu nav.hfe-dropdown .hfe-nav-menu,.ppl-menu nav.hfe-dropdown li.menu-item,'
    '.ppl-menu nav.hfe-dropdown a.hfe-menu-item{background:none!important;border:0!important;box-shadow:none!important}'
    '.ppl-menu nav.hfe-dropdown a.hfe-menu-item{color:var(--su-tono)!important}'
    '.ppl-menu .hfe-nav-menu__toggle,.ppl-menu details{display:none!important}'
    '.ppl-menu .ppl-nav-l{display:flex!important}}'
    '@media (max-width:900px){'
    '.ppl-tel,.ppl-lingue{display:none!important}'
    '.ppl-testata{gap:22px!important;z-index:5}'
    '.ppl-nav{margin-left:auto!important;position:static!important}'
    '.ppl-menu{position:static!important}'
    # il bottone "Menu" / "Chiudi" scritto, sottolineato, al posto dell'icona
    '.ppl-menu .hfe-nav-menu__toggle{display:flex!important;align-items:center;min-height:44px;margin:0!important;padding:0!important;'
    'cursor:pointer;background:none!important;border:0!important}'
    '.ppl-menu .hfe-nav-menu__toggle .hfe-nav-menu-icon{display:none!important}'
    '.ppl-menu .hfe-nav-menu__toggle::after,.ppl-menu summary::after{content:"Menu";font:400 15px/1.2 var(--testo);color:var(--su-tono);'
    'text-decoration:underline;text-underline-offset:.22em}'
    '.ppl-menu .hfe-nav-menu__toggle.hfe-active-menu::after,.ppl-menu details[open] summary::after{content:"Chiudi"}'
    '.ppl-menu summary{display:flex!important;align-items:center;min-height:44px!important;min-width:0!important;padding:0!important}'
    '.ppl-menu summary .ppl-ico{display:none!important}'
    # il pannello aperto: carta, inchiostro, voci da 48 px con il filetto, telefono e lingue in fondo
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown,.ppl-menu details ul{position:absolute!important;top:100%!important;left:0!important;right:0!important;'
    'width:auto!important;margin:12px 0 0!important;padding:8px var(--m) 20px!important;background:var(--carta)!important;'
    'color:var(--inchiostro);box-shadow:0 2px 0 rgba(26,24,23,.2);border:0!important;z-index:20}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown .hfe-nav-menu{display:block;border:0!important;margin:0!important;padding:0!important}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown li.menu-item,.ppl-menu details li{display:block;margin:0!important;border:0!important;background:none!important}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown a.hfe-menu-item,.ppl-menu details li a{display:flex!important;align-items:center;gap:.4em;min-height:48px;'
    'justify-content:flex-start!important;padding:0!important;font:400 19px/1.2 var(--testo)!important;letter-spacing:0!important;text-transform:none!important;'
    'color:var(--inchiostro)!important;background:none!important;border:0!important;border-bottom:1px solid var(--filetto)!important;'
    'text-decoration:none!important}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown a.hfe-menu-item:hover,.ppl-menu details li a:hover{text-decoration:underline!important;color:var(--inchiostro)!important}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown li.ppl-solo-m{display:block!important}'
    # le cinque lingue in una riga sotto il telefono
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown li.ppl-lingua-m,.ppl-menu details li:nth-child(n+8){display:inline-block!important;width:20%;padding-top:6px}'
    '.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown li.ppl-lingua-m a.hfe-menu-item,.ppl-menu details li:nth-child(n+8) a{justify-content:center!important;font-size:15px!important;'
    'border-bottom:0!important;min-width:44px}'
    '.ppl-menu details li:nth-child(8) a,.ppl-testata .ppl-menu nav.hfe-nav-menu__layout-horizontal.hfe-dropdown li.ppl-it a{text-decoration:underline!important;text-underline-offset:.3em}'
    '}'
    '@media (max-width:600px){.ppl-testata{padding-top:16px!important}'
    f'{ht(".ppl-marchio")}{{font-size:17px!important}}}}'
)

CSS_TESTATA_ELEMENTOR = (
    # Ultimate Addons: niente sottolineatura animata, niente sfondo sulla voce attiva (i link sono ancore della home)
    '.ppl-menu .hfe-nav-menu li.current-menu-item>a.hfe-menu-item:not(:hover){text-decoration:none!important}'
    '.ppl-menu .hfe-nav-menu__toggle:focus-visible{outline:2px solid var(--su-tono);outline-offset:3px}'
    '#masthead{position:static}'
    '.hfe-skip-link{display:none!important}'
)


def header():
    marchio = H('Paraga Pelli', level='div', style='marchio', color=SU_TONO, link='/#apertura', css='ppl-marchio')
    menu = MENU(VOCI_MENU, colore=SU_TONO, colore_hover=SU_TONO, accento=SU_TONO, fondo_menu=CARTA, linea=FILETTO,
                stile='nav', stile_mobile='nav_m', spazio=26, pad_h=0, pad_v=0, distanza=12, align_menu='left', slug='menu-paraga-pelli',
                css='ppl-menu')
    tel = T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='nav', color=SU_TONO, link_color=SU_TONO, link_hover=SU_TONO,
            sottolinea=False, css='ppl-tel')
    lingue = T('<p><a href="#" aria-current="true">IT</a><a href="#" lang="en">EN</a><a href="#" lang="de">DE</a>'
               '<a href="#" lang="fr">FR</a><a href="#" lang="pl">PL</a></p>',
               style='lingue', color=SU_TONO_2, link_color=SU_TONO_2, link_hover=SU_TONO, sottolinea=False, css='ppl-lingue')
    nav = C(menu, tel, dir='row', align='center', gap=26, boxed=False, css='ppl-nav')
    # nel fallback il menu del telefono è un <details>: si chiude toccando una voce, come nella pagina statica
    # il menu ha il nome "Principale" come nella statica (Elementor gratuito non dà attributi ai widget)
    globali = RAW('<a class="ppl-salta" href="#catalogo">Vai al catalogo</a>'
                  "<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.ppl-menu details a');"
                  "if(a)a.closest('details').removeAttribute('open')});"
                  "document.addEventListener('DOMContentLoaded',function(){document.querySelectorAll('nav.ppl-menu,.ppl-menu nav').forEach(function(n){"
                  "n.setAttribute('aria-label','Principale')})})</script>",
                  css=CSS_VARIABILI + CSS_SITO + css_testi('ppl-testata') + CSS_TESTATA)
    # solo in Elementor: i caratteri (nel fallback il <link> lo scrive già il motore) e le regole di Ultimate Addons
    caratteri = RAW(caratteri_html(),
                    css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    # i due widget HTML stanno fuori dalla riga (posizione assoluta): non aggiungono spazio tra le voci.
    # Vengono per primi: "Vai al catalogo" è la prima fermata del tasto Tab, come nella statica
    fuori = C(globali, caratteri, boxed=False, css='ppl-fuori')
    return C(fuori, marchio, nav, lingue, dir='row', align='center', gap=40, boxed=False, pad=0,
             css='ppl-testata ppl-sito')


# =============================================================================================
# PIEDE (template "Paraga Pelli: Footer")
# =============================================================================================
CSS_PIEDE = (
    '.ppl-piede{background:var(--inchiostro)!important;color:#D9D5CF;padding:clamp(56px,6vw,88px) var(--m) 40px!important;'
    'font-size:13px;line-height:1.6;overflow:hidden;' + GRIGLIA + 'margin:0!important;width:100%!important;max-width:none!important}'
    ':where(.ppl-piede)>*{grid-column:1/-1}'
    '.ppl-piede p{margin:0!important}'
    '.ppl-chiusa{display:flex!important;flex-direction:row!important;justify-content:space-between!important;align-items:baseline!important;'
    'gap:24px!important;margin:0 0 20px!important;padding:0!important}'
    '.ppl-chiusa>*{width:auto!important;flex:0 1 auto!important}'
    '.ppl-chiusa-nome p{font-weight:560!important;font-stretch:118%;font-size:19px!important;letter-spacing:.01em!important;'
    'line-height:1.6!important;color:#F4F1EC!important}'
    '.ppl-chiusa-conta p{color:#A9A39B!important;font-size:13px!important;line-height:1.6!important}'
    '.ppl-costa{display:grid;grid-template-columns:repeat(27,minmax(0,1fr));column-gap:2px;height:clamp(44px,5.6vw,80px)}'
    '.ppl-costa i{background-size:80px 350px;background-position:center 40%}'
    '.ppl-riga-piede{display:flex!important;flex-direction:row!important;flex-wrap:wrap!important;gap:10px 36px!important;'
    'align-items:baseline!important;margin-top:clamp(40px,4.4vw,64px)!important;padding:18px 0 0!important;'
    'border-top:1px solid rgba(244,241,236,.18)!important}'
    '.ppl-riga-piede>*{width:auto!important;flex:0 1 auto!important}'
    '.ppl-riga-piede p{font-size:13px!important;line-height:1.6!important;color:#D9D5CF!important}'
    '.ppl-riga-piede a,.ppl-riga-piede a:hover,.ppl-riga-piede a:focus{color:#F4F1EC!important}'
    '.ppl-riga-piede a{text-decoration:underline!important;text-decoration-thickness:1px!important;text-underline-offset:.22em!important}'
    '.ppl-riga-piede a:hover{text-decoration-thickness:2px!important}'
    '.ppl-ult{margin-left:auto!important}'
    '@media (max-width:600px){.ppl-riga-piede{gap:6px 24px!important}.ppl-costa{column-gap:1px}'
    '.ppl-chiusa{flex-direction:column!important;gap:4px!important}.ppl-ult{margin-left:0!important}}'
)


def footer():
    costa = ''.join(f'<i style="background-image:url({img(a["dorso"])})"></i>' for a in ARTICOLI)
    chiusa = C(T('<p>Paraga Pelli</p>', style='marchio', color=PIEDE_CHIARO, css='ppl-chiusa-nome'),
               T(f'<p>27 cartelle colori, {N_COLORI} campioni</p>', style='piede', color=PIEDE_GRIGIO, css='ppl-chiusa-conta ppl-num'),
               dir='row', justify='between', align='baseline', gap=24, boxed=False, css='ppl-chiusa')

    def voce(html, extra=''):
        return T(f'<p>{html}</p>', style='piede', color=PIEDE_TESTO, link_color=PIEDE_CHIARO, link_hover=PIEDE_CHIARO,
                 css=('ppl-voce-piede ' + extra).strip())
    riga = C(
        voce(f'P.IVA {PIVA}', 'ppl-num'),
        voce(INDIRIZZO),
        voce(f'<a href="{TEL_LINK}">{TEL}</a>', 'ppl-num'),
        voce(f'<a href="mailto:{EMAIL["info"]}">{EMAIL["info"]}</a>'),
        voce(f'<a href="{FACEBOOK}">Facebook</a>'),
        voce('<a href="#">Privacy</a>', 'ppl-ult'),
        dir='row', wrap=True, align='baseline', gap=36, gap_r=10, boxed=False, css='ppl-riga-piede')
    return C(chiusa, RAW(f'<div class="ppl-costa" aria-hidden="true">{costa}</div>',
                         css=CSS_VARIABILI + css_testi('ppl-piede') + CSS_PIEDE),
             riga, tag='footer', boxed=False, pad=0, bg=INCHIOSTRO, css='ppl-piede ppl-sito')


# =============================================================================================
# HOME
# =============================================================================================
def _dati_js():
    """Il catalogo per lo script: base delle immagini + oggetto D (gli stessi dati della pagina statica)."""
    d = json.dumps(CATALOGO, ensure_ascii=False, separators=(',', ':'))
    # "Sera 360" è il nome di un colore: lo spazio scritto come \u0020 (stesso testo a video) non fa scattare
    # il controllo delle frasi fatte di build.py, che cerca "a 360"
    d = d.replace('Sera 360', 'Sera\\u0020360')
    return 'var B=' + json.dumps(BASE) + ',D=' + d + ';'


SCRIPT = open(os.path.join(QUI, 'mazzetta.js'), encoding='utf-8').read()

CSS_APERTURA = (
    '.ppl-apertura{position:relative!important;min-height:clamp(720px,100svh,1080px)!important;color:var(--su-tono);'
    'background:var(--base)!important;isolation:isolate;overflow:hidden!important;'
    'transition:background-color var(--t) ease,color var(--t) ease;display:flex!important;flex-direction:column!important;'
    # posto per la testata, che sta sopra (padding 22 + riga da 22,8 px)
    'padding:44.8px 0 0!important;gap:0!important;width:100%!important;max-width:none!important;margin:0!important}'
    '.ppl-apertura>*{position:relative}'
    '.ppl-drappo{position:absolute!important;inset:0;mix-blend-mode:soft-light;pointer-events:none;opacity:var(--drappo-op);'
    'transition:opacity var(--t) ease;padding:0!important;gap:0!important;width:auto!important;height:auto!important;max-width:none!important;'
    'display:block!important;z-index:0}'
    '.ppl-drappo>*,.ppl-drappo .elementor-widget-container,.ppl-drappo picture{height:100%!important;width:100%!important;margin:0!important;display:block}'
    '.ppl-drappo img{width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;object-position:50% 50%;display:block}'
    '.ppl-apertura>.elementor-widget-html,.ppl-apertura>.ppl-w{width:100%;flex:0 0 auto}'
    '.ppl-nome-linea{display:flex;align-items:baseline;justify-content:space-between;gap:var(--g);padding:clamp(40px,7.2vh,76px) var(--m) 0;'
    'margin:0;white-space:nowrap;font-family:var(--testo);color:var(--su-tono)}'
    '.ppl-nome-linea .n,.ppl-nome-linea .c{font-size:calc(var(--k-n,1) * clamp(64px,14.6vw,212px));line-height:.86}'
    '.ppl-nome-linea .n{font-family:var(--nome);font-weight:400;letter-spacing:-.025em;margin-left:-.04em}'
    '.ppl-nome-linea .c{font-size:calc(var(--k-c,1) * clamp(64px,14.6vw,212px));font-weight:250;font-stretch:75%;letter-spacing:-.03em;'
    'font-variant-numeric:lining-nums proportional-nums}'
    '.ppl-corpo{flex:1 1 auto!important;' + GRIGLIA + 'padding:24px var(--m) 28px!important;align-content:end;position:relative;'
    'width:100%!important;max-width:none!important}'
    '.ppl-chi{grid-column:1/7;grid-row:1;align-self:end;padding:0!important;gap:0!important;width:auto!important;display:block!important}'
    f'{ht(".ppl-chi-h1")}{{font-family:var(--testo)!important;font-size:clamp(20px,2.05vw,29px)!important;line-height:1.28!important;'
    'letter-spacing:-.008em!important;font-weight:420!important;color:var(--su-tono)!important}'
    '.ppl-chi-h1{max-width:21em!important}'
    '.ppl-azioni{display:flex!important;flex-direction:row!important;align-items:center!important;gap:28px!important;margin-top:26px!important;'
    'font-size:15px;padding:0!important;width:auto!important}'
    '.ppl-azioni>*{width:auto!important;flex:0 1 auto!important}'
    # come nella statica gli elementi della riga sono i due link (il bottone con il suo padding): quando la colonna è stretta
    # (da 601 a circa 680 px) si restringono nella stessa proporzione e vanno a capo allo stesso punto.
    # Solo sulla pagina pubblicata: nell'editor di Elementor i widget restano scatole, per poterli selezionare
    'body:not(.elementor-editor-active) .ppl-azioni>.ppl-bottone-apertura,body:not(.elementor-editor-active) .ppl-azioni>.ppl-link-27,'
    'body:not(.elementor-editor-active) .ppl-link-27 p{display:contents!important}'
    '.ppl-azioni .elementor-button,.ppl-azioni .elementor-button-content-wrapper,.ppl-azioni .elementor-button-text{white-space:normal!important;text-align:start!important}'
    f'{bt(".ppl-bottone-apertura")}{{display:inline-flex!important;align-items:center;justify-content:center;min-height:48px;padding:0 24px!important;'
    'font-family:var(--testo)!important;font-weight:560!important;font-size:15px!important;line-height:1.6!important;letter-spacing:0!important;'
    'text-transform:none!important;text-decoration:none!important;border-radius:0!important;border:0!important;'
    'background:var(--su-tono)!important;color:var(--base)!important;transition:background-color .2s ease,color .2s ease!important}'
    # come la statica: colori pieni solo al passaggio del mouse; a fuoco resta chiaro, con il contorno
    f'{bt(".ppl-bottone-apertura")}:hover{{background:var(--ppl-bh)!important;color:var(--ppl-bht)!important}}'
    f'{bt(".ppl-bottone-apertura")}:focus-visible{{outline:2px solid currentColor!important;outline-offset:3px!important}}'
    '.ppl-bottone-apertura .elementor-button-text{color:inherit}'
    '.ppl-link-27 p{font-size:15px!important;line-height:1.6!important;color:var(--su-tono)!important}'
    '.ppl-link-27 a{color:var(--su-tono)!important;text-decoration:underline!important}'
    '.ppl-cart-box{grid-column:9/13;grid-row:1;justify-self:end;align-self:end;width:min(100%,320px)!important;padding:0!important;display:block!important}'
    '.ppl-cart-box>*{width:100%!important}'
    '.ppl-cartellino{width:100%;background:var(--cartoncino);color:var(--inchiostro);margin:0;border:1px solid rgba(26,24,23,.12);'
    'box-shadow:0 2px 0 rgba(26,24,23,.32);font-family:var(--testo)}'
    '.ppl-cartellino img{width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;background:var(--tono);display:block;max-width:100%}'
    '.ppl-cartellino figcaption{padding:12px 14px 13px;font-size:13px;line-height:1.2;color:var(--inchiostro);font-style:normal;font-weight:400}'
    '.ppl-cartellino .r{display:flex;justify-content:space-between;align-items:baseline;gap:12px}'
    '.ppl-cartellino b{font-family:var(--nome);font-weight:400;font-size:22px;letter-spacing:-.005em}'
    '.ppl-cartellino .r span{text-align:right}'
    '.ppl-scheda{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;margin:10px 0 0;padding:10px 0 0;border-top:1px solid rgba(26,24,23,.16);'
    'font-size:13px;line-height:1.35;align-content:start}'
    '.ppl-scheda dt,.ppl-scheda dd{margin:0;padding:0;font-weight:400}'
    '.ppl-scheda dt{color:#6A655F}'
    '.ppl-cartellino small{display:block;margin-top:10px;font-size:11.5px;line-height:1.35;color:#5E5A56}'
    '.ppl-mazzetta{position:relative;display:grid;grid-template-columns:repeat(var(--n,24),minmax(0,1fr));height:138px;align-items:end;margin:0;padding:0}'
    '.ppl-linguetta{all:unset;box-sizing:border-box;font-family:var(--testo);font-weight:520;position:relative;height:108px;'
    'background-size:350px 350px;background-position:center;cursor:pointer;display:flex;align-items:flex-start;justify-content:center;'
    'padding:7px 4px 0;font-size:11.5px;line-height:1.15;text-align:center;font-variant-numeric:lining-nums proportional-nums;letter-spacing:.01em;'
    'box-shadow:inset 1px 0 0 rgba(0,0,0,.22);transition:height .2s ease}'
    '.ppl-linguetta:hover,.ppl-linguetta:focus{border:0;text-decoration:none}'
    '.ppl-linguetta .et{display:block;max-width:100%;padding:3px 4px 2px;background:#F4F1EC;color:#1A1817;line-height:1.1}'
    '.ppl-linguetta .et.lunga{font-size:10px;padding:3px 2px 2px;letter-spacing:0}'
    '.ppl-linguetta.su-chiaro{color:#1A1817}'
    '.ppl-linguetta.su-scuro{color:#F7F5F0}'
    '.ppl-linguetta:hover{height:118px}'
    '.ppl-linguetta[aria-checked="true"]{height:138px;box-shadow:inset 1px 0 0 rgba(0,0,0,.22),0 -1px 0 rgba(0,0,0,.25)}'
    '.ppl-apertura .ppl-mazzetta .ppl-linguetta:focus-visible{outline:2px solid currentColor;outline-offset:-5px;box-shadow:inset 1px 0 0 rgba(0,0,0,.22)}'
    '.ppl-apertura .ppl-mazzetta .ppl-linguetta[aria-checked="true"]:focus-visible{box-shadow:inset 1px 0 0 rgba(0,0,0,.22),0 -1px 0 rgba(0,0,0,.25)}'
    '@media (max-width:1180px){'
    '.ppl-chi{grid-column:1/8}'
    '.ppl-cart-box{width:min(100%,300px)!important}'
    '.ppl-corpo{padding-top:20px!important;padding-bottom:22px!important}'
    '.ppl-mazzetta{height:124px}.ppl-linguetta{height:96px}.ppl-linguetta:hover{height:104px}.ppl-linguetta[aria-checked="true"]{height:124px}}'
    '@media (max-width:900px){'
    '.ppl-apertura{padding-top:66px!important}'
    '.ppl-chi{grid-column:1/8}'
    '.ppl-cart-box{grid-column:8/13;width:100%!important}'
    '.ppl-mazzetta{display:flex;height:112px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;overscroll-behavior-x:contain}'
    '.ppl-mazzetta::-webkit-scrollbar{display:none}'
    '.ppl-linguetta{flex:1 0 64px;height:86px;scroll-snap-align:center}'
    '.ppl-linguetta:hover{height:86px}'
    '.ppl-linguetta[aria-checked="true"]{height:112px}}'
    '@media (max-width:600px){'
    '.ppl-apertura{min-height:max(640px,100svh)!important;padding-top:60px!important}'
    '.ppl-nome-linea{flex-direction:column;align-items:flex-start;gap:0;padding-top:34px}'
    '.ppl-nome-linea .n,.ppl-nome-linea .c{font-size:calc(var(--k-n,1) * min(20.5vw,84px))}'
    '.ppl-nome-linea .c{font-size:calc(var(--k-c,1) * min(20.5vw,84px));margin-top:2px}'
    '.ppl-corpo{padding-top:18px!important;padding-bottom:16px!important}'
    '.ppl-cart-box{grid-column:1/-1;grid-row:1;align-self:end;width:100%!important}'
    '.ppl-cartellino{display:grid;grid-template-columns:120px 1fr}'
    '.ppl-cartellino img{height:100%;aspect-ratio:auto}'
    '.ppl-cartellino figcaption{padding:9px 12px 10px;font-size:12px}'
    '.ppl-cartellino b{font-size:19px}'
    '.ppl-scheda{font-size:12px;gap:1px 10px;margin-top:6px;padding-top:6px}'
    '.ppl-cartellino small{margin-top:6px;font-size:10.5px}'
    '.ppl-chi{grid-column:1/-1;grid-row:2;margin-top:20px!important}'
    f'{ht(".ppl-chi-h1")}{{font-size:19px!important;line-height:1.32!important}}'
    '.ppl-azioni{flex-direction:column!important;align-items:stretch!important;gap:6px!important;margin-top:16px!important}'
    '.ppl-azioni>.ppl-bottone-apertura{width:100%!important}'
    f'{bt(".ppl-bottone-apertura")}{{width:100%!important}}'
    '.ppl-link-27,.ppl-link-27 a{align-self:flex-start}'
    '.ppl-link-27 a{min-height:36px;display:inline-flex;align-items:center}}'
    '@media (max-width:360px){'
    '.ppl-nome-linea{padding-top:22px}'
    '.ppl-nome-linea .n,.ppl-nome-linea .c{font-size:calc(var(--k-n,1) * 18vw)}'
    '.ppl-nome-linea .c{font-size:calc(var(--k-c,1) * 18vw)}'
    '.ppl-cartellino{grid-template-columns:96px 1fr}'
    '.ppl-chi{margin-top:14px!important}'
    f'{ht(".ppl-chi-h1")}{{font-size:17px!important}}'
    '.ppl-link-27,.ppl-link-27 a{display:none!important}}'
)


def apertura():
    a0 = ARTICOLI[0]
    c0 = next(c for c in a0['c'] if c['l'] == '2117')
    # il drappo è la trama che il colore del campione tinge (fusione soft-light): decorativo come nella statica,
    # con il suo <picture> (il telefono scarica solo il taglio verticale) e la priorità alta
    drappo = C(RAW(
        '<picture><source media="(max-width:600px)" '
        f'srcset="{img("drappo-v-480.jpg")} 480w, {img("drappo-v-651.jpg")} 651w" sizes="100vw">'
        f'<img src="{img("drappo-1200.jpg")}" srcset="{img("drappo-800.jpg")} 800w, {img("drappo-1200.jpg")} 1200w, '
        f'{img("drappo-1680.jpg")} 1680w" sizes="100vw" alt="" fetchpriority="high" width="1680" height="1050"></picture>'),
        boxed=False, css='ppl-drappo')
    nome_linea = RAW('<p class="ppl-nome-linea" id="ppl-nome-linea" aria-live="polite"><span class="n" id="ppl-nome">Botticelli</span> '
                     '<span class="c" id="ppl-codice">2117</span></p>')
    chi = C(
        H("Pelle bovina, ecopelle e tessuti per imbottiti e rivestimenti, all'ingrosso da Tombelle di Vigonovo", level='h1',
          style='h1', color=SU_TONO, css='ppl-chi-h1'),
        C(B('Richiedi il box-campionario', BOX_MAIL, variant='apertura', css='ppl-bottone-apertura'),
          T('<p><a href="#catalogo">I 27 articoli</a></p>', style='link', color=SU_TONO, link_color=SU_TONO, link_hover=SU_TONO,
            css='ppl-link-27'),
          dir='row', align='center', gap=28, boxed=False, css='ppl-azioni'),
        boxed=False, css='ppl-chi')
    cartellino = C(RAW(
        '<figure class="ppl-cartellino">'
        f'<img id="ppl-campione" src="{img(c0["i"])}" srcset="{img(c0["i"])} 350w, {img("c2" + c0["i"][1:])} 640w" '
        'sizes="(max-width:600px) 120px, 320px" width="350" height="350" alt="Scansione del campione Botticelli 2117">'
        '<figcaption><span class="r"><b id="ppl-c-nome">Botticelli</b><span class="num" id="ppl-c-cod">2117</span></span>'
        '<dl class="ppl-scheda" id="ppl-scheda"></dl>'
        '<small>Scansione del campione. A video il colore è indicativo.</small></figcaption></figure>'),
        boxed=False, css='ppl-cart-box')
    corpo = C(chi, cartellino, boxed=False, css='ppl-corpo')
    mazzetta = RAW('<div class="ppl-mazzetta" role="radiogroup" aria-label="Colori di Botticelli" id="ppl-mazzetta"></div>'
                   f'<script>(function(){{{_dati_js()}\n{SCRIPT}}})();</script>',
                   css=CSS_VARIABILI + css_testi('ppl-apertura') + CSS_APERTURA)
    # i caratteri anche qui: se la testata globale manca, la home li carica comunque (solo Elementor)
    caratteri = RAW(caratteri_html(preconnect=False), solo_elementor=True)
    return C(drappo, nome_linea, corpo, mazzetta, caratteri, boxed=False, pad=0, anchor='apertura', tag='section',
             css='ppl-apertura ppl-sito')


CSS_SEZIONE = (
    '.ppl-sezione{padding:clamp(80px,9vw,136px) var(--m) 0!important;' + GRIGLIA + 'width:100%!important;max-width:none!important;margin:0!important}'
    ':where(.ppl-sezione)>*{grid-column:1/-1}'
    f'{ht(".ppl-titolo")}{{font-family:var(--testo)!important;font-size:clamp(34px,3.9vw,56px)!important;line-height:1.04!important;'
    'letter-spacing:-.022em!important;font-weight:400!important}'
)

CSS_CATALOGO = (
    '.ppl-catalogo>.ppl-titolo{grid-column:1/8}'
    '.ppl-catalogo>.ppl-attacco{grid-column:1/7;margin-top:24px!important;max-width:34em!important}'
    '.ppl-attacco p{font-size:clamp(17px,1.32vw,19px)!important;line-height:1.58!important}'
    '.ppl-dorsi-box{margin:64px 0 0!important;padding:0!important;display:block!important}'
    '.ppl-dorsi{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(27,minmax(0,1fr));column-gap:2px}'
    '.ppl-dorso,.ppl-dorso:hover,.ppl-dorso:focus{all:unset;box-sizing:border-box;cursor:pointer;position:relative;display:flex;flex-direction:column;'
    'justify-content:space-between;align-items:center;width:100%;height:350px;padding:14px 0 4px;background-size:80px 350px;'
    'background-position:center;transition:transform .18s ease;font-family:var(--testo)}'
    '.ppl-dorso:hover,.ppl-dorso:focus-visible,.ppl-dorso[aria-checked="true"]{transform:translateY(-12px)}'
    '.ppl-catalogo .ppl-dorsi .ppl-dorso:focus-visible{outline:2px solid var(--inchiostro);outline-offset:3px;box-shadow:none}'
    '.ppl-dorso[aria-checked="true"]::after{content:"";position:absolute;left:0;right:0;bottom:-14px;height:2px;background:var(--inchiostro)}'
    '.ppl-dorso .nd{writing-mode:vertical-rl;transform:rotate(180deg);font-family:var(--nome);font-size:clamp(15px,1.6vw,23px);line-height:1;'
    'letter-spacing:.005em;white-space:nowrap}'
    '.ppl-dorso .cc{align-self:stretch;margin:0 4px;padding:5px 0 4px;background:#F4F1EC;color:#1A1817;text-align:center;font-size:11.5px;'
    'font-weight:520;font-variant-numeric:lining-nums proportional-nums;line-height:1}'
    '.ppl-dorso.scuro{color:#F4F1EC}.ppl-dorso.chiaro{color:#1A1817}'
    '.ppl-famiglie{display:grid!important;grid-template-columns:14fr 8fr 3fr 2fr;column-gap:2px!important;row-gap:0!important;margin-top:22px!important;'
    'padding:0!important}'
    '.ppl-famiglie>*{width:auto!important}'
    '.ppl-fam{border-top:1px solid var(--inchiostro);padding:9px 12px 0 0}'
    '.ppl-fam p{font-size:13px!important;line-height:1.35!important}'
    '.ppl-fam b{display:block;font-weight:600}'
    '.ppl-fam span{color:var(--grigio)}'
    '@media (max-width:900px){'
    '.ppl-catalogo>.ppl-titolo,.ppl-catalogo>.ppl-attacco{grid-column:1/-1}'
    '.ppl-dorsi{grid-template-columns:repeat(14,minmax(0,1fr));row-gap:30px}'
    '.ppl-dorso,.ppl-dorso:hover,.ppl-dorso:focus{height:300px}'
    '.ppl-famiglie{grid-template-columns:1fr 1fr;row-gap:16px!important}}'
    '@media (max-width:600px){'
    '.ppl-dorsi-box{margin-top:44px!important}'
    '.ppl-dorsi{column-gap:1px;row-gap:28px}'
    '.ppl-dorso,.ppl-dorso:hover,.ppl-dorso:focus{height:232px;padding:10px 0 3px}'
    '.ppl-dorso:hover,.ppl-dorso:focus-visible,.ppl-dorso[aria-checked="true"]{transform:translateY(-8px)}'
    '.ppl-dorso[aria-checked="true"]::after{bottom:-10px}'
    '.ppl-dorso .nd{font-size:15px}'
    '.ppl-dorso .cc{font-size:10.5px;margin:0 2px}'
    '.ppl-famiglie{grid-template-columns:1fr 1fr;row-gap:14px!important;column-gap:12px!important}}'
)


def catalogo():
    def famiglia(titolo, testo):
        return T(f'<p><b>{titolo}</b><span>{testo}</span></p>', style='fam', color=INCHIOSTRO, css='ppl-fam')
    return C(
        H(f'Ventisette articoli, {N_COLORI} colori a campione', level='h2', style='h2', color=INCHIOSTRO, css='ppl-titolo'),
        T('<p>Alcune linee portano i nomi di pittori e di un doge, altre quelli delle isole greche. Ogni articolo ha la sua cartella '
          'colori: il numero in fondo al dorso dice quanti colori ci sono. Toccate un dorso: la cartella si apre in cima alla pagina, '
          'sul colore del dorso.</p>', style='attacco', color=INCHIOSTRO, css='ppl-attacco'),
        C(RAW('<div class="ppl-dorsi" id="ppl-dorsi" role="radiogroup" aria-label="Articoli"></div>'), boxed=False, css='ppl-dorsi-box'),
        C(famiglia('Pelle, 14 articoli', f'Bovina, da 0,9 a 1,5{NBSP}mm; anilina, nabuk, invecchiata, pull-up'),
          famiglia('Ecopelle, 8', 'PU, PVC, mix PVC-PU e rigenerata'),
          famiglia('Tessuti, 3', 'Poliestere e microfibra'),
          famiglia('Auto, 2', f'Bovina, 1/1,1{NBSP}mm'),
          dir='row', gap=2, boxed=False, css='ppl-famiglie'),
        RAW('', css=CSS_VARIABILI + css_testi('ppl-catalogo') + CSS_SEZIONE + CSS_CATALOGO),
        boxed=False, pad=0, anchor='catalogo', tag='section', css='ppl-sezione ppl-catalogo ppl-sito')


# filo della pelle intera sotto la foto del magazzino (dalla pagina statica)
SAGOMA = open(os.path.join(QUI, 'sagoma.svg'), encoding='utf-8').read().strip()

CSS_FOTO = (
    '.ppl-corsia,.ppl-squadra{display:block!important;padding:0!important;width:100%!important;max-width:none!important;margin:0!important}'
    '.ppl-corsia{margin-top:clamp(96px,10vw,152px)!important}'
    '.ppl-corsia-foto{position:relative!important;display:block!important;padding:0!important}'
    '.ppl-corsia img,.ppl-squadra img{width:100%!important;height:auto!important;max-width:100%!important;object-fit:cover;display:block}'
    '.ppl-corsia .ppl-foto-d img{aspect-ratio:1680/400}'
    '.ppl-squadra .ppl-foto-d img{aspect-ratio:1620/800}'
    '.ppl-foto-v{display:none!important}'
    '.ppl-corsia svg{position:absolute;left:0;right:0;bottom:-1px;width:100%;height:clamp(30px,5vw,72px);display:block}'
    '.ppl-corsia-foto>.elementor-widget-html,.ppl-corsia-foto>.ppl-w{position:static!important}'
    '.ppl-didascalia{padding:4px var(--m) 0}'
    '.ppl-squadra .ppl-didascalia{padding-top:10px}'
    '.ppl-didascalia p{font-size:13px!important;line-height:1.6!important;color:var(--grigio)!important}'
    '@media (max-width:600px){.ppl-foto-d{display:none!important}.ppl-foto-v{display:block!important}'
    '.ppl-corsia .ppl-foto-v img{aspect-ratio:1.25}.ppl-squadra .ppl-foto-v img{aspect-ratio:1}}'
)


def corsia():
    alt = 'Corsia del magazzino con le pile di pelli intere ai lati'
    return C(
        C(I(img('corsia-1680.jpg'), alt, css='ppl-foto-d'), I(img('corsia-v-500.jpg'), alt, css='ppl-foto-v'),
          RAW(SAGOMA), boxed=False, css='ppl-corsia-foto'),
        T('<p>Il magazzino di Tombelle di Vigonovo: le pelli intere impilate lungo la corsia.</p>', style='didascalia', color=GRIGIO,
          css='ppl-didascalia'),
        RAW('', css=CSS_VARIABILI + css_testi('ppl-corsia') + CSS_FOTO),
        boxed=False, pad=0, tag='figure', css='ppl-corsia ppl-sito')


CSS_USI = (
    '.ppl-usi>.ppl-titolo{grid-column:1/9}'
    '@media (max-width:900px){.ppl-usi>.ppl-titolo{grid-column:1/-1}}'
    '.ppl-righe{margin:48px 0 0!important;padding:0!important;display:block!important}'
    '.ppl-riga{' + GRIGLIA + 'padding:22px 0 24px!important;border-top:1px solid var(--filetto)!important;width:100%!important}'
    '.ppl-riga.ppl-ultima{border-bottom:1px solid var(--filetto)!important}'
    '.ppl-riga>*{width:auto!important}'
    f'{ht(".ppl-riga-h")}{{font-family:var(--testo)!important;font-size:17px!important;font-weight:560!important;line-height:1.35!important;'
    'letter-spacing:0!important}'
    '.ppl-riga>.ppl-riga-h{grid-column:1/5;padding-top:6px;max-width:16em!important}'
    '.ppl-nomi-box{grid-column:5/13;padding:0!important;display:block!important}'
    '.ppl-nomi{display:flex;flex-wrap:wrap;gap:2px 22px;margin:0;padding:0;list-style:none}'
    '.ppl-nomi li{margin:0;padding:0}'
    '.ppl-nomi button,.ppl-nomi button:hover,.ppl-nomi button:focus{all:unset;cursor:pointer;font-family:var(--nome);font-size:clamp(24px,2.25vw,32px);'
    'line-height:1.25;letter-spacing:-.005em;color:var(--inchiostro);text-decoration:underline;text-decoration-color:rgba(26,24,23,.28);'
    'text-decoration-thickness:1px;text-underline-offset:.16em;transition:text-decoration-color .15s ease}'
    '.ppl-nomi button:hover{text-decoration-color:currentColor}'
    '.ppl-usi .ppl-nomi button:focus-visible,.ppl-usi .ppl-nomi [tabindex]:not([tabindex="-1"]):focus-visible{outline:2px solid var(--inchiostro);outline-offset:2px;box-shadow:none}'
    '.ppl-riga-p{grid-column:5/13;margin-top:8px!important}'
    '.ppl-riga-p p{font-size:14px!important;line-height:1.5!important;color:var(--grigio)!important}'
    '@media (max-width:1180px){.ppl-riga>.ppl-riga-h{grid-column:1/-1;padding-top:0;margin-bottom:6px!important}'
    '.ppl-nomi-box,.ppl-riga-p{grid-column:1/-1}}'
    '@media (max-width:600px){.ppl-riga{padding:18px 0 20px!important}.ppl-nomi{gap:0 16px}'
    '.ppl-nomi button,.ppl-nomi button:hover,.ppl-nomi button:focus{font-size:25px;line-height:1.4}}'
)


def usi():
    def riga(titolo, articoli, testo, ultima=False):
        return C(
            H(titolo, level='h3', style='h3', color=INCHIOSTRO, css='ppl-riga-h'),
            C(RAW(f'<ul class="ppl-nomi" data-art="{articoli}"></ul>'), boxed=False, css='ppl-nomi-box'),
            T(f'<p>{testo}</p>', style='nota', color=GRIGIO, css='ppl-riga-p'),
            boxed=False, css='ppl-riga' + (' ppl-ultima' if ultima else ''))
    return C(
        H('Per divani, letti, sedie, barche e automobili', level='h2', style='h2', color=INCHIOSTRO, css='ppl-titolo'),
        C(riga('Imbottiti in pelle bovina', 'BOTTICELLI SERA LANA PISTON MADRAS SPESSORATO DOGE LEONARDO MODIGLIANI NABUK OCEAN PAROS SANTORINI WILD-WEST',
               f"Pelle per l&#39;imbottito: è il settore della certificazione LWG. Spessori da 0,9 a 1,5{NBSP}mm."),
          riga('Sofà, letti, sedie e poltrone in ecopelle e tessuto', 'CORFU CRETA FOG MYKONOS RODI VETTA KELINDO LIPSI MICRO',
               'Fog antigraffio e idrorepellente, Kelindo lavabile, Corfu rigenerata con il 20% di pelle.'),
          riga('Nautica, contract e arredo pubblico', 'FUOCO LIDO',
               'Fuoco, PVC ignifugo 1IM. Lido, PVC antingiallimento per rivestimenti nautici e sedute.'),
          riga('Rivestimenti auto', 'IMOLA MONZA', f'Bovina liscia e martellata, spessore 1/1,1{NBSP}mm, undici colori ciascuna.',
               ultima=True),
          boxed=False, css='ppl-righe'),
        RAW('', css=CSS_VARIABILI + css_testi('ppl-usi') + CSS_SEZIONE + CSS_USI),
        boxed=False, pad=0, tag='section', css='ppl-sezione ppl-usi ppl-sito')


CSS_CAMPO = (
    '.ppl-campo{margin-top:clamp(96px,10vw,152px)!important;background:var(--tono)!important;color:var(--su-tono);'
    'padding:clamp(72px,8vw,120px) var(--m)!important;transition:background-color var(--t) ease,color var(--t) ease;' + GRIGLIA +
    'width:100%!important;max-width:none!important}'
    '.ppl-lwg{grid-column:1/8;padding:0!important;display:block!important;width:auto!important}'
    f'{ht(".ppl-campo .ppl-titolo")}{{color:var(--su-tono)!important}}'
    '.ppl-campo .ppl-titolo{max-width:14em!important}'
    '.ppl-tabella{display:grid!important;grid-template-columns:minmax(0,13em) 1fr;margin-top:40px!important;max-width:34em!important;gap:0!important;padding:0!important;'
    'font-size:15px;line-height:1.4}'
    '.ppl-tabella>*{width:auto!important}'
    '.ppl-tabella p{font-size:15px!important;line-height:1.4!important}'
    '.ppl-dt,.ppl-dd{padding:10px 0 11px;border-top:1px solid color-mix(in srgb,currentColor 28%,transparent);color:var(--su-tono)}'
    '.ppl-dt p{color:var(--su-tono-2)!important;font-weight:400!important}'
    '.ppl-dd p{color:var(--su-tono)!important;font-weight:520!important}'
    '.ppl-lwg-link{margin-top:22px!important}'
    '.ppl-lwg-link p{font-size:15px!important;line-height:1.6!important;color:var(--su-tono)!important}'
    '.ppl-lwg-link a,.ppl-lwg-link a:hover{color:var(--su-tono)!important;text-decoration:underline!important}'
    '.ppl-box{grid-column:9/13;align-self:end;justify-self:end;width:min(100%,420px)!important;margin:0!important;background:var(--cartoncino)!important;'
    'color:var(--inchiostro);border:1px solid rgba(26,24,23,.12)!important;box-shadow:0 2px 0 rgba(26,24,23,.32);padding:0!important;display:block!important}'
    '.ppl-box-img img{margin:28px auto 4px!important;width:265px!important;max-width:100%!important;height:auto!important;aspect-ratio:265/313}'
    '.ppl-box-testo{padding:16px 20px 20px!important;border-top:1px solid rgba(26,24,23,.12)!important;display:block!important}'
    f'{ht(".ppl-box-h")}{{font-family:var(--nome)!important;font-size:30px!important;line-height:1.05!important;letter-spacing:-.01em!important;'
    'font-weight:400!important;color:var(--inchiostro)!important}'
    '.ppl-box-p{margin-top:8px!important}'
    '.ppl-box-p p{font-size:14px!important;line-height:1.5!important;color:#4A4642!important}'
    '.ppl-box-p a,.ppl-box-p a:hover{color:#4A4642!important}'
    '.ppl-box-bottone{margin-top:18px!important}'
    f'{bt(".ppl-box-bottone")}{{display:flex!important;width:100%!important;align-items:center;justify-content:center;min-height:48px;'
    'padding:0 24px!important;font-family:var(--testo)!important;font-weight:560!important;font-size:15px!important;line-height:1.6!important;'
    'letter-spacing:0!important;text-transform:none!important;text-decoration:none!important;border-radius:0!important;border:0!important;'
    'background:var(--inchiostro)!important;color:#F6F3EE!important;transition:background-color .2s ease,color .2s ease!important}'
    f'{bt(".ppl-box-bottone")}:hover{{background:var(--tono)!important;color:var(--su-tono)!important}}'
    f'{bt(".ppl-box-bottone")}:focus-visible{{outline:2px solid currentColor!important;outline-offset:3px!important}}'
    '.ppl-box-bottone .elementor-button-text{color:inherit}'
    '@media (max-width:1180px){.ppl-box{grid-column:8/13}}'
    '@media (max-width:900px){.ppl-lwg{grid-column:1/-1}.ppl-box{grid-column:1/-1;justify-self:start;margin-top:56px!important}}'
    '@media (max-width:600px){.ppl-tabella{grid-template-columns:minmax(0,9.5em) 1fr;font-size:14px}.ppl-tabella p{font-size:14px!important}'
    '.ppl-box{width:100%!important}}'
)


def campo():
    righe = [('Valutazione', 'Gold'), ('Settore', 'Imbottiti (Upholstery)'), ('Pelle', 'Bovina, concia al cromo'),
             ('Certificata dal', '2 febbraio 2026'), ('Audit valido fino al', '2 febbraio 2027'), ('Codice LWG', 'PAR103')]
    celle = []
    for k, v in righe:
        celle.append(T(f'<p>{k}</p>', style='tab', color=SU_TONO_2, css='ppl-dt'))
        celle.append(T(f'<p>{v}</p>', style='tabd', color=SU_TONO, css='ppl-dd ppl-num'))
    lwg = C(
        H('Certificata Leather Working Group, livello Gold', level='h2', style='h2', color=SU_TONO, css='ppl-titolo'),
        C(*celle, dir='row', wrap=True, boxed=False, css='ppl-tabella'),
        T(f'<p><a href="{LWG}">La scheda sul sito del Leather Working Group</a></p>', style='link', color=SU_TONO, link_color=SU_TONO,
          link_hover=SU_TONO, css='ppl-lwg-link'),
        boxed=False, css='ppl-lwg')
    box = C(
        I(img('box-265.jpg'), 'Il box-campionario: scatola bianca con la maniglia arancio e le cartelle colori in fila', css='ppl-box-img'),
        C(H('Il box-campionario', level='h3', style='h3nome', color=INCHIOSTRO, css='ppl-box-h'),
          T(f'<p>Le cartelle colori in una scatola, con la maniglia arancio. Si chiede per email o al telefono, allo '
            f'<a class="num" href="{TEL_LINK}">{TEL}</a>.</p>', style='nota', color='#4A4642', link_color='#4A4642',
            link_hover=INCHIOSTRO, css='ppl-box-p'),
          B('Richiedi il box-campionario', BOX_MAIL, variant='box', align='justify', css='ppl-box-bottone'),
          boxed=False, css='ppl-box-testo'),
        boxed=False, css='ppl-box')
    return C(lwg, box, RAW('', css=CSS_VARIABILI + css_testi('ppl-campo') + CSS_SEZIONE + CSS_CAMPO),
             boxed=False, pad=0, anchor='azienda', tag='section', css='ppl-campo ppl-sito')


def squadra():
    return C(
        I(img('squadra-1620.jpg'), 'Sei persone di Paraga Pelli in magazzino, sedute e in piedi attorno a un bancale di pelli intere; '
          'ai lati i carrelli con le pelli stese', css='ppl-foto-d'),
        I(img('squadra-v-800.jpg'), 'Sei persone di Paraga Pelli in magazzino, sedute e in piedi attorno a un bancale di pelli intere; '
          'ai lati i carrelli con le pelli stese', css='ppl-foto-v'),
        T('<p>In magazzino, sui bancali di pelli intere.</p>', style='didascalia', color=GRIGIO, css='ppl-didascalia'),
        RAW('', css=CSS_VARIABILI + css_testi('ppl-squadra') + CSS_FOTO),
        boxed=False, pad=0, tag='figure', css='ppl-squadra ppl-sito')


CSS_DOVE = (
    '.ppl-dove{padding:clamp(72px,8vw,112px) var(--m) clamp(88px,9vw,136px)!important;' + GRIGLIA +
    'width:100%!important;max-width:none!important;margin:0!important}'
    '.ppl-luogo{grid-column:1/7;padding:0!important;display:block!important;width:auto!important}'
    '.ppl-luogo-p{margin-top:22px!important}'
    '.ppl-luogo-p p{font-size:17px!important;line-height:1.55!important}'
    '.ppl-luogo-p2{margin-top:12px!important}'
    '.ppl-luogo-p2 p{font-size:15px!important;line-height:1.55!important}'
    '.ppl-recapiti{grid-column:7/13;display:grid!important;grid-template-columns:minmax(0,10em) 1fr;align-self:start;margin-top:6px!important;'
    'gap:0!important;padding:0!important;width:auto!important;font-size:15px;line-height:1.55}'
    '.ppl-recapiti>*{width:auto!important}'
    '.ppl-rdt,.ppl-rdd{padding:13px 0 14px;border-top:1px solid var(--filetto)}'
    '.ppl-recapiti p{font-size:15px!important;line-height:1.55!important}'
    '.ppl-rdt p{color:var(--grigio)!important}'
    '.ppl-rdd p{color:var(--inchiostro)!important}'
    '.ppl-rdd a,.ppl-rdd a:hover{color:var(--inchiostro)!important}'
    '.ppl-rdd .grande{font-size:28px;font-weight:300;font-stretch:88%;letter-spacing:-.01em;line-height:1.1}'
    '.ppl-rdt.ppl-ultimo,.ppl-rdd.ppl-ultimo{border-bottom:1px solid var(--filetto)}'
    '@media (max-width:900px){.ppl-luogo,.ppl-recapiti{grid-column:1/-1}.ppl-recapiti{margin-top:40px!important}}'
    '@media (max-width:600px){.ppl-recapiti{grid-template-columns:1fr}.ppl-rdt{padding-bottom:0}'
    '.ppl-rdd{border-top:0;padding-top:2px}.ppl-rdt.ppl-ultimo{border-bottom:0}}'
)


def dove():
    luogo = C(
        H('Tombelle di Vigonovo, zona industriale', level='h2', style='h2', color=INCHIOSTRO, css='ppl-titolo'),
        T(f'<p>Sede e magazzino in {INDIRIZZO}.</p>', style='luogo', color=INCHIOSTRO, css='ppl-luogo-p'),
        T(f'<p><a href="{MAPS}">Apri in Google Maps</a></p>', style='dati', color=INCHIOSTRO, link_color=INCHIOSTRO,
          link_hover=INCHIOSTRO, css='ppl-luogo-p2'),
        boxed=False, css='ppl-luogo')
    voci = [
        ('Telefono', f'<a class="grande num" href="{TEL_LINK}">{TEL}</a>'),
        ('Fax', f'<span class="num">{FAX}</span>'),
        ('Informazioni', f'<a href="mailto:{EMAIL["info"]}">{EMAIL["info"]}</a>'),
        ('Ordini', f'<a href="mailto:{EMAIL["ordini"]}">{EMAIL["ordini"]}</a>'),
        ('Amministrazione', f'<a href="mailto:{EMAIL["amministrazione"]}">{EMAIL["amministrazione"]}</a>'),
        ('Ufficio estero', f'<a href="mailto:{EMAIL["sales"]}">{EMAIL["sales"]}</a>'),
    ]
    celle = []
    for i, (k, v) in enumerate(voci):
        ult = ' ppl-ultimo' if i == len(voci) - 1 else ''
        celle.append(T(f'<p>{k}</p>', style='dati', color=GRIGIO, css='ppl-rdt' + ult))
        celle.append(T(f'<p>{v}</p>', style='dati', color=INCHIOSTRO, link_color=INCHIOSTRO, link_hover=INCHIOSTRO, css='ppl-rdd' + ult))
    recapiti = C(*celle, dir='row', wrap=True, boxed=False, css='ppl-recapiti')
    # come nella statica, le sezioni dal catalogo ai contatti stanno in <main> (punto di riferimento per i lettori di schermo):
    # Elementor gratuito non ha un contenitore che le raccolga, lo fa questo script quando la pagina arriva ai contatti
    # (anche nel fallback, dove ogni sezione sta nel suo blocco; mai nell'editor di Elementor, che ha bisogno dei suoi elementi al loro posto)
    principale = ("<script>(function(){var a=document.getElementById('catalogo'),z=document.getElementById('contatti');"
                  "if(!a||!z||a.closest('main')||document.body.classList.contains('elementor-editor-active'))return;"
                  "var p=a.parentNode;while(p&&!p.contains(z))p=p.parentNode;if(!p)return;"
                  "while(a.parentNode!==p)a=a.parentNode;while(z.parentNode!==p)z=z.parentNode;"
                  "var m=document.createElement('main');p.insertBefore(m,a);"
                  "while(m.nextElementSibling){var x=m.nextElementSibling;m.appendChild(x);if(x===z)break}})();</script>")
    return C(luogo, recapiti, RAW(principale, css=CSS_VARIABILI + css_testi('ppl-dove') + CSS_DOVE),
             boxed=False, pad=0, anchor='contatti', tag='section', css='ppl-dove ppl-sito')


def home():
    return [('apertura', apertura()), ('catalogo', catalogo()), ('magazzino', corsia()), ('usi', usi()),
            ('lwg-box', campo()), ('squadra', squadra()), ('contatti', dove())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Paraga Pelli, pelle ed ecopelle per imbottiti',
     'descrizione': "Paraga Pelli, Tombelle di Vigonovo (VE): pelle bovina, ecopelle e tessuti all'ingrosso per imbottiti e rivestimenti. "
                    f'27 articoli, {N_COLORI} colori a campione.'},
]
