# L'Artificio Battagin: proposta di nuova home

Proposta non richiesta di una nuova homepage per L'Artificio Battagin (A.B. s.r.l., via della Croce Rossa 5/a, Padova). Solo la home, statica, da aprire in un browser. Nessun contatto con l'azienda, niente di pubblicato.

## Dove sono le cose

- `sito/index.html`: la home, livello professionale del 3/11/2026 con il ritocco finale (HTML e CSS in un solo file, un piccolo script per orari, menu del telefono e modulo). Apertura "Negozio di belle arti a Padova" con il posto degli orari, Chiama, WhatsApp, Come arrivare e ricerca nello shop, e dal computer la foto dei cavalletti a tutta altezza a destra; tre porte (Belle arti, Cornici su misura, Corsi); manifesto e quattro numeri; reparti e marche; cornici con Matteo; i prossimi corsi e le news in una riga; chi siamo; orari e dove siamo con il modulo; fascia del logo; piede.
- `sito/img/`: solo foto dell'azienda (servizio del 2023), in JPEG a più larghezze (srcset), mai ingrandite. L'apertura dal computer usa `apertura-cavalletti-800/1200.jpg`, ritaglio verticale dell'originale da 2560 px. `sito/fonts/`: Gambetta 400, Switzer 400 e 600 in woff2.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (esito delle 15 regole, prove d'uso, controlli).
- `_prova/script/build_finale.sh`: rifà caratteri, screenshot e controlli (`--immagini` rifà anche le immagini con `pro_img.py`); `pro_shoot.mjs` (screenshot), `pro_controlli.mjs` (regole della sezione C e prove della scheda), `pro_largo.mjs` (che cosa esce a destra), `pro_mosaico.py` (pagina lunga in colonne).
- `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa viene a fare. `_prova/crawl/`: calendario dei corsi e ultime news lette dal loro sito il 3/11/2026.
- `_prova/versione-1-originale/`: la home di prima (cornice d'apertura con il titolo dentro e i quattro profili), sito e screenshot. `_prova/versione-1/`: la prima versione del 24/10. `01-analisi.md`: i fatti con le fonti.

## Pagine del sito nuovo a cui punta la home

Gli indirizzi sono quelli del sito di oggi, scritti per intero (`https://artificiobattagin.it/...`) così funzionano anche aprendo il file: `/il-negozio/`, `/belle-arti/`, `/cornici/`, `/workshop/` e le pagine dei tre eventi, `/shoponline/`, la ricerca dello shop (`/?s=...&post_type=product`), `/news/` e tre articoli, `/product-category/idee-regalo/gift-card/`, `/condizioni-di-vendita/`, `/resi-e-rimborsi/`, `/spedizioni-e-pagamenti/`. Da creare o collegare: `/privacy-policy/` e `/cookie-policy/` (oggi Privacy e Cookie sono su iubenda: si può puntare direttamente ai documenti iubenda).

## Cosa chiedere all'azienda

Nulla di quanto segue è scritto in pagina finché non viene confermato.

