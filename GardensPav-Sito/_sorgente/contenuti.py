# -*- coding: utf-8 -*-
"""
Contenuti del sito Gardens Pav S.r.l. (Legnaro, PD): vasche monoblocco, depurazione e piattaforme per autolavaggi
in calcestruzzo armato vibrato.

Direzione "La misura" (specifica in _prova/spec.md): la disciplina dei cataloghi di Escofet e Rieder (grottesco pieno,
monospazio per i dati, filetti, una foto vera e nitida), il capo di sezione con le stanghette preso dai disegni quotati
dell'azienda, la tavola tecnica come immagine. Innesti dalla direzione "Il lavoro in primo piano": la vasca 550 quotata,
l'indice con i conteggi, i numeri dell'attrito, la striscia del materiale.
Fonti dei testi: sito attuale (01-analisi-sito-attuale.md, verbatim corretti), tabelle ripulite
(_prova/spec-dati/tabelle-pulite.json), cantieri (_prova/spec-dati/cantieri.json), dati societari da fonti pubbliche.
"""
import json
import os

import motore as m
from motore import C, H, T, B, I, RAW, MENU

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
        'h4':        _st(ARCHIVO, '600', (18, 18, 17), 1.3),
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
    p['css'] = ('gpv-sito ' + p.get('css', '')).strip()
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
    'padding-bottom:7px!important}.gpv-tab-scorre .gpv-tabella tr>*:first-child{position:sticky;left:0;background:#FFFFFF!important}}'
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
             RAW(JS_TESTATA, css=CSS_COMUNE + CSS_TESTATA + CSS_NAV_FALLBACK),
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
    cantieri = json.load(open(os.path.join(os.path.dirname(QUI), '_prova', 'spec-dati', 'cantieri.json'),
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


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Gardens Pav · Vasche, depurazione e piattaforme per autolavaggi in calcestruzzo, Legnaro (PD)',
     'descrizione': 'Vasche monoblocco, separatori, Imhoff, prima pioggia, depuratori biologici e piattaforme prefabbricate '
                    'per autolavaggi in calcestruzzo armato vibrato, prodotti a Legnaro (PD).'},
]
