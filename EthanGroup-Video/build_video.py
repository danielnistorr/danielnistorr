# -*- coding: utf-8 -*-
"""
Video di presentazione di Ethan Group, 90 s, 1920x1080, 25 fps. Stesso impianto del pitch di Encore
(Encore-Sito/pitch/build_video.py): video e foto con colori smorzati, numeri grandi con la fonte a schermo,
tre capitoli (Green Economy, Blue Economy, Innovazione e Ricerca), chiusura sul colore del marchio.
Tutti i numeri vengono da ethan-group.it (Storia e Valori, Risultati finanziari, Struttura del gruppo).
Uso: python3 build_video.py <cartella di lavoro> <font InstrumentSans.ttf> <cartella video Mixkit> <cartella immagini del sito>
Nella cartella video servono <id>.mp4 (versioni 720p da assets.mixkit.co) per gli id usati qui sotto.
Scrive <cartella di lavoro>/ethan-group-90s.mp4
"""
import os
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

W, H, FPS = 1920, 1080, 25
INK, PAPER, GRIGIO = (19, 19, 22), (255, 255, 255), (190, 192, 194)
ARDESIA = (76, 105, 113)                 # il fondo del logo Ethan
VERDE, BLU, ORO = (126, 200, 120), (120, 185, 230), (214, 178, 92)
MUSICA = 'https://assets.mixkit.co/music/601/601.mp3'      # "Skyline", Eugenio Mininni, Mixkit Stock Music Free License
KOM = 'Fonte: Ethan Group, Key Operating Metrics'
FONT = IMG = None

# d: secondi; src: ('video', id, inizio) | ('foto', file, punto focale x) | ('nero',) | ('ardesia',) ; ov: sovrimpressione
SCENE = [
    dict(d=5, src=('video', '49209', 4), ov=('testo', 'Quello che oggi è scarto\nè la risorsa di domani.', None)),
    dict(d=5, src=('foto', '450392181_1038893254438462_12267804372097545_n.jpg', 0.5),
         ov=('testo', 'Ethan Group.\nPassione per l\'ambiente.', 'Grisignano di Zocco (VI)')),
    dict(d=5, src=('video', '49212', 6), ov=('numero', (0, 20, '{:.0f}+'),
         'anni di esperienza, dal primo impianto\ndi riciclo dei rifiuti agricoli a oggi.', 'Fonte: Ethan Group, Storia e Valori', None)),

    dict(d=4, src=('video', '14631', 3), ov=('capitolo', '01', 'Green Economy', 'Rifiuti, bonifiche, energia.', VERDE)),
    dict(d=5, src=('foto', '3_EURO_CSV_TRATTAMENTO_RIFIUTI.webp', 0.5), ov=('numero', (0, 700, '{:.0f}K+'),
         'tonnellate l\'anno di capacità di trattamento.\nRifiuti che tornano materie prime seconde.', KOM, None)),
    dict(d=5, src=('video', '49208', 3), ov=('numero', (0, 30000, '{:,.0f}+'),
         'clienti serviti ogni anno,\ncon la logistica interna del gruppo.', KOM, None)),
    dict(d=5, src=('foto', 'AdobeStock_1033184104.jpeg', 0.45), ov=('numero', (0, 450, '{:.0f}K+'),
         'metri quadri di eternit smaltiti.\nBonifiche ambientali e dell\'amianto.', KOM, None)),
    dict(d=5, src=('video', '14051', 5), ov=('testo', 'Energia e idrogeno\ndai rifiuti non riciclabili.',
         'Pirogassificazione: Evron Sustainability e PFG Hybrid')),
    dict(d=4, src=('video', '15596', 2), ov=('numero', 'EMAS',
         'Primo gruppo italiano certificato EMAS\nnella gestione dei rifiuti.', 'Fonte: Ethan Group, Risultati finanziari', None)),

    dict(d=4, src=('video', '14739', 2), ov=('capitolo', '02', 'Blue Economy', 'Il mare come risorsa da proteggere.', BLU)),
    dict(d=5, src=('video', '4465', 0.5), ov=('testo', 'Tutela dell\'ambiente marino\ne purificazione delle acque.', None)),
    dict(d=5, src=('video', '50186', 4), ov=('testo', 'Mobilità elettrica in mare.', 'Belisama Yacht')),
    dict(d=5, src=('foto', 'AdobeStock_922594244-scaled.jpeg', 0.5), ov=('testo',
         'Progetti certificati con ISPRA, CNR\ne le Università di Padova, Venezia e Verona.', None)),

    dict(d=4, src=('video', '4765', 1), ov=('capitolo', '03', 'Innovazione e Ricerca', 'Software e intelligenza artificiale.', ORO)),
    dict(d=5, src=('video', '22032', 3), ov=('testo', 'Software per gestire rifiuti e CO2.\nDati al posto delle stime.', 'ECO-Management')),
    dict(d=5, src=('ardesia',), ov=('rete',)),

    dict(d=5, src=('foto', 'agriculture-iot-with-rice-field-background-scaled.jpg', 0.55), ov=('crescita',)),
    dict(d=5, src=('nero',), ov=('perche',)),
    dict(d=4, src=('ardesia',), ov=('fine',)),
]


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if r.returncode:
        raise SystemExit(r.stderr.decode()[-2000:])


