# Mario Agnoletto, incisore meccanico: analisi per la nuova home

Sito: https://www.marioagnoletto.it (crawl e screenshot del 19/10/2026). Il sito è una sola pagina: le sezioni si aprono a pannello. Copia locale in `_prova/crawl/home.html` (IT) e `en.html` (EN).

## 1. In breve

- Officina di incisione meccanica che fa **minuterie e accessori metallici su misura ed esclusivi**, soprattutto per **calzatura e pelletteria**. Segue il pezzo per intero: progetto, prototipo, serie. Lavora zama, ottone, alluminio e acciaio (testo "Azienda").
- I prodotti si dividono in due famiglie:
  - **attrezzi per chi lavora la pelle**: punzoni e alfabeti per la stampa a caldo, fustelle, ruote e rulli, servizio di stampa e foratura;
  - **pezzi che finiscono sul prodotto**: fibbie, morsetti, talloni, puntali, copritacchi, tacchi gioiello, bigiotteria, targhe da vetrina.
- Clienti tipo, dedotti dal testo (il sito non fa nomi): calzaturifici e pelletterie della Riviera del Brenta che producono per le maison, laboratori di personalizzazione (alfabeti e "consegna anche in 24 h"), negozi e vetrinisti (targhe e articoli da vetrina).
- Dove: Via dell'Artigianato 18, Tombelle di Vigonovo (VE), in un capannone con insegna (foto `company.jpg`).
- Da quando: "Fondata nel 1979 da Mario Agnoletto". È un'impresa individuale.
- Quanti: 8 dipendenti secondo Atoka. È una microimpresa.

## 2. Il sito di oggi

**Pagine.** È una pagina sola con 4 pannelli:
- Home: la scritta che ruota sopra lo sfondo con i brillantini;
- Azienda;
- Prodotti, con 8 schede e una galleria di 18 foto;
- Contatti, con il modulo.

Ci sono anche gli strati Privacy e Cookies e una copia inglese in `/en/`. La sezione News esiste nel codice con 3 testi "Lorem ipsum" ma è tolta dal menu.

**Testi veri (verbatim, da home.html).**
- `<title>`: "Mario Agnoletto / Incisore Meccanico". Meta description: "Siamo un'azienda specializzata nell'incisoria e realizziamo minuterie e accessori in esclusiva, principalmente per calzature e pelletteria".
- Scritta che ruota (js/the-outskirts.js): "Dal 1979 specializzati in ..." seguita a turno da "Incisore Meccanico", "Punzoni in bronzo e acciaio" e "Fustelle, targhe e incisioni varie". La scritta dice "bronzo", la scheda dei punzoni dice "acciaio e ottone".
- Azienda, "La nostra storia": "Fondata nel 1979 da Mario Agnoletto, siamo un'azienda specializzata nell'incisoria e realizziamo minuterie e accessori in esclusiva, principalmente per calzature e pelletteria. Partendo da un'idea ne seguiamo la progettazione, lo sviluppo del prototipo e la produzione in serie. Lavoriamo materiali quali zama, ottone, alluminio, acciaio per soddisfare tutte le esigenze del cliente. I nostri prodotti sono seguiti con la massima attenzione in termini di qualità e precisione."
- Prodotti, "Realizzazioni":
  - Punzoni: "Punzoni in acciaio e ottone per stampa su pelle/cuoio set alfabeti per personalizzazione. Sviluppo grafica e consegna anche in 24 h".
  - Fustelle: "Fustelle in ottone, alluminio, acciaio per taglio e stampa di pelle/cuoio/tessuto".
  - Accessori: "Accessori quali fibbie, morsetti, talloni, puntali e copritacchi con qualsiasi finitura o verniciatura".
  - Bigiotteria: "Piccola bigiotteria come anelli, bracciali, spille e pendagli con finiture preziose e applicazioni di swarovsky e pietre".
  - Targhe: "Targhe da esposizione e articoli da vetrina". In inglese dice di più: "Personalized plates, Plexiglas plaques, aluminum and brass plates, showcase items".
  - Ruote e Rulli: "Ruote acciaio e rulli".
  - Tacchi gioiello: "Tacchi gioiello in ottone, acciaio e alluminio".
  - Stampa e foratura su pelle: "Servizio stampa e foratura su pelle; con catalogo di lavorazioni pronte".
