# -*- coding: utf-8 -*-
"""
Contenuti della home di Mario Agnoletto per WordPress + Elementor: la home statica approvata ("Tavola dei campioni",
sito/index.html), riportata sezione per sezione nel generatore di Benvegnù (motore.py e build.py, prefisso mag).

- Widget nativi di Elementor, modificabili dal cliente: testata (menu di Ultimate Addons, telefono), titoli, testi,
  bottoni "Chiama", le dieci foto (gabbia, sei campioni, fresa, finiture, ottone), didascalie, recapiti, piede.
- Widget HTML (nodo RAW del motore) solo per quello che Elementor gratuito non fa: il logo e il timbro (SVG),
  il tacco dell'apertura con il <picture> della statica, i richiami numerati e il timbro battuto sul pezzo,
  il filtro per metallo con il suo script, la riga "Non in ...", il menu a tendina sotto i 1240 px,
  il dritto e rovescio del monogramma. Lo script è quello della pagina statica, senza librerie.
- L'impaginazione (griglia a 12 colonne, misure fluide con clamp, punti di rottura 1240, 1100, 900, 600, 360)
  è il foglio di stile della pagina statica, con le classi mag-, dentro i nodi RAW: vale uguale per il template
  Elementor e per il fallback HTML.

Testi e dati: tutti dalla home statica (le fonti sono in 01-analisi.md e in screenshot/home/NOTA.md). Nessun dato nuovo.
"""
import motore as m
from motore import C, H, B, I, RAW, MENU


def T(html, *a, **k):
    """Widget Testo. L'apostrofo è scritto &#39;: Elementor passa i testi a wptexturize, che cambierebbe ' in ’
    (nella statica è l'apostrofo diritto). Nelle righe dei testi non ci sono attributi tra apici singoli."""
    return m.T(html.replace("'", '&#39;'), *a, **k)

PREFISSO = 'mag'
NOME_SITO = 'Mario Agnoletto'

# ---------------------------------------------------------------------------------------------
# Tema: colori e carattere della home statica
# ---------------------------------------------------------------------------------------------
CARTONE = '#E7E4DD'
CARTONE_2 = '#DCD8CF'
GRAFITE = '#2A2A28'
GRAFITE_2 = '#5B5852'
FILO = 'rgba(42,42,40,.24)'
ROSSO = '#C8102E'
BIANCO = '#FFFFFF'
SU_GRAFITE = 'rgba(231,228,221,.86)'

CARATTERE = 'Host Grotesk'
# Host Grotesk non è nell'elenco dei Google Fonts di Elementor, quindi Elementor non lo chiede a Google:
# il carattere arriva dai file di assets/web/fonts/ con la regola @font-face scritta in ogni sezione (vedi css_base).
# Il motore scrive comunque un <link> ai caratteri nel fallback e nell'anteprima: qui è un foglio di stile vuoto.
FOGLIO_VUOTO = 'data:text/css,'


def _st(w, s, lh, ls=0.0):
    return dict(f=CARATTERE, w=w, s=s, lh=lh, ls=ls, up=False)


