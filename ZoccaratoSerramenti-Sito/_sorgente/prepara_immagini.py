# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Zoccarato Serramenti in assets/web/ partendo da assets/originali/ (foto scaricate dal sito
attuale, 01) e dalle liste della specifica (_prova/spec.md, paragrafo 16).

Regole:
- mai più grandi dell'originale: si ritaglia alla proporzione della cella e si riduce, non si ingrandisce mai;
- colori come sono (foto di cantiere), nessun filtro; il bianco e nero solo dove è già nell'originale (camion del 1974);
- JPEG qualità 84, progressivo; le foto col timbro data della fotocamera non entrano (escluse già da GALLERIE);
- le gallerie (pagina Lavori) escono da contenuti.GALLERIE, la stessa struttura che dà i conteggi di home e pagine.

Uso: python3 -I _sorgente/prepara_immagini.py   (legge file scaricati: con -I, senza cartelle di lavoro nel percorso)
"""
import glob
import os
import sys

from PIL import Image

QUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QUI)                     # contenuti.py (GALLERIE): codice nostro, accanto a questo file
import contenuti as c                       # noqa: E402

ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
WEB = os.path.join(ASSET, 'web')
QUALITA = 84


def originale(nome):
    """File originale da un nome breve (abitazioni-106) o da un nome intero (azienda-flotta-autogru-camion.jpg)."""
    if nome.endswith('.jpg'):
        return os.path.join(ORIG, nome)
    trovati = glob.glob(os.path.join(ORIG, f'*-{nome}-*.jpg'))
    trovati = [f for f in trovati if os.path.basename(f).split('-', 1)[1].startswith(nome + '-')]
    if len(trovati) != 1:
        raise SystemExit(f'originale non univoco per {nome}: {trovati}')
    return trovati[0]


def ritaglia(im, r=None, cx=.5, cy=.5, box=None):
    """Ritaglio alla proporzione r (larghezza/altezza) intorno al fuoco cx, cy; box = riquadro da togliere prima."""
    if box:
        im = im.crop(box)
    if not r:
        return im
    w, h = im.size
    if w / h > r:
        nw = round(h * r)
        x0 = min(max(0, round(cx * w - nw / 2)), w - nw)
        return im.crop((x0, 0, x0 + nw, h))
    nh = round(w / r)
    y0 = min(max(0, round(cy * h - nh / 2)), h - nh)
    return im.crop((0, y0, w, y0 + nh))


def riduci(im, larghezza):
    """Riduce alla larghezza indicata solo se l'immagine è più larga: mai ingrandire."""
    if larghezza and im.width > larghezza:
        im = im.resize((larghezza, round(im.height * larghezza / im.width)), Image.LANCZOS)
    return im


def salva(im, nome, sorgente):
    out = os.path.join(WEB, nome)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    src = Image.open(sorgente)
    assert im.width <= src.width and im.height <= src.height, f'{nome}: più grande dell\'originale'
    im.convert('RGB').save(out, quality=QUALITA, optimize=True, progressive=True)
    return im.size


def fai(nome, sorgente, r=None, larghezza=None, cx=.5, cy=.5, box=None):
    f = originale(sorgente)
    im = riduci(ritaglia(Image.open(f).convert('RGB'), r, cx, cy, box), larghezza)
    return salva(im, nome, f)


