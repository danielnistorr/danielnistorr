# Martorana Elettronica, home "Stazioni di collaudo su misura"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, controlli sul sorgente, screenshot, `pro_controlli.mjs`). La versione precedente ("Corretto o scarto", pagina, immagini, screenshot e la sua NOTA) è in `_prova/versione-1-originale/`.

Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). A 320, 768, 1024 e 1920 in `_prova/controlli/`.

## Livello professionale (3/11/2026)

Richieste: "non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" (prima l'uso, poi l'identità, poi l'alta gamma), "ancora troppo poco professionale e di design, e design funzionale all'attività", foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Guardate le prime schermate a 1440 e a 390 di tutti e 14 i riferimenti, le pagine intere di Cly-Del e barth, e la prova su Unicar, Oby e Fornasiero (`_invio/zona/home/livello-professionale.jpg`, colonna di destra).

### Che cosa è cambiato rispetto alla versione 1

- **Titolo.** Via "Corretto o scarto" (un concetto, non il mestiere: la scheda d'uso lo indica tra le cose che sembrerebbero false a loro). Ora l'H1 è la loro frase "Stazioni di collaudo su misura", con l'occhiello "Mestrino (Padova), dal 1973", la loro frase di Chi siamo ("Siamo specializzati nella costruzione di stazioni di collaudo su misura appositamente studiate per velocizzare la produzione in qualsiasi situazione.") e la riga delle sei prove.
- **Colori del marchio.** Via l'alluminio #EEF0EF e il blu #1D5FB8 "di gusto". Ora il blu notte #000072 e il giallo #E4FF00 del logo (letti dai pixel di `LogoUltimo.png`) e il blu degli armadi (#0067C2, un poco più scuro del #0070D0 della foto perché il testo bianco regga AA). Il giallo è un segno (bottoni, occhielli, cifre), mai un fondo, come chiede la scheda.
- **Apertura.** Via il Mod. 1294/P (forse fuori catalogo) e via le legende disegnate. Nel ritocco finale anche via il pannello bianco con le due stazioni: apertura tipografica con l'indice delle prove (vedi sotto).
- **Assistenza.** Nuova sezione: chiamare, scaricare il loro TeamViewerQS (il file `/download/TeamViewerQS.exe?v=15` del loro sito), email con oggetto e traccia (modello, matricola, foto), area riservata e area download; interventi in azienda e ricambi con un'altra email pronta.
- **Prove.** Via il gesto "Otto prove, un esito" e le descrizioni scritte da noi. Sei schede con la foto della stazione, tutte visibili, con le prove, i modelli e le misure pubbliche (70 mbar e 1200 l/h, 396 cc/h e 0,1 %FS, 120/240/208 V a 60 Hz, da 0,5 a 100 kVA, da 12 a 1000 V a 50, 60 e 100 Hz, DALI, DALI2, DMX512, 0-10 V e 1-10 V); sotto, trasformatori (prova surge), impianti refrigeranti e su misura con le loro frasi; la fascia delle normative; il software (Iridium, MccManager, MccDotNet).
- **Ciò di cui vanno fieri.** "famosa per la velocità e competenza", "fornitori ufficiali delle aziende più prestigiose del settore della saldatura", la stazione degli anni '70 per la Zanussi Grandi Impianti "ancora valida", hardware e software fatti da loro. Il 38% e i nomi dei clienti restano fuori finché non li confermano (LEGGIMI).
- **Inglese.** "EN" in testata porta a un blocco in inglese (prove, normative, 60 Hz, email e assistenza remota). La home ha un solo indirizzo: una pagina inglese completa va fatta con il sito.
- **Via il cestello Unsplash** della chiusura: nessuna foto di repertorio in pagina.
- **Ordine.** (ritocco finale: ordine unico nel sorgente, apertura, prove, software, assistenza, senza `order` nel CSS).

Struttura (A1, famiglia M, adattata): testata con Contatti, Area clienti, EN e il telefono; apertura con la dichiarazione di competenza e l'indice delle prove; prove e stazioni in schede con la foto; numeri (4); settori e mercati; la loro storia (Zanussi Grandi Impianti, anni '70); richiesta con il modulo M; contatti con la sede e le mappe; piede in 4 colonne. Mancano, perché non ci sono nelle fonti o vanno confermati: progetti con cliente e città, clienti con il nome, certificati.

### Ritocco finale (3/11/2026, dopo il controllore del livello professionale, voto 6)

Difetti del controllore e dei due clienti tipo, che cosa è stato fatto:
- **Apertura (bloccante).** Tolto il riquadro bianco con il Mod. 1200 e il Mod. 1000 scontornati (difetto B2). L'apertura ora è solo tipografia sul blu notte, come barth e Holzrausch: occhiello "Mestrino (Padova), dal 1973", H1 "Stazioni di collaudo su misura" su una riga a 72 px, la loro frase di Chi siamo con i due bottoni accanto, e sotto l'**indice delle sei prove** (numero in giallo, nome in Hubot 32 px, una riga di fatti, filetti chiari). Ogni voce porta alla sua scheda: è il gesto di scala e dice subito all'ingegnere se fanno la sua prova. A 390 l'indice è un elenco da toccare (righe di 52 px) subito sotto "Chiama" e "Assistenza".
- **Le due stazioni** sono diventate la scheda grande "Sicurezza elettrica in linea" (due colonne su tre, su bianco, alla misura del file), dentro le prove.
- **Numeri.** Via "3 programmi" e "100 kVA" (specifica di prodotto, resta nella scheda Alimentatori). Ora: 1973 (fondazione), 50+ ("a più di cinquant'anni"), 4 continenti all'estero, 5 normative di prova.
- **Schede delle prove.** Via i paragrafi descrittivi: ogni scheda ha nome, una riga di prove e le misure in grassetto. Foto tutte entro la stessa altezza (al massimo 200 px, riquadro 16:10). La serie /NET ha la sua scheda; trasformatori, impianti refrigeranti e su misura sono una scheda "Anche" con tre voci tutte cliccabili. A 390 foto e testo stanno affiancati (miniatura di 112 px) e la riga delle prove è nascosta: la sezione è circa la metà di prima.
- **Saldatrici.** Aggiunti i moduli Mod. 0586 per prova di rigidità, di terra e di dispersione (dai loro collage) e "valori su specifica del cliente", perché i valori non sono pubblici.
- **Software e normative** in un blocco proprio sul blu degli armadi ("Fatti da noi", Iridium, MccDotNet), con CEI EN VDE UL BSI a 72 px su tutta la larghezza: spezza il bianco delle prove.
- **Giallo meno esteso.** Il bottone pieno è blu notte con testo bianco in testata e sulle sezioni chiare; il giallo resta su apertura, azienda e inglese (bottone principale, occhielli, cifre) e come filetto di 4 px in cima alla testata.
- **Ordine.** Tolto l'`order` del CSS: sorgente e schermo hanno lo stesso ordine (apertura, prove, software, assistenza...), il fuoco da tastiera segue la pagina. A 390 l'assistenza resta a un tocco dal bottone in apertura e dal menu.
- **Assistenza.** Link in https (TeamViewerQS, area riservata, area download: rispondono 200). Sotto il passo 2 l'indirizzo da scrivere sul PC della stazione (Windows, circa 30 MB). Interventi e ricambi sono una fascia con il bottone "Chiedi intervento o ricambio" e il numero cliccabile. A 390 si vede la frase corta "Errore, scarti, taratura o ricambio".
- **Modulo.** Il selettore nativo "Choose Files" è sostituito da un bottone bordato "Scegli i file" del sistema dei bottoni, con i nomi scelti accanto e la nota che vanno allegati all'email che si apre.
- **Collegamenti.** Le schede e il piede portano alle pagine di oggi del loro sito (prodotti, sicurezza elettrica, tenuta e portata, saldature, alimentatori, softwares, chi-siamo, cookies-policy, tutte in https e con risposta 200), non più a pagine che non esistono.
- **Dettagli.** Archivio anni '70 senza fondo bianco, con filetto e didascalia "Zanussi Grandi Impianti, anni Settanta"; logo a 120 px a 390 con il menu a icona (etichetta "Apri il menu"); via la frase riempitiva di "Dove siamo"; un solo spazio tra "Chiama" e il numero.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa (sticky); bottone blu notte "049 9003655" alto 48 px; a metà pagina, a 390 e a 1440, si vede e si tocca (`elementFromPoint`). 9 link `tel:`, tutti `tel:+390499003655`. In testata anche Area clienti, Contatti ed EN.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1, "Mestrino (Padova), dal 1973", la frase loro, "Inviateci le specifiche del prodotto" a y 313, "Chiama 049 9003655" e le sei prove dell'indice. A 390 x 844: H1, occhiello, "Chiama 049 9003655" largo 350 su 350 a y 286, "Assistenza su una stazione installata", il link alle specifiche e cinque prove dell'indice. La prova resta solo "dal 1973": non ci sono cifre pubbliche più forti.
3. **Immagine vera nell'apertura: non passa, per scelta.** Niente più oggetto scontornato su fondo chiaro. Persone, laboratorio e sede non ci sono nelle fonti e il committente ha escluso i disegni, quindi l'apertura è di sola tipografia (A7, "una home fatta di tipografia", barth e Holzrausch). La foto del laboratorio con le persone è la prima del servizio fotografico nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` 0 volte; in `sito/img/` solo foto e loghi dell'azienda.
5. **Foto in serie: passa.** 9 foto, tutte loro su bianco; 3 formati (fila della scheda grande, vetrina 16:10, stampa d'archivio); 1 didascalia; nessuna mostrata oltre la misura del file.
6. **Palette dal marchio: passa.** `--notte` #000072 e `--giallo` #E4FF00 dal logo, `--blu` #0067C2 dagli armadi, più i neutri freddi; fondo bianco, nessun beige. Il giallo è usato su meno superficie.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 24, 32, 48, 72) e 7 a 390 (14, 16, 17, 20, 24, 28, 40); testo corrente 20 e 17 px a 1440, 17 e 16 px a 390; nulla sotto i 14 px; H1 72/40, H2 48/28.
8. **Due famiglie al massimo: passa.** Hubot Sans per titoli, indice, cifre e normative; Mona Sans per testo e interfaccia; pesi 400 e 700. Il bottone nativo del file non c'è più.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne (2 a 768, 1 a 390): 7 schede con foto, tutte cliccabili, con nome, prove, misure e "Modelli e prove", più la scheda "Anche" a tre voci cliccabili. I link portano alle pagine prodotti di oggi.
10. **Almeno tre tipi di prova: non passa (2 su 4).** 4 numeri aziendali (1973, 50+, 4 continenti, 5 normative) e la fascia delle normative di prova con la didascalia. Recensioni, clienti con il nome e certificazioni sono da confermare o non esistono: nel LEGGIMI, non in pagina.
11. **Lavori con un nome: non passa.** Un solo lavoro con cliente e decennio (Zanussi Grandi Impianti, anni '70), con la stampa d'archivio alla sua misura di 202 px. Nelle fonti non ce ne sono altri.
12. **Ritmo a blocchi: passa.** Blu notte (apertura, azienda), blu degli armadi (software e normative, inglese), grigio chiaro (assistenza, richiesta), bianco (prove, contatti), piede blu notte. Sezioni a 120/120 px a 1440 e 72/72 a 390 (assistenza 64 sopra); margini 80 px a 1440 e 20 a 390. Pagina alta 9311 px a 1440 e 13642 a 390 (prima 14411).
13. **Un solo sistema di bottoni: passa.** Pieno (blu notte sul chiaro, giallo sullo scuro) e bordato, raggio 4 px, 52 px (48 in testata), testo 17 px (16 in testata a 390); tutti i bottoni di chiamata contengono il numero; anche "Scegli i file" è un bottone del sistema.
14. **Modulo e "dove" per il mestiere: passa.** Tipo di richiesta, nome, azienda, email, telefono, prodotto, norma, cadenza, prove e valori, alimentazione, disegno, scheda o foto (PDF, DXF, DWG, STEP), messaggio; compone un'email (mailto), da collegare a un servizio (LEGGIMI). "Apri la mappa" e "Indicazioni stradali"; nessun iframe.
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA, sede, telefono, email e mappa cliccabili, prodotti, software, area riservata, Cookies policy. Mancano orari e certificazioni, che non sono pubblici.

### Compiti della scheda d'uso (par. 8)

- *A, manutentore a 390*: senza scorrere "Chiama 049 9003655" (52 px, `tel:`) e "Assistenza su una stazione installata"; un tocco porta alla sezione, dove "Scarica TeamViewerQS" è già in vista (y 697 su 844, prima 701), punta al loro file in https e sopra c'è l'indirizzo da scrivere sul PC della stazione; "Scrivete all'assistenza" apre l'email con oggetto "Assistenza: stazione di collaudo installata" e la traccia (modello, matricola, cosa succede, foto); l'area riservata è a due tocchi (Menu, Area clienti; oppure Assistenza, Accedi). Interventi e ricambi hanno un bottone proprio con l'email pronta. Il telefono resta nella testata fissa. Attrito rimasto: "Scrivete all'assistenza" è a y 966, uno scorrimento corto come prima.
- *B, ingegnere a 1440*: senza scorrere "Stazioni di collaudo su misura", l'indice delle sei prove con una riga di fatti ciascuna (un clic porta alla scheda), "Inviateci le specifiche del prodotto" (email con la traccia) e il telefono; nella seconda schermata le prove per famiglia con modelli e misure (rigidità dielettrica e saldatrici, tenuta e piani cottura a gas, con modello e numero, tutto visibile senza toccare); le saldatrici ora dicono quali prove (moduli 0586 di rigidità, terra e dispersione); foto vere del catalogo 2025 (Mod. 1200 e Mod. 1000 nella scheda grande); i link "Modelli e prove" aprono le pagine prodotti di oggi; l'elenco di cosa mandare accanto al modulo.
- *C, estero*: "EN" in testata a 1440 e a 390; il blocco in inglese ha normative (UL, VDE, BSI), 60 Hz, l'email con la traccia in inglese e l'assistenza remota.
- *Tutti*: Via Torino 10/B (sede operativa), mappa e indicazioni con un tocco; nessun orario in pagina.

### Caratteri e licenze

- **Hubot Sans** e **Mona Sans** (GitHub), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; serviti dalla pagina (`sito/fonts/*.woff2`, latin e latin-ext), licenza in `sito/fonts/OFL.txt`. Le cifre dei titoli vengono da Mona Sans (lo zero di Hubot è barrato). Tenuti dalla versione 1: sono due tagli di una famiglia e somigliano alle scritte serigrafate dei loro pannelli.

### Foto

Solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso; elenco in `assets/CREDITI.md`. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs` (ritocco finale): regole 1, 2, 4-9 e 12-14 superate nelle misure; 3 no per scelta (apertura senza immagine), 10, 11 e 15 no per dati che mancano (vedi sopra). Nessuna ancora senza destinazione, nessun errore di script.
- Prove d'uso nello stesso script: tocco su "Assistenza" a 390 (TeamViewerQS in vista), menu aperto e chiuso dopo una voce, modulo vuoto fermato con l'avviso e il fuoco sul nome, email composta e letta senza inviarla.
- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura e in testata; nessun testo che esce da schede, passi e bottoni.
- Screenshot guardati a pezzi a 1440 e a 390 (prime schermate e pagine intere) e confrontati con le prime schermate dei 14 riferimenti e con le pagine intere di barth e Cly-Del; parti alte a 320, 768 e 1024.
- Nessun `order` nel CSS: l'ordine del fuoco da tastiera è quello della pagina.
- Collegamenti: `tel:+390499003655`; `mailto:martorana@martoranaelettronica.com` con 5 oggetti diversi; Google Maps (ricerca e indicazioni) per Via Torino 10/B, 35035 Mestrino; TeamViewerQS, area riservata, area download e le pagine prodotti, softwares, chi-siamo e cookies-policy del loro sito, tutte in https (risposta 200 il 3/11/2026).
- Nessun U+2014 in pagina, nei .md e negli script.
