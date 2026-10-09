# -*- coding: utf-8 -*-
"""
Contenuti della landing page di Encore (Startup Generation Challenge Verona 2026, Sfida 02 "Da scarto a risorsa").
Stesso generatore di Benvegnù (motore.py, build.py): template Elementor, fallback HTML per sezione, anteprima.
Ogni sezione è un widget HTML (RAW) dentro un contenitore: il layout editoriale (immagini al vivo, tabella, modulo)
non ha un equivalente nei widget gratuiti di Elementor. Gli stili comuni stanno nella sezione header.
Testi: esattamente quelli del brief, in inglese.
"""
from html import escape

import motore as m
from motore import C, RAW

PREFISSO = 'enc'
NOME_SITO = 'Encore'
m.LINGUA = 'en'

# ---------------------------------------------------------------------------------------------
# Tema
# ---------------------------------------------------------------------------------------------
IVORY = '#F4F0E8'
INK = '#151412'
STONE = '#8C857B'          # filetti e testo secondario su fondo scuro (5,05:1 su INK)
STONE_TXT = '#6E685F'      # testo secondario piccolo su IVORY: lo STONE del brief arriva a 3,2:1, sotto la soglia AA
OX = '#4A1C1A'             # accento: pulsanti e riga Encore della tabella

SERIF = 'Bodoni Moda'
SANS = 'Jost'

m.applica_tema({
    'nome': 'Encore',
    'fondo': IVORY, 'superficie': IVORY, 'inchiostro': INK, 'testo2': STONE_TXT, 'accento': OX,
    'filetto': STONE, 'filetto_scuro': STONE, 'su_scuro2': STONE,
    'scuro': INK, 'su_scuro': IVORY, 'su_accento': IVORY,
    'font_titoli': SERIF, 'font_testo': SANS, 'larghezza': 1440,
    'google_fonts': ('https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400'
                     '&family=Jost:wght@400;500&display=swap'),
})

BASE_PREDEFINITA = 'https://raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Encore-Sito/assets/web/'
BASE = BASE_PREDEFINITA


def imposta_base(base):
    global BASE
    BASE = base if base.endswith('/') else base + '/'


def img(nome):
    return BASE + nome


# ---------------------------------------------------------------------------------------------
# Scala 8 px e stili comuni (una sola volta, nella sezione header)
# ---------------------------------------------------------------------------------------------
# lato: 64 desktop, 40 tablet, 16 telefono; sezione: 160 / 112 / 80
CSS_COMUNE = f"""
.enc-sr{{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(1px,1px,1px,1px);white-space:nowrap}}
.enc-in{{padding-left:64px;padding-right:64px}}
.enc-sez{{padding-top:160px;padding-bottom:160px}}
.enc-serif{{font-family:'{SERIF}',Didot,'Bodoni 72',Georgia,serif;font-weight:400;font-style:normal;letter-spacing:-0.01em}}
.enc-h1{{font-size:88px;line-height:1.02;margin:0}}
.enc-h2{{font-size:56px;line-height:1.06;margin:0}}
.enc-big{{font-size:48px;line-height:1.16;margin:0}}
.enc-p{{font-family:'{SANS}',Arial,sans-serif;font-size:18px;line-height:1.6;font-weight:400;margin:0;max-width:34em}}
.enc-label{{font-family:'{SANS}',Arial,sans-serif;font-size:12px;line-height:1.5;font-weight:500;letter-spacing:0.14em;
  text-transform:uppercase;margin:0}}
.enc-small{{font-family:'{SANS}',Arial,sans-serif;font-size:14px;line-height:1.6;margin:0}}
.enc-btn.enc-btn{{display:inline-block;font-family:'{SANS}',Arial,sans-serif;font-size:12px;line-height:1;font-weight:500;
  letter-spacing:0.14em;text-transform:uppercase;text-decoration:none;padding:20px 32px;border:1px solid {OX};border-radius:0;
  background:{OX};color:{IVORY};cursor:pointer;transition:none;box-shadow:none}}
.enc-btn.enc-btn:hover,.enc-btn.enc-btn:focus-visible{{background:{IVORY};color:{OX};border-color:{OX}}}
.enc-btn.enc-linea{{background:transparent;color:{INK};border-color:{INK};padding:16px 24px}}
.enc-btn.enc-linea:hover,.enc-btn.enc-linea:focus-visible{{background:{INK};color:{IVORY};border-color:{INK}}}
.enc-fig{{margin:0;overflow:hidden;background:#DDD6CA}}
.enc-fig img{{display:block;width:100%;height:100%;object-fit:cover;transform:scale(1);transition:transform 1.6s ease}}
.enc-fig:hover img{{transform:scale(1.03)}}
[class*="enc-"] a:focus-visible,[class*="enc-"] button:focus-visible,[class*="enc-"] input:focus-visible,
[class*="enc-"] textarea:focus-visible,[class*="enc-"] summary:focus-visible{{outline:2px solid {OX};outline-offset:4px}}
.enc-scuro [class*="enc-"] a:focus-visible{{outline-color:{IVORY}}}
@media (max-width:1024px){{
  .enc-in{{padding-left:40px;padding-right:40px}}
  .enc-sez{{padding-top:112px;padding-bottom:112px}}
  .enc-h1{{font-size:64px}}.enc-h2{{font-size:44px}}.enc-big{{font-size:38px}}
}}
@media (max-width:767px){{
  .enc-in{{padding-left:16px;padding-right:16px}}
  .enc-sez{{padding-top:80px;padding-bottom:80px}}
  .enc-h1{{font-size:44px;line-height:1.06}}.enc-h2{{font-size:36px}}.enc-big{{font-size:30px;line-height:1.2}}
  .enc-p{{font-size:17px}}
}}
@media (prefers-reduced-motion:reduce){{.enc-fig img{{transition:none}}.enc-fig:hover img{{transform:none}}}}
"""


