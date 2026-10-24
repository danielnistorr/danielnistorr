# Solettificio Tollin, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze con srcset, l'oggetto d'apertura con la trasparenza, logo PNG), carattere in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini da `_prova/script/finale_img.py`, pagina da `_prova/script/finale_index.html`, screenshot e prove da `_prova/script/finale_shot.mjs`, segnali da `_metodo/kit/segnali.sh`); le prove della rifinitura (schede con tastiera e tocco, logo a zoom 4x, link) con `node _prova/script/prova_rifinitura.mjs <cartella>`. Altezza a 1440: 4520 px, piede compreso.

## Idea

Il foglio in negativo. Dal plotter della modelleria esce un foglio di cartoncino da cui le sagome dei sottopiedi sono già state tagliate via: restano i fori. In apertura c'è quel foglio, scontornato dalla loro foto, e dai fori si vede la carta della pagina. È un oggetto che ha solo un solettificio: con il nome di un concorrente la pagina non regge. Poi i quattro reparti di via Irpinia, uno per volta, con le foto vere.

## Prime due schermate

- **1440, prima schermata**: fondo carta #F3EFE8; testata con il logo vero (150 px), quattro voci, il telefono e "English". "Sottopiedi per calzature" su una riga, Commissioner 300 a 129 px, da margine a margine (72-1368). Sotto, a destra, il foglio di cartoncino largo 820 px (1,28 volte la misura che ha nella foto), senza riquadro, con un'ombra corta e morbida: i fori a forma di sottopiede sono vuoti e mostrano la carta. Sotto il foglio una sola didascalia: "Il foglio di cartoncino all'uscita del plotter Comelz CN, dopo il taglio delle sagome." In basso a sinistra la frase d'apertura e il bottone "Chiama 049 640620" con la mail. Niente legende, niente punti numerati.
- **390, prima schermata**: titolo su due righe, il foglio a tutta larghezza, la didascalia, la frase e il bottone Chiama: tutto sopra la piega (il bottone finisce a 726 px su 844).
- **Seconda schermata a 1440**: "Quattro reparti sotto lo stesso tetto" con una riga a destra, le quattro schede (1 Modelleria, 2 Taglio, 3 Cambratura, 4 Controllo), sotto la foto del reparto larga 1000 px (3:2) e a destra, allineata alla base della foto, la scheda tecnica stretta (titoletto, una riga, la macchina) sotto un filetto; sotto la foto la frase verbatim del reparto. All'arrivo è aperta Modelleria: lo stesso foglio sul plotter, nel reparto.
- Poi: la scatola di sottopiedi cambrati, larga 880 px e spinta a destra, con la didascalia; sotto, su due righe a 48 px e come h2, "Cuoio, schiuma di lattice, pelle, gommapiuma, lana, tessuto sintetico e antibatterico" e una riga con i tipi. Poi la chiusura e il piede.
- **Chiusura** ("b con foto", testo a sinistra e foto a destra fino al bordo): "Una consegna puntuale, in tempi rapidi" (da `supervisione.html`), telefono a 56 px con tel:+39049640620, info@tollin.it con mailto:, "Via Irpinia 15, Zona Artigianale, 35020 Villatora di Saonara (PD)" con il link a Google Maps. Foto: il loro furgone giallo "TOLLIN" davanti al capannone. Niente fax (va confermato), niente orari (non pubblicati). Sotto gli 860 px la foto tocca il piede.
- **Piede**: logo con una riga ("Sottopiedi per calzature da uomo, da donna e da bambino. Dal 1970, oggi in via Irpinia 15 a Villatora di Saonara."); quattro colonne (Azienda: Chi siamo, Dove siamo, Contatti; Lavorazioni; Sottopiedi; Contatti con telefono, mail e indirizzo); riga legale con "Solettificio Tollin S.r.l. dal 2011", indirizzo, P.IVA e C.F. 04574740280, REA PD 400926, capitale sociale 100.000 euro i.v., PEC; a destra English, Privacy, Cookie. A 390 le colonne vanno due per riga, in ordine. **Niente newsletter**: Tollin vende solo ai calzaturifici e non ha notizie, fiere, cataloghi né clienti privati. **Niente "Seguici"**: nessun profilo social trovato (01-analisi, sez. 8).

