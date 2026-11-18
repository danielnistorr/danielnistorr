# -*- coding: utf-8 -*-
"""
Contenuti del sito Hotel Garibaldi (A.L.P. S.r.l.), Via San Marco 63, Ponte di Brenta, Padova.

Idea (specifica _prova/spec.md, paragrafo 1): l'albergo mostrato un oggetto alla volta, grande sul bianco, con una frase che
dice al cliente cosa ottiene. In home l'oggetto è la chiave (i portachiavi in cuoio rosso con il monogramma GH); il rosso
pompeiano delle pareti e dei portachiavi compare come campo pieno una volta per pagina, solo per prenotare.
La home riproduce il prototipo approvato dal committente (_prova/direzioni/oggetto/proto.html) con le correzioni D1-D6
della specifica (logo monocromo, larghezze in percentuale con la misura nativa come massimo, aree di tocco, breakpoint
di Elementor, scala delle spaziature, fatti non verificati).

Carattere: Spectral 400 e 500, una famiglia (guida CARATTERI-E-SEGNALI-IA, c3: riferimento Hotel Schwarzschmied, Livory;
menu in maiuscolo piccolo spaziato come Schwarzschmied). Palette: bianco, ardesia #1E2631 (la lamiera della facciata),
rosso pompeiano #8A2E33 (pareti, passatoia, portachiavi).
Fonti dei testi: 01-analisi-sito-attuale.md (testi verbatim 1-29, dati aziendali), scheda della Regione del Veneto;
quello che non è verificabile è nel paragrafo 17 della specifica, da copiare nel LEGGIMI.
"""
from urllib.parse import quote

import motore as m
from motore import C, B, I, RAW, MENU

PREFISSO = 'hgr'
NOME_SITO = 'Hotel Garibaldi'

# ---------------------------------------------------------------------------------------------
# Tema (specifica, paragrafo 2)
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'
ARDESIA = '#1E2631'        # inchiostro: la lamiera della facciata scurita, 15,25:1 sul bianco
TESTO2 = '#5A6270'         # didascalie, note, riga legale: 6,15:1 sul bianco
ROSSO = '#8A2E33'          # rosso pompeiano: bottone, campo pieno, stati; bianco sopra 8,34:1
ROSSO_SCURO = '#702328'    # hover del bottone rosso; bianco sopra 10,71:1
SU_ROSSO2 = '#F1D7D5'      # testo secondario sul rosso: 6,12:1
FILETTO = '#D9DCE0'        # l'unico filetto del sito (sopra la riga legale) e i bordi dei campi del modulo
GRIGIO_DIS = '#D9DCE0'     # bottone disabilitato

SPECTRAL = 'Spectral'


def _st(f, w, s, lh, ls=0.0, up=False):
    return dict(f=f, w=w, s=s, lh=lh, ls=ls, up=up)


