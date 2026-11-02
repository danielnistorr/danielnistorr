# L'Artificio Battagin, home finale "Il miglior vestito" (seconda versione, 2/11/2026)

Pagina: `sito/index.html` (6.431 px a 1440 con il piede, 7.531 px a 390). Rigenerazione: `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, prova del gesto, segnali).

Questa versione sostituisce quella del 24/10/2026 (la pagina della prima versione è in `_prova/versione-1/index.html`, senza immagini; lo script delle sue immagini è `_prova/script/img_finale_v1.py`). Resta l'idea scelta dal giudice (prototipo A con gli innesti di B); cambiano la prima schermata, il colore di fondo, il calendario e il piede, come chiesto dal committente il 2 novembre ("più roba di alta gamma, meno uguali tra loro").

## L'idea

La loro frase, "Ogni quadro ha bisogno del suo miglior vestito" (post "Laboratorio di cornici artigianali" del 30/03/2023), non sta accanto a una cornice: **è il quadro dentro la cornice**. Il titolo è stampato sul foglio, dentro un passepartout con la finestra tagliata a 45° (la loro particolarità, dalla pagina Cornici), e la cornice gli sta intorno. Si cambia come in negozio: cinque angolari rivestono il titolo di netto, senza dissolvenza. Il profilo di partenza è il rosso e oro della cornice che Matteo tiene in mano nella foto subito sotto: la prima e la seconda schermata si parlano, e con il nome di un altro corniciaio la pagina non regge.

## Cosa cambia rispetto alla campagna (richiesta del 2 novembre)

1. **Niente legende sull'oggetto**: nessun pallino, nessun filetto numerato. Sotto i campioni c'è una sola didascalia, il nome del profilo con una frase della pagina Cornici.
2. **Il fondo viene dal mestiere**: è il turchese della parete degli angolari del loro negozio (la stessa che si vede dietro Matteo e nella foto a tutta larghezza), schiarito in #D9E8E4. La ragione si vede: due schermate più sotto la parete vera ha lo stesso colore, e la pagina diventa il muro del laboratorio su cui la cornice è appesa. Il piede passa al bianco del passepartout (#F8F6F0): l'unico cambio di fondo.
3. **Un'impaginazione che nella campagna non c'è**: composizione simmetrica e centrata, con il titolo da 84 px **dentro** l'oggetto (la cornice è larga 1.200 px su 1.440, l'83 %), invece del titolo a sinistra con l'oggetto scontornato a destra. Sotto la cornice due blocchi allineati ai suoi bordi esterni: a sinistra il sottotitolo e le azioni, a destra i campioni allineati a destra. Nel corpo, il calendario di Artinpratica è una riga per appuntamento a tutta larghezza (data, titolo, docente e orari, prezzo), sotto la foto delle matite che entra fino al bordo destro con il testo ancorato alla sua base.

## Prima schermata a 1440

- Testata: logo PNG a 120 px, cinque voci di menu, telefono.
- Cornice da 1.200 x 488 px (con il rosso e oro), centrata; passepartout con margini 56, 56 e 76 px (più largo in basso, come si fa in bottega); finestra con lo smusso chiaro in basso e a sinistra e in ombra in alto e a destra (luce dall'alto a destra, la stessa dei listelli); il foglio è un poco più caldo del passepartout.
- Titolo Gambetta 400 a 84 px su due righe centrate, interlinea 1, spaziatura -0,022em.
- Sotto, a 40 px: "Un negozio di belle arti per chi dipinge, disegna e incide, e un laboratorio dove tagliamo e assembliamo cornici su misura. In via della Croce Rossa 5/a, Padova." (l'indirizzo apre la mappa), il bottone verde "Chiamate lo 049 7811043" (tel:) e "Shop online"; a destra "Provate un altro profilo sul titolo", i cinque campioni da 64 px a 16 px l'uno dall'altro con il filetto verde di 2 px sul profilo scelto, e la didascalia.
- In fondo alla finestra si vede l'inizio della foto di Matteo, che invita a scorrere.
- Tecnica: la cornice è un `border-image` disegnato fuori dal passepartout (`border-image-outset`), con i quattro listelli tagliati a 45° e il tratto centrale ripetuto senza giunte (`round`). Cambiare profilo cambia solo il listello: finestra e titolo restano fermi al pixel (provato: h1 sempre in 256,258 con tutti e cinque i profili). Le sorgenti sono WebP a 2x (da 2 a 53 kB).

## Prima schermata a 390

Testata con logo a 88 px, "Menu" e telefono; la cornice a tutta larghezza meno 16 px (listello a metà spessore), il titolo a 37 px su quattro righe bilanciate dentro la finestra; poi i cinque campioni da 60 px, la didascalia, il sottotitolo, il bottone del telefono e Shop online, tutto nella prima schermata da 844 px. A 320 il titolo scende a 30 px e va a capo in modo naturale.

## Il resto della pagina

Matteo con la cornice rossa e oro (64 % della larghezza, fino al bordo) e "La corniceria, uno dei vanti dell'Artificio" con le tre lavorazioni; la parete degli angolari a tutta larghezza (1.440 x 809), con il titolo a sinistra e il testo a destra sulla stessa linea di base; "Una famiglia amante dell'arte" con le cinque vie (Via Cavalletto "In seguito", Via della Croce Rossa "Dal 2007"); belle arti con la cassetta-cavalletto col marchio scontornata sul colore del muro e cinque reparti con i marchi; Artinpratica con la foto delle matite e i tre appuntamenti; la chiusura; il piede.

## Caratteri e colori

- **Gambetta 400** (titoli, vie, reparti, corsi, telefono grande), mai in corsivo; **Switzer 400 e 500** (testo, menu, didascalie, date e prezzi: le cifre di Switzer sono già tabellari, tutte larghe 576 unità). Tutti e due di Indian Type Foundry, da Fontshare, **ITF Free Font License** (uso commerciale libero, anche sul web; i file non si possono rivendere), serviti da `sito/fonts/` in woff2.
- Perché: Gambetta è un serif da libro con grazie taglienti e occhio largo, vicino alle insegne serif dei corniciai storici (Bourlet, Lowy, Cornelissen) senza l'aria da moda di lusso; dentro la finestra sembra davvero un foglio stampato. Switzer è un grottesco neutro che non sta nelle liste della guida. Gambetta compare in un'altra sola home della campagna (Ruffatti).
- Colori: muro #D9E8E4 (parete degli angolari schiarita), passepartout #F8F6F0, foglio #F1EDE4, inchiostro #1F1B17 (13,5:1 sul muro), grigio #4A5553 (6,1:1 sul muro, 7,2:1 sul passepartout), verde Battagin #17633A (il verde di BATTAGIN nel logo, scurito: 5,8:1 sul muro, 6,7:1 sul passepartout; bianco sul verde 7,3:1). Contrasti AA verificati per testo normale.
- Riferimenti: Bourlet (un solo angolo di cornice grande, frase serif, il verde), Arnold Wiggins (telefono e indirizzo in chiaro), Cornelissen (il negozio di colori raccontato come istituzione), Sennelier (un oggetto solo con molta aria). Dalla campagna tengo solo la ricetta del committente (un oggetto vero, grande, titolo sicuro, tanta aria); l'impianto della prima schermata è diverso da tutte le copertine di `_invio/zona/home/`.

## Interazione

"Provate un altro profilo sul titolo": cinque bottoni radio (rosso e oro, oro barocco, argento barocco, nero intagliato, laccato blu). Al clic o al tocco la cornice cambia di netto e la didascalia cambia frase (testi dalla pagina Cornici). Tastiera: frecce, Home e Fine, focus visibile verde; al telefono bottoni da 60 px. I listelli degli altri profili si caricano dopo la pagina, così il cambio è immediato. Provato con `_prova/script/prova_gesto.mjs`: clic e tasti corretti, nessun errore in console, nessun file mancante. Nessuna animazione allo scorrere, niente effetti che seguono il cursore, nessuna dissolvenza.

## Foto, origine e licenza

Tutte le immagini sono dell'azienda, prese dal loro sito (servizio fotografico del 2023 e foto del 2023-2024); nessuna foto di repertorio, nessuna immagine generata dall'IA, nessuna usata in altre home della campagna.
- Listelli della cornice e campioni: ritagliati dalle loro foto. Rosso e oro: il lato alto della cornice di Matteo (`2023-05_339083708_...jpg`, raddrizzata di 28,2°); oro e argento barocco: i listelli sul banco (`2023-04_cornici-1.jpg`); nero intagliato: un angolare della parete nella foto di Matteo; laccato blu: la sezione di un angolare blu della parete (`2023-05_cornici-per-grafica.jpg`), estrusa. È una composizione grafica, da sostituire con le scansioni vere (LEGGIMI).
- Matteo: `2023-05_339083708_...jpg` (1080 px). Parete degli angolari: `2023-05_cornici-per-grafica.jpg` intera (1000 px, a 1440 ingrandita: serve l'originale). Cassetta-cavalletto: `2024-07_IMG_0393-scaled.jpg` (2560 px), solo la cassetta aperta, scontornata dal grigio con ombra morbida, posata sul colore del muro. Matite: `2023-04_matite-1.jpg` (1000 px, tagliata in alto a destra per togliere l'etichetta del marchio). Chiusura: cavalletti in faggio `2023-07_IMG_7395-2-scaled.jpg` (2560 px), diversa da tutte le foto sopra.
- Esportate con PIL in più larghezze (srcset): 620-1440 px in JPEG qualità 80-84, listelli e campioni in WebP.

## Chiusura e piede

- Chiusura "b con foto", testo a sinistra e foto a destra fino al bordo: "Da sempre luogo dove si danno appuntamento artisti e appassionati d'arte" (descrizione della categoria Workshop del loro calendario) in Gambetta 60 px; i cavalletti al 50 % della larghezza, alti 691 px. Recapiti: 049 7811043 grande in verde (tel:), cellulare 380 2308602 (tel:), negozio@artificiobattagin.it (mailto:), Via della Croce Rossa 5/a con il link alla mappa, "Ampio parcheggio privato". Niente orari: non sono confermati.
- Piede sul bianco del passepartout: logo PNG a 125 px (2x) con una riga su chi sono; a destra la newsletter (sì: hanno clienti privati, 22 corsi nel 2026, promozioni e un articolo quasi ogni mese, e una newsletter ce l'hanno già) con campo, bottone verde e consenso; sotto quattro colonne con titoletti Switzer 500 a 13 px e voci a 15 px: Negozio, Artinpratica, Contatti, Seguici (solo Instagram e Facebook, in parole); in fondo A.B. s.r.l., P.IVA 04191710286, REA PD 369492, Condizioni di vendita, Resi e rimborsi, Spedizioni e pagamenti, Privacy, Cookie. A 390 le colonne vanno a due a due. Il modulo non invia nulla: lo dice anche il messaggio di conferma finché non è collegato.

## Controlli

- Guardati a pezzi: 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 1024, 1920, più i profili oro e blu a 1440, argento a 1024 e nero a 390. Nessuno scorrimento orizzontale (320, 390, 768, 1024, 1440, 1920), nessuna sovrapposizione.
- `_metodo/kit/segnali.sh` a 1440: 0 soglie da correggere su 10, 0 da guardare su 8. Foto al 35,7 % della pagina (la cornice d'apertura, fatta di listelli fotografati, non è contata perché è un `border-image`); Switzer 84 % e Gambetta 16 %; 3 misure di H2; 2 fasce (il muro e il piede); 15 filetti larghi; nessuna freccia, nessuna etichetta maiuscola.
- Nessun carattere U+2014 nella pagina, nella NOTA, nel LEGGIMI e nei CREDITI; nessuna lineetta negli orari ("dalle 9.30 alle 12.30").
- Dati: tutti da `01-analisi.md` e dal crawl (`il-negozio/`, `cornici/`, `belle-arti/`, `contatti/`, `events.json`, piede del sito). Lo sconto del 15 %, gli orari, il capitale sociale e la PEC restano fuori dalla pagina e sono nel LEGGIMI.
- A 1920 la tavola della prima schermata si ferma a 1.600 px e resta centrata; le foto a tutta larghezza (angolari) a quella misura sono ingrandite quasi 2 volte: servono gli originali del fotografo.
