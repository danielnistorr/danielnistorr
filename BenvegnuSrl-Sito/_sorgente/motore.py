# -*- coding: utf-8 -*-
"""
Motore del generatore: una pagina descritta una volta sola (albero di nodi) produce
  A) il template Elementor .json (solo widget della versione gratuita, nessun riferimento ai globali del kit)
  B) l'HTML+CSS autosufficiente per il widget HTML di Elementor, un file per sezione
  C) l'anteprima HTML completa della pagina.

Target dichiarato: Elementor 4.3.3 (versione gratuita), contenitori flexbox, WordPress 7.1, tema Hello Elementor 3.5.
Il formato del file è quello prodotto da "Esporta template" (chiavi content, page_settings, version, title, type).
"""
import hashlib
import html as _html
import json

# ---------------------------------------------------------------------------------------------
# Design token: palette, font, scala tipografica e spaziature. Tutto passa da qui.
# ---------------------------------------------------------------------------------------------
NERO = '#111111'
BIANCO = '#FFFFFF'
ROSSO = '#9F2E29'          # il rosso cuoio già usato dal sito attuale (site.css)
NERO_75 = '#4A4A4A'        # nero al 75% su bianco, per i testi secondari (contrasto 8.9:1)
BIANCO_70 = '#C9C9C9'      # bianco al 70% su nero, per i testi secondari su fondo nero (contrasto 11:1)
LINEA = '#D6D6D6'          # nero al 16%, solo per filetti e bordi
LINEA_SCURA = '#3A3A3A'    # filetti su fondo nero

FONT_TITOLI = 'Barlow Condensed'
FONT_TESTO = 'Barlow'
GOOGLE_FONTS = ('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700'
                '&family=Barlow:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap')

LARGHEZZA = 1280           # larghezza del contenuto nei contenitori "boxed"
BP_TABLET = 1024           # breakpoint Elementor di default
BP_MOBILE = 767

# stili di testo: famiglia, peso, dimensioni (desktop, tablet, mobile), interlinea (em), spaziatura lettere (px), maiuscolo
STILI = {
    'display': dict(f=FONT_TITOLI, w='700', s=(84, 66, 44), lh=0.94, ls=0, up=True),
    'h1':      dict(f=FONT_TITOLI, w='700', s=(72, 56, 40), lh=0.96, ls=0, up=True),
    'h2':      dict(f=FONT_TITOLI, w='700', s=(52, 42, 34), lh=1.0, ls=0, up=True),
    'h3':      dict(f=FONT_TITOLI, w='700', s=(28, 26, 22), lh=1.08, ls=0.3, up=True),
    'h4':      dict(f=FONT_TESTO, w='700', s=(19, 18, 17), lh=1.3, ls=0, up=False),
    'num':     dict(f=FONT_TITOLI, w='700', s=(64, 54, 44), lh=0.9, ls=0, up=False),
    'num_s':   dict(f=FONT_TITOLI, w='700', s=(40, 36, 30), lh=0.95, ls=0, up=False),
    'tel':     dict(f=FONT_TITOLI, w='700', s=(60, 52, 40), lh=1.0, ls=0, up=False),
    'lead':    dict(f=FONT_TESTO, w='400', s=(22, 20, 19), lh=1.5, ls=0, up=False),
    'body':    dict(f=FONT_TESTO, w='400', s=(18, 17, 17), lh=1.6, ls=0, up=False),
    'small':   dict(f=FONT_TESTO, w='400', s=(15, 15, 15), lh=1.55, ls=0, up=False),
    'label':   dict(f=FONT_TESTO, w='600', s=(14, 14, 13), lh=1.3, ls=1.6, up=True),
    'btn':     dict(f=FONT_TESTO, w='700', s=(15, 15, 15), lh=1.2, ls=1.2, up=True),
    'nav':     dict(f=FONT_TESTO, w='600', s=(15, 15, 15), lh=1.2, ls=1.0, up=True),
}

# spaziature (desktop, tablet, mobile): una sola scala per tutto il sito
SPAZI = {
    'sezione': (104, 80, 64),   # padding verticale delle sezioni
    'lato':    (40, 32, 20),    # padding laterale delle sezioni
    'xl':      (64, 48, 40),
    'l':       (48, 36, 28),
    'm':       (32, 24, 20),
    's':       (16, 16, 12),
    'xs':      (8, 8, 8),
    '0':       (0, 0, 0),
}


# Ruoli di colore (i nomi storici NERO/BIANCO/ROSSO restano come alias dei ruoli)
FONDO = BIANCO
TEMA_ATTIVO = 'base'


def applica_tema(t):
    """Sostituisce palette, font, scala tipografica e spaziature con quelli di un tema (dizionario)."""
    g = globals()
    mappa = {'inchiostro': 'NERO', 'superficie': 'BIANCO', 'accento': 'ROSSO', 'testo2': 'NERO_75', 'su_scuro2': 'BIANCO_70',
             'filetto': 'LINEA', 'filetto_scuro': 'LINEA_SCURA', 'fondo': 'FONDO'}
    for k, nome in mappa.items():
        if k in t:
            g[nome] = t[k]
    for k in ('SCURO', 'SU_SCURO', 'SU_ACCENTO', 'FONT_TITOLI', 'FONT_TESTO', 'GOOGLE_FONTS', 'LARGHEZZA'):
        if k.lower() in t:
            g[k] = t[k.lower()]
    if 'stili' in t:
        g['STILI'] = t['stili']
    if 'spazi' in t:
        g['SPAZI'] = t['spazi']
    if 'bottoni' in t:
        g['BOTTONI'] = t['bottoni']
    if 'bottone' in t:
        g['BOTTONE_FORMA'] = t['bottone']
    g['TEMA_ATTIVO'] = t.get('nome', 'tema')


SCURO = NERO
SU_SCURO = BIANCO
SU_ACCENTO = BIANCO
BOTTONE_FORMA = {'raggio': 0, 'pad': (18, 28, 18, 28), 'bordo': 2, 'stile': 'btn'}


def rv(v):
    """Valore responsive: accetta uno scalare, una tupla (d, t, m) o il nome di una spaziatura."""
    if isinstance(v, str) and v in SPAZI:
        return SPAZI[v]
    if isinstance(v, (tuple, list)):
        if len(v) == 2:
            v = (v[0], v[1], v[1])
        # ogni voce può essere un numero o il nome di una spaziatura, preso al breakpoint corrispondente
        return tuple(SPAZI[x][i] if isinstance(x, str) and x in SPAZI else x for i, x in enumerate(v))
    return (v, v, v)


