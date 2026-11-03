# Home Poli-Art, livello professionale (3/11/2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere e licenza in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `pro_index.html`, screenshot con `pro_shot.mjs` e `pro_jpeg.py`, controlli con `pro_controlli.mjs`). La versione precedente ("Grezzo e finito", con la testa cromata) è copiata com'era in `_prova/versione-1-originale/` (pagina, immagini e screenshot).

Altezza: 7251 px a 1440, 10916 a 390.

File in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (la sezione "Dove siamo" con il modulo). I due `*-grezzo.jpg` non ci sono più: lo stato "Grezzo" della legenda non esiste in questa versione (restano nella copia della versione 1).

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Criterio: prima l'uso, poi l'identità, poi l'esecuzione. Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14; le pagine intere di barth e Cly-Del (più Budri). Da barth: il blocco "in Zahlen" e la pagina a blocchi pieni; da Cly-Del: la dichiarazione di competenza a sinistra con l'immagine a destra, i blocchi alterni chiaro, scuro e colore, il piede scuro a quattro colonne.

### Che cosa è cambiato rispetto alla versione 1

La versione 1 non aveva ancora l'uso della scheda: apriva con la testa cromata (non si sa se è opera loro, e il grezzo era specchiato), il titolo spezzato "Polistirolo scolpito / e rifinito", il telefono come testo piccolo, nessun "manda il disegno", l'edilizia in quarta casella con le cornici dorate, il cantiere di altri (`Pawson3`), la chaise longue presentata come prototipo, fondo beige #F5F4F1 per tutta la pagina. Tutto questo è uscito.

Struttura, adattata dalla A1 della famiglia M:

