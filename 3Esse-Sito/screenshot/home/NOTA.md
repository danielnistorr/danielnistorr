# Tre Esse, home finale "La tavola"

Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, carattere in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, pagina, controlli, screenshot). Pagina alta 4680 px a 1440 e 5188 px a 390.

## L'idea

Il prodotto di Tre Esse è il disegno che fa stare in piedi un arco d'acciaio. La prima schermata è una tavola tecnica vera: carta chiara, l'assonometria dell'arco del cavalcaferrovia Sarpi al vivo sul bordo destro e su quello inferiore, e in basso a destra il cartiglio, il riquadro dei dati che chiude ogni tavola di progetto (opera, luogo, anno, lavoro). Dentro il cartiglio c'è l'unico gesto della pagina: Disegno / Opera. Un tocco e nello stesso spazio compare il ponte finito. "Dal disegno all'opera" non è più una sezione: è l'interruttore.

Rispetto al prototipo A la prima schermata è ripensata, non ritoccata: il disegno passa da oggetto accanto al titolo a tavola al vivo (59 % della larghezza a 1440), la didascalia "Tav." in basso a sinistra sparisce dentro il cartiglio, i richiami scendono da 3 a 2, la foto calda sta a un tocco e non due schermate più giù. Il cartiglio è il segno del mestiere che Mario Agnoletto e Hambro non hanno: con il nome di un concorrente la pagina non regge, perché la tavola e i dati sono di Tre Esse.

## Le prime due schermate

1. Apertura (1440x900): "Ingegneria strutturale" in Overpass 300 a 132 px, una frase su cosa fanno e per chi, il bottone verde "Scriveteci il progetto" e l'email. A destra la tavola del Sarpi, con i richiami 1 Arco e 2 Imposta; in basso a destra il cartiglio (filetti da 1 px #8A9096, righe in Overpass 600 a 12 px con cifre tabellari) con l'interruttore alto 44 px. In stato Opera la foto del Sarpi all'ora blu compare a destra, allineata al titolo e al vivo sul bordo destro, alla sua misura nativa; il cartiglio resta dov'è. Una riga sottile chiude il foglio.
   - A 390: titolo, tavola a tutta larghezza (al vivo a destra e in basso), subito sotto il cartiglio con l'interruttore: tutto entro 806 px dei 844. Frase e bottone vengono dopo.
2. "Dal Brennero a Riyad": la cupola di Adria da sotto in quadrato su 7 colonne (755 px, file da 865: mai oltre la misura nativa), accanto la didascalia con 90 m e 700 t in grande; sotto, dieci opere in tabella (anno, opera, luogo, acciaio o volume) con cifre tabellari e filetti, e il link al portfolio completo in PDF.

Poi: "Un solo interlocutore, dal calcolo al cantiere" (i quattro servizi in 2x2, senza icone né riquadri, e due righe grigie su software e strumenti), contatti con il telefono a 96 px su fondo carta e tre colonne (Ufficio, Posta, PEC e fax), piede scuro con i dati societari, l'unico cambio di fondo.

## Caratteri e colori

- Overpass, una famiglia sola: 300 per titoli, telefono e misure grandi, 400 testo, 600 voci, cartiglio e righe della tabella; cifre tabellari (`font-variant-numeric: tabular-nums`) per anni, tonnellate, metri cubi e telefoni. Disegno di Delve Withrington (Delve Fonts) per Red Hat, licenza SIL Open Font License 1.1 (testo in `sito/fonts/OFL.txt`), file woff2 presi da Google Fonts e serviti dalla pagina.
- Perché: Overpass ridisegna la Highway Gothic della segnaletica stradale e il suo nome vuol dire cavalcavia: è la lettera delle infrastrutture che Tre Esse calcola. Il registro viene dagli studi di ingegneria: schlaich bergermann partner (titolo grande e sottile su bianco) e Dissing+Weitling (bianco pieno, un solo colore). Niente monospazio, niente corsivi.
- Colori: carta #F4F3EF, inchiostro #16191C, grigio testo #5E646A, grigio quota #8A9096 (filetti del cartiglio e delle righe), verde #2E7D4F preso dal "3" del marchio, solo per marchio, bottone e sottolineature dei link.

