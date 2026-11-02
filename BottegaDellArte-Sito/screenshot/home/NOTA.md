# Bottega dell'Arte, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot con `scatti_finale.cjs`, controlli con `verifica.cjs`, segnali). Altezza a 1440: 4592 px compreso il piede; a 390: 5395 px; a 768: 5806 px.

Base: il prototipo A, "Prima e dopo". Questo è l'ultimo passaggio dopo il giudizio cieco (55,5 su 80): stessa idea e stessa direzione, apertura rifatta come chiedeva il giudice.

## L'idea

Il portone d'ingresso che hanno restaurato, visto da vicino come quando ci si sta davanti: il legno riempie in altezza la prima schermata a filo del bordo destro, con il maniglione in ottone e la toppa. Sotto il titolo, due bottoni Prima / Dopo scambiano di netto le due foto vere dello stesso portone, raddrizzate sullo stesso rettangolo e tagliate allo stesso punto: prima la vernice scurita e i fori della ferramenta tolta, dopo la venatura riportata a vista e il maniglione nuovo. La riga accanto dice cosa è stato fatto con le parole della loro scheda. Con il nome di un concorrente la pagina non regge: servono le due foto del loro portone.

## Cosa è cambiato in questo passaggio

- **Il pezzo è grande.** Prima la porta intera era una striscia di 239 x 680 px (17 % della larghezza). Ora il portone è tagliato sui pannelli centrali con il maniglione e occupa 592 x 900 px a 1440 (41 % della larghezza, dalla cima della pagina al fondo della prima schermata; la testata gli sta accanto). A 1024 e 1920 è sempre il 41 %, a 768 il 49 % e a 390 tutta la larghezza. Il "dopo" ha meno arancio: saturazione da 0,94 a 0,80 e un bilanciamento meno rosso, così il legno si legge come noce e non come laminato. Le foto sono raddrizzate già in grande (900 px di larghezza) con una maschera di contrasto.
- **Niente legende con pallino e filo**, niente pavimento con il bottone del telefono: era il gesto di Mario Agnoletto e sembrava una barra strumenti. Il telefono a 1440 è un link testuale sotto la frase (049 900 4916 e l'email); a 390 resta il bottone pieno "Chiama". L'unico blocco pieno della prima schermata è lo stato attivo dell'interruttore.
- **La riga di stato sta accanto all'interruttore** (a 1024 e sotto va sotto): ora è dentro la piega a 1024 x 768 (fondo a 728), 1280 x 720 (668), 1440 x 900 (848), 1920 x 1080 (1028), 768 x 1024 (1020), 390 x 844 (744) e 320 x 640 (600).
- **I lavori:** non più tre foto 4:5 uguali con link ripetuti. Il sottoscala con la nicchia in ottone grande (7 colonne, a filo del bordo sinistro, tagliato sopra il pavimento e prima di pianta e lampadario) e la porta a bilico più piccola e sfalsata, a filo del bordo destro, con le alte luci del muro recuperate. Il titolo di ogni lavoro è il link alla pagina.
- **Il restauro** tiene le porte del Bo (ora larghe 7 colonne) e assorbe la riga delle finiture. La frase rifatta è quella del loro testo: "Usiamo legno vecchio della stessa essenza del mobile da restaurare." Tolte foglia d'oro e patinatura veneziana (senza prove: sono nel LEGGIMI). Restano vernice all'acqua, laccatura e gommalacca.
- **Tolta la sezione di solo testo:** la frase sui due soci è diventata il sottotitolo della chiusura.
- **La chiusura** non usa più il maniglione (era lo stesso oggetto dell'apertura e ripeteva la didascalia): ora ci sono due porte a vetri piombati restaurate, frontali, 704 x 704 px a filo del bordo destro, didascalia "Porte con vetri a piombo, restaurate." I recapiti sono uno per riga: Mauro e il suo numero, Giuliano e il suo numero.
- **Ritmo:** distanza tra le sezioni da 224 a 200 px, margine del piede da 200 a 160 px; a 768 e a 390 da 112 e 96 px. Il giudice proponeva 160 e 120: con la sezione di solo testo tolta la pagina a 1440 sarebbe scesa sotto i 4500 px chiesti dal committente, quindi 200 e 160, con le foto più grandi a riempire.
- **Menu sotto i 900 px:** si chiude al tocco su una voce (verificato: `aperto` false, `aria-expanded` false) e con Esc, che riporta il fuoco sul bottone.
- **Link coerenti:** "Contatti" nella testata porta a `#contatti`; dalla colonna Bottega del piede è uscita la voce "Contatti" (c'è già la colonna). La colonna Bottega ha Chi siamo, Realizzazioni, Palazzo del Bo.
- **768:** il titolo va in tre righe ("il&nbsp;legno", "nel&nbsp;passato", larghezza massima 8,4 em), sotto a sinistra frase, recapiti e interruttore, a destra il portone alto 724 px. Piede su tre colonne. La pagina scende da 6628 a 5806 px.

## Le schermate

- **1440, prima schermata.** Testata con il logo e cinque voci a sinistra; titolo Zodiak 92 px in tre righe, la frase su chi sono, telefono ed email; in basso "Restauro di un portone d'ingresso", l'interruttore Prima / Dopo e la riga. A destra il portone a tutta altezza.
- **Poi:** "Su misura, in stile o moderni" con i due lavori; le porte del Bo con il restauro, il Bo e le finiture; la chiusura; il piede.
- **390.** Titolo in tre righe, il portone a tutta larghezza alto 404 px, l'interruttore a tutta larghezza, la riga, il bottone del telefono e l'email: tutto dentro i primi 844 px.
- **Piede.** Fascia #ECE8DF, niente ombra. Logo vero PNG a 2x largo 260 px con una riga su chi sono; colonne Lavorazioni, Bottega, Contatti; in fondo ragione sociale, sede legale, P.IVA, Privacy, Cookie e "Torna su". A 390 le colonne si impilano in ordine.
- **Niente Seguici:** non hanno social. **Niente newsletter:** il sito è fermo al 2021 e non hanno novità, fiere, cataloghi o collezioni da comunicare; il privato compra un armadio o un restauro ogni tanti anni.

## Caratteri e colori

- **Zodiak** 400 in tondo (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito) per titoli, finiture e telefono della chiusura; mai il corsivo. Serif contrastata che sta accanto alla firma calligrafica del logo senza imitarla; riferimento Bottega Ghianda.
- **Schibsted Grotesk** 400 e 500 (Google Fonts, SIL Open Font License 1.1) per testi, menu, bottoni e piede, cifre tabellari sui numeri di telefono. Tutti e due serviti dalla pagina in `sito/fonts/`, licenze in `sito/fonts/LICENZE.txt` e `OFL-Schibsted-Grotesk.txt`.
- **Colori:** calce #F4F2EC, pavimento #ECE8DF (piede e passaggio sull'interruttore), inchiostro noce #2A2119 (14,1:1), grigio #5F574F (6,3:1 sulla calce, 5,8:1 sul piede), accento marrone del logo #6F3219 (8,7:1) sul bottone del telefono a 390 e al passaggio sui link. Contrasto AA ovunque.

## Interazione

Un solo gesto: l'interruttore Prima / Dopo. `aria-pressed`, frecce sinistra e destra, Invio e spazio, riga con `aria-live`, bersagli alti 52 px. Scambio netto, senza dissolvenza; l'unica transizione (0,12 s) è il colore del bottone toccato. Nessuna animazione allo scorrimento, niente che segue il cursore, nessun hover con opacità.

## Foto: origine e licenza

Tutte dell'azienda, dalla libreria media del sito bottegadellartesnc.it (`assets/originali/`), lavorate con PIL (`_prova/script/finale_img.py`) ed esportate in WebP a più larghezze con srcset:
- portone dopo `2020-10_Port-3.jpeg` e prima `2020-10_Port.4.jpeg` (scheda `/progetti/portone-dingresso/`), raddrizzati sullo stesso rettangolo 900 x 2760, stessa luce da sinistra;
- sottoscala `2020-05_Bottega_dell_Arte_Armadiature-1.jpeg`; porta a bilico `2020-06_porte-a-bilico-2-scaled.jpg`;
- Palazzo del Bo `2020-06_universita08.jpg` (700 x 500, con una copia ingrandita 1,5x per gli schermi densi);
- porte a vetri piombati `2020-06_porte_restaurate.jpg` (sensore sul muro coperto con il colore del muro);
- logo `logo-bottega-arte-1014.png`; icona `logo-monogramma-B-512.png`.

Nessun segnaposto esterno, nessuna foto di repertorio, nessuna immagine generata. Il portone a 1440 è ingrandito da una porta che nella foto originale è larga 482 px: si vede morbido da vicino, e la foto da rifare è la prima della lista nel LEGGIMI.

## Controlli

- Screenshot di consegna guardati a pezzi (1440 e 390 interi, prime schermate); di controllo a 320, 768, 1024, 1920, stato Prima a 1440 e 390, menu aperto a 390.
- `verifica.cjs`: larghezza del documento uguale alla finestra a 320, 360, 390, 414, 560, 600, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560; riga di stato dentro la piega alle misure sopra; tastiera (frecce, Maiusc+Tab e Invio), tocco su Prima, menu (apertura, chiusura al tocco su una voce, Esc).
- Collegamenti: `tel:+390499004916`, `tel:+393477641720`, `tel:+393474109263`, `mailto:info@bottegadellartesnc.it`, mappa `https://goo.gl/maps/QuC7VTkbjjd1Gpvh6`, Privacy iubenda, `cookie-policy/`.
- Nessun U+2014 nella pagina, nella nota e nel LEGGIMI (controllato dallo script di build).
- `segnali.sh` a 1440: 18 soglie su 18 a posto o da guardare, nessuna da correggere; area coperta da foto 35,3 % (era 22 %). "Contenuto datato": nessuna data in pagina, perché l'anno 2004 e i "40 anni" sono da confermare; i nomi ci sono (Mauro Nosarini, Giuliano Saibene, Palazzo del Bo, Gio Ponti).
- A occhio: niente corsivo, niente badge, niente tre box con icona, niente card, niente gradienti, niente icone, niente legende.
