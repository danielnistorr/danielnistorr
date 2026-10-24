# Home finale, Belletti: "Il carattere dell'edificio"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli sulla pagina, screenshot con `shot_finale.mjs`). Il collaudo dell'interazione e delle misure è in `_prova/script/prova_finale.mjs`.

## Idea

La loro frase, "L'ascensore rispecchia il carattere dell'edificio", è il titolo, e sotto c'è la prova: un solo lavoro vero, al centro della pagina. È il cilindro di vetro di Ca' della Nave accanto all'ala seicentesca delle ex scuderie di Villa Grimani Morosini. Il vecchio e il nuovo stanno nella stessa foto, che si vede intera, alla sua misura reale, con tanta calce intorno. È il mestiere di Belletti: disegna l'ascensore attorno all'edificio. Con il nome di un concorrente la pagina non regge, perché frase, foto e schede sono loro.

## Cosa è cambiato in questo passaggio (dopo il giudizio cieco)

- **Prima schermata**:
  - Il titolo era "Ascensori dal 1908" con il testo a sinistra e la foto a destra fino al bordo. Ora c'è la loro frase su due righe, centrata, e sotto la foto centrata.
  - Lead e bottone sono scesi sotto la foto, in una riga larga quanto l'immagine. Il 1908 è passato nel lead ("Dal 1908 progettiamo…").
