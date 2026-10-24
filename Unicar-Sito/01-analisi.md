# Unicar: analisi per la nuova home

Sito: http://www.unicarcarrelli.it (crawl e screenshot del 24/10/2026: home, 6 voci di menu, 3 sottopagine, 2 notizie, modulo, privacy). Le pagine del sito sono indicate con il percorso dopo `unicarcarrelli.it/`. Fonti esterne citate come URL + frase.

## 1. In breve

- **Chi**: Unicar srl, via Canada 12, 35127 Padova (zona industriale). È l'officina della consociata **Cami2 srl** (via Canada 16, stesso complesso): "la consociata Unicar srl, alla quale è affidata l'assistenza tecnica del prodotto" (cami2.it/azienda/storia/). Cami2 la chiama "Unicar Srl (consociata Service Padova)" (cami2.it/azienda/).
- **Cosa fa davvero**: assistenza, riparazione e manutenzione di carrelli elevatori di ogni marca, in particolare BT e Cesab (oggi Toyota Material Handling); ricambi originali e di altre marche; batterie e caricabatterie; controlli di sicurezza; formazione dei carrellisti (`azienda`, `servizi`).
- **Correzione della nota**: vendita e noleggio **non** sono di Unicar ma di Cami2. La pagina `azienda/vendita_e_noleggio.php` parla solo di Cami2 e rimanda a cami2.it.
- **Per chi**: solo aziende. "aziende leader di tutti i settori merceologici", su "Padova e provincia" (`azienda`).
- **Quanti**: "12 mezzi adatti per l'assistenza presso la clientela" e "messa in funzione entro 24 ore dalla chiamata" (`azienda`). Il testo è del 2012: i "12 furgoni" della nota vanno riconfermati.
  - Numeri di gruppo (Cami2 insieme a Unicar, cami2.it/azienda/): "60 dipendenti, di cui 25 tecnici esterni dotati di furgoni attrezzati", "circa 3500/4000 carrelli di proprietà dei clienti", "un sito di oltre 4000 mq".
- **Da quando**: "da ormai trenta anni" (`azienda`), scritto intorno al 2012, quindi dai primi anni Ottanta: è una mia stima. L'anno vero non è pubblico (sez. 3).
- **Attenzione prima di proporre**:
  - Cami2 dal 5/11/2024 è in maggioranza del Gruppo Selini (comunicato del 16/12/2024).
  - La P.IVA di Unicar non risulta attiva nel VIES.
  - Il furgone del service su cami2.it porta la livrea "Toyota Material Handling / Cami2", non Unicar.
  - Può darsi che Unicar sia stata assorbita o lo stia per essere: va verificato (sez. 9).

## 2. Il sito di oggi

**Pagine**:
- Home, Azienda (più la sottopagina Vendita e noleggio), Servizi (più Assistenza e Ricambi), Dove siamo (mappa Google incorporata), News (2 articoli), Gallery (21 foto), contatti (modulo in iframe), Privacy.
- Mancano `robots.txt` e `sitemap.xml`, che rispondono con una pagina d'errore.

**Testi veri essenziali (verbatim)**:
- Home (h1 "Unicar: Assistenza carrelli elevatori"):
  - "L'assistenza è un settore complesso, nel quale occorre mantenere standard qualitativi alti ed affiancare il cliente come consulenti più che di riparatori, contribuendo all'ottimizzazione ed alla sicurezza del suo parco carrelli."
  - "I tecnici dedicati agli interventi esterni sono specializzati ad intervenire su tutte le marche e modelli, in particolare su su Toyota - Cesab carrelli elevatori." (il "su su" è nel testo originale)
  - "Per ogni nuova unità presa in carico, si procede con un esame tecnico approfondito, si definisce il piano d'intervento e si concorda con il cliente il metodo di operazione."
