# -*- coding: utf-8 -*-
"""
Contenuti del sito Benvegnù S.r.l., direzione "Atelier": la sala campionario di una modelleria della Riviera del Brenta.
Carta avorio, inchiostro grafite (dal logo), il rosso storico di Benvegnù solo come impuntura e segno, Bodoni Moda diritto
per titoli e numeri, Schibsted Grotesk per testo e dati, foto come tavole numerate in passe-partout.
Fonti dei testi: sito attuale ripulito, catalogo online (874 articoli, crawl del 4 ottobre 2026), Registro Imprese, scheda Google.
"""
import json
import os
from urllib.parse import quote

import motore as m
from motore import C, H, T, B, I, MAPPA, LINEA_H, ARTICOLI, RAW, MENU, SHORTCODE

QUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------------------------
# Tema "Atelier"
# ---------------------------------------------------------------------------------------------
CARTA = '#F5F0E8'          # fondo di tutte le pagine
AVORIO = '#FBF8F3'         # superfici: passe-partout, tessere, pannello modulo
PERGAMENA = '#ECE5D9'      # una sola banda per pagina
INCHIOSTRO = '#262320'     # testo, titoli, pulsante primario, filetti forti (dal grafite del logo)
GRAFITE = '#5E574F'        # testo secondario da 14 px in su (6,3:1 su carta)
FILETTO = '#D8CFC2'        # filetti decorativi
FILETTO_FORTE = '#8A8176'  # bordi dei campi del modulo (3,4:1)
CUOIO = '#9F2E29'          # il rosso storico di Benvegnù: impuntura, hover, voce attiva, focus. Mai campiture
CUOIO_SCURO = '#7E2621'
NOTTE = '#262320'          # footer
SABBIA = '#BDB3A6'         # testo secondario solo su notte (7,6:1)
FILETTO_NOTTE = '#4A443E'
TRASPARENTE = 'rgba(0,0,0,0)'

BODONI = 'Bodoni Moda'
GROTESK = 'Schibsted Grotesk'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


