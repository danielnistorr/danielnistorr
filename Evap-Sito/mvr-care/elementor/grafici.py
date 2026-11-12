"""Disegni SVG e piccoli script della pagina MVR CARE, versione 2 (landing page commerciale).

Ogni funzione restituisce il codice di un widget HTML di Elementor: un commento che spiega
dove si cambiano numeri ed etichette, un piccolo foglio di stile e il disegno. Dove serve ci
sono due versioni: larga (oltre 1024 px) e compatta (tablet e telefono, testi mai sotto 11 px).

Regole: solo dati della brochure e del messaggio del cliente; colori della brochure (presi con
il contagocce dalle immagini delle slide, vedi COLORI); carattere della pagina (Plus Jakarta Sans,
ripiego Sans-serif come il sito); nessuna animazione, ombra o gradiente; <title>, <desc> e aria.
"""
import math
from xml.sax.saxutils import escape

# ------------------------------------------------------------------ COLORI della brochure (contagocce)
# Misurati sulle immagini delle slide (pptx/ppt/media/image1-4.png), mediana dei pixel pieni.
COLORI = {
    'navy': '#070D57',          # titoli (slide 2-4: #030853, copertina "MVR CARE": #02238C)
    'pure': '#06316C',          # nome "MVR CARE PURE"
    'plus': '#0A5B2B',          # nome "MVR CARE PLUS"
    'blu': '#0054A0',           # fascia blu (parte chiara)
    'blu_scuro': '#003868',     # fascia blu (parte scura)
    'verde': '#2F9F00',         # pillola "particolarmente vantaggioso", onda
    'verde_onda': '#49A108',    # onda verde della copertina
    'verde_bottone': '#2B880A', # verde dei bottoni: come la pillola ma scurito quanto basta per il testo bianco (4,5:1)
    'verde_icone': '#138D2D',   # spunte e icone
    'verde_barre': '#5EBB15',   # barre del grafico "MVR Monitoring"
    'verde_dato': '#057905',    # "28 kWh/m³"
    'azzurro_chiaro': '#E0F0FC',# scheda PURE
    'verde_chiaro': '#E8F8E4',  # scheda PLUS
    'pannello': '#E4F0F4',      # riquadro dei benefici (slide 2)
    'cielo': '#F2F8FE',         # fondo chiaro dell'apertura (cielo della copertina, senza sfumatura)
    'testo_voci': '#0C2444',    # testo delle voci con la spunta
    'testo': '#4F5D72',         # testo del sito (kit)
}

# ------------------------------------------------------------------ DATI (si cambia qui)
# L'anno di assistenza di ogni formula. Fonte: brochure, slide 4.
ANNO = {
    'mesi': 12,
    'settimane': 52,                      # 1 controllo remoto ogni settimana, in entrambe le formule
    # mesi (1-12) in cui si disegnano le visite: la brochure dice quante sono, non quando;
    # sono distribuite in modo regolare e la nota sotto le schede lo dice
    'visite': {'pure': [2, 5, 8, 11], 'plus': list(range(1, 13))},
    'rapporti': {'pure': [], 'plus': list(range(1, 13))},   # "rapporto tecnico mensile" solo PLUS
    'nome': {'pure': 'MVR CARE PURE', 'plus': 'MVR CARE PLUS'},
    'legenda_controllo': 'Controllo remoto, 1 ogni settimana',
    'legenda_visita': 'Visita tecnica programmata',
    'legenda_rapporto': 'Rapporto tecnico mensile (PLUS)',
    'nota_date': 'Le date delle visite sono indicative: si concordano con il cliente.',
}

# La schermata "MVR Monitoring" (ricostruzione della slide 3). Il dato va confermato da EVAP.
MONITOR = {
    'titolo': 'MVR Monitoring',
    'etichetta_dato': 'Consumo specifico',
    'numero': '28',
    'unita': 'kWh/m³',
    'stato': 'Impianto in esercizio',
    'barre': [34, 40, 46, 50, 57, 63, 70, 82],   # altezze in % (illustrative, senza numeri sugli assi)
    'logo': 'https://evap.it/wp-content/uploads/2025/09/05e4e93b-96da-4b0b-970b-40507e7db2f6-150x150.png',
    'foto': 'https://evap.it/wp-content/uploads/2025/10/IMG_9042-768x576.jpg',
}

