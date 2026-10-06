# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Gardens Pav in assets/web/ (dalle immagini in assets/originali/).
- foto: a colori, mai più grandi dell'originale, lato lungo al massimo 1600, jpg qualità 84;
  ritaglio solo dove serve un rapporto diverso
- render: ritagliati sul pezzo (soglia sul bianco) con un margine d'aria, ridotti alla misura d'uso;
  dove il render va su una fascia #EBECEB il file viene moltiplicato per quel grigio (il bianco diventa #EBECEB,
  niente riquadri bianchi incollati sul grigio, niente mix-blend-mode nel CSS)
- logo: l'originale per la testata; versione chiara per il piede grafite (il grigio del logo portato a bianco,
  l'arancio resta)
Scrive anche _sorgente/immagini.json con le misure finali e le quote ricalcolate sul ritaglio (le legge contenuti.py).
Uso: python3 prepara_immagini.py
"""
import json
import os

from PIL import Image, ImageChops, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
WEB = os.path.join(ASSET, 'web')
GRIGIO = (0xEB, 0xEC, 0xEB)

# nome web: (sorgente, rapporto o None, larghezza massima in uscita, fuoco x, fuoco y)
FOTO = {
    # home, apertura: 733 x 550 a 1440 (2x), 342 x 257 a 390
    'apertura-vasca-autogru.jpg': ('foto-trasporto-vasca-autogru-cielo.jpg', None, 1466, 0.5, 0.5),
    # home, realizzazioni: 624 x 468 a 1440 (2,05x)
    'realizzazione-altivole-tv.jpg': ('realizzazione-altivole-tv-pozzobon-03.jpg', None, 1280, 0.5, 0.5),
}

# nome web: (sorgente, lato lungo in uscita, fondo, aria in px sull'originale)
RENDER = {
    # home, vasche: mostrato a 600 al massimo (1,45x), su #EBECEB
    'render-vasca-550.jpg': ('render-vasca-rettangolare-550-frontale.jpg', 867, GRIGIO, 20),
    # home, depurazione: riquadri 176 x 120 su bianco (oltre 2x)
    'render-dissabbiatore-400.jpg': ('render-dissabbiatore-frontale.jpg', 400, None, 12),
    'render-separatore-grassi-400.jpg': ('render-separatore-grassi.jpg', 400, None, 12),
    'render-imhoff-400.jpg': ('render-vasca-imhoff.jpg', 400, None, 12),
    'render-separatore-oli-400.jpg': ('render-separatore-oli.jpg', 400, None, 12),
    'render-separatore-oli-autorimesse-400.jpg': ('render-separatore-oli-ombra.jpg', 400, None, 12),
    'render-prima-pioggia-400.jpg': ('render-impianto-prima-pioggia-frontale.jpg', 400, None, 12),
    'render-depuratore-biologico-400.jpg': ('render-depuratore-biologico-frontale.jpg', 400, None, 12),
}

# faccia frontale della vasca 550 nel file originale (pixel x): serve a mettere la quota "550 cm" sotto lo spigolo vero
FACCIA_550 = (476, 1117)


def ritaglia(im, ratio, fx=0.5, fy=0.5):
    if not ratio:
        return im
    rw, rh = map(int, ratio.split(':'))
    w, h = im.size
    target = rw / rh
    nw, nh = (int(h * target), h) if w / h > target else (w, int(w / target))
    x = int(min(max(fx * w - nw / 2, 0), w - nw))
    y = int(min(max(fy * h - nh / 2, 0), h - nh))
    return im.crop((x, y, x + nw, y + nh))


def foto(src, dst, ratio, out_w, fx, fy):
    im = ritaglia(Image.open(src).convert('RGB'), ratio, fx, fy)
    out_w = min(out_w, im.size[0])                    # mai più grande dell'originale
    out_h = round(out_w * im.size[1] / im.size[0])
    if out_w != im.size[0]:
        im = im.resize((out_w, out_h), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return out_w, out_h


def riquadro_pezzo(im, aria):
    g = ImageOps.grayscale(im)
    x0, y0, x1, y1 = ImageOps.invert(g).point(lambda v: 255 if v > 12 else 0).getbbox()
    return (max(0, x0 - aria), max(0, y0 - aria), min(im.size[0], x1 + aria), min(im.size[1], y1 + aria))


def render(src, dst, lato, fondo, aria):
    im = Image.open(src).convert('RGB')
    box = riquadro_pezzo(im, aria)
    im = im.crop(box)
    scala = min(1.0, lato / max(im.size))
    if scala < 1:
        im = im.resize((round(im.size[0] * scala), round(im.size[1] * scala)), Image.LANCZOS)
    if fondo:
        im = ImageChops.multiply(im, Image.new('RGB', im.size, fondo))
    im.save(dst, 'JPEG', quality=85, optimize=True, progressive=True)
    return box, im.size


def logo_chiaro(src, dst):
    """Il grigio del logo (lettere 'opere in calcestruzzo', contorno del marchio) diventa bianco; l'arancio resta."""
    logo = Image.open(src).convert('RGBA')
    px = logo.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            r, g, b, a = px[x, y]
            if a and max(r, g, b) - min(r, g, b) < 48:
                px[x, y] = (255, 255, 255, a)
    logo.save(dst, optimize=True)


def main():
    os.makedirs(WEB, exist_ok=True)
    for f in os.listdir(WEB):
        os.remove(os.path.join(WEB, f))
    misure = {}
    for nome, (src, ratio, w, fx, fy) in FOTO.items():
        misure[nome] = foto(os.path.join(ORIG, src), os.path.join(WEB, nome), ratio, w, fx, fy)
    for nome, (src, lato, fondo, aria) in RENDER.items():
        box, dim = render(os.path.join(ORIG, src), os.path.join(WEB, nome), lato, fondo, aria)
        misure[nome] = dim
        if nome == 'render-vasca-550.jpg':
            larg = box[2] - box[0]
            misure['quota-550'] = [round((FACCIA_550[0] - box[0]) / larg * 100, 2),
                                   round((box[2] - FACCIA_550[1]) / larg * 100, 2)]
    Image.open(os.path.join(ORIG, 'logo-gardens-pav-358x75.png')).save(os.path.join(WEB, 'logo-gardens-pav.png'), optimize=True)
    logo_chiaro(os.path.join(ORIG, 'logo-gardens-pav-358x75.png'), os.path.join(WEB, 'logo-gardens-pav-chiaro.png'))
    misure['logo-gardens-pav.png'] = misure['logo-gardens-pav-chiaro.png'] = [358, 75]
    with open(os.path.join(QUI, 'immagini.json'), 'w', encoding='utf-8') as f:
        json.dump(misure, f, indent=1)
    for nome in sorted(misure):
        print(nome, misure[nome])
    print(len(os.listdir(WEB)), 'immagini in', WEB)


if __name__ == '__main__':
    main()
