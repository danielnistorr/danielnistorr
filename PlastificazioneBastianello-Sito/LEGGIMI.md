# Plastificazione Bastianello: proposta di nuova homepage

Proposta non richiesta di una nuova home per Plastificazione Bastianello S.r.l. (Grisignano di Zocco, VI). Solo la home, non pubblicata, azienda non contattata.

- Pagina: `sito/index.html`, con `sito/img/` (WebP in più larghezze) e `sito/fonts/` (Archivo e Onest, woff2). Si apre in locale con il browser.
- Screenshot: `screenshot/home/` (home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg) e la nota di progetto `screenshot/home/NOTA.md`.
- Rifare tutto: `sh _prova/script/build_finale.sh` (astuccio, foto, pagina, screenshot). Prove di interazione e larghezze: `node _prova/script/finale_prova.mjs file://.../sito/index.html <cartella>`.
- Analisi con le fonti: `01-analisi.md`. Giudizio sui prototipi: `_prova/giudizio.json`. Prototipi: `_prova/home/a` e `_prova/home/b`.

## Dati da confermare con l'azienda (non sono in pagina, o ci sono con riserva)

1. **Unità dei formati**: il sito di oggi scrive "formati fino a 120 x 160" (plastificazione) e "f.to min 32 X 44 / f.to max 100 x 140" (serigrafica) senza unità. In pagina sono scritti in cm come gli altri formati: va confermato.
2. **"Da oltre 40 anni"**: è la frase del loro sito, ma la srl è iscritta nel 2004. Quando è nata l'attività, con quale ditta, chi l'ha fondata. Con una data certa si può scrivere l'anno in pagina (oggi non c'è nessuna data).
3. **BRCGS**: i due certificati pubblicati sono scaduti (05/03/2020 e 05/03/2021). In pagina non c'è finché non arriva il certificato in corso; poi va nella riga "Packaging alimentare" e tra le pagine (Certificazioni).
4. **Permessi dei clienti**: il damasco in serigrafia è un foglio "TANCELEBRATE / PaolaP" (in pagina solo il motivo, senza marchio né scritte); i fogli con UV a riserva mostrano il marchio "nathia"; i fogli della verniciatrice serigrafica sono astucci per biscotti di un cliente (sfocati). Serve il permesso o una foto nuova.
5. **Origine delle foto**: `blister.jpeg` (probabile repertorio) e la foto del film olografico sulla plastificatrice (Nikon D5100, sembra loro): chi le ha scattate e con quale licenza.
6. **Soft touch e antigraffio**: sono film che applicano loro o solo voci d'elenco? In pagina restano come sul sito di oggi.
7. **REA e PEC**: REA VI-300667 e PEC da aggregatori (aziende.it, companyreports.it), non dal sito. Fuori dal piede finché non c'è la visura. Lo stesso per dipendenti e fatturato, che non sono in pagina.
8. **Orari** dell'ufficio e del ritiro merce, un eventuale referente: non pubblicati, non in pagina.
9. **Frase sul preventivo**: il prototipo A aveva "Per un preventivo scriveteci la lavorazione, il formato del foglio e la quantità". Tolta dalla pagina: se all'azienda va bene, si può rimettere sotto i recapiti.
10. **Privacy e Cookie**: le pagine di oggi sono vuote; servono i testi (iubenda è già attivo per i cookie).

## Foto da rifare dal vero

Il materiale di oggi è sufficiente per una proposta, non per il sito vero. Mezza giornata di still life e mezza in reparto, con luce controllata.

1. **Apertura, l'astuccio con la finestra** (oggi è un fotomontaggio da Pexels, "Foto indicativa"): un astuccio bianco di cartoncino teso, meglio se con la finestra ad angolo, che è la loro specialità. Fondo carta chiaro (vicino a #F6F4F0), luce di finestra morbida da sinistra, vista a tre quarti un poco dall'alto così si vedono il bordo del film e lo spessore del cartone sul taglio. Finestra vuota o con un contenuto chiaro e neutro. Almeno 3000 px sul lato lungo, a fuoco su tutto l'astuccio (diaframma chiuso, f/11-f/16), nessun marchio di cliente. Serve anche la versione scontornata.
2. **Il damasco senza marchio**: lo stesso foglio nero con serigrafia UV lucida, a luce radente da un lato, su un'area del foglio senza scritte, tutta a fuoco, 3000 px.
3. **Un foglio con UV a riserva su fondo chiaro**: vernice lucida solo su alcune zone, luce radente che la fa brillare; nessun marchio leggibile.
4. **La verniciatura blister**: la valva su un cartoncino verniciato, in mano o su un piano chiaro.
5. **La finestratura ad angolo**: un astuccio con la finestra che gira sullo spigolo, a tre quarti.
6. **I film**: un campione per film (metallizzato, olografico, soft touch) sulla stessa carta, stessa luce, stessa inquadratura.
7. **Reparto**: la bobina di film sulla plastificatrice (meglio senza gli scaffali in alto), la finestratrice con gli astucci in uscita, il forno UV, le mani sul foglio; luce del reparto pulita, niente neon nell'inquadratura.

## Pagine del sito nuovo a cui punta il piede

`azienda/`, `certificazioni/`, `contatti/` (con il modulo di preventivo), `lavorazioni/finestratura/`, `lavorazioni/plastificazione-accoppiatura/`, `lavorazioni/verniciatura-uv/`, `lavorazioni/verniciatura-blister/`, `lavorazioni/verniciatura-serigrafica/`, `settori/alimentare/`, `settori/biodegradabile/`, `settori/lusso-shoppers/`, `privacy/`, `cookie/`. Nella proposta queste pagine non esistono ancora; la testata usa le ancore della home (#lavorazioni, #settori, #azienda, #contatti).

Newsletter: no. Lavorano conto terzi su commessa per cartotecniche e stampatori, senza notizie, fiere, cataloghi, collezioni o clienti privati. Social: nessuno, quindi niente colonna "Seguici".

## Licenze

- **Caratteri**: Archivo e Onest da Google Fonts, SIL Open Font License 1.1 (uso commerciale, incorporazione e distribuzione dei file ammesse). Serviti dalla pagina in `sito/fonts/`.
- **Foto esterne** (segnaposto, da sostituire): Pexels 15807279 di Connor Scott McManus (Pexels License) per l'astuccio d'apertura, rimaneggiato; Unsplash gOfXb8eW4g8 di Emily Bernal (Unsplash License) per la plastificazione. Dettagli e pagine delle foto in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- **Foto del sito di oggi** (`assets/originali/`): proprietà dell'azienda o di chi le ha fornite; usate solo nella proposta.

## Logo

Il logo in pagina (testata e piede) è il loro SVG vettoriale, copiato dal codice della testata del sito di oggi (`assets/originali/logo-orizzontale-vettoriale.svg`): P rossa #CC3429 e B con la scritta nel colore del testo (nel file originale il secondo tracciato non ha colore). Nessuna ricostruzione: è il vettoriale vero. Per il favicon c'è il monogramma `logo-favicon-PB-512.png`. Il marchio vecchio (foglio arricciato con pennino) non è usato.
