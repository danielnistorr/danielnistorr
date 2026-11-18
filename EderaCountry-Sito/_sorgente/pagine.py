"""Le pagine del sito come dati di Elementor: contenitori e widget normali (Titolo, Editor di testo, Immagine,
Pulsante, Elenco icone, Shortcode), con le classi CSS che il tema aggancia in assets/sito.css e legale.css.

I testi della Home sono quelli di originale/index.html, scritti qui a mano nella struttura di Elementor
(build.py controlla che ogni testo ci sia davvero nell'originale). Le pagine legali si leggono direttamente
da originale/privacy.html e originale/cookie.html.

Segnaposto che l'installatore del tema sostituisce:
  {"edera_img": "casa"}   la foto "casa" della libreria media (ID e indirizzo)
  {{pagina:privacy}}      l'indirizzo della pagina Informativa privacy
  {{media:servizi-aggiuntivi}}  l'ID del PDF nella libreria media
"""
import base64
import hashlib
import html
import json
import re
import urllib.parse
from html.parser import HTMLParser

NBSP = " "


class Ids:
    """ID di Elementor (7 caratteri esadecimali) stabili: dipendono dalla pagina e dalla posizione."""

    def __init__(self, pagina):
        self.pagina = pagina
        self.n = 0

    def __call__(self):
        self.n += 1
        return hashlib.md5(f"edera/{self.pagina}/{self.n}".encode()).hexdigest()[:7]


ZERO = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
GAP0 = {"unit": "px", "size": 0, "column": "0", "row": "0", "isLinked": True}


class Costruttore:
    def __init__(self, pagina):
        self.id = Ids(pagina)

    def C(self, classi, *figli, tag=None, ancora=None, nome=None, interno=True):
        """Contenitore a tutta larghezza: l'impaginazione la danno le classi del tema."""
        s = {"content_width": "full", "flex_direction": "column", "css_classes": classi,
             "padding": dict(ZERO), "flex_gap": dict(GAP0)}
        if tag:
            s["html_tag"] = tag
        if ancora:
            s["_element_id"] = ancora
        if nome:
            s["_title"] = nome
        return {"id": self.id(), "elType": "container", "isInner": interno, "settings": s,
                "elements": [f for f in figli if f]}

    def _w(self, tipo, s, classi, nome):
        if classi:
            s["_css_classes"] = classi
        if nome:
            s["_title"] = nome
        return {"id": self.id(), "elType": "widget", "widgetType": tipo, "isInner": False, "settings": s, "elements": []}

    def H(self, testo, tag="h2", classi="", nome=None):
        """Widget Titolo. tag: h1, h2, h3, div, span, p."""
        return self._w("heading", {"title": testo, "header_size": tag}, classi, nome)

    def T(self, html_, classi="", nome=None):
        """Widget Editor di testo."""
        return self._w("text-editor", {"editor": html_}, classi, nome)

    def IMG(self, chiave, classi="", didascalia=None, nome=None):
        """Widget Immagine dalla libreria media (dimensione piena: srcset e sizes li scrive WordPress)."""
        s = {"image": {"edera_img": chiave}, "image_size": "full",
             "caption_source": "custom" if didascalia else "none"}
        if didascalia:
            s["caption"] = didascalia
        return self._w("image", s, classi, nome)

    def BTN(self, testo, url, classi="", esterno=False, nome=None):
        """Widget Pulsante. La freccia finale (↗ ↓) la impagina il tema."""
        link = {"url": url, "is_external": "on" if esterno else "", "nofollow": "",
                "custom_attributes": "rel|noopener" if esterno else ""}
        return self._w("button", {"text": testo, "link": link}, classi, nome)

    def LISTA(self, voci, classi="", nome=None):
        """Widget Elenco icone, senza icone: un <ul> con una voce per riga."""
        el = [{"text": v, "selected_icon": {"value": "", "library": ""}, "_id": self.id()} for v in voci]
        return self._w("icon-list", {"icon_list": el}, classi, nome)

    def PIN(self, testo, x, y, classi, link="", nome=None):
        """Pallino della planimetria: un Pulsante in posizione assoluta, con offset in % sulla foto
        (Avanzate > Posizionamento). Si sposta anche trascinandolo nell'editor."""
        s = {"text": testo,
             "link": {"url": link, "is_external": "", "nofollow": "", "custom_attributes": ""},
             "_position": "absolute",
             "_offset_orientation_h": "start", "_offset_x": {"unit": "%", "size": x, "sizes": []},
             "_offset_orientation_v": "start", "_offset_y": {"unit": "%", "size": y, "sizes": []}}
        return self._w("button", s, classi, nome or f"Pallino {testo}")

    def GAL(self, chiavi, classi="", colonne=3, ancora=None, nome=None):
        """Widget Galleria di base: foto dalla libreria media, link al file, lightbox di Elementor.
        ancora: l'ID CSS (Avanzato > ID CSS), per esempio "foto-rustico"."""
        s = {"wp_gallery": [{"edera_img": k} for k in chiavi], "thumbnail_size": "full",
             "gallery_columns": str(colonne), "gallery_link": "file", "open_lightbox": "yes",
             "gallery_display_caption": "none"}
        if ancora:
            s["_element_id"] = ancora
        return self._w("image-gallery", s, classi, nome)

    def SC(self, codice, classi="", nome=None):
        return self._w("shortcode", {"shortcode": codice}, classi, nome)


