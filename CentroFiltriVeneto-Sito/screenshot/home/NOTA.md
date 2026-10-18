# Home finale di Centro Filtri Veneto

Pagina: `sito/index.html` (statica, si apre con un doppio clic), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rigenera con `_prova/script/build_finale.sh`: rifà immagini e mappa (`prepara_finale.py` per corsia, piramide e banco, `prepara_banco.py` per il logo, `mappa_svg.py`), monta la pagina dal modello `_prova/script/finale.src.html` con la mappa in linea e rifà i quattro screenshot.

Base: il prototipo "banco", scelto dal giudice, con la costa dei cartellini e i marchi per famiglia presi da "ripiano". Giro 1 di correzione: piramide in apertura. Giro 2 di correzione (18/10/2026): in apertura la corsia del magazzino, come proposto dal giudice; la piramide scende nella sezione del magazzino. Vedi "Cosa è cambiato nel giro 2".

## Idea

La home parla come si parla al banco: "Portaci il codice, il mezzo o il filtro vecchio". In apertura c'è il posto dove sta il filtro che cerchi: la corsia del magazzino di Vigonovo, fotografata da CFV, con gli scaffali dei filtri a sinistra, le finestre in fondo e gli scaffali delle scatole a destra. Sui filtri della foto ci sono i cartellini di carta del magazzino, con il codice scritto: =BF593, 33398, 20201, FF155. Sopra quei quattro cartellini veri la pagina mette i suoi, nello stesso formato (carta bianca, solo il codice in nero) e con un filo giallo sotto: ognuno è un link che apre WhatsApp con "Buongiorno, avete il filtro BF593?". La foto è il luogo, la prova che il magazzino esiste, e il primo modo di chiedere.

Il blu pieno dell'insegna parte dalla quarta pennellata del logo e diventa il piano del banco: lì si chiede il filtro nei tre modi in cui lo si chiede davvero, col codice, col mezzo o col pezzo vecchio, in una riga sola di tre sportelli.

Più in basso la piramide dei marchi (una quarantina di filtri di marchi diversi, fotografata da CFV) occupa tutta la larghezza della sezione del magazzino, posata sulla carta con la sua ombra, con quattro cartellini sui filtri. La corsia esce a filo del bordo sinistro in apertura; la foto del banco, in "Dove siamo", esce a filo del bordo destro.

## Prime due schermate

