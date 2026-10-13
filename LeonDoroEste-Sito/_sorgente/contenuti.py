# -*- coding: utf-8 -*-
"""
Contenuti del sito Albergo Ristorante Leon d'Oro, Este (PD).

Idea (specifica _prova/spec.md, paragrafo 1): le cose vere della casa, una alla volta, grandi su molto bianco. Ogni pagina si
apre con una foto sola e un titolo maiuscolo di due o tre parole, e si chiude sul giallo della facciata, dove si prenota.
Nella home la prima schermata è la facciata di sera con "RESTA A CENA" a 144 px.

Home approvata dal committente: _prova/direzioni/giro2/oggetto/proto.html (giro 2, direzione "l'oggetto").
Carattere: Libre Franklin sola, 400, 600, 800 (dalle maiuscole della cartolina e del logo; guida c4).
Palette: bianco #FFFFFF (le tovaglie), verde persiana #263F40, giallo facciata #D3AB45, inchiostro #1B201F.
Fonti dei testi: 01-analisi-sito-attuale.md (testi numerati), Regione Veneto (tredici camere), specifica.

Come è costruito (per chi aggiunge pagine):
- ogni sezione è un contenitore con widget gratuiti di Elementor (titolo, testo, immagine); quello che Elementor gratuito non sa
  fare (misure in proporzione alla larghezza, rapporto d'aspetto, cambi del solo telefono) sta in un widget HTML con il solo
  <style>, l'ultimo figlio della sezione: in Elementor è un foglio di stile, nel fallback viene aggiunto al CSS della sezione;
- le foto con un titolo sopra sono sfondi di contenitore (Elementor le importa nella libreria media); al telefono, quando il
  titolo scende sotto la foto, la foto è un widget immagine visibile solo al telefono;
- il menu della testata è un widget HTML (markup, stile e script, identico nel fallback): Elementor gratuito e il widget di
  Ultimate Addons cambiano a 767 e 1024 px, la specifica vuole il bottone "Menu" con telefono e "Prenota" nel pannello. Il menu
  si chiude a 900 px e non a 820 come nella specifica: misurato, la riga intera (logo, cinque voci, Prenota) chiede 878 px e a 821
  il bottone usciva dalla testata; il telefono si vede da 1181 px (con il telefono la riga chiede 1123 px);
- per le altre pagine: campo_giallo (la chiusura di ogni pagina), foto_con_titolo (foto piena col titolo nel cielo),
  oggetto_centrato con frase (una cosa sola al centro del bianco), testo, link_isolato, contatti, solo_lettori, euro, LISTINO;
  la prima sezione di ogni pagina ha anchor='content' (il link "Vai al contenuto" della testata porta lì);
- le sezioni con una foto di sfondo hanno la classe e-no-lazyload sul contenitore esterno (la sezione): Elementor rimanda gli
  sfondi dei figli finché la sezione non entra nella finestra, e senza JavaScript resterebbero vuoti.
"""
import re
from urllib.parse import quote

import motore as m
from motore import C, H, T, I, RAW, SHORTCODE

PREFISSO = 'ldo'
NOME_SITO = "Leon d'Oro"

# ---------------------------------------------------------------------------------------------
# Tema (specifica 3)
# ---------------------------------------------------------------------------------------------
BIANCO = '#FFFFFF'         # le tovaglie: fondo di quasi tutta ogni pagina
VERDE = '#263F40'          # persiane misurate #4E6D6E, scurite: logo, titoli su bianco, bottone, link, piede
GIALLO = '#D3AB45'         # muro misurato #CEAE5A: un solo campo per pagina; anello del fuoco
INCHIOSTRO = '#1B201F'     # testo, titoli sul giallo e sul cielo, hover dei bottoni
CHIARO = '#E4EAE9'         # testo piccolo del piede, fondo dei bottoni disabilitati
GRIGIO = '#5A615F'         # testo dei bottoni disabilitati, note del modulo
NOTTE = '#140D06'          # il buio della foto della facciata, ai lati oltre 1680 px

FRANKLIN = 'Libre Franklin'
FONT_CSS = f"'{FRANKLIN}',Arial,sans-serif"


def _st(w, s, lh, ls=0.0, up=False):
    return dict(f=FRANKLIN, w=w, s=s, lh=lh, ls=ls, up=up)


# spaziatura delle lettere: motore la scrive in px uguale ai tre breakpoint; il valore è quello a 1440 (em della specifica x px).
# Il titolo della home, l'unico dove la differenza si vede, la riprende in em nel CSS (classe ldo-display).
STILI = {
    'display':   _st('800', (144, 104, 64), 0.9, -2.88, True),   # solo "Resta a cena"
    'h1':        _st('800', (72, 56, 40), 0.98, -1.08, True),     # titolo delle pagine interne
    'h2a':       _st('800', (44, 40, 30), 1.05, -0.44, True),     # titoli su foto o accanto a foto grandi
    'h2b':       _st('800', (40, 36, 30), 1.05, -0.4, True),     # titoli del campo giallo
    'h2c':       _st('800', (36, 36, 30), 1.05, -0.36, True),     # titoli accanto al testo
    'frase':     _st('400', (30, 26, 21), 1.35, -0.3),           # la frase sola centrata sotto l'oggetto
    'primo':     _st('400', (21, 19, 18), 1.55),                 # paragrafo d'apertura
    'h3':        _st('600', (22, 22, 20), 1.3),
    'testo':     _st('400', (19, 19, 17), 1.6),
    'foto':      _st('400', (18, 18, 17), 1.5),                  # testo sopra la cartolina, voci del menù
    'contatto':  _st('600', (24, 21, 20), 1.3),                  # email e telefono grandi nel campo giallo
    'link':      _st('600', (16, 16, 16), 1.2),
    'nav':       _st('400', (16, 16, 20), 1.2),
    'piccolo':   _st('400', (15, 15, 15), 1.6),
    'etichetta': _st('600', (16, 16, 15), 1.3),
    'prezzo':    _st('600', (19, 19, 17), 1.6),                  # prezzi del listino (testo in 600)
}
# nomi che il motore usa come predefiniti (H con livello senza stile, bottoni, shortcode)
STILI.update({'h2': STILI['h2a'], 'p': STILI['testo'], 'body': STILI['testo'], 'small': STILI['piccolo'],
              'btn': STILI['link']})

# una sola scala: 8 16 24 32 40 48 64 72 80 96 128 160 (più 20, solo come margine laterale a 390)
SPAZI = {
    'stacco': (160, 128, 72),   # il bianco fra un momento e l'altro della pagina
    'lato':   (64, 40, 20),     # margine laterale di pagina
    'campo':  (96, 80, 48),     # padding verticale del campo giallo
    'xl':     (96, 80, 48),
    'l':      (64, 48, 32),
    'm':      (40, 40, 32),
    's':      (24, 24, 16),
    'xs':     (16, 16, 16),
    'xxs':    (8, 8, 8),
    '0':      (0, 0, 0),
}

TEMA = {
    'nome': 'Facciata',
    'fondo': BIANCO, 'superficie': BIANCO, 'inchiostro': INCHIOSTRO, 'testo2': GRIGIO, 'accento': GIALLO,
    'filetto': INCHIOSTRO, 'filetto_scuro': CHIARO, 'su_scuro2': CHIARO,
    'scuro': VERDE, 'su_scuro': BIANCO, 'su_accento': INCHIOSTRO,
    'font_titoli': FRANKLIN, 'font_testo': FRANKLIN, 'larghezza': 1200,
    'google_fonts': 'https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;600;800&display=swap',
    'stili': STILI,
    'spazi': SPAZI,
    # (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover): cambio di colore pieno, mai opacità
    'bottoni': {
        'primario': (BIANCO, VERDE, VERDE, BIANCO, INCHIOSTRO, INCHIOSTRO),
    },
    'bottone': {'raggio': 2, 'pad': (12, 24, 12, 24), 'bordo': 0, 'stile': 'link'},
}
m.applica_tema(TEMA)

# Le immagini vengono scaricate da Elementor nella libreria media al momento dell'import.
BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/LeonDoroEste-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Dati (un solo posto da aggiornare)
# ---------------------------------------------------------------------------------------------
NB = ' '                                   # spazio indivisibile
WJ = '⁠'                                   # word joiner: niente a capo dentro un trattino
TEL = f'0429{NB}602949'
TEL_LINK = 'tel:+390429602949'
FAX = f'0429{NB}3072'
EMAIL = 'prenotazioni@leondoroeste.it'
RAGIONE_SOCIALE = "Albergo Ristorante Leon d'Oro S.n.c. di Rubini Rodolfo &amp; C."
INDIRIZZO = f'Viale{NB}Fiume{NB}20, 35042{NB}Este{NB}(PD)'
CHIUSURA = 'Ristorante chiuso la domenica'
PIVA = '04185510288'
REA = f'PD{WJ}-{WJ}369167'
CIN = 'IT028037A1GWJ7NDDS'                      # [DA CONFERMARE: attualità e obbligo sul sito proprio]
FACEBOOK = 'https://www.facebook.com/albergoleondoroeste'
INSTAGRAM = 'https://www.instagram.com/albergoristoranteleondoro'

# listino 2026 (testo 15): un punto solo, alimenta la frase della home e il listino delle camere
LISTINO = {'anno': 2026, 'singola': 50, 'doppia': 75, 'mezza': 65, 'completa': 80}


def euro(n):
    return f'{n}{NB}€'


# apostrofo tipografico (U+2019) nei testi che si leggono: titoli, paragrafi, testi alternativi, l'alternativa del modulo.
# I testi qui sono scritti con l'apostrofo dritto; WordPress lo cambia solo in alcuni widget, così il fallback e i titoli
# restavano con l'apostrofo dritto, che nel maiuscolo 800 sembra una virgoletta. I tag HTML (attributi, stili) non si toccano.
_TAG = re.compile(r'(<[^>]+>)')


def _tipo(html):
    return ''.join(x if x.startswith('<') else x.replace("'", '\u2019') for x in _TAG.split(html))


def apostrofi(nodo):
    p = nodo.p
    if nodo.kind == 'heading':
        p['text'] = _tipo(p['text'])
    elif nodo.kind == 'text':
        p['html'] = _tipo(p['html'])
    elif nodo.kind == 'image':
        p['alt'] = p.get('alt', '').replace("'", '\u2019')
    elif nodo.kind == 'shortcode':
        p['alternativa_html'] = _tipo(p['alternativa_html'])
    for figlio in nodo.children:
        apostrofi(figlio)
    return nodo


def tipografica(pagina):
    """Le sezioni di una pagina con gli apostrofi tipografici (per PAGINE)."""
    return lambda: [(nome, apostrofi(sezione)) for nome, sezione in pagina()]


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    return url + ('&body=' + quote(corpo) if corpo else '')


