"""Prepara le immagini delle pagine interne in WebP e scrive _sorgente/immagini.json (misure e larghezze).

Fonti (fuori da git, in assets/originali/):
  - le foto del sito di oggi (scaricate da https://dieffepiu.it/image/<id>, 3 novembre 2026);
  - i ritagli delle tavole del catalogo 2023 (assets/originali/catalogo/*.png, pagine rasterizzate a 120 dpi).
Le immagini della home restano quelle di sito/img e vengono solo registrate.
"""
import json
import pathlib

from PIL import Image, ImageChops, ImageOps

RADICE = pathlib.Path(__file__).resolve().parent.parent
ORIG = RADICE / "assets" / "originali"
CAT = ORIG / "catalogo"
OUT = RADICE / "_sorgente" / "img-web"
REG = RADICE / "_sorgente" / "immagini.json"

FOTO = {
    # chiave: (file, larghezze)
    "kit-tank": ("kit-tank.jpg", [640, 960, 1440, 2000]),
    "testate-tubi": ("testate-tubi.jpg", [567]),
    "molla-vite": ("molla-vite.jpg", [567]),
    "molla-testata": ("molla-testata.jpg", [567]),
    "plisse-macro": ("plisse-macro.jpg", [624]),
    "rotoli-macro": ("rotoli-macro.jpg", [624]),
}
# immagini gia' pronte nella cartella della home
DELLA_HOME = {
    "cingolo": (1376, 996, [640, 960, 1376]),
    "testate": (2750, 1430, [900, 1440, 2200, 2750]),
    "rotoli": (1240, 853, [720, 1000, 1240]),
}


def _foto(chiave, file, larghezze, tutte):
    im = Image.open(ORIG / file)
    im = ImageOps.exif_transpose(im).convert("RGB")
    W, H = im.size
    larghezze = [w for w in larghezze if w <= W] or [W]
    for w in larghezze:
        dest = OUT / f"{chiave}-{w}.webp"
        if dest.exists() and not tutte:
            continue
        h = round(H * w / W)
        im.resize((w, h), Image.LANCZOS).save(dest, "WEBP", quality=82, method=6)
    return {"w": W, "h": H, "larghezze": larghezze}


def _tavola(png, tutte):
    chiave = png.stem
    dest = OUT / f"{chiave}.webp"
    im = Image.open(png).convert("RGB")
    # bianco della pagina pulito: cosi' con mix-blend-mode:multiply diventa la carta del sito
    g = im.convert("L")
    maschera = g.point(lambda v: 255 if v >= 238 else 0)
    bianco = Image.new("RGB", im.size, (255, 255, 255))
    im = Image.composite(bianco, im, maschera)
    # rifilo dei margini bianchi, con un po' d'aria
    diff = ImageChops.difference(im, bianco).convert("L").point(lambda v: 255 if v > 12 else 0)
    box = diff.getbbox()
    if box:
        m = 12
        box = (max(0, box[0] - m), max(0, box[1] - m), min(im.width, box[2] + m), min(im.height, box[3] + m))
        im = im.crop(box)
    if tutte or not dest.exists():
        im.save(dest, "WEBP", quality=90, method=6)
    return {"w": im.width, "h": im.height, "larghezze": [im.width], "tavola": True}


def prepara(tutte=False):
    OUT.mkdir(parents=True, exist_ok=True)
    reg = {}
    for k, (f, larg) in FOTO.items():
        if (ORIG / f).exists():
            reg[k] = _foto(k, f, larg, tutte)
    for k, (w, h, larg) in DELLA_HOME.items():
        reg[k] = {"w": w, "h": h, "larghezze": larg}
    if CAT.exists():
        for png in sorted(CAT.glob("*.png")):
            reg[png.stem] = _tavola(png, tutte)
    REG.write_text(json.dumps(reg, indent=1, ensure_ascii=False), encoding="utf-8")
    print(len(reg), "immagini registrate")
    return reg


if __name__ == "__main__":
    import sys
    prepara(tutte="--tutte" in sys.argv)
