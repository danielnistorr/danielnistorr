# Home di B.C.M. Enologia: nota

## Alto livello, prova della sezione D (3/11/2026)

Pagina: `sito/index.html`, riscritta da capo secondo `_prova/alto/DIREZIONE.md` e la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`. La home di prima (livello professionale con il ritocco finale) è copiata com'era in `_prova/versione-pro/` (sito intero e screenshot); la sua nota resta qui sotto come storia.

Rifare tutto: `python3 -I _prova/alto/script/pro_img.py` (immagini), `node _prova/alto/shots.mjs` (screenshot all'ora simulata lunedì 2 novembre 2026 alle 10), `node _prova/alto/misura-d.mjs` (soglie D, risultati in `_prova/alto/misura-d.json`). Le miniature della zona a 300 px per la prova D1 sono in `_prova/alto/miniature-zona.jpg`.

Screenshot (stessi nomi, più due): `home-1440.jpg` (5.903 px dopo il ritocco), `home-1440-prima-schermata.jpg`, `home-390.jpg` (7.942 px), `home-390-prima-schermata.jpg`, `home-1024-prima-schermata.jpg`, `home-768-prima-schermata.jpg`, `chiusura-1440.jpg` (cataloghi e piede). Guardati a pezzi a 1440 e 390, e a 320, 768, 1024 e 1920, accanto a Scharfenberger e Krampe (`alto/M2/`) e al foglio dei 12 migliori.

### Ritocco dopo il giudice da agenzia (voto 7, 3/11/2026)

Il giudice ha dato 7 (prima 5,5) per tre ragioni: il mestiere non si capisce dalla foto, sotto la piega il carattere sparisce e ogni sezione ha una griglia sua, il culmine non culmina. La versione prima del ritocco è in `_prova/alto/rit/index-prima.html` e `rit/pro_img-prima.py`. Le prove dei clienti tipo rifatte sulla pagina nuova sono in `_prova/alto/rit/prova-1/` e `rit/prova-2/`. Il controllo della griglia è `_prova/alto/rit/griglia.mjs`. Le tabelle qui sotto riportano i valori di prima del ritocco. Quelli nuovi sono in fondo a questa parte.

**Applicati**
- **Apertura, foto (bloccante)**: al posto delle basi rosse (`wa0002`) c'è `wa0000`, i torchi con la gabbia in faggio e il martinetto DAVID montato sulla vite. È la variante proposta dal giudice: nome e oggetto coincidono e il mestiere si legge a 300 px. Il taglio 16:9 va da y 290 a 1370, così resta fuori la striscia chiara del pavimento. Il taglio 3:4 per il telefono è di 1020x1360 (x 330-1350) e i file sono `apertura-m-780` e `-1020`. Al posto della passata uniforme c'è un velo dentro la foto, in luce lineare: più scuro in alto, sotto DAVID, e in basso a sinistra, sotto il titolo. Non è un livello sopra la foto. I cartoni in alto restano nella fascia scura.
- **Apertura, riga (bloccante)**: "Torchi, martinetti DAVID, pompe e pigiatrici per l'enologia. Saonara, dal 1960." Le parole "per l'enologia" vengono dal loro h2. "Pigiatrici" risponde alla prova T2 del cliente tipo: pompe e pigiatrici senza scorrere, che ora passa. Per restare nei 160 caratteri la didascalia dell'apertura è tolta, e data e soggetto stanno nell'`alt`. Così sparisce anche l'etichetta ghisa che usciva di 8 px dalla colonna (minore del giudice). Caratteri: 147.
- **Culmine (importante)**: l'h2 è la frase-firma "Compatibilità con il passato", a 44/48 500, senza punto e uguale all'h1. Il paragrafo a 44 px sotto l'h2 da 30 è tolto. L'occhiello è "Martinetto DAVID, brevettato negli anni 80" (uno solo, con la cifra). Le sigle A-50...E-90 della tabella sono in Saira Extra Condensed 600: è il ritorno del gesto. Il culmine ha un suo fondo, `#E7E2D8`, e il torchio sta su quel fondo con `multiply`. È il secondo fondo della pagina oltre al piede (D11: al massimo 3).
- **Griglia unica (importante)**: 12 colonne con spazio di 32 px (`.g`, `.sx`, `.dx`). In Ricambi, culmine, officina, cataloghi e piede la seconda colonna parte dalla colonna 7: x 736 a 1440, 528 a 1024, 976 a 1920, misurato con `griglia.mjs`. Voci delle macchine, serie dell'officina e indice stanno sulle stesse 3 colonne (x 56, 509, 963). Tutte le sezioni si aprono allo stesso modo: titolo in alto a sinistra, contenuto allineato in alto.
- **Culmine a 1024 (importante)**: con la griglia unica la colonna del testo è larga 456 px, contro i 272 di prima. La foto ha `max-width:600px` e `sizes` corretti, e a nessuna larghezza tra 320 e 1920 c'è un'immagine ingrandita.
- **Le macchine (importante)**: la fila delle 4 tessere è tolta. Ora c'è una griglia sola di 6 voci con uno scontornato sopra ogni nome: torchio a cricco, martinetto DAVID con la targhetta, gabbia in faggio, Volumex, pompa automatizzata e pigiadiraspatrice. Le tessere sono rifatte in `pro_img.py` in 3:2 (900x600): l'oggetto è alto l'80% della tessera, la base sta all'8,3% dal fondo (24 px a 1440) e l'oggetto è allineato a sinistra sul bordo del nome. Misurato: le basi sono alla stessa y in ogni fila e il left dell'immagine è uguale a quello del nome. Al telefono ogni voce ha lo scontornato a 112 px a sinistra e il testo accanto.
- **Contatto per bisogno (D12, non passava)**: la sezione Ricambi ha a destra "Per le altre richieste", con due strade: "Preventivo per una macchina nuova" (email con l'oggetto e la traccia) e "Rivenditori ed estero" ("Spediamo in tutto il mondo. Per maggiori informazioni contattaci direttamente.", parole loro, con l'email e il link ai cataloghi). Ognuna ha lo stesso numero e lo stesso orario. Nomi e interni diversi non ci sono nelle fonti e non sono inventati. Non è aggiunto nessun link `tel:` (restano 3). La riga "Spediamo in tutto il mondo" esce dai cataloghi. La prova T3 (rivenditori) ora passa.
- **Foto, una serie sola (D10)**: dopo il trattamento comune, le quattro foto d'officina (banchi, martinetti, gabbie, pompe) vanno sulla stessa media di colore e di luce con un guadagno per canale (`allinea` in `pro_img.py`). Le gabbie non sono più calde e le pompe non sono più blu. Le foto sono 12, in 3 formati (16:9, 3:4, 3:2). Il martinetto in Ricambi è diventato la voce 02.
- **Una sola numerazione (minore)**: "01" a due cifre, colore secondario, 600, su una colonna di 40 px, sia nelle tre cose da mandare sia nell'indice. Le misure dei titoli sono due, 44 e 30 px.
- **Unità (D9)**: "Idraulici con la gabbia da 45 a 90 cm, a cricco da 15 a 80 cm", "con il variatore da 0 a 950 hl/ora", "per le viti da 45 a 100 mm".
- **Nota orfana**: "In azienda, giugno 2022" sotto la serie è tolta.
- **Controlli**: in `misura-d.mjs` la didascalia d'apertura si salta se non c'è (prima lo script si fermava).

