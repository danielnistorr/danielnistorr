# Officine Negrizzolo: proposta di nuova home

Proposta non richiesta di una nuova homepage per Negrizzolo S.a.S. di Negrizzolo ing. Paolo & C. (Grisignano di Zocco, VI). Solo la home.

## Dove sono le cose

- `sito/index.html`: la home finale (statica, si apre con file:///). `sito/img/`: solo le immagini usate, WebP e JPEG in più larghezze. `sito/fonts/`: Archivo variabile in woff2 e la licenza `OFL.txt`.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (copia `finale_index.html` in `sito/index.html`), screenshot (`finale_jpg.py`, `finale_misura.mjs`), il controllo dello scorrimento orizzontale (`finale_largo.mjs`) e il collaudo (`finale_prova.mjs`: console, altezza costante del selettore, tastiera, dito, testata a 1024, piede, scrollWidth da 320 a 2560). Con `solo-pagina` salta le immagini.
- `01-analisi.md`: fatti con le fonti; `_prova/home/a` e `_prova/home/b`: i due prototipi giudicati.

## Pagine che il sito nuovo dovrà avere

I link della home e del piede puntano a queste 12 pagine (oggi non esistono nella proposta):
`rimorchi-ribaltabili`, `rimorchi-fissi`, `carribotte`, `vasche-inox-uva`, `applicazioni-speciali` (con le ancore `#idrosemina`, `#digestato`, `#aspira-foglie`, `#scarrabile`), `riparazioni`, `taglio-laser`, `usato`, `chi-siamo`, `contatti`, `privacy`, `cookie`. I link "Altri N modelli" del selettore portano alle tre pagine prodotto con le tabelle complete.

## Dati da confermare con l'azienda

- **Logo**: quale versione usare, "NEGRIZZOLO OFFICINA MECCANICA" del biglietto da visita (qui usata, ricostruita in SVG) o "Officine NEGRIZZOLO" della testata del sito di oggi; e il grigio del marchio (qui #8E9094, un po' più scuro dell'originale #B3B5B8 per reggere sulla carta). Serve il file vettoriale originale, se esiste.
- **"I primi in Veneto a costruire cisterne e carribotte"**: frase di chi-siamo, è nell'apertura; chiedere se c'è un ricordo o un documento da raccontare.
- **"Dall'Ottocento"**: il sito dice "fabbri e maniscalchi già nel lontano 1800"; in pagina è diventato "dall'Ottocento". Se la famiglia ha una data o un documento, si può essere più precisi.
- **Anno di nascita della ditta**: in pagina c'è solo "anni '50" e "a metà degli anni '50"; se si può scrivere un anno preciso, e quindi "70 anni" invece di "oltre 60" del sito di oggi.
- **Famiglia**: in pagina "Dalla fine degli anni '80 c'è Giovanni, dal 2000 suo figlio Paolo". Non si dice che Giovanni sia figlio di Riccardo: da chiedere se si vuole scrivere "tre generazioni".
- **Modelli a listino**: se le tre tabelle (19 ribaltabili, 18 fissi, 13 carribotte) sono ancora tutte valide e se i carribotte si fanno solo zincati. Le 11 portate dell'apertura e del selettore vengono da queste tabelle; dove una portata manca per un prodotto la home mostra la più vicina.
- **Email del laser**: laser@negrizzolo.it (piede del sito di oggi, usata qui) o tecnico@negrizzolo.it (pagina Contatti). Se pubblicare il cellulare 347 2386150 del biglietto (non usato).
- **Civico**: 14 (sito, usato qui) o 14/D (registro delle imprese).
- **Taglio laser**: macchina, potenza, piano di lavoro e spessori massimi per materiale, per una riga in più; e il "da 20 anni" della home di oggi.
- **Foto della chiusura**: è `images_vasche-inox_1.jpg` del sito (la sede con l'insegna al tramonto, un rimorchio a tre assi con vasca inox): chiedere se è un loro lavoro che si può mostrare e se l'insegna è ancora quella.
- **PEC**: non trovata; capitale sociale non pubblico (sas).
- **Altri social**: trovato solo YouTube (4 video di circa 15 anni fa). Nel piede la colonna si chiama "Video" e non "Seguici", perché il canale è fermo: se lo riprendono, o se c'è una pagina Facebook o Instagram, la colonna torna "Seguici".
- **Foto d'archivio**: l'originale della foto del carrobotte sotto i portici (oggi una miniatura di 300 px) e la sua data, per scrivere l'anno nella didascalia.

## Foto da rifare dal vero

Tutte le immagini dei prodotti vengono dal sito di oggi (1000 px, fotografate nel piazzale) e sono scontornate: reggono la proposta, non il sito vero. L'area foto della home è al 22,5 %, sotto il 35 % della guida, per questo (tolta anche la fascia di repertorio dell'uva). Il servizio fotografico è la condizione perché la home sia all'altezza delle migliori della campagna, non un'aggiunta. Una giornata di scatto risolve:

1. **Il dumper rosso dell'apertura** (sostituisce lo scontorno, oggi mostrato a 1000 px e morbido a densità 2): di profilo pieno, intero col timone e il telo, fotocamera all'altezza dei mozzi, obiettivo 70-100 mm da lontano per non deformare, in capannone vuoto o nel piazzale con un fondale chiaro e luce diffusa (cielo coperto o pannelli), almeno 6000 px di lato lungo, portellone aperto come oggi. Uno scatto anche di tre quarti dal davanti. L'ombra vera a terra.
2. **Ribaltabile con sponde, fisso a pianale, carrobotte zincato con la pompa**: stessa luce, stessa altezza e stessa distanza, così stanno sulla stessa linea di terra senza ritocchi.
3. **Vasca inox piena d'uva in vendemmia**: in vigna o all'arrivo in cantina, luce del tardo pomeriggio, dall'alto di tre quarti; e la vasca vuota sul fondale chiaro.
4. **Dettagli** per la pagina prodotto: zincatura, saracinesca, pompa, cerniere delle sponde, la scritta "NE GRI ZZO LO" a luce radente.
5. **Officina**: una riparazione in corso con le mani e il pezzo, il magazzino ricambi, il laser al lavoro su un loro pezzo (non la foto del costruttore della macchina).
6. **Chiusura**: la facciata con l'insegna "NEGRIZZOLO" e un loro rimorchio rosso davanti, alla stessa luce del tramonto della foto di oggi (che è di 1000 px), senza auto parcheggiate, almeno 4000 px.

## Ritocchi fatti alle loro foto (da dire all'azienda)

- Dumper: tolti il trattore, il timone e i cavi a destra (coperti dal trattore nella foto), il braccio e il telo arrotolato sopra il bordo del cassone; fondo sostituito dalla carta, ombra disegnata.
- Foto della chiusura: nessun ritocco, solo colore e contrasto comuni a tutta la pagina.
- Scontorni con il modello di segmentazione ISNet (separa la figura dal fondo, non genera pixel).

## Licenze

- **Archivo**: Omnibus-Type, Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito da `sito/fonts`, licenza in `sito/fonts/OFL.txt`.
- **Foto dell'azienda**: dal sito negrizzolo.it, solo per la proposta.
- **Foto segnaposto**: nessuna nella home finale (la fascia dell'uva di Thomas Schaefer, Unsplash, è stata tolta). Le otto foto di `assets/esterne/` restano con le licenze in `assets/CREDITI.md`, per le pagine interne se servono.

## Perché niente newsletter

Non pubblicano notizie, cataloghi o fiere, l'usato ha un solo annuncio e i clienti sono aziende agricole che telefonano. Se l'usato crescerà, un "avvisami quando c'è un usato" potrà prenderne il posto nel piede, collegato a un servizio di invio.