- Cosa manca sul sito: macchine, certificazioni, numeri, clienti e foto dell'officina. Non ce n'è nessuno.

**Tecnologia.**
- HTML statico, ultima modifica "Last-Modified: Wed, 19 Jan 2022" (intestazione del server). Hosting Ergonet ("x-server-powered-by: Ergonet FireShield").
- Tema a pannelli con Bootstrap, jQuery 1.11.3, `the-outskirts.js` e il plugin wordsrotator.
- Google Analytics `UA-142064024-1`: Universal Analytics, che Google ha dismesso, quindi non raccoglie più dati.
- Il modulo invia a `contact.php`. Non l'ho provato.
- Mancano robots.txt e sitemap (rispondono 404).
- La pagina italiana dichiara `lang="en"` e il viewport ha `maximum-scale=1`, che blocca lo zoom.
- I Google Fonts (Raleway, Dosis, Montserrat, Oswald) sono richiamati in `http://` dentro una pagina https. Negli screenshot i titoli escono in un carattere di sistema.

**Problemi.** Screenshot in `_prova/attuale/`: home, azienda, prodotti e contatti, a 1440 e a 390.

A 1440:
- La prima schermata è una foto di repertorio di brillantini con stelle, senza nessun pezzo dell'azienda. La scritta ruota in 3D e nello screenshot resta storta a metà animazione (`home-1440-fermo.png`).
- Il menu è un hamburger anche su desktop.
- Le 18 foto di prodotto sono in bianco e nero e prendono colore solo al passaggio del mouse.
- I titoli rossi sopra i brillantini si leggono male (`prodotti-1440.png`).
- Il banner dei cookie è in inglese.
- Le sezioni non hanno indirizzi propri: per Google esiste una sola pagina.

A 390:
- Lo stesso sfondo; la prima schermata è solo testo e brillantini.
- I prodotti sono un lungo elenco centrato (`prodotti-390.png`).
- Il modulo ha i campi trasparenti sopra i brillantini (`contatti-390-1.png`).
- Il testo di "Azienda" è giustificato, con buchi tra le parole (`azienda-390.png`).

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Denominazione | Agnoletto Mario (insegna "Incisore Meccanico Mario Agnoletto") | informazione-aziende.it/Azienda_AGNOLETTO-MARIO: "Denominazione Agnoletto Mario"; insegna visibile in `company.jpg` |
| Forma giuridica | impresa individuale | stessa pagina: "Forma Giuridica IMPRESA INDIVIDUALE" |
| P.IVA | 00802440271 | sito, sezione home: "P. IVA 00802440271 / PEC" |
| Indirizzo | Via dell'Artigianato 18, 30030 Tombelle di Vigonovo (VE) | sito: "Via Artigianato, 18 / 30030 Tombelle di Vigonovo (VE)"; informazione-aziende.it: "VIA DELL'ARTIGIANATO 18, 30030, Vigonovo" |
| Telefono / Fax | 049 98 00 985 / 049 50 31 72 | sito, Contatti |
| Email / PEC | info@marioagnoletto.it / marioagnoletto@pec.it | sito, Contatti e home |
| Anno di fondazione | 1979 | sito: "Fondata nel 1979 da Mario Agnoletto" |
| Codice ATECO | 25.99.9, "Fabbricazione di altri prodotti vari in metallo n.c.a." | informazione-aziende.it; atoka.io/public/it/azienda/agnoletto-mario/4eeb54741e26 ("25.99.90") |
| Dipendenti | 8 | atoka.io (stessa pagina): "DIPENDENTI 8", "microimpresa (meno di 10 dipendenti)" |
| Anzianità al registro | 37 anni | atoka.io: "ANZIANITÁ 37 anni"; informazione-aziende.it: "31 - 40 anni" |