# voci del menu, in quest'ordine (specifica 4.1); "Prenota" è il bottone della testata, non una voce
VOCI_MENU = [('camere', '/camere/'), ('ristorante', '/ristorante/'), ('bike hotel', '/bike-hotel/'),
             ('per l\u2019ospedale', '/ospedale-schiavonia/'), ('dove siamo', '/dove-siamo/')]


# ---------------------------------------------------------------------------------------------
# CSS condiviso (nel widget HTML della testata: c'è in ogni pagina, in Elementor e nel fallback)
# ---------------------------------------------------------------------------------------------
CSS_SITO = (
    'body{font-synthesis:none}'
    # testo solo per chi legge con la sintesi vocale (la descrizione delle foto di sfondo)
    '.ldo-sr{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;'
    'clip:rect(1px,1px,1px,1px)!important;white-space:nowrap!important;margin:0!important;padding:0!important}'
    # link nel testo: sottolineatura spessa 2 px a 6 px dal testo (specifica 3.5)
    '.ldo-sott a{font-weight:600;text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important}'
    '.ldo-sott a:focus-visible{outline:3px solid ' + GIALLO + ';outline-offset:3px}'
    '.ldo-campo .ldo-sott a:focus-visible{outline-color:' + INCHIOSTRO + '}'
    '.ldo-intero a{white-space:nowrap}'
    # il titolo grande della home: spaziatura in em, uguale a ogni misura (-0,02em)
    '.ldo-display .elementor-heading-title,h1.ldo-display{letter-spacing:-0.02em!important}'
    # Elementor: a capo bilanciati nei titoli, niente spazio sotto l'ultimo paragrafo (come nel fallback)
    '.elementor-widget-heading .elementor-heading-title{text-wrap:balance}'
    '.elementor-widget-text-editor p{text-wrap:pretty}'
    '.elementor-widget-text-editor p:last-child{margin-block-end:0!important;margin-bottom:0!important}'
    '.ldo-frase p{text-wrap:balance!important}'
    # voci di una carta: niente spazio fra i paragrafi, rientro sospeso
    '.ldo-voci p{margin:0!important;padding-left:1em;text-indent:-1em}'
)

# ---------------------------------------------------------------------------------------------
# Testata: logo, menu, telefono, "Prenota"; da 900 px in giù logo, "Chiama" e "Menu" (specifica 4.1)
# ---------------------------------------------------------------------------------------------
NAV_LINK = f"font:400 16px/1.2 {FONT_CSS};color:{INCHIOSTRO};text-decoration:none;white-space:nowrap;display:inline-block;padding:12px 0"
SOTTOLINEA = 'text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px'
CSS_NAV = (
    # il pannello del telefono si apre sotto tutta la testata: la testata è il riferimento, i widget no
    '.ldo-testata{position:relative;overflow-x:clip}'
    '.ldo-testata .elementor-widget-html,.ldo-testata .ldo-w,.ldo-testata .ldo-marchio{position:static!important}'
    f'.ldo-nav{{display:flex;align-items:center;gap:40px;font-family:{FONT_CSS}}}'
    '.ldo-nav .ldo-pannello{display:flex;align-items:center;gap:40px}'
    '.ldo-nav .ldo-menu{display:flex;gap:32px;list-style:none;margin:0;padding:0}'
    '.ldo-nav .ldo-menu li{margin:0;padding:0;border:0;list-style:none}'
    f'.ldo-nav .ldo-menu a,.ldo-nav .ldo-tel{{{NAV_LINK}}}'
    f'.ldo-nav .ldo-menu a:hover,.ldo-nav .ldo-menu a:focus-visible,.ldo-nav .ldo-tel:hover,.ldo-nav .ldo-tel:focus-visible'
    f'{{color:{VERDE};{SOTTOLINEA}}}'
    f'.ldo-nav .ldo-menu a[aria-current=page]{{color:{VERDE};{SOTTOLINEA}}}'
    f'.ldo-nav .ldo-bottone{{font:600 16px/1.2 {FONT_CSS};color:{BIANCO};background:{VERDE};padding:12px 24px;border:0;'
    'border-radius:2px;text-decoration:none;white-space:nowrap;display:inline-block}'
    f'.ldo-nav .ldo-bottone:hover,.ldo-nav .ldo-bottone:active,.ldo-nav .ldo-bottone:focus{{background:{INCHIOSTRO};color:{BIANCO}}}'
    f'.ldo-nav a:focus-visible,.ldo-nav button:focus-visible{{outline:3px solid {GIALLO};outline-offset:3px}}'
    '.ldo-nav .ldo-chiama,.ldo-nav .ldo-apri{display:none}'
    # "Vai al contenuto" (il nostro nel fallback, quello di Ultimate Addons in WordPress): nascosto, visibile al fuoco
    '.ldo-salta,a.hfe-skip-link{position:absolute!important;left:-9999px!important;top:0}'
    f'.ldo-salta:focus,a.hfe-skip-link:focus{{left:16px!important;top:16px!important;z-index:100;background:{VERDE}!important;'
    f'color:{BIANCO}!important;font:600 16px/1.2 {FONT_CSS}!important;padding:8px 16px!important;text-decoration:none!important;'
    f'border-radius:2px!important;box-shadow:none!important;clip:auto!important;width:auto!important;height:auto!important;'
    f'outline:3px solid {GIALLO}!important;outline-offset:3px}}'
    # il bottone "Menu": il tema Hello colora i bottoni di rosa, qui ogni stato ha il suo colore
    f'.ldo-nav .ldo-apri,.ldo-nav .ldo-apri:focus{{font:600 16px/1 {FONT_CSS};background:{BIANCO};color:{INCHIOSTRO};'
    f'border:2px solid {INCHIOSTRO};border-radius:2px;padding:12px 16px;min-height:44px;min-width:44px;cursor:pointer;'
    'box-shadow:none;text-transform:none;letter-spacing:0;margin:0}'
    f'.ldo-nav .ldo-apri:hover,.ldo-nav .ldo-apri[aria-expanded=true]{{background:{INCHIOSTRO};color:{BIANCO};border-color:{INCHIOSTRO}}}'
    f'.ldo-nav .ldo-chiama{{font:600 16px/1.2 {FONT_CSS};color:{VERDE};{SOTTOLINEA};padding:12px 0;white-space:nowrap}}'
    f'.ldo-nav .ldo-chiama:hover{{color:{INCHIOSTRO}}}'
    '@media (max-width:1180px){.ldo-nav .ldo-tel{display:none}.ldo-nav,.ldo-nav .ldo-pannello{gap:24px}.ldo-nav .ldo-menu{gap:24px}}'
    '@media (max-width:900px){'
    '.ldo-nav{gap:16px}'
    '.ldo-nav .ldo-chiama,.ldo-nav .ldo-apri{display:inline-block}'
    f'.ldo-nav .ldo-pannello{{position:absolute;left:0;right:0;top:100%;z-index:50;background:{BIANCO};flex-direction:column;'
    'align-items:flex-start;gap:24px;padding:16px 40px 32px;min-height:calc(100vh - 88px);overflow-y:auto}'
    '.ldo-nav .ldo-menu{flex-direction:column;gap:0}'
    '.ldo-nav .ldo-menu a{font-size:20px}'
    '.ldo-nav .ldo-pannello .ldo-tel{display:inline-block;font-size:20px}'
    '.ldo-nav.ldo-js .ldo-pannello{display:none}'
    '.ldo-nav.ldo-js.aperto .ldo-pannello{display:flex}'
    # senza JavaScript il bottone non serve: il menu resta visibile in colonna sotto la testata
    '.ldo-nav:not(.ldo-js) .ldo-apri{display:none}'
    '.ldo-nav:not(.ldo-js) .ldo-pannello{position:static;padding:0}'
    '.ldo-nav:not(.ldo-js){flex-direction:column;align-items:flex-end}'
    '.ldo-nav:not(.ldo-js) .ldo-pannello{min-height:0}'
    '.ldo-testata:has(.ldo-nav:not(.ldo-js)){align-items:flex-start!important}'
    '}'
    # il pannello aperto copre tutta la finestra sotto la testata: niente pezzi di pagina sotto le voci
    '@media (max-width:767px){.ldo-nav .ldo-pannello{padding:16px 20px 32px;min-height:calc(100vh - 76px)}}'
)

JS_NAV = (
    "(function(){function via(){document.querySelectorAll('.ldo-nav').forEach(function(n){if(n.dataset.ok)return;n.dataset.ok=1;"
    "n.classList.add('ldo-js');var b=n.querySelector('.ldo-apri'),p=n.querySelector('.ldo-pannello');"
    "if(document.querySelector('.hfe-skip-link')){document.querySelectorAll('.ldo-salta').forEach(function(s){s.remove()})}"
    # voce attiva: la pagina che si sta guardando
    "var qui=location.pathname.replace(/\\/+$/,'');n.querySelectorAll('.ldo-menu a').forEach(function(a){"
    "if(a.pathname.replace(/\\/+$/,'')===qui&&qui!=='')a.setAttribute('aria-current','page')});"
    "function apri(o){n.classList.toggle('aperto',o);b.setAttribute('aria-expanded',o?'true':'false');"
    "if(o){var f=p.querySelector('a');if(f)f.focus()}}"
    "b.addEventListener('click',function(){apri(!n.classList.contains('aperto'))});"
    # Esc chiude; il fuoco gira fra il bottone e le voci del pannello finché è aperto
    "n.addEventListener('keydown',function(e){if(!n.classList.contains('aperto'))return;"
    "if(e.key==='Escape'){apri(false);b.focus();return}"
    "if(e.key==='Tab'){var f=[b].concat([].slice.call(p.querySelectorAll('a'))),i=f.indexOf(document.activeElement);"
    "if(e.shiftKey&&i<=0){e.preventDefault();f[f.length-1].focus()}else if(!e.shiftKey&&i===f.length-1){e.preventDefault();f[0].focus()}}});"
    "document.addEventListener('click',function(e){if(n.classList.contains('aperto')&&!n.contains(e.target))apri(false)});"
    "if(window.matchMedia){var mq=matchMedia('(min-width:901px)');var chiudi=function(){if(mq.matches)apri(false)};"
    "if(mq.addEventListener)mq.addEventListener('change',chiudi);else if(mq.addListener)mq.addListener(chiudi)}"
    "})}if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',via)}else{via()}})();"
)


def nav_html():
    voci = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in VOCI_MENU)
    return (
        '<nav class="ldo-nav" aria-label="Menu principale">'
        f'<a class="ldo-chiama" href="{TEL_LINK}">Chiama</a>'
        '<button class="ldo-apri" type="button" aria-controls="ldo-pannello" aria-expanded="false">Menu</button>'
        f'<div class="ldo-pannello" id="ldo-pannello"><ul class="ldo-menu">{voci}</ul>'
        f'<a class="ldo-tel" href="{TEL_LINK}">{TEL}</a>'
        '<a class="ldo-bottone" href="/prenota/">Prenota</a></div>'
        f'</nav><script>{JS_NAV}</script>'
    )


