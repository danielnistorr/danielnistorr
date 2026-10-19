# Tek.Lam, home finale: "Il foglio annidato"

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini `finale_img.py`, pagina `finale_build.py` da `finale_tpl.html`, controlli `controlla_finale.py`, prova del gesto `finale_prova.mjs`, screenshot). Parte dal prototipo A scelto dal giudice, con la luce, la tavolozza e alcune sezioni del prototipo B.

Screenshot: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg` (JPEG 85). Guardati a pezzi anche a 320, 768, 1024 e 1920.

## L'idea

La home è una lastra di inox 3000 x 1500 mm vista dall'alto sul banco del laser, subito dopo il taglio, disegnata in millimetri veri (viewBox 0 0 3000 1500; fra 700 e 1180 px lo stesso foglio senza il resto, 2400 x 1500; sul telefono la lastra si gira, 1500 x 3000). TEK.LAM è tagliato via dal foglio, TEK pieno e LAM chiaro come nel loro marchio, e nei vuoti delle lettere si vede il loro laser che taglia, col ventaglio di scintille (il fotogramma dello slider del loro sito, fuori fuoco perché sta sotto). Le sei lavorazioni sono sei pezzi ancora annidati nella lastra, e ognuno è ricalcato da un pezzo vero delle loro Realizzazioni: il frontale del case per l'elettromedicale, la griglia punzonata per la macchina movimento terra, lo sviluppo del cassetto per l'arredo odontoiatrico, il fianco del telaio inox, il telaio in tubolare del banco frigo con l'arco calandrato, il pezzo del modello 3D. Si tocca un pezzo, si stacca, e sul resto del foglio, inciso nel metallo e senza riquadro, compare la foto di quel pezzo finito in una finestra tagliata nella lastra, con la lavorazione e la macchina in una riga.

## Le prime due schermate

1. A 1440 (testata 56 px, foglio 1440 x 720, riga di 124 px). In alto TEK.LAM alto 216 px tagliato nella lastra, con il vuoto di taglio, il filo di luce e la tinta di rinvenimento paglia e bronzo lungo il taglio. Sotto, "Lamiera tagliata, punzonata, piegata e saldata per conto terzi, a Vigonovo". Poi i sei pezzi con le etichette 01-06 su una linea di base sola e la quota "3000 × 1500". Sul resto del foglio, a destra del taglio verticale: la finestra con la foto del pezzo (297 x 205 px), la didascalia ("Case per un apparecchio elettromedicale, da una nostra realizzazione."), un filetto, il nome della lavorazione, una riga di macchina e misure ("Bystronic Byspeed 4400 W, campo 3000 × 1500 mm"), il link alla riga della distinta. Testo scuro inciso sull'acciaio chiaro, contrasto 7,5-8:1 misurato sullo screenshot. Sotto il foglio, sul grafite: chi sono, dove, "Mandaci il disegno: ufftec@teklam.it".
   Da 1180 a 700 px: il foglio perde il resto (niente secondo taglio, niente striscia avanzata, 74 px fra la M e il bordo a 1024) e il cartellino scende sotto, sul grafite, con la stessa foto, a altezza fissa.
   A 390: la lastra si gira (390 x 780). TEK. e LAM su due righe, il titolo su due righe, i pezzi in tre colonne alti 91-98 px (il telaio frigo, orizzontale, 55 px), con numero e nome sotto, a 14-36 px dal pezzo; in fondo, sotto un taglio orizzontale, il cartellino inciso: finestra con la foto, nome, didascalia, link.
2. Una frase sola a tutta larghezza sul grafite, in Big Shoulders Display 300 a 108 px: "Non vendiamo un prodotto nostro: facciamo i pezzi del prodotto degli altri."

Dopo: "Dal foglio al pezzo finito", la distinta con le stesse sagome del foglio, piene; nella riga 01 l'interruttore Ferro, Inox, Alluminio con la sezione in millimetri veri; dopo la 02 la loro SG6 a tutta larghezza; "Dal ferro battuto alla lamiera" con la loro saldatura TIG a tutta larghezza e sotto il racconto e Sandro e Dimitri Volpato; la loro piegatrice a tutta larghezza; i settori come frase unica con le note numerate; i contatti sul grafite con il telefono, l'invito, la foto della sede e le quattro colonne; il piede con ragione sociale e P.IVA.

## Caratteri

- **Big Shoulders Display** (Google Fonts, SIL Open Font License 1.1), solo per i titoli e le etichette dei pezzi, 300 nei titoli grandi, 500-600 nelle etichette e nei nomi delle lavorazioni. Grottesco stretto disegnato sulla segnaletica industriale: diritte piatte e curve tese, come la lamiera piegata. Riferimenti: Zahner (aktiv-grotesk 200 maiuscolo a 120 px, titoli leggeri e grandi) e Bystronic (Moderat, tono da officina).
- **Sofia Sans** (Google Fonts, SIL OFL 1.1), per tutti i paragrafi, le didascalie, i dati e il telefono: 400 e 600, testo a 18 px con interlinea 1,55, cifre tabellari per misure e codici. Viene dal DIN, la scritta dei disegni tecnici e delle targhe delle macchine. Il telefono è Sofia Sans 200.
- File serviti dalla pagina: `sito/fonts/bsd-latin.woff2`, `sofia-latin.woff2`, `sofia-latin-ext.woff2`; licenze in `sito/fonts/OFL-bigshouldersdisplay.txt` e `OFL-SofiaSans.txt`. Nessun preload con crossorigin: aperta da file:// la console è pulita.

## Colori

Nero del letto `#0b0907`, grafite caldo `#15130f` (testata, riga sotto il foglio, frase, contatti, piede), bianco caldo `#f4f1ea`, carta `#efece6` con inchiostro `#16130f`. Lastra calda, `#B9B3A8` nei medi, luce dall'alto a sinistra; la grafite scende solo nell'angolo in basso a destra, così il resto del foglio dove è inciso il cartellino resta chiaro. Le due tinte di rinvenimento, paglia `#e2b46c` e bronzo `#8a5a2b`, solo lungo i tagli, sul bordo della finestra, sul link "Mandaci il disegno", sull'interruttore e sugli indici dei settori. Il rosso del logo `#e0281c` solo sulla linea di taglio del pezzo scelto. Niente gradienti di colore.

