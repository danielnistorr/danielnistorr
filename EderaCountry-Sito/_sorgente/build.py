#!/usr/bin/env python3
"""Genera il tema WordPress di Edera Country House e il suo zip.

Uso:  python3 EderaCountry-Sito/_sorgente/build.py

Uscite:
  wordpress/edera/            il tema scompattato (da caricare via FTP in wp-content/themes/)
  wordpress/edera-tema.zip    lo stesso tema, da caricare in Aspetto > Temi > Aggiungi > Carica tema

Fonti:
  _sorgente/tema/             PHP, fogli di stile e script del tema (scritti a mano)
  _sorgente/pagine.py         le pagine come contenitori e widget di Elementor
  originale/                  il sito pubblicato, scaricato: foto, caratteri, PDF, testi delle pagine legali
  _metodo/highend/kit/        il kit dei movimenti (he.js, he.css, GSAP, ScrollTrigger, SplitText)
  assets/web/planimetria/     foto della planimetria gia' compresse (immagini.py le rifa' dagli originali)

Controlli: nessun carattere U+2014, ogni testo della Home presente nell'originale, nessuna credenziale.
"""
import json
import pathlib
import re
import shutil
import sys
import zipfile

SORGENTE = pathlib.Path(__file__).resolve().parent
RADICE = SORGENTE.parent
REPO = RADICE.parent
ORIG = RADICE / "originale"
KIT = REPO / "_metodo" / "highend" / "kit"
WPDIR = RADICE / "wordpress"
TEMA = WPDIR / "edera"
ZIP = WPDIR / "edera-tema.zip"

sys.path.insert(0, str(SORGENTE))
import immagini  # noqa: E402
import pagine  # noqa: E402

VIETATO = chr(0x2014)  # la lineetta lunga, vietata in tutti i file

# Foto: il file piu' grande e le sue misure gia' pronte, il testo alternativo e "sizes" dell'originale.
IMMAGINI = [
    {"chiave": "apertura", "titolo": "Apertura", "file": "apertura-1500.webp", "varianti": ["apertura-1100.webp", "apertura-760.webp"],
     "alt": "Edera Country House: il grande ulivo, la piscina e il giardino apparecchiato per un evento", "sizes": "100vw",
     "tel": "apertura-tel"},
    {"chiave": "apertura-tel", "titolo": "Apertura, versione per il telefono", "file": "apertura-tel-750.webp", "varianti": ["apertura-tel-520.webp"],
     "alt": "Edera Country House: il grande ulivo, la piscina e il giardino apparecchiato per un evento", "sizes": "100vw"},
    {"chiave": "casa", "titolo": "Il giardino la sera", "file": "casa-1250.webp", "varianti": ["casa-900.webp", "casa-620.webp"],
     "alt": "Allestimento esterno la sera, sotto gli ulivi illuminati, accanto alla piscina", "sizes": "(max-width: 900px) 92vw, 560px"},
    {"chiave": "meeting", "titolo": "Meeting e convention", "file": "meeting-573.webp", "varianti": [],
     "alt": "Pubblico durante un meeting e convention", "sizes": ""},
    {"chiave": "celebrazioni", "titolo": "Celebrazioni", "file": "celebrazioni-900.webp", "varianti": ["celebrazioni-620.webp"],
     "alt": "Fuochi d'artificio durante una celebrazione serale", "sizes": "(max-width: 900px) 92vw, 380px"},
    {"chiave": "teambuilding", "titolo": "Team building", "file": "teambuilding-900.webp", "varianti": ["teambuilding-620.webp"],
     "alt": "Ospiti in giardino al tramonto, con le lanterne accese sotto gli ulivi", "sizes": "(max-width: 900px) 92vw, 380px"},
    {"chiave": "piscina-sera", "titolo": "La piscina la sera", "file": "piscina-sera-1093.webp", "varianti": ["piscina-sera-760.webp"],
     "alt": "La piscina illuminata durante un ricevimento serale", "sizes": "(max-width: 900px) 92vw, 590px"},
    {"chiave": "sala", "titolo": "La sala", "file": "sala-1500.webp", "varianti": ["sala-1100.webp", "sala-760.webp"],
     "alt": "La sala interna con le travi in legno a vista", "sizes": "(max-width: 900px) 92vw, 490px"},
    {"chiave": "giardino", "titolo": "Il giardino apparecchiato", "file": "giardino-800.webp", "varianti": ["giardino-560.webp"],
     "alt": "Tavoli apparecchiati nel giardino per un ricevimento all'aperto", "sizes": "(max-width: 900px) 70vw, 290px"},
]
# Planimetria (tema 1.1): foto dall'alto e foto del Rustico, gia' compresse in assets/web/planimetria/
# (da _sorgente/immagini.py). Il gruppo serve al bottone "Aggiungi la planimetria alla Home".
DIDASCALIE_RUSTICO = ["Esterno della struttura", "Sala interna", "Sala interna – seconda vista",
                      "Vista dal soppalco", "Panoramica piscina e struttura"]
