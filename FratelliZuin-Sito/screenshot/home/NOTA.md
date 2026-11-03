# Fratelli Zuin, home: "In qualsiasi situazione e spazio"

## Metodo ibrido (novembre 2026)

Richiesta del committente: la home professionale "non è ancora super professionale" (giudice da agenzia 6). Metodo scelto: **ibrido**, cioè prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md` e, sotto, i contenuti e le funzioni della versione professionale, rimessi in ordine su una griglia sola. La versione professionale com'era (sito e screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`; riga del registro in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.

### Secondo giro (3/11/2026)

Esito del primo giro: giudice da agenzia 6,5 dopo il ritocco (versione professionale 5,5); clienti tipo scesi (cliente 1 da 8 a 7, cliente 2 da 8,5 a 6,5). Questo giro ha due scopi: riportare i compiti della scheda al livello della versione professionale senza toccare i tetti della prima schermata (D3), e dare sotto la piega l'esecuzione che il giudice chiedeva. Fonti: le prove dei clienti tipo (`_prova/alto/prova-1/`, `prova-2/`), i difetti del giudice finale (`_prova/alto/giudice-finale/`) e `ALTO-LIVELLO.md`, cap. 1 e 4. La pagina di prima, i suoi screenshot e la misura di prima sono in `_prova/alto/giro2/prima-del-secondo-giro/`; le viste di lavoro in `_prova/alto/giro2/`. Dove questo paragrafo contraddice quelli sotto, vale questo.