# ------------------------------------------------------------------ comune
STILE = """
.mcg{--mcg-navy:#070D57;--mcg-pure:#06316C;--mcg-plus:#0A5B2B;--mcg-blu:#0054A0;--mcg-verde:#138D2D;--mcg-barre:#5EBB15;--mcg-dato:#057905;--mcg-t:var(--e-global-color-text,#4F5D72);--mcg-b:#1D365C33;--mcg-w:#FFFFFF;--mcg-schermo:#F2F6FA;--mcg-cornice:#262B36;--mcg-base:#D5DAE2;margin:0;font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
figure.mcg svg{display:block;width:100%;height:auto;overflow:visible}
.mcg text{font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
.mcg .f-navy{fill:var(--mcg-navy)}.mcg .f-pure{fill:var(--mcg-pure)}.mcg .f-plus{fill:var(--mcg-plus)}.mcg .f-blu{fill:var(--mcg-blu)}.mcg .f-verde{fill:var(--mcg-verde)}.mcg .f-barre{fill:var(--mcg-barre)}.mcg .f-dato{fill:var(--mcg-dato)}.mcg .f-t{fill:var(--mcg-t)}.mcg .f-w{fill:var(--mcg-w)}.mcg .f-schermo{fill:var(--mcg-schermo)}.mcg .f-cornice{fill:var(--mcg-cornice)}.mcg .f-base{fill:var(--mcg-base)}
.mcg .s-b{stroke:var(--mcg-b)}.mcg .s-blu{stroke:var(--mcg-blu)}.mcg .s-pure{stroke:var(--mcg-pure)}.mcg .s-plus{stroke:var(--mcg-plus)}.mcg .s-w{stroke:var(--mcg-w)}.mcg .s-t{stroke:var(--mcg-t)}
.mcg .no{fill:none}.mcg .b6{font-weight:600}.mcg .b7{font-weight:700}.mcg .b8{font-weight:800}
.mcg .mcg-c{display:none}
@media (max-width:1024px){.mcg .mcg-l{display:none}.mcg .mcg-c{display:block}}
""".strip()


def _t(x, y, s, size, cls='f-t', anchor='start', extra=''):
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


# ------------------------------------------------------------------ 1. l'anno di ogni formula (nelle schede)
def anno(formula):
    d = ANNO
    visite, rapporti, nome = d['visite'][formula], d['rapporti'][formula], d['nome'][formula]
    titolo = f"L'anno di {nome}"
    desc = (f"In un anno {len(visite)} visite tecniche programmate e un controllo remoto ogni settimana"
            + (f", con un rapporto tecnico ogni mese." if rapporti else ".") + ' ' + d['nota_date'])
    cl = 'pure' if formula == 'pure' else 'plus'

    def disegno(W, mese_font, quadro, rq, cls, ident, extra=''):
        X0, X1 = 0, W
        mw, ww = (X1 - X0) / d['mesi'], (X1 - X0) / d['settimane']
        c = []
        for m in range(d['mesi'] + 1):
            x = X0 + mw * m
            c.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="76" class="s-b" stroke-width="1"/>')
        for m in range(d['mesi']):
            c.append(_t(X0 + mw * (m + .5), 16, str(m + 1), mese_font, 'f-t', 'middle'))
        c.append(f'<line x1="{X0}" y1="46" x2="{X1}" y2="46" class="s-b" stroke-width="1"/>')
        for w in range(d['settimane']):
            x = X0 + ww * (w + .5)
            c.append(f'<line x1="{x:.1f}" y1="50" x2="{x:.1f}" y2="62" class="s-blu" stroke-width="2"/>')
        for m in visite:
            x = X0 + mw * (m - .5)
            c.append(f'<rect x="{x - quadro / 2:.1f}" y="{42 - quadro}" width="{quadro}" height="{quadro}" class="f-{cl} v"/>')
        for m in rapporti:
            x = X0 + mw * m - rq
            c.append(f'<rect x="{x - rq / 2:.1f}" y="66" width="{rq}" height="{rq}" class="no s-{cl} r" stroke-width="2"/>')
        return _svg(cls, f'0 0 {W} 80', ident, titolo, desc, ''.join(c), extra)

    larga = disegno(540, 15, 16, 9, 'mcg-l', f'mcg-anno-{formula}-l')
    compatta = disegno(300, 11, 11, 7, 'mcg-c', f'mcg-anno-{formula}-c')
    return f"""<!-- MVR CARE, l'anno di {nome} (widget HTML nella scheda della formula).
  Generato da elementor/genera_template.py con i dati di elementor/grafici.py (sezione ANNO):
  per cambiare numeri e mesi delle visite si modifica lì e si rigenera.
  A mano: le visite sono i <rect class="... v"> (posizione nell'attributo x), i rapporti mensili
  i <rect class="... r">, le tacche settimanali le <line class="s-blu">, i mesi i <text>.
  Due disegni: "mcg-l" (oltre 1024 px) e "mcg-c" (tablet e telefono): vanno cambiati tutti e due. -->
<style>{STILE}</style>
<figure class="mcg mcg-anno">
{larga}
{compatta}
</figure>"""


