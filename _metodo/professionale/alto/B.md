# B: i concorrenti di fascia alta (botteghe, negozi, cibo, vivai e piccole fabbriche che vendono anche al banco)

Ricerca del 3 novembre 2026. Undici aziende del gruppo, 21 siti visitati e analizzati sul loro dominio.

Come ho lavorato:
- il mestiere preciso di ogni azienda viene da `01-analisi.md` e `LEGGIMI.md` della sua cartella;
- le nostre home rifatte le ho guardate in `screenshot/home/` (prima schermata a 1440 e pagina intera) e ho contato immagini e sezioni nei `sito/index.html`;
- per ogni concorrente ci sono tre schermate in `alto/B/`, JPEG qualità 70, densità 1:
  - `<sito>-1440.jpg`: prima schermata 1440x900;
  - `<sito>-1440-intera.jpg`: pagina intera, tagliata a 9000 px;
  - `<sito>-390.jpg`: prima schermata 390x844.
- Famiglie, corpi, pesi e interlinee sono letti dal DOM con uno script (il carattere più usato, i corpi più frequenti, h1, h2, p e link del menu), non a occhio. Le quote di spazio della foto sono misurate sulle schermate.
- Banner dei cookie e porte dell'età chiusi dove si poteva. Restano nelle schermate, perché sono quello che vede chi arriva: il popup della newsletter di Serax (pagina intera), di Crockett & Jones (1440 e 390) e di Tricker's (390), la chat di Serax, la barra della regione di Crockett & Jones.
- Tre siti hanno parti vuote nella pagina intera perché caricano il contenuto con video o con lo scorrimento: il cursore d'apertura di Lorenz von Ehren (vuoto alla cattura), le recensioni di Bisca, il video centrale di Fuller Moto. Lo dico nella scheda.

Siti scartati dopo la visita o non raggiungibili:
- non raggiungibili dal container (connessione rifiutata o 502): Mascioni (biancheria per hotel), John Jones (corniciai e belle arti, Londra), Siller Treppen (scale, Alto Adige), Luxardo (firewall Sucuri in timeout), Hookie Co, Shaw Speed & Custom, Wrenchmonkees, Kingston Custom, Cherry's Company (officine custom), WJ Fisser (forniture per hotel, Amburgo);
- fermi su un controllo anti-robot o un rifiuto: Gravurmanufaktur Werré (incisori dal 1914, Mannheim), Kremer Pigmente, Fabbri 1905 (403), Libeco (429);
- visitati e scartati:
  - Forno Brisa e Davide Longoni: buoni panifici, ma Brisa apre con una frase gialla su bianco senza pane e Longoni con un banner promozionale affollato; Tartine e Hart fanno lo stesso lavoro meglio;
  - Bonci: pizza al taglio, non panificio di quartiere;
  - Busatti: l'apertura mostra la parola "Home" su un riquadro grigio;
  - Frette e Society Limonta: aprono con un popup o con un video grigio, sono marchi di moda casa più che fornitori;
  - Neumeier (progettisti di hotel, Monaco): la home si carica senza fogli di stile;
  - Zecchi (colori per artisti, Firenze) e Varnelli (liquori): impaginazioni degli anni 2000;
  - Fontanot (scale): in home c'è un testo di spam su un casinò online, il sito è compromesso;
  - Kenngott (scale): apre con un'illustrazione 3D di repertorio;
  - Fratelli Rossetti: la home resta nera con il solo piede, il resto non si carica;
  - Thunderbike: concessionaria Harley con la home da negozio a banner; Deus Ex Machina: marchio di abbigliamento; Zero Engineering: sito fermo da anni;
  - Carmina e Schladerer: la pagina non scorre oltre la prima schermata;
  - Stempel Schmidt (timbri, Bamberga): mestiere giusto, ma sito da modello sotto il livello che cerchiamo.

Una premessa. In due mestieri del gruppo non ho trovato un concorrente vero con un sito curato e raggiungibile: il distributore e progettista per l'ospitalità (Foralberg) e il laboratorio di timbri e targhe (San Marco Timbri). Il settore comunica con portali e cataloghi. Per Foralberg ho preso un negozio di attrezzi per cuochi professionisti dal 1908 (Kama-Asa) e un fornitore di tavola che serve anche i ristoranti (Serax); per San Marco un laboratorio di timbri di famiglia (The English Stamp Company). Lo dico nella scheda.

---

## 1. Le nostre aziende: i concorrenti scelti e che cosa fanno che noi non facciamo

Prima tre cose che valgono per tutte le undici home.

1. **Sono lunghe il doppio.** Le nostre vanno da 5.600 px (Nic Dean) a 10.600 px (Overdrive), con 5-9 sezioni piene (e ognuna con 3-6 blocchi dentro). La mediana dei 21 concorrenti è 5.800 px, e i tre migliori stanno sotto: Plain English 2.300 px, Hart una schermata sola, Cornelissen 1.700 px.
2. **Si aprono tutte allo stesso modo.** Titolo grande a sinistra, foto a destra in un riquadro (da un quarto a metà della schermata), due o più bottoni, sotto una fila di ingressi o le schede dei negozi. Dei 21 concorrenti, 14 aprono con una foto a tutta larghezza o quasi (oltre il 65% della prima schermata) e con al massimo tre cose sopra: un nome, una riga, un'azione. Nessuno mette in apertura orari, indirizzi e telefoni di due sedi insieme.
3. **Nessun concorrente ha la fascia delle cifre grandi.** Noi l'abbiamo in tutte e undici le home (1963 / 30+ / 2 / 60 / 400; 5 giorni / 2-6 settimane / 150 kg / 306; 40 / 2 / 22 / 8...). Loro i numeri li scrivono nel testo, uno per volta e con la cosa che misurano: "4.500 colori di pigmento, più di 600 pennelli" (Pigment Tokyo), "32 acri" (Architectural Plants), "più di 400 referenze" (Toschi), "oltre 600 ettari" (Lorenz von Ehren), "1.292 recensioni" (Tricker's). La fascia di cifre è la cosa che più fa "modello" nelle nostre pagine.

### Panificio Galileo Fornasiero (panificio di quartiere con laboratorio, due negozi a Camin, pasta fresca, pizze, dolci da forno, panettone a Natale, forniture a bar e ristoranti)
- **Concorrenti scelti:** Tartine (San Francisco) e Hart Bageri (Copenaghen). Sono due panetterie di laboratorio con più negozi, ordini speciali da prenotare e forniture all'ingrosso: lo stesso schema di Fornasiero, più grande. Tartine è il riferimento mondiale del pane di laboratorio; Hart ha il sito più asciutto del gruppo.
- **Il loro sito fa X che la nostra home non fa:**
  - Tartine apre con una foto a tutta pagina del laboratorio, i fornai al banco e i cestini di lievitazione, e mette le sedi come tre righe sul bordo basso della foto ("Bay Area, 4 locations"). La nostra apre con il titolo "SIAMO FORNASIERO, FORNAI ANCHE NEL NOME" e una foto della vetrina grande un quarto della schermata, sotto due schede negozio con 6 righe di orari ciascuna.
  - Tartine scrive la regola degli ordini in una riga ("special order cakes require a seven day lead time", ritiro "@ 600 Guerrero St."). Noi abbiamo la fascia "Panettone e focaccia di Natale: si prenotano", ma senza il termine per prenotare.
  - Hart tiene tutto in cinque voci (Locations, About, Contact, Pre-order, Gift cards) e tre indirizzi email distinti: richieste generali, wholesale, lavoro. La nostra home è lunga 7.300 px, con 8 sezioni e la storia, i numeri e i prodotti tutti in pagina.

### Servalli Padova (grossista e importatore di tessile casa dal 1895, Centro Grossisti di Padova, marchi propri, tappeti annodati, contract per alberghi, shop per privati dal 2022)
- **Concorrenti scelti:** Rivolta Carmignani (Macherio, dal 1867, biancheria per i grandi hotel e per la casa) e Klippan Yllefabrik (Svezia, dal 1879, coperte e plaid di lana, vende ai negozi e ai privati). Rivolta fa il contract alberghiero come Servalli; Klippan ha lo stesso doppio canale, rivenditori e shop.
- **Il loro sito fa X che la nostra home non fa:**
  - Rivolta mette in fila i loghi degli hotel serviti, con il titolo "Nei migliori hotel del mondo" (Ritz-Carlton Yacht Collection, Four Seasons Milano, Palais, Casa Cipriani New York, Bulgari Hotel Roma). La nostra sezione "Per alberghi e strutture" spiega il servizio ma non nomina un solo albergo cliente.
  - Rivolta apre con tre tessere fotografiche Letto / Tavola / Bagno con lo stesso taglio; noi apriamo "Nel negozio online" con sei righe di testo (Piumini e trapunte, Lenzuola, Bagno, Tappeti...).
  - Klippan mette "Återförsäljarportal" (portale rivenditori) in piccolo nella barra in alto, separato dallo shop, e racconta la lana con i nomi di chi la raccoglie ("Calle e Charlotte"). La nostra ha "Rivenditori" nel menu, ma la home parla ai due pubblici mescolati, con i prezzi dei piumini e le condizioni per i negozi nella stessa pagina.

### Foralberg (forniture per alberghi e ristoranti dal 1953: tavola, bar, sala, buffet, cucina, impianti, con progetto e posa; showroom di 800 m2 in via Cile; La Vetrinetta per i privati)
- **Concorrenti scelti:** Kama-Asa (Kappabashi, Tokyo, dal 1908, coltelli e attrezzi da cucina per cuochi e privati, affilatura, negozi a Tokyo, Parigi e Brooklyn) e Serax (Belgio, dal 1986, azienda di famiglia, stoviglie e tavola anche per ristoranti, con area Professionisti). Nessuno dei distributori per l'ospitalità che ho trovato ha un sito curato raggiungibile; questi due sono il negozio professionale e il fornitore di tavola più vicini.
- **Il loro sito fa X che la nostra home non fa:**
  - Kama-Asa ordina il catalogo in due modi, per tipo (santoku, deba, yanagi...) e per uso (per carne, per pesce, per pane), e mette il servizio di affilatura in una tessera grande come quella dei prodotti. La nostra "Dalla tavola alla cucina" ha sei riquadri di testo con le pagine del catalogo PDF e la progettazione arriva solo a metà pagina.
  - Kama-Asa apre con una foto vera di una mano che taglia con un nakiri, e la didascalia dice da dove viene il coltello ("Yoshikane Hamono in Sanjo, town of blacksmiths"). La nostra apertura ha la foto d'archivio del furgone OM, bellissima, ma nessuna foto di oggi: né lo showroom né un locale arredato da loro.
  - Serax firma ogni collezione con il nome di chi l'ha disegnata (Ottolenghi, Sergio Herman, Marni). Noi abbiamo i marchi in una fascia blu, ma nessun locale cliente con il nome.

