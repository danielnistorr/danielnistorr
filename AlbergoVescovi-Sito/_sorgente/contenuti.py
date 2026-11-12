# -*- coding: utf-8 -*-
"""
Contenuti del sito Albergo Vescovi (Albergo Vescovi Fabio S.r.l., Asiago).

Idea: la casa gialla in mezzo al prato della Piana Ave, a 900 metri dal centro di Asiago. La home si apre con
"Sulla Piana Ave" scritto grande sull'erba davanti all'albergo e si chiude sullo stesso prato d'inverno.
È il prototipo approvato dal committente (giro 2, "la fotografia": _prova/direzioni/giro2/fotografia/), costruito
con il generatore di Benvegnù secondo _prova/spec.md.

Carattere: Petrona sola, pesi 400 e 500, nessun corsivo (guida CARATTERI-E-SEGNALI-IA, c3: riferimento reale
Il Palazzo Experimental, Venezia, con Nantes per il 79 % del testo). Palette: verde bosco del logo tondo, bianco,
inchiostro (lo stesso verde quasi nero). Il resto del colore lo danno le foto: prato, abete, neve.

Fonti dei testi: sito attuale (01-analisi-sito-attuale.md, testi verbatim), motore di prenotazione Persefone,
registro regionale. I fatti da confermare col cliente sono elencati nella specifica, paragrafo 18.
"""
import motore as m
from motore import C, H, T, B, I, RAW, MENU

PREFISSO = 'avs'
NOME_SITO = 'Albergo Vescovi'

# ---------------------------------------------------------------------------------------------
# Tema (specifica, paragrafo 4)
# ---------------------------------------------------------------------------------------------
VERDE = '#2A3F1C'          # metà alta del logo tondo: titoli, bottoni, link, fascia del piede, voce attiva
BIANCO = '#FFFFFF'
INCHIOSTRO = '#20271B'     # testo: lo stesso verde, quasi nero (15,36:1 sul bianco)
NOTA = '#525C4B'           # note, didascalie, piede (7,02:1)
VERDE_SCURO = '#1B2A11'    # solo hover dei bottoni verdi
SALVIA = '#E4E9DD'         # solo hover dei link bianchi sulla fascia verde e del tasto "Chiama"
FILETTO = '#D5DACF'        # solo sotto il menu aperto e fra le righe della tabella delle camere
NEVE = '#E7ECEF'           # fondo della foto d'inverno mentre carica
PRATO = '#566B3C'          # fondo della foto d'apertura mentre carica
VELO = '#121A0C'           # velatura scura sotto il titolo d'apertura

FONT = 'Petrona'
PILA = f"'{FONT}',Georgia,serif"


def _st(w, s, lh, ls=0.0):
    """Stile di testo: peso, misure (1440, 1024, 390), interlinea, spaziatura in px alla misura desktop."""
    return dict(f=FONT, w=w, s=s, lh=lh, ls=ls, up=False)


