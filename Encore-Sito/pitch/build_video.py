# -*- coding: utf-8 -*-
"""
Pitch di Encore, 90 s, 1920x1080, 25 fps: video di produzione, numeri verificati con la fonte a schermo, il ciclo in
cinque passi, musica. La voce si registra a parte seguendo COPIONE.md.
Uso: python3 build_video.py <cartella di lavoro> <font InstrumentSans.ttf> <cartella video> <video del ciclo .webm> <video del portale .webm> [voce .mp3]
Nella cartella video servono: hd-<id Mixkit>.mp4 per gli id usati qui sotto, 32433-720.mp4 e 4480-1080.mp4.
Scrive <cartella di lavoro>/encore-pitch-90s.mp4
"""
import os
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1920, 1080, 25
INK, PAPER, GRIGIO = (19, 19, 22), (255, 255, 255), (185, 185, 188)
QUI = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(os.path.dirname(QUI), 'logo', 'encore-logo.png')
MUSICA = 'https://assets.mixkit.co/music/601/601.mp3'      # "Skyline", Eugenio Mininni, Mixkit Stock Music Free License
EEA = 'Source: European Environment Agency, 2024'
FONT = None

# d: secondi; src: ('video', id, inizio) | ('nero',) | ('ciclo',) | ('fine',); ov: sovrimpressione
SCENE = [
    dict(d=6, src=('video', '35884', 1), ov=('testo', 'Every season, luxury fashion\nis left with unsold stock.', None)),
    dict(d=7, src=('video', '20770', 0), ov=('numero', (0, 9, '{:.0f}%'),
         'of textiles placed on the EU market are destroyed\nbefore use. Up to 594,000 tonnes a year.', EEA, 'UP TO')),
    dict(d=7, src=('video', '4705', 2), ov=('numero', '1/3', 'of clothing returned after an online purchase\nends up destroyed.', EEA)),
    dict(d=7, src=('video', 'cucito', 3), ov=('testo', 'Since 19 July 2026, large companies can no longer\ndestroy unsold clothing in the EU.',
         'Regulation (EU) 2024/1781 (ESPR), Article 25')),
    dict(d=6, src=('video', '17675', 2), ov=('numero', '<1%', 'of clothing material is recycled\ninto new clothing.',
         'Source: Ellen MacArthur Foundation, A New Textiles Economy, 2017')),
    dict(d=4, src=('nero',), ov=('nero', "The technology exists.\nWhat's missing is trust.")),
    dict(d=7, src=('ciclo',), ov=('chiaro', 'One standard.\nOne loop.\nEvery kilo certified.')),
    dict(d=5, src=('video', '15596', 1), ov=('passo', '01', 'Collected', 'Unsold stock, returns and offcuts.')),
    dict(d=5, src=('video', '47258', 4), ov=('passo', '02', 'Scanned', 'Infrared scanners identify each fibre in seconds.')),
    dict(d=5, src=('video', '20684', 3), ov=('passo', '03', 'Matched', 'Each batch goes to the right certified recycler.')),
    dict(d=3, src=('etichetta',), ov=('vuoto',)),
    dict(d=8, src=('portale', 0.5), ov=('vuoto',)),
    dict(d=5, src=('video', 'telaio', 6), ov=('passo', '05', 'Bought back', 'Recycled fibre, at a discount, for your next collection.')),
    dict(d=6, src=('video', '51013', 1), ov=('valore', 'Your unsold stock stops being a cost.', 'It comes back as fibre you buy below market price.')),
    dict(d=5, src=('nero',), ov=('perche',)),
    dict(d=4, src=('fine',), ov=('fine',)),
]


# Con la voce: stacchi sulle frasi della registrazione ElevenLabs (pause misurate con silencedetect), voce in ritardo di 0,5 s.
VOCE_RITARDO = 0.5
DURATE_VOCE = [5.8, 6.25, 5.10, 6.25, 5.05, 4.5, 5.75, 3.95, 4.3, 4.15, 2.6, 7.7, 5.1, 6.55, 5.95, 6.5]


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


def marchio(d, x, y, col, scala=1.0):
    """Il marchio di Encore disegnato: anello aperto con il punto a destra, poi la scritta spaziata."""
    r = 13 * scala
    cx, cy = x + r, y + r
    d.arc((cx - r, cy - r, cx + r, cy + r), start=23, end=337, fill=col, width=max(2, round(2.2 * scala)))
    pr = 3.4 * scala
    d.ellipse((cx + r - pr, cy - pr, cx + r + pr, cy + pr), fill=col)
    f = font(round(19 * scala), 600)
    tx = cx + r + 16 * scala
    for ch in 'ENCORE':
        d.text((tx, cy), ch, font=f, fill=col, anchor='lm')
        tx += d.textlength(ch, font=f) + 7 * scala


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


