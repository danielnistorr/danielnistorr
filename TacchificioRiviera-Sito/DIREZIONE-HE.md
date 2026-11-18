# Tacchificio Riviera, direzione artistica della home HE

Scritta il 7 novembre 2026 seguendo `_metodo/highend/SISTEMA.md` (punto 3) e le lezioni dei primi tre piloti (Bottega dell'Arte 6,7, Foralberg 7,4, Ruffatti 7,5). Pagina: `sito-he/index.html`. La `sito/` di oggi non si tocca. Il committente vuole una home "più high-end, più fashion, più di design": il riferimento non è una fabbrica ma un fornitore delle maison.

## 1. La cosa vera

Il lavoro parte dal disegno di chi fa la scarpa: "Il cliente presenta un disegno con la sua idea, viene interpretata e realizzata" (sito, Ispirazioni). Lo scopo dei certificati SGS lo dice da fabbrica: "Progettazione e fabbricazione (attraverso le fasi di stampaggio ad iniezione, finissaggio ed imballaggio) di tacchi in plastica per calzature di lusso". La prova sta nella loro galleria: diciassette pezzi fotografati uno per uno sullo stesso fondo chiaro (il servizio è firmato "Copyright SHOW LUX STUDIO" nei metadati), dallo stiletto a calice nero al plexiglas, dallo sfumato viola all'ottone a losanghe che ha "RIVIERA" inciso sul piano, la faccia che va contro la scarpa. Sul loro sito c'è anche la frase che regge tutto: "Ogni forma è unica come le persone che lo indosseranno" (sezione Unico).

L'idea in una riga: **il tacco è un oggetto di moda, e si mostra come lo mostrano le maison: da solo, alla sua misura, in mezzo a molto spazio, sotto una tipografia forte.** Le foto sono piccole (800x650): la pagina non le ingrandisce mai, le mette su carta e su schede color avorio, nitide al 100%.

## 2. Riferimenti guardati

Aperti con Playwright il 7/11/2026: prima schermata a 1440x900 e a 390x844, tre scorrimenti da 900 px a 1440. Schermate in `_prova/he/riferimenti/<nome>-1440-prima-schermata.jpg`, `-1440-scorrimento-1/2/3.jpg`, `-390-prima-schermata.jpg` (script `_prova/he/script/riferimenti.mjs`). Hermès, Bottega Veneta e Jil Sander rispondono "Access Denied" o "Access is temporarily restricted" al browser di prova (le schermate del blocco sono nella stessa cartella): non li conto.

**Moda e calzatura**

1. **Manolo Blahnik** (manoloblahnik.com).
   - Mossa 1: le scarpe come still life su bianco, due per riga, con l'ombra lunga e senza cornice: l'oggetto sta da solo nel campo. Da noi: lo stiletto dell'apertura e i tacchi in legno stanno sulla carta senza riquadro, con l'ombra corta della loro foto.
   - Mossa 2: il marchio in maiuscolo leggero al centro della testata, le voci ai lati. Da noi: "TACCHIFICIO RIVIERA" spaziato al centro, le sezioni a sinistra, EN e telefono a destra.
   - Da non prendere: la barra promozionale, il carosello con le barre, il corsivo scritto a mano.
2. **Gianvito Rossi** (gianvitorossi.com).
   - Mossa 1: il prodotto su un pannello di colore accanto alla foto di campagna (lo stivale leopardato sul beige). Da noi: ogni tacco sulla sua scheda color avorio, dentro un campo pieno.
   - Mossa 2: un titolo, una riga, un bottone a filo sottile, molto vuoto intorno. Da noi: "Inviateci il disegno" come bottone pieno che si inverte di colpo, una riga di testo, niente altro.
   - Da non prendere: le frecce del carosello, i titoli in maiuscolo serif ovunque, il bollino dei cookie.
3. **Aquazzura** (aquazzura.com).
   - Mossa 1: la fila "New Arrivals": stesso pannello, stessa inquadratura, il nome piccolo sotto ogni pezzo. Da noi: la galleria delle forme, sei pezzi nella stessa finestra di 560 px, con il punto d'appoggio alla stessa altezza e due righe sotto (italiano e inglese).
   - Mossa 2: il titolo serif grande e solo prima della fila. Da noi: "Ogni forma è unica" in Melodrama prima dei pezzi, nello stesso binario.
   - Da non prendere: il popup della newsletter, le gambe delle modelle.
4. **Pierre Hardy** (pierrehardy.com).
   - Mossa 1: il dittico oggetto e materia (la scarpa sulla lana grossa). Da noi: la frase del mestiere accanto ai due tacchi in legno, uno segnato a matita rossa.
   - Mossa 2: un grottesco pulito per tutta l'interfaccia, il maiuscolo solo per il marchio. Da noi: Synonym per tutto tranne i tre momenti del display.
   - Da non prendere: la testata affollata, la barra della newsletter.
5. **Maison Ernest** (maisonernest.com), un tacchificio diventato maison, "The Parisian Heel since 1904".
   - Mossa 1: il mestiere dichiarato in una riga sopra tutto ("THE ART OF THE ARCH SINCE 1904"). Da noi: "Tacchi" e sotto "Progettiamo e produciamo tacchi per le calzature di lusso delle grandi griffe".
   - Mossa 2: ogni modello con una didascalia di mestiere (altezza in millimetri, colore, materia). Da noi: forma e materia sotto ogni pezzo; le altezze non sono nelle fonti e vanno chieste.
   - Da non prendere: la foto di campagna con la modella e l'auto, il popup.
6. **The Row** (therow.com).
   - Mossa 1: una sola immagine e nient'altro, testo minuscolo, nessun richiamo. Da noi: la prima schermata ha un oggetto e una parola.
   - Mossa 2: il piede a colonne di link piani. Da noi: piede in una riga di dati legali e una colonna di link.
   - Da non prendere: il ritratto al posto del prodotto.

**Premiati su Awwwards in settori vicini** (premi letti e verificati in `_metodo/professionale/alto/awwwards.md`)

7. **PrimeAsia** (primeasialeather.com), concerie che fanno la pelle per i marchi di calzature, Site of the Day 21/5/2025.
   - Mossa 1: il campione come oggetto su una scheda grigia, con il nome e tre righe di scheda. Da noi: il tacco sulla scheda avorio con forma, materia e la riga inglese.
   - Mossa 2: il titolo enorme e leggero (peso 300) sopra l'apertura. Da noi: "Tacchi" in Melodrama 300 a 461 px.
   - Da non prendere: il fondo WebGL, 27 MB.
8. **House of Corto** (houseofcorto.com), sedie e tavoli scultorei, Parigi, Site of the Day 3/12/2025.
   - Mossa 1: foto piccole dentro grandi pannelli di colore pieno (verde scuro). Da noi: le schede avorio dentro il campo rosso matita spento della sezione firma.
   - Mossa 2: una regola sola per la serie: stesso fondo, stesso taglio, etichetta a due voci. Da noi: stessa finestra, stessa linea d'appoggio, nome italiano a sinistra e inglese a destra.
   - Da non prendere: la tela trascinabile, il testo a 7 px.
9. (in più) **Gufram** (gufram.it), oggetti in poliuretano, Site of the Day 10/2/2025.
   - Mossa: gli oggetti scontornati che stanno direttamente sul bianco. Da noi: le foto in "moltiplica" sulla carta, così il fondo dello studio sparisce e resta il pezzo.
   - Da non prendere: la home che non dice chi sono, il trascinamento.

## 3. Carattere

- **Display: Melodrama** (Shaily Patel, Indian Type Foundry, Fontshare, ITF Free Font License 2.0), peso 300. Un serif ad alto contrasto, stretto nelle aste e con i fili sottilissimi: la stessa verticalità dello stiletto, ma più moderno di un bodoniano da rivista. Solo tre momenti: "Tacchi" nell'apertura (461 px a 1440, 133 a 390), "Ogni forma è unica" nella firma (193 px a 1440), "1945" nella storia (432 px a 1440).
- **Testo: Synonym** (Hugo Dumont, ITF, Fontshare, ITF Free Font License 2.0), 400 e 500: un grottesco umanista asciutto, per il testo, gli `h2` di servizio, la testata, le didascalie, i recapiti. Cifre proporzionali (nella pagina non ci sono tabelle).
- File woff2 ufficiali di Fontshare, ospitati dalla pagina senza modifiche (la licenza vieta sottoinsiemi e conversioni), licenza in `sito-he/fonts/FFL-ITF.txt`.
- Mai corsivo, nessuna etichetta sopra i titoli, nessun numero davanti alle fasi; il maiuscolo spaziato solo per il marchio in testata.
- Registro: riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Melodrama e Synonym non sono in nessuna home della campagna né nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`. Escono Imbue e Hanken Grotesk della versione di oggi.

## 4. Colore (dai loro materiali)

| Nome | Valore | Da dove | Dove |
|---|---|---|---|
| Carta | #F2EFEA | il fondo chiaro dello studio degli still life, scaldato | fondo della pagina; il bianco delle foto diventa questo |
| Inchiostro | #161413 | lo stiletto nero | testo, bottoni, piede; i neri delle foto finiscono qui |
| Rosso matita | #A3322A (6,0:1 sulla carta) | il segno a matita rossa sul tacco in legno | fuoco della tastiera, pressione dei bottoni, passaggio del puntatore sul numero |
| Rosso matita spento | #5C1F18 | lo stesso rosso, scurito come un cuoio | **l'unico campo pieno: la sezione firma** |
| Avorio | #EDE6D9 | il color avorio dei prototipi | le schede dei pezzi nella firma |
| Grigio | #625C56 (5,7:1 sulla carta) | | testi secondari, inglese, didascalie |

## 5. Movimento

- **Gesto d'apertura, "seguire le linee"**: la parola "Tacchi" sale (`data-he-split data-he-subito`) e lo stiletto si scopre con un taglio netto dal basso verso l'alto (`data-he-wipe="su"`), dalla punta che tocca terra al piano che regge la scarpa. "Seguire le linee" è il titolo di una sezione del loro sito: il taglio segue la linea del pezzo. Lo stiletto è alla misura nativa, sta sulla linea di base della parola, tra le due "c", e la foto è in moltiplica sulla carta: il gambo passa davanti alle lettere.
- **Sostegno 1, la sezione firma**: galleria orizzontale fissata (`data-he-horizontal`): i pezzi passano uno dopo l'altro come in una sfilata, alla loro misura. Il titolo "Ogni forma è unica" sale riga per riga (`data-he-split`, secondo e ultimo split). Sul telefono il titolo resta fermo sopra (sticky) e i pezzi si sfogliano col dito sotto, il primo già in vista; con "riduci movimento" sullo schermo grande i pezzi vanno a capo in tre colonne.
- **Sostegno 2, la mano**: la foto dell'incisione si scopre da sinistra (`data-he-wipe="sinistra"`), una volta.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con "Chiama".
- Niente scala, parallasse, indice, racconto con foto ferma, prima e dopo, sipario. Gli altri cambi di ritmo li fanno la scala (la parola a 461 px, l'anno a 432, le schede a 560) e l'impaginazione.
- Una eccezione al kit, nella pagina: la galleria fissata usa `pinType: "transform"` (impostato prima di `he.js`), perché il fissaggio con `position: fixed` spostava il layout di 1,0 all'inizio e alla fine (CLS misurato 1,99, ora 0).

## 6. Ritmo (ogni sezione ha uno scheletro diverso)

1. **Apertura, "Tacchi"** (carta, a tutta altezza): la parola a tutta larghezza, lo stiletto in piedi sulla linea di base tra le due "c"; in basso tre colonne: il mestiere in italiano, "Inviateci il disegno", il mestiere in inglese. Didascalia da museo accanto al calice.
2. **Il mestiere** (carta): la frase del cliente in grande (Synonym 500, 52 px) su dieci colonne con l'inglese sotto; poi, sfalsati, i due tacchi in legno alla misura nativa a sinistra e a destra le cinque fasi verificate con lo scopo SGS tra virgolette e i PDF ISO 14001 e 45001.
3. **Firma, "Ogni forma è unica"** (rosso matita spento, l'unico campo pieno): binario orizzontale fissato con il titolo in Melodrama e sei pezzi su schede avorio da 560 px (nero opaco, sfumato viola, plexiglas, avorio, anima metallica, ottone), ognuno con forma e materia; in fondo il nome inciso sul piano dell'ottone.
4. **Seguire le linee** (carta): colonna di testo stretta in basso a sinistra, la foto in bianco e nero della mano che incide un fiore a destra, 840x630, che si scopre da sinistra.
5. **1945** (carta): l'anno a 432 px a sinistra, il testo della fondazione a destra sulla linea di base; due foto d'archivio sfalsate di misura diversa; 1970 e la frase sulle griffe.
6. **Inviateci il disegno** (carta, filetto nero sopra): il telefono grande, email, sede con la mappa, fax e PEC a sinistra; "Writing from abroad" in inglese a destra con l'email già intestata in inglese.
7. **Piede** (inchiostro): timbro chiaro con la firma Valentino Boldrin, dati legali, nota sui cookie, Privacy, Cookie, whistleblowing, English.

La sezione firma è la 3: un'idea (ogni forma è unica, la loro frase) con la prova fotografica (sei pezzi veri della loro galleria, alla misura della foto, dall'avorio all'ottone con il nome inciso), non il logo ingrandito.

## 7. Foto

Riscaricate il 7/11/2026 da tacchificioriviera.it in `assets/originali/` (fuori da git): i 17 still life della galleria (`nascita/tacco_N.jpg`, provati i numeri da 1 a 40: esistono solo i 17 della pagina), gli sfondi delle sezioni (desktop 1920x1080, tablet 1024x1024, telefono 650x650; home, territorio, unico e certificazioni desktop rispondono 404), le tre foto della storia (`territorio/modal1-3.jpg`), le otto miniature del menu e il logo. Cercate e non trovate: varianti senza misura o più grandi (`-big`, `_large`, `@2x`, `-hd`, `.png`, cartelle `big/`, `original/`, `hd/`), indici delle cartelle (404), file diversi nella versione inglese (`/en/app/...` restituisce la pagina, non le foto). **Nessun originale più grande di quelli già noti**: still life 800x650 (JPEG qualità 86, buoni), sfondi 1920x1080 (JPEG qualità 28), archivio 488x562 e 876x704.

Trattamento unico (`_prova/he/script/immagini.py`): gli still life a colore, con il campo piatto (un polinomio di terzo grado stima la luce del fondo e la toglie: il fondo diventa bianco puro, l'ombra corta resta), neri portati all'inchiostro, in moltiplica sulla carta o sull'avorio; le foto di mani e d'archivio in bianco e nero con la stessa curva (nero inchiostro, bianco carta) e la stessa grana fine, che copre anche i blocchi del JPEG molto compresso. Nessuna foto ingrandita: tutte a 1,0 della misura nativa o ridotte.