TEMA = {
    'nome': 'Atelier',
    'fondo': CARTA, 'superficie': AVORIO, 'inchiostro': INCHIOSTRO, 'testo2': GRAFITE, 'accento': CUOIO,
    'filetto': FILETTO, 'filetto_scuro': FILETTO_NOTTE, 'su_scuro2': SABBIA,
    'scuro': NOTTE, 'su_scuro': CARTA, 'su_accento': CARTA,
    'font_titoli': BODONI, 'font_testo': GROTESK, 'larghezza': 1200,
    # stessa API che usa Elementor (css v1): Bodoni Moda arriva con la grandezza ottica da testo, più robusta
    'google_fonts': 'https://fonts.googleapis.com/css?family=Bodoni+Moda:400,500%7CSchibsted+Grotesk:400,500,600&display=swap',
    'stili': {
        'display': _st(BODONI, '400', (64, 52, 34), 1.07, -0.6),
        'h1':      _st(BODONI, '400', (52, 44, 32), 1.12, -0.3),
        'h2':      _st(BODONI, '400', (40, 34, 28), 1.2),
        'h3':      _st(BODONI, '500', (26, 24, 21), 1.24),
        'h3s':     _st(BODONI, '500', (21, 20, 19), 1.25),
        'num':     _st(BODONI, '400', (40, 36, 30), 1.1),
        'cifra':   _st(BODONI, '400', (52, 44, 40), 1.08),
        'anno':    _st(BODONI, '400', (56, 48, 40), 1.07),
        'tel':     _st(BODONI, '400', (44, 40, 32), 1.1),
        'frase':   _st(BODONI, '400', (30, 28, 24), 1.27),
        'nav_m':   _st(BODONI, '400', (24, 24, 24), 1.33),
        'label':   _st(GROTESK, '500', (12, 12, 12), 1.33, 1.68, True),
        'lead':    _st(GROTESK, '400', (20, 19, 18), 1.6),
        'body':    _st(GROTESK, '400', (17, 17, 16), 1.65),
        'small':   _st(GROTESK, '400', (14, 14, 14), 1.57, 0.14),
        'dati':    _st(GROTESK, '400', (15, 15, 15), 1.6),
        'link':    _st(GROTESK, '500', (15, 15, 15), 1.6),
        'nav':     _st(GROTESK, '500', (13, 13, 13), 1.23, 1.56, True),
        'btn':     _st(GROTESK, '600', (13, 13, 13), 1.23, 1.56, True),
    },
    'spazi': {
        'sezione': (128, 96, 64), 'aps': (96, 64, 48), 'apg': (64, 48, 32), 'lato': (40, 32, 20),
        'xl': (64, 48, 32), 'l': (48, 40, 32), 'm': (32, 24, 24), 's': (24, 20, 16), 'xs': (12, 12, 12),
        'xxs': (8, 8, 8), 'col': (32, 24, 16), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): in hover il pulsante cambia colore, mai trasparenza
    'bottoni': {
        'primario': (CARTA, INCHIOSTRO, INCHIOSTRO, CARTA, CUOIO, CUOIO),
        'contorno': (INCHIOSTRO, TRASPARENTE, INCHIOSTRO, CARTA, INCHIOSTRO, INCHIOSTRO),
        'su-notte': (INCHIOSTRO, CARTA, CARTA, CARTA, TRASPARENTE, CARTA),
    },
    'bottone': {'raggio': 0, 'pad': (16, 28, 16, 28), 'bordo': 1, 'stile': 'btn'},
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
TEL = '049 983 0202'
TEL_LINK = 'tel:+390499830202'
FAX = '049 983 1177'
EMAIL = 'commerciale@benvegnusrl.it'
PEC = 'info@pec.benvegnusrl.it'
INDIRIZZO = 'Via del Lavoro 48'
CITTA = '30030 Vigonovo (VE)'
ZONA = 'zona industriale Tombelle'
ORARI = 'dal lunedì al venerdì, 8:30-12:30 e 14:30-18:30'
ORARI_BREVE = 'lun-ven 8:30-12:30 e 14:30-18:30'
CHIUSURA = 'sabato e domenica chiuso'
PIVA = '02326850282'
REA = 'PD-222933'
SEDE_LEGALE = 'Piazzetta Primo Modin 12, 35129 Padova'
MAPS = ('https://www.google.com/maps/search/?api=1&query=Benvegn%C3%B9%20Via%20del%20Lavoro%2048%20Vigonovo'
        '&query_place_id=ChIJCYLIGbDFfkcRl5iSbyMPyb4')
CONDIZIONI_PDF = 'https://www.benvegnusrl.it/condizioni-di-vendita-Benvegnusrl.pdf'
FACEBOOK = 'https://www.facebook.com/benvegnusrl'
CF7 = '[contact-form-7 title="Richiesta disponibilità"]'


def cap(s):
    return s[0].upper() + s[1:]


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
        voci.append(f'{nome} {s["n"]}' if con_numeri else nome)
    return cap(', '.join(voci))


# ---------------------------------------------------------------------------------------------
# Componenti della direzione Atelier
# ---------------------------------------------------------------------------------------------
def sezione(*children, bg=CARTA, pad=('sezione', 'lato'), **p):
    return C(*children, bg=bg, pad=pad, tag='section', **p)


def impuntura(**p):
    """La cucitura: divisore tratteggiato cuoio di 56 px. Massimo due per pagina."""
    return LINEA_H(CUOIO, 2, 'dashed', larghezza=(56, 56, 48), **p)


def doppio(**p):
    return LINEA_H(INCHIOSTRO, 3, 'double', **p)


def riga_inchiostro(**p):
    return LINEA_H(INCHIOSTRO, 1, **p)


def link_testo(testo, url, colore=INCHIOSTRO, **p):
    return T(f'<p><a href="{url}">{testo}</a></p>', style='link', color=colore, link_color=colore, link_hover=CUOIO, **p)


def tav(numero):
    return (f'<span style="font-weight:500;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:{INCHIOSTRO};'
            f'margin-right:14px">Tav. {numero:02d}</span>')


def tavola(foto, alt, numero, didascalia, w=None, hide=None, **p):
    """Foto montata come una stampa: passe-partout avorio con filetto, didascalia numerata sotto."""
    extra = {'w': w} if w else {}
    return C(
        C(I(img(foto), alt), pad=(16, 12, 10), bg=AVORIO, border=1, border_color=FILETTO),
        T(f'<p>{tav(numero)}{didascalia}</p>', style='small', color=GRAFITE),
        gap='xs', hide=hide, **extra, **p)


def testata(titolo, link=None, url=None):
    figli = [H(titolo, 'h2', grow=True)]
    if link:
        figli.append(link_testo(f'{link}&nbsp;&nbsp;→', url, fisso=True))
    return C(*figli, dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s',
             pad=('0', '0', 20, '0'), border_bottom=1, border_color=INCHIOSTRO)


def registro_cifre(voci, colonne=4):
    """Registro a doppio filetto con cifre in Bodoni: apre il doppio filetto, chiude la riga d'inchiostro."""
    w = {4: (23, 48, 47.5), 3: (31, 31, 100)}[colonne]
    celle = [C(H(c, 'p', style='cifra'), T(f'<p>{d}</p>', style='small', color=GRAFITE), gap='xxs', w=w,
               pad=('s', '0', 's', '0')) for c, d in voci]
    return C(doppio(), C(*celle, dir='row', wrap=True, justify='between', gap='0'), riga_inchiostro(), gap='0')


def riga_registro(numero, titolo, testo, quantita=None, link=None, ancora=None):
    """Riga di indice: numero Bodoni, titolo e descrizione, quantità a destra. In hover si schiarisce (avorio)."""
    centro = C(H(titolo, 'h3'), T(f'<p>{testo}</p>', style='small', color=GRAFITE), gap='xxs', grow=True)
    figli = [H(numero, 'p', style='num', fisso=True, w_px=(72, 64, None)), centro]
    if quantita:
        figli.append(T(f'<p>{quantita}</p>', style='dati', color=INCHIOSTRO, align=('right', 'right', 'left'), fisso=True))
    extra = dict(bg_hover=AVORIO, hover_titolo=CUOIO, css='bvg-riga') if link else {}
    return C(*figli, dir='row', dir_m='column', gap=('s', 's', 'xxs'), pad=(28, 12, 28, '0'), border_bottom=1,
             border_color=FILETTO, align=('baseline', 'baseline', 'start'), link=link, anchor=ancora, **extra)


def riga_dato(etichetta, valore, colore_etichetta=GRAFITE, colore=INCHIOSTRO, linea=FILETTO):
    return C(T(f'<p>{etichetta}</p>', style='label', color=colore_etichetta, w_px=(140, 140, None)),
             T(f'<p>{valore}</p>', style='body', color=colore, link_color=colore, link_hover=CUOIO, grow=True),
             dir='row', dir_m='column', gap=('s', 's', 'xxs'), pad=('s', '0', 's', '0'), border_bottom=1, border_color=linea,
             align=('baseline', 'baseline', 'start'))


def registro_dati(righe):
    return C(doppio(), *[riga_dato(e, v) for e, v in righe], gap='0')


def tessera_prodotto(pid, titolo, testo, w=(31, 48, 47)):
    return C(C(I(img(f'prodotto-{pid}.jpg'), titolo), bg=AVORIO, border=1, border_color=FILETTO),
             H(titolo, 'h3', style='h3s', mt='xs'), T(f'<p>{testo}</p>', style='small', color=GRAFITE),
             w=w, gap='xxs')


def griglia_tessere(tessere):
    return C(*tessere, dir='row', wrap=True, justify='start', gap='col', gap_r='l')


def apertura_interna(titolo, lead, destra=None, w_testo=(56.9, 100, 100), allinea=('end', 'start', 'start')):
    testo = C(H(titolo, 'h1'), impuntura(mt='m'), T(f'<p>{lead}</p>', style='lead', color=INCHIOSTRO, max_w=640, mt='s'),
              w=w_testo, gap='0')
    figli = [testo] + ([destra] if destra else [])
    return sezione(*figli, dir='row', dir_t='column', justify='between', align=allinea, gap='xl',
                   pad=('aps', 'lato', 'apg', 'lato'))


def blocco_banco(pulsante=None):
    """Il banco di Via del Lavoro 48: registro della visita e tavola della corsia. Su tutte le pagine tranne Contatti."""
    b1 = pulsante or B('Apri in Google Maps', MAPS, variant='primario')
    return sezione(
        C(H('Il banco di Via del Lavoro 48', 'h2'),
          registro_dati([
              ('Indirizzo', f'{INDIRIZZO}, {ZONA}, {CITTA}'),
              ('Orari', f'{cap(ORARI)}. {cap(CHIUSURA)}.'),
              ('Telefono', f'<a href="{TEL_LINK}">{TEL}</a>'),
              ('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
              ('Parcheggio', 'Posti per i clienti davanti al negozio'),
          ]),
          C(b1, link_testo(f'Chiama {TEL}', TEL_LINK), dir='row', dir_m='column', gap='m', align=('center', 'center', 'start')),
          w=(56.9, 100, 100), gap='m'),
        tavola('corsia-4x5.jpg', 'Corsia del magazzino Benvegnù', 9, 'La corsia del magazzino, dietro al banco.',
               w=(32, 50, 100)),
        dir='row', dir_t='column', justify='between', gap='xl', anchor='banco', border_top=1, border_color=FILETTO)


# ---------------------------------------------------------------------------------------------
# Header e footer (template separati, tipo "section"; con Ultimate Addons diventano header e footer di tutto il sito)
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Catalogo', '/catalogo/'), ('Vibram', '/vibram/'), ('Marchi', '/marchi/'), ('Azienda', '/azienda/'),
             ('Novità', '/novita/'), ('Contatti', '/contatti/')]

# Piccolo CSS di base, caricato una volta dall'header: niente corsivi, focus visibile, titolo della riga in cuoio in hover.
CSS_BASE = (
    'em,i,cite{font-style:normal}'
    f'a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{{outline:2px solid {CUOIO};outline-offset:3px}}'
    f'.bvg-riga:hover .elementor-heading-title{{color:{CUOIO}}}'
    '.elementor-heading-title{font-variant-numeric:lining-nums tabular-nums}'
)


def header():
    servizio = C(
        T(f'<p>Banco aperto {ORARI_BREVE}</p>', style='small', color=GRAFITE),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="{MAPS}">{INDIRIZZO}, Vigonovo</a></p>',
          style='small', color=INCHIOSTRO, link_color=INCHIOSTRO, link_hover=CUOIO, align='right'),
        dir='row', justify='between', align='center', gap='s', pad=(8, 'lato'), bg=CARTA, border_bottom=1,
        border_color=FILETTO, hide=['mobile'], boxed=True)
    marchio = C(
        I(img('logo-benvegnu.png'), 'Benvegnù S.r.l.', link='/', w_img=(168, 148, 128), fisso=True),
        C(T('<p>Vigonovo<br>dal 1980</p>', style='label', color=GRAFITE), pad=('0', '0', '0', 20), border_left=1,
          border_color=FILETTO, hide=['tablet', 'mobile'], fisso=True),
        dir='row', align='center', gap='m', w=(34, 50, 60))
    azioni = C(
        link_testo('Chiama', TEL_LINK, hide=['desktop'], fisso=True),
        MENU(VOCI_MENU, colore=INCHIOSTRO, accento=CUOIO, fondo_menu=CARTA, linea=FILETTO, stile='nav', stile_mobile='nav_m',
             spazio=30, pad_v=8, distanza=22, align_menu='right', fisso=True),
        B('Chiedi disponibilità', '/contatti/#modulo', variant='contorno', hide=['tablet', 'mobile'], fisso=True),
        RAW('', css=CSS_BASE, solo_elementor=True),
        dir='row', align='center', justify='end', gap=('m', 's', 's'), w=(66, 50, 40))
    testata_ = C(marchio, azioni, dir='row', justify='between', align='center', gap='m', min_h=(88, 72, 64),
                 pad=(12, 'lato'), bg=CARTA, border_bottom=1, border_color=FILETTO, boxed=True)
    return C(servizio, testata_, pad='0', boxed=False, tag='header', bg=CARTA)