def header():
    # "Vai al contenuto" prima del logo, così è il primo Tab: serve al fallback; in WordPress Ultimate Addons scrive già il suo
    # (hfe-skip-link, verso #content) e lo script del menu toglie questo, così il link è uno solo.
    # La prima sezione di ogni pagina ha l'ancora "content".
    salta = RAW('<a class="ldo-salta" href="#content">Vai al contenuto</a>')
    logo = I(img('logo-leondoro-verde.png'), "Albergo Leon d'Oro, Este", link='/', link_label="Albergo Leon d'Oro, Este: pagina iniziale",
             w_img=(134, 134, 105), fisso=True, css='ldo-logo')
    marchio = C(salta, logo, dir='row', align='center', gap=0, larg_px=(134, 134, 105), css='ldo-marchio')
    # niente tag header: in WordPress Ultimate Addons avvolge già la testata in <header id="masthead"> e un secondo header
    # dentro il primo è HTML non valido e un secondo punto di riferimento "banner" (lo stesso vale per il piede)
    return apostrofi(C(marchio, RAW(nav_html(), css=CSS_SITO + CSS_NAV), dir='row', justify='between', align='center',
                       gap='m', pad=(16, 'lato'), bg=BIANCO, boxed=False, css='ldo-testata'))


# ---------------------------------------------------------------------------------------------
# Piede (specifica 4.2)
# ---------------------------------------------------------------------------------------------
CSS_PIEDE = (
    f'.ldo-piede strong{{color:{BIANCO};font-weight:600}}'
    '.ldo-piede a{text-decoration:none!important}'
    '.ldo-piede a:hover,.ldo-piede a:focus-visible{text-decoration:underline!important;text-decoration-thickness:2px!important;'
    'text-underline-offset:4px!important}'
    f'.ldo-piede a:focus-visible{{outline:3px solid {GIALLO};outline-offset:3px}}'
)


def _piede_testo(html, **p):
    return T(html, style='piccolo', color=CHIARO, link_color=BIANCO, link_hover=GIALLO, **p)


def footer():
    righe = C(
        I(img('logo-leondoro-bianco.png'), "Albergo Leon d'Oro, Este", link='/', link_label="Albergo Leon d'Oro, Este: pagina iniziale",
          w_img=(153, 130, 105), fisso=True),
        _piede_testo(f'<p><strong>{RAGIONE_SOCIALE}</strong><br>{INDIRIZZO}<br>{CHIUSURA}</p>', max_w=(360, 280, 600)),
        _piede_testo(f'<p>Telefono <a class="ldo-a" href="{TEL_LINK}">{TEL}</a><br>Fax {FAX}<br>'
                     f'<a class="ldo-a" href="mailto:{EMAIL}">{EMAIL}</a></p>', fisso=True),
        _piede_testo(f'<p>P.IVA e C.F.{NB}{PIVA}<br>REA{NB}{REA}<br>CIN{NB}{CIN}</p>', fisso=True),
        dir='row', dir_m='column', wrap=(False, True, False), align='start', gap=(64, 40, 24), gap_r=(32, 32, 24))
    link = [('Privacy', '/privacy/'), ('Cookie', '/cookie/'), ('Facebook', FACEBOOK), ('Instagram', INSTAGRAM)]
    riga_link = C(*[_piede_testo(f'<p><a class="ldo-a" href="{u}">{t}</a></p>', fisso=True) for t, u in link],
                  dir='row', wrap=True, gap=32, gap_r=8, mt=48)
    return apostrofi(C(righe, riga_link, RAW('', css=CSS_PIEDE), bg=VERDE, pad=((64, 64, 48), 'lato', (48, 48, 40), 'lato'),
                       gap=0, boxed=False, css='ldo-piede'))


# ---------------------------------------------------------------------------------------------
# Componenti riusabili (specifica 3.6)
# ---------------------------------------------------------------------------------------------
def solo_lettori(testo, **p):
    """Descrizione di una foto di sfondo per chi usa la sintesi vocale (non si vede)."""
    return T(f'<p>{testo}</p>', style='piccolo', css='ldo-sr', **p)


def testo(html, stile='testo', colore=INCHIOSTRO, link=VERDE, hover=INCHIOSTRO, **p):
    """Paragrafi con i link sottolineati della specifica (verde, hover inchiostro; sul giallo inchiostro, hover verde).
    I link si scrivono <a class="ldo-a" href=...>: così il motore non aggiunge la sottolineatura sottile in linea."""
    classi = ('ldo-sott ' + p.pop('css', '')).strip()
    return T(html, style=stile, color=colore, link_color=link, link_hover=hover, css=classi, **p)


def link_isolato(testo_link, url, colore=VERDE, hover=INCHIOSTRO, **p):
    """Un link da solo sotto un testo ("Il menù", "Il bike hotel"): 600 16 px, sottolineato, senza frecce."""
    return testo(f'<p><a class="ldo-a" href="{url}">{testo_link}</a></p>', stile='link', colore=colore, link=colore, hover=hover, **p)


def contatti(ordine=('email', 'tel'), **p):
    """Email e telefono grandi e sottolineati (campo giallo): in riga, uno per riga al telefono."""
    voci = {'email': f'<a class="ldo-a" href="mailto:{EMAIL}">{EMAIL}</a>', 'tel': f'<a class="ldo-a" href="{TEL_LINK}">{TEL}</a>'}
    return C(*[testo(f'<p>{voci[k]}</p>', stile='contatto', link=INCHIOSTRO, hover=VERDE, css='ldo-intero', fisso=True)
               for k in ordine],
             dir='row', dir_m='column', wrap=True, gap=(40, 40, 16), gap_r=(8, 8, 16), **p)


CSS_CAMPO = (
    # la foto a filo destro: metà della riga, mai più di 720 px; al telefono sopra il testo, alta in proporzione
    '.ldo-campo-foto{max-width:720px!important}'
    '@media (max-width:767px){.ldo-campo-foto{max-width:none!important}.ldo-campo-foto img{height:auto!important}}'
)


def campo_giallo(titolo, primo, foto, alt, testi=(), azione=None, ordine=('email', 'tel'), dopo=None, pos='center center',
                 alt_h=(720, 600, 339), ancora=None, mt='stacco'):
    """Il campo giallo che chiude ogni pagina (specifica 3.6): a sinistra titolo, primo paragrafo, testi, l'azione (H3) e i
    contatti; a destra la foto a filo, 720 x 720 a 1440, il 46 % della riga a 1024; al telefono la foto sopra e il testo sotto.
    testi: paragrafi HTML (link con class="ldo-a"); dopo: un link isolato sotto i contatti (es. "Il modulo di richiesta")."""
    figli = [H(titolo, 'h2', style='h2b', color=INCHIOSTRO),
             testo(f'<p>{primo}</p>', stile='primo', link=INCHIOSTRO, hover=VERDE, mt='s', max_w=(630, 630, 600))]
    figli += [testo(t, link=INCHIOSTRO, hover=VERDE, mt='xs', max_w=(570, 570, 600)) for t in testi]
    if azione:
        figli.append(H(azione, 'h3', style='h3', color=INCHIOSTRO, mt='m'))
    figli.append(contatti(ordine, mt='xs'))
    if dopo:
        figli.append(link_isolato(*dopo, colore=INCHIOSTRO, hover=VERDE, mt='s'))
    parole = C(*figli, pad=('campo', (64, 48, 20), 'campo', 'lato'), justify='center', gap=0, grow=True, css='ldo-campo-testo')
    immagine = C(I(img(foto), alt, height=alt_h, pos=pos), w=(50, 46, 100), fisso=True, gap=0, css='ldo-campo-foto')
    return C(parole, immagine, RAW('', css=CSS_CAMPO), dir='row', dir_m='column-reverse', align='stretch', bg=GIALLO, boxed=False,
             pad='0', gap=0, mt=mt, tag='section', anchor=ancora, css='ldo-campo')


def foto_con_titolo(nome, titolo, foto, misura, descrizione, pos_telefono, colore=INCHIOSTRO, stile='h2a', livello='h2',
                    pad_alto='6.6%', pad_telefono=24, ancora=None, mt='stacco', dopo=(), foto_telefono=None):
    """Foto a tutta larghezza con il titolo nel cielo, in alto a sinistra (home H5, Dove siamo D1): sfondo di contenitore,
    larghezza massima uguale al file, altezza in proporzione al file; al telefono la stessa foto ritagliata dallo sfondo
    (pos_telefono: posizione orizzontale in %, rapporto (w, h) del ritaglio) e il titolo resta nel cielo.
    foto_telefono: al telefono un'altra foto (widget immagine) sopra e il titolo sotto, in verde su bianco (Dove siamo D1,
    dove il cielo a 390 px è troppo basso per il titolo).
    dopo: widget sotto la foto, nel bianco, con il margine di pagina."""
    w, h = misura
    (px, (tw, th)) = pos_telefono
    classe = f'ldo-pieno-{nome}'
    css = f'.{classe} .ldo-pieno-foto{{aspect-ratio:{w}/{h};padding-top:{pad_alto}!important}}'
    if foto_telefono:
        css += ('@media (max-width:767px){'
                f'.{classe} .ldo-pieno-foto{{aspect-ratio:auto;background-image:none!important;padding:32px 20px 0!important}}'
                f'.{classe} .ldo-pieno-foto .elementor-heading-title,.{classe} .ldo-pieno-foto h1,.{classe} .ldo-pieno-foto h2'
                f'{{color:{VERDE}!important}}}}')
    else:
        css += (f'@media (max-width:767px){{.{classe} .ldo-pieno-foto{{aspect-ratio:{tw}/{th};background-position:{px}% top!important;'
                f'padding-top:{pad_telefono}px!important}}}}')
    lettori = solo_lettori(descrizione, hide=['mobile']) if foto_telefono else solo_lettori(descrizione)
    pieno = C(H(titolo, livello, style=stile, color=colore), lettori, img=img(foto), img_pos='center top',
              pad=(0, 'lato', 0, 'lato'), gap=0, css='ldo-pieno-foto e-no-lazyload')
    figli = [I(img(foto_telefono), descrizione, hide=['desktop', 'tablet'])] if foto_telefono else []
    figli.append(pieno)
    if dopo:
        figli.append(C(*dopo, pad=(0, 'lato', 0, 'lato'), gap=0, mt='l'))
    figli.append(RAW('', css=css))
    return C(*figli, boxed=True, boxed_width=w, pad='0', gap=0, mt=mt, tag='section', anchor=ancora, css=f'{classe} e-no-lazyload')


