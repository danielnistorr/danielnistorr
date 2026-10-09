# 01. Analisi del sito attuale (www.benvegnusrl.it)

Analisi del 4 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare con il cliente.

## In breve

- Sito ASP.NET del 2014, non responsive (viewport fisso a 1000 px), contenuti fermi al 2014 (news "Nuovo sito online!!"), avviso ferie del 2015 ancora nella home inglese, versione inglese rotta (pagine in errore 500). [Certo]
- Il catalogo è il vero patrimonio: **874 articoli in 10 famiglie e 55 sottocategorie**, con codice articolo, nome e **600 foto prodotto su fondo bianco** (31% degli articoli senza foto). [Certo]
- Identità: logo grigio e nero con effetto metallico (PNG 295x72, manca il vettoriale), accento rosso cuoio **#9F2E29** già usato nel footer, nei codici articolo e nelle icone categoria. Il nuovo sito tiene bianco, nero e questo rosso. [Certo]
- Foto: 1 esterno della sede caricato dal proprietario su Google (2048 px), 10 foto reali di sede e magazzino nello slider (750x470), loghi di 4 marchi. Nessuna foto adatta a un'apertura a tutta larghezza. [Certo]

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home IT | `/` | slider di 10 foto, 2 news del 2014, testo istituzionale, carosello marchi |
| Home EN | `/index.aspx?language=1` | testi rimasti in italiano, avviso ferie agosto 2015 |
| Azienda | `/IT/Azienda/` (doppione `/about.aspx`) | testo istituzionale ed elenco di 15 famiglie di prodotto |
| News | `/IT/News/` | 2 news del 2014, archivio vuoto |
| Contatti | `/IT/Contatti/` (doppione `/contact.aspx`) | mappa, dati, modulo contatti |
| Prodotti | 10 pagine categoria `/IT/Prodotti/...` + schede prodotto | catalogo vetrina senza prezzi, pulsanti "Richiedi informazioni" e "Scarica scheda" |
| Condizioni di vendita | `/condizioni-di-vendita-Benvegnusrl.pdf` | PDF di una pagina del 2014 |
| Pagine EN Company e Products | `/EN/...` | segnaposto mai compilato, categorie in errore HTTP 500 con codice sorgente visibile |

## Testi reali (verbatim, con i refusi originali)

Home:
1. "Benvegnù S.r.l. nasce nel 1980 a Vigonovo (Venezia), paese situato nell'area calzaturiera della Riviera del Brenta."
2. "Commercia componenti ed accessori per calzature e pelletterie, in particolare i materiali per la rifinitura del fondo e della tomaia. Inoltre dispone di tutta la piccola utensileria ed è specializzata in suole e lastre di gomma marchio Vibram."
3. "Benvegnù è rivenditore autorizzato dei migliori marchi sul mondo degli accessori per la calzatura e la pelletteria tra cui Gutermann, Girba, Vibram e Fratelli Zucchini."
4. "Il catalogo prodotti è in continuo aggiornamento per permettere a stilisti e produttori di seguire le tendenze del mondo della calzatura e dell'abbigliamento in pelle."
5. "Benvegnù si propone come partner per la vostra azienda puntando sulla convenienza, qualità e servizio immediato."
6. Payoff: "BENVEGNU' s.r.l. - Centro Articoli per Calzature e Pelletterie"

Azienda:
7. "Per soddisfare le varie esigenze di mercato la nostra ditta si propone con una vasta gamma di articoli sempre nuovi e aggiornati sulle ultime tendenze della moda, puntando sulla convenienza, qualità, e servizio immediato."
8. Elenco: filo in poliestere; elastico per tomaia; laccio in poliestere e cuoio; cerniere in nylon e metallo; tallonette coprichiodi; piccola utensileria per la calzatura; nastri abrasivi e tamponi marchio SIA; pennelli a mano e spazzole; chiodi, semenze in ferro e ottone; prodotti per la rifinitura della suola e della tomaia; prodotti per l'incollaggio marchio F.LLI ZUCCHINI; rinforzi per tomaia in tessuto; suole e lastre in gomma per suola marchio VIBRAM; occhielli, agraffi, rivetti; tessuti sintetici per la tomaia.

Contatti:
9. "BENVEGNÙ S.r.l. / Centro Articoli per Calzature e Pelletterie / V. Del Lavoro, 48 30030 Vigonovo (Ve) / Tel. (+39) 0499830202 / Fax. (+39) 0499831177 commerciale@benvegnusrl.it / Magazzino 8,30-12,30 14,30-18,30 / Giorno di chiusura : sabato"

Condizioni di vendita (PDF 2014):
10. "TIPOLOGIA CLIENTI: Aziende e soggetti partita iva, con emissione di fattura. MINIMO D'ORDINE: € 200,00 di merce I.v.a. esclusa." Pagamento con bonifico anticipato, evasione "entro 7 gg. lavorativi dal ricevimento del pagamento (solo per materiale pronto a magazzino)", trasporto con corriere Benvegnù o in porto assegnato.

