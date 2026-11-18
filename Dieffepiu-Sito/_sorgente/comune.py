"""Pezzi comuni: contesto dei link e delle immagini, testata, piede, apertura delle pagine interne.

Lo stesso codice scrive due uscite:
- modo "html": l'anteprima statica, con link relativi a file index.html (si apre anche da file://);
- modo "wp": i contenuti del tema WordPress, con i segnaposto {{casa}} e {{tema}} che il tema
  sostituisce con home_url() e con l'indirizzo della cartella del tema.
"""
import html as _html
import json
import pathlib

RADICE = pathlib.Path(__file__).resolve().parent.parent          # Dieffepiu-Sito/
SORGENTE = RADICE / "_sorgente"
IMMAGINI = json.loads((SORGENTE / "immagini.json").read_text(encoding="utf-8")) if (SORGENTE / "immagini.json").exists() else {}

TEL = "+39&nbsp;049&nbsp;8791175"
TEL_HREF = "tel:+390498791175"
MAIL = "info@dieffepiu.it"
MAPPA = "https://www.google.com/maps/search/?api=1&amp;query=Via+Lombardia+33+35020+Saonara+PD"
CATALOGO = "https://dieffepiu.it/catalogo.pdf"
PRIVACY = "https://www.iubenda.com/privacy-policy/11870350"
COOKIE = "https://www.iubenda.com/privacy-policy/11870350/cookie-policy"


def e(t):
    return _html.escape(t, quote=True)


class Ctx:
    def __init__(self, modo, percorso):
        self.modo = modo                  # "html" o "wp"
        self.percorso = percorso.strip("/")  # "" per la home, "sistemi/kit" ...

    @property
    def su(self):
        n = len([p for p in self.percorso.split("/") if p])
        return "../" * n

    def link(self, dove="", ancora=""):
        dove = dove.strip("/")
        if self.modo == "wp":
            return "{{casa}}/" + (dove + "/" if dove else "") + ancora
        return self.su + (dove + "/" if dove else "") + "index.html" + ancora

    def asset(self, nome):
        if self.modo == "wp":
            return "{{tema}}/assets/" + nome
        return self.su + "assets/" + nome

    def img(self, nome):
        return self.asset("img/" + nome)

    def foto(self, chiave, alt, sizes="100vw", lazy=True, classe=None, attr=""):
        """<img> con srcset dalle larghezze registrate in immagini.json."""
        d = IMMAGINI[chiave]
        larg = d["larghezze"]
        src = self.img(f"{chiave}-{larg[min(1, len(larg) - 1)]}.webp")
        srcset = ", ".join(f"{self.img(f'{chiave}-{w}.webp')} {w}w" for w in larg)
        w = larg[-1]
        h = round(w * d["h"] / d["w"])
        cl = f' class="{classe}"' if classe else ""
        lz = ' loading="lazy" decoding="async"' if lazy else ""
        return (f'<img{cl} src="{src}" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" '
                f'alt="{e(alt)}"{lz}{attr}>')

    def tavola(self, chiave, alt, lazy=True, larghezza_max=None):
        """Disegno del catalogo: un'immagine sola, mostrata al massimo alla sua misura vera (niente ingrandimenti)."""
        d = IMMAGINI[chiave]
        w, h = d["w"], d["h"]
        lz = ' loading="lazy" decoding="async"' if lazy else ""
        stile = f' style="width:{larghezza_max or round(w / 1.25)}px"'
        return (f'<img src="{self.img(chiave + ".webp")}" width="{w}" height="{h}" alt="{e(alt)}"{lz}{stile}>')


MENU = [("sistemi", "Sistemi"), ("macchine", "Macchine"), ("azienda", "Azienda"), ("contatti", "Contatti")]


def testata(c):
    voci = []
    for dove, nome in MENU:
        cur = ""
        if c.modo == "html" and (c.percorso == dove or c.percorso.startswith(dove + "/")):
            cur = ' aria-current="page"'
        voci.append(f'      <a href="{c.link(dove)}"{cur}>{nome}</a>')
    voci = "\n".join(voci)
    return f'''<header class="testata">
  <div class="wrap">
    <a class="logo" href="{c.link()}" aria-label="Dieffepiu, pagina iniziale"><img src="{c.img('logo-100.webp')}" width="178" height="100" alt="DIEFFE+"></a>
    <nav class="menu" id="menu" aria-label="Principale">
<!--voci-->
{voci}
<!--/voci-->
    </nav>
    <div class="destra">
      <a class="tel-testata num" href="{TEL_HREF}">{TEL}</a>
      <button class="apri-menu" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>'''


