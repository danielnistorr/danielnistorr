# -*- coding: utf-8 -*-
"""
Contenuti del sito Benvegnù S.r.l.
Direzione: la prima versione (bianco, nero, Barlow Condensed) rifinita sui siti premium reali della filiera:
- hero divisa nero + foto a tutta altezza (Gruppo Mastrotto, Santoni)
- blocchi foto grandi con il titolo sopra l'immagine (Rubelli, Santoni)
- striscia prodotti a colori su fondo chiaro (Vibram)
- interfaccia piccola e pulita, molto spazio, rosso Benvegnù solo come accento (Oerlikon Riri)
Fonti dei testi: sito attuale ripulito, catalogo online (874 articoli, crawl del 4 ottobre 2026), Registro Imprese, scheda Google.
"""
import json
import os
from urllib.parse import quote

import motore as m
from motore import C, H, T, B, I, MAPPA, LINEA_H, ARTICOLI, RAW, MENU, SHORTCODE

QUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------------------------
# Tema
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'
NERO = '#111111'
GRIGIO = '#F3F3F1'         # superfici chiare: striscia prodotti, blocco visita, pannello modulo
TESTO2 = '#5A5A5A'         # testo secondario su bianco (6,9:1)
SU_NERO2 = '#B5B5B5'       # testo secondario su nero (9,6:1)
LINEA = '#E2E2E2'
LINEA_SCURA = '#333333'
ROSSO = '#9F2E29'          # il rosso storico di Benvegnù: solo numeri, voce attiva, piccoli segni
TRASP = 'rgba(0,0,0,0)'

CONDENSED = 'Barlow Condensed'
BARLOW = 'Barlow'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


