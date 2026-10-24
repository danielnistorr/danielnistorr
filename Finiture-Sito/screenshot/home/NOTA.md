# Finiture, home finale: "Cosa vuoi verniciare?"

Pagina: `sito/index.html` (si apre con file:///, nessuna risorsa esterna). Immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot, controlli). Base: prototipo A "Appena verniciato", con il piede e il grafico delle barre presi dal prototipo B.

## L'idea

La loro domanda, "Cosa vuoi verniciare?", è il titolo della pagina, e le quattro risposte (Finestre, Porte, CLT, Sedie e mobili) sono l'unico gesto. Si sceglie il settore e cambia subito il pezzo appena verniciato, appeso alla macchina Finiture: la porta verde laccata con la porta rossa sui ganci del Power&Free, l'anta sotto lo spruzzo con il trasportatore rosso sopra, il pannello CLT sospeso, le sedie arancio sul trasportatore a terra. Sotto la foto, la linea per quel settore e le macchine giuste.
Con il nome di un concorrente la prima schermata non regge: la domanda è quella del loro sito di oggi, le foto sono dei loro impianti, il rosso è quello delle loro macchine.
La pagina resta carta e inchiostro; il colore forte lo portano i pezzi verniciati e il rosso Finiture.

## Prime due schermate

1. **1440x900.** Testata con il logo vero, sei voci, lingue e telefono. "Cosa vuoi verniciare?" su una riga, Archivo largo a 116 px. Sotto, a sinistra (3 colonne su 12), le quattro risposte a 32 px tra filetti sottili, con un punto rosso sulla scelta; in fondo alla colonna, allineate al piede della foto, tre righe su chi sono e il bottone "Prova i tuoi pezzi in area test". A destra (9 colonne) la foto del settore, 978x643, intera dentro la prima schermata (finisce a 897 px). Porte è la scelta iniziale: è la foto più forte (7/8) e mostra insieme il prodotto e la loro macchina.
   **390x844.** Titolo su due righe a 46 px, le tre righe e il bottone, le quattro risposte su una riga sola (anche a 320), poi la foto quadrata a tutta larghezza, che finisce a 819 px.
2. Sotto la foto: una riga di didascalia, poi a sinistra la linea per il settore (titolo, testo, materiali o caso cliente, link alla pagina del settore) e a destra le macchine in una griglia a due colonne: due macchine riempiono una riga, quattro fanno due righe, senza mezze righe vuote.

Poi: area test (foto della cabina con il tecnico a tutta larghezza, testo sotto in una colonna sulla quarta colonna della griglia, lo stesso asse della foto d'apertura); "Quattro linee consegnate, barra per barra", con i fatti dell'azienda in una frase sola e il grafico delle barre; chiusura "b con foto"; piede.

Misure (piede compreso): 1440: 4967 px; 390: 5215 px; 320: 5333 px; 768: 5405 px; 1024: 4849 px; 1920: 5233 px; 2560: 5527 px.

## Caratteri

- **Archivo** (Omnibus-Type), una sola famiglia variabile in peso (100-900) e larghezza (62-125 %). Licenza **SIL Open Font License 1.1**, uso commerciale libero; file e licenza in `sito/fonts/` (`archivo-latin.woff2`, `archivo-latin-ext.woff2`, `OFL-Archivo.txt`), scaricati da Google Fonts e serviti dalla pagina.
- Titoli a larghezza 106-110 % e peso 420-440, interlinea 0,96, spaziatura -0,036em: l'espanso richiama il Rogue Sans Ext del loro marchio. Testo a 100 %, 17-18 px, interlinea 1,5-1,55. Cifre tabellari per barre, millimetri, telefono e orari.
- Riferimenti per la scelta: Biesse (un oggetto e una parola grande), Dürr (Barlow leggero e numeri veri). Nessun monospazio.

## Colori

Carta #F4F3F0, cemento #E7E6E2 (piede), inchiostro #1C1C1A, grigio testo #5C5C58, filetti #D3D0C9, rosso Finiture #A51329 solo sulla scelta attiva, al passaggio, sull'anello del fuoco, sulla rotaia del grafico e sui messaggi d'errore della newsletter. Contrasti: grigio su carta 6,05:1, grigio su cemento 5,38:1, risposte non scelte #6E6D68 su carta 4,67:1, segnaposto del campo email #63625E su cemento 4,89:1, inchiostro su cemento 13,7:1, rosso su carta 6,9:1, rosso su cemento 6,2:1. Tutti AA.

## Interazione

Un solo gesto: le quattro schede (role tab, verticali sopra i 1060 px e orizzontali sotto, con aria-orientation aggiornato; frecce su, giù, destra e sinistra, Inizio e Fine, un solo tabindex attivo). Il cambio è secco, senza animazioni. Transizioni di 120 ms solo sul colore di schede, link e bottoni. A 390 il piede si apre a fisarmonica con veri bottoni. Menu a bottone sotto i 1060 px. Newsletter: con il campo vuoto o sbagliato, o senza consenso, compare un messaggio (role status, aria-live) e il fuoco torna sul campo; a modulo completo dice che è dimostrativo e che va collegato a un servizio. Niente comparse allo scorrere, niente effetti sul cursore.

## Foto: origine e licenza

Tutte di Finiture (finiture.it, `Portals/0`, scaricate in `assets/originali/`): nessuna foto di repertorio, nessuna immagine generata. L'uso va confermato con l'azienda (LEGGIMI). Trattamento comune con PIL: un filo di contrasto (1,02-1,04) e di colore (1,02), WebP in più larghezze con srcset; taglio largo 1,52:1 e quadrato per il telefono.

| Uso | File di partenza | Voto | Pixel della foto per pixel di schermo a 1440 |
|---|---|---|---|
| Porte (apertura) | `EasyGalleryImages_1_17_Porte_3-taglio-dx_R01.jpg`, intera, non scontornata | 7/8 | 1,96 |
| Finestre | `EasyGalleryImages_1_16_Finestre_12_R01.jpg` | 5/4 nell'inventario automatico; guardata: nitida, con lo spruzzo e il trasportatore rosso, la tengo a 6 | 1,47 |
| CLT | `easygalleryimages_1_18_clt_1_taglio-dx-e-no-acqua_r01.jpg` | 6/6 | 1,96 |
| Sedie e mobili | `easygalleryimages_1_19_sedie_1_r01.jpg` | 7/7 | 1,96 |
| Area test | `easygalleryimages_1_1092_cabina-robot.jpg` | 6/4 | 1,67 |
| Chiusura | `EasyGalleryImages_1_82_Birotaia-dettaglio_2.jpg` | 6/6 | 1,39 |
| Macchine | render CAD `EasyDNNnews_19/24/25/27/30/34/35_*` | 6/3 | mai ingranditi (scala 0,27-0,55) |
| Logo | `logo-finiture-da-youtube-ritagliato.png` | | PNG a 300 e 400 px (2x) |

Render: fondo portato a bianco, composti su bianco e moltiplicati per il colore della carta, salvati in WebP senza perdita. Il pixel d'angolo di ogni file è esattamente #F4F3F0, niente più rettangoli chiari.

## Cosa è cambiato in questo passaggio (giudizio cieco del 24/10)

- **Apertura rifatta dentro la stessa idea** (bloccanti K1, K6, K7). Via la lastra verde ritagliata, ruotata di 1,6° con l'ombra, e le tre legende a punto e filetto. Al loro posto la domanda "Cosa vuoi verniciare?" come titolo e le quattro risposte come schede: l'apertura e il gesto sono diventati una cosa sola, come suggerito dal giudice. La foto è intera e mostra il pezzo appeso alla macchina Finiture (gancio, rotaia o trasportatore rosso in tutte e quattro). Composizione nuova: titolo a tutta larghezza in alto, indice delle risposte a sinistra, foto a destra; non è più lo schema di Hambro e Mario Agnoletto.
- **1024**: il testo non tocca più la foto. Fino a 1060 px l'apertura si impila; sopra, tra la colonna di testo e la foto ci sono 48 px a tutte le larghezze (controllo con i rettangoli degli elementi).
- **390 e 320**: le quattro schede stanno su una riga sola (stesso top a 320, 360, 390, 414).
- **Render CAD**: fondo esatto, nessun ingrandimento oltre 1:1, altezza utile più grande.
- **Pannello Sedie e mobili**: le macchine stanno in una griglia a due colonne, quindi due macchine riempiono la riga.
- **Finestre e Porte**: Finestre usa una foto nitida (anta sotto lo spruzzo); Porte usa la porta verde intera al posto della foto con i bianchi bruciati. Nessuna foto è mostrata sotto 1,39 pixel d'origine per pixel di schermo a 1440.
- **Area test e numeri**: tolta la riga dei tre numeri e tolto lo schema titolo a sinistra e testo a destra; i fatti (anni '50, Mizar, Giovanni Sedino, 90% export, quattro lingue, Exporter of the Year 2024) sono una frase sola sopra il grafico delle barre. La foto dell'area test è a tutta larghezza con il testo sotto in una colonna (il giudice proponeva 2/3 della larghezza: con 2/3 l'area coperta da foto scendeva al 25 %, sotto la soglia del 35 %).
- **Newsletter**: messaggi di controllo e di esito, provati con Playwright.
- **Chiusura**: foto più larga (54 %) e più alta; frase in alto e recapiti allineati al piede della foto.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti su 10, 0 da guardare su 8. Area coperta da foto 35 % (soglia 35 %), Archivo 100 %, monospazio 0, 9 filetti, 0 frecce, 0 numerazioni, 0 sezioni con titolo a sinistra e testo a destra, 0 etichette sopra i titoli.
- `finale_controlli.mjs`: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 560, 600, 768, 860, 900, 1024, 1100, 1240, 1280, 1366, 1440, 1600, 1920 e 2560; titolo dentro la griglia a tutte le larghezze; schede su una riga sotto i 1060 px.
- Tastiera: Tab arriva alla scheda attiva (Porte); freccia giù porta a CLT e poi a Sedie e mobili, Fine all'ultima, freccia destra dall'ultima torna a Finestre, Inizio alla prima; tabindex 0 solo sulla scheda scelta; anello del fuoco rosso su tutto ciò che si tocca; link "Vai al contenuto". Tocco a 390: CLT, Sedie e mobili e Finestre si aprono al tocco, aria-orientation orizzontale.
- Newsletter: Iscriviti a vuoto mostra "Scrivi un indirizzo email valido." con il fuoco sul campo; senza consenso il messaggio sul consenso; completo il messaggio dimostrativo.
- Collegamenti: `tel:+390498792458`, `mailto:info@finiture.it` (anche con oggetto "Prova in area test"), indirizzo verso `https://goo.gl/maps/h7pm1kBKtmKQNUDn8`; nessuna ancora rotta.
- Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440 e 1920, più le schede Finestre, CLT e Sedie e mobili a 1440 e a 390 e il menu aperto a 390.
- Nessun carattere U+2014 nella pagina, negli script e nei .md (controllo in `build_finale.sh`).
- Dati: ogni fatto in pagina viene da `01-analisi.md` e dal crawl; nessun dato nuovo in questo passaggio.
