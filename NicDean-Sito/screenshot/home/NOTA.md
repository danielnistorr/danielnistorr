# Nic Dean, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `build_img.py`, caratteri, screenshot con `scatti.mjs`, controllo U+2014 e segnali da IA). Parte dal prototipo A, "La décolleté", con le indicazioni del giudice e gli innesti da B.

## L'idea

La loro fila vera di décolleté con plateau (pitone, arancio, senape, oliva, lilla, firma NicDean sul sottopiede) posata sul gesso della pagina, senza riquadro, e il titolo sotto, come la base su cui stanno le scarpe. Sotto ogni scarpa il suo colore: un tocco spegne le altre quattro (in grigio) e propone "Chiedi se c'è in spaccio", cioè il loro modo di vendere ("cerca la scarpa che ti piace e inviaci il nome per email"). Con il nome di un concorrente la pagina non regge: la foto e la firma sono loro.

Il giudice aveva dato K0 6: la prima schermata è stata ripensata dentro la stessa direzione, non ritoccata.
- **Prima** (prototipo): titolo in alto a sinistra, fila sotto, legenda in basso. Era lo stesso impianto di Hambro, Agnoletto e FM Sistemi; la didascalia galleggiava e la foto era ingrandita fino a 1,6 volte.
- **Ora**: la fila apre la pagina subito sotto la testata. Il titolo "Scarpe fatte a Villatora dal 1975" chiude la schermata in basso a sinistra, le tre righe su chi sono e "Orari dello spaccio" stanno in basso a destra. La didascalia "Cinque colori" è allineata in basso con la riga delle pastiglie, che stanno sotto l'asse di ogni scarpa.
- **Foto rifatta**: ingrandimento 1,09 volte a 1440 (massimo 1,3 sui file), nitidezza leggera (raggio 1,2, 60 %), segni d'uso attenuati su lilla e oliva, confini pitone-arancio e arancio-senape decisi anche dal colore.

## Le schermate

1. **1440x900.** Testata: logo, Spaccio, Storia, Per i negozi, Collezioni, telefono. Sotto, la fila larga 1060 px fino a 24 px dal bordo destro, con le cinque pastiglie; a sinistra "Cinque colori" a 28 px con "Décolleté con plateau, firma NicDean sul sottopiede." e "Tocca un colore per vederlo da solo". In basso il titolo "Scarpe fatte a Villatora dal 1975" in League Spartan 300 a 120 px su due righe; a destra le tre righe, "Orari dello spaccio" (porta a `#contatti`) e la riga degli orari "Dal lunedì al venerdì, 8-12 e 14:30-17" (link alla mappa).
2. **Sotto la piega**, quattro blocchi soltanto:
   - **storia e spaccio in una sezione di solo testo**: "Dal 1975 la famiglia Nicoletto fa scarpe a Villatora di Saonara", due righe sul prodotto e le tre date con filetti (1975, 1997, 2013); poi "Lo spaccio di via Lombardia" e la loro frase "Per donna, uomo e ragazzo. Da ginnastica, eleganti e sportive." a 80 px, come immagine tipografica, e tre righe su pagamento e appuntamento;
   - **"Per negozi, fiere ed eventi"**: testo sopra, poi la foto delle mani al montaggio a tutta larghezza (1440x756);
   - **la chiusura** "Calzature di tutti i tipi e di tutti i numeri" (frase loro): telefono grande, email, indirizzo e mappa, orari e pagamento, con i tronchetti a destra fino al bordo;
   - **il piede**.
3. **390.**
   - Testata: logo, bottone "Menu" (aria-expanded, bordo 1 px, al passaggio inverte i colori) e telefono.
   - La fila ingrandita 1,75 volte: tre scarpe intere e le due esterne tagliate.
   - Le cinque pastiglie a 22 px, poi "Cinque colori" e il testo sotto a 15 px.
   - Il titolo a 52 px, le tre righe e gli orari: tutto nella prima schermata da 844 px.
- **Altezze**: 4606 px a 1440, 5100 a 390, 5302 a 320, 4720 a 768, 4663 a 1024, 4660 a 1920 (da 4429 a 5447 tra 320 e 2560).

## Caratteri e colori

- **League Spartan** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una sola famiglia, servita dalla pagina in woff2 (latin e latin-ext, pesi 300-500 variabili).
  - Pesi: 300 per titolo, titoli di sezione, anni e telefono grande; 400 per il testo; 500 per menu, link e bottoni.
  - Perché: è un geometrico di impianto Futura che sta accanto alla scritta stencil del logo senza imitarla. Il riferimento è il geometrico leggero di Pollini e di ViBi Venezia: una scarpa, fondo chiaro, poche parole.
  - Zodiak di B non è stato portato: due voci indebolivano il gesto unico.
  - League Spartan non ha cifre tabellari vere: orari e recapiti sono su righe brevi allineate con la griglia (`dl` a due colonne).