## Ispirazioni del committente (Pelletteria Graziella, Studio N19)

Usate al minimo, di proposito. Il soggetto è tecnico e lavora per le imprese: un ufficio di calcolo e disegni costruttivi di ponti in acciaio non è un marchio di moda o di lusso, quindi il registro viene dagli studi di ingegneria (sbp, Dissing+Weitling) e non dalla moda. Da N19 resta solo il grottesco grande su fondo chiaro con l'aria intorno; da Graziella niente (fondo nero, corsivi, foto di prodotto di lusso sono il registro sbagliato per chi disegna ponti).

## Interazione

Un solo gesto: l'interruttore Disegno / Opera nel cartiglio. Clic, tocco, oppure frecce sinistra e destra quando il fuoco è sui bottoni; `aria-pressed` sui due bottoni, anello di fuoco verde, 44 px di altezza. Il cambio è netto, senza dissolvenza; l'unica transizione (0,12 s) è sul colore dei bottoni. La foto dell'opera si carica dopo la pagina, così il cambio è immediato. Nessuna animazione allo scorrere, niente effetti sul cursore, nessun hover che sbiadisce.

## Foto e disegni

Tutto materiale di Tre Esse, nessuna foto di repertorio (le foto Unsplash di `assets/esterne/` non sono usate).
- `sarpi-tavola-*` (WebP, 640-1800 px): assonometria dell'arco del Sarpi. Fonte: le due strisce raster della pagina 28 di `Company-Project-Portfolio.pdf` (1027x537 ciascuna, 220 ppi), estratte senza ricompressione con `pdfimages` in `assets/originali/pdf-estratti/`. Tolti i due dettagli staccati (nodo in alto a sinistra, attacco dei pendini in basso a destra) per lasciare l'arco solo. Il tratto è ricostruito, non solo ingrandito: x2 bicubico, sfocatura di 0,7 px, curva a soglia morbida, inchiostro e carta cotti nel file. A 1:1 non ci sono gradini; a 1440 il disegno si vede a 0,93 della misura nativa.
- `sarpi-opera-*` (JPEG, 480-923 px): il Sarpi finito all'ora blu, stessa pagina del PDF (931x529), tolto il filo grigio del bordo. Mai servita oltre 923 px.
- `adria-cupola-*` (JPEG, 480-865 px): ritaglio dal portfolio (1155x865), quadrato centrato sull'oculo, schiarito appena (gamma 0,86), non ingrandito.
- Diritti: sono dell'azienda o dei fotografi delle imprese; l'uso va confermato (LEGGIMI).

## Controlli

- Larghezze guardate a pezzi: 320, 390, 768, 1024, 1366x768, 1440, 1536x864, 1920. Nessuno scorrimento orizzontale, nessuna sovrapposizione: il cartiglio non copre il disegno a nessuna misura (sotto i 900 px di altezza la tavola scorre a sinistra in proporzione).
- Tastiera: le frecce cambiano vista e spostano il fuoco; provato a 1440 e a 390 col tocco.
- U+2014: nessuno in pagina, nella NOTA, nel LEGGIMI e negli script.
- `segnali.sh` a 1440: 15 soglie su 18 a posto. Restano tre voci, tutte volute:
  - area immagini 20,7 % (soglia 35 %): il giudice ha chiesto di togliere la sezione del prospetto, doppione dell'apertura, e di non usare foto altrui. Le altre foto di Tre Esse sono sotto i 500 px o con la filigrana. L'apertura è per metà disegno. Con le foto nuove del Sarpi e del Ponte Verde si può aggiungere una fascia.
  - una tabella di 10 righe in home (soglia 4): chiesta dal giudice al posto della prosa. Qui il dato è il prodotto: anno, opera, luogo, tonnellate.
  - una sola misura di H2 (da guardare): l'unico elemento grande è il titolo d'apertura, come nei riferimenti.
- Divieti del committente: nessuno (niente gradienti, emoji, Inter, card con bordo colorato, vetro, scuro a basso contrasto, tre box con icona, badge, icone, dissolvenze, effetti sul cursore, lineette lunghe, corsivo d'accento).
