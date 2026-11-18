# 01. Analisi del sito attuale (www.hotelgaribaldi.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare con il cliente, **[DA CONFERMARE]** dato che non va pubblicato finché il cliente non lo conferma.
Prove: crawl completo in `_prova/crawl/` (131 pagine HTML, testi estratti in `_prova/crawl/testi/`), screenshot a 1440 e 390 in `_prova/attuale/`, misure di rete in `_prova/attuale/misure-1440.json` e `misure-390.json`, inventario foto in `_prova/inventario-immagini.json`.

## In breve

- Albergo 3 stelle a Ponte di Brenta, periferia est di Padova, a 400-500 m dal casello Padova Est della A4 e a 4 km dalla Fiera. Clientela dichiarata: turisti e lavoro, fiere ed eventi al Palasport San Lazzaro (1 km). [Certo]
- Sito WordPress **3.9.34** (ramo del 2014) con un tema TemplateMonster (CherryFramework, `theme49248`) e jQuery 1.7.2. Due lingue (italiano, inglese) con il plugin mqTranslate. Ultimi articoli del 23 e 30 luglio 2014, ultime foto caricate il 29 gennaio 2019, mappa nel piè di pagina sostituita a gennaio 2024. [Certo]
- **Il problema più grave è commerciale**: tutti i pulsanti "book now" e tutti i prezzi del listino (11 link nella sola pagina Camere e Listino, 8 pagine in tutto) portano al motore di prenotazione Ericsoft, che risponde "Il modulo "Booking Engine" non è attivo per questa struttura" e resta su una rotella di caricamento (provato con 45 secondi di attesa). Da sito non si può prenotare. [Certo]
- La versione inglese dei Servizi è ancora piena di testo finto del template ("Mauris fermeum dictum magna...") in tutti e sei i box, visibile. Il titolo della pagina è "Servces". [Certo]
- **Nessuna foto delle camere** sul sito: il box "Rooms" della home mostra un corridoio. Le foto professionali del 2019 (8, larghe 440-880 px) mostrano la facciata rinnovata, i corridoi, i dettagli. Foto di camera e bagno rinnovati esistono sul portale turistico della Regione Veneto (1024x768). [Certo]
- Identità attuale: logo PNG 183x115 con "Hotel Garibaldi" in carattere graziato a contorno e tre stelle dorate (manca il vettoriale); sito in giallo paglia #EDD47C, antracite #383338 e arancio #F35508 (pulsante "book now") del tema. La facciata rinnovata (rivestimento antracite, insegna "HOTEL***" luminosa, palme) è il materiale più forte. [Certo]
- **Correzione rispetto alla ricerca preliminare**: la sezione "Location" della home **non è vuota**. Lo script vecchio della mappa ha davvero le coordinate vuote e va in errore (`LatLng(, )`), ma il suo contenitore si chiama `map_old` e accanto c'è una mappa Google incorporata (iframe, gennaio 2024) che si vede, a 1440 e a 390 (`_prova/attuale/91-home-location-1440.png`, `-390.png`). Il vuoto negli screenshot a pagina intera è un difetto della cattura (gli iframe di Google escono bianchi). Non va scritto nella PEC. [Certo]
- Anche i segnaposto "Cliente: / Data: / Info: / Lancia Progetto" della galleria sono nel codice ma **nascosti** (larghezza 0, non visibili neanche al passaggio del mouse): sono un problema di pulizia, non qualcosa che il cliente vede. [Certo]

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home IT | `/` | slider di 3 foto 1980x867 (reception, portachiavi, facciata vecchia) con didascalie, blocco "Verifica disponibilità on-line" + "book now", 3 box con titoli inglesi (Hotel, Rooms, Events), 6 servizi, galleria a scorrimento, "About us" con QR code e contatti, "Location" con mappa Google |
| Home EN | `/en/` | stessa home: slider in inglese tranne la terza didascalia, box e servizi in italiano |
| L'Albergo | `/albergo/` (EN `/en/albergo/`) | 3 colonne (L'albergo, Comodità, Prenotazione), "What we offer" con i 2 articoli del 2014, galleria |
| Camere e Listino | `/camere-e-listino/` (EN `/en/camere-e-listino/`) | listino a forchetta per 6 tipologie, offerta "LAST MINUTE WEEK END Luglio e Agosto", 2 articoli 2014, galleria; nessuna foto di camera |
| Servizi | `/servizi/` (EN `/en/servizi/`) | 6 box con icona; in inglese tutti con testo finto |
| Dove Siamo | `/dove-siamo/` (EN `/en/dove-siamo/`, titolo "Contact us") | mappa Google incorporata, cartina disegnata del percorso dal casello, indicazioni (treno, bus, aeroporti, autostrada), modulo contatti Contact Form 7 con captcha, contatti |
| Offerta manifestazioni fieristiche | `/offerte/offerta-manifestazioni-fieristiche/` | articolo del 30 luglio 2014 |
| HOTEL *** | `/news/offerta-hotel/` | articolo del 23 luglio 2014, quasi uguale al precedente |
| Archivi | `/category/news/`, `/offerte/` (= `/category/offerte/`), `/author/admin/` | elenchi degli stessi 2 articoli; `/author/admin/` espone il nome utente "admin" |
| News | `/news/` (in sitemap) | **404** "Spiacente! Pagina non trovata" |
| Galleria | `/portfolio_category/photogallery/` + `page/2/` ... `page/6/` | 28 schede foto ("Foto 01" ... "Foto 27" + `suspendisse-arcu-nisl`, slug del template) |
| Schede foto | `/portfolio-view/foto-01/` ... `/foto-27/` | una foto per scheda, nessun testo |
| Feed | `/feed/` | ultimi 2 articoli del luglio 2014 |

