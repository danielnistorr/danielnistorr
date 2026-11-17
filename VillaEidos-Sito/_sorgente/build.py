#!/usr/bin/env python3
"""Costruisce il sito di Villa Eidos: il tema WordPress, il suo zip e l'anteprima statica.

Uso:  python3 -I VillaEidos-Sito/_sorgente/build.py

Uscite:
  wordpress/villaeidos/          il tema scompattato (da caricare via FTP in wp-content/themes/)
  wordpress/villaeidos-tema.zip  lo stesso tema, da caricare in Aspetto > Temi > Aggiungi tema > Carica tema
  anteprima/                     il sito statico: index.html, privacy.html, cookie.html e assets/

Fonti:
  _sorgente/tema/        PHP, fogli di stile, script, caratteri e parti in HTML del tema (scritti a mano)
  _sorgente/pagine.py    le pagine come contenitori e widget di Elementor, con i testi del cliente
  assets/web/            foto e logo gia' pronti (immagini.py e logo/ li rifanno dagli originali)

L'anteprima usa gli stessi dati di Elementor e lo stesso foglio di stile del tema: i contenitori e i widget sono
scritti con l'HTML che Elementor 4 produce, le parti (testata, piede, modulo) sono gli stessi file del tema.

Controlli: nessun carattere U+2014, ogni testo della Home nel testo del cliente (pagine.FONTE) o tra gli adattati
con la loro fonte (pagine.ADATTATI), nessuna credenziale.
"""
import datetime
import html
import json
import pathlib
import re
import shutil
import sys
import zipfile

SORGENTE = pathlib.Path(__file__).resolve().parent
RADICE = SORGENTE.parent
REPO = RADICE.parent
TEMA_SORG = SORGENTE / "tema"
WEB = RADICE / "assets" / "web"
WPDIR = RADICE / "wordpress"
TEMA = WPDIR / "villaeidos"
ZIP = WPDIR / "villaeidos-tema.zip"
ANTE = RADICE / "anteprima"

sys.path.insert(0, str(SORGENTE))
import pagine  # noqa: E402

VIETATO = chr(0x2014)  # la lineetta lunga, vietata in tutti i file

IMMAGINI = [
    {"chiave": "apertura-conferenze", "titolo": "Apertura: la sala conferenze (da sostituire con la foto della villa)",
     "file": "apertura-conferenze-384.webp", "varianti": [],
     "alt": "La sala conferenze nella barchessa: la colonna, il lampadario e le finestre ad arco",
     "sizes": "(min-width: 900px) 480px, min(91vw, 480px)"},
    {"chiave": "sala-conferenze", "titolo": "Sala conferenze", "file": "sala-conferenze-440.webp", "varianti": [],
     "alt": "La sala conferenze: le colonne, il lampadario e le file di sedie",
     "sizes": "(min-width: 900px) 550px, min(91vw, 550px)"},
    {"chiave": "sale-riunioni", "titolo": "Sale riunioni", "file": "sale-riunioni-1080.webp",
     "varianti": ["sale-riunioni-760.webp", "sale-riunioni-540.webp"],
     "alt": "Una sala riunioni: il tavolo di vetro, le sedie e lo schermo, oltre la parete di vetro",
     "sizes": "(min-width: 900px) 30vw, (min-width: 600px) 45vw, 91vw"},
    {"chiave": "uffici", "titolo": "Uffici", "file": "uffici-480.webp", "varianti": ["uffici-360.webp"],
     "alt": "Un ufficio: la scrivania, gli schermi e la finestra", "sizes": "(min-width: 900px) 30vw, (min-width: 600px) 45vw, 91vw"},
    {"chiave": "reception", "titolo": "Reception", "file": "reception-640.webp", "varianti": ["reception-480.webp"],
     "alt": "La reception, con il bancone di legno chiaro", "sizes": "(min-width: 900px) 30vw, (min-width: 600px) 45vw, 91vw"},
]

DESCRIZIONE = ("Una villa storica e un'ampia barchessa ad Albignasego, alle porte di Padova: uffici e sedi di "
               "rappresentanza, sale riunioni di diverse dimensioni e una grande sala conferenze.")