IMMAGINI += [
    {"chiave": "planimetria", "gruppo": "planimetria", "titolo": "Planimetria vista dall'alto",
     "file": "planimetria-981.webp", "varianti": ["planimetria-760.webp", "planimetria-560.webp", "planimetria-400.webp"],
     "alt": "Planimetria di Edera Country House vista dall'alto", "sizes": "(max-width: 600px) 92vw, 560px"},
] + [
    {"chiave": f"rustico-{n}", "gruppo": "planimetria", "titolo": t, "didascalia": t,
     "file": f"rustico-{n}-1600.webp", "varianti": [f"rustico-{n}-960.webp", f"rustico-{n}-200.webp"],
     "alt": t, "sizes": "(max-width: 900px) 30vw, 180px"}
    for n, t in enumerate(DIDASCALIE_RUSTICO, 1)
]
DOCUMENTI = [{"chiave": "servizi-aggiuntivi", "titolo": "Servizi aggiuntivi", "file": "servizi-aggiuntivi.pdf"}]

PAGINE = [
    {"chiave": "home", "slug": "home", "titolo": "Home", "ordine": 0, "modello": "", "noindex": False, "file": "home.json",
     "titolo_seo": "Edera Country House | Eventi aziendali ad Albettone, Vicenza",
     "descrizione": "Edera Country House ad Albettone, Vicenza: location per eventi aziendali, meeting, convention, cene e team building."},
    {"chiave": "privacy", "slug": "privacy", "titolo": "Informativa privacy", "ordine": 1, "modello": "modelli/legale.php", "noindex": True,
     "file": "privacy.json", "titolo_seo": "Informativa privacy | Edera Country House", "descrizione": ""},
    {"chiave": "cookie", "slug": "cookie", "titolo": "Cookie", "ordine": 2, "modello": "modelli/legale.php", "noindex": True,
     "file": "cookie.json", "titolo_seo": "Cookie | Edera Country House", "descrizione": ""},
]


def controlla_vietato(testo, dove):
    if VIETATO in testo:
        raise SystemExit(f"carattere vietato U+2014 in {dove}")


def controlla_testi_home(el):
    """Ogni testo della Home deve esserci, uguale, nella pagina originale. Fanno eccezione i testi della
    planimetria elencati in pagine.ADATTATI (presi dal prototipo del committente, con la loro fonte);
    le sue capienze devono comunque essere quelle scritte nell'originale."""
    s = (ORIG / "index.html").read_text(encoding="utf-8")
    corpo = pagine.senza_tag(s[s.index("<main"):s.index("</main>")])
    mancanti = []
    for nodo in el:
        for t in pagine.testo_visibile(nodo):
            pulito = pagine.senza_tag(t).replace(" ↓", "").replace(" ↗", "")
            if not pulito or pulito in corpo or pulito in pagine.ADATTATI:
                continue
            if pulito in pagine.LEGENDA and all(x.strip() in corpo for x in pulito.split(",", 1)):
                continue
            if pulito in DIDASCALIE_RUSTICO or re.fullmatch(r"\d{2}", pulito):  # numeri delle sezioni
                continue
            mancanti.append(pulito)
    if mancanti:
        raise SystemExit("testi della Home non presenti nell'originale:\n  " + "\n  ".join(mancanti))


