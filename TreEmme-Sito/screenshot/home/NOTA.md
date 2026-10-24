# Home finale di Tre Emme Manufatti: "Il mozzo", la ruota e il suo codice

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in tre larghezze con srcset, loghi SVG), carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `_prova/script/finale/index.html`, screenshot con `finale_shots.mjs`; con l'argomento `controlli` anche 320, 768, 1024, 1280 e 1920 in `_prova/controlli/`).

Parte dal prototipo A scelto dal giudice. Il K0 era 7,5: la prima schermata non è stata ritoccata ma ripensata dentro la stessa direzione, con la colonna sinistra ridotta a cinque elementi e il gesto spostato in basso, come il righello di Hambro e l'alfabeto di FM Sistemi. Nell'ultimo passaggio (giudizio cieco: K6 a 6 per i pallini numerati sull'oggetto, già usati in altre tre home della campagna) i pallini e le legende numerate sono stati tolti: la legenda adesso è il codice stesso.

## Idea

Una ruota vera di Tre Emme, la Dynamic Happy 24″ (foto loro, ripulita su carta), grande e nitida, senza niente sopra. Sotto il titolo c'è il codice d'ordine che usano davvero, DYHB-12,7+S599BEPS+AAL24, scomposto nei suoi quattro pezzi: sotto ogni pezzo un filetto lungo quanto il pezzo e due righe che dicono cos'è (raggi, cuscinetti, pneumatico, corrimano). Si sceglie il colore dei raggi: cambiano la foto e solo i due pezzi che dipendono dal colore (DYHx e S59x) con le loro righe. È il loro modo di ordinare ("La codifica è semplice ed intuitiva e permette di costruire la ruota completa"), e con il nome di un concorrente la pagina non regge, perché i codici sono i loro.

## Prime due schermate

1. **1440x900.** Testata: logo con il marchio originale (marchio alto 40 px), menu di cinque voci, telefono. A sinistra solo cinque cose: "Ruote per carrozzine" in Saira 400 a 128 px (interlinea 0,95, spaziatura -0,01em), due righe ("Ruote, freni, forcelle e gomme piene in poliuretano. A Saonara, Padova, dal 1981."), poi in basso le cinque pillole dei colori alte 40 px (il nome solo in quella scelta), il codice a 44 px in cifre tabellari con "Copia" a destra (icona a due quadrati disegnata) e, sotto ogni pezzo del codice, il filetto e le due righe in 14 px grigio ("Raggi blu / 12 × Ø3,5", "Cuscinetti / Ø12,7 mm", "Pneumatico blu e nero / antiforatura EPS", "Corrimano / 6 linguette"). Le righe non sono mai più larghe del loro pezzo (misurato da 1024 a 1920 per tutti e cinque i colori), quindi il codice resta compatto. A destra la ruota: riquadro di 880 px, bordo superiore a 110 px dall'alto, niente sopra la foto. Didascalia su una riga: "Dynamic Happy 24×1, novità del 19 agosto 2023".
   **390x844.** Titolo a 56 px, le due righe, la ruota a tutta larghezza (il riquadro è largo il 118 % e il fondo carta sparisce ai lati), "Raggi: blu" scritto sopra cinque bottoni rotondi da 44 px, poi il codice scritto in colonna, un pezzo per riga con i separatori appesi a sinistra (DYHB, -12,7, +S599BEPS, +AAL24) e accanto a ognuno la sua riga, poi "Copia".
2. **Le famiglie.** "Ruote a raggi, anteriori e a dischi": tre ruote vere alla stessa scala (stesso diametro a schermo, base allineata, la stessa ombra rifatta sotto ognuna): Top, ruotina anteriore 5″ in alluminio con gomma TPU, disco a 10 razze da 4″. Una riga e un link per famiglia.

Poi: il mozzo Dynamic-X a 966 px (colonne 1-9) con taglio 5:4 sulla sola flangia davanti, quella a fuoco, e la didascalia con il codice nelle colonne 10-12 in basso; la sezione del poliuretano presa da B (la 200×45 tagliata dal bordo sinistro, "Il poliuretano lo facciamo in casa"), la frase della famiglia in corpo 34 px e le tre righe "per chi" con le garanzie, la chiusura, il piede. Pagina a 1440: 6.278 px compreso il piede.

## Chiusura e piede

- Chiusura: "Vi basterà citare il codice e la quantità" (frase loro, accorciata, dalla pagina Come ordinare: "Vi basterà citare il codice da Voi scelto e la quantità desiderata"), telefono a 44 px con `tel:`, `info@3emme.com` e la commerciale Sara Berto con `mailto:`, l'indirizzo che è esso stesso il link alla mappa, il fax. La frase sta in alto e i recapiti in basso, allineati al fondo della foto. Foto a destra fino al bordo, tagliata in alto: la persona, il lago e gli abeti; la ruota (di altra marca) e le mani sul corrimano restano fuori quadro. "Foto indicativa" è una didascalia di testo grigio 13 px sotto la foto, niente sopra l'immagine. Orari: non pubblicati, quindi non ci sono.
- Piede: logo con il marchio alto 52 px (il PNG è alto 106: 2x) e una riga ("Ruote e componenti per carrozzine, fatti a Saonara dal 1981. Wheels for life!"); newsletter "Novità dall'officina" con campo, bottone inchiostro e casella di consenso; quattro colonne (Ruote, Componenti, Per ordinare, Azienda) e "Seguici" con YouTube e un'icona play disegnata; riga legale con ragione sociale, indirizzo, P.IVA e C.F., REA, capitale sociale, PEC (link `mailto:`), Privacy, Cookie. A 390 le colonne sono una fisarmonica con veri bottoni (`aria-expanded`), "Seguici" resta aperto.
- La newsletter ha senso: 12 notizie pubblicate dal 2015 al 2023, quasi tutte di prodotto, clienti privati oltre a produttori e rivenditori, commerciale "Italia ed estero". Il modulo non invia nulla finché non si collega a un servizio (LEGGIMI): ha `data-collegato="no"` e dopo l'invio risponde "Iscrizione non ancora attiva: scrivi a info@3emme.com per ricevere le novità" con il `mailto:`; il "Grazie" compare solo quando l'attributo vale "si".

## Caratteri e colori

- **Saira** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), file variabile servito dalla pagina (`fonts/saira-var-latin.woff2`). Una famiglia sola: 400 per titoli e testo, 500 per bottoni e titoletti; cifre tabellari per codici e misure; il codice in larghezza 88 % (asse `wdth` dello stesso file) perché stia accanto alla ruota senza perdere corpo; Ø allargato a 125 % perché non si confonda con lo zero. Riferimenti: il grottesco largo di Küschall e il DIN 2014 di Campagnolo e Motion Composites (01-analisi, sez. 7), cioè il registro dei componenti di precisione. Rispetto al prototipo il titolo passa da 300 a 400: più sicuro, meno esile.
- Logo: marchio a mezza ruota preso dal PNG originale del sito (176x106 px, i suoi colori: grigio, raggi neri, asse azzurro, mozzo con verde e rosso) incorporato nell'SVG; la scritta è in tracciati da Ubuntu Bold (Ubuntu Font Licence), il carattere che la scritta del logo sembra usare. Il marchio è a 2,6x nella testata e a 2x nel piede.
- Colori: carta #F3F2EE (fondo della pagina e delle foto), inchiostro #15181D, un solo grigio di testo #565A62 (6,4:1 sulla carta, 5,7:1 sul piede #E9E7E1), filetti #D6D3CC, blu del logo #0B3F94 solo per il passaggio del mouse e il fuoco. Il colore pieno lo danno i raggi.

