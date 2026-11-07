# Argenteria Varotto Alfredo, home HE (7 novembre 2026)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css, he.js e vendor/ identici a `_metodo/highend/kit/`), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (34 file, due misure per pezzo). Cartella `sito-he` 1,2 MB. La `sito/` di oggi non è toccata. Direzione artistica in `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8784`, server fermato), `foglio-1440.jpg` (21 fotogrammi) e `foglio-390.jpg` (22), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` (5) e `fotogrammi-pieni-390-*.jpg` (3) a piena misura estratti dal video con ffmpeg, `prima-schermata-1440.jpg` e `-390.jpg`, `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `ArgenteriaVarotto-Sito`; legge `assets/originali/alta/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (esito in `_prova/he/prove-finale.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; viste di lavoro con `node _prova/he/script/vedi.mjs`; riferimenti con `node _prova/he/script/riferimenti.mjs _prova/he/riferimenti nome=url ...`.

## Idea

**Tutta la tavola, in argento, un pezzo alla volta.** Ogni pezzo del loro catalogo sta da solo sul campo chiaro, alla misura della sua foto, con il nome e il codice, come nella vetrina di una maison. La pagina si apre come un astuccio: prima schermata blu (il blu del marchio), una finestra chiara con le posate Inglese in argento massiccio, il titolo in crema; scorrendo la finestra si apre fino alla pagina e il titolo, fermo, diventa nero.

## Sezioni (scheletri diversi, composizioni alternate)

1. **Apertura, "Tutta la tavola, in argento."** (blu, fissata sopra i 900 px): titolo in Rowan a 150 px a sinistra, finestra alta a destra con le posate e la loro etichetta (BL83006, BL83001), riga del mestiere e due collegamenti (riparazione, hotel e ristoranti). Gesto: la finestra si apre (`data-he-scale`, `data-he-scale-zoom="1"`, nessun ingrandimento della foto), il titolo passa dal crema al nero per fusione "differenza". Sul telefono: blu con titolo e riga, sotto la finestra con le posate, ferma.
2. **Firma, la vetrina "Argento massiccio"** (carta): tre ripiani di filetto. Sul primo il candelabro a cinque fiamme a sinistra e il titolo a 196 px a destra, in piedi sul ripiano come un pezzo (sale riga per riga); sul secondo brocca martellata, coppa, bicchiere, candeliere; sul terzo servizio Impero, secchiello e lo shop. Sotto ogni pezzo nome, materiale e stile, codice.
3. **999, le impugnature** (carta): il numero a 374 px a sinistra, la testa di leone a destra che si scopre dal basso (`data-he-wipe`); sotto, sei teste nella stessa finestra (cavallo, civetta, cobra, anatra, labrador, teschio) con il codice.
4. **Riparazione** (sull'inchiostro, come l'argento sul panno scuro): la loro frase "La vostra argenteria tornerà al suo originario splendore." in Plein a 68 px, i cinque materiali in righe grandi color argento a sinistra, a destra come si fa in tre frasi, "Mandate le foto del pezzo" (email già compilata) e "Chiamate", una riga in inglese.
5. **Hotel e ristoranti**: sottopiatto e vassoio tondi visti dall'alto a sinistra, a destra il testo e quattro strade (preventivo per quantità, Area clienti, export@, riargentatura), "Scrivete la richiesta".
6. **Alfredo Varotto**: due ovali con i titoli 925 e 800, come impressi sull'oggetto, e accanto la citazione della pagina Azienda (senza la data) e la frase sui titoli impressi.
7. **Contatti**: il telefono a 124 px da toccare; dove siamo con la mappa, "Orari: non sono pubblicati. Prima di passare, chiamate."; email, export, fax; lo shop e il suo WhatsApp per le domande sugli articoli; "Writing from abroad" in inglese; accanto il modulo "Scrivete la richiesta", che prepara l'email come la versione di oggi.
8. **Piede** (inchiostro): Varotto & Co. di Varotto Luca, indirizzo, P.IVA, telefono e fax; note su privacy e cookie; Area clienti, shop, sito inglese di oggi.

## Caratteri e colore

