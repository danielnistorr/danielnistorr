# 01. Analisi del sito attuale (www.leondoroeste.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).
Materiale di lavoro: crawl in `_prova/crawl/` (pagine, testi estratti, fonti esterne), screenshot e misure in `_prova/attuale/`, inventario foto in `_prova/inventario-immagini.json`.

## In breve

- Sito statico scritto a mano (XHTML 1.0 del 2014 circa, impaginazione esportata da Adobe Fireworks a fette `presentazione_r1_c1.jpg`), su hosting condiviso Shellrent. Nessun CMS. Blocco fisso largo 800 px, testo chiuso in una scatola di 463x614 px che scorre per conto suo: nella pagina Ristorante il 76% del testo (tutto il menu) è nascosto in quella scatola. **Nessuna meta viewport in nessuna pagina**: a 390 px il telefono disegna la pagina larga 980 px e il testo diventa di **4,8 px** effettivi. [Certo]
- Pagine ferme: home, bike hotel, ospedale, cosa visitare e dove siamo sono del 6/7/2022; il foglio di stile è del 18/11/2014. Solo il listino (marzo 2026) e il ristorante e le prenotazioni (gennaio 2025) vengono aggiornati. Dentro restano frasi superate: "nuovo polo ospedaliero" (aperto nel 2014), "prossima apertura del casello Valdastico sud" (aperto il 31/8/2015), "l'Ospedale di Este si trova a soli 400m". [Certo]
- La home pesa **10 MB** a desktop: 9,5 MB sono il video di Facebook che si scarica da solo, prima di qualsiasi consenso. La mappa Google in Dove siamo carica 40 risorse Google senza consenso. Il banner cookie c'è solo in home e ha solo "Chiudi ed accetta". [Certo]
- Il patrimonio vero è altrove: un **video ufficiale "Emozioni & Sapori"** (Facebook, 3 min 51 s, Full HD, girato da NEON produzione immagini) con droni sui Colli, ciclisti in maglia gialla e nera "Leon d'Oro ESTE (Padova)", la sala piena, la facciata di sera; un **servizio fotografico professionale del 21/10/2021** (Canon 5D Mark III, data letta nei file) di cui il sito pubblica 5 scatti a 1200 px (2 con la data nei metadati, 3 senza metadati ma dello stesso servizio [Probabile]) e il portale della Regione altri 4 a 1024 px; una **foto d'epoca con l'insegna "TRATTORIA AL LEON D'ORO"** ritrovata a 3298 px. [Certo]
- Identità visiva da cui partire, tutta vera e verificabile: facciata ocra con persiane verdi e scritta dipinta in corsivo "Albergo ★★ Leon d'Oro"; insegna nera con leone dorato; logo a tratto con testa di leone; maglia da ciclismo gialla e nera; cartolina con lettere verdi "LEON D'ORO". Il logo esiste solo come immagine da 311x231 px con una foto dietro: manca il vettoriale. [Certo]
- Prenotazione solo via email, senza modulo. Su Google le tariffe mostrate per l'albergo sono solo di portali (Booking.com, Super.com, Bluepillow.com): il sito ufficiale non compare tra le offerte. [Certo, Google, 6/10/2026]

## Pagine esistenti

16 pagine HTML raggiungibili (8 italiane, 7 inglesi, 1 informativa). Nessuna `sitemap.xml` né `robots.txt` (entrambe 404). [Certo]

| Pagina | URL | Ultima modifica (header) | Stato |
|---|---|---|---|
| Home | `/` e `/index.html` (doppione) | 06/07/2022 | testata "Benvenuti" in immagine, video Facebook incorporato, cartolina d'epoca, testo di presentazione, foto della facciata |
| Albergo e camere | `/camere-e-stanze-colli-euganei.html` | 02/03/2026 | testo servizi, **listino 2026**, 4 foto (2 camere, 2 bagni) |
| Ristorante e cucina | `/ristorante-cucina-tipica-veneta.html` | 09/01/2025 | testo, menu di carne e menu di pesce del venerdì, 13 foto |
| Bike Hotel Colli Euganei | `/mtb-bike-hotel-colli-euganei.html` | 06/07/2022 | testo, 3 foto 400 px di uscite in bici |
| Albergo per ospedale unico | `/albergo-per-ospedale-unico-monselice.html` | 06/07/2022 | navetta e taxi per Schiavonia; la testata in immagine dice "Prenotazioni" (fetta sbagliata) |
| Cosa visitare | `/dove-dormire-e-cosa-visitare-este.html` | 06/07/2022 | Este, Colli, città vicine; 16 foto di territorio |
| Prenotazioni camere | `/prenotazione-camera-este-colli-euganei.html` | 09/01/2025 | solo istruzioni per scrivere una email |
| Dove Siamo | `/dovesiamo-colli-euganei.html` | 06/07/2022 | indirizzo, mappa Google (incorporata nel 2018) |
| Informativa Privacy e Cookie | `/informativa-cookie.html` | 06/07/2022 | modello generico; la testata dice "Benvenuti" |
| Versione inglese | `/en_index.html`, `/en_hotel-rooms-euganean-hills.html`, `/en_restaurant-typical-venetian-cuisine.html`, `/en_mtb-bike-hotel-euganean-hills.html`, `/en_sights-in-este.html`, `/en_booking-hotel-este-euganean-hills.html`, `/en_where-we-are-euganean-hills.html` | 2022, camere 02/03/2026 | manca la pagina ospedale; il listino inglese dice "Price List 2023" |

