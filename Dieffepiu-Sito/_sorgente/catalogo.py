"""Sistemi, famiglie e macchine: le pagine costruite dai dati del catalogo generale 2023.

Dati in dati/estratto-sistemi-A.json e -B.json (linee e varianti, pagine stampate 12-226) e in
dati/macchine-grezzo.json (pagine 227-238). I valori sono copiati dalle schede "Dati Tecnici".
L'assegnazione delle linee alle sei famiglie del sito di oggi (in kit, a misura, carrarmato, plissé,
battente, componenti) e' nostra: va confermata con l'azienda (LEGGIMI).
"""
import json
import pathlib
import re

from comune import CATALOGO, IMMAGINI, briciole, e, richiesta

DATI = pathlib.Path(__file__).resolve().parent / "dati"


def _j(nome, vuoto):
    f = DATI / nome
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else vuoto


def _linee():
    out = {}
    for f in ("estratto-sistemi-A.json", "estratto-sistemi-B.json"):
        for L in _j(f, {"linee": []}).get("linee", []):
            out[L["linea"].upper().replace("®", "").strip()] = L
    return out


def _mm(v):
    v = v.replace("[mm]", "mm").replace("[", "").replace("]", "")
    return re.sub(r"\s+", " ", v).strip()


# ------------------------------------------------------------ le sei famiglie

FAMIGLIE = [
    {"slug": "kit", "titolo": "Sistema in kit",
     "linee": [("FLEXAL KIT", "flexal-kit"), ("KIT TRANSFORMER", "kit-transformer")],
     "attacco": "Due linee di zanzariere in kit, FLEXAL KIT e KIT TRANSFORMER: verticali, a catena, laterali, laterali doppie e frontali, con tutti i componenti a catalogo.",
     "seo": "FLEXAL KIT e KIT TRANSFORMER: zanzariere in kit verticali, a catena, laterali e frontali, con misure massime e codici dal catalogo."},
    {"slug": "a-misura", "titolo": "Sistema a misura",
     "linee": [("FLEXAL DIM", "flexal-dim"), ("FLEXAL PLATINUM", "flexal-platinum"), ("ROLLY STYLE - 1", "rolly-style-1"),
               ("ROLLY STYLE - WOOD", "rolly-style-wood"), ("ROLLY STYLE - 3", "rolly-style-3"), ("CIVIKA", "civika")],
     "attacco": "Sei linee di profili in alluminio e accessori per le zanzariere a misura: verticali, a catena, laterali, laterali doppie e con guida bassa.",
     "seo": "FLEXAL DIM, FLEXAL PLATINUM, ROLLY STYLE 1, WOOD e 3, CIVIKA 50: sistemi per zanzariere a misura con misure massime, cassonetti e codici."},
    {"slug": "carrarmato", "titolo": "Sistema carrarmato",
     "linee": [("TANK", "tank")],
     "attacco": "TANK® è il sistema laterale con il cingolo: due versioni, TANK® laterale e TANK REVOLUTION®.",
     "seo": "TANK e TANK REVOLUTION: il sistema carrarmato di Dieffepiu per zanzariere laterali, con misure, profili e codici dal catalogo."},
    {"slug": "plisse", "titolo": "Sistema plissé",
     "linee": [("PLIXI", "plixi")],
     "attacco": "PLIXI® è il sistema con la rete plissettata: laterale, laterale doppia, reverse e verticale.",
     "seo": "PLIXI, il sistema plissé di Dieffepiu: zanzariere con rete plissettata laterali, doppie, reverse e verticali, misure e codici."},
    {"slug": "battente", "titolo": "Sistema battente",
     "linee": [("AMERIKA 35", "amerika-35"), ("SCHERMI FISSI ED APRIBILI", "schermi")],
     "attacco": "La zanzariera ad anta AMERIKA 35 e gli schermi fissi ed apribili, con profili, squadrette e cerniere a catalogo.",
     "seo": "AMERIKA 35 a battente e schermi fissi ed apribili per zanzariere: misure massime, profili e accessori dal catalogo Dieffepiu."},
]