PAGINE = [
    {"chiave": "home", "slug": "home", "titolo": "Home", "ordine": 0, "noindex": False, "file": "home.json", "statica": "index.html",
     "titolo_seo": "Villa Eidos | Uffici, sale riunioni e sala conferenze ad Albignasego, Padova", "descrizione": DESCRIZIONE},
    {"chiave": "privacy", "slug": "privacy", "titolo": "Informativa privacy", "ordine": 1, "noindex": True, "file": "privacy.json",
     "statica": "privacy.html", "titolo_seo": "Informativa privacy | Villa Eidos", "descrizione": ""},
    {"chiave": "cookie", "slug": "cookie", "titolo": "Cookie", "ordine": 2, "noindex": True, "file": "cookie.json",
     "statica": "cookie.html", "titolo_seo": "Cookie | Villa Eidos", "descrizione": ""},
]


# ------------------------------------------------------------------ controlli

def norm(t):
    t = pagine.senza_tag(t).lower().replace("’", "'")
    return re.sub(r"\s+", " ", t).strip()


def controlla_testi_home(el):
    fonte = norm(pagine.FONTE)
    adattati = {norm(k) for k in pagine.ADATTATI}
    noti = {norm(x) for x in [pagine.TEL, pagine.EMAIL, pagine.COMUNE] + pagine.INGRESSI}
    mancanti = []
    for nodo in el:
        for t in pagine.testo_visibile(nodo):
            for f in pagine.frasi(t):
                n = norm(f)
                if n in fonte or n in adattati or n in noti:
                    continue
                mancanti.append(f)
    if mancanti:
        raise SystemExit("testi della Home che non vengono dal testo del cliente:\n  " + "\n  ".join(mancanti))


def controlla_file(cartella):
    sospetti = re.compile(r"(password|passwd|secret|api[_-]?key|token)\s*[=:]\s*['\"][^'\"]{6,}", re.I)
    for f in cartella.rglob("*"):
        if f.is_file() and f.suffix in (".php", ".html", ".json", ".css", ".js", ".txt", ".md", ".svg", ".sh"):
            t = f.read_text(encoding="utf-8")
            if VIETATO in t:
                raise SystemExit(f"carattere vietato U+2014 in {f.relative_to(RADICE)}")
            if sospetti.search(t) and "vendor" not in f.parts:
                raise SystemExit(f"possibile credenziale in {f.relative_to(RADICE)}")


# ------------------------------------------------------------------ tema

def copia_risorse(dest):
    """Foto e logo nella cartella assets/ di dest."""
    a = dest / "assets"
    (a / "img").mkdir(parents=True, exist_ok=True)
    for im in IMMAGINI:
        for f in [im["file"]] + im["varianti"]:
            src = WEB / "foto" / f
            if not src.exists():
                raise SystemExit(f"foto mancante: {src.relative_to(RADICE)} (lancia immagini.py)")
            shutil.copy2(src, a / "img" / f)
    (a / "logo").mkdir(exist_ok=True)
    for f in sorted((WEB / "logo").glob("*.svg")):
        shutil.copy2(f, a / "logo" / f.name)


def contenuti():
    c = TEMA / "contenuti"
    c.mkdir(exist_ok=True)
    dati = {"home": pagine.home(), "privacy": pagine.legale("privacy"), "cookie": pagine.legale("cookie")}
    controlla_testi_home(dati["home"])
    for p in PAGINE:
        (c / p["file"]).write_text(json.dumps(dati[p["chiave"]], ensure_ascii=False, indent=1), encoding="utf-8")
    (c / "pagine.json").write_text(json.dumps(PAGINE, ensure_ascii=False, indent=1), encoding="utf-8")
    (c / "media.json").write_text(json.dumps({"immagini": IMMAGINI}, ensure_ascii=False, indent=1), encoding="utf-8")
    return dati


def zippa():
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(TEMA.rglob("*")):
            if f.is_file():
                z.write(f, "villaeidos/" + str(f.relative_to(TEMA)))
    return ZIP.stat().st_size


# ------------------------------------------------------------------ anteprima: l'HTML che Elementor 4 scrive

CONFIG = {"telefono": pagine.TEL, "telefono_link": pagine.TEL_LINK, "email": pagine.EMAIL, "comune": pagine.COMUNE,
          "indirizzi": ", ".join(pagine.INGRESSI), "mappa": pagine.MAPPA}
TIPI = ["Ufficio o sede", "Sala riunioni", "Sala conferenze"]  # come config/richiesta.php


def leggi_parte(nome):
    h = (TEMA_SORG / "parti" / f"{nome}.html").read_text(encoding="utf-8")
    return re.sub(r"^\s*<!--.*?-->\s*", "", h, flags=re.S)