def foto(nome, larghezze, alt, w, h, sizes, prima=False, css=''):
    """<figure> con srcset WebP; la prima immagine (hero) non è lazy e ha priorità alta."""
    srcset = ', '.join(f'{img(f"{nome}-{x}.webp")} {x}w' for x in larghezze)
    extra = ' fetchpriority="high"' if prima else ' loading="lazy"'
    return (f'<figure class="enc-fig {css}"><img src="{img(f"{nome}-{larghezze[-1]}.webp")}" srcset="{srcset}" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{escape(alt)}" decoding="async"{extra}></figure>')


def sezione(html, css='', ancora=None, scuro=False):
    figli = [RAW(html, css=css)]
    return C(*figli, pad='0', gap='0', boxed=False, tag='section', bg=INK if scuro else IVORY, anchor=ancora)


NAV = [('The loop', '#loop'), ('Why Encore', '#why'), ('Compare', '#compare'), ('Pilot', '#pilot')]


# ---------------------------------------------------------------------------------------------
# Header e footer
# ---------------------------------------------------------------------------------------------
def header():
    voci = ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in NAV)
    html = f"""<header class="enc-testa enc-in">
<a class="enc-marchio enc-serif" href="#top" aria-label="Encore, back to top">ENCORE</a>
<nav aria-label="Main"><ul class="enc-nav enc-label">{voci}</ul></nav>
<a class="enc-btn enc-btn enc-linea enc-testa-btn" href="#contact">Book a pilot</a>
<details class="enc-menu"><summary class="enc-label">Menu</summary><ul class="enc-label">{voci}
<li><a href="#contact">Book a pilot</a></li></ul></details>
</header>
<script>document.querySelectorAll('.enc-menu a').forEach(function(a){{a.addEventListener('click',function(){{a.closest('details').open=false}})}})</script>"""
    css = CSS_COMUNE + f"""
.enc-testa{{display:flex;align-items:center;justify-content:space-between;gap:32px;height:88px;background:{IVORY};
  border-bottom:1px solid {STONE};position:relative}}
.enc-marchio{{font-size:24px;line-height:1;letter-spacing:0.32em;color:{INK};text-decoration:none;margin-right:auto}}
.enc-nav{{display:flex;gap:40px;list-style:none;margin:0;padding:0}}
.enc-nav a,.enc-menu a{{color:{INK};text-decoration:none;display:inline-block;padding:8px 0}}
.enc-nav a:hover{{text-decoration:underline;text-underline-offset:6px;text-decoration-thickness:1px}}
.enc-menu{{display:none}}
.enc-menu summary{{list-style:none;cursor:pointer;color:{INK};padding:16px 0}}
.enc-menu summary::-webkit-details-marker{{display:none}}
.enc-menu ul{{position:absolute;left:0;right:0;top:88px;z-index:20;list-style:none;margin:0;padding:8px 16px 24px;
  background:{IVORY};border-bottom:1px solid {STONE}}}
.enc-menu li a{{display:block;padding:16px 0;border-bottom:1px solid #DDD6CA}}
@media (max-width:1024px){{.enc-nav{{gap:24px}}}}
@media (max-width:900px){{
  .enc-testa{{height:72px}}.enc-menu ul{{top:72px}}
  .enc-testa nav,.enc-testa .enc-testa-btn.enc-testa-btn{{display:none}}.enc-menu{{display:block}}
  .enc-marchio{{font-size:20px}}
}}"""
    return C(RAW(html, css=css), pad='0', gap='0', boxed=False, tag='div', bg=IVORY, anchor='top')


