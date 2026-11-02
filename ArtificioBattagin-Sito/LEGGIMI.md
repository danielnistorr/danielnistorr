# L'Artificio Battagin: proposta di nuova home

Proposta non richiesta di una nuova homepage per L'Artificio Battagin (A.B. s.r.l., via della Croce Rossa 5/a, Padova). Solo la home, statica, da aprire in un browser. Nessun contatto con l'azienda, niente di pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale (HTML e CSS in un solo file, un piccolo script per il gesto, il menu e la newsletter).
- `sito/img/`: solo le immagini usate, in JPEG o WebP e in più larghezze (srcset).
- `sito/fonts/`: Gambetta 400, Switzer 400 e 500 in woff2, serviti dalla pagina.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, caratteri, colori, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, caratteri e screenshot (`img_finale.py`, `campiona.py`, `screenshot_finale.mjs`); `prova_gesto.mjs` prova il gesto con mouse e tastiera; `shoot_finale.mjs` e `trova_fuori.mjs` servono ai controlli a varie larghezze.
- `01-analisi.md`: i fatti con le fonti; `_prova/home/a` e `_prova/home/b`: i due prototipi giudicati.

## Pagine del sito nuovo a cui punta la home

Gli indirizzi sono quelli del sito di oggi, da tenere:
`/il-negozio/`, `/belle-arti/`, `/cornici/`, `/workshop/` (Artinpratica, calendario), `/shoponline/`, `/news/`, `/product-category/idee-regalo/gift-card/`, `/condizioni-di-vendita/`, `/resi-e-rimborsi/`, `/spedizioni-e-pagamenti/`. Da creare o collegare: `/privacy-policy/` e `/cookie-policy/` (oggi Privacy e Cookie sono su iubenda: si può puntare direttamente ai documenti iubenda).

## Dati da confermare con l'azienda

Nulla di quanto segue è scritto in pagina finché non viene confermato.

1. **Orari di apertura**: non sono sul sito. Cylex (21/11/2025) indica lunedì solo pomeriggio, martedì 9.00-12.30 e 15.30-19.00, domenica chiuso. Quando arrivano vanno nella chiusura, sotto l'indirizzo.
2. **I cinque profili del gesto**: oggi sono rosso e oro (la cornice di Matteo), oro barocco e argento barocco (i listelli sul banco), nero intagliato con filo oro e laccato blu (due angolari della parete). Servono i nomi veri o i codici a catalogo e la conferma che siano profili che tengono.
3. **La newsletter e lo sconto**: il popup di oggi promette il 15% sul primo acquisto nello shop. Non l'ho messo in pagina: va confermato se è ancora valido. Il popup all'apertura va tolto.
4. **L'origine**: bottega di pitture murali (pagina Il negozio) o laboratorio di cornici ("50 anni fa", post del 30/03/2023)? E l'anno esatto: "anni '70" non basta per un "dal 197x". In pagina c'è solo "anni '70".
5. **Gli anni delle sedi**: Piazza De Gasperi, Via Marin e Via Cavalletto sono senza anno; Via Sarpi "negli anni '90"; Via della Croce Rossa "dal 2007". Per Via Cavalletto il sito dice solo "In seguito".
6. **Capitale sociale** (10.000 euro) e **PEC** (info@pec.artificiobattagin.it) vengono da aziende.it, non da una visura: non sono nella riga legale.
7. **L'email da mostrare**: in pagina c'è negozio@artificiobattagin.it (pagina Contatti); le locandine usano info@.
8. **WhatsApp**: il widget di oggi non dice il numero. Se è il 380 2308602 si può aggiungere un link wa.me accanto al cellulare.
9. **Il marchio sulla cassetta-cavalletto** (`IMG_0393`): inciso davvero o aggiunto in grafica? È un prodotto venduto con il loro marchio? In pagina la didascalia dice solo "con il marchio L'Artificio Battagin".
10. **Il ruolo di Alessia**: il sito nomina Matteo per le cornici, non dice di cosa si occupa lei.
11. **I corsi**: le tre date (13, 21 e 28 novembre 2026), i docenti, gli orari e i prezzi vengono dal calendario del sito al 24/10/2026. Nel sito vero non vanno scritte a mano: la lista va letta dal calendario (The Events Calendar), i prossimi tre eventi. Anche "Nel 2026, ventidue appuntamenti" va calcolato o tolto a fine anno.
12. **"Ampio parcheggio privato"**: viene dalle schede dei corsi (events.json); confermare che valga anche per i clienti del negozio.
13. **Shop online**: quanto spingerlo in home. Oggi è il link accanto al bottone del telefono e una voce del menu.

