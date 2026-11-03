# Home di Etichettificio Veneto

## Metodo ibrido (novembre 2026)

3/11/2026. Regole: `_metodo/professionale/ALTO-LIVELLO.md`, sezione D ("Carattere e finitura"), con la riga di Etichettificio Veneto nel capitolo 5 (gruppo M1, modello T, riferimento The Label Makers). Metodo scelto dal committente: prima schermata secondo la sezione D, sotto i contenuti e le funzioni della versione professionale su una griglia sola. La versione professionale com'era è copiata in `_prova/versione-pro/` (sito e screenshot). Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`. Misure: `_prova/alto/misura-d.mjs` (copia estesa di `alto/diagnosi/misure/misura.mjs`), esito in `_prova/alto/misura-d-esito.txt` e `misura-d.json`; la stessa misura sulla versione professionale è in `misura-d-esito.pro.txt`.

### Ritocco dopo il giudice da agenzia (3/11/2026)

Il giudice da agenzia aveva dato 6,5 (prima 5,5): idea giusta, esecuzione del gesto debole. Che cosa è cambiato in `sito/index.html` (la versione di prima è copiata in `_prova/alto/prima-del-ritocco/`, con le sue schermate):

- **Orario (difetto bloccante).** Tolto dall'apertura a 390. Nel piede resta "Lunedì-venerdì 8-12 e 13.30-17.30" con sotto "Orario da confermare al telefono."; "Sabato e domenica chiuso", che non veniva da nessuna fonte, è tolto. Sul telefono l'orario sta nel pannello del menu, con la stessa avvertenza ("orario da confermare al telefono"). Ogni occorrenza di "8-12" ha accanto "da confermare".
- **La parola a tutta griglia.** `font-size: calc(100cqi / 2.307)` sulla griglia dell'apertura (contenitore), con `margin-left: -.039em` per recuperare il fianco della E: l'inchiostro va dal margine sinistro al bordo destro della griglia a tutte le larghezze (misurato sui pixel: 112-1328 a 1440, 20-370 a 390, 320-1601 a 1920, 20-300 a 320). A 1440 la parola è a 527 px.
- **Una sovrastampa vera.** La parola è il blu di quadricromia stampato in due passaggi trasparenti (`mix-blend-mode: multiply`): ciano e magenta, con il magenta fuori registro in orizzontale di `max(4px, .03em)` (16 px a 1440, 4,6 a 390, circa 3 px nella miniatura a 300 px). Dove si sovrappongono i due inchiostri fanno il blu scuro, ai bordi restano la frangia ciano da una parte e quella magenta dall'altra, come su un foglio di avviamento. Il giallo e il blu coprente di prima sono tolti: con quattro inchiostri moltiplicati la parola diventava nera. I quattro quadratini sono sostituiti da due crocini di registro in filo (in alto e in basso al centro, fuori dal taglio) e da una striscia di controllo lungo il bordo basso (giallo, magenta, ciano, blu del marchio e le tre sovrastampe a due a due). Questo corregge anche il difetto minore dei quadratini non allineati alla linea delle maiuscole.
- **Il testo della parola una volta sola nel DOM.** La lastra magenta è un pseudo-elemento (`content: attr(data-parola)`): `h1.textContent` è "Etichette autoadesive, prodotte a Saonara (Padova)".
- **Una sola linea d'attacco a destra.** Margini della griglia portati a 112 px a 1440 (griglia di 1216 px; da 1504 px in su resta 1280). Tutto il contenuto di destra parte dalla colonna 6, a 632 px a 1440: riga dei fatti in apertura, descrizioni dell'indice, lato della Stamperia, i quattro passi, l'archivio, la tavola, i certificati, il modulo, la seconda colonna del piede e delle pagine (controllato con `_prova/alto/ritocco-controlli.mjs`). Il titolo dell'apertura non sta più a 80 px dal bordo (D4): l'inchiostro della E è a 112, la scatola del testo a 91.
- **Una sezione che rompe lo schema.** "Per ogni settore, le sue regole" è a tutta griglia: titolo sopra, poi le sei righe larghe 1216 px sulle stesse 12 colonne della pagina, il nome a 40 px Karla 500 nelle colonne 1-5, la descrizione dalla 6, la freccia sulla 12.
- **La facciata nel suo formato nativo 8:3.** File intero 1920x720 (`img/sede-8x3-1920.webp`, 85 KB, fatto con `_prova/alto/script/immagini-8x3.py`, stesso trattamento di `immagini.py`), mostrato a 1216x456 a 1440: rimpicciolito 1,58 volte, niente più taglio 16:9. Sotto i 1000 px `sede-8x3-960.webp`; sul telefono resta il taglio 1:1. I file 16:9 sono tolti da `sito/img/`.
- **La pausa morta sotto l'apertura.** L'apertura non è più alta quanto lo schermo: padding 72 sopra e 64 sotto. A 1440 il foglio finisce a 723 px e il primo titolo è a 907 (184 px), tutto fuori dalla prima schermata.
- **Telefono.** La parola è larga 350 px (150 px di corpo). Il foglio riempie la prima schermata fino alla barra: la parola in testa, il titolo a 32 px e i quattro fatti a righe con il filetto in fondo, come la legenda di un foglio di prova. La riga dei fatti è diventata quattro frasi corte ("In bobina e a foglio. Flexo UV, tipografica UV, offset e digitale. Fino a 8 colori. ISO 9001 e FSC."). "Come arrivare" del piede è nascosto sotto i 700 px: resta solo quello della barra fissa (D12).

