# Copia gli screenshot di prova nel repository come JPEG: uso python3 esporta.py <cartella-sito>
# _prova/shots/el-NN-pagina-vista.png -> screenshot/elementor/NN-pagina-vista.jpg (ht- -> screenshot/fallback/)
import glob, os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
sito = os.path.abspath(sys.argv[1])
for sub, pref in (('elementor', 'el-'), ('fallback', 'ht-')):
    dest = os.path.join(sito, 'screenshot', sub)
    os.makedirs(dest, exist_ok=True)
    for f in glob.glob(os.path.join(dest, '*.jpg')):
        os.remove(f)
    for f in sorted(glob.glob(os.path.join(sito, '_prova', 'shots', pref + '*.png'))):
        Image.open(f).convert('RGB').save(os.path.join(dest, os.path.basename(f)[len(pref):-4] + '.jpg'),
                                          'JPEG', quality=80, optimize=True, progressive=True)
    print(sub, len(os.listdir(dest)), 'file')
