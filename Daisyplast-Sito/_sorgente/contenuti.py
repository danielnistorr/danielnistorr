# -*- coding: utf-8 -*-
"""
Contenuti della home di Daisyplast per WordPress + Elementor: la home statica approvata ("La bolla", sito/index.html),
riportata sezione per sezione nel generatore di Benvegnù.

- Widget nativi di Elementor, modificabili dal cliente: logo, menu (Ultimate Addons), telefono, titolo, testi, foto
  (bolla, materiali, tappe del percorso), cartellini dei materiali, testi delle tappe, cifre della saldatura, clienti,
  recapiti, piede.
- Widget HTML (nodo RAW del motore) solo per quello che Elementor gratuito non fa: il pulsante "Menu" sotto i 1260 px,
  la copia latte del titolo ritagliata dentro la colonna della bolla, le due file di schede (materiali e percorso, con
  clic, dito, frecce, Inizio e Fine) e i fogli di stile. Lo script è quello della pagina statica, senza librerie.
- L'impaginazione (misure fluide con clamp, colonna della bolla, griglia a 12 colonne, punti di rottura a 1260, 1100,
  1000, 860, 560 e 359 px) è il foglio di stile della pagina statica, con le classi dsp-, dentro i nodi RAW: vale uguale
  per il template Elementor e per il fallback HTML.
- Caratteri: Sofia Sans e Sofia Sans Extra Condensed (OFL), gli stessi file woff2 della statica, con @font-face verso
  assets/web/fonts alla base delle immagini (nessuna chiamata a Google Fonts). Vedi LEGGIMI, "Caratteri".

Testi e dati: tutti e soli quelli della home statica. Nessun dato nuovo.
"""
import re

import motore as m
from motore import C, H, I, RAW, MENU


def T(html, *a, **k):
    """Widget Testo. L'apostrofo è scritto come &#39;: WordPress (wptexturize) lo cambierebbe in quello tipografico,
    che la pagina statica non usa."""
    return m.T(html.replace("'", '&#39;'), *a, **k)

PREFISSO = 'dsp'
NOME_SITO = 'Daisyplast'

# ---------------------------------------------------------------------------------------------
# Tema: colori e caratteri della home statica
# ---------------------------------------------------------------------------------------------
LATTE = '#F3F1EA'
GRAFITE = '#1E1F1D'
GRAFITE_2 = '#161715'
GIALLO = '#F2C230'         # il cuore della margherita del logo: l'unico colore pieno
GRIGIO = '#5F625D'         # testo secondario su latte (5,9:1)
GRIGIO_CHIARO = '#BDBFB9'  # testo secondario su grafite (9,6:1)
FILO = '#D3D1C9'
FILO_SCURO = 'rgba(243,241,234,.3)'

