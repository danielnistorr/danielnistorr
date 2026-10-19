# Hambro, home finale: "Campionario al millimetro"

Pagina: `sito/index.html` (immagini in `sito/img/`, caratteri in `sito/fonts/`). Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale_pagina.html`, screenshot). Prove: `node _prova/script/prova_interazione.mjs <url> <cartella>` e `node _prova/script/largo.mjs <url> <larghezza>`.

Base: il prototipo B, scelto dal committente ("i like them a lot"). Idea, prima schermata, trattamento delle foto, tipografia e colore restano quelli di B. In questo passaggio sono cambiati esecuzione, dati, navigazione, telefono e dettagli (elenco più sotto).

## L'idea
La home è la tavola di un campionario tenuto al millimetro. Gli oggetti stanno sulla stessa carta calda, in pieno sole, e le misure del catalogo Hambro diventano il disegno:
- il righello in scala reale in apertura;
- il banco 1:1 subito sotto, dove la striscia prende la larghezza vera;
- le sagome delle fibbie da ricoprire in scala nella ricopertura;
- le quote di ogni articolo sullo stesso righello 0-60 mm nelle misure per settore.

## Le prime due schermate
1. **Apertura a 1440x900.** La foto della fibbia smontata (Rodrigues, specchiata) prende tutta la pagina. Il titolo "Fibbie, lacci e rinforzi" sta a sinistra sulla carta, a 136 px con interlinea 0,92. Sotto ci sono il sottotitolo, il bottone "Prova le misure, mm 2-60" e la mail. Le due didascalie, "Scala 1:1" a sinistra e "Tav. 1" a destra, hanno la stessa linea di base.
   - Il righello è in scala reale, segue la taratura del banco e sta 32 px sopra la piega: le ultime 32 righe sono solo carta.
   - In cuoio ci sono la quota "2-4" (un filo sopra le tacche 2, 3, 3,5 e 4) e le tacche 16, 20, 25, 30, 40, 50 e 60. I numeri sono a 13 px. Dove un numero non sta nella riga bassa sale in quella alta, e la sua tacca si allunga in verticale (niente fili in diagonale).
   - La borchia sciolta che entrava tagliata dal bordo inferiore è stata tolta dalla foto.
   - **Tablet (701-1100).** La stessa composizione: la foto parte dalla testata e occupa tutta la prima schermata, con un taglio apposta in cui la fibbia esce dal bordo destro. Il titolo è sulla carta a 97 px (1024) e 73 px (768). Sotto i 900 px il righello si ferma a 60 mm, prima del ramo della fibbia.
   - **Telefono (390).** Il titolo è sulla carta, sotto c'è la riga delle sezioni; poi la foto con la fibbia intera, il righello su una striscia di carta e, in fondo allo schermo, 48 px del campo cuoio del banco. Bottone e mail stanno sulla stessa riga.
2. **Banco di misura, sul campo cuoio #6E3519.** Titolo "Lacci e nastri in scala 1:1", la lettura grande "mm 30" e la striscia a tutta pagina, larga 30 mm veri. Il tavolo è alto quanto la striscia più 48 px e cambia altezza con lei in 200 ms, quindi non resta campo vuoto (a 4 mm: 63 px in tutto).

Poi, in ordine:
- **Il cassetto della minuteria.** Una fila per famiglia (moschettoni, anelli e fibbie, attacchi, chiusure), con il nome della famiglia sul bordo come l'etichetta di uno scomparto. Gli 11 scontornati Hambro sono alla stessa scala ottica, con la stessa ombra e lo stesso bianco. Poi "Fuori dal cassetto" e un solo link "Chiedi un campione" (mailto con oggetto).
- **Tav. 2.** Due ritagli stretti delle bobine Hambro, al massimo 360 px di lato.
- **La ricopertura.** Il dittico metallo e pelle con le sagome da 40, 50 e 60 mm in scala reale, i dati, i semilavorati e la foto delle mani.
- **Misure per settore.** Pelletteria, calzatura e abbigliamento uno sotto l'altro. Ogni articolo ha la misura del sito e la sua quota in cuoio su un righello 0-60 mm in scala reale: un tratto per le misure singole, una barra per gli intervalli.
- **Il 1979**, sempre con "Giorgio Gastaldello".
- **I contatti come cartellino da campionario**, in scala reale, legato con un laccio tubolare vero (vedi "La chiusura").
- **Il piede**: una riga sola sulla carta.

## Caratteri
- Mona Sans (GitHub con Degarism), SIL Open Font License 1.1. Il testo della licenza è in `sito/fonts/OFL.txt`; i file vengono da Google Fonts e li serve la pagina (latin e latin-ext, variabile in peso e larghezza). Il preload è stato tolto: in anteprima `file://` dava un errore CORS.
- Una sola famiglia. Il motivo viene dai riferimenti: le etichette DIN di Horween e il grottesco pieno del marchio Mastrotto, cioè un grottesco da catalogo industriale. Uso l'asse della larghezza: 100 per testo e titoli, 112-125 per i numeri grandi, il righello e il marchio.
- **Scala dei corpi: 13, 15, 17, 22, 32, 60 e 136 px**, più la lettura del banco (fino a 232). A 1440 sono in uso 8 corpi, contati sugli elementi visibili (prima erano 19). Ruoli:
  - 13: didascalie, righello, numeri del cassetto;
  - 15: menu, bottoni, elenchi, dati;
  - 17: testo e sottotitolo;
  - 22: famiglie del cassetto, settori, marchio, testo del 1979;
  - 32: telefono nel cartellino, titolo dei semilavorati;
  - 60: tutti gli h2;
  - 136: titolo d'apertura e 1979.
