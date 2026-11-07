# -*- coding: utf-8 -*-
"""
Prepara le immagini del sito Wirmec in assets/web/ (specifica, paragrafo 14).
Regole:
- mai ingrandire: ogni immagine esce alla sua misura nativa o più piccola;
- si ritaglia per l'uso (bordi, vignettature, fili grigi) invece di ingrandire;
- JPEG qualità 84, WebP 82 per le foto scontornate grandi, PNG solo per trasparenze e disegni;
- le foto con il fondo grigio studio (WB 10, WPB 10, WSC 15) hanno il fondo portato a #E6E6E6 esatto,
  così stanno sul grigio della sezione senza riquadro;
- logo: ritaglio senza payoff dal PDF, positivo con i colori originali e negativo bianco dal canale alfa.
Nessun materiale di staging.wirmec.com (decisione dell'utente, LEGGIMI).
Legge file scaricati: eseguire con python3 -I prepara_immagini.py
"""
import json
import os
import shutil
import subprocess

from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
ORIG = os.path.join(RADICE, 'assets', 'originali')
EST = os.path.join(RADICE, 'assets', 'esterne')
WEB = os.path.join(RADICE, 'assets', 'web')
PDF_SITO = os.path.join(RADICE, '_prova', 'crawl', 'risorse', 'Loghi')
SVG_LUOGO = os.path.join(RADICE, '_prova', 'direzioni', 'luogo', 'img')

GRIGIO = (230, 230, 230)      # #E6E6E6, grigio studio
misure = {}


def o(nome):
    return os.path.join(ORIG, nome)


def salva(im, nome, origine, nativa, q=84):
    p = os.path.join(WEB, nome)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if nome.endswith('.jpg'):
        im.convert('RGB').save(p, quality=q, optimize=True, progressive=True)
    elif nome.endswith('.webp'):
        im.save(p, quality=82, method=6)
    else:
        im.save(p, optimize=True)
    misure[nome] = {'origine': os.path.relpath(origine, RADICE), 'nativa': list(nativa), 'web': list(im.size),
                    'kb': round(os.path.getsize(p) / 1024)}


def riduci(im, maxw=None, maxh=None):
    """Riduce (mai ingrandisce) a una larghezza o altezza massima."""
    w, h = im.size
    s = 1.0
    if maxw:
        s = min(s, maxw / w)
    if maxh:
        s = min(s, maxh / h)
    if s < 1:
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    return im


def ritaglia_alfa(im, soglia=16):
    bb = im.getchannel('A').point(lambda v: 255 if v > soglia else 0).getbbox()
    return im.crop(bb)


def riempi_fondo(im, colore, simile, tol=9):
    """Riempie dai bordi il fondo vicino a `simile` con il colore esatto `colore` (niente riquadro sulla sezione)."""
    im = im.convert('RGB')
    w, h = im.size
    spia = (255, 0, 255)
    semi = [(x, y) for x in range(0, w, 7) for y in (0, h - 1)] + [(x, y) for y in range(0, h, 7) for x in (0, w - 1)]
    for p in semi:
        c = im.getpixel(p)
        if c != spia and max(abs(v - s) for v, s in zip(c, simile)) <= tol:
            ImageDraw.floodfill(im, p, spia, thresh=tol)
    px = im.load()
    for y in range(h):
        for x in range(w):
            if px[x, y] == spia:
                px[x, y] = colore
    return im


def su_bianco(im):
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    bg.alpha_composite(im.convert('RGBA'))
    return bg.convert('RGB')


def scontorna_bianco(im, tol=10):
    """Fondo bianco collegato ai bordi -> trasparente (per le presse in fila su /da-banco/)."""
    rgb = riempi_fondo(im, (255, 0, 254), (255, 255, 255), tol)
    a = Image.new('L', rgb.size, 255)
    px, pa = rgb.load(), a.load()
    for y in range(rgb.height):
        for x in range(rgb.width):
            if px[x, y] == (255, 0, 254):
                pa[x, y] = 0
                px[x, y] = (255, 255, 255)
    out = rgb.convert('RGBA')
    out.putalpha(a)
    return ritaglia_alfa(out)