def fonte(d, testo, col):
    if testo:
        d.text((96, H - 72), testo, font=font(20, 500), fill=col, anchor='ls')


def ov_frame(ov, t):
    """Sovrimpressione al tempo t (secondi): ritorna un'immagine RGBA 1920x1080."""
    tipo = ov[0]
    im = velo() if tipo in ('testo', 'numero', 'passo', 'valore') else Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if tipo == 'vuoto':
        return im
    marchio(d, 96, 64, INK if tipo == 'chiaro' else PAPER)
    if tipo == 'testo':
        _, testo, src = ov
        f = font(68)
        bb = d.multiline_textbbox((0, 0), testo, font=f, spacing=18)
        d.multiline_text((96, H - 150 - bb[3]), testo, font=f, fill=PAPER, spacing=18)
        fonte(d, src, GRIGIO)
    elif tipo == 'numero':
        _, val, label, src, *pre = ov
        if isinstance(val, tuple):
            a, b, fmt = val
            k = min(1.0, t / 1.6)
            k = 1 - (1 - k) ** 3                       # rallenta verso la fine
            val = fmt.format(a + (b - a) * k)
        fl = font(42)
        bl = d.multiline_textbbox((0, 0), label, font=fl, spacing=14)
        y_label = H - 150 - bl[3]
        d.text((90, y_label - 36), val, font=font(260), fill=PAPER, anchor='ls')
        if pre:                                         # "UP TO": il dato EEA è una forbice (4-9%), si mostra il massimo
            d.text((96, y_label - 36 - 214), pre[0], font=font(26, 500), fill=GRIGIO, anchor='ls')
        d.multiline_text((96, y_label), label, font=fl, fill=PAPER, spacing=14)
        fonte(d, src, GRIGIO)
    elif tipo == 'passo':
        _, n, titolo, testo = ov
        d.text((96, H - 318), n, font=font(26, 500), fill=GRIGIO, anchor='ls')
        d.text((94, H - 214), titolo, font=font(96), fill=PAPER, anchor='ls')
        d.text((96, H - 140), testo, font=font(38), fill=(230, 230, 232), anchor='ls')
        for i in range(5):                              # i cinque passi del ciclo: quello in corso è pieno
            x = W - 96 - (4 - i) * 44
            d.ellipse((x - 7, H - 157, x + 7, H - 143), fill=PAPER if i == int(n) - 1 else None, outline=PAPER, width=2)
    elif tipo == 'nero':
        f = font(92)
        bb = d.multiline_textbbox((0, 0), ov[1], font=f, spacing=22, align='center')
        d.multiline_text(((W - bb[2]) / 2, (H - bb[3]) / 2), ov[1], font=f, fill=PAPER, spacing=22, align='center')
    elif tipo == 'chiaro':
        f = font(76)
        bb = d.multiline_textbbox((0, 0), ov[1], font=f, spacing=18)
        d.multiline_text((96, (H - bb[3]) / 2), ov[1], font=f, fill=INK, spacing=18)
    elif tipo == 'valore':
        _, riga1, riga2 = ov
        d.text((94, H - 250), riga1, font=font(76), fill=PAPER, anchor='ls')
        d.text((96, H - 160), riga2, font=font(52), fill=GRIGIO, anchor='ls')
    elif tipo == 'perche':
        d.text((96, 300), 'WHY ENCORE', font=font(24, 500), fill=GRIGIO, anchor='ls')
        righe = ['One partner instead of dozens of recyclers to vet', 'A certificate no one can falsify',
                 'Answers in plain language, not spreadsheets', 'Your products never reach the grey market']
        for i, r in enumerate(righe):
            vis = min(1.0, max(0.0, (t - 0.2 - i * 0.55) / 0.45))     # una riga alla volta
            if vis <= 0:
                continue
            a = int(255 * vis)
            y = 400 + i * 150
            d.line((96, y, W - 96, y), fill=(58, 58, 63, a), width=2)
            d.text((96, y + 92), r, font=font(58), fill=(255, 255, 255, a), anchor='ls')
    elif tipo == 'pilota':
        d.text((96, 300), 'THE FIRST LOOP', font=font(24, 500), fill=GRIGIO, anchor='ls')
        for i, (num, lab) in enumerate([('1', 'brand'), ('1', 'recycler'), ('1', 'batch of unsold\nwool knitwear')]):
            x = 96 + i * 580
            vis = min(1.0, max(0.0, (t - 0.3 - i * 0.45) / 0.5))      # entrano uno dopo l'altro
            if vis <= 0:
                continue
            a = int(255 * vis)
            d.line((x, 380, x + 500, 380), fill=(58, 58, 63, a), width=2)
            d.text((x - 6, 650), num, font=font(240), fill=(255, 255, 255, a), anchor='ls')
            d.multiline_text((x, 700), lab, font=font(44), fill=(255, 255, 255, a), spacing=12)
        d.text((96, H - 72), 'Pilot · Startup Generation Challenge Verona 2026', font=font(20, 500), fill=GRIGIO, anchor='ls')
    return im