def legenda():
    d = ANNO
    tacca = '<svg viewBox="0 0 10 16" aria-hidden="true"><line x1="5" y1="1" x2="5" y2="15" class="s-blu" stroke-width="2"/></svg>'
    visita = ('<svg viewBox="0 0 34 16" aria-hidden="true" style="width:34px"><rect x="1" y="1" width="14" height="14" class="f-pure"/>'
              '<rect x="19" y="1" width="14" height="14" class="f-plus"/></svg>')
    rapporto = '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="3" width="10" height="10" class="no s-plus" stroke-width="2"/></svg>'
    stile = STILE + """
.mcg-legenda ul{display:flex;flex-wrap:wrap;gap:8px 30px;margin:0;padding:0;list-style:none;color:var(--mcg-t);font-size:15px;line-height:1.4}
.mcg-legenda li{display:flex;align-items:center;gap:10px;margin:0}
.mcg-legenda li svg{width:16px;height:16px;flex:none}
.mcg-legenda li svg[style]{width:34px}
.mcg-legenda p{margin:8px 0 0;color:var(--mcg-t);font-size:14px;line-height:1.4}"""
    return f"""<!-- MVR CARE, legenda delle linee dell'anno nelle schede (widget HTML). Testi in elementor/grafici.py, sezione ANNO. -->
<style>{stile}</style>
<div class="mcg mcg-legenda">
<ul><li>{tacca}{escape(d['legenda_controllo'])}</li><li>{visita}{escape(d['legenda_visita'])}</li><li>{rapporto}{escape(d['legenda_rapporto'])}</li></ul>
<p>{escape(d['nota_date'])}</p>
</div>"""


