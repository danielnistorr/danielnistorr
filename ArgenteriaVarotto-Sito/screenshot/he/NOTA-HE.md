# Argenteria Varotto Alfredo, home HE (7 novembre 2026, giro di ritocco dopo il 7,2)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css, he.js e vendor/ identici a `_metodo/highend/kit/`), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (28 file, due misure per pezzo). Cartella `sito-he` 1,2 MB. La `sito/` di oggi non è toccata. Direzione artistica in `DIREZIONE-HE.md` (scritta prima del primo giudizio: dove questa nota e la direzione non coincidono, vale questa nota).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8787`, server fermato), `foglio-1440.jpg` (21 fotogrammi) e `foglio-390.jpg` (22), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-3.6/10.3/14.3/16.3.jpg` e `fotogrammi-pieni-390-2.5/9.5/14.5.jpg` a piena misura estratti dal video con ffmpeg, `prima-schermata-1440.jpg` e `-390.jpg`, `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `ArgenteriaVarotto-Sito`; legge `assets/originali/alta/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (esito in `_prova/he/prove-finale.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; viste di lavoro con `node _prova/he/script/vedi.mjs`; riferimenti con `node _prova/he/script/riferimenti.mjs _prova/he/riferimenti nome=url ...`.

## Giro di ritocco (giudizio 7,2: "un catalogo online molto curato, non un'argenteria di fascia alta")

