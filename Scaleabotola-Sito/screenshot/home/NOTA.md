# Home Scalarredo (Scaleabotola): nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///, scritta a mano: niente più sorgente composto), immagini in `sito/img/` (JPEG a due misure con srcset), carattere in `sito/fonts/`. La versione 1 com'era prima di questo passaggio (sito, screenshot, LEGGIMI e CREDITI) è copiata in `_prova/versione-1-originale/`; i suoi script (`home_finale.src.html`, `build_finale.py`, `disegno.py`, `finale_img.py`) restano in `_prova/script/` ma non servono più. Per questa azienda non c'era una "versione 1 con l'uso" separata: l'uso è stato rifatto qui dalla scheda `_prova/uso/SCHEDA.md`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari) adattata a un negozio-magazzino di scale, sezione B (difetti tipici), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 (foglio `riferimenti.jpg`) e a 390 di tutti e 14, le pagine intere di Union e Joseph Brot a pezzi; le note del livello professionale di Unicar e Panificio Fornasiero e il foglio `_invio/zona/home/livello-professionale.jpg`.

Rifare tutto: `sh _prova/script/build_finale.sh --immagini controlli` (immagini con `pro_img.py`, screenshot all'ora simulata martedì 3 novembre 2026 alle 10.00, poi 320, 768 e 1024 in `_prova/tmp-pro` e `pro_controlli.mjs`). Solo i controlli: `node _prova/script/pro_controlli.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8.017 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11.400 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Negozio e orari" al piede). Guardati a pezzi a 390 e 1440 accanto ai riferimenti, e a 320, 768 e 1024 (prime schermate e pagine intere), più il menu aperto a 390.

### Che cosa è cambiato, in breve

- **Uso prima di tutto (scheda, par. 4 e 8).** Titolo nuovo con le parole della scheda, che dice il mestiere: "Scale retrattili per la soffitta, pronte o su misura" (il vecchio "Si chiude in soffitta e non ingombra" spiegava una cosa che chi ha il foro sa già). Nella prima schermata, a 390 e a 1440: le quattro voci del foro (Soffitto da 238 € + IVA, Parete da 425 € + IVA, Terrazzo, Soppalco) che portano alle misure; "Chiama l'ufficio tecnico 049 900 00 99" pieno e "Manda le misure del foro" (mailto con oggetto "Misure del foro" e il testo con le tre misure da riempire); sotto, le tre misure da dare; la riga "Aperto ora / Chiuso, riapre..." calcolata sull'ora di Roma e sui festivi, con via Marco Polo 2, Mestrino, statale 11 e "Indicazioni". A 1440 a destra la PLUS e il link alle scale da interno.
- **Struttura della famiglia B adattata.** Testata fissa con "Negozio e orari" come prima voce, "Negozio online" e il telefono in un bottone; apertura con mestiere, luogo, prova e azione; blocco scuro "In quanto tempo arriva" con quattro numeri (5 giorni, 2-6 settimane, 150 kg, 306 prodotti) e consegna, posa, guida e assistenza; "La vostra misura c'è?" con le tabelle dei fori standard per tipo, i prezzi "da", le misure in più del negozio e il link alla categoria del negozio online; scale da interno in quattro schede fotografiche con il dato utile e tre tipi senza foto (chiocciola, pedata alternata, ringhiere in vetro), poi "Mandateci il disegno"; racconto della PLUS ("La scala retrattile comoda e bella", loro titolo) con la gamma Easy, PLUS, Motorizzata, ISO 50; blocco giallo "Mandateci le misure o il disegno" con il modulo; blocco scuro "Negozio e orari" con indirizzo, stato, tabella degli orari, Chiama, Indicazioni e il telefono grande ("Chiamateci per un preventivo immediato", loro frase); piede in quattro colonne.
- **Identità.** Il giallo #FFD700 torna: il logo è un blocco giallo con il marchio e la scritta "Scalarredo scale" nel blu #0075FF del logo vero (estratta dal PNG); il giallo fa anche il blocco del modulo, le cifre e i bottoni sui blocchi scuri. Registro da commerciante tecnico, col "voi": "Chiamateci per un preventivo immediato", "Vieni a vedere la tua scala nel nostro negozio di Mestrino", "consulenza rapida, esaustiva e gratuita", "Spediamo giornalmente tramite corrieri in tutto il paese", "Realizziamo fuori misura in tempi rapidi". Tolti: le quote disegnate sulla foto, il disegno in sezione, "progettate, prodotte e posate da noi" esteso alle retrattili, il fondo carta.
- **Foto, decisione "niente".** Nessuna foto di repertorio e nessuna illustrazione. Solo foto loro che reggono, in due formati: 4:5 circa (la PLUS d'apertura e le tre schede delle scale da interno) e 3:2 (la Montreal del racconto); i gradini in frassino sono stati tolti nel ritocco finale. Stesso trattamento per tutte (`pro_img.py`: bianchi portati al neutro, stessa curva, saturazione un po' smorzata, nitidezza fine), mai ingrandite oltre l'originale (Boston ed elicoidale servite a 480 px, la misura nativa del taglio). Tolta la Montreal bianca da telefono ritoccata (oggetti di casa cancellati a mano) e il disegno in sezione.
- **Tipografia.** Una sola famiglia, Archivo, due pesi (400 e 700), titoli a larghezza 92%. Sei misure a 1440 (84, 56, 24, 18, 16, 14) e sei a 390 (40, 30, 22, 17, 16, 14); il 14 solo nella riga legale del piede.

### Ritocco finale (3 novembre 2026, dal controllo del livello professionale e dalle prove dei due clienti tipo)

Il controllo aveva dato 6 su 10 ("sembra un buon template da e-commerce, non una bottega"). Cambiato:
- **Apertura**: da 1180 px la foto della PLUS non è più un riquadro nella colonna ma sborda a destra per tutta l'altezza dell'apertura (40vw, senza raggio, ritaglio nuovo da `PLUS-pantografo.jpg` a 900x1155, mai ingrandito); sopra, in basso a sinistra, una targa bianca con lo stato "Aperto ora", l'indirizzo, "Indicazioni" e il link alle scale da interno. Le quattro tessere del foro sono piene nel giallo del marchio (#FFD700, testo inchiostro, circa 14:1; al passaggio inchiostro e bianco), alte 96 px a 1440: in prima schermata c'è la massa di colore del marchio e la scelta del foro si distingue dai bottoni blu. Titolo a 88 px (fascia B). La prova si vede: "5 giorni lavorativi" e "2-6 settimane" in grassetto con un sottolineato giallo nel lead (prima il fuori misura era solo "in tempi rapidi"). Accanto a "Dove va il foro?" il link "Tempi e consegna" porta al blocco #consegna. Terrazzo e Soppalco dicono "prezzo al telefono" invece di una misura senza prezzo. Sotto i bottoni: "Servono il foro, l'altezza pavimento-soffitto, lo spessore del solaio e una foto."
- **"La vostra misura c'è?"**: niente più tabelle. Le misure sono pastiglie ("45×70", "45×80"...) a 16 px, una riga per larghezza; quelle con una scheda nel negozio (soffitto 80×120 e 100×100, parete 70×100 e 80×130) sono blu e portano alla scheda. Il prezzo dice la misura ("Easy 50×90 238 € + IVA", "PLUS 50×80 320 € + IVA"). In ogni blocco, dentro le misure, la riga sull'altezza di 300 cm (prima stava sopra l'ancora e finiva sotto la testata) e `scroll-margin-top` sui blocchi. Soffitto porta alle linee Easy e PLUS (il negozio non ha una categoria "a soffitto"). Sotto i 641 px ogni tipo è un `<details>` chiuso con nome, prezzo e link sempre in vista; toccando una tessera dell'apertura il tipo scelto si apre da solo (script su clic e su hashchange): dopo il tocco su "Soffitto" la 60×90, il prezzo e il link al negozio stanno nella schermata.
- **Scale da interno**: si apre con un racconto foto e testo, la Montreal intera (`montreal-012.jpg`, 3422 px, la foto vera migliore) in 3:2 a 7/11 della larghezza (servita a 900 e 1600 px), accanto la loro frase «La nostra azienda, che produce scale per interno, opera in questo settore da due generazioni.» e i dati della Montreal. Sotto, tre schede 4:5 in 3 colonne (New York a zeta, Boston a rampa su cremagliera, elicoidale), a 390 in righe con la foto a sinistra. Etichette dei link uguali ai titoli ("Vedi le scale a zeta", "Vedi le scale a rampa"...), link esterni in una scheda nuova.
- **La PLUS**: tolta la foto dei gradini in frassino (`banner-bg2.jpg`, vecchia e morbida, con un vuoto di 130 px sotto). Ora è un blocco tipografico: titolo a sinistra, paragrafo a destra, sotto la gamma in quattro schede con il filetto di 4 px inchiostro come i blocchi del foro (Easy, PLUS, Motorizzata, ISO 50 a 56 px, una riga di differenza, il dato in blu: prezzo, 20 secondi, pannello da 50 mm).
- **Modulo**: corretto il difetto bloccante. `[hidden]{display:none!important}`: con "Visita in showroom" e "Altro" i campi delle misure spariscono davvero. Con "Scala da interno" i campi restano, con le etichette "Foro nel solaio" e "Da piano a piano", la lista a sinistra diventa "la pianta o il disegno, il foro nel solaio, l'altezza da piano a piano" e le misure arrivano nell'email. "Mandateci il disegno" sceglie da solo "Scala da interno". Accanto all'invio: "Se non si apre nulla, scrivete a scalarredo@scalarredo.it" cliccabile.
- **Foto**: in `pro_img.py` una luce comune (il 30% più chiaro di ogni foto, cioè le pareti, portato allo stesso valore con una curva gamma) prima del trattamento di sempre; la New York ristretta sulla scala e smorzata (saturazione 0,62) perché la carta da parati pesi meno; la Montreal con meno correzione del bianco, che faceva virare il divano. Formati: 4:5 circa (0,78 la PLUS d'apertura, 0,8 le schede) e 3:2.
- **Telefono grande** nel negozio portato a 88 px come il titolo: le misure restano 6 a 1440 (88, 56, 24, 18, 16, 14) e 6 a 390.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot, dopo il ritocco)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata sticky (81 px a 1440, 73 a 390), "Negozio e orari" prima voce; a 390 a metà pagina "049 900 00 99" si vede e si tocca (48 px); 6 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Mestiere nel titolo, Mestrino nell'occhiello, prova in evidenza ("5 giorni lavorativi" e "2-6 settimane" in grassetto col sottolineato giallo), bottone di chiamata 342x52 (a 390 358x52, a tutta larghezza).
3. **Immagine vera nell'apertura**: IN PARTE. A 1440 la PLUS vera dentro la botola occupa tutta l'altezza della colonna destra (576x750), non è scontornata; a 390 viene subito dopo stato e "Indicazioni" (a 895 px) perché la scheda vuole i compiti nella prima schermata. Non mostra persone, sede o magazzino: quelle foto non esistono e, per decisione del committente, al loro posto non c'è nessuna illustrazione (LEGGIMI, "Foto da fare dal vero").
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da `assets/esterne/` o da banche.
5. **Foto in serie**: PASSA, con un limite. Due formati (4:5 circa e 3:2), nessuna didascalia, 5 foto a 1440; luce delle pareti pareggiata e stesso trattamento. Restano origini diverse (reflex, telefono, forse catalogo) e la Boston e l'elicoidale sono native a 480 px: mostrate a circa 380 px a 1440 su schermi 2x si sgranano (originali più grandi da chiedere, LEGGIMI).
6. **Palette dal marchio**: PASSA. Giallo #FFD700 e blu (#0075FF del logo, #0062D6 per testi e bottoni), inchiostro e bianco, più i grigi; niente beige. Il giallo ora è anche nelle tessere del foro in prima schermata.
7. **Scala corta e leggibile**: PASSA. 6 misure a 1440 (88, 56, 24, 18, 16, 14) e 6 a 390 (40, 30, 22, 17, 16, 14); testo 18/17 px; 14 solo nella riga legale; titolo 88 px (fascia B 85-90) e 40 px a 390.
8. **Due famiglie al massimo**: PASSA. Una sola, Archivo, pesi 400 e 700.
9. **Schede con la foto del lavoro**: PASSA. 3 schede in 3 colonne, cliccabili per intero, foto 4:5 dello stesso taglio, nome, dato e link, più il racconto della Montreal. Le retrattili per tipo di foro restano senza foto (non esiste una foto vera per tipo): sono pastiglie di misure con prezzo e link.
10. **Almeno tre tipi di prove**: NON PASSA, per mancanza di materiale. Un tipo su quattro: i numeri (5 giorni, 2-6 settimane, 150 kg con prova a 260 kg, 306 prodotti). Recensioni, certificazioni e clienti con il nome non sono nelle fonti: non inventati, da chiedere (LEGGIMI, "Per arrivare al livello dei riferimenti mancano").
11. **Lavori con un nome**: NON SI APPLICA con le fonti di oggi (nessuna scala posata con cliente, comune e anno); il LEGGIMI chiede tre lavori.
12. **Ritmo a blocchi**: PASSA. Apertura bianca con la foto a tutta altezza, "In quanto tempo arriva" scuro, misure bianche, scale da interno grigio chiaro, PLUS bianca, modulo giallo pieno, negozio scuro, piede grigio chiaro; spazi 120 px a 1440 e 72 a 390; margini 80 e 16 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e con il bordo, raggio 4 px, 52 px (48 in testata a 390), testo 16 px, il numero in ogni bottone di chiamata. Le tessere del foro ora sono piene gialle (navigazione, non un terzo modello di bottone) e le pastiglie delle misure sono etichette con lo stesso raggio.
14. **Modulo e "dove e quando"**: PASSA. Tipo di richiesta in quattro caselle, campi adatti al tipo, email composta con oggetto e tutti i campi (provato anche con "Scala da interno": foro 100 x 250, da piano a piano 280, solaio 30 arrivano nell'email); negozio con tabella degli orari, "Chiama" e "Indicazioni"; nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (nessuna confermata). Quattro colonne a 1440, testo minimo 14 px.

### Rispetto al controllo, non fatto o fatto diversamente

- Montreal come quarta scheda con un ritaglio diverso della stessa foto: la foto è già nel racconto grande; ripeterla due volte nella stessa sezione si notava. Le schede sono tre, in 3 colonne.
- Prezzo accanto a ogni misura e link per ogni misura: non ci sono nelle fonti; i link ci sono solo per le quattro misure con una scheda letta nel negozio (LEGGIMI).
- Occhiello con "da due generazioni": la frase è loro ma riguarda le scale da interno; è nel racconto della Montreal, non sopra il titolo delle retrattili.
- Mappa nella pagina e ora di chiusura del sabato: niente iframe (regola 14) e l'ora non è nelle fonti (LEGGIMI).
- A 390 la foto resta dopo i compiti (stato e "Indicazioni" nella prima schermata, a 775-824 px).

### Prove d'uso della scheda (par. 8)

- **Visitatore 1, telefono 390x844**: senza scorrere il bottone `tel:+390499000099` (358x52), le quattro tessere gialle del foro, "Manda le misure del foro" e le misure da dare scritte sotto; "5 giorni lavorativi" e "2-6 settimane" già nel lead, e "Tempi e consegna" porta al blocco completo. Toccando "Soffitto" la pagina va al blocco e apre le misure: prezzo "Easy 50×90 238 € + IVA" a 309 px, "Vedi le Easy" a 361 px, la 60×90 a 607 px, tutti nella schermata (`USO-1B`).
- **Visitatore 2, computer 1440x900**: "Scale da interno" in testata e "vedete le scale posate" nella targa dell'apertura; quattro foto vere di scale posate (la Montreal grande e tre schede); "anche su vostro disegno" nel titolo; "Mandateci il disegno" porta al modulo con "Scala da interno" già scelto e le misure arrivano nell'email (`MODULO-I`); indirizzo, sabato mattina e "Indicazioni" in un solo blocco.
- **Visitatore 3, telefono 390x844**: lo stato è nella prima schermata (a circa 760 px) con "Indicazioni" sotto (un tocco apre Google Maps sul percorso fino a via Marco Polo 2, 35035 Mestrino). Stato provato a nove orari: martedì 10.00 "Aperto ora, fino alle 12.30"; martedì 13.30 "Chiuso ora. Riapre alle 15.00"; domenica "Riapre domani alle 9.00"; venerdì 19.30 "Riapre domani mattina"; sabato 10.00 "Aperto ora. Il sabato solo la mattina: chiamate prima di passare"; sabato 15.00 "Riapre lunedì alle 9.00"; 8 dicembre "Oggi è festa, chiuso"; prima delle 9 e alle 16 giusti. Con JavaScript spento resta l'orario della settimana.
- **Identità**: logo giallo con il marchio blu nella prima schermata a tutte le larghezze (sotto i 385 px resta il quadrato giallo con il marchio, senza la scritta).

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 375, 390, 414, 768, 1024, 1280, 1440, 1920 e nessun errore in console (`pro_controlli.mjs`). Corretti durante il lavoro: a 320 il bottone "Chiama l'ufficio tecnico" che allargava la colonna (ora va a capo col numero intero), "2-6 settimane" che a 1440 toccava "150 kg" e a 768 usciva dal margine, le voci del foro troppo strette a 1024 (ora 2x2 tra 1024 e 1279), i campi del modulo disallineati a 320, la riga legale stretta in una colonna.
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440 e con il menu aperto a 390 (il menu si apre col tocco, dice "Chiudi", si chiude con Esc e toccando una voce).
- Collegamenti: un solo numero `tel:+390499000099`; `mailto:scalarredo@scalarredo.it` (anche con oggetto "Misure del foro" e "Richiesta dal sito"), `mailto:Scalarredo@pec.it`; una mappa con nome e indirizzo; nessuna ancora rotta, nessun link a pagine locali che non esistono (le voci puntano alle pagine vere di scalarredo.it).
- Dati: ogni fatto in pagina viene da `01-analisi.md` o da `_prova/uso/SCHEDA.md` (prezzi del 03/11/2026, 306 prodotti, terzo dominio, CAP 35035 da infoisinfo); le misure dei fori sono lette sulle tavole "MISURE STANDARD DISPONIBILI" in `assets/originali/scaleabotola/scheda-misure-*.jpg` (anche 140 e 170 cm a terra, gradini 10x35 del soppalco). Il dubbio va nel LEGGIMI.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Archivo (Omnibus-Type, Google Fonts), SIL Open Font License 1.1, uso commerciale libero; file variabile latino con assi peso e larghezza, servito dalla pagina in `sito/fonts/archivo-latin.woff2`. Il file non ha le frecce: in pagina non ce ne sono.

### Respinti o non applicati, apposta

- Apertura a tutto schermo con una foto (famiglia B, punto 2): fatta a metà, con la PLUS a tutta altezza su 40vw a destra; a tutto schermo coprirebbe i compiti, e a 390 la scheda vuole i compiti prima della foto.
- Manifesto e racconti con persone e laboratorio (famiglia B, punti 3 e 4): non ci sono foto di persone, del magazzino o dello showroom; resta un solo racconto foto e testo, quello della Montreal, con la loro frase "da due generazioni".
- Facciata del negozio nella scheda "Negozio e orari": nessuna foto dell'insegna sulla statale 11 (da fare).
- Fascia di certificazioni, recensioni, clienti e lavori con il nome: non sono nelle fonti; non inventati.
- Video dei tre Shorts in pagina: niente iframe (regola 14) e niente video scaricati; c'è il link al canale.
- I contatori del loro sito ("425+ altezze, 100+ misure, 40+ combinazioni"): senza fonte, restano fuori.
- Newsletter: non pubblicano novità e una scala si compra una volta.

---

## Versione 1 (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, disegno, pagina, screenshot; con `controlli` anche 320, 768, 1024, 1920, il menu aperto a 390 e `controlli.mjs`). Sorgente: `_prova/script/home_finale.src.html` più `marchio.part` (marchio SVG), `quote.part` (quota della foto d'apertura) e `disegno.part` (scritto da `disegno.py`), composti da `build_finale.py`; immagini da `finale_img.py`.

Pagina alta 4.843 px a 1440 compreso il piede (6.678 a 390, 4.331 a 1024, 7.451 a 768, 5.728 a 1920).

### Idea

La home è una tavola d'architetto: il prodotto vero con le sue misure vere disegnate sopra, poi lo stesso linguaggio nel disegno in sezione di "Dove va il foro?". In apertura la PLUS a pantografo vista dall'alto dentro il foro della botola: il bianco della scala sul parquet di rovere, una quota blu sul primo gradino (10 cm, la profondità del gradino in acciaio stampato) e la scritta "pannello 18 mm" sul pannello della botola. Il titolo "Si chiude in soffitta e non ingombra" viene dalla loro pagina della PLUS ("Una volta chiusa, la scala si chiude in soffitta e non ingombra spazio utile"); "Dove va il foro?" è accanto al bottone del telefono, nella prima schermata.

### Le prime due schermate

1. A 1440: testata sottile; a sinistra il titolo in Archivo 300 a 86 px, una riga su chi sono (retrattili e scale da interno), il bottone nero "Chiama lo 049 900 00 99" e il link "Dove va il foro?", in basso un cartiglio con tre dati in cifre tabellari (5 giorni dal magazzino, 2-6 settimane fuori misura, 150 kg di portata e collaudo a 260 kg) col filo allineato al fondo della foto; a destra la foto fino al bordo (835 x 846). Sotto, la didascalia che spiega le due misure. A 390: foto a tutta larghezza con quota e scritta, poi titolo, testo e bottone nella prima schermata.
2. Retrattili: testo a sinistra, il gradino in frassino della PLUS a destra fino al bordo (709 px, file da 1180), poi "Dove va il foro?".

Poi: scale da interno (la Montreal antracite a filo del bordo sinistro, l'attacco "Da due generazioni..." e gli otto modelli con le misure vere), chiusura con la Montreal bianca, piede.

### Caratteri e colori

- Archivo (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile latino con assi peso e larghezza servito dalla pagina in `fonts/archivo-latin.woff2`. Una sola famiglia: titoli 300 a larghezza 104 % con spaziatura da -0,03 a -0,042em, testo 400, voci e bottoni 500-600, cifre tabellari per misure, prezzi, orari e telefono. Scritte della foto a 16,5 px (13,5 a 390), scritte del disegno a 15,5 unità (circa 15 px a 1440, 13 px a 390).
- Colori: carta #F7F6F3, inchiostro #14171A, grigio #565B62 (AA su carta e sul piede), blu del marchio scurito #1F4FA8 per quote, marchio e scheda attiva, piede su #EDECE8. Il caldo viene dalle foto: il parquet sotto la botola e il gradino in frassino.
- Riferimenti: Marretti (bianco, una scala grande, menu leggero), EeStairs (didascalia in riga sotto la foto); Kvadrat e Zahner per il rigore di griglia e il piede a colonne.

### Interazione

"Dove va il foro?": quattro schede vere (Soffitto, Parete, Terrazzo, Soppalco; `role="tab"`, frecce, Home e Fine, clic o dito) che cambiano di netto il disegno in sezione e i dati (foro, altezza, spazio a terra, nota del modello, prezzo di partenza del negozio dove c'è). Unica transizione: il colore di schede e bottoni al passaggio (150 ms, spenta con prefers-reduced-motion). Niente animazioni allo scorrere, niente effetti che seguono il cursore. Il bottone Menu sotto i 1024 px è l'unico altro elemento attivo.

### Foto: origine, licenza, lavorazione

| File in `img/` | Origine | Licenza | Lavorazione | Densità a 1440 su schermo 2x |
|---|---|---|---|---|
| `plus-800/1120` | `assets/originali/scalarredo/PLUS-pantografo.jpg` (2000 x 1335, sul loro sito, probabile foto di catalogo) | dell'azienda o del fornitore, da confermare | ritaglio 1120 x 1135 dentro la botola (fuori la ringhiera in ferro battuto e la sedia rossa del piano di sotto), contrasto locale leggero, appena più calda, nitidezza fine; nessuna riduzione del rumore | 1,34x (a 390: 2,9x) |
| `frassino-640/1180` | `scaleabotola/banner-bg2.jpg` (PLUS vera, 1600 x 757) | dell'azienda o del fornitore, da confermare | taglio stretto sul gradino frontale e sulla struttura bianca (fuori molla e lamiere), bianco neutralizzato | 1,66x |
| `antracite-640/955` | `scalarredo/montreal-012.jpg` (foto loro, reflex) | dell'azienda, da confermare | solo rampa e gradini bianchi, taglio abbassato di 70 px (fuori il triangolo di muro scuro), luce schiarita, colore smorzato | 1,35x (più larga entra lo sgabello) |
| `montreal-760/1240` | `scalarredo/scale-giorno-Montreal-1.jpg` (foto loro, da telefono) | dell'azienda, da confermare | riduzione del rumore dimezzata rispetto al giro precedente e microcontrasto sui bordi; nastri grigi tolti dal muro e correnti ricostruiti, una vite tolta; taglio sopra la sedia e la pianta | 1,51x |
| `scritta-blu.png` | scritta "Scalarredo scale" estratta dal logo PNG vero | dell'azienda | dal giallo al trasparente, blu #1F4FA8 | |

Il marchio a triangolo è un SVG tracciato dai contorni del PNG vero (fedele). Nessuna immagine generata dall'IA, nessuna foto di repertorio in pagina, nessuna nuova scaricata, nessuna foto di fibbie di Ruan Richard Rodrigues.

### Chiusura e piede

Chiusura: "Vieni a vedere la tua scala nel nostro negozio di Mestrino", adattata da scaleabotola.com/contatti.html ("Vieni a vedere la tua scala presso il nostro negozio di Mestrino PD"), a sinistra; telefono grande con tel:, email con mailto:, indirizzo con il link alla mappa, orari; a destra la Montreal bianca fino al bordo con la sua didascalia.

Piede: marchio SVG blu con la scritta e una riga su chi sono; colonne Scale da interno, Scale retrattili, Azienda, Contatti con Seguici (solo YouTube, l'unico social che esiste); riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, sede legale, PEC, Privacy e Cookie. A 390 le colonne si impilano in quest'ordine. Niente newsletter: non pubblicano novità, fiere o collezioni e una scala si compra una volta; al suo posto il link al catalogo PDF delle retrattili.

### Cosa è cambiato in questa rifinitura (dal giudizio cieco)

- Apertura rifatta: al posto della Montreal bianca da telefono, troppo ripulita e servita a 1,13x, la PLUS a pantografo nitida e calda, a destra fino al bordo invece che a tutta larghezza (così il file regge meglio); titolo nuovo preso dai loro testi e legato alla retrattile; cartiglio con tre dati.
- Quote con valori: "10 cm" sul gradino, disegnata sui due spigoli veri del gradino (controllati su un ingrandimento), e "pannello 18 mm"; scritte a 16,5 px in cifre tabellari. Le vecchie quote senza numero sono tolte.
- Chiusura: tolta la foto Pexels dell'elicoidale di Ubud; al suo posto la Montreal bianca, prodotto loro, riesportata più nitida.
- Retrattili: il frassino non è più una fascia a tutta larghezza da 1440 x 560 ma una colonna di 709 px col taglio stretto sul gradino.
- Disegno in sezione rifatto da `disegno.py`: scala come due montanti paralleli con 12 gradini a passo costante, tutti i tratti a 1,25 px, niente zig-zag; tolti gli archi senza etichetta; parete con il foro aperto nel muro, la portina chiusa tratteggiata e quella aperta incernierata in basso con l'arco "la portina ruota di circa 170°"; soppalco senza le quote 140/170 a terra; "170 cm per aprirla" scritto per esteso.
- Tolta la fascia delle due frasi grandi: "Da due generazioni..." apre la sezione delle scale da interno.
- Antracite: taglio abbassato di 70 px.
- Schede del foro a 390 su una riga (20 px, spazio 16); sotto i 375 px su due righe a griglia.
- Piede: logo SVG blu più grande al posto del quadrato giallo PNG.
- Tolto il preload del carattere (errore CORS aperto da file://): console senza errori.
- Questa nota: la frase della chiusura è dichiarata "adattata", non "verbatim".

### Controlli

- `controlli.mjs`: nessuno scorrimento orizzontale a 320, 360, 390, 414, 600, 768, 900, 1023, 1024, 1180, 1280, 1440, 1680, 1920, 2560, con ognuna delle quattro schede aperta; tastiera sulle schede (frecce, Home, Fine: aria-selected, pannello e disegno giusti, tabindex 0/-1); schede provate anche col tocco; menu a 390 aperto col tocco ("Chiudi", aria-expanded true) e chiuso con Esc col fuoco che torna al bottone; collegamenti tel:+390499000099, mailto:scalarredo@scalarredo.it, mailto della PEC, mappa Google su "Scalarredo Via Marco Polo 2 Mestrino"; nessuna ancora rotta; nessun errore in console.
- Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440, 1920, il menu aperto a 390 e le quattro schede a 1440.
- Nessun U+2014 nella pagina, negli script e nei .md.
- `segnali.sh`: una soglia sotto il valore, l'area foto al 30,9 % (soglia 35 %). Scelta voluta: per servire le foto più nitide (da 1,34x a 1,66x su schermo 2x) non le ho allargate oltre; la sezione col disegno in sezione (circa 750 x 600 px) non conta come foto. Il giro precedente arrivava al 39 % con foto a 1,1x, che il giudice ha bocciato come morbide. Si risolve con le foto nuove dello showroom (vedi LEGGIMI), che permettono foto più grandi alla stessa nitidezza. Da guardare: H2 in due misure (56 e 63 px), voluto; nessun contenuto con data o nome perché non c'è un fatto sicuro (vedi LEGGIMI). Una sola famiglia, 4 filetti, nessuna etichetta maiuscola sopra i titoli.
- Dati confrontati con `01-analisi.md` (aggiunte le tre frasi della pagina PLUS a pantografo con la fonte): la norma UNI EN 14975 resta fuori finché non la confermano.