# ------------------------------------------------------------------ 2. la schermata "MVR Monitoring"
def monitoraggio():
    m = MONITOR
    titolo = f"Schermata {m['titolo']}"
    desc = (f"Ricostruzione della schermata {m['titolo']} della brochure: foto dell'impianto, "
            f"{m['etichetta_dato'].lower()} {m['numero']} {m['unita']}, {m['stato'].lower()}, grafico a barre senza valori.")

    def barre(x0, y0, w, h, n_w):
        c = [f'<line x1="{x0}" y1="{y0 + h}" x2="{x0 + w}" y2="{y0 + h}" class="s-b" stroke-width="1.5"/>']
        n = len(m['barre'])
        passo = w / n
        for i, p in enumerate(m['barre']):
            bh = h * p / 100
            c.append(f'<rect x="{x0 + passo * i + (passo - n_w) / 2:.1f}" y="{y0 + h - bh:.1f}" width="{n_w}" height="{bh:.1f}" class="f-barre"/>')
        return ''.join(c)

    def spunta(cx, cy, r):
        return (f'<circle cx="{cx}" cy="{cy}" r="{r}" class="f-verde"/>'
                f'<path d="M{cx - r * .45:.1f} {cy:.1f} L{cx - r * .1:.1f} {cy + r * .38:.1f} L{cx + r * .5:.1f} {cy - r * .35:.1f}" class="no s-w" stroke-width="{r * .22:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')

    # --- versione larga: portatile disegnato, 900 x 560
    c = ['<defs><clipPath id="mcg-foto-l"><rect x="100" y="104" width="370" height="366" rx="12"/></clipPath></defs>']
    c.append('<rect x="70" y="0" width="760" height="502" rx="22" class="f-cornice"/>')          # cornice dello schermo
    c.append('<rect x="84" y="14" width="732" height="474" rx="8" class="f-schermo"/>')          # schermo
    c.append('<path d="M0 506 H900 L878 540 Q874 548 862 548 H38 Q26 548 22 540 Z" class="f-base"/>')  # base
    c.append('<rect x="390" y="506" width="120" height="10" rx="5" class="f-cornice" opacity=".35"/>')
    c.append('<rect x="84" y="14" width="732" height="72" class="f-w"/>')                         # barra in alto
    c.append(f'<image href="{escape(m["logo"])}" x="100" y="24" width="52" height="52"/>')
    c.append(_t(166, 61, m['titolo'], 28, 'f-navy b7'))
    c.append(f'<image href="{escape(m["foto"])}" x="100" y="104" width="370" height="366" preserveAspectRatio="xMidYMid slice" clip-path="url(#mcg-foto-l)"/>')
    c.append('<rect x="490" y="104" width="310" height="164" rx="12" class="f-w"/>')
    c.append(_t(512, 144, m['etichetta_dato'], 23, 'f-navy b6'))
    c.append(f'<text x="512" y="226" class="f-dato b8"><tspan font-size="70">{escape(m["numero"])}</tspan><tspan font-size="34" dx="10">{escape(m["unita"])}</tspan></text>')
    c.append('<rect x="490" y="282" width="310" height="60" rx="12" class="f-w"/>')
    c.append(spunta(518, 312, 14))
    c.append(_t(542, 320, m['stato'], 22, 'f-navy b6'))
    c.append('<rect x="490" y="356" width="310" height="114" rx="12" class="f-w"/>')
    c.append(barre(512, 374, 266, 78, 20))
    larga = _svg('mcg-l', '0 0 900 550', 'mcg-monitor-l', titolo, desc, ''.join(c))

    # --- versione compatta: la sola schermata, in colonna, 360 x 520
    c = ['<defs><clipPath id="mcg-foto-c"><rect x="16" y="78" width="328" height="176" rx="10"/></clipPath></defs>']
    c.append('<rect x="0" y="0" width="360" height="516" rx="18" class="f-cornice"/>')
    c.append('<rect x="8" y="8" width="344" height="500" rx="12" class="f-schermo"/>')
    c.append('<rect x="8" y="8" width="344" height="58" rx="12" class="f-w"/><rect x="8" y="40" width="344" height="26" class="f-w"/>')
    c.append(f'<image href="{escape(m["logo"])}" x="20" y="16" width="42" height="42"/>')
    c.append(_t(72, 46, m['titolo'], 21, 'f-navy b7'))
    c.append(f'<image href="{escape(m["foto"])}" x="16" y="78" width="328" height="176" preserveAspectRatio="xMidYMid slice" clip-path="url(#mcg-foto-c)"/>')
    c.append('<rect x="16" y="266" width="328" height="104" rx="10" class="f-w"/>')
    c.append(_t(32, 296, m['etichetta_dato'], 17, 'f-navy b6'))
    c.append(f'<text x="32" y="352" class="f-dato b8"><tspan font-size="52">{escape(m["numero"])}</tspan><tspan font-size="26" dx="8">{escape(m["unita"])}</tspan></text>')
    c.append('<rect x="16" y="380" width="328" height="48" rx="10" class="f-w"/>')
    c.append(spunta(40, 404, 12))
    c.append(_t(62, 410, m['stato'], 17, 'f-navy b6'))
    c.append('<rect x="16" y="438" width="328" height="62" rx="10" class="f-w"/>')
    c.append(barre(32, 448, 296, 42, 22))
    compatta = _svg('mcg-c', '0 0 360 516', 'mcg-monitor-c', titolo, desc, ''.join(c), extra=' style="max-width:440px"')
    return f"""<!-- MVR CARE, schermata "MVR Monitoring" (widget HTML): ricostruzione della slide 3 della brochure.
  Generato da elementor/genera_template.py con i dati di elementor/grafici.py (sezione MONITOR):
  titolo, dato ("28" e "kWh/m³"), stato, altezze delle barre, indirizzi del logo e della foto.
  A mano: il dato è nei <tspan> dentro <text class="f-dato b8">, le scritte nei <text>, le immagini
  negli <image href="...">. Due disegni: "mcg-l" (portatile, oltre 1024 px) e "mcg-c" (tablet e telefono).
  IL DATO DI CONSUMO SPECIFICO E LA SUA FORMULAZIONE VANNO CONFERMATI DA EVAP PRIMA DI PUBBLICARE. -->
<style>{STILE}</style>
<figure class="mcg mcg-monitor">
{larga}
{compatta}
</figure>"""


