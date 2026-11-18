"""Le pagine del sito. Ogni pagina restituisce una lista di sezioni HTML (in WordPress: un blocco HTML ciascuna).

Fatti e testi vengono da 01-analisi.md, dal sito di oggi e dal catalogo generale 2023 (dati/*.json, con le
pagine stampate). Niente dati inventati: dove il catalogo non dice una cosa, la pagina non la dice.
"""
import json
import pathlib

import moduli
from comune import (CATALOGO, MAIL, MAPPA, TEL, TEL_HREF, briciole, e, richiesta)

DATI = pathlib.Path(__file__).resolve().parent / "dati"


def _json(nome, vuoto):
    f = DATI / nome
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else vuoto


def testa(c, titolo, voci, attacco, destra="", azioni="", id_="titolo"):
    """Apertura di una pagina interna: briciole, titolo grande, attacco a sinistra e (se c'e') un'immagine a destra."""
    cl = "griglia apri-pagina" + ("" if destra else " solo-testo")
    att = "".join(f'\n      <p class="attacco">{a}</p>' for a in (attacco if isinstance(attacco, list) else [attacco]))
    return f'''<section class="wrap testa-pagina" aria-labelledby="{id_}">
  {briciole(c, voci)}
  <h1 class="titolo-pagina" id="{id_}">{titolo}</h1>
  <div class="{cl}">
    <div class="testo">{att}{azioni}
    </div>{destra}
  </div>
</section>'''


def riga_link(c, dove, nome, cosa, freccia="Apri"):
    return (f'<a class="famiglia" href="{dove}"><span class="nome">{nome}</span>'
            f'<span class="cosa">{cosa}</span><span class="freccia">{freccia}</span></a>')


# ---------------------------------------------------------------- azienda

def azienda(c):
    destra = f'''
    <figure class="tavola-p foto-p">
      {c.foto("rotoli", "Rotoli di fettuccia grigia impilati in magazzino", sizes="(max-width:960px) 100vw, 50vw", lazy=False)}
      <figcaption>Fettuccia in magazzino, via Lombardia.</figcaption>
    </figure>'''
    s1 = testa(c, "La nostra azienda", [("azienda", "Azienda")],
               ["Progettiamo e produciamo sistemi e macchinari per zanzariere di ogni tipo. Con i nostri tecnici realizziamo anche progetti su misura per i clienti.",
                "Lavoriamo per chi le zanzariere le fa: produttori, assemblatori e installatori, in Italia e all’estero."],
               destra=destra)
    s2 = f'''<section class="wrap blocco" aria-labelledby="t-storia">
  <h2 id="t-storia">Da Di Franco a Dieffepiu</h2>
  <div class="griglia">
    <div class="colonna num">
      <p class="grande">Siamo sul mercato italiano e internazionale dei sistemi per zanzariere dal 1987 e abbiamo progettato e realizzato oltre 2.000 impianti di produzione.</p>
      <p>Dieffepiu nasce dalla scissione dell’originaria Di Franco, diventata Di Franco Holding. Unica proprietà e unica gestione, per offrire un servizio competente, attento alle esigenze del mercato, all’innovazione e alla tecnologia.</p>
      <p>Siamo in via Lombardia 33, nella zona industriale di Villatora a Saonara, in provincia di Padova.</p>
    </div>
    <div class="lato">
      <div class="scheda num">
        <b>Dieffepiu S.r.l.</b><span class="mat">Saonara (PD)</span>
        <dl>
          <dt>Dal</dt><dd>1987</dd>
          <dt>Impianti realizzati</dt><dd>oltre 2.000</dd>
          <dt>Linee a catalogo</dt><dd>14</dd>
          <dt>Macchine a catalogo</dt><dd>12</dd>
          <dt>Catalogo</dt><dd>IT, EN</dd>
        </dl>
      </div>
    </div>
  </div>
</section>'''
    s3 = f'''<section class="wrap blocco" aria-labelledby="t-cosa">
  <h2 id="t-cosa">Che cosa facciamo</h2>
  <div class="righe">
    {riga_link(c, c.link("sistemi"), "Sistemi", "Profili in alluminio, componenti e kit: quattordici linee in sei famiglie, dal kit verticale al plissé e al battente.", "Le linee")}
    {riga_link(c, c.link("macchine"), "Macchine", "Saldatrici per la fettuccia, banchi elettronici che tagliano e saldano la rete fino a 8,2&nbsp;metri, bottonatrici e presse pneumatiche.", "Le macchine")}
    {riga_link(c, c.link("sistemi/componenti"), "Componenti universali", "Molle, testate, terminali e accessori a catalogo, per i sistemi in kit, a misura e per tutti i sistemi.", "I componenti")}
  </div>
</section>'''
    s4 = f'''<section class="wrap blocco" aria-labelledby="t-brevetti">
  <div class="griglia">
    <div class="colonna">
      <h2 id="t-brevetti">Marchio e brevetti</h2>
      <p>Il marchio DIEFFE+ è registrato e depositato. Gran parte dei sistemi per zanzariere e delle macchine del catalogo è coperta da brevetti e da modelli di utilità.</p>
      <p>Il catalogo, i disegni e le schede sono del nostro ufficio tecnico: i dati tecnici di accessori e macchine possono cambiare senza preavviso, per migliorarli.</p>
    </div>
    <div class="lato">
      <h2 class="sr">Fiere</h2>
      <p class="num">Ci trovate a MADE expo a Milano e a BATIMAT a Parigi: cinque fiere dal 2021 a oggi.</p>
      <p class="vai"><a href="{c.link("news")}">Fiere e novità</a></p>
    </div>
  </div>
</section>'''
    s5 = f'''<section class="wrap blocco" aria-labelledby="t-dove">
  <div class="griglia">
    <div class="colonna">
      <h2 id="t-dove">Dove siamo</h2>
      <div class="recapiti">
        <p>Via Lombardia 33, 35020 Saonara (PD)<br>Zona industriale di Villatora<br>
        <a class="nw" href="{MAPPA}">Apri la mappa</a></p>
        <p class="orari num">Dal lunedì al giovedì <span class="nw">8:30-12:30</span> e <span class="nw">13:30-17:30</span><br>Venerdì <span class="nw">8:30-12:30</span> e <span class="nw">13:00-17:00</span></p>
      </div>
    </div>
  </div>
</section>'''
    return [s1, s2, s3, s4, s5, richiesta(c, "Un impianto nuovo?", "Per parlare di una linea di produzione, di una macchina o di un progetto su misura, chiamateci o prendete appuntamento in via Lombardia.")]


