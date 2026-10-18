# Home finale di Centro Filtri Veneto

Pagina: `sito/index.html` (statica, si apre con un doppio clic), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rigenera con `_prova/script/build_finale.sh`: rifà immagini e mappa (`prepara_finale.py` per corsia, piramide e banco, `prepara_banco.py` per il logo, `mappa_svg.py`), monta la pagina dal modello `_prova/script/finale.src.html` con la mappa in linea e rifà i quattro screenshot.

Base: il prototipo "banco", scelto dal giudice, con la costa dei cartellini e i marchi per famiglia presi da "ripiano". Giro 1 di correzione: piramide in apertura. Giro 2 di correzione (18/10/2026): in apertura la corsia del magazzino, come proposto dal giudice; la piramide scende nella sezione del magazzino. Giro 4, l'ultimo (18/10/2026): la corsia è ritagliata sullo scaffale di sinistra e i cartellini coi codici veri diventano l'immagine, con il campo del codice accanto; vedi "Cosa è cambiato nel giro 4". Giro 5 (18/10/2026): solo ritocchi tecnici, vedi "Cosa è cambiato nel giro 5".

## Idea

La home parla come si parla al banco: "Portaci il codice, il mezzo o il filtro vecchio". In apertura c'è lo scaffale dei filtri del magazzino di Vigonovo, fotografato da CFV, in verticale e grande: i filtri Baldwin e Fleetguard e i cartellini di carta col codice. Accanto a quattro cartellini veri (=BF593, 33398, 20201 e FF155, controllati sull'originale ingrandito) la pagina mette i suoi, 14 px a destra e legati da un filo giallo, così il cartellino scritto sullo scaffale resta in vista, nello stesso formato (carta bianca, codice in nero a 20 px, filo giallo sotto): ognuno apre WhatsApp con "Buongiorno, avete il filtro BF593?". Accanto ai cartellini, subito sotto il titolo, c'è il campo "Hai il codice?" con il bottone giallo. Il gesto è uno: il codice sullo scaffale, il codice nel campo.

Il blu pieno dell'insegna parte dalla quarta pennellata del logo, che comincia dal bordo della foto, e diventa il piano del banco: lì restano gli altri due modi di chiedere, col mezzo o col pezzo vecchio.

Più in basso la piramide dei marchi (una quarantina di filtri di marchi diversi, fotografata da CFV) occupa tutta la larghezza della sezione del magazzino, con quattro cartellini sopra i codici stampati sui filtri (P60-8677, SH 51054, 33119, LF3883). La pagina chiude con il banco: la foto con tutte e tre le persone, a tutta larghezza, in fondo a "Dove siamo".

## Prime due schermate

**1440x900**
- Testata: logo, Filtri e marchi, Come si ordina, Dove siamo, 049 9801910 cliccabile.
- Scaffale 591x752 a filo del bordo sinistro, con BF593 e 33398 in alto, 20201 a metà e FF155 in basso. Accanto, in una colonna di 737 px: titolo in condensato 800 a 78 px su tre righe, "Hai il codice?" con campo e bottone giallo "Chiedi su WhatsApp" (campo a 416-476 px) e l'email; 40 px sotto l'email le famiglie in 400 e i marchi in 600 ("Donaldson, Fleetguard, MANN-FILTER, Baldwin, HIFI Filter, UFI e gli altri marchi: più di 4000 filtri pronti a Vigonovo").
- Frontale a pennellate alto 36 px a 820 px, poi il piano blu con due sportelli: "Hai solo il mezzo?" (049 9801910 e "WhatsApp 320 6125425") e "Hai il filtro vecchio?" (Portalo al banco: Via del Lavoro 30, Tombelle di Vigonovo; Come arrivare). In prima schermata si vede l'inizio del piano.

**Seconda schermata e seguenti a 1440**
- "Dal trattore alla pompa a vuoto", su bianco: titolo sopra, poi le cinque famiglie a tutta larghezza (nome a sinistra, prodotti e marchi a destra).
- Le due porte: "Ricambisti e officine" (portale e una riga breve su account, resi ed EXW con il link al portale) e "Privati".
- La piramide a tutta larghezza (1440x975) con i quattro cartellini; sotto "Più di 15000 codici gestiti" e, a destra, "Dal 1985" e "ISO 9001:2015".
- "Il banco è a Tombelle di Vigonovo": indirizzo, recapiti e strada a sinistra, la mappa disegnata a destra; sotto, a tutta larghezza fino a 1440 px e sulla griglia oltre, la foto del banco con le tre persone (1440x514). In fondo il piede.