def footer():
    html = ('<footer class="enc-piede enc-in"><p class="enc-label">ENCORE · Team Atelier Zero · '
            'Startup Generation Challenge Verona 2026 · Sfida 02 &quot;Da scarto a risorsa&quot;</p></footer>')
    css = f'.enc-piede{{background:{INK};color:{IVORY};padding-top:48px;padding-bottom:48px}}.enc-piede p{{color:{IVORY}}}'
    return C(RAW(html, css=css), pad='0', gap='0', boxed=False, tag='div', bg=INK)


# ---------------------------------------------------------------------------------------------
# Landing
# ---------------------------------------------------------------------------------------------
def hero():
    html = f"""<div class="enc-hero">
<div class="enc-hero-testo enc-in">
<h1 class="enc-serif enc-h1">Your textile waste, back in your next collection.</h1>
<p class="enc-p">Encore is a closed-loop service that collects luxury brands' textile waste, sorts it by fibre, recycles it and sells the fibre back to them.</p>
<div><a class="enc-btn enc-btn" href="#contact">Book a pilot</a>
<p class="enc-label enc-hero-nota">Team Atelier Zero · Startup Generation Challenge Verona 2026</p></div>
</div>
{foto('hero-knitwear', (800, 1400), 'Folded wool and cashmere knitwear in neutral tones', 1400, 1750,
      '(max-width:900px) 100vw, 58vw', prima=True, css='enc-hero-foto')}
</div>"""
    css = f"""
.enc-hero{{display:grid;grid-template-columns:5fr 7fr;min-height:calc(100vh - 88px);min-height:calc(100svh - 88px)}}
.enc-hero-testo{{display:flex;flex-direction:column;justify-content:center;gap:40px;padding-top:96px;padding-bottom:96px}}
.enc-hero-testo .enc-h1{{color:{INK};max-width:9.5em}}
.enc-hero-testo .enc-p{{color:{INK};max-width:28em}}
.enc-hero-nota{{color:{STONE_TXT};margin-top:24px}}
.enc-hero-foto{{min-height:560px}}
@media (max-width:1024px){{.enc-hero{{grid-template-columns:1fr 1fr}}}}
@media (max-width:900px){{
  .enc-hero{{grid-template-columns:1fr;min-height:0}}
  .enc-hero-testo{{padding-top:56px;padding-bottom:56px;gap:32px}}
  .enc-hero-foto{{min-height:0;aspect-ratio:3/2}}
}}"""
    return sezione(html, css)


def problema():
    html = f"""<div class="enc-due enc-due-foto-sx">
{foto('problem-rail', (800, 1400), 'Unsold garments hanging on a rail', 1400, 1750, '(max-width:900px) 100vw, 50vw', css='enc-due-foto')}
<div class="enc-due-testo enc-in enc-sez">
<h2 class="enc-serif enc-h2">What happens to your unsold cashmere?</h2>
<p class="enc-p">Every season, high-end brands are left with unsold stock, returns and offcuts in premium wool, cashmere and linen. Destroying them is increasingly illegal in Europe. Recyclers exist, but each works differently, with no shared standard and no proof of where fibre ends up. So most of it is lost.</p>
</div>
</div>"""
    return sezione(html, CSS_DUE)