- **Numeri.** Le cifre tabellari di Mona Sans hanno lo zero barrato, quindi restano le cifre proporzionali allineate (`lining-nums`). Misure e orari stanno in colonne allineate a destra.
- Niente Inter, niente monospazio, niente corsivo.

## Colori
- Carta #F2EDE4: il bianco della foto d'apertura, portato in pagina.
- Inchiostro #1B1714.
- Cuoio #7B4524: il marrone del logo Hambro. Lo usano il marchio, il bottone, le tacche del righello, le quote delle misure e il 1979.
- Campo #6E3519: il banco.
- Cartoncino #E8DBC4: solo il cartellino dei contatti (grigio sopra 5,3:1, cuoio 5,7:1, inchiostro 13:1).
- Taglio #3A2012: il bordo della striscia.
- Oro #E2B866: solo il passaggio sui link nei campi scuri.

## Interazione
- **Navigazione.**
  - Sopra i 1000 px: cinque voci in testata (Lacci e nastri, Minuteria, Ricopertura, Misure per settore, Contatti) e il telefono.
  - Sotto i 1000 px: le stesse voci passano su una riga sotto il marchio, che scorre di lato. Ogni voce è alta 44 px.
- **Banco di misura.**
  - Taglio vivo: ogni millimetro da 2 a 60, come dice il sito ("da mm2 a mm60"). Le frecce spostano di 1 mm, Pagina su e giù di 10 mm, Home e Fine vanno agli estremi. Le tacche del cursore sono ogni 10 mm.
  - Tubolare: 2, 3, 4 e 16.
  - Nastro: 20, 25, 30, 40 e 50, in sei colori.
- Radio e range sono nativi, quindi vanno con tastiera e dito. Il cursore è disegnato.
- "Tara lo schermo" apre una tessera di 85,6 mm. La taratura vale per righello, banco, sagome e quote, e resta nel browser; se lo spazio del browser non c'è, la pagina va lo stesso.
- Nessuna animazione allo scorrere, nessun effetto sul cursore. I bottoni cambiano colore pieno, non sbiadiscono.

## Foto: origine e licenza
Tutte passano per la stessa gradazione: la carta come bianco, il sole da sinistra, il cuoio verso #8A5230 (`_prova/script/finale_img.py`).

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura (3 tagli: 1440+, tablet, telefono) | Ruan Richard Rodrigues, Unsplash `2hWmYcG26E8`, specchiata, borchia sciolta tolta | Unsplash License, segnaposto |
| Dittico, il metallo | Ruan Richard Rodrigues, Unsplash `hqGQcZnEvy0` | Unsplash License, segnaposto |
| Dittico, la pelle; striscia del banco | Igor Karimov, Unsplash `DmxTTqZtDds`, portata su #8A5230 | Unsplash License, segnaposto |
| Semilavorati (mani sul cartamodello) | Cohen Berg, Unsplash `an44PeEll_w` | Unsplash License, segnaposto |
| Tav. 2, bobine di laccio e di tondino | hambro.it, foto da telefono, ritagli stretti 360 e 720 px | dell'azienda, da confermare |
| Cassetto, 11 scontornati | catalogo di hambro.it | diritti da chiarire |