def testa(b, n, titolo, testo):
    """Testa di sezione: numero (visibile da 1400 px), titolo h2 a sinistra, testo a destra."""
    return b.C("testa-sezione",
               b.H(n, "span", "n-sez", nome="Numero della sezione"),
               b.H(titolo, "h2"),
               b.T(f"<p>{testo}</p>"))


# Planimetria (tema 1.1): posizioni dei pallini in % sulla foto, prese dal prototipo del committente
# (x e y in % della larghezza e dell'altezza della foto). In Elementor anche l'offset verticale in % si conta
# sulla larghezza (e' cosi' che l'editor lo calcola quando si trascina un pallino): per questo i pallini stanno
# in un contenitore quadrato largo quanto la foto e la y si converte con il rapporto della foto (1604 / 981).
RAPPORTO_FOTO = 1604 / 981
PALLINI = [
    # nome, x, y, etichetta a sinistra
    ("Rustico", 29.5, 47.5, True),
    ("Serra", 33, 32.5, False),
    ("Piscina", 49.5, 47.5, False),
    ("Casetta bar", 36, 66.5, True),
    ("Grill", 16, 32.5, True),
    ("Spazio verde", 24, 61.5, False),
]
LEGENDA = ["Rustico, fino a 50 persone", "Serra, fino a 70 persone", "Piscina, fino a 30 persone",
           "Casetta bar", "Grill", "Spazio verde"]
FOTO_RUSTICO = ["rustico-1", "rustico-2", "rustico-3", "rustico-4", "rustico-5"]
# testi della planimetria che non sono uguali in originale/index.html, con la loro fonte
ADATTATI = {
    "Planimetria interattiva.": "titolo del prototipo (Planimetria interattiva), con il punto come gli altri titoli",
    "Seleziona il pallino sul Rustico per aprire le fotografie.": "prototipo, senza 'rosso': il pallino non e' piu' rosso",
    "Scegli nel preventivo": "richiesta del committente",
    "Casetta bar": "prototipo", "Grill": "prototipo", "Spazio verde": "prototipo",
}


def planimetria(numero="02"):
    """La sezione della planimetria, tutta in widget di Elementor. Ha un suo costruttore di ID, cosi' e'
    identica nella Home nuova e quando il bottone del tema 1.1 la aggiunge a una Home gia' installata."""
    b = Costruttore("planimetria")
    # tema 1.1.1: il pallino del Rustico ha il link "#foto-rustico" e apre il lightbox di Elementor sulla galleria
    # con ID CSS "foto-rustico" (la regola sta in assets/sito.js). Lo stesso vale per qualunque pallino.
    galleria = b.GAL(FOTO_RUSTICO, "planimetria-galleria", ancora="foto-rustico", nome="Foto del Rustico (lightbox)")
    pallini = []
    for i, (nome, x, y, sinistra) in enumerate(PALLINI):
        classi = "pallino" + (" pallino-attivo" if i == 0 else "") + (" pallino-sinistra" if sinistra else "")
        pallini.append(b.PIN(nome, x, round(y * RAPPORTO_FOTO, 2), classi, "#foto-rustico" if i == 0 else ""))
    return b.C(
        "sezione bianca planimetria-sezione",
        b.C("wrap",
            testa(b, numero, "Planimetria interattiva.", "Seleziona il pallino sul Rustico per aprire le fotografie."),
            b.C("planimetria",
                b.C("planimetria-mappa etichette-mappa-larga",
                    b.IMG("planimetria", "planimetria-foto", nome="Foto dall'alto"),
                    b.C("planimetria-punti", *pallini, nome="Pallini (si spostano trascinandoli)"),
                    nome="Mappa e pallini"),
                b.C("planimetria-lato",
                    b.LISTA(LEGENDA, "planimetria-legenda", nome="Legenda (stesso ordine dei pallini)"),
                    b.H("Rustico", "h3"),
                    galleria,
                    b.BTN("Scegli nel preventivo ↓", "#preventivo", "pulsante pulsante-verde"),
                    nome="Legenda e foto"))),
        tag="section", ancora="planimetria", nome="Planimetria", interno=False)