Refusi da non riportare: "marchi sul mondo", "Gutermann" senza umlaut, "LA nostra ditta", "Da 30 anni" (dal 1980 sono 46), "DREMMEL", "7630 BOUDLER", email sbagliata `commerciale@benvegusrl.it` nella pagina inglese. Il nome compare in quattro grafie (BENVEGNU' s.r.l., BENVEGNÙ s.r.l., Benvegnu SRL, Benvegnu'): nel nuovo sito si usa sempre **Benvegnù S.r.l.**

## Catalogo (10 famiglie, 874 articoli)

| Famiglia | Articoli | Sottocategorie |
|---|---|---|
| Utensili | 370 | arnesi vari 48, compassi 4, cutter e coltelli 49, forbici 25, fustelle 8, lesine 3, martelli 15, mole 9, nastri per timbratura a caldo 12, pennarelli 25, piani di lavoro 12, pinze e tronchesi 48, punzoni 5, strumenti di misura 12, torchi 13, varie 82 |
| Suole Vibram | 177 | gomma monocolore 96, gomma PU 36, Gumlite 23, espanse 22 |
| Lastre Vibram | 94 | compatte 44, espanse 50 |
| Modelleria e riparazione | 67 | allungaforme 8, alzi 13, modelleria 17, riparazione 23, sostegni 2, tendicinturini 1, tendiscarpe 3 |
| Mezzesuole e tacchi Vibram | 58 | mezzesuole compatte 27, tacchi compatti 24, tacchi TPU e PU 7 |
| Filati ed elastici | 44 | 13 sottocategorie (per tomaia 17, poliestere ritorto 5 tra cui Mara e Tera Gütermann, trecce cerate, elastici) |
| Igiene e sicurezza | 28 | guanti 18, mascherine 10 |
| Esposizione e cura | 21 | cura della scarpa 8, esposizione 13 |
| Imballaggio | 10 | nastri 4, numerini autoadesivi 2, pittogrammi 4 |
| Prodotti chimici | 5 | prodotti Girba (Bordobrill, Iris, Lederpolish, Nubio, Tingileder), nessuna foto |

Il menu inglese mostra 16 famiglie (aghi, chiusure, fibbie e bottoni, rinforzi, chiodi e semenze, abrasivi, minuteria) mai pubblicate in italiano: coerente con l'elenco della pagina Azienda. Il nuovo sito lo dice ("Al banco c'è anche quello che non è online").

## Immagini usate oggi

| Tipo | Quantità | Uso nel nuovo sito |
|---|---|---|
| Foto slider (2 sede, 8 magazzino), 750x470 | 10 | convertite in bianco e nero, usate a mezza larghezza nei blocchi foto (`assets/web/magazzino-*.jpg`, `banco-*.jpg`) |
| Esterno sede dal profilo Google del proprietario, 2048x1361 | 1 | in bianco e nero, apertura della Home e pagina Azienda |
| Logo PNG 295x72 | 1 | testata; versione bianca ricavata per il footer nero (serve il vettoriale) |
| Loghi marchi (Vibram, Gütermann, Girba, Fratelli Zucchini) | 4 | striscia marchi, colori originali |
| Foto prodotto su bianco (400 e 800 px) | 600 | 35 scelte per rappresentare famiglie e modelli Vibram, a colori |
| Icone categoria 107 px su #9F2E29 | 27 | non usate (troppo piccole) |

Tutte le immagini originali scaricate sono in `assets/originali/` con `manifest.json` (URL di origine, pagina, dimensioni). Le 3 foto dell'interno trovate su Google sono di utenti terzi: non sono nel progetto e non vanno usate senza permesso.

## Problemi tecnici da segnalare al cliente

1. Sicurezza: le pagine inglesi mostrano errori ASP.NET con query SQL e codice sorgente, pagine d'errore IIS con il percorso del server, link pubblico a `/admin/`. Rischio di SQL injection probabile, non verificato. [Certo per l'esposizione]
2. Privacy: mappa Google caricata prima del consenso, cookie bar senza rifiuto, riferimento alla Legge 196/2003. [Certo]
3. SEO: nessun H1, doppie meta description, immagini senza alt, sitemap vecchia con 493 URL http, host senza www non reindirizzato. [Certo]
4. Schede esterne da correggere dopo il lancio: Girba elenca "Bevegnu srl, Via Alpi 2" (indirizzo vecchio); schede Virgilio, Paginebianche, Europages non rivendicate; categoria Google "Negozio di accessori di moda" poco precisa. [Certo]

Fonti di dettaglio: crawl completo, screenshot e PDF nella cartella di lavoro della ricerca (riassunti qui).
