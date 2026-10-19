# -*- coding: utf-8 -*-
"""
Prepara le immagini e il carattere della home di Mario Agnoletto in assets/web/.

Parte dai file già preparati per la home statica (sito/img/ e sito/fonts/, fatti da _prova/script/build_finale.sh
sulle foto del sito marioagnoletto.it e sulla foto Unsplash della fresa) e prende solo quelli che servono
alla versione WordPress, senza ritoccarli: colori, tagli, scontorni e gradazione sono quelli della home approvata.
- tacco-l-*, tacco-p-*: il tacco dell'apertura, orizzontale e ruotato per il telefono, nelle due larghezze della
  statica (widget HTML con il <picture> della statica, i richiami e il timbro);
- logo.svg, timbro.svg, timbro-grafite.svg: il logo ricalcato e il monogramma (widget HTML);
- le dieci foto dei widget Immagine, nella misura più grande della statica (la risoluzione vera della foto):
  WordPress rifà da sé le misure più piccole quando Elementor le carica nella libreria media;
- fonts/: Host Grotesk (woff2 della statica, sottoinsieme latino, pesi 300-800) con la licenza OFL.
I file si collegano (hard link) invece di copiarli, se il disco lo permette.
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
    'tacco-l-480.webp': (480, 699),        # apertura, da 901 px in su
    'tacco-l-744.webp': (744, 1084),
    'tacco-p-400.webp': (400, 583),        # apertura, telefono e tablet stretto (pezzo ruotato)
    'tacco-p-744.webp': (744, 1084),
    't-tacchi-660.webp': (660, 1000),      # campione 01, la gabbia
    't-punzoni-700.webp': (700, 700),      # 02
    't-fustelle-720.webp': (720, 720),     # 03
    't-ruote-820.webp': (820, 820),        # 04
    't-bigiotteria-1080.webp': (1080, 1080),   # 05
    't-accessori-1180.webp': (1180, 590),  # 06
    't-stampa-960.webp': (960, 480),       # 07
    'fresa-2100.webp': (2100, 1600),       # B, Prototipo (foto di repertorio)
    'finiture-670.webp': (670, 820),       # B, Serie
    'ottone-1920.webp': (1920, 1080),      # C, Punzoni
}
SVG = ['logo.svg', 'timbro.svg', 'timbro-grafite.svg']


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
    for nome in SVG:
        collega(os.path.join(IMG, nome), os.path.join(WEB, nome))
    collega(os.path.join(SITO, 'fonts', 'host-grotesk-latin.woff2'), os.path.join(WEB, 'fonts', 'host-grotesk-latin.woff2'))
    collega(os.path.join(QUI, 'OFL-Host-Grotesk.txt'), os.path.join(WEB, 'fonts', 'OFL-Host-Grotesk.txt'))
    print(f'assets/web: {len(FOTO)} foto, {len(SVG)} SVG, 1 carattere con la licenza')


if __name__ == '__main__':
    main()
