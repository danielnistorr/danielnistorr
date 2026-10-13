# -*- coding: utf-8 -*-
"""
Contenuti del sito Zoccarato Serramenti S.n.c. di Zoccarato Sante & Maurizio, Borgoricco (PD).

Idea (specifica _prova/spec.md, paragrafo 3): il sito è la fiancata del camion Zoccarato. Un campo blu flotta con la scritta
che dice chi sono e da dove partono, e accanto il lavoro vero, in foto, con il nome del pezzo. Ogni pagina apre con la sua
fiancata, dentro il campo c'è sempre un dato da camion (sedi, indice delle lavorazioni, telefono), ogni pagina chiude con la
scheda del sopralluogo.

Fonti dei testi: sito attuale (01-analisi-sito-attuale.md, testi verbatim corretti), Registro Imprese e banche dati
pubbliche citate in 01, foto delle gallerie del sito attuale (descritte in _prova/inventario-immagini.json).
Tutto ciò che non è verificato è segnato [DA CONFERMARE] nei commenti e nel paragrafo 18 della specifica.
"""
import html as _html
import re
from urllib.parse import quote

import motore as m
from motore import C, H, T, B, I, RAW, SHORTCODE

PREFISSO = 'zcs'
NOME_SITO = 'Zoccarato Serramenti'

# ---------------------------------------------------------------------------------------------
# Tema (specifica 4.1-4.5)
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'
BLU = '#006BAC'            # blu flotta: logo, camion, foglio di stile del sito attuale
BLU_SCURO = '#00527F'      # solo hover e focus di link e bottone pieno
INCHIOSTRO = '#13222F'     # testo e titoli, barra del furto
TESTO2 = '#4A5866'         # frasi delle schede, conteggi, didascalie, aiuti, piede (7,29:1 su bianco)
SU_SCURO = '#C9D2D8'       # testo secondario sulla barra inchiostro
ALLUMINIO = '#EDF1F3'      # fascia azienda, chiusura comune, hover delle tendine
FILETTO = '#C9D2D8'        # bordo sotto la testata, miniature, tendine, piede
CAMPO = '#6F808D'          # bordi dei campi del modulo, bottone disabilitato
ERRORE = '#B42318'         # messaggi d'errore del modulo

LARGO = 'Encode Sans Expanded'
NORMALE = 'Encode Sans'
F_LARGO = f"'{LARGO}',Arial,sans-serif"
F_NORMALE = f"'{NORMALE}',Arial,sans-serif"


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


# scala tipografica (specifica 4.2): px a 1440 / 1024 / 390; spaziatura in px calcolata sulla misura desktop,
# riportata in em dalle classi zcs-ls* nel CSS del sito
STILI = {
    'display':    _st(LARGO, '600', (64, 44, 35), 1.02, -1.28),
    'h1':         _st(LARGO, '600', (52, 42, 32), 1.04, -1.04),
    'scritta':    _st(LARGO, '600', (15, 15, 13), 1.2, 2.1, True),
    'h2':         _st(LARGO, '600', (40, 32, 26), 1.08, -0.6),
    'h2m':        _st(LARGO, '600', (32, 28, 24), 1.1, -0.48),
    'h2s':        _st(LARGO, '600', (28, 26, 22), 1.12, -0.28),
    'h3':         _st(NORMALE, '600', (21, 20, 19), 1.25),
    'h3s':        _st(NORMALE, '600', (18, 18, 18), 1.3),
    'h3l':        _st(LARGO, '600', (22, 22, 20), 1.2, -0.22),
    'lead':       _st(NORMALE, '400', (20, 18, 17), 1.5),
    'body':       _st(NORMALE, '400', (18, 17, 17), 1.55),
    'piccolo':    _st(NORMALE, '400', (16, 16, 15), 1.45),
    'piccolo_b':  _st(NORMALE, '600', (16, 16, 15), 1.35),
    'nota':       _st(NORMALE, '400', (15, 15, 14), 1.4),
    'nota_b':     _st(NORMALE, '600', (15, 15, 14), 1.4),
    'barra':      _st(NORMALE, '400', (14, 14, 14), 1.25),
    'piede':      _st(NORMALE, '400', (15, 15, 15), 1.55),
    'sede':       _st(NORMALE, '400', (17, 17, 17), 1.55),
    'nav':        _st(NORMALE, '600', (16, 17, 17), 1.2),
    'btn':        _st(NORMALE, '600', (17, 17, 17), 1.2),
    'fatti':      _st(LARGO, '600', (18, 16, 16), 1.3),
    'tel':        _st(LARGO, '600', (18, 16, 15), 1.2),
    'tel_grande': _st(LARGO, '600', (44, 38, 32), 1.1, -0.66),
    'passo_n':    _st(LARGO, '600', (16, 16, 16), 1.35),
}

# una sola scala di spaziature (specifica 4.4): 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 72, 96
SPAZI = {
    'xxs': (4, 4, 4), 'xs': (8, 8, 8), 's': (12, 12, 12), 'm': (16, 16, 16), 'ml': (20, 16, 12), 'l': (24, 24, 24),
    'xl': (32, 32, 24), 'xxl': (40, 32, 24), 'xxxl': (48, 40, 24), 'campo': (56, 48, 32), 'sezione': (96, 72, 56),
    'lato': (40, 32, 16), '0': (0, 0, 0),
}

