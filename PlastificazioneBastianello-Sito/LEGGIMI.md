# Plastificazione Bastianello: proposta di nuova homepage

Proposta non richiesta di una nuova home per Plastificazione Bastianello S.r.l. (Grisignano di Zocco, VI). Solo la home, non pubblicata, azienda non contattata.

- Pagina: `sito/index.html`, con `sito/img/` (WebP in più larghezze) e `sito/fonts/` (Archivo e Onest, woff2). Si apre in locale con il browser.
- Screenshot: `screenshot/home/` (home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg) e la nota di progetto `screenshot/home/NOTA.md`.
- Rifare tutto: `sh _prova/script/build_finale.sh` (foglio d'apertura, foto, pagina, screenshot). Prove di interazione, larghezze da 320 a 2560 e collegamenti: `node _prova/script/finale_prova.mjs file://.../sito/index.html <cartella>`.
- Analisi con le fonti: `01-analisi.md`. Giudizio sui prototipi: `_prova/giudizio.json`. Prototipi: `_prova/home/a` e `_prova/home/b`.

## Dati da confermare con l'azienda (non sono in pagina, o ci sono con riserva)

1. **Unità dei formati**: il sito di oggi scrive "formati fino a 120 x 160" (plastificazione) e "f.to min 32 X 44 / f.to max 100 x 140" (serigrafica) senza unità. Nelle schede delle lavorazioni sono scritti in cm come gli altri formati: va confermato. Dalla prima schermata la riga "Fogli fino a 120 x 160 cm" è stata tolta finché l'unità non è confermata (e valeva solo per la plastificazione).
2. **"Da oltre 40 anni"**: è la frase del loro sito, ma la srl è iscritta nel 2004. Quando è nata l'attività, con quale ditta, chi l'ha fondata. Con una data certa si può scrivere l'anno in pagina (oggi non c'è nessuna data).
3. **BRCGS**: i due certificati pubblicati sono scaduti (05/03/2020 e 05/03/2021). In pagina non c'è finché non arriva il certificato in corso; poi va nella riga "Packaging alimentare" e tra le pagine (Certificazioni).
4. **Permessi dei clienti**: l'oggetto della prima schermata è il damasco in serigrafia di un foglio "TANCELEBRATE / PaolaP": in pagina solo il motivo, senza marchio, scritte né sito (ritaglio in `_prova/script/finale_foglio.py`), ma il disegno del damasco resta del cliente. I fogli con UV a riserva erano di un cliente con il marchio "nathia" in vista: in pagina il marchio è stato tolto in tutte le sue ripetizioni (ritocco in `finale_img.py`, nessuna IA), restano il nome generico del prodotto e i testi minuti illeggibili. I fogli nella verniciatrice serigrafica sono astucci per biscotti di un cliente, mossi e senza marchio leggibile. Per tutti e tre serve il permesso del cliente o una foto nuova.
5. **Origine delle foto**: `blister.jpeg` (probabile repertorio, in pagina con "Foto indicativa") e le foto di reparto (film olografico sulla plastificatrice, Nikon D5100; finestratrici; verniciatrice serigrafica; il damasco): chi le ha scattate e con quale licenza.
6. **Soft touch e antigraffio**: sono film che applicano loro o solo voci d'elenco? In pagina restano come sul sito di oggi.
7. **REA e PEC**: REA VI-300667 e PEC da aggregatori (aziende.it, companyreports.it), non dal sito. Fuori dal piede finché non c'è la visura. Lo stesso per dipendenti e fatturato, che non sono in pagina.
8. **Orari** dell'ufficio e del ritiro merce, un eventuale referente: non pubblicati, non in pagina.
9. **Frase della chiusura**: "Abbiamo investito per migliorare i tempi di risposta" viene dalla pagina `azienda/` ("migliorare ulteriormente i tempi di risposta"). Al posto dello slogan "Impegno e volontà a tua completa disposizione", che era generico e dava del tu. Se all'azienda lo slogan sta a cuore, si può rimettere nel piede.
10. **Frase sul preventivo**: il prototipo A aveva "Per un preventivo scriveteci la lavorazione, il formato del foglio e la quantità". Tolta dalla pagina: se all'azienda va bene, si può rimettere sotto i recapiti.
11. **Privacy e Cookie**: le pagine di oggi sono vuote; servono i testi (iubenda è già attivo per i cookie).

