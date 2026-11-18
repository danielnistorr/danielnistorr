#!/usr/bin/env python3
"""Genera il sito Dieffepiu da una sola fonte.

Uscite:
  anteprima/                    sito statico multipagina (doppio clic su anteprima/index.html)
  wordpress/dieffepiu/          tema WordPress con le pagine pronte e l'installatore
  wordpress/dieffepiu-tema.zip  lo stesso tema, da caricare in Aspetto > Temi > Aggiungi > Carica tema

La home e' quella di sito/index.html, non ridisegnata: se ne prendono il CSS e il <main>, cambiano solo
i link (ora vanno alle pagine) e sparisce il selettore delle lingue (le pagine EN e DE non ci sono ancora).

Uso: python3 _sorgente/build.py            (rifa' immagini se mancano, anteprima, tema e zip)
     python3 _sorgente/build.py --immagini (rifa' anche tutte le immagini)
"""
import json
import pathlib
import re
import shutil
import sys
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import immagini  # noqa: E402

if "--immagini" in sys.argv or not (pathlib.Path(__file__).resolve().parent / "immagini.json").exists():
    immagini.prepara(tutte="--immagini" in sys.argv)

import comune  # noqa: E402
import pagine  # noqa: E402
from comune import Ctx, RADICE, SORGENTE  # noqa: E402

HOME = RADICE / "sito" / "index.html"
ANTE = RADICE / "anteprima"
WPDIR = RADICE / "wordpress"
TEMA = WPDIR / "dieffepiu"
IMG_WEB = SORGENTE / "img-web"        # immagini pronte (WebP), generate da immagini.py

VIETATO = "—"


def css_completo():
    s = HOME.read_text(encoding="utf-8")
    css = s[s.index("<style>") + 7:s.index("</style>")]
    # il CSS sta in assets/sito.css, i caratteri in assets/fonts/: i percorsi url(fonts/...) restano validi
    tutto = css.strip() + "\n" + (SORGENTE / "interne.css").read_text(encoding="utf-8")
    return tutto + css_elementor(tutto)


def css_elementor(css):
    """Nelle pagine fatte con Elementor il suo foglio di stile toglie le sottolineature (.elementor a) e i margini
    delle figure (.elementor .elementor-widget:not(...) figure). Qui le regole del sito che li toccano vengono
    ripetute con un prefisso piu' forte, nello stesso ordine: la pagina torna uguale a quella senza Elementor."""
    senza_commenti = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    righe = [".elementor .dfp-sez a{text-decoration-line:underline}"]
    media = None
    for m in re.finditer(r"(@media[^{]+)\{|([^{}]+)\{([^{}]*)\}|\}", senza_commenti):
        if m.group(1):
            media = m.group(1).strip()
            continue
        if m.group(2) is not None:
            if "text-decoration" in m.group(3) and not media:
                # solo le dichiarazioni della sottolineatura: il resto della regola resta com'era (e responsive)
                dich = [d.strip() for d in m.group(3).split(";") if d.strip().startswith(("text-decoration", "text-underline"))]
                sel = ",".join(".elementor .dfp-sez " + x.strip() for x in m.group(2).split(","))
                righe.append(sel + "{" + ";".join(dich) + "}")
            continue
        media = None
    P = ".elementor .dfp-sez .elementor-widget:not(.elementor-widget-text-editor):not(.elementor-widget-theme-post-content)"
    righe += [P + " figure.foto-piena{margin:64px 0 0}",
              "@media (max-width:960px){" + P + " .pezzo figure{margin-top:52px}" + P + " .apri-pagina figure.tavola-p{margin-top:40px}}",
              "@media (max-width:600px){" + P + " figure.foto-piena{margin-top:40px}}"]
    return "\n/* Elementor: le regole del sito che il suo foglio di stile annullerebbe */\n" + "\n".join(righe) + "\n"


def main_home(c):
    s = HOME.read_text(encoding="utf-8")
    m = s[s.index('<main id="top">'):s.index("</main>") + 7]
    m = re.sub(r'(?<=["\s,])img/', lambda x: c.img(""), m)
    # link alle pagine nuove, dentro le sezioni della home (niente altro cambia)
    m = m.replace(
        '        </div>\n      </div>\n    </div>\n    <figure class="foto-piena">',
        '        </div>\n      </div>\n      <p class="vai"><a href="' + c.link("sistemi") + '">Le sei famiglie di sistemi</a></p>\n'
        '    </div>\n    <figure class="foto-piena">', 1)
    m = m.replace(
        '          <p class="macchina-nota" id="m-nota">Rumorosità inferiore a 70&nbsp;dB(A).</p>\n        </div>\n      </div>',
        '          <p class="macchina-nota" id="m-nota">Rumorosità inferiore a 70&nbsp;dB(A).</p>\n        </div>\n      </div>\n'
        '      <p class="vai"><a href="' + c.link("macchine") + '">Tutte le macchine, con le schede</a></p>', 1)
    m = m.replace(
        'l’ultima a Parigi tra settembre e ottobre 2026.</p>',
        'l’ultima a Parigi tra settembre e ottobre 2026. <a href="' + c.link("news") + '">Fiere e novità</a></p>', 1)
    assert m.count('class="vai"') == 2, "i punti di aggancio della home sono cambiati"
    return m


def documento(c, p, corpo):
    titolo = p["titolo_seo"]
    desc = p["descrizione"]
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{comune.e(titolo)}</title>
<meta name="description" content="{comune.e(desc)}">
<link rel="icon" type="image/png" href="{c.img('icona-180.png')}">
<link rel="preload" href="{c.asset('fonts/pathway-latin.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{c.asset('sito.css')}">
</head>
<body>

