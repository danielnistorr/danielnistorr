# Paraga Pelli, home HE (7 novembre 2026, prima stesura)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (21 file più le 27 righe dei colori in `img/righe/`). Cartella `sito-he` circa 1,8 MB. La `sito/` di oggi, le cartelle per WordPress e il kit master in `_metodo/` non sono toccati. Direzione artistica in `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8786`, server fermato), `foglio-1440.jpg` e `foglio-390.jpg` (22 fotogrammi ciascuno), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` e `-390-*.jpg` (a piena misura, estratti dal video con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il titolo è salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare (dalla cartella `ParagaPelli-Sito`): immagini con `python3 -I _prova/he/script/immagini.py` (legge `assets/originali/`, fuori da git, e le scansioni di `sito/img/c/`); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; riferimenti con `_prova/he/script/riferimenti.mjs`.

## L'idea

Dal magazzino alla grana. Si apre sul loro mestiere di ingrosso (la corsia di Tombelle, che parte socchiusa sul bordo vivo di una pila di pelli bianche e si apre scorrendo fino a mostrare rotoli, pile e pelli colorate) e scende al dettaglio che un tappezziere sceglie: il disegno della pelle, scritto grande come il nome di una collezione, con la grana vera accanto e lo spessore in millimetri. Chiude con tutti i colori a campione, articolo per articolo, e con la richiesta del box-campionario.

## Sezioni (scheletri diversi)

