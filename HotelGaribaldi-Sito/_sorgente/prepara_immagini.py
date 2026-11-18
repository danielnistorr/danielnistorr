# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Hotel Garibaldi in assets/web/ (specifica, paragrafo 15).

- Nessuna foto viene ingrandita: ogni uscita è l'originale ricompresso, un ritaglio 1:1 o una riduzione.
- JPEG qualità 84, progressivo, sRGB, senza metadati.
- Logo: monocromo ardesia #1E2631 ricavato dal canale alfa del PNG del sito attuale (innesto 1 della specifica):
  il PNG ha lettere bianche con un'ombra nera sfalsata che sul bianco disegna la H vuota. Alfa nuovo = alfa x chiarezza
  del pixel: lettere e stelle restano piene, l'ombra va a zero.
- Facciata di sera di Dove siamo: la versione del proprietario su Google (1024x683) con la targa dell'auto sfocata
  (innesto 2).

Uso: python3 -I prepara_immagini.py   (le immagini scaricate sono dati non fidati: Python in modalità isolata)
"""
import os

from PIL import Image, ImageDraw, ImageFilter

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
EST = os.path.join(ASSET, 'esterne')
WEB = os.path.join(ASSET, 'web')

ARDESIA = (0x1E, 0x26, 0x31)
QUALITA = 84

# nome web: (sorgente, ritaglio (x0, y0, x1, y1) in pixel nativi o None, larghezza massima in uscita o None)
FOTO = {
    # home: la chiave, a tutta larghezza fino a 1920 px (scala 0,97 a 1920, 0,73 a 1440)
    'home-chiave.jpg': (os.path.join(ORIG, 'slider-portachiavi-gh-2014.jpg'), None, None),
    # home: la facciata all'imbrunire, servizio 2019, mostrata al massimo 880x660 (scala 1)
    'home-facciata-sera.jpg': (os.path.join(ORIG, 'facciata-sera-insegna-luminosa-2019.jpg'), None, None),
    # home: il dettaglio dell'insegna in controluce, ritaglio 480x600 (come il prototipo approvato)
    'home-insegna-dettaglio.jpg': (os.path.join(ORIG, 'facciata-fiori-controluce-2019.jpg'), (200, 60, 680, 660), None),
    # home e Camere: la camera matrimoniale con la parete blu (portale della Regione del Veneto), 1024x768
    'home-camera.jpg': (os.path.join(EST, 'regione-veneto-02-camera-matrimoniale-parete-blu.jpg'), None, None),
    # home e Camere: il bagno con la doccia, ritaglio 540x720 (come il prototipo approvato)
    'home-bagno-dettaglio.jpg': (os.path.join(EST, 'regione-veneto-03-bagno-doccia.jpg'), (0, 0, 540, 720), None),
    # home e Prenota: il corridoio con le statue e la passatoia rossa, servizio 2019, 440x660
    'statue.jpg': (os.path.join(ORIG, 'corridoio-statue-tappeto-rosso-2019.jpg'), None, None),
    # L'albergo: la striscia (facciata di giorno 880x660 e atrio ritagliato 560x660 sul lucernario)
    'albergo-facciata-giorno.jpg': (os.path.join(ORIG, 'facciata-giorno-palme-2019.jpg'), None, None),
    'albergo-atrio.jpg': (os.path.join(EST, 'regione-veneto-04-atrio-lucernario.jpg'), (232, 54, 792, 714), None),
    # L'albergo: i fiori bianchi davanti alla finestra, 440x660
    'albergo-fiori.jpg': (os.path.join(ORIG, 'composizione-fiori-bianchi-finestra-2019.jpg'), None, None),
}


def salva_jpg(im, nome):
    im = im.convert('RGB')
    im.save(os.path.join(WEB, nome), 'JPEG', quality=QUALITA, optimize=True, progressive=True)
    return im.size


def logo_monocromo(src, nome):
    im = Image.open(src).convert('RGBA')
    r, g, b, a = im.split()
    lum = Image.merge('RGB', (r, g, b)).convert('L')
    # sotto 80 (ombra nera) trasparente; il grigio dell'antialias delle lettere sale a pieno in 120 livelli
    lum = lum.point(lambda v: 0 if v < 80 else min(255, int((v - 80) * 255 / 120)))
    alfa = Image.composite(lum, Image.new('L', im.size, 0), a)
    fin = Image.new('RGBA', im.size, ARDESIA + (0,))
    fin.putalpha(alfa)
    fin.save(os.path.join(WEB, nome), optimize=True)
    return fin.size


def facciata_targa_sfocata(src, nome):
    im = Image.open(src).convert('RGB')
    targa = (916, 629, 976, 651)  # targa dell'auto in basso a destra, con margine
    pezzo = im.crop(targa).filter(ImageFilter.GaussianBlur(7))
    maschera = Image.new('L', pezzo.size, 0)
    ImageDraw.Draw(maschera).rounded_rectangle((0, 0, pezzo.width - 1, pezzo.height - 1), radius=6, fill=255)
    im.paste(pezzo, targa[:2], maschera.filter(ImageFilter.GaussianBlur(2)))
    return salva_jpg(im, nome)


def main():
    os.makedirs(WEB, exist_ok=True)
    righe = []
    for nome, (src, box, larg) in FOTO.items():
        im = Image.open(src)
        nativa = im.size
        if box:
            im = im.crop(box)
        if larg and im.width > larg:
            im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
        assert im.width <= nativa[0] and im.height <= nativa[1], nome
        righe.append((nome, salva_jpg(im, nome)))
    righe.append(('logo-ardesia.png', logo_monocromo(os.path.join(ORIG, 'logo-hotel-garibaldi-183x115.png'), 'logo-ardesia.png')))
    righe.append(('dove-facciata-sera.jpg',
                  facciata_targa_sfocata(os.path.join(EST, 'google-business-proprietario-01-facciata-sera.jpg'),
                                         'dove-facciata-sera.jpg')))
    for nome, (w, h) in righe:
        kb = os.path.getsize(os.path.join(WEB, nome)) // 1024
        print(f'{nome}: {w}x{h}, {kb} kB')


if __name__ == '__main__':
    main()