- **Rowan** 300 (ITF, Fontshare) solo nei tre momenti forti: titolo d'apertura 150 px a 1440 e 64 a 390, "Argento massiccio" 196 / 64, "999" 374 / 172 (cifre antiche); più gli ovali 925 e 800, piccoli. **Plein** 400 e 500 (ITF, Fontshare) per tutto il resto, cifre allineate. Riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (nessuna altra home con queste famiglie). Supreme, prima scelta per il testo, è uscito: il paragrafo d di `_metodo/CARATTERI-E-SEGNALI-IA.md` lo nomina e lo ha tolto dalla guida.
- Carta #F3F2EE, inchiostro #121416 (testo, e campo pieno della riparazione e del piede), grigio #5C6066, blu astuccio #0E2140, l'unico colore pieno, solo nell'apertura, crema #F1DEBF (il negativo del blu, il titolo sul blu), argento #C9CCD1 per i materiali e i testi sull'inchiostro. Nessun corsivo, nessuna etichetta sopra i titoli, maiuscolo spaziato solo nel marchio.

## Foto

**Originali più grandi: trovati.** Ogni miniatura delle pagine di categoria del sito di oggi apre `immagine.asp?PathImm=<nome>`, che mostra il file di `immaginiAltaRisoluzione/<nome>.jpg`: le miniature erano di 100-500 px, gli originali fino a 1280 px (e una brocca Royal Queen a 1869x2121). Dalle 312 pagine di categoria in italiano ho letto 9.620 schede e scaricato le 1.165 dei marchi Varotto Alfredo, Royal Queen e Royal England (93 MB, `assets/originali/alta/`, fuori da git); più le 70 immagini delle pagine principali e della versione inglese (`assets/originali/sito/`; la versione inglese usa gli stessi file). Provini numerati in `_prova/he/` non salvati: le scelte sono in `_prova/he/immagini.json`.

Trattamento unico (`_prova/he/script/immagini.py`): campo piatto (fondo dello studio stimato con un polinomio e portato a bianco), per i due pezzi tondi il fondo fuori dal profilo portato a bianco, saturazione al 30 %, una curva leggera uguale per tutti, ritaglio sul pezzo con la base che tocca il ripiano; in pagina in "moltiplica" sulla carta. Guardate al 100 % a 1440 prima di sceglierle: catalogo nitido ma con artefatti JPEG, quindi mai oltre 0,95 della misura nativa.

| In pagina | Originale (`immaginiAltaRisoluzione/`) | Ritaglio nativo | A 1440 (rapporto) |
|---|---|---|---|
| Posate, apertura | Posto tavola in argento massiccio 6 pezzi stile Inglese classico BL83006, 1278x1280 | 802x1275 | 362 px di larghezza (0,45) |
| Candelabro 5 fiamme | VAG-Z1595.30, 940x1280 | 961x1256 | 424 (0,44) |
| Brocca martellata | BB01200AG, 1280x1245 | 575x763 | 271 (0,47) |
| Coppa champagne e gelato | VAG-01149, 990x1280 | 818x1048 | 313 (0,38) |
| Bicchiere bimbo | VAG-Z1637.06, 1280x857 | 502x573 | 193 (0,38) |
| Candelabro 1 fiamma | VAG-Z1593-28, 589x1280 | 509x1106 | 219 (0,43) |
| Servizio 4 pezzi Impero | VAG-Z2501, 1280x957 | 1263x780 | 621 (0,49) |
| Secchiello ghiaccio | VAG-Z1617, 1126x1280 | 1017x1146 | 311 (0,31) |
| Leone (impugnatura) | BT00030AX, 1280x1280 | 588x700 | 500 (0,85; 0,95 a 1920) |
| Sei teste | BT00040AX, BT00050AX, BT00101AX, BT00090AX, BT00021AX, BT00120AX, 1280x1280 | da 630 a 960, file a 400 | 201 (0,5 del file; 220 a 1920) |
| Sottopiatto | SS01510AG, 1280x1165 | 1340x1225 | 441 (0,33) |
| Vassoio piatto tondo | VAG-P1165.40, 1280x1008 | 1300x1068 | 433 (0,33) |

Nessuna foto a tutta pagina: il campo che si apre nell'apertura è colore, la foto resta alla sua misura. Nessuna immagine di repertorio, nessuna immagine generata.