def _rgba(hex_, a):
    h = hex_.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f'rgba({r},{g},{b},{a})'


def pad4(v):
    """Padding: scalare/nome (tutti i lati), (vert, oriz) o (top, right, bottom, left); ogni voce può essere responsive."""
    if not isinstance(v, (tuple, list)) or len(v) == 3 and all(not isinstance(x, (tuple, list, str)) for x in v):
        x = rv(v)
        return [x, x, x, x]
    if len(v) == 2:
        a, b = rv(v[0]), rv(v[1])
        return [a, b, a, b]
    return [rv(x) for x in v]


# ---------------------------------------------------------------------------------------------
# Nodi
# ---------------------------------------------------------------------------------------------
class N:
    def __init__(self, kind, children=None, **p):
        self.kind = kind
        self.children = list(children or [])
        self.p = p
        self.id = None


def C(*children, **p):
    """Contenitore flexbox. Opzioni principali:
    dir/dir_t/dir_m, gap, pad, bg, img (src), overlay (opacità 0-1), boxed (bool), w (% responsive),
    align, justify, wrap, min_h, tag, link, anchor, border_top, border_bottom, border (colore), grow."""
    return N('container', children, **p)


def H(text, level='h2', style=None, color=NERO, align='left', link=None, **p):
    return N('heading', text=text, level=level, style=style or level, color=color, align=align, link=link, **p)


def T(html, style='body', color=NERO, align='left', link_color=None, **p):
    return N('text', html=html, style=style, color=color, align=align, link_color=link_color or color, **p)


def B(text, url, variant='primario', align='left', **p):
    return N('button', text=text, url=url, variant=variant, align=align, **p)


def I(src, alt='', height=None, fit='cover', pos='center center', **p):
    return N('image', src=src, alt=alt, height=height, fit=fit, pos=pos, **p)


def MAPPA(address, height=420, zoom=15, **p):
    return N('map', address=address, height=height, zoom=zoom, **p)


def LINEA_H(color=None, weight=1, stile='solid', larghezza=None, **p):
    """Divisore: stile solid, double, dashed, dotted; larghezza in px (responsive) o piena."""
    return N('divider', color=color or LINEA, weight=weight, stile=stile, larghezza=larghezza, **p)


def ARTICOLI(statici, numero=5, **p):
    """Ultimi articoli del blog WordPress: in Elementor è il widget gratuito "Articoli recenti" (dinamico),
    nel fallback HTML un elenco statico con gli stessi esempi."""
    return N('posts', statici=statici, numero=numero, **p)


def MENU(voci, slug='menu-principale', **p):
    """Menu di navigazione. In Elementor è il widget "Navigation Menu" del plugin gratuito Ultimate Addons for Elementor
    (header-footer-elementor), che legge il menu WordPress con questo slug e su tablet e mobile diventa un menu a scomparsa.
    Nel fallback HTML: link in riga su desktop, <details> apribile su tablet e mobile (nessun JavaScript)."""
    return N('navmenu', voci=voci, slug=slug, **p)


def SHORTCODE(codice, alternativa_html='', **p):
    """Widget Shortcode (gratuito). Nel fallback HTML gli shortcode non funzionano: si scrive alternativa_html."""
    return N('shortcode', codice=codice, alternativa_html=alternativa_html, **p)


def RAW(html, css='', solo_elementor=False, **p):
    """HTML grezzo: usato solo dove la versione gratuita non ha un widget adatto.
    solo_elementor=True: serve solo nel template Elementor (per esempio lo stile del widget Articoli recenti),
    nel fallback HTML non viene scritto."""
    return N('html', html=html, css=css, solo_elementor=solo_elementor, **p)


# ---------------------------------------------------------------------------------------------
# ID deterministici (Elementor li rigenera comunque quando inserisci il template in una pagina)
# ---------------------------------------------------------------------------------------------
def assegna_id(node, seed, path='0'):
    node.id = hashlib.md5(f'{seed}/{path}'.encode()).hexdigest()[:7]
    for i, c in enumerate(node.children):
        assegna_id(c, seed, f'{path}.{i}')


# ---------------------------------------------------------------------------------------------
# A) Emettitore Elementor
# ---------------------------------------------------------------------------------------------
SUFFISSI = ('', '_tablet', '_mobile')


def _slider(unit, size):
    return {'unit': unit, 'size': size, 'sizes': []}


def _dims(t, r, b, l, unit='px'):
    linked = t == r == b == l
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l), 'isLinked': linked}


def _resp(settings, key, values, make):
    """Scrive key, key_tablet, key_mobile, saltando i breakpoint che ripetono il valore precedente."""
    prev = object()
    for suf, v in zip(SUFFISSI, values):
        if v is None:
            continue
        if v != prev:
            settings[key + suf] = make(v)
        prev = v


def _tipografia(settings, stile, prefix='typography'):
    st = STILI[stile]
    settings[f'{prefix}_typography'] = 'custom'
    settings[f'{prefix}_font_family'] = st['f']
    _resp(settings, f'{prefix}_font_size', st['s'], lambda v: _slider('px', v))
    settings[f'{prefix}_font_weight'] = st['w']
    settings[f'{prefix}_line_height'] = _slider('em', st['lh'])
    settings[f'{prefix}_letter_spacing'] = _slider('px', st['ls'])
    settings[f'{prefix}_text_transform'] = 'uppercase' if st['up'] else 'none'


# Dominio del sito: se impostato (build.py --url-sito) i link interni diventano assoluti
SITO = ''


def url_finale(url):
    return SITO.rstrip('/') + url if SITO and url.startswith('/') else url


def _link(url):
    url = url_finale(url)
    ext = 'on' if url.startswith('http') and 'benvegnusrl.it' not in url and (not SITO or not url.startswith(SITO)) else ''
    return {'url': url, 'is_external': ext, 'nofollow': '', 'custom_attributes': ''}


# ID numerico finto ma stabile per ogni immagine: Elementor lo usa per riconoscere la stessa immagine
# nello stesso import (anche da ZIP) e così non la scarica due volte. Deve essere unico per URL.
_ID_IMMAGINI = {}


def id_immagine(src):
    nome = src.rsplit('/', 1)[-1]
    n = 9001 + int(hashlib.md5(nome.encode()).hexdigest(), 16) % 80000
    altro = _ID_IMMAGINI.get(n)
    if altro and altro != nome:
        raise ValueError(f'collisione di id immagine: {nome} e {altro}')
    _ID_IMMAGINI[n] = nome
    return n


