#!/usr/bin/env python3
"""VERSIONE 2, "BROCHURE" (alternativa): genera mvr-care-template-brochure.json, la landing page MVR CARE
con l'identità grafica della brochure (onde, fascia blu, pillola verde, schede pastello).
Il modello principale (versione 3, in stile sito) lo scrive genera_template.py, insieme alla pagina di
ringraziamento e ai disegni di grafici/.

Elementor 3.31.5. Widget nativi del gratuito (contenitori, Titolo, Editor di testo, Immagine, Pulsante,
Icona, Elenco icone, HTML) più UN widget di Elementor Pro 3.28: Modulo (form), nella sezione
#richiedi-proposta. Senza Pro attivo, Elementor scarta il modulo durante l'importazione e importa il resto.

Colori: quelli della brochure (grafici.COLORI, presi con il contagocce) per titoli, bottoni, schede e
fasce; il testo usa il colore globale del kit del sito. Carattere: Plus Jakarta Sans (quello del sito),
titoli a peso 800 nel navy della brochure.

Uso: python3 genera_template_brochure.py  (scrive mvr-care-template-brochure.json)
"""
import hashlib
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import grafici  # noqa: E402

C = grafici.COLORI
UPL = 'https://evap.it/wp-content/uploads/'
CTA = 'Richiedi la tua proposta MVR CARE'
ANCORA = '#richiedi-proposta'

# ---------------------------------------------------------------- utilità
_n = [0]


def uid():
    _n[0] += 1
    return hashlib.sha1(f'mvr-care-v2-{_n[0]}'.encode()).hexdigest()[:7]


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
        s['content_width'] = 'full'
    s.update(settings)
    return {'id': uid(), 'elType': 'container', 'isInner': inner, 'settings': s, 'elements': children}


def wid(kind, settings):
    return {'id': uid(), 'elType': 'widget', 'widgetType': kind, 'isInner': False,
            'settings': settings, 'elements': []}


def font(d, t, m, peso='800', lh=1.15, ls=None, transform='none'):
    s = {'typography_typography': 'custom', 'typography_font_family': 'Plus Jakarta Sans',
         'typography_font_size': px(d), 'typography_font_size_tablet': px(t), 'typography_font_size_mobile': px(m),
         'typography_font_weight': peso, 'typography_text_transform': transform, 'typography_text_decoration': 'none',
         'typography_line_height': px(lh, 'em')}
    if ls is not None:
        s['typography_letter_spacing'] = px(ls)
    return s


def heading(text, tag='h2', colore=C['navy'], fnt=None, glob_typo=None, link=None, extra=None):
    s = {'title': text, 'header_size': tag, 'title_color': colore}
    if fnt:
        s.update(fnt)
    if glob_typo:
        s['__globals__'] = {'typography_typography': typ(glob_typo)}
    if link:
        s['link'] = {'url': link, 'is_external': '', 'nofollow': '', 'custom_attributes': ''}
    if extra:
        s.update(extra)
    return wid('heading', s)


def titolo(text, tag='h2', colore=C['navy'], extra=None):
    """Titolo di sezione: Plus Jakarta Sans 800 nel navy della brochure."""
    return heading(text, tag, colore, font(44, 38, 31, '800', 1.15, -0.5), extra=extra)


def text(html_, glob_typo='text', colore=None, extra=None, fnt=None):
    s = {'editor': html_, 'paragraph_spacing': px(0)}
    g = {}
    if fnt:
        s.update(fnt)
    else:
        g['typography_typography'] = typ(glob_typo)
    if colore:
        s['text_color'] = colore
    else:
        g['text_color'] = col('text')
    if g:
        s['__globals__'] = g
    if extra:
        s.update(extra)
    return wid('text-editor', s)


def html(code, extra=None):
    s = {'html': code}
    if extra:
        s.update(extra)
    return wid('html', s)


