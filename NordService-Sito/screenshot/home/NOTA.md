# Nord Service, home finale "Tornano nuove": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (pulizia dello scontorno, immagini, caratteri, screenshot). Parte dal prototipo A, scelto dal giudice, con la prima schermata ripensata (K0 era 7).

Screenshot in questa cartella: `home-1440.jpg` (pagina intera, 4873 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5530 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (chiusura e piede).

## L'idea

Una macchina da lavoro riverniciata, posata sulla linea dei giorni di lavoro. La pala gialla WA320 (foto Sony, l'unica da apertura) sta in piedi su una riga sottile che attraversa tutta la prima schermata come il suolo. Quella riga è un righello di tredici giorni con le date vere della sequenza dell'apripista D8R: 3 ottobre Sabbiato, 10 ottobre Verniciato, 16 ottobre Finito, alle distanze giuste (7 giorni e poi 6, una tacca per giorno). Sotto la ruota posteriore c'è il filetto arancio dell'ultimo giorno. Il titolo "Tornano nuove" viene dal loro "Sappiamo far tornare nuove le macchine". In due secondi si legge: officina che riporta a nuovo, e questo è il percorso. Con il nome di un concorrente la pagina non regge, perché date, macchina e sequenza sono loro.

Cosa è cambiato rispetto al prototipo:
- via le legende Carpenteria e Vetri sulla pala (il segno di Agnoletto, e lavori non confermati su quella macchina);
- titolo più grande (148 px) e alzato in alto a sinistra, senza vuoto sopra;
- scontorno pulito: vetri della cabina in grigio fumé (niente alberi verdi), via il pezzo del tettuccio di un'altra macchina dietro la cabina, ombra rifatta come un'ellisse morbida con le ombre di contatto sotto le tre ruote;
- a 1920 la pala arriva fino al bordo della finestra, senza il taglio dritto a metà pagina.

## Le prime due schermate

1. **Apertura (1440x900)**: testata con il logo vero, tre voci, telefono. A sinistra "Tornano nuove", la riga su cosa fanno e dove ("Carrozzeria per macchine da lavoro: sabbiatura con garnet, fondi e vernici a liquido, vetroresina, carpenteria e vetri. Officina a Mestrino, Padova."), il bottone arancio "Chiama 049 900 5162" e la mail. A destra la pala, grande, sulla linea dei giorni. **A 390**: titolo su due righe, la riga di testo, la pala a tutta larghezza che esce dal bordo destro, la linea dei giorni con le tre date, il bottone. Il telefono è anche nella testata.
2. **Lavorazioni**: "Sulla carrozzeria intera o su un solo pezzo", per chi lavorano, le sei lavorazioni in una griglia 3x2 di solo testo con filetti (a 390 in colonna, il paragrafo d'apertura a tutta larghezza: corretto l'errore di griglia del prototipo). Sotto, a tutta larghezza, la mascheratura in cabina (foto Sony, al posto del mini escavatore fotografato col telefono).

Poi: l'apripista D8R con le tre linguette; la chiusura con la frase del loro titolo, i recapiti, la riga su Stefano e Leonardo Barbieri e la foto delle virole; il piede. "Un lavoro di famiglia" non è più una fascia a parte: sta nella chiusura.

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1: uso commerciale libero, si può incorporare e servire dal proprio sito). Variabile con asse di larghezza, servita da `sito/fonts/` (woff2 latin e latin-ext, presi da Google Fonts). Titolo d'apertura 600 a larghezza 118, titoli di sezione 600 a 108, testo 400 a 100; cifre tabellari per date, orari e telefono. Una sola famiglia. Motivo: le scritte larghe e piene sulle macchine (WA320, D8R) e il logo condensato; la larghezza espansa dà il peso del mezzo senza il nero.
- **Colori** (01-analisi.md, sez. 5): carta #F4F2EE, inchiostro #171717, testo secondario #4A4844, piede #EAE7E1, arancio del logo #EF7821 solo sul bottone, sul filetto del telefono, sull'ultimo giorno della linea e sulla linguetta attiva; #A9500F per i link al passaggio e il fuoco. Contrasti (WCAG): #171717 su #EF7821 6,3:1; #4A4844 su #F4F2EE 8,2:1 e su #EAE7E1 7,4:1; #A9500F su #F4F2EE 4,9:1. Tutti AA.
- **Riferimenti**: Singer Vehicle Design (riportare a nuovo come lusso: una macchina sola, chiara, quasi niente testo), Volvo CE (il mezzo giallo su fondo bianco, menu corto), Hempel (molto vuoto attorno al prodotto vero). Tra le home amate: FM Sistemi chiara (l'oggetto vero e grande, il titolo sicuro, una riga di segni in basso) e Mario Agnoletto chiara, senza però ripeterne le legende.

## Interazione

Un solo gesto, in due punti. Le tre linguette "Sabbiato, Verniciato, Finito" con le date accanto alla foto dell'apripista: al clic o al tocco la foto cambia di colpo, senza dissolvenza, con la sua didascalia. È un `tablist` vero: frecce, Home e Fine da tastiera. Le tre date della linea in apertura sono link alla stessa sezione e aprono direttamente la foto di quel giorno. Nessun'altra animazione; il menu del telefono è un `details` nativo; c'è il link "Vai al contenuto". Collaudato con `_prova/script/finale_controlli.mjs` a 1440 (clic) e a 390 (tocco).

## Foto, origine e licenza

Tutte dell'azienda, scaricate da nordservice.net (vedi `assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessuna foto già usata in un'altra home della campagna.
- `pala-*.webp` (apertura): DSC07377, Sony, maggio 2025 (voti 8/7). Scontorno del prototipo (maschera ISNet, modello Apache 2.0, usato solo per separare la macchina dallo sfondo, corretto a mano), ripulito da `_prova/script/finale_pala.py`: vetri fumé, ombra nuova. Nessun pixel della macchina inventato.
- `mascherata-*.jpg` (fascia): DSC07356, Sony, maggio 2025 (voto 7), taglio 2:1 sulla carta e sul braccio, schiarita.
- `d8r-sabbiato`, `d8r-verniciato`, `d8r-finito` (sequenza): IMG_20241003, IMG_20241010, IMG_20241016, telefono (voti 5-6). Tre quadrati con la base dei cingoli alla stessa altezza; nella foto del 16 ottobre la saturazione del verde del pavimento è al 70 %.
- `virole-*.jpg` (chiusura): DSC07369, Sony, maggio 2025 (voto 7), quadrata e stretta sugli anelli, fuori la targa, il cassone e quasi tutto il cielo bianco.
- `logo-112.png`, `logo-192.png`: logo PNG trasparente con S.R.L., ritagliato, a 2x. Niente SVG ricostruito: il braccio a traliccio della "I" non si ridisegna fedele senza l'originale vettoriale.
Lavorate con PIL (`_prova/script/finale_img.py`), esportate in tre o quattro larghezze con srcset.

## Piede

Logo, una riga su chi sono; colonne Lavorazioni (le sei voci vere), Azienda (Chi siamo, Lavori, Prima e dopo, Contatti), Officina (telefono, mail, indirizzo con mappa, orari), Seguici (solo Instagram: Facebook oggi è un link vuoto). Titoletti 15 px semibold, voci 16 px, "Seguici" sulla griglia. Riga legale: Nord Service S.r.l., P.IVA 04717810289, sede legale a Rubano, Privacy, Cookie. A 390 due colonne per riga, in ordine.
**Niente newsletter**: è un servizio su richiesta per chi possiede o costruisce macchine da lavoro; non hanno notizie, fiere, cataloghi né clienti privati da tenere informati (01-analisi.md, sez. 5 e 8).

## Controlli

- Larghezze 320, 390, 768, 1024, 1440, 1920: nessuno scorrimento orizzontale, nessun testo sovrapposto o fuori finestra (`finale_controlli.mjs`), guardate a pezzi.
- `segnali.sh`: 0 soglie bloccanti. Foto 36,3 %, Archivo 100 %, 9 filetti, nessuna freccia, nessun divieto. Da guardare solo gli H2 di una misura (54 px): voluto, l'unico elemento grande è il titolo d'apertura.
- Nessun carattere U+2014 nella pagina, negli script e nei .md. Nessuna dissolvenza, nessun effetto sul cursore, nessuna icona Lucide, nessun gradiente.
- Altezza a 1440: 4873 px compreso il piede.