## Foto da rifare dal vero

Il materiale di oggi è sufficiente per una proposta, non per il sito vero. Mezza giornata di still life e mezza in reparto, con luce controllata.

1. **Apertura, il foglio col damasco** (oggi è un ritaglio di 917 px della loro foto, ruotato e appoggiato sul fondo con un'ombra disegnata): lo stesso foglio nero con la serigrafia UV lucida, oppure un lavoro di cui si ha il permesso, intero, senza marchio. Foglio appoggiato su un piano color carta (vicino a #F6F4F0), luce radente da sinistra che accende il lucido e lascia opaco il fondo, ripreso un poco dall'alto, tutto a fuoco (f/11-f/16), almeno 3500 px sul lato lungo. Serve anche la versione scontornata con l'ombra vera.
2. **L'astuccio con la finestra**: un astuccio di cartoncino teso stampato, meglio con la finestra ad angolo, a tre quarti su fondo carta, il film della finestra che prende la luce. Per la scheda Finestratura (oggi c'è la finestratrice ad altezza nastro, foto documentaria e scura).
3. **Un foglio con UV a riserva su fondo chiaro**: vernice lucida solo su alcune zone, luce radente che la fa brillare; nessun marchio leggibile.
4. **La verniciatura blister**: la valva su un cartoncino verniciato, in mano o su un piano chiaro.
5. **La finestratura ad angolo**: un astuccio con la finestra che gira sullo spigolo, a tre quarti.
6. **I film**: un campione per film (metallizzato, olografico, soft touch) sulla stessa carta, stessa luce, stessa inquadratura. Il primo sostituisce la foto Unsplash della scheda Plastificazione (film olografico stropicciato, non loro).
7. **Reparto**: la bobina di film sulla plastificatrice (meglio senza gli scaffali in alto), la finestratrice con gli astucci in uscita, il forno UV, le mani sul foglio; luce del reparto pulita, niente neon nell'inquadratura.

## Pagine del sito nuovo a cui punta il piede

`azienda/`, `certificazioni/`, `contatti/` (con il modulo di preventivo), `lavorazioni/finestratura/`, `lavorazioni/plastificazione-accoppiatura/`, `lavorazioni/verniciatura-uv/`, `lavorazioni/verniciatura-blister/`, `lavorazioni/verniciatura-serigrafica/`, `settori/alimentare/`, `settori/biodegradabile/`, `settori/lusso-shoppers/`, `privacy/`, `cookie/`. Nella proposta queste pagine non esistono ancora; la testata usa le ancore della home (#lavorazioni, #settori, #azienda, #contatti).

Newsletter: no. Lavorano conto terzi su commessa per cartotecniche e stampatori, senza notizie, fiere, cataloghi, collezioni o clienti privati. Social: nessuno, quindi niente colonna "Seguici".

## Licenze

- **Caratteri**: Archivo e Onest da Google Fonts, SIL Open Font License 1.1 (uso commerciale, incorporazione e distribuzione dei file ammesse). Serviti dalla pagina in `sito/fonts/`.
- **Foto esterne** (segnaposto, da sostituire): una sola, Unsplash gOfXb8eW4g8 di Emily Bernal (Unsplash License), nella scheda Plastificazione con "foto indicativa". Il fotomontaggio dell'astuccio da Pexels 15807279 non è più in pagina. Dettagli in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- **Foto del sito di oggi** (`assets/originali/`): proprietà dell'azienda o di chi le ha fornite; usate solo nella proposta. In pagina: il damasco (apertura), due foto della finestratrice, i fogli con UV a riserva, `blister.jpeg`, la verniciatrice serigrafica, il film olografico sulla plastificatrice (chiusura).

## Logo

Il logo in pagina (testata e piede) è il loro SVG vettoriale, copiato dal codice della testata del sito di oggi (`assets/originali/logo-orizzontale-vettoriale.svg`): P rossa #CC3429 e B con la scritta nel colore del testo (nel file originale il secondo tracciato non ha colore). Nessuna ricostruzione: è il vettoriale vero. Per il favicon c'è il monogramma `logo-favicon-PB-512.png`. Il marchio vecchio (foglio arricciato con pennino) non è usato.