NOMI = {"FLEXAL KIT": "FLEXAL KIT", "KIT TRANSFORMER": "KIT TRANSFORMER", "FLEXAL DIM": "FLEXAL DIM",
        "FLEXAL PLATINUM": "FLEXAL PLATINUM", "ROLLY STYLE - 1": "ROLLY STYLE 1", "ROLLY STYLE - WOOD": "ROLLY STYLE WOOD",
        "ROLLY STYLE - 3": "ROLLY STYLE 3", "CIVIKA": "CIVIKA 50", "TANK": "TANK®", "PLIXI": "PLIXI®",
        "AMERIKA 35": "AMERIKA 35", "SCHERMI FISSI ED APRIBILI": "Schermi fissi ed apribili"}

COMPONENTI = {"slug": "componenti", "titolo": "Componenti universali",
              "attacco": "Rallentatori, molle, catenelle, fettucce, reti e accessori che servono a più linee: per i sistemi in kit, per quelli a misura e per tutti i sistemi.",
              "seo": "Componenti universali per zanzariere: rallentatori viscodinamici FX135 e FX157, molle, catenelle, fettucce, reti in fibra di vetro, alluminio e inox."}


def famiglie():
    out = []
    for f in FAMIGLIE + [COMPONENTI]:
        out.append({"slug": f["slug"], "titolo": f["titolo"], "descrizione_seo": f["seo"], "dati": f})
    return out


def _pagine_linea(L):
    p = [v["pagina_stampata"] for v in L.get("varianti", []) if v.get("pagina_stampata")]
    return (min(p), max(p)) if p else (None, None)


def _colonne(varianti):
    pref = ["Altezza massima", "Larghezza massima", "Cassonetto", "Ingombro min", "Ingombro minimo", "Tubo rete"]
    viste = []
    for v in varianti:
        for voce, _ in v.get("dati", []):
            if voce not in viste:
                viste.append(voce)
    ordinate = [x for x in pref if x in viste] + [x for x in viste if x not in pref]
    return ordinate[:5]


def _breve(voce):
    return {"Altezza massima": "Altezza max", "Larghezza massima": "Larghezza max", "Ingombro min": "Ingombro min.",
            "Ingombro minimo": "Ingombro min."}.get(voce, voce)


def _nome_variante(v, linea):
    n = v.get("variante") or ""
    if not n:
        n = v.get("nome_completo", linea)
    return n.split(" - ")[0].strip() or n


def tabella_varianti(L):
    vs = [v for v in L.get("varianti", []) if v.get("dati")]
    cols = _colonne(vs)
    th = "".join(f'<th scope="col" class="n">{_breve(c)}</th>' for c in cols)
    righe = []
    for v in vs:
        d = dict(v.get("dati", []))
        nome = _nome_variante(v, L["linea"])
        celle = "".join(f'<td class="n" data-l="{_breve(c)}">{_mm(d[c]) if c in d else ""}</td>' for c in cols)
        righe.append(f'<tr><td class="v">{e(nome)}</td>{celle}<td class="n" data-l="Catalogo">p.&nbsp;{v.get("pagina_stampata", "")}</td></tr>')
    return (f'<table class="tabella num"><thead><tr><th scope="col">Variante</th>{th}<th scope="col" class="n">Catalogo</th></tr></thead>'
            f'<tbody>{"".join(righe)}</tbody></table>')


def _codici(L, quanti=10):
    visti = []
    for v in L.get("varianti", []):
        for c in v.get("codici_principali", []):
            k = c[0]
            if k and k not in visti:
                visti.append(k)
    return visti[:quanti]


def _riga_linea(L):
    vs = [v for v in L.get("varianti", []) if v.get("dati")]
    n = len(vs)
    h = [int(re.sub(r"\D", "", dict(v.get("dati", [])).get("Altezza massima", "0")) or 0) for v in vs]
    l = [int(re.sub(r"\D", "", dict(v.get("dati", [])).get("Larghezza massima", "0")) or 0) for v in vs]
    nomi = [_nome_variante(v, L["linea"]).lower() for v in vs]
    pezzi = []
    if n > 1:
        pezzi.append(f"<b>{n} varianti</b>: " + ", ".join(nomi) + ".")
    if h and max(h):
        def f(x):
            return f"{x:,}".replace(",", ".")
        pezzi.append(f"Fino a {f(max(h))} mm di altezza e {f(max(l))} mm di larghezza.")
    return " ".join(pezzi)


