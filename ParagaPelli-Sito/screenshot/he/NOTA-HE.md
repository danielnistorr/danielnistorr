# Paraga Pelli, home HE (7 novembre 2026, giro di ritocco dopo il 7,1)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (18 file, più 8 strisce delle famiglie in `img/famiglie/` e 5 cartelle colori in `img/cartelle/`). Cartella `sito-he` circa 1,7 MB. La `sito/` di oggi, le cartelle per WordPress e il kit master in `_metodo/` non sono toccati. Direzione artistica in `DIREZIONE-HE.md` (aggiornata nei punti 3, 5, 6 e 7).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8789`, server fermato), `foglio-1440.jpg` (18 fotogrammi) e `foglio-390.jpg` (20), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` e `-390-*.jpg` (a piena misura, estratti dal video con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il titolo è salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare (dalla cartella `ParagaPelli-Sito`): immagini con `python3 -I _prova/he/script/immagini.py` (legge `assets/originali/`, fuori da git, e le scansioni di `sito/img/c/`); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (uscita di questo giro in `_prova/he/prove-ritocco.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`.

## Il giro di ritocco (giudizio 7,1: "sopra la piega regge, sotto è un listino da ingrosso")

1. **Catalogo**: da 27 righe (2,5 schermate a 1440, 4 a 390) a una riga per famiglia: nome in Boska 300 a 64 px (colonne 1-4), i nomi degli articoli in una riga Author 17 px (colonne 5-12), sotto una striscia di 22 tasselli alti 40 px (sul telefono due righe da 11). I tasselli sono gruppi di colori vicini della famiglia (il campione vero più vicino al centro di ogni gruppo), in fila come una mazzetta: neutri chiari, colori per tinta, neutri scuri. L'elenco completo non è in pagina, nemmeno chiuso, finché non è confermato che il catalogo è attuale: al suo posto "Chiedete il campionario" porta ai contatti. L'h2 sta da solo, tolta la frase "Ogni articolo...". Ora 1,2 schermate a 1440 e 1,6 a 390, margini compresi.
2. **Apertura**: `data-he-scale-zoom="1"`, fessura sulle pelli colorate `inset(0% 4.2% 0% 74%)` (dalla colonna 10 al margine destro, sotto il blocco di testo): il gesto si apre verso sinistra e scopre la pila bianca e i rotoli. Luci abbassate nello script per tutte le foto (spalla morbida: fino a 160 invariato, il bianco pieno scende a 232 prima della mappatura): i bianchi della corsia non bruciano più e restano appena sotto la carta. `corsia-t-540.webp` rifatto dalla zona x 1140-1680: sul telefono si vedono subito le pelli colorate, nitide (540 px mostrati a 350). La didascalia "In magazzino..." sta sotto la banda, fuori dalla sezione fissata. Sugli schermi larghi e bassi (1280x720) il blocco di destra si stringe di 20 px, così resta aria sopra la fessura.
3. **Firma**: le grane sono in un tono solo (scala di grigi distesa, stessa luce media, mappata tra inchiostro e carta chiara); il colore sta nei tasselli. `.disegno .he-passo{min-height:560px}` (prima 700 px, con 360 px vuoti sotto ogni passo). La riga nome + misura + striscia del catalogo qui non c'è più: sotto lo spessore c'è la cartella dei colori dell'articolo (6 tasselli da 44 px per riga, nell'ordine della scheda) con accanto l'articolo sotto un filetto.
4. **Magazzino**: tolte container e imballo, mani e taglierina in una riga; le pelli intere con `pelli-460` a 460 px (misura del file), con il fondo allineato a quello delle due foto. `.ds-testa` e `.ct-testa` non hanno più lo stesso schema: il catalogo ha l'h2 da solo.
5. **Testi e telefono**: tolti i raccordi "Sera, e l'articolo che porta...", "accanto alla liscia Imola", "l'unico articolo con questo disegno"; ogni scheda usa le parole delle schede prodotto (Monza: "pelle bovina martellata, impiegata nei rivestimenti auto"; Madras: "Sera e Madras, l'articolo che porta il nome del disegno", perché sia SERA sia MADRAS sono "Disegno madras"). "ecopelle" corretto in "ecopelli" in `.ds-testa p`. A 390 nascosto il numero ripetuto sotto il bottone (resta "Chiama" fisso in testata), h1 a `min(25vw,104px)` (97 px a 390).

File tolti da `sito-he/img/` perché non più usati: le 27 righe `img/righe/`, `az-container-350`, `az-imballo-350`, `pelli-652`.

## L'idea

Dal magazzino alla grana. Si apre sul loro mestiere di ingrosso (la corsia di Tombelle, che parte socchiusa sulle pelli colorate e si apre scorrendo fino a mostrare pile bianche e rotoli) e scende al dettaglio che un tappezziere sceglie: il disegno della pelle, scritto grande come il nome di una collezione, con la grana vera accanto, lo spessore in millimetri e la cartella dei colori. Poi le quattro famiglie in quattro righe, e la richiesta del box-campionario.

