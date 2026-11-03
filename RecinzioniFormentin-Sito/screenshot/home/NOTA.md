# Home "Produciamo e montiamo": nota

## Metodo ibrido (novembre 2026)

3 novembre 2026. Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale com'era (pagina, immagini, carattere, screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`. Provini delle foto: `_prova/alto/provini.jpg`.

Screenshot in questa cartella, ora simulata lunedì 2 novembre 2026 alle 10.00 ("Aperto"): `home-1440.jpg` (5916 px dopo il ritocco, 5962 nella prima stesura ibrida, 10668 nella versione professionale), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8589 px, prima 12856), `home-390-prima-schermata.jpg`, `home-1024-prima-schermata.jpg`, `home-768-prima-schermata.jpg`, `chiusura-1440.jpg` (banco, orari e strada). Confronto con la versione professionale e con Gust. Alberts e Jacksons (prime schermate rifatte sul loro dominio il 3/11/2026, `_prova/alto/concorrenti/`): `_prova/alto/shots/confronto-1440.jpg`.

### Ritocco dopo il giudice da agenzia (3 novembre 2026, voto 7)

Il giudice ha dato 7 (prima 6) e ha indicato cinque punti che separano la home da un sito firmato. Pagina di prima e immagini di prima in `_prova/alto/ritocco/` (`index-prima-del-ritocco.html`, `img-prima/`).