def _img(src, alt=''):
    return {'url': src, 'id': id_immagine(src), 'size': '', 'alt': alt, 'source': 'library'}


# Bottoni: (testo, sfondo, bordo, testo hover, sfondo hover, bordo hover).
# In hover il bottone si inverte e resta sempre visibile sul fondo della sezione: mai dissolvenza.
BOTTONI = {
    'primario':         (BIANCO, ROSSO, ROSSO, BIANCO, NERO, NERO),          # su bianco
    'contorno':         (NERO, BIANCO, NERO, BIANCO, NERO, NERO),            # su bianco
    'primario-su-nero': (BIANCO, ROSSO, ROSSO, NERO, BIANCO, BIANCO),        # su nero
    'contorno-bianco':  (BIANCO, NERO, BIANCO, NERO, BIANCO, BIANCO),        # su nero
    'bianco':           (NERO, BIANCO, BIANCO, BIANCO, NERO, NERO),          # su rosso
    'contorno-su-rosso': (BIANCO, ROSSO, BIANCO, ROSSO, BIANCO, BIANCO),     # su rosso
}


ALLINEA_FLEX = {'start': 'flex-start', 'center': 'center', 'end': 'flex-end', 'stretch': 'stretch',
                'between': 'space-between', 'baseline': 'baseline'}