**Respinti, con il motivo**
- *Foto delle etichette stampate da loro* (bobine, cold foil, multipagina, lavori): non esistono e non si inventano, né con il repertorio né con disegni. Restano il primo punto delle foto da fare nel LEGGIMI ed è il limite principale della pagina.
- *La parola su almeno il 25% dello schermo a 390*: a tutta larghezza una parola di nove lettere in League Gothic è alta 129 px, il 14% dello schermo. Per arrivare al 25% andrebbe spezzata ("Eti-chette") o tagliata fuori dal foglio, e non si leggerebbe più. Il gesto a 390 resta il foglio intero (53% dello schermo).
- *|larghezza della parola - larghezza del foglio| di 8 px al massimo*: la scatola CSS della parola è più larga di 13 px perché comprende i fianchi delle lettere. Conta l'inchiostro, che coincide con la griglia (misura sui pixel qui sopra).

**Clienti tipo** (copie delle prove in `_prova/alto/ritocco/prova-1/` e `prova-2/`): V1 riesce come prima (tutti i fatti in prima schermata, sei settori con il link tra 1052 e 1527 px, PDF dei certificati a un clic dal menu, preventivo fisso in testata, modulo con il file). V2: chiamata, "Manda il file" e "Come arrivare" nella barra fissa; l'orario non è più nella prima schermata ma nel menu, con "da confermare", perché scritto come certo violava il vincolo. V3: "Poche etichette" a 1230 px, il telefono della Stamperia a 1510, "dorate e plastificate" a 1455, consulenza grafica nella stessa sezione.

### Che cosa è cambiato (prima versione ibrida)