**Applicati**
- **P.IVA (bloccante).** Tolta dalla riga legale del piede: viene da atoka ed è da confermare (LEGGIMI 9). Resta "Formentin Srl, via Lombardia 17, 35020 Saonara (PD)" con il commento `<!-- P.IVA da confermare, LEGGIMI 9 -->`. LEGGIMI 9 aggiornato.
- **Gerarchia dell'apertura.** Non è più un dittico 50/50. La macro resta sulle colonne 1-6 più il margine (708 px) ed è alta quanto la schermata: `height:min(calc(100svh - 76px),900px)`, 708 x 824 a 1440, scala 0,92, mai ingrandita. Il cancello passa alle colonne 8-12 più il margine (593 x 445), con la riga e il bottone sotto; la colonna 7 resta come aria. La macro pesa 2,2 volte il cancello. L'apertura chiude esattamente a 900 px, e la striscia verde di 27 px non c'è più. A 1920 la macro arriva a 900 px (scala 1,0) e sotto si vede l'inizio del blocco verde.
- **"Preventivo gratuito".** Non è più uno span accanto al bottone che sembrava un comando: ora è dentro la frase ("Recinzioni e cancelli, dalla vendita alla posa. Villatora di Saonara. Preventivo gratuito.").
- **Culmine con un'altra immagine.** La foto ora è `gallery_reti-ondulate_IMG_1145-1.JPG` (800 x 533, 3:2): la rete che passa tra le guide del telaio della macchina, cioè il "produciamo" mostrato. L'h2 diventa "Reti ondulate di nostra produzione" (frase loro, già nella meta description). La frase-firma resta nell'h1 e nel piede (D7: due punti). Didascalia: "Rete ondulata a maglia intrecciata, sul telaio della nostra macchina. Foto del 2014".
- **Una foto nella seconda metà.** In Aziende, sopra "Mandateci il disegno", c'è il cancello pedonale di un campo sportivo (`gallery_cancelli_img_1114.jpg`, 1024 x 859, tagliato 3:2 e non 4:3 per stare sotto i 6000 px), con la didascalia a due voci "Cancello pedonale / Recinzione di un campo sportivo" (il luogo si aggiunge quando lo danno, LEGGIMI 5). Le foto restano 7 e i formati 3: è uscita `l-bianca`.
- **Lavori più grandi.** Sono tre in tre colonne di 4 (437 x 328 a 1440, file da 800 px): il portale, la casa di sera e le doghe antracite. È uscita la recinzione a doghe bianche, che aveva la luce d'autunno. A 390 il primo lavoro è largo tutta la colonna e gli altri due stanno affiancati.
- **Una divisione sola delle colonne.** Le sezioni si dividono tutte sulle linee 1, 5 e 9 (x 40, 501, 963 a 1440). Il preventivo ha il titolo su 1-8, la frase su 9-12 e i tre passi in tre colonne di 4, come i lavori. Casa ha la stessa testata del preventivo. Culmine e Aziende restano 1-7 + 9-12. La chiusura diventa "Orari e strada" su 1-7 (orari su 1-3, strada su 5-7) e il banco su 9-12. Il piede ha tre colonne di 4. L'unica linea diversa è quella del cancello d'apertura (colonna 8), che è voluta.
- **Piede allineato.** Il marchio del piede non è più un link alto 48 px: ora sta sulla stessa riga dei titoli delle altre due colonne (y 5707 per tutti e tre). La riga legale è centrata in verticale sui link Privacy e Cookie.
- **Culmine a 390.** La frase sugli inizi è uscita dalla figura. A 1440 è un elemento della griglia sotto la foto, sulle colonne 1-4; sotto i 1024 px viene dopo il titolo, il testo e la tabella.
- **768-1023 px.** La macro si allunga fino all'altezza della colonna di destra (`align-self:stretch` e immagine assoluta), e il rettangolo bianco di circa 150 px sotto il titolo non c'è più.
- **Lo scuro sulla macro.** Copre il 46% in basso (prima il 58%) e arriva al massimo a 0,72 (prima 0,86): la maglia nitida si vede di più. Il contrasto medio sotto le lettere è 8,2:1 a 1440. A 390 la macro è quadrata (390 x 390 dal file da 400, scala 0,975) con lo scuro sul 55%, e il bottone finisce a 659 px, nella prima schermata.
- **Cliente tipo, la strada a 390** (era l'unico passaggio in più). Nel menu sotto i 1280 px, dopo "Orari", c'è "Come arrivare: via Lombardia 17", che apre le indicazioni di Google Maps. Così la strada è a due tocchi senza scorrere, e la prima schermata resta a 4 cliccabili. Il link è nascosto a 1440, dove il menu è sempre aperto, e la parola "Indicazioni" compare ancora una volta sola.
- **Altezza.** Per restare sotto i 6000 px di D8 (con la foto in più e i lavori più grandi): le dodici categorie del banco diventano una frase con le stesse parole (era il quarto elenco a filetti), le righe dell'indice dei prodotti passano da 20 a 16 px di spazio, e le testate di Preventivo e Casa stanno su una riga sola. Pagina a 1440: 5916 px.

**Respinti o lasciati**
- **Didascalia sull'apertura** (D10 la vuole su apertura e lavori): non c'è spazio, perché D3 permette al massimo 160 caratteri e la prima schermata ne ha 158.
- **Luogo e anno dei lavori** (D9): non li scrivo, perché mancano i dati e non vanno inventati. D9 resta "non passa" finché l'azienda non li dà (LEGGIMI 5).
- **A 390 l'unico bottone è l'email e non la chiamata** (per S la regola vuole la chiamata): lo lascio. "Chiama" è sempre nella testata fissa, e per un mestiere senza urgenze il primo gesto è mandare foto e misure.
- **REGISTRO-CARATTERI a 152 px invece di 144**: non l'ho toccato, perché lo aggiornano altri agenti in parallelo. In pagina il titolo è a 144.
- **Frasi da scheda** ("Vantiamo al nostro interno", "Si eseguono lavori di carpenteria"): restano, perché sono le frasi dell'azienda.
- **Le foto da telefono a 800 px** (per il giudice, circa il 60% della distanza dal 7,5 in su): non si risolve senza la giornata di foto (LEGGIMI, "Foto da fare dal vero").

**Controlli dopo il ritocco.** `misura-d.mjs`: 35 controlli su 35 passano (esito in `_prova/alto/misure/esito.txt`). `shots.mjs` a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione di testi, nessun errore di script, `tel:` e `mailto:` giusti, nessun cliccabile sotto i 44 px fuori dal testo (`_prova/alto/shots/controlli-finali.json`). Altezze: 8980, 8589, 7751, 6036, 5916 e 5992 px. Gli screenshot di questa cartella sono rifatti con gli stessi nomi. Il menu aperto a 390 è in `_prova/alto/ritocco/shots/menu-390.jpg`. Nessuna U+2014.

### Che cosa è cambiato

- **Idea e gesto.** "Produciamo e montiamo" è una frase loro (pagina Ringhiere e cancelli; "Produciamo direttamente al nostro interno robuste reti ondulate" nella pagina Reti ondulate). È in Big Shoulders Display 700 maiuscolo, a 144 px, bianca sulla macro della loro rete ondulata sulla macchina (`uploads_2014_04_rete_ondul2.jpg`, 800 x 900 alla misura vera, a filo del bordo sinistro). Accanto c'è il secondo verbo: il cancello scorrevole antracite posato (`canc082204`, 4:3). La frase torna uguale nel culmine e nel piede. Modello M del capitolo 5 (riferimento Alberts, "Made in Herscheid").
- **Scostamenti dalla riga del capitolo 5.** La macro non va "a tutta larghezza": sarebbe ingrandita 1,8 volte, perché nessuna foto loro supera gli 800 px (a parte il negozio del 2014). Il titolo non è "Fatte a Villatora": le foto della macchina sono del 2014, prima del trasloco del 2018, e nessuna fonte dice dove si produce oggi.
- **Prima schermata.** A 1440 restano il marchio, cinque voci di menu (l'ultima porta lo stato, "Orari: aperto" o "Orari: chiuso"), il telefono, una riga ("Recinzioni e cancelli, dalla vendita alla posa. Villatora di Saonara."), un bottone ("Manda foto e misure") e "Preventivo gratuito". A 390 ci sono il marchio con "Formentin", "Chiama", "Menu", la riga, lo stato e il bottone, con le due foto.
- **Tolti.** La fila delle quattro garanzie, il bollino "50+" (era due volte), la fascia verde dei quattro ingressi, il secondo bottone dell'apertura, gli occhielli sopra ogni titolo, i numeri dei passi a 48 px, il telefono a 96 px, il modulo (rifaceva il "Manda foto e misure" con un'email), la sezione "Chi siamo" in tre colonne (resta una frase sotto la foto del culmine), le schede prodotto con foto (diventano quattro righe numerate), i doppioni di "Indicazioni stradali", del cellulare e del telefono, il link "Apri la mappa", le foto del negozio e dell'esposizione Betafence (2014 e 2015, probabilmente la sede di prima).
- **Rimasti, su una griglia sola.** La griglia ha 12 colonne, margini di 40 px a 1440 e solchi da 24 px. Le sezioni sono sei, più il piede: 1) apertura; 2) preventivo in tre passi, l'unico blocco nel verde del marchio, con "Manda foto e misure" (email con oggetto e traccia); 3) per la casa, con i lavori in alluminio (quattro nella prima stesura, tre dopo il ritocco; ingrandibili con un tocco, didascalie a due voci), i quattro prodotti in righe numerate e l'esposizione su appuntamento con il bottone "Chiedi l'appuntamento" (email con traccia); 4) culmine su fondo antracite, alto 1049 px a 1440, con la rete ondulata sulla macchina, la didascalia "Rete ondulata a maglia intrecciata, sul telaio della nostra macchina. Foto del 2014" (foto cambiata con il ritocco), la tabella delle maglie (dalla pagina Reti ondulate), le colonne zincate a caldo e la frase sugli inizi; 5) aziende e Betafence, con i cinque sistemi e le altezze, "Mandateci il disegno", l'elenco dei dati e il bottone "Manda il disegno" (email con traccia); 6) banco, orari e strada (dopo il ritocco: orari e strada a sinistra, banco a destra), con le dodici categorie (dopo il ritocco in una frase), carpenteria e grigliati, lo stato aperto o chiuso calcolato con i festivi, la tabella degli orari, l'indirizzo, come arrivare, "Indicazioni stradali", telefono, cellulare ed email. Il piede è un biglietto da visita con la frase e la ragione sociale (la P.IVA è stata tolta con il ritocco, vedi sotto).
- **Caratteri.** Esce Geologica. Entrano Big Shoulders Display 700 e Public Sans 400 e 600 (SIL OFL 1.1, licenze in `sito/fonts/`). Riga aggiunta in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`; lì il titolo è scritto a 152 px, in pagina è a 144 (a 152 la seconda riga andava a capo), e il registro non l'ho riscritto perché altri agenti lo aggiornano in parallelo.
- **Foto.** 7 in pagina, un solo trattamento (`_prova/alto/script/immagini.py`: bilanciamento verso il neutro a metà, saturazione 0,88, contrasto 1,05), WebP con srcset, tre formati (8:9, 4:3, 3:2), nessuna ingrandita. La cartella `assets/originali/` mancava dopo il riavvio: l'ho riscaricata dal sito di oggi (175 file, la libreria e le gallerie; le macro e i negozi a misura piena).

### Misure (`_prova/alto/misura-d.mjs`, esito in `_prova/alto/misure/misure-d.json` e `esito.txt`)

35 controlli su 35 passano.

| Controllo | Soglia | Oggi | Versione professionale, stesso script |
|---|---|---|---|
| Foto nella prima schermata 1440 (area delle immagini) | 60% o più | 65% (a campione, senza le lettere del titolo: 52%); prima del ritocco 72% in due metà uguali | 20% |
| Cliccabili 1440 / 390 | 8 / 4 | 8 / 4 | 16 / 7 |
| Bottoni nella prima schermata 1440 / 390 | 1 / 1 | 1 / 1 | 3 / 4 |
| Caratteri fuori dal menu, 1440 | 160 | 158 | 643 |
| Foto a 390 | 50% | 66% | 29% |
| Famiglie di caratteri | 2 | 2 | 1 |
| Elementi sopra i 100 px | 1 | 1 (il titolo) | 0 |
| Occhielli | al massimo 1 | 0 | 9 |
| Parole | 900 (D8: S fino a 750) | 714 | 1056 |
| Sezioni | 7 | 6 più il piede | 9 più la fascia degli ingressi |
| Altezza a 1440 | 7.500 px (D8: 6.000) | 5.916 px | 10.668 px |
| Cifre di 30 px o più | al massimo 1 | 0 | 8 |
| Foto e formati | 12 e 3 | 7 e 3 (0,86, 1,33, 1,5) | 11 e 2 |
| Fondi | 3 | 3 (bianco, verde, antracite) | 4 |
| Spazi tra le sezioni | due, uno 1,5 volte l'altro | 96 e 160 px | 40 e 120 px |
| Bottoni in pagina | 5 | 5 | 13 |
| Stesso numero o stessa funzione | al massimo 2 volte | 049 760801 due volte (testata e orari), "Manda foto e misure" due volte | 049 760801 nove volte, link alla mappa sei |
| Lista nera, istruzioni sopra i 14 px | 0 | 0 | "soluzioni"; "Il modulo prepara un'email..." |
| Peso caricato | 3 MB | 0,49 MB, foto di 1440 e di 390 sommate (cartella `sito/` 0,55 MB) | 1,34 MB |

La versione professionale si rimisura con `SITO=.../_prova/versione-pro/sito/ node misura-d.mjs` (esito in `_prova/alto/misure/pro-misure-d.json`).

Contrasto del titolo bianco sulla foto (`_prova/alto/script/contrasto-h1.mjs`, testo nascosto e fondo misurato sotto le lettere): dopo il ritocco, con lo scuro più leggero, in media 8,2:1 a 1440 (4,1:1 sul 2% più chiaro), 8,7:1 a 1024, 8,8:1 a 768, 9,3:1 a 390 e 9,0:1 a 320. Prima era 10,6:1 a 1440. Il resto: verde e bianco 5,5:1, secondario su verde 4,7:1, secondario su antracite 8,4:1, secondario su bianco 6,0:1.

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/shots.mjs`, esito in `_prova/alto/shots/controlli-finali.json`): nessuno scorrimento orizzontale, nessuna sovrapposizione di testi, nessun errore di script, `tel:` e `mailto:` giusti, nessun cliccabile sotto i 44 px fuori dal testo. A 1920 la pagina resta larga 1440 px e centrata, perché le foto non reggono di più.

