# Scalarredo, home HE: nota

Pagina: `../../sito-he/index.html` (kit in `sito-he/kit/`, caratteri e immagini in locale). Direzione: `../../DIREZIONE-HE.md`. Ottavo pilota del sistema HE, 7/11/2026, con il giro di ritocco dopo il primo giudizio (7,0). Non pubblicata, azienda non contattata.

## L'idea

La pagina è un soffitto bianco con una botola. In prima schermata il pannello chiuso è disegnato da un filetto e lascia vedere solo una fessura con i gradini; scorrendo la botola si apre e si vede la scala retrattile dall'alto, con "Scale" e "a botola" ai due lati in New Title. Poi la pagina scende come una scala: tre pedate in frassino per le retrattili, la firma "Una vera scala da interno" (la frase loro sulla PLUS con i gradini in frassino da 14 cm), le scale per interno su misura, il modulo, lo showroom e magazzino di Mestrino con il telefono su tutta la riga.

## Ritocco dopo il giudizio (7,0)

Il giudice: sopra la piega un produttore, sotto (prezzi, corrieri, "negozio") un rivenditore. Fatto, in ordine:
1. **Apertura**: `elementilegno.jpg` tagliata a x 331-1690, y 700-2376 (1359x1676, rapporto 0,811 come il vano). Il taglio proposto (x 273-1747, y 673-2491) guardato al 100% teneva ancora il fondo della borsa nera accanto all'avvitatore (fino a y 687) e, in basso, la fessura sbrecciata sotto la cornice e l'intonaco (da y 2382): l'ho stretto di poco, stesso rapporto. Avvitatore, scarpa e intonaco non sono più nel file, quindi restano fuori a tutte le larghezze, all'inizio, alla fine del gesto e con "riduci movimento". `width`/`height` 1359x1676, `aspect-ratio` 1359/1676 sul telefono.
2. **Firma**: frassino tagliato a x 340-1345 (1005x670). A 600 px su retina simulato (densità 2) la foto era ingrandita 1,19 volte e più morbida del testo accanto: è a `min(500px,100%)`, la misura nativa a densità 2.
3. **Retrattili**: `h2` a `clamp(30px,2.9vw,44px)` (anche `.int-testo h2`); tolto il paragrafo dei prezzi scontati, resta il link "Misure e prezzi nel negozio"; `.pedata{min-height:0}`; la motorizzata tagliata stretta su scala e motore (1060x1420), senza cassapanca e fiori.
4. **Su misura**: tolta la zeta antracite con la libreria; sotto la rampa `.modelli` nelle colonne 1-6 e `.altre` ridotto a una frase con i quattro link nelle colonne 8-12.
5. **Telefono e tono**: sotto i 900 px titolo, che cosa fanno (con le scale per interno), foto, indirizzo; la citazione è nascosta. Titolo dello showroom "Showroom e magazzino a Mestrino, sulla statale 11" (scaleabotola.com/contatti: "a Mestrino, sulla statale per Vicenza ha un ampio showrom ed un fornito magazzino"; scalarredo.it/contatti: "SS 11 Padova-Vicenza"). Il grande numero non cambia più colore al passaggio. Tutta la pagina al "voi": via "Vieni a vedere la tua scala nel nostro negozio". Via "team esperto", "scala unica", "preventivo immediato", e anche "esaustiva", "semplice telecomando", "tramite corrieri", "rapidi" nel titolo del modulo: al loro posto frasi più asciutte delle stesse fonti ("possiamo realizzare scale interne su disegno", "consulenza gratuita e senza impegno", "facilmente raggiungibili da Padova, Vicenza o Venezia").

## File

- `foglio-1440.jpg`, `foglio-390.jpg`: i fotogrammi del video (uno al secondo), da `_metodo/highend/kit/registra.mjs`.
- `prima-schermata-1440.jpg`, `prima-schermata-390.jpg`.
- `scorrimento-*.mp4` e `fotogrammi-*` restano fuori da git (si rigenerano).
- Prove, schermate di lavoro, riferimenti e script in `../../_prova/he/` (fuori da git): `prove-finale.json` e `prove-ritocco.json`, `script/immagini.py` (un solo trattamento per tutte le foto), `script/mappa.py`, `riferimenti/`.

## Foto

Originali riscaricati dalla libreria media di scalarredo.it (`/wp-json/wp/v2/media`, 474 voci) il 7/11/2026, anche le versioni senza `-scaled` (sul server sotto `/wordpress/wp-content/uploads/`): 121 file in `assets/originali/wp/`, fuori da git. In pagina, sempre sotto la misura nativa (rapporto peggiore 0,64 a 1440, 0,78 a 1920):

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| botola (apertura) | `2026/05/elementilegno.jpg` | 2020x2491 (tagliata 1359x1676) | 610x752 |
| motorizzata | `2026/05/motorizzata3.jpg` | 1440x2560 (tagliata 1060x1420) | 423x567 |
| firma, gradini in frassino | `2026/04/pantografo-legno-plus-01.jpg` | 1685x670 (tagliata 1005x670) | 500x333 |
| zeta bianca | `2026/05/Immagini-061.jpg` | 2496x1664 (tagliata 2246x1664) | 870x645 |
| rampa in rovere dall'alto | `2026/05/immagini-059.jpg` | 2496x1664 (tagliata 2060x1000) | 1320x641 |