def piede(c):
    L = c.link
    return f'''<footer class="piede">
  <div class="wrap">
    <div class="griglia alto">
      <div class="firma">
        <img src="{c.img('logo-208.webp')}" width="369" height="208" alt="DIEFFE+" loading="lazy">
        <p>Sistemi, componenti e macchine per chi produce zanzariere. Saonara (Padova), dal&nbsp;1987.</p>
        <p class="contatti-piede num"><a href="{TEL_HREF}">{TEL}</a><br>
        <a href="mailto:{MAIL}">{MAIL}</a><br>
        <a href="{MAPPA}">Via Lombardia 33, Saonara (PD)</a></p>
      </div>
      <form class="notizie" action="#" method="post" aria-labelledby="t-notizie">
          <h2 id="t-notizie">Fiere e aggiornamenti del catalogo</h2>
          <p>Una mail quando esce una linea nuova, quando cambia il catalogo e prima di ogni fiera.</p>
          <div class="campo">
            <label class="sr" for="email-notizie">Indirizzo email</label>
            <input id="email-notizie" type="email" name="email" autocomplete="email" placeholder="nome@azienda.it" required>
            <button type="submit">Iscriviti</button>
          </div>
          <label class="consenso"><input type="checkbox" name="consenso" required> <span>Ho letto l’<a href="{PRIVACY}">informativa privacy</a> e accetto di ricevere queste comunicazioni.</span></label>
          <p class="esito" id="esito-notizie" aria-live="polite"></p>
      </form>

      <div class="colonne">
        <section>
          <h3 class="titolo-colonna">Sistemi</h3>
          <button class="fisarmonica-btn" type="button" aria-expanded="false" aria-controls="c-sistemi">Sistemi <span aria-hidden="true">+</span></button>
          <ul id="c-sistemi">
            <li><a href="{L('sistemi/kit')}">Sistema in kit</a></li>
            <li><a href="{L('sistemi/a-misura')}">Sistema a misura</a></li>
            <li><a href="{L('sistemi/carrarmato')}">Carrarmato TANK®</a></li>
            <li><a href="{L('sistemi/plisse')}">Plissé PLIXI®</a></li>
            <li><a href="{L('sistemi/battente')}">Battente e schermi</a></li>
            <li><a href="{L('sistemi/componenti')}">Componenti universali</a></li>
            <li><a href="{L('sistemi')}">Tutte le linee</a></li>
          </ul>
        </section>
        <section>
          <h3 class="titolo-colonna">Macchine</h3>
          <button class="fisarmonica-btn" type="button" aria-expanded="false" aria-controls="c-macchine">Macchine <span aria-hidden="true">+</span></button>
          <ul id="c-macchine">
<!--macchine-piede-->
          </ul>
        </section>
        <section>
          <h3 class="titolo-colonna">Azienda</h3>
          <button class="fisarmonica-btn" type="button" aria-expanded="false" aria-controls="c-azienda">Azienda <span aria-hidden="true">+</span></button>
          <ul id="c-azienda">
            <li><a href="{L('azienda')}">Chi siamo</a></li>
            <li><a href="{L('news')}">Fiere e novità</a></li>
            <li><a href="{CATALOGO}">Catalogo PDF</a></li>
            <li><a href="{L('area-riservata')}">Area riservata</a></li>
            <li><a href="{L('contatti')}">Contatti</a></li>
          </ul>
        </section>
        <section>
          <h3 class="titolo-colonna">Seguici</h3>
          <button class="fisarmonica-btn" type="button" aria-expanded="false" aria-controls="c-social">Seguici <span aria-hidden="true">+</span></button>
          <ul id="c-social">
            <li><a href="https://www.youtube.com/channel/UCuqwKa-y9ZYN9wEd7YAQmXw">YouTube</a></li>
            <li><a href="https://www.facebook.com/dieffepiusrlzanzariere">Facebook</a></li>
          </ul>
        </section>
      </div>
    </div>

    <div class="legale num">
      <span>© 2026 Dieffepiu S.r.l.</span>
      <span>P.IVA IT01335450282</span>
      <span>REA PD-204413</span>
      <span>Capitale sociale 300.000 euro</span>
      <span>PEC <a href="mailto:dieffepiu@pec.it">dieffepiu@pec.it</a></span>
      <span class="spinta"><a href="{PRIVACY}">Privacy</a>&emsp;<a href="{COOKIE}">Cookie</a></span>
    </div>
  </div>
</footer>'''


def briciole(c, voci):
    """voci: [(percorso, nome), ...]; l'ultima e' la pagina corrente, senza link."""
    pezzi = [f'<a href="{c.link()}">Home</a>']
    for i, (dove, nome) in enumerate(voci):
        if i == len(voci) - 1:
            pezzi.append(f'<span aria-current="page">{nome}</span>')
        else:
            pezzi.append(f'<a href="{c.link(dove)}">{nome}</a>')
    sep = '<span class="sep" aria-hidden="true">/</span>'
    return f'<nav class="briciole" aria-label="Sei qui">{sep.join(pezzi)}</nav>'


def richiesta(c, titolo="Schede tecniche e listini", testo=None):
    testo = testo or ("Listini, schede di taglio e disegni li mandiamo alle aziende del settore. "
                      "Diteci che cosa producete e quale linea vi interessa.")
    return f'''<section class="wrap griglia richiesta" aria-labelledby="t-richiesta">
  <h2 id="t-richiesta">{titolo}</h2>
  <div class="r-testo">
    <p>{testo}</p>
    <div class="azioni-r">
      <a class="bottone" href="{c.link('contatti')}">Scriveteci</a>
      <a class="tel-r num" href="{TEL_HREF}">{TEL}</a>
    </div>
  </div>
</section>'''