TEMA = {
    'nome': 'Banco',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': NERO, 'testo2': TESTO2, 'accento': ROSSO,
    'filetto': LINEA, 'filetto_scuro': LINEA_SCURA, 'su_scuro2': SU_NERO2,
    'scuro': NERO, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': CONDENSED, 'font_testo': BARLOW, 'larghezza': 1280,
    'google_fonts': 'https://fonts.googleapis.com/css?family=Barlow+Condensed:500,600%7CBarlow:300,400,500,600&display=swap',
    'stili': {
        'display': _st(CONDENSED, '600', (88, 68, 48), 0.95, 0, True),
        'h1':      _st(CONDENSED, '600', (72, 56, 42), 0.96, 0, True),
        'h2':      _st(CONDENSED, '600', (48, 40, 32), 1.0, 0, True),
        'h3':      _st(CONDENSED, '600', (26, 24, 22), 1.1, 0.4, True),
        'h3l':     _st(CONDENSED, '600', (34, 30, 26), 1.02, 0.2, True),
        'h4':      _st(BARLOW, '600', (18, 18, 17), 1.35),
        'num':     _st(CONDENSED, '500', (36, 32, 28), 1.0),
        'cifra':   _st(CONDENSED, '600', (64, 52, 44), 0.95),
        'tel':     _st(CONDENSED, '600', (56, 48, 40), 1.0),
        'tel2':    _st(CONDENSED, '600', (40, 36, 36), 1.0),
        'mega':    _st(CONDENSED, '600', (168, 140, 120), 0.8, -1.0),      # l'unico numero grande della pagina
        'chiusura': _st(CONDENSED, '600', (144, 96, 72), 0.85, 0, True),   # "Vieni al banco" sopra la facciata
        'h2m':     _st(CONDENSED, '600', (56, 44, 34), 1.0, 0, True),
        'h2s':     _st(CONDENSED, '600', (32, 28, 26), 1.0, 0, True),
        'h2card':  _st(CONDENSED, '600', (40, 36, 36), 0.95, 0, True),
        'nome':    _st(CONDENSED, '600', (20, 20, 20), 1.1, 0, True),
        'micro':   _st(BARLOW, '500', (11, 11, 11), 1.3, 2.0, True),
        'testo15': _st(BARLOW, '400', (15, 15, 15), 1.55),
        'meta':    _st(BARLOW, '400', (13, 13, 13), 1.4),
        'nav_m':   _st(CONDENSED, '600', (24, 24, 24), 1.3, 0.5, True),
        'label':   _st(BARLOW, '500', (12, 12, 12), 1.3, 2.2, True),
        'lead':    _st(BARLOW, '300', (22, 20, 19), 1.5),
        'body':    _st(BARLOW, '400', (17, 17, 16), 1.65),
        'small':   _st(BARLOW, '400', (14, 14, 14), 1.55),
        'dati':    _st(BARLOW, '400', (15, 15, 15), 1.6),
        'link':    _st(BARLOW, '600', (13, 13, 13), 1.4, 1.6, True),
        'nav':     _st(BARLOW, '500', (13, 13, 13), 1.25, 1.6, True),
        'btn':     _st(BARLOW, '600', (13, 13, 13), 1.25, 2.0, True),
    },
    'spazi': {
        'sezione': (120, 88, 64), 'lato': (48, 32, 20), 'xl': (72, 56, 40), 'l': (48, 40, 32), 'm': (32, 24, 20),
        's': (20, 16, 16), 'xs': (12, 12, 10), 'xxs': (6, 6, 6), 'col': (24, 20, 16), 'hero_lato': (80, 32, 20), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): il pulsante si inverte, resta sempre visibile
    'bottoni': {
        'primario': (BIANCO, NERO, NERO, NERO, TRASP, NERO),
        'contorno': (NERO, TRASP, NERO, BIANCO, NERO, NERO),
        'bianco': (NERO, BIANCO, BIANCO, BIANCO, TRASP, BIANCO),
        'contorno-bianco': (BIANCO, TRASP, BIANCO, NERO, BIANCO, BIANCO),
    },
    'bottone': {'raggio': 0, 'pad': (18, 34, 18, 34), 'bordo': 1, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/BenvegnuSrl-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (un solo posto da aggiornare)
# ---------------------------------------------------------------------------------------------
TEL = '049\u00a0983\u00a00202'             # spazi indivisibili: il numero non va mai a capo
TEL_LINK = 'tel:+390499830202'
FAX = '049 983 1177'
EMAIL = 'commerciale@benvegnusrl.it'
PEC = 'info@pec.benvegnusrl.it'
INDIRIZZO = 'Via del Lavoro 48'
CITTA = '30030 Vigonovo (VE)'
ZONA = 'Zona industriale Tombelle'
ZONA_MIN = 'zona industriale Tombelle'
WJ = '\u2060'                                # word joiner: niente a capo dentro gli intervalli orari
ORARI = f'Dal lunedì al venerdì, 8:30{WJ}-{WJ}12:30 e 14:30{WJ}-{WJ}18:30'
ORARI_BREVE = f'Lun{WJ}-{WJ}ven 8:30{WJ}-{WJ}12:30 e 14:30{WJ}-{WJ}18:30'
CHIUSURA = 'Sabato e domenica chiuso'
PIVA = '02326850282'
REA = f'PD{WJ}-{WJ}222933'
SEDE_LEGALE = 'Piazzetta Primo Modin 12, 35129 Padova'
MAPS = ('https://www.google.com/maps/search/?api=1&query=Benvegn%C3%B9%20Via%20del%20Lavoro%2048%20Vigonovo'
        '&query_place_id=ChIJCYLIGbDFfkcRl5iSbyMPyb4')
CONDIZIONI_PDF = 'https://www.benvegnusrl.it/condizioni-di-vendita-Benvegnusrl.pdf'
FACEBOOK = 'https://www.facebook.com/benvegnusrl'
CF7 = '[contact-form-7 title="Richiesta disponibilità"]'


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    if corpo:
        url += '&body=' + quote(corpo)
    return url


CATALOGO = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
FAM = {f['slug']: f for f in CATALOGO['famiglie']}
TOTALE = CATALOGO['totale']                                            # 874
N_VIBRAM = sum(FAM[k]['n'] for k in ('vibram-suole', 'vibram-lastre', 'vibram-mezzesuole-tacchi'))   # 329

NOMI_SUB = {
    'Nastri x timbr.caldo': 'nastri per timbratura a caldo', 'Pinze / Tronchesi': 'pinze e tronchesi',
    'Pennarelli e refil': 'pennarelli e refill', 'Metallizz.ritorto': 'metallizzato ritorto',
    'Numerini autoad.': 'numerini autoadesivi', 'Nastri x imballo': 'nastri per imballo',
    'Suole in Gomma Monocolore': 'gomma monocolore', 'Suole in Gomma Pu': 'gomma PU', 'Suole Gumlite': 'Gumlite',
    'Suole Espanse': 'espanse', 'Lastre Compatte': 'compatte', 'Lastre Espanso': 'espanse',
    'Mezzesuole Compatto': 'mezzesuole compatte', 'Tacchi Compatti': 'tacchi compatti', 'Tacchi TPU/PU': 'tacchi TPU e PU',
}


def sottocategorie(slug, con_numeri=True):
    voci = []
    for s in FAM[slug]['sottocategorie']:
        if s['n'] == 0:
            continue
        nome = NOMI_SUB.get(s['nome'], s['nome']).strip()
        nome = nome[0].lower() + nome[1:] if not nome.startswith(('Gumlite', 'PU')) else nome
        voci.append(f'{nome} ({s["n"]})' if con_numeri else nome)
    testo = ', '.join(voci)
    return testo[0].upper() + testo[1:]


# ---------------------------------------------------------------------------------------------
# Componenti
# ---------------------------------------------------------------------------------------------
def sezione(*children, bg=BIANCO, pad=('sezione', 'lato'), **p):
    return C(*children, bg=bg, pad=pad, tag='section', **p)


def link_freccia(testo, url, colore=NERO, hover=ROSSO, **p):
    """Link testuale in maiuscolo con freccia, come i "Scopri" dei siti di marca."""
    classi = ('bv-tap ' + p.pop('css', '')).strip()
    return T(f'<p><a href="{url}">{testo}&nbsp;&nbsp;→</a></p>', style='link', color=colore, link_color=colore,
             link_hover=hover, css=classi, **p)


def intestazione(titolo, lead, max_w=760, filetto=True):
    # senza filetto quando la sezione dopo apre con una riga che ha già il suo filetto (niente doppie linee)
    return sezione(
        C(H(titolo, 'h1'), T(f'<p>{lead}</p>', style='lead', color=TESTO2, max_w=max_w), gap='m'),
        pad=('xl', 'lato', 'l', 'lato'), anchor='content', **({'border_bottom': 1, 'border_color': LINEA} if filetto else {}))


def hero_divisa(titolo, lead, pulsanti, foto, alt, foto_mobile=None, livello='h1', stile='display', min_h=680):
    """Hero divisa: pannello nero con il titolo a sinistra, foto a tutta altezza a destra (Mastrotto, Santoni)."""
    testo = C(H(titolo, livello, style=stile, color=BIANCO),
              T(f'<p>{lead}</p>', style='lead', color=SU_NERO2, max_w=520),
              C(*pulsanti, dir='row', dir_m='column', gap='s', mt='xs'),
              w=(50, 100, 100), gap='m', justify='center', pad=('xl', 'xl', 'xl', 'hero_lato'), min_h=(min_h, 0, 0),
              bg=NERO)
    # foto come sfondo del contenitore: riempie sempre l'altezza del pannello nero, qualunque sia la lunghezza del testo
    immagine = C(w=(50, 100, 100), min_h=(min_h, 520, 300), img=img(foto), alt=alt, hide=['mobile'] if foto_mobile else None)
    figli = [testo, immagine]
    if foto_mobile:
        figli.append(C(w=(100, 100, 100), min_h=(300, 300, 280), img=img(foto_mobile), alt=alt, hide=['desktop', 'tablet']))
    return C(*figli, dir='row', dir_t='column', boxed=False, pad='0', gap='0', bg=NERO, tag='section', anchor='content')


def blocco_foto(titolo, testo, conteggio, foto, link):
    """Blocco grande con foto come navigazione: titolo e dati sopra la foto scurita (Rubelli, Santoni)."""
    return C(
        T(f'<p>{conteggio}</p>', style='label', color=BIANCO),
        H(titolo, 'h3', style='h3l', color=BIANCO),
        T(f'<p>{testo}</p>', style='small', color='#E6E6E6', max_w=420),
        T('<p>Vedi&nbsp;&nbsp;→</p>', style='link', color=BIANCO, mt='xxs'),   # testo, non link: il blocco intero è il link
        w=(49, 48.5, 100), min_h=(460, 380, 300), justify='end', gap='xs', pad=('l', 'l', 'l', 'l'),
        img=img(foto), alt=titolo, scrim=(20, 0.06, 0.8), link=link, overflow=True)


def riga_indice(numero, titolo, testo, destra=None, colore=NERO, colore_testo=TESTO2, colore_num=ROSSO,
                linea=LINEA, link=None, ancora=None):
    centro = C(H(titolo, 'h3', color=colore), T(f'<p>{testo}</p>', style='body', color=colore_testo), gap='xxs', grow=True)
    figli = [H(numero, 'p', style='num', color=colore_num, fisso=True, w_px=(64, 56, None))] if numero else []
    figli.append(centro)
    if destra:
        figli.append(T(f'<p>{destra}</p>', style='label', color=colore, align=('right', 'right', 'left'), fisso=True))
    return C(*figli, dir='row', dir_m='column', gap=('m', 's', 'xxs'), pad=('m', '0', 'm', '0'), border_top=1,
             border_color=linea, align=('baseline', 'baseline', 'start'), link=link, anchor=ancora)


# larghezze esatte delle griglie: (contenuto - spazi) / colonne, così l'ultima scheda arriva al bordo della colonna
W4 = (23.59, 48.9, 100)      # 4 per riga su desktop (1280 - 3x24), 2 su tablet (960 - 20), una per riga su telefono
W3 = (32.0, 31.9, 100)       # 3 per riga su desktop e tablet

# scheda prodotto: la foto si ingrandisce appena al passaggio, dentro la sua cornice (niente dissolvenze)
CSS_SCHEDE = (
    '.bvg-scheda .bvg-foto{overflow:hidden}'
    '.bvg-scheda img{transition:transform .5s ease}'
    '.bvg-scheda:hover img,.bvg-scheda:focus-visible img{transform:scale(1.045)}'
    f'.bvg-scheda:hover h4,.bvg-scheda:hover .elementor-heading-title{{color:{ROSSO}}}'
)


def scheda_prodotto(pid, nome, famiglia, nota, link=None, w=W4):
    """Scheda prodotto alla maniera dei siti di marca: foto su bianco, famiglia in piccolo, nome, una riga.
    Su telefono diventa una riga (foto a sinistra, testo a destra): niente schede orfane in una griglia a due."""
    foto = C(I(img(f'prodotto-{pid}.jpg'), nome), bg=BIANCO, border=1, border_color=LINEA, w=(100, 100, 34), fisso=True,
             css='bvg-foto')
    testo = C(T(f'<p>{famiglia}</p>', style='label', color=TESTO2),
              H(nome, 'h4', style='h4'),
              T(f'<p>{nota}</p>', style='small', color=TESTO2),
              gap='xxs', w=(100, 100, 62), mt=('xs', 'xs', 0))
    return C(foto, testo, w=w, gap=('xxs', 'xxs', 's'), dir='column', dir_m='row', align=('stretch', 'stretch', 'center'),
             link=link, css='bvg-scheda')


def griglia_schede(schede):
    # il widget con il CSS sta fuori dalla griglia: dentro occuperebbe un posto e manderebbe a capo una riga vuota
    return C(C(*schede, dir='row', wrap=True, justify='start', gap='col', gap_r=('l', 'l', 's')), RAW('', css=CSS_SCHEDE),
             gap='0')


def blocco_banco(titolo='Vieni al banco', pulsante=None):
    """Indirizzo, orari, telefono: fondo chiaro, telefono grande. Su tutte le pagine tranne Contatti."""
    b1 = pulsante or B('Apri in Google Maps', MAPS, variant='primario', full_m=True)
    return sezione(
        C(H(titolo, 'h2'),
          T(f'<p>{INDIRIZZO}, {ZONA_MIN}, {CITTA}.<br>Parcheggio clienti davanti al negozio.</p>'
            f'<p>{ORARI}.<br>{CHIUSURA}.</p>', style='lead', color=NERO, link_color=NERO, link_hover=ROSSO),
          w=(50, 100, 100), gap='m'),
        C(T('<p>Telefono</p>', style='label', color=TESTO2),
          H(TEL, 'p', style='tel', color=NERO, link=TEL_LINK),
          T(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>', style='body', color=NERO, link_color=NERO, link_hover=ROSSO),
          C(b1, B('Scrivi una email', mailto('Richiesta informazioni'), variant='contorno', full_m=True),
            dir='row', dir_m='column', gap='s', mt='s'),
          w=(42, 100, 100), gap='xs'),
        bg=GRIGIO, dir='row', dir_t='column', justify='between', gap='xl', anchor='banco')


# ---------------------------------------------------------------------------------------------
# Header e footer (template separati; con Ultimate Addons diventano header e footer di tutto il sito)
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Catalogo', '/catalogo/'), ('Vibram', '/vibram/'), ('Marchi', '/marchi/'), ('Azienda', '/azienda/'),
             ('Novità', '/novita/'), ('Contatti', '/contatti/')]

CSS_BASE = (
    'em,i,cite{font-style:normal}'
    f'a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{{outline:2px solid {ROSSO};outline-offset:3px}}'
    # il menu Ultimate Addons va a capo prima di riempire lo spazio: su desktop le voci restano su una riga
    '@media (min-width:1025px){.hfe-nav-menu__layout-horizontal .hfe-nav-menu{flex-wrap:nowrap}.hfe-nav-menu .hfe-menu-item{white-space:nowrap}}'
    # su tablet e telefono il menu chiuso resta impaginato (invisibile) e sporge a destra: lo taglio in orizzontale,
    # in verticale la tendina aperta scende normalmente
    '.bvg-testata{overflow-x:clip}'
    '.elementor-widget-text-editor ul{list-style:none;margin:0;padding:0}'
    f'.elementor-widget-text-editor li{{margin:0;padding:10px 0;border-top:1px solid {LINEA}}}'
    f'.elementor-widget-text-editor li:last-child{{border-bottom:1px solid {LINEA}}}'
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}.elementor-widget-text-editor p{text-wrap:pretty}'
    # come nel fallback: l'ultimo paragrafo di un testo non aggiunge 0,9em di spazio sotto
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    f"a.hfe-skip-link:focus{{background:{NERO};color:{BIANCO};border-radius:0;box-shadow:none;outline:2px solid {BIANCO};"
    f"outline-offset:-4px;font:600 14px/1 '{BARLOW}',Arial,sans-serif;letter-spacing:1.6px;text-transform:uppercase;"
    'text-decoration:none;padding:16px 24px}'
)

# aree di tocco: i link testuali restano uguali a vista ma si toccano su circa 40 px
CSS_TAP = (
    '.bv-tap a{display:inline-block;padding:12px 0;margin:-12px 0}'
    '@media (max-width:1024px){.bv-tap-lista p{line-height:40px}.bv-tap-lista a{display:inline-block}}'
)


def header():
    barra = C(
        T(f'<p>Banco aperto {ORARI_BREVE.lower()}</p>', style='small', color=SU_NERO2, hide=['mobile']),
        T(f'<p>{ORARI_BREVE}</p>', style='small', color=SU_NERO2, hide=['desktop', 'tablet']),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="mailto:{EMAIL}">{EMAIL}</a></p>', style='small',
          color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2, align='right', hide=['mobile'], css='bv-tap'),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='small', color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2,
          align='right', hide=['desktop', 'tablet'], css='bv-tap'),
        dir='row', justify='between', align='center', gap='s', pad=(9, 'lato'), bg=NERO, boxed=True)
    marchio = C(I(img('logo-benvegnu-nero.png'), 'Benvegnù S.r.l.', link='/', w_img=(176, 156, 136), fisso=True,
                  link_label='Benvegnù S.r.l. pagina iniziale'),
                dir='row', align='center', w=(30, 50, 55))
    azioni = C(
        T(f'<p><a href="{TEL_LINK}">Chiama</a></p>', style='link', color=NERO, link_color=NERO, link_hover=ROSSO,
          hide=['desktop'], fisso=True, css='bv-tap'),
        MENU(VOCI_MENU, colore=NERO, accento=ROSSO, fondo_menu=BIANCO, linea=LINEA, stile='nav', stile_mobile='nav_m',
             spazio=32, pad_v=8, distanza=12, align_menu='right', fisso=True, larg=(None, 40, 40)),
        B('Chiedi disponibilità', '/contatti/#modulo', variant='contorno', hide=['tablet', 'mobile'], fisso=True),
        dir='row', align='center', justify='end', gap=('l', 's', 's'), w=(70, 50, 45))
    testata = C(marchio, azioni, dir='row', justify='between', align='center', gap='m', min_h=(84, 72, 64),
                pad=(10, 'lato'), bg=BIANCO, border_bottom=1, border_color=LINEA, boxed=True)
    return C(barra, testata, RAW('', css=CSS_BASE, solo_elementor=True), RAW('', css=CSS_TAP), pad='0', boxed=False,
             tag='header', bg=BIANCO, css='bvg-testata')


