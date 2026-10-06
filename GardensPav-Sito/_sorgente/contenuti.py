# -*- coding: utf-8 -*-
"""
Contenuti del sito Gardens Pav S.r.l. (Legnaro, PD): vasche monoblocco, depurazione e piattaforme per autolavaggi
in calcestruzzo armato vibrato.

Direzione "La misura" (specifica in _prova/spec.md): la disciplina dei cataloghi di Escofet e Rieder (grottesco pieno,
monospazio per i dati, filetti, una foto vera e nitida), il capo di sezione con le stanghette preso dai disegni quotati
dell'azienda, la tavola tecnica come immagine. Innesti dalla direzione "Il lavoro in primo piano": la vasca 550 quotata,
l'indice con i conteggi, i numeri dell'attrito, la striscia del materiale.
Fonti dei testi: sito attuale (01-analisi-sito-attuale.md, verbatim corretti), tabelle ripulite
(dati/tabelle-pulite.json), cantieri (dati/cantieri.json), mappe disegnate dai dati OpenStreetMap e Natural Earth (dati/*.svg), dati societari da fonti pubbliche.
"""
import json
import os

import motore as m
from motore import C, H, T, B, I, RAW, MENU, SHORTCODE

QUI = os.path.dirname(os.path.abspath(__file__))

PREFISSO = 'gpv'
NOME_SITO = 'Gardens Pav'

# ---------------------------------------------------------------------------------------------
# Tema (spec §3)
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'
GRAFITE = '#1D1E1F'        # testo, titoli, fascia scura, piede (16,7:1 su bianco)
CLS = '#EBECEB'            # fasce "calcestruzzo": il grigio dei render schiarito
TESTO2 = '#58585A'         # il grigio del logo: testo secondario e didascalie (7,1:1)
ARANCIO_SCURO = '#A6470A'  # link, voce attiva, sigle estere (5,95:1 su bianco)
ARANCIO = '#F38239'        # pulsante pieno, quote, vasca scelta, numeri su grafite: mai testo su fondo chiaro
SU_GRAFITE2 = '#C4C7C7'    # testo secondario su grafite (9,8:1)
EVIDENZA = '#FBE7D9'       # riga evidenziata nelle tabelle
LINEA = '#C9CBCA'          # filetti su bianco
LINEA_CLS = '#B5B8B7'      # filetti su #EBECEB
LINEA_SCURA = '#3D3F41'    # filetti su grafite
TRASP = 'rgba(0,0,0,0)'

ARCHIVO = 'Archivo'
MONO = 'IBM Plex Mono'
FONTS = ('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700'
         '&family=IBM+Plex+Mono:wght@400;500&display=swap')


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


