# uso: python3 slice.py <screenshot.png> [altezza-pezzo] [larghezza] [cartella-uscita]
import os, sys, glob
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src=sys.argv[1]; step=int(sys.argv[2]) if len(sys.argv)>2 else 1800; w=int(sys.argv[3]) if len(sys.argv)>3 else 1000
OUT=sys.argv[4] if len(sys.argv)>4 else os.path.dirname(os.path.abspath(src))
im=Image.open(src).convert('RGB'); n=os.path.basename(src)[:-4]
for f in glob.glob(os.path.join(OUT, n + '-*.jpg')):
    os.remove(f)
i=0
for top in range(0,im.height,step):
    c=im.crop((0,top,im.width,min(im.height,top+step)))
    if c.width>w: c=c.resize((w,int(c.height*w/c.width)))
    c.save(f'{OUT}/{n}-{i}.jpg',quality=80); i+=1
print(n,i,im.size)