def footer():
    def colonna(titolo, html):
        return C(T(f'<p>{titolo}</p>', style='label', color=SU_NERO2),
                 T(html, style='dati', color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2, sottolinea=False,
                   css='bv-tap-lista'), gap='s',
                 w=(22, 46, 100))
    pagine = ''.join(f'<a href="{u}">{t}</a><br>' for t, u in VOCI_MENU)
    righe = C(
        C(I(img('logo-benvegnu-bianco.png'), 'Benvegnù S.r.l.', link='/', w_img=(176, 160, 150),
            link_label='Benvegnù S.r.l. pagina iniziale'),
          T('<p>Componenti, accessori e utensili per calzatura e pelletteria. Vigonovo, dal 1980.</p>', style='dati',
            color=SU_NERO2, max_w=300), gap='m', w=(28, 46, 100)),
        colonna('Il banco', f'<p>{INDIRIZZO}<br>{CITTA}<br>{ZONA}</p>'),   # gli orari sono già nella barra in alto
        colonna('Contatti', f'<p>Tel. <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
                            f'PEC {PEC}</p>'),
        colonna('Pagine', f'<p>{pagine}<a href="{CONDIZIONI_PDF}">Condizioni di vendita (PDF)</a></p>'),
        dir='row', dir_m='column', wrap=(False, True, False), justify='between', gap=('m', 'l', 'l'))
    legale = C(
        T(f'<p>© 2026 Benvegnù S.r.l. · P.IVA {PIVA} · REA {REA} · Sede legale {SEDE_LEGALE}</p>', style='small', color=SU_NERO2),
        T(f'<p><a href="/privacy/">Privacy</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="/cookie/">Cookie</a>&nbsp;&nbsp;·&nbsp;&nbsp;'
          f'<a href="{FACEBOOK}">Facebook</a></p>', style='small', color=SU_NERO2, link_color=SU_NERO2, link_hover=BIANCO, sottolinea=False,
          align=('right', 'right', 'left'), fisso=True, css='bv-tap'),
        dir='row', dir_m='column', justify='between', gap='s', pad=('m', '0', '0', '0'), border_top=1, border_color=LINEA_SCURA)
    return C(righe, legale, gap='xl', pad=('xl', 'lato', 'l', 'lato'), bg=NERO, tag='footer')


# ---------------------------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------------------------
def home():
    n_tomaia = FAM['filati-elastici']['n'] + FAM['modelleria-riparazione']['n']
    n_cura = sum(FAM[k]['n'] for k in ('prodotti-chimici', 'esposizione-cura', 'igiene-sicurezza', 'imballaggio'))
    apertura = hero_divisa(
        'Forniture per calzaturifici, pelletterie e\u00a0calzolai',
        'Suole e lastre Vibram, filati, utensili e prodotti per la rifinitura del fondo e della tomaia. '
        'Al banco di Vigonovo, nella Riviera del Brenta, dal 1980.',
        [B('Sfoglia il catalogo', '/catalogo/', variant='bianco', full_m=True),
         B('Come arrivare', MAPS, variant='contorno-bianco', full_m=True)],
        'sede-hero.jpg', 'La sede Benvegnù in Via del Lavoro 48 a Vigonovo', foto_mobile='sede-hero-mobile.jpg')

    catalogo = sezione(
        C(H('Il catalogo', 'h2'),
          C(T(f'<p>{TOTALE} articoli in 10 famiglie, dagli utensili alle suole Vibram. Quello che non trovi online, '
              'chiedilo al banco.</p>', style='body', color=TESTO2),
            link_freccia('Tutto il catalogo', '/catalogo/'), gap='s', w=(40, 60, 100)),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='m'),
        C(blocco_foto('Vibram', 'Suole, lastre, mezzesuole e tacchi', f'{N_VIBRAM} articoli', 'blocco-vibram.jpg', '/vibram/'),
          blocco_foto('Utensili', 'Forbici, coltelli, lesine, punzoni, martelli, mole, strumenti di misura, torchi',
                      f'{FAM["utensili"]["n"]} articoli', 'blocco-utensili.jpg', '/catalogo/#utensili'),
          blocco_foto('Tomaia e modelleria', 'Filati, elastici, allungaforme, alzi, materiali per modelleria e riparazione',
                      f'{n_tomaia} articoli', 'blocco-tomaia.jpg', '/catalogo/#filati-elastici'),
          blocco_foto('Cura, esposizione e imballo', 'Prodotti Girba, cura della scarpa, calzanti, guanti, nastri ed etichette',
                      f'{n_cura} articoli', 'blocco-cura.jpg', '/catalogo/#esposizione-cura'),
          dir='row', wrap=True, justify='between', gap='col', gap_r='col'),
        gap='l', anchor='catalogo')

    return [('apertura', apertura), ('catalogo', catalogo), ('dal-catalogo', striscia_catalogo()),
            ('vibram', vibram_al_banco()), ('per-chi-lavoriamo', per_chi_lavoriamo()), ('banco', chiusura_banco())]


# ---------------------------------------------------------------------------------------------
# Home sotto il catalogo: quattro sezioni, ognuna con un'idea e un gesto
# (ricerca su siti reali: striscia di Valextra con cella di testo di Edward Green; fascia nera di Edward Green e
# Gruppo Mastrotto con la foto che esce dalla fascia; dichiarazione con i loghi come contesto di Lampo; titolo grande
# appoggiato sulla foto della fascia sostenibilità di Mastrotto e righe d'indice di Ernest Wright e Vitsoe)
# ---------------------------------------------------------------------------------------------
CSS_KICKER = (
    '.bv-kicker p{display:flex;align-items:center;gap:16px;margin:0}'
    ".bv-kicker p::before{content:'';flex:0 0 48px;height:1px;background:currentColor}"
)

# articoli della striscia: (id foto, famiglia, nome, dettaglio verificato sul catalogo, link)
# dettagli dalle varianti del sito attuale: Liverpool 4 colori x 7 misure, Crepe 4 colori 90x60, Tera 7, Mara 6, Lariz 4;
# "Cod." solo dove il catalogo ha un codice articolo (gli altri numeri sono id di pagina, non codici)
STRISCIA = [
    ('80075', 'Suole Vibram', '2600 Liverpool', 'Gumlite, 4 colori, 7 misure', '/vibram/#vibram-suole'),
    ('1895', 'Utensili', 'Forbici Lariz lame curve', 'Da lavoro, 4 misure', '/catalogo/#utensili'),
    ('1030', 'Filati ed elastici', 'Gütermann Tera', 'Poliestere ritorto, 7 varianti', '/catalogo/#filati-elastici'),
    ('82268', 'Lastre Vibram', '7106 Crepe', 'Gomma morbida, 90 x 60 cm, 4 colori', '/vibram/#vibram-lastre'),
    ('14932', 'Utensili', 'Calibro digitale', 'Portata 200 mm, risoluzione 0,01 mm · Cod. 14932', '/catalogo/#utensili'),
    ('80751', 'Tacchi Vibram', '1100T Montagna', 'Tacco 20,5 mm, mescola Vibram Mont', '/vibram/#vibram-mezzesuole-tacchi'),
    ('15887', 'Filati ed elastici', 'Gütermann Mara', 'Poliestere ritorto, 6 varianti', '/catalogo/#filati-elastici'),
    ('9978', 'Utensili', 'Coltello C.Dick Original', 'Misura 270 x 20 mm · Cod. 9978', '/catalogo/#utensili'),
    ('15752', 'Esposizione e cura', 'Tendiscarpa in cedro', 'Modello European · Cod. 15752', '/catalogo/#esposizione-cura'),
    ('14563', 'Modelleria e riparazione', 'Forma allargascarpe 2Way', 'Dasco · Cod. 14563', '/catalogo/#modelleria-riparazione'),
    ('7995', 'Esposizione e cura', 'Calzante Longuette GT', 'Anatomico · Cod. 7995', '/catalogo/#esposizione-cura'),
    ('15531', 'Imballaggio', 'Etichette Made in Italy', '28 x 8 mm, 5000 pezzi · Cod. 15531', '/catalogo/#imballaggio'),
]
CELLA = (312, 288, 300)
FINE = {'14932', '9978'}        # oggetti sottili (calibro, coltello): ingranditi nella loro cella

CSS_STRISCIA = (
    # binario: scorre di lato con aggancio alle schede; il primo bordo è allineato alla griglia di 1280, la fine sborda
    '.bv-strip .bv-track{flex-wrap:nowrap!important;overflow-x:auto!important;overflow-y:hidden;scroll-snap-type:x mandatory;'
    'scrollbar-width:thin;scrollbar-color:#111111 #E2E2E2;padding-left:max(48px,calc((100% - 1280px)/2))!important;'
    'scroll-padding-left:max(48px,calc((100% - 1280px)/2))}'
    # con JavaScript ci sono frecce e barra rossa: la barra di scorrimento del browser si nasconde
    '.bv-strip.bv-js .bv-track{scrollbar-width:none}.bv-strip.bv-js .bv-track::-webkit-scrollbar{display:none}'
    ".bv-strip .bv-track::after{content:'';flex:0 0 max(48px,calc(100% - 1280px))}"
    '.bv-strip .bv-track>*{scroll-snap-align:start}'
    '.bv-strip .bv-img{overflow:hidden}'
    '.bv-strip .bv-img img{display:block;width:100%;height:auto;transition:transform .4s ease}'
    '.bv-strip .bv-fine img{transform:scale(1.3)}'
    '@media (hover:hover){.bv-strip .bv-card:hover .bv-img img{transform:scale(1.04)}'
    '.bv-strip .bv-card:hover .bv-fine img{transform:scale(1.35)}'
    '.bv-strip .bv-card:hover .bv-name,.bv-strip .bv-card:hover .bv-name .elementor-heading-title'
    '{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:4px}}'
    '@media (prefers-reduced-motion:reduce){.bv-strip .bv-img img{transition:none}}'
    f'.bv-strip .bv-card:focus-visible,.bv-strip .bv-track:focus-visible{{outline:2px solid {ROSSO};outline-offset:-3px}}'
    # comandi: barra di avanzamento rossa sottile e due frecce quadrate (si riempiono di nero, mai dissolvenze)
    '.bv-strip .bv-ctrl{max-width:1280px;margin:32px auto 0;padding:0 48px;box-sizing:content-box;display:flex;align-items:center;gap:24px}'
    '.bv-strip .bv-ctrl[hidden]{display:none}'
    '.bv-strip .bv-bar{flex:1;height:1px;background:#CFCFCF;position:relative}'
    f'.bv-strip .bv-thumb{{position:absolute;top:-1px;left:0;height:3px;width:30%;background:{ROSSO}}}'
    '.bv-strip .bv-btns{display:flex;gap:8px}'
    f".bv-strip .bv-ctrl .bv-btn{{width:48px;height:48px;padding:0;border:1px solid {NERO};border-radius:0;background:{BIANCO};"
    f"color:{NERO};font:400 18px/1 '{BARLOW}',Arial,sans-serif;cursor:pointer;box-shadow:none;transition:background-color .2s,color .2s}}"
    f'.bv-strip .bv-ctrl .bv-btn:hover:not([aria-disabled=true]),.bv-strip .bv-ctrl .bv-btn:focus-visible{{background:{NERO};color:{BIANCO};border-color:{NERO}}}'
    f'.bv-strip .bv-ctrl .bv-btn[aria-disabled=true],.bv-strip .bv-ctrl .bv-btn[aria-disabled=true]:hover{{background:{BIANCO};border-color:#CFCFCF;color:#BDBDBD;cursor:default}}'
    f'.bv-strip .bv-ctrl .bv-btn[aria-disabled=true]:focus-visible{{outline:2px solid {ROSSO};outline-offset:2px}}'
    '@media (max-width:1024px){.bv-strip .bv-track{padding-left:32px!important;scroll-padding-left:32px}'
    '.bv-strip .bv-track::after{flex-basis:32px}.bv-strip .bv-ctrl{padding:0 32px}}'
    '@media (max-width:767px){.bv-strip .bv-track{padding-left:20px!important;scroll-padding-left:20px}'
    '.bv-strip .bv-track::after{flex-basis:20px}.bv-strip .bv-ctrl{margin-top:24px;padding:0 20px}'
    '.bv-strip .bv-ctrl .bv-btn{width:44px;height:44px}}'
)

