# -*- coding: utf-8 -*-
"""
Crea plugin/benvegnu-installer.zip: un plugin WordPress che installa e configura il sito su un WordPress pulito
(tema Hello Elementor, Elementor, Ultimate Addons, Contact Form 7, impostazioni, template, pagine, header e footer,
menu, modulo). Si carica da Plugin > Aggiungi nuovo > Carica, poi Strumenti > Installa Benvegnù, un passo alla volta
nell'ordine. Dopo l'uso va disattivato ed eliminato.
Uso: python3 crea_installer.py   (dopo build.py, così i template sono quelli aggiornati)
"""
import glob
import os
import zipfile

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
OUT = os.path.join(RADICE, 'plugin', 'benvegnu-installer.zip')

with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(QUI, 'installer', 'benvegnu-installer.php'), 'benvegnu-installer/benvegnu-installer.php')
    z.write(os.path.join(QUI, 'installer', 'modulo-cf7.txt'), 'benvegnu-installer/modulo-cf7.txt')
    for f in sorted(glob.glob(os.path.join(RADICE, 'elementor-json', 'bvg-*.json'))):
        z.write(f, 'benvegnu-installer/template/' + os.path.basename(f))
print('scritto', OUT)
