# AIT Studio, Stefano Aiti: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata, e l'azienda non è stata contattata.

## Dove sono le cose

- `sito/index.html`: la home, **metodo ibrido** (3/11/2026): prima schermata secondo la sezione D, sotto i contenuti della versione professionale su una griglia sola. Statica, si apre con file:///, con `sito/img/` (WebP) e `sito/fonts/` (con le licenze).
- `screenshot/home/`:
  - home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, home-1024-prima-schermata.jpg, home-768-prima-schermata.jpg, chiusura-1440.jpg (dal preventivo al piede);
  - NOTA.md: in testa il metodo ibrido (cambi, misure, compiti, problemi aperti), sotto la nota della versione professionale.
- `_prova/versione-pro/`: la home professionale com'era prima del metodo ibrido (sito e screenshot).
- `_prova/alto/`:
  - `DIREZIONE.md`: idea, gesto, modello, registro, foto scelte;
  - `provini.jpg`: i provini delle 185 foto originali;
  - `misura-d.mjs` (soglie D e ibride) e `controlli.mjs` (larghezze 320-1920, collegamenti, compiti, screenshot); risultati in `misure/`, la versione pro misurata in `misure-pro/`;
  - `script/immagini.py` rifà le WebP da `assets/originali/`; `script/concorrenti.mjs` le prime schermate di Hufton + Crow e Iwan Baan in `concorrenti/`.
