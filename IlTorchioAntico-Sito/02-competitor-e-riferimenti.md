# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Aperti con Playwright (Chromium, attraverso il proxy) a 1440 e a 390 px: il sito attuale, 7 concorrenti (uno non raggiungibile) e 37 siti provati come riferimento (più 9 che non hanno risposto), 7 tenuti. Tutto è in `_prova/ricerca/`:
- `c0-` il sito attuale, `c1-` ... `c7-` i concorrenti, `r-*` i riferimenti; `-vista` è la prima schermata, senza suffisso la pagina intera;
- `pano/` la pagina intera tagliata in colonne affiancate, per vederla in un colpo; `passi/` le catture fatte una schermata alla volta e cucite (per i siti che con la cattura a pagina intera restano bianchi);
- `ritagli/` i pezzi citati qui sotto, numerati: `00` il materiale del Torchio, `01-12` i riferimenti, `20-27` i concorrenti, `30-31` la prova delle accoppiate;
- caratteri e colori sono letti dal browser (stile calcolato e font caricati, `concorrenti.jsonl`, `rif*.jsonl`, `colori-riferimenti.txt`), i contrasti calcolati con la formula WCAG 2.1 (`_prova/script/r02-contrasto.py`). Script: `_prova/script/r02-*`.

Limiti incontrati, da sapere prima di riaprire i siti:
- il proxy a volte risponde "upstream request failed": Osteria del Guà e La Barchessa di Villa Pisani a 390 sono state rifatte; nella seconda cattura dell'Osteria il CSS della testata si è caricato a metà (menu come elenco puntato): è un artefatto, giudicata sulle parti integre;
- Rocolo Rossato (Valle dell'Agno) risponde con una verifica anti-robot ("Checking the site connection security"): non analizzato;
- molti siti aprono con un video che il Chromium di prova non riproduce (Reschio: "Player error"; La Corte del Belo: riquadro grigio) o con contenuti che entrano in animazione e restano bianchi (Villa Della Torre, Villa Cordevigo, Middleton Lodge, Create, Locanda Margon, Paul Bocuse): Bocuse, Potel et Chabot e Reschio sono stati rifotografati una schermata alla volta (`passi/`);
- non raggiungibili o bloccati: Petersham Nurseries, Villa La Rotonda, Villa Feltrinelli, Landmark Trust (403); Rhubarb, Galateo Ricevimenti, Villa Foscari (nessuna risposta); Lettice ("Access Denied"); l'API di Wikimedia Commons ha risposto "too many requests" (vedi la tavola di Palladio nelle accoppiate).

## Premessa: che cosa è il Torchio Antico e con che cosa lavoriamo

Dal sito attuale (pagine in `_prova/crawl/`): Ristorante Il Torchio Antico, Via Palladio 46, Lugo di Vicenza (VI), "nelle antiche e suggestive barchesse di Villa Godi Malinverni, prima villa di Palladio del 1542"; "da oltre 50 anni" **[DA CONFERMARE: villagodi.com scrive "da oltre 60 anni"]**. Tre attività: ristorante aperto al pubblico ("Aperto tutto l'anno, mezzogiorno e sera", chiuso lunedì e martedì, ferie una settimana a novembre e una a gennaio, "Cucina veneta con menu stagionali e prodotti del territorio"); matrimoni e cerimonie ("vi riserva il locale e vi propone un menu personalizzato", "Nel periodo estivo si utilizza la barchessa all'esterno", può occuparsi di addobbi floreali e musica); catering e banqueting "all'interno delle Vostre dimore o all'interno di indimenticabili Ville, tra le quali Villa Godi Malinverni, Villa Capra Bassani, il Castello di Thiene o il Monastero di San Biagio", per privati e aziende. Posti a sedere: **Sale interne 150, Porticato 180, Giardino 300**. Telefono 0445 860358, cellulare 339 3429942, info@iltorchioantico.com.

Il materiale, base di tutto quello che segue (`ritagli/00-torchio-materiale-galleria.jpg`, `00-torchio-banner-logo.jpg`):
- circa 30 foto da 627-713 px di larghezza (alcune verticali da 354-435 px), amatoriali, molte con dominanti calde o di notte. I soggetti forti sono veri e unici: **il porticato con le colonne di pietra** (8-10 foto), **il vecchio torchio di legno sotto il portico** accanto alla tavolata lunga, la ruota di carro, **il salone affrescato della villa** con lampadario, il giardino con il pozzo scolpito, **il personale in divisa sulla scalinata ad arco**, tre buffet. Nessun piatto fotografato da vicino;
- il banner 1000 x 330 (il portico apparecchiato), l'unica immagine più larga;
- il logo: un torchio stilizzato con stelle, oro su blu (227 x 95) e la scritta "Il Torchio Antico" in corsivo giallo su blu (295 x 49);
- colori misurati sul materiale: **blu del logo #2C52A7**, giallo #E3DB1A, pietra delle colonne #BAB8B4 e #87817B, legno del torchio e delle travi #3B140C e #733710, tovaglie bordeaux #702132 e #822F29, verde del giardino #586C43.

## 1. Concorrenti

Sei strutture vere del Vicentino che si contendono le stesse feste: matrimoni in villa, banchetti, catering per privati e aziende.

| # | Concorrente | Zona | In comune con il Torchio | Cosa fa meglio | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Villa Godi Malinverni](https://www.villagodi.com/) (Palladium SAS, P.IVA 12924220150, altra società) | Lugo di Vicenza, Via A. Palladio 44: **la stessa villa** | sezione "Matrimoni e ricevimenti in villa"; presenta il Torchio come "Ristorante interno"; nel piede "Mail Ristorante ed Eventi: info@iltorchioantico.com" e gli stessi due numeri di telefono del Torchio | video e foto dall'alto della villa e dei giardini, orari di visita stagione per stagione, biglietti e prenotazione della visita, eventi con data (7 giugno 2026, 1 maggio 2026), **posti per sala**: "la Sala Pinacoteca ospita 250 persone in eleganti tavoli rotondi, il Salone Centrale dispone di 100 posti", nove saloni affrescati per le foto | **a 390 scorre di lato** (scrollWidth 529); nel riquadro del Torchio a 1440 **l'immagine è rotta** e si legge il testo alternativo (`ritagli/20`), a 390 al suo posto c'è un piatto impiattato che non si riconosce come del Torchio (`21`); refuso "Villa Godi Maliverni"; titoli in Gilda Display color sabbia #C19B76 su bianco (2,56:1) | `c1-villagodi-*` |
| 2 | [De Pretto Ricevimenti](https://www.deprettoricevimenti.it/) (P.IVA 02149190247) | Schio (VI), Via Paraiso 38 | catering e banqueting per matrimoni, aziende e privati, "ville e luoghi speciali" | **foto vere e professionali del servizio** (camerieri con i vassoi, la pasticceria, `ritagli/22`); sezioni chiare (Cucina, Wedding cake e pasticceria, Matrimoni, Eventi aziendali); una sede propria per gli eventi ("Opificio dei Sogni"); P.IVA nel piede; leggibile a 390 | testo generico ("staff altamente qualificato", "professionalità, puntualità ed eleganza"), ogni blocco finisce con "SCOPRI", nessun numero (ospiti, prezzi, sale); voce di menu "Pasqua in famiglia" a ottobre; a 390, nella nostra cattura, la prima frase è bianca su fondo chiaro e si legge appena (`22b`) | `c6-depretto-*` |
| 3 | [La Corte del Belo](https://lacortedelbelo.it/) (P.IVA 03922500248) | Thiene (VI), Via delle Robinie 10 | ristorante per matrimoni, comunioni, battesimi, lauree; giardino | una pagina per tipo di festa (Matrimoni, Cerimonie, Eventi); piscina e giardino in vista; i bollini di matrimonio.com (Wedding Awards 2023 e 2024, "Consigliato" con 25 recensioni); leggibile a 390. Su matrimonio.com dichiara da 90 € a persona e 80-200 invitati (fonte pubblica, non il loro sito) | **apertura vuota**: un riquadro grigio scuro a 1440 e a 390 nella nostra cattura (probabilmente un video che non parte, `ritagli/23`); testo color malva #9D7B84 su bianco (3,75:1); frasi generiche ("connubio tra eleganza, raffinatezza, qualità e gusto"); nessun numero sul sito | `c3-belo-*` |
| 4 | [Osteria del Guà](https://www.osteriadelgua.it/) e [La Barchessa di Villa Pisani](https://www.labarchessadivillapisani.it/) (AGENA srl) | Bagnolo di Lonigo (VI), Via Risaie | **la stessa formula**: ristorante e sale per eventi nella barchessa di una villa di Palladio (Villa Pisani Bonetti, "realizzata nel 1541") | **prenotazione del tavolo online** in una fascia dedicata (`ritagli/25`), menu pubblicati, foto professionali dei piatti, notizie datate e verificabili (Falstaff, 90/100, 30 settembre 2026; Chiave MICHELIN 2025 e 2026 per il relais); la barchessa disegnata come logo (il portico ad archi); una frase dai Quattro Libri di Palladio in apertura | l'Osteria **a 390 scorre di lato** (scrollWidth 403); la Barchessa a 390 apre con il testo del banner cookie a tutto schermo e una chat automatica sopra ("A che ora è il check-in/check-out?", `27`); quattro caratteri diversi (Caslon, Playfair, Brother 1816, Rosarivo) | `c4-gua-*`, `c4b-barchessa-*` |
| 5 | [Le Tre Grazie](https://www.ristoranteletregrazie.it/) | Vicenza, Viale dell'Oreficeria 21, in Villa Bonin Maistrello | ristorante in villa per matrimoni, banchetti, compleanni, lauree, battesimi, comunioni, cresime | **una pagina per ogni occasione** nel menu; menu da asporto; pagina "I nostri piatti" | **lo stesso difetto del Torchio**: in "Ultimi Eventi e News" ci sono Cenone di Capodanno 2025, Natale 2025, **Pasqua 2023** e un ballo del 18 febbraio 2023 (`ritagli/24`); "Villa Bonin del VIII secolo"; testo grigio #888888 su bianco (3,54:1), titoli oro #B79C17 (2,70:1) | `c5-tregrazie-*` |
| 6 | [Villa Godi Piovene (Porto Godi)](https://www.villagodipiovene.it/it/) | Sarmego di Grumolo delle Abbadesse (VI), Via Venezia 1A | si presenta come "Villa Godi" (come la villa di Lonedo); villa di Scamozzi del 1597 con barchessa a portico, parco di 45.000 m², cappella; matrimoni e cerimonie | richiesta di preventivo strutturata: tipo di evento, numero di invitati a fasce, **"Sei già fornito di catering (cibo e bevande)?"** (`ritagli/26`); pagine Struttura, Parco, Barchessa, Cappella con foto; 161 recensioni Google in pagina | foto ritagliate a cerchio; titoli in The Seasons, testata scura; rischio di confusione nelle ricerche con Villa Godi Malinverni, che ha lo stesso nome | `c2-piovene-*` |
| 7 | Rocolo Rossato | Valle dell'Agno | ristorante per matrimoni, oltre 200 posti (dal loro testo scaricato) | | il sito blocca il browser automatico con una verifica: non analizzato | `c7-rossato-*` |

Il sito attuale del Torchio, per confronto (`ritagli/00-torchio-oggi-1440.jpg` e `-390.jpg`): a 390 la pagina resta larga 1001 px e tutto è rimpicciolito; Arial 14 px; blu #2C52A7 e giallo; "Pasqua 2024" con l'immagine rotta in "Prossimi eventi" e in "Menù Turistici"; modulo con la somma da fare a mano; piede "© 2008 - 2024".

**Cosa fanno meglio del Torchio:** si leggono da telefono (De Pretto, Belo, Tre Grazie, Piovene; Villa Godi e Osteria del Guà scorrono di lato di 13-139 px, il Torchio di 611); mostrano foto fatte da un fotografo (De Pretto, Osteria del Guà); fanno prenotare il tavolo online (Osteria del Guà); chiedono il preventivo con le domande giuste (Piovene: tipo di evento, invitati, catering); datano le notizie e le aggiornano (Osteria del Guà, Villa Godi); danno i posti della sala (Villa Godi: Pinacoteca 250, Salone Centrale 100).

**Cosa non fa nessuno (spazio per il Torchio):**
1. **le tre cose insieme**: ristorante aperto al pubblico, matrimoni nella propria sede, catering nelle ville degli altri. De Pretto è solo catering, Belo e Tre Grazie sono ristoranti con sale, Villa Godi Piovene è una villa senza cucina che chiede agli sposi se hanno già un catering (`ritagli/26`): è il cliente tipo del Torchio Catering;
2. **i posti per spazio, in chiaro**: Sale interne 150, Porticato 180, Giardino 300. Nelle home visitate nessuno li dà così; Villa Godi lo fa per due sale, dentro un paragrafo;
3. **la villa stampata nel libro di Palladio**: Villa Godi compare in pianta e alzato nel Libro II dei Quattro Libri dell'Architettura (Venezia, 1570, [voce Villa Godi su Wikipedia](https://en.wikipedia.org/wiki/Villa_Godi)). La Barchessa di Villa Pisani cita una frase generica dei Quattro Libri; il Torchio sta dentro una villa che è nel libro;
4. **il torchio vero**: l'oggetto che dà il nome al ristorante è sotto il portico, accanto alla tavolata, ed è in 3 foto. Nessun concorrente ha un oggetto così;
5. **notizie che non invecchiano**: Torchio e Tre Grazie mostrano feste passate in home. Nessuno fa scadere da solo un evento passato.

**Attenzione al rapporto con la villa:** villagodi.com è di un'altra società ma manda al Torchio le richieste per ristorante ed eventi (stessa email e stessi telefoni nel piede). Il nuovo sito può dire solo quello che il Torchio scrive di sé; i posti delle sale della villa (Pinacoteca 250, Salone Centrale 100) e chi organizza i matrimoni nelle sale affrescate **[DA CONFERMARE con il cliente]**. Gli anni di attività (50 o 60) **[DA CONFERMARE]**: nel sito si scrive l'anno di apertura, se lo danno, non un contatore.

**Posizionamento proposto:** "Il ristorante nelle barchesse di Villa Godi Malinverni, a Lugo di Vicenza. Aperto tutto l'anno a pranzo e a cena; matrimoni e banchetti sotto il portico (180 posti), nelle sale (150) e in giardino (300); catering nelle ville del Vicentino." Contro Villa Godi Malinverni (stessa villa, sito più ricco ma che scorre di lato e mostra un'immagine rotta proprio sul Torchio) il Torchio diventa il posto dove si mangia e dove si fa la festa; contro De Pretto (catering con foto migliori) ha una sede propria e un ristorante aperto; contro Belo e Tre Grazie ha Palladio, il portico e i numeri.

**Copy evitato** (visto nei concorrenti, e in parte nel Torchio di oggi): "location unica e meravigliosa", "cornice unica / cornice ideale", "momenti indimenticabili", "il giorno più importante", "connubio tra eleganza e raffinatezza", "staff altamente qualificato", "oasi di relax", "esperienza unica", "da oltre N anni".

## 2. Riferimenti premium

Il Torchio non è un hotel di lusso né una villa-museo: è una **casa di ricevimento con cucina propria**, che serve un ristorante aperto, i banchetti nella sua sede e il catering fuori. I riferimenti giusti sono quindi le case di banqueting storiche, i ristoranti di famiglia che hanno una sede per i ricevimenti, e una country house con ristorante ed eventi per il modo di mostrare foto piccole. Sette, tutti aperti e fotografati; per ognuno un gesto preciso e cosa non prendere.

### 2.1 Groupe Potel et Chabot, Parigi ("depuis 1820")
[groupepoteletchabot.com](https://groupepoteletchabot.com/). Casa di ricevimenti e banqueting: tre maisons (Saintclair, Potel et Chabot, Dalloyau), "réceptions privées", matrimoni, "nos lieux d'exception".
- **Gesto da riprendere:** l'apertura è **una foto in bianco e nero della brigata** (camerieri e cuochi che scendono la scalinata di un palazzo con i piatti in mano) e in fondo alla foto, sulla stessa riga, **tre nomi in maiuscolo** che sono le tre porte del sito (SAINTCLAIR, POTEL ET CHABOT, DALLOYAU, `ritagli/01`; a 390 restano su una riga, `01b`). Sotto, "Découvrir nos métiers" **in due colonne di solo testo**: l'etichetta a sinistra, l'elenco dei mestieri a destra, nessuna icona (`02`). Un solo carattere geometrico, Futura PT 300, 500 e 600 (misurato), nero e bianco.
- **Per il Torchio:** il Torchio ha la stessa foto: il personale in divisa sulla scalinata ad arco (642 x 430). In bianco e nero, alla sua misura, diventa la firma della casa. Le tre porte sono RISTORANTE, MATRIMONI E CERIMONIE, CATERING. L'elenco a due colonne serve per il catering: a sinistra "Dove abbiamo cucinato", a destra le ville che il sito nomina.
- **Cosa evitare:** il sito tutto nero (per un ristorante di matrimoni serve luce), la foto a tutta larghezza (le foto del Torchio arrivano a 690 px), il Futura 300 per i paragrafi (troppo chiaro a 17 px).

### 2.2 Paul Bocuse, Collonges-au-Mont-d'Or ("Maison de famille depuis 1924")
[bocuse.fr](https://bocuse.fr/fr/). Ristorante di famiglia con una sede separata per i ricevimenti (Abbaye de Collonges).
- **Gesto da riprendere:** **il piede diviso in due case**: a sinistra RESTAURANT GASTRONOMIQUE con indirizzo, telefono ed email della prenotazione; a destra RÉCEPTIONS & ÉVÉNEMENTS con i recapiti dell'Abbaye e "Visiter le site"; a fianco gli orari d'apertura scritti per esteso (`ritagli/09`). E **l'edificio disegnato**: la locanda dipinta a tratto su un piatto, al posto di una foto (`10`). Foto della brigata in bianco e nero, piatti a colori.
- **Per il Torchio:** il piede con RISTORANTE (aperto al pubblico, orari, giorni di chiusura, telefono fisso) e MATRIMONI E CATERING (cellulare, email, "Chiedi un preventivo"), perché sono due domande diverse. L'edificio disegnato del Torchio esiste già: è la tavola di Villa Godi nel Libro II di Palladio.
- **Cosa evitare:** il serif chiaro spaziato (Antic Didone sottile), i link con la barretta "|" color oro, le animazioni che lasciano la pagina bianca finché non si scorre.

### 2.3 Da Vittorio, Brusaporto (famiglia Cerea)
[davittorio.com, Ristorazione esterna](https://www.davittorio.com/ristorazione-esterna.html). Ristorante di famiglia con catering e una struttura per i banchetti (la Cantalupa).
- **Gesto da riprendere:** la pagina del catering è fatta di **blocchi foto e testo alternati, ognuno con un titolo e un filetto**: WORLDWIDE (il catering fuori), BANCHETTI ed EVENTI (la sede propria), CHIEDI UN PREVENTIVO (una sezione intera, non un popup), GALLERY. Nel blocco dei banchetti **il numero è detto chiaro**: "sale con focolare e giardini che possono ospitare fino a trecento persone" (`ritagli/08`). Nel piede, accanto all'indirizzo: "Chiuso mercoledì a pranzo".
- **Per il Torchio:** stessa struttura per la pagina Catering e banqueting, con i numeri veri (300 in giardino, 180 sotto il portico, 150 nelle sale) e la tavolata lunga sotto il portico accanto al torchio come foto del blocco banchetti. Il giorno di chiusura nel piede.
- **Cosa evitare:** l'oro su bianco (Mrs Eaves color oro), le foto a tutta mezza pagina (le loro sono professionali, le nostre no), il banner cookie in mezzo alla pagina.

### 2.4 Alajmo, Sarmeola di Rubano (PD)
[alajmo.it](https://alajmo.it/). Gruppo di ristoranti di una famiglia veneta ("Il battito di quattro generazioni"); nel piede la voce "Alajmo Event" per gli eventi.
- **Gesto da riprendere:** **i luoghi come parole**: una riga di nomi grandi in maiuscolo (RUBANO (PD), VENEZIA, CORTINA D'AMPEZZO, RONCADE (TV)), quello scelto nero, gli altri grigi, e sotto le foto di quel luogo (`ritagli/03`). E **la mappa a fili**: i locali come punti su una carta a tratto sottile, ognuno collegato da un filo al suo nome e alla città, con il titolo "Quindici modi di darti il benvenuto" (`04`). Colori misurati: nero, bianco, un solo giallo zafferano #F9B026 per i punti.
- **Per il Torchio:** la riga di parole per i tre spazi: SALE INTERNE, PORTICATO, GIARDINO, ognuna con i suoi posti e due foto. La mappa a fili per il catering: Villa Godi Malinverni, Villa Capra Bassani, Castello di Thiene, Monastero di San Biagio, con un solo colore per i punti (il blu della casa). Solo luoghi nominati dal sito, con le coordinate vere **[DA CONFERMARE che ci lavorino ancora]**.
- **Cosa evitare:** i campi neri a tutto schermo, The Seasons (lo usa già Villa Godi Piovene), il carrello e il club fedeltà.

### 2.5 Heckfield Place, Hampshire
[heckfieldplace.com](https://heckfieldplace.com/). Country house georgiana con tenuta agricola, ristorante (Marle) ed eventi.
- **Gesto da riprendere:** **le foto come stampe posate su un tavolo**: due o tre foto per blocco, a misure diverse (da 320 a 405 px di larghezza a 1440), che si sovrappongono di poco, su un fondo pietra misurato #E3DED7; il nome della sezione in maiuscolo spaziato sopra la foto (`ritagli/05`). A 390 diventano una colonna, sempre sfalsate (`07`). Un solo carattere umanista (Johnston, misurato), un rosso #CC2A22 usato solo in piccolo (testata, "Book your stay").
- **Per il Torchio:** è il modo onesto di mostrare foto da 630-690 px: piccole, alla loro misura, in gruppo, come le stampe di una festa. È il gesto della galleria e dei blocchi Matrimoni.
- **Cosa evitare:** il testo lungo tutto in maiuscolo spaziato e centrato (si legge male), il titolo bianco sopra una foto chiara ("House and grounds" sopra il salotto), il video d'apertura (dà errore).

### 2.6 Reschio, Umbria (famiglia Bolza)
[reschio.com](https://www.reschio.com/). Tenuta con hotel, ville in affitto ed eventi stagionali.
- **Gesto da riprendere:** **gli eventi in righe datate**: in ogni riga la data piccola ("September 30, 2026"), il titolo grande in un serif stretto, "Discover more" sottolineato e il numero d'ordine 01, 02, 03 a destra, grigio; le righe separate da un filetto (`ritagli/06`). Nessuna card, nessuna locandina.
- **Per il Torchio:** è la cura per "Pasqua 2024": i menu delle feste e gli eventi come righe con la data sempre in vista, e **la riga sparisce da sola dopo la data** (campo scadenza nel template). Se non ci sono eventi, la sezione non c'è.
- **Cosa evitare:** il video d'apertura ("Player error" nella cattura), i blocchi che compaiono allo scorrimento (pagine bianche a pagina intera), il carattere a pagamento (Canela Condensed).

### 2.7 Cipriani, Venezia ("Simply Italian Since 1931")
[cipriani.com](https://www.cipriani.com/). Ristoranti di famiglia nati con l'Harry's Bar (13 maggio 1931) e sale per "Events & Galas".
- **Gesto da riprendere:** **un dettaglio dell'edificio come foto verticale accanto alla storia**: la porta dell'Harry's Bar (circa 500 x 660 px) che esce dalla fascia chiara sopra e sotto, a fianco un'etichetta in maiuscolo, il titolo e il racconto con nomi e date (`ritagli/11`). Lo stesso impianto per gli eventi, con "Cipriani cuisine and traditional service" (`12`). Futura (light e book, misurato) e un blu notte #14315C.
- **Per il Torchio:** il portico verticale (354 x 500) o il pozzo scolpito (355 x 480) accanto al testo sulla villa e sul 1542: foto piccole che reggono perché sono verticali e alla loro misura.
- **Cosa evitare:** il Futura light per il testo (grigio marrone #54362C su beige, sottile), il fondo beige, i caroselli delle residenze.

### Visitati e scartati

| Sito | Perché no |
|---|---|
| [The Newt in Somerset](https://thenewtinsomerset.com/), [Babylonstoren](https://babylonstoren.com/) | stesso gruppo, stesso impianto da hotel di lusso; titolo in serif corsivo ("Dreaming in Colour"), Cormorant Garamond: il cliché da evitare |
| [Chiswick House & Gardens](https://chiswickhouseandgardens.org.uk/) (villa palladiana a Londra, matrimoni) | EB Garamond corsivo in ogni titolo, popup della newsletter all'apertura |
| [Middleton Lodge](https://middletonlodge.co.uk/), [Butard Enescot](https://www.butard-enescot.com/) | fondo crema e serif display (Butard anche con citazioni in corsivo); di Butard resta l'idea dei luoghi come locandine numerate, non riprese |
| [Il Borro](https://www.ilborro.it/), [Villa Della Torre](https://www.villadellatorre.it/) | Trajan e Cormorant Unicase; Villa Della Torre esce bianca (animazioni) e usa oro e Bembo corsivo: tenuta solo come prova che il Bembo è usato da una villa veneta per eventi (accoppiata C) |
| [Borgo Santo Pietro](https://borgosantopietro.com/), [Ballymaloe](https://www.ballymaloe.ie/), [Les Prés d'Eugénie](https://lespresdeugenie.com/), [Holkham](https://www.holkham.co.uk/) | foto e testo alternati senza un gesto proprio; Ballymaloe con disegni botanici di repertorio |
| [Villa di Maser](https://www.villadimaser.it/), [Villa Valmarana ai Nani](https://www.villavalmarana.com/it/), [Villa Sandi](https://www.villasandi.it/it/) | ville venete con eventi, contenuti utili (orari, degustazioni) ma disegno medio; Valmarana apre con un popup |
| [Dal Pescatore](https://www.dalpescatore.com/it) | conferma che un blu notte regge un ristorante di famiglia di alto livello, ma slider, testata a trama e a 390 scorre di lato (405) |
| [The Admirable Crichton](https://admirable-crichton.co.uk/), [Create](https://createfood.co.uk/) | catering londinesi: Century Gothic e arancio il primo, pagina vuota per le animazioni il secondo |
| [Blue Hill](https://www.bluehillfarm.com/), [Locanda Margon](https://www.locandamargon.it/), [Villa Cordevigo](https://www.villacordevigo.com/) | pagine quasi vuote nella cattura (video e animazioni) |
| [Palladio Museum](https://www.palladiomuseum.org/it/) | un museo, non una casa di ricevimento (carattere monospaziato, linguette nere); utile solo per il titolo della mostra "Geometria, armonia e vita" citato nell'accoppiata A |
| [Aynhoe Park](https://aynhoepark.co.uk/), [Gravetye Manor](https://www.gravetyemanor.co.uk/) | case storiche inglesi per matrimoni: menu a dieci voci e serif spaziato la prima, scritte a mano in corsivo la seconda |
| [Cipriani Events](https://ciprianievents.com/), [Villa Erba](https://www.villaerba.it/), [FAI](https://fondoambiente.it/), [Serego Alighieri](https://www.seregoalighieri.it/en) | Cipriani Events apre con un soffitto decorato e scritte spaziate su rosso (il sito principale cipriani.com è più utile); Villa Erba è un centro congressi in blu elettrico; il FAI è un ente, serif su foto; Serego Alighieri ferma tutto con la verifica dell'età |
| villaemo.org, saint-clair.fr | domini che non sono dell'azienda cercata (un blog e un comune francese) |

## 3. Cosa si riprende (sezione per sezione)

| Sezione del nuovo sito | Gesto | Da | Materiale vero | Limite da rispettare |
|---|---|---|---|---|
| Testata | nome in maiuscolo al centro, menu a sinistra, telefono e "Preventivo" a destra | Potel et Chabot | logo attuale (227 x 95) | serve il logo in vettoriale **[DA CHIEDERE]**; se non c'è, il nome si scrive nel carattere del sito |
| Apertura Home | foto della brigata o del portico in bianco e nero e, sulla stessa fascia, le tre porte RISTORANTE, MATRIMONI E CERIMONIE, CATERING | Potel et Chabot | personale sulla scalinata 642 x 430; banner del portico 1000 x 330 | niente foto a tutta larghezza: al massimo 1000 px a 1440, il resto della fascia è colore pieno |
| Striscia dei fatti | "Aperto tutto l'anno, mezzogiorno e sera", "Chiuso lunedì e martedì", indirizzo, telefono | Da Vittorio (chiusura nel piede), Bocuse (orari) | testi del sito | ferie da aggiornare ogni anno **[DA CONFERMARE le settimane]** |
| Gli spazi | tre parole in riga (SALE INTERNE, PORTICATO, GIARDINO) con i posti e due foto ciascuna; senza JavaScript tre blocchi uno sotto l'altro | Alajmo | 150, 180, 300 posti; circa 10 foto del portico, 6 del giardino, 7 delle sale | a 390 le parole vanno su tre righe, non in scorrimento |
| Matrimoni e cerimonie | blocchi foto e testo con il numero detto chiaro; foto piccole come stampe | Da Vittorio, Heckfield | testi del sito (locale riservato, menu personalizzato, barchessa d'estate, fiori e musica) | foto alla loro misura (630-690 px), mai ingrandite |
| Catering e banqueting | elenco a due colonne ("Dove abbiamo cucinato" / ville) e, se si vuole, mappa a fili; privati e aziende come righe | Potel et Chabot, Alajmo | Villa Godi Malinverni, Villa Capra Bassani, Castello di Thiene, Monastero di San Biagio | solo luoghi citati dal sito **[DA CONFERMARE]**; niente loghi o foto di ville altrui |
| Eventi e menu delle feste | righe datate con numero d'ordine; la riga scade da sola | Reschio | menu di Pasqua 2024 come esempio di formato | se non ci sono eventi la sezione non compare |
| La villa | la tavola di Villa Godi del Libro II come "edificio disegnato"; una foto verticale accanto al racconto | Bocuse, Cipriani | tavola di Palladio (1570, pubblico dominio); portico verticale 354 x 500, pozzo 355 x 480 | la tavola va reperita in alta risoluzione con la fonte **[DA REPERIRE]**; il racconto dice solo "1542" e "prima villa di Palladio" |
| Galleria | stampe sovrapposte di poco, a misure diverse; a 390 una colonna | Heckfield | circa 30 foto | in Elementor gratuito niente posizioni assolute fragili: sovrapposizione con margini negativi, controllata a 4 larghezze |
| Preventivo | sezione intera con domande del settore: tipo di festa, data, invitati, spazio preferito (sala, portico, giardino, catering fuori) | Da Vittorio, Villa Godi Piovene (il modulo) | modulo attuale (nome, città, email, telefono, richiesta) | niente somma da fare a mano: antispam di Contact Form 7 |
| Piede | due colonne: RISTORANTE (orari, chiusure, fisso) e MATRIMONI E CATERING (cellulare, email); sotto ragione sociale, P.IVA, PEC | Bocuse | Le Colline del Palladio S.r.l., P.IVA 03658730241 | P.IVA oggi assente dal piede: obbligatoria |

Scartato in tutte le sezioni: video d'apertura, slider, popup, chat automatiche, recensioni incorporate, contatori di anni, foto stock di piatti, testo grigio chiaro sottile, effetti allo scorrimento.

## 4. Accoppiate

Tre accoppiate, tutte da Google Fonts e tutte nell'elenco di Elementor 4.3.3 (verificato in `includes/fonts.php` dell'istanza di prova `wp-gardenspav` del kit, stessa versione: Jost, Cabin, Cabin Condensed, Cardo). Colori misurati sul materiale del Torchio e sui siti di riferimento. Prova con testi e foto veri del Torchio in `ritagli/30-prova-accoppiate-1440.png` e `31-prova-accoppiate-390.png` (pagina in `_prova/ricerca/prova-accoppiate.html`).

I concorrenti scrivono tutti i titoli in un serif (Gilda Display, The Seasons, Baskervville, Caslon e Playfair, Noto Serif Display) con Roboto, Open Sans, Raleway o Poppins, e usano oro, sabbia o malva. I riferimenti di banqueting usano invece un carattere geometrico (Potel et Chabot e Alajmo Futura PT, Cipriani Futura LT, misurati): è lì che il Torchio si distingue.

### A. "Brigata": Jost, una famiglia (consigliata)

- **Caratteri:** Jost 500 in maiuscolo (spaziatura 0,02 em) per titoli brevi e nome; Jost 600 maiuscolo a 13 px, spaziato 0,12 em, per etichette e per le tre porte; Jost 400 per il testo a 17-18 px, interlinea 1,6; posti e numeri in Jost 500 a 44 px. Mai corsivo, mai pesi sotto 400 per il testo.
- **Perché:** Jost è il Futura libero ("inspired by 1920s German sans-serifs", dalla scheda Google Fonts), cioè il carattere delle case di ricevimento viste dal vivo: Potel et Chabot, Cipriani, Alajmo. È geometria di cerchio e quadrato, la stessa di Palladio (la mostra del Palladio Museum al National Museum of China, febbraio-maggio 2026, si intitola "Geometria, armonia e vita"). Nessun concorrente lo usa; è diverso da Benvegnù (Barlow Condensed, stretto) e dagli altri siti del gruppo.
- **Palette:**

| Ruolo | Colore | Da dove |
|---|---|---|
| inchiostro: testo e titoli | #16191F | il nero di Potel, ammorbidito |
| bianco: fondo | #FFFFFF | tovaglie |
| pietra: fasce di servizio (orari, spazi, piede secondario) | #ECEAE6 | colonne del portico misurate #BAB8B4, schiarite, neutro (non crema) |
| blu Torchio: un campo per pagina (le tre porte, il piede), link, voce attiva | #1F3A73 | blu del logo misurato #2C52A7, stesso tono più profondo; Cipriani usa un blu notte #14315C |
| grigio: note, didascalie | #5B5F66 | |

| Testo su fondo | Contrasto |
|---|---|
| inchiostro su bianco | 17,60:1 |
| inchiostro su pietra | 14,65:1 |
| blu Torchio su bianco / bianco su blu Torchio | 10,99:1 |
| blu Torchio su pietra | 9,15:1 |
| grigio su bianco | 6,42:1 |
| grigio su pietra | 5,34:1 |
| blu esatto del logo #2C52A7 su bianco (alternativa) | 7,31:1 |

- **Foto:** persone e portico in bianco e nero (la brigata sulla scalinata, il portico apparecchiato, il torchio), come Potel et Chabot e Bocuse: unifica foto amatoriali con dominanti diverse. Affreschi, tavola e giardino a colori, perché lì il colore è l'informazione. Sempre alla misura nativa.
- **Rischi:** Jost maiuscolo è largo: nella prova a 390 un titolo di sette parole va su cinque righe (`ritagli/31`): titoli di 2-4 parole, 28 px a 390. Le foto notturne (portico illuminato) in bianco e nero diventano grigie: si scelgono quelle di giorno. Il giallo del logo non torna nell'interfaccia: blu pieno con giallo è il sito di oggi.

### B. "Portico": Cabin Condensed + Cabin

- **Caratteri:** Cabin Condensed 600 in maiuscolo per i titoli; Cabin 400 e 600 per testo, posti, link (sottolineati).
- **Perché:** Heckfield Place scrive tutto in Johnston (misurato); Cabin dichiara di ispirarsi ai caratteri di Edward Johnston ed Eric Gill (scheda Google Fonts). La versione stretta dà ai titoli il ritmo verticale delle colonne del portico. Va con il gesto delle foto come stampe.
- **Palette:** pietra #E8E6E1 come fondo delle sezioni con le foto (Heckfield usa #E3DED7; il nostro viene dalle colonne, più neutro), bianco #FFFFFF, inchiostro #221E1F, **vino #7A2333** dalle tovaglie bordeaux misurate (#702132) per link, un campo e la voce attiva (Heckfield usa il suo rosso #CC2A22 solo in piccolo), grigio #5E5A57.

| Testo su fondo | Contrasto |
|---|---|
| inchiostro su bianco | 16,49:1 |
| inchiostro su pietra | 13,22:1 |
| vino su bianco / bianco su vino | 9,93:1 |
| vino su pietra / pietra su vino | 7,96:1 |
| grigio su bianco | 6,83:1 |
| grigio su pietra | 5,47:1 |

- **Rischi:** il fondo pietra su schermi caldi può avvicinarsi al crema: resta #E8E6E1 e non si scalda. Le foto con le tovaglie rosse più il vino dell'interfaccia fanno troppo rosso: il vino si usa poco. Le stampe sovrapposte sono il pezzo più fragile in Elementor gratuito.

### C. "Libro secondo": Cardo + Jost

- **Caratteri:** Cardo 400 per i titoli da 32 px in su, in tondo, maiuscolo e minuscolo; Cardo 700 per i sottotitoli; Jost 400 e 600 per testo, etichette, posti e pulsanti. Mai il corsivo di Cardo.
- **Perché:** Villa Godi è stampata nel Libro II dei Quattro Libri (Venezia, 1570). Cardo è, per dichiarazione del suo autore, "la mia versione del carattere inciso per Aldo Manuzio e usato per la prima volta nel De Aetna di Pietro Bembo" ([scholarsfonts.net](http://scholarsfonts.net/cardofnt.html)): il carattere dei libri veneziani del Rinascimento. Lo stesso Bembo è il carattere di Villa Della Torre (Allegrini, Fumane), villa rinascimentale veneta con eventi e matrimoni (misurato: bembo-mt-pro). Titoli in serif e testo in un senza grazie è la regola di Bocuse (Antic Didone e Montserrat) e di Alajmo (The Seasons e Futura). Il serif è motivato dal libro in cui la villa è stampata, non dall'abitudine, e sta su bianco, non su crema.
- **Palette:** bianco #FFFFFF, seppia #2B2622 (l'inchiostro della xilografia) per il testo, **blu notte #172B52** per un campo per pagina (dal blu scuro del logo grande, misurato #142647 e #243351), ocra #E3C35A solo su blu notte, per i numeri grandi (dal giallo del logo #E3DB1A, meno acido), grigio #5C5650, fascia #F2F2F0.

| Testo su fondo | Contrasto |
|---|---|
| seppia su bianco | 14,97:1 |
| seppia su fascia | 13,35:1 |
| blu notte su bianco / bianco su blu notte | 13,96:1 |
| blu notte su fascia | 12,46:1 |
| ocra su blu notte | 8,13:1 |
| grigio su bianco | 7,24:1 |
| grigio su fascia | 6,46:1 |
| ocra su bianco | 1,72:1, **mai per testo né per filetti su bianco** |

- **Rischi:** è la più vicina al "classico" bocciato su Benvegnù e ai concorrenti, che sono tutti in serif: tiene solo se resta bianca, dritta e con Cardo grande. Cardo ha solo 400, 700 e corsivo: poche voci.

### Scelta consigliata per la fase 2.3

**A, "Brigata"**, con due innesti: da C la tavola di Villa Godi del Libro II come edificio disegnato nella sezione sulla villa (stampata in blu Torchio su bianco, non come decorazione ripetuta); da B la galleria a stampe alla misura nativa, con un solo livello di sovrapposizione e una colonna a 390. Motivi: è l'unica che nasce dai siti di banqueting veri e non dai siti di ville; tiene il blu del Torchio, quindi il cliente si riconosce; il bianco e nero rende omogenee foto amatoriali che a colori non lo sono; Jost è nell'elenco di Elementor, nessun font da caricare a mano; non somiglia né a Benvegnù né ai concorrenti.

Da confermare con il cliente prima della costruzione: logo in vettoriale; foto originali a risoluzione più alta (quelle sul sito arrivano a 713 px); anni di attività e anno di apertura; settimane di ferie; ville dove fanno ancora catering; chi organizza i matrimoni nelle sale della villa e con quali posti; se esiste un menu attuale da pubblicare. Da reperire: la tavola di Villa Godi dai Quattro Libri in alta risoluzione, con fonte e licenza (opera del 1570, pubblico dominio; la scansione va scelta da una biblioteca digitale).
