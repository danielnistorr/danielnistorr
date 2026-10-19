# -*- coding: utf-8 -*-
"""
Contenuti della home di Hambro per WordPress + Elementor: la home statica approvata ("Campionario al millimetro",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: testata (marchio, menu di Ultimate Addons, telefono), titoli,
  testi, il bottone "Prova le misure", le foto (apertura in tre tagli, cassetto, bobine, dittico, semilavorati),
  didascalie, le misure della ricopertura, le righe delle misure per settore, il cartellino dei contatti, il piede.
- Widget HTML (nodo RAW del motore) solo dove Elementor gratuito non arriva: il righello d'apertura (SVG disegnato
  dallo script), il banco di misura (lettura, comandi, striscia, taratura), il filo e le sagome in scala della
  ricopertura, le quote in scala delle misure per settore. Lo script è quello della pagina statica (_sorgente/banco.js),
  con i selettori col prefisso hbr-, senza librerie.
- L'impaginazione (griglia a 12 colonne, misure fluide con clamp, scala reale in millimetri) è il foglio di stile della
  pagina statica, con le classi hbr-, dentro i nodi RAW: vale uguale per il template Elementor e per il fallback.
  Tutte le dichiarazioni prendono !important (funzione imp), così prevalgono sugli stili che Elementor scrive per
  ogni widget; tra loro si comportano come nella pagina statica.

Testi e dati: tutti dalla home statica. Nessun dato nuovo.
"""
import os
import re

import motore as m
from motore import C, H, T, B, I, RAW, MENU

QUI = os.path.dirname(os.path.abspath(__file__))

PREFISSO = 'hbr'
NOME_SITO = 'Hambro'

# ---------------------------------------------------------------------------------------------
# Tema: i colori e il carattere della home statica
# ---------------------------------------------------------------------------------------------
CARTA = '#F2EDE4'
INCHIOSTRO = '#1B1714'
GRIGIO = '#5E554C'
CUOIO = '#7B4524'
CAMPO = '#6E3519'
CAMPO_TENUE = '#DCC4AE'
PIEDE_TESTO = '#CFC6B8'
ORO = '#E2B866'
F = 'Mona Sans'
# Mona Sans è su Google Fonts (gli stessi file woff2 della pagina statica). Serve con l'asse della larghezza
# (font-stretch 100-125 %), che l'elenco Google di Elementor non dà: il link è in un widget HTML della testata.
GOOGLE_FONTS = 'https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,200..900&display=swap'


def _st(w, s, lh, ls=0.0):
    return dict(f=F, w=w, s=s, lh=lh, ls=ls, up=False)


# misure (1440, 1024, 390) della pagina statica a quelle larghezze: sono i valori che il pannello di Elementor mostra;
# a video valgono quelle del foglio di stile (con clamp), che prevalgono
TEMA = {
    'nome': 'Campionario',
    'fondo': CARTA, 'superficie': CARTA, 'inchiostro': INCHIOSTRO, 'testo2': GRIGIO, 'accento': CUOIO,
    'filetto': 'rgba(27,23,20,.18)', 'filetto_scuro': 'rgba(242,237,228,.45)', 'su_scuro2': CAMPO_TENUE,
    'scuro': CAMPO, 'su_scuro': CARTA, 'su_accento': CARTA,
    'font_titoli': F, 'font_testo': F, 'larghezza': 1440,
    'google_fonts': GOOGLE_FONTS,
    'stili': {
        'marchio':    _st('640', (22, 22, 22), 1.0, 3.08),
        'nav':        _st('400', (15, 15, 15), 1.55),
        'h1':         _st('380', (136, 97, 53), 0.92, -5.44),
        'h2':         _st('400', (60, 44, 34), 1.0, -1.8),
        'h3':         _st('400', (22, 22, 22), 1.2, -0.22),
        'h3semi':     _st('340', (32, 24, 22), 1.1, -0.64),
        'h4':         _st('500', (17, 17, 15), 1.25),
        'body':       _st('400', (17, 17, 17), 1.55),
        'lede':       _st('400', (17, 17, 17), 1.5),
        'small':      _st('400', (15, 15, 15), 1.55),
        'didascalia': _st('400', (13, 13, 13), 1.45),
        'storia':     _st('400', (22, 22, 22), 1.45),
        'piede':      _st('400', (15, 15, 15), 1.6),
        'tel':        _st('340', (32, 32, 32), 1.1, -0.64),
        'btn':        _st('540', (15, 15, 15), 1.0),
    },
    'spazi': {'sezione': (132, 132, 88), 'lato': (72, 51, 20), 'm': (24, 24, 16), 's': (12, 12, 12), '0': (0, 0, 0)},
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): l'hover cambia colore pieno, mai opacità
    'bottoni': {'cuoio': (CARTA, CUOIO, CUOIO, CARTA, INCHIOSTRO, INCHIOSTRO)},
    'bottone': {'raggio': 0, 'pad': (0, 22, 0, 22), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Il menu della testata non diventa mai un menu a scomparsa: sotto i 1000 px le voci passano su una riga che scorre
# di lato, come nella pagina statica. Il widget di Ultimate Addons ha per questo il punto di rottura "None";
# motore.py lo scrive sempre "tablet", quindi qui lo si cambia sul solo widget del menu (la logica del motore resta quella).
_el_settings = m.el_settings


def _el_settings_hbr(n, inner):
    s = _el_settings(n, inner)
    if n.kind == 'navmenu' and n.p.get('dropdown'):
        s['dropdown'] = n.p['dropdown']
    return s


m.el_settings = _el_settings_hbr

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# La striscia del banco (sfondo CSS) resta a questo indirizzo: per non dipendere da GitHub si caricano
# assets/web/ sul sito e si rigenera con build.py --base.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Hambro-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (come nella home statica; quelli da confermare sono nel LEGGIMI)
# ---------------------------------------------------------------------------------------------
TEL = '049&nbsp;980&nbsp;2326'
TEL_LINK = 'tel:+390499802326'
EMAIL = 'commerciale@hambro.it'
CAMPIONI = 'mailto:commerciale@hambro.it?subject=Richiesta%20campioni%20di%20minuteria'
MAPPA = ('https://www.google.com/maps/search/?api=1&amp;query=Hambro%20srl%2C%20via%20dell%27Artigianato%2030%2C'
         '%2030030%20Vigonovo%20VE')
FACEBOOK = 'https://www.facebook.com/profile.php?id=100057503796900'
PIVA = '00967020280'
WJ = '&#8288;'      # word joiner: gli intervalli (8:00-12:00, 2-60) non vanno a capo sul trattino

# voci del menu: in WordPress è il menu "Menu Hambro" (link personalizzati, li crea l'installatore)
VOCI_MENU = [('Lacci e nastri', '/#lacci'), ('Minuteria', '/#minuteria'), ('Ricopertura', '/#ricopertura'),
             ('Misure per settore', '/#misure'), ('Contatti', '/#contatti')]


# ---------------------------------------------------------------------------------------------
# Aiuti
# ---------------------------------------------------------------------------------------------
def imp(css):
    """Aggiunge !important a ogni dichiarazione (non alle variabili CSS, che lo script cambia in linea)."""
    def blocco(mo):
        out = []
        for d in mo.group(1).split(';'):
            d = d.strip()
            if not d:
                continue
            if d.startswith('--') or d.endswith('!important'):
                out.append(d)
            else:
                out.append(d + '!important')
        return '{' + ';'.join(out) + '}'
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};,>])\s*', r'\1', css).replace(' !important', '!important')
    return re.sub(r'\{([^{}]*)\}', blocco, css)


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return ','.join(f'{s},{s} .elementor-heading-title' for s in sel.split(','))


def ap(html):
    """Apostrofi come entità nei widget Testo: Elementor passa il testo da wptexturize, che li farebbe curvi
    (nella pagina statica sono dritti)."""
    return re.sub(r"'(?![^<]*>)", '&#39;', html)


def TX(html, css, style='body', color=INCHIOSTRO):
    """Widget Testo nativo: la sottolineatura e i colori dei link li dà il foglio di stile della sezione."""
    return T(ap(html), style=style, color=color, link_color=color, link_hover=CUOIO, sottolinea=False, css=css)


def CNT(*figli):
    """Contenitore trasparente (display:contents): i figli del widget HTML entrano nella griglia o nella riga
    del contenitore padre, come nella pagina statica."""
    return C(*figli, boxed=False, css='hbr-cnt')


def STILE(css):
    """Il foglio di stile di una sezione, in un widget HTML che non occupa posto."""
    return CNT(RAW('', css=imp(css)))


# --gap della pagina statica qui si chiama --hbr-gap: Elementor usa già --gap su ogni contenitore e widget
CSS_VARIABILI = (
    ':root{--carta:#F2EDE4;--carta-2:#E8E1D5;--inchiostro:#1B1714;--grigio:#5E554C;--filo:rgba(27,23,20,.18);'
    '--cuoio:#7B4524;--campo:#6E3519;--campo-testo:#F2EDE4;--campo-tenue:#DCC4AE;--taglio:#3A2012;--oro:#E2B866;'
    '--m:clamp(20px,5vw,72px);--hbr-gap:24px;--k:1;--u:calc(1mm * var(--k))}'
    '@media (max-width:700px){:root{--hbr-gap:16px}}'
)


