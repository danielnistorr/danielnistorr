# Zeta S.r.l., home finale "Cristal": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, collaudo, segnali).

Screenshot in questa cartella: `home-1440.jpg` (5409 px piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6834 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`.

## L'idea

La prima schermata sta dentro una loro busta. La busta trasparente a quattro spazi di Zeta, dritta e grande da margine a margine, è posata sulla pagina: le due saldature fanno la griglia della prima schermata. Il titolo "Trasparente come il vetro" (la loro frase sul PVC cristal) sta nelle due tasche di sopra, sotto il film, e si legge attraverso. Nella tasca in basso a sinistra c'è la riga su cosa fanno, con il bottone e il telefono. Nella tasca in basso a destra c'è il primato che hanno solo loro, il 1994: "buste trasparenti senza aloni azzurrati e senza anelli di Newton", con una didascalia sobria sull'oggetto. In fondo si vede il rinforzo bianco della busta. Coprendo logo e nome, la busta che contiene la pagina e il primato del 1994 restano di Zeta.

## Cosa è cambiato in questo giro

Il committente ha chiesto "più roba di alta gamma, meno uguali tra loro". Il giudice cieco aveva dato K0 6, K1 5, K6 6 e K7 6.

- **Apertura rifatta dentro l'idea "Cristal".** Prima c'era la busta storta a destra, con il titolo a sinistra e una legenda con pallino e filetto. Adesso la busta è a tutta griglia e il contenuto sta nelle tasche, divise dalle saldature vere. È un'impaginazione che non c'è nelle altre home della campagna (controllato sulle copertine di Est Grisignano e Mestrino e sulle prime schermate delle altre home). In tutte le altre il titolo sta accanto all'oggetto o sopra di lui, mai dentro.
- **Niente legende numerate.** Via il pallino con il filetto; resta una sola didascalia ("Nella foto, una nostra busta in PVC a quattro spazi per raccoglitori ad anelli").
- **Il fondo non è più beige.** È il verde del marchio Zeta (#0A6B42) molto schiarito: #D9E7DF per la pagina, #CCDDD3 per il piede, #CFDFD6 per il piano delle foto del selettore. Il motivo si vede: il fondo è quello che sta sotto la busta. Attraverso il film il verde resta verde, e il titolo resta nero, senza aloni. È la loro promessa del 1994, scritta proprio lì accanto.
- **Il primato del 1994 sale nella prima schermata** (K1: prima stava sotto la piega). In Storia il 1994 resta in una riga breve ("Il brevetto del primo albumino fotografico ecologico d'Europa").
- **La busta è rifatta** (`_prova/script/busta_img.py`). Prima era ruotata di 4 gradi; adesso è dritta e la tela è intera, con le posizioni delle saldature misurate e stampate dallo script. Le righe delle saldature e del bordo sono più leggere (prima sembravano disegnate a penna). Il velo è più chiaro. Ci sono due uscite: in verticale per il telefono, ruotata di 90 gradi da 601 px in su.
- **Chiusura cambiata:** frase grande a tutta riga, sotto i recapiti a sinistra e la foto intera del tavolo (1200x500) fino al bordo destro. Prima c'erano testo a sinistra e foto 4:3 a destra, come in Storia: lo zig-zag è sparito. La foto si vede al massimo a 1:1 (909 px a 1440, prima era ingrandita da 667 a 778 px); a 390 è tagliata 4:3 sull'uomo e sulle mani.
- **Spazi:** tolti 96 px morti sotto la busta; anni della Storia a 36 px (prima 44).
- Già fatti nel passaggio precedente e verificati: Colorato con le buste a L (non più il raccoglitore dell'apertura), Opaco con il primo piano della copertina goffrata a 5456 px di origine, riga di Opaco sulla goffratura, "Dove è possibile, i nostri robot", "Dal 2010 studiamo il PLA", "Interna 55" senza a capo, filetto del telefono tolto sotto i 900 px, foto dei Materiali a 768 a tutta larghezza, niente preload dei font (nessun errore CORS da file://).

## Prima schermata

- **1440**: testata leggera (logo vero, quattro voci, telefono). Sotto, la busta da 64 a 1376 px, film da y 104. Titolo a 190 px (13,2 % della busta, General Sans 500) nelle tasche di sopra, appoggiato sulla saldatura lunga, che lo attraversa tra "il" e "vetro". Nelle tasche di sotto: la riga, "Chiedete un preventivo" (mailto) e 049 774299 (tel:) a sinistra, il 1994 e la didascalia a destra. Il rinforzo bianco esce dalla piega.
- **1920**: stessa composizione, titolo a 253 px, CTA a 980 px su 1080.
- **1024 e 768**: busta orizzontale. A 1024 tutto sta nelle tasche; a 768 la riga e il bottone escono sotto la busta, e il 1994 va nella tasca in basso a sinistra.
- **390 e 320**: busta in verticale a tutta larghezza (con il rinforzo a destra) e titolo a due righe nelle tasche di sopra. Il 1994 e la didascalia stanno nelle tasche di sotto; la riga, il bottone e il telefono escono sotto la busta. A 390 il bottone finisce a 803 px su 844.

## Caratteri e colori

- **General Sans** 500 per titoli e linguette, **Switzer** 400 e 500 per testo, numeri, menu e piede. Tutte e due sono di Indian Type Foundry su Fontshare, con la **ITF Free Font License** (uso commerciale gratuito, anche sul web). I tre woff2 li serve la pagina da `sito/fonts/`. Switzer ha le cifre tabellari, che servono per micron, millimetri, date e telefono.
- Colori: pagina #D9E7DF, piede #CCDDD3, inchiostro #14201A, verde Zeta #0A6B42 (bottone, linguetta attiva, anni), note #4E5550. Contrasti: note 6,0:1 sulla pagina e 5,4:1 sul piede, verde sulla pagina 5,1:1, bianco sul bottone 6,6:1.

## Interazione

Un solo gesto: il selettore "Materiale" con tre linguette vere (Colorato, Cristal, Opaco). Cambia di netto la foto, la didascalia, il titoletto e la riga sotto. Funziona con frecce, Home e Fine da tastiera e con il dito. Al passaggio cambia solo il colore; niente animazioni allo scorrere, niente effetti che seguono il cursore.

## Foto: origine e licenza

Tutte foto di Zeta S.r.l. dal loro sito (`assets/originali/`): nessuna foto esterna, nessuna immagine generata dall'IA.

| In pagina | File sorgente | Lavorazione | Larghezze |
|---|---|---|---|
| Apertura | `2019_12_busta-pvc-4-spazi.jpg` (3072x3848) | raddrizzata in prospettiva, specchiata, resa come film con trasparenza (riflessi e saldature presi dalla foto), ombra rifatta; in orizzontale ruotata di 90 gradi | 600-1800 (verticale), 1000-2900 (orizzontale) |
| Materiali, Colorato | `2019_12_cartelline-a-L-fondo-colorato-semirigido.jpg` | scontornate, posate sul piano #CFDFD6 | 700, 1050, 1400 |
| Materiali, Cristal | `2019_12_porta-campioni-1.jpg` (5456 px) | scontornata, posata sul piano #CFDFD6 | 700, 1050, 1400 |
| Materiali, Opaco | `2019_12_couvette-campionario-1.jpg` (5456 px) | primo piano della copertina goffrata | 700, 1050, 1400 |
| Storia | `2023_02_LAVORAZIONE-PLASTICA-RICICLATA.jpg` (1024 px) | curva leggera | 640, 1024 |
| Chiusura | `2023_02_BUSTE-PVC-SU-MISURA.jpg` (1200x500) | intera, curva leggera e tono caldo | 800, 1200 |
| Logo | `logo-zeta-2268x1098.png` | ritagliato, WebP a 1x e 2x | 300, 600 |

## Il piede

Il logo vero e una riga su chi sono. Poi le colonne Azienda, Prodotti (sette categorie vere), Contatti (tel:, mailto:, mappa, orari), Seguici (solo LinkedIn) e Lingua (i quattro domini esteri). In fondo ZETA S.r.l., l'indirizzo, P.IVA e C.F. 00220030282, il Registro Imprese di Padova, il capitale sociale di 51.480 euro i.v., Privacy e Cookie. A 390 le colonne si impilano in ordine.

**Niente newsletter**: Zeta lavora su commessa per aziende e non ha notizie (la pagina news è vuota), fiere, cataloghi scaricabili o collezioni. LinkedIn basta.

## Controlli (2 novembre)

- Screenshot guardati a pezzi a 1440 e 390, più 320, 768, 1024 e 1920. Nessun testo sovrapposto né fuori finestra (collaudo `_prova/script/collaudo.mjs`; l'unico "fuori" è il link nascosto "Vai al contenuto").
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 768, 900, 1024, 1200, 1280, 1366, 1440, 1680, 1920 e 2560.
- Linguette provate con il clic, con la freccia destra e con Home (aria-selected e il fuoco si spostano) e con il tocco a 390. Il menu del telefono si apre e si chiude con Esc.
- Collegamenti: `tel:+39049774299`, `mailto:info@zetaitaly.com` (anche con l'oggetto "Richiesta di preventivo"), mappa Google su Viale della Navigazione Interna 55, 35129 Padova.
- Altezza a 1440: 5409 px, piede compreso.
- Nessun carattere U+2014 nella pagina, in questa nota e nel LEGGIMI.
- Segnali da IA (`segnali.sh`): 18 soglie su 18 OK. L'area delle foto è al 35,1 %; nessun numero grande con etichetta (anni a 36 px); quattro misure di H2; due famiglie con ruoli fissi; 13 filetti; nessun titolo nero, nessuna etichetta sopra i titoli.
- Nessuno dei divieti del committente: niente gradienti, card, icone, badge, dissolvenze o corsivi d'accento, niente Inter, niente legende con pallino e filetto.
