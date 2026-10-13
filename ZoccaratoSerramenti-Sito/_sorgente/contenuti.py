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
                          f'<li><a href="{url}" data-percorso="{url}">{nome}: tutte le lavorazioni</a></li>{sotto}</ul></details>')
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
    return C(RAW(barra_html(), css=CSS_SITO + CSS_TESTATA), testata, pad='0', gap='0', boxed=False, bg=BIANCO)


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
    return C(colonne, legale, RAW('', css=CSS_PIEDE), pad=((48, 48, 40), 'lato', 32, 'lato'), gap='0', bg=BIANCO,
             border_top=1, border_color=FILETTO, css='zcs-piede')
