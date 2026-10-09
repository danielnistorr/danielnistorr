# -*- coding: utf-8 -*-
"""
Contenuti della landing page di Encore (Startup Generation Challenge Verona 2026, Sfida 02 "Da scarto a risorsa").
Stesso generatore di Benvegnù (motore.py, build.py): template Elementor, fallback HTML per sezione, anteprima.

Direzione (seconda versione, su richiesta del committente): impaginazione e palette di evoxconsulting.it.
Hero con foto al vivo e titolo grande bianco in basso a sinistra, header trasparente con pulsante a pillola,
nero #131316 / bianco / grigi caldi, un solo carattere (Instrument Sans) con titoli grandi in peso 400 e spaziatura
stretta, intestazioni di sezione con filetto ed etichetta, schede foto per i passi, fascia scura con foto,
piè di pagina con il marchio grande in filigrana. Niente numerazione di Evox con la lineetta lunga dopo il numero (vietata dal brief).

Ogni sezione è un widget HTML (RAW) dentro un contenitore: il layout non ha un equivalente nei widget gratuiti di
Elementor. Gli stili comuni stanno nella sezione header. Testi: esattamente quelli del brief, in inglese; le etichette
piccole sono i nomi delle sezioni del brief.
"""
import os
import re
from html import escape
from urllib.parse import quote

import motore as m
from motore import C, RAW

PREFISSO = 'enc'
NOME_SITO = 'Encore'
m.LINGUA = 'en'

# logo (generato da logo.py in ../logo): in pagina inline, bianco sull'hero; come favicon l'icona quadrata
LOGO_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logo')


def _svg(nome):
    t = open(os.path.join(LOGO_DIR, nome + '.svg'), encoding='utf-8').read().strip()
    t = re.sub(r'<title>.*?</title>', '', t)
    return re.sub(r' width="[\d.]+" height="[\d.]+" role="img" aria-label="Encore"', ' aria-hidden="true" focusable="false"', t)


LOGO_BIANCO = _svg('encore-logo-bianco')
m.ICONA = 'data:image/svg+xml,' + quote(open(os.path.join(LOGO_DIR, 'encore-icona.svg'), encoding='utf-8').read().strip())

# ---------------------------------------------------------------------------------------------
# Tema (palette di evoxconsulting.it)
# ---------------------------------------------------------------------------------------------
INK = '#131316'            # testo e superfici scure
INK2 = '#55565A'           # testo secondario su bianco (7,4:1)
INK3 = '#6F7075'           # etichette su bianco (4,9:1)
PAPER = '#FFFFFF'
MIST = '#F5F5F3'           # superfici chiare alternate
LINE = '#E4E4E0'           # filetti
DARK = '#0B0B0C'           # fasce scure
ON_DARK2 = '#B9B9BC'       # testo secondario su scuro (9,6:1)

SANS = 'Instrument Sans'
STACK = f"'{SANS}',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

m.applica_tema({
    'nome': 'Encore',
    'fondo': PAPER, 'superficie': PAPER, 'inchiostro': INK, 'testo2': INK2, 'accento': INK,
    'filetto': LINE, 'filetto_scuro': '#2A2A2E', 'su_scuro2': ON_DARK2,
    'scuro': INK, 'su_scuro': PAPER, 'su_accento': PAPER,
    'font_titoli': SANS, 'font_testo': SANS, 'larghezza': 1440,
    'google_fonts': 'https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&display=swap',
})

BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Encore-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Stili comuni: scala 8 px, tipografia (una sola volta, nella sezione header)
# lato: 48 desktop, 32 tablet, 16 telefono; sezione: 160 / 120 / 88
# ---------------------------------------------------------------------------------------------
CSS_COMUNE = f"""
.enc-sr{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(1px,1px,1px,1px);white-space:nowrap}}
.enc-c{{max-width:1440px;margin:0 auto;padding-left:48px;padding-right:48px}}
.enc-sez{{padding-top:160px;padding-bottom:160px}}
.enc-t{{font-family:{STACK};font-weight:400;font-style:normal;color:{INK};margin:0;text-wrap:balance}}
.enc-h1{{font-size:92px;line-height:1.04;letter-spacing:-0.035em}}
.enc-h2{{font-size:60px;line-height:1.06;letter-spacing:-0.028em}}
.enc-big{{font-size:44px;line-height:1.16;letter-spacing:-0.022em}}
.enc-h3{{font-size:26px;line-height:1.2;letter-spacing:-0.012em}}
.enc-p{{font-family:{STACK};font-size:17px;line-height:1.6;font-weight:400;color:{INK2};margin:0;max-width:36em}}
.enc-label{{font-family:{STACK};font-size:12px;line-height:1.5;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;
  color:{INK3};margin:0}}
.enc-small{{font-family:{STACK};font-size:14px;line-height:1.6;color:{INK2};margin:0}}
.enc-testa-sez{{display:flex;justify-content:space-between;align-items:baseline;gap:24px;padding-top:24px;border-top:1px solid {LINE};
  margin-bottom:96px}}
.enc-btn.enc-btn{{display:inline-flex;align-items:center;justify-content:center;font-family:{STACK};font-size:12px;line-height:1;
  font-weight:500;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;padding:16px 24px;border:1px solid {INK};
  border-radius:999px;background:{INK};color:{PAPER};cursor:pointer;transition:none;box-shadow:none;white-space:nowrap}}
.enc-btn.enc-btn:hover,.enc-btn.enc-btn:focus-visible{{background:{PAPER};color:{INK};border-color:{INK}}}
.enc-btn.enc-chiaro{{background:{PAPER};color:{INK};border-color:{PAPER}}}
.enc-btn.enc-chiaro:hover,.enc-btn.enc-chiaro:focus-visible{{background:transparent;color:{PAPER};border-color:{PAPER}}}
.enc-fig{{margin:0;overflow:hidden;border-radius:6px;background:{MIST}}}
.enc-fig img{{display:block;width:100%;height:100%;object-fit:cover;transform:scale(1);transition:transform 1.6s ease}}
.enc-fig:hover img{{transform:scale(1.03)}}
[class*="enc-"] a:focus-visible,[class*="enc-"] button:focus-visible,[class*="enc-"] input:focus-visible,
[class*="enc-"] textarea:focus-visible,[class*="enc-"] summary:focus-visible{{outline:2px solid currentColor;outline-offset:4px}}
@media (max-width:1024px){{
  .enc-c{{padding-left:32px;padding-right:32px}}
  .enc-sez{{padding-top:120px;padding-bottom:120px}}
  .enc-h1{{font-size:68px}}.enc-h2{{font-size:46px}}.enc-big{{font-size:36px}}
  .enc-testa-sez{{margin-bottom:64px}}
}}
@media (max-width:767px){{
  .enc-c{{padding-left:16px;padding-right:16px}}
  .enc-sez{{padding-top:88px;padding-bottom:88px}}
  .enc-h1{{font-size:46px;line-height:1.06;letter-spacing:-0.03em}}.enc-h2{{font-size:36px}}.enc-big{{font-size:28px;line-height:1.22}}
  .enc-h3{{font-size:22px}}.enc-p{{font-size:16px}}
  .enc-testa-sez{{margin-bottom:48px}}
}}
@media (prefers-reduced-motion:reduce){{.enc-fig img{{transition:none}}.enc-fig:hover img{{transform:none}}}}
"""


def srcset(nome, larghezze):
    return ', '.join(f'{img(f"{nome}-{x}.webp")} {x}w' for x in larghezze)


def foto(nome, larghezze, alt, w, h, sizes, prima=False, css=''):
    """<figure> con srcset WebP; la prima immagine non è lazy e ha priorità alta."""
    extra = ' fetchpriority="high"' if prima else ' loading="lazy"'
    return (f'<figure class="enc-fig {css}"><img src="{img(f"{nome}-{larghezze[-1]}.webp")}" srcset="{srcset(nome, larghezze)}" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" decoding="async"{extra}></figure>')


def testa_sez(sx, dx=''):
    """Riga d'apertura delle sezioni alla maniera di Evox: filetto, etichetta a sinistra, etichetta a destra."""
    destra = f'<p class="enc-label">{dx}</p>' if dx else ''
    return f'<div class="enc-testa-sez"><p class="enc-label">{sx}</p>{destra}</div>'


def sezione(html, css='', ancora=None, bg=PAPER):
    return C(RAW(html, css=css), pad='0', gap='0', boxed=False, tag='section', bg=bg, anchor=ancora)


NAV = [('The loop', '#loop'), ('Why Encore', '#why'), ('Compare', '#compare'), ('Pilot', '#pilot')]