def icona(nome, colore, misura=34, extra=None):
    s = {'selected_icon': {'value': f'fas fa-{nome}', 'library': 'fa-solid'}, 'view': 'default',
         'primary_color': colore, 'size': px(misura), '_element_width': 'auto'}
    if extra:
        s.update(extra)
    return wid('icon', s)


def bottone(url=ANCORA, label=CTA, align=None, larghezza_piena=False, extra=None):
    """Il bottone della landing: verde della brochure a pillola, testo bianco. Al passaggio diventa
    navy di colpo (durata della transizione 0)."""
    s = {
        'text': label,
        'link': {'url': url, 'is_external': '', 'nofollow': '', 'custom_attributes': ''},
        'background_background': 'classic', 'background_color': C['verde_bottone'],
        'button_text_color': '#FFFFFF',
        'button_background_hover_background': 'classic', 'button_background_hover_color': C['navy'],
        'hover_color': '#FFFFFF',
        'border_radius': box(40), 'text_padding': box(18, 34, 18, 34), 'text_padding_mobile': box(16, 20, 16, 20),
        'button_hover_transition_duration': {'unit': 's', 'size': 0, 'sizes': []},
    }
    s.update(font(18, 18, 16, '700', 1.25))
    if align:
        s['align'] = align
    if larghezza_piena:
        s['align'] = 'justify'
    if extra:
        s.update(extra)
    return wid('button', s)


def boxed(settings, children):
    """Contenitore esterno: contenuto largo 1290 px come le altre pagine del sito."""
    s = {'content_width': 'boxed', 'boxed_width': px(1290),
         'padding': box(0, 10), 'padding_tablet': box(0, 20), 'padding_mobile': box(0, 20)}
    s.update(settings)
    return con(s, children, inner=False)


ROW = {'flex_direction': 'row', 'flex_direction_mobile': 'column'}
ONDA = {'shape_divider_bottom': 'waves', 'shape_divider_bottom_color': C['verde_onda'],
        'shape_divider_bottom_width': px(100, '%'), 'shape_divider_bottom_height': px(70),
        'shape_divider_bottom_height_mobile': px(36), 'shape_divider_bottom_flip': 'yes'}

# ---------------------------------------------------------------- 1. apertura chiara, come la copertina
apertura = boxed({**ROW, 'html_tag': 'section', 'flex_align_items': 'center', 'flex_gap': gap(60),
                  'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(36),
                  'padding': box(190, 10, 120, 10), 'padding_tablet': box(170, 20, 100, 20), 'padding_mobile': box(130, 20, 70, 20),
                  'background_background': 'classic', 'background_color': C['cielo'], **ONDA}, [
    con({'width': px(56, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0)}, [
        heading('MVR CARE', 'h1', C['navy'], font(104, 80, 56, '800', 1.0, -1.5), extra={'_margin': box(0, 0, 24, 0)}),
        heading('Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.', 'p', C['navy'],
                font(27, 24, 21, '700', 1.35), extra={'_margin': box(0, 0, 36, 0), '_margin_mobile': box(0, 0, 28, 0)}),
        bottone(),
        text('<p>Fissa una call gratuita con i nostri tecnici per una consulenza di diagnosi gratuita e senza impegno.</p>',
             extra={'_margin': box(18, 0, 0, 0), '_element_width': 'initial', '_element_custom_width': px(520),
                    '_element_custom_width_tablet': px(100, '%'), '_element_width_mobile': 'inherit'}),
    ]),
    con({'width': px(44, '%'), 'width_mobile': px(100, '%'), 'flex_align_items': 'center'}, [
        wid('image', {
            # ritaglio dell'impianto dalla copertina della brochure (autorizzato dal cliente): da caricare nella
            # libreria media (anteprima/img/brochure-copertina-impianto.jpg) e scegliere qui; ora è un segnaposto
            # indirizzo relativo: Elementor non lo scarica e mette il suo segnaposto
            'image': {'url': '/wp-content/plugins/elementor/assets/images/placeholder.png', 'id': '', 'size': '',
                      'alt': "Impianto di evaporazione, illustrazione della brochure MVR CARE", 'source': 'library'},
            'image_size': 'full', 'width': px(100, '%'), 'space': px(100, '%'),
            'image_border_radius': box(24), 'height': px(510), 'height_tablet': px(420), 'height_mobile': px(340),
            'object-fit': 'cover', 'object-position': 'center center',
            '_element_width': 'initial', '_element_custom_width': px(428), '_element_custom_width_tablet': px(100, '%'),
            '_element_custom_width_mobile': px(100, '%'),
        }),
    ]),
])