- Azienda:
  - "Unicar è un'azienda specializzata nel servizio assistenza sul prodotto BTCESAB, con personale altamente qualificato e aggiornato in gradi di garantire la riparazione di qualsiasi marca di carrello elevatore."
  - "un magazzino ricambi estremamente fornito e con 12 mezzi adatti per l'assistenza presso la clientela, in gradi di intervenire anche nei casi più ostici e di garantire la messa in funzione entro 24 ore dalla chiamata."
  - "Cami2 e Unicar, in sinergia tra loro, vi assistono e consigliano prima e dopo la vendita del carrello elevatore."
- Servizi (elenco completo):
  - Preventivi.
  - Normative di sicurezza.
  - Controlli sicurezza.
  - Manutenzione programmata.
  - Formazione per carrellisti.
  - Riparazione e manutenzione batterie.
  - Vendita ricambi originali.
  - Riparazione carrelli di marche primarie.
  - Vendita e montaggio anelli gommati.
  - Trasformazioni, riparazioni impianti elettronici.
  - Assistenza autorizzata per riparazioni carica batterie.
- Assistenza:
  - "In caso di riparazione o revisione, l'Area Tecnica si impegna per garantire continuità al ciclo produttivo del cliente, assicurando la disponibilità di carrelli sostitutivi e concludendo l'intervento in modo rapido e risolutivo."
  - Nella stessa pagina: "contratti di manutenzione programmata".
- Ricambi:
  - "ricambi originali Toyota e di tutte le altre marche, kit di aggiornamento e materiali di consumo (batterie, gomme, olio)".
  - "reperisce qualsiasi tipo e marca di ricambio, anche prodotto all'estero o uscito di produzione".
  - "Il magazzino si occupa dello smaltimento dei materiali esausti e dei ricambi sostituiti."
- News:
  - "Nota informativa": un buon testo sugli obblighi dell'art. 71 del D.Lgs. 81/2008. Dice che le verifiche si annotano su registro, che i controlli vanno conservati tre anni, che funi e catene vanno controllate "trimestrali" e che la buona prassi è il "tagliando annuale".
  - "Corso teorico e pratico per conduttori di carrelli elevatori", destinato agli "Addetti alle attività di magazzino con uso di carrelli elevatori".
- Testata (immagini con testo impresso): "AFFIDABILI DI NATURA", "ESPERTI DI NATURA", "VELOCI DI NATURA", "ASSISTENZA AUTORIZZATA" con i loghi BT e Cesab. In alto, maiuscolo spaziato: "ASSISTENZA CARRELLI ELEVATORI".
- Nessuna certificazione di Unicar. Quelle citate sono di Cami2: ISO 9001:2015 BSI, Toyota A.S.E.C. 2012, OHSAS 18001 2013 (cami2.it/azienda/storia/).

**Tecnologia**:
- PHP 5.3.6 su nginx; XHTML 1.0 Strict, impaginato a tabelle; larghezza fissa di 940 px.
- jQuery 1.7.1; il modulo è un "PHP FormMail Generator" in iframe.
- Google Analytics UA-28978302-1, spento dal 2023.
- Caratteri Trebuchet MS e Helvetica; rosso #A4001A.
- File datati tra il 27/01 e il 29/03/2012: il sito ha 14 anni.
- Niente HTTPS, niente banner dei cookie. L'informativa privacy cita ancora il D.Lgs. 196/2003 (prima del GDPR).

**Problemi a 1440** (`_prova/attuale/home-1440-0.jpg`, `servizi-1440-0.jpg`, `gallery-1440-0.jpg`):
- Colonna di 940 px al centro, su un fondo grigio con una fascia rossa.
- La testata è un banner di 939x249 con l'occhio di cavallo e la scritta impressa nell'immagine; lo stesso banner si ripete identico in ogni pagina.
- La home è divisa in tre colonne: due notizie del 2012 troncate a metà parola ("manut [..]"), quattro bottoni rossi a sfumatura e un testo giustificato con buchi.
- I recapiti sono solo nel piede, in grigio chiaro su grigio (contrasto insufficiente), e il telefono non è cliccabile.
- La Gallery mostra miniature tagliate a caso: tre render escono quasi neri con la scritta "vector" a metà.
- Nessuna foto mostra un tecnico Unicar al lavoro.

