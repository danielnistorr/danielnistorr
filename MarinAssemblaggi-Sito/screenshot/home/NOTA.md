# Marin Assemblaggi, home finale "Sciolto e montato"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, pagina, screenshot; con `controlli` anche 320, 768, 1024 e 1920, e lo stato "Montato", in `_prova/controlli/`). I controlli di questa nota si ripetono con `node _prova/script/controlli_finali.mjs`. Base: il prototipo A scelto dal giudice, rifinito in due passaggi.

## L'idea

Marin fa la parte che il cliente non vede: il pezzo arriva sciolto ed esce montato. La home lo mostra con la loro foto migliore (`8407`): corpo, bussola e sfera separati accanto agli stessi pezzi con la sfera in sede, sulla carta della pagina, senza riquadro. L'interruttore "Sciolto / Montato" cambia la foto: il gruppo scelto resta pieno, l'altro si schiarisce del 70 % verso la carta. Sul telefono cambia il taglio. Con il nome di un concorrente la pagina non regge: pezzi, misure (6 t, 70×90 mm), frasi e recapiti sono di Marin.

## Cosa è cambiato nell'ultimo passaggio (difetti del giudice cieco)

- **Niente più pallini numerati né legenda numerata** (era il gesto di Bertolin Antonio e di Mario Agnoletto). Sotto ogni gruppo c'è una didascalia di testo a 15 px, allineata al bordo sinistro del gruppo: "Sciolto: corpo, bussola e sfera" e "Montato: la sfera è in sede". Quella dello stato scelto è in inchiostro, l'altra in acciaio.
- **L'interruttore cambia la foto anche sul desktop.** Due WebP della stessa misura (`apertura-sciolto`, `apertura-montato`): il gruppo non scelto è schiarito del 70 % verso #F2F1ED. Si scambiano con `display:none`, senza transizione. Controllo: a 1440, 1024, 768 e 1920 `currentSrc` passa da `apertura-sciolto-880.webp` ad `apertura-montato-880.webp`; a 390 e 320 da `sciolto-440.webp` a `montato-440.webp`. Lo stato è annunciato agli screen reader da una riga `aria-live`.
- **Foto a 1x, mai ingrandite.** La foto d'apertura è larga al massimo 880 px CSS, cioè il taglio originale di 8407 (880x410): `--fw:min(880px,75.8cqw)`. `finale_img.py` ora rifiuta qualsiasi esportazione oltre la sorgente; anche i tappi sono scesi da 1000 a 833 px (la loro misura vera). Da 320 a 2560 nessuna foto ha meno di un pixel vero per pixel CSS, salvo le bussole al telefono tra 601 e 640 px (0,94) e a 1920 (1,2x, la foto sorgente è di 1600). Sugli schermi retina resta 1x: la cura vera è la foto nuova a 6000 px, primo punto del LEGGIMI.
- **Riflesso senza spigoli.** Sotto i piedi dei pezzi il riflesso si spegne in modo lineare dal 100 % allo 0 % su 60 px, uguale per i cinque pezzi, e può solo scurire la carta: la macchia bianca a destra del raccordo e il bordo netto sotto il corpo esagonale e la sfera non ci sono più (controllato su un ritaglio al 200 %).
- **Il banco è stretto a un solo gruppo.** Da `8447` resta solo il gruppo in basso al centro: due bussole con la vite, una bussola, due sfere e tre raccordi, a 1x (665x300). Il cilindro nero, l'innesto grigio, le cartucce e le impugnature con le scritte "250 bar" sono fuori; le ombre grigie del piano sono portate sulla carta. Nessun oggetto tocca i bordi. La figura sta a destra, con la riga "Un reparto solo, a Saonara..." in basso a sinistra, sulla stessa linea della didascalia: è lo stesso schema dell'apertura.
- **Tagli del telefono rifatti** a 440x400: 32 px di carta ai lati del gruppo sciolto, 20-30 px attorno al gruppo montato. A 390 e a 320 nessun pezzo tocca i bordi. Fino a 480 px si usano i tagli; da 481 a 640 la foto larga intera (704 px veri).
- **Nome su due righe** in testata e nel piede: "MARIN" in 500 e, sotto, "ASSEMBLAGGI" in 400 a 0,36 del corpo, spaziato a +0,275em perché sia largo quanto "MARIN" (misurato nel browser con `_prova/script/misura_nome.mjs`). Non è un pittogramma inventato: è la ragione sociale composta. Il logo vero resta il punto 1 delle domande.
- **Due sole misure di H2**: 64 px per i titoli di sezione e della chiusura (52 a 1180, 44 a 900, 34 a 640), 13 px per i titoletti del piede. "Dal montaggio al lotto etichettato" è passato da 44 a 64.
- **I quattro passi sono una riga di quattro colonne**, senza numeri in ottone, titoli a 22 px in 500; restano i due dati "6 t" e "70×90 mm". La sezione Lavorazioni è alta 963 px a 1440 (prima superava i 1500).
- **"Apri la mappa"** non va più a capo (`white-space:nowrap`): una riga a tutte le larghezze provate.
- **"committenti" minuscolo** nella frase della chiusura; il LEGGIMI dice che la frase unisce due periodi del loro "Chi siamo" e va fatta approvare.