def logo():
    src = o('pdf-logo-wirmec-payoff-rosso.png')
    im = Image.open(src).convert('RGBA')
    nat = im.size
    # il payoff "....the right partner for Harness Makers" comincia alla riga 204: tengo solo il marchio (righe 0-184)
    im = ritaglia_alfa(im.crop((0, 0, im.width, 186)), 8)
    im = riduci(im, maxw=640)
    salva(im, 'logo.png', src, nat)
    # negativo: bianco pieno con il canale alfa del logo (il piede è notte #1F2429)
    neg = Image.new('RGBA', im.size, (255, 255, 255, 0))
    neg.putalpha(im.getchannel('A'))
    salva(neg, 'logo-neg.png', src, nat)


def home():
    # H1: AM460 Sintesi scontornata (foto caricata su Google dal proprietario della scheda)
    src = os.path.join(EST, 'google-proprietario-am460-sintesi-scontornata.webp')
    im0 = Image.open(src).convert('RGBA')
    im = ritaglia_alfa(im0)
    for w, nome in ((1600, 'am460-sintesi.webp'), (1100, 'am460-sintesi-1100.webp')):
        r = riduci(im, maxw=w)
        # una macchiolina semitrasparente nell'angolo in basso a destra, lontana dalla macchina: tolta
        a = r.getchannel('A')
        a.paste(0, (r.width - round(r.width * 140 / 1600), r.height - round(r.height * 70 / 1173), r.width, r.height))
        r.putalpha(a)
        salva(r, nome, src, im0.size)
    salva(riduci(su_bianco(im), maxw=800), 'am460-riga.jpg', src, im0.size)

    # H2: le dodici lavorazioni, tutte al 36% della nativa (stessa scala: il cavo ha lo stesso spessore)
    for n in ('taglio', 'spelatura', 'spelatura-parziale', 'spelatura-intermedia', 'aggraffatura', 'terminale-chiuso',
              'inserimento-gommino', 'inserimento-guaina', 'doppiatore-cavo', 'attorcigliatura-e-stagnatura',
              'stampa-inkjet', 'stampa-a-caldo'):
        src = o(f'pdf-lavorazione-{n}.png')
        im = Image.open(src)
        salva(im.resize((round(im.width * 0.36), round(im.height * 0.36)), Image.LANCZOS), f'lav-{n}.png', src, im.size)

    # H3: AM310 quattro scontornata dal PDF
    src = o('pdf-am310-quattro-scontornata.png')
    im0 = Image.open(src).convert('RGBA')
    im = ritaglia_alfa(im0)
    salva(riduci(im, maxw=1300), 'am310-quattro.webp', src, im0.size)
    salva(riduci(su_bianco(im), maxw=800), 'am310-quattro-riga.jpg', src, im0.size)

    # H4: W 1500 dalla brochure, fondo portato a bianco puro
    src = o('pdf-w1500-aggraffatrice-da-banco-20kn.jpg')
    im0 = Image.open(src)
    im = riempi_fondo(im0, (255, 255, 255), (255, 255, 255), tol=12)
    salva(riduci(im, maxw=1280), 'w1500.jpg', src, im0.size)
    salva(riduci(scontorna_bianco(im0), maxh=560), 'w1500-banco.png', src, im0.size)

    # H5: applicatori sul loro grigio
    for nome, f in (('wb10.jpg', 'sito-wirtool-wb10-applicatore-side-feed.jpg'),
                    ('wpb10.jpg', 'sito-wirtool-wpb10-applicatore-pneumatico.jpg')):
        im0 = Image.open(o(f))
        salva(riempi_fondo(im0, GRIGIO, GRIGIO), nome, o(f), im0.size, q=86)

    # H6: terminale sul righello senza la vignettatura bianca; micrografia invariata; strumenti
    src = o('sito-wiram-am210-terminale-su-righello.jpg')
    im0 = Image.open(src)
    salva(im0.crop((36, 60, 764, 592)), 'righello.jpg', src, im0.size, q=88)
    src = o('sito-wirtest-w200-sezione-aggraffatura-10awg.jpg')
    salva(Image.open(src), 'sezione-10awg.jpg', src, Image.open(src).size, q=90)
    for nome, f in (('w200.jpg', 'sito-wirtest-w200-laboratorio-micrografia.jpg'), ('w100.jpg', 'sito-wirtest-w100-dinamometro.jpg')):
        im0 = Image.open(o(f))
        salva(im0, nome, o(f), im0.size)