# frecce e barra: senza JavaScript restano nascoste (lo scorrimento a mano e l'aggancio funzionano comunque)
JS_STRISCIA = (
    "(function(){function go(){document.querySelectorAll('.bv-strip').forEach(function(w){"
    "var s=w.querySelector('.bv-track'),c=w.querySelector('.bv-ctrl');if(!s||!c||c.dataset.ok)return;c.dataset.ok=1;"
    "var t=c.querySelector('.bv-thumb'),p=c.querySelector('.bv-prev'),n=c.querySelector('.bv-next');c.hidden=false;"
    "w.classList.add('bv-js');"
    "s.setAttribute('tabindex','0');s.setAttribute('role','region');s.setAttribute('aria-label','Articoli dal catalogo');"
    "var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches,bh=rm?'auto':'smooth';"
    "function st(){var k=s.children[1]||s.children[0];return k?k.getBoundingClientRect().width:300}"
    "function up(){var m=s.scrollWidth-s.clientWidth,v=s.clientWidth/s.scrollWidth,r=m>0?s.scrollLeft/m:0;"
    "t.style.width=(v*100)+'%';t.style.left=(r*(1-v)*100)+'%';"
    "p.setAttribute('aria-disabled',s.scrollLeft<=2);n.setAttribute('aria-disabled',s.scrollLeft>=m-2)}"
    "p.addEventListener('click',function(){if(this.getAttribute('aria-disabled')==='true')return;s.scrollBy({left:-st(),behavior:bh})});"
    "n.addEventListener('click',function(){if(this.getAttribute('aria-disabled')==='true')return;s.scrollBy({left:st(),behavior:bh})});"
    "s.addEventListener('focusin',function(e){var k=e.target.closest&&e.target.closest('.bv-card');if(!k)return;"
    "var a=k.getBoundingClientRect(),b=s.getBoundingClientRect(),pl=parseFloat(getComputedStyle(s).scrollPaddingLeft)||0;"
    "if(a.left<b.left+pl-1||a.right>b.right+1){s.scrollTo({left:s.scrollLeft+a.left-b.left-pl,behavior:bh})}});"
    "s.addEventListener('keydown',function(e){if(e.target!==s)return;if(e.key==='Home'||e.key==='End'){e.preventDefault();"
    "s.scrollTo({left:e.key==='Home'?0:s.scrollWidth,behavior:bh})}});"
    "s.addEventListener('scroll',up,{passive:true});window.addEventListener('resize',up);up()})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();"
)
HTML_COMANDI = (
    '<div class="bv-ctrl" hidden><div class="bv-bar"><span class="bv-thumb"></span></div><div class="bv-btns">'
    '<button type="button" class="bv-btn bv-prev" aria-label="Articoli precedenti">&larr;</button>'
    '<button type="button" class="bv-btn bv-next" aria-label="Articoli successivi">&rarr;</button></div></div>'
)


def striscia_catalogo():
    """S1: striscia di articoli tra filetti neri, aperta da una cella di testo nera; scorre di lato (Valextra, Edward Green)."""
    def testo_cella():
        return [C(T('<p>Dal catalogo</p>', style='label', color=SU_NERO2, css='bv-kicker'),
                  H('Col codice facciamo prima', 'h2', style='h2card', color=BIANCO, mt=24),
                  T('<p>Per riordinare servono il codice o il nome dell’articolo, più il colore o la misura. Basta una '
                    'telefonata o una email.</p>', style='testo15', color=SU_NERO2, mt=20), gap='0'),
                link_freccia('Sfoglia il catalogo', '/catalogo/', colore=BIANCO, hover=SU_NERO2)]
    # desktop e tablet: prima cella della striscia; telefono: blocco nero sopra la striscia, così la prima scheda si vede intera
    cella_testo = C(*testo_cella(), larg_px=CELLA, bg=NERO, pad=(32, 28, 24), justify='between', gap='m', border=1,
                    border_color=NERO, hide=['mobile'])
    blocco_mobile = C(C(*testo_cella(), bg=NERO, pad=(32, 24, 32, 24), gap='m', justify='between'), pad=(0, 20, 0, 20),
                      hide=['desktop', 'tablet'])
    schede = []
    for pid, famiglia, nome, dettaglio, link in STRISCIA:
        schede.append(C(
            C(I(img(f'prodotto-{pid}.jpg'), nome), pad=(24, 24, 24), bg=BIANCO, css='bv-img bv-fine' if pid in FINE else 'bv-img'),
            C(T(f'<p>{famiglia}</p>', style='micro', color=TESTO2),
              H(nome, 'h3', style='nome', color=NERO, mt=8, css='bv-name'),
              T(f'<p>{dettaglio}</p>', style='meta', color=TESTO2, mt=6),
              pad=((4, 4, 4), (24, 24, 20), (24, 24, 20), (24, 24, 20)), min_h=(112, 112, 104), gap='0'),
            larg_px=CELLA, bg=BIANCO, link=link, gap='0', border_top=1, border_right=1, border_bottom=1, border_color=NERO,
            css='bv-card'))
    # overflow anche nel JSON: se il widget HTML perdesse il suo CSS, la striscia scorrerebbe comunque
    binario = C(cella_testo, *schede, dir='row', wrap=False, gap='0', pad='0', css='bv-track', overflow='auto')
    return C(blocco_mobile, binario, RAW(HTML_COMANDI + f'<script>{JS_STRISCIA}</script>', css=CSS_STRISCIA), bg=BIANCO, boxed=False,
             pad=((0, 0, 0), (0, 0, 0), (160, 120, 64), (0, 0, 0)), gap='0', tag='section',
             css='bv-strip')


CSS_RIGHE = (
    CSS_KICKER +
    '.bv-rows{margin-top:32px}'
    f'.bv-rows .bv-row{{display:flex;align-items:baseline;height:52px;padding:15px 8px 15px 0;color:{BIANCO};text-decoration:none}}'
    f".bv-rows .bv-row__n,.bv-rows .bv-row__c{{font:600 22px/1 '{CONDENSED}',Arial,sans-serif;text-transform:uppercase;color:{BIANCO}}}"
    '.bv-rows .bv-row__c{font-weight:500;font-variant-numeric:tabular-nums}'
    '.bv-rows .bv-row__d{flex:1;margin:0 16px;border-bottom:1px dotted rgba(255,255,255,.35);transform:translateY(-6px)}'
    f".bv-rows .bv-row__a{{margin-left:16px;font:400 16px/1 '{BARLOW}',Arial,sans-serif;color:{SU_NERO2};transition:transform .2s,color .2s}}"
    f'.bv-rows .bv-row:hover .bv-row__d,.bv-rows .bv-row:focus-visible .bv-row__d{{border-bottom-style:solid;border-color:{BIANCO}}}'
    f'.bv-rows .bv-row:hover .bv-row__a,.bv-rows .bv-row:focus-visible .bv-row__a{{transform:translateX(4px);color:{BIANCO}}}'
    f'.bv-rows .bv-row:focus-visible{{outline:2px solid {BIANCO};outline-offset:0}}'
    '@media (max-width:1024px){.bv-rows .bv-row{height:48px;padding:14px 8px 14px 0}.bv-rows .bv-row__n,.bv-rows .bv-row__c{font-size:20px}}'
    '@media (max-width:767px){.bv-rows .bv-row{height:52px;padding:16px 8px 16px 0}}'
    '@media (prefers-reduced-motion:reduce){.bv-rows .bv-row__a{transition:none}}'
)