# ---------------------------------------------------------------------------------------------
# HOME (specifica 6)
# ---------------------------------------------------------------------------------------------
CSS_FACCIATA = (
    f'.ldo-facciata{{background-color:{NOTTE}}}'
    # 1680 x 826: l'altezza segue la larghezza, mai oltre il file; il titolo in alto a destra, sopra gli alberi
    '.ldo-fac-foto{position:relative;aspect-ratio:1680/826;padding-top:8.4%!important}'
    # velatura scura solo dietro il titolo (nessun colore: il nero caldo della foto)
    '.ldo-fac-foto::before{content:""!important;display:block;position:absolute;top:0;left:0;width:100%;height:100%;'
    'background:radial-gradient(ellipse 34% 46% at 79% 30%,rgba(14,9,4,.5),rgba(14,9,4,0));opacity:1;'
    'border:0;pointer-events:none;z-index:0}'
    '.ldo-fac-foto>.ldo-fac-titolo{position:relative;z-index:1}'
    # telefono: prima la foto verticale (widget immagine), poi il titolo in verde su bianco
    '@media (max-width:767px){'
    f'.ldo-facciata{{background-color:{BIANCO}!important}}'
    f'.ldo-fac-foto{{aspect-ratio:auto;background-image:none!important;background-color:{BIANCO}!important;padding:32px 20px 0!important}}'
    '.ldo-fac-foto::before{display:none}'
    f'.ldo-fac-titolo .elementor-heading-title,h1.ldo-fac-titolo{{color:{VERDE}!important;line-height:.92!important}}'
    '}'
)


def facciata():
    """H1: la facciata di sera a tutta larghezza (1680 al massimo, oltre i lati prendono il nero della foto) e RESTA A CENA."""
    descr = ("La facciata del Leon d'Oro di sera, in Viale Fiume a Este, con la scritta Albergo Leon dipinta sul muro e l'insegna "
             "col leone accanto alla porta")
    telefono = I(img('facciata-alto.jpg'), descr, hide=['desktop', 'tablet'])
    titolo = H(f'Resta<br>a{NB}cena', 'h1', style='display', color=BIANCO, css='ldo-display ldo-fac-titolo')
    foto = C(titolo, solo_lettori(descr, hide=['mobile']), img=img('facciata-largo.jpg'), img_pos='center top',
             dir='row', justify=('end', 'end', 'start'), align='start', pad=(0, 'lato', 0, 'lato'), gap=0,
             css='ldo-fac-foto e-no-lazyload')
    return C(telefono, foto, RAW('', css=CSS_FACCIATA), boxed=True, boxed_width=1680, bg=NOTTE, pad='0', gap=0, tag='section',
             anchor='content', css='ldo-facciata e-no-lazyload')


CSS_OGGETTO = (
    '.ldo-oggetto-foto img{margin-left:auto;margin-right:auto}'
    '@media (max-width:767px){.ldo-frase{line-height:1.4!important}}'
)


def frase(html, **p):
    """La frase sola centrata sotto un oggetto (stile "frase", al massimo 25em)."""
    return T(f'<p>{html}</p>', style='frase', color=INCHIOSTRO, align='center', max_w=(750, 650, 600), css='ldo-frase', **p)


def oggetto_centrato(nome, foto, alt, sotto, larghezze=(480, 400, 273), ancora=None, pad_alto='stacco'):
    """Una cosa sola al centro del bianco e, a 64 / 48 / 32 px, quello che la accompagna (specifica 3.6, "Oggetto centrato"):
    la targa con la frase in home (H2), la maglia nel bike hotel (B2), la targa sopra il titolo in Prenota (P1).
    sotto: widget già fatti (frase(...), oppure titolo e paragrafo); larghezze della foto in px a 1440, 1024, 390."""
    figli = [I(img(foto), alt, w_img=larghezze, css='ldo-oggetto-foto')]
    for k, w in enumerate(sotto):
        w.p.setdefault('mt', 'l' if k == 0 else 's')
        figli.append(w)
    figli.append(RAW('', css=CSS_OGGETTO))
    return C(*figli, align='center', pad=(pad_alto, 'lato', 0, 'lato'), gap=0, boxed=False, tag='section', anchor=ancora,
             css=f'ldo-oggetto ldo-{nome}')


def targa():
    """H2: la targa in ceramica ALBERGO al centro, sola, e una frase: dove siamo e cosa si trova."""
    return oggetto_centrato(
        'targa', 'targa.jpg', 'La targa in ceramica ALBERGO con la chiave e le due stelle, sul muro giallo della facciata',
        [frase(f'Albergo e trattoria a{NB}Este, in Viale{NB}Fiume{NB}20: la cena, la camera e il garage per la{NB}bici, '
               f'a{NB}due passi dal Castello Carrarese.')])


CSS_SALA = (
    '.ldo-sala-foto,.ldo-sala-riga{max-width:1200px!important}'
    '@media (max-width:767px){.ldo-sala-foto img{height:300px!important;object-fit:cover;object-position:40% center}}'
)


def sala():
    """H3: la sala a filo sinistro (1200 x 740, scala 1,00); sotto il dettaglio della tavola sfalsato e il testo che chiude sul
    bordo destro della foto. Al telefono la sala alta 300, il testo, poi il dettaglio a filo destro."""
    foto = C(I(img('sala.jpg'), 'La sala del ristorante con il soffitto a travi e i tavoli apparecchiati con le tovaglie gialle '
                                'e bianche'), w=(83.33, 87.5, 100), gap=0, css='ldo-sala-foto')
    dettaglio = C(I(img('tavola.jpg'), "Salumi interi sull'ardesia e bottiglie di vino su un tavolo con la tovaglia gialla e bianca"),
                  w=(40, 40, 78), fisso=True, gap=0, mt=(96, 80, 0), css='ldo-dettaglio')
    parole = C(
        H('Cucina veneta', 'h2', style='h2c', color=VERDE),
        testo('<p>Musso con polenta, baccalà alla vicentina, bigoli alla boscaiola, fegato alla veneziana e i vini dei Colli '
              'Euganei: la cucina della tradizione, senza rivisitazioni.</p>', stile='primo', mt='s', max_w=(646, 646, 600)),
        testo("<p>Il menù cambia ogni giorno. Il venerdì sera c'è il pesce, ed è meglio prenotare; la domenica il ristorante "
              "è chiuso.</p>", mt='xs', max_w=(646, 646, 600)),
        link_isolato('Il menù', '/ristorante/#menu', mt='s'),
        grow=True, gap=0, mt='l', pad=(0, (0, 0, 20), 0, (0, 0, 20)), css='ldo-sala-testo')
    riga = C(dettaglio, parole, dir='row', dir_m='column-reverse', justify='between', align=('start', 'start', 'end'),
             gap=(64, 48, 48), w=(83.33, 87.5, 100), css='ldo-sala-riga')
    return C(foto, riga, RAW('', css=CSS_SALA), pad=('stacco', 0, 0, 0), gap=0, boxed=False, tag='section', anchor='cucina',
             css='ldo-sala')


CSS_STORIA = (
    # 2400 x 1333 in scala di grigi: titolo e testo nella stessa colonna, nel cielo a destra
    '.ldo-cartolina{aspect-ratio:2400/1333;padding:10.4% 64px 0 54.2%!important}'
    '.ldo-cart-testo{width:min(27.8vw,540px)!important;max-width:540px!important}'
    # 1024: la cartolina intera in alto, titolo e testo sotto, nel bianco
    '@media (max-width:1024px){'
    '.ldo-cartolina{aspect-ratio:auto;padding:calc(55.54% + 48px) 40px 0 40px!important;background-size:100% auto!important;'
    'background-position:center top!important}'
    '.ldo-cart-testo{width:100%!important;max-width:646px!important}'
    '}'
    # telefono: il taglio verticale (widget immagine) e sotto il testo
    '@media (max-width:767px){'
    '.ldo-cartolina{background-image:none!important;padding:32px 20px 0!important}'
    '.ldo-cart-par{line-height:1.6!important}'
    '}'
)


def storia():
    """H4: la cartolina della Trattoria al Leon d'Oro in bianco e nero, a tutta larghezza (2400 al massimo)."""
    descr = ("Cartolina d'epoca, Este, Viale di Via Restara: a sinistra l'insegna Trattoria al Leon d'Oro con alloggio, davanti "
             "alcuni uomini e un ragazzo con la bicicletta")
    parole = C(
        H('Con alloggio', 'h2', style='h2a', color=VERDE),
        testo(f"<p>Dai primi del Novecento era la Trattoria al Leon{NB}d'Oro con alloggio, vicino alla Porta Vecchia: un posto di "
              "ristoro per i viaggiatori e per i loro cavalli. Dagli anni Cinquanta è della famiglia Rubini.</p>",
              stile='foto', mt='s', css='ldo-cart-par'),
        gap=0, css='ldo-cart-testo')
    cartolina = C(parole, solo_lettori(descr, hide=['mobile']), img=img('cartolina-largo.jpg'), img_pos='center top', gap=0,
                  css='ldo-cartolina e-no-lazyload')
    return C(I(img('cartolina-alto.jpg'), descr, hide=['desktop', 'tablet']), cartolina, RAW('', css=CSS_STORIA),
             boxed=True, boxed_width=2400, pad='0', gap=0, mt='stacco', tag='section', anchor='storia', css='ldo-storia e-no-lazyload')


def colli():
    """H5: i Colli dal crinale, le due maglie gialle sulla strada bianca; titolo scuro nel cielo, testo sotto nel bianco."""
    return foto_con_titolo(
        'colli', 'Sui Colli<br>Euganei', 'colli-largo.jpg', (1920, 850),
        'Due ciclisti con la maglia gialla e nera su una strada bianca, fra i Colli Euganei',
        (63.6, (1040, 850)), ancora='colli',
        dopo=(testo("<p>Le bici passano la notte nel garage dell'albergo. Da Este passa l'anello ciclabile dei Colli, "
                    f"70{NB}km; chi vuole compagnia esce con il Team Este{NB}Bike, ritrovo in piazza alle 8.30 d'estate e "
                    f"alle{NB}9 d'inverno.</p>", max_w=(646, 646, 600)),
              link_isolato('Il bike hotel', '/bike-hotel/', mt='s')))