La sitemap (`/sitemap.xml`, 71 URL in http) ha come ultima modifica il 22 settembre 2014. Il menu ha 5 voci: Home, L'Albergo, Camere e Listino, Servizi, Dove Siamo (in inglese: Home, Hotel, Rooms and Prices, Servces, Contact us).

## Testi reali (verbatim, con i refusi originali)

Home (slider e blocchi):
1. Didascalie slider: "Offriamo il massimo del comfort ad un prezzo da sogno" / "Più di quanto si possa immaginare" / "Tranquillità e raffinatezza esclusiva".
2. "Verifica disponibilità on-line. Controlla la disponibilità per il periodo del tuo soggiorno e prenota subito senza carta di credito, pagherai direttamente in Hotel." (pulsante "book now")
3. Box: "Hotel a Padova. Situato a Padova in posizione strategica tra l'autostrada e la Fiera, a 10 minuti dal centro" / "Un soggiorno esclusivo. Offriamo comfort e servizi all'altezza di un Hotel 3 stelle a prezzi interessanti" / "Eventi a Padova. Concerti, mostre, teatri, ... scropri i migliori eventi in programma a PADOVA" (link a joylife.it, 404).
4. Piè di pagina: "Hotel Garibaldi *** / Via San Marco, 63 - 35129 Padova - Italy / tel. +39 049 893.24.66 r.a. / fax +39 049 893.24.63 / info@hotelgaribaldi.com", poi "Hotel Garibaldi © 2026 ©" e "creazione siti web" (link ad adwebstudio.it). In testata: "(+39) 049 893 24 66".

L'Albergo:
5. "L'Hotel Garibaldi si trova a Padova in posizione strategica tra l 'autostrada e la Fiera di Padova, a 10 minuti dal centro di Padova."
6. "Nato pochi anni fa' il nostro Hotel si presenta sul mercato turistico alberghiero come una struttura moderna in posizione strategica che si adatta dunque sia al turista che alla clientela di affari. Facilmente raggiungibile dall' autostrada A4 (400 metri casello PD Est) offre a chi soggiorna camere accoglienti con tutti i comfort e un ampio giardino con parcheggio privato."
7. "Posizione strategica per ogni meta. A soli 15 minuti dal centro di Padova e 10 minuti dalla Zona Fiera, con autobus (linea 18) ogni 15 minuti spostarsi non è mai stato così semplice. Ci troviamo ad 1 solo chilometro dal Palasport San Lazzaro. Bus diretto per l'areoporto Marco Polo di Venezia ogni mezz'ora."
8. "Trova subito la tua stanza ideale. Verifica la disponibilità direttamente on-line e prenota immediatamente il tuo confortevole soggiorno nella maniera più comoda e sicura. Aprofitta subito delle nostre occasioni e delle offerte dell'ultimo minuto pensate apposta per te. Ti aspettiamo!"

