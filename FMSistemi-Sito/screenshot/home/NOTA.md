# F.M. Sistemi, nuova home: nota della versione finale

Pagina: `sito/index.html` (si apre con file:///, nessuna chiamata esterna tranne i link a Google Maps, Facebook e alla pagina di partner Viessmann). Immagini in `sito/img`, caratteri in `sito/fonts`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, caratteri, prova dell'interazione, screenshot, controllo U+2014). Screenshot qui: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg` e `chiusura-1440.jpg` (solo la chiusura, dai contatti alla fine; JPEG 85); controlli a 320, 768, 1024, 1280 e 1920, clic su E a 1440 e tocco su P a 390 in `_prova/home/finale-controlli/`, esito della prova in `_prova/home/finale-controlli/prova.json`.

Base: prototipo A "Materia". Passaggio dopo il giudizio cieco (55/80, prove in `_prova/cieco/`): stessa idea e stessa direzione, apertura ferma, sezione dei mestieri rifatta. Ultimo passaggio (19 ottobre 2026): **palette chiara**, dopo il commento del committente "fm sistemi non mi fa impazzire così scura la palette". Idea, struttura, caratteri, interazione, testi e dati sono gli stessi; la versione scura resta in `_prova/home/finale-scuro/` (pagina e prime schermate) e in `_prova/script/finale_img_scuro.py`. Dopo (19 ottobre 2026) è cambiata solo **la chiusura** (contatti e piede), vedi sotto; la pagina com'era prima è in `_prova/home/prima-della-chiusura/`.

## La chiusura: dopo la Z, un numero solo

Il committente ha notato che quasi tutte le home della campagna chiudono allo stesso modo: titolo di luogo, numero di telefono gigante, una riga di tre o quattro colonnine (indirizzo, email, orari), piede a più colonne di testo minuto. Anche questa lo faceva ("In via del Lavoro 37...", numero a 92 px, tre colonne Orari, Scrivere, Venire, piede su pietra con logo, dati e Facebook in tre blocchi).

Ora la chiusura è **l'ultima voce dell'indice**: la stessa riga delle otto righe dei mestieri (filetti sopra e sotto, capolettera a 152 px nelle colonne 2-3, nome e riga di testo nelle colonne 4-6), con due differenze che la fanno leggere come la fine dell'alfabeto. La capolettera è la **Z**, spenta come nell'alfabeto dell'apertura (#857C70, 3,3:1, solo in grande, nascosta ai lettori di schermo), perché la Z non è un mestiere; e dove ogni mestiere ha la sua striscia di materiale, qui c'è il **numero**, con sotto il segno di rame della riga raggiunta. Il nome della voce è il titolo della sezione: "Dopo la Z, un numero solo", che riprende la riga dell'apertura ("...un numero solo") e la frase dei lavori ("il cantiere ha un numero solo"). Un oggetto solo, già noto a chi ha letto la pagina, niente concetto nuovo.

- **Voce:** "Dopo la Z, un numero solo" (h2, 28 px come i nomi dei mestieri) e sotto, come la riga di testo di un mestiere, gli orari: "Dal lunedì al sabato, 8.30-19.00. Domenica chiuso."
- **Al posto della striscia:** 049 8305354 in Funnel Display 64 px a 1440 (40 px al telefono), collegamento `tel:` alto 74 px a 1440 e 50 px a 390, grafite, rame al passaggio; sotto, in testo corrente e non in colonne: "Via del Lavoro 37, zona artigianale, 30030 Vigonovo (VE): apri in Google Maps" e "info@fmsistemisrl.it; per preventivi e sopralluoghi commerciale@fmsistemisrl.it" (due `mailto:`, il secondo con l'oggetto "Richiesta di preventivo").
- **Piede:** una riga sola sulla calce, senza fascia: F.M. Sistemi S.r.l., Partita IVA e codice fiscale 03807720283, PEC fmsistemisrl@legalmail.it, Facebook a destra; 14 px, secondario #5C554C (6,0:1). Al telefono le quattro voci vanno a capo una per riga. Nessun link alla privacy: la pagina non esiste ancora e un link vuoto era già stato tolto (va aggiunto quando c'è).
- **Tolti:** il titolo di luogo "In via del Lavoro 37, nella zona artigianale di Vigonovo", il numero a 92 px, le tre colonne Orari, Scrivere, Venire con i loro sottotitoli, il fondo pietra del piede (#E3DBCE, ora la pagina è tutta calce), il logo ripetuto nel piede, l'indirizzo e il telefono ripetuti nel piede.
- **Dati:** tutti quelli che c'erano, nessuno nuovo. L'indirizzo del piede non si ripete perché è nella voce sopra.
- **Da 601 a 1100 e al telefono** la voce segue la riga dei mestieri: Z a sinistra (112 px, 80 px al telefono), voce e orari accanto, numero e recapiti sotto (allineati al testo da 601 a 1100, a tutta larghezza al telefono). "Dopo la Z," e "un numero solo" non si spezzano dentro (a 360 px e meno sì, per stare nella colonna).
- **Controlli della chiusura** (con `_prova/script/build_finale.sh` e una cattura della sola chiusura a 1440, 1024, 768, 390, 360 e 320, guardata a pezzi): nessuno scorrimento orizzontale, nessun elemento fuori dallo schermo, nessuna sovrapposizione; contrasto dei testi come nel resto della pagina (13,2:1, 6,0:1, la Z 3,3:1 in grande); nessuna fascia scura, nessuna colonnina, nessun U+2014.

## L'idea

"Dalla A alla Z" è l'unica frase che FM Sistemi ha scritto sul suo sito. La home la prende alla lettera: un alfabeto dei mestieri, con accese solo le otto lettere che corrispondono a un lavoro vero (A acqua, C clima, E elettrico, F fotovoltaico, M mobilità elettrica, P pompe di calore, R ristrutturazioni, T termoidraulica).
Il segno è un raccordo a T in rame, ruotato finché diventa una T maiuscola: la barra attraversa lo schermo da bordo a bordo e regge il titolo; il gambo scende, sfuma nella calce e diventa la T accesa dell'alfabeto, con il segno di rame sullo stesso asse (1157 px a 1440, misurato da `_prova/script/finale_misura.mjs`).
Il rame è l'unico accento forte della pagina: la T resta a colori, tutte le altre foto sono in una monocromia calda e chiara (grafite caldo, pietra, calce); solo la parete d'inverno, il risultato a cantiere chiuso, resta calda.

## Cosa è cambiato nell'ultimo passaggio: la palette chiara

- **Fondo.** Da grafite #141414 a calce #EDE7DE in tutta la pagina (il piede era su pietra #E3DBCE: con la chiusura nuova è anche lui sulla calce). Nessuna fascia scura.
- **Testo.** Grafite #23201C (13,2:1 sulla calce), secondario #5C554C (6,0:1). Le lettere senza mestiere sono #857C70 (3,3:1), usate solo a 28-46 px, quindi testo grande; restano nascoste ai lettori di schermo.
- **Rame.** Rame #B4703A per il bottone (testo #1A1714, 4,5:1), il segno sotto la T accesa, il segno della riga raggiunta; rame per il testo #8F4F1F (5,2:1) per "Otto mestieri su ventuno lettere", la T della didascalia, la lettera accesa, le capolettera. Al passaggio il bottone diventa grafite con il testo calce (cambio netto, nessuna dissolvenza).
- **Blu FM** #046EA2 solo nell'arco del logo e nel segno del fuoco da tastiera (4,6:1).
- **Logo.** `sito/img/logo.png`: il raster del sito attuale con il nero portato a grafite, l'arco nel blu FM originale e il fondo trasparente (prima era schiarito per il fondo scuro).
- **Apertura.** Lo stesso raccordo a T (Magda Ehlers, Pexels 3721272), fotografato su nero, non reggeva una semplice ri-gradazione: schiarito, il nero restava un buco. È stato scontornato con una sagoma misurata sulla foto (bordo alto della barra letto colonna per colonna, bordi bassi e gambo disegnati, `_prova/script/chiaro_misura.py`), con i medi del rame alzati e le ombre del metallo portate a rame scuro, e posato sulla calce con due ombre morbide dalla stessa luce. Su Unsplash e Pexels non c'è una T in rame su fondo chiaro che si possa girare così (cercate: copper pipe, copper fitting, copper plumbing, copper pipes white; viste e scartate una curva in rame su muro beige, tubi in rame dentro un muro aperto, raccordi in fila su nero, un rendering 3D). La geometria non cambia: gambo al 79,207 % della foto, asse della barra al 33,537 %, stesso allineamento con la T dell'alfabeto.
- **Altre foto.** Stessa luce per tutte: monocromia calda chiara (nero portato a grafite caldo #3A3530, bianco alla calce, medi alzati), niente neri pieni. Le gocce su nero della riga A sono sostituite da gocce fitte su una superficie chiara (Mian Rizwan, Pexels 15192101): su nero restavano un rettangolo scuro anche schiarite. La riga E è spostata di 100 px per lasciar fuori un angolo nero. La parete d'inverno è schiarita: le ombre diventano pietra calda, le righe di luce restano color miele.
- **Didascalie e alt** aggiornati dove la foto è cambiata: "Raccordo a T in rame su fondo chiaro", "Nella foto: gocce d'acqua su una superficie chiara".

## Passaggio precedente (versione scura)

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

**1440x900.** Testata: logo in grafite con l'arco blu, Lavori, Chi siamo, Contatti, telefono. "Dalla A alla Z" in Funnel Display 160 px, linea di base a y 332, 40 px sopra la barra di rame. A destra, colonna di 421 px: la riga (17 px, quattro righe, y 174-266) e il bottone, con il bordo basso sulla linea di base (y 332). Sotto la barra, a sinistra, la voce "T Termoidraulica" con la sua riga. In fondo l'alfabeto a tutta larghezza, lettere 46 px, nomi 13 px.

**390x844.** Titolo su due righe a 82 px, la T di rame a tutta larghezza con il gambo al centro, poi la riga (cinque righe) e il bottone, poi l'alfabeto 7x3 con celle da 50x48 px; la T accesa è al centro della terza riga, sullo stesso asse del gambo.

Sotto: "Una casa dalla A alla Z", collettore a tutta larghezza (la foto tecnica), il 17 a 216 px con la scheda a tre righe; la parete d'inverno con la frase "Il lavoro migliore è quello che a cantiere chiuso non si vede più. In casa resta la temperatura giusta."; la chiusura "Dopo la Z, un numero solo" (l'ultima voce dell'indice, con il numero al posto della striscia); il piede su una riga. Un passo solo fra le sezioni: 160 px a 1440, 96 px a 390.

## Il confronto con Hambro e Paraga Pelli (prime schermate a 1440)

- **Allo stesso livello nell'impianto.** Come la fibbia di Hambro e la pelle di Paraga, qui un oggetto vero del mestiere occupa la schermata e regge la composizione: la barra del raccordo passa sotto il titolo da bordo a bordo, il gambo cade sulla T dell'alfabeto. Tre colori soli (calce, grafite, rame), un dettaglio editoriale in fondo alla schermata (l'alfabeto con i nomi, come il righello di Hambro e il nastro dei campioni di Paraga), un bottone e un link.
- **Riconoscibile come FM Sistemi.** Con un altro nome non regge: "Dalla A alla Z" è la loro frase, la T è la loro lettera, l'arco blu del logo è il loro segno. In chiaro la T in rame si legge meglio di prima: su nero il gambo si perdeva nel fondo, sulla calce la sagoma intera si vede in due secondi.
- **Sotto Hambro per la foto.** La fibbia di Hambro è nitida, in luce radente vera, con l'ombra vera. Il raccordo è un file di 2400 px ingrandito (a 1440 la barra è alta circa 170 px, a 1920 la morbidezza si vede) e l'ombra è disegnata. Finché non c'è lo scatto vero (LEGGIMI, foto 1), la prima schermata resta un gradino sotto.
- **Vicina a Hambro nel colore.** Calce e metallo caldo avvicinano due proposte della stessa zona che il committente vede in fila. La distanza la tengono la geometria a T, l'alfabeto, il bottone in rame con il testo scuro (Hambro: bruno con il testo bianco) e la tipografia (Funnel Display largo e stretto di crenatura). Paraga resta la più satura delle tre; FM è la più quieta.

## Caratteri e colori

- **Funnel Display** (titolo, lettere, capolettera, numeri grandi, frase della parete) e **Funnel Sans** (testo, menu, bottone): stessa superfamiglia, di The Funnel Project Authors (Dicotype), da Google Fonts, licenza SIL Open Font License 1.1 (testo in `sito/fonts/OFL.txt`). Serviti dalla pagina: `sito/fonts/funnel-display-latin.woff2` e `funnel-sans-latin.woff2`, variabili 300-800, usati a 400 e 500. Riferimenti: Aira (titolo enorme in un grottesco proprio, bianco su nero sopra una griglia in luce color rame) e Basalte (grottesco largo e leggero, forti salti di misura). Cifre tabellari su telefono, orari, partita IVA, date, indici. Nessun monospazio.
- **Scala:** 216 il 17, 160 apertura, 152 capolettera, 64 numero della chiusura, 56 h2 e frase della parete, 46 lettere dell'alfabeto, 30 voce della tavola, 28 nomi dei mestieri, 17-20 testo, 13-14 didascalie, indici e nomi.
- **Colori:** calce #EDE7DE (fondo, e fondo della foto d'apertura), grafite #23201C per il testo (13,2:1), secondario #5C554C (6,0:1), lettere spente #857C70 (3,3:1, solo in grande, nascoste ai lettori di schermo), filetti #D3CABD, rame #B4703A per il bottone e i segni sotto le lettere, rame per il testo #8F4F1F (5,2:1) per lettere accese, capolettera, inizio della riga e passaggio del mouse sui link. Il blu FM #046EA2 solo nell'arco del logo e nel segno del fuoco. Riferimenti per la luce: Hambro (oggetto in metallo su carta chiara con la sua ombra) e Kvadrat (fondi caldi, nessun bianco puro).

## Interazione

L'alfabeto è un `nav` con otto collegamenti. Clic, tocco, Tab e Invio portano alla riga del mestiere; la capolettera di quella riga riceve il segno di rame. Unica transizione: colore della lettera e del bottone in 0,12 s. Nessuna animazione allo scorrere, nessun effetto che segue il cursore, nessuno scorrimento morbido.

## Foto

Nessuna è di FM Sistemi (il sito ha solo una foto di repertorio, scartata). Tutte Pexels, licenza "Free" letta sulla pagina il 19/10/2026, elenco in `assets/CREDITI.md`; trattate con PIL (`_prova/script/finale_img.py`) ed esportate in 2-3 larghezze con srcset.
- T, apertura e riga 02: raccordo a T in rame, Magda Ehlers (3721272), unica a colori, scontornata e posata sulla calce
- R: cazzuola con malta, David Antonio Cruz Naira (38561969)
- E: quadro con interruttori, ranjeet . (28950842): solo morsetti bassi e cavi
- A: gocce d'acqua fitte su una superficie chiara, Mian Rizwan (15192101); al posto delle gocce su nero di Yogesh Jangid (7169730)
- P: griglia del ventilatore di un'unità esterna, Natalie Dmay (16848596): solo l'interno della griglia, marchio fuori dal taglio
- C: griglia di aerazione, Filipp Romanovski (16527887)
- F: moduli fotovoltaici, Tobi & Chris (11455626)
- M: presa di ricarica, Vitali Adutskevich (17000830), specchiata
- collettore del riscaldamento a pavimento, Pavel Danilyuk (7937309)
- parete d'inverno, luce di tapparella, Nathanael Arias (13742375), calda e schiarita

Le didascalie descrivono l'oggetto ("Nella foto: ...") e non dicono mai che è un lavoro loro.

## Controlli (19 ottobre 2026, dopo l'ultimo `build_finale.sh`, palette chiara)

- Contrasto di ogni testo sul suo fondo (`_prova/script/contrasto.mjs`): testo 13,2:1, secondario 6,0:1, rame per il testo 5,2:1, bottone 4,5:1, lettere spente 3,3:1 (solo testo grande). La frase della parete d'inverno, misurata sui pixel della foto dietro le lettere: almeno 10,3:1 a 390 e 10,9:1 a 1440.

- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 430, 600, 601, 768, 900, 1024, 1100, 1101, 1280, 1366, 1440, 1536, 1920 e 2560 (`_prova/script/finale_prova.mjs`).
- Interazione: a 1440 clic su A, E e P: la pagina va alla riga (bordo alto a 32 px), `:target` giusto, segno di rame acceso; foto, didascalia e alfabeto dell'apertura identici prima e dopo; `data-tav` non esiste. Tastiera: Tab arriva alla A, Invio porta a `#lavoro-a`, il Tab seguente prosegue da lì. Telefono 390: tocco su P porta a `#lavoro-p`.
- Collegamenti: `tel:+390498305354` (testata, bottone, numero della chiusura), `mailto:info@` e `mailto:commerciale@` con oggetto, Google Maps con l'indirizzo, Facebook, pagina partner Viessmann. Nessun `href="#"`, nessuna ancora rotta, console senza errori a 1440 e a 390.
- Screenshot a 320, 390, 768, 1024, 1440 e 1920 guardati a pezzi: nessuna sovrapposizione dopo le correzioni (a 768 il nome "Ristrutturazioni" toccava la sua riga, a 390 la M toccava il nome: corretti).
- `segnali.sh`: 0 soglie bloccanti. Foto 59,1 % della pagina, una superfamiglia (Funnel Sans 85,5 %, Display 14,5 %), mono 0 %, 0 frecce, un numero grande (17), data 2025. Da guardare: una sola misura di H2 (56 px; la gerarchia la fanno 160, 152 e 216 px) e la numerazione 01-08, che qui è l'ordine vero di un cantiere.
- Nessun carattere U+2014 in pagina, script, nota e LEGGIMI (controllo nel build). Orari con il trattino semplice "8.30-19.00".
- Nessuna chiamata a Google Fonts; nessun dato senza fonte in 01-analisi.md (le deduzioni sono nel LEGGIMI).
