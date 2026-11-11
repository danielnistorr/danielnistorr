#!/usr/bin/env python3
"""Genera mvr-care-template.json: modello di Elementor (formato di esportazione, versione 0.4)
per la pagina MVR CARE, compatibile con Elementor 3.31.5 gratuito.

Solo contenitori e widget nativi del gratuito: Titolo (heading), Editor di testo (text-editor),
Immagine (image), Pulsante (button), Elenco icone (icon-list). Colori e caratteri sono legati al kit
del sito con __globals__ (id letti da /wp-content/uploads/elementor/css/post-11.css di evap.it).

Uso: python3 genera_template.py  (scrive mvr-care-template.json nella stessa cartella)
"""
import hashlib
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
import sys  # noqa: E402
sys.path.insert(0, QUI)
import grafici  # noqa: E402  disegni SVG (anno di assistenza, ciclo del servizio, schema MVR facoltativo)
UPL = 'https://evap.it/wp-content/uploads/'

# ---------------------------------------------------------------- utilità
_n = [0]


def uid():
    _n[0] += 1
    return hashlib.sha1(f'mvr-care-{_n[0]}'.encode()).hexdigest()[:7]


def col(i):
    return f'globals/colors?id={i}'


def typ(i):
    return f'globals/typography?id={i}'


def px(v, unit='px'):
    return {'unit': unit, 'size': v, 'sizes': []}


def box(t, r=None, b=None, l=None, unit='px'):
    r = t if r is None else r
    b = t if b is None else b
    l = r if l is None else l
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l),
            'isLinked': len({t, r, b, l}) == 1}


def gap(c, r=None):
    r = c if r is None else r
    return {'unit': 'px', 'column': str(c), 'row': str(r), 'isLinked': c == r, 'size': c}


def con(settings, children, inner=True):
    s = {'padding': box(0)}  # Elementor mette 10 px di margine interno a ogni contenitore: qui si parte da zero
    if inner:
        s['content_width'] = 'full'  # contenitori interni a tutta larghezza: solo cosi la "Larghezza" in % vale
    s.update(settings)
    return {'id': uid(), 'elType': 'container', 'isInner': inner, 'settings': s, 'elements': children}


def wid(kind, settings):
    return {'id': uid(), 'elType': 'widget', 'widgetType': kind, 'isInner': False,
            'settings': settings, 'elements': []}


def html(code, extra=None):
    """Widget HTML nativo (gratuito) con un disegno SVG in linea."""
    s = {'html': code}
    if extra:
        s.update(extra)
    return wid('html', s)


def merge_globals(s, g):
    """Aggiunge riferimenti globali alle impostazioni (accetta impostazioni o un elemento intero)."""
    target = s['settings'] if 'elType' in s else s
    target.setdefault('__globals__', {}).update(g)
    return s


def heading(text, tag='h2', typo=None, color='primary', custom=None, link=None, extra=None):
    s = {'title': text, 'header_size': tag}
    if custom:
        s.update(custom)
    g = {}
    if typo:
        g['typography_typography'] = typ(typo)
    if color:
        g['title_color'] = col(color)
    if link:
        s['link'] = {'url': link, 'is_external': '', 'nofollow': '', 'custom_attributes': ''}
    if extra:
        s.update(extra)
    return wid('heading', merge_globals(s, g))


def h2(text, color='primary'):
    """Titolo di sezione: stesse misure del titolo H2 del kit (38/35/30 px, 600) ma senza
    maiuscole iniziali su ogni parola, come i titoli della home."""
    custom = {
        'typography_typography': 'custom', 'typography_font_family': 'Plus Jakarta Sans',
        'typography_font_size': px(38), 'typography_font_size_tablet': px(35), 'typography_font_size_mobile': px(30),
        'typography_font_weight': '600', 'typography_text_transform': 'none', 'typography_text_decoration': 'none',
        'typography_line_height': px(1.2, 'em'), 'typography_letter_spacing': px(0),
    }
    return heading(text, 'h2', None, color, custom)