### Compiti della scheda d'uso: dove stanno ora

Posizioni a 390 in `_prova/alto/script/posizioni.mjs`.
- **Privato.** 1) Il mestiere, il luogo, la parola "posa" e due foto loro (la rete e il cancello posato) si leggono senza scorrere. 2) "Manda foto e misure" è senza scorrere, alto 56 px, ed è sempre il bottone pieno. I tre passi, con che cosa mandare, finiscono a 1527 px, entro uno scorrimento. 3) "Preventivo gratuito" è senza scorrere. "Esposizione in sede, su appuntamento" con il suo bottone sta a 2645 px, entro tre scorrimenti. 4) I quattro lavori in alluminio finiscono 1485 px dopo l'apertura, entro due scorrimenti; ci si arriva anche dal menu ("Lavori e prodotti") e si ingrandiscono con un tocco.
- **Impresa.** 1) Lo stato si legge a 441 px, senza scorrere: a 1440 sta nel menu. 2) "Chiama" è nella testata fissa, sempre. 3) **La strada non è più a un tocco**: Menu, "Orari e strada", poi "Indicazioni stradali" (D3: a 390 ci sono al massimo 4 cliccabili). 4) Il banco è a un tocco dal menu ("Attrezzature edili"); carpenteria e grigliati stanno nella stessa sezione.
- **Tecnico.** 1) "Betafence" è nel menu della prima schermata; "Rivenditori e installatori ufficiali" è il titolo della sezione Aziende, a un clic. 2) I sistemi e le altezze sono in testo, a un clic. 3) L'elenco dei dati e "Manda il disegno" stanno nella stessa schermata. 4) Il telefono è nella testata. **L'email non è più nella prima schermata**: sta in "Orari e strada" e nelle email già scritte. La P.IVA è nel piede.