Camere e Listino:
9. Sottotitolo: "Offriamo il massimo del confort ad un prezzo da sogno".
10. "Listino Prezzi: CAMERA SINGOLA: 50 – 62 euro / MATRIMONIALE USO SINGOLO: 58 – 69 euro / CAMERA DOPPIA: 60 – 92 euro / CAMERA MATRIMONIALE: 60 – 110 euro / CAMERA TRIPLA: 80 – 130 euro / CAMERA QUADRUPLA: 100 – 140 euro"
11. "Offerte: LAST MINUTE WEEK END Luglio e Agosto / prenotabile solo con e-mail a: info@hotelgaribaldi.com / Camera dopppia euro 55 / Camera singola euro 45 / Camera doppia + letto euro 70 / Camera quadrupla (2 doppie comunicanti) euro 110"
12. "I prezzi sono per camera, comprensivi di colazione a buffet – parcheggio auto – servizio wirelles in camera e IVA al 10%"
13. Versione inglese diversa: matrimoniale "60 – 92 euro", tripla "80 – 110 euro", "LAST MINUTE WEEK END Luglio e Agosto 2014", "Prices per person per day. Breakfast included. Tax IVA 20%".

Servizi (uguali in home):
14. "Tv LCD in camera con Mediaset Premium. In ogni camera puoi vedere gratuitamente tutti i canali di Mediaset Premium Calcio e Cinema"
15. "Accessibile ai disabili. Abbattimento completo delle barriere architettoniche, ll nostro Hotel è totalmente a norma per l'accessibilità da parte di portatori di handicap."
16. "Connessione WiFi. Collegamento WiFi disponibile gratuitamente in ogni camera o luogo all'interno dell'Hotel."
17. "Colazione. Ricca colazione a Buffet con Brioche fresche, vari dolci, Yogurt, Cereali, Frutta, Affettati, formaggi, Succhi, ecc."
18. "Parcheggio (Gratis). Parcheggio privato gratuito con 50 posti auto."
19. "Frigo bar. Frigo bar su tutte le camere."
20. Inglese: titoli "Tv LCD with Sky", "Wheelchair accessible", "Wireless connection", "Breakfast", "Parking", "Mini bar", tutti con lo stesso testo finto: "Mauris fermeum dictum magna. Sed loreet aliquam leote llus dolor dapibus eget elementum vel curseifend elit. Aenean aucto. wisi et urna. Aliqat volutpat. Duisac turpis. Integer rutrum ante eu lacuestibul."