def font(size, peso=400):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_axes([100, peso])
    except Exception:
        pass
    return f


def entra(t, ritardo, durata=0.5):
    k = min(1.0, max(0.0, (t - ritardo) / durata))
    return 1 - (1 - k) ** 3


_LOGO = {}


def logo(larghezza):
    if larghezza not in _LOGO:
        im = Image.open(os.path.join(IMG, '926fd7fd-97c1-40b5-a80d-ce8851999fff.png')).convert('RGBA')
        _LOGO[larghezza] = im.resize((larghezza, round(im.height * larghezza / im.width)), Image.LANCZOS)
    return _LOGO[larghezza]


def marchio(im, d, col):
    """In alto a sinistra: ETHAN spaziato, come il marchio di Encore nel suo video."""
    f = font(19, 600)
    x = 96
    for ch in 'ETHAN':
        d.text((x, 77), ch, font=f, fill=col, anchor='lm')
        x += d.textlength(ch, font=f) + 7
    d.text((x + 10, 77), 'GROUP', font=font(19, 400), fill=col, anchor='lm')


_VELO = None


def velo():
    global _VELO
    if _VELO is None:
        v = Image.new('L', (1, H))
        for y in range(H):
            t = max(0.0, (y - H * 0.25) / (H * 0.75))
            v.putpixel((0, y), int(70 + 170 * t ** 1.3))
        _VELO = v.resize((W, H))
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    im.paste((11, 11, 12, 255), (0, 0), _VELO)
    return im


def fonte(d, testo, col=GRIGIO):
    if testo:
        d.text((96, H - 72), testo, font=font(20, 500), fill=col, anchor='ls')


