# F.M. Sistemi, nuova home: nota della versione finale

Pagina: `sito/index.html` (si apre con file:///, nessuna chiamata esterna tranne i link a Google Maps, Facebook e alla pagina di partner Viessmann). Immagini in `sito/img`, caratteri in `sito/fonts`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, caratteri, prova dell'interazione, screenshot, controllo U+2014). Screenshot qui: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg` (JPEG 85); controlli a 320, 768, 1024, 1280 e 1920, clic su E a 1440 e tocco su P a 390 in `_prova/home/finale-controlli/`, esito della prova in `_prova/home/finale-controlli/prova.json`.

Base: prototipo A "Materia". Ultimo passaggio dopo il giudizio cieco (55/80, prove in `_prova/cieco/`): stessa idea e stessa direzione, apertura ferma, sezione dei mestieri rifatta.

## L'idea

"Dalla A alla Z" è l'unica frase che FM Sistemi ha scritto sul suo sito. La home la prende alla lettera: un alfabeto dei mestieri, con accese solo le otto lettere che corrispondono a un lavoro vero (A acqua, C clima, E elettrico, F fotovoltaico, M mobilità elettrica, P pompe di calore, R ristrutturazioni, T termoidraulica).
Il segno è un raccordo a T in rame, ruotato finché diventa una T maiuscola: la barra attraversa lo schermo da bordo a bordo e regge il titolo; il gambo scende, sfuma sul grafite e diventa la T accesa dell'alfabeto, con il segno di rame sullo stesso asse (1157 px a 1440, misurato da `_prova/script/finale_misura.mjs`).
Il rame è l'unico colore della pagina: la T resta a colori, tutte le altre foto sono in bianco e nero neutro; solo la parete d'inverno, il risultato a cantiere chiuso, resta calda.

## Cosa è cambiato in questo passaggio

- **Apertura ferma.** Le lettere non cambiano più la foto: la prima schermata resta sul raccordo a T. Ogni lettera accesa è un collegamento alla riga del suo mestiere (`#lavoro-a` ... `#lavoro-t`), dove la stessa lettera fa da capolettera e riceve il segno di rame (`:target`). Niente script in pagina, niente `data-tav`. Così il gesto non è più il nastro dei campioni di Paraga Pelli: l'alfabeto è l'indice della pagina.
- **La riga sotto il titolo dice il fatto solo loro:** "Otto mestieri su ventuno lettere: impianti elettrici e termoidraulici, clima, pompe di calore Viessmann, fotovoltaico e ristrutturazioni. Una squadra di 17 persone a Vigonovo, un numero solo." La conta delle lettere accese diventa l'informazione. La riga è un paragrafo fuori dall'h1 (l'h1 è solo "Dalla A alla Z") e cresce verso l'alto dal bottone, che resta sulla linea di base del titolo.
- **Bottone:** "Telefonate allo 049 8305354", accanto "o scrivete" (mailto a commerciale@, oggetto "Richiesta di sopralluogo").
- **"Una casa dalla A alla Z"** al posto del campionario a otto strisce uguali: i mestieri nell'ordine di un cantiere (01 R, 02 T, 03 E, 04 A, 05 P, 06 C, 07 F, 08 M), ogni riga con indice, capolettera in Funnel Display 152 px rame chiaro, nome, una riga e "Nella foto: ...", e una striscia di materiale 3,5:1 che esce dal bordo destro dello schermo. Le strisce impilate fanno un campionario verticale separato da filetti. Un solo testo per mestiere, uguale nella didascalia dell'apertura (T) e nella riga.
- **Foto:** E rifatta con i morsetti bassi e i cavi pettinati in parallelo (le etichette dei marchi restano fuori, il bianco e nero toglie i colori); F tagliata dove si legge la griglia delle celle; A centrata sulle gocce; T della riga con il collare del raccordo, rame fino ai bordi. Collettore in bianco e nero. Le tavole delle altre lettere e i campioni sono tolti.
- **Chi siamo:** sotto il 17 "persone nella squadra, nel 2025"; la riga Squadra della scheda è sostituita da "Mestieri: 8, con un solo numero da chiamare"; tolti l'appalto e "famiglie": "Lavoriamo per privati, aziende ed enti pubblici. Con Viessmann installiamo anche gli impianti commerciali: la nostra pagina di partner" (link alla pagina Viessmann).
- **Contatti:** commerciale@ con "per preventivi e sopralluoghi" (mailto con oggetto).
- **Piede:** tolti i link Privacy e Cookie vuoti finché le pagine non esistono; tolti i due `preload` dei caratteri (davano errori CORS in file://); il logo in testata punta a `index.html`, non più a `#`.
- **Da 601 a 1100 px e telefono:** la tavola è più bassa e riga e bottone vengono subito dopo la foto, prima dell'alfabeto. Bordo basso del bottone: 600 a 1024x768, 541 a 768x1024, 731 a 390x844.

## Le prime schermate

**1440x900.** Testata: logo in chiaro, Lavori, Chi siamo, Contatti, telefono. "Dalla A alla Z" in Funnel Display 160 px, linea di base a y 332, 40 px sopra la barra di rame. A destra, colonna di 421 px: la riga (17 px, quattro righe, y 174-266) e il bottone, con il bordo basso sulla linea di base (y 332). Sotto la barra, a sinistra, la voce "T Termoidraulica" con la sua riga. In fondo l'alfabeto a tutta larghezza, lettere 46 px, nomi 13 px.

**390x844.** Titolo su due righe a 82 px, la T di rame a tutta larghezza con il gambo al centro, poi la riga (cinque righe) e il bottone, poi l'alfabeto 7x3 con celle da 50x48 px; la T accesa è al centro della terza riga, sullo stesso asse del gambo.

Sotto: "Una casa dalla A alla Z", collettore a tutta larghezza (la foto tecnica), il 17 a 216 px con la scheda a tre righe; la parete d'inverno con la frase "Il lavoro migliore è quello che a cantiere chiuso non si vede più. In casa resta la temperatura giusta."; contatti con il numero grande; piede con i dati societari. Un passo solo fra le sezioni: 160 px a 1440, 96 px a 390.

## Caratteri e colori

- **Funnel Display** (titolo, lettere, capolettera, numeri grandi, frase della parete) e **Funnel Sans** (testo, menu, bottone): stessa superfamiglia, di The Funnel Project Authors (Dicotype), da Google Fonts, licenza SIL Open Font License 1.1 (testo in `sito/fonts/OFL.txt`). Serviti dalla pagina: `sito/fonts/funnel-display-latin.woff2` e `funnel-sans-latin.woff2`, variabili 300-800, usati a 400 e 500. Riferimenti: Aira (titolo enorme in un grottesco proprio, bianco su nero sopra una griglia in luce color rame) e Basalte (grottesco largo e leggero, forti salti di misura). Cifre tabellari su telefono, orari, partita IVA, date, indici. Nessun monospazio.
- **Scala:** 216 il 17, 160 apertura, 152 capolettera, 92 telefono, 56 h2 e frase della parete, 46 lettere dell'alfabeto, 30 voce della tavola, 28 nomi dei mestieri, 17-20 testo, 13-14 didascalie, indici e nomi.
- **Colori:** grafite #141414 (fondo e nero delle foto), testo #EDE7DF (15:1), secondario #A79F95 (7:1), lettere spente #5A544D (spente apposta, nascoste ai lettori di schermo), filetti #2A2A2A, rame #B87333 solo per il bottone e i segni sotto le lettere, rame chiaro #D6955A (7,3:1) per lettere accese, capolettera, inizio della riga e passaggio. Il blu FM resta solo nell'arco del logo.

## Interazione

L'alfabeto è un `nav` con otto collegamenti. Clic, tocco, Tab e Invio portano alla riga del mestiere; la capolettera di quella riga riceve il segno di rame. Unica transizione: colore della lettera e del bottone in 0,12 s. Nessuna animazione allo scorrere, nessun effetto che segue il cursore, nessuno scorrimento morbido.

## Foto

Nessuna è di FM Sistemi (il sito ha solo una foto di repertorio, scartata). Tutte Pexels, licenza "Free" letta sulla pagina il 19/10/2026, elenco in `assets/CREDITI.md`; trattate con PIL (`_prova/script/finale_img.py`) ed esportate in 2-3 larghezze con srcset.
- T, apertura e riga 02: raccordo a T in rame, Magda Ehlers (3721272), unica a colori
- R: cazzuola con malta, David Antonio Cruz Naira (38561969)
- E: quadro con interruttori, ranjeet . (28950842): solo morsetti bassi e cavi
- A: gocce d'acqua, Yogesh Jangid (7169730)
- P: griglia del ventilatore di un'unità esterna, Natalie Dmay (16848596): solo l'interno della griglia, marchio fuori dal taglio
- C: griglia di aerazione, Filipp Romanovski (16527887)
- F: moduli fotovoltaici, Tobi & Chris (11455626)
- M: presa di ricarica, Vitali Adutskevich (17000830), specchiata
- collettore del riscaldamento a pavimento, Pavel Danilyuk (7937309)
- parete d'inverno, luce di tapparella, Nathanael Arias (13742375), calda

Le didascalie descrivono l'oggetto ("Nella foto: ...") e non dicono mai che è un lavoro loro.

## Controlli (19 ottobre 2026, dopo l'ultimo `build_finale.sh`)

- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 430, 600, 601, 768, 900, 1024, 1100, 1101, 1280, 1366, 1440, 1536, 1920 e 2560 (`_prova/script/finale_prova.mjs`).
- Interazione: a 1440 clic su A, E e P: la pagina va alla riga (bordo alto a 32 px), `:target` giusto, segno di rame acceso; foto, didascalia e alfabeto dell'apertura identici prima e dopo; `data-tav` non esiste. Tastiera: Tab arriva alla A, Invio porta a `#lavoro-a`, il Tab seguente prosegue da lì. Telefono 390: tocco su P porta a `#lavoro-p`.
- Collegamenti: `tel:+390498305354` (testata, bottone, numero grande), `mailto:info@` e `mailto:commerciale@` con oggetto, Google Maps con l'indirizzo, Facebook, pagina partner Viessmann. Nessun `href="#"`, nessuna ancora rotta, console senza errori a 1440 e a 390.
- Screenshot a 320, 390, 768, 1024, 1440 e 1920 guardati a pezzi: nessuna sovrapposizione dopo le correzioni (a 768 il nome "Ristrutturazioni" toccava la sua riga, a 390 la M toccava il nome: corretti).
- `segnali.sh`: 0 soglie bloccanti. Foto 59,1 % della pagina, una superfamiglia (Funnel Sans 85,5 %, Display 14,5 %), mono 0 %, 0 frecce, un numero grande (17), data 2025. Da guardare: una sola misura di H2 (56 px; la gerarchia la fanno 160, 152 e 216 px) e la numerazione 01-08, che qui è l'ordine vero di un cantiere.
- Nessun carattere U+2014 in pagina, script, nota e LEGGIMI (controllo nel build). Orari con il trattino semplice "8.30-19.00".
- Nessuna chiamata a Google Fonts; nessun dato senza fonte in 01-analisi.md (le deduzioni sono nel LEGGIMI).