# blocco a due colonne: testo da una parte, foto al vivo dall'altra (usato da problema, soluzione, come funziona, contatti)
CSS_DUE = f"""
.enc-due{{display:grid;grid-template-columns:1fr 1fr;align-items:stretch}}
.enc-due-testo{{display:flex;flex-direction:column;justify-content:center;gap:32px;color:{INK}}}
.enc-due-testo .enc-h2{{max-width:11em}}
.enc-due-foto{{min-height:720px}}
.enc-due-foto-sx .enc-due-testo{{padding-left:96px}}
.enc-due-foto-dx .enc-due-testo{{padding-right:96px}}
@media (max-width:1024px){{.enc-due-foto-sx .enc-due-testo{{padding-left:48px}}.enc-due-foto-dx .enc-due-testo{{padding-right:48px}}}}
@media (max-width:900px){{
  .enc-due{{grid-template-columns:1fr}}
  .enc-due-foto{{min-height:0;aspect-ratio:3/2;order:2}}
  .enc-due-foto-sx .enc-due-testo,.enc-due-foto-dx .enc-due-testo{{padding-left:40px;padding-right:40px}}
}}
@media (max-width:767px){{
  .enc-due-foto-sx .enc-due-testo,.enc-due-foto-dx .enc-due-testo{{padding-left:16px;padding-right:16px}}
  .enc-due-foto{{aspect-ratio:4/5}}
}}"""


def intuizione():
    html = """<div class="enc-intu enc-in">
<p class="enc-serif enc-big">The recycling technology already exists. What's missing is trust between brands and recyclers: one shared standard and one record nobody can alter.</p>
</div>"""
    css = f"""
.enc-intu{{min-height:100vh;min-height:100svh;display:flex;align-items:center;justify-content:center;text-align:center;
  background:{INK};padding-top:160px;padding-bottom:160px}}
.enc-intu p{{color:{IVORY};max-width:22em;margin:0 auto}}
@media (max-width:767px){{.enc-intu{{min-height:0;padding-top:120px;padding-bottom:120px}}}}"""
    return sezione(html, css, scuro=True)


def soluzione():
    html = f"""<div class="enc-due enc-due-foto-dx">
<div class="enc-due-testo enc-in enc-sez">
<h2 class="enc-serif enc-h2">One standard, one loop, every kilo certified.</h2>
<p class="enc-p">You hand over unsold stock, returns and offcuts. Infrared scanners identify each item's fibre and the batch goes to the best certified recycler in our network. Every step is certified on blockchain. Our AI lets you ask, in plain language, where any kilo came from. Buy back the recycled fibre through Encore at a discount.</p>
</div>
{foto('solution-wool', (800, 1400), 'Close-up of cable knit wool', 1400, 1750, '(max-width:900px) 100vw, 50vw', css='enc-due-foto')}
</div>"""
    return sezione(html, CSS_DUE, ancora='loop')


PASSI = [
    ('01', 'Hand over your waste.',
     'Unsold stock, returns and offcuts are collected. Infrared scanners identify each item\'s exact fibre in seconds.'),
    ('02', 'Matched and certified.',
     'Every batch goes to the partner best suited to its fibre. Each scan and handover is certified on blockchain.'),
    ('03', 'Ask, verify, buy back.',
     'Ask our AI anything about your fibre in plain language. Buy it back at a discount, certified.'),
]


def come_funziona():
    passi = ''.join(f"""<li class="enc-passo"><p class="enc-serif enc-passo-n" aria-hidden="true">{n}</p>
<div><h3 class="enc-serif enc-passo-t"><span class="enc-sr">Step {n}: </span>{t}</h3><p class="enc-p">{d}</p></div></li>"""
                    for n, t, d in PASSI)
    html = f"""<div class="enc-due enc-due-foto-sx">
{foto('how-yarn-cones', (800, 1400), 'Cones of recycled yarn by a mill window', 1400, 1750, '(max-width:900px) 100vw, 50vw', css='enc-due-foto')}
<div class="enc-due-testo enc-in enc-sez"><ol class="enc-passi">{passi}</ol></div>
</div>"""
    css = CSS_DUE + f"""
.enc-passi{{list-style:none;margin:0;padding:0;width:100%}}
.enc-passo{{display:grid;grid-template-columns:80px 1fr;gap:24px;padding:40px 0;border-top:1px solid {STONE}}}
.enc-passo:last-child{{border-bottom:1px solid {STONE}}}
.enc-passo-n{{font-size:32px;line-height:1.1;margin:0;color:{STONE_TXT}}}
.enc-passo-t{{font-size:32px;line-height:1.15;margin:0 0 16px;color:{INK}}}
@media (max-width:767px){{.enc-hero-foto{{aspect-ratio:4/5}}}}
@media (max-width:767px){{.enc-passo{{grid-template-columns:56px 1fr;gap:16px;padding:32px 0}}
  .enc-passo-n,.enc-passo-t{{font-size:26px}}}}"""
    return sezione(html, css)


