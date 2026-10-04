# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito in assets/web/ (direzione "Atelier").
- foto di sede e magazzino: monocromia calda grafite a tre punti, grana leggera, ritagli da "tavola" (21:9, 4:3, 3:2, 4:5, 1:1);
  mai ingrandite oltre 2x i pixel reali
- foto prodotto: stesso tono grafite, fondo portato esattamente al colore della tessera (avorio), oggetto centrato
- logo: originale per la testata e versione avorio per il footer scuro; loghi dei marchi invariati
Uso: python3 prepara_immagini.py
"""
import json
import os

from PIL import Image, ImageChops, ImageEnhance, ImageFilter, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
EST = os.path.join(ASSET, 'esterne')
WEB = os.path.join(ASSET, 'web')

# toni della foto (non usati nell'interfaccia): ombre, medi, luci
OMBRE, MEDI, LUCI = '#1F1C1A', '#827A71', '#EDE7DE'
TESSERA = '#FBF8F3'          # avorio: fondo delle tessere prodotto
LOGO_FOOTER = '#EDE7DE'      # logo sul footer scuro

FACCIATA = os.path.join(EST, 'google-business-proprietario-01.jpg')
SLIDE = {
    'rotoli': 'home-slider-articoli-collanti-per-calzature-e-pelletterie-padova-venezia-2-45-38.jpg',
    'lastre': 'home-slider-articoli-collanti-per-calzature-e-pelletterie-padova-venezia-3-37-39.jpg',
    'tacchi': 'home-slider-articoli-per-calzature-padova-venezia-40-41.jpg',
    'colle': 'home-slider-benvegnu-articoli-per-calzature-e-pelletterie-vigonovo-venezia-32-47.jpg',
    'corsia': 'home-slider-ingrosso-articoli-per-pelletteria-calzature-padova-venezia-benvegnu-29-51.jpg',
    'solette': 'home-slider-solette-calzature-padova-venezia-vibram-46-54.jpg',
    'banco': 'home-slider-solette-vibram-suole-benvegu-26.jpg',
    'espositore': 'home-slider-suole-scarpe-ginnastica-vibram-benvegnu-padova-venezia-25.jpg',
}

# nome web: (sorgente, rapporto, larghezza in uscita, fuoco x, fuoco y)
TAVOLE = {
    'sede-21x9.jpg': (FACCIATA, '21:9', 2048, 0.50, 0.36),
    'sede-4x3.jpg': (FACCIATA, '4:3', 1200, 0.62, 0.50),
    'sede-3x2.jpg': (FACCIATA, '3:2', 1600, 0.55, 0.50),
    'sede-4x5.jpg': (FACCIATA, '4:5', 1088, 0.78, 0.50),
    'rotoli-4x5.jpg': (SLIDE['rotoli'], '4:5', 752, 0.55, 0.50),
    'banco-3x2.jpg': (SLIDE['banco'], '3:2', 1120, 0.50, 0.50),
    'espositore-4x5.jpg': (SLIDE['espositore'], '4:5', 752, 0.60, 0.50),
    'corsia-4x5.jpg': (SLIDE['corsia'], '4:5', 752, 0.50, 0.50),
    'colle-4x5.jpg': (SLIDE['colle'], '4:5', 752, 0.75, 0.50),
    'lastre-3x2.jpg': (SLIDE['lastre'], '3:2', 1120, 0.50, 0.50),
    'tacchi-1x1.jpg': (SLIDE['tacchi'], '1:1', 940, 0.50, 0.50),
    'solette-1x1.jpg': (SLIDE['solette'], '1:1', 940, 0.50, 0.50),
}

# articoli scelti dal catalogo per rappresentare famiglie e modelli (productid del sito attuale)
PRODOTTI = [
    '1895', '9978', '14932', '2031', '8843', '1828',                 # utensili
    '80075', '85109', '83169', '82768', '83137', '85014',            # suole Vibram
    '82268', '84413', '84952', '84305',                              # lastre Vibram
    '83255', '80751', '83566', '83263',                              # mezzesuole e tacchi Vibram
    '1075', '15887', '1030', '9266', '10275',                        # filati ed elastici
    '14563', '1802', '1795',                                         # modelleria e riparazione
    '15752', '10572', '7995',                                        # esposizione e cura
    '9907', '15947',                                                 # igiene e sicurezza
    '2055', '15531',                                                 # imballaggio
]


def ritaglia(im, rw, rh, fx=0.5, fy=0.5):
    w, h = im.size
    target = rw / rh
    nw, nh = (int(h * target), h) if w / h > target else (w, int(w / target))
    x = int(min(max(fx * w - nw / 2, 0), w - nw))
    y = int(min(max(fy * h - nh / 2, 0), h - nh))
    return im.crop((x, y, x + nw, y + nh))


def tono(src, dst, out_w, ratio, fx=0.5, fy=0.5, grana=7):
    rw, rh = map(int, ratio.split(':'))
    im = ritaglia(Image.open(src).convert('RGB'), rw, rh, fx, fy)
    out_w = min(out_w, im.size[0] * 2)                 # mai oltre 2x i pixel reali
    out_h = round(out_w * rh / rw)
    up = out_w > im.size[0]
    im = im.resize((out_w, out_h), Image.LANCZOS)
    if up:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=45, threshold=3))
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=(1, 0.5))
    g = ImageEnhance.Contrast(g).enhance(1.06)
    g = g.point(lambda v: round(255 * (v / 255) ** 1.04))
    col = ImageOps.colorize(g, black=OMBRE, mid=MEDI, white=LUCI, midpoint=118)
    n = Image.effect_noise((out_w, out_h), grana if up else grana * 0.7).filter(ImageFilter.GaussianBlur(0.5))
    col = ImageChops.add(col, Image.merge('RGB', (n, n, n)), scale=1.0, offset=-128)
    col.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return col.size


def prodotto(src, dst, lato=600):
    im = Image.open(src).convert('RGB')
    g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=(0.5, 0))
    g = ImageEnhance.Contrast(g).enhance(1.04)
    col = ImageOps.colorize(g, black=OMBRE, mid=MEDI, white=TESSERA, midpoint=120)
    bbox = ImageOps.invert(g).point(lambda v: 255 if v > 12 else 0).getbbox() or (0, 0) + im.size
    obj = col.crop(bbox)
    lim = int(lato * 0.76)
    scala = min(lim / obj.size[0], lim / obj.size[1])
    if max(im.size) <= 400:
        scala = min(scala, 1.5)       # le foto Vibram sono 400x400: ingrandimento contenuto
    obj = obj.resize((max(1, int(obj.size[0] * scala)), max(1, int(obj.size[1] * scala))), Image.LANCZOS)
    out = Image.new('RGB', (lato, lato), TESSERA)
    out.paste(obj, ((lato - obj.size[0]) // 2, (lato - obj.size[1]) // 2))
    out.save(dst, 'JPEG', quality=86, optimize=True, progressive=True)


def logo_colore(src, dst, colore):
    logo = Image.open(src).convert('RGBA')
    r, g, b = Image.new('RGB', (1, 1), colore).getpixel((0, 0))
    out = Image.new('RGBA', logo.size, (r, g, b, 0))
    out.putalpha(logo.getchannel('A'))
    px = out.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            px[x, y] = (r, g, b, px[x, y][3])
    out.save(dst, optimize=True)


def main():
    os.makedirs(WEB, exist_ok=True)
    # via le immagini della versione precedente: restano solo quelle usate
    for f in os.listdir(WEB):
        os.remove(os.path.join(WEB, f))
    for nome, (src, ratio, w, fx, fy) in TAVOLE.items():
        src = src if os.path.isabs(src) else os.path.join(ORIG, src)
        print(nome, tono(src, os.path.join(WEB, nome), w, ratio, fx, fy))
    catalogo = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
    per_id = {a['id']: a['foto'] for f in catalogo['famiglie'] for s in f['sottocategorie'] for a in s['articoli'] if a['foto']}
    for pid in PRODOTTI:
        prodotto(os.path.join(ORIG, per_id[pid]), os.path.join(WEB, f'prodotto-{pid}.jpg'))
    Image.open(os.path.join(ORIG, 'logo-benvegnu.png')).save(os.path.join(WEB, 'logo-benvegnu.png'), optimize=True)
    logo_colore(os.path.join(ORIG, 'logo-benvegnu.png'), os.path.join(WEB, 'logo-benvegnu-avorio.png'), LOGO_FOOTER)
    for m in ('vibram', 'gutermann', 'girba', 'fratelli-zucchini'):
        Image.open(os.path.join(ORIG, f'marchio-{m}.png')).save(os.path.join(WEB, f'marchio-{m}.png'), optimize=True)
    print(len(os.listdir(WEB)), 'immagini in', WEB)


if __name__ == '__main__':
    main()