## Le prime schermate

- **1440.** Testata con il nome su due righe, tre voci e il telefono. Titolo "Assemblaggi meccanici / di precisione" a 96 px, largo. Sotto, a destra, la foto a 880 px che sale fino alla linea di base della seconda riga; a sinistra, sulla linea delle didascalie, l'interruttore. Sotto, in una riga: "Per conto terzi, a Saonara (PD)..." e "Chiamate lo 049 807 0512".
- **390.** Titolo su tre righe a 43 px, il taglio del gruppo scelto a tutta larghezza (440 px veri su 390), la didascalia, l'interruttore a tutta larghezza e la frase: tutto entro gli 844 px (la frase finisce a 744).

## Chiusura e piede

- **Chiusura "b con foto"**, testo sopra e foto a tutta larghezza sotto: "Precisione e puntualità: i nostri committenti ve lo confermeranno" a 64 px; il telefono a 56 px con `tel:`, l'email con `mailto:`, l'indirizzo con "Apri la mappa", "A poche centinaia di metri dall'uscita di Padova Est" e gli orari; le bussole di `slide2` alte 600 px a 1440 (1x esatto della sorgente 1600x600).
- **Piede**: filetto #CFCCC4; il nome su due righe a 34 px con una riga su chi sono; tre colonne (Lavorazioni con le sei voci vere, Azienda, Contatti), titoletti a 13 px in 500 maiuscolo; riga legale con Marin Assemblaggi S.r.l., P.IVA e C.F. 05025290288, indirizzo, Privacy, Cookie. A 390 le colonne si impilano in ordine.
- **Niente "Seguici"**: Facebook è un link vuoto e Google+ è chiuso.
- **Niente newsletter**: Marin è un terzista B2B senza prodotti propri, cataloghi, fiere o clienti privati, e chi lo cerca telefona.

## Caratteri e colori

