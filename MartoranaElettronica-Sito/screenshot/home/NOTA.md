# Martorana Elettronica, home "Stazioni di collaudo su misura"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, controlli sul sorgente, screenshot, `pro_controlli.mjs`). La versione precedente ("Corretto o scarto", pagina, immagini, screenshot e la sua NOTA) è in `_prova/versione-1-originale/`.

Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). A 320, 768, 1024 e 1920 in `_prova/controlli/`.

## Livello professionale (3/11/2026)

Richieste: "non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" (prima l'uso, poi l'identità, poi l'alta gamma), "ancora troppo poco professionale e di design, e design funzionale all'attività", foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Guardate le prime schermate a 1440 e a 390 di tutti e 14 i riferimenti, le pagine intere di Cly-Del e barth, e la prova su Unicar, Oby e Fornasiero (`_invio/zona/home/livello-professionale.jpg`, colonna di destra).

### Che cosa è cambiato rispetto alla versione 1

- **Titolo.** Via "Corretto o scarto" (un concetto, non il mestiere: la scheda d'uso lo indica tra le cose che sembrerebbero false a loro). Ora l'H1 è la loro frase "Stazioni di collaudo su misura", con l'occhiello "Mestrino (Padova), dal 1973", la loro frase di Chi siamo ("Siamo specializzati nella costruzione di stazioni di collaudo su misura appositamente studiate per velocizzare la produzione in qualsiasi situazione.") e la riga delle sei prove.
- **Colori del marchio.** Via l'alluminio #EEF0EF e il blu #1D5FB8 "di gusto". Ora il blu notte #000072 e il giallo #E4FF00 del logo (letti dai pixel di `LogoUltimo.png`) e il blu degli armadi (#0067C2, un poco più scuro del #0070D0 della foto perché il testo bianco regga AA). Il giallo è un segno (bottoni, occhielli, cifre), mai un fondo, come chiede la scheda.
- **Apertura.** Via il Mod. 1294/P (forse fuori catalogo) e via le legende disegnate. A destra, in un pannello bianco, le due stazioni vere del catalogo 2025 (Mod. 1200 e Mod. 1000), alla misura del file o sotto, appoggiate sulla stessa linea di terra.
- **Assistenza.** Nuova sezione: chiamare, scaricare il loro TeamViewerQS (il file `/download/TeamViewerQS.exe?v=15` del loro sito), email con oggetto e traccia (modello, matricola, foto), area riservata e area download; interventi in azienda e ricambi con un'altra email pronta.
- **Prove.** Via il gesto "Otto prove, un esito" e le descrizioni scritte da noi. Sei schede con la foto della stazione, tutte visibili, con le prove, i modelli e le misure pubbliche (70 mbar e 1200 l/h, 396 cc/h e 0,1 %FS, 120/240/208 V a 60 Hz, da 0,5 a 100 kVA, da 12 a 1000 V a 50, 60 e 100 Hz, DALI, DALI2, DMX512, 0-10 V e 1-10 V); sotto, trasformatori (prova surge), impianti refrigeranti e su misura con le loro frasi; la fascia delle normative; il software (Iridium, MccManager, MccDotNet).
- **Ciò di cui vanno fieri.** "famosa per la velocità e competenza", "fornitori ufficiali delle aziende più prestigiose del settore della saldatura", la stazione degli anni '70 per la Zanussi Grandi Impianti "ancora valida", hardware e software fatti da loro. Il 38% e i nomi dei clienti restano fuori finché non li confermano (LEGGIMI).
- **Inglese.** "EN" in testata porta a un blocco in inglese (prove, normative, 60 Hz, email e assistenza remota). La home ha un solo indirizzo: una pagina inglese completa va fatta con il sito.
- **Via il cestello Unsplash** della chiusura: nessuna foto di repertorio in pagina.
- **Ordine.** Sul telefono, dove arriva il manutentore, dopo l'apertura c'è l'assistenza; sul computer, dove arriva l'ingegnere, ci sono prima le prove (ordine cambiato con il CSS: chi naviga da tastiera sul computer incontra l'assistenza prima delle prove).

Struttura (A1, famiglia M, adattata): testata con Contatti, Area clienti, EN e il telefono; apertura con la dichiarazione di competenza e le stazioni vere; prove e stazioni in schede con la foto; numeri (4); settori e mercati; la loro storia (Zanussi Grandi Impianti, anni '70); richiesta con il modulo M; contatti con la sede e le mappe; piede in 4 colonne. Mancano, perché non ci sono nelle fonti o vanno confermati: progetti con cliente e città, clienti con il nome, certificati.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (sticky) 88 px a 1440 e 72 a 390; bottone giallo "049 9003655" alto 48 px. A 390 e a 1440, a metà pagina, il bottone si vede e si tocca (`elementFromPoint`). 8 link `tel:`, tutti `tel:+390499003655`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 "Stazioni di collaudo su misura", "Mestrino (Padova), dal 1973", sei prove, "Inviateci le specifiche del prodotto" a y 607 e "Chiama 049 9003655"; le due stazioni tutte visibili (401 px). A 390 x 844: lo stesso, "Chiama 049 9003655" a tutta larghezza (350 px) a y 383, "Assistenza su una stazione installata" subito sotto, il link alle specifiche e la fascia delle stazioni (208 px visibili su 208).
3. **Immagine vera nell'apertura: passa, con riserva.** Sono due loro stazioni del catalogo 2025, vere e attuali, ma sono foto su fondo bianco piccole (551 e 417 px di altezza) dentro un pannello bianco: non persone, non il laboratorio, non la sede, che nelle fonti non ci sono (la sola foto della sede, nel banner "NEL SETTORE DA OLTRE 40 ANNI", è impastata e con un cielo disegnato: non usata). Nessuna illustrazione, per scelta del committente. Il servizio fotografico è nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo foto e loghi dell'azienda.
5. **Foto in serie: passa.** Tutte foto loro su bianco, stessa luce piatta da catalogo; tre formati (fila dell'apertura, vetrina 4:3 delle schede, stampa d'archivio); una sola didascalia su 9 foto; nessuna ingrandita oltre la misura del file.
6. **Palette dal marchio: passa.** `--notte` #000072 e `--giallo` #E4FF00 dal logo, `--blu` #0067C2 dagli armadi, più sei neutri freddi. Fondo bianco, nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 24, 32, 48, 72) e 7 a 390 (14, 16, 17, 20, 24, 28, 40); testo corrente 20 e 17 px a 1440, 17 e 16 px a 390; nulla sotto i 14 px (solo occhielli, etichette del modulo e riga legale); H1 72/40, H2 48/28.
8. **Due famiglie al massimo: passa.** Hubot Sans per i titoli e Mona Sans per testo e interfaccia (la stessa famiglia di GitHub in due tagli), pesi 400 e 700.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne (2 a 768, 1 a 390), 6 schede tutte cliccabili, ognuna con la foto della stazione nello stesso riquadro 4:3, il nome, prove, modelli, misure e "Modelli e prove". Le schede portano alle pagine del sito nuovo (elenco nel LEGGIMI).
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono 4 numeri (1973, 4 continenti, 100 kVA, 3 programmi) e la fascia delle normative CEI, EN, VDE, UL, BSI con la didascalia. Le recensioni di Pagine Gialle (media 5,0 su 2) e i clienti citati sul loro sito (Electrolux-Zanussi, De Longhi, Ocean, Merloni Indesit, Air Liquide) sono nelle fonti ma da confermare: nel LEGGIMI, non in pagina.
11. **Lavori con un nome: non passa.** Un solo lavoro con cliente e decennio, la stazione degli anni '70 per la Zanussi Grandi Impianti, con la foto di 202 px: nessun altro lavoro con cliente, anno e dati nelle fonti.
12. **Ritmo a blocchi: passa.** Blu notte (apertura, azienda), blu degli armadi (inglese), grigio chiaro (assistenza, richiesta), bianco (prove, contatti), piede blu notte. Sezioni a 120/120 px a 1440 e 72/72 a 390 (l'apertura 88 sopra); contenitore con margini di 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno giallo con testo blu notte e bordato, raggio 4 px, 52 px (48 in testata), testo 17 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Tipo di richiesta (stazione nuova, assistenza o ricambio, altro), nome, azienda, email, telefono, prodotto, norma, cadenza della linea, prove e valori, alimentazione, disegno, scheda o foto (PDF, DXF, DWG, STEP), messaggio; controllo dei campi obbligatori; compone un'email (mailto), da collegare a un servizio (LEGGIMI). "Apri la mappa" e "Indicazioni stradali" per Via Torino 10/B; nessun iframe.
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA, indirizzo, telefono, email e mappa cliccabili, prove, software, area riservata, Privacy e Cookie. Mancano gli orari e le certificazioni: non sono pubblici e non si scrivono finché l'azienda non li dà.

### Compiti della scheda d'uso (par. 8)

- *A, manutentore a 390*: senza scorrere "Chiama 049 9003655" (52 px, `tel:`) e "Assistenza su una stazione installata"; un tocco porta alla sezione, dove "Scarica TeamViewerQS" è già in vista (y 701 su 844) e punta al loro file; "Scrivete all'assistenza" apre l'email con oggetto "Assistenza: stazione di collaudo installata" e la traccia (modello, matricola, cosa succede, foto); l'area riservata è a due tocchi (Menu, Area clienti; oppure Assistenza, Accedi). Il telefono resta nella testata fissa.
- *B, ingegnere a 1440*: senza scorrere "Stazioni di collaudo su misura", sei prove, "Inviateci le specifiche del prodotto" (email con la traccia) e il telefono; nella seconda schermata le prove per famiglia con modelli e misure (rigidità dielettrica e saldatrici, tenuta e piani cottura a gas, con modello e numero, tutto visibile senza toccare); foto vere del catalogo 2025; l'elenco di cosa mandare accanto al modulo.
- *C, estero*: "EN" in testata a 1440 e a 390; il blocco in inglese ha normative (UL, VDE, BSI), 60 Hz, l'email con la traccia in inglese e l'assistenza remota.
- *Tutti*: Via Torino 10/B (sede operativa), mappa e indicazioni con un tocco; nessun orario in pagina.

### Caratteri e licenze

- **Hubot Sans** e **Mona Sans** (GitHub), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; serviti dalla pagina (`sito/fonts/*.woff2`, latin e latin-ext), licenza in `sito/fonts/OFL.txt`. Le cifre dei titoli vengono da Mona Sans (lo zero di Hubot è barrato). Tenuti dalla versione 1: sono due tagli di una famiglia e somigliano alle scritte serigrafate dei loro pannelli.

### Foto

Solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso; elenco in `assets/CREDITI.md`. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-9 e 12-14 superate nelle misure; 10, 11 e 15 no (vedi sopra). Nessuna ancora senza destinazione, nessun errore di script.
- Prove d'uso nello stesso script: tocco su "Assistenza" a 390 (TeamViewerQS in vista), menu aperto e chiuso dopo una voce, modulo vuoto fermato con l'avviso e il fuoco sul nome, email composta e letta senza inviarla.
- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura e in testata; nessun testo che esce da schede, passi e bottoni.
- Screenshot guardati a pezzi a 1440 e a 390 (prime schermate e pagine intere) e confrontati con Cly-Del, barth e la prova su Unicar; parti alte a 320, 768 e 1024.
- Collegamenti: `tel:+390499003655`; `mailto:martorana@martoranaelettronica.com` con 5 oggetti diversi; Google Maps (ricerca e indicazioni) per Via Torino 10/B, 35035 Mestrino; TeamViewerQS, area riservata e area download sul loro sito.
- Nessun U+2014 in pagina, nei .md e negli script.