# una o due frasi per linea, dai testi del catalogo (pagine indicate)
TESTI = {
    "FLEXAL KIT": "Kit preconfigurati per il montaggio: cassonetto completo di tubo con rete e guide laterali con spazzolino. Si ordinano da 15 pezzi o multipli, a richiesta anche tagliati a misura; l’alluminio nel RAL indicato, di serie bianco RAL 9010 (pp. 43-45).",
    "KIT TRANSFORMER": "Kit preconfigurati da 15 pezzi o multipli, a richiesta tagliati a misura. Con la maniglia per la doppia anta la versione doppia laterale copre larghezze fino a 3 metri, e lo stesso sistema fa anche la laterale a un’anta senza cambiare accessori (p. 62).",
    "PLIXI": "Tre modi di comprarlo: componenti sciolti, per chi ha le macchine per lavorarli; kit rete preconfigurati, riducibili fino a 30 cm; kit su misura del foro luce. Il tappo inferiore nuovo ha una rotella che riduce gli attriti, e la barra maniglia DFPX007 pesa il 14% in meno della DFPX003 (p. 71).",
    "TANK": "TANK® 2.0 usa il sistema Bi-Convex di Dieffepiu, fornito già assemblato e pronto all’uso. Si fa a misura o in kit riducibile; con i profili magnetici su cassonetto, barra maniglia e riscontri a muro la zanzariera si toglie e si rimette in fretta e si può cambiare il senso di apertura. Per la versione doppia basta un secondo kit nel lato libero del riscontro (p. 90).",
    "FLEXAL DIM": "Due cassonetti, DIM 40 e DIM 50: cambiano solo contropiastre e testate, il resto degli accessori è lo stesso.",
    "FLEXAL PLATINUM": "Cassonetto da 50 mm, tubo rete da 26 mm e rallentatore FX157.",
}


def tabella_profili(L):
    pa = L.get("profili_alluminio")
    if not pa:
        return ""
    if isinstance(pa, dict):
        pa = [pa]
    out = []
    for p in pa:
        righe = "".join(
            f'<tr><td class="v">{e(r[0])}</td><td data-l="Profilo">{e(r[1])}</td><td class="n" data-l="Peso">{e(r[3].replace("g/mt", "g/m"))}</td>'
            f'<td class="n" data-l="Misura">{e(r[5].split(" (")[0])}</td></tr>' for r in p["righe"][:8])
        tit = "Profili in alluminio EN-AW 6060 T5"
        if len(pa) > 1:
            tit += ", " + ("TANK® 2.0" if "2.0" in p["titolo"] else "TANK REVOLUTION®")
        out.append(f'<table class="tabella num profili"><caption>{tit} (catalogo, p.&nbsp;{p["pagina_stampata"]})</caption>'
                   f'<thead><tr><th scope="col">Codice</th><th scope="col">Profilo</th><th scope="col" class="n">Peso</th><th scope="col" class="n">Misura</th></tr></thead>'
                   f'<tbody>{righe}</tbody></table>')
    return "".join(out)


def _tavola_fig(c, chiave, alt, dida, larg=None):
    if chiave not in IMMAGINI:
        return ""
    return f'''<figure class="tavola-p">
        <div class="foglio">{c.tavola(chiave, alt, larghezza_max=larg)}</div>
        <figcaption class="num">{dida}</figcaption>
      </figure>'''


def _chiave(n):
    return n.upper().replace("®", "").strip()