- **Zalando Sans** (Google Fonts), una famiglia sola con l'asse della larghezza: largo (125 %) per titoli, nome, telefono e dati; normale per il testo; pesi 400 e 500. Riferimenti: LEMO e Fantini, il largo delle targhette incise delle macchine. Non è nella lista b della guida e non è usato da altre home della campagna.
- **Licenza**: SIL Open Font License 1.1, nome riservato "Zalando" (`sito/fonts/OFL.txt`). Gli woff2 sono quelli di Google Fonts (latin e latin-ext), serviti dalla pagina senza modifiche.
- **Cifre**: proporzionali, con spazi indivisibili tra numero e unità e tra i gruppi del telefono (le tabellari di Zalando Sans hanno l'aspetto di un monospazio, vietato dalla guida).
- **Colori**: carta #F2F1ED (il fondo delle foto da studio), inchiostro #1B1D1F (15,0:1), acciaio #5E646B per didascalie e testo secondario (5,3:1), ottone #7D5F27 solo per i due dati (5,25:1), filetto #CFCCC4, #E4E1D9 per il fondo dei bottoni al passaggio.

## Interazione

- Un solo gesto: l'interruttore. Due bottoni veri con `aria-pressed`, bersaglio di 44-49 px, frecce sinistra e destra, Invio e Spazio. Cambio netto della foto e della didascalia, senza dissolvenza.
- Al passaggio cambia solo il fondo dei due bottoni (120 ms) e il colore dei link.
- Nessuna animazione allo scorrimento, nessun effetto che segue il cursore.
- Fino a 900 px il menu si apre con "Menu" (`aria-expanded`) e si chiude anche con Esc.

## Foto: origine e licenza

- Solo foto di Marin dal loro sito, copyright "KeKKo-clicK" nell'EXIF (diritti da confermare, LEGGIMI): `8407.1600.jpg` (apertura e tagli del telefono), `slide3.jpg` (tappi), `8447.1600.jpg` (il gruppo del banco), `slide2.jpg` (bussole). Nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- Lavorazione in `_prova/script/finale_img.py`: fondo portato sulla carta; piedi dei pezzi segnati a mano; riflesso lineare su 60 px; stati dell'interruttore con il gruppo non scelto schiarito del 70 %; per il banco una sagoma a mano, le parti in acciaio e le facce lucide segnate come ellissi, le ombre del piano sulla carta; esportazione WebP solo a 1x o più piccola, con srcset.

## Controlli (20 ottobre 2026)

- **Altezza**: 4591 px a 1440, 4875 a 390, piede compreso.
- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 640, 641, 768, 900, 901, 1024, 1100, 1101, 1180, 1280, 1440, 1680, 1920 e 2560.
- **Screenshot guardati a pezzi**: 1440 (intera, prima schermata, "Montato", chiusura), 390 (intera, prima schermata, "Montato"), 320, 560, 768, 1024 e 1920.
- **Tastiera**: 7 Tab fino a "Sciolto"; freccia destra porta a "Montato" con il fuoco, freccia sinistra torna; Invio e Spazio funzionano. **Tocco** a 390 (DPR 3): "Montato" e "Sciolto" cambiano taglio e didascalia; il menu si apre e si chiude con Esc.
- **Collegamenti**: `tel:+390498070512`, `mailto:info@marinassemblaggi.it`, la mappa `https://www.google.com/maps/search/?api=1&query=Via+Emilia+Romagna+26+35020+Saonara+PD` (8 collegamenti in tutto tra testata, apertura, chiusura e piede).
- **`segnali.sh`**: 0 cerchi numerati, 0 numerazioni, 0 numeri grandi con etichetta, 0 etichette sopra i titoli, 0 frecce, 8 filetti, Zalando Sans al 100 %, monospazio 0 %, una data (2016). Due voci da dire:
  - area foto 28,8 % contro la soglia del 35 %. È il caso previsto dalla guida per le aziende senza foto grandi (le foto di Marin sono di 1600x600 e i pezzi sono scontornati): con le foto a 1x chieste dal giudice non si sale senza ingrandirle o riempire la pagina. Non è da nascondere: è la prima cosa da chiedere a Marin (LEGGIMI, foto a 6000 px);
  - 2 misure di H2 (64 e 13 px), cioè quello che il giudice chiedeva.
- **Divieti**: nessun U+2014 in pagina, in questa NOTA e nel LEGGIMI; nessuna dissolvenza, nessuna opacità al passaggio, nessuna icona, nessun badge, nessun box con icona, nessun gradiente.
- **Testi**: tutti i dati vengono da `01-analisi.md`. I nomi dei pezzi nelle didascalie sono letti dalla foto e sono tra le cose da confermare.