1. **Apertura, la mossa Kevala.** Con il movimento, da 900 px in su, l'astuccio parte socchiuso: una fessura chiara sul blu che mostra solo il coltello e il cucchiaio (`data-he-scale` e `.he-moto .apertura .campo`, stessa regola; a 1440x900 `inset(9% 18% 9% 69.4%)`). La fessura si misura sulla foto in un piccolo script nella testa della pagina, con la stessa geometria del CSS, così a ogni finestra taglia a metà degli spazi tra forchetta e coltello e tra cucchiaio e cucchiaino (provata a 1024, 1440, 1920); la classe `pre-moto` la disegna prima che parta il kit, senza salti. Scorrendo l'astuccio si apre fino alla pagina: arrivano la forchetta e il cucchiaino, che prima non si vedevano, e il titolo passa dal crema al nero. L'etichetta è nascosta da 900 px in su. Con "riduci movimento" (e senza JavaScript) resta la finestra intera con le quattro posate, senza etichetta: nessun pezzo nascosto. Sul telefono la finestra resta ferma sotto il titolo, con un'etichetta corta ("Posto tavola 6 pezzi, stile Inglese", BL83006).
2. **Impugnature.** Il leone sta in 8/11, accanto al 999, con la base del collare sulla base delle cifre (il padding del 999 è in em, quindi l'allineamento tiene a ogni larghezza); didascalia sotto, fuori dal flusso. Il giudice proponeva `clamp(200px,22vw,320px)`: al 100% su schermo retina simulato (densità 2) il leone era ancora morbido (634 px di schermo da un file di 588), quindi è sceso a `clamp(200px,18vw,260px)`: 259 px a 1440, 0,44 della misura del file, più un mediano di 3 px nello script per ammorbidire i blocchi JPEG del catalogo. Sul telefono `min(50vw,240px)`. Fuori dalla fila anatra e teschio: quattro teste in 4 colonne (2 sul telefono), ora a 260 px da file di 520 (ritagli nativi da 630 a 960 px).
3. **Didascalie.** Via "Argento massiccio," da tutte le nove: nome e stile come nel catalogo su una riga ("Brocca martellata, stile Inglese"), il codice sotto a 12 px; la coppa ha solo il nome. Nella fila solo i nomi. In cima alla vetrina la citazione della pagina Azienda, con la fonte: "La produzione consiste in [...] vassoi, piatti, sottopiatti, [...] servizi da caffè, zuccheriere, alzate, centri tavola, [...] secchielli champagne e ghiaccio, vasi, brocche, caraffe, [...] candelabri, bugie, bicchierini, calici, coppe champagne e gelato, [...] posate."
4. **Frasi fuori fonte.** Tolte: "Ogni pezzo ha il suo nome e il suo codice..." (al suo posto la citazione), "lisce, a torciglione, floreali" (ora "animali, teschio, liberty", come la voce Novità dell'analisi), "interno dorato" (didascalia e testo alternativo; è nel nome del file del catalogo, ma non nelle fonti lette dal giudice), "Silverware for the table..." (ora "We can refurbish products coming from hotels, restaurants and catering.", dal loro sito inglese). Riavvicinate al testo della pagina Assistenza la riga sotto il titolo della riparazione e il primo passo ("È sufficiente contattare il 049 870 07 09 o mandare una mail a info@varottoalfredo.com"). **Restano, perché sono nel loro sito inglese** (letto il 7/11/2026, copie in `_prova/he/crawl-en/`): "Varotto Alfredo Silverware" (intestazione di `english/contatti-informazioni.asp` e piede di ogni pagina inglese, "VAROTTO ALFREDO SILVERWARE") e "Our experience will restore your silverware to its former beauty." (`english/area-agenti.asp`).
5. **Hotel e storia.** In `.hotel` il testo a sinistra (1/6), i due pezzi tondi a destra (6/13); sul telefono prima il testo. In `.storia` via gli ovali 925 e 800: la citazione su 3/11, la prima frase (Alfredo Varotto) a 30 px, la seconda (titolo e marchio impressi) più piccola, la fonte sotto.
6. **Shop.** Via il bottone "Apri lo shop" dalla vetrina: il secchiello passa a 7/11. Lo shop resta in testata (da 1200 px), nei contatti ("Lo shop", varottoshop.com e il WhatsApp dello shop) e nel piede. Nei contatti via "Orari: non sono pubblicati."; resta "Prima di passare, chiamate."

## Idea

**Tutta la tavola, in argento, un pezzo alla volta.** Ogni pezzo del loro catalogo sta da solo sul campo chiaro, alla misura della sua foto, con il nome e il codice, come nella vetrina di una maison. La pagina si apre come un astuccio socchiuso: prima schermata blu (il blu del marchio), una fessura di luce sul coltello e sul cucchiaio, il titolo in crema; scorrendo l'astuccio si apre, arrivano la forchetta e il cucchiaino e il titolo, fermo, diventa nero.

## Sezioni (scheletri diversi, composizioni alternate)

1. **Apertura, "Tutta la tavola, in argento."** (blu, fissata sopra i 900 px): titolo in Rowan a 150 px a sinistra, fessura a destra sul coltello e sul cucchiaio, riga del mestiere e due collegamenti (riparazione, hotel e ristoranti). Gesto: l'astuccio si apre (`data-he-scale`, `data-he-scale-zoom="1"`, nessun ingrandimento della foto), il titolo passa dal crema al nero per fusione "differenza". Sul telefono: blu con titolo e riga, sotto la finestra con le posate, ferma.
2. **Firma, la vetrina "Argento massiccio"** (carta): tre ripiani di filetto. Sul primo il candelabro a cinque fiamme a sinistra, a destra la citazione della pagina Azienda e il titolo a 196 px in piedi sul ripiano (sale riga per riga); sul secondo brocca martellata, coppa, bicchiere, candeliere; sul terzo servizio Impero e secchiello. Sotto ogni pezzo nome e stile, codice.
3. **999, le impugnature** (carta): il numero a 374 px a sinistra, il leone in 8/11 sulla stessa base, che si scopre dal basso (`data-he-wipe`); sotto, quattro teste nella stessa finestra (cavallo, civetta, cobra, labrador) con il nome.
4. **Riparazione** (sull'inchiostro, come l'argento sul panno scuro): la loro frase "La vostra argenteria tornerà al suo originario splendore." in Plein a 68 px, i cinque materiali in righe grandi color argento a sinistra, a destra come si fa in tre passi, "Mandate le foto del pezzo" (email già compilata) e "Chiamate", una riga in inglese dal loro sito.
5. **Hotel e ristoranti**: a sinistra il testo e quattro strade (preventivo per quantità, Area clienti, export@, riargentatura), "Scrivete la richiesta"; a destra sottopiatto e vassoio tondi visti dall'alto.
6. **Alfredo Varotto** (fascia stretta, 3/11): la citazione della pagina Azienda, senza la data, e la frase sul titolo dell'argento e sul marchio impressi.
7. **Contatti**: il telefono a 124 px da toccare; dove siamo con la mappa, "Prima di passare, chiamate."; email, export, fax; lo shop e il suo WhatsApp per le domande sugli articoli; "Writing from abroad" in inglese; accanto il modulo "Scrivete la richiesta", che prepara l'email come la versione di oggi.
8. **Piede** (inchiostro): Varotto & Co. di Varotto Luca, indirizzo, P.IVA, telefono e fax; note su privacy e cookie; Area clienti, shop, sito inglese di oggi.

## Caratteri e colore

- **Rowan** 300 (ITF, Fontshare) solo nei tre momenti forti: titolo d'apertura 150 px a 1440 e 64 a 390, "Argento massiccio" 196 / 64, "999" 374 / 172 (cifre antiche). **Plein** 400 e 500 (ITF, Fontshare) per tutto il resto, cifre allineate. Riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (nessuna altra home con queste famiglie).
- Carta #F3F2EE, inchiostro #121416 (testo, e campo pieno della riparazione e del piede), grigio #5C6066, blu astuccio #0E2140, l'unico colore pieno, solo nell'apertura, crema #F1DEBF (il negativo del blu, il titolo sul blu), argento #C9CCD1 per i materiali e i testi sull'inchiostro. Nessun corsivo, nessuna etichetta sopra i titoli, maiuscolo spaziato solo nel marchio.

## Foto

**Originali più grandi: trovati.** Ogni miniatura delle pagine di categoria del sito di oggi apre `immagine.asp?PathImm=<nome>`, che mostra il file di `immaginiAltaRisoluzione/<nome>.jpg`: le miniature erano di 100-500 px, gli originali fino a 1280 px. Scaricati i 1.165 file dei marchi Varotto Alfredo, Royal Queen e Royal England (93 MB, `assets/originali/alta/`, fuori da git); più le 70 immagini delle pagine principali e della versione inglese (`assets/originali/sito/`). Le scelte sono in `_prova/he/immagini.json`. Tutte le teste di bastone del catalogo hanno la stessa compressione JPEG (tabella di quantizzazione media 23): non c'è un leone migliore da scaricare.

Trattamento unico (`_prova/he/script/immagini.py`): campo piatto (fondo dello studio stimato con un polinomio e portato a bianco), per i due pezzi tondi il fondo fuori dal profilo portato a bianco, saturazione al 30 %, una curva leggera uguale per tutti, ritaglio sul pezzo con la base che tocca il ripiano; per il leone un mediano di 3 px contro i blocchi JPEG; in pagina in "moltiplica" sulla carta. Nessuna foto oltre la metà della misura del file a 1440 (rapporto peggiore 0,5; 0,55 a 1920).

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
| Leone (impugnatura) | BT00030AX, 1280x1280 | 588x700 | 259 (0,44; al massimo 260 px) |
| Quattro teste | BT00040AX, BT00050AX, BT00101AX, BT00021AX, 1280x1280 | da 630 a 960, file a 520 | 260 (0,5 del file) |
| Sottopiatto | SS01510AG, 1280x1165 | 1340x1225 | 441 (0,33) |
| Vassoio piatto tondo | VAG-P1165.40, 1280x1008 | 1300x1068 | 433 (0,33) |

Nessuna foto a tutta pagina: il campo che si apre nell'apertura è colore, la foto resta alla sua misura. Nessuna immagine di repertorio, nessuna immagine generata.

## Misure e prove (sezione 6), dopo il ritocco

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", larghezza del documento uguale alla finestra, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (4.772 caratteri a 1440, 4.758 a 390), nessun elemento nascosto. L'apertura resta nella composizione di partenza senza fessura (blu, titolo crema, le quattro posate nella finestra); vale anche senza JavaScript.
- **Peso al primo caricamento** (senza scorrere): 434 KB a 390, 445 a 768, 456 a 1024, 456 a 1440, 411 a 1920 (soglie 2,5 e 1,5 MB). Posate e due caratteri precaricati, tutte le altre immagini pigre. Cartella intera 1,2 MB.
- **Layout stabile**: CLS da 0 a 0,0004 a tutte le larghezze, con e senza movimento; con la rotella 0,0002 a 1440. L'apertura fissata usa `pinType: "transform"`, impostato nella pagina prima di `he.js`; la fessura è disegnata dal CSS prima che parta il kit.
- **Funzioni**: `tel:` in testata (a 1440 il numero, sul telefono "Chiama", aree di 44 px) e cinque volte nella pagina; email generale, export, email della riparazione con oggetto e traccia, email del preventivo per quantità; indirizzo con Google Maps; modulo "Scrivete la richiesta" (prepara l'email a info@ come la versione di oggi); riparazione in testata, nella prima schermata e in una sezione; Area clienti; shop in testata, nei contatti e nel piede, WhatsApp dello shop; "Writing from abroad" in inglese con export@ e "EN" in testata; ragione sociale, P.IVA, note privacy e cookie nel piede.
- **Controllo d'uso dal telefono**: in prima vista il titolo, che cosa fanno e dove ("Argenteria Varotto Alfredo, Padova", tavola, hotel e ristoranti, riparazione), "Riparare un argento", "Chiama" e "Contatti" in testata; l'indirizzo con la mappa a un tocco.
- U+2014: nessuno, nella pagina, negli script e in questa nota.

## Guardato come un estraneo (quattro fotogrammi a piena misura a 1440, tre a 390)

- **3,6 s, l'astuccio che si apre**: la fessura sul coltello e sul cucchiaio si allarga, la forchetta è già entrata, il cucchiaino entra dal bordo. È il gesto che mancava: la fine mostra il servizio intero che all'inizio non c'era.
- **10,3 s, il 999 e il leone**: il leone ora è un oggetto piccolo e prezioso accanto a un numero enorme, sulla stessa base; i blocchi non si vedono più. Resta un intervallo largo tra il 999 e il leone (la colonna 8 chiesta dal giudice): lo lascio, la composizione regge come due metà.
- **14,3 s, hotel**: testo a sinistra e pezzi a destra, dopo la riparazione che ha materiali a sinistra e passi a destra ma sull'inchiostro e senza foto. Correzione fatta guardandolo: il vuoto sotto la sezione era di quasi 250 px, ridotto (respiro sotto a 0,6).
- **16,3 s, storia e contatti**: senza gli ovali la fascia è una citazione sola, con una gerarchia (prima frase grande, seconda piccola) invece di due blocchi uguali da 30 px.
- **Telefono**: la prima schermata è completa; l'etichetta delle posate andava su cinque righe accanto al cucchiaino e sembrava una scheda prodotto: ora è nome, stile e codice, su tre righe corte.

Voto atteso, tenendo conto che l'autovoto sta in media 0,7 sopra il giudice: tra 7,6 e 8. La distanza che resta dipende per circa il 60% dalle foto (scontorni di catalogo a 1280 px, prospettive e ombre diverse, nessuna mano, nessun banco, nessun punzone impresso).

## Problemi aperti

- **Fatti lasciati fuori perché da confermare** (LEGGIMI 7 e 8, analisi sez. 9): il punzone 364 PD e la produzione nello stabilimento di Padova, il 1974, gli orari. Il titolo non dice "fabbrica". Se l'azienda conferma, il 364 PD può entrare nella storia e "dal 1974" nella riga d'apertura.
- **Diritti delle foto**: sono del sito di oggi e del catalogo; alcune potrebbero essere dei fornitori. Le impugnature sono "Novità" del marchio Varotto Alfredo: chi le produce va chiesto.
- **Codici e misure**: in pagina ci sono i codici del catalogo, non le misure; i codici con un numero finale (VAG-Z1595.30, VAG-P1165.40) potrebbero essere le misure in centimetri: da chiedere prima di scriverle.
- **Area clienti**: porta all'area riservata di oggi (`area-clienti.asp`); LEGGIMI punto 12.
- **Privacy e cookie**: note nella pagina; servono pagine vere con l'informativa nuova (quella di oggi cita il D.Lgs. 196/2003).
- **Caratteri ITF**: la licenza permette di ospitarli ma non di ridurli: tre file, 56 KB.
- **Modulo**: prepara un'email (`mailto:`), non invia da sé; con il sito vero va collegato a un servizio di invio con gli allegati (LEGGIMI).
- **Fessura e finestre ridimensionate**: la fessura si misura all'apertura della pagina; se si allarga molto la finestra dopo, la fessura resta quella di partenza (si vede al massimo un filo della forchetta o del cucchiaino).

## Foto da rifare (in ordine di valore)

1. **Un servizio still life dei pezzi in argento massiccio**, 10-12 pezzi scelti con l'azienda (posate Inglese, candelabri, brocca martellata, coppa, secchiello, servizio Impero), stesso fondo chiaro, stessa luce morbida da un lato, camera alla stessa altezza e distanza (così i pezzi stanno davvero alla stessa scala sul ripiano), 4000 px. È il guadagno più grande: la vetrina resta uguale e diventa una serie vera.
2. **Le posate Inglese per l'apertura**, a 4000 px, dall'alto, con un poco di ombra, più una versione nell'astuccio blu socchiuso e aperto: la fessura dell'apertura potrebbe essere la foto vera dell'astuccio.
3. **Il leone e le teste delle impugnature** a 4000 px, su fondo chiaro, luce che legga il cesello senza bruciare i riflessi; ogni testa tagliata alla ghiera. Oggi il leone deve restare sotto i 260 px per i blocchi JPEG del file.
4. **I titoli impressi**: macro del 925 o dell'800 e del marchio impressi su un pezzo, luce radente, obiettivo macro 1:1 (con il 364 PD, se confermato). Darebbe alla fascia della storia la prova fotografica che oggi manca.
5. **La riparazione**: un pezzo rovinato com'è arrivato, il lavoro al banco (lucidatura, argentatura), lo stesso pezzo finito, 3:2, stessa luce. Oggi la sezione è solo tipografia.
6. **Un buffet o una sala d'hotel** allestiti con i loro pezzi, con il permesso di nominare l'hotel: il lavoro con un nome che manca.
7. **La sede** di Corso Stati Uniti 23/A, facciata e ingresso, per i contatti.
