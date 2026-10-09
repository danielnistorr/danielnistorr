# -*- coding: utf-8 -*-
"""
Montaggio di prova del pitch di Encore (90 s, 1920x1080, 25 fps): immagini, testi a schermo, musica.
La voce si registra a parte seguendo COPIONE.md.
Uso: python3 build_video.py <cartella di lavoro> <font InstrumentSans.ttf> <video macchina da cucire> <video telaio> <video ciclo .webm>
Scrive <cartella di lavoro>/encore-pitch-90s.mp4
"""
import io
import os
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

W, H, FPS = 1920, 1080, 25
INK, PAPER = (19, 19, 22), (255, 255, 255)
QUI = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(os.path.dirname(QUI), 'logo', 'encore-logo.png')
MUSICA = 'https://assets.mixkit.co/music/601/601.mp3'      # "Skyline", Eugenio Mininni, Mixkit Stock Music Free License

# (secondi, sorgente, testo a schermo, tema) sorgente: ('video', file, inizio) | ('foto', id Pexels) | ('nero',) | ('ciclo',) | ('fine',)
SCENE = [
    (8, ('video', 'cucito', 3), 'Every season, unsold cashmere.', 'scuro'),
    (8, ('foto', 14641424), 'Since 19 July 2026, the EU bans destroying it.', 'scuro'),
    (8, ('foto', 5706275), "Recyclers exist. A shared standard doesn't.", 'scuro'),
    (9, ('nero',), "What's missing is trust.", 'nero'),
    (12, ('ciclo',), 'One standard.\nOne loop.\nEvery kilo certified.', 'chiaro'),
    (8, ('foto', 2973400), 'Infrared scanners identify every fibre in seconds.', 'scuro'),
    (8, ('video', 'telaio', 6), 'Each batch, to the right certified recycler.\nEvery step on blockchain.', 'scuro'),
    (8, ('foto', 7794331), 'Ask our AI where any kilo came from.', 'scuro'),
    (10, ('foto', 7760243), 'Buy the fibre back, at a discount,\nfor your next collection.', 'scuro'),
    (6, ('foto', 6757412), 'The first loop: one brand, one recycler, one batch.', 'scuro'),
    (5, ('fine',), 'Start your first loop.', 'fine'),
]


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def foto_pexels(pid, cache):
    f = os.path.join(cache, f'px-{pid}.jpg')
    if not os.path.exists(f):
        url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=3000'
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read()
        open(f, 'wb').write(data)
    im = Image.open(f).convert('RGB')
    # ritaglio 16:9 centrato (per le foto verticali un po' più in alto del centro), colori smorzati come la landing
    r = W / H
    w, h = im.size
    if w / h > r:
        nw = int(h * r); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / r); y = int((h - nh) * 0.45); im = im.crop((0, y, w, y + nh))
    im = ImageEnhance.Color(im).enhance(0.6)
    im = im.resize((W * 2, H * 2), Image.LANCZOS)          # margine per lo zoom lento senza scatti
    out = os.path.join(cache, f'px-{pid}-16x9.png')
    im.save(out)
    return out


def font(path, size, peso=400):
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_axes([100, peso])
    except Exception:
        pass
    return f


