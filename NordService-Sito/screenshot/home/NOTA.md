# Nord Service, home finale "Tornano nuove": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (pulizia dello scontorno, immagini, caratteri, screenshot). Parte dal prototipo A, scelto dal giudice; questa è la versione dopo l'ultima rifinitura (giudizio cieco in `_prova/cieco.json`).

Screenshot in questa cartella: `home-1440.jpg` (pagina intera, 5292 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5580 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (chiusura e piede).

## L'idea

Una macchina da lavoro che torna nuova, posata sul suolo. "Tornano nuove" (dal loro "Sappiamo far tornare nuove le macchine") su una sola riga larga quanto la pagina; sotto, la pala gialla WA320 (foto Sony, l'unica da apertura) in piedi su un filo sottile che attraversa la prima schermata come il suolo e arriva fino al bordo della finestra, anche a 1920. Sotto il filo una sola didascalia: "Komatsu WA320, maggio 2025". Subito dopo, nella seconda schermata, la prova: lo stesso lavoro su un apripista D8R in tre giorni veri (sabbiato, verniciato, finito). La pagina racconta una cosa per volta.

## Cosa è cambiato nell'ultima rifinitura

Dal giudizio cieco (K0 6,5, K1 6, K6 6):
- **Apertura**: tolta la linea dei giorni con le date dell'apripista sotto la WA320 (ingannava: sembravano le date della pala). Il filo resta come suolo, senza tacche né numeri, con la didascalia che nomina la macchina. Nessuna data di ottobre 2024 nella prima schermata.
- **Composizione nuova**: il titolo su una riga a tutta larghezza in alto, la pala grande in basso a destra che esce dal bordo, il testo in basso a sinistra sulla stessa linea di terra. Non è più lo schema "titolo a sinistra, oggetto a destra, righello graduato sotto" di Hambro, Innovatex e Agnoletto.
- **Titolo e benna**: il titolo non si sovrappone più alla pala a nessuna larghezza (distanza misurata tra la linea di base e il primo pixel della benna: 48-50 px da 1024 a 2560, 148-169 px sul telefono).
- **Ordine**: l'apripista con le linguette è la seconda sezione, prima delle lavorazioni. Foto della sequenza più piccole (6 colonne su 12, al massimo 640 px sotto i 1000).
- **Chiusura**: via le virole blu (fuori soggetto, lavoro da confermare). Al loro posto un dettaglio 4:5 della foto del 10 ottobre: ruota dentata e cingolo appena verniciati di giallo, quasi solo macchina.
- **Fascia delle lavorazioni**: via la mascheratura Sony affollata (finestre, tubi). Al suo posto il mini escavatore in cabina con carta e nastro (telefono, dicembre 2024): braccio arancio, il resto coperto. L'arancio è quello del logo.
- **Telefono**: il bottone "Chiama" sta tutto nella prima schermata (fino a 780 px su 844); il menu si chiude dopo il tocco su una voce; il telefono in testata è un bersaglio di 44 px.
- **Minori**: alt della pala senza "riverniciata"; in testata "Prima e dopo" (non più "Lavori", che nel piede porta a `lavori/`); "Fondi e vernici a liquido" con lo stesso nome nella sezione e nel piede.

## Le sezioni

1. **Apertura**: testata con il logo vero, Prima e dopo, Lavorazioni, Contatti, telefono. Titolo, la riga su cosa fanno e dove, il bottone arancio "Chiama 049 900 5162" e la mail; la pala sul suolo. A 390: titolo su due righe, la riga, la pala a tutta larghezza, il suolo con la didascalia, il bottone.
2. **Un apripista D8R, ottobre 2024**: foto a filo del bordo sinistro, tre linguette Sabbiato, Verniciato, Finito con le date.
3. **Sulla carrozzeria intera o su un solo pezzo**: per chi lavorano, le sei lavorazioni in griglia 3x2 di solo testo con filetti; sotto, la fascia del mini escavatore.
4. **Chiusura**: "Sappiamo far tornare nuove le macchine con cui lavori ogni giorno", telefono grande, mail, indirizzo con mappa, orari, la riga su Stefano e Leonardo Barbieri; a destra fino al bordo la foto del cingolo.
5. **Piede**.

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1: uso commerciale libero, si può incorporare e servire dal proprio sito). Variabile con asse di larghezza, servita da `sito/fonts/` (woff2 latin e latin-ext). Titolo d'apertura 600 a larghezza 118, titoli di sezione 600 a 108, testo 400 a 100; cifre tabellari per date, orari e telefono. Una sola famiglia. Motivo: le scritte larghe e piene sulle macchine (WA320, D8R) e il logo condensato; la larghezza espansa dà il peso del mezzo senza il nero.
- **Colori** (01-analisi.md, sez. 5): carta #F4F2EE, inchiostro #171717, testo secondario #4A4844, piede #EAE7E1, arancio del logo #EF7821 solo sul bottone, sul filetto del telefono e sulla linguetta attiva; #A9500F per i link al passaggio e il fuoco. Contrasti (WCAG): #171717 su #EF7821 6,3:1; #4A4844 su #F4F2EE 8,2:1 e su #EAE7E1 7,4:1; #A9500F su #F4F2EE 4,9:1. Tutti AA.
- **Riferimenti**: Singer Vehicle Design (riportare a nuovo come lusso: una macchina sola, chiara, quasi niente testo), Volvo CE (il mezzo giallo su fondo bianco, menu corto), Hempel (molto vuoto attorno al prodotto vero). Tra le home amate: FM Sistemi chiara e Mario Agnoletto chiara (l'oggetto vero e grande, il titolo sicuro), senza ripeterne gli schemi.

## Interazione

Un solo gesto: le tre linguette "Sabbiato, Verniciato, Finito" accanto alla foto dell'apripista. Al clic o al tocco la foto cambia di colpo, senza dissolvenza, con la sua didascalia. È un `tablist` vero: frecce, Home e Fine da tastiera. Nessun'altra animazione; il menu del telefono è un `details` nativo che si chiude dopo la scelta; c'è il link "Vai al contenuto".

## Foto, origine e licenza

Tutte dell'azienda, scaricate da nordservice.net (vedi `assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- `pala-*.webp` (apertura): DSC07377, Sony, maggio 2025 (voti 8/7). Scontorno del prototipo (maschera ISNet, modello Apache 2.0, usato solo per separare la macchina dallo sfondo, corretto a mano), ripulito da `_prova/script/finale_pala.py`: vetri fumé, ombra nuova. Nessun pixel della macchina inventato.
- `d8r-sabbiato`, `d8r-verniciato`, `d8r-finito` (sequenza): IMG_20241003, IMG_20241010, IMG_20241016, telefono (voti 5-6). Tre quadrati con la base dei cingoli alla stessa altezza; nella foto del 16 ottobre il verde del pavimento è smorzato.
- `carta-*.jpg` (fascia): IMG_20241202, telefono (voto 6), 2:1 a tutta larghezza, a sinistra tagliata la scatola elettrica.
- `cingoli-*.jpg` (chiusura): dettaglio 4:5 di IMG_20241010 (voto 6), ruota dentata e cingolo.
- `logo-112.png`, `logo-192.png`: logo PNG trasparente con S.R.L., ritagliato, a 2x. Niente SVG ricostruito: il braccio a traliccio della "I" non si ridisegna fedele senza l'originale vettoriale.
Lavorate con PIL (`_prova/script/finale_img.py`), esportate in tre o quattro larghezze con srcset. Tutte, tranne la pala, vanno rifatte con la Sony (LEGGIMI).

## Piede

Logo, una riga su chi sono; colonne Lavorazioni (le sei voci vere), Azienda (Chi siamo, Lavori, Prima e dopo, Contatti), Officina (telefono, mail, indirizzo con mappa, orari), Seguici (solo Instagram: Facebook oggi è un link vuoto). Riga legale: Nord Service S.r.l., P.IVA 04717810289, sede legale a Rubano, Privacy, Cookie. A 390 due colonne per riga, in ordine.
**Niente newsletter**: è un servizio su richiesta per chi possiede o costruisce macchine da lavoro; non hanno notizie, fiere, cataloghi né clienti privati da tenere informati (01-analisi.md, sez. 5 e 8).

## Controlli (ultima rifinitura)

- `_prova/script/finale_controlli.mjs` a 320, 390, 768, 1024, 1100, 1200, 1280, 1366, 1440, 1920 e 2560: scrollWidth uguale a innerWidth a tutte, nessun testo sovrapposto o fuori finestra, titolo lontano dalla benna. Prime schermate guardate a 320, 390, 768, 1024, 1440 e 1920; pagine intere a 1440, 390 e 768 guardate a pezzi.
- Gesto provato con il clic a 1440 e con il tocco a 390: la foto cambia, frecce, Fine e Home spostano fuoco e selezione. Menu del telefono: si apre al tocco, si chiude dopo la scelta.
- Collegamenti: `tel:+390499005162` (5), `mailto:info@nordservice.net` (3), mappa Google con "Via Levico 20 35035 Mestrino PD" (2), Instagram; i link alle pagine future sono nel LEGGIMI.
- `segnali.sh`: 0 soglie bloccanti. Foto 35,9 % dell'area, Archivo 100 %, 9 filetti, nessuna freccia, nessun numero grande con etichetta, nessun divieto. Da guardare solo le due misure di H2 (54 e 66 px): voluto, l'unico elemento grande è il titolo d'apertura.
- Nessun carattere U+2014 nella pagina, negli script, nella nota e nel LEGGIMI. Nessuna dissolvenza, nessun effetto sul cursore, nessuna icona Lucide, nessun gradiente.
- Altezza a 1440: 5292 px compreso il piede.