def copia_risorse():
    a = TEMA / "assets"
    if immagini.mancano():
        immagini.prepara()  # serve Pillow e gli originali in assets/originali/planimetria/
    (a / "img").mkdir(parents=True, exist_ok=True)
    for f in sorted(immagini.WEB.glob("*.webp")):
        shutil.copy2(f, a / "img" / f.name)
    for sotto, dove, schema in (("img", ORIG / "img", "*.webp"), ("fonts", ORIG / "fonts", "*.woff2")):
        (a / sotto).mkdir(parents=True, exist_ok=True)
        for f in sorted(dove.glob(schema)):
            shutil.copy2(f, a / sotto / f.name)
    (a / "doc").mkdir(exist_ok=True)
    for d in DOCUMENTI:
        shutil.copy2(ORIG / d["file"], a / "doc" / d["file"])
    he = a / "he"
    (he / "vendor").mkdir(parents=True, exist_ok=True)
    for f in ("he.js", "he.css"):
        shutil.copy2(KIT / f, he / f)
    for f in ("gsap.min.js", "ScrollTrigger.min.js", "SplitText.min.js", "LICENZE.txt"):
        shutil.copy2(KIT / "vendor" / f, he / "vendor" / f)
    # licenze dei caratteri (SIL Open Font License 1.1)
    (a / "fonts" / "LICENZE.txt").write_text(
        "Caratteri ospitati nel tema, tutti con licenza SIL Open Font License 1.1 (https://openfontlicense.org):\n"
        "- Newsreader, Copyright 2020 The Newsreader Project Authors (https://github.com/productiontype/Newsreader)\n"
        "- Jost, Copyright 2020 The Jost Project Authors (https://github.com/indestructible-type/Jost)\n"
        "- Bodoni Moda, Copyright 2020 The Bodoni Moda Project Authors (https://github.com/indestructible-type/Bodoni)\n"
        "File presi dal sito originale ederacountry.it (fonts/).\n", encoding="utf-8")


def contenuti():
    c = TEMA / "contenuti"
    c.mkdir(exist_ok=True)
    home = pagine.home()
    controlla_testi_home(home)
    dati = {
        "home.json": home,
        "privacy.json": pagine.legale("privacy", (ORIG / "privacy.html").read_text(encoding="utf-8")),
        "cookie.json": pagine.legale("cookie", (ORIG / "cookie.html").read_text(encoding="utf-8")),
        "planimetria.json": pagine.planimetria("02"),
        "planimetria-1.1.json": pagine.link_rustico_1_1(),
        "pagine.json": PAGINE,
        "media.json": {"immagini": IMMAGINI, "documenti": DOCUMENTI},
    }
    for nome, v in dati.items():
        (c / nome).write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    for im in IMMAGINI:
        for f in [im["file"]] + im["varianti"]:
            if not (TEMA / "assets" / "img" / f).exists():
                raise SystemExit(f"foto mancante: {f}")


def controlli_finali():
    sospetti = re.compile(r"(password|passwd|secret|api[_-]?key|token)\s*[=:]\s*['\"][^'\"]{6,}", re.I)
    for f in TEMA.rglob("*"):
        if f.is_file() and f.suffix in (".php", ".html", ".json", ".css", ".js", ".txt", ".md"):
            t = f.read_text(encoding="utf-8")
            controlla_vietato(t, str(f.relative_to(RADICE)))
            if sospetti.search(t) and "vendor" not in f.parts:
                raise SystemExit(f"possibile credenziale in {f}")


def zippa():
    if ZIP.exists():
        ZIP.unlink()
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(TEMA.rglob("*")):
            if f.is_file():
                z.write(f, "edera/" + str(f.relative_to(TEMA)))
    return ZIP.stat().st_size


def main():
    if TEMA.exists():
        shutil.rmtree(TEMA)
    WPDIR.mkdir(exist_ok=True)
    shutil.copytree(SORGENTE / "tema", TEMA)
    # anteprima del tema in Aspetto > Temi: la prima schermata del sito (1200 x 900)
    shutil.copy2(SORGENTE / "screenshot.jpg", TEMA / "screenshot.jpg")
    copia_risorse()
    contenuti()
    controlli_finali()
    peso = zippa()
    print(f"tema: {TEMA.relative_to(REPO)}  zip: {ZIP.relative_to(REPO)} ({peso // 1024} KB)")


if __name__ == "__main__":
    main()
