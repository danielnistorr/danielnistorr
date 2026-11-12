# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito in assets/web/.
- foto di sede e magazzino: bianco e nero neutro, curva a S leggera (neri profondi, luci pulite), ritagli per l'uso
  (hero a tutta altezza, blocchi foto del catalogo); mai ingrandite oltre 2x i pixel reali
- foto prodotto: a colori (il colore di un filo o di una suola è informazione), 800x800 su bianco, oggetto centrato
- logo: originale per la testata, versione bianca per le parti nere; loghi dei marchi a un solo colore (#111111),
  così stanno con le foto in bianco e nero invece di fare quattro macchie di colore; logo Benvegnù piatto nero per la testata
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

# nome web: (sorgente, rapporto o None per l'intera foto, larghezza in uscita, fuoco x, fuoco y)
FOTO = {
    'sede-hero.jpg': (FACCIATA, '9:10', 1240, 0.70, 0.45),        # metà destra della hero, a tutta altezza
    'sede-hero-mobile.jpg': (FACCIATA, '4:3', 1200, 0.66, 0.42),
    'sede-larga.jpg': (FACCIATA, '21:9', 2048, 0.50, 0.36),
    'blocco-vibram.jpg': (SLIDE['banco'], '4:3', 750, 0.45, 0.55),
    'blocco-utensili.jpg': (SLIDE['colle'], '4:3', 750, 0.62, 0.50),
    'blocco-tomaia.jpg': (SLIDE['rotoli'], '4:3', 750, 0.50, 0.50),
    'blocco-cura.jpg': (SLIDE['solette'], '4:3', 750, 0.60, 0.50),
    'espositore-vibram.jpg': (SLIDE['espositore'], '1:1', 940, 0.50, 0.50),    # tiene intera la scritta 'vibram' a sinistra
    'banco-suole.jpg': (SLIDE['banco'], None, 750, 0.5, 0.5),
    'magazzino-corsia.jpg': (SLIDE['corsia'], None, 750, 0.5, 0.5),
    'magazzino-lastre.jpg': (SLIDE['lastre'], None, 750, 0.5, 0.5),
    'magazzino-tacchi.jpg': (SLIDE['tacchi'], None, 750, 0.5, 0.5),
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


def bianco_nero(im):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=(0.8, 0.4))
    lut = []
    for i in range(256):
        x = i / 255.0
        y = x * x * (3 - 2 * x)          # curva a S leggera
        y = 0.55 * y + 0.45 * x
        lut.append(int(round(y * 255)))
    g = g.point(lut)
    return g.convert('RGB')


def foto(src, dst, ratio, out_w, fx, fy):
    im = ritaglia(Image.open(src).convert('RGB'), ratio, fx, fy)
    out_w = min(out_w, im.size[0] * 2)
    out_h = round(out_w * im.size[1] / im.size[0])
    up = out_w > im.size[0]
    im = im.resize((out_w, out_h), Image.LANCZOS)
    if up:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=40, threshold=3))
    else:
        im = ImageEnhance.Sharpness(im).enhance(1.1)
    bianco_nero(im).save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return out_w, out_h


def prodotto(src, dst, lato=800):
    im = Image.open(src).convert('RGB')
    g = ImageOps.grayscale(im)
    bbox = ImageOps.invert(g).point(lambda v: 255 if v > 14 else 0).getbbox() or (0, 0) + im.size
    obj = im.crop(bbox)
    lim = int(lato * 0.78)
    scala = min(lim / obj.size[0], lim / obj.size[1])
    if max(im.size) <= 400:
        scala = min(scala, 1.6)           # le foto Vibram sono 400x400: ingrandimento contenuto
    obj = obj.resize((max(1, int(obj.size[0] * scala)), max(1, int(obj.size[1] * scala))), Image.LANCZOS)
    out = Image.new('RGB', (lato, lato), 'white')
    out.paste(obj, ((lato - obj.size[0]) // 2, (lato - obj.size[1]) // 2))
    out.save(dst, 'JPEG', quality=86, optimize=True, progressive=True)


def logo_colore(src, dst, colore):
    logo = Image.open(src).convert('RGBA')
    r, g, b = Image.new('RGB', (1, 1), colore).getpixel((0, 0))
    out = Image.new('RGBA', logo.size, (r, g, b, 0))
    a = logo.getchannel('A')
    out.putalpha(a)
    px = out.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            px[x, y] = (r, g, b, px[x, y][3])
    out.save(dst, optimize=True)


def logo_monocolore(src, dst, colore='#111111'):
    """Logo di marchio a un solo colore, come nelle versioni monocromatiche ufficiali: le parti scure restano piene,
    i fondi chiari (l'ottagono giallo Vibram) diventano trasparenti, i colori medi (blu Girba, rosso Zucchini) pieni."""
    logo = Image.open(src).convert('RGBA')
    lum = ImageOps.grayscale(logo.convert('RGB'))
    copertura = lum.point(lambda v: int(max(0.0, min(1.0, (0.85 - v / 255.0) / 0.45)) * 255))
    a = ImageChops.darker(copertura, logo.getchannel('A'))
    r, g, b = Image.new('RGB', (1, 1), colore).getpixel((0, 0))
    out = Image.new('RGBA', logo.size, (r, g, b, 0))
    out.putalpha(a)
    out.save(dst, optimize=True)


def main():
    os.makedirs(WEB, exist_ok=True)
    for f in os.listdir(WEB):
        os.remove(os.path.join(WEB, f))
    for nome, (src, ratio, w, fx, fy) in FOTO.items():
        src = src if os.path.isabs(src) else os.path.join(ORIG, src)
        print(nome, foto(src, os.path.join(WEB, nome), ratio, w, fx, fy))
    catalogo = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
    per_id = {a['id']: a['foto'] for f in catalogo['famiglie'] for s in f['sottocategorie'] for a in s['articoli'] if a['foto']}
    for pid in PRODOTTI:
        prodotto(os.path.join(ORIG, per_id[pid]), os.path.join(WEB, f'prodotto-{pid}.jpg'))
    Image.open(os.path.join(ORIG, 'logo-benvegnu.png')).save(os.path.join(WEB, 'logo-benvegnu.png'), optimize=True)
    logo_colore(os.path.join(ORIG, 'logo-benvegnu.png'), os.path.join(WEB, 'logo-benvegnu-bianco.png'), '#FFFFFF')
    # versione piatta nera per la testata: la sfera sfumata dell'originale stona su un sito tutto piatto
    logo_colore(os.path.join(ORIG, 'logo-benvegnu.png'), os.path.join(WEB, 'logo-benvegnu-nero.png'), '#111111')
    for m in ('vibram', 'gutermann', 'girba', 'fratelli-zucchini'):
        logo_monocolore(os.path.join(ORIG, f'marchio-{m}.png'), os.path.join(WEB, f'marchio-{m}.png'))
    print(len(os.listdir(WEB)), 'immagini in', WEB)


if __name__ == '__main__':
    main()
