# Area Systems: analisi per la nuova home

Sito: https://www.areasystems.it (crawl e screenshot del 19/10/2026: home, 61 pagine interne su 65 della sitemap, area download, catalogo PDF 2022). Il blocco "IIS 10.0 Detailed Error 999.0" della nota iniziale oggi non c'è: con curl e un user agent da browser, e con Chromium, il sito risponde 200. Fonti citate come URL + frase; le pagine del sito sono indicate con il nome del file dopo `areasystems.it/`.

## 1. In breve

- **Chi**: Area Systems srl, sede legale in via Brescia 6 a Saonara (PD), sede operativa in via San Marco 10 a Tombelle di Vigonovo (VE). Società attiva "dal 2016" (aziende.it). Piccola: 2 dipendenti e 495.699 euro di ricavi nel 2024 (aziende.it, dati del Registro Imprese).
- **Cosa fa davvero**: non è un'azienda di "sistemi" o di impiantistica, come fa pensare il nome. Vende componenti per il quadro elettrico, quasi tutti per tenerlo alla temperatura giusta ("Catalogo thermal solution"): gruppi di ventilazione con filtro, torrini, ventilatori assiali e centrifughi, condizionatori da parete, da tetto e ad aria compressa, resistenze anticondensa, termostati e igrostati. Accanto: alimentatori Mean Well, relè e zoccoli Relpol, finecorsa e microinterruttori, lampade LED da quadro, guaine e calze trecciate, lo sticker antincendio MAUS Stixx.
- **Come**: in parte è distributore di marchi dichiarati (ACDCFAN, Commonwealth, Jason Fan, ECOFIT, Mean Well, Relpol, Lonyung), in parte vende linee con sigla propria (ASB, ASVC, ASVE, ASRC, ASTH, AS-CC, AS-T5), che per l'ASRC dice "ideata da Area Systems". Chi le produca non è scritto (sez. 8).
- **Per chi**: quadristi, costruttori di macchine e impianti. Il sito cita tre mondi: accumulo di energia ed eolico/fotovoltaico, telecomunicazioni e data center, macchinari industriali ("macchine CNC, macchine per stampaggio a iniezione, impianti essiccazione plastica, gruppi frigo, pompe di calore").
- **Il punto**: il loro mestiere è il clima dentro una scatola di lamiera grigia RAL 7035. Il soggetto visivo vero è uno solo per volta: la ventola, la griglia, l'aletta del dissipatore. È un registro tecnico, non di lusso.

## 2. Il sito di oggi

**Pagine** (menu, pagine di `index.html`): Home Page, Azienda, Prodotti (11 famiglie e circa 45 schede), Applicazioni, Contatti, Lavora con noi, Area download, Area E-commerce, Compliance (due pagine: acdcfan, lonyung).

**Testi veri essenziali (verbatim)**:
- Home: un solo titolo, "I nostri prodotti", e 12 riquadri. Esempi: "Condizionamento: Gamma da 350W a 4000W Condizionatori d'aria compatti per interni ed esterni: maggiore efficienza e minor vibrazioni."; "Riscaldamento: Riscaldatori anticondensa statici e ventilati"; "Ventilatori EC: Una nuova tecnologia nel campo della ventilazione e del controllo del flusso d'aria con un' alta efficienza energetica e una lunga durata".
- Azienda: "Area Systems Srl è un punto di riferimento per il mercato industriale italiano, grazie alla capacità di progettare e fornire soluzioni tecnologiche innovative e personalizzabili." Poi 7 "Settori di Competenza": "Ventilazione e Climatizzazione", "Riscaldamento Industriale", "Monitoraggio e Controllo Ambientale", "Illuminazione Tecnica", "Componenti Elettronici", "Sicurezza Antincendio", "Materiali Speciali".
- Gruppi ASB: "fissaggio a scatto senza viti", "compatibilità con le dime standard", "ABS UL94V0", "ventilatore assiale su cuscinetti a sfera", "fino a 50.000 ore a 40°C", "RAL 7035 (standard) e RAL 7032 (su richiesta)", "da -10°C a +70°C", "IP54". Misure: 114x114, 150x150, 204x204, 250x250, 325x325 mm.
- Torrini: "progettato per aspirare l'aria calda dalla parte superiore del quadro"; portate da 500 a 1500 mc/h (GT500...GT1500).
- Condizionatori ASVC: "ottimizzati per il montaggio sulla porta o sui pannelli laterali dei quadri di qualsiasi marca", "gamma di potenza frigorifera da 350W a 4000W", "compressori rotativi". ASRC (da tetto): "potenze frigorifere comprese tra 500 W e 4000 W".
- Resistenze CTSH: "Riscaldatore touch safe, compatto e leggero", "Potenza da 25 a 150 W", "PTC autoregolante", "-45/+70", "Montaggio su guida DIN 35 mm EN50022".
- Antincendio: "Quando la temperatura raggiunge i 380°C, lo Sticker antincendio sprigiona radicali di potassio".
- Lavora con noi: "Area Systems Srl investe costantemente nelle proprie Persone e nella tecnologia".
- Area E-commerce: solo l'immagine "SITO IN COSTRUZIONE".
- Certificazioni e numeri: nessuna certificazione propria. Le certificazioni citate sono dei fornitori (ACDCFAN "certificato ISO 9001 e ISO 14001"; Commonwealth "UL, CAS, TUV"; Mean Well "2.800 dipendenti"). Nessun numero dell'azienda (anni, clienti, pezzi, magazzino).