def link_rustico_1_1():
    """Il link del pallino del Rustico com'era nel tema 1.1 (azione di Elementor con l'ID della galleria in base64):
    il bottone "Semplifica il link del Rustico" lo cambia in "#foto-rustico" solo se e' ancora questo."""
    nuovo_id = Ids("planimetria")
    ids = [nuovo_id(), nuovo_id()]  # stesso ordine di planimetria(): prima la galleria, poi il pallino del Rustico
    azione = "#elementor-action:action=lightbox&settings=" + base64.b64encode(
        json.dumps({"slideshow": ids[0]}, separators=(",", ":")).encode()).decode()
    return {"link": "#" + urllib.parse.quote(azione[1:], safe=""), "galleria": ids[0], "pallino": ids[1]}


MAPPA = "https://www.google.com/maps/search/?api=1&query=Via%20Pal%C3%B9%20Massara%2010%2C%20Albettone%20VI"
STRADA = "https://www.google.com/maps/dir/?api=1&destination=Via%20Pal%C3%B9%20Massara%2010%2C%20Albettone%20VI"


def home():
    b = Costruttore("home")
    C, H, T, IMG, BTN = b.C, b.H, b.T, b.IMG, b.BTN

    def testa_sezione(n, titolo, testo):
        return testa(b, n, titolo, testo)

    apertura = C(
        "apertura moto-testata",
        IMG("apertura", "apertura-foto", nome="Foto d'apertura"),
        C("wrap",
          C("apertura-testo",
            H(f"<span>Gli eventi</span> <span>che lasciano il{NBSP}segno.</span>", "h1", "moto-righe"),
            T("<p>Un contesto distintivo ad Albettone, nel Vicentino, per incontri aziendali, convention, team building e serate da ricordare.</p>", "lead"),
            C("azioni",
              BTN("Calcola il tuo preventivo", "#preventivo", "pulsante pulsante-chiaro"),
              BTN("Scopri la location", "#location", "collega"))),
          b.LISTA(["Albettone · Vicenza", "Rustico, serra, piscina, spazio esterno"], "fatti-apertura", nome="Luogo e spazi")),
        tag="section", nome="Apertura", interno=False)

    def spazio(n, nome, persone):
        return C("spazio-voce",
                 H(n, "span", "i"),
                 H(nome, "div", "nome"),
                 H(persone, "span", "capienza"))

    location = C(
        "sezione bianca",
        C("wrap casa",
          C("casa-testo",
            H("01", "span", "n-sez", nome="Numero della sezione"),
            H("Il luogo giusto per dare spazio alle idee.", "h2"),
            T("<p>Spazi interni ed esterni, piscina e scenari suggestivi per costruire un evento aziendale su misura.</p>", "lead scura"),
            T("<p>Dalla riunione riservata alla grande occasione con il team, ogni dettaglio può contribuire a creare un'esperienza riconoscibile.</p>"
              "<p>Una cornice verde e contemporanea, capace di cambiare atmosfera durante la giornata e trasformarsi in una location d'impatto la sera.</p>"),
            C("spazi-elenco",
              spazio("01", "Rustico", "fino a 50 persone"),
              spazio("02", "Serra", "fino a 70 persone"),
              spazio("03", "Piscina", "fino a 30 persone, anche mezza giornata"),
              spazio("04", "Spazio esterno", "fino a 120 persone"),
              nome="Gli spazi")),
          IMG("casa", "casa-foto", "Il giardino la sera, tra gli ulivi e la piscina.")),
        tag="section", ancora="location", nome="La location", interno=False)

    def formato(chiave, n, titolo, testo):
        return C("formato",
                 IMG(chiave),
                 H(n, "span", "num"),
                 H(titolo, "h3"),
                 T(f"<p>{testo}</p>"))

    eventi = C(
        "sezione",
        C("wrap",
          testa_sezione("03", "Un format per ogni occasione.", "Una location versatile per riunire persone, idee e obiettivi."),
          C("formati",
            formato("meeting", "01", "Meeting &amp; convention", "Incontri aziendali, presentazioni, momenti di confronto e appuntamenti professionali."),
            formato("celebrazioni", "02", "Celebrazioni", "Serate aziendali, anniversari, ricorrenze e occasioni per valorizzare il gruppo."),
            formato("teambuilding", "03", "Team building", "Esperienze condivise in un contesto informale, all'aperto e da vivere insieme."),
            nome="I formati")),
        tag="section", ancora="eventi", nome="Eventi", interno=False)

    galleria = C(
        "sezione bianca",
        C("wrap",
          testa_sezione("04", "Ogni spazio ha la sua atmosfera.", "Una selezione di fotografie reali fornite dalla struttura."),
          C("galleria",
            IMG("piscina-sera", "g-a moto-taglio", "La piscina, durante un ricevimento serale."),
            IMG("sala", "g-b", "La sala con le travi a vista."),
            IMG("giardino", "g-c", "Il giardino apparecchiato."),
            nome="Le foto")),
        tag="section", ancora="gallery", nome="Gallery", interno=False)

    riga = f"Meeting ·{NBSP}Convention ·{NBSP}Team{NBSP}building ·{NBSP}Celebrazioni"
    fascia = C(
        "fascia",
        C("wrap",
          C("fascia-testo",
            H("La tua idea parte da qui.", "h2"),
            T("<p>Indicaci le caratteristiche principali dell'evento: riceverai una prima stima indicativa, da confermare con un'offerta personalizzata.</p>"),
            H(riga, "p", "formati-riga")),
          BTN("Vai al preventivo flash ↓", "#preventivo", "pulsante pulsante-chiaro")),
        tag="section", nome="Fascia verde", interno=False)

    preventivo = C(
        "sezione",
        C("wrap",
          testa_sezione("05", "Una prima stima, in pochi passaggi.", "Scegli gli spazi, il numero di partecipanti e la durata: la stima si aggiorna mentre compili."),
          b.SC('[edera_preventivo pdf="{{media:servizi-aggiuntivi}}"]', "calcolatore", nome="Calcolatore (prezzi in config/preventivo.php)")),
        tag="section", ancora="preventivo", nome="Preventivo flash", interno=False)

    def domanda(n, q, a):
        return C("faq-voce",
                 H(n, "span", "i nascosto-lettori"),
                 C("faq-risposta", H(q, "h3"), T(f"<p>{a}</p>")))

    faq = C(
        "sezione bianca",
        C("wrap faq",
          C("faq-testa",
            H("06", "span", "n-sez", nome="Numero della sezione"),
            H("Domande frequenti.", "h2")),
          C("faq-elenco",
            domanda("01", "Possiamo portare un catering di nostra scelta?",
                    "Certamente! Puoi affidarti a un catering di tua fiducia e organizzare liberamente il servizio. In alternativa, possiamo consigliarti alcuni professionisti del settore."),
            domanda("02", "È possibile utilizzare la piscina?",
                    "Sì, la piscina è a disposizione per un massimo di 30 persone. Per garantire la sicurezza di tutti, è obbligatoria la presenza di un bagnino in possesso di brevetto. Se non hai già una persona di fiducia con questa qualifica, possiamo fornirti noi dei contatti."),
            domanda("03", "È disponibile un parcheggio?",
                    "Sì, la struttura dispone di un parcheggio privato a disposizione, così da permettere a tutti di raggiungere la location comodamente."),
            nome="Le domande")),
        tag="section", ancora="faq", nome="Domande frequenti", interno=False)

    contatti = C(
        "sezione",
        C("wrap contatti",
          C("contatti-testo",
            H("07", "span", "n-sez", nome="Numero della sezione"),
            H("Il prossimo evento può iniziare qui.", "h2"),
            T("<p>Condividi l'idea, il numero di ospiti e le esigenze della tua azienda. Definiremo insieme la soluzione più adatta.</p>")),
          C("scheda",
            H("Edera Country House", "h3"),
            C("scheda-dati",
              H("Indirizzo", "div", "dt"),
              C("dd",
                T(f'<a href="{html.escape(MAPPA)}" target="_blank" rel="noopener" title="Apri in Google Maps">Via Palù Massara, 10<br>Albettone (VI)</a>'),
                BTN("Indicazioni stradali ↗", STRADA, "strada", esterno=True)),
              H("Email", "div", "dt"),
              T('<a href="mailto:edera@ederacountry.it">edera@ederacountry.it</a>', "dd"),
              H("Telefono", "div", "dt"),
              T('<a href="tel:+393494731515">349 473 1515</a>', "dd"),
              nome="Recapiti"),
            BTN("Richiedi una stima", "#preventivo", "pulsante pulsante-verde"))),
        tag="section", ancora="contatti", nome="Contatti", interno=False)

    return [apertura, location, planimetria("02"), eventi, galleria, fascia, preventivo, faq, contatti]


