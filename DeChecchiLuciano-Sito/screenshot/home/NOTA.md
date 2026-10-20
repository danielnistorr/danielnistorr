# Home finale De Checchi Luciano, "La sagoma": nota

Pagina: `sito/index.html` (statica, si apre anche come file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (maschera, immagini, pagina, prova del gesto, screenshot). Altezza compreso il piede: 5766 px a 1440, 5999 a 1024, 7218 a 768, 6583 a 390.

## Idea

Il battiscopa visto di testa, con le sue due misure. La sagoma 82×13 è la cosa che De Checchi ha portato per prima sul mercato rivestita, nel 1988 (`storia-de-checchi`: "la prima a inserire nel mercato la classica sagoma 82×13, rivestita in varie essenze"). In apertura c'è un solo pezzo vero, una loro foto su carta chiara, e una linea: la linea del pavimento. Il titolo ci sta sopra in una riga sola, come il battiscopa, e il taglio del profilo ci arriva da destra con la quota disegnata: 82 mm lungo l'altezza, 13 mm attraverso lo spessore. Più sotto la stessa testa diventa un disegno in sezione, e il disegno si cambia al tocco. Con il nome di un concorrente la pagina non regge: la misura e l'anno sono solo loro.

## Prime due schermate

1. **Apertura** (`home-1440-prima-schermata.jpg`).
   - Testata: logo vero, menu e telefono tutti a sinistra.
   - In alto a sinistra una riga su materiali, luogo e clienti, il bottone "Richiedi il catalogo" e accanto "Oltre 350 pagine, edizione 2023".
   - In basso, a tutta larghezza, la linea del pavimento: filetto da 1 px in inchiostro, dal margine sinistro al bordo destro. Il titolo "Battiscopa e profili" ci sta sopra in una riga sola, SUSE 300 a 140 px (9,72vw fino a 140).
   - Il taglio del battiscopa rivestito, ripulito e posato sulla carta, sta sulla stessa linea ed esce solo a destra. Il riquadro del taglio è largo il 44,8 % della finestra (645 px a 1440, al massimo 860); da 1101 px la foto si vede intera con la sua carta, alla stessa scala, sotto tutta l'apertura.
   - Sotto la linea, la nota "82×13 mm. La sagoma classica…" come una didascalia di tavola.
   - La quota ha filetti da 1,25 px e frecce chiuse, con "82 mm" e "13 mm" in SUSE 400 a cifre tabellari. È in SVG dentro lo stesso riquadro della foto, quindi scala con lei a ogni larghezza; frecce ed etichette hanno tre misure, per restare tra 12 e 16 px a ogni scala.
   - Da 901 a 1100 px: titolo in una riga sopra, testo a sinistra, foto a destra sulla linea.
   - Fino a 900 px: titolo, foto con la linea del pavimento sotto, poi testo e bottone. A 390 il titolo va su due righe; quota, bottone e telefono stanno nella prima schermata.
   - La linea del pavimento torna nel disegno delle sagome, subito sotto (muro e pavimento).
2. **Sagome.**
   - Il disegno è alto 380 px, con contorno da 1,5 px in inchiostro e campitura del legno della foto (#C9A06A al 25 %). Ci sono la linea del muro, la linea del pavimento e l'interruzione a zigzag.
   - A destra: il titolo "Sei sagome, dalla testa quadra al barocco", due righe su Rivestwood ed Essenza e sei tasti su una riga, senza celle. Ogni tasto ha la piccola testa disegnata, il codice in 500 e il nome in 400 grigio.
   - La sagoma scelta ha la testa piena d'inchiostro e la barretta arancio #E84E0E sotto.

Il resto della pagina:
- la fascia Trattline, unica foto a tutta larghezza;
- l'indice delle otto famiglie a righe, con il nome della famiglia, i nomi veri delle linee in SUSE 300 a 34 px e una riga di dato; ogni riga porta alla sua pagina prodotto;
- i due stabilimenti, con la foto vera del reparto a filo del bordo sinistro e il testo a destra;
- la chiusura "Rifinisci con amore", frase delle slide del sito, con il telefono grande, l'email, le due sedi con il link alla mappa, la riga A13 e il fax in piccolo; la foto Woodled24, alla sua misura (al massimo 900 px), arriva al bordo destro con una didascalia;
- il piede con logo, una riga su chi sono, le colonne Prodotti, Azienda, Contatti e Seguici (solo YouTube), la newsletter "Novità, fiere e catalogo" e la riga legale.

## Caratteri e colori

- **SUSE** (René Bieder per il progetto SUSE). Google Fonts, SIL Open Font License 1.1: la licenza è in `sito/fonts/OFL-SUSE.txt`, il file è `sito/fonts/suse-latin.woff2` (asse dei pesi 100-900).
  - Ruoli: una sola famiglia, 300 per i titoli, 400 per il testo, 500 per enfasi, menu e codici.
  - Le cifre sono tabellari di serie (tutte a 600 unità), quindi misure, codici e telefoni stanno in colonna senza monospazio.
  - Perché: è una grotesk larga e sobria, vicina al DIN del logo. I titoli leggeri e grandi su legno sono quelli di Dinesen (riferimento 1 dell'analisi); il registro chiaro sabbia con il prodotto a filo è quello di Garbelotto (riferimento 3). Non è nella lista b e non è usata da altre home della campagna.
- **Colori**: carta #F3F0E8 (fondo; è il colore esatto della carta nella foto d'apertura dopo la compressione WebP, così il bordo della foto non si vede), piede #EAE4DA, inchiostro #1D1D1B (quello del logo), grigio #5B5750 (6,3:1 sulla carta, 5,7:1 sul piede), segnaposto del campo email #625D54. L'arancio del logo #E84E0E compare solo in due punti piccoli: la barretta della sagoma scelta e l'anello del fuoco da tastiera. Il colore vero è quello del legno nelle foto.

## Interazione

Un solo gesto: il selettore delle sagome Q, QC, I, BC, S, B.
- Al clic o al tocco la sezione grande cambia di netto, senza transizione, con il nome e le linee in cui esiste (Rivestwood tutte e sei; Essenza Q, BC e B).
- I tasti sono veri `button` con `aria-pressed`; le frecce, Home e Fine scorrono, il fuoco è visibile.
- L'unica transizione è sul bottone scuro (colore pieno, 0,15 s).
- Nessuna animazione allo scorrere, nessun effetto sul cursore.
- Utilità: sotto i 1100 px il menu si apre con un bottone vero; sotto i 700 px le colonne Prodotti, Azienda e Contatti del piede si aprono a fisarmonica con un vero bottone (`aria-expanded`). Senza JavaScript restano tutte aperte.
- La newsletter controlla email e consenso e non invia nulla.

## Foto, origine e licenza

Tutte le foto della home sono di De Checchi Luciano, prese dal loro sito. Nessuna foto di repertorio, nessuna immagine generata. I diritti sono da confermare (vedi LEGGIMI).
- Apertura: `assets/originali/2017-04_slide_DeChecchi_2.jpg` (slide del sito, 1920x882).
  - Lavorazione: ritaglio con maschera GrabCut rifinita a mano (`finale_maschera.py`), carta piena, ombra ricostruita. La fascia alta della faccia, fuori fuoco, è stata scaldata un poco per togliere la velatura grigio-verde (solo colore). Il triangolino verde nella scanalatura vicino al piede (un pezzo del profilo bianco dietro) è stato tolto.
  - Sotto i 1101 px: il taglio x 880-1920, y 56-882 della sorgente, in 1040, 780 e 560 px. Da 1101 px: la sorgente intera nell'angolo di un foglio di carta piena 2400x1100 (fuori dalla sorgente c'è solo carta), in 2400 e 1800 px. A 1440 con DPR 2 la densità è 1,61 in entrambi i casi (2400 px su 1489 px CSS, il taglio cade sui 645 px del riquadro).
  - L'inventario la segnava come possibile render: va chiesto (LEGGIMI).
- Fascia Trattline: `2017-04_slide_DeChecchi_3.jpg` (1920x882), a 1920, 1440 e 960 px, più il taglio per il telefono. A 1440 è alta 878 px (61vw, al massimo 880), senza ingrandimento.
- Reparto: `2017-05_De_Checchi_Tecnologia_1.jpg` (900x500), tagliata a 830x500 per togliere i fili rossi sul bordo sinistro, su sei colonne a filo del bordo. Sotto gli 860 px non supera gli 830 px.
- Chiusura: `2019-12_woodled_24_DeChecchi_3.jpg` (900x550), a 900 e 640 px, su sei colonne fino al bordo in proporzione 3:2 (676x451 a 1440, 1,33 a DPR 2). È diversa dalla foto subito sopra e non è usata in altre home della campagna.
- Trattamento comune con PIL: neri verso l'inchiostro, bianchi verso la carta, saturazione appena ridotta. Uscita WebP con srcset.
- Le foto Unsplash e Pexels di `assets/esterne/` non sono usate nella versione finale. La fascia dei listelli di Eiermann è stata tolta.

## Ultimo passaggio: cosa è cambiato

Dopo il giudizio cieco (K0 7, K1 7, K6 6, non passava):
- **Apertura rifatta nella composizione**, non solo nell'oggetto: non più titolo a sinistra e oggetto a destra (il gesto di Hambro e Mario Agnoletto), ma il titolo in una riga sola posato sulla linea del pavimento, con il taglio che ci arriva da destra.
- **Foto più nitida**: tavola unica 1040x826 mostrata al massimo a 0,62 px CSS per px; densità 1,61 a 1440 con DPR 2. Fascia alta scaldata, scanalatura ripulita.
- **Quota visibile a ogni larghezza** da 320 a 2560 (prima spariva sotto i 1100 px). "82 mm" e "13 mm" con l'unità; la freccia di 82 finisce sulla linea del pavimento.
- `button, input, select, textarea{font:inherit}`: Menu, Chiudi e campo email ora sono in SUSE.
- Tolta la riga delle quattro date (con le fiere 2025). Il premio Amici della Zip 2010 è passato nella riga Woodled24 dell'indice; il catalogo resta accanto al bottone.
- Stabilimenti e chiusura restano a due colonne fino a 861 px. Sotto, le foto non superano la loro misura (830 e 900 px). A 1024 la pagina scende da 7875 a 5999 px.
- Foto Woodled24 in 3:2 (676x451 a 1440) con didascalia, invece di 676x600 tagliata e ingrandita: da 0,67 a 1,33 di densità a DPR 2. Il giudice proponeva 560 px; ne ho tenuti 676 per non scendere sotto il 35 % di area foto.
- Didascalia delle sagome: "disegno indicativo, 82×13 mm".
- English nel menu aperto sotto i 1100 px.
- Carta della pagina da #F3EFE8 a #F3F0E8, il colore che la carta della foto ha dopo la compressione WebP: il bordo del riquadro non si vede più.
- Area foto riportata sopra il 35 %: foto d'apertura intera da 1101 px (stessa scala, solo carta in più), fascia Trattline alta 878 px a 1440, reparto e Woodled24 su sei colonne.
- La riga d'apertura dice "per chi vende, posa e sceglie pavimenti" (il sito cita "distributore o utente finale").

## Controlli

- `segnali.sh`: 0 soglie bloccanti su 10.
  - Area foto 35,2 % (era 22,7 % con la sola tavola piccola: per questo la foto d'apertura si vede intera da 1101 px, la fascia Trattline è più alta e reparto e Woodled24 stanno su sei colonne), SUSE 100 %, mono 0 %, 11 filetti, nessuna freccia, nessuna etichetta maiuscola, 2 fasce di fondo, 4 misure di H2.
  - Una riga da guardare, "titolo a sinistra e paragrafo a destra": lo strumento conta le colonne del piede (Informazioni sul sito, Prodotti, Azienda); la sola sezione vera è "Due stabilimenti", dove titolo e testo stanno nella stessa colonna accanto alla foto.
- `finale_gesto.mjs` a 1440, 1024, 768, 390 e 320: il selettore cambia al clic e al tocco, risponde alle frecce, `aria-pressed` è giusto, la fisarmonica si apre, nessun errore JavaScript, nessuno scorrimento orizzontale.
- `finale_controlli.mjs` a 20 larghezze da 320 a 2560 (DPR 2): `scrollWidth` uguale a `innerWidth` ovunque; la quota è visibile a ogni larghezza; Menu e campo email in SUSE; il menu aperto a 390 ha Prodotti, Sagome, Lavorazioni, Azienda, Contatti, English; il bottone d'apertura sta nella prima schermata fino a 390x844.
- Collegamenti: `tel:+39049644709`, `mailto:info@dechecchiluciano.com` (e con oggetto per il catalogo), `mailto:` della PEC, due link Google Maps a via Lombardia 13 e via Irpinia 16.
- Guardati a pezzi: 1440 e 390 (pagine intere e prime schermate), 320, 768, 1024 e 1920 a pagina intera, le prime schermate a 1101, 1200, 1920 e 2560. Niente sovrapposizioni: a 1101 la fine del titolo resta a sinistra della quota.
- Contrasto AA su tutti i testi. Nessun carattere U+2014 nella pagina, negli script e nei .md.
- Divieti controllati a occhio: nessun gradiente, badge, card, icona Lucide, corsivo d'accento, emoji, dissolvenza, hover con opacità.
