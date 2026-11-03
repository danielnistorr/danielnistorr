# San Marco Timbri: proposta di nuova home

Proposta non richiesta di una nuova homepage per San Marco Timbri di Tosato Andrea (sanmarcotimbri.it, Padova). Solo la home. Versione di oggi: livello professionale (3 novembre 2026).

## Dove sono le cose

- `sito/index.html`: la home (si apre con file:///). In `sito/img/` ci sono solo le immagini usate, in WebP a due larghezze; in `sito/fonts/` Encode Sans e la sua licenza (`OFL.txt`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (sezione "Livello professionale": esito delle 15 regole, prove d'uso, respinti, caratteri, foto).
- `_prova/script/build_finale.sh`: rifà tutto. I suoi pezzi:
  - `pro_img.py`: immagini, trattamento comune;
  - `index.sorgente.html`: la pagina;
  - `fin_shoot.mjs`: screenshot;
  - `pro_controlli.mjs`: le 15 regole e le prove d'uso della scheda.
  Prova a parte: `pro_largo.mjs` (scorrimento orizzontale). `pro_provini.py` fa i provini delle foto candidate. Gli script `fin_*` e `proto_*` sono delle versioni precedenti e non sono più usati dalla build.
- `_prova/versione-1-originale/`: la home e gli screenshot di prima ("L'impronta", fondo blu e leone LEO).
- `_prova/uso/SCHEDA.md`: chi apre il sito, che cosa viene a fare, l'identità. `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Da chiedere all'azienda (in pagina non c'è nulla di dubbio)

- **Orari** del laboratorio, e se si riceve al banco o su appuntamento. L'unico dato pubblico è 2gis (8.30-12.30 e 15.00-19.00), sulla scheda della vecchia sede. Quando sono confermati, si scrivono nella costante `ORARI` in cima allo script della pagina, per esempio `{1:[['08:30','12:30'],['15:00','19:00']], ...}`. La pagina mostra allora "Aperto ora" o "Ora chiuso" con le fasce di oggi nell'apertura e la tabella della settimana in "Quando passare". Finché è `null` dice "Prima di passare chiamateci".
- **Indirizzo**: in pagina c'è via G. A. Longhin 91, 35129 Padova (sito e registri). 2gis, Yelp, coobiz e trovainitalia danno ancora via Domenico Turazza 42, con lo stesso telefono. Va aggiornata la scheda di Google Maps e degli elenchi. Il link "Indicazioni" porta all'indirizzo, non al nome dell'attività, apposta.
- **PEC**, e se sono **ancora sul MEPA**: per gli enti servono. Alcuni elenchi riportano sanmarcotimbri@internetpec.it, visto solo in un riassunto di ricerca. In pagina c'è solo il fatto del 2018 (fornitori invitati da Agenzia delle Entrate alla gara MEPA per i timbri): va chiesto se vogliono vederlo scritto.
- **Fattura elettronica e codice destinatario** (o SDI), se vogliono metterli tra i dati per gli uffici.
- **Spedizione**: si spedisce o solo ritiro? Il modulo e l'email chiedono "ritiro o spedizione" (lo chiedeva la scheda), ma non promettono nulla.
- **Tempi tipici** (in giornata, 24 ore, qualche giorno) e un **prezzo indicativo** di un autoinchiostrante: non ce ne sono di pubblici, quindi in pagina non c'è nessun tempo di consegna.
- **Parcheggio** davanti al laboratorio, se c'è.
- **Anno di inizio** dell'attività: il sito dice solo "da molti anni"; con l'anno l'apertura avrebbe una prova più forte.
- **Recensioni**: non ce n'è nessuna leggibile (Maps 429, Facebook solo con login, 2gis e Yelp vuoti). Se hanno recensioni Google, o clienti che si possono nominare (studi, condomini, enti), sono la prova che manca (regola 10).
- **Lavori con un nome**: per due o tre lavori su misura, il cliente o il luogo, l'anno e due dati (materiale, misura, pezzi), se si possono dire (regola 11).
- **Che le foto siano loro e il permesso di usarle**, soprattutto quando mostrano il lavoro di un cliente: la targa in corten (un resort), l'insegna traforata col cavallo e la targa TOILETTES 101.
- **Macchine vere** (marca e tipo della CNC, del laser, della fresa, della stampante): ora c'è solo la loro frase generica.
- Se **casellari, plexiglass e insegne luminose** si fanno in laboratorio o si comprano e si personalizzano.
- Il **logo in vettoriale** e il nome del carattere della scritta (somiglia a Comfortaa): oggi testata e piede usano i raster 641x114 e 256x200.
- I **social** veri, se ci sono: le icone del vecchio piede non portano a nulla, quindi nel piede non ci sono.
- Se le 16 pagine "timbri-a-<comune>" vanno tenute: i comuni sono elencati in "Dove lavoriamo".

## Modulo di richiesta: va collegato

Il modulo "Chiedete un timbro o un preventivo" chiede il tipo di richiesta in quattro caselle (timbro in gomma, timbro in metallo o sigillo, targa o pulsantiera, altro lavoro su misura), poi nome, ragione sociale, telefono, email, testo riga per riga o descrizione, misura o modello, quantità, ritiro o spedizione.

Oggi **non invia nulla da solo**: compone un'email (mailto a info@sanmarcotimbri.it con oggetto "tipo, ragione sociale o nome" e tutte le voci) e il visitatore la manda dal suo programma di posta, allegando lì logo e foto. Per il sito vero va collegato a un servizio di invio:
- il modulo del CMS (per esempio Contact Form 7 su WordPress, che usano già);
- oppure un servizio come Formspree o Brevo.
Serve anche un **campo per allegare file** (foto del vecchio timbro, logo, disegno: JPG, PNG, PDF), una risposta di conferma e l'informativa privacy che cita il servizio scelto. Il bottone "Prepara l'email" diventa "Invia la richiesta".

Anche i bottoni "Scrivi a info@sanmarcotimbri.it" e "Email con le voci già scritte" aprono un'email con oggetto "Richiesta timbro" e le voci da compilare; i bottoni WhatsApp aprono la chat con 376 167 3361 con un messaggio già avviato, diverso per ogni lavoro.

## Pagine richiamate dalla home

Tutti i link della home portano a sezioni della home stessa (`#dove`, `#timbri`, `#su-misura`, `#metodo`, `#enti`, `#scrivi`), tranne due pagine da creare: `privacy/` e `cookie/` (oggi gestite con iubenda).

## Foto da fare dal vero

Il materiale loro è fatto di scatti da banco a 1000 px, con luci e fondi diversi: per una serie vera serve una giornata di fotografia.
- **Come**: un solo fotografo e una sola luce per tutto. Luce laterale morbida (finestra o softbox da sinistra, pannello bianco a destra), fotocamera su cavalletto, almeno 3000 px sul lato lungo, fuoco su tutto il pezzo, sempre lo stesso fondo (carta grigio chiaro neutro per gli oggetti).
- **In ordine di importanza**:
  1. **Il laboratorio e chi ci lavora**: Andrea Tosato al banco con un timbro appena montato o un pezzo appena inciso, le mani al lavoro, la CNC o il laser in funzione (la persona guarda il lavoro, non l'obiettivo). È la foto che manca per l'apertura (regola 3) e per "Come funziona".
  2. **L'ingresso di via Longhin 91**, con l'insegna e il numero civico, di giorno: va nella scheda "Dove siamo", e chi arriva in macchina riconosce il posto.
  3. **Il banco con i timbri pronti**: autoinchiostranti montati, con l'impronta accanto su carta bianca. Oggi non esiste nessuna foto loro di un timbro in gomma; senza marchio Trodat in primo piano.
  4. **Il punzone in ottone con il suo segno a caldo** su legno o cuoio, rifatto a 3000 px, per l'apertura (oggi 1000 px).
  5. **Le sei schede su misura**, rifatte con la stessa luce, in 4:3: una pulsantiera in pietra, una targa in ottone, le lettere in ottone brunito in macro, un'insegna, una segnaletica in opera, una premiazione. In più un casellario postale loro, che oggi manca (ci sono solo foto di catalogo).
  6. **Un sigillo con la sua ceralacca** e una pressa a secco con il suo rilievo, per la sezione dei timbri.

## Licenze

- Nessuna foto di repertorio nella home. Le foto Pexels e Unsplash in `assets/esterne/` sono servite solo ai prototipi e non sono usate; licenze in `assets/CREDITI.md`.
- Le foto in pagina e i loghi vengono dalla libreria media del sito sanmarcotimbri.it e vanno confermati prima di pubblicare.
- Carattere: Encode Sans, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina; testo della licenza in `sito/fonts/OFL.txt`.

## Collaudo da file

Aperta da file://, la pagina non scrive errori in console. Il menu sotto i 1100 px si apre con il tocco e si chiude con Esc. Nessuno scorrimento orizzontale da 320 a 1920 px. Su un server la pagina funziona uguale.