def sezione_linea(c, nome_l, chiave, L, prima=False):
    nome = NOMI.get(nome_l, nome_l)
    p1, p2 = _pagine_linea(L)
    pag = f"p.&nbsp;{p1}" + (f"-{p2}" if p2 and p2 != p1 else "")
    es = chiave + "-esploso"
    fig = _tavola_fig(c, es, f"Tavola esplosa {nome} dal catalogo, con i codici dei componenti",
                      f"<b>Tavola esplosa</b><span>catalogo 2023, {pag}</span>")
    cod = _codici(L)
    codici = f'<p class="codici num"><b>Codici nella tavola</b> {", ".join(cod)}</p>' if cod else ""
    nota = ""
    for v in L.get("varianti", []):
        for n in v.get("note_verbatim", []):
            if "Rallentatore viscodinamico" in n and not nota:
                ver = re.findall(r"(\w+) (HD|MD)(?: Colore:)? ([A-Za-z]+)", n)
                if ver:
                    cod = ver[0][0]
                    alt = " o ".join(f"{t} {col.lower()}" for _, t, col in ver)
                    nota = f'<p class="nota-linea num">Tra gli accessori: rallentatore viscodinamico {cod}, {alt}.</p>'
    cl = "griglia corpo-linea" + ("" if fig else " senza-tavola")
    ida = "l-" + chiave
    return f'''<section class="wrap linea" id="{chiave}" aria-labelledby="{ida}">
  <h2 id="{ida}">{nome.replace("®", '<span class="reg">®</span>')}</h2>
  <p class="riga num">{_riga_linea(L)}</p>
  {('<p class="nota-linea testo-l num">' + TESTI[_chiave(nome_l)] + '</p>') if _chiave(nome_l) in TESTI else ""}
  <div class="{cl}">
    <div class="tab">
      {tabella_varianti(L)}
      {nota}
      {codici}
      {tabella_profili(L)}
    </div>
    <div class="esploso">
      {fig}
    </div>
  </div>
</section>'''


def _apertura(c, f, destra, azioni=""):
    att = f'\n      <p class="attacco">{f["attacco"]}</p>'
    return f'''<section class="wrap testa-pagina" aria-labelledby="titolo">
  {briciole(c, [("sistemi", "Sistemi"), ("", f["titolo"])])}
  <h1 class="titolo-pagina" id="titolo">{f["titolo"]}</h1>
  <div class="griglia apri-pagina">
    <div class="testo">{att}{azioni}
    </div>
    <div class="tavola-p">{destra}</div>
  </div>
</section>'''


def _altre(c, attuale):
    righe = []
    for f in FAMIGLIE + [COMPONENTI]:
        if f["slug"] == attuale:
            continue
        righe.append(f'<a class="famiglia" href="{c.link("sistemi/" + f["slug"])}"><span class="nome">{f["titolo"]}</span>'
                     f'<span class="cosa">{_cosa_famiglia(f)}</span><span class="freccia">Apri</span></a>')
    return f'''<section class="wrap blocco" aria-labelledby="t-altre">
  <h2 id="t-altre">Le altre famiglie</h2>
  <div class="righe">
    {"".join(righe)}
  </div>
</section>'''


def _cosa_famiglia(f):
    if f["slug"] == "componenti":
        return "Rallentatori FX135 e FX157, molle, catenelle, fettucce, reti e <b>espositore</b>."
    return ", ".join(f"<b>{NOMI.get(n, n)}</b>" for n, _ in f["linee"]) + "."


def famiglia(c, f):
    d = f["dati"]
    if d["slug"] == "componenti":
        return componenti(c, d)
    linee = _linee()
    sezioni = []
    primo = d["linee"][0]
    L0 = linee.get(primo[0], {"varianti": []})
    p1, _ = _pagine_linea(L0)
    ritratti = []
    for n, k in d["linee"]:
        if k in IMMAGINI:
            q, _ = _pagine_linea(linee.get(n, {}))
            ritratti.append(f'<figure><div class="foglio">{c.tavola(k, NOMI.get(n, n) + ", disegno del catalogo", lazy=False, larghezza_max=IMMAGINI[k]["w"])}</div>'
                            f'<figcaption class="num"><b>{NOMI.get(n, n)}</b>{(" p.&nbsp;" + str(q)) if q else ""}</figcaption></figure>')
    img = f'''
      <div class="ritratti r{len(ritratti)}">{"".join(ritratti)}</div>''' if ritratti else ""
    if d["slug"] == "carrarmato" and "kit-tank" in IMMAGINI:
        img = f'''
      {c.foto("kit-tank", "Il kit TANK su fondo chiaro: cingolo nero arrotolato, guide e terminali", sizes="(max-width:960px) 100vw, 55vw", lazy=False)}
      <figcaption class="num"><b>Kit TANK®</b><span>cingolo, terminali e guide</span></figcaption>'''
    if d["slug"] == "plisse" and "plisse-macro" in IMMAGINI:
        img = f'''
      {c.foto("plisse-macro", "Rete plissettata grigia in primo piano", sizes="(max-width:960px) 100vw, 624px", lazy=False)}
      <figcaption class="num"><b>Rete plissettata</b><span>PLIXI®</span></figcaption>'''
    pagine = [x for n, _ in d["linee"] for x in _pagine_linea(linee.get(n, {})) if x]
    azioni = ""
    if pagine:
        azioni = f'''
      <div class="azioni">
        <a class="bottone" href="{c.link('contatti')}">Chiedete listino e schede</a>
        <a class="link-cat" href="{CATALOGO}">Catalogo PDF, pagine {min(pagine)}-{max(pagine)}</a>
      </div>'''
    sezioni.append(_apertura(c, d, img, azioni))
    for nome_l, chiave in d["linee"]:
        L = linee.get(nome_l)
        if L:
            sezioni.append(sezione_linea(c, nome_l, chiave, L))
    sezioni.append(_altre(c, d["slug"]))
    sezioni.append(richiesta(c))
    return sezioni