# ------------------------------------------------------------------ pagine legali

class _Main(HTMLParser):
    """Divide il <main> di privacy.html e cookie.html nei suoi blocchi di primo livello."""

    VUOTI = {"br", "img", "hr", "input", "meta", "link"}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.dentro = False
        self.livello = 0
        self.blocchi = []
        self.corrente = None

    def handle_starttag(self, tag, attrs):
        testo = self.get_starttag_text()
        if tag == "main":
            self.dentro = True
            return
        if not self.dentro:
            return
        if self.livello == 0:
            self.corrente = {"tag": tag, "classe": dict(attrs).get("class", ""), "inizio": testo, "html": ""}
        else:
            self.corrente["html"] += testo
        if tag not in self.VUOTI:
            self.livello += 1

    def handle_startendtag(self, tag, attrs):
        if self.dentro and self.corrente is not None and self.livello > 0:
            self.corrente["html"] += self.get_starttag_text()

    def handle_endtag(self, tag):
        if tag == "main":
            self.dentro = False
            return
        if not self.dentro or tag in self.VUOTI:
            return
        self.livello -= 1
        if self.livello == 0:
            self.blocchi.append(self.corrente)
            self.corrente = None
        else:
            self.corrente["html"] += f"</{tag}>"

    def handle_data(self, data):
        if self.dentro and self.corrente is not None:
            self.corrente["html"] += data

    def handle_entityref(self, name):
        self.handle_data(f"&{name};")

    def handle_charref(self, name):
        self.handle_data(f"&#{name};")