# ---------------------------------------------------------------- fascia blu con i tre punti della copertina
PUNTI = [('cog', 'Continuità di produzione'), ('chart-line', 'Prestazioni costanti'), ('leaf', 'Efficienza e sostenibilità')]
fascia = boxed({**ROW, 'html_tag': 'section', 'flex_gap': gap(0), 'flex_align_items': 'stretch',
                'padding': box(34, 10, 34, 10), 'padding_mobile': box(14, 20, 14, 20),
                'background_background': 'classic', 'background_color': C['blu']}, [
    con({'width': px(33.333, '%'), 'width_mobile': px(100, '%'), 'flex_direction': 'row', 'flex_direction_mobile': 'row',
         'flex_align_items': 'center', 'flex_justify_content': 'center', 'flex_justify_content_mobile': 'flex-start',
         'flex_gap': gap(18), 'padding': box(8, 20), 'padding_mobile': box(16, 0),
         'border_border': 'solid', 'border_width': box(0, 0, 0, 0 if i == 0 else 1),
         'border_width_mobile': box(0 if i == 0 else 1, 0, 0, 0), 'border_color': 'rgba(255,255,255,0.45)'}, [
        icona(ic, '#FFFFFF', 36),
        heading(t, 'p', '#FFFFFF', font(22, 20, 19, '700', 1.2), extra={'_element_width': 'auto'}),
    ]) for i, (ic, t) in enumerate(PUNTI)
])

# ---------------------------------------------------------------- 2. perché conta
BENEFICI = [('industry', 'Evita fermi impianto imprevisti'), ('bullseye', 'Mantiene le performance progettuali'),
            ('coins', 'Riduce i costi operativi nel tempo')]