## Misure e prove (sezione 6)

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", larghezza del documento uguale alla finestra, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (5.220 caratteri a 1440, 5.162 a 390), nessun elemento nascosto. L'apertura resta nella composizione di partenza (blu, titolo crema, posate nella finestra); vale anche senza JavaScript.
- **Peso al primo caricamento** (senza scorrere): da 391 a 432 KB a 1440 secondo la corsa e 432 KB a 390 (soglie 2,5 e 1,5 MB); 445 a 768, 551 a 1024, 432 a 1920. Posate e due caratteri precaricati, tutte le altre immagini pigre. Pagina intera con tutte le foto: circa 1,2 MB.
- **Layout stabile**: CLS 0 o 0,0004 a tutte le larghezze, con e senza movimento; con la rotella 0,0002 a 1440 e 0 a 1920. L'apertura fissata usa `pinType: "transform"`, impostato nella pagina prima di `he.js`.
- **Funzioni**: `tel:` in testata (a 1440 il numero, sul telefono "Chiama", aree di 44 px) e cinque volte nella pagina; email generale, export, email della riparazione con oggetto e traccia, email del preventivo per quantità; indirizzo con Google Maps; orari: non pubblicati, scritto così; modulo "Scrivete la richiesta" (prepara l'email a info@ come la versione di oggi); riparazione in testata, nella prima schermata e in una sezione; Area clienti; shop e WhatsApp dello shop; "Writing from abroad" in inglese con export@ e "EN" in testata; ragione sociale, P.IVA, note privacy e cookie nel piede.
- **Controllo d'uso dal telefono**: in prima vista il titolo, che cosa fanno e dove ("Argenteria Varotto Alfredo, Padova", tavola, hotel e ristoranti, riparazione), "Riparare un argento", "Chiama" e "Contatti" in testata; l'indirizzo con la mappa a un tocco.
- U+2014: nessuno, nella pagina, negli script, nella direzione, nel registro e in questa nota.

## Giudizio da solo (griglia della sezione 7 e lezioni della sezione 8)

Guardati il foglio a 1440 e a 390, le prime schermate, cinque fotogrammi a piena misura a 1440 (4,4 s il gesto a metà, con il titolo metà crema e metà nero; 7,3 s la vetrina; 10,6 s il 999 e il leone; 13,4 s la riparazione; 16,4 s i contatti) e tre a 390, accanto alle prime schermate di Puiforcat, Christofle, Georg Jensen, Buccellati, Broggi, Greggio, Kevala e Artisans de Genève.

- **Design 8,2**: l'idea sta nel display ("Tutta la tavola, in argento."), un display vero usato tre volte oltre i 140 px, un solo trattamento delle foto, composizioni alternate (apertura testo e pezzo, vetrina pezzo e titolo, 999 numero e pezzo). Limiti: riparazione e hotel sono corretti ma più ordinari della prima metà; le foto di catalogo, guardate da vicino, hanno artefatti.
- **Creatività 8,0**: l'astuccio blu che si apre con il titolo che cambia colore senza muoversi non somiglia a un modello; il titolo in piedi sul ripiano come un pezzo; il 999 accanto al leone. La vetrina a ripiani è una tipologia nota (Greggio, Puiforcat), salvata dalla scala del titolo.
- **Usabilità 8,4**: il mestiere in cinque secondi, il numero sempre in testata, la riparazione a un tocco dalla prima schermata, il movimento breve, il telefono progettato (apertura riorganizzata, ripiani a due pezzi, teste in tre colonne), contatti in inglese.
- **Contenuto 8,3**: nomi e codici veri del catalogo, frasi loro (Assistenza, Azienda), nessun fatto da confermare.

Media pesata circa 8,2. La sezione 8 avverte che l'autovoto è in media 0,7 sopra quello del giudice: il voto atteso è tra 7,5 e 8. Correzioni fatte dopo aver guardato fotogrammi e schermate: la moltiplica del leone non funzionava dentro il taglio (rettangolo bianco: spostata sul contenitore del taglio); tre sezioni di fila avevano testo a sinistra e pezzo a destra (il primo ripiano è stato rovesciato); sul telefono la finestra con le posate stava sopra il titolo (ora sotto) e il leone sopra il 999; il fondo grigio del sottopiatto e del vassoio restava visibile in moltiplica (portato a bianco fuori dal profilo); i colli dell'anatra e del labrador erano tagliati troppo in alto; "Contatti" era doppio in testata a 1440; i bottoni della riparazione stavano lontani dai passi; i contatti erano lunghi quattro schermate (ora dati e modulo in due colonne); i codici andavano a capo; le cifre antiche di Plein nei codici (ora allineate); apostrofi tipografici. Dopo aver riletto le lezioni aggiornate della sezione 8: la riparazione, corretta ma più debole della prima metà, è passata sull'inchiostro (sotto la piega la pagina resta all'altezza della prima schermata); tolte tre frasi di raccordo non nelle fonti ("il suo stile", "due righe su che cosa è successo", "quello che la sala consuma", sostituita con la loro frase sulla rimessa a nuovo).

