# Argenteria Varotto Alfredo, direzione artistica della home HE

Scritta il 7 novembre 2026, prima dell'HTML, seguendo `_metodo/highend/SISTEMA.md` (punto 3) e le lezioni dei piloti (Bottega dell'Arte 6,7, Foralberg 7,4, Ruffatti 7,5, Tacchificio Riviera). Pagina: `sito-he/index.html`. La `sito/` di oggi non si tocca. Il committente vuole una home "più high-end, più fashion, più di design".

## 1. La cosa vera

Il catalogo dell'argento Varotto Alfredo, sul loro sito, è fatto di pezzi in argento massiccio con il loro nome e il loro codice, uno per uno: "Posto tavola in argento massiccio 6 pezzi stile Inglese classico BL83006", "Servizio 77 pz in argento massiccio pesante stile Inglese BL83001P", "Brocca martellata in argento massiccio stile Inglese BB01200AG", "Candelabro 5 fiamme in argento massiccio stile Inglese VAG-Z1595.30". Insieme fanno la tavola intera, come dice la pagina Azienda: "vassoi, piatti, sottopiatti, [...] servizi da caffè, zuccheriere, alzate, centri tavola, [...] secchielli champagne e ghiaccio, [...] candelabri, bugie, [...] posate". Accanto, l'altro mestiere, con la loro frase: "la vostra argenteria tornerà al suo originario splendore" (pagina Assistenza).

L'idea in una riga: **tutta la tavola, in argento, un pezzo alla volta: ogni pezzo sta da solo sul suo campo chiaro, alla misura della sua foto, con il nome e il codice del catalogo, come nella vetrina di una maison.** Le foto sono di catalogo (al massimo 1280 px), quindi la pagina non le ingrandisce mai: le mostra a metà della misura nativa o poco più, nitide anche sugli schermi retina.

