# -*- coding: utf-8 -*-
"""
Prepara assets/web/ per la versione WordPress della home di Tek.Lam.

La home statica approvata (sito/index.html) usa le immagini di sito/img/, che fa _prova/script/finale_img.py
dagli originali di assets/originali/ e dalla spazzolatura di assets/esterne/ (trattamento caldo, lastra con la
luce rifatta, ritagli dei pezzi dalle Realizzazioni, tagli verticali per il telefono). Per avere in WordPress
esattamente gli stessi pixel, qui non si rielabora niente: si copiano gli stessi file, con gli stessi nomi,
e si controlla che ci siano tutti quelli che la home usa (contenuti.py li chiama per nome).

Caratteri: gli stessi woff2 della statica (Big Shoulders Display e Sofia Sans, file di Google Fonts non modificati,
SIL OFL 1.1) vanno in assets/web/fonts/ con le licenze: servono solo con build.py --caratteri-locali.

Uso: python3 _sorgente/prepara_immagini.py   (dopo python3 -I _prova/script/finale_img.py, se le foto cambiano)
"""
import hashlib
import os
import shutil
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
IMG = os.path.join(RADICE, 'sito', 'img')
FONT = os.path.join(RADICE, 'sito', 'fonts')
WEB = os.path.join(RADICE, 'assets', 'web')

# le immagini della home, nell'ordine in cui compaiono
IMMAGINI = [
    'logo-segno.png',                                                    # segno del marchio, testata e piede
    'letto-1000.jpg', 'letto-1600.jpg', 'letto-v-480.jpg', 'letto-v-800.jpg',    # il loro laser, sotto la lastra
    'lastra-1440.jpg', 'lastra-2160.jpg', 'lastra-2730.jpg',             # la lastra 3000 x 1500 (motivo SVG)
    'lastra-v-780.jpg', 'lastra-v-1170.jpg',                             # la lastra girata, sul telefono
    'p-case.jpg', 'p-griglia.jpg', 'p-cassetto.jpg', 'p-telaio-inox.jpg', 'p-telaio-frigo.jpg', 'p-modello.jpg',
    'punzonatura-960.jpg', 'punzonatura-1330.jpg', 'punzonatura-m-514.jpg',          # la SG6
    'officina-640.jpg', 'officina-960.jpg', 'officina-1330.jpg', 'officina-m-861.jpg',  # saldatura TIG
    'piega-960.jpg', 'piega-1330.jpg', 'piega-v-516.jpg',               # la piegatrice
    'sede-470.jpg',                                                      # la sede
]
CARATTERI = ['bsd-latin.woff2', 'sofia-latin.woff2', 'sofia-latin-ext.woff2',
             'OFL-bigshouldersdisplay.txt', 'OFL-SofiaSans.txt']


def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def copia(nomi, da, a):
    os.makedirs(a, exist_ok=True)
    mancano = [n for n in nomi if not os.path.exists(os.path.join(da, n))]
    if mancano:
        sys.exit('mancano in ' + da + ': ' + ', '.join(mancano))
    for n in nomi:
        s, d = os.path.join(da, n), os.path.join(a, n)
        if not os.path.exists(d) or md5(s) != md5(d):
            shutil.copy2(s, d)
    return sum(os.path.getsize(os.path.join(a, n)) for n in nomi)


def main():
    tot = copia(IMMAGINI, IMG, WEB)
    tot_f = copia(CARATTERI, FONT, os.path.join(WEB, 'fonts'))
    usate = set(os.listdir(IMG))
    in_piu = sorted(usate - set(IMMAGINI))
    if in_piu:
        print('in sito/img ma non copiate (non usate dalla home?):', ', '.join(in_piu))
    print(f'assets/web: {len(IMMAGINI)} immagini, {tot / 1e6:.1f} MB; fonts/: {len(CARATTERI)} file, {tot_f / 1e3:.0f} kB')


if __name__ == '__main__':
    main()
