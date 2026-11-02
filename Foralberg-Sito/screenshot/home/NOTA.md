# Foralberg, home finale: "Firmato Foralberg"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot). Altezza a 1440: 5396 px piede compreso.

## L'idea

La firma corsiva del logo di oggi è già dipinta sul cassone dell'OM Lupetto 30 delle prime consegne. La home apre su quella foto d'archivio, a tutta larghezza e subito sotto il logo in testata: firma di allora sotto logo di oggi, si legge in due secondi senza didascalia. Con il nome di un concorrente la pagina non regge: il furgone, la portiera con le voci del catalogo, lo stand della 38a Fiera e la frase di chiusura sono solo loro.

## Cosa è cambiato in questa rifinitura (2 novembre)

Dal giudizio cieco (K0 7, K6 6, 57 su 80) e dalla richiesta del committente "più alta gamma, meno uguali tra loro".
- **Fondo dal mestiere**: via la carta beige #F3F1EC. La pagina è bianco porcellana #F5F6F5, il bianco della porcellana da tavola che è il primo capitolo del catalogo ("il bianco valorizza il cibo", catalogo p. 47). La ragione si vede: le luci di tutte le foto finiscono esattamente su quel bianco (il furgone, lo stand, il piatto, le posate, il calice con la sua ombra), così gli oggetti stanno sulla pagina come sulla tovaglia.
- **Impaginazione che non c'è nelle altre home** (controllate le copertine di Est-Grisignano e Mestrino e le prime schermate della campagna): la foto parte dal filo della testata, a tutta larghezza, prima del titolo; il titolo viene dopo, sotto la foto. Nelle altre home il titolo sta sopra o accanto all'oggetto. In più la pagina si chiude a specchio con un'altra foto d'archivio a tutta larghezza (chiusura con testo sopra e foto sotto), e tra le due c'è un solo blocco diviso foto e testo (l'indice).
- **Apertura** (K6): titolo "Consulenti dell'ospitalità" (dalla home di oggi, "Dal 1953 Consulenti dell'Ospitalità") al posto della formula "X dal 1953"; foto subito sotto la testata, didascalia del furgone sopra la piega nella colonna destra, poi la riga su cosa vendono, il bottone "I capitoli del catalogo" e "Vieni in via Cile 2". Logo in testata a 52 px.
- **Ponte tra archivio e catalogo**: l'introduzione dell'indice cita la portiera del Lupetto ("porcellane, cristallerie, posaterie, art. vari cucina", letto sull'originale) e dice che oggi sono i capitoli del catalogo.
- **Foto dell'indice** (bloccante): sei soggetti diversi, uno per capitolo e nominato nella sua riga: piatto piano bianco dall'alto (Çelik), forchette d'argento (Irina P), calice da grappa con l'ombra (Kovaleva), coppe da cocktail e shaker (Çoban), chafing dish in acciaio (Starostin), gastronorm con le posate (Filirovska). A colori naturali smorzati, luci neutre sul bianco della pagina; il piatto, nato in bianco e nero, con la grana attenuata e il piano schiarito. L'archivio resta in bianco e nero: la voce del passato contro quella del presente.
- **Viraggio dell'archivio**: neri a #1A1A1A, nessuna apertura locale delle ombre (via l'aspetto HDR dell'arco).
- **Storia e chiusura** (bloccante): tolta la sezione storia con lo stand della 38a e tolta la foto della 42a (mangani e lavatrici). Resta una sola foto di stand, la 38a con porcellane, posate e tavoli apparecchiati, in chiusura a tutta larghezza sotto la frase e i recapiti. Tolta la frase ambigua sui "fratelli Desiderio".
- **Numeri**: una frase per chi lavorano (con la PA) e quattro cifre grandi in riga (800 m², 30.000, 6.000, 11), cifre proporzionali perché le tabellari di Schibsted allargavano il punto ("30 . 000").
- **Progetto**: i quattro tempi in righe a filetto (numero e titolo a 30 px, riga a destra), non più quattro colonne da modello.
- **Minori**: bottone rinominato; "(PDF, 56 MB)" accanto al link del capitolo; menu Cataloghi e Chi siamo verso le pagine del sito nuovo; altezza dell'indice costante a ogni capitolo e a ogni larghezza (lo script misura il testo più lungo e fissa l'altezza della scheda); a 1024 la foto dell'indice è alta quanto la colonna di testo (nessun vuoto sotto); link del piede alti almeno 29 px a schermo largo e 35 px fino a 860, colonna Contatti in grigio con il solo telefono in inchiostro; tolto il preload del font (nessun errore in console con file://); foto di apertura e chiusura più alte (37,5vw fino a 56vh, e 64vw fino a 940 px) e ritmo tra le sezioni a 132 px.

## Le prime schermate

- **1440**: testata con logo vettoriale, menu corto e 049 760955. Foto del furgone da y=88 a 592: firma, monogramma, via Trieste 11, i marchi rappresentati, la portiera e la calandra con "Lupetto 30". Sotto, a sinistra, "Consulenti dell'ospitalità" a 106 px su due righe; a destra la didascalia del furgone, la riga su cosa vendono, il bottone e il link, tutto sopra la piega (il bottone finisce a y=895).
- **390**: foto quadrata sul cassone (firma, monogramma, marchi, portiera), titolo a 46 px su due righe, didascalia, riga e bottone dentro la prima schermata.
- Poi: numeri, indice del catalogo (il gesto), progetto in quattro tempi, chiusura, piede.

## Caratteri e colori