Menu (uguale in tutte le pagine): Home page, Albergo e camere, Ristorante e cucina, Bike Hotel Colli Euganei, Albergo per ospedale unico, Cosa visitare, Prenotazioni camere, Dove Siamo, bandiera inglese.

## Testi reali (verbatim, con i refusi originali)

Testi completi in `_prova/crawl/testi/*.txt`. Qui quelli che servono al nuovo sito.

Colonna laterale (tutte le pagine):
1. "Albergo Ristorante "Leon d'Oro" / Viale Fiume, 20 35042 Este (PD) / Tel. 0429 602949 - Fax 0429 3072 / prenotazioni@leondoroeste.it / P.IVA 04185510288"

Home:
2. Didascalia del video Facebook: "ALBERGO RISTORANTE LEON D'ORO: il vostro punto di partenza per escursioni in bici nel cuore degli Euganei e la Bassa, all'insegna del divertimento e della buona Cucina. Cucina Divertimento Assistenza Relax"
3. "L'Albergo Ristorante Leon d'Oro, è una confortevole struttura situata nella graziosa città di Este a due passi dal centro e dal Castello Carrarese."
4. "L'albergo è sorto agli inizi del 900 nei pressi della Porta Vecchia, storica porta cittadina e punto d'approdo per chi a quel tempo arrivava a Este per via fluviale."
5. "Oggi la struttura è gestita dalla 4° generazione della famiglia Rubini, che ha fatto dell'Ospitalità un valore da tramandare e coltivare."
6. "Con la [parola omessa, è in PAROLE_VIETATE; testo integrale in `_prova/crawl/testi/index.txt`] che li contraddistingue offrono al turista e al viaggiatore l'opportunità di soggiornare in un'atmosfera diversa, con la possibilità di trascorrere momenti di piacevole svago e regalare al palato i sapori di tempi ormai passati."
7. "Il ristorante serve la cucina tipica veneta preparata e servita secondo la tradizione, senza rivisitazioni, con piatti caratteristici come il Musso con polenta, il Baccalà alla vicentina, i Bigoli alla boscaiola, il Fegato alla veneziana. Per curiosare nella nostra cucinai vi invitiamo a visitare la pagina dedicata al ristorante con il menu completo e le specialità di pesce."
8. "L'albergo non offre solo servizi di pernottamento per chi ama immergersi nella storia e nella cultura delle cittadine della provincia di Padova. Infatti la sua collocazione è strategica per chi ama avventurarsi in escursioni sui Colli Euganei a piedi, in bicicletta o in Mountain Bike."
9. "La città di Este fa parte della ciclovia E2, detta anche "anello ciclabile" dei Colli Euganei, ma gli amanti dell'MTB possono anche seguire il percorso dell'Atestina Superbike Granfondo Regionale di mountain bike XCP grazie alle indicazioni messe a disposizione dal personale del"bike hotel"."
10. "Da anni la società agonistica amatoriale Estebike collabora con l'albergo Leon d'Oro offrendo indicazioni pratiche e assistenza tecnica per facilitare turisti e ciclisti nel vivere i Colli Euganei a contatto con la natura in sella alle due ruote."

Albergo e camere:
11. "Per chi cerca un soggiorno tranquillo l'ospitalità offerta dall'albergo Leon d'Oro è l'ideale: può contare su camere ampie, arredate in modo sobrio e caratteristico e dotate di tutti i comfort (aria condizionata, TV SAT, wi-fi, telefono e parcheggio pubblico adiacente l'albergo)."
12. "Per coloro che viaggiano in bici lungo la ciclovia E2, o desiderano prenotare una camera per visitare i Colli Euganei in bicicletta o MTB, è disponibile un garage privato."
13. "Inoltre il personale dell'albergo può fornire indicazioni riguardo le mete di maggiore interesse turistico della zona."
14. "La collocazione è ideale anche per chi necessita di accedere comodamente alla locale struttura sanitaria: l'Ospedale di Este si trova a soli 400m dall'albergo ed è raggiungibile comodamente in taxi o a piedi."
15. Listino: "Listino Prezzi 2026 - stagione unica / Pernottamento e colazione / Singola € 50,00 / Doppia/matrimoniale € 75,00 / Listino Prezzi - stagione unica / Mezza pensione o Pensione completa incluso bevande / Mezza pensione per persona € 65,00 / Pensione completa per persona € 80,00"

