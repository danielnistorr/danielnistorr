# Poli-Art: proposta di nuova homepage

Proposta non richiesta, solo la home. Nessun contatto con l'azienda, niente pubblicato.

- **Pagina**: `sito/index.html` (statica; immagini in `sito/img/`, carattere e licenza in `sito/fonts/`). Versione "livello professionale" del 3/11/2026.
- **Screenshot e nota**: `screenshot/home/` (`NOTA.md`: struttura, le 15 regole una per una, i compiti dei visitatori, caratteri, foto e controlli).
- **Rifare tutto**: `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `pro_index.html`, screenshot con `pro_shot.mjs` e `pro_jpeg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).
- **Versione precedente** ("Grezzo e finito", con la testa cromata): copiata com'era in `_prova/versione-1-originale/`; i suoi script sono `_prova/script/finale_*`.
- **Analisi e fonti**: `01-analisi.md`; scheda d'identità e d'uso: `_prova/uso/SCHEDA.md`.

## Il modulo di contatto va collegato a un servizio

Oggi il modulo "Richiesta di preventivo" non invia nulla: controlla nome, email e telefono e poi **compone un'email** (`mailto:info@poli-art.it` con oggetto "Preventivo: <lavoro> (<azienda>)" e tutti i campi) nel programma di posta di chi lo compila. Un mailto non porta allegati: il file 3D, il disegno o le foto si aggiungono nell'email che si apre, ed è scritto sopra il modulo.

Sul sito vero va collegato a un servizio che riceva anche gli allegati (per esempio il modulo di WordPress che hanno già, Gravity Forms, con un campo "carica file" per STEP, STL, DXF, PDF, JPG e un limite di misura), con l'informativa privacy accanto al bottone e la casella del consenso. Il bottone "Mandaci il disegno" può restare un mailto.

## Dati da confermare prima di pubblicare

In pagina c'è solo ciò che è verificato o scritto da loro; quello che segue è dubbio e va chiesto.

