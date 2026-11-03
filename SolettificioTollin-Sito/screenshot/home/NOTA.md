# Solettificio Tollin, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP, logo PNG), carattere in `sito/fonts/` con la licenza `OFL.txt`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini `pro_img.py`, pagina dal sorgente `pro_index.html`, screenshot `pro_shoot.mjs`, controlli `pro_controlli.mjs` con l'esito in `_prova/pro_controlli.json`; con `--tieni` restano le prove a 320, 768 e 1024 in `_prova/tmp-build/`).

Screenshot (stessi nomi di prima): `home-1440.jpg` (5400 px circa), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8700 px circa), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede).

La versione 1 (il foglio di cartoncino in negativo, 24/10/2026) è copiata com'era in `_prova/versione-1-originale/` (sito, screenshot e la sua nota).

## Livello professionale (3/11/2026)

Richiesta del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; poi "non rappresentano bene l'identità e l'utilizzo corretto"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home) e sezione C (15 regole). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Cly-Del e barth a pezzi; come esempio del livello, la colonna di destra di `_invio/zona/home/livello-professionale.jpg` e le note di Unicar e Panificio Fornasiero.

### Che cosa è cambiato rispetto alla versione 1

- **Via il foglio in negativo.** L'apertura mostrava lo scarto della modelleria, scontornato su fondo carta (la scheda lo vota 3 come apertura; la regola 3 e la B2 lo escludono). Ora c'è la loro foto `supervisione2`: le mani che sistemano i sottopiedi garbati per il tacco nella scatola, in reparto. È l'unica foto con una persona e racconta "controllati dai titolari".
- **Via il beige.** Il fondo carta #F3EFE8 era il "beige di comodo" della sezione B1. Ora: bianco, antracite #1C1D1E per i blocchi scuri, e l'arancione della loro barra del menu e del cartoncino del catalogo (#E0622A), scurito a #B4491E per il testo bianco (5,4:1), come blocco pieno dell'azienda e nei bottoni pieni.
- **Il catalogo torna in pagina.** I nove tipi del loro sito, con la loro foto e il loro nome, in una griglia di tre colonne su antracite: le miniature restano sul loro cartoncino arancione (fondo uniformato, il sottopiede non è toccato), a 120 px (sotto la misura d'origine 227 x 367). Tutta la scheda è un link: porta alla richiesta con il tipo già scelto.
- **I quattro reparti a vista**, non più dietro le schede: quattro colonne con la foto 3:2, il nome del reparto e la loro frase, senza caporali. Sotto, la fascia "Le macchine" (Comelz CN, Comelz CM44S, Comec SPM12) con la didascalia di che cosa fanno.
- **Titolo da manifesto tolto.** "Sottopiedi per calzature" resta (sono le parole della loro home), ma a 64 px e non più a 129; nello stesso H1 la riga "da uomo, da donna e da bambino" a 36 px, come in `azienda.html`.
- **Uso**: in prima schermata Chiama, Scrivi (mail con oggetto e traccia) e, sul telefono, Indicazioni sul civico 15; indirizzo, "per ritiri e consegne chiamate prima di passare" (gli orari non sono pubblicati da nessuna parte) e la riga su come si comincia una campionatura. English in testata a 1440 e nel menu a 390.
- **Modulo di richiesta di campionatura** in home, con i campi del mestiere; compone una mail a info@tollin.it (va collegato a un servizio di invio: LEGGIMI).
- **Piede su antracite** in quattro colonne, con il logo in negativo (lettere bianche, impronte verdi).

### Struttura (famiglia M adattata a Tollin)

1. Testata fissa: logo, Sottopiedi, Lavorazioni, Azienda, Richiesta, Dove siamo, English, bottone bordato "049 640620". Sotto i 1100 px le voci vanno nel bottone Menu (con English); logo, telefono e Menu restano sempre visibili.
2. Apertura (dichiarazione di competenza e foto delle mani in reparto): occhiello "Solettificio dal 1970 · Villatora di Saonara (PD)", H1, una riga per chi e dove, Chiama / Scrivi (/ Indicazioni sul telefono), indirizzo e "chiamate prima di passare", come si comincia una campionatura.
3. Prodotti (blocco antracite): i nove tipi in schede con la foto; materiali e "non solo sottopiedi" (suole, puntali, contrafforti, tallonette).
4. Competenze e processi: i quattro reparti con foto e la fascia delle macchine.
5. Numeri aziendali (blocco arancione): "Dal 1970, a conduzione familiare", due frasi loro, sei numeri (1970, 12, 4, 9, 7, 4).
6. Richiesta di campionatura: testo, recapiti (telefono, +39, email, fax), modulo.
7. Dove siamo: indirizzo, Indicazioni e Chiama, orari ("chiamate prima di passare"), consegne con il furgone, email; la foto del furgone giallo TOLLIN davanti al capannone.
8. Piede.

Della struttura M mancano i settori, i progetti con il cliente, i clienti con il nome e i certificati: non sono nelle fonti e non si inventano (LEGGIMI).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 390 e 1440 accanto ai riferimenti, e le prove a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (sticky) di 88 px a 1440 e 64 a 390, bottone "049 640620" alto 48 px (44 sul telefono). A metà pagina, a 390 e a 1440, il bottone si vede e si tocca (`elementFromPoint`). C'è anche la voce "Richiesta" chiesta per la famiglia M. 6 link `tel:`, tutti `tel:+39049640620`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1 "Sottopiedi per calzature da uomo, da donna e da bambino", occhiello con Villatora di Saonara (PD) e "dal 1970", la riga "Per i calzaturifici", Chiama a 429 px. 390 x 844: lo stesso, Chiama a tutta la larghezza della colonna (350 px, alto 56) a 356 px, Scrivi e Indicazioni affiancati sotto.
3. **Immagine vera nell'apertura: passa, con il limite delle loro foto.** Le mani che sistemano i sottopiedi garbati nella scatola, in reparto (`supervisione2`, 698 x 465 dopo il taglio delle bande nere), a 634 px a 1440 e a 390 sul telefono: mai ingrandita. È una foto del 2016 o prima, a 850 px d'origine: va rifatta (LEGGIMI). Nessuna illustrazione, per scelta del committente.
4. **Zero repertorio: passa.** "indicativ" compare 0 volte; in `sito/img/` solo foto e logo di Tollin.
5. **Foto in serie: passa.** Tutte del loro reparto, con lo stesso trattamento (bilanciamento del bianco comune, saturazione 0,9, rumore JPEG tolto: `finale_img.py`); due formati (3:2 per apertura, reparti e furgone; 227:367 per le miniature, che sono la loro serie di catalogo sul cartoncino arancione); nessuna didascalia; nessuna ingrandita oltre la misura del file.
6. **Palette dal marchio: passa.** Quattro colori: `--arancio` #B4491E (barra del menu e cartoncino del catalogo), `--inchiostro` #1C1D1E, `--bianco`, `--grigio-chiaro` #F0F1F1 (solo il fondo della richiesta), più i grigi di testo e filetti. Nessun beige. Il verde delle impronte resta nel logo.
7. **Scala tipografica corta: passa.** 1440: 7 misure (14, 17, 19, 22, 36, 44, 64); 390: 8 (14, 16, 17, 19, 20, 28, 34, 44). Testo corrente 19 px a 1440 e 17 a 390; 14 px solo per occhielli maiuscoli spaziati, titoli del piede e riga legale. H1 64 px a 1440 (fascia M 60-70), 34 px a 390 (fascia 34-40); H2 44 e 28.
8. **Due famiglie al massimo: passa.** Una sola, Commissioner, pesi 400 (titoli, testo, numeri) e 700 (nomi delle schede, bottoni, occhielli).
9. **Servizi in schede con la foto: passa.** Nove schede in tre colonne a 1440 (tre anche tra 860 e 1100 px, lista a una colonna sul telefono), tutte con la loro foto di catalogo nello stesso taglio, il nome e "Chiedete questo tipo"; tutta la scheda è cliccabile e sceglie il tipo nel modulo (provato a 1440 e 390: "Per sandalo con incastri a ragno").
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono sei numeri aziendali (1970, 12 persone, 4 reparti, 9 tipi, 7 materiali, 4 altri tagli) e la fascia delle macchine con la didascalia (i fornitori delle loro macchine, come Wilson con Reece). Mancano recensioni (zero in tutte le schede pubbliche), clienti con il nome e certificazioni: non sono nelle fonti e non si inventano (LEGGIMI).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti; Tollin non ha mai nominato un cliente (LEGGIMI).
12. **Ritmo a blocchi: passa.** Due blocchi pieni oltre al piede (sottopiedi su antracite, azienda su arancione) e la richiesta su grigio chiaro; sezioni a 112/112 px a 1440 (64 sopra il catalogo, che segue l'apertura) e 72/72 a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno arancione e bordato, raggio 3 px, 56 px (48 e 44 in testata), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Campi M: nome, calzaturificio, email, telefono, tipo di sottopiede (i nove più "suole, puntali, contrafforti o tallonette"), materiale (i sette), modello, numerata e quantità, messaggio; il disegno o il file si allegano alla mail che si apre (un mailto non porta allegati: è scritto sopra il bottone). Il modulo vuoto si ferma con l'avviso e il fuoco sul primo campo; pieno compone la mail con oggetto "Richiesta di campionatura, <calzaturificio>". Indirizzo con "Indicazioni" (Google Maps, percorso sul civico 15). Nessun iframe di mappa.
15. **Piede completo: passa, con riserva.** Quattro colonne a 1440 (marchio, Contatti, Sede, Pagine), testo di 17 px e riga legale di 14; ragione sociale, P.IVA e C.F., REA, capitale, PEC, indirizzo, telefono, email cliccabili, fax, Privacy e Cookie. Mancano gli orari veri (non pubblicati: c'è "Ritiri e consegne: chiamate prima di passare") e le certificazioni (nessuna nelle fonti).

### Compiti della scheda d'uso (par. 8)

- *V1, calzaturificio a 1440*: titolo, "Per i calzaturifici" e la foto vera dei sottopiedi tutti sopra i 900 px; i nove tipi tutti insieme in una griglia alta 620 px circa, che comincia a 838 px (uno scorrimento); "Per una campionatura si parte dalla forma del vostro modello: scriveteci tipo, materiale, numerata e quantità" nella prima schermata, con il link al modulo, e "Scrivi a info@tollin.it" apre la mail con un tocco; i quattro reparti a vista, senza clic.
- *V2, telefono a 390*: Chiama `tel:+39049640620` alto 56 px a 356 px (e il bottone della testata, 44 px, sempre visibile); Indicazioni sul civico 15 a 422 px; "per ritiri e consegne chiamate prima di passare" nella prima schermata; Scrivi con la mail, senza aprire il menu.
- *V3, estero a 1440*: "English" in testata a 17 px, porta alla versione inglese del sito di oggi (`tollin.it/welcome.html`, che esiste); "+39 049 640620" nella richiesta e nel piede, info@tollin.it.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra testata, titolo, testo, bottoni e foto dell'apertura.

### Respinti, con il motivo

- **Recensioni, clienti con il nome, lavori con cliente e anno, certificazioni** (regole 10 e 11): non ci sono nelle fonti; non si inventano.
- **Orari in tabella** (regole 14 e 15): non pubblicati da nessuna parte; al loro posto "chiamate prima di passare".
- **Raggruppare i tipi per uomo, donna e tacco, sandalo, bambino** (SCHEDA par. 6): le fonti dicono a chi è destinato solo il sandalo e il bambino; gli altri gruppi sarebbero inventati. Restano nell'ordine del loro catalogo.
- **"Cosa mandare" scritto come istruzione** (forma fisica, file, campione): non è nelle fonti; la pagina dice da dove parte la progettazione (la forma del modello) e chiede di telefonare per come mandarla.
- **La foto della scatola senza le scritte del materiale**: niente più ritocco (si vedeva); la foto è com'è, con "Tecno-Sint" sulla pianta. Se non si può mostrare, va rifatta (LEGGIMI).
- **Dove siamo e orari subito dopo i tipi sul telefono** (SCHEDA par. 4): sul telefono indirizzo, Indicazioni e "chiamate prima di passare" sono già nella prima schermata; spostare la sezione solo sul telefono avrebbe separato l'ordine visivo da quello della tastiera.
- **Illustrazione al tratto al posto delle foto** (A7): esclusa dal committente.

### Caratteri e licenze

- **Commissioner** (Kostas Bartsokas), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file variabile servito dalla pagina (`sito/fonts/commissioner-latin.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700.
- Foto: solo materiale del loro sito (`assets/originali/immagini/`: `supervisione2`, `modelleria1`, `lavorazione2`, `cambratura3`, `supervisione1`, `supervisione3`, `foto1prod`...`foto9prod`) e il logo; da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-9 e 12-15 superate nelle misure (la 15 con la riserva scritta sopra); 10 e 11 no. Tutte le prove della scheda superate. Nessuna ancora senza destinazione.
- Link: `tel:+39049640620` ovunque; `mailto:info@tollin.it` con oggetto "Richiesta sottopiedi" (bottone Scrivi anche con la traccia) e quella composta dal modulo; mappe solo `google.com/maps/dir/?api=1&destination=Via Irpinia 15, 35020 Villatora di Saonara PD`.
- Menu a 390 aperto e chiuso col tocco, con English.
- Screenshot guardati a pezzi a 1440 e 390, prime schermate e pagine intere a 320, 768 e 1024.
- Nessun U+2014 in pagina, negli script, nella NOTA, nel LEGGIMI e nei CREDITI.