def camere_home():
    """H6: il campo giallo della home: tredici camere, i prezzi del listino in una frase, l'ospedale, email e telefono."""
    L = LISTINO
    return campo_giallo(
        'Tredici camere',
        f"Con la colazione, la singola costa {euro(L['singola'])} e la doppia {euro(L['doppia'])}; la mezza pensione "
        f"{euro(L['mezza'])} a persona, bevande incluse. È il listino del {L['anno']}.",
        'camera.jpg', 'Camera matrimoniale con il soffitto a travi e la finestra',
        testi=["<p>Chi assiste un ricoverato all'ospedale di Schiavonia trova qui una camera, e "
               '<a class="ldo-a" href="/ospedale-schiavonia/">le indicazioni per arrivarci</a> in navetta o in taxi.</p>'],
        azione='Prenota una camera', pos='45% center', ancora='prenota')


def home():
    return [('facciata', facciata()), ('targa', targa()), ('cucina', sala()), ('storia', storia()), ('colli', colli()),
            ('camere', camere_home())]


# ---------------------------------------------------------------------------------------------
# Componenti delle pagine interne
# ---------------------------------------------------------------------------------------------
def euro2(n):
    """Prezzo del listino, sempre nella stessa forma (50,00 €): l'allineamento a destra basta, niente colonne di cifre."""
    return f'{n},00{NB}€'


def apertura(titolo, primo, centro=False, altro=None, ancora='content', css='', pad_alto='xl'):
    """Il titolo della pagina (h1, 72 / 56 / 40) e il primo paragrafo, nel bianco sotto la testata, a 96 / 80 / 48 px.
    centro: titolo e testo centrati da 768 px in su (al telefono a sinistra, come il resto della pagina)."""
    al = ('center', 'center', 'left') if centro else 'left'
    figli = [H(titolo, 'h1', style='h1', color=VERDE, align=al),
             testo(f'<p>{primo}</p>', stile='primo', align=al, mt='s', max_w=(714, 714, 600))]
    if altro:
        figli.append(testo(f'<p>{altro}</p>', align=al, mt='xs', max_w=(646, 646, 600)))
    return C(*figli, align=('center', 'center', 'start') if centro else 'start', pad=(pad_alto, 'lato', 0, 'lato'), gap=0,
             boxed=False, tag='section', anchor=ancora, css=('ldo-apertura ' + css).strip())


def foto_filo(nome, foto, alt, lato='destro', foto_tel=None, alt_tel=None, h_tel=300, pos_tel='center center', larghezza=1200,
              w=(83.33, 87.5, 100)):
    """Foto a filo del bordo della pagina (specifica 3.6): 1200 px a 1440 (scala 1,00 per un file da 1200), l'87,5 % a 1024,
    tutta la larghezza al telefono. foto_tel: un altro ritaglio per il telefono; altrimenti al telefono la stessa foto alta
    h_tel, ritagliata (pos_tel)."""
    classe = f'ldo-filo-{nome}'
    css = f'.{classe}{{max-width:{larghezza}px!important}}'
    if foto_tel:
        figli = [I(img(foto), alt, hide=['mobile']), I(img(foto_tel), alt_tel or alt, hide=['desktop', 'tablet'])]
    else:
        figli = [I(img(foto), alt)]
        css += (f'@media (max-width:767px){{.{classe} img{{height:{h_tel}px!important;object-fit:cover;'
                f'object-position:{pos_tel}}}}}')
    return C(*figli, RAW('', css=css), w=w, gap=0, css=f'ldo-filo {classe}'), ('end' if lato == 'destro' else 'start')


def h2(titolo, stile='h2a', colore=VERDE, **p):
    return H(titolo, 'h2', style=stile, color=colore, **p)


def h3(titolo, colore=VERDE, **p):
    return H(titolo, 'h3', style='h3', color=colore, **p)


def voci(elenco, **p):
    """Righe di una carta (piatti, luoghi): una per riga, 18 px, senza puntini, senza filetti, senza prezzi. Un paragrafo per
    voce, con il rientro sospeso: una voce che va a capo non sembra due voci."""
    return T(''.join(f'<p>{v}</p>' for v in elenco), style='foto', color=INCHIOSTRO, css='ldo-voci', **p)


def colonne(blocchi, w=(31, 47, 100), gap=0, gap_r=(0, 48, 32), justify='between', **p):
    """Colonne di solo testo, distribuite sulla riga (a 1440 tre da 31 %, a 1024 due da 47 %, al telefono una): la distanza
    viene dallo spazio che avanza, così la somma resta sotto il 100 % (lezione di Benvegnù sulle griglie)."""
    return C(*[C(*b, w=w, gap=0) for b in blocchi], dir='row', wrap=True, justify=justify, align='start', gap=gap,
             gap_r=gap_r, **p)


def gruppo_carta(titolo, piatti):
    return [h3(titolo), voci(piatti, mt='xs')]


CSS_LARGO = (
    # colonne centrate larghe al massimo 880 (carta di ogni giorno) e 640 (listino)
    '.ldo-largo-640{max-width:640px!important;margin-left:auto!important;margin-right:auto!important}'
    '.ldo-largo-880{width:100%!important;max-width:880px!important;margin-left:auto!important;margin-right:auto!important}'
)


# ---------------------------------------------------------------------------------------------
# 02 CAMERE (specifica 7)
# ---------------------------------------------------------------------------------------------
def camere_apertura():
    """C1: il titolo nel bianco, poi la camera a due letti a filo destro, 1200 x 740 (scala 1,00): lo specchio della sala in
    home. Al telefono il ritaglio sui letti e sulla porta."""
    foto, lato = foto_filo('camere', 'camere-largo.jpg', 'Camera con due letti, il soffitto a travi e le pareti color ocra',
                           foto_tel='camere-alto.jpg')
    parole = C(H(f'Camera e<br>colazione', 'h1', style='h1', color=VERDE),
               testo(f'<p>Tredici camere singole, doppie e matrimoniali, con la colazione compresa nel prezzo: a{NB}Este, in '
                     f'Viale{NB}Fiume, a{NB}due passi dal centro e dal Castello Carrarese.</p>', stile='primo', mt='s',
                     max_w=(714, 714, 600)),
               pad=(0, 'lato', 0, 'lato'), gap=0)
    foto.p['mt'] = 'l'
    # la sezione allinea a destra: il testo è largo quanto la pagina, la foto (83 %) va a filo destro
    return C(parole, foto, align='end', pad=('xl', 0, 0, 0), gap=0, boxed=False, tag='section', anchor='content',
             css='ldo-camere-apertura')


def listino():
    """C2: il listino 2026 stretto al centro come una carta (640 px): l'unica tabella del sito, quattro righe con il prezzo
    allineato a destra e un filetto sotto ogni riga."""
    L = LISTINO

    def riga(nome, prezzo):
        return C(testo(f'<p>{nome}</p>', grow=True),
                 T(f'<p>{euro2(prezzo)}</p>', style='prezzo', color=INCHIOSTRO, fisso=True),
                 dir='row', justify='between', align='baseline', gap='s', pad=('xs', 0), border_bottom=1,
                 border_color=INCHIOSTRO)

    colonna = C(
        h2(f'Listino {L["anno"]}', stile='h2c', align='center'),
        h3('Camera e colazione', mt='l'),
        C(riga('Singola', L['singola']), riga('Doppia o matrimoniale', L['doppia']), gap=0, mt='xxs'),
        h3('Con i pasti, bevande incluse', mt='l'),
        C(riga('Mezza pensione, a persona', L['mezza']), riga('Pensione completa, a persona', L['completa']), gap=0, mt='xxs'),
        T('<p>Stagione unica.</p>', style='piccolo', color=INCHIOSTRO, mt='s'),
        gap=0, css='ldo-largo-640')
    return C(colonna, RAW('', css=CSS_LARGO), pad=('stacco', 'lato', 0, 'lato'), gap=0, boxed=False, tag='section',
             anchor='listino', css='ldo-listino')


CSS_RIGA_FOTO = (
    # foto a filo e testo accanto: al telefono la foto sopra, a tutta larghezza, e il testo sotto con i margini di pagina
    '.ldo-riga-foto .ldo-riga-img img{width:100%!important}'
)


def foto_e_testo(nome, foto, alt, figli, lato_foto='sinistro', w_foto=(50, 44.5, 100), ancora=None, mt='stacco', allinea='center',
                 larghezza_file=None):
    """Una foto a filo (sinistro o destro) e il testo accanto, nella stessa colonna titolo e paragrafi, centrato in verticale
    sulla foto; al telefono la foto sopra e il testo sotto (camere C3). larghezza_file: la foto non va oltre (sugli schermi
    larghi la percentuale la ingrandirebbe)."""
    immagine = C(I(img(foto), alt), w=w_foto, fisso=True, gap=0, css=f'ldo-riga-img ldo-riga-img-{nome}')
    if lato_foto == 'sinistro':
        parole = C(*figli, grow=True, gap=0, pad=(0, 'lato', 0, (64, 48, 20)), css='ldo-riga-testo')
        parti, dir_m = (immagine, parole), 'column'
    else:
        parole = C(*figli, grow=True, gap=0, pad=(0, (64, 48, 20), 0, 'lato'), css='ldo-riga-testo')
        parti, dir_m = (parole, immagine), 'column-reverse'
    css = CSS_RIGA_FOTO + (f'.ldo-riga-img-{nome}{{max-width:{larghezza_file}px!important}}' if larghezza_file else '')
    return C(*parti, RAW('', css=css), dir='row', dir_m=dir_m, align=(allinea, allinea, 'stretch'), gap=(0, 0, 32),
             mt=mt, pad='0', boxed=False, tag='section', anchor=ancora, css=f'ldo-riga-foto ldo-{nome}')


def in_albergo():
    """C3: il salottino a filo sinistro (840 x 630, scala 0,82; mai oltre i 1024 px del file) e accanto i servizi detti in una frase, non in icone."""
    return foto_e_testo('in-albergo', 'salottino.jpg', "Il salottino dell'albergo con la parete in legno e le poltrone verdi", [
        h2('In albergo'),
        testo("<p>Aria condizionata, TV satellitare, wi-fi e telefono in camera. L'auto resta nel parcheggio pubblico accanto "
              "all'albergo, la bici nel garage.</p>", mt='s', max_w=(646, 646, 600)),
        testo('<p>Al banco vi diamo indicazioni su cosa vedere a Este, sui sentieri dei Colli e su cantine e frantoi da '
              'visitare.</p>', mt='xs', max_w=(646, 646, 600)),
        testo("<p>Chi assiste un ricoverato all'ospedale di Schiavonia trova qui una camera.</p>", mt='xs',
              max_w=(646, 646, 600)),
        link_isolato("Per l'ospedale", '/ospedale-schiavonia/', mt='s'),
    ], w_foto=(58.33, 44.5, 100), ancora='servizi', larghezza_file=1024)


def camere_prenota():
    """C4: il campo giallo con il banco della reception."""
    return campo_giallo(
        'Prenota una camera',
        'Scriveteci le date di arrivo e di partenza e quante persone siete, adulti e bambini: vi rispondiamo con la '
        'disponibilità.',
        'reception.jpg', 'Il banco della reception in legno, con il casellario delle chiavi',
        dopo=('Il modulo di richiesta', '/prenota/'), ancora='prenota')