**Problemi a 390** (`home-390-viewport980.jpg`, `home-390-come-sul-telefono.jpg`):
- Non c'è il meta viewport, quindi il telefono impagina a 980 px e rimpicciolisce tutto a circa il 40 per cento. Il testo diventa di 5-6 px e i bottoni sono minuscoli.
- Il menu a sette voci resta in orizzontale.
- La pagina è lunga 2121 px a 980, con mezzo schermo grigio vuoto sotto il piede.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Unicar srl | cami2.it/azienda/storia/: "la consociata Unicar srl"; il piede di unicarcarrelli.it dice solo "Unicar" |
| P.IVA e C.F. | 01014160285 | piede di ogni pagina: "P.IVA/C.F. 01014160285". La cifra di controllo è valida e il codice d'ufficio 028 è Padova, ma il VIES risponde "isValid: false" (ec.europa.eu, 24/10/2026); quello di Cami2 risponde valido |
| Capitale sociale | 100.000,00 euro | piede: "Capitale Sociale 100.000,00 €" |
| REA | PD 170490 | piede: "CCIA PD170490" |
| Registro | Reg. Trib. 17247 | piede: "Reg. Trib. 17247" (vecchio registro delle società del tribunale, da prima del 1996) |
| Indirizzo | via Canada 12, 35127 Padova | piede: "Via Canada, 12 - Padova"; il CAP 35127 viene dall'indirizzo di Cami2 nella stessa via (VIES: "VIA CANADA 16 35127 PADOVA PD") |
| Telefono | 049 8792361 r.a. | `contatti`: "Tel. 049.8792361 r.a." |
| Fax | 049 8792357 | `contatti`: "Fax 049.8792357" |
| Email | unicar@protec.it | `contatti` e piede |
| PEC | non trovata | |
| Mappa | Google Maps, scheda "unicar padova" (cid 7853003542386361464) | `dove_siamo`, iframe |
| Anno | non pubblico; circa 1982 per stima | `azienda`: "da ormai trenta anni" (testo del 2012) |
| Sede comune | Cami2 e Unicar nella stessa sede operativa, ampliata a 3000 mq nel 2009 | cami2.it/azienda/storia/: "la sede operativa dove Cami2 e Unicar operano si ingrandisce fino a toccare i 3000 mq" |
| Gruppo | 60 dipendenti, 25 tecnici esterni con furgone, 3500/4000 carrelli dei clienti gestiti tra Padova e Venezia | cami2.it/azienda/ (numeri di Cami2 più Unicar insieme) |
| Proprietà della consociata | Cami2 in maggioranza del Gruppo Selini dal 5/11/2024 | gruppo.bancobpm.it/download/gruppo-selini-e-cami2-nuova-sinergia-non-solo-per-padova: "L'acquisizione, formalizzata il giorno 5 novembre 2024" |
| Dipendenti, fatturato di Unicar | non trovati | atoka, aziende.it e reportaziende non hanno la scheda (403, 404 o 429; le schede "Unicar srl" trovate sono di Salerno e Pordenone) |

## 4. Materiale visivo

Ho scaricato 34 file dal sito (circa 2 MB) in `assets/originali/` e 7 immagini di Cami2 per confronto in `assets/originali/cami2/`. L'inventario con misure, soggetto e voti (qualità / forza come apertura, da 0 a 10) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`. Non ci sono video.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| La sede: palazzina di via Canada con le insegne UNICAR, BT CESAB e CAMI2, i furgoni bianchi e due Cesab verdi sul piazzale (`testata/007.jpg`) | 1 | 939x249 | 4 | 4 | il soggetto giusto per una home, ma il file è una panoramica cucita, velata e piccola |
| La squadra: circa 50 persone davanti all'ingresso tra i furgoni (`testata/008.jpg`) | 1 | 939x249 | 3 | 3 | vera e simpatica, ma i volti sono di 10 px; probabilmente è la squadra di Cami2 e Unicar insieme |
| Banner degli occhi (cavallo, elefante, leone) con il testo impresso | 3 | 939x249 | 4 | 0 | repertorio di provenienza ignota; l'idea è da abbandonare |
| Collage in testata (magazzini, baia di carico, Cesab diesel) | 4 | 939x249 | 3 | 1 | inservibili |
| Foto del costruttore: magazzini visti dall'alto, retrattile BT con operatore, Cesab diesel con radiatori | 10 | 680 px | 4-6 | 1-3 | foto da brochure BT e Cesab di circa quindici anni fa: non mostrano Unicar |
| Scontornati su bianco (Cesab verdi, BT arancio) e render su nero con il nome del modello impresso | 11 | 680 px | 5-6 | 1-2 | da catalogo del costruttore; modelli e marchi superati (BT e Cesab oggi sono Toyota) |
| Logo | 1 | 241x100 PNG | 3 | 0 | unico file; serve un vettoriale (sez. 8) |