def el_settings(n, inner):
    p = n.p
    s = {}
    if n.kind == 'container':
        boxed = p.get('boxed', not inner)
        s['content_width'] = 'boxed' if boxed else 'full'
        if boxed:
            s['boxed_width'] = _slider('px', p.get('boxed_width', LARGHEZZA))
        if 'w' in p:
            # Elementor non eredita la larghezza mobile da quella tablet (container.php, "not inherited"):
            # la scrivo sempre su tutti e tre i breakpoint
            for suf, v in zip(SUFFISSI, rv(p['w'])):
                s['width' + suf] = _slider('%', v)
        if p.get('larg_px'):
            # larghezza fissa in px (schede di una striscia scorrevole): non si allarga e non si restringe
            for suf, v in zip(SUFFISSI, rv(p['larg_px'])):
                s['width' + suf] = _slider('px', v)
            s['_flex_size'] = 'none'
        if p.get('z') is not None:
            s['z_index'] = p['z']
        if p.get('grow'):
            # "grow" di Elementor imposta anche flex-shrink 0 e schiaccia i vicini: uso cresci + restringi
            s['_flex_size'] = 'custom'
            s['_flex_grow'] = 1
            s['_flex_shrink'] = 1
        elif p.get('fisso'):
            s['_flex_size'] = 'none'   # tiene la larghezza impostata, non si restringe per far posto ai vicini
        s['flex_direction'] = p.get('dir', 'column')
        if p.get('dir_t'):
            s['flex_direction_tablet'] = p['dir_t']
        if p.get('dir_m'):
            s['flex_direction_mobile'] = p['dir_m']
        # a capo esplicito su tutti i breakpoint: Elementor su mobile manda a capo per default, il fallback HTML no
        for suf, v in zip(SUFFISSI, rv(p.get('wrap', False))):
            s['flex_wrap' + suf] = 'wrap' if v else 'nowrap'
        if p.get('justify'):
            _resp(s, 'flex_justify_content', rv(p['justify']), lambda v: ALLINEA_FLEX[v])
        if p.get('align'):
            _resp(s, 'flex_align_items', rv(p['align']), lambda v: ALLINEA_FLEX[v])
        gap = rv(p.get('gap', '0'))
        if p.get('gap_r') is not None:
            # spaziatura diversa tra righe (a capo) e colonne
            gr = rv(p['gap_r'])
            for i, suf in enumerate(SUFFISSI):
                s['flex_gap' + suf] = {'column': str(gap[i]), 'row': str(gr[i]), 'isLinked': False, 'unit': 'px', 'size': gap[i]}
        else:
            _resp(s, 'flex_gap', gap, lambda v: {'column': str(v), 'row': str(v), 'isLinked': True, 'unit': 'px', 'size': v})
        pad = pad4(p.get('pad', '0'))
        for i, suf in enumerate(SUFFISSI):
            s['padding' + suf] = _dims(pad[0][i], pad[1][i], pad[2][i], pad[3][i])
        if p.get('min_h'):
            mh = rv(p['min_h'])
            _resp(s, 'min_height', mh, lambda v: _slider('px', v))
        if p.get('bg') or p.get('img'):
            s['background_background'] = 'classic'
            if p.get('bg'):
                s['background_color'] = p['bg']
            if p.get('img'):
                s['background_image'] = _img(p['img'], p.get('alt', ''))
                s['background_position'] = p.get('img_pos', 'center center')
                s['background_size'] = 'cover'
                s['background_repeat'] = 'no-repeat'
        if p.get('bg_hover'):
            s['background_hover_background'] = 'classic'
            s['background_hover_color'] = p['bg_hover']
            s['background_hover_transition'] = _slider('px', 0.15)
        if p.get('scrim'):
            # velatura sfumata: trasparente in alto, scura in basso, dove sta il testo
            da, a_alto, a_basso = p['scrim']
            s['background_overlay_background'] = 'gradient'
            s['background_overlay_color'] = _rgba(p.get('overlay_color', NERO), a_alto)
            s['background_overlay_color_stop'] = _slider('%', da)
            s['background_overlay_color_b'] = _rgba(p.get('overlay_color', NERO), a_basso)
            s['background_overlay_color_b_stop'] = _slider('%', 100)
            s['background_overlay_gradient_type'] = 'linear'
            s['background_overlay_gradient_angle'] = {'unit': 'deg', 'size': 180, 'sizes': []}
            s['background_overlay_opacity'] = _slider('px', 1)
        elif p.get('overlay') is not None:
            s['background_overlay_background'] = 'classic'
            s['background_overlay_color'] = p.get('overlay_color', NERO)
            s['background_overlay_opacity'] = _slider('px', p['overlay'])
        borders = {k: p.get(k) for k in ('border_top', 'border_bottom', 'border_left', 'border_right')}
        if p.get('border') or any(borders.values()):
            col = p.get('border_color', LINEA)
            if p.get('border'):
                t = r = b = l = p['border']
            else:
                t, r, b, l = (borders['border_top'] or 0, borders['border_right'] or 0,
                              borders['border_bottom'] or 0, borders['border_left'] or 0)
            s['border_border'] = 'solid'
            s['border_width'] = _dims(t, r, b, l)
            s['border_color'] = col
        if p.get('tag'):
            s['html_tag'] = p['tag']
        if p.get('link'):
            s['html_tag'] = 'a'
            s['link'] = _link(p['link'])
        if p.get('anchor'):
            s['_element_id'] = p['anchor']
        if p.get('overflow'):
            s['overflow'] = 'auto' if p['overflow'] == 'auto' else 'hidden'
        if p.get('css'):
            s['css_classes'] = p['css']
        if p.get('hide'):
            for bp in p['hide']:
                s[f'hide_{bp}'] = 'hidden-' + bp
        if p.get('mt') or p.get('mb'):
            mt, mb = rv(p.get('mt', 0)), rv(p.get('mb', 0))
            for i, suf in enumerate(SUFFISSI):
                s['margin' + suf] = _dims(mt[i], 0, mb[i], 0)
        return s

    if n.kind == 'heading':
        s['title'] = p['text']
        s['header_size'] = p['level']
        _resp(s, 'align', rv(p['align']), lambda v: v)
        s['title_color'] = p['color']
        _tipografia(s, p['style'])
        if p.get('link'):
            s['link'] = _link(p['link'])
    elif n.kind == 'text':
        # sottolineatura inline: il widget Testo non ha un controllo per text-decoration e temi come Hello la tolgono
        html = p['html']
        if p.get('sottolinea', True):
            html = html.replace('<a href=', '<a style="text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px" href=')
        else:
            html = html.replace('<a href=', '<a style="text-decoration:none" href=')
        s['editor'] = html
        _resp(s, 'align', rv(p['align']), lambda v: v)
        s['text_color'] = p['color']
        s['link_color'] = p['link_color']
        s['link_hover_color'] = p.get('link_hover', ROSSO if p['link_color'] != ROSSO else NERO)
        s['paragraph_spacing'] = _slider('em', 0.9)
        _tipografia(s, p['style'])
    elif n.kind == 'button':
        s['text'] = p['text']
        s['link'] = _link(p['url'])
        _resp(s, 'align', rv(p['align']), lambda v: v)
        s['size'] = 'md'
        _tipografia(s, BOTTONE_FORMA.get('stile', 'btn'))
        v = p['variant']
        colori = BOTTONI[v]
        s['button_text_color'] = colori[0]
        s['background_background'] = 'classic'
        s['background_color'] = colori[1]
        bf = BOTTONE_FORMA
        s['border_border'] = 'solid'
        s['border_width'] = _dims(bf['bordo'], bf['bordo'], bf['bordo'], bf['bordo'])
        s['border_color'] = colori[2]
        s['hover_color'] = colori[3]
        s['button_background_hover_background'] = 'classic'
        s['button_background_hover_color'] = colori[4]
        s['button_hover_border_color'] = colori[5]
        r = bf['raggio']
        s['border_radius'] = _dims(r, r, r, r)
        s['text_padding'] = _dims(*bf['pad'])
        if p.get('full_m'):
            s['align_mobile'] = 'justify'
    elif n.kind == 'image':
        s['image'] = _img(p['src'], p.get('alt', ''))
        s['image_size'] = 'full'
        if p.get('w_img'):
            _resp(s, 'width', rv(p['w_img']), lambda v: _slider('px', v))
            s['align'] = 'left'
        else:
            s['width'] = _slider('%', 100)
        s['max_width'] = _slider('%', 100)
        if p.get('height'):
            _resp(s, 'height', rv(p['height']), lambda v: _slider('px', v))
            s['object-fit'] = p['fit']
            if p['fit'] == 'cover':
                s['object-position'] = p['pos']
        s['caption_source'] = 'none'
        s['link_to'] = 'custom' if p.get('link') else 'none'
        if p.get('link'):
            s['link'] = _link(p['link'])
            if p.get('link_label'):
                s['link']['custom_attributes'] = 'aria-label|' + p['link_label']
    elif n.kind == 'map':
        s['address'] = p['address']
        s['zoom'] = _slider('px', p['zoom'])
        _resp(s, 'height', rv(p['height']), lambda v: _slider('px', v))
        if p.get('grigia'):
            s['css_filters_css_filter'] = 'custom'
            s['css_filters_saturate'] = _slider('px', 0)
            s['css_filters_contrast'] = _slider('px', 95)
            s['css_filters_brightness'] = _slider('px', 102)
    elif n.kind == 'divider':
        s['style'] = p['stile']
        s['weight'] = _slider('px', p['weight'])
        s['color'] = p['color']
        if p.get('larghezza'):
            for suf, v in zip(SUFFISSI, rv(p['larghezza'])):
                s['width' + suf] = _slider('px', v)
            s['align'] = 'left'
        else:
            s['width'] = _slider('%', 100)
        s['gap'] = _slider('px', 2)
    elif n.kind == 'html':
        s['html'] = (f'<style>{p["css"]}</style>' if p.get('css') else '') + p['html']
    elif n.kind == 'posts':
        s['wp'] = {'title': '', 'number': str(p['numero']), 'show_date': 'on'}
    elif n.kind == 'shortcode':
        s['shortcode'] = p['codice']
    elif n.kind == 'navmenu':
        st_nav = p.get('stile', 'nav')
        s.update({
            'menu': p['slug'], 'layout': 'horizontal', 'navmenu_align': p.get('align_menu', 'right'),
            'dropdown': 'tablet', 'resp_align': 'left', 'full_width_dropdown': 'yes',
            'pointer': 'underline', 'animation_line': 'fade',
            'padding_horizontal_menu_item': _slider('px', p.get('pad_h', 0)),
            'padding_vertical_menu_item': _slider('px', p.get('pad_v', 8)),
            'menu_space_between': _slider('px', p.get('spazio', 32)),
            'color_menu_item': p.get('colore', NERO), 'color_menu_item_hover': p.get('colore_hover', NERO),
            'pointer_color_menu_item_hover': p.get('accento', ROSSO),
            'color_menu_item_active': p.get('colore', NERO), 'pointer_color_menu_item_active': p.get('accento', ROSSO),
            'color_dropdown_item': p.get('colore', NERO), 'background_color_dropdown_item': p.get('fondo_menu', BIANCO),
            'color_dropdown_item_hover': p.get('accento', ROSSO), 'background_color_dropdown_item_hover': p.get('fondo_menu', BIANCO),
            'color_dropdown_item_active': p.get('accento', ROSSO), 'background_color_dropdown_item_active': p.get('fondo_menu', BIANCO),
            'padding_horizontal_dropdown_item': _slider('px', 20), 'padding_vertical_dropdown_item': _slider('px', 16),
            'distance_from_menu': _slider('px', p.get('distanza', 18)),
            'toggle_color': p.get('colore', NERO), 'toggle_hover_color': p.get('colore', NERO),
            # icone semplici al posto di quelle predefinite (fa-align-justify e fa-window-close, il quadrato con la X)
            'dropdown_icon': {'value': 'fas fa-bars', 'library': 'fa-solid'},
            'dropdown_close_icon': {'value': 'fas fa-times', 'library': 'fa-solid'},
            'toggle_size': _slider('px', 22), 'toggle_border_width': _slider('px', 0), 'toggle_border_radius': _slider('px', 0),
            'dropdown_border_border': 'solid', 'dropdown_border_width': _dims(1, 0, 1, 0), 'dropdown_border_color': p.get('linea', LINEA),
        })
        _tipografia(s, st_nav, prefix='menu_typography')
        _tipografia(s, p.get('stile_mobile', st_nav), prefix='dropdown_typography')
    # larghezza massima (testi e titoli) e larghezza fissa in px (None = automatica)
    if p.get('max_w') and not p.get('w_px'):
        _resp(s, '_element_custom_width', rv(p['max_w']), lambda v: _slider('px', v))
        s['_element_width'] = 'initial'
    if p.get('w_px'):
        vals = rv(p['w_px'])
        s['_element_width'] = 'initial'
        _resp(s, '_element_custom_width', vals, lambda v: _slider('px', v) if v else _slider('%', 100))
    if p.get('larg'):
        # larghezza in px solo su alcuni breakpoint (None = larghezza automatica del contenuto)
        for suf, v in zip(SUFFISSI, p['larg']):
            s['_element_width' + suf] = 'initial' if v else 'auto'
            if v:
                s['_element_custom_width' + suf] = _slider('px', v)
    if p.get('grow'):
        s['_flex_size'] = 'custom'
        s['_flex_grow'] = 1
        s['_flex_shrink'] = 1
    if p.get('fisso'):
        s['_flex_size'] = 'none'   # larghezza del contenuto, non si restringe
    if p.get('css') and n.kind != 'html':     # per RAW, css è il foglio di stile, non una classe
        s['_css_classes'] = p['css']
    if p.get('z') is not None:
        s['_z_index'] = p['z']
    # spaziature esterne dei widget
    if p.get('mt') or p.get('mb'):
        mt, mb = rv(p.get('mt', 0)), rv(p.get('mb', 0))
        for i, suf in enumerate(SUFFISSI):
            s['_margin' + suf] = _dims(mt[i], 0, mb[i], 0)
    if p.get('hide'):
        for bp in p['hide']:
            s[f'hide_{bp}'] = 'hidden-' + bp
    return s