# ---------------------------------------------------------------------------------------------
# Home e parti comuni (home finale: _prova/script/fiancata_immagini.py e finale_immagini.py)
# nome web: (originale, proporzione o None, larghezza massima o None, fuoco x, fuoco y[, riquadro da togliere])
# ---------------------------------------------------------------------------------------------
HOME = {
    'logo.jpg': ('grafica-logo.jpg', None, None, .5, .5),
    # flotta: tolto il muro a destra (x > 820); la sponda "ZOCCARATO" sta tra x 60 e 300, il primo furgone tra 462 e 636
    'flotta-autogru.jpg': ('azienda-flotta-autogru-camion.jpg', None, None, .5, .5, (0, 0, 820, 600)),
    'casa-finestre.jpg': ('abitazioni-106', 4 / 3, None, .5, .5),
    'casa-scorrevoli.jpg': ('scorrevoli-101', 4 / 3, None, .5, .5),
    'casa-oscuranti.jpg': ('abitazioni-115', 4 / 3, None, .5, .5),
    'casa-portoncini.jpg': ('portoncini-10', 3 / 4, None, .5, .5),
    'casa-porte-interne.jpg': ('abitazioni-130', 3 / 4, None, .5, .5),
    'casa-pergole.jpg': ('pensiline-14a', 3 / 4, None, .42, .5),
    'casa-speciali.jpg': ('speciali-102', 3 / 4, None, .62, .5),
    'ind-commerciali.jpg': ('commerciali-101', 4 / 3, None, .5, .5),
    'ind-pensiline.jpg': ('commerciali-109', 4 / 3, None, .5, .5),
    'ind-monoblocchi.jpg': ('monoblocchi-38', 4 / 3, None, .5, .5),
    'lav-bovindo.jpg': ('abitazioni-109', 4 / 3, None, .5, .5),
    'lav-inglesine.jpg': ('abitazioni-128', 3 / 4, None, .5, .5),
    'lav-timpano.jpg': ('abitazioni-9', 4 / 3, None, .56, .5),
    'lav-veranda-bronzo.jpg': ('scorrevoli-114', 3 / 4, None, .5, .5),
    'lav-persiane-scorrevoli.jpg': ('oscuranti-113', 3 / 4, None, .5, .5),
    'lav-copertura-vetrata.jpg': ('speciali-104', 4 / 3, None, .5, .5),
    'lav-vetrata-bar.jpg': ('commerciali-116', 3 / 4, None, .5, .5),
    'lav-cancello.jpg': ('speciali-108', 4 / 3, None, .5, .5),
    'furto-serranda.jpg': ('azienda-effrazioni-01-serranda-divelta.jpg', 4 / 3, None, .5, .5),
    'furto-porta.jpg': ('azienda-effrazioni-03-porta-ripristinata.jpg', None, None, .5, .5),
    # bordo della scansione tolto prima del ritaglio
    'storia-1974.jpg': ('azienda-storia-1-camion-struttura-ferro.jpg', 4 / 3, None, .5, .5, (16, 8, 944, 752)),
    'sede-furgoni.jpg': ('azienda-flotta-2-sede-dall-alto.jpg', 4 / 3, None, .55, .5),
}

# miniature quadrate della scheda del sopralluogo (320 px da ritagli di 600-750 px); nessuna ripete una foto della home
MINI = {
    'm-finestre.jpg': ('abitazioni-107', .5, .5),
    'm-scorrevoli.jpg': ('scorrevoli-104', .5, .5),
    'm-oscuranti.jpg': ('oscuranti-07', .5, .5),
    'm-portoncini.jpg': ('portoncini-102', .5, .45),
    'm-pergole.jpg': ('pensiline-14b', .4, .5),
    'm-speciali.jpg': ('speciali-103', .45, .5),
    'm-vetrine.jpg': ('commerciali-112', .5, .5),
    'm-monoblocchi.jpg': ('monoblocchi-34', .32, .5),
}

# ---------------------------------------------------------------------------------------------
# Pagine interne (specifica 16.1): foto delle fiancate, delle schede delle lavorazioni, di Chi siamo
# ---------------------------------------------------------------------------------------------
PAGINE_INTERNE = {
    'apre-casa.jpg': ('home-02-scorrevole-legno.jpg', None, 1280, .5, .5, (160, 0, 1520, 850)),
    'apre-aziende.jpg': ('home-03-stazione-servizio.jpg', None, 1280, .5, .5, (160, 0, 1520, 850)),
    'apre-lavori.jpg': ('abitazioni-109', None, None, .5, .5, (0, 62, 1000, 687)),
    'apre-furto.jpg': ('azienda-effrazioni-02-vetrata-a-terra.jpg', None, None, .5, .5, (0, 62, 1000, 687)),
    'apre-storia.jpg': ('azienda-storia-1-camion-struttura-ferro.jpg', None, None, .5, .5, (0, 67, 1000, 692)),
    'apre-contatti.jpg': ('azienda-flotta-3-furgoni-piazzale.jpg', None, None, .5, .5, (0, 103, 899, 665)),
    'storia-1982.jpg': ('azienda-storia-2-aerea-sede.jpg', None, 800, .5, .5, (0, 8, 1000, 1008)),
    'flotta-autogru-43.jpg': ('azienda-flotta-autogru-camion.jpg', None, None, .5, .5, (0, 0, 800, 600)),
    'flotta-furgoni.jpg': ('azienda-flotta-3-furgoni-piazzale.jpg', None, None, .5, .5, (0, 47, 899, 721)),
}

