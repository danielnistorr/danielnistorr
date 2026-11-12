#!/usr/bin/env python3
"""Genera i modelli di Elementor (formato di esportazione 0.4) della landing page MVR CARE, VERSIONE 3
("in stile sito web", il modello principale):
- mvr-care-template.json: la pagina;
- mvr-care-grazie-template.json: la pagina di ringraziamento facoltativa (per misurare le conversioni);
- grafici/*.html: i widget HTML (anche per l'anteprima).
La versione 2 "brochure" resta come alternativa: la scrive genera_template_brochure.py.

Elementor 3.31.5. Widget nativi del gratuito (contenitori, Titolo, Editor di testo, Immagine, Pulsante,
Icona, Elenco icone, HTML) più UN widget di Elementor Pro 3.28: Modulo (form), nella sezione
#richiedi-proposta. Senza Pro attivo, Elementor scarta il modulo durante l'importazione e importa il resto.

Veste: quella del sito evap.it (kit 11): titoli a peso 600, bottoni del sito (azzurro, spigoli vivi,
15/30 px), contenuto largo 1290 px, 100 px tra le sezioni, filetti sottili, riquadri a spigoli vivi,
fascia blu del sito con la cornice bianca. Della brochure restano solo due accenti: il navy dei titoli
e il verde per spunte, icone, dettagli e la scheda PLUS.

Uso: python3 genera_template.py
"""
import hashlib
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)
import grafici  # noqa: E402

C = grafici.COLORI
NAVY = C['navy']                 # titoli (accento della brochure)
VERDE = C['verde_bottone']       # barra della scheda PLUS e dettagli (#2B880A)
SPUNTA = C['verde_icone']        # spunte e icone lineari (#138D2D)
FILETTO = '#1D365C26'            # filetti sottili
UPL = 'https://evap.it/wp-content/uploads/'
CTA = 'Richiedi la tua proposta MVR CARE'
ANCORA = '#richiedi-proposta'

# ---------------------------------------------------------------- utilità
_n = [0]


def uid():
    _n[0] += 1
    return hashlib.sha1(f'mvr-care-v3-{_n[0]}'.encode()).hexdigest()[:7]


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


def font(d, t, m, peso='600', lh=1.2, ls=None, transform='none'):
    s = {'typography_typography': 'custom', 'typography_font_family': 'Plus Jakarta Sans',
         'typography_font_size': px(d), 'typography_font_size_tablet': px(t), 'typography_font_size_mobile': px(m),
         'typography_font_weight': peso, 'typography_text_transform': transform, 'typography_text_decoration': 'none',
         'typography_line_height': px(lh, 'em')}
    if ls is not None:
        s['typography_letter_spacing'] = px(ls)
    return s


def heading(text, tag='h2', colore=NAVY, fnt=None, glob_typo=None, glob_colore=None, link=None, extra=None):
    s = {'title': text, 'header_size': tag}
    g = {}
    if glob_colore:
        g['title_color'] = col(glob_colore)
    else:
        s['title_color'] = colore
    if fnt:
        s.update(fnt)
    if glob_typo:
        g['typography_typography'] = typ(glob_typo)
    if g:
        s['__globals__'] = g
    if link:
        s['link'] = {'url': link, 'is_external': '', 'nofollow': '', 'custom_attributes': ''}
    if extra:
        s.update(extra)
    return wid('heading', s)


def titolo(text, tag='h2', colore=NAVY, extra=None):
    """Titolo di sezione come le pagine del sito: H2 del kit (38/35/30 px, peso 600), senza maiuscole
    iniziali su ogni parola, nel navy della brochure."""
    return heading(text, tag, colore, font(38, 35, 30, '600', 1.2), extra=extra)


def text(html_, glob_typo='text', colore=None, glob_colore='text', extra=None, fnt=None):
    s = {'editor': html_, 'paragraph_spacing': px(0)}
    g = {}
    if fnt:
        s.update(fnt)
    else:
        g['typography_typography'] = typ(glob_typo)
    if colore:
        s['text_color'] = colore
    elif glob_colore:
        g['text_color'] = col(glob_colore)
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


def icona(nome, colore=SPUNTA, misura=26, extra=None):
    """Icona lineare: Font Awesome "regular" (contorno), la sola libreria lineare di Elementor gratuito."""
    s = {'selected_icon': {'value': f'far fa-{nome}', 'library': 'fa-regular'}, 'view': 'default',
         'primary_color': colore, 'size': px(misura), '_element_width': 'auto'}
    if extra:
        s.update(extra)
    return wid('icon', s)


