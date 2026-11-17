#!/usr/bin/env python3
"""Villa Eidos: dalle foto originali del cliente (assets/originali/, fuori da git) alle versioni web (assets/web/foto/).

Uso:  python3 -I VillaEidos-Sito/_sorgente/immagini.py
Serve Pillow. Il fregio d'apertura si rende prima con node _sorgente/fregio/fregio.mjs <cartella>: se in
assets/web/fregio/ ci sono fregio-largo.png e fregio-alto.png, li converte anche loro.

Le foto sono piccole (640 x 480 dal telefono, una 1600 x 1200): si tengono alla loro misura vera, nessun
ingrandimento, e il sito le mostra al massimo a 1,25 volte (in CSS). Un trattamento solo per tutte:
- bilanciamento del bianco a meta' strada verso il grigio medio (toglie le dominanti diverse dei due telefoni);
- saturazione all'88 %, un filo di calore, contrasto morbido;
- nitidezza leggera alla misura vera e una grana fine uguale per tutte, che tiene insieme le foto.

Ritagli:
- sale riunioni: via la scritta della fotocamera "HONOR 400" in basso a sinistra e la parte del murale
  con il casco (il simbolo disegnato sul casco non serve a una pagina d'affari): 1080 x 810 dal punto 500, 170;
- uffici: via il cestino giallo e lo scatolone a destra: 480 x 360 dal punto 10, 60;
- sale d'attesa: raddrizzata secondo l'EXIF (orientamento 6), intera.
"""
import pathlib
import random

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps

RADICE = pathlib.Path(__file__).resolve().parent.parent
ORIG = RADICE / "assets" / "originali"
WEB = RADICE / "assets" / "web" / "foto"
FREGIO = RADICE / "assets" / "web" / "fregio"

FOTO = [
    # chiave, file originale, ritaglio (x, y, larghezza, altezza) o None, larghezze da scrivere (la prima e' la misura vera)
    ("sale-riunioni", "sale riunioni.jpg", (500, 170, 1080, 810), [1080, 760, 540]),
    ("sala-conferenze", "sala conferenze.jpeg", None, [640, 480]),
    ("reception", "reception.jpeg", None, [640, 480]),
    ("sale-attesa", "sale d'attesa.jpeg", None, [480, 360]),
    ("uffici", "uffici.jpeg", (10, 60, 480, 360), [480, 360]),
]
FREGI = [("apertura-fregio", "fregio-largo.png", [3200, 2400, 1600]), ("apertura-fregio-tel", "fregio-alto.png", [1080, 720])]


def tratta(im, seme):
    im = im.convert("RGB")
    # bilanciamento del bianco: ogni canale va a meta' strada verso la media dei tre
    medie = [sum(c.histogram()[i] * i for i in range(256)) / max(1, sum(c.histogram())) for c in im.split()]
    m = sum(medie) / 3
    canali = []
    for c, mc in zip(im.split(), medie):
        k = 1 + 0.5 * (m / mc - 1)
        canali.append(c.point(lambda v, k=k: max(0, min(255, round(v * k)))))
    im = Image.merge("RGB", canali)
    im = ImageEnhance.Color(im).enhance(0.88)
    # un filo di calore e un contrasto morbido (curva a S leggera)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, round(v * 1.015)))
    b = b.point(lambda v: round(v * 0.985))
    im = Image.merge("RGB", (r, g, b))
    im = im.point(lambda v: max(0, min(255, round(128 + (v - 128) * 1.04 + 2))))
    im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=35, threshold=2))
    # grana fine, monocroma, uguale per tutte le foto
    rnd = random.Random(seme)
    w, h = im.size
    rumore = Image.new("L", (w, h))
    rumore.putdata([max(0, min(255, round(rnd.gauss(128, 3.2)))) for _ in range(w * h)])
    grana = Image.merge("RGB", (rumore, rumore, rumore))
    return ImageChops.add(im, grana, scale=1.0, offset=-128)


def salva(im, chiave, larghezze, dove, qualita=77):
    dove.mkdir(parents=True, exist_ok=True)
    fatti = []
    for lw in larghezze:
        x = im if lw == im.width else im.resize((lw, round(im.height * lw / im.width)), Image.LANCZOS)
        f = dove / f"{chiave}-{lw}.webp"
        x.save(f, "WEBP", quality=qualita, method=6)
        fatti.append((f.name, x.size, f.stat().st_size))
    return fatti


def prepara():
    for chiave, nome, taglio, larghezze in FOTO:
        im = ImageOps.exif_transpose(Image.open(ORIG / nome))
        if taglio:
            x, y, w, h = taglio
            im = im.crop((x, y, x + w, y + h))
        assert im.width == larghezze[0], (chiave, im.size)
        for n, dim, peso in salva(tratta(im, chiave), chiave, larghezze, WEB):
            print(f"{n:28} {dim[0]}x{dim[1]} {peso // 1024} KB")
    for chiave, nome, larghezze in FREGI:
        f = FREGIO / nome
        if not f.exists():
            print("manca", f, "(rendilo con _sorgente/fregio/fregio.mjs)")
            continue
        im = Image.open(f).convert("RGB")
        for n, dim, peso in salva(im, chiave, larghezze, FREGIO, qualita=86):
            print(f"{n:28} {dim[0]}x{dim[1]} {peso // 1024} KB")


def mancano():
    return not all((WEB / f"{k}-{l[0]}.webp").exists() for k, _, _, l in FOTO)


if __name__ == "__main__":
    prepara()