# foto delle schede delle lavorazioni (specifica 8 e 9): orizzontali 4:3 a 800 px, verticali 3:4 a 600 px
SCHEDE = {
    'finestre': [('abitazioni-106', 'O'), ('abitazioni-108', 'O'), ('abitazioni-9', 'O'), ('abitazioni-119', 'O')],
    'scorrevoli': [('scorrevoli-101', 'O'), ('scorrevoli-102', 'O'), ('scorrevoli-105', 'O'), ('abitazioni-5', 'O')],
    'oscuranti': [('abitazioni-115', 'O'), ('oscuranti-106', 'O'), ('oscuranti-108', 'O'), ('oscuranti-18', 'O')],
    'portoncini': [('portoncini-10', 'V'), ('portoncini-16', 'V'), ('portoncini-42', 'V')],
    'porte-interne': [('abitazioni-130', 'V'), ('porte-interne-101', 'V'), ('porte-interne-33', 'V')],
    'pergole': [('pensiline-14a', 'O'), ('pensiline-102', 'O'), ('pensiline-103', 'O'), ('pensiline-101', 'O')],
    'speciali': [('speciali-102', 'O'), ('speciali-105', 'O'), ('speciali-108', 'O'), ('speciali-13a', 'O')],
    'commerciali': [('commerciali-101', 'O'), ('commerciali-112', 'O'), ('commerciali-105', 'O'), ('commerciali-114', 'O')],
    'pensiline': [('commerciali-109', 'O'), ('pensiline-14d', 'O'), ('pensiline-14f', 'O'), ('commerciali-108', 'O')],
    'monoblocchi': [('monoblocchi-38', 'O'), ('monoblocchi-34', 'O'), ('monoblocchi-35', 'O')],
}
FUOCO_X = {'monoblocchi-34': .32}


def main():
    os.makedirs(WEB, exist_ok=True)
    fatte = []
    for nome, v in list(HOME.items()) + list(PAGINE_INTERNE.items()):
        src, r, larg, cx, cy = v[:5]
        fatte.append((nome, fai(nome, src, r, larg, cx, cy, v[5] if len(v) > 5 else None)))
    for nome, (src, cx, cy) in MINI.items():
        fatte.append((nome, fai(nome, src, 1, 320, cx, cy)))
    for ancora, foto in SCHEDE.items():
        for i, (src, o) in enumerate(foto, 1):
            r, larg = (4 / 3, 800) if o == 'O' else (3 / 4, 600)
            nome = f'fam-{ancora}-{i}.jpg'
            fatte.append((nome, fai(nome, src, r, larg, FUOCO_X.get(src, .5), .5)))
    # gallerie: il file grande per il lightbox alla sua misura (fino a 1000 px) e la miniatura ritagliata
    for ancora, foto in c.GALLERIE.items():
        for nome, o, _, _ in foto:
            fatte.append((f'g/{nome}.jpg', fai(f'g/{nome}.jpg', nome, None, 1000)))
            r, larg = (4 / 3, 520) if o == 'O' else (3 / 4, 420)
            fatte.append((f'g/{nome}-p.jpg', fai(f'g/{nome}-p.jpg', nome, r, larg, FUOCO_X.get(nome, .5), .5)))
    # niente file vecchi rimasti da una lista precedente
    attese = {n for n, _ in fatte}
    for f in glob.glob(os.path.join(WEB, '**', '*.jpg'), recursive=True):
        if os.path.relpath(f, WEB) not in attese:
            os.remove(f)
    for nome, dim in fatte:
        print(f'{nome}: {dim[0]}x{dim[1]}')
    print(f'{len(fatte)} immagini in {WEB}, gallerie {c.TOTALE_FOTO} foto')


if __name__ == '__main__':
    main()
