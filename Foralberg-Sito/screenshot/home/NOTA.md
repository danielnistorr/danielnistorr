# Foralberg, home finale: "Firmato Foralberg"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot). Altezza a 1440: 5842 px piede compreso.

## L'idea

La firma corsiva del logo di oggi è già dipinta sul cassone dell'OM Lupetto 30 delle prime consegne. La home apre su quella foto d'archivio, grande e a tutta larghezza, sotto il logo in testata: due secondi e si vede che la firma è la stessa dalle prime consegne a oggi. Con il nome di un concorrente la pagina non regge, perché il furgone, gli stand in fiera e la frase di chiusura sono solo loro.
Rispetto al prototipo B la pagina è portata alla luce e all'ordine del prototipo A: viraggio chiaro su tutte le foto, un solo gesto (l'indice del catalogo), niente riga del tempo cliccabile, sezioni corte.

## Le prime due schermate

- **1440**: testata con logo vettoriale, menu corto e 049 760955. Titolo loro "Forniture alberghiere dal 1953" a 106 px su due righe; accanto a "dal 1953" solo la riga su cosa vendono, il bottone blu "Sfoglia il catalogo 2026/2027" e "Vieni in via Cile 2". Il furgone comincia a y=372 e sopra la piega mostra intera la firma, il monogramma, via Trieste 11 e la cabina con "Lupetto 30"; il taglio cade sulla cabina, sotto la targhetta. Subito sotto, a sinistra, la didascalia: "Le prime consegne firmate Foralberg. Un OM Lupetto 30 sotto i portici di Padova, con l'indirizzo di via Trieste 11 sul cassone: la firma è la stessa del logo di oggi." Seconda schermata: "Consulenti dell'ospitalità" in una riga e sotto, nella stessa colonna, i numeri veri (800 m², 30.000 articoli, 6.000 in pronta consegna, oltre 30 collaboratori, 11 agenti, Venezia).
- **390**: titolo a 50 px su tre righe, riga, bottone e link, poi un taglio quadrato fatto apposta sul cassone (firma, monogramma, via Trieste 11, i marchi rappresentati) che chiude la prima schermata a 834 px.
- Il resto: l'indice del catalogo (il gesto), il progetto in quattro tempi con la riga sulla PA, la storia con lo stand della 38a Fiera, la chiusura con lo stand della 42a Fiera, il piede.

## Caratteri e colori