def camere():
    return [('apertura', camere_apertura()), ('listino', listino()), ('in-albergo', in_albergo()),
            ('prenota', camere_prenota())]


# ---------------------------------------------------------------------------------------------
# 03 RISTORANTE (specifica 8)
# ---------------------------------------------------------------------------------------------
def foto_piena(nome, foto, alt, larghezza_file, foto_tel, figli=(), ancora=None, mt='stacco'):
    """Una foto a tutta larghezza, mai più larga del file (la sezione si ferma alla sua larghezza, centrata); al telefono un
    ritaglio più alto. figli: quello che segue nel bianco, con i margini di pagina (bike hotel B1)."""
    sotto = [C(*figli, pad=(0, 'lato', 0, 'lato'), gap=0, mt='l')] if figli else []
    return C(I(img(foto), alt, hide=['mobile']), I(img(foto_tel), alt, hide=['desktop', 'tablet']), *sotto,
             boxed=True, boxed_width=larghezza_file, pad='0', gap=0, mt=mt, tag='section', anchor=ancora,
             css=f'ldo-piena ldo-piena-{nome}')


MENU_CARNE = [
    ('Antipasti', ['Affettati misti', 'Sopressa, polenta e funghi', 'Prosciutto crudo e melone', 'Bresaola, rucola e grana']),
    ('Primi', ["Pasta all'uovo al ragù o al pomodoro", 'Tagliolini in brodo', 'Zuppa di verdure', 'Pasta e fagioli',
               'Fettuccine al sugo', 'Spaghetti alla carbonara', 'Gnocchi della casa', 'Pasticcio della casa',
               'Cannelloni della casa', "Pasta all'arrabbiata", 'Risotti', 'Bigoli alla boscaiola']),
    ('Secondi', ['Braciola di maiale', 'Braciola di vitello', 'Costata di manzo o filetto', 'Bistecca di manzo o di tacchino',
                 'Fegato o cuore di vitellone', 'Fegato alla veneziana', 'Trippa alla parmigiana',
                 'Coniglio al forno o alla cacciatora', 'Spezzatino o ossobuco di vitello', 'Arrosto di vitello',
                 'Musso con polenta', 'Brasato di manzo', 'Bollito misto', 'Salsiccia e polenta', 'Vitello tonnato',
                 'Carpaccio', 'Roast beef', 'Baccalà alla vicentina']),
]
MENU_PESCE = [
    ('Antipasti', ['Insalata di mare', 'Carpaccio di pesce spada', 'Scampi alla busara', 'Granseola o granzoporro',   # [DA CONFERMARE: grafia]
                   'Gamberetti in salsa rosa o con rucola e grana', 'Sarde in saor', 'Cozze e vongole', 'Astice']),
    ('Primi', ['Spaghetti allo scoglio', 'Pasticcio di pesce', 'Spaghetti alla marinara', 'Tagliatelle alla busara',
               'Tagliatelle con le seppie', 'Gnocchi alla marinara', 'Risotti di pesce', 'Penne al salmone', 'Zuppa di pesce']),
    ('Secondi', ['Vitello di mare ai ferri', 'Sogliola ai ferri', 'Branzino ai ferri', 'Orata ai ferri', 'Scampi e capesante',
                 'Seppie ai ferri', 'Spiedini di gamberoni', 'Fritto misto',
                 'Baccalà alla vicentina o in insalata',                                                       # [DA CONFERMARE: lettura]
                 'Seppie alla veneta', 'Grigliata mista']),
]


def ristorante_apertura():
    """R1: il titolo centrato nel bianco, una frase del cliente: senza rivisitazioni (testo 7)."""
    return apertura('Senza<br>rivisitazioni',
                    'Cucina veneta preparata come vuole la tradizione: musso con polenta, baccalà alla vicentina, bigoli alla '
                    'boscaiola, fegato alla veneziana. I vini vengono da cantine dei Colli Euganei.', centro=True)


def ristorante_cucina():
    """R2: la padella sulla fiamma, a tutta larghezza (1600 al massimo, il file): il gesto della cucina, nessun testo sopra."""
    return foto_piena('padella', 'padella-largo.jpg', "Una padella di pasta sulla fiamma, nella cucina del Leon d'Oro", 1600,
                      'padella-alto.jpg', mt='xl')


def ristorante_menu():
    """R3: la carta di ogni giorno al centro del bianco, come la targa in home: titolo e due frasi centrati, poi le voci in
    due colonne strette (antipasti e primi, secondi e contorni), larghe insieme 880 px. Nessuna foto: la carta è l'oggetto.
    Due colonne e non tre: quattro antipasti accanto a diciotto secondi lasciavano un buco; così le colonne pareggiano."""
    al = ('center', 'center', 'left')
    carne = dict(MENU_CARNE)
    prima = gruppo_carta('Antipasti', carne['Antipasti']) + [h3('Primi', mt='l'), voci(carne['Primi'], mt='xs')]
    seconda = gruppo_carta('Secondi', carne['Secondi']) + [h3('Contorni', mt='l'),
                                                           voci(['Cotti, freschi e alla griglia'], mt='xs')]
    return C(
        h2('Ogni giorno', align=al),
        testo('<p>Questo è il menù tipo: le proposte cambiano ogni giorno.</p>', stile='primo', align=al, mt='s',
              max_w=(714, 714, 600)),
        testo("<p>In cucina c'è la signora Annalisa Brugin, madre dei titolari.</p>", align=al, mt='xs',
              max_w=(646, 646, 600)),
        colonne([prima, seconda], w=(44, 47, 100), gap_r=(0, 0, 48), mt='l', css='ldo-largo-880'),
        RAW('', css=CSS_LARGO), align=('center', 'center', 'start'), pad=('stacco', 'lato', 0, 'lato'), gap=0,
        boxed=False, tag='section', anchor='menu', css='ldo-menu-carne')


CSS_VENERDI = (
    # la sala a filo destro, mai più larga del file (1080); il titolo accanto, in basso, nel bianco
    '.ldo-venerdi-foto{max-width:1080px!important}'
)


def ristorante_pesce():
    """R4: il venerdì sera, pesce. La sala col vino a filo destro (1008 x 793 a 1440, scala 0,93) e accanto, in basso nel
    bianco, il titolo e la frase, come una didascalia grande; sotto, la carta del pesce in tre colonne (otto, nove e undici
    voci), allineata al margine di pagina come il titolo. A 1024 e al telefono la foto sopra, a tutta larghezza."""
    immagine = C(I(img('sala-vino.jpg'), "In sala una coppia a tavola, con il vino e il pane; alle pareti le stampe di Este"),
                 w=(70, 100, 100), fisso=True, gap=0, css='ldo-venerdi-foto')
    parole = C(h2('Il venerdì, pesce', stile='h2c'),
               testo("<p>Il venerdì sera c'è il menù di pesce, in omaggio alla cultura contadina di queste terre: è gradita "
                     'la prenotazione.</p>', stile='primo', mt='s', max_w=(560, 560, 600)),
               grow=True, gap=0, pad=((0, 48, 32), (48, 40, 20), 0, 'lato'), css='ldo-venerdi-testo')
    riga = C(parole, immagine, dir='row', dir_t='column-reverse', justify='end', align=('end', 'stretch', 'stretch'), gap=0)
    carta = colonne([gruppo_carta(t, v) for t, v in MENU_PESCE], gap_r=(0, 48, 32), mt='l', pad=(0, 'lato', 0, 'lato'))
    return C(riga, carta, RAW('', css=CSS_VENERDI), pad='0', gap=0, mt='stacco', boxed=False, tag='section', anchor='pesce',
             css='ldo-pesce')


def ristorante_prenota():
    """R5: il campo giallo con la cantinetta: si prenota per telefono."""
    return campo_giallo(
        'Prenota un tavolo',
        'La domenica il ristorante è chiuso. Il venerdì sera, per il pesce, è meglio prenotare.',
        'cantinetta.jpg', 'La cantinetta con lo scaffale dei vini e un tavolo apparecchiato con la tovaglia gialla',
        azione='Telefonate', ordine=('tel', 'email'), ancora='prenota')


def ristorante():
    return [('apertura', ristorante_apertura()), ('cucina', ristorante_cucina()), ('menu', ristorante_menu()),
            ('pesce', ristorante_pesce()), ('prenota', ristorante_prenota())]


# ---------------------------------------------------------------------------------------------
# 04 BIKE HOTEL (specifica 9)
# ---------------------------------------------------------------------------------------------
def bike_apertura():
    """B1: la strada bianca fra le vigne dal drone, a tutta larghezza subito sotto la testata; il titolo sotto, nel bianco."""
    return foto_piena(
        'vigne', 'vigne-largo.jpg', 'Due ciclisti su una strada bianca fra i vigneti dei Colli Euganei, visti dall\'alto', 1920,
        'vigne-alto.jpg', mt=0, ancora='content',
        figli=[H('Bike hotel', 'h1', style='h1', color=VERDE),
               testo(f"<p>Este è ai piedi dei Colli Euganei: si parte dall'albergo, in bici da strada o in mountain bike, e la "
                     f"sera la bici dorme nel garage.</p>", stile='primo', mt='s', max_w=(714, 714, 600))])


def bike_percorsi():
    """B2: i ciclisti con la maglia del Leon d'Oro a filo sinistro (1200 x 503, scala 0,75); sotto, i percorsi detti in frase,
    con le distanze dentro il testo (nessuna riga di numeri, nessun profilo altimetrico), in una colonna che chiude sul bordo
    destro della foto, come il testo sotto la sala in home: l'apertura ha il testo a sinistra, qui va a destra."""
    foto, _ = foto_filo('mura', 'mura.jpg', "Due ciclisti con la maglia gialla e nera del Leon d'Oro su una strada alberata, con "
                                            'una torre sullo sfondo', h_tel=300, pos_tel='35% center')
    colonna = C(
        h2('Da Este'),
        testo(f"<p>Per chi va piano c'è la ciclovia E2, l'anello che gira attorno ai Colli Euganei passando per i paesi: "
              f"70{NB}km, e Este è sul percorso.</p>", mt='s'),
        testo(f'<p>Per la mountain bike c\'è la Transeuganea, 60{NB}km nella natura dei Colli Euganei, e molti altri '
              'sentieri.</p>', mt='xs'),
        testo(f"<p>Il Leon d'Oro collabora da anni con il Team Este{NB}Bike e aiuta a organizzare le sue uscite in mountain bike "
              f"e in bici da strada: il ritrovo è in piazza, alle 8.30 d'estate e alle{NB}9 d'inverno. Al banco vi diamo consigli "
              'e indicazioni per i giri dei Colli.</p>', mt='xs'),
        w=(53.83, 62.5, 100), gap=0, css='ldo-percorsi-testo')
    riga = C(colonna, dir='row', justify=('end', 'end', 'start'), w=(83.33, 87.5, 100), gap=0, mt='l',
             pad=(0, (0, 0, 20), 0, (0, 0, 20)), css='ldo-percorsi-riga')
    return C(foto, riga, pad='0', gap=0, mt='stacco', boxed=False, tag='section', anchor='percorsi',
             css='ldo-percorsi')


