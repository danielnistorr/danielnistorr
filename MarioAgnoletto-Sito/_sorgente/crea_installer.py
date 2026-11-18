# -*- coding: utf-8 -*-
"""
Crea plugin/agnoletto-installer.zip: un plugin WordPress che installa e configura la home su un WordPress pulito
(tema Hello Elementor, Elementor, Ultimate Addons, impostazioni, i file di assets/web nella cartella del sito,
i 3 template con i testi alternativi delle foto, pagina Home, header e footer, menu).
Si carica da Plugin > Aggiungi nuovo > Carica plugin, poi Strumenti > Installa Mario Agnoletto, un passo alla volta
nell'ordine. Dopo l'uso va disattivato ed eliminato.
Il passo "File del sito" copia assets/web in wp-content/uploads/mario-agnoletto/ e l'import riscrive la base delle
immagini dei template (scritta in base.txt) con quella cartella: la home non dipende da GitHub né da altri domini.
Uso: python3 crea_installer.py            (dopo build.py, così i template sono quelli aggiornati)
     python3 crea_installer.py --json DIR --base URL --out FILE.zip   (per una prova, con un'altra build)
"""
import argparse
import glob
import os
import sys
import zipfile

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, QUI)
import contenuti as c   # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--json', default=os.path.join(RADICE, 'elementor-json'), help='cartella dei template (mag-*.json)')
ap.add_argument('--base', default=c.BASE_PREDEFINITA, help='base delle immagini con cui sono stati costruiti i template')
ap.add_argument('--out', default=os.path.join(RADICE, 'plugin', 'agnoletto-installer.zip'))
a = ap.parse_args()
os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
template = sorted(glob.glob(os.path.join(a.json, 'mag-*.json')))
if len(template) != 3:
    raise SystemExit(f'attesi 3 template in {a.json}, trovati {len(template)}')
for f in template:
    if a.base not in open(f, encoding='utf-8').read() and 'header' not in f:
        raise SystemExit(f'{os.path.basename(f)}: non contiene la base {a.base}')
WEB = os.path.join(RADICE, 'assets', 'web')
n = 0
with zipfile.ZipFile(a.out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(os.path.join(QUI, 'installer', 'agnoletto-installer.php'), 'agnoletto-installer/agnoletto-installer.php')
    for f in template:
        z.write(f, 'agnoletto-installer/template/' + os.path.basename(f))
    # i testi alternativi delle foto: l'installatore li scrive nella libreria media dopo l'import
    z.write(os.path.join(a.json, 'testi-alternativi-immagini.txt'), 'agnoletto-installer/testi-alternativi.txt')
    z.writestr('agnoletto-installer/base.txt', a.base + '\n')
    for root, _, files in os.walk(WEB):
        for fn in sorted(files):
            p = os.path.join(root, fn)
            z.write(p, 'agnoletto-installer/assets/' + os.path.relpath(p, WEB).replace(os.sep, '/'))
            n += 1
print('scritto', a.out, '(' + ', '.join(os.path.basename(f) for f in template) + f', {n} file di assets/web)')
