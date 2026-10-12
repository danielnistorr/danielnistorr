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
  Ultimate Addons cambiano a 767 e 1024 px, la specifica vuole il bottone "Menu" a 820 px con telefono e "Prenota" nel pannello.
"""
from urllib.parse import quote

import motore as m
from motore import C, H, T, I, RAW

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
    'h1':        _st('800', (72, 56, 40), 0.98, -1.0, True),     # titolo delle pagine interne
    'h2a':       _st('800', (44, 40, 30), 1.05, -0.4, True),     # titoli su foto o accanto a foto grandi
    'h2b':       _st('800', (40, 36, 30), 1.05, -0.4, True),     # titoli del campo giallo
    'h2c':       _st('800', (36, 36, 30), 1.05, -0.4, True),     # titoli accanto al testo
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


def mailto(oggetto, corpo=''):
    url = f'mailto:{EMAIL}?subject={quote(oggetto)}'
    return url + ('&body=' + quote(corpo) if corpo else '')


# voci del menu, in quest'ordine (specifica 4.1); "Prenota" è il bottone della testata, non una voce
VOCI_MENU = [('camere', '/camere/'), ('ristorante', '/ristorante/'), ('bike hotel', '/bike-hotel/'),
             ("per l'ospedale", '/ospedale-schiavonia/'), ('dove siamo', '/dove-siamo/')]


# ---------------------------------------------------------------------------------------------
# CSS condiviso (nel widget HTML della testata: c'è in ogni pagina, in Elementor e nel fallback)
# ---------------------------------------------------------------------------------------------
CSS_SITO = (
    'body{font-synthesis:none}'
    # testo solo per chi legge con la sintesi vocale (la descrizione delle foto di sfondo)
    '.ldo-sr{position:absolute!important;width:1px!important;height:1px!important;overflow:hidden!important;'
    'clip:rect(1px,1px,1px,1px)!important;white-space:nowrap!important;margin:0!important;padding:0!important}'
    # link nel testo: sottolineatura spessa 2 px a 6 px dal testo (specifica 3.5)
    '.ldo-sott a{text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important}'
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
)

# ---------------------------------------------------------------------------------------------
# Testata: logo, menu, telefono, "Prenota"; sotto 820 px logo, "Chiama" e "Menu" (specifica 4.1)
# ---------------------------------------------------------------------------------------------
NAV_LINK = f"font:400 16px/1.2 {FONT_CSS};color:{INCHIOSTRO};text-decoration:none;white-space:nowrap;display:inline-block;padding:12px 0"
SOTTOLINEA = 'text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px'
CSS_NAV = (
    # il pannello del telefono si apre sotto tutta la testata: la testata è il riferimento, i widget no
    '.ldo-testata{position:relative;overflow-x:clip}'
    '.ldo-testata .elementor-widget-html,.ldo-testata .ldo-w{position:static!important}'
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
    # il bottone "Menu": il tema Hello colora i bottoni di rosa, qui ogni stato ha il suo colore
    f'.ldo-nav .ldo-apri,.ldo-nav .ldo-apri:focus{{font:600 16px/1 {FONT_CSS};background:{BIANCO};color:{INCHIOSTRO};'
    f'border:2px solid {INCHIOSTRO};border-radius:2px;padding:12px 16px;min-height:44px;min-width:44px;cursor:pointer;'
    'box-shadow:none;text-transform:none;letter-spacing:0;margin:0}'
    f'.ldo-nav .ldo-apri:hover,.ldo-nav .ldo-apri[aria-expanded=true]{{background:{INCHIOSTRO};color:{BIANCO};border-color:{INCHIOSTRO}}}'
    f'.ldo-nav .ldo-chiama{{font:600 16px/1.2 {FONT_CSS};color:{VERDE};{SOTTOLINEA};padding:12px 0;white-space:nowrap}}'
    f'.ldo-nav .ldo-chiama:hover{{color:{INCHIOSTRO}}}'
    '@media (max-width:1100px){.ldo-nav .ldo-tel{display:none}.ldo-nav,.ldo-nav .ldo-pannello{gap:24px}.ldo-nav .ldo-menu{gap:24px}}'
    '@media (max-width:820px){'
    '.ldo-nav{gap:16px}'
    '.ldo-nav .ldo-chiama,.ldo-nav .ldo-apri{display:inline-block}'
    f'.ldo-nav .ldo-pannello{{position:absolute;left:0;right:0;top:100%;z-index:50;background:{BIANCO};flex-direction:column;'
    'align-items:flex-start;gap:24px;padding:16px 40px 32px}'
    '.ldo-nav .ldo-menu{flex-direction:column;gap:0}'
    '.ldo-nav .ldo-menu a{font-size:20px}'
    '.ldo-nav .ldo-pannello .ldo-tel{display:inline-block;font-size:20px}'
    '.ldo-nav.ldo-js .ldo-pannello{display:none}'
    '.ldo-nav.ldo-js.aperto .ldo-pannello{display:flex}'
    # senza JavaScript il bottone non serve: il menu resta visibile in colonna sotto la testata
    '.ldo-nav:not(.ldo-js) .ldo-apri{display:none}'
    '.ldo-nav:not(.ldo-js) .ldo-pannello{position:static;padding:0}'
    '.ldo-nav:not(.ldo-js){flex-direction:column;align-items:flex-end}'
    '}'
    '@media (max-width:767px){.ldo-nav .ldo-pannello{padding:16px 20px 32px}}'
)

JS_NAV = (
    "(function(){function via(){document.querySelectorAll('.ldo-nav').forEach(function(n){if(n.dataset.ok)return;n.dataset.ok=1;"
    "n.classList.add('ldo-js');var b=n.querySelector('.ldo-apri'),p=n.querySelector('.ldo-pannello');"
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
    "if(window.matchMedia){var mq=matchMedia('(min-width:821px)');var chiudi=function(){if(mq.matches)apri(false)};"
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
    logo = I(img('logo-leondoro-verde.png'), "Albergo Leon d'Oro, Este", link='/', link_label="Albergo Leon d'Oro, Este: pagina iniziale",
             w_img=(134, 134, 105), fisso=True, css='ldo-logo')
    return C(logo, RAW(nav_html(), css=CSS_SITO + CSS_NAV), dir='row', justify='between', align='center', gap='m',
             pad=(16, 'lato'), bg=BIANCO, boxed=False, tag='header', css='ldo-testata')


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
    return C(righe, riga_link, RAW('', css=CSS_PIEDE), bg=VERDE, pad=((64, 64, 48), 'lato', (48, 48, 40), 'lato'), gap=0,
             boxed=False, tag='footer', css='ldo-piede')


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
                    pad_alto='6.6%', pad_telefono=24, ancora=None, mt='stacco', dopo=()):
    """Foto a tutta larghezza con il titolo nel cielo, in alto a sinistra (home H5, Dove siamo D1): sfondo di contenitore,
    larghezza massima uguale al file, altezza in proporzione al file; al telefono la stessa foto ritagliata dallo sfondo
    (pos_telefono: posizione orizzontale in %, rapporto (w, h) del ritaglio) e il titolo resta nel cielo.
    dopo: widget sotto la foto, nel bianco, con il margine di pagina."""
    w, h = misura
    (px, (tw, th)) = pos_telefono
    classe = f'ldo-pieno-{nome}'
    css = (f'.{classe} .ldo-pieno-foto{{aspect-ratio:{w}/{h};padding-top:{pad_alto}!important}}'
           f'@media (max-width:767px){{.{classe} .ldo-pieno-foto{{aspect-ratio:{tw}/{th};background-position:{px}% top!important;'
           f'padding-top:{pad_telefono}px!important}}}}')
    pieno = C(H(titolo, livello, style=stile, color=colore), solo_lettori(descrizione), img=img(foto), img_pos='center top',
              pad=(0, 'lato', 0, 'lato'), gap=0, css='ldo-pieno-foto e-no-lazyload')
    figli = [pieno]
    if dopo:
        figli.append(C(*dopo, pad=(0, 'lato', 0, 'lato'), gap=0, mt='l'))
    figli.append(RAW('', css=css))
    return C(*figli, boxed=True, boxed_width=w, pad='0', gap=0, mt=mt, tag='section', anchor=ancora, css=classe)


# ---------------------------------------------------------------------------------------------
# HOME (specifica 6)
# ---------------------------------------------------------------------------------------------
CSS_FACCIATA = (
    f'.ldo-facciata{{background-color:{NOTTE}}}'
    # 1680 x 826: l'altezza segue la larghezza, mai oltre il file; il titolo in alto a destra, sopra gli alberi
    '.ldo-fac-foto{position:relative;aspect-ratio:1680/826;padding-top:8.4%!important}'
    # velatura scura solo dietro il titolo (nessun colore: il nero caldo della foto)
    '.ldo-fac-foto::before{content:""!important;display:block;position:absolute;top:0;left:0;width:100%;height:100%;'
    'background:radial-gradient(ellipse 34% 46% at 79% 30%,rgba(14,9,4,.5),rgba(14,9,4,0));opacity:1;mix-blend-mode:normal;'
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
             anchor='contenuto', css='ldo-facciata')


CSS_TARGA = (
    '.ldo-targa-foto img{margin-left:auto;margin-right:auto}'
    '@media (max-width:767px){.ldo-frase{line-height:1.4!important}}'
)


def targa():
    """H2: la targa in ceramica ALBERGO al centro, sola, e una frase: dove siamo e cosa si trova."""
    return C(
        I(img('targa.jpg'), 'La targa in ceramica ALBERGO con la chiave e le due stelle, sul muro giallo della facciata',
          w_img=(480, 400, 273), css='ldo-targa-foto'),
        T(f'<p>Albergo e trattoria a{NB}Este, in Viale{NB}Fiume{NB}20: la cena, la camera e il garage per la{NB}bici, '
          f'a{NB}due passi dal Castello Carrarese.</p>', style='frase', color=INCHIOSTRO, align='center',
          max_w=(750, 650, 600), mt='l', css='ldo-frase'),
        RAW('', css=CSS_TARGA),
        align='center', pad=('stacco', 'lato', 0, 'lato'), gap=0, boxed=False, tag='section', css='ldo-targa')


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
             boxed=True, boxed_width=2400, pad='0', gap=0, mt='stacco', tag='section', anchor='storia', css='ldo-storia')


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


PAGINE = [
    {'slug': '01-home', 'titolo': 'Home', 'sezioni': home,
     'titolo_seo': "Albergo Ristorante Leon d'Oro, Este (PD)",
     'descrizione': 'Albergo e trattoria in Viale Fiume 20 a Este: cucina veneta, tredici camere con la colazione, garage per le bici, '
                    "vicino all'ospedale di Schiavonia."},
]