# ---------------------------------------------------------------------------------------------
# Header e footer
# ---------------------------------------------------------------------------------------------
def header():
    voci = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in NAV)
    # in Elementor i widget HTML non caricano i Google Fonts: il link sta qui, nella prima sezione della pagina
    html = f"""<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="{m.GOOGLE_FONTS}">
<header class="enc-testa"><div class="enc-c enc-testa-in">
<a class="enc-marchio" href="#top" aria-label="Encore, back to top">{LOGO_BIANCO}</a>
<nav aria-label="Main"><ul class="enc-nav">{voci}</ul></nav>
<a class="enc-btn enc-btn enc-chiaro enc-testa-btn" href="#contact">Book a pilot</a>
<details class="enc-menu"><summary>Menu</summary><ul>{voci}<li><a href="#contact">Book a pilot</a></li></ul></details>
</div></header>
<script>document.querySelectorAll('.enc-menu a').forEach(function(a){{a.addEventListener('click',function(){{a.closest('details').open=false}})}})</script>"""
    css = CSS_COMUNE + f"""
.enc-testa{{position:absolute;top:0;left:0;right:0;z-index:20}}
.enc-testa-in{{display:flex;align-items:center;gap:40px;height:88px;position:relative}}
.enc-marchio{{display:block;line-height:0;text-decoration:none;margin-right:auto}}
.enc-marchio svg{{height:30px;width:auto;display:block}}
.enc-nav{{display:flex;gap:32px;list-style:none;margin:0;padding:0}}
.enc-nav a{{font-family:{STACK};font-size:14px;color:{PAPER};text-decoration:none;display:inline-block;padding:8px 0}}
.enc-nav a:hover{{text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:1px}}
.enc-menu{{display:none}}
.enc-menu summary{{list-style:none;cursor:pointer;font-family:{STACK};font-size:12px;font-weight:500;letter-spacing:0.14em;
  text-transform:uppercase;color:{PAPER};padding:16px 0}}
.enc-menu summary::-webkit-details-marker{{display:none}}
.enc-menu ul{{position:absolute;left:16px;right:16px;top:72px;list-style:none;margin:0;padding:8px 24px;background:{PAPER};
  border-radius:6px}}
.enc-menu li a{{display:block;padding:16px 0;font-family:{STACK};font-size:16px;color:{INK};text-decoration:none;
  border-bottom:1px solid {LINE}}}
.enc-menu li:last-child a{{border-bottom:0}}
@media (max-width:900px){{
  .enc-testa-in{{height:72px}}.enc-marchio svg{{height:26px}}
  .enc-testa nav,.enc-testa .enc-testa-btn.enc-testa-btn{{display:none}}.enc-menu{{display:block}}
}}"""
    return C(RAW(html, css=css), pad='0', gap='0', boxed=False, tag='div', anchor='top')


def footer():
    voci = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in NAV)
    html = f"""<footer class="enc-piede">
<div class="enc-c enc-piede-in">
<div class="enc-piede-alto">
<a class="enc-piede-logo" href="#top" aria-label="Encore, back to top">{LOGO_BIANCO}</a>
<a class="enc-btn enc-btn enc-chiaro" href="#contact">Book a pilot</a>
</div>
<div class="enc-piede-mezzo">
<nav aria-label="Footer"><ul class="enc-piede-nav">{voci}</ul></nav>
<p class="enc-label enc-piede-riga">ENCORE · Team Second Thread · Startup Generation Challenge Verona 2026 · Sfida 02 &quot;Da scarto a risorsa&quot;</p>
</div>
</div>
<div class="enc-piede-marchio" aria-hidden="true"></div>
</footer>"""
    css = f"""
.enc-piede{{background:{DARK};color:{PAPER};overflow:hidden;position:relative}}
.enc-piede-in{{padding-top:120px}}
.enc-piede-alto{{display:flex;justify-content:space-between;align-items:center;gap:32px;padding-bottom:64px}}
.enc-piede-logo{{display:block;line-height:0}}
.enc-piede-logo svg{{height:40px;width:auto;display:block}}
.enc-piede-mezzo{{display:flex;justify-content:space-between;align-items:baseline;gap:32px;padding-top:32px;border-top:1px solid #2A2A2E;flex-wrap:wrap}}
.enc-piede-nav{{display:flex;gap:40px;list-style:none;margin:0;padding:0}}
.enc-piede-nav a{{font-family:{STACK};font-size:15px;color:{PAPER};text-decoration:none;display:inline-block;padding:8px 0}}
.enc-piede-nav a:hover{{text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:1px}}
.enc-piede-riga{{color:{ON_DARK2};text-align:right}}
.enc-piede-marchio{{font-family:{STACK};font-weight:500;font-size:23vw;line-height:0.74;letter-spacing:-0.02em;color:#1B1B1F;
  text-align:center;white-space:nowrap;user-select:none;margin-top:96px;transform:translateY(14%)}}
.enc-piede-marchio::before{{content:'ENCORE'}}
@media (min-width:1600px){{.enc-piede-marchio{{font-size:368px}}}}
@media (max-width:767px){{.enc-piede-in{{padding-top:80px}}.enc-piede-alto{{flex-direction:column;align-items:flex-start;padding-bottom:48px}}
  .enc-piede-logo svg{{height:32px}}.enc-piede-nav{{flex-wrap:wrap;gap:8px 24px}}.enc-piede-riga{{text-align:left}}
  .enc-piede-marchio{{margin-top:64px}}}}"""
    return C(RAW(html, css=css), pad='0', gap='0', boxed=False, tag='div', bg=DARK)