**Tecnologia**: Incomedia WebSite X5 Professional 16.3.1 (meta generator), Open Sans da Google Fonts, banner e badge cookie di iubenda. Meta description "Area Systems Home", og:title "Home Page". Il logo esiste in JPEG (1047x592 il più grande). Il catalogo 2022 è un PDF Scribus di 74 MB, protetto contro la copia del testo.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, pezzi in `p1440/`; anche `azienda-1440.jpg` e `asb-1440.jpg`):
- Il menu non si vede: la testata è una fascia bianca con il solo logo in alto a sinistra. Su desktop non c'è modo di arrivare ad Azienda, Contatti o Download.
- La prima schermata è una fascia grigia con al centro uno slider di 288x253 px di scontornati da catalogo; la stessa fascia si ripete identica in ogni pagina interna.
- L'unico titolo è "I nostri prodotti"; non c'è una frase che dica chi sono.
- Sotto, una griglia di 12 riquadri con foto di misure diverse (alcune con il fondo grigio della foto, altre bianche) e testi centrati in Arial piccolo.
- Pagina Azienda: foto del capannone in controluce con il sole nel lampione, testo tutto centrato con elenchi puntati centrati.
- Schede prodotto: tabelle con bottoni rossi "Click me!" per le schede tecniche.
- Altezza della home: 2402 px.

**Problemi a 390** (`home-390.jpg`, pezzi in `p390/`):
- Logo e pulsante del menu impilati uno sotto l'altro in due riquadri bianchi.
- Sotto lo slider restano circa 300 px di grigio vuoto prima del titolo.
- I 12 riquadri vanno in colonna con molto vuoto tra l'uno e l'altro: la pagina è alta 5946 px.
- Nel piede i due badge iubenda "Privacy Policy" e "Cookie Policy" coprono l'email e la partita IVA.
- Non c'è scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Area Systems srl | piede di ogni pagina: "Area Systems Srl"; aziende.it/area-systems-s-r-l: "AREA SYSTEMS S.R.L. Attiva SOCIETA' A RESPONSABILITA' LIMITATA" |
| P.IVA e C.F. | 04952870287 | piede: "C. F. / P. IVA / VAT:(IT) 04952870287"; catalogo 2022, retro: "P. Iva/C.F. 04952870287" |
| Sede legale | via Brescia 6, 35020 Saonara (PD) | retro del catalogo 2022: "Sede legale: Via Brescia 6 35020 Saonara PD"; aziende.it: "Sede legale: Via Brescia 6, 35020 Saonara (PD)" |
| Sede operativa | via San Marco 10, 30030 Tombelle di Vigonovo (VE) | retro del catalogo: "Sede operativa: Via San Marco 10 30030 Tombelle di Vigonovo VE"; piede del sito: "Via San Marco 10 30030 Vigonovo ( VE ) Italy" |
| Telefono | +39 049 7960705 | piede: "Tel. +39 049 7960705" |
| Email | info@areasystems.it | piede: "email: info@areasystems.it" |
| PEC | area.systems@pec.it | aziende.it: "PEC area.systems@pec.it" (non è sul sito) |
| Anno | 2016 | aziende.it: "ATECO 46.50.2 dal 2016" |
| REA | PD-431335 | aziende.it: "REA PD-431335" |
| Attività registrata | commercio all'ingrosso | aziende.it: "Commercio all'ingrosso di apparecchiature per telecomunicazioni" (codice ATECO 46.50.2, che non descrive bene ciò che vendono) |
| Numeri | 2 dipendenti; ricavi 495.699 euro (2024), 577.233 (2022), 484.608 (2021); capitale 10.000 euro | aziende.it: "€ 495.699 Fatturato 2024", "2 Dipendenti", "€ 10.000 Capitale sociale" |
| Marchi trattati | ACDCFAN, Commonwealth, Jason Fan, ECOFIT, Mean Well, Relpol, Lonyung, MAUS Stixx | schede prodotto e pagine Compliance (`acdcfan`: "Guangzhou Guanxie Fan Manufacturing Co.,Ltd."; `lonyung`: "LONYUNG LED LIGHTING CO.,LTD") |
| Social, certificazioni proprie | non trovati | |

