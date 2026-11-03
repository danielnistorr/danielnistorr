# Solettificio Tollin, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP, logo PNG), carattere in `sito/fonts/` con la licenza `OFL.txt`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini `pro_img.py`, pagina dal sorgente `pro_index.html`, screenshot `pro_shoot.mjs`, controlli `pro_controlli.mjs` con l'esito in `_prova/pro_controlli.json`; con `--tieni` restano le prove a 320, 768 e 1024 in `_prova/tmp-build/`).

Screenshot (stessi nomi di prima): `home-1440.jpg` (5400 px circa), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8700 px circa), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede).

La versione 1 (il foglio di cartoncino in negativo, 24/10/2026) è copiata com'era in `_prova/versione-1-originale/` (sito, screenshot e la sua nota).

## Livello professionale (3/11/2026)

Richiesta del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; poi "non rappresentano bene l'identità e l'utilizzo corretto"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home) e sezione C (15 regole). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Cly-Del e barth a pezzi; come esempio del livello, la colonna di destra di `_invio/zona/home/livello-professionale.jpg` e le note di Unicar e Panificio Fornasiero.

### Ritocco finale (3/11/2026, dopo il controllo del livello e le prove dei due clienti tipo)

- **Gesto di scala**: i numeri dell'azienda passano da sei a quattro (1970, 12, 4, 9) e da 64 a 120 px, in una fascia a tutta larghezza sotto il titolo e le frasi; a 390 due per due a 64 px.
- **Logo** in testata da 176 a 216 px (150 a 390, prima 124): la scritta SOLETTIFICIO TOLLIN si legge. Il file resta il ritaglio raster: serve il vettoriale.
- **Apertura** nella griglia della testata (la foto non sborda più a destra), alta quanto il testo, tagliata sulle mani; meno giallo nella foto; occhiello a 17 px; a 390 H1 a 36 px e il paese non si spezza.
- **Catalogo**: un solo arancione (il cartoncino uniformato a #B4491E), foto a 128 px con testo alternativo, materiali sopra la griglia; la griglia sta tutta in una schermata dopo uno scorrimento.
- **Spazi**: 96 px sopra il catalogo (prima 64).
- **Bottoni**: telefono in testata 48 px anche sul telefono, testata 72 px a 390; Menu bordato quadrato con le tre righe.
- **Modulo**: campo "Forma o disegno del modello", tipo a tutta larghezza, solo il calzaturificio obbligatorio.
- **Dove siamo** prima del modulo, con il fax; l'indirizzo dell'apertura è un link al percorso; il bottone Scrivi apre la mail con il solo oggetto (il testo guidato resta nel modulo); il piede ha anche Dove siamo e Richiesta.

### Che cosa è cambiato rispetto alla versione 1

- **Via il foglio in negativo.** L'apertura mostrava lo scarto della modelleria, scontornato su fondo carta (la scheda lo vota 3 come apertura; la regola 3 e la B2 lo escludono). Ora c'è la loro foto `supervisione2`: le mani che sistemano i sottopiedi garbati per il tacco nella scatola, in reparto. È l'unica foto con una persona e racconta "controllati dai titolari".
- **Via il beige.** Il fondo carta #F3EFE8 era il "beige di comodo" della sezione B1. Ora: bianco, antracite #1C1D1E per i blocchi scuri, e l'arancione della loro barra del menu e del cartoncino del catalogo (#E0622A), scurito a #B4491E per il testo bianco (5,4:1), come blocco pieno dell'azienda e nei bottoni pieni.
- **Il catalogo torna in pagina.** I nove tipi del loro sito, con la loro foto e il loro nome, in una griglia di tre colonne su antracite: le miniature restano sul loro cartoncino arancione (fondo uniformato allo stesso #B4491E della pagina, il sottopiede non è toccato), a 128 px (sotto la misura d'origine 227 x 367). Tutta la scheda è un link: porta alla richiesta con il tipo già scelto.
- **I quattro reparti a vista**, non più dietro le schede: quattro colonne con la foto 3:2, il nome del reparto e la loro frase, senza caporali. Sotto, la fascia "Le macchine" (Comelz CN, Comelz CM44S, Comec SPM12) con la didascalia di che cosa fanno.
- **Titolo da manifesto tolto.** "Sottopiedi per calzature" resta (sono le parole della loro home), ma a 64 px e non più a 129; nello stesso H1 la riga "da uomo, da donna e da bambino" a 36 px, come in `azienda.html`.
- **Uso**: in prima schermata Chiama, Scrivi (mail con oggetto e traccia) e, sul telefono, Indicazioni sul civico 15; indirizzo, "per ritiri e consegne chiamate prima di passare" (gli orari non sono pubblicati da nessuna parte) e la riga su come si comincia una campionatura. English in testata a 1440 e nel menu a 390.
- **Modulo di richiesta di campionatura** in home, con i campi del mestiere; compone una mail a info@tollin.it (va collegato a un servizio di invio: LEGGIMI).
- **Piede su antracite** in quattro colonne, con il logo in negativo (lettere bianche, impronte verdi).

### Struttura (famiglia M adattata a Tollin)

1. Testata fissa: logo (216 px a 1440, 150 a 390), Sottopiedi, Lavorazioni, Azienda, Richiesta, Dove siamo, English, bottone bordato "049 640620". Sotto i 1100 px le voci vanno nel bottone Menu (quadrato bordato con le tre righe, con English); logo, telefono e Menu restano sempre visibili.
2. Apertura (dichiarazione di competenza e foto delle mani in reparto, nella stessa griglia della testata, alta quanto il testo): occhiello "Solettificio dal 1970 · Villatora di Saonara (PD)", H1, una riga per chi e dove, Chiama / Scrivi (/ Indicazioni sul telefono), indirizzo cliccabile (percorso sul civico 15) e "chiamate prima di passare", come si comincia una campionatura.
3. Prodotti (blocco antracite): titolo, materiali e "non solo sottopiedi" (suole, puntali, contrafforti, tallonette) in una riga, poi i nove tipi in schede con la foto.
4. Competenze e processi: i quattro reparti con foto e la fascia delle macchine.
5. Numeri aziendali (blocco arancione): "Dal 1970, a conduzione familiare" e le due frasi loro sopra, poi quattro numeri a tutta larghezza a 120 px (1970, 12, 4, 9): il gesto di scala della pagina.
6. Dove siamo: indirizzo, Indicazioni e Chiama, orari ("chiamate prima di passare"), consegne con il furgone, email, fax; la foto del furgone giallo TOLLIN davanti al capannone.
7. Richiesta di campionatura: testo, recapiti (telefono, +39, email, fax), modulo.
8. Piede.

Della struttura M mancano i settori, i progetti con il cliente, i clienti con il nome e i certificati: non sono nelle fonti e non si inventano (LEGGIMI).

### Le 15 regole, una per una (dopo il ritocco finale)

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 390 e 1440 accanto ai riferimenti, e le prove a 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (sticky) di 88 px a 1440 e 72 a 390, bottone "049 640620" alto 48 px a tutte le larghezze. A metà pagina, a 390 e a 1440, il bottone si vede e si tocca (`elementFromPoint`). C'è la voce "Richiesta" chiesta per la famiglia M. 6 link `tel:`, tutti `tel:+39049640620`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: occhiello "Solettificio dal 1970 · Villatora di Saonara (PD)" a 17 px, H1 "Sottopiedi per calzature da uomo, da donna e da bambino", la riga "Per i calzaturifici", Chiama a 417 px. 390 x 844: lo stesso (l'occhiello va a capo dopo il punto, il nome del paese non si spezza), Chiama a tutta la colonna (350 x 56) a 369 px, Scrivi e Indicazioni affiancati sotto.
3. **Immagine vera nell'apertura: passa, con il limite delle loro foto.** Le mani che sistemano i sottopiedi garbati nella scatola, in reparto (`supervisione2`, 698 x 465), a 548 x 478 a 1440 (taglio a destra, sulle mani; arriva al fondo del testo, niente più striscia bianca; il file è appena 1,03 volte la misura a schermo in altezza) e a 390 x 260 sul telefono. Dominante gialla ridotta in `pro_img.py`. Va rifatta grande (LEGGIMI).
4. **Zero repertorio: passa.** "indicativ", "unsplash", "pexels" compaiono 0 volte; in `sito/img/` solo foto e logo di Tollin.
5. **Foto in serie: passa, con riserva.** Tutte del loro reparto, stesso trattamento; due formati (3:2 e 227:367 del catalogo); nessuna didascalia; nessuna mostrata oltre la misura del file. Riserva: la luce non è una sola (furgone all'aperto, reparti sotto la luce del capannone, catalogo su cartoncino): è il limite delle loro foto, da rifare (LEGGIMI).
6. **Palette dal marchio: passa.** Quattro colori: `--arancio` #B4491E, `--inchiostro` #1C1D1E, `--bianco`, `--grigio-chiaro` #F0F1F1, più i grigi. Il cartoncino delle nove miniature ora ha lo stesso arancio della pagina (#B4491E, uniformato in `pro_img.py`): in pagina c'è un solo arancione. Nessun beige.
7. **Scala tipografica corta: passa.** 1440: 8 misure (14, 17, 19, 22, 36, 44, 64, 120); 390: 8 (14, 16, 17, 19, 20, 28, 36, 64). Testo corrente 19 px a 1440 e 17 a 390; 14 px solo per occhielli maiuscoli spaziati, titoli del piede e riga legale. H1 64 px a 1440 (fascia M 60-70), 36 px a 390 (fascia 34-40); i numeri a 120 e 64.
8. **Due famiglie al massimo: passa.** Una sola, Commissioner, pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Nove schede in tre colonne a 1440, foto 128 x 207 (prima 120 x 194), il nome e "Chiedete questo tipo"; ogni foto ha ora un testo alternativo che dice che cosa si vede; tutta la scheda sceglie il tipo nel modulo. La griglia (alta 669 px) parte a 990 px a 1440: dopo uno scorrimento di 812, 787 (PagGiù) o 900 px i nove tipi sono tutti interi sotto la testata.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Quattro numeri aziendali a tutta larghezza (1970, 12 persone, 4 reparti, 9 tipi in catalogo; tolti "7 materiali" e "4 altri tagli", che ripetevano la pagina) e la fascia delle macchine con la didascalia. Mancano recensioni, clienti con il nome e certificazioni: non sono nelle fonti e non si inventano (LEGGIMI, punti 8-10).
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti (LEGGIMI, punto 8, con il formato da chiedere).
12. **Ritmo a blocchi: passa.** Due blocchi pieni oltre al piede (sottopiedi su antracite, azienda su arancione) e la richiesta su grigio chiaro; sezioni a 112 px a 1440, ora anche sopra il catalogo 96 (prima 64), 72 a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno arancione e bordato, raggio 3 px, 56 px (48 in testata, anche a 390), testo 16-17 px; il Menu è lo stesso bordato, quadrato di 48 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Campi M: nome, calzaturificio (l'unico obbligatorio, serve per l'oggetto), email, telefono, tipo di sottopiede a tutta larghezza (il tipo scelto non si tronca più), materiale, "Forma o disegno del modello" (lo allego alla mail, ho la forma e chiedo come mandarla, da definire al telefono), modello, numerata e quantità, messaggio. Il mailto non porta allegati: il file si allega alla mail che si apre (scritto sopra il bottone; LEGGIMI per il servizio di invio). Indirizzo con "Indicazioni" (percorso sul civico 15), anche l'indirizzo dell'apertura è un link. Nessun iframe di mappa.
15. **Piede completo: passa, con riserva.** Quattro colonne a 1440 (marchio, Contatti, Sede, Pagine, ora con Dove siamo e Richiesta), testo 17 px e riga legale 14; ragione sociale, P.IVA e C.F., REA, capitale, PEC, indirizzo, telefono, email cliccabili, fax, Privacy e Cookie. Mancano gli orari veri e le certificazioni: non sono nelle fonti (LEGGIMI, punti 1 e 10).

### Compiti della scheda d'uso (par. 8)

- *V1, calzaturificio a 1440*: titolo, "Per i calzaturifici" e la foto vera dei sottopiedi tutti sopra i 900 px; i nove tipi tutti insieme in una griglia alta 669 px, da 990 a 1659 px (uno scorrimento, di rotella o PagGiù, li mostra tutti interi sotto la testata); "Per una campionatura si parte dalla forma del vostro modello: scriveteci tipo, materiale, numerata e quantità" nella prima schermata, con il link al modulo, e "Scrivi a info@tollin.it" apre la mail con un tocco; i quattro reparti a vista, senza clic.
- *V2, telefono a 390*: Chiama `tel:+39049640620` alto 56 px a 369 px (e il bottone della testata, 48 px, sempre visibile); Indicazioni sul civico 15 sotto, e l'indirizzo stesso è un link al percorso; "Dove siamo" (con il fax) ora viene prima del modulo, a 4921 px invece di 6889; "per ritiri e consegne chiamate prima di passare" nella prima schermata; Scrivi con la mail, senza aprire il menu.
- *V3, estero a 1440*: "English" in testata a 17 px, porta alla versione inglese del sito di oggi (`tollin.it/welcome.html`, che esiste); "+39 049 640620" nella richiesta e nel piede, info@tollin.it.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra testata, titolo, testo, bottoni e foto dell'apertura.

### Respinti, con il motivo

- **Recensioni, clienti con il nome, lavori con cliente e anno, certificazioni** (regole 10 e 11): non ci sono nelle fonti; non si inventano.
- **Orari in tabella** (regole 14 e 15): non pubblicati da nessuna parte; al loro posto "chiamate prima di passare".
- **Raggruppare i tipi per uomo, donna e tacco, sandalo, bambino** (SCHEDA par. 6): le fonti dicono a chi è destinato solo il sandalo e il bambino; gli altri gruppi sarebbero inventati.
- **"Cosa mandare" scritto come istruzione** (forma fisica, file, campione): non è nelle fonti; la pagina dice da dove parte la progettazione e il modulo chiede a chi scrive che cosa ha (disegno, forma, da definire).
- **Foto del catalogo a 180 x 290 o più grandi** (cliente 1): il file d'origine è 227 x 367 e a 180 px la griglia supera i 812 px utili a 1440, quindi i nove tipi non si vedrebbero più insieme (compito V1). Portate a 128 x 207; per vederle meglio servono le foto nuove (LEGGIMI).
- **"Dove siamo" spostato solo sul telefono subito dopo i tipi** (cliente 2): l'ordine visivo diverso da quello del codice confonde tastiera e lettori di schermo; al suo posto la sezione viene prima del modulo a tutte le larghezze (a 390 sale di quasi 2000 px) e indirizzo, Indicazioni e "chiamate prima di passare" sono già nella prima schermata.
- **Coordinate o place_id nel link alle indicazioni** (cliente 2): Google non si può aprire da qui; il link resta sull'indirizzo con il civico 15, da provare a mano da un telefono (LEGGIMI).
- **English verso una pagina del sito nuovo**: non esiste ancora; resta la pagina inglese di oggi (LEGGIMI).
- **Illustrazione al tratto al posto delle foto** (A7): esclusa dal committente.

### Caratteri e licenze

- **Commissioner** (Kostas Bartsokas), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file variabile servito dalla pagina (`sito/fonts/commissioner-latin.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700.
- Foto: solo materiale del loro sito (`assets/originali/immagini/`: `supervisione2`, `modelleria1`, `lavorazione2`, `cambratura3`, `supervisione1`, `supervisione3`, `foto1prod`...`foto9prod`) e il logo; da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-9 e 12-15 superate nelle misure (la 5 e la 15 con la riserva scritta sopra); 10 e 11 no. Tutte le prove della scheda superate. Nessuna ancora senza destinazione.
- Link: `tel:+39049640620` ovunque; `mailto:info@tollin.it` con oggetto "Richiesta sottopiedi" (bottone Scrivi anche con la traccia) e quella composta dal modulo; mappe solo `google.com/maps/dir/?api=1&destination=Via Irpinia 15, 35020 Villatora di Saonara PD`.
- Menu a 390 aperto e chiuso col tocco, con English. Modulo vuoto: "Mancano: calzaturificio." con il fuoco sul campo; pieno: mail con tutti i campi, il tipo scelto dal catalogo e la voce sulla forma o il disegno.
- Screenshot guardati a pezzi a 1440 e 390, prime schermate e pagine intere a 320, 768 e 1024.
- Nessun U+2014 in pagina, negli script, nella NOTA, nel LEGGIMI e nei CREDITI.
