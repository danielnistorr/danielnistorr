# -*- coding: utf-8 -*-
"""
Logo di Encore: un anello aperto con un punto nel varco (il ciclo che si chiude: ogni chilo torna al marchio)
e la scritta ENCORE in Instrument Sans SemiBold, spaziata, convertita in tracciati (il file non dipende dal font).
Uso: python3 logo.py <percorso InstrumentSans[wdth,wght].ttf>
Scrive in ../logo/: orizzontale scuro e chiaro, solo marchio scuro e chiaro, in SVG.
"""
import math
import os
import sys

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(QUI), 'logo')
INK, PAPER = '#131316', '#FFFFFF'


def scritta(font, testo='ENCORE', altezza_maiuscole=40.0, spaziatura=0.34):
    """Tracciato SVG della scritta, con la linea di base a y=0 e la x che parte da 0. Ritorna (path, larghezza)."""
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upm = font['head'].unitsPerEm
    cap = getattr(font['OS/2'], 'sCapHeight', 0) or 700
    k = altezza_maiuscole / cap
    pen = SVGPathPen(gs)
    x = 0.0
    for i, ch in enumerate(testo):
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (k, 0, 0, -k, x, 0))
        gs[g].draw(tp)
        x += gs[g].width * k
        if i < len(testo) - 1:
            x += spaziatura * upm * k * 0.72     # spaziatura in em sul corpo del carattere
    return pen.getCommands(), x


def anello(cx, cy, r, colore, spessore, varco_gradi=46, angolo_punto=0):
    """Anello aperto: arco di (360 - varco) gradi, punto pieno al centro del varco."""
    a0 = math.radians(angolo_punto + varco_gradi / 2)
    a1 = math.radians(angolo_punto - varco_gradi / 2 + 360)
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    ap = math.radians(angolo_punto)
    px, py = cx + r * math.cos(ap), cy + r * math.sin(ap)
    arco = (f'<path d="M {x0:.2f} {y0:.2f} A {r} {r} 0 1 1 {x1:.2f} {y1:.2f}" fill="none" stroke="{colore}" '
            f'stroke-width="{spessore}" stroke-linecap="round"/>')
    punto = f'<circle cx="{px:.2f}" cy="{py:.2f}" r="{spessore * 1.55:.2f}" fill="{colore}"/>'
    return arco + punto


def svg(w, h, corpo, titolo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}" '
            f'role="img" aria-label="{titolo}"><title>{titolo}</title>{corpo}</svg>\n')


def main():
    font = TTFont(sys.argv[1])
    font = instantiateVariableFont(font, {'wght': 600, 'wdth': 100})
    os.makedirs(OUT, exist_ok=True)
    path, larg = scritta(font)
    cap = 40.0
    # orizzontale: anello alto quanto 1,6 maiuscole, a sinistra della scritta
    r = cap * 0.8
    pad = 8
    cx, cy = pad + r + 3, pad + r + 3
    gx = cx + r + 3 + 28
    h = 2 * (r + 3) + 2 * pad
    base = cy + cap / 2
    w = gx + larg + pad
    for nome, col in (('encore-logo', INK), ('encore-logo-bianco', PAPER)):
        corpo = anello(cx, cy, r, col, 3.2) + f'<path d="{path}" fill="{col}" transform="translate({gx:.2f} {base:.2f})"/>'
        open(os.path.join(OUT, nome + '.svg'), 'w').write(svg(w, h, corpo, 'Encore'))
    # solo marchio, quadrato (icona, favicon, profilo social)
    for nome, col, fondo in (('encore-marchio', INK, None), ('encore-marchio-bianco', PAPER, None),
                             ('encore-icona', PAPER, INK)):
        s = 64
        bg = f'<rect width="{s}" height="{s}" fill="{fondo}"/>' if fondo else ''
        rr = 19 if fondo else 24
        open(os.path.join(OUT, nome + '.svg'), 'w').write(svg(s, s, bg + anello(32, 32, rr, col, 3.4 if fondo else 3.6), 'Encore'))
    print('ok', OUT, f'{w:.0f}x{h:.0f}')


if __name__ == '__main__':
    main()
