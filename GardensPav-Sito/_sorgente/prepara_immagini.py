# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Gardens Pav in assets/web/ a partire da assets/originali/ (file scaricati dal sito attuale:
si leggono solo con PIL, lanciare con python3 -I).

Regole (specifica del 13 ottobre, paragrafo 15):
- mai più grandi dell'originale: ogni immagine viene solo ritagliata e ridotta, mai ingrandita;
- jpg qualità 82-85, progressivo; il logo resta il PNG originale 358 x 75 (non serve una versione monocroma: piede chiaro);
- render e disegni che stanno su una scheda #F2F1EE: ritaglio sul pezzo, proporzione 3:2, il bianco del fondo portato al
  grigio della scheda moltiplicando i pixel (si fa qui, non con mix-blend-mode nel CSS);
- foto di cantiere: ritaglio 4:3 (o il rapporto della cornice) attorno a un fuoco, alla larghezza che serve.

Le immagini della home riproducono quelle del prototipo finale (_prova/home-finale/img, stesse sorgenti e stessi ritagli).
Scrive _sorgente/immagini.json: per ogni file la sorgente, la misura nativa, la misura in uscita e dove si usa.

Uso:  python3 -I prepara_immagini.py            scrive o aggiorna i file dell'elenco
      python3 -I prepara_immagini.py --pulisci  in più toglie da assets/web i file che non sono nell'elenco
"""
import json
import os
import shutil
import sys

from PIL import Image, ImageChops

QUI = os.path.dirname(os.path.abspath(__file__))
ASSET = os.path.join(os.path.dirname(QUI), 'assets')
ORIG = os.path.join(ASSET, 'originali')
WEB = os.path.join(ASSET, 'web')
SCHEDA = (0xF2, 0xF1, 0xEE)        # --gpv-scheda
registro = {}


def _salva(im, nome, q):
    im.save(os.path.join(WEB, nome), 'JPEG', quality=q, optimize=True, progressive=True)


def _nota(nome, sorgente, uscita, uso):
    registro[nome] = {'da': sorgente, 'nativa': list(Image.open(os.path.join(ORIG, sorgente)).size),
                      'uscita': list(uscita), 'uso': uso}


def _bbox_non_bianco(im, soglia=238):
    return im.convert('L').point(lambda v: 255 if v < soglia else 0).getbbox()


def scheda(nome, sorgente, uso, rapporto=1.5, margine=0.07, maxw=640, riquadro=None):
    """Render o disegno per una scheda: ritaglio sul pezzo con un margine d'aria, tela 3:2 bianca, tinta #F2F1EE."""
    im = Image.open(os.path.join(ORIG, sorgente)).convert('RGB')
    if riquadro:
        im = im.crop(riquadro)
    x0, y0, x1, y1 = _bbox_non_bianco(im)
    w, h = x1 - x0, y1 - y0
    m = int(max(w, h) * margine)
    x0, y0, x1, y1 = x0 - m, y0 - m, x1 + m, y1 + m
    w, h = x1 - x0, y1 - y0
    if w / h < rapporto:                       # allarga il lato corto con il bianco del fondo
        nw = int(h * rapporto); x0 -= (nw - w) // 2; x1 = x0 + nw
    else:
        nh = int(w / rapporto); y0 -= (nh - h) // 2; y1 = y0 + nh
    tela = Image.new('RGB', (x1 - x0, y1 - y0), (255, 255, 255))
    tela.paste(im, (-x0, -y0))
    tela = ImageChops.multiply(tela, Image.new('RGB', tela.size, SCHEDA))
    if tela.width > maxw:
        tela = tela.resize((maxw, round(maxw * tela.height / tela.width)), Image.LANCZOS)
    _salva(tela, nome, 84)
    _nota(nome, sorgente, tela.size, uso)


def foto(nome, sorgente, uso, larghezza, rapporto=None, cx=0.5, cy=0.5, riquadro=None, q=82):
    """Foto o render a fondo bianco: riquadro fisso oppure ritaglio al rapporto voluto attorno al fuoco (cx, cy)."""
    im = Image.open(os.path.join(ORIG, sorgente)).convert('RGB')
    if riquadro:
        im = im.crop(riquadro)
    if rapporto:
        W, H = im.size
        w, h = (int(H * rapporto), H) if W / H > rapporto else (W, int(W / rapporto))
        x = int(min(max(cx * W - w / 2, 0), W - w))
        y = int(min(max(cy * H - h / 2, 0), H - h))
        im = im.crop((x, y, x + w, y + h))
    if im.width > larghezza:                   # mai oltre la misura nativa
        im = im.resize((larghezza, round(larghezza * im.height / im.width)), Image.LANCZOS)
    _salva(im, nome, q)
    _nota(nome, sorgente, im.size, uso)


# --------------------------------------------------------------------------------------------- elenco
def globali():
    shutil.copyfile(os.path.join(ORIG, 'logo-gardens-pav-358x75.png'), os.path.join(WEB, 'logo-gardens-pav.png'))
    _nota('logo-gardens-pav.png', 'logo-gardens-pav-358x75.png', (358, 75), 'testata 172 x 36 (136 a mobile), piede 172')