In pagina non c'è più nessun avviso sulle foto provvisorie: è nel LEGGIMI e va nella mail di accompagnamento. Nessuna immagine generata. Nessuna foto viene mostrata oltre i suoi pixel: lo controllo con i file veri scelti dal srcset a 1440, 1024 e 390.

## La chiusura (rifatta il 19 ottobre)
Il committente ha notato che quasi tutte le home della campagna finivano allo stesso modo: titolo di luogo, telefono grande su una fascia scura, una riga di colonnine con indirizzo, posta e orari, piede scuro a quattro colonne. Anche qui il cartellino stava su una fascia cuoio piena e sotto c'era il piede nero a quattro colonne.

Ora la chiusura è **un solo oggetto del loro mondo: un cartellino da campionario posato sulla stessa carta della pagina**, come gli altri oggetti, con il sole da sinistra e l'ombra a destra.
- **Il cartellino è largo 100 mm veri** (con la taratura dello schermo, come righello, banco e sagome). Ha gli angoli alti smussati e l'occhiello rinforzato a 13 mm dal bordo. Sotto c'è una quota che scrive la larghezza vera: "mm 100" a 1440, 1024 e 768. Dove il telefono non ha 100 mm di spazio il cartellino si stringe e la quota lo dice ("mm 93" a 390, "mm 74" a 320).
- **Il laccio è un laccio tubolare in pelle da 3 mm in scala reale** (un articolo del catalogo, nelle misure per settore e nel banco). Passa nell'occhiello e i due capi tagliati restano sciolti sulla carta. La didascalia dice "Laccio tubolare in pelle, mm 3".
- **Sul cartellino, in ordine:** il marchio, il telefono a 32 px (`tel:`, sottolineato, alto 44 px), la posta (`mailto:`), l'indirizzo con "Apri la mappa" (Google Maps) e gli orari. Le etichette sono a 13 px e i dati a 15. Sono gli stessi dati di prima, nessuno nuovo.
- **Il piede è una riga sola sulla carta,** sotto un filetto: Hambro srl, P.IVA 00967020280, Informativa privacy e, a destra, Facebook. Il corpo è 15 px, in grigio (6,2:1). La PEC non c'è, perché non era in pagina.

Tolto: la fascia cuoio piena dei contatti, il piede nero a quattro colonne con il marchio ripetuto, l'indirizzo, il telefono e la posta ripetuti nel piede. Le fasce di fondo a tutta larghezza scendono da 4 a 3.

Perché così: la pagina parla di misure vere, e chiudere con un cartellino in scala e un laccio del catalogo in scala tiene l'idea fino in fondo, con un oggetto solo e niente di nuovo da leggere. Anche la carta continua fino alla fine, invece di chiudere su due fasce scure come le altre home della campagna.

## Cosa è cambiato nel passaggio precedente (rilievi del giudice cieco)
Applicati:
- **Didascalie e piede.** Tolte le cinque note "foto provvisoria" e "Proposta di nuova home". `grep -ci "provvisori\|da rifare\|Proposta di nuova home" sito/index.html` dà 0.
- **Menu sotto i 1100 px.** La riga di sezioni scorrevole sotto i 1000 px; tra 1000 e 1100 il menu resta in testata. A 1024 si vedono 5 voci, a 390 se ne vedono 3 intere e le altre si raggiungono scorrendo la riga.
- **Tablet.** La composizione sovrapposta del 1440, con la foto al 100 % della prima schermata a 1024 e a 768.
- **Bordo della prima schermata.** Tolta la borchia tagliata, righello alzato di 32 px, quota "2-4" al posto di "3,5" e "4" col filo diagonale.
- **Sezioni da modello.** Le tre colonne uguali di settore sono diventate un solo elenco di misure con le quote in scala. I contatti sono un cartellino, non più telefono a 120 px più tre colonne (e in questo passaggio il cartellino è sceso dal campo cuoio sulla carta, vedi "La chiusura"). Il cassetto è a file per famiglia.
- **Bobine.** Mostrate al massimo a 360 px di lato.
- **Scala tipografica.** Da 19 corpi a 8, con la scala qui sopra.
- **Banco.** Il tavolo è alto quanto la striscia più 48 px.
- **Dati.**
  - Taglio vivo da 2 a 60 al millimetro.
  - Didascalia del righello corretta.
  - "Accessori in legno e bambù, in plastica e metallo nichel free, con strass".
  - Tolti "a rotolo", "a bobina" e "su misura", che non erano nelle fonti.
