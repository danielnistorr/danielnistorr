# Home Poli-Art, livello professionale, ritocco finale (3/11/2026)

Pagina: `sito/index.html` (statica, si apre con file:///), con `sito/privacy.html` e `sito/cookie.html`; immagini in `sito/img/`, carattere e licenza in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagine da `pro_index.html`, `pro_privacy.html` e `pro_cookie.html`, screenshot con `pro_shot.mjs` e `pro_jpeg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). La versione 1 ("Grezzo e finito", con la testa cromata) è copiata com'era in `_prova/versione-1-originale/`.

Altezza: 8384 px a 1440, 12372 a 390.

File in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (la sezione "Dove siamo" con il modulo).

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Criterio: prima l'uso, poi l'identità, poi l'esecuzione. Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14; le pagine intere di barth e Cly-Del, a pezzi. Da barth: il logotipo come gesto di scala (qui nel piede), i blocchi pieni; da Cly-Del: la dichiarazione a sinistra con l'immagine a destra, la fascia piena di colore con la cifra grande, il piede scuro a quattro colonne.

### Che cosa è cambiato in questo ritocco

Dal controllo del livello (voto 6) e dalle prove dei due clienti tipo:

1. **Gesto di scala**: la fascia blu non ha più le sigle EPS, CNC e 3D messe come numeri. Ora è il 1986 a 220 px (112 sul telefono) in bianco sul blu del logo, con accanto il loro manifesto a 32 px ("Essendo un mercato di nicchia...", spostato qui dal laboratorio) e la firma "Poli-Art, Chi siamo". Fascia alta 480 px a 1440.
2. **Apertura**: il pallone è ritagliato in 4:5 verticale sul pallone e sulla persona (via la rete, il soffitto bruciato e i pannelli della mostra), il verde del prato è spento, i bianchi hanno una spalla morbida. A 1440 la foto va al vivo sul bordo destro, a tutta altezza del primo schermo (da 88 a 900 px, 708x812). Sotto i 900 px la foto è 4:5 sotto la riga dei lavori, con la didascalia "Il pallone abitabile: la persona accanto dà la misura." (rimessa, come chiedeva il cliente fiera).
3. **Trattamento delle foto rifatto** (`pro_img.py`): bianco misurato solo sui pixel quasi neutri e portato a R=G=B al 70 %; livelli sulla luminanza con la stessa curva per i tre canali (prima l'autocontrasto lavorava canale per canale e creava la dominante azzurra); spalla sulle alte luci; saturazione 0,88 e verdi più spenti. Il fondo delle lettere ora è (209,209,209), neutro. Al posto di `3Da` (la M toccava il bordo e la parola forse è di un cliente) c'è `3Db`, le lettere sparse, a fotogramma intero.
4. **Logo**: in testata 190 px a 1440 e 128 sul telefono (prima 150 e 104); nel piede il logotipo bianco a tutta larghezza del contenitore (1280 px a 1440, 350 sul telefono), come barth. Il logo porta a `./`, la home.
5. **Fila "Edilizia e casseri, dai cantieri"** sotto le schede, con ancora propria `#l-casseri` (la voce "Casseri" dell'apertura ora porta lì): quattro foto vere 4:3 (cassero resinato, casseri resinati, cornice di finestra posata, cornicione dietro il ponteggio), la loro frase sull'edilizia, un bottone "Manda la foto della facciata" con l'email per il cantiere (oggetto "Edilizia: cornici, cornicioni o casseri"; pezzo, metri lineari o quantità, comune del cantiere, quando vi serve, nome e impresa, telefono) e "Chiama 0444 614719".
6. **Laboratorio**: foto 16:9, le due frasi e un elenco di quattro fatti del mestiere con occhiello (materiale, lavorazione, finitura, stampa 3D), a 19 px.
7. **Apertura, testo**: la riga sotto il titolo dice subito i lavori con le parole del cliente ("Oggetti fuori scala per fiere e vetrine, cornici e casseri per l'edilizia, scenografie, lettere in volume, prototipi e torte finte: a controllo numerico e, dove serve, a mano."); la nota sotto i bottoni aggiunge "Formati e misura massima del blocco: chiedeteli al telefono."; "Grisignano di Zocco (VI)" nell'occhiello porta a "Dove siamo".
8. **Schede**: i link "Vedi..." si aprono in una nuova scheda, con la freccia e il testo nascosto "galleria sul sito attuale"; la scheda raggiunta dalla riga dei lavori ha un bordo blu che sfuma in 2,4 s e il titolo visibile sotto la testata. Alt ridotti a ciò che si vede (cornicione, cassettoni).
9. **Dove siamo**: sotto i recapiti c'è "Cosa mandarci" (file 3D o disegno o foto con le misure; quanti pezzi e in che finitura; la data), così la colonna non resta vuota accanto al modulo; "Per passare in laboratorio o chiedere del ritiro di un pezzo, telefonate prima."
10. **Piede**: "Per passare in laboratorio, telefonate prima." nella colonna della sede (al posto degli orari, finché non sono confermati); il credito "Sito di Evox Consulting"; link alti 44 px, Privacy e Cookie 32 px; `privacy.html` e `cookie.html` ora esistono (testi brevi e fattuali, da far verificare: LEGGIMI).

Struttura, adattata dalla A1 della famiglia M:

1. **Testata fissa** (88 px, 72 sul telefono): logo, quattro voci (Cosa facciamo, Come mandarci il progetto, Laboratorio, Dove siamo), il telefono come bottone "0444 614719" e "Mandaci il disegno". Sotto i 1200 px le voci vanno in "Menu"; sotto i 900 resta il telefono.
2. **Apertura** (bianca, foto al vivo a destra): occhiello con il comune, H1 "Lavorazione del polistirolo dal 1986", la riga dei lavori, i due bottoni, la nota sui file, le 8 voci dei lavori.
3. **Cosa facciamo** (grigio azzurro): sei schede 4:3 in tre colonne, poi la fila dell'edilizia e casseri, poi "Tutti i lavori, circa 140 foto" e Instagram.
4. **Come mandarci il progetto** (blu notte): tre modi, la coppia della scarpa, i bottoni.
5. **Il laboratorio** (bianco): foto, due frasi, quattro fatti del mestiere.
6. **Dal 1986** (fascia nel blu del logo): la cifra grande e il manifesto.
7. **Dove siamo** (bianco): telefono a 64 px, email, laboratorio con mappa e indicazioni, cosa mandarci, Instagram; a destra il modulo.
8. **Piede** blu notte: logotipo a tutta larghezza, quattro colonne, riga legale.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (`_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024.

1. **Telefono come bottone nella testata fissa: passa.** Testata `position:fixed`; a metà pagina, a 1440 e a 390, il bottone "0444 614719" (48 px) si vede e si tocca (`elementFromPoint`). 6 link `tel:`, tutti `tel:+390444614719`. C'è anche "Mandaci il disegno" (la voce "Richiesta" della famiglia M).
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440x900: occhiello con Grisignano di Zocco, H1 con "polistirolo" e "dal 1986", la riga dei lavori, "Mandaci il disegno" e "Chiama 0444 614719" alti 56 px, foto 812 px visibili su 812. A 390x844: lo stesso, bottoni a tutta larghezza (350 su 350), 8 voci su 8 visibili; la foto comincia a 736 px.
3. **Immagine vera nell'apertura: passa.** Il pallone abitabile loro, con la persona accanto, nel suo ambiente, non scontornato. Riserva: resta una foto da compatta; non mostra né il laboratorio né la sede (da rifare, LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo foto loro (da `assets/originali/`) e il logo; nessuna immagine di `assets/esterne/`, nessun disegno, nessun `<svg>`.
5. **Foto in serie: non passa (la luce).** Le condizioni misurabili passano: tre formati a 1440 (apertura 0,87 in un box da un ritaglio 4:5, schede, fila e coppia 4:3, laboratorio 16:9); 4 didascalie su 14 foto (al massimo 1 ogni 3); stesso trattamento per tutte, ora senza dominanti (bianco neutro, curva unica sui tre canali). Non passa la stessa luce: sono scatti di anni e macchine diverse (fiera al neon, cantiere al sole, giardino, negozio, laboratorio sotto i tubi fluorescenti). Si risolve solo con un servizio fotografico (LEGGIMI).
6. **Palette dal marchio: passa.** `--ardesia` #5F708E (il blu del logo), `--ardesia-scuro` #4E5F7D, `--notte` #1C2330, più i neutri freddi; fondo bianco, niente beige. Limite: una sola tinta in tre valori; il marchio non ha un secondo colore e non lo invento.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 44, 64, 220) e 8 a 390 (14, 16, 17, 20, 26, 30, 38, 112); testo corrente 19 px a 1440 e 17 a 390; nessun testo sotto i 14 px (14 solo per occhielli maiuscoli spaziati e riga legale); H1 64 / 38, H2 44 / 30.
8. **Due famiglie al massimo: passa.** Una sola, Mona Sans, pesi 400 e 700, larghezza 100 %.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne (2 a 768, 1 a 390), sei schede, foto 4:3 per tutte, nome, riga, link; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa (1 su 4, parziale).** L'unico numero aziendale vero è il 1986, ora in grande da solo (le sigle EPS, CNC e 3D sono tolte perché fingevano numeri). Mancano recensioni, certificazioni, clienti con il nome. Nulla è inventato; cosa chiedere è nel LEGGIMI.
11. **Lavori con un nome: non passa.** Le fonti non danno cliente, luogo e anno di nessun lavoro. La sezione "Lavori" è preparata nel LEGGIMI (tre lavori proposti e i dati da chiedere per ognuno), non in pagina.
12. **Ritmo a blocchi: passa.** Due blocchi pieni oltre al piede (progetto blu notte, fascia del 1986 blu ardesia), "Cosa facciamo" grigio azzurro, il resto bianco; spazio tra le sezioni 120 px a 1440 (anche la fascia) e 72 a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px ovunque, 56 px (48 in testata), testo 17 px (16 in testata sul telefono e sotto i 360 px); tutti i bottoni di chiamata contengono "0444 614719".
14. **Modulo e "dove" per il mestiere: passa.** Nome, azienda, email, telefono, lavoro (9 voci), misure e quantità, data, "Cosa allegherete", messaggio. Provato: vuoto avvisa "Manca: nome e cognome." e mette il fuoco sul campo; compilato compone `mailto:info@poli-art.it` con oggetto "Preventivo: <lavoro> (<azienda>)" e tutti i campi. L'allegato si aggiunge nell'email (detto sopra il modulo; collegamento a un servizio nel LEGGIMI). "Apri la mappa" e "Indicazioni stradali"; nessun iframe.
15. **Piede completo: non passa.** Quattro colonne a 1440, testo di almeno 14 px, ragione sociale, impresa individuale, P.IVA, indirizzo con la mappa, telefono ed email cliccabili, sede, social con il sottotitolo, Privacy e Cookie (pagine che ora esistono), credito dello studio. Mancano gli **orari** (solo da un aggregatore; al loro posto "Per passare in laboratorio, telefonate prima.") e le **certificazioni** (nessuna nota): non si scrivono finché l'azienda non li conferma.

### Compiti dei clienti tipo (scheda d'uso par. 8 e prove)

- *Marketing o allestitore in fiera, 1440*: prima schermata con il pallone a tutta altezza e la persona accanto, didascalia della misura, la riga "Oggetti fuori scala per fiere e vetrine..." sotto il titolo, "Fiere e vetrine" prima voce: 0 scorrimenti, 1 clic alla scheda, che ora si segnala con il bordo. "Mandaci il disegno" in testata e in apertura (oggetto "Richiesta con disegno o file 3D" e traccia); formati e misura massima detti subito sotto i bottoni. Il telefono resta fisso in testata. Le gallerie del vecchio sito si aprono in una nuova scheda, così la home resta aperta. Nessun compito peggiora.
- *Impresa edile, 390*: "Cornici e cornicioni" porta alla scheda Edilizia (titolo a 184 px, foto visibile); "Casseri" ora porta alla fila dei cantieri con quattro foto vere, tra cui due di casseri (176 px, foto visibile); lì c'è l'email per il cantiere (comune, metri lineari) e "Chiama". Il telefono fisso in testata, 48 px. "Grisignano di Zocco (VI)" in apertura porta a "Dove siamo", con mappa, indicazioni e "telefonate prima" anche per il ritiro. Nessun compito peggiora.
- *Pasticceria e feste, 390*: "Torte finte" e "Stampa 3D" portano alla scheda (prova automatica: titolo sotto la testata, foto visibile); Instagram sotto le schede, nei contatti e nel piede; modulo con la data dell'evento.
- Menu a 390: si apre al tocco, si chiude con Esc e al tocco su una voce.

### Controlli fatti

- Screenshot rigenerati e guardati a pezzi a 1440, 390, 320, 768 e 1024 (e la pagina privacy a 390).
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura e nella testata.
- Collegamenti: un solo `tel:+390444614719`; `mailto:info@poli-art.it` con oggetto in tutti i link email (tre oggetti: disegno o file 3D, edilizia, richiesta dal sito); Google Maps ricerca e indicazioni; nessuna ancora senza destinazione; `privacy.html` e `cookie.html` presenti.
- Nessun carattere U+2014 in pagina, nei .md e negli script; nessun segnaposto in pagina.
- Ogni frase in pagina è loro (da `01-analisi.md` e `SCHEDA.md`) o è un'istruzione ("telefonate prima", "chiedeteli al telefono"); la riga sotto il titolo e i quattro fatti del laboratorio ricompongono le loro parole (settori di `cosa-facciamo/`, `cosa-facciamo/` sulla lavorazione, `scenografie/` sui trattamenti, `stampa-3d/`). La P.IVA viene da un aggregatore e resta da confermare.

### Caratteri e licenze

- **Mona Sans** (GitHub Next), da Google Fonts, **SIL Open Font License 1.1**, uso commerciale libero; woff2 serviti dalla pagina (`sito/fonts/mona-sans-latin.woff2`, `mona-sans-latin-ext.woff2`), licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700.
- Foto: solo materiale di Poli-Art dalla libreria media del loro sito (`assets/originali/`), da usare con il loro permesso; nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| In pagina | Originale | Lavorazione |
|---|---|---|
| apertura | `Pallone1.jpg` 2048x1536 | ritaglio 960x1200 (4:5) sul pallone e sulla persona |
| Fiere e vetrine | `Vino1.jpg` 1600x1200 | intera |
| Edilizia e casseri | `IMG_20190531_181254_resized_20191023_075428502.jpg` 1040x780 | intera |
| Scenografie | `CorniciORO2.jpg` 1024x768 | intera |
| Lettere e loghi | `3Db-scaled.jpg` 2560x1928 | fotogramma intero, 4:3 |
| Prototipi e mockup | `Oggetti2-scaled.jpg` 2560x1920 | intera |
| Torte finte e stampa 3D | `Pasticceria.jpg` 2048x1536 | intera |
| fila edilizia | `Cassero1.jpg`, `Colonna5.jpg`, `IMG_20190329_090137_resized_20191023_075153440.jpg`, `IMG-20190705-WA0023.jpg` | 4:3 (la cornice di finestra ritagliata dal verticale) |
| progetto, coppia | `Scarpa-converse3-scaled.jpg`, `Scarpa-converse1.jpg` | intere |
| laboratorio | `Fotovoltaico-working.jpg` 2048x1536 | ritaglio 16:9 sul pantografo e sulle due persone |
| logo | `logo-blu-1815x400.png`, `logo-bianco-1815x400.png` | ritagliati; il bianco anche a 1300 e 1815 px per il piede |
