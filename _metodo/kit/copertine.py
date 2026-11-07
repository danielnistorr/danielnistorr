# uso: python3 copertine.py <out.jpg> <Cartella-Sito> [<Cartella-Sito> ...] [--colonne 3] [--larghezza 720]
# Mette in griglia le prime schermate a 1440 (screenshot/home/home-1440-prima-schermata.jpg) con il nome sotto.
import argparse, os
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = argparse.ArgumentParser()
p.add_argument('out')
p.add_argument('cartelle', nargs='+')
p.add_argument('--colonne', type=int, default=3)
p.add_argument('--larghezza', type=int, default=720)
a = p.parse_args()

W = a.larghezza
H = W * 900 // 1440
ETI, M = 44, 24
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 20)
except OSError:
    font = ImageFont.load_default()

voci = []
for c in a.cartelle:
    f = os.path.join(REPO, c, 'screenshot/home/home-1440-prima-schermata.jpg')
    if os.path.exists(f):
        voci.append((c.removesuffix('-Sito'), f))
    else:
        print(f'manca: {f}')
righe = (len(voci) + a.colonne - 1) // a.colonne
foglio = Image.new('RGB', (M + a.colonne * (W + M), M + righe * (H + ETI + M)), (236, 234, 229))
d = ImageDraw.Draw(foglio)
for i, (nome, f) in enumerate(voci):
    x = M + (i % a.colonne) * (W + M)
    y = M + (i // a.colonne) * (H + ETI + M)
    im = Image.open(f).convert('RGB').resize((W, H), Image.LANCZOS)
    foglio.paste(im, (x, y))
    d.rectangle([x, y, x + W - 1, y + H - 1], outline=(200, 197, 190))
    d.text((x, y + H + 12), nome, fill=(30, 30, 30), font=font)
foglio.save(a.out, quality=86)
print(a.out, foglio.size)
