# Home finale, Belletti: "Il carattere dell'edificio"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli sulla pagina, screenshot con `shot_finale.mjs`). Base: prototipo A, con gli innesti da B scelti dal giudice.

## Idea

Un lavoro vero, letto come un disegno d'architetto: il cilindro di vetro di Cà della Nave accanto all'ala seicentesca delle ex scuderie di Villa Grimani Morosini. Una sola linea di quota, sottile, va dal muro antico al vetro nuovo. A un capo c'è "Ala ovest, seconda metà del '600", all'altro "Ascensore tondo, 480 kg, 5 persone, 4 fermate". Il contrasto tra vecchio e nuovo è il mestiere di Belletti: disegna l'ascensore attorno all'edificio. Sopra c'è un titolo stretto e leggero come un architrave, "Ascensori dal 1908". Con il nome di un concorrente la pagina non regge, perché foto, legende e schede sono loro.

Rispetto al prototipo ho tolto i tre pallini numerati, che ripetevano il gesto di Mario Agnoletto e di Area Systems. Al loro posto c'è la quota, con le due tacche alle estremità come nei disegni tecnici.

## Prime due schermate

- **1440**:
  - Testata di 88 px con il logo vero in SVG, cinque voci e il telefono.
  - Il titolo sta su una riga a 170 px, in Radio Canada 300 stretto al 75 %.
  - La foto parte a 268 px dall'alto, va da 540 px al bordo destro (900 px reali) e scende oltre la piega, fino a 1045 px.
  - A sinistra: la frase su cosa fanno, il bottone verde "Chiama lo 049 508 2430", il numero dei guasti e, in basso, la didascalia di due righe con il luogo e i progettisti.
  - Scorrendo si arriva a "Un secolo e tre generazioni", con tre fatti brevi a destra, e poi ai lavori.
- **390**:
  - Il titolo va su due righe a 74 px, poi la frase, il bottone e i guasti.
  - Segue la foto in 4:5, tagliata sullo spigolo dell'ala e sul cilindro, con la sola linea di quota.
  - Sotto la foto, in due colonne, "Il muro" e "Il vetro", poi la didascalia.
  - Le schede dei lavori scorrono in orizzontale, gli impianti stanno in una colonna, le colonne del piede si aprono a fisarmonica con veri bottoni.
- **Misure**: la pagina è alta 5151 px a 1440, piede compreso (6799 px a 390). Ho controllato anche 320, 768, 1024 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione.

## Sezioni

1. Apertura.
2. Storia: Rodolfo, Paolo ed Elvira, Gaetano e Irma, l'ing. Viel; trenta addetti, Veneto e Friuli, per chi.
3. Lavori. Il titolo è la loro frase "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito", con sotto "L'ascensore rispecchia il carattere dell'edificio". Tre schede in fila con la sottolineatura verde sull'attiva. Sotto, la foto a filo del bordo sinistro (708 x 540) e, allineate in alto, la descrizione, i cinque dati e i progettisti.
4. Impianti a tutta larghezza: sei famiglie in 3 colonne per 2 righe, senza foto e senza icone.
5. Assistenza, una fascia corta: "Assistenza 24 ore, dal 1997" con una frase; a destra i quattro servizi presi da B e lo 049 900 5131 a 40 px.
6. Chiusura con foto: la sede di sera con il furgone dell'assistenza, a filo del bordo sinistro. A destra la loro frase "Trenta cuori e una sola anima" e sotto i recapiti: uffici a 32 px, guasti, email, indirizzo con "Apri la mappa". Gli orari non sono pubblicati, quindi non ci sono.
7. Piede: logo SVG a 170 px con una riga su chi sono; colonne Azienda, Impianti, Assistenza (con Servoscala), Seguici (solo YouTube); la riga legale.

Spazio fisso tra le sezioni: 160 px a 1440, 96 px a 390.

## Caratteri e colori

- **Carattere**: Radio Canada, una famiglia variabile da Google Fonts con licenza SIL Open Font License 1.1 (uso commerciale libero). La pagina la serve da `sito/fonts/` (woff2 latin e latin-ext).
  - Titoli in peso 300; quello d'apertura è stretto al 75 % e richiama le lettere condensate del logo e la verticalità del vano.
  - Testo in 400, enfasi in 500. Cifre tabellari per misure e telefoni.
  - Riferimenti: Schindler (1) usa un umanistico leggero, Frutiger Light, per l'ascensore nel palazzo; seele (2) un grottesco pulito su bianco.
  - Niente Inter, niente monospazio, niente corsivo.
