# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Gardens Pav in assets/web/ (dalle immagini in assets/originali/).
- foto: a colori, mai più grandi dell'originale, lato lungo al massimo 1600, jpg qualità 84;
  ritaglio solo dove serve un rapporto diverso
- render: ritagliati sul pezzo (soglia sul bianco) con un margine d'aria, ridotti alla misura d'uso;
  dove il render va su una fascia #EBECEB il file viene moltiplicato per quel grigio (il bianco diventa #EBECEB,
  niente riquadri bianchi incollati sul grigio, niente mix-blend-mode nel CSS)
- logo: l'originale per la testata; versione chiara per il piede grafite (il grigio del logo portato a bianco,
  l'arancio resta)
Scrive anche _sorgente/immagini.json con le misure finali e le quote ricalcolate sul ritaglio (le legge contenuti.py).
Uso: python3 prepara_immagini.py
"""
import json
import os
import shutil

from PIL import Image, ImageChops, ImageFilter, ImageOps

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
WEB = os.path.join(ASSET, 'web')
GRIGIO = (0xEB, 0xEC, 0xEB)

# nome web: (sorgente, rapporto o None, larghezza massima in uscita, fuoco x, fuoco y)
FOTO = {
    # home, apertura: 733 x 550 a 1440 (2x), 342 x 257 a 390
    'apertura-vasca-autogru.jpg': ('foto-trasporto-vasca-autogru-cielo.jpg', None, 1466, 0.5, 0.5),
    # home, realizzazioni: 624 x 468 a 1440 (2,05x)
    'realizzazione-altivole-tv.jpg': ('realizzazione-altivole-tv-pozzobon-03.jpg', None, 1280, 0.5, 0.5),
    # vasche, apertura: 720 x 540 a 1440 (2,2x); a tablet ritaglio 16:9 nel CSS (1024 x 576, 1,56x)
    'vasche-circolari-piazzale.jpg': ('foto-vasche-circolari-piazzale-panoramica.jpg', None, 1600, 0.5, 0.5),
    # vasche, rettangolari: 405 x 540 a 1440 (2,2x), nativa
    'vasca-1050-posa.jpg': ('foto-posa-vasca-1050-autogru-verticale.jpg', None, 901, 0.5, 0.5),
    # vasche, resine: 515 x 289 (2,1x) e 296 x 395 (2,3x, ritaglio 3:4 dall'alto)
    'resina-circolare.jpg': ('foto-vasca-circolare-interno-resina-rossa-a.jpg', None, 1100, 0.5, 0.5),
    'resina-rettangolare.jpg': ('foto-vasca-rettangolare-interno-resina-rossa-verticale.jpg', '3:4', 674, 0.5, 0.42),
    # depurazione: apertura 515 x 481 (2,1x), separatore oli 515 x 289 (2,1x)
    'depurazione-vasca-pozzetto.jpg': ('foto-vasca-rettangolare-lunga-e-pozzetto-cantiere.jpg', None, 1100, 0.5, 0.5),
    'separatore-oli-interno.jpg': ('foto-separatore-oli-interno-azzurro.jpg', None, 1100, 0.5, 0.5),
    # piattaforme: apertura 720 x 540 (2,2x), riscaldamento 515 x 351 (2,1x)
    'pista-self-spazzole.jpg': ('foto-piattaforme-slide-2.jpg', None, 1440, 0.5, 0.5),
    'piattaforma-riscaldata.jpg': ('foto-piattaforma-riscaldata-neve-frecce.jpg', None, 1100, 0.5, 0.5),
    # azienda: 624 x 438 (2,1x) e 515 x 411 (2,1x)
    'vasche-autoarticolato.jpg': ('foto-trasporto-vasche-autoarticolato.jpg', None, 1300, 0.5, 0.5),
    'vasche-batteria-cantiere.jpg': ('foto-vasche-rettangolari-batteria-cantiere.jpg', None, 1100, 0.5, 0.5),
}

# nome web: (sorgente, lato lungo in uscita, fondo, aria in px sull'originale)
RENDER = {
    # home, vasche: mostrato a 600 al massimo (1,45x), su #EBECEB
    'render-vasca-550.jpg': ('render-vasca-rettangolare-550-frontale.jpg', 867, GRIGIO, 20),
    # home, depurazione: riquadri 176 x 120 su bianco (oltre 2x)
    'render-dissabbiatore-400.jpg': ('render-dissabbiatore-frontale.jpg', 400, None, 12),
    'render-separatore-grassi-400.jpg': ('render-separatore-grassi.jpg', 400, None, 12),
    'render-imhoff-400.jpg': ('render-vasca-imhoff.jpg', 400, None, 12),
    'render-separatore-oli-400.jpg': ('render-separatore-oli.jpg', 400, None, 12),
    'render-separatore-oli-autorimesse-400.jpg': ('render-separatore-oli-ombra.jpg', 400, None, 12),
    'render-prima-pioggia-400.jpg': ('render-impianto-prima-pioggia-frontale.jpg', 400, None, 12),
    'render-depuratore-biologico-400.jpg': ('render-depuratore-biologico-frontale.jpg', 400, None, 12),
    # depurazione, schede: alla misura nativa del ritaglio (mai ingranditi); su #EBECEB dove la scheda è grigia
    'render-dissabbiatore-cls.jpg': ('render-dissabbiatore-frontale.jpg', 1600, GRIGIO, 20),
    'render-separatore-grassi.jpg': ('render-separatore-grassi.jpg', 1600, None, 20),
    'render-imhoff-cls.jpg': ('render-vasca-imhoff.jpg', 1600, GRIGIO, 20),
    'render-separatore-oli.jpg': ('render-separatore-oli.jpg', 1600, None, 20),
    'render-separatore-oli-autorimesse-cls.jpg': ('render-separatore-oli-ombra.jpg', 1600, GRIGIO, 20),
    'render-prima-pioggia.jpg': ('render-impianto-prima-pioggia-frontale.jpg', 1600, None, 20),
    'render-depuratore-biologico-cls.jpg': ('render-depuratore-biologico-frontale.jpg', 1600, GRIGIO, 20),
    # vasche, circolari: 260 x 330 su #EBECEB
    'render-vasca-circolare-cls.jpg': ('render-vasca-circolare.jpg', 1600, GRIGIO, 20),
}

# disegni dell'azienda: copiati tali e quali (sono già alla misura giusta, la ricompressione sporcherebbe le linee)
COPIE = {
    'schema-pista-self-450.jpg': 'schema-pista-self-450-pianta.jpg',
    'schema-pista-self-500.jpg': 'schema-pista-self-500-pianta.jpg',
    'schema-pista-self-500-doppia-griglia.jpg': 'schema-pista-self-500-doppia-griglia-pianta.jpg',
    'schema-portale-mod1.jpg': 'schema-portale-mod1-pianta.jpg',
    'schema-portale-mod2.jpg': 'schema-portale-mod2-pianta.jpg',
    'schema-portale-mod3.jpg': 'schema-portale-mod3-pianta.jpg',
    'schema-portale-mod4.jpg': 'schema-portale-mod4-pianta.jpg',
    'schema-portale-mod5.jpg': 'schema-portale-mod5-pianta.jpg',
    'esempio-di-posa.jpg': 'testo-in-immagine-esempio-di-posa.jpg',
}

# campioni di colore: quadrati 400 x 400 ritagliati dalle piante colorate sul giunto e sul grigliato
CAMPIONI = {
    'colore-rosso.jpg': ('schema-piattaforma-colorata-rosso.jpg', (300, 300, 700, 700)),
    'colore-verde.jpg': ('schema-piattaforma-colorata-verde.jpg', (300, 300, 700, 700)),
    'colore-giallo.jpg': ('schema-piattaforma-colorata-giallo.jpg', (400, 330, 800, 730)),
    'colore-marrone.jpg': ('schema-piattaforma-colorata-marrone.jpg', (400, 330, 800, 730)),
}

# accessori: render ritagliato sul pezzo, al centro di un quadrato 480 x 480, portato su #EBECEB
ACCESSORI = {
    'accessorio-isola.jpg': 'render-isola-aspirazione-tipo-1.jpg',
    'accessorio-trave.jpg': 'render-trave-di-rialzo-h30.jpg',
}

# copertine dei cantieri: 4:3, lato lungo al massimo 1000 (296 x 222 nella griglia, 400 x 300 nella striscia)
COPERTINE_DIVERSE = {'san-marino': 'realizzazione-san-marino-rossi-service-07.jpg'}
FUOCO_Y = {'rubano': 0.56}

# faccia frontale della vasca 550 nel file originale (pixel x): serve a mettere la quota "550 cm" sotto lo spigolo vero
FACCIA_550 = (476, 1117)


def ritaglia(im, ratio, fx=0.5, fy=0.5):
    if not ratio:
        return im
    rw, rh = map(int, ratio.split(':'))
    w, h = im.size
    target = rw / rh
    nw, nh = (int(h * target), h) if w / h > target else (w, int(w / target))
    x = int(min(max(fx * w - nw / 2, 0), w - nw))
    y = int(min(max(fy * h - nh / 2, 0), h - nh))
    return im.crop((x, y, x + nw, y + nh))


def foto(src, dst, ratio, out_w, fx, fy):
    im = ritaglia(Image.open(src).convert('RGB'), ratio, fx, fy)
    out_w = min(out_w, im.size[0])                    # mai più grande dell'originale
    out_h = round(out_w * im.size[1] / im.size[0])
    if out_w != im.size[0]:
        im = im.resize((out_w, out_h), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=84, optimize=True, progressive=True)
    return out_w, out_h


def riquadro_pezzo(im, aria):
    g = ImageOps.grayscale(im)
    # il filtro mediano toglie i puntini isolati (nel render del dissabbiatore un pixel a 240 px dal pezzo)
    x0, y0, x1, y1 = ImageOps.invert(g).point(lambda v: 255 if v > 12 else 0).filter(ImageFilter.MedianFilter(5)).getbbox()
    return (max(0, x0 - aria), max(0, y0 - aria), min(im.size[0], x1 + aria), min(im.size[1], y1 + aria))


def render(src, dst, lato, fondo, aria):
    im = Image.open(src).convert('RGB')
    box = riquadro_pezzo(im, aria)
    im = im.crop(box)
    scala = min(1.0, lato / max(im.size))
    if scala < 1:
        im = im.resize((round(im.size[0] * scala), round(im.size[1] * scala)), Image.LANCZOS)
    if fondo:
        im = ImageChops.multiply(im, Image.new('RGB', im.size, fondo))
    im.save(dst, 'JPEG', quality=85, optimize=True, progressive=True)
    return box, im.size


def quadrato(src, dst, lato=480, fondo=GRIGIO, aria=12, margine=0.08):
    im = Image.open(src).convert('RGB')
    im = im.crop(riquadro_pezzo(im, aria))
    utile = round(lato * (1 - 2 * margine))
    scala = min(utile / im.size[0], utile / im.size[1], 1.0)
    im = im.resize((round(im.size[0] * scala), round(im.size[1] * scala)), Image.LANCZOS)
    tela = Image.new('RGB', (lato, lato), (255, 255, 255))
    tela.paste(im, ((lato - im.size[0]) // 2, (lato - im.size[1]) // 2))
    tela = ImageChops.multiply(tela, Image.new('RGB', tela.size, fondo))
    tela.save(dst, 'JPEG', quality=85, optimize=True, progressive=True)
    return tela.size


def copertina(src, dst, fy=0.5, lato=1000):
    im = ritaglia(Image.open(src).convert('RGB'), '4:3', 0.5, fy)
    if im.size[0] > lato:
        im = im.resize((lato, round(lato * 3 / 4)), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=80, optimize=True, progressive=True)
    return im.size


def logo_chiaro(src, dst):
    """Il grigio del logo (lettere 'opere in calcestruzzo', contorno del marchio) diventa bianco; l'arancio resta."""
    logo = Image.open(src).convert('RGBA')
    px = logo.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            r, g, b, a = px[x, y]
            if a and max(r, g, b) - min(r, g, b) < 48:
                px[x, y] = (255, 255, 255, a)
    logo.save(dst, optimize=True)