def bottone(url=ANCORA, label=CTA, su_scuro=False, pieno=False, extra=None):
    """Bottone del sito: colori del kit (azzurro, testo bianco; al passaggio blu del sito, oppure bianco
    sul fondo blu), spigoli vivi, 15/30 px, peso 500. Testo senza maiuscole iniziali: è la frase del cliente.
    Si inverte di colpo (durata della transizione 0)."""
    s = {
        'text': label,
        'link': {'url': url, 'is_external': '', 'nofollow': '', 'custom_attributes': ''},
        'background_background': 'classic', 'button_background_hover_background': 'classic',
        'border_radius': box(0), 'text_padding': box(15, 30, 15, 30), 'text_padding_mobile': box(15, 20, 15, 20),
        'button_hover_transition_duration': {'unit': 's', 'size': 0, 'sizes': []},
        '__globals__': {'background_color': col('secondary'), 'button_text_color': col('accent'),
                        'button_background_hover_color': col('accent' if su_scuro else 'primary'),
                        'hover_color': col('primary' if su_scuro else 'accent')},
    }
    s.update(font(16, 16, 16, '500', 1.2))
    if pieno:
        s['align'] = 'justify'
    if extra:
        s.update(extra)
    return wid('button', s)


def boxed(settings, children):
    """Contenitore esterno largo come le pagine del sito: 1290 px di contenuto."""
    s = {'content_width': 'boxed', 'boxed_width': px(1290),
         'padding': box(0, 10), 'padding_tablet': box(0, 20), 'padding_mobile': box(0, 20)}
    s.update(settings)
    return con(s, children, inner=False)


def riga_con_filetti(voci, dimensione_testo=(19, 18, 18), extra=None):
    """Riga di tre voci con icona lineare verde, filetto sopra e filetti verticali tra una e l'altra
    (sul telefono in colonna, con i filetti orizzontali)."""
    s = {'flex_direction': 'row', 'flex_direction_mobile': 'column', 'flex_gap': gap(0),
         'border_border': 'solid', 'border_width': box(1, 0, 0, 0), 'border_color': FILETTO}
    if extra:
        s.update(extra)
    d, t, m = dimensione_testo
    return con(s, [
        con({'width': px(33.333, '%'), 'width_mobile': px(100, '%'), 'flex_direction': 'row', 'flex_direction_mobile': 'row',
             'flex_align_items': 'center', 'flex_gap': gap(16),
             'padding': box(26, 30, 6, 0 if i == 0 else 30), 'padding_mobile': box(18, 0, 18, 0),
             'border_border': 'solid', 'border_width': box(0, 0, 0, 0 if i == 0 else 1),
             'border_width_mobile': box(0 if i == 0 else 1, 0, 0, 0), 'border_color': FILETTO}, [
            icona(ic, SPUNTA, 26),
            heading(etichetta, 'p', NAVY, font(d, t, m, '500', 1.3), extra={'_element_width': 'auto'}),
        ]) for i, (ic, etichetta) in enumerate(voci)
    ])


ROW = {'flex_direction': 'row', 'flex_direction_mobile': 'column'}

