# -*- coding: utf-8 -*-
"""
Prepara assets/web/ per la versione WordPress della home di Tek.Lam.

La home statica approvata ("Scintilla e spessore", sito/index.html) usa le immagini di sito/img/, che fanno gli
script di _prova/script/ (build_finale.sh) dagli originali di assets/originali/ e dalle foto di assets/esterne/
(trattamento caldo, tagli verticali per il telefono, più larghezze per il srcset). Per avere in WordPress
esattamente gli stessi pixel, qui non si rielabora niente: si copiano gli stessi file, con gli stessi nomi,
e si controlla che ci siano tutti quelli che la home usa (contenuti.py li chiama per nome).

Carattere: gli stessi woff2 della statica (Sofia Sans, file di Google Fonts non modificati, SIL OFL 1.1) vanno in assets/web/fonts/ con le licenze: servono solo con build.py --caratteri-locali.

Uso: python3 _sorgente/prepara_immagini.py   (dopo bash _prova/script/build_finale.sh, se le foto cambiano)
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
    'logo-segno.png', 'logo-scritta-chiara.png',                          # marchio, testata e piede
    'apertura-1000.jpg', 'apertura-1440.jpg', 'apertura-1800.jpg', 'apertura-2400.jpg',   # taglio laser (Unsplash)
    'apertura-v-600.jpg', 'apertura-v-860.jpg', 'apertura-v-1280.jpg',    # il taglio verticale per il telefono
    'piega-1000.jpg', 'piega-1600.jpg', 'piega-2400.jpg', 'piega-m-640.jpg', 'piega-m-1000.jpg',   # fascia (Unsplash)
    'officina-640.jpg', 'officina-960.jpg', 'officina-1330.jpg',          # saldatura TIG (Tek.Lam)
    'contatti-1000.jpg', 'contatti-1600.jpg', 'contatti-2400.jpg', 'contatti-m-800.jpg',   # fondo dei contatti
]
CARATTERI = ['sofia-latin.woff2', 'sofia-latin-ext.woff2', 'OFL-SofiaSans.txt']


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
    # via i file che la home non usa più (per esempio quelli della versione "Il foglio annidato", bocciata)
    for d, nomi in ((WEB, IMMAGINI), (os.path.join(WEB, 'fonts'), CARATTERI)):
        if os.path.isdir(d):
            for n in os.listdir(d):
                if os.path.isfile(os.path.join(d, n)) and n not in nomi:
                    os.remove(os.path.join(d, n))
    tot = copia(IMMAGINI, IMG, WEB)
    tot_f = copia(CARATTERI, FONT, os.path.join(WEB, 'fonts'))
    usate = set(os.listdir(IMG))
    in_piu = sorted(usate - set(IMMAGINI))
    if in_piu:
        print('in sito/img ma non copiate (non usate dalla home?):', ', '.join(in_piu))
    print(f'assets/web: {len(IMMAGINI)} immagini, {tot / 1e6:.1f} MB; fonts/: {len(CARATTERI)} file, {tot_f / 1e3:.0f} kB')


if __name__ == '__main__':
    main()