1. **Orari di apertura (la cosa più importante, da chiedere per prima)**. Non sono sul sito. Cylex (21/11/2025) indica lunedì solo pomeriggio, martedì 9.00-12.30 e 15.30-19.00, domenica chiuso; mancano gli altri giorni. Oggi la pagina dice "Orari: chiamaci prima di venire" in apertura e nel piede, e la regola 14 e la 15 del livello professionale non passano solo per questo. Quando arrivano si scrivono in cima allo script della pagina (`var ORARI = null;`, un elenco di fasce per giorno, 0 = domenica): la riga diventa "Orari di oggi: Aperto ora, fino alle 19.00" o "Ora chiuso, riapre alle 15.30", ricompare il link "Tutta la settimana", in "Orari e dove siamo" compare la tabella della settimana con il giorno di oggi in grassetto e nel piede gli orari in breve (provato con dati di prova, vedi NOTA). Chiedere anche le chiusure per ferie e i festivi.
2. **Le recensioni**. itaglietti.it riporta 689 recensioni su Google con media 4,5 e frasi come "Entri all'Artificio e ti si apre un mondo!" e "Anche per il restauro resta un fornitore top!". Vanno verificate sul loro profilo Google. Senza, la regola 10 del livello professionale (almeno tre tipi di prove) non passa: oggi ci sono i numeri e la fascia delle marche. Dove e come andrebbero: una fascia di tre recensioni subito dopo il blocco verde dei numeri, ognuna con il testo intero, il nome e il comune del cliente (con il permesso), le stelle e la fonte "Google"; sopra, il numero delle recensioni e la media verificati. Non mettere niente in pagina finché non è verificato.
3. **WhatsApp**: in pagina c'è il 380 2308602 (è il numero del widget del sito di oggi, `"phone":"393802308602"`). Confermare che risponda il negozio e chi: la pagina dice solo "Mandaci una foto dell'opera con le misure su WhatsApp".
4. **Le cornici**: prezzo e tempi non sono scritti ("Prezzo e tempi te li dice Matteo, guardando l'opera o la foto"). Se c'è un tempo medio di consegna o un prezzo di partenza per le misure più comuni, si aggiunge. Confermare anche se serve un appuntamento per portare l'opera, e quali misure vuole Matteo nella foto su WhatsApp: se sono quelle dell'opera (larghezza x altezza in cm), il messaggio già scritto del bottone si può completare ("misure dell'opera, larghezza x altezza in cm: ").
5. **Il parcheggio**: "Ampio parcheggio privato" viene dalle schede dei corsi; confermare che valga per tutti i clienti. "Ingresso accessibile" viene dalla scheda Google.
6. **I numeri del blocco verde**: "5 sedi", "Oltre 20" anni di Matteo, "22 corsi e workshop nel 2026" e "186 prodotti nello shop online" (sitemap dello shop, in `01-analisi.md`). Il 186 va ricontato quando il sito vero è in linea, o letto dallo shop; se il numero cambia spesso, meglio toglierlo che lasciarlo vecchio.
7. **I corsi**: le tre date in pagina (13, 21 e 28 novembre 2026), docenti, orari, posti, materiale e prezzi vengono dal calendario del sito al 3/11/2026 (`_prova/crawl/eventi-2026-11-03.json`): olio "Minimo 6, massimo 10 persone", manga e lettering "6-13", materiale incluso per manga (set Manga Fude Pen) e lettering (kit), non incluso per l'olio ("potrà essere acquistato direttamente in negozio"). Nel sito vero la lista va letta dal calendario (The Events Calendar, i prossimi tre eventi), non scritta a mano; anche "22 corsi e workshop nel 2026" va calcolato o tolto a fine anno. Le tre news (23/09, 08/09, 08/07/2026) vanno lette dagli ultimi articoli.
8. **L'origine**: bottega di pitture murali (pagina Il negozio) o laboratorio di cornici ("50 anni fa", post del 30/03/2023)? In pagina c'è solo "Correvano gli anni '70 [...] aprì in pieno centro a Padova la sua prima bottega" e "Dagli anni '70". L'anno esatto servirebbe per un "dal 197x".
9. **Le cinque sedi**: in pagina sono nell'ordine della pagina Il negozio, senza anni tranne Via Sarpi ("negli anni '90") e via della Croce Rossa ("dal 2007"). Il numero "5 sedi in città in cinquant'anni" conta le cinque vie nominate; se la prima bottega in centro era un'altra via, sono sei.
10. **Il ruolo di Alessia**: il sito nomina Matteo per le cornici; di Alessia dice solo che è "al timone" con lui. Una riga su che cosa segue lei (e il suo nome nella sezione Chi siamo) sarebbe utile.
11. **La newsletter e lo sconto**: il popup di oggi promette il 15% sul primo acquisto nello shop. Non è in pagina: va confermato se vale ancora. La newsletter è stata tolta dal piede (non inviava nulla); se la vogliono, si rimette nel piede collegata a un servizio (Brevo, Mailchimp o MailerLite) con doppio consenso, e il popup all'apertura va comunque tolto.
12. **L'email**: in pagina c'è negozio@artificiobattagin.it (pagina Contatti); le locandine usano info@. Il modulo scrive a negozio@.
13. **Capitale sociale** (10.000 euro) e **PEC** (info@pec.artificiobattagin.it) vengono da aziende.it, non da una visura: non sono nella riga legale.
14. **Il vecchio numero**: un record su misterimprese.it ("L Artificio Battagin Sas, via Sarpi 48, 049 8721644") va fatto correggere; in pagina non c'è.
15. **Lo shop online**: in pagina c'è la ricerca nell'apertura e nella sezione Belle arti, la voce di menu e la riga delle spedizioni (10 euro, gratis oltre 79, "nel 90% dei casi in 48/72 ore"). Se lo shop conta più del negozio si può spingere di più.