# ------------------------------------------------------------------ 3. formula già scelta nel modulo
def modulo_js():
    return """<!-- MVR CARE: sceglie la formula nel modulo quando si arriva da un bottone di una scheda
  (indirizzo con ?formula=pure o ?formula=plus, anche dalle campagne). Il campo del modulo deve avere
  ID "formula" e le opzioni "PURE", "PLUS", "Non so, consigliatemi". Nessun effetto visivo. -->
<script>
(function () {
  var VALORI = { pure: 'PURE', plus: 'PLUS' };
  function imposta(v) {
    var s = document.querySelector('select[name="form_fields[formula]"]');
    var scelta = v && VALORI[String(v).toLowerCase()];
    if (!s || !scelta) return;
    for (var i = 0; i < s.options.length; i++) { if (s.options[i].value === scelta) { s.selectedIndex = i; } }
  }
  function daIndirizzo() { try { imposta(new URLSearchParams(location.search).get('formula')); } catch (e) {} }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', daIndirizzo); } else { daIndirizzo(); }
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="formula="]');
    if (!a) return;
    try { imposta(new URL(a.href, location.href).searchParams.get('formula')); } catch (err) {}
  }, true);
})();
</script>"""


def onda(colore, posizione='basso'):
    """Onda con lo stesso tracciato del divisore "Waves" di Elementor, per l'anteprima statica.
    'basso': come il divisore in basso con "Capovolgi" (l'onda sale dal bordo inferiore);
    'alto': come il divisore in alto (l'onda scende dal bordo superiore)."""
    t = ' transform="translate(0 100) scale(1 -1)"' if posizione == 'basso' else ''
    return (f'<svg class="mc-onda mc-onda--{posizione}" viewBox="0 0 1000 100" preserveAspectRatio="none" aria-hidden="true">'
            f'<path{t} fill="{colore}" d="M421.9,6.5c22.6-2.5,51.5,0.4,75.5,5.3c23.6,4.9,70.9,23.5,100.5,35.7c75.8,32.2,133.7,44.5,192.6,49.7'
            'c23.6,2.1,48.7,3.5,103.4-2.5c54.7-6,106.2-25.6,106.2-25.6V0H0v30.3c0,0,72,32.6,158.4,30.5c39.2-0.7,92.8-6.7,134-22.4'
            'c21.2-8.1,52.2-18.2,79.7-24.2C399.3,7.9,411.6,7.5,421.9,6.5z"/></svg>')


# stili delle classi usate dallo schema facoltativo (versione 1)
STILE_SCHEMA = """
.mcg{--mcg-p:var(--e-global-color-primary,#1D365C);--mcg-s:var(--e-global-color-secondary,#3798E2);--mcg-t:var(--e-global-color-text,#4F5D72);--mcg-b:var(--e-global-color-0012040,#1D365C40);--mcg-g:var(--e-global-color-386aba7,#DBDBDB);--mcg-w:var(--e-global-color-accent,#FFFFFF);--mcg-l:var(--e-global-color-50cd0e7,#FFFFFF36);margin:0;font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
figure.mcg svg{display:block;width:100%;height:auto;overflow:visible}
.mcg text{font-family:var(--e-global-typography-text-font-family,"Plus Jakarta Sans"),Sans-serif}
.mcg .p{fill:var(--mcg-p)}.mcg .s{fill:var(--mcg-s)}.mcg .t{fill:var(--mcg-t)}.mcg .w{fill:var(--mcg-w)}.mcg .g{fill:var(--mcg-g)}
.mcg .sp{stroke:var(--mcg-p)}.mcg .ss{stroke:var(--mcg-s)}.mcg .st{stroke:var(--mcg-t)}.mcg .sb{stroke:var(--mcg-b)}.mcg .sl{stroke:var(--mcg-l)}.mcg .sw{stroke:var(--mcg-w)}
.mcg .no{fill:none}.mcg .b6{font-weight:600}.mcg .b7{font-weight:700}
.mcg .mcg-c{display:none}
@media (max-width:1024px){.mcg .mcg-l{display:none}.mcg .mcg-c{display:block}}
""".strip()

_tt = _t


# ------------------------------------------------------------------ 3. facoltativo: come funziona un evaporatore MVR
SCHEMA_PASSI = [
    'Nello scambiatore di calore il liquido da trattare si scalda e bolle.',
    'Nel separatore il vapore si stacca dal liquido, che torna nello scambiatore e via via si concentra.',
    'Il compressore aspira il vapore e lo comprime: il vapore compresso è più caldo.',
    'Il vapore compresso torna nello scambiatore, cede il suo calore al liquido e condensa: esce come distillato.',
]


def schema():
    def _t(x, y, s, size, cls='t', anchor='start', extra=''):
        return _tt(x, y, s, size, cls, anchor, extra)

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
    stile = STILE_SCHEMA + """
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
