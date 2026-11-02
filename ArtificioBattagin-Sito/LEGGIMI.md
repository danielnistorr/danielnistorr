# L'Artificio Battagin: proposta di nuova home

Proposta non richiesta di una nuova homepage per L'Artificio Battagin (A.B. s.r.l., via della Croce Rossa 5/a, Padova). Solo la home, statica, da aprire in un browser. Nessun contatto con l'azienda, niente di pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale, terza versione del 2/11/2026 (HTML e CSS in un solo file, un piccolo script per il gesto, il menu e la newsletter): cornice d'apertura in proporzione 4:3 con la firma del laboratorio, quattro profili, parete degli angolari a 1000 px, la storia in un paragrafo, chiusura senza vuoto. La prima versione del 24/10/2026 è in `_prova/versione-1/index.html` (solo la pagina).
- `sito/img/`: solo le immagini usate, in JPEG o WebP e in più larghezze (srcset).
- `sito/fonts/`: Gambetta 400, Switzer 400 e 500 in woff2, serviti dalla pagina.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (idea, caratteri, colori, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini, caratteri e screenshot (`img_finale.py`, `campiona.py`, `screenshot_finale.mjs`), prova il gesto con mouse e tastiera (`prova_gesto.mjs`), il tocco, il menu, le larghezze da 320 a 2560 e i collegamenti (`controlli_finali.mjs`) e misura i segnali da IA; `shoot_finale.mjs` e `trova_fuori.mjs` servono ai controlli a varie larghezze.
- `01-analisi.md`: i fatti con le fonti; `_prova/home/a` e `_prova/home/b`: i due prototipi giudicati.

## Pagine del sito nuovo a cui punta la home

Gli indirizzi sono quelli del sito di oggi, da tenere:
`/il-negozio/`, `/belle-arti/`, `/cornici/`, `/workshop/` (Artinpratica, calendario), `/shoponline/`, `/news/`, `/product-category/idee-regalo/gift-card/`, `/condizioni-di-vendita/`, `/resi-e-rimborsi/`, `/spedizioni-e-pagamenti/`. Da creare o collegare: `/privacy-policy/` e `/cookie-policy/` (oggi Privacy e Cookie sono su iubenda: si può puntare direttamente ai documenti iubenda).

## Dati da confermare con l'azienda

Nulla di quanto segue è scritto in pagina finché non viene confermato.

1. **Orari di apertura**: non sono sul sito. Cylex (21/11/2025) indica lunedì solo pomeriggio, martedì 9.00-12.30 e 15.30-19.00, domenica chiuso. Quando arrivano vanno nella chiusura, sotto l'indirizzo.
2. **I quattro profili del gesto**: oggi sono rosso e oro (la cornice di Matteo), oro barocco e argento barocco (i listelli sul banco), nero intagliato con filo oro (un angolare della parete). Il quinto, un laccato blu, è stato tolto perché non c'era una foto vera da cui ritagliarlo: si può rimettere (o aggiungere un legno naturale) quando arrivano le scansioni. Servono i nomi veri o i codici a catalogo, la larghezza vera di ogni listello (in pagina sono 60, 52, 56 e 34 px a 1440, a occhio) e la conferma che siano profili che tengono.
2a. **La firma sul passepartout**: "Taglio a 45°, laboratorio di via della Croce Rossa" è composta da due fatti del sito (il taglio del passepartout a 45° dalla pagina Cornici, il laboratorio interno in via della Croce Rossa). Se in bottega firmano o timbrano davvero i passepartout, conviene usare quella dicitura.
2b. **Il colore del muro**: il fondo della pagina (#D9E8E4) è il turchese della parete degli angolari schiarito, campionato dalle foto. Se hanno il codice della tinta della parete (per esempio un RAL o un NCS), conviene partire da quello.
3. **La newsletter e lo sconto**: il popup di oggi promette il 15% sul primo acquisto nello shop. Non l'ho messo in pagina: va confermato se è ancora valido. Il popup all'apertura va tolto.
4. **L'origine**: bottega di pitture murali (pagina Il negozio) o laboratorio di cornici ("50 anni fa", post del 30/03/2023)? E l'anno esatto: "anni '70" non basta per un "dal 197x". In pagina c'è solo "anni '70".
5. **Gli anni delle sedi**: in pagina le vie sono in un solo paragrafo, nell'ordine della pagina Il negozio. Piazza De Gasperi, Via Marin e Via Cavalletto sono senza anno; Via Sarpi "negli anni '90"; Via della Croce Rossa "dal 2007". Per Via Cavalletto il sito dice solo "In seguito": se c'è un anno o un fatto (che cosa c'era in quella sede), va aggiunto nel paragrafo.
6. **Capitale sociale** (10.000 euro) e **PEC** (info@pec.artificiobattagin.it) vengono da aziende.it, non da una visura: non sono nella riga legale.
7. **L'email da mostrare**: in pagina c'è negozio@artificiobattagin.it (pagina Contatti); le locandine usano info@.
8. **WhatsApp**: il widget di oggi non dice il numero. Se è il 380 2308602 si può aggiungere un link wa.me accanto al cellulare.
9. **Il marchio sulla cassetta-cavalletto** (`IMG_0393`): inciso davvero o aggiunto in grafica? È un prodotto venduto con il loro marchio? In pagina la didascalia dice solo "con il marchio L'Artificio Battagin".
10. **Il ruolo di Alessia**: il sito nomina Matteo per le cornici, non dice di cosa si occupa lei.
11. **I corsi**: le tre date (13, 21 e 28 novembre 2026), i docenti, gli orari e i prezzi vengono dal calendario del sito al 24/10/2026. Nel sito vero non vanno scritte a mano: la lista va letta dal calendario (The Events Calendar), i prossimi tre eventi. Anche "Nel 2026, ventidue appuntamenti" va calcolato o tolto a fine anno.
12. **"Ampio parcheggio privato"**: viene dalle schede dei corsi (events.json); confermare che valga anche per i clienti del negozio.
13. **Shop online**: quanto spingerlo in home. Oggi è il link accanto al bottone del telefono e una voce del menu.

## Foto da rifare dal vero (con indicazioni di scatto)

La pagina usa solo foto dell'azienda prese dal sito; nessuna foto di repertorio. Le foto del servizio del 2023 sono online solo a 1000-1080 px: **chiedere al fotografo gli originali a piena risoluzione** (angolari, Matteo, cornici, reparti, matite) e il suo nome per i crediti.

1. **La cornice dell'apertura (la più importante)**. Oggi è una composizione: i quattro listelli sono ritagliati dalle loro foto (sorgenti da 1000-1080 px), tagliati a 45° in Python e montati con `border-image` intorno a un passepartout disegnato in proporzione 4:3, con il titolo al posto dell'opera. Da rifare così: quattro o cinque **barre campione vere** (o cinque angolari della parete) fotografate frontali e in bolla su fondo neutro grigio chiaro, luce diffusa da in alto a destra, macro o 100 mm a f/8, almeno 2.400 px sul lato lungo, una per file con il nome del profilo nel nome del file. Dalla barra dritta si rifà il listello per il `border-image` senza ritagli inclinati. In alternativa, una cornice vera in 4:3 (per esempio 80x60 cm) con il passepartout bianco, fotografata frontale su una parete del negozio, ma allora il titolo non potrebbe stare dentro come testo vero.
2. **I cinque campioni**: gli stessi angolari, scansionati o fotografati come sopra.
3. **Matteo al banco**: oggi c'è Matteo che regge la cornice rossa e oro (bella, da tenere). Manca il gesto del mestiere: il taglio del passepartout a 45° e l'assemblaggio. Mani e attrezzo in primo piano, luce laterale, 3.000 px.
4. **La parete degli angolari**: l'originale del fotografo. Oggi la sorgente è di 1000 px e in pagina non supera i 1000 px CSS (a filo del bordo destro); con un originale di almeno 2.880 px si può tornare alla foto a tutta larghezza. Se si rifà: frontale, a tutta parete, luce uniforme, 4.000 px di larghezza.
5. **La cassetta-cavalletto**: oggi è scontornata dalla foto su fondo grigio e posata sul colore del muro. Da rifare su carta bianca senza cuciture o, meglio, su un cartoncino del colore della parete, luce morbida da sinistra, ombra naturale sotto, solo la cassetta aperta, 3.000 px.
6. **Le matite colorate** (Artinpratica): l'originale del fotografo (oggi 1000 px, tagliata in alto a destra per togliere l'etichetta del marchio). Se si rifà: stessa diagonale, senza etichette di marca nell'inquadratura, 2.400 px.
7. **I cavalletti in faggio** (chiusura): da `IMG_7395` (2.560 px) uso solo il ritaglio in basso a sinistra, il legno della cassetta-cavalletto con i galletti e il cassetto, perché in alto ci sono neon e controsoffitto. Se si rifà: un dettaglio di legno e ottone ad altezza del cassetto, luce della vetrina da sinistra, niente soffitto in quadro, 3.000 px. In alternativa le cornici barocche sul cavalletto (`2023-04_cornici-1.jpg`) quando arriva l'originale.

## Licenze

- **Caratteri**: Gambetta e Switzer di Indian Type Foundry, da Fontshare, con la ITF Free Font License (uso commerciale libero, anche sul web; non si possono vendere i file dei caratteri). I file woff2 stanno in `sito/fonts/`.
- **Foto di repertorio**: nessuna nella seconda versione. Le nove foto Unsplash di riserva (Unsplash License, verificata il 24/10/2026) sono elencate in `assets/CREDITI.md`; la prima versione usava come muro quella di In The Making Studio (`gx6NxtpgHqY`).
- **Foto dell'azienda**: dal loro sito (servizio fotografico del 2023 e foto del 2023-2024). Vanno chieste formalmente prima di un uso pubblico, insieme ai nomi dei fotografi.
- Nessuna immagine generata dall'IA.

## Logo

Nel piede e nella testata c'è il PNG originale del sito (250x117 px con trasparenza), mostrato a 120-125 px di larghezza, quindi a 2x: sul muro e sul bianco i bordi delle lettere si vedono un poco morbidi. Nei file del sito non c'è una versione migliore (le altre sono più piccole o sono solo l'icona "L'ART" a 512 px). Non l'ho ricostruito in SVG: le lettere sono illustrate (la L è un angolo di cornice dorata, la R un pennello, la I una matita) e un ridisegno non sarebbe fedele. **Serve il vettoriale** (AI, EPS, PDF o SVG) dal grafico che l'ha disegnato.

## Newsletter

C'è nel piede: campo email, bottone e casella del consenso con il link all'informativa. **Non invia nulla** finché non si collega a un servizio di invio (per esempio Brevo, Mailchimp o MailerLite): oggi il modulo controlla solo che l'email sia valida e che il consenso sia spuntato. Va collegata con il doppio consenso (double opt-in) e l'informativa aggiornata.