**Verdetto**: il materiale **non regge** una home di alta gamma. In media vale 2 su 10. Le uniche due foto vere (la sede e la squadra) sono strisce di 939x249 e dicono la cosa giusta nel formato sbagliato. Tutto il resto è del costruttore e ha quindici anni. Per la proposta servono i segnaposto della sez. 6. Per il sito vero servono una mattina di riprese:
- la sede al mattino con i furgoni allineati;
- un tecnico al lavoro su un carrello in officina;
- il magazzino ricambi;
- un carrello appena revisionato, su un fondo pulito.

## 5. Due direzioni artistiche

Le ispirazioni Graziella e N19 non si usano: Unicar è un'officina di assistenza tra aziende, non un soggetto di moda o di lusso. Il registro giusto è quello dei costruttori seri (pulito, tecnico, affidabile), non quello di un atelier.

**Direzione A, "Pronto in 24 ore" (chiara, un solo oggetto)**
- Idea visiva: prima schermata bianca e luminosa con un solo carrello Toyota, grande e nitido, ripreso di tre quarti su cielo coperto e cemento chiaro. Accanto c'è un titolo grande preso dai loro testi ("Messa in funzione entro 24 ore dalla chiamata"), poi tre sezioni: cosa riparano, ricambi, come lavorano.
- Immagini: un carrello appena revisionato, fotografato nel piazzale di via Canada. Segnaposto: Reding (Toyota su cielo bianco, l'adesivo SOFIMA va tolto), Leyva, Duc LE (retrattili BT in fila).
- Tipografia: Archivo (Google Fonts, OFL), con i titoli sull'asse di larghezza a 115-125 in peso 600 e i testi a larghezza normale. Cifre tabellari per "24", "12", "049 8792361".
- Colore: carta #F5F4F1, grafite #1B1D1F, grigio cemento #D9D7D2. Il rosso del logo #EE1C25 compare solo nella C del logo e sul numero di telefono. Niente rosso #A4001A a sfondo pieno.
- Gesto: "Promemoria controlli". Si sceglie il mese dell'ultimo tagliando e la pagina mostra quando cadono il prossimo controllo annuale e i controlli trimestrali di funi e catene, citando la loro nota sull'art. 71 del D.Lgs. 81/2008, con il bottone per chiamare.

**Direzione B, "Via Canada 12" (fotografica e documentaria, chiara)**
- Idea visiva: il posto vero come garanzia. In apertura, a tutta larghezza, la sede al mattino con i furgoni allineati e un titolo sicuro in basso a sinistra. Seguono l'officina e il magazzino ricambi, ognuno con una frase loro ("anche prodotto all'estero o uscito di produzione").
- Immagini: reportage in luce naturale (piazzale, mani sul motore, scaffali dei ricambi), tutto nello stesso tono. Segnaposto: Duc LE (capannone di ricarica luminoso), Yurtman (tecnici sul carrello), Savinov (parete degli attrezzi), Davis (carrellista Toyota).
- Tipografia: Barlow Semi Condensed 600 per i titoli, che riprende senza enfasi il condensato di "AFFIDABILI DI NATURA". Barlow 400 per i testi e IBM Plex Mono per numeri e recapiti (tutti Google Fonts, OFL).
- Colore: cemento chiaro #ECEBE7, inchiostro #151515, rosso segnale #D7141A per un solo dettaglio per schermata e giallo pavimento #F2C230 solo come filo sottile.
- Gesto: un selettore "Elettrico, Diesel, Da magazzino". Cambia la foto grande e le tre voci di servizio pertinenti, prese dal loro elenco (batterie e caricabatterie, anelli gommati, impianti elettronici, ricambi), con un cambio netto e senza dissolvenze.

## 6. Immagini sostitutive

Ci sono 8 foto Unsplash in `assets/esterne/`, lato lungo massimo 2400 px. Su ogni pagina ho verificato la licenza ("Free to use under the Unsplash License", nessuna Unsplash+); URL, autori, date e avvertenze sono in `assets/CREDITI.md`. Nessuna è usata in un'altra home della campagna e nessuna è generata dall'IA.
- A, apertura: Reding, Toyota Tonero su cielo bianco (`r4Y_VNKzAbw`). Altre per A: Leyva (carrello arancio davanti al capannone, molto cielo), Homa (carrello arancio su pavimento lucido).
- B, apertura: Duc LE, retrattili BT Reflex in fila nel capannone di ricarica (`p0VP_TOAd5E`). Altre per B: Yurtman (tecnici al lavoro, solo in piccolo), Savinov (attrezzi), Davis (carrellista su Toyota).
- Comuni: Londono (carrello in penombra, solo se serve un contrasto).
- Ho scartato le foto con un marchio concorrente in primo piano: Hyster, UniCarriers, Doosan, Manitou, Linde e Komatsu.
- Manca una foto di furgone del service: deve essere vera, con la loro livrea.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 24/10/2026. Le prime schermate a 1440 e a 390 sono in `riferimenti/` (JPEG, qualità 78); i caratteri li ho letti dal codice.

1. **Scania** (scania.com/it, veicoli industriali e officine).
   - Cosa lo rende di alta gamma: quattro foto verticali a tutta altezza, ognuna con un solo mezzo, e titoli maiuscoli in Scania Sans Headline. Un'azienda di officina e di servizio con l'aspetto di un marchio premium; a 390 le foto diventano fasce.
   - Da non riprendere: la barra della nazione sopra il menu e il menu blu pieno a due righe.
2. **Fendt** (fendt.com/it, macchine agricole).
   - Cosa lo rende di alta gamma: una sola macchina grande in luce radente, un titolo bianco sicuro e una frase breve ("Nessuna scusa. Nessun compromesso."). Il logo è centrato tra due filetti sottili.
   - Da non riprendere: il carosello 02/05 con le frecce e la foto scurita per far leggere il testo (a noi serve la versione chiara).
3. **Konecranes** (konecranes.com/it-it, gru e servizi industriali).
   - Cosa lo rende di alta gamma: in apertura c'è la macchina vera in primo piano (il paranco arancio), pulita e nitida. Il menu fa capire subito che servizio e ricambi pesano quanto il prodotto; i caratteri sono Plus Jakarta Sans.
   - Da non riprendere: il bottone a gradiente rosso-viola (vietato), la bolla "Contact us" fissa e le tre card sotto.
4. **Kardex** (kardex.com/it-it, magazzini verticali, gli stessi della loro Gallery).
   - Cosa lo rende di alta gamma: una foto chiara e vera di una tecnica davanti alla macchina, il menu in una pillola bianca sopra la foto e un titolo bianco grande in Open Sans.
   - Da non riprendere: il chatbot, il banner dei cookie a tutta larghezza e Open Sans per tutto.
5. **Toyota Material Handling Europe** (toyota-forklifts.eu, il marchio che assistono).
   - Cosa lo rende di alta gamma: una foto di lavoro vera (il trattore elettrico tra i coils d'acciaio), il logo sobrio e una griglia di persone vere. È il riferimento di marchio che il cliente riconosce.
   - Da non riprendere: la griglia a mosaico con le scritte sopra le foto e la testata a riquadro non a tutta larghezza.

Scartati, con le schermate in `riferimenti/scartati/`:
- toyota-forklifts.it e linde-mh.it: banner dei cookie a tutto schermo.
- linde-mh.com e still.it: slider con puntini e testata da catalogo.
- Combilift: foto velata di verde e bottoni pieni.
- Jungheinrich: risponde 403.
- Kalmar: verifica anti bot.
- Hilti: promozioni dell'app.
- Volvo CE: banner dei cookie.

## 8. Per il piede

- **Logo**: c'è solo `assets/originali/logo-unicar-241x100.png` (PNG trasparente). È fatto così:
  - "UNI" e "AR" in lettere bastone nere filettate, con una linea bianca interna e un'ombra grigia a rilievo;
  - in mezzo una grande C rossa #EE1C25 a doppio anello, che abbraccia la A.

  Nel codice non c'è nessun SVG e la favicon non esiste. Una ricostruzione in SVG "piatta" (filetti neri, C rossa a doppio tratto) è fattibile ma toglie il rilievo grigio: va mostrata come proposta e confermata. Altrimenti si usa il PNG ingrandito a 2x, che però è morbido. Serve il file originale.
- **Voci per le colonne** (dal menu di oggi):
  - Servizi: Assistenza, Manutenzione programmata, Ricambi, Batterie e caricabatterie, Controlli di sicurezza, Formazione carrellisti.
  - Azienda: Chi siamo, Dove siamo, Normative (la nota sull'art. 71), Vendita e noleggio (link esterno a cami2.it).
  - Contatti: telefono, fax, email, indirizzo con mappa.
- **Social**: nessuno. Unicar non ha profili (ricerca del 24/10/2026). Cami2 ha Facebook, Instagram e YouTube, ma sono di Cami2: non vanno nel piede di Unicar, al massimo un link "Gruppo Cami2".
- **Newsletter**: non ce l'hanno e non ha senso. Lavorano solo per aziende, le notizie sono due del 2012, non vanno a fiere e non hanno cataloghi né clienti privati. Al suo posto, il promemoria dei controlli della direzione A.
- **Riga legale**: "Unicar srl, via Canada 12, 35127 Padova, P.IVA e C.F. 01014160285, REA PD 170490, capitale sociale 100.000,00 euro", più Privacy e Cookie. L'informativa va riscritta per il GDPR. La PEC non è pubblica.

## 9. Da confermare

- **Prima di tutto**: Unicar esiste ancora come società a sé? Il VIES dà la P.IVA non attiva, Cami2 è del Gruppo Selini dal novembre 2024 e il furgone del service porta la livrea Cami2. Se Unicar è stata fusa in Cami2, la proposta va rivolta a Cami2 o lasciata cadere.
- L'anno di costituzione (la mia stima è intorno al 1982) e chi sono i soci e il titolare.
- Quanti furgoni e quanti tecnici ha oggi Unicar da sola (12 mezzi nel 2012; 25 tecnici esterni per tutto il gruppo).
- Se "entro 24 ore" vale ancora e su quale zona (Padova e provincia? anche Venezia?).
- Se sono ancora "assistenza autorizzata" BT e Cesab, cioè Toyota Material Handling Italia.
- Le certificazioni: quelle citate (ISO 9001, A.S.E.C., OHSAS) sono di Cami2; servono quelle di Unicar, se ci sono.
- PEC, orari di apertura dell'officina, un eventuale numero per le emergenze.
- Se fanno ancora i corsi per carrellisti (la notizia è del 2012) e con quale ente.
- I diritti delle foto della Gallery (BT e Cesab) e la provenienza dei banner con gli occhi.
- Il logo vettoriale originale, e se la C rossa a doppio anello si può ridisegnare piatta.
- Se nel sito nuovo la vendita e il noleggio devono restare un rimando a cami2.it.
- Le foto da rifare dal vero: la sede con i furgoni, un tecnico al lavoro, il magazzino ricambi, un carrello revisionato.
