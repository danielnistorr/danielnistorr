# L'Artificio Battagin, home finale "Il miglior vestito"

Pagina: `sito/index.html` (5.692 px a 1440 con il piede, 7.468 px a 390). Rigenerazione: `bash _prova/script/build_finale.sh`.

## L'idea

Una sola cornice vera, grande e nitida, appesa a un muro chiaro nella luce di una finestra, e accanto la loro frase: "Ogni quadro ha bisogno del suo miglior vestito" (post "Laboratorio di cornici artigianali" del 30/03/2023). La cornice è il vestito, e si cambia come in negozio: cinque profili presi dalle loro foto la rivestono al tocco. Il profilo di partenza è il rosso e oro della cornice che Matteo tiene in mano nella foto subito sotto, così la prima e la seconda schermata si parlano e con il nome di un altro corniciaio la pagina non regge.

## Prima schermata (ripensata rispetto al prototipo A)

- La foto stock della cornice in rovere non si vede più: al suo posto c'è una cornice disegnata pixel per pixel (Python, PIL e OpenCV) con i listelli veri ritagliati dalle loro foto, tagliati a 45°, con giunti, battuta, luce da destra e ombra di contatto. La foto del muro resta solo come muro: la sua cornice in rovere cade esattamente sotto quella disegnata, che ne eredita l'ombra. Le cinque cornici sono immagini WebP a 1x, 1,5x e 2x: a 1440 sono nitide.
- 1440: titolo Gambetta 104 px su tre righe, con l'altezza delle maiuscole della prima riga allineata al bordo alto della cornice (168 px); cornice di 480 px; sotto, "Prova il profilo sulla cornice" e i cinque campioni da 64 px con 16 px tra l'uno e l'altro e il filetto verde di 2 px su quello scelto. Il fondo dei campioni è allineato al fondo del bottone verde (764 px), così le due colonne chiudono alla stessa altezza.
- Sottotitolo con il negozio in testa: "Un negozio di belle arti per chi dipinge, disegna e incide, e un laboratorio dove tagliamo e assembliamo cornici su misura", con l'indirizzo che porta alla mappa. Azioni: "Chiamate lo 049 7811043" (tel:) e "Shop online".
- La tavola si ferma a 1600 px: a 1920 resta centrata e la cornice cade sempre allo stesso punto. Tra 700 e 1099 px due colonne in flusso; sotto 700 px titolo, muro con la cornice, campioni, sottotitolo, bottone. A 390 titolo, cornice e campioni stanno nella prima schermata.

## Seconda schermata e resto

Matteo con la cornice rossa e oro (foto loro) e "La corniceria, uno dei vanti dell'Artificio", con le tre lavorazioni della pagina Cornici. Poi la parete degli angolari a tutta larghezza sul turchese (titolo a sinistra e testo a destra sulla stessa linea di base), unica fascia di colore. "Una famiglia amante dell'arte" con le cinque vie (Via Cavalletto con "In seguito", Via della Croce Rossa "Dal 2007"). Belle arti: la cassetta-cavalletto col marchio scontornata sulla carta, a sinistra, e cinque reparti con i marchi a destra, più "Lo shop online" e "Tutti i reparti". Artinpratica: i prossimi tre appuntamenti con data, docente, orari "dalle ... alle ..." e prezzo a destra. Chiusura "b con foto" e piede.

## Caratteri e colori

- Gambetta 400 (titoli, vie, reparti, corsi, telefono grande), mai in corsivo; Switzer 400 e 500 (testo, menu, date e prezzi in cifre tabellari). Tutti e due di Indian Type Foundry da Fontshare, ITF Free Font License (uso commerciale libero), serviti da `sito/fonts/`. Gambetta perché è un serif da libro con le grazie taglienti e l'occhio largo, vicino alle insegne serif dei corniciai storici (Bourlet, Lowy, Cornelissen), senza l'aria da lusso di moda; Switzer è un grottesco neutro e leggibile che non è nella lista dei caratteri da IA.
- Colori: carta #F6F3EE, inchiostro #1F1B17, grigio #5E564D (6,5:1 sulla carta), verde Battagin #17633A (il verde della scritta del logo scurito: 6,6:1 sulla carta, bianco sul verde 7,3:1) per bottoni, link e la sede di oggi, turchese #CFE7E4 (il colore della parete degli angolari) per una sola fascia, testo #3B4644 sul turchese (7,6:1).
- Riferimenti: Bourlet (un solo angolo di cornice grande, frase serif, il verde), Arnold Wiggins (telefono e indirizzo in chiaro), Cornelissen (il negozio di colori raccontato come istituzione); nella campagna la prima schermata di Hambro e di Mario Agnoletto (un oggetto vero, grande, titolo sicuro, tanta aria), ma senza legende.

