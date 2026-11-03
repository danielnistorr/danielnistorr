# Nord Service, home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh --immagini`. La versione precedente ("Tornano nuove", pala scontornata su carta) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot, con la sua nota).

Screenshot in questa cartella, fatti all'ora simulata martedì 3 novembre 2026 alle 10 (stato "Aperto ora"): `home-1440.jpg` (7693 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10345 px), `home-390-prima-schermata.jpg`, `home-320.jpg`, `home-768.jpg`, `home-1024.jpg`, `chiusura-1440.jpg` (contatti e piede).

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Riferimenti guardati: le prime schermate di tutti e 14 (foglio `riferimenti.jpg`); le pagine intere di Eggentaler e Dulwich Diggers a pezzi con `slice.py` (in questa passata), di Kline e Wilson nella passata prima. Partenza: il giudizio del controllore (voto 6, regole 3, 5, 9, 10, 11, 14 non superate) e dei due clienti tipo (voti 8 e 7,5). Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Cosa è cambiato in questo ritocco e perché

- **Apertura su un blocco nero pieno a tutta larghezza** (difetto B1: prima era bianca come le altre home della campagna). Titolo bianco 72 px "Verniciatura e sabbiatura industriale" (la riga del loro logo), occhiello in arancio del logo, Chiama pieno arancio e "Manda le foto per mail" con il bordo bianco; sotto, "oppure scrivi a info@nordservice.net" in chiaro (per chi non ha un'app di posta impostata). In basso, allineata al piede della foto, la riga dei fatti: **40+** a 48 px in arancio con "anni di Stefano Barbieri nel settore, oggi con il figlio Leonardo" (ora anche sul telefono), orari con lo stato, officina con "Indicazioni".
- **La foto di apertura è la loro cabina**: `DSC07356` (Sony), una macchina coperta da carta, nastro e nylon nella cabina di verniciatura, a filo del bordo destro dello schermo, 4:5, alta quanto l'apertura (605x756 a 1440, nessun raggio); sul telefono 4:3 a tutta larghezza. Mostra l'officina e il mestiere, non un mezzo da catalogo. La WA320 passa alla scheda "Movimento terra" (al posto del CAT 330C da telefono).
- **Fascia arancio piena** subito dopo l'apertura con tre garanzie brevi (A1.3): Un numero solo (le sei lavorazioni con una sola officina), Sul punto del danno (la loro frase sulla vernice a liquido), Sabbiatura con garnet (la loro frase su polvere, riutilizzo e salute). Sul telefono la fascia viene dopo i mezzi, così le schede dei mezzi restano a 1230 px come prima.
- **Tolta la riga "Su che mezzi lavoriamo" dell'apertura** (si ripeteva col titolo della sezione dopo e lasciava 100 px vuoti): i link ai mezzi restano nella riga sotto il titolo.
- **Mezzi su bianco** (non più due neri vicini), sei schede 4:3 come prima.
- **Lavorazioni in schede con la foto del lavoro** (regola 9, B7): Sabbiatura a secco con garnet (dettaglio del D8R appena sabbiato, metallo grigio e garnet a terra), Fondi e vernici a liquido (mini escavatore in carta e nastro), Vetroresina e plastica (pannello stuccato); tutta la scheda cliccabile, porta al modulo con la lavorazione scelta. **Sostituzione vetri** in una scheda nera piena con "Mezzo fermo? Chiama l'officina." e il bottone "Chiama 049 900 5162"; Carpenteria e Consulenza in due colonne di testo. Tolti i numeri 01-06 e la fila doppia delle garanzie (il garnet non è più ripetuto). Frase di testa nuova e concreta: "Dal metallo nudo alla vernice, sulla macchina intera o su un pezzo solo." (al posto di "servizi di qualità e altamente personalizzati").
- **Lavori su un blocco nero, il D8R grande** (regola 11): a 1440 il finito è largo 942 px (74 % del contenitore), sabbiato e verniciato quadrati impilati a sinistra (prima e dopo si leggono da sinistra a destra); sul telefono i due quadrati affiancati e il finito a tutta larghezza. Le date (3 ottobre, 10 ottobre, 16 ottobre 2024) sono le uniche didascalie della pagina.
- **Altri lavori: due su sei colonne**, solo componenti (virole blu, traliccio giallo in cabina), con il solo nome: tolte le didascalie con la data di scatto e le frasi scritte da noi; tolti il mini escavatore (ora nelle lavorazioni) e il T916.
- **Chi siamo su bianco**: titolo "Stefano e Leonardo Barbieri" a 48 px, la loro frase sulla famiglia, poi ragione sociale, P.IVA, officina e sede legale. Tolte le cifre "2 generazioni" e "6 lavorazioni" (riempitivi).
- **Modulo**: accanto al titolo "Hai fretta? Chiama 049 900 5162"; la loro frase con la virgola e senza punto esclamativo; la nota sulle foto spostata in cima; nuovo campo "Quanti pezzi o macchine" (per chi manda lavori in serie); dopo "Prepara la mail" compare il testo composto con "Copia il testo" e l'indirizzo in chiaro, per chi usa una webmail.
- **Serie fotografica**: in `pro_img.py` tutte le foto hanno lo stesso trattamento (bilanciamento neutro misurato sui pixel quasi grigi, colore -10 %, contrasto +5 %, stessa curva sulle ombre; il pavimento verde del D8R finito portato verso il grigio). In grande solo le Sony e il D8R; le foto da telefono e da WhatsApp restano nelle schede.
- **Formati in pagina**: tre (4:5 apertura a 1440, 1:1 sabbiato e verniciato, 4:3 tutto il resto). Foto di contenuto: 15.

### Esito regola per regola

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot a 320, 390, 768, 1024 e 1440 guardati a pezzi.

1. **Telefono come bottone nella testata fissa: PASSA.** Testata fissa 88 px a 1440 e 72 a 390, bottone arancio 48 px ("Chiama 049 900 5162", sul telefono solo il numero). A metà pagina il bottone si vede e si tocca (`elementFromPoint`) a 390 e a 1440. 6 link `tel:` (testata, apertura, vetri, "Hai fretta?", telefono grande, piede), tutti `tel:+390499005162`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** 1440x900: H1, occhiello con Mestrino, 40+ a 48 px, Chiama a 453-509 px, mail, Indicazioni, foto. 390x844: Chiama largo 350 px su 350 a 313-369, mail delle foto a 379-435, indirizzo in chiaro a 437, 40+ a 498, stato "Aperto ora" a 590, Indicazioni a 630-680.
3. **Immagine vera nell'apertura: PASSA.** La cabina di verniciatura con una macchina mascherata (Sony), 4:5, 605x756 a 1440 e 390x293 a 390, non scontornata, nessun oggetto su fondo chiaro. Non ci sono ancora persone: la foto di Stefano e Leonardo resta la prima richiesta del LEGGIMI. Sul telefono della foto si vedono 136 px nella prima schermata.
4. **Zero repertorio: PASSA.** `indicativ` 0, `unsplash|pexels|repertorio` 0; 15 foto in pagina, tutte di Nord Service (elenco in `assets/CREDITI.md`); nessun file di `assets/esterne/`, nessuna delle sei di repertorio del loro sito, nessuna illustrazione.
5. **Foto in serie: PASSA.** Formati misurati 0,8, 1,33 e 1 (tre); didascalie 3 su 15 (le date del D8R); trattamento comune in `pro_img.py`. Le luci di partenza restano diverse (telefono, WhatsApp): il trattamento le avvicina, la serie vera è nel LEGGIMI.
6. **Palette dal marchio: PASSA.** Arancio #EF7821 del logo (#A9500F per il testo arancio su chiaro), nero #161616, grigio #4C4C4B del logo, bianco, #F1F1F1. Nessun colore fuori da `:root`, niente beige. Fondi: nero, arancio, bianco, grigio chiaro.
7. **Scala tipografica corta: PASSA.** 7 misure a 1440 (14, 17, 19, 23, 48, 72, 96) e 6 a 390 (14, 17, 20, 30, 36, 48); testo corrente 19 px a 1440 e 17 a 390; niente sotto i 14 px; H1 72/36, H2 48/30.
8. **Due famiglie al massimo: PASSA.** Una sola, Archivo, pesi 400 e 700; titoli, cifre e telefono grande in larghezza 78 %.
9. **Servizi in schede con la foto: PASSA.** Sei schede dei mezzi e tre delle lavorazioni, tre colonne a 1440 con passo di 24 px, tutte 4:3 con la loro foto, nome di 23 px, riga e link, tutta la scheda cliccabile. Vetri, carpenteria e consulenza senza foto: non ci sono foto vere di quei lavori (LEGGIMI).
10. **Almeno tre tipi di prova: NON PASSA (0 su 4).** Recensioni, 4-8 numeri aziendali, certificazioni o fornitori e clienti con il nome non sono nelle fonti e non sono stati inventati (LEGGIMI, punti 4, 6, 7, 8). In pagina c'è l'unico numero vero (40+ anni), in apertura, e i nomi di chi lavora.
11. **Lavori con un nome: NON PASSA (1 su 3).** Il D8R ha luogo (in officina), anno, tre date e la foto grande al 74 % del contenitore. Virole e traliccio hanno solo il nome: cliente, anno e dati del lavoro non sono nelle fonti (LEGGIMI, punto 9).
12. **Ritmo a blocchi: PASSA.** Blocchi pieni oltre al piede: apertura nero, fascia arancio, lavori nero, contatti arancio; mezzi e chi siamo bianchi, lavorazioni #F1F1F1. Sezioni 120/120 px a 1440 e 72/72 a 390 (fascia 56 e 36); margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno arancio e con il bordo (nero su chiaro, bianco su nero), raggio 4 px, 56 px (48 in testata), testo 17 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove e quando" per il mestiere: PASSA in parte.** Modulo con mezzo e lavorazione (tendine), marca e modello, quanti pezzi o macchine, cosa c'è da fare, dove si trova la macchina, urgenza (macchina ferma, entro il mese, senza fretta), nome e telefono obbligatori; compone la mail con oggetto e campi e mostra il testo da copiare; nessun iframe. Il campo foto non c'è (il mailto non allega: la nota lo dice in cima al modulo; il servizio vero è nel LEGGIMI). L'elenco dei comuni non c'è: nessuna fonte dice una zona (LEGGIMI, punto 5).
15. **Piede completo: PASSA, senza certificazioni.** Quattro colonne a 1440, testo di 14-17 px; Nord Service SRL, P.IVA, officina e sede legale, telefono, email e indirizzo cliccabili, orari, lavorazioni e mezzi, Instagram, Privacy e Cookie. Certificazioni: nessuna nelle fonti.

### Compiti della scheda d'uso (par. 8) e dei clienti tipo

- *Visitatore 1, telefono 390x844*: "Verniciatura", "sabbiatura" e "macchine da lavoro" a 127-280 px; Chiama 56 px a 313 px e telefono in testata; "Lun-ven 7:00-17:30" con "Aperto ora" a 590; "Manda le foto per mail" (oggetto e traccia) a 379 e l'indirizzo in chiaro subito sotto; la scheda Movimento terra a 1230 px (prima 1236). RIESCE, come prima o meglio (mail più in alto, indirizzo copiabile, il bottone dice che apre una mail).
- *Visitatore 2, computer 1440x900*: foto vera dell'officina, telefono, mail e indirizzo sopra 900 px; il D8R in tre foto insieme, il finito largo 942 px; virole e traliccio come componenti, torretta 813 nelle schede; lavorazioni con la foto e il metodo con le loro parole; Stefano e Leonardo Barbieri, Nord Service SRL, P.IVA e sede legale in "Chi siamo"; campo "Quanti pezzi o macchine"; testo da copiare se il programma di posta non si apre. RIESCE.
- *Visitatore 3, telefono*: "vetri", "camion e rimorchi" e "mezzi agricoli" nella riga della prima schermata (link alle schede), schede Camion a 1702 e Mezzi agricoli a 1843 (prima 1708 e 1849); "Indicazioni" nella prima schermata; telefono nella testata fissa e nella scheda nera dei vetri. RIESCE.
- *Per tutte*: nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440, 1920; nessuna foto di repertorio; logo vero e arancio nella prima schermata; niente prezzi, tempi o zone.

### Respinti, con il motivo

- *Riga "Tempi e prezzo te li diciamo dopo aver visto le foto; le macchine arrivano anche su carrellone"*: non confermata dall'azienda; va nel LEGGIMI tra le domande, non in pagina.
- *"Anche lavori in serie per costruttori e noleggiatori"*: nessuna fonte dice che li fanno; in pagina solo "Anche un pezzo solo" e il campo quantità; domanda nel LEGGIMI.
- *Sottotitolo "I lavori in officina" sotto Instagram, o togliere il link*: il link è sul loro sito di oggi ed è un fatto; il contenuto dell'account non è leggibile da qui, quindi niente sottotitolo inventato. Resta il nome dell'account, da confermare (LEGGIMI, punto 13).
- *Foto delle persone o dell'officina in "Chi siamo"*: non ci sono foto delle persone; l'unica foto dell'officina regge l'apertura e non va ripetuta.
- *Promessa dei tempi di risposta accanto al modulo*: nessun tempo nelle fonti; domanda aggiunta nel LEGGIMI.
- *Riscrivere "Più sei specifico..." come "Più sei preciso, più ci aiuti..."*: è una loro frase (scheda, par. 5); corretta solo la punteggiatura.

### Controlli fatti

- `pro_controlli.mjs`: regole 1-9 e 12-15 superate nelle misure, 10 e 11 no (sopra); nessuna sovrapposizione nell'apertura e nessun elemento fuori schermo alle otto larghezze; nessuna ancora senza destinazione; nessun errore di script; menu del telefono aperto e chiuso dopo la scelta; clic su "Scrivici" dei vetri: "Sostituzione vetri" e "Macchina ferma" già scelti; invio vuoto fermato con l'avviso e il fuoco sul nome; mail composta (con "Quanti pezzi o macchine") letta senza inviarla, e testo da copiare visibile.
- Stato a ore diverse: martedì 6:30 "Chiuso, apre oggi alle 7:00"; 10:00 "Aperto ora"; 17:45 "riapre domani"; venerdì sera e sabato "riapre lunedì"; 8 dicembre e Pasquetta 2027 "Chiuso oggi, festivo, riapre domani"; vigilia di Natale sera "riapre lunedì".
- Screenshot guardati a pezzi: 1440, 1024, 768, 390, 320 (pagine intere) e le due prime schermate. Corretti durante il lavoro: bilanciamento troppo freddo sulle foto gialle (ora misurato sui pixel neutri), bottone dei vetri su due righe sul telefono, date del D8R a capo, segnaposto del modulo tagliati, riga dei fatti staccata dal piede della foto.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin.woff2`, `archivo-latin-ext.woff2`, variabile con asse di larghezza), licenza in `sito/fonts/OFL.txt`.
- Foto: solo di Nord Service SRL (`assets/CREDITI.md`), da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessuno scontorno, nessun disegno.
