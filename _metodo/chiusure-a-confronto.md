# Chiusure della campagna a confronto (stile B)

Foglio: `_metodo/chiusure-a-confronto.jpg` (JPEG 80): le 13 chiusure a 1440 px, da `<Cartella>/screenshot/home/chiusura-1440.jpg`, ridotte a metà, tre per riga, nell'ordine della tabella. Controllo del 20 ottobre 2026, dopo il passaggio di tutte le chiusure allo stile B scelto dal committente (frase propria grande, recapiti in poche righe, una sola foto grande, piede su una riga). Tutti gli screenshot sono più recenti della loro `sito/index.html`.

## Esito

- **Stile B**: lo seguono tutte e 13. Ognuna ha una frase dell'azienda come H2 (nessun "Contatti", nessun titolo di luogo), i recapiti senza etichette né riquadri, una sola foto e il piede su una riga.
- **Oggetti disegnati, riquadri, tabelle a filetti**: nessuno. Nella chiusura e nel piede di nessuna pagina ci sono `svg`, `canvas`, `table` o immagini di fondo (misurato con Playwright); l'unica immagine è la foto.
- **Foto**: tutte diverse. Nessuna foto di chiusura compare in un'altra home della campagna: confronto per impronta visiva (dHash, anche sul taglio quadrato) con tutte le immagini di tutte le `*-Sito/sito/`, e nessun ID Unsplash o Pexels ripetuto tra i `CREDITI.md`.
- **Frasi**: tutte diverse; nessuna compare nella pagina di un'altra azienda. Sette frasi riprendono una frase già detta più su nella stessa pagina (Paraga Pelli, FM Sistemi, Daisyplast, Teklam, Solteco, Innovatex Green, Tacchificio Riviera): è voluto, la chiusura chiude con la frase dell'azienda.
- **Impaginazioni**: tre schemi (F = frase e recapiti affiancati in alto, foto a tutta larghezza sotto; D = frase e recapiti a sinistra, foto a destra fino al bordo; S = foto a sinistra dal bordo, frase e recapiti a destra). Due chiusure vicine nella sequenza non hanno mai lo stesso schema: F D S D S F D S F S D F S.
- **Altri controlli**: contrasto AA su tutti i testi della chiusura e del piede a 1440 e 390 (nessun testo sotto 4,5:1, o 3:1 per i titoli); nessuno scorrimento orizzontale e nessun elemento fuori dalla finestra a 1440, 390 e 320; nessun U+2014 nelle 13 pagine.
- **Correzioni**: nessuna. Non c'era niente da correggere, quindi nessuna pagina e nessuno screenshot sono stati rifatti.

## Tabella

| Azienda | Frase | Foto | Impaginazione |
|---|---|---|---|
| Paraga Pelli | "Ogni articolo ha la sua cartella colori. Si chiede per email o al telefono." | La squadra seduta sui bancali di pelli intere nel magazzino di Tombelle (foto loro, `squadra-*.jpg`) | F: frase a sinistra, recapiti a destra, foto a tutta larghezza con didascalia, piede chiaro |
| Hambro | "Sul sito c'è solo una parte: il resto si chiede al telefono o per posta" | Fibbia dorata in primo piano (Rodrigues, Unsplash FXVC26csSz4, segnaposto) | D: frase in alto e recapiti in basso a sinistra, foto a destra che esce dal bordo |
| Mario Agnoletto | "Seguiamo il pezzo dal progetto alla serie" | La sede con l'insegna "Incisore meccanico Mario Agnoletto" (foto del loro sito) | S: foto a sinistra dal bordo, frase e recapiti a destra |
| FM Sistemi | "Qui il cantiere ha un numero solo, e i mestieri arrivano nell'ordine in cui servono." | La metà bassa del collettore con i tubi multistrato (Pavel Danilyuk, Pexels 7937309, segnaposto) | D: frase e recapiti a sinistra, foto a destra fino al bordo |
| Daisyplast | "Estrudiamo il film in bolla e lo saldiamo in sacchi, shopper, bobine e monopieghe." | Le bobine di film bianco sui mandrini della linea (foto 001 del loro sito) | S: foto a sinistra dal bordo, frase stretta e alta e recapiti a destra |
| Teklam | "Dal file al camion, in un'officina sola" | L'ugello del laser sulla lamiera con poche scintille (Cemrecan Yurtman, Unsplash qk2i7n39-B0, "Foto indicativa") | F su nero: frase a sinistra, referenti per nome a destra, foto a tutta larghezza, piede nero |
| 3Esse | "Calcoli e disegni costruttivi di ponti, coperture ed edifici in acciaio e cemento armato." | L'arco di un ponte strallato in bianco e grigio (Wesley Li, Unsplash, segnaposto) | D: frase e recapiti a sinistra, foto a destra fino al bordo |
| Bertolin Antonio | "Per un preventivo mandate disegno, materiale e quantità." | Lo stabilimento di Tombelle visto dall'alto (foto loro) | S: foto a sinistra dal bordo, frase e recapiti a destra, su bianco |
| Bazzato | "L'officina di Andrea e Paolo Bazzato, per auto di ogni marca." | SUV bianco intero sul ponte in officina chiara (Artem Podrez, Pexels 8986138, "Foto indicativa") | F: frase grande a sinistra, recapiti con WhatsApp a destra, foto a tutta larghezza fino al piede |
| Area Systems | "Chiamate o scrivete con la sigla del pezzo o le misure del quadro." | La cuffia di sfiato in acciaio (Pancrate, Unsplash CQkoCt7taPo, segnaposto) | S: foto a sinistra dal bordo, frase e recapiti a destra |
| Solteco | "Solteco porta gli adesivi a base acqua nei calzaturifici e segue il reparto sul processo d'incollaggio." | Tomaie montate sulle forme e suole sul carrello (Fernanda Simões, Pexels 13524876, segnaposto) | D: frase lunga e recapiti a sinistra, foto a destra che esce dal bordo |
| Innovatex Green | "Ordini la mattina, ricevi il materiale nel pomeriggio." | La corsia del magazzino con il carrello elevatore fra i rotoli (foto loro, febbraio 2026) | F: frase a sinistra, recapiti a destra, foto a tutta larghezza con didascalia |
| Tacchificio Riviera | "Il cliente presenta un disegno con la sua idea: noi la interpretiamo e la realizziamo." | Due persone esaminano un prototipo di tacco davanti agli scaffali dei modelli (foto del loro sito) | S: foto a sinistra dal bordo, frase in carattere stretto e recapiti a destra |