- **Schibsted Grotesk** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una famiglia sola servita dalla pagina in woff2 variabile: 400 per titoli e testo, 500 per menu, bottoni, h3 e didascalie in grassetto. Grottesco da giornale, accanto ai caratteri dipinti degli stand e del furgone senza fare a gara con la firma corsiva del logo. Cifre tabellari solo sui numeri di pagina dell'indice (in questo carattere le tabellari allargano anche il punto e lo spazio, quindi orari e telefoni restano proporzionali). Nota: la guida mette Schibsted tra i "tic di casa" in coppia con Source Serif 4 (Albergo Vescovi); qui è da sola e l'ha scelta il giudice.
- Carta #F3F1EC, inchiostro #161616 (16,1:1), grigio #5A5A5A (6,1:1), filetti al 16 %, blu Foralberg scurito #00699A (5,5:1 sulla carta, bianco sul blu 6,0:1; il #0082B9 della copertina non regge AA col testo bianco) solo per bottoni, pagina del capitolo attivo e numeri dei passi.
- Riferimenti (sez. 7 dell'analisi): Serax e Robbe & Berking per la misura, tanta carta, un'immagine per schermata, poche parole; Schönwald per l'oggetto del mestiere protagonista, qui sostituito dall'archivio che nessun concorrente ha.

## Interazione

Un solo gesto: l'indice del catalogo 2026/2027 con le pagine vere (Porcellana p. 10, Posateria 182, Vetro 232, Bar e mixology 290, Buffet e catering 378, Gastronorm 470). Clic, tocco, frecce, Home e Fine cambiano di colpo la foto, la riga del capitolo e il link "Apri il capitolo nel catalogo, p. N", che apre il PDF del sito a #page=N. Bottoni veri con aria-pressed, area di 526x73 px a 1440 e 168x67 a 390; a 390 le voci stanno in due colonne sopra la foto. Nessuna dissolvenza, nessuna animazione allo scorrere; transizioni di 0,12 s solo sul colore di ciò che si tocca. Prova: `node _prova/script/finale_gesto.mjs <percorso>/sito/index.html` (clic, freccia, Fine e Home danno sempre foto, voce e pagina coerenti).

## Foto

Trattamento unico (`_prova/script/finale_img.py`): bianco e nero neutro, luci esattamente sulla carta #F3F1EC, neri a #2A2A2A, ombre grandi aperte in modo locale (l'arco dietro il furgone e il sotto del telaio non sono più masse nere), esportazione in 2-5 larghezze con srcset.

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura, il furgone (largo e quadrato per il telefono) | archivio Foralberg, `storia_camion2_foralberg.jpg` da foralberg.it/it/company | proprietà dell'azienda; diritti da chiedere (didascalie Giordani sulle altre foto della serie) |
| Storia, stand alla 38a Fiera di Padova | archivio Foralberg, `storia_fiera_1_foralberg.jpg`, "foto Giordani" | come sopra |
| Chiusura, stand alla 42a Fiera di Padova | archivio Foralberg, `storia_fiera_2_foralberg.jpg`, "foto Giordani" | come sopra |
| Indice, Porcellana | Mikhail Nilov, Pexels 6957563 | Pexels License, verificata il 24/10/2026 |
| Indice, Posateria | Irina P, Pexels 12021478, ruotata | Pexels License |
| Indice, Vetro | Nguyễn Thanh Ngọc, Pexels 3992482 (scatto da telefono: usato al massimo a 1440 px di lato corto) | Pexels License |
| Indice, Bar e mixology | Julia Sakelli, Pexels 5676260 | Pexels License |
| Indice, Buffet e catering | Magda Ehlers, Pexels 12255469, ritagliata sul buffet senza il lampadario | Pexels License |
| Indice, Gastronorm | Julia Filirovska, Pexels 7140435 | Pexels License |

Nessuna foto di repertorio è usata in un'altra home della campagna (controllo per ID su tutti i `*-Sito/assets/CREDITI.md`); nessuna immagine generata da IA. La foto della chiusura (archivio) è diversa da quella subito sopra e non compare in altre home. Tolte rispetto ai prototipi: la sala colazioni col lampadario in chiusura, il piatto Pexels e la cucina di repertorio di A.

## Chiusura e piede

- Chiusura "b con foto", testo a sinistra e foto fino al bordo destro a tutta altezza (860 px): "Ci piace pensare di essere più di un semplice fornitore" (dalla home di oggi), 049 760955 grande con tel:+39049760955, Servizio clienti 335 142 6521 e servizioclienti@foralberg.it, "Vendite e showroom" ldesiderio@foralberg.it, via Cile 2 con il link alla mappa, orari di uffici e showroom.
- Piede: logo orizzontale vettoriale (monogramma e firma) alto 44 px con una riga su chi sono; newsletter "Novità e cataloghi" con email, bottone e casella del consenso (non invia nulla finché non è collegata a un servizio: la pagina lo dice dopo l'invio); quattro colonne Prodotti (le sei voci dell'indice più Cucina e pasticceria e Cataloghi), Servizi, Azienda (con La Vetrinetta e il suo Facebook, l'unico social verificato), Contatti; riga legale con Foralberg s.r.l., via Cile 2, P.IVA 00210840286, Privacy, Cookie, Note legali. Niente colonna Seguici: Foralberg non collega profili. A 390 Prodotti a sinistra, Servizi e Azienda a destra, Contatti a tutta larghezza.

## Controlli

- Screenshot guardati a pezzi: 1440 (5842 px), 390 (6417), 320 (6633), 768 (6697), 1024 (5421), 1920 (6113). Nessuno scorrimento orizzontale (a 320 la testata si stringe: logo a 26 px, margini a 16), nessuna sovrapposizione.
- Tutti i tel: del numero principale sono "tel:+39049760955" (testata, chiusura, piede, a 1440 e a 390); il servizio clienti è "tel:+393351426521".
- U+2014 assente dalla pagina, dagli script e dai .md.
- `segnali.sh` a 1440: 0 soglie bloccanti su 10. Foto 35,4 %, una famiglia (Schibsted 100 %), mono 0 %, 14 filetti, 3 fasce di fondo, nessuna freccia, nessuna etichetta sopra i titoli. Da guardare: H2 di una sola misura (56 px, più i 21 px del piede): voluto, la gerarchia la fanno il titolo d'apertura a 106 px e le foto, come Rieder e Hermle tra i riferimenti misurati.
- A occhio: niente badge, tre box con icona, card col bordo, corsivo d'accento, gradienti, dissolvenze, hover che sbiadiscono, icone Lucide; le didascalie dicono luogo e anno, non la fonte della foto ("foto Giordani" è il nome del fotografo, scritto sulla stampa).