TEMA = {
    'nome': 'Fiancata',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': INCHIOSTRO, 'testo2': TESTO2, 'accento': BLU,
    'filetto': FILETTO, 'filetto_scuro': INCHIOSTRO, 'su_scuro2': SU_SCURO,
    'scuro': INCHIOSTRO, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': LARGO, 'font_testo': NORMALE, 'larghezza': 1360,
    'google_fonts': ('https://fonts.googleapis.com/css2?family=Encode+Sans+Expanded:wght@600'
                     '&family=Encode+Sans:wght@400;600&display=swap'),
    'stili': STILI,
    'spazi': SPAZI,
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): il colore cambia pieno, mai opacità
    'bottoni': {
        'pieno': (BIANCO, BLU, BLU, BIANCO, BLU_SCURO, BLU_SCURO),
        'bianco': (BLU, BIANCO, BIANCO, BIANCO, INCHIOSTRO, INCHIOSTRO),   # solo sul campo blu
    },
    'bottone': {'raggio': 2, 'pad': (16, 24, 16, 24), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = ('https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/'
                    'ZoccaratoSerramenti-Sito/assets/web/')
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati aziendali (01, "Dati aziendali"): un solo posto da aggiornare
# ---------------------------------------------------------------------------------------------
NB = ' '                                  # spazio indivisibile
WJ = '⁠'                                  # word joiner: niente a capo dentro un trattino
TEL = f'049{NB}579{NB}81{NB}94'
TEL_LINK = 'tel:+390495798194'
FAX = f'049{NB}933{NB}55{NB}88'
EMAIL = 'info@zoccaratoserramenti.it'
PEC = 'zoccaratoserramenti@pec.it'              # [DA CONFERMARE su INI-PEC con la P.IVA prima di pubblicare]
RAGIONE = 'Zoccarato Serramenti S.n.c. di Zoccarato Sante &amp; Maurizio'
PIVA = '01298510288'
REA = f'PD{WJ}-{WJ}239515'
SDI = 'J6URRTW'
SEDE_VIA = "Via dell'Industria 18"
SEDE_CITTA = f'35010 Borgoricco{NB}(PD)'
UL_VIA = 'Via Sandro Pertini 1'
UL_CITTA = f'21020 Brebbia{NB}(VA)'
MAPS_SEDE = 'https://www.google.com/maps/search/?api=1&query=Via+dell%27Industria+18+Borgoricco+PD'
MAPS_UL = 'https://www.google.com/maps/search/?api=1&query=Via+Sandro+Pertini+1+Brebbia+VA'
CF7_SOPRALLUOGO = '[contact-form-7 title="Sopralluogo e preventivo"]'


_TAGS = re.compile(r'(<[^>]+>)')


def diritti(nodo):
    """Apostrofi diritti anche in WordPress: il widget Testo di Elementor passa per wptexturize, che li fa curvi;
    l'entità &#39; resta com'è (provato su questa versione). Vale per i testi, non per titoli e attributi."""
    if nodo.kind == 'text':
        nodo.p['html'] = ''.join(x if x.startswith('<') else x.replace("'", '&#39;') for x in _TAGS.split(nodo.p['html']))
    for figlio in nodo.children:
        diritti(figlio)
    return nodo


def num(testo):
    """Numeri di telefono, misure, codici: cifre tabellari e niente a capo."""
    return f'<span class="zcs-num">{testo}</span>'


def tel_link(testo=TEL, cls='zcs-num'):
    return f'<a class="{cls}" href="{TEL_LINK}">{testo}</a>'


# ---------------------------------------------------------------------------------------------
# Le dieci lavorazioni e le gallerie dei lavori finiti (specifica 7, 16.2): una sola struttura dati.
# I conteggi di home, pagine e Lavori escono da GALLERIE, così non possono divergere.
# ---------------------------------------------------------------------------------------------
# voce di GALLERIE: (nome breve della foto, orientamento O/V, didascalia col nome del pezzo, alt se la didascalia non basta)
# nome breve = parte del file originale dopo "privati-" o "industria-" (es. abitazioni-106); file web g/<nome>.jpg
GALLERIE = {
    'finestre': [
        ('abitazioni-106', 'O', 'Finestre scure a battente sul giardino', None),
        ('abitazioni-107', 'O', 'Finestre effetto legno chiaro', None),
        ('abitazioni-108', 'O', "Veranda d'angolo con serramenti ad arco", None),
        ('abitazioni-109', 'O', 'Villa con bovindo vetrato', None),
        ('abitazioni-110', 'O', 'Veranda vetrata sotto la struttura in legno', None),
        ('abitazioni-111', 'O', 'Veranda con timpano in legno e vetrate effetto legno', None),
        ('abitazioni-101', 'O', 'Finestre ad arco ribassato effetto legno', None),
        ('abitazioni-103', 'O', 'Finestra ad arco bianca, aperta a ribalta', None),
        ('abitazioni-104', 'O', 'Serramento sotto falda in mansarda', None),
        ('abitazioni-1', 'O', 'Vasistas aperto sulle colline', None),
        ('abitazioni-116', 'O', 'Vetrata a tutta altezza con parapetto in vetro', None),
        ('abitazioni-117', 'O', 'Vetrate a doppia altezza', None),
        ('abitazioni-118', 'O', 'Villa con vetrate sulla piscina', None),
        ('abitazioni-119', 'O', 'Vetrate a doppia altezza sulla piscina', None),
        ('abitazioni-120', 'O', 'Facciata con serramenti e pannelli scuri', None),
        ('abitazioni-114', 'O', 'Portafinestra bianca tra persiane nere', None),
        ('abitazioni-2', 'O', 'Finestre bianche con inglesine in cucina', None),
        ('abitazioni-20a', 'O', 'Timpano vetrato sotto il tetto in legno', None),
        ('abitazioni-29', 'O', 'Veranda circolare vetrata', None),
        ('abitazioni-30', 'O', 'Veranda curva con vetrate curve', None),
        ('abitazioni-4', 'O', 'Soggiorno con finestre a nastro', None),
        ('abitazioni-8', 'O', 'Veranda sotto il tetto in legno a falda', None),
        ('abitazioni-9', 'O', 'Casa con timpano vetrato', None),
        ('abitazioni-122', 'V', 'Ingresso con porta vetrata', None),
        ('abitazioni-123', 'V', 'Portafinestra con anta scura', None),
        ('abitazioni-124', 'V', 'Finestra a due ante effetto legno', None),
        ('abitazioni-126', 'V', 'Finestra scura a ribalta', None),
        ('abitazioni-127', 'V', 'Portafinestra nera sul terrazzo', None),
        ('abitazioni-128', 'V', 'Portafinestra effetto legno con inglesine', None),
        ('abitazioni-129', 'V', 'Portafinestra bianca con inglesine', None),
        ('abitazioni-131', 'V', 'Vetrata con corrimano', None),
        ('abitazioni-132', 'V', 'Facciata continua vetrata', None),
        ('abitazioni-133', 'V', 'Vetrata a doppia altezza in soggiorno', None),
        ('abitazioni-15', 'V', 'Portafinestra effetto legno con persiane', None),
        ('abitazioni-20', 'V', 'Ingresso con lunetta ad arco', None),
    ],
    'scorrevoli': [
        ('scorrevoli-101', 'O', 'Scorrevole effetto legno con le veneziane nel vetro', None),
        ('scorrevoli-102', 'O', 'Vetrata scorrevole scura sul giardino', None),
        ('scorrevoli-103', 'O', 'Scorrevole bianco', None),
        ('scorrevoli-104', 'O', 'Scorrevole bianco sul cortile', None),
        ('scorrevoli-105', 'O', 'Lo stesso scorrevole, aperto', "Scorrevole bianco sul cortile, con l'anta aperta"),
        ('scorrevoli-106', 'O', 'Scorrevole scuro con le tende nel vetro', None),
        ('scorrevoli-108', 'O', 'Veranda vetrata sotto il portico in legno', None),
        ('scorrevoli-111', 'O', 'Veranda con scorrevoli e persiane effetto legno', None),
        ('scorrevoli-112', 'O', 'Scorrevole effetto legno con le veneziane, sul giardino', None),
        ('scorrevoli-7', 'O', 'Finestra scorrevole sopra il lavello', None),
        ('abitazioni-112', 'O', 'Scorrevole effetto legno sotto il porticato', None),
        ('abitazioni-113', 'O', "Lo stesso scorrevole, con l'anta aperta",
         "Scorrevole effetto legno sotto il porticato, con l'anta aperta"),
        ('abitazioni-5', 'O', 'Veranda con scorrevoli effetto legno sotto il portico', None),
        ('abitazioni-19b', 'O', 'Terrazzo coperto con vetrate scorrevoli grigie', None),
        ('scorrevoli-113', 'V', 'Scorrevole scuro aperto sulla terrazza', None),
        ('scorrevoli-114', 'V', 'Veranda con scorrevoli color bronzo', None),
        ('scorrevoli-115', 'V', 'Scorrevole color bronzo, i binari', None),
        ('scorrevoli-116', 'V', 'Scorrevole scuro con le tende nel vetro, da vicino', None),
        ('scorrevoli-118', 'V', "Scorrevole grigio, d'inverno", None),
        ('scorrevoli-120', 'V', 'Scorrevole sul balcone', None),
    ],
    'oscuranti': [
        ('oscuranti-101', 'O', 'Persiane scure su facciata rosa', None),
        ('oscuranti-102', 'O', 'Persiane scure e portafinestra', None),
        ('oscuranti-104', 'O', 'Persiana grigia con lamelle orientabili', None),
        ('oscuranti-106', 'O', 'Persiane scorrevoli grigie', None),
        ('oscuranti-107', 'O', 'Casa con persiane rosse', None),
        ('oscuranti-108', 'O', 'Balcone con persiane rosse', None),
        ('oscuranti-17', 'O', 'Casa gialla con persiane effetto legno', None),
        ('oscuranti-18', 'O', 'Villetta con persiane arancio', None),
        ('oscuranti-19a', 'O', 'Avvolgibili color legno', None),
        ('oscuranti-41', 'O', 'Finestra con scuri aperti', None),
        ('abitazioni-41b', 'O', 'Scuri effetto legno socchiusi', None),
        ('abitazioni-115', 'O', 'Facciata con persiane grigie', None),
        ('oscuranti-03', 'V', 'Portafinestra con scuri effetto legno', None),
        ('oscuranti-110', 'V', 'Persiana grigio azzurra a due ante', None),
        ('oscuranti-112', 'V', 'Persiana grigia', None),
        ('oscuranti-113', 'V', 'Persiane scorrevoli lungo la facciata', None),
        ('oscuranti-31', 'V', 'Persiana a libro effetto legno', None),
        ('oscuranti-52', 'V', 'Persiana a libro effetto legno, altra vista', None),
    ],
    'portoncini': [
        ('portoncini-10', 'V', 'Portoncino ad arco bordeaux con vetro decorato', None),
        ('portoncini-16', 'V', 'Portoncino pannellato con battiporta e laterale vetrato', None),
        ('portoncini-42', 'V', 'Portoncino a spina di pesce con laterale vetrato', None),
    ],
    'porte-interne': [
        ('porte-interne-33', 'O', 'Porte scure con vetro satinato', None),
        ('abitazioni-130', 'V', 'Bussola con porte effetto legno e vetro', None),
        ('porte-interne-101', 'V', 'Porta a due ante vetrata con fasce satinate', None),
        ('porte-interne-102', 'V', 'La stessa porta, altra vista', 'Porta a due ante vetrata con fasce satinate, altra vista'),
        ('porte-interne-107', 'V', 'Porta bianca con chiudiporta', None),
        ('porte-interne-32', 'V', 'Porta bianca del bagno', None),
    ],
    'pergole': [
        ('pensiline-101', 'O', 'Pergola sulla terrazza', None),
        ('pensiline-102', 'O', "Pergola effetto legno con l'edera", None),
        ('pensiline-103', 'O', 'Pergola effetto legno sul muro in pietra', None),
        ('pensiline-104', 'O', 'La stessa pergola, altra vista', 'Pergola effetto legno sul muro in pietra, altra vista'),
        ('pensiline-14', 'O', 'Pergola effetto legno tra le piante', None),
        ('pensiline-14a', 'O', 'Pergola in alluminio scuro sulla terrazza', None),
        ('pensiline-14b', 'O', 'Pergola grigia sul terrazzo', None),
        ('pensiline-14c', 'O', 'Tettoia in giardino', None),
        ('pensiline-14g', 'O', 'Copertura a lamelle sul tetto', None),
    ],
    'speciali': [
        ('speciali-101', 'O', 'Lucernario', None),
        ('speciali-102', 'O', 'Parapetto inox a cavi sulla terrazza', None),
        ('speciali-103', 'O', 'Parapetto inox a cavi tra gli alberi', None),
        ('speciali-104', 'O', 'Copertura vetrata apribile sulla scala, chiusa', None),
        ('speciali-105', 'O', 'La stessa copertura, aperta', 'Copertura vetrata apribile sulla scala, aperta'),
        ('speciali-108', 'O', 'Cancello in lamiera stirata', None),
        ('speciali-13a', 'O', 'Cancello in lamiera bugnata', None),
        ('speciali-28', 'O', 'Parapetto inox sulla terrazza', None),
    ],
    'commerciali': [
        ('commerciali-101', 'O', 'Uffici con finestre a nastro', None),
        ('commerciali-102', 'O', 'La stessa facciata gialla, dal basso', 'Uffici con finestre a nastro e facciata gialla, dal basso'),
        ('commerciali-103', 'O', 'Finestre a nastro, altra facciata', None),
        ('commerciali-104', 'O', 'Corridoio degli uffici', None),
        ('commerciali-105', 'O', 'Corridoio vetrato', None),
        ('commerciali-106', 'O', 'Corridoio vetrato al piano', None),
        ('commerciali-107', 'O', 'Cortile con finestre grigie', None),
        ('commerciali-108', 'O', 'Punto vendita sotto la pensilina ad arco', None),
        ('commerciali-110', 'O', 'Punto vendita di una stazione di servizio', None),
        ('commerciali-111', 'O', 'Fronte in mattoni con porta vetrata', None),
        ('commerciali-112', 'O', 'Vetrina a griglia bianca', None),
        ('commerciali-113', 'O', 'Vetrina a griglia con la porta aperta', None),
        ('commerciali-114', 'O', 'Box vetrato sotto la pensilina', None),
        ('commerciali-21', 'O', 'Punto vendita, il fronte', 'Punto vendita di una stazione di servizio, il fronte'),
        ('commerciali-22', 'O', 'Ingresso vetrato del punto vendita', None),
        ('commerciali-22a', 'O', 'Edificio con serramenti effetto legno e inglesine', None),
        ('commerciali-22b', 'O', 'Facciata con timpano, porte e finestre effetto legno', None),
        ('commerciali-24', 'O', 'Edificio commerciale con finestre', None),
        ('speciali-107', 'O', 'Chiosco con la porta rossa', None),
        ('commerciali-115', 'V', 'Cabina vetrata in un negozio', None),
        ('commerciali-116', 'V', 'Vetrata di un bar', None),
        ('commerciali-117', 'V', "Vetrata d'ingresso sul parcheggio", None),
        ('commerciali-118', 'V', 'Chiosco bianco e rosso sotto la pensilina', None),
        ('commerciali-120', 'V', 'Cabina vetrata, da dentro', None),
    ],
    'pensiline': [
        ('commerciali-109', 'O', 'Pensilina ad arco di una stazione di servizio', None),
        ('pensiline-14d', 'O', 'Pensilina ad arco davanti a un ingresso', None),
        ('pensiline-14f', 'O', 'Struttura ad archi rossi', None),
    ],
    'monoblocchi': [
        ('monoblocchi-38', 'O', 'Monoblocco bianco e rosso', None),
        ('monoblocchi-34', 'O', 'Monoblocco verde lungo una recinzione', None),
        ('monoblocchi-35', 'O', 'Monoblocco aperto: il vano tecnico con i serbatoi', None),
    ],
}


def n_foto(ancora):
    """Numero di foto mostrate nella galleria di una lavorazione (pagina Lavori)."""
    return len(GALLERIE[ancora])


TOTALE_FOTO = sum(len(v) for v in GALLERIE.values())          # 129

# Le dieci lavorazioni nell'ordine del menu: ancora, nome, gruppo, sottotipi della tendina (prototipo, righe 378-393),
# foto e testi della scheda in home (specifica H2, H3; frase breve per le schede strette, None = la stessa).
LAVORAZIONI = [
    dict(ancora='finestre', nome='Finestre e portefinestre', gruppo='casa',
         sotto='vasistas, anta ribalta, bovindi, timpani vetrati',
         foto='casa-finestre.jpg', o='O', alt="Due finestre scure a battente aperte su un giardino, viste dall'interno",
         frase='A battente, a vasistas e a ribalta, con inglesine o effetto legno; verande, bovindi e timpani vetrati.',
         breve=None),
    dict(ancora='scorrevoli', nome='Scorrevoli e alzanti', gruppo='casa',
         sotto='effetto legno, con le veneziane nel vetro',
         foto='casa-scorrevoli.jpg', o='O', alt='Scorrevole effetto legno con le veneziane nel vetro',
         frase='Infissi scorrevoli e alzanti, anche effetto legno e con le veneziane nel vetro.',
         breve='Effetto legno, veneziane nel vetro.'),
    dict(ancora='oscuranti', nome='Sistemi oscuranti', gruppo='casa',
         sotto='persiane a battente, a libro e scorrevoli, scuri, avvolgibili',
         foto='casa-oscuranti.jpg', o='O', alt='Facciata con persiane grigie e balcone con parapetto in acciaio',
         frase='Persiane a battente, a libro e scorrevoli, scuri e avvolgibili.',
         breve='Persiane, scuri, avvolgibili.'),
    dict(ancora='portoncini', nome="Portoncini d'ingresso", gruppo='casa',
         sotto='pannellati, a spina di pesce, con vetri, ad arco',
         foto='casa-portoncini.jpg', o='V', alt='Portoncino ad arco bordeaux con vetro decorato',
         frase='Pannellati, a spina di pesce o con vetri, anche ad arco e con laterale vetrato.',
         breve='Pannellati, con vetri, ad arco.'),
    dict(ancora='porte-interne', nome='Porte interne', gruppo='casa',
         sotto='porte e bussole, vetrate o cieche',
         foto='casa-porte-interne.jpg', o='V', alt='Bussola interna con porte effetto legno e vetro',
         frase='Porte e bussole, vetrate o cieche, anche effetto legno.',
         breve='Porte e bussole, anche vetrate.'),
    dict(ancora='pergole', nome='Pergole e pensiline', gruppo='casa',
         sotto='pergole per terrazze, tettoie, coperture a lamelle',
         foto='casa-pergole.jpg', o='V', alt='Pergola in alluminio scuro su una terrazza affacciata sul lago',
         frase='Pergole per terrazze, tettoie e coperture a lamelle, anche effetto legno.',
         breve='Pergole, tettoie, lamelle.'),
    dict(ancora='speciali', nome='Speciali residenziali', gruppo='casa',
         sotto='parapetti inox a cavi, cancelli, coperture vetrate',
         foto='casa-speciali.jpg', o='V', alt='Terrazza con parapetto in acciaio inox a cavi',
         frase='Parapetti inox a cavi, cancelli in lamiera, coperture vetrate apribili e lucernari.',
         breve='Parapetti inox, cancelli, lucernari.'),
    dict(ancora='commerciali', nome='Commerciali e industriali', gruppo='aziende',
         sotto='finestre a nastro, vetrine, box e chioschi',
         foto='ind-commerciali.jpg', o='O', alt='Edificio per uffici con finestre a nastro e facciata gialla',
         frase='Finestre a nastro per uffici, vetrine, ingressi vetrati, box e chioschi.',
         breve=None),
    dict(ancora='pensiline', nome='Pensiline commerciali', gruppo='aziende',
         sotto='pensiline ad arco per stazioni di servizio',
         foto='ind-pensiline.jpg', o='O', alt='Pensilina ad arco di una stazione di servizio sopra il punto vendita',
         frase='Pensiline ad arco per stazioni di servizio e per gli ingressi.',
         breve='Ad arco, per stazioni di servizio.'),
    dict(ancora='monoblocchi', nome='Monoblocchi prefabbricati', gruppo='aziende',
         sotto='box e vani tecnici in pannelli',
         foto='ind-monoblocchi.jpg', o='O', alt='Monoblocco prefabbricato bianco e rosso posato su un prato',
         frase='Box e vani tecnici prefabbricati in pannelli, anche per i serbatoi.',
         breve='Box e vani tecnici in pannelli.'),
]
LAV = {x['ancora']: x for x in LAVORAZIONI}
for _x in LAVORAZIONI:
    _x['pagina'] = '/per-la-casa/' if _x['gruppo'] == 'casa' else '/per-le-aziende/'
    _x['url'] = _x['pagina'] + '#' + _x['ancora']

# le otto voci della scheda del sopralluogo: (valore mostrato e letto da ?lavoro=, valore nella mail, miniatura)
SCELTE = [
    ('Finestre', 'Finestre e portefinestre', 'm-finestre.jpg'),
    ('Scorrevoli', 'Scorrevoli e alzanti', 'm-scorrevoli.jpg'),
    ('Persiane e scuri', 'Persiane, scuri o avvolgibili', 'm-oscuranti.jpg'),
    ('Portoncini e porte', 'Portoncino o porte interne', 'm-portoncini.jpg'),
    ('Pergole', 'Pergola o pensilina', 'm-pergole.jpg'),
    ('Parapetti', 'Parapetto, cancello o copertura vetrata', 'm-speciali.jpg'),
    ('Vetrine e uffici', 'Vetrina, ufficio o negozio', 'm-vetrine.jpg'),
    ('Monoblocchi', 'Pensilina commerciale o monoblocco', 'm-monoblocchi.jpg'),
]


# ---------------------------------------------------------------------------------------------
# CSS del sito: base e componenti condivisi. Sta nel widget HTML della testata, che c'è in ogni pagina (in Elementor con
# Ultimate Addons, nell'anteprima nel blocco della testata). Il CSS di una sola sezione sta nel suo widget HTML.
# Il tema Hello colora link e bottoni di rosa (#c36): ogni selettore ha i suoi colori espliciti.
# ---------------------------------------------------------------------------------------------
SOTT = 'text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important'
CSS_SITO = (
    'body{font-synthesis:none}'
    '.zcs-sr{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;'
    'clip-path:inset(50%)!important;white-space:nowrap!important;margin:0!important;padding:0!important}'
    '.zcs-num{font-variant-numeric:tabular-nums lining-nums;white-space:nowrap}'
    '.zcs-nw{white-space:nowrap}'
    # Elementor: a capo bilanciati nei titoli, niente spazio sotto l'ultimo paragrafo (come nell'anteprima)
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}'
    '.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    '.elementor-widget-image img{display:block}'
    # spaziatura dei titoli in em, uguale a ogni misura (specifica 4.2)
    '.zcs-ls20 .elementor-heading-title,.zcs-ls20.zcs-w{letter-spacing:-0.02em!important}'
    '.zcs-ls15 .elementor-heading-title,.zcs-ls15.zcs-w{letter-spacing:-0.015em!important}'
    '.zcs-ls10 .elementor-heading-title,.zcs-ls10.zcs-w{letter-spacing:-0.01em!important}'
    # fuoco visibile: blu, bianco sul campo blu
    f'a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible,select:focus-visible,'
    f'textarea:focus-visible{{outline:3px solid {BLU};outline-offset:3px}}'
    '.zcs-fiancata a:focus-visible{outline-color:#FFFFFF}'
    '[id]{scroll-margin-top:24px}'
    'html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'
    # link nel testo: blu 600 sottolineato a 4 px; al passaggio blu scuro e sottolineatura di 2 px (specifica 4.5)
    f'.zcs-link a{{color:{BLU}!important;font-weight:600;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:4px!important}'
    f'.zcs-link a:hover,.zcs-link a:focus-visible{{color:{BLU_SCURO}!important;text-decoration-thickness:2px!important}}'
    # "Vai al contenuto": il nostro nell'anteprima, quello di Ultimate Addons in WordPress; visibile solo al fuoco
    '.zcs-salta,a.hfe-skip-link{position:absolute!important;left:-9999px!important;top:0}'
    f'.zcs-salta:focus,a.hfe-skip-link:focus{{left:16px!important;top:8px!important;z-index:100;background:{BIANCO}!important;'
    f'color:{BLU}!important;font:600 16px/1.2 {F_NORMALE}!important;padding:12px 16px!important;text-decoration:none!important;'
    'clip:auto!important;clip-path:none!important;width:auto!important;height:auto!important;box-shadow:none!important}'
    # griglie regolari (schede, passi, piede): colonne uguali a ogni larghezza, nessuna riga che va a capo per pochi px
    '.zcs-griglia{display:grid!important}'
    '.zcs-griglia>*{width:auto!important;max-width:none!important;min-width:0}'
    '.zcs-g3{grid-template-columns:repeat(3,minmax(0,1fr))}'
    '.zcs-g4{grid-template-columns:repeat(4,minmax(0,1fr))}'
    '@media (max-width:767px){.zcs-g3,.zcs-g4{grid-template-columns:repeat(2,minmax(0,1fr))}'
    '.zcs-g3>:first-child{grid-column:1/-1}}'
    # foto nelle loro proporzioni, senza bordi né ombre
    '.zcs-o img,.zcs-v img,.zcs-q img{display:block;width:100%!important;height:auto!important;max-width:100%!important;object-fit:cover}'
    '.zcs-o img{aspect-ratio:4/3}.zcs-v img{aspect-ratio:3/4}.zcs-q img{aspect-ratio:1/1}'
    # schede delle lavorazioni (home): una scheda = un link; conteggio in fondo, stessa linea di base nella riga
    '.zcs-scheda{text-decoration:none!important}'
    '.zcs-conta{margin-top:auto!important;padding-top:8px}'
    '.zcs-breve{display:none}'
    f'.zcs-scheda:hover .elementor-heading-title,.zcs-scheda:hover h3,.zcs-scheda:focus-visible .elementor-heading-title,'
    f'.zcs-scheda:focus-visible h3{{color:{BLU}!important;text-decoration:underline;text-decoration-thickness:2px;'
    'text-underline-offset:4px}'
    f'.zcs-scheda:hover .zcs-conta p,.zcs-scheda:focus-visible .zcs-conta p{{color:{BLU_SCURO}!important;'
    'text-decoration:underline;text-underline-offset:3px}'
    '@media (max-width:1024px){.zcs-g4 .zcs-lungo{display:none}.zcs-g4 .zcs-breve{display:inline}}'
    '@media (max-width:767px){.zcs-scheda .zcs-lungo{display:none}.zcs-scheda .zcs-breve{display:inline}'
    '.zcs-g3>.zcs-scheda:not(:first-child) h3,.zcs-g4>.zcs-scheda h3,'
    '.zcs-g3>.zcs-scheda:not(:first-child) .elementor-heading-title,.zcs-g4>.zcs-scheda .elementor-heading-title'
    '{font-size:17px!important}}'
    # didascalie: il nome del pezzo in 600, sotto la lavorazione
    f'.zcs-didascalia b{{display:block;font-weight:600;color:{INCHIOSTRO}}}'
    # i quattro passi (una procedura vera: numerati)
    '.zcs-passi2{grid-template-columns:repeat(2,minmax(0,1fr))}'
    '.zcs-passi4{grid-template-columns:repeat(4,minmax(0,1fr))}'
    '@media (max-width:1024px){.zcs-passi4{grid-template-columns:repeat(2,minmax(0,1fr))}}'
    '@media (max-width:767px){.zcs-passi2,.zcs-passi4{grid-template-columns:1fr}}'
    # sedi: link senza sottolineatura, sottolineati al passaggio
    f'.zcs-sede-dati a{{color:{BLU}!important;font-weight:600;text-decoration:none!important}}'
    f'.zcs-sede-dati a:hover,.zcs-sede-dati a:focus-visible{{color:{BLU_SCURO}!important;text-decoration:underline!important;'
    'text-underline-offset:4px!important}'
    # telefono grande: un recapito, si sottolinea al passaggio
    '.zcs-tel a{color:inherit!important;text-decoration:none!important;white-space:nowrap}'
    f'.zcs-tel a:hover,.zcs-tel a:focus-visible{{color:{BLU_SCURO}!important;text-decoration:underline!important;'
    'text-decoration-thickness:3px!important;text-underline-offset:6px!important}'
    '.zcs-fiancata .zcs-tel a:hover,.zcs-fiancata .zcs-tel a:focus-visible{color:#FFFFFF!important}'
    # la fiancata (specifica 4.6): campo blu alto quanto il testo, foto vera a filo a destra, mai oltre la sua misura
    '.zcs-fiancata{overflow:hidden}'
    '.zcs-fia-foto{position:relative;max-width:800px;overflow:hidden}'
    '.zcs-fia-foto>.elementor-widget-image,.zcs-fia-foto>.zcs-w{position:absolute!important;inset:0;width:100%!important;'
    'max-width:none!important;height:100%!important;margin:0!important}'
    '.zcs-fia-foto>.elementor-widget-image>*{height:100%}'
    '.zcs-fia-foto img{width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;'
    'object-position:50% 50%}'
    '@media (min-width:1025px){.zcs-fia-testo{padding-left:max(40px,calc((100vw - 1440px)/2 + 40px))!important}}'
    '@media (min-width:1025px) and (max-width:1300px){.zcs-fia-foto{width:50%!important}'
    '.zcs-fia-testo{padding-top:48px!important;padding-right:40px!important;padding-bottom:48px!important}}'
    '@media (max-width:1300px){.zcs-fia-sedi .zcs-sep{display:none}.zcs-fia-sedi .zcs-nw{display:block}}'
    '@media (max-width:767px){.zcs-fia-foto{order:-1;max-width:none;aspect-ratio:16/10;min-height:0!important}}'
    # coppie di foto (orizzontale 4:3 e verticale 3:4 alla stessa altezza): lavori finiti, dopo un furto
    '.zcs-coppia{flex:1 1 0!important;min-width:0}'
    '.zcs-lav{min-width:0}'
    '.zcs-duo>.zcs-o{flex:1.3333 1 0!important}.zcs-duo>.zcs-v{flex:.75 1 0!important}'
    '.zcs-duo>.zcs-q{flex:1 1 0!important}'
    '@media (max-width:767px){.zcs-righe-lav .zcs-coppia{flex:none!important;width:100%!important}}'
    # testo e foto affiancati (dopo un furto)
    '.zcs-furto-testo{flex:1 0 340px!important;min-width:0}'
    '.zcs-furto-foto{flex:0 1 744px!important;min-width:0}'
    '@media (max-width:1024px){.zcs-furto-foto{flex-basis:470px!important}}'
    '@media (max-width:767px){.zcs-furto-testo,.zcs-furto-foto{flex:none!important;width:100%!important}}'
)

