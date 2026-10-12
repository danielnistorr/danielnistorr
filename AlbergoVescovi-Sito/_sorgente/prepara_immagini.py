# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Albergo Vescovi in assets/web/ (specifica, paragrafi 4.7 e 16).

- Un solo tono per tutte le foto (quello del prototipo approvato, giro 2 "la fotografia"): neri sollevati a 12,
  bianchi abbassati a 247 (il bordo di una foto chiara si vede sul bianco della pagina), saturazione 0,82.
  Prima del tono solo correzioni di luce, mai di colore degli oggetti: la sauna meno arancio, il cielo d'inverno
  meno ciano.
- Una sola eccezione: il secchio tirolese in bianco e nero (la doccia emozionale è illuminata di verde acceso).
- Ritagli per uso e per punto di rottura, mai più grandi della sorgente; jpg qualità 82, progressivi.
- Logo tondo: il PNG scontornato ha un alone semitrasparente, qui viene appoggiato sul bianco ed esportato
  al doppio della misura mostrata (120 px per la testata da 60, 152 px per il piede da 76).

Legge file scaricati: eseguire con python3 -I prepara_immagini.py
Scrive anche _prova/immagini-web.json (sorgente, riquadro, pixel in uscita) per il controllo delle densità.
"""
import json
import os

from PIL import Image, ImageEnhance, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
EST = os.path.join(ASSET, 'esterne')
WEB = os.path.join(ASSET, 'web')

NERO = 12
BIANCO = 247
SATURAZIONE = 0.82
QUALITA = 82


def tono(im):
    """Lo stesso per tutte le foto a colori."""
    lut = [round(NERO + v * (BIANCO - NERO) / 255) for v in range(256)]
    im = im.point(lut * 3)
    return ImageEnhance.Color(im).enhance(SATURAZIONE)


def bilancia(im, r, g, b):
    """Bilanciamento del bianco: moltiplica i canali."""
    out = [c.point(lambda v, f=f: min(255, round(v * f))) for c, f in zip(im.split(), (r, g, b))]
    return Image.merge('RGB', out)


def azzurri_meno_accesi(im, fattore):
    """Riduce la saturazione solo dei toni azzurri e ciano (cielo e ombre sulla neve)."""
    h, s, v = im.convert('HSV').split()

    def peso(t):
        if 118 <= t <= 182:
            return 255
        if 104 <= t < 118:
            return round(255 * (t - 104) / 14)
        if 182 < t <= 196:
            return round(255 * (196 - t) / 14)
        return 0

    maschera = h.point([peso(t) for t in range(256)])
    s = Image.composite(s.point(lambda x: round(x * fattore)), s, maschera)
    return Image.merge('HSV', (h, s, v)).convert('RGB')


CORREZIONI = {
    'booking-spa-sauna.jpg': lambda im: bilancia(im, 0.94, 1.02, 1.04),
    'booking-inverno-hotel-nella-neve.jpg': lambda im: azzurri_meno_accesi(im, 0.74),
}

# nome in assets/web: (cartella, sorgente, ritaglio x0, y0, x1, y1 nei px della sorgente, larghezza in uscita o None,
#                      'colore' | 'bn')
FOTO = {
    # Home (prototipo approvato)
    'apertura-prato.jpg': (EST, 'booking-esterno-hotel-prato-estate.jpg', (0, 700, 1870, 1755), None, 'colore'),
    'apertura-prato-telefono.jpg': (EST, 'booking-esterno-hotel-prato-estate.jpg', (500, 600, 1340, 2250), None, 'colore'),
    'camera-abete.jpg': (EST, 'booking-camera-legno-finestre.jpg', (120, 250, 2850, 1730), None, 'colore'),
    'camera-abete-telefono.jpg': (EST, 'booking-camera-legno-finestre.jpg', (700, 200, 2300, 1800), 1200, 'colore'),
    'tavola-prati.jpg': (EST, 'booking-tavola-pasta-vino-vista-prati.jpg', (0, 330, 1996, 2825), 1400, 'colore'),
    'sauna-panche-stufa.jpg': (EST, 'booking-spa-sauna.jpg', (130, 1480, 1866, 2782), 1560, 'colore'),
    'inverno-prato.jpg': (EST, 'booking-inverno-hotel-nella-neve.jpg', (0, 340, 2000, 1451), None, 'colore'),
    'inverno-prato-telefono.jpg': (EST, 'booking-inverno-hotel-nella-neve.jpg', (60, 380, 1060, 1500), None, 'colore'),
    # Camere
    'camere-letto-abete.jpg': (EST, 'booking-camera-letto-parete-legno.jpg', (150, 380, 2850, 1730), 2250, 'colore'),
    'camere-letto-abete-telefono.jpg': (EST, 'booking-camera-letto-parete-legno.jpg', (750, 121, 2250, 1996), 1000, 'colore'),
    'camere-pietra.jpg': (EST, 'booking-camera-pietra-arazzo.jpg', (200, 0, 2860, 1996), 1440, 'colore'),
    'camere-bagno-pietra.jpg': (EST, 'booking-bagno-vasca-pietra-scura.jpg', (0, 0, 2660, 1996), 1440, 'colore'),
    'camere-famiglie.jpg': (EST, 'booking-camera-bianca-armadio.jpg', (300, 0, 2960, 1996), 1440, 'colore'),
    # Ristorante
    'ristorante-stube.jpg': (EST, 'booking-ristorante-stube-stufa.jpg', (0, 260, 2560, 1540), 1920, 'colore'),
    'ristorante-stube-telefono.jpg': (EST, 'booking-ristorante-stube-stufa.jpg', (250, 0, 1847, 1996), 1000, 'colore'),
    'ristorante-tavola-alto.jpg': (EST, 'booking-tavola-gnocchi-pane-vino.jpg', (0, 250, 1996, 2745), 1320, 'colore'),
    'ristorante-cantinetta.jpg': (EST, 'booking-cantinetta-vini.jpg', (100, 250, 1896, 2495), 1320, 'colore'),
    # Centro benessere
    'benessere-sauna.jpg': (EST, 'booking-spa-sauna.jpg', (0, 300, 1996, 2795), 1440, 'colore'),
    'benessere-secchio-bn.jpg': (EST, 'booking-spa-doccia-emozionale.jpg', (850, 150, 1850, 1150), None, 'bn'),
    # Contatti e chiusura comune
    'contatti-panorama.jpg': (ORIG, 'panorama-piana-ave-hotel.jpg', (0, 0, 2000, 600), None, 'colore'),
    'chiusura-panorama-telefono.jpg': (ORIG, 'panorama-piana-ave-hotel.jpg', (560, 0, 1360, 600), None, 'colore'),
    'contatti-reception.jpg': (EST, 'booking-reception-bancone-legno.jpg', (0, 250, 3000, 1996), 1700, 'colore'),
    # Contributi: il banner è un'immagine ufficiale, nessun tono
    'banner-por-fesr.jpg': (ORIG, 'banner-por-fesr-2014-2020.png', None, 1120, 'grafica'),
}


def bianco_e_nero(im):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=(0.5, 0.5))
    lut = [round(NERO + v * (BIANCO - NERO) / 255) for v in range(256)]
    return g.point(lut).convert('RGB')


def salva_jpg(im, nome):
    im.save(os.path.join(WEB, nome), quality=QUALITA, optimize=True, progressive=True)


def logo_su_bianco(misure):
    """Logo tondo appoggiato sul bianco (niente alone semitrasparente), al doppio della misura mostrata."""
    src = Image.open(os.path.join(ORIG, 'logo-tondo-hotel-vescovi.png')).convert('RGBA')
    bbox = src.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox()
    src = src.crop(bbox)
    lato = max(src.size)
    quadro = Image.new('RGBA', (lato, lato), (255, 255, 255, 0))
    quadro.paste(src, ((lato - src.width) // 2, (lato - src.height) // 2))
    fondo = Image.new('RGBA', quadro.size, (255, 255, 255, 255))
    piatto = Image.alpha_composite(fondo, quadro).convert('RGB')
    out = {}
    for px in misure:
        nome = f'logo-tondo-{px}.png'
        piatto.resize((px, px), Image.LANCZOS).save(os.path.join(WEB, nome), optimize=True)
        out[nome] = {'sorgente': 'logo-tondo-hotel-vescovi.png', 'ritaglio': list(bbox), 'uscita_px': [px, px]}
    return out


def loghi_contributi():
    src = Image.open(os.path.join(ORIG, 'loghi-contributi-csr-2023-2027.png')).convert('RGBA')
    fondo = Image.new('RGBA', src.size, (255, 255, 255, 255))
    Image.alpha_composite(fondo, src).convert('RGB').save(os.path.join(WEB, 'loghi-contributi.png'), optimize=True)
    return {'loghi-contributi.png': {'sorgente': 'loghi-contributi-csr-2023-2027.png', 'uscita_px': list(src.size)}}


def main():
    os.makedirs(WEB, exist_ok=True)
    rapporto, cache = {}, {}
    for nome, (cartella, sorgente, box, larghezza, modo) in FOTO.items():
        chiave = (cartella, sorgente, modo)
        if chiave not in cache:
            im = Image.open(os.path.join(cartella, sorgente)).convert('RGB')
            if modo == 'colore':
                if sorgente in CORREZIONI:
                    im = CORREZIONI[sorgente](im)
                im = tono(im)
            elif modo == 'bn':
                im = bianco_e_nero(im)
            cache[chiave] = im
        im = cache[chiave]
        x0, y0, x1, y1 = box or (0, 0, im.width, im.height)
        c = im.crop((x0, y0, min(x1, im.width), min(y1, im.height)))
        if larghezza and c.width > larghezza:          # solo riduzioni: mai più grande della sorgente
            c = c.resize((larghezza, round(c.height * larghezza / c.width)), Image.LANCZOS)
        salva_jpg(c, nome)
        rapporto[nome] = {'sorgente': sorgente, 'ritaglio': [x0, y0, x1, y1], 'uscita_px': list(c.size), 'modo': modo}
        print(f'{nome}: {c.width} x {c.height}')
    rapporto.update(logo_su_bianco((120, 152)))
    rapporto.update(loghi_contributi())
    prova = os.path.join(os.path.dirname(QUI), '_prova')
    os.makedirs(prova, exist_ok=True)
    with open(os.path.join(prova, 'immagini-web.json'), 'w', encoding='utf-8') as f:
        json.dump(rapporto, f, ensure_ascii=False, indent=1)
    print(f'ok: {len(rapporto)} file in {WEB}')


if __name__ == '__main__':
    main()
