# Ferridea: analisi per la nuova home

Sito: https://www.ferridea.com/ (crawl e screenshot del 20/10/2026: home, 5 pagine di lavori, contatti, feed). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `ferridea.com/`.

## 1. In breve

- **Chi**: Ferridea di Malimpensa Mario, viale Veneto 32, Saonara (PD). È una **ditta individuale** (impresaitalia.info), non una società: niente capitale sociale.
- **Cosa fa davvero**: un'officina di fabbro e carpenteria leggera. Fa cancelli in ferro battuto e in lamiera, ringhiere e parapetti, capottine (pergole e pensiline in ferro e vetro o policarbonato), scale e serramenti, più serrature, saldature e riparazioni. Lavora acciaio inox, ferro e alluminio (home).
- **Per chi**: soprattutto case private e palazzine: villette, cortili, balconi, vani scala. Le foto mostrano lavori a casa del cliente, non opere industriali. Nessun cliente è citato.
- **Dove**: Saonara, nella zona di viale Veneto. Le foto hanno nomi di luoghi come Treviso e San Giacomo, ma non dicono dove sono stati fatti i lavori.
- **Da quando**: "operante nel settore dal 1959" (home). La P.IVA attuale non può essere del 1959: il 1959 è con ogni probabilità l'inizio dell'attività di famiglia, da confermare (sez. 9).
- **Quanti**: "piccola-media dimensione" (home). Dipendenti e metri quadri non sono pubblici.
- **Correzioni alla nota di partenza**: le categorie sono **cinque**, non sei: Cancelli, Capottine, Parapetti, Scale e Serramenti, più Contatti. Le foto sono **28**. Il "logo" non esiste: è solo il nome scritto in Arial blu.

## 2. Il sito di oggi

**Pagine**: Home, Cancelli, Capottine, Parapetti, Scale, Serramenti, Contatti. È ancora pubblico l'articolo di prova di WordPress "Hello world!" del 01/11/2016, con un commento (`2016/11/01/hello-world/`). Non ci sono pagine di Privacy né di Cookie.

**Testi veri essenziali (verbatim, sono tutti quelli del sito)**:
- Testata: "FERRIDEA di Malimpensa Mario", sotto "Carpenterie metalliche e infissi".
- Home:
  - "La ditta Ferridea di Malimpensa Mario è una realtà aziendale padovana di piccola-media dimensione operante nel settore dal 1959, specializzata in lavorazioni di carpenteria metallica e infissi."
  - "L'Azienda offre ai suo clienti uno servizio a 360°, a partire dallo studio e sviluppo di soluzioni personalizzate fino alla realizzazione delle stesse, e anche successivamente attraverso l'assistenza post-vendita." (refusi originali)
  - "Grazie all'utilizzo di impianti produttivi tecnologicamente avanzati è in grado di ottenere prodotti di elevata qualità con la massima precisione."
  - "Il portafoglio prodotti comprende lavorazioni in acciaio inox, ferro e alluminio, cancelli in ferro battuto e lamiera, ringhiere, parapetti, capottine, scale, serramenti, serrature, saldature e riparazioni in genere."
- Le cinque pagine dei lavori: **nessuna parola**, solo foto (Cancelli 9, Capottine 3, Parapetti 7, Scale 4, Serramenti 4), senza didascalie e senza ingrandimento.
- Contatti: "Viale Veneto 32 / 35020 Saonara (PD) / Tel/Fax +39 049 87 92 451 / Mobile +39 335 52 03 918 / email: info@ferridea.com".
- Sul sito non ci sono macchine, certificazioni, numeri, orari né social.