# ---------------------------------------------------------------- 1. apertura
apertura = boxed({'html_tag': 'section', 'flex_gap': gap(70), 'flex_gap_mobile': gap(40),
                  'padding': box(190, 10, 60, 10), 'padding_tablet': box(170, 20, 50, 20), 'padding_mobile': box(130, 20, 30, 20),
                  'background_background': 'classic', '__globals__': {'background_color': col('9f5d5c9')}}, [
    con({**ROW, 'flex_align_items': 'center', 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(36)}, [
        con({'width': px(56, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0)}, [
            heading('MVR CARE', 'h1', NAVY, font(80, 60, 44, '600', 1.0, -1), extra={'_margin': box(0, 0, 24, 0)}),
            text('<p>Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.</p>',
                 fnt=font(25, 23, 21, '500', 1.4), colore=NAVY,
                 extra={'_margin': box(0, 0, 34, 0), '_margin_mobile': box(0, 0, 28, 0),
                        '_element_width': 'initial', '_element_custom_width': px(640), '_element_width_mobile': 'inherit',
                        '_element_custom_width_tablet': px(100, '%')}),
            bottone(),
            text('<p>Fissa una call gratuita con i nostri tecnici per una consulenza di diagnosi gratuita e senza impegno.</p>',
                 extra={'_margin': box(16, 0, 0, 0), '_element_width': 'initial', '_element_custom_width': px(520),
                        '_element_custom_width_tablet': px(100, '%'), '_element_width_mobile': 'inherit'}),
        ]),
        con({'width': px(44, '%'), 'width_mobile': px(100, '%'), 'flex_align_items': 'flex-end',
             'flex_align_items_mobile': 'stretch'}, [
            wid('image', {
                # ritaglio dell'impianto dalla copertina della brochure (autorizzato dal cliente): caricarlo nella
                # libreria (anteprima/img/brochure-copertina-impianto.jpg) e sceglierlo qui. Indirizzo relativo:
                # Elementor non lo scarica e mette il suo segnaposto.
                'image': {'url': '/wp-content/plugins/elementor/assets/images/placeholder.png', 'id': '', 'size': '',
                          'alt': 'Impianto di evaporazione, illustrazione della brochure MVR CARE', 'source': 'library'},
                'image_size': 'full', 'width': px(100, '%'), 'height': px(510), 'height_tablet': px(420), 'height_mobile': px(340),
                'object-fit': 'cover', 'object-position': 'center center',
                '_element_width': 'initial', '_element_custom_width': px(428), '_element_custom_width_tablet': px(100, '%'),
                '_element_custom_width_mobile': px(100, '%'),
                '_border_border': 'solid', '_border_width': box(1), '_border_color': FILETTO,
            }),
        ]),
    ]),
    riga_con_filetti([('clock', 'Continuità di produzione'), ('chart-bar', 'Prestazioni costanti'),
                      ('lightbulb', 'Efficienza e sostenibilità')], (21, 20, 19)),
])