- `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa viene a fare.
- `01-analisi.md`: i fatti con le fonti.
- `assets/originali/` era stata cancellata con un riavvio: il 3/11/2026 ho riscaricato dai due siti dello studio 31 foto in `aitistudio/` (cantieri, mezzi, studio, con EXIF) e 154 in `portfolio/` (Calearo, Calegaro, Marijke, Superoro, Studio 4 Marmicolor, Fornace Morandi, Banca Prealpi). Il logo tracciato, gli altri portfolio e l'inventario non ci sono più; i due SVG del logo restano in `sito/img/`.

## Il modulo del preventivo va collegato

- Oggi "Prepara l'email" apre la posta di chi scrive, con un messaggio già composto:
  - indirizzo info@aitistudio.it se il lavoro scelto è di cantiere (reportage, foto aziendali, livree, video e siti), stefano@stefanoaiti.com per gli altri; sotto il bottone è scritto a quale indirizzo parte;
  - oggetto "Richiesta di preventivo: tipo di lavoro, azienda";
  - nel testo nome, azienda, telefono, email, cosa fotografare, dove, entro quando, per quale uso e messaggio.
- Prima della messa online va collegato a un servizio di invio, per esempio il modulo del sito o un servizio di moduli. Quando c'è il servizio:
  - il primo campo da aggiungere è **"Allega planimetrie, logo, foto dei mezzi (PDF, JPG, DWG)"**: la regola 14 lo chiede per la famiglia M e con il mailto non si può fare (in pagina c'è solo la frase "si allegano lì", in nero a 16 px);
  - poi la casella del consenso privacy;
  - va scelto a quale indirizzo arrivano le richieste: stefano@stefanoaiti.com o info@aitistudio.it.
- Le schede dei servizi di cantiere portano al modulo con il tipo di lavoro già scelto. Altrimenti la tendina parte da "Scegli il tipo di lavoro", vuota, così chi chiede uno still life non manda per sbaglio una richiesta di cantiere.

## Da chiedere all'azienda prima di mandarla

- **Identità e dominio.**
  - Quale dominio resta (stefanoaiti.com o aitistudio.it).
  - Il marchio: "AIT Studio", "Aiti Studio" o "Stefano Aiti Fotografo". In pagina ci sono il logo AIT STUDIO, "Stefano Aiti" e "AIT Studio, Mestrino".
- **Matrimoni.**
  - Se vuole la voce "Matrimoni" in home: oggi è una sezione corta dopo il preventivo, con il voto, le 9 recensioni, il prezzo da 1.000 euro, "Chiama per la data" e i link a Weddgraphy e Matrimonio.com; è nel menu del telefono e nel piede.
  - Le tre frasi di Ornella, Elena e Melissa sono **tolte** dalla home: erano state lette con uno strumento di sintesi (curl riceve 403) e vanno ricontrollate parola per parola sulla scheda prima di rimetterle.
- **Recensioni delle aziende.** Non ne abbiamo trovate né su Google né altrove. Se qualche impresa o azienda gli ha scritto, una o due frasi con nome e comune vanno accanto ai clienti.
- **Data, ora e tempo di posa dei lavori.** Sotto ogni foto di cantiere la home scrive data, ora e tempo di posa dello scatto, letti nell'EXIF dei file pubblicati su aitistudio.it (è il gesto della pagina, "la riga dello scatto"). Vanno confermati con Stefano, anche l'orologio della fotocamera:
  - Salima a Mirano: 18 marzo 2023, ore 19:19, posa 1,3 s (`Aiti-Salima_CAV_Mirano-93820-1.jpg`, Nikon Z 9), in apertura;
  - Salima a Padova, fresatura notturna: 18 maggio 2024, ore 0:09, posa 1/60 s (`Studio-Aiti-Video-Storytelling-Salima-Cantiere-Giro-Italia.jpg`), il culmine. Il luogo viene dal titolo del video di cui è la copertina su aitistudio.it/video-storytelling: "Padova - Asfaltatura vie urbane per il passaggio del 107esimo Giro d'Italia";
  - Salima, A4 Verona Sud: 30 settembre 2023, ore 19:19, posa 1/100 s (`Studio-Aiti-Video-Storytelling-Salima-Cantiere-VR-Sud.jpg`). Il luogo viene dal titolo del video: "A4 Verona Sud - Manutenzione straordinaria (corsia di emergenza e prima corsia)";
  - Salima, foto aziendale: 13 dicembre 2021, ore 13:06, posa 1/1600 s (`Studio-Aiti-Fotografia-Aziendale-3.jpg`). Il luogo (un piazzale con gli inerti) non è scritto: va chiesto, e il nome dell'operaio va chiesto solo se vuole comparire.
  - Girardini a Carpane e Salima a Massenza sono uscite dalla home (novembre 2026, ritocco dopo il giudice): erano mezzi in posa, senza persone.

  Restano da chiedere gli anni di Banca Prealpi (Artufficio), della scala di Studio 4 Marmicolor e della Fornace Morandi: i file del portfolio non hanno EXIF. Per ora sotto c'è la categoria (contract, interni, architettura).
- **Clienti che si possono nominare e diritti d'uso delle foto.**
  - In pagina: Salima, Girardini, Martini Silvestro, Calearo, Calegaro, Marijke, Superoro, Pianegonda, Luceplan, Bellissima Vodka, Trek, Goppion Caffè, Saip, Artufficio (con Banca Prealpi e Credito Cooperativo di Brendola), Lago, Studio 4 Marmicolor e Fornace Morandi (il cliente è Bruno Stocco?).
  - "Anas" non è più citato: la foto di Girardini a Carpane è uscita dalla home.
  - Le foto di cantiere mostrano mezzi e marchi di Salima, Martini Silvestro e Volvo.
- **Didascalie da confermare.**
  - "Salima, Mirano (VE)": il file si chiama "CAV Mirano" (CAV è il committente dell'opera?).
  - "Salima, Padova" e "Salima, A4 Verona Sud": dai titoli dei video su aitistudio.it.
  - "Artufficio, Banca Prealpi", "Studio 4 Marmicolor", "Fornace Morandi" (il cliente è Bruno Stocco?).
  - Sotto gli still life: Calearo (antenna per auto), Marijke (vaso), Calegaro (ciotole smaltate), Superoro (anello, `Superoro-5.jpg`). I quattro fondi sono portati allo stesso grigio chiarissimo (245,245,244) e gli oggetti alla stessa scala: va chiesto se a Stefano va bene, o se preferisce i suoi bianchi.
- **Frasi di servizio da confermare.**
  - "Fotografiamo il cantiere quando lavora, anche di notte" è **tolta** dalla pagina finché Stefano non la conferma: la notte la dicono le ore sotto le foto (0:09 a Padova). Va chiesto se è un servizio che offrono sempre.
  - "I cantieri di queste foto sono in Veneto": è un fatto sulle foto (Mirano, Padova, Verona Sud), non un elenco di zone. Va chiesto l'elenco vero delle zone, con il raggio che fanno.
  - I tempi di risposta al preventivo non sono scritti: vanno chiesti.
  - I prodotti si portano in sala di posa a Mestrino o vanno fotografati in azienda? La pagina dice solo "Prodotti in sala di posa", come la scheda.
- **Orari e appuntamenti.** Non sono nelle fonti: lo studio riceve su appuntamento? Se sì, va scritto nel piede e nei contatti.
- **Numeri.** La fascia delle cifre è tolta. In pagina restano, dentro le frasi: 1995 e 2008 (sa.com/about), "siamo in due" (ais.it/contatti), "le sei banche e casse rurali arredate da Artufficio" (portfolio di sa.com). Servono numeri più forti, da chiedere: quanti cantieri documentati, quante imprese, quanti mezzi con la livrea, da quanti anni con Salima.
- **Certificazioni e associazioni.** È ancora socio TAU Visual? Se sì, il marchio va nel piede con la didascalia.
- **Recapiti.**
  - Se info@aitistudio.it resta.
  - Oggi i contatti sono divisi per bisogno: cantieri e imprese a info@aitistudio.it (anche nel menu del telefono), prodotti e architettura a stefano@stefanoaiti.com. Va deciso se è la divisione giusta. In testata non c'è più "Scrivici": c'è "Preventivo".
  - Il telefono di Giulia Morandin non è in pagina: su aitistudio.it ha una cifra di troppo, e serve il suo consenso.
- **Ragione sociale nel piede.** "Stefano Aiti Fotografo, ditta individuale" va confermata. La P.IVA e la PEC vengono dal piede di stefanoaiti.com. Il codice fiscale personale non è ripetuto.
- **Pagine da fare**: `privacy/` e `cookie/`, linkate nel piede.

## Foto da chiedere o rifare dal vero

Il materiale è suo e buono, ma i file web sono piccoli: 1900-2000 px, alcuni a 1200.

- **Gli originali ad alta risoluzione**, almeno 2400 px sul lato lungo. Servono per:
  - l'apertura (Salima a Mirano) e il culmine (la fresatura notturna a Padova);
  - la sala di posa;
  - Verona Sud, la foto aziendale e Banca Prealpi.

  Basta metterli al posto dei file in `assets/originali/` e rilanciare `python3 -I _prova/alto/script/immagini.py`, aggiungendo le larghezze 2400 e 3200 nella lista.
- **Mirano in apertura e Padova nel culmine** sono le due immagini più grandi della pagina (1360 px a 1440, 1840 a 1920): i file sono a 1900 px, quindi sugli schermi ad alta densità sono un po' morbide. Per queste due servono gli originali da almeno 3200 px.
- **Superoro, Marijke e Calegaro** sono a 1200 px: bastano per la fila dei prodotti, ma vanno chiesti gli originali.
- **Una foto di un sito web fatto da loro, vista su un telefono o uno schermo vero** (non un mockup). Servirebbe per dare ai siti una scheda propria: oggi stanno con i video.
- **La sala di posa a colori e orizzontale**, con un prodotto sul banco. Quella in pagina (`a4`) è vera e va bene, ma è in bianco e nero, e un'immagine di un lavoro in corso direbbe di più.
- **Stefano in cantiere, al lavoro con la fotocamera**, possibilmente di notte su una stesa: è la foto che manca per l'impresa.
- **Architettura più recente del 2017**, se c'è.

## Licenze

- **Caratteri**: Albert Sans 400 e 500 (The Albert Sans Project Authors) e Spline Sans Mono 400 (solo per data, ora e numeri dei servizi), entrambi SIL Open Font License 1.1, uso commerciale gratuito. I woff2 (sottoinsieme latino) vengono da @fontsource 5.1.0 su jsDelivr, scaricati il 3/11/2026, e stanno in `sito/fonts/` con le licenze `OFL-albert-sans.txt` e `OFL-spline-sans-mono.txt`. Switzer non è più usato (resta in `assets/fonts-scaricati/` e in `_prova/versione-pro/`).
- **Foto**: tutte di Stefano Aiti o di AIT Studio (vedi `assets/CREDITI.md`). Nessuna foto di repertorio: i segnaposto Pexels in `assets/esterne/` non sono usati.

## Loghi

- In testata c'è `sito/img/logo-ait.svg`, il solo segno AIT senza la riga STUDIO, accanto a "Stefano Aiti" (non è un link: la pagina è una sola).
- Nel piede, sul nero, c'è `sito/img/logo-ait-studio-bianco.svg`: il logo completo tracciato (`assets/originali/logo-ait-studio-tracciato.svg`), con il nero passato al bianco e il grigio #AAAEAD lasciato com'è.
- Non ho trovato un vettoriale ufficiale: va chiesto lo SVG o l'AI originale, anche nella versione per fondo scuro.