TEMA = {
    'nome': 'Misura',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': GRAFITE, 'testo2': TESTO2, 'accento': ARANCIO_SCURO,
    'filetto': LINEA, 'filetto_scuro': LINEA_SCURA, 'su_scuro2': SU_GRAFITE2,
    'scuro': GRAFITE, 'su_scuro': BIANCO, 'su_accento': GRAFITE,
    'font_titoli': ARCHIVO, 'font_testo': ARCHIVO, 'larghezza': 1280, 'google_fonts': FONTS,
    # spaziatura lettere in px (il motore non usa em): valori dagli em della specifica sul corpo desktop
    'stili': {
        'h1':        _st(ARCHIVO, '600', (56, 44, 34), 1.04, -1.0),
        'h2':        _st(ARCHIVO, '600', (42, 34, 28), 1.08, -0.6),
        'h2s':       _st(ARCHIVO, '600', (32, 28, 24), 1.1, -0.4),     # valori della striscia del materiale
        'h3':        _st(ARCHIVO, '600', (24, 22, 20), 1.2, -0.2),
        'h3s':       _st(ARCHIVO, '600', (22, 20, 18), 1.2, -0.2),     # nomi nelle celle di Depurazione
        'h3m':       _st(ARCHIVO, '600', (20, 20, 18), 1.2, -0.2),     # nomi dei modelli di piattaforma
        'h4':        _st(ARCHIVO, '600', (18, 18, 17), 1.3),
        'h4s':       _st(ARCHIVO, '600', (16, 16, 15), 1.3),             # nomi delle tessere colore e accessori
        'mega':      _st(ARCHIVO, '600', (160, 120, 88), 0.9, -4.8),   # solo "C35/45" nella pagina Azienda
        'tel':       _st(ARCHIVO, '600', (72, 56, 40), 1.0, -1.4),
        'tel2':      _st(ARCHIVO, '600', (44, 40, 32), 1.0, -0.4),
        'lettura':   _st(ARCHIVO, '600', (56, 44, 30), 1.0, -1.1),
        'num':       _st(ARCHIVO, '600', (48, 40, 34), 1.0, -0.5),
        'lead':      _st(ARCHIVO, '400', (20, 19, 18), 1.5),
        'body':      _st(ARCHIVO, '400', (17, 17, 16), 1.6),
        'small':     _st(ARCHIVO, '400', (15, 15, 14), 1.55),
        'small13':   _st(ARCHIVO, '400', (13, 13, 13), 1.55),
        'nav':       _st(ARCHIVO, '500', (15, 15, 15), 1.2),
        'nav_m':     _st(ARCHIVO, '600', (22, 22, 22), 1.3),
        'btn':       _st(ARCHIVO, '600', (15, 15, 15), 1.2),
        'link':      _st(ARCHIVO, '600', (15, 15, 15), 1.4),
        'label':     _st(MONO, '500', (12, 12, 11), 1.4, 1.0, True),
        'label_n':   _st(MONO, '400', (12, 12, 11), 1.4, 1.0, True),   # nota a destra del capo di sezione
        'mono':      _st(MONO, '400', (14, 14, 13), 1.5),
        'mono13':    _st(MONO, '400', (13, 13, 13), 1.55),
        'mono12':    _st(MONO, '400', (12, 12, 12), 1.5),
        'mono_m':    _st(MONO, '500', (14, 14, 14), 1.2),               # telefono nella testata
        'didascalia': _st(MONO, '400', (12, 12, 11), 1.5, 0.7, True),
    },
    # una sola scala: 8, 16, 24, 32, 48, 64, 96 (desktop, tablet, mobile)
    'spazi': {
        'sezione': (96, 64, 64), 'lato': (48, 32, 24), 'xl': (64, 48, 48), 'l': (48, 32, 32), 'm': (32, 24, 24),
        's': (16, 16, 16), 'xs': (8, 8, 8), 'col': (32, 24, 16), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): l'hover cambia colore pieno, mai opacità
    'bottoni': {
        'primario': (GRAFITE, ARANCIO, ARANCIO, BIANCO, GRAFITE, GRAFITE),
        'contorno': (GRAFITE, TRASP, GRAFITE, BIANCO, GRAFITE, GRAFITE),
        # su grafite (i nomi "bianco" danno al fallback il contorno di focus chiaro)
        'bianco': (GRAFITE, ARANCIO, ARANCIO, GRAFITE, BIANCO, BIANCO),
        'contorno-bianco': (BIANCO, TRASP, BIANCO, GRAFITE, BIANCO, BIANCO),
    },
    'bottone': {'raggio': 0, 'pad': (16, 32, 16, 32), 'bordo': 1, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/GardensPav-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# misure delle immagini e quote ricalcolate sui ritagli (scritte da prepara_immagini.py)
MISURE_IMG = json.load(open(os.path.join(QUI, 'immagini.json'), encoding='utf-8'))

# ---------------------------------------------------------------------------------------------
# Dati aziendali (un solo posto da aggiornare; fonti in 01-analisi-sito-attuale.md)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
WJ = '⁠'                                  # word joiner: niente a capo dentro gli intervalli orari
TEL = f'049{NBSP}641591'
TEL_LINK = 'tel:+39049641591'
FAX = f'049{NBSP}641913'
EMAIL = 'info@gardenspav.it'
PEC = 'gardenspav@legalmail.it'
INDIRIZZO = 'Via Romea 154/A'
CITTA = f'35020 Legnaro{NBSP}(PD)'
ORE = f'8{WJ}-{WJ}12 e 14{WJ}-{WJ}18'
ORARI = f'Dal lunedì al venerdì, {ORE}'
ORARI_BREVE = f'lun{WJ}-{WJ}ven {ORE}'
CHIUSURA = 'Sabato e domenica chiuso'
PIVA = '03963070283'
REA = f'PD{WJ}-{WJ}351148'
MAPS = 'https://www.google.com/maps/place/?q=place_id:ChIJbQ_ElZHDfkcRCaj8RLz7rzQ'
RICHIESTA = '/contatti/#richiesta'
FRECCIA = f'{NBSP}→'

# larghezze delle colonne della griglia a 12 (contenitore 1280, spazio 32; a 1024 960 e 24: stesse percentuali),
# arrotondate per difetto perché somma + spazi stia sotto il 100%
W = {2: 14.55, 3: 23.1, 4: 31.65, 5: 40.2, 6: 48.7, 7: 57.25, 8: 65.8, 12: 100}


def w(d, t=None, mob=100):
    """Larghezze in colonne: desktop, tablet (predefinito come desktop), mobile in % (predefinito 100)."""
    return (W[d], W[t if t is not None else d], mob)


# ---------------------------------------------------------------------------------------------
# Componenti comuni (riusabili nelle altre pagine)
# ---------------------------------------------------------------------------------------------
def sezione(*children, bg=BIANCO, pad=('sezione', 'lato'), **p):
    """Sezione a contenitore da 1280. Gli spazi tra i blocchi si danno con mt sui figli (gap 0): così i widget HTML
    che portano solo CSS non aggiungono spazio."""
    p.setdefault('gap', '0')
    # gpv-cls: fascia grigia (la prima colonna fissa delle tabelle che scorrono prende lo stesso fondo)
    p['css'] = ('gpv-sito ' + ('gpv-cls ' if bg == CLS else '') + p.get('css', '')).strip()
    return C(*children, bg=bg, pad=pad, tag='section', **p)


def capo(etichetta, nota='', scuro=False, **p):
    """Capo di sezione: etichetta in monospazio a sinistra, nota di servizio a destra, sotto la quota con le stanghette
    (dai disegni quotati dell'azienda). Su grafite tutto #C4C7C7."""
    c1 = SU_GRAFITE2 if scuro else GRAFITE
    c2 = SU_GRAFITE2 if scuro else TESTO2
    figli = [T(f'<p>{etichetta}</p>', style='label', color=c1)]
    if nota:
        figli.append(T(f'<p>{nota}</p>', style='label_n', color=c2, align=('right', 'right', 'left')))
    riga = C(*figli, dir='row', dir_m='column', justify='between', align=('baseline', 'baseline', 'start'),
             gap=('m', 'm', 4))
    stanghette = C(min_h=9, border_left=1, border_right=1, border_bottom=1, border_color=c1, css='gpv-stanghette')
    p.setdefault('mb', 'l')
    return C(riga, stanghette, gap='xs', css='gpv-capo', **p)


def testo(html, style='body', color=GRAFITE, scuro=False, **p):
    """Editor di testo con i link del sito: arancio scuro sottolineato, hover grafite (su grafite: bianco, hover arancio)."""
    if scuro:
        p.setdefault('link_color', BIANCO)
        p.setdefault('link_hover', ARANCIO)
    else:
        p.setdefault('link_color', ARANCIO_SCURO)
        p.setdefault('link_hover', GRAFITE)
    return T(html, style=style, color=color, **p)


def link_freccia(testo_link, url, scuro=False, **p):
    """Link di testo con la freccia (carattere, non icona)."""
    colore = BIANCO if scuro else ARANCIO_SCURO
    classi = ('gpv-tap ' + p.pop('css', '')).strip()
    return T(f'<p><a href="{url}">{testo_link}{FRECCIA}</a></p>', style='link', color=colore, link_color=colore,
             link_hover=ARANCIO if scuro else GRAFITE, css=classi, **p)


def figura(nome, alt, didascalia, colore=TESTO2, **p):
    """Foto o render con la didascalia in monospazio sotto, a 8 px."""
    return C(I(img(nome), alt), T(f'<p>{didascalia}</p>', style='didascalia', color=colore), gap='xs', **p)


def indice(voci, **p):
    """Righe-link alte 56 tra filetti (grafite sopra la prima, #C9CBCA tra le righe): nome a sinistra,
    conteggio in monospazio e freccia a destra. voci = [(nome, conteggio, url), ...]"""
    righe = [C(H(nome, 'p', style='h4', color=GRAFITE, css='gpv-nome'),
               T(f'<p>{conto}<span class="gpv-freccia" aria-hidden="true">→</span></p>', style='label', color=TESTO2,
                 fisso=True),
               dir='row', justify='between', align='center', gap='s', min_h=56, pad=(12, 0), border_bottom=1,
               border_color=LINEA, link=url, css='gpv-riga')
             for nome, conto, url in voci]
    return C(*righe, border_top=1, border_color=GRAFITE, gap='0', css='gpv-indice', **p)


def bottoni(*b, **p):
    """Pulsanti in fila (a capo se non stanno), uno sotto l'altro a tutta larghezza sul telefono."""
    return C(*b, dir='row', dir_m='column', wrap=True, gap='s', **p)


def celle_filettate(celle, classe, w_celle=(25, 50, 100), pad_v=24, filetto=LINEA):
    """Fila di celle divise da filetti verticali (cartiglio, riga dati, materiale). A tablet 2 x 2, al telefono in
    colonna con filetti orizzontali: i bordi per punto di rottura sono nel CSS comune (classi gpv-fila-celle e gpv-cN)."""
    out = []
    n = len(celle)
    for i, figli in enumerate(celle):
        sinistra = (0 if i == 0 else pad_v, 0 if i % 2 == 0 else pad_v, 0)
        destra = (0 if i == n - 1 else pad_v, pad_v if i % 2 == 0 else 0, 0)
        out.append(C(*figli, gap='xs', w=w_celle, pad=((pad_v, pad_v, 16), destra, (pad_v, pad_v, 16), sinistra),
                     border_left=1 if i else 0, border_color=filetto, css=f'gpv-cella gpv-c{i + 1}'))
    return C(*out, dir='row', wrap=True, gap='0', css=f'gpv-fila-celle {classe}')


def riga_contatto(etichetta, *valori):
    """Riga a filetto del blocco ufficio tecnico: etichetta a 140 px, valore a destra (al telefono sopra/sotto)."""
    return C(T(f'<p>{etichetta}</p>', style='label', color=TESTO2, w_px=(140, 140, 0), mt=(6, 6, 0), fisso=True),
             C(*valori, gap='xs', grow=True),
             dir='row', dir_m='column', gap=('s', 's', 'xs'), pad=(16, 0), border_bottom=1, border_color=LINEA,
             align='start')


def ufficio_tecnico(bg=BIANCO, nota=f'LUN{WJ}-{WJ}VEN 8{WJ}-{WJ}12 E 14{WJ}-{WJ}18'):
    """Blocco comune in fondo a ogni pagina tranne Contatti (spec §3.6)."""
    sinistra = C(
        H('Portate più grandi o misure fuori tabella: chiedete all’ufficio tecnico', 'h2'),
        testo('<p>Indicate il manufatto e il dato che lo dimensiona: portata in litri al secondo, abitanti equivalenti '
              'o superficie scolante in metri quadri. Per le piattaforme, il modello e il luogo di posa.</p>',
              color=TESTO2, mt='m'),
        C(B('Scrivi all’ufficio tecnico', RICHIESTA, variant='primario', full_m=True), mt='m'),
        w=w(6), gap='0')
    destra = C(
        riga_contatto('Telefono',
                      H(TEL, 'p', style='tel2', color=GRAFITE, link=TEL_LINK, css='gpv-tel-grande'),
                      T(f'<p>Fax {FAX}</p>', style='small', color=TESTO2)),
        riga_contatto('Email',
                      testo(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
                      T(f'<p>PEC {PEC}</p>', style='small', color=TESTO2)),
        riga_contatto('Orari', T(f'<p>{ORARI}</p>', style='body', color=GRAFITE),
                      T(f'<p>{CHIUSURA}</p>', style='small', color=TESTO2)),
        riga_contatto('Sede', T(f'<p>{INDIRIZZO}, {CITTA}</p>', style='body', color=GRAFITE),
                      testo(f'<p><a href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps</a></p>',
                            style='small', css='gpv-tap')),
        w=w(6), gap='0', border_top=1, border_color=LINEA)
    return sezione(
        capo('Contatti', nota),
        C(sinistra, destra, dir='row', dir_m='column', justify='between', gap=('col', 'col', 'l')),
        bg=bg, anchor='ufficio-tecnico')


def tabella(colonne, righe, nome, scura=False, evidenzia=None, note=None):
    """Tabella dati (widget HTML): intestazione in monospazio maiuscolo, celle in monospazio, prima colonna a sinistra,
    numeri a destra. evidenzia = (indice riga, etichetta). Sopra le 4 colonne scorre dentro il suo involucro."""
    th = ''.join(f'<th scope="col">{c}</th>' for c in colonne)
    tr = []
    for i, r in enumerate(righe):
        cls = ' class="gpv-evid"' if evidenzia and evidenzia[0] == i else ''
        extra = f' <span class="gpv-infoto">{evidenzia[1]}</span>' if cls else ''
        tr.append(f'<tr{cls}><th scope="row">{r[0]}{extra}</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>')
    tab = (f'<table class="gpv-tabella{" gpv-tabella-scura" if scura else ""}"><thead><tr>{th}</tr></thead>'
           f'<tbody>{"".join(tr)}</tbody></table>')
    if len(colonne) > 4:
        tab = f'<div class="gpv-tab-scorre" tabindex="0" role="region" aria-label="{nome}">{tab}</div>'
    if note:
        tab += '<p class="gpv-tab-note">' + '<br>'.join(note) + '</p>'
    return tab


# ---------------------------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------------------------
# solo Elementor: correzioni al tema Hello e a Ultimate Addons (nel fallback non servono)
CSS_BASE = (
    'em,i,cite{font-style:normal}'
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    # Ultimate Addons: voci su una riga, testata tagliata in orizzontale (il menu chiuso sporge a destra)
    '@media (min-width:1025px){.hfe-nav-menu__layout-horizontal .hfe-nav-menu{flex-wrap:nowrap}'
    '.hfe-nav-menu .hfe-menu-item{white-space:nowrap}}'
    '.gpv-testata{overflow-x:clip}'
    # voce attiva: testo arancio scuro, sottolineatura arancio da 2 px
    f'.gpv-testata .hfe-nav-menu .current-menu-item>a.hfe-menu-item,.gpv-testata .hfe-nav-menu .current-menu-item>a.hfe-menu-item:hover'
    f'{{color:{ARANCIO_SCURO}!important}}'
    f'@media (min-width:1025px){{.gpv-testata .hfe-pointer__underline .menu-item>a.hfe-menu-item:after{{height:2px!important;'
    f'background-color:{ARANCIO}!important;bottom:-2px}}}}'
    # pulsante del menu a tendina: quadrato 48 x 48 con bordo, tre linee (X quando è aperto)
    f'.gpv-testata .hfe-nav-menu__toggle{{margin:0}}'
    f'.gpv-testata .hfe-nav-menu-icon{{width:48px;height:48px;display:flex!important;align-items:center;justify-content:center;'
    f'border:1px solid {GRAFITE}!important;border-radius:0!important;padding:0!important;color:{GRAFITE}!important;'
    f'background:{BIANCO}!important;box-sizing:border-box}}'
    f'.gpv-testata .hfe-nav-menu-icon:hover{{background:{GRAFITE}!important;color:{BIANCO}!important}}'
    f'.gpv-testata .hfe-nav-menu-icon svg{{fill:currentColor!important;width:20px!important;height:20px!important}}'
    # tendina: righe alte 56 con filetto, voce attiva con la barretta arancio a sinistra
    f'@media (max-width:1024px){{.gpv-testata nav.hfe-dropdown{{border-top:1px solid {LINEA};border-bottom:1px solid {LINEA}}}'
    f'.gpv-testata nav.hfe-dropdown .menu-item a.hfe-menu-item{{min-height:56px;display:flex!important;align-items:center;'
    f'padding:0 32px!important;border-bottom:1px solid {LINEA};position:relative}}'
    f'.gpv-testata nav.hfe-dropdown .menu-item:last-child a.hfe-menu-item{{border-bottom:0}}'
    '.gpv-testata nav.hfe-dropdown .menu-item a.hfe-menu-item:after,.gpv-testata nav.hfe-dropdown .menu-item a.hfe-menu-item:before'
    '{display:none!important}'
    f'.gpv-testata nav.hfe-dropdown .menu-item.current-menu-item>a.hfe-menu-item:before{{content:""!important;display:block!important;'
    f'position:absolute!important;left:0!important;right:auto!important;top:16px!important;bottom:auto!important;width:3px!important;'
    f'height:24px!important;background:{ARANCIO}!important;opacity:1!important;transform:none!important}}}}'
    '@media (max-width:767px){.gpv-testata nav.hfe-dropdown .menu-item a.hfe-menu-item{padding:0 24px!important}}'
    f"a.hfe-skip-link:focus{{background:{GRAFITE};color:{BIANCO};border-radius:0;box-shadow:none;outline:2px solid {BIANCO};"
    f"outline-offset:-4px;font:600 15px/1 '{ARCHIVO}',Arial,sans-serif;text-decoration:none;padding:16px 24px}}"
)

# entrambe le versioni (Elementor e fallback): componenti comuni a tutte le pagine
CSS_COMUNE = (
    # focus visibile: arancio scuro su chiaro, arancio su grafite
    f'.gpv-sito a:focus-visible,.gpv-sito button:focus-visible,.gpv-sito summary:focus-visible,'
    f'.gpv-sito [tabindex]:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:2px!important}}'
    f'.gpv-scuro a:focus-visible,.gpv-scuro button:focus-visible,.gpv-scuro summary:focus-visible,'
    f'.gpv-scuro [tabindex]:focus-visible{{outline-color:{ARANCIO}!important}}'
    # aree di tocco dei link di testo: uguali a vista, alte circa 40 px
    '.gpv-tap a{display:inline-block;padding:10px 0;margin:-10px 0}'
    # capo di sezione: la quota con le stanghette è alta 9 px, sempre
    '.gpv-stanghette{height:9px;min-height:9px!important;flex:0 0 auto}'
    # righe-link: al passaggio il nome si sottolinea e la freccia si sposta di 4 px e diventa arancio scuro
    '.gpv-riga{text-decoration:none!important}'
    '.gpv-riga .gpv-freccia{display:inline-block;margin-left:16px;transition:transform .15s,color .15s}'
    f'.gpv-riga:hover .gpv-freccia,.gpv-riga:focus-visible .gpv-freccia{{transform:translateX(4px);color:{ARANCIO_SCURO}}}'
    '.gpv-riga:hover .gpv-nome,.gpv-riga:focus-visible .gpv-nome{text-decoration:underline;text-decoration-thickness:1px;'
    'text-underline-offset:4px}'
    '@media (prefers-reduced-motion:reduce){.gpv-riga .gpv-freccia{transition:none}}'
    # etichette dentro le righe di dati
    f".gpv-lab{{font-family:'{MONO}',monospace;font-weight:500;font-size:12px;letter-spacing:1px;text-transform:uppercase;"
    f'color:{TESTO2};margin-right:10px}}'
    '.gpv-nowrap{white-space:nowrap}'
    # link in fila (gap 24)
    '.gpv-fila p{display:flex;flex-wrap:wrap;column-gap:24px;row-gap:4px}'
    # celle filettate: a tablet 2 x 2, al telefono in colonna con filetti orizzontali
    f'@media (min-width:768px) and (max-width:1024px){{.gpv-fila-celle>.gpv-c3{{border-left-width:0!important}}'
    f'.gpv-fila-celle>.gpv-c3,.gpv-fila-celle>.gpv-c4{{border-top:1px solid {LINEA}!important}}'
    f'.gpv-fila-cls>.gpv-c3,.gpv-fila-cls>.gpv-c4{{border-top-color:{LINEA_CLS}!important}}}}'
    f'@media (max-width:767px){{.gpv-fila-celle>.gpv-cella{{border-left-width:0!important}}'
    f'.gpv-fila-celle>.gpv-cella+.gpv-cella{{border-top:1px solid {LINEA}!important}}'
    f'.gpv-fila-cls>.gpv-cella+.gpv-cella{{border-top-color:{LINEA_CLS}!important}}}}'
    # numero di telefono grande sottolineato in arancio
    f'.gpv-tel-grande a{{color:{GRAFITE}!important;text-decoration:underline!important;text-decoration-color:{ARANCIO}!important;'
    'text-decoration-thickness:2px!important;text-underline-offset:6px}'
    f'.gpv-tel-grande a:hover{{color:{ARANCIO_SCURO}!important}}'
    # tabelle dati (il tema Hello colora le righe alterne e mette i bordi: qui si tolgono)
    f".gpv-tabella{{width:100%;border-collapse:collapse;border-spacing:0;margin:0!important;font-family:'{MONO}',monospace;"
    f'font-size:14px;line-height:1.4;color:{GRAFITE};font-variant-numeric:tabular-nums;background:transparent}}'
    f'.gpv-tabella tr>*{{padding:9px 0 9px 16px!important;height:40px;border:0!important;border-bottom:1px solid {LINEA}!important;'
    'background:transparent!important;text-align:right;font-weight:400;vertical-align:middle;white-space:nowrap;'
    'line-height:1.4!important}'
    '.gpv-tabella tr>*:first-child{text-align:left;padding-left:0!important;white-space:normal}'
    f'.gpv-tabella thead th{{font-size:12px;font-weight:500;letter-spacing:1px;text-transform:uppercase;color:{TESTO2};'
    f'height:auto;padding-top:0!important;padding-bottom:8px!important;border-bottom-color:{GRAFITE}!important;vertical-align:bottom}}'
    f'.gpv-tabella tr.gpv-evid>*{{background:{EVIDENZA}!important}}'
    f".gpv-tabella .gpv-infoto{{font-weight:500;font-size:12px;letter-spacing:1px;color:{ARANCIO_SCURO};margin-left:8px}}"
    f'.gpv-tabella-scura{{color:{BIANCO}}}.gpv-tabella-scura tr>*{{border-bottom-color:{LINEA_SCURA}!important}}'
    f'.gpv-tabella-scura thead th{{color:{SU_GRAFITE2};border-bottom-color:{SU_GRAFITE2}!important}}'
    f".gpv-tab-note{{margin:16px 0 0!important;font:400 14px/1.55 '{ARCHIVO}',Arial,sans-serif;color:{TESTO2}}}"
    '.gpv-tab-scorre{overflow-x:auto;max-width:100%}'
    '.gpv-piede-lista .gpv-voce{display:block;padding:4px 0;line-height:1.45}'
    '@media (max-width:1024px){.gpv-piede-lista .gpv-voce{padding:8px 0}}'
    # titoli-paragrafo bilanciati anche nel fallback (in Elementor lo fa la regola sui widget Titolo)
    '.gpv-sito p.gpv-w{text-wrap:balance}'
    '.gpv-tabella thead th{white-space:normal}'
    '@media (max-width:1024px){.gpv-tabella{font-size:13px}}'
    '@media (max-width:767px){.gpv-tabella{font-size:13px}.gpv-tabella tr>*{height:36px;padding-top:7px!important;'
    'padding-bottom:7px!important}.gpv-tab-scorre .gpv-tabella tr>*:first-child{position:sticky;left:0;background:#FFFFFF!important}'
    f'.gpv-cls .gpv-tab-scorre .gpv-tabella tr>*:first-child{{background:{CLS}!important}}'
    f'.gpv-tab-scorre .gpv-tabella tr.gpv-evid>*:first-child{{background:{EVIDENZA}!important}}}}'
)

# fallback: stessi colori del menu di Ultimate Addons (voce attiva, tendina, pulsante a tre linee)
CSS_NAV_FALLBACK = (
    f'.gpv-testata .gpv-nav-l a[aria-current=page]{{color:{ARANCIO_SCURO}!important;border-bottom:2px solid {ARANCIO}!important;'
    'padding-bottom:6px!important}'
    f'.gpv-testata .gpv-nav-l a:hover{{color:{ARANCIO_SCURO}!important}}'
    f'.gpv-testata summary{{width:48px;height:48px;min-width:48px;border:1px solid {GRAFITE};justify-content:center!important;'
    f'background:{BIANCO}}}'
    f'.gpv-testata summary:hover{{background:{GRAFITE}}}'
    f'.gpv-testata summary .gpv-ico{{width:20px!important;height:14px!important;border-top-width:2px!important;'
    'border-bottom-width:2px!important}'
    '.gpv-testata summary .gpv-ico::after{top:4px!important;border-top-width:2px!important}'
    f'.gpv-testata summary:hover .gpv-ico,.gpv-testata summary:hover .gpv-ico::after{{border-color:{BIANCO}!important}}'
    '.gpv-testata .gpv-con{position:static!important}.gpv-testata nav.gpv-w{position:static!important}'
    f'.gpv-testata details ul{{margin-top:0!important;top:100%!important;left:0!important;right:0!important}}'
    '.gpv-testata details[open] summary .gpv-ico{border-color:transparent!important}'
    '.gpv-testata details[open] summary .gpv-ico::after{top:4px!important;transform:rotate(45deg)}'
    f'.gpv-testata details[open] summary .gpv-ico::before{{content:"";position:absolute;left:0;right:0;top:4px;'
    f'border-top:2px solid {GRAFITE};transform:rotate(-45deg)}}'
    f'.gpv-testata details[open] summary:hover .gpv-ico::before{{border-color:{BIANCO}}}'
    f'.gpv-testata details li a{{min-height:56px;display:flex!important;align-items:center;padding:0 32px!important;'
    f'border-bottom:1px solid {LINEA}!important;position:relative;font-size:22px!important;font-weight:600!important;'
    'line-height:1.3!important}'
    f'.gpv-testata details li:last-child a{{border-bottom:0!important}}'
    '@media (max-width:767px){.gpv-testata details li a{padding:0 24px!important}}'
    f'.gpv-testata details li a[aria-current=page]{{color:{ARANCIO_SCURO}!important}}'
    f'.gpv-testata details li a[aria-current=page]::before{{content:"";position:absolute;left:0;top:16px;width:3px;height:24px;'
    f'background:{ARANCIO}}}'
)

# testata: telefono in monospazio solo sopra i 1280 px, "Chiama" sottolineato in arancio, pulsante più basso
CSS_TESTATA = (
    '@media (max-width:1279px){.gpv-tel-testata{display:none!important}}'
    f'.gpv-tel-testata a{{color:{GRAFITE}!important;text-decoration:none!important}}'
    f'.gpv-tel-testata a:hover{{color:{ARANCIO_SCURO}!important}}'
    f'.gpv-chiama a{{color:{GRAFITE}!important;text-decoration:underline!important;text-decoration-color:{ARANCIO}!important;'
    'text-decoration-thickness:2px!important;text-underline-offset:6px;display:inline-block;padding:12px 0}'
    f'.gpv-chiama a:hover{{color:{ARANCIO_SCURO}!important}}'
    '.gpv-btn-testata a{padding:12px 24px!important}'
    # tra 1025 e 1179 px logo, menu e pulsante non stanno in una riga: resta il menu (Contatti è una voce)
    '@media (min-width:1025px) and (max-width:1179px){.gpv-btn-testata{display:none!important}}'
)

# Esc chiude il menu a tendina (Ultimate Addons e fallback) e riporta il fuoco sul pulsante
JS_TESTATA = (
    "<script>document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;"
    "var t=document.querySelector('.gpv-testata .hfe-nav-menu__toggle[aria-expanded=true]');if(t){t.click();t.focus();}"
    "var d=document.querySelector('.gpv-testata details[open]');if(d){d.open=false;d.querySelector('summary').focus();}});</script>"
)


# ---------------------------------------------------------------------------------------------
# Testata e piede (template separati; con Ultimate Addons diventano testata e piede di tutto il sito)
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Vasche', '/vasche/'), ('Depurazione', '/depurazione/'),
             ('Piattaforme per autolavaggi', '/piattaforme-autolavaggi/'), ('Realizzazioni', '/realizzazioni/'),
             ('Azienda', '/azienda/'), ('Contatti', '/contatti/')]


def header():
    marchio = I(img('logo-gardens-pav.png'), 'Gardens Pav, opere in calcestruzzo', link='/', w_img=(172, 156, 144),
                fisso=True, link_label='Gardens Pav, pagina iniziale')
    azioni = C(
        T(f'<p><a href="{TEL_LINK}">Chiama</a></p>', style='link', color=GRAFITE, link_color=GRAFITE, sottolinea=False,
          hide=['desktop'], fisso=True, css='gpv-chiama'),
        MENU(VOCI_MENU, colore=GRAFITE, colore_hover=ARANCIO_SCURO, accento=ARANCIO_SCURO, fondo_menu=BIANCO, linea=LINEA,
             stile='nav', stile_mobile='nav_m', spazio=24, pad_v=8, distanza=(10), align_menu='right', fisso=True,
             larg=(None, 48, 48)),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='mono_m', color=GRAFITE, link_color=GRAFITE, sottolinea=False,
          hide=['tablet', 'mobile'], fisso=True, css='gpv-tel-testata'),
        B('Richiedi informazioni', RICHIESTA, variant='primario', hide=['tablet', 'mobile'], fisso=True,
          css='gpv-btn-testata'),
        dir='row', align='center', justify='end', gap=('m', 's', 's'), grow=True)
    testata = C(marchio, azioni, dir='row', justify='between', align='center', gap='m', min_h=(84, 64, 64),
                pad=(0, 'lato'), boxed=True)
    return C(testata, RAW('', css=CSS_BASE, solo_elementor=True),
             RAW(JS_TESTATA, css=CSS_COMUNE + CSS_PAGINE + CSS_TESTATA + CSS_NAV_FALLBACK),
             pad='0', gap='0', boxed=False, tag='header', bg=BIANCO, border_bottom=1, border_color=LINEA,
             css='gpv-testata gpv-sito')


def footer():
    def colonna(titolo, voci, larghezza):
        # una voce per riga, ognuna un blocco: se va a capo resta compatta, tra le voci c'è lo spazio di tocco
        html = '<p>' + ''.join(f'<span class="gpv-voce">{v}</span>' for v in voci) + '</p>'
        return C(T(f'<p>{titolo}</p>', style='label', color=SU_GRAFITE2),
                 T(html, style='small', color=BIANCO, link_color=BIANCO, link_hover=ARANCIO, sottolinea=False,
                   css='gpv-piede-lista'),
                 gap='s', w=larghezza)

    def voci(coppie):
        return [f'<a href="{u}">{t}</a>' for t, u in coppie]
    prodotti = voci((('Vasche rettangolari', '/vasche/#rettangolari'), ('Vasche circolari', '/vasche/#circolari'),
                     ('Vasche con resine epossidiche', '/vasche/#resine'), ('Depurazione', '/depurazione/'),
                     ('Piattaforme per autolavaggi', '/piattaforme-autolavaggi/')))
    azienda = voci((('Azienda', '/azienda/'), ('Realizzazioni', '/realizzazioni/'), ('Contatti', '/contatti/'),
                    ('Privacy', '/privacy/'), ('Cookie', '/cookie/')))
    recapiti = [f'Tel. <a href="{TEL_LINK}">{TEL}</a>', f'Fax {FAX}', f'<a href="mailto:{EMAIL}">{EMAIL}</a>',
                f'PEC {PEC}', f'Lun{WJ}-{WJ}ven {ORE}']
    righe = C(
        C(I(img('logo-gardens-pav-chiaro.png'), 'Gardens Pav, opere in calcestruzzo', link='/', w_img=(172, 172, 156),
            link_label='Gardens Pav, pagina iniziale'),
          T('<p>Vasche monoblocco, depurazione e piattaforme per autolavaggi in calcestruzzo armato vibrato, '
            'prodotte a Legnaro (PD).</p>', style='small', color=SU_GRAFITE2),
          gap='m', w=(W[4], W[6], 100)),
        colonna('Prodotti', prodotti, (W[3], W[6], 47)),
        colonna('Azienda', azienda, (W[2], W[6], 47)),
        colonna('Recapiti', recapiti, (W[3], W[6], 100)),
        dir='row', wrap=True, justify='between', gap='col', gap_r=('l', 'l', 'l'))
    legale = C(
        T(f'<p>© 2026 Gardens Pav S.r.l. · Sede legale e operativa {INDIRIZZO}, {CITTA} · P.IVA e C.F. {PIVA} · '
          f'Registro Imprese di Padova, REA {REA} · Capitale sociale 100.000 euro</p>', style='small13', color=SU_GRAFITE2),
        T('<p><a href="/privacy/">Privacy</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="/cookie/">Cookie</a></p>', style='small13',
          color=SU_GRAFITE2, link_color=BIANCO, link_hover=ARANCIO, sottolinea=False, align=('right', 'right', 'left'),
          fisso=True, css='gpv-tap'),
        dir='row', dir_m='column', justify='between', gap='m', pad=('m', 0, 0, 0), border_top=1, border_color=LINEA_SCURA)
    return C(righe, legale, gap='l', pad=((64, 64, 48), 'lato', (48, 48, 32), 'lato'), bg=GRAFITE,
             tag='footer', css='gpv-scuro gpv-sito')


# ---------------------------------------------------------------------------------------------
# HOME (spec §6)
# ---------------------------------------------------------------------------------------------
def home_apertura():
    """H1: la vasca col logo dipinto appesa all'autogru accanto a un titolo che dice le due cose che l'azienda fa;
    sotto, il cartiglio come la tabella in fondo ai disegni dell'azienda."""
    sinistra = C(
        testo('<p>Produciamo a Legnaro, in provincia di Padova, manufatti in calcestruzzo armato vibrato per i reflui '
              'domestici e industriali e per le acque meteoriche, e piattaforme che in poche ore diventano la '
              'pavimentazione di un autolavaggio.</p>', style='lead', color=TESTO2),
        indice([('Vasche monoblocco', '17 misure', '/vasche/'),
                ('Depurazione', '7 impianti', '/depurazione/'),
                ('Piattaforme per autolavaggi', '8 modelli', '/piattaforme-autolavaggi/'),
                ('Realizzazioni', '36 cantieri', '/realizzazioni/')], mt='m'),
        bottoni(B('Richiedi informazioni', RICHIESTA, variant='primario', full_m=True),
                B(f'Chiama {TEL}', TEL_LINK, variant='contorno', full_m=True), mt='m'),
        w=w(5), gap='0')
    destra = figura('apertura-vasca-autogru.jpg', 'Vasca rettangolare monoblocco con il logo Gardens Pav sollevata '
                    'dall’autogru sopra l’autoarticolato, montagne sullo sfondo',
                    'Vasca rettangolare monoblocco sollevata con l’autogru', w=w(7))
    celle = [
        [T('<p>Sede e stabilimento</p>', style='label', color=TESTO2),
         T(f'<p>{INDIRIZZO}, {CITTA}</p>', style='small', color=GRAFITE)],
        [T('<p>Telefono e orari</p>', style='label', color=TESTO2),
         T(f'<p><a href="{TEL_LINK}">{TEL}</a>, {ORARI_BREVE}</p>', style='small', color=GRAFITE, link_color=GRAFITE,
           link_hover=ARANCIO_SCURO)],
        [T('<p>Trasporto e posa</p>', style='label', color=TESTO2),
         T('<p>Trasporto con automezzi con e senza gru, su richiesta. Le piattaforme le installa il nostro personale.</p>',
           style='small', color=GRAFITE)],
        [T('<p>Cantieri</p>', style='label', color=TESTO2),
         T('<p>Italia, Svizzera, Slovacchia, Francia, San Marino</p>', style='small', color=GRAFITE)],
    ]
    cartiglio = celle_filettate(celle, 'gpv-cartiglio')
    cartiglio.children[3].p['hide'] = ['mobile']          # al telefono tre celle
    cartiglio.p.update(border_top=1, border_bottom=1, border_color=GRAFITE, mt=48)
    return sezione(
        T('<p>Opere in calcestruzzo · Legnaro (PD)</p>', style='label', color=TESTO2),
        H('Vasche e impianti per il trattamento delle acque.<br>Piattaforme prefabbricate per autolavaggi.', 'h1',
          mt=24, css='gpv-sbilancia'),
        C(sinistra, destra, dir='row', dir_m='column-reverse', justify='between', align='start', gap=('col', 'col', 'm'),
          mt=48),
        cartiglio,
        RAW('', css='.gpv-sbilancia,.gpv-sbilancia .elementor-heading-title{text-wrap:wrap!important}'),
        pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')


def home_vasche():
    """H2: il pezzo grande con la sua quota, letto come in un disegno tecnico."""
    sx, dx = MISURE_IMG['quota-550']
    quota = (f'<div class="gpv-quota" aria-hidden="true" style="margin-left:{sx}%;margin-right:{dx}%">'
             '<span></span><b>550 cm</b><span></span></div>')
    css = (f'.gpv-quota{{display:flex;align-items:center;height:16px;border-left:1px solid {GRAFITE};'
           f'border-right:1px solid {GRAFITE}}}'
           f'.gpv-quota span{{flex:1 1 0;height:1px;background:{GRAFITE}}}'
           f".gpv-quota b{{font:400 13px/1 '{MONO}',monospace;color:{GRAFITE};padding:0 12px;white-space:nowrap}}")
    def dato(i, etich, valore):
        # 4 in fila a desktop (la prima più larga: porta le tre misure), 2 x 2 a tablet e telefono;
        # filetti verticali #B5B8B7 tra le celle, il valore allineato in basso anche se l'etichetta va a capo
        sinistra = (0 if i == 0 else 16, 0 if i % 2 == 0 else 16, 0 if i % 2 == 0 else 16)
        destra = (0 if i == 3 else 16, 16 if i % 2 == 0 else 0, 16 if i % 2 == 0 else 0)
        return C(T(f'<p>{etich}</p>', style='label', color=TESTO2), H(valore, 'p', style='h4', css='gpv-nowrap'),
                 gap='xs', w=((30, 22, 22, 26)[i], 50, 50), pad=(8, destra, (0, 12, 12), sinistra), justify='between',
                 border_left=1 if i else 0, border_color=LINEA_CLS, css=f'gpv-dato gpv-d{i + 1}')
    dati = C(dato(0, 'Misure, cm', '550×243×260&nbsp;h'), dato(1, 'Volume', '25,00&nbsp;mc'),
             dato(2, 'Peso vasca', '16,00&nbsp;t'), dato(3, 'Soletta in due elementi', '7,50&nbsp;t'),
             dir='row', wrap=True, gap='0')
    css += '@media (max-width:1024px){.gpv-dato.gpv-d3{border-left-width:0!important}}'
    immagine = C(
        C(I(img('render-vasca-550.jpg'), 'Render della vasca rettangolare 550 con la soletta di copertura in due elementi'),
          RAW(quota, css=css), gap='s', w=(81.8, 100, 100)),
        C(T('<p>Vasca rettangolare 550</p>', style='label', color=GRAFITE), dati, gap='xs', border_top=1,
          border_color=GRAFITE, pad=(16, 0, 0, 0), mt=24),
        align='center', w=w(7, 6), gap='0')
    titolo = 'Undici misure rettangolari e sei circolari, da 2,30 a 50&nbsp;mc.'
    destra = C(
        H(titolo, 'h2', hide=['mobile']),
        testo('<p>Vasche monolitiche a tenuta idraulica, in calcestruzzo armato vibrato in cassero. Servono per il recupero '
              'dell’acqua piovana, le acque di prima pioggia, l’acqua potabile e l’accumulo per impianti antincendio.</p>'
              '<p>Sono disponibili anche con l’interno trattato con resine epossidiche.</p>', color=TESTO2, mt=('m', 'm', 0)),
        testo('<p><a href="/vasche/#rettangolari">Rettangolari</a><a href="/vasche/#circolari">Circolari</a>'
              '<a href="/vasche/#resine">Con resine epossidiche</a></p>', style='link', css='gpv-fila gpv-tap', mt='m'),
        C(B('Le tabelle delle vasche', '/vasche/', variant='contorno', full_m=True), mt='m'),
        w=w(5, 6), gap='0')
    return sezione(
        capo('Vasche prefabbricate monoblocco', 'Misure esterne in cm, pesi in tonnellate'),
        H(titolo, 'h2', hide=['desktop', 'tablet'], mb='m'),
        C(immagine, destra, dir='row', dir_m='column', justify='between', align=('center', 'center', 'stretch'),
          gap=('col', 'col', 'l')),
        bg=CLS, anchor='vasche')


IMPIANTI = [
    ('Dissabbiatore statico', 'Sabbie e fanghi si depositano sul fondo, l’acqua e i liquidi leggeri proseguono verso '
     'l’uscita.', 'Volume', 'da 2,30 a 50&nbsp;mc', 'render-dissabbiatore-400.jpg', 'dissabbiatore'),
    ('Separatore grassi', 'Per le acque di cucine e mense, macellerie, salumifici e impianti per grigliare, arrostire e '
     'friggere.', 'Portata', 'da 3 a 38&nbsp;l/s · <span class="gpv-nowrap">UNI EN 1825-1</span>',
     'render-separatore-grassi-400.jpg', 'separatore-grassi'),
    ('Vasca Imhoff', 'Trattamento primario dei reflui domestici: sedimentazione nel comparto alto, digestione in quello '
     'basso.', 'Abitanti eq.', 'da 5 a 70', 'render-imhoff-400.jpg', 'imhoff'),
    ('Separatore oli con filtro a coalescenza', 'Per i piazzali di officine, distributori di carburante, autolavaggi e '
     'autodemolizioni.', 'Portata', 'da 3 a 30&nbsp;l/s', 'render-separatore-oli-400.jpg', 'separatore-oli'),
    ('Separatore oli per autorimesse', 'Per le acque di lavaggio di pavimenti e rampe, anche con scarico nella Laguna '
     'di Venezia.', 'Superficie', 'fino a 7.000&nbsp;mq e 450 posti auto', 'render-separatore-oli-autorimesse-400.jpg',
     'separatore-oli-autorimesse'),
    ('Impianto di prima pioggia', 'Accumulo per 48 ore; in uscita oli minerali e idrocarburi non oltre 5&nbsp;mg/l.',
     'Superficie', 'da 400 a 10.000&nbsp;mq', 'render-prima-pioggia-400.jpg', 'prima-pioggia'),
    ('Depuratore biologico', 'Ossidazione totale a fanghi attivi per case sparse, campeggi, ristoranti e scuole senza '
     'rete fognaria.', 'Abitanti eq.', 'da 5 a 20', 'render-depuratore-biologico-400.jpg', 'depuratori-biologici'),
]


def home_depurazione():
    """H3: un indice a due colonne da leggere come un catalogo tecnico, render in sezione senza riquadro."""
    celle = []
    for i, (nome, frase, etich, dato, render, ancora) in enumerate(IMPIANTI, 1):
        celle.append(C(
            I(img(render), nome, w_img=(176, 136, 96), height=(120, 92, 64), fit='contain', fisso=True),
            C(H(nome, 'h3', style='h3s', css='gpv-nome'),
              T(f'<p>{frase}</p>', style='small', color=TESTO2, hide=['mobile'], mt='xs'),
              T(f'<p><span class="gpv-lab">{etich}</span>{dato}</p>', style='mono', color=GRAFITE, mt=('s', 's', 'xs')),
              gap='0', grow=True),
            dir='row', align='start', gap=('m', 's', 's'), pad=(24, 0), w=(W[6], W[6], 100), border_top=1,
            border_color=GRAFITE if i <= 2 else LINEA, link=f'/depurazione/#{ancora}', css=f'gpv-dep gpv-dep-{i}'))
    celle.append(C(
        H('Per portate superiori contattate il nostro ufficio tecnico.', 'p', style='h3s', w_px=(420, 380, 0)),
        C(B('Richiedi informazioni', RICHIESTA, variant='primario', full_m=True), mt=('s', 's', 's')),
        pad=(24, 0), w=(W[6], W[6], 100), border_top=1, border_color=LINEA, justify='start', css='gpv-dep gpv-dep-8'))
    css = (f'.gpv-dep-7,.gpv-dep-8{{border-bottom:1px solid {GRAFITE}!important}}'
           '.gpv-dep{text-decoration:none!important}'
           '.gpv-dep:hover .gpv-nome,.gpv-dep:focus-visible .gpv-nome{text-decoration:underline;text-decoration-thickness:1px;'
           'text-underline-offset:4px}'
           f'@media (max-width:767px){{.gpv-dep-2{{border-top-color:{LINEA}!important}}'
           '.gpv-dep-7{border-bottom:0!important}}')
    return sezione(
        capo('Depurazione', '7 impianti'),
        C(C(H('Dal dissabbiatore al depuratore biologico.', 'h2'), w=w(7, 6)),
          C(testo('<p>Separatori, vasche e impianti in calcestruzzo armato vibrato per i reflui domestici e industriali e '
                  'per le acque meteoriche. Ogni scheda ha la sua tabella di portate, misure, pesi e volumi.</p>',
                  color=TESTO2), w=w(5, 6)),
          dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 's')),
        C(*celle, dir='row', wrap=True, justify='between', gap='col', gap_r=0, mt='l'),
        RAW('', css=css),
        anchor='depurazione')


PIANTA_SVG = (
    '<figure class="gpv-pianta"><svg viewBox="0 0 880 660" role="img" '
    'aria-label="Pianta della pista self Mod. 450: 450 × 650 cm, grigliato 400 × 100 cm">'
    '<defs><pattern id="gpv-rombi" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
    f'<path d="M0 0H24M0 0V24" stroke="{LINEA_SCURA}" stroke-width="1.5" fill="none"/></pattern>'
    '<pattern id="gpv-griglia" width="12.5" height="12.5" patternUnits="userSpaceOnUse" x="235" y="275">'
    '<path d="M0 0H12.5M0 0V12.5" stroke="#8E9191" stroke-width="1" fill="none"/></pattern></defs>'
    # pannelli
    '<rect x="110" y="100" width="650" height="450" fill="url(#gpv-rombi)"/>'
    # pendenze verso il grigliato
    f'<path class="gpv-ns" d="M110 100L235 275M760 100L635 275M110 550L235 375M760 550L635 375" stroke="{SU_GRAFITE2}" '
    'stroke-width="1" fill="none"/>'
    # giunto tra i due pannelli
    '<path class="gpv-ns" d="M110 325H235M635 325H760" stroke="#FFFFFF" stroke-width="1.5" fill="none"/>'
    # grigliato in vetroresina, due moduli da 200 x 100
    f'<rect x="235" y="275" width="400" height="100" fill="{GRAFITE}"/>'
    '<rect x="235" y="275" width="400" height="100" fill="url(#gpv-griglia)"/>'
    '<rect class="gpv-ns" x="235" y="275" width="400" height="100" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
    '<path class="gpv-ns" d="M435 275V375" stroke="#FFFFFF" stroke-width="2"/>'
    # perimetro
    '<rect class="gpv-ns" x="110" y="100" width="650" height="450" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
    # quote
    f'<g class="gpv-ns" stroke="{ARANCIO}" stroke-width="1.4" fill="none">'
    '<path d="M110 562V622M760 562V622M110 605H760M104 611L116 599M754 611L766 599"/>'
    '<path d="M98 100H38M98 550H38M55 100V550M49 106L61 94M49 556L61 544"/>'
    '<path d="M235 262V36M635 262V36M235 52H635M229 58L241 46M629 58L641 46"/>'
    '<path d="M648 275H842M648 375H842M825 275V375M819 281L831 269M819 381L831 369"/></g>'
    f'<g fill="{ARANCIO}" text-anchor="middle" class="gpv-quote-num">'
    '<text x="435" y="644">650</text><text x="435" y="40">400</text>'
    '<text transform="translate(30 325) rotate(-90)">450</text>'
    '<text transform="translate(812 325) rotate(-90)">100</text></g></svg></figure>'
)
CSS_PIANTA = (
    '.gpv-pianta{margin:0}.gpv-pianta svg{display:block;width:100%;height:auto}'
    '.gpv-pianta .gpv-ns,.gpv-pianta .gpv-ns *{vector-effect:non-scaling-stroke}'
    f".gpv-pianta .gpv-quote-num{{font-family:'{MONO}',monospace;font-weight:500;font-size:22px}}"
    # le cifre delle quote restano sopra i 14 px reali a ogni larghezza
    '@media (max-width:1024px){.gpv-pianta .gpv-quote-num{font-size:25px}}'
    '@media (max-width:767px){.gpv-pianta .gpv-quote-num{font-size:37px}}'
)

MODELLI = [
    ('Pista self Mod. 450', '450 × 650 · 2'), ('Pista self Mod. 500', '500 × 650 · 2'),
    ('Pista self Mod. 500 doppia griglia', '500 × 650 · 2'), ('Portale Mod. 1', '500 × 1200 · 4'),
    ('Portale Mod. 2', '500 × 1100 · 4'), ('Portale Mod. 3 lavaggio chassis', '500 × 1200 · 4'),
    ('Portale Mod. 4 con area prelavaggio', '500 × 1300/1800 · 6'), ('Portale Mod. 5', '500 × 1300/1800 · 6'),
]


def home_piattaforme():
    """H4: la pianta quotata della pista self 450 come una tavola, arancio sulle quote (l'unica fascia scura)."""
    righe = [(n.replace('Mod. ', f'Mod.{NBSP}'), v.replace(' ', NBSP)) for n, v in MODELLI]
    tab = tabella(['Modello', 'Pianta in cm · pannelli'], righe, 'Modelli di piattaforma', scura=True)

    def tab_e_pulsante(**p):
        return C(RAW(tab), C(B(f'Le piattaforme{FRECCIA}', '/piattaforme-autolavaggi/', variant='bianco', full_m=True),
                             mt='l'), gap='0', **p)
    numeri = C(
        C(H('0,88', 'p', style='num', color=ARANCIO),
          T('<p>coefficiente di attrito medio sulla superficie bagnata, riferito alla gomma 4S</p>', style='small',
            color=SU_GRAFITE2),
          gap='xs', w=(48.7, 48.7, 47), border_top=1, border_color=LINEA_SCURA, pad=(16, 0, 0, 0)),
        C(H('0,40', 'p', style='num', color=ARANCIO),
          T('<p>il valore da superare secondo il D.M. 236 del 14/06/1989, art. 8.2.2</p>', style='small',
            color=SU_GRAFITE2),
          gap='xs', w=(48.7, 48.7, 47), border_top=1, border_color=LINEA_SCURA, pad=(16, 0, 0, 0)),
        dir='row', justify='between', gap='col', mt='l')
    sinistra = C(
        H('La pavimentazione dell’autolavaggio, operativa in poche ore.', 'h2', color=BIANCO),
        T('<p>Pannelli prefabbricati in calcestruzzo Rck 45, spessi 20 cm, accostati e contrapposti: due per la pista self, '
          'quattro per il portale. Basta preparare il pozzetto centrale di scarico, gli scarichi e il sottofondo di '
          'appoggio, senza casseforme.</p>', style='body', color=SU_GRAFITE2, mt='m'),
        tab_e_pulsante(hide=['mobile'], mt='l'),
        w=w(5), gap='0')
    destra = C(
        RAW(PIANTA_SVG, css=CSS_PIANTA),
        T('<p>Pista self Mod. 450 · pianta in cm · 2 pannelli 228 × 650 × 20, 5,90 t ciascuno · vasca di raccolta '
          '400 × 100 × 110 h · grigliato in vetroresina in moduli 200 × 100</p>', style='didascalia', color=SU_GRAFITE2,
          mt='s'),
        numeri,
        link_freccia('Caratteristiche e vantaggi', '/piattaforme-autolavaggi/#caratteristiche', scuro=True, mt='m'),
        w=w(7), gap='0')
    return sezione(
        capo('Piattaforme per autolavaggi', 'Brevetto depositato n° 275.271', scuro=True),
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        tab_e_pulsante(hide=['desktop', 'tablet'], mt='l'),
        bg=GRAFITE, anchor='piattaforme', css='gpv-scuro')


def home_calcestruzzo():
    """H5: il materiale scritto come una riga di cartiglio, non come un numero-trovata."""
    def cella(etich, valore, nota):
        return [T(f'<p>{etich}</p>', style='label', color=TESTO2),
                T(f'<p>{valore}</p>', style='h2s', color=GRAFITE, mt=4),
                T(f'<p>{nota}</p>', style='small', color=TESTO2, mt=4)]
    esposizione = ' · '.join(f'<span class="gpv-nowrap">{x}</span>' for x in ('XC4', 'XS1-XD2', 'XF1', 'XA2'))
    fila = celle_filettate([
        cella('Calcestruzzo', 'C35/45', 'Rck 45 N/mm², conforme alla UNI EN 206-1. Impianto di betonaggio '
                                        'computerizzato.'),
        cella('Esposizione', esposizione, 'Carbonatazione, cloruri anche di origine marina, gelo e disgelo, terreni e '
                                          'acque aggressivi.'),
        cella('Armatura', 'B450C', 'Acciaio ad aderenza migliorata, copriferro di 3 cm.'),
        cella('Getto', 'S4', 'Classe di consistenza. Getto in cassero, vibratore ad immersione ad alta frequenza.'),
    ], 'gpv-materiale')
    fila.p.update(border_top=1, border_color=GRAFITE)
    return sezione(
        capo('Il calcestruzzo', 'UNI EN 206-1'),
        fila,
        link_freccia('Il calcestruzzo e le norme', '/azienda/#calcestruzzo', mt='m'),
        anchor='calcestruzzo')


def _luoghi():
    cantieri = json.load(open(os.path.join(QUI, 'dati', 'cantieri.json'),
                              encoding='utf-8'))
    ids = {c['luogo']: c['id'] for c in cantieri}
    for c in cantieri:
        c['luogo'] = c['luogo'].replace("'", '’')
    ids.update({c['luogo']: c['id'] for c in cantieri})
    italiane = sorted({(c['luogo'], c['sigla']) for c in cantieri if c['regione'] not in
                       ('Svizzera', 'Slovacchia', 'Francia', 'San Marino')}, key=lambda x: x[0])
    voci = []
    for luogo, sigla in italiane:
        if luogo == 'Verona':
            voci.append(('Verona, due cantieri', sigla, 'verona-autolavaggio', False))
        else:
            voci.append((luogo, sigla, ids[luogo], False))
    voci += [('Poschiavo', 'CH', 'poschiavo', True), ('Lučenec', 'SK', 'lucenec', True),
             ('Francia, due centri di lavaggio', 'FR', 'francia-1', True), ('San Marino', 'RSM', 'san-marino', True)]
    return voci


def home_realizzazioni():
    """H6: una foto vera e la distinta dei luoghi, come l'elenco di una tavola."""
    voci = _luoghi()
    lista = ' '.join(f'<li><a href="/realizzazioni/#{i}">{n}</a> <span class="gpv-sigla{" gpv-estera" if e else ""}">'
                     f'{s}</span></li>' for n, s, i, e in voci)
    css = (f'.gpv-luoghi ul{{columns:4;column-gap:32px;border-top:1px solid {GRAFITE}!important;margin:0!important;'
           'padding:0!important;list-style:none}'
           f'.gpv-luoghi li{{break-inside:avoid;display:flex!important;justify-content:space-between;align-items:center;gap:16px;'
           f'height:36px;padding:0!important;margin:0!important;border:0!important;border-bottom:1px solid {LINEA_CLS}!important}}'
           f'.gpv-luoghi a{{color:{GRAFITE}!important;text-decoration:none!important;white-space:nowrap;overflow:hidden;'
           'text-overflow:ellipsis}'
           f'.gpv-luoghi a:hover,.gpv-luoghi a:focus-visible{{color:{ARANCIO_SCURO}!important;text-decoration:underline!important;'
           'text-underline-offset:4px}'
           f".gpv-luoghi .gpv-sigla{{font:400 12px/1 '{MONO}',monospace;letter-spacing:1px;color:{TESTO2}}}"
           f'.gpv-luoghi .gpv-estera{{color:{ARANCIO_SCURO}}}'
           '@media (max-width:1024px){.gpv-luoghi ul{columns:3;column-gap:24px}}'
           '@media (max-width:767px){.gpv-luoghi ul{columns:1;padding-top:16px!important;border-top:1px solid #1D1E1F!important}'
           '.gpv-luoghi li{display:inline!important;height:auto;border:0!important;line-height:2;white-space:nowrap}'
           '.gpv-luoghi li:not(:last-child)::after{content:" · ";color:#58585A}'
           '.gpv-luoghi .gpv-sigla{font-size:11px;margin-left:2px}}')
    sinistra = figura('realizzazione-altivole-tv.jpg', 'Piattaforme per autolavaggio appena posate ad Altivole, con i '
                      'grigliati verdi e i telai dei portali, autogru sullo sfondo', 'Altivole (TV) · autolavaggio',
                      w=w(6))
    destra = C(
        H('36 cantieri, da Aosta ad Avetrana. Cinque oltre confine.', 'h2'),
        testo('<p>Autolavaggi, autofficine, concessionarie e autotrasporti in Italia, Svizzera, Slovacchia, Francia e '
              'San Marino.</p>', color=TESTO2, mt='m'),
        testo('<p><a href="/realizzazioni/">Tutte le realizzazioni, con le foto dei cantieri</a></p>', style='link',
              mt='m', css='gpv-tap'),
        w=w(6), gap='0', justify='end')
    return sezione(
        capo('Realizzazioni', 'Piattaforme posate'),
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='stretch', gap=('col', 'col', 'm')),
        T(f'<ul>{lista}</ul>', style='small', color=GRAFITE, link_color=GRAFITE, link_hover=ARANCIO_SCURO,
          sottolinea=False, css='gpv-luoghi', mt='l'),
        RAW('', css=css),
        bg=CLS, anchor='realizzazioni')