WIDGET = {'heading': 'heading', 'text': 'text-editor', 'button': 'button', 'image': 'image',
          'map': 'google_maps', 'divider': 'divider', 'html': 'html', 'posts': 'wp-widget-recent-posts',
          'navmenu': 'navigation-menu', 'shortcode': 'shortcode'}


def to_elementor(n, inner=False):
    if n.kind == 'container':
        return {'id': n.id, 'elType': 'container', 'isInner': inner, 'settings': el_settings(n, inner),
                'elements': [to_elementor(c, True) for c in n.children]}
    return {'id': n.id, 'elType': 'widget', 'widgetType': WIDGET[n.kind], 'isInner': False,
            'settings': el_settings(n, inner), 'elements': []}


def template_json(title, sections, kind='page', page_settings=None):
    return {
        'content': [to_elementor(s) for s in sections],
        'page_settings': page_settings if page_settings is not None else [],
        'version': '0.4',
        'title': title,
        'type': kind,
    }


# ---------------------------------------------------------------------------------------------
# B) Emettitore HTML (CSS con prefisso per sezione, resiste agli stili del tema)
# ---------------------------------------------------------------------------------------------
def _px(v):
    return f'{v}px' if v else '0'


def _css_tipo(stile):
    st = STILI[stile]
    base = (f"font-family:'{st['f']}',Arial,sans-serif;font-weight:{st['w']};font-size:{st['s'][0]}px;"
            f"line-height:{st['lh']};letter-spacing:{st['ls']}px;text-transform:{'uppercase' if st['up'] else 'none'};")
    return base, st['s']


class Css:
    def __init__(self):
        self.d, self.t, self.m = [], [], []

    def add(self, sel, d='', t='', m=''):
        if d:
            self.d.append(f'{sel}{{{d}}}')
        if t:
            self.t.append(f'{sel}{{{t}}}')
        if m:
            self.m.append(f'{sel}{{{m}}}')

    def out(self):
        s = ''.join(self.d)
        if self.t:
            s += f'@media (max-width:{BP_TABLET}px){{{"".join(self.t)}}}'
        if self.m:
            s += f'@media (max-width:{BP_MOBILE}px){{{"".join(self.m)}}}'
        return s


def _resp_css(css, sel, prop, values, fmt):
    d, t, m = values
    css.add(sel, f'{prop}:{fmt(d)};', f'{prop}:{fmt(t)};' if t != d else '', f'{prop}:{fmt(m)};' if m != t else '')


def to_html(n, css, scope, inner=False):
    out = _to_html(n, css, scope, inner)
    extra = n.p.get('css') if n.kind != 'html' else None
    if extra and out:
        c = f'b{n.id}'
        for pre in (f'class="bvg-con {c}"', f'class="bvg-w {c}"'):
            if pre in out:
                out = out.replace(pre, pre[:-1] + f' {extra}"', 1)
                break
    return out