### San Marco Timbri (laboratorio di timbri in gomma e metallo, targhe in ottone, incisioni laser e a fresa, insegne, premiazioni, ceralacca, via Longhin a Padova)
- **Concorrente scelto:** The English Stamp Company (Dorset, famiglia, dal 1992, timbri in gomma su misura e timbri disegnati in casa). Solo uno: il secondo candidato con un sito curato (Werré, incisori dal 1914) si ferma sul controllo anti-robot.
- **Il loro sito fa X che la nostra home non fa:**
  - In ogni foto si vede il timbro accanto alla sua impronta, su un oggetto vero: la carta da pacchi, il barattolo di marmellata con l'etichetta, il biglietto. La nostra mostra le targhe e i punzoni come oggetti, ma nessuna impronta e nessun timbro in uso.
  - Dice in una frase che cosa si può mandare per un timbro su misura: "your own logo, a drawing or illustration, handwriting, a graphic or most photos". La nostra ha il bottone "Mandaci testo o foto su WhatsApp", ma non elenca che cosa vale come file di partenza.
  - Divide l'offerta per occasione (business, matrimoni, indirizzo, conserve fatte in casa) invece che per tecnica; la nostra "Che timbro vi serve?" parte da gomma, metallo, sigilli.

### L'Artificio Battagin (negozio di belle arti con laboratorio di cornici interno e corsi Artinpratica, via della Croce Rossa, Padova)
- **Concorrenti scelti:** L. Cornelissen & Son (Londra, dal 1855, colori, pigmenti, doratura, negozio con gli arredi vittoriani) e Pigment Tokyo (Tokyo, negozio di pigmenti e materiali con workshop e consulenza). Sono negozi di belle arti di riferimento, con la stessa clientela di professionisti e appassionati.
- **Il loro sito fa X che la nostra home non fa:**
  - Cornelissen mette in home tre riquadri uguali: telefono e orari ("9:30 - 18:00, Mon - Sat"), il giro virtuale del negozio, l'indirizzo. Fine della home: 1.700 px. La nostra è lunga 8.400 px e gli orari arrivano dopo i reparti, i marchi, le cornici e i corsi.
  - Pigment Tokyo mette la parete dei pigmenti in vetro come immagine del negozio e i marchi come tessere con la foto del prodotto (Kusakabe, Kuretake, Zecchi...). Noi elenchiamo i marchi in una riga di testo serif.
  - Pigment chiama la consulenza un servizio con il suo bottone ("Shopping consultation", "Private workshop"). Noi abbiamo "Chiamaci prima di venire", che è un consiglio, non un servizio prenotabile.

### Scalarredo (scale retrattili a botola pronte e su misura, scale da interno e ringhiere su misura, negozio e magazzino a Mestrino)
- **Concorrenti scelti:** Bisca (Helmsley, North Yorkshire, scale su misura dal disegno alla posa) e Dolle (Danimarca, scale retrattili da soffitta, scale salvaspazio e botole). Bisca fa le scale su misura, Dolle le retrattili: i due mestieri di Scalarredo.
- **Il loro sito fa X che la nostra home non fa:**
  - Bisca apre con una sola foto a tutta pagina e sopra scrive il nome del lavoro e il luogo ("Ash Multiflight Stair, York") e il telefono in basso a destra. La nostra foto d'apertura è una retrattile vista dall'alto, senza dire dove è posata.
  - Bisca racconta il su misura in tre foto con lo stesso taglio: lo schizzo a matita, le scintille della saldatura, la scala posata (Design, Craft, Install). Noi lo diciamo con il testo "Scale da interno su vostro disegno" e una foto.
  - Bisca mette in fila dieci premi e accreditamenti con l'anno (Build It Awards 2018-2021, Northern Design Awards, Houzz 2017). La nostra home non ha nessun riconoscimento esterno.

### Bottega dell'Arte (falegnameria di due soci a Mestrino: arredo su misura, serramenti, restauro, anche il Palazzo del Bo)
- **Concorrenti scelti:** Plain English (Suffolk, dal 1992, cucine e armadi su misura, laboratorio a Stowupland Hall, showroom a Londra, New York, Los Angeles) e Benchmark (falegnameria inglese di arredi e allestimenti su misura, con apprendisti). Sono due laboratori di legno che lavorano su misura per privati e committenti.
- **Il loro sito fa X che la nostra home non fa:**
  - Plain English sta in 2.300 px: una foto, un manifesto di tre righe, l'elenco delle stanze in parole, sei tessere quadrate e il piede. In testata due sole azioni scritte: "View brochure" e "Make an enquiry". La nostra home è lunga 8.800 px, con i due telefoni dei soci in apertura e cinque bottoni.
  - Plain English presenta il laboratorio come un luogo da visitare ("Stowupland Hall... home to our workshops where our cupboards are still handcrafted today. Visit us"). Noi mostriamo il capannone di via Levico con il furgone in fondo alla pagina, ma come indirizzo, non come invito.
  - Benchmark mette i soci e i ragazzi di bottega in una foto in bianco e nero ("A legacy of making, apprenticeships"). Nella nostra home ci sono 13 immagini e nessuna mostra Mauro o Giuliano.

### Distilleria Rizzi (liquorificio dal 1926: liquori e amari con etichette storiche, sciroppi e aromi per la pasticceria professionale, spaccio per i privati, Mestrino)
- **Concorrenti scelti:** Toschi (Vignola, dal 1945, amarene, sciroppi, liquori e preparati per bar, gelateria e pasticceria) e Nardini (Bassano del Grappa, dal 1779, grappa e liquori, visite guidate). Toschi fa lo stesso lavoro per i professionisti della pasticceria; Nardini è la casa storica veneta che fa anche liquori.
- **Il loro sito fa X che la nostra home non fa:**
  - Toschi divide la home per mestiere del cliente, ognuno con il suo blocco di colore e il suo bottone: Bar e ristorazione (bianco), Gelateria (azzurro), Pasticceria (giallo), sotto il titolo "Per i professionisti". La nostra mette in fila spaccio, liquori, pasticceria e festa dei 100 anni con lo stesso peso.
  - Toschi apre con il frutteto delle amarene in fiore a tutta pagina, cioè la materia prima, senza testo. La nostra apre con il rosso pieno, la firma e una foto dello spaccio addobbato per Natale.
  - Nardini usa le incisioni dell'archivio (il Ponte Vecchio, la tavola dei bevitori) come immagini di sezione e mette le visite guidate in home con il loro invito. Rizzi ha le etichette storiche e il marchio del leone "dal 1850", ma in home sono solo foto di bottiglie una accanto all'altra.

### Overdrive Customs (officina Harley-Davidson e giapponesi custom di Matteo, a Vigonovo, e costruzione di special da concorso)
- **Concorrenti scelti:** Fuller Moto (Atlanta, officina e costruttore di special di Bryan Fuller) e Old Empire Motorcycles (Regno Unito, special fatte a mano, ricambi e abbigliamento). Due costruttori di special con il nome del titolare o del marchio al centro.
- **Il loro sito fa X che la nostra home non fa:**
  - Fuller apre con una sola special a tutta pagina, il suo nome ("THE RAPTOR T"), una riga e un bottone "Inside the build" che porta alla storia di quel lavoro. La nostra apre con il titolo "OFFICINA HARLEY-DAVIDSON E CUSTOM GIAPPONESI", due bottoni e la foto di Matteo, e le special hanno nome (Hagane, Drakkar) ma non una pagina ciascuna.
  - Fuller elenca le lavorazioni fatte in casa in cinque parole (paint, upholstery, metal fabrication, CAD design, 3D printing). La nostra elenca i servizi d'officina, ma non dice che cosa si fa a mano in casa sulle special.
  - Old Empire mette la lista dei premi con evento e anno (Salon Privé 2014, Malle Mile 2015 Best of Show, Verona 2017). Noi l'abbiamo già, in tabella: è la cosa più "da studio" della nostra home e va tenuta.

### Bordin Garden & Vivai (vivaio di produzione dal 1955, garden center a piramide dal 1996, progetto e realizzazione di giardini, Saonara)
- **Concorrenti scelti:** Architectural Plants (Pulborough, West Sussex, vivaio dal 1990, 32 acri, aperto a privati e professionisti, progettazione di giardini) e Lorenz von Ehren (Amburgo, vivaio dal 1865, alberi grandi ed esemplari unici, giardini espositivi in Germania). Sono vivai di produzione che vendono a privati e a professionisti e fanno giardini.
- **Il loro sito fa X che la nostra home non fa:**
  - Architectural Plants fa prenotare la visita al vivaio ("Book a visit", primo bottone in testata) e mette in testa l'elenco completo delle piante in vendita ("View our complete stock list"). La nostra ha "Vivai, esemplari in zolla" come riga, senza l'elenco di quello che c'è.
  - Architectural Plants spiega come arrivare con parole precise ("next to the Brinsbury campus of Chichester College, on the west side of the A29, 2.7 miles north of Pulborough"), dice che i cani sono benvenuti e che ci sono due sedie a rotelle. Noi diamo l'indirizzo e il bottone "Indicazioni".
  - Lorenz von Ehren mette cinque persone del vivaio con nome, ruolo e albero preferito ("Kollegen und ihre Lieblingsbäume") e una regola chiara per i privati (sotto i 750 euro netti si passa al garden center). Bordin ha la terza generazione e due sedi per due pubblici, ma nessun volto e nessuna regola su chi va dove.

### Nic Dean (calzaturificio della famiglia Nicoletto dal 1975, scarpe medio-fini per negozi europei e americani, spaccio di fabbrica a Villatora dal 2013; attenzione: i registri dicono che oggi la srl affitta immobili, va verificato se lo spaccio è aperto)
- **Concorrenti scelti:** Tricker's (Northampton, dal 1829, calzaturificio di famiglia, negozi a Londra, Tokyo, Shanghai) e Crockett & Jones (Northampton, calzaturificio di famiglia). Fabbriche di scarpe che vendono ai negozi e direttamente.
- **Il loro sito fa X che la nostra home non fa:**
  - Tricker's ha un blocco "Northampton through & through" con la foto degli operai al banco e la frase "every shoe and boot is made from start to finish in our Northampton factory". La nostra dice "Calzature prodotte interamente in azienda" su un fondo rosso, senza una foto della fabbrica o di chi ci lavora.
  - Tricker's mostra i negozi con la foto della facciata e l'anno ("Our flagship store on Jermyn Street... since 1938"). Il nostro spaccio di via Lombardia ha orari e indirizzo, ma nessuna foto dell'ingresso.
  - Crockett & Jones dà a ogni modello un nome e la pelle con cui è fatto ("VAIL, Dark Brown Reverse Butt Suede"). Le nostre schede dicono "Tronchetto nero con tacco largo", senza nome del modello.

---

## 2. Le schede dei 21 siti

Ordine: panifici, tessile casa, forniture per la tavola, timbri, belle arti, scale, falegnami, liquori, officine moto, vivai, calzaturifici.