**Per i clienti tipo**
- *Testata.* La chiamata in testata è alta 48 px, come chiede la scheda (prima 44), e "Menu" è un bersaglio di 64x48 px a 16 px dal bottone, che non si sposta più quando la parola diventa "Chiudi". Le voci nominano quello che si cerca: "Cassoni e lavori", "Escavatori a risucchio", "Chi siamo", "Enti e SOA", "Preventivo e sede". Sopra i 1099 px stanno tutte nella testata; sotto si apre il pannello.
- *Barra in basso sul telefono* (sotto i 760 px). Compare quando la foto d'apertura è passata, senza animazione, e dà due cose: "Chiama 049 625336", rossa, 52 px, sotto il pollice, e "Via Bassette 6/A, Padova Est, la mappa", che apre Google Maps. Così la sede con la mappa è a un tocco dalla seconda schermata in poi (compito 4 del visitatore 1, che nel primo giro non passava). Quando c'è la barra, il bottone della testata lascia il suo posto vuoto: la chiamata non compare due volte nello stesso schermo. Nella prima schermata la barra non c'è, quindi i tetti di D3 a 390 restano 4 cliccabili e 1 bottone. Senza JavaScript la barra è sempre visibile.
- *Stato aperto o chiuso: non c'è.* Il loro sito non scrive gli orari (controllato il 3/11 sulla pagina Dove siamo e sulla home), e il LEGGIMI li chiede (punto 1). Un "Aperto" senza orari sarebbe inventato: il posto è accanto alla chiamata, quando arrivano.
- *Prima schermata, stessi tetti.* La riga del mestiere ora nomina il risucchio: "Scavi, cassoni, fognature e risucchio a Padova Est, dal 1946" (visitatore 2). Per restare a 160 caratteri a 1440 la didascalia è "Fiat-Hitachi EX215 / Movimento terra" ("Carico di terra" era sbagliato: in primo piano ci sono macerie; l'alt dice ora "carica il cassone rosso... tra i cumuli di macerie e di inerti"). A 390 la foto è 390x510 (60% dello schermo): la riga dei cassoni entra intera e cassoni, fognature e cortili finiscono a 824, 912 e 1000 px, entro 1,2 schermate (1013).
- *Lavori.* "Per privati e cantieri" dice al privato che lavorano anche per lui; "Escavatori a risucchio" è la prima riga di "Per imprese ed enti". Le righe che portano al modulo hanno a destra "Preventivo" con la freccia; le due che portano a una sezione (risucchio, SOA) hanno la freccia sola. Così non si aspetta più una pagina del servizio.
- *Risucchio.* Il culmine comincia a 1657 px a 1440 (1,84 schermate, entro le due della regola ammorbidita; prima 2,2) e a 1716 a 390 (2,03; prima 2,6), perché la serie di foto è scesa in Chi siamo. Arrivando da "Escavatori a risucchio" nel menu, a 1440 foto (88-801 px), didascalia e frase dei materiali (fino a 865) stanno in una schermata. Nella sezione ci sono "Chiama 049 625336" e "Scrivi la richiesta" (sul telefono la chiamata è nella barra), l'email in chiaro a 17 px ("Oppure scrivete a info@fratellizuin.it, o compilate il modulo", con il modulo già su "Escavatore a risucchio") e la riga "Per le fognature c'è anche l'autobotte combinata della Ditta: preventivo per una fognatura", che porta al modulo con "Fognatura". Spurgo e canal jet restano fuori (LEGGIMI, punto 4): il compito "arrivare allo spurgo" si chiude solo con la loro conferma.
- *Sede.* È tornata nel blocco del preventivo (menu "Preventivo e sede"), con la strada dal casello presa dalla loro pagina Dove siamo, che il 3/11 rispondeva, e accorciata senza saltare svolte: "Dall'A4, casello di Padova Est: a destra sul cavalcavia, a metà della discesa a sinistra, al semaforo a destra e poi la prima a destra, Via Madonna del Rosario. Dopo il ponte, Via Bassette è sulla destra; la sede è sulla sinistra dopo 100 m." Il link apre la mappa.
- *Modulo.* "Tipo di lavoro" è il primo campo: chi arriva da una riga vede subito il lavoro scelto. Il messaggio "Mancano: ..." sta in cima al modulo, sotto la frase, e non più sotto il bottone; ogni campo mancante ha `aria-invalid`, un bordo nero e l'etichetta "Manca" collegata con `aria-describedby`, che sparisce quando si scrive. La legend "Per quando" è allineata alle etichette (`padding:0`), e i radio sono disegnati come i campi (22 px, bordo bianco, pallino bianco).

**Sotto la piega**
- *Il gesto torna una volta.* Il maiuscolo condensato nero è solo sulle due scritte dipinte: la frase d'apertura e la scritta della fiancata nel cielo della foto del risucchio (2 elementi in tutta la pagina, prima 7). I titoli di sezione sono in Fira Sans 500 a 34 px, frase normale, interlinea 1,15 (28 px a 390): "Lavori", "Tre generazioni, dal cortile di casa", "Dati della Ditta e attestazione SOA", "Richiedi un preventivo gratuito". Il telefono grande è in Fira Sans 500 a 40 px, cifre tabellari. La frase non torna più nel piede.
- *Una griglia sola.* Dodici colonne, bordi 80-1360 a 1440, e ogni blocco parte dalla colonna 1 o dalla 7: indice dei lavori, sotto-foto del risucchio, storia e lavori in città, serie, dati, preventivo e modulo, piede. Etichette dei gruppi a 17 px nere (prima 24 grigie, come i nomi delle righe: ora il rapporto è 1,4).
- *Il culmine.* 96 px di nero sopra la foto (prima 160) e 160 sotto, per la pausa. La foto domina a 1280 px con la scritta nel cielo; sotto, a sinistra la frase dei materiali a 22 px e la richiesta, a destra la didascalia e le azioni, senza più la colonna vuota di 360 px. Didascalia vera: "Escavatore a risucchio su autocarro MAN a quattro assi / Escavazioni e aspirazioni industriali" (via l'indirizzo della fiancata, che sembrava un riempitivo). Tolto il link "Formazione e sistemazione delle fognature, tra i lavori", che il giudice leggeva come un errore.
- *Moduli di sezione diversi.* Lavori: titolo sopra e due indici affiancati. Risucchio: foto dominante e due colonne sotto. Chi siamo: titolo sopra, storia a sinistra e "Lavori in città, a Padova" a destra in tre righe con filetto (Ex Foro Boario, demolizione, 1968-69; sede dell'Azienda del Gas in Via Trieste, demolizione, dopo il Foro Boario; Prato della Valle, formazione parziale dell'impianto di illuminazione: l'anno c'è solo dove lo danno loro), poi la serie delle due foto. Dati: titolo sopra, frase SOA e bottone sulla stessa riga, dati da copiare su due colonne di tre righe. Preventivo: tre strade per bisogno a sinistra (telefono per cassoni, scavi e lavori piccoli; email per risucchio, imprese ed enti; sede con la strada), modulo a destra. Lo schema "titolo a sinistra, testo a destra" resta una volta sola, nel preventivo.
- *Piede come biglietto da visita*, su bianco: il blocco rosso e il piede nero non si toccano più. Timbro, poi sede, telefono, fax ed email su due colonne, poi la riga legale.
- *Finiture.* `text-wrap:balance` sui titoli, spazi unificatori dove restava una parola sola ("SOA", "m", "fognatura"), "Preventivo gratuito" su una riga da 1100 a 1920 px, la frase d'apertura più piccola (fino a 92 px) negli schermi larghi e bassi: a 1280x720 l'ultima riga finisce a 295 px, sopra le chiome.

**Misure finali** (`node _prova/alto/misura-d.mjs`, esito in `_prova/alto/esito-d.txt`): passano tutte e 77 le soglie. In `misura-d.mjs` ho cambiato quattro cose, scritte nel file: gli spazi di sezione si contano sopra e sotto; le ripetizioni dei contatti seguono C1 e D12 per S (link `tel:` al massimo 5, numero scritto 4, email 3, Via Bassette 6/A 3); il primo campo mancante è "Tipo di lavoro"; c'è il controllo della barra in basso.

| Soglia | Valore |
|---|---|
| Foto nella prima schermata | 80% a 1440, 60% a 390 |
| Cliccabili / bottoni a 1440 | 7 / 1 |
| Cliccabili / bottoni a 390 | 4 / 1, la chiamata |
| Caratteri fuori dal menu a 1440 | 160 (tetto 160) |
| Elementi in condensato maiuscolo | 2 (prima 7) |
| Famiglie, testo corrente, sopra i 100 px | 2; 17 px; 1 (l'h1, 104 px) |
| Parole, sezioni, altezza a 1440 | 641, 6, 5.811 px (prima 5.984) |
| Peso | 0,50 MB a 1440, 0,30 MB a 390 |
| Foto | 4, nessuna ingrandita alle sei larghezze; formati: largo e 3:2 a 1440, più la verticale a 390 |
| Bottoni in pagina | 5 a 1440 (testata, Chiama e Scrivi nel risucchio, SOA, Prepara la mail); 4 a 390 più la barra |
| Spazi di sezione | 96 e 160 px |
| Contatti | 5 `tel:` (testata, risucchio, preventivo, piede, barra), numero scritto 4, email 3, Via Bassette 6/A 3 |
| Visitatore 1, 390 | chiamata in testata 48 px; a metà pagina nella barra (y 784); cassoni, fognature, cortili a 824, 912, 1000 px; "piccola entità" a 1045; sede e mappa nella barra dalla seconda schermata; campo mancante detto per nome con il fuoco sul primo |
| Visitatore 2 | risucchio nel menu e nella riga d'apertura; sezione a 1,84 schermate a 1440 e 2,03 a 390; foto e materiali in una schermata dall'arrivo; chiamata, richiesta, email in chiaro e modulo nella sezione |
| Visitatore 3, 1440 | riga SOA a 1419 px; dati su una schermata; bottone per l'attestazione |
| 320, 390, 768, 1024, 1440, 1920 | niente scorrimento orizzontale, niente testi sovrapposti, nessun errore di script |

Screenshot rifatti con gli stessi nomi (`home-1440.jpg`, `home-390.jpg`, prime schermate a 1440, 390, 1024 e 768, `chiusura-1440.jpg`) e guardati a pezzi, insieme alle viste a 320, 768, 1024, 1280x720, 1366x768 e 1920 e alle prove del telefono (barra, arrivo al risucchio, modulo dopo una riga, invio a vuoto: `_prova/alto/giro2/quattro-390.jpg`).

**Restano aperti**
- Spurgo e canal jet, orari (per "Aperto" e "Chiuso"), luogo e anno delle foto, gli anni dei due lavori in città: tutti nel LEGGIMI, punti 1, 4, 8 e 12.
- A 1440 nel blocco rosso la colonna dei contatti finisce circa 200 px prima del modulo: è il modulo che detta l'altezza.
- Il punto di scala di D5: la frase d'apertura resta a 104 px (oltre i 140 coprirebbe il braccio). I titoli a 34 px fanno da manifesto, come proponeva il giudice.
- Le foto restano il limite sopra il 7,5 (servizio fotografico nel LEGGIMI). I voti del giudice e dei clienti tipo li dà chi giudica.

### Alto livello: ritocco dopo il giudice da agenzia (3/11/2026)

Il giudice da agenzia ha dato 6,5 (prima 5,5): prima schermata riconoscibile, ma sotto la piega la pagina tornava fascicolo, con errori di finitura e il gesto che non tornava sul risucchio. Questo giro corregge i difetti bloccanti e importanti e i compiti dei clienti tipo non riusciti, senza toccare la prima schermata della sezione D (stessa foto, stessa frase, un bottone). La pagina di prima e i suoi screenshot sono in `_prova/alto/prima-del-ritocco/`; le immagini tolte in `_prova/alto/ritocco/img-tolte/`; le prove dei compiti in `_prova/alto/ritocco/compiti.mjs`. Dove i punti qui sotto contraddicono "Che cosa è cambiato", vale questo paragrafo.

- **Modello del mezzo (bloccante).** La didascalia d'apertura diceva "Hitachi EX245": sulla torretta c'è scritto EX215 e sul braccio FIAT HITACHI. Ora è "Fiat-Hitachi EX215 e DAF / Carico di terra", e l'alt dice "L'escavatore arancio Fiat-Hitachi EX215 carica terra nel cassone rosso di un autocarro DAF CF". Corretto anche `DIREZIONE.md`. "CF" resta solo nell'alt: con "Carico di terra" nella didascalia, la prima schermata a 1440 resta a 158 caratteri (il tetto è 160).
- **"Mezzi della Ditta" tolto** dalla didascalia d'apertura e dall'alt: il LEGGIMI (punto 12) lo dà da confermare. Al suo posto c'è un fatto che si vede, "Carico di terra".
- **Fascia sotto la foto.** "Preventivo gratuito" non va più a capo (`white-space:nowrap`, colonne 10-13, didascalia 7-10). Con `wrap.mjs` è alto 30 px, su una riga, a 1100, 1180, 1280, 1366, 1400 e 1440. Le tre voci sono allineate sulla linea di base (`align-items:baseline`), non più con i rientri a mano.
- **Gerarchia sotto la piega.** C'è un solo titolo per i lavori, "Lavori", in condensato a 56 px. "Per casa e cantiere" e "Per imprese ed enti" sono diventate etichette in tondo 24/31 peso 500, in grigio. Il condensato a 56 px resta solo su Lavori, Risucchio e Preventivo. Chi siamo e i Dati vanno a 40 px, come il numero di telefono nel blocco rosso (prima 56). Titoli con `text-wrap:balance` e spazi unificatori dove restava una parola sola a fine riga ("e&nbsp;attestazione", "a&nbsp;risucchio", "attestazione&nbsp;SOA", "ATECO&nbsp;42.11", "Padova&nbsp;Est", "1968-69").
- **Doppione dei titoli.** La sezione `#enti` si chiama "Dati della Ditta e attestazione SOA" e la voce di menu "Dati e SOA". "Per imprese ed enti" resta solo come etichetta dei lavori.
- **Ordine e chiusura (D11).** Le sezioni sono ora Lavori, Risucchio, Chi siamo, Dati e SOA, Preventivo e piede. Il rosso chiude la pagina e c'è un'alternanza in meno: bianco, nero, bianco (Chi siamo e Dati, divisi da un filetto), rosso, nero.
- **Il gesto torna sul risucchio (D1, D7).** La scritta della fiancata, "Escavazioni ed aspirazioni a risucchio controllato", è composta come la frase d'apertura: maiuscolo condensato nero #141414 a 56/54, allineato a destra, in alto a destra nel cielo della foto. Per avere il cielo, `gallery3` è tagliata più in alto (1365x760, `risucchio-cielo`, mostrata al massimo a 1280 px). Il contrasto con il cielo è di 16,8:1. Sotto la foto ci sono la didascalia a sinistra e la frase dei materiali a destra, poi la richiesta. Arrivando da "Risucchio" nel menu, a 1440 titolo, foto (88-801 px) e materiali (fino a 873) stanno in una schermata, grazie allo `scroll-margin` sulla sezione. Sotto i 760 px il titolo sta sopra la foto, in bianco sul nero: il cielo, a quella misura, è alto 40 px.
- **Serie dei lavori (D9, D10).** Le quattro miniature sono diventate due foto di reportage a 6 colonne, in 3:2 (628 px a 1440, file da 820 e 1000/1280 px). Una è lo scavo tra le case, con la terra scaricata sui tubi nel telo; l'altra la pala CAT 928G che carica le macerie. Ognuna ha la didascalia "che cosa si fa / quale riga dell'indice". L'autobotte esce finché lo spurgo non è confermato, la demolizione per il doppione. La serie mostra che cosa si fa, non lavori con il nome.
- **Culmine senza miniature.** Tolti i due dettagli da 248 px ("Visto da dietro", "Rosso e blu, con il timbro"). La pagina a 1440 è alta 5.984 px, sotto i 6.000 di D8. In `misura-d.mjs` la soglia è tornata a 6.000.
- **Lavori a Padova (D9).** Sede dell'Azienda del Gas e Prato della Valle non hanno l'anno, e non si inventa. I tre lavori non sono più presentati come righe di prova: stanno nella storia, con l'unico anno che c'è ("La prima demolizione importante è l'ex Foro Boario di Padova, negli anni 1968-69; in città seguono..."). Via anche "una vasta gamma di mezzi", frase generica.
- **Compiti dei clienti tipo.** Le righe dei lavori portano a `#modulo` e non più a `#preventivo`. Sul telefono il modulo compare così in cima allo schermo, con il tipo già scelto (`f-tipo` a 397 px a 390, a 291 a 1440). Nel risucchio c'è il link "Formazione e sistemazione delle fognature, tra i lavori", che porta alla riga Fognature, e da lì al modulo con "Fognatura". A 390 cassoni, fognature e cortili finiscono a 852, 942 e 1009 px, entro 1,2 schermate (1013). La sede si trova da Menu, "Contatti e sede", in vista a 548 px. Il risucchio comincia più in basso di prima (2,5 schermate a 1440), ma si arriva con un clic dal menu, e lì titolo, foto e materiali stanno insieme.

**Respinti o rimandati**
- Il punto di scala a 104 px (riserva su D5) non è stato portato oltre i 140 px: a 140 la frase coprirebbe il braccio dell'escavatore, e la prima schermata non si tocca.
- Il risucchio non è stato portato più in alto: servirebbe di nuovo la fila degli ingressi, oppure il culmine prima dei lavori. Ci si arriva dal menu.
- La sede non torna entro due schermate a 390. "Via Bassette 6/A" compare già due volte (contatti e dati), che è il tetto delle ripetizioni. Si arriva dal menu.
- Le foto (55% della distanza secondo il giudice) restano quelle d'archivio: per andare sopra l'8 serve il servizio fotografico del LEGGIMI.

### Che cosa è cambiato

- **Idea e gesto (D1).** Una Ditta di famiglia che dal 1946 arriva con i suoi mezzi "in qualsiasi situazione e spazio". La frase è loro (pagina Azienda: "scarrabili anche di piccole dimensioni della larghezza di una automobile in grado di intervenire in qualsiasi situazione e spazio"), accorciata e non inventata. È composta in maiuscolo condensato nero nel cielo della foto, allineata a destra sopra l'escavatore che carica il cassone rosso, come una scritta dipinta su un mezzo. Lo stesso trattamento torna sul risucchio, con la scritta della loro fiancata ("Escavazioni ed aspirazioni a risucchio controllato"), e nel piede, con la frase.
- **Modello F (D4)**, la foto a tutta pagina con la didascalia, come dice il capitolo 5 (riferimenti Eberhard e Brandenburg). Il nome di un lavoro come titolo (Brandenburg) non si può usare: l'unico lavoro con nome e anno è l'ex Foro Boario del 1968-69, e la sua foto non c'è.
- **Prima schermata a 1440.** Testata bianca fissa con il timbro, cinque voci (Lavori, Risucchio, Chi siamo, Enti e imprese, Contatti e sede) e "Chiama 049 625336", unico bottone. Sotto c'è la foto a tutta larghezza (`pagina-iniziale-1`, 2000 px), mostrata alla scala della sua larghezza e mai ingrandita, con la frase. In una fascia bianca: la riga del mestiere e del luogo ("Scavi, scarrabili e fognature a Padova Est, dal 1946"), la didascalia a due voci e il link "Preventivo gratuito". Tolti il titolo-elenco, l'occhiello, il secondo bottone, l'indirizzo e la fila nera dei sei ingressi.
- **Prima schermata a 390.** Testata fissa con il timbro, "Chiama 049 625336" (l'unico bottone) e "Menu" senza riquadro. La stessa scena è tagliata in verticale (camion e braccio, 692 px), con la frase nel cielo; sotto, la riga e il link. In fondo allo schermo cominciano le righe dei lavori.
- **Sotto la piega, i contenuti della versione professionale su una griglia a 12 colonne** (contenitore di 1280 px, margini di 80, 40 e 20 px, bordi destri tutti a 1360 a 1440):
  1. **Lavori**: due indici a righe, "Per casa e cantiere" (Cassoni scarrabili 2-25 m³, Fognature, Cortili e passi carrai, Scavi e movimento terra, Ritiro di macerie e terra) e "Per imprese ed enti" (Demolizioni, Strade e urbanizzazioni, Escavatori a risucchio, Lavori pubblici con attestazione SOA). Ogni riga ha la frase loro e porta al modulo con il tipo di lavoro già scelto. Sotto c'è la serie di quattro foto 4:3 con la didascalia a due voci. Le sei schede con foto sono diventate righe, perché le foto dei lavori sono quattro.
  2. **Culmine, il risucchio**: su nero, con 160 px di spazio invece di 96. La scritta della fiancata è il titolo, accanto c'è la loro frase sui materiali, poi la foto dominante 2:1 a 1280 px (`gallery3`, 1365 px) con la didascalia "Escavatore a risucchio su autocarro MAN a quattro assi / Sulla fiancata: Via Bassette 6, Padova". Seguono la richiesta per email con la traccia, l'indirizzo in chiaro a 14 px accanto al comando e due dettagli (`gallery4`, `gallery5`, questa nuova).
  3. **Chi siamo**: la storia con le loro parole (fratelli, cortile, DOGE, figli, tre generazioni) e i soci che compaiono nella ragione sociale (Antonio, Luigi e Andrea Zuin). I tre lavori a Padova sono in righe.
  4. **Preventivo e contatti**, l'unico blocco rosso: "Richiedi un preventivo gratuito", il numero (l'unica cifra oltre i 30 px della pagina), email con traccia, fax, sede operativa con le indicazioni a parole (dal loro "Dove siamo") e il link alla mappa. Il modulo è quello della versione professionale: quattro campi obbligatori, il campo mancante detto per nome con il fuoco sopra, la mail composta. Senza JavaScript il modulo cade su `mailto:`.
  5. **Per enti e imprese**: la frase SOA, "Chiedi l'attestazione SOA" e i dati da copiare (ragione sociale, P.IVA e CF, REA, ATECO, sede legale e operativa).
  6. **Piede** come biglietto da visita: timbro, frase, nome, P.IVA, Privacy, Cookie. Il menu ripetuto non c'è più.
- **Tolti** anche la fascia delle cifre (1946 a 144 px, 3 generazioni, 2-25 m³, 30-250 q, quest'ultima da confermare), la fascia delle qualifiche (i dati sono passati agli enti), gli occhielli di sezione e 4 dei 6 link `tel:`. "Spurgo" e "canal jet" escono dalla pagina: nel LEGGIMI sono da confermare. La riga si chiama "Fognature" e il modulo ha "Fognatura".
- **Caratteri (D5).** Sofia Sans, quella indicata, è già in 3 home. Al suo posto **Fira Sans Extra Condensed 800** (frase e titoli, maiuscolo) e **Fira Sans 400 e 500** (testo), SIL OFL 1.1, in `sito/fonts/` con `OFL.txt`. Fira non è in nessun'altra home. Archivo esce.
- **Foto.** `assets/originali/` era vuota dopo il riavvio: l'ho riscaricata oggi dal loro sito con l'API `wp-json/wp/v2/media` e ho tolto le foto del tema, di repertorio e di cronaca. Un trattamento solo (`_prova/alto/script/foto.py`): livelli comuni ai tre canali contro la foschia, il 35% della correzione verso il neutro, una curva leggera, alte luci a 244, saturazione 0,88. In pagina ci sono 8 foto in WebP con srcset. Le misure dei formati sono nella tabella qui sotto. Provini: `_prova/alto/provini.jpg`.

### Misure

`node _prova/alto/misura-d.mjs`, cioè `misura.mjs` della diagnosi esteso alle soglie D e ibride. L'esito è in `_prova/alto/esito-d.txt`, i dati in `_prova/alto/misure-d.json`. Passano tutte e 76 le soglie (dopo il ritocco, con l'altezza tornata alla soglia di D8, 6.000 px).

| Soglia | Valore |
|---|---|
| Foto nella prima schermata | 80% a 1440, 67% a 390 |
| Cliccabili / bottoni a 1440 | 7 (massimo 8 per S) / 1 |
| Cliccabili / bottoni a 390 | 4 / 1, la chiamata |
| Caratteri fuori dal menu a 1440 | 158 (massimo 160) |
| Fila di ingressi, cifre di 30 px o più nella prima schermata, occhielli | 0, 0, 0 |
| `h1` | 5 parole, 0 virgole, 104 px a 1440 e 46 a 390; unico elemento sopra i 100 px |
| Famiglie, testo corrente | 2; 17 px o più (19 per il testo, 17 per le righe) |
| Parole, sezioni, altezza a 1440 | 590 (prima 830), 6 sezioni, 5.984 px (prima 7.998; 6.027 prima del ritocco) |
| Peso caricato | 0,52 MB a 1440, 0,32 MB a 390 |
| Foto, formati, ingrandite | 4 (prima del ritocco 8); a 1440 la scena larga e 3:2, a 390 anche la verticale; nessuna mostrata oltre i suoi pixel, alle sei larghezze |
| Didascalie | 4 su 4 a due voci, nessuna ripetuta |
| Fondi | bianco, nero (culmine) e rosso (un blocco solo); spazi di sezione 96 e 160 px |
| Ripetizioni | 2 `tel:`, numero scritto 2 volte, email 2, Via Bassette 6/A 2, nessun link più di 2 volte, 4 bottoni in pagina |
| Controlli a 320, 390, 768, 1024, 1440, 1920 | niente scorrimento orizzontale, niente testi sovrapposti, nessun errore di script; tutti i `tel:` sono +39049625336 e tutti i `mailto:` vanno a info@fratellizuin.it |

**Compiti della scheda e dove stanno ora**
- *Privato, 390*: "Chiama 049 625336" sta nella testata fissa (44 px), si tocca in cima e a metà pagina. "Cassoni scarrabili 2-25 m³", "Fognature" e "Cortili e passi carrai" finiscono a 830, 919 e 987 px, entro 1,2 schermate (1013), e "anche di piccola entità" a 1010. La richiesta parte dal link "Preventivo gratuito" della prima schermata o da una riga, che sceglie il tipo nel modulo. La sede è in "Contatti e sede", dal menu.
- *Tecnico, 1440 e 390*: "Risucchio" è nel menu, la sezione comincia a 2,2 schermate a 1440 e a 2,6 a 390 (dal menu o dalla riga "Escavatori a risucchio"). Titolo, materiali e foto stanno insieme in una schermata. La richiesta per email ha la traccia, l'indirizzo è scritto in chiaro e la chiamata è nella testata fissa.
- *Ente, 1440*: la riga "Lavori pubblici con attestazione SOA" è a 1379 px, nella seconda schermata. I dati si copiano da una schermata sola, l'attestazione si chiede con un clic, la storia e i tre lavori a Padova sono in "Chi siamo".

Screenshot (gli stessi nomi di prima): `home-1440.jpg` e `home-390.jpg` (intere, con la testata resa statica solo per la cattura), le prime schermate a 1440, 390, 1024 e 768, `chiusura-1440.jpg` (preventivo, enti, piede). Li ho guardati a pezzi accanto alla versione professionale (`_prova/versione-pro/screenshot/home/`) e alle prime schermate di Eberhard e Brandenburg rifatte oggi (`_prova/alto/concorrenti/`). Le viste di lavoro sono in `_prova/alto/viste/`.

### Problemi aperti

1. **Didascalie senza luogo e anno.** Non sappiamo dove e quando sono state fatte le foto. Le didascalie dicono che cosa si vede e un fatto visibile (l'indirizzo dipinto sulla fiancata, il carico nel cassone). "Mezzi della Ditta" non c'è più: torna quando l'azienda conferma che le foto sono sue (LEGGIMI, punto 12).
2. **Il risucchio è più in basso di quanto chiedesse la scheda** (2,5 schermate a 1440 e 2,8 a 390 dopo il ritocco). Per la sezione D il compito passa perché si arriva dal menu con un clic, e all'arrivo titolo, foto e materiali stanno in una schermata; tenerlo più in alto voleva dire tornare alla fila degli ingressi.
3. **La sede non è più entro due schermate a 390**: compare già due volte (contatti e dati della Ditta), che è il tetto delle ripetizioni. Si arriva dal menu "Contatti e sede" (in vista a 548 px dopo il tocco).
4. **Spurgo**: il compito "arrivare allo spurgo" del tecnico non si può fare finché l'azienda non conferma il servizio (LEGGIMI, punto 4). Quando lo conferma, va in testata come voce a sé, se c'è il pronto intervento.
5. **Foto**: luce di mezzogiorno con foschia, nessuna persona, lavori finiti senza foto. La composizione dell'apertura dipende da questa foto, con la frase nel cielo a destra: se la foto cambia, la frase va rimessa dove il fondo è libero. Sugli schermi ad alta densità la foto d'apertura è servita a 2000 px, sotto i 2880 che servirebbero. Sopra l'8, per il gruppo S, serve il servizio fotografico del LEGGIMI.
6. **Controlli non fatti da me**: la prova D1 (tre persone e le miniature a 300 px) e i voti del giudice da agenzia e dei clienti tipo vanno dati da chi giudica. Il controllo D4 dell'ondata (`media-prime-schermate.jpg` della zona) si fa quando tutte le home della zona sono rifatte.
7. Orari, zone servite e PEC non ci sono ancora (LEGGIMI, punti 1, 2 e 6).
8. Nella riga di `REGISTRO-CARATTERI.md` è scritto "d apertura" senza apostrofo, per l'escape nel comando di aggiunta. Non l'ho corretto per non riscrivere un file che altri agenti scrivono in parallelo.

---

*Nota di prima (versione professionale, 3/11/2026). Descrive la home salvata in `_prova/versione-pro/`.*


La home di prima (fondo giallo, la parola "risucchio" a tutta pagina, nove lavori in una frase da toccare, sei foto Unsplash "indicative") è salvata con la sua nota in `_prova/versione-1-originale/` (sito e screenshot). Questa nota descrive la home di oggi.

Screenshot in questa cartella: `home-1440.jpg` e `home-390.jpg` (pagine intere), `home-1440-prima-schermata.jpg` e `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (preventivo, enti, dove siamo, piede).

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di Eggentaler e di Wilson, a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`. Questo giro applica il controllo del livello professionale (voto 6) e le prove dei due clienti tipo (privato a 390, tecnico a 1440).

### Che cosa è cambiato in questo giro e perché

- **Apertura a 1440 con la foto vera a destra**, come chiede la scheda (par. 4) e come fanno Eggentaler e Kline: griglia 7/5, a sinistra occhiello, H1 a 64 px, la riga loro, "Chiama 049 625336" e "Scrivi per un preventivo", l'indirizzo con la mappa; a destra una foto verticale 4:5 alta 633 px, l'escavatore della Ditta che carica il cassone rosso del DAF (`pagina-iniziale-1`, 2000 px, ritagliata a 704x880 e servita senza ingrandire). Via il pannello di sei riquadri bordati, che sembrava un'interfaccia.
- **Le sei voci in una striscia nera sotto l'apertura**, sei colonne divise da filetti verticali, testo bianco: tutte e sei dentro la prima schermata a 1440. A 390 restano dov'erano (sotto i bottoni, prima dell'indirizzo), ma senza bordo: righe a due colonne con filetto, alte 52 px, con la freccia rossa. "Strade e cortili" diventa "Cortili e passi carrai" (le strade sono già nel titolo): il privato legge "passi carrai" senza toccare.
- **Sotto i 900 px la foto dell'apertura è la stessa scena intera** (striscia larga, art direction con `<picture>`): a 390 resta alta 140 px in fondo alla prima schermata.
- **Un gesto di scala nella seconda schermata**: "1946" a 144 px (52 a 390) con "La Ditta nasce nel cortile di casa dei tre fratelli Zuin, con il primo autocarro, un DOGE."; accanto tre cifre a 48 px in righe con filetto: 3 generazioni, 2-25 m³ cassoni scarrabili, 30-250 q autocarri (dato del sito `.com`, in SCHEDA par. 1). "SOA" non è più una cifra.
- **Fascia delle qualifiche**, con filetti e senza loghi (non abbiamo il certificato): Attestazione SOA, qualificazione per i lavori pubblici; REA PD 82662, iscritta alla Camera di Commercio di Padova; ATECO 42.11, costruzione di strade e autostrade.
- **Serie fotografica** (`_prova/script/pro_img.py`): stessa curva per tutte. Blu del cielo spenti del 45%, saturazione -15%, alte luci compresse fino a 240 (il bianco bruciato diventa il grigio chiaro della pagina), bilanciamento appena freddo. Nelle 4:3 il taglio scende perché il cielo stia attorno al 20% (ritiro, demolizioni, fognature, scavi). La scheda "Scavi e movimento terra" usa ora `movimento-terra-1000x800-1` (stessa giornata dell'apertura, altro punto di vista), così nessuna foto si ripete.
- **Risucchio**: la frase corretta ("Scavi controllati e aspirazione di qualsiasi materiale: liquido, secco, solido e polveri, anche in luoghi confinati"); i quattro materiali come testo in grassetto separato da punti, non più riquadri che sembrano bottoni; l'autobotte combinata è un link alla scheda "Fognature e spurgo"; la riga "Portata, profondità di scavo e lunghezza del tubo: chiedetecele al telefono, per il vostro lavoro"; i bottoni sotto la foto (niente vuoto nero) e "oppure scrivete a info@fratellizuin.it" in chiaro, da copiare se il computer non ha un programma di posta. "Quantità indicativa" diventa "quantità approssimativa" (anche nella mail).
- **Sul telefono il risucchio viene subito dopo l'apertura** (comincia a 747 px, la foto si intravede già in fondo alla prima schermata), poi le cifre e le qualifiche: il tecnico vede foto e materiali entro la seconda schermata come prima; a 1440 l'ordine resta apertura, cifre, risucchio (il risucchio comincia a 1,54 schermate).
- **Schede dei servizi a 390**: foto a tutta larghezza in 3:2 e il testo sotto, invece della miniatura con il testo in una colonna di 182 px.
- **Lavori a Padova** in righe con filetto (nome a 24 px, a destra tipo e anno), non più schede grigie con "Città Padova" ripetuto.
- **Per enti e imprese** in una sezione a sé su grigio, dopo il preventivo: il privato arriva prima al modulo. "Dove siamo" passa a bianco.
- **Modulo**: nessuna scelta preimpostata su "Per quando" (se resta vuota la mail dice "Per quando: da concordare"); le righe dei campi facoltativi vuoti (email, descrizione) non compaiono nella mail.
- **Testata**: timbro a 128 px a 1440 (testata 88 px) e 84 px a 390 (testata 72). **Piede**: link alti 44 px per il dito, voce "Dati per enti e imprese".

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 72 a 390, bottone rosso "049 625336" alto 48 px con la cornetta; a metà pagina si vede e si tocca (`elementFromPoint`) a 1440 e a 390. 6 link `tel:`, tutti `tel:+39049625336`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con mestiere, "Padova" e "dal 1946"; a 1440 bottone di chiamata a 609 px, foto intera (633 px), le sei voci e l'indirizzo dentro i 900 px; a 390 bottone a tutta colonna (350 su 350) a 251 px, "Scrivi", le sei voci, l'indirizzo con la mappa e la foto (140 px) dentro gli 844 px.
3. **Immagine vera nell'apertura: passa, con riserva.** Escavatore e autocarro con il cassone rosso al lavoro, foto loro; nessun oggetto scontornato. Riserva: nessuna persona, e la provenienza della foto è "loro (probabile)" (LEGGIMI, foto).
4. **Zero repertorio: passa.** `grep -ci indicativ index.html` = 0; in `sito/img/` solo foto e logo dal loro sito (`assets/originali/`); nessuna Unsplash o Pexels.
5. **Foto in serie: passa.** Otto foto dallo stesso archivio con lo stesso trattamento (sopra); formati: a 1440 4:5, 2:1 e 4:3; a 390 striscia 2,79:1, 2:1 e 3:2; nessuna didascalia; nessuna ingrandita. Restano foto d'archivio di giornate diverse: il livello di Klindworth o Wilson arriva solo con la ripresa nuova (LEGGIMI).
6. **Palette dal marchio: passa.** `--rosso` #B42620 (cassoni), `--rosso-scuro` per il passaggio del mouse, `--nero` #141414 (timbro), `--bianco`; grigi neutri freddi. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 24, 48, 64, 144) e 7 a 390 (14, 16, 18, 20, 30, 34, 52); testo corrente 17 e 16 px; niente sotto i 14 px; H1 64/34, H2 48/30.
8. **Due famiglie al massimo: passa.** Una sola, Archivo, pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 1024 e 768, una a 390), sei schede con foto loro, stesso taglio (4:3, 3:2 sul telefono), nome e link, tutta la scheda cliccabile. Strade, cortili, urbanizzazioni e SOA in elenco a righe: le foto di questi lavori non ci sono.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 cifre (1946, 3 generazioni, 2-25 m³, 30-250 q) e la fascia delle qualifiche con didascalia (SOA, REA, ATECO). Mancano recensioni (nessuna in rete) e clienti con il nome: non si inventano (LEGGIMI punti 9 e 10).
11. **Lavori con un nome: non passa.** Tre lavori con luogo e tipo (Ex Foro Boario 1968-69, Azienda del Gas di Via Trieste, Prato della Valle), anno solo per il primo, nessuna foto e nessun numero. Servono lavori recenti con committente, anno, dati e foto (LEGGIMI punto 8).
12. **Ritmo a blocchi: passa.** Bianco (apertura), nero (striscia, cifre, qualifiche, risucchio), grigio (lavori), bianco (chi siamo), rosso (preventivo), grigio (enti), bianco (dove siamo), nero (piede): 3 blocchi pieni oltre al piede. Sezioni a 120 px a 1440 e 72 a 390; contenitore 1280 px, margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e bordato (nero sul chiaro, bianco sul nero), raggio 4 px, 56 px (48 in testata e Menu), testo 17 e 16 px; i bottoni di chiamata contengono il numero. Tolti gli altri stili bordati (riquadri delle voci, materiali); restano solo le radio del modulo, che sono controlli.
14. **Modulo e "dove" per il mestiere: non passa (manca l'elenco dei comuni).** Modulo con nome, telefono, email, tipo di lavoro (10 voci), indirizzo del lavoro, descrizione, per quando (nessuna scelta preimpostata) e l'istruzione per le foto (un mailto non porta allegati); nessun iframe di mappa. Le zone servite non sono note (LEGGIMI punto 2).
15. **Piede completo: non passa (mancano orari e zone).** Quattro colonne, testo di almeno 14 px, logo, nome, telefono, fax, email, sedi con la mappa, lavori, P.IVA, REA, SOA, Privacy e Cookie. Orari, zone e PEC non sono nelle fonti (LEGGIMI punti 1, 2 e 6).

### Compiti dei clienti tipo e della scheda (par. 8)

- *Privato, 390*: bottone tel: alto 56 px a 251 px, la testata con il numero resta fissa; "Cassoni scarrabili 2-25 m³", "Fognature e spurgo" e "Cortili e passi carrai" visibili senza toccare; "Via Bassette 6/A, Padova Est" visibile e apre Maps; "Scrivi per un preventivo" apre con un tocco l'email con oggetto e traccia (indirizzo, foto); il modulo arriva prima dei dati per gli enti; nessun orario inventato.
- *Tecnico, 1440 e 390*: a 1440 il risucchio comincia a 1,54 schermate, foto e "liquido, secco, solido e polveri" nella seconda schermata (a 390 la sezione comincia a 0,88 schermate); chiamata, email ed email in chiaro dalla sezione; l'autobotte porta alla scheda dello spurgo.
- *Ente, 1440*: SOA, REA e ATECO nella seconda schermata; ragione sociale, P.IVA, sedi in "Per enti e imprese" e nel piede, senza fisarmoniche; storia dal 1946 e tre lavori di Padova per nome.
- Prove automatiche (`pro_controlli.mjs`): menu del telefono aperto e chiuso; "Dove siamo" sotto la testata; la scheda "Fognature e spurgo" sceglie "Fognatura o spurgo" nel modulo; invio vuoto fermato con "Mancano: nome e cognome, telefono, indirizzo del lavoro." e il fuoco sul nome; email composta senza la riga vuota "Email:" e con "Per quando: da concordare"; nessun errore di script.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700.
- Foto e logo: solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `sh _prova/script/build_finale.sh`: immagini, pagina, controlli di testo, screenshot, `pro_controlli.mjs` (regole 1-9, 12 e 13 superate nelle misure; 10, 11, 14 e 15 no, per i motivi sopra).
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura e nessun testo che esce da bottoni, schede, cifre o qualifiche.
- Screenshot guardati a pezzi a 1440 e a 390, prime schermate e pezzi a 320, 768 e 1024. Nessun U+2014 in pagina, nelle note e negli script.
