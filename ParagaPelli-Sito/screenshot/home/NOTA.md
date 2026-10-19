# Paraga Pelli, home finale: "La mazzetta"

Pagina: `sito/index.html` (si apre anche da file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (catalogo, immagini, pagina, screenshot). Base: il prototipo A scelto dal committente, con le indicazioni del giudice e tre innesti dal prototipo B.

## L'idea

La home è la cartella colori di Paraga Pelli. In apertura una pelle drappeggiata a tutta pagina prende il colore vero del campione scelto; sopra, il nome dell'articolo e il codice del colore, grandi come l'intestazione di un cartellino; in fondo, la mazzetta con le linguette vere di quell'articolo. Si tocca un colore e cambia tutto: drappo, codice, cartellino con la scansione, campo LWG più in basso. Si tocca uno dei 27 dorsi (o un nome nella sezione degli usi) e la pagina torna in cima con la cartella di quell'articolo aperta. Con il nome di un concorrente non regge: "Botticelli 2117", "Madras testa di moro", "Sc 02", le 403 scansioni sono solo loro.

Alla domanda del committente ("se seleziono il materiale o il colore cambia l'immagine?"): sì, per tutti i 27 articoli e tutti i 403 colori, nella prima schermata. Cambiano il colore del drappo a tutta pagina, la scansione nel cartellino, il codice e, con l'articolo, nome, scheda e mazzetta. La fotografia del drappo resta la stessa (una pelle bianca tinta): dall'ultimo passaggio il suo colore è tarato sulla scansione di ogni campione.

## Le prime due schermate

1. **Apertura (1440x900).** Drappo nel colore Botticelli 2117 a tutta pagina. In alto "Botticelli" in Libre Caslon Display a 212 px e "2117" in Mona Sans stretto e leggero alla stessa misura. A destra il cartellino (scansione da 320 px di lato, materiale, spessore 1,3/1,5 mm, disegno dollaro, 24 colori, "A video il colore è indicativo"), come un cartoncino appoggiato: filo di 1 px e ombra dura di 2 px, niente ombra sfumata. A sinistra chi sono e cosa fanno, un solo invito ("Richiedi il box-campionario"). In fondo la mazzetta: la linguetta scelta sporge di 30 px, i codici sono in inchiostro o in carta secondo il contrasto con la scansione. Testata: menu e telefono a sinistra, lingue a filo del margine destro (x 1376), allineate al cartellino.
   A 390x844 tutto sta nella schermata: nome e codice su due righe allineate a sinistra, cartellino orizzontale, bottone a tutta larghezza meno 16 px per lato, mazzetta centrata sul colore scelto con i vicini ai lati e un tassello tagliato a ogni bordo, così si capisce che scorre.
2. **Catalogo.** "Ventisette articoli, 403 colori a campione": i 27 dorsi delle cartelle (scansione vera, nome in Libre Caslon, numero di colori), che sono anche il selettore degli articoli; sotto, le quattro famiglie con una riga di materiale ciascuna. Poi la corsia del magazzino a tutta larghezza col bordo vivo della pelle intera, gli usi riga per riga con i nomi degli articoli cliccabili, il campo nel colore scelto con la tabella LWG e il box-campionario, la squadra in magazzino sui bancali di pelli, i contatti sul cartellino della ditta, il piede con la fila dei 27 dorsi in piccolo e una riga sola.

## Cosa è cambiato rispetto al prototipo A

- Testata allungata fino al margine destro; il vuoto centrale a 1440 è riempito dal drappo: la mappa di luce è capovolta in verticale, così la piega chiara cade fra il titolo e il cartellino (a 1440x900 l'immagine copre la finestra quasi senza ritaglio e `object-position` non la spostava).
- Cartellino da 280 a 320 px, senza ombra sfumata; pallino della linguetta tolto; codici delle linguette leggibili sui chiari (2101-2108, 2121-2123).
- Colore del drappo: il tono è la media della superficie della scansione (pixel fra il 40 e il 90 percentile di luminanza), non la media semplice, che usciva grigia. Controllati a mano i 24 colori Botticelli e il primo colore di ogni articolo a 1440x900: bianchi e grigi chiari (2101-2105, 2121-2123) schiariti del 22% verso la carta con la mappa all'80%, se no erano grigio sporco; bordeaux (2118-2120) con la mappa più leggera e meno blu, se no le luci viravano al viola. Il dizionario è in `_prova/script/finale_correzioni.json`; gli altri articoli seguono la stessa regola nel codice. Il testo sopra il drappo sceglie inchiostro o carta su un tono scurito del 35%, perché il titolo cade anche nelle pieghe in ombra.
- Innesto da B: i 27 dorsi diventano selettori; la sagoma frastagliata della pelle intera usata una volta sola, come taglio del bordo inferiore della corsia del magazzino; la tabella LWG al posto del paragrafo; il nome nel piede a tutta misura (tolto nell'ultimo passaggio, vedi sotto).
- Parte bassa: tolto il dittico (poltrona e ricciolo); una sola foto larga; usi in righe con i nomi in Libre Caslon (niente tre colonne uguali); fascia LWG con tabella a sinistra e box-campionario a destra; contatti in una legenda a due colonne invece di quattro colonne (poi rifatti come cartellino, vedi "La chiusura").
- Dati: 403 colori ricontati sulle schede (A e B davano numeri diversi; il vecchio script di B perdeva cinque link), conteggio per articolo in `01-analisi.md`, sezione 2. Monza "spessore 1/1.1 mm" è sulla scheda (citata in analisi): resta. Fuori dalla pagina come prima: civico, forma giuridica, deposito di Altamura.
- Una scelta che si scosta dalla lettera delle indicazioni: toccando un dorso la cartella si apre sul colore del dorso, non sul primo della lista. Cinque articoli (Sera, Lana, Piston, Madras, Spessorato) cominciano col bianco: aprire sempre sul primo colore avrebbe dato un drappo bianco quasi una volta su due, e il dorso che si tocca avrebbe un colore diverso da quello che si apre.

## Caratteri e colori

- **Libre Caslon Display** (Pablo Impallari, Google Fonts, SIL Open Font License 1.1): solo i nomi delle linee (titolo d'apertura, cartellino, dorsi, usi, box). Un romano da stampa classica, dritto, senza corsivo, per nomi di pittori e di un doge. Riferimenti: Dedar (Lyon, serif editoriale piccolo e preciso) ed Edelman (serif di marca accanto a un grottesco).
- **Mona Sans** (GitHub, Google Fonts, SIL Open Font License 1.1, Reserved Font Name "Mona"), variabile in peso e larghezza: tutto il resto; il codice grande in peso 250 a larghezza 75. Riferimenti: ABC Diatype di Dedar, il grottesco di Kvadrat e Bridge of Weir. Numeri allineati proporzionali: le cifre tabellari di Mona Sans hanno lo zero barrato e l'1 con la grazia e a 13 px sembrano un monospazio (segnale da IA); dove serve l'allineamento i numeri stanno in colonne di tabella.
- File: i woff2 latini serviti da Google Fonts, non modificati, in `sito/fonts/` con `OFL-Mona-Sans.txt` e `OFL-Libre-Caslon-Display.txt`.
- Colori: carta pietra #ECEBE7 (dal fondo #EDEDE8 di Edelman), cartoncino #F7F6F2, inchiostro #1A1817. L'unico colore è quello del campione scelto, misurato sulla scansione (2117: #993B1D): drappo, campo LWG, bottone. Riferimento: Kvadrat, campioni posati sul tessuto dello stesso colore.

## Interazione

- Mazzetta: gruppo di radio; clic, tocco, frecce, Home e Fine; fuoco visibile. Cambiano in 260 ms il colore del drappo e del campo; codice, cartellino e linguetta cambiano subito. Su telefono scorre di lato a scatti (scroll-snap al centro).
- Dorsi: gruppo di radio con le frecce; tocco o Invio aprono l'articolo e riportano in cima (scorrimento morbido, istantaneo con "riduci movimento"); il fuoco passa alla linguetta scelta. Il dorso scelto resta sollevato con un filo sotto.
- Nomi negli usi: bottoni, stessa azione dei dorsi.
- Nome e codice si stringono da soli se non stanno nella riga ("Spessorato" con "testa di moro").
- Niente animazioni allo scorrere, niente effetti sul cursore, niente dissolvenze; con "riduci movimento" nessuna transizione.

## Foto, origine e licenza

| Dove | File in sito/img | Origine | Licenza |
|---|---|---|---|
| Apertura, drappo | `drappo-{800,1200,1680}.jpg`, `drappo-v-{480,651}.jpg` | sfondo della home di oggi `public__foto__sfondi__1__bg-home.jpg`, ridotto a mappa di luce e capovolto | dell'azienda, forse uno stock: da chiedere |
| Cartellino, mazzetta | `c/<articolo>/*.webp`, 403 file 350x350; `c2/<articolo>/*.webp`, le stesse a 640 per il cartellino in alta densità (Lanczos e maschera di contrasto leggera) | scansioni delle schede prodotto di paragapelli.com, colori non toccati | dell'azienda |
| Dorsi | `d-<articolo>.jpg`, 27 file 80x350 | striscia centrale di una scansione per articolo | dell'azienda |
| Box-campionario | `box-265.jpg` | `immagini/campionario.jpg` del sito, fondo bianco portato al cartoncino | dell'azienda |
| Magazzino | `corsia-{800,1200,1680}.jpg`, `corsia-v-500.jpg` | `immagini/paragapelli-visual-home.jpg` del sito (1680x400) | dell'azienda |
| Squadra | `squadra-{800,1200,1620}.jpg`, `squadra-v-{600,800}.jpg` | `public/foto/sfondi/2/bg_chisiamo.jpg` del sito (1620x800), sfondo di "Chi siamo" | dell'azienda (consenso delle persone da confermare) |

Gradazione unica sulle foto (saturazione 0,86; rosso +3%, blu -5%, neri a 14, bianchi a 250, maschera di contrasto), più larghezze con srcset. Le scansioni non sono gradate. Nessuna immagine generata.

## Controlli (passaggio precedente)

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920 (`_prova/finale/pezzi/`, `_prova/finale/controllo/`); prima schermata e cambio colore guardati per i 24 colori Botticelli e per i 27 articoli (`_prova/finale/tb*.jpg`, `ta*.jpg`).
- Nessuno scorrimento orizzontale, nessun elemento fuori dalla finestra, nessuna sovrapposizione; nessun U+2014 nella pagina, nel LEGGIMI e in questa nota.
- Interazione provata con Playwright a 1440 e 390: dorso Madras, poi "testa di moro" (nome e codice stanno nella riga), freccia destra sulla mazzetta, nome "Fuoco" negli usi; la pagina torna in cima ogni volta.
- (Passaggio precedente) `segnali.sh` a 1440: 0 soglie bloccanti. Foto 35,6%; nessun carattere della lista b; mono 0%; 0 etichette sopra i titoli; filetti 27 (sotto 30: sono le righe della tabella LWG, dei recapiti e degli usi); numero grande 1 ("2117", il codice del colore); date "2 febbraio 2026" e "2 febbraio 2027". Da guardare: H2 di una misura sola (56 px, voluto: l'elemento grande è il nome della linea, poi il nome nel piede); 5 fasce di fondo (apertura nel colore, carta, campo nel colore, carta, piede nero): due sono lo stesso colore scelto, che è l'idea.
- Divieti del committente: nessun gradiente, nessun testo in gradiente, niente emoji, niente Inter, nessuna card col bordo sinistro, niente vetro, niente modo scuro, nessuna fila di tre box con icona, nessun badge, nessuna icona, nessuna dissolvenza, niente effetti sul cursore, bottoni che cambiano colore pieno (non sbiadiscono), niente corsivo.

## Ultimo passaggio (dopo il giudice cieco: K0 7,5)

La prima schermata, l'idea, la tipografia e il colore restano quelli del prototipo A scelto. Cosa è cambiato:

- **Drappo e scansione d'accordo (bloccante).** Nuovo `_prova/script/finale_drappo.py`: per ogni colore simula la fusione soft-light del browser (in sRGB) sulla zona centrale del drappo e corregge il tono di base finché la media di quella zona coincide con la mediana della scansione in Lab. I colori con croma C* > 45 (61 su 403) hanno la mappa a 0,72, come i bordeaux. Delta E medio fra drappo e scansione: prima 7,5 sui saturi e 6,9 su tutti, ora 0,9 e 1,0 (massimo 1,7). Guardati a 1440x900 sugli screenshot veri: Sera 372 e 394, Lana 6699, Fuoco 10, Ocean 424, Madras giallo, Botticelli 2101, 2117, 2119, Creta black 06 (`_prova/finale/verifica/foglio-drappi.jpg`). Il rosa di Sera 372 non tira più al rosso, il verde di Lana non è più chiaro e giallo. Il dizionario a mano `finale_correzioni.json` ora dà solo le opacità.
- **Foto Unsplash tolta.** Al suo posto la corsia del magazzino (foto loro). Per non lasciare la pagina senza fotografie nella parte bassa, fra il campo LWG e i contatti c'è la squadra in magazzino sui bancali di pelli intere (sfondo della pagina "Chi siamo" del sito). In pagina ora solo immagini di Paraga Pelli.
- **Menu del telefono:** "Telefono 049 983 2030" con lo spazio (gap fra etichetta e numero); in fondo al menu le lingue IT EN DE FR PL.
- **Lingue** visibili in testata fino a 901 px (prima sparivano sotto 1180).
- **Cartellino fermo:** la scheda ha l'altezza della più alta dei 27 articoli, misurata alla larghezza corrente; la cima non si sposta più cambiando articolo (a 1440x900 sempre a 322 px su 403 colori). Scansione in 3:2 sopra i 600 px, così fra il codice grande e il cartellino restano almeno 32 px a 1440 e 25 a 1024.
- **320:** nome e codice a 18vw sotto i 360 px e 18 px fra il codice e il cartellino (prima 0).
- **Apertura:** l'altezza minima resta la finestra (fra 720 e 1080 px) ma il contenuto non viene più tagliato: a 1024x768 la mazzetta prima perdeva 64 px sotto il bordo, ora si vede con i codici e il resto scende di poco.
- **Codici sulle linguette** su un tassello di cartoncino con l'inchiostro, come i numeri dei dorsi: si leggono anche sulle scansioni di tono medio (Botticelli 2111, 2115, Fuoco 16, 18, 26). I nomi lunghi ("bianco", "testa di moro") in corpo 10.
- **Cartellino in alta densità:** a DPR 2 il browser carica la scansione a 640 (`img/c2/`), più nitida della 350 ingrandita.
- **Dati:** Madras "rosso f" diventa "rosso F" (la scheda tronca il nome, il file è `MADRAS_ROSSO_F.jpg`: la F resta come sigla, da chiedere); Spessorato "1,3/1,5 mm" (la scheda omette l'unità, segnalato nel LEGGIMI).
- **Preload dei caratteri tolti:** da file:// davano 4 errori CORS; i @font-face caricano comunque. Console senza errori.
- **Piede:** tolto "Paraga Pelli" a tutta misura; al suo posto il nome in piccolo, "27 cartelle colori, 403 campioni" e la fila dei 27 dorsi come indice di chiusura.

## Controlli dell'ultimo passaggio

- `bash _prova/script/build_finale.sh` e poi `node _prova/script/finale_verifica.mjs <sito/index.html> _prova/finale/verifica`.
- Screenshot guardati a pezzi a 1440 e 390 (`_prova/finale/pezzi/`), prime schermate a 320, 768, 1024 e 1920 (`_prova/finale/controllo/`), menu aperto a 390 e 320, cartellino a DPR 2.
- scrollWidth uguale a innerWidth a 320, 360, 375, 390, 414, 600, 601, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560.
- Per tutti i 403 colori a 1440, 1920, 1024, 768, 390 e 320: nome e codice dentro la riga, nessuna sovrapposizione fra testo, cartellino e mazzetta.
- Tastiera a 1440: frecce, Fine e Home sulla mazzetta (2117, 2118, 2119, 2125, 2101, 2125: cambiano codice, drappo e scansione); freccia sui dorsi (Botticelli, poi Sera 372), Invio riporta in cima col fuoco sulla linguetta. Tocco a 390: linguetta 2120, poi "Piston" negli usi riporta in cima su Piston 8371. Nessun errore in console.
- Collegamenti: `tel:+390499832030`, mailto a info, ordini, amministrazione, sales (e info con oggetto "Richiesta box-campionario"), Google Maps con "Paraga Pelli Via del Lavoro Tombelle di Vigonovo", scheda LWG, Facebook. Lingue e Privacy a "#" finché non esistono.
- `segnali.sh` a 1440: 0 soglie bloccanti. Foto 36,2%, mono 0%, 27 filetti, un numero grande (2117), date LWG. Da guardare come prima: H2 di una misura sola, 5 fasce di fondo (due sono il colore scelto).
- Nessun U+2014 in pagina, in questa nota e nel LEGGIMI.

## Cosa manca per arrivare a 8 sulla prima schermata

La prima schermata non è stata ripensata, come chiesto. Il colore del drappo ora coincide con la scansione, ma il drappo resta una sola foto bianca (forse stock) tinta: cambia il colore, non la fotografia, e la piega è la stessa per i 403 colori. Le scansioni d'origine sono a 350 px: la versione a 640 è più nitida, ma non aggiunge dettaglio vero. Per arrivare a 8 servono le foto vere del drappo nei colori più venduti e le scansioni a 1200 px (LEGGIMI, foto da rifare 1 e 2).

## La chiusura: il cartellino della ditta (passaggio del 19 ottobre)

Il committente ha notato che quasi tutte le home della campagna finivano uguali: titolo di luogo, telefono grande, una legenda o una riga di colonnine con indirizzo ed email, piede scuro. Anche questa: "Tombelle di Vigonovo, zona industriale", legenda a due colonne col telefono a 28 px, piede nero con nome, fila dei dorsi e sei voci in riga. Rifatte solo la sezione dei contatti e il piede; il resto della pagina non è cambiato.

- **I recapiti sul cartellino.** La pagina si apre con un cartellino appoggiato sul drappo (scansione, nome in Libre Caslon, codice, scheda a righe, nota in piccolo). La chiusura è lo stesso oggetto, più largo e disteso in orizzontale come il cartellino del telefono: cartoncino #F7F6F2, filo di 1 px e ombra dura di 2 px; a sinistra la scansione del colore scelto in cima alla pagina con il suo tassello ("Botticelli 2117", cambia con la mazzetta, coi dorsi e con i nomi degli usi); a destra "Paraga Pelli" in Libre Caslon dove sta il nome della linea e "Contatti" dove sta il codice; al posto di materiale, spessore e disegno le righe Sede e magazzino (con "Apri in Google Maps"), Telefono, Fax, Informazioni, Ordini, Amministrazione, Ufficio estero; in fondo, dove il cartellino dice "A video il colore è indicativo", la nota "Per ordini e campioni indicate articolo e codice del colore, come sul cartellino: Botticelli 2117" col colore scelto. Un solo oggetto, che chi compra da una cartella colori riconosce, e che serve: dice cosa scrivere nell'email.
- **Perché così e non altro:** il titolo di luogo e la legenda andavano bene per qualunque azienda; il cartellino c'è già in apertura, è il loro modo di presentare un articolo, e chiude la pagina con la stessa cosa con cui la apre.
- **Telefono:** `tel:+390499832030`, 30 px leggero e stretto come il codice (28 px al telefono), sottolineato, area toccabile alta 44 px; non è più un numero gigante. Email in `mailto:`, mappa come collegamento. Tutti i dati erano già in pagina: nessun dato nuovo (niente civico, niente forma giuridica, niente PEC: non sono in pagina).
- **Piede:** non più nero a più voci. Sulla carta della pagina, la fila dei 27 dorsi (che è loro) e sotto una riga sola: Paraga Pelli, P.IVA 03748440272, Facebook, Privacy. Indirizzo, telefono ed email non si ripetono: sono sul cartellino subito sopra. Tolto anche "27 cartelle colori, 403 campioni", già nel titolo del catalogo.
- **Misure:** cartellino sulle colonne 3-10 a 1440 (866 px), 2-11 fino a 1180, a tutta larghezza fino a 900 con la scansione a 2/7, sotto i 600 px in verticale con la scansione in una fascia alta 96 px e le etichette sopra i valori. L'indirizzo va a capo dopo "Via del Lavoro," e "30030 Tombelle di Vigonovo (VE)" non si spezza.
- **Contrasto (AA):** etichette e note #5E5A56 su cartoncino 6,3:1; testo e collegamenti #1A1817 su cartoncino 16,4:1; piede #5E5A56 su carta 5,7:1, inchiostro su carta 14,8:1; tassello 15,7:1.
- **Script:** contatti e piede in `_prova/script/finale_modello.html` (CSS "contatti: il cartellino della ditta" e "piede", HTML della sezione `#contatti` e del `footer`, tre righe in `scegli()` per la scansione e il nome del colore); `finale_scatti.mjs` salva anche la chiusura a 1440 e `build_finale.sh` la porta in `screenshot/home/chiusura-1440.jpg` (JPEG 85, dall'inizio della sezione contatti alla fine della pagina).
- **Controlli:** chiusura guardata a pezzi a 1440, 1024, 768, 390, 320 e 1920; a tutte le larghezze scrollWidth uguale alla finestra, nessun elemento fuori, nessun testo che esce dal cartellino, nessuna sovrapposizione fra i testi (misurata coi rettangoli), link del telefono 44 px di altezza. A 390: "Madras" negli usi e poi "testa di moro" cambiano scansione, tassello e nota del cartellino; console senza errori. Nessun U+2014 in pagina, in questa nota e nel LEGGIMI. Divieti: nessun gradiente, niente emoji, niente Inter, nessuna card col bordo sinistro, niente vetro, niente fondo scuro, nessuna fila di box con icona, nessun badge sopra il titolo, nessuna icona, nessuna dissolvenza o effetto sul cursore, niente corsivo.
- `segnali.sh` non è stato rifatto in questo passaggio: le fasce di fondo scendono da 5 a 4 (il piede nero non c'è più).