# ---------------------------------------------------------------------------------------------
# Testata (specifica 5.1): barra del furto e testata con logo, menu con le tendine e telefono.
# Un widget HTML (le tendine con i sottotipi non si fanno con il widget menu), identico nell'anteprima; il logo è un widget
# Immagine, così entra nella libreria media all'import.
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('Per la casa', '/per-la-casa/'), ('Per le aziende', '/per-le-aziende/'), ('Lavori', '/lavori/'),
             ('Dopo un furto', '/dopo-un-furto/'), ('Chi siamo', '/chi-siamo/'), ('Contatti', '/contatti/')]
TENDINE = {'/per-la-casa/': 'casa', '/per-le-aziende/': 'aziende'}

CSS_TESTATA = (
    '.zcs-box{max-width:1440px;margin:0 auto;padding:0 40px;box-sizing:border-box}'
    f'.zcs-barra{{background:{INCHIOSTRO};color:{BIANCO};font:400 14px/1.25 {F_NORMALE}}}'
    '.zcs-barra p{margin:0}'
    '.zcs-barra-in{display:flex;justify-content:space-between;align-items:center;gap:24px;min-height:32px}'
    f'.zcs-barra a{{color:{BIANCO}!important;font-weight:600;text-decoration:none!important}}'
    f'.zcs-barra a:hover,.zcs-barra a:focus-visible{{color:{BIANCO}!important;text-decoration:underline!important;'
    'text-underline-offset:3px!important}'
    '.zcs-barra a:focus-visible{outline-color:#FFFFFF}'
    f'.zcs-barra-sedi{{color:{SU_SCURO};white-space:nowrap}}'
    # testata: il widget HTML occupa l'altezza della testata, così le tendine partono dal suo bordo
    '.zcs-testata{position:relative;z-index:30;overflow-x:clip}'
    '.zcs-testata .zcs-logo{align-self:center!important}'
    f'.zcs-nav{{display:flex;align-items:stretch;justify-content:flex-end;gap:32px;min-height:84px;font-family:{F_NORMALE}}}'
    '.zcs-nav>*{align-self:center}'
    '.zcs-menu{align-self:stretch;display:flex}'
    '.zcs-menu>ul{display:flex;gap:28px;list-style:none;margin:0;padding:0}'
    '.zcs-menu>ul>li{position:relative;display:flex;align-items:center;margin:0;padding:0}'
    f'.zcs-menu>ul>li>a{{color:{INCHIOSTRO}!important;text-decoration:none!important;font:600 16px/1.2 {F_NORMALE};'
    'white-space:nowrap;padding:8px 0}'
    f'.zcs-menu>ul>li>a:hover,.zcs-menu>ul>li>a:focus-visible,.zcs-voce:focus-within>a,.zcs-menu a[aria-current=page]'
    f'{{color:{BLU}!important;{SOTT}}}'
    f'.zcs-tendina{{display:none;position:absolute;top:100%;left:-24px;width:400px;background:{BIANCO};'
    f'border:1px solid {FILETTO};box-shadow:0 10px 28px rgba(19,34,47,.12);padding:8px 0;z-index:40}}'
    '.zcs-voce:hover .zcs-tendina,.zcs-voce:focus-within .zcs-tendina{display:block}'
    '.zcs-tendina ul{list-style:none;margin:0;padding:0}.zcs-tendina li{margin:0;padding:0}'
    f'.zcs-tendina a{{display:block;padding:8px 24px;text-decoration:none!important;color:{INCHIOSTRO}!important}}'
    f'.zcs-tendina b{{display:block;font:600 16px/1.3 {F_NORMALE}}}'
    f'.zcs-tendina span{{display:block;margin-top:4px;font:400 14px/1.4 {F_NORMALE};color:{TESTO2}}}'
    f'.zcs-tendina a:hover,.zcs-tendina a:focus-visible{{background:{ALLUMINIO}}}'
    f'.zcs-tendina a:hover b,.zcs-tendina a:focus-visible b{{color:{BLU}}}'
    '.zcs-tendina a:focus-visible{outline-offset:-3px}'
    f'.zcs-tel-testata{{font:600 18px/1.2 {F_LARGO};color:{BLU}!important;text-decoration:none!important;white-space:nowrap}}'
    f'.zcs-tel-testata:hover,.zcs-tel-testata:focus-visible{{color:{BLU_SCURO}!important;text-decoration:underline!important;'
    'text-underline-offset:4px!important}'
    '.zcs-menu-m{display:none;position:relative}'
    # da 1025 a 1199: logo 170, voci più strette, "Tel." nascosto alla vista
    '@media (max-width:1199px) and (min-width:1025px){.zcs-menu>ul{gap:20px}.zcs-nav{gap:24px}'
    '.zcs-testata .zcs-logo img{width:170px!important}'
    '.zcs-tel-pre{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}}'
    # fino a 1024: bottone "Menu" con il pannello; il telefono resta a vista
    '@media (max-width:1024px){'
    '.zcs-box{padding:0 32px}'
    '.zcs-barra-sedi .zcs-via{display:none}'
    '.zcs-menu{display:none}'
    '.zcs-nav{min-height:76px;gap:24px}'
    '.zcs-tel-testata{font-size:16px}'
    '.zcs-menu-m{display:block}'
    f'.zcs-menu-m>summary{{list-style:none;cursor:pointer;font:600 15px/1 {F_NORMALE};color:{INCHIOSTRO};background:{BIANCO};'
    f'border:1px solid {CAMPO};border-radius:2px;padding:8px 12px}}'
    '.zcs-menu-m>summary::-webkit-details-marker{display:none}'
    f'.zcs-menu-m>summary:hover{{border-color:{INCHIOSTRO}}}'
    f'.zcs-menu-m[open]>summary{{background:{INCHIOSTRO};color:{BIANCO};border-color:{INCHIOSTRO}}}'
    f'.zcs-menu-m>nav{{position:absolute;right:0;top:calc(100% + 12px);width:min(320px,calc(100vw - 32px));'
    f'max-height:calc(100vh - 120px);overflow-y:auto;background:{BIANCO};border:1px solid {FILETTO};'
    'box-shadow:0 10px 28px rgba(19,34,47,.12);display:flex;flex-direction:column;padding:8px 0;z-index:40}'
    f'.zcs-menu-m nav a,.zcs-menu-m .zcs-sotto>summary{{color:{INCHIOSTRO}!important;text-decoration:none!important;'
    f'font:600 17px/1.3 {F_NORMALE};padding:12px 16px}}'
    '.zcs-menu-m nav>a{display:block}'
    '.zcs-menu-m .zcs-sotto>summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:12px}'
    '.zcs-menu-m .zcs-sotto>summary::-webkit-details-marker{display:none}'
    f'.zcs-menu-m .zcs-sotto>summary::after{{content:"+";font-weight:600;color:{BLU}}}'
    '.zcs-menu-m .zcs-sotto[open]>summary::after{content:"\\2212"}'
    '.zcs-menu-m .zcs-sotto ul{list-style:none;margin:0 0 8px;padding:0}.zcs-menu-m .zcs-sotto li{margin:0;padding:0}'
    '.zcs-menu-m .zcs-sotto a{display:block;font-weight:400;font-size:16px;padding:8px 16px 8px 32px}'
    f'.zcs-menu-m nav a:hover,.zcs-menu-m nav a:focus-visible,.zcs-menu-m .zcs-sotto>summary:hover{{color:{BLU}!important;'
    f'background:{ALLUMINIO}}}'
    f'.zcs-menu-m nav a[aria-current=page]{{color:{BLU}!important;{SOTT}}}'
    '.zcs-menu-m nav a:focus-visible,.zcs-menu-m summary:focus-visible{outline-offset:-3px}'
    '}'
    '@media (max-width:767px){.zcs-box{padding:0 16px}.zcs-barra-sedi{display:none}.zcs-barra-in{justify-content:flex-start}'
    '.zcs-nav{min-height:64px;gap:12px}.zcs-tel-testata{font-size:15px}'
    '.zcs-tel-pre{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}}'
)

