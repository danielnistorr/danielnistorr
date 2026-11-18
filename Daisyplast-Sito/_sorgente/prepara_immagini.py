# -*- coding: utf-8 -*-
"""
Prepara le immagini e i caratteri della home di Daisyplast in assets/web/.

Parte dalle immagini già preparate per la home statica (sito/img/, fatte da _prova/script/finale_img.py:
bicromo grafite e latte con le luci al giallo del logo, WebP in più larghezze) e prende solo quelle che servono
alla versione WordPress. Non le ritocca: colori, tagli e gradazione sono quelli della home approvata.

- Widget Immagine di Elementor (finiscono nella libreria media, WordPress rifà da sé le misure più piccole):
  per ogni foto la versione più larga della statica, più il taglio verticale del telefono dove la statica lo ha
  (la statica usa <picture>: qui sono due widget, uno per desktop e tablet e uno per il telefono).
- logo.webp: il logo del sito daisyplast.it, nei suoi colori.
- fonts/: Sofia Sans e Sofia Sans Extra Condensed (woff2 di Google Fonts, non modificati) con la licenza OFL,
  per chi vuole servire i caratteri dal sito invece che da Google Fonts (vedi LEGGIMI, "Caratteri").

I file sono collegati (hard link) invece che copiati, se il disco lo permette.
Uso: python3 prepara_immagini.py
"""
import os
import shutil

from PIL import Image

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
SITO = os.path.join(RADICE, 'sito')
IMG = os.path.join(SITO, 'img')
WEB = os.path.join(RADICE, 'assets', 'web')

# nome in sito/img (uguale in assets/web) -> misura attesa
FOTO = {
    'logo.webp': (530, 146),                  # testata
    'bolla-768.webp': (768, 1280),            # apertura, colonna della bolla (desktop e tablet)
    'bolla-p-590.webp': (590, 1280),          # apertura, telefono
    'vergine-l-2400.webp': (2400, 1200),      # selettore dei materiali
    'vergine-p-1160.webp': (1160, 1450),
    'rigenerato-l-2400.webp': (2400, 1200),
    'rigenerato-p-1200.webp': (1200, 1500),
    'compostabile-l-2400.webp': (2400, 1200),
    'compostabile-p-1120.webp': (1120, 1400),
    't1-ordine-1440.webp': (1440, 640),       # percorso di un ordine, le tappe
    't1-ordine-p-900.webp': (900, 1076),
    't2-piano-1920.webp': (1920, 853),
    't2-piano-p-700.webp': (700, 700),
    't3-bobine-1920.webp': (1920, 854),
    't3-bobine-p-900.webp': (900, 1117),
    't5-consegna-1920.webp': (1920, 853),
    't5-consegna-p-900.webp': (900, 1031),
}

CARATTERI = ['sofiasans-latin.woff2', 'sofiasansextracondensed-latin.woff2', 'OFL.txt']


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
    for nome, misura in FOTO.items():
        src = os.path.join(IMG, nome)
        with Image.open(src) as im:
            if im.size != misura:
                raise SystemExit(f'{nome}: misura {im.size}, attesa {misura}')
        collega(src, os.path.join(WEB, nome))
    for nome in CARATTERI:
        collega(os.path.join(SITO, 'fonts', nome), os.path.join(WEB, 'fonts', nome))
    print(f'assets/web: {len(FOTO)} immagini, {len(CARATTERI)} file di caratteri')


if __name__ == '__main__':
    main()
