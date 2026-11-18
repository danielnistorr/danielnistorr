# Griste: analisi per la nuova home

Sito: http://www.griste.com/ (crawl e screenshot del 20/10/2026: home, 5 pagine di profilo e contatti, 4 categorie, 99 schede prodotto, versione inglese, cartelle con indice aperto `img/`, `video/`, `pdf/`, `file/prodotti/`). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `griste.com/`.

## 1. In breve

- **Chi**: Griste S.r.l., via Irpinia 55, Villatora di Saonara (PD), zona artigianale. "La ditta Griste nasce nel 1975" (`chi-siamo.php`). "Oggi la società è gestita dai figli di Guido", cioè Alberto e Letizia Burattin (`chi-siamo.php`, home).
- **Cosa fa davvero**: progetta e produce gioielli per scarpe, cioè applicazioni, bottoni, placche, fibbie, puntali e talloni in metallo con smalto, strass, pietre e perle. Lo dice il certificato ISO: "Progettazione e produzione di gioielli e accessori per calzature mediante microlavorazioni metalliche e trattamenti galvanici". La pelletteria c'è ma è secondaria ("i primi accessori per scarpe e pelletterie", `chi-siamo.php`). Il processo: disegno, CAD e CAM, prototipo, produzione interna più "un gruppo di aziende selezionate che operano in esclusiva per Griste" (`gioielli.php`).
- **Per chi**: stilisti e marchi della calzatura di lusso. Nessun cliente è nominato. Va a Première Vision Paris (banner 2018, 2019, 2020) e a Lineapelle (febbraio 2026, con il Gruppo Altofare).
- **Quanti**: 23 dipendenti, ricavi 7,6 milioni di euro nel 2024, in calo del 24,9% (Atoka). Sul sito ci sono 99 pezzi in 4 collezioni.
- **Correzioni alla nota di partenza**:
  - Dal 2023 circa Griste non è più solo un'azienda di famiglia: fa parte di **Altofare**, il gruppo italiano di accessori per il lusso sostenuto da White Bridge Investments. Alberto Burattin ne è "Managing Director Accessori Calzature".
  - Il sito non è fermo del tutto. La copertina della home è un video caricato il 02/02/2026 e il certificato ISO è stato aggiornato nel 2025. Il resto invece è del 2015-2017 ("© 2015", "SPRING SUMMER 2017" nel codice).
  - È più calzatura che pelletteria.
- **Il punto**: Griste fa gioielli, non minuteria. Smalto colato a mano su fiori e insetti, strass e cristalli, un campionario "in astucci di velluto" che gli stilisti consultano "come un'opera conservata in un museo". Sono oggetti piccoli e colorati, da trattare come gioielleria.

## 2. Il sito di oggi

**Pagine (IT ed EN)**:
- Home.
- Profilo: Chi siamo, L'impegno ambientale, Sostenibilità (`certificazioni.php`), Gioielli.
- Prodotti: Natura (31 pezzi), Moda (21), Macchina creativa (26), Natura umana (21). Ogni categoria è una griglia di scontornati con il nome del pezzo e la lavorazione.
- Contatti, privacy, cookie policy.
- Nel server ci sono altre 49 cartelle prodotto non più pubblicate.