# ---------------------------------------------------------------------------------------------
# Landing
# ---------------------------------------------------------------------------------------------
def hero():
    html = f"""<div class="enc-hero">
<video class="enc-hero-video" muted loop playsinline preload="none" aria-hidden="true" poster="{img('hero-poster-1280.webp')}"
 data-d="{img('hero-loop-1280')}" data-m="{img('hero-loop-576')}" data-pm="{img('hero-poster-576.webp')}"></video>
<div class="enc-hero-velo"></div>
<div class="enc-c enc-hero-in">
<div class="enc-hero-testo">
<h1 class="enc-t enc-h1">Your textile waste, back in your next collection.</h1>
<p class="enc-p">Encore is a closed-loop service that collects luxury brands' textile waste, sorts it by fibre, recycles it and sells the fibre back to them.</p>
<div><a class="enc-btn enc-btn enc-chiaro" href="#contact">Book a pilot</a></div>
</div>
<p class="enc-label enc-hero-nota">Team Second Thread · Startup Generation Challenge Verona 2026</p>
</div>
</div>
<script>(function(){{var v=document.querySelector('.enc-hero-video');if(!v)return;var m=window.matchMedia('(max-width:767px)').matches;
if(m)v.poster=v.dataset.pm;if(window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var ext=v.canPlayType('video/webm; codecs="vp9"')?'.webm':'.mp4';
var go=function(){{v.src=(m?v.dataset.m:v.dataset.d)+ext;v.play().catch(function(){{}});}};
var later=function(){{setTimeout(go,2500);}};
if(document.readyState==='complete')later();else window.addEventListener('load',later);}})();</script>"""
    css = f"""
.enc-hero{{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:flex-end;background:{DARK};overflow:hidden}}
.enc-hero-video{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%;background:{DARK}}}
.enc-hero-velo{{position:absolute;inset:0;background:linear-gradient(to top,rgba(11,11,12,0.82) 0%,rgba(11,11,12,0.45) 55%,rgba(11,11,12,0.35) 100%)}}
.enc-hero-in{{position:relative;width:100%;display:flex;justify-content:space-between;align-items:flex-end;gap:48px;
  padding-top:160px;padding-bottom:64px}}
.enc-hero-testo{{display:flex;flex-direction:column;gap:32px;max-width:860px}}
.enc-hero-testo .enc-h1{{color:{PAPER}}}
.enc-hero-testo .enc-p{{color:rgba(255,255,255,0.86);max-width:30em}}
.enc-hero-nota{{color:rgba(255,255,255,0.78);text-align:right;max-width:30em}}
@media (max-width:900px){{.enc-hero-in{{flex-direction:column;align-items:flex-start;gap:40px}}.enc-hero-nota{{text-align:left}}}}
@media (max-width:767px){{.enc-hero-in{{padding-bottom:40px}}.enc-hero-testo{{gap:24px}}}}"""
    return sezione(html, css, bg=DARK)


# titolo a sinistra, testo a destra (sezioni "The problem" e "The first loop", come "What we do" di Evox)
CSS_DUE_COL = """
.enc-due-col{display:grid;grid-template-columns:7fr 5fr;gap:64px;align-items:start}
.enc-due-col .enc-h2{max-width:11em}
.enc-due-col .enc-p{padding-top:12px}
@media (max-width:900px){.enc-due-col{grid-template-columns:1fr;gap:32px}.enc-due-col .enc-p{padding-top:0}}"""


def problema():
    html = f"""<div class="enc-c enc-sez">
{testa_sez('The problem')}
<div class="enc-due-col">
<h2 class="enc-t enc-h2">What happens to your unsold cashmere?</h2>
<p class="enc-p">Every season, high-end brands are left with unsold stock, returns and offcuts in premium wool, cashmere and linen. Destroying them is increasingly illegal in Europe. Recyclers exist, but each works differently, with no shared standard and no proof of where fibre ends up. So most of it is lost.</p>
</div>
</div>"""
    return sezione(html, CSS_DUE_COL)


def intuizione():
    html = """<div class="enc-c enc-intu">
<p class="enc-label">Insight</p>
<p class="enc-t enc-big">The recycling technology already exists. What's missing is trust between brands and recyclers: one shared standard and one record nobody can alter.</p>
</div>"""
    css = """
.enc-intu{min-height:100vh;min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;
  text-align:center;padding-top:160px;padding-bottom:160px}
.enc-intu .enc-big{max-width:21em;font-size:52px}
@media (max-width:1024px){.enc-intu .enc-big{font-size:40px}}
@media (max-width:767px){.enc-intu{min-height:0;padding-top:120px;padding-bottom:120px;gap:32px}.enc-intu .enc-big{font-size:30px}}"""
    return sezione(html, css, bg=MIST)


