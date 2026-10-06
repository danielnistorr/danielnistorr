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
from motore import C, H, T, B, I, LINEA_H, RAW, MENU

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


def testa(titolo, lead, colore=INK, colore_lead=TESTO2):
    """Testa di sezione: H2 con filetto a sinistra, lead a destra allineato in basso; su tablet e telefono in colonna."""
    return C(C(*titolo_h2(titolo, colore), w=(50, 100, 100)),
             C(T(f'<p>{lead}</p>', style='lead', color=colore_lead, max_w=(560, 760, 560)), w=(50, 100, 100),
               mt=(0, 'm', 'm')),
             dir='row', dir_t='column', align=('end', 'start', 'start'), gap='0')


def dati_dl(coppie, varianti='', colore_et=TESTO2, **p):
    """Righe di dati: <dl> con etichetta (label) e valore (Plex Mono). varianti: 'wrm-dl-forte', 'wrm-dl-grigio'."""
    righe = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in coppie)
    return T(f'<dl>{righe}</dl>', style='label', color=colore_et, css=f'wrm-dl {varianti}'.strip(), **p)


def nome(testo, colore=INK, livello='p', **p):
    """Nome o codice di un modello (stile `nome`); dentro un contenitore-link cambia colore in hover."""
    classi = ('wrm-nome ' + p.pop('css', '')).strip()
    return H(testo, livello, style='nome', color=colore, css=classi, **p)


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


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Wirmec, macchine per tagliare, spelare e aggraffare il cavo',
     'descrizione': 'Applicatori, presse da banco, spela aggraffa e taglia spela aggraffa automatiche fino a 6 stazioni. '
                    'Wirmec, Ponte San Nicolò (Padova).'},
]