## Interazione

Un gesto: ogni pezzo è un pulsante (role button, aria-pressed). Clic, tocco, Invio o Spazio: il pezzo si solleva (10 x 16 px sul foglio largo, 4 x 7 px sul telefono) con un'ombra calda in 220 ms, sotto resta il vuoto col loro laser e la linea rossa del taglio, e il cartellino inciso cambia (aria-live): foto del pezzo vero, lavorazione, macchina. Le frecce spostano il fuoco fra i sei pezzi. La zona di presa è tutto il rettangolo del pezzo, fori compresi. Al passaggio del mouse il pezzo si alza appena. L'interruttore Ferro, Inox, Alluminio è nella riga 01 della distinta (radiogroup, frecce, Home e Fine, 44 px al dito) e cambia la sezione tratteggiata, alta in millimetri veri. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto sul cursore, hover a colore pieno; con riduzione del movimento le transizioni si spengono.

## Foto: origine e licenza

- Lastra: apryan widodo, Unsplash (inox spazzolato), tenuta solo la spazzolatura e rifatta la luce con PIL. È l'unica foto di repertorio rimasta in pagina.
- Tutte le altre sono di Tek.Lam, dal loro sito: `slide2-2` (letto), i pezzi finiti ritagliati dai collage di Realizzazioni (`lavorazione1-5`) e il render `pc` nelle finestre del cartellino, `slide3` (SG6), `slide1` (saldatura TIG), `slide4` (piegatrice), `fabbrica` (sede). Uso da confermare.
- Un trattamento solo per tutte, quello caldo di B; le foto grandi in più larghezze con srcset (la lastra del motivo SVG cambia misura via script secondo lo schermo). I ritagli dei pezzi sono piccoli (240-380 px) e restano alla misura nativa. 27 file, 2,3 MB.
- Elenco completo con URL e licenze: `assets/CREDITI.md`. Foto da rifare in officina: `LEGGIMI.md`.

## Cosa è cambiato nell'ultimo passaggio (giudizio cieco: K0 6, non inviabile)