**1440x900**
- Testata: logo, Filtri e marchi, Come si ordina, Dove siamo, 049 9801910 cliccabile.
- Corsia 924x624 a filo del bordo sinistro, con quattro cartellini (BF593, 33398, 20201, FF155) centrati sui cartellini veri della foto. Accanto, in una colonna di 404 px: titolo in condensato 800 a 54 px su tre righe, le famiglie in 400 a 18 px (auto, camion, trattori, movimento terra, oleodinamica, pompe a vuoto e reparti produttivi), i marchi in 600 ("Donaldson, Fleetguard, MANN-FILTER, Baldwin, HIFI Filter, UFI e gli altri marchi: più di 4000 filtri pronti a Vigonovo") e la riga che spiega i cartellini.
- Frontale a pennellate alto 36 px, poi il piano blu con i tre sportelli: "Hai il codice?" (campo e bottone giallo "Chiedi su WhatsApp", sotto l'email), "Hai solo il mezzo?" (049 9801910 e "WhatsApp 320 6125425"), "Hai il filtro vecchio?" (Portalo al banco: Via del Lavoro 30, Tombelle di Vigonovo; Come arrivare). L'ultima riga finisce a circa 890 px.

**Seconda schermata a 1440**
- "Dal trattore alla pompa a vuoto", su bianco: a sinistra il titolo, a destra le cinque famiglie con i prodotti e i marchi.
- Le due porte: "Ricambisti e officine" (portale, account, resi su autorizzazione, EXW) e "Privati".
- La piramide a tutta larghezza (1440x975) con i cartellini PowerCore, SH 51054, 33119 e LF3883; sotto "Più di 15000 codici gestiti" e, a destra, "Dal 1985" e "ISO 9001:2015". Poi "Il banco è a Tombelle di Vigonovo": indirizzo e recapiti, la foto del banco a filo del bordo destro, la strada e la mappa disegnata. In fondo il piede.

**390x844**
- Testata: logo, "Ordini" e "Chiama".
- Titolo su tre righe, famiglie in 400 e marchi in 600 a 15 px, la corsia a tutta larghezza (ritaglio più stretto sugli scaffali, 390x279) con i quattro cartellini, la riga "Tocca un cartellino: apre WhatsApp con il codice", il frontale di 22 px e il piano blu: campo del codice, bottone ed email nella prima schermata.

## Caratteri e colori

- **Pathway Extreme** (SIL Open Font License, asse della larghezza 75-100), una famiglia sola, servita dalla pagina (`sito/fonts/pathway-extreme-latin.woff2`, sottoinsieme latin, 97 KB): nessuna richiesta a Google al caricamento.
  - titoli in condensato 800, testo in 400, codici e telefoni in 600 con cifre tabellari;
  - la scelta viene dai siti del settore letti in 02: titoli in grottesco condensato pesante e testo in grottesco neutro (MANN-FILTER, HIFI FILTER, DT Spare Parts, Kramp);
  - scala: 54/52/44/36/34/30/28/24/20/18/17/15/13 px.
- **Blu #0099E1**, l'ultima pennellata del logo e l'insegna, pieno solo nel piano del banco. In bianco ci sono solo i numeri grandi (24 px in 600 a tutte le larghezze, testo grande per le WCAG: 3,16:1 basta); il testo piccolo è in inchiostro #17191B, contrasto 5,6:1. Al passaggio del mouse i link del piano non diventano bianchi: si ispessisce il sottolineato.
- **Pennellate del logo**: ocra #E9C177, crema #F4E1BC, azzurro #9FCCF4, solo nel frontale.
- **Giallo sole #FEED00**, il tondo "CFV": bottone della richiesta, filo sotto i cartellini (e cartellino intero al passaggio del mouse), punto sulla mappa, contorno del focus nel piede.
- **Fondi**: inchiostro su bianco caldo #FBF8EF; bianco puro solo nella sezione delle famiglie e dei marchi; piede in inchiostro.

## Foto: origine e licenza

Tutte le foto sono di CFV, scaricate dal sito attuale (`assets/originali/`). Nessuna foto di stock e nessuna immagine generata (vedi `assets/CREDITI.md`). Escono tutte da `_prova/script/prepara_finale.py`, che `build_finale.sh` ora richiama a ogni build insieme a `prepara_banco.py` (logo) e `mappa_svg.py`.

- `2017-01-magazzino_centrofiltriveneto.jpg` (corsia, Nikon, 2017, 3813x2471), in apertura. Desktop: ritaglio 3200x2162 dall'angolo in alto a sinistra (scaffali con i filtri e i cartellini, corsia, finestre), contrasto +4 % e un filo di calore; `corsia-940.jpg` e `corsia-1860.jpg` (924 px a 1440, densità 2 coperta). Telefono: ritaglio 2860x2043, `corsia-m780.jpg` e `corsia-m1170.jpg` (390 px a densità 3 coperti).
- `2015-04-home_factory_slider_bg.jpg` (piramide, iPhone, 2016, 4032x3024, già scontornata su bianco puro), nella sezione del magazzino. Il plinto bianco al centro, grigio-lilla (circa 230,230,240), è portato verso #F3EEE2 con una maschera sui pixel chiari e neutri; sotto la fila bassa c'è un'ombra di contatto (fascia scura sotto il punto più basso di ogni colonna, sfocata 14 e 60 px, al massimo 32 %), solo sul fondo; i filtri sono scaldati di circa 150-200 K, il fondo no. Ritaglio 4032x2730, moltiplicato per la carta #FBF8EF: il fondo coincide con la pagina. `pila-780/1170/1440/2400.jpg`.
- `2015-04-IMG_1589.jpg` (banco, iPhone, 2016, neon). Ritaglio 2520x1440 sull'uomo che parla, il ragazzo che scrive e il piano con le carte, filtro mediano 3x3, pannello fucsia desaturato al 90 % (solo le tinte tra 290 e 350 gradi), autocontrasto, luce scaldata di poco; `banco-560/900/1820.jpg`.
- Logo `2015-11-centrofiltriveneto_logo.png`, ridotto a 720 px.
- Mappa disegnata in SVG dai dati OpenStreetMap (ODbL), con l'attribuzione sotto la mappa.

## Cosa è cambiato nel giro 2

Dai due rapporti (giudice e tecnica):
- **Apertura** (giudice, bloccante K1 e K6): la piramide lascia l'apertura, entra la corsia del magazzino, l'alternativa proposta dal giudice con le foto vere. La adotto perché a 1440 e a 390 la pagina migliora in modo evidente (luogo vero, profondità, luce delle finestre, filtri Baldwin e Fleetguard riconoscibili) e l'idea resta: titolo, cartellini che aprono WhatsApp, tre sportelli. Due scostamenti dalla proposta: ritaglio orizzontale e non verticale 4:5 (a tutta altezza avrebbe spinto il piano blu fuori dalla prima schermata, mentre il giudice lo vuole lì), e cartellini sugli scaffali di sinistra, dove ci sono i filtri con i codici leggibili, non su quelli di destra (scatole e codici di posizione interni, come 50303A). I cartellini non hanno più sottotitoli e riportano i codici scritti davvero sui filtri della foto.
- **Piramide**: scende nella sezione del magazzino al posto della corsia (non nella sezione delle famiglie, per non mettere due foto di seguito sotto l'apertura e tenere leggibile l'elenco), a tutta larghezza, con 4 cartellini invece di 8; ombra di contatto, plinto al tono della carta, filtri più caldi. SH 51054 ora sta sul filtro HIFI e non tocca altri cartellini (tecnica).
- **Prima schermata**: tolto "in pronta consegna" (resta "più di 4000 filtri pronti"); famiglie in 400 e marchi in 600 a tutte le larghezze; "UFI" ovunque.
- **Magazzino**: titolo nuovo "Più di 15000 codici gestiti" (non ripete più la riga d'apertura); a destra "Dal 1985" e "ISO 9001:2015" in 600.
- **Famiglie**: "Aria, olio e idraulica, più marche" al posto di "Per più settori"; "GFT Filter, ne siamo distributori" (il giudice proponeva "distributori ufficiali", ma il portale dice solo "Distributori GFT Filters"); "Anche ricambi aftermarket...".
- **Ricambisti, telefono**: "Dal telefono: WhatsApp 320 6125425 o 049 9801910" (non più resi@).
- **Banco**: pannello fucsia spento; da 641 a 1180 px la foto è larga quanto mappa e testi (via il max-width 880).
- **Oltre i 1440 px**: corsia e banco allineati alla griglia (logo e testi), non più a metà tra griglia e bordo.
- **Mappa**: il tracciato nero finisce sul punto di CFV (rotonda, Via Statuto dei Lavoratori, Via del Lavoro verso sud); niente più anello, ramo a nord e uncino. Il riquadro sale di 30 unità e la rotonda di partenza è intera. Sotto i 375 px "Via Vigonovese" sale e non copre più la strada.
- **Piede**: colonna "Ordini e uffici", indirizzi email su una riga propria (senza spezzarli sopra i 640 px), Facebook nella prima colonna, via "Seguici".
- **Tecnica**: numeri del piano a 24 px anche sul telefono; link WhatsApp con lo spazio vero ("WhatsApp 320 6125425"); sorgenti 1170 px per il telefono; `sizes` misurati (924 px a 1440, 860 oltre); description di 151 caratteri con luogo e telefono all'inizio; spaziature: magazzino 64 px sotto, porte 64 px sopra anche sul telefono; filo giallo fisso sotto i cartellini e riga "Tocca un cartellino" sul telefono.

## Cosa è cambiato nel giro 1

Dai quattro rapporti (giudice, tecnica, dati, compratore):
- **Apertura** (giudice, bloccante): la foto del banco del 2016 lascia l'apertura. Al suo posto la piramide dei filtri con i cartellini cliccabili; titolo accanto alla piramide; i tre sportelli in una riga sul blu. La foto del banco scende in "Dove siamo" (non nello sportello: con gli sportelli in una riga non c'è posto per una foto, e "Come arrivare" porta lì).
- **Doppioni** (giudice): tolti i sei ritagli della piramide nei ripiani gialli (fondi sporchi, gli stessi filtri dell'apertura) e la piramide nella sezione dei marchi. La costa dei cartellini continua nei cartellini sulla piramide.
- **Etichette sopra i titoli** (giudice): "Su strada e in campo" e "Negli impianti e nei reparti" non ci sono più; mezzi e prodotti stanno nelle righe delle famiglie, accanto al nome della famiglia.
- **Sezioni**: "Dal trattore alla pompa a vuoto" e "I marchi, per famiglia" sono una sezione sola (stesse cinque famiglie, ora con mezzi e prodotti). Serve anche alla soglia delle foto: senza i ripiani e la piramide doppia l'area foto era scesa al 28,5 %.
- **Testata**: il logo non si stringe più (flex:none, 264 px fino a 1180, 220 px sotto); da 641 a 1100 px il menu va su una seconda riga invece di sparire; sul telefono c'è "Ordini" accanto a "Chiama"; sotto i 375 px logo a 128 px. Voce "Come si ordina" al posto di "Ricambisti e privati".
- **Telefono**: niente più scorrimento orizzontale a 320 e 360 (la riga dei ritagli non c'è più, testata ristretta); i cartellini non si toccano a nessuna larghezza; l'etichetta CFV della mappa non copre più l'attribuzione (posizioni in CSS, attribuzione sotto la mappa).
- **Accessibilità e tecnica**: focus giallo nel piede; tolti i link vuoti Privacy e Cookie; carattere servito dalla pagina; campo del codice con `pattern` e controllo nello script (un campo di soli spazi non apre più WhatsApp), `autocapitalize="characters"` ed `enterkeyhint="send"`; `loading="lazy"` sulle foto sotto la prima schermata; `sizes` corretti; `<wbr>` nell'email lunga del piede.
- **Dati** (rapporto dati): resi scritti come nel PDF (su autorizzazione, email solo senza account, esclusioni); EXW con ritiro o spedizione a carico del cliente; tolti Starline e Coopers Fiamm (pagine 404, non confermati), "Cummins" accanto a Fleetguard, Vipiemme (sostituito da FAAM, il marchio della pagina marchi di oggi), "filtri a tasche" (nessuna fonte); privati con un testo neutro, senza "passa al banco"; "a circa 10 km dal centro di Padova" al posto dei 10 minuti; in apertura i marchi partono da Donaldson.
- **Compratore**: "più di 4000 filtri in pronta consegna" accanto al titolo; "Tombelle di Vigonovo" nello sportello; numero WhatsApp con l'etichetta sulla stessa riga; link per la targhetta della pompa a vuoto; nota "il portale si usa da computer" solo sul telefono.

## Controlli fatti (giro 2)

- Screenshot guardati tutti a pezzi: 1440 e 390 (build), 320, 768, 1024 e 1920 (`_prova/verifica/correttore-2/shot/`, `p1440/`, `p390/`).
- Scorrimento orizzontale: nessuno (`scrollWidth == innerWidth`) a 320, 360, 375, 390, 414, 600, 641, 768, 900, 901, 1024, 1100, 1180, 1181, 1220, 1260, 1261, 1280, 1360, 1440, 1680, 1920 e 2560, col telefono emulato sotto i 641 px (`_prova/verifica/correttore-2/js/misura.mjs`, `misura.txt`).
- Sovrapposizioni: 0. Tra due cartellini qualsiasi (corsia e piramide) ci sono sempre almeno 8 px a tutte le larghezze sopra; nessun cartellino esce dalla foto; le etichette della mappa non si coprono e non coprono l'attribuzione (a 641 l'etichetta di CFV la toccava: salita al 83 %); i titoli dei tre sportelli stanno su una riga.
- Prima schermata: a 1440 il piano blu finisce a 921 px con l'ultima riga a circa 890; a 390 campo, bottone ed email stanno nei 844 px.
- `segnali.sh` esce con 0 e nessuna soglia bloccante: area foto 35,1 % (corsia 924x624, piramide 1440x975, banco 907x518), Pathway Extreme 100 %, 3 misure di H2, 0 etichette sopra i titoli, 0 frecce, 4 fasce di fondo. Da guardare: "titolo a sinistra e paragrafo a destra" in 3 sezioni (famiglie, porte, magazzino): tre impaginazioni diverse.
- Nessuna richiesta verso altri domini al caricamento. Nessun U+2014 nella pagina, nel modello, in questa nota e nel LEGGIMI. Nessun segnaposto a vista.

## Controlli del giro 1

- Screenshot guardati tutti a pezzi: 1440 e 390 (build), 320, 768, 1024 e 1920 (`_prova/verifica/correttore/shot/`).
- Scorrimento orizzontale: nessuno (`scrollWidth == innerWidth`) a 320, 360, 375, 390, 414, 600, 641, 768, 900, 901, 1024, 1100, 1180, 1181, 1220, 1260, 1280, 1360, 1440 e 1920, col telefono emulato sotto i 641 px (`_prova/verifica/correttore/js/sez.mjs`, `largo.mjs`).
- Sovrapposizioni: 0 tra cartellini, etichette della mappa e attribuzione a tutte le larghezze sopra; nessun cartellino esce dalla foto; i titoli dei tre sportelli stanno su una riga da 641 a 1440 (`js/modi.mjs`); logo a 264 px da 1181, 220 px da 641 a 1180, 160 px sul telefono, 128 px sotto i 375.
- `segnali.sh` esce con 0 e nessuna soglia bloccante:
  - area foto 35,7 %, Pathway Extreme 100 %, 3 misure di H2, 0 etichette sopra i titoli, 0 frecce, 4 fasce di fondo;
  - da guardare: "titolo a sinistra e paragrafo a destra" in 3 sezioni. Sono la sezione delle famiglie (titolo a sinistra, righe a destra), le due porte affiancate e il testo sotto la corsia: tre impaginazioni diverse, ognuna con una foto o un elenco accanto, non lo stesso schema ripetuto.
- Nessuna richiesta verso altri domini al caricamento (niente Google Fonts).
- Nessun U+2014 nella pagina, nel modello, in questa nota e nel LEGGIMI. Nessun segnaposto a vista.