def footer():
    def colonna(titolo, html):
        return C(T(f'<p>{titolo}</p>', style='label', color=SABBIA),
                 T(html, style='dati', color=CARTA, link_color=CARTA, link_hover=SABBIA), gap='xs', w=(23, 48, 100))
    pagine = ''.join(f'<a href="{u}">{t}</a><br>' for t, u in VOCI_MENU)
    apertura = C(
        I(img('logo-benvegnu-avorio.png'), 'Benvegnù S.r.l.', link='/', w_img=(148, 148, 128)),
        H('Componenti, accessori e utensili per calzatura e pelletteria. Vigonovo, dal 1980.', 'p', style='frase', color=CARTA,
          max_w=640),
        gap='m', pad=('0', '0', 'xl', '0'))
    colonne = C(
        colonna('Il banco', f'<p>{INDIRIZZO}<br>{CITTA}<br>{cap(ZONA)}</p><p>{cap(ORARI_BREVE)}<br>{cap(CHIUSURA)}</p>'),
        colonna('Contatti', f'<p>Tel. <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>PEC {PEC}</p>'),
        colonna('Pagine', f'<p>{pagine}</p>'),
        colonna('Documenti', f'<p><a href="{CONDIZIONI_PDF}">Condizioni di vendita (PDF)</a><br><a href="/privacy/">Privacy</a><br>'
                             f'<a href="/cookie/">Cookie</a><br><a href="{FACEBOOK}">Facebook</a></p>'),
        dir='row', dir_m='column', wrap=(False, True, False), justify='between', gap=('0', 'm', 'm'),
        pad=('m', '0', '0', '0'), border_top=1, border_color=FILETTO_NOTTE)
    legale = C(T(f'<p>© 2026 Benvegnù S.r.l. · P.IVA {PIVA} · REA {REA} · Sede legale {SEDE_LEGALE}</p>', style='small',
                 color=SABBIA),
               pad=('s', '0', '0', '0'), border_top=1, border_color=FILETTO_NOTTE, mt='xl')
    return C(apertura, colonne, legale, gap='0', pad=((96, 64, 48), 'lato', (40, 32, 24), 'lato'), bg=NOTTE, tag='footer')


# ---------------------------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------------------------
def home():
    n_tomaia = FAM['filati-elastici']['n'] + FAM['modelleria-riparazione']['n']
    n_cura = sum(FAM[k]['n'] for k in ('prodotti-chimici', 'esposizione-cura', 'igiene-sicurezza', 'imballaggio'))
    apertura = sezione(
        C(C(H('Componenti e accessori per la calzatura, dal 1980.', 'h1', style='display'), impuntura(mt='m'),
            w=(65.3, 100, 100), gap='0'),
          C(T('<p>Suole e lastre Vibram, filati, adesivi, prodotti di finitura e utensili per calzaturifici, pelletterie, '
              'modellisti e calzolai. Al banco di Vigonovo, nella Riviera del Brenta.</p>', style='lead', color=INCHIOSTRO),
            C(B('Sfoglia il catalogo', '/catalogo/', variant='primario'), link_testo('Vieni al banco', '#banco'),
              dir='row', wrap=True, gap='m', align='center'),
            w=(32, 75, 100), gap='m'),
          dir='row', dir_t='column', justify='between', align=('end', 'start', 'start'), gap='l'),
        tavola('sede-21x9.jpg', 'La sede Benvegnù in Via del Lavoro 48 a Vigonovo', 1,
               'La sede di Via del Lavoro 48, zona industriale di Tombelle, Vigonovo.', hide=['mobile'], mt='xl'),
        tavola('sede-4x3.jpg', 'La sede Benvegnù in Via del Lavoro 48 a Vigonovo', 1,
               'La sede di Via del Lavoro 48, zona industriale di Tombelle, Vigonovo.', hide=['desktop', 'tablet'], mt='xl'),
        C(registro_cifre([('1980', 'Inizio dell’attività a Vigonovo'), (str(TOTALE), 'Articoli nel catalogo online'),
                          (str(N_VIBRAM), 'Articoli Vibram tra suole, lastre e tacchi'), ('10', 'Famiglie di prodotto')]),
          mt='xl'),
        gap='0', pad=('aps', 'lato', 'sezione', 'lato'))

    indice = sezione(
        tavola('rotoli-4x5.jpg', 'Rotoli di rinforzi e materiali in magazzino', 2,
               'Rotoli di rinforzi e materiali per tomaia in magazzino.', w=(32, 50, 100)),
        C(testata('Il campionario in dieci famiglie', 'Tutte le famiglie', '/catalogo/'),
          riga_registro('01', 'Vibram', 'Suole, lastre, mezzesuole e tacchi', f'{N_VIBRAM} articoli', link='/vibram/'),
          riga_registro('02', 'Utensili', 'Forbici, coltelli, lesine, punzoni, mole, strumenti di misura, torchi',
                        f'{FAM["utensili"]["n"]} articoli', link='/catalogo/#utensili'),
          riga_registro('03', 'Tomaia e modelleria', 'Filati, elastici, allungaforme, alzi, materiali per modelleria e riparazione',
                        f'{n_tomaia} articoli', link='/catalogo/#filati-elastici'),
          riga_registro('04', 'Finitura, cura e imballo', 'Prodotti Girba, cura della scarpa, esposizione, guanti, nastri ed etichette',
                        f'{n_cura} articoli', link='/catalogo/#prodotti-chimici'),
          w=(56.9, 100, 100), gap='0'),
        dir='row', dir_t='column', justify='between', gap='xl', pad=('0', 'lato', 'sezione', 'lato'))

    vibram = sezione(
        C(H('Vibram al banco', 'h2'), impuntura(mt='s'),
          T('<p>Suole in gomma, Gumlite e PU, lastre compatte ed espanse, mezzesuole e tacchi. Per chi produce e per chi '
            'ripara.</p>', style='lead', color=INCHIOSTRO, mt='s'),
          C(registro_cifre([(str(FAM['vibram-suole']['n']), 'Suole'), (str(FAM['vibram-lastre']['n']), 'Lastre'),
                            (str(FAM['vibram-mezzesuole-tacchi']['n']), 'Mezzesuole e tacchi')], colonne=3), mt='m'),
          C(B('La pagina Vibram', '/vibram/', variant='primario'), mt='m'),
          w=(40.4, 100, 100), gap='0'),
        tavola('banco-3x2.jpg', 'Suole e mezzesuole Vibram sul banco del negozio', 3,
               'Suole e mezzesuole Vibram sul banco del negozio.', w=(48.6, 100, 100)),
        bg=PERGAMENA, dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='xl')

    marchi_ = sezione(testata('Quattro marchi, tenuti a magazzino', 'La pagina marchi', '/marchi/'),
                      griglia_marchi(), gap='l')

    passi = [
        ('01', 'Dicci cosa ti serve', f'Al banco, al telefono {TEL} o per email. Con il codice dell’articolo la richiesta è più '
                                      'rapida: lo trovi nel catalogo.'),
        ('02', 'Verifichiamo disponibilità e varianti', 'Colore, misura, formato e quantità. Per Vibram partiamo da modello e '
                                                        'misura, per i filati da articolo e colore.'),
        ('03', 'Ritiri al banco o spediamo', f'Si ritira in {INDIRIZZO} a Vigonovo, con parcheggio davanti al negozio. Per gli '
                                             'ordini da lontano spediamo con corriere, alle condizioni di vendita per le aziende.'),
        ('04', 'Per il riordino basta il codice', 'Codice e colore dell’articolo bastano per riordinare con una telefonata o '
                                                  'una email.'),
    ]
    come = sezione(
        C(H('Come si lavora con noi', 'h2'),
          T('<p>Che si passi al banco o si ordini da lontano, i passaggi sono questi.</p>', style='body', color=GRAFITE),
          w=(32, 100, 100), gap='s'),
        C(doppio(), *[riga_registro(n, t, x) for n, t, x in passi], w=(56.9, 100, 100), gap='0'),
        dir='row', dir_t='column', justify='between', gap='xl', pad=('0', 'lato', 'sezione', 'lato'))

    return [('apertura', apertura), ('campionario', indice), ('vibram', vibram), ('marchi', marchi_),
            ('come-si-lavora', come), ('banco', blocco_banco())]


