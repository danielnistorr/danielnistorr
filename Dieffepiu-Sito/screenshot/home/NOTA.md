# Dieffepiu, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze con `srcset`), carattere in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, controllo U+2014, screenshot con `shot_finale.mjs`). Base: prototipo A, "Il pezzo", con gli innesti di B.

Altezza a 1440: 5.482 px, piede compreso (era 6.436). A 390: 6.040 px.

## Idea

Dieffepiu non fa zanzariere: fa i pezzi e le macchine con cui le fanno gli altri. La home mette in scena un pezzo solo, il cingolo del sistema TANK® arrotolato, scontornato sulla carta della pagina e annotato come nella tavola esplosa del loro catalogo: punto sul pezzo, filetto di 1 px, codice. Sotto, la stessa logica: le linee come indice, i profili con codice e peso al metro, le testate sulla carta, le macchine misurate con una barra gialla in scala, il giallo delle loro carrozzerie e l'unico colore deciso della pagina.

## Cosa è cambiato nel giro 3 (dal giudizio cieco)

- **Apertura propria.** Titolo "Per chi fa zanzariere" al posto di "Sistemi per zanzariere" (che resta nel `<title>` e apre il sottotitolo): dice il mestiere vero, fornitore di chi produce, e con il nome di Neher o Bettio, che vendono la zanzariera finita, non regge. Sul cingolo due legende: "TK101 Cingolo" (il codice della tavola esplosa del TANK REVOLUTION®, catalogo p. 93) e "Occhielli di attacco"; sotto il pezzo, su un filetto, "TANK REVOLUTION® laterale, fino a 3.000 × 1.900 mm, ingombro minimo 50 mm". A 1440 la legenda degli occhielli va a sinistra nel bianco, quella del cingolo sale sopra il pezzo accanto al titolo; da 960 in giù salgono tutte e due nella fascia sopra il pezzo; a 370 e meno "Occhielli" si accorcia.
- **Ritaglio del cingolo rifatto** dall'originale a 3166 px: prima l'alfa era "1 meno luminanza" e le chiazze grigie del fondale restavano semitrasparenti. Ora una maschera vera (solo il nero del pezzo dentro il poligono, riflessi delle maglie riempiti, luce interna della spirale, fessura sotto il giro esterno e fori degli occhielli trasparenti, un frammento grigio nella fessura cancellato), bordo con rampa di 1-2 px, colori del bordo ripuliti dal chiaro del fondale, una sola ombra di contatto calda e continua (due sfocature gaussiane della sagoma, al 30 e al 16 %), niente maschera di contrasto, WebP a qualità 92 con alfa a 100. Guardato al 200 % a 768, 1024 e 1440: nessuna macchia grigia fuori dal pezzo.
- **Tolto il fotogramma ATT030** (morbido, con il bordo scuro e la didascalia doppia): la sezione Macchine è il selettore con la barra gialla.
- **Tolta la fascia dello spazzolino** (piano marrone scuro, altra luce).
- **Linee**: ROLLY STYLE 1, ROLLY STYLE WOOD e ROLLY STYLE 3 scritte come tre voci, così l'elenco conta davvero quattordici.
- **Scheda della sezione Sistemi**: i dati del TANK REVOLUTION® sono saliti in apertura; al loro posto i quattro profili TANK con codice e peso al metro (DFTK005-DFTK008, catalogo p. 91).
- **Selettore**: titolo "Da 3 a 8,2 metri di lavoro" (la scala mette insieme piano, banco e tubi); lo span del codice vuoto della saldatrice per tubi è nascosto.
- **Chi siamo**: tolta la frase sulle lingue; la fiera ora è "cinque fiere dal 2021 a oggi, l'ultima a Parigi tra settembre e ottobre 2026".
- **Chiusura**: foto più grande (7 colonne su 12 a 1440, 820 px di altezza), titolo su due righe decise, "Apri la mappa" su una riga sua.
- **Piede**: recapiti sotto la riga su chi sono (tel:, mailto:, indirizzo con la mappa), così restano anche nelle pagine interne; a 1024 la firma sta a sinistra e la newsletter a destra, le colonne sotto; Instagram tolto (non verificato); messaggio `aria-live` all'invio della newsletter; a 390 link alti 44 px.
- **Lingue**: IT, EN, DE visibili fino a 961 px e in fondo al menu del telefono, con `href` veri (`/`, `/en/`, `/de/`).
- **Logo** senza la riga piccola "SISTEMI PER ZANZARIERE" (a 50 e 104 px sarebbe una macchia gialla di 4-7 px).

Respinto: il filetto giallo in scala sotto il cingolo (alternativa del giudice): il giallo resta delle macchine, le legende bastano a rendere propria l'apertura.

## Prime due schermate

- **1440.** "Per chi fa zanzariere" su una riga, Pathway Extreme stretto e leggero a 164 px. A destra il cingolo a 872 px con le due legende e la riga delle misure; a sinistra in basso la frase su cosa fanno (sistemi e macchine, Saonara, dal 1987), il bottone "Chiamate +39 049 8791175" (tel:) e il catalogo PDF. Tutto dentro i 900 px. Seconda schermata: "Progettiamo e produciamo i sistemi e le macchine con cui altre aziende fanno le zanzariere", il 1987 e gli oltre 2.000 impianti, due righe su Di Franco, via Lombardia e le fiere.
- **390.** Titolo su due righe a 84 px, le legende sopra il cingolo a tutta larghezza, la riga delle misure, la frase e il bottone del telefono: tutto dentro gli 844 px.

## Caratteri e colori

