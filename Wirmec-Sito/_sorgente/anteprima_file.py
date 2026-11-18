# -*- coding: utf-8 -*-
"""
Completa i link interni dell'anteprima (anteprima/*.html) perché si apra con un doppio clic.

build.py riscrive solo i link verso pagine con un nome senza trattino e senza parametri (`/azienda/`, `/contatti/#estero`):
Wirmec ha `/da-banco/` e `/controllo-qualita/`, e i link al modulo portano la linea scelta (`/contatti/?linea=...#richiesta`).
Questo script, lanciato dopo build.py, trasforma anche quelli nei file accanto (`03-da-banco.html#w15`,
`07-contatti.html?linea=...#richiesta`). Non tocca build.py, motore.py né i template Elementor e il fallback HTML.

Uso: python3 _sorgente/anteprima_file.py            (dopo python3 _sorgente/build.py)
"""
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
CARTELLA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(QUI), 'anteprima')


def main():
    file = sorted(f for f in os.listdir(CARTELLA) if re.match(r'\d\d-[a-z-]+\.html$', f))
    pagine = {('/' if f[3:-5] == 'home' else f'/{f[3:-5]}/'): f for f in file}
    totale = 0
    for f in file:
        p = os.path.join(CARTELLA, f)
        html = open(p, encoding='utf-8').read()

        def sost(m):
            nome = pagine.get(m.group(1))
            return f'href="{nome}{m.group(2) or ""}"' if nome else m.group(0)
        nuovo, n = re.subn(r'href="(/[a-z-]*/?)([?#][^"]*)?"', sost, html)
        if nuovo != html:
            open(p, 'w', encoding='utf-8').write(nuovo)
        totale += n
        resto = sorted(set(re.findall(r'href="(/[^"]*)"', nuovo)))
        if resto:
            print(f'{f}: link non riscritti (pagine fuori dal sito): {", ".join(resto)}')
    print(f'anteprima: {len(file)} pagine, link riscritti in questo passaggio: {totale}')


if __name__ == '__main__':
    main()
