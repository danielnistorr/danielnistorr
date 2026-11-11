"""Disegni SVG della pagina MVR CARE (usati dal modello di Elementor e dall'anteprima).

Ogni funzione restituisce il codice di un widget HTML di Elementor: un commento che spiega
dove si cambiano numeri ed etichette, un piccolo foglio di stile e i disegni. Due versioni
per disegno: larga (oltre 1024 px) e compatta (tablet e telefono, testi mai sotto gli 11 px).

Regole: solo dati della brochure; colori del kit di evap.it (variabili --e-global-color-*,
con il valore del sito come ripiego); carattere della pagina (Plus Jakarta Sans, ripiego
Sans-serif come il sito); nessuna animazione, ombra o gradiente; <title>, <desc> e aria.
"""
import math
from xml.sax.saxutils import escape

# ------------------------------------------------------------------ DATI (si cambia qui)
# L'anno di assistenza. Fonte: brochure, slide 4.
ANNO = {
    'mesi': 12,
    'settimane': 52,                      # 1 controllo remoto ogni settimana, in entrambe le formule
    'settimane_per_mese': [4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5],   # solo per disegnare le tacche (somma 52)
    # mesi (da 1 a 12) in cui si disegnano le visite: la brochure dice solo quante sono,
    # non quando; qui sono distribuite in modo regolare e la nota lo dice
    'visite_pure': [2, 5, 8, 11],
    'visite_plus': list(range(1, 13)),
    'rapporti_plus': list(range(1, 13)),  # "rapporto tecnico mensile": uno al mese
    'nome_pure': 'MVR CARE PURE',
    'nome_plus': 'MVR CARE PLUS',
    'nota_pure': 'più il rapporto sintetico di verifica',
    'nota_plus': '12 rapporti tecnici mensili',
    'legenda_controllo': 'Controllo remoto: 1 ogni settimana, in entrambe le formule',
    'legenda_visita': 'Visita tecnica programmata',
    'legenda_rapporto': 'Rapporto tecnico mensile (PLUS)',
    'nota_date': 'Le date delle visite sono indicative: si concordano con il cliente.',
}

# Il ciclo del servizio. Fonte: brochure, slide 3 (stessi testi della pagina).
CICLO = [
    ('Monitoraggio e verifiche periodiche', 'dei principali parametri operativi.'),
    ('Diagnosi preventiva', 'e individuazione tempestiva di eventuali criticità.'),
    ('Interventi mirati', 'per mantenere la massima efficienza, sicurezza e affidabilità.'),
    ('Report e raccomandazioni', "per l'ottimizzazione dell'esercizio."),
]

# ------------------------------------------------------------------ comune
STILE = """
.mcg{--mcg-p:var(--e-global-color-primary,#1D365C);--mcg-s:var(--e-global-color-secondary,#3798E2);--mcg-t:var(--e-global-color-text,#4F5D72);--mcg-b:var(--e-global-color-0012040,#1D365C40);--mcg-g:var(--e-global-color-386aba7,#DBDBDB);--mcg-w:var(--e-global-color-accent,#FFFFFF);--mcg-l:var(--e-global-color-50cd0e7,#FFFFFF36);margin:0;font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
figure.mcg svg{display:block;width:100%;height:auto;overflow:visible}
.mcg text{font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
.mcg .p{fill:var(--mcg-p)}.mcg .s{fill:var(--mcg-s)}.mcg .t{fill:var(--mcg-t)}.mcg .w{fill:var(--mcg-w)}.mcg .g{fill:var(--mcg-g)}
.mcg .sp{stroke:var(--mcg-p)}.mcg .ss{stroke:var(--mcg-s)}.mcg .st{stroke:var(--mcg-t)}.mcg .sb{stroke:var(--mcg-b)}.mcg .sl{stroke:var(--mcg-l)}.mcg .sw{stroke:var(--mcg-w)}
.mcg .no{fill:none}.mcg .b6{font-weight:600}.mcg .b7{font-weight:700}
.mcg .mcg-c{display:none}
@media (max-width:1024px){.mcg .mcg-l{display:none}.mcg .mcg-c{display:block}}
""".strip()