# misure (1440, 1024, 390) della pagina statica a quelle larghezze: sono i valori del pannello di Elementor;
# le misure fluide (clamp) e gli altri punti di rottura della statica sono nel foglio di stile dei widget HTML
TEMA = {
    'nome': 'Tavola dei campioni',
    'fondo': CARTONE, 'superficie': CARTONE, 'inchiostro': GRAFITE, 'testo2': GRAFITE_2, 'accento': ROSSO,
    'filetto': FILO, 'filetto_scuro': 'rgba(231,228,221,.22)', 'su_scuro2': SU_GRAFITE,
    'scuro': GRAFITE, 'su_scuro': CARTONE, 'su_accento': BIANCO,
    'font_titoli': CARATTERE, 'font_testo': CARATTERE, 'larghezza': 1440,
    'google_fonts': FOGLIO_VUOTO,
    'stili': {
        'h1':        _st('300', (134, 95, 60), 0.9, -6),
        'h2':        _st('300', (66, 47, 38), 0.98, -2.3),
        'h2m':       _st('300', (48, 35, 32), 1.02, -1.4),
        'attacco':   _st('400', (19, 17, 16.5), 1.48),
        'intro':     _st('400', (18, 18, 18), 1.5),
        'body':      _st('400', (17, 17, 16), 1.5),
        'cartellino': _st('400', (16, 16, 16), 1.5),
        'dati':      _st('400', (15, 15, 15), 1.5),
        'recapito':  _st('400', (15, 15, 15), 1.55),
        'campione':  _st('400', (14, 14, 13), 1.4),
        'piccolo':   _st('400', (13, 13, 13), 1.45),
        'piede':     _st('400', (13, 13, 13), 1.55),
        'tel':       _st('500', (15, 15, 15), 1.5),
        'tel_grande': _st('300', (76, 54, 44), 1.0, -3),
        'nav':       _st('400', (15, 15, 15), 1.5),
        'btn':       _st('500', (16, 16, 16), 1.5),
    },
    'spazi': {'sezione': (0, 0, 0), 'lato': (0, 0, 0), 'm': (0, 0, 0), 's': (0, 0, 0), '0': (0, 0, 0)},
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): l'hover cambia colore pieno, mai opacità
    'bottoni': {'grafite': (CARTONE, GRAFITE, GRAFITE, BIANCO, ROSSO, ROSSO)},
    'bottone': {'raggio': 0, 'pad': (0, 22, 0, 22), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import.
# Il resto (tacco dell'apertura, logo, timbro, carattere) resta a questo indirizzo: per non dipendere da GitHub
# l'installatore copia assets/web/ nel sito e riscrive l'indirizzo, oppure si rigenera con build.py --base.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/MarioAgnoletto-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati (come nella home statica; quelli da confermare sono nel LEGGIMI)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'049{NBSP}98{NBSP}00{NBSP}985'
TEL_HTML = '049&nbsp;98&nbsp;00&nbsp;985'
TEL_LINK = 'tel:+390499800985'
FAX_HTML = '049&nbsp;50&nbsp;31&nbsp;72'
EMAIL = 'info@marioagnoletto.it'
PEC = 'marioagnoletto@pec.it'
PIVA = '00802440271'
MAPS = 'https://www.google.com/maps/search/?api=1&amp;query=Via+dell%27Artigianato+18+Tombelle+di+Vigonovo'

# voci del menu: in WordPress è il menu "Menu Mario Agnoletto" (link personalizzati, li crea l'installatore)
VOCI_MENU = [('Lavorazioni', '/#lavorazioni'), ('Dal disegno alla serie', '/#serie'), ('Punzoni', '/#punzoni'),
             ('Dove siamo', '/#contatti')]
SLUG_MENU = 'menu-mario-agnoletto'


def ht(sel):
    """Il testo di un titolo: in Elementor sta in .elementor-heading-title dentro il widget, nel fallback è il widget stesso."""
    return f'{sel},{sel} .elementor-heading-title'


def tx(sel):
    """Un widget Testo e il suo paragrafo: stesse misure sul contenitore e sul <p> (in Elementor il carattere
    del pannello sta sul contenitore)."""
    return f'{sel},{sel} p'


def css(s):
    """Foglio di stile scritto su più righe: righe unite senza spazi (ogni riga finisce con ; { o })."""
    return ''.join(r.strip() for r in s.strip().splitlines())


# ---------------------------------------------------------------------------------------------
# Regole comuni: carattere, variabili e regole di base della statica. Ogni sezione le porta con sé
# (il fallback HTML incolla le sezioni una per una).
# ---------------------------------------------------------------------------------------------
def css_base():
    return css(f'''
    @font-face{{font-family:"Host Grotesk";src:url("{img('fonts/host-grotesk-latin.woff2')}") format("woff2");font-weight:300 800;font-style:normal;font-display:swap}}
    :root{{--cartone:#E7E4DD;--cartone-2:#DCD8CF;--grafite:#2A2A28;--grafite-2:#5B5852;--filo:rgba(42,42,40,.24);--rosso:#C8102E;
    --m:clamp(16px,4.45vw,64px);--g:clamp(12px,1.67vw,24px)}}
    body{{background:var(--cartone);color:var(--grafite);font-family:"Host Grotesk",system-ui,sans-serif;font-weight:400;font-size:17px;
    line-height:1.5;font-synthesis:none;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;overflow-x:clip}}
    @media (max-width:600px){{body{{font-size:16px}}}}
    ''')


def css_testi(s):
    """Regole di base dentro una sezione: margini del tema e di Elementor azzerati, link che prendono il colore
    del testo (il tema Hello li colora di rosa), fuoco visibile, cifre tabellari."""
    s = f'.{s}'
    return css(f'''
    {s}{{font-family:"Host Grotesk",system-ui,sans-serif;font-weight:400;font-size:17px;line-height:1.5;color:var(--grafite);
    font-synthesis:none;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;box-sizing:border-box}}
    @media (max-width:600px){{{s}{{font-size:16px}}}}
    {s} *,{s} *::before,{s} *::after{{box-sizing:border-box}}
    {s} .elementor-widget-text-editor,{s} .elementor-widget-heading{{color:inherit}}
    {s} p{{margin:0!important;text-wrap:pretty}}
    {s} h1,{s} h2,{s} h3,{s} .elementor-heading-title{{margin:0;padding:0;text-wrap:balance}}
    {s} .elementor-widget:not(:last-child){{margin-block-end:0}}
    {s} a{{color:inherit!important;text-decoration:underline!important;text-decoration-thickness:1px!important;text-underline-offset:.22em!important;
    transition:none}}
    {s} a:hover{{color:var(--rosso)!important}}
    {s} :focus-visible{{outline:2px solid var(--grafite);outline-offset:3px}}
    {s} a:focus-visible,{s} button:focus-visible,{s} summary:focus-visible{{box-shadow:none;outline:2px solid var(--grafite)!important;outline-offset:3px!important}}
    {s} img{{display:block;max-width:100%;height:auto;border:0;border-radius:0;box-shadow:none}}
    {s} .num{{font-variant-numeric:tabular-nums lining-nums}}
    ''')


def stile(*fogli):
    """Widget HTML con il solo foglio di stile della sezione, dentro un contenitore nascosto (non occupa posto)."""
    return C(RAW('', css=''.join(fogli)), boxed=False, css='mag-stile')


CSS_STILE = '.mag-stile{display:none!important}'

# bottone "Chiama": in Elementor .elementor-button, nel fallback l'unico <a> del widget
CSS_BOTTONE = css('''
.mag-bottone a{display:inline-flex!important;align-items:center!important;min-height:48px;padding:0 22px!important;
background:var(--grafite)!important;color:var(--cartone)!important;text-decoration:none!important;font-family:"Host Grotesk",system-ui,sans-serif!important;
font-weight:500!important;font-size:16px!important;line-height:1.5!important;letter-spacing:0!important;text-transform:none!important;
border:0!important;border-radius:0!important;box-shadow:none!important;font-variant-numeric:tabular-nums lining-nums;white-space:nowrap;
transition:background-color .18s ease!important;vertical-align:baseline}
.mag-bottone a:focus:not(:hover),.mag-bottone a:focus-visible:not(:hover){background:var(--grafite)!important;color:var(--cartone)!important}
.mag-bottone a:hover{background:var(--rosso)!important;color:#fff!important}
.mag-bottone .elementor-button-content-wrapper,.mag-bottone .elementor-button-text{display:inline;color:inherit}
''')

# i titoli di sezione (h2) e l'etichetta con la lettera della sezione (A, B, C, D)
CSS_TITOLI = css(f'''
{ht('.mag-h2')}{{font-family:"Host Grotesk",system-ui,sans-serif!important;font-weight:300!important;font-size:clamp(38px,4.6vw,66px)!important;
line-height:.98!important;letter-spacing:-.035em!important;text-transform:none!important;color:inherit}}
{ht('.mag-h2m')}{{font-family:"Host Grotesk",system-ui,sans-serif!important;font-weight:300!important;font-size:clamp(32px,3.4vw,48px)!important;
line-height:1.02!important;letter-spacing:-.03em!important;text-transform:none!important;color:inherit}}
{tx('.mag-tav')}{{font-size:13px!important;line-height:1.45!important}}
.mag-tav{{margin:0 0 22px!important}}
.mag-tav p{{display:flex;gap:18px;align-items:baseline;color:var(--grafite-2)}}
.mag-tav span{{white-space:nowrap}}
''')

CSS_GRIGLIA = css('''
.mag-griglia{display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--g)!important;row-gap:0!important;
padding:0 var(--m)!important;margin:0!important;width:100%!important;max-width:none!important}
:where(.mag-griglia)>*{grid-column:1/-1}
.mag-griglia>*{width:auto!important;max-width:none!important;margin:0}
.mag-intro{grid-column:1/span 7;display:block!important;padding:0!important}
.mag-intro-p{margin-top:22px!important;max-width:34em!important}
.mag-intro-p,.mag-intro-p p{font-size:18px!important;line-height:1.5!important;color:var(--grafite)}
@media (max-width:1100px){.mag-intro{grid-column:1/span 10}}
''')

CSS_SEZIONE = css('''
.mag-sezione{padding:clamp(88px,10vw,148px) 0 0!important;display:block!important;margin:0!important;width:100%!important;max-width:none!important}
''')

# il riquadro di una foto: l'immagine lo riempie (object-fit cover), come .foto img della statica
CSS_RIQUADRO = css('''
.mag-riquadro{position:relative!important;overflow:hidden!important;display:block!important;padding:0!important;margin:0!important}
.mag-riquadro>.mag-img{position:absolute!important;inset:0;width:100%!important;height:100%!important;max-width:none!important;margin:0!important;line-height:0}
.mag-riquadro img{width:100%!important;height:100%!important;max-width:none!important;object-fit:cover!important;display:block!important}
''')


# =============================================================================================
# TESTATA (template "Mario Agnoletto: Header", da mettere su tutto il sito con Ultimate Addons)
# =============================================================================================
CSS_TESTATA = css('''
.mag-testata{position:absolute!important;inset:0 0 auto 0;z-index:5;display:flex!important;flex-direction:row!important;flex-wrap:nowrap!important;
align-items:center!important;gap:24px!important;height:84px;padding:0 var(--m)!important;margin:0!important;width:100%!important;max-width:none!important;
background:none!important}
.mag-testata>*{flex:0 0 auto!important;width:auto!important;max-width:none!important;margin:0}
.mag-testata a.mag-logo{display:block;text-decoration:none!important}
.mag-testata .mag-logo img{width:206px;height:auto}
.mag-nav{margin-left:clamp(32px,4vw,64px)!important}
.mag-nav .hfe-nav-menu__layout-horizontal .hfe-nav-menu,.mag-nav .mag-nav-l{display:flex!important;flex-wrap:nowrap;gap:30px!important;justify-content:flex-start!important}
.mag-nav .hfe-nav-menu>li.menu-item,.mag-nav .mag-nav-l li{margin:0!important;padding:0!important}
.mag-nav .hfe-nav-menu::before,.mag-nav .hfe-nav-menu::after{display:none!important}
.mag-nav .hfe-nav-menu a.hfe-menu-item,.mag-nav .mag-nav-l a{display:inline!important;padding:0!important;font-family:inherit!important;font-size:15px!important;
font-weight:400!important;line-height:1.5!important;letter-spacing:0!important;text-transform:none!important;color:var(--grafite)!important;
text-decoration:none!important;white-space:nowrap;border:0!important;background:none!important}
.mag-nav .hfe-nav-menu a.hfe-menu-item:hover,.mag-nav .mag-nav-l a:hover{color:var(--rosso)!important;text-decoration:underline!important}
.mag-nav a.hfe-menu-item::before,.mag-nav a.hfe-menu-item::after{display:none!important}
.mag-nav .hfe-nav-menu__toggle,.mag-nav details{display:none!important}
.mag-nav,.mag-nav nav,.mag-nav .hfe-nav-menu__layout-horizontal{font-size:15px;line-height:1.5}
.mag-tel{margin-left:auto!important}
.mag-tel,.mag-tel p{font-size:15px!important;line-height:1.5!important}
.mag-tel p{text-wrap:wrap}
.mag-tel a{font-weight:500;text-decoration:none!important;white-space:nowrap}
.mag-menu-box{display:none!important;padding:0!important;position:relative}
.mag-menu{position:relative}
.mag-testata .mag-menu summary{list-style:none;cursor:pointer;font-size:15px;font-weight:500;line-height:1.5;min-height:44px;display:flex;align-items:center}
.mag-menu summary::-webkit-details-marker{display:none}
.mag-testata .mag-menu ul{position:absolute;right:0;top:100%;margin:0;min-width:220px;padding:18px 22px;list-style:none;background:var(--cartone);
box-shadow:0 0 0 1px var(--filo);display:grid;gap:12px;font-size:16px;line-height:1.5}
.mag-testata .mag-menu li{margin:0;padding:0}
.mag-menu[open] ul a{display:block;min-height:32px}
@media (max-width:1240px){.mag-nav{display:none!important}.mag-menu-box{display:block!important;margin-left:auto!important}.mag-tel{margin-left:0!important}}
@media (max-width:600px){.mag-testata{height:68px}.mag-testata .mag-logo img{width:158px}.mag-tel{display:none!important}}
@media (max-width:360px){.mag-testata .mag-logo img{width:140px}}
''')

CSS_TESTATA_ELEMENTOR = css('''
#masthead{position:static}
html{scroll-behavior:auto!important}
.hfe-skip-link{display:none!important}
.mag-nav .hfe-nav-menu li.current-menu-item>a.hfe-menu-item:not(:hover){color:var(--grafite)!important;text-decoration:none!important}
''')

SCRIPT_MENU = (
    "<script>(function(){var menu=document.querySelector('.mag-menu');if(!menu)return;"
    # il menu in riga ha lo stesso nome della statica ("Sezioni"), in Elementor e nel fallback
    "var nv=document.querySelector('.mag-nav nav, nav.mag-nav');if(nv)nv.setAttribute('aria-label','Sezioni');"
    # le voci del menu di Ultimate Addons saltano alla sezione come nella statica: senza questo il plugin anima lo
    # scorrimento per 0,8 s anche con "riduci movimento"; il clic arriva al browser, che va all'ancora subito
    # (non nell'editor, dove il clic serve a scegliere il widget)
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.mag-nav .hfe-nav-menu a[href*=\"#\"]');"
    "if(a&&!document.body.classList.contains('elementor-editor-active'))e.stopPropagation()},true);"
    # le voci sono quelle del menu di WordPress (Ultimate Addons) o del menu del fallback, se ci sono
    "var fonte=document.querySelector('.mag-nav ul');var ul=menu.querySelector('ul');"
    "if(fonte&&ul){var v=fonte.querySelectorAll('a');if(v.length){ul.innerHTML='';v.forEach(function(x){"
    "var li=document.createElement('li'),a=document.createElement('a');a.href=x.getAttribute('href');"
    "a.textContent=x.textContent.trim();li.appendChild(a);ul.appendChild(li)})}}"
    # menu a tendina: si chiude scegliendo una voce, con Esc e toccando fuori (come la statica)
    "menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){menu.open=false})});"
    "document.addEventListener('keydown',function(e){if(e.key==='Escape'&&menu.open){menu.open=false;menu.querySelector('summary').focus()}});"
    "document.addEventListener('click',function(e){if(menu.open&&!menu.contains(e.target))menu.open=false})})();</script>"
)


def header():
    logo = RAW(f'<a class="mag-logo" href="/" aria-label="Mario Agnoletto, incisore meccanico: torna all\'inizio">'
               f'<img src="{img("logo.svg")}" alt="Mario Agnoletto" width="206" height="42"></a>',
               css=css_base() + css_testi('mag-testata') + CSS_STILE + CSS_TESTATA)
    menu = MENU(VOCI_MENU, slug=SLUG_MENU, colore=GRAFITE, colore_hover=ROSSO, accento=ROSSO, fondo_menu=CARTONE, linea=FILO,
                stile='nav', spazio=30, pad_h=0, pad_v=0, distanza=6, align_menu='left', css='mag-nav')
    voci = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in VOCI_MENU)
    tendina = C(RAW(f'<details class="mag-menu"><summary>Menu</summary><ul>{voci}</ul></details>' + SCRIPT_MENU),
                boxed=False, css='mag-menu-box')
    tel = T(f'<p><a href="{TEL_LINK}">{TEL_HTML}</a></p>', style='tel', color=GRAFITE, link_color=GRAFITE, link_hover=ROSSO,
            sottolinea=False, css='mag-tel num')
    # solo in Elementor: le regole per Ultimate Addons e per la testata del tema
    elementor = RAW('', css=CSS_TESTATA_ELEMENTOR, solo_elementor=True)
    return C(logo, menu, tendina, tel, C(elementor, boxed=False, css='mag-stile'),
             dir='row', align='center', gap=24, boxed=False, pad=0, css='mag-testata mag-sito')


# =============================================================================================
# PIEDE (template "Mario Agnoletto: Footer")
# =============================================================================================
CSS_PIEDE = css('''
.mag-piede{padding:36px var(--m) 40px!important;display:grid!important;grid-template-columns:repeat(12,minmax(0,1fr));column-gap:var(--g)!important;
row-gap:16px!important;align-items:start!important;margin:0!important;width:100%!important;max-width:none!important;background:none!important}
.mag-piede>*{width:auto!important;max-width:none!important;margin:0}
.mag-logo-box{grid-column:1/span 3;display:block!important;padding:0!important}
.mag-piede a.mag-logo{display:block;text-decoration:none!important}
.mag-piede .mag-logo img{width:168px;height:auto}
.mag-piede-p{grid-column:4/span 6}
.mag-piede-p,.mag-piede-p p{font-size:13px!important;line-height:1.55!important;color:var(--grafite-2)!important}
.mag-piede-2{grid-row:2}
@media (max-width:900px){.mag-logo-box,.mag-piede-p{grid-column:1/-1;justify-self:start}.mag-piede-2{grid-row:auto}}
''')


def footer():
    logo = C(RAW(f'<a class="mag-logo" href="/"><img src="{img("logo.svg")}" alt="Mario Agnoletto" width="168" height="34"></a>',
                 css=css_base() + css_testi('mag-piede') + CSS_STILE + CSS_PIEDE), boxed=False, css='mag-logo-box')
    p1 = T(f"<p>Agnoletto Mario, impresa individuale, incisore meccanico dal 1979. Via dell'Artigianato 18, 30030 Tombelle di Vigonovo (VE). "
           f'P.IVA {PIVA}.</p>', style='piede', color=GRAFITE_2, css='mag-piede-p num')
    p2 = T('<p>La foto della fresa (B, Prototipo) è di repertorio (Unsplash); le altre sono pezzi dell\'officina.</p>',
           style='piede', color=GRAFITE_2, css='mag-piede-p mag-piede-2')
    # niente tag footer: in WordPress il piede sta già dentro il <footer id="colophon"> di Ultimate Addons
    # (un footer dentro un footer non è HTML valido), come la testata sta nel suo <header id="masthead">
    return C(logo, p1, p2, boxed=False, pad=0, css='mag-piede mag-sito')


# =============================================================================================
# HOME
# =============================================================================================
CSS_APERTURA = css(f'''
.mag-apertura{{position:relative!important;height:100svh;min-height:760px;max-height:1040px;overflow:hidden!important;display:block!important;
padding:0!important;margin:0!important;width:100%!important;max-width:none!important}}
.mag-testo{{position:absolute!important;left:var(--m);top:clamp(150px,20vh,196px);width:min(46vw,720px)!important;z-index:2;display:block!important;
padding:0!important;margin:0!important}}
{ht('.mag-h1')}{{font-family:"Host Grotesk",system-ui,sans-serif!important;font-weight:300!important;font-size:clamp(60px,9.3vw,152px)!important;
line-height:.9!important;letter-spacing:-.045em!important;text-transform:none!important;color:var(--grafite)!important;margin:0}}
.mag-attacco{{margin-top:36px!important;max-width:27em!important}}
{tx('.mag-attacco')}{{font-size:19px!important;line-height:1.48!important}}
.mag-contatto{{margin-top:30px!important;display:flex!important;flex-direction:row!important;flex-wrap:wrap!important;align-items:baseline!important;
gap:8px 28px!important;padding:0!important}}
.mag-contatto>*{{width:auto!important;max-width:none!important;flex:0 1 auto!important;margin:0}}
.mag-contatto>.mag-bottone{{display:flex}}
{tx('.mag-dove')}{{font-size:15px!important;line-height:1.5!important;color:var(--grafite-2)!important;text-wrap:wrap}}
.mag-tavola-box{{position:absolute!important;top:0;right:0;height:100%;aspect-ratio:744/1084;margin:0!important;padding:0!important;display:block!important;
width:auto!important;max-width:none!important}}
.mag-tavola-box>*{{height:100%;width:100%}}
.mag-tavola{{position:relative;margin:0;height:100%;width:100%}}
.mag-tavola picture,.mag-tavola .mag-pezzo{{display:block;width:100%;height:100%}}
.mag-tavola .richiamo{{position:absolute;display:flex;align-items:center;gap:8px;font-size:12.5px;line-height:1;white-space:nowrap;transform:translate(-6px,-50%)}}
.mag-tavola .richiamo::before{{content:"";flex:none;width:9px;height:9px;border-radius:50%;background:var(--grafite);box-shadow:0 0 0 3px rgba(231,228,221,.9)}}
.mag-tavola .richiamo b{{font-weight:500;font-variant-numeric:tabular-nums}}
.mag-tavola .richiamo.sx{{flex-direction:row-reverse;transform:translate(calc(-100% + 6px),-50%)}}
.mag-tavola .richiamo i{{display:block;width:40px;height:1px;background:var(--grafite)}}
.mag-tavola .richiamo.lungo i{{width:72px}}
.mag-tavola .richiamo.lunghissimo i{{width:116px}}
.mag-tavola .richiamo.p{{display:none}}
.mag-legenda{{position:absolute!important;left:var(--m);bottom:30px;z-index:2;margin:0!important;width:auto!important;max-width:none!important}}
{tx('.mag-legenda')}{{font-size:13px!important;line-height:1.45!important;color:var(--grafite-2)!important}}
.mag-legenda p{{display:flex;gap:18px;align-items:baseline}}
.mag-legenda .num{{font-weight:500;color:var(--grafite)}}
.mag-legenda span:first-child{{white-space:nowrap}}
.mag-tavola .timbro{{position:absolute;width:112px;height:112px;transform:translate(-50%,-50%) rotate(-11deg);mix-blend-mode:multiply;z-index:1;pointer-events:none;max-width:none}}
.mag-tavola .timbro.p{{display:none}}
@media (max-width:1100px){{
.mag-testo{{width:min(50vw,520px)!important;top:150px}}
.mag-attacco{{max-width:24em!important}}
{tx('.mag-attacco')}{{font-size:17px!important}}
.mag-tavola .timbro{{width:96px;height:96px}}
}}
@media (min-width:601px) and (max-width:900px){{
.mag-apertura .mag-tavola-box{{width:min(58vw,430px)!important;align-self:flex-start}}
.mag-tavola .richiamo i{{width:18px}}
.mag-tavola .richiamo.lungo i{{width:44px}}
}}
@media (max-width:900px){{
.mag-apertura{{height:auto;min-height:0;max-height:none;overflow:visible!important;display:flex!important;flex-direction:column!important;align-items:stretch!important}}
.mag-tavola-box{{position:relative!important;top:auto;right:auto;height:auto;width:min(84vw,560px)!important;order:-1}}
.mag-tavola .richiamo.l{{display:none}}
.mag-tavola .richiamo.p{{display:flex}}
.mag-tavola .timbro.l{{display:none}}
.mag-tavola .timbro.p{{display:block;width:84px;height:84px}}
.mag-testo{{position:relative!important;left:auto;top:auto;width:auto!important;padding:4px var(--m) 0!important;margin-top:-6px!important}}
.mag-legenda{{position:relative!important;left:auto;bottom:auto;padding:22px var(--m) 0!important}}
}}
@media (max-width:600px){{
.mag-tavola-box{{width:86vw!important}}
{ht('.mag-h1')}{{font-size:clamp(50px,15.4vw,72px)!important;line-height:.92!important}}
.mag-attacco{{margin-top:20px!important}}
{tx('.mag-attacco')}{{font-size:16.5px!important}}
.mag-contatto{{margin-top:22px!important}}
.mag-tavola .richiamo{{font-size:11px;gap:6px}}
.mag-tavola .richiamo i{{width:18px}}
.mag-tavola .richiamo.lungo i{{width:44px}}
.mag-tavola .timbro.p{{width:68px;height:68px}}
}}
@media (max-width:360px){{
.mag-tavola .richiamo.p.sx:not(.lungo) i{{display:none}}
.mag-tavola .richiamo.p{{gap:4px}}
.mag-tavola .timbro.p{{width:58px;height:58px}}
}}
''')


def apertura():
    testo = C(
        H('Incisore<br>meccanico', level='h1', style='h1', color=GRAFITE, css='mag-h1'),
        T('<p>Fibbie, puntali, tacchi gioiello, punzoni e fustelle su disegno, per la calzatura e la pelletteria. '
          'Seguiamo il pezzo dal progetto alla serie, in zama, ottone, alluminio e acciaio.</p>',
          style='attacco', color=GRAFITE, css='mag-attacco'),
        C(B(f'Chiama {TEL}', TEL_LINK, variant='grafite', css='mag-bottone'),
          T('<p>Tombelle di Vigonovo (VE), dal 1979</p>', style='dati', color=GRAFITE_2, css='mag-dove'),
          dir='row', wrap=True, align='baseline', boxed=False, css='mag-contatto'),
        boxed=False, css='mag-testo')
    tavola = C(RAW(
        '<figure class="mag-tavola"><picture>'
        f'<source media="(max-width: 900px)" srcset="{img("tacco-p-400.webp")} 400w, {img("tacco-p-744.webp")} 744w" sizes="86vw">'
        f'<img class="mag-pezzo" src="{img("tacco-l-744.webp")}" srcset="{img("tacco-l-480.webp")} 480w, {img("tacco-l-744.webp")} 744w" '
        'sizes="69vh" width="744" height="1084" fetchpriority="high" '
        'alt="Un tacco gioiello a lamelle in ottone visto dall\'alto: l\'anello d\'appoggio, quattro lamelle e lo stelo in cui si innestano">'
        '</picture>'
        '<span class="richiamo l sx lunghissimo" style="left:64.25%;top:79.34%"><i></i><b>1</b> Anello</span>'
        '<span class="richiamo l" style="left:72.18%;top:42.62%"><i></i><b>2</b> Lamelle</span>'
        '<span class="richiamo l lungo" style="left:43.41%;top:27.03%"><i></i><b>3</b> Asola</span>'
        '<span class="richiamo l lungo" style="left:36.69%;top:18.36%"><i></i><b>4</b> Stelo</span>'
        '<span class="richiamo p" style="left:35.62%;top:79.34%"><i></i><b>1</b> Anello</span>'
        '<span class="richiamo p sx" style="left:27.69%;top:42.62%"><i></i><b>2</b> Lamelle</span>'
        '<span class="richiamo p sx lungo" style="left:56.45%;top:27.03%"><i></i><b>3</b> Asola</span>'
        '<span class="richiamo p sx lungo" style="left:63.17%;top:18.36%"><i></i><b>4</b> Stelo</span>'
        f'<img class="timbro l" src="{img("timbro.svg")}" alt="" width="112" height="112" style="left:74.87%;top:89.76%">'
        f'<img class="timbro p" src="{img("timbro.svg")}" alt="" width="84" height="84" style="left:25.0%;top:89.76%">'
        '</figure>',
        css=css_base() + css_testi('mag-apertura') + CSS_STILE + CSS_BOTTONE + CSS_APERTURA),
        boxed=False, css='mag-tavola-box')
    legenda = T("<p><span class=\"num\">01</span><span>Tacco gioiello a lamelle in ottone, visto dall'alto</span></p>",
                style='piccolo', color=GRAFITE_2, css='mag-legenda')
    return C(testo, tavola, legenda, boxed=False, pad=0, tag='section', css='mag-apertura mag-sito')


# --- A. Campionario ---------------------------------------------------------------------------
CSS_CAMPIONARIO = css('''
.mag-filtro{margin-top:40px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.mag-sito .mag-filtro button,.mag-sito .mag-filtro button:focus{appearance:none;-webkit-appearance:none;font:inherit;font-size:15px;line-height:1.5;
color:var(--grafite);background:transparent;border:1px solid var(--filo);border-radius:0;min-height:46px;padding:0 18px 0 14px;display:inline-flex;
align-items:center;gap:10px;cursor:pointer;text-transform:none;letter-spacing:0;white-space:nowrap;user-select:auto;
transition:background-color .16s ease,color .16s ease,border-color .16s ease}
.mag-sito .mag-filtro button:hover{border-color:var(--grafite);color:var(--grafite);background:transparent}
.mag-sito .mag-filtro button[aria-pressed="true"],.mag-sito .mag-filtro button[aria-pressed="true"]:hover,
.mag-sito .mag-filtro button[aria-pressed="true"]:focus{background:var(--grafite);color:var(--cartone);border-color:var(--grafite)}
.mag-filtro .campo{width:18px;height:18px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.mag-filtro .campo.tutti{background:conic-gradient(#8E959B 0 25%,#C5A465 0 50%,#D9DBDC 0 75%,#6E7377 0)}
.mag-filtro .campo.zama{background:linear-gradient(135deg,#B9BEC2,#7F868C)}
.mag-filtro .campo.ottone{background:linear-gradient(135deg,#E6CC8E,#A8844C)}
.mag-filtro .campo.alluminio{background:linear-gradient(135deg,#F3F4F4,#B9BCBF)}
.mag-filtro .campo.acciaio{background:linear-gradient(135deg,#A9AEB2,#4F5458)}
.mag-filtro .mag-conteggio{margin-left:auto!important;color:var(--grafite-2);font-size:15px;line-height:1.5}
.mag-filtro .mag-conteggio b{font-weight:500;color:var(--grafite)}
.mag-campioni{margin-top:28px!important;display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr));gap:44px var(--g)!important;
container-type:inline-size;padding:0!important}
.mag-campione{margin:0!important;position:relative!important;display:block!important;padding:0!important;width:auto!important;max-width:none!important}
.mag-foto{aspect-ratio:1;background:var(--cartone-2)!important}
.mag-campione.largo{grid-column:span 2}
.mag-campione.largo .mag-foto{aspect-ratio:auto;height:calc((100cqw - 3 * var(--g)) / 4)}
.mag-campione.grande{grid-column:span 2;grid-row:span 2;display:flex!important;flex-direction:column!important;flex-wrap:nowrap!important}
.mag-campione.grande .mag-foto{aspect-ratio:auto;flex:1 1 auto!important;min-height:0}
.mag-foto.pelle{background:#3a2c22!important}
.mag-cap{margin-top:14px!important}
.mag-cap,.mag-cap p{font-size:14px!important;line-height:1.4!important;color:var(--grafite)}
.mag-cap p{display:grid;grid-template-columns:2.2em 1fr;column-gap:6px;text-wrap:wrap}
.mag-cap .n{font-variant-numeric:tabular-nums;color:var(--grafite-2)}
.mag-cap .nome{font-size:17px;font-weight:500;line-height:1.25}
.mag-cap .met{grid-column:2;color:var(--grafite-2)}
.mag-cap .desc{grid-column:2;margin-top:6px;max-width:30em!important}
.mag-campione.acceso .mag-foto::after{content:"";position:absolute;top:12px;right:12px;width:12px;height:12px;border-radius:50%;background:var(--rosso);
box-shadow:0 0 0 3px var(--cartone-2);z-index:1}
.mag-campioni.filtrato .mag-campione{grid-column:auto;grid-row:auto;display:block!important}
.mag-campioni.filtrato .mag-campione .mag-foto{aspect-ratio:1;height:auto}
.mag-campioni.filtrato .mag-campione.spento{display:none!important}
.mag-altri-box{grid-column:1/-1;display:none!important;padding:0!important;margin:0!important}
.mag-campioni.filtrato .mag-altri-box{display:block!important}
.mag-altri{margin:36px 0 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:14px;line-height:1.5;color:var(--grafite-2)}
.mag-altri[hidden]{display:none}
.mag-altri li{margin:0}
.mag-altri .tit{margin-right:8px}
.mag-altri li.c{display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 12px;box-shadow:inset 0 0 0 1px var(--filo)}
.mag-altri li.c b{font-weight:400;font-variant-numeric:tabular-nums}
@media (max-width:1100px){.mag-cap .desc{font-size:13px}}
@media (max-width:900px){
.mag-campioni{grid-template-columns:repeat(2,minmax(0,1fr));gap:36px var(--g)!important}
.mag-campione.grande{grid-row:auto}
.mag-campione.largo .mag-foto{height:auto;aspect-ratio:2/1}
.mag-campione.largo{grid-column:1/-1}
.mag-campione.grande .mag-foto{aspect-ratio:4/5}
}
@media (max-width:600px){
.mag-filtro{gap:8px}
.mag-sito .mag-filtro button,.mag-sito .mag-filtro button:focus{min-height:44px;padding:0 13px 0 11px;font-size:14px}
.mag-filtro .mag-conteggio{margin:6px 0 0!important;flex-basis:100%}
.mag-campioni{gap:30px 12px!important}
.mag-campione.largo,.mag-campione.grande{grid-column:1/-1}
.mag-cap p{grid-template-columns:1.9em 1fr}
.mag-cap,.mag-cap p{font-size:13px!important}
.mag-cap .nome{font-size:15px}
.mag-cap .desc{font-size:13px}
}
''')

# lo script del filtro della statica: i metalli di ogni campione sono nelle classi mag-m-<metallo> del suo contenitore
# (Elementor gratuito non dà attributi data- ai contenitori), numero e nome nelle classi n e nome della didascalia
SCRIPT_FILTRO = (
    "<script>(function(){var filtro=document.querySelector('.mag-filtro'),tavola=document.querySelector('.mag-campioni');"
    "if(!filtro||!tavola)return;"
    "var bottoni=filtro.querySelectorAll('button');var campioni=tavola.querySelectorAll('.mag-campione');"
    "var altri=tavola.querySelector('.mag-altri');var conteggio=filtro.querySelector('.mag-conteggio');"
    "var nomi={tutti:'',zama:'Zama',ottone:'Ottone',alluminio:'Alluminio',acciaio:'Acciaio'};"
    "function metalli(c){var m=[];c.classList.forEach(function(k){if(k.indexOf('mag-m-')===0)m.push(k.slice(6))});return ' '+m.join(' ')+' '}"
    "function scegli(m,daUtente){if(nomi[m]===undefined)m='tutti';var n=0,fuori=[];"
    "campioni.forEach(function(c){var ok=m==='tutti'||metalli(c).indexOf(' '+m+' ')>-1;"
    "c.classList.toggle('spento',!ok);c.classList.toggle('acceso',ok&&m!=='tutti');"
    "if(ok)n++;else fuori.push('<li class=\"c\"><b>'+c.querySelector('.n').textContent+'</b>'+c.querySelector('.nome').textContent+'</li>')});"
    "tavola.classList.toggle('filtrato',m!=='tutti');altri.hidden=m==='tutti';"
    "altri.innerHTML=m==='tutti'?'':'<li class=\"tit\">Non in '+nomi[m].toLowerCase()+':</li>'+fuori.join('');"
    "bottoni.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.m===m?'true':'false')});"
    "conteggio.innerHTML=m==='tutti'?'<b class=\"num\">7</b> lavorazioni in tavola':nomi[m]+': <b class=\"num\">'+n+'</b> '+(n===1?'lavorazione':'lavorazioni')+' su 7';"
    "if(daUtente&&history.replaceState)history.replaceState(null,'',m==='tutti'?location.pathname+location.search:'#metallo='+m)}"
    "bottoni.forEach(function(b){b.addEventListener('click',function(){scegli(b.dataset.m,true)})});"
    "function daIndirizzo(){var q=(location.hash.match(/metallo=(\\w+)/)||[])[1];if(q)scegli(q,false)}"
    "window.addEventListener('hashchange',daIndirizzo);daIndirizzo()})();</script>"
)

# i sette campioni: (classi, file, alt, numero, nome, metalli, riga, metalli del filtro)
CAMPIONI = [
    ('grande', 't-tacchi-660.webp', "Un tacco gioiello a gabbia in acciaio lucido, visto dall'alto",
     '01', 'Tacchi gioiello', 'ottone, acciaio, alluminio', 'A gabbia, a lamelle o a stelo, su disegno.', 'ottone acciaio alluminio'),
    ('', 't-punzoni-700.webp', "Cliché in ottone inciso con un cavallo e il suo guidatore, visto dall'alto",
     '02', 'Punzoni e alfabeti', 'acciaio, ottone', 'Per stampare pelle e cuoio, anche in set di alfabeti.', 'acciaio ottone'),
    ('', 't-fustelle-720.webp', 'Stampo in acciaio a due fiori, con i segni della fresa',
     '03', 'Fustelle', 'ottone, alluminio, acciaio', 'Per tagliare e stampare pelle, cuoio e tessuto.', 'ottone alluminio acciaio'),
    ('', 't-ruote-820.webp', "Ruota forata in acciaio vista dall'alto",
     '04', 'Ruote e rulli', 'acciaio', 'Ruote in acciaio e rulli.', 'acciaio'),
    ('', 't-bigiotteria-1080.webp', 'Farfalle in metallo lucido traforate a ovali',
     '05', 'Bigiotteria', 'finiture preziose', 'Anelli, bracciali, spille e pendagli, con cristalli e pietre.', ''),
    ('largo', 't-accessori-1180.webp', 'Due fibbie in ottone lucido, una con le borchie a punta',
     '06', 'Accessori', 'zama, ottone, alluminio, acciaio', 'Fibbie, morsetti, talloni, puntali e copritacchi, con qualsiasi finitura o verniciatura.',
     'zama ottone alluminio acciaio'),
    ('largo pelle', 't-stampa-960.webp', 'Pelle argento goffrata e cuoio marrone stampato a rilievo con un motivo a grappolo',
     '07', 'Stampa e foratura su pelle', 'servizio, su pelle', 'Con un catalogo di lavorazioni pronte.', ''),
]


def campionario():
    filtro = RAW(
        '<div class="mag-filtro" id="metalli" role="group" aria-label="Filtra per metallo">'
        '<button type="button" data-m="tutti" aria-pressed="true"><span class="campo tutti" aria-hidden="true"></span>Tutti</button>'
        '<button type="button" data-m="zama" aria-pressed="false"><span class="campo zama" aria-hidden="true"></span>Zama</button>'
        '<button type="button" data-m="ottone" aria-pressed="false"><span class="campo ottone" aria-hidden="true"></span>Ottone</button>'
        '<button type="button" data-m="alluminio" aria-pressed="false"><span class="campo alluminio" aria-hidden="true"></span>Alluminio</button>'
        '<button type="button" data-m="acciaio" aria-pressed="false"><span class="campo acciaio" aria-hidden="true"></span>Acciaio</button>'
        '<p class="mag-conteggio" aria-live="polite"><b class="num">7</b> lavorazioni in tavola</p></div>',
        css=css_base() + css_testi('mag-lavorazioni') + CSS_STILE + CSS_SEZIONE + CSS_GRIGLIA + CSS_TITOLI + CSS_RIQUADRO + CSS_CAMPIONARIO)
    campioni = []
    for classi, file, alt, n, nome, met, desc, metalli in CAMPIONI:
        pelle = ' pelle' if 'pelle' in classi else ''
        forma = classi.replace('pelle', '').strip()
        cl = ' '.join(['mag-campione'] + ([forma] if forma else []) + [f'mag-m-{x}' for x in metalli.split()])
        campioni.append(C(
            C(I(img(file), alt, css='mag-img'), boxed=False, css='mag-riquadro mag-foto' + pelle),
            T(f'<p><span class="n">{n}</span><span class="nome">{nome}</span><span class="met">{met}</span><span class="desc">{desc}</span></p>',
              style='campione', color=GRAFITE, css='mag-cap'),
            boxed=False, css=cl))
    altri = C(RAW('<ul class="mag-altri" hidden></ul>' + SCRIPT_FILTRO), boxed=False, css='mag-altri-box')
    griglia = C(
        T('<p><span>A</span><span>Campionario</span></p>', style='piccolo', color=GRAFITE_2, css='mag-tav'),
        C(H('Otto lavorazioni, quattro metalli', level='h2', style='h2', color=GRAFITE, css='mag-h2'),
          T("<p>Due famiglie di pezzi: gli attrezzi per chi lavora la pelle e i pezzi che finiscono sulla scarpa, sulla borsa, in vetrina. "
            "In tavola ce ne sono sette; l'ottava sono le targhe da esposizione, in alluminio, ottone e plexiglas.</p>",
            style='intro', color=GRAFITE, css='mag-intro-p'),
          boxed=False, css='mag-intro'),
        filtro,
        C(*campioni, altri, boxed=False, css='mag-campioni'),
        boxed=False, css='mag-griglia')
    return C(griglia, boxed=False, pad=0, anchor='lavorazioni', tag='section', css='mag-sezione mag-lavorazioni mag-sito')


# --- B. Dal disegno alla serie ---------------------------------------------------------------
CSS_SERIE = css('''
.mag-dittico{display:grid!important;grid-template-columns:7fr 5fr;gap:6px!important;margin-top:56px!important;padding:0!important;width:100%!important}
.mag-fig{margin:0!important;display:block!important;padding:0!important;width:auto!important;max-width:none!important}
.mag-foto-d{height:clamp(300px,44vw,640px)}
.mag-figcap{padding:16px var(--m) 0!important}
.mag-figcap,.mag-figcap p{font-size:15px!important;line-height:1.5!important}
.mag-figcap p{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;text-wrap:wrap}
.mag-fig:first-child .mag-figcap{padding-right:0!important}
.mag-fig:last-child .mag-figcap{padding-left:0!important}
.mag-figcap b{font-weight:500;font-size:17px}
@media (max-width:600px){
.mag-dittico{grid-template-columns:1fr;gap:28px!important}
.mag-foto-d{height:auto;aspect-ratio:4/3}
.mag-figcap,.mag-fig:first-child .mag-figcap,.mag-fig:last-child .mag-figcap{padding:12px var(--m) 0!important}
}
''')


def serie():
    def fig(file, alt, titolo, testo):
        return C(C(I(img(file), alt, css='mag-img'), boxed=False, css='mag-riquadro mag-foto-d'),
                 T(f'<p><b>{titolo}</b><span>{testo}</span></p>', style='dati', color=GRAFITE, css='mag-figcap'),
                 boxed=False, css='mag-fig')
    griglia = C(
        T('<p><span>B</span><span>Un pezzo, tre passaggi</span></p>', style='piccolo', color=GRAFITE_2, css='mag-tav'),
        C(H('Dal disegno alla serie', level='h2', style='h2', color=GRAFITE, css='mag-h2'),
          T("<p>Si parte da un'idea del cliente: ne seguiamo la progettazione, lo sviluppo del prototipo e la produzione in serie.</p>",
            style='intro', color=GRAFITE, css='mag-intro-p'),
          boxed=False, css='mag-intro'),
        boxed=False, css='mag-griglia')
    dittico = C(
        fig('fresa-2100.webp', 'Una fresa al lavoro su un pezzo in rame', 'Prototipo', 'Il primo pezzo, prima della serie. Foto di repertorio.'),
        fig('finiture-670.webp', "Una fibbia a catena cromata e una placca in ottone con l'inserto martellato, su pelle stampata",
            'Serie', 'Pezzi finiti, con qualsiasi finitura o verniciatura.'),
        boxed=False, css='mag-dittico')
    return C(griglia, dittico,
             stile(css_base(), css_testi('mag-serie'), CSS_STILE, CSS_SEZIONE, CSS_GRIGLIA, CSS_TITOLI, CSS_RIQUADRO, CSS_SERIE),
             boxed=False, pad=0, anchor='serie', tag='section', css='mag-sezione mag-serie mag-sito')


# --- C. Punzoni -------------------------------------------------------------------------------
CSS_PUNZONI = css('''
.mag-punzoni{position:relative!important;margin:clamp(72px,7vw,104px) 0 0!important;display:block!important;padding:0!important;width:100%!important;max-width:none!important}
.mag-foto-p{height:clamp(420px,58vw,820px)}
.mag-foto-p img{object-position:50% 40%!important}
.mag-didascalia{margin:14px var(--m) 0 auto!important;max-width:34em!important;width:auto!important;text-align:right}
.mag-didascalia,.mag-didascalia p{font-size:13px!important;line-height:1.5!important;color:var(--grafite-2)!important;text-align:right}
.mag-cartellino{position:absolute!important;left:var(--m);bottom:calc(var(--m) * 0.9);width:min(440px,calc(100% - 2 * var(--m)))!important;max-width:none!important;
background:var(--cartone)!important;padding:30px 32px 32px!important;display:block!important;margin:0!important}
/* come nella statica, dove la regola del cartellino sui paragrafi vale anche per l'etichetta: 16 px */
.mag-cartellino .mag-tav{margin:0 0 18px!important}
.mag-cartellino .mag-tav,.mag-cartellino .mag-tav p{font-size:16px!important}
.mag-cart-p{margin-top:14px!important}
.mag-cart-p,.mag-cart-p p{font-size:16px!important;line-height:1.5!important}
.mag-cartellino .mag-bottone{margin-top:24px!important;font-size:17px;line-height:1.5}
.mag-specchio{margin:26px 0 0;display:flex;gap:26px;align-items:flex-start;padding-top:20px;border-top:1px solid var(--filo)}
.mag-specchio div{display:flex;align-items:center;gap:12px;font-size:13px;line-height:1.35;color:var(--grafite-2)}
.mag-specchio img{width:52px;height:52px;flex:none}
.mag-specchio .rovescio img{transform:scaleX(-1)}
@media (max-width:600px){
.mag-cartellino .mag-bottone{font-size:16px}
.mag-foto-p{height:auto;aspect-ratio:4/3}
.mag-cartellino{position:relative!important;left:auto;bottom:auto;width:auto!important;margin:-48px var(--m) 0!important;padding:24px 22px 26px!important}
.mag-didascalia,.mag-didascalia p{text-align:left}
.mag-didascalia{margin:14px var(--m) 0!important}
.mag-specchio{gap:18px}
}
''')


def punzoni():
    foto = C(I(img('ottone-1920.webp'), "Ottone inciso dall'alto: un cliché a foglie, due bordi a spina e un blocchetto forato, sopra una lastra traforata",
               css='mag-img'), boxed=False, css='mag-riquadro mag-foto-p')
    cartellino = C(
        T('<p><span>C</span><span>Punzoni e alfabeti</span></p>', style='piccolo', color=GRAFITE_2, css='mag-tav'),
        H('Punzoni anche in 24 ore', level='h2', style='h2m', color=GRAFITE, css='mag-h2m'),
        T('<p>In acciaio e ottone, per stampare pelle e cuoio, anche in set di alfabeti per la personalizzazione. La grafica la sviluppiamo noi.</p>',
          style='cartellino', color=GRAFITE, css='mag-cart-p'),
        B(f'Chiama {TEL}', TEL_LINK, variant='grafite', css='mag-bottone'),
        RAW(f'<div class="mag-specchio"><div class="rovescio"><img src="{img("timbro-grafite.svg")}" alt="" width="52" height="52">'
            '<span>Sul punzone,<br>a rovescio</span></div>'
            f'<div><img src="{img("timbro.svg")}" alt="" width="52" height="52"><span>Sulla pelle,<br>dritto</span></div></div>',
            css=css_base() + css_testi('mag-punzoni') + CSS_STILE + CSS_TITOLI + CSS_RIQUADRO + CSS_BOTTONE + CSS_PUNZONI),
        boxed=False, css='mag-cartellino')
    didascalia = T("<p>Ottone inciso dell'officina: un cliché a foglie, due bordi a spina, un blocchetto forato, sopra una lastra traforata.</p>",
                   style='piccolo', color=GRAFITE_2, css='mag-didascalia')
    return C(foto, cartellino, didascalia, boxed=False, pad=0, anchor='punzoni', tag='section', css='mag-punzoni mag-sito')


# --- D. Dove siamo ----------------------------------------------------------------------------
CSS_CONTATTI = css('''
.mag-contatti{background:var(--grafite)!important;color:var(--cartone)!important;padding:clamp(72px,8vw,120px) 0 clamp(56px,6vw,88px)!important;
display:block!important;margin:0!important;width:100%!important;max-width:none!important}
.mag-contatti a:hover{color:#fff!important}
.mag-contatti .mag-tav p{color:rgba(231,228,221,.62)}
.mag-contatti .mag-h2,.mag-contatti .mag-h2 .elementor-heading-title{color:var(--cartone)!important}
.mag-sinistra{grid-column:1/span 6;display:block!important;padding:0!important}
.mag-destra{grid-column:8/span 5;padding:40px 0 0!important;display:block!important}
.mag-chi{margin-top:26px!important;max-width:30em!important}
.mag-chi,.mag-chi p{font-size:18px!important;line-height:1.5!important;color:rgba(231,228,221,.86)!important}
.mag-tel-grande,.mag-tel-grande p{font-size:17px!important;line-height:1.5!important;color:var(--cartone)!important}
.mag-tel-grande a{display:inline-block;font-size:clamp(44px,5.3vw,78px);font-weight:300;letter-spacing:-.04em;line-height:1;text-decoration:none!important;white-space:nowrap}
.mag-recapiti{margin-top:40px!important;display:grid!important;grid-template-columns:1fr 1fr;column-gap:var(--g)!important;row-gap:28px!important;
padding:24px 0 0!important;border-top:1px solid rgba(231,228,221,.22)!important;width:100%!important}
.mag-recapiti>*{width:auto!important;max-width:none!important;margin:0}
.mag-recapito,.mag-recapito p{font-size:15px!important;line-height:1.55!important;color:var(--cartone)!important}
.mag-recapito p,.mag-tel-grande p{text-wrap:wrap}
.mag-recapito .etichetta{display:block;color:rgba(231,228,221,.6);margin-bottom:8px;font-size:11.5px;line-height:1.3;font-weight:500;letter-spacing:.12em;
text-transform:uppercase}
@media (max-width:900px){.mag-sinistra,.mag-destra{grid-column:1/-1}.mag-destra{padding-top:56px!important}}
@media (max-width:600px){.mag-tel-grande,.mag-tel-grande p{font-size:16px!important}.mag-recapiti{grid-template-columns:1fr}
.mag-destra{padding-top:44px!important}}
@media (max-width:360px){.mag-tel-grande a{font-size:38px}}
''')

# come nella statica, le sezioni dall'apertura ai contatti stanno in <main> (punto di riferimento per i lettori di schermo):
# Elementor gratuito non ha un contenitore che le raccolga, lo fa questo script quando la pagina arriva ai contatti
# (anche nel fallback, dove ogni sezione sta nel suo blocco; mai nell'editor di Elementor)
SCRIPT_MAIN = (
    "<script>(function(){var a=document.querySelector('.mag-apertura'),z=document.getElementById('contatti');"
    "if(!a||!z||a.closest('main')||document.body.classList.contains('elementor-editor-active'))return;"
    "var p=a.parentNode;while(p&&!p.contains(z))p=p.parentNode;if(!p)return;"
    "while(a.parentNode!==p)a=a.parentNode;while(z.parentNode!==p)z=z.parentNode;"
    "var m=document.createElement('main');p.insertBefore(m,a);"
    "while(m.nextElementSibling){var x=m.nextElementSibling;m.appendChild(x);if(x===z)break}})();</script>"
)


def contatti():
    def recapito(html, extra=''):
        return T(f'<p>{html}</p>', style='recapito', color=CARTONE, link_color=CARTONE, link_hover=BIANCO, sottolinea=False,
                 css=('mag-recapito ' + extra).strip())
    sinistra = C(
        T('<p><span>D</span><span>Dove siamo</span></p>', style='piccolo', color='rgba(231,228,221,.62)', css='mag-tav'),
        H('Tombelle di Vigonovo, nella Riviera del Brenta', level='h2', style='h2', color=CARTONE, css='mag-h2'),
        T('<p>Lavoriamo soprattutto per calzaturifici e pelletterie. Le targhe e gli articoli da vetrina sono per i negozi e i vetrinisti.</p>',
          style='intro', color=SU_GRAFITE, css='mag-chi'),
        boxed=False, css='mag-sinistra')
    destra = C(
        T(f'<p><a href="{TEL_LINK}">{TEL_HTML}</a></p>', style='tel_grande', color=CARTONE, link_color=CARTONE, link_hover=BIANCO,
          sottolinea=False, css='mag-tel-grande num'),
        C(recapito("<span class=\"etichetta\">Officina</span>Via dell'Artigianato 18<br>30030 Tombelle di Vigonovo (VE)<br>"
                   f'<a href="{MAPS}">Apri in Google Maps</a>'),
          recapito(f'<span class="etichetta">Scrivere</span><a href="mailto:{EMAIL}">{EMAIL}</a><br>PEC <a href="mailto:{PEC}">{PEC}</a>'),
          recapito(f'<span class="etichetta">Telefono e fax</span>Tel. <a href="{TEL_LINK}">{TEL_HTML}</a><br>Fax {FAX_HTML}', 'num'),
          recapito(f'<span class="etichetta">Ditta</span>Agnoletto Mario<br>impresa individuale<br>P.IVA <span class="num">{PIVA}</span>'),
          dir='row', wrap=True, boxed=False, css='mag-recapiti'),
        boxed=False, css='mag-destra')
    griglia = C(sinistra, destra, boxed=False, css='mag-griglia')
    return C(griglia,
             C(RAW(SCRIPT_MAIN, css=css_base() + css_testi('mag-contatti') + CSS_STILE + CSS_GRIGLIA + CSS_TITOLI + CSS_CONTATTI),
               boxed=False, css='mag-stile'),
             boxed=False, pad=0, anchor='contatti', tag='section', css='mag-contatti mag-sito')


def home():
    return [('apertura', apertura()), ('lavorazioni', campionario()), ('serie', serie()), ('punzoni', punzoni()),
            ('contatti', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Mario Agnoletto, incisore meccanico a Tombelle di Vigonovo',
     'descrizione': 'Fibbie, puntali, tacchi gioiello, punzoni e fustelle su disegno per calzatura e pelletteria. '
                    'Zama, ottone, alluminio e acciaio, dal progetto alla serie.'},
]