def vibram_al_banco():
    """S2: fascia nera, la foto dell'espositore esce sopra e sotto la fascia; un solo numero grande; righe a puntini."""
    famiglie = [('Suole', 'vibram-suole'), ('Lastre', 'vibram-lastre'), ('Mezzesuole e tacchi', 'vibram-mezzesuole-tacchi')]
    righe = ''.join(f'<a class="bv-row" href="/vibram/#{slug}"><span class="bv-row__n">{nome}</span>'
                    f'<span class="bv-row__d" aria-hidden="true"></span><span class="bv-row__c">{FAM[slug]["n"]}</span>'
                    f'<span class="bv-row__a" aria-hidden="true">&rarr;</span></a>' for nome, slug in famiglie)
    foto = C(w=(50, 50, 100), min_h=(0, 0, 390), img=img('espositore-vibram.jpg'), img_pos='center left',
             alt='Espositore Vibram al banco Benvegnù',
             mt=(-40, -32, 0), mb=(-40, -32, 0), z=2)
    pannello = C(
        T('<p>Rivenditore autorizzato Vibram</p>', style='label', color=SU_NERO2, css='bv-kicker'),
        H(str(N_VIBRAM), 'p', style='mega', color=BIANCO, mt=32),
        H('Articoli Vibram al banco', 'h2', style='h2s', color=BIANCO, mt=12),
        T('<p>Per chi produce e per chi ripara. Partiamo da modello e misura, poi verifichiamo colore e disponibilità.</p>',
          style='body', color=SU_NERO2, max_w=440, mt=16),
        RAW(f'<nav class="bv-rows" aria-label="Famiglie Vibram">{righe}</nav>', css=CSS_RIGHE),
        B('La pagina Vibram', '/vibram/', variant='bianco', full_m=True, mt=32),
        w=(50, 50, 100), pad=((72, 56, 56), (80, 32, 20), (72, 56, 64), (96, 40, 20)), justify='center', gap='0')
    riga = C(foto, pannello, dir='row', dir_m='column', align='stretch', gap='0', min_h=(720, 600, 0), pad='0',
             boxed=True, boxed_width=1600)
    # e-no-lazyload: Elementor non differisce lo sfondo (senza JavaScript la foto resterebbe nera)
    return C(riga, bg=NERO, boxed=False, pad='0', gap='0', tag='section', css='e-no-lazyload')


def per_chi_lavoriamo():
    """S3: una dichiarazione semplice accanto ai marchi del banco, in una griglia 2x2 con filetti interni (Lampo)."""
    marchi = [('vibram', 'Vibram', 'Suole, lastre, tacchi', '/vibram/', (52, 46, 44)),
              ('gutermann', 'Gütermann', 'Filati Mara e Tera', '/catalogo/#filati-elastici', (48, 44, 40)),
              ('girba', 'Girba', 'Tinture e finissaggio', '/catalogo/#prodotti-chimici', (64, 56, 50)),
              ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi', '/marchi/', (48, 42, 38))]
    bordi = [dict(border_right=1, border_bottom=1), dict(border_bottom=1), dict(border_right=1), {}]
    celle = []
    for (slug, nome, etichetta, link, h), b in zip(marchi, bordi):
        celle.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=h, fit='contain'), min_h=(64, 56, 52), justify='center'),
            T(f'<p><span class="screen-reader-text">{nome}: </span>{etichetta}</p>', style='micro', color=TESTO2, align='center',
              css='bv-logo-label'),
            w=(50, 50, 50), min_h=(176, 150, 140), justify='center', align='stretch', gap=(20, 16, 16), link=link,
            pad=(0, (16, 12, 10), 0, (16, 12, 10)), css='bv-logo', border_color=NERO, **b))
    css = (CSS_KICKER +
           f'.bv-logo:hover .bv-logo-label p,.bv-logo:focus-visible .bv-logo-label p{{color:{NERO};text-decoration:underline;'
           'text-underline-offset:4px}')
    css += ('@media (max-width:1024px){.bv-logo-label p{letter-spacing:1.2px}}'
            f'@media (min-width:768px) and (max-width:1024px){{.bv-logo{{width:25%!important;border-bottom:0!important;'
            f'border-right:1px solid {NERO}!important}}.bv-logo:last-child{{border-right:0!important}}}}')
    testa = C(
        T('<p>Per chi lavoriamo</p>', style='label', color=TESTO2, css='bv-kicker'),
        H('Molti dei nostri clienti<br>producono per<br>i marchi del lusso', 'h2', style='h2m', mt=32),
        T('<p>Calzaturifici, pelletterie e modellisti, ma anche calzolai e negozi di calzature. Al banco trovano gli stessi '
          'marchi che usano ogni giorno in produzione e in riparazione.</p>', style='lead', color=TESTO2, max_w=560, mt=24),
        RAW('', css=css), gap='0')
    # lo spazio in più va solo tra il testo e il link: il link chiude alla stessa altezza della griglia dei marchi
    sinistra = C(testa, link_freccia('Cosa trovi di ciascun marchio', '/marchi/', mt=32), w=(55, 100, 100), gap='0',
                 justify='between')
    destra = C(
        T('<p>I marchi al banco</p>', style='label', color=TESTO2, mb=20),
        C(*celle, dir='row', wrap=True, gap='0'),
        w=(42.5, 100, 100), gap='0', mt=(0, 56, 48), justify='between')
    return sezione(sinistra, destra, pad=((160, 120, 64), 'lato', (120, 88, 64), 'lato'), dir='row', dir_t='column', dir_m='column',
                   justify='between', align=('stretch', 'stretch', 'stretch'), gap='0', css='bv-who')


CSS_CHIUSURA = (
    '.bv-chiusura .bv-facade img{display:block;width:100%!important;height:auto!important;max-width:100%;'
    'aspect-ratio:2048/877;object-fit:cover;object-position:50% 50%}'
    '@media (max-width:767px){.bv-chiusura .bv-facade img{aspect-ratio:7/5;object-position:78% 50%}}'
)


def chiusura_banco():
    """S4: "Vieni al banco" grande appoggiato sul cielo della facciata, poi quattro colonne con filetto (Mastrotto, Ernest Wright)."""
    corpo = ('Codice o nome articolo:\nColore, misura o formato:\nQuantità:\nRitiro al banco o spedizione:\n')
    def colonna(etichetta, valore, nota, link=None, telefono=False):
        figli = [T(f'<p>{etichetta}</p>', style='label', color=TESTO2)]
        if telefono:
            figli.append(H(TEL, 'p', style='tel2', color=NERO, link=TEL_LINK, mt=12))
        else:
            figli.append(T(f'<p>{valore}</p>', style='body', color=NERO, link_color=NERO, link_hover=ROSSO, mt=12))
        figli.append(T(f'<p>{nota}</p>', style='testo15', color=TESTO2, mt=8))
        if link:
            figli.append(link_freccia(link[0], link[1], mt=16))
        return C(*figli, w=(23, 48, 100), border_top=1, border_color=NERO, pad=(20, 0, 0, 0), gap='0')
    indice = C(
        colonna('Indirizzo', f'{INDIRIZZO}, {ZONA_MIN}, 30030\u00a0Vigonovo\u00a0(VE)', 'Parcheggio clienti davanti al negozio.',
                ('Apri in Google Maps', MAPS)),
        colonna('Orari del banco', ORARI, f'{CHIUSURA}.'),
        colonna('Telefono', None, 'Per disponibilità, colori e misure.', telefono=True),
        colonna('Email e spedizioni', f'<a href="{mailto("Richiesta disponibilità", corpo)}">{EMAIL}</a>',
                'Verifichiamo varianti e disponibilità. Per gli ordini da lontano spediamo con corriere, alle condizioni '
                'di vendita per le aziende.', ('Condizioni di vendita (PDF)', CONDIZIONI_PDF)),
        dir='row', wrap=True, justify='between', gap='0', gap_r=(40, 40, 32), mt=(56, 56, 40))
    return sezione(
        H('Vieni al\u00a0banco', 'h2', style='chiusura', mb=(-58, -38, -26), z=2),
        I(img('sede-larga.jpg'), 'La sede Benvegnù in Via del Lavoro 48, zona industriale Tombelle, Vigonovo', css='bv-facade', z=1),
        indice, RAW('', css=CSS_CHIUSURA),
        bg=GRIGIO, pad=((120, 88, 64), 'lato', (120, 88, 64), 'lato'), gap='0', anchor='banco', css='bv-chiusura')


MARCHI = [
    ('vibram', 'Vibram', 'Suole, lastre, mezzesuole e tacchi', 'https://www.vibram.com/it/', (60, 52, 44)),
    ('gutermann', 'Gütermann', 'Filati per cucire Mara e Tera', 'https://www.guetermann.com/', (40, 36, 30)),
    ('girba', 'Girba', 'Tinture e prodotti per il finissaggio', 'https://www.girbasrl.it/it/', (76, 68, 56)),
    ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi per calzatura', 'https://www.zucchini.it/it/', (76, 68, 56)),
]


def striscia_marchi():
    celle = []
    for i, (slug, nome, famiglia, _, h_logo) in enumerate(MARCHI):
        celle.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=h_logo, fit='contain'), min_h=(120, 110, 96), justify='center'),
            T(f'<p>{nome}</p>', style='label', color=NERO, align='center', mt='xs'),
            T(f'<p>{famiglia}</p>', style='small', color=TESTO2, align='center'),
            w=(25, 50, 50), gap='xxs', pad=('m', 's', 'm', 's'),
            border_right=1 if i < 3 else 0, border_color=LINEA))
    return C(*celle, dir='row', wrap=True, gap='0', border_top=1, border_bottom=1, border_color=LINEA)


# ---------------------------------------------------------------------------------------------
# CATALOGO
# ---------------------------------------------------------------------------------------------
ORDINE_FAMIGLIE = [
    ('vibram-suole', '83137', ['2600 Liverpool, suola da città e tempo libero', '1012 Breithorn, suola da lavoro',
                               '0056C Winter City, suola da uomo']),
    ('vibram-lastre', '82268', ['7106 Crepe, lastra in gomma morbida', '7130 New Boulder, lastra per arrampicata',
                                '8281 Diflex, lastra per ortesi plantari']),
    ('vibram-mezzesuole-tacchi', '80751', ['2023 Wellness, mezza suola in gomma compatta', '1100T Montagna, tacco 20,5 mm',
                                           '0750P Nuvola, lastra bi-mescola per tacchi']),
    ('utensili', '1895', ['9978 Coltello C.Dick Original 270x20', '14932 Calibro digitale 200 mm', '2031 Martello con calamita']),
    ('filati-elastici', '15887', ['Filato poliestere ritorto Mara', 'Filato poliestere ritorto Tera',
                                  '1075 Filo Gialla Braid size 8']),
    ('modelleria-riparazione', '14563', ['9049 Alzo per forma art. 601/29', '1802 Bipiede in ghisa cm 62',
                                         '14563 Forma allargascarpe 2Way Dasco']),
    ('prodotti-chimici', None, ['G04000 Bordobrill (Girba), 1 litro', 'G42001 Lederpolish 04 (Girba), 1 litro',
                                'G61001 Tingileder (Girba), 25 litri']),
    ('esposizione-cura', '15752', ['15752 Tendiscarpa in legno di cedro', '7995 Calzante Longuette anatomico',
                                   '14933 Calze usa e getta, confezione da 200']),
    ('igiene-sicurezza', '9907', ['9907 Guanti Marigold Green Nitrile', '15947 Mascherina con valvola FFP2', '16200 Guanti antiacido']),
    ('imballaggio', '15531', ['2055 Nastro adesivo Comet', '15531 Etichette Made in Italy 28x8, 5000 pezzi',
                              '9519 Numeri autoadesivi oro, 2000 pezzi']),
]