def pagine_prodotto():
    """Immagini delle pagine 02-07 (specifica 14): native o ridotte, mai ingrandite."""
    # da banco
    src = o('sito-wirpress-w15-aggraffatrice-da-banco-dritta.jpg')
    im0 = Image.open(src)
    salva(im0.crop((0, 4, im0.width - 6, im0.height)), 'w15.jpg', src, im0.size)   # filo grigio in alto e a destra
    src = o('pdf-w2000-w3000-aggraffatrice-scontornata.png')
    im0 = Image.open(src).convert('RGBA')
    salva(riduci(ritaglia_alfa(im0), maxh=560), 'w2000-w3000.png', src, im0.size)
    src = o('pdf-wsc15-spela-aggraffa.jpg')
    im0 = Image.open(src)
    salva(riduci(riempi_fondo(im0, GRIGIO, GRIGIO), maxw=900), 'wsc15.jpg', src, im0.size)
    for nome, f in (('wsc31.jpg', 'sito-wirpress-wsc31-fianco-macchina.jpg'),
                    ('wsg100.jpg', 'sito-wirstrip-wsg100-troncatrice-da-banco.jpg'),
                    ('wsg200.jpg', 'sito-wirstrip-wsg200-sguainatrice-da-banco.jpg')):
        im0 = Image.open(o(f))
        salva(im0, nome, o(f), im0.size)
    # applicatori
    for nome, f in (('wl10.png', 'sito-wirtool-wl10-applicatore-end-feed.png'),
                    ('wb13.jpg', 'sito-wirtool-wb13-applicatore-ferrules-a.jpg'),
                    ('wpb16.jpg', 'sito-wirtool-wpb16-applicatore-pneumatico-ferrules.jpg'),
                    ('wl11.jpg', 'sito-wirtool-wl11-applicatore-splice-a.jpg'),
                    ('wl19.jpg', 'sito-wirtool-wl19-applicatore-splice-doppia-bandella.jpg'),
                    ('wb23.jpg', 'sito-wirtool-wb23-applicatore-contatti-torniti.jpg'),
                    ('wb27.jpg', 'sito-wirtool-wb27-bus-bar-applicatore.jpg'),
                    ('banco-applicatori.jpg', 'sito-azienda-fila-di-miniapplicatori.jpg')):
        im0 = Image.open(o(f))
        salva(im0, nome, o(f), im0.size)
    # automatiche
    src = o('pdf-am400-quattro.jpg')
    im0 = Image.open(src)
    salva(riduci(im0, maxw=1600), 'am400-quattro.jpg', src, im0.size)
    for nome, f in (('am210-futura.jpg', 'sito-wiram-am210-futura.jpg'),
                    ('am400-quattro-riga.jpg', 'sito-wiram-am400-quattro.jpg'),
                    ('am500-vantage.jpg', 'sito-wiram-am500-vantage.jpg'),
                    ('postazione-vantage.jpg', 'pdf-vantage-postazione-software.jpg'),
                    ('am0010.jpg', 'sito-accessori-am0010-aggraffatrice-20kn.jpg'),
                    ('am0011.jpg', 'sito-accessori-am0011-aggraffatrice-30kn.jpg'),
                    ('am0012.jpg', 'sito-accessori-am0012-aggraffatrice-regolazione-elettronica.jpg'),
                    ('am0061.jpg', 'sito-accessori-am0061-unita-attorcigliatura.jpg'),
                    ('am0083.jpg', 'sito-accessori-am0083-inseritore-coprifaston.jpg'),
                    ('am0090.png', 'sito-accessori-am0090-inseritore-gommino.png'),
                    ('w202.jpg', 'sito-wirtest-w202-penna-elettrolitica.jpg')):
        im0 = Image.open(o(f))
        salva(im0, nome, o(f), im0.size)
    src = o('pdf-am0064-attorcigliatore-programmabile.jpg')
    im0 = Image.open(src)
    salva(riduci(im0, maxw=600), 'am0064.jpg', src, im0.size)
    # pianta della AM310 quattro: senza cornice e ombra, fondo bianco; ritaglio delle stazioni per il telefono
    src = o('pdf-am310-quattro-pianta-ingombri.png')
    im0 = Image.open(src).convert('RGBA')
    g = su_bianco(im0).convert('L')
    W, H = g.size
    g = g.crop((28, 34, W - 36, H - 34)).point(lambda v: 255 if v > 232 else v)   # via anche il filo della cornice a sinistra
    salva(g, 'pianta-am310.png', src, im0.size)
    salva(g.crop((0, 0, 760, g.height)), 'pianta-am310-stazioni.png', src, im0.size)
    # AM600 Vantage, il gruppo del doppio cavo: ritaglio sul gruppo (via il bordo destro con i tubi), 800 x 462
    src = o('pdf-am600-dettaglio-doppio-cavo.jpg')
    im0 = Image.open(src)
    salva(riduci(im0.crop((0, 40, 2420, 1438)), maxw=800), 'am600-doppio-cavo.jpg', src, im0.size)


