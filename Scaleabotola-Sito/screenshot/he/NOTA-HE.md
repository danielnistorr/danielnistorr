# Scalarredo, home HE: nota

Pagina: `../../sito-he/index.html` (kit in `sito-he/kit/`, caratteri e immagini in locale). Direzione: `../../DIREZIONE-HE.md`. Ottavo pilota del sistema HE, 7/11/2026. Non pubblicata, azienda non contattata.

## L'idea

La pagina è un soffitto bianco con una botola. In prima schermata il pannello chiuso è disegnato da un filetto e lascia vedere solo una fessura con i gradini; scorrendo la botola si apre e si vede la scala retrattile dall'alto, con "Scale" e "a botola" ai due lati in New Title. Poi la pagina scende come una scala: tre pedate in frassino per le retrattili, la firma "Una vera scala da interno" (la frase loro sulla PLUS con i gradini in frassino da 14 cm), le scale per interno su misura, il modulo, lo showroom di Mestrino con il telefono su tutta la riga.

## File

- `foglio-1440.jpg`, `foglio-390.jpg`: i fotogrammi del video (uno al secondo), da `_metodo/highend/kit/registra.mjs`.
- `prima-schermata-1440.jpg`, `prima-schermata-390.jpg`.
- `scorrimento-*.mp4` e `fotogrammi-*` restano fuori da git (si rigenerano).
- Prove, schermate di lavoro, riferimenti e script in `../../_prova/he/` (fuori da git): `prove-finale.json`, `script/immagini.py` (un solo trattamento per tutte le foto), `script/mappa.py`, `riferimenti/`.

## Foto

Originali riscaricati dalla libreria media di scalarredo.it (`/wp-json/wp/v2/media`, 474 voci) il 7/11/2026, anche le versioni senza `-scaled` (sul server sotto `/wordpress/wp-content/uploads/`): 121 file in `assets/originali/wp/`, fuori da git. In pagina, sempre sotto la misura nativa (rapporto peggiore 0,65 a 1440, 0,80 a 1920):

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| botola (apertura) | `2026/05/elementilegno.jpg` | 2020x2491 | 610x752 |
| motorizzata | `2026/05/motorizzata3.jpg` | 1440x2560 (tagliata 1440x2240) | 423x658 |
| firma, gradini in frassino | `2026/04/pantografo-legno-plus-01.jpg` | 1685x670 | 1095x435 |
| zeta bianca | `2026/05/Immagini-061.jpg` | 2496x1664 (tagliata 2246x1664) | 870x645 |
| zeta antracite | `2026/05/scala-a-giorno.jpg` | 1664x2496 | 535x802 |
| rampa in rovere dall'alto | `2026/05/immagini-059.jpg` | 2496x1664 (tagliata 2060x1000) | 1320x641 |

Trovati e non usati: l'originale di `montreal-012.jpg` (3422x2288, il divano rosso domina), `IMG_20260120_162208.jpg` (6528x4896, scala a zeta con la carta da parati fotografica e gli armadi), `Toronto0012.jpg` (2496x1664, pareti gialle e cotto). Le circa 75 immagini con i segni dell'IA restano fuori.

Mappa: tasselli OpenStreetMap (ODbL, attribuzione in pagina) in un tono solo, con la statale 11 ripassata nel tratto di via Marco Polo; nessuno spillo, perché il civico 2 non è sulla mappa.

## Prove (sezione 6)

- 390, 768, 1024, 1440, 1920, con e senza "riduci movimento": nessuno scorrimento orizzontale, nessun errore di script o di rete.
- "Riduci movimento": stesso testo (5.112 caratteri a 1440), nessun elemento nascosto, botola aperta e ferma.
- Peso al primo caricamento: 375 KB a 1440, 343 KB a 390.
- CLS: al massimo 0,0002, anche con la sezione fissata.
- Video: 0 errori a 1440 e a 390.

## Foto da rifare (materiale per il servizio fotografico)

Le foto pesano per circa metà della distanza da un 9: tutte quelle in pagina sono scatti di telefono o di vecchie fotocamere in casa dei clienti.
1. **La botola dall'alto**, come `elementilegno.jpg` ma con la PLUS bianca e i gradini in frassino, dal cavalletto sopra il foro, ottica 35 mm, almeno 4000 px: oggi sul parquet ci sono un avvitatore e la scarpa di chi monta, e il telaio ha una dominante azzurra. Servirebbe anche lo stesso punto con la botola chiusa (il pannello bianco da 18 mm): il gesto d'apertura diventerebbe una foto vera.
2. **Macro dei gradini in frassino spazzolato** sul pantografo bianco, luce radente: `pantografo-legno-plus-01.jpg` è morbida al 100% e su retina (è la prova della firma).
3. **La motorizzata aperta su un muro bianco**, senza la cassapanca e i fiori, con il motore leggibile.
4. **Scale a giorno posate, casa sgombra, luce di finestra**, almeno 3000 px: la zeta bianca di `Immagini-061.jpg` ha lo stipite scuro a sinistra e la finestra bruciata; la zeta antracite ha libreria e oggetti dietro. Una per modello (Montreal, Toronto, New York, Boston), con comune e anno.
5. **Elicoidale, chiocciola Londra o Parigi, parapetto in vetro**: oggi non c'è una foto vera e grande di nessuna.
6. **Showroom e magazzino di Mestrino** (facciata sulla statale 11, scaffali in pronta consegna, la persona dell'ufficio tecnico): non ce n'è nessuna.

## Problemi aperti

- Diritti: `elementilegno.jpg`, `pantografo-legno-plus-01.jpg` e `motorizzata3.jpg` sono sul loro sito ma potrebbero essere del fornitore; le scale da interno sono in case di clienti. Da chiedere.
- Le didascalie delle foto da interno descrivono quello che si vede (struttura a zeta, pedate scure, ventaglio): il nome del modello (New York?) va confermato prima di scriverlo.
- Prezzi (Easy da 238 euro, PLUS da 320, IVA esclusa) letti nel negozio: vanno riletti alla pubblicazione.
- Orario del sabato: in pagina solo "il sabato solo al mattino", come sul loro sito.
- Il modulo prepara un'email (come nella versione di oggi): va collegato a un invio vero con il caricamento delle foto del foro.
- Logo: in testata il marchio a triangolo in SVG (tracciato dal PNG) nel quadrato giallo, con "Scalarredo" composto in Ranade; serve il vettoriale e il nome del carattere della loro scritta.
- Ranade ha lo spazio indivisibile largo il doppio: numero e unità sono tenuti insieme da uno `span` senza a capo.
- Nel video la prima riga di fotogrammi mostra quattro volte la botola chiusa: è l'attesa iniziale di `registra.mjs`, non un blocco della pagina.

## Voto

Il mio: 8,1 (design 8, creatività 8,5, usabilità 8, contenuto 8). Con lo scarto medio dei piloti (0,7) mi aspetto dal giudice circa 7,4. Quello che manca per l'8 sta quasi tutto nelle foto (punti 1, 2 e 4 sopra).