**Respinti, con il motivo**
- **Sigle del DAVID a 56/56 px** (giudice): a 56 px sarebbero 5 elementi numerici di 30 px o più, e D9 ne ammette 1 (c'è già l'h2 "nasce nel 1960"). Le sigle sono in Saira a 28/32: il carattere torna, ma la scala resta sotto la soglia.
- **Taglio di `wa0002` da y 360** (giudice, prima strada): non serve più, perché la seconda strada che indicava il giudice, `wa0000`, risolve anche il mestiere.
- **Stato "Aperto ora" e orario nella prima schermata** (prova 1, telefono): resterebbe il servizio in apertura, contro D3 e D12. Dopo un tocco sul bottone o su "Ricambi" nel menu, stato, telefono ed email sono nella stessa schermata (verificato in `rit/prova-1`).
- **Link ai PDF dentro le voci delle macchine e tutta la gamma in una schermata** (prova 2, T1 e T5): i PDF sono a un clic dalla voce "Cataloghi IT DE EN FR" in testata, e le 6 voci con la scheda stanno nelle due schermate dopo il clic su "Macchine". Un link PDF per voce riporterebbe i 99 link di prima.
- **Servizio fotografico**: resta il limite sopra l'8. La foto d'apertura è ancora uno scatto WhatsApp del 2022, morbido su retina.

**Valori dopo il ritocco** (`misura-d.mjs`, tutti PASSA): 6 cliccabili, 1 bottone e 147 caratteri a 1440; 4 cliccabili e 1 bottone a 390; foto al 90% (1440) e al 62% (390). Famiglie 2, un solo elemento sopra i 100 px. 573 parole, 5 sezioni, 2 bottoni. Altezza 5.903 px a 1440 e 7.942 a 390, culmine 1.152 px. 1 numero di 30 px o più. 12 foto in 3 formati. Fondi: carta, carta del culmine e ghisa del piede. Spazi tra le sezioni di 112 e 176 px. 3 `tel:` e 4 `mailto` con l'oggetto. Peso 404 kB a 1440 e 379 kB a 390. Contrasto sul punto più chiaro: DAVID 3,44:1, h1 4,57:1 e riga 4,87:1 a 1440. Nessuno scorrimento orizzontale e nessuna sovrapposizione tra 320 e 1920. 0 U+2014.

### Che cosa è cambiato

