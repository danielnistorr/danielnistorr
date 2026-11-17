"""Le pagine di Villa Eidos come dati di Elementor: contenitori e widget della versione gratuita (Titolo, Editor di
testo, Immagine, Pulsante, Shortcode), con le classi CSS che il tema aggancia in assets/sito.css.

I testi vengono solo dal testo del cliente (villaeidos.it.doc): build.py controlla che ogni frase della Home sia in
FONTI qui sotto, cioe' copiata dal testo o scritta con le sue parole. Niente numeri di posti, metri quadri,
servizi, orari o anni: il testo non li da'.

Segnaposti che l'installatore del tema sostituisce:
  {"ve_img": "sale-riunioni"}   la foto con quella chiave nella libreria media (ID e indirizzo)
  {{pagina:privacy}}            l'indirizzo della pagina Informativa privacy
  {{casa}}                      l'indirizzo della Home
"""
import hashlib
import html
import re
import urllib.parse

NBSP = " "

TEL = "049 0990550"
TEL_LINK = "+390490990550"
EMAIL = "eidos@eco-management.it"
COMUNE = "Albignasego (PD)"
INGRESSI = ["Via Battaglia 67", "via Colombo 2", "via Colombo 6A"]


def mappa(via):
    """Link a Google Maps per un indirizzo (una ricerca: nessuna mappa incorporata, nessun cookie)."""
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(f"{via}, Albignasego PD")


MAPPA = mappa("Via Battaglia 67")

# Il testo del cliente, frase per frase (accenti corretti dalla codifica Windows-1252). E' la fonte di tutti i testi.
FONTE = """Riunioni, Convegni, Sedi di Rappresentanza in una villa storica alle porte di Padova
Il complesso si trova ad Albignasego, in una posizione strategica dal punto di vista logistico. È a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud dell'autostrada A13 Bologna-Padova, ed è servito direttamente dalla SS16 Adriatica. Questo garantisce collegamenti rapidi con l'A4 Milano-Venezia, con il centro città e la stazione ferroviaria di Padova, e con l'aeroporto di Venezia.
La proprietà comprende una villa storica e un'ampia barchessa, immerse in un giardino centenario dotato di ampi parcheggi. Entrambi gli edifici sono stati riqualificati e adattati a funzioni direzionali, conservando i caratteri architettonici originali.
La villa ospita uffici e sedi di rappresentanza, con ambienti eleganti adatti all'accoglienza di clienti, partner e delegazioni istituzionali. La barchessa, grazie ai suoi volumi ampi e flessibili, accoglie sale riunioni di diverse dimensioni e una grande sala conferenze. Quest'ultima è adatta a convegni, presentazioni aziendali, eventi formativi e incontri con un pubblico numeroso.
L'insieme unisce il prestigio di una dimora storica alla funzionalità di un moderno polo direzionale e congressuale. È quindi una sede ideale per attività di rappresentanza, networking ed eventi business nel cuore produttivo del Veneto.
Per info: 049.0990550
Email: eidos@eco-management.it
Villa EIDOS
ALBIGNASEGO (PD) Via Battaglia, 67 - via Colombo, 2 - via Colombo, 6A"""