TEMA = {
    'nome': 'Piana Ave',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': INCHIOSTRO, 'testo2': NOTA, 'accento': VERDE,
    'filetto': FILETTO, 'filetto_scuro': VERDE_SCURO, 'su_scuro2': SALVIA,
    'scuro': VERDE, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': FONT, 'font_testo': FONT, 'larghezza': 1344,
    'google_fonts': 'https://fonts.googleapis.com/css2?family=Petrona:wght@400;500&display=swap',
    # spaziatura delle lettere: il motore la scrive in px; -0,022em a 164 px = -3,6 px. Dove la misura cambia molto fra
    # desktop e telefono (display, chiusura) la spaziatura in em è riscritta nel CSS della sezione.
    'stili': {
        'display':     _st('400', (164, 112, 76), 0.90, -3.6),
        'h1':          _st('500', (58, 46, 34), 1.06, -0.5),
        'h2_chiusura': _st('500', (64, 50, 38), 1.02, -1.0),
        'h2':          _st('500', (42, 36, 30), 1.10, -0.5),
        'domanda':     _st('500', (30, 27, 26), 1.20, -0.18),
        'h3':          _st('500', (22, 21, 20), 1.30),
        'lead':        _st('400', (20, 19, 18), 1.45),
        'body':        _st('400', (19, 19, 18), 1.60),
        'inverno':     _st('500', (19, 18, 18), 1.50),
        'link':        _st('500', (19, 19, 18), 1.60),
        'nota':        _st('400', (17, 17, 17), 1.55),
        'small':       _st('400', (15, 15, 15), 1.60),
        'tel':         _st('400', (28, 24, 23), 1.20, -0.14),
        'nav':         _st('500', (17, 20, 20), 1.20),
        'btn':         _st('500', (17, 17, 17), 1.20),
    },
    # una sola scala: 8, 16, 24, 32, 48, 72, 112, 160 (specifica 4.4)
    'spazi': {
        'xs': (8, 8, 8), 's': (16, 16, 16), 'm': (24, 24, 24), 'l': (32, 32, 32), 'xl': (48, 48, 32),
        'xxl': (72, 72, 48), 'sezione': (160, 112, 112), 'lato': (48, 32, 24), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): il colore cambia pieno, mai opacità
    'bottoni': {
        'primario': (BIANCO, VERDE, VERDE, BIANCO, VERDE_SCURO, VERDE_SCURO),
    },
    'bottone': {'raggio': 2, 'pad': (16, 32, 16, 32), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Sfondo diverso a telefono (specifica 7, H1 e H6): il motore non ha la chiave, la aggiungo qui senza toccarne la logica.
# In Elementor è l'impostazione nativa "Sfondo, immagine" del punto di rottura Mobile (background_image_mobile): così
# all'import anche questa foto entra nella libreria media. Nel fallback HTML la stessa foto arriva dal CSS della sezione,
# con un selettore che esiste solo lì (.avs-con è la classe dei contenitori del fallback).
_el_settings_motore = m.el_settings


def _el_settings(n, inner):
    s = _el_settings_motore(n, inner)
    if n.kind == 'container' and n.p.get('img_m'):
        s['background_image_mobile'] = m._img(n.p['img_m'], n.p.get('alt', ''))
        if n.p.get('img_pos_m'):
            s['background_position_mobile'] = n.p['img_pos_m']
    return s


m.el_settings = _el_settings


def sfondo_telefono(classe, url, posizione):
    """CSS del fallback per lo sfondo del telefono (in Elementor lo fa background_image_mobile)."""
    return (f'@media (max-width:767px){{.avs-con.{classe}{{background-image:url("{url}")!important;'
            f'background-position:{posizione}!important}}}}')


# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/AlbergoVescovi-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati dell'albergo (01-analisi-sito-attuale.md; un solo posto da aggiornare)
# ---------------------------------------------------------------------------------------------
NBSP = ' '
TEL = f'0424{NBSP}462614'
TEL_LINK = 'tel:+390424462614'
FAX = f'0424{NBSP}462840'
EMAIL = 'info@albergovescovi.com'
PEC = 'albergovescovifabiosrl@pec.it'
INDIRIZZO = 'Via Don G. Viero 80'
CAP_CITTA = '36012 Asiago (VI)'
RAGIONE_SOCIALE = 'Albergo Vescovi Fabio S.r.l.'
PIVA = '04435970241'
SDI = 'WTYVJK9'
CIN = 'IT024009A19GB3I2IC'
FACEBOOK = 'https://www.facebook.com/AlbergoVescovi'
# motore di prenotazione Persefone usato oggi dall'albergo: il nuovo sito ci manda le prenotazioni, non lo sostituisce
PRENOTA = 'https://www.booking-engine.it/Scripts/index.pl?hotel_id=53'
MAPPA = 'https://www.google.com/maps/search/?api=1&query=45.86642%2C11.50932'
MAPPA_HTML = MAPPA.replace('&', '&amp;')

VOCI_MENU = [('camere', '/camere/'), ('ristorante', '/ristorante/'), ('centro benessere', '/centro-benessere/'),
             ('contatti', '/contatti/')]


# ---------------------------------------------------------------------------------------------
# Componenti riutilizzabili
# ---------------------------------------------------------------------------------------------
CSS_SR = ('.avs-sr{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;'
          'clip-path:inset(50%)!important;white-space:nowrap!important;margin:0!important;padding:0!important}')


def sezione(*children, **p):
    """Sezione a tutta larghezza (nessun riquadro di 1280: i margini sono il token 'lato')."""
    p.setdefault('boxed', False)
    p.setdefault('gap', '0')
    p.setdefault('bg', BIANCO)
    return C(*children, tag='section', **p)


def stile(css):
    """Foglio di stile della sezione: un widget HTML senza contenuto (va in un contenitore con gap 0)."""
    return RAW('', css=css)


def nascosto(testo):
    """Frase per i lettori di schermo al posto del testo alternativo degli sfondi (Elementor non lo ha)."""
    return T(f'<p>{testo}</p>', style='small', color=INCHIOSTRO, css='avs-sr')


def link_testo(testo, url, colore=VERDE, hover=INCHIOSTRO, **p):
    """Link nel testo: verde 500, sottolineato; in hover inchiostro con la sottolineatura di 2 px. Niente frecce."""
    classi = ('avs-link ' + p.pop('css', '')).strip()
    return T(f'<p><a href="{url}">{testo}</a></p>', style='link', color=colore, link_color=colore, link_hover=hover,
             css=classi, **p)


CSS_LINK = ('.avs-link a:hover,.avs-link a:focus-visible{text-decoration-thickness:2px!important}'
            '.avs-link a{text-underline-offset:.24em!important}')


def foto(nome, alt, rapporto, chiave, nome_telefono=None, rapporto_telefono=None, posizione='50% 50%',
         posizione_telefono=None):
    """Foto a filo con il suo rapporto (aspect-ratio) a ogni larghezza, mai oltre la misura nativa.
    Con nome_telefono, sotto 768 px si vede un altro ritaglio (due widget Immagine, uno nascosto per punto di rottura).
    Ritorna (nodi, css)."""
    r = rapporto.replace(':', '/')
    css = (f'.avs-f-{chiave} img{{display:block;width:100%!important;max-width:100%!important;height:auto!important;'
           f'aspect-ratio:{r};object-fit:cover;object-position:{posizione}}}')
    nodi = [I(img(nome), alt, css=f'avs-foto avs-f-{chiave}', hide=['mobile'] if nome_telefono else None)]
    if nome_telefono:
        rt = (rapporto_telefono or rapporto).replace(':', '/')
        css += (f'.avs-f-{chiave}-t img{{display:block;width:100%!important;max-width:100%!important;height:auto!important;'
                f'aspect-ratio:{rt};object-fit:cover;object-position:{posizione_telefono or posizione}}}')
        nodi.append(I(img(nome_telefono), alt, css=f'avs-foto avs-f-{chiave}-t', hide=['desktop', 'tablet']))
    elif rapporto_telefono:
        css += f'@media (max-width:767px){{.avs-f-{chiave} img{{aspect-ratio:{rapporto_telefono.replace(":", "/")}}}}}'
    return nodi, css


def riga_foto(foto_nodo, testo_nodi, lato_foto='destra', w_foto=(50, 50, 100), align=('start', 'start', 'stretch'),
              pad=('sezione', 0, 0, 0), gap_testo=(72, 48, 24), css_sezione='', **p):
    """Foto a filo di un bordo della finestra e testo accanto (specifica 19): il contenitore non ha margini laterali,
    la foto ha la sua percentuale della finestra e non si restringe, la colonna del testo porta il gap verso la foto e il
    margine 'lato' verso l'altro bordo. A telefono la foto viene prima, a tutta larghezza, e il testo sotto con i margini."""
    colonna_foto = C(foto_nodo, w=w_foto, fisso=True, gap='0')
    if lato_foto == 'destra':
        pad_testo = (0, (gap_testo[0], gap_testo[1], 24), 0, ('lato', 'lato', 24))
        figli, dir_m = [None, colonna_foto], 'column-reverse'
    else:
        pad_testo = (0, ('lato', 'lato', 24), 0, (gap_testo[0], gap_testo[1], 24))
        figli, dir_m = [colonna_foto, None], 'column'
    colonna_testo = C(*testo_nodi, grow=True, gap='0', pad=pad_testo)
    figli[figli.index(None)] = colonna_testo
    if css_sezione:
        figli.append(stile(css_sezione))
    return sezione(*figli, dir='row', dir_m=dir_m, align=align, pad=pad, gap=(0, 0, 32), **p)


def riga_date(pad=('xl', 'lato')):
    """Riga delle date (specifica 4.6): una domanda, un bottone verso il motore Persefone, il telefono."""
    return sezione(
        H('Quando arrivate?', 'h2', style='domanda', color=VERDE, fisso=True),
        B('Scegli le date', PRENOTA, variant='primario', full_m=True, fisso=True),
        T(f'<p>oppure chiamate lo <a href="{TEL_LINK}">{TEL}</a></p>', style='nota', color=NOTA, link_color=INCHIOSTRO,
          link_hover=VERDE, css='avs-date-tel'),
        stile('.avs-date-tel a{white-space:nowrap;font-variant-numeric:tabular-nums lining-nums;'
              'text-underline-offset:.22em!important}'
              '.avs-date-tel a:hover,.avs-date-tel a:focus-visible{text-decoration-thickness:2px!important}'),
        dir='row', dir_m='column', wrap=(True, True, False), align=('center', 'center', 'stretch'),
        gap=(32, 32, 16), gap_r=(16, 16, 16), pad=pad, css='avs-date')


# ---------------------------------------------------------------------------------------------
# Testata e piede (template separati; con Ultimate Addons diventano header e footer di tutto il sito)
# ---------------------------------------------------------------------------------------------
# CSS solo per Elementor: il tema Hello, il menu di Ultimate Addons, la testata fissa
CSS_ELEMENTOR = (
    'html{scroll-padding-top:96px}'
    'body{font-variant-numeric:lining-nums;font-synthesis:none}'
    '#masthead{position:sticky;top:0;z-index:100;background:#FFFFFF}'
    'body.admin-bar #masthead{top:32px}'
    '@media (max-width:782px){body.admin-bar #masthead{top:0}}'
    f'a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,'
    f'summary:focus-visible{{outline:2px solid {VERDE};outline-offset:3px}}'
    '.avs-testata{overflow-x:clip}'
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}'
    '.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    # menu di Ultimate Addons: su una riga, in minuscolo come nel prototipo, voce attiva in verde
    '@media (min-width:1025px){.avs-testata .hfe-nav-menu__layout-horizontal .hfe-nav-menu{flex-wrap:nowrap}'
    '.avs-testata .hfe-nav-menu .hfe-menu-item{white-space:nowrap}}'
    '.avs-testata .hfe-nav-menu a.hfe-menu-item{text-transform:lowercase!important}'
    f'.avs-testata .hfe-nav-menu .current-menu-item>a.hfe-menu-item{{color:{VERDE}!important}}'
    f"a.hfe-skip-link:focus,.skip-link:focus{{background:{VERDE};color:{BIANCO};border-radius:0;box-shadow:none;"
    f"outline:2px solid {BIANCO};outline-offset:-4px;font:500 17px/1 {PILA};text-decoration:none;padding:16px 24px}}"
)

# CSS di testata comune a Elementor e fallback
CSS_TESTATA = (
    CSS_SR +
    '.avs-header{position:sticky;top:0;z-index:100}'
    '.avs-tel a{white-space:nowrap;font-variant-numeric:tabular-nums lining-nums}'
    f'.avs-tel a:hover,.avs-tel a:focus-visible{{color:{VERDE}!important;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:.3em!important}'
    # da 1024 in giù: logo a sinistra, telefono, Prenota e icona del menu a destra
    '@media (max-width:1024px){.avs-testata .avs-nav{order:3}.avs-testata .avs-azioni{margin-left:auto!important}}'
)


def header():
    logo = I(img('logo-tondo-120.png'), 'Hotel Vescovi, tre stelle', link='/', w_img=(60, 54, 46), fisso=True,
             link_label='Albergo Vescovi, pagina iniziale')
    menu = MENU(VOCI_MENU, colore=INCHIOSTRO, colore_hover=VERDE, accento=VERDE, fondo_menu=BIANCO, linea=FILETTO,
                stile='nav', stile_mobile='nav', spazio=48, pad_v=8, distanza=18, align_menu='center', fisso=True,
                larg=(None, 40, 40), css='avs-nav')
    azioni = C(
        T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='nav', color=INCHIOSTRO, link_color=INCHIOSTRO,
          link_hover=VERDE, sottolinea=False, fisso=True, css='avs-tel'),
        B('Prenota', PRENOTA, variant='primario', fisso=True),
        dir='row', align='center', gap=(32, 24, 24), fisso=True, hide=['mobile'], css='avs-azioni')
    testata = C(logo, menu, azioni, dir='row', justify=('between', 'start', 'between'), align='center',
                gap=(32, 24, 16), min_h=(88, 80, 66), pad=(0, 'lato'), bg=BIANCO, boxed=False, css='avs-testata')
    return C(testata, RAW('', css=CSS_ELEMENTOR, solo_elementor=True), RAW('', css=CSS_TESTATA), pad='0', gap='0',
             boxed=False, tag='header', bg=BIANCO)