# ------------------------------------------------------------ componenti

GRUPPI_COMP = [
    ("Rallentatori viscodinamici", ["FX135 HD", "FX135 MD", "FX157 HD", "FX157 MD", "MX135 HD", "MX135 MD", "FX158", "FX137"]),
    ("Molle e tappi", ["FX120", "FX121", "FX122", "FX141", "CR1110", "CR1109", "CR1109M", "FX119R", "CR1112R"]),
    ("Catenelle e giunti", ["CR1134", "CR1147", "CR1147S", "CR1162", "CR1193", "CR1192", "CR1194", "CR1191", "CR1188"]),
    ("Spazzolini, nappine e bottoni", ["FX129", "CR1130", "FX113", "CR2322", "CR1118", "CR1143BN", "CR3227", "CR1119", "CR1119S", "CR1120", "CR1120S"]),
    ("Guide, maniglie e bloccaggi", ["CR1151", "FX147", "FX161", "FX109", "FX134", "FX136", "FX159", "AK109", "AK109A", "CR1113", "CR1114", "CR1150", "CR1150S"]),
    ("Fettucce, tondini e biadesivi", ["CR1124", "CR1123", "CR2223", "CR2223NR", "CR1128", "CR1126T", "CR1129", "CR1142", "CR1133", "CR1133/PS"]),
    ("Reti", ["RFV101", "RFV121", "RFV141", "RFV161", "RFV201", "RFV261", "RAL080", "RAL100", "RAL120", "RAC080", "RAC100", "RAC120", "RE03G", "RE024NR", "RE043N"]),
]


