# Paraga Pelli, direzione artistica della home HE

Scritta il 7 novembre 2026 seguendo `_metodo/highend/SISTEMA.md` (punto 3) e le lezioni della sezione 8. Pagina: `sito-he/index.html`. La `sito/` di oggi ("La mazzetta") e le cartelle per WordPress non si toccano. Il committente vuole una home "più high-end, più fashion, più di design"; la lezione dei piloti dice come leggerlo per un fornitore: **mostrare il mestiere con la cura di una maison**, non vestire un ingrosso da casa di moda.

## 1. La cosa vera

Paraga Pelli non concia e non cuce: compra, tiene a magazzino e vende pelle bovina, ecopelle e tessuti a chi fa imbottiti e rivestimenti (01-analisi §1 e schede). Il loro mestiere si vede in due cose, e le due cose sono la pagina:

- **il magazzino di Tombelle**: la corsia con i rotoli sugli scaffali, le pelli intere impilate sui bancali con il bordo vivo, le pelli colorate (la foto `paragapelli-visual-home.jpg`, 1680x400, la più "loro" del sito, 01-analisi §4);
- **la scheda dell'articolo**: un nome (pittori e dogi per la pelle, isole greche per l'ecopelle), uno spessore in millimetri e un **disegno**: "Disegno Dollaro", "Disegno Uruguay", "Disegno madras", "Disegno naturale", "martellata" (schede prodotto, 01-analisi §2). Il disegno è la grana: è il dettaglio che un tappezziere sceglie, ed è la parola che in pagina diventa grande come il nome di una collezione.

L'idea in una riga: **dal magazzino alla grana**. La pagina si apre sulla pila di pelli intere, la apre fino a mostrare tutta la corsia, poi scende alla superficie di cinque articoli con il nome del loro disegno in grande e lo spessore accanto, e chiude con tutti i colori a campione e la richiesta del box-campionario.

Fuori dalla pagina perché "da confermare" (01-analisi §8, LEGGIMI): forma giuridica (in pagina solo "Paraga Pelli" e la P.IVA), civico (solo "Via del Lavoro"), anno 2007, deposito di Altamura, **LWG Gold** (il consenso a mostrarlo è da chiedere), contenuto e spedizione del box-campionario, numero totale di articoli e di colori (27 e 403 non sono scritti: si vedono le righe dei colori, senza totale), unità di misura dello Spessorato (in pagina senza spessore), foto della squadra (consenso delle persone), drappo bianco della home di oggi (licenza forse di repertorio).

## 2. Riferimenti guardati

Aperti con Playwright il 7/11/2026: prima schermata a 1440x900 e a 390x844, tre scorrimenti da 900 px a 1440. Schermate in `_prova/he/riferimenti/<nome>-1440-prima-schermata.jpg`, `-1440-scorrimento-1/2/3.jpg`, `-390-prima-schermata.jpg` (script `_prova/he/script/riferimenti.mjs`, log in `riferimenti/log.txt`). Pellizzari non risponde dal browser di prova (tunnel rifiutato); Sabrina Leather non ha dato schermate; la prima schermata di Foglizzo è un video che il browser di prova non riproduce (resta bianca), gli scorrimenti si vedono.

**Pelle e tessuti per l'arredo**

1. **Foglizzo** (foglizzo.com), pelle per arredo dal 1921.
   - Mossa 1: sotto ogni ambiente il dettaglio della materia, nella stessa griglia (quattro interni sopra, quattro macro di pelle sotto). Da noi: accanto al nome del disegno, la grana vera dell'articolo, alla misura del file.
   - Mossa 2: "Leather Library" come porta d'ingresso al campionario, un titolo e una riga sola. Da noi: "Catalogo" con una riga, poi i colori.
   - Da non prendere: il corsivo calligrafico di "Atelier", il carrello in testata.