{comune.testata(c)}

{corpo}

{piede_con_macchine(c)}

<script src="{c.asset('sito.js')}"></script>
</body>
</html>
'''


def piede_con_macchine(c):
    voci = "\n".join(f'            <li><a href="{c.link("macchine", "#" + a)}">{n}</a></li>' for a, n in pagine.macchine_piede())
    return comune.piede(c).replace("<!--macchine-piede-->", voci)


def corpo_pagina(c, p):
    if p["chiave"] == "home":
        return [main_home(c)]
    return p["fai"](c)


def avvolgi_main(c, p, sezioni):
    if p["chiave"] == "home":
        return sezioni[0]
    return '<main id="top" class="interna">\n' + "\n\n".join(sezioni) + "\n</main>"


def copia_asset(dest):
    (dest / "img").mkdir(parents=True, exist_ok=True)
    (dest / "fonts").mkdir(parents=True, exist_ok=True)
    for f in (RADICE / "sito" / "img").iterdir():
        shutil.copy2(f, dest / "img" / f.name)
    for f in IMG_WEB.iterdir():
        shutil.copy2(f, dest / "img" / f.name)
    for f in (RADICE / "sito" / "fonts").iterdir():
        shutil.copy2(f, dest / "fonts" / f.name)
    (dest / "sito.css").write_text(css_completo(), encoding="utf-8")
    (dest / "sito.js").write_text((SORGENTE / "sito.js").read_text(encoding="utf-8"), encoding="utf-8")


def controlla(testo, dove):
    if VIETATO in testo:
        raise SystemExit(f"carattere vietato U+2014 in {dove}")


def anteprima():
    if ANTE.exists():
        shutil.rmtree(ANTE)
    copia_asset(ANTE / "assets")
    for p in pagine.PAGINE + pagine.articoli():
        c = Ctx("html", p["percorso"])
        sez = corpo_pagina(c, p)
        doc = documento(c, p, avvolgi_main(c, p, sez))
        controlla(doc, p["percorso"])
        out = ANTE / p["percorso"] / "index.html" if p["percorso"] else ANTE / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(doc, encoding="utf-8")
    # 404 statica
    p = pagine.P404
    c = Ctx("html", "")
    (ANTE / "404.html").write_text(documento(c, p, avvolgi_main(c, p, p["fai"](c))), encoding="utf-8")


def blocchi(sezioni):
    return "\n\n".join(f"<!-- wp:html -->\n{s}\n<!-- /wp:html -->" for s in sezioni)


def tema():
    if TEMA.exists():
        shutil.rmtree(TEMA)
    shutil.copytree(SORGENTE / "tema", TEMA)
    copia_asset(TEMA / "assets")
    (TEMA / "contenuti").mkdir(exist_ok=True)
    (TEMA / "parti").mkdir(exist_ok=True)
    c0 = Ctx("wp", "")
    (TEMA / "parti" / "testata.html").write_text(comune.testata(c0), encoding="utf-8")
    (TEMA / "parti" / "piede.html").write_text(piede_con_macchine(c0), encoding="utf-8")
    elenco = []
    for p in pagine.PAGINE:
        c = Ctx("wp", p["percorso"])
        sez = corpo_pagina(c, p)
        if p["chiave"] == "home":
            # la home e' un <main> unico: in WordPress ogni <section> diventa un blocco HTML a se'
            interno = sez[0][len('<main id="top">'):-len("</main>")]
            sez = [s.strip() for s in re.split(r"\n(?=  <section )", interno) if s.strip()]
        testo = blocchi(sez)
        controlla(testo, p["percorso"])
        nome = (p["chiave"]) + ".html"
        (TEMA / "contenuti" / nome).write_text(testo, encoding="utf-8")
        elenco.append({k: p[k] for k in ("chiave", "slug", "genitore", "titolo", "titolo_seo", "descrizione", "ordine")} | {"file": nome})
    (TEMA / "contenuti" / "pagine.json").write_text(json.dumps(elenco, ensure_ascii=False, indent=1), encoding="utf-8")
    # parti per le notizie (archivio e articolo), scritte una volta sola qui
    c = Ctx("wp", "news")
    (TEMA / "parti" / "news-testa.html").write_text(pagine.news_testa(c), encoding="utf-8")
    (TEMA / "parti" / "richiesta.html").write_text(comune.richiesta(c), encoding="utf-8")
    import moduli
    for tipo in ("contatti", "accesso"):
        (TEMA / "parti" / f"modulo-{tipo}.html").write_text(moduli.html(tipo, anteprima=False), encoding="utf-8")
    p = pagine.P404
    (TEMA / "parti" / "404.html").write_text("\n\n".join(p["fai"](Ctx("wp", ""))), encoding="utf-8")
    arts = [{"titolo": a["titolo"], "slug": a["slug"], "data": a["data"], "testo": a["testo_wp"], "estratto": a["estratto"]}
            for a in pagine.articoli()]
    (TEMA / "contenuti" / "articoli.json").write_text(json.dumps(arts, ensure_ascii=False, indent=1), encoding="utf-8")
    for f in TEMA.rglob("*"):
        if f.is_file() and f.suffix in (".php", ".html", ".json", ".css", ".js", ".txt"):
            controlla(f.read_text(encoding="utf-8"), str(f))
    # zip
    z = WPDIR / "dieffepiu-tema.zip"
    if z.exists():
        z.unlink()
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zz:
        for f in sorted(TEMA.rglob("*")):
            if f.is_file():
                zz.write(f, "dieffepiu/" + str(f.relative_to(TEMA)))
    print("zip", z, z.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    anteprima()
    tema()
    print("ok")