TEMA = {
    'nome': 'Oggetto',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': ARDESIA, 'testo2': TESTO2, 'accento': ROSSO,
    'filetto': FILETTO, 'filetto_scuro': FILETTO, 'su_scuro2': SU_ROSSO2,
    'scuro': ARDESIA, 'su_scuro': BIANCO, 'su_accento': BIANCO,
    'font_titoli': SPECTRAL, 'font_testo': SPECTRAL, 'larghezza': 1440,
    'google_fonts': 'https://fonts.googleapis.com/css?family=Spectral:400,500&display=swap',
    # _st(famiglia, peso, (1440, 1024, 390), interlinea, spaziatura in px, maiuscolo)
    'stili': {
        'display': _st(SPECTRAL, '400', (104, 72, 46), 1.0, -1.5),     # il solo elemento grande della pagina
        'h1':      _st(SPECTRAL, '400', (56, 46, 34), 1.08, -0.5),
        'h2r':     _st(SPECTRAL, '400', (58, 46, 34), 1.06, -0.8),     # titolo sul campo rosso
        'h2':      _st(SPECTRAL, '400', (44, 36, 30), 1.12, -0.4),
        'h2b':     _st(SPECTRAL, '400', (40, 34, 29), 1.14, -0.2),
        'h3':      _st(SPECTRAL, '500', (22, 21, 20), 1.3),
        'lead':    _st(SPECTRAL, '400', (24, 21, 20), 1.5),
        'body':    _st(SPECTRAL, '400', (19, 18, 18), 1.6),
        'prezzo':  _st(SPECTRAL, '400', (19, 18, 18), 1.4),
        'small':   _st(SPECTRAL, '400', (15, 15, 15), 1.5),
        'legale':  _st(SPECTRAL, '400', (14, 14, 14), 1.6),
        'piede':   _st(SPECTRAL, '400', (16, 16, 16), 1.6),
        'tel':     _st(SPECTRAL, '400', (30, 26, 26), 1.2, -0.15),
        'tel_r':   _st(SPECTRAL, '400', (32, 32, 28), 1.2),
        'tel_t':   _st(SPECTRAL, '400', (18, 18, 18), 1.2),            # telefono nella testata
        'link':    _st(SPECTRAL, '500', (17, 17, 17), 1.4),
        'nav':     _st(SPECTRAL, '500', (13, 13, 13), 1.2, 1.8, True),  # +0,14em, come il menu di Schwarzschmied
        'btn':     _st(SPECTRAL, '500', (13, 13, 13), 1.2, 1.8, True),
        'nav_m':   _st(SPECTRAL, '400', (22, 22, 22), 1.3),
        'campo':   _st(SPECTRAL, '500', (15, 15, 15), 1.3),
    },
    # una sola scala (px a 1440, 1024, 390): 8, 16, 24, 32, 48, 64, 96, 128, 160
    'spazi': {
        'sezione': (160, 128, 96), 'xl': (128, 96, 96), 'l': (96, 64, 64), 'col': (64, 48, 32), 'm': (48, 32, 32),
        's': (32, 32, 32), 'xs': (24, 24, 24), 'xxs': (16, 16, 16), 'min': (8, 8, 8), 'lato': (64, 48, 24), '0': (0, 0, 0),
    },
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): sempre colore pieno, mai opacità
    'bottoni': {
        'primario': (BIANCO, ROSSO, ROSSO, BIANCO, ROSSO_SCURO, ROSSO_SCURO),
        'chiaro': (ROSSO, BIANCO, BIANCO, BIANCO, ARDESIA, ARDESIA),       # sul campo rosso
    },
    'bottone': {'raggio': 0, 'pad': (16, 24, 16, 24), 'bordo': 0, 'stile': 'btn'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/HotelGaribaldi-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def H(text, level='h2', style=None, color=None, **p):
    """Titolo: in motore il colore predefinito è il NERO di Benvegnù (legato all'import), qui l'ardesia."""
    return m.H(text, level, style, color or ARDESIA, **p)


def T(html, style='body', color=None, **p):
    return m.T(html, style, color or ARDESIA, **p)


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati (un solo posto da aggiornare; fonti in 01-analisi-sito-attuale.md, "Dati aziendali")
# ---------------------------------------------------------------------------------------------
NB = ' '                                  # spazio indivisibile
TEL = f'049{NB}893{NB}24{NB}66'
TEL_LINK = 'tel:+390498932466'
TEL_EN = f'+39{NB}049{NB}893{NB}24{NB}66'
FAX = f'049{NB}893{NB}24{NB}63'
EMAIL = 'info@hotelgaribaldi.com'
INDIRIZZO = f'Via San Marco{NB}63'
CAP_CITTA = '35129 Padova'                     # [DA CONFERMARE] il CAP: il sito scrive 35129, la Regione 35020
RAGIONE = 'A.L.P. S.r.l.'                      # [DA CONFERMARE] che A.L.P. S.r.l. gestisca l'albergo
PIVA = '02209920285'
REA = 'PD-214632'
CAPITALE = f'60.000{NB}euro'
PEC = 'a.l.p.srl@pec.it'                       # [DA CONFERMARE] su INI-PEC
CIN = 'IT028060A173Q36JDQ'


# Sopra 1440 px ogni sezione è un contenitore di 1440 centrato. In Elementor il margine laterale (padding) sta fuori dalla
# larghezza "boxed": per avere a 1920 gli stessi allineamenti di 1440 la larghezza boxed è 1440 meno i margini.
W_TESTO = 1312     # margine di 64 a sinistra e a destra (testata, piede, titoli)
W_FILO = 1376      # foto a filo di un bordo, margine di 64 solo dall'altro lato
W_PIENO = 1440     # campo rosso: foto a filo, margine dentro la colonna di testo


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    if corpo:
        url += '&body=' + quote(corpo)
    return url


# ---------------------------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------------------------
# solo Elementor: correzioni al tema Hello e a Ultimate Addons (nel fallback non servono)
CSS_BASE = (
    'body{font-synthesis:none}em,i,cite{font-style:normal}'
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    '.elementor-social-icon:hover{opacity:1}'
    # Ultimate Addons: voci su una riga, testata tagliata in orizzontale (il menu chiuso sporge a destra)
    '@media (min-width:1025px){.hfe-nav-menu__layout-horizontal .hfe-nav-menu{flex-wrap:nowrap}'
    '.hfe-nav-menu .hfe-menu-item{white-space:nowrap}}'
    '.hgr-testata{overflow-x:clip}'
    # niente segno animato sotto le voci: la voce attiva è rossa e sottolineata da 1 px a 6 px dal testo
    '.hgr-testata .hfe-nav-menu .menu-item a.hfe-menu-item:after,.hgr-testata .hfe-nav-menu .menu-item a.hfe-menu-item:before'
    '{display:none!important}'
    f'.hgr-testata .hfe-nav-menu .menu-item a.hfe-menu-item:hover,.hgr-testata .hfe-nav-menu .menu-item a.hfe-menu-item:focus-visible'
    f'{{color:{ROSSO}!important}}'
    f'.hgr-testata .hfe-nav-menu .current-menu-item>a.hfe-menu-item{{color:{ROSSO}!important;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:6px!important}'
    # il telefono è la prima voce del menu WordPress: solo nella tendina (su desktop è già a vista nella testata)
    '@media (min-width:1025px){.hgr-testata .hfe-nav-menu__layout-horizontal .menu-item.hgr-voce-tel,'
    '.hgr-testata .hfe-nav-menu__layout-horizontal .menu-item:has(>a[href^="tel:"]){display:none!important}}'
    '.hgr-testata .menu-item a[href^="tel:"]{font-variant-numeric:tabular-nums lining-nums}'
    # la voce "Menu" al posto dell'icona a tre linee; rossa a tendina aperta
    '.hgr-testata .hfe-nav-menu__toggle{margin:0!important}'
    f".hgr-testata .hfe-nav-menu-icon{{display:inline-flex!important;align-items:center;min-height:44px;padding:0 0 0 4px!important;"
    f"border:0!important;border-radius:0!important;background:transparent!important;color:{ARDESIA}!important;cursor:pointer}}"
    '.hgr-testata .hfe-nav-menu-icon svg,.hgr-testata .hfe-nav-menu-icon i{display:none!important}'
    f".hgr-testata .hfe-nav-menu-icon::before{{content:'Menu';font:500 13px/1.2 '{SPECTRAL}',Georgia,serif;letter-spacing:1.8px;"
    'text-transform:uppercase}'
    f'.hgr-testata .hfe-nav-menu-icon:hover,.hgr-testata .hfe-active-menu .hfe-nav-menu-icon,'
    f'.hgr-testata .hfe-nav-menu__toggle[aria-expanded=true] .hfe-nav-menu-icon{{color:{ROSSO}!important}}'
    # la tendina: pannello bianco a tutta larghezza sotto la testata, senza filetti, con un'ombra leggera
    '@media (max-width:1024px){'
    '.hgr-testata .hgr-menu{flex:0 0 auto!important;width:auto!important}'
    '.hgr-testata nav.hfe-dropdown{position:absolute!important;top:100%!important;margin-top:30px!important;border:0!important;'
    f'box-shadow:0 12px 24px rgba(30,38,49,.12)!important;background:{BIANCO}!important;padding:0!important}}'
    '.hgr-testata nav.hfe-dropdown ul.hfe-nav-menu{padding:16px 0 40px!important}'
    '.hgr-testata nav.hfe-dropdown li.menu-item{border:0!important}'
    '.hgr-testata nav.hfe-dropdown .menu-item a.hfe-menu-item{padding:8px 48px!important;border:0!important;'
    f'color:{ARDESIA}!important;background:{BIANCO}!important}}'
    f'.hgr-testata nav.hfe-dropdown .menu-item a.hfe-menu-item:hover{{color:{ROSSO}!important}}'
    f'.hgr-testata nav.hfe-dropdown .current-menu-item>a.hfe-menu-item{{color:{ROSSO}!important}}}}'
    '@media (max-width:767px){.hgr-testata nav.hfe-dropdown .menu-item a.hfe-menu-item{padding:8px 24px!important}'
    '.hgr-testata nav.hfe-dropdown{margin-top:16px!important}}'
    f"a.hfe-skip-link:focus{{background:{ARDESIA};color:{BIANCO};border-radius:0;box-shadow:none;outline:2px solid {BIANCO};"
    f"outline-offset:-4px;font:500 13px/1 '{SPECTRAL}',Georgia,serif;letter-spacing:1.8px;text-transform:uppercase;"
    'text-decoration:none;padding:16px 24px}'
)

# Elementor e fallback: regole comuni a tutte le pagine (stanno nella testata, presente in ogni pagina)
CSS_COMUNE = (
    'html body{font-synthesis:none}'
    # fuoco: contorno rosso pompeiano a 3 px; bianco sul campo rosso
    f'body a:focus-visible,body button:focus-visible,body summary:focus-visible,body input:focus-visible,'
    f'body select:focus-visible,body textarea:focus-visible,body [tabindex]:focus-visible'
    f'{{outline:2px solid {ROSSO}!important;outline-offset:3px!important}}'
    f'body .hgr-rosso a:focus-visible,body .hgr-rosso button:focus-visible{{outline-color:{BIANCO}!important}}'
    # link di testo: area di tocco di 44 px senza cambiare l'aspetto
    '.hgr-tap a{display:inline-block;padding:10px 0;margin:-10px 0}'
    # telefoni grandi (titoli con link): ardesia, hover rosso; sul rosso bianchi, hover sottolineato
    f'.hgr-tel a,.hgr-tel a:visited{{color:inherit!important;text-decoration:none!important}}'
    f'.hgr-tel a:hover{{color:{ROSSO}!important}}'
    f'.hgr-rosso .hgr-tel a:hover,.hgr-rosso .hgr-su-rosso a:hover{{color:{BIANCO}!important;text-decoration:underline!important;'
    'text-decoration-thickness:1px!important;text-underline-offset:5px!important}'
    '.hgr-tel,.hgr-tel a,.hgr-cifre{font-variant-numeric:tabular-nums lining-nums}'
    # testi del piede: link senza sottolineatura, al passaggio rossi e sottolineati; voci in colonna a 8 px
    f'.hgr-piede a{{text-decoration:none!important}}'
    f'.hgr-piede a:hover{{color:{ROSSO}!important;text-decoration:underline!important;text-decoration-thickness:1px!important;'
    'text-underline-offset:4px!important}'
    '.hgr-voci p{margin:0!important}.hgr-voci a{display:block;padding:4px 0}'
    '.hgr-voci-dx a{display:block;padding:4px 0}'
    '@media (max-width:1024px){.hgr-voci a,.hgr-voci-dx a{padding:9px 0}}'
    '.hgr-legale .hgr-nw{white-space:nowrap}'
)

# testata: telefono solo da 1280 px (tra 1025 e 1279 il menu non starebbe su una riga); "Menu" a destra di "Prenota"
CSS_TESTATA = (
    '@media (min-width:1025px) and (max-width:1279px){.hgr-tel-testata{display:none!important}}'
    f'.hgr-tel-testata a{{color:{ARDESIA}!important;text-decoration:none!important;white-space:nowrap}}'
    f'.hgr-tel-testata a:hover{{color:{ROSSO}!important}}'
    '@media (max-width:1024px){.hgr-testata .hgr-menu{order:3;flex-grow:0!important}'
    '.hgr-testata .hgr-btn-testata{margin-left:auto!important}}'
    '@media (max-width:767px){.hgr-btn-testata a,.hgr-btn-testata .elementor-button{padding:16px!important}}'
)

# fallback: il menu del generatore vestito come quello di Ultimate Addons (voce attiva, tendina, voce "Menu")
CSS_NAV_FALLBACK = (
    '.hgr-testata .hgr-con{position:static!important}.hgr-testata nav.hgr-w{position:static!important}'
    '.hgr-testata .hgr-nav-l{justify-content:center!important}'
    '.hgr-testata .hgr-nav-l a{border-bottom:0!important;padding:8px 0!important}'
    f'.hgr-testata .hgr-nav-l a:hover{{color:{ROSSO}!important}}'
    f'.hgr-testata .hgr-nav-l a[aria-current=page]{{color:{ROSSO}!important;text-decoration:underline;text-decoration-thickness:1px;'
    'text-underline-offset:6px}'
    '.hgr-testata .hgr-nav-l li:has(a[href^="tel:"]){display:none}'
    '.hgr-testata summary{min-width:0!important;padding:0 0 0 4px!important}'
    '.hgr-testata summary .hgr-ico{display:none!important}'
    f".hgr-testata summary::before{{content:'Menu';font:500 13px/1.2 '{SPECTRAL}',Georgia,serif;letter-spacing:1.8px;"
    f'text-transform:uppercase;color:{ARDESIA}}}'
    f'.hgr-testata summary:hover::before,.hgr-testata details[open] summary::before{{color:{ROSSO}}}'
    f'.hgr-testata details ul{{margin-top:0!important;top:100%!important;left:0!important;right:0!important;border:0!important;'
    f'background:{BIANCO}!important;padding:16px 0 40px!important;box-shadow:0 12px 24px rgba(30,38,49,.12)}}'
    f".hgr-testata details li a{{padding:8px 48px!important;font:400 22px/1.3 '{SPECTRAL}',Georgia,serif!important;"
    f'letter-spacing:0!important;text-transform:none!important;color:{ARDESIA}!important}}'
    f'.hgr-testata details li a:hover,.hgr-testata details li a[aria-current=page]{{color:{ROSSO}!important}}'
    '.hgr-testata details li a[href^="tel:"]{font-variant-numeric:tabular-nums lining-nums}'
    '@media (max-width:767px){.hgr-testata details li a{padding:8px 24px!important}}'
)

# Esc chiude la tendina (Ultimate Addons e fallback) e riporta il fuoco sulla voce "Menu"
JS_TESTATA = (
    "<script>document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;"
    "var t=document.querySelector('.hgr-testata .hfe-nav-menu__toggle[aria-expanded=true]');if(t){t.click();t.focus();}"
    "var d=document.querySelector('.hgr-testata details[open]');if(d){d.open=false;d.querySelector('summary').focus();}});</script>"
)

# home ed English: ritagli per breakpoint, ordine a telefono, didascalia che non sposta il dettaglio del bagno
CSS_OGGETTO = (
    # la chiave: a telefono la foto viene prima del titolo, ritagliata sul portachiavi grande
    '.hgr-chiave img{object-position:62% 50%}'
    '@media (min-width:1025px){.hgr-chiave img{height:auto!important;aspect-ratio:12/5;max-height:600px}}'
    '@media (min-width:768px) and (max-width:1024px){.hgr-chiave img{height:auto!important;aspect-ratio:1024/440}}'
    # il titolo d'apertura resta su una riga anche tra 1025 e 1439 px: scende da 104 px con la larghezza della finestra
    '@media (min-width:1025px) and (max-width:1439px){.hgr-apertura h1{font-size:min(104px,calc((100vw - 128px) / 11.6))!important}}'
    '@media (max-width:767px){.hgr-chiave{order:-1}.hgr-chiave img{object-position:84% 50%!important}}'
    # la camera: su desktop la didascalia sta sotto la foto senza allungare la riga, così il bagno è allineato al fondo
    '@media (min-width:1025px){.hgr-figura{position:relative!important}.hgr-figura .hgr-didascalia{position:absolute!important;'
    'left:0;top:100%;width:100%}}'
    # le statue: a telefono un ritaglio 390x420 al 40 % in verticale
    '@media (max-width:767px){.hgr-statue img{height:420px!important;object-fit:cover;object-position:50% 40%}}'
)


# ---------------------------------------------------------------------------------------------
# Componenti riutilizzabili
# ---------------------------------------------------------------------------------------------
def link_testo(testo, url, colore=ARDESIA, hover=ROSSO, **p):
    """Link di testo sottolineato (1 px a 5 px dal testo), senza freccia; area di tocco di 44 px."""
    classi = ('hgr-tap ' + p.pop('css', '')).strip()
    return T(f'<p><a href="{url}">{testo}</a></p>', style='link', color=colore, link_color=colore, link_hover=hover,
             css=classi, **p)


def telefono(stile='tel', colore=ARDESIA, numero=TEL, **p):
    """Il numero di telefono come testo grande cliccabile (titolo-paragrafo con link tel:)."""
    classi = ('hgr-tel ' + p.pop('css', '')).strip()
    return H(numero, 'p', style=stile, color=colore, link=TEL_LINK, css=classi, **p)


def email(colore=ARDESIA, hover=ROSSO, stile='body', **p):
    return T(f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>', style=stile, color=colore, link_color=colore, link_hover=hover,
             sottolinea=False, **p)


def testo(html, stile='body', colore=ARDESIA, **p):
    return T(html if html.startswith('<') else f'<p>{html}</p>', style=stile, color=colore, link_color=colore, **p)


def blocco_titolo_testo(titolo, corpo, link=None, stile_titolo='h2'):
    """Titolo, testo e link nella stessa colonna (mai titolo a sinistra e testo a destra)."""
    figli = [H(titolo, 'h2', style=stile_titolo), testo(corpo, mt='xs')]
    if link:
        figli.append(link_testo(link[0], link[1], mt='xs'))
    return C(*figli, gap='0')


# ---------------------------------------------------------------------------------------------
# Testata e piede (template separati; con Ultimate Addons diventano testata e piede di tutto il sito)
# ---------------------------------------------------------------------------------------------
VOCI_MENU = [('L’albergo', '/albergo/'), ('Camere e prezzi', '/camere/'), ('Dove siamo', '/dove-siamo/'),
             ('English', '/en/')]


def header():
    marchio = I(img('logo-ardesia.png'), 'Hotel Garibaldi, tre stelle', link='/', w_img=(100, 100, 74), fisso=True,
                link_label='Hotel Garibaldi, pagina iniziale', css='hgr-logo')
    # nel fallback il telefono è la prima voce, visibile solo nella tendina (come la voce del menu WordPress)
    menu = MENU([(TEL, TEL_LINK)] + VOCI_MENU, colore=ARDESIA, colore_hover=ROSSO, accento=ROSSO, fondo_menu=BIANCO,
                linea=BIANCO, stile='nav', stile_mobile='nav_m', spazio=32, pad_v=8, distanza=30, align_menu='center',
                grow=True, css='hgr-menu')
    # desktop: logo, menu (cresce e si centra nello spazio libero), telefono, "Prenota";
    # tablet e telefono: logo, "Prenota" e "Menu" a destra (ordine e margine nel CSS della testata)
    tel = T(f'<p><a href="{TEL_LINK}">{TEL}</a></p>', style='tel_t', color=ARDESIA, link_color=ARDESIA, link_hover=ROSSO,
            sottolinea=False, hide=['tablet', 'mobile'], fisso=True, css='hgr-tel-testata hgr-cifre hgr-tap')
    prenota = B('Prenota', '/prenota/', variant='primario', fisso=True, css='hgr-btn-testata')
    riga = C(marchio, menu, tel, prenota, dir='row', justify='between', align='center', gap=('s', 'xs', 'xs'),
             min_h=(104, 104, 76), pad=(0, 'lato'), boxed=True, boxed_width=W_TESTO)
    return C(riga, RAW('', css=CSS_BASE, solo_elementor=True),
             RAW(JS_TESTATA, css=CSS_COMUNE + CSS_TESTATA + CSS_NAV_FALLBACK + CSS_OGGETTO),
             pad='0', gap='0', boxed=False, tag='header', bg=BIANCO, css='hgr-testata hgr-sito')


def footer():
    pagine = ''.join(f'<a href="{u}">{t}</a>' for t, u in
                     [('L’albergo', '/albergo/'), ('Camere e prezzi', '/camere/'), ('Dove siamo', '/dove-siamo/'),
                      ('Prenota', '/prenota/')])
    altre = '<a href="/en/" lang="en">English</a><a href="/privacy/">Privacy</a><a href="/cookie/">Cookie</a>'
    colonne = C(
        C(I(img('logo-ardesia.png'), 'Hotel Garibaldi, tre stelle', link='/', w_img=(92, 92, 92),
            link_label='Hotel Garibaldi, pagina iniziale'),
          testo(f'{INDIRIZZO}, {CAP_CITTA}<br>Ponte di Brenta, uscita Padova Est della{NB}A4', stile='piede', mt='xs'),
          w=(40, 47, 100), gap='0'),
        C(testo(f'Telefono <a href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a>',
                stile='piede', sottolinea=False, css='hgr-cifre'),
          w=(30, 47, 100), gap='0'),
        C(testo(f'<p>{pagine}</p>', stile='piede', sottolinea=False, css='hgr-voci', mt=(-4, -9, -9)),
          w=(18, 47, 100), gap='0'),
        C(testo(f'<p>{altre}</p>', stile='piede', sottolinea=False, align=('right', 'left', 'left'), css='hgr-voci',
                mt=(-4, -9, -9)),
          w=(12, 47, 100), gap='0'),
        dir='row', dir_m='column', wrap=(False, True, False), justify='between', align='start',
        gap=(0, 48, 32), gap_r=(0, 48, 32))
    legale = C(
        testo(f'{RAGIONE}, <span class="hgr-nw">P.IVA e C.F. {PIVA}</span>, <span class="hgr-nw">REA {REA}</span>, '
              f'<span class="hgr-nw">capitale sociale {CAPITALE}</span>, <span class="hgr-nw">PEC {PEC}</span>. '
              f'<span class="hgr-nw">CIN {CIN}</span>.', stile='legale', colore=TESTO2, css='hgr-cifre'),
        pad=('xs', 0, 0, 0), border_top=1, border_color=FILETTO, mt='l', gap='0', css='hgr-legale')
    return C(colonne, legale, gap='0', pad=('xl', 'lato', (48, 48, 32), 'lato'), bg=BIANCO, tag='footer', boxed_width=W_TESTO,
             css='hgr-piede hgr-sito')


# ---------------------------------------------------------------------------------------------
# Sezioni della home (parametriche: la pagina English usa le stesse con i testi tradotti)
# ---------------------------------------------------------------------------------------------
ALT_CHIAVE = ('I portachiavi dell’Hotel Garibaldi, in cuoio rosso con il monogramma GH e la greca dorata, nelle caselle '
              'di legno del ricevimento')
ALT_FACCIATA_SERA = ('La facciata dell’Hotel Garibaldi all’imbrunire, con l’insegna HOTEL e le tre stelle accese sul tetto '
                     'e le palme davanti all’ingresso')
ALT_INSEGNA = ('L’insegna sul tetto e la scritta Hotel Garibaldi sopra l’ingresso, con il sole in controluce tra i fiori '
               'bianchi')
ALT_CAMERA = ('Camera matrimoniale con la parete blu dietro il letto, la testiera in legno chiaro e la porta finestra aperta '
              'sul balcone')
ALT_BAGNO = 'Il bagno di una camera, con la doccia in vetro e il rivestimento in gres chiaro'
ALT_STATUE = ('Il corridoio delle camere, con due statue bianche su piedistalli di legno ai lati della passatoia rossa')


def sezione_chiave(titolo, attacco, numero=TEL):
    """H1, la chiave: titolo grande sul bianco, sopra i portachiavi a tutta larghezza (fino a 1920 px);
    sotto, la frase con indirizzo, casello, parcheggio e colazione e, a destra, telefono ed email.
    A telefono la foto viene prima del titolo (regola G9 della guida)."""
    titolo_n = C(H(titolo, 'h1', style='display'), boxed=True, boxed_width=W_TESTO, pad=(0, 'lato'), mt=(0, 0, 32),
                 mb=(48, 32, 0), gap='0')
    foto = I(img('home-chiave.jpg'), ALT_CHIAVE, height=(600, 440, 300), fit='cover', pos='62% 50%', css='hgr-chiave')
    frase = C(testo(attacco, stile='lead', max_w=(744, 651, 744)), w=(60, 66, 100), gap='0')
    destra = ('right', 'right', 'left')
    contatti = C(telefono(numero=numero, align=destra), email(mt='min', align=destra), align=('end', 'end', 'start'),
                 w=(30, 28, 100), gap='0')
    attacco_n = C(frase, contatti,
                  dir='row', dir_m='column', justify='between', align=('end', 'end', 'start'), gap='col', boxed=True,
                  boxed_width=W_TESTO, pad=(0, 'lato'), mt=(48, 48, 24))
    return C(titolo_n, foto, attacco_n, boxed=True, boxed_width=1920, pad=((48, 48, 0), 0, 0, 0), gap='0', tag='section',
             anchor='content', css='hgr-apertura')


def sezione_insegna(titolo, corpo, link):
    """H2, l'insegna: la facciata all'imbrunire a filo del bordo sinistro (61,1 %, al massimo 880x660); accanto una
    colonna alta quanto la foto, con il dettaglio dell'insegna in alto e titolo, testo e link al fondo."""
    # 880 su 1376 (1440 meno il margine destro di 64) e 560 su 976 a 1024: a 1440 la foto è 880x660, scala 1
    foto = C(I(img('home-facciata-sera.jpg'), ALT_FACCIATA_SERA), w=(63.95, 57.38, 100), fisso=True, gap='0')
    colonna = C(
        I(img('home-insegna-dettaglio.jpg'), ALT_INSEGNA, w_img=(256, 192, 192), hide=['mobile']),
        blocco_titolo_testo(titolo, corpo, link),
        justify='between', gap='m', grow=True, pad=(0, (0, 0, 24)))
    return C(foto, colonna, dir='row', dir_m='column', gap='col', boxed=True, boxed_width=W_FILO,
             pad=('sezione', (64, 48, 0), 0, 0), tag='section', css='hgr-insegna')


def sezione_camera(titolo, corpo, link, didascalia, dettaglio=True, extra=None):
    """H3, la camera: specchio dell'insegna. La camera a filo del bordo destro (66,7 %, al massimo 960x720) con la
    didascalia; a sinistra titolo, testo e link in alto e il dettaglio del bagno in basso, allineato al fondo della foto."""
    figura = C(I(img('home-camera.jpg'), ALT_CAMERA),
               C(testo(didascalia, stile='small', colore=TESTO2), pad=('xxs', (0, 0, 24), 0, (0, 0, 24)), gap='0',
                 css='hgr-didascalia'),
               w=(69.77, 61.48, 100), fisso=True, gap='0', css='hgr-figura')   # 960 su 1376, 600 su 976
    alto = [blocco_titolo_testo(titolo, corpo, link, stile_titolo='h2b')]
    if extra:
        alto.append(extra)
    figli = [C(*alto, gap='m')]
    if dettaglio:
        figli.append(I(img('home-bagno-dettaglio.jpg'), ALT_BAGNO, w_img=(240, 240, 240), hide=['tablet', 'mobile']))
    colonna = C(*figli, justify='between', gap='m', grow=True, pad=(0, (0, 0, 24)))
    return C(figura, colonna, dir='row-reverse', dir_m='column', gap='col', boxed=True, boxed_width=W_FILO,
             pad=('sezione', 0, 0, (64, 48, 0)), tag='section', css='hgr-camera')


def sezione_prenota(titolo, corpo, bottone, numero=TEL):
    """H4, il campo rosso: l'unico cambio di fondo della pagina. Titolo, lingue, telefono ed email, un bottone chiaro;
    a destra le statue del corridoio a filo dei bordi alto, destro e basso (al massimo 440x660, mai allungate)."""
    contatti = C(telefono(stile='tel_r', colore=BIANCO, numero=numero, fisso=True),
                 email(colore=BIANCO, hover=BIANCO, fisso=True, css='hgr-su-rosso'),
                 dir='row', dir_m='column', wrap=True, align=('baseline', 'baseline', 'start'), gap=(48, 48, 8),
                 gap_r=(16, 16, 8), mt=(48, 48, 32), mb=(48, 48, 32))
    testo_n = C(
        H(titolo, 'h2', style='h2r', color=BIANCO, max_w=(725, 575, 342)),
        testo(corpo, colore=SU_ROSSO2, max_w=(608, 576, 576), mt='s'),
        contatti,
        B(bottone[0], bottone[1], variant='chiaro'),
        justify='center', gap='0', grow=True, pad=((96, 64, 48), (96, 48, 24), (96, 64, 64), (64, 48, 24)))
    foto = C(I(img('statue.jpg'), ALT_STATUE, css='hgr-statue'), w=(30.56, 37.1, 100), fisso=True, gap='0')
    return C(testo_n, foto, dir='row', dir_m='column-reverse', gap='0', boxed=True, boxed_width=W_PIENO, pad='0', bg=ROSSO,
             mt='sezione',
             tag='section', css='hgr-rosso hgr-prenota-home')


# ---------------------------------------------------------------------------------------------
# HOME (specifica, paragrafo 7)
# ---------------------------------------------------------------------------------------------
def home():
    return [
        ('chiave', sezione_chiave(
            f'La tua chiave a{NB}Padova{NB}Est',
            f'Hotel Garibaldi, tre stelle in {INDIRIZZO} a{NB}Ponte di Brenta, a{NB}mezzo chilometro dal casello Padova Est '
            f'della{NB}A4. Parcheggio privato gratuito e{NB}colazione a{NB}buffet sono compresi nel prezzo.')),
        ('insegna', sezione_insegna(
            'Uscita Padova Est',
            f'Dal casello segui le indicazioni per Vigonza e{NB}Ponte di Brenta. Il parcheggio privato è gratuito, con '
            f'50{NB}posti auto; la Fiera di Padova è a{NB}4{NB}km, il Palasport San Lazzaro a{NB}1{NB}km.',
            ('Come arrivare', '/dove-siamo/'))),
        ('camera', sezione_camera(
            'Dalla singola alla quadrupla',
            'Sei tipi di camera, anche con due doppie comunicanti, con TV, frigobar e WiFi gratuito. Nel prezzo ci sono la '
            f'colazione a{NB}buffet e{NB}il parcheggio.',
            ('Camere e prezzi', '/camere/'), 'Camera matrimoniale con balcone')),
        ('prenota', sezione_prenota(
            'Prenoti senza carta di credito e paghi in hotel',
            'Chiamaci o scrivici con le date del soggiorno. In albergo si parla italiano, inglese, tedesco, francese '
            'e spagnolo.',
            ('Scrivi una richiesta', '/prenota/'))),
    ]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': 'Hotel Garibaldi, Padova Est: tre stelle con parcheggio gratuito all’uscita della A4',
     'descrizione': 'Hotel Garibaldi, tre stelle in Via San Marco 63 a Ponte di Brenta, a mezzo chilometro dal casello '
                    'Padova Est della A4. Parcheggio privato gratuito e colazione a buffet compresi.'},
]
