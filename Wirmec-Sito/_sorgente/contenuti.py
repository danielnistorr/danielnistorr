# -*- coding: utf-8 -*-
"""
Contenuti del sito Wirmec S.r.l. (Ponte San Nicolò, Padova).
Direzione: "il lavoro in primo piano" (specifica _prova/spec.md, paragrafo 0), con gli innesti di "misura" e "luogo".
- apertura: la macchina vera scontornata sul grigio studio, codice e valori sotto (Hermle C 12, Universal Robots UR7e);
- le dodici lavorazioni sul cavo nei disegni Wirmec, alla stessa scala (Komax StripCrimp 208, "Processing capabilities");
- una fascia ardesia per pagina, tabelle e righe di dati con filetto forte sopra (Schleuniger, Komax, Salvagnini B3);
- il codice come titolo (Hermle, Universal Robots), il telefono del commerciale sempre a vista (TRUMPF).
Caratteri e colori: accoppiata A di 02 (IBM Plex Sans Condensed, Plex Sans, Plex Mono; ardesia, grigio studio e rosso
del sito attuale). Fonti dei testi: 01-analisi-sito-attuale.md (testi verbatim, schede, PDF), Registro delle Imprese.
"""
from urllib.parse import quote

import motore as m
from motore import C, H, T, B, I, LINEA_H, RAW, MENU, SHORTCODE

PREFISSO = 'wrm'
NOME_SITO = 'Wirmec'

# ---------------------------------------------------------------------------------------------
# Tema (specifica, paragrafo 1)
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'
GRIGIO = '#E6E6E6'          # grigio studio: fondo delle foto WB 10, WPB 10, WSC 15
ARDESIA = '#323A41'         # la barra della testata del sito attuale: una fascia per pagina
NOTTE = '#1F2429'           # piè di pagina
INK = '#1F2429'             # testo e titoli su chiaro (15,64:1 su bianco)
TESTO2 = '#5C6369'          # testo secondario (6,10:1 su bianco, 4,89:1 sul grigio)
SU_SCURO2 = '#D6DADE'       # testo su ardesia (8,22:1)
SU_SCURO3 = '#B3BAC0'       # etichette su ardesia (5,89:1)
PIEDE2 = '#C9CED3'          # testo del piede (9,87:1 su notte)
ROSSO = '#E20004'           # rosso Wirmec: pulsante pieno, filetto sotto gli H2, voce attiva, anello del fuoco
ROSSO_SCURO = '#9B1517'     # hover dei pulsanti rossi, link su bianco e su grigio (8,36:1 e 6,69:1)
FILETTO = '#CDD1D5'         # righe su bianco
FILETTO_G = '#B8BEC4'       # righe sul grigio studio
FILETTO_S = '#4A535B'       # righe su ardesia e notte
TRASP = 'rgba(0,0,0,0)'

COND = 'IBM Plex Sans Condensed'
SANS = 'IBM Plex Sans'
MONO = 'IBM Plex Mono'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


TEMA = {
    'nome': 'Lavoro',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': INK, 'testo2': TESTO2, 'accento': ROSSO,
    'filetto': FILETTO, 'filetto_scuro': FILETTO_S, 'su_scuro2': SU_SCURO2,
    'scuro': ARDESIA, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': COND, 'font_testo': SANS, 'larghezza': 1280,
    'google_fonts': ('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600'
                     '&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap'),
    'stili': {
        'codice':  _st(COND, '600', (176, 128, 88), 0.86, -1),       # solo "W 1500" in home
        'h1':      _st(COND, '600', (64, 52, 40), 1.02, -0.5),
        'h2':      _st(COND, '600', (48, 40, 32), 1.05, -0.3),
        'h3':      _st(COND, '600', (28, 26, 24), 1.15),
        'nome':    _st(COND, '600', (22, 21, 20), 1.2),
        'nome_s':  _st(COND, '600', (18, 18, 18), 1.2),             # nomi dei distributori in Azienda
        'cifra':   _st(COND, '600', (64, 52, 44), 0.95),
        'tel':     _st(COND, '600', (56, 48, 40), 1.0),
        'nav':     _st(COND, '500', (18, 18, 18), 1.2),
        'nav_m':   _st(COND, '600', (26, 26, 24), 1.25),
        'lead':    _st(SANS, '400', (20, 19, 18), 1.55),
        'body':    _st(SANS, '400', (17, 17, 16), 1.65),
        'small':   _st(SANS, '400', (15, 15, 14), 1.55),
        'piede':   _st(SANS, '400', (15, 15, 15), 1.9),
        'meta':    _st(SANS, '400', (13, 13, 13), 1.45),
        'label':   _st(SANS, '500', (13, 13, 13), 1.3),
        'kicker':  _st(SANS, '500', (15, 15, 14), 1.3),
        'link':    _st(SANS, '600', (15, 15, 15), 1.4),
        'btn':     _st(SANS, '600', (16, 16, 16), 1.2),
        'dato':    _st(MONO, '500', (17, 17, 16), 1.3),
        'dato_l':  _st(MONO, '500', (18, 18, 17), 1.3),            # i quattro valori sotto la macchina d’apertura
        'dato_s':  _st(MONO, '500', (14, 14, 13), 1.4),
        'tel_s':   _st(MONO, '500', (15, 15, 15), 1.2),            # telefono in testata
    },
    'spazi': {
        'sezione': (112, 88, 64), 'lato': (48, 32, 20), 'xl': (72, 56, 40), 'l': (48, 40, 32), 'm': (32, 24, 20),
        's': (20, 16, 16), 'xs': (12, 12, 10), 'xxs': (6, 6, 6), 'col': (48, 32, 20), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): colore pieno in hover, mai opacità
    'bottoni': {
        'primario': (BIANCO, ROSSO, ROSSO, BIANCO, ROSSO_SCURO, ROSSO_SCURO),
        'contorno': (INK, TRASP, INK, BIANCO, INK, INK),
        'contorno-bianco': (BIANCO, TRASP, BIANCO, INK, BIANCO, BIANCO),
    },
    'bottone': {'raggio': 0, 'pad': (16, 26, 16, 26), 'bordo': 2, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell’import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Wirmec-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


def pdf(nome):
    return BASE + 'pdf/' + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (un solo posto da aggiornare; fonti in 01, "Dati aziendali")
# ---------------------------------------------------------------------------------------------
NB = ' '                     # spazio indivisibile: telefoni, "20 kN", "W 1500" non vanno a capo
WJ = '⁠'                     # word joiner: niente a capo dentro "PD-391905"
TEL = f'+39{NB}049{NB}718{NB}464'
TEL_LINK = 'tel:+39049718464'
FAX = f'+39{NB}049{NB}896{NB}6147'
EMAIL = 'info@wirmec.com'
PEC = 'wirmecsrl@legalmail.it'                   # [DA CONFERMARE su INI-PEC]
INDIRIZZO = 'Viale Europa 16'                     # [DA CONFERMARE: 16 nel registro, 4/4A nella privacy]
CITTA = f'35020 Ponte San Nicolò{NB}(PD)'
PIVA = '04468400280'
REA = f'PD{WJ}-{WJ}391905'
CAPITALE = f'50.000{NB}euro'
LINKEDIN = 'https://www.linkedin.com/company/wirmec'
PAYOFF = '....the right partner for Harness Makers'   # il payoff del marchio, in inglese come nel logo


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    if corpo:
        url += '&body=' + quote(corpo)
    return url


def richiesta(linea='', modello=''):
    """Link al modulo di Contatti con la linea (e il modello) già scelti (specifica 5.1 e 13)."""
    q = []
    if linea:
        q.append('linea=' + linea)
    if modello:
        q.append('modello=' + quote(modello))
    return '/contatti/' + ('?' + '&'.join(q) if q else '') + '#richiesta'


# ---------------------------------------------------------------------------------------------
# Stile comune (vale in Elementor e nel fallback HTML; ogni sezione ne porta una copia nel suo RAW)
# ---------------------------------------------------------------------------------------------
F_MONO = f"'{MONO}',ui-monospace,Menlo,monospace"
F_SANS = f"'{SANS}',Arial,sans-serif"
F_COND = f"'{COND}','Arial Narrow',Arial,sans-serif"

CSS_COMUNE = (
    # link di testo: rosso scuro su chiaro, sottolineatura 1 px; in hover inchiostro e sottolineatura 2 px
    '.wrm-link a{text-underline-offset:4px!important}'
    '.wrm-link a:hover,.wrm-link a:focus-visible{text-decoration-thickness:2px!important}'
    # freccia dopo i link di navigazione: si sposta di 4 px (niente opacità)
    '.wrm-fr{position:relative;left:0;transition:left .15s ease}'
    'a:hover .wrm-fr,a:focus-visible .wrm-fr,.wrm-cl:hover .wrm-fr,.wrm-cl:focus-visible .wrm-fr{left:4px}'
    # contenitori-link: in hover il nome passa al rosso scuro, nessuna ombra e nessun sollevamento
    '.wrm-cl{text-decoration:none!important;color:inherit}'
    f'.wrm-cl:hover .wrm-nome,.wrm-cl:hover .wrm-nome .elementor-heading-title,'
    f'.wrm-cl:focus-visible .wrm-nome,.wrm-cl:focus-visible .wrm-nome .elementor-heading-title{{color:{ROSSO_SCURO}!important}}'
    f'.wrm-cl:focus-visible{{outline:2px solid {ROSSO};outline-offset:-2px}}'
    # righe di dati (<dl> in un Editor di testo): etichetta a sinistra, valore in Plex Mono a destra
    '.wrm-dl dl{margin:0;padding:0}'
    f'.wrm-dl dl>div{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:13px 0;'
    f'border-bottom:1px solid {FILETTO};margin:0}}'
    '.wrm-dl dt{margin:0;font-weight:500}'
    f'.wrm-dl dd{{margin:0;text-align:right;text-wrap:balance;font:500 17px/1.3 {F_MONO};color:{INK};font-variant-numeric:tabular-nums}}'
    f'.wrm-dl-forte dl{{border-top:2px solid {INK}}}'
    f'.wrm-dl-grigio dl>div{{border-color:{FILETTO_G}}}'
    '@media (max-width:767px){.wrm-dl dd{font-size:16px}}'
    f'.wrm-dl-scuro dl>div{{border-color:{FILETTO_S}}}.wrm-dl-scuro dd{{color:{BIANCO}}}.wrm-dl-scuro dd a{{color:{BIANCO}!important}}'
    f'.wrm-dl-scuro.wrm-dl-forte dl{{border-top-color:{BIANCO}}}'
    # registro (Azienda): etichetta al 40%, valore a sinistra al 60%; sul telefono uno sotto l'altro
    '.wrm-dl-reg dl>div{display:grid;grid-template-columns:40% 60%;gap:0;align-items:baseline;min-height:52px;box-sizing:border-box}'
    '.wrm-dl-reg dd{text-align:left;text-wrap:pretty}'
    '@media (max-width:767px){.wrm-dl-reg dl>div{grid-template-columns:100%;gap:4px}}'
    # n.d.: dato non pubblicato nella scheda, in grigio e più piccolo
    f'.wrm-nd{{font-size:14px!important;color:{TESTO2}!important;font-family:{F_MONO}}}'
    # ancore dei codici: il titolo non finisce sotto la testata
    '[id]{scroll-margin-top:100px}@media (max-width:1024px){[id]{scroll-margin-top:80px}}'
    # testo forte nelle didascalie
    f'.wrm-meta strong{{font-weight:600;color:{INK}}}'
    '@media (prefers-reduced-motion:reduce){.wrm-fr{transition:none}}'
    # testi che non vanno mai a capo (codice W 1500, telefono grande): sui tablet stretti e sui telefoni piccoli
    # la misura scende con la larghezza della finestra invece di uscire dalla colonna
    '@media (min-width:768px) and (max-width:1024px){.wrm-codice,.wrm-codice .elementor-heading-title'
    '{font-size:min(128px,13.4vw)!important}.wrm-tel-g,.wrm-tel-g .elementor-heading-title{font-size:min(48px,5.7vw)!important}}'
    '@media (min-width:1025px){.wrm-codice,.wrm-codice .elementor-heading-title{font-size:min(176px,calc(15.6vw - 32px))!important}'
    '.wrm-tel-g,.wrm-tel-g .elementor-heading-title{font-size:min(56px,calc(5.8vw - 6px))!important}}'
    '@media (max-width:767px){.wrm-codice,.wrm-codice .elementor-heading-title{font-size:min(88px,25vw)!important}'
    '.wrm-tel-g,.wrm-tel-g .elementor-heading-title{font-size:min(40px,11.5vw)!important}}'
)


def stile(*parti):
    """Foglio di stile di una sezione: un widget HTML vuoto con <style> (in Elementor) e lo stesso CSS nel fallback."""
    return RAW('', css=CSS_COMUNE + ''.join(parti))


# ---------------------------------------------------------------------------------------------
# Componenti riutilizzabili (anche per le pagine 02-07)
# ---------------------------------------------------------------------------------------------
def sezione(*children, bg=BIANCO, pad=('sezione', 'lato'), css='', **p):
    """Sezione a larghezza piena con contenuto di 1280; spazi tra i figli dati con mt (gap 0), CSS in fondo."""
    extra = p.pop('stile_extra', '')
    p.setdefault('gap', '0')
    return C(*children, stile(extra), bg=bg, pad=pad, tag='section', css=css, **p)


def freccia(testo):
    return f'{testo}&nbsp;<span class="wrm-fr" aria-hidden="true">→</span>'


def link_freccia(testo, url, scuro=False, **p):
    """Link di testo sottolineato con freccia (stile `link`): rosso scuro su chiaro, bianco su ardesia."""
    colore, hover = (BIANCO, SU_SCURO2) if scuro else (ROSSO_SCURO, INK)
    classi = ('wrm-link ' + p.pop('css', '')).strip()
    return T(f'<p><a href="{url}">{freccia(testo)}</a></p>', style='link', color=colore, link_color=colore,
             link_hover=hover, css=classi, **p)


def filetto_rosso(larghezza=40, **p):
    """Filetto rosso 40 x 3 sotto gli H2 di sezione (72 x 3 sotto il codice W 1500)."""
    return LINEA_H(ROSSO, weight=3, larghezza=(larghezza, larghezza, larghezza), **p)


def titolo_h2(testo, colore=INK, filetto=True, **p):
    """H2 di sezione con il filetto rosso sotto (margine `s`): ritorna una lista da spargere in un contenitore a gap 0."""
    out = [H(testo, 'h2', color=colore, **p)]
    if filetto:
        out.append(filetto_rosso(mt='s'))
    return out


def testa(titolo, lead, colore=INK, colore_lead=TESTO2, stile_lead='lead'):
    """Testa di sezione: H2 con filetto a sinistra, lead a destra allineato in basso; su tablet e telefono in colonna."""
    return C(C(*titolo_h2(titolo, colore), w=(50, 100, 100)),
             C(T(f'<p>{lead}</p>', style=stile_lead, color=colore_lead, max_w=(560, 760, 560)), w=(50, 100, 100),
               mt=(0, 'm', 'm')),
             dir='row', dir_t='column', align=('end', 'start', 'start'), gap='0')


def dati_dl(coppie, varianti='', colore_et=TESTO2, stile='label', **p):
    """Righe di dati: <dl> con etichetta (label) e valore (Plex Mono).
    varianti: 'wrm-dl-forte', 'wrm-dl-grigio', 'wrm-dl-scuro' (su ardesia), 'wrm-dl-reg' (valore a sinistra, 40/60)."""
    righe = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in coppie)
    return T(f'<dl>{righe}</dl>', style=stile, color=colore_et, css=f'wrm-dl {varianti}'.strip(), **p)


def nome(testo, colore=INK, livello='p', **p):
    """Nome o codice di un modello (stile `nome`); dentro un contenitore-link cambia colore in hover."""
    classi = ('wrm-nome ' + p.pop('css', '')).strip()
    return H(testo, livello, style=p.pop('style', 'nome'), color=colore, css=classi, **p)


def didascalia(html, colore=TESTO2, **p):
    return T(f'<p>{html}</p>', style='meta', color=colore, css='wrm-meta', **p)


# ---------------------------------------------------------------------------------------------
# Testata e piede (template separati; con Ultimate Addons diventano header e footer di tutto il sito)
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Automatiche', '/automatiche/'), ('Da banco', '/da-banco/'), ('Applicatori', '/applicatori/'),
             ('Controllo qualità', '/controllo-qualita/'), ('Azienda', '/azienda/'), ('Contatti', '/contatti/')]

ICONA_MENU = (f'linear-gradient({INK},{INK}) 0 0/20px 2px no-repeat,linear-gradient({INK},{INK}) 0 6px/20px 2px no-repeat,'
              f'linear-gradient({INK},{INK}) 0 12px/20px 2px no-repeat')
ICONA_X = (f'linear-gradient(45deg,transparent calc(50% - 1px),{INK} calc(50% - 1px),{INK} calc(50% + 1px),transparent calc(50% + 1px)),'
           f'linear-gradient(-45deg,transparent calc(50% - 1px),{INK} calc(50% - 1px),{INK} calc(50% + 1px),transparent calc(50% + 1px))')

# solo Elementor (tema Hello, Ultimate Addons): regole generali della pagina
CSS_BASE = (
    'em,i,cite{font-style:normal}'
    # come nel fallback: l'immagine non aggiunge lo spazio della riga di testo sotto di sé
    '.elementor-widget-image{line-height:0}.elementor-widget-image img{vertical-align:top}'
    f'a:focus-visible,button:focus-visible,[role=button]:focus-visible,input:focus-visible,select:focus-visible,'
    f'textarea:focus-visible,summary:focus-visible{{outline:2px solid {ROSSO};outline-offset:3px}}'
    f'.wrm-scuro a:focus-visible,.wrm-piede a:focus-visible{{outline-color:{BIANCO}}}'
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    f"a.hfe-skip-link:focus{{background:{INK};color:{BIANCO};border-radius:0;box-shadow:none;outline:2px solid {BIANCO};"
    f"outline-offset:-4px;font:600 15px/1 {F_SANS};text-decoration:none;padding:16px 24px}}"
    # menu Ultimate Addons su una riga a desktop; voce attiva: linea rossa 3 px a filo del filetto della testata
    '@media (min-width:1025px){.wrm-testata .hfe-nav-menu__layout-horizontal .hfe-nav-menu{flex-wrap:nowrap}'
    '.wrm-testata .hfe-nav-menu .hfe-menu-item{white-space:nowrap}}'
    f'.wrm-testata .hfe-nav-menu .menu-item a.hfe-menu-item:hover,.wrm-testata .hfe-nav-menu .menu-item a.hfe-menu-item:focus-visible'
    f'{{color:{ROSSO_SCURO}}}'
    '.wrm-testata .hfe-pointer__underline .menu-item:not(.current-menu-item) a.hfe-menu-item::after{background-color:transparent!important}'
    '.wrm-testata .hfe-pointer__underline a.hfe-menu-item::after{height:3px!important;bottom:0!important}'
    # pulsante del menu: quadrato 48 x 48 con bordo, tre linee 20 x 2 (X quando è aperto)
    f'.wrm-testata .hfe-nav-menu__toggle{{width:48px;height:48px;box-sizing:border-box;border:2px solid {INK};border-radius:0;'
    'align-items:center;justify-content:center;margin:0!important;cursor:pointer}'
    '@media (max-width:1024px){.wrm-testata .hfe-nav-menu__toggle{display:flex!important}}'
    f'.wrm-testata .hfe-nav-menu__toggle .hfe-nav-menu-icon{{width:20px;height:14px;padding:0!important;border:0!important;'
    f'background:{ICONA_MENU}!important;font-size:0!important;line-height:0}}'
    '.wrm-testata .hfe-nav-menu__toggle .hfe-nav-menu-icon i,.wrm-testata .hfe-nav-menu__toggle .hfe-nav-menu-icon svg{display:none!important}'
    f'.wrm-testata .hfe-nav-menu__toggle.hfe-active-menu .hfe-nav-menu-icon{{width:18px;height:18px;background:{ICONA_X}!important}}'
    '@media (hover:hover){'
    f'.wrm-testata .hfe-nav-menu__toggle:hover{{background:{INK}}}'
    f'.wrm-testata .hfe-nav-menu__toggle:hover .hfe-nav-menu-icon{{background:{ICONA_MENU.replace(INK, BIANCO)}!important}}'
    f'.wrm-testata .hfe-nav-menu__toggle.hfe-active-menu:hover .hfe-nav-menu-icon{{background:{ICONA_X.replace(INK, BIANCO)}!important}}}}'
    # menu a scomparsa: righe alte 56 con filetto, voce attiva rosso scuro sottolineata (niente bordo sinistro)
    '@media (max-width:1024px){'
    f'.wrm-testata .hfe-dropdown .menu-item a.hfe-menu-item{{padding:12px 32px!important;border-bottom:1px solid {FILETTO}!important}}'
    f'.wrm-testata .hfe-dropdown .current-menu-item a.hfe-menu-item{{color:{ROSSO_SCURO}!important;text-decoration:underline;'
    'text-decoration-thickness:2px;text-underline-offset:6px}'
    '.wrm-testata .hfe-dropdown a.hfe-menu-item::after{display:none!important}}'
    '@media (max-width:767px){.wrm-testata .hfe-dropdown .menu-item a.hfe-menu-item{padding:12px 20px!important}'
    '.wrm-testata .hfe-nav-menu__toggle{width:44px;height:44px}}'
)