def per_chi():
    html = """<div class="enc-perchi enc-in enc-sez">
<p class="enc-serif enc-big">For high-end fashion brands that, at the end of every season, face unsold stock, returns and premium offcuts they can neither sell nor destroy.</p>
</div>"""
    css = f'.enc-perchi p{{color:{INK};max-width:24em}}.enc-perchi{{border-bottom:1px solid {STONE}}}'
    return sezione(html, css)


PUNTI = [
    'One partner instead of dozens of recyclers to vet',
    'A certificate no one can falsify',
    'Answers in plain language, not spreadsheets',
    'Your products never reach the grey market',
]


def perche():
    punti = ''.join(f'<li class="enc-small">{p}</li>' for p in PUNTI)
    html = f"""<div class="enc-perche enc-in enc-sez">
<p class="enc-serif enc-big">Your unsold stock is frozen capital. Encore turns it into fibre you buy back below market price, protecting your brand and your margin.</p>
<ul class="enc-punti">{punti}</ul>
</div>"""
    css = f"""
.enc-perche{{background:{INK};display:flex;flex-direction:column;gap:96px}}
.enc-perche .enc-big{{color:{IVORY};max-width:22em}}
.enc-punti{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:32px}}
.enc-punti li{{color:{IVORY};font-size:16px;padding-top:24px;border-top:1px solid {STONE};max-width:16em}}
@media (max-width:1024px){{.enc-punti{{grid-template-columns:repeat(2,1fr);gap:40px 32px}}}}
@media (max-width:767px){{.enc-perche{{gap:64px}}.enc-punti{{grid-template-columns:1fr;gap:24px}}}}"""
    return sezione(html, css, ancora='why', scuro=True)


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
    html = f"""<div class="enc-conf enc-in enc-sez">
<h2 class="enc-serif enc-h2" id="enc-conf-t">Others do one step. Encore closes the loop.</h2>
<div class="enc-tab" role="region" aria-labelledby="enc-conf-t" tabindex="0">
<table><thead><tr><th scope="col"><span class="enc-sr">Company</span></th>{testa}</tr></thead><tbody>{righe}</tbody></table>
</div>
<p class="enc-small enc-conf-nota">Based on each company's public offering, October 2026. Re.Verso and Manteco produce certified recycled wool and cashmere; TextileGenesis traces fibre on blockchain; Reverse Resources matches factory leftovers with recyclers; Fibersort builds NIR sorting machines.</p>
</div>"""
    css = f"""
.enc-conf{{display:flex;flex-direction:column;gap:64px;color:{INK};min-width:0}}
.enc-conf>*{{min-width:0}}
.enc-conf .enc-h2{{max-width:12em}}
.enc-tab{{position:relative;overflow-x:auto;-webkit-overflow-scrolling:touch;min-width:0;max-width:100%}}
.enc-tab table{{width:100%;min-width:760px;border-collapse:collapse;font-family:'{SANS}',Arial,sans-serif;color:{INK};
  background:transparent;border:0;margin:0}}
.enc-tab th,.enc-tab td{{border:0;border-bottom:1px solid {STONE};padding:24px 16px;text-align:center;vertical-align:middle;
  background:transparent;font-weight:400}}
.enc-tab thead th{{font-size:12px;line-height:1.5;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;
  vertical-align:bottom;color:{INK};width:16%}}
.enc-tab tbody th{{text-align:left;font-size:18px;white-space:nowrap;padding-left:0}}
.enc-tab thead th:first-child{{width:20%}}
.enc-dot{{display:inline-block;width:10px;height:10px;border-radius:50%;background:{INK}}}
.enc-tab tr.enc-noi th,.enc-tab tr.enc-noi td{{background:{OX};color:{IVORY};border-bottom-color:{OX}}}
.enc-tab tr.enc-noi th{{padding-left:16px;font-family:'{SERIF}',Georgia,serif;font-size:22px;letter-spacing:0.2em}}
.enc-tab tr.enc-noi .enc-dot{{background:{IVORY}}}
.enc-conf-nota{{color:{STONE_TXT};max-width:52em}}
@media (max-width:767px){{.enc-conf{{gap:40px}}}}"""
    return sezione(html, css, ancora='compare')


