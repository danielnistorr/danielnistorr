# Impreservice, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri e licenza in `sito/fonts/`. Rigenerazione e controlli: `bash _prova/script/build_finale.sh`. La nota della versione precedente (sezione ricostruita, interruttore Aperto / Agganciato, foto di repertorio) è in `_prova/versione-1-originale/screenshot/home/NOTA.md`, con la pagina e gli screenshot di allora.

Screenshot in questa cartella: `home-1440.jpg` e `home-390.jpg` (pagine intere), prime schermate a 320, 390, 768, 1024, 1440 e 1920, `home-1440-en-prima-schermata.jpg` (la stessa pagina in inglese), `chiusura-1440.jpg` (ponti, contatti, piede). `home-1440-agganciato.jpg` non c'è più: l'interruttore è stato tolto.

## Livello professionale (03/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente". Criterio: prima l'uso (chi apre il sito trova subito ciò per cui è venuto), poi l'identità (parole e tono loro), poi l'esecuzione da studio. Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori), adattata a un produttore tecnico che vende a imprese di scavo, prefabbricatori ed enti gestori di ponti. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (foglio `riferimenti.jpg` e le 14 catture a 390), le pagine intere di Cly-Del e barth a pezzi. Da Cly-Del: apertura con la dichiarazione di competenza, blocco scuro, fascia dei numeri, schede in griglia, piede scuro a quattro colonne; da barth: i numeri aziendali in griglia, la lingua nella testata, l'uso del colore del marchio come blocco pieno.

### Cosa è cambiato rispetto alla versione 1

