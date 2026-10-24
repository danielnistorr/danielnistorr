# -*- coding: utf-8 -*-
"""
Crea plugin/fmsistemi-installer.zip: un plugin WordPress che installa e configura la home su un WordPress pulito
(tema Hello Elementor, Elementor, Ultimate Addons, impostazioni, i 3 template con i testi alternativi delle foto,
pagina Home, header e footer, menu).
Si carica da Plugin > Aggiungi nuovo > Carica plugin, poi Strumenti > Installa FM Sistemi, un passo alla volta
nell'ordine. Dopo l'uso va disattivato ed eliminato.
Uso: python3 crea_installer.py            (dopo build.py, così i template sono quelli aggiornati)
     python3 crea_installer.py --json DIR --out FILE.zip   (per una prova, per esempio con la build di _prova)
"""
import argparse
import glob
import os
import zipfile

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)

ap = argparse.ArgumentParser()
ap.add_argument('--json', default=os.path.join(RADICE, 'elementor-json'), help='cartella dei template (fms-*.json)')
ap.add_argument('--out', default=os.path.join(RADICE, 'plugin', 'fmsistemi-installer.zip'))
a = ap.parse_args()
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
template = sorted(glob.glob(os.path.join(a.json, 'fms-*.json')))
if len(template) != 3:
    raise SystemExit(f'attesi 3 template in {a.json}, trovati {len(template)}')
with zipfile.ZipFile(a.out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(QUI, 'installer', 'fmsistemi-installer.php'), 'fmsistemi-installer/fmsistemi-installer.php')
    for f in template:
        z.write(f, 'fmsistemi-installer/template/' + os.path.basename(f))
    # i testi alternativi delle foto: l'installatore li scrive nella libreria media dopo l'import
    z.write(os.path.join(a.json, 'testi-alternativi-immagini.txt'), 'fmsistemi-installer/testi-alternativi.txt')
print('scritto', a.out, '(' + ', '.join(os.path.basename(f) for f in template) + ')')