### Problemi aperti

- **Le foto restano da telefono e piccole.** È il limite più grande: la macro dell'apertura è nitida in primo piano ma ha 800 px, e la serie dei lavori ha luci diverse. Sopra il 7,5 serve la giornata di foto (LEGGIMI, "Foto da fare dal vero"): prima di tutto la macro della rete ondulata sulla macchina di oggi, a 2400 px almeno. Con quella l'apertura diventa davvero a tutta larghezza.
- **La macchina della rete c'è ancora?** Le foto sono del 2014. "Produciamo direttamente al nostro interno" è scritto sul sito di oggi, ma va confermato che la rete si fa ancora, e dove. Se non è più così, la frase va cambiata (LEGGIMI, punto 16).
- **I lavori non hanno né luogo né anno** (LEGGIMI, punto 5): per questo D9 non passa. La didascalia del culmine ha cosa, dove e anno ("sul telaio della nostra macchina", 2014); quelle dei tre lavori e del campo sportivo hanno lavoro e materiale. Comune e anno vanno chiesti e scritti come seconda voce ("Alluminio antracite / Comune, anno"), senza inventarli.
- **La misura della foto a campione** dà il 59% a 1440, perché le lettere del titolo coprono la foto. L'area delle immagini dà il 72%. Ho tenuto la seconda, perché la regola misura la foto e non il testo sopra.
- **La strada per l'impresa**: dopo il ritocco è nel menu ("Come arrivare: via Lombardia 17", solo sotto i 1280 px), cioè due tocchi da qualunque punto della pagina. **L'email nella prima schermata per il tecnico** resta fuori per i tetti di D3: sta in "Orari e strada" e nelle email già scritte.
- La P.IVA è uscita dal piede: viene da atoka e non è confermata (LEGGIMI, punto 9). Al suo posto c'è il commento `<!-- P.IVA da confermare, LEGGIMI 9 -->`; si rimette quando l'azienda la conferma.