- **Colori**:
  - Calce #F6F5F2 per il fondo, inchiostro #1B1D1F, grigio #58595B per i testi secondari (6,4:1 sul fondo).
  - Verde #007A43 (5,4:1 con il testo bianco) solo sul bottone, sui link al passaggio e sulla scheda attiva. Il verde chiaro #009A54 resta solo nel logo.
  - Il piede sta su #ECEAE5, stesso tono: il grigio #58595B ci fa 5,8:1.

## Interazione

C'è un solo gesto, il selettore dei lavori (Galleria Cavour, Ca' Michiel, Cà della Nave). Un tocco o le frecce della tastiera (anche Home e Fine) cambiano foto, descrizione e scheda tecnica, senza transizioni. Usa i ruoli ARIA tablist e tabpanel, con il fuoco visibile. A 390 la fila delle schede scorre col dito, con l'aggancio. Provato con `_prova/script/prova_tab.mjs`: clic e freccia portano a Cà della Nave con il fuoco giusto; la fisarmonica e il menu si aprono. Non ci sono animazioni allo scorrere né effetti sul cursore; i link cambiano a colore pieno.

## Foto: origine e licenza

Sono tutte foto di impianti Belletti. In pagina non c'è nessuna foto di repertorio.

| File in `sito/img/` | Soggetto | Origine |
|---|---|---|
| `apertura-cadellanave-*`, `-tel-*` | Cà della Nave, Martellago, dalla corte | redazionale DiBaio `assets/originali/pdf/01_DiBaio_Martellago.pdf`, immagine 942x694 (la più grande nel PDF, controllato con `pdfimages -list`), `_prova/crawl/pdfimg/mart-007.jpg`; taglio 660x570, mostrata a 900 px |
| `lavoro-cavour-*` | Galleria Cavour, Padova, di giorno | `02_DiBaio_Cavour.pdf`, `cav-003.jpg` |
| `lavoro-camichiel-*` | Ca' Michiel, Venezia, cabina dall'alto | depliant 2008, `d-020.jpg` |
| `lavoro-cadellanave-*` | Cà della Nave, scala a chiocciola dall'alto | `01_DiBaio_Martellago.pdf`, `mart-021.jpg` |
| `chiusura-sede-*` | sede di Mestrino di sera, furgone dell'assistenza | depliant 2008, `d-027.jpg`; targa sfocata |
| `logo-belletti.svg` | logo vero | tracciati del depliant 2008, `assets/originali/logo-belletti-depliant.svg` |

- **Trattamento comune**: autocontrasto leggero, saturazione 0,9, contrasto 1,03 e una maschera di contrasto lieve, senza nitidezza vistosa. Esportate in WebP in tre o quattro larghezze per srcset (`_prova/script/finale_img.py`).
- **Diritti**: le foto stanno nei PDF che Belletti pubblica sul suo sito, ma il fotografo non è indicato. Prima di pubblicare va chiesto chi le ha scattate e con quali diritti, anche all'editore DiBaio per quelle dei redazionali.
- **Villa Pavan tolta**: la stampa CMYK resta falsa anche convertita con un profilo SWOP, e un quarto lavoro con foto e dati tecnici non c'è.
- **Facciata a griglia nera della sede (`d-051`) tolta**, come chiesto dal giudice.
- **Chiusura**: la foto non compare altrove nella pagina e non è usata in altre home della campagna.

## Controlli

- **`segnali.sh`** (`_prova/tmp-finale/segnali`, cancellata dopo la lettura): 16 soglie su 18 a posto.
  - Area foto 23,1 %, sotto il 35 %. Le foto vere sono di 590-950 px e non le ho stirate (l'apertura è già ingrandita 1,36 volte). Il giudice ha chiesto zero foto di repertorio e la foto d'apertura al massimo a 900 px. È la prima cosa da chiedere a Belletti: gli originali del fotografo.
  - Numeri grandi: 2 ("6" persone e "2" fermate). Sono i dati tecnici veri della scheda del lavoro, cioè il prodotto.
  - Una famiglia sola, 0 % di monospazio, 0 frecce, 5 filetti, 2 fasce di fondo (pagina e piede).
  - "Titolo a sinistra e paragrafo a destra" in 1 sezione, la storia, dove a destra stanno tre fatti brevi.
- **Testi**: nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (controllo dentro `build_finale.sh`). Nessuna dissolvenza, nessuna icona, nessun badge, nessuna card.
- **Dati**: tutti da `01-analisi.md` e dai testi del sito o dei redazionali. "Nelle province del Veneto" è scritto come sul sito, senza "tutte".
- **Newsletter**: non c'è, e non avrebbe senso. La pagina News è vuota da anni, non ci sono fiere né cataloghi nuovi (il depliant è del 2008) e i clienti (condomini, progettisti, enti) cercano un numero di telefono, non aggiornamenti.