- **Idea e gesto (D1)**: la parola DAVID, il loro marchio registrato, a 220 px color carta sopra la foto vera delle basi rosse dei torchi in fila, ognuna con la sua vite (`wa0002`, giugno 2022). Il titolo è la frase della loro brochure, "Compatibilità con il passato", che torna uguale nel culmine. Sotto, "Torchi, martinetti e pompe. Saonara, dal 1960." e un solo bottone, "Ricambi? Mandaci una foto". Modello N (il nome sopra la foto di serie).
- **Prima schermata**: da 22 a 6 cliccabili, da 3 a 1 bottone, da 673 a 152 caratteri, la foto dal 32 al 90%. Il telefono è un link di testo rosso in testata, fisso. Il menu passa da 6 voci più "Catalogues" e il bottone a 3 voci: Macchine, Cataloghi IT DE EN FR, Contatti. Al telefono la voce "Menu" è un `details`, quindi si apre anche senza JavaScript.
- **Cinque sezioni** al posto di nove: Ricambi (l'unica sezione contatti: le tre cose da mandare, il telefono con lo stato "Aperto ora" e l'email con l'oggetto e la traccia), il culmine sul DAVID (il torchio 60 del catalogo a 600x800 con la tabella "Quale DAVID per il tuo torchio" in testo), Le macchine (4 tessere scontornate con il solo nome e un indice 01-06 con una frase di misure ciascuna), L'officina (i banchi con i corpi in ghisa, tre frasi del loro chi-siamo, la serie di tre foto 3:2), Cataloghi (quattro righe, le lingue, la spedizione nel mondo). Il piede è il biglietto da visita, con "Apri la mappa" e i dati legali.
- **Tolto dalla home**: l'occhiello maiuscolo e il titolo-elenco dell'apertura, il secondo bottone, la fila degli 8 ingressi, gli 8 scontornati con i due link e il peso dei PDF, la tabella del torchio idraulico, la fascia rossa delle 4 cifre a 128 px, i 4 riquadri dei cataloghi con il peso, le 10 brochure ZIP, i 4 rivenditori con il testo in 4 lingue, la riga dei SIMEI, la linea del tempo con le cifre grandi (e il 2012, da confermare), il modulo "Scrivici" e le ripetizioni di indirizzo e orari. I link `tel:` passano da 9 a 3, i bottoni da 6 a 2, le parole da 1.351 a 534.
- **Caratteri (D5)**: Saira Extra Condensed 600 solo per DAVID; Source Sans 3 (400-600) per tutto il resto, testo a 18/28 (17/26 al telefono), titolo a 44/48 peso 500. Tolti Sofia Sans e Sofia Sans Condensed (già in 4 home). Saira arriva a 2 home su 45 (TreEmme usa Saira, fuori zona), Source Sans 3 è in questa sola.
- **Colori**: un solo fondo, la carta `#F3F0EA`; ghisa `#1D1E20` per il testo e il piede; il rosso dei cerchi `#9E2B22` solo nel bottone, nel telefono, nel punto dello stato, nei numeri dell'elenco e nel filetto della tabella. Nessuna fascia di colore.
- **Foto (D10)**: 11, in 3 formati (16:9, 3:4, 3:2), tutte con lo stesso trattamento in `pro_img.py` (verso il neutro sui pixel quasi grigi, contrasto +6%, neri alzati di 4 livelli, saturazione 0,88, una sfocatura di 0,45 px contro il rumore WhatsApp sulle foto d'officina, nessuna nitidezza). L'apertura è scurita in modo uniforme, senza sfumature, a un quarto della luce (2 stop): mezzo stop, come nella direzione, lasciava DAVID a 1,5:1 sul muro chiaro. Il torchio 60 viene dal catalogo PDF (2362x3149 dopo il taglio, in pagina 600x800 con `multiply` sulla carta). Il martinetto è ritagliato sul pezzo e messo al centro del 3:2.
- **Didascalie**: due voci solo sull'apertura ("Basi dei torchi con la vite / giugno 2022"), su un'etichetta ghisa piena perché a 14 px sopra i riflessi dei piatti arrivava a 2,5:1; i soli nomi sotto la serie e sotto il martinetto, più "In azienda, giugno 2022". Non c'è scritto "DAVID" sotto le foto d'officina.

### Esito regola per regola (misure di `misura-d.mjs`, prima: `alto/diagnosi/misure/nostre-*.json`)

| Regola | Prima | Dopo | Esito |
|---|---|---|---|
| D1 idea e gesto | nessun gesto proprio; schema "titolo a sinistra, foto a destra" | DAVID a 220 px sulla foto di serie; nelle miniature della zona (`miniature-zona.jpg`) non somiglia a nessuna delle cinque | passa per la parte misurabile; la prova con tre persone non è fatta |
| D2 foto in prima schermata 1440 | 32% (576x720, file di 624 px) | 90% geometrica, 74% a campioni (il testo sopra la foto toglie i punti), file di 1440 o 1920 px | passa |
| D2 foto e gesto a 390 | 27% | 62% geometrica, 51% a campioni | passa |
| D2 nessuna foto ingrandita | (non misurato) | scala resa al massimo 1 a 320, 390, 768, 1024, 1440 e 1920, anche con `object-fit: cover`, sui pixel veri del file scelto dal `srcset` | passa |
| D3 cliccabili 1440 | 22 | 6 (logo, 3 voci, telefono, bottone) | passa |
| D3 bottoni 1440 | 3 | 1 | passa |
| D3 caratteri fuori dal menu 1440 | 673 (tutto compreso) | 152, più 36 del menu | passa |
| D3 fila di ingressi | 8 | 0 | passa |
| D3 cifre di 30 px o più | 0 in prima schermata, 7 in pagina | 0 | passa |
| D3 a 390 | 9 cliccabili, 4 bottoni | 4 (logo, telefono, Menu, bottone), 1 bottone | passa |
| D4 distanza del titolo | 80 px, come 27 home su 31 | 56 px; modello N, secondo e ultimo N della zona dopo Overdrive | passa |
| D5 famiglie | 2 (Sofia Sans, già in 4 home) | 2 (Source Sans 3, Saira Extra Condensed) | passa |
| D5 elementi oltre 100 px | 4 cifre a 128 px | 1, DAVID | passa |
| D5 testo corrente | 18 e 16 px | 18 px a 1440, 17 a 390 | passa |
| D6 occhielli | 13 maiuscoli spaziati, occhiello sopra l'h1 e sopra 5 h2 su 7 | 1, "Brevettato negli anni 80", sopra l'h2 del culmine | passa |
| D7 h1 | "Torchi, martinetti DAVID e pompe, dal 1960", 7 parole, 1 virgola | "Compatibilità con il passato", 4 parole, nessuna virgola | passa |
| D7 lista nera | "leader" nel loro sito | 0 | passa |
| D7 testo d'interfaccia | in vista in più punti, sopra i 14 px | una riga sola, a 14 px accanto al bottone email | passa |
| D7 frase-firma | nessuna | 2 volte, h1 e culmine, Source Sans 3 500 a 44 px tutte e due (più il `<title>`) | passa |
| D8 parole | 1.351 | 534 (528 a 390) | passa |
| D8 sezioni | 8-9 | 5 | passa |
| D8 bottoni in pagina | 6 (7 a 390) | 2 | passa |
| D8 altezza a 1440 | 9.328 px | 5.881 px (8.232 a 390) | passa |
| D8 culmine | nessuno | sezione DAVID alta 1.153 px | passa |
| D9 numeri di 30 px o più | 7 | 1, l'h2 "La ditta BCM nasce nel 1960" (30 px, la cifra è nella frase) | passa |
| D9 peso dei PDF in pagina | 24 pesi in MB nel sorgente | 0 (il peso resta nel `title` dei link) | passa |
| D10 foto | 13 | 11 | passa |
| D10 formati | 3 | 3 (16:9, 3:2, 3:4) | passa |
| D10 "indicativ" | 0 | 0 | passa |
| D11 fondi oltre al piede | 4 | 1 (carta) | passa |
| D11 sezioni con il colore del marchio | 1 (fascia rossa) | 0 | passa |
| D11 spazi tra le sezioni | un valore, 120 px | 112 e 176 px (1,57 volte, il culmine); 72 e 112 a 390 | passa |
| D12 link `tel:` | 9 | 3 (testata, ricambi, piede), tutti `tel:+39049640372` | passa |
| D12 "Apri la mappa" | 2 | 1, nel piede | passa |
| D12 telefono grande e modulo | tutti e due | nessuno dei due | passa |
| D12 contatto per bisogno | contatto unico | non passa del tutto: c'è una strada sola con telefono, orario ed email (i ricambi). Le altre (rivenditori, preventivi) non hanno un numero o una persona propri nelle fonti | in parte |
| Peso della pagina | cartella da 1,4 MB | 436 kB a 1440, 401 kB a 390 (HTML, 2 caratteri, 13 immagini) | passa |
| Contrasto sull'apertura (punto più chiaro dietro le lettere, 99,5° percentile) | | 1440: DAVID 3,76:1, h1 4,97:1, riga 4,96:1, didascalia 14,7:1. 390: DAVID 4,17:1, h1 e riga su carta 16,7:1 | passa AA (testo grande 3:1, normale 4,5:1); DAVID resta sotto il 4,5:1 chiesto dalla direzione, vedi sotto |
| Larghezze 320-1920 | | nessuno scorrimento orizzontale, nessuna sovrapposizione di testo, nessun errore di script; il telefono in testata è toccabile a metà pagina (44 px) | passa |
| U+2014 | 0 | 0 | passa |

### Quello che non passa o resta aperto

- **DAVID a 4,5:1**: la direzione lo chiedeva sul punto più chiaro dietro le lettere. Sopra il muro di cemento e le viti zincate arriva a 3,76:1 (5,66:1 in mediana): è testo di 220 px, per cui l'AA chiede 3:1. Per arrivare a 4,5:1 la foto andrebbe scurita di un altro stop, e i piatti rossi diventerebbero marroni.
- **Prova D1 con tre persone**: non fatta. Le miniature a 300 px senza logo, con BCM di prima e le cinque home vicine della zona, sono in `_prova/alto/miniature-zona.jpg`.
- **Contatto diviso per bisogno (D12)**: le fonti non danno nomi, interni o orari diversi per ricambi, preventivi e rivenditori. In pagina c'è una strada sola, quella dei ricambi.
- **Persone con il nome**: ci sono i fondatori (Marino Benetazzo e Mario Camerotto) nel testo, ma nessuna foto di persone. Il servizio fotografico resta il limite per salire sopra l'8 (LEGGIMI).
- **Foto d'apertura**: è uno scatto WhatsApp del 2022. A 1440 la compressione si vede nelle viti al 100%; scurita e alla sua misura regge, ma è la foto da rifare per prima.
- **Pagine che la home dà per scontate**: Ricambi e assistenza con il modulo, Misure (la tabella del torchio idraulico), Download con le 10 brochure, Dove trovare le macchine BCM (solo dopo il permesso dei rivenditori). Oggi i link portano alle pagine del sito attuale o alle sezioni della home. Il link ai rivenditori non c'è.

### Caratteri e licenze

Saira Extra Condensed 600 (The Saira Project Authors, Omnibus-Type) e Source Sans 3 variabile 400-600 (Paul D. Hunt, Adobe), entrambe SIL Open Font License 1.1, WOFF2 solo latin in `sito/fonts/` con `OFL-Saira-Extra-Condensed.txt` e `OFL-Source-Sans-3.txt`. Tolti Sofia Sans e Sofia Sans Condensed.

---

## Prima della sezione D (livello professionale)

## Ritocco finale (dopo il controllore del livello professionale, voto 6)

Pagina: `sito/index.html`. La versione prima del ritocco è descritta qui sotto ("Livello professionale"). Le modifiche sono negli script `_prova/script/ritocco_css.py` e `ritocco_html.py` (sostituzioni puntuali, già applicate), le immagini si rifanno con `pro_img.py`, i controlli con `pro_controlli.mjs`: **65 su 66 passano**, non passa solo la regola 11 (lavori con il nome, che non ci sono nelle fonti).

Screenshot rifatti (stessi nomi, ora simulata lunedì 2 novembre 2026 alle 10): `home-1440.jpg` (9.328 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13.420 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Guardati a pezzi a 1440 e 390, e a 320, 768, 1024, 1280 e 1920: nessuno scorrimento orizzontale (anche le tabelle a 320 ora stanno nella colonna), nessuna sovrapposizione.

### Che cosa è cambiato

- **Apertura**: la foto dei torchi in magazzino non è più un quadrato con gli angoli arrotondati dentro la colonna. È tagliata in 4:5 sul torchio centrale e sui martinetti (980x1225 nativi), a filo del bordo destro della pagina e alta quanto la prima schermata meno testata e indice (720 px a 1440x900, al massimo 780). La fascia bianca in basso e parte degli scatoloni restano fuori; nel LEGGIMI resta la richiesta dello scatto nuovo. Occhiello "Macchine enologiche e ricambi a Saonara, Padova", la promessa dei ricambi in grassetto nella riga sotto il titolo, due PDF diretti sotto i bottoni (torchi 1,9 MB, pompe con inverter 2,3 MB, "IT DE EN FR") e "Tutti i cataloghi".
- **Gesto di scala**: la fascia rossa ha quattro cifre su una riga a 128 px (1960, 30+, 400, 950), quasi il doppio del titolo (68 px), con l'etichetta di 18 px sotto. Tolti "8 modelli" e "4 lingue", deboli.
- **Foto in serie**: tolta l'ombra a terra disegnata dagli scontornati, che ora stanno sullo stesso piano grigio #E6E5E2. Le due foto d'officina (magazzino e banco) hanno lo stesso trattamento (`grade` in `pro_img.py`): bilanciamento del bianco sui pixel quasi grigi, la stessa tinta calda, la stessa curva e lo stesso colore. Il banco non è più grigio-verde e il magazzino è meno arancio. Il martinetto dei ricambi è nello stesso quadrato delle schede.
- **Ricambi**: dopo il titolo, una riga con i pezzi (manometro del DAVID, listelli e cerchi della gabbia, tappi e mezzelune, girante della pompa); i tre passi; subito dopo la foto della targhetta con la didascalia (al telefono piccola, accanto alla didascalia); poi Chiama e "Manda le foto per email". Tolta la formula "Siamo sempre a tua disposizione"; al suo posto "Fuori orario puoi mandarci le foto per email... allegale dalla galleria". Punto 1: "Se non si legge, una foto intera della macchina".
- **Fuori orario**: quando lo stato è "Chiuso", sotto compare "Fuori orario? Mandaci le foto della targhetta per email" (mailto dei ricambi), nella prima schermata a 390. Lo script ha un elenco `chiusure` per ferie e ponti (oggi vuoto, da far confermare a BCM): in quei giorni dice "Chiusi per ferie, riapriamo il ...".
- **Rivenditori**: la fascia "Dove trovi le macchine BCM" nei cataloghi, a 4 colonne, con i quattro rivenditori delle fonti (Vivi in Campagna e Enologys in Italia, Kidonakis ad Atene, KOL-Technik in Austria), poi quattro colonne per rivenditori e importatori in italiano, inglese, tedesco e francese (email con l'oggetto nella lingua, telefono +39 cliccabile, orari), poi la riga dei titoli: DAVID marchio registrato e i quattro SIMEI con le foto degli stand (tolta dal "Chi siamo" per non ripeterla).
- **Brochure ZIP**: in un `details` "Le 10 brochure delle linee, in ZIP", aperto sui monitor e chiuso al telefono; i link ZIP hanno `download`, i PDF `target="_blank"`.
- **Contatti**: "Come si compra" spostato nella colonna dei recapiti, che non ha più il vuoto di 449 px sotto lo stato; il numero grande e quello del piede sono "+39 049 640372".
- **Modulo**: "Macchina e modello" e "Quantità" sulla stessa riga, l'allegato vero (`input type="file"`, JPEG, PNG o PDF, più file) e la nota "Le foto non partono da sole: il modulo apre un'email, allegale lì". Il corpo dell'email scrive i nomi dei file scelti; dopo l'invio compare "Si è aperta l'email: ricordati di allegare le foto". Con "Sono un rivenditore" il campo diventa "Paese e linee che ti interessano", l'allegato sparisce e l'oggetto è "Rivenditori: listino e condizioni, <azienda>".
- **Tono**: "Siamo nati nel 1960 con i soci...", "l'anno in cui siamo nati", "Nasce la nostra ditta". Nessuna frase in terza persona su BCM (controllato).
- **Misure del testo**: descrizioni delle schede, cataloghi, tabelle e date a 18 px a 1440 (16 px al telefono). Nessuna misura nuova: a 1440 sono 128, 68, 44, 26, 20, 18, 16, 14; a 390 72, 38, 30, 22, 18, 17, 16, 14.

### Esito regola per regola dopo il ritocco

1. **Telefono in testata fissa**: PASSA. A 390, al 50% della pagina, il bottone "049 640372" è a 12 px dall'alto, 125x48, toccabile; 9 link `tel:`, tutti +39049640372.
2. **Prima schermata**: PASSA a 1440x900 e 390x844: mestiere in H1, Saonara nell'occhiello, "dal 1960", "Aperto ora", "Chiama 049 640372" pieno (350 px a tutta larghezza a 390).
3. **Immagine vera in apertura**: PASSA. I torchi BCM in magazzino, ora a filo del bordo in 4:5, alta 720 px. Riserva: è uno scatto da telefono (vedi LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" 0, nessuna foto di banche, nessuna illustrazione.
5. **Foto in serie**: PASSA, con un limite più piccolo di prima. Tre formati a 1440 (4:5, 1:1, 16:9), due a 390; 2 didascalie su 11 foto. Ombre disegnate tolte, stesso piano per gli scontornati, stesso trattamento per le due foto d'officina. Il limite resta: scatti di telefono e scatti da catalogo, non una giornata di un solo fotografo.
6. **Palette dal marchio**: PASSA. Rosso #9E2B22 e ghisa #1F1E1C, verde solo per lo stato, più i neutri (bianco, due grigi freddi, testo secondario, filo, chiaro).
7. **Scala corta**: PASSA. 8 misure a 1440 e 8 a 390; testo corrente 18 e 17 px; niente sotto i 14 px; H1 68 e 38 px.
8. **Due famiglie**: PASSA. Sofia Sans Condensed (titoli, cifre, nomi dei rivenditori) e Sofia Sans (testo e interfaccia).
9. **Schede con la foto**: PASSA. Otto schede in 4 colonne, stesso quadrato 1:1, nome, scheda della linea e PDF o ZIP. Riserva: sono scontornati del catalogo, non foto del lavoro.
10. **Tre tipi di prove**: PASSA IN PARTE. Numeri: 4 cifre grandi. Clienti e collaborazioni con il nome: i 4 rivenditori in una fascia con il titolo "Dove trovi le macchine BCM". Al posto delle certificazioni, che non hanno: la riga dei titoli (DAVID marchio registrato, SIMEI 2009-2019). Recensioni: nessuna nelle fonti, non inventate.
11. **Lavori con il nome**: NON PASSA. Nessuna cantina nominata nelle fonti; nulla inventato, richiesta nel LEGGIMI.
12. **Ritmo a blocchi**: PASSA. Ghisa (ricambi) e rosso (numeri) oltre al piede, grigi per indice, misure e chi siamo; 120 px tra le sezioni a 1440, 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno rosso e con il bordo, raggio 4 px, 52 px (48 in testata e nelle caselle del modulo), testo 16 e 18 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando"**: PASSA. Tipo di richiesta, macchina e modello, quantità, allegato (foto della targhetta e del pezzo), nome, azienda, email, telefono, messaggio; compone un mailto (da collegare a un servizio, LEGGIMI). Indirizzo con "Apri la mappa", tabella degli orari, nessun iframe.
15. **Piede completo**: PASSA. Ragione sociale, P.IVA e C.F., REA, capitale, sede con la mappa, +39 049 640372 ed email cliccabili, orari, le linee, Privacy e Cookie, 4 colonne, testo da 14 px. Certificazioni: non ne hanno.

### Prove d'uso della SCHEDA dopo il ritocco

- **A, ricambio al telefono**: nella prima schermata "ricambi" è nell'occhiello e in grassetto nella riga sotto il titolo, con lo stato, Chiama e "Ricambi e assistenza"; fuori orario c'è anche la riga per mandare le foto per email. Un tocco su "Ricambi e assistenza" porta a titolo, pezzi e passi; con mezzo scorrimento si vedono la targhetta d'esempio e poi i bottoni (prima la foto stava dopo i bottoni). Il tempo è lo stesso, ma chi scrive ha visto che cosa fotografare.
- **B, rivenditore a 1440**: il PDF giusto ora si scarica in un clic dalla prima schermata (torchi e pompe con inverter) o dalle schede, in una scheda nuova; "Catalogues EN · DE · FR" porta ai cataloghi e, subito sotto, alla fascia dei rivenditori con una colonna per lingua; il modulo da rivenditore non chiede più le foto.
- **C, scelta**: invariata (indice delle linee, tabelle, "Quale DAVID per il tuo torchio", come si compra ora nei contatti, "Apri la mappa").

### Respinti, con il motivo

- **Scheda propria per l'inverter universale**: una nona scheda romperebbe la griglia 4x2. La pagina della linea sul sito ha un solo prodotto e il suo indirizzo rimanda (301) a quel prodotto (`41-filocontrollo-14`): il link del piede porta quindi al posto giusto. Lo ZIP dell'inverter universale è nelle brochure. Da rivedere quando ci sarà la pagina nuova della linea.
- **Siti dei rivenditori e "da confermare con BCM" nella didascalia**: i siti non sono nelle fonti e una scritta "da confermare" in pagina è un segnaposto; la conferma è nel LEGGIMI.
- **Tempo di risposta ("rispondiamo in giornata")** e **guarnizioni** tra i pezzi: non sono nelle fonti.
- **Dove sta la targhetta su torchio e pompa**: non è nelle fonti; c'è "Se non si legge, una foto intera della macchina".
- **Misure e cataloghi richiudibili al telefono**: le tabelle servono alla scelta del DAVID (prova C) e i cataloghi al rivenditore; si chiude solo l'elenco degli ZIP. La pagina a 390 resta lunga (13.420 px), per la fascia dei rivenditori nelle quattro lingue.
- **"1960" a 240 px nel Chi siamo**: basta un gesto di scala, quello della fascia rossa.

### Caratteri e licenze

Invariati: Sofia Sans e Sofia Sans Condensed (Lettersoup, Google Fonts, SIL Open Font License 1.1), serviti da `sito/fonts/`, pesi 400 e 700.

---


## Livello professionale (prima del ritocco finale)

Pagina: `sito/index.html` (statica, si apre con file:///). La versione di prima ("Il torchio" sulla carta, con il selettore del diametro) è copiata in `_prova/versione-1-originale/` (sito, screenshot, LEGGIMI). Per BCM non c'era una "versione 1 con l'uso" separata: le prove d'uso della SCHEDA (`_prova/uso/SCHEDA.md`, paragrafo 8) sono state risolte in questo stesso passaggio e sono tra i controlli.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia M (manifattura), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (foglio `riferimenti.jpg`, più Cly-Del, barth, Odermatt, Kline e Wilson a 390), le pagine intere di Cly-Del e barth a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shots.mjs` all'ora simulata lunedì 2 novembre 2026 alle 10, controlli con `pro_controlli.mjs`: 60 su 61 passano, quello che non passa è la regola 11).

Screenshot (stessi nomi): `home-1440.jpg` (8470 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13067 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Contatti" al piede). Guardati a pezzi a 390 e 1440 accanto a Cly-Del e barth, e a 320, 768, 1024, 1280 e 1920.

### Che cosa è cambiato, in breve

- **Struttura della famiglia M adattata a un'officina che tiene i ricambi**: testata fissa con sei voci (Ricambi, Macchine, Misure, Cataloghi, Chi siamo, Contatti), "Catalogues EN · DE · FR" e il bottone "Chiama 049 640372"; apertura con il mestiere nel titolo, il comune nell'occhiello, lo stato "Aperto ora" e la loro foto dei torchi in magazzino; un indice delle otto linee con la misura in una riga (come una pagina di catalogo); Ricambi e assistenza su blocco scuro (che cosa fotografare, Chiama, email con l'oggetto, il martinetto con la targhetta); otto schede delle linee con foto, misura, scheda e PDF; le tabelle delle misure (torchio idraulico e "Quale DAVID per il tuo torchio"); sei numeri su blocco rosso; cataloghi con lingua e peso, brochure ZIP, come si compra e i rivenditori; chi siamo con le date; contatti con la tabella degli orari e il modulo; piede in quattro colonne.
- **Il titolo**: "Torchi, martinetti DAVID e pompe, dal 1960". È il titolo di prima ("Torchi e martinetti, dal 1960") con le pompe, che sono metà del loro lavoro di oggi (SCHEDA, par. 1 e 4).
- **Il tono**: "noi" e "tu" come scrivono loro ("teniamo i ricambi", "siamo sempre a tua disposizione", "Produciamo...", "Una piccola e seria azienda artigianale" come titolo di chi siamo, non come slogan di chiusura). Tolti la terza persona, la newsletter e il selettore in apertura.
- **Foto, decisione "niente"**: nessuna foto di repertorio, nessuna illustrazione. Restano solo foto di BCM: in apertura la fila di torchi pronti in magazzino (wa0000, la loro foto più forte: faggio, cerchi rossi, martinetti), in quadrato nativo 1060 px (in pagina 563 px) e in 16:9 sul telefono; in chi siamo la fila di meccanismi in officina (wa0032, stessa giornata, stesso trattamento); il martinetto con la targhetta su fondo scuro nei ricambi, dove serve a far vedere che cosa fotografare; gli otto scontornati del sito tutti nello stesso quadrato grigio. Tolto il torchio scontornato sulla carta dell'apertura (regola 3 e difetto B2).
- **Colori dal marchio**: niente più carta beige. Fondo bianco, grigio neutro #F0F0EE per i blocchi chiari, ghisa #1F1E1C per testo e blocchi scuri, rosso #9E2B22 dei cerchi e del logo dei cataloghi per bottoni, cifre e un blocco pieno, verde #2A6234 solo per "Aperto ora".
- **Tipografia**: da tre famiglie (Zodiak, Sofia Sans, Sofia Sans Condensed) a due. Sofia Sans Condensed 700 per titoli e cifre, come i titoli dei loro cataloghi; Sofia Sans 400 e 700 per testo, etichette, bottoni e tabelle. Zodiak tolto: la serif da galleria a 114 px era una delle cose che "a loro sembrerebbe da grafico" (SCHEDA, par. 5).

### Uso: le prove della SCHEDA

- **A, ricambio, telefono 390x844**: senza scorrere ci sono "ricambi" nella riga sotto il titolo, "Aperto ora, fino alle 18" (calcolato sull'ora di Roma, lunedì-venerdì 8-18, festivi e Pasquetta chiusi, "riapriamo lunedì alle 8" il sabato), "Chiama 049 640372" a tutta larghezza (350x52) e "Ricambi e assistenza". Un tocco su "Ricambi e assistenza" porta ai tre passi (targhetta, diametro di gabbia o vite, pezzo) e al bottone "Manda le foto per email" con l'oggetto "Ricambio per la mia macchina BCM" e il testo da riempire: secondo tocco. A metà pagina il bottone Chiama resta nella testata (48 px).
- **B, rivenditore, 1440x900**: senza scorrere l'indice delle linee mostra pompe Volumex, pompe con inverter, inverter universale e pigiatrici; in un clic dalla scheda "Pompe con inverter" si scarica il catalogo PDF, con "2,3 MB, IT DE EN FR" scritto prima; "Catalogues EN · DE · FR" in testata porta ai cataloghi con una riga in inglese; nei contatti telefono, email e indirizzo stanno in 420 px.
- **C, scelta**: a 390 "Pompe Volumex, fino a 950 hl/ora" è nell'indice a 782 px (prima schermata e poco più) e porta alla scheda; "Quale DAVID per il tuo torchio" dice la vite da 45 a 100 mm per ogni modello; "Come si compra" è nella stessa sezione dei cataloghi; "Apri la mappa" è nei contatti e nel piede.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata fissa a tutte le larghezze (80 px a 1440, 72 a 390); a 390 al 50% della pagina il bottone "049 640372" è a 12 px dall'alto, alto 48; 6 link `tel:`, tutti `+39049640372`. Per la famiglia M c'è anche la voce "Contatti" e il modulo.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. "Torchi, martinetti DAVID e pompe" in H1, "Saonara, Padova" nell'occhiello, "dal 1960" nel titolo, "Chiama 049 640372" pieno (a 390 a tutta larghezza).
3. **Immagine vera dell'azienda in apertura**: PASSA. La fila di torchi BCM nel loro magazzino (nativa 1060x1060, in pagina 563x563 a 1440; 16:9 a tutta larghezza sul telefono). Non è uno scontornato su fondo chiaro.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche e nessun file da `assets/esterne/`.
5. **Foto in serie**: PASSA con un limite. Due serie: le due foto della galleria "In azienda" (stesso giorno, stesso trattamento di `pro_img.py`) e gli scontornati del sito, tutti con lo stesso trattamento, la stessa ombra e lo stesso quadrato. Formati a 1440: tre (1:1, 16:9 e il martinetto scontornato, 1,15). Didascalie: 2 su 11 foto, tutte e due con un fatto (cosa fotografare; luogo e anno). Il limite: sono scatti da telefono e da catalogo, non di un solo fotografo (LEGGIMI, foto da rifare).
6. **Palette dal marchio**: PASSA. Rosso #9E2B22 (cerchi, bacini, logo dei cataloghi) e ghisa #1F1E1C, verde solo per "Aperto ora", più bianco e quattro grigi; niente `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 68, 44, 26, 20, 18, 16, 14 (7 misure); 390: 48, 38, 30, 22, 18, 17, 16, 14 (8). Testo corrente 18 e 17 px. I 14 px sono solo etichette in maiuscolo spaziato (come M, A4) e la riga legale. Titolo 68 px a 1440 (fascia 60-70), 38 a 390 (34-40).
8. **Due famiglie**: PASSA. Sofia Sans Condensed (titoli, cifre, telefono grande) e Sofia Sans (testo e interfaccia).
9. **Servizi in schede con foto**: PASSA. Otto schede in 4 colonne (2 sotto 860 px), passo 28 px, tutte col quadrato 1:1 grigio, nome di 26 px, una riga di misure, "Scheda della linea" (tutta la parte alta è un link) e sotto il PDF o lo ZIP con peso e lingue.
10. **Almeno tre tipi di prove**: PASSA con quello che hanno. Sei numeri veri (1960, 30+, 400, 950, 8, 4); rivenditori con il nome (Vivi in Campagna, Enologys, Kidonakis, KOL-Technik); marchio registrato DAVID e quattro SIMEI con il link alle foto degli stand al posto delle certificazioni, che non hanno. Recensioni: nessuna nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: NON PASSA (non ci sono nelle fonti). Nessuna cantina cliente è nominata in 01-analisi o nella SCHEDA. Al loro posto ci sono le tabelle delle misure, che per chi sceglie un torchio servono di più. Da chiedere: tre cantine con nome, comune, anno, modello e una foto (LEGGIMI).
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: Ricambi su ghisa e numeri su rosso; blocchi grigi per indice, misure e chi siamo. Spazio tra le sezioni 120 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno rosso e con il solo bordo, raggio 4 px, 52 px (48 in testata), testo 18 e 16 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando" per il mestiere**: PASSA. Modulo M adattato: tipo di richiesta (Ricambio o assistenza, Preventivo, Sono un rivenditore), macchina e modello dalla targhetta, nome, azienda, email, telefono, messaggio, "Foto della targhetta e del pezzo: allegale all'email che si apre"; compone un mailto con oggetto e campi (da collegare a un servizio, LEGGIMI). Sede con indirizzo, "Apri la mappa", telefono, email e la tabella degli orari; nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Logo, ragione sociale, sede con la mappa, Macchine (8 linee), BCM, Contatti con orari e il link EN DE FR, P.IVA, REA, capitale sociale, Privacy e Cookie; 4 colonne a 1440, testo da 14 px.

### Respinti o non applicati, con il motivo

- **Lavori con il nome, recensioni, certificazioni, squadra con i nomi**: non sono nelle fonti; non inventati, chiesti nel LEGGIMI.
- **Testata di 56 px a 390** (SCHEDA, par. 4): la regola A2 chiede 72-88 px e la prima schermata ci sta lo stesso (la foto finisce a 704 px su 844).
- **Torchio idraulico a destra in apertura a 1440** (SCHEDA, par. 4): la regola 3 vieta l'oggetto scontornato su fondo chiaro in apertura; il torchio è nella prima scheda delle linee. Al suo posto la loro foto dei torchi in magazzino, che mostra le stesse macchine.
- **Martinetto con la targhetta nella prima schermata a 390** (SCHEDA, par. 4): è nella sezione Ricambi, a un tocco, accanto ai passi "che cosa fotografare", dove spiega che cosa mandare; in apertura c'è la foto del magazzino per la regola 3.
- **Il selettore del diametro con il torchio in scala** (versione di prima): tolto. Le stesse misure sono nella tabella del torchio idraulico, leggibili tutte insieme.
- **Mappa incorporata**: no (regola 14 e A6): link "Apri la mappa".

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440, 1920 (corretto durante il lavoro: la tabella del torchio a 320, con le gabbie "45 × 60" su una riga e i margini delle celle stretti sotto 360 px).
- Nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1280, 1440, 1920 (corretti durante il lavoro: le righe dei PDF non allineate nelle schede, perché anche il link del PDF si allungava; le schede a due colonne enormi a 1024, ora 4 colonne fino a 860 px; il campo "Azienda" più basso degli altri).
- Collegamenti: `tel:+39049640372` (6), `mailto:info@bcmenologia.com` (6, tre con oggetto), due mappe su "Viale Veneto 10-12 35020 Saonara PD", 14 ancore tutte esistenti, nessun `href="#"`; PDF e ZIP con i percorsi e i pesi letti dal sito il 3/11/2026.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Sofia Sans e Sofia Sans Condensed (Lettersoup, Google Fonts, SIL Open Font License 1.1), file woff2 variabili serviti dalla pagina da `sito/fonts/`; pesi usati 400 e 700. Zodiak (ITF Free Font License) non è più usato e il file è tolto da `sito/fonts/`.

---

## Versione 1 originale ("Il torchio"), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli e screenshot con `finale_shots.mjs`); i controlli dell'ultimo passaggio sono in `_prova/script/controlli_finali.mjs`. Alta 5.070 px a 1440 piede compreso, 6.916 px a 390.

### Idea

Il torchio idraulico BCM, la loro foto migliore, in piedi sulla carta chiara come in una tavola di catalogo fatta bene: un solo oggetto vero, grande, con la sua ombra su una linea di terra sottile. Quattro legende a filo leggono il pezzo (vite, martinetto DAVID, gabbia in faggio, bacino). Il selettore del diametro cambia i numeri veri della scheda tecnica e porta il torchio in scala sulla linea di terra. La stessa linea di terra torna sotto le sei macchine. Con il nome di un concorrente la pagina non regge: il "60" impresso nel faggio, i cerchi rossi, il DAVID e le sue spinte sono solo di BCM.

### Ultimo passaggio: cosa è cambiato dopo il giudice cieco

Il giudice aveva dato K0 7,5 e K6 6. Le correzioni sono tutte dentro la stessa idea:

- **Il gesto agisce sull'oggetto.** Il torchio cresce e cala dalle ruote in proporzione all'altezza della gabbia del modello scelto: il 90 (gabbia alta 105 cm) ha l'altezza piena della prima schermata, il 60 il 71 %, il 45 il 57 %. Le legende restano agganciate ai pezzi perché la loro posizione usa la stessa scala. Il cambio è netto, senza animazione. Fuori dal modello 60 la didascalia dice "Foto del modello 60, in proporzione alla gabbia del 45". Al telefono la foto non si riscala, perché il selettore sta sotto la foto e la pagina salterebbe sotto il dito: cambiano capacità, peso, gabbia e modello DAVID.
- **Chiusura.** Adesso la frase e i recapiti stanno sopra e la fila di torchi è a tutta larghezza sotto. Il taglio nuovo, largo 1.920 px, non viene mai ingrandito a 1440 né a 1920. Le alte luci sono recuperate e il faggio ha il 22 % di saturazione in meno, con il colore generale al -20 %. I rossi tornano verso il #9E2B22 dei cerchi. La fascia alta con plastica e scatole è rifilata e abbassata. Per il telefono c'è un taglio a parte (1280x800).
- **Officina.** Il taglio è nuovo, in 16:9, sulla fila di meccanismi, senza sgabello, tavolo e cassoni. I medi sono più luminosi di circa 0,7 EV e i grigi sono scaldati verso la carta. La foto sta su 9 colonne (972 px CSS) con la didascalia nelle 3 accanto; la sorgente è larga 1.060 px, quindi non viene ingrandita.
- **Le sei macchine.** Hanno lo stesso trattamento del torchio: rossi e blu del motore spenti, alte luci da flash riportate giù, toni caldi e un filo di contrasto locale. Il faggio della gabbia è riportato verso quello del torchio. In ogni riga l'area visibile degli oggetti sta entro circa il 15 %: il martinetto è al 72 % del riquadro e la gabbia al 74 %, così un componente non è più grande quanto un torchio intero. Le box sono alte 360 px.
- **Link.** Ogni voce della griglia ha il suo id (`#torchi`, `#martinetti`, `#gabbie`, `#pompe`, `#pigiatrici`, `#frutta`) e porta alla pagina della sua linea. Nel menu, "Martinetti DAVID" porta a `#martinetti` e "Ricambi" a `#ricambi`, il paragrafo dei ricambi. I cataloghi portano alla pagina download; Privacy, Cookie e l'informativa portano alle pagine vere. Nessun `href="#"` e nessun link che punta alla sezione che lo contiene.
- **Preventivo nella prima schermata.** Sotto capacità e peso c'è una riga: "Per un preventivo: 049 640372 o info@bcmenologia.com", con `tel:` e `mailto:`. Non c'è nessun bottone pieno.
- **Testi.** "Il DAVID è progettato e brevettato da BCM negli anni 80…" (prima soggetto e verbo non andavano d'accordo). Nella storia tutto è in terza persona: "Di ogni macchina BCM tiene i ricambi…".
- **Piede, colonna Contatti.** Ci sono telefono, email, indirizzo breve con il link alla mappa e "Cataloghi PDF"; gli orari restano solo nella chiusura. Il logo nel piede è a 128x72.
- **Newsletter.** Quando l'invio è valido, sotto il campo compare "Grazie. (Modulo dimostrativo, da collegare al servizio di invio.)" in una riga `aria-live`. La validazione di email e consenso è quella del browser.
- **Menu al telefono.** Il tocco non accende più il celeste di sistema. A menu aperto il bottone dice "Chiudi", Esc lo chiude e il fuoco torna sul bottone.
- **Mappa.** La query è "Viale Veneto 10-12 35020 Saonara PD" in tutti e due i link.
- **Fra 881 e 960 px**, accanto al torchio il titolo restava in una colonna di 150 px. Il giudice non l'aveva visto, perché non aveva provato quelle larghezze. Ora fino a 960 vale l'impaginazione da tablet, e fra 961 e 1180 l'altezza del torchio ha un tetto anche sulla larghezza: alla colonna del titolo restano almeno 400 px. Sotto i 1180 px la didascalia scende sotto la linea di terra, così non tocca le legende quando vanno a capo.

### Prime due schermate

1. **Apertura (1440x900)**:
   - il menu sta accanto al logo e il telefono rosso in alto a destra, così il centro resta libero per la vite;
   - il torchio sta sulla linea di terra, che corre da margine a margine all'altezza delle ruote;
   - a sinistra il titolo "Torchi e martinetti, dal 1960" (Zodiak 114 px), la riga dei fatti, il selettore 45-90, capacità e peso e la riga del preventivo;
   - le legende stanno in una colonna allineata a destra.
   A 390: titolo, il torchio grande senza legende, la riga, il selettore, le quattro misure in due colonne e la riga del preventivo.
2. **Le macchine**:
   - titolo "Attrezzatura per l'enologia, dalla pigiatura al travaso";
   - sei oggetti scontornati con la stessa ombra, in una griglia 3x2 senza riquadri, appoggiati sulla linea di terra;
   - ogni voce ha una frase con misure vere;
   - a 390 è una colonna sola.

Poi l'officina, "Dal 1960, i torchi e i loro ricambi" con i tre fatti (SIMEI 2009-2019, spedizioni, cataloghi in quattro lingue), la chiusura e il piede.

### Caratteri e colori

- **Zodiak** 400 (Indian Type Foundry, Fontshare, ITF Free Font License: uso commerciale gratuito) per i titoli. È una serif ad alto contrasto che fa eco al "BCM" con le grazie del logo.
- **Sofia Sans** (Lettersoup, Google Fonts, SIL Open Font License 1.1) per il testo.
- **Sofia Sans Condensed** (stessa licenza) solo per misure, modelli e telefono, con cifre tabellari.
- I file woff2 sono in `sito/fonts/` e serviti dalla pagina, senza chiamate esterne. `font-synthesis: none`.
- Colori:
  - carta #F2F0EB;
  - inchiostro #1C1B1A;
  - testo secondario #57534E (6,7:1 sulla carta, 6,0:1 sul piede #E8E4DC);
  - un solo accento, #9E2B22, il rosso dei cerchi (6,5:1 sulla carta; bianco su rosso 7,4:1).
  Niente fondo nero: le foto sono al sole e chiedono luce.

### Interazione

Un solo gesto: il selettore del diametro della gabbia (45, 50, 55, 60, 65, 70, 80, 90).
- Sono radio veri: dito, clic, frecce della tastiera e Tab, con il fuoco visibile.
- Al cambio si aggiornano:
  - la scala del torchio e delle legende;
  - capacità e peso;
  - la vite (Ø mm);
  - il martinetto (modello DAVID e spinta);
  - la gabbia (diametro x altezza);
  - la didascalia.
- Dati dalla tabella del torchio idraulico e da quella dei martinetti (brochure BCM 2022).
- Niente dissolvenze allo scorrere, niente effetti sul cursore. Su bottoni e link toccati c'è solo un cambio di colore pieno di 0,12 s.

### Foto

Tutte di BCM, dal loro sito (`assets/originali/`), lavorate con PIL in `finale_img.py` ed esportate in WebP in più larghezze con srcset. Nessuna foto di repertorio. I diritti sono da confermare (LEGGIMI).
- Scontornati: bordo ammorbidito, ombra a terra uguale per tutti, trattamento comune.
- Officina (wa0032) e chiusura (wa0000), galleria "In azienda" del 2022: sono foto da telefono, ripulite. Vanno rifatte dal vero (LEGGIMI).
- Logo: il PNG bianco del sito (170x96) ricolorato in inchiostro, a 85x48 in testata (2x) e a 128x72 nel piede. Non è ricostruito in SVG.

### Chiusura e piede

- **Chiusura "b con foto"**:
  - la frase loro (dal "chi siamo") "Piccola e seria azienda artigianale" a sinistra, i recapiti a destra;
  - i recapiti: telefono grande rosso (`tel:+39049640372`), email (`mailto:`), indirizzo con "Apri la mappa", orari;
  - sotto, la fila di torchi a tutta larghezza;
  - niente riquadri.
- **Piede**:
  - logo e una riga su chi sono;
  - colonne Macchine, BCM e Contatti;
  - newsletter piccola "Una lettera prima della vendemmia";
  - riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, Privacy e Cookie.
  Niente "Seguici", perché non c'è nessun social. A 390 l'ordine è: logo, Macchine e BCM su due colonne, Contatti, newsletter, riga legale.

### Controlli (ultimo passaggio)

- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 880, 881, 1024, 1180, 1280, 1366, 1440, 1600, 1920 e 2560.
- **Screenshot guardati a pezzi**: 1440 e 390, intere e prima schermata; 320, 768, 1024, 1280, 1366 e 1920 in `_prova/tmp-finale/`; 920, 961, 1024, 1100 e 1180 con i modelli 45, 60 e 90. Nessuna sovrapposizione fra legende, didascalia e titolo.
- **Gesto con la tastiera**: da 60, tre volte freccia sinistra porta al 45. Il torchio passa da 604 a 483 px e le legende scendono con lui; la freccia successiva torna al 90.
- **Gesto con il clic**: sul 90 si legge 660 kg, 630 kg, E-90, 50.850 kg, Ø 90 mm, 90 × 105 cm, e il torchio è alto 846 px.
- **Tocco a 390**: sull'80 si legge 475 kg, 460 kg, 80 × 95 cm, D-80.
- **Menu**: si apre con "Chiudi", Esc lo chiude, il tocco su una voce lo chiude e porta all'ancora.
- **Newsletter**: senza consenso non parte; con il consenso compare la riga di riscontro.
- **Link**: un solo numero `tel:+39049640372`, un solo `mailto:info@bcmenologia.com`, la mappa su "Viale Veneto 10-12 35020 Saonara PD". Nessun `href="#"`, e tutte le ancore esistono.
- **Foto**: naturalWidth è maggiore o uguale alla larghezza CSS a 1440 e a 1920 (officina 1060 su 972, chiusura 1920 su 1920). A 2560 la chiusura è ingrandita di 1,33 volte: serve lo scatto nuovo.
- **U+2014**: nessuno in pagina, in questa nota e nel LEGGIMI.
- **Segnali da IA** (`_metodo/kit/segnali.sh`): 17 soglie su 18 a posto. Da guardare: due misure di H2 (60 e 66 px), volute, perché la gerarchia la fa l'apertura da 114 px. Resta sotto soglia l'area foto, al 29,5 % contro il 35 %. È il caso che la guida descrive per le aziende senza foto grandi: le loro foto vere più larghe sono scatti da telefono di 1.920 px, il resto è scontornato. In più, il torchio riportato in scala al modello 60 occupa meno spazio. La guida dice che non va nascosto: è la prima cosa da chiedere a BCM, cioè la giornata di foto nel LEGGIMI. Non ho allargato le foto oltre la loro misura nativa. Il taglio più alto della chiusura riportava plastica e scatole e l'ho scartato.
- **Divieti del committente**: niente gradienti viola, testo in gradiente, emoji, Inter, card col bordo colorato, vetro, badge, tre box con icona, Lucide, shadcn, dissolvenze, effetti sul cursore, hover che sbiadiscono, corsivo d'accento, tabelle a filetti.
- **Dati**: ogni numero viene da `01-analisi.md` e dalle brochure in `assets/originali/cataloghi/`.