Ricerche web su nome e partita IVA non hanno dato altro; web.archive.org non ha risposto.

## 4. Materiale visivo

Ho scaricato 418 file dal sito (circa 10 MB) in `assets/originali/` e `assets/originali/gallery/`, più 8 immagini estratte dal catalogo PDF 2022 in `assets/originali/catalogo-2022/` (convertite da CMYK, al massimo 2400 px). Inventario con misure, pagine, soggetto e voti (qualità / forza come apertura, da 1 a 10) in `_prova/inventario-immagini.json`; fogli provino in `_prova/fogli/`. Non ci sono video.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Catalogo 2022: resistenza con dissipatore alettato nero (`p53-resistenza.jpg`) | 1 | 1782x1917 | 6 | 5 | la più bella: alette in alluminio estruso, foto vera. Fondo nero da scontornare |
| Catalogo 2022: gruppo di ventilazione con griglia cromata (`p13-gruppo-ventilazione.jpg`) | 1 | 1949x2002 | 6 | 5 | nitida; polvere visibile sul mozzo, da ritoccare |
| Catalogo 2022: torrini e ventilatori scontornati | 5 | da 922 a 2400 px | 4-5 | 2-4 | puliti ma da catalogo, alcuni con granelli di polvere |
| Catalogo 2022: copertina (collage di repertorio in rombi) | 1 | 1694x2400 | 4 | 1 | grafica datata |
| Scontornati di prodotto del sito (ventilatori, condizionatori, resistenze, relè, alimentatori, finecorsa) | 70 | da 300 a 475 px | 3 | 1 | foto o render dei produttori, piccoli; Mean Well e Relpol con marchio in vista |
| Miniature e schede di categoria con testo dentro l'immagine | 314 | 220x400 e minori | 2 | 0 | da non usare |
| Foto di repertorio delle applicazioni (data center, eolico, CNC, fotovoltaico) | 18 | 420x315 | 3 | 1 | stock di origine ignota, minuscole |
| Copertine di cataloghi dei fornitori | 8 | circa 229x320 | 2 | 0 | materiale non loro |
| Capannone di Vigonovo in controluce | 1 | 560x433 | 3 | 1 | unica foto della sede, da telefono |
| Logo | 5 | fino a 1047x592 | 3 | 0 | serve il vettoriale |
| Clip-art "sito in costruzione" | 1 | 659x441 | 1 | 0 | da eliminare |

**Verdetto**: il materiale **non regge** una home di alta gamma. In media vale 2 su 10; le due foto del catalogo (resistenza alettata e gruppo con griglia cromata) arrivano a 6 e potrebbero, ripulite e scontornate, fare da oggetto protagonista di una sezione, non da apertura. Non c'è una foto loro di persone, magazzino, banco di prova o quadro montato. Per la proposta servono i segnaposto della sez. 6. Per il sito vero serve mezza giornata di still life (un ventilatore, un gruppo ASB in RAL 7035, una resistenza alettata, un termostato, su fondo grigio chiaro con luce laterale) più un quadro elettrico vero aperto con i loro componenti montati, da fotografare frontale.

## 5. Due direzioni artistiche