## Sezioni (scheletri diversi)

1. **Apertura** (carta, a tutta altezza): "Pelle, ecopelle, tessuti" in Boska 200 a 226 px su due righe; a destra della seconda riga che cosa fanno e per chi, la via con la mappa, "Richiedi il box-campionario" e il telefono; sotto, la banda della corsia (1440x343) che parte stretta sulle pelli colorate e si apre; la didascalia sotto la banda.
2. **Il magazzino** (carta): h2 e testo a sinistra, due foto in una riga sotto; a destra le pelli intere, alte quanto il blocco.
3. **Firma, "Disegno e spessore"** (carta): h2 a sinistra e testo a destra; la grana ferma a sinistra (560x660), a destra cinque disegni in Boska a 181 px, lo spessore, la cartella dei colori e l'articolo. `data-he-story`. Sul telefono e con "riduci movimento" ogni disegno ha la sua grana accanto o sotto.
4. **Catalogo** (carta): h2 da solo, quattro righe (famiglia, articoli, striscia), "Chiedete il campionario".
5. **Chiusura, "Richiedi il box-campionario"** (cuoio #7A3A23, l'unico campo pieno): titolo in Boska a 147 px, la scatola sulla sua scheda (#E3DFD9, il bianco della foto dopo il trattamento), il bottone email già intestato; sotto un filetto i recapiti.
6. **Piede** (carta): una riga con nome, P.IVA, via, Privacy, Cookie, Facebook, English; sotto le due note su privacy e cookie.

## Caratteri

Boska 200 e 300 (display: apertura, disegni, famiglie del catalogo, chiusura) e Author 300, 400, 500 (testo, `h2` di servizio, misure, recapiti), Indian Type Foundry, Fontshare, ITF Free Font License 2.0. Nessuno dei due è in un'altra home; riga nel `REGISTRO-CARATTERI.md`. `font-display: block` con precaricamento.

## Foto

Nessun originale più grande di quelli noti (vedi il giro precedente: servizio "Azienda" solo a 350 px, scansioni a 350x350, nessun PDF). Nessuna foto di repertorio, nessuna immagine generata.

| In pagina | Originale | Misura nativa | Mostrata |
|---|---|---|---|
| Corsia, apertura | `immagini/paragapelli-visual-home.jpg` | 1680x400 | 1440x343 a 1440 (0,86, anche nella fessura); 1680x400 a 1920 |
| Corsia, telefono | ritaglio x 1140-1680 della stessa (pelli colorate) | 540x400 | 350x259 a 390, 540x400 a 768 |
| Pelli intere sui carrelli | `public/foto/sfondi/2/bg_chisiamo.jpg`, ritaglio senza persone (652x704) ridotto | 460x497 | 460x497 (1,0) |
| Mani, taglierina | pagine zoom di `immagini/azienda/4, 2.jpg` | 350x263 | 350x263 (1,0) |
| Cinque grane, in grigio | copertine `art.-BOTTICELLI, LEONARDO, SERA, DOGE, MONZA-cover.jpg` | 560x660 | 536x660 (1,0) |
| Box-campionario | `immagini/campionario.jpg` | 265x313 | 265x313 (1,0) |
| Cartelle della firma | scansioni 350x350 (ritaglio centrale 200 px) | tasselli 88 px | 44 px |
| Strisce del catalogo | le stesse scansioni | tasselli 80 px (64 sul telefono) | 40 px a 1440, 32 a 390 |

Trattamento unico per le fotografie: luci abbassate con la spalla, neri all'inchiostro, bianchi verso la carta chiara, saturazione 0,92; le grane in scala di grigi con la stessa mappatura. Le scansioni del campionario non sono toccate. Misurato da `prove.mjs`: rapporto massimo 1,0 tra misura mostrata e file; le grane non attive del racconto risultano 1,06 perché il kit le tiene a `scale(1.06)` mentre sono invisibili.

## Misure e prove (sezione 6)

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", nessuno scorrimento orizzontale, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-ritocco.json`). Viste di lavoro anche a 1280x720 e 1024x768. Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (2.572 caratteri a 1440, 2.503 a 390), nessun elemento nascosto; la corsia è intera, la firma diventa cinque righe grana e testo.
- **Peso al primo caricamento**: 936 KB a 1440 e 644 KB a 390 (soglie 2,5 e 1,5 MB); 609 a 768, 933 a 1024, 936 a 1920. Le grane in grigio pesavano di più (contrasto disteso): portate a qualità 80, guardate al 100%, restano nitide.
- **Layout stabile**: CLS 0 a tutte le larghezze nelle prove a salti; con la rotella 0 a 1440, 1920, 1280x720, 1024 e 390.
- **Controllo d'uso dal telefono**: nella prima vista che cosa vendono e per chi, la via con la mappa, "Richiedi il box-campionario", le pelli colorate; "Chiama 049 983 2030" fisso in testata.
- U+2014: nessuno, nella pagina, nella direzione, nello script e in questa nota.

## Quattro fotogrammi guardati da estraneo (a piena misura)

- **1440, 2,0 s, apertura**: il titolo regge da solo; la fessura sulle pelli colorate, alla misura del file, è un dettaglio nitido e colorato, non più bianco su carta. Resta un vuoto in basso a sinistra finché non si scorre: è l'inizio del gesto, si apre al primo movimento della rotella.
- **1440, 6,5 s, magazzino**: due foto e le pelli intere, nessun provino. Corretto qui: il fondo delle pelli era 30 px più basso di quello delle due foto (sembrava un caso), ora sono allineati.
- **1440, 12,5 s, fine della firma e catalogo**: la cartella di Monza accanto alla grana grigia non somiglia più alle righe del catalogo; le quattro famiglie stanno in una schermata. Corretto qui: le strisce a 21 tasselli ordinate solo per chiarezza alternavano colori a caso (lilla accanto al giallo); ora sono in fila per tinta.
- **390, 2,0 s, prima vista**: titolo a 97 px su tre righe, testo, bottone e il ritaglio delle pelli colorate entrano nella prima schermata; il numero non è più ripetuto sotto il bottone. Corretto qui: le strisce del catalogo a 390 scendevano a tasselli di 16 px (un codice a barre); ora due righe da 11, tasselli di 32 px.
- Nel video della registrazione alcune zone della carta diventano grigie: è la compressione del registratore (lo stesso difetto è nei video di Tacchificio, Varotto e Ruffatti). La pagina è uniforme (vedi le prime schermate ferme).

## Problemi aperti

- **Catalogo attuale**: in pagina solo i nomi degli articoli e una striscia di colori per famiglia. Quando l'azienda conferma che le schede (copia del febbraio 2025) sono attuali, l'elenco completo può tornare in una pagina a parte, non in home.
- **LWG Gold** fuori dalla pagina finché non danno il consenso: è il fatto più forte che manca (codice PAR103, audit fino al 2 febbraio 2027). Pronto da aggiungere come riga nella chiusura.
- **Da confermare** e quindi non in pagina: forma giuridica, civico (37 o 31), anno, deposito di Altamura, contenuto e spedizione del box-campionario, totali del catalogo (27 articoli e 403 colori), spessore dello Spessorato.
- **Grane dalle copertine**: sono la superficie dell'articolo dentro le copertine dei loro cataloghi, ora in grigio; non danno un colore del campionario, e in pagina non lo dicono.
- **Privacy e cookie**: note vere sulla pagina (non raccoglie dati, nessun cookie); per il sito servono le pagine legali dell'azienda. "English" porta alla versione inglese di oggi. Orari: non sono nelle fonti.

## Foto da rifare (in ordine di valore)

1. **La corsia del magazzino a piena risoluzione** (oggi 1680x400): orizzontale da 6000 px dal centro della corsia, ottica 35 mm, luce del capannone, più una verticale sulle pelli colorate per il telefono. Con una foto alta 1500 px la banda dell'apertura diventa una pagina intera e il gesto può allargarsi a tutto schermo.
2. **Le grane dei disegni in studio**: Dollaro, Uruguay, Madras, Naturale, Martellata, ognuno in un colore vero del campionario con il suo codice, luce radente a 15-20 gradi, 4000 px, stesso set per tutti. Sostituiscono i ritagli delle copertine nella firma.
3. **Gli originali del servizio fotografico "Azienda"** (oggi 350 px): mani sulla pelle invecchiata, taglierina sul rotolo, pelli sui cavalletti. Il magazzino può tornare a più foto, grandi.
4. **Il bordo vivo in macro**: la pila di pelli intere sul bancale, luce radente da un lato, 6000 px.
5. **Il box-campionario come oggetto**: aperto, con le cartelle a ventaglio, di tre quarti su fondo carta, 3000 px.
6. **Le scansioni dei colori a 1200 px o più** (oggi 350): stessa luce, profilo sRGB; cartelle e strisce reggono gli schermi densi.
7. **Un imbottito finito di un cliente** in pelle o ecopelle Paraga, con il nome dell'articolo e del colore, se un cliente dà il permesso.
8. **La squadra in magazzino**, se le persone acconsentono.

## Voto

Stima personale 8,0 (design 8, creatività 7,5, usabilità 8,5, contenuto 8); con lo scarto medio di 0,7 tra costruttore e giudice, realisticamente 7,4-7,8. Chiusi i punti sotto la piega che il giudice aveva elencato (catalogo, firma, magazzino, raccordi); la distanza dal 9 dipende per più di metà dalle foto (corsia in striscia, servizio "Azienda" a 350 px, grane prese dalle copertine).