def pdf_e_copertine():
    if not os.path.isdir(PDF_SITO):
        return
    os.makedirs(os.path.join(WEB, 'pdf'), exist_ok=True)
    for f in sorted(os.listdir(PDF_SITO)):
        if not f.endswith('.pdf'):
            continue
        shutil.copy(os.path.join(PDF_SITO, f), os.path.join(WEB, 'pdf', f))
        tmp = os.path.join(WEB, 'pdf', '_copertina')
        subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-r', '72', '-scale-to-x', '320', '-scale-to-y', '-1', '-jpeg',
                        os.path.join(PDF_SITO, f), tmp], check=True, capture_output=True)
        prodotto = [x for x in os.listdir(os.path.join(WEB, 'pdf')) if x.startswith('_copertina')][0]
        im = Image.open(os.path.join(WEB, 'pdf', prodotto))
        os.remove(os.path.join(WEB, 'pdf', prodotto))
        salva(im, f'pdf-copertina-{f[:-4]}.jpg', os.path.join(PDF_SITO, f), im.size)


def mappe():
    """Mappe vettoriali della direzione "luogo" (scritte già in tracciati). Le piccole Italie restano SVG (finiscono
    in linea nel widget dei referenti); Europa e sede diventano anche PNG al doppio della misura, perché Elementor
    non importa gli SVG nella libreria media senza "upload non filtrati"."""
    if os.path.isdir(SVG_LUOGO):
        for f in sorted(os.listdir(SVG_LUOGO)):
            if f.endswith('.svg') and (f.startswith(('europa', 'mappa-sede', 'italia'))):
                shutil.copy(os.path.join(SVG_LUOGO, f), os.path.join(WEB, f))
    if not shutil.which('node'):
        print('node non trovato: PNG delle mappe non rifatti')
        return
    for f in ('europa-desktop', 'europa-mobile', 'mappa-sede-desktop', 'mappa-sede-mobile'):
        svg, png = os.path.join(WEB, f + '.svg'), os.path.join(WEB, f + '.png')
        subprocess.run(['node', os.path.join(QUI, 'svg_png.mjs'), svg, png, '2'], check=True, capture_output=True)
        im = Image.open(png)
        nat = (im.width // 2, im.height // 2)
        # pochi colori piatti: la tavolozza a 256 colori (octree, tiene il rosso del punto della sede) riduce il peso
        im = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
        im.save(png, optimize=True)
        misure[f + '.png'] = {'origine': os.path.relpath(svg, RADICE), 'nativa': list(nat), 'web': list(Image.open(png).size),
                              'kb': round(os.path.getsize(png) / 1024)}


if __name__ == '__main__':
    os.makedirs(WEB, exist_ok=True)
    logo()
    home()
    pagine_prodotto()
    pdf_e_copertine()
    mappe()
    with open(os.path.join(WEB, 'misure.json'), 'w', encoding='utf-8') as fh:
        json.dump(misure, fh, indent=1, ensure_ascii=False)
    for k, v in misure.items():
        print(f'{k}: {v["nativa"][0]}x{v["nativa"][1]} -> {v["web"][0]}x{v["web"][1]}, {v["kb"]} kB')