def segnaposti_parti(home):
    e = html.escape
    return {
        "{{home}}": home, "{{logo}}": "assets/logo/villaeidos-orizzontale.svg",
        "{{logo_intero}}": "assets/logo/villaeidos-logo.svg",
        "{{tel}}": e(CONFIG["telefono"]), "{{tel_link}}": e(CONFIG["telefono_link"]), "{{email}}": e(CONFIG["email"]),
        "{{comune}}": e(CONFIG["comune"]), "{{indirizzi}}": "<br>".join(e(x.strip()) for x in CONFIG["indirizzi"].split(",")),
        "{{mappa}}": e(CONFIG["mappa"]), "{{privacy}}": "privacy.html", "{{cookie}}": "cookie.html",
        "{{anno}}": str(datetime.date.today().year),
        "{{legale}}": '<span class="da-completare">Ragione sociale e partita IVA da completare</span>',
    }


def parte(nome, home, altri=None):
    h = leggi_parte(nome)
    for k, v in {**segnaposti_parti(home), **(altri or {})}.items():
        h = h.replace(k, v)
    return h


MEDIA = {im["chiave"]: im for im in IMMAGINI}


def dimensioni(f):
    from PIL import Image
    with Image.open(TEMA / "assets" / "img" / f) as im:
        return im.size


def srcset(im):
    out = []
    for f in [im["file"]] + im["varianti"]:
        out.append(f"assets/img/{f} {dimensioni(f)[0]}w")
    return ", ".join(out)


def tag_img(chiave, apertura=False):
    im = MEDIA[chiave]
    w, h = dimensioni(im["file"])
    caricamento = 'loading="eager" fetchpriority="high"' if apertura else 'loading="lazy"'
    img = (f'<img {caricamento} decoding="async" width="{w}" height="{h}" src="assets/img/{im["file"]}" '
           f'class="attachment-full size-full" alt="{html.escape(im["alt"])}" srcset="{srcset(im)}" sizes="{im["sizes"]}" />')
    if apertura and im.get("tel"):
        t = MEDIA[im["tel"]]
        img = f'<picture><source media="(max-width: 760px)" srcset="{srcset(t)}" sizes="{t["sizes"]}">{img}</picture>'
    return img


def risolvi(t):
    return t.replace("{{pagina:privacy}}", "privacy.html").replace("{{pagina:cookie}}", "cookie.html").replace("{{casa}}", "index.html")


def rendi(el, home):
    """Un elemento di Elementor nell'HTML che Elementor 4 produce (markup ottimizzato, senza widget-container)."""
    s = el["settings"]
    if el["elType"] == "container":
        tag = s.get("html_tag", "div")
        classi = " ".join(x for x in ["elementor-element", f"elementor-element-{el['id']}", "e-con-full", s.get("css_classes", ""),
                                      "e-flex", "e-con", "e-child" if el["isInner"] else "e-parent"] if x)
        ancora = f' id="{s["_element_id"]}"' if s.get("_element_id") else ""
        figli = "\n".join(rendi(f, home) for f in el["elements"])
        return (f'<{tag} class="{classi}" data-id="{el["id"]}" data-element_type="container" data-e-type="container"{ancora}>\n'
                f"{figli}\n</{tag}>")
    tipo = el["widgetType"]
    classi = " ".join(x for x in ["elementor-element", f"elementor-element-{el['id']}", s.get("_css_classes", ""),
                                  "elementor-widget", f"elementor-widget-{tipo}"] if x)
    if tipo == "heading":
        t = s["title"]
        if s.get("link", {}).get("url"):
            t = f'<a href="{html.escape(s["link"]["url"])}">{t}</a>'
        corpo = f'<{s["header_size"]} class="elementor-heading-title elementor-size-default">{t}</{s["header_size"]}>'
    elif tipo == "text-editor":
        corpo = risolvi(s["editor"])
    elif tipo == "image":
        corpo = tag_img(s["image"]["ve_img"], "apertura-foto" in s.get("_css_classes", ""))
    elif tipo == "button":
        l = s["link"]
        est = ' target="_blank"' if l.get("is_external") else ""
        for riga in (l.get("custom_attributes") or "").split("\n"):
            if "|" in riga:
                k, v = riga.split("|", 1)
                est += f' {k.strip()}="{html.escape(v.strip())}"'

        corpo = (f'<a class="elementor-button elementor-button-link elementor-size-sm" href="{html.escape(l["url"])}"{est}>\n'
                 f'<span class="elementor-button-content-wrapper">\n<span class="elementor-button-text">{s["text"]}</span>\n</span>\n</a>')
    elif tipo == "shortcode":
        assert s["shortcode"] == "[villaeidos_richiesta]", s["shortcode"]
        tipi = "".join(f'<label><input type="radio" name="tipo" value="{html.escape(t)}"{" required" if i == 0 else ""}><span>{html.escape(t)}</span></label>'
                       for i, t in enumerate(TIPI))
        corpo = '<div class="elementor-shortcode">' + parte("richiesta", home, {"{{tipi}}": tipi}) + "</div>"
    else:
        raise SystemExit(f"widget non previsto: {tipo}")
    return (f'<div class="{classi}" data-id="{el["id"]}" data-element_type="widget" data-e-type="widget" '
            f'data-widget_type="{tipo}.default">\n{corpo}\n</div>')