def soluzione():
    html = f"""<div class="enc-c enc-sez enc-sol">
{testa_sez('The solution')}
<div class="enc-sol-griglia">
<div class="enc-sol-testo">
<h2 class="enc-t enc-h2">One standard, one loop, every kilo certified.</h2>
<p class="enc-p">You hand over unsold stock, returns and offcuts. Infrared scanners identify each item's fibre and the batch goes to the best certified recycler in our network. Every step is certified on blockchain. Our AI lets you ask, in plain language, where any kilo came from. Buy back the recycled fibre through Encore at a discount.</p>
</div>
{ciclo_svg()}
</div>
<figure class="enc-fig enc-sol-foto"><img src="{img('solution-wide-1600.webp')}" srcset="{srcset('solution-wide', (900, 1600, 2400))}"
 sizes="(max-width:1440px) 100vw, 1344px" width="1600" height="700" alt="Close-up of cable knit wool" loading="lazy" decoding="async"></figure>
</div>"""
    css = """
.enc-sol-griglia{display:grid;grid-template-columns:6fr 6fr;gap:64px;align-items:center;margin-bottom:120px}
.enc-sol-testo{display:flex;flex-direction:column;gap:32px}
.enc-sol-testo .enc-h2{max-width:11em}
.enc-ciclo{width:100%;max-width:680px;justify-self:end;display:block;overflow:visible}
.enc-ciclo text{font-family:'Instrument Sans',Helvetica,Arial,sans-serif}
.enc-ciclo-lista{display:none}
@media (max-width:900px){.enc-sol-griglia{grid-template-columns:1fr;gap:56px;margin-bottom:80px}.enc-ciclo{justify-self:center}}
.enc-sol-foto{aspect-ratio:16/7}
@media (max-width:767px){.enc-sol-testo{gap:24px}.enc-sol-foto{aspect-ratio:4/3}
  .enc-ciclo{max-width:300px;overflow:hidden}.enc-ciclo .enc-lbl{display:none}
  .enc-ciclo-lista{display:grid;gap:12px;list-style:none;margin:-24px 0 0;padding:0;font-family:'Instrument Sans',Helvetica,Arial,sans-serif;font-size:16px;color:#131316}
  .enc-ciclo-lista li{display:flex;gap:16px;padding-top:12px;border-top:1px solid #E4E4E0}
  .enc-ciclo-lista span{color:#6F7075;font-size:13px;letter-spacing:0.08em;padding-top:2px}}"""
    return sezione(html, css, ancora='loop')


# il ciclo in un disegno: cinque tappe su un cerchio (nomi presi dalla tabella del brief), un punto che lo percorre lento
TAPPE = ['Unsold stock', 'NIR fibre sorting', 'Network of recyclers', 'Blockchain certificate', 'Fibre back to the brand']


def ciclo_svg():
    import math
    cx, cy, r = 400, 400, 250
    parti = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LINE}" stroke-width="2"/>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="2 10" '
             f'stroke-linecap="round" opacity="0.35"/>']
    for i, t in enumerate(TAPPE):
        a = math.radians(-90 + i * 72)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        lx, ly = cx + (r + 44) * math.cos(a), cy + (r + 44) * math.sin(a)
        anc = 'middle' if abs(math.cos(a)) < 0.3 else ('start' if math.cos(a) > 0 else 'end')
        dy = -8 if math.sin(a) < -0.9 else (30 if math.sin(a) > 0.5 else 10)
        parti.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>')
        parti.append(f'<text class="enc-lbl" x="{lx:.1f}" y="{ly + dy:.1f}" text-anchor="{anc}" font-size="25" fill="{INK}">{t}</text>')
        parti.append(f'<text class="enc-lbl" x="{lx:.1f}" y="{ly + dy - 32:.1f}" text-anchor="{anc}" font-size="17" letter-spacing="2" '
                     f'fill="{INK3}">0{i + 1}</text>')
    percorso = f'M {cx} {cy - r} A {r} {r} 0 1 1 {cx - 0.01} {cy - r} Z'
    parti.append(f'<circle r="7" fill="{INK}"><animateMotion dur="16s" repeatCount="indefinite" path="{percorso}"/></circle>')
    parti.append(f'<text x="{cx}" y="{cy + 10}" text-anchor="middle" font-size="30" font-weight="600" letter-spacing="10" fill="{INK}">ENCORE</text>')
    return ('<svg class="enc-ciclo" viewBox="-80 40 960 760" role="img" aria-label="The Encore loop: unsold stock, NIR fibre sorting, '
            'network of recyclers, blockchain certificate, fibre back to the brand">' + ''.join(parti) + '</svg>'
            '<ol class="enc-ciclo-lista" aria-hidden="true">'
            + ''.join(f'<li><span>0{i + 1}</span>{t}</li>' for i, t in enumerate(TAPPE)) + '</ol>'
            "<script>(function(){var s=document.querySelector('.enc-ciclo');"
            "if(s&&window.matchMedia('(prefers-reduced-motion:reduce)').matches&&s.pauseAnimations)s.pauseAnimations();})();</script>")


PASSI = [
    ('01', 'Hand over your waste.',
     'Unsold stock, returns and offcuts are collected. Infrared scanners identify each item\'s exact fibre in seconds.',
     'step-handover', 'Folded wool and cashmere knitwear in warm neutral tones'),
    ('02', 'Matched and certified.',
     'Every batch goes to the partner best suited to its fibre. Each scan and handover is certified on blockchain.',
     'how-yarn-cones', 'Cones of recycled yarn by a mill window'),
    ('03', 'Ask, verify, buy back.',
     'Ask our AI anything about your fibre in plain language. Buy it back at a discount, certified.',
     'cta-wool-macro', 'Macro photograph of woven wool'),
]


