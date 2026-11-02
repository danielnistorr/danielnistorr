# Meccanica Masi, home finale "Dal pieno"

Pagina: `sito/index.html`, si rigenera con `bash _prova/script/build_finale.sh`. Alta 5850 px a 1440, piede compreso (7545 a 390). Ultimo passaggio del 2 novembre 2026, dopo il giudizio cieco (`_prova/cieco.json`) e la richiesta del committente "più alta gamma, meno uguali tra loro".

## Idea

Un pezzo ricavato dal pieno e finito bene è già un oggetto da guardare. La loro leva con settore dentato in ghisa sta da sola al centro della prima schermata, appena fresata, con i segni dell'utensile nella tasca e la dentatura ad arco; un interruttore la mostra verniciata. Sotto il pezzo il titolo "Pezzi dal pieno, su disegno" corre esattamente da margine a margine e gli fa da basamento. Il pezzo, la coppia grezzo e verniciato e il verde del loro banco sono di Masi: con il nome di un concorrente la pagina non regge.

## Cosa è cambiato in questo passaggio

- **Impaginazione dell'apertura** (bloccante del giudice, K6): non più titolo a sinistra e pezzo scontornato a destra con le legende, lo schema che si ripeteva nella campagna (Agnoletto, DZ Stampi, BCM, Plastificazione Bastianello). Ora tutto sta sull'asse: pezzo al centro, didascalia in basso a sinistra e interruttore in basso a destra sulla stessa linea di base del pezzo, titolo su una riga sola a tutta misura (146 px a 1440, 164 px a 1920, corpo calcolato dalla larghezza del titolo in em, 8,99), sotto il testo a sinistra e la chiamata a destra. Nessun'altra home della campagna ha la composizione simmetrica né un titolo che misura esattamente la riga (controllato su `_invio/zona/home/copertine-est-grisignano.jpg` e sulle prime schermate dei `*-Sito`).
- **Titolo** (bloccante, K1): "Precisione in officina, continuità in produzione" (slogan del sito di oggi) diventa "Pezzi dal pieno, su disegno"; il testo sotto dice officina meccanica a Padova, le quattro lavorazioni, i rulli per la stampa offset e flexo e gli interventi in azienda.
- **Prima e dopo leggibile** (bloccante): tolto lo specchio della foto grezza (mostrava un pezzo che non esiste) e anche la rotazione; ognuna delle due foto è com'è stata scattata. Bottoni "Appena fresato" e "Verniciato", didascalia "Lo stesso pezzo, visto da due lati". La pagina apre sul pezzo appena fresato, il più bello.
- **Niente legende numerate sull'oggetto** (richiesta del committente): via pallini, filetti e numeri, sia a 1440 sia a 390. Resta una didascalia sobria: "Leva con settore dentato in ghisa. Fresata CNC dal pieno, alesatura H7. Lo stesso pezzo, visto da due lati."
- **Colore di fondo dal mestiere** (richiesta del committente): non più carta beige #F2F0EB ma #E1E6DE, il verde grigio del tappetino da banco su cui posano i loro pezzi nelle foto (pulegge #647062, misurato sulla foto, schiarito). Il motivo si vede: le pulegge della chiusura, il supporto Man-Roland e il mandrino stanno sullo stesso verde. Piede #D2D9CF. Le foto hanno un trattamento comune che porta il verde e l'azzurro del banco verso il verde della pagina e riporta a grigio le luci del metallo (l'alluminio accanto al verde tirava al rosa).
- **Ombra e bordi del pezzo** (importante): ogni leva su una tela stretta attorno a sé con 110 px di fondo in più sotto, quindi l'ombra sfuma e non è più tagliata da una riga dritta; ombra della leva bianca più corta (meno macchia grigia a sinistra del manicotto); sul verde la leva bianca ha contrasto pieno.
- **Fresatrice di repertorio tolta** (importante): al suo posto, a tutta larghezza, il loro gruppo mandrino espansibile smontato sul banco (inventario: qualità 5, apertura 5). Nella home non c'è più nessuna foto di repertorio né "Foto indicativa".
- **Sezione "veniamo noi da voi"** (importante): titolo in alto su dieci colonne, poi foto (colonne 1-6) e fasi (8-12) allineate in alto alla stessa quota; niente più vuoti accanto al titolo.
- **Lavorazioni**: quattro colonne, solo le lavorazioni d'officina e ognuna con un dato vero in testa (6 torni, 1 a CNC; 3 assi; da 10 cm a 3 m; TIG, MIG/MAG, elettrodo). Manutenzione e installazione stanno nella loro sezione. Cifre allineate senza tabellari (lo zero tabellare di Mona Sans è puntato).
- **Frasi ripetute** (minore): la commessa dei giornali resta solo nel progetto; "senza subappalti" una volta sola; "dal montaggio al collaudo" una volta; "nastri trasportatori, rulli e guide" una volta; la riga "Officina meccanica a Padova, dal 1977" non è più accanto all'email ma in chiusura ("A Padova dal 1977").
- **Logo** (importante): era già corretto dal passaggio precedente (`finale_logo.py`): "SRL" in tracciati, nessun `<text>`, nessun contorno bianco. Verificato con grep.
- **Legenda che toccava l'email a 1024** e **squilibrio del grezzo a 390** (minori): non esistono più; il pezzo sta in un riquadro fisso, allineato in basso al centro, quindi la distanza dal titolo è la stessa nei due stati e a ogni larghezza.

