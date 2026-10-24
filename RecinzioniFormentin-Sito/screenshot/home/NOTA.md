# Home finale, "La rete ondulata": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `index.sorgente.html`, screenshot con `shots.mjs`; con l'argomento `tutte` anche 320, 768, 1024 e 1920). Controlli: `misura.mjs` (scorrimento orizzontale da 320 a 2560) e `prova_gesti.mjs` (campionario, menu, fisarmonica, console, nitidezza, collegamenti).

## L'idea

Una parete chiara e, a filo del fondo della prima schermata, la recinzione: è il confine della pagina e il titolo sta sulla parete sopra di lei. In questo giro la recinzione non è più il pannello verde di repertorio ma la cosa che solo Formentin fa: la loro rete ondulata a maglia intrecciata, disegnata in SVG con le misure vere di maglia e filo, i fili ondulati che passano sopra e sotto agli incroci e l'ombra sulla parete. Il titolo la nomina: "La rete ondulata la facciamo noi". Con il nome di un concorrente la prima schermata non regge: le sette maglie sono quelle della loro pagina `reti-ondulate/`.
L'unico gesto della pagina sta nella prima schermata: le sette maglie di serie sono un gruppo di scelta sopra la rete; toccandone una, la rete in fondo alla schermata si ridisegna con quella maglia e quel filo. Il disegno è vettoriale, quindi nitido a ogni densità di pixel e a ogni larghezza.

## La pagina, in ordine

1. **Apertura** (1440x900): testata con il marchio fedele, Produzione, Prodotti, Lavori, Esposizione e 049 760801. Titolo a 116 px su due righe; frase "Recinzioni e cancelli dal progetto alla posa, per abitazioni, aziende e campi sportivi. A Saonara, dai primi anni Settanta."; a sinistra "Le sette maglie di serie, disegnate in proporzione." con un righello di 40 mm disegnato nella stessa unità del disegno; a destra le sette maglie; sotto, a tutta larghezza, la rete. A 390 il titolo va su due righe a 40 px, le maglie su due file da quattro e la rete occupa il fondo della schermata (circa 300 px).
2. **Chi siamo e produzione** (inizia a y 900 a 1440): il paragrafo grande dalla pagina Azienda, poi due foto loro della rete ondulata (sul banco; posata in pannelli con telaio) mostrate a 400 px CSS, e il testo della produzione (filo nero o zincato, su ordinazione in rotolo o in pannelli; colonne, ringhiere, inferriate e tettoie).
3. **Per la casa, per l'azienda, per il campo sportivo**: tre righe, nome grande e una frase; sotto una riga sola su Betafence, materiali ed esposizione. Nessuna sigla di norma e nessuna misura in mm.
4. **Lavori recenti in alluminio**: tre foto loro, intere in 4:3, a 400 px CSS.
5. **Chiusura** e **piede**. Pagina alta 4524 px a 1440, piede compreso.

## Caratteri e colori

