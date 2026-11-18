# -*- coding: utf-8 -*-
"""
Estrae il catalogo (27 articoli, 403 colori) dalla home statica approvata, sito/index.html, e lo scrive in
_sorgente/catalogo.json. È lo stesso oggetto D che la pagina statica usa nel suo script (nomi, materiali, spessori,
disegni, colori, scansioni, toni del drappo tarati da _prova/script/finale_drappo.py): nessun dato nuovo.
I percorsi delle immagini perdono il prefisso "img/": contenuti.py li completa con la base delle immagini.
Uso: python3 estrai_catalogo.py
"""
import json
import os
import re

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)


def main():
    html = open(os.path.join(RADICE, 'sito', 'index.html'), encoding='utf-8').read()
    mo = re.search(r'var D=(\{.*?\});\n', html, re.S)
    if not mo:
        raise SystemExit('oggetto D non trovato in sito/index.html')
    d = json.loads(mo.group(1))
    colori = 0
    for a in d['articoli']:
        for c in a['c']:
            if not c['i'].startswith('img/'):
                raise SystemExit(f'percorso inatteso: {c["i"]}')
            c['i'] = c['i'][4:]
            colori += 1
    if len(d['articoli']) != 27 or colori != 403:
        raise SystemExit(f'conteggio inatteso: {len(d["articoli"])} articoli, {colori} colori')
    with open(os.path.join(QUI, 'catalogo.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, separators=(',', ':'))
        f.write('\n')
    print(f'catalogo.json: {len(d["articoli"])} articoli, {colori} colori')


if __name__ == '__main__':
    main()