Quanto della distanza da un 9 dipende dalle foto: circa metà. La pagina regge perché le foto sono mostrate a metà della loro misura, su un campo che le unifica; con un servizio still life vero (stesso fondo, stessa luce, 4000 px) i pezzi potrebbero crescere, la vetrina diventerebbe una serie e il leone sarebbe nitido a tutta altezza.

## Problemi aperti

- **Fatti lasciati fuori perché da confermare** (LEGGIMI 7 e 8, analisi sez. 9): il punzone 364 PD e la produzione nello stabilimento di Padova, il 1974, gli orari. Il titolo non dice "fabbrica". Se l'azienda conferma, il 364 PD può entrare negli ovali della sezione 6 e "dal 1974" nella riga d'apertura.
- **Diritti delle foto**: sono del sito di oggi e del catalogo; alcune potrebbero essere dei fornitori (per esempio le cornici con altri marchi, non usate). Le impugnature sono "Novità" del marchio Varotto Alfredo: chi le produce va chiesto.
- **Codici e misure**: in pagina ci sono i codici del catalogo, non le misure; i codici con un numero finale (VAG-Z1595.30, VAG-P1165.40) potrebbero essere le misure in centimetri: da chiedere prima di scriverle.
- **Area clienti**: porta all'area riservata di oggi (`area-clienti.asp`); LEGGIMI punto 12.
- **Privacy e cookie**: note nella pagina; servono pagine vere con l'informativa nuova (quella di oggi cita il D.Lgs. 196/2003).
- **Retina**: tutte le foto sono a metà della misura nativa o meno, quindi nitide a doppia densità, tranne il leone (0,85).
- **Caratteri ITF**: la licenza permette di ospitarli ma non di ridurli: tre file, 56 KB.
- **Modulo**: prepara un'email (`mailto:`), non invia da sé; con il sito vero va collegato a un servizio di invio con gli allegati (LEGGIMI).

## Foto da rifare (in ordine di valore)

1. **Un servizio still life dei pezzi in argento massiccio**, 10-12 pezzi scelti con l'azienda (posate Inglese, candelabri, brocca martellata, coppa, secchiello, servizio Impero), stesso fondo chiaro, stessa luce morbida da un lato, camera alla stessa altezza e distanza (così i pezzi stanno davvero alla stessa scala sul ripiano), 4000 px. È il guadagno più grande: la vetrina resta uguale e diventa una serie vera.
2. **Le posate Inglese per l'apertura**, a 4000 px, dall'alto, con un poco di ombra, più una versione nell'astuccio blu aperto: l'apertura potrebbe partire dalla foto vera dell'astuccio.
3. **Il leone e le teste delle impugnature** a 4000 px, su fondo chiaro, luce che legga il cesello senza bruciare i riflessi; ogni testa tagliata alla ghiera.
4. **I titoli impressi**: macro del 925 o dell'800 e del marchio impressi su un pezzo, luce radente, obiettivo macro 1:1 (con il 364 PD, se confermato). Prenderebbe il posto degli ovali disegnati.
5. **La riparazione**: un pezzo rovinato com'è arrivato, il lavoro al banco (lucidatura, argentatura), lo stesso pezzo finito, 3:2, stessa luce. Oggi la sezione è solo tipografia.
6. **Un buffet o una sala d'hotel** allestiti con i loro pezzi, con il permesso di nominare l'hotel: il lavoro con un nome che manca.
7. **La sede** di Corso Stati Uniti 23/A, facciata e ingresso, per i contatti.
