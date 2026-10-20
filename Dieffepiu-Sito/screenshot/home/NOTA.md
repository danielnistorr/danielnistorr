# Dieffepiu, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze con `srcset`), carattere in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, controllo U+2014, screenshot con `shot_finale.mjs`). Base: prototipo A, "Il pezzo", con gli innesti di B indicati dal giudice.

Altezza a 1440: 6.436 px, piede compreso. A 390: 6.418 px.

## Idea

Dieffepiu non fa zanzariere: fa i pezzi e le macchine con cui le fanno gli altri. La home mette in scena un pezzo solo, il cingolo del sistema TANK® arrotolato, scontornato sulla stessa carta della pagina, grande e fermo, con gli occhielli rivolti verso il titolo. Sotto, la stessa logica del catalogo: le linee come indice, le testate sulla carta, e le macchine misurate con una barra gialla in scala, il giallo delle loro carrozzerie e l'unico colore deciso della pagina.

## Prime due schermate

- **1440.** In alto "Sistemi per zanzariere" su una riga, Pathway Extreme stretto e leggero a 164 px. Sotto, a destra, il cingolo a 872 px di larghezza; a sinistra, in basso, una frase su cosa fanno e per chi (profili, componenti e kit, e le macchine per produrle, Saonara, dal 1987), il bottone "Chiamate +39 049 8791175" (tel:) e il link "Catalogo PDF, 76 MB". Didascalia di una riga sotto il pezzo: "TANK®, il cingolo della zanzariera a catena". Niente tabella, niente "Tav.", niente cambio di vista. Seconda schermata: la frase grande "Progettiamo e produciamo i sistemi e le macchine con cui altre aziende fanno le zanzariere", con il 1987 e gli oltre 2.000 impianti, e due righe su Di Franco, via Lombardia e la fiera BATIMAT 2026 con padiglione e stand.
- **390.** Titolo su due righe a 84 px, il cingolo a tutta larghezza, la didascalia, la frase, il bottone del telefono e il catalogo: tutto dentro gli 844 px. Telefono anche nella testata, menu con un bottone vero.
- **Il resto, in ordine.** Una fascia a tutta larghezza con lo spazzolino in due giri su piano scuro; "Quattordici linee a catalogo" come indice tipografico con accanto la scheda TANK REVOLUTION® laterale (3.000 x 1.900 mm, ingombro minimo 50 mm, profili EN-AW 6060 T5); la tavola delle testate a tutta larghezza e due righe sui colori; le dodici macchine con il fotogramma dell'ATT030 a 860 px e il selettore con la barra gialla; la chiusura e il piede.

## Caratteri e colori

- **Pathway Extreme** (Eduardo Tunni, Google Fonts, SIL Open Font License 1.1, testo della licenza in `sito/fonts/OFL-Pathway-Extreme.txt`), una sola famiglia variabile servita dalla pagina (latin e latin-ext). Titoli a larghezza 78-92 % e peso 400-420 con spaziatura da -0,01 a -0,03 em; testo a larghezza 100 % in 400; 500 per menu, bottoni e titoletti. Cifre tabellari per misure, pesi, orari e telefono. Riferimenti: **FSB** (un solo pezzo di ferramenta grande su fondo chiaro, Trade Gothic Next: Pathway viene dallo stesso grottesco stretto americano), **Emmegi** e **Vitrocsa** (una frase sicura in un peso leggero e grande). Nessun'altra home della campagna usa Pathway.
- **Colori**: carta #F3F1EB (scaldata dal #F4F3EF del prototipo, come chiesto), inchiostro #16191B, grigio #4C5155 per il testo secondario (7,1:1 sulla carta, 6,4:1 sul piede #E9E6DD), blu del marchio #006B9D solo per link al passaggio e fuochi (5,2:1), giallo macchina #F2B705 solo come campitura della barra in scala, mai come colore di testo (sul giallo il testo è inchiostro, 9,7:1). Bottoni in inchiostro con testo bianco (17,7:1), al passaggio diventano blu pieni. Nessun gradiente, nessuna ombra sui riquadri, nessun modo scuro.

## Interazione

Un gesto solo, innestato da B nella sezione delle macchine al posto della tabella a filetti: quattro bottoni (Basic ATT001-B, ATT007, Tubi rete 6 m, ATT030) con `aria-pressed`; la barra gialla prende la lunghezza vera della macchina sulla scala di 8,2 m (transizione di 0,24 s solo sulla barra toccata, tolta con `prefers-reduced-motion`), cambiano nome, codice e fino a quattro dati del catalogo, con le etichette corrette ("Piano 3.000 mm" per ATT001-B; "Banco e saldatrice automatica per tubi rete da 6 m"). Frecce destra e sinistra per passare da una macchina all'altra, zona dei dati `aria-live`; provato con tastiera e tocco (`_prova/script/prova_gesto.mjs`). Senza JavaScript resta visibile ATT030. Il resto è servizio: menu a 960 px e meno, piede a fisarmonica a 600 px e meno con bottoni veri. Nessuna animazione allo scorrimento, nessun effetto sul cursore, nessun hover che sbiadisce.

