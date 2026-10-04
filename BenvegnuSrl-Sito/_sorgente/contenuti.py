# -*- coding: utf-8 -*-
"""
Contenuti del sito Benvegnù S.r.l.: testi, struttura delle pagine e immagini.
Fonti dei testi: sito attuale (testi verbatim ripuliti dai refusi), catalogo online (874 articoli, crawl del
4 ottobre 2026), Registro Imprese, scheda Google. Ogni dato da far confermare al cliente è elencato in LEGGIMI.md.
"""
import json
import os
from urllib.parse import quote

import motore as m
from motore import C, H, T, B, I, MAPPA, LINEA_H, ARTICOLI

QUI = os.path.dirname(os.path.abspath(__file__))

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
ZONA = 'Zona industriale Tombelle'
ORARI = 'Dal lunedì al venerdì, 8:30-12:30 e 14:30-18:30'
ORARI_BREVE = 'Lun-ven 8:30-12:30 e 14:30-18:30'
CHIUSURA = 'Sabato e domenica chiuso'
PIVA = '02326850282'
REA = 'PD-222933'
SEDE_LEGALE = 'Piazzetta Primo Modin 12, 35129 Padova'
MAPS = ('https://www.google.com/maps/search/?api=1&query=Benvegn%C3%B9%20Via%20del%20Lavoro%2048%20Vigonovo'
        '&query_place_id=ChIJCYLIGbDFfkcRl5iSbyMPyb4')
CONDIZIONI_PDF = 'https://www.benvegnusrl.it/condizioni-di-vendita-Benvegnusrl.pdf'
FACEBOOK = 'https://www.facebook.com/benvegnusrl'


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    if corpo:
        url += '&body=' + quote(corpo)
    return url


CATALOGO = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
FAM = {f['slug']: f for f in CATALOGO['famiglie']}
TOTALE = CATALOGO['totale']                                            # 874
N_VIBRAM = sum(FAM[k]['n'] for k in ('vibram-suole', 'vibram-lastre', 'vibram-mezzesuole-tacchi'))   # 329

# nomi delle sottocategorie ripuliti (il sito attuale usa abbreviazioni)
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
# Componenti riusati
# ---------------------------------------------------------------------------------------------
def sezione(*children, bg=m.BIANCO, pad=('sezione', 'lato'), **p):
    return C(*children, bg=bg, pad=pad, tag='section', **p)


def intestazione(titolo, lead, livello='h1', stile='h1', colore=m.NERO, colore_lead=m.NERO_75, max_w=760):
    return C(
        H(titolo, livello, style=stile, color=colore),
        T(f'<p>{lead}</p>', style='lead', color=colore_lead, max_w=max_w),
        gap='m')


def blocco_banco(titolo='Vieni al banco'):
    """L'unico blocco rosso pieno della pagina: indirizzo, orari, telefono."""
    return sezione(
        C(
            H(titolo, 'h2', color=m.BIANCO),
            T(f'<p>{INDIRIZZO}, {ZONA.lower()}, {CITTA}. Parcheggio clienti davanti al negozio.</p>'
              f'<p>{ORARI}. {CHIUSURA}.</p>', style='lead', color=m.BIANCO, link_color=m.BIANCO, link_hover=m.NERO),
            w=(55, 55, 100), gap='m'),
        C(
            T('<p>Telefono</p>', style='label', color=m.BIANCO),
            H(TEL, 'p', style='tel', color=m.BIANCO, link=TEL_LINK),
            T(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>', style='body', color=m.BIANCO, link_color=m.BIANCO, link_hover=m.NERO),
            C(B('Apri in Google Maps', MAPS, variant='bianco'), B('Scrivi una email', mailto('Richiesta informazioni'), variant='contorno-su-rosso'),
              dir='row', dir_m='column', gap='s', mt=('s', 's', 'xs')),
            w=(45, 45, 100), gap='s'),
        bg=m.ROSSO, dir='row', dir_m='column', gap='xl', align=('end', 'end', 'start'), anchor='banco')


def riga_indice(numero, titolo, testo, destra=None, colore=m.NERO, colore_testo=m.NERO_75, colore_num=m.ROSSO,
                linea=m.LINEA, link=None, ancora=None):
    """Riga di un indice numerato: numero, titolo, testo, dato a destra; filetto sopra."""
    centro = C(H(titolo, 'h3', color=colore), T(f'<p>{testo}</p>', style='body', color=colore_testo), gap='xs', grow=True)
    figli = [H(numero, 'p', style='num_s', color=colore_num, fisso=True), centro]
    if destra:
        figli.append(T(f'<p>{destra}</p>', style='label', color=colore, align=('right', 'right', 'left'), fisso=True))
    return C(*figli, dir='row', dir_m='column', gap=('l', 'm', 'xs'), pad=('m', '0', 'm', '0'), border_top=1,
             border_color=linea, align=('start', 'start', 'start'), link=link, anchor=ancora)


def card_prodotto(pid, titolo, testo, sotto=None):
    return C(
        I(img(f'prodotto-{pid}.jpg'), titolo, height=(260, 220, 120), fit='contain'),
        C(H(titolo, 'h4', style='h4'), T(f'<p>{testo}</p>', style='small', color=m.NERO_75),
          *([T(f'<p>{sotto}</p>', style='label', color=m.ROSSO)] if sotto else []), gap='xs'),
        w=(33.33, 33.33, 100), gap='s', pad='m', border=1, border_color=m.LINEA)


def griglia(*cards, per_riga=3):
    righe = []
    for i in range(0, len(cards), per_riga):
        righe.append(C(*cards[i:i + per_riga], dir='row', dir_m='column', gap='m'))
    return C(*righe, gap='m')


# ---------------------------------------------------------------------------------------------
# Header e footer (template separati, tipo "section")
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Catalogo', '/catalogo/'), ('Vibram', '/vibram/'), ('Marchi', '/marchi/'), ('Azienda', '/azienda/'),
             ('Novità', '/novita/'), ('Contatti', '/contatti/')]