def text(html, typo='text', color='text', extra=None):
    s = {'editor': html, 'paragraph_spacing': px(0)}  # niente margine sotto i paragrafi: gli spazi li danno i contenitori
    if extra:
        s.update(extra)
    g = {'typography_typography': typ(typo)}
    if color:
        g['text_color'] = col(color)
    return wid('text-editor', merge_globals(s, g))


def button(label, url, on_dark=False, align=None):
    """Bottone del sito: azzurro, testo bianco, 15/30 px, spigoli vivi.
    Al passaggio si inverte subito (durata della transizione 0): blu su fondo chiaro, bianco sulla foto."""
    s = {
        'text': label,
        'link': {'url': url, 'is_external': '', 'nofollow': '', 'custom_attributes': ''},
        'background_background': 'classic',
        'button_background_hover_background': 'classic',
        'border_radius': box(0),
        'text_padding': box(15, 30, 15, 30),
        'button_hover_transition_duration': {'unit': 's', 'size': 0, 'sizes': []},
    }
    if align:
        s['align'] = align
    g = {
        'typography_typography': typ('264998f'),
        'background_color': col('secondary'),
        'button_text_color': col('accent'),
        'button_background_hover_color': col('accent' if on_dark else 'primary'),
        'hover_color': col('primary' if on_dark else 'accent'),
    }
    return wid('button', merge_globals(s, g))


def link_button(label, url):
    """Collegamento secondario sulla foto: testo bianco sottolineato da un filetto."""
    s = {
        'text': label,
        'link': {'url': url, 'is_external': '', 'nofollow': '', 'custom_attributes': ''},
        'background_background': 'classic', 'background_color': 'rgba(0,0,0,0)',
        'button_background_hover_background': 'classic', 'button_background_hover_color': 'rgba(0,0,0,0)',
        'border_border': 'solid', 'border_width': box(0, 0, 1, 0), 'border_radius': box(0),
        'text_padding': box(15, 0, 4, 0),
        'button_hover_transition_duration': {'unit': 's', 'size': 0, 'sizes': []},
    }
    g = {
        'typography_typography': typ('264998f'),
        'button_text_color': col('accent'), 'border_color': col('accent'),
        'hover_color': col('secondary'), 'button_hover_border_color': col('secondary'),
    }
    return wid('button', merge_globals(s, g))


def boxed(settings, children):
    """Contenitore esterno largo come le pagine di servizio: 1290 px di contenuto."""
    s = {'content_width': 'boxed', 'boxed_width': px(1290),
         'padding': box(0, 10), 'padding_tablet': box(0, 20), 'padding_mobile': box(0, 20)}
    s.update(settings)
    return con(s, children, inner=False)


ROW = {'flex_direction': 'row', 'flex_direction_mobile': 'column'}

# ---------------------------------------------------------------- 1. apertura
hero = con({
    'content_width': 'boxed', 'boxed_width': px(1290), 'html_tag': 'section',
    'flex_direction': 'column', 'flex_gap': gap(0),
    'padding': box(210, 10, 60, 10), 'padding_tablet': box(190, 20, 50, 20), 'padding_mobile': box(140, 10, 40, 10),
    'background_background': 'classic',
    'background_image': {'url': UPL + '2025/10/IMG_9042-1536x1152.jpg', 'id': '', 'size': '', 'alt': '', 'source': 'library'},
    'background_image_mobile': {'url': UPL + '2025/10/IMG_9042-1024x768.jpg', 'id': '', 'size': '', 'alt': '', 'source': 'library'},
    'background_position': 'center center', 'background_position_mobile': 'center center',
    'background_repeat': 'no-repeat', 'background_size': 'cover',
    'background_overlay_background': 'classic', 'background_overlay_opacity': px(0.6),
    'border_border': 'solid', 'border_width': box(20), 'border_width_mobile': box(10),
    '__globals__': {'background_color': col('primary'), 'background_overlay_color': col('primary'),
                    'border_color': col('accent')},
}, [
    heading('MVR CARE', 'h1', 'primary', 'accent',
            extra={'_margin': box(0, 0, 28, 0), '_margin_mobile': box(0, 0, 20, 0)}),
    text('<p>Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.</p>',
         'eac7479', 'accent', extra={'_element_width': 'initial', '_element_custom_width': px(780),
                                      '_element_custom_width_tablet': px(100, '%'), '_element_width_mobile': 'inherit'}),
    con({'flex_direction': 'row', 'flex_wrap': 'wrap', 'flex_align_items': 'center',
         'flex_gap': gap(40, 20), 'flex_gap_mobile': gap(28, 16),
         'margin': box(40, 0, 0, 0), 'margin_mobile': box(32, 0, 0, 0)}, [
        button('Richiedi il canone', 'https://evap.it/contattaci/', on_dark=True),
        link_button('Le due formule', '#formule'),
    ]),
    con({'flex_direction': 'row', 'flex_direction_mobile': 'column', 'flex_gap': gap(40), 'flex_gap_mobile': gap(0),
         'margin': box(120, 0, 0, 0), 'margin_mobile': box(60, 0, 0, 0)}, [
        con({'width': px(33.333, '%'), 'width_mobile': px(100, '%'),
             'border_border': 'solid', 'border_width': box(1, 0, 0, 0),
             'padding': box(22, 0, 0, 0), 'padding_mobile': box(16, 0, 16, 0),
             '__globals__': {'border_color': col('50cd0e7')}}, [
            heading(t, 'p', 'c959aeb', 'accent')])
        for t in ('Continuità di produzione', 'Prestazioni costanti', 'Efficienza e sostenibilità')
    ]),
], inner=False)