**Le ispirazioni del committente** (Pelletteria Graziella e Studio N19; il file `_metodo/ispirazione-graziella-n19.md` non c'era, ho aperto io le prime schermate in `_prova/ispirazione/`): **le uso pochissimo**. Graziella è un registro da maison di pelletteria (serif ad alto contrasto con le parole in corsivo, nero pieno, foto di moda): per un rivenditore di ventole e resistenze da quadro sarebbe un travestimento, e il corsivo d'accento è anche tra i divieti. Da Studio N19 prendo un solo tratto: il bianco con tanta aria e la grotesk molto grande e sicura. Il resto segue il registro del mestiere, cioè il catalogo tecnico fatto bene (riferimento maxon, sez. 7).

**Direzione A, "Il pezzo" (chiara, un solo oggetto)** [consigliata]
- Idea visiva: prima schermata su grigio chiarissimo, quasi bianco, con UN ventilatore assiale fotografato grande e nitido, di tre quarti, e il titolo grande e sicuro accanto ("Il clima giusto dentro il quadro", da verificare con loro). Attorno al pezzo, sottili, poche legende tecniche vere (diametro, "fino a 50.000 ore a 40°C", "IP54"), come nella home Mario Agnoletto. Poi 4 sezioni: le tre famiglie (aria, freddo, caldo) con un oggetto ciascuna, le applicazioni, i marchi, il contatto. Altezza 5000-5500 px.
- Immagini: still life su fondo grigio caldo chiaro, luce laterale morbida, ombra corta. Segnaposto: Matveev ventola nera su cemento (`CxW8a2ts8GE`, apertura, logo sul mozzo da ritoccare), Pancrate griglia tonda e cuffia, SHOX dissipatore; dal loro catalogo la resistenza alettata e il gruppo con griglia cromata, ripuliti.
- Tipografia: Switzer (Fontshare, licenza ITF Free Font) per titoli e testi, grande e asciutto; IBM Plex Mono (Google Fonts, OFL) piccolo per sigle e misure (ASB25, 250x250 mm, 198 mc/h).
- Colore: carta #F3F3F1, grigio quadro #C9CDCB (vicino al RAL 7035 dei loro gruppi), inchiostro #1B1D1E, un solo accento #A03A2B preso dal rosso del logo, usato solo per le misure attive. Niente arancio-giallo del logo in pagina.
- Gesto: un righello di temperatura da -45 a +70 °C sotto la prima schermata. Trascinando o toccando un punto, si accende la famiglia che lavora in quel campo (resistenze sotto zero, ventilazione fino a +70, condizionamento quando l'aria esterna non basta), con i campi presi dalle schede vere. Cambio netto, nessuna dissolvenza.

**Direzione B, "Il quadro aperto" (chiara, il sistema)**
- Idea visiva: la prima schermata è la foto frontale di un quadro elettrico aperto, chiaro e ordinato, ritagliata grande. Sopra, 5 o 6 numeri sottili indicano dove stanno i loro pezzi (gruppo di ventilazione in basso, torrino in alto, resistenza, termostato, lampada LED, alimentatore). Titolo grande a sinistra, poche parole. Poi 3 sezioni: il percorso dell'aria dal basso all'alto, i cataloghi da scaricare, il contatto.
- Immagini: un quadro vero, fotografato frontale con luce piatta e uniforme, più gli stessi pezzi scontornati in tavole. Segnaposto: Sime quadro aperto (`NAchd3UmxXo`, apertura) e cablaggio (`KDkU44ikiko`), Sun dissipatori in fila; per i pezzi gli scontornati del catalogo 2022.
- Tipografia: Instrument Sans (Google Fonts, OFL) per titoli e testi, JetBrains Mono (Google Fonts, OFL) per i numeri delle legende e le sigle.
- Colore: bianco #FAFAF8, grigio lamiera #D5D8D6, inchiostro #15171A, accento #A03A2B per il numero attivo; il colore pieno arriva solo dai fili del cablaggio nella foto.
- Gesto: toccando un numero nella foto, la legenda a fianco mostra il pezzo scontornato con sigla, misura e una riga di scheda vera (es. "CTSH, da 25 a 150 W, guida DIN 35 mm"); da tastiera i numeri si scorrono con le frecce. Niente zoom, niente cursore che segue.

Una variante scura (dissipatore Padriñán su nero, `3520696`) è possibile per una sola sezione "calore", ma non la consiglio come apertura: il committente vuole il chiaro e il soggetto non lo chiede.

## 6. Immagini sostitutive

Ci sono 9 foto in `assets/esterne/` (7 Unsplash, 2 Pexels), a 2400 px sul lato lungo. Licenza verificata sulla pagina di ogni foto il 19/10/2026 ("Free to use under the Unsplash License", nessuna Unsplash+; Pexels "Free"). Nessuna è già usata in un'altra home della campagna. URL, autori e licenze in `assets/CREDITI.md`.
- A, apertura: Matveev, ventola nera su cemento chiaro (`CxW8a2ts8GE`). Altre per A: Matveev tre ventole bianche (`MenG-vuJr30`), Pancrate griglia tonda (`cI-2N2bV6Lo`) e cuffia di sfiato (`CQkoCt7taPo`), SHOX dissipatore su bianco (Pexels `31665486`).
- B, apertura: Sime, quadro aperto (`NAchd3UmxXo`). Altre per B: Sime cablaggio (`KDkU44ikiko`), Sun dissipatori in fila (`GYDBZrVPRU8`).
- Variante scura: Padriñán dissipatore su nero (Pexels `3520696`).
- Attenzione: le due foto di Matveev hanno il logo ID-COOLING (marchio di ventole) sul mozzo: va ritoccato (la licenza lo permette) o escluso dal taglio. Le ventole dei segnaposto sono da PC, non da quadro: lo deve dire il LEGGIMI.
- Scartata: Makhumisane, ventola su grigio (`KlgHazXg2Ic`), che sembra un render 3D.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 19/10/2026; prime schermate a 1440 e 390 in `riferimenti/` (JPEG qualità 78), font letti dal codice. Nel settore stretto (clima per quadri elettrici) non c'è un sito davvero di alta gamma: i primi tre riferimenti sono di mestieri vicini (azionamenti di precisione, componenti elettrici, ventilazione), gli ultimi due sono il settore stesso, utili soprattutto per vedere cosa evitare.

1. **maxon** (maxongroup.com, motori e azionamenti di precisione, Svizzera).
   - Alta gamma: una sola foto enorme di un oggetto tecnico (la ventola di un motore d'aereo, frontale, nitidissima), titolo bianco "Precision electric drives for aerospace." in Suisse Int'l, un solo filo rosso sotto la testata, menu di tre voci. A 390 l'oggetto resta protagonista.
   - Da non riprendere: il selettore di regione a tutto schermo all'arrivo e il testo bianco sopra la foto.
2. **Gira** (gira.com, interruttori e domotica).
   - Alta gamma: un componente elettrico trattato come oggetto di design, foto scura con un raggio di luce a spettro, Univers Next leggero, poche parole.
   - Da non riprendere: il nero e il carosello con le frecce.
3. **Elica** (elica.com, cappe aspiranti, Fabriano).
   - Alta gamma: un'azienda dell'aria che parla di una finitura ("Nero opaco Raw."), titolo grande in Favorit, due righe, un solo bottone.
   - Da non riprendere: il grigio medio uniforme senza oggetto in vista nella prima schermata.
4. **STEGO** (stego.de, thermal management per quadri: è il mestiere di Area Systems).
   - Utile: dice in una riga per chi lavora ("Optimal thermal management whichever way the wind blows"), il prodotto bianco su fucsia a 390.
   - Da non riprendere: video che non carica, maiuscolo condensato, barra di navigazione fucsia inclinata, molte icone laterali.
5. **Cosmotec** (cosmotec.it, condizionamento per quadri, concorrente italiano).
   - Utile: il prodotto vero (un condizionatore su un armadio aperto) grande nella prima schermata e numeri chiari ("Dal 1989", "70+ paesi", "300+ persone").
   - Da non riprendere: fascia blu-verde con gradiente, fila di riquadri con icona, popup F-GAS sopra il contenuto.

Scartati, con le prime schermate in `riferimenti/scartati/`: Pfannenberg e Rittal (coperti dai banner cookie, impianto datato), ebm-papst (titolo su fondo verde acido e banner), Big Ass Fans (registro americano urlato), Fandis (collage su arcobaleno), Vortice (CSS non caricato a 1440). Noctua blocca i browser automatici; ziehl-abegg.com e jung-group.com non hanno reso la prima schermata.

## 8. Da confermare

- Chi produce le linee con sigla propria (ASB, ASVC, ASVE, ASRC, ASTH, AS-CC, AS-T5) e cosa vuol dire "ideata da Area Systems" per l'ASRC: progettazione propria o marchio su prodotto di terzi?
- Se sono distributori ufficiali (esclusivi?) di ACDCFAN, Commonwealth, Mean Well, Relpol per l'Italia, e se possono mostrarne i marchi.
- Il rapporto con la sede di Saonara (solo legale?) e se a Tombelle c'è un magazzino visitabile e fotografabile.
- Anno: "dal 2016" viene da aziende.it; c'era un'attività precedente dei soci?
- Numeri pubblicabili: clienti, articoli a magazzino, tempi di consegna. Oggi non ce n'è uno.
- L'e-commerce "in costruzione": è in programma?
- Cosa sono le pagine "Compliance" (acdcfan, lonyung): documentazione per i clienti o pagine dimenticate?
- I diritti degli scontornati e delle foto del catalogo 2022 (sembrano dei produttori) e delle 18 foto di repertorio delle applicazioni.
- Il logo vettoriale.
- Il menu che su desktop non compare: è un guasto del tema WebSite X5 o una scelta?
- Il titolo d'apertura proposto ("Il clima giusto dentro il quadro") è mio: va approvato da loro.