# Ogni testo della Home che non e' copiato tale e quale dalla FONTE, con la frase della fonte da cui viene.
# build.py ferma la costruzione se in pagina c'e' un testo che non sta ne' nella FONTE ne' qui.
ADATTATI = {
    "Riunioni, convegni, sedi di rappresentanza in una villa storica alle porte di Padova": "titolo del testo, in minuscolo",
    "Ad Albignasego, a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud dell'A13.": "Il complesso si trova ad Albignasego... a pochi minuti dalla Tangenziale... casello Padova Sud dell'autostrada A13",
    "Chiama " + TEL: "Per info: 049.0990550",
    "Richiedi disponibilità": "invito del sito (richiesta del committente)",
    "Una villa storica e un'ampia barchessa, immerse in un giardino centenario con ampi parcheggi": "La proprietà comprende una villa storica e un'ampia barchessa, immerse in un giardino centenario dotato di ampi parcheggi.",
    "Villa": "villa storica", "Barchessa": "un'ampia barchessa", "Giardino": "giardino centenario", "Parcheggi": "ampi parcheggi",
    "Uffici e sedi di rappresentanza.": "La villa ospita uffici e sedi di rappresentanza",
    "Sale riunioni di diverse dimensioni e una grande sala conferenze.": "accoglie sale riunioni di diverse dimensioni e una grande sala conferenze",
    "Centenario: la villa e la barchessa vi sono immerse.": "immerse in un giardino centenario",
    "Ampi, nel giardino della proprietà.": "un giardino centenario dotato di ampi parcheggi",
    "Uffici, sale riunioni e una grande sala conferenze": "uffici... sale riunioni... una grande sala conferenze",
    "Uffici e sedi di rappresentanza": "La villa ospita uffici e sedi di rappresentanza",
    "Nella villa, in ambienti eleganti adatti all'accoglienza.": "La villa ospita uffici e sedi di rappresentanza, con ambienti eleganti adatti all'accoglienza",
    "Sale riunioni": "sale riunioni di diverse dimensioni",
    "Di diverse dimensioni, nei volumi ampi e flessibili della barchessa.": "La barchessa, grazie ai suoi volumi ampi e flessibili, accoglie sale riunioni di diverse dimensioni",
    "Sala conferenze": "una grande sala conferenze",
    "Una grande sala nella barchessa, per convegni, presentazioni aziendali ed eventi formativi.": "La barchessa... accoglie... una grande sala conferenze. Quest'ultima è adatta a convegni, presentazioni aziendali, eventi formativi",
    "Reception e sale d'attesa": "nomi delle foto del cliente (reception.jpeg, sale d'attesa.jpeg)",
    "Il prestigio di una dimora storica e la funzionalità di un moderno polo direzionale e congressuale": "L'insieme unisce il prestigio di una dimora storica alla funzionalità di un moderno polo direzionale e congressuale.",
    "Rappresentanza": "attività di rappresentanza",
    "Clienti, partner e delegazioni istituzionali, accolti negli ambienti della villa.": "ambienti eleganti adatti all'accoglienza di clienti, partner e delegazioni istituzionali",
    "Riunioni": "Riunioni (titolo del testo)",
    "In sale di diverse dimensioni, nella barchessa.": "La barchessa... accoglie sale riunioni di diverse dimensioni",
    "Convegni, presentazioni e formazione": "convegni, presentazioni aziendali, eventi formativi",
    "Nella grande sala conferenze, anche con un pubblico numeroso.": "una grande sala conferenze... incontri con un pubblico numeroso",
    "Networking ed eventi business": "attività di rappresentanza, networking ed eventi business",
    "Una sede nel cuore produttivo del Veneto.": "È quindi una sede ideale per... nel cuore produttivo del Veneto",
    "Come arrivare": "titolo di servizio (richiesta del committente)",
    "Ad Albignasego, in una posizione strategica dal punto di vista logistico.": "Il complesso si trova ad Albignasego, in una posizione strategica dal punto di vista logistico.",
    "Apri la mappa": "link a Google Maps (richiesta del committente)",
    "A pochi minuti": "È a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud",
    "Tangenziale di Padova": "Tangenziale di Padova",
    "Casello Padova Sud, A13 Bologna-Padova": "casello Padova Sud dell'autostrada A13 Bologna-Padova",
    "Servito direttamente": "ed è servito direttamente dalla SS16 Adriatica",
    "SS16 Adriatica": "SS16 Adriatica",
    "Collegamenti rapidi": "Questo garantisce collegamenti rapidi",
    "A4 Milano-Venezia": "l'A4 Milano-Venezia",
    "Centro e stazione ferroviaria di Padova": "con il centro città e la stazione ferroviaria di Padova",
    "Aeroporto di Venezia": "l'aeroporto di Venezia",
    "Tre ingressi": "Via Battaglia, 67 - via Colombo, 2 - via Colombo, 6A (tre indirizzi, tre ingressi: committente)",
    "Richiesta di disponibilità": "titolo di servizio (richiesta del committente)",
    "Il modulo prepara una mail per " + EMAIL + ", da inviare dal proprio programma di posta. Per una risposta a voce, il telefono.":
        "Email: eidos@eco-management.it; Per info: 049.0990550",
}