**Testi veri essenziali (verbatim)**:
- Home: "DAL 1975 LA MAISON DEL GIOIELLO PER CALZATURE E ACCESSORI" (EN: "SPECIALISING IN FOOTWEAR AND ACCESSORIES SINCE 1975").
- Home: "Prendete un pizzico di storia, un tocco d'arte, creatività a piene mani. Aggiungete bagliori metallici e tutti i colori dell'iride, mescolate con cura (artigianale, of course) e… voilà, ecco nascere i gioielli Griste."
- Home: "la storica azienda veneta tiene alto nel mondo il nome della qualità made in Italy."
- Chi siamo: "Sfruttando l'esperienza nelle microlavorazioni metalliche e nei trattamenti galvanici, negli anni Ottanta Griste si rivolge al settore della calzatura".
- Chi siamo: "Grazie alla collaborazione con affermati stilisti locali [...] diventa in breve tempo punto di riferimento del settore."
- Chi siamo: "accompagnandoli in una ricerca dell'elemento perfetto che renda uniche le loro creazioni."
- Gioielli: "Ogni accessorio Griste è unico e originale: inizia a prendere forma nella mente di chi lo crea a partire dalle suggestioni più diverse, un gioiello famoso, una sfilata di moda, un romanzo, un libro di architettura, per poi spostarsi sulla carta e in seguito essere elaborato a computer in CAD e CAM." (Le lineette dell'originale sono rese con le virgole.)
- Gioielli: "Dal disegno tecnico si passa alla produzione di un prototipo, che va ad arricchire il campionario interno."
- Gioielli: "Griste realizza sogni. Quelli che i clienti conoscono e quelli che ancora non sanno di avere."
- Gioielli: "IL CAMPIONARIO, OVVERO IL TESORO DI GRISTE". Poi: "Griste conserva in astucci di velluto non solo la storia dell'azienda, ma quella dell'intero mondo dell'accessorio per calzature."
- Gioielli, materie: "solo materie prime di alta qualità, pietre dure, cristalli, smalti, ottone."
- Gioielli, lavorazioni: "Fusione zama, fusione ottone, stampaggio a freddo, lavorazioni a pantografo, saldatura, marcatura, smaltatura, pulimentatura e bagni galvanici anallergici".
- Impegno ambientale: "Dal 2008 è operativo sulle coperture dei capannoni un impianto che produce 49 kw ora di energia pulita".
- Certificazioni: "UNI EN ISO 14001:2015" (Certiquality), "Codice etico" (aggiornamento 28/02/2022), "Codice etico di gruppo", "Modello di Organizzazione, Gestione e Controllo", "Procedura whistleblowing". Gli ultimi tre documenti stanno su altofare.com.

**Numeri contati sulle 99 schede** (script `_prova/script/`, pagine `_prova/crawl/pages/prodotti.php_idCat_*.html`):
- Per lavorazione:
  - 58 pezzi con strass;
  - 30 con smalto;
  - 18 con pietre;
  - 3 con perle;
  - 19 "su metallo" senza altro.
- Per tipo:
  - 33 applicazioni;
  - 20 bottoni;
  - 12 placche;
  - 11 fibbie;
  - 3 puntali e 2 talloni;
  - e poi fiori, farfalle, libellule, un bruco, una rana, un'ape, un gufo, una fragola e un pappagallo.

**Tecnologia**:
- Sito PHP fatto a mano da creative-lab.it ("adv: creative-lab.it"), su Apache. Usa Bootstrap 3.3.2 (2015), jQuery 1.11.1, gli slider jssor e slick e Fancybox.
- Carattere: Roboto da Google Fonts; i titoli sono in Times New Roman corsivo maiuscolo.
- Cookiebot e Google Analytics 4. Mappa Google incorporata nei Contatti.
- **HTTPS non funziona**: il certificato non è valido e il sito gira solo in http.
- `<title>` è "Home" su ogni pagina e la meta description è vuota.
- Le cartelle `img/`, `video/`, `pdf/` e `file/` hanno l'indice aperto: chiunque vede tutti i file caricati, compresi i video natalizi e i banner delle fiere.
- I link della versione inglese sono relativi e si annidano all'infinito (`en/en/en/...`).
- Il link "Modello di Organizzazione" punta alla pagina whistleblowing.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `gioielli-1440.jpg`, `natura-1440.jpg`):
- Il banner Cookiebot copre il terzo inferiore della pagina.
- Il logo blu è piccolo (152x42) e centrato sopra un menu maiuscolo a tendina.
- La prima schermata è un video 1000x700 stirato a 1168 px. È un collage: la cupola di una serra con fiori in smalto incollati sopra, con i controlli del lettore in vista. È morbido e da cartolina, e non fa capire che cosa vende Griste.
- Sotto c'è un carosello di 5 pezzi dentro un riquadro, con didascalie generiche ("APPLICAZIONE", "FIBBIA").
- Poi una foto di repertorio (mano che firma su un tablet) accanto al testo sulla certificazione, che è il titolo più visibile dopo il video.
- Il claim "DAL 1975 LA MAISON DEL GIOIELLO" arriva solo in fondo, a 1560 px.
- Il testo è grigio chiaro su bianco, centrato o allineato a destra e lungo.
- Nella pagina Gioielli le foto vere del laboratorio sono a 365x230.

