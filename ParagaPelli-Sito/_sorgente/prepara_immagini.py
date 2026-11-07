# -*- coding: utf-8 -*-
"""
Prepara le immagini e i caratteri della home di Paraga Pelli in assets/web/.

Parte dalle immagini già preparate per la home statica (sito/img/, fatte da _prova/script/finale_img.py
sugli originali del sito paragapelli.com) e prende solo quelle che servono alla versione WordPress:
- c/<articolo>/*.webp e c2/<articolo>/*.webp: le 403 scansioni dei campioni a 350 e a 640 px (mazzetta e cartellino);
  sono le stesse della home statica, quindi si collegano (hard link) invece di copiarle, se il disco lo permette
- d-<articolo>.jpg: i 27 dorsi delle cartelle colori (80x350)
- drappo: le cinque misure della statica (800, 1200, 1680 e i tagli verticali 480 e 651), per il <picture> del widget HTML
- corsia, squadra: la versione più larga per desktop e tablet e il taglio verticale per il telefono
  (WordPress rifà da sé le misure più piccole quando Elementor le carica nella libreria media)
- box-265.jpg: il box-campionario
- fonts/: Mona Sans e Libre Caslon Display (woff2 di Google Fonts, non modificati) con le licenze OFL

Le immagini non vengono ritoccate: colori, tagli e gradazione sono quelli della home approvata.
Uso: python3 prepara_immagini.py
"""
import glob
import os
import shutil

from PIL import Image

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
SITO = os.path.join(RADICE, 'sito')
IMG = os.path.join(SITO, 'img')
WEB = os.path.join(RADICE, 'assets', 'web')

# immagini singole: nome in sito/img -> nome in assets/web (uguale) e misura attesa
FOTO = {
    # apertura: mappa di luce del drappo, tinta dal browser; nel widget HTML con il <picture> della statica
    'drappo-800.jpg': (800, 500),
    'drappo-1200.jpg': (1200, 750),
    'drappo-1680.jpg': (1680, 1050),
    'drappo-v-480.jpg': (480, 774),      # telefono
    'drappo-v-651.jpg': (651, 1050),
    'corsia-1680.jpg': (1680, 400),      # il magazzino
    'corsia-v-500.jpg': (500, 400),
    'squadra-1620.jpg': (1620, 800),     # la squadra in magazzino
    'squadra-v-800.jpg': (800, 800),
    'box-265.jpg': (265, 313),           # il box-campionario
}

CARATTERI = ['mona-sans-latin.woff2', 'libre-caslon-display-latin.woff2', 'OFL-Mona-Sans.txt', 'OFL-Libre-Caslon-Display.txt']


def collega(src, dst):
    """Hard link se possibile (nessuno spazio in più sul disco), altrimenti copia."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        if os.path.samefile(src, dst):
            return
        os.remove(dst)
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def main():
    os.makedirs(WEB, exist_ok=True)
    n = 0
    for nome, misura in FOTO.items():
        src = os.path.join(IMG, nome)
        with Image.open(src) as im:
            if im.size != misura:
                raise SystemExit(f'{nome}: misura {im.size}, attesa {misura}')
        collega(src, os.path.join(WEB, nome))
        n += 1
    dorsi = sorted(glob.glob(os.path.join(IMG, 'd-*.jpg')))
    if len(dorsi) != 27:
        raise SystemExit(f'dorsi: {len(dorsi)} invece di 27')
    for f in dorsi:
        collega(f, os.path.join(WEB, os.path.basename(f)))
        n += 1
    scansioni = 0
    for cartella in ('c', 'c2'):
        file = sorted(glob.glob(os.path.join(IMG, cartella, '*', '*.webp')))
        if len(file) != 403:
            raise SystemExit(f'{cartella}: {len(file)} scansioni invece di 403')
        for f in file:
            rel = os.path.relpath(f, IMG)
            collega(f, os.path.join(WEB, rel))
            scansioni += 1
    for nome in CARATTERI:
        collega(os.path.join(SITO, 'fonts', nome), os.path.join(WEB, 'fonts', nome))
    print(f'assets/web: {n} immagini, {scansioni} scansioni, {len(CARATTERI)} file di caratteri')


if __name__ == '__main__':
    main()
