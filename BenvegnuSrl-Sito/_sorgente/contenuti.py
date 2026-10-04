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
    return T(f'<p><a href="{url}">{testo}&nbsp;&nbsp;→</a></p>', style='link', color=colore, link_color=colore,
             link_hover=hover, **p)


def intestazione(titolo, lead, max_w=760):
    return sezione(
        C(H(titolo, 'h1'), T(f'<p>{lead}</p>', style='lead', color=TESTO2, max_w=max_w), gap='m'),
        pad=('xl', 'lato', 'l', 'lato'), border_bottom=1, border_color=LINEA)


def hero_divisa(titolo, lead, pulsanti, foto, alt, foto_mobile=None, livello='h1', stile='display'):
    """Hero divisa: pannello nero con il titolo a sinistra, foto a tutta altezza a destra (Mastrotto, Santoni)."""
    testo = C(H(titolo, livello, style=stile, color=BIANCO),
              T(f'<p>{lead}</p>', style='lead', color=SU_NERO2, max_w=520),
              C(*pulsanti, dir='row', dir_m='column', gap='s', mt='xs'),
              w=(50, 100, 100), gap='m', justify='center', pad=('xl', 'xl', 'xl', 'hero_lato'), min_h=(680, 0, 0),
              bg=NERO)
    # foto come sfondo del contenitore: riempie sempre l'altezza del pannello nero, qualunque sia la lunghezza del testo
    immagine = C(w=(50, 100, 100), min_h=(680, 520, 300), img=img(foto), alt=alt, hide=['mobile'] if foto_mobile else None)
    figli = [testo, immagine]
    if foto_mobile:
        figli.append(C(w=(100, 100, 100), min_h=(300, 300, 280), img=img(foto_mobile), alt=alt, hide=['desktop', 'tablet']))
    return C(*figli, dir='row', dir_t='column', boxed=False, pad='0', gap='0', bg=NERO, tag='section')


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
)


def header():
    barra = C(
        T(f'<p>Banco aperto {ORARI_BREVE.lower()}</p>', style='small', color=SU_NERO2, hide=['mobile']),
        T(f'<p>{ORARI_BREVE}</p>', style='small', color=SU_NERO2, hide=['desktop', 'tablet']),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="mailto:{EMAIL}">{EMAIL}</a></p>', style='small',
          color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2, align='right', hide=['mobile']),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='small', color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2,
          align='right', hide=['desktop', 'tablet']),
        dir='row', justify='between', align='center', gap='s', pad=(9, 'lato'), bg=NERO, boxed=True)
    marchio = C(I(img('logo-benvegnu-nero.png'), 'Benvegnù S.r.l.', link='/', w_img=(176, 156, 136), fisso=True),
                dir='row', align='center', w=(30, 50, 55))
    azioni = C(
        T(f'<p><a href="{TEL_LINK}">Chiama</a></p>', style='link', color=NERO, link_color=NERO, link_hover=ROSSO,
          hide=['desktop'], fisso=True),
        MENU(VOCI_MENU, colore=NERO, accento=ROSSO, fondo_menu=BIANCO, linea=LINEA, stile='nav', stile_mobile='nav_m',
             spazio=32, pad_v=8, distanza=12, align_menu='right', fisso=True, larg=(None, 40, 40)),
        B('Chiedi disponibilità', '/contatti/#modulo', variant='contorno', hide=['tablet', 'mobile'], fisso=True),
        dir='row', align='center', justify='end', gap=('l', 's', 's'), w=(70, 50, 45))
    testata = C(marchio, azioni, dir='row', justify='between', align='center', gap='m', min_h=(84, 72, 64),
                pad=(10, 'lato'), bg=BIANCO, border_bottom=1, border_color=LINEA, boxed=True)
    return C(barra, testata, RAW('', css=CSS_BASE, solo_elementor=True), pad='0', boxed=False, tag='header', bg=BIANCO,
             css='bvg-testata')