def home():
    return [('apertura', home_apertura()), ('vasche', home_vasche()), ('depurazione', home_depurazione()),
            ('piattaforme', home_piattaforme()), ('calcestruzzo', home_calcestruzzo()),
            ('realizzazioni', home_realizzazioni()), ('ufficio-tecnico', ufficio_tecnico(bg=BIANCO))]

# ---------------------------------------------------------------------------------------------
# PAGINE INTERNE: dati e componenti in comune
# ---------------------------------------------------------------------------------------------
TABELLE = json.load(open(os.path.join(QUI, 'dati', 'tabelle-pulite.json'), encoding='utf-8'))


def _cella(v):
    # niente a capo dentro una misura ("1050×243×263 h", "Ø 148×206 h", "7,50 *")
    return v.replace(' ', NBSP)


def tab(nome, titolo, evidenzia=None, scura=False, note=True, righe=None):
    """Una tabella di tabelle-pulite.json (colonne, righe, note) nel formato gpv-tabella."""
    t = TABELLE[nome]
    return tabella(t['colonne'], [[_cella(c) for c in r] for r in (righe or t['righe'])], titolo, scura=scura,
                   evidenzia=evidenzia, note=t.get('note') if note else None)


def tabella_voci(righe, nome, scura=False):
    """Tabella a due colonne con testo: codice in monospazio a sinistra, descrizione che va a capo."""
    import re

    def codice(a):
        return re.sub(r'([^ <>]+-[^ <>]+)', r'<span class="gpv-nowrap">\1</span>', a)
    tr = ''.join(f'<tr><th scope="row">{codice(a)}</th><td>{b}</td></tr>' for a, b in righe)
    return (f'<table class="gpv-tabella gpv-tab-voci{" gpv-tabella-scura" if scura else ""}" aria-label="{nome}">'
            f'<tbody>{tr}</tbody></table>')


def etichetta(testo_lab, colore=TESTO2, **p):
    return T(f'<p>{testo_lab}</p>', style='label', color=colore, **p)


def didascalia(testo_did, colore=TESTO2, **p):
    return T(f'<p>{testo_did}</p>', style='didascalia', color=colore, **p)