**Tecnologia**:
- WordPress **4.6.29** (2016) su hosting Aruba, con il tema gratuito "Smpl Skeleton" di Simple Themes e il plugin smpl-shortcodes; jQuery 1.12.4 e menu Superfish.
- Font di sistema ("Sans-Serif", di fatto Arial). Colori: fondo #CECECE, titolo #375199, sottotitolo #BE3243, link #3376EA.
- L'API REST risponde 404 e non c'è una sitemap. La favicon è un file vuoto (0 byte).
- Non c'è meta description. Il `viewport` ha `maximum-scale=1`, che impedisce lo zoom su telefono (un problema di accessibilità).
- Il dominio è registrato dal 03/04/2012 (RDAP Verisign); le foto sono state caricate a novembre 2016.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `cancelli-1440.jpg`, `scale-1440.jpg`, `contatti-1440.jpg`):
- Tutta la pagina è grigio cemento #CECECE, con una doppia riga blu in cima.
- Il nome sta in Arial nero a 56 px, con spaziatura stretta e ombra bianca: sembra un titolo di Word.
- Il menu è fatto di linguette con gradiente e bordi del 2010.
- La home ha una sola foto da 300x225 a sinistra e il vuoto a destra. Seguono tre paragrafi giustificati a tutta larghezza.
- Il piede è solo "WordPress Theme by Simple Themes", grigio #9F9F9F su grigio (contrasto 1,7:1).
- Nessun telefono in testata.
- Le pagine dei lavori sono griglie di miniature da 300 px, di altezze diverse e non cliccabili, senza nemmeno il nome del lavoro.
- In Contatti telefono ed email sono testo semplice (nessun `tel:` né `mailto:`), e non c'è mappa.
- Il sottotitolo rosso su grigio ha un contrasto di 3,6:1: non passa AA.