def ov_statico(ov):
    return ov[0] in ('testo', 'passo', 'nero', 'chiaro', 'valore', 'vuoto') or (ov[0] == 'numero' and not isinstance(ov[1], tuple))


def fine(out):
    im = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(im)
    logo = Image.open(LOGO).convert('RGBA')
    logo = logo.resize((640, int(logo.height * 640 / logo.width)), Image.LANCZOS)
    im.paste(logo, ((W - 640) // 2, 330), logo)
    for testo, f, y, col in (('Start your first loop.', font(64), 560, INK),
                             ('BOOK A PILOT', font(24, 500), 680, INK),
                             ('Team Second Thread  ·  Startup Generation Challenge Verona 2026', font(24, 500), 960, (111, 112, 117))):
        bb = d.textbbox((0, 0), testo, font=f)
        d.text(((W - bb[2]) / 2, y), testo, font=f, fill=col)
    im.save(out)


def etichetta(lav):
    """Fotogramma 3840x2160: maglie piegate (Pexels 14641424) con il cartellino del lotto e il QR code."""
    out = os.path.join(lav, 'etichetta.png')
    foto = os.path.join(lav, 'px-14641424.jpg')
    if not os.path.exists(foto):
        url = 'https://images.pexels.com/photos/14641424/pexels-photo-14641424.jpeg?auto=compress&cs=tinysrgb&w=3000'
        open(foto, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
    im = Image.open(foto).convert('RGB')
    w, h = im.size
    nh = int(w * 9 / 16); y = int((h - nh) * 0.5)
    im = im.crop((0, y, w, y + nh)).resize((W * 2, H * 2), Image.LANCZOS)
    from PIL import ImageEnhance
    im = ImageEnhance.Brightness(ImageEnhance.Color(im).enhance(0.55)).enhance(0.62).convert('RGBA')
    # cartellino
    tw, th = 760, 1180
    tag = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.rounded_rectangle((0, 0, tw - 1, th - 1), radius=36, fill=(250, 250, 248, 255))
    td.ellipse((tw / 2 - 26, 46, tw / 2 + 26, 98), fill=(40, 40, 44, 255))
    marchio(td, 70, 150, INK, scala=2.0)
    td.text((70, 300), 'BATCH', font=font(30, 500), fill=(111, 112, 117))
    td.text((70, 345), 'EN-26-0412', font=font(72), fill=INK)
    td.text((70, 445), 'Wool 81%  ·  Cashmere 19%', font=font(38), fill=INK)
    td.text((70, 500), '486.2 kg  ·  1,240 items', font=font(38), fill=(85, 86, 90))
    qr = Image.open(os.path.join(QUI, 'qr.png')).convert('RGBA').resize((420, 420), Image.NEAREST)
    tag.paste(qr, (70, 590), qr)
    td.text((70, 1060), 'Scan to verify on chain', font=font(34, 500), fill=INK)
    tag = tag.rotate(-5, resample=Image.BICUBIC, expand=True)
    sd = ImageDraw.Draw(im)
    sd.line((W * 2 * 0.64, 0, W * 2 * 0.64 + 40, 330), fill=(235, 235, 232, 255), width=6)      # il filo del cartellino
    im.paste(tag, (int(W * 2 * 0.52), 300), tag)
    im.convert('RGB').save(out)
    return out


def scena(i, s, lav, vid):
    dur, src, ov = s['d'], s['src'], s['ov']
    out = os.path.join(lav, f'scena-{i:02d}.mp4')
    n = int(round(dur * FPS))
    fade = f'fade=t=in:st=0:d=0.3,fade=t=out:st={dur - 0.3:.2f}:d=0.3'
    enc = ['-r', str(FPS), '-pix_fmt', 'yuv420p', '-c:v', 'libx264', '-crf', '19', '-preset', 'medium', '-an', out]
    if ov[0] == 'fine':
        img = os.path.join(lav, 'fine.png'); fine(img)
        run(['ffmpeg', '-y', '-loop', '1', '-t', str(dur), '-i', img, '-vf', f'fps={FPS},fade=t=in:st=0:d=0.8', *enc])
        return out
    # sovrimpressione: un PNG se è ferma, una sequenza se si anima
    if ov_statico(ov):
        p = os.path.join(lav, f'ov-{i:02d}.png'); ov_frame(ov, 0).save(p)
        ov_in = ['-loop', '1', '-framerate', str(FPS), '-t', str(dur), '-i', p]
    else:
        cart = os.path.join(lav, f'ov-{i:02d}'); os.makedirs(cart, exist_ok=True)
        for k in range(n):
            ov_frame(ov, k / FPS).save(os.path.join(cart, f'{k:04d}.png'), compress_level=1)
        ov_in = ['-framerate', str(FPS), '-i', os.path.join(cart, '%04d.png')]
    if src[0] == 'nero':
        base = ['-f', 'lavfi', '-i', f'color=c=0x0B0B0C:s={W}x{H}:d={dur}:r={FPS}']
        v = '[0]null[v]'
    elif src[0] == 'etichetta':
        base = ['-loop', '1', '-framerate', str(FPS), '-t', str(dur), '-i', etichetta(lav)]
        v = f"[0]zoompan=z='1+0.07*on/{n}':x='iw*0.62-(iw/zoom/2)':y='ih*0.5-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}[v]"
    elif src[0] == 'portale':
        base = ['-ss', str(src[1]), '-t', str(dur), '-i', vid['portale']]
        v = f'[0]scale={W}:{H},fps={FPS}[v]'
    elif src[0] == 'ciclo':
        base = ['-ss', '1', '-t', str(dur), '-i', vid['ciclo']]
        v = f'[0]scale={W}:{H},fps={FPS}[v]'
    else:
        f = vid.get(src[1]) or os.path.join(vid['dir'], f'hd-{src[1]}.mp4')
        base = ['-ss', str(src[2]), '-t', str(dur), '-i', f]
        # colori smorzati e zoom lento anche sul video: il movimento non si ferma mai
        v = (f'[0]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},eq=saturation=0.5:contrast=1.05,fps={FPS},'
             f"scale={W * 2}:{H * 2},zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}[v]")
    run(['ffmpeg', '-y', *base, *ov_in, '-filter_complex', f'{v};[v][1]overlay=0:0,{fade}', '-frames:v', str(n), *enc])
    return out


def main():
    global FONT
    lav, FONT, vdir, ciclo, portale = sys.argv[1:6]
    voce = sys.argv[6] if len(sys.argv) > 6 else None
    if voce:
        for sc, d in zip(SCENE, DURATE_VOCE):
            sc['d'] = d
    vid = {'dir': vdir, 'ciclo': ciclo, 'portale': portale, 'cucito': os.path.join(vdir, '32433-720.mp4'), 'telaio': os.path.join(vdir, '4480-1080.mp4')}
    os.makedirs(lav, exist_ok=True)
    pezzi = []
    for i, s in enumerate(SCENE, 1):
        pezzi.append(scena(i, s, lav, vid))
        print('scena', i, 'ok', flush=True)
    lista = os.path.join(lav, 'lista.txt')
    open(lista, 'w').write(''.join(f"file '{p}'\n" for p in pezzi))
    muto = os.path.join(lav, 'muto.mp4')
    run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', muto])
    totale = sum(s['d'] for s in SCENE)
    mp3 = os.path.join(lav, 'musica.mp3')
    if not os.path.exists(mp3):
        open(mp3, 'wb').write(urllib.request.urlopen(urllib.request.Request(MUSICA, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
    out = os.path.join(lav, 'encore-pitch-90s.mp4')
    if voce:
        # musica abbassata sotto la voce (sidechain), voce normalizzata a -16 LUFS, limitatore finale
        ms = int(VOCE_RITARDO * 1000)
        filtro = (f'[1]atrim=0:{totale},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.5,afade=t=out:st={totale - 4}:d=4,volume=0.55[m];'
                  f'[2]loudnorm=I=-16:TP=-2,adelay={ms}|{ms},pan=stereo|c0=c0|c1=c0,apad=whole_dur={totale}[v];'
                  '[v]asplit=2[v1][v2];'
                  '[m][v1]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=450[md];'
                  '[md][v2]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.9[a]')
        run(['ffmpeg', '-y', '-i', muto, '-i', mp3, '-i', voce, '-filter_complex', filtro,
             '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', str(totale), '-movflags', '+faststart', out])
    else:
        run(['ffmpeg', '-y', '-i', muto, '-i', mp3, '-filter_complex',
             f'[1]atrim=0:{totale},afade=t=in:st=0:d=2,afade=t=out:st={totale - 4}:d=4,loudnorm=I=-20:TP=-2[a]',
             '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out])
    print('ok', out, totale, 's')


if __name__ == '__main__':
    main()