# voce attiva (aria-current) sulla voce il cui percorso è l'inizio dell'indirizzo; la home non accende nessuna voce.
# Il "Vai al contenuto" dell'anteprima si toglie se Ultimate Addons ha già il suo.
JS_TESTATA = (
    "(function(){function via(){var qui=location.pathname;"
    "if(document.querySelector('.hfe-skip-link')){document.querySelectorAll('.zcs-salta').forEach(function(s){s.remove()})}"
    "document.querySelectorAll('.zcs-menu>ul>li>a,.zcs-menu-m nav>a,.zcs-menu-m .zcs-sotto>a').forEach(function(a){"
    "var p=a.getAttribute('data-percorso');if(p&&p!=='/'&&qui.indexOf(p)===0)a.setAttribute('aria-current','page')})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',via)}else{via()}})();"
)


def _tendina(gruppo):
    return ''.join(f'<li><a href="{x["url"]}"><b>{x["nome"]}</b><span>{x["sotto"]}</span></a></li>'
                   for x in LAVORAZIONI if x['gruppo'] == gruppo)


def nav_html():
    voci, voci_m = [], []
    for nome, url in VOCI_MENU:
        if url in TENDINE:
            g = TENDINE[url]
            voci.append(f'<li class="zcs-voce"><a href="{url}" data-percorso="{url}">{nome}</a>'
                        f'<div class="zcs-tendina"><ul>{_tendina(g)}</ul></div></li>')
            sotto = ''.join(f'<li><a href="{x["url"]}">{x["nome"]}</a></li>' for x in LAVORAZIONI if x['gruppo'] == g)
            voci_m.append(f'<details class="zcs-sotto"><summary>{nome}</summary><ul>'
                          f'<li><a href="{url}" data-percorso="{url}">Tutte le lavorazioni</a></li>{sotto}</ul></details>')
        else:
            voci.append(f'<li><a href="{url}" data-percorso="{url}">{nome}</a></li>')
            voci_m.append(f'<a href="{url}" data-percorso="{url}">{nome}</a>')
    return (
        '<div class="zcs-nav">'
        f'<nav class="zcs-menu" aria-label="Menu principale"><ul>{"".join(voci)}</ul></nav>'
        f'<a class="zcs-tel-testata" href="{TEL_LINK}"><span class="zcs-tel-pre">Tel. </span>{TEL}</a>'
        f'<details class="zcs-menu-m"><summary>Menu</summary><nav aria-label="Menu principale">{"".join(voci_m)}</nav></details>'
        f'</div><script>{JS_TESTATA}</script>'
    )


def barra_html():
    return (
        '<a class="zcs-salta" href="#content">Vai al contenuto</a>'
        '<div class="zcs-barra"><div class="zcs-box zcs-barra-in">'
        f'<p>Furto o effrazione? Chiamate il {tel_link()}</p>'
        f'<p class="zcs-barra-sedi">Borgoricco{NB}(PD)<span class="zcs-via">, via dell\'Industria{NB}18</span> · '
        f'Brebbia{NB}(VA)<span class="zcs-via">, via Sandro Pertini{NB}1</span></p>'
        '</div></div>'
    )


def header():
    logo = I(img('logo.jpg'), 'Zoccarato serramenti, dal 1974', link='/', link_label='Zoccarato Serramenti, pagina iniziale',
             w_img=(200, 170, 132), fisso=True, css='zcs-logo')
    testata = C(logo, RAW(nav_html(), grow=True), dir='row', justify='between', align='center', gap=(32, 24, 12),
                pad=(0, 'lato'), bg=BIANCO, border_bottom=1, border_color=FILETTO, boxed=True, css='zcs-testata')
    # niente tag header: Ultimate Addons avvolge già la testata in <header id="masthead">
    return diritti(C(RAW(barra_html(), css=CSS_SITO + CSS_TESTATA), testata, pad='0', gap='0', boxed=False, bg=BIANCO))


# ---------------------------------------------------------------------------------------------
# Piede (specifica 5.2): widget normali
# ---------------------------------------------------------------------------------------------
CSS_PIEDE = (
    '.zcs-piede-griglia{grid-template-columns:1.3fr 1fr 1fr 1.2fr 1fr}'
    f'.zcs-piede b{{display:block;color:{INCHIOSTRO};font-weight:600;margin-bottom:4px}}'
    f'.zcs-piede a{{color:{TESTO2}!important;text-decoration:underline!important;text-decoration-thickness:1px!important;'
    'text-underline-offset:3px!important}'
    f'.zcs-piede a:hover,.zcs-piede a:focus-visible{{color:{BLU}!important;text-decoration-thickness:2px!important}}'
    '@media (max-width:1200px){.zcs-piede-griglia{grid-template-columns:repeat(4,minmax(0,1fr))}'
    '.zcs-piede-griglia>:first-child{grid-column:1/-1}}'
    '@media (max-width:767px){.zcs-piede-griglia{grid-template-columns:1fr}}'
)


def _piede(html, **p):
    return T(html, style='piede', color=TESTO2, link_color=TESTO2, link_hover=BLU, **p)


def footer():
    marchio = C(I(img('logo.jpg'), 'Zoccarato serramenti, dal 1974', link='/', link_label='Zoccarato Serramenti, pagina iniziale',
                  w_img=(160, 160, 160), fisso=True),
                _piede(f'<p>{RAGIONE}</p>', mt='s', max_w=(300, 600, None)), gap='0', w=(25, 100, 100))
    colonne = C(
        marchio,
        _piede(f'<p><b>Sede</b>{SEDE_VIA}<br>{SEDE_CITTA}</p>', w=(16, 23, 100)),
        _piede(f'<p><b>Unità locale</b>{UL_VIA}<br>{UL_CITTA}</p>', w=(16, 23, 100)),
        _piede(f'<p><b>Contatti</b>Tel. {tel_link()}<br>Fax {num(FAX)}<br><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
               f'PEC {PEC}</p>', w=(22, 23, 100)),
        _piede(f'<p><b>Dati societari</b>P.IVA e C.F. {num(PIVA)}<br>REA {num(REA)}<br>Codice SDI {SDI}</p>', w=(16, 23, 100)),
        dir='row', dir_m='column', wrap=True, gap=(32, 32, 20), gap_r=(32, 32, 20), css='zcs-griglia zcs-piede-griglia')
    legale = C(
        T('<p>© 2026 Zoccarato Serramenti S.n.c.</p>', style='barra', color=TESTO2, fisso=True),
        T('<p><a href="/privacy/">Privacy</a></p>', style='barra', color=TESTO2, link_color=TESTO2, link_hover=BLU, fisso=True),
        T('<p><a href="/cookie/">Cookie</a></p>', style='barra', color=TESTO2, link_color=TESTO2, link_hover=BLU, fisso=True),
        dir='row', dir_m='column', wrap=True, gap=(24, 24, 8), mt=40)
    return diritti(C(colonne, legale, RAW('', css=CSS_PIEDE), pad=((48, 48, 40), 'lato', 32, 'lato'), gap='0', bg=BIANCO,
                     border_top=1, border_color=FILETTO, css='zcs-piede'))


