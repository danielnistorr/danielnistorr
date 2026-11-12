"""Le immagini della planimetria: dagli originali (assets/originali/planimetria/, fuori da git) alle versioni
compresse in WebP (assets/web/planimetria/, in git), alle misure che servono al sito.

- La foto aerea non si ridisegna e non si ritocca: solo riduzione e compressione (il canale alfa era tutto
  opaco, si toglie senza cambiare nulla). Misure: 981 (quella vera), 760, 560, 400 px di larghezza.
- Le cinque foto del Rustico: grande 1600 (quella vera), media 960, miniatura 200.

Gli originali vengono dal prototipo del committente (planimetria_interattiva1_1.html, immagini in base64).
Si rifanno con: python3 EderaCountry-Sito/_sorgente/immagini.py   (serve Pillow con il supporto WebP)
"""
import pathlib

RADICE = pathlib.Path(__file__).resolve().parent.parent
ORIGINALI = RADICE / "assets" / "originali" / "planimetria"
WEB = RADICE / "assets" / "web" / "planimetria"

AEREA = ("planimetria-aerea.png", "planimetria", (981, 760, 560, 400), 72)
GALLERIA = [(f"rustico-{n}.jpg", f"rustico-{n}") for n in range(1, 6)]
MISURE_GALLERIA = ((1600, 78), (960, 78), (200, 74))


def nomi():
    """I file WebP che il tema si aspetta, in ordine: [(nome base, [file dal piu' grande])]."""
    out = [(AEREA[1], [f"{AEREA[1]}-{w}.webp" for w in AEREA[2]])]
    for _, base in GALLERIA:
        out.append((base, [f"{base}-{w}.webp" for w, _ in MISURE_GALLERIA]))
    return out


def mancano():
    return [f for _, fs in nomi() for f in fs if not (WEB / f).exists()]


def prepara():
    from PIL import Image  # noqa: WPS433 (solo quando servono)
    WEB.mkdir(parents=True, exist_ok=True)
    im = Image.open(ORIGINALI / AEREA[0])
    if im.mode == "RGBA" and im.getchannel("A").getextrema() != (255, 255):
        raise SystemExit("la foto aerea ha zone trasparenti: va controllata prima di toglierne il canale alfa")
    im = im.convert("RGB")
    for w in AEREA[2]:
        r = im if w == im.width else im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        r.save(WEB / f"{AEREA[1]}-{w}.webp", "WEBP", quality=AEREA[3], method=6)
    for nome, base in GALLERIA:
        g = Image.open(ORIGINALI / nome).convert("RGB")
        for w, q in MISURE_GALLERIA:
            r = g if w == g.width else g.resize((w, round(g.height * w / g.width)), Image.LANCZOS)
            r.save(WEB / f"{base}-{w}.webp", "WEBP", quality=q, method=6)


if __name__ == "__main__":
    prepara()
    for _, fs in nomi():
        for f in fs:
            print(f, (WEB / f).stat().st_size // 1024, "KB")