def header():
    barra = C(
        T(f'<p>Banco aperto {ORARI_BREVE.lower()}</p>', style='small', color=m.BIANCO_70, hide=['mobile']),
        T(f'<p>{ORARI_BREVE}</p>', style='small', color=m.BIANCO_70, hide=['desktop', 'tablet']),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a><span class="sep">&nbsp;&nbsp;·&nbsp;&nbsp;</span><a href="mailto:{EMAIL}">{EMAIL}</a></p>',
          style='small', color=m.BIANCO, link_color=m.BIANCO, link_hover=m.BIANCO_70, align='right', hide=['mobile']),
        T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='small', color=m.BIANCO, link_color=m.BIANCO,
          link_hover=m.BIANCO_70, align='right', hide=['desktop', 'tablet']),
        dir='row', justify='between', align='center', gap='s', pad=(10, 'lato'), bg=m.NERO)
    voci = [H(t, 'div', style='nav', link=u) for t, u in VOCI_MENU]
    marchio = C(
        I(img('logo-benvegnu.png'), 'Benvegnù S.r.l.', link='/', w_img=(210, 190, 170)),
        T('<p>Componenti per calzatura e pelletteria<br>Vigonovo, dal 1980</p>', style='label', color=m.NERO_75,
          hide=['tablet', 'mobile']),
        dir='row', align='center', gap='m', w=(38, 100, 100))
    menu = C(*voci, B(f'Chiama {TEL}', TEL_LINK, variant='primario', hide=['mobile']),
             dir='row', align='center', gap=('m', 'm', 's'), wrap=(False, True, True), justify=('end', 'start', 'start'),
             w=(62, 100, 100))
    testata = C(marchio, menu, dir='row', dir_t='column', justify=('between', 'start', 'start'), align=('center', 'start', 'start'),
                gap=('m', 's', 's'), pad=(18, 'lato'), bg=m.BIANCO, border_bottom=1, border_color=m.LINEA)
    return C(barra, testata, pad='0', boxed=False, tag='header')


def footer():
    def colonna(titolo, html, w):
        return C(T(f'<p>{titolo}</p>', style='label', color=m.BIANCO),
                 T(html, style='small', color=m.BIANCO_70, link_color=m.BIANCO, link_hover=m.BIANCO_70), gap='s', w=w)
    pagine = ''.join(f'<a href="{u}">{t}</a><br>' for t, u in VOCI_MENU)
    righe = C(
        C(I(img('logo-benvegnu-bianco.png'), 'Benvegnù S.r.l.', link='/', w_img=(190, 180, 170)),
          T('<p>Componenti, accessori e utensili per calzatura e pelletteria. Vigonovo, dal 1980.</p>',
            style='small', color=m.BIANCO_70), gap='m', w=(31, 46, 100)),
        colonna('Il banco', f'<p>{INDIRIZZO}<br>{CITTA}<br>{ZONA}</p><p>{ORARI_BREVE}<br>{CHIUSURA}</p>', (23, 46, 100)),
        colonna('Contatti', f'<p>Tel. <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
                            f'PEC {PEC}</p>', (23, 46, 100)),
        colonna('Pagine', f'<p>{pagine}<a href="{CONDIZIONI_PDF}">Condizioni di vendita (PDF)</a><br>'
                          f'<a href="{FACEBOOK}">Facebook</a></p>', (23, 46, 100)),
        dir='row', dir_m='column', wrap=(False, True, False), gap='l')
    legale = C(
        T(f'<p>© 2026 Benvegnù S.r.l. · P.IVA {PIVA} · REA {REA} · Sede legale {SEDE_LEGALE}</p>', style='small', color=m.BIANCO_70),
        T('<p><a href="/privacy/">Privacy</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="/cookie/">Cookie</a></p>', style='small',
          color=m.BIANCO_70, link_color=m.BIANCO_70, link_hover=m.BIANCO, align=('right', 'right', 'left')),
        dir='row', dir_m='column', justify='between', gap='s', pad=('m', '0', '0', '0'), border_top=1, border_color=m.LINEA_SCURA)
    return C(righe, legale, gap='xl', pad=(('xl'), 'lato', 'l', 'lato'), bg=m.NERO, tag='footer')


# ---------------------------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------------------------
def tile(numero, titolo, testo, conteggio, foto, alt, link):
    """Blocco grande con foto come navigazione (dal PMF): la foto senza testo sopra, la didascalia sotto,
    tutto il blocco è un link."""
    return C(
        I(img(foto), alt, height=(380, 300, 220)),
        C(H(numero, 'p', style='num_s', color=m.ROSSO, fisso=True),
          C(H(titolo, 'h3'), T(f'<p>{testo}</p>', style='small', color=m.NERO_75), gap='xs', grow=True),
          T(f'<p>{conteggio}&nbsp;&nbsp;→</p>', style='label', color=m.NERO, align=('right', 'right', 'left'), fisso=True),
          dir='row', dir_m='column', gap=('m', 's', 'xs'), pad=('m', 'm', 'm', 'm'), align='start'),
        w=(50, 50, 100), gap='0', border=1, border_color=m.NERO, link=link, overflow=True)


