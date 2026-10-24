# Nardi, home finale: "Una scatola sola"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (63 file, JPEG e WebP in più larghezze), caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot e controlli con `finale_shots.mjs`, segnali con `_metodo/kit/segnali.sh`).

Screenshot: `home-1440.jpg` (4808 px, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6034 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Guardati a pezzi anche a 320, 768, 1024 e 1920, più gli stati del selettore (Stucchi, Cementi, Ossidi), il menu e la fisarmonica del piede a 390.

## Idea

La scatola Briko Line è l'oggetto più riconoscibile che Nardi ha: il motivo degli attrezzi e un colore per famiglia. La home la mette in scena da sola, grande e scontornata su un fondo color gesso, accanto a un titolo che dice il mestiere, "Stucchi, gessi e malte". A destra, in colonna, i due dati della scatola attiva e le sei famiglie con il colore preso dalle confezioni: un tocco cambia la scatola. Con il nome di Kerakoll la pagina non regge: la scatola, i suoi colori, le sue frasi e il magazzino sono di Nardi.

## Le prime due schermate

1. **Apertura** (1440x900). Testata con il logo vero ricolorato in verde, quattro voci e il telefono a destra. A sinistra il titolo a 130 px, due righe su cosa fanno, dove e da quando, il bottone "I 96 prodotti" e il link "Dove trovarli". Sulle colonne 7-10 la scatola di gesso alabastrino, alta 636 px, con una sola ombra a terra; sotto, la frase stampata sulla scatola e il suo uso. Sulle colonne 11-12, in alto, due dati veri in cifre tabellari ("Inizio presa 15-25 min", "Acqua/gesso 100/140"); in basso, sotto un filetto, le sei famiglie in colonna, ognuna con il suo quadratino di colore che si allunga quando è attiva. Nessun elemento dell'apertura va da margine a margine.
   A 390: titolo su due righe, testo e bottoni sopra la piega, poi la scatola a sinistra con i dati e la colonna delle famiglie accanto, la didascalia ad altezza fissa (tre righe), così le famiglie non si spostano sotto il dito.
2. **Quattro linee, 96 prodotti**. Titolo a 76 px e una frase; la fila di 12 scatole da 1 kg a passo costante, sovrapposte del 20 % solo sul fianco, con cinque etichette di gruppo; tre colonne brevi (Briko Line 43, Artelinea 41, Speciali e altri 12) e, nella stessa sezione sotto un filetto, i sei barattoli degli ossidi alti 120 px.

Poi: una foto a tutta larghezza delle mani con la spatola e lo stucco (segnaposto, senza didascalia: la nota sta nel LEGGIMI); "Dal gesso decorativo alle polveri", con la storia in due paragrafi e la lista dei tempi di inizio presa, dal gesso murario (5-8 min) alla scagliola (60-90 min); la chiusura; il piede.

## Chiusura e piede

- **Chiusura** ("b con foto", testo a sinistra e foto a destra fino al bordo): "Ricostruire, livellare, tappare", la frase stampata sulla scatola dello stucco cementizio, a 76 px; sotto "Prodotti per il privato e per il professionista. Chiamateci per sapere dove trovarli."; il telefono a 52 px con `tel:`, l'email con `mailto:`, l'indirizzo con il link a Google Maps, gli orari. La foto è il magazzino (`IMG_4232`, 4272x2848): taglio stretto sui due bancali di scatole Briko Line, dal traverso alto a quello basso, arancio delle scaffalature spento, sorgente 1752x1165 servita a 720, 1080, 1440 e 1600 px. Didascalia "In magazzino: bancali di scatole Briko Line."
- **Piede**: logo vero (PNG del sito, tagliato sul disegno e ricolorato in #276E59, 436 px per una resa a 146 px, 3x) con una riga su chi sono; quattro colonne Azienda, Prodotti, Gessi, Contatti (telefono, fax, email, indirizzo, orari); riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, Privacy, Cookie, su una riga flessibile che a capo riparte dal margine. Fondo #ECE7DC. A 390 le colonne diventano una fisarmonica: i bottoni con `aria-expanded` si creano solo sotto i 600 px; sopra, i titoli sono testo.
- **Nessuna colonna Seguici**: non esiste un social verificato (l'icona Facebook del sito di oggi punta a "#").
- **Nessuna newsletter**: Nardi non ha notizie, cataloghi sfogliabili, fiere datate o collezioni da annunciare, e chi compra passa dal negozio o ordina per telefono.

## Caratteri e colori

- **Encode Sans**, una sola famiglia variabile (Impallari, Torresi, Le Bailly; Google Fonts, SIL Open Font License 1.1, uso commerciale libero, file ospitati in `sito/fonts/`, sottoinsiemi latin e latin-ext). Stretta (wdth 75) a 500 per titoli, famiglie, dati e nomi; normale a 400 e 600 per testi, menu, bottone e piede. Due misure di titolo, 130 e 76 px; passi verticali 120, 64 e 28 px. Cifre tabellari per telefono, tempi, orari, misure e dati societari. Perché: i nomi dei prodotti sulle scatole Briko Line sono in un grottesco stretto e chiaro.
- **Colori**: fondo gesso #F4F1EA, piede #ECE7DC, inchiostro #1B1A17, testo secondario #57534B (6,8:1 sul fondo), famiglie non attive #6F6A60 (4,8:1, testo grande), filetti #D6CFC1, verde Nardi scurito #276E59 per bottone e link (5,4:1; bianco sul verde 6,1:1). I colori pieni vengono solo dalle confezioni (verde alabastrino #8CAA97, azzurro stucco #6CC2F8, viola malta #7A70B5, giallo cemento #EDD836, arancio colla #D0934B, rosso ossido #C03532).
- **Riferimenti**: Bauwerk Colour (il colore della confezione come materia e nome), Kerakoll (marchio e titolo grandi, poche voci), Farrow & Ball e Mylands per la misura del fondo chiaro.

## Interazione

Un solo gesto: le sei famiglie (Gessi, Stucchi, Malte, Cementi, Colle, Ossidi) sono bottoni veri con `aria-pressed`. Un tocco cambia la scatola protagonista, il testo alternativo, i due dati e la didascalia. Dati dalle schede: alabastrino 15-25 min e 100/140; stucco cementizio strati da 1 a 5 cm e impasto 2 ore; malta pronta grigia tempo di impiego 2 ore e acqua 18 %; cemento rapido 20/100 e almeno 3 MPa a 30 minuti; colla per piastrelle 3-4 kg/m² e pedonabile in 24 ore; ossidi barattolo da 500 g, si mescolano con malte e pitture. Tastiera: Tab arriva ai bottoni, le frecce passano alla famiglia vicina e girano (provato: da Ossidi con la freccia destra si torna a Gessi, con il fuoco). Tocco provato a 390 su tutte e sei le famiglie: la colonna resta ferma (top 548 px in tutti gli stati), la didascalia sempre alta 63 px. Transizioni di 120 ms solo su ciò che si tocca. Niente animazioni allo scorrere, niente effetti sul cursore.

## Foto, origine e licenza

- **Scatole Briko Line da 1 kg** (rendering 1600x1226 del sito): scontornate con un contorno unico, WebP a 522, 680 (nativa) e 784 px. A 1440 la scatola è larga 415 px: sul retina il 784 dà 1,9x.
- **Secchiello e barattoli degli ossidi** (rendering del sito): WebP a 180 e 360 px (fila) e 522 e 812 px (apertura).
- **Magazzino** (`IMG_4232`, foto dell'azienda): vedi Chiusura.
- **Mani con spatola e stucco**: segnaposto esterno, Sasun Bughdaryan su Unsplash (Unsplash License), in `assets/CREDITI.md`; non è usata in nessun'altra home della campagna. Nessuna didascalia in pagina; nel LEGGIMI come va rifatta con un prodotto Nardi.
- **Logo**: `logo-nardi-bianco-500x139.png` del sito, maschera ricolorata. Non ricostruito in SVG: il corsivo è a mano libera e senza il file originale non sarebbe fedele.
- Nessuna immagine generata dall'IA; nessun marchio concorrente.

## Ultimo passaggio: cosa è cambiato dopo il giudice cieco

- Le sei famiglie non sono più una fila a tutta larghezza in basso (il gesto di FM Sistemi): stanno in colonna a destra sotto i due dati, con un quadratino del colore della scatola.
- Scatola protagonista ridotta da circa 800 a 636 px di altezza a 1440 (1,9x sul retina con il 784), una sola ombra a terra, senza drop-shadow.
- Chiusura: via la facciata `TESTATA6` (700 px di sorgente, cassetta delle lettere, lampeggiante, ghiaia); al suo posto il magazzino `IMG_4232`, tagliato stretto sui bancali Briko Line senza il ripiano di sotto, arancio spento, 1600 px per il 768. Titolo "Ricostruire, livellare, tappare" al posto della frase da brochure.
- Tolta la didascalia "Foto indicativa" sotto le mani.
- Ossidi uniti alla sezione delle linee, barattoli a 120 px.
- Riga legale del piede in flex con spazio fisso: a 768 "Privacy" parte dal margine.
- 768: scatola e dati a 32 px di distanza (griglia con `justify-content:start`).
- 390: didascalia ad altezza fissa di tre righe; i bottoni non saltano.
- Stato Ossidi: "Si mescola con malte e pitture" al posto di "Colori 6".
- Piede: i bottoni della fisarmonica esistono solo sotto i 600 px.
- Tolto "1 kg" dalle didascalie di colla e stucco cementizio; tolto il preload del carattere (errore CORS in file://).
- Logo tagliato sul disegno: il corsivo parte esattamente dal margine della griglia in testata e nel piede.

## Controlli

- `scrollWidth` uguale a `innerWidth` a 320, 360, 375, 414, 480, 600, 601, 700, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560; nessuna sovrapposizione di testi (controllo sui riquadri e a occhio sui pezzi). Altezza a 1440: 4808 px, piede compreso.
- Collegamenti: `tel:+390498790626` (testata, chiusura, piede), `mailto:info@narditalia.com`, Google Maps su Via Sant'Antonio 24/a, 35020 Tombelle di Saonara PD.
- Menu a 390 con bottone vero e `aria-expanded`; fisarmonica del piede provata (si apre "Contatti", le altre restano chiuse).
- Nessun U+2014 in pagina, nella NOTA, nel LEGGIMI e negli script (controllo nel `build_finale.sh`).
- `segnali.sh`: 15 soglie OK, 1 da guardare, 2 segnate da correggere che non sono segnali veri:
  - **Monospazio 100 %**: falso positivo dello strumento, che cerca "code" nel nome della famiglia; "En**code** Sans" è un grottesco proporzionale.
  - **Foto 27,2 % (soglia 35)**: la pagina è guidata da prodotti veri scontornati su fondo chiaro, come chiede la direzione; la chiusura usa una foto di Nardi a metà larghezza come da impaginazione scelta. Salirà con lo still life indicato nel LEGGIMI.
  - Da guardare: due misure di H2 (76 e 15 px del piede), voluto.
- Divieti del committente: nessun gradiente, nessun testo in gradiente, nessuna emoji, nessun Inter, nessuna card con bordo colorato, nessun vetro smerigliato, nessun modo scuro, nessuna fila di tre box con icona, nessun badge, nessuna icona Lucide, nessuna dissolvenza allo scorrere, nessun effetto sul cursore, nessun bottone che sbiadisce, nessuna lineetta lunga, nessun corsivo.
- Dati: ogni numero in pagina viene da `01-analisi.md` o dalle schede in `_prova/crawl/prodotti.json`. Quello che è dubbio sta nel LEGGIMI.