---

## Nota di prima: home "Recinzioni e cancelli, dalla vendita alla posa" (livello professionale)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, screenshot con `pro_shots.mjs` e `pro_shots.py`, controlli con `pro_controlli.mjs`; con l'argomento `tutte` anche 320, 768 e 1024). `largo.mjs` trova gli elementi che escono dalla larghezza. La versione di prima ("La rete ondulata la facciamo noi") è in `_prova/versione-1-originale/`.

Screenshot in questa cartella (ora simulata lunedì 2 novembre 2026, 10.00, quindi "Aperto ora"): `home-1440.jpg` (10668 px), `home-1440-prima-schermata.jpg` (1440 x 900), `home-390.jpg` (12856 px), `home-390-prima-schermata.jpg` (390 x 844), `chiusura-1440.jpg` (richiesta e piede).

## L'idea

Prima l'uso, poi l'identità, poi la forma. La scheda d'uso (`_prova/uso/SCHEDA.md`) dice chi apre il sito: il privato con la casa nuova, al telefono la sera (preventivo); l'impresa in furgone (è aperto adesso? che cosa tengono? come arrivo?); il tecnico al computer (Betafence, altezze, dove mando il disegno). La home risponde a tutti e tre nella prima schermata e poi si apre come un sito di servizi tecnici (famiglia S).

Identità: le loro parole e il loro tono al "noi" e al "voi", il loro marchio (rombo di rete azzurra e F verde), il loro verde come colore dei blocchi pieni e delle azioni, l'azzurro della rete per le cifre e i filetti sui blocchi scuri, l'antracite dei loro lavori in alluminio. Nessuna foto di repertorio, nessun disegno al posto delle foto.

## Ritocco del 3 novembre (controllo del livello professionale, voto 6)