def home():
    s = 'home, scheda di famiglia 268 px a 1440 (231 a 1024, 116 sotto 900)'
    scheda('scheda-pista-self.jpg', 'schema-pista-self-450-500-esploso.jpg', s, margine=0.03, riquadro=(0, 0, 610, 330))
    scheda('scheda-portali.jpg', 'schema-portale-mod5-assonometria.jpg', s, margine=0.02)
    scheda('scheda-isola.jpg', 'render-isola-aspirazione-tipo-1.jpg', s)
    scheda('scheda-colori.jpg', 'schema-piattaforma-colorata-rosso.jpg', s, margine=0.04)
    scheda('scheda-rettangolari.jpg', 'render-vasca-rettangolare-550-proiezione.jpg', s)
    scheda('scheda-circolari.jpg', 'render-vasca-circolare-ombra.jpg', s, margine=0.10)
    scheda('scheda-prima-pioggia.jpg', 'render-impianto-prima-pioggia-proiezione.jpg', s, margine=0.03)
    scheda('scheda-dissabbiatore.jpg', 'render-dissabbiatore-frontale.jpg', s)
    scheda('scheda-separatore-oli.jpg', 'render-separatore-oli-ombra.jpg', s)
    scheda('scheda-separatore-grassi.jpg', 'render-separatore-grassi-ombra.jpg', s, margine=0.10)
    scheda('scheda-imhoff.jpg', 'render-vasca-imhoff-ombra.jpg', s)
    scheda('scheda-biologici.jpg', 'render-depuratore-biologico-frontale.jpg', s)

    c = 'home, In consegna e in cantiere, 308 x 231 a 1440'
    foto('consegna-autogru.jpg', 'foto-trasporto-vasca-autogru-cielo.jpg', c, 1000, 4 / 3, cx=0.45, q=84)
    foto('consegna-calata.jpg', 'foto-trasporto-vasche-autoarticolato.jpg', c, 720, 4 / 3, q=84)
    foto('consegna-lunga.jpg', 'foto-vasca-rettangolare-lunga-e-pozzetto-cantiere.jpg', c, 720, 4 / 3, q=84)
    foto('consegna-batteria.jpg', 'foto-vasche-rettangolari-batteria-cantiere.jpg', c, 720, 4 / 3, q=84)

    foto('prima-pioggia-percorso.jpg', 'render-impianto-prima-pioggia-frontale.jpg',
         'home, prima pioggia, 1040 x 436 a 1440', 1360, riquadro=(140, 80, 1500, 650))
    foto('pista-portale.jpg', 'foto-piattaforme-slide-2.jpg', 'home, misure e posa, 821 x 616 a 1440', 1232)

    f = 'home, posa in quattro fasi, 308 x 231 a 1440'
    foto('posa-1-tracciatura.jpg', 'realizzazione-san-giovanni-persiceto-bo-02-controllo-dimensioni-e-quote.jpg', f, 640, 4 / 3)
    foto('posa-2-vasca.jpg', 'realizzazione-abano-terme-pd-01-piano-di-posa-self.jpg', f, 640, 4 / 3)
    foto('posa-3-cordoli.jpg', 'realizzazione-biella-02-piano-di-posa-self.jpg', f, 640, 4 / 3)
    foto('posa-4-pannelli.jpg', 'realizzazione-grugliasco-to-01-posa-pista-self-mod-450.jpg', f, 640, 4 / 3)

    foto('avetrana-posa.jpg', 'realizzazione-avetrana-ta-carrozzo-06-posa-griglie-e-supporti.jpg',
         'home, cantieri per regione, 719 x 539 a 1440', 1200, 4 / 3, cx=0.62, q=84)
    foto('vasche-circolari-piazzale.jpg', 'foto-vasche-circolari-piazzale-panoramica.jpg',
         'home, contatto, 612 x 459 a 1440', 1280, 4 / 3, q=84)


# copertine dei cantieri: 4:3 attorno al fuoco, fino a 800 px (308 x 231 nel mosaico della home e nelle schede delle
# Realizzazioni: 2,6x su retina); dove la copertina del sito è debole si usa un'altra foto dello stesso cantiere
COPERTINE_DIVERSE = {'san-marino': 'realizzazione-san-marino-rossi-service-07.jpg'}
FUOCO_Y = {'rubano': 0.56}


def cantieri():
    for c in json.load(open(os.path.join(QUI, 'dati', 'cantieri.json'), encoding='utf-8')):
        foto(f'cantiere-{c["id"]}.jpg', COPERTINE_DIVERSE.get(c['id'], c['copertina']),
             'copertina del cantiere, 308 x 231 a 1440 (home e Realizzazioni)', 800, 4 / 3, cy=FUOCO_Y.get(c['id'], 0.5))


def main():
    os.makedirs(WEB, exist_ok=True)
    globali()
    home()
    cantieri()
    with open(os.path.join(QUI, 'immagini.json'), 'w', encoding='utf-8') as f:
        json.dump(registro, f, indent=1, ensure_ascii=False)
    for nome, v in registro.items():
        assert v['uscita'][0] <= v['nativa'][0] and v['uscita'][1] <= v['nativa'][1], f'{nome} ingrandita'
    altri = sorted(set(os.listdir(WEB)) - set(registro))
    if '--pulisci' in sys.argv:
        for nome in altri:
            os.remove(os.path.join(WEB, nome))
        print(len(altri), 'file vecchi tolti da assets/web')
    elif altri:
        print(len(altri), 'file in assets/web non prodotti da questo script (con --pulisci si tolgono)')
    print(len(registro), 'immagini scritte in', WEB)


if __name__ == '__main__':
    main()