CSS_PIEDE = (
    # fascia verde dei recapiti: bianco, senza sottolineatura; in hover salvia sottolineato
    '.avs-recapito a{white-space:nowrap;font-variant-numeric:tabular-nums lining-nums}'
    f'.avs-recapito a:hover,.avs-recapito a:focus-visible{{color:{SALVIA}!important;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:.2em!important}'
    f'.avs-recapiti a:focus-visible{{outline-color:{BIANCO}!important}}'
    # piede bianco
    f'.avs-piede strong{{font-weight:500;color:{INCHIOSTRO}}}'
    f'.avs-piede a:hover,.avs-piede a:focus-visible{{color:{VERDE}!important;text-decoration:underline!important;'
    'text-underline-offset:.2em!important}'
    '.avs-piede-tel{white-space:nowrap;font-variant-numeric:tabular-nums lining-nums}'
    # a tablet la colonna della società va sotto, dalla seconda colonna (logo 76 + spazio 48)
    '@media (min-width:768px) and (max-width:1024px){.avs-piede-societa{margin-left:124px!important}}'
    # barra Chiama e Prenota del telefono
    '.avs-barra{display:none}'
    '@media (max-width:767px){body{padding-bottom:56px}'
    '.avs-barra{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:200;height:56px;background:#FFFFFF;'
    'box-shadow:0 -1px 0 rgba(32,39,27,.14)}'
    f".avs-barra a{{flex:1 1 50%;display:flex;align-items:center;justify-content:center;text-decoration:none;"
    f"font:500 18px/1.2 {PILA};transition:background-color .15s}}"
    f'.avs-barra a.avs-barra-chiama{{color:{VERDE};background:{BIANCO}}}'
    f'.avs-barra a.avs-barra-chiama:hover,.avs-barra a.avs-barra-chiama:focus-visible{{color:{VERDE};background:{SALVIA}}}'
    f'.avs-barra a.avs-barra-prenota{{color:{BIANCO};background:{VERDE}}}'
    f'.avs-barra a.avs-barra-prenota:hover,.avs-barra a.avs-barra-prenota:focus-visible{{color:{BIANCO};background:{VERDE_SCURO}}}'
    f'.avs-barra a:focus-visible{{outline:2px solid {VERDE};outline-offset:-4px}}'
    '.avs-js .avs-barra{visibility:hidden}.avs-js .avs-barra.avs-vista{visibility:visible}}'
)

