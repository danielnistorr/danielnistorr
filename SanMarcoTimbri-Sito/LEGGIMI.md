# San Marco Timbri: proposta di nuova home

Proposta non richiesta di una nuova homepage per San Marco Timbri di Tosato Andrea (sanmarcotimbri.it, Padova). Solo la home.

## Dove sono le cose

- `sito/index.html`: la home finale (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG e WebP in più larghezze. `sito/fonts/`: Encode Sans e la sua licenza (`OFL.txt`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, cosa è cambiato, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà tutto (scontorno del leone, immagini, pagina, caratteri, screenshot). I suoi pezzi: `fin_leone.py`, `fin_immagini.py`, `index.sorgente.html` (la pagina), `fin_shoot.mjs`. Prove a parte: `fin_gesto.mjs` (gesto, tastiera, tocco, collegamenti), `fin_larghezze.mjs` (scorrimento orizzontale da 320 a 2560), `fin_2x.mjs` (dettaglio a 2x), `fin_console.mjs` (errori in console). `fin_scontorno.py` è della versione precedente (timbro di repertorio) e non è più usato.
- `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine. `_prova/home/a` e `b`: i due prototipi. `_prova/cieco.json`: il giudizio cieco sulla versione precedente.

## Dati da confermare (in pagina non c'è nulla di dubbio)

- **Indirizzo**: in pagina c'è via G. A. Longhin 91, 35129 Padova (sito e registri). Molti elenchi (coobiz, 2gis, trovainitalia) danno ancora via Domenico Turazza 42, 35128 Padova con lo stesso telefono: va chiesto quale delle due è la vecchia sede e, se serve, aggiornata la scheda di Google.
- **Orari** del laboratorio e se si riceve al banco o su appuntamento: oggi non ci sono; vanno nella chiusura, sotto l'indirizzo.
- **Anno di inizio** dell'attività (la P.IVA risulta attiva da 11-20 anni; il sito dice solo "da molti anni"): con l'anno la pagina avrebbe il contenuto datato che oggi manca.
- **Macchine vere** (marca e tipo della CNC, della fresa, del laser, della stampante digitale): "I file li prepariamo noi" usa solo la loro frase generica.
- Se **plexiglass, insegne luminose e casellari** si fanno in laboratorio o si comprano e si personalizzano.
- Che il **leone traforato**, le **lettere in ottone brunito** e la **targa in corten** siano lavori loro e il permesso di usarli (in pagina le didascalie dicono solo cosa sono, non "un nostro lavoro"); per il leone, per chi è stato fatto e se il cliente è d'accordo a vederlo in apertura; per la targa, il nome del cliente e l'anno, se si possono dire.
- Se il **blu dell'apertura e del piede** va bene come colore della casa (oggi il loro sito usa il rosso #FF0000): il blu è quello dell'inchiostro da timbri; se preferiscono, lo stesso impianto regge con un loro colore d'inchiostro.
- Il **WhatsApp** da mostrare (oggi 376 167 3361) e gli eventuali **social** veri: le icone del vecchio piede non portano a nulla, quindi nel piede non c'è "Seguici".
- **PEC e REA**, se vogliono metterli nella riga legale (un'impresa individuale non ha capitale sociale).
- Se vogliono la **newsletter**, chi la scrive e con quale servizio (sotto).
- Se le 16 pagine "timbri-a-<comune>" vanno tenute.

## Newsletter: va collegata

Nel piede c'è la fascia "Novità e promozioni" con campo email, bottone "Iscriviti" e casella del consenso privacy. Oggi **non invia nulla**: controlla solo email e consenso e scrive un messaggio di cortesia. Per farla funzionare va collegata a un servizio (Brevo, Mailchimp, MailerLite o il modulo del CMS) con doppia conferma, e l'informativa privacy deve citare il servizio scelto. Se la newsletter non interessa, si toglie il blocco `.news` e il piede resta in ordine.

## Pagine del sito nuovo richiamate dalla home

Dalla home e dal piede partono link a queste pagine, da creare:
- `lavorazioni/targhe/`, `lavorazioni/incisioni/`, `lavorazioni/segnaletica/`, `lavorazioni/insegne/`, `lavorazioni/casellari-postali/`, `lavorazioni/premiazioni/`, `lavorazioni/pulsantiere/`, `lavorazioni/vetrinistica/`, `lavorazioni/plexiglass/`;
- `idee-regalo/calligrafia/`, `idee-regalo/ceralacca/`, `idee-regalo/penne-timbro/`;
- `chi-siamo/`, `novita/` (Promozioni e novità), `privacy/`, `cookie/`.
Timbri, Come lavoriamo e Contatti portano alle sezioni della home (`#timbri`, `#metodo`, `#contatti`); "Prova la tua impronta" porta a `#impronta`.

## Foto da rifare dal vero

Una giornata di still life con luce laterale morbida (finestra o softbox da sinistra, pannello bianco a destra), fotocamera su cavalletto, almeno 3000 px sul lato lungo, fuoco su tutto il pezzo (diaframma chiuso o più scatti uniti):
1. **Apertura**: il leone traforato in ottone cromato, di profilo, steso su un cartoncino neutro e fotografato dall'alto in piano (niente prospettiva), con una luce che faccia brillare le linee incise; meglio ancora su fondo da scontornare. Oggi viene da uno scatto di 1000 px su cartone con segni a matita: a 1x è nitido, su schermi 2x è morbido. Con lo scatto nuovo si può allargare fino a circa 900 px a 1440.
2. **Le lettere in ottone brunito** in macro, stessa luce (oggi 1000 px).
3. **Il banco di via Longhin** con la CNC o il laser al lavoro e le mani di Andrea Tosato su un pezzo appena inciso: darebbe a "I file li prepariamo noi" la sua foto (oggi è solo testo, per non usare macchine di repertorio).
4. **La targa in corten in opera** rifatta più grande (oggi 666 px di altezza, mostrata alla sua misura vera), o un'altra targa loro montata, per la chiusura; oppure la vetrina o la porta del laboratorio.
5. Utili per le pagine interne: un punzone in ottone con il suo segno a caldo, un timbro in metallo con la sua impronta d'inchiostro, una pulsantiera in pietra, una targa in plexiglass sabbiato.

## Licenze

- Nessuna foto di repertorio nella home finale. Le foto Pexels scaricate per i prototipi (Pauline Raw, Dana Sredojevic e le altre in `assets/esterne/`) non sono più usate; licenze in `assets/CREDITI.md`.
- Le foto loro (leone, lettere in ottone, targa in corten) e i loghi vengono dal loro sito: vanno confermati prima di pubblicare.
- Carattere: Encode Sans, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina; testo della licenza in `sito/fonts/OFL.txt`.

## Loghi

Esistono solo raster: `logo-orizzontale-641x114.jpg` (in testata ne uso solo la scritta, in bianco, a 30 px di altezza, 2x) e `logo-verticale-256x200.png` (piede, in bianco sul blu, a 120 px, 2x), con il bianco reso trasparente. Il leone di San Marco con il libro "TARGHE" non si può ricostruire in SVG in modo fedele a questa risoluzione: serve l'originale vettoriale (e il nome del carattere della scritta, che somiglia a Comfortaa). Anche le icone del sito (favicon) vanno rifatte da lì.

## Collaudo da file

Aperta da file://, la pagina non scrive errori in console (il preload del carattere è stato tolto). Su un server la pagina funziona uguale.