def footer():
    def colonna(titolo, html):
        return C(T(f'<p>{titolo}</p>', style='label', color=SU_NERO2),
                 T(html, style='dati', color=BIANCO, link_color=BIANCO, link_hover=SU_NERO2, sottolinea=False), gap='s',
                 w=(22, 46, 100))
    pagine = ''.join(f'<a href="{u}">{t}</a><br>' for t, u in VOCI_MENU)
    righe = C(
        C(I(img('logo-benvegnu-bianco.png'), 'Benvegnù S.r.l.', link='/', w_img=(176, 160, 150)),
          T('<p>Componenti, accessori e utensili per calzatura e pelletteria. Vigonovo, dal 1980.</p>', style='dati',
            color=SU_NERO2, max_w=300), gap='m', w=(28, 46, 100)),
        colonna('Il banco', f'<p>{INDIRIZZO}<br>{CITTA}<br>{ZONA}</p><p>{ORARI_BREVE}<br>{CHIUSURA}</p>'),
        colonna('Contatti', f'<p>Tel. <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
                            f'PEC {PEC}</p>'),
        colonna('Pagine', f'<p>{pagine}<a href="{CONDIZIONI_PDF}">Condizioni di vendita (PDF)</a></p>'),
        dir='row', dir_m='column', wrap=(False, True, False), justify='between', gap=('m', 'l', 'l'))
    legale = C(
        T(f'<p>© 2026 Benvegnù S.r.l. · P.IVA {PIVA} · REA {REA} · Sede legale {SEDE_LEGALE}</p>', style='small', color=SU_NERO2),
        T(f'<p><a href="/privacy/">Privacy</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="/cookie/">Cookie</a>&nbsp;&nbsp;·&nbsp;&nbsp;'
          f'<a href="{FACEBOOK}">Facebook</a></p>', style='small', color=SU_NERO2, link_color=SU_NERO2, link_hover=BIANCO, sottolinea=False,
          align=('right', 'right', 'left')),
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

    righe_v = [riga_indice(f'{i:02d}', t, x, destra=f'{n} articoli', colore=BIANCO, colore_testo=SU_NERO2,
                           colore_num=SU_NERO2, linea=LINEA_SCURA)
               for i, (t, x, n) in enumerate([
                   ('Suole', sottocategorie('vibram-suole', False), FAM['vibram-suole']['n']),
                   ('Lastre', sottocategorie('vibram-lastre', False), FAM['vibram-lastre']['n']),
                   ('Mezzesuole e tacchi', sottocategorie('vibram-mezzesuole-tacchi', False), FAM['vibram-mezzesuole-tacchi']['n'])], 1)]
    vibram = sezione(
        C(H('Vibram al banco', 'h2', color=BIANCO),
          T(f'<p>Siamo rivenditori autorizzati Vibram. In catalogo ci sono {N_VIBRAM} articoli Vibram, per chi produce '
            'e per chi ripara.</p>', style='lead', color=SU_NERO2, max_w=540),
          C(*righe_v, gap='0', mt='xs'),
          C(B('La pagina Vibram', '/vibram/', variant='bianco'), mt='s'),
          w=(52, 100, 100), gap='m'),
        C(I(img('espositore-vibram.jpg'), 'Espositore Vibram nel negozio Benvegnù', height=(600, 520, 320)), w=(42, 100, 100)),
        bg=NERO, dir='row', dir_t='column', justify='between', gap='xl', align='center')

    prodotti = sezione(
        C(H('Dal catalogo', 'h2'), link_freccia('Tutte le famiglie', '/catalogo/'),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s'),
        griglia_schede([
            scheda_prodotto('80075', '2600 Liverpool', 'Suole Vibram', 'Suola da città e tempo libero, disegno a onde', '/vibram/#vibram-suole'),
            scheda_prodotto('82268', '7106 Crepe', 'Lastre Vibram', 'Lastra in gomma morbida', '/vibram/#vibram-lastre'),
            scheda_prodotto('1895', 'Forbici da lavoro Lariz', 'Utensili', 'Forbici con lame curve', '/catalogo/#utensili'),
            scheda_prodotto('15887', 'Filato Mara', 'Filati ed elastici', 'Poliestere ritorto Gütermann', '/catalogo/#filati-elastici'),
        ]),
        bg=GRIGIO, gap='l')

    passi = [
        ('01', 'Dicci cosa ti serve', f'Al banco, al telefono {TEL} o per email. Se hai il codice dell’articolo facciamo prima: '
                                      'lo trovi nel catalogo.'),
        ('02', 'Verifichiamo disponibilità e varianti', 'Colore, misura, formato, quantità. Per Vibram partiamo da modello e '
                                                        'misura, per i filati da articolo e colore.'),
        ('03', 'Ritiri al banco o spediamo', f'Ritiri in {INDIRIZZO} a Vigonovo, con parcheggio davanti al negozio. Per gli ordini '
                                             'da lontano spediamo con corriere, alle condizioni di vendita per le aziende.'),
        ('04', 'Per il riordino basta il codice', 'Tieni codice e colore dell’articolo: il riordino si fa con una telefonata '
                                                  'o una email.'),
    ]
    come = sezione(
        C(H('Come si lavora con noi', 'h2', max_w=(400, 600, 600)),
          T('<p>Che tu passi al banco o ordini da lontano, i passaggi sono questi.</p>', style='body', color=TESTO2, max_w=360),
          w=(36, 100, 100), gap='m'),
        C(*[riga_indice(n, t, x) for n, t, x in passi], C(LINEA_H(LINEA)), w=(58, 100, 100), gap='0'),
        dir='row', dir_t='column', justify='between', gap='xl')

    marchi_ = sezione(
        C(H('I marchi', 'h2'), link_freccia('Cosa trovi di ciascuno', '/marchi/'),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s'),
        striscia_marchi(),
        gap='l', border_top=1, border_color=LINEA)

    return [('apertura', apertura), ('catalogo', catalogo), ('vibram', vibram), ('dal-catalogo', prodotti),
            ('come-si-lavora', come), ('marchi', marchi_), ('banco', blocco_banco())]


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
        gap='l', pad=('xl', 'lato', 'l', 'lato'), border_bottom=1, border_color=LINEA)

    righe = []
    for i, (slug, foto, esempi) in enumerate(ORDINE_FAMIGLIE, 1):
        f = FAM[slug]
        miniatura = (C(I(img(f'prodotto-{foto}.jpg'), f['nome']), border=1, border_color=LINEA, bg=BIANCO)
                     if foto else C(T('<p>Prodotti Girba<br>per il finissaggio</p>', style='label', color=TESTO2, align='center'),
                                    min_h=(180, 160, 140), justify='center', bg=GRIGIO))
        righe.append(C(
            H(f'{i:02d}', 'p', style='num', color=ROSSO, fisso=True, w_px=(64, 56, None)),
            C(miniatura, w=(17, 22, 50), fisso=True),
            C(H(f['nome'], 'h3'),
              T(f'<p>{sottocategorie(slug)}</p>', style='body', color=TESTO2),
              T('<p>' + '<br>'.join(esempi) + '</p>', style='small', color=NERO),
              gap='s', grow=True),
            C(T(f'<p>{f["n"]} articoli</p>', style='label', color=NERO, align=('right', 'right', 'left')),
              T(f'<p><a href="{mailto("Disponibilità: " + f["nome"])}">Chiedi disponibilità&nbsp;&nbsp;→</a></p>',
                style='link', color=NERO, link_color=NERO, link_hover=ROSSO, align=('right', 'right', 'left')),
              gap='xs', w=(20, 22, 100), fisso=True),
            dir='row', dir_m='column', gap=('l', 'm', 's'), pad=('l', '0', 'l', '0'), border_top=1, border_color=LINEA,
            anchor=slug, align='start'))
    famiglie = sezione(*righe, C(LINEA_H(LINEA)), gap='0', pad=('m', 'lato', 'sezione', 'lato'))

    non_online = sezione(
        C(H('Al banco c’è anche quello che non è online', 'h2'),
          T(f'<p>Il catalogo online non comprende tutte le famiglie che vendiamo. Chiedi al banco o chiama il {TEL}.</p>',
            style='body', color=TESTO2),
          C(B('Chiedi un articolo', mailto('Richiesta articolo non in catalogo'), variant='primario'), mt='xs'),
          w=(40, 100, 100), gap='m'),
        C(T('<ul><li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
            '<li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>', style='body'),
          T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per l’incollaggio Fratelli Zucchini</li>'
            '<li>Rinforzi per tomaia in tessuto</li><li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per tomaia</li></ul>',
            style='body'),
          dir='row', dir_m='column', gap='l', w=(54, 100, 100)),
        bg=GRIGIO, dir='row', dir_t='column', justify='between', gap='xl')
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
        'banco-suole.jpg', 'Suole e mezzesuole Vibram sul banco', livello='h1', stile='h1')

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
                                      'utensili e materiali di altri produttori.')
    schede = [
        ('vibram', 'Vibram', f'Suole, mezzesuole, tacchi e lastre in gomma, per produzione e riparazione. È il marchio più '
                             f'presente nel nostro catalogo: {N_VIBRAM} articoli.', [('La pagina Vibram', '/vibram/')], (96, 84, 72)),
        ('gutermann', 'Gütermann', 'Filati industriali per cucire. Per pelle e calzatura teniamo i filati in poliestere ritorto '
                                   'Mara e Tera, in più colori.', [('Filati ed elastici', '/catalogo/#filati-elastici')], (52, 48, 40)),
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
    elenco = sezione(*righe, C(LINEA_H(LINEA)), gap='0', pad=('m', 'lato', 'sezione', 'lato'))
    altri = sezione(
        C(H('Negli articoli del catalogo trovi anche', 'h3'), w=(32, 100, 100)),
        C(T('<p>Olfa, Mozart, Mark, Lariz, Kai, Wiss, C.Dick, Norton, Pentel, Marvy, Mitsubishi, Stanley, Dremel, Einhell, '
            'Luxoro, 3M, Marigold, Sperian, Coats.</p>', style='lead', color=NERO),
          T('<p>Sono i marchi che compaiono nei nomi degli articoli del catalogo online. Per un marchio che non vedi, chiedi.</p>',
            style='small', color=TESTO2), w=(60, 100, 100), gap='s'),
        bg=GRIGIO, dir='row', dir_t='column', justify='between', gap='l')
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
          height=(560, 420, 240)),
        gap='xl', pad=('xl', 'lato', 'sezione', 'lato'))

    cosa = sezione(
        C(H('Cosa vendiamo', 'h2'),
          T(f'<p>Il catalogo online ha {TOTALE} articoli in 10 famiglie. Al banco trovi anche le famiglie che non sono '
            'online.</p>', style='body', color=TESTO2),
          C(B('Sfoglia il catalogo', '/catalogo/', variant='primario'), mt='xs'),
          w=(32, 100, 100), gap='m'),
        C(T('<ul><li>Suole e lastre in gomma Vibram</li><li>Filo in poliestere ed elastico per tomaia</li>'
            '<li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
            '<li>Piccola utensileria per la calzatura</li><li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>',
            style='body'),
          T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per la rifinitura della suola e della tomaia</li>'
            '<li>Prodotti per l’incollaggio Fratelli Zucchini</li><li>Rinforzi per tomaia in tessuto</li>'
            '<li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per la tomaia</li></ul>', style='body'),
          dir='row', dir_m='column', gap='l', w=(60, 100, 100)),
        dir='row', dir_t='column', justify='between', gap='xl', border_top=1, border_color=LINEA)

    tappe = [
        ('1980', 'Inizio dell’attività', 'A Vigonovo, nel distretto calzaturiero della Riviera del Brenta.'),
        ('1990', 'Nasce Benvegnù S.r.l.', 'Iscrizione alla Camera di Commercio di Padova il 24 ottobre 1990.'),
        ('2014', 'Il catalogo va online', f'Dal 16 aprile 2014 i prodotti sono sul sito. Oggi sono {TOTALE} articoli in 10 famiglie.'),
        ('2026', 'Il nuovo sito', 'Il catalogo si consulta anche da telefono, con codici e famiglie.'),
    ]
    righe = [C(H(a, 'p', style='cifra', color=NERO, fisso=True, w_px=(170, 150, None)), C(H(t, 'h3'), w=(30, 30, 100)),
               T(f'<p>{d}</p>', style='body', color=TESTO2, grow=True),
               dir='row', dir_m='column', gap=('l', 'm', 'xs'), pad=('m', '0', 'm', '0'), border_top=1, border_color=LINEA,
               align=('center', 'center', 'start'))
             for a, t, d in tappe]
    storia = sezione(
        C(H('Le date', 'h2'), T('<p>Quelle che possiamo documentare.</p>', style='body', color=TESTO2),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s'),
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
    f'.bvg-modulo input[type=checkbox],.bvg-modulo input[type=radio]{{accent-color:{NERO};width:18px;height:18px;margin:0 8px 0 0;vertical-align:-3px}}'
    '.bvg-modulo .wpcf7-list-item{display:block;margin:10px 0 0}'
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
                                        'orari di apertura.')
    corpo = ('Codice o nome articolo:\nColore, misura o formato:\nQuantità:\nRitiro al banco o spedizione:\n'
             'Ragione sociale e partita IVA:\nTelefono:\n')
    alternativa = (f'<p style="margin:0 0 16px">Scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a> indicando codice o nome '
                   'dell’articolo, colore, misura o formato, quantità, ritiro al banco o spedizione.</p>'
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
          C(MAPPA(f'Benvegnù, {INDIRIZZO}, {CITTA}', height=(360, 340, 300), zoom=15, grigia=True), mt='l'),
          w=(46, 100, 100), gap='0'),
        C(H('Richiesta di disponibilità', 'h2'),
          T('<p>Indica il codice o il nome dell’articolo: ti rispondiamo negli orari del banco.</p>', style='body', color=TESTO2),
          C(SHORTCODE(CF7, alternativa_html=alternativa), RAW('', css=STILE_CF7, solo_elementor=True), mt='s', css='bvg-modulo'),
          w=(46, 100, 100), gap='s', pad='l', bg=GRIGIO, anchor='modulo'),
        dir='row', dir_t='column', justify='between', align='start', gap='xl', pad=('l', 'lato', 'sezione', 'lato'))
    societari = sezione(
        C(H('Dati societari', 'h3'), w=(32, 100, 100)),
        C(T(f'<p>Benvegnù S.r.l.<br>P.IVA e codice fiscale {PIVA}<br>REA {REA}<br>Sede legale: {SEDE_LEGALE}<br>PEC {PEC}</p>',
            style='body', color=TESTO2),
          link_freccia('Condizioni generali di vendita (PDF)', CONDIZIONI_PDF), w=(60, 100, 100), gap='s'),
        dir='row', dir_t='column', justify='between', gap='l', pad=('l', 'lato', 'l', 'lato'), border_top=1, border_color=LINEA)
    return [('apertura', apertura), ('dati-modulo', dati), ('dati-societari', societari)]


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