Fuori dalla pagina, perché "da confermare" (01-analisi sez. 9, LEGGIMI punti 7 e 8): il punzone 364 PD e la produzione nello stabilimento di Padova (a chi è intestato il punzone, se la produzione è dell'impresa), il 1974 contro "agli inizi degli anni '70", gli orari, i rapporti tra Alfredo e Luca Varotto, i marchi Royal Queen, Royal England, Sweet Home e TEN, i social dello shop. La storia di Alfredo Varotto entra solo come citazione della pagina Azienda, senza la data.

## 2. Riferimenti guardati

Aperti con Playwright il 7/11/2026: prima schermata a 1440x900 e a 390x844 e tre scorrimenti da 900 px a 1440. Schermate in `_prova/he/riferimenti/<nome>-1440-prima-schermata.jpg`, `-1440-scorrimento-1/2/3.jpg`, `-390-prima-schermata.jpg` (script `_prova/he/script/riferimenti.mjs`, che chiude cookie e finestre). Christofle con l'indirizzo italiano risponde "Page introuvable": guardata la home americana. Sambonet mostra una finestra "Vuoi ricevere un regalo di benvenuto?" che copre gli scorrimenti: contano la prima schermata e il primo scorrimento.

**Argenteria e tavola**

1. **Puiforcat** (puiforcat.com).
   - Mossa 1: il nome in un serif tagliente e grande davvero ("Tomás Alonso" a circa 250 px), nero sul bianco, senza altro intorno. Da noi: "999" e "Argento massiccio" in Rowan 300, oltre i 200 px.
   - Mossa 2: i pezzi piccoli dentro una griglia di filetti sottili, ognuno con un'etichetta minima ("Verre 01"). Da noi: la vetrina a ripiani, un filetto per ripiano e sotto ogni pezzo il nome e il codice del catalogo.
   - Da non prendere: il carosello, la finestra dei cookie al centro.
2. **Christofle** (christofle.com).
   - Mossa 1: un solo colore del marchio, pieno, che fa da cornice (l'oliva della barra). Da noi: il blu del loro marchio, pieno solo nell'apertura.
   - Mossa 2: il nome della linea come identità del pezzo (Perles, Albi, Malmaison). Da noi: lo stile del catalogo nel nome di ogni pezzo (Inglese, Impero).
   - Da non prendere: la barra piena di voci, i prezzi, la finestra dei cookie.
3. **Georg Jensen** (georgjensen.com).
   - Mossa 1: i prodotti tutti con la stessa inquadratura su campi uguali ("Popular products"). Da noi: le sei impugnature nella stessa finestra quadrata, la testa alla stessa altezza.
   - Mossa 2: il candelabro da solo su un tavolo con molta aria. Da noi: il candelabro a cinque fiamme da solo sul primo ripiano, accanto al titolo.
   - Da non prendere: la barra dei cookie, le schede editoriali con l'etichetta azzurra sopra il titolo.
4. **Buccellati** (buccellati.com).
   - Mossa 1: il pezzo tagliato da vicino e grande, sul bianco (il bracciale d'oro in primo piano). Da noi: la testa di leone in argento 999 alla misura nativa, tagliata sotto il collare.
   - Mossa 2: dopo una foto grande, una fila di pezzi piccoli con il nome sotto. Da noi: la fila delle sei teste sotto il leone.
   - Da non prendere: le modelle, il testo maiuscolo spaziato sulle foto.
5. **Broggi** (broggi.it, posateria dal 1818).
   - Mossa 1: le posate d'argento sul nero, illuminate da un lato. Da noi: le posate Inglese nella finestra chiara dentro il blu.
   - Mossa 2: la storia in poche righe accanto a un solo oggetto. Da noi: la citazione della pagina Azienda su Alfredo Varotto, da sola, in una fascia.
   - Da non prendere: i pallini del carosello, il bottone a pillola marrone.
6. **Greggio** (greggio.com, Padova, lo stesso distretto).
   - Mossa 1: i pezzi scontornati sul bianco in fila, appoggiati alla stessa linea. Da noi: i ripiani della vetrina.
   - Mossa 2: tavola e regalo vicini ai servizi. Da noi: hotel e ristoranti e riparazione subito dopo i pezzi.
   - Da non prendere: la foto di sala carica, il titolo in Jost sottile sulla foto, il nastro di testo.
7. **Sambonet** (sambonet.com).
   - Mossa 1: una frase centrata e un solo bottone nero ("Il meglio per ogni ospite"). Da noi: un solo bottone pieno per sezione, che si inverte di colpo.
   - Da non prendere: la finestra del regalo, le icone delle categorie, le stelle delle recensioni in testata.

**Premiati su Awwwards in settori vicini** (premi letti in `_metodo/professionale/alto/awwwards.md`)

8. **Kevala Ceramics** (kevalaceramics.com), ceramiche da tavola per hotel e ristoranti, Menzione d'onore 22/2/2024.
   - Mossa 1: la superficie di un solo pezzo come immagine (la ciotola granulosa a tutta pagina). Da noi: all'inizio la finestra mostra solo il dettaglio delle posate, poi si apre sul pezzo intero.
   - Mossa 2: una frase sola nella prima schermata dice mestiere e clienti ("for the global hospitality and F&B industry"). Da noi: la riga sotto il titolo con tavola, hotel e ristoranti, riparazione.
   - Da non prendere: il caricamento di 22 secondi, 52 MB, il testo a 11 px.
9. **Artisans de Genève** (artisansdegeneve.com), laboratorio di orologeria su misura, Menzione d'onore 13/12/2025.
   - Mossa 1: un serif leggero e chiaro su un fondo scuro ("What We Create Lives Once"). Da noi: il titolo crema in Rowan 300 sul blu.
   - Mossa 2: i collegamenti sottolineati al posto dei bottoni ("Discover our Atelier"). Da noi: nell'apertura solo collegamenti di testo, il bottone pieno arriva nelle sezioni.
   - Da non prendere: l'avviso legale che copre la pagina, 144 MB di video.
10. (in più) **House of Corto** (houseofcorto.com), Site of the Day 3/12/2025: la regola unica della serie (stessa finestra, stessa etichetta). Già usata da Tacchificio: qui vale solo per la fila delle teste.

## 3. Carattere

- **Display: Rowan** (Indian Type Foundry, Fontshare, ITF Free Font License 2.0), peso 300. Un serif di testo e titolo con grazie taglienti e cifre antiche: il 9 e il 5 scendono sotto la riga, come nei numeri incisi. Sottile come un filo d'argento lucidato, ma con le aste nette. Solo tre momenti: il titolo d'apertura (150 px a 1440), "Argento massiccio" nella vetrina (196 px), "999" nelle impugnature (380 px).
- **Testo: Supreme** (ITF, Fontshare, ITF Free Font License 2.0), 400 e 500: un grottesco asciutto e geometrico, per il testo, gli `h2` di servizio, la testata, le etichette dei pezzi, il telefono, il modulo.
- File woff2 ufficiali di Fontshare, ospitati dalla pagina senza modifiche, licenza in `sito-he/fonts/FFL-ITF.txt`.
- Mai corsivo, nessuna etichetta sopra i titoli, nessun numero davanti ai passi; il maiuscolo spaziato solo nel marchio in testata.
- Registro: riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Rowan e Supreme non sono in nessuna home della campagna né nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`. Escono Bodoni Moda e Rethink Sans della versione di oggi.

## 4. Colore (dai loro materiali)

| Nome | Valore | Da dove | Dove |
|---|---|---|---|
| Carta | #F3F2EE | il campo chiaro delle foto di catalogo | fondo della pagina; il bianco delle foto diventa questo |
| Inchiostro | #121416 | | testo, bottoni, piede |
| Blu astuccio | #0E2140 | il blu del loro marchio (#00265a) e dell'"Astuccio 77 pezzi blue" del catalogo | **l'unico campo pieno: l'apertura** |
| Crema | #F1DEBF | il raso dentro l'astuccio; è il negativo esatto del blu | il titolo sul blu (lo fa la fusione "differenza": sul campo chiaro lo stesso testo diventa nero) |
| Argento | #A4A8AE | il metallo lucidato, nei mezzi toni | filetti dei ripiani sul blu, segni secondari |
| Grigio | #5C6066 (6,0:1 sulla carta) | | testi secondari, codici, inglese |

## 5. Movimento

- **Gesto d'apertura, "l'astuccio si apre"** (`data-he-scale` con `data-he-scale-zoom="1"`, finestra di partenza e arrivo scritte nella pagina): la prima schermata è blu pieno, come l'interno di un astuccio, con una finestra chiara a destra dove stanno le posate Inglese in argento massiccio (forchetta, coltello, cucchiaio, cucchiaino) e a sinistra il titolo in crema. Scorrendo la finestra si apre fino alla pagina: il blu se ne va, la luce entra, le posate restano ferme alla loro misura e il titolo, senza muoversi, passa dal crema al nero (fusione "differenza" sul campo). Il titolo sale riga per riga all'apertura (`data-he-split data-he-subito`). Ragione di mestiere: l'argento si conserva nell'astuccio e si tira fuori per la tavola; il catalogo ha l'astuccio blu per il servizio da 77 pezzi.
- **Sostegno 1, la vetrina**: il titolo "Argento massiccio" sale riga per riga (`data-he-split`), secondo e ultimo split.
- **Sostegno 2, il leone**: la testa di leone in argento 999 si scopre dal basso con un taglio netto (`data-he-wipe="su"`), una volta.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con "Chiama".
- Niente parallasse, indice, racconto con foto ferma, prima e dopo, galleria orizzontale, sipario. Gli altri cambi di ritmo li fanno la scala (il titolo a 150 px, le teste a 180 px accanto al 999 a 380 px, i ripiani) e l'impaginazione.
- Con "riduci movimento" (e senza JavaScript) l'apertura resta nella composizione di partenza: blu, titolo crema, posate nella finestra. Pagina completa.
- Fissaggio con `pinType: "transform"` (impostato prima di `he.js`), come in Tacchificio, per non spostare il layout.

## 6. Ritmo (ogni sezione ha uno scheletro diverso)

1. **Apertura, "Tutta la tavola, in argento."** (blu, fissata sopra i 900 px): titolo su tre righe a sinistra, finestra alta a destra con le posate e la loro etichetta, sotto il titolo la riga del mestiere e due collegamenti (riparazione, hotel e ristoranti). Sul telefono: blu con titolo e riga, poi la finestra chiara con le posate sotto, ferma.
2. **Firma, la vetrina "Argento massiccio"** (carta): tre ripiani di filetto. Sul primo il titolo in Rowan, in piedi sul ripiano come un pezzo, con il candelabro a cinque fiamme accanto; sul secondo quattro pezzi di altezze diverse (brocca martellata, coppa champagne, bicchiere, candeliere); sul terzo il servizio Impero, il secchiello e lo shop. Sotto ogni pezzo nome, materiale e codice.
3. **999, le impugnature** (carta): il numero a 380 px a sinistra, la testa di leone alla misura nativa a destra; sotto, la fila delle sei teste nella stessa finestra (cavallo, civetta, cobra, anatra, labrador, teschio) con il nome.
4. **Riparazione** (carta, filetto nero spesso sopra): a sinistra la loro frase grande in Supreme ("La vostra argenteria tornerà al suo originario splendore."), a destra i cinque materiali in righe; sotto, come si fa in tre frasi, "Mandate le foto del pezzo" e il telefono. Nessuna foto: il lavoro non è fotografato.
5. **Hotel e ristoranti**: due pezzi tondi visti dall'alto (sottopiatto e vassoio Inglese) sovrapposti a sinistra, il testo a destra con la rimessa a nuovo, l'argentatura dell'acciaio, Area clienti ed export.
6. **Alfredo Varotto** (fascia stretta): la citazione della pagina Azienda in Supreme a 30 px su otto colonne, la fonte sotto.
7. **Contatti**: il telefono grande da toccare, email, indirizzo con la mappa, fax, "prima di passare, chiamate"; il modulo "Scrivete la richiesta" (prepara l'email, come la versione di oggi); accanto "Writing from abroad" in inglese con export@; lo shop e il suo WhatsApp per le domande sugli articoli.
8. **Piede** (inchiostro): marchio, ragione sociale, indirizzo, P.IVA, note su privacy e cookie, Area clienti, shop, sito inglese di oggi.

La sezione firma è la 2: un'idea (la tavola intera in argento massiccio, pezzo per pezzo) con la prova fotografica (sette pezzi veri del catalogo, ognuno con il suo codice), non il logo ingrandito.

## 7. Foto

Riscaricate il 7/11/2026 dal sito di oggi in `assets/originali/` (fuori da git). La scoperta: ogni miniatura delle pagine di categoria apre `immagine.asp?PathImm=<nome>`, che mostra il file della cartella **`immaginiAltaRisoluzione/`**, fino a 1280 px (una brocca Royal Queen a 1869x2121). Le miniature che si vedevano erano di 100-500 px. Scaricati 1.165 file (93 MB, `assets/originali/alta/`): tutti i pezzi dei marchi Varotto Alfredo (647), Royal Queen (446) e Royal England (72), dalle 312 pagine di categoria in italiano; più le 70 immagini delle pagine principali e della versione inglese (`assets/originali/sito/`, tra cui `assistenza-clienti.jpg` a 932x1097, posate così sbiadite da essere solo uno sfondo). La versione inglese usa gli stessi file.

Trattamento unico (`_prova/he/script/immagini.py`): campo piatto (il fondo dello studio, bianco o grigio sfumato, stimato con un polinomio e portato a bianco), saturazione al 30 % (l'argento resta neutro, l'oro degli interni appena accennato), una curva leggera uguale per tutti, ritaglio sul pezzo; in pagina ogni foto sta in "moltiplica" sulla carta. Nessuna foto oltre la misura nativa: in pagina a 1440 tra 0,4 e 0,6 della misura del file, cioè nitide anche a doppia densità; la testa di leone a 1,0.