def come_funziona():
    schede = ''.join(f"""<li class="enc-passo">
{foto(f, (800, 1400), alt, 1400, 1750, '(max-width:900px) 100vw, 33vw', css='enc-passo-foto')}
<h3 class="enc-t enc-h3"><span class="enc-passo-n">{n}</span>{t}</h3>
<p class="enc-p">{d}</p></li>""" for n, t, d, f, alt in PASSI)
    html = f"""<div class="enc-c enc-sez enc-come">
{testa_sez('How it works')}
<ol class="enc-passi">{schede}</ol>
</div>"""
    css = f"""
.enc-come{{padding-top:0}}
.enc-passi{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.enc-passo{{display:flex;flex-direction:column;gap:16px;min-width:0}}
.enc-passo-foto{{aspect-ratio:4/5;margin-bottom:8px}}
.enc-passo .enc-h3{{display:flex;gap:16px;align-items:baseline}}
.enc-passo-n{{font-size:14px;letter-spacing:0.08em;color:{INK3};font-variant-numeric:tabular-nums}}
.enc-passo .enc-p{{font-size:16px;max-width:26em}}
@media (max-width:900px){{.enc-passi{{grid-template-columns:1fr;gap:56px}}.enc-passo-foto{{aspect-ratio:3/2}}}}"""
    return sezione(html, css)


def per_chi():
    html = """<div class="enc-c enc-sez enc-perchi">
<p class="enc-label">Who it's for</p>
<p class="enc-t enc-big">For high-end fashion brands that, at the end of every season, face unsold stock, returns and premium offcuts they can neither sell nor destroy.</p>
</div>"""
    css = f"""
.enc-perchi{{display:grid;grid-template-columns:3fr 9fr;gap:64px;align-items:start;border-top:1px solid {LINE}}}
.enc-perchi .enc-label{{padding-top:16px}}
.enc-perchi .enc-big{{max-width:22em}}
@media (max-width:900px){{.enc-perchi{{grid-template-columns:1fr;gap:24px}}.enc-perchi .enc-label{{padding-top:0}}}}"""
    return sezione(html, css)


PUNTI = [
    'One partner instead of dozens of recyclers to vet',
    'A certificate no one can falsify',
    'Answers in plain language, not spreadsheets',
    'Your products never reach the grey market',
]


def perche():
    punti = ''.join(f'<li><p class="enc-t">{p}</p></li>' for p in PUNTI)
    html = f"""<div class="enc-c enc-sez enc-perche">
<div class="enc-testa-sez"><p class="enc-label">Why Encore</p></div>
<p class="enc-t enc-big">Your unsold stock is frozen capital. <span class="enc-tenue">Encore turns it into fibre you buy back below market price, protecting your brand and your margin.</span></p>
<ul class="enc-punti">{punti}</ul>
</div>"""
    css = f"""
.enc-perche .enc-testa-sez{{border-top-color:#2A2A2E}}
.enc-perche .enc-label{{color:{ON_DARK2}}}
.enc-perche .enc-big{{color:{PAPER};max-width:21em;font-size:52px}}
.enc-tenue{{color:{ON_DARK2}}}
.enc-punti{{list-style:none;margin:120px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:32px}}
.enc-punti li{{padding-top:24px;border-top:1px solid #3A3A3F}}
.enc-punti .enc-t{{color:{PAPER};font-size:19px;line-height:1.35;letter-spacing:-0.01em;max-width:14em}}
@media (max-width:1024px){{.enc-perche .enc-big{{font-size:40px}}.enc-punti{{grid-template-columns:repeat(2,1fr);gap:40px 32px}}}}
@media (max-width:767px){{.enc-perche .enc-big{{font-size:30px}}.enc-punti{{grid-template-columns:1fr;margin-top:64px;gap:24px}}}}"""
    return sezione(html, css, ancora='why', bg=DARK)


COLONNE = ['Takes back the brand\'s own stock', 'NIR fibre sorting', 'Network of recyclers', 'Blockchain certificate',
           'Fibre back to the same brand']
RIGHE = [
    ('Encore', [1, 1, 1, 1, 1]),
    ('Re.Verso', [0, 0, 0, 0, 0]),
    ('Manteco', [0, 0, 0, 0, 0]),
    ('TextileGenesis', [0, 0, 0, 1, 0]),
    ('Reverse Resources', [0, 0, 1, 0, 0]),
    ('Fibersort', [0, 1, 0, 0, 0]),
]