# ---------------------------------------------------------------------------------------------
# Componenti riusabili (specifica 4.6): servono anche alle pagine interne
# ---------------------------------------------------------------------------------------------
_LS = {'display': 'zcs-ls20', 'h1': 'zcs-ls20', 'h2': 'zcs-ls15', 'h2m': 'zcs-ls15', 'h2s': 'zcs-ls10', 'h3l': 'zcs-ls10',
       'tel_grande': 'zcs-ls15'}


def classi(*nomi):
    return ' '.join(n for n in nomi if n) or None


def titolo(testo, livello='h2', stile='h2', colore=INCHIOSTRO, **p):
    """Titolo con la spaziatura in em della sua misura (classe zcs-ls*)."""
    css = classi(_LS.get(stile), p.pop('css', None))
    return H(testo, livello, style=stile, color=colore, **({'css': css} if css else {}), **p)


def testo(html, stile='body', colore=INCHIOSTRO, **p):
    """Testo; se contiene link, sono blu 600 sottolineati (classe zcs-link)."""
    css = classi('zcs-link' if '<a ' in html else None, p.pop('css', None))
    return T(html, style=stile, color=colore, link_color=BLU, link_hover=BLU_SCURO, **({'css': css} if css else {}), **p)


def sezione(*figli, pad=('sezione', 'lato'), bg=BIANCO, **p):
    """Sezione larga 1360 (con i margini laterali della scala); i figli si distanziano col loro mt."""
    return C(*figli, pad=pad, bg=bg, gap=p.pop('gap', '0'), tag='section', **p)


def capo(titolo_testo, frase=None, stile='h2', nota=None, max_w=(936, 884, None), **p):
    """Capo di sezione: titolo e frase nella stessa colonna (mai titolo a sinistra e paragrafo a destra)."""
    figli = [titolo(titolo_testo, 'h2', stile)]
    if frase:
        figli.append(testo(f'<p>{frase}</p>', colore=TESTO2, mt='s', max_w=max_w))
    if nota:
        figli.append(testo(f'<p>{nota}</p>', 'nota', TESTO2, mt='xs', max_w=max_w))
    return C(*figli, gap='0', **p)


def fiancata(colonna, foto, alt, css='', min_h=(400, 300, 0)):
    """Apertura di ogni pagina: campo blu flotta alto quanto il testo, foto vera a filo a destra (prima del titolo a 390).
    colonna = widget della colonna di testo (titolo, riga, dato da camion)."""
    testo_col = C(*colonna, w=(55.556, 50, 100), grow=True, gap='0', css='zcs-fia-testo',
                  pad=((56, 48, 32), (48, 40, 16), (56, 48, 40), 'lato'))
    foto_col = C(I(img(foto), alt), w=(44.444, 50, 100), fisso=True, min_h=min_h, css='zcs-fia-foto')
    return C(testo_col, foto_col, dir='row', dir_m='column', boxed=False, pad='0', gap='0', bg=BLU, align='stretch',
             tag='section', anchor='content', css=classi('zcs-fiancata', css))


def scheda_lavorazione(x):
    """Scheda della home: foto, nome, sottotipi, numero di foto in galleria; tutta la scheda è il link alla lavorazione."""
    frase = (f'<span class="zcs-lungo">{x["frase"]}</span><span class="zcs-breve">{x["breve"]}</span>'
             if x['breve'] else x['frase'])
    return C(
        I(img(x['foto']), x['alt']),
        titolo(x['nome'], 'h3', 'h3', mt=(16, 16, 12)),
        T(f'<p>{frase}</p>', style='piccolo', color=TESTO2, mt='xs', max_w=(480, 480, None)),
        T(f'<p>{num(n_foto(x["ancora"]))} foto di lavori</p>', style='nota', color=TESTO2, css='zcs-conta'),
        link=x['url'], gap='0', css=f'zcs-scheda zcs-{x["o"].lower()}')


def griglia(schede, colonne, **p):
    """Griglia regolare di 3 o 4 colonne (2 a 390, la prima scheda di una griglia da 3 a tutta larghezza).
    Le larghezze native restano come riserva; le colonne le fa il CSS zcs-griglia."""
    w = {3: (32.3, 32.3, 48.5), 4: (23.7, 23.7, 48.5)}[colonne]
    for i, sc in enumerate(schede):
        sc.p.setdefault('w', (w[0], w[1], 100) if colonne == 3 and i == 0 else w)
    return C(*schede, dir='row', wrap=True, gap=(20, 16, 12), gap_r=(40, 32, 24), css=f'zcs-griglia zcs-g{colonne}', **p)


def figura(foto, alt, nome, sotto=None, o='O', **p):
    """Foto di un lavoro con il nome del pezzo (e sotto, in secondario, la lavorazione)."""
    cap = f'<p><b>{nome}</b>{sotto}</p>' if sotto else f'<p>{nome}</p>'
    css = classi('zcs-lav', f'zcs-{o.lower()}', p.pop('css', None))
    return C(I(img(foto), alt), T(cap, style='nota', color=TESTO2, mt='xs', css='zcs-didascalia'), gap='0', css=css, **p)


PASSI = [
    ('Sopralluogo e misure', 'Veniamo a vedere i serramenti da cambiare o il vano da chiudere e prendiamo le misure.'),
    ('Preventivo', "Vi prepariamo il preventivo. Dopo un furto, anche quello per l'assicurazione."),
    ('Costruzione', 'Progettiamo i serramenti in alluminio e li costruiamo nella sede di Borgoricco.'),
    ('Posa e rifinitura', 'Li montiamo e li rifiniamo con il nostro personale e i nostri mezzi.'),
]


def passi(colonne=2, **p):
    """I quattro passi veri, numerati perché sono una procedura (2 colonne nella fascia azienda, 4 nelle pagine)."""
    voci = []
    for i, (t, x) in enumerate(PASSI, 1):
        voci.append(C(
            H(str(i), 'p', style='passo_n', color=BLU, w_px=(22, 22, 22), fisso=True),
            C(H(t, 'h4', style='piccolo_b', color=INCHIOSTRO), T(f'<p>{x}</p>', style='nota', color=TESTO2, mt='xxs'),
              gap='0', grow=True),
            dir='row', dir_m='row', gap='xs', w=(48, 48, 100)))
    return C(*voci, dir='row', wrap=True, gap=(32, 32, 12), gap_r=(16, 16, 12), css=f'zcs-griglia zcs-passi{colonne}', **p)


def sede(nome, ruolo, indirizzo, contatti=None):
    figli = [titolo(nome, 'h3', 'h3l'),
             T(f'<p>{ruolo}</p>', style='sede', color=TESTO2, mt='xxs'),
             T(f'<p>{indirizzo}</p>', style='sede', color=INCHIOSTRO, mt='xs')]
    if contatti:
        figli.append(T(f'<p>{contatti}</p>', style='sede', color=INCHIOSTRO, link_color=BLU, link_hover=BLU_SCURO, mt='xs',
                       sottolinea=False, css='zcs-sede-dati'))
    return C(*figli, gap='0', css='zcs-sede')


def sedi(maps=False, foto=None):
    """Le due sedi accanto al modulo (home H7, Contatti K2); foto = (file, alt, didascalia) sotto le sedi, solo da 1201 px,
    dove accanto al modulo la colonna resterebbe vuota."""
    borgo = (f'Tel. {tel_link()}<br>Fax {num(FAX)}<br><a href="mailto:{EMAIL}">{EMAIL}</a>')
    figli = [
        sede('Borgoricco (PD)', 'Sede, produzione e uffici', f'{SEDE_VIA}<br>{SEDE_CITTA}', borgo),
        # [DA CONFERMARE telefono e orari di Brebbia]
        sede('Brebbia (VA)', f'Unità locale, dal{NB}1997', f'{UL_VIA}<br>{UL_CITTA}'),
    ]
    if foto:
        figli.append(figura(foto[0], foto[1], foto[2], css='zcs-sedi-foto'))
    return C(*figli, gap=(40, 32, 32), css='zcs-sedi')


# ---------------------------------------------------------------------------------------------
# Modulo "Sopralluogo e preventivo" (specifica 14.1): Contact Form 7 in WordPress; nell'anteprima lo stesso markup che
# CF7 produce, così un solo CSS vale per tutti e due, e l'invio apre l'email già scritta.
# ---------------------------------------------------------------------------------------------
PROVINCE = ['Padova', 'Venezia', 'Treviso', 'Vicenza', 'Rovigo', 'Verona', 'Varese', 'Como', 'Milano', 'Novara',
            'Verbano-Cusio-Ossola']
PROV_BREBBIA = ['Varese', 'Como', 'Milano', 'Novara', 'Verbano-Cusio-Ossola']      # [DA CONFERMARE zone servite]
PROV_BORGORICCO = ['Padova', 'Venezia', 'Treviso', 'Vicenza', 'Rovigo', 'Verona']
FILE_FOTO = 'limit:8mb filetypes:jpg|jpeg|png|heic|webp'


def _riga_misura(n):
    altra = n > 1
    suf = f', misura {n}' if altra else ''
    return (f'<div class="zcs-misura{" zcs-altra" if altra else ""}">'
            f'<label class="zcs-mini"><span>Pezzi{suf}</span>[number pezzi{n} min:1 "1"]</label>'
            f'<label class="zcs-mini"><span>Larghezza L{suf}</span><span class="zcs-cm">[number larghezza{n} min:1]<i>cm</i></span></label>'
            '<span class="zcs-per" aria-hidden="true">×</span>'
            f'<label class="zcs-mini"><span>Altezza H{suf}</span><span class="zcs-cm">[number altezza{n} min:1]<i>cm</i></span></label>'
            '</div>')


def _scelte_cf7():
    return ' '.join(f'"{a}|{b}"' for a, b, _ in SCELTE)


MODULO_SOPRALLUOGO = '\n'.join([
    '<div class="zcs-scheda">',
    '<fieldset class="zcs-gruppo"><legend>Cosa va cambiato</legend><p class="zcs-aiuto">Potete sceglierne più di uno.</p>'
    f'[checkbox lavoro use_label_element default:get class:zcs-scelte {_scelte_cf7()}]</fieldset>',
    '<fieldset class="zcs-gruppo"><legend>Quanti pezzi e che misure</legend>'
    '<p class="zcs-aiuto">Larghezza per altezza del vano, in centimetri. Una riga per ogni misura diversa.</p>',
    '<div class="zcs-misure">' + ''.join(_riga_misura(n) for n in range(1, 5)) + '</div>',
    '<button type="button" class="zcs-aggiungi" hidden>+ Aggiungi un\'altra misura</button></fieldset>',
    '<fieldset class="zcs-gruppo"><legend>Dove si trova</legend>'
    '<div class="zcs-dove"><label class="zcs-mini"><span>Comune</span>[text* comune autocomplete:address-level2]</label>'
    '<label class="zcs-mini"><span>Provincia</span>[select provincia first_as_label "Scegliete" '
    + ' '.join(f'"{x}"' for x in PROVINCE) + ' "Altra provincia"]</label></div>'
    '<p class="zcs-aiuto zcs-sede-risponde" aria-live="polite">Secondo il comune vi risponde Borgoricco (PD) o Brebbia (VA).</p>'
    '</fieldset>',
    '<div class="zcs-gruppo"><span class="zcs-etichetta">Foto del vecchio serramento</span>'
    '<p class="zcs-aiuto">Anche fatta col telefono, da dentro e da fuori. Fino a 3 foto da 8 MB.</p>'
    f'[file foto1 {FILE_FOTO}]<span class="zcs-altra">[file foto2 {FILE_FOTO}]</span>'
    f'<span class="zcs-altra">[file foto3 {FILE_FOTO}]</span>'
    '<button type="button" class="zcs-aggiungi" hidden>+ Aggiungi un\'altra foto</button></div>',
    '<div class="zcs-campi zcs-c3"><label class="zcs-campo"><span>Nome e cognome</span>[text* your-name autocomplete:name]</label>'
    '<label class="zcs-campo"><span>Telefono</span>[tel* telefono autocomplete:tel]</label>'
    '<label class="zcs-campo"><span>Email</span>[email your-email autocomplete:email]</label></div>',
    '<label class="zcs-campo"><span>Azienda o ente</span><span class="zcs-aiuto">se la richiesta è per un\'attività o un Comune'
    '</span>[text azienda autocomplete:organization]</label>',
    '<label class="zcs-campo"><span>Note</span><span class="zcs-aiuto">piano, tipo di apertura, colore</span>[textarea note x3]</label>',
    '<div class="zcs-consenso">[acceptance privacy] Ho letto l\'<a href="/privacy/">informativa sulla privacy</a> e acconsento a '
    'essere ricontattato. [/acceptance]</div>',
    '<div class="zcs-invio">[submit class:zcs-invia "Inviate la richiesta"]'
    f'<p class="zcs-oppure">Oppure telefonate al <a href="{TEL_LINK}">{TEL}</a></p><!--anteprima--></div>',
    '</div>',
])