Fatto, in ordine di peso:
- **Fascia delle quattro garanzie** in fondo all'apertura, con le loro parole: "Preventivo gratuito", "Posa del nostro personale", "Ampia esposizione in sede", "Betafence ufficiale". A 1440 è dentro la prima schermata (y 700-825), a 390 è una griglia 2x2 con i soli titoli.
- **La prova si vede da sola**: un riquadro verde pieno sopra l'angolo della foto, "50+ anni di mestiere, dai primi anni Settanta" (il gesto del voto di Kline, con l'unico numero vero che hanno). La riga sotto il titolo ora parla al privato ("Recinzioni in alluminio, cancelli e ringhiere per la casa, con la posa del nostro personale"); Betafence sta nella fascia delle garanzie e nella sezione aziende.
- **Foto di apertura ritagliata in 16:10** (cy 0,42): via un terzo del piazzale di cemento, cancello e casa riempiono il riquadro; 640 px CSS da un file di 800.
- **Il colore del marchio fa i blocchi**: l'indice dei quattro usi e la chiusura "Chiamateci o scriveteci" (telefono bianco a 96 px, modulo su carta bianca) sono su verde #0A7A32; i filetti dei blocchi scuri sono nell'azzurro della rete.
- **Ritmo**: la sezione aziende passa su antracite (il riquadro "Mandateci il disegno" resta bianco). Sequenza a 1440: bianco, verde, grigio, antracite, bianco, antracite, grigio, bianco, antracite, verde, piede antracite; nessuna coppia di fondi uguali di fila. A 390 dopo i lavori (antracite) viene l'indice verde: niente più blocco scuro di 1470 px.
- **Numeri di riempitivo tolti** ("4 materiali", "3 usi", "3,0 m"): in Chi siamo resta solo "50+" a 96 px in azzurro, con la storia in tre tappe (gli inizi, la specializzazione, oggi) scritta con le frasi della pagina Azienda.
- **Lavori**: 4 invece di 6 (uscite `canc082203` e `canc082206`, doppioni delle schede), in due colonne da 624 x 468 a 1440, senza didascalie; ogni foto apre la versione da 800 px (anche sul telefono, dove restano 2 x 2 per stare nei due scorrimenti). Occhiello "Alcuni nostri lavori" e titolo "Recinzioni e cancelli in alluminio per abitazioni": non diciamo più "recenti" né "posati", che le fonti non confermano.
- **Schede dei prodotti a 390** in righe (foto 4:3 da 128 px, nome e link, tutta la riga cliccabile): la sezione scende da 3281 a circa 1000 px.
- **Marchi e norme**: titolo visibile, Betafence ed EN 13241-1 ("certificazione del produttore dei cancelli pedonali e carrai in kit"); ForFence esce dalla fascia e resta solo tra i sistemi. Nel piede una voce "Marchi e norme" a sé.
- **Preventivo detto in un modo solo**: 1. foto e misure ("Per email" è un link alla mail già scritta), 2. vi richiamiamo e fissiamo l'appuntamento in sede, 3. "Vedete i modelli, avete il preventivo": in sede vi diamo il preventivo, gratuito. Tolta la frase vuota "Per un preventivo senza impegno, vi invitiamo a contattarci" (ora "Gratuito e senza impegno. Bastano due o tre foto e le misure."). Il cellulare compare anche qui.
- **Fuori orario** (sera, notte, domenica, festivi, chiusure) il bottone pieno diventa "Manda foto e misure", "Chiama" passa al bordo e sotto compare "Fuori orario: mandateci foto e misure, vi richiamiamo noi." Il sabato resta "Chiama" (su appuntamento, chiamate prima).
- **Stato degli orari**: sopra i bottoni (a 390 finisce a y 610, dentro i 664 px di Safari con le barre); il link accanto apre la navigazione (`maps/dir`) con zona di tocco allargata; nella mezz'ora prima di ogni chiusura dice "Aperto, chiude alle 12.00: chiamate prima"; c'è un elenco `CHIUSURE` per ferie e chiusure straordinarie, vuoto finché l'azienda non dà le date.
- **Imprese**: sotto i bottoni, a 390, il link "Imprese: attrezzature edili al banco" porta diretto al banco; nel riquadro del banco c'è anche il cellulare.
- **Menu**: prima voce "Preventivo". L'email della testata compare da 1600 px; a 1440 è nell'apertura, sotto i bottoni.
- **Modulo**: aggiunti email (facoltativa), "Foto e misure" (le allego / non ancora) e "Giorni preferiti per l'appuntamento" (lun-ven), tutti nel testo dell'email.
- **Ripetizioni**: tolti gli orari dal blocco di chiusura, che rimanda a "Dove siamo".

Respinto o lasciato com'è, con il motivo:
- *Lavori a 390 in una sola colonna da 350 px con 3 foto*: il quarto lavoro finirebbe oltre i due scorrimenti, e il compito del privato ("4 lavori in al più 2 scorrimenti") peggiorerebbe. Restano 2 x 2, ma ingrandibili.
- *"Indice" riportato subito dopo l'apertura a 390*: allontanerebbe passi e lavori del privato; ho scelto l'altra correzione proposta (indice verde) e il link diretto al banco nell'apertura.
- *Un grande lavoro a 1280 px*: i file sono di 800 px, a 1280 sarebbero sgranati.
- *Foto di apertura `l-sera`*: è di sera, con le case dei vicini; `canc082204` ritagliata è più chiara e più frontale.
- *Gesto di scala a 160-200 px per "50+"*: sarebbe la nona misura di carattere (regola 7); resta a 96 px, come il telefono della chiusura.
- *Promessa dei tempi di risposta accanto al modulo*: non è nelle fonti; è nel LEGGIMI.

## La pagina, in ordine