def confronto():
    testa = ''.join(f'<th scope="col">{escape(x)}</th>' for x in COLONNE)
    righe = ''
    for nome, vals in RIGHE:
        celle = ''.join('<td><span class="enc-dot" aria-hidden="true"></span><span class="enc-sr">Yes</span></td>' if v
                        else '<td><span class="enc-sr">No</span></td>' for v in vals)
        cls = ' class="enc-noi"' if nome == 'Encore' else ''
        righe += f'<tr{cls}><th scope="row">{nome}</th>{celle}</tr>'
    html = f"""<div class="enc-c enc-sez enc-conf">
{testa_sez('Compare')}
<h2 class="enc-t enc-h2" id="enc-conf-t">Others do one step. Encore closes the loop.</h2>
<div class="enc-tab" role="region" aria-labelledby="enc-conf-t" tabindex="0">
<table><thead><tr><th scope="col"><span class="enc-sr">Company</span></th>{testa}</tr></thead><tbody>{righe}</tbody></table>
</div>
<p class="enc-small enc-conf-nota">Based on each company's public offering, October 2026. Re.Verso and Manteco produce certified recycled wool and cashmere; TextileGenesis traces fibre on blockchain; Reverse Resources matches factory leftovers with recyclers; Fibersort builds NIR sorting machines.</p>
</div>"""
    css = f"""
.enc-conf{{min-width:0}}
.enc-conf .enc-h2{{max-width:12em;margin-bottom:80px}}
.enc-tab{{position:relative;overflow-x:auto;-webkit-overflow-scrolling:touch;min-width:0;max-width:100%}}
.enc-tab table{{width:100%;min-width:760px;border-collapse:separate;border-spacing:0;font-family:{STACK};color:{INK};
  background:transparent;border:0;margin:0}}
.enc-tab th,.enc-tab td{{border:0;border-bottom:1px solid {LINE};padding:24px 16px;text-align:center;vertical-align:middle;
  background:transparent;font-weight:400}}
.enc-tab thead th{{font-size:12px;line-height:1.5;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;
  vertical-align:bottom;color:{INK3};width:16%;padding-bottom:20px}}
.enc-tab tbody th{{text-align:left;font-size:18px;white-space:nowrap;padding-left:24px}}
.enc-tab thead th:first-child{{width:20%}}
.enc-dot{{display:inline-block;width:8px;height:8px;border-radius:50%;background:{INK}}}
.enc-tab tr.enc-noi th,.enc-tab tr.enc-noi td{{background:{INK};color:{PAPER};border-bottom-color:{INK}}}
.enc-tab tr.enc-noi th{{font-weight:600;letter-spacing:0.28em;font-size:15px;border-radius:6px 0 0 6px}}
.enc-tab tr.enc-noi td:last-child{{border-radius:0 6px 6px 0}}
.enc-tab tr.enc-noi .enc-dot{{background:{PAPER}}}
.enc-conf-nota{{color:{INK3};max-width:56em;margin-top:40px}}
@media (max-width:767px){{.enc-conf .enc-h2{{margin-bottom:48px}}}}"""
    return sezione(html, css, ancora='compare')


def primo_ciclo():
    html = f"""<div class="enc-c enc-sez">
{testa_sez('Where we start', 'MVP')}
<div class="enc-due-col">
<h2 class="enc-t enc-h2">The first loop</h2>
<p class="enc-p">One brand, one recycler, one batch of unsold wool knitwear. A handheld infrared scanner identifies every item, each step is certified on a blockchain, an AI assistant answers questions on the data, and the brand buys back the yarn discounted.</p>
</div>
</div>"""
    return sezione(html, CSS_DUE_COL, ancora='pilot', bg=MIST)


def risultato():
    html = f"""<div class="enc-ris">
<img class="enc-ris-img" src="{img('result-knit-1600.webp')}" srcset="{srcset('result-knit', (900, 1600, 2400))}" sizes="100vw"
 width="1600" height="900" alt="A model wearing a neutral wool knit sweater" loading="lazy" decoding="async">
<div class="enc-ris-velo"></div>
<div class="enc-c enc-ris-testo"><p class="enc-label">The result</p>
<p class="enc-t enc-big">Your end-of-season stock stops being a cost and a risk, and becomes cheaper fibre for your next collection.</p></div>
</div>"""
    css = f"""
.enc-ris{{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;background:{DARK}}}
.enc-ris-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:30% 30%}}
.enc-ris-velo{{position:absolute;inset:0;background:linear-gradient(to top,rgba(11,11,12,0.86) 0%,rgba(11,11,12,0.5) 50%,rgba(11,11,12,0.3) 100%)}}
.enc-ris-testo{{position:relative;width:100%;display:flex;flex-direction:column;gap:32px;padding-top:160px;padding-bottom:96px}}
.enc-ris-testo .enc-label{{color:rgba(255,255,255,0.78)}}
.enc-ris-testo .enc-big{{color:{PAPER};max-width:19em;font-size:52px}}
@media (max-width:1024px){{.enc-ris-testo .enc-big{{font-size:40px}}}}
@media (max-width:767px){{.enc-ris{{min-height:620px}}.enc-ris-testo{{padding-bottom:56px}}.enc-ris-testo .enc-big{{font-size:30px}}}}"""
    return sezione(html, css, bg=DARK)