def ov_frame(ov, t):
    """Sovrimpressione al tempo t (secondi): immagine RGBA 1920x1080."""
    tipo = ov[0]
    im = velo() if tipo in ('testo', 'numero', 'capitolo', 'crescita') else Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if tipo != 'fine':
        marchio(im, d, PAPER)
    if tipo == 'testo':
        _, testo, src = ov
        f = font(68)
        bb = d.multiline_textbbox((0, 0), testo, font=f, spacing=18)
        d.multiline_text((96, H - 150 - bb[3]), testo, font=f, fill=PAPER, spacing=18)
        fonte(d, src)
    elif tipo == 'numero':
        _, val, label, src, pre = ov
        if isinstance(val, tuple):
            a, b, fmt = val
            k = entra(t, 0, 1.6)
            val = fmt.format(a + (b - a) * k).replace(',', '.')
        fl = font(42)
        bl = d.multiline_textbbox((0, 0), label, font=fl, spacing=14)
        y_label = H - 150 - bl[3]
        d.text((90, y_label - 36), val, font=font(260), fill=PAPER, anchor='ls')
        d.multiline_text((96, y_label), label, font=fl, fill=PAPER, spacing=14)
        fonte(d, src)
    elif tipo == 'capitolo':
        _, n, titolo, sotto, col = ov
        k = entra(t, 0.15, 0.7)
        d.text((96, H - 330), n + '  /  03', font=font(26, 500), fill=col, anchor='ls')
        d.line((96, H - 300, 96 + int(560 * k), H - 300), fill=col, width=3)
        d.text((92, H - 178), titolo, font=font(130), fill=PAPER, anchor='ls')
        d.text((96, H - 110), sotto, font=font(40), fill=(230, 230, 232), anchor='ls')
    elif tipo == 'rete':
        d.text((96, 300), 'LA RETE', font=font(24, 500), fill=(220, 228, 230), anchor='ls')
        d.text((92, 440), 'Veneto Green Cluster', font=font(96), fill=PAPER, anchor='ls')
        for i, (num, lab) in enumerate([('90', 'aziende'), ('3', 'università'), ('5', 'enti di ricerca')]):
            x = 96 + i * 580
            a = int(255 * entra(t, 0.4 + i * 0.4))
            if a <= 0:
                continue
            d.line((x, 560, x + 500, 560), fill=(255, 255, 255, a // 3), width=2)
            d.text((x - 6, 790), num, font=font(200), fill=(255, 255, 255, a), anchor='ls')
            d.text((x, 860), lab, font=font(44), fill=(255, 255, 255, a), anchor='ls')
        fonte(d, 'Rete Innovativa Regionale promossa dal gruppo dal 2017', (220, 228, 230))
    elif tipo == 'crescita':
        k = entra(t, 0.3, 1.8)
        d.text((96, 330), 'FATTURATO CONSOLIDATO', font=font(24, 500), fill=GRIGIO, anchor='ls')
        d.text((90, 560), '€41,1M', font=font(170), fill=(255, 255, 255, 150), anchor='ls')
        d.text((96, 620), '2024', font=font(34, 500), fill=GRIGIO, anchor='ls')
        val = 41.1 + (63.6 - 41.1) * k
        d.text((W // 2 + 40, 560), f'€{val:.1f}M'.replace('.', ','), font=font(170), fill=PAPER, anchor='ls')
        d.text((W // 2 + 46, 620), '2027, obiettivo', font=font(34, 500), fill=GRIGIO, anchor='ls')
        d.line((96, 700, 96 + int((W - 192) * k), 700), fill=VERDE, width=3)
        d.text((96, 800), 'Crescita media annua stimata di circa il 15,6%.', font=font(46), fill=PAPER, anchor='ls')
        fonte(d, 'Fonte: Ethan Group, dati gestionali consolidati. 2025-2027 stimati.')
    elif tipo == 'perche':
        d.text((96, 300), 'PERCHÉ ETHAN', font=font(24, 500), fill=GRIGIO, anchor='ls')
        righe = ['Oltre 9 società lungo tutta la filiera ambientale', 'Dal rifiuto alla materia prima seconda',
                 '12 dei 17 Obiettivi ONU dell\'Agenda 2030', 'Ricerca con università ed enti nazionali']
        for i, r in enumerate(righe):
            vis = entra(t, 0.2 + i * 0.6, 0.45)
            if vis <= 0:
                continue
            a = int(255 * vis)
            y = 400 + i * 150
            d.line((96, y, W - 96, y), fill=(58, 58, 63, a), width=2)
            d.text((96, y + 92), r, font=font(58), fill=(255, 255, 255, a), anchor='ls')
    elif tipo == 'fine':
        lg = logo(560)
        im.paste(lg, ((W - lg.width) // 2, 190), lg)
        for testo, f, y, col in (('Passione per l\'ambiente.', font(64), 640, PAPER),
                                 ('ETHAN-GROUP.IT', font(26, 600), 740, ORO),
                                 ('Via dell\'Industria 1, Grisignano di Zocco (VI)  ·  +39 0444 41 41 25', font(24, 500), 960, (220, 228, 230))):
            bb = d.textbbox((0, 0), testo, font=f)
            d.text(((W - bb[2]) / 2, y), testo, font=f, fill=col)
    return im


def ov_statico(ov):
    return ov[0] == 'testo' or (ov[0] == 'numero' and not isinstance(ov[1], tuple))


def foto16x9(nome, fx, lav):
    """Foto del sito ritagliata 16:9 attorno al punto focale fx, colori smorzati, al doppio della risoluzione."""
    out = os.path.join(lav, 'foto-' + os.path.splitext(nome)[0] + '.png')
    if os.path.exists(out):
        return out
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(os.path.join(IMG, nome)).convert('RGB')
    w, h = im.size
    if w / h > 16 / 9:
        nw = int(h * 16 / 9); x = int(min(max(0, w * fx - nw / 2), w - nw)); im = im.crop((x, 0, x + nw, h))
    else:
        nh = int(w * 9 / 16); y = (h - nh) // 2; im = im.crop((0, y, w, y + nh))
    ImageEnhance.Color(im).enhance(0.7).resize((W * 2, H * 2), Image.LANCZOS).save(out)
    return out


def scena(i, s, lav, vdir):
    dur, src, ov = s['d'], s['src'], s['ov']
    out = os.path.join(lav, f'scena-{i:02d}.mp4')
    n = int(round(dur * FPS))
    fade = f'fade=t=in:st=0:d=0.3,fade=t=out:st={dur - 0.3:.2f}:d=0.3'
    if ov[0] == 'fine':
        fade = 'fade=t=in:st=0:d=0.6'
    enc = ['-r', str(FPS), '-pix_fmt', 'yuv420p', '-c:v', 'libx264', '-crf', '19', '-preset', 'veryfast', '-an', out]
    if ov_statico(ov):
        p = os.path.join(lav, f'ov-{i:02d}.png'); ov_frame(ov, 0).save(p)
        ov_in = ['-loop', '1', '-framerate', str(FPS), '-t', str(dur), '-i', p]
    else:
        cart = os.path.join(lav, f'ov-{i:02d}'); os.makedirs(cart, exist_ok=True)
        for k in range(n):
            ov_frame(ov, k / FPS).save(os.path.join(cart, f'{k:04d}.png'), compress_level=1)
        ov_in = ['-framerate', str(FPS), '-i', os.path.join(cart, '%04d.png')]
    if src[0] in ('nero', 'ardesia'):
        c = '0x0B0B0C' if src[0] == 'nero' else '0x%02X%02X%02X' % ARDESIA
        base = ['-f', 'lavfi', '-i', f'color=c={c}:s={W}x{H}:d={dur}:r={FPS}']
        v = '[0]null[v]'
    elif src[0] == 'foto':
        base = ['-loop', '1', '-framerate', str(FPS), '-t', str(dur), '-i', foto16x9(src[1], src[2], lav)]
        v = f"[0]zoompan=z='1+0.07*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}[v]"
    else:
        base = ['-ss', str(src[2]), '-t', str(dur), '-i', os.path.join(vdir, f'{src[1]}.mp4')]
        # colori smorzati ma non spenti: il verde e il blu devono restare leggibili
        v = (f'[0]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},'
             f'eq=saturation=0.7:contrast=1.05,fps={FPS}[v]')
    run(['ffmpeg', '-y', *base, *ov_in, '-filter_complex', f'{v};[v][1]overlay=0:0,{fade}', '-frames:v', str(n), *enc])
    return out


def main():
    global FONT, IMG
    lav, FONT, vdir, IMG = sys.argv[1:5]
    os.makedirs(lav, exist_ok=True)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(4) as ex:
        pezzi = list(ex.map(lambda a: scena(a[0], a[1], lav, vdir), enumerate(SCENE, 1)))
    lista = os.path.join(lav, 'lista.txt')
    open(lista, 'w').write(''.join(f"file '{p}'\n" for p in pezzi))
    muto = os.path.join(lav, 'muto.mp4')
    run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', muto])
    totale = sum(s['d'] for s in SCENE)
    mp3 = os.path.join(lav, 'musica.mp3')
    if not os.path.exists(mp3):
        open(mp3, 'wb').write(urllib.request.urlopen(urllib.request.Request(MUSICA, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
    out = os.path.join(lav, 'ethan-group-90s.mp4')
    run(['ffmpeg', '-y', '-i', muto, '-i', mp3, '-filter_complex',
         f'[1]atrim=0:{totale},afade=t=in:st=0:d=2,afade=t=out:st={totale - 4}:d=4,loudnorm=I=-20:TP=-2[a]',
         '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out])
    print('ok', out, totale, 's')


if __name__ == '__main__':
    main()
