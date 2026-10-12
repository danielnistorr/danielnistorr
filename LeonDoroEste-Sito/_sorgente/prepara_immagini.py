# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Leon d'Oro in assets/web/ (specifica, paragrafo 15).

Regole:
- mai più grandi del ritaglio: ogni file esce alla misura del ritaglio o più piccolo, e il sito lo mostra al massimo a
  scala 1,00 (controllato a 1440, 1024 e 390);
- bilanciamento del bianco come nel prototipo approvato (giro 2, "l'oggetto"): una zona che nella realtà è bianca (tenda
  della pensilina, tovaglia, muro, ceramica della targa, strada bianca) viene portata allo stesso bianco caldo, R/G 1,04 e
  B/G 0,94, con un guadagno sul rosso e uno sul blu; nessuna curva, nessun filtro, nessuna saturazione. Dove la luce è
  calda di suo (la facciata di sera) la correzione è parziale ("forza");
- i fotogrammi del video del cliente si tagliano sopra il marchio in basso a destra (y 850);
- la cartolina in scala di grigi, con autocontrasto leggero;
- logo: il tratto del leone e della scritta estratto dalla fetta 311 x 231 del sito attuale, in verde persiana e in bianco.

Sorgenti: assets/originali (sito attuale), assets/esterne (Regione Veneto, video "Emozioni e sapori" del cliente, cartolina
del blog Micro Storie del Commercio; manifest.json in ogni cartella). I tre fotogrammi del video presi al secondo esatto
(facciata 213,28 s, targa 219,16 s, porta 213,6 s) sono in assets/esterne/video-emozioni-e-sapori/fotogrammi/.