### Tartine: tartinebakery.com
- **Che cosa fa:** panetteria e pasticceria di laboratorio nata a San Francisco (600 Guerrero St.), oggi 4 sedi nella Bay Area, 7 a Los Angeles, 8 in Corea; ordini speciali, spedizioni nazionali, libri.
- **Prima schermata:** barra di 30 px "Click here to pre-order your holiday pastry and pies"; testata bianca con due voci a sinistra (Locations, About us), il logotipo TARTINE spaziato al centro, "National shipping" e il bottone ocra "ORDER" a destra. Sotto, la foto occupa circa il 90% della schermata: il laboratorio sfocato, una fornaia in grembiule, i cestini di lievitazione in primo piano, scurita. Sopra, a sinistra, "Welcome to Tartine" (40 px) e una riga; sul bordo basso le tre sedi con il numero di negozi e una freccia. In tutto 8 elementi. A 390: barra, logotipo e bottone ORDER, la foto piena con il titolo in basso.
- **Struttura della home:** apertura; "Tartine Happenings" (due foto piccole, lavora con noi e spedizioni); torte su ordinazione e torte da prenotare (due foto, due link lunghi in maiuscolo con l'indirizzo di ritiro); buoni regalo con la facciata blu della bottega; video "Inside Stories, Chapter 3"; "Who we are" con le mani nell'impasto; citazione di Vogue in grande; i libri (Tartine Bread); griglia di foto (tre piatti e una foto larga di due fornaie al banco); piede. 8.200 px.
- **Fotografia:** servizio vero, sempre lo stesso fotografo e la stessa luce calda di finestra; persone che lavorano senza guardare l'obiettivo, prodotti dall'alto, la facciata. Circa 25 foto, tre formati (orizzontale largo, 4:3, quadrato).
- **Tipografia:** una sola famiglia, PitchSans, un monospaziato da macchina da scrivere, usato per tutto. Titolo d'apertura 40/48 px peso 500, titoli di sezione 32/30 px peso 600, testo 18/28 px con spaziatura di 1,5 px, link 14 px. Corpi distinti: 9. Maiuscole spaziate solo per etichette e link.
- **Colori:** bianco e un bianco caldo per le fasce, nero per il testo, ocra per il solo bottone ORDER, bruno rossiccio per il motto del piede ("Rise each day. Warm every table.").
- **Griglia e margini:** contenitore di circa 1180 px centrato, margini di 120-130 px; blocchi alternati testo e foto con molto bianco (120-160 px tra le sezioni).
- **Dettagli da studio:** un carattere solo, con una voce precisa; la regola dell'ordine scritta per intero ("seven day lead time"); l'indirizzo di ritiro dentro il link; nessuna cifra grande, nessuna icona, nessun bottone secondario oltre ai due link contornati. Il motto in piede, non in apertura.
- **Prove:** la citazione di Vogue con la fonte, i libri pubblicati, il numero di sedi per città.
- **Contatto:** "Locations" in testata (pagina per ogni sede), tre email nel piede (info, manufactory, press).
- **Che cosa si trasferisce:** la regola degli ordini in una riga con il termine e il luogo di ritiro (Fornasiero: panettone da prenotare entro una data, ritiro in via Vigonovese); le sedi come righe brevi sul bordo della foto invece di due schede piene di orari; un carattere solo con carattere per tutta la pagina. **Che cosa no:** la foto sfocata e scurita funziona perché dietro c'è un servizio intero; con le poche foto di Fornasiero una foto sfocata sembra un errore. Il monospaziato da solo è una scelta di marchio, non una regola: per un forno di quartiere veneto va scelto un carattere che c'entri con l'insegna di legno.

### Hart Bageri: hartbageri.com
- **Che cosa fa:** panetteria di Copenaghen (società Fresh Out The Oven ApS), più negozi in città, pre-ordini, buoni regalo, forniture all'ingrosso.
- **Prima schermata:** un video a tutta pagina (100%) dell'insegna dipinta HART BAGERI sulla facciata blu. In alto a sinistra il logotipo HART bianco, a destra cinque voci in maiuscolo (Locations, About, Contact, Pre-order, Gift cards) e il sacchetto. In basso il piede è già dentro la schermata (copyright, privacy, cookie, "Smiley report", il rapporto dell'ispezione sanitaria danese). Nessun titolo, nessun bottone. A 390: la foto della porta del negozio con una persona che esce, "Open every day" in basso.
- **Struttura della home:** una sola schermata. Il resto (sedi, contatti) è in pannelli: "General enquiries", "Hiring", "Wholesale", "FAQ", ognuno con il suo indirizzo email.
- **Fotografia:** video vero della bottega, girato in strada; nessuna foto di prodotto in home.
- **Tipografia:** Basel Grotesk Mono (menu 14 px maiuscolo, peso 535) e Graphik per i testi. Corpi: 10-17 px, nessun titolo.
- **Colori:** quelli della facciata (blu notte, mattone, bianco dell'insegna); fondo #0b0b0b.
- **Griglia e margini:** margini di 16 px, testata e piede sullo stesso filo.
- **Dettagli da studio:** la home è l'insegna. Tre email per tre pubblici. Il rapporto dell'ispezione igienica linkato nel piede come una prova.
- **Prove:** nessuna in home oltre all'ispezione sanitaria.
- **Contatto:** email divise per tipo di richiesta.
- **Che cosa si trasferisce:** le richieste divise per tipo con il loro indirizzo (Fornasiero: "Per bar e ristoranti" con il suo numero o la sua email, separato dal banco); l'insegna come immagine d'apertura (Fornasiero ha l'insegna di legno "FORNASIERO Galileo"). **Che cosa no:** la home di sola immagine regge per un marchio già famoso; per un forno di Camin serve che la prima schermata dica anche orari e indirizzo. Il video non c'è e non va finto.

### Rivolta Carmignani: rivoltacarmignani.com
- **Che cosa fa:** manifattura di biancheria di lusso dal 1867 a Macherio (Monza): letto, tavola, bagno, tessuti jacquard prodotti in casa, forniture per i grandi hotel e i ristoranti, atelier su misura, negozio online.
- **Prima schermata:** testata beige di 48 px con il leone a sinistra e sei voci centrate in maiuscolo spaziato (12 px, spaziatura 6 px: Dal 1867, Atelier, Ispirazioni, E-boutique, Collezioni, Progetti). Sotto, un video largo tutta la pagina e alto circa il 70% della schermata: una cameriera che stende un lenzuolo bianco sul balcone, sfocato, con il leone e "RIVOLTA CARMIGNANI 1867" al centro. Sotto il video il titolo "LO STILE ITALIANO CHE DURA NEL TEMPO" (40/60 px, peso 400, maiuscolo, spaziatura 4 px) e l'inizio del testo. 5 elementi.
- **Struttura della home:** video; manifesto; tre tessere Letto, Tavola, Bagno con l'etichetta in un riquadro bianco semitrasparente; "Un comfort in continuo rinnovamento" con due foto d'archivio in bianco e nero (la sarta alla macchina); collezione "Giardino italiano" in un cursore (macro del jacquard); "I nostri progetti" con quattro foto di camere d'hotel; "Nei migliori hotel del mondo" con cinque loghi; Coburg; "La cura dei tuoi prodotti"; "Entra in atelier" con un collage (rocchetti, mani che cuciono); le collezioni; piede. Oltre 9.000 px.
- **Fotografia:** tre famiglie: ambienti d'hotel fotografati da professionisti, archivio in bianco e nero, macro dei tessuti. Circa 76 immagini.
- **Tipografia:** una sola famiglia, Montserrat. Titoli 40 px peso 400 maiuscoli spaziati, testo 15/30 px peso 300, menu 12 px. Corpi distinti: 11. Il testo a 15 px peso 300 grigio si legge male.
- **Colori:** bianco caldo #f9f8f7, beige della testata, grigio scuro, un oro nei filetti.
- **Griglia e margini:** testo in colonna stretta con margini di 80 px; foto anche a filo pagina; collage sfalsati.
- **Dettagli da studio:** il titolo "Nei migliori hotel del mondo" tra due filetti; le etichette Letto, Tavola, Bagno; l'archivio usato come prova di mestiere, non come nostalgia.
- **Prove:** i loghi degli hotel con il nome (Ritz-Carlton Yacht Collection, Four Seasons Milano, Palais, Casa Cipriani New York, Bulgari Hotel Roma), "unico produttore italiano con un processo integrato", 150 anni.
- **Contatto:** icone in testata, pagine Progetti e Atelier; nessun telefono in home.
- **Che cosa si trasferisce:** la fila dei clienti alberghieri con il nome (Servalli: solo quelli che si possono nominare); l'archivio in bianco e nero come racconto di lavoro (Servalli ha i telai jacquard, la 500 Giardiniera del 1967, la tessitrice in Persia fotografata da Franco Servalli); tre ingressi fotografici per i tre usi. **Che cosa no:** il video e gli ambienti d'hotel servono un servizio che Servalli non ha; il testo sottile a 15 px; i loghi senza il permesso dei clienti.

### Klippan Yllefabrik: klippanyllefabrik.se
- **Che cosa fa:** lanificio di Klippan (Svezia), dal 1879, coperte, plaid, cuscini e borse in materiali naturali; vende online e ai rivenditori.
- **Prima schermata:** barra grigia con le promesse di consegna; riga sottile con Designers, Återförsäljarportal (portale rivenditori), Press; logotipo KLIPPAN al centro e otto voci in maiuscolo spaziato. La foto è a tutta pagina (100%): una donna con il plaid arancio e azzurro davanti al camino. Al centro un occhiello spaziato, "HÖSTENS NYA MÖNSTER" (34 px) e un bottone ruggine. 6 elementi.
- **Struttura della home:** apertura; i cinque plaid più venduti, scontornati su bianco, con prezzo e pallini dei colori; quattro tessere fotografiche 2x2 (coperte, plaid, una collaborazione con un'artista, una con un marchio); bambini; video; William Morris; cuscini e borse; "Leverantörer av svensk ull" con la lana raccolta da due persone nominate; la cesta di lana; "140 års kunskap"; piede. 6.700 px.
- **Fotografia:** servizio vero di stagione, luce calda d'interno e luce fredda di mare, persone con i plaid; prodotti scontornati per il negozio.
- **Tipografia:** Source Sans Pro sola. Titoli 30-40 px maiuscoli peso 400, testo 13-15 px, etichette 14 px con spaziatura 4 px. Testo troppo piccolo.
- **Colori:** bianco, grigio della barra, il ruggine del bottone preso dai plaid.
- **Griglia e margini:** tessere a filo, senza spazi, con il testo centrato sopra la foto.
- **Dettagli da studio:** il portale rivenditori in piccolo, dove lo cerca chi lo conosce; la lana con il nome di chi la raccoglie e la "tracciabilità completa".
- **Prove:** 1879, i nomi dei fornitori di lana, le collaborazioni con il nome.
- **Contatto:** "Kontakt" nel piede, email e telefono nella riga legale.
- **Che cosa si trasferisce:** il canale per i rivenditori come link discreto in alto; la materia prima raccontata con nomi e luoghi (Servalli: i tappeti importati direttamente dagli anni 70, la tessitrice in Persia). **Che cosa no:** le foto di moda con le modelle; i corpi di 13 px.

### Kama-Asa: kama-asa.co.jp
- **Che cosa fa:** negozio di attrezzi da cucina a Kappabashi, Tokyo, dal 1908: coltelli, padelle di ferro, griglie, attrezzi per cuochi professionisti e privati; affilatura; negozi a Kappabashi, Parigi e Brooklyn; noleggio della cucina.
- **Prima schermata:** barra nera con un avviso (siti falsi che imitano il marchio); testata bianca con il logo a sinistra e il menu in quattro gruppi con una piccola etichetta sopra ciascuno (Online store / Services, About, Contents, Online store). Sotto, un cursore a tutta larghezza alto circa il 60% della schermata: una mano che taglia una zucca con un nakiri, la didascalia "YOSHIKANE HAMONO in Sanjo, Town of blacksmiths" e una pillola bianca "Nakiri knife built for a chef's precision". 7 elementi. A 390: sotto la testata una fila di linguette che scorrono di lato (Top, Knives, Kitchen utensils, Knife sharpening).
- **Struttura della home:** cursore; tre "kitchen essentials"; notizie con la data; prodotti propri in un cursore; negozio con due linguette (coltelli, attrezzi) e dentro le categorie per tipo e per uso, ognuna con un disegno al tratto; il giornale (storie di artigiani, di clienti, del personale, la nota dell'amministratore); l'enciclopedia degli attrezzi; quattro tessere grandi (coltelli, attrezzi, servizio di affilatura, chi siamo con la facciata del negozio); i tre negozi con la foto; noleggio della cucina; Instagram; piede. Oltre 9.000 px.
- **Fotografia:** servizio vero, mani che cucinano, carbone, cibo; prodotti su fondi pastello; la facciata con le tende noren. 160 immagini.
- **Tipografia:** YuGothic e Noto Sans Japanese. Menu 15 px grassetto, titoli di sezione 12-21 px maiuscoli spaziati, testo 11-16 px. Il corpo più frequente è 11 px: troppo piccolo.
- **Colori:** fondi pastello per blocchi (grigio azzurro, beige, terracotta, blu notte), bianco, nero.
- **Griglia e margini:** contenitore di circa 1180 px; blocchi colorati a tutta larghezza.
- **Dettagli da studio:** il menu con le etichette dei gruppi; il catalogo leggibile in due modi (che cos'è e a che cosa serve); il servizio messo alla pari dei prodotti; la didascalia che nomina il fabbro.
- **Prove:** i nomi delle forge (Yoshikane, Sanjo), i tre negozi nel mondo, le storie degli artigiani.
- **Contatto:** "Location" in menu, scheda per ogni negozio.
- **Che cosa si trasferisce:** il catalogo per tipo di locale e per uso (Foralberg: per un bar, per una sala colazioni, per un banqueting), il servizio di progetto in una tessera grande come quelle dei prodotti, la didascalia che nomina il produttore. **Che cosa no:** i disegni al tratto delle categorie (il committente non vuole illustrazioni al posto delle foto); i corpi di 11 px; la home lunga.

### Serax: serax.com
- **Che cosa fa:** azienda belga di famiglia, dal 1986: stoviglie, vetri, posate, pentole, lampade e mobili disegnati con designer e cuochi; area Professionisti e portale B2B per negozi e ristoranti.
- **Prima schermata:** coperta dalla finestra "Visiting from the United States?" e, chiusa quella, dal popup della newsletter e dalla chat. Dietro: barra nera sottile, testata con quattro voci a sinistra, il logotipo SERAX spaziato al centro, tre voci a destra (Progetti, Professionisti, Informazioni); sotto "Categoria in evidenza, Illuminazione Serax" (16 px) e una foto in un contenitore di circa 1080 px, alta il 70% della schermata. A 390 la chat copre metà dello schermo.
- **Struttura della home:** categoria in evidenza; quattro categorie scontornate (stoviglie, illuminazione, accessori, arredamento); due collezioni affiancate con un testo lungo ciascuna e il nome della designer; articoli firmati in un cursore con designer e prezzo; "Spazi curati"; blog; newsletter; "Dal 1986. Siamo un'azienda familiare con una passione per il design" con tre riquadri; designer dalla A alla Z; mappa dei prodotti; piede scuro con "Contatti per professionisti" e "Portale B2B". 7.600 px.
- **Fotografia:** prodotti su fondi neutri da studio, ambienti allestiti, ritratti dei designer nei loro luoghi.
- **Tipografia:** tre famiglie (Serax-Sans, Serax-Serif, Avenir Next). Titoli 12-16 px maiuscoli spaziati, testo 14/21 px serif, interfaccia 10-11 px. Il corpo più frequente è 11 px.
- **Colori:** bianco, nero, grigio antracite del piede.
- **Griglia e margini:** contenitore di 1080 px, filetti sottili tra le sezioni, una linea verticale tra le due collezioni.
- **Dettagli da studio:** ogni oggetto ha il nome di chi l'ha disegnato; filetti e titoli piccoli al centro; la frase "azienda familiare" in fondo, non in apertura.
- **Prove:** i nomi dei designer e dei cuochi (Ottolenghi, Sergio Herman, Marni, Piet Boon, Vincent Van Duysen).
- **Contatto:** voce "Professionisti" in testata, "Contatti per professionisti" e "Portale B2B" nel piede.
- **Che cosa si trasferisce:** la voce "Professionisti" separata con il suo contatto (Foralberg ha già "Privati: La Vetrinetta", serve l'opposto chiaro); il nome di chi ha fatto la cosa accanto alla cosa (Foralberg: il locale arredato con il nome del cliente). **Che cosa no:** tre popup in apertura; testo a 10-11 px; tre famiglie di caratteri.

### The English Stamp Company: englishstamp.com
- **Che cosa fa:** laboratorio di famiglia a Worth Matravers (Swanage, Dorset), dal 1992: timbri in gomma su misura dal logo, dal disegno, dalla calligrafia o da una foto; timbri disegnati in casa; tamponi e accessori.
- **Prima schermata:** barra taupe "Free delivery on UK orders over £40"; testata con ricerca a sinistra, logotipo condensato al centro con sotto la riga corsiva "Celebrating over 30 years in business", icone a destra; menu di otto voci (Custom stamps, Weddings, Art stamps, Gift ideas, Christmas, Ink pads, Accessories, Help). Il cursore occupa circa il 55% della schermata: un riquadro taupe con "ART STAMPS", due righe e "SHOP NOW", e due foto di pacchetti incartati con carta timbrata. 9 elementi.
- **Struttura della home:** cursore; tre bottoni di aiuto (video, consegne, aiuto con l'ordine); due tessere (novità di stagione, timbri su misura fatti a mano); "Welcome" con il testo e una citazione di un cliente; tre tessere per occasione (conserve, guida ai regali, biglietti); timbri di testo e timbri da cancelleria; "Be inspired" (rilievo, video, superfici diverse); social; newsletter; piede con indirizzo e partita IVA. 4.800 px.
- **Fotografia:** foto di prodotto fatte in casa, ma con una regia costante: sempre il timbro accanto all'impronta, su legno scuro, con fiori, nastri e spago, luce laterale calda. Circa 12 foto, due formati.
- **Tipografia:** Karla (titoli 20-29 px maiuscoli, spaziatura 1 px) e Nunito Sans (testo 16/29 px). Il corpo più frequente è 14 px. Corsivo calligrafico solo nel motto sotto il logo.
- **Colori:** taupe (#b6a898 circa), bianco, grigio chiaro per la fascia del testo.
- **Griglia e margini:** contenitore di circa 1160 px, tessere con bordo sottile e bottoni contornati.
- **Dettagli da studio:** l'impronta sempre insieme al timbro; la lista di che cosa si può mandare; l'offerta per occasione.
- **Prove:** dal 1992, "family business", una citazione di cliente, la pagina "How green are we?".
- **Contatto:** pagine di aiuto e FAQ; indirizzo registrato nel piede.
- **Che cosa si trasferisce:** fotografare ogni timbro accanto alla sua impronta e ogni targa montata al suo posto (si fa con il telefono, sul banco, con la luce della finestra: è una regia, non un servizio); dire in una riga che file mandare; dividere per occasione (ufficio, studio professionale, condominio, premiazione). **Che cosa no:** il cursore in apertura; il corsivo calligrafico del motto; i fiori e i nastri, che per un laboratorio di timbri per notai e uffici pubblici sarebbero fuori tono.

### L. Cornelissen & Son: cornelissen.com
- **Che cosa fa:** negozio di colori per artisti a Londra, 105 Great Russell Street, dal 1855: pigmenti, gomme, resine, olii, tele, acquerelli, pastelli, doratura e restauro, incisione, pennelli, carta, insegne; negozio con gli arredi vittoriani originali.
- **Prima schermata:** contenitore di 1170 px su fondo verde menta. Testata verde bottiglia con le medaglie delle esposizioni e il nome in maiuscoletto; due righe di categorie a linguette (Pigments, Gums, Resins / Oils, Acrylics / ... / Gilding, Restoration / Signwriting, Specialist Decorating / Brands); a sinistra una colonna con il menu, il carrello, "GIFTS". A destra un cursore alto circa il 75% della schermata: una bottiglia del loro inchiostro ferrogallico con il tappo di ceralacca rossa, appoggiata sulle galle di quercia. 12 elementi. A 390: la foto dell'interno del negozio con le cassettiere e sotto le categorie come righe grandi con la freccia.
- **Struttura della home:** cursore; un avviso sulle dogane UE; cinque prodotti in evidenza; tre riquadri: "Contact us" (telefono, orari 9:30-18:00 dal lunedì al sabato), "Tour the shop" (il negozio con gli arredi del 1855, giro virtuale), "Location" (indirizzo); piede con email e telefono. 1.700 px.
- **Fotografia:** foto fatte in negozio, di prodotto e di materia prima (la bottiglia sulle galle, i vasetti di pigmento). Poche, ma vere.
- **Tipografia:** Roboto Serif (nome, titoli, testo dei riquadri, 13-20 px) e Sofia Sans Condensed (menu e categorie, 16 px). Corpi distinti: 8.
- **Colori:** verde bottiglia (#2b4f3c circa), verde menta chiaro, bianco, il rosso della ceralacca nella foto.
- **Griglia e margini:** impaginazione a due colonne vecchio stile; è il sito meno moderno del gruppo, ma il più coerente con il negozio.
- **Dettagli da studio:** le categorie con le parole del mestiere ("Gilding, Restoration", "Signwriting, Specialist Decorating"); la voce "Recipes" (ricette per preparare i colori); il negozio stesso come prova ("maintains its original Victorian fittings").
- **Prove:** 1855, le medaglie delle esposizioni nel marchio, i prodotti a proprio marchio.
- **Contatto:** telefono, orari e indirizzo in home in tre riquadri uguali e di nuovo nel piede.
- **Che cosa si trasferisce:** i tre riquadri uguali (telefono e orari, il negozio da vedere, l'indirizzo) come chiusura corta della home; le categorie con le parole di chi compra; un prodotto fotografato con la sua materia prima (Artificio: una foglia d'oro sul bolo, un pennello di martora). **Che cosa no:** la colonna laterale e le linguette su due righe; la home così corta funziona perché il negozio online fa il resto.

### Pigment Tokyo: pigment.tokyo
- **Che cosa fa:** negozio di pigmenti e materiali per artisti a Tokyo (Warehouse Terrada): circa 4.500 colori di pigmento, più di 600 pennelli, colle animali, carta washi, foglia d'oro; workshop in negozio, consulenza su appuntamento, negozio online.
- **Prima schermata:** barra sottile di avviso; testata con il menu a tendina e la ricerca a sinistra, il logotipo PIGMENT al centro, quattro voci in grassetto (Items, Articles, Workshops, Store) e le icone a destra. Sotto, un cursore di articoli a tutta larghezza alto circa metà schermata, con le diapositive numerate 01-08 (i pastelli Gondola, i pigmenti a effetto); sotto inizia "Shop by Category". 10 elementi.
- **Struttura della home:** cursore; dieci categorie in tessere con la foto (pigmenti, pigmenti a effetto, colori, leganti e colle, pennelli, stick di sumi, pietre da inchiostro, foglia metallica, carte, attrezzi e libri); dieci marchi in tessere (Kusakabe, Kuretake, Nakagawa Gofun, Zecchi...); prodotti numerati (foglie d'argento colorate dalla No.1 alla No.13 con prezzo, "New", "Sold out"); articoli ("PIGMENT Color Dictionary"); workshop con data, orario e "Sold out"; il testo di chi sono; due tessere grandi (consulenza, workshop privato); piede. 5.300 px.
- **Fotografia:** foto vere del negozio e dei materiali, macro dei pigmenti, la parete dei vasetti di vetro; trattamento chiaro e coerente.
- **Tipografia:** futura-pt quasi ovunque (menu 18 px grassetto spaziato, titoli 26 px grassetto, testo 13-16 px), giapponese di sistema per i testi locali.
- **Colori:** bianco, grigio chiarissimo per le fasce, nero; il colore viene tutto dai materiali.
- **Griglia e margini:** contenitore di circa 1200 px, griglie di 5 e 6 colonne con passo di 12 px.
- **Dettagli da studio:** i prodotti numerati come in un campionario; i workshop con data e ora; il numero dei colori e dei pennelli detto una volta, nel testo.
- **Prove:** 4.500 colori, 600 pennelli, la lista dei marchi, i workshop esauriti.
- **Contatto:** "Shopping consultation services" e "Private workshop" come servizi prenotabili; pagina Store.
- **Che cosa si trasferisce:** i corsi con data, ora, prezzo, posti e "esaurito" (Artificio ha Artinpratica: va presentato così); i marchi come tessere con la foto dello scaffale di quel marchio; la consulenza come servizio da prenotare. **Che cosa no:** il cursore d'apertura; la home costruita come un negozio online da 85 immagini.

### Bisca: bisca.co.uk
- **Che cosa fa:** progettazione, costruzione e posa di scale su misura, Helmsley (North Yorkshire), per privati, architetti, interior designer e imprese.
- **Prima schermata:** una foto a tutta pagina (100%) di una scala a sbalzo in rovere con il parapetto di vetro su un pavimento a scacchi. Sopra: il logo a mano bianco in alto a sinistra, nove voci piccole in maiuscolo a destra, le icone dei social in basso a sinistra, "TEL: +44 (0) 1439 771 702" in basso a destra, una freccia in giù al centro e la didascalia "Ash Multiflight Stair, York". 6 elementi. A 390: la stessa foto a tutto schermo con il telefono in basso.
- **Struttura della home:** apertura; "Welcome to Bisca Staircases" con quattro foto della galleria e un bottone; "We push the boundaries" con tre foto di processo (schizzo a matita, scintille in officina, scala finita) e le etichette Design, Craft, Install; "Who we work with" (privati, architetti, interior designer, imprese); recensioni (vuote alla cattura); "Ready to get started?" con tre tessere (il processo, i materiali, la squadra con la foto del progettista alla scrivania); articoli; dieci premi e accreditamenti; piede con un modulo breve (nome, cognome, telefono, email), indirizzo, "Get directions". 6.100 px.
- **Fotografia:** servizio vero sulle scale posate, più foto di officina; luce d'interni, qualche foto più vecchia.
- **Tipografia:** source-sans-pro. Titoli 36/44 px peso 300 in rosa antico, testo 15-18 px; un font a mano solo per il logo. I titoli sottili rosa su bianco hanno poco contrasto.
- **Colori:** rosa antico (#c98a85 circa), bianco, grigio carta con una trama, nero per le etichette.
- **Griglia e margini:** contenitore di circa 1250 px; tessere a filo nella parte delle foto.
- **Dettagli da studio:** la didascalia con il nome della scala e la città; il trio schizzo, officina, posa; il marchio "Made by Bisca craftsmen in Great Britain".
- **Prove:** dieci premi con l'anno, "100% customer satisfaction rate", recensioni lunghe, la squadra con il nome.
- **Contatto:** telefono sulla foto d'apertura e nel piede, modulo nel piede.
- **Che cosa si trasferisce:** la didascalia sulla foto d'apertura ("Scala a giorno Montreal, Padova"); il su misura raccontato in tre foto dello stesso taglio (misura presa sul posto, lavorazione, posa: le può fare il titolare con il telefono); i riconoscimenti, se ci sono. **Che cosa no:** i titoli sottili rosa; le icone al tratto di "Who we work with" (sono le icone in fila che il committente non vuole).

### Dolle: dolle.com
- **Che cosa fa:** fabbrica danese (Frøstrup) di scale retrattili da soffitta, scale salvaspazio, scale a chiocciola, ringhiere, botole da tetto e da parete; si presenta come leader mondiale delle scale da soffitta.
- **Prima schermata:** riga di servizio in alto (Projects & Guides, Jobs, Distribution, For business customers, Downloads); ricerca a sinistra, logo rosso al centro, lingua a destra; menu di otto categorie a tendina. La foto occupa circa metà della schermata: una scala a giorno grigia in una cucina, con "Staircase DUBAI" (48 px grassetto bianco), una riga e il bottone rosso "Have a look!". 6 elementi. A 390: il titolo a 40 px su due righe sopra la foto.
- **Struttura della home:** apertura; "More possibilities. Inside and out." con due righe; mosaico di dieci tessere fotografiche con il nome sopra (scale da soffitta, scale, ringhiere, botole da tetto, botole da parete, salvaspazio, corrimano, esterne, a chiocciola); le scale più vendute con i pallini dei colori RAL; piede con le società del gruppo. 3.200 px.
- **Fotografia:** ambienti allestiti da studio e foto di prodotto scontornate; diverse sembrano costruite al computer.
- **Tipografia:** DIN Next LT Pro sola. Titolo 48 px peso 700, sezioni 30-32 px peso 700, testo 16/24 px, interfaccia 12 px. Corpi distinti: 7.
- **Colori:** rosso del marchio (#e30613 circa), bianco, grigio chiaro del piede.
- **Griglia e margini:** contenitore di 1220 px, mosaico con tessere di due larghezze e passo di 8 px.
- **Dettagli da studio:** il mosaico per luogo d'uso con il nome in bianco in basso a sinistra; i colori RAL come pallini sotto il prodotto; la home corta.
- **Prove:** "world market leader", la lista delle società e delle fabbriche del gruppo.
- **Contatto:** servizio clienti per paese; "For business customers" in alto.
- **Che cosa si trasferisce:** il mosaico di tessere fotografiche con il nome del luogo (Scalarredo: soffitta, parete, terrazzo, soppalco, scale da interno, ringhiere), al posto dei bottoni gialli di testo; i colori disponibili come pallini; "Download" per le schede di montaggio. **Che cosa no:** le foto costruite al computer (per noi sarebbero foto di repertorio); il tono da multinazionale.

### Plain English: plainenglishdesign.co.uk
- **Che cosa fa:** "cupboardmakers" dal 1992: cucine, dispense, armadi e altre stanze su misura in legno, fatte nel laboratorio di Stowupland Hall (Suffolk); showroom a Londra (Pimlico Road), New York, Los Angeles.
- **Prima schermata:** riga sottile con le bandiere e "Contact us" a sinistra, "View brochure" e "Make an enquiry" a destra, il menu nascosto; logotipo serif "Plain English" con "CUPBOARDMAKERS" piccolo sotto, al centro. Sotto, una foto in un contenitore con 22 px di margine, alta circa il 70% della schermata: una cucina color crema in una casa di campagna con la luce della finestra e un cavolo verza sul piano. Sotto la foto il titolo "FINE CRAFTSMANSHIP SINCE 1992" (Baskerville 30/39 px, maiuscolo, spaziatura 6 px). 6 elementi.
- **Struttura della home:** foto (cursore); manifesto di tre righe in maiuscolo serif spaziato; "LONDON NEW YORK LOS ANGELES"; l'elenco delle stanze come parole (Kitchens, Pantries, Mudrooms, Butler's pantries, Sculleries, Bedrooms...); sei tessere 3x2 quadrate con il nome al centro (Kitchens, How we work, Other rooms, Pimlico showroom, Stowupland Hall, Colour collections); piede di sei link. 2.300 px.
- **Fotografia:** un servizio d'interni vero, una sola luce naturale, colori tenui, stessi tagli. Le persone non ci sono.
- **Tipografia:** Baskerville BT (titoli e manifesto, 18-30 px maiuscoli spaziati) e Gill Sans MT Pro (interfaccia, 14 px maiuscolo spaziato 1,5 px). Corpi distinti: 9, ma quelli visibili in home sono quattro.
- **Colori:** bianco, grigio caldo del testo; il colore lo danno le cucine.
- **Griglia e margini:** margini di 22 px, tessere quadrate con passo di 22 px; un solo filetto prima del piede.
- **Dettagli da studio:** due azioni scritte in testata e nessun bottone in pagina; il laboratorio come una delle sei tessere; la nota legale nel piede "Colours inevitably vary in photography. Please visit one of our showrooms". Non c'è: nessuna cifra, nessuna icona, nessuna recensione, nessun modulo.
- **Prove:** dal 1992, il nome del laboratorio, le tre città.
- **Contatto:** "Make an enquiry" e "View brochure" in testata; pagine degli showroom.
- **Che cosa si trasferisce:** la home corta con sei tessere quadrate, il laboratorio come luogo da visitare, le due azioni scritte (Bottega: "Mandaci un disegno" e "Vieni in bottega"), l'elenco dei lavori come parole. **Che cosa no:** l'apertura dipende da una foto d'interni di livello; con le foto di Bottega dell'Arte serve una foto di lavoro finito scattata bene (il sottoscala con la nicchia d'ottone è la candidata), altrimenti la pagina si svuota.

### Benchmark: benchmarkfurniture.com
- **Che cosa fa:** falegnameria inglese (Benchmark Woodworking Ltd) di mobili e allestimenti su misura per uffici, università e case; collabora con studi di architettura; programma di apprendisti.
- **Prima schermata:** filo verde oliva in cima; testata bianca con BENCHMARK spaziato a sinistra e cinque voci in maiuscolo da 13 px a destra (Furniture, Projects, Sustainability, About us, Contact). La foto occupa circa il 67% della schermata: un sentiero nel bosco, senza mobili, con una freccia in giù. 4 elementi.
- **Struttura della home:** bosco; due tessere (una nuova serie disegnata con Foster + Partners, l'intera gamma); fascia verde (modelli BIM con i dati di sostenibilità); due tessere (sostenibilità, "Bespoke furniture & joinery"); fascia verde (rapporto di sostenibilità da scaricare); tre progetti con il nome (Case Western Reserve University, Norton Folgate, Worcester College); tre collezioni; "A workshop built on care" e "A legacy of making" con quattro apprendisti in bianco e nero; newsletter; piede. 4.700 px.
- **Fotografia:** servizio vero su mobili e progetti, luce morbida; ritratti in bianco e nero.
- **Tipografia:** BasicCommercial (etichette 13 px maiuscole spaziate) e Bressay Italic per i titoli (22 px corsivo serif). È il serif corsivo d'accento che il committente vieta.
- **Colori:** verde oliva (#6b7451 circa), bianco, nero.
- **Griglia e margini:** tessere a due e a tre colonne; ogni tessera ha il titolo in corsivo e sotto un'etichetta piccola in maiuscolo verde (PROJECT, EXPLORE).
- **Dettagli da studio:** la coppia titolo più etichetta ripetuta sempre uguale; i progetti con il nome del luogo; gli apprendisti come prova.
- **Prove:** progetti con il nome, la collaborazione con Foster + Partners, il rapporto di sostenibilità, gli apprendisti.
- **Contatto:** "Contact" in testata.
- **Che cosa si trasferisce:** i lavori con il nome del committente in tre tessere uguali (Bottega lo fa già con Palazzo del Bo e la pasticceria: va tenuto e reso più asciutto); la foto in bianco e nero di chi lavora in bottega; un sistema di etichette ripetuto sempre uguale. **Che cosa no:** il corsivo serif nei titoli; il bosco al posto del lavoro in apertura.

### Toschi: toschi.it
- **Che cosa fa:** Toschi Vignola, dal 1945, fondata da Giancarlo e Lanfranco Toschi: amarene, sciroppi, salse, topping e liquori; più di 400 referenze per bar, ristorazione, gelateria e pasticceria, e per la casa.
- **Prima schermata:** il frutteto di ciliegi in fiore a tutta pagina (100%), cielo azzurro e prato. In alto a sinistra il logo piccolo, a destra il cerchio rosso "SHOP", il menu a panino e "ITALIANO". Nessun titolo. 4 elementi. A 390: barra rossa delle lingue, logo, il frutteto e subito sotto il titolo della storia in rosso maiuscolo.
- **Struttura della home:** frutteto; "80 anni di Toschi" con la T, due paragrafi, la firma di Giancarlo Toschi e il bottone "La nostra storia"; cursore dei topping senza zuccheri; "Per i professionisti" in grande; tre blocchi con il loro colore e il loro marchio (Bar e ristorazione su bianco, Gelateria su azzurro, Pasticceria su giallo), ognuno con una foto di prodotto e un bottone; piede rosso con indirizzo, email, telefono e il marchio storico. 6.400 px.
- **Fotografia:** il frutteto è una foto vera di paesaggio; il resto sono foto di prodotto da studio con le ciliegie scontornate che volano intorno.
- **Tipografia:** DinPro (testo 20/30 px, buono) e DinPro Condensed (titoli 35-80 px maiuscoli, spaziatura 3 px). Corpi distinti: 9.
- **Colori:** il rosso Toschi del marchio, bianco, azzurro e giallo pastello per i canali.
- **Griglia e margini:** blocchi a tutta larghezza alternati, testo centrato in colonna di 800 px.
- **Dettagli da studio:** la materia prima come prima immagine; un colore per ogni canale professionale; la firma del fondatore.
- **Prove:** 1945, i nomi dei fondatori, tre generazioni, 400 referenze, "Marchio storico".
- **Contatto:** nel piede (via, email, telefono); "Area riservata" per i professionisti.
- **Che cosa si trasferisce:** la home divisa per mestiere del cliente, con un blocco di colore per canale (Rizzi: pasticcerie, bar e ristoranti, spaccio per i privati); la materia prima in apertura, se c'è una foto vera (agrumi e frutta nell'essiccatore di Rizzi). **Che cosa no:** le ciliegie scontornate che volano (decorazione da agenzia di packaging); la firma in corsivo.

### Nardini: nardini.it
- **Che cosa fa:** Distilleria Nardini, Bassano del Grappa, dal 1779 al Ponte Vecchio: grappe e liquori, mixology, visite guidate alla distilleria.
- **Prima schermata:** porta dell'età ("Hai compiuto 18 anni?") dentro una cornice incisa; dopo: testata nera con il logo e sei voci in maiuscolo da 12 px (Acquista online, La prima distilleria d'Italia, I prodotti, Mixology, I luoghi, Visite guidate). Sotto, in un contenitore di circa 1140 px, una diapositiva alta circa il 60% della schermata con la bottiglia di un liquore ai fiori di sambuco e la scritta in un carattere decorativo. 6 elementi.
- **Struttura della home:** tre diapositive di prodotto; "Fieri della nostra storia" con l'incisione del Ponte Vecchio dietro una bottiglia; fascia nera "La distillazione, un'arte che ci appartiene"; "I nostri prodotti" con le mani piene di vinacce; "Grappa & mixology"; "I nostri luoghi" con l'incisione del ponte virata in ocra; "Organizza la tua visita guidata" sull'incisione di una tavolata; newsletter; piede nero con indirizzo e partita IVA. 5.000 px.
- **Fotografia:** foto di prodotto e di campagna pubblicitaria, una foto vera di mani con le vinacce; molte incisioni d'archivio usate come fondo.
- **Tipografia:** Raleway (testo 19/28 px, titoli 52-90 px leggeri), un corsivo calligrafico e un carattere decorativo per i nomi dei prodotti. Tre stili che litigano.
- **Colori:** nero, crema, ocra delle incisioni, i colori delle etichette.
- **Griglia e margini:** contenitore di 1140 px con margini bianchi ai lati; testo su immagine.
- **Dettagli da studio:** le incisioni d'archivio come illustrazioni di sezione; la fascia nera con il motto in condensato.
- **Prove:** 1779, "la prima distilleria d'Italia", il Ponte Vecchio.
- **Contatto:** "Contattaci" nel piede, "Visite guidate" in menu.
- **Che cosa si trasferisce:** le incisioni e le etichette storiche d'archivio come immagini di sezione (Rizzi ha il leone "casa fondata nel 1850", le etichette Genzial: sono documenti, non illustrazioni inventate); le visite allo spaccio o al laboratorio come invito con il loro bottone. **Che cosa no:** la porta dell'età come barriera; tre famiglie di caratteri; le diapositive pubblicitarie.

### Fuller Moto: fullermoto.com
- **Che cosa fa:** officina di Atlanta di Bryan Fuller: progetto e costruzione di moto e auto su misura, vernice, sellatura, lamiera, CAD e stampa 3D; programmi TV, workshop.
- **Prima schermata:** foto a tutta pagina (100%) della calandra di una Ford Model T rifatta, scura, tra le foglie. Logo con le ali in alto a sinistra, nove voci in maiuscolo da 14 px spaziate, icone social; a sinistra "THE RAPTOR T" (41 px grassetto condensato), una riga e il bottone contornato "INSIDE THE BUILD". 5 elementi.
- **Struttura della home:** apertura; "Art, culture & the craft of metal" con la foto da studio di una special argento e il testo; fascia video "The advanced technology workshop" (vuota alla cattura) con "Builder challenge"; "Your dream, our team" con l'elenco delle lavorazioni e la foto di un meccanico al lavoro; quattro tessere (Tune in, Shop, Learn, Make); iscrizione; piede bianco. 4.400 px.
- **Fotografia:** servizio vero sulle costruzioni, scuro e contrastato; una foto d'officina.
- **Tipografia:** Roboto Condensed (titoli maiuscoli spaziati), Roboto, Open Sans (testo 18/29 px). Tre famiglie quasi uguali.
- **Colori:** nero pieno, bianco.
- **Griglia e margini:** contenitore di 1200 px, testo centrato.
- **Dettagli da studio:** ogni costruzione ha un nome e una pagina "inside the build"; l'elenco delle lavorazioni in cinque parole.
- **Prove:** le costruzioni con il nome, i programmi TV.
- **Contatto:** "Contact" in alto a destra.
- **Che cosa si trasferisce:** una special per volta in apertura, con il nome e il link alla sua storia (Overdrive: Hagane, con le copertine di Kustom World e Bigtwin); l'elenco di che cosa si fa a mano in casa. **Che cosa no:** il nero pieno ovunque con il testo grigio; il video.

### Old Empire Motorcycles: oldempiremotorcycles.com
- **Che cosa fa:** costruttore britannico di moto su misura fatte a mano, ricambi e abbigliamento.
- **Prima schermata:** logo con il cavaliere a sinistra, menu di cinque voci in corsivo dentro un parallelogramma nero, social a destra; foto per circa l'85% della schermata di un motociclista su una special con il faro giallo; a destra un riquadro nero "Old Empire Motorcycles" e un bottone obliquo "View motorcycles". 5 elementi.
- **Struttura della home:** apertura; frase di mestiere e due tessere (About us, Electric); foto larga con il testo in un riquadro; seconda frase e due tessere (Concepts, Contact us); blocco YouTube; nastro dei premi che scorre; piede (copyright 2017). 4.300 px.
- **Fotografia:** servizio vero sulle moto, all'aperto, luce di giorno.
- **Tipografia:** Montserrat (titoli 32-37 px peso 600, testo 15 px) e Ropa Sans.
- **Colori:** bianco, nero, il giallo del faro.
- **Griglia e margini:** blocchi foto e testo alternati a filo.
- **Dettagli da studio:** la frase "Specialists in the design and creation of handmade custom motorcycles, parts & attire" come prima riga di testo.
- **Prove:** la lista dei premi con evento e anno (Salon Privé 2014 Winner, Malle Mile 2015 Best of Show, Top 3 MCN Custom Championship 2015, Verona Custom Motorcycle Championship 2017).
- **Contatto:** una tessera "Contact us".
- **Che cosa si trasferisce:** la frase di mestiere in una riga; i premi con evento e anno (Overdrive ce li ha già in tabella, va bene così). **Che cosa no:** il nastro che scorre; le forme oblique; il sito fermo al 2017 (un sito non aggiornato toglie più di quanto dia).

### Architectural Plants: architecturalplants.com
- **Che cosa fa:** vivaio specializzato a Pulborough (West Sussex), dal 1990, 32 acri, guidato dal titolare Guy Watts: topiaria, palme, piante esotiche ed esemplari; aperto a privati e professionisti; progettazione e messa a dimora di giardini, matrimoni ed eventi.
- **Prima schermata:** barra nera con i buoni regalo, il telefono "01798 879213" e l'email; testata antracite con la ricerca, il logotipo spaziato "Architectural PLANTS, since 1990" al centro e due bottoni, "BOOK A VISIT" nero e "CONTACT US" rosso; menu di nove voci; tre promesse con un disegnino (prenota la visita, la più grande collezione del Regno Unito, progettazione); fascia rossa "View our complete stock list: click here". La foto (il vivaio visto dal drone) occupa circa il 50% della schermata, con il titolo in un riquadro e due bottoni. 16 elementi: troppi. A 390: i due bottoni a metà larghezza in cima allo schermo, poi logo, ricerca, fascia rossa e la foto.
- **Struttura della home:** apertura; titolo di mestiere "Hunt for plants. Explore our nursery. Discover our garden design."; tre schede con foto (le piante, la visita, il giardino); "A warm welcome" con il titolare e la squadra; una recensione con le stelle su foto; "A bold vision for every garden"; otto schede (vivaio, piante, progettazione, visite, negozio, matrimoni, guide, squadra); "Visit our nursery" con la mappa disegnata a mano e le istruzioni; due certificati; newsletter; piede di quattro colonne. 5.800 px.
- **Fotografia:** foto vere del vivaio, dei giardini e della squadra; luce di giorno, qualità varia.
- **Tipografia:** Halant (serif) quasi ovunque, titoli 27 px maiuscoli, testo 15-17 px; capolettera nel testo di benvenuto.
- **Colori:** antracite, rosso bordeaux, bianco.
- **Griglia e margini:** contenitore di 1280 px, schede a 3 e a 4 colonne con lo stesso taglio della foto.
- **Dettagli da studio:** le istruzioni per arrivare scritte come le direbbe una persona; "Dogs are always welcome"; l'elenco completo delle piante in vendita.
- **Prove:** dal 1990, 32 acri, il titolare con il nome, le recensioni, il certificato "Plant Healthy".
- **Contatto:** telefono ed email in cima, "Book a visit" e "Contact us" come bottoni, mappa e istruzioni.
- **Che cosa si trasferisce:** la visita al vivaio da prenotare; l'elenco delle piante disponibili (Bordin: esemplari in zolla con specie, misura e foto, anche come PDF aggiornato); le istruzioni d'arrivo in parole ("in via dei Vivai, il Garden al 6, il vivaio al 14"); il titolare con il nome. **Che cosa no:** 16 elementi in prima schermata; il capolettera; la mappa disegnata va fatta fare apposta, e non deve sostituire le foto.

### Lorenz von Ehren: lve-baumschule.de
- **Che cosa fa:** vivaio di alberi di Amburgo, dal 1865, oltre 600 ettari: alberi grandi, esemplari unici, siepi, piante formate; giardini espositivi a Monaco, Düsseldorf, Francoforte e uffici in Inghilterra e Svizzera; accademia e progetti.
- **Prima schermata:** testata bianca con il logo dell'abete a sinistra, una grande barra di ricerca delle piante, il menu (Projekte, Pflanzen, Service, Wissen, LvE Welt), tre icone tonde verdi (Baumkauf, Shop, Meine Auswahl); fascia verde con tre promesse. Il cursore d'apertura alla cattura era vuoto: resta una schermata bianca con la fascia. Il banner dei cookie chiuso.
- **Struttura della home:** cursore; "Bäume für Generationen" con la regola per i privati (ordine minimo 750 euro netti, sotto si passa al garden center Garten von Ehren); i certificati GLOBALG.A.P. e AVPQ e la ricerca delle piante; quattro tessere (accademia, lavoro, il bunker verde di Amburgo, progetti); "Große Bäume kaufen" in cursore con nome latino, nome comune e scheda; esemplari unici; "Kollegen und ihre Lieblingsbäume", cinque persone con nome, ruolo e albero preferito; alberi per il clima che cambia; testo lungo; "Hier finden Sie uns!" con la cartina della Germania e i contatti di ogni sede; "Wir beraten Sie gerne" su una foto di alberi; piede. 8.600 px.
- **Fotografia:** foto vere dei campi, degli esemplari e delle persone; qualità da archivio aziendale, non da servizio.
- **Tipografia:** Inter ovunque (testo 18/27 px, titoli 28-36 px peso 700). È l'"Inter ovunque" che il committente vieta.
- **Colori:** verde scuro (#1d4d35 circa), bianco, grigio.
- **Griglia e margini:** contenitore di 1280 px, schede con bordo grigio, cursori.
- **Dettagli da studio:** le persone con l'albero preferito; la regola su chi compra dove; ogni sede con il suo link "Kontakt".
- **Prove:** dal 1865, 600 ettari, due certificati, progetti con il nome (il bunker verde di Amburgo).
- **Contatto:** "Kontakt" in testata, sedi con il loro contatto, telefono ed email nel piede.
- **Che cosa si trasferisce:** le persone del vivaio con nome, ruolo e pianta preferita (Bordin: la terza generazione e chi segue Garden, Vivai, Giardini); la regola chiara su chi va al Garden e chi ai Vivai; gli esemplari con il nome latino e la misura. **Che cosa no:** Inter, i cursori, 243 immagini, la testata a icone.

### Tricker's: trickers.com
- **Che cosa fa:** calzaturificio di famiglia a Northampton, dal 1829: scarpe e stivali Goodyear; negozi a Londra (Jermyn Street dal 1938), Tokyo e Shanghai; fornitore della casa reale.
- **Prima schermata:** barra ocra delle spedizioni; riga di servizio (Owners Club, i negozi, spedizioni, chat, social, valuta); testata trasparente sulla foto con il logo e cinque voci; foto a tutta pagina (100%), un cursore: gli stivali e le scarpe in camoscio sul banco di legno con le lesine e il filo, "NEW IN" (40 px maiuscolo), una riga e il bottone bianco. In un'altra diapositiva "CORBETT WALKING BOOT, celebrating our 195th anniversary". 8 elementi. A 390 il popup della newsletter copre tutto.
- **Struttura della home:** apertura; "The Originals" con due linguette e cinque modelli su bianco con il prezzo; film "Everything you need to know about Tricker's, 10 minutes" sulla campagna; citazione di re Carlo; "Trusted by our customers since 1829" con le recensioni e "1292 reviews"; novità; "Stow country boots" ("created back in 1840"); "Classic men's looks" con quattro persone; "Northampton through & through" con gli operai al banco; i tre negozi con la facciata; il giornale; newsletter; lo stemma del fornitore reale; piede blu notte con il sigillo dei 195 anni e "Living wage employer". 7.900 px.
- **Fotografia:** servizio vero e coerente: prodotto sul banco con gli attrezzi, persone in campagna, operai in fabbrica, facciate dei negozi; luce calda e laterale.
- **Tipografia:** sweet-sans-pro (titoli e menu, maiuscolo largo, 19-40 px) e Helvetica Neue Light (testo 13-17 px). Il testo di 13 px peso 300 è piccolo.
- **Colori:** blu notte (#0f1a2c circa), ocra della barra, bianco, i marroni del cuoio.
- **Griglia e margini:** margini di 44 px, prodotti a 5 colonne, blocchi a due metà foto e testo.
- **Dettagli da studio:** la fabbrica come capitolo della home; l'anno di ogni modello e di ogni negozio; la citazione con il nome di chi l'ha detta.
- **Prove:** dal 1829, lo stemma reale, la citazione del re, 1.292 recensioni, "Living wage", gli anni dei modelli.
- **Contatto:** "Our stores" in alto, chat, pagina contatti.
- **Che cosa si trasferisce:** il capitolo della fabbrica con le persone al banco (Nic Dean: se la fabbrica lavora ancora, una foto del reparto e di chi ci lavora); lo spaccio presentato come "il nostro negozio" con la foto dell'ingresso e l'anno d'apertura (2013); un nome per ogni modello. **Che cosa no:** il negozio online con i prezzi in sterline e i popup; lo stemma reale (non c'è un equivalente e non va inventato).

### Crockett & Jones: crockettandjones.com
- **Che cosa fa:** calzaturificio di famiglia a Northampton (dal 1879): scarpe e stivali per uomo e donna, negozi propri, riparazione in fabbrica.
- **Prima schermata:** barra della regione con la tendina e "Continue"; testata scura sulla foto con nove icone e otto voci; il popup della newsletter con il titolo in corsivo calligrafico e una foto di mocassini copre il centro; dietro, una foto a tutta pagina. Chiuso tutto, la foto è a tutta pagina e il titolo di sezione arriva sotto. A 390 il popup copre tutto.
- **Struttura della home:** collezione d'autunno con testo e bottone; cursore di dieci modelli fotografati ai piedi con il nome e la pelle; una lunga serie di blocchi foto e riquadro con la parola in corsivo e il nome in maiuscolo ("New style, VAIL"); "100% Made in England, the Crockett & Jones way" con i ritratti degli operai sorridenti; i classici; il film con l'alleanza britannica (James Bond); il pellame Horween; i mocassini; "Guest authors". Oltre 9.000 px.
- **Fotografia:** servizio vero, sempre all'aperto su pietra e legno, più i ritratti in fabbrica.
- **Tipografia:** sans in maiuscolo spaziato per i nomi, corsivo calligrafico per le parole d'accento (vietato dal committente), testo piccolo.
- **Colori:** grigio chiaro dei riquadri, nero, i colori della natura nelle foto.
- **Griglia e margini:** blocchi a metà con riquadri sottili sfalsati sulla foto.
- **Dettagli da studio:** ogni modello con il nome e la pelle; le persone della fabbrica con la faccia.
- **Prove:** Made in England, il pellame Horween con il nome, la collaborazione con il cinema.
- **Contatto:** "Stores" in menu, "Making & Repair".
- **Che cosa si trasferisce:** il nome del modello e del pellame in ogni scheda (Nic Dean: "décolleté con plateau in camoscio" diventa un modello con il nome e la pelle); i ritratti di chi lavora. **Che cosa no:** i popup e la barra della regione in apertura; il corsivo calligrafico; la home infinita.

---

## 3. Le costanti del gruppo: come si presenta una bottega o un negozio di alto livello

**Prima schermata**
- La foto riempie la schermata. In 14 siti su 21 l'immagine d'apertura prende più del 65% della prima schermata; in 7 il 100% (Hart, Klippan, Bisca, Toschi, Fuller, Tricker's, Crockett & Jones), in altri due quasi (Tartine 90%, Old Empire 85%).
- Sopra la foto ci sono al massimo tre cose: il nome o una frase, una riga, un'azione. Spesso nessun titolo (Hart, Toschi, Bisca, Benchmark).
- L'immagine è il luogo o la materia, non l'oggetto da catalogo: l'insegna (Hart), il laboratorio (Tartine), il frutteto (Toschi), il vivaio dal drone (Architectural Plants), il banco con gli attrezzi (Tricker's), una scala posata con il suo nome (Bisca).
- Le sedi e gli orari non stanno in apertura. Al massimo una riga per sede sul bordo della foto (Tartine) o una voce "Locations" in testata (Tartine, Hart, Tricker's, Kama-Asa).
- La testata ha 4-6 voci con parole del mestiere, spesso il logotipo al centro (10 siti su 21) e una o due azioni scritte, non bottoni colorati (Plain English "Make an enquiry"; Tartine "Order"; Architectural Plants "Book a visit").

**Fotografia**
- Un solo sguardo per tutta la pagina: stessa luce, stessi tagli (Tartine, Plain English, Tricker's, The English Stamp Company). Quando le foto sono di prodotto, hanno una regia ripetuta (il timbro con l'impronta; lo stivale sul banco).
- Le persone lavorano e non guardano l'obiettivo, tranne nei ritratti della squadra (Lorenz von Ehren, Crockett & Jones, Benchmark).
- L'archivio in bianco e nero vale come prova (Rivolta, Nardini con le incisioni, Benchmark con gli apprendisti).
- Didascalie poche e con un fatto: il nome del lavoro e la città (Bisca), il fabbro e la città (Kama-Asa), il nome del modello e la pelle (Crockett & Jones).

**Tipografia**
- Una famiglia con una voce precisa, o due con ruoli fissi: Tartine (PitchSans sola), Dolle (DIN sola), Plain English (Baskerville e Gill Sans), Toschi (DIN e DIN Condensed), Cornelissen (Roboto Serif e Sofia Sans Condensed).
- Titoli in maiuscolo spaziato a corpi moderati (30-40 px) più spesso dei titoloni: Plain English 30 px, Rivolta 40 px, Tricker's 40 px, Tartine 40 px. I titoli enormi li usano solo Toschi (80 px) e Nardini.
- I difetti più comuni sono gli stessi nostri al contrario: testo troppo piccolo (11 px a Kama-Asa e Serax, 13 px a Klippan e Tricker's) e troppe famiglie (Serax, Nardini, Fuller). Su questo le nostre home sono già meglio e non vanno peggiorate.

**Colori**
- Il colore viene dal marchio o dal materiale: il verde bottiglia di Cornelissen, il rosso Toschi, l'oliva di Benchmark, il rosso Dolle, il blu notte di Tricker's. Molti sono bianco e nero e lasciano il colore alle foto (Plain English, Pigment Tokyo, Serax, Tartine).
- Il fondo beige fisso compare solo in Rivolta (testata) e in English Stamp (fasce).

**Prove**
- Prove con il nome e la fonte, non cifre grandi: gli hotel (Rivolta), i progetti (Benchmark), i premi con evento e anno (Old Empire, Bisca), la citazione con chi l'ha detta (Vogue per Tartine, re Carlo per Tricker's), le persone con il ruolo (Lorenz von Ehren), il fornitore della materia prima (Klippan, Crockett & Jones).
- I numeri sono nel testo, uno alla volta, con la cosa che misurano.
- Nessuno ha la fascia delle cifre grandi, nessuno ha la fila di tre icone, nessuno ha un badge sopra il titolo.

**Contatto**
- Diviso per pubblico: richieste generali, ingrosso, lavoro (Hart); professionisti e portale B2B (Serax, Klippan, Toschi); privati e professionisti con una regola (Lorenz von Ehren).
- Per le botteghe con sede da visitare, il contatto è una visita: "Book a visit" (Architectural Plants), "Visit us at Stowupland Hall" (Plain English), "Tour the shop" (Cornelissen), visite guidate (Nardini), workshop con data (Pigment Tokyo).
- Il modulo in home è raro (solo Bisca, breve, nel piede). Il telefono in grande è raro (Bisca sulla foto, Architectural Plants in cima, Cornelissen nel riquadro).

**Lingua**
- Frasi corte, concrete, in prima persona plurale, con un dato preciso: "special order cakes require a seven day lead time"; "every shoe and boot is made from start to finish in our Northampton factory"; "Dogs are always welcome".
- Le parole del mestiere al posto delle parole di marketing: "cupboardmakers", "Gilding, Restoration", "Signwriting", "nakiri", "in zolla".
- Il motto c'è, ma in fondo o piccolo (Tartine "Rise each day. Warm every table." nel piede).

**Lunghezza**
- Mediana 5.800 px; le migliori sono corte (Plain English 2.300, Cornelissen 1.700, Hart una schermata, Dolle 3.200). Le lunghe (Kama-Asa, Rivolta, Crockett & Jones) sono negozi online.

---

## 4. Le 8 mosse da portare nelle nostre home del gruppo B

### 1. Aprire con una sola foto del luogo vero a tutta larghezza, con al massimo tre cose sopra
- **Esempio:** Tartine (laboratorio, 90% della schermata, nome, una riga, le tre sedi sul bordo); Hart (l'insegna); Toschi (il frutteto); Bisca (una scala posata).
- **Da noi:** Fornasiero con la vetrina e l'insegna di legno, Galileo e Fidalma sulla porta; Bordin con la piramide di vetro; Servalli con la 500 Giardiniera del 1967 a tutta larghezza in bianco e nero; Foralberg con il furgone OM; Overdrive con una special sola. Sopra: il nome del mestiere e del paese in una riga, "Aperto ora" o una sola azione. Gli orari e le schede negozio scendono sotto.
- **Che cosa serve:** una foto orizzontale larga almeno 1600 px. Se l'azienda non ne ha una nuova, la foto d'archivio in bianco e nero regge la larghezza anche se è piccola, perché la grana è accettata; una foto a colori del telefono no. Se non c'è nessuna delle due, l'apertura resta tipografica (vedi le regole M di barth) e la foto va più in basso. Mai foto di repertorio.

### 2. Una didascalia-fatto sulla foto d'apertura
- **Esempio:** Bisca "Ash Multiflight Stair, York"; Kama-Asa "Yoshikane Hamono in Sanjo, town of blacksmiths".
- **Da noi:** Scalarredo "Scala a giorno Montreal, posata a Padova"; Bottega dell'Arte "Bussola del Palazzo del Bo, restauro"; Overdrive "Hagane, chopper su motore Suzuki DR650, 2024"; Fornasiero "Galileo e Fidalma, via Vigonovese 116".
- **Che cosa serve:** sapere per ogni foto che cosa è, dove è stata fatta, quando. Una riga di 14-16 px, in basso a destra o a sinistra, non sotto ogni foto: solo sull'apertura e sui lavori.

### 3. Togliere la fascia delle cifre grandi e accorciare la home a 4.000-6.000 px
- **Esempio:** Plain English (2.300 px, nessuna cifra); Cornelissen (1.700 px); Pigment Tokyo ("4.500 colori di pigmento, più di 600 pennelli" detto una volta nel testo).
- **Da noi:** tutte e undici le home tolgono la fascia di cifre; i numeri che contano restano dentro una frase con la cosa che misurano ("dal 1963 a Camin", "30.000 articoli in 800 m2 di showroom"). Storia, numeri e catalogo vanno nelle loro pagine; in home restano 5-7 sezioni. Overdrive passa da 10.600 a circa 6.000, Rizzi da 10.000 a circa 5.500.
- **Che cosa serve:** decidere per ogni azienda le 5-7 sezioni (apertura, ingressi, una storia di lavoro, le prove, la visita, il piede) e spostare il resto nelle pagine interne. Nessun materiale nuovo.

### 4. Gli ingressi come tessere fotografiche quadrate con lo stesso taglio e il nome sopra
- **Esempio:** Plain English (sei tessere 3x2: cucine, come lavoriamo, altre stanze, showroom, laboratorio, colori); Rivolta (Letto, Tavola, Bagno); Dolle (mosaico per luogo d'uso).
- **Da noi:** Servalli (Letto, Bagno, Tavola, Tappeti, Contract alberghi, Rivenditori); Scalarredo (Soffitta, Parete, Terrazzo, Soppalco, Scale da interno, Ringhiere, al posto dei bottoni gialli di testo); Artificio (Belle arti, Cornici su misura, Corsi); Bordin (Garden, Vivai, Giardini); Bottega (Arredo, Serramenti, Restauro).
- **Che cosa serve:** da 3 a 6 foto vere ritagliate tutte quadrate o tutte 4:3. Quando una voce non ha la foto, la tessera è di sola tipografia sullo stesso fondo e con la stessa misura; niente disegni o icone al posto delle foto.

### 5. Un ingresso separato e chiaro per i professionisti, con il suo contatto e la sua regola
- **Esempio:** Toschi ("Per i professionisti": bar, gelateria, pasticceria, ognuno con il suo colore); Hart (email "wholesale"); Klippan e Serax (portale rivenditori, "Contatti per professionisti"); Lorenz von Ehren (sotto i 750 euro netti si va al garden center).
- **Da noi:** Rizzi (Pasticcerie / Bar e ristoranti / Spaccio per i privati, tre blocchi con il loro colore); Fornasiero ("Per bar e ristoranti: pane consegnato ogni mattina", con il suo telefono o la sua email); Servalli e Foralberg (professionisti e privati separati da una regola, non mescolati nella stessa pagina); Bordin (Garden per i privati, Vivai per i professionisti e i giardinieri); Nic Dean (negozi e distributori da una parte, spaccio dall'altra).
- **Che cosa serve:** dall'azienda: chi risponde ai professionisti, con quale numero o email, e la regola (minimo d'ordine, zona di consegna, orari di consegna). Nessuna foto nuova.

### 6. Le prove con il nome, al posto delle cifre e dei testi generici
- **Esempio:** Rivolta (gli hotel con il logo); Benchmark (tre progetti con il nome); Old Empire e Bisca (premi con evento e anno); Tartine (la citazione di Vogue); Tricker's (la citazione con il nome, 1.292 recensioni).
- **Da noi:** Servalli (gli alberghi e i negozi clienti che si possono nominare); Rizzi (i sei clienti già citati sul loro sito, pasticcerie e distributori, con il paese); Bottega (Palazzo del Bo, la pasticceria vicino a Bolzano); Overdrive (premi e copertine, già fatto: tenerlo); Fornasiero (gli articoli del Mattino di Padova con la data, uno citato per intero); Scalarredo (le recensioni Google con nome e comune, se ci sono).
- **Che cosa serve:** l'elenco dei clienti nominabili, con il loro consenso; i ritagli di giornale con testata e data; i premi con evento e anno. Nessun dato inventato: se un'azienda non ha prove con il nome, la sezione non c'è.

### 7. Le persone della bottega, con nome e ruolo
- **Esempio:** Lorenz von Ehren (cinque colleghi con nome, ruolo e albero preferito); Tricker's e Crockett & Jones (operai al banco); Benchmark (gli apprendisti in bianco e nero); Architectural Plants (il titolare Guy Watts nominato nel benvenuto).
- **Da noi:** Bottega dell'Arte (Mauro Nosarini e Giuliano Saibene al banco: oggi 13 immagini e nessuna con loro); Fornasiero (Galileo, Fidalma, Filippo, Romina, Michele); Bordin (la terza generazione, chi segue Garden, Vivai e Giardini); Distilleria Rizzi (Maddalena e Alessandro, già nel loro sito); Artificio (Matteo con la cornice, già c'è: farne la foto di sezione); Nic Dean (la famiglia Nicoletto, se lo spaccio è aperto).
- **Che cosa serve:** da 2 a 6 ritratti fatti nello stesso giorno, con la stessa luce, anche al telefono, in bottega e non davanti a un muro bianco; oppure una sola foto di gruppo. Se non si possono fare, una foto d'archivio con i nomi in didascalia. È il punto in cui il servizio fotografico proposto a parte rende di più.

### 8. La sede come posto da visitare, con istruzioni da persona e appuntamenti con la data
- **Esempio:** Architectural Plants ("Book a visit", come arrivare in parole, "Dogs are always welcome"); Plain English ("Visit us at Stowupland Hall"); Cornelissen (tre riquadri uguali: telefono e orari, giro del negozio, indirizzo); Pigment Tokyo (workshop con data, orario, "Sold out"); Nardini (visite guidate); Tricker's (i negozi con la facciata e l'anno).
- **Da noi:** Bordin ("Il Garden al 6 e il vivaio al 14 di via dei Vivai, a Saonara: si parcheggia davanti"); Artificio (i corsi Artinpratica con data, ora, prezzo, posti e "esaurito"); Rizzi (lo spaccio di via Negri con l'invito a vedere il laboratorio, se lo fanno); Nic Dean (lo spaccio con la foto dell'ingresso e "dal 2013"); Bottega (la bottega di via Levico come posto dove portare un disegno o un mobile da restaurare); Fornasiero (il negozio "a pochi metri dal semaforo").
- **Che cosa serve:** la foto dell'ingresso o della facciata (si fa al telefono di mattina, con il sole alle spalle); le indicazioni scritte da chi ci lavora; il calendario degli eventi se c'è. La chiusura della home diventa i tre riquadri di Cornelissen: telefono e orari, il posto da vedere, l'indirizzo con "Indicazioni".

---

## 5. I tre siti migliori del gruppo
1. **Plain English** (plainenglishdesign.co.uk): la home più corta e più sicura, una foto, un manifesto, sei tessere, due azioni scritte; dimostra che il "su misura" si vende con la calma.
2. **Tartine** (tartinebakery.com): un forno con un carattere solo, una fotografia coerente, le sedi sul bordo della foto e la regola degli ordini scritta per intero.
3. **Tricker's** (trickers.com): una fabbrica di famiglia che mette la fabbrica, le persone, i negozi con l'anno e le prove con il nome in una pagina ordinata.