Non ho trovato pubblicati numeri su metri quadri, macchine, fatturato o clienti.

## 4. Materiale visivo

**Cosa ho scaricato.** In `assets/originali/` ci sono 23 file:
- 18 foto di prodotto a 1920x1080;
- la foto della sede;
- lo sfondo con i brillantini;
- un segnaposto rimasto dal tema, con la scritta "1920 X 1080 PX";
- il logo, in PNG 500x100: monogramma MA dentro un cerchio puntinato, più "Mario Agnoletto" in corsivo rosso;
- la favicon.

Non ci sono video. L'inventario con i soggetti è in `_prova/inventario-immagini.json` e il provino in `_prova/provino.jpg`.

**Voti.** Q = qualità (luce, nitidezza, risoluzione), A = forza come immagine d'apertura, entrambi da 1 a 10.

| Foto | Soggetto | Q | A |
|---|---|---|---|
| 12 | tre tacchi gioiello (stelo cromato, gabbia d'acciaio, lamelle in ottone) su pelle stampata | 6 | 6 |
| 17 | farfalle in acciaio lucido traforate, fondo nero | 6 | 5 |
| 13 | fibbie in ottone e cromo, una con borchie | 5 | 5 |
| 2 | lamiera d'ottone traforata a motivo geometrico | 5 | 5 |
| 6 | punzoni in ottone con il monogramma M; su un cliché si legge il marchio di una maison | 4 (fuori fuoco) | 5 |
| 1 | punzoni con lettere, ruota forata, fustelle | 5 | 4 |
| 15 | pelli stampate, forate e dipinte | 4 | 4 |
| 3, 4, 5, 7, 10, 14, 16 | ciondoli, minuterie miste, stampi, cavallo bronzato, applicazioni colorate, accessori su pelle rossa | 4-5 | 3 |
| 8, 9, 11, 18 | orecchini, anelli, moschettoni, fondo in foglia oro | 3-5 | 2 |
| sede | facciata del capannone con insegna | 5 | 2 |
| sfondo con i brillantini | immagine di repertorio | 6 | 1 |

**Giudizio: 4/10. Il materiale NON regge una home di alta gamma.**
- Sono foto da telefono, con luce piatta e riflessi bruciati.
- I fondi sono improvvisati (pietra, foglia oro, rete, cartoncino) e le composizioni affollate.
- Metà della galleria è bigiotteria con cuori e teschi, che parla di bancarella e non di maison.
- Non c'è nessuna foto dell'officina, delle macchine o delle mani.

Le foto 12, 17, 13 e 2 si possono usare in una griglia secondaria, ritagliate e corrette, ma non in apertura. Serve mezza giornata di still life, sui pezzi e sui punzoni con la loro impronta, più mezza giornata in officina.

## 5. Il soggetto visivo

**Cosa è bello da vedere, a livello da rivista.**
- Il punzone d'ottone visto dalla testa: le lettere sono a rovescio, lucide sugli spigoli, opache nel fondo.
- L'impronta che lo stesso punzone lascia, a secco o a caldo, sulla pelle.
- Il tacco gioiello trattato come una scultura.
- La fibbia grezza appena fusa in zama e la stessa fibbia finita in oro, palladio o canna di fucile.
- Il filo affilato di una fustella.
- I trucioli d'ottone sotto la fresa.
- Un alfabeto completo di punzoni allineato in un astuccio.

**Il dettaglio che è solo loro: il dritto e il rovescio.** Ogni loro lavoro esiste due volte: in metallo, in negativo e a specchio, e sulla pelle, in positivo e leggibile. Nessun fornitore di pelle o di accessori finiti può raccontarlo. Anche il loro marchio, il monogramma MA nel cerchio puntinato, sembra già la testa di un punzone o un marchio di garanzia.

**Direzione A, "Dritto e rovescio".**
- Idea: ogni immagine è una coppia, il punzone e la sua impronta, il grezzo e il finito, a piena pagina su fondo scuro.
- Immagini: still life macro con luce radente, da sinistra, su pelle nera e cuoio naturale. Il metallo è l'unica cosa che brilla.
- Tipografia: un bodoni da titolo molto grande (Bodoni Moda), testo in un grottesco sobrio (Inter Tight), codici e misure in monospazio (Geist Mono), come "PZ 0412 · ottone · 18 mm".
- Colore: nero conceria #151311, avorio pelle #EFE8DC, ottone #B08D57 solo per i dettagli. Il rosso del logo resta minimo, come un bollino.
- Gesto d'interazione: il titolo d'apertura è composto a specchio, come su un punzone. Un solo interruttore "Stampa" lo gira leggibile con uno scatto netto, e lo stesso interruttore mette a confronto le coppie di foto.

**Direzione B, "Tavola dei campioni".**
- Idea: la home come una tavola da archivio tecnico, chiara e precisa, con i pezzi fotografati dall'alto e numerati, come in un catalogo museale.
- Immagini: piani dall'alto su cartone grigio chiaro con ombre corte, una scala millimetrata nell'inquadratura e le tre fasi di ogni pezzo (disegno, prototipo, serie) affiancate.
- Tipografia: un grottesco svizzero (Schibsted Grotesk o Neue Montreal) a pesi leggeri, numeri tabellari, didascalie in monospazio.
- Colore: carta #F3F1EC, grafite #2A2A28, un solo accento rosso #C8102E preso dal logo, usato come timbro di controllo.
- Gesto d'interazione: un filtro per materiale (zama, ottone, alluminio, acciaio) che cambia subito la tavola, senza animazioni, e tre schede "Progetto / Prototipo / Serie" sullo stesso pezzo.

## 6. Immagini sostitutive

In `assets/esterne/` ci sono 10 foto Unsplash, scaricate a 2400 px. Su ogni pagina ho verificato la dicitura "Free to use under the Unsplash License". Elenco, autori e note sono in `assets/CREDITI.md`.

- Per la Direzione A:
  - fibbie in ottone e cromo di Ruan Richard Rodrigues (3 foto, una buona per l'apertura);
  - una décolleté dorata riflessa su fondo scuro;
  - la grana di una pelle nera.
- Per la Direzione B:
  - punzoni incisi su un banco di legno (apertura);
  - una fresa al lavoro su rame;
  - un mandrino su alluminio;
  - mani che incidono a bulino;
  - minuterie zigrinate in ottone.

Sono **segnaposto da sostituire** con foto vere di Agnoletto e il LEGGIMI lo dirà. Non c'è nessuna immagine generata dall'IA. Nessuna mostra punzoni da pelletteria con lettere a specchio: quello scatto va fatto da loro.

## 7. Riferimenti di alta gamma

Screenshot della prima schermata a 1440 e a 390 in `_prova/riferimenti/<nome>-1440.png` e `-390.png`, con i caratteri letti dal codice in `<nome>.json`.

**De Castelli** (decastelli.com), metallo lavorato a mano, Treviso. È il più forte.
- Cosa lo rende di alta gamma:
  - nessuna scritta sopra le foto;
  - una griglia a tre colonne di oggetti in metallo su fondo bianco, a tutta pagina e con altezze diverse;
  - il logo al centro, con la C barrata;
  - un solo carattere, Gramatika, piccolo (14-16 px, spaziatura 0.15 px).
- Il lusso viene dal silenzio e dalla qualità dello still life.
- Cosa non riprendere: il menu da e-commerce con l'icona dell'account.

**Giobagnara** (giobagnara.com), oggetti in pelle, Genova.
- Cosa lo rende di alta gamma:
  - il nome in maiuscolo al centro;
  - un menu fitto in maiuscoletto;
  - testi in Plantin (un serif da libro) con titoli in DIN Neuzeit Grotesk;
  - un carosello di still life in uno studio grigio;
  - un fondo #FBFBFB caldo.
- Cosa non riprendere: il menu con 20 voci e su mobile il testo lungo e giustificato.

**Tanneries Haas** (tanneries-haas.com), conceria dal 1842.
- Cosa lo rende di alta gamma: una sola foto di reportage a tutta pagina, l'operaio che lancia una pelle nel vapore, e il logo minuscolo in un riquadro "HAAS 1842". Mostra la fabbrica come un'azione, non come un capannone.
- Cosa non riprendere: i caratteri qualsiasi (Open Sans e Poppins) e il carosello con le frecce.

**Gruppo Mastrotto** (mastrotto.com), conceria vicentina.
- Cosa lo rende di alta gamma:
  - "Leather forward" in Silka 80 px, corto e sicuro;
  - un video in apertura (a 1440 nello screenshot esce nero perché il video non parte senza interfaccia);
  - su mobile il macro di pelle rossa a grana;
  - il menu in una pillola scura.
- Cosa non riprendere: l'apertura che dipende tutta dal video e lo slogan in inglese generico.

**Ghidini 1961** (ghidini1961.com), arredi in ottone, Lumezzane.
- Cosa lo rende di alta gamma: il nome scritto anche a specchio ("GHIDINI 1961 1961INIDIHG"), la stessa idea del punzone usata come marchio, e Apercu grande sopra una foto ambientata in un palazzo affrescato.
- Cosa non riprendere: "NEW COLLECTION 2026" in maiuscolo con il bottone bordato, che è un cliché.

**Bottega Ghianda** (bottegaghianda.com), ebanisteria.
- Cosa lo rende di alta gamma: un oggetto unico in studio su sfumatura scura, il marchio-emblema al centro e un titolo in Playfair.
- Cosa non riprendere: Playfair, che ormai è ovunque, e il carosello di notizie in apertura.

**Esempi da non seguire, dal loro stesso settore.**
- Riri (riri.com, cerniere e bottoni per il lusso) e Lampo (lampo.eu): slider con riquadro di testo sopra la foto, foto di moda di repertorio, citazione d'autore. Mostrano che anche i grandi fornitori di accessori metallici hanno siti ordinari: lo spazio per distinguersi c'è.
- Officine Gullo (`gullo-*.png`): la prima schermata è coperta dalla finestra per scegliere il paese, quindi non è valutabile. Si vede solo il titolo in Nyght Serif su nero.

## 8. Da confermare

- **Anno.** Il sito dice 1979. Atoka dà 37 anni di anzianità, cioè circa il 1989, forse la data d'iscrizione dell'attuale impresa individuale. Va chiarito prima di scrivere "dal 1979" in grande.
- **Dipendenti.** Il dato di Atoka (8) va confermato insieme alle macchine, ai metri quadri del capannone e alle finiture interne o esterne. Il bagno galvanico è probabilmente esterno: non c'è nessuna fonte.
- **Clienti e marchi.** Nella foto 6 si legge "BURBERRY" su un cliché. Non prova un rapporto di fornitura e non si può citare né mostrare senza permesso; lo stesso vale per qualunque altro marchio.
- **Materiale dei punzoni.** La scritta che ruota dice "bronzo", la scheda dice "acciaio e ottone".
- **Persone.** Chi guida oggi l'azienda (Mario Agnoletto o un familiare) e se si può mostrare in foto.
- **Fondi delle foto.** Le pelli stampate a rilievo nelle foto 12 e 13 potrebbero essere il loro servizio "stampa e foratura": è un'ipotesi da verificare. Se è così, quei fondi sono già un lavoro loro.
- **Diritti delle immagini.** Le foto prodotto vanno riscattate o usate con il loro permesso. Lo sfondo con i brillantini è di repertorio e non va riusato.
- **Modulo contatti.** Non verificato (non inviato).
