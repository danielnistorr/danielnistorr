# Metodo ibrido (novembre 2026)

3 novembre 2026. Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale com'era (sito e screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`.

## Secondo giro (3 novembre 2026)

Dopo il ritocco il giudice da agenzia dava 7, ma i clienti tipo erano scesi (azienda di prodotto da 8 a 6: in prima schermata leggeva "è il fotografo delle imprese stradali" e in testata non trovava come scrivere). Questo giro recupera i compiti persi senza toccare i tetti D3 e rifinisce la metà bassa. Dove questa sezione e le righe sotto non coincidono, vale questa. Copia della pagina prima del giro: `_prova/alto/giro2/index-prima.html` (con lo script delle immagini, `controlli.mjs` e gli screenshot di prima nella stessa cartella).

**Per i clienti tipo**
- **Prima schermata, una riga sola cambiata.** Sotto "Foto e video di cantiere" ora c'è "AIT Studio, Mestrino (PD). Anche prodotti e architettura." (sul telefono "AIT Studio, Stefano Aiti, Mestrino (PD). ..."): chi viene per uno still life lo legge in 3 secondi, e chi conosce Stefano per nome lo trova anche sul telefono. Foto e titolo restano come erano.
- **Testata.** Sul computer: le cinque voci (Cantieri, Prodotti, Architettura, Clienti, Preventivo), il numero scritto in chiaro e un solo bottone, "Scrivici", che apre l'email a stefano@stefanoaiti.com con l'oggetto già scritto (il compito 4 dell'azienda di prodotto). Il numero sul computer non è un link, così i cliccabili restano 6. Sul telefono: il numero è un bottone pieno nero di 48 px, sempre in alto, e "Menu" (Matrimoni e "Scrivici a info@aitistudio.it" in più). Lo stato aperto o chiuso non c'è: gli orari non sono nelle fonti (scritto nel LEGGIMI). La barra in basso non l'ho messa: il numero è già fisso in alto e i `tel:` sono già 3, il massimo per M1.
- **La seconda schermata è l'indice dei tre campi.** "Per chi abbiamo lavorato" è salito subito sotto l'apertura, a 982 px a 1440: tre colonne con il nome del campo come link ("Cantieri e mezzi", "Prodotti e design", "Architettura e arredo", ognuno con la freccia e 44 px di bersaglio) e i 17 clienti sotto. Sotto c'è lo studio: Stefano e Giulia, la sala di posa, lo Iuav e il 2008 a 1266 px, dentro le due schermate. Nessuna miniatura nell'indice: le foto in home restano 12 (D10).
- **Sul telefono l'impresa viene prima.** Sotto i 600 px l'ordine è apertura, Cantieri, lo studio e i clienti, Prodotti, Architettura, Preventivo, Matrimoni (con `order`, solo CSS): la seconda schermata del capocantiere è il culmine di Padova. Sul computer l'ordine resta quello di prima.
- **I servizi si toccano tutti interi.** Ogni riga 01-04 è un solo link (numero, nome e descrizione), alta 113 px a 390 invece dei 27 px di prima.
- **Il modulo.** 7 campi invece di 9, e "Cosa fotografare" è il primo: cosa, entro quando, dove, per quale uso, nome e azienda, telefono o email, due righe. Sul telefono il modulo viene prima dei contatti: dopo il tocco su "Livree dei mezzi" la tendina con "Livree dei mezzi" sta a 246 px, nello schermo, e sotto il bottone c'è "per info@aitistudio.it" (provato con un tocco vero in `controlli.mjs`). A 1440 il blocco è alto 781 px (era circa 1000).
- **I lavori con il luogo.** Dopo il tocco su "Cantieri": Padova (culmine, con la didascalia del video), Verona Sud, la galleria Girardini (luogo da chiedere), e nella riga dei servizi "Cantieri di Salima e Girardini a Mirano, Padova, Verona Sud, Carpane (VI) e Massenza (TN).", presa dai nomi dei file e dai titoli dei video di aitistudio.it. Così il Trentino torna, come fatto e non come elenco di zone.
- **Prodotti più grandi.** Le quattro still life sono due per due, 437x291 a 1440 (erano 322x215), e accanto c'è "Tutto il portfolio su stefanoaiti.com".
- **Matrimoni.** "Chiama per la data, 348 748 58 71" è la prima riga dell'indice, con Weddgraphy, le recensioni e l'email: dopo il tocco su "Matrimoni" voto, chiamata, Weddgraphy e recensioni stanno nello schermo a 390 (provato).

**Sotto la piega**
- **Il gesto torna una volta.** La regia dell'apertura (titolo bianco in basso a sinistra sulla foto, la riga dello scatto sotto) torna una sola volta, nel culmine: "Cantieri e mezzi" sta sulla foto di Padova con la riga dei servizi, e l'ancora #cantieri mostra la parola "Cantieri" insieme alla foto e alla didascalia intere (80-877 px a 1440x900). La riga con i dati dello scatto è solo sotto l'apertura e sotto il culmine, e comincia con **"EXIF"** (difetto del giudice: data e ora erano scritte come fatti certi; ora descrivono il file). Sotto gli altri lavori c'è solo il mese e l'anno.
- **Didascalie vere.** Il culmine dice che cosa succede: "Salima, Padova, di notte: asfaltatura delle vie per il passaggio del Giro d'Italia" (dal titolo del video; "di notte" dall'ora 0:09). La seconda voce di tutte le didascalie, anche di prodotti e architettura, è in monospaziato a 15 px, che a occhio fa la stessa altezza della x di Albert Sans a 16.
- **Due imprese, non una.** Il ritratto Salima davanti al Volvo (HDR, la foto più debole) esce; entra la finitrice Girardini in galleria con l'operaio (`Studio-Aiti-Foto-cantieri-3.jpg`, `l-galleria` 3:2, stesso trattamento). Le foto restano 12.
- **Una griglia sola, tre linee di partenza.** Tutti i testi partono dalle colonne 1, 5 o 9 delle 12: testa delle sezioni a 1 e 5, studio, colonna dell'architettura e contatti a 9, indice dei matrimoni a 5 fino al bordo destro (niente più bottone a 5 e link a 9 con 280 px di vuoto). Bordi 40/1400 a 1440 e 20/370 a 390 in tutte le sezioni.
- **Moduli di sezione diversi.** Lo studio è foto e colonna; Cantieri si apre con la foto; Prodotti ha il testo a lato (fermo mentre si scorrono le foto) e le foto due per due; Architettura, Preventivo e Matrimoni hanno la testa con il filetto. Prima erano sei teste uguali.
- **La frase-firma** chiude la colonna dello studio sul piede della foto (e torna nel piede): non è più una riga sola tra due vuoti.
- **Spazi.** Tre valori soli: 40 px tra la testa e il contenuto, 64 px tra blocchi della stessa sezione, 104 e 160 px tra le sezioni (160 prima del culmine); sul telefono 32, 48, 72 e 112.
- **Gerarchia.** I nomi dei clienti e dei servizi passano da 22 a 18 px: 22 resta solo agli `h2`, 32 al manifesto.
- **Finiture.** "Sala di posa" in vista 2 volte (titolo dello studio e dei prodotti; il menu e la tendina dicono "Prodotti"); "sei" banche e "107esimo" tolti dalle frasi (numeri in frase: 1995, 2008 e quelli dei matrimoni); `text-wrap:pretty` anche su didascalie e descrizioni; a 320 la riga dello scatto sta su una riga (mono a 13 px sotto i 360); "1.000 euro" non si spezza.
- **Privacy e Cookie** del piede portano a due pagine segnaposto vere (`sito/privacy/`, `sito/cookie/`), non più a un errore.

**Respinto, con il motivo**
- **Miniature dei tre campi nell'indice**: avrebbero portato le foto in home a 15 (D10 ne vuole 12).
- **Il marchio come link e "Altri cantieri" in prima schermata**: a 1440 i cliccabili diventerebbero 7. Sul telefono la strada ai cantieri è lo scorrimento (Cantieri è la seconda schermata) o il menu.
- **Il numero del piede come link**: sarebbe il quarto `tel:` (D12, massimo 3 per M1). Restano testata, contatti e "Chiama per la data".
- **Modulo a 5 campi**: "per quale uso" ed "entro quando" sono nel compito dell'azienda di prodotto; a 7 campi il blocco scende a 781 px.
- **Saturazione di Padova a 0,88 in più, originali da 3200 px**: vanno chiesti a Stefano (LEGGIMI).

**Misure finali** (`_prova/alto/misura-d.mjs`, tabella in `_prova/alto/misure/tabella.txt`): passano tutte e 39. Cliccabili 6 a 1440 e 2 a 390, bottoni 1 e 1, 155 caratteri a 1440 (145 a 390), foto nella prima schermata 81% a 1440 e 68% a 390, `h1` di 5 parole, 0 occhielli, 521 parole, 7 sezioni, altezza 7417 px a 1440 (era 7359) e 8855 a 390, 12 foto, 0 ingrandite, formati 1,78 1,50 1,33 a 1440 e 0,80 1,50 1,00 a 390, 2 fondi oltre al piede, culmine 1360x797, 3 `tel:`, 1 mappa, 2 bottoni in pagina (erano 3), peso 682 KB a 1440 e 352 KB a 390, 0 errori. Controlli (`_prova/alto/controlli.mjs`, ora con la prova del tocco su "Livree dei mezzi" a 390) a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione, nessuna foto ingrandita, nessun errore, nessun bersaglio sotto i 24 px, nessuna àncora rotta. Screenshot rifatti con gli stessi nomi e guardati a pezzi. U+2014: nessuno.

## Alto livello: ritocco dopo il giudice da agenzia (3 novembre 2026)

Il giudice da agenzia ha dato 7 (prima 6): la prima schermata regge accanto a Hufton + Crow e Iwan Baan, ma sotto la piega la pagina era "corretta ma senza regia", il culmine non entrava nello schermo, i prodotti erano miniature su quattro bianchi diversi e la riga dello scatto "bisbigliava". Dove questa sezione e le righe sotto non coincidono, vale questa. Copia della pagina prima del ritocco: `_prova/alto/rit/index-prima.html`; script delle immagini di prima: `_prova/alto/rit/immagini-prima.py`.

**Applicato**
- **La riga dello scatto si legge (difetto 4).** Spline Sans Mono a 16 px in nero (14 px solo sotto i 600), e il tempo di posa dall'EXIF dopo data e ora: "18 marzo 2023, 19:19, posa 1,3 s" sotto Mirano (spiega le scie di luce), "posa 1/60 s", "1/100 s", "1/1600 s" sotto i lavori. Per restare nei 160 caratteri della prima schermata ho tolto "le" ("per imprese di strade e costruzioni"), "ore" da tutte le righe e "(VE)" da Mirano (ora scritto come Padova e Verona Sud): 157 caratteri.
- **Forma corta sul telefono (difetto 7).** Sotto i 600 px la data è "18.3.2023, 19:19" (due span alternati nel markup, niente JavaScript); sui lavori il tempo di posa sparisce, sull'apertura resta perché ci sta. A 390 ogni riga dei lavori è su una riga sola (31 px con il filetto sopra, 21 di testo). Tra 901 e 1180 px le coppie usano la stessa forma corta.
- **Il culmine (difetti 1, 2 e 3).** Il culmine ora è la fresatura notturna Salima a **Padova** (18 maggio 2024, ore 0:09): il luogo è nel titolo del video di cui la foto è la copertina su aitistudio.it/video-storytelling ("Padova - Asfaltatura vie urbane per il passaggio del 107esimo Giro d'Italia"), quindi non è più da indovinare. 16:9 (`l-padova`, taglio cy 0,55) con `max-height:calc(100svh - testata - 56px)`, e **apre la sezione Cantieri**, prima del titolo: dopo il clic su "Cantieri" a 1440x900 foto e riga stanno intere nello schermo (foto da 80 a 845, riga fino a 877). Sotto i 600 px va a filo dello schermo, 1:1 (`l-padova-q`, 1267 px, non ingrandita): 390x390 contro 350x233 delle altre. È anche la regia che mancava: Cantieri è l'unica sezione che si apre con la foto.
- **Persone nei cantieri (difetto 3).** Massenza (Volvo in posa, HDR) e Carpane (mezzi lontani tra montagne e guardrail) escono. La coppia ora è **Salima, A4 Verona Sud** (operaio con le cuffie ai comandi, al tramonto; il luogo è nel titolo del video "A4 Verona Sud - Manutenzione straordinaria") e **Salima, foto aziendale** (il ritratto davanti all'escavatore Volvo, 13 dicembre 2021, ore 13:06). Due foto su tre di cantiere hanno una persona in primo piano; tre lavori su quattro hanno impresa e luogo (Mirano, Padova, Verona Sud). Restano 12 foto. La stesa notturna (`Studio-Aiti-Foto-cantieri-6`) l'ho tenuta fuori: senza luogo, e la notte la dice già Padova.
- **"Fotografiamo il cantiere quando lavora, anche di notte" tolta (difetto 5).** Resta "Reportage di cantiere, foto aziendali, livree dei mezzi, video e siti web per le imprese di strade e costruzioni. I cantieri di queste foto sono in Veneto." (Trentino esce con Massenza.) `grep "anche di notte" sito/index.html`: 0.
- **Still life rifiniti (difetto 6).** Nello script delle immagini un passaggio solo sul bianco porta i quattro fondi a 245,245,244 (angoli misurati: 243-245 su tutte e quattro), le tessere hanno `background:#F5F5F4`, e ogni oggetto è ritagliato al 65% dell'altezza della tessera. Superoro passa dalla collana (che usciva dai bordi) all'anello (`Superoro-5.jpg`): didascalia "Superoro, anello". Riga della sezione: "Oggetti, gioielli e componenti, fotografati nella nostra sala di posa a Mestrino."
- **Architettura, piedi allineati (difetto 8).** Sopra i 1180 px Banca Prealpi è 4:3 con un file tagliato apposta (`a-prealpi-43`, cx 0,85, la persona resta dentro), e la colonna di destra è alta quanto la foto grande (flex, spazio in mezzo): scarto tra i due piedi 0 px a 1440 e a 1920. Sotto i 1180 px la foto grande va a tutta larghezza e le due piccole affiancate sotto. Formati a 1440: 16:9, 3:2, 4:3 (3).
- **Filetti uguali in testa a ogni sezione (difetto 9).** Ogni apertura di sezione (lo studio, Cantieri, Prodotti, Architettura, Preventivo, Matrimoni) ha lo stesso filetto nero di 1 px con 16 px sopra il titolo, come "Per chi abbiamo lavorato" e "Per le imprese".
- **La seconda metà meno da modello.** Matrimoni: titolo e dati nella stessa testa delle altre sezioni ("4,9 su 5 con 9 recensioni su Matrimonio.com. Servizio da 1.000 euro."), "Chiama per la data" da solo, e Weddgraphy, le recensioni e info@weddgraphy.it come righe d'indice con filetto e freccia, non più quattro azioni in fila. Nei contatti "Prodotti e architettura" ha ora la persona (Stefano Aiti), come "Cantieri e imprese" (D12).
- **A 390 la foto dello studio è 3:2** come i lavori, così i formati sul telefono restano 3 (4:5, 3:2, 1:1).
- File tolti da `sito/img/`: `l-carpane-*`, `l-massenza-*`, `l-fresatura-*` e i vecchi `p-*`; nuovi `l-padova-*`, `l-padova-q-*`, `l-verona-*`, `l-ritratto-*`, `a-prealpi-43-*`, `p-*` (script `_prova/alto/script/immagini.py`). LEGGIMI aggiornato (didascalie e date da confermare, frasi tolte).

**Respinto, con il motivo**
- **D9, l'anno sotto ogni lavoro d'architettura**: Banca Prealpi, Studio 4 Marmicolor e Fornace Morandi non hanno EXIF né un anno nelle fonti. Resta la categoria finché Stefano non li dà; non li metto a caso.
- **Gli originali da 3200 px e Stefano al lavoro** (la parte del 55% che dipende dalle foto): vanno chiesti, non si fanno da qui.
- **La riga dello scatto leggibile nella miniatura a 300 px**: a 300 px un testo di 16 px diventa di 3 px e non si legge con nessun corpo compatibile con D3 e D5. Ora è nera e più lunga e nella miniatura si vede come riga, ma non si legge.
- **Prodotti più grandi (2x2)**: avrebbero portato la pagina oltre i 7500 px a 1440. Restano in fila, rifiniti.

**Misure dopo il ritocco** (`_prova/alto/misura-d.mjs`, tabella in `_prova/alto/misure/tabella.txt`): passano tutte e 39. Cliccabili 6 / 2, bottoni 1 / 1, caratteri 157 a 1440, foto nella prima schermata 81% a 1440 e 63-67% a 390, 0 occhielli, `h1` di 5 parole, 535 parole, 7 sezioni, altezza 7359 px a 1440 (era 7423), 12 foto, 0 ingrandite, formati 1,78 1,50 1,33 a 1440 e 0,80 1,50 1,00 a 390, culmine 1360x797 con la riga (era 1360x939), 3 `tel:`, 1 mappa, 3 bottoni in pagina, peso 584 KB a 1440 e 329 KB a 390. Controlli (`_prova/alto/controlli.mjs`) a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione, nessuna foto ingrandita, nessun errore, nessun bersaglio sotto i 24 px, nessuna àncora rotta; scheda "Livree dei mezzi" porta al modulo con il lavoro scelto e info@aitistudio.it; "Clienti" a 17 nomi; matrimoni a 390 con voto, "Chiama", Weddgraphy e recensioni nello schermo dopo il tocco. Verifica del culmine e delle righe: `_prova/alto/rit/verifica.mjs`. A 320 le righe di Mirano, Verona Sud e della foto aziendale vanno su due righe (a 390 no). U+2014: nessuno.

## Che cosa è cambiato

- **Idea e gesto (D1).** AIT Studio fotografa i cantieri quando lavorano, e ogni foto porta scritto chi, dove e a che ora è stata scattata. Il gesto è **la riga dello scatto**: sotto la foto, a sinistra impresa e luogo, a destra data e ora in monospaziato ("18 marzo 2023, ore 19:19"), come il bordo di un provino. Torna sotto ogni lavoro di cantiere (dopo il ritocco: Padova 0:09, Verona Sud 19:19, foto aziendale 13:06, con il tempo di posa). Data e ora vengono dall'EXIF dei file.
- **Apertura, modello F (D2, D4).** Lo Scania di Salima sull'asfalto nuovo a Mirano, ripreso rasoterra la sera, a tutta larghezza: 1360x765 a 1440 (81% della prima schermata), 390x487 in 4:5 a 390 (63%). In basso a sinistra, sull'asfalto, "Foto e video di cantiere" (32 px, 500) e la riga "AIT Studio, per le imprese di strade e costruzioni. Mestrino (PD)". Sotto la foto la riga dello scatto. Nessun bottone sulla foto. Come Hufton + Crow e Iwan Baan (`_prova/alto/concorrenti/confronto-1440.jpg`, con la versione professionale accanto).
- **Testata fissa.** Segno AIT e "Stefano Aiti", cinque voci (Cantieri, Prodotti, Architettura, Clienti, Preventivo) e il telefono "348 748 58 71" come unico bottone, bordato, 44 px. A 900 px e meno: segno AIT, telefono e "Menu" (un `<details>`, funziona anche senza JavaScript), con Matrimoni e "Scrivici a info@aitistudio.it" in più. Niente barra in basso: il telefono è già fisso in alto e i `tel:` restano 3.
- **Foto rifatte dagli originali.** `assets/originali/` era stata cancellata con il riavvio: ho riscaricato le foto dai due siti dello studio (31 da aitistudio.it in `assets/originali/aitistudio/`, 154 dai portfolio di stefanoaiti.com in `assets/originali/portfolio/`). Provini: `_prova/alto/provini.jpg`. WebP con srcset in `sito/img/` (script `_prova/alto/script/immagini.py`), un solo trattamento (saturazione 0,88, contrasto 0,97), tre formati (16:9, 3:2, 4:5 solo per l'apertura sul telefono). Le JPEG di prima sono tolte da `sito/img/` (copia in `_prova/versione-pro/`).
- **Sotto la piega, su una griglia di 12 colonne** con margini di 40 px (32 a 768, 20 a 390) e gli stessi bordi destri in tutte le sezioni:
  1. **Lo studio e i clienti**: Stefano Aiti e Giulia Morandin nella sala di posa (foto a4, 7 colonne), il testo a destra (lauree Iuav, "dal 1995", "dal 2008" in una frase), la frase-firma "«Le foto sono comunicazione silenziosa.»" a 32 px, e "Per chi abbiamo lavorato" con 17 nomi in tre campi.
  2. **Cantieri e mezzi**: una riga con i servizi in parole loro, "anche di notte" e "in Veneto e in Trentino"; il **culmine**, Girardini a Carpane a tutta larghezza (1360x907); Massenza e la fresatura notturna Salima affiancate; i quattro servizi come righe d'indice numerate 01-04, ognuna un link al modulo con il lavoro già scelto.
  3. **Prodotti in sala di posa**: Calearo, Marijke, Calegaro, Superoro, quattro still life su bianco in fila.
  4. **Architettura e interni**: Banca Prealpi di Artufficio (8 colonne), la scala di Studio 4 Marmicolor e la Fornace Morandi (4 colonne).
  5. **Chiedi un preventivo**: lo stesso modulo (9 campi, mailto con oggetto e testo, indirizzo che cambia con il tipo di lavoro) e i contatti divisi per bisogno: cantieri e imprese (Stefano, telefono, info@aitistudio.it), prodotti e architettura (stefano@stefanoaiti.com), lo studio con "Vai alla mappa". Sul telefono i contatti vengono prima del modulo.
  6. **Matrimoni**: Stefano Aiti Weddgraphy, 4,9 su 5 con 9 recensioni, servizio da 1.000 euro, "Chiama per la data", Weddgraphy, le recensioni su Matrimonio.com e info@weddgraphy.it.
  - Piede nero come biglietto da visita: la frase-firma, il logo, lo studio, i contatti, i lavori, la riga legale.
- **Tolto**: il titolo nero a 64 px e i due bottoni, le tre porte in apertura, la fascia dei quattro numeri, gli otto occhielli maiuscoli, le fasce grigie e nere alternate, le tre recensioni dei matrimoni (il LEGGIMI dice che vanno ricontrollate parola per parola), il secondo "Scrivici" in testata, due "Vai alla mappa" su tre, due `tel:` su cinque, i quattro "Chiedi un preventivo" ripetuti delle schede, le quattro foto delle schede di cantiere (le foto in home passano da 18 a 12).
- **Caratteri (D5).** Albert Sans 400 e 500 per tutto, Spline Sans Mono 400 solo per data, ora e numeri dei servizi; entrambi SIL OFL 1.1, in `sito/fonts/` con le licenze `OFL-albert-sans.txt` e `OFL-spline-sans-mono.txt`. Switzer esce. Misure: 32, 22, 18, 16, 14 px. Riga aggiunta in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.
- **Colori.** Bianco (le sale di posa: gli still life si fondono con la pagina), nero del logo, grigio del logo #AAAEAD per i filetti, chiaro #EEEFEE solo per il preventivo, piede nero. Il testo bianco sulla foto d'apertura ha una sfumatura locale sotto il testo (mediana 14,5:1, nel caso peggiore misurato 4,4:1 con i bordi delle lettere nel conto); la foto non è scurita in blocco.

## Le misure

`_prova/alto/misura-d.mjs` (da `misura.mjs` della diagnosi, esteso alle soglie D e del metodo ibrido; tabella in `_prova/alto/misure/tabella.txt`, dati in `misure.json`). **Passano tutte e 39.**

| Misura | Oggi | Soglia | Versione pro (stesso script, `_prova/alto/misure-pro/`) |
|---|---|---|---|
| Cliccabili 1440 / 390 | 6 / 2 | 6 / 4 | 15 / 7 |
| Bottoni 1440 / 390 | 1 / 1 | 1 / 1 | 4 / 5 |
| Caratteri fuori dal menu 1440 / 390 | 157 / 149 | 160 | 516 / 393 |
| Foto nella prima schermata 1440 / 390 | 81% / 63% | 60% o meno del 12% / 50% | 32% / 25% |
| Cifre di 30 px o più in pagina | 0 | 1 | 7 |
| `h1` | 5 parole, 0 virgole | 9 / 1 | 9 parole, 2 virgole |
| Occhielli | 0 | 0 | 8 |
| Parole | 538 | 900 | 752 |
| Sezioni | 7 | 7 | 8 |
| Altezza 1440 / 390 | 7423 / 8986 px | 7500 a 1440 | 10115 / 12694 |
| Griglia | un bordo (40/1400 a 1440, 20/370 a 390), 12 colonne | uno | griglie diverse per sezione |
| Foto / formati / ingrandite | 12 / 2 a 1440, 3 a 390 / 0 a tutte le larghezze | 12 / 3 / 0 | 18 / 2 a 1440, 4 a 390 / 0 |
| Fondi oltre al piede | 2 | 3 | 3 con alternanza |
| Spazi tra sezioni | 104 e 160 px (culmine) | due, uno 1,5 volte l'altro | 128 ovunque |
| `tel:` / mappa / bottoni in pagina | 3 / 1 / 3 | 3 / 1 / 5 | 5 / 3 / 8 |
| Peso caricato 1440 / 390 | 1008 / 380 KB | 3 MB | 1225 / 871 KB |
| Famiglie | Albert Sans + Spline Sans Mono (dati) | 2 + mono | Switzer |

Controlli (`_prova/alto/controlli.mjs`, `misure/controlli.json`) a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione (il testo sulla foto d'apertura è voluto ed è escluso dal conto), nessun errore di script né risorsa mancante, nessuna foto mostrata oltre la misura del file (misurata ricaricando il file scelto dal srcset), nessun bersaglio sotto i 24 px fuori dal piede. Collegamenti: `tel:+393487485871` 3 volte (testata, contatti, matrimoni); `mailto:` a info@aitistudio.it (con oggetto, menu e contatti), stefano@stefanoaiti.com, info@weddgraphy.it, la PEC; Google Maps su Via Galileo Galilei 40, Mestrino; weddgraphy.it e Matrimonio.com; nessuna àncora rotta. U+2014: nessuno.

Screenshot rifatti con gli stessi nomi, più due nuovi: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `home-1024-prima-schermata.jpg`, `home-768-prima-schermata.jpg`, `chiusura-1440.jpg` (dal preventivo al piede). Guardati a pezzi accanto alla versione professionale e alle prime schermate di Hufton + Crow e Iwan Baan (`_prova/alto/concorrenti/`).

## I compiti della scheda, dove stanno ora

- **Impresa, telefono.**
  - "AIT Studio", "cantiere" e una foto vera di cantiere: tutto nella prima schermata a 390 (foto al 63%, `h1` e riga sotto).
  - Chiamare: testata fissa con il numero leggibile, bottone di 44 px, in primo piano anche a metà pagina.
  - Tre lavori: Mirano è l'apertura; "Cantieri" nel menu (un tocco) porta a Carpane e Massenza con impresa, luogo, data e ora, e alla fresatura notturna. Nella stessa schermata del tocco c'è la riga con livree, video e siti, "anche di notte", "in Veneto e in Trentino".
  - Preventivo: la riga "Livree dei mezzi" porta al modulo con il lavoro già scelto e l'indirizzo info@aitistudio.it scritto sotto il bottone (provato). Il modulo ha 9 campi.
- **Azienda o architetto, computer.**
  - I tre campi sono le prime tre voci del menu, Mestrino è nella riga dell'apertura. Non c'è più una foto per campo nella prima schermata: le foto di prodotti e architettura sono alla quarta e quinta schermata, a un clic dal menu.
  - Quattro still life e tre architetture con il cliente sotto, nessuna ingrandita.
  - "Clienti" nel menu porta a 17 nomi divisi per campo; Stefano e Giulia, la sala di posa, lo Iuav e il 2008 sono alla seconda schermata (titolo a 982 px).
  - "Preventivo" nel menu: modulo con cosa, dove, entro quando, per quale uso, e accanto l'indirizzo con "Vai alla mappa". La voce "Scrivici" non c'è più: in testata c'è "Preventivo".
- **Sposi, telefono.** "Matrimoni" nel menu; dopo il tocco, senza scorrere, voto, 9 recensioni, prezzo, "Chiama per la data", Weddgraphy e Matrimonio.com (provato). Il numero si legge nella testata fissa, non più dentro il bottone.

## Problemi aperti

- **Le date e i luoghi dei lavori vengono dai file** (EXIF e nomi pubblicati su aitistudio.it): vanno confermati con Stefano come prima. La fresatura notturna Salima sembra davanti a Santa Giustina a Padova, ma il luogo non è scritto.
- **Il terzo lavoro con il luogo**: chiuso nel ritocco (Padova e Verona Sud dai titoli dei video; la foto aziendale è senza luogo).
- **La foto d'apertura** è di 1900 px: a 1440 regge, sugli schermi ad alta densità è un po' morbida. Servono gli originali da almeno 3200 px (come scritto nel LEGGIMI).
- **"Fotografiamo il cantiere quando lavora, anche di notte"** è tolta finché non è confermata; va chiesto se è un servizio che offrono sempre.
- **A 1440 la soglia dei caratteri è al limite** (157 su 160): ogni parola in più in apertura va tolta da un'altra parte.
- **Le recensioni dei matrimoni** sono fuori finché non sono ricontrollate sulla scheda di Matrimonio.com.
- Restano da collegare il modulo (allegati, privacy) e da fare le pagine `privacy/` e `cookie/`.

---

# Home di AIT Studio, Stefano Aiti: livello professionale, ritocco finale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La home di prima ("Comunicazione silenziosa"), con la sua NOTA, è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot).

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs`, poi `pro_controlli.mjs`). Prove d'uso della scheda: `node _prova/script/pro_uso.mjs`. Scorrimento orizzontale, elemento per elemento: `node _prova/script/trova_largo.mjs <larghezza>`. Larghezze delle lettere in Chromium: `node _prova/script/kern_prova.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (dal preventivo al piede). Misure: circa 10100 px a 1440 e 12700 a 390.

## Livello professionale

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati per questo ritocco: le prime schermate a 1440 e 390 di tutti e 14 e le pagine intere di Odermatt, Budri e Holzrausch, a pezzi (prima erano state viste Cly-Del e barth).

### Che cosa cambia nel ritocco finale (dal controllo del livello e dalle prove dei clienti tipo)

- **Un gesto di scala in apertura.** Prima le foto erano tre tessere di 411x308 a 1440 e tre miniature di 96x96 a 390. Ora:
  - a 1440 il titolo sta a sinistra (8 colonne) e a destra ci sono la riga del luogo e i due bottoni impilati;
  - sotto, la porta Cantieri è grande (7 colonne, 737x414, 16:9): la stesa notturna con il semirimorchio Salima, con il marchio leggibile;
  - accanto, Prodotti e Architettura sono due porte più piccole, con la foto e i clienti, e sotto c'è la riga dei matrimoni;
  - a 390 la porta Cantieri è a tutta larghezza (350x197) e le altre due sono righe con la miniatura da 80 px. Tutte e tre stanno nella prima schermata.
- **Luogo e prova in chiaro.** L'occhiello dice "AIT Studio, Stefano Aiti" (chi conosce AIT Studio dai mezzi ha subito la conferma). Sotto il titolo, in 18 px nero (17 a 390): "Studio fotografico a Mestrino (PD), dal 2008. Lavoriamo in Veneto e in Trentino."
- **Bottoni senza doppi spazi.** L'etichetta è chiusa in un solo span ("Chiama Stefano 348 748 58 71", "Chiama per la data 348 748 58 71").
- **Spaziatura delle lettere.** "Stef ano", "St udio", "Mest rino": Chromium su Linux arrotondava le larghezze delle lettere (la f a 16 px passava da 4,8 a 7 px, misurato con `kern_prova.mjs`). Con `text-rendering:geometricPrecision` sul body la f torna a 5,1 px e le parole si chiudono.
- **Pesi distanti.** Switzer 400 e 700 (prima 400 e 600), come chiede A4.
- **Cantieri senza schemi ripetuti.** Dopo le quattro schede, "Lavori recenti 2022-2023" apre con la foto di Mirano a tutta larghezza (fino a 1600 px, 16:9) e prosegue con Carpane e Massenza affiancati (6+6). "Avete un cantiere da documentare? Scriveteci" viene dopo le foto, non prima.
- **Lavori con anno e tre dati.** "Salima, Mirano (VE) · marzo 2023 · reportage di cantiere", "Girardini, Carpane (VI) · ottobre 2022 · cantiere Anas, reportage", "Salima, Massenza (TN) · marzo 2022 · parco mezzi, Volvo FL250". Mese e anno vengono dall'EXIF dei file originali. Tolto "all'alba" da Mirano: l'EXIF dice ore 19:19.
- **Prodotti con quattro foto e il nome.** Testo a lato (4 colonne, fermo mentre si scorre) e quattro still life in 2x2: Calearo (prima c'era solo nella porta, senza nome), Marijke, Calegaro, Superoro. A 390 restano in 2x2, così la sezione è corta.
- **Architettura speculare e con Studio 4 Marmicolor.** Foto grande a destra (Artufficio, Banca Prealpi), a sinistra la scala di Studio 4 Marmicolor e la Fornace Morandi, ognuna con il nome. Tolta Brendola, che ripeteva Artufficio.
- **Clienti come testo.** I nomi sono composti in 44 px (28 a 390), separati da un punto, con il campo in 14 px maiuscolo sopra ogni gruppo. Prima erano tre colonne in 24 px.
- **Numeri veri.** Tolti "2 lauree" e "5 servizi". Ora: 1995, 2008, "2 persone: ideazione, scatto ed editing, tutto fatto da noi", "6 banche e casse rurali arredate da Artufficio, fotografate da noi" (01-analisi, sez. 1). Le lauree Iuav sono nel testo dello studio.
- **Ritmo.** Il chiaro passa da #EDEFEE a #E2E4E3 (stesso grigio del logo), così i blocchi chiari si distinguono dal bianco. Il testo secondario #565A59 sul chiaro resta a 5,5:1.
- **Menu e contatti.** Il menu ora ha Cantieri e mezzi, Prodotti, Architettura, Clienti, Matrimoni, Preventivo (6 voci); sul telefono c'è anche "Scrivici a info@aitistudio.it". "Lo studio" è il primo blocco dopo l'apertura e non serve nel menu. Le email nei contatti sono bersagli alti 44 px.
- **Modulo.** La tendina parte da "Scegli il tipo di lavoro". L'email va a info@aitistudio.it per i lavori di cantiere e a stefano@stefanoaiti.com per gli altri, e sotto il bottone è scritto a quale indirizzo parte. La frase sugli allegati è in nero a 16 px.
- **Matrimoni dopo il preventivo.** Per chi viene per lavoro non è più un intoppo tra i clienti e il modulo. Chi cerca i matrimoni ha la riga in apertura e la voce nel menu.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile: PASSA.** Testata `position:sticky`, 80 px a 1440 e 72 a 390. A 390, scorsa a metà pagina, il bottone "348 748 58 71" (48 px) si vede e si tocca. In pagina ci sono 5 link `tel:`. Voce di richiesta M: "Preventivo" nel menu e "Scrivici" in testata a 1440.
2. **Prima schermata con mestiere, luogo, prova, azione: PASSA** a 1440x900 e 390x844. Mestiere nell'H1; luogo e prova ("Mestrino (PD), dal 2008") nella riga in 18 px nero sotto il titolo; azione "Chiama Stefano 348 748 58 71", a 390 a tutta larghezza.
3. **Immagine vera nell'apertura: PASSA.** La stesa notturna di AIT Studio con il semirimorchio Salima, grande: 737x414 a 1440, 350x197 a 390. Accanto l'antenna Calearo e la scala di Studio 4 Marmicolor, foto loro.
4. **Zero repertorio: PASSA.** "indicativ", Pexels, Unsplash ed `esterne/` compaiono 0 volte. Le uniche immagini non fotografiche sono i due SVG del logo.
5. **Foto in serie: PASSA IN PARTE, con una deroga dichiarata.**
   - Formati: 2 a 1440 (16:9 e 4:3), 3 a 390 (16:9, 4:3 e 1:1 per le due miniature).
   - Didascalie: 18 foto, 10 con il nome sotto (3 lavori di cantiere con i dati, 4 still life, 3 di architettura), cioè circa 1 ogni 2. La prima stesura diceva "6 su 19": il conteggio era sbagliato. Le righe che descrivevano solo ciò che si vede ("vaso di cubetti metallici", "la facciata in mattoni" e simili) sono tolte.
   - Deroga: per un fotografo il nome del cliente sotto la foto è il fatto che conta (A7: cliente, luogo, anno), e la scheda chiede "ogni foto con il nome del cliente". Restano solo nomi e dati, mai descrizioni.
   - Luce: non può essere una sola, perché lo studio vende tre generi (notte di cantiere, bianco di sala di posa, interni). Ogni genere sta nella sua sezione, e le foto di cantiere sono calmate insieme (saturazione 86 %, contrasto 96 %).
6. **Palette dal marchio: PASSA.** Cinque token: bianco, nero del logo (#0B0A0A dal #040000), grigio del logo #AAAEAD, chiaro #E2E4E3 (lo stesso grigio schiarito), testo secondario #565A59. Niente beige.
7. **Scala corta e leggibile: PASSA.** 6 misure a 1440 (64, 44, 24, 18, 16, 14) e 8 a 390 (44, 34, 28, 20, 17, 16, 15, 14). Testo corrente 18 px a 1440 e 17 a 390. Niente sotto i 14 px. H1 64 px a 1440 (fascia M 60-70) e 34 a 390 (34-40).
8. **Due famiglie al massimo: PASSA.** Una sola, Switzer, come barth: 700 per titoli, nomi, cifre e bottoni, 400 per il testo.
9. **Servizi in schede con foto: PASSA.** Quattro schede per le costruzioni, 4 colonne a 1440 (2 a 1024 e 768, 1 a 390), foto 4:3, nome, una riga con le loro parole e "Chiedi un preventivo". Tutta la scheda è il link e porta al modulo con il tipo già scelto (provato: "Livree dei mezzi" arriva nel campo, e l'email va a info@aitistudio.it).
10. **Almeno tre tipi di prove: PASSA (3 su 4).** Clienti con il nome (17, per campo, come testo grande); quattro numeri dalle fonti (1995, 2008, 2 persone, 6 banche e casse rurali); tre recensioni vere con nome, mese e fonte (Matrimonio.com, solo dei matrimoni; il comune non è nella fonte). Certificazioni: nessuna (TAU Visual da confermare, nel LEGGIMI).
11. **I lavori hanno un nome: PASSA.** Tre lavori di cantiere con cliente, luogo, mese e anno e il tipo di servizio; Mirano è a tutta larghezza (1440 px), Carpane e Massenza a 628 px ciascuno. In più tre lavori di architettura con il cliente (anni da chiedere, nel LEGGIMI).
12. **Ritmo a blocchi: PASSA.** Due blocchi neri (cantieri, clienti) più il piede, tre chiari (studio, architettura, matrimoni) e tre bianchi alternati. Spazio tra le sezioni 128 px a 1440 e 72 a 390. Margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 2 px ovunque, 52 px (48 in testata), testo 16 px in 700. I bottoni di chiamata contengono il numero, senza doppi spazi.
14. **Modulo e "dove e quando": PASSA IN PARTE.** Nome, azienda, telefono, email, cosa fotografare (tendina vuota all'inizio, con sette lavori più "Altro"), dove, entro quando, per quale uso, messaggio; mailto con oggetto e campi (provato). Indirizzo con "Vai alla mappa", zone scritte, nessun iframe. Manca il campo allegato chiesto per M: un mailto non porta file e un campo finto non funzionerebbe. È il primo campo da aggiungere quando il modulo sarà collegato a un servizio (LEGGIMI).
15. **Piede completo: PASSA, senza orari né certificazioni** (non sono nelle fonti, chiesti nel LEGGIMI). Quattro colonne: logo e mestiere, lavori, lo studio, contatti; riga legale con ragione sociale, P.IVA, PEC, Privacy e Cookie; testo di almeno 14 px.

### Prove d'uso della scheda (`_prova/script/pro_uso.mjs` e screenshot)

- **Impresa di costruzioni, 390x844.** Senza scorrere: "AIT Studio" nell'occhiello, "cantieri" nel titolo, la stesa Salima grande e leggibile, due `tel:` (testata e bottone a tutta larghezza). Un tocco sulla porta porta alla sezione. Livree, video, Salima, Girardini e Martini Silvestro sono nell'introduzione della sezione; le zone sono lì e nei contatti. Nel menu c'è "Scrivici a info@aitistudio.it". Come prima o meglio.
- **Azienda o architetto, 1440x900.** Senza scorrere: mestiere, i tre generi, Mestrino, telefono e "Scrivici". Un clic su "Prodotti" porta a quattro still life con il cliente sotto, Calearo compreso; un clic su "Architettura" a tre lavori con il cliente, Studio 4 Marmicolor compreso. "Clienti" e "Preventivo" sono nel menu. Il preventivo dice cosa scrivere e ha l'indirizzo con la mappa; il blocco matrimoni non sta più in mezzo.
- **Coppia di sposi, 390x844.** "Matrimoni" è nel menu (un tocco: voto 4,9, prezzo, "Chiama per la data" e "Vai a Weddgraphy" visibili) e c'è la riga con il voto subito sotto le porte, all'inizio della seconda schermata.

### Controlli generali

- Screenshot guardati a pezzi a 1440 e 390 (interi e prime schermate) e a 320, 768 e 1024; il menu aperto a 390.
- **Scorrimento orizzontale**: nessuno a 320, 390, 768, 1024, 1280, 1440 e 1920. Trovato e corretto durante il lavoro: i nomi dei clienti senza spazi tra i separatori (ora il punto resta attaccato al nome che lo precede e non apre mai una riga).
- **Immagini ingrandite oltre la misura del file**: nessuna, a nessuna larghezza (corretti i `sizes` per 1024, 1280 e 1920).
- **Collegamenti**: `tel:+393487485871` 5 volte; `mailto:` per stefano@stefanoaiti.com (con oggetto), info@aitistudio.it, info@weddgraphy.it e la PEC; Google Maps su Via Galileo Galilei 40, 35035 Mestrino; weddgraphy.it e la scheda di Matrimonio.com; nessuna àncora rotta. Restano i link a `privacy/` e `cookie/`, pagine da fare.
- **U+2014**: nessuno, nella pagina, in questa NOTA, nel LEGGIMI, nei CREDITI e negli script.

### Caratteri e licenze

Switzer (Indian Type Foundry, da Fontshare), pesi 400 e 700, con la ITF Free Font License, che permette l'uso commerciale gratuito. I file woff2 sono serviti dalla pagina in `sito/fonts/`. Il 700 è stato scaricato da Fontshare il 3/11/2026; la copia è in `assets/fonts-scaricati/`.