def _t(x, y, s, size, cls='t', anchor='start', extra=''):
    return f'<text x="{x:g}" y="{y:g}" font-size="{size}" class="{cls}" text-anchor="{anchor}"{extra}>{escape(s)}</text>'


def _wrap(s, n):
    righe, cur = [], ''
    for w in s.split():
        if cur and len(cur) + 1 + len(w) > n:
            righe.append(cur)
            cur = w
        else:
            cur = f'{cur} {w}'.strip()
    return righe + ([cur] if cur else [])


def _svg(cls, vb, ident, titolo, desc, corpo, extra=''):
    return (f'<svg class="{cls}" viewBox="{vb}" role="img" aria-labelledby="{ident}-t {ident}-d"{extra} '
            f'xmlns="http://www.w3.org/2000/svg"><title id="{ident}-t">{escape(titolo)}</title>'
            f'<desc id="{ident}-d">{escape(desc)}</desc>{corpo}</svg>')


# ------------------------------------------------------------------ 1. l'anno di assistenza
def anno():
    d = ANNO
    titolo = "L'anno di assistenza: MVR CARE PURE e MVR CARE PLUS a confronto"
    desc = (f"In un anno, in entrambe le formule, un controllo remoto ogni settimana ({d['settimane']} tacche). "
            f"{d['nome_pure']}: {len(d['visite_pure'])} visite tecniche programmate all'anno e il rapporto sintetico di verifica. "
            f"{d['nome_plus']}: {len(d['visite_plus'])} visite tecniche programmate all'anno e un rapporto tecnico ogni mese. "
            f"{d['nota_date']}")

    # --- versione larga: 1290 x 330, scala 1:1 con il contenuto della pagina a 1440
    X0, X1 = 300, 1290
    mw, ww = (X1 - X0) / d['mesi'], (X1 - X0) / d['settimane']
    c = []
    c.append(_t(0, 26, 'Mesi di servizio', 15))
    for m in range(d['mesi'] + 1):
        x = X0 + mw * m
        c.append(f'<line x1="{x:g}" y1="40" x2="{x:g}" y2="318" class="sb" stroke-width="1" stroke-opacity=".55"/>')
    for m in range(d['mesi']):
        c.append(_t(X0 + mw * (m + .5), 26, str(m + 1), 15, anchor='middle'))
    righe = [
        (d['nome_pure'], d['visite_pure'], [], 125, d['nota_pure']),
        (d['nome_plus'], d['visite_plus'], d['rapporti_plus'], 258, d['nota_plus']),
    ]
    for nome, visite, rapporti, y, nota in righe:
        c.append(_t(0, y - 40, nome, 16, 'p b6'))
        n = str(len(visite))
        c.append(_t(0, y + 14, n, 46, 'p b6'))
        c.append(_t(30 * len(n) + 6, y + 14, "visite all'anno", 15))
        c.append(_t(0, y + 42, nota, 15))
        c.append(f'<line x1="{X0}" y1="{y}" x2="{X1}" y2="{y}" class="sb" stroke-width="1"/>')
        for w in range(d['settimane']):
            x = X0 + ww * (w + .5)
            c.append(f'<line x1="{x:.1f}" y1="{y + 4}" x2="{x:.1f}" y2="{y + 18}" class="ss" stroke-width="2"/>')
        for m in visite:
            x = X0 + mw * (m - .5)
            c.append(f'<rect x="{x - 11:.1f}" y="{y - 30}" width="22" height="22" class="p v"/>')
        for m in rapporti:
            x = X0 + mw * m - 12
            c.append(f'<rect x="{x - 6:.1f}" y="{y + 28}" width="12" height="12" class="no sp r" stroke-width="2"/>')
    larga = _svg('mcg-l', '0 0 1290 318', 'mcg-anno-l', titolo, desc, ''.join(c))

    # --- versione compatta: mesi in verticale, 340 x 520
    c = []
    CP, CL = 62, 204          # inizio colonna PURE e colonna PLUS
    c.append(_t(CP, 18, d['nome_pure'], 14, 'p b6'))
    c.append(_t(CL, 18, d['nome_plus'], 14, 'p b6'))
    for x0, visite in ((CP, d['visite_pure']), (CL, d['visite_plus'])):
        n = str(len(visite))
        c.append(_t(x0, 56, n, 32, 'p b6'))
        c.append(_t(x0 + 21 * len(n) + 6, 56, "visite all'anno", 12))
    c.append(_t(0, 90, 'Mese', 12))
    top, h = 100, 32
    wk = 0
    for m in range(d['mesi']):
        y = top + h * m
        yc = y + h / 2
        c.append(f'<line x1="0" y1="{y}" x2="340" y2="{y}" class="sb" stroke-width="1"/>')
        c.append(_t(12, yc + 5, str(m + 1), 13, anchor='middle'))
        for x0, visite, rapporti in ((CP, d['visite_pure'], []), (CL, d['visite_plus'], d['rapporti_plus'])):
            for k in range(d['settimane_per_mese'][m]):
                x = x0 + 2 + 8 * k
                c.append(f'<line x1="{x}" y1="{yc - 6}" x2="{x}" y2="{yc + 6}" class="ss" stroke-width="2"/>')
            if (m + 1) in visite:
                c.append(f'<rect x="{x0 + 60}" y="{yc - 9}" width="18" height="18" class="p v"/>')
            if (m + 1) in rapporti:
                c.append(f'<rect x="{x0 + 92}" y="{yc - 5.5}" width="11" height="11" class="no sp r" stroke-width="2"/>')
        wk += d['settimane_per_mese'][m]
    yb = top + h * d['mesi']
    c.append(f'<line x1="0" y1="{yb}" x2="340" y2="{yb}" class="sb" stroke-width="1"/>')
    for i, riga in enumerate(_wrap(d['nota_pure'], 22)):
        c.append(_t(CP, yb + 22 + 17 * i, riga, 12))
    for i, riga in enumerate(_wrap(d['nota_plus'], 20)):
        c.append(_t(CL, yb + 22 + 17 * i, riga, 12))
    compatta = _svg('mcg-c', f'0 0 340 {yb + 50}', 'mcg-anno-c', titolo, desc, ''.join(c),
                    extra=' style="max-width:440px"')

    tacca = '<svg viewBox="0 0 10 16" aria-hidden="true"><line x1="5" y1="1" x2="5" y2="15" class="ss" stroke-width="2"/></svg>'
    visita = '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1" y="1" width="14" height="14" class="p"/></svg>'
    rapporto = '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="3" width="10" height="10" class="no sp" stroke-width="2"/></svg>'
    stile = STILE + """
.mcg-anno .mcg-legenda{display:flex;flex-wrap:wrap;gap:10px 32px;margin:26px 0 0;padding:0;list-style:none;color:var(--mcg-t);font-size:15px;line-height:1.4}
.mcg-anno .mcg-legenda li{display:flex;align-items:center;gap:10px;margin:0}
.mcg-anno .mcg-legenda svg{width:16px;height:16px;flex:none}
.mcg-anno .mcg-nota{margin:10px 0 0;color:var(--mcg-t);font-size:14px;line-height:1.4}
@media (max-width:767px){.mcg-anno .mcg-legenda{flex-direction:column;gap:8px;font-size:14px}}"""
    return f"""<!-- MVR CARE, "L'anno di assistenza" (widget HTML).
  Generato da elementor/genera_template.py con i dati di elementor/grafici.py (sezione ANNO):
  per cambiare numeri, mesi delle visite ed etichette si modifica lì e si rigenera il modello.
  Ritocchi a mano: le visite sono i <rect class="p v"> (posizione nell'attributo x), i rapporti
  mensili i <rect class="no sp r">, le tacche settimanali le <line class="ss">, le scritte i <text>.
  Ci sono due disegni: "mcg-l" (schermi oltre 1024 px) e "mcg-c" (tablet e telefono): vanno
  cambiati tutti e due. Legenda e nota sotto il disegno sono testo normale. Solo dati della brochure. -->
<style>{stile}</style>
<figure class="mcg mcg-anno">
{larga}
{compatta}
<ul class="mcg-legenda"><li>{tacca}{escape(d['legenda_controllo'])}</li><li>{visita}{escape(d['legenda_visita'])}</li><li>{rapporto}{escape(d['legenda_rapporto'])}</li></ul>
<figcaption class="mcg-nota">{escape(d['nota_date'])}</figcaption>
</figure>"""