1. **Partita IVA 03796810244**: viene da un aggregatore (informazione-aziende.it, dati iCribis), cifra di controllo valida, ufficio di Vicenza. Va confermata con la visura, insieme a REA e PEC (non trovati). Oggi sul sito la P.IVA manca, ed è obbligatoria.
2. **"Impresa individuale"** nella riga legale: da informazione-aziende.it.
3. **Il 1986** (nel titolo, nella fascia dei fatti e nel piede): il sito dice "L'Azienda nasce nel 1986", ma la P.IVA di Manuel ha 11-20 anni; la stessa sede era registrata come "Poli - Art Di Gregori Franca". Si può scrivere "dal 1986"? Se sì, si può aggiungere "40 anni"?
4. **Indirizzo**: via Tesinella 7, 7/A o 7/A/9 (la mappa oggi usa "Via Tesinella 7").
5. **Orari**: solo da un aggregatore (lun-ven 8-12 e 14.30-18), quindi **non in pagina** (in "Dove siamo" c'è "Per passare in laboratorio, telefonate prima"). Se confermati, vanno sotto l'indirizzo e nel piede, in tabella. Chiedere anche se si può **ritirare in sede**.
6. **WhatsApp**: hanno un cellulare per ricevere foto dal cantiere? Se sì, un bottone "WhatsApp" accanto a "Chiama" sul telefono.
7. **Formati dei file e misura massima del blocco**: quali file accettano (STEP, STL, DXF, DWG, PDF?), quanto è grande il blocco più grande che lavorano, quanti pantografi CNC, filo caldo o fresa, quali stampanti 3D. Con queste risposte la frase "Formati dei file e misure massime: chiedetecele al telefono" diventa una riga di fatti nel blocco del progetto.
8. **Tempi e consegna**: tempi tipici; consegnano o montano in fiera? Oggi la pagina non dice nulla.
9. **Resinatura e verniciatura**: interne o affidate fuori? La fascia dei fatti dice "con trattamenti plastici e resinature", parole loro.
10. **Imballaggio e grafica adesiva** (citati da una vecchia scheda): li fanno ancora?

## Le prove che mancano (regole 10, 11 e 15)

Le regole chiedono almeno tre tipi di prova e almeno tre lavori con un nome. Oggi in pagina ci sono solo i fatti del mestiere e il 1986; niente è stato inventato. Da chiedere:

1. **Numeri aziendali** (da 4 a 8): anni di attività, persone in laboratorio, metri quadri del laboratorio, misura massima lavorabile, pezzi o commesse l'anno, fiere servite. Vanno nella fascia blu al posto di EPS, CNC e 3D.
2. **Clienti con il nome**: nelle foto si vedono Longo (la bottiglia in fiera, `Vino1`), mosaico+ (lo stand, `Oggetti2`), Converse (la scarpa, `Scarpa-converse1` e `-3`), e nell'archivio Paul & Shark, Blauer, ASUS, Busatta, Sterilgarda, Bertolo, Taplast, Carlo Gavazzi, Pietrarredo, Leodari 75. Quali si possono **mostrare** (le foto in pagina lo fanno già, e vanno autorizzate) e quali si possono **nominare** in una fascia "Hanno lavorato con noi"?
3. **Tre lavori con cliente, luogo e anno** e 2-3 dati (misura, tempo, numero di pezzi): per esempio la bottiglia Longo (fiera, anno, altezza), il pallone abitabile (mostra, anno, diametro), il cornicione in cantiere (comune, anno, metri lineari). Vanno in una sezione "Lavori" con foto larga.
4. **Recensioni**: non ne ho trovate di leggibili (Google Maps, Pagine Gialle, Facebook bloccati). Se hanno recensioni Google o lettere di clienti, tre con nome e comune.
5. **Certificazioni o fornitori** (EPS ad alta densità di quale produttore, resine): una fascia con la didascalia.

## Foto in pagina: permessi

1. **Il pallone abitabile** (apertura, `Pallone1`): è un lavoro loro, per quale mostra? La persona accanto (forse Manuel) acconsente a comparire?
2. **La bottiglia con lo schizzo di vino** (`Vino1`, stand Longo): permesso del cliente.
3. **Lo stand mosaico+** (`Oggetti2`, scheda "Prototipi e mockup"): è un mockup in senso loro ("riproposto in dimensioni più grandi")? Permesso del cliente. Se non è giusto per la scheda, la foto cambia.
4. **La scarpa** (`Scarpa-converse3` e `-1`): il foglio accanto al pezzo bianco è il disegno del cliente? Permesso di Converse o del negozio.
5. **Il cornicione** (`IMG_20190531_181254...`): dove, per quale impresa, se si può dire.
6. **Il soffitto a cassettoni** (`CorniciORO2`, scheda "Scenografie") e **il ponte di Rialto** (`Pasticceria`, scheda "Torte finte e stampa 3D"): per chi e per che cosa; il Rialto è una decorazione per pasticceria?
7. **Il laboratorio** (`Fotovoltaico-working`): le due persone acconsentono? È il laboratorio di via Tesinella?

## Foto da rifare dal vero

La qualità di oggi è da telefono o da compatta (media 4,6 su 10), con luci diverse. Un fotografo, una giornata, la stessa luce per tutto:

1. **Apertura**: un pezzo fuori scala finito, senza marchio, con Manuel accanto che lo guarda (non l'obiettivo), in laboratorio o in un capannone pulito; inquadratura frontale all'altezza degli occhi, 4:5 e 16:9 dallo stesso punto.
2. **Il laboratorio al lavoro** (mezza giornata): il pantografo o il filo caldo che taglia il blocco, le mani che rifiniscono, la resinatura, i trucioli bianchi; luce del capannone più una lampada continua, niente pavimento arancio in primo piano. Serve per "Il laboratorio" e per le mani nella sezione del progetto.
3. **Una foto per scheda**, tutte 4:3, con la stessa luce: un cornicione o una cornice di finestra posati (in cantiere, cielo coperto, senza ponteggio davanti), un cassero blu pulito, una lettera in volume, un pezzo stampato in 3D, una torta finta, uno stand o una vetrina finiti con il permesso del cliente.
4. **La sequenza dal disegno al pezzo**: lo stesso oggetto fotografato dallo stesso punto in tre momenti (disegno o file a schermo, pezzo bianco appena fresato, pezzo finito), per il blocco "Come mandarci il progetto".
5. **La sede**: l'ingresso di via Tesinella 7 con l'insegna, per "Dove siamo", così chi arriva la riconosce.

## Pagine collegate

Le sei schede e il piede portano alle pagine di oggi su poli-art.it (`mockup/`, `edilizia/`, `scenografie/`, `loghistica/`, `prototipi-personalizzati-di-alta-qualita/`, `cake-design/`, `stampa-3d/`, `realizzazioni/`). Quando il sito nuovo avrà le sue pagine (per esempio `fiere-e-vetrine/`, `edilizia/`, `scenografie/`, `lettere-e-loghi/`, `prototipi-e-mockup/`, `torte-finte/`, `stampa-3d/`, `lavori/`), i link vanno cambiati. Mancano le pagine `privacy.html` e `cookie.html` (oggi `privacy-policy/` dà 404 e Google Analytics parte senza consenso): servono i testi.

Altre domande ancora aperte dalla versione precedente: la collaborazione con Palloncini WOW è attiva? Instagram e Facebook sono attivi (il piede li mostra)? Tenere il nome "Loghistica" o "Lettere e loghi in volume" (in pagina c'è il secondo)?

**Niente newsletter**: lavorano su commessa e non hanno notizie, cataloghi o fiere proprie da comunicare; per i clienti privati basta Instagram.

## Licenze

- **Carattere**: Mona Sans (GitHub Next), da Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file woff2 serviti dalla pagina (`sito/fonts/`, copia in `assets/fonts/`), licenza in `sito/fonts/OFL.txt`.
- **Foto in pagina**: tutte di Poli-Art, dalla libreria media del loro sito (`assets/originali/`); da usare solo con il loro consenso. Nessuna foto di repertorio, nessuna immagine generata dall'IA, nessun disegno al posto delle foto. Le foto scaricate in `assets/esterne/` (licenze in `assets/CREDITI.md`) **non sono usate**.
- **Logo**: PNG del sito (`logo-blu-1815x400.png` per la testata, `logo-bianco-1815x400.png` per il piede scuro), ritagliati e ridotti a 300 e 600 px; non ricostruiti in SVG. Per il sito vero conviene chiedere il file vettoriale.