# scheda Mail del modulo (specifica 14.1): la imposta _prova/script/cf7-mail.php
MAIL_SOPRALLUOGO = {
    'oggetto': 'Sopralluogo: [lavoro], [comune] ([provincia])',
    'corpo': '\n'.join([
        'Cosa va cambiato: [lavoro]', '',
        'Misure (pezzi, larghezza x altezza):',
        *[f'[pezzi{n}] pezzi, [larghezza{n}] x [altezza{n}] cm' for n in range(1, 5)], '',
        'Comune: [comune] ([provincia])', 'Nome: [your-name]', 'Telefono: [telefono]', 'Email: [your-email]',
        'Azienda o ente: [azienda]', '', 'Note:', '[note]', '', '--', 'Inviato dal modulo "Sopralluogo e preventivo" del sito.']),
    'allegati': '[foto1]\n[foto2]\n[foto3]',
    # messaggi di Contact Form 7 col voi del sito (quelli di serie danno del tu e parlano di "termini e condizioni")
    'messaggi': {
        'mail_sent_ok': 'Richiesta inviata. Vi richiamiamo per fissare il sopralluogo.',
        'mail_sent_ng': f'La richiesta non è partita. Riprovate o telefonate al {TEL}.',
        'spam': f'La richiesta non è partita. Riprovate o telefonate al {TEL}.',
        'validation_error': 'Alcuni campi non sono compilati bene. Controllate e riprovate.',
        'accept_terms': 'Per inviare la richiesta serve il consenso all\'informativa sulla privacy.',
        'invalid_required': 'Compilate questo campo.',
        'invalid_email': 'L\'indirizzo email non sembra giusto.',
        'invalid_tel': 'Il numero di telefono non sembra giusto.',
        'invalid_number': 'Scrivete un numero.',
        'number_too_small': 'Il numero è troppo piccolo.',
        'upload_failed': 'Il caricamento della foto non è riuscito. Riprovate.',
        'upload_file_type_invalid': 'Questo tipo di file non va bene: usate una foto jpg, png, heic o webp.',
        'upload_file_too_large': 'La foto supera gli 8 MB.',
    },
}

_TAG_CF7 = re.compile(r'\[(\w+\*?)\s+([\w-]+)([^\]]*)\]')


def _attr(v):
    return _html.escape(v, quote=True)


def _campo_cf7(mo):
    """Un campo CF7 nel markup che CF7 stesso produce (versione 6.1), per l'anteprima."""
    tipo, nome, resto = mo.groups()
    req = tipo.endswith('*')
    tipo = tipo.rstrip('*')
    valori = re.findall(r'"([^"]*)"', resto)
    opz = re.sub(r'"[^"]*"', ' ', resto).split()
    o = dict(x.split(':', 1) for x in opz if ':' in x)
    cls = ' '.join(x.split(':', 1)[1] for x in opz if x.startswith('class:'))
    obbl = ' aria-required="true" required' if req else ''
    if tipo == 'submit':
        return f'<input class="wpcf7-form-control wpcf7-submit {cls}" type="submit" value="{_attr(valori[0])}">'
    if tipo in ('text', 'tel', 'email'):
        ac = f' autocomplete="{o["autocomplete"]}"' if 'autocomplete' in o else ''
        campo = f'<input class="wpcf7-form-control wpcf7-{tipo}"{ac}{obbl} value="" type="{tipo}" name="{nome}">'
    elif tipo == 'number':
        v = valori[0] if valori else ''
        campo = (f'<input class="wpcf7-form-control wpcf7-number" min="{o.get("min", "")}" inputmode="numeric"{obbl} '
                 f'value="{v}" type="number" name="{nome}">')
    elif tipo == 'textarea':
        righe = next((x[1:] for x in opz if re.fullmatch(r'x\d+', x)), '3')
        campo = f'<textarea rows="{righe}" class="wpcf7-form-control wpcf7-textarea" name="{nome}"></textarea>'
    elif tipo == 'select':
        primo = 'first_as_label' in opz
        voci = ''.join(f'<option value="{"" if primo and i == 0 else _attr(v)}">{v}</option>' for i, v in enumerate(valori))
        campo = f'<select class="wpcf7-form-control wpcf7-select" name="{nome}">{voci}</select>'
    elif tipo == 'file':
        acc = ','.join('.' + x for x in o.get('filetypes', '').split('|') if x)
        campo = f'<input class="wpcf7-form-control wpcf7-file" accept="{acc}" type="file" name="{nome}">'
    elif tipo == 'checkbox':
        voci = []
        for i, v in enumerate(valori):
            vis = v.split('|')[0]
            pos = ' first' if i == 0 else ' last' if i == len(valori) - 1 else ''
            voci.append(f'<span class="wpcf7-list-item{pos}"><label><input type="checkbox" name="{nome}[]" value="{_attr(vis)}">'
                        f'<span class="wpcf7-list-item-label">{vis}</span></label></span>')
        campo = f'<span class="wpcf7-form-control wpcf7-checkbox {cls}">{"".join(voci)}</span>'
    else:
        raise ValueError(f'campo CF7 non previsto: {tipo}')
    return f'<span class="wpcf7-form-control-wrap" data-name="{nome}">{campo}</span>'


def cf7_in_html(modello, nota_anteprima=''):
    """Il modulo CF7 come HTML statico per l'anteprima (stesse classi, stessa struttura)."""
    def consenso(mo):
        nome, testo_c = mo.group(1), mo.group(2).strip()
        return (f'<span class="wpcf7-form-control-wrap" data-name="{nome}"><span class="wpcf7-form-control wpcf7-acceptance">'
                f'<span class="wpcf7-list-item"><label><input type="checkbox" name="{nome}" value="1" required>'
                f'<span class="wpcf7-list-item-label">{testo_c}</span></label></span></span></span>')
    h = re.sub(r'\[acceptance ([\w-]+)\](.*?)\[/acceptance\]', consenso, modello, flags=re.S)
    h = _TAG_CF7.sub(_campo_cf7, h).replace('<!--anteprima-->', nota_anteprima).replace('\n', '')
    return (f'<div class="wpcf7"><form class="wpcf7-form zcs-anteprima" action="mailto:{EMAIL}" method="post" novalidate>'
            f'{h}</form></div>')


def modulo_cf7_testo(modello):
    """Il testo da incollare nella scheda Modulo di Contact Form 7."""
    return modello.replace('<!--anteprima-->', '') + '\n'