# ---------------------------------------------------------------- notizie

def notizie():
    return _json("notizie.json", [])


def articoli():
    out = []
    for n in notizie():
        out.append({
            "chiave": "art-" + n["slug"], "percorso": "news/" + n["slug"], "slug": n["slug"],
            "titolo": n["titolo"], "titolo_seo": n["titolo"] + " | Dieffepiu",
            "descrizione": n["testo"][:150], "data": n["data"], "estratto": n["testo"],
            "testo_wp": "\n\n".join(f"<!-- wp:paragraph -->\n<p>{p}</p>\n<!-- /wp:paragraph -->" for p in n["paragrafi"]),
            "fai": (lambda c, n=n: articolo(c, n)),
        })
    return out


def news_testa(c):
    return testa(c, "Fiere e novità", [("news", "Fiere e novità")],
                 "Cinque fiere dal 2021 a oggi, tra MADE expo a Milano e BATIMAT a Parigi. Qui date, padiglioni e stand.")


def elenco_notizie(c):
    righe = []
    for n in notizie():
        righe.append(f'''    <article class="notizia">
      <time datetime="{n["data"][:10]}">{n["quando"]}</time>
      <div class="corpo-n">
        <h2><a href="{c.link("news/" + n["slug"])}">{n["titolo"]}</a></h2>
        <p>{n["testo"]}</p>
      </div>
    </article>''')
    return '<section class="wrap" aria-label="Elenco delle notizie">\n  <div class="notizie-elenco">\n' + "\n".join(righe) + "\n  </div>\n</section>"


def news(c):
    return [news_testa(c), elenco_notizie(c), richiesta(c)]


def articolo(c, n):
    corpo = "\n".join(f"      <p>{p}</p>" for p in n["paragrafi"])
    s1 = f'''<section class="wrap testa-pagina" aria-labelledby="titolo">
  {briciole(c, [("news", "Fiere e novità"), ("", n["titolo"])])}
  <h1 class="titolo-pagina" id="titolo">{n["titolo"]}</h1>
  <p class="data-art"><time datetime="{n["data"][:10]}">{n["pubblicata"]}</time></p>
  <div class="griglia articolo">
    <div class="testo-art num">
{corpo}
    </div>
  </div>
  <p class="vai"><a href="{c.link("news")}">Tutte le fiere e le novità</a></p>
</section>'''
    return [s1, richiesta(c)]


# ---------------------------------------------------------------- contatti e area riservata

def contatti(c):
    s1 = testa(c, "Contatti", [("contatti", "Contatti")],
               "Per listini, schede tecniche, ricambi e preventivi delle macchine chiamateci o scriveteci. Per un impianto nuovo, prendete appuntamento.")
    s2 = f'''<section class="wrap griglia contatti-p" aria-label="Recapiti e modulo">
  <div class="recapiti">
    <p><a class="tel num" href="{TEL_HREF}">{TEL}</a><br>
    <a href="mailto:{MAIL}">{MAIL}</a></p>
    <p>Via Lombardia 33, 35020 Saonara (PD)<br>Zona industriale di Villatora<br>
    <a class="nw" href="{MAPPA}">Apri la mappa</a></p>
    <p class="orari num">Dal lunedì al giovedì <span class="nw">8:30-12:30</span> e <span class="nw">13:30-17:30</span><br>Venerdì <span class="nw">8:30-12:30</span> e <span class="nw">13:00-17:00</span></p>
    <div class="righe-r num">
      <p><b>Fax</b>+39 049 8790918</p>
      <p><b>PEC</b><a href="mailto:dieffepiu@pec.it">dieffepiu@pec.it</a></p>
      <p><b>Dati societari</b>Dieffepiu S.r.l., P.IVA IT01335450282, REA PD-204413</p>
    </div>
  </div>
  <div class="modulo-box">
    {moduli.blocco(c, "contatti")}
  </div>
</section>'''
    return [s1, s2]