class Ids:
    """ID di Elementor (7 caratteri esadecimali) stabili: dipendono dalla pagina e dalla posizione."""

    def __init__(self, pagina):
        self.pagina = pagina
        self.n = 0

    def __call__(self):
        self.n += 1
        return hashlib.md5(f"villaeidos/{self.pagina}/{self.n}".encode()).hexdigest()[:7]


ZERO = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
GAP0 = {"unit": "px", "size": 0, "column": "0", "row": "0", "isLinked": True}


def link(url, esterno=False):
    return {"url": url, "is_external": "on" if esterno else "", "nofollow": "",
            "custom_attributes": "rel|noopener" if esterno else ""}


class Costruttore:
    def __init__(self, pagina):
        self.id = Ids(pagina)

    def C(self, classi, *figli, tag=None, ancora=None, nome=None, interno=True):
        """Contenitore a tutta larghezza, senza spazi propri: l'impaginazione la danno le classi del tema."""
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

    def H(self, testo, tag="h2", classi="", nome=None, url=None, esterno=False):
        """Widget Titolo (h1, h2, h3, div, p), con un link se serve."""
        s = {"title": testo, "header_size": tag}
        if url:
            s["link"] = link(url, esterno)
        return self._w("heading", s, classi, nome)

    def T(self, html_, classi="", nome=None):
        """Widget Editor di testo."""
        return self._w("text-editor", {"editor": html_}, classi, nome)

    def IMG(self, chiave, classi="", nome=None):
        """Widget Immagine dalla libreria media, misura piena (srcset e sizes li scrive WordPress)."""
        return self._w("image", {"image": {"ve_img": chiave}, "image_size": "full", "caption_source": "none"}, classi, nome)

    def BTN(self, testo, url, classi="", esterno=False, nome=None):
        """Widget Pulsante."""
        return self._w("button", {"text": testo, "link": link(url, esterno)}, classi, nome)

    def SC(self, codice, classi="", nome=None):
        return self._w("shortcode", {"shortcode": codice}, classi, nome)


