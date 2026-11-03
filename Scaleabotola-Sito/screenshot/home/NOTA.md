# Home Scalarredo (Scaleabotola): nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///, scritta a mano: niente più sorgente composto), immagini in `sito/img/` (JPEG a due misure con srcset), carattere in `sito/fonts/`. La versione 1 com'era prima di questo passaggio (sito, screenshot, LEGGIMI e CREDITI) è copiata in `_prova/versione-1-originale/`; i suoi script (`home_finale.src.html`, `build_finale.py`, `disegno.py`, `finale_img.py`) restano in `_prova/script/` ma non servono più. Per questa azienda non c'era una "versione 1 con l'uso" separata: l'uso è stato rifatto qui dalla scheda `_prova/uso/SCHEDA.md`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari) adattata a un negozio-magazzino di scale, sezione B (difetti tipici), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 (foglio `riferimenti.jpg`) e a 390 di tutti e 14, le pagine intere di Union e Joseph Brot a pezzi; le note del livello professionale di Unicar e Panificio Fornasiero e il foglio `_invio/zona/home/livello-professionale.jpg`.

Rifare tutto: `sh _prova/script/build_finale.sh --immagini controlli` (immagini con `pro_img.py`, screenshot all'ora simulata martedì 3 novembre 2026 alle 10.00, poi 320, 768 e 1024 in `_prova/tmp-pro` e `pro_controlli.mjs`). Solo i controlli: `node _prova/script/pro_controlli.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (7.227 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11.752 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Negozio e orari" al piede). Guardati a pezzi a 390 e 1440 accanto ai riferimenti, e a 320, 768 e 1024 (prime schermate e pagine intere), più il menu aperto a 390.

### Che cosa è cambiato, in breve

- **Uso prima di tutto (scheda, par. 4 e 8).** Titolo nuovo con le parole della scheda, che dice il mestiere: "Scale retrattili per la soffitta, pronte o su misura" (il vecchio "Si chiude in soffitta e non ingombra" spiegava una cosa che chi ha il foro sa già). Nella prima schermata, a 390 e a 1440: le quattro voci del foro (Soffitto da 238 € + IVA, Parete da 425 € + IVA, Terrazzo, Soppalco) che portano alle misure; "Chiama l'ufficio tecnico 049 900 00 99" pieno e "Manda le misure del foro" (mailto con oggetto "Misure del foro" e il testo con le tre misure da riempire); sotto, le tre misure da dare; la riga "Aperto ora / Chiuso, riapre..." calcolata sull'ora di Roma e sui festivi, con via Marco Polo 2, Mestrino, statale 11 e "Indicazioni". A 1440 a destra la PLUS e il link alle scale da interno.
- **Struttura della famiglia B adattata.** Testata fissa con "Negozio e orari" come prima voce, "Negozio online" e il telefono in un bottone; apertura con mestiere, luogo, prova e azione; blocco scuro "In quanto tempo arriva" con quattro numeri (5 giorni, 2-6 settimane, 150 kg, 306 prodotti) e consegna, posa, guida e assistenza; "La vostra misura c'è?" con le tabelle dei fori standard per tipo, i prezzi "da", le misure in più del negozio e il link alla categoria del negozio online; scale da interno in quattro schede fotografiche con il dato utile e tre tipi senza foto (chiocciola, pedata alternata, ringhiere in vetro), poi "Mandateci il disegno"; racconto della PLUS ("La scala retrattile comoda e bella", loro titolo) con la gamma Easy, PLUS, Motorizzata, ISO 50; blocco giallo "Mandateci le misure o il disegno" con il modulo; blocco scuro "Negozio e orari" con indirizzo, stato, tabella degli orari, Chiama, Indicazioni e il telefono grande ("Chiamateci per un preventivo immediato", loro frase); piede in quattro colonne.
- **Identità.** Il giallo #FFD700 torna: il logo è un blocco giallo con il marchio e la scritta "Scalarredo scale" nel blu #0075FF del logo vero (estratta dal PNG); il giallo fa anche il blocco del modulo, le cifre e i bottoni sui blocchi scuri. Registro da commerciante tecnico, col "voi": "Chiamateci per un preventivo immediato", "Vieni a vedere la tua scala nel nostro negozio di Mestrino", "consulenza rapida, esaustiva e gratuita", "Spediamo giornalmente tramite corrieri in tutto il paese", "Realizziamo fuori misura in tempi rapidi". Tolti: le quote disegnate sulla foto, il disegno in sezione, "progettate, prodotte e posate da noi" esteso alle retrattili, il fondo carta.
- **Foto, decisione "niente".** Nessuna foto di repertorio e nessuna illustrazione. Solo foto loro che reggono, in due formati: 4:5 (la PLUS d'apertura e le quattro scale da interno) e 3:2 (i gradini in frassino della PLUS). Stesso trattamento per tutte (`pro_img.py`: bianchi portati al neutro, stessa curva, saturazione un po' smorzata, nitidezza fine), mai ingrandite oltre l'originale (Boston ed elicoidale servite a 480 px, la misura nativa del taglio). Tolta la Montreal bianca da telefono ritoccata (oggetti di casa cancellati a mano) e il disegno in sezione.
- **Tipografia.** Una sola famiglia, Archivo, due pesi (400 e 700), titoli a larghezza 92%. Sei misure a 1440 (84, 56, 24, 18, 16, 14) e sei a 390 (40, 30, 22, 17, 16, 14); il 14 solo nella riga legale del piede.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata sticky (80 px a 1440, 72 a 390), "Negozio e orari" prima voce; a 390 a metà pagina il bottone "049 900 00 99" si vede e si tocca (48 px; a 1440 "Chiama 049 900 00 99"); 6 link `tel:` in pagina.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Mestiere nel titolo, "Scalarredo, negozio e magazzino a Mestrino (PD)" nell'occhiello (a 390 "Scalarredo, Mestrino (PD)"), prova "in pronta consegna, di solito in 5 giorni lavorativi", bottone di chiamata 342x52 (a 390 a tutta larghezza, 358x52).
3. **Immagine vera nell'apertura**: PASSA a 1440 (la PLUS a pantografo vista dall'alto nella botola, 431x538, nella colonna destra), IN PARTE a 390: lì la foto viene subito dopo lo stato e "Indicazioni" (a 911 px), come chiede la scheda ("non a tutto schermo sopra al titolo"): la prima schermata del telefono è tutta per i compiti. È un oggetto, non persone o sede: le foto dello showroom e delle persone non esistono (LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche (`assets/esterne/` non è usata in pagina).
5. **Foto in serie**: PASSA. Due formati (4:5 e 3:2), stesso trattamento, nessuna didascalia (6 foto a 1440). Limite dichiarato: sono scatti di origini diverse (reflex, telefono, forse catalogo) e il trattamento comune li avvicina ma non li rende una serie vera.
6. **Palette dal marchio**: PASSA. Quattro token: giallo #FFD700 e blu (#0075FF nel marchio, scurito a #0062D6 per bottoni e link, AA su bianco) dal logo, inchiostro #0E1A2B e bianco; tre grigi. Niente `--carta` beige.
7. **Scala corta e leggibile**: PASSA. 6 misure a 1440 e 6 a 390; testo 18/17 px; nulla sotto i 14 px; titolo 84 px interlinea 1,0 a 1440 (fascia B 85-90 px: 1 px sotto, perché il titolo stia su tre righe nella colonna e la prima schermata tenga tutto), 40 px a 390. Non in maiuscolo: è una frase lunga, in maiuscolo andrebbe su cinque righe.
8. **Due famiglie al massimo**: PASSA. Una sola: Archivo (titoli 700 stretti, testo 400, etichette e bottoni 700); anche moduli e bottoni ereditano il carattere.
9. **Schede con la foto del lavoro**: PASSA per le scale da interno: 4 schede in 4 colonne (2 a 390), tutte cliccabili, foto 4:5 dello stesso taglio, nome, dato e link alla pagina del tipo sul loro sito. Le schede dei fori retrattili sono senza foto apposta: sono tabelle di misure (come le tabelle dei modelli di Negrizzolo, sezione B13), e una foto vera per tipo di foro non c'è.
10. **Almeno tre tipi di prove**: NON PASSA, per mancanza di materiale. C'è un tipo: quattro numeri (5 giorni, 2-6 settimane, 150 kg con prova a 260 kg, 306 prodotti). Recensioni pubbliche: nessuna (scheda, par. 1); clienti con il nome: nessuno; certificazioni: la portata certificata è scritta, ma senza logo né norma finché non confermano quale (UNI EN 14975 con anni diversi nei due siti). Non inventati: da chiedere (LEGGIMI).
11. **Lavori con un nome**: NON SI APPLICA con le fonti di oggi: nessuna scala posata ha cliente, comune o anno. Le schede delle scale da interno mostrano scale posate per tipo; con tre lavori nominati (LEGGIMI) diventa una galleria.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: "In quanto tempo arriva" e "Negozio e orari" scuri, il modulo giallo, le scale da interno su grigio chiaro; spazi 120 px a 1440 e 72 a 390; margini 80 e 16 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e con il bordo, raggio 4 px, 52 px (48 in testata a 390), testo 16 px; ogni bottone di chiamata contiene il numero. Sui blocchi scuri il pieno è giallo con il testo inchiostro, stessa forma.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta in quattro caselle (scala retrattile, scala da interno, visita in showroom, altro), nome, telefono, email, comune e, per la retrattile, foro, altezza e solaio; compone un'email con oggetto ("Misure del foro, Nome") e campi; foto e disegni si allegano all'email che si apre (da collegare a un servizio: LEGGIMI). Negozio con stato, tabella degli orari (la riga di oggi evidenziata), "Chiama" e "Indicazioni" (`google.com/maps/dir`); nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ce ne sono di confermate). Logo, chi sono, negozio con indirizzo, orari, telefono, email e indicazioni; retrattili con il catalogo PDF; scale da interno, negozio online e YouTube; riga legale con ragione sociale, P.IVA e C.F., CCIAA, capitale sociale, sede legale di Rubano, PEC, condizioni di vendita, privacy e cookie. Quattro colonne a 1440, testo minimo 14 px.

