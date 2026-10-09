# -*- coding: utf-8 -*-
"""Scarica le foto scelte da Pexels (CDN pubblico), le ritaglia e le salva in WebP in assets/web/ in due o tre larghezze."""
import io
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from PIL import Image, ImageEnhance

QUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(QUI), 'assets', 'web')

# nome: (id Pexels, rapporto larghezza/altezza del ritaglio o None, saturazione, larghezze, qualità[, ancoraggio del ritaglio])
FOTO = {
    'hero-knitwear':   (5475173, 4 / 5, 1.0, (800, 1400), 72),
    'problem-rail':    (5706275, 4 / 5, 0.35, (800, 1400), 70, 'basso'),
    'solution-wool':   (6757412, 4 / 5, 0.9, (800, 1400), 58),
    'how-yarn-cones':  (2973400, 4 / 5, 0.45, (800, 1400), 70),
    'result-knit':     (7760243, 16 / 9, 0.9, (900, 1600, 2400), 70),
    'cta-wool-macro':  (7794331, 4 / 5, 0.9, (800, 1400), 70),
    'hero-wide':       (5475173, 16 / 9, 0.85, (900, 1600, 2400), 68),
    'solution-wide':   (6757412, 16 / 7, 0.85, (900, 1600, 2400), 58),
}


def scarica(pid):
    url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=2600'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=60).read())).convert('RGB')


def ritaglia(im, r, ancora='centro'):
    w, h = im.size
    if w / h > r:
        nw = int(h * r)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(w / r)
    y = (h - nh) if ancora == 'basso' else (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def prepara(item):
    nome, (pid, r, sat, larghezze, q, *resto) = item
    im = scarica(pid)
    if r:
        im = ritaglia(im, r, *resto)
    if sat != 1.0:
        im = ImageEnhance.Color(im).enhance(sat)
    out = []
    for w in larghezze:
        if w > im.width:
            continue
        x = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        fn = f'{nome}-{w}.webp'
        x.save(os.path.join(OUT, fn), 'WEBP', quality=q, method=6)
        out.append((fn, x.size, os.path.getsize(os.path.join(OUT, fn)) // 1024))
    return nome, im.size, out


if __name__ == '__main__':
    import sys
    os.makedirs(OUT, exist_ok=True)
    scelte = {k: v for k, v in FOTO.items() if not sys.argv[1:] or k in sys.argv[1:]}
    with ThreadPoolExecutor(6) as ex:
        for nome, size, out in ex.map(prepara, scelte.items()):
            print(nome, size, out)