def bike_prenota():
    """B3: il campo giallo con le due mountain bike sullo sterrato."""
    L = LISTINO
    return campo_giallo(
        'Camera e garage',
        f"Con la colazione, la singola costa {euro(L['singola'])} e la doppia {euro(L['doppia'])}; le bici restano nel garage "
        "privato dell'albergo.",
        'sterrato.jpg', 'Due ciclisti in maglia gialla in mountain bike su uno sterrato bianco',
        azione='Prenota una camera', dopo=('Il modulo di richiesta', '/prenota/'), ancora='prenota')


def bike_hotel():
    return [('apertura', bike_apertura()), ('percorsi', bike_percorsi()), ('prenota', bike_prenota())]


# ---------------------------------------------------------------------------------------------
# 05 PER L'OSPEDALE (specifica 10)
# ---------------------------------------------------------------------------------------------
def ospedale_apertura():
    """O1: pagina pratica: il titolo, dove è l'ospedale e come si chiama, che cosa offre l'albergo."""
    return apertura(
        f"Per<br>l'ospedale",
        f"Dal 5 novembre 2014 l'ospedale della Bassa Padovana è a Schiavonia, nel comune di Monselice: si chiama Ospedali Riuniti "
        f"Padova Sud Madre Teresa di Calcutta.",
        altro=f"Da sempre il Leon d'Oro dà una camera a chi deve stare vicino a un ricoverato. Per ogni altra informazione, "
              f"chiedete al banco.")


def ospedale_strade():
    """O2: le due strade per arrivare, due colonne di solo testo: niente riquadri, niente icone, niente filetti."""
    cols = C(
        C(h3('In navetta'),
          testo(f'<p>Il bus navetta parte dalla stazione delle corriere di Este; andata e ritorno costano 4,80{NB}€.</p>',
                mt='xs'), w=(40, 47, 100), gap=0),
        C(h3('In taxi'),
          testo(f'<p>Taxi Este, telefono <a class="ldo-a" href="tel:+393395040502">339{NB}5040502</a>.</p>', mt='xs'),
          w=(40, 47, 100), gap=0),
        dir='row', wrap=True, justify=('start', 'between', 'start'), align='start', gap=(64, 0, 0), gap_r=(0, 0, 32))
    return C(cols,
             testo(f"<p>Il centralino dell'ospedale risponde allo "
                   f'<a class="ldo-a" href="tel:+390429714111">0429{NB}714111</a>.</p>', mt='m', max_w=(646, 646, 600)),
             pad=(0, 'lato', 0, 'lato'), gap=0, mt='l', boxed=False, tag='section', anchor='come-arrivare',
             css='ldo-ospedale-strade')


def ospedale_camera():
    """O3: il campo giallo con la reception di sera; il telefono per primo."""
    L = LISTINO
    return campo_giallo(
        'Una camera vicina',
        f"Con la colazione, la singola costa {euro(L['singola'])} e la doppia {euro(L['doppia'])}; con la mezza pensione "
        f"{euro(L['mezza'])} a persona, bevande incluse. Il ristorante è nella stessa casa.",
        'reception-sera.jpg', 'La reception di sera, con la lampada verde accesa sul banco',
        azione='Chiamate o scrivete', ordine=('tel', 'email'), ancora='prenota')


def ospedale():
    return [('apertura', ospedale_apertura()), ('strade', ospedale_strade()), ('camera', ospedale_camera())]


# ---------------------------------------------------------------------------------------------
# 06 DOVE SIAMO (specifica 11)
# ---------------------------------------------------------------------------------------------
MAPPA_URL = 'https://www.google.com/maps/search/?api=1&query=45.2267456,11.6543665'


def dove_apertura():
    """D1: Este dal drone a tutta larghezza, l'indirizzo nel cielo; al telefono il titolo sotto la foto, in verde."""
    return foto_con_titolo(
        'este', f'Viale<br>Fiume{NB}20', 'este-largo.jpg', (1920, 850),
        "Este vista dall'alto, con i tetti del centro, il campanile e il verde delle mura", (50, (1040, 850)),
        stile='h1', livello='h1', pad_alto='4.44%', ancora='content', mt=0, foto_telefono='este-alto.jpg')


def dove_arrivare():
    """D2: come arrivare, in una colonna; un link a Google Maps al posto della mappa incorporata (niente cookie di terzi)."""
    return C(
        testo('<p>Siamo a Este, a due passi dal centro e dal Castello Carrarese, ai piedi dei Colli Euganei, poco lontano dalle '
              'terme di Abano e Montegrotto, in provincia di Padova.</p>', stile='primo', max_w=(714, 714, 600)),
        testo("<p>Accanto all'albergo c'è il parcheggio pubblico. Dalla stazione delle corriere di Este parte la navetta per "
              "l'ospedale di Schiavonia.</p>", mt='xs', max_w=(646, 646, 600)),
        T(f'<p>{INDIRIZZO}</p>', style='contatto', color=VERDE, mt='m'),
        link_isolato('Apri in Google Maps', MAPPA_URL, mt='s'),
        pad=(0, 'lato', 0, 'lato'), gap=0, mt='l', boxed=False, tag='section', anchor='come-arrivare', css='ldo-arrivare')


def dove_intorno():
    """D3: i Colli dal drone a filo destro, poi i luoghi da vedere in due colonne di nomi e una riga per le gite in giornata."""
    foto, _ = foto_filo('borgo', 'borgo.jpg', 'Colli a cono, vigneti e un borgo, ripresi dall\'alto sui Colli Euganei',
                        h_tel=300, pos_tel='40% center')
    a_este = [h3('A Este'),
              testo('<p>Una città murata, nata con i Paleoveneti, colonia romana, poi degli Estensi, dei Carraresi e di '
                    'Venezia.</p>', mt='xs'),
              voci(['Castello Carrarese', 'Museo Nazionale Atestino', 'Duomo di Santa Tecla, con la pala di Giambattista Tiepolo',
                    'Chiesa di San Martino', 'Santuario della Madonna delle Grazie'], mt='s'),
              testo("<p>All'ufficio turistico IAT trovate orari, opuscoli e la Ceramica Estense.</p>", mt='s')]
    sui_colli = [h3('Sui Colli'),
                 testo('<p>Colline di origine vulcanica, parco regionale dal 1989: vini, olio, sentieri a piedi e in bici. Vi '
                       'diciamo noi quali cantine e frantoi visitare.</p>', mt='xs'),
                 voci(['Arquà Petrarca', 'Monte Gemola e Villa Beatrice', 'Buso della Casara a Valnogaredo',
                       'Fonte Regina a Torreglia', 'Cascata Schivanoia a Teolo'], mt='s')]
    parole = C(
        h2('Intorno'),
        colonne([a_este, sui_colli], w=(40, 47, 100), gap=(64, 0, 0), gap_r=(0, 0, 40), justify=('start', 'between', 'start'),
                mt='l'),
        testo('<p>In auto, da Este si va in giornata a Padova, Vicenza, Verona, Venezia, Chioggia, Rovigo, Ferrara e '
              'Mantova.</p>', mt='l', max_w=(646, 646, 600)),
        pad=(0, 'lato', 0, 'lato'), gap=0, mt='l')
    return C(foto, parole, align='end', pad='0', gap=0, mt='stacco', boxed=False, tag='section', anchor='cosa-vedere',
             css='ldo-intorno')


def dove_porta():
    """D4: il campo giallo con la porta e l'insegna nera col leone, per riconoscere l'ingresso."""
    return campo_giallo(
        "L'insegna col leone",
        "L'insegna nera col leone è accanto alla porta, sotto la scritta Albergo Leon d'Oro dipinta sul muro giallo.",
        'porta.jpg', "La porta del Leon d'Oro di sera, con l'insegna nera e il leone dorato accanto all'ingresso",
        testi=[f'<p>{INDIRIZZO}. Il ristorante è chiuso la domenica.</p>'], ordine=('tel', 'email'), pos='right center',
        ancora='indirizzo')


def dove_siamo():
    return [('apertura', dove_apertura()), ('come-arrivare', dove_arrivare()), ('intorno', dove_intorno()),
            ('porta', dove_porta())]


# ---------------------------------------------------------------------------------------------
# 07 PRENOTA (specifica 12 e 13)
# ---------------------------------------------------------------------------------------------
CF7_TITOLO = "Richiesta camera Leon d'Oro"
CF7 = f'[contact-form-7 title="{CF7_TITOLO}"]'