# ------------------------------------------------------------------ 2. il ciclo del servizio
def ciclo():
    titolo = 'Il ciclo di MVR CARE'
    desc = ' '.join(f'{a} {b}' for a, b in CICLO) + ' Poi il ciclo ricomincia.'

    # --- versione larga: anello con le quattro fasi in senso orario, 740 x 500
    cx, cy, r = 370, 262, 122
    c = ['<defs><marker id="mcg-fr-l" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
         '<path d="M0 0 L10 5 L0 10 z" class="s"/></marker></defs>']
    for i in range(4):
        a0, a1 = math.radians(-90 + 90 * i + 13), math.radians(-90 + 90 * i + 77)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        c.append(f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}" class="no ss" stroke-width="2.5" marker-end="url(#mcg-fr-l)"/>')
    nodi = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    for x, y in nodi:
        c.append(f'<rect x="{x - 11}" y="{y - 11}" width="22" height="22" class="s"/>')
    c.append(_t(cx, cy + 7, 'MVR CARE', 20, 'w b6', 'middle'))
    # testi: sopra, a destra, sotto, a sinistra
    pos = [
        dict(x=cx, y=44, anchor='middle', nb=40, nd=44),
        dict(x=cx + r + 32, y=cy - 22, anchor='start', nb=21, nd=24),
        dict(x=cx, y=cy + r + 50, anchor='middle', nb=40, nd=40),
        dict(x=cx - r - 32, y=cy - 34, anchor='end', nb=17, nd=22),
    ]
    for (a, b), p in zip(CICLO, pos):
        y = p['y']
        for riga in _wrap(a, p['nb']):
            c.append(_t(p['x'], y, riga, 18, 'w b7', p['anchor']))
            y += 24
        for riga in _wrap(b, p['nd']):
            c.append(_t(p['x'], y, riga, 16, 'g', p['anchor']))
            y += 22
    larga = _svg('mcg-l', '0 0 740 500', 'mcg-ciclo-l', titolo, desc, ''.join(c), extra=' style="max-width:740px"')

    # --- versione compatta: fasi in colonna, freccia che torna in cima, 340 x 560
    c = ['<defs><marker id="mcg-fr-c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
         '<path d="M0 0 L10 5 L0 10 z" class="s"/></marker></defs>']
    xs, passo, y0 = 34, 138, 22
    ys = [y0 + passo * i for i in range(4)]
    for i in range(3):
        c.append(f'<line x1="{xs}" y1="{ys[i] + 16}" x2="{xs}" y2="{ys[i + 1] - 15}" class="ss" stroke-width="2.5" marker-end="url(#mcg-fr-c)"/>')
    c.append(f'<path d="M{xs - 12} {ys[3]} H8 V{ys[0]} H{xs - 15}" class="no ss" stroke-width="2.5" marker-end="url(#mcg-fr-c)"/>')
    for y in ys:
        c.append(f'<rect x="{xs - 10}" y="{y - 10}" width="20" height="20" class="s"/>')
    for (a, b), y in zip(CICLO, ys):
        yy = y + 6
        for riga in _wrap(a, 28):
            c.append(_t(64, yy, riga, 16, 'w b7'))
            yy += 22
        for riga in _wrap(b, 31):
            c.append(_t(64, yy, riga, 15, 'g'))
            yy += 21
    compatta = _svg('mcg-c', f'0 0 340 {ys[3] + 110}', 'mcg-ciclo-c', titolo, desc, ''.join(c),
                    extra=' style="max-width:440px"')
    return f"""<!-- MVR CARE, "Il ciclo del servizio" (widget HTML).
  Generato da elementor/genera_template.py con i testi di elementor/grafici.py (sezione CICLO),
  gli stessi della brochure: per cambiarli si modifica lì e si rigenera il modello.
  Ritocchi a mano: ogni fase è un gruppo di <text> (titolo in bianco, testo in grigio chiaro);
  le frecce sono i <path> e le <line> con marker. Due disegni: "mcg-l" (oltre 1024 px) e
  "mcg-c" (tablet e telefono): vanno cambiati tutti e due. -->
<style>{STILE}</style>
<figure class="mcg mcg-ciclo">
{larga}
{compatta}
</figure>"""


# ------------------------------------------------------------------ 3. facoltativo: come funziona un evaporatore MVR
SCHEMA_PASSI = [
    'Nello scambiatore di calore il liquido da trattare si scalda e bolle.',
    'Nel separatore il vapore si stacca dal liquido, che torna nello scambiatore e via via si concentra.',
    'Il compressore aspira il vapore e lo comprime: il vapore compresso è più caldo.',
    'Il vapore compresso torna nello scambiatore, cede il suo calore al liquido e condensa: esce come distillato.',
]


def schema():
    titolo = 'Come funziona un evaporatore MVR (schema di principio)'
    desc = ' '.join(f'{i + 1}. {p}' for i, p in enumerate(SCHEMA_PASSI))

    def badge(x, y, n):
        return (f'<circle cx="{x}" cy="{y}" r="14" class="p"/>'
                f'<text x="{x}" y="{y + 5}" font-size="15" class="w b7" text-anchor="middle">{n}</text>')

    def freccia(d, cls, w, ident, dash=''):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<path d="{d}" class="no {cls}" stroke-width="{w}"{da} marker-end="url(#{ident})"/>'

    def marker(ident, cls):
        return (f'<marker id="{ident}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
                f'<path d="M0 0 L10 5 L0 10 z" class="{cls}"/></marker>')

    # --- versione larga 1290 x 470 (O = spostamento orizzontale per centrare)
    O = 190
    E = (O + 420, 140, 100, 240)          # scambiatore: x, y, larghezza, altezza
    S = (O + 700, 120, 110, 280)          # separatore
    C = (O + 600, 66, 28)                 # compressore: centro e raggio
    c = ['<defs>', marker('mcg-sl', 't'), marker('mcg-sv', 's'), marker('mcg-sd', 'p'), '</defs>']
    ex, ey, ew, eh = E
    sx, sy, sw, sh = S
    # tubazioni
    c.append(freccia(f'M{O + 120} 430 H{ex + 50} V{ey + eh + 4}', 'st', 3, 'mcg-sl'))                       # alimentazione
    c.append(freccia(f'M{sx + sw / 2} {sy + sh} V430 H{ex + 58}', 'st', 3, 'mcg-sl'))                       # ricircolo
    c.append(freccia(f'M{sx + sw / 2} 430 V452 H{O + 990}', 'st', 3, 'mcg-sl'))                             # concentrato
    c.append(freccia(f'M{ex + 50} {ey} V114 H{O + 650} V200 H{sx - 4}', 'st', 3, 'mcg-sl'))                 # miscela verso il separatore
    c.append(freccia(f'M{sx + sw / 2} {sy} V{C[1]} H{C[0] + C[2] + 4}', 'ss', 3, 'mcg-sv'))                 # vapore
    c.append(freccia(f'M{C[0] - C[2]} {C[1]} H{O + 360} V200 H{ex - 4}', 'ss', 6, 'mcg-sv'))                # vapore compresso
    c.append(freccia(f'M{ex} 350 H{O + 120}', 'sp', 3, 'mcg-sd', '9 6'))                                     # distillato
    # componenti
    c.append(f'<rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" class="w sp" stroke-width="2.5"/>')
    for k in range(1, 6):
        x = ex + ew * k / 6
        c.append(f'<line x1="{x:.1f}" y1="{ey + 14}" x2="{x:.1f}" y2="{ey + eh - 14}" class="st" stroke-width="1.5"/>')
    c.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{sw / 2}" class="w sp" stroke-width="2.5"/>')
    c.append(f'<line x1="{sx + 8}" y1="{sy + sh * .62}" x2="{sx + sw - 8}" y2="{sy + sh * .62}" class="st" stroke-width="1.5"/>')
    c.append(f'<circle cx="{C[0]}" cy="{C[1]}" r="{C[2]}" class="w sp" stroke-width="2.5"/>')
    c.append(f'<path d="M{C[0] - 14} {C[1] - 16} L{C[0] + 16} {C[1] - 7} L{C[0] + 16} {C[1] + 7} L{C[0] - 14} {C[1] + 16} Z" class="no sp" stroke-width="2"/>')
    # scritte
    c.append(_t(ex - 16, 286, 'Scambiatore', 16, 'p b6', 'end'))
    c.append(_t(ex - 16, 307, 'di calore', 16, 'p b6', 'end'))
    c.append(_t(sx + sw + 18, sy + 40, 'Separatore', 16, 'p b6'))
    c.append(_t(C[0], C[1] - C[2] - 14, 'Compressore', 16, 'p b6', 'middle'))
    c.append(_t(sx + sw / 2 + 12, 90, 'Vapore', 15, 's b6'))
    c.append(_t(O + 346, 96, 'Vapore compresso,', 15, 's b6', 'end'))
    c.append(_t(O + 346, 115, 'più caldo', 15, 's b6', 'end'))
    c.append(_t(O + 120, 420, 'Liquido da trattare', 15, 't b6'))
    c.append(_t(O + 120, 340, 'Distillato', 15, 'p b6'))
    c.append(_t(O + 990, 442, 'Concentrato', 15, 't b6', 'end'))
    c.append(badge(ex + ew / 2, ey + eh / 2, 1))
    c.append(badge(sx + sw / 2, sy + sh * .4, 2))
    c.append(badge(C[0] + 60, C[1] - 18, 3))
    c.append(badge(O + 360, 150, 4))
    larga = _svg('mcg-l', '0 0 1290 470', 'mcg-schema-l', titolo, desc, ''.join(c))

    # --- versione compatta 340 x 440
    c = ['<defs>', marker('mcg-sl2', 't'), marker('mcg-sv2', 's'), marker('mcg-sd2', 'p'), '</defs>']
    E2, S2, C2 = (60, 120, 60, 170), (220, 108, 70, 200), (170, 54, 22)
    ex, ey, ew, eh = E2
    sx, sy, sw, sh = S2
    c.append(freccia(f'M{ex + 30} 410 V{ey + eh + 4}', 'st', 2.5, 'mcg-sl2'))
    c.append(freccia(f'M{sx + sw / 2} {sy + sh} V340 H{ex + 36}', 'st', 2.5, 'mcg-sl2'))
    c.append(freccia(f'M{sx + sw / 2} 340 V404', 'st', 2.5, 'mcg-sl2'))
    c.append(freccia(f'M{ex + 30} {ey} V94 H170 V180 H{sx - 4}', 'st', 2.5, 'mcg-sl2'))
    c.append(freccia(f'M{sx + sw / 2} {sy} V{C2[1]} H{C2[0] + C2[2] + 4}', 'ss', 2.5, 'mcg-sv2'))
    c.append(freccia(f'M{C2[0] - C2[2]} {C2[1]} H24 V170 H{ex - 4}', 'ss', 5, 'mcg-sv2'))
    c.append(freccia(f'M{ex} 268 H24 V404', 'sp', 2.5, 'mcg-sd2', '7 5'))
    c.append(f'<rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" class="w sp" stroke-width="2"/>')
    for k in range(1, 4):
        x = ex + ew * k / 4
        c.append(f'<line x1="{x:.1f}" y1="{ey + 10}" x2="{x:.1f}" y2="{ey + eh - 10}" class="st" stroke-width="1.2"/>')
    c.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="{sw / 2}" class="w sp" stroke-width="2"/>')
    c.append(f'<circle cx="{C2[0]}" cy="{C2[1]}" r="{C2[2]}" class="w sp" stroke-width="2"/>')
    c.append(f'<path d="M{C2[0] - 10} {C2[1] - 11} L{C2[0] + 11} {C2[1] - 5} L{C2[0] + 11} {C2[1] + 5} L{C2[0] - 10} {C2[1] + 11} Z" class="no sp" stroke-width="1.6"/>')
    c.append(_t(C2[0], 18, 'Compressore', 13, 'p b6', 'middle'))
    c.append(_t(262, 84, 'Vapore', 12, 's b6'))
    c.append(_t(ex + 36, 428, 'Liquido', 12, 't b6'))
    c.append(_t(20, 428, 'Distillato', 12, 'p b6', 'start'))
    c.append(_t(sx + sw / 2, 428, 'Concentrato', 12, 't b6', 'middle'))
    c.append(badge(ex + ew / 2, ey + eh / 2, 1))
    c.append(badge(sx + sw / 2, sy + sh * .4, 2))
    c.append(badge(C2[0] + 44, C2[1] - 14, 3))
    c.append(badge(24, 120, 4))
    compatta = _svg('mcg-c', '0 0 340 440', 'mcg-schema-c', titolo, desc, ''.join(c), extra=' style="max-width:440px"')
    passi = ''.join(f'<li><span class="mcg-n">{i + 1}</span>{escape(p)}</li>' for i, p in enumerate(SCHEMA_PASSI))
    stile = STILE + """
.mcg-schema .mcg-passi{display:grid;grid-template-columns:1fr 1fr;gap:16px 40px;margin:30px 0 0;padding:0;list-style:none;counter-reset:none;color:var(--mcg-t);font-size:16px;line-height:1.5}
.mcg-schema .mcg-passi li{display:flex;gap:12px;align-items:flex-start;margin:0}
.mcg-schema .mcg-n{flex:none;width:28px;height:28px;border-radius:50%;background:var(--mcg-p);color:var(--mcg-w);font-weight:700;font-size:14px;display:flex;align-items:center;justify-content:center}
@media (max-width:767px){.mcg-schema .mcg-passi{grid-template-columns:1fr;font-size:15px}}"""
    return f"""<!-- MVR CARE, "Come funziona un evaporatore MVR" (widget HTML, FACOLTATIVO).
  Schema di principio generico, senza dati EVAP: va controllato da un tecnico EVAP prima di pubblicarlo.
  Generato da elementor/genera_template.py con i testi di elementor/grafici.py (SCHEMA_PASSI e
  funzione schema). Due disegni: "mcg-l" (oltre 1024 px) e "mcg-c" (tablet e telefono). -->
<style>{stile}</style>
<figure class="mcg mcg-schema">
{larga}
{compatta}
<ol class="mcg-passi">{passi}</ol>
</figure>"""