def riga_dato(lab, valore, larg=140, linea=LINEA, col_lab=TESTO2, pad_v=16, **p):
    """Riga a filetto: etichetta in monospazio a larghezza fissa, valore a destra (al telefono sotto l'etichetta).
    valore: un nodo, o una lista di nodi."""
    valori = valore if isinstance(valore, (list, tuple)) else [valore]
    return C(T(f'<p>{lab}</p>', style='label', color=col_lab, w_px=(larg, larg, 0), fisso=True, mt=(4, 4, 0)),
             C(*valori, gap='xs', grow=True),
             dir='row', dir_m='column', gap=('s', 's', 'xs'), pad=(pad_v, 0), border_bottom=1, border_color=linea,
             align='start', **p)


def elenco_righe(voci, segno=False, linea=LINEA, linea_alta=GRAFITE, stile='small', **p):
    """Elenco a filetti, una voce per riga, non puntato (segno=True: trattino corto arancio a sinistra)."""
    cls = 'gpv-elenco gpv-elenco-segno' if segno else 'gpv-elenco'
    lis = ''.join(f'<li>{v}</li>' for v in voci)
    css = p.pop('css', '')
    return T(f'<ul>{lis}</ul>', style=stile, color=GRAFITE, css=(cls + ' ' + css).strip(), **p)


def mailto(oggetto, corpo):
    from urllib.parse import quote
    return f'mailto:{EMAIL}?subject={quote(oggetto)}&amp;body={quote(corpo)}'


# entrambe le versioni: componenti delle pagine interne
CSS_PAGINE = (
    # sezioni a filo pagina: la colonna di testo riparte dal margine della griglia da 1280
    '@media (min-width:1025px){.gpv-filo-sx{padding-left:max(48px,calc((100% - 1280px) / 2))!important}'
    '.gpv-filo-dx{padding-right:max(48px,calc((100% - 1280px) / 2))!important}'
    '.gpv-filo-int{max-width:515px}'
    '.gpv-did-filo{padding-left:max(48px,calc(100% - 640px))!important}}'
    # foto a filo al telefono, dentro una colonna con il margine di 24
    '@media (max-width:767px){.gpv-filo-m{margin-left:-24px!important;margin-right:-24px!important;'
    'width:calc(100% + 48px)!important;max-width:none!important}}'
    # proporzioni delle foto (ritaglio per punto di rottura, mai ingrandito oltre la nativa)
    '.gpv-ar43 img{aspect-ratio:4/3;object-fit:cover;width:100%!important;height:auto!important}'
    '.gpv-ar11 img{aspect-ratio:1/1;object-fit:cover;width:100%!important;height:auto!important}'
    '@media (min-width:768px) and (max-width:1024px){.gpv-ar169-t img{aspect-ratio:16/9;object-fit:cover;'
    'width:100%!important;height:auto!important}}'
    # elenchi a filetti, una voce per riga
    f'.gpv-elenco ul{{list-style:none;margin:0!important;padding:0!important;border-top:1px solid {GRAFITE}}}'
    f'.gpv-elenco li{{margin:0!important;padding:10px 0!important;border:0!important;border-bottom:1px solid {LINEA}!important}}'
    f'.gpv-cls .gpv-elenco li{{border-bottom-color:{LINEA_CLS}!important}}'
    '.gpv-elenco-segno li{position:relative;padding-left:32px!important}'
    f'.gpv-elenco-segno li::before{{content:"";position:absolute;left:0;top:21px;width:16px;height:2px;background:{ARANCIO}}}'
    # tabelle a due colonne con testo
    '.gpv-tab-voci tr>*{text-align:left!important;white-space:normal!important;vertical-align:top!important;height:auto!important;'
    'padding-top:12px!important;padding-bottom:12px!important}'
    f'.gpv-tab-voci tbody tr:first-child>*{{border-top:1px solid {GRAFITE}!important}}'
    '.gpv-tab-voci th{font-weight:500!important;width:36%;padding-right:16px!important}'
    '.gpv-voci-corte th{width:22%}'
    f".gpv-tab-voci td{{font-family:'{ARCHIVO}',Arial,sans-serif!important;font-size:15px!important;line-height:1.5!important;"
    'padding-left:0!important;font-variant-numeric:normal}'
    '@media (max-width:767px){.gpv-tab-voci td{font-size:14px!important}.gpv-tab-voci th{width:40%}}'
    f'.gpv-cls .gpv-tabella tr>*{{border-bottom-color:{LINEA_CLS}!important}}'
    f'.gpv-cls .gpv-tabella thead th{{border-bottom-color:{GRAFITE}!important}}'
    # codici 01-07 in arancio scuro
    f".gpv-cod{{font-family:'{MONO}',monospace;font-weight:500;color:{ARANCIO_SCURO};margin-right:16px;"
    'font-variant-numeric:tabular-nums}'
    '@media (min-width:1025px){.gpv-sticky{position:sticky!important;top:32px;align-self:flex-start}}'
    f".gpv-sigla-t{{font-family:'{MONO}',monospace;font-weight:400;font-size:.72em;line-height:1;letter-spacing:1px;"
    f'color:{TESTO2};margin-left:8px}}'
)


def capo_scheda(codice, nome, nota, scuro=False):
    return capo(f'{codice}&nbsp;&nbsp;{nome}', nota, scuro=scuro)


# ---------------------------------------------------------------------------------------------
# 02 VASCHE (spec §7)
# ---------------------------------------------------------------------------------------------
def vasche_apertura():
    """V1: il piazzale delle vasche circolari, la foto con più materiale del sito, esce dal margine destro."""
    foto = 'vasche-circolari-piazzale.jpg'
    alt = 'Vasche circolari in calcestruzzo allineate sul piazzale, viste dall’alto'
    testo_col = C(
        etichetta('Vasche prefabbricate monoblocco'),
        H('Vasche in calcestruzzo armato vibrato, a tenuta idraulica.', 'h1', mt=24),
        I(img(foto), alt, hide=['desktop', 'tablet'], css='gpv-filo-m gpv-ar43', mt='m'),
        testo('<p>Le vasche prodotte dalla Gardens Pav sono a tenuta idraulica e possono essere utilizzate per il recupero '
              'dell’acqua piovana, acque di prima pioggia, acqua potabile e accumulo per impianti antincendio.</p>',
              style='lead', color=TESTO2, mt='m'),
        indice([('Rettangolari', f'11 misure, da 2,40 a 50{NBSP}mc', '#rettangolari'),
                ('Circolari', f'6 misure, da 2,30 a 9,80{NBSP}mc', '#circolari'),
                ('Con resine epossidiche', '15 misure', '#resine')], mt='l'),
        gap='0')
    sinistra = C(testo_col, w=(50, 100, 100), pad=(0, ('xl', 'lato', 'lato'), 0, 'lato'), gap='0', css='gpv-filo-sx')
    destra = C(I(img(foto), alt, css='gpv-ar43 gpv-ar169-t'),
               didascalia('Vasche circolari sul piazzale', pad=(0, 0, 0, 24)),
               w=(50, 100, 100), gap='xs', hide=['mobile'])
    return sezione(sinistra, destra, dir='row', dir_t='column', align='start', boxed=False,
                   gap=(0, 'l', 0), pad=(('xl', 48, 48), 0, ('sezione', 'sezione', 'sezione'), 0), anchor='content')


RETT = TABELLE['rettangolari']['righe']
COPERCHIO = {'(1)': 'carrabile leggero', '*': 'in due elementi', '**': 'in tre elementi'}


def _misure(testo_mis):
    return [int(x) for x in testo_mis.replace(' h', '').replace('Ø ', '').split('×')]


def _lettura(riga):
    mis, peso, cop, vol = riga
    if cop == 'senza':
        coperchio = 'senza'
    else:
        num, _, segno = cop.partition(' ')
        coperchio = f'{num} t' + (f', {COPERCHIO[segno]}' if segno else '')
    return mis.replace('×', ' × '), f'{peso} t', coperchio, f'{vol} mc'


CSS_GAMMA = (
    f'.gpv-gamma ul{{display:flex;align-items:flex-end;gap:16px;margin:0!important;padding:0!important;list-style:none;'
    f'background:linear-gradient({GRAFITE},{GRAFITE}) left bottom 26px/100% 1px no-repeat}}'
    '.gpv-gamma li{flex:var(--l) 1 0px;min-width:0;margin:0!important;padding:0!important;border:0!important;list-style:none;'
    'display:flex;align-items:flex-end}'
    '.gpv-gamma button,.gpv-gamma button:hover,.gpv-gamma button:focus{display:block;width:100%;margin:0;padding:0!important;'
    f'border:0!important;border-radius:0!important;background:none!important;box-shadow:none!important;color:{GRAFITE}!important;'
    'cursor:pointer;text-align:center;font:inherit}'
    f'.gpv-gamma .gpv-v{{display:block;width:100%;aspect-ratio:var(--l)/var(--h);border:1px solid {GRAFITE};background:{CLS};'
    'box-sizing:border-box;transition:background-color .15s}'
    f".gpv-gamma .gpv-vol{{display:block;height:16px;margin-top:10px;font:400 12px/16px '{MONO}',monospace;color:{TESTO2};"
    'font-variant-numeric:tabular-nums;white-space:nowrap}'
    f'.gpv-gamma button[aria-pressed=true] .gpv-v{{background:{ARANCIO}}}'
    f'.gpv-gamma button[aria-pressed=true] .gpv-vol{{color:{GRAFITE};font-weight:500}}'
    f'@media (hover:hover){{.gpv-gamma.gpv-js button:hover .gpv-v{{background:{EVIDENZA}}}'
    f'.gpv-gamma.gpv-js button[aria-pressed=true]:hover .gpv-v{{background:{ARANCIO}}}}}'
    '.gpv-gamma:not(.gpv-js) button{cursor:default}'
    f'.gpv-gamma button:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:3px}}'
    '.gpv-gamma-piede{display:flex;align-items:flex-start;gap:24px;margin-top:16px}'
    '.gpv-scala{flex:0 0 auto;width:calc((100% - 160px) * 500 / 6355)}'
    f'.gpv-scala i{{display:block;height:6px;border:1px solid {GRAFITE};box-sizing:border-box;'
    f'background:linear-gradient(90deg,{GRAFITE} 20%,#fff 20% 40%,{GRAFITE} 40% 60%,#fff 60% 80%,{GRAFITE} 80%)}}'
    f".gpv-scala b{{display:block;margin-top:6px;font:500 12px/1 '{MONO}',monospace;color:{GRAFITE};white-space:nowrap}}"
    f".gpv-gamma-nota{{margin:0!important;font:400 12px/1.5 '{MONO}',monospace;letter-spacing:.7px;text-transform:uppercase;"
    f'color:{TESTO2};text-wrap:pretty}}'
    '.gpv-gamma:not(.gpv-js) .gpv-gamma-js{display:none}'
    '.gpv-lettura{margin-top:32px}'
    f".gpv-lett-m{{margin:0!important;font:600 56px/1 '{ARCHIVO}',Arial,sans-serif;letter-spacing:-1.1px;color:{GRAFITE}}}"
    f".gpv-lett-m span{{font:400 14px/1 '{MONO}',monospace;letter-spacing:0;color:{TESTO2};margin-left:8px}}"
    f".gpv-lett-d{{margin:16px 0 0!important;font:400 14px/1.6 '{MONO}',monospace;color:{GRAFITE}}}"
    f'.gpv-lett-d .gpv-sep{{color:{TESTO2};margin:0 10px}}.gpv-lett-d .gpv-lab{{margin-right:8px}}'
    '@media (max-width:1024px){.gpv-lett-m{font-size:44px}}'
    '@media (max-width:767px){.gpv-gamma ul{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 16px;'
    'background:none}'
    f'.gpv-gamma li{{background:linear-gradient({GRAFITE},{GRAFITE}) left bottom 26px/100% 1px no-repeat}}'
    '.gpv-gamma .gpv-v{width:calc(var(--l) / 1050 * 100%)}.gpv-gamma button{text-align:left}'
    '.gpv-scala{width:calc((100% - 32px) / 3 * 500 / 1050)}.gpv-gamma-piede{gap:16px}'
    '.gpv-lett-m{font-size:30px;letter-spacing:-.6px}.gpv-lett-m b{display:block}.gpv-lett-m span{margin-left:0}'
    '.gpv-lett-d .gpv-sep{display:block;height:0;overflow:hidden}}'
)

JS_GAMMA = (
    "<script>(function(){function go(){document.querySelectorAll('.gpv-gamma').forEach(function(g){"
    "if(g.dataset.ok)return;g.dataset.ok=1;g.classList.add('gpv-js');"
    "var bs=[].slice.call(g.querySelectorAll('button[data-i]')),t=document.getElementById(g.getAttribute('data-tab')),"
    "rs=t?[].slice.call(t.querySelectorAll('tbody tr')):[],m=g.querySelector('.gpv-lett-m b'),"
    "v=g.querySelector('[data-k=v]'),c=g.querySelector('[data-k=c]'),o=g.querySelector('[data-k=o]'),"
    "hov=window.matchMedia&&matchMedia('(hover:hover)').matches;"
    "function sc(i){bs.forEach(function(b,k){b.setAttribute('aria-pressed',k===i?'true':'false');"
    "b.setAttribute('tabindex',k===i?'0':'-1')});rs.forEach(function(r,k){r.classList.toggle('gpv-evid',k===i)});"
    "var b=bs[i];m.textContent=b.dataset.m;v.textContent=b.dataset.v;c.textContent=b.dataset.c;o.textContent=b.dataset.o}"
    "bs.forEach(function(b,k){b.addEventListener('click',function(){sc(k)});"
    "if(hov)b.addEventListener('mouseenter',function(){sc(k)});"
    "b.addEventListener('keydown',function(e){var n=e.key==='ArrowRight'?k+1:e.key==='ArrowLeft'?k-1:e.key==='Home'?0:"
    "e.key==='End'?bs.length-1:-1;if(n<0||n>=bs.length)return;e.preventDefault();bs[n].focus();sc(n)})});"
    "sc(bs.length-1)})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();</script>"
)


def gamma_vasche():
    """Dinamica 1: le 11 vasche disegnate di lato nella stessa scala; scegliere una vasca aggiorna la lettura e la riga
    della tabella. Geometria senza JavaScript (flex-grow = lunghezza, aspect-ratio = lunghezza/altezza)."""
    voci = []
    for i, riga in enumerate(RETT):
        lung, _, alt = _misure(riga[0])
        mis, peso, cop, vol = _lettura(riga)
        scelta = i == len(RETT) - 1
        voci.append(
            f'<li style="--l:{lung};--h:{alt}"><button type="button" data-i="{i}" aria-pressed="{"true" if scelta else "false"}" '
            f'aria-label="Vasca {mis}, {riga[3]} mc" data-m="{mis}" data-v="{peso}" data-c="{cop}" data-o="{vol}">'
            f'<span class="gpv-v" aria-hidden="true"></span><span class="gpv-vol" aria-hidden="true">{riga[3]}</span></button></li>')
    mis, peso, cop, vol = _lettura(RETT[-1])
    html = (f'<div class="gpv-gamma" data-tab="gpv-tab-rett"><ul aria-label="Vasche rettangolari disegnate in scala">'
            + ''.join(voci) + '</ul>'
            '<div class="gpv-gamma-piede"><span class="gpv-scala" aria-hidden="true"><i></i><b>5 m</b></span>'
            '<p class="gpv-gamma-nota">Vasche disegnate in scala, viste di lato.<span class="gpv-gamma-js"> Toccate una vasca '
            'per leggerne le misure.</span></p></div>'
            f'<div class="gpv-lettura" aria-live="polite"><p class="gpv-lett-m"><b>{mis}</b><span>cm</span></p>'
            f'<p class="gpv-lett-d"><span class="gpv-lab">Vasca</span><span data-k="v">{peso}</span><span class="gpv-sep">·</span>'
            f'<span class="gpv-lab">Coperchio</span><span data-k="c">{cop}</span><span class="gpv-sep">·</span>'
            f'<span class="gpv-lab">Volume</span><span data-k="o">{vol}</span></p></div></div>')
    return RAW(html + JS_GAMMA, css=CSS_GAMMA)


def vasche_rettangolari():
    """V2: la gamma delle 11 vasche in scala sceglie la riga della tabella; accanto la 1050 vera, in posa."""
    tabella_html = tab('rettangolari', 'Vasche rettangolari', evidenzia=(len(RETT) - 1, 'IN FOTO'))
    tabella_html = tabella_html.replace('<table class=', '<table id="gpv-tab-rett" class=', 1)
    foto = C(
        I(img('vasca-1050-posa.jpg'), 'Vasca rettangolare lunga sollevata dall’autogru sopra lo scavo, due operai a terra '
          'guidano il carico'),
        didascalia('Vasca 1050 in posa con autogru'),
        T(f'<p>1050×243×263{NBSP}h · 27,00{NBSP}t · 50,00{NBSP}mc</p>', style='mono', color=GRAFITE),
        w=w(4, 5), gap='xs')
    return sezione(
        capo('Vasche rettangolari', '11 misure · misure esterne in cm'),
        H('Dalla 205 alla 1050: fino a 50 metri cubi in un pezzo solo.', 'h2'),
        C(gamma_vasche(), mt='l'),
        C(foto, C(RAW(tabella_html), w=w(8, 7)), dir='row', dir_m='column', justify='between', align='start',
          gap=('col', 'col', 'l'), mt='l'),
        pad=(0, 'lato', 'sezione', 'lato'), anchor='rettangolari')


