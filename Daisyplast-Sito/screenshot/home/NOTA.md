# Daisyplast, home finale "La bolla": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze), caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini (`finale_img.py`), pagina (`finale_pagina.html`), screenshot e prove dell'interazione (`finale_scatti.mjs`). Le verifiche finali sono in `finale_verifica.mjs` (larghezze, collegamenti, console, tocco) e `finale_misure.py` (misure delle foto).

Screenshot consegnati: `home-1440.jpg` (intera), `home-1440-prima-schermata.jpg` (1440x900), `home-390.jpg` (intera, telefono), `home-390-prima-schermata.jpg` (390x844), JPEG qualità 85.

## L'idea

Daisyplast fa una cosa che si vede da lontano: un tubo di film che sale per metri da un anello d'acciaio, la bolla di estrusione. La home mette in piedi quella bolla al centro dello schermo, come una colonna a tutta altezza su un campo bianco latte, e il titolo "Sacchi e film in polietilene" la attraversa in due righe incrociate: grafite sul latte, latte dentro la foto. Il cambio di colore cade esatto sul bordo della colonna, anche a metà di una lettera. La foto è la loro, la 015 del sito. Il giallo del cuore della margherita del logo resta una luce leggera sui riflessi; la margherita compare una volta sola, sul film compostabile.

## Le prime due schermate