def componenti(c, d):
    B = _j("estratto-sistemi-B.json", {})
    comp = B.get("componenti", {})
    nomi, dove = {}, {}
    for s in comp.get("sezioni", []):
        for cod, nome in s.get("articoli", []):
            nomi.setdefault(cod, nome)
            dove.setdefault(cod, []).append(s["titolo"].split(" - ")[0])
    # i rallentatori sono elencati in tutte e due le sezioni (p. 199: "stessi rallentatori della sezione KIT")
    for k in ("FX135 HD", "FX135 MD", "FX157 HD", "FX157 MD", "MX135 HD", "MX135 MD", "FX158"):
        if k in dove and "Sistemi a MISURA" not in dove[k]:
            dove[k].append("Sistemi a MISURA")
    img = ""
    if "componenti-foto" in IMMAGINI:
        img = f'''
      <div class="foglio">{c.tavola("componenti-foto", "Rallentatori viscodinamici FX135, FX157 e MX135, disegni del catalogo", lazy=False, larghezza_max=620)}</div>
      <figcaption class="num"><b>Rallentatori viscodinamici</b><span>catalogo 2023, p.&nbsp;191</span></figcaption>'''
    azioni = f'''
      <div class="azioni">
        <a class="bottone" href="{c.link('contatti')}">Chiedete listino e schede</a>
        <a class="link-cat" href="{CATALOGO}">Catalogo PDF, pagine 191-215</a>
      </div>'''
    sez = [_apertura(c, d, img, azioni)]
    # il rallentatore: le quattro frasi del catalogo (p. 192)
    sez.append(f'''<section class="wrap blocco" aria-labelledby="t-freno">
  <div class="griglia">
    <div class="colonna">
      <h2 id="t-freno">Il rallentatore viscodinamico</h2>
      <p class="grande">Agisce solo durante il riavvolgimento del telo: il telo si riavvolge con dolcezza e senza essere accompagnato.</p>
      <p>In chiusura la forza per accompagnare il telo non cambia. Gli sbalzi di temperatura non lo danneggiano, e la molla di richiamo e il telaio non subiscono stress meccanico: le schermature durano di più. Aumenta il grado di sicurezza dei sistemi e ne favorisce la messa a norma.</p>
    </div>
    <div class="lato">
      {_tavola_fig(c, "componenti", "Spaccato del rallentatore viscodinamico", "<b>Spaccato</b><span>arpionismo unidirezionale, rotore alettato, olio siliconico</span>", larg=394)}
    </div>
  </div>
</section>''')
    for titolo, codici in GRUPPI_COMP:
        righe = []
        for k in codici:
            if k not in nomi:
                continue
            per = " e ".join(dict.fromkeys(x.replace("Sistemi in KIT", "in kit").replace("Sistemi a MISURA", "a misura").replace("Tutti i sistemi", "tutti i sistemi") for x in dove[k]))
            righe.append(f'<tr><td class="v">{e(k)}</td><td data-l="Articolo">{e(nomi[k])}</td><td class="n" data-l="Sistemi">{per}</td></tr>')
        if not righe:
            continue
        idg = "g-" + re.sub(r"[^a-z]+", "-", titolo.lower()).strip("-")
        sez.append(f'''<section class="wrap linea" aria-labelledby="{idg}">
  <h2 id="{idg}">{titolo}</h2>
  <div class="griglia corpo-linea senza-tavola">
    <div class="tab">
      <table class="tabella num"><thead><tr><th scope="col">Codice</th><th scope="col">Articolo</th><th scope="col" class="n">Sistemi</th></tr></thead>
      <tbody>{"".join(righe)}</tbody></table>
    </div>
  </div>
</section>''')
    # espositore
    L = _linee().get("ESPOSITORE PER ZANZARIERE")
    if L:
        v = L["varianti"][0]
        dd = dict(v["dati"])
        sez.append(f'''<section class="wrap linea" id="espositore" aria-labelledby="l-espositore">
  <h2 id="l-espositore">Espositore per zanzariere</h2>
  <p class="riga num">Per mostrare i sistemi in negozio o in showroom: fino a {_mm(dd.get("Altezza massima", ""))} × {_mm(dd.get("Larghezza massima", ""))}, profili E001 e E002 in alluminio EN-AW 6060 T5. Ordine minimo di 20 profili per tipo.</p>
  <div class="griglia corpo-linea">
    <div class="tab"><p class="codici num"><b>Codici</b> E001, E002, E003, E004, E005, E006 (catalogo 2023, p.&nbsp;{v["pagina_stampata"]})</p></div>
    <div class="esploso">{_tavola_fig(c, "espositore", "Espositore per zanzariere, disegno del catalogo", f"<b>Espositore</b><span>catalogo 2023, p.&nbsp;{v['pagina_stampata']}</span>")}</div>
  </div>
</section>''')
    sez.append(_altre(c, "componenti"))
    sez.append(richiesta(c))
    return sez


# ------------------------------------------------------------ indice dei sistemi