def vasche_circolari():
    """V3: tre diametri, due altezze; il render sul grigio e la tabella."""
    render = C(I(img('render-vasca-circolare-cls.jpg'), 'Render della vasca circolare monoblocco con il coperchio',
                 w_img=(260, 260, 220), fisso=True),
               didascalia('Vasca circolare con coperchio'),
               w=w(4, 5), gap='s', align='start')
    destra = C(
        H('Tre diametri, due altezze.', 'h2'),
        testo('<p>Le vasche prefabbricate di tipo monolitico sono realizzate in calcestruzzo armato vibrato in cassero '
              'tramite vibratore ad immersione ad alta frequenza.</p>', color=TESTO2, mt='m'),
        C(RAW(tab('circolari', 'Vasche circolari')), mt='l'),
        w=w(8, 7), gap='0')
    return sezione(
        capo('Vasche circolari', f'6 misure · Ø{NBSP}148, 196 e 242{NBSP}cm'),
        C(render, destra, dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        bg=CLS, anchor='circolari')


CSS_DETTAGLI = (
    '.gpv-dettagli summary{list-style:none;cursor:pointer;display:inline-flex;align-items:center;gap:12px;padding:10px 0;'
    f"font:600 15px/1.4 '{ARCHIVO}',Arial,sans-serif;color:{ARANCIO_SCURO}}}"
    '.gpv-dettagli summary span{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px}'
    '.gpv-dettagli summary::-webkit-details-marker{display:none}'
    f".gpv-dettagli summary::after{{content:'+';font:500 16px/1 '{MONO}',monospace;"
    f'display:inline-block;width:20px;height:20px;line-height:18px;text-align:center;border:1px solid currentColor}}'
    ".gpv-dettagli[open] summary::after{content:'\\2212'}"
    f'.gpv-dettagli summary:hover{{color:{GRAFITE}}}'
    '.gpv-dettagli .gpv-dettagli-c{padding-top:16px}'
    f'.gpv-scuro .gpv-dettagli summary{{color:{BIANCO}}}.gpv-scuro .gpv-dettagli summary:hover{{color:{ARANCIO}}}'
    f'.gpv-scuro .gpv-dettagli .gpv-tab-note{{color:{SU_GRAFITE2}}}'
)


def dettagli(sommario, contenuto, **p):
    """Dinamica 8: <details> nativo, nessun JavaScript; sommario con il segno + e il segno meno in monospazio."""
    return RAW(f'<details class="gpv-dettagli"><summary><span>{sommario}</span></summary>'
               f'<div class="gpv-dettagli-c">{contenuto}</div></details>', css=CSS_DETTAGLI, **p)


def vasche_resine():
    """V4: l'unico colore pieno del materiale, il rosso della resina, su grafite. Foto in due misure, allineate in alto."""
    righe_tab = tab('resine', 'Vasche trattate con resine epossidiche', scura=True)
    foto1 = C(I(img('resina-circolare.jpg'), 'Interno di una vasca circolare trattato con resina epossidica rossa, '
                'visto dall’alto', css='gpv-ar169-t'),
              didascalia('Vasca circolare, interno in resina epossidica', colore=SU_GRAFITE2),
              w=(W[5], W[6], 100), gap='xs')
    foto2 = C(I(img('resina-rettangolare.jpg'), 'Interno di una vasca rettangolare trattato con resina epossidica rossa',
                css='gpv-ar169-t'),
              didascalia('Vasca rettangolare, interno in resina epossidica', colore=SU_GRAFITE2),
              w=(W[3], W[6], 100), gap='xs', hide=['mobile'])
    testo_col = C(
        H('Le stesse vasche, con l’interno trattato.', 'h2', color=BIANCO),
        T(f'<p>Circolari e rettangolari da 250{NBSP}×{NBSP}240 in su: le stesse misure, pesi e volumi della tabella, da '
          f'2,30 a 50{NBSP}mc.</p>', style='body', color=SU_GRAFITE2, mt='m'),
        dettagli('Le 15 misure', righe_tab, mt='m'),
        w=(W[4], 100, 100), gap='0')
    return sezione(
        capo('Vasche trattate con resine epossidiche', '15 misure', scuro=True),
        C(foto1, foto2, testo_col, dir='row', dir_m='column', wrap=(False, True, False), justify='between', align='start',
          gap=('col', 'col', 'l'), gap_r=('col', 'l', 'l')),
        bg=GRAFITE, anchor='resine', css='gpv-scuro')


def vasche_calcestruzzo():
    """V5: il materiale delle vasche, parola per parola, e la tabella delle classi di esposizione."""
    classi = tabella_voci([
        ('XC4', 'Corrosione delle armature indotta da carbonatazione'),
        ('XS1-XD2', 'Corrosione delle armature indotta da cloruri, anche di provenienza marina'),
        ('XF1', 'Cicli di gelo e disgelo, con o senza disgelanti'),
        ('XA2', 'Ambienti chimici aggressivi nel suolo naturale e nell’acqua presente nel terreno'),
    ], 'Classi di esposizione').replace('gpv-tab-voci', 'gpv-tab-voci gpv-voci-corte', 1)
    return sezione(
        capo('Calcestruzzo e armature', 'UNI EN 206-1 · D.M. 17.01.2018'),
        C(C(testo('<p>Le vasche sono gettate in cassero e vibrate con vibratore ad immersione ad alta frequenza, in '
                  'calcestruzzo di classe di resistenza a compressione C35/45 (Rck 45 N/mm²), conforme alla norma UNI EN 206-1 '
                  'e alle normative antisismiche (D.M. 14.01.2008 e D.M. 17.01.2018, Norme Tecniche per le Costruzioni).</p>'
                  '<p>Le armature interne sono in acciaio ad aderenza migliorata B450C.</p>'),
            w=w(6)),
          C(etichetta('Classi di esposizione', mb='s'), RAW(classi), w=w(6), gap='0'),
          dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        anchor='calcestruzzo-vasche')


def vasche():
    return [('apertura', vasche_apertura()), ('rettangolari', vasche_rettangolari()), ('circolari', vasche_circolari()),
            ('resine', vasche_resine()), ('calcestruzzo', vasche_calcestruzzo()),
            ('ufficio-tecnico', ufficio_tecnico(bg=CLS, nota='Ufficio tecnico'))]


# ---------------------------------------------------------------------------------------------
# 03 DEPURAZIONE (spec §8)
# ---------------------------------------------------------------------------------------------
CHIUSURA_UT = 'Per portate superiori contattare il nostro ufficio tecnico'
SCHEDE_DEP = [('01', 'Dissabbiatore statico', 'dissabbiatore'), ('02', 'Separatore grassi', 'separatore-grassi'),
              ('03', 'Vasca Imhoff', 'imhoff'), ('04', 'Separatore oli con filtro a coalescenza', 'separatore-oli'),
              ('05', 'Separatore oli per autorimesse e garage', 'separatore-oli-autorimesse'),
              ('06', 'Impianti di prima pioggia', 'prima-pioggia'), ('07', 'Depuratori biologici', 'depuratori-biologici')]


def depurazione_apertura():
    """D1: un indice numerato da catalogo e una foto vera di cantiere."""
    foto = 'depurazione-vasca-pozzetto.jpg'
    alt = 'Vasca rettangolare lunga con la soletta e un pozzetto circolare posati nello scavo di un cantiere'
    righe = []
    for i, (cod, nome, ancora) in enumerate(SCHEDE_DEP):
        righe.append(C(
            H(f'<span class="gpv-cod">{cod}</span>{nome}', 'p', style='h4', color=GRAFITE, css='gpv-nome'),
            T('<p><span class="gpv-freccia" aria-hidden="true">→</span></p>', style='label', color=TESTO2, fisso=True),
            dir='row', justify='between', align='center', gap='s', min_h=48, pad=(12, 0), border_bottom=1,
            border_color=LINEA, link=f'#{ancora}', w=(47.5, 47.5, 100), css=f'gpv-riga gpv-ind-{i + 1}'))
    css = (f'.gpv-indice-n>.gpv-ind-1,.gpv-indice-n>.gpv-ind-2{{border-top:1px solid {GRAFITE}!important}}'
           f'@media (max-width:767px){{.gpv-indice-n>.gpv-ind-2{{border-top:0!important}}}}'
           '.gpv-indice-n .gpv-cod{font-size:14px}')
    sinistra = C(
        etichetta('Depurazione'),
        H('Separatori, Imhoff, prima pioggia e depuratori biologici in calcestruzzo.', 'h1', mt=24),
        I(img(foto), alt, hide=['desktop', 'tablet'], mt='m'),
        testo('<p>Manufatti per il trattamento dei reflui domestici, industriali e delle acque meteoriche. Ogni impianto '
              'ha la sua tabella; per portate superiori risponde il nostro ufficio tecnico.</p>', style='lead',
              color=TESTO2, mt='m'),
        C(*righe, RAW('', css=css), dir='row', wrap=True, justify='between', gap='col', gap_r=0, mt='l',
          css='gpv-indice-n'),
        w=w(7), gap='0')
    destra = figura(foto, alt, 'Vasca rettangolare e pozzetto circolare in cantiere', w=w(5), hide=['mobile'])
    return sezione(
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap='col'),
        pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')


def render_box(nome_img, alt, pct, didascalia_txt=None, **p):
    """Render (o foto) a una frazione della colonna, centrato: pct = (desktop, tablet, mobile) in %."""
    figli = [I(img(nome_img), alt)]
    if didascalia_txt:
        figli.append(didascalia(didascalia_txt))
    return C(*figli, w=pct, gap='xs', **p)


def chiusura_ut(**p):
    return C(etichetta(CHIUSURA_UT),
             link_freccia('Scrivete all’ufficio tecnico', RICHIESTA, mt='xs'),
             gap='0', **p)


def scheda(ancora, codice, nome, nota, immagine, corpo, bg=BIANCO, lato='sx', titolo=None):
    """Scheda d'impianto: capo con codice e nome, render da un lato, dall'altro titolo, testo, tabella.
    Al telefono: titolo, immagine, testo, tabella."""
    titolo = titolo or nome
    img_col = C(*immagine, w=w(5), gap='m', align='center', css='gpv-sticky')
    testo_col = C(H(titolo, 'h2', hide=['mobile']), *corpo, w=w(7), gap='0')
    figli = (img_col, testo_col) if lato == 'sx' else (testo_col, img_col)
    return sezione(
        capo_scheda(codice, nome, nota),
        H(titolo, 'h2', hide=['desktop', 'tablet'], mb='m'),
        C(*figli, dir='row', dir_m='column' if lato == 'sx' else 'column-reverse', justify='between', align='start',
          gap=('col', 'col', 'l')),
        bg=bg, anchor=ancora, pad=('xl', 'lato'))


CSS_TAB = (
    '.gpv-tab-l{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 24px}'
    '.gpv-tab-l button,.gpv-tab-l button:focus{margin:0;min-height:44px;padding:12px 16px!important;'
    f'border:1px solid {GRAFITE}!important;border-radius:0!important;background:transparent!important;color:{GRAFITE}!important;'
    f"font:500 12px/1.4 '{MONO}',monospace!important;letter-spacing:1px;text-transform:uppercase;cursor:pointer;"
    'box-shadow:none!important;transition:background-color .15s,color .15s}'
    '.gpv-tab-l button[aria-selected=true],.gpv-tab-l button:hover,.gpv-tab-l button[aria-selected=true]:focus'
    f'{{background:{GRAFITE}!important;color:{BIANCO}!important}}'
    f'.gpv-tab-l button:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:2px}}'
    f".gpv-tab-t{{margin:0 0 12px!important;font:500 12px/1.4 '{MONO}',monospace;letter-spacing:1px;text-transform:uppercase;"
    f'color:{GRAFITE}}}'
    '.gpv-tab.gpv-js .gpv-tab-t{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);'
    'white-space:nowrap}'
    '.gpv-tab:not(.gpv-js) .gpv-tab-l{display:none}'
    '.gpv-tab:not(.gpv-js) [role=tabpanel][hidden]{display:block}'
    '.gpv-tab:not(.gpv-js) [role=tabpanel]+[role=tabpanel]{margin-top:40px}'
    f'.gpv-tab [role=tabpanel]:focus-visible{{outline:2px solid {ARANCIO_SCURO};outline-offset:4px}}'
    '@media (max-width:767px){.gpv-tab-l{display:grid;grid-template-columns:1fr 1fr}'
    '.gpv-tab-l button,.gpv-tab-l button:focus{padding:10px 8px!important;letter-spacing:.5px}}'
)

JS_TAB = (
    "<script>(function(){function go(){document.querySelectorAll('.gpv-tab').forEach(function(w){"
    "if(w.dataset.ok)return;w.dataset.ok=1;w.classList.add('gpv-js');"
    "var ts=[].slice.call(w.querySelectorAll('[role=tab]'));"
    "function sel(i,f){ts.forEach(function(t,k){var on=k===i;t.setAttribute('aria-selected',on?'true':'false');"
    "t.setAttribute('tabindex',on?'0':'-1');document.getElementById(t.getAttribute('aria-controls')).hidden=!on});"
    "if(f)ts[i].focus()}"
    "ts.forEach(function(t,k){t.addEventListener('click',function(){sel(k)});"
    "t.addEventListener('keydown',function(e){var n=e.key==='ArrowRight'?(k+1)%ts.length:e.key==='ArrowLeft'?"
    "(k-1+ts.length)%ts.length:e.key==='Home'?0:e.key==='End'?ts.length-1:-1;if(n<0)return;e.preventDefault();sel(n,true)})})"
    "})}if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();</script>"
)


def tabelle_a_schede(nome, prefisso, titolo):
    """Dinamica 2: due tabelle a schede (acque superficiali, Laguna di Venezia). Senza JavaScript si vedono tutte e due,
    una sotto l'altra, ciascuna col suo titolo."""
    t = TABELLE[nome]
    bottoni, pannelli = [], []
    for k, sch in enumerate(t['schede']):
        tid, pid = f'gpv-t-{prefisso}-{k + 1}', f'gpv-p-{prefisso}-{k + 1}'
        breve = 'Acque superficiali' if 'superficiali' in sch['nome'] else sch['nome']
        sel = 'true' if k == 0 else 'false'
        ti = '' if k == 0 else ' tabindex="-1"'
        nascosto = '' if k == 0 else ' hidden'
        bottoni.append(f'<button type="button" role="tab" id="{tid}" aria-controls="{pid}" aria-selected="{sel}"{ti}>'
                       f'{breve}</button>')
        tabella_html = tabella(t['colonne'], [[_cella(c) for c in r] for r in sch['righe']], f'{titolo}, {sch["nome"]}',
                               note=[sch['nota'] + '.'])
        pannelli.append(f'<div role="tabpanel" id="{pid}" aria-labelledby="{tid}" tabindex="0"{nascosto}>'
                        f'<p class="gpv-tab-t">{sch["nome"]}</p>{tabella_html}</div>')
    html = (f'<div class="gpv-tab"><div class="gpv-tab-l" role="tablist" aria-label="Recapito dello scarico">'
            f'{"".join(bottoni)}</div>{"".join(pannelli)}</div>')
    return RAW(html + JS_TAB, css=CSS_TAB)


def dep_dissabbiatore():
    return scheda(
        'dissabbiatore', '01', 'Dissabbiatore statico', '15 misure',
        [render_box('render-dissabbiatore-cls.jpg', 'Render in sezione del dissabbiatore statico rettangolare, con il '
                    'deflettore all’ingresso e il fango depositato sul fondo', (100, 100, 100))],
        [testo('<p>I dissabbiatori sono costituiti da una vasca monolitica a tenuta idraulica circolare o rettangolare, '
               'corredata all’interno di un deflettore in pvc posto nel foro d’ingresso che rallenta il flusso dell’acqua. '
               'Qui il materiale pesante, fanghi e sabbie, si deposita sul fondo, lasciando defluire l’acqua e i liquidi '
               'leggeri verso l’uscita.</p>', color=TESTO2, mt='m'),
         dettagli('Le 15 misure, circolari e rettangolari', tab('dissabbiatore', 'Dissabbiatore statico'), mt='m')],
        bg=CLS)


def dep_separatore_grassi():
    voci = ['Cucine per ristorazione collettiva e grandi stabilimenti di fornitura di pasti, per esempio alberghi, locande, '
            'stazioni di servizio in autostrada, mense',
            'Impianti per grigliare, arrostire e friggere',
            'Punti di distribuzione alimenti, con stoviglie a rendere',
            'Macellerie, con o senza impianti di macellazione',
            'Stabilimenti di lavorazione carni e salumifici, con o senza impianti di macellazione',
            'Impianti di macellazione pollame, di preparazione fast-food, di produzione di patate e patatine fritte, di '
            'tostatura arachidi']
    return scheda(
        'separatore-grassi', '02', 'Separatore grassi', 'UNI EN 1825-1:2005',
        [render_box('render-separatore-grassi.jpg', 'Render in sezione del separatore grassi circolare con la parete '
                    'divisoria centrale', (58, 67, 64))],
        [testo('<p>I separatori grassi monoblocco prefabbricati, costruiti secondo la norma europea UNI EN 1825-1:2005, si '
               'usano ogni volta che serve separare grassi e oli di origine vegetale e animale dalle acque reflue di:</p>',
               color=TESTO2, mt='m'),
         elenco_righe(voci, mt='s'),
         testo('<p>Sono compresi fori di entrata e uscita, raccordi in pvc con guarnizioni in gomma elastomerica sigillati a '
               'tenuta idraulica, deflettori di calma in pvc, parete divisoria centrale e paratie in acciaio inox per il '
               'controllo del flusso. Le dimensioni nominali sono stabilite con il criterio costruttivo del punto 5.5.3 '
               'lettera b) della norma.</p>', color=TESTO2, mt='m'),
         C(RAW(tab('separatore-grassi', 'Separatore grassi')), mt='l'),
         chiusura_ut(mt='l')],
        lato='dx')


def dep_imhoff():
    return scheda(
        'imhoff', '03', 'Vasca Imhoff', 'Da 5 a 70 abitanti equivalenti',
        [render_box('render-imhoff-cls.jpg', 'Render in sezione della vasca Imhoff rettangolare, con il comparto di '
                    'sedimentazione sopra quello di digestione', (82, 100, 88))],
        [testo('<p>La fossa biologica Imhoff prefabbricata si usa generalmente come impianto di trattamento primario delle '
               'acque reflue domestiche o assimilate, nei piccoli e medi impianti di depurazione: separa i materiali '
               'grossolani e fa una prima depurazione delle acque nere, quelle dei servizi igienici.</p>', color=TESTO2,
               mt='m'),
         C(riga_dato('Comparto superiore · sedimentazione',
                     T('<p>Trattiene i corpi solidi e manda il materiale sedimentato al comparto inferiore.</p>',
                       style='small', color=GRAFITE), larg=240, linea=LINEA_CLS),
           riga_dato('Comparto inferiore · digestione',
                     T('<p>Raccoglie per caduta i fanghi, che subiscono la digestione anaerobica e si ispessiscono. Il gas '
                       'biologico esce dalla tubazione di ventilazione in alto.</p>', style='small', color=GRAFITE),
                     larg=240, linea=LINEA_CLS),
           gap='0', border_top=1, border_color=GRAFITE, mt='m'),
         C(RAW(tab('imhoff', 'Vasca Imhoff')), mt='l'),
         chiusura_ut(mt='l')],
        bg=CLS)


def dep_separatore_oli():
    return scheda(
        'separatore-oli', '04', 'Separatore oli con filtro a coalescenza', 'Superfici scoperte',
        [render_box('separatore-oli-interno.jpg', 'Interno azzurro di un separatore oli circolare visto dall’alto, con il '
                    'filtro a coalescenza cilindrico', (100, 100, 100), 'Separatore oli, interno visto dall’alto'),
         render_box('render-separatore-oli.jpg', 'Render in sezione del separatore oli rettangolare con il filtro a '
                    'coalescenza', (47, 60, 58))],
        [testo('<p>I separatori oli monoblocco prefabbricati, con filtro a coalescenza e dispositivo di chiusura '
               'automatica, raccolgono le acque inquinate dal dilavamento dei piazzali di officine meccaniche, stazioni di '
               'rifornimento carburante, autolavaggi e autodemolizioni.</p>', color=TESTO2, mt='m'),
         C(RAW(tab('separatore-oli', 'Separatore oli con filtro a coalescenza')), mt='l'),
         chiusura_ut(mt='l')],
        lato='dx')


def dep_autorimesse():
    return scheda(
        'separatore-oli-autorimesse', '05', 'Separatore oli per autorimesse e garage', 'D.M. 01/02/1986',
        [render_box('render-separatore-oli-autorimesse-cls.jpg', 'Render in sezione del separatore oli per autorimesse, con '
                    'il filtro a coalescenza in acciaio inox', (82, 100, 88))],
        [testo('<p>Raccoglie le acque inquinate dalle eventuali perdite d’olio e idrocarburi delle auto in sosta durante il '
               'lavaggio di pavimenti e rampe d’accesso, ed è completo di filtro a coalescenza in acciaio inox.</p>'
               '<p>Tratta le acque da idrocarburi come previsto dal D.Lgs. 152/2006, entro i limiti della Tabella 3, '
               'Allegato 5 per lo scarico in acque superficiali e del D.M. 30/07/1999 per le acque che recapitano nella '
               'Laguna di Venezia. È conforme al D.M. 01/02/1986, “Norme di sicurezza antincendio per la costruzione e '
               'l’esercizio di autorimesse e simili”.</p>', color=TESTO2, mt='m'),
         C(tabelle_a_schede('separatore-oli-autorimesse', 'aut', 'Separatore oli per autorimesse'), mt='l')],
        bg=CLS)


def dep_prima_pioggia():
    """D7: variazione di forma, il render lungo va sopra a sinistra, i tre passaggi in fila, la tabella intera."""
    tabella_html = tab('prima-pioggia', 'Impianti di prima pioggia', note=False)
    tabella_html = (f'<div class="gpv-tab-scorre" tabindex="0" role="region" aria-label="Impianti di prima pioggia">'
                    f'{tabella_html}</div>')
    passi = [('Pozzetto scolmatore', 'Separa le acque di prima pioggia da quelle di seconda pioggia, con una tubazione '
              'd’ingresso e due d’uscita ad altezze diverse.'),
             ('Accumulo, 48 ore', 'L’acqua di prima pioggia resta nelle vasche di accumulo per 48 ore: il materiale pesante '
              'si deposita sul fondo. Allo scadere, un’elettropompa sommergibile alimenta a portata costante la '
              'disoleazione.'),
             ('Separatore oli', f'Costruito secondo la UNI EN 858-1, con filtro a coalescenza e valvola di occlusione. In '
              f'uscita oli minerali e idrocarburi non oltre 5{NBSP}mg/litro.')]
    tre = C(*[C(etichetta(t, colore=ARANCIO_SCURO), T(f'<p>{d}</p>', style='small', color=GRAFITE),
                gap='xs', w=(W[4], W[4], 100), border_top=1, border_color=GRAFITE, pad=(16, 0, 0, 0)) for t, d in passi],
            dir='row', dir_m='column', justify='between', gap=('col', 'col', 'm'), mt='xl')
    return sezione(
        capo_scheda('06', 'Impianti di prima pioggia', f'Da 400 a 10.000{NBSP}mq'),
        H('Impianti di prima pioggia', 'h2', hide=['desktop', 'tablet'], mb='m'),
        C(render_box('render-prima-pioggia.jpg', 'Render in sezione dell’impianto di prima pioggia: pozzetto scolmatore, '
                     'vasca di accumulo con elettropompa, separatore oli e pozzetto di prelievo', (W[7], W[6], 100)),
          C(H('Impianti di prima pioggia', 'h2', hide=['mobile']),
            testo('<p>Vengono considerate acque di prima pioggia “quelle corrispondenti per ogni evento meteorico ad una '
                  'precipitazione di 5 mm uniformemente distribuita sull’intera superficie scolante servita dalla rete di '
                  'drenaggio”.</p>', color=TESTO2, mt='m'),
            w=w(5, 6), gap='0'),
          dir='row', dir_m='column', justify='between', align='center', gap=('col', 'col', 'l')),
        tre,
        C(RAW(tabella_html), mt='xl'),
        chiusura_ut(mt='l'),
        pad=('xl', 'lato'), anchor='prima-pioggia')


def dep_biologici():
    return scheda(
        'depuratori-biologici', '07', 'Depuratori biologici', 'Ossidazione totale a fanghi attivi',
        [render_box('render-depuratore-biologico-cls.jpg', 'Render in sezione del depuratore biologico a ossidazione '
                    'totale, con il compressore nel quadro sopra la vasca', (78, 100, 88))],
        [testo('<p>Gli impianti di depurazione biologica ad ossidazione totale a fanghi attivi trattano le acque reflue di '
               'case sparse, lottizzazioni private, campeggi, villaggi turistici, ristoranti, ospedali, scuole e altre '
               'attività non servite da rete fognaria. Sono escluse dal trattamento le acque di attività artigianali e le '
               'acque piovane.</p><p>La digestione aerobica non produce odori molesti e il livello di rumorosità è '
               'contenuto entro limiti accettabili.</p>', color=TESTO2, mt='m'),
         C(tabelle_a_schede('depuratori-biologici', 'bio', 'Depuratori biologici'), mt='l'),
         chiusura_ut(mt='l')],
        bg=CLS, lato='dx', titolo='Depuratori biologici a ossidazione totale')


def depurazione():
    return [('apertura', depurazione_apertura()), ('dissabbiatore', dep_dissabbiatore()),
            ('separatore-grassi', dep_separatore_grassi()), ('imhoff', dep_imhoff()),
            ('separatore-oli', dep_separatore_oli()), ('autorimesse', dep_autorimesse()),
            ('prima-pioggia', dep_prima_pioggia()), ('biologici', dep_biologici()),
            ('ufficio-tecnico', ufficio_tecnico(bg=BIANCO))]


# ---------------------------------------------------------------------------------------------
# 04 PIATTAFORME PER AUTOLAVAGGI (spec §9)
# ---------------------------------------------------------------------------------------------
CANTIERI = json.load(open(os.path.join(QUI, 'dati', 'cantieri.json'), encoding='utf-8'))
for _c in CANTIERI:
    _c['luogo'] = _c['luogo'].replace("'", '’')
    _c['regione'] = _c['regione'].replace("'", '’')
CANTIERE = {c['id']: c for c in CANTIERI}
SIGLA_PAESE = {'CH': 'Svizzera', 'SK': 'Slovacchia', 'FR': 'Francia', 'RSM': 'San Marino'}


def piattaforme_apertura():
    """P1: la pista vera sotto le spazzole, a filo del bordo sinistro."""
    foto = 'pista-self-spazzole.jpg'
    alt = ('Pista di lavaggio prefabbricata sotto le spazzole di un portale: superficie antiscivolo a rombi e grigliato '
           'verde in vetroresina')
    foto_col = C(I(img(foto), alt, css='gpv-ar43 gpv-ar169-t'),
                 C(didascalia('Pista con grigliato in vetroresina e superficie antiscivolo'), pad=(0, 0, 0, 'lato'),
                   css='gpv-did-filo'),
                 w=(50, 100, 100), gap='xs', hide=['mobile'])
    testo_col = C(
        etichetta('Piattaforme per autolavaggi'),
        H('La pista di lavaggio arriva in pannelli e si posa in poche ore.', 'h1', mt=24),
        I(img(foto), alt, hide=['desktop', 'tablet'], css='gpv-filo-m gpv-ar43', mt='m'),
        testo('<p>Le nuove piattaforme prefabbricate Gardens Pav sono state progettate per essere utilizzate come '
              'pavimentazione per autolavaggi: si accostano contrapposti quattro pannelli per la postazione con portale e '
              'due pannelli per la pista self.</p>', style='lead', color=TESTO2, mt='m'),
        etichetta(f'Brevetto per invenzione industriale depositato n°{NBSP}275.271', colore=ARANCIO_SCURO, mt='m'),
        bottoni(B('Richiedi un’offerta', RICHIESTA, variant='primario', full_m=True),
                B('Gli otto modelli', '#modelli', variant='contorno', full_m=True), mt='l'),
        w=(50, 100, 100), gap='0', pad=(0, 'lato', 0, ('xl', 'lato', 'lato')), css='gpv-filo-dx')
    return sezione(foto_col, testo_col, dir='row', dir_t='column', align=('center', 'start', 'start'), boxed=False,
                   gap=(0, 'l', 0), pad=(('xl', 0, 48), 0, 'sezione', 0), anchor='content')


def piattaforme_caratteristiche():
    """P2: i cinque scopi scritti dall'azienda e la tabella d'attrito che oggi è chiusa in un'immagine."""
    scopi = ['pavimentazioni con la finitura adatta al deflusso dell’acqua e contro gli scivolamenti;',
             'pavimentazioni senza casseforme o strutture di contenimento;',
             'pavimentazioni senza deformazioni superficiali;',
             'calcestruzzo e armatura corretti e maturati senza sbalzi di temperatura e umidità;',
             'tempi di realizzazione ridotti: basta allestire il pozzetto centrale di scarico, gli scarichi e il sottofondo '
             'di appoggio, e i pannelli si posano in poche ore.']
    attrito = tabella(['Riferito a', 'Asciutto', 'Bagnato'],
                      [['Gomma 4S', '0,64', '0,88'], ['Cuoio', '0,64', '0,89'],
                       [f'Limite D.M. 236/1989, art.{NBSP}8.2.2', f'&gt;{NBSP}0,40', f'&gt;{NBSP}0,40']],
                      'Coefficiente di attrito', evidenzia=(2, ''))
    vantaggi = ['Tempi di costruzione ridotti', 'Prodotto standard, operativo anche il giorno della posa', 'Posa semplice',
                'Superficie che fa defluire l’acqua e tiene il piede anche bagnata',
                'Tubazioni predisposte per acque piovane, acque di lavaggio e cavi elettrici',
                f'Calcestruzzo da 45{NBSP}N/mm²']
    css = ('.gpv-elenco-2 ul{columns:2;column-gap:32px;border-top:0!important}'
           '.gpv-elenco-2 li{break-inside:avoid}'
           '@media (max-width:767px){.gpv-elenco-2 ul{columns:1}}')
    sinistra = C(
        H('Una pavimentazione solida, inclinata, che non scivola.', 'h2'),
        testo('<p>Gli autolavaggi self service richiedono una pavimentazione solida, su cui l’auto possa sostare, e inclinata '
              'per favorire il deflusso dell’acqua caduta o spruzzata. Le piattaforme sono state studiate per:</p>',
              color=TESTO2, mt='m'),
        elenco_righe(scopi, segno=True, mt='m'),
        w=w(6), gap='0')
    destra = C(
        C(H('Coefficiente di attrito medio della superficie', 'h3', style='h4'),
          C(RAW(attrito), mt='m'),
          bg=BIANCO, pad=('m', 'm', 'm', 'm'), gap='0'),
        C(etichetta('Vantaggi', mb='xs'), elenco_righe(vantaggi, css='gpv-elenco-2'), RAW('', css=css), gap='0', mt='l'),
        w=w(6), gap='0')
    return sezione(
        capo('Caratteristiche e vantaggi', f'D.M. 236 del 14/06/1989, art.{NBSP}8.2.2'),
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        bg=CLS, anchor='caratteristiche')


def piattaforme_tavola():
    """P3: la tavola della pista self 450, la stessa della home ma più grande e spiegata."""
    def riga_scura(lab, valore):
        return riga_dato(lab, T(f'<p>{valore}</p>', style='small', color=BIANCO), larg=150, linea=LINEA_SCURA,
                         col_lab=SU_GRAFITE2, pad_v=14)
    destra = C(
        riga_scura('Pianta', f'450{NBSP}×{NBSP}650{NBSP}cm'),
        riga_scura('Pannelli', f'2 pannelli a incastro da 228{NBSP}×{NBSP}650, spessi 20{NBSP}cm, 5,90{NBSP}t ciascuno'),
        riga_scura('Vasca di raccolta', f'in calcestruzzo armato, 400{NBSP}×{NBSP}100{NBSP}×{NBSP}110{NBSP}h{NBSP}cm'),
        riga_scura('Grigliato', f'in vetroresina anticorrosivo, superficie antiscivolo al quarzo, moduli 200{NBSP}×{NBSP}100, '
                                f'maglia 3,8{NBSP}×{NBSP}3,8{NBSP}×{NBSP}3,8{NBSP}h, verde'),
        riga_scura('Calcestruzzo', f'Rck 45{NBSP}N/mm²'),
        link_freccia('Esempio di posa', '#posa', scuro=True, mt='m'),
        w=w(4, 5), gap='0', border_top=1, border_color=LINEA_SCURA)
    return sezione(
        capo('Pista self Mod. 450', 'Pianta in cm', scuro=True),
        C(C(RAW(PIANTA_SVG, css=CSS_PIANTA), w=w(8, 7)), destra, dir='row', dir_m='column', justify='between',
          align='start', gap=('col', 'col', 'l')),
        bg=GRAFITE, css='gpv-scuro', anchor='tavola')


MODELLI_SCHEDE = [
    ('pista', 'mod-450', 'Pista self Mod. 450', 'schema-pista-self-450.jpg',
     f'450 × 650 cm · 2 pannelli 228 × 650 × 20 · 5,90 t l’uno · vasca 400 × 100 × 110 h'),
    ('pista', 'mod-500', 'Pista self Mod. 500', 'schema-pista-self-500.jpg',
     f'500 × 650 cm · 2 pannelli 253 × 650 × 20 · 6,70 t l’uno · vasca 400 × 100 × 110 h'),
    ('pista', 'mod-500-doppia-griglia', 'Pista self Mod. 500 doppia griglia', 'schema-pista-self-500-doppia-griglia.jpg',
     f'500 × 650 cm · 2 piastre 253 × 650 × 20 · 6,70 t l’una · vasche di raccolta 400 × 100 × 110 h'),
    ('portale', 'mod-1', 'Portale Mod. 1', 'schema-portale-mod1.jpg',
     f'500 × 1200 cm · 4 pannelli 253 × 600 × 20 · 6,70 t l’uno · vasca 400 × 100 × 110 h'),
    ('portale', 'mod-2', 'Portale Mod. 2', 'schema-portale-mod2.jpg',
     f'500 × 1100 cm · 4 pannelli 253 × 550 × 20 · 6,00 t l’uno · pozzetto di raccolta escluso'),
    ('portale', 'mod-3', 'Portale Mod. 3 lavaggio chassis', 'schema-portale-mod3.jpg',
     f'500 × 1200 cm · 4 pannelli 253 × 600 × 20 · 6,70 t l’uno · 2 vasche 400 × 100 × 110 h · grigliato nello spazio del '
     f'lavaggio chassis'),
    ('portale', 'mod-4', 'Portale Mod. 4 con area prelavaggio', 'schema-portale-mod4.jpg',
     f'500 × 1300/1800 cm · 6 pannelli a incastro, misure variabili, spessore 20 · Rck 45'),
    ('portale', 'mod-5', 'Portale Mod. 5', 'schema-portale-mod5.jpg',
     f'500 × 1300/1800 cm · 6 pannelli a incastro, misure variabili, spessore 20 · vasca 400 × 100 × 110 h'),
]


def _misura_unita(testo_m):
    """Spazi indivisibili attorno a × e prima delle unità: la misura non va a capo, la frase sì."""
    import re
    testo_m = testo_m.replace(' × ', f'{NBSP}×{NBSP}')
    return re.sub(r' (cm|h|t)\b', NBSP + r'\1', testo_m)


def scheda_modello(ancora, nome, disegno, dati, larghezze, gruppo):
    righe = '<br>'.join(_misura_unita(d) for d in dati.split(' · '))
    misura = dati.split(' · ')[0]
    alt = f'Disegno in pianta della piattaforma {nome}, {misura}'
    return C(
        C(I(img(disegno), alt, css=f'gpv-dis gpv-dis-{gruppo}'), w=(100, 100, 39.8)),
        C(H(nome.replace('Mod. ', f'Mod.{NBSP}'), 'h3', style='h3m', css='gpv-nome'),
          T(f'<p>{righe}</p>', style='mono13', color=GRAFITE), gap='xs', w=(100, 100, 55)),
        w=larghezze, dir='column', dir_m='row', gap=('s', 's', 's'), align='start', border_top=1, border_color=GRAFITE,
        pad=(16, 0, 0, 0), anchor=ancora)


def piattaforme_modelli():
    """P4: i disegni in pianta dell'azienda, ciascuno con i suoi numeri; il passo cambia a metà sezione."""
    pista = [scheda_modello(a, n, d, x, (W[4], W[4], 100), g) for g, a, n, d, x in MODELLI_SCHEDE if g == 'pista']
    portale = [scheda_modello(a, n, d, x, (17.9, W[4], 100), g) for g, a, n, d, x in MODELLI_SCHEDE if g == 'portale']
    css = ('@media (min-width:1025px){.gpv-h2-largo{max-width:843px}}'
           '.gpv-dis img{width:100%!important;height:auto!important;object-fit:contain;object-position:left center}'
           '.gpv-dis-pista img{aspect-ratio:61/31}.gpv-dis-portale img{aspect-ratio:2/1}')
    return sezione(
        capo('Modelli', 'Pista self 3 · portale 5'),
        H('Otto piattaforme, dalla pista self al portale con prelavaggio.', 'h2', mb='l', css='gpv-h2-largo'),
        etichetta('Pista self · 3 modelli', mb='s'),
        C(*pista, dir='row', dir_m='column', wrap=True, justify='start', gap='col', gap_r=('l', 'l', 'm')),
        T(f'<p>Dove il modello la prevede, la vasca di raccolta in calcestruzzo armato misura 400{NBSP}×{NBSP}100{NBSP}×{NBSP}'
          f'110{NBSP}h{NBSP}cm; il grigliato è in vetroresina verde con superficie antiscivolo al quarzo, maglia '
          f'3,8{NBSP}×{NBSP}3,8{NBSP}cm.</p>', style='small', color=TESTO2, mt='m', max_w=733),
        etichetta('Portale · 5 modelli', mb='s', mt='xl'),
        C(*portale, dir='row', dir_m='column', wrap=True, justify='start', gap='col', gap_r=('l', 'l', 'm')),
        RAW('', css=css),
        anchor='modelli')


def piattaforme_fornitura():
    """P5: cosa arriva in cantiere, e cosa resta all'impresa."""
    voci = [('01', 'La fascia in giuntoplasto adesivo per appoggiare i pannelli sul bordo della vasca'),
            ('02', 'Staffe e viti in acciaio inox per bloccare i pannelli'),
            ('03', 'Supporti porta grigliato in acciaio zincato'),
            ('04', 'Tubazioni predisposte nei pannelli per lo scarico di pluviali e lance e per i cavi elettrici'),
            ('05', 'Il disegno delle fasi prima della posa: tracciatura della piazzola, posa della vasca, cordoli '
                   'perimetrali, posa dei pannelli'),
            ('06', 'L’installazione in cantiere con il nostro personale'),
            ('07', 'Relazione strutturale, scheda tecnica e piano di manutenzione')]

    def blocchi(**p):
        return C(C(etichetta('Su richiesta'),
                   T('<p>Trasporto con automezzi, con o senza gru. Noleggio dell’autogru.</p>', style='small', color=GRAFITE),
                   gap='xs', border_top=1, border_color=GRAFITE, pad=(16, 0, 0, 0)),
                 C(etichetta('Escluso'),
                   T('<p>Opere edili in genere: scavo, sbancamento, piano di posa, cordolo perimetrale di appoggio e relative '
                     'relazioni di calcolo. Per il Portale Mod.&nbsp;2 anche il pozzetto di raccolta da installare sotto la '
                     'piattaforma.</p>', style='small', color=GRAFITE),
                   gap='xs', border_top=1, border_color=GRAFITE, pad=(16, 0, 0, 0)),
                 gap='m', **p)
    sinistra = C(
        H('Cosa arriva in cantiere, e cosa resta all’impresa.', 'h2'),
        testo('<p>Dal disegno delle fasi alla posa dei pannelli con il nostro personale. Restano fuori le opere edili.</p>',
              color=TESTO2, mt='m'),
        blocchi(mt='l', hide=['mobile']),
        w=w(5), gap='0')
    distinta = ''.join(f'<li><span class="gpv-cod">{c}</span>{t}</li>' for c, t in voci)
    destra = C(
        C(etichetta('Compreso nella fornitura', colore=GRAFITE), etichetta('7 voci'), dir='row', justify='between',
          gap='m', mb='s'),
        T(f'<ul>{distinta}</ul>', style='body', color=GRAFITE, css='gpv-elenco gpv-distinta'),
        RAW('', css='.gpv-distinta li{display:flex;align-items:baseline;padding:14px 0!important}'
                    '.gpv-distinta .gpv-cod{font-size:13px;flex:0 0 auto;width:32px;margin-right:16px}'),
        w=w(7), gap='0')
    return sezione(
        capo('Fornitura', 'Per tutti i modelli'),
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        blocchi(mt='l', hide=['desktop', 'tablet']),
        bg=CLS, anchor='fornitura')


def piattaforme_posa():
    """P6: la sezione a strati, con le didascalie che oggi sono chiuse nell'immagine portate in HTML."""
    strati = [('Griglie in vetroresina PRFV', ''), ('Supporti portagriglia in acciaio zincato', ''),
              ('Piazzola prefabbricata', f'650{NBSP}×{NBSP}500{NBSP}cm'),
              ('Vasca sottopista', f'400{NBSP}×{NBSP}100{NBSP}×{NBSP}110{NBSP}h{NBSP}cm'),
              ('Sistema di trattamento acque', ''), ('Pietrisco tipo 4/8', f'spessore 20{NBSP}cm'),
              ('Cordolo perimetrale di magrone', ''), ('Magrone di appoggio della vasca sottopista', '')]
    lis = ''.join(f'<li><span>{n}</span><span class="gpv-mis">{v}</span></li>' for n, v in strati)
    css = ('.gpv-strati li{display:flex;justify-content:space-between;align-items:baseline;gap:16px}'
           f".gpv-strati .gpv-mis{{font:400 14px/1.4 '{MONO}',monospace;white-space:nowrap;color:{GRAFITE}}}"
           '@media (max-width:767px){.gpv-strati .gpv-mis{font-size:13px}}')
    return sezione(
        capo('Esempio di posa', 'Sezione'),
        C(C(C(I(img('esempio-di-posa.jpg'), 'Esempio di posa della piattaforma: sezione con vasca sottopista, pietrisco e '
                'cordolo di magrone'), w=(89.7, 100, 100)), w=w(6)),
          C(H('Dal magrone al grigliato.', 'h2'),
            T(f'<ul>{lis}</ul>', style='small', color=GRAFITE, css='gpv-elenco gpv-strati', mt='m'),
            RAW('', css=css), w=w(6), gap='0'),
          dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        anchor='posa')


def piattaforme_personalizzazione():
    """P7: i quattro colori del calcestruzzo, gli accessori, il riscaldamento contro il ghiaccio."""
    tessere = [('colore-rosso.jpg', 'Rosso', 'Ossidi di ferro', 'Campione della piattaforma in calcestruzzo rosso, con il '
                'giunto e il grigliato verde', None),
               ('colore-verde.jpg', 'Verde', 'Ossidi di ferro', 'Campione della piattaforma in calcestruzzo verde', None),
               ('colore-giallo.jpg', 'Giallo', 'Ossidi di ferro', 'Campione della piattaforma in calcestruzzo giallo', None),
               ('colore-marrone.jpg', 'Marrone', 'Ossidi di ferro', 'Campione della piattaforma in calcestruzzo marrone',
                None),
               ('accessorio-isola.jpg', 'Isola di aspirazione', f'Spessore 25{NBSP}cm · 2,50{NBSP}t',
                'Render dell’isola di aspirazione in calcestruzzo con il grigliato', 'accessori'),
               ('accessorio-trave.jpg', 'Trave di rialzo', f'Spessore 30{NBSP}cm · 3,20{NBSP}t',
                'Render della trave di rialzo in calcestruzzo', None)]
    celle = []
    for f, nome, nota, alt, ancora in tessere:
        p = {'anchor': ancora} if ancora else {}
        did = didascalia(nota, hide=['mobile'] if nota == 'Ossidi di ferro' else None)
        celle.append(C(I(img(f), alt, css='gpv-ar11'), H(nome, 'h3', style='h4s', mt='xs'), did,
                       w=(14.5, W[4], 30), gap='xs', **p))
    riga1 = C(
        C(H('Colori e accessori', 'h3'), w=w(5, 5)),
        C(T('<p>Ogni piattaforma, self o portale, si può realizzare in calcestruzzo colorato con ossidi di ferro: rosso, '
            'verde, giallo, marrone.</p>', style='small', color=TESTO2), w=w(7, 7)),
        dir='row', dir_m='column', justify='between', align='baseline', gap=('col', 'col', 's'))
    riga2 = C(
        figura('piattaforma-riscaldata.jpg', 'Pista self davanti a un portale con la neve intorno: le frecce disegnate '
               'mostrano il riscaldamento sotto la pavimentazione', 'Schema del riscaldamento a pavimento su una pista self',
               w=w(5)),
        C(H('Riscaldamento integrato', 'h3'),
          testo('<p>Con un sistema di riscaldamento a pavimento, installato da Gardens Pav, si evita la formazione del '
                'ghiaccio a terra alle basse temperature.</p>', mt='s'),
          C(etichetta('Esempi'),
            testo('<p><a href="/realizzazioni/#lucenec">Autolavaggio a Lučenec, Slovacchia</a> · '
                  '<a href="/realizzazioni/#francia-2">Centro di lavaggio in Francia</a></p>', style='small', css='gpv-tap'),
            gap='xs', mt='m', border_top=1, border_color=LINEA_CLS, pad=(16, 0, 0, 0)),
          H('Isola di aspirazione e travi di rialzo', 'h3', mt='xl'),
          testo(f'<p>L’isola è una piastra prefabbricata in calcestruzzo Rck 45{NBSP}N/mm², spessa 25{NBSP}cm e pesante '
                f'2,50{NBSP}t, che fa da basamento a impianti di aspirazione di modeste dimensioni.</p><p>La trave di rialzo '
                f'è una trave rovescia, spessa 30{NBSP}cm e pesante 3,20{NBSP}t, posata in parallelo alle piattaforme come '
                'basamento per sovrastrutture in acciaio. Entrambe possono avere tubazioni predisposte per il passaggio dei '
                'cavi.</p>', style='small', color=TESTO2, mt='s'),
          w=w(7), gap='0'),
        dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l'), mt='xl')
    return sezione(
        capo('Personalizzazione', 'Su ogni modello, self o portale'),
        riga1,
        C(*celle, dir='row', wrap=True, justify='between', gap='col', gap_r=('l', 'l', 'm'), mt='l'),
        riga2,
        bg=CLS, anchor='personalizzazione')


STRISCIA = ['rubano', 'abano-terme', 'alonte', 'altivole', 'milano', 'aosta', 'san-marino', 'pistoia', 'san-lazzaro-di-savena']

CSS_STRISCIA = (
    '.gpv-striscia .gpv-track{flex-wrap:nowrap!important;overflow-x:auto!important;overflow-y:hidden;'
    'scroll-snap-type:x mandatory;scrollbar-width:thin;'
    f'scrollbar-color:{GRAFITE} {CLS};padding-left:max(48px,calc((100% - 1280px) / 2))!important;'
    'scroll-padding-left:max(48px,calc((100% - 1280px) / 2))}'
    '.gpv-striscia.gpv-js .gpv-track{scrollbar-width:none}.gpv-striscia.gpv-js .gpv-track::-webkit-scrollbar{display:none}'
    ".gpv-striscia .gpv-track::after{content:'';flex:0 0 max(16px,calc((100% - 1280px) / 2 - 32px))}"
    '.gpv-striscia .gpv-track>*{scroll-snap-align:start}'
    '.gpv-striscia .gpv-card{text-decoration:none!important}'
    '.gpv-striscia .gpv-card:hover .gpv-nome,.gpv-striscia .gpv-card:focus-visible .gpv-nome,'
    '.gpv-striscia .gpv-card:hover .gpv-nome .elementor-heading-title{text-decoration:underline;'
    'text-decoration-thickness:1px;text-underline-offset:4px}'
    f'.gpv-striscia .gpv-card:focus-visible,.gpv-striscia .gpv-track:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;'
    'outline-offset:-2px!important}'
    '.gpv-striscia .gpv-ctrl{max-width:1280px;margin:32px auto 0;padding:0 48px;box-sizing:content-box;display:flex;'
    'align-items:center;gap:24px}'
    '.gpv-striscia .gpv-ctrl[hidden]{display:none}'
    f'.gpv-striscia .gpv-bar{{flex:1;height:1px;background:{LINEA};position:relative}}'
    f'.gpv-striscia .gpv-thumb{{position:absolute;top:-1px;left:0;height:3px;width:30%;background:{GRAFITE}}}'
    '.gpv-striscia .gpv-btns{display:flex;gap:8px}'
    f".gpv-striscia .gpv-ctrl .gpv-btn{{width:48px;height:48px;padding:0!important;border:1px solid {GRAFITE}!important;"
    f"border-radius:0!important;background:{BIANCO}!important;color:{GRAFITE}!important;font:400 18px/1 '{ARCHIVO}',Arial,"
    'sans-serif;cursor:pointer;box-shadow:none!important;transition:background-color .15s,color .15s}'
    '.gpv-striscia .gpv-ctrl .gpv-btn:hover:not([aria-disabled=true]),.gpv-striscia .gpv-ctrl .gpv-btn:focus-visible'
    f'{{background:{GRAFITE}!important;color:{BIANCO}!important;border-color:{GRAFITE}!important}}'
    '.gpv-striscia .gpv-ctrl .gpv-btn[aria-disabled=true],.gpv-striscia .gpv-ctrl .gpv-btn[aria-disabled=true]:hover'
    f'{{background:{BIANCO}!important;border-color:{LINEA}!important;color:{LINEA_CLS}!important;cursor:default}}'
    f'.gpv-striscia .gpv-ctrl .gpv-btn:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:2px}}'
    '@media (max-width:1024px){.gpv-striscia .gpv-track{padding-left:32px!important;scroll-padding-left:32px}'
    '.gpv-striscia .gpv-track::after{flex-basis:8px}.gpv-striscia .gpv-ctrl{padding:0 32px}}'
    '@media (max-width:767px){.gpv-striscia .gpv-track{padding-left:24px!important;scroll-padding-left:24px}'
    '.gpv-striscia .gpv-track::after{flex-basis:0}.gpv-striscia .gpv-ctrl{margin-top:24px;padding:0 24px}'
    '.gpv-striscia .gpv-ctrl .gpv-btn{width:44px;height:44px}}'
)

# frecce e barra: senza JavaScript restano nascoste (lo scorrimento a mano e l'aggancio funzionano comunque)
JS_STRISCIA = (
    "<script>(function(){function go(){document.querySelectorAll('.gpv-striscia').forEach(function(w){"
    "var s=w.querySelector('.gpv-track'),c=w.querySelector('.gpv-ctrl');if(!s||!c||c.dataset.ok)return;c.dataset.ok=1;"
    "var t=c.querySelector('.gpv-thumb'),p=c.querySelector('.gpv-prev'),n=c.querySelector('.gpv-next');c.hidden=false;"
    "w.classList.add('gpv-js');"
    "s.setAttribute('tabindex','0');s.setAttribute('role','region');"
    "s.setAttribute('aria-label','Cantieri con le piattaforme Gardens Pav');"
    "var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches,bh=rm?'auto':'smooth';"
    "function st(){var k=s.children[1]||s.children[0];return k?k.getBoundingClientRect().left-s.children[0].getBoundingClientRect().left:300}"
    "function up(){var m=s.scrollWidth-s.clientWidth,v=s.clientWidth/s.scrollWidth,r=m>0?s.scrollLeft/m:0;"
    "t.style.width=(v*100)+'%';t.style.left=(r*(1-v)*100)+'%';"
    "p.setAttribute('aria-disabled',s.scrollLeft<=2);n.setAttribute('aria-disabled',s.scrollLeft>=m-2)}"
    "p.addEventListener('click',function(){if(this.getAttribute('aria-disabled')==='true')return;s.scrollBy({left:-st(),behavior:bh})});"
    "n.addEventListener('click',function(){if(this.getAttribute('aria-disabled')==='true')return;s.scrollBy({left:st(),behavior:bh})});"
    "s.addEventListener('focusin',function(e){var k=e.target.closest&&e.target.closest('.gpv-card');if(!k)return;"
    "var a=k.getBoundingClientRect(),b=s.getBoundingClientRect(),pl=parseFloat(getComputedStyle(s).scrollPaddingLeft)||0;"
    "if(a.left<b.left+pl-1||a.right>b.right+1){s.scrollTo({left:s.scrollLeft+a.left-b.left-pl,behavior:bh})}});"
    "s.addEventListener('keydown',function(e){if(e.target!==s)return;if(e.key==='Home'||e.key==='End'){e.preventDefault();"
    "s.scrollTo({left:e.key==='Home'?0:s.scrollWidth,behavior:bh})}});"
    "s.addEventListener('scroll',up,{passive:true});window.addEventListener('resize',up);up()})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();</script>"
)
HTML_COMANDI = (
    '<div class="gpv-ctrl" hidden><div class="gpv-bar"><span class="gpv-thumb"></span></div><div class="gpv-btns">'
    '<button type="button" class="gpv-btn gpv-prev" aria-label="Cantieri precedenti">&larr;</button>'
    '<button type="button" class="gpv-btn gpv-next" aria-label="Cantieri successivi">&rarr;</button></div></div>'
)


def _alt_cantiere(c):
    """Testo alternativo dalla didascalia nel nome del file della foto (es. "portale con lavachassis")."""
    nome = c['copertina'] if c['id'] != 'san-marino' else 'realizzazione-san-marino-rossi-service-07.jpg'
    coda = nome.rsplit('.', 1)[0].split('-')
    parole = []
    for i, x in enumerate(coda):
        if x.isdigit() and len(x) == 2:
            parole = [p for p in coda[i + 1:] if not p.isdigit() or len(p) == 1]
            break
    descr = ' '.join(parole).replace('s s q8', 'stazione di servizio').strip()
    luogo = c['luogo'] if c['regione'] not in SIGLA_PAESE.values() else c['regione']
    if descr:
        return f'{descr[0].upper() + descr[1:]}, {luogo}'
    return f'Piattaforme per autolavaggio posate, {luogo}'


def _titolo_luogo(c):
    if c['sigla'] == 'FR':
        return 'Francia'
    return c['luogo']


def piattaforme_striscia():
    """P8: la striscia a scorrimento dei cantieri, con la regione in monospazio sopra il luogo."""
    schede = []
    for cid in STRISCIA:
        c = CANTIERE[cid]
        figli = [I(img(f'cantiere-{cid}.jpg'), _alt_cantiere(c), css='gpv-ar43'),
                 etichetta(c['regione'], mt='s'),
                 H(f'{_titolo_luogo(c)} ({c["sigla"]})', 'h3', style='h4', css='gpv-nome', mt=4)]
        if c['modelli_nelle_didascalie']:
            figli.append(T(f'<p>{c["modelli_nelle_didascalie"]}</p>', style='small', color=TESTO2, mt=4))
        schede.append(C(*figli, larg_px=(400, 340, 290), gap='0', link=f'/realizzazioni/#{cid}', css='gpv-card'))
    testa = C(
        capo('Realizzazioni', '36 cantieri'),
        C(C(H('Da Aosta ad Avetrana, e in Svizzera, Slovacchia, Francia e San Marino.', 'h2'), w=w(8, 7)),
          C(T('<p>Piattaforme posate per autolavaggi, stazioni di servizio, officine, concessionarie e autotrasporti.</p>',
              style='small', color=TESTO2), w=w(4, 5)),
          dir='row', dir_m='column', justify='between', align='end', gap=('col', 'col', 's')),
        boxed=True, pad=(0, 'lato'), gap='0', mb='l')
    binario = C(*schede, dir='row', wrap=False, gap=(32, 24, 24), pad='0', css='gpv-track', overflow='auto')
    piede = C(link_freccia('Tutte le 36 realizzazioni', '/realizzazioni/'), boxed=True, pad=(0, 'lato'), gap='0', mt='m')
    return sezione(testa, binario, RAW(HTML_COMANDI + JS_STRISCIA, css=CSS_STRISCIA), piede,
                   boxed=False, pad=('sezione', 0), css='gpv-striscia', anchor='cantieri')


def piattaforme():
    return [('apertura', piattaforme_apertura()), ('caratteristiche', piattaforme_caratteristiche()),
            ('tavola', piattaforme_tavola()), ('modelli', piattaforme_modelli()), ('fornitura', piattaforme_fornitura()),
            ('posa', piattaforme_posa()), ('personalizzazione', piattaforme_personalizzazione()),
            ('striscia', piattaforme_striscia()), ('ufficio-tecnico', ufficio_tecnico(bg=CLS, nota='Ufficio tecnico'))]


# ---------------------------------------------------------------------------------------------
# 05 REALIZZAZIONI (spec §10)
# ---------------------------------------------------------------------------------------------
# id dei punti e delle linee nella mappa (mappa-cantieri.svg) per i cantieri che li hanno con un altro nome
ID_MAPPA = {'cornate-d-adda': 'cornate', 'vezza-d-oglio': 'vezza', 'verona-autolavaggio': 'verona',
            'verona-autotrasporti': 'verona', 'abano-terme': 'abano', 'san-giovanni-in-persiceto': 'persiceto',
            'san-lazzaro-di-savena': 'sanlazzaro', 'san-mauro-pascoli': 'smauro', 'tivoli-terme': 'tivoli',
            'san-marino': 'sanmarino', 'francia-1': 'francia', 'francia-2': 'francia'}
ESTERE = ('Svizzera', 'Slovacchia', 'Francia', 'San Marino')


def _svg(nome):
    return open(os.path.join(QUI, 'dati', nome), encoding='utf-8').read().strip()


def _elenco_luoghi():
    """Italia da nord a sud (dalla coordinata del punto nella mappa), poi fuori dall'Italia. Verona e Francia: una voce
    per due cantieri."""
    import re
    svg = _svg('mappa-cantieri.svg')
    nord = {k: float(y) for k, y in re.findall(r'id="p-([a-z]+)"[^>]*?cy="([\d.]+)"', svg)}
    italiane, viste = [], set()
    for c in CANTIERI:
        k = ID_MAPPA.get(c['id'], c['id'])
        if c['regione'] in ESTERE or k in viste:
            continue
        viste.add(k)
        nome = 'Verona, due cantieri' if k == 'verona' else c['luogo']
        italiane.append((nord[k], nome, c['sigla'], c['id'], k))
    italiane.sort()
    estere = [('Poschiavo', 'CH', 'poschiavo', 'poschiavo'), ('Lučenec', 'SK', 'lucenec', 'lucenec'),
              ('Francia, due centri di lavaggio', 'FR', 'francia-1', 'francia'),
              ('San Marino', 'RSM', 'san-marino', 'sanmarino')]
    return [(n, s, i, k) for _, n, s, i, k in italiane], estere


CSS_LUOGHI = (
    f".gpv-luoghi-r .gpv-luoghi-t{{margin:0 0 8px!important;font:500 12px/1.4 '{MONO}',monospace;letter-spacing:1px;"
    f'text-transform:uppercase;color:{TESTO2}}}'
    f'.gpv-luoghi-r ul{{columns:2;column-gap:32px;margin:0 0 32px!important;padding:0!important;list-style:none;'
    f'border-top:1px solid {GRAFITE}}}'
    '.gpv-luoghi-r ul:last-child{margin-bottom:0!important}'
    f'.gpv-luoghi-r li{{break-inside:avoid;margin:0!important;padding:0!important;border:0!important;'
    f'border-bottom:1px solid {LINEA}!important;list-style:none}}'
    f".gpv-luoghi-r a{{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:36px;padding:6px 0;"
    f"box-sizing:border-box;color:{GRAFITE}!important;text-decoration:none!important;font:400 15px/1.35 '{ARCHIVO}',Arial,"
    'sans-serif}'
    f'.gpv-luoghi-r a:hover,.gpv-luoghi-r a:focus-visible,.gpv-luoghi-r a.gpv-on{{color:{ARANCIO_SCURO}!important}}'
    '.gpv-luoghi-r a:hover span,.gpv-luoghi-r a:focus-visible span{text-decoration:underline;text-underline-offset:4px}'
    f".gpv-luoghi-r b{{font:400 12px/1 '{MONO}',monospace;letter-spacing:1px;color:{TESTO2};white-space:nowrap}}"
    f'.gpv-luoghi-r .gpv-estera b{{color:{ARANCIO_SCURO}}}'
    '@media (min-width:768px) and (max-width:1024px){.gpv-luoghi-r ul{columns:3;column-gap:24px}}'
    '@media (max-width:767px){.gpv-luoghi-r ul{column-gap:16px}.gpv-luoghi-r a{font-size:14px;gap:8px}}'
)

CSS_MAPPA = (
    '.gpv-mappa-box{margin:0}.gpv-mappa-box svg{display:block;width:100%;height:auto}'
    f'.gpv-mappa-box .gpv-p.gpv-on{{fill:{ARANCIO};stroke:{GRAFITE};stroke-width:2px;r:9px}}'
    '.gpv-mappa-box .gpv-l.gpv-on{stroke-width:3.5px}'
    f".gpv-mappa-box figcaption{{margin-top:12px;font:400 12px/1.5 '{MONO}',monospace;letter-spacing:.7px;"
    f'text-transform:uppercase;color:{TESTO2}}}'
    '@media (min-width:768px) and (max-width:1024px){.gpv-mappa-box{max-width:640px;margin-left:auto!important;'
    'margin-right:auto!important}}'
    '@media (max-width:767px){.gpv-mappa-box .gpv-mt{font-size:30px}.gpv-mappa-box .gpv-mt-l{font-size:34px}'
    '.gpv-mappa-box .gpv-l{stroke-width:2.5px}.gpv-mappa-box .gpv-p{r:9px}.gpv-mappa-box .gpv-p.gpv-on{r:13px}}'
)

JS_MAPPA = (
    "<script>(function(){function go(){var b=document.querySelector('.gpv-mappa-box');if(!b||b.dataset.ok)return;"
    "b.dataset.ok=1;function on(k,si){['p-','l-'].forEach(function(x){var e=document.getElementById(x+k);"
    "if(e)e.classList.toggle('gpv-on',si)})}"
    "document.querySelectorAll('.gpv-luoghi-r a[data-p]').forEach(function(a){var k=a.getAttribute('data-p');"
    "['mouseenter','focus'].forEach(function(ev){a.addEventListener(ev,function(){on(k,true);a.classList.add('gpv-on')})});"
    "['mouseleave','blur'].forEach(function(ev){a.addEventListener(ev,function(){on(k,false);a.classList.remove('gpv-on')})})"
    "})}if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();</script>"
)


def elenco_luoghi_html():
    italiane, estere = _elenco_luoghi()

    def li(n, s, i, k, e=False):
        cls = ' class="gpv-estera"' if e else ''
        return f'<li{cls}><a href="#{i}" data-p="{k}"><span>{n}</span><b>{s}</b></a></li>'
    return ('<div class="gpv-luoghi-r"><p class="gpv-luoghi-t">Italia · 31 cantieri</p><ul>'
            + ''.join(li(*v) for v in italiane) + '</ul><p class="gpv-luoghi-t">Fuori dall’Italia · 5 cantieri</p><ul>'
            + ''.join(li(*v, e=True) for v in estere) + '</ul></div>')


def realizzazioni_apertura():
    """R1: la mappa con una linea arancio da Legnaro a ogni cantiere; l'elenco accende il punto."""
    luoghi = elenco_luoghi_html()
    mappa = _svg('mappa-cantieri.svg')
    sinistra = C(
        etichetta('Realizzazioni'),
        H('36 cantieri, in 22 province e cinque paesi.', 'h1', mt=24),
        testo('<p>Sono le piattaforme per autolavaggi pubblicate nelle nostre realizzazioni, da Aosta ad Avetrana e fino a '
              'Lučenec, in Slovacchia. Le foto sono quelle dei cantieri, durante e dopo la posa.</p>', style='lead',
              color=TESTO2, mt='m'),
        RAW(luoghi, css=CSS_LUOGHI, mt='l', hide=['tablet', 'mobile']),
        w=w(5, 12), gap='0')
    destra = C(
        RAW(f'<figure class="gpv-mappa-box">{mappa}<figcaption>Le linee partono da Legnaro · confini Natural Earth · '
            f'località OpenStreetMap</figcaption></figure>' + JS_MAPPA, css=CSS_MAPPA),
        w=w(7, 12), gap='0')
    return sezione(
        C(sinistra, destra, dir='row', dir_t='column', justify='between', align='start', gap=('col', 'l', 'l')),
        RAW(luoghi, mt='l', hide=['desktop']),
        pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')


GRUPPI = [('Veneto', ['Veneto']), ('Valle d’Aosta e Piemonte', ['Valle d’Aosta', 'Piemonte']),
          ('Lombardia', ['Lombardia']), ('Emilia-Romagna', ['Emilia-Romagna']), ('Toscana', ['Toscana']),
          ('Lazio e Puglia', ['Lazio', 'Puglia']), ('Fuori dall’Italia', list(ESTERE))]


def scheda_cantiere(c):
    nome_img = f'cantiere-{c["id"]}.jpg'
    figli = [I(img(nome_img), _alt_cantiere(c), link=img(nome_img), css='gpv-ar43 gpv-zoom'),
             H(f'{_titolo_luogo(c)}<span class="gpv-sigla-t">{c["sigla"]}</span>', 'h3', style='h4', mt='xs')]
    if c['tipo']:
        figli.append(T(f'<p>{c["tipo"]}</p>', style='small', color=TESTO2, hide=['mobile']))
    if c['modelli_nelle_didascalie']:
        figli.append(T(f'<p>{c["modelli_nelle_didascalie"]}</p>', style='mono12', color=GRAFITE))
    return C(*figli, w=(W[3], W[4], 47.6), gap='xs', anchor=c['id'])


def realizzazioni_cantieri():
    """R2: il luogo piccolo sopra, la foto vera, i modelli citati dall'azienda (Jensen, Godelmann)."""
    gruppi = []
    for nome, regioni in GRUPPI:
        elenco = sorted((c for c in CANTIERI if c['regione'] in regioni),
                        key=lambda c: (regioni.index(c['regione']), c['luogo'] if c['regione'] not in ESTERE else ''))
        gruppi.append(C(
            etichetta(f'{nome} · {len(elenco)}', colore=GRAFITE, mb='s'),
            C(*[scheda_cantiere(c) for c in elenco], dir='row', wrap=True, justify='start', gap=('col', 'col', 16),
              gap_r=('l', 'l', 'm'), border_top=1, border_color=GRAFITE, pad=('m', 0, 0, 0)),
            gap='0', mt=0 if not gruppi else 'xl'))
    css = ('.gpv-zoom a{display:block;cursor:zoom-in}'
           f'.gpv-zoom a:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:2px!important}}')
    return sezione(
        capo('I cantieri', 'Foto dal sito Gardens Pav'),
        *gruppi,
        RAW('', css=css),
        bg=CLS, anchor='cantieri')


def realizzazioni():
    return [('apertura', realizzazioni_apertura()), ('cantieri', realizzazioni_cantieri()),
            ('ufficio-tecnico', ufficio_tecnico(bg=BIANCO))]


# ---------------------------------------------------------------------------------------------
# 06 AZIENDA (spec §11)
# ---------------------------------------------------------------------------------------------
def azienda_apertura():
    foto = 'vasche-autoarticolato.jpg'
    alt = ('Vasca rettangolare aperta, appesa alle fasce di sollevamento, calata nello scavo accanto alle vasche già posate '
           'e coperte')
    sinistra = C(
        etichetta('Azienda'),
        H('Gardens Pav S.r.l., opere in calcestruzzo a Legnaro.', 'h1', mt=24),
        I(img(foto), alt, hide=['desktop', 'tablet'], mt='m'),
        testo('<p>Gardens Pav opera nel campo della prefabbricazione di manufatti in calcestruzzo armato per il trattamento '
              'dei reflui domestici, industriali e delle acque meteoriche. Realizza inoltre piattaforme prefabbricate per '
              'autolavaggi, che progetta, produce e installa in Italia e in Europa con personale specializzato.</p>',
              style='lead', color=TESTO2, mt='m'),
        indice([('Vasche monoblocco', '17 misure', '/vasche/'), ('Depurazione', '7 impianti', '/depurazione/'),
                ('Piattaforme per autolavaggi', '8 modelli', '/piattaforme-autolavaggi/')], mt='l'),
        w=w(6), gap='0')
    destra = figura(foto, alt, 'Posa di una vasca rettangolare nello scavo', w=w(6), hide=['mobile'])
    return sezione(
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap='col'),
        pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')


def azienda_calcestruzzo():
    """A2: il numero che descrive tutto quello che esce dallo stabilimento, una volta sola nel sito."""
    return sezione(
        capo('Il calcestruzzo', 'UNI EN 206-1', scuro=True),
        C(C(H('C35/45', 'p', style='mega', color=BIANCO, css='gpv-nowrap'),
            didascalia(f'Classe di resistenza a compressione · Rck 45{NBSP}N/mm²', colore=SU_GRAFITE2, mt='m'),
            C(*[riga_dato(l, T(f'<p>{v}</p>', style='small', color=BIANCO), larg=150, linea=LINEA_SCURA,
                          col_lab=SU_GRAFITE2, pad_v=14)
                for l, v in (('Esposizione', 'XC4 · <span class="gpv-nowrap">XS1-XD2</span> · XF1 · XA2'),
                             ('Armatura', f'Acciaio B450C, copriferro 3{NBSP}cm'), ('Consistenza', 'S4'),
                             ('Getto', 'In cassero, con vibratore ad immersione ad alta frequenza'))],
              gap='0', border_top=1, border_color=LINEA_SCURA, mt='xl', w=(80, 100, 100)),
            w=w(7, 6), gap='0'),
          C(T(f'<p>L’impianto di calcestruzzo computerizzato, a standard controllati elettronicamente, miscela inerti, '
              f'cemento, acqua e additivi chimici: ne esce un calcestruzzo con resistenza caratteristica cubica Rck 45{NBSP}'
              f'N/mm² e classe di consistenza S4. Il calcestruzzo è armato con acciaio B450C, con copriferro di 3{NBSP}cm.'
              '</p>', style='body', color=SU_GRAFITE2),
            figura('vasche-batteria-cantiere.jpg', 'Vasche rettangolari aperte posate una accanto all’altra nello scavo di '
                   'un cantiere, con i numeri dipinti sulle pareti', 'Vasche rettangolari in cantiere', colore=SU_GRAFITE2,
                   mt='l'),
            w=w(5, 6), gap='0'),
          dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        bg=GRAFITE, css='gpv-scuro', anchor='calcestruzzo')


def azienda_norme():
    norme = tabella_voci([
        ('D.M. 17/01/2018', 'Aggiornamento delle Norme tecniche per le costruzioni'),
        ('Circolare 21/01/2019 n.&nbsp;7 C.S.LL.PP.', 'Istruzioni per l’applicazione delle Norme tecniche'),
        ('UNI EN 206-1', 'Calcestruzzo'),
        ('UNI 11104', 'Calcestruzzo, istruzioni complementari'),
        ('Regolamento UE 305/2011', 'Prodotti da costruzione (CPR)'),
        ('UNI EN 858-1:2005', 'Impianti di separazione per liquidi leggeri'),
        ('UNI EN 1825-1:2005', 'Separatori di grassi, parte 1'),
    ], 'Norme di riferimento')
    return sezione(
        capo('Norme di riferimento', 'Manufatti e materie prime'),
        C(C(H('Le norme dei manufatti.', 'h2'),
            testo('<p>Le materie prime acquistate hanno i requisiti di conformità e i manufatti sono realizzati nel rispetto '
                  'di queste norme.</p>', color=TESTO2, mt='m'),
            w=w(5), gap='0'),
          C(RAW(norme), w=w(7)),
          dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'l')),
        anchor='norme')


def azienda_dati():
    def valore(v):
        return T(f'<p>{v}</p>', style='body', color=GRAFITE, link_color=ARANCIO_SCURO, link_hover=GRAFITE)
    righe = [('Ragione sociale', 'Gardens Pav S.r.l.'), ('Sede legale e operativa', f'{INDIRIZZO}, {CITTA}'),
             ('Partita IVA e codice fiscale', PIVA), ('REA', REA), ('Capitale sociale', '100.000 euro'), ('PEC', PEC),
             ('Codice destinatario SDI', 'J6URRTW'), ('Telefono e fax', f'{TEL} · fax {FAX}'),
             ('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>')]
    tabella_dati = C(*[riga_dato(l, valore(v), larg=280, linea=LINEA_CLS) for l, v in righe],
                     w=w(8, 7), gap='0', border_top=1, border_color=GRAFITE)
    return sezione(
        capo('Dati societari', 'Registro Imprese di Padova'),
        C(tabella_dati,
          C(H('Per l’ufficio acquisti', 'h3'),
            T('<p>I dati per l’anagrafica fornitori e la fatturazione elettronica.</p>', style='small', color=TESTO2, mt='s'),
            w=w(4, 5), gap='0'),
          dir='row', dir_m='column-reverse', justify='between', align='start', gap=('col', 'col', 'm')),
        bg=CLS, anchor='dati-societari')


def azienda():
    return [('apertura', azienda_apertura()), ('calcestruzzo', azienda_calcestruzzo()), ('norme', azienda_norme()),
            ('dati-societari', azienda_dati()), ('ufficio-tecnico', ufficio_tecnico(bg=BIANCO))]


# ---------------------------------------------------------------------------------------------
# 07 CONTATTI (spec §12)
# ---------------------------------------------------------------------------------------------
TITOLO_MODULO = 'Richiesta informazioni'
CF7 = f'[contact-form-7 title="{TITOLO_MODULO}"]'

STILE_CF7 = (
    '.gpv-modulo .wpcf7 p{margin:0}.gpv-modulo .wpcf7 br{display:none}'
    '.gpv-modulo .gpv-campi{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);column-gap:24px;row-gap:20px}'
    '.gpv-modulo .gpv-campi>p{display:contents}'
    '.gpv-modulo .gpv-largo{grid-column:1/-1}'
    f".gpv-modulo .wpcf7 label{{display:block;margin:0;font:500 12px/1.4 '{MONO}',monospace;letter-spacing:1px;"
    f'text-transform:uppercase;color:{TESTO2}}}'
    '.gpv-modulo .wpcf7-form-control-wrap{display:block;margin-top:8px}'
    '.gpv-modulo input[type=text],.gpv-modulo input[type=email],.gpv-modulo input[type=tel],.gpv-modulo select,'
    f'.gpv-modulo textarea{{display:block;width:100%;height:48px;margin:0;background:{BIANCO};border:1px solid {LINEA_CLS};'
    f"border-radius:0;box-shadow:none;padding:12px 14px;font:400 16px/22px '{ARCHIVO}',Arial,sans-serif;letter-spacing:0;"
    f'text-transform:none;color:{GRAFITE};box-sizing:border-box}}'
    '.gpv-modulo textarea{height:auto;min-height:120px;resize:vertical}'
    f".gpv-modulo input[type=file]{{display:block;width:100%;padding:8px 0;font:400 14px/1.4 '{ARCHIVO}',Arial,sans-serif;"
    f'text-transform:none;letter-spacing:0;color:{TESTO2}}}'
    f".gpv-modulo input[type=file]::file-selector-button{{margin-right:16px;padding:10px 16px;border:1px solid {GRAFITE};"
    f"border-radius:0;background:{BIANCO};color:{GRAFITE};font:600 14px/1.2 '{ARCHIVO}',Arial,sans-serif;cursor:pointer;"
    'transition:background-color .15s,color .15s}'
    f'.gpv-modulo input[type=file]::file-selector-button:hover{{background:{GRAFITE};color:{BIANCO}}}'
    f'.gpv-modulo input:focus,.gpv-modulo select:focus,.gpv-modulo textarea:focus{{border:2px solid {ARANCIO_SCURO};'
    'outline:0;padding:11px 13px}'
    f".gpv-modulo input[type=submit]{{background:{ARANCIO};color:{GRAFITE};border:1px solid {ARANCIO};border-radius:0;"
    f"padding:16px 32px;font:600 15px/1.2 '{ARCHIVO}',Arial,sans-serif;letter-spacing:0;text-transform:none;cursor:pointer;"
    'transition:background-color .15s,color .15s,border-color .15s}'
    f'.gpv-modulo input[type=submit]:hover,.gpv-modulo input[type=submit]:focus-visible{{background:{GRAFITE};'
    f'color:{BIANCO};border-color:{GRAFITE}}}'
    f'.gpv-modulo input[type=submit]:focus-visible{{outline:2px solid {ARANCIO_SCURO};outline-offset:2px}}'
    f'.gpv-modulo input[type=checkbox]{{accent-color:{GRAFITE};flex:0 0 20px;width:20px;height:20px;margin:1px 0 0}}'
    '.gpv-modulo .wpcf7-list-item{display:block;margin:0}'
    '.gpv-modulo .wpcf7-acceptance label{display:flex;align-items:flex-start;gap:12px;min-height:44px;padding:4px 0;'
    f"font:400 14px/1.5 '{ARCHIVO}',Arial,sans-serif;letter-spacing:0;text-transform:none;color:{GRAFITE}}}"
    f".gpv-modulo .wpcf7-not-valid-tip{{color:{ARANCIO_SCURO};font:400 14px/1.4 '{ARCHIVO}',Arial,sans-serif;margin-top:6px;"
    'text-transform:none;letter-spacing:0}'
    f'.gpv-modulo .wpcf7 form .wpcf7-response-output{{margin:24px 0 0;padding:14px 16px;border:1px solid {GRAFITE};'
    f"font:400 15px/1.5 '{ARCHIVO}',Arial,sans-serif}}"
    '.gpv-modulo .wpcf7-spinner{display:block;margin:12px 0 0}'
    '@media (max-width:767px){.gpv-modulo .gpv-campi{grid-template-columns:minmax(0,1fr)}'
    '.gpv-modulo input[type=submit]{width:100%}}'
)


def contatti_recapiti():
    corpo = ('Per che cosa (vasca, impianto, piattaforma):\nDato di dimensionamento (portata l/s, abitanti equivalenti, mq o '
             'modello):\nComune e provincia di posa:\nNote:\n')
    alternativa = (f'<p style="margin:0 0 24px">Scrivete a <a href="mailto:{EMAIL}">{EMAIL}</a>: il pulsante qui sotto apre '
                   'una email con i campi già pronti da compilare.</p>'
                   f'<p style="margin:0"><a class="gpv-btn-mail" href="{mailto(TITOLO_MODULO, corpo)}">Scrivi a {EMAIL}</a>'
                   '</p>')
    css_alt = (f".gpv-btn-mail{{display:inline-block;background:{ARANCIO};color:{GRAFITE}!important;border:1px solid {ARANCIO};"
               f"padding:16px 32px;font:600 15px/1.2 '{ARCHIVO}',Arial,sans-serif;text-decoration:none!important;"
               'transition:background-color .15s,color .15s,border-color .15s;overflow-wrap:anywhere}'
               f'.gpv-btn-mail:hover,.gpv-btn-mail:focus-visible{{background:{GRAFITE};color:{BIANCO}!important;'
               f'border-color:{GRAFITE}}}')
    sinistra = C(
        etichetta('Contatti'),
        H(f'{INDIRIZZO}, Legnaro{NBSP}(PD).', 'h1', mt=24),
        etichetta('Telefono', mt='m'),
        H(TEL, 'p', style='tel', color=GRAFITE, link=TEL_LINK, css='gpv-tel-grande', mt='xs'),
        C(riga_dato('Email', testo(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'), larg=120),
          riga_dato('PEC', T(f'<p>{PEC}</p>', style='body', color=GRAFITE), larg=120),
          riga_dato('Fax', T(f'<p>{FAX}</p>', style='body', color=GRAFITE), larg=120),
          riga_dato('Orari', T(f'<p>{ORARI}. {CHIUSURA}.</p>', style='body', color=GRAFITE), larg=120),
          riga_dato('Sede', [T(f'<p>{INDIRIZZO}, {CITTA}</p>', style='body', color=GRAFITE),
                             testo(f'<p><a href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps</a></p>',
                                   style='small', css='gpv-tap')], larg=120),
          gap='0', border_top=1, border_color=LINEA, mt='m'),
        w=w(5, 5), gap='0')
    destra = C(
        H('Richiesta all’ufficio tecnico', 'h2'),
        T('<p>Compilate il modulo e sarete ricontattati al più presto. Per scegliere la vasca o l’impianto servono il manufatto '
          'e il dato che lo dimensiona: portata, abitanti equivalenti o superficie; per le piattaforme il modello e il luogo '
          'di posa.</p>', style='small', color=TESTO2, mt='s'),
        C(SHORTCODE(CF7, alternativa_html=alternativa, colore=TESTO2, stile='small'),
          RAW('', css=STILE_CF7, solo_elementor=True), RAW('', css=css_alt), mt='m', css='gpv-modulo', gap='0'),
        w=w(7, 7), gap='0', bg=CLS, pad=(('l', 'l', 'm'), ('l', 'l', 'm')), anchor='richiesta')
    return sezione(
        C(sinistra, destra, dir='row', dir_m='column', justify='between', align='start', gap=('col', 'col', 'xl')),
        pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')


CSS_GMAPS = (
    f'.gpv-gmaps{{background:{BIANCO};border:1px solid {LINEA_CLS};padding:24px}}'
    f".gpv-gmaps p{{margin:0 0 16px!important;font:400 15px/1.55 '{ARCHIVO}',Arial,sans-serif;color:{TESTO2}}}"
    '.gpv-gmaps button,.gpv-gmaps button:focus{margin:0;padding:16px 32px!important;'
    f'border:1px solid {GRAFITE}!important;border-radius:0!important;background:transparent!important;color:{GRAFITE}!important;'
    f"font:600 15px/1.2 '{ARCHIVO}',Arial,sans-serif!important;cursor:pointer;box-shadow:none!important;"
    'transition:background-color .15s,color .15s}'
    f'.gpv-gmaps button:hover,.gpv-gmaps button:focus-visible{{background:{GRAFITE}!important;color:{BIANCO}!important}}'
    f'.gpv-gmaps button:focus-visible{{outline:2px solid {ARANCIO_SCURO}!important;outline-offset:2px}}'
    '.gpv-gmaps iframe{display:block;width:100%;height:420px;border:0;filter:grayscale(1)}'
    '.gpv-gmaps.gpv-aperta{padding:0}'
    '.gpv-gmaps:not(.gpv-js){display:none}'
    '@media (max-width:767px){.gpv-gmaps button{width:100%}.gpv-gmaps iframe{height:360px}}'
)

JS_GMAPS = (
    "<script>(function(){document.querySelectorAll('.gpv-gmaps').forEach(function(g){if(g.dataset.ok)return;g.dataset.ok=1;"
    "g.classList.add('gpv-js');var b=g.querySelector('button');b.addEventListener('click',function(){"
    "var f=document.createElement('iframe');f.src=b.getAttribute('data-src');"
    "f.title='Mappa di Google: Via Romea 154/A, Legnaro';f.setAttribute('allowfullscreen','');"
    "g.innerHTML='';g.classList.add('gpv-aperta');g.appendChild(f);f.focus()})})})();</script>"
)

CSS_MAPPA_LEGNARO = (
    '.gpv-legnaro{margin:0}.gpv-legnaro svg{display:block;width:100%;height:auto}'
    '@media (min-width:768px) and (max-width:1024px){.gpv-legnaro svg{height:560px}}'
    f".gpv-legnaro figcaption{{font:400 12px/1.5 '{MONO}',monospace;letter-spacing:.7px;text-transform:uppercase;"
    f'color:{TESTO2};margin-top:8px}}'
    '@media (max-width:1024px){.gpv-mappa-col .gpv-legnaro figcaption{padding:0 32px}}'
    '@media (max-width:767px){.gpv-mappa-col .gpv-legnaro figcaption{padding:0 24px}}'
)


def contatti_mappa():
    """K2: la mappa dei dintorni disegnata dai dati OpenStreetMap; Google si carica solo se la si chiede."""
    gmaps = ('<div class="gpv-gmaps"><p>La mappa di Google si carica solo se la chiedete: aprendola, Google riceve i dati '
             'di navigazione del vostro browser.</p><button type="button" data-src="https://www.google.com/maps?'
             'q=Gardens+Pav,+Via+Romea+154%2FA,+35020+Legnaro+PD&amp;z=15&amp;output=embed">Mostra la mappa di Google'
             '</button></div>')
    did = '<figcaption>Nord in alto · SS516 · dati © OpenStreetMap</figcaption>'
    mobile = _svg('mappa-legnaro-mobile.svg').replace('"mlt"', '"mlt2"').replace('"mld"', '"mld2"').replace(
        'aria-labelledby="mlt mld"', 'aria-labelledby="mlt2 mld2"')
    testo_col = C(
        C(etichetta('Dove siamo'),
          H('Sulla SS516, tra Padova e Piove di Sacco.', 'h2', mt=24),
          testo(f'<p>{INDIRIZZO}, {CITTA}.</p>', color=TESTO2, mt='m'),
          RAW(gmaps + JS_GMAPS, css=CSS_GMAPS, mt='l'),
          testo(f'<p><a href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps</a></p>', style='link',
                css='gpv-tap', mt='m'),
          gap='0', css='gpv-filo-int'),
        w=(50, 100, 100), pad=(0, ('xl', 'lato', 'lato'), 0, 'lato'), gap='0', css='gpv-filo-sx')
    mappa_col = C(
        RAW(f'<figure class="gpv-legnaro">{_svg("mappa-legnaro.svg")}{did}</figure>', css=CSS_MAPPA_LEGNARO,
            hide=['mobile']),
        RAW(f'<figure class="gpv-legnaro">{mobile}{did}</figure>', hide=['desktop', 'tablet']),
        w=(50, 100, 100), gap='0', css='gpv-mappa-col')
    return sezione(testo_col, mappa_col, dir='row', dir_t='column', align='center', boxed=False,
                   gap=(0, 'l', 'l'), pad=(('sezione', 64, 64), 0, ('sezione', 64, 48), 0), bg=CLS, anchor='dove-siamo')


def contatti():
    return [('recapiti', contatti_recapiti()), ('dove-siamo', contatti_mappa())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Gardens Pav · Vasche, depurazione e piattaforme per autolavaggi in calcestruzzo, Legnaro (PD)',
     'descrizione': 'Vasche monoblocco, separatori, Imhoff, prima pioggia, depuratori biologici e piattaforme prefabbricate '
                    'per autolavaggi in calcestruzzo armato vibrato, prodotti a Legnaro (PD).'},
    {'slug': '02-vasche', 'titolo': 'Vasche', 'sezioni': vasche,
     'titolo_seo': 'Vasche prefabbricate monoblocco in calcestruzzo · Gardens Pav',
     'descrizione': 'Undici vasche rettangolari e sei circolari, anche con interno in resine epossidiche: misure, pesi e '
                    'volumi, da 2,30 a 50 mc.'},
    {'slug': '03-depurazione', 'titolo': 'Depurazione', 'sezioni': depurazione,
     'titolo_seo': 'Depurazione: separatori, Imhoff, prima pioggia, biologici · Gardens Pav',
     'descrizione': 'Dissabbiatori, separatori grassi e oli, vasche Imhoff, impianti di prima pioggia e depuratori biologici '
                    'in calcestruzzo, con le tabelle di portate e misure.'},
    # titolo "Piattaforme autolavaggi": make-pages.php ritrova la pagina dallo slug del titolo (/piattaforme-autolavaggi/)
    {'slug': '04-piattaforme-autolavaggi', 'titolo': 'Piattaforme autolavaggi', 'sezioni': piattaforme,
     'titolo_seo': 'Piattaforme prefabbricate per autolavaggi · Gardens Pav',
     'descrizione': 'Pannelli in calcestruzzo Rck 45 per piste self e portali: otto modelli, fornitura, posa con personale '
                    'Gardens Pav. Brevetto depositato n° 275.271.'},
    {'slug': '05-realizzazioni', 'titolo': 'Realizzazioni', 'sezioni': realizzazioni,
     'titolo_seo': 'Realizzazioni: 36 autolavaggi con piattaforme Gardens Pav',
     'descrizione': 'Le piattaforme posate in Italia, Svizzera, Slovacchia, Francia e San Marino, con le foto dei cantieri.'},
    {'slug': '06-azienda', 'titolo': 'Azienda', 'sezioni': azienda,
     'titolo_seo': 'Azienda · Gardens Pav S.r.l., Legnaro (PD)',
     'descrizione': 'Manufatti in calcestruzzo armato vibrato C35/45 per il trattamento delle acque e piattaforme per '
                    'autolavaggi. Dati societari e norme.'},
    {'slug': '07-contatti', 'titolo': 'Contatti', 'sezioni': contatti,
     'titolo_seo': 'Contatti e richiesta all’ufficio tecnico · Gardens Pav',
     'descrizione': 'Via Romea 154/A, 35020 Legnaro (PD). Tel. 049 641591, info@gardenspav.it. Dal lunedì al venerdì 8-12 '
                    'e 14-18.'},
]