def css_base(s):
    """Regole di base della pagina statica (reset, corpo, link, fuoco, griglia), limitate alla sezione s.
    Il reset è a specificità zero: ogni regola della sezione lo supera, gli stili di Elementor e del tema no."""
    return (
        CSS_VARIABILI +
        'body{background:var(--carta);overflow-x:hidden}'
        # Elementor scorre in modo morbido fino alle ancore del menu; la pagina statica salta subito
        'html{scroll-behavior:auto}'
        f':where({s}),:where({s}) *{{margin:0;padding:0}}'
        f':where({s}) *,:where({s}) *::before,:where({s}) *::after{{box-sizing:border-box}}'
        f'{s}{{font-family:"Mona Sans",system-ui,sans-serif;font-size:17px;line-height:1.55;font-weight:400;font-stretch:100%;'
        'font-synthesis:none;font-variant-numeric:lining-nums;-webkit-font-smoothing:antialiased;color:var(--inchiostro);'
        'text-align:left;text-transform:none;letter-spacing:normal;-webkit-text-size-adjust:100%;text-size-adjust:100%}'
        # i widget e i contenitori ereditano il carattere come i div della pagina statica
        f':where({s}) :is(.elementor-widget,.hbr-w,.e-con,.hbr-con){{font:inherit;letter-spacing:inherit;text-transform:inherit;'
        'color:inherit;text-align:inherit;line-height:inherit;width:auto;max-width:none;min-height:0}'
        f':where({s}) :is(h1,h2,h3,h4,.elementor-heading-title){{font:inherit;font-weight:400;letter-spacing:inherit;'
        'text-transform:inherit;color:inherit;line-height:inherit;text-wrap:balance}'
        f':where({s}) :is(p,li,dd,td){{text-wrap:pretty}}'
        f':where({s}) li{{list-style:none;border:0}}'
        f':where({s}) label{{line-height:inherit;vertical-align:baseline}}'
        f'{s} img{{display:block;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}'
        f'{s} a{{color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.22em;box-shadow:none;'
        'transition:none;background:none}'
        f'{s} a:hover{{color:var(--cuoio)}}'
        f'{s} :focus-visible{{outline:2px solid var(--cuoio);outline-offset:3px;box-shadow:none}}'
        f'{s} .hbr-nascosto{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}'
        '.hbr-cnt,.hbr-cnt>.elementor-widget,.hbr-cnt>.hbr-w{display:contents}'
        '.hbr-griglia{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--hbr-gap);padding-inline:var(--m);'
        'flex-wrap:nowrap}'
        '.hbr-didascalia{font-size:13px;line-height:1.45;color:var(--grigio)}'
        '.hbr-didascalia b{font-weight:600;color:var(--inchiostro);margin-right:.35em}'
        f'{ht(".hbr-h2")}{{font-size:clamp(34px,4.3vw,60px);line-height:1;letter-spacing:-.03em}}'
    )


# =============================================================================================
# TESTATA (template "Hambro: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_TESTATA = (
    '#masthead{position:static}'
    # il collegamento "Salta al contenuto principale" che Ultimate Addons mette prima dell'header (si vede solo col fuoco):
    # porta all'apertura (id content) e ha il carattere e i colori della pagina invece del blu e del carattere di sistema
    '.hfe-skip-link:focus{background:var(--carta);color:var(--inchiostro);font-family:"Mona Sans",system-ui,sans-serif;'
    'font-size:15px;font-weight:400;line-height:1;padding:14px 22px;text-decoration:underline;text-decoration-thickness:1px;'
    'text-underline-offset:.22em;outline:2px solid var(--cuoio);outline-offset:-2px;border-radius:0;box-shadow:none}'
    '.hbr-testa{position:absolute;top:0;left:0;right:0;z-index:5;display:flex;flex-direction:row;flex-wrap:nowrap;'
    'align-items:center;justify-content:space-between;gap:0 24px;padding:16px var(--m) 0;width:auto;max-width:none;margin:0;'
    'background:none;font-size:17px}'
    '.hbr-testa>*{flex:0 1 auto;width:auto}'
    '.hbr-testa>.hbr-fuori{position:absolute;left:0;top:0;width:0;height:0;overflow:hidden}'
    f'{ht(".hbr-marchio")}{{font-stretch:125%;font-weight:640;font-size:22px;letter-spacing:.14em;line-height:1;color:var(--cuoio)}}'
    '.hbr-marchio a{display:block;padding:11px 0;color:var(--cuoio);text-decoration:none}'
    '.hbr-marchio a:hover{color:var(--inchiostro)}'
    # menu: Ultimate Addons (Elementor) e il menu del fallback, a vista uguali al menu della pagina statica
    '.hbr-menu .hfe-nav-menu__toggle,.hbr-menu details{display:none}'
    '.hbr-menu div.hfe-nav-menu,.hbr-menu nav.hfe-nav-menu__layout-horizontal{display:block;font-size:inherit;position:static;'
    'visibility:visible;opacity:1;height:auto;width:auto;background:none;border:0;box-shadow:none}'
    '.hbr-menu ul.hfe-nav-menu,.hbr-menu .hbr-nav-l{display:flex;flex-wrap:nowrap;gap:28px;list-style:none;font-size:15px;'
    'justify-content:flex-start;align-items:stretch;width:auto;visibility:visible;opacity:1;position:static;background:none;border:0}'
    '.hbr-menu ul.hfe-nav-menu::before,.hbr-menu ul.hfe-nav-menu::after{display:none;content:none}'
    '.hbr-menu li{font-size:inherit;width:auto;position:static;background:none;border:0}'
    '.hbr-menu a.hfe-menu-item,.hbr-menu .hbr-nav-l a{text-decoration:none;display:inline-flex;align-items:center;min-height:44px;'
    'white-space:nowrap;font:inherit;line-height:inherit;letter-spacing:inherit;text-transform:none;color:inherit;border:0;background:none;'
    'justify-content:flex-start;transform:none}'
    '.hbr-menu a.hfe-menu-item::before,.hbr-menu a.hfe-menu-item::after{display:none;content:none}'
    '.hbr-menu a.hfe-menu-item:hover,.hbr-menu .hbr-nav-l a:hover{text-decoration:underline;color:var(--inchiostro)}'
    '.hbr-tel a{font-size:15px;text-decoration:none;font-weight:520;display:flex;align-items:center;min-height:44px;white-space:nowrap}'
    '@media (max-width:1000px){'
    '.hbr-testa{flex-wrap:wrap}'
    '.hbr-testa>.hbr-menu{order:3;flex:0 0 calc(100% + 2 * var(--m));margin:0 calc(-1 * var(--m));padding:0 var(--m);'
    'overflow-x:auto;scrollbar-width:none}'
    '.hbr-menu::-webkit-scrollbar{display:none}'
    # in Ultimate Addons la riga è tre livelli più giù (div, div e nav): anche loro larghi quanto le voci, così la riga
    # scorre fino al margine destro come nella pagina statica
    '.hbr-menu>.elementor-widget-container,.hbr-menu div.hfe-nav-menu,.hbr-menu nav.hfe-nav-menu__layout-horizontal{width:max-content}'
    '.hbr-menu ul.hfe-nav-menu,.hbr-menu .hbr-nav-l{gap:22px;width:max-content}}'
    '@media (max-width:700px){.hbr-testa{padding-top:4px}'
    f'{ht(".hbr-marchio")}{{font-size:22px}}}}'
)