def contatti():
    campo = ('<label class="enc-campo{x}" for="enc-{n}"><span class="enc-label">{l}</span>'
             '<input class="enc-input enc-input" id="enc-{n}" name="{n}" type="{t}" autocomplete="{a}" required></label>')
    campi = ''.join(campo.format(l=l, n=n, t=t, a=a, x=x) for l, n, t, a, x in (
        ('Name', 'name', 'text', 'name', ''), ('Brand', 'brand', 'text', 'organization', ''),
        ('Email', 'email', 'email', 'email', ' enc-campo-pieno')))
    html = f"""<div class="enc-cta">
<div class="enc-cta-foto">
<img src="{img('cta-wool-macro-1400.webp')}" srcset="{srcset('cta-wool-macro', (800, 1400))}" sizes="(max-width:900px) 100vw, 50vw"
 width="1400" height="1750" alt="Macro photograph of woven wool" loading="lazy" decoding="async">
<div class="enc-cta-velo"></div>
<p class="enc-label enc-cta-nota">Pilot · Startup Generation Challenge Verona 2026</p>
</div>
<div class="enc-cta-modulo">
<div class="enc-cta-in">
<h2 class="enc-t enc-h2">Start your first loop.</h2>
<form class="enc-form" id="enc-form" novalidate>
{campi}
<label class="enc-campo enc-campo-pieno" for="enc-message"><span class="enc-label">Message</span><textarea class="enc-input enc-input" id="enc-message" name="message" rows="3"></textarea></label>
<button class="enc-btn enc-btn enc-invia" type="submit">Book a pilot</button>
</form>
<p class="enc-t enc-grazie" id="enc-grazie" tabindex="-1" hidden>Thank you.</p>
</div>
</div>
</div>
<script>(function(){{var f=document.getElementById('enc-form'),g=document.getElementById('enc-grazie');if(!f)return;
f.addEventListener('submit',function(e){{e.preventDefault();if(!f.checkValidity()){{f.reportValidity();return;}}
f.hidden=true;g.hidden=false;g.focus();}});}})();</script>"""
    css = f"""
.enc-cta{{display:grid;grid-template-columns:1fr 1fr;min-height:100vh;min-height:100svh}}
.enc-cta-foto{{position:relative;overflow:hidden;background:{DARK};min-height:560px}}
.enc-cta-foto img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scale(1);transition:transform 1.6s ease}}
.enc-cta-foto:hover img{{transform:scale(1.03)}}
.enc-cta-velo{{position:absolute;inset:0;background:linear-gradient(to top,rgba(11,11,12,0.7) 0%,rgba(11,11,12,0.1) 45%)}}
.enc-cta-nota{{position:absolute;left:48px;bottom:48px;color:rgba(255,255,255,0.86)}}
.enc-cta-modulo{{display:flex;align-items:center;background:{PAPER}}}
.enc-cta-in{{width:100%;max-width:640px;padding:120px 96px}}
.enc-cta-in .enc-h2{{margin-bottom:72px}}
.enc-form{{display:grid;grid-template-columns:1fr 1fr;gap:40px 32px}}
.enc-campo{{display:flex;flex-direction:column;gap:12px;min-width:0}}
.enc-campo-pieno{{grid-column:1/-1}}
.enc-input.enc-input{{font-family:{STACK};font-size:20px;line-height:1.4;color:{INK};background:transparent;border:0;
  border-bottom:1px solid #CFCFCA;border-radius:0;padding:4px 0 14px;width:100%;box-shadow:none;outline:none}}
.enc-input.enc-input:hover{{border-bottom-color:{INK3}}}
.enc-input.enc-input:focus{{border-bottom-color:{INK};box-shadow:0 1px 0 {INK}}}
.enc-input.enc-input:focus-visible{{outline:none}}
textarea.enc-input.enc-input{{resize:none;min-height:96px}}
.enc-btn.enc-invia{{grid-column:1/-1;width:100%;padding:24px 32px;font-size:13px;margin-top:16px}}
.enc-grazie{{font-size:60px;line-height:1.06;letter-spacing:-0.028em}}
.enc-form[hidden],.enc-grazie[hidden]{{display:none}}
@media (max-width:1100px){{.enc-cta-in{{padding:96px 48px}}}}
@media (max-width:900px){{.enc-cta{{grid-template-columns:1fr;min-height:0}}.enc-cta-foto{{min-height:0;aspect-ratio:4/3}}
  .enc-cta-in{{max-width:none;padding:88px 32px}}}}
@media (max-width:767px){{.enc-cta-nota{{left:16px;bottom:24px}}.enc-cta-in{{padding:72px 16px}}.enc-cta-in .enc-h2{{margin-bottom:48px}}
  .enc-form{{grid-template-columns:1fr;gap:32px}}.enc-grazie{{font-size:40px}}}}"""
    return sezione(html, css, ancora='contact')


def landing():
    return [('hero', hero()), ('problem', problema()), ('insight', intuizione()), ('solution', soluzione()),
            ('how-it-works', come_funziona()), ('who', per_chi()), ('why', perche()), ('compare', confronto()),
            ('first-loop', primo_ciclo()), ('result', risultato()), ('contact', contatti())]


PAGINE = [
    {'slug': '01-home', 'titolo': 'Landing', 'sezioni': landing,
     'titolo_seo': 'Encore | Your textile waste, back in your next collection',
     'descrizione': ('Encore is a closed-loop service that collects luxury brands\' textile waste, sorts it by fibre, '
                     'recycles it and sells the fibre back to them.')},
]
