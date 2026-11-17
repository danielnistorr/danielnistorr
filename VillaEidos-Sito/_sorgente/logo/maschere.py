#!/usr/bin/env python3
"""Logo di Villa Eidos: dall'originale CMYK (assets/originali/Villa Eidos.jpg, 2010x2184, profilo Coated FOGRA39)
alle due maschere da vettorializzare (verde e verde acqua) e al PNG sRGB di controllo.

Uso:  python3 -I VillaEidos-Sito/_sorgente/logo/maschere.py <cartella di lavoro>
Poi:  node VillaEidos-Sito/_sorgente/logo/traccia.mjs <cartella di lavoro>   (potrace, vedi traccia.mjs)

I due inchiostri del logo, letti nel file: verde C74 M23 Y88 K7, verde acqua C61 M0 Y24 K0.
Convertiti in sRGB con il profilo incorporato (intento colorimetrico relativo con compensazione del nero,
come "Converti in profilo" di Photoshop): verde #508E4C, verde acqua #63C2CA.
"""
import io
import pathlib
import sys

from PIL import Image, ImageCms

RADICE = pathlib.Path(__file__).resolve().parents[2]
ORIGINALE = RADICE / "assets" / "originali" / "Villa Eidos.jpg"
VERDE_CMYK = (189, 59, 224, 18)
ACQUA_CMYK = (156, 0, 61, 0)


def main(lavoro):
    lavoro = pathlib.Path(lavoro)
    lavoro.mkdir(parents=True, exist_ok=True)
    im = Image.open(ORIGINALE)
    assert im.mode == "CMYK", im.mode
    ingresso = ImageCms.ImageCmsProfile(io.BytesIO(im.info["icc_profile"]))
    srgb = ImageCms.createProfile("sRGB")
    flag = ImageCms.Flags.BLACKPOINTCOMPENSATION if hasattr(ImageCms, "Flags") else 0x2000
    t = ImageCms.buildTransform(ingresso, srgb, "CMYK", "RGB", renderingIntent=1, flags=flag)
    ImageCms.applyTransform(im, t).save(lavoro / "logo-srgb.png")
    campioni = Image.new("CMYK", (2, 1))
    campioni.putpixel((0, 0), VERDE_CMYK)
    campioni.putpixel((1, 0), ACQUA_CMYK)
    c = ImageCms.applyTransform(campioni, t)
    print("verde #%02X%02X%02X" % c.getpixel((0, 0)), " verde acqua #%02X%02X%02X" % c.getpixel((1, 0)))

    # copertura di ciascun inchiostro: il giallo dice quanto verde c'e' (l'acqua ne ha poco),
    # il ciano che resta tolto quello del verde dice quanto verde acqua
    C, M, Y, K = [b.load() for b in im.split()]
    w, h = im.size
    verde = Image.new("L", (w, h), 255)
    acqua = Image.new("L", (w, h), 255)
    pv, pa = verde.load(), acqua.load()
    for y in range(h):
        for x in range(w):
            g = min(1.0, Y[x, y] / VERDE_CMYK[2])
            a = max(0.0, min(1.0, C[x, y] / ACQUA_CMYK[0] - g * VERDE_CMYK[0] / ACQUA_CMYK[0]))
            pv[x, y] = round(255 * (1 - g))
            pa[x, y] = round(255 * (1 - a))
    verde.save(lavoro / "maschera-verde.png")
    acqua.save(lavoro / "maschera-acqua.png")
    print("maschere in", lavoro)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "logo-lavoro")