def _to_html(n, css, scope, inner=False):
    p = n.p
    c = f'b{n.id}'
    sel = f'.{scope} .{c}'
    if n.kind == 'container':
        boxed = p.get('boxed', not inner)
        tag = 'a' if p.get('link') else p.get('tag', 'div')
        attrs = f' class="bvg-con {c}"'
        if p.get('link'):
            ext = p['link'].startswith('http') and 'benvegnusrl.it' not in p['link']
            attrs += f' href="{_html.escape(url_finale(p["link"]))}"' + (' target="_blank" rel="noopener"' if ext else '')
        if p.get('anchor'):
            attrs += f' id="{p["anchor"]}"'
        d = ['display:flex;position:relative;box-sizing:border-box;']
        pad = pad4(p.get('pad', '0'))
        pv = [f'padding:{_px(pad[0][i])} {_px(pad[1][i])} {_px(pad[2][i])} {_px(pad[3][i])};' for i in range(3)]
        css.add(sel, pv[0], pv[1] if pv[1] != pv[0] else '', pv[2] if pv[2] != pv[1] else '')
        if p.get('larg_px'):
            _resp_css(css, sel, 'width', rv(p['larg_px']), lambda v: f'{v}px')
            d.append('flex-grow:0;flex-shrink:0;')
        elif 'w' in p:
            _resp_css(css, sel, 'width', rv(p['w']), lambda v: f'{v}%')
        else:
            d.append('width:100%;')
        if p.get('z') is not None:
            d.append(f'z-index:{p["z"]};')
        if p.get('grow'):
            d.append('flex-grow:1;')
        if not p.get('larg_px'):
            d.append('flex-shrink:0;' if p.get('fisso') and not p.get('grow') else 'flex-shrink:1;min-width:0;')
        if p.get('min_h'):
            _resp_css(css, sel, 'min-height', rv(p['min_h']), lambda v: f'{v}px')
        bgs = []
        if p.get('bg'):
            d.append(f'background-color:{p["bg"]};')
        if p.get('img'):
            d.append(f'background-image:url("{p["img"]}");background-size:cover;'
                     f'background-position:{p.get("img_pos", "center center")};background-repeat:no-repeat;')
        if p.get('scrim'):
            da, a_alto, a_basso = p['scrim']
            col = p.get('overlay_color', NERO)
            css.add(f'{sel}::before', f'content:"";position:absolute;inset:0;pointer-events:none;'
                                      f'background:linear-gradient(180deg,{_rgba(col, a_alto)} {da}%,{_rgba(col, a_basso)} 100%);')
            css.add(f'{sel} > *', 'position:relative;z-index:1;')
        elif p.get('overlay') is not None:
            css.add(f'{sel}::before', f'content:"";position:absolute;inset:0;background:{p.get("overlay_color", NERO)};'
                                      f'opacity:{p["overlay"]};pointer-events:none;')
            css.add(f'{sel} > *', 'position:relative;z-index:1;')
        if p.get('border'):
            d.append(f'border:{p["border"]}px solid {p.get("border_color", LINEA)};')
        for side in ('top', 'bottom', 'left', 'right'):
            if p.get(f'border_{side}'):
                d.append(f'border-{side}:{p[f"border_{side}"]}px solid {p.get("border_color", LINEA)};')
        if p.get('overflow'):
            d.append('overflow:auto;' if p['overflow'] == 'auto' else 'overflow:hidden;')
        if p.get('bg_hover'):
            d.append('transition:background-color .15s;')
            css.add(f'{sel}:hover', f'background-color:{p["bg_hover"]};')
        if p.get('hover_titolo'):
            css.add(f'{sel}:hover h3,{sel}:hover h2', f'color:{p["hover_titolo"]} !important;')
        if tag == 'a':
            d.append('text-decoration:none;color:inherit;')
        if p.get('mt') or p.get('mb'):
            _resp_css(css, sel, 'margin-top', rv(p.get('mt', 0)), _px)
            _resp_css(css, sel, 'margin-bottom', rv(p.get('mb', 0)), _px)
        if p.get('hide'):
            mq = {'desktop': f'@media (min-width:{BP_TABLET + 1}px)', 'tablet': f'@media (min-width:{BP_MOBILE + 1}px) and (max-width:{BP_TABLET}px)',
                  'mobile': f'@media (max-width:{BP_MOBILE}px)'}
            for bp in p['hide']:
                css.d.append(f'{mq[bp]}{{{sel}{{display:none !important;}}}}')
        # direzione, gap, allineamenti: sul contenitore interno se boxed
        inner_sel = f'{sel} > .bvg-inner' if boxed else sel
        dirs = (p.get('dir', 'column'), p.get('dir_t') or p.get('dir', 'column'),
                p.get('dir_m') or p.get('dir_t') or p.get('dir', 'column'))
        _resp_css(css, inner_sel, 'flex-direction', dirs, lambda v: v)
        _resp_css(css, f'{inner_sel} > .bvg-w', 'width', dirs, lambda v: 'auto' if v == 'row' else '100%')
        if p.get('gap_r') is not None:
            _resp_css(css, inner_sel, 'column-gap', rv(p.get('gap', '0')), lambda v: f'{v}px')
            _resp_css(css, inner_sel, 'row-gap', rv(p['gap_r']), lambda v: f'{v}px')
        else:
            _resp_css(css, inner_sel, 'gap', rv(p.get('gap', '0')), lambda v: f'{v}px')
        _resp_css(css, inner_sel, 'flex-wrap', rv(p.get('wrap', False)), lambda v: 'wrap' if v else 'nowrap')
        if p.get('justify'):
            _resp_css(css, inner_sel, 'justify-content', rv(p['justify']), lambda v: ALLINEA_FLEX[v])
        if p.get('align'):
            _resp_css(css, inner_sel, 'align-items', rv(p['align']), lambda v: ALLINEA_FLEX[v])
        css.add(sel, ''.join(d))
        kids = ''.join(to_html(k, css, scope, True) for k in n.children)
        if boxed:
            css.add(f'{sel} > .bvg-inner', f'display:flex;width:100%;max-width:{p.get("boxed_width", LARGHEZZA)}px;margin:0 auto;')
            kids = f'<div class="bvg-inner">{kids}</div>'
        return f'<{tag}{attrs}>{kids}</{tag}>'

    # selettore rinforzato: deve battere la regola generica ".riga > .bvg-w {width:auto}" dei contenitori in riga
    sel_w = f'{sel}.bvg-w.bvg-w'
    if p.get('max_w') and not p.get('w_px'):
        _resp_css(css, sel_w, 'max-width', rv(p['max_w']), lambda v: f'{v}px')
    if p.get('w_px'):
        vals = rv(p['w_px'])
        _resp_css(css, sel_w, 'width', vals, lambda v: f'{v}px' if v else '100%')
        _resp_css(css, sel_w, 'flex-shrink', vals, lambda v: '0' if v else '1')
    if p.get('grow'):
        css.add(sel, 'flex-grow:1;flex-shrink:1;min-width:0;')
    if p.get('fisso'):
        css.add(sel, 'flex-grow:0;flex-shrink:0;')
    if p.get('mt') or p.get('mb'):
        mt, mb = rv(p.get('mt', 0)), rv(p.get('mb', 0))
        _resp_css(css, sel, 'margin-top', mt, _px)
        _resp_css(css, sel, 'margin-bottom', mb, _px)
    if p.get('z') is not None:
        css.add(sel, f'position:relative;z-index:{p["z"]};')
    if p.get('hide'):
        mq = {'desktop': f'@media (min-width:{BP_TABLET + 1}px)', 'tablet': f'@media (min-width:{BP_MOBILE + 1}px) and (max-width:{BP_TABLET}px)',
              'mobile': f'@media (max-width:{BP_MOBILE}px)'}
        for bp in p['hide']:
            css.d.append(f'{mq[bp]}{{{sel}{{display:none !important;}}}}')

    if n.kind == 'heading':
        base, sizes = _css_tipo(p['style'])
        # margin:0 solo se il titolo non ha mt/mb: altrimenti azzererebbe i margini scritti sopra
        css.add(sel, base + f'color:{p["color"]};' + ('margin-left:0;margin-right:0;' if (p.get('mt') or p.get('mb')) else 'margin:0;')
                + 'padding:0;')
        _resp_css(css, sel, 'font-size', sizes, lambda v: f'{v}px')
        _resp_css(css, sel, 'text-align', rv(p['align']), lambda v: v)
        txt = p['text']
        if p.get('link'):
            css.add(f'{sel} a', 'color:inherit;text-decoration:none;')
            txt = f'<a href="{_html.escape(url_finale(p["link"]))}">{txt}</a>'
        return f'<{p["level"]} class="bvg-w {c}">{txt}</{p["level"]}>'
    if n.kind == 'text':
        base, sizes = _css_tipo(p['style'])
        css.add(sel, base + f'color:{p["color"]};')
        _resp_css(css, sel, 'font-size', sizes, lambda v: f'{v}px')
        _resp_css(css, sel, 'text-align', rv(p['align']), lambda v: v)
        css.add(f'{sel} p', 'margin:0 0 0.9em;')
        css.add(f'{sel} p:last-child', 'margin-bottom:0;')
        if p.get('sottolinea', True):
            css.add(f'{sel} a', f'color:{p["link_color"]};text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px;')
        else:
            css.add(f'{sel} a', f'color:{p["link_color"]};text-decoration:none;')
        css.add(f'{sel} a:hover,{sel} a:focus', f'color:{p.get("link_hover", ROSSO if p["link_color"] != ROSSO else NERO)};')
        # elenchi senza pallini: righe separate da un filetto, come una scheda tecnica
        css.add(f'{sel} ul', 'margin:0;padding:0;list-style:none;')
        css.add(f'{sel} li', f'margin:0;padding:10px 0;border-top:1px solid {LINEA};')
        css.add(f'{sel} li:last-child', f'border-bottom:1px solid {LINEA};')
        return f'<div class="bvg-w {c}">{p["html"]}</div>'
    if n.kind == 'button':
        bf = BOTTONE_FORMA
        base, _ = _css_tipo(bf.get('stile', 'btn'))
        col = BOTTONI[p['variant']]
        al = rv(p['align'])
        css.add(sel, 'display:flex;' + f'justify-content:{ {"left": "flex-start", "center": "center", "right": "flex-end"}.get(al[0], "flex-start")};',
                f'justify-content:{ {"left": "flex-start", "center": "center", "right": "flex-end"}.get(al[1], "flex-start")};' if al[1] != al[0] else '',
                f'justify-content:{ {"left": "flex-start", "center": "center", "right": "flex-end"}.get(al[2], "flex-start")};' if al[2] != al[1] else '')
        pt, pr, pb, pl = bf['pad']
        css.add(f'{sel} a', base + f'display:inline-block;color:{col[0]};background:{col[1]};border:{bf["bordo"]}px solid {col[2]};'
                f'padding:{pt}px {pr}px {pb}px {pl}px;border-radius:{bf["raggio"]}px;text-decoration:none;'
                'transition:background-color .2s,color .2s,border-color .2s;')
        css.add(f'{sel} a:hover,{sel} a:focus-visible', f'color:{col[3]};background:{col[4]};border-color:{col[5]};')
        css.add(f'{sel} a:focus-visible', f'outline:3px solid {BIANCO if p["variant"] in ("bianco", "contorno-bianco") else ROSSO};outline-offset:3px;')
        if p.get('full_m'):
            css.add(f'{sel} a', '', '', 'display:block;width:100%;text-align:center;box-sizing:border-box;')
        ext = p['url'].startswith('http') and 'benvegnusrl.it' not in p['url']
        return (f'<div class="bvg-w {c}"><a href="{_html.escape(url_finale(p["url"]))}"'
                + (' target="_blank" rel="noopener"' if ext else '') + f'>{p["text"]}</a></div>')
    if n.kind == 'image':
        css.add(sel, 'line-height:0;')
        css.add(f'{sel} img', 'display:block;width:100%;max-width:100%;' + (f'object-fit:{p["fit"]};object-position:{p["pos"]};' if p.get('height') else 'height:auto;'))
        if p.get('w_img'):
            _resp_css(css, f'{sel} img', 'width', rv(p['w_img']), lambda v: f'{v}px')
        if p.get('height'):
            _resp_css(css, f'{sel} img', 'height', rv(p['height']), lambda v: f'{v}px')
        img = f'<img src="{_html.escape(p["src"])}" alt="{_html.escape(p.get("alt", ""))}" loading="lazy">'
        if p.get('link'):
            lab = f' aria-label="{_html.escape(p["link_label"])}"' if p.get('link_label') else ''
            img = f'<a href="{_html.escape(url_finale(p["link"]))}"{lab}>{img}</a>'
        return f'<div class="bvg-w {c}">{img}</div>'
    if n.kind == 'map':
        hh = rv(p['height'])
        _resp_css(css, f'{sel} iframe', 'height', hh, lambda v: f'{v}px')
        css.add(f'{sel} iframe', 'display:block;width:100%;border:0;' + ('filter:saturate(0) contrast(.95) brightness(1.02);' if p.get('grigia') else ''))
        q = _html.escape(p['address'])
        return (f'<div class="bvg-w {c}"><iframe loading="lazy" title="Mappa: {q}" '
                f'src="https://maps.google.com/maps?q={q.replace(" ", "+")}&amp;t=m&amp;z={p["zoom"]}&amp;output=embed&amp;iwloc=near"></iframe></div>')
    if n.kind == 'divider':
        st = p['stile']
        css.add(sel, f'padding:2px 0;')
        if st == 'double':
            linea = f'border-top:{max(1, p["weight"] // 3)}px solid {p["color"]};border-bottom:{max(1, p["weight"] // 3)}px solid {p["color"]};height:{p["weight"]}px;'
        else:
            linea = f'border-top:{p["weight"]}px {st} {p["color"]};height:0;'
        css.add(f'{sel} span', 'display:block;' + linea)
        if p.get('larghezza'):
            _resp_css(css, f'{sel} span', 'width', rv(p['larghezza']), lambda v: f'{v}px')
        return f'<div class="bvg-w {c}" role="separator"><span></span></div>'
    if n.kind == 'html':
        if p.get('solo_elementor'):
            return ''
        if p.get('css'):
            css.d.append(p['css'])
        return f'<div class="bvg-w {c}">{p["html"]}</div>'
    if n.kind == 'shortcode':
        if not p['alternativa_html']:
            return ''
        base, sizes = _css_tipo(p.get('stile', 'body'))
        css.add(f'{sel} p', base + f'color:{p.get("colore", NERO)};')
        _resp_css(css, f'{sel} p', 'font-size', sizes, lambda v: f'{v}px')
        css.add(f'{sel} a', f'color:{NERO};text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px;')
        css.add(f'{sel} a:hover,{sel} a:focus', f'color:{ROSSO};')
        return f'<div class="bvg-w {c}">{p["alternativa_html"]}</div>'
    if n.kind == 'navmenu':
        base, sizes = _css_tipo(p.get('stile', 'nav'))
        col, acc, fondo, linea = p.get('colore', NERO), p.get('accento', ROSSO), p.get('fondo_menu', BIANCO), p.get('linea', LINEA)
        voci = ''.join(f'<li><a href="{_html.escape(url_finale(u))}">{t}</a></li>' for t, u in p['voci'])
        css.add(f'{sel}', 'position:relative;')
        css.add(f'{sel} ul', 'list-style:none;margin:0;padding:0;')
        css.add(f'{sel} .bvg-nav-l', f'display:flex;flex-wrap:nowrap;gap:{p.get("spazio", 32)}px;justify-content:flex-end;align-items:center;',
                'display:none;')
        css.add(f'{sel} a', base + f'color:{col};text-decoration:none;display:inline-block;padding:{p.get("pad_v", 8)}px 0;'
                'border-bottom:1px solid transparent;transition:border-color .2s;')
        css.add(f'{sel} .bvg-nav-l a:hover,{sel} .bvg-nav-l a:focus-visible', f'border-bottom-color:{acc};')
        css.add(f'{sel} details', 'display:none;', 'display:block;')
        css.add(f'{sel} summary', f'list-style:none;cursor:pointer;color:{col};display:inline-flex;align-items:center;'
                'justify-content:flex-end;min-width:44px;min-height:44px;padding:0;')
        css.add(f'{sel} summary::-webkit-details-marker', 'display:none;')
        css.add(f'{sel} summary .bvg-ico', f'display:inline-block;width:20px;height:17px;border-top:3px solid {col};border-bottom:3px solid {col};position:relative;')
        css.add(f'{sel} summary .bvg-ico::after', f'content:"";position:absolute;left:0;right:0;top:4px;border-top:3px solid {col};')
        css.add(f'{sel} .bvg-nav-l a[aria-current=page]', f'border-bottom:3px solid {acc};padding-bottom:{max(0, p.get("pad_v", 8) - 2)}px;')
        css.add(f'{sel} details li a[aria-current=page]', f'color:{acc};')
        css.add(f'{sel} details ul', f'position:absolute;left:0;right:0;top:100%;z-index:50;background:{fondo};border-top:1px solid {linea};'
                f'border-bottom:1px solid {linea};margin-top:{p.get("distanza", 18)}px;')
        css.add(f'{sel} details li a', 'display:block;padding:16px 20px;')
        css.add(f'{sel} details li a:hover', f'color:{acc};')
        return (f'<nav class="bvg-w {c}" aria-label="Menu principale"><ul class="bvg-nav-l">{voci}</ul>'
                f'<details><summary aria-label="Menu"><span class="bvg-ico" aria-hidden="true"></span></summary><ul>{voci}</ul></details>'
                # voce della pagina corrente: il fallback è incollato pagina per pagina, la riconosce dall'indirizzo
                f"<script>document.querySelectorAll('.{scope} .{c} a').forEach(function(a){{if(a.pathname===location.pathname)"
                "a.setAttribute('aria-current','page')})</script></nav>")
    if n.kind == 'posts':
        base, sizes = _css_tipo('h3')
        css.add(f'{sel} ul', 'list-style:none;margin:0;padding:0;')
        css.add(f'{sel} li', f'border-top:1px solid {LINEA};padding:20px 0;')
        css.add(f'{sel} a', base + f'color:{NERO};text-decoration:none;')
        css.add(f'{sel} a:hover', f'color:{ROSSO};')
        b2, _ = _css_tipo('small')
        css.add(f'{sel} .bvg-data', b2 + f'display:block;color:{NERO_75};margin-top:6px;')
        voci = ''.join(f'<li><a href="{_html.escape(u)}">{t}</a><span class="bvg-data">{d}</span></li>' for t, u, d in p['statici'])
        return f'<div class="bvg-w {c}"><ul>{voci}</ul></div>'
    raise ValueError(n.kind)