CSS_MODULO = (
    '.zcs-modulo .hidden-fields-container{display:none!important}'
    f'.zcs-modulo .zcs-scheda{{display:flex;flex-direction:column;gap:32px;font:400 16px/1.3 {F_NORMALE};color:{INCHIOSTRO};'
    'text-align:left}'
    # i paragrafi e gli a capo che Contact Form 7 aggiunge da solo non devono cambiare la griglia
    '.zcs-modulo .zcs-scheda p:not([class]){display:contents}'
    '.zcs-modulo .zcs-scheda br{display:none}'
    '.zcs-modulo .zcs-scheda p{margin:0}'
    '.zcs-modulo .wpcf7-form-control-wrap{display:block;position:relative}'
    '.zcs-modulo .zcs-altra{display:block}.zcs-modulo .zcs-misura.zcs-altra{display:grid}'
    '.zcs-modulo .zcs-altra[hidden],.zcs-modulo .zcs-aggiungi[hidden]{display:none!important}'
    '.zcs-modulo .zcs-gruppo{border:0;padding:0;margin:0;min-width:0}'
    f'.zcs-modulo .zcs-gruppo>legend,.zcs-modulo .zcs-etichetta{{display:block;float:none;width:auto;padding:0;margin:0;'
    f'font:600 17px/1.3 {F_NORMALE};color:{INCHIOSTRO}}}'
    f'.zcs-modulo .zcs-scheda .zcs-aiuto{{display:block;font:400 15px/1.45 {F_NORMALE};color:{TESTO2};margin:4px 0 0}}'
    # cosa va cambiato: le miniature dei lavori veri come scelte
    '.zcs-modulo .zcs-scelte{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:12px}'
    f'.zcs-modulo .zcs-scelte .wpcf7-list-item{{display:block;position:relative;margin:0;background:{BIANCO};'
    f'border:1px solid {FILETTO}}}'
    f'.zcs-modulo .zcs-scelte .wpcf7-list-item:hover{{border-color:{INCHIOSTRO}}}'
    f'.zcs-modulo .zcs-scelte .wpcf7-list-item:has(input:checked){{border-color:{BLU};box-shadow:0 0 0 1px {BLU}}}'
    '.zcs-modulo .zcs-scelte label{display:block;cursor:pointer;margin:0;line-height:1.3}'
    f'.zcs-modulo .zcs-scelte label::before{{content:"";display:block;aspect-ratio:1/1;background:{ALLUMINIO} center/cover no-repeat}}'
    '__MINIATURE__'
    '.zcs-modulo .zcs-scelte label.zcs-con-foto::before{content:none}'
    '.zcs-modulo .zcs-scelte label img{display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:cover;margin:0}'
    '.zcs-modulo .zcs-scelte input{position:absolute;opacity:0;width:1px;height:1px;margin:0}'
    f'.zcs-modulo .zcs-scelte .wpcf7-list-item-label{{position:relative;display:block;margin:0;padding:8px 8px 12px 32px;'
    f'font:600 15px/1.3 {F_NORMALE};color:{INCHIOSTRO}}}'
    f'.zcs-modulo .zcs-scelte .wpcf7-list-item-label::before{{content:"";position:absolute;left:8px;top:10px;width:16px;'
    f'height:16px;box-sizing:border-box;border:1.5px solid {CAMPO};border-radius:2px;background:{BIANCO}}}'
    '.zcs-modulo .zcs-scelte .wpcf7-list-item-label::after{content:none}'
    f'.zcs-modulo .zcs-scelte input:checked+.wpcf7-list-item-label::before{{background:{BLU};border-color:{BLU}}}'
    '.zcs-modulo .zcs-scelte input:checked+.wpcf7-list-item-label::after{content:"";position:absolute;left:13px;top:12px;'
    'width:5px;height:10px;border:solid #FFFFFF;border-width:0 2px 2px 0;transform:rotate(45deg)}'
    f'.zcs-modulo .zcs-scelte input:focus-visible+.wpcf7-list-item-label{{outline:3px solid {BLU};outline-offset:-3px}}'
    # misure L x H in centimetri
    '.zcs-modulo .zcs-misure{display:grid;gap:12px;margin-top:12px}'
    '.zcs-modulo .zcs-misura{display:grid;grid-template-columns:96px minmax(0,1fr) 20px minmax(0,1fr);gap:12px;align-items:end}'
    f'.zcs-modulo .zcs-mini{{display:flex;flex-direction:column;gap:8px;min-width:0;margin:0;font:400 15px/1.3 {F_NORMALE};'
    f'color:{INCHIOSTRO}}}'
    f'.zcs-modulo .zcs-per{{text-align:center;padding-bottom:13px;color:{TESTO2}}}'
    '.zcs-modulo .zcs-cm{position:relative;display:block}'
    f'.zcs-modulo .zcs-cm i{{position:absolute;right:12px;top:25px;transform:translateY(-50%);font-style:normal;'
    f'font:400 16px/1 {F_NORMALE};color:{TESTO2};pointer-events:none}}'
    '.zcs-modulo .zcs-cm input{padding-right:44px!important}'
    '.zcs-modulo .zcs-misura.zcs-altra .zcs-mini>span:first-child{position:absolute;width:1px;height:1px;overflow:hidden;'
    'clip-path:inset(50%);white-space:nowrap}'
    f'.zcs-modulo .zcs-aggiungi,.zcs-modulo .zcs-aggiungi:focus{{display:inline-block;margin-top:12px;padding:4px 0;'
    f'background:none;border:0;border-radius:0;box-shadow:none;font:600 16px/1.3 {F_NORMALE};color:{BLU};'
    'text-decoration:underline;text-underline-offset:4px;cursor:pointer;white-space:normal;width:auto}'
    f'.zcs-modulo .zcs-aggiungi:hover,.zcs-modulo .zcs-aggiungi:focus-visible{{background:none;color:{BLU_SCURO};'
    'text-decoration-thickness:2px}'
    # dove si trova, dati della persona
    '.zcs-modulo .zcs-dove{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:20px;margin-top:12px}'
    '.zcs-modulo .zcs-campi{display:grid;gap:20px;min-width:0}'
    '.zcs-modulo .zcs-c3{grid-template-columns:repeat(3,minmax(0,1fr))}'
    '.zcs-modulo .zcs-c2{grid-template-columns:repeat(2,minmax(0,1fr))}'
    f'.zcs-modulo .zcs-campo{{display:flex;flex-direction:column;gap:8px;min-width:0;margin:0;font:400 16px/1.3 {F_NORMALE};'
    f'color:{INCHIOSTRO}}}'
    '.zcs-modulo .zcs-campo>span:first-child{font-weight:600}'
    '.zcs-modulo .zcs-scheda .zcs-campo>.zcs-aiuto{margin-top:-4px}'
    '.zcs-modulo .zcs-scheda input[type=text],.zcs-modulo .zcs-scheda input[type=tel],.zcs-modulo .zcs-scheda input[type=email],'
    '.zcs-modulo .zcs-scheda input[type=number],.zcs-modulo .zcs-scheda select,.zcs-modulo .zcs-scheda textarea'
    f'{{display:block;width:100%;min-height:50px;margin:0;padding:12px;box-sizing:border-box;font:400 17px/1.3 {F_NORMALE};'
    f'color:{INCHIOSTRO};background:{BIANCO};border:1px solid {CAMPO};border-radius:2px;box-shadow:none;transition:none;'
    'font-variant-numeric:tabular-nums lining-nums}'
    '.zcs-modulo .zcs-scheda input:focus,.zcs-modulo .zcs-scheda select:focus,.zcs-modulo .zcs-scheda textarea:focus'
    f'{{border-color:{CAMPO}}}'
    '.zcs-modulo .zcs-scheda select{height:50px;padding-top:0;padding-bottom:0}'
    '.zcs-modulo .zcs-scheda textarea{height:96px;min-height:96px;resize:vertical}'
    '.zcs-modulo .zcs-scheda input[type=number]{-moz-appearance:textfield;appearance:textfield}'
    '.zcs-modulo .zcs-scheda input[type=number]::-webkit-inner-spin-button,'
    '.zcs-modulo .zcs-scheda input[type=number]::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}'
    # foto: bottone e nome del file scelto (lo script le costruisce; senza script resta il campo del browser)
    f'.zcs-modulo .zcs-scheda input[type=file]{{display:block;max-width:100%;margin-top:12px;font:400 15px/1.3 {F_NORMALE}}}'
    f'.zcs-modulo .zcs-file{{position:relative;display:flex;align-items:center;gap:12px;min-height:50px;margin:12px 0 0;'
    f'padding:4px 8px 4px 4px;box-sizing:border-box;border:1px solid {CAMPO};border-radius:2px;background:{BIANCO};'
    'cursor:pointer;font-weight:400;line-height:1.3}'
    '.zcs-modulo .zcs-file input[type=file]{position:absolute;width:1px;height:1px;margin:0;overflow:hidden;'
    'clip-path:inset(50%);white-space:nowrap;opacity:0}'
    f'.zcs-modulo .zcs-file-bottone{{flex:0 0 auto;background:{ALLUMINIO};color:{INCHIOSTRO};border:1px solid {CAMPO};'
    f'border-radius:2px;padding:8px 12px;font:600 15px/1.2 {F_NORMALE}}}'
    f'.zcs-modulo .zcs-file:hover .zcs-file-bottone{{background:{INCHIOSTRO};border-color:{INCHIOSTRO};color:{BIANCO}}}'
    f'.zcs-modulo .zcs-file:focus-within{{outline:3px solid {BLU};outline-offset:3px}}'
    f'.zcs-modulo .zcs-file-nome{{min-width:0;font:400 15px/1.3 {F_NORMALE};color:{TESTO2};overflow:hidden;'
    'text-overflow:ellipsis;white-space:nowrap}'
    # consenso e invio
    '.zcs-modulo .zcs-consenso .wpcf7-list-item{display:block;margin:0}'
    f'.zcs-modulo .zcs-consenso label{{display:flex;gap:12px;align-items:flex-start;margin:0;cursor:pointer;'
    f'font:400 16px/1.4 {F_NORMALE};color:{INCHIOSTRO}}}'
    f'.zcs-modulo .zcs-consenso input{{width:20px;height:20px;margin:1px 0 0;flex:0 0 auto;accent-color:{BLU}}}'
    '.zcs-modulo .zcs-consenso .wpcf7-list-item-label::before,.zcs-modulo .zcs-consenso .wpcf7-list-item-label::after{content:none}'
    f'.zcs-modulo .zcs-scheda a{{color:{BLU};font-weight:600;text-decoration:underline;text-decoration-thickness:1px;'
    'text-underline-offset:4px}'
    f'.zcs-modulo .zcs-scheda a:hover,.zcs-modulo .zcs-scheda a:focus-visible{{color:{BLU_SCURO};text-decoration-thickness:2px}}'
    '.zcs-modulo .zcs-invio{position:relative;display:flex;flex-wrap:wrap;align-items:center;gap:12px 32px}'
    '.zcs-modulo .zcs-scheda .wpcf7-submit,.zcs-modulo .zcs-scheda .wpcf7-submit:focus'
    f'{{display:inline-block;width:auto;margin:0;padding:16px 28px;font:600 17px/1.2 {F_NORMALE};color:{BIANCO};'
    f'background:{BLU};border:0;border-radius:2px;box-shadow:none;cursor:pointer;white-space:nowrap;'
    'transition:background-color .12s}'
    f'.zcs-modulo .zcs-scheda .wpcf7-submit:hover,.zcs-modulo .zcs-scheda .wpcf7-submit:focus-visible'
    f'{{background:{BLU_SCURO};color:{BIANCO}}}'
    f'.zcs-modulo .zcs-scheda .wpcf7-submit:disabled{{background:{CAMPO};color:{BIANCO};cursor:default}}'
    f'.zcs-modulo .zcs-scheda .zcs-oppure{{font:400 16px/1.4 {F_NORMALE};color:{TESTO2}}}'
    '.zcs-modulo .zcs-scheda .zcs-oppure a{text-decoration:none;white-space:nowrap}'
    '.zcs-modulo .zcs-scheda .zcs-oppure a:hover,.zcs-modulo .zcs-scheda .zcs-oppure a:focus-visible{text-decoration:underline}'
    '.zcs-modulo .zcs-scheda .zcs-nota-anteprima{flex:1 0 100%}'
    '.zcs-modulo .wpcf7-spinner{position:absolute;left:0;top:100%;margin:8px 0 0}'
    # esito ed errori: testo semplice, nessun riquadro colorato
    f'.zcs-modulo .wpcf7 form .wpcf7-response-output{{margin:24px 0 0;padding:0;border:0;font:400 17px/1.55 {F_NORMALE};'
    f'color:{INCHIOSTRO}}}'
    f'.zcs-modulo .wpcf7-not-valid-tip{{display:block;margin-top:8px;font:400 15px/1.4 {F_NORMALE};color:{ERRORE}}}'
    '.zcs-modulo .zcs-scheda input.wpcf7-form-control.wpcf7-not-valid,.zcs-modulo .zcs-scheda select.wpcf7-form-control.wpcf7-not-valid,'
    f'.zcs-modulo .zcs-scheda textarea.wpcf7-form-control.wpcf7-not-valid{{border:2px solid {ERRORE}}}'
    '@media (max-width:767px){'
    '.zcs-modulo .zcs-scelte{grid-template-columns:repeat(2,minmax(0,1fr))}'
    '.zcs-modulo .zcs-misura{grid-template-columns:64px minmax(0,1fr) 12px minmax(0,1fr);gap:8px}'
    '.zcs-modulo .zcs-c2,.zcs-modulo .zcs-c3,.zcs-modulo .zcs-dove{grid-template-columns:1fr;gap:16px}'
    '.zcs-modulo .zcs-scheda .wpcf7-submit{width:100%}'
    '}'
)

JS_MODULO = (
    "(function(){var BRE=" + str(PROV_BREBBIA).replace("'", '"') + ",BOR=" + str(PROV_BORGORICCO).replace("'", '"') + ";"
    "var NESSUNA='Nessuna foto scelta',MINI=__MINI__;"
    "function via(){document.querySelectorAll('.zcs-modulo .zcs-scheda').forEach(function(s){"
    "if(s.getAttribute('data-pronto'))return;s.setAttribute('data-pronto','1');var form=s.closest('form');"
    # le miniature delle scelte come immagini vere (alt vuoto: il nome è il testo della voce)
    "s.querySelectorAll('.zcs-scelte .wpcf7-list-item label').forEach(function(l,k){if(!MINI[k]||l.querySelector('img'))return;"
    "var im=document.createElement('img');im.src=MINI[k];im.alt='';im.width=320;im.height=320;im.loading='lazy';"
    "l.insertBefore(im,l.firstChild);l.classList.add('zcs-con-foto')});"
    # foto: bottone e nome del file
    "s.querySelectorAll('input[type=file]').forEach(function(i){var l=document.createElement('label');l.className='zcs-file';"
    "i.parentNode.insertBefore(l,i);l.appendChild(i);var b=document.createElement('span');b.className='zcs-file-bottone';"
    "b.textContent='Scegliete la foto';var n=document.createElement('span');n.className='zcs-file-nome';n.textContent=NESSUNA;"
    "l.appendChild(b);l.appendChild(n);var up=function(){n.textContent=i.files&&i.files.length?i.files[0].name:NESSUNA};"
    "i.addEventListener('change',up);if(form)form.addEventListener('reset',function(){setTimeout(up,0)})});"
    # righe di misura e foto in più: una alla volta, il fuoco va sul primo campo nuovo
    "s.querySelectorAll('.zcs-aggiungi').forEach(function(b){var g=b.closest('.zcs-gruppo');"
    "var al=[].slice.call(g.querySelectorAll('.zcs-altra'));if(!al.length)return;al.forEach(function(a){a.hidden=true});"
    "b.hidden=false;b.addEventListener('click',function(){var a=al.filter(function(x){return x.hidden})[0];if(!a)return;"
    "a.hidden=false;var f=a.querySelector('input:not([type=hidden])');"
    "if(!al.some(function(x){return x.hidden}))b.hidden=true;if(f)f.focus()})});"
    # la provincia dice quale sede risponde
    "var p=s.querySelector('select[name=provincia]'),m=s.querySelector('.zcs-sede-risponde');"
    "if(p&&m){var t0=m.textContent;p.addEventListener('change',function(){var v=p.value;"
    "m.textContent=BRE.indexOf(v)>-1?'Vi risponde l\\'unità locale di Brebbia (VA), via Sandro Pertini 1.'"
    ":BOR.indexOf(v)>-1?'Vi risponde la sede di Borgoricco (PD), via dell\\'Industria 18.':t0})}"
    # anteprima HTML: ?lavoro= spunta la voce; l'invio apre l'email già scritta
    "if(form&&form.classList.contains('zcs-anteprima')){"
    "new URLSearchParams(location.search).getAll('lavoro').forEach(function(v){"
    "form.querySelectorAll('input[name=\"lavoro[]\"]').forEach(function(c){if(c.value===v)c.checked=true})});"
    "form.addEventListener('submit',function(e){e.preventDefault();if(!form.reportValidity())return;"
    "var d=new FormData(form),g=function(k){return (d.get(k)||'').toString().trim()},r=[];"
    "var lav=d.getAll('lavoro[]').join(', ');r.push('Cosa va cambiato: '+(lav||'da indicare'));"
    "for(var k=1;k<=4;k++){if(g('larghezza'+k)||g('altezza'+k))r.push('Misura '+k+': '+(g('pezzi'+k)||'1')+' pezzi, '"
    "+g('larghezza'+k)+' x '+g('altezza'+k)+' cm')}"
    "r.push('Comune: '+g('comune')+(g('provincia')?' ('+g('provincia')+')':''),'Nome: '+g('your-name'),"
    "'Telefono: '+g('telefono'),'Email: '+g('your-email'),'Azienda o ente: '+g('azienda'),'Note: '+g('note'));"
    "location.href='mailto:" + EMAIL + "?subject='+encodeURIComponent('Sopralluogo: '+(lav||'richiesta')+', '+g('comune'))"
    "+'&body='+encodeURIComponent(r.join('\\n'))})}"
    "})}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',via)}else{via()}})();"
)


def css_modulo():
    mini = ''.join(f'.zcs-modulo .zcs-scelte .wpcf7-list-item:nth-child({i}) label::before{{background-image:url("{img(f)}")}}'
                   for i, (_, _, f) in enumerate(SCELTE, 1))
    return CSS_MODULO.replace('__MINIATURE__', mini)


def modulo_sopralluogo(**p):
    """Il modulo intero (home e Contatti): shortcode CF7 in WordPress, lo stesso markup nell'anteprima."""
    nota = '<p class="zcs-aiuto zcs-nota-anteprima">L\'invio apre il vostro programma di posta con la richiesta già scritta: le foto allegatele all\'email.</p>'
    alternativa = cf7_in_html(MODULO_SOPRALLUOGO, nota)
    mini = '[' + ','.join(f'"{img(f)}"' for _, _, f in SCELTE) + ']'
    return C(SHORTCODE(CF7_SOPRALLUOGO, alternativa_html=alternativa, colore=INCHIOSTRO),
             RAW(f'<script>{JS_MODULO.replace("__MINI__", mini)}</script>', css=css_modulo()), gap='0', css='zcs-modulo',
             anchor='scheda', **p)