def main():
    os.makedirs(WEB, exist_ok=True)
    for f in os.listdir(WEB):
        os.remove(os.path.join(WEB, f))
    misure = {}
    for nome, (src, ratio, w, fx, fy) in FOTO.items():
        misure[nome] = foto(os.path.join(ORIG, src), os.path.join(WEB, nome), ratio, w, fx, fy)
    for nome, (src, lato, fondo, aria) in RENDER.items():
        box, dim = render(os.path.join(ORIG, src), os.path.join(WEB, nome), lato, fondo, aria)
        misure[nome] = dim
        if nome == 'render-vasca-550.jpg':
            larg = box[2] - box[0]
            misure['quota-550'] = [round((FACCIA_550[0] - box[0]) / larg * 100, 2),
                                   round((box[2] - FACCIA_550[1]) / larg * 100, 2)]
    for nome, src in COPIE.items():
        shutil.copyfile(os.path.join(ORIG, src), os.path.join(WEB, nome))
        misure[nome] = list(Image.open(os.path.join(WEB, nome)).size)
    for nome, (src, box) in CAMPIONI.items():
        im = Image.open(os.path.join(ORIG, src)).convert('RGB').crop(box)
        im.save(os.path.join(WEB, nome), 'JPEG', quality=85, optimize=True, progressive=True)
        misure[nome] = list(im.size)
    for nome, src in ACCESSORI.items():
        misure[nome] = quadrato(os.path.join(ORIG, src), os.path.join(WEB, nome))
    cantieri = json.load(open(os.path.join(QUI, 'dati', 'cantieri.json'), encoding='utf-8'))
    for c in cantieri:
        src = COPERTINE_DIVERSE.get(c['id'], c['copertina'])
        misure[f'cantiere-{c["id"]}.jpg'] = copertina(os.path.join(ORIG, src), os.path.join(WEB, f'cantiere-{c["id"]}.jpg'),
                                                      FUOCO_Y.get(c['id'], 0.5))
    Image.open(os.path.join(ORIG, 'logo-gardens-pav-358x75.png')).save(os.path.join(WEB, 'logo-gardens-pav.png'), optimize=True)
    logo_chiaro(os.path.join(ORIG, 'logo-gardens-pav-358x75.png'), os.path.join(WEB, 'logo-gardens-pav-chiaro.png'))
    misure['logo-gardens-pav.png'] = misure['logo-gardens-pav-chiaro.png'] = [358, 75]
    with open(os.path.join(QUI, 'immagini.json'), 'w', encoding='utf-8') as f:
        json.dump(misure, f, indent=1)
    for nome in sorted(misure):
        print(nome, misure[nome])
    print(len(os.listdir(WEB)), 'immagini in', WEB)


if __name__ == '__main__':
    main()