def _reset():
    return (
    "{s}{{margin:0;padding:0;box-sizing:border-box;font-family:'" + FONT_TESTO + "',Arial,sans-serif;color:" + NERO + ";"
    "-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;}}"
    "{s} *,{s} *::before,{s} *::after{{box-sizing:border-box;}}"
    "{s} img{{border:0;border-radius:0;box-shadow:none;}}"
    "{s} a{{transition:none;}}"
    "{s} h1,{s} h2,{s} h3,{s} h4,{s} p{{margin-top:0;}}"
    "{s} .bvg-w{{width:100%;max-width:100%;}}"
    "{s} h1,{s} h2,{s} h3{{text-wrap:balance;}}{s} p{{text-wrap:pretty;}}"
    "{s} .screen-reader-text{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(1px,1px,1px,1px);white-space:nowrap;}}"
    )


def sezione_html(section, scope, fonts=True):
    """Una sezione come blocco autosufficiente: <link> ai font + <style> con prefisso + markup."""
    css = Css()
    body = to_html(section, css, scope)
    style = _reset().format(s='.' + scope) + css.out()
    head = f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="{GOOGLE_FONTS}">' if fonts else ''
    return f'{head}<style>{style}</style><div class="{scope}">{body}</div>'


def pagina_html(title, blocks, description=''):
    return ('<!doctype html><html lang="it"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{_html.escape(title)}</title>'
            + (f'<meta name="description" content="{_html.escape(description)}">' if description else '') +
            f'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="{GOOGLE_FONTS}">'
            f'<style>html,body{{margin:0;padding:0;background:{FONDO};}}</style></head><body>'
            + ''.join(blocks) + '</body></html>')


def json_dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=1)
