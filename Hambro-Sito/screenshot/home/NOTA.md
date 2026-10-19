# Hambro, home finale: "Campionario al millimetro"

Pagina: `sito/index.html` (immagini in `sito/img/`, caratteri in `sito/fonts/`). Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale_pagina.html`, screenshot). Prova del banco di misura con clic e tastiera: `node _prova/script/prova_pagina.mjs <url> <cartella> [larghezza] [altezza] [mobile]`.

Base: il prototipo B, scelto dal committente. Idea, prima schermata, trattamento delle foto, tipografia e colore restano quelli di B; sono cambiati esecuzione, dati, telefono e dettagli, più due innesti da A (il dittico metallo e pelle con le sagome in scala, il telefono come targa nei contatti).

## L'idea
La home è la tavola di un campionario tenuto al millimetro. Gli oggetti stanno sulla stessa carta calda, in pieno sole, e le misure del catalogo Hambro (lacci da 2 a 60, tondini da 2 a 3,5, tubolari fino a 16, nastri da 20 a 50, fibbie da ricoprire 40, 50 e 60) diventano il disegno: un righello in scala reale in apertura, uno strumento subito sotto, le sagome delle fibbie in scala nella ricopertura.

## Le prime due schermate
1. Apertura a 1440x900. La foto della fibbia smontata (Rodrigues, specchiata) prende tutta la pagina; il titolo "Fibbie, lacci e rinforzi" sta a sinistra sulla carta, a 136 px con interlinea 0,92. Il sottotitolo è di tre righe. Segue il bottone "Prova le misure, mm 2-60", che porta al banco, con la mail accanto. Le due didascalie, "Scala 1:1" a sinistra e "Tav. 1" a destra, hanno la stessa forma e la stessa linea di base. La lineetta verticale color cuoio non c'è più.
   - Il righello in fondo è in scala reale e segue la taratura del banco.
   - Le tacche delle misure a catalogo (2, 3,5, 4, 16, 20, 25, 30, 40, 50, 60) sono in cuoio, alte 18 px, con il numero in cuoio sopra. Dove i numeri non ci stanno, 3,5 e 4 salgono di una riga con un filo fino alla tacca.
   - Le altre tacche sono in inchiostro al 40 %.
   - Il righello si ferma a 100 mm; dopo, la riga sfuma sotto la fibbia.
   - A 390 il titolo sta sulla carta. Sotto c'è la foto, tagliata su una fibbia intera (anello, ardiglione e borchie tutti dentro), poi il righello su una striscia di carta di 34 px. In fondo allo schermo si vedono 42 px del campo cuoio del banco. Telefono in testata, bottone alto 44 px.
2. Banco di misura, sul campo cuoio #6E3519. Titolo "Lacci e nastri in scala 1:1", la lettura grande "mm 30" e la striscia a taglio vivo a tutta pagina, larga 30 mm veri.
   - La striscia è grana di cuoio desaturata verso #8A5230, con il taglio vivo più scuro (1 px #3A2012 sopra e sotto).
   - L'ombra parte dalla stessa x della striscia, scende di 6 px ed è sfocata.

Poi, in ordine:
- il cassetto della minuteria: 11 famiglie, con gli scontornati Hambro alla stessa scala ottica, con la stessa ombra e lo stesso bianco. "Fuori dal cassetto" è chiuso da un filetto inchiostro sulla carta, non più dal riquadro nero;
- Tav. 2: due bobine del magazzino Hambro, laccio a taglio vivo e tondino. Prendono il posto della corda di Tepavac, che era fuori scala;
- la ricopertura: il dittico metallo e pelle con le sagome da 40, 50 e 60 mm in scala reale, i dati e i semilavorati, con la foto delle mani;
- le tre colonne pelletteria, calzatura e abbigliamento;
- il 1979, sempre insieme a "Giorgio Gastaldello";
- i contatti, con il telefono a 120 px;
- il piede con i dati societari.

## Caratteri
- Mona Sans (GitHub con Degarism), licenza SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`, file presi da Google Fonts e serviti dalla pagina (latin e latin-ext, variabile in peso e larghezza).
- Una sola famiglia. Il motivo viene dai riferimenti: le etichette DIN di Horween e il grottesco pieno del marchio Mastrotto, cioè un grottesco da catalogo industriale. Uso l'asse della larghezza:
  - 100 per testo e titoli;
  - 112-125 per i numeri grandi, il righello, il telefono e il marchio.
- Scala:
  - apertura 136 px, peso 380, spaziatura -0,04em;
  - h2 60 e 80 px;
  - telefono 120 px, peso 300, larghezza 112;
  - lettura del banco fino a 232 px;
  - testo 17 px;
  - didascalie 13 px;
  - maiuscolo spaziato solo per le etichette dei contatti.
- Numeri: le cifre tabellari di Mona Sans hanno lo zero barrato e l'1 con la grazia, quindi la pagina sembrerebbe un terminale. Restano le cifre proporzionali allineate (`lining-nums`); misure, orari e codici stanno in colonne allineate a destra.
- Niente Inter, niente monospazio, niente corsivo.