- **Nitidezza**: la foto d'apertura era un ritaglio di 660 px mostrato a 900. Ora è l'inquadratura intera del redazionale (942x592, senza le panchine) mostrata a 900 px. Il rapporto naturalWidth / larghezza mostrata vale 1,00 o più da 320 a 2560 px (misurato).
- **Legende e quota tolte**: niente linea di quota senza misura e niente legende sulla foto. Resta una sola didascalia sotto l'immagine, con il link "La scheda del lavoro", che apre direttamente la scheda Ca' della Nave nel selettore.
- **Ca' della Nave non si ripete più con gli stessi dati**: i dati tecnici (480 kg, 5 persone, 4 fermate) ora stanno solo nella scheda del selettore, che ha un'altra foto (la scala a chiocciola dall'alto). L'apertura mostra il lavoro, la scheda lo spiega.
- **Storia**: i tre fatti in colonna sono diventati l'ultima frase del racconto (trenta addetti, oltre venti tecnici, Veneto e Friuli). "Per chi" è passato sotto il titolo degli Impianti.
- **Assistenza**: è diventata una fascia corta, con titolo e una frase a sinistra e il numero dei guasti grande a destra. La griglia dei quattro servizi è tolta, i servizi stanno in una frase, e con lei è sparita la riga "Ogni anno…" contestata dal giudice. Nota: il sito di Belletti dice davvero "ogni anno gli impianti vengono sottoposti ad accurati controlli" (`assistenza.aspx`); il depliant dice invece "con frequenza variabile". In pagina non c'è più nessuna delle due.
- **Telefoni**:
  - Il numero dei guasti c'è tre volte: nell'apertura, nella fascia Assistenza e nel piede. Dalla chiusura è tolto e non ci sono più due blocchi di telefoni di seguito.
  - Il numero degli uffici sta in testata, nel bottone d'apertura e nella chiusura.
- **Ca' Michiel**: nuovo taglio alto sulla cabina col mosaico, il tetto in inox e i fiori del balcone, senza il fondo buio del cortile.
- **Grafia**: "Ca’ della Nave" con l'apostrofo, come "Ca’ Michiel", in schede, didascalie e alt.
- **Testata a 390**: ora mostra anche il numero degli uffici, che sotto i 375 px si nasconde.
- **Piede**:
  - A 1440 le quattro colonne hanno la stessa larghezza (due colonne di griglia ciascuna), con spazi uguali.
  - A 390 "Seguici: YouTube" è una riga semplice, senza fisarmonica.
  - Tutti i link del piede, della riga legale e dei recapiti sono alti almeno 24 px a 390 (misurato).
- **Preload del carattere tolto**: a file:// la console non ha più errori.
- **Altezza**: 5300 px a 1440 piede compreso (prima 5151), 6253 px a 390.

## Prime due schermate

- **1440**:
  - Testata di 88 px con il logo vero in SVG, cinque voci e il telefono.
  - Il titolo in Radio Canada 300, stretto al 75 %, 100 px su due righe centrate, va da 112 a 300 px.
  - La foto, larga 900 px e centrata, parte a 336 px e finisce a 902: sta quasi tutta nella prima schermata.
  - Sotto: la didascalia con il link alla scheda; poi il lead a sinistra e il bottone verde con il numero dei guasti a destra, allineati ai bordi della foto.
- **390**:
  - Testata con logo, telefono e Menu.
  - Il titolo va su quattro righe a 55 px; la foto a tutta larghezza, in 4:5 sullo spigolo dell'ala e sul cilindro, chiude la prima schermata.
  - Sotto: didascalia, lead, bottone e guasti.
- Ho controllato anche 320, 768, 1024 e 1920. Da 641 a 1080 la foto è centrata e larga quanto il testo; sotto i 640 va a tutta larghezza.

## Sezioni

1. Apertura.
2. Storia: un solo racconto, da Rodolfo all'ing. Viel, fino ai trenta addetti di oggi.
3. Lavori: il titolo è la loro frase "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito". Tre schede in fila (Galleria Cavour, Ca' Michiel, Ca' della Nave); sotto, la foto a filo del bordo sinistro e, a destra, la descrizione, i cinque dati e i progettisti.
4. Impianti: "Per chi" in una riga, poi sei famiglie in 3 colonne per 2 righe, con descrizioni di una riga, senza foto e senza icone.
5. Assistenza, una fascia corta.
6. Chiusura con foto: la sede di sera, a filo del bordo sinistro. A destra la loro frase "Trenta cuori e una sola anima" e i recapiti: uffici a 32 px con tel:, email con mailto:, indirizzo con "Apri la mappa". Gli orari non sono pubblicati, quindi non ci sono.
7. Piede:
   - logo SVG con una riga su chi sono;
   - le colonne Azienda, Impianti, Assistenza e Seguici (solo YouTube);
   - la riga legale con ragione sociale, P.IVA, REA, Privacy e Cookie.

## Caratteri e colori

- **Carattere**: Radio Canada (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), servito da `sito/fonts/`.
  - Titoli in 300; quello d'apertura è stretto al 75 % come le lettere condensate del logo.
  - Testo in 400, enfasi in 500, cifre tabellari per misure e telefoni.
  - Niente Inter, niente monospazio, niente corsivo.
- **Colori**:
  - Calce #F6F5F2, inchiostro #1B1D1F, grigio #58595B (6,4:1 sul fondo, 5,8:1 sul piede #ECEAE5).
  - Verde #007A43 (5,4:1 con il bianco) solo sul bottone, sui link al passaggio e sulla scheda attiva.

## Interazione

C'è un solo gesto, il selettore dei lavori, con i ruoli ARIA tablist e tabpanel. Clic, tocco, frecce, Inizio e Fine cambiano foto, descrizione e scheda tecnica, senza transizioni. Il link della didascalia d'apertura apre la scheda Ca' della Nave. Non ci sono animazioni allo scorrere né effetti sul cursore.

## Foto

Tutte di impianti Belletti, dai PDF del loro sito; nessuna foto di repertorio. Trattamento comune: autocontrasto leggero, saturazione 0,9, contrasto 1,03 e una maschera di contrasto lieve. Esportate in WebP in più larghezze per srcset, mai oltre la larghezza reale.

| File in `sito/img/` | Soggetto | Origine |
|---|---|---|
| `apertura-cadellanave-*` | Ca' della Nave dalla corte | `01_DiBaio_Martellago.pdf`, `mart-007.jpg` 942x694, taglio 942x592 |
| `apertura-cadellanave-tel-*` | lo stesso, 4:5 per il telefono | taglio 456x570 |
| `lavoro-cavour-*` | Galleria Cavour di giorno | `02_DiBaio_Cavour.pdf`, `cav-003.jpg` |
| `lavoro-camichiel-*` | Ca' Michiel, cabina dall'alto | depliant 2008, `d-020.jpg`, taglio alto |
| `lavoro-cadellanave-*` | Ca' della Nave, scala a chiocciola dall'alto | `mart-021.jpg` |
| `chiusura-sede-*` | sede di Mestrino di sera | depliant 2008, `d-027.jpg`, targa sfocata |
| `logo-belletti.svg` | logo vero | tracciati del depliant 2008 |

## Controlli

- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 640, 641, 768, 900, 1024, 1080, 1180, 1280, 1440, 1680, 1920 e 2560 (`prova_finale.mjs`).
- **Interazione**: provata con `prova_finale.mjs`:
  - con la tastiera: Tab raggiunge il selettore; frecce destra e sinistra (anche col giro), Inizio e Fine spostano il fuoco e aria-selected;
  - con il mouse: clic su Ca' Michiel; il link della didascalia porta a #lavori con Ca' della Nave aperta;
  - con il tocco a 390: scheda, menu, fisarmonica del piede.
- **Collegamenti**:
  - tel:+390495082430 e tel:+390499005131;
  - mailto:info@bellettiascensori.it;
  - la mappa Google con Via della Tecnica 29, Mestrino;
  - YouTube @BellettiAscensori.
- **Console**: nessun errore a file://.
- **Testi**: nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (controllo dentro `build_finale.sh`).
- **Segnali da IA** (`_metodo/kit/segnali.sh`, uscita cancellata dopo la lettura): 16 soglie su 18 a posto.
  - Area foto 20,3 %, sotto il 35 %. È una scelta: il giudice ha chiesto che l'unico oggetto sia nitido, quindi nessuna foto è mostrata oltre la sua larghezza reale (590-950 px). Gli originali del fotografo sono la prima cosa da chiedere a Belletti (LEGGIMI).
  - Numeri grandi: 2 ("6" persone e "2" fermate). Sono i dati tecnici veri della scheda del lavoro, cioè il prodotto.
  - Il resto è a posto:
    - una famiglia sola, 0 % di monospazio, 0 frecce, 4 filetti;
    - 2 fasce di fondo (pagina e piede);
    - 0 sezioni "titolo a sinistra e paragrafo a destra";
    - nessun titolo col punto e nessuna etichetta maiuscola.
- **Screenshot guardati a pezzi**: `home-1440.jpg`, `home-390.jpg`, le prime schermate e le pagine di controllo a 320, 768, 1024 e 1920 (PNG cancellati dopo la lettura).
- **Newsletter**: non c'è, e non avrebbe senso. La pagina News è vuota da anni e non ci sono fiere né cataloghi nuovi (il depliant è del 2008). I clienti sono condomini, progettisti ed enti: cercano un numero di telefono, non aggiornamenti.