def scrivi_moduli(cartella):
    """Scrive in plugin/ il testo dei moduli Contact Form 7 (da incollare nella scheda Modulo, o con cf7.php)."""
    import os
    os.makedirs(cartella, exist_ok=True)
    with open(os.path.join(cartella, 'contact-form-7-sopralluogo-e-preventivo.txt'), 'w', encoding='utf-8') as f:
        f.write(modulo_cf7_testo(MODULO_SOPRALLUOGO))


# ---------------------------------------------------------------------------------------------
# HOME (specifica 7)
# ---------------------------------------------------------------------------------------------
CSS_HOME_FIANCATA = (
    # la foto dell'autogru tiene la sponda "ZOCCARATO" e il primo furgone a ogni larghezza
    '.zcs-fia-home .zcs-fia-foto img{object-position:17% 50%}'
    '@media (min-width:1025px) and (max-width:1300px){.zcs-fia-home .zcs-display .elementor-heading-title,'
    '.zcs-fia-home h1.zcs-display{font-size:52px!important}}'
    '@media (max-width:999px) and (min-width:768px){.zcs-fia-home .zcs-fia-foto img{object-position:0 50%}}'
    '@media (max-width:767px){.zcs-fia-home .zcs-fia-foto{aspect-ratio:820/600}'
    '.zcs-fia-home .zcs-fia-foto img{object-position:50% 50%}'
    '.zcs-fia-home .zcs-display .elementor-heading-title,.zcs-fia-home h1.zcs-display{line-height:1.05!important}}'
)


def home_fiancata():
    colonna = [
        T('<p>Serramenti metallici</p>', style='scritta', color=BIANCO),
        titolo(f'Serramenti in alluminio da Borgoricco, dal{NB}1974', 'h1', 'display', BIANCO, mt='m', css='zcs-display'),
        T('<p>Finestre, scorrevoli, persiane, portoncini e pensiline. Li progettiamo, li costruiamo e li montiamo con il nostro '
          'personale, fino alla rifinitura.</p>', style='lead', color=BIANCO, mt=(20, 16, 16), max_w=(620, 558, None)),
        T(f'<p><span class="zcs-nw">Padovano: Borgoricco{NB}(PD)</span><span class="zcs-sep" aria-hidden="true"> · </span>'
          f'<span class="zcs-nw">Varesotto: Brebbia{NB}(VA)</span></p>', style='fatti', color=BIANCO, mt='l', css='zcs-fia-sedi'),
        B('Chiedete un sopralluogo', '#preventivo', variant='bianco', full_m=True, mt='l'),
        RAW('', css=CSS_HOME_FIANCATA),
    ]
    return fiancata(colonna, 'flotta-autogru.jpg',
                    "Il camion con l'autogru e la scritta Serramenti metallici Zoccarato, Borgoricco (PD) - Brebbia (VA), nel "
                    'piazzale della sede, e dietro i furgoni con la stessa scritta', css='zcs-fia-home', min_h=(360, 300, 0))


def home_casa():
    casa = [x for x in LAVORAZIONI if x['gruppo'] == 'casa']
    return sezione(
        capo('Per la casa', 'Per sostituire i vecchi serramenti o per una casa nuova facciamo il sopralluogo, prendiamo le misure, '
                            'costruiamo nella sede di Borgoricco e montiamo con il nostro personale, fino alla rifinitura.'),
        griglia([scheda_lavorazione(x) for x in casa[:3]], 3, mt='xl'),
        griglia([scheda_lavorazione(x) for x in casa[3:]], 4, mt='xxl'),
        pad=('sezione', 'lato', 0, 'lato'), anchor='casa')


def home_aziende():
    # [DA CONFERMARE quali compagnie si possono nominare; il permesso di citare i due lavori pubblici]
    return sezione(
        capo('Per aziende, negozi e stazioni di servizio',
             'Per le più note compagnie di distribuzione carburanti abbiamo fatto vetrine e porte dei punti vendita, chioschi e '
             'pensiline. Lavoriamo anche per uffici, negozi e capannoni.',
             nota=f'Tra i lavori pubblici, le porte degli uffici di Villa Frua a Laveno Mombello ({num("2021")}) e gli infissi '
                  f"dell'asilo nido Torre a Cocquio Trevisago ({num('2023')})."),
        griglia([scheda_lavorazione(x) for x in LAVORAZIONI if x['gruppo'] == 'aziende'], 3, mt='xl'),
        pad=('sezione', 'lato', 0, 'lato'), anchor='aziende')


LAVORI_HOME = [
    [[('lav-bovindo.jpg', 'O', 'Villa con bovindo vetrato al piano terra e giardino fiorito', 'Villa con bovindo vetrato', 'finestre'),
      ('lav-inglesine.jpg', 'V', 'Portafinestra effetto legno con inglesine aperta su un balcone in ferro',
       'Portafinestra con inglesine', 'finestre')],
     [('lav-timpano.jpg', 'O', 'Casa con timpano vetrato sotto il tetto in coppi', 'Timpano vetrato', 'finestre'),
      ('lav-veranda-bronzo.jpg', 'V', 'Veranda con scorrevoli color bronzo su pavimento in pietra', 'Veranda color bronzo',
       'scorrevoli')]],
    [[('lav-persiane-scorrevoli.jpg', 'V', 'Persiane scorrevoli grigie chiuse lungo la facciata', 'Persiane scorrevoli',
       'oscuranti'),
      ('lav-copertura-vetrata.jpg', 'O', 'Copertura vetrata apribile sopra una scala esterna',
       'Copertura vetrata apribile sulla scala', 'speciali')],
     [('lav-vetrata-bar.jpg', 'V', 'Vetrata a tutta altezza di un bar con tavolini e sedie arancioni', 'Vetrata di un bar',
       'commerciali'),
      ('lav-cancello.jpg', 'O', 'Cancello scorrevole in lamiera stirata grigia', 'Cancello in lamiera stirata', 'speciali')]],
]


def home_lavori():
    righe = []
    for riga in LAVORI_HOME:
        coppie = [C(*[figura(f, alt, nome, LAV[a]['nome'], o, w=(63, 63, 63) if o == 'O' else (34, 34, 34))
                      for f, o, alt, nome, a in coppia],
                    dir='row', gap=(20, 16, 12), w=(48.5, 48.5, 100), css='zcs-coppia zcs-duo') for coppia in riga]
        righe.append(C(*coppie, dir='row', dir_m='column', gap=(20, 16, 24)))
    return sezione(
        capo('Lavori finiti', f'Nella pagina <a href="/lavori/">Lavori</a> trovate {TOTALE_FOTO} foto di case, negozi, uffici e '
                              'stazioni di servizio, divise per lavorazione.', stile='h2m'),
        C(*righe, gap=(40, 32, 24), mt='xxl', css='zcs-righe-lav'),
        pad=((72, 72, 56), 'lato', 0, 'lato'))


def home_furto():
    testo_col = C(
        titolo('Dopo un furto'),
        testo('<p>Se vi hanno forzato una porta, una vetrina o una serranda, interveniamo in tempi rapidi e prepariamo il '
              'preventivo per la compagnia assicurativa.</p>', mt='m', max_w=(486, 459, None)),
        testo('<p>Chiamate subito il</p>', colore=TESTO2, mt='m'),
        titolo(TEL, 'p', 'tel_grande', BLU, link=TEL_LINK, mt='xxs', css='zcs-tel'),
        testo('<p><a href="/dopo-un-furto/">Cosa fare dopo un furto</a></p>', mt='m'),
        gap='0', w=(40, 45, 100), css='zcs-furto-testo')
    foto = C(
        figura('furto-serranda.jpg', 'Serranda metallica divelta davanti a una vetrina, vetri a terra',
               "Serranda divelta dopo un'effrazione", o='O', w=(57, 57, 57)),
        figura('furto-porta.jpg', 'Porta vetrata a due ante di un punto vendita, rimessa a nuovo',
               'Porta di un punto vendita, ripristinata', o='Q', w=(40, 40, 40)),
        dir='row', gap=(20, 16, 12), w=(55, 50, 100), css='zcs-furto-foto zcs-duo')
    return sezione(C(testo_col, foto, dir='row', dir_m='column', gap=(56, 40, 24), align='start'),
                   anchor='furto')


CSS_AZIENDA = (
    '.zcs-azienda-testo{flex:1 1 0!important;min-width:0}'
    '.zcs-az-foto{flex:0 0 304px!important}'
    '@media (max-width:1024px){.zcs-azienda-in{flex-wrap:wrap!important}.zcs-azienda-testo{order:-1;flex:0 0 100%!important}'
    '.zcs-az-foto{flex:1 1 0!important;min-width:0}}'
)


def home_azienda():
    testo_col = C(
        titolo("Dall'officina del ferro all'alluminio", 'h2', 'h2s'),
        testo('<p>Nel 1974 il fondatore apre una piccola officina per recinzioni e cancelli. Nel 1982 entrano in azienda i figli '
              'Sante e Maurizio e comincia la produzione dei serramenti in alluminio, nel primo capannone della zona artigianale, '
              "che oggi è la sede di via dell'Industria. Nel 1997 apre l'unità locale di Brebbia, in provincia di Varese.</p>",
              mt='s', max_w=(648, 612, None)),
        testo('<p><a href="/chi-siamo/">La storia e la flotta</a></p>', mt='s'),
        titolo('Dal sopralluogo alla rifinitura', 'h3', 'h3s', mt='xl'),
        passi(2, mt='s'),
        gap='0', w=(50, 100, 100), css='zcs-azienda-testo')
    f1 = figura('storia-1974.jpg', 'Foto in bianco e nero degli inizi: un camion carico di una struttura in ferro',
                '1974, gli inizi', w=(22, 48, 48), css='zcs-az-foto')
    f2 = figura('sede-furgoni.jpg', "La sede di via dell'Industria vista dall'alto, con i furgoni bianchi e l'autogru rossa nel "
                'piazzale', "La sede di Borgoricco, con i furgoni e l'autogru", w=(22, 48, 48), css='zcs-az-foto')
    return sezione(C(f1, testo_col, f2, dir='row', wrap=(False, True, True), gap=(40, 24, 12), gap_r=(40, 24, 24),
                     align='start', css='zcs-azienda-in'),
                   RAW('', css=CSS_AZIENDA), bg=ALLUMINIO, pad=((48, 48, 40), 'lato'), anchor='azienda')


CSS_PREVENTIVO = (
    '.zcs-prev-modulo{flex:0 0 716px!important;min-width:0}'
    '.zcs-sedi{flex:1 1 0!important;min-width:0;padding-top:8px}'
    '@media (max-width:1200px){.zcs-prev-in{flex-direction:column!important;gap:48px!important}'
    '.zcs-prev-modulo{flex:none!important;width:100%!important;max-width:716px}'
    '.zcs-sedi{flex:none!important;width:100%!important;max-width:716px;display:grid!important;'
    'grid-template-columns:repeat(2,minmax(0,1fr));gap:32px!important;padding-top:0}}'
    '@media (max-width:1200px){.zcs-sedi-foto{display:none!important}}'
    '@media (max-width:767px){.zcs-sedi{grid-template-columns:1fr}}'
)


def blocco_preventivo(anchor='preventivo', maps=False):
    """Sopralluogo e preventivo: il modulo intero e le due sedi (home H7, Contatti K2)."""
    modulo_col = C(
        titolo('Sopralluogo e preventivo'),
        testo('<p>Diteci cosa va cambiato, quanti pezzi sono e le misure indicative del vano, larghezza per altezza in '
              'centimetri. Una foto del vecchio serramento ci aiuta a capire il lavoro. Vi richiamiamo per fissare il '
              'sopralluogo.</p>', mt='m'),
        modulo_sopralluogo(mt='xl'),
        gap='0', w=(55, 100, 100), css='zcs-prev-modulo')
    foto = ('flotta-furgoni.jpg', "I furgoni bianchi con la scritta Zoccarato nel piazzale della sede di Borgoricco",
            'I nostri furgoni nel piazzale di Borgoricco')
    return sezione(C(modulo_col, sedi(maps, foto), dir='row', dir_t='column', gap=(96, 48, 48), align='start',
                     css='zcs-prev-in'),
                   RAW('', css=CSS_PREVENTIVO), anchor=anchor)


def home():
    return [(n, diritti(s)) for n, s in (
        ('fiancata', home_fiancata()), ('per-la-casa', home_casa()), ('per-le-aziende', home_aziende()),
        ('lavori-finiti', home_lavori()), ('dopo-un-furto', home_furto()), ('azienda', home_azienda()),
        ('sopralluogo', blocco_preventivo()))]


# ---------------------------------------------------------------------------------------------
# Pagine (specifica 6): in questa fase solo la home; testata e menu hanno già tutte le voci
# ---------------------------------------------------------------------------------------------
PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Zoccarato Serramenti, serramenti in alluminio a Borgoricco (PD) e Brebbia (VA)',
     'descrizione': 'Finestre, scorrevoli, persiane, portoncini, pergole e pensiline in alluminio. Progettati, costruiti e '
                    'montati dal nostro personale. Borgoricco (PD) e Brebbia (VA), dal 1974.'},
]
