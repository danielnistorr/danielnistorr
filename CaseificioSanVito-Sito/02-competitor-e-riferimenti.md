# 02. Concorrenti e riferimenti di design

Ricerca dal vivo del 6 ottobre 2026. Sei concorrenti e trenta siti di riferimento aperti con Playwright (Chromium a 1440 e a 390 px, passando dal proxy); otto riferimenti tenuti, con ritagli dei pezzi da riprendere.

- screenshot interi: `_prova/ricerca/c*-1440.png` e `c*-390.png` (concorrenti), `r*-1440.png` e `r*-390.png` (riferimenti);
- ritagli: `_prova/ricerca/ritagli/` (24 file, nomi parlanti: `gennari-1-meta-foto-e-numeri.jpg`, `paxton-1-le-botteghe-con-indirizzo.jpg`...);
- campione delle tre accoppiate con i testi veri di San Vito: `_prova/ricerca/accoppiate.html`, fotografato in `accoppiate-1440.png` e `accoppiate-390.png`;
- script: `_prova/script/shot.mjs` (screenshot, chiusura banner cookie, siti solo http via curl), `_prova/script/ritagli.py`.

Fonte dei concorrenti: l'elenco degli associati al Consorzio Tutela Formaggio Asiago (asiagocheese.it, PDF `Elenco_Soci_1503.pdf`, "Aggiornato il 15/03/2024"). Nello stesso elenco il caseificio compare come "VI 154 CASEIFICIO SOCIALE SAN VITO", con CAP 36031 (il piè di pagina del sito attuale dice 36030: vedi 01).

## 1. Concorrenti

I concorrenti diretti sono i caseifici sociali e le latterie della provincia di Vicenza soci del Consorzio, che fanno Asiago DOP e hanno uno spaccio. Tutti e sei i siti, a 390 px, non scorrono in orizzontale (scrollWidth 390); il sito di San Vito misura 980.