def home():
    n_tomaia = FAM['filati-elastici']['n'] + FAM['modelleria-riparazione']['n']
    n_cura = sum(FAM[k]['n'] for k in ('prodotti-chimici', 'esposizione-cura', 'igiene-sicurezza', 'imballaggio'))
    apertura = sezione(
        C(H('Forniture per calzaturifici, pelletterie e calzolai', 'h1', style='display'),
          T('<p>Suole e lastre Vibram, filati, utensili e prodotti per la rifinitura del fondo e della tomaia. '
            'Al banco di Vigonovo, nella Riviera del Brenta, dal 1980.</p>', style='lead', color=m.NERO_75, max_w=620),
          C(B('Sfoglia il catalogo', '/catalogo/', variant='primario'), B('Come arrivare', MAPS, variant='contorno'),
            dir='row', dir_m='column', gap='s'),
          w=(56, 56, 100), gap='l', justify='center'),
        C(I(img('sede-esterno-verticale.jpg'), 'La sede Benvegnù in Via del Lavoro 48 a Vigonovo', height=(600, 480, 300)),
          T('<p>La sede di Via del Lavoro 48, zona industriale Tombelle</p>', style='small', color=m.NERO_75),
          w=(44, 44, 100), gap='s'),
        dir='row', dir_m='column', gap='xl', align='center', pad=('l', 'lato', 'l', 'lato'))

    catalogo = sezione(
        C(H('Il catalogo', 'h2'),
          C(T(f'<p>{TOTALE} articoli in 10 famiglie. Quello che non trovi online, chiedilo al banco.</p>', style='body',
              color=m.NERO_75),
            T('<p><a href="/catalogo/">Tutte le famiglie</a>&nbsp;&nbsp;→</p>', style='label', color=m.NERO, link_color=m.NERO),
            gap='xs', w=(40, 50, 100)),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='m'),
        C(tile('01', 'Vibram', 'Suole, lastre, mezzesuole e tacchi', f'{N_VIBRAM} articoli', 'banco-suole-vibram.jpg',
               'Suole Vibram sul banco del negozio', '/vibram/'),
          tile('02', 'Utensili', 'Forbici, coltelli, lesine, punzoni, martelli, mole, strumenti di misura, torchi',
               f'{FAM["utensili"]["n"]} articoli', 'magazzino-colle-abrasivi.jpg', 'Scaffali con mole, nastri e barattoli',
               '/catalogo/#utensili'),
          dir='row', dir_m='column', gap='m'),
        C(tile('03', 'Tomaia e modelleria', 'Filati, elastici, allungaforme, alzi, materiali per modelleria e riparazione',
               f'{n_tomaia} articoli', 'magazzino-rotoli.jpg', 'Rotoli di materiali in magazzino', '/catalogo/#filati-elastici'),
          tile('04', 'Cura, esposizione e imballo', 'Prodotti Girba, cura della scarpa, calzanti, guanti, nastri ed etichette',
               f'{n_cura} articoli', 'magazzino-solette-cura.jpg', 'Scaffali con solette e prodotti per la cura',
               '/catalogo/#esposizione-cura'),
          dir='row', dir_m='column', gap='m'),
        gap='l', anchor='catalogo')

    righe_v = [riga_indice(f'{i:02d}', t, x, destra=f'{n} articoli', colore=m.BIANCO, colore_testo=m.BIANCO_70,
                           colore_num=m.BIANCO, linea=m.LINEA_SCURA)
               for i, (t, x, n) in enumerate([
                   ('Suole', sottocategorie('vibram-suole', False), FAM['vibram-suole']['n']),
                   ('Lastre', sottocategorie('vibram-lastre', False), FAM['vibram-lastre']['n']),
                   ('Mezzesuole e tacchi', sottocategorie('vibram-mezzesuole-tacchi', False), FAM['vibram-mezzesuole-tacchi']['n'])], 1)]
    vibram = sezione(
        C(H('Vibram al banco', 'h2', color=m.BIANCO),
          T(f'<p>Siamo rivenditori autorizzati Vibram. In catalogo ci sono {N_VIBRAM} articoli Vibram, per chi produce '
            'e per chi ripara.</p>', style='lead', color=m.BIANCO_70, max_w=560),
          C(*righe_v, gap='0', mt=('xs', 'xs', '0')),
          C(B('La pagina Vibram', '/vibram/', variant='primario-su-nero'), mt='xs'),
          w=(55, 55, 100), gap='m'),
        C(I(img('banco-espositore-vibram.jpg'), 'Espositore Vibram nel negozio Benvegnù', height=(560, 460, 260)),
          w=(45, 45, 100)),
        bg=m.NERO, dir='row', dir_m='column', gap='xl', align='center')

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
        C(H('Come si lavora con noi', 'h2'),
          T('<p>Che tu passi al banco o ordini da lontano, i passaggi sono questi.</p>', style='body', color=m.NERO_75),
          w=(34, 100, 100), gap='m'),
        C(*[riga_indice(n, t, x) for n, t, x in passi], C(LINEA_H(m.LINEA)), w=(66, 100, 100), gap='0'),
        dir='row', dir_t='column', gap='xl', border_top=1, border_color=m.LINEA)

    marchi = sezione(
        C(H('I marchi', 'h2'),
          T('<p>Teniamo a magazzino i prodotti di questi marchi. <a href="/marchi/">Cosa trovi di ciascuno</a>.</p>',
            style='body', color=m.NERO_75, link_color=m.NERO),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='m'),
        striscia_marchi(),
        gap='l', border_top=1, border_color=m.LINEA)

    return [('apertura', apertura), ('catalogo', catalogo), ('vibram', vibram), ('come-si-lavora', come),
            ('marchi', marchi), ('banco', blocco_banco())]