- **Colori**:
  - gesso #F2EEE7 su tutta la pagina;
  - gesso scuro #E9E3DA solo nel piede, per staccarlo dalla chiusura;
  - inchiostro #1C1A17;
  - grigio caldo #625C53 per le note: 5,7:1 sul gesso e 5,2:1 sul gesso scuro;
  - rosso #C21F28 solo al passaggio sui link (5,2 e 4,7:1);
  - rosso del logo solo nel marchio;
  - verde #2E6B3A per il punto "aperto", che oggi non compare.

  Il colore lo portano le scarpe.

## Interazione

Cinque bottoni veri (`aria-pressed`), uno per colore.
- **Tocco o clic**: la foto passa di colpo alla versione con quel colore acceso e gli altri in grigio (saturazione al 18 %, schiariti di un quinto), senza dissolvenza. Sono sei immagini preparate con PIL e caricate dopo la pagina.
- **Didascalia**: (`aria-live`) dice il colore e il modello e offre "Chiedi se c'è in spaccio", con l'oggetto già scritto ("Décolleté con plateau, colore arancio", mailto a info@nicdean.it).
- **Tastiera**: secondo tocco o Esc riportano tutte le scarpe a colori; le frecce passano da un colore all'altro.
- **Telefono**: la foto scorre fino a mettere al centro la scarpa scelta, senza ingrandire oltre 1,75 volte (a 2,2 volte la foto da 1024 px mostrava i bordi delle maschere).
- **Stato attivo**: anello di 2 px, senza transizioni.

Nient'altro si muove: niente animazioni allo scorrere, niente effetti che seguono il cursore.

**Stato dello spaccio (innesto da B, spento).** Il codice c'è ma oggi la riga mostra solo gli orari, come chiesto, finché non si conferma che lo spaccio è aperto. Per accenderlo basta `STATO_ACCESO = true` nello script della pagina. Il calcolo usa l'ora italiana ed esclude il sabato, la domenica, agosto e i festivi nazionali: Pasquetta compresa, e il 4 ottobre dal 2026. Il testo è del tipo "Chiuso, riapre lunedì alle 8:00". Non c'è nessuna barra delle ore disegnata.

## Foto: origine e licenza

| File in sito/img/ | Origine | Licenza | Lavorazione |
|---|---|---|---|
| fila-*.jpg (6 stati, 760/1060/1264/1600/2120) | Nic Dean, `assets/originali/nuovo_images_index_foto1.jpg` (1024x683, loro sito di prova) | da chiarire: EXIF "Software: Google", autore ignoto | muro e piano portati al gesso; chiazze di luce e di colore attenuate su tutto il camoscio (lilla e oliva al 90 %, arancio e senape al 60 %); confini tra le scarpe disegnati, corretti sul colore e sfumati di 2,4 px; quattro scarpe in grigio per ogni stato, fondo invariato; 1600 e 2120 ingranditi con Lanczos e nitidezza proporzionale per gli schermi 2x |
| negozi-largo-*.jpg (960/1440/1600) e negozi-*.jpg (600/900/1200, telefono) | Fernanda Simões, Pexels 13524888 | Pexels License | taglio largo sulle mani e taglio 4:5; più calda, azzurri al 55 % di saturazione, velo di gesso al 10 % |
| chiusura-*.jpg | José Martin Segura Benites, Pexels 27256471 | Pexels License | taglio 1300x1625 sul risvolto, sopra l'arco dello specchio; più calda, velo di gesso all'8 % |
| logo-nicdean.png | rendering 4x del vettoriale del Flash `indice_nic.swf` (`assets/originali/logo-flash-reso-4x.png`) | dell'azienda | bianco reso trasparente, alto 96 px (2x del piede) |

Le foto di repertorio sono in `assets/CREDITI.md` (licenza verificata il 24/10/2026) e non compaiono nei CREDITI delle altre home della campagna (controllato di nuovo). Nessuna immagine generata. Nessuna foto di repertorio ha una didascalia o un testo che la faccia passare per loro: la sola didascalia è sulla fila, che è loro. I mocassini di repertorio, che stavano accanto a "prodotte interamente in azienda", sono stati tolti. La foto della chiusura non compare altrove nella pagina.

## Piede

