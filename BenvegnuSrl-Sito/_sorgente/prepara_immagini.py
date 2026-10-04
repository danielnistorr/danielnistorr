# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito in assets/web/ partendo da assets/originali/ e assets/esterne/.
- foto di sede e magazzino: bianco e nero con contrasto deciso (così il bancone arancione,
  il verde delle vetrate e le scatole colorate non escono dalla palette bianco/nero/rosso)
- foto prodotto: restano a colori (il colore di un filo o di una suola è informazione), 600x600 su bianco
- logo: versione originale e versione bianca per il footer nero
Uso: python3 prepara_immagini.py
"""
import json
import os

from PIL import Image, ImageEnhance, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
EST = os.path.join(ASSET, 'esterne')
WEB = os.path.join(ASSET, 'web')

FOTO_BN = {
    # nome web: (file sorgente, ritaglio (sinistra, alto, destra, basso) in frazioni, larghezza finale)
    'sede-esterno.jpg': (os.path.join(EST, 'google-business-proprietario-01.jpg'), (0.0, 0.17, 1.0, 0.70), 1800),
    'sede-esterno-verticale.jpg': (os.path.join(EST, 'google-business-proprietario-01.jpg'), (0.52, 0.10, 0.99, 0.72), 900),
    'magazzino-rotoli.jpg': (os.path.join(ORIG, 'home-slider-articoli-collanti-per-calzature-e-pelletterie-padova-venezia-2-45-38.jpg'), None, 750),
    'magazzino-lastre.jpg': (os.path.join(ORIG, 'home-slider-articoli-collanti-per-calzature-e-pelletterie-padova-venezia-3-37-39.jpg'), None, 750),
    'magazzino-tacchi.jpg': (os.path.join(ORIG, 'home-slider-articoli-per-calzature-padova-venezia-40-41.jpg'), None, 750),
    'magazzino-colle-abrasivi.jpg': (os.path.join(ORIG, 'home-slider-benvegnu-articoli-per-calzature-e-pelletterie-vigonovo-venezia-32-47.jpg'), None, 750),
    'magazzino-corsia.jpg': (os.path.join(ORIG, 'home-slider-ingrosso-articoli-per-pelletteria-calzature-padova-venezia-benvegnu-29-51.jpg'), None, 750),
    'magazzino-solette-cura.jpg': (os.path.join(ORIG, 'home-slider-solette-calzature-padova-venezia-vibram-46-54.jpg'), None, 750),
    'banco-suole-vibram.jpg': (os.path.join(ORIG, 'home-slider-solette-vibram-suole-benvegu-26.jpg'), None, 750),
    'banco-espositore-vibram.jpg': (os.path.join(ORIG, 'home-slider-suole-scarpe-ginnastica-vibram-benvegnu-padova-venezia-25.jpg'), None, 750),
}

# articoli scelti dal catalogo per rappresentare le famiglie (productid del sito attuale)
PRODOTTI = [
    '1895', '9978', '14932', '2031', '8843', '1828',                 # utensili
    '80075', '85109', '83169', '82768', '83137', '85014',            # suole Vibram
    '82268', '84413', '84952', '84305',                              # lastre Vibram
    '83255', '80751', '83566', '83263',                              # mezzesuole e tacchi Vibram
    '1075', '15887', '1030', '9266', '10275',                                 # filati ed elastici
    '14563', '1802', '1795',                                         # modelleria e riparazione
    '15752', '10572', '7995',                                        # esposizione e cura
    '9907', '15947',                                                 # igiene e sicurezza
    '2055', '15531',                                                 # imballaggio
]


def bianco_nero(im):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    # curva a S leggera: neri più profondi, luci pulite
    lut = []
    for i in range(256):
        x = i / 255.0
        y = x * x * (3 - 2 * x)          # smoothstep
        y = 0.65 * y + 0.35 * x
        lut.append(int(round(y * 255)))
    g = g.point(lut)
    g = ImageEnhance.Sharpness(g).enhance(1.15)
    return g.convert('RGB')


def main():
    os.makedirs(WEB, exist_ok=True)
    log = []
    for nome, (src, crop, w) in FOTO_BN.items():
        im = Image.open(src).convert('RGB')
        if crop:
            W, H = im.size
            im = im.crop((int(crop[0] * W), int(crop[1] * H), int(crop[2] * W), int(crop[3] * H)))
        if im.size[0] > w:
            im = im.resize((w, int(im.size[1] * w / im.size[0])), Image.LANCZOS)
        bianco_nero(im).save(os.path.join(WEB, nome), quality=84, optimize=True, progressive=True)
        log.append((nome, im.size))

    catalogo = json.load(open(os.path.join(QUI, 'catalogo.json'), encoding='utf-8'))
    per_id = {a['id']: a['foto'] for f in catalogo['famiglie'] for s in f['sottocategorie'] for a in s['articoli'] if a['foto']}
    for pid in PRODOTTI:
        src = os.path.join(ORIG, per_id[pid])
        im = Image.open(src).convert('RGB')
        im.thumbnail((600, 600), Image.LANCZOS)
        tela = Image.new('RGB', (600, 600), 'white')
        tela.paste(im, ((600 - im.size[0]) // 2, (600 - im.size[1]) // 2))
        tela.save(os.path.join(WEB, f'prodotto-{pid}.jpg'), quality=85, optimize=True, progressive=True)
        log.append((f'prodotto-{pid}.jpg', (600, 600)))

    # loghi: originale, e versione bianca dal canale alfa per il footer nero
    logo = Image.open(os.path.join(ORIG, 'logo-benvegnu.png')).convert('RGBA')
    logo.save(os.path.join(WEB, 'logo-benvegnu.png'), optimize=True)
    bianco = Image.new('RGBA', logo.size, (255, 255, 255, 0))
    bianco.putalpha(logo.getchannel('A'))
    pix = bianco.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            a = pix[x, y][3]
            pix[x, y] = (255, 255, 255, a)
    bianco.save(os.path.join(WEB, 'logo-benvegnu-bianco.png'), optimize=True)
    for m in ('vibram', 'gutermann', 'girba', 'fratelli-zucchini'):
        Image.open(os.path.join(ORIG, f'marchio-{m}.png')).save(os.path.join(WEB, f'marchio-{m}.png'), optimize=True)
    for n, s in log:
        print(n, s)
    print('immagini in', WEB)


if __name__ == '__main__':
    main()