## Foto da rifare dal vero (con indicazioni di scatto)

La pagina usa una sola foto di repertorio (il muro con la luce di finestra, Unsplash) e foto dell'azienda. Le foto del servizio del 2023 sono online solo a 1000-1080 px: **chiedere al fotografo gli originali a piena risoluzione** (angolari, Matteo, cornici, reparti) e il suo nome per i crediti.

1. **La cornice dell'apertura (la più importante)**. Oggi è una resa composta: i cinque listelli sono ritagliati dalle loro foto e montati con il taglio a 45° su un muro di repertorio. Da rifare così: una parete chiara del negozio, luce naturale dalla vetrina da sinistra (niente flash), cavalletto, macchina frontale e in bolla all'altezza del centro della cornice, obiettivo 50-85 mm, diaframma f/8. La stessa cornice vuota quadrata (circa 50x50 cm) appesa sempre allo stesso chiodo e alla stessa luce, rifatta con i cinque profili scelti (o cinque cornici dello stesso formato), così il gesto resta uguale: almeno 2.880 px di larghezza, RAW, bilanciamento sul muro.
2. **I cinque campioni**: gli angolari veri della parete, scansionati o fotografati frontali su fondo neutro grigio chiaro, luce diffusa, almeno 2.400 px, uno per file, con il nome del profilo nel nome del file.
3. **Matteo al banco**: oggi c'è Matteo che regge la cornice rossa e oro (bella, da tenere). Manca il gesto del mestiere: il taglio del passepartout a 45° e l'assemblaggio. Mani e attrezzo in primo piano, luce laterale, 3.000 px.
4. **La parete degli angolari**: l'originale del fotografo (oggi 1000 px, a 1440 è ingrandita). Se si rifà: frontale, a tutta parete, luce uniforme, 4.000 px di larghezza.
5. **La cassetta-cavalletto**: oggi è scontornata dalla foto su fondo grigio. Da rifare su carta bianca senza cuciture, luce morbida da sinistra, ombra naturale sotto, solo la cassetta aperta, 3.000 px.
6. **I cavalletti in faggio** (chiusura): la foto `IMG_7395` regge (2.560 px); se si rifà, stessa inquadratura con la luce della vetrina e meno neon.

## Licenze

- **Caratteri**: Gambetta e Switzer di Indian Type Foundry, da Fontshare, con la ITF Free Font License (uso commerciale libero, anche sul web; non si possono vendere i file dei caratteri). I file woff2 stanno in `sito/fonts/`.
- **Foto di repertorio**: solo il muro con la luce di finestra, "a square wooden frame hanging on a wall" di In The Making Studio, Unsplash `gx6NxtpgHqY`, Unsplash License (uso commerciale libero, attribuzione non richiesta), verificata il 24/10/2026. La cornice in rovere della foto non si vede: è coperta dalla cornice disegnata. Elenco completo in `assets/CREDITI.md`. Non è usata in nessun'altra home della campagna.
- **Foto dell'azienda**: dal loro sito (servizio fotografico del 2023 e foto del 2023-2024). Vanno chieste formalmente prima di un uso pubblico, insieme ai nomi dei fotografi.
- Nessuna immagine generata dall'IA.

## Logo

Nel piede e nella testata c'è il PNG originale del sito (250x117 px con trasparenza), mostrato a 120-125 px di larghezza, quindi a 2x. Non l'ho ricostruito in SVG: le lettere sono illustrate (la L è un angolo di cornice dorata, la R un pennello, la I una matita) e un ridisegno non sarebbe fedele. **Serve il vettoriale** (AI, EPS, PDF o SVG) dal grafico che l'ha disegnato.

## Newsletter

C'è nel piede: campo email, bottone e casella del consenso con il link all'informativa. **Non invia nulla** finché non si collega a un servizio di invio (per esempio Brevo, Mailchimp o MailerLite): oggi il modulo controlla solo che l'email sia valida e che il consenso sia spuntato. Va collegata con il doppio consenso (double opt-in) e l'informativa aggiornata.