def legale(chiave, sorgente):
    """Una pagina legale: etichetta, titolo, riquadro iniziale, poi un Titolo h2 e un Editor di testo per sezione."""
    p = _Main()
    p.feed(sorgente)
    b = Costruttore(chiave)
    widget = []
    testo = []

    def chiudi_testo():
        if testo:
            widget.append(b.T("\n".join(testo)))
            testo.clear()

    for bl in p.blocchi:
        corpo = bl["html"].strip()
        # i link alle altre pagine del sito diventano quelli di WordPress
        corpo = corpo.replace('href="privacy.html"', 'href="{{pagina:privacy}}"').replace('href="cookie.html"', 'href="{{pagina:cookie}}"')
        corpo = corpo.replace('href="index.html"', 'href="{{casa}}"')
        if bl["tag"] == "span" and "eti" in bl["classe"]:
            chiudi_testo()
            widget.append(b.H(corpo, "span", "eti"))
        elif bl["tag"] in ("h1", "h2"):
            chiudi_testo()
            widget.append(b.H(corpo, bl["tag"]))
        elif bl["tag"] == "p" and bl["classe"] in ("avviso", "aggiornato"):
            chiudi_testo()
            widget.append(b.T(f"<p>{corpo}</p>", bl["classe"]))
        else:
            testo.append(f"{bl['inizio']}{corpo}</{bl['tag']}>")
    chiudi_testo()
    return [b.C("legale", *widget, nome="Testo", interno=False)]


def testo_visibile(nodo):
    """Tutti i testi di un albero di Elementor (per il controllo con l'originale)."""
    out = []
    s = nodo.get("settings", {})
    for k in ("title", "editor", "text", "caption"):
        if k in s:
            out.append(s[k])
    for v in s.get("icon_list", []):
        out.append(v["text"])
    for f in nodo.get("elements", []):
        out += testo_visibile(f)
    return out


def senza_tag(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace(NBSP, " ")
    return re.sub(r"\s+", " ", t).strip()