- **Apertura di tipografia (modello T).** La parola "Etichette" in League Gothic a 380 px, stampata in quattro passaggi (giallo, magenta, ciano e per ultimo il blu del logo) appena fuori registro, su un foglio di prova con i segni di taglio agli angoli e la barra dei quattro colori. Sotto, nello stesso `h1`, "autoadesive, prodotte a Saonara (Padova)" (la loro frase "Produzione di etichette autoadesive" con il comune) e la riga dei fatti: bobina e foglio, le quattro tecniche, fino a 8 colori, ISO 9001 e FSC. Tutto in CSS, nessun disegno, nessuna animazione.
- **Tolto dalla prima schermata** (capitolo 5): la facciata, l'occhiello "ISO 9001 TÜV NORD dal 2009 · FSC-C146871", il secondo bottone, lo stato e l'indirizzo, la fascia scura dei sei settori. Il logo in testata non è più un link (la home è la home).
- **I compiti spostati.** Il telefono sta nella testata fissa a 1440 (049 879 0566 leggibile) e nella barra fissa in basso sul telefono ("Chiama", con il numero sotto, più "Manda il file" e "Come arrivare"). Il menu nomina quello che il cliente cerca: Etichette, Piccole tirature, Certificati, Contatti. "Richiedi un preventivo" è l'unico bottone della testata.
- **Sotto la piega, la versione professionale rimessa in ordine** su una griglia a 12 colonne (margini 80 px a 1440, bordo destro a 1360 per tutte le sezioni e il piede): i sei tipi di etichetta come righe d'indice con il link alla pagina del settore; La Stamperia di Padova con telefono, sito, email, consulenza grafica e prestampa; il culmine con la facciata a 1280x720 (didascalia "La sede di via Irpinia 51/53, Saonara (Padova)" / "Foto pubblicata sul nostro sito nel 2015"), la frase-firma, i quattro passi dal file alla consegna e l'archivio per le ristampe; la tavola di tecniche e supporti e i due certificati in PDF; il modulo del preventivo completo; contatti e piede in un solo blocco nel blu del marchio.
- **Tolto come riempitivo o ripetizione:** la fascia di cifre grandi (8, 4, 3 e 5, 1200 a 104 px), gli occhielli sopra i titoli, l'elenco dei dati accanto al modulo, "Preferite il telefono?", il terzo riquadro dei certificati (UE 1169/2011 è già nella riga dell'Alimentare e nella tavola), il secondo telefono della Stamperia nel piede, il testo d'interfaccia sopra i 14 px.
- **Tolto perché "da confermare" nel LEGGIMI:** il fax, lo stato "Aperto ora" calcolato (il codice resta in pagina, spento con `MOSTRA_STATO = false`), "clienti in tutto il Nord Italia", "zona artigianale di Villatora" (non trovata nelle fonti). L'orario resta scritto, con "da confermare" accanto (ritocco).
- **Caratteri:** League Gothic 400 (parola e titoli) e Karla 400, 500, 700 (testo), SIL OFL 1.1, in `sito/fonts/` con `OFL-league-gothic.txt` e `OFL-karla.txt`. Esce Mona Sans, già in 8 home. Riga aggiunta in coda a `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (lì il gesto a 390 è scritto "120 px": in pagina è 131 px, il 33,5% della larghezza).
- **Foto:** una sola, la facciata, dal file del loro sito (`assets/originali/2015-11-sld02.jpg`, 1920x720, ricaricato dal loro sito perché `assets/originali/` era andata persa con il riavvio). Un trattamento (`_prova/alto/script/immagini.py`: saturazione 0,88, cielo spento, riflessi arancio riportati all'oro, scritta blu lasciata blu), due tagli: 16:9 a 1280x720 (a 1440 si vede 1:1) e 1:1 a 720 per il telefono. Provini in `_prova/alto/provini.jpg`. Le altre immagini del loro sito e della Stamperia sono di repertorio (`_prova/alto/candidati.jpg`) e non si usano.
- **Frase-firma**: "Etichette uniche per i vostri prodotti, studiate per dargli il giusto valore", dallo slider della loro home (`_prova/alto/uso-crawl/x.html`). Torna due volte con lo stesso trattamento (League Gothic 56): intera sopra la foto del culmine, accorciata ("Etichette uniche per i vostri prodotti.") in testa al piede.

### Misure (misura-d.mjs, 3/11/2026, rifatte dopo il ritocco)

| Soglia | Versione professionale | Ibrida |
|---|---|---|
| Cliccabili nella prima schermata a 1440 (max 6) | 12 | 6 |
| Bottoni a 1440 (max 1) | 4 | 1 |
| Caratteri fuori dal menu a 1440 (max 160) | 410 | 145 |
| Foto nella prima schermata a 1440 (60% o più, oppure sotto il 12%) | 35% | 0% (apertura di tipografia; il foglio di prova occupa il 44%) |
| Cliccabili e bottoni a 390 (max 4 e 1) | 6 e 4 | 4 e 1 |
| Foto o gesto a 390 (almeno 50%) | 24% | 53% |
| Occhielli (max 1) | 4 | 0 |
| `h1` (max 9 parole) | 7 | 6 |
| Parole (max 900) | 996 | 652 |
| Sezioni con il piede (max 7) | 9 | 7 |
| Altezza a 1440 (max 7.500 px) | 7.822 | 7.101 |
| Numeri di 30 px o più (max 1) | 5 | 0 |
| Peso caricato a 1440 (sotto i 3 MB) | 262 KB | 222 KB |
| Fondi oltre il piede (max 3) | 3 | 2 (bianco, grigio chiaro della Stamperia), più il blu del piede |
| Famiglie di caratteri (max 2) | 1 | 2 |

Passano anche: una griglia sola (stesso margine e bordo destro in tutte le sezioni), nessuna foto ingrandita a 320-1920 (il file 1920x720 mostrato a 1216x456 a 1440 e a 1280x480 a 1920), un solo formato, un solo blocco nel colore del marchio, due spazi tra le sezioni (120 e 184 px attorno al culmine), testo della prima schermata a 1440: "Etichette | autoadesive, prodotte a Saonara (Padova) | In bobina e a foglio. | Flexo UV, tipografica UV, offset e digitale. | Fino a 8 colori. | ISO 9001 e FSC.", un solo elemento sopra i 100 px, nessuna istruzione sopra i 14 px, nessun termine della lista nera, nessun link e nessun fatto più di due volte, 3 link `tel:` visibili, nessun U+2014. A 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore di script. Link: `tel:+390498790566`, `tel:+39049640459`, `mailto:info@eveneto.com` con oggetto "Ordine o invio file" e traccia, `mailto:info@lastamperiadipadova.com`, il modulo compone `mailto:info@eveneto.com` con oggetto "Richiesta di preventivo: <azienda>".

### Compiti della scheda d'uso, dove stanno ora

- *V1, 1440*: mestiere, Saonara (Padova), bobina e foglio, le quattro tecniche, 8 colori, ISO e FSC nella prima schermata (y 621-680); i sei tipi di etichetta, ognuno con il link al settore, tra 1.052 e 1.567 px (seconda schermata); "Certificati" nel menu porta alla sezione con i due PDF (4.749 px); "Richiedi un preventivo" fisso in testata, modulo completo con il file.
- *V2, 390*: "Chiama 049 879 0566", "Manda il file" (email con traccia) e "Come arrivare" sempre nella barra fissa in basso; l'orario, con "da confermare", nel pannello del menu e nel piede (dopo il ritocco non è più nella prima schermata).
- *V3, 390*: righe "Dorate e argentate" a 1.190 px, "Poche etichette, o tante varianti?" a 1.357, "Etichette dorate e plastificate" a 1.581, "Chiama La Stamperia di Padova, 049 640459" a 1.637 (tutto entro 1.700); consulenza grafica e prestampa nel testo della stessa sezione, con il link a lastamperiadipadova.com. Sul telefono la sezione mette prima l'elenco e il telefono, poi il testo.

### Problemi aperti

- **La sola foto è la facciata**, 1920x720, ritoccata in origine: regge il culmine a 1280 px ma non un'apertura né uno schermo retina. Le bobine fotografate in reparto (capitolo 5, "sotto, le bobine fotografate in reparto su fondo uniforme") non esistono: senza il servizio fotografico del LEGGIMI la pagina resta senza nessuna etichetta loro stampata, ed è il limite principale per salire oltre il 7.
- **Il gesto non dice un fatto sull'azienda**: i quattro passaggi sono il segno del mestiere (la flexo), non un dato. Non è legato a una loro macchina o a un loro lavoro.
- **Orari ancora da confermare**: in pagina c'è l'orario scritto (2GIS, 2012), sempre con "da confermare" accanto, senza lo stato. Il fax è tolto finché non lo confermano.
- **Prova D1 con le persone** (tre persone, miniatura a 300 px senza logo tra altre cinque della zona) non fatta: va fatta prima dell'ondata.
- **Il modulo** compone ancora un'email e non invia il file (vedi LEGGIMI).
- Lo spazio tra il foglio di prova e la prima sezione: risolto nel ritocco (184 px a 1440).
- La griglia sotto la piega ripete ancora titolo a sinistra e contenuto a destra in cinque sezioni su sei: la rompono solo i settori e il culmine.

---

## Nota di prima (versione professionale)

Pagina: `sito/index.html`, statica, si apre anche con file:///. Immagini in `sito/img/` (solo la facciata della sede, il logo con la cornice e la favicon), caratteri in `sito/fonts/`, i due certificati in PDF (ISO 9001 e FSC, dal loro sito) in `sito/doc/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot, poi i controlli di `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).

Screenshot (stessi nomi di prima): `home-1440.jpg` (7770 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11779 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). La versione 1 com'era prima di questo passaggio (etichetta in lamina oro, settori a schede da cliccare, foto di repertorio) è copiata in `_prova/versione-1-originale/` con la sua nota.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (in due fogli), le pagine intere di barth e Cly-Del a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Che cosa è cambiato

- **Uso prima di tutto.** La versione 1 non aveva ancora l'uso della scheda: niente orari, niente "Manda il file", niente Stamperia, settori nascosti in schede, preventivo verso una pagina senza allegati. Ora:
  - *buyer a 1440*: nella prima schermata il mestiere e il luogo nel titolo ("Produzione di etichette autoadesive a Saonara (Padova)", la loro frase con il comune), la riga dei fatti (bobina e foglio, neutre o personalizzate, flexo UV, tipografica UV, offset e digitale, fino a 8 colori), la prova nell'occhiello (ISO 9001 dal 2009, FSC-C146871), "Richiedi un preventivo" e "Manda il file", il telefono come bottone in testata, gli orari con lo stato, la facciata vera e, sotto la foto, la fascia scura con i sei tipi di etichetta come link. Con uno scorrimento ci sono la fascia e le prime schede (multipagina, bassa migrazione e RFID visibili insieme); poi la tavola di tecniche, colori e supporti; i certificati con anno e licenza; il modulo con il file;
  - *cliente a 390*: senza scorrere "Chiama 049 879 0566" a tutta larghezza, "Manda file o ordine" (email a info@eveneto.com con oggetto e traccia), "Come arrivare" (percorso in Google Maps) e lo stato "Aperto ora / Chiuso, riapre alle..."; il numero resta nella testata fissa a ogni altezza;
  - *piccolo produttore a 390*: nella seconda schermata i sei tipi di etichetta (con "Dorate e argentate") e la porta della Stamperia di Padova, "Poche etichette, o tante varianti?", con "Chiama 049 640459" e il sito; subito sotto "Etichette dorate e plastificate". A 1440 la stessa porta è anche una riga nell'apertura.
- **Struttura M adattata.** Testata sobria con "Richiedi un preventivo"; apertura con la dichiarazione del mestiere e la sede; settori (sei schede); tecniche e numeri su blocco scuro; la Stamperia; come lavoriamo in quattro passi e l'archivio per le ristampe; qualità con i certificati; preventivo con il modulo del mestiere; contatti con le due "sedi" (Etichettificio Veneto e La Stamperia di Padova), ognuna con telefono ed email; piede in quattro colonne.
- **Foto, decisione "niente".** Tolti l'etichetta in lamina col loro logo (fotomontaggio), i vasetti, i flaconi, la striscia di bar code e il nastro in macchina, e con loro la riga "Le immagini della pagina sono indicative". Resta solo la facciata vera, dal file del loro sito (1920x720): dopo il ritocco finale a tutta larghezza nel suo 8:3, in 4:3 sul telefono, mai ingrandita. Nessun disegno al posto delle foto.
- **Colori del marchio, niente beige.** Fondo bianco; blu #233588 della scritta del logo per bottoni, link e blocco dei contatti; blu notte #141C47 (lo stesso blu scurito) per la fascia dei settori, le tecniche e il piede; arancio #F28C00 del filo del logo solo sul blu notte (cifre grandi, titoletti) e nei filetti; verde #1F7A45 solo per "Aperto ora". Grigi freddi.
- **Logo vero.** Il logo con la cornice bianca, il filo arancio e l'angolo sollevato, come lo usano loro, in testata e nel piede (nella versione 1 era ritagliato e ricolorato).
- **Dalla versione 1 tengo:** Mona Sans (una famiglia), il blu del logo, il titolo "Etichette autoadesive" dentro la loro frase completa, i testi verbatim dei settori, la frase dello slider "Etichette uniche per i vostri prodotti, studiate per dargli il giusto valore" in chiusura.

## Ritocco finale (3/11/2026, dopo il controllore e le prove dei clienti)

Il controllore aveva dato 6: pagina ordinata e funzionale, ma con la composizione della campagna (testo a sinistra, foto in un riquadro a destra, B1), nessun gesto di scala, cinque blocchi impilati nell'apertura, schede da modello con un "segno" che ripeteva il nome, e due cifre su quattro spese sugli anni dei certificati. Che cosa è cambiato:

- **Apertura.** A sinistra l'occhiello e il titolo (64 px, su tre righe nelle colonne 1-8); a destra, allineato al fondo del titolo, il sottotitolo, che ora dice anche i supporti ("su carta, carta gommata e polipropilene"). Sotto, solo i due bottoni e una riga di 17 px: stato, orario, indirizzo, "Come arrivare". Niente filetti. Poi **la facciata a tutta larghezza nel suo formato nativo 8:3** (1440x540 a 1440, file da 1920 px, senza raggio): è il gesto di scala della pagina, la lastra dorata piegata come un'etichetta che si stacca. A 390 un taglio 4:3 centrato sulla scritta, a tutta larghezza, dopo i bottoni. Il riquadro 1110x720 di prima non c'è più.
- **Fascia dei settori.** Resta sotto la foto, in blu notte; a 1440 ha una seconda riga con la porta della Stamperia ("Poche etichette o tante varianti? La Stamperia di Padova, la nostra divisione digitale" e 049 640459), tolta dall'apertura. A 390 la Stamperia è già la sezione dopo.
- **Schede dei settori.** Via il "segno" e il fondo grigio: nome a 32 px come primo elemento, filetto blu di 2 px sopra, testo e link sotto, su bianco (come le "Capabilities" di Cly-Del). A 390 una lista compatta: nome, una riga breve, la freccia (circa 90-110 px per voce invece di 260). Il link di "Dorate e argentate" dice dove porta: "Etichette per cosmesi, con cold foil".
- **Ordine.** Le tecniche vengono subito dopo i settori, poi la Stamperia: il buyer trova i supporti al secondo schermo, non al terzo. A 390 l'ordine resta apertura, Stamperia, settori.
- **Numeri.** 8 colori, 4 tecniche, 3 e 5 pagine (multipagina), 1200 dpi (digitale della Stamperia, SCHEDA par. 3). Gli anni dei certificati restano solo nell'occhiello e nelle schede della qualità.
- **Qualità.** Nelle schede ISO 9001 e FSC c'è "Il certificato, in PDF": sono i due PDF del loro sito (TÜV NORD), copiati in `sito/doc/`.
- **Preventivo.** La colonna di sinistra resta ferma accanto al modulo (sticky sopra i 1100 px). Nuovi campi: varianti, consegna desiderata entro, applicazione manuale o automatica; "privato" è solo un suggerimento nel campo Azienda. Sopra il bottone la riga dell'informativa privacy. Nel testo dell'email "File da allegare: nome.pdf" (non più "allegati a questa email"), e l'esito dice anche l'indirizzo da usare se non si apre nessun programma di posta.
- **Contatti e orari.** Tutti i link a info@eveneto.com hanno oggetto e traccia; una sola grafia degli orari (8-12 e 13.30-17.30); la destinazione di Google Maps è "Via Irpinia 51/53". Nello script degli orari c'è un elenco `CHIUSURE` (vuoto) per ferie e ponti: compilato, la pagina dice "Chiuso per ferie, riapre lunedì 23 alle 8" (provato su una copia di prova).

### Esito regola per regola

Misure di `node _prova/script/pro_controlli.mjs` più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: PASSA.** Testata fissa di 80 px a 1440 e 64 a 390, bottone "049 879 0566" alto 48 px, più "Richiedi un preventivo" (la voce "Richiesta" della famiglia M) da 701 px in su. A 390, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 9 link `tel:`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** A 1440x900: H1 con "etichette autoadesive" e "Saonara (Padova)", occhiello "ISO 9001 dal 2009 · FSC-C146871", "Richiedi un preventivo" in testata e nell'apertura. A 390x844: lo stesso, con "Chiama 049 879 0566" largo 350 px (tutta la colonna) a 380 px dall'alto.
3. **Immagine vera nell'apertura: PASSA, con riserva.** La sede vera con la facciata dorata e il logo in rilievo, nel formato nativo 8:3 a tutta larghezza: a 1440 da 587 a 1127 px (la scritta e la piega della lastra nella prima schermata), a 390 in 4:3 da 643 px. Mai ingrandita (1440 px su un file da 1440 e 1920). È una foto 6 su 10, senza persone né mezzi, e a 2x sui monitor retina il file da 1920 px non basta: va rifatta (LEGGIMI, foto 1).
4. **Zero repertorio: PASSA.** "indicativ" 0 volte; in `sito/img/` solo `sede-facciata`, `logo-etichetta` e `favicon`; nessun riferimento a Unsplash o Pexels.
5. **Foto in serie: PASSA.** Una sola foto, un solo formato per larghezza (8:3, 4:3 sul telefono), nessuna didascalia.
6. **Palette dal marchio: PASSA.** Quattro colori (blu, blu notte, arancio, verde solo per "Aperto"), sei neutri; nessun colore scritto fuori da `:root`; nessun token `--carta`.
7. **Scala tipografica corta: PASSA.** 8 misure a 1440 (14, 17, 19, 23, 32, 44, 64, 104) e 8 a 390 (14, 16, 17, 20, 24, 28, 36, 56); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px; H1 64/36 e H2 44/28, nella fascia M.
8. **Al massimo due famiglie: PASSA.** Una sola, Mona Sans, pesi 400 e 650; i titoli in larghezza 112 %, il testo al 100 %; anche modulo e bottoni.
9. **Servizi in schede con la foto: NON PASSA.** Sei schede in tre colonne (due a 768-1100, una lista compatta sul telefono), tutte cliccabili, con il nome a 32 px, il testo verbatim e il link, sotto un filetto blu. Il "segno" che ripeteva il nome è stato tolto. Nessuna foto vera di un loro lavoro: per decisione del committente niente repertorio e niente disegni. Le foto da fare sono nel LEGGIMI (foto 2).
10. **Almeno tre tipi di prova: NON PASSA (2 su 4).** Ci sono quattro numeri in cifre da 104 px (8 colori, 4 tecniche, 3 e 5 pagine, 1200 dpi) e la fascia dei certificati con didascalia e PDF scaricabile (ISO 9001:2015 TÜV NORD, FSC-C146871, regolamento UE 1169/2011). Mancano recensioni e clienti con il nome: non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 5, 6 e 7). I quattro numeri sono del mestiere, non aziendali (persone, metri quadri): da chiedere.
11. **Lavori con un nome: NON PASSA.** Nessun lavoro con cliente, anno e dati nelle fonti (LEGGIMI, punto 6). Al loro posto "Come lavoriamo" e l'archivio per le ristampe.
12. **Ritmo a blocchi: PASSA.** Blocchi pieni oltre al piede: la fascia dei settori e le tecniche in blu notte, i contatti in blu; la Stamperia e la qualità in grigio chiaro; in apertura la facciata a tutta larghezza. Bianco, notte, chiaro si alternano sia a 1440 sia a 390. Spazi di 120 px a 1440 (96 la Stamperia) e 72/64 a 390; contenitore di 1280 px con margini di 80 a 1440, 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 4 px, 56 px (48 in testata), testo 17 px (16 sul telefono, 15 sotto i 360 px); sul blu le stesse due varianti in bianco. Ogni bottone di chiamata ha il numero.
14. **Modulo e "dove" per il mestiere: PASSA.** Modulo M: nome, azienda, email, telefono, settore, materiale, bobina o foglio, misure, quantità, varianti, consegna desiderata, colori e finiture, avvolgimento e anima, applicazione, file grafico, note, riga dell'informativa privacy; controllo dei campi obbligatori con avviso e fuoco. "Indicazioni stradali" e "Come arrivare" aprono il percorso in Google Maps; nessun iframe. Le due sedi (etichettificio e Stamperia) hanno telefono ed email ognuna. Il modulo compone un'email (mailto): va collegato a un servizio (LEGGIMI).
15. **Piede completo: PASSA.** Quattro colonne a 1440 (marchio, Etichette, Servizi e azienda, Contatti), testo di almeno 14 px; ragione sociale, P.IVA e C.F., REA, capitale, indirizzo con il percorso, telefono ed email cliccabili, orari, fax, la Stamperia, ISO 9001 e FSC-C146871, Privacy, Cookie e Accessibilità.

### Compiti della scheda d'uso (par. 8), con `pro_controlli.mjs`

- Buyer, 1440x900: cosa, dove e i supporti nella prima schermata in testo; telefono e "Richiedi un preventivo" senza scorrere, il modulo accetta PDF e AI; multipagina, bassa migrazione e RFID visibili insieme dopo uno scorrimento; tecniche, 8 colori, carta, carta gommata e polipropilene nella stessa tavola; ISO 9001 con la data e FSC con la licenza. Tutto riesce.
- Cliente, 390x844: tel:+390498790566 a un tocco, orari e stato, email con oggetto "Ordine o invio file", indicazioni: tutto nella prima schermata. La testata fissa non copre nulla (la pagina parte sotto di lei e le ancore si fermano sotto la testata). Riesce.
- Piccolo produttore, 390x844: "Poche etichette", "La Stamperia di Padova" e "digitale" nella seconda schermata, tel:+39049640459 a 1527 px e il sito a 1593; "Dorate e argentate" nella fascia e "Etichette dorate e plastificate" nella Stamperia. Riesce.
- Stato degli orari provato a 10 ore e date (`?ora=`): aperto la mattina e il pomeriggio, pausa, prima delle 8, sera, venerdì sera e sabato (riapre lunedì), 8 dicembre, vigilia di Natale sera (salta Natale, Santo Stefano e la domenica: "riapre lunedì 28"), Pasquetta 2027; con l'elenco delle chiusure compilato su una copia di prova, "Chiuso per ferie, riapre lunedì 23 alle 8".
- Modulo provato con `?prova=1` (nessuna email aperta, nulla inviato): invio vuoto fermato con il fuoco sul nome; con i dati e un file l'email ha oggetto "Richiesta di preventivo: Prova Srl", il formato, le misure e "File da allegare: etichetta.pdf"; l'esito dice di allegare il file e l'indirizzo da usare se la posta non si apre.

### Controlli generali

- Nessuno scorrimento orizzontale e nessuna sovrapposizione in testata e apertura a 320, 360, 390, 768, 1024, 1180, 1280, 1440 e 1920 (misure dello script); screenshot guardati a pezzi a 1440 e 390 interi, e a 320, 768 e 1024 (dopo il ritocco finale: la riga dello stato sotto i 1100 px va a capo per voce, l'occhiello non si spezza più dentro "FSC-C146871"). Corretti durante il lavoro: le cifre tabellari di Mona Sans (sembravano di macchina da scrivere, ora proporzionali), il titolo su cinque righe a 390, gli orari spezzati a 320, il campo file con il testo inglese del browser, il menu del telefono (si apre, si chiude al tocco su una voce e con Esc).
- Collegamenti: solo `tel:+390498790566` e `tel:+39049640459`; solo `mailto:info@eveneto.com` (con oggetto) e `mailto:info@lastamperiadipadova.com`; mappe con `google.com/maps/dir/?api=1&destination=Etichettificio Veneto, Via Irpinia 51/53, 35020 Saonara PD`; nessuna ancora senza destinazione; nessun errore di script.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

- **Mona Sans** (GitHub), da Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Servita dalla pagina (`sito/fonts/mona-sans-latin.woff2`, `mona-sans-latin-ext.woff2`, variabile in peso e larghezza), licenza in `sito/fonts/OFL.txt` (le due lineette lunghe della definizione di "Modified Version" sono diventate virgole, per la regola del carattere U+2014; il testo è lo stesso).
- Immagini: solo materiale dell'azienda dal suo sito (facciata `2015-11-sld02.jpg` in 8:3 e 4:3, logo con la cornice, favicon); i PDF dei certificati sono i loro. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.