## Caratteri e colori, con il riferimento

- **Commissioner** (Kostas Bartsokas, Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia, file variabile servito dalla pagina (`sito/fonts/commissioner-latin.woff2`). Titoli in peso 300 con l'asse FLAR a 100, testo in 400, enfasi in 500. Riferimento: la scritta lineare con le terminazioni svasate di Edward Green e la calma di J&FJ Baker (una frase grande, molta aria). Limite: Commissioner non ha cifre tabellari; i numeri in pagina sono pochi e nessuno sta in colonna.
- **Scala a 1440**: 129 (titolo) / 60 (h2 dei reparti) / 56 (chiusura e telefono) / 48 (materiali) / 30 (frasi dei reparti) / 20 / 18 / 15 / 13.
- **Colori**: carta #F3EFE8, inchiostro #1B1A17, grigio caldo #5F5950 per note e schede non attive (6,0:1 sulla carta, 5,5:1 sul piede), carta più scura #EAE4DA solo per il piede; un accento, l'arancione della barra del menu di oggi (#E0622A) scurito a #A9461D: bottone, filetto della scheda attiva, fuoco (testo bianco sul bottone 5,9:1).

## Interazione

Un solo gesto: le quattro schede dei reparti. Bottoni veri con `aria-pressed` e `aria-controls`; il tocco o il clic cambia foto, frase e scheda tecnica con un cambio netto, senza dissolvenza; frecce, Home e Fine da tastiera. L'altezza della sezione resta ferma (1260 px a 1440) passando da una scheda all'altra. A 390 due bottoni per riga, alti 56 px. L'unica altra interazione è il bottone "Menu" sotto gli 860 px.

## Foto, origine e licenza

- **Tutte le foto in pagina sono di Tollin** (dal sito, `assets/originali/immagini/`, diritti dell'azienda). Nessuna foto di repertorio, nessuna immagine generata.
- **Apertura**: `modelleria2.jpg`. Il foglio è scontornato con una soglia sulla luminosità dentro un poligono e la pulizia dei ponticelli verso la macchina; ingrandito 3 volte con interpolazione bicubica prima della maschera, così i bordi restano netti anche a 2x; due passaggi di filtro bilaterale per pulire il cartoncino; colore quasi neutro (resta un filo del grigio freddo vero), toni rimappati senza bruciare i bianchi; ombra corta e morbida. In pagina a 820 px a 1440 (1,28x), 0,6x sul telefono.
- **Reparti, scatola, chiusura**: `modelleria1` (Modelleria), `lavorazione2` (Taglio), `cambratura3` (Cambratura), `supervisione2` (Controllo), `supervisione1` (la scatola), `supervisione3` (il furgone). Stesso trattamento: bilanciamento del bianco comune (i grigi della foto portati tutti allo stesso grigio appena caldo, che toglie la dominante verde di Cambratura e Controllo e quella gialla di Taglio), saturazione 0,9, ombre appena aperte, senza la cornice disegnata nel file, rumore JPEG tolto con OpenCV. Misure in pagina a 1440: reparti 1000 px da 802 (1,25x; Controllo da 698, 1,43x, perché la foto ha le bande nere ai lati), scatola 880 da 692 (1,27x), furgone circa 950 da 720. Nella scatola le scritte del fornitore (Tecno-Sint, Texon) sono tolte col ritocco e la striscia in basso è fuori dal taglio: a guardare da vicino il ritocco si vede, la foto va rifatta (LEGGIMI).

## Cosa è cambiato in questa rifinitura (giudizio cieco: K0 5, K1 5, K6 5, K7 6)

- **Apertura**: tolto il segnaposto Pexels (i sandali da donna di Valentin Ivantsov) e la scritta "Foto indicativa"; al loro posto il foglio di cartoncino di Tollin, scontornato. Nessun file Pexels in `sito/img`.
- **Legende tolte**: niente punti numerati, filetti e "1 Tallone, 2 Fiosso, 3 Pianta" (ricordavano l'apertura di Mario Agnoletto); una sola didascalia sotto l'oggetto.
- **1970 e Villatora**: la frase d'apertura, la riga del piede e la meta description non legano più il 1970 a Villatora di Saonara. Ora: "...li cambriamo in via Irpinia 15. Siamo nati nel 1970, come piccola realtà a conduzione familiare." (da `azienda.html`: "nasce nel 1970 come piccola realtà a conduzione familiare") e nel piede "Dal 1970, oggi in via Irpinia 15 a Villatora di Saonara."
- **Sottopiedi**: non più foto a sinistra e testo a destra; foto larga sopra, frase dei materiali sotto come h2 a 48 px; tolta l'etichetta grigia "Sottopiedi e materiali". Ora l'unica sezione con foto da un lato e testo dall'altro è la chiusura.
- **Foto dei reparti**: da 1296 a 1000 px (non più ingrandite di 1,6 volte), taglio 3:2, bilanciamento del bianco comune. La scheda tecnica sta a destra della foto, la frase sotto: sparito il vuoto di 270 px sotto la scheda attiva.
- **Sezione azienda tolta** (le due frasi da registro): "1970" e "a conduzione familiare" sono nella frase d'apertura, il 2011 della S.r.l. nella riga legale; la voce "Azienda" della testata porta ad `azienda.html`.
- **Logo**: rifatto dal ritaglio più grande (420 px) senza ingrandirlo, senza la riga piccola illeggibile, a 150 px.
- **Chiusura sotto gli 860 px**: la foto tocca il piede, niente più fascia vuota.
- **1024**: niente più legenda incollata al testo; la frase d'apertura sta in una colonna di 357 px a 17 px (circa 42 caratteri per riga); la chiusura ha il titolo a 44 px su tre righe.
- **Piede**: "English" spostato nella riga in basso accanto a Privacy e Cookie; "Contatti" nella colonna Azienda.
- Altezza a 1440 da 4875 a 4520 px.

## Controlli fatti

- Altezza: 4520 px a 1440, 3989 a 390, 4034 a 1024, 4808 a 768, 4083 a 320, 4520 a 1920. `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 480, 600, 768, 820, 900, 1024, 1100, 1280, 1440, 1600, 1920, 2560. Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440 e 1920, e le quattro schede a 1440: nessuna sovrapposizione.
- Link: i quattro telefoni (testata, bottone d'apertura, chiusura, piede) sono `tel:+39049640620`; la mail `mailto:info@tollin.it`; l'indirizzo porta a Google Maps (ricerca "Via Irpinia 15, 35020 Villatora di Saonara PD").
- Schede: con la tastiera il Tab arriva alla prima scheda e le frecce passano da una all'altra (sempre una sola visibile); col tocco a 390 Cambratura, Controllo e Modelleria si aprono; altezza della sezione ferma. Menu del telefono: si apre e si chiude col tocco.
- `segnali.sh` a 1440: 0 soglie bloccanti su 10, 0 da guardare su 8 (foto al 35,7 %, una famiglia, nessun monospazio, nessuna etichetta maiuscola, 3 misure di H2, 2 fasce di fondo).
- Nessun carattere U+2014 in pagina, negli script, nella NOTA e nel LEGGIMI. Ogni dato in pagina viene da 01-analisi.md.
- Divieti del committente: niente gradienti, niente glassmorphism, niente badge o etichette sopra i titoli, niente icone, niente comparse allo scorrere, niente effetti sul cursore; transizioni brevi solo sul colore delle schede.