Trovati e non usati: `scala-a-giorno.jpg` (zeta antracite, 1664x2496: libreria e oggetti dietro, uscita nel ritocco), l'originale di `montreal-012.jpg` (3422x2288, il divano rosso domina), `IMG_20260120_162208.jpg` (6528x4896, scala a zeta con la carta da parati fotografica e gli armadi), `Toronto0012.jpg` (2496x1664, pareti gialle e cotto). Le circa 75 immagini con i segni dell'IA restano fuori.

Mappa: tasselli OpenStreetMap (ODbL, attribuzione in pagina) in un tono solo, con la statale 11 ripassata nel tratto di via Marco Polo; nessuno spillo, perché il civico 2 non è sulla mappa.

## Prove (sezione 6), rifatte dopo il ritocco

- 390, 768, 1024, 1440, 1920, con e senza "riduci movimento": nessuno scorrimento orizzontale, nessun errore di script o di rete (`_prova/he/prove-ritocco.json`).
- "Riduci movimento": stesso testo (4.550 caratteri a 1440, 4.371 a 390), nessun elemento nascosto, botola aperta e ferma.
- Peso al primo caricamento: circa 395 KB a 1440, 345 KB a 390.
- CLS: al massimo 0,0001, anche con la sezione fissata.
- Video: 0 errori a 1440 e a 390. Retina simulato (densità 2): fine del gesto e firma alla misura nativa o sotto.

## Foto da rifare (materiale per il servizio fotografico)

Le foto pesano per circa metà della distanza da un 9: tutte quelle in pagina sono scatti di telefono o di vecchie fotocamere in casa dei clienti.
1. **La botola dall'alto**, come `elementilegno.jpg` ma con la PLUS bianca e i gradini in frassino, dal cavalletto sopra il foro, ottica 35 mm, almeno 4000 px: oggi la foto è tagliata stretta per lasciare fuori l'avvitatore, la scarpa di chi monta e l'intonaco rotto, e la cornice bassa ha ancora una dominante azzurra. Servirebbe anche lo stesso punto con la botola chiusa (il pannello bianco da 18 mm): il gesto d'apertura diventerebbe una foto vera.
2. **Macro dei gradini in frassino spazzolato** sul pantografo bianco, luce radente: `pantografo-legno-plus-01.jpg` è morbida anche al 100%, per questo nella firma sta a 500 px (è la prova della firma, e oggi è piccola).
3. **La motorizzata aperta su un muro bianco**, intera fino al pavimento, con il motore leggibile: oggi è tagliata a metà scala per lasciare fuori la cassapanca e i fiori.
4. **Scale a giorno posate, casa sgombra, luce di finestra**, almeno 3000 px: la zeta bianca di `Immagini-061.jpg` ha lo stipite scuro a sinistra e la finestra bruciata; la zeta antracite (uscita dalla pagina) ha libreria e oggetti dietro. Una per modello (Montreal, Toronto, New York, Boston), con comune e anno.
5. **Elicoidale, chiocciola Londra o Parigi, parapetto in vetro**: oggi non c'è una foto vera e grande di nessuna.
6. **Showroom e magazzino di Mestrino** (facciata sulla statale 11, scaffali in pronta consegna, la persona dell'ufficio tecnico): non ce n'è nessuna.

## Problemi aperti

- Diritti: `elementilegno.jpg`, `pantografo-legno-plus-01.jpg` e `motorizzata3.jpg` sono sul loro sito ma potrebbero essere del fornitore; le scale da interno sono in case di clienti. Da chiedere.
- Le didascalie delle foto da interno descrivono quello che si vede (struttura a zeta, pedate scure, ventaglio): il nome del modello (New York?) va confermato prima di scriverlo.
- Prezzi: in pagina non ce ne sono più (238 e 320 euro erano prezzi scontati, listino 290 e 450); resta il link al negozio.
- Orario del sabato: in pagina solo "il sabato solo al mattino", come sul loro sito.
- Il modulo prepara un'email (come nella versione di oggi): va collegato a un invio vero con il caricamento delle foto del foro.
- Logo: in testata il marchio a triangolo in SVG (tracciato dal PNG) nel quadrato giallo, con "Scalarredo" composto in Ranade; serve il vettoriale e il nome del carattere della loro scritta.
- Ranade ha lo spazio indivisibile largo il doppio: numero e unità sono tenuti insieme da uno `span` senza a capo.
- Nel video la prima riga di fotogrammi mostra quattro volte la botola chiusa: è l'attesa iniziale di `registra.mjs`, non un blocco della pagina.

## Voto

Primo giro: il mio 8,1, il giudice 7,0 (scarto 1,1). Dopo il ritocco il mio è 8,1 (design 7,5, creatività 8, usabilità 8,5, contenuto 8,5); con lo scarto di questo pilota mi aspetto dal giudice 7,4-7,6. Guardati da estraneo, i fotogrammi a piena misura dicono: la fine del gesto ora è pulita e regge come composizione; la firma ha una prova vera ma piccola (500 px) e morbida per natura; sotto la gamma delle retrattili resta un vuoto di circa 400 px accanto alla motorizzata, che è il sottoscala dello schema a gradini. Quello che manca per l'8 sta nelle foto (punti 1, 2 e 6 sopra): lo showroom non si vede da nessuna parte.