- **In alto**: a sinistra il logo e una riga su chi sono; a destra la newsletter "Le novità dello spaccio" su una riga (campo, bottone inchiostro) con il consenso sotto.
- **Sotto un filetto, quattro colonne**:
  - Azienda: Storia, Fiere, Spaccio di fabbrica, Per i negozi;
  - Collezioni: Primavera, Estate, Autunno e inverno;
  - Contatti: telefono, fax, email, indirizzo in due righe;
  - Seguici: solo Facebook, come parola.
- **Riga legale**: "Nic Dean S.r.l., C.F. e P.IVA 02707240285, REA PD-300932, capitale sociale 51.000 euro i.v." con Privacy e Cookie a destra; a 390 diventa un testo continuo.
- **Newsletter**: sì, perché lo spaccio ha clienti privati e il loro sito dava già collezioni per stagione, sconti e chiusure per ferie. Il browser controlla email e consenso (campi obbligatori, con il suo avviso accanto al campo); se sono a posto una riga `aria-live` dice "Grazie, la newsletter sarà attiva a breve." Non invia nulla finché non si collega un servizio (LEGGIMI).

## Giro finale: cosa è cambiato dopo il giudice cieco (57 su 80)

- **La fila**: chiazze attenuate su tutto il camoscio, non solo sulla punta di lilla e oliva; file da 1060, 1600 e 2120 px nello srcset (prima il più grande era 1264). Resta una foto da 1024 px: nitida a 1x, non un 2x vero. La foto in studio è la condizione per mandare la home (LEGGIMI).
- **Il gesto**: scarpe spente in grigio invece che bianco latte, fondo che resta gesso; tolta la scheggia marrone a sinistra del tacco arancio (il colore decide solo dove l'arancio è chiaro e saturo) e i puntini grigi sul bordo destro dell'arancio; confini senape-oliva e oliva-lilla lisciati (media su 31 righe), niente più scaletta; al telefono niente ingrandimento a 2,2 volte.
- **Date vecchie fuori dalla pagina**: tolti "collezione estate 2017" (didascalia e oggetto della mail) e la riga della fiera di marzo 2012.
- **Niente più zig-zag**: storia e spaccio sono una sola sezione di testo; "Per negozi" ha il testo sopra e la foto a tutta larghezza sotto; solo la chiusura ha testo e foto affiancati. Tolta la foto dei mocassini.
- **Parole**: titolo "Scarpe fatte a Villatora dal 1975" (al posto di "Scarpe da donna", che contraddiceva "Per donna, uomo e ragazzo"); tolto "di livello medio-fine".
- **Foto**: negozi scaldata con gli azzurri spenti; chiusura ritagliata sopra l'arco dello specchio e scaldata.
- **Minori**: "Orari dello spaccio" porta a `#contatti`; nella chiusura testo dall'alto con 64 px tra titolo e recapiti (niente più vuoto da space-between); a 768 il testo d'apertura va su tutta la riga (52ch); newsletter con risposta; a 320 orari su una colonna.

## Controlli

- **Larghezze guardate a pezzi**: 1440 intera, 390 intera, 320 intera, 768, 1024 e 1920 (prime schermate e pagine). `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 414, 600, 768, 900, 1024, 1100, 1280, 1440, 1600, 1920 e 2560 (`_prova/script/controlli.mjs`).
- **Gesto provato** con Playwright: Invio, frecce destra e sinistra, Esc, spazio due volte; tocco a 390 su oliva, lilla, pitone e secondo tocco; `aria-pressed`, immagine caricata, didascalia e oggetto della mail corretti in ogni stato. Stati guardati ingranditi tre volte nei punti dove le scarpe si toccano.
- **Collegamenti**: `tel:+39049640672`, `mailto:info@nicdean.it` (anche con oggetto), mappa Google su via Lombardia 29, Facebook; nessuna ancora interna senza destinazione. Menu del telefono: si apre, si chiude col link e con Esc.
- **Segnali da IA**: `segnali.sh` dà 0 soglie bloccanti e 0 da guardare. Foto oltre il 35 % della pagina, una famiglia, H2 di 5 misure, 6 filetti larghi, nessuna freccia, nessuna etichetta maiuscola.
- **Nessun U+2014** in pagina, nota, LEGGIMI e script.
- **Divieti del committente**: nessun gradiente viola, nessuna card, nessuna icona, nessuna dissolvenza, nessun corsivo d'accento.
- **Limite noto**: la fila resta una foto da 1024 px con cinque scarpe ritagliate a mano; con una foto per colore dalla stessa posizione il gesto diventa esatto (LEGGIMI, prima foto da rifare).