## Interazione

Un solo gesto: il gruppo dei cinque colori (radiogroup), con clic, dito o frecce, Home e Fine. Cambiano la foto (dissolvenza di 160 ms solo su ciò che si tocca) e i due pezzi del codice che dipendono dal colore, con le loro righe; per i lettori di schermo il codice intero e la sua spiegazione sono in una riga `aria-live`. Codici veri dalla scheda Dynamic Happy: DYHB-12,7+S599BEPS+AAL24, DYHY-12,7+S599YEPS+AAL24, DYHR, DYHN e DYHW-12,7+S595NEPSX+AAL24. "Copia" mette il codice negli appunti, diventa "Copiato" e lo annuncia ai lettori di schermo. Nessuna animazione allo scorrere, nessun effetto sul cursore, i bottoni cambiano colore pieno (niente opacità). `prefers-reduced-motion` toglie anche la dissolvenza.

## Foto, origine e licenza

- Dell'azienda (da 3emme.com, `assets/originali/`, restano loro; si usano solo nella proposta a loro): Dynamic Happy nei cinque colori; mozzo Dynamic-X 12 cavi; Top argento; ruotina anteriore 125 mm in alluminio con TPU; ruota 4″ a 10 razze; 200DPU60 in poliuretano; marchio del logo. Trattamento comune con PIL: fondo da studio stimato e diviso (flat field) e riportato alla carta, polvere tolta, per le famiglie ombra originale tolta e rifatta uguale; per il mozzo contrasto +12 % e luci compresse sotto il bianco della carta, così il bordo dritto non fa un rettangolo; il taglio è sulla flangia davanti (la flangia dietro, fuori fuoco, resta sotto il 15 % del riquadro). Lo scatto originale è morbido già a 1:1: il file più grande è 1230 px, per questo va rifatto (LEGGIMI).
- Chiusura: Zachary Kyra-Derksen su Unsplash, "Free to use under the Unsplash License" (verificata, in `assets/CREDITI.md`), mai usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md`), tagliata 1600x1130 dall'alto dello scatto perché la carrozzina di altra marca resti fuori. Nessuna foto nuova scaricata, nessuna immagine generata.

## Controlli fatti (ultimo passaggio)

- Screenshot rifatti in `screenshot/home/` e guardati a pezzi a 1440 e 390; anche 320, 768, 1024, 1280 e 1920 (`_prova/controlli/`). scrollWidth uguale alla finestra a 320, 360, 390, 414, 600, 768, 820, 960, 1024, 1100, 1180, 1280, 1366, 1440, 1680, 1920 e 2560.
- Interazione provata con Playwright (`_prova/script/prova_finale.mjs`): frecce, Home e Fine spostano scelta e fuoco e cambiano foto, DYHx, S59x e le loro righe; Tab porta a "Copia", Invio copia davvero negli appunti ("Copiato" e annuncio per i lettori di schermo); tocco su "rosso" a 390 e a 768; menu aperto a 768 e a 390 (pannello a tutta altezza, nessuna riga tagliata sotto); fisarmonica del piede con `aria-expanded`; newsletter senza nessun "Grazie".
- Misure (`_prova/script/misura_codice.mjs`): nessun cerchietto numerato in pagina; a 768 telefono e Menu distano 42 px; a 1024 tra la fine della riga sotto il titolo e il copertone più di 40 px; a 390 icona e parola YouTube distano 9 px; logo del piede a 2,04x; mozzo a 966 px.
- Collegamenti: `tel:+390498790210` (due volte), `mailto:` per info, Sara Berto, PEC e il messaggio della newsletter, indirizzo con il link a Google Maps.
- `_metodo/kit/segnali.sh`: 0 soglie bloccanti su 10, 0 da guardare su 8; foto 35,4 % della pagina, Saira 100 %, 3 filetti larghi, 4 misure di H2, 0 frecce, 0 etichette maiuscole.
- Nessun U+2014 nella pagina, in questa nota e nel LEGGIMI (lo script di build ora controlla solo i file di testo: prima si fermava su una sequenza casuale dentro un JPEG). Nessun segnaposto in pagina.
- Dati: ogni fatto viene da 01-analisi.md e dalla scheda Dynamic Happy del crawl (righe nuove: 12 raggi Ø3,5, pneumatico "blu/nero EPS" e "giallo/nero EPS", corrimano "Allum 6 linguette").

## Cosa è cambiato nell'ultimo passaggio

1. Apertura: tolti i quattro pallini sulla ruota e la fila di legende numerate; il codice è diventato la legenda (filetto e due righe sotto ogni pezzo; in colonna sul telefono).
2. Mozzo Dynamic-X: da 1296 px 2:1 a 966 px 5:4 sulla sola flangia a fuoco, didascalia e codice a destra in basso.
3. Chiusura: foto tagliata senza la carrozzina, "Foto indicativa" in didascalia sotto la foto, recapiti allineati al fondo.
4. Testata a 1024 e meno: telefono spostato a sinistra del bottone Menu (42 px a 768); menu aperto a tutta altezza con fondo pieno.
5. Piede: icona YouTube staccata dalla parola a 390, marchio a 52 px (2x), PEC come link, newsletter che non conferma iscrizioni finché non è collegata.
6. Riga sotto il titolo più stretta da 1180 px in giù, didascalia dell'apertura allineata alla griglia anche sopra i 1584 px.