# ---------------------------------------------------------------- 2. perché conta
perche = boxed({'html_tag': 'section', 'flex_gap': gap(56), 'flex_gap_mobile': gap(36),
                'margin': box(100, 0, 100, 0), 'margin_mobile': box(60, 0, 60, 0)}, [
    con({**ROW, 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(32), 'flex_align_items': 'center'}, [
        con({'width': px(58, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(18)}, [
            titolo('Un evaporatore efficiente è il cuore della tua produttività', extra={'_margin': box(0, 0, 10, 0)}),
            text("<p>L'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione degli effluenti industriali.</p>",
                 '58b3754', NAVY),
            text('<p>Per garantirne nel tempo la massima efficienza e continuità operativa, EVAP ha sviluppato '
                 '<strong>MVR CARE</strong>: il servizio di assistenza tecnica dedicato ai suoi clienti.</p>'),
            con({'padding': box(22, 0, 0, 0), 'margin': box(12, 0, 0, 0),
                 'border_border': 'solid', 'border_width': box(3, 0, 0, 0), 'border_color': VERDE}, [
                heading('MVR CARE non è un costo aggiuntivo di assistenza: è un investimento programmato per ridurre '
                        'il rischio di inefficienze e interruzioni produttive.', 'p', NAVY, font(21, 20, 19, '600', 1.45)),
            ]),
        ]),
        con({'width': px(42, '%'), 'width_mobile': px(100, '%')}, [
            wid('image', {
                'image': {'url': UPL + '2025/10/IMG_7517-768x1024.jpg', 'id': '', 'size': '',
                          'alt': 'Evaporatore EVAP con il quadro di controllo', 'source': 'library'},
                'image_size': 'full', 'width': px(100, '%'), 'height': px(520), 'height_tablet': px(460), 'height_mobile': px(340),
                'object-fit': 'cover', 'object-position': 'center center',
            }),
        ]),
    ]),
    riga_con_filetti([('calendar-check', 'Evita fermi impianto imprevisti'), ('dot-circle', 'Mantiene le performance progettuali'),
                      ('money-bill-alt', 'Riduce i costi operativi nel tempo')], (21, 20, 19),
                     extra={'border_width': box(1, 0, 1, 0), 'padding': box(0, 0, 20, 0), 'padding_mobile': box(0)}),
])

# ---------------------------------------------------------------- 3. monitoraggio
ATT = [('eye', 'Monitoraggio e verifiche', 'periodiche dei principali parametri operativi.'),
       ('clipboard', 'Diagnosi preventiva', 'e individuazione tempestiva di eventuali criticità.'),
       ('life-ring', 'Interventi mirati', 'per mantenere massima efficienza, sicurezza e affidabilità.'),
       ('file-alt', 'Report e raccomandazioni', "per l'ottimizzazione dell'esercizio.")]
monitor = con({'content_width': 'boxed', 'boxed_width': px(1290), 'html_tag': 'section', **ROW,
               'flex_gap': gap(70), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(40), 'flex_align_items': 'center',
               'padding': box(100, 10), 'padding_tablet': box(90, 20), 'padding_mobile': box(60, 20),
               'background_background': 'classic', '__globals__': {'background_color': col('9f5d5c9')}}, [
    con({'width': px(44, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(18)}, [
        titolo('Controllo, prevenzione, performance: sempre sotto controllo'),
        con({'flex_gap': gap(0), 'margin': box(6, 0, 0, 0), 'border_border': 'solid', 'border_width': box(1, 0, 0, 0),
             'border_color': FILETTO}, [
            con({'flex_direction': 'row', 'flex_direction_mobile': 'row', 'flex_gap': gap(18), 'flex_align_items': 'center',
                 'padding': box(18, 0), 'border_border': 'solid', 'border_width': box(0, 0, 1, 0), 'border_color': FILETTO}, [
                icona(ic, SPUNTA, 26),
                text(f'<p><strong>{a}</strong> {b}</p>', fnt=font(17, 17, 16, '400', 1.5), colore=NAVY,
                     extra={'_element_width': 'initial', '_element_custom_width': px(88, '%')}),
            ]) for ic, a, b in ATT
        ]),
        bottone(extra={'_margin': box(14, 0, 0, 0)}),
    ]),
    con({'width': px(56, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(26)}, [
        html(grafici.monitoraggio()),
        con({**ROW, 'flex_direction_mobile': 'column', 'flex_gap': gap(30), 'flex_gap_mobile': gap(10),
             'flex_align_items': 'flex-end', 'flex_align_items_mobile': 'flex-start',
             'padding': box(22, 0, 0, 0), 'border_border': 'solid', 'border_width': box(1, 0, 0, 0), 'border_color': FILETTO}, [
            con({'width': px(50, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0)}, [
                heading('28 <span style="font-size:.42em;letter-spacing:0">kWh/m³</span>', 'p', C['verde_dato'],
                        font(76, 66, 58, '600', 1.0, -1.5)),
                heading('consumo specifico', 'p', NAVY, font(17, 17, 16, '600', 1.3), extra={'_margin': box(8, 0, 0, 0)}),
            ]),
            con({'width': px(50, '%'), 'width_mobile': px(100, '%')}, [
                text('<p>Controllo remoto settimanale dei principali parametri operativi.</p>'),
            ]),
        ]),
    ]),
], inner=False)

# ---------------------------------------------------------------- 4. le due formule
VOCI = {
    'pure': ['<strong>4 visite tecniche programmate all\'anno</strong>', '<strong>1 controllo remoto ogni settimana</strong>',
             'Verifica dello stato di esercizio e manutenzione', 'Segnalazione anomalie e azioni raccomandate',
             'Rapporto sintetico di verifica'],
    'plus': ['<strong>12 visite tecniche programmate all\'anno</strong>', '<strong>1 controllo remoto ogni settimana</strong>',
             'Verifica dello stato di esercizio e manutenzione', 'Analisi anomalie e perdite di produttività',
             'Rapporto tecnico mensile'],
}


def scheda(f):
    barra = {'background_background': 'classic'}
    if f == 'pure':
        barra['__globals__'] = {'background_color': col('secondary')}
    else:
        barra['background_color'] = VERDE
    return con({'width': px(50, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0),
                'border_border': 'solid', 'border_width': box(1), 'border_color': FILETTO,
                'background_background': 'classic', 'background_color': '#FFFFFF'}, [
        con({**barra, 'min_height': px(6), 'width': px(100, '%')}, []),     # barra in alto: blu PURE, verde PLUS
        con({'flex_gap': gap(22), 'padding': box(34, 36, 36, 36), 'padding_tablet': box(28, 24), 'padding_mobile': box(26, 20)}, [
            heading(f'MVR CARE {f.upper()}', 'h3', NAVY, font(34, 30, 28, '600', 1.15, -0.3)),
            html(grafici.anno(f)),
            wid('icon-list', {
                'icon_list': [{'_id': uid(), 'text': t, 'selected_icon': {'value': 'fas fa-check', 'library': 'fa-solid'}} for t in VOCI[f]],
                'space_between': px(26), 'icon_size': px(15), 'text_indent': px(14), 'icon_self_vertical_align': 'center',
                'divider': 'yes', 'divider_style': 'solid', 'divider_weight': px(1), 'divider_color': FILETTO,
                'icon_color': SPUNTA, 'text_color': C['testo_voci'],
                'icon_typography_typography': 'custom', 'icon_typography_font_family': 'Plus Jakarta Sans',
                'icon_typography_font_size': px(16), 'icon_typography_font_weight': '400', 'icon_typography_line_height': px(1.45, 'em'),
                '_border_border': 'solid', '_border_width': box(1, 0, 1, 0), '_border_color': FILETTO,
                '_padding': box(14, 0, 14, 0),
            }),
            bottone(f'?formula={f}{ANCORA}', pieno=True, extra={'_margin': box(4, 0, 0, 0)}),
        ]),
    ])


formule = boxed({'html_tag': 'section', '_element_id': 'formule', 'flex_gap': gap(0),
                 'margin': box(100, 0, 100, 0), 'margin_mobile': box(60, 0, 60, 0)}, [
    con({'width': px(900), 'width_tablet': px(100, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(16)}, [
        titolo('Scegli il livello di servizio più adatto alle tue esigenze'),
        text("<p>Due formule flessibili, con la qualità e l'esperienza EVAP.</p>", '58b3754', NAVY),
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
        if cid == 'anno':
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
        # aspetto: i campi del kit del sito (bordo 1 px blu al 25%, spigoli vivi) e il bottone del sito
        'column_gap': px(20), 'row_gap': px(18),
        'mark_required_color': VERDE,
        'label_typography_typography': 'custom', 'label_typography_font_family': 'Plus Jakarta Sans',
        'label_typography_font_size': px(15), 'label_typography_font_weight': '500',
        'field_background_color': '#FFFFFF', 'field_border_width': box(1), 'field_border_radius': box(0),
        'button_border_radius': box(0), 'button_text_padding': box(15, 30),
        'button_typography_typography': 'custom', 'button_typography_font_family': 'Plus Jakarta Sans',
        'button_typography_font_size': px(16), 'button_typography_font_weight': '500',
        'button_typography_text_transform': 'none',
        '__globals__': {'label_color': col('primary'), 'field_text_color': col('primary'),
                        'field_border_color': col('0012040'), 'button_background_color': col('secondary'),
                        'button_text_color': col('accent'), 'button_background_hover_color': col('primary'),
                        'button_hover_color': col('accent')},
    })


richiesta = con({'content_width': 'boxed', 'boxed_width': px(1290), 'html_tag': 'section', '_element_id': 'richiedi-proposta',
                 **ROW, 'flex_gap': gap(60), 'flex_gap_tablet': gap(40), 'flex_gap_mobile': gap(36), 'flex_align_items': 'flex-start',
                 'padding': box(100, 10), 'padding_tablet': box(90, 20), 'padding_mobile': box(60, 10),
                 'border_border': 'solid', 'border_width': box(20), 'border_width_mobile': box(10),
                 'background_background': 'classic',
                 '__globals__': {'background_color': col('primary'), 'border_color': col('accent')}}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(20)}, [
        titolo('Scopri il canone a te riservato, particolarmente vantaggioso.', colore='#FFFFFF'),
        text('<p>Ogni evaporatore ha caratteristiche ed esigenze operative specifiche. Scopri la formula MVR CARE più '
             'adatta al tuo impianto e richiedi una proposta economica personalizzata, senza impegno.</p>',
             '58b3754', glob_colore='accent'),
        bottone('#modulo-proposta', su_scuro=True, extra={'_margin': box(6, 0, 0, 0)}),
        con({'margin': box(18, 0, 0, 0), 'padding': box(22, 0, 0, 0), 'flex_gap': gap(10),
             'border_border': 'solid', 'border_width': box(1, 0, 0, 0), '__globals__': {'border_color': col('50cd0e7')}}, [
            heading('Fissa una call gratuita con i nostri tecnici', 'h3', '#FFFFFF', font(21, 20, 19, '600', 1.3)),
            text('<p>Una consulenza di diagnosi gratuita e senza impegno, finalizzata alla quotazione del servizio MVR CARE '
                 'per il tuo impianto.</p>', glob_colore='386aba7'),
            text('<p>Preferisci telefonare? <a href="tel:+3904441276355">+39 0444 1276355</a><br>'
                 'Oppure scrivi a <a href="mailto:tecnico2@evap.it">tecnico2@evap.it</a></p>',
                 glob_colore='386aba7', extra={'link_color': '#FFFFFF'}),
        ]),
    ]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), '_element_id': 'modulo-proposta',
         'padding': box(40), 'padding_tablet': box(30), 'padding_mobile': box(24, 18),
         'background_background': 'classic', 'background_color': '#FFFFFF'}, [
        modulo(),
        html(grafici.modulo_js()),
    ]),
], inner=False)

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
             'margin': box(100, 0, 100, 0), 'margin_mobile': box(60, 0, 60, 0)}, [
    con({'width': px(40, '%'), 'width_mobile': px(100, '%')}, [titolo('Domande frequenti')]),
    con({'width': px(60, '%'), 'width_mobile': px(100, '%'), 'flex_gap': gap(0),
         'border_border': 'solid', 'border_width': box(1, 0, 0, 0), 'border_color': FILETTO}, [
        con({'flex_gap': gap(10), 'padding': box(26, 0, 26, 0),
             'border_border': 'solid', 'border_width': box(0, 0, 1, 0), 'border_color': FILETTO}, [
            heading(q, 'h3', NAVY, glob_typo='c959aeb'),
            text(f'<p>{a}</p>', extra={'link_color': C['verde_dato']}),
        ]) for q, a in FAQ
    ]),
])