# testata: vale in tutte e due le build
CSS_TESTATA = (
    '.wrm-testata{overflow-x:clip}'
    # tra 1025 e 1299 px il telefono lascia il posto al menu; sotto i 1200 voci a 16 px e margini di 32
    '@media (min-width:1025px) and (max-width:1299px){.wrm-testata .wrm-tel{display:none!important}'
    '.wrm-testata .wrm-btn-t{margin-left:auto!important}}'
    '@media (min-width:1025px) and (max-width:1199px){'
    '.wrm-testata .hfe-nav-menu>li.menu-item:not(:last-child){margin-right:16px!important}'
    '.wrm-testata a.hfe-menu-item,.wrm-testata .wrm-nav-l a{font-size:16px!important}.wrm-testata .wrm-nav-l{gap:16px!important}'
    '.wrm-testata>.e-con,.wrm-testata>.wrm-con{padding-left:32px!important;padding-right:32px!important}}'
    '@media (min-width:1025px){.wrm-testata .wrm-menu{margin-left:24px!important}.wrm-testata .wrm-tel{margin-left:auto!important}}'
    '@media (max-width:1024px){.wrm-testata .wrm-chiama{margin-left:auto!important}.wrm-testata .wrm-menu{order:9}}'
    # pulsante della testata più compatto (12 x 20)
    '.wrm-testata .wrm-btn-t .elementor-button,.wrm-testata .wrm-btn-t a{padding:12px 20px!important}'
    f'.wrm-testata .wrm-tel a{{color:{INK};text-decoration:none!important}}'
    f'.wrm-testata .wrm-tel a:hover,.wrm-testata .wrm-tel a:focus-visible{{color:{ROSSO_SCURO};text-decoration:underline!important;'
    'text-underline-offset:4px}'
    # fallback HTML: voce attiva e hover come in Ultimate Addons, pulsante del menu quadrato
    f'.wrm-testata .wrm-nav-l a:hover,.wrm-testata .wrm-nav-l a:focus-visible{{color:{ROSSO_SCURO};border-bottom-color:transparent}}'
    f'.wrm-testata .wrm-nav-l a[aria-current=page]{{border-bottom-color:{ROSSO}}}'
    f'.wrm-testata summary{{width:48px;height:48px;min-width:48px!important;min-height:48px!important;box-sizing:border-box;'
    f'border:2px solid {INK};justify-content:center!important}}'
    f'.wrm-testata summary .wrm-ico{{width:20px!important;height:14px!important;border:0!important;background:{ICONA_MENU}}}'
    '.wrm-testata summary .wrm-ico::after{display:none}'
    f'.wrm-testata details[open] summary .wrm-ico{{width:18px!important;height:18px!important;background:{ICONA_X}}}'
    # la tendina del fallback si apre a tutta larghezza sotto la testata (come Ultimate Addons), non sotto il pulsante
    '@media (max-width:1024px){.wrm-testata .wrm-menu{position:static!important}}'
    f'.wrm-testata details ul{{margin-top:0!important}}'
    '@media (hover:hover){'
    f'.wrm-testata summary:hover{{background:{INK}}}.wrm-testata summary:hover .wrm-ico{{background:{ICONA_MENU.replace(INK, BIANCO)}}}'
    f'.wrm-testata details[open] summary:hover .wrm-ico{{background:{ICONA_X.replace(INK, BIANCO)}}}}}'
    f".wrm-testata .wrm-menu details li a{{padding:12px 32px!important;border-bottom:1px solid {FILETTO}!important;"
    f"font:600 26px/1.25 {F_COND}}}"
    f'.wrm-testata .wrm-menu details li a[aria-current=page]{{color:{ROSSO_SCURO};text-decoration:underline;'
    'text-decoration-thickness:2px;text-underline-offset:6px}'
    "@media (max-width:767px){.wrm-testata .wrm-menu details li a{padding:12px 20px!important;font-size:24px}"
    '.wrm-testata summary{width:44px;height:44px;min-width:44px!important;min-height:44px!important}}'
)


# menu a scomparsa: Esc lo chiude e riporta il fuoco sul pulsante; si chiude anche toccando una voce
# (Ultimate Addons in Elementor, <details> nel fallback HTML)
JS_TESTATA = (
    "(function(){function go(){"
    "document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;"
    "var t=document.querySelector('.wrm-testata .hfe-nav-menu__toggle.hfe-active-menu');if(t){t.click();t.focus();return}"
    "var d=document.querySelector('.wrm-testata details[open]');if(d){d.open=false;d.querySelector('summary').focus()}});"
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.wrm-testata .hfe-dropdown a,.wrm-testata details a');"
    "if(!a)return;var t=document.querySelector('.wrm-testata .hfe-nav-menu__toggle.hfe-active-menu');if(t)t.click();"
    "var d=document.querySelector('.wrm-testata details[open]');if(d)d.open=false})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();"
)


def header():
    logo = I(img('logo.png'), 'Wirmec', link='/', w_img=(156, 140, 124), fisso=True, link_label='Wirmec, home',
             css='wrm-logo')
    menu = MENU(VOCI_MENU, colore=INK, colore_hover=ROSSO_SCURO, accento=ROSSO, fondo_menu=BIANCO, linea=FILETTO,
                stile='nav', stile_mobile='nav_m', spazio=28, pad_v=30, distanza=11, align_menu='left', fisso=True,
                larg=(None, 48, 44),
                css='wrm-menu')
    tel = T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='tel_s', color=INK, link_color=INK, link_hover=ROSSO_SCURO,
            hide=['tablet', 'mobile'], fisso=True, sottolinea=False, css='wrm-tel')
    chiama = T(f'<p><a href="{TEL_LINK}">Chiama</a></p>', style='link', color=INK, link_color=INK, link_hover=ROSSO_SCURO,
               hide=['desktop'], fisso=True, css='wrm-link wrm-chiama')
    pulsante = B('Richiedi offerta', '/contatti/#richiesta', variant='primario', hide=['tablet', 'mobile'], fisso=True,
                 css='wrm-btn-t')
    riga = C(logo, menu, tel, chiama, pulsante, dir='row', align='center', gap=(24, 20, 16), min_h=(84, 72, 64),
             pad=(0, 'lato'), bg=BIANCO, border_bottom=1, border_color=FILETTO, boxed=True)
    # i due fogli di stile stanno fuori dalla riga: dentro occuperebbero due spazi in fondo alla fila
    return C(riga, RAW('', css=CSS_BASE, solo_elementor=True), RAW(f'<script>{JS_TESTATA}</script>', css=CSS_TESTATA), pad='0', gap='0',
             boxed=False,
             tag='header', bg=BIANCO, css='wrm-testata')


CSS_PIEDE = (
    f'.wrm-piede .wrm-pl a{{color:{PIEDE2};text-decoration:none!important}}'
    f'.wrm-piede .wrm-pl a:hover,.wrm-piede .wrm-pl a:focus-visible{{color:{BIANCO};text-decoration:underline!important;'
    'text-underline-offset:4px}'
    f'.wrm-piede a:focus-visible{{outline-color:{BIANCO}!important}}'
    # aree di tocco: sul telefono le voci stanno su righe da 40 px
    '@media (max-width:767px){.wrm-piede .wrm-pl-lista p{line-height:36px}}'
)


def footer():
    def colonna(titolo, html, w):
        return C(T(f'<p>{titolo}</p>', style='label', color=BIANCO),
                 T(html, style='piede', color=PIEDE2, link_color=PIEDE2, link_hover=BIANCO, sottolinea=False,
                   css='wrm-pl wrm-pl-lista', mt='xs'),
                 w=w, gap='0')
    prodotti = ''.join(f'<a href="{u}">{t}</a><br>' for t, u in (
        ('Automatiche WirAM', '/automatiche/'), ('Accessori macchina', '/automatiche/#accessori'),
        ('Presse e spela aggraffa', '/da-banco/#wirpress'), ('WirStrip', '/da-banco/#wirstrip'),
        ('Applicatori WirTool', '/applicatori/'), ('Controllo qualità WirTest', '/controllo-qualita/')))[:-4]
    wirmec = (f'<a href="/azienda/">Azienda</a><br><a href="/contatti/">Contatti</a><br>'
              f'<a href="/contatti/#richiesta">Richiedi offerta</a><br><a href="{LINKEDIN}">LinkedIn</a>')
    sede = (f'Wirmec S.r.l.<br>{INDIRIZZO}<br>{CITTA}<br>Tel. <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br>'
            f'<a href="mailto:{EMAIL}">{EMAIL}</a><br>PEC {PEC}')
    righe = C(
        C(I(img('logo-neg.png'), 'Wirmec', link='/', w_img=(156, 156, 140), link_label='Wirmec, home'),
          T('<p>Macchine e applicatori per tagliare, spelare e aggraffare il cavo.</p>', style='small', color=PIEDE2,
            max_w=(320, 560, 350), mt='m'),
          T(f'<p>{PAYOFF}</p>', style='meta', color=PIEDE2, mt='xs'),
          w=(29.5, 100, 100), gap='0'),
        colonna('Prodotti', f'<p>{prodotti}</p>', (18.4, 31, 47)),
        colonna('Wirmec', f'<p>{wirmec}</p>', (18.4, 31, 47)),
        colonna('Sede', f'<p>{sede}</p>', (22.1, 31, 100)),
        dir='row', wrap=True, justify='between', gap='col', gap_r='l')
    legale = C(
        T(f'<p>© 2026 Wirmec S.r.l. · {INDIRIZZO}, {CITTA} · P.IVA e C.F. {PIVA} · REA {REA} · '
          f'Capitale sociale {CAPITALE}</p>', style='meta', color=PIEDE2, grow=True),
        T('<p><a href="/privacy/">Privacy</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cookie/">Cookie</a></p>', style='meta',
          color=PIEDE2, link_color=PIEDE2, link_hover=BIANCO, sottolinea=False, align=('right', 'left', 'left'), fisso=True,
          css='wrm-pl'),
        dir='row', dir_t='column', justify='between', gap=('m', 's', 's'), pad=('m', 0, 0, 0), border_top=1,
        border_color=FILETTO_S, mt='l')
    return C(righe, legale, RAW('', css=CSS_PIEDE), gap='0', pad=('xl', 'lato', 'l', 'lato'), bg=NOTTE, tag='footer',
             css='wrm-piede wrm-scuro')


# ---------------------------------------------------------------------------------------------
# HOME (specifica, paragrafo 6)
# ---------------------------------------------------------------------------------------------
# le sei linee come prima navigazione: (nome, descrizione, conteggio, link)  [conteggi DA CONFERMARE, 17.7]
LINEE = [
    ('WirTool', 'Applicatori side feed ed end feed', '10 modelli', '/applicatori/'),
    ('WirPress', 'Presse e spela aggraffa da banco', '9 modelli', '/da-banco/#wirpress'),
    ('WirStrip', 'Troncatrice e sguainatrici da banco', '3 modelli', '/da-banco/#wirstrip'),
    ('WirAM', 'Taglia spela aggraffa automatiche', '7 modelli', '/automatiche/'),
    ('Accessori', 'Unità da montare sulle automatiche', '10 unità', '/automatiche/#accessori'),
    ('WirTest', "Controllo dell’aggraffatura", '3 strumenti', '/controllo-qualita/'),
]

CSS_APRE = (
    # fila delle sei linee: filetto sinistro tra le celle, la prima di ogni riga senza filetto e senza rientro
    f'.wrm-linee>.wrm-linea{{border-left:1px solid {FILETTO_G}}}'
    '.wrm-linea .wrm-desc p{min-height:3.1em}'
    '@media (min-width:1025px) and (max-width:1199px){.wrm-linee>.wrm-linea{padding-left:16px!important;padding-right:16px!important}}'
    '@media (min-width:1025px){.wrm-linee>.wrm-linea:first-child{border-left:0;padding-left:0!important}}'
    '@media (min-width:768px) and (max-width:1024px){.wrm-linee>.wrm-linea:nth-child(3n+1){border-left:0;padding-left:0!important}'
    f'.wrm-linee>.wrm-linea:nth-child(n+4){{border-top:1px solid {FILETTO_G}}}}}'
    '@media (max-width:767px){.wrm-linee>.wrm-linea:nth-child(2n+1){border-left:0;padding-left:0!important}'
    f'.wrm-linee>.wrm-linea:nth-child(n+3){{border-top:1px solid {FILETTO_G}}}}}'
)