def sistemi(c):
    linee = _linee()
    s1 = f'''<section class="wrap testa-pagina" aria-labelledby="titolo">
  {briciole(c, [("sistemi", "Sistemi")])}
  <h1 class="titolo-pagina" id="titolo">Sistemi per zanzariere</h1>
  <div class="griglia apri-pagina solo-testo">
    <div class="testo">
      <p class="attacco">Quattordici linee a catalogo, in sei famiglie: profili in alluminio, componenti e kit per chi produce, assembla e installa zanzariere.</p>
      <div class="azioni">
        <a class="link-cat" href="{CATALOGO}">Catalogo generale PDF, 76&nbsp;MB</a>
      </div>
    </div>
  </div>
  <div class="famiglie">
'''
    righe = []
    for f in FAMIGLIE + [COMPONENTI]:
        righe.append(f'    <a class="famiglia" href="{c.link("sistemi/" + f["slug"])}"><span class="nome">{f["titolo"]}</span>'
                     f'<span class="cosa">{_cosa_famiglia(f)}</span><span class="freccia">Apri</span></a>')
    s1 += "\n".join(righe) + "\n  </div>\n</section>"
    s2 = f'''<section class="wrap blocco" aria-labelledby="t-colori">
  <div class="griglia">
    <div class="colonna">
      <h2 id="t-colori">Colori degli accessori</h2>
      <p class="num">Gli accessori escono neri. Da 1.000 pezzi per tipo anche bronzo, grigio, RAL&nbsp;1013, RAL&nbsp;9010 e RAL&nbsp;8017, con il 20% in più sul listino.</p>
      <p>I profili sono in alluminio EN-AW 6060 T5, grezzi o verniciati.</p>
    </div>
  </div>
</section>'''
    return [s1, s2, richiesta(c)]


# ------------------------------------------------------------ macchine

GRUPPI_M = [
    ("saldatrici", "Saldatrici per fettuccia", ["ATT001-B", "ATT035-3BF", "ATT035-3BM"]),
    ("banchi", "Banchi di taglio e saldatura", ["ATT007", "ATT030"]),
    ("tubi-rete", "Tubi rete da 6 metri", ["ATT012", "ATT015"]),
    ("bottonatrice", "Bottonatrice e rivettatrice", ["ATT009", "ATT010"]),
    ("presse", "Presse pneumatiche", ["ATT006", "ATT008", "ATT011"]),
    ("kit-banco", "Kit pneumatico per il banco", [""]),
]
NOME_M = {"ATT001-B": "Saldatrice manuale Basic", "ATT035-3BF": "Saldatrice pneumatica per fettuccia",
          "ATT035-3BM": "Saldatrice elettropneumatica per fettuccia", "ATT007": "Banco elettronico di taglio e saldatura della rete",
          "ATT030": "Banco elettronico per sistemi a misura e in kit", "ATT012": "Banco automatico per tubi rete da 6 m",
          "ATT015": "Saldatrice automatica per tubi rete da 6 m", "ATT009": "Bottonatrice pneumatica",
          "ATT010": "Rivettatrice pneumatica", "ATT006": "Pressa per il foro della nappina",
          "ATT008": "Pressa per il foro squadretta, anta AMERIKA", "ATT011": "Pressa per il foro squadretta, telaio AMERIKA",
          "": "Kit pneumatico per autocostruzione del banco taglio rete"}
# descrizioni: quelle del catalogo; dove il catalogo ha un testo sbagliato o doppio, solo la scheda (vedi LEGGIMI)
DESCR = {
    "ATT001-B": [0, 1, 2, 3],
    "ATT035-3BF": [0, 1, 4],
    "ATT035-3BM": [0, 1, 2],
    "ATT007": [1, 2, 4, 7],
    "ATT030": [4, 8],
    "ATT012": [],
    "ATT015": [],
    "ATT009": [0],
    "ATT010": [],
    "ATT006": [0],
    "ATT008": [],
    "ATT011": [],
    "": [0],
}
EXTRA = {
    "ATT030": "Stessa costruzione e stessa plancia di comando del banco ATT007, con il piano lungo 8,2 metri.",
    "ATT012": "Banco automatico per la produzione dei tubi rete lunghi 6 metri.",
    "": "Kit pneumatico preassemblato, completo di disegni tecnici, per costruire da sé il banco di taglio della rete.",
}


def _macchine():
    return {m["codice"]: m for m in _j("macchine-grezzo.json", [])}


def macchine_piede():
    return [(a, n) for a, n, _ in GRUPPI_M]