1. **Testata fissa** (89 px a 1440, 73 a 390): marchio, "Recinzioni Formentin / Villatora di Saonara", Preventivo, Prodotti, Lavori, Aziende, Attrezzature edili, Dove siamo, email (da 1600 px) e il bottone "049 760801" (bordato finché i bottoni dell'apertura sono in vista). Sotto i 1280 px il menu va nel bottone "Menu".
2. **Apertura** (bianco): occhiello "Villatora di Saonara (PD)", H1 64 px, riga per il privato, stato con "Mappa" (navigazione), "Chiama 049 760801" e "Manda foto e misure", indirizzo ed email; a destra il loro cancello scorrevole in 16:10 con il riquadro verde "50+"; sotto, le quattro garanzie.
3. **Indice** (verde): Per la casa, Per le aziende, Per gli impianti sportivi, Per le imprese (cinque categorie del banco).
4. **Come chiedere il preventivo** (grigio zinco): tre passi, "Manda foto e misure", "Chiama", "Oppure compilate la richiesta", cellulare.
5. **Alcuni nostri lavori** (antracite): quattro foto grandi, poi "Volete vedere i modelli dal vero? L'esposizione è in sede, su appuntamento." con "Appuntamento 049 760801" e "Indicazioni stradali".
6. **Prodotti** (bianco): sei schede con la foto loro, tutte cliccabili.
7. **Aziende, condomini, impianti sportivi** (antracite): Betafence, tabella dei sistemi, riquadro bianco "Mandateci il disegno", fascia "Marchi e norme".
8. **Attrezzature edili e ferramenta al banco** (grigio): dodici categorie, carpenteria e grigliati, riquadro con stato, orari, "Chiama", "Indicazioni stradali", cellulare.
9. **Dove siamo** (bianco): indirizzo grande, come arrivare, navigazione e mappa; tabella degli orari con il giorno di oggi in verde; telefono, cellulare, email.
10. **Chi siamo** (antracite): "Dai primi anni Settanta", "50+" a 96 px, la frase sul servizio completo, la storia in tre tappe.
11. **Richiesta** (verde): "Chiamateci o scriveteci", telefono bianco a 96 px, cellulare, email; modulo che compone l'email.
12. **Piede** (antracite): marchio, riga, Marchi e norme; Prodotti; Orari; Contatti; riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie.

## Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs <cartella>` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 1024, 768, 390 e 320.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky 89/73 px, bottone "049 760801" 127 x 48 a 390; a metà pagina si vede e si tocca (`elementFromPoint`) a 1440 e a 390. 14 link `tel:`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 "Recinzioni e cancelli, dalla vendita alla posa", occhiello "Villatora di Saonara (PD)", prova visibile da sola ("50+ anni di mestiere, dai primi anni Settanta" in verde pieno, più "Betafence ufficiale" nelle garanzie), "Chiama 049 760801" largo 350 px su 350 a 390.
3. **Immagine vera nell'apertura: passa con riserva.** È un loro lavoro (`canc082204`), non un oggetto scontornato, ora in 16:10 senza il piazzale; non mostra persone, mezzi o la sede. Senza servizio fotografico (e senza illustrazioni, esclusi dal committente) resta così: LEGGIMI, Foto da fare, punto 1.
4. **Zero repertorio: passa.** "indicativ" 0 volte; nessuna immagine da `assets/esterne`, Unsplash o Pexels; in `sito/img/` 11 foto loro e il marchio.
5. **Foto in serie: passa in parte.** Formati: 2 (4:3 e 16:10 dell'apertura). Didascalie: 0. Luce: non ancora una serie (due lavori al crepuscolo, due di giorno, banco ed esposizione al neon del 2014-2015); il trattamento comune di `pro_img.py` attenua ma non basta. La serie vera la fa la giornata di foto del LEGGIMI.
6. **Palette dal marchio: passa.** `--verde` #0A7A32 (F del marchio scurita, ora anche in due blocchi pieni), `--verde-scuro` per il passaggio del mouse, `--azzurro` #5A94F7 (rete: cifre e filetti sui blocchi scuri), `--antracite` #2B3134; neutri bianco, grigio zinco #EEF1F2, grigi di testo e filetti (sul verde, il bianco trasparente). Nessun colore fuori da `:root` a parte i due del marchio nell'SVG. Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 96) e 7 a 390 (14, 17, 20, 24, 30, 36, 44); testo corrente 19 px a 1440 e 17 a 390; niente sotto i 14 px; H1 64/36.
8. **Due famiglie al massimo: passa.** Una: Geologica 400 e 700, anche per campi e bottoni.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 768-1023, righe con la foto a sinistra al telefono), sei schede in 4:3, nome a 23 px, link con freccia; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa (1 su 4).** C'è la fascia "Marchi e norme" con la didascalia (Betafence, EN 13241-1). I numeri aziendali non sono 4 (c'è solo "50+": gli altri tre erano riempitivi e sono usciti). Mancano recensioni e clienti con il nome: non sono nelle fonti verificabili (LEGGIMI, punti 4, 6 e 13). Non inventati.
11. **I lavori hanno un nome: non passa.** Quattro lavori con foto larga quasi metà pagina (624 px a 1440), ma senza luogo, anno né dati: non sono nelle fonti (LEGGIMI, punto 5).
12. **Ritmo a blocchi: passa.** Cinque blocchi pieni oltre al piede (indice e richiesta verdi; lavori, aziende e chi siamo antracite), nessun fondo uguale due volte di fila a 1440 e a 390; sezioni a 120 px a 1440 e 64 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato, raggio 4 px, 56 px (48 in testata), testo 17 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: non passa (manca solo la zona).** Modulo con nome, telefono, email, tipo di lavoro, comune e via, metri, altezza, cancelli, foto (le allego / non ancora), urgenza, giorni preferiti e descrizione; nessun iframe. Manca l'elenco dei comuni serviti: non è nelle fonti (LEGGIMI, punto 3).
15. **Piede completo: non passa (manca solo la zona).** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA (da atoka, da confermare), indirizzo con la mappa, telefono, cellulare ed email cliccabili, orari, "Marchi e norme", Privacy e Cookie. La colonna "Dove posiamo" è preparata (commento nel codice) e si aggiunge con l'elenco dei comuni.