**Problemi a 390** (`_prova/attuale/home-390.jpg`, `chi-390.jpg`):
- Il banner dei cookie copre tutto lo schermo.
- Chiuso il banner, la home è alta 1122 px: video piccolo, testo della certificazione, claim e piede. Il carosello dei prodotti sparisce.
- Niente scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Griste S.r.l. | `contatti.php`: "Griste Srl"; certificato ISO: "GRISTE S.R.L." |
| P.IVA e C.F. | 00465750289 | `contatti.php`: "P.IVA e C.F. 00465750289" |
| Registro imprese, REA | PD 00465750289, REA PD 126289 | `contatti.php`: "REG. IMP. PD N.00465750289", "REA – PD 126289" |
| Capitale sociale | € 20.800,00 | `contatti.php`: "CAP.SOC. € 20.800,00". Atoka scrive "21.0 K €" (sez. 9) |
| Indirizzo | via Irpinia, 55, 35020 Villatora di Saonara (PD) | `contatti.php`: "via Irpinia, 55 - 35020 Villatora di Saonara (ZONA ARTIGIANALE) - PADOVA - ITALIA". Il piede dice "55/55", privacy e Atoka "55/57", il certificato "35029" (sez. 9) |
| Telefono | 049 8790716 | `contatti.php`: "tel. 049 8790716" |
| Fax | 049 8791367 | `contatti.php`: "fax 049 8791367" |
| Email | info@griste.com; amministrazione@griste.com | `contatti.php`: "info@griste.com", "richieste amministrative: amministrazione@griste.com" |
| PEC | gristesrl@legalmail.it | piede di ogni pagina: "PEC gristesrl@legalmail.it" |
| Mappa | Google Maps, scheda "Griste S.r.l.", 45.38008, 11.96602 | iframe in `contatti.php` (`!2sGriste+S.r.l.`) |
| Orari | non pubblicati | |
| Anno | 1975 | `chi-siamo.php`: "La ditta Griste nasce nel 1975" |
| Attività | ATECO 25.99.90 | atoka.io/public/it/azienda/griste-srl/d73dcfd84073: "Fabbricazione di altri prodotti vari in metallo n.c.a." |
| Dipendenti, ricavi | 23; 7,6 milioni di euro nel 2024, -24,9% | Atoka (stessa pagina): "DIPENDENTI 23", "RICAVI 7.6 M €", "TREND RICAVI -24.9%" |
| Certificazione | ISO 14001:2015 n. 51540, Certiquality; prima emissione 22/03/2022, scadenza 20/03/2028 | `pdf/cert-sistema-gestione-ambientale.pdf` |
| Energia | fotovoltaico da 49 kW dal 2008 | `impegno-ambientale.php` (frase in sez. 2) |
| Gruppo | Altofare (White Bridge Investments) | altofare.com/accessori-calzature/: "Griste / Maison del gioiello per calzature e accessori."; altofare.com/chi-siamo/: "Alberto Burattin / Managing Director Accessori Calzature" e "Il progetto è sostenuto da White Bridge Investments". Ingresso nel gruppo: financecommunity.it, "Griste entra nel progetto per i brand del lusso di White Bridge Investments" (la pagina risponde 403, letto solo l'estratto di ricerca) |
| Fiere | Première Vision Paris 2018, 2019 (febbraio e settembre) e 2020; Lineapelle 11-13 febbraio 2026, "PAD 7, STAND A01/A09/B02/B10" con il Gruppo Altofare | banner in `img/` (`premiere-vision-2018.jpg`, `banner-fiera-*.jpg`, `banner-fiera-febbraio2026.jpg`) |

## 4. Materiale visivo

Ho scaricato 186 file (circa 35 MB) in `assets/originali/`. L'inventario con misure, soggetto, collezione e voti (qualità e forza come apertura, da 1 a 10) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Scontornati dei pezzi, PNG con trasparenza vera e luce da studio coerente | 103 file (99 pezzi) | tutti 450x450 | 7 (i migliori 8) | 4 (i migliori 5-6) | **il tesoro del sito**: puliti, nitidi e coloratissimi. I migliori sono i fiori in smalto (`165 zoom_17`, `157 zoom_09`, `163 zoom_15`, `164 zoom_16`) e i cristalli (`181 bottone-01`, `183 applicazione-10`). Il limite è la misura: a 2x reggono 225 px, a 1x circa 450. Non si possono ingrandire a tutta pagina |
| Foto del laboratorio: cesello, saldatura, bagno galvanico, fresatura, CAD, taglio ad acqua | 6 (+6 miniature) | 640x427 | 5-6 | 2-4 | vere e ben illuminate, con profondità di campo corta. Piccole: vanno bene solo come foto da 400-600 px. Il cesello del fiore (`f03`) è la più bella |
| Mani al lavoro: pinzetta sul fiore in smalto verde, campionario a scomparti, incastonatura | 5 | 364x227 / 365x230 | 6 | 2 | ottimi soggetti, risoluzione inservibile |
| Collage illustrati dello slider e delle categorie (serra, pappagalli, signore anni Venti, mani di foglie) | 14 | 1000x600, 1200x330, 1503x1050 | 4-5 | 2-3 | gioielli veri incollati su illustrazioni: hanno identità ma l'aspetto è da campagna stagionale, e i diritti delle illustrazioni sono da chiarire |
| Fotogrammi dei video (spilla di strass su velluto nero, bracciale su un libro, serra 2026) | 6 | 1165-1500 px | 3-6 | 1-4 | la spilla su velluto (`video__img_natale2.jpg`, 6/4) è l'unica foto grande di un pezzo vero, ma è natalizia, con i fiocchi di neve. Gli altri fotogrammi hanno la barra del lettore impressa |
| Capannone con l'insegna Griste, fotovoltaico | 2 | 365x230 | 4-5 | 0-1 | |
| Repertorio (mano che firma, mondo dipinto) e banner di fiera | 10 | piccoli | 2 | 0 | da non usare |
| Video | 1 in home, più 27 nella cartella `video/` | 1000x700, 11 s | | | li ho guardati a fotogrammi e non li ho tenuti sul disco: sono collage animati (serra, Natale, origami) |

**Verdetto**: il materiale **regge in parte** una home di alta gamma. In media vale 5 su 10, ma per il prodotto vale 7: i 99 scontornati sono quelli di un vero fornitore del lusso e bastano per una prima schermata con UN pezzo nitido a 400-450 px su fondo chiaro, purché si accetti che l'oggetto non sia gigante. Non ci sono foto grandi del laboratorio, delle persone, del campionario di velluto né di un gioiello montato su una scarpa. Per la proposta servono i segnaposto della sez. 6. Per il sito vero bisogna chiedere i file originali dello studio fotografico (gli scontornati sono evidentemente ricavati da scatti più grandi) e fare una giornata di foto: macro di 6-8 pezzi a 3000 px, il campionario aperto, le mani al banco di smaltatura, un pezzo montato su una scarpa.

## 5. Due direzioni artistiche

Il registro giusto è quello della gioielleria, non della minuteria. Rispetto a Hambro (fondo crema caldo, fibbia d'oro, grottesco nero, accento cuoio) Griste cambia idea, apertura e tavolozza: il fondo è freddo, c'è un pezzo colorato in smalto, una serif ad alto contrasto, il blu del loro logo e il verde dello smalto.

**Ispirazioni Graziella e N19**: le uso a metà, perché il soggetto è moda e gioiello per marchi del lusso. Riprendo il titolo-manifesto senza corsivo, l'etichetta piccola a sinistra con il testo nella metà destra e l'elenco a righe con filetto per le lavorazioni. Non riprendo il nero ovunque (i pezzi sono colorati e chiedono luce), l'elenco dei clienti (nessun nome è pubblico), le comparse allo scorrere né il menu nascosto.

**Direzione A, "Un fiore alla volta" (chiara, un solo pezzo protagonista)**
- Idea visiva: fondo porcellana fredda e tanta aria. Al centro destro c'è UN pezzo vero a 440 px, il fiore in smalto bianco e verde (`zoom_17`), con un'ombra corta disegnata sotto e una legenda a filetti: "Fiore. Lavorazione su metallo con smalto. Collezione Natura". A sinistra il titolo grande "La maison del gioiello per calzature", poi "Dal 1975 a Villatora di Saonara". Sotto vengono quattro sezioni: le quattro collezioni, la lavorazione (dal disegno al prototipo), il campionario, la chiusura.
- Immagini: solo gli scontornati veri, mai più grandi della loro misura. Segnaposto per laboratorio e scarpa: GN Group al banco, Gogh che salda, McFollis con le punte di strass, Kier in Sight con i cristalli.
- Tipografia: Bodoni Moda (Google Fonts, OFL) da 96-120 px in peso 400 per i titoli, Instrument Sans (Google Fonts, OFL) per testi ed etichette. Nessuno dei due è già usato nella campagna.
- Colore: porcellana #F4F3EE, inchiostro #15181D (16:1), grigio #5E6470 per le legende (5,3:1), blu Griste #014778 del logo per link, bottone e logo (8,7:1), verde smalto #1F7A5C solo per i numeri piccoli (4,7:1).
- Gesto: quattro nomi di collezione sotto il pezzo (Natura, Moda, Macchina creativa, Natura umana). Al clic o al tocco il pezzo e la sua legenda cambiano subito, senza dissolvenza; i tasti freccia passano da una collezione all'altra.

**Direzione B, "L'astuccio di velluto" (scura ma pulita, il campionario)**
- Idea visiva: la frase "Il campionario, ovvero il tesoro di Griste" come chiave. Il fondo è blu notte vellutato, il colore dei loro astucci immaginato dal logo, non nero pieno. Al centro un solo pezzo di cristalli (`181 bottone-01`, fucsia con corona di strass) che brilla come in vetrina, con un numero d'archivio accanto. Sotto, un cassetto: la griglia regolare dei 99 pezzi, ognuno nel suo scomparto.
- Immagini: scontornati su fondo blu, più i segnaposto scuri hoylee song (fiori di cristalli), Safaei (foglia con perla) e O'neill (fiori in smalto su specchio). Da rifare dal vero: il campionario aperto e fotografato dall'alto.
- Tipografia: Zodiak (Fontshare, ITF Free Font License) da 88 px per i titoli, Satoshi (Fontshare, ITF) per il testo, numeri tabellari per il "n. 01/99".
- Colore: velluto #14203A, testo #F2EEE6 (14:1), secondario #A9B6CF (7,9:1), ottone #C9A45C per numeri e filetti (6,9:1). Il colore pieno lo portano solo i pezzi.
- Gesto: filtri per lavorazione sopra il cassetto, con i conteggi veri (Strass 58, Smalto 30, Pietre 18, Perle 3, Metallo 19). Al tocco si spengono gli scomparti che non c'entrano, senza ricaricare la pagina; toccando uno scomparto se ne legge il nome e la lavorazione.

## 6. Immagini sostitutive

Otto foto Unsplash sono in `assets/esterne/`, con lato lungo fino a 2400 px. Su ogni pagina ho verificato la licenza ("Free to use under the Unsplash License", nessuna Unsplash+) e nessuna è già usata in un'altra home della campagna. URL, autori e licenza sono in `assets/CREDITI.md`. Sono segnaposto, non sono generate dall'IA e non mostrano marchi.
- Chiare, per A: COPPERTIST WU (paguro in ottone su bianco), Kier in Sight (cristalli sfaccettati su azzurro), McFollis (punte di sandalo con strass, ritagliata da me per togliere il marchio sul sottopiede).
- Scure, per B: hoylee song (fiori di cristalli rossi su nero), parisa safaei (foglia di strass con perla su raso nero), César O'neill (fiori in smalto rosa su specchio).
- Laboratorio, per entrambe: GN Group (ragazza al banco orafo) e Mario Gogh (saldatura a cannello).
- Ho scartato le décolleté dorate con fiocco gioiello di McFollis, che erano perfette, perché si legge il marchio sul sottopiede.
- Mancano e vanno fatte dal vero: un gioiello Griste montato su una scarpa, il campionario di velluto, la smaltatura.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 20/10/2026. Le prime schermate a 1440 e 390 sono in `riferimenti/` (JPEG, qualità 78). Caratteri letti dal codice.

1. **Pomellato** (pomellato.com, gioielleria, Milano).
   - Cosa lo rende di alta gamma: un pezzo vero, le catene in oro rosa, grande e nitido su un grigio neutro, con un solo titolo "ICONICA" in FuturaStd. A 390 ci sono solo i tre anelli: l'oggetto basta.
   - Da non riprendere: la modella (Griste non avrà quel materiale) e i due pannelli sovrapposti (paese e cookie).
2. **Buccellati** (buccellati.com, alta gioielleria).
   - Cosa lo rende di alta gamma: il logo serif centrato, il menu maiuscolo spaziato in Novecento Wide e la macro di un orecchino sulla pelle a tutta finestra.
   - Da non riprendere: il testo bianco maiuscolo sopra la foto, il bottone a filetto "DISCOVER MORE", dieci voci di menu.
3. **Aquazzura** (aquazzura.com, scarpe gioiello, Firenze).
   - Cosa lo rende di alta gamma: il fondo chiaro, la scarpa protagonista e la serif Miller leggera per i titoli. È anche il mondo del cliente di Griste: è così che si presenta chi compra un'applicazione gioiello.
   - Da non riprendere: la barra delle spedizioni, il popup della newsletter all'arrivo, la chat.
4. **FOPE** (fope.com, oro, Vicenza).
   - Cosa lo rende di alta gamma: il titolo grande e sottile "THE GOLDEN NOW" in NeuzeitGro 300 da 81 px su grigio caldo, con la foto a metà pagina fino al bordo. È vicino alla ricetta della chiusura "testo a sinistra, foto a destra fino al bordo".
   - Da non riprendere: il riquadro "Confirm location" sopra la prima schermata.
5. **Altofare Group** (altofare.com, il gruppo di cui Griste fa parte).
   - Cosa lo rende di alta gamma: è il tono del gruppo (logo spaziato, Be Vietnam Pro) e la nuova home deve starci accanto senza stonare.
   - Da non riprendere: la prima schermata è un video che nel Chromium di prova resta grigio scuro con un "SCOPRI", e il menu è nascosto dietro un'icona.

Scartati:
- René Caovilla, le scarpe gioiello della Riviera del Brenta: risponde "An unknown error occurred" al browser automatico.
- Le19M e Lesage: "Access Denied".
- Goossens: errore dell'applicazione.
- Preciosa Components: pagina vuota.
- Roger Vivier: pagina vuota.
- Sharra Pagano: il dominio è in vendita.
- Lampa: è un'altra Lampa, di accessori per auto.

## 8. Per il piede

**Logo**:
- La sorgente migliore è il PDF del codice etico (`griste.com/pdf/codice-etico-1.pdf`), che contiene il logo come immagine da 1374x392 px. Il colore è blu notte #014778, diverso dal blu #2F68C1 del JPEG sul sito. L'ho salvato in `assets/originali/logo-griste-codice-etico-1374x392.png`.
- Da questo ho ricostruito il logo in SVG: `logo-griste-tracciato-blu.svg` (#014778), `-nero.svg` e `-chiaro.svg`. Il tracciato coincide con l'originale nel 99,3% dei pixel (IoU 0,993); le differenze sono di 1 px lungo i bordi. È fedele e si può usare in testata e in piede.
- Ci sono anche i PNG a 2x con trasparenza, `logo-griste-blu-2x.png` e `logo-griste-nero-2x.png` (1369x382).
- Altre versioni, più povere:
  - `logo-griste-altofare-1001x500.jpg`, chiaro su grigio, dalla pagina di Altofare;
  - `logo-griste-sito-152x42.jpg`, il logo del sito;
  - `logo-griste-newsletter-248x76.png`, nero.
- La favicon dà 404 e nel codice del sito non c'è un SVG.
- Il vettoriale originale va comunque chiesto all'azienda, insieme al blu ufficiale.

**Menu e pagine di oggi**: Home; Profilo (Chi siamo, L'impegno ambientale, Sostenibilità, Gioielli); Prodotti (Natura, Moda, Macchina creativa, Natura umana); Contatti; Privacy; Cookie policy; versione EN.

**Pagine che il sito nuovo può avere**, da elencare nel LEGGIMI:
- Azienda: Chi siamo, Il campionario, Lavorazioni, Sostenibilità e certificazioni.
- Collezioni: Natura, Moda, Macchina creativa, Natura umana.
- Contatti.
- Documenti: Codice etico, Modello 231 e Whistleblowing, che puntano ad altofare.com.
- Privacy, Cookie, versione EN.

**Social**:
- Il sito non ne linka nessuno e la ricerca non ne ha trovati.
- linkedin.com/company/griste-srl esiste ("griste srl | 9 followers on LinkedIn"), ma è quasi vuota e non so se sia ufficiale.
- I tentativi su Instagram e Facebook rimandano al login, quindi non sono verificabili.
- Esiste il LinkedIn del gruppo, linkedin.com/company/altofare/about.
- Proposta: nessuna colonna "Seguici". Al suo posto, una riga "Parte del Gruppo Altofare" con il link ad altofare.com.

**Newsletter: sì, ha senso.**
- Griste comunica collezioni stagionali ("SPRING SUMMER 2017", `spring21.jpg`, `winter21.jpg`) e fiere (Première Vision, Lineapelle 2026).
- Ha già mandato newsletter: in `video/` ci sono `logo-griste-newsletter.png` e `immagine-nw-auguri.jpg` del dicembre 2020.
- La privacy cita già "l'invio di newsletter".
- Il pubblico sono stilisti e uffici prodotto, non privati.
- Va in piede come "Collezioni e fiere, due volte l'anno": campo email, bottone, casella del consenso. Nel LEGGIMI va scritto che va collegata a un servizio.

**Riga legale**: Griste S.r.l., via Irpinia 55, 35020 Villatora di Saonara (PD), P.IVA e C.F. 00465750289, REA PD 126289, Cap. soc. € 20.800,00 i.v. (solo se confermato "interamente versato"), PEC gristesrl@legalmail.it, Privacy, Cookie.

## 9. Da confermare

- La data di ingresso in Altofare. L'unica fonte datata è l'immagine caricata da Altofare nel 09/2023. Va chiesto anche se in piede serve la dicitura "soggetta a direzione e coordinamento di..." (art. 2497-bis c.c.) e con quale ragione sociale. Il piede di altofare.com riporta "Lampa S.r.l. Società Benefit".
- Il capitale sociale: € 20.800,00 sul sito, "21.0 K €" su Atoka. E se è interamente versato.
- Il civico (55, 55/55 o 55/57) e il CAP (35020 sul sito, 35029 sul certificato ISO).
- I ricavi 2024 e il calo del 24,9% vengono da Atoka (dati aggregati): non vanno in pagina senza il loro consenso.
- I clienti: nessuno è nominato. Si possono citare marchi o almeno "per le maison della calzatura"?
- Chi produce che cosa: in sede o presso le "aziende selezionate che operano in esclusiva".
- Le collezioni attuali: le 99 schede sono del 2020 e il lookbook visibile è "SPRING SUMMER 2017". Esiste una collezione corrente?
- Le foto originali ad alta risoluzione degli scontornati e delle foto di laboratorio; i diritti delle illustrazioni dei collage (chi è l'illustratore).
- Il logo vettoriale e il colore ufficiale del blu: #014778 nel PDF del codice etico, #2F68C1 nel JPEG del sito.
- La pagina LinkedIn "griste srl" (9 follower) e altri social ufficiali.
- Gli orari di apertura e se il fax 049 8791367 è ancora attivo.
- Se la newsletter esiste ancora e con quale servizio.
- Il "libro 2022" (`video/libro-2022.mp4`, `libro2022.jpg`): è un catalogo stampato da citare?
- Le lingue: oggi IT ed EN. Servono altre lingue per le fiere di Parigi?
