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