MARCHI = [
    ('vibram', 'Vibram', 'Suole, lastre, mezzesuole e tacchi', 'https://www.vibram.com/it/', (64, 56, 44)),
    ('gutermann', 'A&amp;E Gütermann', 'Filati per cucire Mara e Tera', 'https://www.guetermann.com/', (44, 40, 32)),
    ('girba', 'Girba', 'Tinture, creme e prodotti di finitura', 'https://www.girbasrl.it/it/', (80, 72, 56)),
    ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi e primer per calzatura', 'https://www.zucchini.it/it/', (80, 72, 56)),
]


def griglia_marchi():
    tessere = []
    for slug, nome, famiglia, _, alt_logo in MARCHI:
        tessere.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=alt_logo, fit='contain'), min_h=(184, 150, 112),
              justify='center', pad=('m', 'm', 'm', 'm'), bg=AVORIO, border=1, border_color=FILETTO),
            T(f'<p>{nome}</p>', style='label', color=INCHIOSTRO, mt='s'),
            T(f'<p>{famiglia}</p>', style='small', color=GRAFITE),
            w=(22.75, 48, 47), gap='xxs'))
    return C(*tessere, dir='row', wrap=True, justify='start', gap='col', gap_r='l')


# ---------------------------------------------------------------------------------------------
# AZIENDA
# ---------------------------------------------------------------------------------------------
def azienda():
    apertura = apertura_interna(
        'Dal 1980 a Vigonovo',
        'Benvegnù vende dal 1980 componenti, accessori e materiali di finitura per calzatura e pelletteria, la piccola '
        'utensileria e le suole e lastre in gomma Vibram. Al nostro banco si riforniscono calzaturifici, pelletterie, '
        'modellisti e calzolai.')
    sede = sezione(tavola('sede-3x2.jpg', 'La sede Benvegnù in Via del Lavoro 48, Vigonovo', 1,
                          'La sede di Via del Lavoro 48, zona industriale di Tombelle.', w=(66.6, 100, 100)),
                   align=('end', 'start', 'start'), pad=('0', 'lato', 'sezione', 'lato'))

    clienti = [
        ('Calzaturifici', 'Suole e lastre Vibram, filati, elastici, adesivi e prodotti per il fondo e la tomaia.'),
        ('Pelletterie', 'Filati, utensili da taglio, punzoni, tinture per bordi e prodotti di finitura.'),
        ('Modellisti e designer', 'Materiali per modelleria, alzi e allungaforme, compassi, strumenti di misura.'),
        ('Calzolai', 'Mezzesuole, tacchi e lastre Vibram per la riparazione, colle e utensili da banco.'),
    ]
    chi = sezione(
        testata('Lavoriamo per chi fa le scarpe e per chi le ripara'),
        C(*[C(H(t, 'h3'), T(f'<p>{x}</p>', style='body', color=GRAFITE), gap='xs', w=(48, 48, 100),
              pad=('s', '0', 's', '0'), border_top=1, border_color=INCHIOSTRO) for t, x in clienti],
          dir='row', wrap=True, justify='between', gap='col', gap_r='m'),
        gap='l', pad=('0', 'lato', 'sezione', 'lato'))

    voci = ['Suole e lastre in gomma Vibram', 'Filo in poliestere ed elastico per tomaia', 'Lacci in poliestere e cuoio',
            'Cerniere in nylon e metallo', 'Tallonette coprichiodi', 'Piccola utensileria per la calzatura',
            'Nastri abrasivi e tamponi SIA', 'Pennelli a mano e spazzole', 'Chiodi e semenze in ferro e ottone',
            'Prodotti per la rifinitura della suola e della tomaia', 'Adesivi Fratelli Zucchini', 'Rinforzi per tomaia in tessuto',
            'Occhielli, agraffi e rivetti', 'Tessuti sintetici per la tomaia']
    meta = (len(voci) + 1) // 2

    def colonna_voci(lista):
        return C(*[C(T(f'<p>{v}</p>', style='body'), pad=(14, '0', 14, '0'), border_bottom=1, border_color=FILETTO)
                   for v in lista], w=(48, 48, 100), gap='0')
    cosa = sezione(
        C(H('Cosa vendiamo', 'h2'),
          T(f'<p>Il catalogo online ha {TOTALE} articoli in 10 famiglie. Al banco trovi anche le famiglie che non sono online.</p>',
            style='body', color=GRAFITE),
          C(B('Sfoglia il catalogo', '/catalogo/', variant='contorno'), mt='xs'), w=(32, 100, 100), gap='s'),
        C(colonna_voci(voci[:meta]), colonna_voci(voci[meta:]), dir='row', dir_m='column', justify='between', gap='0',
          w=(56.9, 100, 100), border_top=3, border_color=INCHIOSTRO),
        dir='row', dir_t='column', justify='between', gap='xl', pad=('0', 'lato', 'sezione', 'lato'))

    tappe = [
        ('1980', 'Inizio dell’attività', 'A Vigonovo, nel distretto calzaturiero della Riviera del Brenta.'),
        ('1990', 'Nasce Benvegnù S.r.l.', 'Iscrizione alla Camera di Commercio di Padova, 24 ottobre 1990.'),
        ('2014', 'Il catalogo online', f'La sezione prodotti va online il 16 aprile 2014. Oggi: {TOTALE} articoli in 10 famiglie.'),
        ('2026', 'Il nuovo sito', 'Catalogo, marchi e banco consultabili anche da telefono.'),
    ]
    righe = [C(H(a, 'p', style='anno', fisso=True, w_px=(160, 140, None)), C(H(t, 'h3'), w=(30, 30, 100)),
               T(f'<p>{d}</p>', style='body', color=GRAFITE, grow=True),
               dir='row', dir_m='column', gap=('m', 's', 'xxs'), pad=('m', '0', 'm', '0'), border_bottom=1, border_color=FILETTO,
               align=('baseline', 'baseline', 'start'))
             for a, t, d in tappe]
    storia = sezione(
        testata('Dal 1980'),
        C(*righe, riga_inchiostro(), gap='0'),
        T('<p>Le date che possiamo documentare: l’anno di inizio dichiarato dall’azienda, il Registro Imprese, il sito.</p>',
          style='small', color=GRAFITE, mt='xs'),
        gap='0', pad=('0', 'lato', 'sezione', 'lato'))

    distretto = sezione(
        C(H('Nel distretto della Riviera del Brenta', 'h2'), impuntura(mt='s'),
          T('<p>Siamo a Vigonovo, uno dei comuni del distretto calzaturiero della Riviera del Brenta con Stra, Fiesso d’Artico, '
            'Dolo e Fossò. Qui lavorano oltre 500 imprese della filiera e si producono circa 20 milioni di paia di scarpe '
            'l’anno, molte per le case del lusso.</p><p>Per chi lavora nel distretto il banco è a pochi chilometri: si passa, '
            'si guarda il materiale, si ritira.</p>', style='body', color=INCHIOSTRO, mt='s'),
          T('<p>Fonti: Unioncamere, “Le calzature della Riviera del Brenta”; FashionUnited, 7 novembre 2024.</p>',
            style='small', color=GRAFITE, mt='s'),
          w=(48.6, 100, 100), gap='0'),
        tavola('rotoli-4x5.jpg', 'Rotoli di materiali nel magazzino Benvegnù', 2, 'Materiali per tomaia in rotolo.',
               w=(32, 50, 100)),
        bg=PERGAMENA, dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='xl')

    condizioni = sezione(
        C(H('Condizioni di vendita', 'h3'),
          T('<p>Per le aziende con partita IVA valgono le condizioni generali di vendita: ordine minimo, pagamento e '
            'spedizione sono indicati nel documento.</p>', style='body', color=GRAFITE), w=(56.9, 100, 100), gap='xs'),
        C(B('Scarica il PDF', CONDIZIONI_PDF, variant='contorno'), w=(32, 100, 100), align=('end', 'start', 'start')),
        dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='m',
        pad=('l', 'lato', 'l', 'lato'), border_top=1, border_color=FILETTO, anchor='condizioni')
    return [('apertura', apertura), ('sede', sede), ('per-chi', chi), ('cosa-vendiamo', cosa), ('dal-1980', storia),
            ('distretto', distretto), ('condizioni', condizioni), ('banco', blocco_banco())]


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
    apertura = apertura_interna(
        'Catalogo',
        f'{TOTALE} articoli in 10 famiglie, dagli utensili alle suole Vibram. Per disponibilità, colori e misure chiedi al banco '
        'o telefona negli orari di apertura.',
        destra=C(H(str(TOTALE), 'p', style='cifra'), T('<p>articoli nel catalogo online</p>', style='small', color=GRAFITE),
                 w=(32, 100, 100), gap='xxs', pad=('s', '0', 's', '0'), border_top=3, border_color=INCHIOSTRO))
    gruppi = ORDINE_FAMIGLIE[:5], ORDINE_FAMIGLIE[5:]
    indice_ancore = sezione(
        C(T('<p>Indice</p>', style='label', color=GRAFITE), w=(32, 100, 100)),
        C(*[T('<p>' + ''.join(f'<a href="#{s}">{FAM[s]["nome"]}</a><br>' for s, _, _ in grp) + '</p>', style='link',
              color=INCHIOSTRO, link_color=INCHIOSTRO, link_hover=CUOIO, w=(48, 48, 100)) for grp in gruppi],
          dir='row', dir_m='column', justify='between', gap='s', w=(56.9, 100, 100)),
        dir='row', dir_t='column', justify='between', gap='s', pad=('0', 'lato', 'xl', 'lato'))

    righe = []
    for i, (slug, foto, esempi) in enumerate(ORDINE_FAMIGLIE, 1):
        f = FAM[slug]
        tessera = (C(I(img(f'prodotto-{foto}.jpg'), f['nome']), bg=AVORIO, border=1, border_color=FILETTO)
                   if foto else C(T('<p>Prodotti Girba per la finitura</p>', style='label', color=GRAFITE, align='center'),
                                  min_h=(160, 140, 120), justify='center', bg=AVORIO, border=1, border_color=FILETTO, pad='s'))
        righe.append(C(
            H(f'{i:02d}', 'p', style='num', fisso=True, w_px=(72, 64, None)),
            C(H(f['nome'], 'h3'),
              T(f'<p>{sottocategorie(slug)}</p>', style='small', color=GRAFITE),
              T('<p>' + '<br>'.join(esempi) + '</p>', style='dati', color=INCHIOSTRO, mt='xxs'),
              gap='xxs', grow=True),
            C(tessera,
              T(f'<p>{f["n"]} articoli</p>', style='dati', color=INCHIOSTRO, mt='xxs'),
              link_testo('Chiedi disponibilità', mailto('Disponibilità: ' + f['nome'])),
              w=(19, 22, 60), gap='xxs'),
            dir='row', dir_m='column', gap=('m', 's', 's'), pad=('m', '0', 'm', '0'), border_bottom=1, border_color=FILETTO,
            align='start', anchor=slug))
    famiglie = sezione(doppio(), *righe, riga_inchiostro(), gap='0', pad=('0', 'lato', 'sezione', 'lato'))

    fuori = sezione(
        C(H('Al banco c’è anche quello che non è online', 'h2'), impuntura(mt='s'),
          T('<p>Il catalogo online non comprende tutte le famiglie che vendiamo. Chiedi al banco o al telefono.</p>',
            style='body', color=INCHIOSTRO, mt='s'),
          C(*[C(T(f'<p>{v}</p>', style='body'), pad=(12, '0', 12, '0'), border_bottom=1, border_color=FILETTO) for v in [
              'Lacci in poliestere e cuoio', 'Cerniere in nylon e metallo', 'Chiodi e semenze in ferro e ottone',
              'Occhielli, agraffi e rivetti', 'Rinforzi e tessuti per tomaia', 'Adesivi Fratelli Zucchini',
              'Nastri abrasivi e tamponi SIA']], gap='0', mt='m', border_top=1, border_color=INCHIOSTRO),
          C(B(f'Chiama {TEL}', TEL_LINK, variant='primario'), mt='m'),
          w=(48.6, 100, 100), gap='0'),
        tavola('lastre-3x2.jpg', 'Scaffali di lastre nel magazzino', 4, 'Lastre per suole e sottopiedi in magazzino.',
               w=(40.4, 100, 100)),
        bg=PERGAMENA, dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='xl')

    condizioni = sezione(
        C(H('Condizioni per le aziende', 'h2'), T('<p>Dalle condizioni generali di vendita pubblicate.</p>', style='body',
                                                  color=GRAFITE), w=(32, 100, 100), gap='s'),
        C(registro_dati([
            ('Clienti', 'Aziende e titolari di partita IVA, con fattura, per gli ordini a distanza'),
            ('Ordine minimo', '200 euro di merce, IVA esclusa'),
            ('Pagamento', 'Bonifico anticipato'),
            ('Evasione', 'Entro 7 giorni lavorativi dal pagamento, per il materiale a magazzino'),
            ('Trasporto', 'Corriere Benvegnù oppure corriere del cliente in porto assegnato'),
          ]), link_testo('Condizioni generali di vendita (PDF)', CONDIZIONI_PDF, mt='s'), w=(56.9, 100, 100), gap='0'),
        dir='row', dir_t='column', justify='between', gap='xl')
    return [('apertura', apertura), ('indice', indice_ancore), ('famiglie', famiglie), ('fuori-catalogo', fuori),
            ('condizioni', condizioni), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# VIBRAM
# ---------------------------------------------------------------------------------------------
def vibram():
    apertura = apertura_interna(
        'Vibram a Vigonovo',
        f'Benvegnù è rivenditore autorizzato Vibram. Nel catalogo ci sono {N_VIBRAM} articoli: suole da città, montagna e lavoro, '
        'lastre compatte ed espanse, mezzesuole e tacchi. Servono a chi produce e a chi ripara.',
        destra=C(C(I(img('marchio-vibram.png'), 'Logo Vibram', height=(64, 56, 48), fit='contain'), min_h=(150, 130, 110),
                   justify='center', pad='m', bg=AVORIO, border=1, border_color=FILETTO),
                 tavola('espositore-4x5.jpg', 'Espositore Vibram nel negozio Benvegnù', 1, 'L’espositore Vibram al banco.'),
                 w=(32, 60, 100), gap='m'),
        allinea=('center', 'start', 'start'))
    cifre = sezione(registro_cifre([(str(N_VIBRAM), 'Articoli Vibram nel catalogo'), (str(FAM['vibram-suole']['n']), 'Suole'),
                                    (str(FAM['vibram-lastre']['n']), 'Lastre'),
                                    (str(FAM['vibram-mezzesuole-tacchi']['n']), 'Mezzesuole e tacchi')]),
                    pad=('0', 'lato', 'sezione', 'lato'))

    def blocco(titolo, slug, intro, tessere):
        return sezione(
            testata(titolo),
            C(T(f'<p>{intro}</p>', style='body', color=GRAFITE, max_w=640),
              T(f'<p>{FAM[slug]["n"]} articoli</p>', style='dati', align=('right', 'right', 'left'), fisso=True),
              dir='row', dir_m='column', justify='between', gap='s', mt='s'),
            C(griglia_tessere(tessere), mt='l'),
            gap='0', anchor=slug, pad=('0', 'lato', 'sezione', 'lato'))

    suole = blocco('Suole', 'vibram-suole', sottocategorie('vibram-suole') + '.', [
        tessera_prodotto('80075', '2600 Liverpool', 'Suola da città e tempo libero, monoblocco, disegno a onde'),
        tessera_prodotto('85109', '0056C Winter City', 'Suola da città e tempo libero da uomo'),
        tessera_prodotto('82768', '2603 Gumblock', 'Suola a tacco staccato, disegno Carrarmato'),
        tessera_prodotto('83137', '2609 Athena Gumlite', 'Suola per applicazioni ortopediche a dima extra large'),
        tessera_prodotto('85014', '4303 Betulla tranciata', 'Suola da città e tempo libero, disegno Carrarmato'),
        tessera_prodotto('83169', 'V.0121P Fourà PU', 'Suola in PU, nero e grigio, in più misure'),
    ])
    lastre = blocco('Lastre', 'vibram-lastre', sottocategorie('vibram-lastre') + '. Da tagliare a misura per suole, '
                                                'riparazioni e costruzioni ortopediche.', [
        tessera_prodotto('82268', '7106 Crepe', 'Lastra in gomma morbida'),
        tessera_prodotto('84305', '7107 Crepe cardata', 'Lastra in gomma compatta'),
        tessera_prodotto('84413', '7130 New Boulder', 'Lastra per arrampicata e bouldering, mescola extra morbida'),
    ])
    tacchi = blocco('Mezzesuole e tacchi', 'vibram-mezzesuole-tacchi', sottocategorie('vibram-mezzesuole-tacchi') + '.', [
        tessera_prodotto('83255', '2023 Wellness', 'Mezza suola in gomma compatta'),
        tessera_prodotto('83263', '2025 Sebastian', 'Mezza suola invernale in gomma compatta'),
        tessera_prodotto('80751', '1100T Montagna', 'Tacco 20,5 mm da montagna e sportivo, mescola Vibram Mont'),
    ])
    chi = sezione(
        C(C(H('Per chi produce', 'h3'),
            T('<p>Il calzaturificio sceglie modello, mescola e misure; insieme verifichiamo formati e quantità disponibili.</p>',
              style='body', color=INCHIOSTRO), gap='xs', pad=('s', '0', '0', '0'), border_top=1, border_color=INCHIOSTRO),
          C(H('Per chi ripara', 'h3'),
            T('<p>Il calzolaio trova mezzesuole, tacchi e lastre da tagliare per risuolare scarpe da città, da lavoro e da '
              'montagna.</p>', style='body', color=INCHIOSTRO), gap='xs', pad=('s', '0', '0', '0'), border_top=1,
            border_color=INCHIOSTRO, mt='m'),
          w=(40.4, 100, 100), gap='0'),
        tavola('tacchi-1x1.jpg', 'Scaffali di tacchi e mezzesuole', 2, 'Tacchi e mezzesuole a scaffale.', w=(40.4, 60, 100)),
        bg=PERGAMENA, dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='xl')
    pulsante = B('Chiedi un modello Vibram', mailto('Disponibilità Vibram', 'Modello:\nMisura:\nColore:\nQuantità:\n'),
                 variant='primario')
    return [('apertura', apertura), ('cifre', cifre), ('suole', suole), ('lastre', lastre), ('mezzesuole-tacchi', tacchi),
            ('per-chi', chi), ('banco', blocco_banco(pulsante))]


# ---------------------------------------------------------------------------------------------
# MARCHI
# ---------------------------------------------------------------------------------------------
def marchi():
    apertura = apertura_interna('I marchi al banco', 'I marchi di cui teniamo a magazzino i prodotti, con le famiglie che '
                                                     'trovi al banco e nel catalogo.')
    schede = [
        ('vibram', 'Vibram', f'Suole, mezzesuole, tacchi e lastre in gomma, per produzione e riparazione. È il marchio più presente '
                             f'nel catalogo: {N_VIBRAM} articoli.', [('La pagina Vibram', '/vibram/')], (72, 64, 52)),
        ('gutermann', 'A&amp;E Gütermann', 'Filati industriali per cucire. Per pelle e calzatura teniamo i filati in poliestere '
                                          'ritorto Mara e Tera, in più colori.',
         [('Filati ed elastici nel catalogo', '/catalogo/#filati-elastici')], (64, 56, 48)),
        ('girba', 'Girba', 'Prodotti chimici per la finitura di calzatura e pelletteria: tinture, creme e cere per tomaia, tinture '
                           'per bordi. Nel catalogo online: Bordobrill, Iris, Lederpolish, Nubio, Tingileder.',
         [('Prodotti chimici nel catalogo', '/catalogo/#prodotti-chimici')], (80, 72, 60)),
        ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi e primer per calzatura. Non sono ancora nel catalogo online: '
                                                   'chiedi al banco quali formati sono disponibili.',
         [('Chiedi gli adesivi', mailto('Adesivi Fratelli Zucchini'))], (80, 72, 60)),
    ]
    sito = {s: u for s, _, _, u, _ in MARCHI}
    righe = []
    for i, (slug, nome, testo, links, alt_logo) in enumerate(schede, 1):
        lk = ''.join(f'<a href="{u}">{t}</a>&nbsp;&nbsp;→<br>' for t, u in links) + \
            f'<a href="{sito[slug]}">Sito ufficiale {nome}</a>&nbsp;&nbsp;↗'
        righe.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=alt_logo, fit='contain'), justify='center',
              min_h=(240, 200, 150), pad='m', bg=AVORIO, border=1, border_color=FILETTO, w=(40.4, 40.4, 100)),
            C(H(f'{i:02d}', 'p', style='num'), H(nome, 'h2'), T(f'<p>{testo}</p>', style='body', color=GRAFITE, max_w=560),
              T(f'<p>{lk}</p>', style='link', color=INCHIOSTRO, link_color=INCHIOSTRO, link_hover=CUOIO), gap='s',
              w=(48.6, 52, 100)),
            dir='row', dir_m='column', justify='between', gap=('xl', 'l', 'm'), pad=('xl', '0', 'xl', '0'), border_bottom=1,
            border_color=FILETTO, align='center'))
    elenco = sezione(doppio(), *righe, gap='0', pad=('0', 'lato', 'sezione', 'lato'))
    altri = sezione(
        C(H('Altri nomi nel catalogo', 'h2'), impuntura(mt='s'), w=(32, 100, 100), gap='0'),
        C(T('<p>Olfa, Mozart, Mark, Lariz, Kai, Wiss, C.Dick, Norton, Pentel, Marvy, Mitsubishi, Stanley, Dremel, Einhell, '
            'Luxoro, 3M, Marigold, Sperian, Coats.</p>', style='lead', color=INCHIOSTRO),
          T('<p>Sono i produttori che compaiono nei nomi degli articoli del catalogo online, senza loghi. Per un marchio che '
            'non vedi, chiedi al banco.</p>', style='small', color=GRAFITE), w=(56.9, 100, 100), gap='s'),
        bg=PERGAMENA, dir='row', dir_t='column', justify='between', gap='xl')
    return [('apertura', apertura), ('elenco', elenco), ('altri-nomi', altri), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# NOVITÀ
# ---------------------------------------------------------------------------------------------
ARTICOLI_ESEMPIO = [
    ('Il nuovo sito di Benvegnù è online', '/novita/', 'Avviso'),
    (f'Il catalogo online: {TOTALE} articoli in 10 famiglie', '/catalogo/', 'Catalogo'),
]

# Il widget gratuito "Articoli recenti" di WordPress non ha controlli di stile in Elementor: CSS solo per il contenitore .bvg-news
STILE_NEWS = (
    '.bvg-news h5,.bvg-news .widget-title,.bvg-news .wp-block-heading{display:none}'
    '.bvg-news ul{list-style:none;margin:0;padding:0}'
    f'.bvg-news li{{display:grid;grid-template-columns:160px 1fr;column-gap:32px;align-items:baseline;padding:24px 0;'
    f'border-bottom:1px solid {FILETTO};margin:0}}'
    f".bvg-news li a{{grid-column:2;grid-row:1;font-family:'{BODONI}',Georgia,serif;font-weight:400;font-size:24px;line-height:30px;"
    f"color:{INCHIOSTRO};text-decoration:none}}"
    f'.bvg-news li a:hover,.bvg-news li a:focus{{color:{CUOIO}}}'
    f".bvg-news .post-date{{grid-column:1;grid-row:1;font-family:'{GROTESK}',Arial,sans-serif;font-weight:500;font-size:12px;"
    f'line-height:16px;letter-spacing:.14em;text-transform:uppercase;color:{GRAFITE}}}'
    '@media (max-width:767px){.bvg-news li{grid-template-columns:1fr}.bvg-news li a,.bvg-news .post-date{grid-column:1;grid-row:auto}'
    '.bvg-news .post-date{margin-top:8px}}'
)


def novita():
    apertura = apertura_interna('Novità', 'Avvisi del banco, nuovi arrivi e chiusure per ferie, con la data di ogni avviso.')
    elenco = sezione(
        C(doppio(), ARTICOLI(ARTICOLI_ESEMPIO, numero=10), RAW('', css=STILE_NEWS, solo_elementor=True), gap='0',
          css='bvg-news'),
        C(riga_dato('Arrivi', f'Per sapere se un articolo è arrivato: <a href="{TEL_LINK}">{TEL}</a>, negli orari del banco.'),
          riga_dato('Orari', f'{cap(ORARI)}. {cap(CHIUSURA)}.'), mt='l', gap='0'),
        gap='0', pad=('0', 'lato', 'sezione', 'lato'))
    return [('apertura', apertura), ('elenco', elenco), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# CONTATTI
# ---------------------------------------------------------------------------------------------
STILE_CF7 = (
    f".bvg-modulo .wpcf7 label,.bvg-modulo .bvg-scelta{{display:block;margin:0 0 24px;font:500 12px/16px '{GROTESK}',Arial,sans-serif;"
    f'letter-spacing:.14em;text-transform:uppercase;color:{GRAFITE}}}'
    '.bvg-modulo .wpcf7 p{margin:0}.bvg-modulo .wpcf7 br{display:none}'
    '.bvg-modulo .wpcf7-form-control-wrap{display:block}'
    '.bvg-modulo input[type=text],.bvg-modulo input[type=email],.bvg-modulo input[type=tel],.bvg-modulo select,'
    f'.bvg-modulo textarea{{display:block;width:100%;margin-top:8px;background:{AVORIO};border:1px solid {FILETTO_FORTE};'
    f"border-radius:0;box-shadow:none;padding:14px 16px;font:400 17px/24px '{GROTESK}',Arial,sans-serif;letter-spacing:0;"
    f'text-transform:none;color:{INCHIOSTRO}}}'
    '.bvg-modulo textarea{min-height:150px;resize:vertical}'
    f'.bvg-modulo input:focus,.bvg-modulo textarea:focus{{border-color:{INCHIOSTRO};outline:2px solid {CUOIO};outline-offset:2px}}'
    f".bvg-modulo input[type=submit]{{background:{INCHIOSTRO};color:{CARTA};border:1px solid {INCHIOSTRO};border-radius:0;"
    f"padding:16px 28px;font:600 13px/16px '{GROTESK}',Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;cursor:pointer;"
    'transition:background-color .12s linear,border-color .12s linear}'
    f'.bvg-modulo input[type=submit]:hover{{background:{CUOIO};border-color:{CUOIO}}}'
    f'.bvg-modulo input[type=checkbox],.bvg-modulo input[type=radio]{{accent-color:{CUOIO};width:18px;height:18px;margin:0 8px 0 0;vertical-align:-3px}}'
    '.bvg-modulo .wpcf7-list-item{display:block;margin:10px 0 0}'
    f'.bvg-modulo .wpcf7-list-item-label,.bvg-modulo .wpcf7-acceptance{{text-transform:none;letter-spacing:0;font-size:15px;color:{INCHIOSTRO}}}'
    f'.bvg-modulo .wpcf7-not-valid-tip{{color:{CUOIO_SCURO};font-size:14px;margin-top:6px;text-transform:none;letter-spacing:0}}'
    f'.bvg-modulo .wpcf7 form .wpcf7-response-output{{margin:24px 0 0;padding:14px 16px;border:1px solid {INCHIOSTRO};font-size:15px}}'
    '@media (max-width:767px){.bvg-modulo input[type=submit]{width:100%}}'
)


def contatti():
    apertura = apertura_interna('Contatti', 'Il banco è aperto dal lunedì al venerdì. Per una richiesta precisa, indica il codice '
                                            'dell’articolo.')
    corpo = ('Codice o nome articolo:\nColore, misura o formato:\nQuantità:\nRitiro al banco o spedizione:\n'
             'Ragione sociale e partita IVA:\nTelefono:\n')
    alternativa = (f'<p style="margin:0 0 16px">Scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a> indicando codice o nome '
                   'dell’articolo, colore, misura o formato, quantità, ritiro al banco o spedizione.</p>'
                   f'<p style="margin:0"><a href="{mailto("Richiesta disponibilità", corpo)}">Scrivi la richiesta</a></p>')
    dati = sezione(
        C(registro_dati([
            ('Indirizzo', f'{INDIRIZZO}<br>{cap(ZONA)}<br>{CITTA}'),
            ('Orari', f'{cap(ORARI)}<br>{cap(CHIUSURA)}'),
            ('Telefono', f'<a href="{TEL_LINK}">{TEL}</a>'),
            ('Fax', FAX),
            ('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
            ('PEC', PEC),
            ('Parcheggio', 'Posti per i clienti davanti al negozio'),
            ('Sede legale', SEDE_LEGALE),
          ]),
          C(tavola('sede-4x5.jpg', 'Ingresso della sede Benvegnù', 1, 'L’ingresso di Via del Lavoro 48.'), w=(60, 50, 100), mt='l'),
          w=(48.6, 100, 100), gap='0'),
        C(H('Chiedi disponibilità', 'h2'),
          T('<p>Rispondiamo nei giorni di apertura del banco.</p>', style='small', color=GRAFITE),
          C(SHORTCODE(CF7, alternativa_html=alternativa), RAW('', css=STILE_CF7, solo_elementor=True), mt='s', css='bvg-modulo'),
          w=(48.6, 100, 100), gap='xs', pad=('l', 'l', 'l', 'l'), bg=AVORIO, border=1, border_color=FILETTO, anchor='modulo'),
        dir='row', dir_t='column', justify='between', align='start', gap='xl', pad=('0', 'lato', 'sezione', 'lato'))
    mappa = sezione(
        C(MAPPA(f'Benvegnù, {INDIRIZZO}, {CITTA}', height=(480, 400, 320), zoom=15, grigia=True), pad=(16, 12, 10), bg=AVORIO,
          border=1, border_color=FILETTO),
        pad=('0', 'lato', 'sezione', 'lato'))
    condizioni = sezione(
        C(H('Condizioni di vendita', 'h3'),
          T('<p>Per le aziende con partita IVA valgono le condizioni generali di vendita.</p>', style='body', color=GRAFITE),
          w=(56.9, 100, 100), gap='xs'),
        C(link_testo('Condizioni generali di vendita (PDF)', CONDIZIONI_PDF), w=(32, 100, 100), align=('end', 'start', 'start')),
        dir='row', dir_t='column', justify='between', align=('center', 'start', 'start'), gap='m', bg=PERGAMENA,
        pad=('xl', 'lato', 'xl', 'lato'))
    return [('apertura', apertura), ('dati-modulo', dati), ('mappa', mappa), ('condizioni', condizioni)]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Benvegnù | Componenti e accessori per calzatura e pelletteria a Vigonovo, dal 1980',
     'descrizione': 'Suole e lastre Vibram, filati Gütermann, prodotti Girba, adesivi Fratelli Zucchini e utensili. Il banco di Vigonovo nella Riviera del Brenta, dal 1980.'},
    {'slug': '02-azienda', 'titolo': 'Azienda', 'sezioni': azienda,
     'titolo_seo': 'Azienda | Benvegnù, Vigonovo dal 1980',
     'descrizione': 'Dal 1980 a Vigonovo, nel distretto calzaturiero della Riviera del Brenta: per chi fa le scarpe e per chi le ripara.'},
    {'slug': '03-catalogo', 'titolo': 'Catalogo', 'sezioni': catalogo,
     'titolo_seo': f'Catalogo | {TOTALE} articoli per calzatura e pelletteria | Benvegnù',
     'descrizione': 'Utensili, filati ed elastici, modelleria, prodotti chimici, esposizione e cura, suole, lastre, mezzesuole e tacchi Vibram.'},
    {'slug': '04-vibram', 'titolo': 'Vibram', 'sezioni': vibram,
     'titolo_seo': 'Vibram | Suole, lastre, mezzesuole e tacchi | Benvegnù Vigonovo',
     'descrizione': f'Rivenditore autorizzato Vibram: {N_VIBRAM} articoli tra suole, lastre, mezzesuole e tacchi, per produzione e riparazione.'},
    {'slug': '05-marchi', 'titolo': 'Marchi', 'sezioni': marchi,
     'titolo_seo': 'Marchi | Vibram, Gütermann, Girba, Fratelli Zucchini | Benvegnù',
     'descrizione': 'I marchi che teniamo a magazzino e cosa trovi di ciascuno, al banco e nel catalogo.'},
    {'slug': '06-novita', 'titolo': 'Novità', 'sezioni': novita,
     'titolo_seo': 'Novità e avvisi | Benvegnù', 'descrizione': 'Avvisi del banco, nuovi arrivi e chiusure per ferie.'},
    {'slug': '07-contatti', 'titolo': 'Contatti', 'sezioni': contatti,
     'titolo_seo': 'Contatti | Benvegnù, Via del Lavoro 48, Vigonovo',
     'descrizione': f'{INDIRIZZO}, {CITTA}. Aperto {ORARI}. Tel. {TEL}. Richiesta di disponibilità online.'},
]