2. **Poltrona Frau** (poltronafrau.com).
   - Mossa 1: titolo grande e sottile a sinistra, testo breve a destra ("Metropolitan Living"). Da noi: gli h2 di servizio a sinistra e la riga di testo a destra, nel catalogo e nel disegno.
   - Mossa 2: ogni pezzo con il nome e una seconda riga piccola in grigio (il progettista). Da noi: ogni articolo del catalogo con il nome in Boska e sotto spessore e disegno in grigio.
   - Da non prendere: il carosello con le frecce, i bottoni bianchi sopra la foto.
3. **Dedar** (dedar.com), tessuti, Milano.
   - Mossa 1: un pannello di colore pieno con il testo e un solo oggetto accanto (il campo rosa di "Amuleto" con la sedia). Da noi: la chiusura nel cuoio, con il box-campionario come unico oggetto.
   - Mossa 2: la testata di poche parole (Menu, Search, Login come parole, niente icone). Da noi: voci scritte e il telefono come testo.
   - Da non prendere: lo slideshow d'apertura, il testo bianco sulla foto affollata.
4. **Rubelli** (rubelli.com), tessuti, Venezia.
   - Mossa 1: la materia vicinissima, un pannello mezza pagina accanto a una colonna di testo. Da noi: la grana ferma a sinistra (560x660, misura nativa) e il nome del disegno a destra.
   - Mossa 2: due pannelli di materia con il nome della categoria. Da noi: le quattro famiglie del catalogo (Pelle, Ecopelle, Tessuti, Pelle auto) come titoli delle righe.
   - Da non prendere: le etichette in maiuscolo bianco sulla foto, poco leggibili.
5. **Kvadrat** (kvadrat.dk), tessuti, Danimarca.
   - Mossa 1: i campioni colore posati come oggetto, il colore vero è la foto. Da noi: le righe dei colori a campione, una per articolo, dalle loro scansioni senza ritocco.
   - Mossa 2: molto bianco intorno agli oggetti, un oggetto per volta. Da noi: le foto del servizio "Azienda" alla loro misura, con aria intorno.
   - Da non prendere: la barra dei sotto-marchi, il bottone d'accessibilità flottante.
6. **Moore & Giles** (mooreandgiles.com), pelle e arredo.
   - Mossa 1: il colore della pelle (il senape) solo sul marchio e sui bottoni. Da noi: il cuoio solo nel campo della chiusura, mai altrove.
   - Mossa 2: dopo l'apertura una frase breve di missione centrata ("Since 1933", "a purpose for every hide"). Da noi: la loro frase "Servizio, qualità, prezzo sono imperativi categorici" come titolo del magazzino.
   - Da non prendere: il popup della newsletter, il corsivo d'accento, il riquadro della chat.
7. **Spinneybeck** (spinneybeck.com), pelle per arredo.
   - Mossa 1: "Color Book" come prima voce del menu: il campionario è il prodotto. Da noi: il box-campionario in testata e come unico bottone dell'apertura.
   - Mossa 2: nel piede i recapiti in una riga (numeri ed email). Da noi: il piede in una riga sola sulla carta.
   - Da non prendere: la foto con il bollino del premio, la griglia di notizie.

**Premiati su Awwwards in settori vicini** (premi verificati in `_metodo/professionale/alto/awwwards.md`)

8. **PrimeAsia** (primeasialeather.com), concerie, Site of the Day 21/5/2025.
   - Mossa 1: ogni pelle come oggetto, con il nome in basso a sinistra e tre righe di scheda (grana, nappa, pigmentata). Da noi: il passo del disegno: la parola, lo spessore, una riga con l'articolo e la materia.
   - Mossa 2: il titolo enorme e leggero sopra l'apertura (137 px, peso 300). Da noi: "Pelle, ecopelle, tessuti" in Boska 200 a 226 px.
   - Da non prendere: lo sfondo WebGL, 27 MB.