## Foto: origine e licenza

Tutte dell'azienda, nessuna foto di repertorio, nessuna immagine generata. Diritti da chiedere (chi ha scattato e girato i video).
- **Cingolo TANK** (apertura): `assets/originali/slides_2-6__...-2.jpg`, sito dieffepiu.it, 3166 px. Rifatto dall'originale: fondo stimato e portato alla carta; tolto il taglio piatto del prototipo seguendo la fessura vera tra cingolo e guida a sinistra; sotto la colonna della guida a destra la parete del cingolo è ricostruita copiando la stessa parete 172 px più in là, colonna per colonna; ombra di contatto corta disegnata dove le guide la toglievano; luce un po' più calda sui riflessi delle maglie; immagine specchiata in orizzontale perché gli occhielli guardino il titolo. Esportato a 640, 960 e 1376 px in WebP con trasparenza (anche la tavola delle testate): il browser posa il pezzo e la sua ombra sulla carta della pagina, così non si vede il bordo della foto.
- **Spazzolino** (fascia dopo la seconda schermata): `difranco__home5.jpg`, vecchio sito difranco.it (stessa P.IVA), 1900 px.
- **Testate e supporti**: `slides_2-8__imm05.jpg`, sito, 2961 px; fondo portato alla carta dentro un involucro unico degli oggetti, così lo stacco grigio del fondale in basso a destra non c'è più.
- **Banco ATT030**: anteprima del video YouTube dell'azienda `youtube-anteprima__Dxt6fEBRLbA.jpg` (1280 x 720), con il trattamento di B (bianchi puliti, colori smorzati tranne il giallo, grana fine), tolto il bordo destro, mostrata al massimo a 860 px perché la morbidezza non si veda.
- **Chiusura, rotoli di fettuccia**: `slides_2-2___DSC4780.jpg`, sito, 1280 px, appena scaldata. Non compare altrove nella pagina né in altre home della campagna.
- **Logo**: `logo-dieffepiu-1396x857.png` rifilato, WebP senza perdita a 2x (112 e 192 px di altezza). Non ricostruito in SVG: le scritte piccole non si rifanno fedeli senza il file originale.

## Chiusura e piede

- **Chiusura** ("b con foto", testo a sinistra e foto fino al bordo destro): il motto del catalogo (p. 2) "I valori di sempre, lo sguardo al futuro"; telefono +39 049 8791175 grande con tel: e sottolineato nell'inchiostro della pagina, scritto uguale in testata, bottone e chiusura; info@dieffepiu.it con mailto:; "Via Lombardia 33, 35020 Saonara (PD), apri la mappa" con il link a Google Maps; zona industriale di Villatora; orari.
- **Piede** (impaginazione di B): a sinistra il logo, una riga su chi sono e la newsletter "Fiere e aggiornamenti del catalogo" (campo, bottone, casella del consenso; non invia nulla finché non si collega un servizio); a destra quattro colonne: Sistemi, Macchine, Azienda, Seguici (YouTube, Facebook, Instagram come parole). Tolta la colonna Contatti che ripeteva la chiusura. Riga legale: © 2026 Dieffepiu S.r.l., P.IVA IT01335450282, REA PD-204413, capitale sociale 300.000 euro, PEC dieffepiu@pec.it, Privacy, Cookie (iubenda di oggi). A 390 le colonne si aprono a fisarmonica.

## Controlli

- `segnali.sh` sulla pagina (uscita in `_prova/segnali-finale/`): 0 soglie bloccanti, 0 da guardare. Area foto 37,3 %, una famiglia sola, 3 misure di H2, 2 fasce di fondo, 2 filetti, nessuna freccia, nessuna tabella, date trovate (1987, BATIMAT 2026), nessun divieto.
- Screenshot guardati a pezzi a 1440 e 390, e a 320, 768, 1024 e 1920: nessuno scorrimento orizzontale (a 320 la testata usciva di 6 px: corretta), nessuna sovrapposizione (a 1024 la didascalia toccava il pezzo: corretta).
- Nessun U+2014 nella pagina, nella nota, nel LEGGIMI e negli script (controllo nel `build_finale.sh`).
- Dati: tutti da `01-analisi.md`. Tolti dalla pagina perché da verificare: norma EN UNI 13561 e freno FX135, stato "brevettato" o "patent pending" del TANK 2.0. Il resto da confermare è nel `LEGGIMI.md`.