def catalogo():
    # indice a salti: un link per widget in una riga che va a capo (niente stili in linea, che l'import può togliere)
    indice = C(*[T(f'<p><a href="#{slug}">{FAM[slug]["nome"]}</a></p>', style='nav', color=NERO, link_color=NERO,
                   link_hover=ROSSO) for slug, _, _ in ORDINE_FAMIGLIE],
               dir='row', wrap=True, gap=('m', 'm', 's'), gap_r=('xs', 'xs', 'xs'), mt='xs')
    apertura = sezione(
        C(H('Catalogo', 'h1'),
          T(f'<p>{TOTALE} articoli in 10 famiglie, dagli utensili alle suole Vibram. Per disponibilità, colori e misure chiedi al '
            'banco o telefona negli orari di apertura.</p>', style='lead', color=TESTO2, max_w=760), gap='m'),
        indice,
        gap='l', pad=('xl', 'lato', 'l', 'lato'), anchor='content')

    righe = []
    for i, (slug, foto, esempi) in enumerate(ORDINE_FAMIGLIE, 1):
        f = FAM[slug]
        # senza foto prodotto (i chimici Girba non ne hanno): il logo del marchio nella stessa cornice quadrata
        miniatura = (C(I(img(f'prodotto-{foto}.jpg'), f['nome']), border=1, border_color=LINEA, bg=BIANCO)
                     if foto else C(I(img('marchio-girba.png'), 'Logo Girba', height=(84, 80, 44), fit='contain'),
                                    min_h=(218, 211, 105), justify='center', border=1, border_color=LINEA, bg=BIANCO))
        righe.append(C(
            H(f'{i:02d}', 'p', style='num', color=ROSSO, fisso=True, w_px=(64, 56, None), hide=['mobile']),
            C(miniatura, w=(17, 22, 30), fisso=True),
            C(T(f'<p>{i:02d}</p>', style='label', color=ROSSO, hide=['desktop', 'tablet']),
              H(f['nome'], 'h3'),
              T(f'<p>{sottocategorie(slug)}</p>', style='body', color=TESTO2),
              T('<p>' + '<br>'.join(esempi) + '</p>', style='small', color=NERO),
              gap='s', grow=True, w=(40, 40, 62)),
            C(T(f'<p>{f["n"]} articoli</p>', style='label', color=NERO, align=('right', 'right', 'left')),
              T(f'<p><a href="{mailto("Disponibilità: " + f["nome"])}">Chiedi disponibilità&nbsp;&nbsp;→</a></p>',
                style='link', color=NERO, link_color=NERO, link_hover=ROSSO, align=('right', 'right', 'left')),
              gap='xs', w=(20, 22, 100), fisso=True),
            dir='row', wrap=(False, False, True), gap=('l', 'm', 's'), pad=('l', '0', 'l', '0'), border_top=1, border_color=LINEA,
            anchor=slug, align='start'))
    famiglie = sezione(*righe, C(LINEA_H(LINEA)), gap='0', pad=('xl', 'lato', 'sezione', 'lato'))

    non_online = sezione(
        C(H('Al banco c’è anche quello che non è online', 'h2'),
          T(f'<p>Il catalogo online non comprende tutte le famiglie che vendiamo. Chiedi al banco o chiama il {TEL}.</p>',
            style='body', color=TESTO2),
          C(B('Chiedi un articolo', mailto('Richiesta articolo non in catalogo'), variant='primario'), mt='xs'),
          w=(40, 100, 100), gap='m'),
        C(C(T('<ul><li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
              '<li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>', style='body'), w=(50, 50, 100)),
          C(T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per l’incollaggio Fratelli Zucchini</li>'
              '<li>Rinforzi per tomaia in tessuto</li><li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per tomaia</li></ul>',
              style='body'), w=(50, 50, 100)),
          dir='row', dir_m='column', gap='l', w=(54, 100, 100)),
        bg=BIANCO, pad=('0', 'lato', 'sezione', 'lato'), dir='row', dir_t='column', justify='between', gap='xl')
    return [('apertura', apertura), ('famiglie', famiglie), ('non-online', non_online), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# VIBRAM
# ---------------------------------------------------------------------------------------------
def vibram():
    apertura = hero_divisa(
        'Vibram a Vigonovo',
        f'Benvegnù è rivenditore autorizzato Vibram. Nel catalogo ci sono {N_VIBRAM} articoli: suole da città, montagna e lavoro, '
        'lastre compatte ed espanse, mezzesuole e tacchi. Servono a chi produce e a chi ripara.',
        [B('Chiedi disponibilità', mailto('Disponibilità Vibram', 'Modello:\nMisura:\nColore:\nQuantità:\n'), variant='bianco',
           full_m=True),
         B(f'Chiama {TEL}', TEL_LINK, variant='contorno-bianco', full_m=True)],
        'banco-suole.jpg', 'Suole e mezzesuole Vibram sul banco', livello='h1', stile='h1', min_h=520)

    def blocco(titolo, slug, intro, schede, bordo=True):
        return sezione(
            C(C(H(titolo, 'h2'), T(f'<p>{intro}</p>', style='body', color=TESTO2, max_w=620), gap='s', grow=True),
              T(f'<p>{FAM[slug]["n"]} articoli</p>', style='label', align=('right', 'right', 'left'), fisso=True),
              dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='m'),
            griglia_schede(schede), gap='l', anchor=slug,
            **({'border_top': 1, 'border_color': LINEA} if bordo else {}))

    w3 = W3
    suole = blocco('Suole', 'vibram-suole', sottocategorie('vibram-suole') + '.', [
        scheda_prodotto('80075', '2600 Liverpool', 'Gumlite', 'Suola da città e tempo libero, monoblocco, disegno a onde', w=w3),
        scheda_prodotto('85109', '0056C Winter City', 'Gomma monocolore', 'Suola da città e tempo libero da uomo', w=w3),
        scheda_prodotto('82768', '2603 Gumblock', 'Gumlite', 'Suola a tacco staccato, disegno Carrarmato', w=w3),
        scheda_prodotto('83137', '2609 Athena Gumlite', 'Gumlite', 'Suola per applicazioni ortopediche a dima extra large', w=w3),
        scheda_prodotto('85014', '4303 Betulla tranciata', 'Espanse', 'Suola da città e tempo libero, disegno Carrarmato', w=w3),
        scheda_prodotto('83169', 'V.0121P Fourà PU', 'Gomma PU', 'Suola in PU, nero e grigio, in più misure', w=w3),
    ], bordo=False)
    lastre = blocco('Lastre', 'vibram-lastre', sottocategorie('vibram-lastre') + '. Da tagliare a misura per suole, '
                                                 'riparazioni e costruzioni ortopediche.', [
        scheda_prodotto('82268', '7106 Crepe', 'Compatte', 'Lastra in gomma morbida', w=w3),
        scheda_prodotto('84952', '8281 Diflex', 'Espanse', 'Lastra per ortesi plantari', w=w3),
        scheda_prodotto('84413', '7130 New Boulder', 'Compatte', 'Lastra per arrampicata e bouldering, mescola extra morbida', w=w3),
    ])
    tacchi = blocco('Mezzesuole e tacchi', 'vibram-mezzesuole-tacchi', sottocategorie('vibram-mezzesuole-tacchi') + '.', [
        scheda_prodotto('83255', '2023 Wellness', 'Mezzesuole compatte', 'Mezza suola in gomma compatta', w=w3),
        scheda_prodotto('83263', '2025 Sebastian', 'Mezzesuole compatte', 'Mezza suola invernale in gomma compatta', w=w3),
        scheda_prodotto('80751', '1100T Montagna', 'Tacchi compatti', 'Tacco 20,5 mm da montagna e sportivo, mescola Vibram Mont', w=w3),
    ])
    chi = sezione(
        C(H('Per chi produce', 'h3'),
          T('<p>Calzaturifici e suolifici: scegli modello, mescola e misure, poi verifichiamo insieme formati e quantità '
            'disponibili.</p>', style='body', color=TESTO2), w=(48, 48, 100), gap='s', pad=('m', '0', '0', '0'),
          border_top=2, border_color=NERO),
        C(H('Per chi ripara', 'h3'),
          T('<p>Calzolai: mezzesuole, tacchi e lastre da tagliare per risuolare scarpe da città, da lavoro e da montagna.</p>',
            style='body', color=TESTO2), w=(48, 48, 100), gap='s', pad=('m', '0', '0', '0'), border_top=2,
          border_color=NERO),
        dir='row', dir_m='column', justify='between', gap='l', border_top=1, border_color=LINEA)
    return [('apertura', apertura), ('suole', suole), ('lastre', lastre), ('mezzesuole-tacchi', tacchi),
            ('per-chi', chi), ('banco', blocco_banco('Chiedi un modello Vibram'))]


# ---------------------------------------------------------------------------------------------
# MARCHI
# ---------------------------------------------------------------------------------------------
def marchi():
    apertura = intestazione('Marchi', 'I marchi che trovi al banco e cosa c’è di ciascuno. Nel catalogo compaiono anche '
                                      'utensili e materiali di altri produttori.', filetto=False)
    schede = [
        ('vibram', 'Vibram', f'Suole, mezzesuole, tacchi e lastre in gomma, per produzione e riparazione. È il marchio più '
                             f'presente nel nostro catalogo: {N_VIBRAM} articoli.', [('La pagina Vibram', '/vibram/')], (96, 84, 72)),
        ('gutermann', 'Gütermann', 'Filati industriali per cucire. Per pelle e calzatura teniamo i filati in poliestere ritorto '
                                   'Mara e Tera, in più colori.', [('Filati ed elastici', '/catalogo/#filati-elastici')], (60, 52, 44)),
        ('girba', 'Girba', 'Prodotti chimici per il finissaggio di calzatura e pelletteria: tinture e prodotti per tomaia e '
                           'bordi. Nel catalogo online: Bordobrill, Iris, Lederpolish, Nubio, Tingileder.',
         [('Prodotti chimici', '/catalogo/#prodotti-chimici')], (104, 92, 80)),
        ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi e prodotti per l’incollaggio in calzatura. Non sono ancora nel '
                                                   'catalogo online: chiedi al banco quali formati sono disponibili.',
         [('Chiedi gli adesivi', mailto('Adesivi Fratelli Zucchini'))], (104, 92, 80)),
    ]
    sito = {s: u for s, _, _, u, _ in MARCHI}
    righe = []
    for i, (slug, nome, testo, links, h_logo) in enumerate(schede, 1):
        righe.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=h_logo, fit='contain'), justify='center',
              min_h=(260, 220, 170), pad='l', bg=GRIGIO, w=(38, 40, 100)),
            C(H(f'{i:02d}', 'p', style='num', color=ROSSO), H(nome, 'h2'),
              T(f'<p>{testo}</p>', style='body', color=TESTO2, max_w=600),
              C(*[link_freccia(t, u) for t, u in links], link_freccia(f'Sito ufficiale {nome}', sito[slug]),
                gap='xs', mt='xs'),
              gap='s', w=(54, 54, 100)),
            dir='row', dir_m='column', justify='between', gap=('xl', 'l', 'm'), pad=('l', '0', 'l', '0'), border_top=1,
            border_color=LINEA, align='center'))
    elenco = sezione(*righe, C(LINEA_H(LINEA)), gap='0', pad=('xl', 'lato', 'sezione', 'lato'))
    altri = sezione(
        C(H('Nel catalogo trovi anche', 'h3'), w=(32, 100, 100)),
        C(T('<p>Olfa, Mozart, Mark, Lariz, Kai, Wiss, C.Dick, Norton, Pentel, Marvy, Mitsubishi, Stanley, Dremel, Einhell, '
            'Luxoro, 3M, Marigold, Sperian, Coats.</p>', style='lead', color=NERO),
          T('<p>Sono i marchi che compaiono nei nomi degli articoli del catalogo online. Per un marchio che non vedi, chiedi.</p>',
            style='small', color=TESTO2), w=(54, 100, 100), gap='s'),
        bg=BIANCO, pad=('0', 'lato', 'sezione', 'lato'), dir='row', dir_t='column', justify='between', gap='l')
    return [('apertura', apertura), ('elenco', elenco), ('altri-marchi', altri), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# AZIENDA
# ---------------------------------------------------------------------------------------------
def azienda():
    apertura = sezione(
        C(H('Dal 1980 a Vigonovo', 'h1'),
          T('<p>Benvegnù nasce nel 1980 a Vigonovo, nell’area calzaturiera della Riviera del Brenta. Vendiamo componenti e '
            'accessori per calzature e pelletterie, in particolare i materiali per la rifinitura del fondo e della tomaia, e '
            'tutta la piccola utensileria. Siamo specializzati in suole e lastre in gomma Vibram.</p>', style='lead',
            color=TESTO2, max_w=820), gap='m'),
        I(img('sede-larga.jpg'), 'La sede Benvegnù in Via del Lavoro 48, zona industriale Tombelle, Vigonovo',
          height=(560, 420, 240), pos='center right'),   # su telefono resta inquadrata l'insegna
        gap='xl', pad=('xl', 'lato', 'sezione', 'lato'), anchor='content')

    cosa = sezione(
        C(H('Cosa vendiamo', 'h2'),
          T(f'<p>Il catalogo online ha {TOTALE} articoli in 10 famiglie. Al banco trovi anche le famiglie che non sono '
            'online.</p>', style='body', color=TESTO2),
          C(B('Sfoglia il catalogo', '/catalogo/', variant='primario'), mt='xs'),
          w=(32, 100, 100), gap='m'),
        C(C(T('<ul><li>Suole e lastre in gomma Vibram</li><li>Filo in poliestere ed elastico per tomaia</li>'
              '<li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
              '<li>Piccola utensileria per la calzatura</li><li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>',
              style='body'), w=(50, 50, 100)),
          C(T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per la rifinitura della suola e della tomaia</li>'
              '<li>Prodotti per l’incollaggio Fratelli Zucchini</li><li>Rinforzi per tomaia in tessuto</li>'
              '<li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per la tomaia</li></ul>', style='body'), w=(50, 50, 100)),
          dir='row', dir_m='column', gap='l', w=(60, 100, 100)),
        dir='row', dir_t='column', justify='between', gap='xl', border_top=1, border_color=LINEA)

    tappe = [
        ('1980', 'Inizio dell’attività', 'A Vigonovo, nel distretto calzaturiero della Riviera del Brenta.'),
        ('1990', 'Nasce Benvegnù S.r.l.', 'Iscrizione alla Camera di Commercio di Padova il 24 ottobre 1990.'),
        ('2014', 'Il catalogo va online', f'Dal 16 aprile 2014 i prodotti sono sul sito. Oggi sono {TOTALE} articoli in 10 famiglie.'),
    ]
    righe = [C(H(a, 'p', style='cifra', color=NERO, fisso=True, w_px=(170, 150, None)), C(H(t, 'h3'), w=(30, 30, 100), fisso=True),
               T(f'<p>{d}</p>', style='body', color=TESTO2, grow=True),
               dir='row', dir_m='column', gap=('l', 'm', 'xs'), pad=('m', '0', 'm', '0'), border_top=1, border_color=LINEA,
               align=('baseline', 'baseline', 'start'))
             for a, t, d in tappe]
    storia = sezione(
        H('Le date', 'h2'),
        C(*righe, C(LINEA_H(LINEA)), gap='0'),
        gap='l', border_top=1, border_color=LINEA)

    distretto = sezione(
        C(I(img('magazzino-corsia.jpg'), 'Corsia del magazzino Benvegnù', height=(520, 420, 260)), w=(50, 100, 100)),
        C(H('Nel distretto della Riviera del Brenta', 'h2', color=BIANCO),
          T('<p>Vigonovo è uno dei comuni del distretto calzaturiero della Riviera del Brenta, con Stra, Fiesso d’Artico, Dolo e '
            'Fossò. Nel distretto lavorano oltre 500 imprese della filiera e si producono circa 20 milioni di paia di scarpe '
            'l’anno.</p><p>Per chi lavora qui, il banco è a pochi chilometri: si passa, si guarda il materiale, si ritira.</p>',
            style='body', color=SU_NERO2),
          T('<p>Fonti: Unioncamere, “Le calzature della Riviera del Brenta”; FashionUnited, 7 novembre 2024.</p>',
            style='small', color=SU_NERO2),
          w=(42, 100, 100), gap='m'),
        dir='row', dir_t='column', justify='between', gap='xl', align='center', bg=NERO)

    clienti = [
        ('Calzaturifici', 'Suole e lastre Vibram, filati, elastici, prodotti per il fondo e la tomaia.'),
        ('Pelletterie', 'Filati, utensili da taglio, punzoni, tinture per bordi, prodotti per il finissaggio.'),
        ('Calzolai', 'Mezzesuole, tacchi e lastre Vibram per la riparazione, colle, utensili.'),
        ('Stilisti e modellisti', 'Materiali per modelleria, alzi e allungaforme, compassi, strumenti di misura.'),
        ('Negozi di calzature', 'Calzanti, tendiscarpe, prodotti per la cura, calze monouso per la prova.'),
    ]
    per_chi = sezione(
        C(H('Per chi lavoriamo', 'h2'), w=(32, 100, 100)),
        C(*[riga_indice(f'{i:02d}', t, x) for i, (t, x) in enumerate(clienti, 1)], C(LINEA_H(LINEA)), w=(60, 100, 100),
          gap='0'),
        dir='row', dir_t='column', justify='between', gap='xl')

    condizioni = sezione(
        C(H('Condizioni di vendita', 'h3'),
          T('<p>Per le aziende con partita IVA valgono le condizioni generali di vendita: ordine minimo, pagamento e spedizione '
            'sono indicati nel documento.</p>', style='body', color=TESTO2), w=(60, 100, 100), gap='s'),
        C(link_freccia('Scarica il PDF', CONDIZIONI_PDF), w=(30, 100, 100), align=('end', 'start', 'start')),
        dir='row', dir_t='column', justify='between', gap='m', align=('center', 'start', 'start'),
        pad=('l', 'lato', 'l', 'lato'), border_top=1, border_color=LINEA, anchor='condizioni')
    return [('apertura', apertura), ('cosa-vendiamo', cosa), ('dal-1980', storia), ('distretto', distretto),
            ('per-chi', per_chi), ('condizioni', condizioni), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# NOVITÀ
# ---------------------------------------------------------------------------------------------
ARTICOLI_ESEMPIO = [
    ('Il nuovo sito di Benvegnù è online', '/novita/', 'Avviso'),
    (f'Il catalogo online: {TOTALE} articoli in 10 famiglie', '/catalogo/', 'Catalogo'),
]

# Il widget gratuito "Articoli recenti" di WordPress non ha controlli di stile in Elementor: CSS solo per .bvg-news
STILE_NEWS = (
    '.bvg-news h5,.bvg-news .widget-title,.bvg-news .wp-block-heading{display:none}'
    '.bvg-news ul{list-style:none;margin:0;padding:0}'
    f'.bvg-news li{{border-top:1px solid {LINEA};padding:24px 0;margin:0}}'
    f'.bvg-news li:last-child{{border-bottom:1px solid {LINEA}}}'
    f".bvg-news li a{{font-family:'{CONDENSED}',Arial,sans-serif;font-weight:600;font-size:28px;line-height:1.1;letter-spacing:.3px;"
    f'text-transform:uppercase;color:{NERO};text-decoration:none}}'
    f'.bvg-news li a:hover,.bvg-news li a:focus{{color:{ROSSO}}}'
    f".bvg-news .post-date{{display:block;font-family:'{BARLOW}',Arial,sans-serif;font-weight:500;font-size:12px;letter-spacing:2px;"
    f'text-transform:uppercase;color:{TESTO2};margin-top:8px}}'
    '@media (max-width:767px){.bvg-news li a{font-size:22px}}'
)


def novita():
    apertura = intestazione('Novità e avvisi', 'Chiusure, nuovi arrivi e novità dai marchi. Ogni avviso ha una data.')
    avvisi = sezione(
        C(C(T('<p>Orari del banco</p>', style='label', color=TESTO2),
            H(ORARI, 'p', style='h3'),
            T(f'<p>{CHIUSURA}. Le chiusure per ferie e festività le pubblichiamo qui, con le date di inizio e di fine.</p>',
              style='body', color=TESTO2), gap='s', w=(64, 100, 100)),
          C(B(f'Chiama {TEL}', TEL_LINK, variant='primario'), w=(32, 100, 100), align=('end', 'start', 'start')),
          dir='row', dir_t='column', justify='between', gap='l', pad='l', bg=GRIGIO, align=('center', 'start', 'start')),
        pad=('l', 'lato', '0', 'lato'))
    elenco = sezione(
        C(H('Ultime novità', 'h2'), w=(32, 100, 100)),
        C(ARTICOLI(ARTICOLI_ESEMPIO, numero=8), RAW('', css=STILE_NEWS, solo_elementor=True), w=(60, 100, 100),
          css='bvg-news'),
        dir='row', dir_t='column', justify='between', gap='xl')
    return [('apertura', apertura), ('avvisi', avvisi), ('elenco', elenco), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# CONTATTI
# ---------------------------------------------------------------------------------------------
STILE_CF7 = (
    f".bvg-modulo .wpcf7 label,.bvg-modulo .bvg-scelta{{display:block;margin:0 0 22px;font:500 12px/16px '{BARLOW}',Arial,sans-serif;"
    f'letter-spacing:2px;text-transform:uppercase;color:{TESTO2}}}'
    '.bvg-modulo .wpcf7 p{margin:0}.bvg-modulo .wpcf7 br{display:none}'
    '.bvg-modulo .wpcf7-form-control-wrap{display:block}'
    '.bvg-modulo input[type=text],.bvg-modulo input[type=email],.bvg-modulo input[type=tel],.bvg-modulo select,'
    f'.bvg-modulo textarea{{display:block;width:100%;margin-top:8px;background:{BIANCO};border:1px solid #BDBDBD;'
    f"border-radius:0;box-shadow:none;padding:14px 16px;font:400 16px/24px '{BARLOW}',Arial,sans-serif;letter-spacing:0;"
    f'text-transform:none;color:{NERO}}}'
    '.bvg-modulo textarea{min-height:140px;resize:vertical}'
    f'.bvg-modulo input:focus,.bvg-modulo textarea:focus{{border-color:{NERO};outline:2px solid {ROSSO};outline-offset:2px}}'
    f".bvg-modulo input[type=submit]{{background:{NERO};color:{BIANCO};border:1px solid {NERO};border-radius:0;"
    f"padding:18px 34px;font:600 13px/16px '{BARLOW}',Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;cursor:pointer;"
    'transition:background-color .15s,color .15s}'
    f'.bvg-modulo input[type=submit]:hover{{background:transparent;color:{NERO}}}'
    f'.bvg-modulo input[type=checkbox],.bvg-modulo input[type=radio]{{accent-color:{NERO};flex:0 0 20px;width:20px;height:20px;margin:1px 0 0}}'
    '.bvg-modulo .wpcf7-list-item{display:block;margin:0}'
    '.bvg-modulo .wpcf7-list-item label{display:flex;align-items:flex-start;gap:10px;margin:0;min-height:44px;padding:11px 0;line-height:22px}'
    f'.bvg-modulo .wpcf7-list-item-label,.bvg-modulo .wpcf7-acceptance{{text-transform:none;letter-spacing:0;font-size:15px;color:{NERO}}}'
    f'.bvg-modulo .wpcf7-not-valid-tip{{color:{ROSSO};font-size:14px;margin-top:6px;text-transform:none;letter-spacing:0}}'
    f'.bvg-modulo .wpcf7 form .wpcf7-response-output{{margin:24px 0 0;padding:14px 16px;border:1px solid {NERO};font-size:15px}}'
    '@media (max-width:767px){.bvg-modulo input[type=submit]{width:100%}}'
)


def contatti():
    def dato(etichetta, html):
        return C(T(f'<p>{etichetta}</p>', style='label', color=TESTO2, w_px=(130, 130, None)),
                 T(f'<p>{html}</p>', style='body', color=NERO, link_color=NERO, link_hover=ROSSO, grow=True),
                 dir='row', dir_m='column', gap=('m', 'm', 'xxs'), pad=('s', '0', 's', '0'), border_top=1, border_color=LINEA,
                 align=('baseline', 'baseline', 'start'))
    apertura = intestazione('Contatti', f'Il banco è a Vigonovo, in {INDIRIZZO}, {ZONA_MIN}. Rispondiamo al telefono negli '
                                        'orari di apertura.', filetto=False)
    corpo = ('Codice o nome articolo:\nColore, misura o formato:\nQuantità:\nRitiro al banco o spedizione:\n'
             'Ragione sociale e partita IVA:\nTelefono:\n')
    alternativa = (f'<p style="margin:0 0 24px">Scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>: il pulsante qui sotto apre '
                   'una email con i campi già pronti da compilare.</p>'
                   f'<p style="margin:0"><a href="{mailto("Richiesta disponibilità", corpo)}" style="display:inline-block;'
                   f'background:{NERO};color:{BIANCO};border:1px solid {NERO};padding:18px 34px;font:600 13px/16px \'{BARLOW}\','
                   'Arial,sans-serif;letter-spacing:2px;text-transform:uppercase;text-decoration:none">Scrivi la richiesta</a></p>')
    dati = sezione(
        C(dato('Indirizzo', f'{INDIRIZZO}<br>{CITTA}<br>{ZONA}'),
          dato('Orari', f'{ORARI}<br>{CHIUSURA}'),
          dato('Telefono', f'<a href="{TEL_LINK}">{TEL}</a>'),
          dato('Fax', FAX),
          dato('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
          dato('PEC', PEC),
          dato('Parcheggio', 'Per i clienti, davanti al negozio'),
          C(LINEA_H(LINEA)),
          C(MAPPA(f'Benvegnù, {INDIRIZZO}, {CITTA}', height=(650, 340, 300), zoom=15, grigia=True), mt='l'),
          w=(46, 100, 100), gap='0'),
        C(H('Richiesta di disponibilità', 'h2'),
          T('<p>Indica il codice o il nome dell’articolo: ti rispondiamo negli orari del banco.</p>', style='body', color=TESTO2),
          C(SHORTCODE(CF7, alternativa_html=alternativa, colore=TESTO2), RAW('', css=STILE_CF7, solo_elementor=True), mt='s',
            css='bvg-modulo'),
          w=(46, 100, 100), gap='s', pad='l', bg=GRIGIO, anchor='modulo'),
        dir='row', dir_t='column', justify='between', align='start', gap='xl', pad=('xl', 'lato', 'sezione', 'lato'))
    societari = sezione(
        C(H('Dati societari', 'h3'), w=(32, 100, 100)),
        C(T(f'<p>Benvegnù S.r.l.<br>P.IVA e codice fiscale {PIVA}<br>REA {REA}<br>Sede legale: {SEDE_LEGALE}<br>PEC {PEC}</p>',
            style='body', color=TESTO2),
          link_freccia('Condizioni generali di vendita (PDF)', CONDIZIONI_PDF), w=(48.67, 100, 100), gap='s'),
        dir='row', dir_t='column', justify='between', gap='l', pad=('l', 'lato', 'l', 'lato'), border_top=1, border_color=LINEA)
    # le fasi del lavoro (pattern "processo in fasi" del brief): quattro colonne con filetto, numeri piccoli in grigio
    fasi = [
        ('Fase 1', 'Dicci cosa ti serve', f'Al banco, al telefono {TEL} o per email. Se l’articolo ha un codice, indicalo: '
                                         'è nella sua scheda del catalogo.'),
        ('Fase 2', 'Verifichiamo le varianti', 'Colore, misura, formato, quantità. Per Vibram partiamo da modello '
                                               'e misura, per i filati da articolo e colore.'),
        ('Fase 3', 'Ritiri al banco o spediamo', 'Ritiro a Vigonovo con parcheggio davanti al negozio. Per gli ordini da lontano '
                                                 'spediamo con corriere, alle condizioni di vendita per le aziende.'),
        ('Fase 4', 'Riordino col codice', 'Annota codice e colore, o misura, degli articoli che usi: per riordinare basta '
                                          'dettarceli al telefono o per email.'),
    ]
    come = sezione(
        H('Come si lavora con noi', 'h2', max_w=(760, 760, 600)),
        C(*[C(T(f'<p>{n}</p>', style='label', color=TESTO2), H(t, 'h3', mt=12), T(f'<p>{x}</p>', style='body', color=TESTO2, mt=8),
              w=(23, 48, 100), border_top=1, border_color=NERO, pad=(20, 0, 0, 0), gap='0') for n, t, x in fasi],
          dir='row', wrap=True, justify='between', gap='0', gap_r=(40, 40, 32)),
        gap='l', pad=('sezione', 'lato', 'sezione', 'lato'), border_top=1, border_color=LINEA)
    return [('apertura', apertura), ('dati-modulo', dati), ('come-si-lavora', come), ('dati-societari', societari)]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Benvegnù | Forniture per calzaturifici, pelletterie e calzolai a Vigonovo',
     'descrizione': 'Suole e lastre Vibram, filati, utensili e prodotti per fondo e tomaia. Al banco di Vigonovo, Riviera del Brenta, dal 1980.'},
    {'slug': '02-azienda', 'titolo': 'Azienda', 'sezioni': azienda,
     'titolo_seo': 'Azienda | Benvegnù, Vigonovo dal 1980',
     'descrizione': 'Benvegnù nasce nel 1980 a Vigonovo, nel distretto calzaturiero della Riviera del Brenta.'},
    {'slug': '03-catalogo', 'titolo': 'Catalogo', 'sezioni': catalogo,
     'titolo_seo': f'Catalogo | {TOTALE} articoli per calzatura e pelletteria | Benvegnù',
     'descrizione': 'Utensili, filati ed elastici, modelleria, prodotti chimici, esposizione e cura, suole e lastre Vibram.'},
    {'slug': '04-vibram', 'titolo': 'Vibram', 'sezioni': vibram,
     'titolo_seo': 'Vibram | Suole, lastre, mezzesuole e tacchi | Benvegnù Vigonovo',
     'descrizione': f'Rivenditore autorizzato Vibram: {N_VIBRAM} articoli tra suole, lastre, mezzesuole e tacchi.'},
    {'slug': '05-marchi', 'titolo': 'Marchi', 'sezioni': marchi,
     'titolo_seo': 'Marchi | Vibram, Gütermann, Girba, Fratelli Zucchini | Benvegnù',
     'descrizione': 'I marchi che trovi al banco di Benvegnù e cosa c’è di ciascuno.'},
    {'slug': '06-novita', 'titolo': 'Novità', 'sezioni': novita,
     'titolo_seo': 'Novità e avvisi | Benvegnù', 'descrizione': 'Chiusure, nuovi arrivi e novità dai marchi.'},
    {'slug': '07-contatti', 'titolo': 'Contatti', 'sezioni': contatti,
     'titolo_seo': 'Contatti | Benvegnù, Via del Lavoro 48, Vigonovo',
     'descrizione': f'{INDIRIZZO}, {CITTA}. {ORARI}. Tel. {TEL}. Richiesta di disponibilità online.'.replace(WJ, '')
                    .replace('\u00a0', ' ')},
]