1. **Testata fissa** (88 px, 72 sul telefono): logo vero, quattro voci con le parole del cliente (Cosa facciamo, Come mandarci il progetto, Laboratorio, Dove siamo), il telefono come bottone bordato "0444 614719" e il bottone pieno "Mandaci il disegno" (email con oggetto e traccia). Sotto i 1200 px le voci vanno nel bottone "Menu"; sotto i 900 resta solo il telefono.
2. **Apertura** (bianca): occhiello "Poli-Art · Grisignano di Zocco (VI)", titolo della scheda "Lavorazione del polistirolo dal 1986" (le loro parole: "Lavorazione del polistirolo", "dal 1986"), la loro frase "qualsiasi richiesta plastico decorativa in polistirolo espanso ad alta densità" con la macchina e la mano, i due bottoni, la riga "File 3D, disegno o foto con le misure. Se manca il 3D, provvediamo noi all'elaborazione del solido virtuale", e la riga dei lavori come li cerca il cliente (8 voci toccabili, alte 44 px, che portano alla scheda giusta). A destra **il pallone abitabile con la persona accanto** (`Pallone1`), ritagliato senza striscione e senza i pannelli della mostra.
3. **Cosa facciamo** (fondo grigio azzurro chiaro): sei schede in tre colonne, foto vera 4:3 per tutte, nome, una riga con le loro parole, "Vedi..."; tutta la scheda è un link alla loro pagina di oggi su poli-art.it. Ordine: Fiere e vetrine, **Edilizia e casseri subito dopo** (cornicione vero in cantiere), Scenografie, Lettere e loghi in volume, Prototipi e mockup, Torte finte e stampa 3D. Sotto, "Tutti i lavori, circa 140 foto" (la galleria `realizzazioni/`) e Instagram.
4. **Come mandarci il progetto** (blocco blu notte): "Tutto inizia con un progetto" (loro), tre modi (file 3D, disegno o foto con le misure, "lo disegniamo noi" con la loro frase sul solido virtuale), la coppia vera della scarpa (il disegno del cliente accanto al pezzo bianco, poi il finito in negozio), i due bottoni e "Formati dei file e misure massime: chiedetecele al telefono".
5. **Il laboratorio** (bianco): "Controllo numerico, poi la mano", l'unica foto loro del lavoro in corso (`Fotovoltaico-working`: la scocca sul pantografo, due persone che rifiniscono), le loro frasi sulla macchina, la mano, le resinature e "a prova di curiosi", e il manifesto in grande: "Essendo un mercato di nicchia l'esperienza ed il know-how maturato negli anni imperano per la riuscita di un buon prodotto."
6. **I fatti** (fascia nel blu del logo): 1986, EPS, CNC, 3D in cifre da 64 px con l'etichetta sotto. È il gesto di scala della pagina.
7. **Dove siamo**: il telefono a 64 px, email, laboratorio con "Apri la mappa" e "Indicazioni stradali" (Google Maps), "Per passare in laboratorio, telefonate prima", Instagram; a destra il modulo di preventivo.
8. **Piede** blu notte a quattro colonne.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `position:fixed`, bottone "0444 614719" alto 48 px; a metà pagina, a 1440 e a 390, il bottone si vede e si tocca (`elementFromPoint`). 5 link `tel:`, tutti `tel:+390444614719`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: H1 con "polistirolo", "Grisignano di Zocco" nell'occhiello, "dal 1986" nel titolo, "Mandaci il disegno" e "Chiama 0444 614719" a 458 px, foto intera (604 px). A 390 x 844: lo stesso, i due bottoni a tutta larghezza (350 px su 350), alti 56 px, a 234 e 302 px, le 8 voci dei lavori tutte visibili, la foto che comincia a 712 px.
3. **Immagine vera nell'apertura: passa.** Un pezzo fuori scala loro, con la persona accanto che dà la misura, nel suo ambiente (non scontornato). Resta una foto da fiera fatta con una compatta: va rifatta (LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo foto loro e il logo. Nessuna immagine di `assets/esterne/`, nessun disegno.
5. **Foto in serie: passa, con riserva.** Un solo trattamento per tutte (`pro_img.py`: bianco portato verso il neutro al 35 %, contrasto con taglio 0,4 %, saturazione 0,9, nitidezza leggera); tre formati a 1440 (apertura circa 1:1 da un ritaglio 5:4, schede e coppia 4:3, laboratorio 16:9); 2 didascalie su 10 foto; nessuna foto ingrandita oltre la misura d'origine. La riserva: sono scatti di anni e macchine diverse, e la luce non è la stessa (fiera, cantiere al sole, laboratorio al neon).
6. **Palette dal marchio: passa.** `--ardesia` #5F708E (il blu del logo), `--ardesia-scuro` #4E5F7D (bottoni, link, fascia dei fatti), `--notte` #1C2330 (blocco scuro e piede, lo stesso blu quasi nero); neutri freddi (bianco, #EDF0F4, filetti, grigi). Fondo bianco, niente beige: il bianco caldo della versione 1 era il fondo di comodo che le regole vietano.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 19, 23, 32, 44, 64) e 7 a 390 (14, 16, 17, 20, 26, 30, 38); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px (14 solo per occhielli maiuscoli spaziati e riga legale); H1 64 / 38, H2 44 / 30, nella fascia della famiglia M.
8. **Due famiglie al massimo: passa.** Una sola, Mona Sans (come la versione 1), ora alla larghezza normale (100 %, non più 118 % "da galleria") e in due pesi, 400 e 700.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne (2 a 768, 1 a 390), sei schede, stessa foto 4:3, nome, riga, link; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa (1 su 4, e parziale).** C'è la fascia dei fatti, ma l'unico numero aziendale vero è il 1986; EPS, CNC e 3D sono fatti del mestiere detti dalle loro pagine. Mancano recensioni (nessuna leggibile, SCHEDA par. 1), certificazioni (nessuna nota), clienti con il nome (i marchi si vedono solo nelle foto e vanno autorizzati). Nulla è stato inventato; cosa chiedere è nel LEGGIMI.
11. **Lavori con un nome: non passa.** Le fonti non danno cliente, luogo e anno di nessun lavoro. La coppia della scarpa racconta il passaggio dal disegno al finito senza nomi. Da chiedere (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: "Come mandarci il progetto" in blu notte e la fascia dei fatti nel blu del logo; "Cosa facciamo" in grigio azzurro, il resto bianco. Spazio tra le sezioni 120 px a 1440 (96 la fascia dei fatti) e 72 a 390; margini 80 px a 1440 (contenitore 1280) e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno (blu ardesia; bianco sul blu notte) e bordato, raggio 4 px ovunque, 56 px (48 in testata), testo 17 px (16 in testata sul telefono); tutti i bottoni di chiamata contengono "0444 614719".
14. **Modulo e "dove" per il mestiere: passa.** Campi della famiglia M: nome, azienda, email, telefono, lavoro (9 voci), misure e quantità, data di consegna o dell'evento, "Cosa allegherete" (file 3D, disegno, foto con le misure, niente), messaggio. Il modulo controlla nome, email e telefono (avviso e fuoco sul primo campo vuoto), poi compone l'email con oggetto "Preventivo: <lavoro> (<azienda>)" e tutti i campi; l'allegato si aggiunge nell'email che si apre (un mailto non porta file): è detto sopra il modulo. Indirizzo con "Apri la mappa" e "Indicazioni stradali"; nessun iframe di mappa.
15. **Piede completo: non passa.** Quattro colonne a 1440 (marchio, Cosa facciamo, Sede e laboratorio, Seguici), testo di almeno 14 px, ragione sociale, P.IVA, indirizzo con la mappa, telefono ed email cliccabili, social con il sottotitolo, Privacy e Cookie. Mancano gli **orari** (lun-ven 8-12 e 14.30-18 vengono solo da un aggregatore) e le **certificazioni** (nessuna nota): non si scrivono finché l'azienda non li conferma.

### Compiti della scheda d'uso (par. 8)

- *Visitatore 1, fiera e vetrina, 1440*: nella prima schermata il pallone fuori scala con la persona accanto e le 8 voci dei lavori ("fanno oggetti giganti e scenografie in polistirolo"); "Mandaci il disegno" sia in testata sia nell'apertura apre l'email a info@poli-art.it con oggetto "Richiesta con disegno o file 3D" e la traccia (lavoro, misure, quantità, data, nome e azienda, telefono); la frase "se manca il 3D, provvediamo noi..." è già nella prima schermata e di nuovo nel blocco "Come mandarci il progetto"; il telefono resta in alto a destra in ogni punto della pagina.
- *Visitatore 2, edilizia, 390*: "Chiama 0444 614719" a tutta larghezza, alto 56 px, a 302 px dall'alto, `tel:+390444614719`, e lo stesso numero nella testata fissa; "Cornici e cornicioni" e "Casseri" nella riga dei lavori portano con un tocco alla scheda "Edilizia e casseri", seconda della griglia, con la foto del cornicione in cantiere e i nomi cornicioni, cornici di finestra, marcapiani, colonne, casseforme; l'indirizzo apre Google Maps su via Tesinella 7 (mappa e indicazioni). Gli orari non ci sono (da confermare).
- *Visitatore 3, pasticceria e feste, 390*: "Torte finte" e "Stampa 3D" nella riga dei lavori portano alla scheda "Torte finte e stampa 3D" con la foto vera (prova automatica: la scheda arriva sotto la testata con la foto visibile); Instagram @poliartgrisignano è sotto le schede, nei contatti e nel piede; per scrivere ci sono il bottone "Manda foto o disegno" in cima, "Mandaci il disegno" nel blocco del progetto e il modulo con la data dell'evento.
- Menu a 390: si apre al tocco, si chiude con Esc e al tocco su una voce.

### Controlli fatti

- Screenshot guardati a pezzi a 1440 e 390, e le pagine intere a 320, 768 e 1024. Confrontati con i riferimenti M: la prima schermata ha la struttura di Cly-Del (dichiarazione a sinistra, immagine a destra, due bottoni), il ritmo a blocchi di barth.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra i blocchi dell'apertura e nella testata.
- Collegamenti: un solo `tel:+390444614719`; `mailto:info@poli-art.it` con oggetto in tutti i link email; Google Maps "Poli-Art Via Tesinella 7 36040 Grisignano di Zocco VI" (ricerca) e indicazioni verso "Via Tesinella 7 36040 Grisignano di Zocco VI"; nessuna ancora senza destinazione.
- Nessun carattere U+2014 nella pagina, nei .md e negli script; nessun segnaposto in pagina.
- Ogni frase in pagina è loro (da `01-analisi.md` e `SCHEDA.md`) o è un'istruzione ("telefonate prima", "chiedetecele al telefono"). La P.IVA viene da un aggregatore e resta da confermare (LEGGIMI).

### Caratteri e licenze

- **Mona Sans** (GitHub Next), da Google Fonts, **SIL Open Font License 1.1**, uso commerciale libero; file woff2 serviti dalla pagina (`sito/fonts/mona-sans-latin.woff2`, `mona-sans-latin-ext.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, larghezza 100 %.
- Foto: solo materiale di Poli-Art dalla libreria media del loro sito (`assets/originali/`), da usare con il loro permesso; nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| In pagina | Originale | Lavorazione |
|---|---|---|
| apertura | `Pallone1.jpg` 2048x1536 | ritaglio 1370x1096 senza striscione e pannelli della mostra |
| Fiere e vetrine | `Vino1.jpg` 1600x1200 | intera |
| Edilizia e casseri | `IMG_20190531_181254_resized_20191023_075428502.jpg` 1040x780 | intera |
| Scenografie | `CorniciORO2.jpg` 1024x768 | intera |
| Lettere e loghi | `3Da-scaled.jpg` 2560x1928 | 4:3 al centro |
| Prototipi e mockup | `Oggetti2-scaled.jpg` 2560x1920 | intera |
| Torte finte e stampa 3D | `Pasticceria.jpg` 2048x1536 | intera |
| progetto, coppia | `Scarpa-converse3-scaled.jpg`, `Scarpa-converse1.jpg` | intere |
| laboratorio | `Fotovoltaico-working.jpg` 2048x1536 | ritaglio 16:9 sul pantografo e sulle due persone |