- Tolta la nota di lavoro dalla prima schermata ("20 mm nella home del sito di oggi, 25 mm nella pagina Attrezzature. Spessori da confermare."): un valore solo per metallo (20/15/10 mm, quelli della home di oggi), il dubbio solo nel LEGGIMI. L'interruttore è sceso nella riga 01 della distinta.
- Le sei sagome generiche (flangia, pannello, fazzoletto, sviluppo di scatola) sono state ridisegnate da pezzi veri delle loro Realizzazioni; il letto di Cardinalli nei vuoti delle lettere è stato sostituito dal loro laser che taglia (`slide2-2`).
- Tolto il cartellino chiaro appoggiato sul foglio (stesso componente della home di Paraga Pelli: foto, nome e numero su una riga, coppie etichetta e valore): ora nome, macchina e misure sono incisi direttamente sul resto della lastra, senza riquadro, e la foto del pezzo vero sta in una finestra tagliata, larga il 100 % della colonna. Tolti dalla prima schermata l'interruttore (gesto della home di Mario Agnoletto), la sezione e la scala in millimetri: resta una riga di dati.
- Fra 1180 e 700 px niente più secondo taglio e striscia di foglio avanzata a destra: c'è un foglio a parte di 2400 x 1500, senza resto.
- Zona di presa dei pezzi: un rettangolo trasparente su tutto il pezzo; la prova a griglia 9 x 9 dà 81/81 su tutti e sei, a tutte le larghezze.
- Telefono: pezzi alti 91-98 px (prima 52-69), etichette sotto il pezzo, su due righe corte (numero e nome), a 14-36 px dal pezzo; il pezzo sollevato non tocca nessuna etichetta.
- Via tutte le "Foto indicativa": le strisce di repertorio (taglio di Cardinalli, lamiera forata di Sayles, piegatrice e ugello di Yurtman) sono state sostituite dalle loro foto (SG6, piegatrice) o tolte; il cartellino 05 mostra il loro telaio in tubolare.
- Storia: la loro saldatura TIG a tutta larghezza, il racconto sotto; tolte le due miniature seppia (la sede è passata nei contatti, con lo stesso trattamento delle altre foto).
- Contatti: niente più telefono gigante su foto scura; grafite pieno, telefono a 120 px, la foto della sede, le quattro colonne con le etichette a contrasto pieno.
- Riga sotto il foglio fra 900 e 1180 px: indirizzo su una colonna larga, "(VE)," non resta più solo.
- Distinta sul telefono: "Verniciatura e consegna" parte dalla stessa colonna di "Tubi e profili".
- Cartellino ad altezza fissa: a 1440 il bordo sotto è lo stesso per tutti e sei i pezzi; sotto il foglio, fra 700 e 1180 px, altezza minima uguale per tutti.
- Tolti i due preload dei caratteri con crossorigin: nessun errore in console aperta da file://.
- Titolo della distinta: da "Le lavorazioni e le macchine" a "Dal foglio al pezzo finito"; nessuna frase sul "sito di oggi" in pagina.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti. Area foto 36,3 %, monospazio 0 %, 2 famiglie (Sofia Sans 86 %, Big Shoulders 14 %), 16 filetti, 0 frecce, 0 etichette sopra i titoli, 0 titoli a sinistra con paragrafo a destra, nessun divieto trovato.
- Da guardare, con la ragione: 6 fasce di fondo (grafite della riga e della frase, carta delle lavorazioni e della storia spezzata da due foto, carta dei settori, grafite dei contatti e del piede); 12 voci numerate (i sei pezzi del foglio ripresi nella distinta e le sei note dei settori).
- `finale_prova.mjs`: scrollWidth uguale a innerWidth a 320, 360, 390, 768, 900, 1024, 1280, 1440, 1920 e 2560; il cartellino non copre nessun pezzo, né a riposo né sollevato; tocco (a 390 e 320, touchscreen) e clic (a 1440 e 1024) su tutti e sei i pezzi; frecce, Invio e Spazio; interruttore con tocco, clic, frecce e Home; nessun errore in console.
- Collegamenti: `tel:+390499801486` (testata, contatti, colonna), `mailto:` per ufftec, commerciale, info, sandro, dimitri, mappa su Google Maps con "Via del Lavoro 68 Vigonovo VE".
- Nessun U+2014 nella pagina, nei .md e negli script (`controlla_finale.py`); nessun segnaposto in pagina; nessuna "Foto indicativa", nessun "da confermare" e nessun "sito di oggi" in pagina.
- Dati: tutti da `01-analisi.md` e `_prova/testi.txt`. Restano fuori le portate delle piegatrici, l'autocarro da 35 quintali, la TrumaBend e i dati Atoka; gli spessori del laser sono quelli della home di oggi.