Dove Siamo:
21. "TRENO + BUS: La stazione ferroviaria di Padova rispetto all' Hotel Garibaldi *** si trova a soli 10 minuti di auto e a 15 minuti di bus (numero 18). Vi è poi la nuova stazione ferroviaria di Busa di Vigonza che dista dalla nostra struttura 2 minuti d'auto o di bus. In suddetta stazione è possibile prendere i treni direzione Venezia e direzione Padova ed è possibile usufruire del suo ampio parcheggio gratuito." (link all'orario della linea 18 su apsholding.it: 404)
22. "AEROPORTO DI VENEZIA "MARCO POLO": Bus diretto "PADOVA AUTOSTAZIONE" Partenze ai minuti 05 e 35 di ogni ora: durata 1 ora e 10 minuti Distanza = 41 km" (link "Orari Corse SITA": errore 500)
23. "AEROPORTO DI TREVISO "ANTONIO CANOVA": Bus diretto "PADOVA AUTOSTAZIONE" Partenze ai minuti 22 e 52 durata del viaggio : 1 ora e 8 minuti Distanza = 38 km"
24. "AUTOSTRADA : Arrivando da Bologna prendere svincolo per A4 Milano – Venezia Arrivando da Venezia; Milano prendere Uscita Padova Est, poi seguire in direzione Vigonza – Ponte di Brenta (distanza dall'Hotel – 500mt)". In inglese in più: "A soli 200 m dall' IKEA".
25. "FIERA DI PADOVA: 4 km (10 min in auto; bus ogni 25 minuti) / PALASPORT SAN LAZZARO: 1 km"
26. Modulo "Contattaci senza impegno": Nome (*), E-mail (*), Telefono, Messaggio, captcha. Frase: "Con l'invio del presente modulo acconsento al trattamento dei dati personali trasmessi. Consenso esplicito secondo il D.Lgs 196/2003."
27. Contatti: "Hotel Garibaldi / Via San Marco, 63 / 35129 Padova – Italy / Telefono: +39 049 893.24.66 r.a. / FAX: +39 049 893.24.63 / E-mail: info@hotelgaribaldi.com"

Articoli 2014:
28. "Offerta manifestazioni fieristiche" (30 luglio 2014): "Prezzi per evento Doppia o Matrimoniale euro 55,00 . Doppia uso singola euro 50,00 compreso colazione a buffet – parcheggio -servizio wireless gratuito – Pacchetto Mediaset Premium Calcio e Cinema GRATUITI -Tale offerta non è valida per la fiera delle auto e moto d'epoca di Padova che si terrà ad ottobre-"
29. "HOTEL ***" (23 luglio 2014): stesso testo senza l'esclusione.

Testo della scheda regionale (Veneto Around Me), uguale al sito: "Nato pochi anni fa, il nostro Hotel si presenta sul mercato turistico alberghiero come una struttura moderna..." [Certo]

Refusi e incoerenze da non riportare: "fa'", "l 'autostrada", "dall' autostrada", "Aprofitta", "areoporto", "ll nostro Hotel", "scropri", "dopppia", "wirelles", "confort" accanto a "comfort", "Servces", "Was borned". Distanze discordanti: centro a 10 o 15 minuti, casello a 400 o 500 m, stazione "10 minuti di auto" (IT) o "5 km" (EN). Listino IT e EN con prezzi diversi per matrimoniale e tripla, IVA 10% contro 20%, prezzi "per camera" contro "per person per day". "Nato pochi anni fa" è scritto almeno dal 2014: l'anno di apertura non c'è. Nel nuovo sito il nome si scrive **Hotel Garibaldi**, le stelle si dicono "3 stelle".

## Cosa fanno o vendono

- **Camere**: singola, matrimoniale uso singolo, doppia, matrimoniale, tripla, quadrupla (anche come 2 doppie comunicanti). Numero totale di camere non dichiarato sul sito; i portali Hotels.com/Expedia indicano 46 camere [DA CONFERMARE]. Dotazioni dichiarate: TV LCD, frigobar, WiFi gratuito; i portali aggiungono aria condizionata, asciugacapelli, finestre insonorizzate [DA CONFERMARE]. [Certo per il sito]
- **Prezzi** in forchetta (50-140 euro a camera, colazione, parcheggio e WiFi compresi): fermi almeno dal 2014, da non pubblicare senza conferma [DA CONFERMARE].
- **Servizi**: colazione a buffet, parcheggio privato gratuito con 50 posti, accessibilità per persone con disabilità, WiFi gratuito, frigobar, giardino. Le foto mostrano anche un bar (bottigliera) e una sala colazione con vetrate sul giardino. Google segnala "Ristorante: sì" e "Animali ammessi: no" [DA CONFERMARE]. "Mediaset Premium Calcio e Cinema" va verificato: secondo la stampa i canali Premium hanno lasciato il digitale terrestre il 1° giugno 2019 [Probabile].
- **Posizione**: Via San Marco 63, Ponte di Brenta, a 400-500 m dal casello Padova Est (A4), 200 m da IKEA (testo inglese), 1 km dal Palasport San Lazzaro, 4 km dalla Fiera di Padova, bus 18 per il centro e la stazione, stazione di Busa di Vigonza a 2 minuti. Coordinate 45,42205 N 11,93762 E (Google). [Certo]
- **Clientela**: lavoro e fiere (offerta fiere, vicinanza a casello e Fiera), turismo (Padova; Venezia a 20 minuti d'auto secondo i portali [DA CONFERMARE]), eventi. [Certo]
- **Prenotazione**: oggi solo telefono, email e modulo (il motore Ericsoft non è attivo). Presenza su Booking.com, Expedia, Hotels.com, Kayak, Trip.com. [Certo]
- **Recensioni**: Google 4,1 su 906 recensioni (dato letto dalla scheda il 6 ottobre 2026) [Certo]. Booking.com non leggibile (blocca i robot). Non vanno pubblicate recensioni senza permesso.

## Immagini usate oggi

Tutte scaricate in `assets/originali/` (40 file, nomi parlanti, `manifest.json` con URL d'origine e pagine). Il sito non usa `srcset`: gli originali WordPress senza `-370x247` sono la risoluzione più alta. Nessun PDF o catalogo.

| Gruppo | Quantità | Dimensione | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Servizio professionale del 29/01/2019 (facciata rinnovata di sera e di giorno, fiori con controluce, bar con orchidee, consolle con specchio dorato, corridoio con statue, fiori, corridoio camere) | 8 | 880x660 (4) e 440x660 (4) | ottima qualità, nitide, luce curata; **piccole** | il materiale principale: a 880 px al massimo (440 px CSS su retina). Niente apertura a tutta larghezza |
| Slider 2014 (reception in noce, portachiavi GH, facciata vecchia) | 3 | 1980x867 | discreta, compatta amatoriale; la facciata è quella prima del rinnovo | reception e portachiavi utilizzabili larghi se la hall è ancora così [DA CONFERMARE]; facciata vecchia no |
| Foto 2014 (giardino e parcheggio, bagno con lavabo blu, atrio con lucernario, corridoio, veranda, ingresso vecchio) | 7 | 525-880 px | media, iPhone 5; alcune superate dal rinnovo | dettagli piccoli; bagno e ingresso vecchi no |
| Foto 2011-2012 (sala colazione, salotto rosa, reception, cartella in pelle, telecomando Mediaset) | 14 | 370-1024 px | bassa o superata, molto compresse | quasi nessuno; sala colazione 1024 px solo se invariata [DA CONFERMARE] |
| Miniature e grafiche (box home 370 px, QR code, cartina del percorso 501 px con testo nell'immagine, sfondo testata, Prato della Valle demo) | 7 | 183-1980 px | non utilizzabili | nessuno; Prato della Valle è di provenienza ignota |
| Logo PNG | 1 | 183x115 | troppo piccolo, nessun vettoriale | solo riferimento: chiedere il vettoriale |

Foto mostrate più grandi della loro misura: miniatura 370x247 mostrata a 620 px nelle due pagine articolo (x1,68), foto 440x660 mostrata a 770 px nella galleria (x1,75) (misurato da `naturalWidth` contro larghezza a schermo, `_prova/attuale/misure-1440.json`).

Foto trovate fuori dal sito (`assets/esterne/`, `manifest.json`):
- **Regione del Veneto, portale Veneto Around Me** (scheda con CIN): 4 foto 1024x768: facciata rinnovata di giorno, **camera matrimoniale rinnovata** (parete blu, legno chiaro, balcone), **bagno rinnovato** (doccia in vetro, gres beige; scatto da smartphone), atrio con lucernario. Sono le uniche foto di camera e bagno attuali. Utilizzabili previa conferma.
- **Google, scheda dell'hotel**: 1 foto caricata dal proprietario (facciata di sera, 1024x683, 19/08/2024). La scheda dichiara 457 foto, quasi tutte di utenti.
- **Foto di terzi** (13, utenti Google 2022-2026, fino a 4000 px): camere, hall con pavimento a intarsio, buffet della colazione, salotto, parcheggio. **Non utilizzabili**: servono per capire come sono oggi gli ambienti e per il brief fotografico.
- Booking.com blocca i robot (403): nessuna foto scaricata. Facebook e Instagram: nessun profilo ufficiale trovato. Wayback Machine non raggiungibile da questo ambiente.

Conclusione sul materiale: **13 foto utilizzabili e attuali** (8 del 2019 a 440-880 px, 4 della Regione a 1024 px, 1 Google a 1024 px), più 2 foto larghe 1980 px del 2014 (reception e portachiavi) da confermare. Nessuna foto supera i 1024 px tranne lo slider 2014: il design deve lavorare con foto a mezza larghezza o a riquadri, non con aperture a tutto schermo; serve un servizio fotografico nuovo di camere, colazione e hall (o gli originali del fotografo del 2019).

## Problemi tecnici da segnalare al cliente

Misure prese il 6 ottobre 2026 con Chromium (Playwright) attraverso il proxy di questo ambiente: numero di richieste e peso sono affidabili, i tempi assoluti sono pessimistici.

1. **Prenotazione online non funzionante.** Tutti i "book now" e tutti i prezzi del listino (11 link in Camere e Listino, 8 pagine con il link) aprono `booking.ericsoft.com/BookingEngine/Book?idh=1604DB72868FF5A5`; la chiamata `api/book/GetConfiguration` risponde "Il modulo "Booking Engine" non è attivo per questa struttura" e la pagina resta su una rotella di caricamento dopo 45 secondi. La home promette "prenota subito senza carta di credito". Prova: `_prova/attuale/90-prenota-ericsoft-dopo-45s.png`, `_prova/crawl/esterne/ericsoft.json`. [Certo]
2. **Testo finto del template nella versione inglese.** `/en/servizi/`: 6 box su 6 con "Mauris fermeum dictum magna...", visibile (controllato nel DOM e nello screenshot `_prova/attuale/pezzi/11-en-servizi-lorem.jpg`); titolo "Servces". Gran parte della versione inglese è in italiano (box della home, servizi in home, listino, indicazioni). [Certo]
3. **Contenuti e prezzi fermi.** Ultimi articoli del 23 e 30 luglio 2014 (feed `/feed/`), offerta "LAST MINUTE WEEK END Luglio e Agosto" (in inglese "2014"), listino IT e EN con prezzi diversi e IVA al 10% contro 20%, servizio "Mediaset Premium Calcio e Cinema" da verificare. La pagina `/news/` è in sitemap ma risponde 404. Il "© 2026" del piè di pagina è generato in automatico (e il simbolo è ripetuto: "© 2026 ©"). [Certo]
4. **Software del 2014.** `<meta name="generator" content="WordPress 3.9.34">`, `/readme.html` raggiungibile, jQuery 1.7.2, tema TemplateMonster CherryFramework, Contact Form 7 3.9. Il ramo 3.9 di WordPress non riceve più aggiornamenti di sicurezza (dal dicembre 2022 secondo l'annuncio di WordPress) [Probabile]. `/author/admin/` espone il nome utente "admin". [Certo]
5. **Errore JavaScript in home a ogni caricamento.** `SyntaxError: Unexpected token ','` dallo script vecchio della mappa (`new google.maps.LatLng(, );`, riga 456 dell'HTML), più gli avvisi Google Maps "NoApiKeys" e "SensorNotRequired". Non ha effetti visibili perché la mappa mostrata è un iframe separato: è codice morto che carica comunque le API di Google Maps. [Certo]
6. **Peso e richieste.** Home a 1440: fino a **126 richieste e 2,3 MB** (51 immagini 1,28 MB, 47 script 805 KB, 18 CSS, 4 font), 7 domini esterni (Google Fonts, Google Maps, netdna.bootstrapcdn.com per Font Awesome 3.2.1). Da 60 a 102 richieste nelle pagine interne. TTFB dell'HTML 0,6-2,9 s; load della home 10 s nella misura migliore. [Certo]
7. **Link rotti.** Box "Events" verso `joylife.it/hotelgaribaldi.com` (404, 2 link in home IT e EN); orario linea 18 su `apsholding.it` (404, 3 pagine); "Orari Corse SITA" su `ro.autobus.it` (errore 500); 5 icone social in testata con `href="#"` (Facebook, Google+ chiuso dal 2019, RSS, Pinterest, LinkedIn); `/news/` 404. [Certo]
8. **Privacy e cookie.** Nessuna informativa privacy e nessuna cookie policy in tutto il sito (nessun link "privacy" o "cookie" in 131 pagine); nessun banner; Google Fonts, Google Maps (iframe e API) e Font Awesome da CDN si caricano prima di qualsiasi consenso; il modulo contatti cita il "D.Lgs 196/2003" (pre GDPR) senza link a un'informativa. [Certo]
9. **Dati obbligatori mancanti.** Nessuna ragione sociale né P.IVA nelle pagine (home, albergo, dove siamo, piè di pagina); manca anche il **CIN** (codice identificativo nazionale IT028060A173Q36JDQ, pubblicato dalla Regione), che va esposto negli annunci della struttura [Probabile per l'obbligo sul sito proprio]. [Certo per l'assenza]
10. **Mobile.** Nessuno scorrimento orizzontale a 390 (scrollWidth 390 su tutte le 13 pagine misurate). Però: menu come `<select>` nativo, didascalia dello slider in maiuscolo sopra il logo, telefono mai cliccabile (nessun link `tel:` nel sito), da 10 a 31 link o bottoni sotto i 24 px per pagina, home lunga 5.179 px a 390. Screenshot: `_prova/attuale/01-home-390.png`, `03-camere-e-listino-390.png`. [Certo]
11. **SEO di base.** Meta description vuota in home e ridotta a "» Pagina" nelle interne, 4 H1 in home (tra cui "Verifica disponibilità on-line"), titoli inglesi del template sulla home italiana (Hotel, Rooms, Events, Our services, Gallery, About us, Location), 28 schede foto senza testo con titoli "Foto 01"... e uno slug del template (`suspendisse-arcu-nisl`), nessun dato strutturato, nessun Open Graph, sitemap in http del 2014. [Certo]
12. **Testi in immagine.** La cartina "percorso evidenziato" (501x318) contiene nomi di vie, IKEA, A4, uscita Padova Est: illeggibili a 390 e non indicizzabili. [Certo]

Cosa **non** è un problema (verificato, da non usare nella PEC):
- La sezione "Location" mostra una mappa Google funzionante (iframe del gennaio 2024), a 1440 e a 390.
- HTTPS attivo: certificato Let's Encrypt valido fino al 25/12/2026, http e dominio senza www reindirizzati con 301 su `https://www.`.
- `viewport` presente, nessuno sbordamento orizzontale a 390.
- I segnaposto della galleria ("Cliente:", "Lancia Progetto") non sono visibili.
- Durante le misure da 1 a 8 risorse su circa 120 sono tornate 502 o interrotte a ogni caricamento: può dipendere dalla rete di questo ambiente, non è attribuibile al server con certezza. [Ipotesi]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Insegna | Hotel Garibaldi, 3 stelle | sito, Regione Veneto, Google [Certo] |
| Società | **A.L.P. S.r.l.**, P.IVA e C.F. 02209920285, REA PD-214632, capitale sociale 60.000 euro, costituita nel 1988, attiva | aziende.it (fonte Registro Imprese, aggiornato 8/7/2026), companyreports.it [Certo per i dati]. Legame con l'hotel: stessa sede, 7 dipendenti, ricavi coerenti con un albergo, ma ATECO dichiarato 68.20.01 "Locazione immobiliare di beni propri" [Probabile: A.L.P. gestisce l'hotel; **DA CONFERMARE prima di inviare la PEC**] |
| Dati economici | fatturato 891.542 euro nel 2024 (+23,6% sul 2022), utile 4.568 euro, costo del personale 163.415 euro, 7 dipendenti | aziende.it, companyreports.it |
| PEC | a.l.p.srl@pec.it | aziende.it (verificare su INI-PEC prima dell'invio) [Probabile] |
| Sede | Via San Marco 63, 35129 Padova (Ponte di Brenta); la Regione usa CAP 35020 | sito, Google, Regione |
| Telefono | 049 893 2466 (+39 049 893.24.66 r.a.) | sito, Google |
| Fax | 049 893 2463 | sito, Regione |
| Email | info@hotelgaribaldi.com | sito |
| CIN | IT028060A173Q36JDQ | Veneto Around Me (Regione del Veneto) [Certo] |
| Orari | reception, check-in e check-out non pubblicati [DA CONFERMARE] | |
| Anni di attività | non dichiarati ("Nato pochi anni fa'" dal 2014 almeno); società dal 1988; facciata rinnovata prima del gennaio 2019 [DA CONFERMARE] | |
| Lingue parlate | tedesco, inglese, francese, spagnolo | Regione Veneto [Certo] |
| Social | nessun profilo ufficiale trovato | ricerca del 6/10/2026 |
| Marchi, certificazioni | nessuno dichiarato | |
| Fornitori web | sito di adwebstudio.it (link "creazione siti web"), hosting Ergonet (intestazione `x-server-powered-by: Ergonet FireShield`) | sito [Certo] |

## URL vecchi

95 URL in `_prova/crawl/url-vecchi.txt` (pagine raggiungibili più quelle della sitemap). Per `plugin/redirect-301.csv`:

- Pagine: `/`, `/albergo/`, `/camere-e-listino/`, `/servizi/`, `/dove-siamo/` e le stesse sotto `/en/` (`/en/`, `/en/albergo/`, `/en/camere-e-listino/`, `/en/servizi/`, `/en/dove-siamo/`).
- Articoli e archivi: `/offerte/offerta-manifestazioni-fieristiche/`, `/news/offerta-hotel/`, `/offerte/`, `/category/offerte/`, `/category/news/`, `/news/` (oggi 404), `/author/admin/`, `/feed/`, e gli equivalenti `/en/...`.
- Galleria: `/portfolio_category/photogallery/` e `/page/2/` ... `/page/6/`; 28 schede `/portfolio-view/foto-01/` ... `/foto-27/` e `/portfolio-view/suspendisse-arcu-nisl/`, tutte anche sotto `/en/`.
- Link brevi in uso nel sito: `/albergo`, `/camere-e-listino`, `/dove-siamo` (senza barra) e `/?p=N` (reindirizzati da WordPress).