Ristorante e cucina:
16. "Il ristorante Leon d'Oro, da sempre attento alla tradizione locale, offre ai suoi clienti un'ampia scelta di piatti tipici veneti con i sapori dei Colli Euganei."
17. "Nel clima di cortesia e disponibilità che solo una gestione famigliare può assicurare potrete gustare il meglio della tradizione culinaria del Veneto preparato "come una volta" con particolare cura nella scelta di prodotti di prima qualità."
18. "Tra le nostre portate spiccano il Musso con polenta, il Baccalà alla vicentina, i Bigoli alla Boscaiola, il Fegato alla veneziana."
19. "La nostra selezione di vini proviene da cantine selezionate del territorio dei Colli Euganei."
20. "In omaggio alla cultura contadina delle nostre terre, il venerdì sera proponiamo un menù speciale a base di pesce (il venerdì sera è gradita la prenotazione)."
21. "Ricordiamo ai nostri ospiti che il ristorante è chiuso di Domenica."
22. Menu di carne, titolo: "MENU DI CARNE (Questo proposto è standard. Le nostre proposte variano ogni giorno)". ANTIPASTI: AFFETATI MISTI; SOPRESSA POLENTA FUNGHI; PROSCIUTTO CRUDO con MELONE---BRESAOLA/RUCCOLA/GRANA. PRIMI -PIATTI: PASTA ALL'UOVO AL RAGU O POMODORO; TAGLIOLINI IN BRODO; ZUPPA DI VERDURA VARIE; PASTA FAGIOLI; FETTUCINE AL SUGO; SPAGHETTI ALLA CARBONARA; GNOCCHI DELLA CASA; PASTICCIO DELLA CASA; CANELLONI DELLA CASA; PASTA ALL'ARRABBIATA; RISOTTI; BIGOLI ALLA BOSCAIOLA. SECONDI PIATTI: BRACIOLA DI MAIALE; BRACIOLA DI VITELLO; COSTATA DI MANZO O FILETTO; BISTECCA DI MANZO O TACCHINO; FEGATO O CUORE DI VITELLONE; FEGATO ALLA VENEZIANA; TRIPPA ALLA PARMIGIANA; CONIGLIO AL FORNO O CACCIATORA; SPEZZATINO O OSSOBUCO DI VITELLO; ARROSTO DI VITELLO; MUSSO CON POLENTA; BRASATO DI MANZO; BOLLITO MISTO; SALSICCIA POLENTA CON CONTORNO; VITELLO TONNATO-- CARPACCIO.--ROASTBEFF--CRUDO MELONE; BACCALA ALLA VICENTINA; CONTORNI COTTI, FRESCHI, GRILIATI.
23. "MENU DI PESCE SOLO IL VENERDI'". ANTIPASTI: INSALATA DI MARE; CARPACCIO DI SPADA; SCAMPI ALLA BUZZARA; GRANSEOLA O GRANSIPORO; GAMBERETTI IN SALSA ROSA O CON RUCOLA E GRANA; SARDE IN SAORA; COZZE VONGOLE; ASTICE. PRIMI PIATTI: SPAGHETTI ALLO SCOGLIO; PASTICCIO DI PESCE; SPAGHETTI ALLA MARINARA; TAGLIATELLE ALLA BUZZARA; TAGLIATELLE CON LE SEPPIE; GNOCCHI ALLA MARINARA; RISOTTI A BASE DI PESCE; PENNE AL SALMONE; ZUPPA DI PESCE. SECONDI PIATTI: VITELLO DI MARE AI FERRI; SOGLIOLA AI FERRI; BRANZINO AI FERRI; ORATA AI FERRI; SCAMPI E CAPPESANTE; SEPPIE AI FERRI; SPIEDINI DI GAMBERONI; FRITTI MISTI; BACCALA :VICENTINA, INSALATA; SEPPIE ALLA VENETA; GRIGLIATA MISTA.

Bike Hotel Colli Euganei:
24. "Este è il punto di partenza ideale per piacevoli e divertenti escursioni sui Colli Euganei a piedi e in biciletta."
25. "A questo proposito l'albergo Leon d'Oro è anche Bike hotel: mette a disposizione dei suoi ospiti un garage in cui custodire le biciclette."
26. "Se siete amanti dell'MTB da Este partono il circuito dell'Atestina Superbike Granfondo Regionale di mountain bike XCP, nonché numerosi altri sentieri percorribili sulle due ruote come la Transeuganea, un percorso nella flora e fauna dei Colli Euganei con un'attenzione anche alla cultura enogastronomica."
27. "Se invece preferite percorsi meno spericolati, Este si inserisce nella ciclovia E2, ovvero l'anello ciclabile che unisce i paesi attorno ai Colli Euganei per una lunghezza di 70km."
28. "L'albergo Leon d'Oro collabora da molti anni con il Team Este Bike e contribuisce all'organizzazione delle sue escursioni in MTB e bicicletta da strada."
29. "Grazie a questo sodalizio è in grado di offrire ai suoi ospiti consigli, guide e Tour dei colli Euganei in bicicletta."
30. Didascalie: "Ritrovo in Piazza alle 9.00 (inverno) e 8.30 (estate)"; "Piste ciclabili (Este, Padova, Vicenza, Colli Euganei) L'anello ciclabile dei Colli misura ben 70 km!"; "Possibilità di percorrere la famosa "Transeuganea" (60 Km)"

Albergo per ospedale unico:
31. "Cercate un albergo per il nuovo ospedale unico di Monselice?"
32. "Il suo nome per esteso è Ospedali riuniti Padova Sud - Madre Teresa di Calcutta e dal 5 novembre 2014 è diventato il nuovo polo ospedaliero della Bassa Padovana."
33. "Il nostro albergo da sempre forniva camere a prezzi vantaggiosi a chi per necessità era costretto a soggiornare nei pressi dell'ospedale di Este e con la costruzione del nuovo ospedale unico, continueremo a fornire agli ospiti prezzi unici e servizi riservati."
34. "Tramite bus navetta dal costo di 4,80 euro (andata e ritorno compresa) partente dalla stazione delle corriere di Este, ecco gli orari in PDF e il numero di telefono dell'ospedale 0429.714111; Tramite servizio Taxi Este tel. +39.339.5040502 sig.Malaman."

