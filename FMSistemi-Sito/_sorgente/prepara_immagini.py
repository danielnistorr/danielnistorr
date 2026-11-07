# -*- coding: utf-8 -*-
"""
Prepara le immagini e i caratteri della home di F.M. Sistemi in assets/web/.

Parte dalle immagini già preparate per la home statica (sito/img/, fatte da _prova/script/finale_img.py
sulle foto segnaposto Pexels di assets/esterne/) e prende solo quelle che servono alla versione WordPress.
Le immagini non vengono ritoccate: tagli, bianco e nero e gradazione sono quelli della home approvata.
Sono le stesse della home statica, quindi si collegano (hard link) invece di copiarle, se il disco lo permette.

- tavola-t-*: il raccordo a T dell'apertura, tutte e cinque le misure, per il <picture> del widget HTML
  (la geometria della T dipende dalla larghezza della finestra, come nella statica)
- lavoro-<lettera>-1440 e lavoro-<lettera>-m-1170: le otto strisce dei mestieri, la versione larga per computer e tablet
  e il taglio del telefono (widget Immagine: WordPress rifà da sé le misure più piccole nella libreria media)
- collettore e inverno: 1920 per computer e tablet, taglio verticale 1170 per il telefono (widget Immagine)
- logo.png (testata e piede: il raster del sito attuale con il nero portato a grafite, fondo trasparente), favicon-192.png (icona del sito)
- fonts/: Funnel Display e Funnel Sans (woff2 della pagina statica, non modificati) e la licenza OFL. Le @font-face
  sono nel foglio di stile di ogni sezione (contenuti.css_variabili), con l'indirizzo dei woff2 sulla base delle immagini:
  nessun foglio .css a parte, perché raw.githubusercontent serve i .css come text/plain e il browser li scarta

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

LETTERE = 'rteapcfm'          # i mestieri nell'ordine del cantiere

# nome in sito/img (uguale in assets/web) -> misura attesa
FOTO = {
    'tavola-t-1600.jpg': (1600, 1409),
    'tavola-t-2000.jpg': (2000, 1761),
    'tavola-t-2560.jpg': (2560, 2254),
    'tavola-t-m-780.jpg': (780, 1100),
    'tavola-t-m-1170.jpg': (1170, 1650),
    'collettore-1920.jpg': (1920, 960),
    'collettore-m-1170.jpg': (1170, 1462),
    'inverno-1920.jpg': (1920, 960),
    'inverno-m-1170.jpg': (1170, 1773),
    'logo.png': (480, 80),
    'favicon-192.png': (192, 192),
}
for l in LETTERE:
    FOTO[f'lavoro-{l}-1440.jpg'] = None        # 1440 x 411-412
    FOTO[f'lavoro-{l}-m-1170.jpg'] = None      # 1170 x 449-450

CARATTERI = ['funnel-display-latin.woff2', 'funnel-sans-latin.woff2', 'OFL.txt']


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
            if misura and im.size != misura:
                raise SystemExit(f'{nome}: misura {im.size}, attesa {misura}')
            if not misura and not (abs(im.width / im.height - (2.6 if nome.endswith('-m-1170.jpg') else 3.5)) < 0.02):
                raise SystemExit(f'{nome}: proporzioni {im.size} diverse dalla striscia della statica')
        collega(src, os.path.join(WEB, nome))
    for nome in CARATTERI:
        collega(os.path.join(SITO, 'fonts', nome), os.path.join(WEB, 'fonts', nome))
    # il vecchio foglio dei caratteri non serve più (le @font-face sono nei fogli delle sezioni)
    vecchio = os.path.join(WEB, 'fonts', 'caratteri.css')
    if os.path.exists(vecchio):
        os.remove(vecchio)
    # nient'altro in assets/web: se una foto non serve più, la tolgo
    tenere = set(FOTO) | {'fonts'}
    for nome in os.listdir(WEB):
        if nome not in tenere:
            os.remove(os.path.join(WEB, nome))
    print(f'assets/web: {len(FOTO)} immagini e {len(CARATTERI)} file di caratteri')


if __name__ == '__main__':
    main()
