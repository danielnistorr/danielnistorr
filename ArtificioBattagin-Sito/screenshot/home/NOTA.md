# L'Artificio Battagin, home finale "Il miglior vestito" (terza versione, 2/11/2026)

Pagina: `sito/index.html` (6.018 px a 1440 con il piede, 7.360 px a 390). Rigenerazione: `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, prova del gesto con clic, tastiera e tocco, larghezze, collegamenti, segnali).

Questa versione rifinisce la seconda (stesso giorno) secondo il giudizio cieco (K0 7, K1 7, 59 su 80). L'idea resta quella: la loro frase è il quadro dentro la cornice. Cambia la proporzione della cornice, che ora è un quadro e non uno striscione, e la pagina si accorcia di un elenco.

## L'idea

La loro frase, "Ogni quadro ha bisogno del suo miglior vestito" (post "Laboratorio di cornici artigianali" del 30/03/2023), non sta accanto a una cornice: **è il quadro dentro la cornice**. Il titolo è stampato sul foglio, dentro un passepartout con la finestra tagliata a 45° (la loro particolarità, dalla pagina Cornici), e sul passepartout, in basso a destra e in piccolo come una firma a matita, c'è "Taglio a 45°, laboratorio di via della Croce Rossa". Si cambia profilo come in negozio: quattro angolari rivestono il titolo di netto. Il profilo di partenza è il rosso e oro della cornice che Matteo tiene in mano nella foto subito sotto: la prima e la seconda schermata si parlano, e con il nome di un altro corniciaio la pagina non regge (la firma e la cornice di Matteo sono solo loro).

## Cosa è cambiato rispetto alla seconda versione

1. **La cornice è un quadro in 4:3**: 860 x 640 px a 1440 (era 1.200 x 488, un rapporto da striscione), a filo del margine sinistro della testata (x 80). Titolo Gambetta 84 px su tre righe dentro la finestra ("Ogni quadro ha / bisogno del suo / miglior vestito"). A destra, nella colonna x 1004-1360, il mestiere, il testo, il telefono e i campioni, tutto entro i 900 px della prima schermata; sotto si vede l'inizio della foto di Matteo.
2. **La firma del laboratorio sul passepartout**: il legame con loro si vede senza leggere la didascalia. Sotto i 360 px resta solo "Taglio a 45°".
3. **Il mestiere in apertura**: la colonna si apre con "Negozio di belle arti con laboratorio di cornici, a Padova." in Gambetta 28 px (l'ATECO è 47.62.20, la cornice è uno dei reparti), poi "Colori, carte e pennelli per chi dipinge, disegna e incide. E un laboratorio interno dove tagliamo e assembliamo cornici su misura, in via della Croce Rossa 5/a."
4. **Tolto il laccato blu**: era un'estrusione sintetica di una sezione, si vedeva accanto all'oro e all'argento fotografati. Restano quattro profili, tutti ritagliati da foto loro.
5. **La parete degli angolari non è più ingrandita**: la sorgente è larga 1000 px e ora si mostra al massimo a 1000 px CSS, a filo del bordo destro; il titolo "Gli angolari campione, appesi in negozio" diventa la sua didascalia, a sinistra, ancorato alla base della foto.
6. **Le cinque vie in un paragrafo**: niente più elenco numerato. "Una famiglia amante dell'arte" è un titolo e un solo paragrafo in Gambetta 29 px con le vie nel testo, dalle parole della pagina Il negozio; "Dal 2007 siamo in via della Croce Rossa" in verde. Sparisce la voce vuota "In seguito, Via Cavalletto". Elenchi in pagina: tre (lavorazioni, reparti, calendario).
7. **La chiusura senza vuoto**: frase e recapiti sono un solo blocco centrato in verticale sulla foto, con il telefono a 48 px dalla frase. La foto è ritagliata solo sul legno (fuori i neon e il controsoffitto): il dettaglio della cassetta-cavalletto in faggio, con il leggio, i galletti in ottone e il cassetto a coda di rondine, alta 628 px a 1440.
8. **Matteo intero**: la foto è quasi quadrata (1080 x 1020), con tutta la cornice dentro e il banco dei listelli in basso a sinistra. A 1024 foto e titolo partono dalla stessa riga.
9. **Piede al telefono**: le voci delle colonne hanno un bersaglio di 39 px (padding 8 px sopra e sotto), 31 px sul computer.

## Rispetto alla campagna (richiesta del 2 novembre)

- **Niente legende sull'oggetto**: nessun pallino, nessun filetto numerato. Sotto i campioni una sola didascalia, il nome del profilo con una frase della pagina Cornici.
- **Il fondo viene dal mestiere**: il turchese della parete degli angolari del loro negozio, schiarito in #D9E8E4. La parete vera si vede dietro Matteo e nella foto degli angolari, con lo stesso colore: la pagina è il muro del laboratorio su cui la cornice è appesa. Il piede passa al bianco del passepartout (#F8F6F0).
- **Un'impaginazione che nella campagna non c'è**: il titolo sta **dentro** l'oggetto, come opera incorniciata, e l'oggetto è un quadro appeso a sinistra con una colonna stretta da cartellino di galleria a destra, invece del titolo a sinistra con l'oggetto scontornato a destra. Nel corpo, la parete degli angolari a filo del bordo destro con il titolo come didascalia, la storia in un solo paragrafo grande, il calendario a una riga per appuntamento a tutta larghezza.

## Prima schermata a 1440

- Testata: logo PNG a 120 px, cinque voci di menu, telefono.
- Cornice 860 x 640 (rosso e oro, listello 60 px); passepartout con margini 56, 56 e 76 px (più largo in basso, come si fa in bottega); finestra 628 x 388 con lo smusso chiaro in basso e a sinistra e in ombra in alto e a destra (luce dall'alto a destra, la stessa dei listelli); il foglio è un poco più caldo del passepartout.
- Titolo Gambetta 400 a 84 px, interlinea 1,02, spaziatura -0,022em, centrato su tre righe.
- Colonna a destra larga 356 px: mestiere in Gambetta 28 px, testo Switzer 17 px, bottone verde "Chiamate lo 049 7811043" (tel:) e "Shop online"; poi un filetto, "Provate un altro profilo sul titolo", i quattro campioni da 64 px e la didascalia, che finisce a 50 px sopra la base della cornice.
- Tecnica: la cornice è un `border-image` disegnato fuori dal passepartout (`border-image-outset`), con i quattro listelli tagliati a 45° e il tratto centrale ripetuto senza giunte (`round`). Cambiare profilo cambia solo il listello: finestra e titolo restano fermi al pixel (provato: h1 sempre in 216,298 con i quattro profili).
- A 1920 la tavola si ferma a 1.600 px: cornice 956 x 711, colonna da 396 px. Da 960 a 1199 la stessa composizione con la colonna più stretta e campioni da 54 px; da 700 a 959 la cornice va in tavola sopra (titolo su tre righe) e sotto il testo a sinistra e i campioni a destra.

## Prima schermata a 390

Testata con logo a 88 px, "Menu" e telefono; la cornice a tutta larghezza meno 16 px (listello a metà spessore), il titolo a 37 px su quattro righe dentro la finestra e la firma; poi i quattro campioni da 60 px, la didascalia, il mestiere, il testo e il bottone del telefono, tutto nella prima schermata da 844 px. A 320 il titolo scende a 28 px e la firma si accorcia.

## Caratteri e colori

- **Gambetta 400** (titoli, mestiere, storia, reparti, corsi, telefono grande), mai in corsivo; **Switzer 400 e 500** (testo, menu, didascalie, date e prezzi: le cifre di Switzer sono tabellari, tutte larghe 576 unità). Tutti e due di Indian Type Foundry, da Fontshare, **ITF Free Font License** (uso commerciale libero, anche sul web; i file non si possono rivendere), serviti da `sito/fonts/` in woff2.
- Perché: Gambetta è un serif da libro con grazie taglienti e occhio largo, vicino alle insegne serif dei corniciai storici (Bourlet, Lowy, Cornelissen) senza l'aria da moda di lusso; dentro la finestra sembra davvero un foglio stampato. Switzer è un grottesco neutro che non sta nelle liste della guida.
- Colori: muro #D9E8E4, passepartout #F8F6F0, foglio #F1EDE4, inchiostro #1F1B17 (13,5:1 sul muro), grigio #4A5553 (6,1:1 sul muro, 7,2:1 sul passepartout), verde Battagin #17633A (il verde di BATTAGIN nel logo, scurito: 5,8:1 sul muro, 6,7:1 sul passepartout; bianco sul verde 7,3:1). Contrasti AA per testo normale.
- Riferimenti: Bourlet (un solo angolo di cornice grande, frase serif, il verde), Arnold Wiggins (telefono e indirizzo in chiaro), Cornelissen (il negozio di colori raccontato come istituzione), Sennelier (un oggetto solo con molta aria).

## Interazione

"Provate un altro profilo sul titolo": quattro bottoni radio (rosso e oro, oro barocco, argento barocco, nero intagliato). Al clic o al tocco la cornice cambia di netto e la didascalia cambia frase (testi dalla pagina Cornici). Tastiera: frecce, Home e Fine, focus visibile verde; al telefono bottoni da 60 px. I listelli degli altri profili si caricano dopo la pagina, così il cambio è immediato. Nessuna animazione allo scorrere, niente effetti che seguono il cursore, nessuna dissolvenza.

## Foto, origine e licenza

Tutte le immagini sono dell'azienda, prese dal loro sito (servizio fotografico del 2023 e foto del 2023-2024); nessuna foto di repertorio, nessuna immagine generata dall'IA, nessuna usata in altre home della campagna.
- Listelli della cornice e campioni: ritagliati dalle loro foto. Rosso e oro: il lato alto della cornice di Matteo (`2023-05_339083708_...jpg`, raddrizzata di 28,2°); oro e argento barocco: i listelli sul banco (`2023-04_cornici-1.jpg`); nero intagliato: un angolare della parete nella foto di Matteo. È una composizione grafica, da sostituire con le scansioni vere (LEGGIMI).
- Matteo: `2023-05_339083708_...jpg`, 1080 x 1020. Parete degli angolari: `2023-05_cornici-per-grafica.jpg` intera, mostrata al massimo a 1000 px CSS. Cassetta-cavalletto: `2024-07_IMG_0393-scaled.jpg` (2560 px), solo la cassetta aperta, scontornata con ombra morbida sul colore del muro, al 54 % della larghezza. Matite: `2023-04_matite-1.jpg` (tagliata in alto a destra per togliere l'etichetta del marchio), a 1:1. Chiusura: `2023-07_IMG_7395-2-scaled.jpg` ritagliata a 1712 x 1307 dal basso a sinistra (solo il legno della cassetta-cavalletto).
- Esportate con PIL in più larghezze (srcset): 620-1440 px in JPEG qualità 80-84, listelli e campioni in WebP.

## Chiusura e piede

- Chiusura "b con foto", testo a sinistra e foto a destra fino al bordo: "Da sempre luogo dove si danno appuntamento artisti e appassionati d'arte" (descrizione della categoria Workshop del loro calendario) in Gambetta 60 px; a 48 px il 049 7811043 grande in verde (tel:), cellulare 380 2308602 (tel:), negozio@artificiobattagin.it (mailto:), Via della Croce Rossa 5/a con il link alla mappa, "Ampio parcheggio privato". Niente orari: non sono confermati.
- Piede sul bianco del passepartout: logo PNG a 125 px (2x) con una riga su chi sono; a destra la newsletter (sì: hanno clienti privati, 22 corsi nel 2026, promozioni e un articolo quasi ogni mese, e una newsletter ce l'hanno già) con campo, bottone verde e consenso; sotto quattro colonne: Negozio, Artinpratica, Contatti, Seguici (solo Instagram e Facebook, in parole); in fondo A.B. s.r.l., P.IVA 04191710286, REA PD 369492, Condizioni di vendita, Resi e rimborsi, Spedizioni e pagamenti, Privacy, Cookie. A 390 le colonne vanno a due a due. Il modulo non invia nulla finché non è collegato, e lo dice.

## Controlli (2/11/2026)

- Guardati a pezzi: 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 960, 1024 (intera), 1920.
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 430, 600, 699, 700, 768, 900, 959, 960, 1024, 1099, 1100, 1199, 1200, 1280, 1440, 1600, 1920 e 2560 (`_prova/script/controlli_finali.mjs`).
- Gesto: clic sui quattro profili, frecce, Fine, Home a 1440 (`prova_gesto.mjs`) e tocco a 390: cornice, radio e didascalia corrette, h1 fermo, nessun errore in console, nessun file mancante. Menu del telefono: si apre e aria-expanded passa a true.
- Collegamenti: tel:+390497811043, tel:+393802308602, mailto:negozio@artificiobattagin.it, la mappa di Google su "Via della Croce Rossa 5/a, 35129 Padova".
- `_metodo/kit/segnali.sh` a 1440: 17 soglie su 18 a posto. L'unica segnata è l'area coperta da foto, 34,2 % contro 35 %: lo strumento conta solo `img` e sfondi, non il `border-image` della cornice d'apertura, che è fatta di listelli fotografati e copre 860 x 640 px; contandola si arriva a circa 40 %. Non è un segnale vero: la pagina ha sei foto loro più la cornice. Switzer 73 %, Gambetta 27 %; 4 misure di H2; 2 fasce (il muro e il piede); 16 filetti larghi; nessuna freccia, nessuna etichetta maiuscola, nessuna numerazione.
- Nessun carattere U+2014 nella pagina, nella NOTA, nel LEGGIMI e nei CREDITI.
- Dati: tutti da `01-analisi.md` e dal crawl (`il-negozio/`, `cornici/`, `belle-arti/`, `contatti/`, `events.json`, piede del sito). Lo sconto del 15 %, gli orari, il capitale sociale e la PEC restano fuori dalla pagina e sono nel LEGGIMI.