- **Geologica** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file `sito/fonts/geologica-latin-var.woff2`, licenza in `sito/fonts/OFL.txt`), una sola famiglia variabile: 300 per i titoli, 400 per il testo, 500 per enfasi e nomi; cifre tabellari per telefono, orari e maglie. Riferimento: Heras (sez. 7 dell'analisi), titolo grande e leggero in un grottesco razionale.
- Colori, scaldati in questo giro: calce calda #F2F0EB, parete dell'apertura #E8E5DE, piede #E9E6DF, antracite #1F2629 per i testi (13,5:1 sulla calce, 12,2:1 sulla parete), grigio #50585B per i secondari (6,4:1 sulla calce, 5,8:1 su parete e piede), verde scuro #0B5A4C per la maglia scelta (7,1:1), filetti #CFC9BE. La rete: filo zincato #A7AEB0 con bordo #3A4245 e un riflesso chiaro. Il marchio usa i suoi colori (#5A94F7, #08B508).

## Interazione

Campionario delle sette maglie (10x10 filo 2; 12x12 filo 2; 15x15 filo 2,5; 20x20 filo 3; 30x30 filo 3; 30x30 filo 4; 40x40 filo 4): gruppo di scelta ARIA con clic, tocco, frecce, Home e Fine; la maglia scelta prende il filetto verde e la rete si ridisegna. Ogni filo è una sinusoide con due onde per maglia (come nelle foto loro), fili orizzontali e verticali in controfase; agli incroci alterni il filo orizzontale torna sopra il verticale. Scala: 1 mm = 96/25,4 px CSS; la pagina non promette più la "scala 1:1" né la "misura vera" (la grandezza fisica cambia con lo schermo): dice "in proporzione" e mostra il righello nella stessa unità. Cambio netto, senza dissolvenze; transizioni di 0,15 s solo su bottoni e link. Sotto i 900 px un bottone Menu; a 600 px e meno il piede si apre a fisarmonica con veri bottoni.

## Chiusura e piede

- **Chiusura** ("b con foto", testo a sinistra e foto a destra fino al bordo; a 900 px e meno foto a tutta larghezza sotto): "Ampia esposizione in sede, su appuntamento, e preventivi gratuiti" (dalla home di oggi, con "previo appuntamento"), telefono grande con `tel:`, cellulare, `mailto:`, indirizzo con "Apri la mappa", orari, "Facilmente raggiungibile da corso Stati Uniti e dal casello Padova Zona Industriale."
- **Piede**: marchio con "Formentin / Recinzioni e cancelli" in antracite e una riga su chi sono; colonne Prodotti (Reti ondulate in testa), Azienda, Contatti (solo telefono, mail e Apri la mappa, per non ripetere la chiusura); riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie. Niente colonna social: nessun profilo trovato. **Niente newsletter**: il sito è fermo dal 2016, non hanno cataloghi propri, fiere né collezioni, e una recinzione si compra una volta ogni vent'anni; resterebbe vuota.

## Foto

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura: la rete ondulata | disegno SVG nella pagina, dalle misure di `reti-ondulate/` | nessuna foto |
| Rete ondulata sul banco | sito Formentin, `uploads_2014_04_rete_ondul01.jpg` (800 px) | dell'azienda |
| Rete ondulata posata in pannelli | sito Formentin, `gallery_reti-ondulate_IMG_1130-1.JPG` (800 px) | dell'azienda |
| Lavori: portale, recinzione e cancello, doghe sul muretto | sito Formentin, `canc082202`, `canc082204`, `ringh082202` (800x600) | dell'azienda, permesso dei clienti da chiedere |
| Chiusura, ringhiera e ombra sul muro | Jan van der Wolf, Pexels 38439497 | Pexels License |

Uscite in questo giro: il pannello verde di repertorio (Pexels 20182917) e la recinzione a doghe bianche (Unsplash YCEJqQeEsYA). Trattamento in PIL: chiari verso la calce calda, colore naturale (saturazione 0,85-0,95 invece di 0,2-0,62), leggera dominante calda. Ogni foto ha la versione 2x con `srcset`: le foto loro a 800 px per 400 px CSS, la chiusura a 1440 px per 720 px CSS.

## Cosa è cambiato dopo il giudizio cieco

- Apertura: la rete ondulata loro al posto del pannello di repertorio, il titolo che la nomina, niente legende, niente bottone e link sotto la frase (il telefono resta in testata); il campionario sale nella prima schermata e diventa il gesto dell'apertura.
- La produzione segue subito l'apertura (y 900 a 1440); il paragrafo di chi siamo è fuso in quella sezione.
- Disegno della rete rifatto: fili ondulati riempiti in grigio zinco con bordo antracite e riflesso, sopra e sotto agli incroci, ombra sulla parete.
- "Scala 1:1" e "misura vera" tolte; "in proporzione" con righello in mm.
- Sezione degli usi: tolta la foto di repertorio e la terza colonna di sigle e norme; una frase per uso.
- Colori scaldati e foto loro senza desaturazione forzata.
- Foto 2x; tre lavori visibili anche a 768 (tre colonne); marchio del piede in antracite; colonna Contatti del piede ridotta; "su appuntamento" nella chiusura e frase sui materiali corretta; tolto il preload del carattere (nessun errore in console su file://); `-webkit-tap-highlight-color:transparent` su bottoni e link.

## Controlli

- Screenshot in questa cartella: `home-1440.jpg` (4524 px), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`; guardati a pezzi, più 320, 768, 1024 e 1920 (intere e prime schermate).
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 430, 600, 768, 900, 1024, 1180, 1280, 1440, 1920 e 2560 (`misura.mjs`).
- Gesti (`prova_gesti.mjs`): clic su 40x40, freccia destra (passa a 10x10 con il fuoco), End e freccia sinistra (30x30 filo 4), Home, tocco a 390 su 30x30; menu e fisarmonica al tocco; zero errori e zero messaggi di errore in console su file://. A DPR 2 il browser carica i file da 800 px per le foto da 400 px CSS (rapporto 2,0; a 390 2,3) e quello da 1440 px per la chiusura da 720 px CSS (2,0).
- Collegamenti: `tel:+39049760801`, `tel:+393357740278`, `mailto:info@recinzioniformentin.it`, Google Maps su "Via Lombardia 17 35020 Saonara PD".
- `segnali.sh` a 1440: 16 soglie su 18 a posto; "contenuto datato" da guardare (un anno preciso manca, vedi LEGGIMI); "area foto" al 20,1 % contro il 35 % perché lo strumento conta solo img, video e canvas: l'oggetto dell'apertura è un disegno SVG a tutta larghezza (con lui l'area d'immagine sale a circa il 26 %). Scelta voluta: le foto loro sono a 800 px e mostrate più grandi sarebbero sfocate; la rete torna in foto vera appena c'è lo scatto del punto 1 del LEGGIMI.
- Nessun carattere U+2014 nella pagina, nella nota e nel LEGGIMI. Nessuna icona Lucide, nessun gradiente, nessuna dissolvenza allo scorrere, nessun effetto che segue il cursore.