# ---------------------------------------------------------------- pagina di ringraziamento (facoltativa)
grazie = boxed({'html_tag': 'section', 'flex_gap': gap(22), 'flex_align_items': 'flex-start',
                'padding': box(190, 10, 100, 10), 'padding_mobile': box(130, 20, 60, 20),
                'background_background': 'classic', '__globals__': {'background_color': col('9f5d5c9')}}, [
    heading('Grazie, abbiamo ricevuto la tua richiesta', 'h1', NAVY, font(54, 45, 34, '600', 1.15, -0.5)),
    text('<p>I tecnici EVAP ti contatteranno per fissare la call di diagnosi gratuita e senza impegno sul tuo evaporatore MVR.</p>',
         fnt=font(21, 20, 18, '500', 1.5), colore=NAVY,
         extra={'_element_width': 'initial', '_element_custom_width': px(720), '_element_width_mobile': 'inherit'}),
    text('<p>Per qualsiasi necessità: <a href="tel:+3904441276355">+39 0444 1276355</a>, '
         '<a href="mailto:tecnico2@evap.it">tecnico2@evap.it</a>.</p>', extra={'link_color': NAVY}),
    bottone('/servizi/mvr-care/', 'Torna a MVR CARE'),
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
    assert '\\u2014' not in out and chr(0x2014) not in out, 'lineetta lunga nel modello'
    with open(os.path.join(QUI, nome), 'w', encoding='utf-8') as f:
        f.write(out + '\n')


scrivi('mvr-care-template.json', [apertura, perche, monitor, formule, richiesta, faq], 'MVR CARE')
scrivi('mvr-care-grazie-template.json', [grazie], 'MVR CARE, grazie')

# gli stessi disegni come file a parte: li usa l'anteprima e si possono incollare in un widget HTML
os.makedirs(os.path.join(QUI, 'grafici'), exist_ok=True)
for nome, codice in (('anno-pure.html', grafici.anno('pure')), ('anno-plus.html', grafici.anno('plus')),
                     ('anno-legenda.html', grafici.legenda()), ('monitoraggio.html', grafici.monitoraggio()),
                     ('modulo-formula.html', grafici.modulo_js()),
                     ('schema-mvr-facoltativo.html', grafici.schema())):
    assert chr(0x2014) not in codice
    with open(os.path.join(QUI, 'grafici', nome), 'w', encoding='utf-8') as f:
        f.write(codice + '\n')
print('scritti mvr-care-template.json e mvr-care-grazie-template.json (versione 3),', _n[0], 'elementi')
