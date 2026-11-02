# Distilleria Rizzi, nuova home: "L'etichetta in piano" (versione finale, rifinita)

Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (solo quelle usate, WebP e JPEG in più larghezze), caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini, caratteri, pagina, screenshot). Alta 4717 px a 1440 (piede compreso), 6206 px a 390.

## Idea

Su un fondo color carta c'è una sola bottiglia vera di Rizzi, ritta su un filo sottile che attraversa la pagina come il piano di un tavolo d'archivio. Il patrimonio di Rizzi sono le sei etichette di casa, non un alambicco che oggi non c'è più. Con il nome di un concorrente la pagina non regge, perché le etichette sono solo loro. La pagina si chiude sul manifesto storico «i classici prodotti Rizzi Padova»: Bitter, Pinalpe e Crema Marsala disegnati in un'altra epoca.

## Cosa è cambiato in questo giro (dal giudizio cieco)

- **Legende tolte del tutto**, con i pallini e i filetti (erano lo stesso gesto della home di Mario Agnoletto). Via anche la funzione `legende()` e i dati delle posizioni. Resta un solo gesto: i sei nomi che scambiano la bottiglia.
- **Prima schermata ricomposta in tre parti**: titolo e nomi nelle colonne 1-6, la bottiglia al centro delle colonne 7-9, a destra (colonne 10-12) la sua scheda con il grado grande in Zodiak 300 (92 px, cifre tabellari), il nome in Zodiak a 22 px e uso e formato in Switzer. Il grado vero diventa l'elemento grafico che cambia con la scelta. A 1440 accanto alla bottiglia non c'è nessun filetto né pallino.
- **Bottiglie rifatte** (`finale_img.py`): tolta l'ombra portata laterale, resta solo l'ombra di contatto ellittica sul filo (circa 12 px a schermo, opacità 0,25). Scontorno più stretto di circa 5 px sull'originale e sfumato. Mediana e sfocatura leggera sull'originale prima della riduzione, per togliere gli aloni della maschera di contrasto del telefono e la grana del liquido. Tolto il lembo chiaro del sigillo di carta sul lato destro del tappo della Felsina e del Punch, che a schermo sembrava un alone. La bottiglia è alta 700 px al massimo (prima 755).
- **Alchermes ridotto** da 730 a 450 px, senza didascalia, ritto sullo stesso filo che chiude la sezione pasticceria, a destra delle famiglie. Nessuna bottiglia della seconda schermata supera i 450 px.
- **Striscia delle spezie Pexels tolta**, con la sua didascalia sbagliata (nominava agrumi e mele che nel taglio non c'erano).
- **Sezione "mestiere" rimessa in griglia**: tre righe che partono tutte dal margine di 64 px. Pasticceria (titolo, famiglie, Vodka e link a sinistra, Alchermes a destra); "Facciamo tutto noi, dall'inizio alla fine" con il titolo nelle colonne 1-6 e il testo nelle 7-12, prima riga allineata; una riga nuova sul "per chi" con la frase grande "Lavoriamo soprattutto con pasticcerie, bar, ristoranti e distributori del Veneto" e lo spaccio aperto ai privati dal 29/09/2024 (fatti da `01-analisi.md`, sez. 1 e 3).
- **Chiusura con un prodotto Rizzi**: al posto della bottiglia generica di Pexels c'è il manifesto storico «i classici prodotti RIZZI PADOVA» (Bitter, Pinalpe, Crema Marsala all'uovo), dalla foto della mostra «Padova da gustare» 2025 nella libreria media dell'azienda. Raddrizzato in prospettiva con PIL sui quattro angoli interni della cornice misurati a zoom 3x, ritagliato dentro la cornice, HDR del telefono calmato. Sta a destra fino al bordo, nelle sue proporzioni (nessun taglio), con una didascalia che dice cos'è e di chi è la collezione.
- **Difetti di esecuzione**: "1926-2026" nel piede con il trattino non separabile (U+2011); tra 1001 e 1180 px il logo del piede va su una riga propria e le colonne sono larghe 3/12 (a 1024 nessuna voce va a capo); sotto i 1000 px la chiusura resta a due colonne ma il manifesto tiene le sue proporzioni e si appoggia al piede, quindi a 768 il titolo sta su 3 righe e l'indirizzo su una; la newsletter scrive un riscontro in un `role="status"` dopo l'invio; la voce "Liquori e amari" della testata va a `/liquori-e-amari/`; il bottone Menu diventa "Chiudi" quando è aperto e il menu si chiude anche con Esc (il fuoco torna sul bottone); tolti i due `link rel=preload` dei caratteri (con `font-display:swap` il guadagno era minimo e in file:// davano errori CORS).
- A 1024x768 l'apertura scende a 760 px e la bottiglia si riduce con l'altezza della finestra, così il filo resta nella prima schermata.

## Caratteri e colori

- **Zodiak** 300 e 400 (Indian Type Foundry, Fontshare) per titoli, nomi delle etichette, gradi, anni e telefono: serif dritto ad alto contrasto, mai corsivo, vicino alle lettere dello scudo RIZZI. Riferimenti: Fernet-Branca e Cocchi (la bottiglia storica accanto a un titolo grande e sicuro), Marzadro (bianco e serif).
- **Switzer** 400 e 500 (stessa fonderia) per testi e piede, dai pacchetti completi con la crenatura. Le cifre sono tabellari: gradi, orari, P.IVA e formati incolonnati.
- **Licenza**: ITF Free Font License 2.0, uso commerciale gratuito anche in self-hosting. Testo in `sito/fonts/LICENZA-ITF-FFL.txt`.
- Colori: carta #F3EEE6, inchiostro #1C1815 (15,3:1), grigio testi #5B524A (6,6:1 sulla carta, 6,2:1 sul piede #ECE6DC), rosso etichetta #B8231C solo per il nome scelto, il campo del centenario (carta su rosso 5,5:1) e il passaggio sui link.

## Interazione (un solo gesto)

I sei nomi formano un gruppo di scelta (role radio): tocco, clic, frecce, Home e Fine, fuoco visibile in rosso. Al cambio la bottiglia si scambia di netto, senza dissolvenza (immagini precaricate nella misura giusta), e cambiano grado, nome, uso e formato nella scheda (`aria-live`). Le sole transizioni, di 0,12 s, riguardano il colore dei nomi e del bottone della newsletter. Niente animazioni allo scorrere, niente effetti sul cursore.

## Foto, origine e licenza

- Bottiglie Felsina, Fernet, Garofano, Pinalpe, Prugna, Punch Arancio (`assets/originali/2024-02-*.png`) e Alchermes (`2023-02-bott-alchermes.png`): di Distilleria Rizzi, dalla libreria media del loro sito. WebP con alfa a 480, 760 e 1000 px.
- Manifesto storico: foto `2025-04-1000098150-01.jpeg` della libreria media dell'azienda (mostra «Padova da gustare», Palazzo Santo Stefano, 2025). L'originale è della collezione di Simone Marzari: i diritti di riproduzione vanno chiesti a lui (vedi LEGGIMI). JPEG a 400 e 588 px (588 è la misura nativa dopo il raddrizzamento, nessun ingrandimento).
- Le due foto Pexels del giro precedente (spezie di Kunuk, bottiglia di Reding) non sono più in pagina. Nessuna immagine è generata dall'IA; nessuna foto di repertorio.
- Logo: PNG ricolorati in inchiostro (scritta a pennello nella testata, calice e scritta nel piede), non ricostruiti in SVG perché il tratto a pennello non si rifà in modo fedele.
- Newsletter: c'è, perché ci sono il centenario, i cofanetti delle feste, le fiere e i clienti privati dello spaccio. Non invia nulla finché non è collegata a un servizio (LEGGIMI).

## Controlli fatti

- Screenshot a 1440 e 390 (consegna) e a 320, 768, 1024 e 1920 (controlli in `_prova/tmp-finale/controlli/`), guardati a pezzi da 1600 px. Nessuna sovrapposizione: a 768 la scheda non tocca più la bottiglia, a 1024 il manifesto non è tagliato.
- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 700, 701, 768, 900, 1000, 1001, 1024, 1180, 1181, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/collaudo_finale.mjs`).
- Gesto da tastiera a 1440: frecce su tutte e sei le bottiglie (grado, nome e file cambiano), Fine, Home e freccia a sinistra dal primo all'ultimo. Al tocco a 390 (dpr 2): Punch, Pinalpe, Garofano, Felsina; aree di tocco alte 44 px. Menu a 390: "Chiudi" con aria-expanded true, Esc lo chiude e riporta il fuoco.
- Newsletter: dopo l'invio con email e consenso compare "Grazie: ti scriveremo per confermare l'iscrizione."
- Collegamenti: tel:+390499000053 (testata, menu, chiusura), mailto:info@distilleriarizzi.com, mappa Google con l'indirizzo di via G. Negri 7; ancore interne tutte presenti. Nessuna immagine rotta.
- Console: nessun errore servendo la cartella con `python3 -m http.server`, e nessun errore neanche in file:// (preload tolti).
- Carattere U+2014: nessuno in pagina, negli script, in questa nota e nel LEGGIMI.
- Segnali da IA (`segnali.sh`): 17 soglie su 18 passano; il titolo a sinistra con paragrafo a destra ora compare una volta sola. Resta fuori l'area coperta da foto: 13,8 % contro il 35 %. È voluto: il giudice ha chiesto di togliere la striscia di repertorio e di ridurre l'Alchermes perché nulla facesse concorrenza al solo oggetto, e lo strumento conta solo in parte le bottiglie scontornate su carta. Non ho aggiunto foto di riempimento.