| # | Concorrente | Dove | Cosa fa meglio di San Vito | Cosa fa peggio | Caratteri e colori |
|---|---|---|---|---|---|
| 1 | [Latterie Vicentine](https://www.latterievicentine.it/) (VI 107) | Bressanvido (VI) | shop online e pagina "Spacci aziendali"; la grotta di stagionatura del Brenta Oro raccontata con data, orari e luogo dell'apertura al pubblico; foto vere delle malghe dei soci ("Da giugno a settembre raccogliamo il latte nelle malghe dei nostri soci"); numero verde in evidenza | blocco evento con bordo sinistro colorato e etichetta sopra il titolo (due divieti di METODO §3); circa 1000 px di bianco dove dovrebbe caricarsi il feed social; a 390 il carosello d'apertura esce con due diapositive tagliate (forse colto a metà scorrimento, comunque è un carosello automatico); frasi generiche sul territorio | Poppins, Lato, Roboto; rosso pieno |
| 2 | [Latteria Sociale di Bolzano Vicentino](https://www.latteriasocialebolzanovicentino.it/) (VI 109) | Bolzano Vicentino (VI) | numeri e modello dichiarati: "46.000 forme all'anno", "Il 90% della produzione della Cooperativa viene venduta a grossisti stagionatori", spaccio interno. È il modello più vicino a San Vito | quattro box con illustrazioni clip-art in fila; a 1440 la fascia d'apertura è rimasta vuota nello screenshot; copyright "©2018"; in home un evento del 7 giugno 2025; loghi dei fondi europei grandi quanto i contenuti | Oswald, Lato; bordeaux scuro, giallo |
| 3 | [Caseificio Pennar Asiago](https://www.caseificiopennar.it/) (VI 102) | Asiago (VI) | apertura con una forma vera e i marchi impressi sullo scalzo; "I nostri punti vendita": quattro spacci con foto della facciata e indirizzo, tra cui "Spaccio Pennar Vicenza, prossima apertura, Str. della Caimpenta" (un concorrente diretto che arriva a Vicenza); visite guidate, filiera, "Prodotto della montagna" | slogan con una parola della lista vietata; spruzzo di latte disegnato; foto ritagliate in cerchio; fascia crema; punti vendita senza orari | Cormorant Garamond, Barlow, Montserrat; verde acido e crema |
| 4 | [Caseificio Sociale San Rocco](https://www.caseificiosanrocco.it/) (VI 140) | Tezze sul Brenta (VI) | numeri di filiera: "oltre 400 quintali di latte conferito", latte da stalle a "massimo 30 chilometri"; foto vere del casaro alla caldaia e del banco dello spaccio; marchio QV spiegato | testi pieni di parole della lista vietata; l'apertura è un video: senza video resta un blocco grigio con testo chiaro poco leggibile; schede molto arrotondate, bordi disegnati a mano | Cheddar Gothic Sans, Biryani; verde scuro, salvia, arancio |
| 5 | [Caseificio Sociale Ponte di Barbarano](https://caseificiobarbarano.it/) (VI 108) | Barbarano Mossano (VI) | apertura con la caldaia di rame e la lira; due accessi grandi "I nostri spacci" e "Le nostre offerte"; "Offerte del mese" in testata; "Spesa pronta": ordine dall'app e ritiro in negozio (San Vito offre la stessa cosa al telefono, ma lo scrive in fondo a una pagina interna); eventi al caseificio | titoli in Poiret One, sottilissimo, che sulle foto si legge male; prodotti fotografati con pomodorini e peperoncini come oggetti di scena; mascotte disegnata; caroselli | Red Hat Text, Poiret One; giallo arancio |
| 6 | [Latteria Sociale Villa](https://www.latteriavilla.it/) (VI 155) | Castelgomberto (VI) | apertura con una forma stagionata che porta impresso "155", il suo codice del Consorzio (nel testo: "Asiago D.O.P. stagionato VI155"); fatti concreti: 6 soci, latte conferito caldo due volte al giorno, 100 ql al giorno, latte crudo; pagina Premi | payoff con una parola della lista vietata; un'immagine rotta; il blocco dei fondi europei occupa una schermata; Zilla Slab con un corsivo calligrafico; colonna di testo lunghissima | Zilla Slab, Open Sans; bordeaux e crema |

Non raggiungibile: Stefani Vittorino S.a.s. (stagionatore, "ST 504" nello stesso elenco del Consorzio, via IV Novembre 35, Dueville): `stefani-formaggi.it` non risponde il 6 ottobre 2026. È a Dueville come San Vito, ma stagiona e non produce.

**Cosa fanno i migliori:** foto vere della lavorazione (caldaia, lira, forme, banco); numeri di filiera al posto degli aggettivi; spacci con la foto della facciata e l'indirizzo; un modo semplice per comprare (shop, spesa pronta, offerte).

**Cosa non fa bene nessuno (lo spazio di San Vito):**
1. gli orari dello spaccio in alto, leggibili da telefono: nessuno dei sei li mette in testata;
2. un archivio vero: la galleria di San Vito ha il "Registro dei Soci", lo "Statuto" e otto foto storiche in bianco e nero (la sede, una benedizione, un taglio del nastro). Nessun concorrente mostra documenti propri;
3. la lavorazione passo per passo con foto proprie: i file della galleria sono già numerati per fase (01 rottura della cagliata, 02 polivalente, 03 salatura, 04 preparazione degli stampi, 06 preparazione per la pressatura, 07 pulizia delle forme e fasciatura, 08 sistemazione delle forme, 09 salatura in salamoia, 10 stagionatura);
4. il colore: i sei usano rosso, bordeaux, verde, verde scuro, giallo arancio, bordeaux. Il blu del logo San Vito e dell'etichetta "Il Fresco di Povolaro" non lo usa nessuno nella zona;
5. un sito senza caroselli automatici, popup e video che non partono.

**Copy evitato** (visto nei concorrenti): le parole della lista vietata (`PAROLE_VIETATE` in `build.py`), frasi su tradizione e territorio che vanno bene per chiunque, contatori di anni che invecchiano ("oltre 100 anni", "125 anni"): si scrive "dal 1899".

**Posizionamento proposto:** "Caseificio sociale di Povolaro dal 1899. Asiago DOP fresco e stagionato, e lo spaccio in via Duse." Contro Latterie Vicentine (grande, shop online) San Vito non compete sull'e-commerce ma sul banco di paese e sull'Asiago Fresco di Povolaro; contro Pennar, che apre uno spaccio a Vicenza, con la data, l'archivio e gli orari chiari.

## 2. Riferimenti premium

San Vito è una cooperativa di paese che fa un formaggio DOP e lo vende anche al proprio banco. I riferimenti giusti sono quindi consorzi e caseifici con siti molto curati, e formaggiai che hanno insieme banco e ingrosso. Niente moda né design d'arredo. Tutti aperti e fotografati il 6 ottobre 2026.

### 2.1 Comté, Comité Interprofessionnel ([comte.com](https://www.comte.com/))
Il formaggio delle fruitières, le latterie di paese del Giura, in gran parte cooperative: nel sito "2 400 exploitations agricoles, 140 fruitières, 14 maisons d'affinage". È il parente più stretto di un caseificio sociale.
- **Gesto da riprendere:** (a) l'apertura mette in primo piano lo scalzo della forma con la fascia-etichetta del marchio ripetuta, e il titolo bianco in maiuscolo stretto sopra la foto (`ritagli/comte-1-apertura-fascia-crosta.jpg`); (b) la filiera in tre numeri grandi bianchi su campo pieno del colore del marchio, con l'etichetta piccola sotto (`comte-3-filiera-in-numeri.jpg`); (c) un blocco "dove comprarlo" con un solo campo (`comte-2-comteradar-punto-vendita.jpg`).
- **Per San Vito:** (a) e (b) con il blu e con i numeri veri del caseificio; (c) diventa il blocco dello spaccio: un solo punto vendita, quindi niente ricerca, ma indirizzo, orari e telefono in un riquadro unico.
- **Da evitare:** menu laterale fisso, timbro circolare con testo che gira ("recette du mois"), riquadri lasciati vuoti finché le immagini lazy non caricano (visti nello screenshot).

### 2.2 Latteria Sorrentina ([latteriasorrentina.it](https://latteriasorrentina.it/))
Latteria napoletana con un marchio blu molto forte.
- **Gesto da riprendere:** il prodotto mostrato nella sua confezione vera, una scheda alta per famiglia, il nome grande in basso (`sorrentina-1-prodotti-nella-loro-carta.jpg`); il blu del marchio usato come campo pieno; le foto d'archivio in bianco e nero con una frase in maiuscolo sopra (`sorrentina-2-foto-archivio-bn.jpg`); una sola dichiarazione maiuscola in apertura (`sorrentina-3-dichiarazione-maiuscola.jpg`).
- **Per San Vito:** l'Asiago Fresco fotografato con la sua carta bianca e blu "Il Fresco di Povolaro", l'Etichetta Oro con la sua carta scura; il blu del logo come campo; le foto storiche della galleria in bianco e nero, alla loro dimensione.
- **Da evitare:** pulsanti a pillola semitrasparenti sulla foto (glassmorphism, vietato), caroselli con frecce, testo bianco su foto chiara senza velatura, il nero pesantissimo usato ovunque.

### 2.3 Caseificio Gennari ([caseificiogennari.it](https://www.caseificiogennari.it/))
Parmigiano Reggiano dal 1953, Collecchio: un solo caseificio, di taglia confrontabile (16.220.564 kg di latte l'anno, circa il doppio dei 250 quintali al giorno dichiarati da San Vito).
- **Gesto da riprendere:** sotto una fascia metà foto e metà testo, una striscia di quattro numeri verificabili: "100 forme al giorno prodotte", "67.000 forme in stagionatura", "1.600 capi di proprietà", "16.220.564 kg di latte lavorati in un anno". Numero grande, etichetta maiuscola piccola sotto (`gennari-1-meta-foto-e-numeri.jpg`; su telefono si impilano bene: `gennari-3-numeri-mobile.jpg`). Foto di lavorazione vere: il casaro che annusa la forma (`gennari-2-casaro-e-forma.jpg`).
- **Per San Vito:** la striscia dei numeri con i dati del sito attuale: 1899 (inizio dell'attività), 90 soci fondatori, 650 litri al giorno all'inizio, 250 quintali di latte al giorno oggi ("Attualmente il Caseificio trasforma giornalmente 250,00 quintali di latte": il testo è fermo al 2011, quindi [DA CONFERMARE] il dato di oggi).
- **Da evitare:** corsivo serif per le frasi d'accento (Cormorant, vietato), fascia rossa con testo corsivo centrato, il motto in inglese, la barra cookie rossa.

### 2.4 Neal's Yard Dairy ([nealsyarddairy.co.uk](https://www.nealsyarddairy.co.uk/))
Londra: selezionano e stagionano formaggi britannici; nel menu "Our Shops" e "Wholesale & Export", cioè banco e ingrosso, il doppio canale di San Vito.
- **Gesto da riprendere:** tutti i formaggi fotografati sullo stesso fondo blu notte, forme intere e pezzi impilati; sotto solo nome e prezzo, piccoli (`nealsyard-1-prodotti-stesso-fondo.jpg`).
- **Per San Vito:** un solo fondo per tutte le foto prodotto (il blu dell'etichetta o un grigio), da scrivere nel brief fotografico del LEGGIMI; nella scheda nome e una riga di dati, niente altro.
- **Da evitare:** popup della newsletter all'apertura, Times e Garamond di sistema, icone sovrapposte alle foto.

### 2.5 Paxton & Whitfield ([paxtonandwhitfield.co.uk](https://paxtonandwhitfield.co.uk/))
Formaggiai inglesi, "EST. 1797" sull'insegna.
- **Gesto da riprendere:** "Visit our shops": la facciata vera di ogni bottega e sotto il nome della via, sottolineato; sopra una sola riga pratica ("Want to avoid the queues? ... try our FREE Click & Collect service") (`paxton-1-le-botteghe-con-indirizzo.jpg`).
- **Per San Vito:** il blocco dello spaccio con la foto della facciata (IMG_5251, 4272 x 2848 px: l'unica foto grande del sito) e la frase del sito attuale "Se vuoi evitare inutili attese, ordina telefonicamente la tua spesa e ritirala in cassa." con il telefono cliccabile.
- **Da evitare:** fondo crema e Baskerville corsivo: è proprio l'accoppiata bocciata come "AI slop". Anche il popup sconto.

### 2.6 Parmigiano Reggiano, Consorzio ([parmigianoreggiano.com](https://www.parmigianoreggiano.com/it))
Il consorzio DOP italiano più curato.
- **Gesto da riprendere:** i mesi di stagionatura come numero grande sul prodotto (bolli "12" e "30" sulle schede, `parmigiano-1-mesi-di-stagionatura.jpg`); la marchiatura della forma come immagine dell'origine (`parmigiano-2-marchiatura.jpg`).
- **Per San Vito:** la stagionatura come dato principale della scheda. Dal Consorzio Tutela Formaggio Asiago (asiagocheese.it): Asiago DOP Fresco "almeno 20 giorni", Mezzano 4-10 mesi, Vecchio 10-15 mesi, Stravecchio oltre 15 mesi; quanto stagionano i prodotti di San Vito è [DA CONFERMARE]. Il marchio DOP sullo scalzo lo imprimono le "fascere marchianti" (testo del Consorzio): si mostra come compare nelle foto delle forme, non si ridisegna.
- **Da evitare:** cornici dorate, titoli in corsivo, troppi caroselli, widget di accessibilità sopra i contenuti; a 390 la home scorre in orizzontale (scrollWidth 396, misurato).

### 2.7 Perenzin Latteria ([perenzin.com](https://perenzin.com/))
"Perenzin Latteria creatori di formaggi dal 1898": una latteria con museo e negozio, la data quasi uguale a quella di San Vito.
- **Gesto da riprendere:** barra nera sottile in cima con le due azioni utili sempre visibili ("Prenota la tua esperienza", "Cheese shop") (`perenzin-1-barra-azioni-e-apertura.jpg`); le persone della latteria fotografate in piedi nel magazzino di stagionatura, tra le forme (`perenzin-2-persone-in-magazzino.jpg`).
- **Per San Vito:** barra in cima con "Spaccio: oggi aperto 8.30-12.30, 16.00-19.00" e "0444 590488"; il ritratto di soci e casari nel magazzino va nel brief fotografico (oggi non c'è).
- **Da evitare:** Playfair con capolettera, fondo di legno scuro, quattro pulsanti in testata.

### 2.8 Luigi Guffanti 1876 ([guffantiformaggi.com](https://www.guffantiformaggi.com/))
"Allevatori di formaggi dal 1876", cantine ad Arona.
- **Gesto da riprendere:** schede con la sezione della forma su bianco e, sotto il nome, il formato in piccolo ("Vezzena 8-10 KG", "Valtellina Casera DOP 7-12 KG") (`guffanti-1-schede-con-formato.jpg`); una sola fascia di colore pieno nella pagina (`guffanti-2-fascia-di-colore.jpg`).
- **Per San Vito:** riga di dati sotto il nome del prodotto (stagionatura, formato); il peso delle forme è [DA CONFERMARE]. Una sola fascia piena di blu per pagina.
- **Da evitare:** ritratto ritagliato in cerchio, carattere decorativo sottile per i titoli, popup all'apertura, foto d'apertura sfocata con un riquadro semitrasparente.

### 2.9 Visti e scartati
Jasper Hill Farm (video che non partono, cerchi, pulsanti verde acqua), Isigny Sainte-Mère (Inter ovunque), Beaufort AOP (buono il "Où nous trouver ?", ma lo copre già Comté), Fromageries Marcel Petite, Mons, Androuet, Quatrehomme, Beillevaire (serif e blu notte da maison francese, lontani da una cooperativa di pianura), Point Reyes e Vermont Creamery (crema, Fraunces e corsivi calligrafici: l'esempio da non seguire), Tillamook e Cabot (cooperative anche loro, ma pubblicità da supermercato americano), Lattebusche e Brimi (cooperative grandi, siti da industria del latte confezionato), Milchhof Sterzing (a 1440 scrollWidth 8020), Beppino Occelli, Fattorie Fiandino, Consorzio Vacche Rosse, La Fromagerie, Montgomery's, Rogue Creamery, Emmentaler AOP (si apre con la scelta del paese). Gruyère AOP risponde 403.

## 3. Cosa si riprende

Il materiale è il vincolo: la galleria del sito ha 60 foto, quasi tutte con il lato lungo di 500 px (le foto dello spaccio sono da 200 x 150); una sola è grande (IMG_5251, la facciata dello spaccio, 4272 x 2848). Le foto da 500 px si mostrano al massimo a 500 px CSS, in mosaico o in striscia, mai a tutta larghezza. Le foto da fare vanno nel brief del LEGGIMI.

| Sezione | Gesto | Da | Materiale di San Vito | Attenzione |
|---|---|---|---|---|
| Barra in cima | orari dello spaccio di oggi e telefono, sempre visibili | Perenzin | orari e telefono dal sito attuale | su telefono una riga sola con l'orario del giorno e il numero; gli orari cambiano (sabato fino alle 18.00, mercoledì pomeriggio e domenica chiuso): o la riga segue il giorno con un piccolo script, o porta a "Orari della settimana" |
| Apertura | campo blu pieno, titolo maiuscolo stretto molto grande, la forma con la sua etichetta accanto alla sua dimensione vera | Comté, Sorrentina | DSC_0023 e DSC_0029 (Fresco con carta blu), DSC_0045 (carta scura, probabilmente l'Etichetta Oro), 500 px | niente foto a tutta larghezza: la foto sta nella metà destra, al massimo 500 px |
| Numeri | quattro numeri grandi in paglia su blu, etichetta piccola | Gennari, Comté | 1899, 90 soci fondatori, 650 litri al giorno, 250 quintali al giorno | il dato di oggi è [DA CONFERMARE]; niente contatori animati |
| Prodotti | una scheda per famiglia, prodotto nella sua carta, stesso fondo, sotto nome e una riga di dati (stagionatura) | Neal's Yard, Sorrentina, Guffanti, Parmigiano | Asiago Fresco di Povolaro DOP, Etichetta Oro, Asiago Stagionato, I prodotti dello spaccio | dati di stagionatura dal Consorzio; quelli di San Vito [DA CONFERMARE] |
| La lavorazione | striscia orizzontale delle fasi numerate, foto da 500 px alla loro misura, nome della fase sotto | Comté ("Plongée au cœur du Comté"), Gennari | le foto 01-10 della galleria, con i nomi delle fasi presi dai nomi dei file | scroll-snap, frecce che si disabilitano agli estremi, `data-scorre` (METODO §4) |
| Lo spaccio | foto grande della facciata, indirizzo sotto, la riga "ordina per telefono e ritira in cassa", orari in tabella | Paxton & Whitfield, Comté (Comtéradar), Pennar | IMG_5251 (4272 px), orari e frase verbatim del sito attuale | l'insegna dice anche "MACELLERIA": cosa sia e di chi è [DA CONFERMARE] |
| Storia e archivio | foto d'archivio in bianco e nero con una riga sopra; documenti veri | Sorrentina | Registro dei Soci, Statuto, otto foto storiche; date: 1899, 1965, 1979, 1987, 2011 | didascalie senza date inventate: quale evento mostrano le foto è [DA CONFERMARE]; niente "ISO 9001:2008" (norma ritirata) |
| Piede | dati societari completi | Pennar (P.IVA in fondo alla pagina) | P.IVA 00180910242, REA VI 1161, Albo Soc. Coop A101490 | PEC [DA CONFERMARE]; i loghi di fondi europei, se dovuti, piccoli in fondo |

Scartato per tutto il sito: caroselli automatici, popup all'apertura, video di sfondo, foto ritagliate in cerchio, spruzzi e illustrazioni clip-art, fondo crema, corsivi, foto virate calde.

## 4. Accoppiate

Tre accoppiate, provate con i testi veri di San Vito in `_prova/ricerca/accoppiate.html` (screenshot `accoppiate-1440.png`). Tutti i caratteri sono su Google Fonts (verificati con l'API css2 il 6 ottobre 2026). Nessun concorrente della zona usa questi caratteri. Contrasti calcolati con la formula WCAG 2.

### A. Fascera (consigliata)
- **Caratteri:** **Sofia Sans Extra Condensed** 800, maiuscolo, per titoli, numeri e nomi dei prodotti; **Sofia Sans** 400, 600 e 700 per testo, menu e pulsanti.
- **Perché:** le lettere alte e strette sono quelle che le fascere marchianti imprimono sullo scalzo di ogni Asiago (si leggono nelle foto 10-stagionatura della galleria); Comté e Sorrentina aprono con un maiuscolo stretto e molto grande, su foto o su campo pieno. Una famiglia sola, due larghezze: il titolo fa il marchio, il testo resta tranquillo.
- **Colori:** blu etichetta `#234A8C` (campi, pulsanti, link: il blu del logo `#3462A8`, scurito per reggere il testo); inchiostro `#15181D` (testo); bianco `#FFFFFF` (fondo); grigio siero `#F1F3F6` (fasce di servizio: spaccio, modulo); paglia `#F6E7A8`, vicino al colore della pasta dell'Asiago fresco campionato dalla foto DSC_0023 (circa `#F8E898`), solo per numeri e titoli su campo blu; grigio `#5B6270` per il testo secondario. Il blu del logo `#3462A8` resta per filetti, voce di menu attiva e numeri grandi.
- **Foto:** prodotti a colori (la carta dell'etichetta e il giallo della pasta sono informazione), lavorazione a colori come sono, archivio in bianco e nero originale. Nessuna virata.
- **Nota tecnica:** negli screenshot a 1x (Chromium su Linux) Sofia Sans sotto i 15 px mostra spaziature irregolari attorno alla "t" ("at tività"); a 2x è pulita (`_prova/ricerca/pezzi/prova-testo.png`). Testo corrente a 17 px, didascalie non sotto 15 px; se nel WordPress di prova il difetto resta, il testo passa a Public Sans e Sofia Sans Extra Condensed resta per i titoli.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro `#15181D` | bianco | 17,79:1 |
| inchiostro `#15181D` | grigio siero `#F1F3F6` | 16,01:1 |
| blu `#234A8C` (titoli, link) | bianco | 8,64:1 |
| bianco (pulsanti, testo su campo) | blu `#234A8C` | 8,64:1 |
| blu `#234A8C` | grigio siero `#F1F3F6` | 7,78:1 |
| paglia `#F6E7A8` (numeri, titoli) | blu `#234A8C` | 6,96:1 |
| grigio `#5B6270` | bianco / grigio siero | 6,13:1 / 5,51:1 |
| blu logo `#3462A8` | bianco | 6,07:1 |

### B. Insegna
- **Caratteri:** **Jost** 500 e 600, maiuscolo spaziato, per i titoli; **Work Sans** 400 e 500 per il testo.
- **Perché:** l'insegna dello spaccio (foto IMG_5251) è rossa con "SPACCIO FORMAGGI" in un bastone geometrico color oro, e nel logo "CASEIFICIO SOCIALE" è scritto in un geometrico sottile; Jost è il geometrico di Google più vicino. Il ritmo a botteghe viene da Paxton & Whitfield, la fascia di un solo colore pieno da Guffanti.
- **Colori:** rosso insegna `#A3201F` (campionato dalla foto e schiarito: va tarato sull'insegna vera), rosso scuro `#8E1C1C`, oro `#E2C27E` solo su rosso scuro, inchiostro `#15181D`, bianco, grigio neutro `#F2F2F0`.

| Testo | Fondo | Contrasto |
|---|---|---|
| bianco | rosso `#A3201F` | 7,54:1 |
| rosso `#A3201F` | bianco / grigio `#F2F2F0` | 7,54:1 / 6,73:1 |
| oro `#E2C27E` (solo testo grande) | rosso scuro `#8E1C1C` | 5,25:1 |
| oro `#E2C27E` | rosso `#A3201F` | 4,40:1 (non basta per il testo normale) |
| inchiostro `#15181D` | grigio `#F2F2F0` | 15,87:1 |

- **Rischi:** il rosso è il colore di Latterie Vicentine; rosso e oro insieme ricordano la pizzeria; l'insegna rappresenta lo spaccio, che è una parte dell'azienda, non tutta.

### C. Registro
- **Caratteri:** **Libre Caslon Text** 400 e 700, solo tondo, per titoli e numeri; **Public Sans** 400 e 600 per testo e interfaccia.
- **Perché:** l'archivio è il materiale più raro di San Vito (Registro dei Soci, Statuto); tra i riferimenti del settore usano un serif tondo Neal's Yard Dairy (Garamond, blu notte su bianco), il Consorzio del Parmigiano Reggiano (Baskerville) e Gennari (numeri serif). Qui senza crema e senza corsivi.
- **Colori:** blu notte `#13233F` (testo e campi), bianco, grigio `#EEF1F4`, azzurro etichetta `#9AB4DD` (accenti su blu notte), blu logo `#3462A8` (link su bianco).

| Testo | Fondo | Contrasto |
|---|---|---|
| blu notte `#13233F` | bianco | 15,67:1 |
| blu notte `#13233F` | grigio `#EEF1F4` | 13,83:1 |
| azzurro `#9AB4DD` | blu notte `#13233F` | 7,42:1 |
| blu logo `#3462A8` (link) | bianco | 6,07:1 |
| blu logo `#3462A8` | blu notte `#13233F` | 2,58:1 (da non usare) |

- **Rischi:** è la strada più vicina al "lusso generato" bocciato su Benvegnù; un serif su un caseificio di pianura si regge solo se l'archivio è davvero al centro, e oggi le foto d'archivio sono da 500 px.

### Valutazione

| Criterio (METODO §2.3) | A. Fascera | B. Insegna | C. Registro |
|---|---|---|---|
| più vivo e più bello del sito attuale | sì: campo blu e titoli grandi | sì | sì, ma più freddo |
| tracciabile ai riferimenti veri | Comté, Sorrentina, Gennari, Neal's Yard | Paxton, Guffanti | Neal's Yard, Parmigiano, Gennari |
| nasce dal materiale dell'azienda | logo, etichetta del Fresco, lettere della fascera | insegna dello spaccio | Registro dei Soci, Statuto |
| distinto dai concorrenti | blu: nessuno lo usa in zona | rosso come Latterie Vicentine | blu notte libero, serif già usati da Pennar e Villa |
| regge foto da 500 px | sì: il titolo fa il lavoro, le foto stanno piccole | sì | in parte: l'archivio vorrebbe foto grandi |
| costruibile in Elementor gratuito | sì (Google Fonts, colori pieni) | sì | sì |
| rischio "AI slop" | basso | medio (rosso e oro) | alto (serif e blu notte) |

**Scelta:** A. Fascera. Da B si prende solo la foto della facciata con l'insegna, così com'è, nel blocco dello spaccio; da C l'idea che l'archivio abbia una sezione sua, in bianco e nero, impaginata con i caratteri di A.