def home():
    b = Costruttore("home")
    C, H, T, IMG, BTN = b.C, b.H, b.T, b.IMG, b.BTN

    righe = ["Riunioni, convegni,", "sedi di rappresentanza", "in una villa storica", f"alle porte di{NBSP}Padova"]
    apertura = C(
        "apertura",
        C("wrap",
          H(" ".join(f"<span>{r}</span>" for r in righe), "h1", "moto-righe", nome="Titolo d'apertura (una riga per <span>)"),
          C("apertura-sotto",
            T("<p>Ad Albignasego, a pochi minuti dalla Tangenziale di Padova e dal casello Padova Sud dell'A13.</p>", "lead"),
            C("azioni",
              BTN(f"Chiama {TEL}", f"tel:{TEL_LINK}", "pulsante pulsante-filo", nome="Chiama"),
              BTN("Richiedi disponibilità", "#disponibilita", "pulsante pulsante-verde", nome="Richiedi disponibilità"),
              nome="Azioni"),
            nome="Frase e azioni"),
          IMG("apertura-fregio", "apertura-foto", nome="Foto d'apertura (oggi il fregio: si cambia con la foto della villa)")),
        tag="section", ancora="inizio", nome="Apertura", interno=False)

    def voce(parola, fatto):
        return C("luogo-voce", H(parola, "h3", "luogo-parola"), T(f"<p>{fatto}</p>", "luogo-fatto"), nome=parola)

    luogo = C(
        "sezione luogo",
        C("wrap",
          H("Una villa storica e un'ampia barchessa, immerse in un giardino centenario con ampi parcheggi", "h2", "luogo-titolo"),
          C("luogo-elenco",
            voce("Villa", "Uffici e sedi di rappresentanza."),
            voce("Barchessa", "Sale riunioni di diverse dimensioni e una grande sala conferenze."),
            voce("Giardino", "Centenario: la villa e la barchessa vi sono immerse."),
            voce("Parcheggi", "Ampi, nel giardino della proprietà."),
            nome="Le quattro parole"),
          T("<p>Entrambi gli edifici sono stati riqualificati e adattati a funzioni direzionali, conservando i caratteri architettonici originali.</p>", "luogo-chiusa")),
        tag="section", ancora="luogo", nome="Il luogo", interno=False)

    def spazio(classe, foto, titolo, testo, taglio=False):
        immagini = [IMG(f, "spazio-foto" + (" moto-taglio" if taglio and i == 0 else "")) for i, f in enumerate(foto)]
        figli = [C("spazio-foto-gruppo", *immagini, nome="Foto")] if len(immagini) > 1 else immagini
        figli.append(H(titolo, "h3", "spazio-nome"))
        if testo:
            figli.append(T(f"<p>{testo}</p>", "spazio-testo"))
        return C(f"spazio {classe}", *figli, nome=titolo)

    spazi = C(
        "sezione spazi",
        C("wrap",
          H("Uffici, sale riunioni e una grande sala conferenze", "h2", "spazi-titolo"),
          C("spazi-griglia",
            C("spazi-col spazi-col-larga",
              spazio("spazio-riunioni", ["sale-riunioni"], "Sale riunioni",
                     "Di diverse dimensioni, nei volumi ampi e flessibili della barchessa.", taglio=True),
              spazio("spazio-conferenze", ["sala-conferenze"], "Sala conferenze",
                     "Una grande sala nella barchessa, per convegni, presentazioni aziendali ed eventi formativi.", taglio=True),
              nome="Colonna larga"),
            C("spazi-col spazi-col-stretta",
              spazio("spazio-uffici", ["uffici"], "Uffici e sedi di rappresentanza",
                     "Nella villa, in ambienti eleganti adatti all'accoglienza."),
              spazio("spazio-accoglienza", ["reception", "sale-attesa"], "Reception e sale d'attesa", ""),
              nome="Colonna stretta"),
            nome="Gli spazi")),
        tag="section", ancora="spazi", nome="Gli spazi", interno=False)

    def uso(nome_, testo):
        return C("uso", H(nome_, "h3", "uso-nome"), T(f"<p>{testo}</p>", "uso-testo"), nome=nome_)

    attivita = C(
        "sezione attivita",
        C("wrap",
          H("Il prestigio di una dimora storica e la funzionalità di un moderno polo direzionale e congressuale", "h2", "attivita-titolo"),
          C("usi",
            uso("Rappresentanza", "Clienti, partner e delegazioni istituzionali, accolti negli ambienti della villa."),
            uso("Riunioni", "In sale di diverse dimensioni, nella barchessa."),
            uso("Convegni, presentazioni e formazione", "Nella grande sala conferenze, anche con un pubblico numeroso."),
            uso("Networking ed eventi business", "Una sede nel cuore produttivo del Veneto."),
            nome="Cosa ci si fa")),
        tag="section", ancora="attivita", nome="Per chi è", interno=False)

    def gruppo(titolo, voci):
        return C("collegamento", H(titolo, "h3", "collegamento-titolo"),
                 T("<ul>" + "".join(f"<li>{v}</li>" for v in voci) + "</ul>", "collegamento-voci"), nome=titolo)

    ingressi = "".join(
        f'<li><a href="{html.escape(mappa(v))}" target="_blank" rel="noopener">{v}</a></li>' for v in INGRESSI)
    arrivare = C(
        "sezione arrivare",
        C("wrap",
          C("arrivare-testa",
            H("Come arrivare", "h2", "arrivare-titolo"),
            T("<p>Ad Albignasego, in una posizione strategica dal punto di vista logistico.</p>", "arrivare-testo"),
            BTN("Apri la mappa", MAPPA, "pulsante pulsante-filo", esterno=True, nome="Link a Google Maps"),
            nome="Titolo e mappa"),
          C("collegamenti",
            gruppo("A pochi minuti", ["Tangenziale di Padova", "Casello Padova Sud, A13 Bologna-Padova"]),
            gruppo("Servito direttamente", ["SS16 Adriatica"]),
            gruppo("Collegamenti rapidi", ["A4 Milano-Venezia", "Centro e stazione ferroviaria di Padova", "Aeroporto di Venezia"]),
            nome="Collegamenti"),
          C("ingressi",
            H("Tre ingressi", "h3", "collegamento-titolo"),
            T(f"<ul>{ingressi}</ul><p>{COMUNE}</p>", "ingressi-voci"),
            nome="Ingressi (ogni via apre Google Maps)")),
        tag="section", ancora="arrivare", nome="Come arrivare", interno=False)

    richiesta = C(
        "sezione richiesta",
        C("wrap",
          H(TEL, "p", "richiesta-telefono", url=f"tel:{TEL_LINK}", nome="Telefono grande"),
          C("richiesta-corpo",
            C("richiesta-testo",
              H("Richiesta di disponibilità", "h2", "richiesta-titolo"),
              T(f"<p>Il modulo prepara una mail per {EMAIL}, da inviare dal proprio programma di posta. Per una risposta a voce, il telefono.</p>"
                f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>', "richiesta-nota"),
              nome="Testo"),
            b.SC("[villaeidos_richiesta]", "richiesta-modulo", nome="Modulo (testi in parti/richiesta.html, email in config/richiesta.php)"))),
        tag="section", ancora="disponibilita", nome="Richiesta di disponibilità", interno=False)

    return [apertura, luogo, spazi, attivita, arrivare, richiesta]


# ------------------------------------------------------------------ pagine legali
# Testi scritti per questo sito, che non riceve dati: il modulo prepara una mail nel programma di posta di chi lo usa.
# I dati del titolare non li abbiamo: i segnaposto [DA COMPLETARE ...] restano finche' il cliente non li manda.

DA_COMPLETARE = '<mark class="da-completare">[DA COMPLETARE: {}]</mark>'


def legale(chiave):
    b = Costruttore(chiave)
    H, T = b.H, b.T
    dc = DA_COMPLETARE.format
    if chiave == "privacy":
        w = [
            H("Informativa privacy", "h1"),
            T("<p>Questa informativa spiega quali dati personali tratta il sito villaeidos.it e come. Le parti tra parentesi quadre vanno completate con i dati del titolare prima della pubblicazione.</p>", "avviso"),
            H("Titolare del trattamento", "h2"),
            T(f"<p>{dc('ragione sociale')}, {dc('sede legale')}, partita IVA {dc('numero')}. "
              f'Per ogni richiesta sui dati: <a href="mailto:{EMAIL}">{EMAIL}</a>, telefono <a href="tel:{TEL_LINK}">{TEL}</a>.</p>'),
            H("Quali dati", "h2"),
            T("<p><strong>Richiesta di disponibilità.</strong> Il modulo della pagina non invia niente al sito: prepara una mail nel programma di posta di chi lo compila. "
              f"I dati scritti (azienda, nome, email, telefono, tipo di spazio, data indicativa, numero di persone, messaggio) arrivano solo se la mail viene inviata, all'indirizzo {EMAIL}.</p>"
              "<p><strong>Dati di navigazione.</strong> Il server che ospita il sito registra, come ogni server web, l'indirizzo IP, la data e l'ora, la pagina richiesta e il tipo di browser (registri tecnici).</p>"),
            H("Perché e su quale base", "h2"),
            T("<ul><li>Rispondere a una richiesta di disponibilità e preparare un'eventuale offerta: misure precontrattuali chieste dall'interessato (art. 6, par. 1, lett. b del Regolamento UE 2016/679).</li>"
              "<li>Tenere il sito sicuro e funzionante: legittimo interesse del titolare (art. 6, par. 1, lett. f).</li></ul>"),
            H("Per quanto tempo", "h2"),
            T(f"<p>Le mail di richiesta si conservano per il tempo necessario a rispondere e a gestire gli eventuali rapporti che ne seguono. I registri tecnici per il tempo previsto dal fornitore dell'hosting: {dc('durata')}.</p>"),
            H("A chi arrivano", "h2"),
            T(f"<p>Ai fornitori dell'hosting e della posta elettronica, che trattano i dati per conto del titolare: {dc('nomi dei fornitori')}. I dati non vengono diffusi né venduti.</p>"),
            H("I diritti", "h2"),
            T(f'<p>Si possono chiedere in ogni momento l\'accesso ai propri dati, la rettifica, la cancellazione, la limitazione, l\'opposizione e la portabilità (articoli 15-22 del Regolamento), scrivendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. '
              'Si può anche proporre reclamo al Garante per la protezione dei dati personali (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>).</p>'),
            H("Cookie", "h2"),
            T('<p>Il sito non usa cookie di profilazione né di statistica: i dettagli sono nella pagina <a href="{{pagina:cookie}}">Cookie</a>.</p>'),
            T(f"<p>Ultimo aggiornamento: {dc('data di pubblicazione')}.</p>", "aggiornato"),
        ]
    else:
        w = [
            H("Cookie", "h1"),
            T("<p>Il sito villaeidos.it non usa cookie di profilazione, di statistica o di marketing, e non incorpora contenuti di altri siti (mappe, video, caratteri da server esterni). Per questo non mostra il banner dei cookie.</p>", "avviso"),
            H("Cookie tecnici", "h2"),
            T("<p>WordPress, il programma che fa funzionare il sito, usa cookie tecnici solo per chi entra nell'area riservata (gli amministratori). Chi visita le pagine non li riceve.</p>"),
            H("Link ad altri siti", "h2"),
            T("<p>I link alla mappa aprono Google Maps in una nuova scheda: da quel momento valgono le regole di Google (<a href=\"https://policies.google.com/privacy\" target=\"_blank\" rel=\"noopener\">policies.google.com</a>).</p>"),
            H("Se il sito cambia", "h2"),
            T('<p>Se un giorno si aggiungono statistiche, mappe incorporate o altri servizi di terzi, questa pagina e l\'<a href="{{pagina:privacy}}">informativa privacy</a> verranno aggiornate, e servirà il banner per il consenso.</p>'),
            T(f"<p>Ultimo aggiornamento: {dc('data di pubblicazione')}.</p>", "aggiornato"),
        ]
    return [b.C("legale", *w, tag="section", nome="Testo", interno=False)]


# ------------------------------------------------------------------ controlli

def testo_visibile(nodo):
    """Tutti i testi di un albero di Elementor (per il controllo con la fonte)."""
    out = []
    s = nodo.get("settings", {})
    for k in ("title", "editor", "text"):
        if k in s:
            out.append(s[k])
    for f in nodo.get("elements", []):
        out += testo_visibile(f)
    return out


def senza_tag(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).replace(NBSP, " ")
    return re.sub(r"\s+", " ", t).strip()


def frasi(t):
    """Un testo diviso in frasi (per il controllo): paragrafi e voci di elenco separati."""
    t = re.sub(r"</(p|li|h\d)>", "\n", t)
    return [x for x in (senza_tag(r) for r in t.split("\n")) if x]