MARCHI = [
    ('vibram', 'Vibram', 'Suole, lastre, mezzesuole e tacchi', 'https://www.vibram.com/it/'),
    ('gutermann', 'Gütermann', 'Filati per cucire Mara e Tera', 'https://www.guetermann.com/'),
    ('girba', 'Girba', 'Tinture e prodotti per il finissaggio', 'https://www.girbasrl.it/it/'),
    ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi per calzatura', 'https://www.zucchini.it/it/'),
]


def striscia_marchi():
    tessere = []
    for slug, nome, famiglia, _ in MARCHI:
        tessere.append(C(
            C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=(90, 80, 64), fit='contain'), min_h=(120, 110, 90),
              justify='center'),
            H(nome, 'h3', style='h4'), T(f'<p>{famiglia}</p>', style='small', color=m.NERO_75),
            w=(25, 50, 50), gap='xs', pad=('m', 'm', 'm', 'm'), border_right=1, border_bottom=1, border_color=m.LINEA))
    return C(*tessere, dir='row', wrap=True, gap='0', border_top=1, border_left=1, border_color=m.LINEA)


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
    indice = ''.join(f'<a href="#{slug}">{FAM[slug]["nome"]}</a>&nbsp;&nbsp;&nbsp; ' for slug, _, _ in ORDINE_FAMIGLIE)
    apertura = sezione(
        intestazione('Catalogo', f'{TOTALE} articoli in 10 famiglie, dagli utensili alle suole Vibram. Per disponibilità, '
                                 'colori e misure chiedi al banco o telefona negli orari di apertura.'),
        T(f'<p>{indice}</p>', style='nav', color=m.NERO, link_color=m.NERO, mt=('xs', 'xs', '0')),
        gap='l', pad=('l', 'lato', 'l', 'lato'), border_bottom=1, border_color=m.LINEA)

    righe = []
    for i, (slug, foto, esempi) in enumerate(ORDINE_FAMIGLIE, 1):
        f = FAM[slug]
        miniatura = (I(img(f'prodotto-{foto}.jpg'), f['nome'], height=(150, 130, 120), fit='contain')
                     if foto else C(T('<p>Prodotti Girba<br>per il finissaggio</p>', style='label', color=m.NERO_75,
                                      align='center'), min_h=(150, 130, 120), justify='center', bg=m.BIANCO,
                                    border=1, border_color=m.LINEA))
        righe.append(C(
            H(f'{i:02d}', 'p', style='num_s', color=m.ROSSO, fisso=True),
            C(miniatura, w=(16, 20, 40)),
            C(H(f['nome'], 'h3'),
              T(f'<p>{sottocategorie(slug)}</p>', style='body', color=m.NERO_75),
              T('<p>' + '<br>'.join(esempi) + '</p>', style='small', color=m.NERO),
              gap='s', grow=True),
            C(T(f'<p>{f["n"]} articoli</p>', style='label', color=m.NERO, align=('right', 'right', 'left')),
              T(f'<p><a href="{mailto("Disponibilità: " + f["nome"])}">Chiedi disponibilità</a></p>', style='small',
                color=m.ROSSO, link_color=m.ROSSO, link_hover=m.NERO, align=('right', 'right', 'left')),
              gap='xs', w=(18, 20, 100)),
            dir='row', dir_m='column', gap=('l', 'm', 's'), pad=('l', '0', 'l', '0'), border_top=1, border_color=m.LINEA,
            anchor=slug))
    famiglie = sezione(*righe, C(LINEA_H(m.LINEA)), gap='0', pad=('m', 'lato', 'sezione', 'lato'))

    non_online = sezione(
        C(H('Al banco c’è anche quello che non è online', 'h2'),
          T(f'<p>Il catalogo online non comprende tutte le famiglie che vendiamo. Chiedi al banco o chiama il {TEL}.</p>',
            style='body', color=m.NERO_75),
          C(B('Chiedi un articolo', mailto('Richiesta articolo non in catalogo'), variant='primario'), mt='xs'),
          w=(40, 100, 100), gap='m'),
        C(T('<ul><li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
            '<li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>', style='body'),
          T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per l’incollaggio Fratelli Zucchini</li>'
            '<li>Rinforzi per tomaia in tessuto</li><li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per tomaia</li></ul>',
            style='body'),
          dir='row', dir_m='column', gap='l', w=(60, 100, 100)),
        dir='row', dir_t='column', gap='xl', border_top=1, border_color=m.LINEA)
    return [('apertura', apertura), ('famiglie', famiglie), ('non-online', non_online), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# VIBRAM
# ---------------------------------------------------------------------------------------------
def vibram():
    apertura = sezione(
        C(H('Vibram a Vigonovo', 'h1', color=m.BIANCO),
          T(f'<p>Benvegnù è rivenditore autorizzato Vibram. Nel catalogo ci sono {N_VIBRAM} articoli: suole da città, '
            'montagna e lavoro, lastre compatte ed espanse, mezzesuole e tacchi. Servono a chi produce e a chi ripara.</p>',
            style='lead', color=m.BIANCO_70, max_w=600),
          C(B('Chiedi disponibilità', mailto('Disponibilità Vibram', 'Modello:\nMisura:\nColore:\nQuantità:\n'),
              variant='primario-su-nero'),
            B(f'Chiama {TEL}', TEL_LINK, variant='contorno-bianco'), dir='row', dir_m='column', gap='s'),
          w=(52, 52, 100), gap='l'),
        C(I(img('banco-suole-vibram.jpg'), 'Suole e mezzesuole Vibram sul banco', height=(520, 420, 260)), w=(48, 48, 100)),
        bg=m.NERO, dir='row', dir_m='column', gap='xl', align='center', pad=('sezione', 'lato'))

    def blocco(titolo, slug, intro, cards, bordo=True):
        return sezione(
            C(H(titolo, 'h2'), T(f'<p>{intro}</p>', style='body', color=m.NERO_75, max_w=520),
              T(f'<p>{FAM[slug]["n"]} articoli</p>', style='label', align=('right', 'right', 'left')),
              dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='m'),
            griglia(*cards), gap='l', anchor=slug, **({'border_top': 1, 'border_color': m.LINEA} if bordo else {}))

    suole = blocco('Suole', 'vibram-suole', sottocategorie('vibram-suole') + '.', [
        card_prodotto('80075', '2600 Liverpool', 'Suola da città e tempo libero, monoblocco, disegno a onde'),
        card_prodotto('85109', '0056C Winter City', 'Suola da città e tempo libero da uomo'),
        card_prodotto('82768', '2603 Gumblock', 'Suola da città e tempo libero a tacco staccato, disegno Carrarmato'),
        card_prodotto('83137', '2609 Athena Gumlite', 'Suola per applicazioni ortopediche a dima extra large'),
        card_prodotto('85014', '4303 Betulla tranciata', 'Suola da città e tempo libero, monoblocco, disegno Carrarmato'),
        card_prodotto('83169', 'V.0121P Fourà PU', 'Suola in PU, nero e grigio, in più misure'),
    ], bordo=False)
    lastre = blocco('Lastre', 'vibram-lastre', sottocategorie('vibram-lastre') + '. Da tagliare a misura per suole, '
                                                 'riparazioni e costruzioni ortopediche.', [
        card_prodotto('82268', '7106 Crepe', 'Lastra in gomma morbida'),
        card_prodotto('84305', '7107 Crepe cardata', 'Lastra in gomma compatta'),
        card_prodotto('84413', '7130 New Boulder', 'Lastra per arrampicata e bouldering, mescola extra morbida'),
        card_prodotto('84952', '8281 Diflex', 'Lastra per ortesi plantari, per sottopiedi e zeppe'),
    ][:3])
    tacchi = blocco('Mezzesuole e tacchi', 'vibram-mezzesuole-tacchi', sottocategorie('vibram-mezzesuole-tacchi') + '.', [
        card_prodotto('83255', '2023 Wellness', 'Mezza suola in gomma compatta'),
        card_prodotto('83263', '2025 Sebastian', 'Mezza suola invernale in gomma compatta'),
        card_prodotto('80751', '1100T Montagna', 'Tacco 20,5 mm da montagna e sportivo, mescola Vibram Mont'),
    ])
    chi = sezione(
        C(H('Per chi produce', 'h3'),
          T('<p>Calzaturifici e suolifici: scegli modello, mescola e misure, poi verifichiamo insieme formati e quantità '
            'disponibili.</p>', style='body', color=m.NERO_75), w=(50, 50, 100), gap='s', pad=('l', 'l', 'l', '0'),
          border_top=4, border_color=m.NERO),
        C(H('Per chi ripara', 'h3'),
          T('<p>Calzolai: mezzesuole, tacchi e lastre da tagliare per risuolare scarpe da città, da lavoro e da montagna.</p>',
            style='body', color=m.NERO_75), w=(50, 50, 100), gap='s', pad=('l', 'l', 'l', '0'), border_top=4,
          border_color=m.NERO),
        dir='row', dir_m='column', gap='l', pad=('0', 'lato', 'sezione', 'lato'))
    return [('apertura', apertura), ('suole', suole), ('lastre', lastre), ('mezzesuole-tacchi', tacchi),
            ('per-chi', chi), ('banco', blocco_banco('Chiedi un modello Vibram'))]


# ---------------------------------------------------------------------------------------------
# MARCHI (dal "sponsor" del PMF: chi c'è e cosa porta)
# ---------------------------------------------------------------------------------------------
def marchi():
    apertura = sezione(
        intestazione('Marchi', 'I marchi che trovi al banco e cosa c’è di ciascuno. Nel catalogo compaiono anche utensili '
                               'e materiali di altri produttori.'),
        pad=('l', 'lato', 'l', 'lato'))
    schede = [
        ('vibram', 'Vibram', f'Suole, mezzesuole, tacchi e lastre in gomma, per produzione e riparazione. È il marchio più '
                             f'presente nel nostro catalogo: {N_VIBRAM} articoli.', [('La pagina Vibram', '/vibram/')]),
        ('gutermann', 'Gütermann', 'Filati industriali per cucire. Per pelle e calzatura teniamo i filati in poliestere ritorto '
                                   'Mara e Tera, in più colori.', [('Filati ed elastici nel catalogo', '/catalogo/#filati-elastici')]),
        ('girba', 'Girba', 'Prodotti chimici per il finissaggio di calzatura e pelletteria: tinture e prodotti per tomaia e '
                           'bordi. Nel catalogo online: Bordobrill, Iris, Lederpolish, Nubio, Tingileder.',
         [('Prodotti chimici nel catalogo', '/catalogo/#prodotti-chimici')]),
        ('fratelli-zucchini', 'Fratelli Zucchini', 'Adesivi e prodotti per l’incollaggio in calzatura. Non sono ancora nel '
                                                   'catalogo online: chiedi al banco quali formati sono disponibili.',
         [('Chiedi gli adesivi', mailto('Adesivi Fratelli Zucchini'))]),
    ]
    sito = {s: u for s, _, _, u in MARCHI}
    righe = []
    for i, (slug, nome, testo, links) in enumerate(schede, 1):
        lk = ''.join(f'<a href="{u}">{t}</a>&nbsp;&nbsp;→<br>' for t, u in links) + f'<a href="{sito[slug]}">Sito ufficiale {nome}</a>&nbsp;&nbsp;↗'
        righe.append(C(
            C(C(I(img(f'marchio-{slug}.png'), f'Logo {nome}', height=(110, 100, 80), fit='contain'), justify='center',
                min_h=(200, 180, 140), pad='m', border=1, border_color=m.LINEA), w=(30, 34, 100)),
            C(H(f'{i:02d}', 'p', style='num_s', color=m.ROSSO), H(nome, 'h2', style='h3'),
              T(f'<p>{testo}</p>', style='body', color=m.NERO_75, max_w=620),
              T(f'<p>{lk}</p>', style='small', color=m.NERO, link_color=m.NERO), gap='s', grow=True),
            dir='row', dir_m='column', gap=('xl', 'l', 'm'), pad=('l', '0', 'l', '0'), border_top=1, border_color=m.LINEA,
            align='start'))
    elenco = sezione(*righe, C(LINEA_H(m.LINEA)), gap='0', pad=('0', 'lato', 'sezione', 'lato'))
    altri = sezione(
        C(H('Negli articoli del catalogo trovi anche', 'h2', style='h3'), w=(34, 100, 100)),
        C(T('<p>Olfa, Mozart, Mark, Lariz, Kai, Wiss, C.Dick, Norton, Pentel, Marvy, Mitsubishi, Stanley, Dremel, Einhell, '
            'Luxoro, 3M, Marigold, Sperian, Coats.</p>', style='lead', color=m.NERO),
          T('<p>Sono i marchi che compaiono nei nomi degli articoli del catalogo online. Per un marchio che non vedi, chiedi.</p>',
            style='small', color=m.NERO_75), w=(66, 100, 100), gap='s'),
        dir='row', dir_t='column', gap='l', border_top=1, border_color=m.LINEA)
    return [('apertura', apertura), ('elenco', elenco), ('altri-marchi', altri), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# AZIENDA (chi siamo + tabella "Dal 1980", dal pattern risultati del PMF)
# ---------------------------------------------------------------------------------------------
def azienda():
    apertura = sezione(
        intestazione('Dal 1980 a Vigonovo', 'Benvegnù nasce nel 1980 a Vigonovo, nell’area calzaturiera della Riviera del '
                     'Brenta. Vendiamo componenti e accessori per calzature e pelletterie, in particolare i materiali per la '
                     'rifinitura del fondo e della tomaia, e tutta la piccola utensileria. Siamo specializzati in suole e '
                     'lastre in gomma Vibram.', max_w=820),
        I(img('sede-esterno.jpg'), 'La sede Benvegnù in Via del Lavoro 48, zona industriale Tombelle, Vigonovo',
          height=(520, 400, 220)),
        gap='l', pad=('l', 'lato', 'sezione', 'lato'))

    cosa = sezione(
        C(H('Cosa vendiamo', 'h2'),
          T(f'<p>Il catalogo online ha {TOTALE} articoli in 10 famiglie. Al banco trovi anche le famiglie che non sono '
            'online.</p>', style='body', color=m.NERO_75),
          C(B('Sfoglia il catalogo', '/catalogo/', variant='primario'), mt='xs'),
          w=(34, 100, 100), gap='m'),
        C(T('<ul><li>Suole e lastre in gomma Vibram</li><li>Filo in poliestere ed elastico per tomaia</li>'
            '<li>Lacci in poliestere e cuoio</li><li>Cerniere in nylon e metallo</li><li>Tallonette coprichiodi</li>'
            '<li>Piccola utensileria per la calzatura</li><li>Nastri abrasivi e tamponi SIA</li><li>Pennelli a mano e spazzole</li></ul>',
            style='body'),
          T('<ul><li>Chiodi e semenze in ferro e ottone</li><li>Prodotti per la rifinitura della suola e della tomaia</li>'
            '<li>Prodotti per l’incollaggio Fratelli Zucchini</li><li>Rinforzi per tomaia in tessuto</li>'
            '<li>Occhielli, agraffi e rivetti</li><li>Tessuti sintetici per la tomaia</li></ul>', style='body'),
          dir='row', dir_m='column', gap='l', w=(66, 100, 100)),
        dir='row', dir_t='column', gap='xl', border_top=1, border_color=m.LINEA)

    tappe = [
        ('1980', 'Inizio dell’attività', 'A Vigonovo, nel distretto calzaturiero della Riviera del Brenta.'),
        ('1990', 'Nasce Benvegnù S.r.l.', 'Iscrizione alla Camera di Commercio di Padova il 24 ottobre 1990.'),
        ('2014', 'Il catalogo va online', f'Dal 16 aprile 2014 i prodotti sono sul sito. Oggi sono {TOTALE} articoli in 10 famiglie.'),
        ('2026', 'Il nuovo sito', 'Il catalogo si consulta anche da telefono, con codici e famiglie.'),
    ]
    righe = [C(H(a, 'p', style='num', color=m.ROSSO, fisso=True), C(H(t, 'h3'), w=(30, 34, 100)),
               T(f'<p>{d}</p>', style='body', color=m.NERO_75, grow=True),
               dir='row', dir_m='column', gap=('l', 'm', 'xs'), pad=('m', '0', 'm', '0'), border_top=1, border_color=m.LINEA,
               align=('center', 'center', 'start'))
             for a, t, d in tappe]
    storia = sezione(
        C(H('Dal 1980', 'h2'), T('<p>Le date che possiamo documentare.</p>', style='body', color=m.NERO_75),
          dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='s'),
        C(*righe, C(LINEA_H(m.LINEA)), gap='0'),
        gap='l', border_top=1, border_color=m.LINEA)

    distretto = sezione(
        C(I(img('magazzino-corsia.jpg'), 'Corsia del magazzino Benvegnù', height=(460, 380, 240)), w=(50, 50, 100)),
        C(H('Nel distretto della Riviera del Brenta', 'h2'),
          T('<p>Vigonovo è uno dei comuni del distretto calzaturiero della Riviera del Brenta, con Stra, Fiesso d’Artico, Dolo e '
            'Fossò. Nel distretto lavorano oltre 500 imprese della filiera e si producono circa 20 milioni di paia di scarpe '
            'l’anno.</p><p>Per chi lavora qui, il banco è a pochi chilometri: si passa, si guarda il materiale, si ritira.</p>',
            style='body', color=m.NERO_75),
          T('<p>Fonti: Unioncamere, “Le calzature della Riviera del Brenta”; FashionUnited, 7 novembre 2024.</p>',
            style='small', color=m.NERO_75),
          w=(50, 50, 100), gap='m'),
        dir='row', dir_m='column', gap='xl', align='center', bg=m.BIANCO, border_top=1, border_color=m.LINEA)

    clienti = [
        ('Calzaturifici', 'Suole e lastre Vibram, filati, elastici, prodotti per il fondo e la tomaia.'),
        ('Pelletterie', 'Filati, utensili da taglio, punzoni, tinture per bordi, prodotti per il finissaggio.'),
        ('Calzolai', 'Mezzesuole, tacchi e lastre Vibram per la riparazione, colle, utensili.'),
        ('Stilisti e modellisti', 'Materiali per modelleria, alzi e allungaforme, compassi, strumenti di misura.'),
        ('Negozi di calzature', 'Calzanti, tendiscarpe, prodotti per la cura, calze monouso per la prova.'),
    ]
    per_chi = sezione(
        C(H('Per chi lavoriamo', 'h2'), w=(34, 100, 100)),
        C(*[riga_indice(f'{i:02d}', t, x) for i, (t, x) in enumerate(clienti, 1)], C(LINEA_H(m.LINEA)), w=(66, 100, 100),
          gap='0'),
        dir='row', dir_t='column', gap='xl', border_top=1, border_color=m.LINEA)

    condizioni = sezione(
        C(H('Condizioni di vendita', 'h3'),
          T('<p>Per le aziende con partita IVA valgono le condizioni generali di vendita: ordine minimo, pagamento e spedizione '
            'sono indicati nel documento.</p>', style='body', color=m.NERO_75), w=(60, 60, 100), gap='s'),
        C(B('Scarica il PDF', CONDIZIONI_PDF, variant='contorno'), w=(40, 40, 100), align=('end', 'end', 'start')),
        dir='row', dir_m='column', gap='l', align='center', pad=('l', 'lato', 'l', 'lato'), border_top=1, border_color=m.LINEA)
    return [('apertura', apertura), ('cosa-vendiamo', cosa), ('dal-1980', storia), ('distretto', distretto),
            ('per-chi', per_chi), ('condizioni', condizioni), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# NOVITÀ
# ---------------------------------------------------------------------------------------------
ARTICOLI_ESEMPIO = [
    ('Il nuovo sito di Benvegnù è online', '/novita/', 'Avviso'),
    (f'Il catalogo online: {TOTALE} articoli in 10 famiglie', '/catalogo/', 'Catalogo'),
]


def novita():
    apertura = sezione(
        intestazione('Novità e avvisi', 'Chiusure, nuovi arrivi e novità dai marchi. Ogni avviso ha una data.'),
        pad=('l', 'lato', 'l', 'lato'))
    avvisi = sezione(
        C(C(T('<p>Orari del banco</p>', style='label', color=m.ROSSO),
            H(ORARI, 'p', style='h3'),
            T(f'<p>{CHIUSURA}. Le chiusure per ferie e festività le pubblichiamo qui, con le date di inizio e di fine.</p>',
              style='body', color=m.NERO_75), gap='s', w=(66, 100, 100)),
          C(B(f'Chiama {TEL}', TEL_LINK, variant='primario'), w=(34, 100, 100), align=('end', 'start', 'start')),
          dir='row', dir_t='column', gap='l', pad='l', border=1, border_color=m.NERO, align=('center', 'start', 'start')),
        pad=('0', 'lato', 'l', 'lato'))
    elenco = sezione(
        C(H('Ultime novità', 'h2'), w=(34, 100, 100)),
        C(ARTICOLI(ARTICOLI_ESEMPIO, numero=6), w=(66, 100, 100)),
        dir='row', dir_t='column', gap='xl', border_top=1, border_color=m.LINEA)
    return [('apertura', apertura), ('avvisi', avvisi), ('elenco', elenco), ('banco', blocco_banco())]


# ---------------------------------------------------------------------------------------------
# CONTATTI
# ---------------------------------------------------------------------------------------------
def contatti():
    def dato(etichetta, html):
        return C(T(f'<p>{etichetta}</p>', style='label', color=m.NERO_75, w_px=(130, 130, None)),
                 T(f'<p>{html}</p>', style='body', color=m.NERO, link_color=m.NERO, grow=True),
                 dir='row', dir_m='column', gap=('m', 'm', 'xs'), pad=('s', '0', 's', '0'), border_top=1,
                 border_color=m.LINEA)
    apertura = sezione(
        intestazione('Contatti', f'Il banco è a Vigonovo, in {INDIRIZZO}, {ZONA.lower()}. Rispondiamo al telefono negli orari '
                                 'di apertura.'),
        pad=('l', 'lato', 'l', 'lato'))
    dati = sezione(
        C(dato('Indirizzo', f'{INDIRIZZO}<br>{CITTA}<br>{ZONA}'),
          dato('Orari', f'{ORARI}<br>{CHIUSURA}'),
          dato('Telefono', f'<a href="{TEL_LINK}">{TEL}</a>'),
          dato('Fax', FAX),
          dato('Email', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
          dato('PEC', PEC),
          dato('Parcheggio', 'Per i clienti, davanti al negozio'),
          C(LINEA_H(m.LINEA)),
          C(B('Apri in Google Maps', MAPS, variant='primario'), B('Scrivi una email', mailto('Richiesta informazioni'),
                                                                   variant='contorno'),
            dir='row', dir_m='column', gap='s', mt=('m', 'm', 's')),
          w=(42, 100, 100), gap='0'),
        C(MAPPA(f'Benvegnù, {INDIRIZZO}, {CITTA}', height=(560, 420, 320), zoom=15), w=(58, 100, 100)),
        dir='row', dir_t='column', gap='xl', pad=('0', 'lato', 'sezione', 'lato'))
    corpo = ('Codice o nome articolo:\nColore, misura o formato:\nQuantità:\nRitiro al banco o spedizione:\n'
             'Ragione sociale e partita IVA:\nTelefono:\n')
    richiesta = sezione(
        C(H('Richiesta di disponibilità', 'h2', color=m.BIANCO),
          T(f'<p>Scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>. Il pulsante apre una email già impostata con le voci che ci '
            'servono.</p>', style='lead', color=m.BIANCO, link_color=m.BIANCO, link_hover=m.NERO),
          C(B('Scrivi la richiesta', mailto('Richiesta disponibilità', corpo), variant='bianco'), mt='xs'),
          w=(50, 50, 100), gap='m'),
        C(T('<p>Cosa indicare</p>', style='label', color=m.BIANCO),
          T('<ul><li>Codice o nome dell’articolo, come nel catalogo</li><li>Colore, misura o formato</li><li>Quantità</li>'
            '<li>Ritiro al banco o spedizione</li><li>Ragione sociale e partita IVA, se ordini come azienda</li></ul>',
            style='body', color=m.BIANCO),
          w=(50, 50, 100), gap='s'),
        bg=m.ROSSO, dir='row', dir_m='column', gap='xl')
    societari = sezione(
        C(H('Dati societari', 'h3'), w=(34, 100, 100)),
        C(T(f'<p>Benvegnù S.r.l.<br>P.IVA e codice fiscale {PIVA}<br>REA {REA}<br>Sede legale: {SEDE_LEGALE}<br>PEC {PEC}</p>',
            style='body', color=m.NERO_75),
          T(f'<p><a href="{CONDIZIONI_PDF}">Condizioni generali di vendita (PDF)</a></p>', style='body', color=m.NERO,
            link_color=m.NERO), w=(66, 100, 100), gap='s'),
        dir='row', dir_t='column', gap='l', pad=('l', 'lato', 'l', 'lato'))
    return [('apertura', apertura), ('dati-mappa', dati), ('richiesta', richiesta), ('dati-societari', societari)]


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
     'descrizione': f'{INDIRIZZO}, {CITTA}. {ORARI}. Tel. {TEL}.'},
]