# ---------------------------------------------------------------- 2. perché conta
why = boxed({**ROW, 'html_tag': 'section', 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(40),
             'flex_align_items': 'flex-start',
             'margin': box(100, 0, 100, 0), 'margin_mobile': box(60, 0, 60, 0)}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%')}, [
        wid('image', {
            'image': {'url': UPL + '2025/10/IMG_7517-768x1024.jpg', 'id': '', 'size': '',
                      'alt': 'Evaporatore EVAP con il quadro di controllo, in officina', 'source': 'library'},
            'image_size': 'full', 'width': px(100, '%'),
            'height': px(580), 'height_tablet': px(520), 'height_mobile': px(380),
            'object-fit': 'cover', 'object-position': 'center center',
        }),
    ]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(16),
         'padding': box(10, 0, 0, 0), 'padding_mobile': box(0)}, [
        merge_globals(h2('Un evaporatore efficiente è il cuore della tua produttività'), {}),
        text('<p>L\'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione '
             'degli effluenti industriali.</p>', '58b3754', 'primary', extra={'_margin': box(14, 0, 0, 0)}),
        text('<p>Per garantirne nel tempo la massima efficienza e la continuità operativa, EVAP ha sviluppato '
             'MVR CARE: il servizio di assistenza tecnica dedicato ai suoi clienti.</p>'),
        merge_globals(wid('icon-list', {
            'icon_list': [{'_id': uid(), 'text': t, 'selected_icon': {'value': 'fas fa-square', 'library': 'fa-solid'}}
                          for t in ('Evita i fermi impianto imprevisti', 'Mantiene le performance progettuali',
                                    'Riduce i costi operativi nel tempo')],
            'space_between': px(44), 'space_between_mobile': px(36),
            'divider': 'yes', 'divider_style': 'solid', 'divider_weight': px(1),
            'icon_size': px(10), 'text_indent': px(18), 'icon_self_vertical_align': 'center',
            '_border_border': 'solid', '_border_width': box(1, 0, 1, 0),
            '_padding': box(22, 0, 22, 0), '_padding_mobile': box(18, 0, 18, 0),
            '_margin': box(24, 0, 0, 0),
        }), {'icon_color': col('secondary'), 'text_color': col('primary'),
             'icon_typography_typography': typ('c959aeb'),
             'divider_color': col('0012040'), '_border_color': col('0012040')}),
    ]),
])

# ---------------------------------------------------------------- 3. cosa facciamo
# le quattro attività sono disegnate come un ciclo (testi in grafici.CICLO, dalla brochure)
do = con({
    'content_width': 'boxed', 'boxed_width': px(1290), 'html_tag': 'section', **ROW,
    'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(40),
    'padding': box(100, 10), 'padding_tablet': box(100, 20), 'padding_mobile': box(60, 10),
    'background_background': 'classic',
    'border_border': 'solid', 'border_width': box(20), 'border_width_mobile': box(10),
    '__globals__': {'background_color': col('primary'), 'border_color': col('accent')},
}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%')}, [
        h2('Controllo, prevenzione, performance: sempre sotto controllo', 'accent'),
    ]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_justify_content': 'center'}, [
        html(grafici.ciclo()),
    ]),
], inner=False)