## Prime due schermate

- **1440** (`home-1440-prima-schermata.jpg`): testata (logo, Settori, Lavorazioni, Progetti, Contatti, telefono). La leva in ghisa al centro, alta 526 px; a sinistra in basso la didascalia, a destra in basso l'interruttore; il titolo da 64 a 1376 px; sotto, il testo d'apertura su tre righe a sinistra, "Chiama 348 169 34 51" e l'email a destra. Tutto entro i 900 px.
- **Seconda schermata**: "Dalla stampa ai trasporti industriali" e l'indice dei quattro settori, poi il mandrino a tutta larghezza.
- **390** (`home-390-prima-schermata.jpg`): la leva al centro alta 335 px, la didascalia, l'interruttore a tutta larghezza, il titolo su due righe a 52 px, poi il testo; telefono e Menu in testata.

## Chiusura e piede

- Chiusura ("b con foto", testo a sinistra e foto fino al bordo destro): "Un'officina che c'era ieri, c'è oggi e sarà qui domani" (Chi siamo), telefono grande in rosso #D8121A con tel:, email con mailto:, indirizzo come link alla mappa, orari, la loro frase "Chi ci chiama parla con chi lavora, e chi lavora conosce il mestiere." e "A Padova dal 1977". Foto vera delle pulegge dal pieno sul loro banco verde.
- Piede su #D2D9CF: logo vero con una riga su chi sono; quattro colonne Azienda, Lavorazioni (sette voci), Progetti, Contatti; riga legale con ragione sociale, indirizzo, P.IVA e C.F. 05200110285, REA PD-450853, codice SDI M5UXCR1, Privacy, Cookie. A 390 fisarmonica con veri bottoni (`aria-expanded`, `aria-controls`).
- **Niente colonna Seguici**: nessun profilo social vero (l'Instagram del sito porta a "#").
- **Niente newsletter**: lavorano su commessa per altre aziende, senza fiere, cataloghi, collezioni né clienti privati; il plugin newsletter del sito è installato e mai usato.

## Caratteri e colori

- **Mona Sans** (GitHub, distribuita da Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia, file variabili serviti dalla pagina in `sito/fonts/`. Titolo d'apertura 500 a larghezza 82 %, interlinea 0,86, spaziatura -0,024em; h2 500 a 85 %; testo 400 a larghezza piena; h3 e bottoni 600. Riferimenti: il maiuscolo stretto di Hermle e l'HelveticaNeue condensato di Fehlmann (`riferimenti/`); il pezzo solo con la sua ombra da Hermle; la composizione centrata con un solo oggetto e poco testo da Vaucher.
- Colori e contrasti (WCAG): inchiostro #141A16 su fondo 13,9:1, su piede 12,3:1; grigio #48514A 6,5:1 e 5,7:1; rosso scuro #A5101A (numeri delle fasi, passaggio su bottoni e link) 6,2:1; rosso del logo #D8121A solo per il telefono da 48 px della chiusura, 4,1:1 (testo grande); bottone nero con testo chiaro 13,9:1. AA ovunque.

## Interazione

Un solo gesto: l'interruttore "Appena fresato / Verniciato" sulla linea di base del pezzo. Due bottoni veri con `aria-pressed`, frecce sinistra e destra da tastiera, tocco su telefono; cambio netto della foto, senza dissolvenze. Il bottone di chiamata diventa rosso scuro al passaggio, mai sbiadito. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto sul cursore. Su telefono il menu è un bottone "Menu" e il piede si apre a fisarmonica.

## Controlli (2 novembre 2026)

- `finale_controlli.mjs` a 2560, 1920, 1440, 1280, 1024, 768, 390, 320: scrollWidth uguale a innerWidth a tutte le larghezze; nessuna sovrapposizione tra il pezzo (riquadro calcolato da object-fit), didascalia, interruttore, titolo, testo e bottoni, nei due stati. Clic (schermi grandi) e tocco (768, 390, 320) su Verniciato: `aria-pressed` passa e la foto grezza si nasconde. Tastiera a 390: freccia destra da Verniciato porta il fuoco e lo stato su Appena fresato, freccia sinistra torna a Verniciato. Fisarmonica: Lavorazioni si apre, le altre restano chiuse.
- Altezze: 2560 e 1920 = 6149 px, 1440 = 5850, 1280 = 5497, 1024 = 5449, 768 = 7151, 390 = 7545, 320 = 7855.
- Collegamenti: tel:+393481693451 (4 volte), mailto:info@meccanicamasi.it (3), mappa Google con l'indirizzo (2).
- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare; area foto 35,2 %, Mona Sans 100 %, monospazio 0 %, 18 filetti, 0 frecce, 0 numeri grandi, 0 etichette sopra i titoli, una sola sezione con titolo a sinistra e testo a destra (Lavorazioni), una data nel corpo (1977).
- Screenshot guardati a pezzi a 1440 e 390, prime schermate nei due stati a 320, 390, 768, 1024, 1440 e 1920. Nessun U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script. Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, niente card col bordo sinistro, niente vetro, niente tre box con icona, niente badge sopra il titolo, niente icone Lucide, niente dissolvenze allo scorrere, niente effetti sul cursore, niente bottoni che sbiadiscono, niente corsivo d'accento, niente legende numerate sull'oggetto.