Cosa visitare (estratti):
35. "In questa pagina offriamo spunti per il turismo a Este e nei dintorni. Maggiori informazioni e opuscoli vi verranno fornite dal personale dell'albergo."
36. "Este è una città murata che vede le sue origini nell'età del ferro, abitata dalle antiche popolazioni di Paleoveneti." (segue storia: Alberto Azzo II d'Este, castello di Ubertino da Carrara, Repubblica di Venezia)
37. "Per approfondire e conoscere la storia di Este vi invitiamo a visitare il Museo Nazionale Atestino, il Castello Carrarese, il Duomo di Santa Tecla, dove è custodita la splendida pala di Giambattista Tiepolo [...], l'antica chiesa di San Martino e il Santuario della Madonna delle Grazie."
38. "I Colli Euganei sono famosi per i Vini e per la produzione di Olio, presso il nostro albergo vi daremo indicazioni su quali cantine e frantoi visitare se amate il turismo enogastronomico."
39. "A meno di un'ora di strada potere visitare Verona, Mantova, Vicenza, Padova, Treviso, Venezia, Chioggia, Rovigo, Ferrara, Bologna."
40. "Inoltre, con la prossima apertura del casello autostradale dell'autostrada Valdastico sud a Noventa Vicentina, sarà possibile raggiungere l'altopiano di Asiago in meno di un'ora."

Prenotazioni e Dove siamo:
41. "Per richiedere la prenotazione di una stanza all'albergo Leon d'Oro di Este (Padova) puoi scrivere una email all'indirizzo: prenotazioni@leondoroeste.it. Nell'email specificate: Nome, Cognome, telefono, data di arrivo, data di partenza, numero di adulti e bambini. Il nostro personale ti risponderà al più presto comunicandoti la disponibilità e le varie opzioni disponibili."
42. "Ci troviamo nella città storica di Este ai piedi dei Colli Euganei, poco distanti dalla zona termale di Abano e Montegrotto, in Provincia di Padova."

Storia da fonte pubblica (non sul sito; scheda della Regione Veneto "Veneto Around Me", ripresa dal blog "Micro Storie del Commercio a Padova e provincia", 09/02/2015, testo raccolto dal signor Lorenzo Rubini):
43. "In origine era la "Trattoria al Leon D'oro con Alloggio" [...]. La sua storia inizia nei primi anni del '900 come trattoria e punto di ristoro per i viaggiatori e i loro cavalli, ma si ha motivo di credere che, intorno al 1300, fosse un monastero: sono stati trovati resti di mosaico e un pozzo antico, ancora annesso nella struttura interna."
44. "Negli anni '50 il locale venne acquistato da Giulio Rubini e Norma Momoli, nonni degli attuali gestori e titolari, che sistemarono le camere, al tempo erano 18, e allargarono la sala ristorante. Dal 1976/77 il locale passò al figlio Rodolfo che portò il numero delle camere a 13."
45. "Oggi la ditta titolare è formata dai fratelli Rubini Lorenzo e Giulio, eredi di Rodolfo. La loro è la terza generazione che gestisce il Leon D'oro, ma la tradizione di albergatori- ristoratori risale ai bisnonni, proprietari dello scomparso Albergo Sasso, sempre in Este."
46. "Le specialità culinarie sono i piatti tipici della cucina veneta, baccalà, musso, bigoli al ragù, preparati come vuole la tradizione dalla signora Brugin Annalisa, madre dei titolari."
47. Sul nome: "il glorioso passato di Venezia rimane impresso nelle insegne di numerosi locali di fine '800 - primi '900 di tutta la Regione, da Treviso a Padova, ad indicare i punti di ristoro per coloro che passavano con carrozze, cavalli e la diligenza."

Testi dentro le immagini (trascritti): logo "ALBERGO ★★ LEON D'ORO ESTE" con testa di leone; testate in gotico "Benvenuti", "Le Camere", "La Cucina", "Sport e Tempo Libero", "Cosa Visitare", "Prenotazioni", "Dove Siamo"; cartolina "ALBERGO - RISTORANTE" / "LEON D'ORO"; foto d'epoca "Este - Viale di Via Restara" con l'insegna "TRATTORIA AL LEON D'ORO"; nel video: facciata con scritta dipinta "Albergo ★★ Leon d'Oro", insegna nera "LEON D'ORO Albergo ★★ Ristorante" con leone dorato, targa "ALBERGO LEON D'ORO" accanto alla porta, maglia da ciclismo "Leon d'Oro ESTE (Padova)", titoli di coda "NEON produzione immagini". Le cartoline del territorio dicono "Este - Porta Vecchia" e "ESTE - Via Roma".

Refusi e incoerenze da non riportare: "nostra cucinai", "4° generazione" (4ª), "biciletta", "potere visitare", "opuscoli vi verranno fornite", "del"bike hotel"", "colli Euganei", "AFFETATI", "RUCCOLA", "FETTUCINE", "CANELLONI", "ROASTBEFF", "GRILIATI", "ZUPPA DI VERDURA VARIE", "BUZZARA" (busara), titolo della pagina ospedale "Albero per ospedale unico", "ai piedi del Colli Euganei" nel titolo delle camere. Generazioni: il sito dice **4ª**, la Regione e il blog dicono **terza** (contando dai nonni del 1950; i bisnonni avevano l'Albergo Sasso) [DA CONFERMARE quale formula usare]. Il nome compare come Leon d'Oro, Leon D'oro, LEON D'ORO, Leon D'Oro: nel nuovo sito **Leon d'Oro**.

## Cosa fanno o vendono

| Cosa | Dettaglio | Fonte |
|---|---|---|
| Albergo 2 stelle | 13 camere, 24 posti letto; singole e doppie/matrimoniali; aria condizionata, TV SAT, wi-fi, telefono; parcheggio pubblico accanto all'albergo | [Certo] sito, pagina camere; Regione Veneto (dati.veneto.it, elenco strutture ricettive, aggiornato al 6/10/2026) |
| Listino 2026, stagione unica | pernottamento e colazione: singola € 50, doppia/matrimoniale € 75; mezza pensione € 65 a persona, pensione completa € 80 a persona, bevande incluse | [Certo] sito (pagina aggiornata il 2/3/2026); l'inglese dice ancora "2023" |
| Ristorante di cucina veneta | piatti della tradizione "senza rivisitazioni": musso con polenta, baccalà alla vicentina, bigoli alla boscaiola, fegato alla veneziana; menu del giorno variabile; vini dei Colli Euganei; chiuso la domenica | [Certo] sito |
| Venerdì sera di pesce | menu di pesce solo il venerdì sera, prenotazione gradita | [Certo] sito |
| Bike hotel | garage privato per le bici; collaborazione con il Team Este Bike (escursioni MTB e strada, ritrovo in piazza alle 9.00 d'inverno e alle 8.30 d'estate); ciclovia E2 (70 km), Transeuganea; maglia da ciclismo gialla e nera "Leon d'Oro ESTE (Padova)" nel video | [Certo] sito e video; attualità della collaborazione e dell'Atestina Superbike [DA CONFERMARE] (il dominio atestinasuperbike.it è oggi parcheggiato) |
| Albergo per l'ospedale | camere per chi assiste un ricoverato all'Ospedale di Schiavonia (Ospedali riuniti Padova Sud); indicazioni su navetta e taxi | [Certo] sito; prezzi della navetta e taxi [DA CONFERMARE] |
| Informazioni turistiche | consigli su Este, Colli, cantine e frantoi; opuscoli in reception | [Certo] sito |
| Servizi secondo Google | Wi-Fi, colazione inclusa, parcheggio gratuito, aria condizionata, ristorante | [Certo] Google, scheda "Leon d'Oro", 6/10/2026 |

Non dichiarati da nessuna parte: orari del ristorante (pranzo e cena), orari di check-in e check-out, colazione (orario, tipo), numero di posti in sala, menu con prezzi, lingue parlate oltre all'inglese (la Regione indica solo inglese), animali (la Regione dice no). Tutto [DA CONFERMARE].

## Immagini usate oggi

Scaricate tutte in `assets/originali/` (57 file, con `manifest.json`: URL, pagina, misure), più le fonti esterne in `assets/esterne/` (35 file, con `manifest.json`). Inventario completo con soggetto, qualità e larghezza massima in `_prova/inventario-immagini.json` (92 voci). Nessun `srcset`, nessun PDF o catalogo; per ogni foto il sito ha una miniatura `_p` e una grande `_b`: si è presa la grande.

| Gruppo | Quante | Misure | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Servizio fotografico 2021 sul sito (camere, reception, sala; 2 con data EXIF, 3 senza metadati, stesso stile [Probabile]) | 5 | 1200x800 | buone, professionali, luce calda | Camere, Ristorante, Home fino a 1200 px; chiedere gli originali (la fotocamera scatta 5760x3840) |
| Stesso servizio sul portale della Regione (cantinetta, camera, sala, salottino con poltrone verdi) | 4 | 1024x768 | buone; il salottino non è sul sito | spazi comuni e cantinetta fino a 1024 px |
| Fotogrammi del video "Emozioni & Sapori" | 29 + anteprima | 1920x904 (bande nere tolte) | morbidi al 100% per la compressione del video, reggono fino a circa 1400 px; piccolo marchio "Leon d'Oro" in basso a destra | aperture e fasce larghe: Colli dal drone, ciclisti in maglia gialla, sala piena, facciata di sera, cucina |
| Piatti (foto da telefono) | 10 | 3 a 2048x1536, 1 a 1600, 5 tra 750 e 960, 1 a 620 | luce piatta, piatto bianco su tovaglia; pixel sufficienti, resa da trattoria | griglia dei piatti a mezza colonna; il fegato (620 px) solo piccolo |
| Foto d'epoca | 1 + 1 | cartolina 501x402 sul sito; la stessa foto "Este - Viale di Via Restara" con l'insegna TRATTORIA AL LEON D'ORO a 3298x2196 (blog Micro Storie, riproduzione del 2010) | ottima la versione grande | storia in Home: chiedere al cliente l'originale da scansionare |
| Facciata (foto ferma) | 1 | 420x315, mostrata a 430 (già ingrandita) | scarsa, con piante coperte di brina davanti | solo piccola: per la facciata c'è il fotogramma di sera; serve una foto diurna nuova |
| Foto vecchie di sala e camere (alcune non collegate a nessuna pagina) | 7 | 800x600 | arredi superati | quasi tutte da non usare |
| Bagni | 2 | 600x800 | mediocri | piccola o niente |
| Bike, uscite di gruppo | 3 | 400x300 | piccole e vecchie | sostituite dai fotogrammi del video |
| Logo | 1 | 311x231 con foto dietro, logo utile circa 260 px | non utilizzabile come logo | ridisegnare o farsi dare il vettoriale |
| Testate con titoli in carattere gotico, fette di sfondo | 10 | 800x92 e fette | testo chiuso in immagine | non usare |
| Territorio (Este, Colli, Verona, ospedale) | 17 | 372-960 px | provenienza non dichiarata, alcune chiaramente prese dal web (Arena di Verona dall'alto) | non usare senza verificare i diritti; due cartoline d'epoca (Porta Vecchia, Via Roma) da chiedere al cliente |

Foto utilizzabili, in sintesi: **9 professionali** (fino a 1024-1200 px), **29 fotogrammi** del video (fino a circa 1400 px), **10 piatti** (3 fino a 2048 px), **1 foto d'epoca** a 3298 px. Nessuna foto ferma della facciata di giorno sopra i 420 px. Nessuna foto delle singole tipologie di camera oltre alle due del 2021.

Sul sito di oggi le foto sono mostrate quasi tutte come miniature da 210 px: tre foto da 2048 px (baccalà, pancetta, trippa) e la carbonara da 1600 px sono servite intere per essere mostrate a 210 px (spreco fino a 10 volte), mentre l'unica foto della facciata è ingrandita oltre la sua misura.

## Problemi tecnici da segnalare al cliente

Prove: screenshot in `_prova/attuale/NN-pagina-1440.png`, `-390.png` e `-390-schermo.png` (quello che vede il telefono), misure in `_prova/attuale/misure-screenshot.json` e `_prova/attuale/rete/misure.json` (dettaglio di ogni richiesta).

1. **Telefono.** Nessuna `<meta name="viewport">` in nessuna delle 16 pagine. A 390 px `document.documentElement.scrollWidth` vale **980**: il telefono rimpicciolisce il blocco da 800 px e il testo (Verdana 12 px) diventa di **4,8 px** effettivi. Si legge solo ingrandendo e scorrendo di lato (`01-home-390-schermo.png`). [Certo]
2. **Testo nascosto in una scatola.** Il contenuto di ogni pagina sta in un riquadro di 463x614 px con scorrimento interno (`.scroll {overflow:auto}`): nella pagina Ristorante sono nascosti 1976 px su 2590 (76%, tutto il menu), in Cosa visitare il 66%, nel Bike hotel il 48%, in Home il 35%. Sul telefono diventa uno scorrimento dentro lo scorrimento. [Certo]
3. **Impaginazione del 2014.** XHTML 1.0 Transitional, da 6 a 12 tabelle annidate per pagina, attributi `bgcolor`, `align`, `border`; foglio di stile del 18/11/2014; jQuery 1.10.2 e Lightbox 2.6 (2013); nessun attributo `lang`. Nessun CMS: ogni modifica richiede di toccare l'HTML a mano. Server Apache su hosting condiviso Shellrent (web500.shellrent.com). [Certo]
4. **Peso e richieste** (rete di Playwright, 6/10/2026):

   | Pagina | Richieste | Peso | Evento load |
   |---|---|---|---|
   | Home 1440 | 52-54 | **10,0 MB** (9,5 MB da Facebook, di cui 7,5 MB il file del video, scaricato senza che nessuno lo avvii) | 4,5 s |
   | Home 390 | 53-56 | 1,1-1,2 MB in due prove, 10,1 MB in una | 4,9 s |
   | Ristorante | 32 | 1,8 MB (foto da 2048 px mostrate a 210) | 2,1-2,4 s |
   | Cosa visitare | 35 | 1,9 MB | 2,0-2,4 s |
   | Dove siamo | 54-55 | 1,4-1,5 MB (40 richieste a Google Maps) | 1,1-1,8 s |
   | Camere, Bike, Ospedale, Prenotazioni | 15-23 | 0,3-0,8 MB | 1,1-2,5 s |

   Tempo di prima risposta del server 0,2-0,9 s. I tempi sono misurati da un datacenter attraverso un proxy: valgono come ordine di grandezza. [Certo per pesi e richieste]
5. **HTTPS.** Funziona: certificato Let's Encrypt `*.leondoroeste.it` valido fino al 6/12/2026, HSTS attivo, `http://` reindirizza a `https://`. Però `leondoroeste.it` senza www risponde 200 con le stesse pagine invece di reindirizzare a `www`: due copie del sito. [Certo]
6. **Link rotti o superati.** Museo Nazionale Atestino `http://www.atestino.beniculturali.it/`: il dominio non esiste più (DNS NXDOMAIN). Atestina Superbike `http://www.atestinasuperbike.it/`: dominio parcheggiato (parkingcrew). Transeuganea `euganeo.org/2009/08/transeuganea-classic/`: 401. Orari della navetta per l'ospedale `fsbusitalia.it/.../VNT-orari-Schiavonia.pdf`: 404. Ciclovia E2 `venetostrade.it/.../e2.html`: rimanda alla home di Veneto Strade. Ufficio IAT `comune.este.pd.it/amministrazione/ufficio.php?ID=35`: oggi apre una pagina generica del portale MyPortal. [Certo]
7. **Errori in console.** Dove siamo: `ReferenceError: showMap is not defined` e `GUnload is not defined` a ogni apertura e chiusura (resti del vecchio codice Google Maps v2 nel `<body onload>`). [Certo]
8. **Immagini.** 70 immagini di contenuto su 72 senza testo alternativo. L'unica foto della facciata (420 px) è mostrata a 430 px. Miniature da 210 px che scaricano file da 2048 px. La testata della pagina Ospedale dice "Prenotazioni" e quella dell'Informativa "Benvenuti" (fette riciclate). [Certo]
9. **Testi chiusi in immagini.** I titoli di tutte le pagine ("Benvenuti", "Le Camere", "La Cucina", "Sport e Tempo Libero", "Cosa Visitare", "Prenotazioni", "Dove Siamo") sono immagini in carattere gotico; il logo è un'immagine. Nessuna pagina ha un `<h1>`: Google e i lettori di schermo non trovano il titolo. [Certo]
10. **Leggibilità.** Testo grigio #666 su fondo #D9D2CB: contrasto **3,84:1**, sotto il minimo di 4,5:1 per il testo normale. [Certo]
11. **Contenuti fermi.** Nessun copyright né anno a piè di pagina. Sei pagine su nove ferme al 6/7/2022. "Nuovo polo ospedaliero" dal 2014; "prossima apertura del casello Valdastico sud" (aperto il 31/8/2015, fonte Il Post, 1/9/2015); la pagina camere dice "l'Ospedale di Este si trova a soli 400m", mentre la pagina ospedale dello stesso sito spiega che dal 5/11/2014 il polo è a Schiavonia; listino inglese "2023" contro italiano "2026"; inglese "free public parking", italiano "parcheggio pubblico". Mappa incorporata nel 2018. [Certo]
12. **Dati obbligatori.** La P.IVA c'è in ogni pagina. Mancano la ragione sociale completa (si legge solo "Albergo Ristorante "Leon d'Oro"", non "S.n.c. di Rubini Rodolfo & C."), la sede legale come tale e il numero REA PD-369167, che l'art. 2250 c.c. chiede anche sul sito alle società iscritte al Registro Imprese. Manca il **CIN** IT028037A1GWJ7NDDS, che l'art. 13-ter del D.L. 145/2023 chiede di indicare in ogni annuncio della struttura [Probabile che valga anche per il sito proprio; DA CONFERMARE con il consulente del cliente]. [Certo per l'assenza]
13. **Privacy e cookie.** Il banner c'è solo in home (lo script `cookiechoices.js` non è nelle altre pagine), offre solo "Chiudi ed accetta" e dice "Se decidi di continuare la navigazione accetta il loro uso": niente rifiuto, niente scelta. Prima di qualsiasi clic la home fa 32 richieste a Facebook e Dove siamo 40 a Google. L'informativa cita il D.Lgs 196/2003 e il GDPR ma è un modello per negozi online ("Al momento dell'ordine il sito rileva automaticamente [...] i dati per il destinatario dei prodotti"), afferma che "Con l'uso o la consultazione del presente sito i visitatori [...] approvano esplicitamente la presente privacy policy" e indica come titolare una persona ("Giulio Rubini") invece della società. Nessuna nota privacy vicino all'invito a scrivere per prenotare. [Certo]
14. **Prenotazione.** Solo "scrivete una email": nessun modulo, nessuna data, nessun pulsante. Su Google la scheda dell'albergo mostra tre offerte, tutte di portali (Booking.com, Super.com, Bluepillow.com, 84-85 USD per la notte del 14/10/2026), e nessuna del sito ufficiale; sulla scheda compare anche "Rivendica questa attività" [Probabile: scheda non gestita dal titolare, DA CONFERMARE]. [Certo, Google, 6/10/2026]
15. **SEO di base.** Titoli e descrizioni ci sono e sono specifici, ma: nessun `h1`, nessuna sitemap, nessun `robots.txt`, nessun `hreflang` tra italiano e inglese, host con e senza www duplicati, refuso nel titolo ("Albero per ospedale unico"). [Certo]

Nota sulle misure: durante le prove la connessione con il server si è chiusa spesso (risposte 502 dal proxy, circa una pagina su tre al primo tentativo). Non è stato possibile capire se dipenda dal server o dal tunnel di prova, quindi **non va segnalato al cliente**; gli screenshot finali sono stati presi ripetendo le richieste fallite.

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Albergo Ristorante Leon d'Oro S.n.c. di Rubini Rodolfo & C. | [Certo] aziende.it (scheda aggiornata al 5/7/2026, copia in `_prova/crawl/esterne/aziende-it.html`); ufficiocamerale.it (titolo della scheda) |
| Forma giuridica | Società in nome collettivo, attiva | [Certo] aziende.it |
| P.IVA e codice fiscale | 04185510288 | [Certo] sito (ogni pagina), aziende.it |
| REA | PD-369167, CCIAA di Padova, iscrizione 01/03/2007 | [Certo] aziende.it |
| ATECO | 55.1 Alberghi e strutture simili | [Certo] aziende.it |
| Dipendenti | 8 nel 2023 (aziende.it); 9 nel 2025 secondo ufficiocamerale.it | [Certo] per le fonti; numero attuale [DA CONFERMARE], non usarlo nel sito |
| Codice SDI | XL13LG4 | [Certo] aziende.it |
| Sede | Viale Fiume 20, 35042 Este (PD) | [Certo] sito, Regione, Google |
| Coordinate | 45.2267456, 11.6543665 | [Certo] Google |
| CIN | IT028037A1GWJ7NDDS | [Certo] Regione Veneto (dati.veneto.it e Veneto Around Me) |
| Classificazione | albergo 2 stelle, 13 camere, 24 posti letto | [Certo] Regione Veneto, open data CC BY 4.0, 6/10/2026 |
| Telefono | 0429 602949 | [Certo] sito, Google |
| Secondo numero | 0429 2955 | [Certo] Regione (come "mobile") e blog Micro Storie (2015) [DA CONFERMARE se attivo] |
| Fax | 0429 3072 | [Certo] sito, Regione |
| Email | prenotazioni@leondoroeste.it | [Certo] sito |
| Seconda email | albergo.leondoro@virgilio.it | [Certo] Regione Veneto [DA CONFERMARE se ancora letta] |
| PEC | **non trovata in chiaro**. Esiste: ufficiocamerale.it la riporta ma la nasconde dietro protezione anti-bot (pagina 403, nei risultati di ricerca appare offuscata) | da recuperare su INI-PEC (inipec.gov.it, ricerca per P.IVA, gratuita) [DA CONFERMARE] |
| Titolari | fratelli Lorenzo e Giulio Rubini, eredi di Rodolfo; in cucina la madre Annalisa Brugin | [Certo] Regione Veneto e blog Micro Storie (2015); attualità [DA CONFERMARE] |
| Titolare del trattamento dati (sul sito) | Giulio Rubini | [Certo] informativa |
| Anni di attività | trattoria con alloggio dai primi del Novecento; famiglia Rubini dagli anni '50; Rodolfo dal 1976/77; società attuale dal 2007 | [Certo] sito, Regione, aziende.it. Non scrivere "dal 1900": l'anno preciso non c'è |
| Chiusura | ristorante chiuso la domenica | [Certo] sito |
| Orari | non pubblicati (né sul sito né su Google) | [DA CONFERMARE] |
| Recensioni | Google 4,4 su 531 recensioni; categorie "Ristorante veneziano, Hotel, Ristorante italiano, Ristorante di pesce" | [Certo] Google, 6/10/2026 (solo per noi: il nuovo sito non riporta voti) |
| Portali | Booking.com (hotel 1551306), Tripadvisor, Kayak e altri aggregatori | [Certo] Google |
| Canali social | facebook.com/albergoleondoroeste, instagram.com/albergoristoranteleondoro | [Certo] sito; contenuti non leggibili senza login |
| Certificazioni, marchi, premi | nessuno dichiarato | [Certo] nessuna fonte |
| Dominio e posta | sito su Shellrent, posta su server Shellrent (serverlet.com) | [Certo] DNS |

## URL vecchi (per `plugin/redirect-301.csv`)

Pagine (tutte rispondono 200 oggi):
```
/
/index.html
/camere-e-stanze-colli-euganei.html
/ristorante-cucina-tipica-veneta.html
/mtb-bike-hotel-colli-euganei.html
/albergo-per-ospedale-unico-monselice.html
/dove-dormire-e-cosa-visitare-este.html
/prenotazione-camera-este-colli-euganei.html
/dovesiamo-colli-euganei.html
/informativa-cookie.html
/en_index.html
/en_hotel-rooms-euganean-hills.html
/en_restaurant-typical-venetian-cuisine.html
/en_mtb-bike-hotel-euganean-hills.html
/en_sights-in-este.html
/en_booking-hotel-este-euganean-hills.html
/en_where-we-are-euganean-hills.html
```
Host: `https://leondoroeste.it/*` va reindirizzato a `https://www.leondoroeste.it/*`.

Cartelle con foto che Google può avere indicizzato: `/foto/*.jpg` (46 file), `/images/*.jpg` (48 file, quasi tutte fette di impaginazione). Basta un reindirizzamento generico verso la pagina corrispondente o la home.

## Limiti dell'analisi

- Wayback Machine non raggiungibile da qui (web.archive.org chiude la connessione, archive.org risponde 429). archive.org conferma che esiste una copia del 13/05/2024. Le foto del sito attuale sono comunque già le versioni grandi (1200 px).
- Facebook e Instagram chiedono il login: del canale Facebook si è letto solo il video incorporato nella home. Booking blocca i programmi automatici. Le foto della scheda Google visibili senza login sono di utenti, non del titolare, e non sono state scaricate.
- Fonti esterne usate: dati.veneto.it (elenco strutture ricettive, CC BY 4.0), venetoaroundme.regione.veneto.it/it/dove-dormire/albergo-leon-d-oro, microstoriecommercio.wordpress.com/2015/02/09/este-albergo-ristorante-leon-doro/, aziende.it/albergo-ristorante-leon-d-oro-s-n-c-di-rubini-rodolfo-c, ufficiocamerale.it/9413/albergo-ristorante-leon-doro-snc-di-rubini-rodolfo-c (solo il titolo nei risultati di ricerca), Google Maps (place_id ChIJCcy3Yfsdf0cRFKt0dSfofGs), Il Post 1/9/2015 (Valdastico sud).