def area_riservata(c):
    s1 = testa(c, "Area riservata", [("area-riservata", "Area riservata")],
               ["Listini, schede di taglio e disegni tecnici sono riservati alle aziende del settore: produttori, assemblatori e installatori di zanzariere.",
                "Mandateci la richiesta con i dati dell’azienda: vi ricontattiamo per l’accesso."])
    s2 = f'''<section class="wrap griglia contatti-p" aria-label="Richiesta di accesso">
  <div class="recapiti">
    <p>Siete già clienti? Chiamate l’ufficio.</p>
    <p><a class="tel num" href="{TEL_HREF}">{TEL}</a><br>
    <a href="mailto:{MAIL}">{MAIL}</a></p>
    <p class="vai"><a href="{CATALOGO}">Il catalogo generale è pubblico: PDF, 76&nbsp;MB</a></p>
  </div>
  <div class="modulo-box">
    {moduli.blocco(c, "accesso")}
  </div>
</section>'''
    return [s1, s2]


def pagina_404(c):
    s1 = testa(c, "Pagina non trovata", [("", "Pagina non trovata")],
               "L’indirizzo non esiste o è cambiato con il sito nuovo. Da qui trovate tutto.")
    s2 = f'''<section class="wrap" aria-label="Pagine principali">
  <div class="righe">
    {riga_link(c, c.link("sistemi"), "Sistemi", "Le quattordici linee del catalogo, in sei famiglie.")}
    {riga_link(c, c.link("macchine"), "Macchine", "Saldatrici, banchi di taglio e saldatura, bottonatrici e presse.")}
    {riga_link(c, c.link("contatti"), "Contatti", "Telefono, email, indirizzo e orari.")}
  </div>
</section>'''
    return [s1, s2, richiesta(c)]


# ---------------------------------------------------------------- sistemi e macchine (dati del catalogo)
import catalogo  # noqa: E402

macchine_piede = catalogo.macchine_piede


def _p(chiave, percorso, titolo, seo, desc, fai, genitore="", ordine=0):
    slug = percorso.split("/")[-1] if percorso else "home"
    return {"chiave": chiave, "percorso": percorso, "slug": slug, "genitore": genitore, "titolo": titolo,
            "titolo_seo": seo, "descrizione": desc, "fai": fai, "ordine": ordine}


PAGINE = [
    _p("home", "", "Home", "Dieffepiu, sistemi per zanzariere",
       "Profili in alluminio, componenti, kit e macchine per chi produce zanzariere. Saonara (Padova), dal 1987.", None),
    _p("sistemi", "sistemi", "Sistemi", "Sistemi per zanzariere | Dieffepiu",
       "Quattordici linee a catalogo in sei famiglie: in kit, a misura, carrarmato TANK, plissé PLIXI, battente e componenti universali.",
       catalogo.sistemi, ordine=1),
] + [
    _p("f-" + f["slug"], "sistemi/" + f["slug"], f["titolo"], f["titolo"] + " | Dieffepiu", f["descrizione_seo"],
       (lambda c, f=f: catalogo.famiglia(c, f)), genitore="sistemi", ordine=10 + i)
    for i, f in enumerate(catalogo.famiglie())
] + [
    _p("macchine", "macchine", "Macchine", "Macchine per zanzariere | Dieffepiu",
       "Saldatrici per fettuccia, banchi elettronici di taglio e saldatura fino a 8,2 m, saldatrice per tubi rete, bottonatrici e presse pneumatiche.",
       catalogo.macchine, ordine=2),
    _p("azienda", "azienda", "Azienda", "La nostra azienda | Dieffepiu",
       "Dal 1987 sistemi e macchine per zanzariere, oltre 2.000 impianti di produzione progettati e realizzati. Via Lombardia 33, Saonara (PD).",
       azienda, ordine=3),
    _p("news", "news", "Fiere e novità", "Fiere e novità | Dieffepiu",
       "MADE expo a Milano e BATIMAT a Parigi: date, padiglioni e stand di Dieffepiu.", news, ordine=4),
    _p("contatti", "contatti", "Contatti", "Contatti | Dieffepiu",
       "Telefono +39 049 8791175, info@dieffepiu.it, via Lombardia 33, Saonara (PD). Orari e modulo di contatto.", contatti, ordine=5),
    _p("area-riservata", "area-riservata", "Area riservata", "Area riservata | Dieffepiu",
       "Listini, schede di taglio e disegni per le aziende del settore: richiesta di accesso.", area_riservata, ordine=6),
]

P404 = _p("404", "", "Pagina non trovata", "Pagina non trovata | Dieffepiu", "La pagina non esiste.", pagina_404)
