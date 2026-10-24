# Home finale Negrizzolo, "Il cassone rosso": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot, collaudo); `bash _prova/script/build_finale.sh solo-pagina` rifà solo pagina, screenshot e collaudo. Base: prototipo A, con le indicazioni dei due giudizi.

## Idea

Un loro rimorchio rosso, intero, posato su carta chiara su una linea di terra sottile. La stessa linea regge tutte le macchine della pagina: il dumper dell'apertura, le tre sagome delle portate, la vasca inox. Il titolo in Archivo stretto fa rima con le lettere "NE GRI ZZO LO" del cassone e con la scritta condensata del logo. Sotto la linea, nella prima schermata, le loro undici portate a listino: con il nome di un concorrente la pagina non regge.

## Le prime due schermate

1. **Apertura (1440x900)**. Testata con il logo SVG, sei voci e il telefono. Prima l'oggetto: il dumper intero, centrato, largo 1000 px (mai più della sua tela, che è di 1027 px), con la sua ombra sulla linea di terra che va da margine a margine; in alto a sinistra la didascalia "Rimorchio ribaltabile dumper, due assi". Sotto la linea, in una riga sola, il titolo "Rimorchi, carribotte e vasche inox" a 88 px e a destra il bottone "Chiama 0444 614515". Ancora sotto, a sinistra la frase di chi-siamo ("Dagli anni '50 a Grisignano di Zocco, i primi in Veneto a costruire cisterne e carribotte"), a destra la riga "Portate a listino, in quintali: 20 28 30 35 40 50 60 100 120 140 200 q": ogni cifra sceglie quella portata nel selettore e ci porta. Tutto finisce a y 779.
   A 390: il dumper a tutta larghezza utile sulla linea, il titolo su due righe, il bottone, la frase; la riga delle portate si nasconde sotto i 900 px perché il selettore è già nella prima schermata (titolo "Da 20 a 200 quintali" a y 600). Sotto i 960 px c'è un vero bottone "Menu" (aria-expanded, Esc chiude).
2. **Da 20 a 200 quintali**. Una riga di 11 cifre tabellari (le portate delle tre tabelle del sito), la scelta in inchiostro con un trattino rosso sotto, le altre in grigio #5E5F62. Si parte da 140 q, l'unica portata con tutte e tre le colonne piene. Sotto, tre colonne con le sagome dei loro ribaltabile, fisso e carrobotte sulla stessa linea di terra e per ciascuna i modelli di quella portata (al massimo 4 righe, soli filetti orizzontali, poi "Altri N modelli ... nella pagina dei ..."). Dove una portata non ha modelli a listino, la colonna dice "Da 100 q nessuno a listino. Il più vicino: 120 q" e mostra i modelli della portata più vicina; "120 q" è un bottone che la sceglie. In fondo i link alle applicazioni speciali.

Poi: "Vasche inox per uva, anche sul vostro rimorchio" con la vasca sulla linea di terra (dopo un filetto, senza fascia di foto); "Riparazioni di qualsiasi marca" (con "Magazzino ricambi" in fondo alla colonna) e "Taglio laser e carpenteria per conto terzi" con gli otto materiali, due colonne che finiscono alla stessa altezza; "Una famiglia che lavora il ferro dall'Ottocento" con la foto d'archivio alla sua misura (288 px) e le due superfici; la chiusura con la sede; il piede.

Altezza a 1440: 4834 px compreso il piede (prima 5408), uguale per tutte le 11 portate. A 390: 6933 px, uguale per tutte le portate.

## Cosa è cambiato in questo giro (giudizio cieco 60/80)