- **Schibsted Grotesk** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una famiglia sola servita dalla pagina in woff2 variabile: 400 per titoli e testo, 500 per menu, bottoni e didascalie in grassetto. Grottesco da giornale accanto ai caratteri dipinti degli stand e del furgone, senza fare a gara con la firma corsiva. Cifre tabellari solo sui numeri di pagina dell'indice e sulla P.IVA.
- Bianco porcellana #F5F6F5, inchiostro #161616 (17,1:1), grigio #5A5A5A (6,5:1), filetti al 16 %, blu Foralberg scurito #00699A (5,8:1 sul fondo, bianco sul blu 6,0:1; il #0082B9 della copertina non regge AA col testo bianco) solo per bottoni, pagina del capitolo attivo e numeri dei passi.
- Riferimenti (sez. 7 dell'analisi): Serax e Robbe & Berking per la misura, tanto bianco, un'immagine per schermata, poche parole; Zwiesel per il vetro raccontato in luce; Schönwald per la porcellana bianca protagonista, qui portata nel colore della pagina.

## Interazione

Un solo gesto: l'indice del catalogo 2026/2027 con le pagine vere (Porcellana p. 10, Posateria 182, Vetro 232, Bar e mixology 290, Buffet e catering 378, Gastronorm 470). Clic, tocco, frecce, Home e Fine cambiano di colpo la foto, la riga del capitolo e il link "Apri il capitolo nel catalogo, p. N (PDF, 56 MB)", che apre il PDF del sito a #page=N. Bottoni veri con aria-pressed, area di 526x73 px a 1440 e 168x67 a 390; a 390 le voci stanno in due colonne sopra la foto. Nessuna dissolvenza, nessuna animazione allo scorrere; transizioni di 0,12 s solo sul colore di ciò che si tocca. Prova: `node _prova/script/finale_gesto.mjs <percorso>/sito/index.html`.

## Foto

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura, il furgone (largo, e quadrato per il telefono) | archivio Foralberg, `storia_camion2_foralberg.jpg` da foralberg.it/it/company | proprietà dell'azienda; diritti da chiedere |
| Chiusura, stand alla 38a Fiera di Padova | archivio Foralberg, `storia_fiera_1_foralberg.jpg`, "foto Giordani" | come sopra |
| Indice, Porcellana | Yusuf Çelik, Pexels 18677610 | Pexels License, verificata il 24/10/2026 |
| Indice, Posateria | Irina P, Pexels 12021478, ruotata | Pexels License |
| Indice, Vetro | Polina Kovaleva, Pexels 7283407 | Pexels License |
| Indice, Bar e mixology | Gülsüm Çoban, Pexels 33174185, tagliata senza la ciotola di frutta | Pexels License, verificata il 02/11/2026 |
| Indice, Buffet e catering | Sergei Starostin, Pexels 39388324 | Pexels License, verificata il 02/11/2026 |
| Indice, Gastronorm | Julia Filirovska, Pexels 7140435 | Pexels License |

Nessuna foto di repertorio è usata in un'altra home della campagna (controllo per ID su tutti i `*-Sito/assets/CREDITI.md` il 02/11/2026); nessuna immagine generata da IA; nessun marchio concorrente in primo piano. Nessuna legenda numerata sugli oggetti: solo didascalie sobrie sotto le foto d'archivio.

## Chiusura e piede

- Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto (922 px a 1440): "Ci piace pensare di essere più di un semplice fornitore" (dalla home di oggi); 049 760955 grande con tel:+39049760955; Servizio clienti 335 142 6521 (tel:+393351426521) e servizioclienti@foralberg.it; "Vendite e showroom" ldesiderio@foralberg.it; via Cile 2 con "Apri la mappa"; orari di uffici e showroom.
- Piede: logo orizzontale vettoriale (monogramma e firma) con una riga su chi sono; newsletter "Novità e cataloghi" (email, bottone, casella del consenso; non invia nulla finché non è collegata a un servizio); quattro colonne Prodotti, Servizi (con "Acquisti PA, MePA e portali regionali"), Azienda (con La Vetrinetta e il suo Facebook, l'unico social verificato), Contatti; riga legale con Foralberg s.r.l., via Cile 2, P.IVA 00210840286, Privacy, Cookie, Note legali. Niente colonna Seguici: Foralberg non collega profili. A 390 Prodotti a sinistra, Servizi e Azienda a destra, Contatti a tutta larghezza.

## Controlli (2 novembre)

- Screenshot guardati a pezzi: 1440 (5396 px), 390 (5728), 320 (6015), 768 (6113), 1024 (4915), 1920 (5515). Nessuna sovrapposizione, nessun vuoto non voluto.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 560, 768, 860, 1024, 1180, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/finale_controlli.mjs`); console senza errori con file://.
- Gesto: clic, tocco, freccia giù, Fine e Home danno sempre foto, voce attiva e pagina coerenti a 1440 e a 390; altezza di #catalogo identica sui sei capitoli a ogni larghezza.
- Collegamenti: tel:+39049760955, tel:+393351426521, mailto:servizioclienti@foralberg.it, mailto:ldesiderio@foralberg.it, mappa Google su "Foralberg via Cile 2 35127 Padova".
- U+2014 assente dalla pagina, dagli script, da questa nota e dal LEGGIMI.
- `segnali.sh` a 1440: 0 soglie bloccanti su 10 (foto 35,6 %, una famiglia, mono 0 %, 19 filetti, nessuna etichetta sopra i titoli, nessuna freccia). Da guardare: H2 di una sola misura (56 px, più i 21 px del piede), voluto: la gerarchia la fanno il titolo a 106 px e le foto; quattro numeri grandi con etichetta, chiesti dal giudice al posto del paragrafo di numeri.
- A occhio: niente badge, tre box con icona, card col bordo, corsivo d'accento, gradienti, dissolvenze, hover che sbiadiscono, icone Lucide, legende a pallino.