def header():
    marchio = H('HAMBRO', level='div', style='marchio', color=CUOIO, link='/', css='hbr-marchio')
    menu = MENU(VOCI_MENU, colore=INCHIOSTRO, colore_hover=INCHIOSTRO, accento=INCHIOSTRO, fondo_menu=CARTA,
                linea='rgba(27,23,20,.18)', stile='nav', spazio=0, pad_h=0, pad_v=0, distanza=0, align_menu='left',
                slug='menu-hambro', dropdown='none', css='hbr-menu')
    tel = TX(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', 'hbr-tel', style='nav')
    # Ultimate Addons fa scorrere la pagina in 800 ms fino alle ancore del menu; nella pagina statica il salto è immediato:
    # il clic sulle voci che puntano a questa stessa pagina non arriva al suo script (il collegamento funziona come un link normale)
    globali = RAW("<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.hbr-menu a[href*=\"#\"]');"
                  "if(a&&a.pathname===location.pathname)e.stopPropagation()},true)</script>",
                  css=imp(css_base('.hbr-testa') + CSS_TESTATA))
    # solo in Elementor: il carattere (nel fallback il <link> lo scrive già il motore)
    caratteri = RAW(f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="{GOOGLE_FONTS}">',
                    solo_elementor=True)
    # i due widget HTML stanno fuori dalla riga (posizione assoluta): non aggiungono spazio tra le voci
    fuori = C(globali, caratteri, boxed=False, css='hbr-fuori')
    return C(marchio, menu, tel, fuori, dir='row', align='center', justify='between', gap=24, boxed=False, pad=0,
             tag='header', css='hbr-testa hbr-sito')


# =============================================================================================
# PIEDE (template "Hambro: Footer")
# =============================================================================================
CSS_PIEDE = (
    '.hbr-piede{background:var(--inchiostro);color:#CFC6B8;padding:56px 0;font-size:15px;line-height:1.6;display:block;'
    'width:auto;max-width:none;margin:0}'
    '.hbr-piede .hbr-piede-marchio{grid-column:1/4;align-self:start}'
    f'{ht(".hbr-piede-marchio")}{{font-stretch:125%;font-weight:640;font-size:22px;letter-spacing:.14em;line-height:1;color:var(--carta)}}'
    '.hbr-piede .hbr-col{grid-column:span 3}'
    '.hbr-piede .hbr-col p{text-wrap:wrap}'
    '.hbr-piede a{text-decoration:none;color:inherit}'
    # il marchio del piede è un blocco largo quanto la colonna, come nella statica (stesso riquadro del fuoco)
    '.hbr-piede .hbr-piede-marchio a{display:block;color:var(--carta)}'
    '.hbr-piede a:hover,.hbr-piede .hbr-piede-marchio a:hover{color:var(--carta);text-decoration:underline}'
    '@media (max-width:1100px){.hbr-piede .hbr-piede-marchio{grid-column:1/13;margin-bottom:24px}.hbr-piede .hbr-col{grid-column:span 4}}'
    '@media (max-width:700px){.hbr-piede .hbr-col{grid-column:1/13;margin-bottom:18px}}'
)


def footer():
    def col(html):
        return TX(f'<p>{html}</p>', 'hbr-col', style='piede', color=PIEDE_TESTO)
    griglia = C(
        H('HAMBRO', level='div', style='marchio', color=CARTA, link='/', css='hbr-piede-marchio'),
        col("Hambro srl<br>via dell'Artigianato, 30<br>30030 Vigonovo (Venezia)"),
        col(f'Tel. <a href="{TEL_LINK}">{TEL}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{FACEBOOK}">Facebook</a>'),
        col(f'P.IVA {PIVA}<br><a href="#">Informativa privacy</a>'),
        STILE(css_base('.hbr-piede') + CSS_PIEDE),
        boxed=False, css='hbr-griglia')
    return C(griglia, tag='footer', boxed=False, pad=0, bg=INCHIOSTRO, css='hbr-piede hbr-sito')


# =============================================================================================
# HOME
# =============================================================================================
SCRIPT = open(os.path.join(QUI, 'banco.js'), encoding='utf-8').read()

CSS_BOTTONE = (
    '.hbr-bottone a{display:flex;align-items:center;min-height:44px;background:var(--cuoio);color:var(--carta);text-decoration:none;'
    'padding:0 22px;font-family:inherit;font-weight:540;font-size:15px;line-height:1;letter-spacing:inherit;text-transform:none;'
    'border:0;border-radius:0;fill:currentColor;width:auto;transition:background-color .18s,color .18s}'
    '.hbr-bottone a:focus,.hbr-bottone a:visited{background:var(--cuoio);color:var(--carta)}'
    '.hbr-bottone a:hover{background:var(--inchiostro);color:var(--carta)}'
    '.hbr-bottone .elementor-button-content-wrapper,.hbr-bottone .elementor-button-text{display:contents}'
)

CSS_APERTURA = (
    '.hbr-apertura{position:relative;height:900px;max-height:100svh;min-height:680px;overflow:hidden;display:block;'
    'padding:0;width:auto;max-width:none;margin:0}'
    '@media (min-height:1000px){.hbr-apertura{height:1000px;max-height:none}}'
    '.hbr-apertura .hbr-foto,.hbr-apertura .hbr-foto img{position:absolute;inset:0;width:100%;height:100%;max-width:none;'
    'object-fit:cover;object-position:62% 70%}'
    '.hbr-apertura .hbr-foto{display:block}'
    '.hbr-foto>*{position:static;height:auto}'
    '.hbr-foto>.hbr-foto-t,.hbr-foto>.hbr-foto-m{display:none}'
    '.hbr-apertura .hbr-testo{position:relative;z-index:2;padding:clamp(120px,17vh,170px) var(--m) 0;display:block}'
    '.hbr-apertura h1{font-size:clamp(46px,9.45vw,136px);line-height:.92;letter-spacing:-.04em;font-weight:380;max-width:7.4em}'
    '.hbr-apertura .hbr-lede{margin-top:34px;max-width:27em;font-size:17px;line-height:1.5;color:#2D2622}'
    '.hbr-apertura .hbr-azione{margin-top:26px;display:flex;flex-direction:row;gap:6px 28px;flex-wrap:wrap;align-items:center;font-size:15px}'
    '.hbr-azione>*{flex:0 1 auto;width:auto}'
    '.hbr-apertura .hbr-mail a{display:flex;align-items:center;min-height:44px}'
    '.hbr-didascalie{position:absolute;z-index:3;left:var(--m);right:var(--m);bottom:128px;display:flex;flex-direction:row;'
    'flex-wrap:nowrap;justify-content:space-between;align-items:last baseline;gap:40px;width:auto}'
    '.hbr-didascalie>*{flex:0 1 auto;width:auto}'
    '.hbr-didascalie>.hbr-dida-sx{max-width:18em}'
    '.hbr-didascalie>.hbr-dida-dx{text-align:right;max-width:17em}'
    '.hbr-righello{position:absolute;left:0;right:0;bottom:32px;height:76px;z-index:3}'
    '.hbr-righello svg{display:block;width:100%;height:100%}'
    '.hbr-rt{font-family:"Mona Sans",sans-serif;font-size:13px;font-weight:500;font-stretch:112%}'
    '.hbr-rt.c{font-weight:620}'
    + CSS_BOTTONE +
    '@media (max-width:1100px){'
    '.hbr-foto>.hbr-foto-d{display:none}.hbr-foto>.hbr-foto-t{display:block}'
    '.hbr-apertura .hbr-foto img{object-position:100% 50%}'
    '.hbr-apertura .hbr-lede{max-width:22em}'
    '.hbr-didascalie{display:none}}'
    '@media (max-width:900px){'
    '.hbr-apertura .hbr-azione{flex-direction:column;align-items:flex-start}'
    '.hbr-righello{bottom:12px}}'
    '@media (max-width:700px){'
    '.hbr-foto>.hbr-foto-t{display:none}.hbr-foto>.hbr-foto-m{display:block}'
    '.hbr-apertura{height:auto;min-height:0;max-height:none;overflow:visible;display:flex;flex-direction:column}'
    '.hbr-apertura .hbr-testo{padding-top:112px;order:1}'
    '.hbr-apertura h1{font-size:clamp(40px,13.6vw,60px);line-height:.92;letter-spacing:-.04em}'
    '.hbr-apertura .hbr-lungo{display:none}'
    '.hbr-apertura .hbr-lede{margin-top:16px}'
    '.hbr-apertura .hbr-azione{margin-top:14px;flex-direction:row;align-items:center;gap:0 20px}'
    '.hbr-apertura .hbr-bottone a{padding:0 18px}'
    '.hbr-apertura .hbr-foto{position:relative;order:2;display:block;margin-top:16px;height:auto;inset:auto}'
    '.hbr-apertura .hbr-foto img{position:relative;inset:auto;height:auto;aspect-ratio:1460/1360;object-position:50% 50%}'
    '.hbr-righello{position:relative;order:3;bottom:auto;height:48px;background:var(--carta)}}'
)


def apertura():
    alt = 'Fibbia dorata ad ardiglione con borchie a piramide, smontata su carta bianca, in pieno sole'
    foto = C(I(img('apertura-2400.jpg'), alt, css='hbr-foto-d'),
             I(img('apertura-t-1600.jpg'), alt, css='hbr-foto-t'),
             I(img('apertura-m-1170.jpg'), alt, css='hbr-foto-m'),
             boxed=False, css='hbr-foto')
    testo = C(
        H('Fibbie, lacci e rinforzi', level='h1', style='h1', color=INCHIOSTRO, css='hbr-h1'),
        TX('<p>Minuteria in zama, ferro e ottone, lacci in pelle da&nbsp;mm2 a&nbsp;mm60, nastri, fodere e rinforzi per borse, '
           'cinture, calzature e&nbsp;capi.<span class="hbr-lungo"> Da&nbsp;Vigonovo, Venezia.</span></p>', 'hbr-lede',
           style='lede', color='#2D2622'),
        C(B(f'Prova le misure<span class="hbr-lungo">, mm&nbsp;2{WJ}-{WJ}60</span>', '#lacci', variant='cuoio', css='hbr-bottone'),
          TX(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>', 'hbr-mail', style='small'),
          dir='row', wrap=True, align='center', gap=28, boxed=False, css='hbr-azione'),
        boxed=False, css='hbr-testo')
    didascalie = C(
        TX('<p><b>Scala 1:1</b>Righello in millimetri. In cuoio le misure a catalogo: lacci e tondini da&nbsp;2 a&nbsp;4, '
           'tubolari fino a&nbsp;16, nastri da&nbsp;20 a&nbsp;50, strisce e fibbie fino a&nbsp;60.</p>',
           'hbr-didascalia hbr-dida-sx', style='didascalia', color=GRIGIO),
        TX('<p><b>Tav. 1</b>Fibbia ad ardiglione con borchie a&nbsp;piramide, finitura oro.</p>',
           'hbr-didascalia hbr-dida-dx', style='didascalia', color=GRIGIO),
        dir='row', justify='between', align='baseline', gap=40, boxed=False, css='hbr-didascalie')
    righello = CNT(RAW('<div class="hbr-righello" data-righello aria-hidden="true"></div>',
                       css=imp(css_base('.hbr-apertura') + CSS_APERTURA)))
    # id content: è la destinazione del collegamento "Salta al contenuto principale" di Ultimate Addons
    return C(foto, testo, didascalie, righello, boxed=False, pad=0, tag='section', anchor='content', css='hbr-apertura hbr-sito')


CSS_BANCO = (
    '.hbr-banco{--n:30;background:var(--campo);color:var(--campo-testo);padding:104px 0 48px;position:relative;display:block;'
    'width:auto;max-width:none;margin:0}'
    '.hbr-banco a:hover{color:var(--oro)}'
    '.hbr-banco .hbr-banco-h2{grid-column:1/7}'
    '.hbr-banco .hbr-intro{grid-column:1/6;margin-top:24px;color:var(--campo-tenue);max-width:30em}'
    '.hbr-lettura{grid-column:7/13;grid-row:1/3;align-self:end;justify-self:end;text-align:right}'
    '.hbr-lettura .hbr-valore{display:flex;align-items:flex-start;justify-content:flex-end;gap:10px;font-stretch:125%;font-weight:250;'
    'font-size:clamp(104px,15.5vw,232px);line-height:.8;letter-spacing:-.04em}'
    '.hbr-lettura .hbr-valore small{font-size:32px;font-weight:500;letter-spacing:.02em;margin-top:.35em}'
    '.hbr-lettura .hbr-cosa{margin-top:18px;font-size:15px;color:var(--campo-tenue);max-width:24em;margin-left:auto}'
    '.hbr-comandi{grid-column:1/13;margin-top:48px;display:flex;flex-wrap:wrap;align-items:center;gap:20px 48px}'
    '.hbr-scelte{display:flex;flex-wrap:wrap;border:1px solid rgba(242,237,228,.45);min-width:min-content}'
    '.hbr-scelte label{position:relative;cursor:pointer;display:block}'
    '.hbr-scelte input{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer;width:100%;height:100%}'
    '.hbr-scelte span{display:flex;align-items:center;justify-content:center;min-height:44px;padding:0 18px;font-size:15px;line-height:1.1;'
    'transition:background-color .18s,color .18s}'
    '.hbr-scelte label+label span{border-left:1px solid rgba(242,237,228,.45)}'
    '.hbr-scelte label:hover span{background:#7E4223}'
    '.hbr-scelte input:checked+span{background:var(--carta);color:var(--inchiostro)}'
    '.hbr-scelte input:focus-visible+span{outline:2px solid var(--oro);outline-offset:2px}'
    '.hbr-colori{display:flex;gap:12px;border:0}'
    '.hbr-colori label{position:relative;width:36px;height:36px;cursor:pointer;margin:4px 0;display:block}'
    '.hbr-colori input{position:absolute;inset:0;opacity:0;margin:0;cursor:pointer;width:100%;height:100%}'
    '.hbr-colori span{position:absolute;inset:0;background:var(--c);box-shadow:inset 0 0 0 1px rgba(0,0,0,.2);transition:box-shadow .15s}'
    '.hbr-colori label:hover span{box-shadow:inset 0 0 0 1px rgba(0,0,0,.2),0 0 0 2px rgba(242,237,228,.5)}'
    '.hbr-colori input:checked+span{box-shadow:inset 0 0 0 1px rgba(0,0,0,.2),0 0 0 2px var(--campo),0 0 0 4px var(--carta)}'
    '.hbr-colori input:focus-visible+span{outline:2px solid var(--oro);outline-offset:5px}'
    '.hbr-banco [hidden]{display:none}'
    '.hbr-regolo{display:flex;align-items:center;gap:16px;font-size:15px;flex:1 1 360px;max-width:560px;min-width:0}'
    '.hbr-pista{position:relative;flex:1;height:44px}'
    '.hbr-tacche{position:absolute;left:12px;right:12px;top:50%;height:0;pointer-events:none}'
    '.hbr-tacche i{position:absolute;top:-7px;width:1px;height:14px;background:rgba(242,237,228,.55)}'
    '.hbr-regolo input{-webkit-appearance:none;appearance:none;position:relative;display:block;width:100%;height:44px;margin:0;'
    'padding:0;border:0;background:transparent;cursor:pointer;box-shadow:none}'
    '.hbr-regolo input::-webkit-slider-runnable-track{height:2px;background:rgba(242,237,228,.3);border:0}'
    '.hbr-regolo input::-moz-range-track{height:2px;background:rgba(242,237,228,.3);border:0}'
    '.hbr-regolo input::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;width:24px;height:24px;margin-top:-11px;border-radius:50%;'
    'background:var(--carta);border:0;box-shadow:0 2px 0 var(--taglio);transition:background-color .15s}'
    '.hbr-regolo input::-moz-range-thumb{width:24px;height:24px;border-radius:50%;background:var(--carta);border:0;box-shadow:0 2px 0 var(--taglio)}'
    '.hbr-regolo input:hover::-webkit-slider-thumb{background:#fff}'
    '.hbr-regolo input:focus{outline:none;box-shadow:none}'
    '.hbr-regolo input:focus-visible::-webkit-slider-thumb{box-shadow:0 0 0 3px var(--campo),0 0 0 5px var(--oro)}'
    '.hbr-regolo input:focus-visible::-moz-range-thumb{box-shadow:0 0 0 3px var(--campo),0 0 0 5px var(--oro)}'
    # il tavolo è alto quanto la striscia più 48 px: nessun campo vuoto sopra e sotto
    '.hbr-tavolo{position:relative;margin-top:32px;height:calc(var(--n) * var(--u) + 48px);display:flex;align-items:center;'
    'transition:height .2s ease-out}'
    '.hbr-striscia{position:relative;width:100%;height:calc(var(--n) * var(--u));transition:height .2s ease-out;'
    'border-top:1px solid var(--taglio);border-bottom:1px solid var(--taglio);box-shadow:0 6px 8px rgba(28,10,0,.38)}'
    '.hbr-striscia.vivo{background:url(@CUOIO@) 30% 50%/cover no-repeat}'
    '.hbr-striscia.tubo{background:linear-gradient(180deg,rgba(30,12,2,.7) 0%,rgba(30,12,2,.15) 20%,rgba(255,232,205,.22) 38%,'
    'rgba(255,232,205,0) 54%,rgba(30,12,2,.22) 78%,rgba(30,12,2,.75) 100%),url(@CUOIO@) 60% 50%/cover no-repeat}'
    '.hbr-striscia.nastro{background:repeating-linear-gradient(90deg,rgba(0,0,0,.09) 0 1px,transparent 1px 3px),'
    'repeating-linear-gradient(0deg,rgba(255,255,255,.07) 0 1px,transparent 1px 2px),var(--c);border-color:rgba(0,0,0,.35)}'
    '.hbr-sotto{grid-column:1/13;margin-top:16px;display:flex;flex-direction:row;flex-wrap:wrap;justify-content:space-between;'
    'align-items:baseline;gap:0 40px;font-size:13px;color:var(--campo-tenue)}'
    '.hbr-sotto>*{flex:0 1 auto;width:auto}'
    '.hbr-sotto .hbr-sotto-p p{padding:12px 0}'
    '.hbr-taratura summary{cursor:pointer;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.22em;'
    'list-style:none;padding:12px 0;display:list-item}'
    '.hbr-taratura summary::-webkit-details-marker{display:none}'
    '.hbr-taratura summary:hover{color:var(--carta)}'
    '.hbr-sotto>.hbr-taratura[open]{flex-basis:100%}'
    '.hbr-taratura .hbr-corpo{margin-top:14px;display:flex;flex-wrap:wrap;gap:24px 40px;align-items:center}'
    '.hbr-tessera{width:calc(85.6 * var(--u));height:calc(53.98 * var(--u));border:1px dashed var(--carta);'
    'border-radius:calc(3.2 * var(--u));display:flex;align-items:flex-end;padding:10px;font-size:13px;color:var(--carta);flex:none;max-width:100%}'
    '.hbr-taratura .hbr-regolo{max-width:380px}'
    '@media (max-width:900px){'
    '.hbr-banco .hbr-banco-h2,.hbr-banco .hbr-intro{grid-column:1/13}'
    '.hbr-lettura{grid-column:1/13;grid-row:auto;justify-self:start;text-align:left;margin-top:40px}'
    '.hbr-lettura .hbr-valore{justify-content:flex-start}'
    '.hbr-lettura .hbr-valore small{font-size:22px}'
    '.hbr-lettura .hbr-cosa{margin-left:0}}'
    '@media (max-width:700px){'
    '.hbr-banco{padding-top:80px}'
    '.hbr-comandi{margin-top:36px;gap:20px}'
    '.hbr-scelte{width:100%}'
    '.hbr-scelte label{flex:1 1 auto}'
    '.hbr-scelte span{padding:0 10px}'
    '.hbr-regolo{flex-basis:100%}}'
    '@media (max-width:360px){'
    '.hbr-scelte span{padding:0 6px;font-size:13px}'
    '.hbr-colori{gap:8px}'
    '.hbr-colori label{width:32px;height:32px}}'
)

HTML_LETTURA = (
    '<div class="hbr-lettura" aria-live="polite">'
    '<p class="hbr-valore"><small>mm</small><span data-valore>30</span></p>'
    '<p class="hbr-cosa" data-cosa>Striscia in pelle a taglio vivo, da mm2 a mm60</p>'
    '</div>'
    '<div class="hbr-comandi">'
    '<fieldset class="hbr-scelte"><legend class="hbr-nascosto">Materiale</legend>'
    '<label><input type="radio" name="mat" value="vivo" checked><span>Taglio vivo</span></label>'
    '<label><input type="radio" name="mat" value="tubo"><span>Tubolare</span></label>'
    '<label><input type="radio" name="mat" value="nastro"><span>Nastro</span></label>'
    '</fieldset>'
    '<div class="hbr-regolo" data-regolo><span data-min>2</span>'
    '<div class="hbr-pista"><div class="hbr-tacche" data-tacche></div><input type="range" min="2" max="60" step="1" value="30" '
    'aria-label="Larghezza in millimetri" aria-valuetext="30 millimetri" data-range></div>'
    '<span data-max>60</span></div>'
    '<fieldset class="hbr-scelte" data-misure-nastro hidden><legend class="hbr-nascosto">Larghezza del nastro in millimetri</legend>'
    + ''.join(f'<label><input type="radio" name="mn" value="{v}"{" checked" if v == 30 else ""}><span>{v}</span></label>'
              for v in (20, 25, 30, 40, 50)) +
    '</fieldset>'
    '<fieldset class="hbr-colori" data-colori hidden><legend class="hbr-nascosto">Colore del nastro</legend>'
    + ''.join(f'<label title="{n}"><input type="radio" name="col" value="{c}" aria-label="{n}"{" checked" if i == 0 else ""}>'
              f'<span style="--c:{c}"></span></label>'
              for i, (n, c) in enumerate([('Rosso', '#C9433E'), ('Giallo', '#E9BC2A'), ('Salvia', '#AEB887'), ('Viola', '#6A4378'),
                                          ('Grigio', '#8C8780'), ('Nero', '#25221D')])) +
    '</fieldset>'
    '</div>'
)

HTML_TAVOLO = ('<div class="hbr-tavolo"><div class="hbr-striscia vivo" data-striscia style="--c:#C9433E" role="img" '
               'aria-label="Striscia in pelle a taglio vivo: 30 millimetri"></div></div>')

HTML_TARATURA = (
    '<details class="hbr-taratura"><summary>La misura non torna? Tara lo schermo</summary>'
    '<div class="hbr-corpo"><div class="hbr-tessera">Appoggia qui una tessera sanitaria o un bancomat</div>'
    '<div class="hbr-regolo"><span>più piccola</span><div class="hbr-pista"><input type="range" min="0.5" max="1.8" step="0.005" '
    'value="1" aria-label="Taratura della scala" data-k></div><span>più grande</span></div></div></details>'
)


def banco():
    griglia = C(
        H('Lacci e nastri in scala 1:1', level='h2', style='h2', color=CARTA, css='hbr-h2 hbr-banco-h2'),
        TX('<p>Scegli il materiale e la misura: la striscia qui sotto prende la larghezza vera. Il laccio in pelle lo facciamo '
           'tubolare, piatto, cucito o a taglio vivo, e su richiesta anche a campione.</p>', 'hbr-intro', color=CAMPO_TENUE),
        CNT(RAW(HTML_LETTURA)),
        boxed=False, css='hbr-griglia')
    tavolo = CNT(RAW(HTML_TAVOLO))
    css = imp(css_base('.hbr-banco') + CSS_BANCO).replace('@CUOIO@', img('banco-cuoio.jpg'))
    sotto = C(C(
        TX('<p>Nastri in cotone e poliestere per tracolle e cinture: mm20, 25, 30, 40 e&nbsp;50.</p>', 'hbr-sotto-p',
           style='didascalia', color=CAMPO_TENUE),
        CNT(RAW(HTML_TARATURA + f'<script>{SCRIPT}</script>', css=css)),
        dir='row', wrap=True, justify='between', align='baseline', gap=40, boxed=False, css='hbr-sotto'),
        boxed=False, css='hbr-griglia')
    return C(griglia, tavolo, sotto, boxed=False, pad=0, bg=CAMPO, anchor='lacci', tag='section', css='hbr-banco hbr-sito')


CSS_CAMPIONARIO = (
    '.hbr-campionario{padding:132px 0 120px;display:block;width:auto;max-width:none;margin:0}'
    '.hbr-capo{grid-column:1/13;display:flex;flex-direction:row;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;'
    'gap:24px 48px;margin-bottom:56px}'
    '.hbr-capo>*{flex:0 1 auto;width:auto}'
    '.hbr-capo>.hbr-capo-h2{max-width:9em}'
    '.hbr-capo>.hbr-capo-p{max-width:29em;color:var(--grigio)}'
    '.hbr-cassetto{grid-column:1/13;display:block}'
    '.hbr-fila{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--hbr-gap);border-top:1px solid var(--inchiostro);'
    'padding:16px 0 32px}'
    '.hbr-fila>.hbr-fila-h3{grid-column:1/4}'
    f'{ht(".hbr-fila-h3")}{{font-size:22px;line-height:1.2;letter-spacing:-.01em}}'
    '.hbr-vano{grid-column:span 3;display:flex;flex-direction:column}'
    '.hbr-vano .hbr-n{font-size:13px;color:var(--grigio)}'
    '.hbr-vano img{width:100%;aspect-ratio:560/360;object-fit:cover;margin:0 0 8px;mix-blend-mode:multiply}'
    f'{ht(".hbr-vano-h4")}{{font-size:17px;line-height:1.25;font-weight:500}}'
    '.hbr-vano .hbr-vano-p{font-size:15px;color:var(--grigio);margin-top:2px}'
    '.hbr-fila.hbr-fuori{padding-bottom:0}'
    '.hbr-fuori .hbr-fuori-ul{grid-column:4/13}'
    '.hbr-fuori ul{list-style:none;font-size:15px;line-height:1.45;columns:2;column-gap:var(--hbr-gap)}'
    '.hbr-fuori li{padding:0 0 10px;break-inside:avoid}'
    '.hbr-fuori .hbr-chiedi{grid-column:4/13;margin-top:20px;font-size:15px}'
    '.hbr-fuori .hbr-chiedi a{display:inline-flex;align-items:center;min-height:44px}'
    '@media (max-width:700px){'
    '.hbr-campionario{padding-top:88px;padding-bottom:72px}'
    '.hbr-fila{padding:12px 0 24px}'
    '.hbr-fila>.hbr-fila-h3{grid-column:1/13;margin-bottom:12px}'
    '.hbr-vano{grid-column:span 4}'
    f'{ht(".hbr-vano-h4")}{{font-size:15px}}'
    '.hbr-vano .hbr-vano-p{font-size:13px}'
    '.hbr-fuori .hbr-fuori-ul,.hbr-fuori .hbr-chiedi{grid-column:1/13}'
    '.hbr-fuori ul{columns:1}}'
)

CASSETTO = [
    ('Moschettoni', [('01', 'moschettoni-tondo', 'Anello tondo', 'Zama'),
                     ('02', 'moschettoni-ovale', 'Anello ovale', 'Zama, ferro, ottone'),
                     ('03', 'moschettoni-rettangolare', 'Anello rettangolare', 'Zama')]),
    ('Anelli e fibbie', [('04', 'mezzi-anelli', 'Mezzi anelli', 'Ferro, zama'),
                         ('05', 'anelli', 'Anelli tondi e rettangolari', 'Varie forme e materiali'),
                         ('06', 'fibbie-doppie', 'Fibbie doppie', 'Anche per calzature')]),
    ('Attacchi', [('07', 'attacchi-spinetta', 'Con spinetta', 'Zama'),
                  ('08', 'attacco-alette', 'Con alette', 'Zama')]),
    ('Chiusure', [('09', 'chiusure-pulsante', 'A pulsante', 'Zama'),
                  ('10', 'chiusure-girello', 'A girello', 'Zama'),
                  ('11', 'chiusure-battente', 'A battente', 'Zama')]),
]


def campionario():
    capo = C(
        H('Minuteria metallica', level='h2', style='h2', color=INCHIOSTRO, css='hbr-h2 hbr-capo-h2'),
        TX("<p>Undici famiglie dal cassetto, in zama, ferro e ottone. Su ordinazione si possono avere varie finiture; qui c'è solo "
           "una parte di quello che è disponibile.</p>", 'hbr-capo-p', color=GRIGIO),
        dir='row', wrap=True, justify='between', align='end', gap=48, boxed=False, css='hbr-capo')
    file = []
    for famiglia, vani in CASSETTO:
        figli = [H(famiglia, level='h3', style='h3', color=INCHIOSTRO, css='hbr-fila-h3')]
        for n, foto, nome, materiale in vani:
            figli.append(C(
                TX(f'<p>{n}</p>', 'hbr-n', style='didascalia', color=GRIGIO),
                I(img(f'cat/{foto}.jpg'), f'{famiglia}: {nome.lower()}', css='hbr-vano-img'),
                H(nome, level='h4', style='h4', color=INCHIOSTRO, css='hbr-vano-h4'),
                TX(f'<p>{materiale}</p>', 'hbr-vano-p', style='small', color=GRIGIO),
                boxed=False, css='hbr-vano'))
        file.append(C(*figli, boxed=False, css='hbr-fila'))
    file.append(C(
        H('Fuori dal cassetto', level='h3', style='h3', color=INCHIOSTRO, css='hbr-fila-h3'),
        TX('<ul><li>Cerniere dorate o nichelate</li><li>Scheletri, salpe e rinforzi per borse</li><li>Fodere tinta unita e stampate</li>'
           '<li>Nappe e vitelli lavabili, sp.&nbsp;0,7 e&nbsp;1,1</li>'
           '<li>Accessori in legno e bambù, in plastica e metallo nichel free, con strass</li></ul>', 'hbr-fuori-ul', style='small'),
        TX(f'<p><a href="{CAMPIONI}">Chiedi un campione</a></p>', 'hbr-chiedi', style='small'),
        boxed=False, css='hbr-fila hbr-fuori'))
    griglia = C(capo, C(*file, boxed=False, css='hbr-cassetto'),
                STILE(css_base('.hbr-campionario') + CSS_CAMPIONARIO), boxed=False, css='hbr-griglia')
    return C(griglia, boxed=False, pad=0, anchor='minuteria', tag='section', css='hbr-campionario hbr-sito')


CSS_TAV2 = (
    '.hbr-tav2{padding-top:24px;padding-bottom:132px;align-items:start;width:auto;max-width:none;margin:0}'
    '.hbr-tav2 .hbr-b1{grid-column:4/7;justify-self:end;width:100%;max-width:360px}'
    '.hbr-tav2 .hbr-b2{grid-column:7/10;width:100%;max-width:360px}'
    '.hbr-tav2 img{width:100%;max-width:360px;aspect-ratio:2/3;object-fit:cover}'
    '.hbr-tav2 .hbr-tav2-dida{grid-column:4/10;margin-top:14px}'
    '.hbr-tav2 .hbr-tav2-dida p{display:flex;justify-content:space-between;flex-wrap:wrap;gap:4px 24px;text-wrap:wrap}'
    '@media (max-width:1100px){.hbr-tav2 .hbr-b1{grid-column:3/7}.hbr-tav2 .hbr-b2{grid-column:7/11}.hbr-tav2 .hbr-tav2-dida{grid-column:3/11}}'
    '@media (max-width:700px){.hbr-tav2{padding-bottom:88px}.hbr-tav2 .hbr-b1{grid-column:1/7}.hbr-tav2 .hbr-b2{grid-column:7/13}'
    '.hbr-tav2 .hbr-tav2-dida{grid-column:1/13}.hbr-tav2 .hbr-tav2-dida p{flex-direction:column}}'
)


def tav2():
    return C(
        I(img('bobina-laccio-720.jpg'), 'Bobina di laccio in cuoio a taglio vivo: il fiore scuro e il taglio chiaro in giri fitti',
          css='hbr-b1'),
        I(img('bobina-tondino-720.jpg'), 'Bobina di tondino in pelle color cipria, giri affiancati', css='hbr-b2'),
        TX('<p><span><b>Tav. 2</b>In bobina, dal magazzino Hambro: laccio in cuoio a taglio vivo e tondino in pelle.</span>'
           '<span>Per i nastri siamo rappresentanti Satab: organza e vichy.</span></p>', 'hbr-didascalia hbr-tav2-dida',
           style='didascalia', color=GRIGIO),
        STILE(css_base('.hbr-tav2') + CSS_TAV2),
        boxed=False, pad=0, css='hbr-tav2 hbr-griglia hbr-sito')


CSS_RICOPERTURA = (
    '.hbr-ricopertura{padding:0;display:block;width:auto;max-width:none;margin:0}'
    '.hbr-ric-titolo{grid-column:1/8;margin-bottom:48px;display:block}'
    '.hbr-ricopertura .hbr-ric-intro{margin-top:20px;max-width:30em;color:var(--grigio)}'
    '.hbr-ric-fig,.hbr-semi-fig{display:block}'
    '.hbr-dittico{display:grid;grid-template-columns:1fr 1fr;position:relative}'
    '.hbr-dittico img{width:100%;height:100%;object-fit:cover}'
    '.hbr-prova{height:min(820px,62vw)}'
    '.hbr-prova>.hbr-metallo,.hbr-prova>.hbr-pelle{height:100%;overflow:hidden;display:block}'
    '.hbr-metallo>*,.hbr-pelle>*{height:100%}'
    '.hbr-prova .hbr-filo{position:absolute;top:0;bottom:0;left:50%;width:2px;margin-left:-1px;background:var(--cuoio);z-index:2}'
    '.hbr-prova .hbr-metallo img{object-position:30% 45%}'
    '.hbr-sagome{position:absolute;left:50%;bottom:clamp(40px,7vw,96px);z-index:3;width:0;height:0}'
    '.hbr-sagoma{position:absolute;bottom:0;left:calc(var(--w) * var(--u) / -2);width:calc(var(--w) * var(--u));'
    'height:calc(var(--w) * .62 * var(--u));border-radius:calc(7 * var(--u))}'
    '.hbr-sagoma .l{position:absolute;inset:0;border:2px solid;border-radius:inherit}'
    '.hbr-sagoma .l.sx{color:var(--inchiostro);clip-path:inset(-2px 50% -2px -2px)}'
    '.hbr-sagoma .l.dx{color:var(--carta);clip-path:inset(-2px -2px -2px 50%)}'
    '.hbr-sagoma b{position:absolute;right:calc(3 * var(--u));top:calc(1.4 * var(--u));font-size:13px;font-weight:600;font-stretch:112%;'
    'color:var(--carta);line-height:1}'
    '.hbr-ricopertura .hbr-dida{padding:14px var(--m) 0;max-width:none}'
    # nella statica le didascalie sono figcaption, non paragrafi: niente text-wrap:pretty
    '.hbr-ricopertura .hbr-dida p{text-wrap:wrap}'
    '.hbr-ricopertura .hbr-ric-testo{grid-column:1/7;margin-top:56px}'
    '.hbr-misure{grid-column:8/13;margin-top:56px;align-self:start}'
    '.hbr-misure dl{display:grid;grid-template-columns:auto 1fr;gap:0 28px;font-size:15px}'
    '.hbr-misure dt,.hbr-misure dd{padding:7px 0}'
    '.hbr-misure dt{color:var(--grigio)}'
    '.hbr-semilavorati{padding-top:80px;display:block}'
    # nella statica anche questo blocco è un ".ricopertura .testo": prende il suo margine di 56 px
    '.hbr-semi-testo{grid-column:1/7;margin-top:56px;margin-bottom:40px;display:block}'
    f'{ht(".hbr-semi-h3")}{{font-size:clamp(22px,2.3vw,32px);line-height:1.1;letter-spacing:-.02em;font-stretch:112%;font-weight:340}}'
    '.hbr-semi-testo>.hbr-semi-h3{margin-bottom:16px}'
    '.hbr-semi-fig img{width:100%}'
    '.hbr-semi-fig>.hbr-semi-m{display:none}'
    '@media (max-width:1100px){.hbr-ric-titolo{grid-column:1/13;margin-bottom:24px}}'
    '@media (max-width:900px){.hbr-ricopertura .hbr-ric-testo,.hbr-misure,.hbr-semi-testo{grid-column:1/13}'
    '.hbr-prova{height:auto;aspect-ratio:390/330}}'
    '@media (max-width:700px){.hbr-prova{aspect-ratio:390/360}.hbr-semilavorati{padding-top:72px}'
    '.hbr-semi-fig>.hbr-semi-d{display:none}.hbr-semi-fig>.hbr-semi-m{display:block}}'
)


def ricopertura():
    titolo = C(C(
        H('Ricoperte con il vostro materiale', level='h2', style='h2', color=INCHIOSTRO, css='hbr-h2'),
        TX('<p>Fibbie e bottoni rivestiti in pelle o in tessuto, anche con quello che ci mandate.</p>', 'hbr-ric-intro', color=GRIGIO),
        boxed=False, css='hbr-ric-titolo'), boxed=False, css='hbr-griglia')
    sagome = ''.join(f'<div class="hbr-sagoma" style="--w:{w}"><span class="l sx"></span><span class="l dx"></span><b>{w}</b></div>'
                     for w in (60, 50, 40))
    dittico = C(
        C(I(img('metallo-1170.jpg'), 'Fibbia in metallo dorato, senza rivestimento'), boxed=False, css='hbr-metallo'),
        C(I(img('pelle-1072.jpg'), 'Pelle color cuoio con la grana in evidenza'), boxed=False, css='hbr-pelle'),
        CNT(RAW('<span class="hbr-filo" aria-hidden="true"></span>'
                '<div class="hbr-sagome" role="img" aria-label="Sagome delle fibbie da ricoprire da 60, 50 e 40 millimetri, in scala reale">'
                + sagome + '</div>')),
        boxed=False, css='hbr-dittico hbr-prova')
    figura = C(dittico,
               TX('<p><b>Tav. 3</b>A sinistra il metallo, a destra la pelle. Le sagome sono le fibbie da ricoprire da mm40, 50 '
                  'e&nbsp;60, in scala reale.</p>', 'hbr-didascalia hbr-dida', style='didascalia', color=GRIGIO),
               boxed=False, css='hbr-ric-fig')
    dettagli = C(
        TX('<p>Nel laboratorio ricopriamo fibbie e bottoni con il tessuto o la pelle che ci mandate. Sulla pelle facciamo anche '
           'lavorazioni particolari, dal camouflage al floreale alla stampa cocco.</p>', 'hbr-ric-testo'),
        TX('<dl><dt>Fibbie da ricoprire</dt><dd>mm40, mm50, mm60</dd><dt>Bottoni</dt><dd>Yvette, a pressione e altri da ricoprire</dd>'
           '<dt>Rivestimento</dt><dd>tessuto o pelle, anche vostri</dd>'
           '<dt>Lavorazioni sulla pelle</dt><dd>camouflage, floreale, stampa cocco</dd></dl>', 'hbr-misure', style='small'),
        boxed=False, css='hbr-griglia')
    alt_semi = 'Mani che tracciano un cartamodello su una pelle scamosciata, sul banco di legno'
    semilavorati = C(
        C(C(H('Semilavorati in pelle e tessuto', level='h3', style='h3semi', color=INCHIOSTRO, css='hbr-semi-h3'),
            TX("<p>In laboratorio facciamo componenti semilavorati in pelle e tessuto. Se un articolo non c'è, lo creiamo su vostra "
               "richiesta.</p>", 'hbr-semi-p'),
            boxed=False, css='hbr-semi-testo'), boxed=False, css='hbr-griglia'),
        C(I(img('semilavorati-2400.jpg'), alt_semi, css='hbr-semi-d'), I(img('semilavorati-m-1170.jpg'), alt_semi, css='hbr-semi-m'),
          TX('<p><b>Tav. 4</b>Il banco del taglio: cartamodello e pelle scamosciata.</p>', 'hbr-didascalia hbr-dida',
             style='didascalia', color=GRIGIO),
          boxed=False, css='hbr-semi-fig'),
        boxed=False, css='hbr-semilavorati')
    return C(titolo, figura, dettagli, semilavorati, STILE(css_base('.hbr-ricopertura') + CSS_RICOPERTURA),
             boxed=False, pad=0, anchor='ricopertura', tag='section', css='hbr-ricopertura hbr-sito')


CSS_MESTIERI = (
    '.hbr-mestieri{padding:132px 0;display:block;width:auto;max-width:none;margin:0}'
    '.hbr-mestieri .hbr-mes-h2{grid-column:1/9;margin-bottom:20px}'
    '.hbr-mestieri .hbr-mes-intro{grid-column:1/7;color:var(--grigio);margin-bottom:48px}'
    '.hbr-settori{grid-column:1/13;display:block}'
    '.hbr-settori .hbr-nome{min-width:0}'
    '.hbr-testata-quote,.hbr-li{display:grid;grid-template-columns:minmax(0,1fr) 220px calc(60 * var(--u) + 12px);column-gap:24px;'
    'align-items:center}'
    '.hbr-testata-quote{font-size:13px;color:var(--grigio);padding-bottom:10px}'
    '.hbr-testata-quote .hbr-mis,.hbr-li .hbr-mis{text-align:right;white-space:nowrap}'
    '.hbr-settore{border-top:1px solid var(--inchiostro);padding:14px 0 36px;display:block}'
    f'{ht(".hbr-settore-h3")}{{font-size:22px;letter-spacing:-.01em}}'
    '.hbr-settore>.hbr-settore-h3{margin-bottom:6px}'
    '.hbr-ul{font-size:15px;display:block}'
    '.hbr-li{padding:9px 0}'
    '.hbr-li+.hbr-li{background:linear-gradient(var(--filo),var(--filo)) top/100% 1px no-repeat}'
    '.hbr-li .hbr-mis{color:var(--grigio)}'
    '.hbr-settore .hbr-anche{font-size:15px;color:var(--grigio);padding-top:9px;'
    'background:linear-gradient(var(--filo),var(--filo)) top/100% 1px no-repeat}'
    '.hbr-asse{position:relative;display:block;width:calc(60 * var(--u));height:18px;'
    'background:linear-gradient(rgba(27,23,20,.35),rgba(27,23,20,.35)) left bottom/100% 1px no-repeat,'
    'repeating-linear-gradient(90deg,rgba(27,23,20,.35) 0 1px,transparent 1px calc(10 * var(--u))) left bottom/calc(100% + 1px) 5px no-repeat}'
    '.hbr-asse i{position:absolute;bottom:0;background:var(--cuoio)}'
    '.hbr-asse .da{left:calc(var(--a) * var(--u));width:calc((var(--b) - var(--a)) * var(--u));height:8px}'
    '.hbr-asse .pt{left:calc(var(--a) * var(--u) - 1px);width:2px;height:16px}'
    '.hbr-quote{position:relative;display:block;width:calc(60 * var(--u));height:16px}'
    '.hbr-quote span{position:absolute;bottom:0;transform:translateX(-50%);line-height:1}'
    '.hbr-quote span:first-child{transform:none}'
    '@media (max-width:900px){.hbr-mestieri .hbr-mes-h2,.hbr-mestieri .hbr-mes-intro{grid-column:1/13}'
    '.hbr-testata-quote,.hbr-li{grid-template-columns:minmax(0,1fr) 150px calc(60 * var(--u) + 12px)}}'
    '@media (max-width:700px){.hbr-mestieri{padding-top:88px;padding-bottom:88px}'
    '.hbr-testata-quote{display:flex;justify-content:flex-end}'
    '.hbr-testata-quote .hbr-nome,.hbr-testata-quote .hbr-mis{display:none}'
    '.hbr-li{grid-template-columns:minmax(0,1fr) auto;row-gap:8px}'
    '.hbr-li .hbr-sc{grid-column:1/3;justify-self:end}'
    '.hbr-li .hbr-sc:empty{display:none}}'
)

# (articolo, misura come sul sito, quote sul righello: ('pt', a) tratto, ('da', a, b) barra)
SETTORI = [
    ('Pelletteria', [
        ('Nastri per tracolla e cinture, cotone e poliestere', '20, 25, 30, 40, 50', [('pt', 20), ('pt', 25), ('pt', 30), ('pt', 40), ('pt', 50)]),
        ('Laccio tubolare in pelle', 'da 2 a 16', [('da', 2, 16)]),
        ('Laccio in cuoio a taglio vivo', '4', [('pt', 4)]),
    ], 'E poi nastro intrecciato, scheletri, salpe e rinforzi.'),
    ('Calzatura', [
        ('Laccio tubolare: corda cerata, elastico, pelle', '2, 3, 4', [('pt', 2), ('pt', 3), ('pt', 4)]),
        ('Tondino in pelle', 'da 2 a 3,5', [('da', 2, 3.5)]),
        ('Rivetti', '00, 033, 034, 036', []),
    ], 'E poi occhielli piatti e bombati, lampo in plastica e metallo, fibbie doppie.'),
    ('Abbigliamento', [
        ('Strisce in pelle a taglio vivo', 'da 2 a 60', [('da', 2, 60)]),
        ('Cordoncino in poliestere', '3, 4', [('pt', 3), ('pt', 4)]),
        ('Tondino in pelle', '2, 3', [('pt', 2), ('pt', 3)]),
        ('Alcantara, vari colori', 'h. 1,40', []),
    ], 'E poi corda juta.'),
]


def _quota(q):
    if q[0] == 'pt':
        return f'<i class="pt" style="--a:{q[1]}"></i>'
    return f'<i class="da" style="--a:{q[1]};--b:{q[2]}"></i>'


def mestieri():
    quote = ''.join(f'<span style="left:{"0" if v == 0 else f"calc({v} * var(--u))"}">{v}</span>' for v in range(0, 61, 10))
    testata = CNT(RAW(f'<p class="hbr-testata-quote" aria-hidden="true"><span class="hbr-nome">Articolo</span><span class="hbr-mis">mm</span>'
                      f'<span class="hbr-sc"><span class="hbr-quote">{quote}</span></span></p>'))
    settori = [testata]
    for nome, righe, anche in SETTORI:
        li = []
        for articolo, misura, qq in righe:
            asse = (f'<span class="hbr-sc"><span class="hbr-asse" aria-hidden="true">{"".join(_quota(q) for q in qq)}</span></span>'
                    if qq else '<span class="hbr-sc"></span>')
            li.append(C(TX(f'<p>{articolo}</p>', 'hbr-nome', style='small'),
                        TX(f'<p>{misura}</p>', 'hbr-mis', style='small', color=GRIGIO),
                        CNT(RAW(asse)),
                        boxed=False, css='hbr-li'))
        settori.append(C(H(nome, level='h3', style='h3', color=INCHIOSTRO, css='hbr-settore-h3'),
                         C(*li, boxed=False, css='hbr-ul'),
                         TX(f'<p>{anche}</p>', 'hbr-anche', style='small', color=GRIGIO),
                         boxed=False, css='hbr-settore'))
    griglia = C(
        H('Per chi fa borse, scarpe e capi', level='h2', style='h2', color=INCHIOSTRO, css='hbr-h2 hbr-mes-h2'),
        TX('<p>Le misure a catalogo, settore per settore. Ogni quota è in scala reale sullo stesso righello da 0 a 60&nbsp;mm.</p>',
           'hbr-mes-intro', color=GRIGIO),
        C(*settori, boxed=False, css='hbr-settori'),
        STILE(css_base('.hbr-mestieri') + CSS_MESTIERI),
        boxed=False, css='hbr-griglia')
    return C(griglia, boxed=False, pad=0, anchor='misure', tag='section', css='hbr-mestieri hbr-sito')


CSS_STORIA = (
    '.hbr-storia{padding:0 0 132px;display:block;width:auto;max-width:none;margin:0}'
    '.hbr-storia .hbr-anno{grid-column:1/7;align-self:end}'
    '.hbr-storia .hbr-anno span{display:block;font-stretch:125%;font-weight:240;font-size:clamp(96px,9.45vw,136px);line-height:.8;'
    'letter-spacing:-.045em;color:var(--cuoio)}'
    '.hbr-storia .hbr-anno b{display:block;margin-top:18px;font-weight:540;font-size:15px}'
    '.hbr-storia .hbr-storia-testo{grid-column:7/12;align-self:end;font-size:22px;line-height:1.45;letter-spacing:-.005em}'
    '@media (max-width:900px){.hbr-storia .hbr-anno,.hbr-storia .hbr-storia-testo{grid-column:1/13}.hbr-storia .hbr-storia-testo{margin-top:32px}}'
    '@media (max-width:700px){.hbr-storia{padding-bottom:88px}}'
)


def storia():
    return C(C(
        TX('<p><span>1979</span><b>Giorgio Gastaldello, nella pelletteria dal 1979</b></p>', 'hbr-anno'),
        TX("<p>Hambro nasce da un'idea di Giorgio Gastaldello: interni, rinforzi e minuteria per chi produce borse, cinture, calzature "
           "e abbigliamento.</p>", 'hbr-storia-testo', style='storia'),
        STILE(css_base('.hbr-storia') + CSS_STORIA),
        boxed=False, css='hbr-griglia'),
        boxed=False, pad=0, tag='section', css='hbr-storia hbr-sito')


CSS_CONTATTI = (
    '.hbr-contatti{background:var(--campo);color:var(--campo-testo);padding:112px 0;display:block;width:auto;max-width:none;margin:0}'
    '.hbr-contatti a:hover{color:var(--oro)}'
    '.hbr-invito{grid-column:1/6;align-self:start;display:block}'
    '.hbr-invito .hbr-invito-p{margin-top:24px;color:var(--campo-tenue);max-width:22em}'
    '.hbr-cartellino{grid-column:7/13;position:relative;background:var(--carta);color:var(--inchiostro);padding:40px 40px 28px;'
    'box-shadow:0 10px 22px rgba(28,10,0,.3);display:block;overflow:visible}'
    '.hbr-cartellino::before{content:"";display:block;position:absolute;top:22px;right:22px;left:auto;bottom:auto;width:14px;height:14px;'
    'border:0;border-radius:50%;background:var(--campo);box-shadow:inset 0 2px 3px rgba(0,0,0,.45);opacity:1;mix-blend-mode:normal;'
    'transition:none}'
    '.hbr-cartellino a:hover{color:var(--cuoio)}'
    '.hbr-cartellino .hbr-ditta{font-size:15px;color:var(--grigio)}'
    '.hbr-cartellino .hbr-tel-g a{display:inline-flex;align-items:center;min-height:44px;font-stretch:112%;font-weight:340;font-size:32px;'
    'line-height:1.1;letter-spacing:-.02em;text-decoration:none}'
    '.hbr-cartellino .hbr-tel-g a:hover{text-decoration:underline;text-decoration-thickness:1px}'
    '.hbr-cartellino dl{margin-top:12px;font-size:15px}'
    '.hbr-cartellino dl>div{display:grid;grid-template-columns:96px minmax(0,1fr);column-gap:24px;padding:10px 0;'
    'background:linear-gradient(var(--filo),var(--filo)) top/100% 1px no-repeat}'
    '.hbr-cartellino dt{color:var(--grigio)}'
    '.hbr-cartellino dd a{display:inline-block}'
    '.hbr-cartellino .hbr-ore{display:grid;grid-template-columns:auto auto;column-gap:16px;row-gap:2px}'
    '.hbr-cartellino .hbr-ore span:nth-child(even){text-align:right;white-space:nowrap}'
    '@media (max-width:1100px){.hbr-invito{grid-column:1/13}.hbr-cartellino{grid-column:1/13;margin-top:48px;max-width:620px}}'
    '@media (max-width:700px){.hbr-contatti{padding-top:80px;padding-bottom:80px}.hbr-cartellino{padding:32px 20px 20px}'
    '.hbr-cartellino dl>div{grid-template-columns:1fr;row-gap:2px}.hbr-cartellino dt{font-size:13px}}'
    '@media (max-width:420px){.hbr-cartellino .hbr-ore{grid-template-columns:1fr;row-gap:0}'
    '.hbr-cartellino .hbr-ore span:nth-child(even){text-align:left;white-space:normal;margin-bottom:6px}}'
)


def contatti():
    invito = C(
        H('Per ordini e campioni', level='h2', style='h2', color=CARTA, css='hbr-h2'),
        TX("<p>Sul sito c'è solo una parte di quello che è disponibile: il resto si chiede al telefono o per posta.</p>", 'hbr-invito-p',
           color=CAMPO_TENUE),
        boxed=False, css='hbr-invito')
    ore = (f'<span>Lunedì a giovedì</span><span>8:00{WJ}-{WJ}12:00 e 13:30{WJ}-{WJ}17:30</span><span>Venerdì</span>'
           f'<span>8:00{WJ}-{WJ}12:00</span><span>Sabato e domenica</span><span>chiuso</span>')
    cartellino = C(
        TX('<p>Hambro srl</p>', 'hbr-ditta', style='small', color=GRIGIO),
        TX(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', 'hbr-tel-g', style='tel'),
        TX(f'<dl><div><dt>Posta</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>'
           f"<div><dt>Indirizzo</dt><dd>via dell'Artigianato, 30, 30030 Vigonovo (Venezia)<br><a href=\"{MAPPA}\">Apri la mappa</a></dd></div>"
           f'<div><dt>Orari</dt><dd class="hbr-ore">{ore}</dd></div></dl>', 'hbr-cart-dl', style='small'),
        boxed=False, css='hbr-cartellino')
    return C(C(invito, cartellino, STILE(css_base('.hbr-contatti') + CSS_CONTATTI), boxed=False, css='hbr-griglia'),
             boxed=False, pad=0, bg=CAMPO, anchor='contatti', tag='section', css='hbr-contatti hbr-sito')


def home():
    sezioni = [('apertura', apertura()), ('banco', banco()), ('minuteria', campionario()), ('tav2', tav2()),
               ('ricopertura', ricopertura()), ('misure', mestieri()), ('storia', storia()), ('contatti', contatti())]
    # e-no-lazyload: Elementor toglie le immagini di sfondo (anche i gradienti: fili tra le righe, righelli delle quote,
    # striscia del banco) dalle sezioni dalla quarta in giù finché il suo script non le vede; senza script restavano vuote
    for _, nodo in sezioni:
        nodo.p['css'] += ' e-no-lazyload'
    return sezioni


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Hambro, Vigonovo',
     'descrizione': 'Hambro srl, Vigonovo (Venezia): minuteria in zama, ferro e ottone, lacci in pelle da mm2 a mm60, nastri, fodere '
                    'e rinforzi per borse, cinture, calzature e abbigliamento. Fibbie e bottoni ricoperti con il vostro materiale.'},
]