def pagina_statica(p, elementi, n):
    home = "" if p["chiave"] == "home" else "index.html"
    legale = p["noindex"]
    moto = p["chiave"] == "home"
    testa = [
        '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<title>{html.escape(p["titolo_seo"])}</title>',
    ]
    if p["descrizione"]:
        testa.append(f'<meta name="description" content="{html.escape(p["descrizione"])}">')
    if legale:
        testa.append('<meta name="robots" content="noindex">')
    testa += ['<link rel="preload" href="assets/fonts/fustat-latin.woff2" as="font" type="font/woff2" crossorigin>',
              '<link rel="icon" href="assets/logo/villaeidos-marchio.svg" type="image/svg+xml">',
              '<link rel="stylesheet" href="assets/sito.css">']
    corpo = "\n".join(rendi(e, home) for e in elementi)
    script = ['<script src="assets/sito.js"></script>']
    if "villaeidos_richiesta" in json.dumps(elementi):
        script += ['<script>var VILLAEIDOS_RICHIESTA = {"oggetto":"Richiesta di disponibilità"};</script>',
                   '<script src="assets/richiesta.js"></script>']
    classe = "ve ve-legale" if legale else ("ve ve-moto" if moto else "ve")
    return ("<!doctype html>\n<html lang=\"it\">\n<head>\n" + "\n".join(testa) + "\n</head>\n"
            f'<body class="{classe}">\n' + parte("testata", home) + '\n<main id="contenuto">\n'
            f'<div data-elementor-type="wp-page" data-elementor-id="{n}" class="elementor elementor-{n}">\n{corpo}\n</div>\n'
            "</main>\n" + parte("piede", home) + "\n" + "\n".join(script) + "\n</body>\n</html>\n")


def anteprima(dati):
    if ANTE.exists():
        shutil.rmtree(ANTE)
    a = ANTE / "assets"
    a.mkdir(parents=True)
    for f in ("sito.css", "sito.js", "richiesta.js"):
        shutil.copy2(TEMA_SORG / "assets" / f, a / f)
    shutil.copytree(TEMA_SORG / "assets" / "fonts", a / "fonts")
    for sotto in ("img", "logo"):
        shutil.copytree(TEMA / "assets" / sotto, a / sotto)
    for n, p in enumerate(PAGINE, 1):
        (ANTE / p["statica"]).write_text(pagina_statica(p, dati[p["chiave"]], n), encoding="utf-8")


def main():
    sys.path.insert(0, str(SORGENTE))
    import immagini
    if immagini.mancano():
        immagini.prepara()
    if TEMA.exists():
        shutil.rmtree(TEMA)
    WPDIR.mkdir(exist_ok=True)
    shutil.copytree(TEMA_SORG, TEMA, ignore=shutil.ignore_patterns("__pycache__"))
    if (SORGENTE / "screenshot.jpg").exists():
        shutil.copy2(SORGENTE / "screenshot.jpg", TEMA / "screenshot.jpg")
    copia_risorse(TEMA)
    dati = contenuti()
    anteprima(dati)
    for c in (TEMA, ANTE, SORGENTE):
        controlla_file(c)
    for f in list(RADICE.glob("*.md")) + list(WPDIR.glob("*.md")) + list(WPDIR.glob("*.sh")):
        if VIETATO in f.read_text(encoding="utf-8"):
            raise SystemExit(f"carattere vietato U+2014 in {f.relative_to(RADICE)}")
    peso = zippa()
    print(f"tema: {TEMA.relative_to(REPO)}  zip: {ZIP.relative_to(REPO)} ({peso // 1024} KB)")
    print(f"anteprima: {ANTE.relative_to(REPO)}/index.html")


if __name__ == "__main__":
    main()