def apertura():
    """H1: la AM460 Sintesi scontornata sul grigio, codice e quattro valori sotto, le sei linee in fondo alla fascia."""
    testo = C(
        T('<p>Dal 2010 a Ponte San Nicolò, Padova</p>', style='kicker', color=TESTO2),
        H('Macchine per tagliare, spelare e aggraffare il cavo', 'h1', mt='s'),
        T("<p>Applicatori, presse da banco, spela aggraffa e taglia spela aggraffa automatiche fino a 6 stazioni, con gli "
          "strumenti per controllare l’aggraffatura. Le progettiamo e le costruiamo per chi produce cablaggi, in Italia e "
          "all’estero con 9 distributori.</p>", style='lead', color=INK, max_w=(470, 470, 560), mt='m'),
        C(B("Richiedi un’offerta", '/contatti/#richiesta', variant='primario', full_m=True),
          B('Le automatiche WirAM', '/automatiche/', variant='contorno', full_m=True),
          dir='row', dir_m='column', wrap=(True, True, False), gap=(16, 16, 12), mt='l'),
        w=(37.9, 44.3, 100), gap='0')
    valori = [('Stazioni', 'fino a 5'), ('Sezione cavo', f'0,13–6{NB}mm²'), ('Alimentazione cavo', f'8,5{NB}m/s'),
              ('Unità aggraffatrici', 'fino a 3')]
    macchina = C(
        I(img('am460-sintesi.webp'), 'AM460 Sintesi, taglia spela aggraffa automatica Wirmec'),
        C(C(H('AM460 Sintesi', 'p', style='h3'),
            T('<p>Taglia spela aggraffa automatica</p>', style='small', color=TESTO2, mt='xxs'), gap='0'),
          link_freccia('Scheda AM460', '/automatiche/#am460-sintesi', fisso=True, mt=(0, 0, 'xs')),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s', mt=24),
        C(*[C(T(f'<p>{k}</p>', style='label', color=TESTO2), T(f'<p>{v}</p>', style='dato_l', color=INK, mt='xs'),
              w=(25, 50, 50), gap='0') for k, v in valori],
          dir='row', wrap=True, gap='0', gap_r='s', border_top=1, border_color=FILETTO_G, pad=('s', 0, 0, 0), mt='s'),
        w=(58.2, 52.2, 100), gap='0', mt=(0, 0, 'l'))
    riga = C(testo, macchina, dir='row', dir_m='column', align=('center', 'center', 'stretch'), gap='col')
    celle = []
    for n, (nm, desc, conta, url) in enumerate(LINEE):
        celle.append(C(
            nome(nm),
            T(f'<p>{desc}</p>', style='small', color=TESTO2, mt='xxs', css='wrm-desc'),
            T(f'<p>{freccia(conta)}</p>', style='dato_s', color=INK, mt='s'),
            w=(16.66, 33.33, 50), pad=((24, 24, 20), (24, 24, 16), (32, 32, 24), (24, 24, 16)), gap='0', link=url,
            css='wrm-cl wrm-linea'))
    linee = C(*celle, dir='row', wrap=True, gap='0', border_top=1, border_color=FILETTO_G, mt='xl', css='wrm-linee')
    return sezione(riga, linee, bg=GRIGIO, pad=((72, 56, 40), 'lato', 0, 'lato'), css='wrm-apre', anchor='content',
                   stile_extra=CSS_APRE)


# le dodici lavorazioni delle brochure AM400, AM500, AM600: (file, nome, nota, larghezza nativa dei disegni)
LAVORAZIONI = [
    ('taglio', 'Taglio', '', 1533), ('spelatura', 'Spelatura', f'0,1–15{NB}mm per lato', 1959),
    ('spelatura-parziale', 'Spelatura parziale', '', 2386), ('spelatura-intermedia', 'Spelatura intermedia', '', 2386),
    ('aggraffatura', 'Aggraffatura', '', 2467), ('terminale-chiuso', 'Terminale chiuso, split cycle', '', 2369),
    ('inserimento-gommino', 'Inserimento gommino', '', 2437), ('inserimento-guaina', 'Inserimento guaina', '', 2446),
    ('doppiatore-cavo', 'Doppiatore cavo', '', 2433),
    ('attorcigliatura-e-stagnatura', 'Attorcigliatura e stagnatura', '', 1998),
    ('stampa-inkjet', 'Stampa inkjet', '', 1959), ('stampa-a-caldo', 'Stampa a caldo', '', 1959),
]


def disegno_lavorazione(chiave, testo, nativa):
    """Disegno Wirmec di una lavorazione, largo in proporzione alla sua misura nativa (stessa scala per tutti)."""
    pct = round(nativa / 2467 * 100, 1)
    return C(I(img(f'lav-{chiave}.png'), f'Disegno della lavorazione: {testo.lower()}'), w=(pct, pct, pct), gap='0')


def lavorazioni():
    """H2: "Una stazione, una lavorazione sul cavo", dodici voci numerate in due colonne."""
    voci = []
    for i, (chiave, testo, nota, nativa) in enumerate(LAVORAZIONI, 1):
        etichetta = C(
            C(T(f'<p>{i:02d}</p>', style='dato_s', color=TESTO2, w_px=(None, None, 28), fisso=True),
              nome(testo, livello='h3', mt=('xxs', 'xxs', 0)),
              dir='column', dir_m='row', align=('start', 'start', 'baseline'), gap=(0, 0, 0)),
            *([T(f'<p>{nota}</p>', style='dato_s', color=TESTO2, mt='xxs', css='wrm-nota')] if nota else []),
            w=(37, 100, 100), gap='0', pad=(0, (16, 0, 0), 0, 0))
        voci.append(C(etichetta, C(disegno_lavorazione(chiave, testo, nativa), w=(63, 100, 100), gap='0'),
                      dir='row', dir_t='column', align=('center', 'start', 'start'), gap=(0, 16, 12),
                      w=(47.5, 47.5, 100), pad=((24, 24, 16), 0, (28, 28, 20), 0), border_top=1, border_color=FILETTO))
    griglia = C(*voci, dir='row', wrap=True, justify='between', gap='0', mt='xl')
    return sezione(
        testa('Una stazione, una lavorazione sul cavo',
              'Sulle taglia spela aggraffa WirAM ogni stazione montata aggiunge una lavorazione: fino a 5 sulla AM400 '
              'quattro e sulla AM460 Sintesi, fino a 6 sulle AM500 e AM600 Vantage. Qui le dodici lavorazioni delle loro '
              'brochure, nei disegni Wirmec alla stessa scala.'),
        griglia,
        link_freccia('Le stazioni sono unità Accessori: vedi quale fa cosa', '/automatiche/#accessori', mt='l'),
        css='wrm-lav', anchor='lavorazioni',
        stile_extra='@media (max-width:767px){.wrm-lav .wrm-nota p{padding-left:28px}}')


WIRAM = [
    ('AM210 futura', 'cavi da 16 a 34 AWG', 'am210-futura'),
    ('AM310 quattro', f'fino a 5 stazioni, 0,13–2,5{NB}mm²', 'am310-quattro'),
    ('AM350 quattro', 'per cavo flat e Nily', 'am350-quattro'),
    ('AM400 quattro', f'fino a 5 stazioni, 0,13–4{NB}mm²', 'am400-quattro'),
    ('AM460 Sintesi', f'fino a 5 stazioni, 0,13–6{NB}mm²', 'am460-sintesi'),
    ('AM500 Vantage', f'fino a 6 stazioni, 12{NB}m/s', 'am500-vantage'),
    ('AM600 Vantage', '6 stazioni, doppio cavo', 'am600-vantage'),
]

CSS_RIGHE_SCURE = (
    f'.wrm-riga-s .wrm-dato p{{transition:color .15s}}'
    f'.wrm-riga-s:hover .wrm-dato p,.wrm-riga-s:focus-visible .wrm-dato p{{color:{BIANCO}!important}}'
    f'.wrm-riga-s:hover .wrm-nome .elementor-heading-title,.wrm-riga-s:hover .wrm-nome{{color:{BIANCO}!important}}'
    f'.wrm-riga-s:focus-visible{{outline:2px solid {BIANCO}!important;outline-offset:-2px}}'
    '.wrm-riga-s .wrm-fr{font-size:17px}'
)


def riga_scura(testo, dato, url):
    """Riga-link su ardesia: nome a sinistra, dato a destra, freccia (sul telefono il dato va sotto il nome)."""
    return C(
        C(nome(testo, colore=BIANCO),
          T(f'<p>{dato}</p>', style='dato_s', color=SU_SCURO2, css='wrm-dato', align=('right', 'right', 'left')),
          dir='row', dir_m='column', justify='between', align=('center', 'center', 'start'), gap=(16, 16, 2), grow=True),
        T('<p><span class="wrm-fr" aria-hidden="true">→</span></p>', style='body', color=BIANCO, fisso=True),
        dir='row', align='center', gap=16, min_h=(52, 52, 0), pad=((0, 0, 12), 0, (0, 0, 12), 0), border_bottom=1,
        border_color=FILETTO_S, link=url, css='wrm-cl wrm-riga-s')


def wiram():
    """H3: la fascia ardesia con la AM310 quattro e i sette modelli, un dato ciascuno."""
    foto = C(
        I(img('am310-quattro.webp'), 'AM310 quattro, taglia spela aggraffa automatica'),
        C(nome('AM310 quattro', colore=BIANCO),
          T(f'<p>fino a 5 stazioni, 0,13–2,5{NB}mm²</p>', style='meta', color=SU_SCURO2),
          dir='row', wrap=True, justify='between', align='baseline', gap=(16, 16, 4), border_top=1, border_color=FILETTO_S,
          pad=('xs', 0, 0, 0), mt='s'),
        w=(46, 66.7, 100), gap='0')
    testo = C(
        *titolo_h2('WirAM, taglia spela aggraffa automatiche', colore=BIANCO),
        T('<p>Dalla AM210 futura, per cavi sottili fino a 34 AWG, alla AM600 Vantage, che lavora due cavi diversi con il '
          f'sistema a doppio cavo brevettato. Sulle Vantage il cavo avanza fino a 12{NB}m/s.</p>', style='body',
          color=SU_SCURO2, mt='m'),
        C(*[riga_scura(n, d, f'/automatiche/#{a}') for n, d, a in WIRAM], gap='0', border_top=2, border_color=BIANCO,
          mt='l'),
        C(link_freccia('Tutte le WirAM e gli accessori', '/automatiche/', scuro=True, fisso=True),
          link_freccia('Brochure in PDF', '/automatiche/#brochure', scuro=True, fisso=True),
          dir='row', dir_m='column', wrap=True, gap=(32, 32, 12), mt='m'),
        w=(50.2, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(foto, testo, dir='row', dir_t='column', align=('center', 'center', 'stretch'), gap=(48, 0, 0)),
                   bg=ARDESIA, css='wrm-wiram wrm-scuro', anchor='wiram', stile_extra=CSS_RIGHE_SCURE)


FAMIGLIA_BANCO = (
    'Nella stessa famiglia: <a href="/da-banco/#w15">W15</a> e <a href="/da-banco/#w15-sc">W15 SC</a> 20&nbsp;kN, '
    '<a href="/da-banco/#w-2000">W&nbsp;2000</a> 25&nbsp;kN, <a href="/da-banco/#w-3000">W&nbsp;3000</a> 30&nbsp;kN; '
    'spela aggraffa <a href="/da-banco/#wsc-15">WSC&nbsp;15</a>, <a href="/da-banco/#wsc-21">WSC&nbsp;21</a>, '
    '<a href="/da-banco/#wsc-25">WSC&nbsp;25</a> e <a href="/da-banco/#wsc-31">WSC&nbsp;31</a>.'
)

CSS_W1500 = (
    '.wrm-w1500 .wrm-dl dl>div{min-height:48px;box-sizing:border-box}'
    '.wrm-foto-c.elementor-widget-image{text-align:center!important}'
    '.wrm-foto-c img{margin-left:auto;margin-right:auto}'
)


def w1500():
    """H4: una sola pressa, il codice scritto a 176 px, il filetto rosso corto, i dati in righe (dalla direzione "misura")."""
    alt = 'W 1500, aggraffatrice da banco 20 kN'
    dati = [('Forza di aggraffatura', f'20{NB}kN'), ('Corsa', f'40{NB}mm'), ('Sezione di aggraffatura max', f'6{NB}mm²'),
            ('Spessore terminale max', f'0,6{NB}mm'), ('Alimentazione', f'230{NB}V monofase, 0,75{NB}kW'),
            ('Peso', f'45{NB}kg')]
    # prima riga: la foto in basso a sinistra, appoggiata sull'ultima riga dei dati; a destra codice, testo e dati
    foto = C(I(img('w1500.jpg'), alt, w_img=(600, 440, 300)), w=(50, 48, 100), gap='0', hide=['mobile'])
    scheda = C(
        T('<p>WirPress, aggraffatrice da banco</p>', style='kicker', color=TESTO2),
        H(f'W{NB}1500', 'h2', style='codice', mt='s', css='wrm-codice'),
        filetto_rosso(72, mt='m'),
        H('Aggraffatrice da banco 20 kN', 'h3', mt='m'),
        I(img('w1500.jpg'), alt, w_img=(300, 300, 300), hide=['desktop', 'tablet'], css='wrm-foto-c', mt='l'),
        T('<p>Unità aggraffatrice da banco semplice e compatta per aggraffare in piena sicurezza: punto morto inferiore '
          f'regolabile, standard 135,78{NB}mm; selettore jog per la corsa lenta; controllo della forza di aggraffatura (CFM) '
          'a richiesta.</p>', style='body', color=INK, mt=('s', 's', 'l')),
        dati_dl(dati, 'wrm-dl-forte', mt='l'),
        w=(50, 52, 100), gap='0', pad=(0, 0, 0, (48, 32, 0)))
    # seconda riga: a sinistra la didascalia sotto la foto, a destra frase, pulsanti, brochure e famiglia
    nota = C(C(didascalia(f'W{NB}1500, foto della brochure Wirmec.'), border_top=1, border_color=FILETTO,
               pad=('xs', 0, 0, 0)), w=(50, 48, 100), gap='0', hide=['mobile'])
    azioni = C(
        T('<p>Le nostre presse si usano anche con gli applicatori di altri costruttori.</p>', style='body', color=INK),
        C(B(f"Richiedi un’offerta per la W{NB}1500", richiesta('wirpress', 'W 1500'), variant='primario', full_m=True),
          B('Tutte le macchine da banco', '/da-banco/', variant='contorno', full_m=True),
          dir='row', dir_m='column', wrap=(True, True, False), gap=(16, 16, 12), mt='l'),
        T(f'<p><a href="{pdf("wirmec_w1500.pdf")}">Brochure W{NB}1500 (PDF, inglese, 0,3{NB}MB)</a></p>', style='link',
          color=ROSSO_SCURO, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link', mt='s'),
        T(f'<p>{FAMIGLIA_BANCO}</p>', style='small', color=TESTO2, link_color=ROSSO_SCURO, link_hover=INK,
          css='wrm-link', mt='m'),
        w=(50, 52, 100), gap='0', pad=(0, 0, 0, (48, 32, 0)))
    return sezione(C(foto, scheda, dir='row', dir_m='column', align='end', gap='0'),
                   C(nota, azioni, dir='row', dir_m='column', gap='0', mt='m'),
                   css='wrm-w1500', anchor='w-1500', stile_extra=CSS_W1500)


def wirtool():
    """H5: WB 10 e WPB 10 sul grigio uguale al fondo delle loro foto, accanto i dati comuni della famiglia."""
    dati = [('Corsa', f'40{NB}mm'), ('Corsa di alimentazione', f'30{NB}mm'), ('Ghiera di registro', '4 posizioni'),
            ('Ghiera micrometrica, a richiesta', f'passo 0,02{NB}o{NB}0,01{NB}mm, corsa{NB}3{NB}mm'), ('Peso', f'&lt;{NB}4{NB}kg')]
    sinistra = C(
        *titolo_h2('WirTool, applicatori'),
        T("<p>Applicatori per l’aggraffatura side feed ed end feed, con movimentazione meccanica e pneumatica, e sistemi "
          'per il cablaggio semiautomatico di connettori IDC progettati sulla specifica del costruttore del connettore.</p>',
          style='body', color=INK, mt='m'),
        dati_dl(dati, 'wrm-dl-grigio', mt='l'),
        link_freccia('I dieci applicatori WirTool', '/applicatori/', mt='l'),
        w=(40, 100, 100), gap='0')

    def applicatore(file, codice, alt, testo):
        return C(C(I(img(file), alt, w_img=(336, 336, 165), css='wrm-foto-c'), min_h=(364, 364, 179), justify='end',
                   gap='0'),
                 C(nome(codice), T(f'<p>{testo}</p>', style='small', color=TESTO2, mt='xxs'), gap='0',
                   border_top=1, border_color=FILETTO_G, pad=('s', 0, 0, 0), mt='s'),
                 w=(46.6, 48.3, 47.1), gap='0')
    destra = C(
        applicatore('wb10.jpg', 'WB 10', 'WB 10, applicatore side feed',
                    "Side feed, con alimentazione a rapporti di leva e ampia visibilità sul punto di aggraffatura."),
        applicatore('wpb10.jpg', 'WPB 10', 'WPB 10, applicatore side feed pneumatico',
                    'Side feed ad alimentazione pneumatica, per terminali a passo lungo.'),
        dir='row', justify='between', align='start', gap='col', w=(60, 100, 100), pad=(0, 0, 0, (48, 0, 0)),
        mt=(0, 'xl', 'l'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align=('center', 'stretch', 'stretch'), gap='0'),
                   bg=GRIGIO, css='wrm-wirtool', anchor='wirtool', stile_extra=CSS_W1500)


def strumento(file, alt, codice, sotto, testo, valori=''):
    """Riga di uno strumento WirTest: foto piccola a sinistra, nome, sottotitolo, testo, valori."""
    corpo = [nome(codice), T(f'<p>{sotto}</p>', style='small', color=TESTO2, mt='xxs'),
             T(f'<p>{testo}</p>', style='small', color=INK, mt='xs')]
    if valori:
        corpo.append(T(f'<p>{valori}</p>', style='dato_s', color=INK, mt='xs'))
    return C(I(img(file), alt, w_img=(132, 132, 112), fisso=True), C(*corpo, gap='0', grow=True),
             dir='row', align='start', gap='s', pad=('m', 0, 'm', 0), border_top=1, border_color=FILETTO,
             w=(100, 48.3, 100))


def wirtest():
    """H6: il risultato in primo piano: terminale sul righello, sezione al micrografo, gli strumenti W200 e W100."""
    foto1 = C(I(img('righello.jpg'), 'Terminale aggraffato su cavo sottile accanto a un righello'),
              didascalia('<strong>Terminale aggraffato su cavo sottile</strong>, accanto alle tacche di un righello. Foto '
                         'della scheda AM210 futura, per cavi fino a 34 AWG.', mt='s'),
              w=(31.6, 48.3, 100), gap='0')
    foto2 = C(I(img('sezione-10awg.jpg'), "Sezione al micrografo di un’aggraffatura su cavo 10 AWG"),
              didascalia("<strong>Sezione di un’aggraffatura su cavo 10 AWG</strong>, misurata sulla foto: altezza 2,57, "
                         'larghezza 3,83. Foto della scheda W200.', mt='s'),
              w=(31.6, 48.3, 100), gap='0')
    strumenti = C(
        strumento('w200.jpg', 'W200, laboratorio di micrografia', 'W200', 'Laboratorio di micrografia',
                  'Taglio, lucidatura e fotografia della sezione sulla stessa apparecchiatura. Al PC la sezione si '
                  'ingrandisce fino a 200 volte e si misura sulla foto; con il software opzionale le quote diventano un '
                  'report.'),
        strumento('w100.jpg', 'W100, dinamometro', 'W100', 'Dinamometro motorizzato',
                  f'Forza di tenuta fino a 1000{NB}N con test non distruttivo, valore di picco, stampante e certificato di '
                  f'calibrazione. Fino a 2500{NB}N c’è il W125.', f'0–1000{NB}N · 50{NB}mm/min'),
        dir='column', dir_t='row', dir_m='column', justify='between', gap='0', w=(31.7, 100, 100), mt=(0, 'l', 0),
        css='wrm-strumenti')
    return sezione(
        testa("WirTest, il controllo dell’aggraffatura",
              "Attrezzature per il controllo qualità dell’aggraffatura: la forza di tenuta con i dinamometri, la sezione "
              'del terminale con il laboratorio di micrografia.'),
        C(foto1, foto2, strumenti, dir='row', dir_m='column', wrap=(False, True, False), justify='between',
          gap=(32, 32, 0), gap_r=(0, 0, 'l'), mt='xl'),
        link_freccia('Controllo qualità: W200, W100 e W125', '/controllo-qualita/', mt='l'),
        css='wrm-wirtest', anchor='wirtest',
        stile_extra='@media (min-width:1025px){.wrm-strumenti>.e-con:first-child,.wrm-strumenti>.wrm-con:first-child'
                    '{padding-top:0!important;border-top:0!important}}')


REFERENTI = [
    ('Gianluca Corio', 'Lombardia, Piemonte, Liguria', f'+39{NB}347{NB}980{NB}0747', 'tel:+393479800747'),
    ('Gianluca Trivellato', 'Triveneto, Emilia-Romagna', f'+39{NB}347{NB}798{NB}6503', 'tel:+393477986503'),
    ('Marco Di Martino', "Resto d’Italia", f'+39{NB}347{NB}433{NB}1068', 'tel:+393474331068'),
]


def contatti_home():
    """H7: il numero della sede per intero e grande, accanto chi segue la tua zona (TRUMPF)."""
    sinistra = C(
        *titolo_h2("Richiedi un’offerta"),
        H(TEL, 'p', style='tel', color=INK, link=TEL_LINK, mt='m', css='wrm-tel-g'),
        T(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a><br>Fax {FAX}<br>{INDIRIZZO}, {CITTA}</p>', style='body', color=INK,
          link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link', mt='m'),
        B('Scrivi a Wirmec', '/contatti/#richiesta', variant='primario', full_m=True, mt='l'),
        w=(41.67, 45, 100), gap='0')
    righe = [C(C(nome(n), T(f'<p>{z}</p>', style='small', color=TESTO2, mt='xxs'), gap='0', grow=True),
               T(f'<p><a href="{tl}">{t}</a></p>', style='dato_s', color=INK, link_color=INK, link_hover=ROSSO_SCURO,
                 sottolinea=False, fisso=True, css='wrm-tel-r'),
               dir='row', dir_m='column', justify='between', align=('center', 'center', 'start'), gap=('s', 's', 'xs'),
               pad=('s', 0, 's', 0), border_bottom=1, border_color=FILETTO_G)
             for n, z, t, tl in REFERENTI]
    destra = C(
        H('In Italia, per zona', 'h3'),
        C(*righe, gap='0', border_top=2, border_color=INK, mt='s'),
        H("All’estero", 'h3', mt='l'),
        T('<p>Vendiamo con nove distributori: Germania, Repubblica Ceca, Svezia e paesi nordici, Regno Unito, Spagna, '
          f'Francia, Ungheria, Polonia e Turchia. <a href="/contatti/#estero"><strong>{freccia("Trova il distributore del tuo paese")}'
          '</strong></a></p>', style='body', color=INK, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link', mt='s'),
        w=(58.33, 55, 100), gap='0', pad=(0, 0, 0, (48, 32, 0)), mt=(0, 0, 'xl'))
    return sezione(C(sinistra, destra, dir='row', dir_m='column', gap='0'), bg=GRIGIO, css='wrm-contatti',
                   anchor='contatti',
                   stile_extra=(f'.wrm-tel-r a:hover,.wrm-tel-r a:focus-visible{{text-decoration:underline!important;'
                                'text-underline-offset:4px}'))


def home():
    return [('apertura', apertura()), ('lavorazioni', lavorazioni()), ('wiram', wiram()), ('w1500', w1500()),
            ('wirtool', wirtool()), ('wirtest', wirtest()), ('contatti', contatti_home())]


# ---------------------------------------------------------------------------------------------
# Componenti delle pagine 02-07 (specifica, paragrafo 5)
# ---------------------------------------------------------------------------------------------
def ancora(codice):
    """Ancora di un codice: minuscolo, spazi in trattino ("AM 0010" -> "am-0010", "W 1500" -> "w-1500")."""
    return codice.lower().replace(' ', '-')


def unito(testo):
    """Codici e misure che non vanno a capo: "W 1500", "AM 0010"."""
    return testo.replace(' ', NB)


CODICI = {
    'wiram': ['AM210 futura', 'AM310 quattro', 'AM350 quattro', 'AM400 quattro', 'AM460 Sintesi', 'AM500 Vantage',
              'AM600 Vantage'],
    'accessori': ['AM 0010', 'AM 0011', 'AM 0012', 'AM 0038', 'AM 0040', 'AM 0061', 'AM 0063', 'AM 0064', 'AM 0083',
                  'AM 0090'],
    'presse': ['W15', 'W15 SC', 'W 1500', 'W 2000', 'W 3000'],
    'spela': ['WSC 15', 'WSC 21', 'WSC 25', 'WSC 31'],
    'wirstrip': ['WSG 100', 'WSG 200', 'WSG 300'],
    'wirtool': ['WB 10', 'WB 13', 'WB 14', 'WB 23', 'WB 27', 'WL 10', 'WL 11', 'WL 19', 'WPB 10', 'WPB 16'],
    'wirtest': ['W100', 'W125', 'W200'],
}
PAGINA_DI = {'wiram': '/automatiche/', 'accessori': '/automatiche/', 'presse': '/da-banco/', 'spela': '/da-banco/',
             'wirstrip': '/da-banco/', 'wirtool': '/applicatori/', 'wirtest': '/controllo-qualita/'}


def codici_link(gruppo, qui=False, codici=None):
    """[(codice, link)] di una linea; qui=True: ancore della stessa pagina."""
    base = '' if qui else PAGINA_DI[gruppo]
    return [(c, f'{base}#{ancora(c)}') for c in (codici or CODICI[gruppo])]


CSS_INDICE = (
    '.wrm-indice-c p{display:flex;flex-wrap:wrap;gap:6px 20px}'
    '.wrm-indice-c a{white-space:nowrap}'
    '.wrm-indice-c a:hover,.wrm-indice-c a:focus-visible{text-decoration:underline!important;text-decoration-thickness:1px!important;'
    'text-underline-offset:4px}'
    '@media (max-width:767px){.wrm-indice-c p{gap:6px 16px}}'
)


def indice(gruppi, scuro=False, **p):
    """Indice dei codici (5.3): filetto forte sopra, una riga per gruppo, i codici come link alle ancore."""
    col_et, col_cod, hover, fil, forte = ((SU_SCURO3, BIANCO, SU_SCURO2, FILETTO_S, BIANCO) if scuro else
                                          (TESTO2, INK, ROSSO_SCURO, FILETTO, INK))
    righe = []
    for et, codici in gruppi:
        links = ''.join(f'<a href="{u}">{unito(c)}</a>' for c, u in codici)
        righe.append(C(
            T(f'<p>{et}</p>', style='label', color=col_et, w_px=(132, 132, None), fisso=True),
            T(f'<p>{links}</p>', style='dato_s', color=col_cod, link_color=col_cod, link_hover=hover, sottolinea=False,
              css='wrm-indice-c', grow=True),
            dir='row', dir_m='column', align=('baseline', 'baseline', 'start'), gap=('s', 's', 'xs'), pad=(14, 0, 14, 0),
            border_bottom=1, border_color=fil))
    return C(*righe, gap='0', border_top=2, border_color=forte, css='wrm-indice', **p)


CSS_SCURO = '.wrm-scuro a:focus-visible,.wrm-scuro [tabindex]:focus-visible{outline-color:#FFFFFF!important}'
CSS_NOWRAP = '.wrm-nowrap a,.wrm-nowrap .elementor-button{white-space:nowrap}'


def blocco_richiesta(linea=''):
    """Blocco "Richiesta" (5.1): ardesia, titolo e frase a sinistra, due pulsanti a destra. Chiude le pagine prodotto."""
    sinistra = C(
        H("Richiedi un’offerta", 'h2', color=BIANCO),
        T('<p>Scrivi il modello che ti interessa, oppure il terminale e il cavo da lavorare. La richiesta non è '
          'impegnativa.</p>', style='lead', color=SU_SCURO2, max_w=(640, 700, 560), mt='s'),
        w=(58.33, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    destra = C(
        B("Richiedi un’offerta", richiesta(linea), variant='primario', full_m=True),
        B(f'Chiama {TEL}', TEL_LINK, variant='contorno-bianco', full_m=True, css='wrm-nowrap'),
        dir='row', dir_m='column', justify=('end', 'start', 'start'), wrap=(True, True, False), gap=(16, 16, 12),
        w=(41.67, 100, 100), mt=(0, 'm', 'm'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
                   bg=ARDESIA, pad=('xl', 'lato'), css='wrm-richiesta wrm-scuro', anchor='richiesta-offerta',
                   stile_extra=CSS_SCURO + CSS_NOWRAP)


def nd():
    return '<span class="wrm-nd">n.d.</span>'


def tabella(scope, titolo, testa_col, righe, bg=BIANCO, fil=FILETTO, prima=(220, 180, 130), min_col=132, scorre=True):
    """Tabella tecnica (5.2): <table> vera in un widget HTML, filetto forte sopra i nomi, prima colonna ferma quando
    scorre di lato (solo sotto i 768 px). testa_col: [(testo, id)]; righe: [(intestazione, id, [celle])],
    una cella può essere ('html', colspan). scope: classe della sezione (lo stile vale solo lì)."""
    def cella(c):
        if isinstance(c, tuple):
            return f'<td colspan="{c[1]}">{c[0]}</td>'
        return f'<td>{nd() if c == "n.d." else c}</td>'
    th = ''.join(f'<th scope="col"' + (f' id="{i}"' if i else '') + f'>{t}</th>' for t, i in testa_col)
    tr = ''.join(f'<tr><th scope="row"' + (f' id="{i}"' if i else '') + f'>{h}</th>{"".join(cella(c) for c in celle)}</tr>'
                 for h, i, celle in righe)
    html = ((f'<p class="wrm-tab-scorri">Scorri la tabella di lato <span aria-hidden="true">→</span></p>' if scorre else '')
            + f'<div class="wrm-tab" role="region" aria-label="Dati tecnici, {titolo}" tabindex="0"><table>'
            f'<caption>Dati tecnici, {titolo}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
    n = len(testa_col) - 1
    t = f'.{scope} .wrm-tab'
    css = (
        f'{t}{{overflow-x:auto;margin:0;-webkit-overflow-scrolling:touch}}'
        f'{t}:focus-visible{{outline:2px solid {ROSSO};outline-offset:3px}}'
        f'{t} table{{width:100%!important;border-collapse:separate!important;border-spacing:0;margin:0!important;border:0!important;'
        'font-size:inherit;font-variant-numeric:tabular-nums}}'
        f'{t} caption{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(1px,1px,1px,1px);white-space:nowrap}}'
        f'{t} th,{t} td{{padding:14px 16px!important;text-align:left;vertical-align:top!important;border:0!important;'
        f'border-bottom:1px solid {fil}!important;background:{bg}!important;line-height:1.3}}'
        f'{t} thead th{{border-top:2px solid {INK}!important;vertical-align:bottom!important;font:600 22px/1.2 {F_COND};color:{INK}}}'
        f'{t} thead th:first-child{{font:500 13px/1.3 {F_SANS};color:{TESTO2}}}'
        f'{t} tbody th{{font:500 13px/1.3 {F_SANS};color:{TESTO2};width:{prima[0]}px}}'
        f'{t} td{{font:500 17px/1.3 {F_MONO};color:{INK}}}'
        f'{t} td.wrm-tab-testo,{t} .wrm-tab-testo{{font:400 15px/1.45 {F_SANS};color:{INK}}}'
        f'{t} .wrm-tab-nome{{display:block;font:600 22px/1.2 {F_COND};color:{INK}}}'
        f'{t} .wrm-tab-sotto{{display:block;margin-top:4px;font:400 15px/1.4 {F_SANS};color:{TESTO2}}}'
        f'{t} td a{{font:600 15px/1.4 {F_SANS};color:{ROSSO_SCURO};text-decoration:underline;text-decoration-thickness:1px;'
        'text-underline-offset:4px}}'
        f'{t} td a:hover,{t} td a:focus-visible{{color:{INK};text-decoration-thickness:2px}}'
        f'{t} th:first-child{{position:sticky;left:0;z-index:1}}'
        f'@media (max-width:1024px){{{t} thead th{{font-size:21px}}{t} tbody th{{width:{prima[1]}px}}{t} .wrm-tab-nome{{font-size:21px}}}}'
        f'@media (max-width:767px){{{t} th,{t} td{{padding:12px!important}}{t} table{{min-width:{prima[2] + n * min_col}px}}'
        f'{t} tbody th,{t} thead th:first-child{{width:{prima[2]}px;min-width:{prima[2]}px;box-shadow:inset -1px 0 0 {fil}}}'
        f'{t} thead th{{font-size:20px}}{t} .wrm-tab-nome{{font-size:20px}}{t} td{{font-size:16px}}}}'
        f'.{scope} .wrm-tab-scorri{{display:none;margin:0 0 10px!important;font:400 13px/1.45 {F_SANS};color:{TESTO2}}}'
        f'@media (max-width:767px){{.{scope} .wrm-tab-scorri{{display:block}}}}'
    )
    return RAW(html, css=css)


CSS_AZIONI = (
    '.wrm-azioni p{display:flex;flex-wrap:wrap;gap:8px 24px}'
)

CSS_BROCHURE = (
    f'.wrm-cop img{{border:1px solid {FILETTO};box-sizing:border-box}}'
    '.wrm-scarica{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}'
    '.wrm-cl:hover .wrm-scarica,.wrm-cl:focus-visible .wrm-scarica{text-decoration-thickness:2px}'
    f'.wrm-cl:hover .wrm-scarica-t p,.wrm-cl:focus-visible .wrm-scarica-t p{{color:{INK}!important}}'
)


def scheda_brochure(titolo, file, lingua, mb, w):
    """Scheda download (Komax, TRUMPF): copertina, nome, lingua e peso, "Scarica". Tutta la scheda è il link al PDF."""
    return C(
        C(I(img(f'pdf-copertina-{file[:-4]}.jpg'), f'Copertina della brochure {titolo}', w_img=(160, 160, 150),
            css='wrm-cop'), min_h=(228, 228, 214), justify='end', gap='0'),
        nome(unito(titolo), mt='s'),
        T(f'<p>PDF, {lingua}, {mb}{NB}MB</p>', style='meta', color=TESTO2, mt='xxs'),
        T(f'<p><span class="wrm-scarica">{freccia("Scarica")}</span></p>', style='link', color=ROSSO_SCURO, mt='xs',
          css='wrm-scarica-t'),
        w=w, gap='0', link=pdf(file), css='wrm-cl wrm-broch')


def sezione_brochure(schede, nota, w, scope):
    return sezione(
        *titolo_h2('Brochure'),
        T(f'<p>{nota}</p>', style='small', color=TESTO2, mt='m'),
        C(*[scheda_brochure(*x, w=w) for x in schede], dir='row', wrap=True, gap=(20, 16, 16), gap_r=(40, 32, 28),
          mt='xl'),
        css=scope, anchor='brochure', stile_extra=CSS_BROCHURE)


CSS_DL2 = (
    # dati di un modello in due colonne (tre su tablet): etichetta sopra, valore in Plex Mono sotto
    f'.wrm-dl2 dl{{display:grid;grid-template-columns:1fr 1fr;column-gap:24px;margin:0;border-top:1px solid {FILETTO_G}}}'
    f'.wrm-dl2 dl>div{{padding:10px 0 12px;border-bottom:1px solid {FILETTO_G};margin:0}}'
    '.wrm-dl2 dt{margin:0;font-weight:500}'
    f'.wrm-dl2 dd{{margin:4px 0 0;font:500 17px/1.3 {F_MONO};color:{INK};text-wrap:balance}}'
    '@media (min-width:768px) and (max-width:1024px){.wrm-dl2 dl{grid-template-columns:1fr 1fr 1fr}}'
    '@media (max-width:767px){.wrm-dl2 dl{column-gap:16px}.wrm-dl2 dd{font-size:16px}}'
)


def dl2(coppie, **p):
    righe = ''.join(f'<div><dt>{k}</dt><dd>{nd() if v == "n.d." else v}</dd></div>' for k, v in coppie)
    return T(f'<dl>{righe}</dl>', style='label', color=TESTO2, css='wrm-dl2', **p)


def riga_numerata(n, html, colore=INK, **p):
    """Voce numerata: numero in Plex Mono a sinistra, testo a destra (passi, brevetti)."""
    return C(T(f'<p>{n:02d}</p>', style='dato_s', color=TESTO2, w_px=(40, 40, 32), fisso=True),
             T(f'<p>{html}</p>', style='body', color=colore, grow=True),
             dir='row', align='baseline', gap='0', **p)


# ---------------------------------------------------------------------------------------------
# 02 AUTOMATICHE: WirAM e Accessori macchina (specifica, paragrafo 7)
# ---------------------------------------------------------------------------------------------
def automatiche_apertura():
    """A1: la AM400 quattro intera su bianco, accanto titolo e pulsanti; sotto l'indice di tutti i codici."""
    testo = C(
        T('<p>WirAM e Accessori macchina</p>', style='kicker', color=TESTO2),
        H('Taglia spela aggraffa automatiche', 'h1', color=INK, mt='s'),
        T('<p>Sette modelli, dalla AM210 futura per cavi fino a 34 AWG alla AM600 Vantage, che lavora due cavi diversi. '
          'Si equipaggiano con fino a cinque o sei stazioni: le unità Accessori aggraffano, inseriscono gommini e '
          'coprifaston, attorcigliano e stagnano.</p>', style='lead', color=INK, max_w=(500, 640, 560), mt='m'),
        C(B("Richiedi un’offerta", richiesta('wiram'), variant='primario', full_m=True),
          B('Brochure in PDF', '#brochure', variant='contorno', full_m=True),
          dir='row', dir_m='column', wrap=(True, True, False), gap=(16, 16, 12), mt='l'),
        w=(41.67, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    foto = C(
        I(img('am400-quattro.jpg'), 'AM400 quattro, taglia spela aggraffa automatica a 5 stazioni'),
        C(didascalia('AM400 quattro, dalla brochure Wirmec.'), border_top=1, border_color=FILETTO, pad=('xs', 0, 0, 0),
          mt='s'),
        w=(58.33, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(
        C(testo, foto, dir='row', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
        indice([('Modelli', codici_link('wiram', qui=True)), ('Accessori', codici_link('accessori', qui=True))], mt='xl'),
        pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-auto-apre', anchor='content', stile_extra=CSS_INDICE)


NA = f'{NB}mm²'
WIRAM_SCHEDE = [
    dict(nome='AM210 futura', sotto='Taglia spela aggraffa automatica',
         testo='Molto compatta, per cavi molto sottili fino a 34 AWG. Ha di serie lo svolgitore della bobina e il '
               'prealimentatore integrato, che porta il cavo all’alimentatore senza stirarlo; la guida filo si cambia con '
               'un innesto rapido.',
         dati=['n.d.', '16–34 AWG', 'n.d.', f'3{NB}m/s', f'700{NB}kg, macchina base', f'1900 x 900 x 1500{NB}mm'],
         foto='am210-futura.jpg'),
    dict(nome='AM310 quattro', sotto='Taglia spela aggraffa, fino a 5 stazioni',
         testo='Pensata per lavorazioni del cavo molto diverse tra loro. Di serie: alimentatore a cinghie, testa di taglio '
               'programmabile, raddrizzatori con posizione memorizzabile, PC con monitor da 21 pollici, connessione Wi-Fi, '
               'Ethernet e USB, protezione apribile verso l’alto, conformità CE.',
         dati=['fino a 5', f'0,13–2,5{NA} (4{NA} a richiesta)', f'1–20{NB}mm (oltre a richiesta)', f'8,5{NB}m/s',
               f'800{NB}kg', f'3000 x 1400 x 2000{NB}mm'],
         foto='am310-quattro-riga.jpg', pdf=('am310quattro.pdf', '1,8')),
    dict(nome='AM350 quattro', sotto='Per cavo flat e Nily',
         testo='Studiata per i vari tipi di cavo flat e Nily: si presta a spelature molto lunghe e a un attrezzaggio veloce '
               'per il cambio cavo.'),
    dict(nome='AM400 quattro', sotto='Taglia spela aggraffa, fino a 5 stazioni',
         testo='Con la testa di taglio a sei lame e un sistema avanzato di alimentazione del cavo, lavora le piccole sezioni '
               'con una produttività molto alta.',
         dati=['fino a 5', f'0,13–4{NA} (6{NA} a richiesta)', f'1–15{NB}mm', f'8{NB}m/s', f'1100{NB}kg', 'n.d.'],
         foto='am400-quattro-riga.jpg', pdf=('am400quattro_eng_0.pdf', '2,9')),
    dict(nome='AM460 Sintesi', sotto='Taglia spela aggraffa, fino a 5 stazioni e 3 aggraffatrici',
         testo='Porta in un telaio compatto la tecnica delle macchine di fascia superiore. Di serie: accatastatore con nastro '
               'trasportatore di 2 m, alimentatore a 4 rulli convertibile a cinghie, salvataggio dei codici di lavorazione, '
               'pannello remoto per i parametri del lato 1.',
         dati=['fino a 5', f'0,13–6{NA} (26–10 AWG)', f'0,1–15{NB}mm (fino a 30 a richiesta)', f'8,5{NB}m/s',
               f'circa 750{NB}kg, macchina base', f'3400 x 1400 x 2000{NB}mm'],
         foto='am460-riga.jpg'),
    dict(nome='AM500 Vantage', sotto='Taglia spela aggraffa, fino a 6 stazioni',
         testo='Completamente automatica, pensata per un utilizzo facile e una manutenzione ridotta. A richiesta: '
               'regolazione elettronica dell’altezza di aggraffatura, misura integrata dell’altezza, prova di trazione '
               'integrata.',
         dati=['fino a 6', f'0,13–6{NA} (10{NA} a richiesta)', f'0,1–15{NB}mm (fino a 30 a richiesta)', f'12{NB}m/s',
               f'1300{NB}kg', 'n.d.'],
         foto='am500-vantage.jpg', pdf=('am500vantage_eng_0.pdf', '0,8')),
    dict(nome='AM600 Vantage', sotto='Taglia spela aggraffa, 6 stazioni, doppio cavo',
         testo='Lavora due cavi diversi sulla stessa macchina, con il sistema a doppio cavo brevettato.',
         dati=['6', f'0,13–2,5{NA}, 6{NA} con cavo doppio', f'0,1–15{NB}mm (fino a 30 a richiesta)', f'12{NB}m/s',
               f'1300{NB}kg', 'n.d.'],
         foto='am600-doppio-cavo.jpg', dida='Il gruppo del doppio cavo, dalla brochure.', pdf=('am600vantage_eng_0.pdf', '1,6')),
]
ETICHETTE_WIRAM = ['Stazioni', 'Sezione cavo', 'Lunghezza spelatura', 'Velocità cavo', 'Peso', 'Ingombro L x P x H']


def riga_wiram(m):
    if m.get('foto'):
        alt = m['nome'] + (', il gruppo del doppio cavo' if m.get('dida') else ', taglia spela aggraffa automatica')
        foto = C(C(I(img(m['foto']), alt, height=(178, 168, 230), fit='contain'), bg=BIANCO, pad=16, gap='0'),
                 *([didascalia(m['dida'], mt='xs')] if m.get('dida') else []),
                 w=(22, 30, 100), gap='0')
    else:
        foto = C(w=(22, 30, 100), gap='0', hide=['mobile'])          # niente segnaposto: il testo resta al suo posto
    azioni = []
    if m.get('pdf'):
        azioni.append(f'<a href="{pdf(m["pdf"][0])}">Brochure PDF ({m["pdf"][1]}{NB}MB)</a>')
    azioni.append(f'<a href="{richiesta("wiram", m["nome"])}">{freccia("Richiedi un’offerta")}</a>')
    testo = C(
        H(m['nome'], 'h3', color=INK),
        T(f'<p>{m["sotto"]}</p>', style='small', color=TESTO2, mt='xxs'),
        T(f'<p>{m["testo"]}</p>', style='small', color=INK, mt='s'),
        T(f'<p>{"".join(azioni)}</p>', style='link', color=ROSSO_SCURO, link_color=ROSSO_SCURO, link_hover=INK,
          css='wrm-link wrm-azioni', mt='s'),
        w=(40, 70, 100), gap='0', pad=((0, 0, 'm'), (32, 0, 0), 0, (32, 24, 0)))
    if m.get('dati'):
        dati = dl2(list(zip(ETICHETTE_WIRAM, m['dati'])))
    else:
        dati = T(f'<p>I dati tecnici della AM350 quattro non sono pubblicati: '
                 f'<a href="{richiesta("wiram", m["nome"])}">chiedili con il modulo</a>.</p>', style='small', color=TESTO2,
                 link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link')
    return C(foto, testo, C(dati, w=(38, 100, 100), gap='0', mt=(0, 'm', 'm')),
             dir='row', dir_m='column', wrap=(False, True, False), gap='0', pad=((32, 28, 24), 0, (32, 28, 28), 0),
             border_bottom=1, border_color=FILETTO_G, anchor=ancora(m['nome']))


def automatiche_modelli():
    """A2: un catalogo a righe; foto, testo e dati in colonne fisse, letti dall'alto diventano una tabella."""
    return sezione(
        testa('Sette modelli', 'Dati dalle schede Wirmec. n.d.: dato non pubblicato nella scheda.', stile_lead='small'),
        C(*[riga_wiram(m) for m in WIRAM_SCHEDE], gap='0', border_top=2, border_color=INK, mt='xl'),
        bg=GRIGIO, css='wrm-modelli', anchor='modelli', stile_extra=CSS_DL2 + CSS_AZIONI)


CSS_PIANTA = (
    f'.wrm-quota-o{{position:relative;height:13px;margin:0 0 14px 48px;border-left:1px solid {INK};border-right:1px solid {INK}}}'
    f'.wrm-quota-o::before{{content:"";position:absolute;left:0;right:0;top:6px;border-top:1px solid {INK}}}'
    f'.wrm-quota-o span,.wrm-quota-v span{{position:absolute;background:{BIANCO};padding:0 10px;font:500 13px/15px {F_SANS};'
    f'color:{INK};white-space:nowrap}}'
    '.wrm-quota-o span{left:50%;top:-1px;transform:translateX(-50%)}'
    '.wrm-quota-v{position:relative;width:40px;height:100%;min-height:120px}'
    f'.wrm-quota-v::before{{content:"";position:absolute;top:0;bottom:0;left:20px;border-left:1px solid {INK}}}'
    f'.wrm-quota-v::after{{content:"";position:absolute;top:0;bottom:0;left:14px;width:13px;border-top:1px solid {INK};'
    f'border-bottom:1px solid {INK};box-sizing:border-box}}'
    '.wrm-quota-v span{top:50%;left:20px;transform:translate(-50%,-50%) rotate(-90deg)}'
    '@media (max-width:767px){.wrm-quota-v{width:28px}.wrm-quota-v::before{left:14px}.wrm-quota-v::after{left:8px}'
    '.wrm-quota-v span{left:14px;padding:0 6px}}'
    '.wrm-pianta .wrm-disegno{align-self:stretch}'
)


def automatiche_pianta():
    """A3: la pianta quotata della AM310 quattro (direzione "misura"), con la legenda delle stazioni."""
    alt = 'Pianta della AM310 quattro con le stazioni A1, A2, A3, B1, B2, B3'
    disegno = C(
        RAW('<div class="wrm-quota-v" aria-hidden="true"><span>1400 mm</span></div>', fisso=True),
        C(I(img('pianta-am310.png'), alt, hide=['mobile']),
          I(img('pianta-am310-stazioni.png'), alt + ', la zona delle stazioni', hide=['desktop', 'tablet']),
          gap='0', grow=True),
        dir='row', gap=(8, 8, 6), css='wrm-disegno')
    legenda = [('A1 e B1', '<a href="#am-0064">AM&nbsp;0064</a>, attorcigliatore programmabile'),
               ('A2 e B2', '<a href="#am-0010">AM&nbsp;0010</a> o <a href="#am-0012">AM&nbsp;0012</a>, aggraffatrice'),
               ('A3 e B3', '<a href="#am-0038">AM&nbsp;0038</a>, stazione di stagnatura e flussatura')]
    foglio = C(
        RAW('<div class="wrm-quota-o" aria-hidden="true"><span>3000 mm</span></div>', hide=['mobile']),
        disegno,
        C(*[C(nome(sig), T(f'<p>{u}</p>', style='small', color=INK, link_color=ROSSO_SCURO, link_hover=INK, mt='xxs',
                         css='wrm-link'),
              w=(33.33, 33.33, 100), gap='0', pad=(0, (24, 24, 0), 0, 0)) for sig, u in legenda],
          dir='row', dir_m='column', gap='0', gap_r=(0, 0, 16), border_top=1, border_color=FILETTO, pad=('s', 0, 0, 0),
          mt='m'),
        didascalia('AM310 quattro, pianta dalla brochure Wirmec. Ingombro 3000 x 1400 mm, altezza 2000 mm.', mt='m'),
        gap='0', border=1, border_color=FILETTO, pad=(48, 32, 16), mt='xl')
    return sezione(
        testa('La AM310 quattro in pianta',
              'Le stazioni si montano attorno alla testa di taglio, tre per lato. Qui una delle configurazioni della '
              'brochure, con l’ingombro della macchina.', stile_lead='body'),
        foglio, css='wrm-pianta', anchor='pianta', stile_extra=CSS_PIANTA)


def automatiche_postazione():
    """A4: la postazione dell'operatore su ardesia, la foto a filo del bordo sinistro della pagina (Zünd)."""
    voci = ['Salvataggio dei codici di lavorazione (AM460 Sintesi)',
            'Pannello remoto per i parametri del lato 1 (AM460 Sintesi)',
            'Ampia possibilità di salvare i parametri (brochure AM500)',
            'Consolle con portaoggetti e porta disegni (AM310 quattro)']
    foto = C(I(img('postazione-vantage.jpg'), 'Postazione dell’operatore di una WirAM Vantage, con PC e pannello'),
             w=(52.78, 100, 100), gap='0', pad=(0, (0, 32, 0), 0, (0, 32, 0)))
    testo = C(
        *titolo_h2('Dal pannello si prepara la lavorazione', colore=BIANCO),
        T('<p>Sulle WirAM la lavorazione si imposta e si salva dall’interfaccia operatore, in italiano. La AM310 quattro '
          'ha di serie un PC con monitor da 21 pollici e la connessione Wi-Fi, Ethernet e USB.</p>', style='body',
          color=SU_SCURO2, mt='m'),
        C(*[C(T(f'<p>{v}</p>', style='small', color=BIANCO), pad=(12, 0, 12, 0), border_bottom=1, border_color=FILETTO_S,
              gap='0') for v in voci],
          gap='0', border_top=1, border_color=FILETTO_S, mt='l'),
        w=(47.22, 100, 100), gap='0', pad=(0, (0, 32, 20), 0, (64, 32, 20)), mt=(0, 'xl', 'l'), css='wrm-post-testo')
    return sezione(C(foto, testo, dir='row', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
                   bg=ARDESIA, pad=('sezione', 0), boxed=False, css='wrm-postazione wrm-scuro', anchor='postazione',
                   stile_extra=CSS_SCURO + '@media (min-width:1025px){.wrm-post-testo{padding-right:max(48px,calc((100% - 1280px) / 2))!important}}')


LAV = {k: (t, n) for k, t, _, n in LAVORAZIONI}
ACCESSORI = [
    dict(codice='AM 0010', nome='Aggraffatrice per macchina automatica 20 kN', lav='aggraffatura', foto='am0010.jpg',
         testo='Con aggancio rapido dell’applicatore, base su quattro colonne regolabile in altezza, cassetto sfridi '
               'removibile, punto morto inferiore regolabile a mano (standard 135,78 mm). A richiesta: controllo della '
               'forza di aggraffatura (CFM) a 3 zone, taglia bandella, avvolgicarta.',
         dati=[f'Forza 20{NB}kN', f'Sezione fino a 6{NA}', f'165 x 350 x 850{NB}mm', f'70{NB}kg']),
    dict(codice='AM 0011', nome='Aggraffatrice per taglia spela aggraffa 30 kN', lav='aggraffatura', foto='am0011.jpg',
         testo='Come la AM 0010, con forza di 30 kN e sezione fino a 10 mm².',
         dati=[f'Forza 30{NB}kN', f'Sezione 10{NA}', f'165 x 350 x 850{NB}mm', f'75{NB}kg']),
    dict(codice='AM 0012', nome='Aggraffatrice con regolazione elettronica dell’altezza', lav='aggraffatura',
         foto='am0012.jpg'),
    dict(codice='AM 0038', nome='Stazione di stagnatura e flussatura', lav='attorcigliatura-e-stagnatura',
         testo='Unità stretta e compatta, si integra facilmente; stagna in cascata o a onda, va in temperatura in poco '
               'tempo e si pulisce dal condotto di scarico dello stagno.',
         dati=[f'Crogiolo 7{NB}kg', 'Lega senza piombo', f'230{NB}V, 1056{NB}W', f'8{NB}kg a vuoto',
               f'135 x 535 x 450{NB}mm']),
    dict(codice='AM 0040', nome='Unità doppiatore cavo', lav='doppiatore-cavo'),
    dict(codice='AM 0061', nome='Unità di attorcigliatura removibile', lav='attorcigliatura-e-stagnatura',
         foto='am0061.jpg',
         testo='Unità removibile per attorcigliare la spelatura, con aspirazione e raccolta dello sfrido.',
         dati=[f'Sezione fino a 2,5{NA} (4{NA} a richiesta)', f'Attorcigliatura 3–15{NB}mm', 'Oraria e antioraria',
               f'6{NB}bar', f'70 x 350 x 130{NB}mm']),
    dict(codice='AM 0063', nome='Spelatrice coassiale',
         testo='Per cavi coassiali o speciali che non si spelano in modo convenzionale; si programma dall’interfaccia della '
               'macchina e scarica lo sfrido nella cassetta scarti.',
         dati=[f'Spelatura 0,5–10{NB}mm', f'Diametro isolante 0,5–4,5{NB}mm']),
    dict(codice='AM 0064', nome='Attorcigliatore programmabile', lav='attorcigliatura-e-stagnatura', foto='am0064.jpg',
         testo='Per cavi unipolari, anche molto sottili: velocità e giri programmabili dall’interfaccia, ganasce '
               'intercambiabili, sistema antirotazione, regolabile in altezza, estrattore e aspiratore sfridi.',
         dati=[f'Sezione 0,03–2,5{NA}', f'Spelatura 1–15{NB}mm (20 sulla AM310)', 'Motore passo passo',
               f'24{NB}Vdc, 6–7{NB}bar', f'160 x 370 x 480{NB}mm'],
         pdf=('am-0064_eng.pdf', '0,9')),
    dict(codice='AM 0083', nome='Inseritore coprifaston 6,3, 4,8 e 2,8', lav='inserimento-guaina', foto='am0083.jpg',
         testo='Unità indipendente e compatta: passa da una misura all’altra cambiando il kit di selezione e alimentazione; '
               'la lavorazione si sceglie dal pannello touch.'),
    dict(codice='AM 0090', nome='Inseritore gommino', lav='inserimento-gommino', foto='am0090.png',
         testo='Alimentatore intercambiabile, programmabile da pannello touch screen; con la logica integrata si monta anche '
               'su altre macchine automatiche.'),
]

CSS_ACC = (
    '.wrm-acc .wrm-dis{max-width:300px!important}'
    '@media (max-width:1024px){.wrm-acc .wrm-acc-foto img{object-position:left center}}'
)


def scheda_accessorio(a):
    corpo = [T(f'<p>{unito(a["codice"])}</p>', style='dato_s', color=TESTO2),
             H(a['nome'], 'h3', style='nome', color=INK, mt='xxs')]
    if a.get('lav'):
        t, n = LAV[a['lav']]
        corpo.append(C(disegno_lavorazione(a['lav'], t, n), gap='0', mt='s', css='wrm-dis'))
    if a.get('testo'):
        corpo.append(T(f'<p>{a["testo"]}</p>', style='small', color=INK, mt='s'))
    if a.get('dati'):
        corpo.append(T('<p>' + '<br>'.join(a['dati']) + '</p>', style='dato_s', color=INK, mt='s'))
    if a.get('pdf'):
        corpo.append(T(f'<p><a href="{pdf(a["pdf"][0])}">Brochure {unito(a["codice"])} (PDF, inglese, {a["pdf"][1]}{NB}MB)'
                       '</a></p>', style='link', color=ROSSO_SCURO, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link',
                       mt='s'))
    figli = []
    if a.get('foto'):
        figli.append(C(I(img(a['foto']), f'{a["codice"]}, {a["nome"][0].lower() + a["nome"][1:]}', height=(220, 240, 220),
                         fit='contain'),
                       w=(34, 100, 100), gap='0', pad=(0, (24, 0, 0), 0, 0), css='wrm-acc-foto'))
    figli.append(C(*corpo, w=(66 if a.get('foto') else 100, 100, 100), gap='0', mt=(0, 's', 's') if a.get('foto') else 0))
    return C(*figli, dir='row', dir_t='column', gap='0', bg=BIANCO, pad=(32, 24, 20), w=(48.5, 48.5, 100),
             anchor=ancora(a['codice']))


def automatiche_accessori():
    """A5: le dieci unità, con la foto (se c'è), il disegno della lavorazione che fanno e i dati (TRUMPF, Komax)."""
    return sezione(
        testa('Accessori macchina, le stazioni',
              'Dieci unità da montare sulle taglia spela aggraffa WirAM: aggraffatrici, inseritori di gommino e '
              'coprifaston, unità di stagnatura, attorcigliatura, doppiatura e spelatura coassiale. Accanto al nome, il '
              'disegno della lavorazione.'),
        C(*[scheda_accessorio(a) for a in ACCESSORI], dir='row', wrap=True, justify='between', gap='0',
          gap_r=(36, 28, 20), mt='xl'),
        bg=GRIGIO, css='wrm-acc', anchor='accessori', stile_extra=CSS_ACC)


def automatiche():
    return [('apertura', automatiche_apertura()), ('modelli', automatiche_modelli()), ('pianta', automatiche_pianta()),
            ('postazione', automatiche_postazione()), ('accessori', automatiche_accessori()),
            ('brochure', sezione_brochure([('AM310 quattro', 'am310quattro.pdf', 'inglese', '1,8'),
                                           ('AM400 quattro', 'am400quattro_eng_0.pdf', 'inglese', '2,9'),
                                           ('AM500 Vantage', 'am500vantage_eng_0.pdf', 'inglese', '0,8'),
                                           ('AM600 Vantage', 'am600vantage_eng_0.pdf', 'inglese', '1,6'),
                                           ('AM 0064 attorcigliatore', 'am-0064_eng.pdf', 'inglese', '0,9')],
                                          'Le brochure delle automatiche sono in inglese.', (18, 31.33, 47),
                                          'wrm-broch-auto')),
            ('richiesta', blocco_richiesta('wiram'))]


# ---------------------------------------------------------------------------------------------
# 03 DA BANCO: WirPress e WirStrip (specifica, paragrafo 8)
# ---------------------------------------------------------------------------------------------
PRESSE = [('W15', f'20{NB}kN', 'w15.jpg', ''), ('W15 SC', f'20{NB}kN, split cycle', '', ''),
          ('W 1500', f'20{NB}kN', 'w1500-banco.png', ''), ('W 2000', f'25{NB}kN', 'w2000-w3000.png', ''),
          ('W 3000', f'30{NB}kN', 'w2000-w3000.png', f'Stesso corpo macchina della W{NB}2000, 325 x 325 x 735{NB}mm.')]
FRASE_APPLICATORI = 'Le nostre presse si usano anche con gli applicatori di altri costruttori.'


def banco_apertura():
    """B1: la pagina apre con le macchine: le cinque presse in fila, ciascuna sopra il suo codice (Salvagnini B3)."""
    celle = []
    for cod, forza, foto, nota in PRESSE:
        if foto:
            box = I(img(foto), f'{cod}, aggraffatrice da banco {forza.replace(NB, " ").split(",")[0]}',
                    height=(280, 200, 140), fit='contain', css='wrm-fila-foto')
        else:
            box = C(min_h=(280, 200, 140), gap='0')          # W15 SC: la foto del sito è rotta, nessun riquadro
        celle.append(C(
            box,
            C(H(unito(cod), 'p', style='h3', color=INK, css='wrm-nome'),
              T(f'<p>{forza}</p>', style='dato_s', color=TESTO2, mt='xxs'),
              *([T(f'<p>{nota}</p>', style='meta', color=TESTO2, mt='xs')] if nota else []),
              gap='0', border_top=2, border_color=INK, pad=('xs', 0, 0, 0), mt='s'),
            w=(20, 20, 33.33), gap='0', pad=(0, (24, 16, 12), 0, 0), link=f'#{ancora(cod)}', css='wrm-cl'))
    fila = C(*celle, dir='row', wrap=(False, False, True), gap='0', gap_r=(0, 0, 'l'), align='start', css='wrm-fila')
    testo = C(
        C(T('<p>WirPress e WirStrip</p>', style='kicker', color=TESTO2),
          H('Macchine da banco', 'h1', color=INK, mt='s'), w=(50, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0)),
        C(T('<p>Aggraffatrici da banco da 20, 25 e 30 kN, spela aggraffa dalla elettropneumatica alla elettronica con '
            'inseritore di gommino, e le WirStrip per tagliare e sguainare cavi di grosso diametro.</p>', style='lead',
            color=INK),
          T(f'<p><strong>{FRASE_APPLICATORI}</strong></p>', style='body', color=INK, mt='s', css='wrm-forte'),
          w=(50, 100, 100), gap='0', mt=(0, 'm', 'm')),
        dir='row', dir_t='column', align='end', gap='0', mt='xl')
    return sezione(
        fila, testo,
        indice([('Presse', codici_link('presse', qui=True)), ('Spela aggraffa', codici_link('spela', qui=True)),
                ('WirStrip', codici_link('wirstrip', qui=True))], mt='l'),
        pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-banco-apre', anchor='content',
        stile_extra=CSS_INDICE + '.wrm-fila .wrm-fila-foto img{object-position:center bottom!important}'
                    '.wrm-forte strong{font-weight:600}')


def banco_presse():
    """B2: i cinque modelli in colonna, le grandezze in riga: si confrontano con un'occhiata (Salvagnini B3)."""
    br = lambda f, mb: f'<a href="{pdf(f)}">Brochure PDF</a> <span class="wrm-nd">{mb}{NB}MB</span>'
    testo = lambda x: (f'<span class="wrm-tab-testo">{x}</span>')
    testa_col = [('Modello', None)] + [(unito(c), ancora(c)) for c in CODICI['presse']]
    righe = [
        ('Versione', None, [testo(x) for x in ('Versione dritta', 'Split cycle, per terminali chiusi e ferrules',
                                               'Semplice e compatta', 'Controllo a inverter', 'Controllo a inverter')]),
        ('Forza di aggraffatura', None, [f'20{NB}kN'] * 3 + [f'25{NB}kN', f'30{NB}kN']),
        ('Corsa', None, [f'40{NB}mm'] * 5),
        ('Sezione max', None, [f'6{NA}'] * 4 + [f'10{NA}']),
        ('Spessore terminale max', None, [f'0,6{NB}mm'] * 3 + [f'0,8{NB}mm', f'1,1{NB}mm']),
        ('Potenza', None, ['n.d.', 'n.d.', f'0,75{NB}kW', f'1,1{NB}kW', f'1,1{NB}kW']),
        ('Tempo ciclo', None, [f'0,3{NB}s', f'0,3{NB}s', 'n.d.', 'n.d.', 'n.d.']),
        ('Alimentazione', None, [(f'230{NB}V monofase, su tutte', 5)]),
        ('Dimensioni L x P x H', None, ['n.d.'] + [f'390 x 350 x 1020{NB}mm'] * 2 + [f'325 x 325 x 735{NB}mm'] * 2),
        ('Peso', None, [f'45{NB}kg'] * 3 + [f'60{NB}kg'] * 2),
        ('Documenti', None, ['n.d.', 'n.d.', br('wirmec_w1500.pdf', '0,3'), br('wirmec_w2000.pdf', '0,4'),
                             br('wirmec_w3000.pdf', '0,4')]),
    ]
    in_piu = [
        ('W15', 'Applicatori di grandi dimensioni, aggancio rapido, braccio porta bobina girevole per terminali frontali e '
                'laterali, illuminazione a led, avvolgicarta, kit ciclo aria per applicatore pneumatico, controllo '
                'dell’aggraffatura con certificato di calibrazione.'),
        ('W15 SC', 'Split cycle a singola e doppia azione; a richiesta controllo elettronico dell’aggraffatura con '
                   'certificato di calibrazione.'),
        (f'W{NB}2000 e W{NB}3000', 'La forma facilita il cambio dell’applicatore e il caricamento dei terminali; braccio '
                                   'doppio per bobine end feed e side feed a richiesta.'),
    ]
    piu = C(
        T('<p>In più, per modello</p>', style='label', color=TESTO2),
        C(*[C(H(c, 'p', style='nome', color=INK, w_px=(220, 180, None), fisso=True),
              T(f'<p>{x}</p>', style='small', color=INK, grow=True, max_w=(760, 760, 600)),
              dir='row', dir_m='column', gap=('s', 's', 'xxs'), align=('baseline', 'baseline', 'start'),
              pad=(14, 0, 14, 0), border_bottom=1, border_color=FILETTO_G) for c, x in in_piu],
          gap='0', border_top=1, border_color=FILETTO_G, mt='xs'),
        gap='0', mt='l')
    return sezione(
        testa('Presse da banco',
              f'Su tutte: altezza del punto morto inferiore regolabile, standard 135,78{NB}mm; selettore jog per la corsa '
              'lenta; contatore elettronico azzerabile; controllo della forza di aggraffatura (CFM) a richiesta.',
              colore_lead=INK, stile_lead='body'),
        C(tabella('wrm-presse', 'presse da banco', testa_col, righe, bg=GRIGIO, fil=FILETTO_G, prima=(220, 150, 130),
                  min_col=132), gap='0', mt='xl'),
        didascalia('n.d.: dato non pubblicato nella scheda.', mt='s'),
        piu,
        link_freccia('Richiedi un’offerta per una pressa', richiesta('wirpress'), mt='l'),
        bg=GRIGIO, css='wrm-presse', anchor='presse')


def banco_spela():
    """B3: quattro macchine che spelano e aggraffano in un ciclo: la WSC 15 grande, le note, la tabella, i brevetti."""
    nota = [('WSC 15', 'Per chi non cambia lavorazione di continuo; regolazioni di sezione e spelatura a display, '
                       'estrattore mobile, scivolo per applicatori senza taglia bandella, aspirazione sfridi.'),
            ('WSC 25', 'Per terminali preisolati e ferrules blu, rossi e gialli cambiando solo l’applicatore '
                       f'<a href="/applicatori/#wb-14">WB{NB}14</a>; lavora anche terminali aperti.')]
    foto = C(I(img('wsc15.jpg'), 'WSC 15, spela aggraffa elettropneumatica', w_img=(400, 400, 350)),
             C(didascalia(f'WSC{NB}15, dalla brochure Wirmec.'), border_top=1, border_color=FILETTO, pad=('xs', 0, 0, 0),
               mt='s', max_w=(400, 400, 350)),
             w=(33.33, 100, 100), gap='0')
    destra = C(
        C(*[C(H(unito(c), 'p', style='nome', color=INK, w_px=(120, 120, None), fisso=True),
              T(f'<p>{x}</p>', style='small', color=INK, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link', grow=True),
              dir='row', dir_m='column', gap=('s', 's', 'xxs'), align=('baseline', 'baseline', 'start'),
              pad=(16, 0, 16, 0), border_bottom=1, border_color=FILETTO) for c, x in nota],
          gap='0', border_top=2, border_color=INK),
        C(link_freccia('Richiedi un’offerta per una spela aggraffa', richiesta('wirpress')),
          T(f'<p><a href="{pdf("wirmec_wsc15_taglia_spela.pdf")}">Brochure WSC{NB}15 (PDF, italiano, 0,6{NB}MB)</a></p>',
            style='link', color=ROSSO_SCURO, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link'),
          dir='row', dir_m='column', wrap=True, gap=(32, 32, 12), mt='l'),
        w=(66.67, 100, 100), gap='0', pad=(0, 0, 0, (48, 0, 0)), mt=(0, 'l', 'l'))
    modello = lambda c, t: f'<span class="wrm-tab-nome">{unito(c)}</span><span class="wrm-tab-sotto">{t}</span>'
    testa_col = [('Modello', None), ('Sezione cavo', None), ('Spelatura', None), ('Cavo min', None),
                 ('Ø esterno max', None), ('Tempo ciclo', None), ('Ricette', None), ('Peso', None)]
    righe = [
        (modello('WSC 15', 'elettropneumatica'), 'wsc-15',
         [f'0–4{NA}', f'0–11{NB}mm', f'20{NB}mm', f'6{NB}mm', f'1{NB}s', 'n.d.', f'60{NB}kg']),
        (modello('WSC 21', 'elettronica'), 'wsc-21',
         [f'0–4{NA}', f'0–11{NB}mm', f'20{NB}mm', f'4,5{NB}mm', f'&lt;{NB}0,8{NB}s', '200', f'65{NB}kg']),
        (modello('WSC 25', 'per terminali chiusi'), 'wsc-25',
         [f'0–4{NA}', f'0–11{NB}mm', f'20{NB}mm', 'n.d.', f'1,3{NB}s', '200', f'105{NB}kg']),
        (modello('WSC 31', 'con inseritore gommino'), 'wsc-31',
         [('<span class="wrm-tab-testo wrm-nd">Dati non pubblicati nella scheda: '
           f'<a href="{richiesta("wirpress", "WSC 31")}">chiedili con il modulo</a>.</span>', 7)]),
    ]
    brevetti = C(
        H('Due brevetti sulla WSC 21', 'h3', color=INK),
        riga_numerata(1, 'Movimento elettronico della testa di sezione e spelatura, per aggraffare con alta precisione '
                         'terminali e sezioni di cavo molto piccole.', mt='m'),
        riga_numerata(2, 'Protezione della pinza, per lavorare cavi unipolari e multipolari lunghi fino a 20 mm, con '
                         'movimento verticale elettronico a tempo regolabile.', mt='s'),
        didascalia('Dalla scheda WSC 21.', mt='s'),
        w=(50, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    wsc31 = C(
        C(H('WSC 31', 'h3', color=INK),
          T('<p>La WSC 31 è il modello di punta WirPress: spelatura, inserzione del gommino e aggraffatura in un solo ciclo. '
            'Nata dalla WSC 21, ha l’unità elettronica di inserimento del gommino con sistema brevettato; ogni '
            'posizionamento è motorizzato e si salva dal pannello touch screen.</p>', style='body', color=INK, mt='s'),
          gap='0', grow=True),
        I(img('wsc31.jpg'), 'WSC 31, spela aggraffa con inseritore di gommino, vista di fianco', w_img=(220, 260, 200),
          fisso=True),
        dir='row', dir_m='column', gap=('m', 'm', 's'), align='start', w=(50, 100, 100), mt=(0, 'l', 'l'))
    return sezione(
        testa('Spela aggraffa', 'Spelano, aggraffano e, sulla WSC 31, inseriscono il gommino in un solo ciclo. Montano '
                                'applicatori side feed ed end feed.'),
        C(foto, destra, dir='row', dir_t='column', align='start', gap='0', mt='xl'),
        C(tabella('wrm-spela', 'spela aggraffa', testa_col, righe, prima=(240, 200, 150), min_col=120), gap='0', mt='xl'),
        didascalia('Cavo min: lunghezza minima del cavo, sotto i 20 mm a richiesta. n.d.: dato non pubblicato nella '
                   'scheda.', mt='s'),
        C(brevetti, wsc31, dir='row', dir_t='column', gap='0', border_top=2, border_color=INK, pad=('l', 0, 0, 0),
          mt='xl'),
        css='wrm-spela', anchor='spela-aggraffa')


WSG = [
    ('WSG 100', 'Troncatrice da banco', 'Taglia cavi di grosse dimensioni.',
     [('Diametro max di taglio', f'14{NB}mm'), ('Peso', f'9{NB}kg'), ('Dimensioni', '370 x 150 x 230')], 'wsg100.jpg'),
    ('WSG 200', 'Sguainatrice da banco', 'Sguainatrice manuale per cavi unipolari e multipolari, anche di grossa sezione.',
     [('Diametro max del cavo', f'14{NB}mm'), ('Sguainatura', f'25–250{NB}mm'), ('Peso', f'25{NB}kg'),
      ('Dimensioni', f'365 x 550 x 290{NB}mm')], 'wsg200.jpg'),
    ('WSG 300', 'Sguainatrice da banco', 'Per cavi di grosso diametro e sguainature molto lunghe; si completa con kit di '
                                         'lame raggiate a richiesta, costruite sul cavo campione. Conforme CE.',
     [('Diametro isolante', f'5–25{NB}mm'), ('Spelatura', f'50–500{NB}mm'), ('Spelatura parziale max', f'250{NB}mm'),
      ('Alimentazione', f'230{NB}V, aria min 6{NB}bar'), ('Peso', f'60{NB}kg'), ('Dimensioni', f'950 x 400 x 300{NB}mm')],
     ''),
]


def banco_wirstrip():
    """B4: le uniche macchine Wirmec con la carrozzeria rossa, su riquadri bianchi; i dati sotto ciascuna."""
    colonne = []
    for cod, sotto, testo, dati, foto in WSG:
        if foto:
            box = C(I(img(foto), f'{cod}, {sotto.lower()}', height=(258, 190, 230), fit='contain'), bg=BIANCO, pad=16,
                    gap='0')
        else:
            box = C(min_h=(290, 222, 0), gap='0', hide=['mobile'])   # WSG 300: foto rotta sul sito, nessun riquadro
        colonne.append(C(
            box,
            C(H(unito(cod), 'h3', color=INK),
              T(f'<p>{sotto}</p>', style='small', color=TESTO2, mt='xxs'),
              T(f'<p>{testo}</p>', style='small', color=INK, mt='s'),
              dati_dl(dati, 'wrm-dl-grigio', mt='m'),
              gap='0', border_top=2, border_color=INK, pad=('s', 0, 0, 0), mt=('s', 's', 0 if not foto else 's')),
            w=(32, 32, 100), gap='0', anchor=ancora(cod)))
    return sezione(
        testa('WirStrip, taglio e sguainatura', 'Una troncatrice e due sguainatrici da banco per cavi unipolari e '
                                                'multipolari, anche di grosso diametro e con sguainature lunghe.'),
        C(*colonne, dir='row', dir_m='column', justify='between', gap='0', gap_r=(0, 0, 'xl'), mt='xl'),
        link_freccia('Richiedi un’offerta per una WirStrip', richiesta('wirstrip'), mt='l'),
        bg=GRIGIO, css='wrm-wirstrip', anchor='wirstrip')


def da_banco():
    return [('apertura', banco_apertura()), ('presse', banco_presse()), ('spela-aggraffa', banco_spela()),
            ('wirstrip', banco_wirstrip()),
            ('brochure', sezione_brochure([('W 1500', 'wirmec_w1500.pdf', 'inglese', '0,3'),
                                           ('W 2000', 'wirmec_w2000.pdf', 'inglese', '0,4'),
                                           ('W 3000', 'wirmec_w3000.pdf', 'inglese', '0,4'),
                                           ('WSC 15', 'wirmec_wsc15_taglia_spela.pdf', 'italiano', '0,6')],
                                          'Le brochure delle presse sono in inglese; quella della WSC 15 in italiano.',
                                          (23, 22.5, 47), 'wrm-broch-banco')),
            ('richiesta', blocco_richiesta('wirpress'))]


# ---------------------------------------------------------------------------------------------
# 04 APPLICATORI: WirTool (specifica, paragrafo 9)
# ---------------------------------------------------------------------------------------------
def applicatori_apertura():
    """C1: WB 10 e WPB 10 grandi sul grigio uguale al fondo delle loro foto; titolo e dati comuni accanto."""
    dati = [('Corsa', f'40{NB}mm'), ('Corsa di alimentazione', f'30{NB}mm'), ('Ghiera di registro', '4 posizioni'),
            ('Peso', f'&lt;{NB}4{NB}kg'), ('Contatore, a richiesta', '6 cifre, non azzerabile'),
            ('Ghiera micrometrica, a richiesta', f'passo 0,02{NB}o{NB}0,01{NB}mm, corsa{NB}3{NB}mm')]
    sinistra = C(
        T('<p>WirTool</p>', style='kicker', color=TESTO2),
        H('Applicatori side feed ed end feed', 'h1', color=INK, mt='s'),
        T('<p>Applicatori per l’aggraffatura side feed ed end feed, con movimentazione meccanica e pneumatica, e sistemi '
          'per il cablaggio semiautomatico di connettori IDC progettati sulla specifica del costruttore del connettore.</p>',
          style='lead', color=INK, max_w=(520, 640, 560), mt='m'),
        B('Richiedi un applicatore', richiesta('wirtool'), variant='primario', full_m=True, mt='l'),
        T('<p>Dati comuni, dalle schede</p>', style='label', color=TESTO2, mt='xl'),
        dati_dl(dati, 'wrm-dl-grigio wrm-dl-forte', mt='xs'),
        w=(41.67, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))

    def app(file, cod, alt, testo, alto):
        return C(C(I(img(file), alt, w_img=(360, 360, 165), css='wrm-foto-c'), min_h=alto, justify='end', gap='0'),
                 C(nome(cod), T(f'<p>{testo}</p>', style='small', color=TESTO2, mt='xxs'), gap='0',
                   border_top=1, border_color=FILETTO_G, pad=('s', 0, 0, 0), mt='s'),
                 w=(48.5, 48.5, 47), gap='0')
    destra = C(
        app('wb10.jpg', 'WB 10', 'WB 10, applicatore side feed', 'Side feed, meccanico', (390, 390, 179)),
        app('wpb10.jpg', 'WPB 10', 'WPB 10, applicatore side feed pneumatico', 'Side feed, alimentazione pneumatica',
            (390, 390, 179)),
        dir='row', justify='between', align='end', gap='0', w=(58.33, 100, 100), mt=(0, 'xl', 'xl'))
    return sezione(
        C(sinistra, destra, dir='row', dir_t='column', align=('end', 'stretch', 'stretch'), gap='0'),
        indice([('Applicatori', codici_link('wirtool', qui=True))], mt='xl'),
        bg=GRIGIO, pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-app-apre', anchor='content',
        stile_extra=CSS_INDICE + CSS_W1500)


GRUPPI_APP = [
    ('Side feed', 'Terminali in nastro laterale.', [
        ('WB 10', 'Alimentazione a rapporti di leva, dolce e silenziosa; dietro l’aggraffatura lascia ampia visibilità per '
                  'centrare e registrare. Per spela aggraffa e macchine automatiche.', f'L135 x P105 x H145{NB}mm',
         'wb10.jpg', True),
        ('WPB 10', 'Alimentazione pneumatica, per terminali a passo lungo e dove serve un’alimentazione dolce; ha gli '
                   'ingombri di un applicatore tradizionale e si monta su tutti i tipi di macchine.',
         f'L135 x P105 x H145{NB}mm', 'wpb10.jpg', True)]),
    ('End feed', 'Terminali in nastro in linea.', [
        ('WL 10', 'Passo regolabile in avanti e indietro, fino a 33 mm; leggero e facile da prendere nel cambio '
                  'lavorazione; previsto per tutti i tipi di spela aggraffa in commercio.', f'L70 x P180 x H145{NB}mm',
         'wl10.png', False)]),
    ('Ferrules', 'Terminali a tubetto.', [
        ('WB 13', 'Applicatore ferrules per aggraffatrice da banco, semiautomatico.', f'L135 x P105 x H145{NB}mm',
         'wb13.jpg', False),
        ('WB 14', 'Applicatore ferrules automatico; si monta sulla WSC 25 per terminali preisolati.', '', '', False),
        ('WPB 16', 'Side feed con alimentazione pneumatica, per ferrules.', '', 'wpb16.jpg', False)]),
    ('Splice', 'Giunzioni.', [
        ('WL 11', 'Protezione integrale: si aggraffa in sicurezza vicino al punto di aggraffatura, anche su cavi molto '
                  'corti.', f'L70 x P180 x H145{NB}mm', 'wl11.jpg', False),
        ('WL 19', 'Per il terminale di giunzione a doppia bandella: un’alternativa all’autosplice, perché lavora su '
                  'qualsiasi aggraffatrice da banco.', '', 'wl19.jpg', False)]),
    ('Contatti torniti', '', [
        ('WB 23', 'Applicatore per contatti torniti.', '', 'wb23.jpg', False)]),
    ('Bus bar', '', [
        ('WB 27', 'Per connettori bus bar, in versione manuale (il trancio lo decide l’operatore) o automatica, che lavora '
                  'anche sequenze complesse riducendo gli errori.', f'L135 x P105 x H145{NB}mm', 'wb27.jpg', False)]),
]


def scheda_applicatore(cod, testo, dati, foto, grigio, tipo):
    figli = []
    if foto:
        figli.append(C(I(img(foto), f'{cod}, applicatore {tipo.lower()}', height=(176, 176, 126), fit='contain'),
                       bg=GRIGIO if grigio else BIANCO, border=1, border_color=FILETTO, pad=12, gap='0'))
    figli += [H(unito(cod), 'h4', style='nome', color=INK, mt='s' if foto else 0),
              T(f'<p>{testo}</p>', style='small', color=INK, mt='xxs')]
    if dati:
        figli.append(T(f'<p>{dati}</p>', style='dato_s', color=TESTO2, mt='xs'))
    return C(*figli, w=(30.5, 30.5, 47), gap='0', anchor=ancora(cod))


def applicatori_elenco():
    """C2: gli applicatori raggruppati per quello che aggraffano: il tipo a sinistra, le schede a destra."""
    gruppi = []
    for tipo, riga, schede in GRUPPI_APP:
        gruppi.append(C(
            C(H(tipo, 'h3', color=INK),
              *([T(f'<p>{riga}</p>', style='small', color=TESTO2, mt='xxs')] if riga else []),
              w=(25, 100, 100), gap='0', pad=(0, (32, 0, 0), 0, 0)),
            C(*[scheda_applicatore(*x, tipo=tipo) for x in schede], dir='row', wrap=True, gap=(24, 24, 16),
              gap_r=(32, 32, 28), w=(75, 100, 100), mt=(0, 'm', 's')),
            dir='row', dir_t='column', gap='0', pad=(32, 0, 40, 0), border_top=2, border_color=INK))
    return sezione(*titolo_h2('Dieci applicatori, per tipo di terminale'), C(*gruppi, gap='0', mt='xl'),
                   css='wrm-app-elenco', anchor='elenco')


def applicatori_montaggio():
    """C3: la fila di applicatori sul banco, con le targhette rosse; accanto le macchine su cui si montano."""
    foto = C(I(img('banco-applicatori.jpg'), 'Applicatori WirTool sul banco, con la targhetta rossa',
               w_img=(720, 720, 350), css='wrm-foto-c'),
             C(didascalia('Applicatori WirTool sul banco, con la targhetta rossa. Foto della pagina Azienda del sito.'),
               border_top=1, border_color=FILETTO_G, pad=('xs', 0, 0, 0), mt='s'),
             w=(58.33, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    testo = C(
        *titolo_h2('Dove si montano'),
        T('<p>Gli applicatori WirTool sono studiati per le spela aggraffa e per le macchine automatiche; il WPB 10 si monta '
          'su tutti i tipi di macchine e il WL 10 ha gli accorgimenti per tutte le spela aggraffa in commercio.</p>',
          style='body', color=INK, mt='m'),
        C(link_freccia('Presse da banco', '/da-banco/#presse'),
          link_freccia('Spela aggraffa', '/da-banco/#spela-aggraffa'),
          link_freccia('Aggraffatrici per automatiche', '/automatiche/#am-0010'), gap='xs', mt='l'),
        w=(41.67, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(foto, testo, dir='row', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
                   bg=GRIGIO, css='wrm-montaggio', anchor='dove-si-montano', stile_extra=CSS_W1500)


def applicatori():
    return [('apertura', applicatori_apertura()), ('elenco', applicatori_elenco()),
            ('dove-si-montano', applicatori_montaggio()), ('richiesta', blocco_richiesta('wirtool'))]


# ---------------------------------------------------------------------------------------------
# 05 CONTROLLO QUALITÀ: WirTest (specifica, paragrafo 10)
# ---------------------------------------------------------------------------------------------
def qualita_apertura():
    """D1: la sezione di un'aggraffatura alla sua misura vera (508 px, 1:1) su ardesia, le tre letture scritte grandi."""
    testo = C(
        T('<p>WirTest</p>', style='kicker', color=SU_SCURO2),
        H('Il controllo dell’aggraffatura', 'h1', color=BIANCO, mt='s'),
        T('<p>Per sapere se un’aggraffatura è buona si misura la forza che tiene e si guarda la sezione. Wirmec costruisce '
          'i dinamometri per la prima e il laboratorio di micrografia per la seconda.</p>', style='lead', color=SU_SCURO2,
          max_w=(560, 640, 560), mt='m'),
        B("Richiedi un’offerta", richiesta('wirtest'), variant='primario', full_m=True, mt='l'),
        indice([('Strumenti', codici_link('wirtest', qui=True, codici=['W200', 'W100', 'W125']))], scuro=True, mt='xl'),
        w=(60.3, 100, 100), gap='0', pad=(0, 0, 0, (64, 0, 0)))
    letture = [('10 AWG', 'sezione del cavo'), ('2,57', 'altezza'), ('3,83', 'larghezza')]
    foto = C(
        I(img('sezione-10awg.jpg'), 'Sezione al micrografo di un’aggraffatura su cavo 10 AWG, altezza 2,57, larghezza 3,83',
          w_img=(508, 508, 350)),
        C(didascalia('Sezione di un’aggraffatura su cavo 10 AWG, mostrata alla sua misura. Foto della scheda W200.',
                     colore=SU_SCURO2), border_top=1, border_color=FILETTO_S, pad=('xs', 0, 0, 0), mt='s'),
        C(*[C(H(v, 'p', style='cifra', color=BIANCO), T(f'<p>{e}</p>', style='label', color=SU_SCURO3, mt='xs'),
              w=w, gap='0') for (v, e), w in zip(letture, [(40, 40, 38), (30, 30, 31), (30, 30, 31)])],
          dir='row', gap='0', mt='l'),
        didascalia('Le tre letture stampate sulla micrografia.', colore=SU_SCURO2, mt='s'),
        w=(39.7, 52.9, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(testo, foto, dir='row-reverse', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
                   bg=ARDESIA, pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-qual-apre wrm-scuro',
                   anchor='content', stile_extra=CSS_INDICE + CSS_SCURO)


def qualita_w200():
    """D2: la macchina che ha fatto la foto sopra, con la penna W202, e il percorso in tre passi."""
    passi = C(*[C(T(f'<p>{n:02d}</p>', style='dato_s', color=TESTO2), nome(p, mt='xxs'), w=(31, 31, 31), gap='0',
                  border_top=2, border_color=INK, pad=('xs', 0, 0, 0))
                for n, p in enumerate(['Taglio', 'Lucidatura', 'Fotografia'], 1)],
              dir='row', justify='between', gap='0', mt='l')
    sinistra = C(
        H('W200', 'h2', style='h1', color=INK),
        H('Laboratorio di micrografia', 'p', style='h3', color=TESTO2, mt='xs'),
        T('<p>Unità per l’analisi delle aggraffature. Taglio, lucidatura e fotografia si fanno sulla stessa apparecchiatura. '
          'Con l’ingranditore e un personal computer la sezione si fotografa e si ingrandisce fino a 200 volte; il '
          'software in dotazione permette di misurare sulle foto. Con un software opzionale le quote rilevate passano in '
          'un report generato in automatico.</p>', style='body', color=INK, mt='m'),
        passi,
        link_freccia('Il W200 in un video', 'https://www.youtube.com/watch?v=Ep2YVFejAtk', mt='l'),
        w=(50, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    destra = C(
        I(img('w200.jpg'), 'W200, laboratorio di micrografia', w_img=(640, 480, 350)),
        C(I(img('w202.jpg'), 'W202, la penna fornita con il W200', w_img=(300, 300, 280)),
          C(didascalia('W202, la penna fornita con il W200.'), border_top=1, border_color=FILETTO, pad=('xs', 0, 0, 0),
            mt='s', max_w=(300, 300, 280)),
          gap='0', mt='l'),
        w=(50, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align='start', gap='0'), css='wrm-w200', anchor='w200')


def qualita_dinamometri():
    """D3: la tabella dei dati del W100 con la macchina accanto; il W125 dichiarato per quello che è."""
    dati = [('Forza di trazione', f'0–1000{NB}N'), ('Precisione', f'±{NB}0,5 del fondo scala'), ('Unità di misura', 'N, kg'),
            ('Velocità di trazione', f'50{NB}mm/min'), ('Apertura morsa', f'0–10{NB}mm'), ('Connessione', 'RS232, RS485'),
            ('Test non distruttivo', 'sì'), ('Alimentazione', f'230{NB}V monofase'), ('Peso', f'16{NB}kg'),
            ('Dimensioni', f'225 x 470 x 245{NB}mm')]
    foto = C(C(I(img('w100.jpg'), 'W100, dinamometro motorizzato', w_img=(420, 420, 310), css='wrm-foto-c'),
               bg=BIANCO, pad=20, gap='0'),
             w=(41.67, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    testo = C(
        *titolo_h2('Dinamometri per la forza di tenuta'),
        T('<p>Il W100 è un dinamometro motorizzato per controllare la forza di tenuta dell’aggraffatura fino a 1000 N: '
          'compatto e facile da trasportare. Viene fornito con display alfanumerico a due decimali, memorizzazione del '
          'valore di picco, stampante con intestazione e logo dell’azienda, bloccaggio per terminali rollati, certificato '
          'di calibrazione e conformità CE.</p>', style='body', color=INK, mt='m'),
        H('W100', 'h3', style='nome', color=INK, mt='l'),
        dati_dl(dati, 'wrm-dl-forte wrm-dl-grigio', mt='xs'),
        C(H('W125', 'h3', style='nome', color=INK),
          T(f'<p>Dinamometro fino a 2500{NB}N. I dati tecnici non sono pubblicati: '
            f'<a href="{richiesta("wirtest", "W125")}">chiedili con il modulo</a>.</p>', style='body', color=INK,
            link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link', mt='xs'),
          gap='0', border_top=2, border_color=INK, pad=('s', 0, 0, 0), mt='l', anchor='w125'),
        w=(58.33, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(foto, testo, dir='row', dir_t='column', align='start', gap='0'), bg=GRIGIO, css='wrm-dinamo',
                   anchor='w100', stile_extra=CSS_W1500)


def qualita_terminale():
    """D4: il risultato del lavoro delle altre macchine, un terminale su un cavo sottile accanto al righello."""
    foto = C(I(img('righello.jpg'), 'Terminale aggraffato su cavo sottile accanto a un righello', w_img=(560, 480, 350)),
             C(didascalia('Foto della scheda AM210 futura.'), border_top=1, border_color=FILETTO, pad=('xs', 0, 0, 0),
               mt='s', max_w=(560, 480, 350)),
             w=(58.33, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    testo = C(
        *titolo_h2('Il terminale, da vicino'),
        T('<p>Un terminale aggraffato su un cavo sottile, accanto alle tacche di un righello. È la foto della scheda della '
          'AM210 futura, la taglia spela aggraffa Wirmec per cavi da 16 a 34 AWG.</p>', style='body', color=INK, mt='m'),
        link_freccia('AM210 futura', '/automatiche/#am210-futura', mt='l'),
        w=(41.67, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(foto, testo, dir='row', dir_t='column', align=('center', 'start', 'stretch'), gap='0'),
                   css='wrm-terminale', anchor='terminale')


def controllo_qualita():
    return [('apertura', qualita_apertura()), ('w200', qualita_w200()), ('dinamometri', qualita_dinamometri()),
            ('terminale', qualita_terminale()), ('richiesta', blocco_richiesta('wirtest'))]


# ---------------------------------------------------------------------------------------------
# 06 AZIENDA (specifica, paragrafo 11): niente foto della sede finché non ci sono, tipografia e dati
# ---------------------------------------------------------------------------------------------
def azienda_apertura():
    """E1: a sinistra il testo, a destra i dati del Registro delle Imprese in mono, come su una scheda tecnica."""
    dati = [('Ragione sociale', 'Wirmec S.r.l.'), ('Sede', f'{INDIRIZZO}, {CITTA}'), ('Iscrizione', '02/05/2010'),
            ('REA', REA), ('P.IVA e C.F.', PIVA), ('Capitale sociale', CAPITALE), ('Attività', 'ATECO 28.99.2'),
            ('Addetti', '28 (2025)')]
    sinistra = C(
        T('<p>Wirmec S.r.l., Ponte San Nicolò (PD)</p>', style='kicker', color=TESTO2),
        H('Macchine e attrezzature per il cablaggio, dal 2010', 'h1', color=INK, mt='s', max_w=(640, 760, 560)),
        T('<p>Wirmec progetta e costruisce macchine e attrezzature per il cablaggio elettrotecnico ed elettronico: '
          'applicatori, presse e spela aggraffa da banco, taglia spela aggraffa automatiche e strumenti per il controllo '
          'dell’aggraffatura.</p>', style='lead', color=INK, max_w=(640, 760, 560), mt='m'),
        T('<p>È iscritta al Registro delle Imprese dal 2 maggio 2010 ed è nata dall’esperienza trentennale delle sue persone '
          'nella fornitura di attrezzature per il cablaggio.</p>'
          '<p>In Italia vende con tre referenti di zona, all’estero con nove distributori. I clienti sono le aziende che '
          f'producono cablaggi: gli harness makers del suo payoff, “{PAYOFF}”.</p>', style='body', color=INK,
          max_w=(640, 760, 560), mt='m'),
        C(link_freccia('Le macchine automatiche', '/automatiche/', fisso=True),
          link_freccia('Contatti e referenti', '/contatti/#italia', fisso=True),
          dir='row', dir_m='column', wrap=True, gap=(32, 32, 12), mt='l'),
        w=(58.33, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    destra = C(
        T('<p>Wirmec in breve</p>', style='label', color=INK),
        dati_dl(dati, 'wrm-dl-forte wrm-dl-reg', mt='xs'),
        didascalia('Registro delle Imprese, tramite aziende.it e companyreports.it, ottobre 2026.', mt='s'),
        w=(41.67, 100, 100), gap='0', mt=(0, 'xl', 'xl'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align='start', gap='0'),
                   pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-az-apre', anchor='content')


LINEE_TUTTE = [
    ('WirTool', 'Applicatori', 'Applicatori per l’aggraffatura side feed ed end feed, con movimentazione meccanica e '
                               'pneumatica.', 'wirtool', '/applicatori/'),
    ('WirPress', 'Semiautomatiche da banco', 'Aggraffatrici da banco da 20, 25 e 30 kN e spela aggraffa, dalla '
                                             'elettropneumatica alla elettronica con inseritore di gommino.',
     ('presse', 'spela'), '/da-banco/'),
    ('WirStrip', 'Taglio e sguainatura', 'Troncatrice e sguainatrici da banco per cavi unipolari e multipolari, anche di '
                                         'grosso diametro.', 'wirstrip', '/da-banco/#wirstrip'),
    ('WirAM', 'Taglia spela aggraffa automatiche', 'Tagliano, spelano e aggraffano il cavo con fino a sei stazioni di '
                                                   'lavorazione.', 'wiram', '/automatiche/'),
    ('Accessori', 'Unità per le automatiche', 'Aggraffatrici, inseritori di gommino e coprifaston, unità di stagnatura, '
                                              'attorcigliatura, doppiatura e spelatura coassiale.', 'accessori',
     '/automatiche/#accessori'),
    ('WirTest', 'Controllo dell’aggraffatura', 'Dinamometri per la forza di tenuta e laboratorio di micrografia per la '
                                               'sezione.', 'wirtest', '/controllo-qualita/'),
]


def azienda_linee():
    """E2: l'indice completo del catalogo, per ogni linea il nome grande, cosa fa e tutti i codici (Salvagnini)."""
    righe = []
    for nm, sotto, desc, gruppo, url in LINEE_TUTTE:
        gruppi = gruppo if isinstance(gruppo, tuple) else (gruppo,)
        codici = [x for g in gruppi for x in codici_link(g)]
        links = ''.join(f'<a href="{u}">{unito(c)}</a>' for c, u in codici)
        righe.append(C(
            C(H(nm, 'h3', color=INK, link=url, css='wrm-linea-t'),
              T(f'<p>{sotto}</p>', style='small', color=TESTO2, mt='xxs'),
              w=(25, 30, 100), gap='0', pad=(0, (24, 24, 0), 0, 0)),
            C(T(f'<p>{desc}</p>', style='small', color=INK, w=(46.67, 100, 100)),
              C(T(f'<p>{links}</p>', style='dato_s', color=INK, link_color=INK, link_hover=ROSSO_SCURO, sottolinea=False,
                  css='wrm-indice-c'), w=(53.33, 100, 100), gap='0', mt=(0, 's', 's')),
              dir='row', dir_t='column', gap='0', w=(75, 70, 100), mt=(0, 0, 's'), css='wrm-linea-r'),
            dir='row', dir_m='column', gap='0', pad=(28, 0, 28, 0), border_bottom=1, border_color=FILETTO_G))
    return sezione(
        testa('Sei linee, 42 macchine e unità', 'Ogni codice porta alla sua scheda: descrizione, dati tecnici e brochure '
                                                'dove c’è.', stile_lead='body'),
        C(*righe, gap='0', border_top=2, border_color=INK, mt='xl'),
        bg=GRIGIO, css='wrm-az-linee', anchor='linee',
        stile_extra=CSS_INDICE + '@media (min-width:1025px){.wrm-linea-r>.wrm-w:first-child,.wrm-linea-r>.elementor-widget:first-child'
                                 '{padding-right:32px}}'
                    f'.wrm-linea-t a:hover,.wrm-linea-t a:focus-visible,.wrm-linea-t .elementor-heading-title a:hover'
                    f'{{color:{ROSSO_SCURO}!important}}')


DISTRIBUTORI = [
    ('AAC Kabelbearbeitungssysteme', 'Germania', 'Heiligenhaus', 'AAC Kabelbearbeitungssysteme GmbH',
     'Hauptstraße 262, 42579 Heiligenhaus'),
    ('Wiretech', 'Repubblica Ceca', 'Brno', 'Wiretech s.r.o.', 'Cacovická 47, 614 00 Brno'),
    ('Calotec', 'Svezia e paesi nordici', 'Vänersborg', 'Calotec AB', 'Östra vägen 1 E, 462 32 Vänersborg, Svezia'),
    ('CST Automation', 'Regno Unito', 'Failsworth, Manchester', 'CST Automation',
     'Unit 14, Crown Business Centre, George Street, Failsworth, Manchester M35 9BW'),
    ('Epix', 'Spagna', 'Sant Joan Despí, Barcellona', 'EPIX Alta Tecnología para el Cableado',
     'Rambla Jujol 51, local 1, 08970 Sant Joan Despí (Barcellona)'),
    ('Wireflex', 'Ungheria', 'Budapest', 'Wireflex Kft.', 'Takács S. u. 14, 1174 Budapest'),
    ('Wirelease', 'Francia', 'Châtenay-Malabry', 'Wirelease', '23 rue Léon Martine, 92290 Châtenay-Malabry'),
    ('Saff Makine', 'Turchia', 'Istanbul', 'Saff Makine San. Dış Tic. Ltd. Şti.',
     'Beylikdüzü O.S.B. Birlik Sanayi Sitesi, Istanbul'),
    ('Wire Solutions', 'Polonia', 'Breslavia', 'Wire Solutions', 'ul. Opatowicka 16, 52-028 Breslavia'),
]
PAESI_SCHEDA = {'Calotec': 'Svezia, Norvegia, Finlandia, Danimarca, Paesi Baltici'}

CSS_CERCHIO = (
    f'.wrm-cerchio p{{display:flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:50%;'
    f'background:{ARDESIA};color:{BIANCO};font:500 11px/1 {F_MONO};margin:0}}'
)


def azienda_distributori():
    """E3: un filo per ogni distributore, da Ponte San Nicolò alla sua città (Zünd, LEMO), accanto l'elenco numerato."""
    alt = 'Mappa d’Europa con i nove distributori Wirmec collegati a Ponte San Nicolò'
    mappa = C(I(img('europa-desktop.png'), alt, hide=['tablet', 'mobile']),
              I(img('europa-mobile.png'), alt, hide=['desktop']),
              didascalia('Confini: Natural Earth. Città: OpenStreetMap.', mt='s'),
              w=(58, 50, 100), gap='0')
    righe = [C(T(f'<p>{n}</p>', style='dato_s', color=BIANCO, css='wrm-cerchio', fisso=True),
               C(nome(nm, livello='p', style='nome_s'), T(f'<p>{paese} · {citta}</p>', style='small', color=TESTO2, mt=2),
                 gap='0', grow=True),
               dir='row', align='start', gap=12, pad=(12, 0, 12, 0), border_bottom=1, border_color=FILETTO)
             for n, (nm, paese, citta, _, _) in enumerate(DISTRIBUTORI, 1)]
    elenco = C(C(*righe, gap='0', border_top=2, border_color=INK),
               link_freccia('Indirizzi completi', '/contatti/#estero', mt='m'),
               w=(42, 50, 100), gap='0', pad=(0, 0, 0, (48, 32, 0)), mt=(0, 0, 'l'))
    return sezione(
        testa('Nove distributori, da Manchester a Istanbul',
              'All’estero le macchine Wirmec si comprano dai distributori locali. Calotec segue anche Norvegia, Finlandia, '
              'Danimarca e Paesi Baltici.', stile_lead='body'),
        C(mappa, elenco, dir='row', dir_m='column', align='start', gap='0', mt='xl'),
        css='wrm-az-distr', anchor='distributori', stile_extra=CSS_CERCHIO)


def azienda_brevetti():
    """E4: righe "codice, fatto, fonte", come un registro: quello che l'azienda dichiara nelle sue schede."""
    voci = [('WSC 21', '/da-banco/#wsc-21', 'Due brevetti: il movimento elettronico della testa di sezione e spelatura, e '
                                            'la protezione della pinza.', 'Scheda WSC 21', None),
            ('AM600 Vantage', '/automatiche/#am600-vantage', 'Il sistema a doppio cavo brevettato, per lavorare due cavi '
                                                            'diversi sulla stessa macchina.', 'Scheda AM600 Vantage',
             ('am600-doppio-cavo.jpg', 'AM600 Vantage, il gruppo del doppio cavo', 200)),
            ('WSC 31', '/da-banco/#wsc-31', 'L’unità elettronica di inserimento del gommino, con sistema brevettato.',
             'Scheda WSC 31', ('wsc31.jpg', 'WSC 31, spela aggraffa con inseritore di gommino', 193)),
            ('WSC 15', '/da-banco/#wsc-15', 'Cavi unipolari e multipolari lunghi fino a 20 mm, con il sistema brevettato '
                                            'della protezione.', 'Scheda WSC 15',
             ('wsc15.jpg', 'WSC 15, spela aggraffa elettropneumatica', 200))]
    righe = []
    for cod, url, fatto, fonte, foto in voci:
        righe.append(C(
            T(f'<p><a href="{url}">{unito(cod)}</a></p>', style='dato', color=INK, link_color=INK, link_hover=ROSSO_SCURO,
              css='wrm-link', w=(15, 15, 100)),
            C(T(f'<p>{fatto}</p>', style='body', color=INK), didascalia(fonte, mt='xs'), w=(60, 55, 100), gap='0',
              pad=(0, (32, 32, 0), 0, (0, 0, 0)), mt=(0, 0, 'xs')),
            C(*([I(img(foto[0]), foto[1], w_img=(foto[2], foto[2], foto[2]))] if foto else []), w=(25, 30, 100), gap='0',
              mt=(0, 0, 's' if foto else 0), hide=[] if foto else ['mobile']),
            dir='row', dir_m='column', gap='0', pad=(24, 0, 24, 0), border_bottom=1, border_color=FILETTO_G))
    return sezione(
        *titolo_h2('Brevetti dichiarati'),
        C(*righe, gap='0', border_top=2, border_color=INK, mt='xl'),
        didascalia('I numeri dei brevetti si aggiungono quando Wirmec li conferma.', mt='s'),
        bg=GRIGIO, css='wrm-az-brevetti', anchor='brevetti')


def azienda():
    return [('apertura', azienda_apertura()), ('linee', azienda_linee()), ('distributori', azienda_distributori()),
            ('brevetti', azienda_brevetti()), ('richiesta', blocco_richiesta(''))]


# ---------------------------------------------------------------------------------------------
# 07 CONTATTI (specifica, paragrafo 12): la pagina è la richiesta
# ---------------------------------------------------------------------------------------------
CF7 = '[contact-form-7 title="Richiesta offerta"]'
CORPO_MAIL = ('Nome e cognome:\nAzienda:\nTelefono:\nProvincia o paese:\nLinea e modello:\n'
              'Terminale e cavo (codice, sezione):\nQuantità o volumi:\nMessaggio:\n')

STILE_CF7 = (
    '.wrm-modulo .wpcf7 p{margin:0}.wrm-modulo .wpcf7 br{display:none}'
    '.wrm-campi{display:grid;grid-template-columns:1fr 1fr;gap:20px}'
    '.wrm-campi .wrm-largo{grid-column:1/-1}'
    '@media (max-width:767px){.wrm-campi{grid-template-columns:100%}}'
    f".wrm-modulo .wpcf7 label{{display:block;margin:0;font:500 13px/1.3 {F_SANS};color:{INK}}}"
    '.wrm-modulo .wpcf7-form-control-wrap{display:block;margin-top:6px}'
    '.wrm-modulo input[type=text],.wrm-modulo input[type=email],.wrm-modulo input[type=tel],.wrm-modulo select,'
    f'.wrm-modulo textarea{{display:block;width:100%;height:48px;box-sizing:border-box;margin:0;background:{BIANCO};'
    f'border:1px solid {TESTO2}!important;border-radius:0!important;box-shadow:none;padding:0 14px!important;'
    f'font:400 17px/1.4 {F_SANS};color:{INK}}}'
    '.wrm-modulo textarea{height:140px;padding:12px 14px!important;resize:vertical}'
    f'.wrm-modulo input[type=file]{{font:400 15px/1.4 {F_SANS};color:{INK};padding:8px 0}}'
    f'.wrm-modulo ::placeholder{{color:{TESTO2};opacity:1}}'
    f'.wrm-modulo input:focus,.wrm-modulo select:focus,.wrm-modulo textarea:focus{{border:2px solid {INK}!important;'
    f'outline:2px solid {ROSSO};outline-offset:2px}}'
    f'.wrm-modulo .wpcf7-not-valid{{border-color:{ROSSO_SCURO}!important}}'
    f'.wrm-modulo .wpcf7-not-valid-tip{{color:{ROSSO_SCURO};font:400 13px/1.45 {F_SANS};margin-top:6px}}'
    '.wrm-modulo .wpcf7-acceptance .wpcf7-list-item{margin:0}'
    f'.wrm-modulo .wpcf7-acceptance label{{display:flex;gap:10px;align-items:flex-start;font:400 15px/1.55 {F_SANS}}}'
    f'.wrm-modulo .wpcf7-acceptance input{{accent-color:{INK};width:20px;height:20px;flex:0 0 20px;margin:2px 0 0}}'
    f'.wrm-modulo .wpcf7-acceptance a{{color:{ROSSO_SCURO};text-decoration:underline}}'
    f'.wrm-modulo input[type=submit]{{background:{ROSSO};color:{BIANCO};border:2px solid {ROSSO};border-radius:0;'
    f'padding:16px 26px;font:600 16px/1.2 {F_SANS};cursor:pointer;transition:background-color .15s,border-color .15s}}'
    f'.wrm-modulo input[type=submit]:hover,.wrm-modulo input[type=submit]:focus-visible{{background:{ROSSO_SCURO};'
    f'border-color:{ROSSO_SCURO};color:{BIANCO}}}'
    f'.wrm-modulo input[type=submit]:disabled{{background:{FILETTO_G};border-color:{FILETTO_G};color:{INK};cursor:default}}'
    f'.wrm-modulo .wrm-nota{{font:400 13px/1.45 {F_SANS};color:{TESTO2}}}'
    '.wrm-modulo .wpcf7-spinner{margin:0 0 0 16px}'
    f'.wrm-modulo .wpcf7 form .wpcf7-response-output{{margin:20px 0 0;padding:14px 16px;border:1px solid {INK};'
    f'font:400 15px/1.5 {F_SANS};color:{INK};background:{BIANCO}}}'
    '@media (max-width:767px){.wrm-modulo input[type=submit]{width:100%}}'
    '@media (prefers-reduced-motion:reduce){.wrm-modulo input[type=submit]{transition:none}}'
)


def contatti_richiesta():
    """F1: il telefono della sede grande e il modulo subito, nella prima schermata (TRUMPF)."""
    def riga(et, html):
        return C(T(f'<p>{et}</p>', style='label', color=TESTO2, w_px=(96, 96, None), fisso=True),
                 T(f'<p>{html}</p>', style='body', color=INK, link_color=ROSSO_SCURO, link_hover=INK, css='wrm-link',
                   grow=True),
                 dir='row', dir_m='column', align=('baseline', 'baseline', 'start'), gap=('s', 's', 2),
                 pad=(12, 0, 12, 0), border_bottom=1, border_color=FILETTO)
    sinistra = C(
        T('<p>Contatti</p>', style='kicker', color=TESTO2),
        H("Richiedi un’offerta", 'h1', color=INK, mt='s'),
        T('<p>Scrivi il modello che ti interessa, oppure il terminale e il cavo da lavorare. La richiesta non è '
          'impegnativa.</p>', style='lead', color=INK, max_w=(480, 640, 560), mt='m'),
        H(TEL, 'p', style='tel', color=INK, link=TEL_LINK, mt='l', css='wrm-tel-g'),
        C(riga('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'), riga('Fax', FAX), riga('PEC', PEC),
          riga('Sede', f'{INDIRIZZO}, {CITTA}<br><a href="#come-arrivare">Come arrivare&nbsp;↓</a>'),
          gap='0', border_top=1, border_color=FILETTO, mt='m'),
        w=(41.67, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    alternativa = (
        f'<p style="margin:0 0 24px">Scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a> con il modello, oppure il terminale e il '
        'cavo da lavorare.</p>'
        f'<p style="margin:0"><a href="{mailto("Richiesta offerta dal sito", CORPO_MAIL)}" style="display:inline-block;'
        f'background:{ROSSO};color:{BIANCO};border:2px solid {ROSSO};padding:16px 26px;font:600 16px/1.2 {F_SANS};'
        'text-decoration:none">Scrivi la richiesta</a></p>')
    modulo = C(SHORTCODE(CF7, alternativa_html=alternativa, stile='body', colore=INK),
               RAW('', css=STILE_CF7, solo_elementor=True),
               bg=GRIGIO, pad=(40, 32, 20), gap='0', css='wrm-modulo')
    destra = C(modulo, w=(58.33, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align='start', gap='0'),
                   pad=((72, 56, 40), 'lato', 'sezione', 'lato'), css='wrm-ct-richiesta', anchor='richiesta',
                   stile_extra=f'.wrm-modulo a[href^="mailto:{EMAIL}?"]:hover,.wrm-modulo a[href^="mailto:{EMAIL}?"]:focus-visible'
                               f'{{background:{ROSSO_SCURO}!important;border-color:{ROSSO_SCURO}!important;color:{BIANCO}!important}}')


REGIONI = {'Abruzzo': 'resto', 'Basilicata': 'resto', 'Calabria': 'resto', 'Campania': 'resto',
           'Emilia-Romagna': 'nordest', 'Friuli-Venezia Giulia': 'nordest', 'Lazio': 'resto', 'Liguria': 'nordovest',
           'Lombardia': 'nordovest', 'Marche': 'resto', 'Molise': 'resto', 'Piemonte': 'nordovest', 'Puglia': 'resto',
           'Sardegna': 'resto', 'Sicilia': 'resto', 'Toscana': 'resto', 'Trentino-Alto Adige': 'nordest',
           'Umbria': 'resto', 'Valle d’Aosta': 'resto', 'Veneto': 'nordest'}
ZONE = [
    ('nordovest', 'Gianluca Corio', 'Lombardia, Piemonte, Liguria', '+39 347 980 0747', 'tel:+393479800747', ''),
    ('nordest', 'Gianluca Trivellato', 'Triveneto ed Emilia-Romagna', '+39 347 798 6503', 'tel:+393477986503', ''),
    ('resto', 'Marco Di Martino', 'Tutte le altre regioni: Valle d’Aosta, centro, sud e isole', '+39 347 433 1068',
     'tel:+393474331068', 'mdimartino@wirmec.com'),
]


def _italia():
    """Le piccole Italie in linea (niente immagini da caricare): un solo set di tracciati delle regioni, riusato con
    <use> nelle tre mappe, con le regioni della zona in ardesia. Tracciati: ISTAT, tramite openpolis (CC BY)."""
    import os
    import re
    cartella = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'web')
    zone = {}
    tracciati = None
    for z in ('nordovest', 'nordest', 'resto'):
        svg = open(os.path.join(cartella, f'italia-{z}.svg'), encoding='utf-8').read()
        pz = re.findall(r'<path d="([0-9MLZmlz. \-]+)" fill="(#[0-9A-Fa-f]{6})"', svg)
        tracciati = [d for d, _ in pz]
        zone[z] = [i for i, (_, f) in enumerate(pz) if f.upper() == ARDESIA]
    defs = ''.join(f'<path id="wrm-it-{i}" d="{d}"/>' for i, d in enumerate(tracciati))
    return defs, zone, len(tracciati)


CSS_ZONE = (
    f'.wrm-zone-cerca{{background:{BIANCO};padding:24px}}'
    '.wrm-zone-cerca[hidden]{display:none!important}'
    f'.wrm-zone-cerca label{{display:block;margin:0 0 12px;font:600 22px/1.2 {F_COND};color:{INK}}}'
    '.wrm-zone-sel{position:relative}'
    f'.wrm-zone-sel select{{appearance:none;-webkit-appearance:none;display:block;width:100%;height:52px;margin:0;'
    f'padding:0 48px 0 16px!important;font:400 17px/1.2 {F_SANS};color:{INK};background:{BIANCO}!important;'
    f'border:1px solid {TESTO2}!important;border-radius:0!important;box-shadow:none;cursor:pointer}}'
    f'.wrm-zone-sel select:focus{{border:2px solid {INK}!important;outline:2px solid {ROSSO};outline-offset:2px}}'
    f'.wrm-zone-sel::after{{content:"";position:absolute;right:20px;top:50%;width:9px;height:9px;border-right:2px solid {INK};'
    f'border-bottom:2px solid {INK};transform:translateY(-70%) rotate(45deg);pointer-events:none}}'
    f'.wrm-zone-esito{{margin:12px 0 0!important;font:400 16px/1.5 {F_SANS};color:{INK}}}'
    '.wrm-zone-esito:empty{display:none}'
    f'.wrm-zone-esito a{{color:{ROSSO_SCURO};font-weight:600;white-space:nowrap;text-decoration:underline;text-underline-offset:4px}}'
    f'.wrm-zone-righe{{list-style:none;margin:0!important;padding:0!important;border-top:2px solid {INK}}}'
    f'.wrm-ref{{display:grid;grid-template-columns:96px 1fr auto;gap:24px;align-items:center;margin:0;padding:24px 16px;'
    f'border-bottom:1px solid {FILETTO_G};transition:background-color .15s}}'
    f'.wrm-ref[data-scelto]{{background:#F2F3F4;box-shadow:inset 0 2px 0 {INK}}}'
    '.wrm-ref svg{display:block;width:96px;height:auto}'
    f'.wrm-ref h3{{margin:0!important;font:600 28px/1.15 {F_COND};color:{INK}}}'
    f'.wrm-ref-ruolo{{margin:4px 0 0!important;font:400 15px/1.55 {F_SANS};color:{ROSSO_SCURO}}}'
    f'.wrm-ref-reg{{margin:2px 0 0!important;font:400 15px/1.55 {F_SANS};color:{TESTO2}}}'
    '.wrm-ref-tel{display:flex;flex-direction:column;align-items:flex-end;gap:4px;text-align:right}'
    f'.wrm-ref-tel small{{font:500 13px/1.3 {F_SANS};color:{TESTO2}}}'
    f'.wrm-ref-tel a{{font:500 17px/1.3 {F_MONO};color:{INK};white-space:nowrap;text-decoration:none;'
    f'border-bottom:1px solid {FILETTO_G}}}'
    f'.wrm-ref-tel a:hover,.wrm-ref-tel a:focus-visible{{color:{ROSSO_SCURO};border-bottom-color:{ROSSO_SCURO}}}'
    '.wrm-ref-tel a.wrm-ref-mail{font-size:14px}'
    '@media (max-width:1024px){.wrm-ref h3{font-size:26px}}'
    '@media (max-width:767px){.wrm-ref{grid-template-columns:72px 1fr;gap:16px;padding:20px 12px}.wrm-ref svg{width:72px}'
    '.wrm-ref-tel{grid-column:2;align-items:flex-start;text-align:left}.wrm-ref h3{font-size:24px}'
    '.wrm-zone-cerca{padding:16px}.wrm-ref-tel a{font-size:16px}}'
    '@media (prefers-reduced-motion:reduce){.wrm-ref{transition:none}}'
)

JS_ZONE = (
    "(function(){function go(){var s=document.getElementById('wrm-regione');if(!s)return;"
    "var box=s.closest('.wrm-zone-cerca'),esito=box.querySelector('.wrm-zone-esito'),"
    "righe=document.querySelectorAll('.wrm-ref');box.hidden=false;"
    "s.addEventListener('change',function(){var z=s.value,r=null;"
    "righe.forEach(function(li){if(li.getAttribute('data-zona')===z){li.setAttribute('data-scelto','');r=li}"
    "else{li.removeAttribute('data-scelto')}});esito.textContent='';if(!r)return;"
    "var t=r.getAttribute('data-tel');esito.appendChild(document.createTextNode(s.options[s.selectedIndex].text+"
    "': ti segue '+r.getAttribute('data-nome')+', '));var a=document.createElement('a');"
    "a.href='tel:'+t.replace(/\\s/g,'');a.textContent=t.replace(/ /g,'\\u00a0');esito.appendChild(a)})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();"
)


def contatti_italia():
    """F2: scegli la tua regione e la riga del referente si evidenzia; ogni riga ha la sua piccola Italia (Hermle)."""
    defs, zone, n = _italia()
    opzioni = ''.join(f'<option value="{z}">{r}</option>' for r, z in REGIONI.items())
    selettore = ('<div class="wrm-zone-cerca" hidden><label for="wrm-regione">In che regione lavori?</label>'
                 f'<div class="wrm-zone-sel"><select id="wrm-regione"><option value="">Scegli la regione</option>{opzioni}'
                 '</select></div><p class="wrm-zone-esito" aria-live="polite"></p></div>')
    righe = ''
    for z, nm, reg, tel, link, mail in ZONE:
        usi = ''.join(f'<use href="#wrm-it-{i}" fill="{ARDESIA if i in zone[z] else "#D5D9DC"}"/>' for i in range(n))
        mappa = (f'<svg viewBox="0 0 240 283" aria-hidden="true" focusable="false"><g stroke="#FFFFFF" stroke-width="0.9" '
                 f'stroke-linejoin="round">{usi}</g><circle cx="106.6" cy="50.5" r="5" fill="{ROSSO}" stroke="#FFFFFF" '
                 'stroke-width="1.6"/></svg>')
        posta = f'<a class="wrm-ref-mail" href="mailto:{mail}">{mail}</a>' if mail else ''
        righe += (f'<li class="wrm-ref" data-zona="{z}" data-nome="{nm}" data-tel="{tel}">{mappa}<div><h3>{nm}</h3>'
                  f'<p class="wrm-ref-ruolo">Responsabile vendite</p><p class="wrm-ref-reg">{reg}</p></div>'
                  f'<div class="wrm-ref-tel"><small>Cellulare</small><a href="{link}">{tel.replace(" ", NB)}</a>{posta}</div></li>')
    elenco = (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>{defs}</defs>'
              f'</svg><ul class="wrm-zone-righe">{righe}</ul><script>{JS_ZONE}</script>')
    sinistra = C(
        *titolo_h2('In Italia, un referente per zona'),
        T('<p>Per un’offerta chiama il referente della tua regione, oppure la sede.</p>', style='body', color=INK, mt='m'),
        RAW(selettore, css=CSS_ZONE, mt='l'),
        w=(41.67, 100, 100), gap='0', pad=(0, (48, 0, 0), 0, 0))
    destra = C(RAW(elenco), didascalia('Regioni: ISTAT, tramite openpolis, CC BY.', mt='s'),
               w=(58.33, 100, 100), gap='0', mt=(0, 'xl', 'l'))
    return sezione(C(sinistra, destra, dir='row', dir_t='column', align='start', gap='0'), bg=GRIGIO,
                   css='wrm-ct-italia', anchor='italia')


def contatti_estero():
    """F3: gli indirizzi completi dei nove distributori, in griglia, come una rubrica (Zünd)."""
    schede = [C(T(f'<p>{PAESI_SCHEDA.get(breve, paese)}</p>', style='label', color=TESTO2),
                nome(ragione, mt='xs'),
                T(f'<p>{indirizzo}</p>', style='small', color=INK, mt='xxs'),
                w=(31.33, 48.5, 100), gap='0', border_top=2, border_color=INK, pad=(20, 0, 28, 0))
              for breve, paese, _, ragione, indirizzo in DISTRIBUTORI]
    return sezione(
        testa('All’estero, nove distributori', 'Fuori dall’Italia le macchine Wirmec si comprano dal distributore del tuo '
                                               'paese. Per i paesi che non sono in elenco scrivi alla sede.',
              stile_lead='body'),
        C(*schede, dir='row', wrap=True, justify='between', gap='0', gap_r=(24, 16, 8), mt='xl', css='wrm-rubrica'),
        css='wrm-ct-estero', anchor='estero',
        stile_extra='@media (min-width:1025px){.wrm-rubrica::after{content:"";width:31.33%}}')


def contatti_arrivare():
    """F4: la mappa della zona disegnata dai dati OpenStreetMap, il filo dal punto della sede al nome (LEMO)."""
    alt = ('Mappa della zona di Ponte San Nicolò con la sede Wirmec in Viale Europa 16, l’A4, l’A13 e il casello Padova '
           'Zona Industriale')
    mappa = C(I(img('mappa-sede-desktop.png'), alt, hide=['tablet', 'mobile']),
              I(img('mappa-sede-mobile.png'), alt, hide=['desktop']),
              w=(58.33, 50, 100), gap='0')
    gmaps = ('https://www.google.com/maps/search/?api=1&amp;query=Viale%20Europa%2016%2C%2035020%20Ponte%20San%20Nicol%C3%B2')
    osm = 'https://www.openstreetmap.org/?mlat=45.35601&amp;mlon=11.93173#map=15/45.35601/11.93173'
    testo = C(
        C(filetto_rosso(24), T('<p>45°21′22″ N · 11°55′54″ E</p>', style='dato_s', color=SU_SCURO2),
          dir='row', align='center', gap=12),
        H(f'{INDIRIZZO}, Ponte San Nicolò', 'h2', color=BIANCO, mt='s'),
        T('<p>Nel comune di Ponte San Nicolò, a sud-est di Padova. Dall’autostrada si esce a Padova Zona Industriale, '
          'sull’A13.</p>', style='body', color=SU_SCURO2, mt='m'),
        dati_dl([('Casello A13 Padova Zona Industriale', f'6,9{NB}km'), ('Stazione di Padova', f'10,5{NB}km'),
                 ('Centro di Padova, in linea d’aria', f'7,3{NB}km')], 'wrm-dl-scuro', colore_et=SU_SCURO2, stile='small',
                mt='l'),
        dati_dl([('Telefono', f'<a href="{TEL_LINK}">{TEL}</a>'), ('Fax', FAX),
                 ('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>')], 'wrm-dl-scuro', colore_et=SU_SCURO3, mt='m'),
        C(link_freccia('Apri in Google Maps', gmaps, scuro=True, fisso=True),
          link_freccia('Apri in OpenStreetMap', osm, scuro=True, fisso=True),
          dir='row', dir_m='column', wrap=True, gap=(32, 32, 12), mt='l'),
        didascalia('Distanze su strada (OSRM) e in linea d’aria calcolate su OpenStreetMap, ottobre 2026. Mappa disegnata '
                   'da dati © OpenStreetMap contributors, ODbL. Il punto è quello della via: il civico non è mappato.',
                   colore=SU_SCURO3, mt='l'),
        w=(41.67, 50, 100), gap='0', pad=(('sezione', 'sezione', 'sezione'), (0, 32, 20), ('sezione', 'sezione', 'l'),
                                           (64, 32, 20)), css='wrm-arr-testo')
    return sezione(C(mappa, testo, dir='row', dir_m='column-reverse', align='center', gap='0'), bg=ARDESIA, pad=0,
                   boxed=False, css='wrm-ct-arrivare wrm-scuro', anchor='come-arrivare',
                   stile_extra=CSS_SCURO + '@media (min-width:1025px){.wrm-arr-testo{padding-right:max(48px,calc((100% - 1280px) / 2))!important}}'
                               f'.wrm-dl-scuro dd a{{text-decoration:none!important}}'
                               f'.wrm-dl-scuro dd a:hover,.wrm-dl-scuro dd a:focus-visible{{text-decoration:underline!important;'
                               'text-underline-offset:4px}')


def contatti():
    return [('richiesta', contatti_richiesta()), ('italia', contatti_italia()), ('estero', contatti_estero()),
            ('come-arrivare', contatti_arrivare())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Wirmec, macchine per tagliare, spelare e aggraffare il cavo',
     'descrizione': 'Applicatori, presse da banco, spela aggraffa e taglia spela aggraffa automatiche fino a 6 stazioni. '
                    'Wirmec, Ponte San Nicolò (Padova).'},
    {'slug': '02-automatiche', 'titolo': 'Automatiche', 'sezioni': automatiche,
     'titolo_seo': 'Taglia spela aggraffa automatiche WirAM e accessori, Wirmec',
     'descrizione': 'Sette WirAM, dalla AM210 futura per cavi fino a 34 AWG alla AM600 Vantage a doppio cavo, e le unità '
                    'per equipaggiarle.'},
    {'slug': '03-da-banco', 'titolo': 'Da banco', 'sezioni': da_banco,
     'titolo_seo': 'Presse da banco e spela aggraffa WirPress, WirStrip, Wirmec',
     'descrizione': 'Aggraffatrici da banco da 20, 25 e 30 kN, spela aggraffa WSC e troncatrici e sguainatrici WirStrip. '
                    'Dati tecnici e brochure.'},
    {'slug': '04-applicatori', 'titolo': 'Applicatori', 'sezioni': applicatori,
     'titolo_seo': 'Applicatori WirTool side feed ed end feed, Wirmec',
     'descrizione': 'Dieci applicatori per terminali side feed, end feed, ferrules, splice, contatti torniti e bus bar. '
                    'Dati e foto.'},
    {'slug': '05-controllo-qualita', 'titolo': 'Controllo qualità', 'sezioni': controllo_qualita,
     'titolo_seo': 'Controllo dell’aggraffatura WirTest: micrografia e dinamometri',
     'descrizione': 'Laboratorio di micrografia W200 e dinamometri W100 e W125 per controllare sezione e forza di tenuta '
                    'dell’aggraffatura.'},
    {'slug': '06-azienda', 'titolo': 'Azienda', 'sezioni': azienda,
     'titolo_seo': 'Wirmec S.r.l., Ponte San Nicolò (Padova)',
     'descrizione': 'Chi è Wirmec, le sei linee con tutti i codici, i nove distributori in Europa, i brevetti dichiarati e i '
                    'dati societari.'},
    {'slug': '07-contatti', 'titolo': 'Contatti', 'sezioni': contatti,
     'titolo_seo': 'Contatti e richiesta di offerta, Wirmec',
     'descrizione': 'Telefono, email, referenti per regione, distributori all’estero e come arrivare in Viale Europa 16 a '
                    'Ponte San Nicolò.'},
]
