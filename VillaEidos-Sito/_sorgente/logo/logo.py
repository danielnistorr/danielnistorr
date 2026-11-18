#!/usr/bin/env python3
"""Compone i file del logo di Villa Eidos dai tracciati di traccia.mjs.

Uso:  python3 -I VillaEidos-Sito/_sorgente/logo/logo.py <cartella di lavoro>
Esce in assets/web/logo/:
  villaeidos-logo.svg         il logo intero, com'e' nell'originale (marchio sopra, scritta sotto)
  villaeidos-orizzontale.svg  marchio a sinistra e scritta a destra, per la testata (stessi tracciati, solo accostati)
  villaeidos-marchio.svg      solo il marchio (cerchio, albero, foglie): icona del sito
  villaeidos-logo-bianco.svg  il logo intero in bianco, per i fondi scuri
I colori sono quelli dell'originale convertiti in sRGB con il suo profilo (vedi maschere.py).
Poi i file si alleggeriscono con SVGO 3 (un decimale, la forma non cambia a vista):
  npx svgo -q -p 1 VillaEidos-Sito/assets/web/logo/*.svg
"""
import json
import pathlib
import re
import sys

RADICE = pathlib.Path(__file__).resolve().parents[2]
USCITA = RADICE / "assets" / "web" / "logo"
VERDE = "#4A8C46"
ACQUA = "#5EC1C9"
TAGLIO_SCRITTA = 1800  # sotto questa riga (in pixel dell'originale) c'e' solo la scritta "villa EIDOS"


def sottotracciati(d):
    pezzi = [p.strip() for p in re.split(r"(?=M )", d) if p.strip()]
    fuori = []
    for p in pezzi:
        n = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", p)]
        xs, ys = n[0::2], n[1::2]
        fuori.append({"d": p, "x0": min(xs), "x1": max(xs), "y0": min(ys), "y1": max(ys)})
    return fuori


def scatola(parti):
    return (min(p["x0"] for p in parti), min(p["y0"] for p in parti), max(p["x1"] for p in parti), max(p["y1"] for p in parti))


def arrotonda(d, dx=0.0, dy=0.0, k=1.0):
    """Coordinate spostate, scalate e arrotondate a un decimale (il file pesa meno, la forma non cambia)."""
    numeri = iter(range(10 ** 9))

    def r(m):
        i = next(numeri)
        v = float(m.group(0))
        v = (v + (dx if i % 2 == 0 else dy)) * k
        s = f"{v:.1f}".rstrip("0").rstrip(".")
        return s if s != "-0" else "0"

    return re.sub(r"-?\d+(?:\.\d+)?", r, d)


def svg(larghezza, altezza, gruppi, titolo):
    corpo = "".join(f'<path fill="{colore}" fill-rule="evenodd" d="{d}"/>' for colore, d in gruppi if d)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {larghezza:.0f} {altezza:.0f}" role="img" aria-label="{titolo}">'
            f"<title>{titolo}</title>{corpo}</svg>\n")


def main(lavoro):
    t = json.loads((pathlib.Path(lavoro) / "tracciati.json").read_text())
    verde = sottotracciati(t["verde"])
    acqua = sottotracciati(t["acqua"])
    tutti = verde + acqua
    marchio = [p for p in tutti if p["y0"] < TAGLIO_SCRITTA]
    scritta = [p for p in tutti if p["y0"] >= TAGLIO_SCRITTA]
    USCITA.mkdir(parents=True, exist_ok=True)

    def gruppi(parti, dx, dy, k=1.0, bianco=False):
        v = " ".join(arrotonda(p["d"], dx, dy, k) for p in parti if p in verde)
        a = " ".join(arrotonda(p["d"], dx, dy, k) for p in parti if p in acqua)
        if bianco:
            return [("#FFFFFF", (v + " " + a).strip())]
        return [(VERDE, v), (ACQUA, a)]

    m = 8  # margine
    x0, y0, x1, y1 = scatola(tutti)
    w, h = x1 - x0 + 2 * m, y1 - y0 + 2 * m
    (USCITA / "villaeidos-logo.svg").write_text(svg(w, h, gruppi(tutti, m - x0, m - y0), "Villa Eidos"))
    (USCITA / "villaeidos-logo-bianco.svg").write_text(svg(w, h, gruppi(tutti, m - x0, m - y0, bianco=True), "Villa Eidos"))

    mx0, my0, mx1, my1 = scatola(marchio)
    mw, mh = mx1 - mx0 + 2 * m, my1 - my0 + 2 * m
    (USCITA / "villaeidos-marchio.svg").write_text(svg(mw, mh, gruppi(marchio, m - mx0, m - my0), "Villa Eidos"))

    # orizzontale: la scritta alta il 30 % del marchio, centrata sul suo asse, a distanza di mezza altezza di scritta
    sx0, sy0, sx1, sy1 = scatola(scritta)
    sw, sh = sx1 - sx0, sy1 - sy0
    k = 0.30 * (my1 - my0) / sh
    spazio = 0.62 * sh * k
    W = (mx1 - mx0) + spazio + sw * k + 2 * m
    H = (my1 - my0) + 2 * m
    g = gruppi(marchio, m - mx0, m - my0)
    dy = (H - sh * k) / 2 / k - sy0
    dx = (m + (mx1 - mx0) + spazio) / k - sx0
    gs = gruppi(scritta, dx, dy, k)
    (USCITA / "villaeidos-orizzontale.svg").write_text(svg(W, H, [(c, a + " " + b) for (c, a), (_, b) in zip(g, gs)], "Villa Eidos"))
    for f in sorted(USCITA.glob("*.svg")):
        print(f.name, f.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "logo-lavoro")
