# uso: python3 prima-dopo.py <out.jpg> [--pro] <Cartella-Sito> [<Cartella-Sito> ...]
# --prima <sottocartella>: confronta con quella (per esempio _prova/versione-pro/screenshot/home)
# --pro: prima = _prova/versione-1-originale/screenshot/home, dopo = screenshot/home (livello professionale)
# Per ogni azienda una riga: prima schermata a 1440 e a 390 della home attuale (screenshot/home/)
# accanto a quelle della versione 2 (screenshot/home-v2/).
import os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
argv = sys.argv[1:]
PRIMA = None
if '--prima' in argv:
    i = argv.index('--prima'); PRIMA = argv[i + 1]; del argv[i:i + 2]
out, cartelle = argv[0], [c for c in argv[1:] if c != '--pro']
PRO = '--pro' in sys.argv
COPPIE = [(PRIMA, 'prima'), ('screenshot/home', 'dopo')] if PRIMA else [('_prova/versione-1-originale/screenshot/home', 'prima'), ('screenshot/home', 'dopo')] if PRO else [('screenshot/home', 'prima'), ('screenshot/home-v2', 'dopo')]
WD, HD = 720, 450          # 1440x900 a metà
WM, HM = 208, 450          # 390x844 alla stessa altezza
M, ETI = 24, 40
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
    piccolo = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
except OSError:
    font = piccolo = ImageFont.load_default()

larg = M + 2 * (WD + M + WM + M) + M
alt = M + len(cartelle) * (ETI + HD + M)
foglio = Image.new('RGB', (larg, alt), (236, 234, 229))
d = ImageDraw.Draw(foglio)
for r, c in enumerate(cartelle):
    y = M + r * (ETI + HD + M)
    for k, (sotto, titolo) in enumerate(COPPIE):
        x = M + k * (WD + M + WM + M + M)
        d.text((x, y + 8), f"{c.removesuffix('-Sito')}, {titolo}", fill=(30, 30, 30), font=font)
        for f, w, h, dx in [('home-1440-prima-schermata.jpg', WD, HD, 0), ('home-390-prima-schermata.jpg', WM, HM, WD + M)]:
            p = os.path.join(REPO, c, sotto, f)
            if not os.path.exists(p):  # alcune copie hanno la cartella screenshot-home
                p = os.path.join(REPO, c, sotto.replace('screenshot/home', 'screenshot-home'), f)
            if not os.path.exists(p):
                d.text((x + dx, y + ETI + 10), 'manca', fill=(160, 0, 0), font=piccolo)
                continue
            im = Image.open(p).convert('RGB')
            im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).crop((0, 0, w, h))
            foglio.paste(im, (x + dx, y + ETI))
            d.rectangle([x + dx, y + ETI, x + dx + w - 1, y + ETI + h - 1], outline=(200, 197, 190))
foglio.save(out, quality=86)
print(out, foglio.size)