perche = boxed({'html_tag': 'section', 'flex_gap': gap(50), 'flex_gap_mobile': gap(36),
                'margin': box(110, 0, 110, 0), 'margin_mobile': box(64, 0, 64, 0)}, [
    con({**ROW, 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(32), 'flex_align_items': 'center'}, [
        con({'width': px(58, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(18)}, [
            titolo('Un evaporatore efficiente è il cuore della tua produttività'),
            wid('divider', {'style': 'solid', 'weight': px(5), 'width': px(64), 'color': C['verde_onda'],
                            'gap': px(4)}),
            text("<p>L'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione degli effluenti industriali.</p>",
                 '58b3754', C['navy']),
            text('<p>Per garantirne nel tempo la massima efficienza e continuità operativa, EVAP ha sviluppato '
                 '<strong>MVR CARE</strong>: il servizio di assistenza tecnica dedicato ai suoi clienti.</p>'),
            con({'padding': box(22, 26), 'margin': box(10, 0, 0, 0), 'background_background': 'classic',
                 'background_color': C['verde_chiaro'], 'border_radius': box(16)}, [
                heading('MVR CARE non è un costo aggiuntivo di assistenza: è un investimento programmato per ridurre '
                        'il rischio di inefficienze e interruzioni produttive.', 'p', C['plus'], font(20, 19, 18, '700', 1.45)),
            ]),
        ]),
        con({'width': px(42, '%'), 'width_mobile': px(100, '%')}, [
            wid('image', {
                'image': {'url': UPL + '2025/10/IMG_7517-768x1024.jpg', 'id': '', 'size': '',
                          'alt': 'Evaporatore EVAP con il quadro di controllo', 'source': 'library'},
                'image_size': 'full', 'width': px(100, '%'), 'height': px(520), 'height_tablet': px(460), 'height_mobile': px(340),
                'object-fit': 'cover', 'object-position': 'center center', 'image_border_radius': box(24),
            }),
        ]),
    ]),
    con({**ROW, 'flex_gap': gap(0), 'padding': box(34, 20), 'padding_mobile': box(10, 24),
         'background_background': 'classic', 'background_color': C['pannello'], 'border_radius': box(24)}, [
        con({'width': px(33.333, '%'), 'width_mobile': px(100, '%'), 'flex_direction': 'row', 'flex_direction_mobile': 'row',
             'flex_align_items': 'center', 'flex_gap': gap(20), 'padding': box(10, 30), 'padding_mobile': box(20, 0),
             'border_border': 'solid', 'border_width': box(0, 0, 0, 0 if i == 0 else 3),
             'border_width_mobile': box(0 if i == 0 else 2, 0, 0, 0), 'border_color': C['verde_onda']}, [
            icona(ic, C['navy'], 40),
            heading(t, 'p', C['navy'], font(21, 20, 19, '700', 1.3), extra={'_element_width': 'auto'}),
        ]) for i, (ic, t) in enumerate(BENEFICI)
    ]),
])

# ---------------------------------------------------------------- 3. monitoraggio (slide 3)
ATT = [('desktop', 'Monitoraggio e verifiche', 'periodiche dei principali parametri operativi.'),
       ('search', 'Diagnosi preventiva', 'e individuazione tempestiva di eventuali criticità.'),
       ('cog', 'Interventi mirati', 'per mantenere massima efficienza, sicurezza e affidabilità.'),
       ('chart-bar', 'Report e raccomandazioni', "per l'ottimizzazione dell'esercizio.")]
monitor = con({'content_width': 'boxed', 'boxed_width': px(1290), 'html_tag': 'section', **ROW,
               'flex_gap': gap(70), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(40), 'flex_align_items': 'center',
               'padding': box(100, 10), 'padding_tablet': box(90, 20), 'padding_mobile': box(64, 20),
               'background_background': 'classic', 'background_color': C['cielo']}, [
    con({'width': px(44, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(18)}, [
        titolo('Controllo, prevenzione, performance: sempre sotto controllo'),
        wid('divider', {'style': 'solid', 'weight': px(5), 'width': px(64), 'color': C['verde_onda'], 'gap': px(4)}),
        con({'flex_gap': gap(0), 'margin': box(6, 0, 0, 0)}, [
            con({'flex_direction': 'row', 'flex_direction_mobile': 'row', 'flex_gap': gap(20), 'flex_align_items': 'center',
                 'padding': box(18, 0), 'border_border': 'solid', 'border_width': box(0, 0, 1, 0), 'border_color': '#1D365C26'}, [
                icona(ic, C['verde_icone'], 36),
                text(f'<p><strong>{a}</strong> {b}</p>', fnt=font(18, 18, 17, '500', 1.45), colore=C['navy'],
                     extra={'_element_width': 'initial', '_element_custom_width': px(86, '%')}),
            ]) for ic, a, b in ATT
        ]),
        bottone(extra={'_margin': box(18, 0, 0, 0)}),
    ]),
    con({'width': px(56, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(22)}, [
        html(grafici.monitoraggio()),
        con({'flex_gap': gap(14)}, [
            con({'flex_gap': gap(0)}, [
                heading('28 kWh/m³', 'p', C['verde_dato'], font(60, 54, 48, '800', 1.0, -1)),
                heading('consumo specifico', 'p', C['navy'], font(17, 17, 16, '700', 1.3), extra={'_margin': box(6, 0, 0, 0)}),
            ]),
            text('<p>Controllo remoto settimanale dei principali parametri operativi.</p>'),
        ]),
    ]),
], inner=False)

# ---------------------------------------------------------------- 4. le due formule: due proposte
VOCI = {
    'pure': ['<strong>4 visite tecniche programmate all\'anno</strong>', '<strong>1 controllo remoto ogni settimana</strong>',
             'Verifica dello stato di esercizio e manutenzione', 'Segnalazione anomalie e azioni raccomandate',
             'Rapporto sintetico di verifica'],
    'plus': ['<strong>12 visite tecniche programmate all\'anno</strong>', '<strong>1 controllo remoto ogni settimana</strong>',
             'Verifica dello stato di esercizio e manutenzione', 'Analisi anomalie e perdite di produttività',
             'Rapporto tecnico mensile'],
}


def scheda(f):
    fondo = C['azzurro_chiaro'] if f == 'pure' else C['verde_chiaro']
    nome = C['pure'] if f == 'pure' else C['plus']
    return con({'width': px(50, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(22),
                'padding': box(38, 36), 'padding_tablet': box(30, 24), 'padding_mobile': box(28, 20),
                'background_background': 'classic', 'background_color': fondo, 'border_radius': box(24)}, [
        heading(f'MVR CARE {f.upper()}', 'h3', nome, font(40, 34, 30, '800', 1.1, -0.5)),
        html(grafici.anno(f)),
        con({'padding': box(22, 24), 'padding_mobile': box(18, 16), 'background_background': 'classic',
             'background_color': '#FFFFFF', 'border_radius': box(16)}, [
            wid('icon-list', {
                'icon_list': [{'_id': uid(), 'text': t, 'selected_icon': {'value': 'fas fa-check', 'library': 'fa-solid'}} for t in VOCI[f]],
                'space_between': px(14), 'icon_size': px(16), 'text_indent': px(14), 'icon_self_vertical_align': 'center',
                'icon_color': C['verde_icone'], 'text_color': C['testo_voci'],
                'icon_typography_typography': 'custom', 'icon_typography_font_family': 'Plus Jakarta Sans',
                'icon_typography_font_size': px(17), 'icon_typography_font_size_mobile': px(16),
                'icon_typography_font_weight': '500', 'icon_typography_line_height': px(1.4, 'em'),
            }),
        ]),
        bottone(f'?formula={f}{ANCORA}', larghezza_piena=True, extra={'_margin': box(6, 0, 0, 0)}),
    ])


formule = boxed({'html_tag': 'section', '_element_id': 'formule', 'flex_gap': gap(0),
                 'margin': box(110, 0, 110, 0), 'margin_mobile': box(64, 0, 64, 0)}, [
    con({'width': px(900), 'width_tablet': px(100, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(16)}, [
        titolo('Scegli il livello di servizio più adatto alle tue esigenze'),
        text("<p>Due formule flessibili, con la qualità e l'esperienza EVAP.</p>", '58b3754', C['navy']),
    ]),
    con({**ROW, 'flex_gap': gap(30), 'flex_gap_mobile': gap(24), 'flex_align_items': 'stretch',
         'margin': box(44, 0, 0, 0), 'margin_mobile': box(32, 0, 0, 0)}, [scheda('pure'), scheda('plus')]),
    html(grafici.legenda(), extra={'_margin': box(24, 0, 0, 0)}),
])

# ---------------------------------------------------------------- 5. canone e modulo (#richiedi-proposta)
CAMPI = [
    ('nome', 'text', 'Nome e cognome', True, '', '50'),
    ('azienda', 'text', 'Azienda', True, '', '50'),
    ('ruolo', 'text', 'Ruolo', False, '', '50'),
    ('email', 'email', 'Email', True, '', '50'),
    ('telefono', 'tel', 'Telefono', True, '', '50'),
    ('evaporatore', 'select', 'Hai già un evaporatore MVR?', False, 'Sì, EVAP\nSì, di un altro costruttore\nNo, sto valutando', '50'),
    ('settore', 'text', 'Settore o tipo di effluente', False, '', '100'),
    ('capacita', 'number', 'Capacità dell\'impianto (m³/giorno), facoltativo', False, '', '50'),
    ('anno', 'number', 'Anno di installazione, facoltativo', False, '', '50'),
    ('formula', 'select', 'Formula di interesse', False, 'PURE\nPLUS\nNon so, consigliatemi', '50'),
    ('esigenza', 'select', 'Esigenza principale', False, 'Evitare fermi impianto\nMantenere le prestazioni\nRidurre i costi operativi\nAltro', '50'),
    ('fascia', 'select', 'Fascia oraria preferita per la call', False, 'Mattina\nPomeriggio\nIndifferente', '100'),
    ('messaggio', 'textarea', 'Messaggio', False, '', '100'),
]
PRIVACY = ('Ho letto l\'<a href="https://evap.it/privacy-policy/" target="_blank">informativa privacy</a> '
           'e acconsento al trattamento dei miei dati per essere ricontattato.')
CONFERMA = ('Grazie, abbiamo ricevuto la tua richiesta. I tecnici EVAP ti contatteranno per fissare '
            'la call di diagnosi gratuita e senza impegno.')


def modulo():
    campi = []
    for cid, tipo, label, req, opzioni, w in CAMPI:
        f = {'_id': uid(), 'custom_id': cid, 'field_type': tipo, 'field_label': label, 'placeholder': '',
             'required': 'true' if req else '', 'width': w, 'width_mobile': '100'}
        if opzioni:
            f['field_options'] = opzioni
        if tipo == 'textarea':
            f['rows'] = 4
        if tipo == 'number' and cid == 'anno':
            f['field_min'] = 1950
            f['field_max'] = 2100
        campi.append(f)
    campi.append({'_id': uid(), 'custom_id': 'privacy', 'field_type': 'acceptance', 'field_label': 'Privacy',
                  'acceptance_text': PRIVACY, 'required': 'true', 'width': '100', 'width_mobile': '100'})
    return wid('form', {
        'form_name': 'Richiesta proposta MVR CARE',
        'form_fields': campi,
        'input_size': 'md', 'show_labels': 'yes', 'mark_required': 'yes', 'label_position': 'above',
        'button_text': 'Fissa la call di diagnosi gratuita', 'button_size': 'md', 'button_width': '100', 'button_align': 'stretch',
        # azioni: email a EVAP e raccolta nelle "Submissions" di Elementor. Per misurare le conversioni con la
        # pagina di ringraziamento: aggiungere l'azione "Reindirizzamento" (redirect); l'indirizzo è già scritto.
        'submit_actions': ['email', 'collect_submissions'],
        'email_to': 'tecnico2@evap.it',
        'email_subject': 'Richiesta proposta MVR CARE dal sito evap.it',
        'email_content': '[all-fields]',
        'email_from_name': 'Sito EVAP, MVR CARE',
        'email_reply_to': '[field id="email"]',
        'redirect_to': 'https://evap.it/servizi/mvr-care/grazie/',
        'custom_messages': 'yes',
        'success_message': CONFERMA,
        'error_message': 'Si è verificato un errore: riprova o scrivi a tecnico2@evap.it.',
        'required_field_message': 'Questo campo è obbligatorio.',
        'invalid_message': 'Controlla il dato inserito.',
        # aspetto, come l'anteprima
        'column_gap': px(20), 'row_gap': px(18),
        'label_color': C['navy'], 'mark_required_color': C['verde_bottone'],
        'label_typography_typography': 'custom', 'label_typography_font_family': 'Plus Jakarta Sans',
        'label_typography_font_size': px(15), 'label_typography_font_weight': '600',
        'field_text_color': C['testo_voci'], 'field_background_color': '#F5F8FB',
        'field_border_color': '#1D365C40', 'field_border_width': box(1), 'field_border_radius': box(10),
        'field_typography_typography': 'custom', 'field_typography_font_family': 'Plus Jakarta Sans',
        'field_typography_font_size': px(16),
        'button_background_color': C['verde_bottone'], 'button_text_color': '#FFFFFF',
        'button_background_hover_color': C['navy'], 'button_hover_color': '#FFFFFF',
        'button_border_radius': box(40), 'button_text_padding': box(18, 30),
        'button_typography_typography': 'custom', 'button_typography_font_family': 'Plus Jakarta Sans',
        'button_typography_font_size': px(18), 'button_typography_font_weight': '700',
        'button_typography_text_transform': 'none',
        'button_hover_animation': '',
    })


richiesta = con({'html_tag': 'section', '_element_id': 'richiedi-proposta', 'content_width': 'full', 'flex_gap': gap(0)}, [
    # fascia blu con l'onda verde, come la chiusura della slide 4
    boxed({'flex_gap': gap(0), 'flex_align_items': 'center', 'padding': box(80, 10, 150, 10),
           'padding_tablet': box(70, 20, 140, 20), 'padding_mobile': box(56, 20, 110, 20),
           'background_background': 'classic', 'background_color': C['blu_scuro'],
           'shape_divider_top': 'waves', 'shape_divider_top_color': C['verde_onda'],
           'shape_divider_top_width': px(100, '%'), 'shape_divider_top_height': px(60),
           'shape_divider_top_height_mobile': px(30)}, [
        con({'width': px(900), 'width_tablet': px(100, '%'), 'flex_gap': gap(22), 'flex_align_items': 'center'}, [
            icona('leaf', '#FFFFFF', 46),
            heading('Scopri il canone a te riservato, <span style="background:#2B880A;border-radius:40px;padding:0 .35em;'
                    '-webkit-box-decoration-break:clone;box-decoration-break:clone">particolarmente vantaggioso.</span>',
                    'h2', '#FFFFFF', font(44, 38, 30, '800', 1.3, -0.5), extra={'align': 'center'}),
            text('<p>Ogni evaporatore ha caratteristiche ed esigenze operative specifiche. Scopri la formula MVR CARE più '
                 'adatta al tuo impianto e richiedi una proposta economica personalizzata, senza impegno.</p>',
                 fnt=font(19, 18, 17, '500', 1.55), colore='#FFFFFF', extra={'align': 'center'}),
            bottone('#modulo-proposta', align='center', extra={'_margin': box(10, 0, 0, 0)}),
        ]),
    ]),
    # il modulo, su un riquadro bianco che sale sulla fascia
    boxed({'flex_gap': gap(0), 'margin': box(-90, 0, 110, 0), 'margin_mobile': box(-70, 0, 64, 0)}, [
        con({**ROW, '_element_id': 'modulo-proposta', 'flex_gap': gap(50), 'flex_gap_tablet': gap(30), 'flex_gap_mobile': gap(28),
             'padding': box(48), 'padding_tablet': box(32), 'padding_mobile': box(28, 20),
             'background_background': 'classic', 'background_color': '#FFFFFF', 'border_radius': box(24),
             'border_border': 'solid', 'border_width': box(1), 'border_color': '#1D365C26'}, [
            con({'width': px(36, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(16)}, [
                heading('Fissa una call gratuita con i nostri tecnici', 'h3', C['navy'], font(30, 27, 25, '800', 1.2, -0.3)),
                text('<p>Una consulenza di diagnosi gratuita e senza impegno, finalizzata alla quotazione del servizio MVR CARE '
                     'per il tuo impianto.</p>', '58b3754', C['navy']),
                text('<p>Preferisci telefonare? <a href="tel:+3904441276355">+39 0444 1276355</a><br>'
                     'Oppure scrivi a <a href="mailto:tecnico2@evap.it">tecnico2@evap.it</a></p>',
                     extra={'link_color': C['navy']}),
            ]),
            con({'width': px(64, '%'), 'width_mobile': px(100, '%')}, [
                modulo(),
                html(grafici.modulo_js()),
            ]),
        ]),
    ]),
])

# ---------------------------------------------------------------- 6. domande frequenti
FAQ = [
    ("Che differenza c'è tra PURE e PLUS?",
     "Entrambe comprendono un controllo remoto ogni settimana e la verifica dello stato di esercizio e manutenzione. "
     "PURE prevede 4 visite tecniche programmate all'anno, la segnalazione delle anomalie con le azioni raccomandate e "
     "un rapporto sintetico di verifica. PLUS prevede 12 visite tecniche programmate all'anno, l'analisi delle anomalie "
     "e delle perdite di produttività e un rapporto tecnico mensile."),
    ("Il controllo remoto è continuo?",
     "No: in entrambe le formule è previsto un controllo remoto ogni settimana dei principali parametri operativi, "
     "insieme alle visite tecniche programmate (4 all'anno con PURE, 12 con PLUS)."),
    ("Cosa succede dopo la richiesta?",
     "Fissiamo una call gratuita con i nostri tecnici: una consulenza di diagnosi gratuita e senza impegno, per individuare "
     "la formula MVR CARE più adatta al tuo impianto e prepararti una proposta economica personalizzata."),
    ("Quanto costa MVR CARE?",
     'Il canone è riservato e particolarmente vantaggioso, e dipende dalle caratteristiche e dalle esigenze operative del '
     f'tuo evaporatore. <a href="{ANCORA}">Richiedi la tua proposta personalizzata</a>, senza impegno.'),
]
faq = boxed({**ROW, 'html_tag': 'section', 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(28),
             'margin': box(0, 0, 110, 0), 'margin_mobile': box(0, 0, 64, 0)}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(18)}, [
        titolo('Domande frequenti'),
        wid('divider', {'style': 'solid', 'weight': px(5), 'width': px(64), 'color': C['verde_onda'], 'gap': px(4)}),
    ]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0),
         'border_border': 'solid', 'border_width': box(1, 0, 0, 0), 'border_color': '#1D365C26'}, [
        con({'flex_gap': gap(10), 'padding': box(26, 0, 26, 0),
             'border_border': 'solid', 'border_width': box(0, 0, 1, 0), 'border_color': '#1D365C26'}, [
            heading(q, 'h3', C['navy'], font(21, 20, 19, '700', 1.3)),
            text(f'<p>{a}</p>', extra={'link_color': C['verde_bottone']}),
        ]) for q, a in FAQ
    ]),
])

# ---------------------------------------------------------------- documenti
def normalizza(elementi, livello=0):
    """isInner: falso per i contenitori di primo livello, vero per tutti quelli dentro."""
    for e in elementi:
        if e['elType'] == 'container':
            e['isInner'] = livello > 0
            if livello > 0:
                e['settings'].setdefault('content_width', 'full')
        normalizza(e['elements'], livello + 1)
    return elementi


def scrivi(nome, contenuto, titolo_doc):
    normalizza(contenuto)
    doc = {'content': contenuto, 'page_settings': {'hide_title': 'yes', 'template': 'elementor_header_footer'},
           'version': '0.4', 'title': titolo_doc, 'type': 'page'}
    out = json.dumps(doc, ensure_ascii=False, indent=1)
    assert '\u2014' not in out, 'lineetta lunga U+2014 nel modello'
    with open(os.path.join(QUI, nome), 'w', encoding='utf-8') as f:
        f.write(out + '\n')


scrivi('mvr-care-template-brochure.json', [apertura, fascia, perche, monitor, formule, richiesta, faq], 'MVR CARE (versione brochure)')
print('scritto mvr-care-template-brochure.json,', _n[0], 'elementi')