## Interazione

"Prova il profilo": cinque bottoni radio (rosso e oro, oro barocco, argento barocco, nero intagliato con passepartout tagliato a 45°, laccato blu). Al clic o al tocco la cornice cambia di netto, senza dissolvenza, e sotto cambia la frase (dalla pagina Cornici). Tastiera: frecce, Home e Fine, focus visibile; al telefono bottoni da 64 px. Provato con `_prova/script/prova_gesto.mjs`: clic e tasti corretti, nessun errore in console. Nessuna animazione allo scorrere, niente effetti che seguono il cursore.

## Foto, origine e licenza

- Muro dell'apertura: "a square wooden frame hanging on a wall", In The Making Studio, Unsplash `gx6NxtpgHqY`, Unsplash License (verificata il 24/10/2026, vedi `assets/CREDITI.md`). Bianco portato al colore carta, sfumato a sinistra e in basso. Non usata in altre home della campagna.
- Cornici e campioni: listelli dalle foto dell'azienda. Rosso e oro: il lato alto della cornice di Matteo (`2023-05_339083708_...jpg`, raddrizzata di 28,2°); oro e argento barocco: i listelli sul banco (`2023-04_cornici-1.jpg`); nero intagliato: un angolare della parete nella foto di Matteo; laccato blu: la sezione di un angolare blu della parete (`2023-05_cornici-per-grafica.jpg`), estrusa. Composizione grafica, da sostituire con la foto vera (indicazioni nel LEGGIMI).
- Matteo: `2023-05_339083708_...jpg` (1080 px). Parete degli angolari: `2023-05_cornici-per-grafica.jpg` (1000 px, a 1440 ingrandita: serve l'originale). Cassetta-cavalletto: `2024-07_IMG_0393-scaled.jpg` (2560 px), solo la cassetta aperta, scontornata dal grigio con ombra morbida intera. Chiusura: cavalletti in faggio `2023-07_IMG_7395-2-scaled.jpg` (2560 px), diversa da tutte le foto sopra.
- Logo: PNG originale 250x117 mostrato a 120-125 px (2x). Nessuna immagine generata dall'IA.

## Chiusura e piede

- Chiusura: "Da sempre luogo dove si danno appuntamento artisti e appassionati d'arte" (descrizione della categoria Workshop del loro calendario) in Gambetta 60 px su tre righe, testo a sinistra e i cavalletti a destra fino al bordo (562 px di altezza). Recapiti: 049 7811043 grande in verde (tel:), cellulare 380 2308602 (tel:), negozio@artificiobattagin.it (mailto:), Via della Croce Rossa 5/a con il link alla mappa, "Ampio parcheggio privato". Orari non ancora: non sono confermati.
- Piede: logo e una riga su chi sono, a destra la newsletter (sì, perché hanno clienti privati, 22 corsi nel 2026, promozioni e un articolo quasi ogni mese, e la newsletter ce l'hanno già): campo, bottone verde e consenso. Sotto quattro colonne con titoletti Switzer 500 a 13 px e voci a 15 px #5E564D: Negozio, Artinpratica, Contatti, Seguici (solo Instagram e Facebook, in parole). In fondo A.B. s.r.l., P.IVA 04191710286, REA PD 369492, Condizioni di vendita, Resi e rimborsi, Spedizioni e pagamenti, Privacy, Cookie. A 390 le colonne vanno a due a due.

## Controlli

- Guardati a pezzi: 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 1024, 1920, più i profili oro (390) e nero (1440). Nessuno scorrimento orizzontale a 320, 390, 700, 768, 900, 1024, 1099, 1440 e 1920; nessuna sovrapposizione.
- `_metodo/kit/segnali.sh` a 1440: 0 soglie da correggere su 10, 0 da guardare su 8 (foto al 42,8 % della pagina, Switzer 84 % e Gambetta 16 %, 3 misure di H2, 3 fasce, 16 filetti larghi, nessuna freccia).
- Contrasti AA verificati (sopra). Nessun carattere U+2014 nella pagina, nella NOTA e nel LEGGIMI; nessuna lineetta negli orari.
- Dati: tutti da `01-analisi.md` e dal crawl (`il-negozio/`, `cornici/`, `belle-arti/`, `contatti/`, `events.json`, piede del sito). Lo sconto del 15% della newsletter, gli orari, il capitale sociale e la PEC sono fuori dalla pagina e nel LEGGIMI.
- Nota: Gambetta compare anche nella home di Ruffatti della campagna (le foto invece non si ripetono).