## Il modulo "Scrivici"

È in "Orari e dove siamo": "Che cosa ti serve?" (Un prodotto, Una cornice su misura, Un corso, Altro), nome, telefono, email, messaggio. Oggi **non invia nulla**: apre il programma di posta di chi scrive con un'email già composta a negozio@artificiobattagin.it, oggetto "Dal sito: <tipo>, <nome>" e i campi nel testo. **Va collegato a un servizio** (il Contact Form 7 che hanno già, o Formspree, Brevo e simili) con l'informativa privacy e un controllo anti spam. La foto di un quadro da incorniciare si manda meglio su WhatsApp, e la pagina lo dice.

## Foto da rifare dal vero (con indicazioni di scatto)

La pagina usa solo foto dell'azienda, tutte dello stesso servizio fotografico del 2023 (otto: reparto belle arti, matite, parete degli angolari, spazio Artinpratica, pennelli, Matteo con la cornice, cavalletti in faggio, open space con le tele); nessuna foto di repertorio, nessuna illustrazione. Online sono a 1000 px (i cavalletti a 2560): **chiedere al fotografo gli originali a piena risoluzione** e il suo nome per i crediti. Oggi l'apertura dal computer usa i cavalletti, l'unica abbastanza grande per la colonna a tutta altezza; con l'originale del reparto belle arti (`2023-05_negozio-bellearti-2.jpg`, gli scaffali pieni) a 3.000 px quella colonna può passare al reparto, che dice "negozio" ancora meglio, senza ingrandire.

Da fare in più, con la stessa luce del servizio (vetrate, mattina, grandangolo moderato):
1. **La facciata e l'ingresso**, con l'insegna e il parcheggio, per la scheda "Orari e dove siamo" (oggi c'è l'open space). Orizzontale 16:9, 3.000 px.
2. **Il reparto in apertura**, originale a piena risoluzione o rifatto: dall'alto, gli scaffali pieni, una persona dello staff al banco che consiglia un cliente (il "consiglio dello staff" è ciò di cui vanno fieri). 4:3 e 16:9, 3.000 px.
3. **Matteo al banco**: il taglio del passepartout a 45° e l'assemblaggio, mani e attrezzo in primo piano, luce laterale. 16:9, 3.000 px. Servirebbe anche per la porta Cornici.
4. **Un corso in corso** nello spazio Artinpratica, con le persone che dipingono (con il loro consenso; niente bambini riconoscibili). 4:3, 2.400 px.
5. **Alessia** (e lo staff) in negozio, per Chi siamo. Ritratto ambientato, 16:9.

## Licenze

- **Caratteri**: Gambetta e Switzer di Indian Type Foundry, da Fontshare, con la ITF Free Font License (uso commerciale libero, anche sul web; non si possono vendere i file dei caratteri). I file woff2 stanno in `sito/fonts/`; Switzer 600 scaricato il 3/11/2026 (copia in `assets/fonts-scaricati/`).
- **Foto di repertorio**: nessuna in pagina. Le nove foto Unsplash di riserva restano in `assets/esterne/` con la licenza in `assets/CREDITI.md`, non usate.
- **Foto dell'azienda**: dal loro sito (servizio fotografico del 2023). Vanno chieste formalmente prima di un uso pubblico, insieme al nome del fotografo.
- Nessuna immagine generata dall'IA.

## Logo

Nella testata c'è il PNG originale del sito (250x117 px con trasparenza), a 76-150 px di larghezza, e prima del piede una fascia bianca con il logo a 250 px (la sua misura vera) accanto al claim; nel piede scuro c'è il nome scritto, perché le lettere blu e verdi del logo non si leggono sull'antracite. Dal logo viene anche l'oro dei due filetti (#D8A000, la L-cornice). **Serve il vettoriale** (AI, EPS, PDF o SVG) dal grafico che l'ha disegnato: le lettere sono illustrate (la L è un angolo di cornice dorata, la R un pennello, la I una matita) e un ridisegno non sarebbe fedele.