ALTO = 'Sofia Sans Extra Condensed'    # titoli, nomi dei materiali, tappe, cifre grandi, telefono
TESTO = 'Sofia Sans'                   # testo, menu, didascalie


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# misure (1440, 1024, 390) della pagina statica a quelle larghezze: servono all'editor di Elementor;
# a video comandano le misure fluide (clamp) del foglio di stile
TEMA = {
    'nome': 'Bolla',
    'fondo': LATTE, 'superficie': LATTE, 'inchiostro': GRAFITE, 'testo2': GRIGIO, 'accento': GRAFITE,
    'filetto': FILO, 'filetto_scuro': FILO_SCURO, 'su_scuro2': GRIGIO_CHIARO,
    'scuro': GRAFITE, 'su_scuro': LATTE, 'su_accento': LATTE,
    'font_titoli': ALTO, 'font_testo': TESTO, 'larghezza': 1440,
    # nessun foglio di stile dei caratteri da Google nel fallback e nell'anteprima (e niente preconnect a Google):
    # le @font-face stanno già nel foglio di stile di ogni sezione (verso assets/web/fonts)
    'google_fonts': '',
    'stili': {
        'nav':      _st(TESTO, '400', (16, 16, 16), 1.2),
        'tel':      _st(TESTO, '400', (16, 16, 15), 1.55),
        'titolo':   _st(ALTO, '300', (176, 125, 72), 0.88, -2),
        'intro':    _st(TESTO, '400', (20, 18, 17), 1.45),
        'prev':     _st(TESTO, '400', (16, 16, 15), 1.45),
        'didascalia': _st(TESTO, '400', (13, 13, 13), 1.45),
        'kg':       _st(ALTO, '300', (96, 76, 56), 0.86, -1),
        'sotto':    _st(TESTO, '400', (14, 14, 14), 1.45),
        'vh':       _st(TESTO, '400', (18, 17, 17), 1.55),
        'h3cart':   _st(ALTO, '400', (44, 44, 44), 1.0),
        'materia':  _st(TESTO, '400', (15, 15, 15), 1.4),
        'lista':    _st(TESTO, '400', (17, 17, 17), 1.35),
        'h2':       _st(ALTO, '300', (72, 51, 44), 0.94, -1),
        'n':        _st(TESTO, '400', (14, 14, 14), 1.4),
        'h3tappa':  _st(ALTO, '300', (88, 62, 56), 0.92, -1),
        'frase':    _st(TESTO, '400', (20, 18, 17), 1.45),
        'det':      _st(TESTO, '400', (15, 15, 15), 1.55),
        'cifre':    _st(TESTO, '400', (15, 15, 15), 1.35),
        'h2grande': _st(ALTO, '300', (88, 62, 44), 0.92, -1),
        'gruppi':   _st(TESTO, '400', (18, 17, 17), 1.55),
        'h2contatti': _st(ALTO, '300', (95, 68, 44), 0.92, -1),
        'grande':   _st(ALTO, '300', (245, 174, 66), 0.86, -2),
        'h3rec':    _st(TESTO, '400', (14, 14, 14), 1.5),
        'rec':      _st(TESTO, '400', (17, 17, 17), 1.5),
        'piede':    _st(TESTO, '400', (14, 14, 14), 1.6),
        # usati dal motore per i widget che questa home non ha (bottoni, articoli)
        'h1':       _st(ALTO, '300', (176, 125, 72), 0.88),
        'h3':       _st(ALTO, '300', (44, 44, 44), 1.0),
        'body':     _st(TESTO, '400', (18, 17, 17), 1.55),
        'small':    _st(TESTO, '400', (14, 14, 14), 1.45),
        'btn':      _st(TESTO, '400', (16, 16, 16), 1.2),
    },
    'spazi': {'sezione': (128, 91, 80), 'lato': (64, 46, 20), 'm': (24, 17, 16), 's': (16, 16, 12), '0': (0, 0, 0)},
    'bottone': {'raggio': 0, 'pad': (6, 0, 6, 0), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# I caratteri restano a questo indirizzo (l'installatore li copia sul sito, vedi LEGGIMI): per non dipendere da GitHub
# si caricano assets/web/ sul sito e si rigenera con build.py --base.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Daisyplast-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali, come nella home statica
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}980{NBSP}2226'
TEL_LINK = 'tel:+390499802226'
FAX = f'049{NBSP}982{NBSP}9961'
EMAIL = 'info@daisyplast.it'
PEC = 'daisyplastsrl@pec.it'
MAPPA = 'https://www.google.com/maps/search/?api=1&amp;query=Via+del+Lavoro+25+30030+Vigonovo+VE'

# voci del menu: in WordPress è il menu "Menu Daisyplast" (link personalizzati, li crea l'installatore)
VOCI_MENU = [('Materiali', '/#materiali'), ('Un ordine', '/#percorso'), ('Clienti', '/#clienti'), ('Contatti', '/#contatti')]
SLUG_MENU = 'menu-daisyplast'


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def _font(mo):
    # "font:400 16px/1.55 var(--testo)" scritto per esteso: la forma breve azzererebbe anche le cifre tabellari (.num)
    peso, misura, interlinea, famiglia, imp = mo.groups()
    imp = imp or ''
    return (f'font-weight:{peso}{imp};font-size:{misura}{imp};line-height:{interlinea}{imp};font-family:{famiglia.strip()}{imp}')


def _css(s):
    """Il foglio di stile scritto su più righe, compattato su una."""
    s = re.sub(r'\s*\n\s*', '', s.strip())
    return re.sub(r'(?<![-\w])font:(\d+) (\S+(?:\([^)]*\))?)/([\d.]+) ([^;!}]+)(!important)?', _font, s)


# ---------------------------------------------------------------------------------------------
# Fogli di stile comuni: caratteri, variabili e regole di base della pagina statica.
# Ogni sezione li porta con sé (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
def css_variabili():
    return _css(f'''
    @font-face{{font-family:"Sofia Sans";src:url({img("fonts/sofiasans-latin.woff2")}) format("woff2");font-weight:300 700;font-style:normal;font-display:swap}}
    @font-face{{font-family:"Sofia Sans Extra Condensed";src:url({img("fonts/sofiasansextracondensed-latin.woff2")}) format("woff2");font-weight:200 600;font-style:normal;font-display:swap}}
    :root{{--latte:#F3F1EA;--grafite:#1E1F1D;--grafite-2:#161715;--giallo:#F2C230;--grigio:#5F625D;--grigio-chiaro:#BDBFB9;
    --filo:#D3D1C9;--filo-scuro:rgba(243,241,234,.3);--m:clamp(20px,4.45vw,64px);--g:clamp(16px,1.67vw,24px);
    --r:clamp(80px,8.9vw,128px);--mezza:min(19vw,300px);--colonna-l:calc(50% - var(--mezza));--colonna-r:calc(50% + var(--mezza));
    --alto:"Sofia Sans Extra Condensed","Arial Narrow",sans-serif;--testo:"Sofia Sans",system-ui,sans-serif}}
    @media (max-width:1100px){{:root{{--mezza:14vw}}}}
    @media (min-width:561px) and (max-width:860px){{:root{{--mezza:22vw}}}}
    html{{scroll-behavior:auto;-webkit-text-size-adjust:100%;text-size-adjust:100%}}
    ''')


def css_testi(scope):
    """Regole di base dentro una sezione: margini del tema e di Elementor azzerati, link che prendono il colore del testo
    (il tema Hello li colora di rosa), fuoco visibile, cifre tabellari dove la statica le usa."""
    s = f'.{scope}'
    return _css(f'''
    {s}{{font-family:var(--testo);font-size:clamp(17px,1.25vw,18px);line-height:1.55;font-weight:400;font-synthesis:none;
    -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-kerning:normal;box-sizing:border-box}}
    {s} *,{s} *::before,{s} *::after{{box-sizing:border-box}}
    {s} p{{margin:0!important;text-wrap:pretty}}
    {s} h1,{s} h2,{s} h3,{s} .elementor-heading-title{{margin:0;font-weight:inherit;text-wrap:balance}}
    {s} ul,{s} ol{{margin:0!important;padding:0!important;list-style:none}}
    {s} li{{margin:0}}
    {s} figure{{margin:0}}
    {s} .elementor-widget:not(:last-child){{margin-block-end:0}}
    {s} .elementor-widget-container{{margin:0;padding:0}}
    {s} a{{color:inherit}}
    {s} a:hover,{s} a:focus,{s} a:active{{color:inherit}}
    {s} img{{display:block;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}
    {s} .num{{font-variant-numeric:tabular-nums lining-nums}}
    {s} :focus-visible,{s} [tabindex]:not([tabindex="-1"]):focus-visible{{outline:2px solid var(--grafite);outline-offset:3px}}
    {s} a:focus-visible,{s} button:focus-visible,{s} [tabindex]:not([tabindex="-1"]):focus-visible{{box-shadow:none}}
    {s}.dsp-scuro :focus-visible,{s}.dsp-scuro [tabindex]:not([tabindex="-1"]):focus-visible{{outline-color:var(--giallo)}}
    {s} .dsp-vh,{s} .dsp-vh .elementor-heading-title{{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden;
    clip:rect(0 0 0 0);white-space:nowrap;padding:0!important;margin:0!important}}
    @media (prefers-reduced-motion:reduce){{{s} *{{transition:none!important}}}}
    ''')


# il widget che porta solo un foglio di stile: non occupa posto (lo <style> vale anche dentro un elemento nascosto)
CSS_STILE = '.dsp-stile{display:none!important}'


def stile(scope, css):
    return C(RAW('', css=css_variabili() + CSS_STILE + css_testi(scope) + css), boxed=False, css='dsp-stile')


# regole che valgono per tutta la pagina: stanno nella testata (Elementor e fallback)
CSS_SITO = _css('''
body{background:var(--latte);color:var(--grafite);font-family:var(--testo);font-size:clamp(17px,1.25vw,18px);line-height:1.55;
font-weight:400;font-synthesis:none;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-kerning:normal;margin:0}
.dsp-sito a.dsp-salta{position:absolute;left:var(--m);top:-60px;background:var(--latte);color:var(--grafite)!important;padding:10px 14px;
z-index:10;font:400 17px/1.55 var(--testo);text-decoration:underline;white-space:nowrap}
.dsp-sito a.dsp-salta:focus{top:12px}
''')


# =============================================================================================
# TESTATA (template "Daisyplast: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_TESTATA = _css('''
.dsp-testata{position:absolute!important;top:0;left:0;right:0;z-index:5;display:flex!important;flex-direction:row!important;
flex-wrap:nowrap!important;align-items:center!important;gap:0!important;padding:26px var(--m) 14px!important;color:var(--grafite);
background:none!important;width:100%!important;max-width:none!important;margin:0!important;min-height:0!important}
.dsp-testata>*{flex:0 0 auto!important;width:auto!important;max-width:none!important;margin:0!important}
.dsp-testata>.dsp-fuori{position:absolute!important;left:0;top:0;width:0!important;height:0!important;padding:0!important;overflow:visible}
.dsp-marchio{display:block!important;width:clamp(124px,10.6vw,152px)!important;flex:none!important;order:-2;line-height:0;text-align:left!important}
.dsp-marchio a{display:block}
.dsp-marchio img{display:block;width:100%!important;max-width:100%!important;height:auto!important}
.dsp-tel{order:-1;margin-left:clamp(20px,2.4vw,36px)!important;color:inherit!important}
.dsp-tel p{color:inherit!important}
.dsp-tel p{margin:0!important}
.dsp-tel a,.dsp-tel a:hover,.dsp-tel a:focus{display:block;font:400 16px/1.55 var(--testo)!important;color:inherit!important;text-decoration:none!important;
padding:6px 0;border-bottom:1px solid var(--grigio);transition:border-color .15s;white-space:nowrap}
.dsp-tel a:hover{border-bottom-color:var(--grafite)}
.dsp-menu{margin-left:auto!important}
.dsp-menu ul.hfe-nav-menu,.dsp-menu .dsp-nav-l{display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;
gap:clamp(18px,1.9vw,28px)!important;margin:0!important;padding:0!important;list-style:none;align-items:center}
.dsp-menu ul.hfe-nav-menu,.dsp-menu ul.hfe-nav-menu li{visibility:visible!important;opacity:1!important;height:auto!important;
position:static!important;transform:none!important;max-height:none!important;overflow:visible!important}
.dsp-menu .hfe-nav-menu,.dsp-menu nav.hfe-dropdown,.dsp-menu .hfe-dropdown .hfe-nav-menu{border:0!important;box-shadow:none!important}
.dsp-menu .hfe-nav-menu::before,.dsp-menu .hfe-nav-menu::after{display:none!important}
.dsp-menu li{margin:0!important;padding:0!important;border:0!important;background:none!important;width:auto!important}
.dsp-menu a.hfe-menu-item,.dsp-menu .dsp-nav-l a{display:block!important;padding:6px 0!important;font:400 16px/1.2 var(--testo)!important;
letter-spacing:0!important;text-transform:none!important;color:inherit!important;text-decoration:none!important;background:none!important;
border:0!important;border-bottom:1px solid transparent!important;transition:border-color .15s!important;white-space:nowrap;justify-content:flex-start!important}
.dsp-menu a.hfe-menu-item:hover,.dsp-menu .dsp-nav-l a:hover{border-bottom-color:currentColor!important;color:inherit!important}
.dsp-menu a.hfe-menu-item:focus,.dsp-menu .dsp-nav-l a:focus{color:inherit!important}
.dsp-menu a.hfe-menu-item::before,.dsp-menu a.hfe-menu-item::after{display:none!important}
.dsp-menu .hfe-nav-menu__toggle,.dsp-menu details{display:none!important}
.dsp-menu nav{visibility:visible!important;opacity:1!important;height:auto!important;position:static!important;background:none!important;
box-shadow:none!important;border:0!important;width:auto!important;margin:0!important;padding:0!important}
.dsp-apri-box{display:none!important;padding:0!important}
.dsp-sito button.dsp-apri,.dsp-sito button.dsp-apri:hover,.dsp-sito button.dsp-apri:focus{display:inline-block;appearance:none;background:none;border:0;
border-bottom:1px solid var(--grigio);border-radius:0;color:inherit;font:400 16px/1.2 var(--testo);padding:6px 0;margin:0;cursor:pointer;
text-transform:none;letter-spacing:0;white-space:nowrap;transition:none}
.dsp-sito button.dsp-apri:hover{border-bottom-color:var(--grafite)}
@media (max-width:1260px){
.dsp-testata .dsp-menu{display:none!important}
.dsp-testata .dsp-apri-box{display:block!important;margin-left:auto!important}
.dsp-testata.dsp-aperto .dsp-menu{display:flex!important;position:absolute!important;top:100%;left:0;right:0;width:auto!important;margin:0!important;
flex-direction:column;background:var(--grafite-2)!important;color:var(--latte);padding:8px var(--m) 18px!important}
.dsp-aperto .dsp-menu>*,.dsp-aperto .dsp-menu .hfe-nav-menu,.dsp-aperto .dsp-menu nav{width:100%!important}
.dsp-aperto .dsp-menu ul.hfe-nav-menu,.dsp-aperto .dsp-menu .dsp-nav-l{flex-direction:column!important;align-items:stretch;gap:0!important}
.dsp-aperto .dsp-menu li{width:100%!important}
.dsp-aperto .dsp-menu a.hfe-menu-item,.dsp-aperto .dsp-menu .dsp-nav-l a{padding:12px 0!important;border-bottom:1px solid rgba(243,241,234,.12)!important;font-size:18px!important}
.dsp-aperto .dsp-menu a.hfe-menu-item:hover,.dsp-aperto .dsp-menu .dsp-nav-l a:hover{border-bottom-color:currentColor!important}
.dsp-aperto .dsp-menu a:focus-visible{outline-color:var(--giallo)}
}
@media (min-width:561px) and (max-width:860px){
.dsp-testata .dsp-tel{order:0;margin-left:auto!important}
.dsp-testata .dsp-apri-box{order:1;margin-left:22px!important}
}
@media (max-width:560px){
.dsp-testata{padding-top:18px!important;color:var(--latte)}
.dsp-testata .dsp-marchio{width:116px!important}
.dsp-tel a,.dsp-tel a:hover,.dsp-tel a:focus{font-size:15px!important;border-bottom-color:var(--grigio-chiaro)}
.dsp-sito button.dsp-apri,.dsp-sito button.dsp-apri:hover,.dsp-sito button.dsp-apri:focus{border-bottom-color:var(--grigio-chiaro)}
.dsp-tel a:hover{border-bottom-color:var(--grafite)}
.dsp-sito button.dsp-apri:hover{border-bottom-color:var(--grafite)}
.dsp-testata :focus-visible{outline-color:var(--giallo)!important}
.dsp-testata a.dsp-salta:focus-visible{outline-color:var(--grafite)!important}
}
''')

# solo in Elementor: Ultimate Addons e il tema
CSS_TESTATA_ELEMENTOR = _css('''
#masthead{position:static}
.hfe-skip-link{display:none!important}
.dsp-menu .hfe-nav-menu li.current-menu-item>a.hfe-menu-item{border-bottom-color:transparent!important}
.dsp-menu .hfe-nav-menu li.current-menu-item>a.hfe-menu-item:hover{border-bottom-color:currentColor!important}
''')

SCRIPT_MENU = (
    # sotto i 1260 px il menu si apre con il pulsante; si chiude toccando una voce. Il menu prende il nome "Principale"
    # e il logo "Daisyplast, pagina iniziale" come nella statica (Elementor gratuito non dà attributi ai widget, e nel campo
    # degli attributi del link la virgola separa due attributi)
    "<script>(function(){function avvia(){var t=document.querySelector('.dsp-testata');if(!t||t.dataset.pronto)return;t.dataset.pronto='1';"
    "var apri=t.querySelector('.dsp-apri'),menu=t.querySelector('.dsp-menu');if(!apri||!menu)return;"
    "var nav=menu.tagName==='NAV'?menu:menu.querySelector('nav');if(nav){nav.id='dsp-menu';nav.setAttribute('aria-label','Principale')}"
    "apri.setAttribute('aria-controls','dsp-menu');"
    "apri.addEventListener('click',function(){var a=t.classList.toggle('dsp-aperto');apri.setAttribute('aria-expanded',a?'true':'false')});"
    # le voci portano alla sezione con un salto netto, come nella statica: il clic si ferma qui, prima dello scorrimento
    # morbido che Ultimate Addons aggancia alle voci del menu
    "menu.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;"
    "if(a.hash&&a.pathname===location.pathname)e.stopPropagation();t.classList.remove('dsp-aperto');"
    "apri.setAttribute('aria-expanded','false')},true);"
    "var m=t.querySelector('.dsp-marchio a');if(m)m.setAttribute('aria-label','Daisyplast, pagina iniziale')}"
    "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',avvia);else avvia()})();</script>"
)


def header():
    marchio = I(img('logo.webp'), 'Daisyplast s.r.l.', link='/', css='dsp-marchio')
    apri = C(RAW('<button class="dsp-apri" type="button" aria-expanded="false">Menu</button>'), boxed=False, css='dsp-apri-box')
    menu = MENU(VOCI_MENU, colore=GRAFITE, colore_hover=GRAFITE, accento=GRAFITE, fondo_menu=GRAFITE_2, linea='rgba(0,0,0,0)',
                stile='nav', stile_mobile='nav', spazio=28, pad_h=0, pad_v=6, distanza=0, align_menu='right', slug=SLUG_MENU,
                css='dsp-menu')
    tel = T(f'<p><a class="num" href="{TEL_LINK}">{TEL}</a></p>', style='tel', color=GRAFITE, link_color=GRAFITE,
            link_hover=GRAFITE, sottolinea=False, css='dsp-tel')
    globali = RAW('<a class="dsp-salta" href="#materiali">Vai ai materiali</a>' + SCRIPT_MENU,
                  css=css_variabili() + CSS_SITO + css_testi('dsp-testata') + CSS_TESTATA)
    solo_el = RAW('', css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    # i due widget HTML stanno fuori dalla riga (posizione assoluta, misura zero): non spostano logo, menu e telefono.
    # Vengono per primi: "Vai ai materiali" è la prima fermata del tasto Tab, come nella statica
    fuori = C(globali, solo_el, boxed=False, css='dsp-fuori')
    # stesso ordine della statica (logo, pulsante, menu, telefono); la posizione a video la dà "order"
    return C(fuori, marchio, apri, menu, tel, dir='row', align='center', boxed=False, pad=0, css='dsp-testata dsp-sito')


# =============================================================================================
# PIEDE (template "Daisyplast: Footer")
# =============================================================================================
CSS_PIEDE = _css('''
.dsp-piede{background:var(--grafite-2)!important;color:var(--grigio-chiaro);padding:40px var(--m) 48px!important;font-size:14px;line-height:1.6;
display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--g)!important;row-gap:20px!important;
width:100%!important;max-width:none!important;margin:0!important}
.dsp-piede>*{width:auto!important;max-width:none!important}
.dsp-piede>.dsp-pa{grid-column:1 / span 4}
.dsp-piede>.dsp-pb{grid-column:5 / span 4}
.dsp-piede>.dsp-pc{grid-column:9 / span 4}
.dsp-pa,.dsp-pb,.dsp-pc{font:400 14px/1.6 var(--testo)!important;color:var(--grigio-chiaro)!important}
.dsp-piede strong{color:var(--latte);font-weight:600}
.dsp-piede a,.dsp-piede a:focus{color:var(--grigio-chiaro)!important;text-decoration:underline!important;text-decoration-thickness:auto!important;
text-underline-offset:3px!important}
.dsp-piede a:hover{color:var(--latte)!important}
.dsp-piede :focus-visible{outline-color:var(--giallo)!important}
@media (max-width:860px){.dsp-piede>.dsp-pa,.dsp-piede>.dsp-pb,.dsp-piede>.dsp-pc{grid-column:1 / -1}}
''')


def footer():
    def col(html, cls):
        return T(f'<p>{html}</p>', style='piede', color=GRIGIO_CHIARO, link_color=GRIGIO_CHIARO, link_hover=LATTE, css=cls)
    return C(
        col('<strong>DAISYPLAST s.r.l.</strong><br>Via del Lavoro 25, Tombelle di Vigonovo<br><span class="num">30030</span> Vigonovo (VE)', 'dsp-pa'),
        col(f'P. IVA e C.F. 03861090276<br>REA VE-344838<br>Capitale sociale 60.000{NBSP}euro i.v.', 'dsp-pb num'),
        col(f'Tel. <a class="num" href="{TEL_LINK}">{TEL}</a><br>PEC <a class="dsp-l" href="mailto:{PEC}">{PEC}</a><br>'
            'Questa pagina non usa cookie', 'dsp-pc num'),
        stile('dsp-piede', CSS_PIEDE),
        boxed=False, pad=0, bg=GRAFITE_2, css='dsp-piede dsp-sito')


# =============================================================================================
# HOME
# =============================================================================================

# ---------- Apertura: la bolla in colonna sul campo latte ----------
CSS_APERTURA = _css('''
.dsp-apertura{position:relative!important;display:block!important;background:var(--latte)!important;color:var(--grafite);height:100vh;
height:100svh;min-height:720px!important;max-height:1080px;overflow:hidden!important;padding:0!important;width:100%!important;
max-width:none!important;margin:0!important}
.dsp-apertura>.elementor-widget-html{position:static!important}
.dsp-bolla{position:absolute!important;top:0;bottom:0;left:50%;width:calc(2 * var(--mezza))!important;max-width:none!important;
transform:translateX(-50%);background:var(--grafite)!important;padding:0!important;margin:0!important;display:block!important;min-height:0!important}
.dsp-bolla>*,.dsp-bolla .elementor-widget-container{height:100%!important;width:100%!important;margin:0!important}
.dsp-bolla img{width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;object-position:50% 0}
.dsp-bolla>.dsp-bolla-p{display:none!important}
.dsp-titolo{position:absolute!important;left:var(--m);right:var(--m);top:clamp(120px,19vh,190px);margin:0!important;width:auto!important;
max-width:none!important;z-index:1}
.dsp-titolo,.dsp-titolo .elementor-heading-title{font-family:var(--alto)!important;font-weight:300!important;letter-spacing:-.012em!important;
font-size:clamp(64px,12.2vw,216px)!important;line-height:.88!important;color:var(--grafite)!important;text-transform:none!important;margin:0!important}
.dsp-titolo span{display:block}
.dsp-titolo .r{text-align:right}
.dsp-h1{clip-path:polygon(0 0,var(--colonna-l) 0,var(--colonna-l) 100%,var(--colonna-r) 100%,var(--colonna-r) 0,100% 0,100% 100%,0 100%)}
.dsp-sito .dsp-luce{color:var(--latte)!important;clip-path:inset(0 var(--colonna-l));pointer-events:none;user-select:none}
.dsp-fondo{position:absolute!important;left:var(--m);right:var(--m);bottom:clamp(100px,13vh,124px);display:grid!important;
grid-template-columns:repeat(12,1fr);column-gap:var(--g)!important;row-gap:0!important;align-items:last baseline!important;padding:0!important;
width:auto!important;max-width:none!important;margin:0!important;min-height:0!important;z-index:1}
.dsp-fondo>*{width:auto!important;margin:0!important}
.dsp-intro{grid-column:1 / span 5;display:block!important;padding:0!important;font-size:clamp(18px,1.4vw,20px);line-height:1.45;max-width:calc(50vw - var(--mezza) - var(--m) - 32px)!important}
.dsp-intro-p{font:400 clamp(18px,1.4vw,20px)/1.45 var(--testo)!important;color:inherit!important}
.dsp-prev{margin-top:18px!important;font:400 16px/1.45 var(--testo)!important;color:inherit!important}
.dsp-prev a,.dsp-prev a:hover,.dsp-prev a:focus{color:inherit!important;text-decoration:none!important;border-bottom:1px solid var(--grigio);
padding-bottom:3px;transition:border-color .15s}
.dsp-prev a:hover{border-bottom-color:var(--grafite)}
.dsp-dato{grid-column:8 / span 5;position:relative!important;display:block!important;padding:0!important;text-align:right;justify-self:end;
max-width:calc(50vw - var(--mezza) - var(--m) - 24px)!important}
.dsp-didascalia{max-width:19em!important;margin:0 0 26px auto!important;text-align:left;font:400 13px/1.45 var(--testo)!important;color:var(--grigio)!important}
.dsp-kg,.dsp-kg p{white-space:nowrap!important}
.dsp-kg{font-family:var(--alto)!important;font-weight:300!important;letter-spacing:-.012em!important;font-size:96px!important;line-height:.86!important;
white-space:nowrap;font-variant-numeric:lining-nums proportional-nums!important;color:inherit!important;text-align:right!important}
.dsp-sotto{position:absolute!important;right:0;top:100%;width:min(100%,25em)!important;max-width:none!important;margin-top:16px!important;
font:400 14px/1.45 var(--testo)!important;color:inherit!important;text-align:right!important}
@media (max-width:1100px){.dsp-kg{font-size:76px!important}}
@media (max-width:860px){
.dsp-fondo{grid-template-columns:1fr 1fr}
.dsp-intro{grid-column:1 / span 2;max-width:30em!important}
.dsp-dato{grid-column:1 / span 2;max-width:none!important;justify-self:stretch}
}
@media (min-width:561px) and (max-width:860px){
.dsp-bolla{bottom:auto;height:max(720px,min(100svh,1080px))!important}
.dsp-apertura{height:auto;max-height:none;min-height:0!important}
.dsp-fondo{position:relative!important;left:auto;right:auto;bottom:auto;margin:0 var(--m)!important;
padding:calc(max(720px,min(100svh,1080px)) + 48px) 0 0!important;align-items:start!important}
.dsp-dato{text-align:left;margin-top:36px!important}
.dsp-didascalia{margin:0 0 20px!important}
.dsp-kg{text-align:left!important}
.dsp-sotto{position:static!important;margin-top:12px!important;width:auto!important;max-width:30em!important;text-align:left!important}
}
@media (max-width:560px){
.dsp-apertura{min-height:680px!important;max-height:none;background:var(--grafite)!important;color:var(--latte)}
.dsp-apertura :focus-visible{outline-color:var(--giallo)!important}
.dsp-bolla{width:100%!important}
.dsp-bolla>.dsp-bolla-d{display:none!important}
.dsp-bolla>.dsp-bolla-p{display:block!important}
.dsp-bolla::after{content:"";position:absolute;inset:0;background:linear-gradient(to bottom,rgba(22,23,21,.5) 0,rgba(22,23,21,0) 30%,
rgba(22,23,21,0) 44%,rgba(22,23,21,.9) 72%,rgba(22,23,21,.96) 100%)}
.dsp-titolo{top:clamp(92px,13vh,120px)}
.dsp-titolo,.dsp-titolo .elementor-heading-title{font-size:clamp(58px,18.6vw,84px)!important;line-height:.9!important;color:var(--latte)!important}
.dsp-h1{clip-path:none}
.dsp-sito .dsp-luce{display:none}
.dsp-fondo{display:block!important;top:auto;bottom:24px}
.dsp-intro{font-size:17px}
.dsp-intro-p{font-size:17px!important}
.dsp-prev{margin-top:12px!important;font-size:15px!important}
.dsp-prev a,.dsp-prev a:hover,.dsp-prev a:focus{border-bottom-color:var(--grigio-chiaro)}
.dsp-prev a:hover{border-bottom-color:var(--grafite)}
.dsp-dato{text-align:left;margin-top:18px!important}
.dsp-didascalia{display:none!important}
.dsp-kg{font-size:56px!important}
.dsp-kg{text-align:left!important}
.dsp-sotto{position:static!important;margin-top:8px!important;width:auto!important;text-align:left!important}
}
''')

SCRIPT_LUCE = (
    # la copia latte del titolo segue il titolo vero: se il cliente cambia il titolo in Elementor, cambia anche la copia
    "<script>(function(){function avvia(){var h=document.querySelector('.dsp-h1 h1,h1.dsp-h1'),l=document.querySelector('.dsp-luce');"
    "if(h&&l&&h.innerHTML!==l.innerHTML)l.innerHTML=h.innerHTML}"
    "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',avvia);else avvia()})();</script>"
)

TITOLO = '<span>Sacchi e film</span><span class="r">in polietilene</span>'
ALT_BOLLA = "La bolla di film che sale dalla testa di estrusione, dentro l'anello di raffreddamento in acciaio forato"


def apertura():
    bolla = C(I(img('bolla-768.webp'), ALT_BOLLA, css='dsp-bolla-d'), I(img('bolla-p-590.webp'), ALT_BOLLA, css='dsp-bolla-p'),
              boxed=False, tag='figure', css='dsp-bolla')
    titolo = H(TITOLO, level='h1', style='titolo', color=GRAFITE, css='dsp-titolo dsp-h1')
    # il titolo è grafite sul latte e latte dove attraversa la bolla: due strati, ritagliati sul bordo della colonna
    luce = RAW(f'<p class="dsp-titolo dsp-luce" aria-hidden="true">{TITOLO}</p>' + SCRIPT_LUCE)
    intro = C(
        T('<p>Estrudiamo il film in bolla e lo saldiamo in sacchi, shopper, bobine e monopieghe per grossisti del Triveneto, '
          f'industrie e artigiani. A Tombelle di Vigonovo dal{NBSP}2008.</p>', style='intro', color=GRAFITE, css='dsp-intro-p'),
        T(f'<p>Per un preventivo: <a class="num" href="{TEL_LINK}">{TEL}</a></p>', style='prev', color=GRAFITE, link_color=GRAFITE,
          link_hover=GRAFITE, sottolinea=False, css='dsp-prev'),
        boxed=False, css='dsp-intro')
    dato = C(
        T("<p>Nella foto, una testa di estrusione: il film sale dall'anello di raffreddamento verso i rulli di traino.</p>",
          style='didascalia', color=GRIGIO, css='dsp-didascalia'),
        T(f'<p>oltre 10.000{NBSP}kg</p>', style='kg', color=GRAFITE, css='dsp-kg num'),
        T('<p>di sacchi e film al giorno, da 5 linee in bolla e 4 di saldatura. Consegne con i nostri mezzi.</p>',
          style='sotto', color=GRAFITE, css='dsp-sotto num'),
        boxed=False, css='dsp-dato')
    fondo = C(intro, dato, boxed=False, css='dsp-fondo')
    return C(bolla, titolo, luce, fondo, stile('dsp-apertura', CSS_APERTURA),
             boxed=False, pad=0, anchor='apertura', tag='section', css='dsp-apertura dsp-sito')


# ---------- Schede: lo script della pagina statica, per una fila di schede ----------
def script_schede(id_lista, fuoco_pannelli):
    """Una fila di schede (role=tablist): clic, dito, frecce, Inizio e Fine. Cambio netto, nessun movimento automatico.
    I pannelli sono contenitori di Elementor (ancora = id del pannello): lo script dà loro ruolo e nome e li nasconde."""
    return (
        "<script>(function(){function avvia(){"
        f"var lista=document.getElementById('{id_lista}');if(!lista||lista.dataset.pronto)return;"
        "var schede=[].slice.call(lista.querySelectorAll('[role=tab]'));"
        "var pannelli=schede.map(function(s){return document.getElementById(s.getAttribute('aria-controls'))});"
        "if(pannelli.some(function(p){return !p}))return;lista.dataset.pronto='1';"
        "pannelli.forEach(function(p,k){p.setAttribute('role','tabpanel');p.setAttribute('aria-labelledby',schede[k].id);"
        + ("p.tabIndex=0;" if fuoco_pannelli else "") +
        "});var cur=0;"
        "function vai(i,fuoco){i=(i+schede.length)%schede.length;cur=i;"
        "schede.forEach(function(s,k){var su=k===i;s.setAttribute('aria-selected',su?'true':'false');s.tabIndex=su?0:-1;pannelli[k].hidden=!su});"
        "[].forEach.call(pannelli[i].querySelectorAll('img'),function(im){im.loading='eager'});"
        "if(fuoco)schede[i].focus()}"
        "schede.forEach(function(s,k){s.addEventListener('click',function(){vai(k,false)});"
        "s.addEventListener('keydown',function(e){var d={ArrowRight:1,ArrowDown:1,ArrowLeft:-1,ArrowUp:-1}[e.key];"
        "if(d){e.preventDefault();vai(cur+d,true)}else if(e.key==='Home'){e.preventDefault();vai(0,true)}"
        "else if(e.key==='End'){e.preventDefault();vai(schede.length-1,true)}})});"
        "vai(0,false);pannelli[0].parentNode.classList.add('dsp-pronto');"
        # sul palco del percorso si sfoglia anche col dito
        "var palco=lista.closest('.dsp-palco');palco=palco&&palco.querySelector('.dsp-tappe');"
        "if(palco){var x0=null,y0=null;palco.addEventListener('dragstart',function(e){e.preventDefault()});"
        "palco.addEventListener('pointerdown',function(e){x0=e.clientX;y0=e.clientY});"
        "palco.addEventListener('pointercancel',function(){x0=null});"
        "palco.addEventListener('pointerup',function(e){if(x0===null)return;var dx=e.clientX-x0,dy=e.clientY-y0;x0=null;"
        "if(Math.abs(dx)>48&&Math.abs(dx)>Math.abs(dy)*1.4)vai(cur+(dx<0?1:-1),false)})}}"
        "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',avvia);else avvia()})();</script>"
    )


# ---------- Tre materiali: il selettore ----------
CSS_MATERIALI = _css('''
.dsp-materiali{display:block!important;padding:var(--r) 0 0!important;background:var(--latte)!important;color:var(--grafite);width:100%!important;
max-width:none!important;margin:0!important}
.dsp-testa{display:block!important;padding:0 var(--m)!important}
.dsp-testa-p{max-width:30em!important;font:400 clamp(18px,1.4vw,20px)/1.45 var(--testo)!important;color:inherit!important}
.dsp-schede{display:flex;column-gap:clamp(20px,3.2vw,52px);margin:clamp(20px,2.4vw,32px) 0 0;padding:0 var(--m)}
.dsp-sito .dsp-schede button,.dsp-sito .dsp-schede button:hover,.dsp-sito .dsp-schede button:focus{appearance:none;background:none;border:0;
border-bottom:3px solid transparent;border-radius:0;padding:0 0 10px;margin:0;cursor:pointer;font-family:var(--alto);font-weight:300;
font-size:clamp(46px,8.2vw,118px);line-height:.95;letter-spacing:-.01em;color:#83867F;text-transform:none;white-space:normal;text-align:center;
transition:color .12s,border-color .12s;box-shadow:none}
.dsp-sito .dsp-schede button:hover{color:var(--grafite)}
.dsp-sito .dsp-schede button[aria-selected="true"]{color:var(--grafite);border-bottom-color:var(--grafite)}
.dsp-pannelli{display:grid!important;margin-top:clamp(24px,2.8vw,40px)!important;padding:0!important;gap:0!important}
.dsp-pannello{position:relative!important;grid-area:1 / 1;display:block!important;padding:0!important;width:auto!important;min-width:0}
.dsp-pannello[hidden],.dsp-pannelli:not(.dsp-pronto)>.dsp-pannello~.dsp-pannello{display:block!important;visibility:hidden}
.dsp-foto{position:relative!important;display:block!important;background:var(--grafite)!important;padding:0!important;margin:0!important}
.dsp-chiaro .dsp-foto{background:var(--latte)!important}
.dsp-foto>*{margin:0!important}
.dsp-foto img{width:100%!important;max-width:100%!important;height:clamp(440px,50vw,800px)!important;object-fit:cover}
.dsp-foto>.dsp-foto-p{display:none!important}
.dsp-cartellino{position:absolute!important;right:var(--m);bottom:var(--m);width:440px!important;max-width:none!important;display:block!important;
background:var(--latte)!important;color:var(--grafite);padding:28px 32px 30px!important;margin:0!important}
.dsp-chiaro .dsp-cartellino{box-shadow:0 0 0 1px var(--filo)}
.dsp-cart-h,.dsp-cart-h .elementor-heading-title{font-family:var(--alto)!important;font-weight:400!important;font-size:44px!important;line-height:1!important;
letter-spacing:-.005em!important;color:var(--grafite)!important;text-transform:none!important}
.dsp-materia{margin-top:8px!important;font:400 15px/1.4 var(--testo)!important;color:var(--grigio)!important}
.dsp-lista{margin-top:18px!important;font:400 17px/1.35 var(--testo)!important;color:var(--grafite)!important}
.dsp-lista li,.dsp-lista li:last-child{padding:8px 0!important;margin:0!important;border:0!important;border-top:1px solid var(--filo)!important;
font:inherit!important;list-style:none!important}
.dsp-lista li::marker{content:none}
@media (max-width:1100px){.dsp-cartellino{width:400px!important}}
@media (max-width:860px){
.dsp-foto img{height:auto!important;aspect-ratio:4/3}
.dsp-cartellino{position:relative!important;right:auto;bottom:auto;width:auto!important;margin:0 var(--m)!important;padding:24px 0 0!important;background:none!important}
.dsp-chiaro .dsp-cartellino{box-shadow:none}
}
@media (max-width:560px){
.dsp-schede{display:grid;grid-template-columns:1fr;justify-items:start;row-gap:6px}
.dsp-sito .dsp-schede button,.dsp-sito .dsp-schede button:hover,.dsp-sito .dsp-schede button:focus{font-size:44px;padding-bottom:6px}
.dsp-foto>.dsp-foto-d{display:none!important}
.dsp-foto>.dsp-foto-p{display:block!important}
.dsp-foto img{aspect-ratio:4/5}
}
''')

MATERIALI = [
    ('vergine', 'Vergine', 'PE-LD vergine', 'Polietilene a bassa densità di prima scelta',
     ['Sacchi per alimenti', 'Buste con chiusura minigrip', 'Sacchi per maglieria', 'Sacchi industriali',
      'Bobine e monopieghe per imballaggio'],
     'vergine-l-2400.webp', 'vergine-p-1160.webp', 'Un sacchetto trasparente per alimenti, su fondo nero', False),
    ('rigenerato', 'Rigenerato', 'PE-LD rigenerato', 'Polietilene da materiale riciclato',
     ["Sacchi neri per l'immondizia, sfusi e in rotolo", 'Sacchi per la raccolta differenziata', 'Shopper riutilizzabili',
      'Sacchi industriali', 'Bobine in materiale rigenerato'],
     'rigenerato-l-2400.webp', 'rigenerato-p-1200.webp', 'Film nero lucido, spiegazzato', False),
    ('compostabile', 'Compostabile', 'Compostabile', 'Biodegradabile e compostabile',
     ['Sacchetti per i rifiuti', 'Shopper biocompostabili'],
     'compostabile-l-2400.webp', 'compostabile-p-1120.webp', 'Una margherita bianca a cui manca un petalo, posato accanto', True),
]


def materiali():
    testa = C(H('Tre materiali', level='h2', style='vh', color=GRAFITE, css='dsp-vh'),
              T('<p>Dalle stesse cinque linee escono tre film.</p>', style='intro', color=GRAFITE, css='dsp-testa-p'),
              boxed=False, css='dsp-testa')
    bottoni = ''.join(
        f'<button role="tab" id="s-{k}" aria-controls="p-{k}" aria-selected="{"true" if i == 0 else "false"}"'
        + ('' if i == 0 else ' tabindex="-1"') + f'>{nome}</button>'
        for i, (k, nome, *_r) in enumerate(MATERIALI))
    schede = RAW(f'<div class="dsp-schede" role="tablist" aria-label="Materiale del film" id="dsp-schede-materiali">{bottoni}</div>'
                 + script_schede('dsp-schede-materiali', True))
    pannelli = []
    for k, _nome, h3, materia, voci, l, p, alt, chiaro in MATERIALI:
        foto = C(I(img(l), alt, css='dsp-foto-d'), I(img(p), alt, css='dsp-foto-p'), boxed=False, tag='figure', css='dsp-foto')
        cartellino = C(
            H(h3, level='h3', style='h3cart', color=GRAFITE, css='dsp-cart-h'),
            T(f'<p>{materia}</p>', style='materia', color=GRIGIO, css='dsp-materia'),
            T('<ul>' + ''.join(f'<li>{v}</li>' for v in voci) + '</ul>', style='lista', color=GRAFITE, css='dsp-lista'),
            boxed=False, css='dsp-cartellino')
        pannelli.append(C(foto, cartellino, boxed=False, anchor=f'p-{k}', css='dsp-pannello' + (' dsp-chiaro' if chiaro else '')))
    return C(testa, schede, C(*pannelli, boxed=False, css='dsp-pannelli'), stile('dsp-materiali', CSS_MATERIALI),
             boxed=False, pad=0, anchor='materiali', tag='section', css='dsp-materiali dsp-sito')


# ---------- Il percorso di un ordine: il palco ----------
CSS_PERCORSO = _css('''
.dsp-percorso{display:block!important;background:var(--grafite)!important;color:var(--latte);padding:var(--r) 0 clamp(32px,3vw,48px)!important;
width:100%!important;max-width:none!important;margin:0!important}
.dsp-capo{display:grid!important;grid-template-columns:repeat(12,1fr);column-gap:var(--g)!important;row-gap:0!important;align-items:last baseline!important;
padding:0 var(--m)!important}
.dsp-capo>*{width:auto!important}
.dsp-capo>.dsp-h2p{grid-column:1 / span 8}
.dsp-h2p,.dsp-h2p .elementor-heading-title{font-family:var(--alto)!important;font-weight:300!important;letter-spacing:-.012em!important;
font-size:clamp(44px,5vw,72px)!important;line-height:.94!important;color:var(--latte)!important;text-transform:none!important}
.dsp-palco{display:block!important;margin-top:clamp(36px,4vw,56px)!important;padding:0!important}
.dsp-palco>.elementor-element:not(.dsp-tappe){position:static!important}
.dsp-tappe{position:relative!important;display:block!important;height:clamp(420px,44.45vw,760px);overflow:hidden!important;touch-action:pan-y;
background:var(--grafite-2)!important;padding:0!important}
.dsp-tappa{position:absolute!important;inset:0;display:block!important;padding:0!important;width:auto!important;margin:0!important;min-height:0!important}
.dsp-tappa[hidden],.dsp-tappe:not(.dsp-pronto)>.dsp-tappa~.dsp-tappa{display:none!important}
.dsp-tappa>.dsp-foto-d,.dsp-tappa>.dsp-foto-p{position:absolute!important;inset:0;height:100%!important;width:100%!important;margin:0!important}
.dsp-tappa>*>.elementor-widget-container{height:100%}
.dsp-tappa img{width:100%!important;max-width:none!important;height:100%!important;object-fit:cover;-webkit-user-drag:none;user-select:none}
.dsp-tappa>.dsp-foto-p{display:none!important}
.dsp-testo{position:absolute!important;left:var(--m);bottom:clamp(36px,3.9vw,56px);max-width:min(40em,58%)!important;width:auto!important;
display:block!important;padding:0!important;text-shadow:0 1px 18px rgba(22,23,21,.75);font-size:clamp(17px,1.25vw,18px)}
.dsp-n{font:400 14px/1.4 var(--testo)!important;color:var(--giallo)!important}
.dsp-h3t{margin-top:6px!important}
.dsp-h3t,.dsp-h3t .elementor-heading-title{font-family:var(--alto)!important;font-weight:300!important;font-size:clamp(56px,6.1vw,88px)!important;
line-height:.92!important;letter-spacing:-.012em!important;color:var(--latte)!important;text-transform:none!important}
.dsp-frase{margin-top:14px!important;font:400 clamp(18px,1.4vw,20px)/1.45 var(--testo)!important;max-width:27em!important;color:var(--latte)!important}
.dsp-det{margin-top:12px!important;font:400 15px/1.55 var(--testo)!important;color:var(--grigio-chiaro)!important}
.dsp-det a,.dsp-det a:hover,.dsp-det a:focus{color:var(--latte)!important;text-decoration:underline!important;text-underline-offset:3px!important;
text-decoration-thickness:1px!important}
.dsp-tipo{background:var(--grafite-2)!important}
.dsp-cifre{position:absolute!important;right:var(--m);top:clamp(32px,3.6vw,52px);width:auto!important;margin:0!important}
.dsp-cifre ul{display:flex;gap:clamp(28px,3.4vw,52px)}
.dsp-cifre li,.dsp-cifre li:last-child{width:clamp(120px,12vw,180px);padding:0!important;border:0!important;margin:0!important;
font:400 15px/1.35 var(--testo)!important;color:var(--grigio-chiaro)!important;list-style:none!important}
.dsp-cifre b{display:block;margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--filo-scuro);font-family:var(--alto);font-weight:200;
font-size:clamp(220px,30vw,440px);line-height:.74;letter-spacing:-.02em;color:var(--latte);font-variant-numeric:lining-nums proportional-nums}
.dsp-indice{display:grid;grid-template-columns:repeat(5,1fr);column-gap:var(--g);padding:0 var(--m)}
.dsp-sito .dsp-indice button,.dsp-sito .dsp-indice button:hover,.dsp-sito .dsp-indice button:focus{appearance:none;background:none;border:0;
border-top:1px solid var(--filo-scuro);border-radius:0;margin:0;padding:18px 0 22px;text-align:left;cursor:pointer;color:var(--grigio-chiaro);
font:400 16px/1.3 var(--testo);letter-spacing:0;text-transform:none;white-space:normal;box-shadow:inset 0 0 0 transparent;
transition:color .12s,border-color .12s,box-shadow .12s}
.dsp-indice button .k{display:inline-block;min-width:1.4em;font-variant-numeric:tabular-nums}
.dsp-sito .dsp-indice button:hover{color:var(--latte)}
.dsp-sito .dsp-indice button[aria-selected="true"]{color:var(--latte);border-top-color:var(--giallo);box-shadow:inset 0 2px 0 var(--giallo)!important}
@media (max-width:860px){
.dsp-capo{display:block!important}
.dsp-cifre li,.dsp-cifre li:last-child{width:clamp(96px,16vw,140px)}
}
@media (min-width:561px) and (max-width:860px){
.dsp-testo{max-width:80%!important}
.dsp-tipo .dsp-testo{max-width:46%!important}
}
@media (max-width:560px){
.dsp-tappe{display:grid!important;height:auto;overflow:visible!important}
.dsp-tappa{position:relative!important;inset:auto;grid-area:1 / 1}
.dsp-tappa[hidden],.dsp-tappe:not(.dsp-pronto)>.dsp-tappa~.dsp-tappa{display:block!important;visibility:hidden}
.dsp-tappa>.dsp-foto-d{display:none!important}
.dsp-tappa>.dsp-foto-p{display:block!important;position:static!important;height:auto!important}
.dsp-tappa img{height:auto!important;aspect-ratio:1/1}
.dsp-testo{position:static!important;max-width:none!important;padding:22px var(--m) 28px!important}
.dsp-h3t,.dsp-h3t .elementor-heading-title{font-size:56px!important}
.dsp-frase{font-size:17px!important}
.dsp-tipo{display:flex!important;flex-direction:column!important}
.dsp-cifre{position:static!important;flex:1 0 auto!important;min-height:100vw;display:grid!important;align-content:end;padding:0 var(--m) 4px!important}
.dsp-cifre ul{display:grid;grid-template-columns:repeat(3,1fr);align-items:start;gap:clamp(20px,6vw,32px)}
.dsp-cifre li,.dsp-cifre li:last-child{width:auto}
.dsp-cifre b{font-size:clamp(130px,42vw,200px);margin-bottom:10px;padding-bottom:10px}
.dsp-indice{column-gap:8px}
.dsp-sito .dsp-indice button,.dsp-sito .dsp-indice button:hover,.dsp-sito .dsp-indice button:focus{font-size:13px;padding:14px 0 18px}
.dsp-indice button .k{display:block}
}
@media (max-width:359px){.dsp-sito .dsp-indice button,.dsp-sito .dsp-indice button:hover,.dsp-sito .dsp-indice button:focus{font-size:12px}}
''')

TAPPE = [
    ('Ordine', "L'ordine", "Nell'arco di una giornata l'ordine diventa una scheda di lavorazione.",
     f'Al telefono, <a class="num" href="{TEL_LINK}">{TEL}</a>, o per email a <a class="dsp-l" href="mailto:{EMAIL}">{EMAIL}</a>',
     't1-ordine-1440.webp', 't1-ordine-p-900.webp', 'Gli strati di film di una bobina, visti di taglio'),
    ('Piano', 'Il piano', 'La scheda entra nella programmazione settimanale delle linee di estrusione, poi in quella delle linee di saldatura.',
     'Il polietilene deriva dal petrolio: sugli aumenti teniamo aggiornati i clienti.',
     't2-piano-1920.webp', 't2-piano-p-700.webp',
     'Il quadro comandi di una linea di estrusione: schermo, pulsanti, due display e una nota scritta a penna in alto'),
    ('Bolla', 'La bolla', "Cinque linee di estrusione in bolla. Il film esce dalla testa, sale gonfiato d'aria fino ai rulli di traino "
     'e si avvolge in bobina.', 'Siamo in tredici, dal 2008.',
     't3-bobine-1920.webp', 't3-bobine-p-900.webp', 'Bobine di film bianco avvolte su mandrini'),
    ('Saldatura', 'La saldatura', 'Quattro linee di saldatura, ognuna per il suo sacco.', None, None, None, None),
    ('Consegna', 'La consegna', 'Consegniamo con i nostri mezzi.',
     'Carico e scarico dal lunedì al venerdì, 8:00–12:00 e 14:00–17:30',
     't5-consegna-1920.webp', 't5-consegna-p-900.webp', 'Rotoli di sacchi di polietilene pronti'),
]


def percorso():
    tappe = []
    for i, (_k, h3, frase, det, d, p, alt) in enumerate(TAPPE, 1):
        testo = [T(f'<p>{i} di 5</p>', style='n', color=GIALLO, css='dsp-n num'),
                 H(h3, level='h3', style='h3tappa', color=LATTE, css='dsp-h3t'),
                 T(f'<p>{frase}</p>', style='frase', color=LATTE, css='dsp-frase')]
        if det:
            testo.append(T(f'<p>{det}</p>', style='det', color=GRIGIO_CHIARO, link_color=LATTE, link_hover=LATTE,
                           css='dsp-det' + (' num' if i == 5 else '')))
        testo = C(*testo, boxed=False, css='dsp-testo')
        if d:
            figli = [I(img(d), alt, css='dsp-foto-d'), I(img(p), alt, css='dsp-foto-p'), testo]
            cls = 'dsp-tappa'
        else:
            # tappa 4: palco solo tipografico, le linee di saldatura come cifre
            cifre = T('<ul><li><b>2</b>per sacchi arrotolati</li><li><b>1</b>per sacchi sfusi</li><li><b>1</b>per shopper</li></ul>',
                      style='cifre', color=GRIGIO_CHIARO, css='dsp-cifre num')
            figli = [cifre, testo]
            cls = 'dsp-tappa dsp-tipo'
        tappe.append(C(*figli, boxed=False, anchor=f'tappa-{i}', css=cls))
    bottoni = ''.join(
        f'<button role="tab" id="k-{i}" aria-controls="tappa-{i}" aria-selected="{"true" if i == 1 else "false"}"'
        + ('' if i == 1 else ' tabindex="-1"') + f'><span class="k">{i}</span> {t[0]}</button>'
        for i, t in enumerate(TAPPE, 1))
    indice = RAW(f'<div class="dsp-indice" role="tablist" aria-label="Il percorso di un ordine, cinque tappe" id="dsp-indice">{bottoni}</div>'
                 + script_schede('dsp-indice', False))
    capo = C(H("Dall'ordine alla consegna", level='h2', style='h2', color=LATTE, css='dsp-h2p'), boxed=False, css='dsp-capo')
    palco = C(C(*tappe, boxed=False, css='dsp-tappe'), indice, boxed=False, css='dsp-palco')
    return C(capo, palco, stile('dsp-percorso', CSS_PERCORSO),
             boxed=False, pad=0, anchor='percorso', tag='section', bg=GRAFITE, css='dsp-percorso dsp-scuro dsp-sito')


# ---------- Clienti ----------
CSS_CLIENTI = _css('''
.dsp-clienti{display:block!important;background:var(--latte)!important;color:var(--grafite);padding:var(--r) var(--m)!important;width:100%!important;
max-width:none!important;margin:0!important}
.dsp-h2c{max-width:11em!important}
.dsp-h2c,.dsp-h2c .elementor-heading-title{font-family:var(--alto)!important;font-weight:300!important;letter-spacing:-.012em!important;
font-size:clamp(44px,6.1vw,88px)!important;line-height:.92!important;color:var(--grafite)!important;text-transform:none!important}
.dsp-gruppi{margin-top:clamp(36px,4vw,56px)!important;font:400 clamp(17px,1.25vw,18px)/1.55 var(--testo)!important;color:var(--grafite)!important}
.dsp-gruppi li,.dsp-gruppi li:last-child{padding:18px 0 26px!important;margin:0!important;border:0!important;border-top:1px solid var(--filo)!important;list-style:none!important}
.dsp-gruppi .et{display:block;font-size:14px;line-height:1.4;font-weight:600;margin-bottom:8px}
.dsp-gruppi .elenco{display:block;font-family:var(--alto);font-weight:300;font-size:clamp(32px,3.75vw,54px);line-height:1.04;letter-spacing:-.008em;max-width:25em}
@media (max-width:560px){.dsp-gruppi .elenco{font-size:32px;line-height:1.06}}
''')


def clienti():
    gruppi = [
        ('Grossisti', "Ferramenta, ingrossi di detersivi e prodotti per le pulizie, di carta e plastica, di forniture alberghiere e catering, "
                      "di materiali per l'imballaggio"),
        ('Industrie e artigiani', 'Colorifici, panifici, maglierie, tacchifici, calzaturifici, mobilifici'),
        ('Utilizzatori', 'Imprese di pulizia, mense, Ulss, cooperative, consorzi, enti'),
    ]
    lista = '<ul>' + ''.join(f'<li><span class="et">{e}</span><span class="elenco">{t}</span></li>' for e, t in gruppi) + '</ul>'
    return C(H('Per grossisti, industrie e artigiani', level='h2', style='h2grande', color=GRAFITE, css='dsp-h2c'),
             T(lista, style='gruppi', color=GRAFITE, css='dsp-gruppi'),
             stile('dsp-clienti', CSS_CLIENTI),
             boxed=False, pad=0, anchor='clienti', tag='section', css='dsp-clienti dsp-sito')


# ---------- Contatti ----------
CSS_CONTATTI = _css('''
.dsp-contatti{display:block!important;background:var(--grafite)!important;color:var(--latte);padding:var(--r) var(--m) clamp(64px,6vw,96px)!important;
width:100%!important;max-width:none!important;margin:0!important}
.dsp-h2k{max-width:11em!important}
.dsp-h2k,.dsp-h2k .elementor-heading-title{font-family:var(--alto)!important;font-weight:300!important;letter-spacing:-.012em!important;
font-size:clamp(44px,6.6vw,96px)!important;line-height:.92!important;color:var(--latte)!important;text-transform:none!important}
.dsp-grande-box{font:400 clamp(17px,1.25vw,18px)/1.55 var(--testo)!important;color:var(--latte)!important}
.dsp-grande-box a.dsp-grande,.dsp-grande-box a.dsp-grande:hover,.dsp-grande-box a.dsp-grande:focus{display:inline-block;margin-top:clamp(28px,3.4vw,48px);
font-family:var(--alto);font-weight:300;font-size:clamp(64px,17vw,250px);line-height:.86;letter-spacing:-.01em;
font-variant-numeric:lining-nums proportional-nums;text-decoration:none!important;color:var(--latte)!important;
border-bottom:2px solid var(--filo-scuro);transition:border-color .15s}
.dsp-grande-box a.dsp-grande:hover{border-bottom-color:var(--giallo)}
.dsp-recapiti{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:var(--g)!important;row-gap:32px!important;
margin-top:clamp(56px,6vw,88px)!important;padding:0!important;font-size:17px;line-height:1.5}
.dsp-recapiti>*{width:auto!important}
.dsp-recapito{display:block!important;border-top:1px solid var(--filo-scuro)!important;padding:16px 0 0!important}
.dsp-h3r,.dsp-h3r .elementor-heading-title{font-family:var(--testo)!important;font-size:14px!important;font-weight:400!important;line-height:1.5!important;
color:var(--grigio-chiaro)!important;letter-spacing:0!important;text-transform:none!important}
.dsp-h3r{margin-bottom:8px!important}
.dsp-rec{font:400 17px/1.5 var(--testo)!important;color:var(--latte)!important}
.dsp-rec a,.dsp-rec a:focus{color:var(--latte)!important;text-decoration:underline!important;text-underline-offset:4px!important;
text-decoration-thickness:1px!important;text-decoration-color:var(--grigio-chiaro)!important}
.dsp-rec a:hover{text-decoration-color:var(--giallo)!important;color:var(--latte)!important}
.dsp-rec table{border-collapse:collapse;border-spacing:0;width:auto!important;margin:0!important;font-size:inherit!important;background:none!important}
.dsp-rec table td,.dsp-rec table tbody>tr:nth-child(odd)>td,.dsp-rec table tbody tr:hover>td{padding:0 16px 0 0!important;vertical-align:baseline!important;
border:0!important;background:none!important;line-height:1.5!important}
@media (max-width:1000px){.dsp-recapiti{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.dsp-recapiti{grid-template-columns:1fr;row-gap:24px!important}}
''')

SCRIPT_MAIN = (
    # come nella statica, le sezioni dall'apertura ai contatti stanno in <main> (punto di riferimento per i lettori di schermo):
    # Elementor gratuito non ha un contenitore che le raccolga, lo fa questo script quando la pagina arriva ai contatti
    # (mai nell'editor di Elementor, che ha bisogno dei suoi elementi al loro posto)
    "<script>(function(){var a=document.getElementById('apertura'),z=document.getElementById('contatti');"
    "if(!a||!z||a.closest('main')||document.body.classList.contains('elementor-editor-active'))return;"
    "var p=a.parentNode;while(p&&!p.contains(z))p=p.parentNode;if(!p)return;"
    "while(a.parentNode!==p)a=a.parentNode;while(z.parentNode!==p)z=z.parentNode;"
    "var m=document.createElement('main');p.insertBefore(m,a);"
    "while(m.nextElementSibling){var x=m.nextElementSibling;m.appendChild(x);if(x===z)break}})();</script>"
)


def contatti():
    def recapito(titolo, html):
        return C(H(titolo, level='h3', style='h3rec', color=GRIGIO_CHIARO, css='dsp-h3r'),
                 T(html, style='rec', color=LATTE, link_color=LATTE, link_hover=LATTE, css='dsp-rec'),
                 boxed=False, css='dsp-recapito')
    recapiti = C(
        recapito('Dove', '<p>Via del Lavoro 25<br>Tombelle di Vigonovo<br><span class="num">30030</span> Vigonovo (VE)</p>'
                         f'<p><a class="dsp-l" href="{MAPPA}">Apri la mappa</a></p>'),
        recapito('Scrivere', f'<p><a class="dsp-l" href="mailto:{EMAIL}">{EMAIL}</a><br><span class="num">Fax {FAX}</span></p>'),
        recapito('Carico e scarico', '<table class="num"><tbody><tr><td>Lun–Ven</td><td>8:00–12:00</td></tr>'
                                     '<tr><td></td><td>14:00–17:30</td></tr><tr><td>Sab–Dom</td><td>chiuso</td></tr></tbody></table>'),
        recapito('Consegne', '<p>Con i nostri mezzi</p>'),
        boxed=False, css='dsp-recapiti')
    return C(H('Misure, materiale, quantità: ditecele al telefono', level='h2', style='h2contatti', color=LATTE, css='dsp-h2k'),
             T(f'<p><a class="dsp-grande num" href="{TEL_LINK}">{TEL}</a></p>', style='grande', color=LATTE, link_color=LATTE,
               link_hover=LATTE, sottolinea=False, css='dsp-grande-box'),
             recapiti,
             C(RAW(SCRIPT_MAIN, css=css_variabili() + CSS_STILE + css_testi('dsp-contatti') + CSS_CONTATTI), boxed=False, css='dsp-stile'),
             boxed=False, pad=0, anchor='contatti', tag='section', bg=GRAFITE, css='dsp-contatti dsp-scuro dsp-sito')


def home():
    return [('apertura', apertura()), ('materiali', materiali()), ('percorso', percorso()), ('clienti', clienti()),
            ('contatti', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Daisyplast, sacchi e film in polietilene a Tombelle di Vigonovo',
     'descrizione': 'Daisyplast estrude film in bolla e salda sacchi, shopper, bobine e monopieghe in polietilene vergine, '
                    'rigenerato e compostabile. Tombelle di Vigonovo (VE), dal 2008.'},
]