Uso: python3 -I prepara_immagini.py            (scrive assets/web/ e assets/web/ritagli.json)
"""
import json
import os
import sys

from PIL import Image, ImageOps, ImageStat

QUI = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(QUI), 'assets')
WEB = os.path.join(ASSETS, 'web')
VIDEO = 'esterne/video-emozioni-e-sapori/'
FOTOGRAMMI = VIDEO + 'fotogrammi/'
CARTOLINA = 'esterne/microstorie-commercio/cartolina-trattoria-al-leon-doro-viale-restara.jpg'

BIANCO = (1.04, 0.94)      # R/G e B/G del bianco di riferimento, lo stesso per tutte le foto a colori
BANDA_VIDEO = 88           # bande nere dei fotogrammi 1920 x 1080 (contenuto 1920 x 904)
QUALITA = 84               # jpg: 84 per le foto a colori, 82 per la cartolina in grigio

VERDE = (0x26, 0x3F, 0x40)  # verde persiana #263F40
BIANCO_PIENO = (255, 255, 255)


def apri(rel):
    im = Image.open(os.path.join(ASSETS, rel)).convert('RGB')
    if im.size == (1920, 1080):                  # fotogramma con le bande nere: resta il contenuto 1920 x 904
        im = im.crop((0, BANDA_VIDEO, 1920, BANDA_VIDEO + 904))
    return im


def rapporti(im, zona):
    r, g, b = ImageStat.Stat(im.crop(zona)).mean
    return r / g, b / g


def guadagni(im, zona, forza=1.0):
    rg, bg = rapporti(im, zona)
    return (BIANCO[0] / rg) ** forza, (BIANCO[1] / bg) ** forza


def bilancia(im, gr, gb):
    r, g, b = im.split()
    r = r.point(lambda v: min(255, round(v * gr)))
    b = b.point(lambda v: min(255, round(v * gb)))
    return Image.merge('RGB', (r, g, b))


REGISTRO = {}


def salva(im, nome, larghezza=None, q=QUALITA):
    if larghezza and im.width > larghezza:
        im = im.resize((larghezza, round(im.height * larghezza / im.width)), Image.LANCZOS)
    im.save(os.path.join(WEB, nome), quality=q, optimize=True, progressive=True)
    return list(im.size)


def foto(nome, sorgente, ritaglio, larghezza=None, zona=None, forza=1.0, gains=None, uso=''):
    """Una foto a colori: bilanciamento (zona bianca o guadagni dati), ritaglio, misura massima."""
    im = apri(sorgente)
    voce = {'sorgente': sorgente, 'ritaglio': list(ritaglio), 'uso': uso}
    if zona:
        gr, gb = guadagni(im, zona, forza)
        voce.update(zona_bianca=list(zona), forza=forza, prima_RG_BG=[round(x, 3) for x in rapporti(im, zona)])
        im = bilancia(im, gr, gb)
        voce['dopo_RG_BG'] = [round(x, 3) for x in rapporti(im, zona)]
        voce['guadagni_R_B'] = [round(gr, 3), round(gb, 3)]
    elif gains:
        im = bilancia(im, *gains)
        voce['guadagni_R_B'] = [round(g, 3) for g in gains]
    else:
        voce['nota'] = 'senza bilanciamento: zona bianca da scegliere sul provino prima della pagina'
    voce['misura_file'] = salva(im.crop(ritaglio), nome, larghezza)
    REGISTRO[nome] = voce
    return voce


def grigio(nome, ritaglio, larghezza, uso=''):
    im = ImageOps.autocontrast(ImageOps.grayscale(apri(CARTOLINA)), cutoff=0.3).convert('RGB')
    REGISTRO[nome] = {'sorgente': CARTOLINA, 'ritaglio': list(ritaglio), 'uso': uso, 'nota': 'scala di grigi, autocontrasto 0,3 %',
                      'misura_file': salva(im.crop(ritaglio), nome, larghezza, q=82)}


def logo(nome, colore):
    """Tratto nero della fetta 311 x 231 (leone e scritta) in colore pieno, il resto trasparente; ingrandito 3 volte con
    Lanczos solo per avere un bordo morbido: il file serve a 134 x 56 (testata) e 153 x 64 (piede), cioè sotto i pixel veri."""
    im = Image.open(os.path.join(ASSETS, 'originali/grafica/logo-leone-su-foto-311x231.jpg')).convert('L')
    im = im.crop((28, 62, 292, 192))
    im = im.resize((im.width * 3, im.height * 3), Image.LANCZOS)
    alfa = im.point(lambda v: max(0, min(255, int((150 - v) * 255 / 90))))
    out = Image.new('RGBA', im.size, colore + (0,))
    out.putalpha(alfa)
    out = out.crop(out.getbbox())
    out.save(os.path.join(WEB, nome), optimize=True)
    REGISTRO[nome] = {'sorgente': 'originali/grafica/logo-leone-su-foto-311x231.jpg', 'misura_file': list(out.size),
                      'nota': 'tratto estratto dalla foto; il vettoriale va chiesto al cliente'}


def main():
    os.makedirs(WEB, exist_ok=True)

    # ---- home (file del prototipo approvato, giro 2 "l'oggetto") ----
    # facciata di sera, fotogramma a 213,28 s: zona bianca la tenda della pensilina, forza 0,75 (il muro resta giallo)
    fac = foto('facciata-largo.jpg', FOTOGRAMMI + 'facciata-213.28s.png', (240, 0, 1920, 826),
               zona=(650, 522, 1150, 562), forza=0.75, uso='home H1, 1440 e 1024 (sfondo, larghezza massima 1680)')
    foto('facciata-alto.jpg', FOTOGRAMMI + 'facciata-213.28s.png', (420, 40, 1400, 904), 900,
         zona=(650, 522, 1150, 562), forza=0.75, uso='home H1, telefono')
    foto('targa.jpg', FOTOGRAMMI + 'targa-219.16s.png', (300, 40, 1300, 790), 800,
         zona=(430, 332, 520, 392), forza=0.85, uso='home H2, prenota P1 (480 x 360)')
    foto('sala.jpg', 'originali/ristorante/sala-travi-tovaglie-gialle.jpg', (0, 30, 1200, 770),
         zona=(760, 535, 980, 560), uso='home H3 (1200 x 740 a 1440)')
    foto('tavola.jpg', 'originali/ristorante/sala-tavola-pane-vino.jpg', (350, 440, 830, 760),
         zona=(420, 640, 700, 700), uso='home H3, dettaglio (480 x 320 a 1440)')
    grigio('cartolina-largo.jpg', (0, 0, 3298, 1832), 2400, uso='home H4, 1440 e 1024 (sfondo, larghezza massima 2400)')
    grigio('cartolina-alto.jpg', (300, 560, 2300, 1900), 1200, uso='home H4, telefono')
    foto('colli-largo.jpg', VIDEO + 'video-crinale-colli-strada-bianca.jpg', (0, 0, 1920, 850),
         zona=(1040, 560, 1100, 640), forza=0.8, uso='home H5 (sfondo, larghezza massima 1920; al telefono la parte 560-1600)')
    foto('colli-alto.jpg', VIDEO + 'video-crinale-colli-strada-bianca.jpg', (560, 0, 1600, 850),
         zona=(1040, 560, 1100, 640), forza=0.8, uso='riserva: lo stesso taglio che la home ottiene da colli-largo al telefono')
    foto('camera.jpg', 'originali/albergo/camera-matrimoniale-finestra.jpg', (280, 0, 1200, 800),
         zona=(700, 150, 880, 330), uso='home H6, campo giallo (720 x 720 a 1440)')

    # ---- pagine interne (specifica 15): ritagli da guardare sul provino prima di costruire la pagina ----
    foto('camere-largo.jpg', 'originali/albergo/camera-due-letti-travi.jpg', (0, 30, 1200, 770),
         zona=(830, 150, 930, 400), uso='camere C1')
    foto('camere-alto.jpg', 'originali/albergo/camera-due-letti-travi.jpg', (210, 100, 990, 700),
         zona=(830, 150, 930, 400), uso='camere C1, telefono')
    foto('salottino.jpg', 'esterne/regione-veneto/salottino-poltrone-verdi.jpg', (0, 0, 1024, 768), uso='camere C3')
    foto('reception.jpg', 'originali/albergo/reception-banco-legno.jpg', (200, 0, 1000, 800), uso='camere C4')
    foto('padella-largo.jpg', VIDEO + 'video-cucina-padella-fiamma.jpg', (0, 0, 1920, 850), uso='ristorante R2')
    foto('padella-alto.jpg', VIDEO + 'video-cucina-padella-fiamma.jpg', (440, 0, 1480, 850), uso='ristorante R2, telefono')
    foto('sala-vino.jpg', VIDEO + 'video-sala-servizio-vino.jpg', (0, 0, 1600, 850), uso='ristorante R4')
    foto('cantinetta.jpg', 'esterne/regione-veneto/cantinetta-vini-tavolo.jpg', (128, 0, 896, 768),
         zona=(200, 600, 400, 680), uso='ristorante R5')
    foto('vigne-largo.jpg', VIDEO + 'video-drone-vigneto-viale.jpg', (0, 0, 1920, 850),
         zona=(860, 700, 930, 780), forza=0.8, uso='bike hotel B1')
    foto('vigne-alto.jpg', VIDEO + 'video-drone-vigneto-viale.jpg', (560, 0, 1600, 850),
         zona=(860, 700, 930, 780), forza=0.8, uso='bike hotel B1, telefono')
    foto('maglia.jpg', VIDEO + 'video-maglia-team-leon-doro.jpg', (80, 304, 1760, 904), uso='bike hotel B2')
    foto('sterrato.jpg', VIDEO + 'video-mtb-coppia-sterrato.jpg', (480, 0, 1330, 850),
         zona=(900, 780, 1100, 840), forza=0.8, uso='bike hotel B4')
    foto('reception-sera.jpg', VIDEO + 'video-reception-sera.jpg', (380, 0, 1230, 850), uso='ospedale O3')
    foto('este-largo.jpg', VIDEO + 'video-drone-este-dall-alto.jpg', (0, 0, 1920, 850), uso='dove siamo D1')
    foto('este-alto.jpg', VIDEO + 'video-drone-este-dall-alto.jpg', (440, 0, 1480, 850), uso='dove siamo D1, telefono')
    # la porta è la stessa ripresa della facciata (0,3 s dopo): stessi guadagni, così i due gialli sono uguali
    foto('porta.jpg', FOTOGRAMMI + 'porta-213.6s.png', (500, 60, 1380, 904), gains=tuple(fac['guadagni_R_B']),
         uso='dove siamo D4')

    logo('logo-leondoro-verde.png', VERDE)
    logo('logo-leondoro-bianco.png', BIANCO_PIENO)

    with open(os.path.join(WEB, 'ritagli.json'), 'w', encoding='utf-8') as f:
        json.dump(REGISTRO, f, indent=1, ensure_ascii=False)
    for k, v in REGISTRO.items():
        print(k, v['misura_file'], v.get('dopo_RG_BG', ''), v.get('nota', ''))


if __name__ == '__main__':
    sys.exit(main())