**390x844**
- Testata: logo, "Ordini" e "Chiama".
- Titolo su tre righe, "Hai il codice?" con campo (217-269 px) e bottone (fino a 323 px), l'email, famiglie e marchi a 15 px, la riga "Tocca un codice sulla foto: ti rispondiamo su WhatsApp." e lo scaffale a tutta larghezza (ritaglio più basso, 390x364) con BF593, 33398 e 20201. Poi il frontale e il piano blu.

## Caratteri e colori

- **Pathway Extreme** (SIL Open Font License, asse della larghezza 75-100), una famiglia sola, servita dalla pagina (`sito/fonts/pathway-extreme-latin.woff2`, sottoinsieme latin, 97 KB): nessuna richiesta a Google al caricamento.
  - titoli in condensato 800, testo in 400, codici e telefoni in 600 con cifre tabellari;
  - la scelta viene dai siti del settore letti in 02: titoli in grottesco condensato pesante e testo in grottesco neutro (MANN-FILTER, HIFI FILTER, DT Spare Parts, Kramp);
  - scala: 78/52/44/36/34/30/28/24/20/18/17/15/13 px (il titolo d'apertura cresce con la finestra, da 40 a 80 px).
- **Blu #0099E1**, l'ultima pennellata del logo e l'insegna, pieno solo nel piano del banco. In bianco ci sono solo i numeri grandi (24 px in 600 a tutte le larghezze, testo grande per le WCAG: 3,16:1 basta); il testo piccolo è in inchiostro #17191B, contrasto 5,6:1. Al passaggio del mouse i link del piano non diventano bianchi: si ispessisce il sottolineato.
- **Pennellate del logo**: ocra #E9C177, crema #F4E1BC, azzurro #9FCCF4, solo nel frontale.
- **Giallo sole #FEED00**, il tondo "CFV" (anche l'icona della pagina, presa dal sito di oggi): bottone della richiesta, filo sotto i cartellini (e cartellino intero al passaggio del mouse), anello di focus dei cartellini (giallo e inchiostro), punto sulla mappa, contorno del focus nel piede.
- **Fondi**: inchiostro su bianco caldo #FBF8EF; bianco puro solo nella sezione delle famiglie e dei marchi; piede in inchiostro.

## Foto: origine e licenza

Tutte le foto sono di CFV, scaricate dal sito attuale (`assets/originali/`). Nessuna foto di stock e nessuna immagine generata (vedi `assets/CREDITI.md`). Escono tutte da `_prova/script/prepara_finale.py`, che `build_finale.sh` ora richiama a ogni build insieme a `prepara_banco.py` (logo) e `mappa_svg.py`.

- `2017-01-magazzino_centrofiltriveneto.jpg` (corsia, Nikon, 2017, 3813x2471), in apertura. Giro 4: solo lo scaffale di sinistra. Oltre i 900 px ritaglio verticale 1760x2240 dall'angolo in alto a sinistra (`corsia-v640.jpg`, `corsia-v1240.jpg`: 591 px a 1440, densità 2 coperta); fino a 900 px ritaglio 1760x1640 a tutta larghezza (`corsia-o780/1170/1760.jpg`). Le finestre bruciate (x 1870-2050) e gli scaffali di scatole a destra sono fuori; i due fori neri nel pilastro in fondo sono coperti con una toppa dello stesso pilastro; contrasto +4 %, un filo di calore, ombre appena sollevate. Da qui anche `anteprima-1200.jpg` (1200x630) per l'anteprima nei messaggi.
- Codici leggibili sull'originale ingrandito, con il centro del cartellino in pixel dell'originale: =BF593 (272,178) su un filtro blu accanto alle scatole Baldwin; 33398 (832,178) su una scatola; 20201 (325,1362) su una cartuccia; FF155 (247,1940) scritto a mano su una scatola. FF108 (25,2185) è leggibile ma tagliato dal bordo sinistro della foto; FS20.., =2040.., FS204.., FF10.. e ..92 sono coperti a metà. Per questo i cartellini sono quattro (tre fino a 900 px, dove FF155 resta fuori dal ritaglio) e non 5-8: non ci sono altri codici interi.
- `2015-04-home_factory_slider_bg.jpg` (piramide, iPhone, 2016, 4032x3024, già scontornata su bianco puro), nella sezione del magazzino. Il plinto bianco al centro, grigio-lilla (circa 230,230,240), è portato verso #F3EEE2 con una maschera sui pixel chiari e neutri; sotto la fila bassa c'è un'ombra di contatto (fascia scura sotto il punto più basso di ogni colonna, sfocata 14 e 60 px, al massimo 32 %), solo sul fondo; i filtri sono scaldati di circa 150-200 K, il fondo no. Ritaglio 4032x2730, moltiplicato per la carta #FBF8EF: il fondo coincide con la pagina. `pila-780/1170/1440/2880.jpg` (giro 4: 2880 al posto di 2400, densità 2 coperta a 1440). I cartellini stanno sui codici stampati: P60-8677 (in basso sul Donaldson PowerCore, al posto del nome di linea "PowerCore"), SH 51054 (HIFI), 33119 (FuelManager), LF3883 (Fleetguard), ricontrollati sull'immagine ingrandita.
- `2015-04-IMG_1589.jpg` (banco, iPhone, 2016, neon). Giro 4: ritaglio largo 4032x1440 con tutte e tre le persone (l'uomo che parla, il ragazzo che scrive, l'uomo con la barba a destra, prima tagliato) e il piano con le carte; il tubo al neon resta fuori. Rumore: sfocatura leggera sulla luminanza (0,8 px) e più forte sul colore (3 px), al posto del mediano 3x3, poi la riduzione di scala; pannello fucsia desaturato al 92 %, autocontrasto, luce scaldata di poco. `banco-780/1170/1440/2880.jpg`.
- Logo `2015-11-centrofiltriveneto_logo.png`, ridotto a 720 px; giro 4: PNG a tavolozza di 128 colori con la trasparenza (da 44 a 8 KB). Icona della pagina: `2017-01-favicon-32x32.png` del sito di oggi (il tondo giallo "CFV"), copiata com'è in `icona-32.png`.
- Mappa disegnata in SVG dai dati OpenStreetMap (ODbL), con l'attribuzione sotto la mappa.

## Cosa è cambiato nel giro 5 (ritocchi tecnici)

Dal rapporto finale. Nessun cambio d'impianto: solo i difetti misurati.

- **Cartellini della corsia**: non coprono più i cartellini veri. Ognuno sta 14 px a destra del bordo del cartellino scritto (il bordo è misurato sull'immagine ingrandita: --rx 1,3-2,7 % della foto), con un filo giallo di 14 px e un contorno scuro sottile che li collega; =BF593, 33398, 20201 e FF155 a pennarello si leggono nella foto. Stessa posizione nel ritaglio del telefono. Nessun ritaglio nuovo della corsia.
- **Campo**: segnaposto "scrivi il codice del filtro" al posto di "per esempio LF3883".
- **Colonna accanto alla foto**: famiglie e marchi non sono più spinti in fondo: stanno 40 px sotto l'email (32 sotto i 1181 px). Il vuoto di 161 px a 1440 non c'è più; la colonna finisce a 669 px e la foto a 820.
- **Cartellini della piramide**: telefono 14 px (13 sotto i 375), alti 28 px con un'area di tocco di 52 (51 sotto i 375); da 641 a 1260 px area di tocco 49 px; sopra 48. P60-8677 resta almeno 10 px dentro la foto (sul telefono non va più a sinistra di 53 px dal bordo).
- **Foto del banco oltre i 1440 px**: sulla griglia, a filo di logo, mappa e didascalia (112-1424 a 1536, 304-1616 a 1920, 624-1936 a 2560). Fino a 1440 resta a tutta larghezza.
- **Mappa**: "Via Vigonovese" al 47 % su tutto il telefono (prima solo sotto i 375 px); da 641 a 760 px "Via Vigonovese" e "Via Statuto dei Lavoratori" salgono (50,5 % e 63,5 %). Nessuna etichetta copre il tracciato a nessuna larghezza.
- **Piede da 641 a 900 px** (fuori elenco, visto negli screenshot): "info@centrofiltriveneto.com" si spezzava in "...co / m"; ora va a capo solo dopo la chiocciola.

**Respinti**
- Ritaglio più stretto della corsia, ingrandito al doppio: i quattro codici distano 1760 px nell'originale, un ritaglio su due o tre ripiani ne terrebbe uno o due, e a densità 2 la foto andrebbe ingrandita oltre l'originale. I cartellini veri ora si vedono spostando quelli della pagina.
- Apertura con la fila dei cartellini al centro, o col campo sullo scaffale: è un cambio d'impianto, e questo era l'ultimo giro.
- Foto del banco a 1312 px anche a 1440, o ritagliata sulle mani: a 1312 l'area foto scende al 34,3 % (soglia bloccante 35 %); il ritaglio sulle mani cambia la foto. Resta in attesa dello scatto nuovo chiesto nel LEGGIMI.

## Cosa è cambiato nel giro 4

Dai rapporti del giro 3 (giudice e tecnica). Nessuna riprogettazione: il gesto proprio dell'apertura è rinforzato e i difetti misurati sono chiusi.

**A. I cartellini diventano l'immagine**
- Corsia ritagliata sullo scaffale di sinistra, in verticale: filtri e cartellini grandi, finestre bruciate e scatole anonime fuori. I fori nel pilastro sono coperti.
- Cartellini a 20 px (18 px sotto i 1261 px e sul telefono), alti 37-41 px con un'area di tocco di 45-49 px, ben dentro la foto (BF593 a 39 px dal bordo alto a 1440), centrati sui cartellini veri (verificato sovrapponendo i centri all'immagine ingrandita). Quattro, perché nella foto non ci sono altri codici interi.
- Focus dei cartellini a doppio anello, giallo e inchiostro: si vede sugli scaffali scuri e sulla carta (`_prova/giro4/shot/focus-*.png`).
- "Hai il codice?" con campo e bottone giallo sta sotto il titolo, accanto ai cartellini: a 1366x657 (finestra utile di un portatile 1366x768) il bottone finisce a 464 px, a 1536x730 a 474, a 390x664 a 323.
- Il piano blu tiene solo "Hai solo il mezzo?" e "Hai il filtro vecchio?": niente più fila di tre colonne. Blu e pennellate restano.
- Tolta la frase che spiegava i cartellini; sul telefono c'è una riga sola, "Tocca un codice sulla foto: ti rispondiamo su WhatsApp." Tolta anche la spiegazione sotto la piramide.
- Il codice va nel messaggio in maiuscolo (`toUpperCase()` per WhatsApp e per l'email; il campo lo mostra già in maiuscolo): "  lf3883 " apre "...avete il filtro LF3883?".
- Foto del banco con tutte e tre le persone, a tutta larghezza in fondo a "Dove siamo", con meno rumore e il fucsia spento. Il consenso resta condizione nel LEGGIMI.

**B. Difetti misurati**
- Famiglie: titolo sopra l'elenco a tutta larghezza; il vuoto di 500 px a 1440 non c'è più.
- Famiglie coerenti e con fonte: "Multimarca, per mezzi e impianti" con la riga dei prodotti dalla pagina SF Filter (olio, aria, carburante, idraulici, aria condizionata) e "Di GFT Filters siamo distributori" (il portale dice "Distributori GFT Filters"); "Auto e veicoli" con la riga "Filtri per auto, fuoristrada e furgoni, compresi i filtri dell'aria e dell'abitacolo" (pagine MANN-FILTER e UFI del sito di oggi).
- Ricambisti: resi ed EXW in una riga breve con il link al portale, dove sono la politica resi e le condizioni di vendita (le pagine del portale si aprono da script, quindi il link porta alla prima pagina).
- Testata su una riga da 761 a 1180 px (a 1024 non va più a capo); da 641 a 760 il menu va ancora su una seconda riga. Titolo e foto partono entrambi sotto la testata a tutte le larghezze sopra 900.
- Pennellate legate alla foto: la prima comincia dal bordo sinistro della foto a tutte le larghezze (0 fino a 1440, 304 px a 1920, 624 a 2560).
- Piede a 320: email spezzata solo dopo la chiocciola, CAP col comune ("30030 Vigonovo (VE)" non si divide), "Il banco è a" con la preposizione legata al nome. Bottoni su una riga a 320 (47 px). MANN-FILTER non si spezza al trattino.
- Piramide a 2880 px (densità 2 a 1440 coperta); logo da 44 a 8 KB; a 1440 densità 1 la pagina scarica 501 KB all'apertura e 625 KB dopo lo scorrimento (prima 749).
- Icona della pagina (il tondo "CFV"), og:title, og:description, og:image (1200x630) e dati strutturati LocalBusiness (indirizzo, telefono, email, partita IVA).
- Etichette della mappa a 12 px sul telefono.

**Respinti o lasciati**
- 5-8 cartellini: nella foto ci sono quattro codici interi e leggibili; non ne aggiungo di parziali o inventati.
- Foto in WebP: non fatto. Il peso a 1440 è già sceso a 501 KB iniziali; il JPEG resta l'unico formato.
- Pagina Privacy: non esiste nemmeno sul sito di oggi; resta nel LEGGIMI, nessun link vuoto in pagina.
- Striscia del banco nello sportello "Hai il filtro vecchio?": la foto del banco va in "Dove siamo", come chiesto, e non si ripete.
- A 901 px la colonna del testo è circa 20 px più alta della foto: resta una striscia di carta sotto la foto prima del frontale.

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

## Controlli fatti (giro 5)

- Build rifatta; i quattro screenshot guardati a pezzi (`_prova/giro5/p1440/`, `p390/`) e screenshot miei a 320, 641, 1024 e 1920 (`_prova/giro5/shot/`), tutti a pezzi; focus di BF593 col doppio anello (`shot/focus-BF593.png`).
- Scorrimento orizzontale: nessuno (`scrollWidth == innerWidth`) alle 32 larghezze da 320 a 2560, col telefono emulato sotto i 641 px (`_prova/giro5/js/misura4.mjs`, `_prova/giro5/misura.txt`).
- Cartellini: nessuno ne tocca un altro e nessuno esce dalla foto (almeno 8 px dentro) a nessuna larghezza. Piramide, P60-8677 e 33119: 28 px di distanza a 320 (aree di tocco 16), 51 a 390; corsia, BF593 e 33398: 26 px a 320.
- Mappa: nessuna etichetta copre il tracciato o il punto, nessuna sovrapposizione, da 320 a 1920 (`js/mappa.mjs`).
- Prima schermata: campo e bottone dentro a 1280x720, 1366x657, 1366x768, 1440x790, 1440x900, 1536x730, 1536x864, 390x664, 390x844, 360x640 e 320x568.
- `segnali.sh` esce con 0 e nessuna soglia bloccante: area foto 36 %, Pathway Extreme 100 %, 3 misure di H2, 4 fasce di fondo, 0 etichette sopra i titoli, 0 frecce. Da guardare: "titolo a sinistra e paragrafo a destra" in 2 sezioni (porte e magazzino), come nel giro 4.
- Nessun U+2014 nella pagina, nel modello, in questa nota e nel LEGGIMI.

## Controlli fatti (giro 4)

- Screenshot della build guardati a pezzi (1440 e 390, `_prova/giro4/p1440/`, `p390/`) e screenshot miei a 320, 768, 901, 1024, 1366x768 e 1920 (`_prova/giro4/shot/`), tutti a pezzi.
- Scorrimento orizzontale: nessuno (`scrollWidth == innerWidth`) a 320, 341, 360, 375, 390, 414, 480, 600, 640, 641, 700, 760, 761, 768, 820, 900, 901, 960, 1024, 1100, 1180, 1181, 1220, 1260, 1261, 1280, 1366, 1440, 1536, 1680, 1920 e 2560, col telefono emulato sotto i 641 px (`_prova/giro4/js/misura.mjs`, `_prova/giro4/misura.txt`).
- Sovrapposizioni: nessun cartellino ne tocca un altro e nessuno esce dalla foto, a tutte le larghezze; il più vicino al bordo è P60-8677 sulla piramide a 320 px, 7 px dentro, perché il codice stampato è a sinistra sul filtro. Le etichette della mappa non si coprono.
- Prima schermata: campo e bottone dentro a 1280x720, 1366x657, 1366x768, 1440x790, 1440x900, 1536x730, 1536x864, 390x664, 390x844, 360x640 e 320x568.
- Collegamenti: WhatsApp col codice in maiuscolo e mailto aggiornato provati (`_prova/giro4/js/peso.mjs`, `_prova/giro4/peso.txt`); nessuna richiesta verso altri domini al caricamento.
- `segnali.sh` esce con 0 e nessuna soglia bloccante: area foto 36 %, Pathway Extreme 100 %, 3 misure di H2, 4 fasce di fondo, 0 etichette sopra i titoli, 0 frecce. Da guardare: "titolo a sinistra e paragrafo a destra" in 2 sezioni (porte e magazzino), erano 3.
- Nessun U+2014 nella pagina, nel modello, in questa nota e nel LEGGIMI.

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