# ---------------------------------------------------------------- 4. le due formule
def cell(kind, children, head=False):
    s = {'flex_direction': 'column', 'flex_justify_content': 'center', 'flex_gap': gap(0)}
    if kind == 'label':
        s.update({'width': px(34, '%'), 'width_mobile': px(100, '%'),
                  'padding': box(24, 30, 24, 0), 'padding_tablet': box(20, 20, 20, 0), 'padding_mobile': box(18, 0, 8, 0)})
        if head:
            s['hide_mobile'] = 'hidden-mobile'
    else:
        s.update({'width': px(33, '%'), 'width_mobile': px(50, '%'),
                  'padding': box(30 if head else 24, 30, 26 if head else 24, 30),
                  'padding_tablet': box(20), 'padding_mobile': box(18 if head else 12, 14, 16, 14),
                  'flex_justify_content_mobile': 'flex-start'})
        if kind == 'plus':
            s['background_background'] = 'classic'
            s['__globals__'] = {'background_color': col('9f5d5c9')}
    return con(s, children)


def row(label, pure, plus, head=False):
    s = {'flex_direction': 'row', 'flex_wrap': 'wrap', 'flex_gap': gap(0),
         'border_border': 'solid', 'border_width': box(0, 0, 3 if head else 1, 0),
         '__globals__': {'border_color': col('secondary' if head else '0012040')}}
    lab = [heading(label, 'p', 'd438253', 'primary')] if label else []
    return con(s, [cell('label', lab, head), cell('pure', pure, head), cell('plus', plus, head)])


def value(t, strong=False):
    # Titolo con tag <p>: niente margine sotto il paragrafo, cosi il valore resta centrato nella cella
    if strong:
        return heading(t, 'p', 'd438253', 'primary')
    return heading(t, 'p', 'text', 'text')


plans = boxed({'html_tag': 'section', '_element_id': 'formule', 'flex_gap': gap(0),
               'margin': box(100, 0, 100, 0), 'margin_mobile': box(60, 0, 60, 0)}, [
    con({'width': px(900, 'px'), 'width_tablet': px(100, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(16)}, [
        h2('Scegli il livello di servizio più adatto alle tue esigenze'),
        text("<p>Due formule flessibili, con la qualità e l'esperienza EVAP.</p>", '58b3754', 'text'),
    ]),
    html(grafici.anno(), extra={'_margin': box(50, 0, 0, 0), '_margin_mobile': box(36, 0, 0, 0)}),
    con({'margin': box(70, 0, 0, 0), 'margin_mobile': box(48, 0, 0, 0), 'flex_gap': gap(0)}, [
        row('', [heading('MVR CARE PURE', 'h3', 'ffbed2e', 'primary')],
            [heading('MVR CARE PLUS', 'h3', 'ffbed2e', 'primary')], head=True),
        row('Verifica dello stato di esercizio e della manutenzione', [value('Compresa')], [value('Compresa')]),
        row('Anomalie', [value('Segnalazione delle anomalie e azioni raccomandate')],
            [value('Analisi delle anomalie e delle perdite di produttività')]),
        row('Rapporto', [value('Rapporto sintetico di verifica')], [value('Rapporto tecnico mensile')]),
    ]),
])

# ---------------------------------------------------------------- 5. richiesta del canone
fee = boxed({'html_tag': 'section', '_element_id': 'canone', 'flex_gap': gap(0),
             'margin': box(0, 0, 100, 0), 'margin_mobile': box(0, 0, 60, 0)}, [
    con({**ROW, 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(28),
         'flex_align_items': 'center', 'flex_align_items_mobile': 'stretch',
         'padding': box(60), 'padding_tablet': box(40), 'padding_mobile': box(36, 24),
         'background_background': 'classic', 'border_border': 'solid', 'border_width': box(0, 0, 3, 0),
         '__globals__': {'background_color': col('9f5d5c9'), 'border_color': col('secondary')}}, [
        con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(20)}, [
            h2('Scopri il canone a te riservato'),
            text('<p>Il canone di MVR CARE è particolarmente vantaggioso. Chiedi a EVAP quello riservato a te, '
                 'per la formula PURE o per la PLUS.</p>', '58b3754', 'text'),
        ]),
        con({'width': px(40, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(8)}, [
            heading('+39 0444 1276355', 'p', 'accent', 'primary', link='tel:+3904441276355'),
            heading('tecnico2@evap.it', 'p', 'text', 'primary', link='mailto:tecnico2@evap.it'),
            merge_globals(button('Richiedi il canone', 'https://evap.it/contattaci/'), {}),
        ]),
    ]),
])
fee['elements'][0]['elements'][1]['elements'][2]['settings']['_margin'] = box(22, 0, 0, 0)