def primo_ciclo():
    html = """<div class="enc-mvp enc-in enc-sez">
<h2 class="enc-serif enc-h2">The first loop</h2>
<p class="enc-p">One brand, one recycler, one batch of unsold wool knitwear. A handheld infrared scanner identifies every item, each step is certified on a blockchain, an AI assistant answers questions on the data, and the brand buys back the yarn discounted.</p>
</div>"""
    css = f"""
.enc-mvp{{display:grid;grid-template-columns:5fr 7fr;gap:64px;align-items:start;color:{INK};border-top:1px solid {STONE}}}
.enc-mvp .enc-p{{font-size:20px;max-width:30em}}
@media (max-width:900px){{.enc-mvp{{grid-template-columns:1fr;gap:32px}}.enc-mvp .enc-p{{font-size:18px}}}}"""
    return sezione(html, css, ancora='pilot')


def risultato():
    srcset = ', '.join(f'{img(f"result-knit-{x}.webp")} {x}w' for x in (900, 1600, 2400))
    html = f"""<div class="enc-ris">
<img class="enc-ris-img" src="{img('result-knit-1600.webp')}" srcset="{srcset}" sizes="100vw" width="1600" height="900"
 alt="A model wearing a neutral wool knit sweater" loading="lazy" decoding="async">
<div class="enc-ris-velo"></div>
<div class="enc-ris-testo enc-in"><p class="enc-serif enc-big">Your end-of-season stock stops being a cost and a risk, and becomes cheaper fibre for your next collection.</p></div>
</div>"""
    css = f"""
.enc-ris{{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:flex-end;overflow:hidden;background:{INK}}}
.enc-ris-img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:30% 30%}}
.enc-ris-velo{{position:absolute;inset:0;background:rgba(21,20,18,0.62)}}
.enc-ris-testo{{position:relative;padding-top:160px;padding-bottom:120px}}
.enc-ris-testo p{{color:{IVORY};max-width:20em}}
@media (max-width:767px){{.enc-ris{{min-height:640px}}.enc-ris-testo{{padding-bottom:64px}}}}"""
    return sezione(html, css, scuro=True)


def contatti():
    campo = ('<label class="enc-campo"><span class="enc-label">{l}</span>'
             '<input class="enc-input enc-input" name="{n}" type="{t}" autocomplete="{a}" required></label>')
    campi = ''.join(campo.format(l=l, n=n, t=t, a=a) for l, n, t, a in (
        ('Name', 'name', 'text', 'name'), ('Brand', 'brand', 'text', 'organization'), ('Email', 'email', 'email', 'email')))
    html = f"""<div class="enc-due enc-due-foto-sx">
{foto('cta-wool-macro', (800, 1400), 'Macro photograph of woven wool', 1400, 1750, '(max-width:900px) 100vw, 50vw', css='enc-due-foto')}
<div class="enc-due-testo enc-in enc-sez">
<h2 class="enc-serif enc-h2">Start your first loop.</h2>
<form class="enc-form" id="enc-form" novalidate>
{campi}
<label class="enc-campo"><span class="enc-label">Message</span><textarea class="enc-input enc-input" name="message" rows="4"></textarea></label>
<div><button class="enc-btn enc-btn" type="submit">Book a pilot</button></div>
</form>
<p class="enc-serif enc-grazie" id="enc-grazie" tabindex="-1" hidden>Thank you.</p>
</div>
</div>
<script>(function(){{var f=document.getElementById('enc-form'),g=document.getElementById('enc-grazie');if(!f)return;
f.addEventListener('submit',function(e){{e.preventDefault();if(!f.checkValidity()){{f.reportValidity();return;}}
f.hidden=true;g.hidden=false;g.focus();}});}})();</script>"""
    css = CSS_DUE + f"""
.enc-form{{display:flex;flex-direction:column;gap:24px;width:100%;max-width:520px}}
.enc-campo{{display:flex;flex-direction:column;gap:8px;color:{INK}}}
.enc-input.enc-input{{font-family:'{SANS}',Arial,sans-serif;font-size:17px;line-height:1.5;color:{INK};background:transparent;
  border:0;border-bottom:1px solid {STONE};border-radius:0;padding:8px 0;width:100%;box-shadow:none;outline-offset:4px}}
.enc-input.enc-input:focus{{border-bottom-color:{INK}}}
textarea.enc-input.enc-input{{resize:vertical;min-height:96px}}
.enc-form .enc-btn{{margin-top:16px}}
.enc-grazie{{font-size:40px;line-height:1.1;color:{INK};margin:0}}
.enc-form[hidden],.enc-grazie[hidden]{{display:none}}"""
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