- **Cassetto.** Le card non sono più link a #contatti; c'è un solo "Chiedi un campione".
- **Preload del carattere.** Tolto.
- **Voce.** "Il laboratorio attrezzato realizza..." è diventato "In laboratorio facciamo componenti semilavorati...".

Respinto:
- **Il banco 1:1 al posto della foto in apertura.** Il committente ha visto la prima schermata e ha scritto "i like them a lot". La consegna dice di non ripensarla. Dentro l'idea ho fatto quello che si poteva fare senza cambiarla: righello intero, più leggibile e staccato dalla piega; fondo pulito; tablet sovrapposto come il 1440.

## Controlli
- **Screenshot in questa cartella.**
  - `home-1440.jpg` (intera, 9090 px);
  - `home-1440-prima-schermata.jpg`;
  - `home-390.jpg` (intera, 8541 px);
  - `home-390-prima-schermata.jpg`.
  - `chiusura-1440.jpg`: solo la chiusura a 1440, dall'inizio dei contatti alla fine della pagina.
  - La chiusura è stata guardata a pezzi a 1440, 1024, 768, 390 e 320 (e controllata anche a 1101, 1100, 920, 700 e 360): nessuna sovrapposizione tra i testi, nessuno scorrimento orizzontale.
  - Guardati a pezzi anche 320, 768, 1024 e 1920 (PNG in `_prova/screenshot-tmp/`, cancellati dopo il controllo).
- **Scorrimento orizzontale.** scrollWidth uguale a innerWidth a 320, 360, 390, 700, 701, 768, 900, 1000, 1024, 1100, 1280, 1440, 1920 e 2560.
- **Tastiera, a 1440 e 1024.** Freccia sui materiali dà Tubolare 4; End dà 16; Home più freccia dà 3. Il taglio vivo, ripreso a 30, con due volte Pagina giù e una freccia dà 9. Nastro 50 giallo funziona.
- **Tocco, a 390.** Un tocco su Tubolare dà 4; un tocco in fondo al cursore dà 16; Taglio vivo con un tocco all'inizio dà 2; nastro 50 giallo funziona.
- **Menu.** Il link Contatti porta alla sezione.
- **Console.** Nessun errore e nessun avviso a 1440, 1024 e 390.
- **Collegamenti.**
  - `tel:+390499802326`;
  - `mailto:commerciale@hambro.it` (anche con oggetto per i campioni);
  - Google Maps sull'indirizzo di via dell'Artigianato 30, Vigonovo;
  - Facebook;
  - nessuna ancora senza destinazione.
- **U+2014.** Assente in pagina, script, NOTA, LEGGIMI e CREDITI.
- **`segnali.sh`.** 0 soglie bloccanti. Foto 37 %, Mona Sans 100 %, nessuna tabella oltre 4 righe, 0 frecce, 3 fasce di fondo (erano 4 prima della chiusura nuova), 19 filetti. Da guardare, e motivati nel LEGGIMI:
  - una sola misura di H2;
  - 2 numeri grandi (la lettura del banco e il 1979 con il nome);
  - l'indice 01-11 del cassetto.

## Cosa manca perché la prima schermata arrivi a 8
Una foto vera di Hambro in apertura: una loro fibbia in zama smontata, sulla stessa carta e con lo stesso sole radente da sinistra (indicazioni di scatto nel LEGGIMI). Con la foto di Rodrigues la pagina resta "un fornitore di minuteria qualunque, fatto molto bene". La prima schermata non è stata ripensata, per scelta del committente.