- **Pathway Extreme** (Eduardo Tunni, Google Fonts, SIL Open Font License 1.1, testo della licenza in `sito/fonts/OFL-Pathway-Extreme.txt`), una sola famiglia variabile servita dalla pagina (latin e latin-ext). Titoli a larghezza 78-92 % e peso 400-420; testo a larghezza 100 % in 400; 500 per menu, bottoni, codici e titoletti. Cifre tabellari per codici, misure, pesi, orari e telefono. Riferimenti: FSB (un solo pezzo di ferramenta grande su fondo chiaro, Trade Gothic Next), Emmegi e Vitrocsa (una frase sicura in un peso leggero e grande).
- **Colori**: carta #F3F1EB, inchiostro #16191B, grigio #4C5155 (7,1:1 sulla carta, 6,4:1 sul piede #E9E6DD), blu del marchio #006B9D per link al passaggio e fuochi (5,2:1), giallo macchina #F2B705 solo come campitura della barra (testo inchiostro sopra, 9,7:1). Nessun gradiente, nessuna ombra sui riquadri, nessun modo scuro.

## Interazione

Un gesto solo, nella sezione Macchine: quattro bottoni (Basic ATT001-B, ATT007, Tubi rete 6 m, ATT030) con `aria-pressed`; la barra gialla prende la lunghezza vera sulla scala di 8,2 m (transizione di 0,24 s solo sulla barra, tolta con `prefers-reduced-motion`), cambiano nome, codice e fino a quattro dati del catalogo; frecce destra e sinistra, zona `aria-live`. Il resto è servizio: menu a 960 px e meno con le lingue in fondo, piede a fisarmonica a 600 px e meno con bottoni veri, messaggio della newsletter. Nessuna animazione allo scorrimento, nessun effetto sul cursore, nessun hover che sbiadisce. Le legende sono statiche (`aria-hidden`, con il testo equivalente nella didascalia per i lettori di schermo).

## Foto: origine e licenza

Tutte dell'azienda, nessuna foto di repertorio, nessuna immagine generata. Diritti da chiedere.
- **Cingolo TANK** (apertura): `assets/originali/slides_2-6__...-2.jpg`, sito dieffepiu.it, 3166 px; parete ricostruita sotto la guida destra, maschera e ombra come sopra, specchiato perché gli occhielli guardino il titolo; 640, 960 e 1376 px.
- **Testate e supporti**: `slides_2-8__imm05.jpg`, sito, 2961 px, fondo portato alla carta dentro un involucro unico degli oggetti.
- **Chiusura, rotoli di fettuccia**: `slides_2-2___DSC4780.jpg`, sito, 1280 px, appena scaldata.
- **Logo**: `logo-dieffepiu-1396x857.png`, tagliato sopra la riga piccola, WebP senza perdita a 2x. Non ricostruito in SVG: le scritte non si rifanno fedeli senza il file originale.

## Chiusura e piede

- **Chiusura** ("b con foto", testo a sinistra e foto fino al bordo destro): il motto del catalogo (p. 2) "I valori di sempre, lo sguardo al futuro"; telefono grande con tel:; info@dieffepiu.it con mailto:; via Lombardia 33, zona industriale di Villatora, "Apri la mappa" (Google Maps); orari.
- **Piede**: logo, una riga su chi sono, tel:, mailto: e indirizzo con la mappa; la newsletter "Fiere e aggiornamenti del catalogo" (ha senso: una fiera quasi ogni anno, il catalogo che cambia, clienti professionali registrati; non invia nulla finché non si collega un servizio); quattro colonne: Sistemi, Macchine, Azienda, Seguici (YouTube, Facebook). Riga legale: © 2026 Dieffepiu S.r.l., P.IVA IT01335450282, REA PD-204413, capitale sociale 300.000 euro, PEC, Privacy, Cookie (iubenda). A 390 le colonne si aprono a fisarmonica.

## Controlli (20/10/2026, dopo il giro 3)

- Screenshot guardati a pezzi a 1440 e 390 (pagina intera), e a 320, 768, 1024 e 1920 (prima schermata e chiusura); il cingolo ingrandito al 200 % a 768 e 1024. Correzioni fatte guardando: riga delle misure su una riga a 1440, legende che a 320 si toccavano, bottone del telefono dentro gli 844 px a 390, titolo della chiusura a due righe.
- `prova_giro3.mjs`: scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 768, 961, 1024, 1180, 1280, 1440, 1920 e 2560; menu del telefono con Italiano, English, Deutsch (bersagli di 50 px); newsletter bloccata senza consenso e con messaggio dopo email e consenso; link del piede a 390 alti 44 px; nessun Instagram; nessun `href="#"`; tel:+390498791175, mailto:info@dieffepiu.it, mailto:dieffepiu@pec.it e la mappa corretti.
- `prova_gesto.mjs`: selettore con frecce, Invio e tocco; fisarmonica chiusa e aperta al tocco.
- `segnali.sh` (uscita in `_prova/segnali-finale/`): 17 soglie su 18 a posto; resta sotto soglia l'area foto, 30,2 % contro 35 %, perché il giro 3 ha tolto le due foto deboli che il giudice chiedeva di togliere. Come dice la guida per le aziende senza foto grandi, non lo copro con foto di repertorio: è la prima cosa da chiedere (LEGGIMI, "Foto da rifare dal vero"). Nessun divieto del committente, una famiglia sola, 3 misure di H2, nessuna freccia, nessuna tabella.
- Nessun U+2014 nella pagina, nella nota, nel LEGGIMI e negli script (controllo nel `build_finale.sh`).
- Dati: tutti da `01-analisi.md`, dove ho aggiunto con la fonte i codici TK101 e DFTK005-DFTK008 letti sulle pagine 91 e 93 del catalogo. Il resto da confermare è nel `LEGGIMI.md`.
