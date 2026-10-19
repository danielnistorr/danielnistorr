# -*- coding: utf-8 -*-
"""
Prepara le immagini e i caratteri della home di Hambro in assets/web/.

Parte dalle immagini già preparate per la home statica (sito/img/, fatte da _prova/script/finale_img.py:
ritagli, gradazione sulla carta #F2EDE4, larghezze) e prende solo quelle che servono alla versione WordPress.
Per ogni foto prende il file più largo della home statica: WordPress, quando Elementor la carica nella libreria
media, rifà da sé le misure più piccole e le mette nel srcset.
- apertura: i tre tagli della home statica (oltre 1100 px, tablet, telefono)
- banco-cuoio.jpg: la striscia del banco di misura (sfondo CSS, resta all'indirizzo della base delle immagini)
- cat/: gli 11 scontornati del cassetto della minuteria
- bobine della Tav. 2, dittico metallo e pelle, semilavorati (desktop e telefono)
- fonts/: Mona Sans (woff2 di Google Fonts, non modificati) con la licenza OFL

Le immagini non vengono ritoccate: colori, tagli e gradazione sono quelli della home approvata.
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

# nome in sito/img -> misura attesa (in assets/web il nome resta uguale)
FOTO = {
    'apertura-2400.jpg': (2400, 1500),          # apertura oltre 1100 px
    'apertura-t-1600.jpg': (1600, 1391),        # apertura tablet (701-1100)
    'apertura-m-1170.jpg': (1170, 1090),        # apertura telefono
    'banco-cuoio.jpg': (1500, 300),             # striscia del banco (taglio vivo e tubolare)
    'bobina-laccio-720.jpg': (720, 1080),       # Tav. 2
    'bobina-tondino-720.jpg': (720, 1080),
    'metallo-1170.jpg': (1170, 1460),           # dittico della ricopertura, il metallo
    'pelle-1072.jpg': (1072, 1340),             # dittico, la pelle
    'semilavorati-2400.jpg': (2400, 1420),      # Tav. 4, oltre 700 px
    'semilavorati-m-1170.jpg': (1170, 1310),    # Tav. 4, telefono
}
CASSETTO = ['moschettoni-tondo', 'moschettoni-ovale', 'moschettoni-rettangolare', 'mezzi-anelli', 'anelli', 'fibbie-doppie',
            'attacchi-spinetta', 'attacco-alette', 'chiusure-pulsante', 'chiusure-girello', 'chiusure-battente']
CARATTERI = ['mona-latin.woff2', 'mona-latin-ext.woff2', 'OFL.txt']


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
    for nome in CASSETTO:
        src = os.path.join(IMG, 'cat', nome + '.jpg')
        with Image.open(src) as im:
            if im.size != (560, 440):
                raise SystemExit(f'cat/{nome}.jpg: misura {im.size}, attesa (560, 440)')
        collega(src, os.path.join(WEB, 'cat', nome + '.jpg'))
        n += 1
    for nome in CARATTERI:
        collega(os.path.join(SITO, 'fonts', nome), os.path.join(WEB, 'fonts', nome))
    print(f'assets/web: {n} immagini, {len(CARATTERI)} file di caratteri')


if __name__ == '__main__':
    main()