# in home la barra compare quando la riga delle date (che ha già il suo bottone) è uscita in alto,
# nelle altre pagine dopo 480 px di scorrimento; senza JavaScript è sempre visibile
JS_BARRA = (
    "(function(){document.documentElement.classList.add('avs-js');"
    "function go(){var b=document.querySelector('.avs-barra');if(!b)return;var d=document.querySelector('.avs-date');"
    "function up(){var v=d?d.getBoundingClientRect().bottom<0:(window.pageYOffset||0)>480;b.classList.toggle('avs-vista',v)}"
    "window.addEventListener('scroll',up,{passive:true});window.addEventListener('resize',up);up()}"
    "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',go)}else{go()}})();"
)
HTML_BARRA = (f'<nav class="avs-barra" aria-label="Chiama o prenota"><a class="avs-barra-chiama" href="{TEL_LINK}">Chiama</a>'
              f'<a class="avs-barra-prenota" href="{PRENOTA}">Prenota</a></nav><script>{JS_BARRA}</script>')


def footer():
    def recapito(html):
        return T(f'<p>{html}</p>', style='tel', color=BIANCO, link_color=BIANCO, link_hover=SALVIA, sottolinea=False,
                 fisso=True, css='avs-recapito')
    recapiti = C(
        recapito(f'<a href="{TEL_LINK}">{TEL}</a>'),
        recapito(f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
        recapito(f'<a href="{MAPPA_HTML}">{INDIRIZZO}, Asiago</a>'),
        dir='row', dir_m='column', wrap=(False, True, False), align=('center', 'center', 'start'),
        gap=(112, 72, 16), gap_r=(16, 16, 16), pad=('xl', 'lato'), bg=VERDE, boxed=False, css='avs-recapiti')

    def colonna(html, w, css=None):
        return C(T(html, style='small', color=NOTA, link_color=NOTA, link_hover=VERDE, sottolinea=False), w=w, gap='0',
                 css=css)
    voci = [('Camere', '/camere/'), ('Ristorante', '/ristorante/'), ('Centro benessere', '/centro-benessere/'),
            ('Contatti', '/contatti/'), ('Contributi', '/contributi/'), ('Privacy', '/privacy/'), ('Cookie', '/cookie/')]
    elenco = '<br>'.join(f'<a href="{u}">{t}</a>' for t, u in voci) + f'<br><a href="{FACEBOOK}">Facebook</a>'
    griglia = C(
        I(img('logo-tondo-152.png'), 'Hotel Vescovi', w_img=(76, 76, 76), fisso=True),
        colonna(f'<p><strong>Albergo Vescovi</strong><br>{INDIRIZZO}<br>{CAP_CITTA}<br>'
                f'Tel. <a class="avs-piede-tel" href="{TEL_LINK}">{TEL}</a><br>Fax <span class="avs-piede-tel">{FAX}</span><br>'
                f'<a href="mailto:{EMAIL}">{EMAIL}</a></p>', (20, 34, 100)),
        colonna(f'<p>{elenco}</p>', (20, 34, 100)),
        colonna(f'<p><strong>{RAGIONE_SOCIALE}</strong><br>P.IVA e C.F. {PIVA}<br>Codice SDI {SDI}<br>PEC {PEC}<br>'
                f'CIN {CIN}</p>', (27, 70, 100), css='avs-piede-societa'),
        dir='row', dir_m='column', wrap=(False, True, False), gap=(72, 48, 32), gap_r=(48, 48, 32), justify='start')
    contributi = C(
        I(img('loghi-contributi.png'), 'Cofinanziato dall’Unione europea, Repubblica italiana, Regione del Veneto, '
          'Sviluppo rurale Veneto 2023-2027, GAL Montagna Vicentina', w_img=(344, 344, 344), fisso=True),
        T('<p><a href="/contributi/#csr-2023-2027">Sviluppo rurale, CSR 2023-2027</a><br>'
          '<a href="/contributi/#por-fesr">Progetto POR FESR 2014-2020</a></p>', style='small', color=NOTA,
          link_color=NOTA, link_hover=VERDE, sottolinea=False),
        dir='row', dir_m='column', align=('center', 'center', 'start'), gap=(48, 48, 24), mt=(48, 48, 32))
    piede = C(griglia, contributi,
              T(f'<p>© 2026 {RAGIONE_SOCIALE}</p>', style='small', color=NOTA, mt=(32, 32, 32)),
              pad=(72, 'lato', (48, 48, 104), 'lato'), gap='0', boxed=False, bg=BIANCO, css='avs-piede')
    return C(recapiti, piede, RAW(HTML_BARRA, css=CSS_PIEDE), pad='0', gap='0', boxed=False, tag='footer', bg=BIANCO)


# ---------------------------------------------------------------------------------------------
# HOME (specifica, paragrafo 7: il prototipo approvato con le correzioni del paragrafo 2)
# ---------------------------------------------------------------------------------------------
CSS_APERTURA = (
    CSS_SR +
    # alta quanto la finestra sotto la testata, fra 600 e 1000 px; sopra 1870 px non si allarga (la foto è di 1870)
    '.avs-apertura{height:clamp(600px,calc(100vh - 88px),1000px);max-width:1870px!important;'
    'margin-left:auto!important;margin-right:auto!important}'
    '.avs-display,.avs-display .elementor-heading-title{letter-spacing:-.022em!important;white-space:nowrap}'
    # fra 1025 e 1439 il titolo scala con la finestra; sotto 1280 la riga va sotto il titolo, come a tablet
    '@media (min-width:1025px) and (max-width:1439px){.avs-display,.avs-display .elementor-heading-title'
    '{font-size:max(112px,11.4vw)!important}}'
    '@media (min-width:1025px) and (max-width:1279px){.avs-apertura-testo{flex-direction:column!important;'
    'align-items:flex-start!important;gap:16px!important}.avs-apertura-riga{width:auto!important;max-width:none!important;'
    'margin-bottom:0!important}}'
    '@media (max-width:1024px){.avs-apertura{height:clamp(600px,calc(100vh - 80px),1000px)}}'
    '@media (max-width:767px){.avs-apertura{height:clamp(560px,calc(100svh - 66px),820px)}'
    '.avs-apertura::before{background-image:linear-gradient(180deg,rgba(18,26,12,0) 52%,rgba(18,26,12,.42) 100%)!important}'
    '.avs-display,.avs-display .elementor-heading-title{letter-spacing:-.02em!important;line-height:.92!important;'
    'white-space:normal}}'
)


def home_apertura():
    titolo = H('Sulla Piana Ave', 'h1', style='display', color=BIANCO, fisso=True, css='avs-display')
    riga = T('<p>L’albergo è l’edificio giallo in mezzo al prato. Il centro di Asiago è a 900&nbsp;metri.</p>',
             style='lead', color=BIANCO, max_w=(310, 900, 360), mb=(16, 0, 0), css='avs-apertura-riga')
    testo = C(titolo, riga, dir='row', dir_t='column', justify=('between', 'start', 'start'),
              align=('end', 'start', 'start'), gap=(48, 16, 16), css='avs-apertura-testo')
    return sezione(
        nascosto('L’Albergo Vescovi d’estate: la casa gialla con i balconi in legno sul prato della Piana Ave.'),
        testo, stile(CSS_APERTURA + sfondo_telefono('avs-apertura', img('apertura-prato-telefono.jpg'), '50% 100%')),
        img=img('apertura-prato.jpg'), img_pos='30% 100%', img_m=img('apertura-prato-telefono.jpg'),
        img_pos_m='50% 100%', bg=PRATO,
        alt='L’Albergo Vescovi d’estate, la casa gialla con i balconi in legno sul prato della Piana Ave',
        scrim=(58, 0, 0.40), overlay_color=VELO, justify='end', min_h=(600, 600, 560),
        pad=(0, 'lato', (48, 32, 32), 'lato'), anchor='content', css='avs-apertura e-no-lazyload')


def home_camere():
    nodi, css = foto('camera-abete.jpg', 'Camera con le pareti in abete, due finestre con le tende chiare e il letto '
                     'matrimoniale', '1440:780', 'camera', nome_telefono='camera-abete-telefono.jpg',
                     rapporto_telefono='1:1')
    testo = C(H('Doppie, triple e quadruple, alcune col balcone sui&nbsp;prati', 'h2', color=VERDE, max_w=(630, 540, 540)),
              link_testo('Le camere', '/camere/', mt='m'), pad=('xl', 'lato', 0, 'lato'), gap='0')
    return sezione(*nodi, testo, stile(css + CSS_LINK), pad=(('xxl', 'xxl', 'l'), 0, 0, 0), anchor='camere')


def home_ristorante():
    nodi, css = foto('tavola-prati.jpg', 'Tagliatelle ai funghi, pane e vino rosso su un tavolo accanto alla vetrata; '
                     'fuori, i prati e le colline', '4:5', 'tavola', posizione='50% 50%')
    testo = [
        H('A tavola, con i&nbsp;prati alla finestra', 'h2', color=VERDE, max_w=(513, 513, 513), mt=(-6, -5, 0)),
        T('<p>Cucina tradizionale: spezzatino con polenta, stinco con patate, soppressa con polenta e formaggio, '
          'tagliatelle ai funghi.</p>', style='body', color=INCHIOSTRO, max_w=(513, 513, 513), mt='l'),
        link_testo('Il ristorante', '/ristorante/', mt='m'),
    ]
    return riga_foto(nodi[0], testo, lato_foto='destra', w_foto=(50, 50, 100), align=('start', 'start', 'stretch'),
                     pad=('sezione', 0, 0, 0), css_sezione=css + CSS_LINK, anchor='ristorante')


def home_benessere():
    nodi, css = foto('sauna-panche-stufa.jpg', 'La sauna finlandese: le panche in legno e la stufa', '4:3', 'sauna')
    testo = [
        H('Dalle 15 alle 19, sauna e bagno&nbsp;turco', 'h2', color=VERDE, max_w=(475, 475, 475)),
        T('<p>Con la vasca idromassaggio, le docce emozionali e la tisaneria. Dopo la sauna c’è il secchio tirolese: si '
          'tira la catenella e arriva l’acqua gelata.</p>', style='body', color=INCHIOSTRO, max_w=(475, 475, 475), mt='l'),
        T('<p>Per chi dorme in albergo, su prenotazione. 10&nbsp;euro, accappatoio e ciabatte compresi.</p>', style='nota',
          color=NOTA, max_w=(475, 475, 475), mt='m'),
        link_testo('Il centro benessere', '/centro-benessere/', mt='m'),
    ]
    return riga_foto(nodi[0], testo, lato_foto='sinistra', w_foto=(56, 54, 100), align=('end', 'end', 'stretch'),
                     pad=('sezione', 0, 'sezione', 0), css_sezione=css + CSS_LINK, anchor='benessere')


CSS_INVERNO = (
    CSS_SR +
    '.avs-h2c,.avs-h2c .elementor-heading-title{letter-spacing:-.016em!important}'
)


def home_inverno():
    riga = '<p>L’albergo apre per stagioni e, su prenotazione, anche negli altri periodi dell’anno.</p>'
    foto_inverno = C(
        nascosto('L’albergo e il paese d’inverno, dal prato innevato.'),
        H('D’inverno, lo&nbsp;stesso&nbsp;prato', 'h2', style='h2_chiusura', color=VERDE, css='avs-h2c'),
        T(riga, style='inverno', color=VERDE, max_w=(437, 414, 414), mt='m', hide=['mobile']),
        img=img('inverno-prato.jpg'), img_pos='center top', img_m=img('inverno-prato-telefono.jpg'),
        img_pos_m='center top', bg=NEVE,
        alt='L’albergo e il paese d’inverno, dal prato innevato', min_h=(800, 569, 437),
        pad=((472, 300, 206), 'lato', 0, 'lato'), justify='start', gap='0', boxed=False, css='avs-inverno e-no-lazyload')
    # a telefono la riga esce dalla foto e va sotto, su bianco
    dopo = C(T(riga, style='inverno', color=VERDE), pad=('m', 'lato', 'xl', 'lato'), gap='0', hide=['desktop', 'tablet'])
    return sezione(foto_inverno, dopo,
                   stile(CSS_INVERNO + sfondo_telefono('avs-inverno', img('inverno-prato-telefono.jpg'), 'center top')))


def home():
    return [('apertura', home_apertura()), ('date', riga_date()), ('camere', home_camere()),
            ('ristorante', home_ristorante()), ('benessere', home_benessere()), ('inverno', home_inverno())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Albergo Vescovi, tre stelle ad Asiago sulla Piana Ave',
     'descrizione': 'Albergo Vescovi, tre stelle ad Asiago, sul prato della Piana Ave a 900 metri dal centro: camere, '
                    'ristorante di cucina tradizionale, sauna e bagno turco.'},
]