**Problemi a 390** (`home-390.jpg`, `cancelli-390.jpg`, `scale-390.jpg`, `contatti-390.jpg`):
- Il nome va a capo in "FERRIDEA di / Malimpensa Mario" con un'interlinea enorme.
- Il menu è un elenco di 7 link blu che spinge giù il contenuto.
- La foto resta larga 300 px invece di riempire lo schermo.
- Cancelli diventa una colonna di 9 foto alta 2748 px. Telefono ed email non si toccano.
- Non c'è scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Ferridea di Malimpensa Mario | `contatti`: "Ferridea di Malimpensa Mario". impresaitalia.info la scrive "FERRIDEA DI MALIMPENSA MARIO MARIO" (refuso di registro) |
| Forma giuridica | ditta individuale | impresaitalia.info/kk04365347/ferridea-di-malimpensa-mario-mario/saonara.aspx: "avente la seguente forma giuridica: DITTA INDIVIDUALE" |
| P.IVA | 02602070282 | stessa pagina: "Partita IVA: 02602070282". La cifra di controllo è valida; 028 è l'ufficio di Padova. **Non è scritta sul sito**: va confermata prima di metterla nel piede |
| ATECO | 28.1 | stessa pagina: "classificata col codice ateco 281" (forse dato vecchio: per un fabbro ci si aspetta 25.1) |
| Indirizzo | viale Veneto 32, 35020 Saonara (PD) | `contatti`: "Viale Veneto 32 / 35020 Saonara (PD)"; uguale su aziende.virgilio.it/carpenterie/saonara-pd/ferridea-di-malimpensa-mario e reteimprese.it/carpenterie-metalliche/saonara/azienda/1391229 |
| Telefono e fax | 049 879 2451 | `contatti`: "Tel/Fax +39 049 87 92 451" |
| Cellulare | 335 520 3918 | `contatti`: "Mobile +39 335 52 03 918" |
| Email | info@ferridea.com | `contatti`: "email: info@ferridea.com" |
| PEC, REA, codice fiscale | non trovati | ufficiocamerale, paginegialle, aziendit e trova-aperto rispondono 403, reportaziende 429. Il codice fiscale personale del titolare compare su un elenco, ma non va pubblicato |
| Anno | 1959 (attività) | home: "operante nel settore dal 1959" |
| Dimensione | "piccola-media" | home: "realtà aziendale padovana di piccola-media dimensione" |
| Orari | non pubblicati | un aggregatore (trova-aperto.it, letto solo nell'estratto di ricerca) indica "08:00-19:00" nei giorni feriali e "08:00-12:00" il sabato. Non è affidabile: niente orari in pagina finché l'azienda non li conferma |
| Social | nessuno trovato | ricerche "Ferridea Saonara" con facebook e instagram: nessun profilo |

## 4. Materiale visivo

Ho scaricato le 28 foto del sito alla misura originale (52 MB) in `assets/originali/`. L'inventario con pagina, misura, data e fotocamera dall'EXIF, soggetto e voti (qualità / forza come apertura) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`.
- **Video**: nessuno.
- **Logo**: non esiste (sez. 8).
- **Fotocamere**: compatte Panasonic DMC-FX10, Sony W210, Nikon E2200 e Canon Ixus, con scatti dal 2006 al 2013. Quasi tutte le foto sono da 2816x2112: abbastanza pixel, poca qualità.

| Gruppo | Quanti | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| Scale con gradini in rovere e ringhiera in inox (`Scala-Treviso-011`, `-016`), scala a sbalzo con gradini scuri (`P1020524`) | 3 | 5 | 3 | le migliori: soggetti belli e puliti, ma luce di flash, inquadrature storte e nitidezza morbida |
| Cancello in ferro battuto a volute, frontale (`P1030185`, `P1030186` della home) | 2 | 4 | 3 | lavoro vero e riconoscibile. Il ritaglio sulle volute regge a 1200 px, con rumore |
| Cancelli in lamiera: a pannelli (`P1030320_`), forata a quadri (`P1030183`), portone ad arco storico (`DSCN0383_`) | 3 | 4 | 3 | disegni interessanti, luce piatta di cielo grigio, contesto di strada |
| Altri cancelli scorrevoli e recinzioni | 4 | 3-4 | 1-2 | lampeggianti, asfalto, auto, inquadrature larghe |
| Capottine: pergola bianca in vetro (`P1030303`), tettoia sul pranzo, pensilina sull'auto | 3 | 3-4 | 1-3 | solo la prima è presentabile |
| Parapetti e ringhiere: balconi, inox a cavi, raggiera in lamiera (`P1030315`) | 7 | 3-4 | 1-2 | documentazione di cantiere. La raggiera è l'unico dettaglio "a mano" |
| Scala ancora coperta dal feltro di cantiere | 1 | 3 | 1 | da non usare |
| Serramenti in alluminio bianco in cantiere, con calcinacci e cerniere | 4 | 2-3 | 0-1 | da non usare |

**Verdetto**: il materiale **non regge** una home di alta gamma. In media vale 3,5 su 10 per qualità e 1,8 per apertura, e nessuna foto supera il 5. Ha però un valore che il sito di oggi spreca: sono **lavori veri, tanti e diversi**. Ripulite (raddrizzate, ritagliate, con i colori corretti) le 8-10 migliori possono stare in una sezione "Lavori", non in apertura. Per l'apertura e la chiusura servono i segnaposto della sez. 6. Per il sito vero serve una mezza giornata di foto:
- tre o quattro lavori recenti ripresi di mattina con luce laterale: un cancello frontale come un prospetto, una scala intera dal pianerottolo, un parapetto in controluce;
- dettagli in macro: una voluta battuta, una saldatura molata, un chiavistello;
- l'officina di viale Veneto di giorno, con le mani al lavoro.

## 5. Il soggetto e le due direzioni

**Cosa è bello da vedere**:
- un pezzo di ferro **nella luce di una casa**, cioè una scala sul muro bianco o un cancello frontale, con la sua ombra che lo ridisegna sull'intonaco o sul selciato;
- la differenza tra **ferro battuto e lamiera**, le due parole che il sito usa per i cancelli: la voluta fatta a mano accanto alla lastra tagliata e piegata;
- i tre materiali: ferro, inox, alluminio.

**Il dettaglio solo loro**: "dal 1959" e "dallo studio ... fino all'assistenza post-vendita". È un artigiano che prima disegna il pezzo per quella casa e poi ci torna. Non vende un catalogo.

**Registro**: architettonico, luminoso e domestico. Il lusso di questo mestiere è il pezzo fatto su misura che sta bene nella casa, non la fabbrica. Tek.Lam ha già nero, scintille e oro: qui niente scuro, niente scintille, niente oro.

**Le ispirazioni Graziella e N19**: non le uso. Ferridea non è un soggetto di moda né di lusso: ne tengo solo il principio generale, una cosa per schermata e tanta aria.

**Direzione A, "Ferro sul muro" (chiara, un solo oggetto)**
- **Idea visiva**: un solo pezzo di ferro in luce piena su un muro di calce, grande e a filo del bordo destro. Il titolo è grande e sicuro a sinistra, per esempio "Cancelli, scale e parapetti su misura", con sotto "Saonara, dal 1959"; tutt'intorno tanta aria. Sotto vengono pochi lavori grandi, uno per tipo, con il nome e il materiale.
- **Immagini**: architettura domestica di giorno, scale e ringhiere su intonaco bianco, ombre nette. Apertura: Wegelius, la scala a gradini color minio sul muro bianco. Poi Gomez Angel, Lartey, Henman e le scale Treviso ripulite.
- **Tipografia**: Archivo (Google Fonts, OFL), un grottesco con larghezze variabili. Titoli in semi-esteso 500, testo in normale 400, cifre tabellari per telefono e misure.
- **Colore**: calce #F2F0EB, ferro #222426, grigio micaceo #62666A per i testi secondari (5,1:1). Un solo accento minio #B8401C, il colore dell'antiruggine, usato solo per il bottone del telefono, il lavoro attivo e i link (contrasto 4,9:1 sulla calce).
- **Gesto**: un selettore dei materiali, "Ferro, Inox, Alluminio". Al clic o al tocco cambia di netto la foto grande e la riga che dice cosa ci fanno (per esempio Inox: scale, parapetti, corrimano), senza dissolvenza.

**Direzione B, "Ferro battuto e lamiera" (chiara, frontale da prospetto)**
- **Idea visiva**: il cancello come soglia della casa, ripreso frontale e diritto come in un prospetto d'architetto, centrato su un fondo sabbia. Il titolo racconta le due anime del mestiere: "Ferro battuto e lamiera". Sotto il cancello, la quota della luce in metri (solo quando avremo le misure vere) e il nome del lavoro.
- **Immagini**: prospetti frontali in luce di mattina, con l'ombra a righe del cancello sul selciato, e dettagli in macro delle volute battute. Apertura: Kesselhut, il cancello nero su muro bianco. Poi Prouzet per le volute, i loro P1030185 e P1030320 ripuliti, Young per le capottine e Piunninen per le mani sull'incudine.
- **Tipografia**: Gambetta (Fontshare, ITF Free Font License, uso commerciale) in tondo per i titoli, mai il corsivo, con una serif solida da insegna di bottega. Instrument Sans (Google Fonts, OFL) per il testo.
- **Colore**: intonaco sabbia #ECE7DE, ferro micaceo #2F3133, un accento verde cancello #2F4A3C, il verde scuro dei cancelli veneti (contrasto 7,9:1 sulla sabbia), e carta #FAF8F4 per le fasce.
- **Gesto**: un interruttore "Ferro battuto / Lamiera" sopra la foto di apertura. Scambia di netto le due foto vere dello stesso tipo di cancello, la voluta contro la lastra, e la riga che spiega la differenza. Su telefono sono due bottoni a tutta larghezza.

## 6. Immagini sostitutive

Ci sono 9 foto Unsplash in `assets/esterne/`, con il lato lungo a 2400 px.
- Su ogni pagina ho letto "Free to use under the Unsplash License", e nessuna è Unsplash+. URL, autori, date e note sono in `assets/CREDITI.md`.
- Nessuna è già usata in un'altra home della campagna: ho controllato gli ID in tutti i `CREDITI.md` e `LEGGIMI.md`.
- Nessuna è generata dall'IA e nessuna mostra marchi.
- Unsplash e Pexels bloccano anche curl sulle pagine, quindi le ho lette con WebFetch e ho scaricato le foto da images.unsplash.com.

Le foto, per uso:
- **A, apertura**: Wegelius, scala in acciaio color minio su muro bianco. **B, apertura**: Kesselhut, cancello nero e ombra a righe. Le doghe potrebbero essere di legno: vale solo per luce e composizione.
- **Scale e parapetti**: Gomez Angel (profilo della scala), Lam (lamiera forata), Lartey (ringhiera di condominio, il lavoro più simile al loro).
- **Ferro battuto**: Prouzet, volute con la loro ombra.
- **Capottine**: Young, pergola su terrazza (scatto da telefono, da usare in piccolo).
- **Serramenti**: Henman, telai scuri su mattone bianco.
- **Il mestiere e la chiusura**: Piunninen, mani all'incudine all'aperto e di giorno.

Manca un'immagine vera di Ferridea all'altezza. Il "prima e dopo" del ferro battuto (la barra e la voluta finita) va fotografato da loro.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 20/10/2026. Le prime schermate sono in `riferimenti/<nome>-1440.jpg` e `-390.jpg`, i piedi di tre di loro in `riferimenti/piede-<nome>-1440.jpg`.

1. **Secco Sistemi** (seccosistemi.com, serramenti in acciaio, ottone e corten, Preganziol TV).
   - Cosa lo rende di alta gamma: pagina bianca e quasi vuota, con due foto di realizzazioni accostate come in una rivista e il nome dell'opera sotto ("realizzazione / Biblioteca Civica di Nardò"). Il logo è un quadratino rosso, il carattere Soho è piccolo. Il piede è una sola riga, "contatti", che si apre a fisarmonica.
   - Da non riprendere: la barra "cerca / lista breve" in testata, le foto troppo piccole a 1440 e la bolla della chat.
2. **EeStairs** (eestairs.com, scale su misura, Paesi Bassi).
   - Cosa lo rende di alta gamma: la scala trattata come scultura, con foto di realizzazioni a tutta larghezza e una didascalia col luogo ("Hanover Square, London [GB]"). Nel piede ci sono newsletter, social, telefono ed email su una riga.
   - Da non riprendere: lo slider col contatore 5/16, l'hamburger su desktop, la fascia nera, il riquadro dei cookie arancio e Inter.
3. **Capoferri** (capoferri.it, serramenti dal 1894, Bergamo).
   - Cosa lo rende di alta gamma: la data dentro il titolo ("CAPOFERRI SINCE 1894") sopra una sola foto grande di una casa. È il modo giusto per dire "dal 1959".
   - Da non riprendere: la foto notturna scura, il titolo maiuscolo condensato che urla, l'hamburger su desktop, il muro dei cookie e la lentezza (a 390 non ha finito di caricare in 60 secondi).
4. **De Castelli** (decastelli.com, oggetti e superfici in metallo, Treviso).
   - Cosa lo rende di alta gamma: il metallo come oggetto di lusso, scontornato su bianco con un'ombra morbida e la luce che corre sulle pieghe della lamiera. Ha un logo con una legatura propria.
   - Da non riprendere: la griglia a mosaico di molti oggetti senza titolo né testo, troppo piena.
5. **Bisca** (bisca.co.uk, scale su misura, Yorkshire).
   - Cosa lo rende di alta gamma: una sola foto a tutta pagina di una scala (la curva del corrimano, i gradini in rovere) con una didascalia piccola ("Stairs with Carpet Runner, Leeds"). Il piede è una riga: indirizzo, "Get Directions", telefono ed email.
   - Da non riprendere: il menu maiuscolo a 9 voci, il logo a pennarello, la vignettatura scura, il fondo a texture di carta e i social nei cerchietti.

Scartati: Crittall (una finestra modale "I'm looking for..." sopra la home e testi dentro riquadri grigi) e Siller Treppen (il proxy rifiuta la connessione).

## 8. Per il piede

- **Logo**: non esiste. Nel codice non ci sono SVG né immagini del logo, la favicon è vuota e non ci sono PDF o cataloghi. La testata è testo HTML, "FERRIDEA di Malimpensa Mario" in Arial blu #375199 con sottotitolo rosso #BE3243; il ritaglio è in `assets/originali/logo-testata-sito-attuale.png` solo come documento. Per il piede propongo una scritta "Ferridea" composta nel carattere della direzione scelta, dichiarata nel LEGGIMI come proposta e non come logo. Va chiesto se esiste un marchio su insegna, furgone o carta intestata.
- **Voci di menu e pagine di oggi**: Home, Cancelli, Capottine, Parapetti, Scale, Serramenti, Contatti (`/cancelli/`, `/capottine/`, `/parapetti/`, `/scale/`, `/serramenti/`, `/contatti/`). Conviene tenere gli stessi indirizzi, così non servono redirect. Da togliere: `/2016/11/01/hello-world/`.
- **Colonne proposte**:
  - **Lavori**: Cancelli, Capottine, Parapetti e ringhiere, Scale, Serramenti, Saldature e riparazioni (le prime cinque sono pagine; l'ultima è un'ancora della home).
  - **Ferridea**: Dal 1959, Come lavoriamo ("dallo studio ... all'assistenza post-vendita"), Contatti.
  - **Contatti**: 049 879 2451 (`tel:+390498792451`, anche fax), 335 520 3918 (`tel:+393355203918`), info@ferridea.com (`mailto:`), viale Veneto 32, Saonara (con link a Google Maps).
- **Pagine nuove** da elencare nel LEGGIMI: Privacy e Cookie (oggi mancano), e una pagina Azienda se si vuole raccontare il 1959.
- **Social**: nessuno trovato. Niente colonna "Seguici".
- **Newsletter: no.** Il sito non è aggiornato dal 2016, non hanno notizie, fiere, cataloghi né collezioni. Hanno clienti privati, ma chi compra un cancello o una scala lo fa una volta in vent'anni: una newsletter resterebbe vuota. Una riga nella NOTA lo spiega.
- **Riga legale**: "Ferridea di Malimpensa Mario, ditta individuale, viale Veneto 32, 35020 Saonara (PD), P.IVA 02602070282", poi Privacy e Cookie. La P.IVA viene da un elenco e non dal sito: va confermata, e oggi il sito non la mostra (obbligo di legge). REA e PEC non trovati; capitale sociale non applicabile.

## 9. Da confermare

- L'anno 1959: chi ha cominciato (padre, nonno?) e quando è nata la ditta individuale di oggi.
- La P.IVA 02602070282, il REA, la PEC e il codice ATECO (28.1 sull'elenco, 25.1 atteso).
- Gli orari di officina, oggi non pubblicati.
- Se lo 049 879 2451 è ancora anche il fax, e quale numero mettere in evidenza (fisso o cellulare).
- Una seconda sede o un vecchio indirizzo a Noventa Padovana (via Polati): un risultato di ricerca lo cita, ma non l'ho trovato in nessuna pagina.
- Se esiste un logo o un marchio (insegna, furgone, carta intestata).
- Gli "impianti produttivi tecnologicamente avanzati": quali macchine ci sono in officina, se si possono nominare e fotografare.
- I serramenti: sono di produzione propria o montati (alluminio di quale sistema)?
- Il permesso dei clienti per le foto dei lavori, e i nomi da togliere dai file (Fanton Michele, San Giacomo, Treviso).
- Quanti sono in officina, la zona servita, e se lavorano anche per imprese edili e condomini oltre che per i privati.
- Profili social o recensioni Google: non trovati.
