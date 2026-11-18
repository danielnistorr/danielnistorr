# D.Z. Stampi, home finale "Il pezzo"

Proposta non richiesta di nuova homepage (solo la home). Pagina statica in `sito/index.html`, immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (scontorno dello stampo, immagini, pagina, screenshot, controlli).

Base: prototipo A. Ultimo passaggio fatto sulle indicazioni del giudice cieco (52/80, non passava per K1, K6, K7): prima schermata rifatta dentro la stessa idea, foto dello stampo rifatta, palette scaldata, settori reimpaginati.

## Idea

Una metà di stampo a iniezione in acciaio, nitida e grande, che entra nel campo chiaro dal bordo destro e da quello in basso, con tre legende sulle sue parti come in una tavola di montaggio: golfare, colonna di guida, impronte. È l'oggetto del mestiere, non un pezzo lavorato qualsiasi. Il titolo è la loro frase ("l'intero processo creativo/produttivo dello stampo, partendo dalla progettazione 2D e 3D, fino alla fase finale del collaudo"). Il racconto va dallo stampo (apertura) ai pezzi di plastica che ne escono (settori e chiusura), passando per le quattro tappe e le macchine vere.

## Cosa è cambiato in questo passaggio

- **Foto dello stampo** (bloccante): stessa foto Unsplash scaricata a 3600x4500 invece di 1920x2400; niente CLAHE e niente denoise aggressivo; grigio ricavato dal colore, curva morbida in virgola mobile con neri sollevati (nessun nero pieno, nessuna banda), tinta acciaio appena calda; il moncone della seconda colonna sul bordo destro è fuori dal taglio. WebP a 800, 1200, 1800 e 2400 px, `sizes` 66vw. Verifica a 1440 con deviceScaleFactor 2, ritaglio 920x680 da x=520 y=220: spigoli puliti, nessuna macchia o banda; resta sfocato il lato destro, che è la profondità di campo dell'obiettivo (la foto vera dovrà essere tutta a fuoco, vedi LEGGIMI).
- **Prima schermata** (bloccante K1, importante K6): titolo "Dal disegno al collaudo" dalla loro voce al posto di "Stampi per materie plastiche" (che resta nella frase e nel title); tre legende sulle parti dello stampo, con punto, filetto e nome ("1 Golfare", "2 Colonna di guida", "3 Quattro impronte in un unico assieme", dalla loro "matrice multipla in un unico assieme"); tolta la didascalia col filetto sulla corsa del Parpas, che resta solo nella sezione Macchine; bottone nero invece che corallo; lo stampo è più grande (66 % della larghezza). A telefono e tablet le legende diventano numeri cerchiati sulla foto e una riga di legenda sopra.
- **Settori** (importante K6, esecuzione 960-1150): le tre parole in riga sopra la foto a tutta larghezza, la frase a destra; niente più colonna di nomi sopra la foto, quindi niente sovrapposizioni a nessuna larghezza (spazio tra schede e frase 18-24 px in orizzontale o in verticale, "Foto indicative" sempre dentro la sezione). Oggetti spostati verso il centro della foto. Il bordo alto delle foto prende esattamente il colore della sezione, colonna per colonna.
- **Palette** (importante K7): carta #ECEBE7, campo #DEDCD7, piede #E4E2DD, inchiostro #1B1A18, grigio #57534D; tutte le foto portate allo stesso grigio caldo (siringhe e vasetto senza più azzurro, fresatura e pezzi della chiusura appena caldi).
- **Alimentare**: la scheda ora si chiama "Alimentare" e la frase dice "Vaschette, contenitori e secchielli a spessore sottile, anche con il sistema IML", senza descrivere un decoro che la foto non mostra; il vasetto è reso neutro e chiaro. Una foto gratuita di una vaschetta IML decorata non esiste su Unsplash e Pexels (ricerca in `assets/CREDITI.md`): resta da fotografare.
- **Chiusura**: foto rifatta con i due pezzi interi e margini ampi (nessun pezzo tocca i bordi a 1440, 1024 e 390); recapiti ridotti a telefono, info@, indirizzo con "Apri la mappa" e fax in grigio, senza etichette né filetto. dzstampi@ e amministrazione@ passano alla pagina Contatti.
- **Piede**: la colonna Contatti non ripete più fax e indirizzo: telefono, info@, Dove siamo, Area riservata; Azienda ha Chi siamo, Le macchine, Contatti.
- **Testi**: medicale "Pezzi per il medicale: progetto e lavorazioni restano in officina, il prodotto che ci affidate resta riservato." (dalla loro frase sulla segretezza); automotive "Stampi per componenti dell'automobile." (tolto il percorso SLS, che nella fonte non è legato all'auto); tappe "Quattro tappe, dal prototipo alla serie".
- **Margini e larghezze**: tra testata e titolo almeno 49 px a ogni larghezza (51 a 960 e 1024); tra 960 e 1180 la frase si stringe a 270 px e il piede dell'apertura sparisce; sopra i 1920 px il contenuto si ferma a 1920 e lo stampo resta a filo del bordo destro; l'apertura è alta 62,5vw fino a 1200 px, così a 1920 le legende non vengono tagliate.
- **Schede inattive**: #605C56, 4,85:1 sul campo; a 390 le schede sono in peso 400.

## Prime due schermate

1. **Apertura (1440x900)**: testata con il logo vero, quattro voci e il telefono. Titolo "Dal disegno al collaudo" a 124 px su due righe; sotto una frase su cosa fanno e per chi e un solo bottone "Chiama 0444 415163". Lo stampo entra da destra e dal basso con le tre legende; in basso "Dal 1985 a Grisignano di Zocco, a 50 metri dal casello A4" e "Foto indicativa" sotto la terza legenda.
   - A 390: titolo, frase, bottone, la riga della legenda e lo stampo a filo del bordo destro con i numeri 1, 2, 3 sulle parti. A 768 lo stesso schema; da 960 in su l'impaginazione larga in unità del contenitore (cqw).
2. **Settori**: "Stampi per i settori", le tre schede in riga (Medicale, Automotive, Alimentare) con la frase a destra, sotto la foto del pezzo a tutta larghezza. A 390 le schede stanno una per riga, alte 52 px.

Poi: "Quattro tappe, dal prototipo alla serie" con la fresatura (banda 5:2) e le quattro tappe, più revisione e manutenzione; "Tre centri di lavoro a 5 assi, fino a 3000 × 1600 mm" con le macchine in cinque righe per tipo; la chiusura e il piede. Altezza a 1440: 5282 px, piede compreso.

## Chiusura e piede

- **Chiusura**: titolo "Cinquanta metri dal casello, e siete arrivati" (dal loro "Dove siamo"), telefono grande in corallo scuro con `tel:`, "Formuliamo offerte senza alcun impegno." (dal testo Azienda), poi info@ con `mailto:`, l'indirizzo con "Apri la mappa" (coordinate del loro link a Google Maps) e il fax in grigio. A destra, fino al bordo e alta quanto il testo, la foto dei due pezzi bianchi su grigio caldo. Niente riquadri.
- **Piede**: logo vero (PNG 352x172 mostrato a 176 px, quindi a 2x) con una riga su chi sono; quattro colonne (Azienda, Lavorazioni, Settori, Contatti) con le voci vere; riga legale con ragione sociale, P.IVA e C.F., capitale sociale, Privacy, Cookie. REA e PEC non messi (dubbi, vedi LEGGIMI). A 390 le colonne vanno due per riga in ordine; sotto i 360 px una per riga.
- **Niente colonna social**: non esistono profili dell'azienda.
- **Niente newsletter**: nessuna novità periodica da comunicare (niente notizie, fiere o cataloghi), clienti solo aziendali che lavorano su commessa e su offerta.

## Caratteri e colori

- **Bai Jamjuree** (Cadson Demak, Google Fonts, licenza SIL Open Font License 1.1, uso commerciale libero; `sito/fonts/OFL.txt`), servita dalla pagina in tre pesi: 300 per i titoli (spaziatura -0,03em), 400 per il testo corrente (mai sotto i 16 px, 18 px di base), 500 per nomi delle macchine, numeri delle legende e titoletti del piede. Riferimento: **Glaroform** (stampi a iniezione svizzeri) usa Daytona Light; Bai Jamjuree ha lo stesso scheletro quadrato con gli angoli raccordati, come una tasca fresata col raggio della fresa. Numeri delle legende in cifre tabellari (`font-variant-numeric`).
- **Colori**: carta #ECEBE7, campo #DEDCD7 (apertura con una luce radiale appena più chiara in alto a sinistra, settori), piede #E4E2DD, inchiostro #1B1A18, grigio #57534D (6,4:1 sulla carta, 5,6:1 sul campo, 5,9:1 sul piede), schede inattive #605C56 (4,85:1). Corallo #E2604E solo per la sottolineatura della scheda attiva e i tre quadratini dei 5 assi; corallo scuro #A8382A per il telefono della chiusura (5,4:1) e il passaggio sul bottone; bottone nero con testo bianco (17,4:1). Il viola resta solo nel logo.

## Interazione

Un solo gesto: le tre schede dei settori (`role="tab"`, frecce, Home e Fine, Tab entra sulla scheda attiva). Al clic o al tocco cambiano subito foto e frase, senza dissolvenze; transizione di colore breve solo sulla scheda toccata. Sotto i 900 px il menu si apre con un bottone "Menu" con `aria-expanded`. Niente animazioni allo scorrere, niente effetti che seguono il cursore.

## Foto, origine e licenza

Tutte segnaposto Unsplash in `assets/esterne/` (licenza verificata sulla pagina di ogni foto, uso commerciale libero, nessuna Unsplash+; dettagli in `assets/CREDITI.md`). Nessuna è usata in altre home della campagna. Nessuna immagine generata dall'IA.

- **Apertura**: `FizNN4mzOA0` (hosein fayton) a 3600 px, metà di stampo vero con quattro impronte, colonna di guida e golfare, scontornata (GrabCut di OpenCV guidato da poligoni tracciati a mano, bordo sinistro della piastra dritto, golfare ridisegnato sulla sua forma misurata) e trattata come sopra, con un'ombra morbida.
- **Settori**: medicale `1SutQMy6UVU` (Diana Polekhina, siringhe), automotive `Epi5exvDtkU` (Mastars, scocca nera), alimentare `Rg0KmrUPB_Q` (Diana Polekhina, vasetto: non è IML). "Foto indicative" in pagina.
- **Lavorazioni**: `sxtClAGwRck` (aluminum Zheng ji), centro di lavoro con refrigerante, quasi monocromo e appena caldo.
- **Chiusura**: `Ec1mAEzKtRw` (Mastars), due pezzi tecnici bianchi.
- **Logo**: `DZlogo.png` del sito attuale (352x172), a 112 px in testata e 176 px nel piede.

Da rifare dal vero prima della pubblicazione: vedi LEGGIMI (con la foto vera vanno rimisurate le posizioni delle legende). Le due foto di Mastars (azienda cinese di stampi, nessun marchio visibile) vanno comunque tolte.

## Controlli

- Screenshot: `home-1440.jpg` (5282 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6174 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più pagina intera e prima schermata a 320, 768, 1024 e 1920. Guardati a pezzi; in più prove a 960, 1100, 2560 e a 1440 in 2x per la nitidezza dello stampo, e le schede Automotive e Alimentare aperte.
- `_prova/segnali-finale/controlli.json` (da `rif_controlli.mjs`): scrollWidth uguale a innerWidth a 28 larghezze da 320 a 2560; nessuna sovrapposizione tra titolo, frase, bottone, legende e piede dell'apertura, nessun testo dell'apertura fuori dalla sezione; schede provate col tocco (Alimentare, Automotive) e con la tastiera (frecce destra e sinistra con il giro, Fine, Home, Tab che esce): `aria-selected`, `tabindex`, pannelli e foto sempre coerenti; menu a 390 con `aria-expanded` da false a true e di nuovo false dopo il clic su una voce; collegamenti `tel:+390444415163` (tre), `mailto:info@dzstampi.com` (due), mappa `google.com/maps/search/?api=1&query=45.482702,11.708293`; nessuna ancora interna rotta.
- Nessun testo oltre il margine a 320, 390, 768, 1024, 1440 e 1920 (`finale_shots.mjs`); una sola famiglia, nessun testo corrente sotto i 16 px; contrasti AA calcolati come sopra.
- `segnali.sh` del kit: 18 soglie su 18 OK, nessuna da guardare (foto al 42,6 % della pagina, una famiglia, niente monospazio, 0 etichette maiuscole, 0 titoli col punto, 12 filetti, 4 fasce). Divieti del committente: nessuno (niente gradienti viola, niente card, niente badge, niente icone, niente dissolvenze, nessuna lineetta lunga in pagina, NOTA e LEGGIMI).
- Ogni fatto in pagina viene da `01-analisi.md`.