### Prove d'uso della scheda (par. 8)

- **Visitatore 1, telefono 390x844**: senza scorrere il bottone `tel:+390499000099` (358x52), le quattro voci del foro, "Manda le misure del foro" e le tre misure scritte sotto. Toccando "Soffitto" la pagina va alla scheda: titolo, tabella, "Easy da 238 € + IVA" e il link al negozio stanno tutti nella schermata (titolo a 108 px, link a 536 px). Tempi in un solo punto: "5 giorni" e "2-6 settimane" nel blocco subito dopo l'apertura.
- **Visitatore 2, computer 1440x900**: "Scale da interno" in testata e "vedete le scale posate" nell'apertura; quattro foto vere di scale posate; "anche su vostro disegno" nel titolo, "Mandateci il disegno" e il modulo con "Scala da interno"; indirizzo, sabato mattina e "Indicazioni" in un solo blocco.
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

- Apertura a tutto schermo con una foto (famiglia B, punto 2): l'unica foto forte è la PLUS dall'alto, forse del fornitore, e a 390 la scheda vuole i compiti prima della foto.
- Manifesto e racconti con persone e laboratorio (famiglia B, punti 3 e 4): non ci sono foto di persone, del magazzino o dello showroom; resta un solo racconto, quello della PLUS, con la loro frase.
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