## Compiti della scheda d'uso

- *Privato, 390 x 844*: senza scorrere la foto del loro cancello, "dalla vendita alla posa", "Villatora di Saonara", lo stato, "Chiama 049 760801" (350 x 56) e "Manda foto e misure" (`mailto:` con oggetto e traccia). Fuori orario il bottone pieno è "Manda foto e misure". Con uno scorrimento i tre passi (y 1215) e il link "Per email" (y 1322). Quattro lavori loro entro due scorrimenti (il quarto comincia a y 2342), ingrandibili. "L'esposizione è in sede, su appuntamento" e "Indicazioni stradali" subito sotto.
- *Impresa, 390 x 844*: lo stato nella prima schermata, sopra i bottoni, giusto a lunedì 10.00, 12.30 e 17.15, venerdì 18.00, sabato, domenica, 8 dicembre, Pasquetta e 24 dicembre sera. "Mappa" apre la navigazione con un tocco. "Imprese: attrezzature edili al banco" nella prima schermata; "Per le imprese" con cinque categorie a y 3205, entro tre scorrimenti; il banco dal menu.
- *Tecnico, 1440 x 900*: telefono in testata ed email nell'apertura; "Betafence ufficiale" nella prima schermata; nella sezione aziende i sistemi con le altezze, "Mandateci il disegno" con i dati che servono e la mail con oggetto "Richiesta per azienda o impianto sportivo".
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 768, 1024, 1280, 1440 e 1920 (controllato sulla larghezza vera, non sulla finestra del telefono che si allarga); nessuna sovrapposizione in testata e apertura; zoom permesso.

## Caratteri e licenze

- **Geologica** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile `sito/fonts/geologica-latin-var.woff2` servito dalla pagina, licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, cifre tabellari per numeri e orari.
- Foto: solo materiale del loro sito, da usare con il loro permesso e, per le case riconoscibili, con quello dei clienti.

| In pagina | File d'origine (`assets/originali/`) |
|---|---|
| Apertura (16:10) | `gallery_cancelli_canc082204.jpeg` |
| Lavori | `canc082202`, `canc082201`, `ringh082202`, `ringh082203` |
| Schede | `ringh082201` (alluminio), `canc082207` (cancelli), `gallery_ringhiere_img_1061.jpg` (ringhiere), `gallery_reti-ondulate_IMG_1130-1.JPG` (rete), `uploads_2016_01_20151223_103842n.jpg` (esposizione Betafence), `uploads_2014_04_IMG_1135.jpg` (banco) |

## Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1, 2, 4, 6-9, 12 e 13 superate nelle misure; 3 e 5 con riserva (vedi sopra); 10, 11, 14 e 15 no, per materiali che mancano. Compiti d'uso, collegamenti, ancore, larghezze, errori di script: tutti a posto.
- Collegamenti: `tel:+39049760801`, `tel:+393357740278`, `mailto:info@recinzioniformentin.it` con oggetto (e traccia dove serve), Google Maps `search` e `dir` su via Lombardia 17.
- Modulo: invio vuoto fermato con l'avviso e il fuoco sul nome; con i campi pieni compone `mailto:` con oggetto "Preventivo: <tipo>" (letto nella prova, non aperto); le schede scelgono il tipo di lavoro.
- Stato fuori orario guardato a venerdì 20.30 a 390 (bottoni scambiati e riga "Fuori orario").
- Screenshot guardati a pezzi a 1440 e a 390, pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