- **Via la sezione ricostruita e l'interruttore** (la scheda d'uso la indica come il rischio peggiore: un ingegnere che vede il suo pezzo disegnato male). Via tutte le foto di repertorio (galleria di Mishin, viadotto di Nagda, scudo di Mpikakis, calcestruzzo di Dvoretskyi). Via "Siamo in ventidue" e "Dal Brennero a Brisbane", frasi non loro.
- **Restano** il titolo con le loro parole ("Sistemi di connessione", dal titolo del loro video "SISTEMI DI CONNESSIONE / Conci attrezzati con tecnologia EasyClick"), ora "Sistemi di connessione per conci attrezzati" come chiede la scheda; Geologica, una sola famiglia; il blu del simbolo `#075A9E`; i dati legali, il link alle segnalazioni e l'elenco dei cantieri, ora completo per Europa e Mondo.
- **Apertura** su blocco scuro `--notte` (il sottosuolo del loro video): luogo nell'occhiello, titolo a 64 px, la riga dei due mestieri ("Easy Click per i conci delle gallerie scavate con la fresa. Giunti, appoggi e vincoli antisismici per ponti e viadotti, con la posa."), "Richiedi un'offerta, manda il disegno" pieno e "Versioni e schede tecniche" con il bordo. A destra la copertina del loro video, che si carica da YouTube solo al clic. Sotto, una striscia di quattro ingressi: Brevetto IT 1391815 (link a Google Patents), 42 cantieri in 11 paesi, Consegne in tutto il mondo secondo quantità, e Ponti e viadotti su blu pieno.
- **Testata fissa** con il telefono come bottone ("0444 1939838"), "Richiedi un'offerta" e IT / EN sempre in vista a 1440; a 390 il telefono pieno blu, "Scrivi" e "Menu" (nel menu anche "Mappa: Via Serenissima 8/b" e la lingua).
- **Quale Easy Click?** su grigio freddo: Smart, Medium, Magnum con i loro render nello stesso taglio; Smart HD con "480 kN" e Hybrid con "L140" in cifre grandi al posto della foto che non c'è. Ogni scheda porta al modulo con la versione scelta e la scheda tecnica spuntata.
- **Numeri** su blu pieno (il gesto di scala della pagina): 42, 11, 18, 5, 480 kN, 2008, sotto il titolo preso dal loro profilo ("rewarded by the references of leading contractors, both in Italy and around the world").
- **Come funziona** con le tre frasi del loro comunicato 2013 (inserimento facile, serraggio affidabile, meno gap e offset), gli altri accessori (sistemi di connessione, bulloni e barre di guida) e la fascia brevetto, laboratori indipendenti, WTC 2022, Viatec 2013.
- **Ponti e viadotti** su blocco scuro: "Ricerca e sviluppo nella produzione e nella posa di giunti antisismici, appoggi e vincoli", i tre prodotti con "produzione e posa", "Si affidano a Impreservice: ANAS, Autostrade per l'Italia, Province autonome", "Chiedi un sopralluogo o un'offerta" (email con l'oggetto già scritto) e il telefono.
- **Contatti**: a sinistra sede, telefono, mappa, due email (colonna che resta ferma mentre si scorre il modulo); a destra il modulo per il mestiere.
- **Inglese**: tutta la pagina, con le loro frasi inglesi dove esistono; `?lang=en` la apre già in inglese.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 72 a 390; bottone "0444 1939838" alto 48 px (pieno blu sul telefono, sotto i 375 px diventa "Chiama"). A metà pagina, a 390 e a 1440, si vede e si tocca (`elementFromPoint`). Per la famiglia M c'è anche "Richiedi un'offerta" in testata. 4 link `tel:`, tutti `tel:+3904441939838`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440 x 900: titolo e riga dei due mestieri, "Grisignano di Zocco (VI)" nell'occhiello, Brevetto IT 1391815 e 42 cantieri nella striscia, "Richiedi un'offerta" a 468 px, EN in testata, l'ingresso Ponti e viadotti a 593 px. A 390 x 844: titolo, riga, bottone a tutta larghezza (350 px) a 412 px, "Brevetto IT 1391815 · 42 cantieri in 11 paesi", telefono e Scrivi in testata.
3. **Immagine vera nell'apertura: non passa del tutto.** C'è l'unica immagine vera di cantiere che hanno, il fotogramma del loro video (1280 x 720, mostrato a 519 px, sotto la misura d'origine), ma non mostra persone di Impreservice, la sede o il pezzo. Nessuna illustrazione, per scelta del committente. Le foto da fare sono nel LEGGIMI.
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; in `sito/img/` solo render, fotogramma del video e simbolo del logo.
5. **Foto in serie: passa.** Tre render della stessa serie (stesso fondo, stessa luce, stesso taglio quadrato) e il fotogramma; due formati (16:9 e 3:2 delle schede); nessuna didascalia sotto le foto; nessuna ingrandita oltre la misura d'origine.
6. **Palette dal marchio: passa.** `--blu` #075A9E (simbolo del logo) con `--blu-scuro` per il passaggio del mouse e `--notte` #0A1A2A per i blocchi scuri; neutri freddi (`--bianco`, `--nebbia` #EEF1F4, `--testo`, `--testo-2`). Nessun colore scritto fuori da `:root`. Nessun beige.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 16, 18, 22, 30, 44, 64) e 7 a 390 (14, 16, 17, 20, 26, 30, 36); testo corrente 18 px a 1440 e 17 a 390; nessun testo sotto i 14 px; titolo 64 / 36 px, titoli di sezione 44 / 30. Due pesi, 400 e 700.
8. **Due famiglie al massimo: passa.** Una sola, Geologica.
9. **Servizi in schede con la foto: passa, con riserva.** Griglia di 3 colonne con Smart, Medium, Magnum e i loro render nello stesso taglio, poi Smart HD e Hybrid in 2 colonne con la cifra al posto della foto (il render non esiste); tutte le schede sono cliccabili. La linea ponti è un elenco tipografico, senza foto: non ne hanno.
10. **Almeno tre tipi di prova: passa (3 su 4, con riserva).** Sei numeri aziendali; clienti con il nome (ANAS, Autostrade per l'Italia, Province autonome); fascia con didascalia di brevetto, laboratori indipendenti e due fiere, che però non è una fascia di certificazioni. Recensioni: nessuna, non esistono (LEGGIMI, punto 8).
11. **Lavori con un nome: non passa.** 26 cantieri con nome e luogo, ma senza anno, dati e foto: le fonti non li danno (LEGGIMI, punto 7).
12. **Ritmo a blocchi: passa.** Tre blocchi scuri o di colore pieno oltre al piede (apertura e ponti `--notte`, numeri blu), due grigi (versioni, referenze); sezioni a 120 px a 1440 e 72 a 390; contenitore di 1280 px con margini di 80 px a 1440 e 20 a 390. La fascia delle prove continua la sezione sopra, senza spazio in alto.
13. **Un solo sistema di bottoni: passa.** Pieno blu e con il bordo, raggio 3 px ovunque, 52 px (48 in testata), testo 16 px in grassetto; i bottoni di chiamata contengono il numero. A 320 px il bottone principale va su due righe e supera i 58 px.
14. **Modulo e "dove" per il mestiere: passa.** Campi della famiglia M: nome, azienda, email, telefono, prodotto (le cinque versioni, "Non so, consigliatemi", bulloni e barre di guida, ponti), cosa serve (offerta, scheda tecnica, sopralluogo), progetto, quantità in conci o anelli, consegna, **disegno del concio** (PDF, DWG, DXF, STEP), messaggio. Il modulo compone l'email e va collegato a un servizio (LEGGIMI). Indirizzo con "Apri la mappa" (Google Maps), nessun iframe di mappa.
15. **Piede completo: non passa.** Quattro colonne a 1440, testo di almeno 14 px, ragione sociale, P.IVA e C.F., REA, capitale, indirizzo con la mappa, telefono ed email cliccabili, prodotti, azienda, YouTube con il sottotitolo, segnalazioni, Privacy e Cookie. Mancano gli orari e le certificazioni, che oggi non sono pubblicati (LEGGIMI, punti 5 e 6).

### Compiti della scheda d'uso (par. 8)

- *Ufficio tecnico, 1440*: in 5 secondi titolo e riga dicono connettori per conci e giunti per ponti; "Richiedi un'offerta, manda il disegno" porta al modulo con il campo file; "480 kN" di Smart HD è nella seconda schermata (e nella fascia dei numeri); ogni versione porta alla richiesta della scheda tecnica (i PDF non esistono ancora); EN in testata con un clic; brevetto con il numero e il link già nella prima schermata; le metropolitane sono nelle prime righe di ogni elenco.
- *Ponti e viadotti, 1440*: ingresso su blu nella prima schermata, a destra della striscia, e voce di menu; nel blocco giunti, appoggi e vincoli, "produzione e posa", ANAS e Autostrade per l'Italia, e i due contatti.
- *Cliente in cantiere, 390*: telefono pieno e "Scrivi" in testata senza scorrere (48 px), restano in vista scorrendo; la mappa a due tocchi (Menu, "Mappa: Via Serenissima 8/b"). Gli orari non ci sono (non pubblicati).
- Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920, in italiano e in inglese; nessuna sovrapposizione tra testata, titolo, bottoni, video e striscia.

### Gesti provati (pro_controlli.mjs)

Menu a 390 aperto e chiuso dopo il clic, ancora "Ponti" che si ferma sotto la testata; IT / EN avanti e indietro (titolo, `lang`, oggetti delle email); la scheda Smart HD sceglie il prodotto e spunta la scheda tecnica; invio vuoto fermato con l'avviso e il fuoco sul nome; email composta e letta senza inviarla ("Richiesta offerta: Easy Click Smart HD (480 kN) (Prova Srl)", con tutti i campi); nessun iframe prima del clic sul video, quello di youtube-nocookie dopo; nessun errore di script.

### Caratteri e licenze

- **Geologica** (Monokrom), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt`. Servita dalla pagina (`geologica-latin.woff2`, `geologica-latin-ext.woff2`), pesi 400 e 700.
- Immagini: solo materiale loro (render della pagina Prodotti, fotogramma del video YouTube, simbolo del logo), da usare con il loro permesso; dettagli in `assets/CREDITI.md`. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Controlli fatti

- `pro_controlli.mjs`: regole 1, 2, 4-10, 12-14 superate nelle misure; 3, 11 e 15 no (vedi sopra).
- Collegamenti: `tel:+3904441939838`; `mailto:info@impreservicesrl.it` e `mailto:carlo@impreservicesrl.it` con oggetti in italiano e in inglese; mappa `https://www.google.com/maps/search/?api=1&query=Via+Serenissima+8b+36040+Grisignano+di+Zocco+VI`; tutte le ancore interne esistono.
- Screenshot guardati a pezzi a 1440 e 390 (pagine intere), prime schermate a 320, 768, 1024, 1920 e 1440 in inglese, confrontati con Cly-Del e barth. Nessun U+2014 in pagina, nei .md e negli script; nessun segnaposto in pagina.