CSS_MODULO = (
    # il modulo sul giallo: campi bianchi con il bordo inchiostro, etichette sopra, errori a parole (nessun rosso, che sul
    # giallo non reggerebbe), arrivo e partenza affiancati da 768 px in su, adulti e bambini sempre affiancati
    f'.ldo-modulo .wpcf7 label,.ldo-modulo .ldo-scelta{{display:block;margin:0;font:600 16px/1.3 {FONT_CSS};color:{INCHIOSTRO};'
    'letter-spacing:0;text-transform:none}'
    '.ldo-modulo .wpcf7 p{margin:0}.ldo-modulo .wpcf7 br{display:none}'
    '.ldo-modulo .wpcf7-form-control-wrap{display:block}'
    '.ldo-modulo .ldo-campi{display:grid;grid-template-columns:1fr 1fr;column-gap:16px;row-gap:24px}'
    '.ldo-modulo .ldo-campi>p{display:contents}'
    '.ldo-modulo .ldo-tutta{grid-column:1/-1}'
    f'.ldo-modulo .ldo-nota{{display:block;margin-top:4px;font:400 15px/1.4 {FONT_CSS};color:{INCHIOSTRO}}}'
    '.ldo-modulo input[type=text],.ldo-modulo input[type=email],.ldo-modulo input[type=tel],.ldo-modulo input[type=date],'
    '.ldo-modulo input[type=number],.ldo-modulo select,.ldo-modulo textarea{display:block;width:100%;box-sizing:border-box;'
    f'margin:8px 0 0;background:{BIANCO};border:2px solid {INCHIOSTRO};border-radius:2px;box-shadow:none;padding:12px 16px;'
    f'height:48px;font:400 17px/1.3 {FONT_CSS};color:{INCHIOSTRO};letter-spacing:0;text-transform:none}}'
    '.ldo-modulo select{padding-top:10px;padding-bottom:10px}'
    '.ldo-modulo textarea{height:auto;min-height:144px;resize:vertical}'
    f'.ldo-modulo input::placeholder,.ldo-modulo textarea::placeholder{{color:{GRIGIO};opacity:1}}'
    f'.ldo-modulo input:focus,.ldo-modulo select:focus,.ldo-modulo textarea:focus{{border-color:{VERDE};'
    f'outline:3px solid {INCHIOSTRO};outline-offset:2px}}'
    f'.ldo-modulo input[type=checkbox],.ldo-modulo input[type=radio]{{accent-color:{VERDE};flex:0 0 20px;width:20px;height:20px;'
    'margin:2px 0 0}'
    '.ldo-modulo .wpcf7-list-item{display:block;margin:0}'
    '.ldo-modulo .wpcf7-list-item label{display:flex;align-items:flex-start;gap:12px;min-height:44px;padding:10px 0 0;'
    'font-weight:400;font-size:17px;line-height:1.4}'
    '.ldo-modulo .wpcf7-radio,.ldo-modulo .wpcf7-checkbox,.ldo-modulo .wpcf7-acceptance{display:block;margin-top:4px}'
    f'.ldo-modulo .wpcf7-acceptance a{{color:{INCHIOSTRO};text-decoration:underline;text-decoration-thickness:2px;'
    'text-underline-offset:4px;font-weight:600}'
    f'.ldo-modulo .wpcf7-acceptance a:hover,.ldo-modulo .wpcf7-acceptance a:focus-visible{{color:{VERDE}}}'
    f'.ldo-modulo input[type=submit]{{background:{VERDE};color:{BIANCO};border:0;border-radius:2px;padding:12px 24px;height:auto;'
    f'font:600 16px/1.2 {FONT_CSS};letter-spacing:0;text-transform:none;cursor:pointer;margin-top:8px;box-shadow:none}}'
    '.ldo-modulo input[type=submit]:hover,.ldo-modulo input[type=submit]:active,.ldo-modulo input[type=submit]:focus'
    f'{{background:{INCHIOSTRO};color:{BIANCO}}}'
    f'.ldo-modulo input[type=submit]:focus-visible{{outline:3px solid {INCHIOSTRO};outline-offset:3px}}'
    f'.ldo-modulo input[type=submit]:disabled{{background:{CHIARO};color:{GRIGIO};cursor:not-allowed}}'
    f'.ldo-modulo .wpcf7-not-valid{{border:3px solid {INCHIOSTRO}!important}}'
    f'.ldo-modulo .wpcf7-not-valid-tip{{color:{INCHIOSTRO};font:600 15px/1.3 {FONT_CSS};margin-top:8px}}'
    ".ldo-modulo .wpcf7-not-valid-tip::before{content:'Errore: '}"
    f'.ldo-modulo .wpcf7 form .wpcf7-response-output{{margin:24px 0 0;padding:16px;border:0;background:{BIANCO};'
    f'color:{INCHIOSTRO};font:400 17px/1.4 {FONT_CSS}}}'
    '.ldo-modulo .wpcf7-spinner{margin:8px 0 0 16px}'
    '@media (max-width:767px){.ldo-modulo .ldo-data{grid-column:1/-1}.ldo-modulo input[type=submit]{width:100%}}'
)

CSS_SCRIVI = (
    # il bottone del fallback (al posto del modulo): verde, hover inchiostro, mai opacità
    f'.ldo-modulo a.ldo-scrivi{{display:inline-block;background:{VERDE}!important;color:{BIANCO}!important;padding:12px 24px;'
    f'border-radius:2px;font:600 16px/1.2 {FONT_CSS};text-decoration:none!important}}'
    f'.ldo-modulo a.ldo-scrivi:hover,.ldo-modulo a.ldo-scrivi:focus{{background:{INCHIOSTRO}!important;color:{BIANCO}!important}}'
    f'.ldo-modulo a.ldo-scrivi:focus-visible{{outline:3px solid {INCHIOSTRO};outline-offset:3px}}'
    f'.ldo-modulo .ldo-alt p{{font:400 19px/1.6 {FONT_CSS}!important;color:{INCHIOSTRO}!important;margin:0 0 24px!important}}'
    '.ldo-modulo .ldo-alt p:last-child{margin-bottom:0!important}'
)


def prenota_apertura():
    """P1: la targa con la chiave al centro, il titolo sotto e una frase: come si chiede una camera."""
    return oggetto_centrato(
        'prenota-targa', 'targa.jpg', 'La targa in ceramica ALBERGO con la chiave e le due stelle, sul muro giallo della facciata',
        [H('Prenota', 'h1', style='h1', color=VERDE, align='center'),
         testo('<p>Diteci le date, quante persone siete e come volete stare: vi rispondiamo con la disponibilità e le opzioni. '
               'Per un tavolo, telefonate.</p>', stile='primo', align='center', max_w=(714, 714, 600))],
        ancora='content', pad_alto='xl')


def prenota_richiesta():
    """P2: il campo giallo grande, con il modulo dentro: a sinistra chi risponde e i recapiti, a destra il modulo (640 px).
    Nel fallback HTML, dove Contact Form 7 non c'è, un bottone apre un'email con le voci già scritte."""
    corpo = ('Nome e cognome:\nTelefono:\nArrivo:\nPartenza:\nAdulti:\nBambini (età):\n'
             'Camera (singola, doppia o matrimoniale, più camere):\n'
             'Trattamento (camera e colazione, mezza pensione, pensione completa):\nGarage per la bici (sì o no):\nNote:\n')
    alternativa = (f'<div class="ldo-alt"><p>Il bottone qui sotto apre un\'email già indirizzata a noi, con le voci da '
                   'compilare: date, persone, camera e trattamento.</p>'
                   f'<p><a class="ldo-scrivi" href="{mailto("Richiesta camera", corpo)}">Scrivi un\'email</a></p></div>')
    parole = C(
        h2('Scriveteci', stile='h2b', colore=INCHIOSTRO),
        testo("<p>Rispondiamo all'indirizzo che ci lasciate. Se preferite, chiamate o scrivete direttamente.</p>",
              link=INCHIOSTRO, hover=VERDE, mt='s', max_w=(570, 570, 600)),
        C(*[testo(f'<p>{v}</p>', stile='contatto', link=INCHIOSTRO, hover=VERDE, css='ldo-intero', fisso=True)
            for v in (f'<a class="ldo-a" href="{TEL_LINK}">{TEL}</a>', f'<a class="ldo-a" href="mailto:{EMAIL}">{EMAIL}</a>')],
          gap=(16, 16, 16), mt='m'),
        testo(f'<p>Fax {FAX}</p>', mt='xs'),
        w=(43, 100, 100), gap=0, css='ldo-richiesta-testo')
    modulo = C(SHORTCODE(CF7, alternativa_html=alternativa, stile='testo', colore=INCHIOSTRO),
               RAW('', css=CSS_MODULO, solo_elementor=True), RAW('', css=CSS_SCRIVI),
               w=(49, 100, 100), gap=0, css='ldo-modulo')
    return C(parole, modulo, dir='row', dir_t='column', justify='between', align='start', gap=0, gap_r=(0, 48, 48),
             pad=('campo', 'lato', 'campo', 'lato'), bg=GIALLO, boxed=False, mt='xl', tag='section', anchor='richiesta',
             css='ldo-campo ldo-richiesta')


def prenota_tavolo():
    """P3: una riga per il tavolo, nel bianco dopo il campo giallo: qui il giallo non è l'ultima sezione."""
    return C(
        h2('Un tavolo', stile='h2c'),
        testo("<p>Per il ristorante basta una telefonata. Il venerdì sera c'è il pesce ed è gradita la prenotazione; la "
              'domenica siamo chiusi.</p>', mt='s', max_w=(646, 646, 600)),
        testo(f'<p><a class="ldo-a" href="{TEL_LINK}">{TEL}</a></p>', stile='contatto', css='ldo-intero', mt='s', fisso=True),
        pad=('stacco', 'lato', 'stacco', 'lato'), gap=0, boxed=False, tag='section', anchor='tavolo', css='ldo-tavolo')


def prenota():
    return [('apertura', prenota_apertura()), ('richiesta', prenota_richiesta()), ('tavolo', prenota_tavolo())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': tipografica(home),
     'titolo_seo': "Albergo Ristorante Leon d'Oro, Este (PD)",
     'descrizione': 'Albergo e trattoria in Viale Fiume 20 a Este: cucina veneta, tredici camere con la colazione, garage per le bici, '
                    "vicino all'ospedale di Schiavonia."},
    {'slug': '02-camere', 'titolo': 'Camere', 'sezioni': tipografica(camere),
     'titolo_seo': "Camere a Este, listino 2026, Leon d'Oro",
     'descrizione': 'Tredici camere a Este, singole, doppie e matrimoniali, con la colazione: listino 2026, mezza pensione e '
                    'pensione completa con le bevande.'},
    {'slug': '03-ristorante', 'titolo': 'Ristorante', 'sezioni': tipografica(ristorante),
     'titolo_seo': "Ristorante di cucina veneta a Este, Leon d'Oro",
     'descrizione': 'Musso con polenta, baccalà alla vicentina, bigoli, fegato alla veneziana; il menù di ogni giorno e il pesce '
                    'del venerdì sera. Chiuso la domenica.'},
    {'slug': '04-bike-hotel', 'titolo': 'Bike hotel', 'sezioni': tipografica(bike_hotel),
     'titolo_seo': "Bike hotel a Este sui Colli Euganei, Leon d'Oro",
     'descrizione': 'Garage per le bici, l\'anello ciclabile dei Colli da 70 km, la Transeuganea e le uscite con il Team Este Bike.'},
    {'slug': '05-ospedale-schiavonia', 'titolo': "Per l'ospedale", 'sezioni': tipografica(ospedale),
     'titolo_seo': "Albergo vicino all'ospedale di Schiavonia, Leon d'Oro",
     'descrizione': "Una camera a Este per chi assiste un ricoverato all'Ospedale di Schiavonia: come arrivare in navetta o in "
                    'taxi.'},
    {'slug': '06-dove-siamo', 'titolo': 'Dove siamo', 'sezioni': tipografica(dove_siamo),
     'titolo_seo': "Dove siamo: Viale Fiume 20, Este, Leon d'Oro",
     'descrizione': "Come arrivare al Leon d'Oro a Este e cosa vedere in città e sui Colli Euganei."},
    {'slug': '07-prenota', 'titolo': 'Prenota', 'sezioni': tipografica(prenota),
     'titolo_seo': "Prenota una camera, Leon d'Oro Este",
     'descrizione': 'Richiesta di prenotazione: date, persone e trattamento. Rispondiamo con la disponibilità.'},
]