- **Apertura rifatta dentro la stessa idea** (era lo schema di FM Sistemi e Berto: titolo enorme in alto a sinistra, colonna frase più bottone in alto a destra, oggetto che esce dal bordo): ora oggetto intero centrato in alto, titolo e telefono in una riga sotto la linea di terra, frase e portate nella riga sotto. Messa accanto alle prime schermate di FM Sistemi e Berto Guerrino, la composizione è diversa a colpo d'occhio.
- **Le portate nella prima schermata**: la riga delle 11 portate sceglie la portata nel selettore e ci porta (clic, Invio, dito); senza JavaScript resta un'ancora a #portata.
- **Dumper ripulito e intero**: maschera rifatta in `finale_img.py` (`dumper_alpha`): il fronte del cassone preso dal solo rosso, così il bordo inclinato è netto; tolti braccio e telo arrotolato sopra il bordo, che lasciavano l'alone grigio-azzurro; alfa netta su ruote e telaio davanti; tolti trattore, timone e cavi. Esportato a 760 e 1000 px: niente più file ingranditi (via il 1100 e il 1500), resa massima 1000 px CSS. Controllato a densità 2 (`_prova/script/finale_prova.mjs`, ritaglio della metà destra): nessun alone.
- **Chiusura**: al posto del rimorchio blu tagliato, la sede con l'insegna NEGRIZZOLO al tramonto e un loro rimorchio rosso a tre assi con la vasca inox, intero dal paraurti al timone. Riquadro fisso 6:5 sopra i 900 px (a 390 la foto intera, 10:7), così il taglio è lo stesso a ogni larghezza: a 1440 e a 1024 nessun pezzo di rimorchio tagliato.
- **Via la fascia dell'uva** (Unsplash): la sezione vasche resta titolo, testo e vasca sulla linea di terra.
- **Selettore**: si parte da 140 q; stato vuoto con la portata più vicina cliccabile; altezza delle tabelle fissata via script alla più alta tra tutte le portate (ricalcolata al cambio di larghezza e quando arrivano i caratteri): l'altezza della pagina non cambia più.
- **Officina**: frase del laser riscritta ("Dal pezzo singolo alla grande serie. Pezzi singoli e piccole serie in otto ore lavorative, poi piegatura, cesoiatura, saldatura e montaggio."); colonna Riparazioni con "Magazzino ricambi, veloce ed efficiente, per un fermo macchina ridotto al minimo" (parole del sito) in fondo: le due colonne finiscono alla stessa riga.
- **Storia**: "dall'Ottocento" al posto di "dal 1800" (la fonte dice "già nel lontano 1800"); foto d'archivio solo a 288 px, anche a 390; tolto il file ingrandito.
- **Testata**: menu in riga fino a 961 px (a 1024 sei voci e telefono, senza bottone).
- **Piede**: tra 901 e 1180 px il blocco del logo occupa una riga e le quattro colonne stanno sotto, nessuna voce su due righe a 1024; a 390 link alti almeno 41 px. "Seguici" diventa "Video: YouTube, 4 video" (il canale è fermo da circa 15 anni).
- **Console pulita** anche da file://: tolto il preload del carattere.

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt`), un solo file variabile servito dalla pagina (`Archivo-var-latin.woff2` e `-latin-ext.woff2`, assi larghezza 62-125 % e peso 100-900). Titoli a larghezza 74 % e peso 600-620, spaziatura da -0,016 a -0,024em, interlinea 0,9-0,98; testo a larghezza 100 %, 400, 17-18 px, interlinea 1,55; cifre tabellari per portate, misure, hl, telefono. Motivo: il grottesco stretto e nero delle lettere sui cassoni e del logo. Riferimenti: Krampe per il titolo condensato grande e il colore del marchio solo sul bottone; Väderstad e CLAAS per un'immagine, un titolo e aria; Zunhammer per il prodotto come figura grafica.
- Colori: carta #F4F2EE, piede #ECE9E3, inchiostro #1B1C1E (15,3:1 sulla carta), grigio #5E5F62 (5,7:1), link del piede #3A3B3E (9,2:1 sul fondo del piede), linea di terra inchiostro al 42 %. Rosso cassone #C41A22 solo su bottone, trattino della portata scelta e passaggio sui link (bianco sul rosso 6:1); al passaggio sul bottone il pieno diventa #9E141B, nessuna opacità.

## Interazione

Un solo gesto: le portate. Nel selettore, clic o dito su una cifra: le tre tabelle mostrano subito i modelli di quella portata, senza animazioni. Tastiera: gruppo di radio (role radiogroup, aria-checked), frecce, Home e Fine; le tabelle sono regioni aria-live; il bottone "il più vicino" porta il fuoco sulla portata scelta. Nell'apertura le stesse portate sono link che scelgono e portano al selettore. Transizioni di 0,12-0,15 s solo sul colore di ciò che si tocca; nessuna dissolvenza allo scorrere, nessun effetto sul cursore; con "riduci movimento" le transizioni si spengono.

## Foto, origine e licenza

- `dumper-*.webp`: `assets/originali/images_rimorchi-ribaltabili_e.jpg` (sito Negrizzolo, 1000x700), maschera ISNet (`isnet-general-use`, separa la figura dal fondo e non genera pixel) corretta a mano come sopra, bordi ripuliti dal colore del cielo, nitidezza leggera, ombra a terra disegnata con PIL.
- `ribaltabile-*`, `fisso-*`, `carrobotte-*`, `vasca-*`: `images_rimorchi-ribaltabili_q.jpg`, `images_rimorchi-fissi_n.jpg`, `images_carribotte_6.jpg`, `images_vasche-inox_9.jpg` (sito Negrizzolo), stesso trattamento.
- `sede-*.jpg` (chiusura): `images_vasche-inox_1.jpg` (sito Negrizzolo, 1000x700), non ritoccata, solo il trattamento comune; esportata a 720 e 1000 px, mai oltre la sua misura.
- `archivio-288.jpg`: `images_foto-antica.jpg` (miniatura 300x197), in bianco e nero, alla sua misura.
- `logo.svg`: ricostruito dall'immagine di condivisione `images_og-negrizzolo.png` (contorni ingranditi 8 volte e vettorializzati).
- Nessuna foto di repertorio nella home finale, nessuna immagine generata dall'IA, nessun marchio concorrente in vista.

## Piede

Logo SVG, una riga su chi sono, telefono ed email; colonne Prodotti (cinque pagine), Officina (Riparazioni e ricambi, Taglio laser e carpenteria, Usato), Azienda (Chi siamo, Contatti e orari, Come arrivare), Video (YouTube, l'unico canale che esiste); riga legale con ragione sociale, P.IVA e C.F., REA, Privacy, Cookie. Capitale sociale non indicato (sas, non pubblico). **Niente newsletter**: non pubblicano notizie, cataloghi o fiere e i clienti sono aziende agricole che telefonano (01-analisi.md, sez. 8).

## Controlli (24/10/2026, dopo il giudizio)

- Screenshot in questa cartella, guardati a pezzi a 1440 e 390; prime schermate guardate anche a 320, 768, 1024 e 1920: nessuna sovrapposizione, nessun taglio.
- `_prova/script/finale_prova.mjs` (lanciato dal build):
  - console vuota a 1440 e 390 aperta da file://;
  - altezza a 1440 uguale per le 11 portate (4834 px), a 390 uguale (6933 px); ogni colonna mostra sempre almeno una riga (o quelle della portata più vicina);
  - tastiera: due frecce a sinistra da 140 portano a 100, Invio sul "più vicino" sceglie 120 con il fuoco su 120, Home 20, Fine 200; portate dell'apertura con clic e con Invio;
  - dito a 390: menu che si apre e si chiude (Esc), cifre e "più vicino" toccati;
  - 1024: menu in riga, nessun bottone, nessuna voce del piede su due righe; 390: link del piede alti almeno 41 px, foto d'archivio larga 288 px;
  - scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 900, 960, 1024, 1180, 1280, 1440, 1680, 1920 e 2560;
  - collegamenti: `tel:+390444614515`, `mailto:info@negrizzolo.it`, `mailto:laser@negrizzolo.it`, mappa Google con via Ferramosca 14 Grisignano di Zocco, YouTube.
- Nessun U+2014 in pagina, in questa nota, nel LEGGIMI e negli script. Nessuna richiesta a Google Fonts.
- `segnali.sh`: 16 soglie su 18 a posto. Due righe con una ragione:
  - area foto 22,5 % contro 35 % (bloccante): scesa dal 30 % perché il giudice ha chiesto di togliere la fascia di repertorio dell'uva; le foto vere dell'azienda sono da 1000 px e restano scontorni su carta alla loro misura. La soglia si raggiunge solo con il servizio fotografico del LEGGIMI, non allargando foto morbide o rimettendo repertorio;
  - 11 "numeri grandi": sono le cifre del selettore delle portate, bottoni e non statistiche.
- Segnali da IA a vista: nessun badge, nessuna tripletta di box con icona, nessuna card, nessun gradiente, nessuna dissolvenza, nessuna icona Lucide, nessuna parola da brochure; un solo invito ripetuto (il telefono), un solo carattere.