## Colori
- Carta #F2EDE4: il bianco della foto d'apertura, portato in pagina. Lo stesso principio della carta terracotta di Riri.
- Inchiostro #1B1714.
- Cuoio #7B4524: marchio, bottone, tacche del righello e 1979. È il marrone del logo Hambro.
- Campo #6E3519: banco e contatti, il colore pieno della pagina, come il fondo di Mastrotto.
- Taglio #3A2012: il bordo della striscia.
- Oro #E2B866: solo il passaggio sui link nei campi scuri.
- Il colore pieno dei nastri viene dai rotoli della foto Hambro (`originali/202008281a708a….jpeg`).

## Interazione
- Banco di misura con tre scelte.
  - Taglio vivo: il cursore si aggancia alle misure a catalogo 2, 3, 3,5, 4, 16, 20, 25, 30, 40, 50 e 60. Il taglio a qualsiasi millimetro non è confermato.
  - Tubolare: 2, 3, 4 e 16.
  - Nastro: 20, 25, 30, 40 e 50, in sei colori.
- La striscia cambia altezza in 200 ms.
- Il cursore è disegnato: traccia in carta al 30 %, tacche sulle misure, pomello carta, nessun grigio di sistema.
- Frecce, Home e Fine saltano da una misura all'altra. Radio e range sono nativi, quindi funzionano anche con tastiera e dito.
- Il link "Tara lo schermo" apre una tessera di 85,6 mm. La taratura vale per righello, banco e sagome e resta nel browser; se lo spazio del browser non c'è, la pagina va lo stesso.
- Il selettore Oro/Nichel di A non c'è: arriverà con lo still life della stessa fibbia in più finiture.
- Nessuna animazione allo scorrere, nessun effetto sul cursore. I bottoni cambiano colore pieno, non sbiadiscono.

## Foto: origine e licenza
Tutte passano per la stessa gradazione: la carta come bianco, il sole da sinistra, il cuoio verso #8A5230 (`_prova/script/finale_img.py`).

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura (3 tagli: 1440+, tablet, telefono) | Ruan Richard Rodrigues, Unsplash `2hWmYcG26E8`, specchiata | Unsplash License, segnaposto |
| Dittico, il metallo | Ruan Richard Rodrigues, Unsplash `hqGQcZnEvy0` (la fibbia oro), fondo ripulito dal rumore | Unsplash License, segnaposto |
| Dittico, la pelle; striscia del banco | Igor Karimov, Unsplash `DmxTTqZtDds`, portata su #8A5230 | Unsplash License, segnaposto |
| Semilavorati (mani sul cartamodello) | Cohen Berg, Unsplash `an44PeEll_w` | Unsplash License, segnaposto |
| Tav. 2, bobine di laccio e di tondino | hambro.it, `originali/2020082819b5….jpeg` e `20200828c559….jpeg` (foto da telefono) | dell'azienda, da confermare |
| Cassetto, 11 scontornati | catalogo di hambro.it (`originali/`, 400x300 e 640x480) | diritti da chiarire, sembrano foto di produttore |

Le foto di fibbie dorate di Rodrigues restano a questa home. Pagine e licenze sono in `assets/CREDITI.md`. Nessuna immagine generata. Non sono più usati Tepavac, Juno Jo e Devon Chan.

## Controlli
- Screenshot:
  - `home-1440.jpg` (intera, 8422 px);
  - `home-1440-prima-schermata.jpg`;
  - `home-390.jpg` (intera);
  - `home-390-prima-schermata.jpg`.
  - Guardati a pezzi anche 320, 768, 1024 e 1920.
- Nessuno scorrimento orizzontale a nessuna larghezza, nessuna sovrapposizione.
- Banco provato con clic e tastiera a 1440 e a 390: tubolare più tre frecce dà 16, nastro 50 giallo.
- U+2014: assente in pagina, script e note.
- `segnali.sh`: 0 soglie bloccanti. Area foto 46,1 %, Mona Sans 100 %, 4 misure di H2, 18 filetti, 0 frecce. Da guardare:
  - 5 fasce: apertura, banco, carta, contatti, piede. Sono volute: un fondo carta e due campi cuoio;
  - 2 numeri grandi: la lettura del banco, che è lo strumento, e il 1979 con il nome;
  - la numerazione 01-11 del cassetto, che è l'indice del campionario.

## Cosa manca perché la prima schermata arrivi a 8
La prima schermata non è stata ripensata. Le mancano due cose.
- Una foto vera di Hambro in apertura: una loro fibbia in zama smontata, sulla stessa carta e con lo stesso sole radente da sinistra. Con la foto di Rodrigues la pagina resta "un fornitore di minuteria qualunque, fatto molto bene".
- Il righello letto come catalogo Hambro: le tacche in cuoio ci sono già, ma serve la conferma delle misure (vedi LEGGIMI). Con le misure confermate si possono scrivere i nomi degli articoli sotto le tacche.