1. **Apertura (bianco latte).** Colonna della bolla al 38 % della larghezza (fino a 600 px), da cima a fondo, bordi netti. "Sacchi e film" a sinistra e "in polietilene" a filo destro, in Sofia Sans Extra Condensed 300 a 176 px (fino a 216 px sopra i 1770 px). Il titolo è un h1 ritagliato fuori dalla colonna più una copia latte, nascosta ai lettori di schermo, ritagliata dentro la colonna (`clip-path`). In basso a sinistra chi sono, cosa fanno e per chi ("per grossisti del Triveneto, industrie e artigiani"), da quando, e la riga "Per un preventivo: 049 980 2226" sottolineata come il telefono della testata. A destra, sulla stessa linea di base, un solo dato composto come il titolo: "oltre 10.000 kg" a 96 px, con sotto le linee e le consegne. Sopra il dato la didascalia della foto (grigio #5F625D su latte, 5,9:1). Il logo è nei suoi colori veri, sul fondo chiaro per cui è disegnato. A 390 la bolla occupa lo schermo, il titolo la attraversa in latte e il testo sta in basso sulla velatura; a 768 la colonna resta un manifesto e il testo scende sotto.
2. **Tre materiali (bianco latte).** "Dalle stesse cinque linee escono tre film." Poi "Vergine", "Rigenerato", "Compostabile" a 118 px, che sono il titolo e il selettore. Sotto, la foto a tutta larghezza cambia col materiale; il cartellino con materia ed elenco dei prodotti sta dentro la foto, in basso a destra. I tre pannelli sono impilati nella stessa cella della griglia: la sezione ha la stessa altezza nei tre stati (1074 px a 1440, 1117 a 390).

Poi: il percorso di un ordine su grafite (palco a tutta larghezza, cinque tappe: la bobina vista di taglio, il quadro comandi della loro linea con la nota "110 AMP", le bobine avvolte, un palco solo tipografico con le linee di saldatura 2, 1, 1 a 432 px, i rotoli di sacchi), i clienti in elenco impilato, i contatti su grafite col telefono a 245 px e quattro recapiti in riga sotto filetti, il piede con i dati societari.

## Caratteri e colori, con i riferimenti

- **Sofia Sans Extra Condensed** 200-300 per titoli, nomi dei materiali, tappe, cifre grandi e telefono: alta e stretta come la bolla. È la stessa idea del Trade Gothic Next Condensed di Favini (riferimento 1 dell'analisi), una lettera condensata e sottile che lascia parlare la materia. **Sofia Sans** 400-600 per testo, menu e didascalie, con cifre tabellari per misure, orari e codici; le cifre grandi usano le proporzionali. Una superfamiglia, due ruoli fissi.
- Licenza: SIL Open Font License 1.1 (Google Fonts), testo in `sito/fonts/OFL.txt`. File woff2 variabili, solo latino, serviti dalla pagina, senza preload (con file:// dava un errore CORS).
- **Colori**: bianco latte #F3F1EA e grafite #1E1F1D sono i due campi (la monocromia di materia di Favini, lo still life scuro di Sulapac); il giallo #F2C230 del cuore della margherita è l'unico colore pieno: riga della tappa attiva, numero della tappa, luce leggera nelle foto. Il verde del logo resta solo nel logo.
- **Trattamento delle foto**, uguale per tutte tranne la margherita: bicromo grafite-latte; le luci virano verso il giallo moltiplicando il bicromo per il rapporto giallo/latte, al 20-24 % e con una curva morbida, così ogni sfumatura resta e non ci sono tinte piene; velatura cotta nella foto dove sta il testo; WebP con srcset.

## Interazione

- **Selettore dei materiali** e **percorso di un ordine**: due gruppi di schede (`role="tablist"`). Si usano con clic, dito, frecce, Inizio e Fine; il fuoco è visibile. Il palco si sfoglia anche trascinando col dito sulla foto. Il cambio è netto, senza movimento; solo il colore e la riga delle schede hanno una transizione di 120 ms. Pannelli e tappe nascosti restano nella griglia con `visibility:hidden`: nessun salto d'altezza cambiando stato.
- Sotto i 1260 px il menu si apre con un pulsante (`aria-expanded`); sopra, le quattro voci stanno a destra della colonna.
- Niente animazioni allo scorrere, niente effetti sul cursore, niente bottoni che sbiadiscono. Con `prefers-reduced-motion` nessuna transizione.

## Foto: origine e licenza

Ogni sorgente compare una volta sola in pagina; la 015 dà due tagli diversi (la bolla in apertura, il quadro comandi nella tappa 2), come chiesto dalla revisione.

| File in sito/img | Origine | Licenza | Dove |
|---|---|---|---|
| bolla, bolla-p | foto 015 del sito daisyplast.it, lato sinistro (testa di estrusione), ritaglio nativo 768x1280 e 590x1280 | da far confermare all'azienda | apertura |
| t2-piano, t2-piano-p | foto 015, lato destro (quadro comandi, nota "110 AMP"), ingrandito 1,35x su palco grafite | da far confermare | tappa 2 |
| t1-ordine | foto 005 della libreria del sito (bobina in asse, taglio stretto sugli strati) | da far confermare | tappa 1 |
| t3-bobine | foto 001 del sito (bobine di film bianco su mandrini), repertorio | da far confermare | tappa 3 |
| t5-consegna | foto 002 del sito (rotoli di sacchi), fondo del catalogo portato a grafite con maschera stretta | da far confermare | tappa 5 |
| logo.webp | Logo.png del sito, nei suoi colori | logo aziendale | testata |
| vergine-l, vergine-p | Unsplash tJ-SrdvRF20, Yosafat Herdian; fondo nero allungato a destra | Unsplash License | selettore |
| rigenerato-l, rigenerato-p | Unsplash mFcsYcSSiMQ, Compagnons | Unsplash License | selettore |
| compostabile-l, compostabile-p | Unsplash kFK54FCIB3U, Daniele Levis Pelusi; scontornata, fondo latte uniforme, specchiata | Unsplash License | selettore |

Tolte in questo passaggio: la 007 (bobina rossa, tappa 2), la 005 intera dei contatti (era la seconda apparizione), il quadro del reparto e la tappa 3 sulla 015 (terza apparizione). Nessuna didascalia attribuisce a Daisyplast una foto Unsplash. Nessuna immagine generata dall'IA, nessuna foto nuova scaricata. Le licenze sono in `assets/CREDITI.md`.

## Cosa è cambiato con la revisione cieca (K0 7, 59/80)

1. **Foto dell'apertura** (bloccante): rifatta dal 015 originale al ritaglio nativo più grande, 768x1280 (prima 640x1200), servita con srcset 600w e 768w; via il filtro mediano e la nitidezza aggiunta. La virata al giallo scende dal 55 % al 24 % e moltiplica il bicromo invece di sostituirlo con una tinta: 0,000 % di pixel di giallo pieno, saturazione massima 63 su 255; 36 finestre 20x20 piatte su 9450 (0,4 %), 23 delle quali già bruciate nella foto dello smartphone (riflessi e finestra).
2. **Campo dell'apertura latte invece di grafite** (rischio K6 con FM Sistemi): la colonna resta, il titolo è grafite fuori e latte dentro la foto. Le due prime schermate non condividono più fondo né trattamento del titolo (FM Sistemi: campo nero, lettere larghe, tubo di rame orizzontale). La prima schermata è anche più calda (K7).
3. **Via la sezione Reparto** (schema foto ai 2/3 più tabella dell'anti-esempio, dati doppi): "Siamo in tredici, dal 2008" passa nella tappa 3, la frase sul petrolio nella tappa 2, il quadro comandi diventa la foto della tappa 2 "Il piano". Tolta la voce Reparto dal menu.
4. **Ripetizioni**: la bobina rossa 007 e la spirale 005 dei contatti sono tolte; la tappa 3 usa le bobine avvolte (001), quello che esce dalla linea in bolla; la tappa 4 è un palco solo tipografico con 2, 1, 1 grandi, così la foto non dice più una cosa diversa dal testo. Le cifre stanno solo nella tappa 4.
5. **Contatti** senza foto: titolo, telefono a 245 px, quattro recapiti in riga sotto filetti (due colonne sotto i 1000 px, una sotto i 560). Sparisce anche la fascia vuota a 768.
6. **Testi**: via le istruzioni d'uso ("Scegliete il materiale...", "Si sfogliano con un clic..."); sopra le schede "Dalle stesse cinque linee escono tre film."; il titolo del percorso diventa "Dall'ordine alla consegna", così non ripete la frase della tappa 1. Il "per chi" e un invito al preventivo sono nella prima schermata.
7. **Margherita**: scontorno rifatto con maschera chiusa sul fiore e sul petalo staccato, contorno grigio schiarito, fondo latte uniforme. Fascia di fondo: deviazione standard della luminanza 0,00; intorno ai petali L minima 62,5, nessun pixel sotto L 60.
8. **Rotoli della tappa 5**: maschera nuova (fondo bianco, riflesso giallino e ombra grigia), stretta di 2 px e sfumata di 1 px: niente alone sul bordo destro.
9. **Minori**: padding sotto le schede del percorso a clamp(32px, 3vw, 48px); a 390 niente più min-height fissa, il palco tiene l'altezza della tappa più lunga (900 px in tutti e cinque gli stati); orari con la lineetta media U+2013 (8:00–12:00, Lun–Ven); logo su `index.html`; nel piede "Questa pagina non usa cookie" al posto del collegamento vuoto; tolto il preload del carattere.
10. **Respinto**: object-position del quadro a 50% 8% (la sezione non esiste più; nella tappa 2 la scritta "110 AMP" si legge a 1440 e a 390).

## Controlli

- **Larghezze**: screenshot a 320, 390, 768, 1024, 1440, 1920, guardati a pezzi, con i cinque stati del palco, i tre del selettore e il menu aperto a 390. scrollWidth uguale a innerWidth su 108 larghezze da 320 a 2560 (passo 10 px fino a 1000, poi 40).
- **Interazione**: a 1440 e 390 la freccia porta il fuoco su "Compostabile", End porta alla tappa 5, la freccia torna alla 1, il trascinamento passa dalla 1 alla 2; altezze di materiali e percorso uguali in tutti gli stati. A 390 con tocco vero (eventi touch): tap su "Rigenerato", trascinamento del dito sul palco dalla 1 alla 2, tap sulla tappa 3.
- **Collegamenti**: tel:+390499802226 (testata, prima schermata, tappa 1, contatti, piede), mailto:info@daisyplast.it, mailto:daisyplastsrl@pec.it, mappa Google su "Via del Lavoro 25 30030 Vigonovo VE", ancore #materiali #percorso #clienti #contatti tutte con destinazione. Nessun errore o avviso in console aperta come file://.
- **U+2014**: assente da pagina, script, nota e LEGGIMI (lo verifica `build_finale.sh`).
- **Segnali** (`segnali.sh` a 1440): 0 soglie bloccanti. Area foto 36 %, 13 filetti, nessuna freccia, nessuna etichetta maiuscola, nessun titolo col punto, 4 misure di H2, una data (2008), Sofia Sans 71 % ed Extra Condensed 29 %, nessun titolo nero, nessun numero grande con etichetta. Una riga DA GUARDARE, voluta: 5 fasce di fondo (prima 8), cioè latte e grafite che si alternano tra apertura e materiali, percorso, clienti, contatti e piede.
- Divieti del committente: niente Inter, gradienti viola-blu, testo in gradiente, emoji, bordo sinistro colorato, glassmorphism, tre box con icona, badge, icone, dissolvenze, effetti sul cursore, bottoni che sbiadiscono, lineette lunghe, corsivi d'accento.