def _scheda_m(c, m):
    cod = m["codice"]
    nome = NOME_M.get(cod, m["nome"])
    idm = "m-" + (cod.lower() or "kit")
    par = [m["descrizione"][i] for i in DESCR.get(cod, []) if i < len(m["descrizione"])]
    par = [p.replace(" [mm]", " mm").replace(" [mt]", " m").replace("[", "").replace("]", "") for p in par]
    if cod in EXTRA:
        par = ([EXTRA[cod]] if cod != "ATT030" else par[:1] + [EXTRA[cod]] + par[1:])
        if cod == "":
            par = [EXTRA[cod]]
    descr = "".join(f"<p>{e(p)}</p>" for p in par)
    timbro = '<p class="timbro">Brevetto depositato</p>' if cod == "ATT015" else ""
    immagine = m.get("immagine") or ""
    if cod == "":
        immagine = "m-kit-pneumatico-banco"
    fig = ""
    if immagine in IMMAGINI:
        fig = f'''<figure class="tavola-p">
      <div class="foglio">{c.tavola(immagine, nome + ", disegno del catalogo")}</div>
      <figcaption class="num"><b>{cod or "Kit"}</b><span>catalogo 2023, p.&nbsp;{m["pagina"]}</span></figcaption>
    </figure>'''
    dati = ""
    if m["dati"]:
        righe = "".join(f'<tr><td data-l="">{e(v)}</td><td class="n">{e(x)}</td></tr>' for v, x in m["dati"])
        dati = (f'<div class="dt"><table class="tabella num due-col"><caption>Dati tecnici</caption>'
                f'<thead><tr><th scope="col">Voce</th><th scope="col" class="n">Valore</th></tr></thead><tbody>{righe}</tbody></table></div>')
    ric = ""
    if m.get("ricambi"):
        righe = "".join(f'<tr><td class="v">{e(k)}</td><td data-l="">{e(n)}</td></tr>' for k, n in m["ricambi"])
        ric = (f'<div class="ric"><table class="tabella num due-col"><caption>Ricambi</caption>'
               f'<thead><tr><th scope="col">Codice</th><th scope="col">Ricambio</th></tr></thead><tbody>{righe}</tbody></table></div>')
    tab = f'<div class="tabelle">{dati}{ric}</div>' if (dati or ric) else ""
    return f'''<article class="griglia macchina-p" id="{idm}" aria-labelledby="{idm}-t">
    <div class="intesta">
      <h3 id="{idm}-t">{e(nome)}</h3>
      <p class="codice num">{cod or "Senza codice a catalogo"}</p>
      <div class="descr">{descr}</div>
      {timbro}
    </div>
    <div class="figura">{fig}</div>
    {tab}
  </article>'''


def macchine(c):
    M = _macchine()
    s1 = f'''<section class="wrap testa-pagina" aria-labelledby="titolo">
  {briciole(c, [("macchine", "Macchine")])}
  <h1 class="titolo-pagina" id="titolo">Macchine per zanzariere</h1>
  <div class="griglia apri-pagina solo-testo">
    <div class="testo">
      <p class="attacco">Dodici macchine e un kit per lavorare la rete: saldatrici per la fettuccia, banchi elettronici che tagliano e saldano fino a 8,2&nbsp;metri, tubi rete da 6&nbsp;metri, bottonatrici e presse.</p>
      <div class="azioni">
        <a class="bottone" href="{c.link('contatti')}">Chiedete un preventivo</a>
        <a class="link-cat" href="{CATALOGO}">Catalogo PDF, pagine 227-238</a>
      </div>
    </div>
  </div>
  <div class="griglia indice-m">
'''
    for a, titolo, codici in GRUPPI_M:
        voci = "".join(f'<li><a href="#m-{(k.lower() or "kit")}">{e(NOME_M.get(k, ""))}<span>{k or "kit"}</span></a></li>' for k in codici if k in M)
        s1 += f'    <section aria-label="{titolo}"><h2>{titolo}</h2><ul>{voci}</ul></section>\n'
    s1 += "  </div>\n</section>"
    sez = [s1]
    for a, titolo, codici in GRUPPI_M:
        schede = "\n  ".join(_scheda_m(c, M[k]) for k in codici if k in M)
        sez.append(f'''<section class="wrap gruppo" id="{a}" aria-labelledby="g-{a}">
  <h2 id="g-{a}">{titolo}</h2>
  {schede}
</section>''')
    sez.append(richiesta(c, "Preventivi e ricambi",
                         "Per una macchina nuova, per i ricambi o per un impianto di produzione completo, diteci che cosa producete e quanti pezzi vi servono."))
    return sez