# ---------------------------------------------------------------- 6. domande frequenti
FAQ = [
    ("Che differenza c'è tra PURE e PLUS?",
     "Entrambe comprendono un controllo remoto ogni settimana e la verifica dello stato di esercizio e della "
     "manutenzione. PURE prevede 4 visite tecniche programmate all'anno, la segnalazione delle anomalie con le "
     "azioni raccomandate e un rapporto sintetico di verifica. PLUS prevede 12 visite all'anno, l'analisi delle "
     "anomalie e delle perdite di produttività e un rapporto tecnico mensile."),
    ("A chi è rivolto MVR CARE?",
     "È il servizio di assistenza tecnica che EVAP dedica ai suoi clienti, per mantenere nel tempo l'efficienza "
     "e la continuità operativa dell'evaporatore MVR."),
    ("Che cosa ricevo dopo i controlli?",
     "Report e raccomandazioni per l'ottimizzazione dell'esercizio: con PURE un rapporto sintetico di verifica, "
     "con PLUS un rapporto tecnico mensile."),
    ("Quanto costa?",
     'Il canone è riservato e particolarmente vantaggioso: per conoscerlo <a href="https://evap.it/contattaci/">'
     'scrivi a EVAP</a> o chiama il +39 0444 1276355.'),
]
faq = boxed({**ROW, 'html_tag': 'section', 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(28),
             'margin': box(0, 0, 100, 0), 'margin_mobile': box(0, 0, 60, 0)}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%')}, [h2('Domande frequenti')]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0),
         'border_border': 'solid', 'border_width': box(1, 0, 0, 0), '__globals__': {'border_color': col('0012040')}}, [
        con({'flex_gap': gap(10), 'padding': box(26, 0, 26, 0),
             'border_border': 'solid', 'border_width': box(0, 0, 1, 0), '__globals__': {'border_color': col('0012040')}}, [
            heading(q, 'h3', 'c959aeb', 'primary'),
            merge_globals(text(f'<p>{a}</p>'), {'link_color': col('primary')}),
        ]) for q, a in FAQ
    ]),
])

# ---------------------------------------------------------------- documento
doc = {
    'content': [hero, why, do, plans, fee, faq],
    'page_settings': {'hide_title': 'yes', 'template': 'elementor_header_footer'},
    'version': '0.4',
    'title': 'MVR CARE',
    'type': 'page',
}
out = json.dumps(doc, ensure_ascii=False, indent=1)
assert '\u2014' not in out, 'lineetta lunga U+2014 nel modello'
with open(os.path.join(QUI, 'mvr-care-template.json'), 'w', encoding='utf-8') as f:
    f.write(out + '\n')
# gli stessi disegni come file a parte: li usa l'anteprima e si possono incollare in un widget HTML
os.makedirs(os.path.join(QUI, 'grafici'), exist_ok=True)
for nome, codice in (('anno-assistenza.html', grafici.anno()), ('ciclo-servizio.html', grafici.ciclo()),
                     ('schema-mvr-facoltativo.html', grafici.schema())):
    assert '\u2014' not in codice
    with open(os.path.join(QUI, 'grafici', nome), 'w', encoding='utf-8') as f:
        f.write(codice + '\n')
print('scritto mvr-care-template.json,', _n[0], 'elementi')