def sovrapposizione(testo, tema, fpath, out):
    """PNG trasparente 1920x1080: velo scuro in basso, marchio piccolo in alto, testo grande in basso a sinistra."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if tema == 'scuro':
        velo = Image.new('L', (1, H))
        for y in range(H):
            t = max(0.0, (y - H * 0.35) / (H * 0.65))
            velo.putpixel((0, y), int(40 + 175 * t ** 1.4))
        im.paste((11, 11, 12, 255), (0, 0), velo.resize((W, H)))
        d = ImageDraw.Draw(im)
    colore = PAPER if tema in ('scuro', 'nero') else INK
    grande = font(fpath, 76, 400)
    piccolo = font(fpath, 22, 600)
    # marchio in alto a sinistra
    d.text((96, 72), 'E N C O R E', font=piccolo, fill=colore + (235,))
    if tema == 'nero':
        bb = d.multiline_textbbox((0, 0), testo, font=font(fpath, 96, 400), spacing=18)
        d.multiline_text(((W - bb[2]) / 2, (H - bb[3]) / 2), testo, font=font(fpath, 96, 400), fill=colore, spacing=18, align='center')
    elif tema == 'chiaro':
        f = font(fpath, 72, 400)
        bb = d.multiline_textbbox((0, 0), testo, font=f, spacing=16)
        d.multiline_text((96, (H - bb[3]) / 2), testo, font=f, fill=colore, spacing=16)
    elif tema == 'scuro':
        bb = d.multiline_textbbox((0, 0), testo, font=grande, spacing=16)
        d.multiline_text((96, H - 120 - bb[3]), testo, font=grande, fill=colore, spacing=16)
    im.save(out)


def fine(fpath, out):
    im = Image.new('RGB', (W, H), PAPER)
    d = ImageDraw.Draw(im)
    logo = Image.open(LOGO).convert('RGBA')
    k = 640 / logo.width
    logo = logo.resize((640, int(logo.height * k)), Image.LANCZOS)
    im.paste(logo, ((W - 640) // 2, 330), logo)
    f1, f2 = font(fpath, 64, 400), font(fpath, 24, 500)
    for testo, f, y, col in (('Start your first loop.', f1, 560, INK),
                             ('BOOK A PILOT', f2, 680, INK),
                             ('Team Second Thread  ·  Startup Generation Challenge Verona 2026', f2, 960, (111, 112, 117))):
        bb = d.textbbox((0, 0), testo, font=f)
        d.text(((W - bb[2]) / 2, y), testo, font=f, fill=col)
    im.save(out)


def scena(i, dur, src, testo, tema, lav, fpath, video):
    out = os.path.join(lav, f'scena-{i:02d}.mp4')
    ov = os.path.join(lav, f'ov-{i:02d}.png')
    n = dur * FPS
    fade = f'fade=t=in:st=0:d=0.6,fade=t=out:st={dur - 0.6}:d=0.6'
    base = ['-r', str(FPS), '-pix_fmt', 'yuv420p', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-an', out]
    if tema == 'fine':
        img = os.path.join(lav, 'fine.png'); fine(fpath, img)
        run(['ffmpeg', '-y', '-loop', '1', '-t', str(dur), '-i', img, '-vf', f'fps={FPS},fade=t=in:st=0:d=0.8', *base])
        return out
    sovrapposizione(testo, tema, fpath, ov)
    if src[0] == 'nero':
        run(['ffmpeg', '-y', '-f', 'lavfi', '-i', f'color=c=0x0B0B0C:s={W}x{H}:d={dur}:r={FPS}', '-i', ov,
             '-filter_complex', f'[0][1]overlay=0:0,{fade}', '-t', str(dur), *base])
    elif src[0] == 'foto':
        img = foto_pexels(src[1], lav)
        zoom = f"zoompan=z='1.0+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}"
        run(['ffmpeg', '-y', '-loop', '1', '-i', img, '-i', ov, '-filter_complex',
             f'[0]{zoom}[v];[v][1]overlay=0:0,{fade}', '-frames:v', str(n), *base])
    elif src[0] == 'video':
        f, ss = video[src[1]], src[2]
        run(['ffmpeg', '-y', '-ss', str(ss), '-t', str(dur), '-i', f, '-i', ov, '-filter_complex',
             f'[0]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},eq=saturation=0.55,fps={FPS}[v];'
             f'[v][1]overlay=0:0,{fade}', '-t', str(dur), *base])
    elif src[0] == 'ciclo':
        run(['ffmpeg', '-y', '-ss', '1', '-t', str(dur), '-i', video['ciclo'], '-i', ov, '-filter_complex',
             f'[0]scale={W}:{H},fps={FPS}[v];[v][1]overlay=0:0,{fade}', '-t', str(dur), *base])
    return out


def main():
    lav, fpath = sys.argv[1], sys.argv[2]
    video = {'cucito': sys.argv[3], 'telaio': sys.argv[4], 'ciclo': sys.argv[5]}
    os.makedirs(lav, exist_ok=True)
    pezzi = [scena(i, *s, lav, fpath, video) for i, s in enumerate(SCENE, 1)]
    lista = os.path.join(lav, 'lista.txt')
    open(lista, 'w').write(''.join(f"file '{p}'\n" for p in pezzi))
    muto = os.path.join(lav, 'muto.mp4')
    run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', lista, '-c', 'copy', muto])
    totale = sum(s[0] for s in SCENE)
    mp3 = os.path.join(lav, 'musica.mp3')
    if not os.path.exists(mp3):
        open(mp3, 'wb').write(urllib.request.urlopen(urllib.request.Request(MUSICA, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90).read())
    out = os.path.join(lav, 'encore-pitch-90s.mp4')
    run(['ffmpeg', '-y', '-i', muto, '-i', mp3, '-filter_complex',
         f'[1]atrim=0:{totale},afade=t=in:st=0:d=2,afade=t=out:st={totale - 4}:d=4,loudnorm=I=-20:TP=-2[a]',
         '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', out])
    print('ok', out, totale, 's')


if __name__ == '__main__':
    main()