1. **Apertura** (carta, a tutta altezza): "Pelle, ecopelle, tessuti" in Boska 200 a 226 px su due righe; a destra della seconda riga che cosa fanno e per chi, la via con la mappa, "Richiedi il box-campionario" e il telefono; sotto, la banda della corsia (1440x343) che parte stretta sulle colonne 4-7 e si apre. Gesto: `data-he-scale`, scala 1,16 ancorata in basso fino a 1.
2. **Il magazzino** (carta): la loro frase "Servizio, qualità, prezzo sono imperativi categorici" e la riga di Chi siamo; quattro foto del servizio "Azienda" alla loro misura (350x263) con una riga sotto; a destra, sfalsate, le pelli intere sui carrelli con il bordo vivo.
3. **Firma, "Disegno e spessore"** (carta): la grana ferma a sinistra (536x660 dal file 560x660), a destra cinque disegni in Boska a 181 px: Dollaro (Botticelli, 1,3/1,5 mm), Uruguay (Leonardo, 1,0/1,1 mm), Madras (Sera, 1/1,1 mm), Naturale (Doge, 1,0 mm), Martellata (Monza, 1/1,1 mm); sotto ogni disegno la riga dei colori a campione di quell'articolo. `data-he-story`. Sul telefono e con "riduci movimento" ogni disegno ha la sua grana accanto o sotto.
4. **Catalogo** (carta): Pelle, Ecopelle, Tessuti, Pelle auto; per ogni articolo il nome in Boska 300, spessore e disegno (o materia e uso) in grigio, la riga dei suoi colori dalle scansioni del sito, un tassello per colore, nell'ordine delle schede. Nessun totale scritto.
5. **Chiusura, "Richiedi il box-campionario"** (cuoio #7A3A23, l'unico campo pieno): titolo in Boska a 147 px, la scatola sulla sua scheda chiara (265x313, misura del file), il bottone email già intestato; sotto un filetto i recapiti in poche righe: telefono grande, quattro email, via con la mappa, fax.
6. **Piede** (carta): una riga con nome, P.IVA, via, Privacy, Cookie, Facebook, English; sotto le due note su privacy e cookie.

## Caratteri

Boska 200 e 300 (display: apertura, disegni, chiusura, nomi del catalogo) e Author 300, 400, 500 (testo, `h2` di servizio, misure, recapiti), Indian Type Foundry, Fontshare, ITF Free Font License 2.0. Nessuno dei due è in un'altra home; riga nel `REGISTRO-CARATTERI.md`. `font-display: block` con precaricamento: con `swap` il blocco di testo dell'apertura si spostava (CLS 0,032 a 1024).

## Foto

Riscaricato il sito il 7/11/2026 (italiano e inglese, con le immagini collegate e gli sfondi caricati dallo script) in `assets/originali/`. Nessun originale più grande di quelli noti: il servizio "Azienda" esiste online solo nelle pagine zoom a 350 px (`immagini/azienda/N.jpg` risponde 404), le scansioni a 350x350, nessun PDF di catalogo o campionario, la versione inglese usa le stesse immagini. Novità rispetto alla versione di oggi: le **copertine dei cataloghi** (985x1500) hanno dentro la sagoma della pelle la superficie vera dell'articolo a una risoluzione più alta delle scansioni; ne ho preso il riquadro pulito (560x660) per le cinque grane. Nessuna foto di repertorio, nessuna immagine generata.

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| Corsia, apertura | `immagini/paragapelli-visual-home.jpg` | 1680x400 | 1440x343 (0,86; parte a 1,0 nella fessura); 1680x400 a 1920 |
| Corsia, telefono | ritaglio 540x400 della stessa | 540x400 | 350x259 a 390 |
| Pelli intere sui carrelli | `public/foto/sfondi/2/bg_chisiamo.jpg` (sfondo di Chi siamo), ritaglio senza persone | 652x704 | 536x579 (0,82) |
| Mani, taglierina, container, imballo | pagine zoom di `immagini/azienda/4, 2, 5, 8.jpg` | 350x263 | 350x263 (1,0) |
| Cinque grane | `public/foto/pelle/linee/art.-BOTTICELLI, LEONARDO, SERA, DOGE-cover.jpg`, `auto/monza/art.-MONZA-cover.jpg` | 560x660 | 536x660 (1,0) |
| Box-campionario | `immagini/campionario.jpg` | 265x313 | 265x313 (1,0) |
| Righe dei colori | 403 scansioni 350x350 (ritaglio centrale 200 px) | tasselli 80 px | 24 px (30 a 1920) |

Trattamento unico per le fotografie (grane comprese): neri all'inchiostro, bianchi alla carta chiara, saturazione 0,92. Le scansioni del campionario non sono toccate. Misurato da `prove.mjs`: rapporto massimo 1,0 tra misura mostrata e file a 1440, 1,16 a 1920 solo all'inizio del gesto; le grane non attive del racconto risultano 1,06 perché il kit le tiene a `scale(1.06)` mentre sono invisibili.

## Misure e prove (sezione 6)

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", nessuno scorrimento orizzontale, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Anche a 360 e 1280x720. Le due registrazioni non hanno errori. Corretto durante le prove: a 390 con il movimento la foto d'apertura ingrandita usciva di 12 px (ora la cornice taglia).
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (3.290 caratteri a 1440, 3.234 a 390), nessun elemento nascosto; la corsia è intera, la firma diventa cinque righe grana e testo.
- **Peso al primo caricamento**: 921 KB a 1440 e 572 KB a 390 (soglie 2,5 e 1,5 MB); 620 a 768, 930 a 1024, 921 a 1920. La corsia è precaricata con `imagesrcset`.
- **Layout stabile**: CLS 0 a tutte le larghezze nelle prove a salti; con la rotella 0 a 1440, 1920, 1024 e 390, anche con l'apertura fissata (`pinType: "transform"`).
- **Controllo d'uso dal telefono**: nella prima vista che cosa vendono e per chi, la via con la mappa, "Richiedi il box-campionario", il numero; "Chiama 049 983 2030" fisso in testata.
- U+2014: nessuno, nella pagina, nella direzione, nello script e in questa nota.

## Cinque fotogrammi guardati da estraneo

- **3,0 s, apertura**: il titolo regge la pagina da solo, la fessura sulla pila di pelli è un dettaglio vero e nitido. Corretto prima: il testo a destra copriva la prima riga del titolo a 1024x768 e 1280x720 (ora parte sotto la prima riga), la didascalia si scontrava con il testo (ora a sinistra, sopra la banda), la fessura era fuori griglia (ora colonne 4-7) e partiva senza il bordo vivo (ora la scala è ancorata in basso).
- **4,8 s, corsia aperta**: il gesto scopre davvero qualcosa, i rotoli e le pelli colorate. Bene.
- **7,2 s, magazzino**: le foto del servizio "Azienda" sono alla loro misura e si leggono come un provino; restano piccole e morbide (sono 350 px). Corretti prima: il vuoto di mezza pagina sopra le pelli e tra magazzino e firma (spazi ridotti), le foto a 313 px (ora 350, la misura del file).
- **10,0 e 13,0 s, firma**: "Martellata" accanto alla grana di Monza è la schermata più "moda" della pagina; la riga dei colori sotto ogni disegno lega la grana al campionario e riempie il vuoto sotto il testo. Con "riduci movimento" la grana finiva sopra il testo nella colonna di destra (regola CSS più debole): ora sta a sinistra. Corretto prima: "pelle bovina" ripetuto in tutte e cinque le didascalie (ora una volta), la frase "le pelli hanno nomi di pittori" era troppo larga (ora con i nomi: Botticelli, Leonardo, Modigliani, Doge).
- **19,4 s, chiusura**: un campo pieno, un titolo, un oggetto, i recapiti in poche righe. Corretti prima: "box-campionario" che andava a capo sul trattino e poi finiva sotto la scheda della scatola; la chiusura generica con titolo "Contatti", legenda e piede scuro (ora recapiti dentro il campo e piede in una riga sulla carta); il telefono ripetuto due volte di fila.
- Nel video della registrazione alcune zone della carta diventano grigie (231,231,231): è la compressione del registratore, lo stesso difetto è nei video di Tacchificio, Varotto e Ruffatti. La pagina è uniforme (vedi le prime schermate ferme).

## Problemi aperti

- **LWG Gold** fuori dalla pagina finché non danno il consenso: è il fatto più forte che manca (codice PAR103, audit fino al 2 febbraio 2027). Pronto da aggiungere come riga nella chiusura.
- **Da confermare** e quindi non in pagina: forma giuridica, civico (37 o 31), anno, deposito di Altamura, contenuto e spedizione del box-campionario, totali del catalogo (27 articoli e 403 colori), spessore dello Spessorato. Il catalogo mostra quello che c'è oggi sulle schede del sito (copia del febbraio 2025): va chiesto se è attuale.
- **Grane dalle copertine**: sono la superficie dell'articolo dentro le copertine dei loro cataloghi; il colore della copertina può non coincidere con un colore del campionario (Botticelli in copertina è grigio). Didascalia e testo alternativo non danno un codice colore per questo.
- **Privacy e cookie**: note vere sulla pagina (non raccoglie dati, nessun cookie); per il sito servono le pagine legali dell'azienda. "English" porta alla versione inglese di oggi.
- **Orari**: non sono nelle fonti, non sono in pagina.

## Foto da rifare (in ordine di valore)

1. **La corsia del magazzino a piena risoluzione** (oggi 1680x400): orizzontale da 6000 px dal centro della corsia, ottica 35 mm, luce del capannone, più una verticale per il telefono. Con una foto alta 1500 px la banda dell'apertura diventa una pagina intera e il gesto può allargarsi a tutto schermo.
2. **Il bordo vivo in macro**: la pila di pelli intere sul bancale, luce radente da un lato, 6000 px. Sostituisce il dettaglio da cui parte il gesto.
3. **Le grane dei disegni in studio**: Dollaro, Uruguay, Madras, Naturale, Martellata, Liscio, Nabuk, ognuno in un colore vero del campionario con il suo codice, luce radente a 15-20 gradi, 4000 px, stesso set per tutti. Sostituiscono i ritagli delle copertine nella firma.
4. **Gli originali del servizio fotografico "Azienda"** (oggi 350 px): mani sulla pelle invecchiata, taglierina sul rotolo, container, imballo, pelli sui cavalletti. Le quattro foto del magazzino diventano grandi senza cambiare la pagina.
5. **Il box-campionario come oggetto**: aperto, con le cartelle a ventaglio, di tre quarti su fondo carta, 3000 px.
6. **Le scansioni dei colori a 1200 px o più** (oggi 350): stessa luce, profilo sRGB; le righe del catalogo reggono gli schermi densi e un tassello può aprirsi in grande.
7. **Un imbottito finito di un cliente** in pelle o ecopelle Paraga, con il nome dell'articolo e del colore, se un cliente dà il permesso: è l'uso, che oggi la pagina dice solo a parole.
8. **La squadra in magazzino**, se le persone acconsentono (oggi lo sfondo di Chi siamo è fuori dalla home per questo).

## Voto

Stima personale 8,0 (design 8, creatività 8, usabilità 8,5, contenuto 7,5), da leggere con lo scarto medio di 0,7 che il SISTEMA registra tra costruttore e giudice: realisticamente 7,3-7,6. La distanza dal 9 dipende per più di metà dalle foto (corsia in striscia, servizio "Azienda" a 350 px, grane prese dalle copertine).