9. **House of Corto** (houseofcorto.com), sedie e tavoli, Parigi, Site of the Day 3/12/2025.
   - Mossa 1: foto piccole tenute alla loro misura dentro grandi campi (verde scuro, carta). Da noi: le foto del servizio "Azienda" (350 px online) mai ingrandite, e il box-campionario (265 px) su una scheda chiara dentro il campo cuoio.
   - Mossa 2: la didascalia a due voci sotto ogni foto. Da noi: una riga sotto ogni foto che dice che cosa si vede.
   - Da non prendere: il testo a 7 px, il carrello.

## 3. Carattere

- **Display: Boska** (Barbara Bigosinska, Indian Type Foundry, Fontshare, ITF Free Font License 2.0), peso 200 (e 300 per i nomi del catalogo). Un serif ad alto contrasto, stretto, con le grazie sottili: a 226 px ha la tensione di un titolo di moda, e i nomi delle collezioni (Botticelli, Doge, Modigliani) ci stanno come su una copertina. Solo nei momenti forti: "Pelle, ecopelle, tessuti" in apertura (226 px a 1440, 295 a 1920, 74 a 390), i cinque disegni nella firma (181 px a 1440, 74 a 390), "Richiedi il box-campionario" nella chiusura (147 px a 1440, 55 a 390). I nomi degli articoli del catalogo in Boska 300 a 30 px.
- **Testo: Author** (Satya Rajpurohit, Indian Type Foundry, Fontshare, ITF Free Font License 2.0), 300, 400 e 500: un grottesco asciutto con un po' di calore, per testo, `h2` di servizio, testata, didascalie, misure e recapiti. Le misure grandi ("1,3/1,5 mm", il telefono) in Author 300.
- File woff2 ufficiali di Fontshare, ospitati dalla pagina senza modifiche, licenza in `sito-he/fonts/FFL-ITF.txt`. `font-display: block` con precaricamento: con `swap` il cambio di carattere spostava il blocco di testo dell'apertura (CLS 0,032 a 1024).
- Mai corsivo, nessuna etichetta sopra i titoli, nessun numero davanti alle sezioni; maiuscolo spaziato solo per il nome in testata e nel piede.
- Registro: riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Boska e Author non sono in nessuna `*/sito/index.html` né `*/sito-he/index.html` e non sono nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`. Escono Mona Sans e Libre Caslon Display della versione di oggi.

## 4. Colore (dai loro materiali)

| Nome | Valore | Da dove | Dove |
|---|---|---|---|
| Carta | #ECE7DF | le pelli bianche sui bancali | fondo di quasi tutta la pagina |
| Carta chiara | #F7F3EC | il bianco delle foto dopo il trattamento | la scheda del box-campionario, il testo sul cuoio |
| Inchiostro | #1C1714 | testa di moro | testo, bottoni |
| Grigio | #665E56 (5,2:1 sulla carta) | la crosta grigia delle pelli sui carrelli | didascalie, misure secondarie |
| Cuoio | #7A3A23 (testo chiaro 8:1) | il cuoio di Botticelli 2117 | **l'unico campo pieno: la chiusura** con il box-campionario e i recapiti |

Gli unici altri colori sono quelli veri delle scansioni del campionario, nelle righe del catalogo.

## 5. Movimento

- **Gesto d'apertura, "aprire la corsia"** (`data-he-scale` con `data-he-scale-zoom="1"`): la banda della corsia (1680x400, misura nativa a 1920, 1440x343 a 1440) parte socchiusa sulle colonne 4-7, stretta sul bordo vivo della pila di pelli bianche e portata alla misura nativa (scala 1,16 ancorata in basso, così il bordo resta in vista); scorrendo si apre a tutta larghezza e torna a 1, e mostra quello che prima non si vedeva: i rotoli a sinistra, la pila intera, le pelli colorate a destra. A 1920 la scala iniziale è 1,16 della misura nativa, sotto il tetto di 1,25. La fessura è applicata prima del primo disegno (classe `pre-moto`), così non lampeggia la foto intera.
- **Sostegno 1, la firma** (`data-he-story`): la grana ferma a sinistra cambia passo per passo mentre a destra scorrono i cinque disegni. Sul telefono e con "riduci movimento" ogni passo ha la sua grana sotto il testo, niente di fermo.
- **Sostegno 2, due titoli che salgono** (`data-he-split`): l'apertura (subito) e la chiusura.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con "Chiama".
- Niente parallasse, tagli, galleria orizzontale, indice, prima e dopo, nastro, sipario. Gli altri cambi di ritmo li fanno la scala (226 px, 181 px, 147 px, 30 px) e l'impaginazione.
- `ScrollTrigger.defaults({ pinType: "transform" })` prima di `he.js`, come Tacchificio e Varotto: l'apertura fissata non sposta il layout.

## 6. Ritmo (ogni sezione ha uno scheletro diverso)

1. **Apertura, "Pelle, ecopelle, tessuti"** (carta, a tutta altezza): il titolo su due righe a sinistra; a destra della seconda riga che cosa fanno e per chi, la via con la mappa, "Richiedi il box-campionario" e il telefono; in basso la banda della corsia che si apre.
2. **Il magazzino** (carta): a sinistra la loro frase ("Servizio, qualità, prezzo sono imperativi categorici") e quattro foto del servizio "Azienda" alla loro misura con una riga sotto (le mani sulla pelle invecchiata, la taglierina sul rotolo, i rotoli dal container, l'imballo); a destra, più in basso, le pelli intere sui carrelli con il bordo vivo (file 652x704, 536x579 a 1440).
3. **Firma, "Disegno e spessore"** (carta, filetto sopra): la grana ferma a sinistra, a destra i cinque disegni in Boska a 181 px, lo spessore in Author 300, una riga con l'articolo e la riga dei suoi colori a campione. Dollaro (Botticelli), Uruguay (Leonardo), Madras (Sera), Naturale (Doge), Martellata (Monza).
4. **Catalogo** (carta): quattro famiglie, per ogni articolo il nome in Boska 300, spessore e disegno in grigio, e la riga dei suoi colori a campione (le scansioni del sito, un tassello per colore, nell'ordine delle schede).
5. **Chiusura, "Richiedi il box-campionario"** (cuoio, l'unico campo pieno): il titolo in Boska, la scatola sulla sua scheda chiara alla misura del file, il bottone email già intestato; sotto un filetto, i recapiti in poche righe (telefono grande, le quattro email, la via con la mappa, il fax).
6. **Piede** (carta): una riga con nome, P.IVA, via, Privacy, Cookie, Facebook, English; sotto le due note su privacy e cookie della pagina.

La sezione firma è la 3: un'idea (il disegno della pelle è il nome che conta, come una collezione) con la prova fotografica (cinque grane vere dalle copertine dei loro cataloghi, alla misura del file, accanto allo spessore della scheda).

## 7. Foto

Riscaricate il 7/11/2026 da paragapelli.com (sito in http, copia HTTrack) in `assets/originali/` (fuori da git): tutto il sito italiano e inglese con le immagini collegate, più gli sfondi caricati dallo script (`public/foto/sfondi/1/bg-home.jpg` 1680x1050, `sfondi/2/bg_chisiamo.jpg` 1620x800, in realtà PNG), le 25 copertine dei cataloghi (985x1500), le 403 scansioni (350x350), le 13 foto del servizio "Azienda" (le pagine zoom a 350 px). Cercati e non trovati: gli originali del servizio "Azienda" (`immagini/azienda/N.jpg` risponde 404, le cartelle 403), le scansioni senza la pagina zoom (404), PDF di cataloghi o campionari (nessuno), file diversi nella versione inglese (stesse immagini). La Wayback Machine non è raggiungibile dal proxy. Nessuna foto di repertorio in pagina.

Trattamento unico (`_prova/he/script/immagini.py`) per tutte le fotografie, grane comprese: neri all'inchiostro, bianchi alla carta chiara, saturazione 0,92. Le scansioni del campionario non si toccano: sono il colore, non una fotografia. Nessuna foto ingrandita oltre la misura nativa.
