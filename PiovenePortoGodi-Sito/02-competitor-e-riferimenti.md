# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Aperti dal vivo con Playwright (Chromium, attraverso il proxy) a 1440 e a 390 px: il sito attuale, 6 concorrenti (uno blocca i browser automatici) e 35 siti di cantine provati come riferimento, 8 tenuti. Tutto è in `_prova/ricerca/`:
- `c0-` il sito attuale, `c1-` ... `c6-` i concorrenti, `r-*` i riferimenti; `-vista` è la prima schermata, senza suffisso la pagina intera; `*.pezzi/` le catture fatte una schermata alla volta con la rotella e poi cucite (per i siti che scorrono dentro un contenitore o restano bianchi nella cattura a pagina intera);
- `pano/` la pagina intera tagliata in colonne affiancate, per vederla in un colpo;
- `ritagli/` i pezzi citati qui sotto, numerati: `00` il materiale di Piovene, `01-15` i riferimenti, `20-25` i concorrenti, `29-32` la prova delle accoppiate;
- caratteri e colori dei siti sono letti dal browser (stile calcolato e font caricati, `log/*.jsonl`), i colori di fondo campionati sugli screenshot, i contrasti calcolati con la formula WCAG 2.1 (`_prova/script/r02-contrasto.py`). Script: `_prova/script/r02-*` (cattura, verifica dell'età, ritagli, prova delle accoppiate, misura degli sbordamenti).

Limiti incontrati, da sapere prima di riaprire i siti:
- molti siti di vino aprono con la verifica dell'età ("Hai l'età legale per bere alcolici?"): lo script clicca "Sì"; Masi e Haut-Brion chiedono paese e anno di nascita e restano sulla verifica;
- rispondono 403 o con una verifica anti-robot al browser automatico: Inama a 1440, Guerrieri Rizzardi, Pio Cesare, Maculan (prima cattura), Cavazza ("Checking the site connection security"); Serego Alighieri ha risposto una volta "upstream request failed" ed è stato rifatto;
- aprono con un video che il Chromium di prova non riproduce, e la prima schermata resta nera o bianca: Mazzei, Pieropan, Antinori, Tenuta San Guido, Capezzana (pagina bianca anche cucendo le schermate), Fontodi; giudicati sulle parti che si vedono;
- Elena Walch carica le immagini solo allo scorrimento e nella cattura restano vuote; non tenuto;
- non raggiungibili dal proxy: Barbagianni (agriturismo a Toara), Villa Dal Ferro Lazzarini, Costalunga, Le Pignole, Colle di Bugano, Cantina Colli Vicentini, Marchesi Fumanelli, Conte Collalto.

## Premessa: che cosa è Piovene Porto Godi e con che cosa lavoriamo

Dal sito attuale (pagine in `_prova/crawl/r02/`): Piovene Porto Godi Alessandro SS, Via Villa 14, 36021 Toara di Villaga (VI). "Nel cuore della DOC Colli Berici": 220 ettari "tra superfici coltivate a seminativi, un oliveto e bosco, con 28 ettari di vigneti aziendali", in "un anfiteatro naturale nella parte sud dei Colli Berici", vigneti "dal piede della collina fino a una quota di circa 250 m". Vitigni: Tai Rosso, Cabernet Franc e Sauvignon, Merlot, Sauvignon, Pinot Bianco, Garganega. Enologi citati: Enzo Mazzocco, Flavio Prà, Giovanni Nordera. La storia parte da "una mappa del 1584" con "una pianta della casa circondata dal cortile" (proprietario Flavio Barbarano, poi Conti, poi Piovene Porto Godi); la casa è descritta come "la corte di una cascina rossa"; l'agriturismo è "l'antica colombara adiacente alla villa"; le degustazioni sono "a singoli o gruppi. Anche in inglese", con "stanze attrezzate o il grande porticato in giardino". Il vino di punta raccontato dall'azienda è il Thovara, Tai Rosso affinato "in tonneau francesi per un anno", "resa di soli 35 quintali/ettaro".

Il materiale, base di tutto quello che segue (`ritagli/00-piovene-materiale.jpg`, `00-piovene-materiale-2.jpg`, `00-piovene-etichetta-cru.jpg`, `00-piovene-storia.jpg`):
- **le bottiglie fotografate in studio su fondo bianco, 2362 x 3543 px** (Thovara, Pozzare, Fostine, Fra' i Broli verificati; gli altri vini hanno file con lo stesso schema di nome): il materiale migliore che c'è, nitido e grande;
- **le etichette**: la linea con lo stemma (Pozzare, Fostine, Fra' i Broli) ha carta color pergamena, stemma coronato col leone rampante in rosso per i rossi e in verde per i bianchi, "Piovene Porto Godi" in capitali romane con le iniziali più alte, "Vigneto Pozzare" in corsivo inglese, il vitigno in maiuscolo spaziato, l'annata; sullo sfondo lo stemma grande in filigrana tono su tono. Il Thovara ha etichetta bianca, scudetto azzurro-grigio e il nome "THOVARA" in maiuscoletto rosso;
- **il logo**: stemma inciso (versione nera e versione color mora) e "Piovene Porto Godi" in capitali di tipo Traiano; il file più grande è `logo_Piovene_cru.jpg` 3300 x 1172, raster [DA CONFERMARE: esiste un vettoriale];
- foto d'ambiente poche e piccole: vigna 2000 x 633 (l'unica panoramica), colombara-agriturismo 1770 x 2832 (verticale, buona), ghiacciaia con le botti 640 x 480, coppia di famiglia d'archivio 290 x 390, due familiari davanti al muro della villa 290 x 390, facciata della villa con lo stemma sul portale 347 x 463 (il nome del file `410085489_cee230dea3` è quello tipico di Flickr: [DA CONFERMARE la provenienza]), porticato con trattori d'epoca 650 x 487 (pubblicato in un articolo del 2017 su Villa Fracanzan Piovene: [DA CONFERMARE che sia la loro corte]); degustazioni 225 x 265;
- la mappa del 1584 è citata ma non pubblicata [DA CONFERMARE: chiederne una riproduzione];
- colori misurati sul materiale: **tratto scuro dello stemma #2A121E**, **stemma color mora #481830-#54243C**, **rosso del nome "Thovara" #8C3328**, rosso dello stemma sulle etichette dei rossi #92493D, **verde dello stemma dei bianchi #2B6336**, scudetto del Thovara #7E93A7, capsula bordeaux #6E3232.

Il sito attuale, per confronto (`ritagli/20-piovene-oggi-1440.jpg` e `-390.jpg`): Museo 500 grigio #686868 a 15 px, foto della vigna a 640 px di larghezza in una colonna, colonna destra con l'elenco dei vini e "Download Logo", riquadro "Che tempo fa a Toara" vuoto, "Ultime notizie" ferme al 2018, piede "© 2012". A 390 la pagina non sborda (scrollWidth 390) ma il menu è un `<select>` che mostra "– Vigne e Vini".

## 1. Concorrenti

Sei cantine vere che si contendono lo stesso visitatore: chi cerca un vino dei Colli Berici, una degustazione in cantina, un soggiorno in campagna tra Vicenza e Padova.

| # | Concorrente | Zona | In comune con Piovene | Cosa fa meglio | Cosa fa peggio | Ritagli |
|---|---|---|---|---|---|---|
| 1 | [Cantina Pegoraro](https://cantinapegoraro.it/it/) (P.IVA 03742750247) | Barbarano Mossano, Via Calbin 24: a pochi km | Tai Rosso e Tai dei Colli Berici, degustazioni, punto vendita, porticato ("il fascino antico del monastero") | **orari della cantina nel piede** (dal lunedì al sabato, 9.00-12.00 e 15.00-18.30), telefono e due email; **le bottiglie in vista in home** con nome e tipo; modulo di contatto vero; foto del porticato e dei cartoni con il marchio | titoli in Times New Roman di sistema (misurato) accanto a Montserrat; a 390 **il logo nero sta sulla foto scura** della testata e non si legge (`21-pegoraro-390-logo-su-foto.jpg`); ritratto ritagliato a cerchio; bottiglie in un carosello a pallini | `21-pegoraro-*` |
| 2 | [Vini Pialli](https://www.vinipialli.it/) (P.IVA 03059660245) | Barbarano Mossano, Via R. Fabiani 22 | Tai Rosso e Garganega, ospitalità ("Relais Nonno Fiore") | due porte chiare in apertura: "Vini Pialli" e "Relais Nonno Fiore"; una foto vera e grande della casa | la home è solo quella foto e il piede; "© Copyright 2022"; **sborda a destra a 390 (405 px) e a 1440 (1455 px)** per una riga del piede (misurato con `r02-sborda.mjs`); testo del piede attaccato al bordo | `22-pialli-home-1440.jpg` |
| 3 | [Dal Maso](https://www.dalmasovini.com/) | Montebello Vicentino; vigne tra Gambellara, Lessini e Colli Berici | Colli Berici DOC Tai Rosso (Montemitorio, Colpizzarda), visite e degustazioni | "dal 1919" e "quattro generazioni" detti subito; **fila di bottiglie con denominazione e nome**; "Prenota la degustazione" come azione principale; accoglienza separata per privati e aziende | **a 390 la pagina è larga 583 px** (un divisore di Elementor esce a destra: si scorre di lato col dito); foto inclinate con ombra; nomi dei vini in maiuscoletto grigio chiaro poco leggibile; copy da brochure ("viaggio unico", "l'emozione di una degustazione firmata") | `23-dalmaso-vini-visite.jpg` |
| 4 | [Conte Emo Capodilista, La Montecchia](https://lamontecchia.it/) (P.IVA 03650530284) | Selvazzano Dentro (PD), Colli Euganei, una ventina di km in linea d'aria | **lo stesso profilo**: famiglia nobile ("22 generazioni" nel logo), villa del Cinquecento, vino, ospitalità nel borgo, degustazioni | **barra di prenotazione del soggiorno** (arrivo, partenza, ospiti) sotto la foto; stemma e corona nel marchio; P.IVA e contatti nel piede | home con un calendario "fiere e degustazioni 2023" (fermo come le notizie di Piovene); icona di Google+ (servizio chiuso); grandi vuoti bianchi; a 390 testo giustificato con buchi tra le parole e titoli tagliati al bordo ("SPACCIO DEI V...") | `24-montecchia-*` |
| 5 | [Inama](https://inama.wine/) (Soc. Agr. Eredi di Inama Giuseppe s.s., P.IVA 03883480232) | San Bonifacio (VR); vigne nei Colli Berici (il titolo della home: "Soave Classico e Colli Berici") | rossi dei Colli Berici, famiglia, esperienze in cantina | il nome dei Colli Berici nel titolo della pagina; club e iscrizioni curati | a 1440 risponde 403 al browser automatico; a 390 la pagina arriva senza parte dei fogli di stile (probabile effetto dello stesso blocco: non lo conto come difetto) | `25-inama-1440-403.jpg` |
| 6 | Cavazza | Montebello Vicentino, Colli Berici | Colli Berici | | verifica anti-robot ("Checking the site connection security"): non analizzato | `c6-cavazza-*` |

Il caso più vicino per formula è La Montecchia (famiglia, villa, vino e ospitalità); il più vicino per territorio è Pegoraro (Tai Rosso, a pochi chilometri, porticato). Agriturismo Barbagianni, nella stessa Toara, non è raggiungibile dal proxy.

**Cosa fanno meglio di Piovene:** dicono quando si può passare (orari nel piede, Pegoraro); mostrano le bottiglie in home; hanno un'azione chiara per la degustazione (Dal Maso) e per il soggiorno (La Montecchia, Pialli); hanno un modulo.

**Cosa non fa bene nessuno (spazio per Piovene):**
1. raccontare la tenuta con i numeri veri invece che con gli aggettivi: Piovene li ha già scritti (220 ettari, 28 di vigneto, circa 250 m, anfiteatro esposto a sud) e nessuno dei concorrenti li dà;
2. mostrare le etichette come un documento della famiglia: lo stemma coronato, la carta, il nome della vigna. Tutti mostrano bottiglie piccole in carosello;
3. una prova di continuità come la mappa del 1584: nessun concorrente dei Colli Berici ha una data documentata così;
4. un sito che regge da telefono: due su cinque sbordano (Dal Maso 583 px, Pialli 405 px), uno ha il logo illeggibile (Pegoraro), uno taglia i titoli (La Montecchia);
5. freschezza: calendari 2023, copyright 2022, notizie 2018 sono la norma, Piovene compreso.

**Posizionamento proposto per il sito:** "Tai Rosso e vini dei Colli Berici dalla tenuta di Toara di Villaga: 28 ettari di vigna in 220 di campagna, cantina aperta per degustazioni e la colombara per chi resta qualche giorno". Contro Pegoraro e Pialli (vicini, piccoli) Piovene compete sulla tenuta e sulla storia documentata; contro La Montecchia (stessa formula) sul vino del territorio, il Tai Rosso.

**Copy da evitare** (visto nei concorrenti): "emozione", "viaggio unico", "esperienza unica", "entusiasmo", "dalla vigna alla bottiglia", "una terra bellissima", "vini autentici e riconoscibili", "apprezzati in tutto il mondo", e anche la frase del sito attuale "un punto di riferimento per chi cerca vini di alta qualità": al suo posto i premi documentati nella pagina Premi (che si ferma alle guide 2012: da aggiornare con l'azienda) [DA CONFERMARE].

## 2. Riferimenti premium

Piovene è una tenuta di famiglia con stemma, una corte storica, vigne con il nome del luogo e un'ospitalità piccola (una casa, le degustazioni). I riferimenti giusti sono cantine con la stessa natura e siti di livello alto: le grandi tenute storiche (Margaux, Mazzei, Lageder), le famiglie con villa e ospitalità (Ghizzano, Villa Sandi, Coltibuono), e due siti che fanno dell'etichetta e del colore un'identità (Felluga, Palmer). Caratteri misurati (font caricati dal browser, `log/*.jsonl`): dei 30 siti di cantina di cui si sono potuti leggere, **22 usano un carattere con grazie per i nomi e i titoli e un bastoni per testo e interfaccia** (Margaux, Felluga, Mazzei, Ghizzano, Palmer, Allegrini, Antinori, Pieropan, Ricasoli, Volpaia, Walch, Ca' del Bosco, Capezzana, Gresy, Masi, Serego Alighieri, Querciabella, Gobelsburg, Loredan, Maculan, Ama, Haut-Brion); 2 solo un serif (Frescobaldi, San Guido); 6 solo bastoni nell'impianto (Lageder, che usa un serif solo nella finestra della newsletter, Coltibuono, Villa Sandi, Venissa, Weinbach, Fontodi). Il serif, qui, non è un'abitudine: è la regola del settore, e Piovene ce l'ha già nel logo e nelle etichette.

### 2.1 Château Margaux, Médoc ("Premier Grand Cru Classé en 1855")
[chateau-margaux.com](https://www.chateau-margaux.com/). Ritagli `01-margaux-apertura.jpg`, `02-margaux-domaine-numeri.jpg`, `02b-margaux-domaine-390.jpg`, `03-margaux-griglia-vini.jpg`, `03b-margaux-vini-390.jpg`.
- **Cosa fa:** apre con il nome in capitali romane sopra la foto del viale e una sola riga sotto ("Premier Grand Cru Classé en 1855"). "Notre domaine": foto dall'alto della tenuta e, sotto, una fascia quasi nera (#170F0B) con una frase che contiene i numeri ("s'étend aujourd'hui sur 265 hectares, dont une centaine consacrée à la vigne"). "Nos vins": griglia a tre colonne di pannelli alti color pietra (#EBEAE6 su fondo #F0F0EE, misurati), la bottiglia al centro tagliata dal bordo basso del pannello, sotto il nome e la riga "du Château Margaux"; l'ultima cella non è una bottiglia ma la foto della cantina con un solo bottone ("Les millésimes"). A 390 la griglia diventa una colonna e i pannelli restano a tutta larghezza.
- **Il gesto da riprendere:** la griglia dei vini a pannelli con la bottiglia tagliata in basso e il nome sotto, chiusa da una cella foto; la frase con i numeri della tenuta su una fascia scura. Piovene ha esattamente gli ingredienti: bottiglie 2362 x 3543 e la frase "220 ettari di terreni ... con 28 ettari di vigneti aziendali".
- **Da evitare:** i titoli in Cormorant corsivo (anche il titolo d'apertura su tre righe sfalsate), il video del film; la scritta ad arco, che sta bene solo sul loro marchio.

### 2.2 Livio Felluga, Cormons e Rosazzo
[liviofelluga.it](https://www.liviofelluga.it/). Ritagli `04-felluga-etichetta-come-identita.jpg`, `05-felluga-esperienze-asimmetrico.jpg`.
- **Cosa fa:** l'etichetta "Carta Geografica" (una vecchia carta dei colli, "ideata nel 1956") è mostrata piatta, come un documento, in un pannello a mezza pagina, accanto a un paragrafo che ne racconta l'origine. Le sezioni alternano foto a metà pagina e testo, con molto spazio bianco e un solo link piccolo ("Scopri", "Prenota la tua visita"). Testo di lettura in serif (Immortel) a 18-22 px, interfaccia in bastoni piccolo (Suisse Intl).
- **Il gesto da riprendere:** l'etichetta come prova della famiglia, ingrandita e ritagliata dalla foto di studio (lo stemma coronato e "Vigneto Pozzare" dalla bottiglia a 2362 px reggono un pannello di 700 px); e, se la famiglia la fornisce, la mappa del 1584 trattata allo stesso modo: un documento in un pannello, una didascalia vera accanto. Per le degustazioni, la composizione asimmetrica foto e testo con due link ("Scrivete per prenotare", "Come arrivare").
- **Da evitare:** il fondo crema come colore di tutto il sito (lì viene dalla carta della loro etichetta e copre ogni pagina); la verifica dell'età che copre la prima schermata.

### 2.3 Marchesi Mazzei, Castello di Fonterutoli
[mazzei.it](https://www.mazzei.it/). Ritaglio `06-mazzei-scheda-tenuta.jpg`.
- **Cosa fa:** "Our Estates": un contorno d'Italia disegnato a filo con i marchi delle tenute, e accanto per ogni tenuta tre righe di dati con l'etichetta in maiuscolo piccolo: LOCATION, PROPERTY ("650 hectares of overall area (110 vineyards - 114 parcels), From 220 to 570 m a.s.l."), VINES.
- **Il gesto da riprendere:** la scheda della tenuta come righe di dati, con l'etichetta piccola in maiuscolo e il valore sotto: Luogo (Toara di Villaga, parte sud dei Colli Berici), Terreni (220 ettari, 28 di vigneto), Quota (fino a circa 250 m), Vitigni. Accanto, un disegno a filo dei Colli Berici con Toara segnata, da disegnare in vettoriale [DA CONFERMARE la fonte cartografica].
- **Da evitare:** la fisarmonica che nasconde i dati (Piovene ha una sola tenuta: tutto in vista), il blu notte su ogni sezione, il video d'apertura che resta nero.

### 2.4 Alois Lageder, Magrè
[aloislageder.eu](https://www.aloislageder.eu/). Ritagli `07-lageder-scacchiera-numeri.jpg`, `07b-lageder-numeri-390.jpg`, `08-lageder-piede-gps.jpg`.
- **Cosa fa:** la home è una scacchiera di quadrati: foto e testo si alternano, ogni testo ha un titolo in maiuscolo, due o tre righe e un link sottolineato in maiuscolo piccolo. "La nostra tenuta in numeri" è una frase piana: "Anno di fondazione: 1823. Luogo: Magrè, Alto Adige. ... 3 linee di vini. 30 varietà di uva." Il piede è concreto: indirizzi, telefoni, email, **coordinate GPS**, codice di certificazione bio, loghi dei finanziamenti europei piccoli in fondo.
- **Il gesto da riprendere:** l'alternanza foto e testo a quadrati per le pagine Vigne e Storia (dove le foto sono poche e piccole il quadrato le tiene alla loro misura); i numeri detti in una frase, non in contatori; il piede con le coordinate (dal link della mappa della pagina Contatti attuale: 45.388565, 11.514927 [DA CONFERMARE che punti all'ingresso della cantina]) e i loghi del progetto Regione Veneto del 2023, piccoli.
- **Da evitare:** la finestra della newsletter che copre la pagina all'apertura ("Hey you! Thirsty for more?") e il bollo giallo "Book now".

### 2.5 Tenuta di Ghizzano, famiglia Venerosi Pesciolini
[tenutadighizzano.com](https://www.tenutadighizzano.com/). Ritagli `09-ghizzano-casa-ospiti.jpg`, `10-ghizzano-vini-maiuscoletto.jpg`.
- **Cosa fa:** è il caso più simile a Piovene: famiglia nobile, villa, vino, una casa per gli ospiti (Villa Ginevra) e le degustazioni. La casa ha un blocco tutto suo con poche cose concrete (cosa c'è, dove si trova) e "per prenotare scrivi a" con l'email diretta, senza motore di prenotazione. I vini sono bottiglie grandi su fondo chiarissimo (#F8F5F1), un filetto corto sopra il nome in Bellefair maiuscolo e la denominazione in maiuscoletto piccolo colorato.
- **Il gesto da riprendere:** la colombara presentata così: le frasi dell'azienda (due piani, due camere matrimoniali, due bagni, cucina e sala da pranzo, soggiorno, scala a chiocciola, "soltanto per periodi superiori a 4 giorni"), la foto verticale 1770 x 2832, l'email agriturismo@piovene.com e il cellulare. Per i vini: nome della vigna in capitali, vitigno e denominazione sotto, in piccolo.
- **Da evitare:** le icone a filo sopra ogni etichetta di sezione, le foto sovrapposte con cornice, il miscuglio di quattro caratteri (Bellefair, Montserrat, Lato, Playfair).

### 2.6 Villa Sandi, Marca Trevigiana (villa del 1622)
[villasandi.it](https://www.villasandi.it/). Ritagli `11-villasandi-apertura-villa.jpg`, `12-villasandi-indice-filetti.jpg`, `13-villasandi-piede-stemma-psr.jpg`.
- **Cosa fa:** una villa veneta con cantina: apre con la facciata dritta, frontale, all'imbrunire. A metà pagina un indice di tre righe ("The Family", "Villa Sandi", "Estates"), ognuna con una riga di spiegazione e un link a destra, separate da filetti. Nel piede la villa incisa con "Anno 1622", lo stemma, e i loghi del PSR Veneto in un riquadro bianco.
- **Il gesto da riprendere:** l'indice a righe con filetto per la parte "Azienda" (Storia, La lezione del tempo, Le vigne, Premi), al posto dei menu a tendina di oggi; lo stemma inciso piccolo nel piede, sopra la ragione sociale, e i loghi del progetto Regione Veneto nello stesso modo (Piovene ha un articolo "progetto regione Veneto" del 2023 con i loghi: `wp-content/uploads/2023/07/loghi-cpv.png`).
- **Da evitare:** il maiuscolo largo (Sackers Gothic) su tutti i testi, i sottotitoli in grigio chiaro così piccoli che nello screenshot quasi non si leggono, il carosello delle bottiglie.

### 2.7 Badia a Coltibuono, Gaiole in Chianti ("A.D. 1051")
[coltibuono.com](https://www.coltibuono.com/). Ritaglio `14-coltibuono-stemma-data.jpg`.
- **Cosa fa:** prima schermata con il nome, sotto lo stemma inciso e una data; poi una frase che mette insieme i numeri e il luogo ("incastonata in 800 ettari di bosco"). Vino e ospitalità (camere, appartamenti, ristorante, visite e degustazioni) sono nella stessa home, uno dopo l'altro.
- **Il gesto da riprendere:** lo stemma inciso del logo usato da solo, grande, una volta, con sotto una data vera: per Piovene "Mappa del 1584" (mai "dal 1584": la mappa documenta la casa e le viti, non la nascita dell'azienda). E l'ordine della home: la tenuta, i vini, poi le due porte per chi viene (degustazioni, colombara).
- **Da evitare:** il fondo nero con testo sottile chiaro (bastoni sottili, peso 200-300, su #1A1A1A), cioè la "dark mode a basso contrasto" dei divieti.

### 2.8 Château Palmer, Margaux
[chateau-palmer.com](https://www.chateau-palmer.com/). Ritaglio `15-palmer-campo-pieno.jpg`.
- **Cosa fa:** "Millésimes": un campo pieno di colore (#BC7E6A, su fondo pagina #CBAFA6) con il titolo in alto a sinistra, il testo in basso a sinistra e la foto delle bottiglie a destra; il colore viene dalla casa, non da una palette di moda. Nel piede, il castello inciso, piccolo e in tono.
- **Il gesto da riprendere:** una sola fascia piena per pagina nel colore dello stemma (mora), con il Thovara: titolo in alto, le frasi dell'azienda in basso, la bottiglia a destra.
- **Da evitare:** l'impianto da rivista (ritratti, film, "Les intelligences particulières"), i titoli in bastoni largo maiuscolo.

### Visitati e scartati

| Sito | Perché no |
|---|---|
| [Tenuta San Guido](https://www.tenutasanguido.com/), [Gaja](https://www.gaja.com/) | San Guido è una sequenza di video a tutta pagina con il menu a lato; Gaja è una pagina nera con il nome e l'indirizzo: bellissimi per chi è già famoso, inutili per chi deve spiegare un vitigno come il Tai Rosso |
| [Allegrini](https://www.allegrini.it/), [Antinori](https://www.antinori.it/), [Pieropan](https://www.pieropan.it/) | verifica dell'età e prima schermata a video; Allegrini colora di rosso le parole d'accento dei titoli in Bodoni (il gesto vietato, in un altro colore) |
| [Frescobaldi](https://www.frescobaldi.com/), [Loredan Gasparini](https://www.loredangasparini.it/), [Ca' del Bosco](https://www.cadelbosco.com/) | crema e oro con serif enormi (Frescobaldi), nero e oro (Loredan, Ca' del Bosco): il cliché del "lusso" che il cliente ha già bocciato |
| [Masi](https://www.masi.it/) | campagna di moda (abito rosso a Venezia): fuori dal carattere di una tenuta agricola |
| [Barone Ricasoli](https://www.ricasoli.com/), [Marchesi di Gresy](https://www.marchesidigresy.com/), [Castello di Volpaia](https://www.volpaia.com/) | griglie affollate con chat e bottoni ovunque (Ricasoli), foto con cornice e ombra (Gresy), fasce scure sovrapposte alle foto (Volpaia) |
| [Castello di Ama](https://www.castellodiama.com/), [Venissa](https://www.venissa.it/) | Ama: quattro colonne con il testo solo al passaggio del mouse; Venissa: buona apertura (vigna e campanile dall'alto) ma il resto è un piede grigio |
| [Serego Alighieri](https://www.seregoalighieri.it/) | stessa formula (famiglia, villa, foresteria) e barra di prenotazione, ma bottoni blu e tessere scure: utile solo come conferma della barra di La Montecchia |
| [Elena Walch](https://www.elenawalch.com/), [Capezzana](https://www.capezzana.it/), [Fontodi](https://www.fontodi.com/), [Domaine Weinbach](https://www.domaineweinbach.com/) | immagini o contenuti che non si caricano nella cattura (pigri o animati); Walch usa Marcellus maiuscolo, annotato come uso reale di un Traiano libero |
| [López de Heredia](https://www.lopezdeheredia.com/), [Schloss Gobelsburg](https://www.gobelsburg.at/), [Querciabella](https://www.querciabella.com/), [Haut-Brion](https://www.haut-brion.com/), [Yquem](https://www.yquem.fr/) | Heredia e Gobelsburg sono pagine fitte di testo e bollini; Querciabella apre con la newsletter; Haut-Brion e Yquem non superano la verifica dell'età |
| Guerrieri Rizzardi, Pio Cesare, Maculan | 403 al browser automatico |

## 3. Cosa si riprende (sezione per sezione)

Una proposta di impianto da verificare in 03 e in 2.3: ogni riga dice il gesto, da chi viene e quale materiale di Piovene lo regge. Le misure delle foto sono quelle native: nessuna va mostrata più grande.

| Sezione del nuovo sito | Gesto | Riferimento | Materiale Piovene | Limite |
|---|---|---|---|---|
| Testata | logo (stemma e capitali) a sinistra, menu su una riga, voce attiva in rosso etichetta con filetto sotto; a telefono menu a scomparsa vero, non il `<select>` di oggi | Margaux, Felluga | `logo_Piovene_cru.jpg` 3300 x 1172 | logo raster: chiedere il vettoriale |
| Apertura Home | nome del luogo in piccolo, titolo breve ("Nel cuore della DOC Colli Berici"), due righe del testo dell'azienda, foto della vigna accanto; sotto, una riga di dati con filetto | Margaux (apertura), Mazzei (dati) | vigna 2000 x 633 (a 1440 al massimo 1440 x 456 a tutta larghezza, o 720 di larghezza a metà) | nessuna foto della corte o della villa a risoluzione buona: brief foto nel LEGGIMI |
| La tenuta in numeri | righe di dati con etichetta piccola maiuscola: Luogo, Terreni, Vigneti, Quota, Vitigni; frase piana, niente contatori animati | Mazzei, Lageder, Margaux ("Notre domaine") | testi della home attuale | disegno a filo dei Colli Berici da fare in vettoriale |
| I vini | griglia a pannelli: bottiglia di studio tagliata dal bordo basso del pannello, nome della vigna in capitali (rosso per i rossi, verde per i bianchi, come lo stemma sull'etichetta), vitigno e denominazione sotto; ultima cella una foto con un solo link | Margaux, Ghizzano | bottiglie di studio a 2362 x 3543 su fondo bianco (verificate Thovara, Pozzare, Fostine, Fra' i Broli; gli altri vini hanno file con lo stesso schema): pannello bianco su fascia pietra, così il fondo della foto coincide col pannello | i nomi completi dei vini e le denominazioni vanno presi dalle schede tecniche (alcuni nomi sul sito sono incoerenti: "Garganego Riveselle" e "Garganega") [DA CONFERMARE] |
| Thovara, il vino di casa | una fascia piena color mora, titolo in alto, frasi dell'azienda in basso ("resa di soli 35 quintali/ettaro", "tonneau francesi per un anno"), bottiglia a destra | Palmer | `Thovara.jpg` 2362 x 3543 | una sola fascia piena per pagina |
| Storia | l'etichetta e la mappa come documenti, in un pannello, con una didascalia vera; la foto d'archivio dei coniugi alla sua misura (290 px) | Felluga, Coltibuono (stemma e data) | etichetta Pozzare ritagliata dalla foto di studio; mappa del 1584 [DA CONFERMARE]; `conti.jpg` 290 x 390 | la mappa non è sul sito: senza la riproduzione la sezione usa solo l'etichetta |
| Indice dell'azienda | righe con filetto: Storia, La lezione del tempo, Le vigne, Premi, ognuna con una riga e un link | Villa Sandi | testi delle pagine attuali | |
| Degustazioni | foto a metà, testo dell'azienda ("a singoli o gruppi. Anche in inglese", "stanze attrezzate o il grande porticato in giardino", "È gradita la prenotazione"), due link: email e telefono | Felluga ("Esperienze"), Dal Maso (azione chiara) | foto degustazioni 225 x 265: non basta, serve una foto nuova | orari della cantina non pubblicati [DA CONFERMARE] |
| Agriturismo, la colombara | blocco unico con i fatti della casa, foto verticale, email agriturismo@piovene.com e cellulare 340 8543966; niente motore di prenotazione | Ghizzano (Villa Ginevra) | `agriturismo.jpg` 1770 x 2832 | prezzi e periodi non pubblicati [DA CONFERMARE] |
| Piede | ragione sociale e P.IVA, indirizzo, telefoni, email, coordinate, stemma inciso piccolo, loghi del progetto Regione Veneto in un riquadro, anno corrente | Lageder, Villa Sandi, Pegoraro (orari) | dati della pagina Contatti, `loghi-cpv.png` | |

Scartato da tutti i riferimenti: video in apertura, verifica dell'età a tutta pagina, finestre della newsletter, caroselli automatici di bottiglie, parole d'accento in corsivo o colorate, fondo crema o nero come colore di tutto il sito, filigrana dello stemma a tutta pagina (sta bene sull'etichetta, sul sito diventa carta da parati), foto inclinate o a cerchio.

## 4. Accoppiate

Tre accoppiate, tutte da Google Fonts e tutte nell'elenco di Elementor 4.3.3 (verificato in `includes/fonts.php` dell'istanza di prova `wp-gardenspav` del kit, stessa versione: Cinzel, Source Sans 3, Alegreya, Alegreya SC, Alegreya Sans, Instrument Sans). Nessun concorrente le usa (oggi: Museo 500 per Piovene, Montserrat e Times per Pegoraro, Roboto per Pialli, Kalnia e Google Sans Flex per Dal Maso, Open Sans per La Montecchia). Nessuna usa il corsivo. Prova di ognuna con i testi veri del sito e le bottiglie vere: `ritagli/30-prova-A-etichetta-1440.jpg`, `30b-prova-A-etichetta-390.jpg`, `31-prova-B-carta-1440.jpg`, `32-prova-C-cantina-1440.jpg` (sono prove di caratteri e colori, non l'impianto); confronto dei titoli con il logo in `29-caratteri-titoli-contro-logo.jpg`.

### A. "Etichetta": Cinzel + Source Sans 3 (consigliata)

- **Caratteri:** **Cinzel** 500 per i titoli brevi (48-56 px a 1440, 32-34 px a 390) e per i nomi dei vini (24-26 px, spaziatura 0,08 em); **Source Sans 3** 400 per il testo (18 px, interlinea 1,6), 500-600 per menu, bottoni e dati, le etichette dei dati in maiuscolo 13 px spaziato 0,14 em. Cinzel non va mai nel testo corrente né sotto i 18 px.
- **Perché:** il logo e le etichette di Piovene sono composti in capitali romane con le iniziali più alte e il resto in maiuscoletto ("Piovene Porto Godi" sull'etichetta del Pozzare, "THOVARA" su quella del Thovara). Cinzel lavora esattamente così: ha solo maiuscole e le minuscole escono come maiuscoletti (verificato nella prova), ed è "a typeface inspired in first century roman inscriptions, and based on classical proportions" (descrizione del progetto, github.com/NDISCOVER/Cinzel), lo stesso modello delle capitali del logo. Nel confronto con il logo (`29-...`) è il più vicino insieme a Forum, che però è più leggero e meno leggibile piccolo. La coppia capitali romane per nomi e titoli, bastoni pulito per il resto è quella di Margaux (capitali nel marchio e nella riga "Premier Grand Cru Classé", Brandon Grotesque per il testo), di Ghizzano (Bellefair maiuscolo e Montserrat) e di Walch (Marcellus maiuscolo). Source Sans 3 (Adobe) è un bastoni chiaro e sobrio, leggibile a 15 px su telefono, con pesi dal 200 al 900.
- **Colori:**
  - bianco #FFFFFF, fondo di base;
  - pietra #ECEAE5, fasce dei vini e di servizio (un grigio caldo come il #EBEAE6 dei pannelli di Margaux, non un crema: il crema non sta sulle etichette di Piovene, il Thovara è bianco);
  - inchiostro #2A1720, testo e filetti (il tratto scuro dello stemma, misurato #2A121E);
  - mora #4A1F33, una sola fascia piena per pagina e il testo dei bottoni chiari (lo stemma in versione colore, misurato #481830-#54243C);
  - rosso etichetta #8C3328, nomi dei rossi, voce di menu attiva, link (il "THOVARA" dell'etichetta, misurato);
  - verde cru #2B6336, solo per i nomi dei bianchi (lo stemma verde sull'etichetta del Fostine, misurato);
  - grigio mora #5E5157, testi secondari e didascalie; rosa chiaro #E4C9C3 per le etichette piccole sulla fascia mora.
- **Contrasti (WCAG 2.1):**

| Testo su fondo | Rapporto |
|---|---|
| inchiostro #2A1720 su bianco / su pietra | 16,91:1 / 14,07:1 |
| grigio mora #5E5157 su bianco / su pietra | 7,53:1 / 6,26:1 |
| rosso etichetta #8C3328 su bianco / su pietra | 8,02:1 / 6,67:1 |
| verde cru #2B6336 su bianco / su pietra | 7,14:1 / 5,94:1 |
| bianco su mora #4A1F33 (e mora su bianco nei bottoni) | 13,68:1 |
| rosa chiaro #E4C9C3 su mora | 8,76:1 |

- **Rischi:** Cinzel è largo: a 390 un titolo di sei parole occupa due righe a 34 px (provato, `30b-...`), oltre va accorciato il titolo, non ridotto il corpo. Usato per frasi lunghe sembra un'insegna: per questo resta su nomi e titoli brevi.

### B. "Carta": Alegreya + Alegreya SC + Alegreya Sans

- **Caratteri:** **Alegreya** 500 per i titoli in tondo (minuscolo), **Alegreya SC** 500 per i nomi dei vini in maiuscoletto vero, **Alegreya Sans** 400/500 per testo e interfaccia. Una sola famiglia con le tre voci.
- **Perché:** Felluga compone il testo di lettura in un serif di libro e tratta l'etichetta come un documento: questa è la versione "da archivio", per una casa che parte da una mappa del 1584. Alegreya è "originally intended for literature" e "conveys a dynamic and varied rhythm which facilitates the reading of long texts", con "a Small Caps sister family" (descrizione del progetto, github.com/huertatipografica/Alegreya): un maiuscoletto vero, come sull'etichetta. Le fasce piene mora vengono da Palmer.
- **Colori:** bianco #FFFFFF; pietra #EEEBE4; inchiostro #231A1E; mora #4A1F33 (qui per due fasce per pagina, come i campi di Palmer); rosso etichetta #8C3328; grigio #5B5257; lilla chiaro #E9D6DF per le etichette su mora.
- **Contrasti:** inchiostro su bianco / pietra 16,96:1 / 14,25:1; grigio 7,53:1 / 6,32:1; rosso 8,02:1 / 6,73:1; bianco su mora 13,68:1; #E9D6DF su mora 9,87:1.
- **Rischi:** è la più calda e la più "libro": vicina a un sito di editore più che di cantina; nella prova i titoli in tondo hanno meno presenza del logo che li sovrasta.

### C. "Cantina": Instrument Sans, una famiglia

- **Caratteri:** **Instrument Sans** 500 maiuscolo spaziato 0,06 em per i titoli, 600 maiuscolo 0,1 em per i nomi dei vini, 400 per il testo. Il logo resta l'unico elemento classico.
- **Perché:** è la via di Lageder (titoli in maiuscolo di un bastoni, foto e testo a scacchiera), di Coltibuono (Manrope e un bastoni sottile per i titoli) e di Venissa (Helvetica Neue): le cantine che puntano sulla vigna più che sulla casata. È la più moderna e la più facile da tenere coerente in Elementor.
- **Colori:** bianco #FFFFFF; pietra #EDEDEA; inchiostro #1F1D1D; verde cru #2B6336 (link, nomi, fascia piena); grigio #585656; verde chiaro #D5E6D8 per le etichette sulla fascia verde.
- **Contrasti:** inchiostro su bianco / pietra 16,78:1 / 14,30:1; grigio 7,29:1 / 6,22:1; verde su bianco / pietra 7,14:1 / 6,09:1; bianco su verde 7,14:1; #D5E6D8 su verde 5,49:1.
- **Rischi:** stacca il sito dalle etichette e dallo stemma, cioè da quello che Piovene ha di unico; il verde pieno legge "agricolo" generico.

### Scelta consigliata per la fase 2.3

**A, "Etichetta"**, con due innesti: da B la regola della fascia piena color mora (una per pagina, per il Thovara o per la storia), da C la regola che i titoli di servizio (orari, dati, schede tecniche, piede) stanno nel bastoni maiuscolo piccolo e non in Cinzel. Il sistema viene tutto dalla bottiglia: capitali romane e maiuscoletto come sull'etichetta, rosso del nome del Thovara, verde dello stemma dei bianchi, mora dello stemma, pietra al posto della carta, e le bottiglie di studio a 2362 px come prime protagoniste perché sono il materiale migliore che l'azienda ha.

Da confermare con il cliente prima della costruzione: logo in vettoriale; riproduzione della mappa del 1584; provenienza delle foto della facciata e del porticato; orari della cantina; schede tecniche aggiornate e nomi esatti dei vini (annate in commercio); premi successivi al 2012; periodi e condizioni dell'agriturismo. Foto da fare (brief nel LEGGIMI): la corte e la cascina rossa, il porticato in giardino, la colombara da fuori, la cantina e la ghiacciaia a risoluzione piena, la vigna del Tai Rosso, la famiglia.
