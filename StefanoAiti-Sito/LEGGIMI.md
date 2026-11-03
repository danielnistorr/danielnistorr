# AIT Studio, Stefano Aiti: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata, e l'azienda non è stata contattata.

## Dove sono le cose

- `sito/index.html`: la home, al livello professionale (statica, si apre con file:///), con `sito/img/` e `sito/fonts/`.
- `screenshot/home/`:
  - home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg;
  - chiusura-1440.jpg va dal preventivo al piede;
  - NOTA.md, con le scelte, l'esito delle 15 regole e i controlli.
- `_prova/versione-1-originale/`: la home di prima ("Comunicazione silenziosa"), con sito, screenshot e NOTA, com'era prima di questo passaggio.
- `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa viene a fare.
- `_prova/script/`:
  - `build_finale.sh --immagini` rifà immagini, caratteri, screenshot e controlli;
  - `pro_img.py`, `pro_shoot.mjs`, `pro_controlli.mjs`, `pro_uso.mjs`, `trova_largo.mjs`.
- `_prova/crawl/matrimonio/recensioni.md`: le recensioni di Matrimonio.com lette il 3/11/2026.
- `01-analisi.md`: i fatti con le fonti.

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
  - Se vuole la voce "Matrimoni" in home: c'è nella prima schermata (una riga), nel menu e in una sezione dopo il preventivo, con il voto, il prezzo da 1.000 euro e tre recensioni. È stata spostata in fondo perché, tra i clienti e il preventivo, interrompeva chi viene per lavoro.
  - Le tre frasi di Ornella, Elena e Melissa sono state lette con uno strumento di sintesi (curl riceve 403): vanno ricontrollate parola per parola sulla scheda prima di pubblicarle.
  - Il comune degli sposi non c'è nella fonte; va aggiunto, se lo vogliono.
- **Recensioni delle aziende.** Non ne abbiamo trovate né su Google né altrove. Se qualche impresa o azienda gli ha scritto, una o due frasi con nome e comune vanno accanto ai clienti.
- **Anno dei lavori.** Per i tre lavori di cantiere mese e anno vengono dall'EXIF dei file originali (data di scatto), da confermare con Stefano:
  - Salima a Mirano: 18/03/2023, ore 19:19 (`Aiti-Salima_CAV_Mirano-93820-1.jpg`). È di sera, non all'alba: la didascalia "all'alba" della prima stesura è tolta;
  - Girardini, cantiere Anas a Carpane: 10/10/2022 (`Aiti-Girardini-Anas-Carpane-89448.jpg`);
  - Salima a Massenza: 11/03/2022 (`Aiti-Salima-Volvo_FL250-Massenza-99134.jpg`);
  - la stesa della porta Cantieri: 18/05/2024, ore 0:09 (non scritto in pagina).

  Il materiale di cantiere va quindi dal 2022 al 2024 secondo l'EXIF (non 2024-2025, come scritto prima: quelle sono le date delle pagine di aitistudio.it). Restano da chiedere gli anni di Banca Prealpi (Artufficio), della scala di Studio 4 Marmicolor e della Fornace Morandi: il portfolio è caricato nel 2017 e i file non hanno EXIF.
- **Clienti che si possono nominare e diritti d'uso delle foto.**
  - In pagina: Salima, Girardini, Martini Silvestro, Calearo, Calegaro, Marijke, Superoro, Pianegonda, Luceplan, Bellissima Vodka, Trek, Goppion Caffè, Saip, Artufficio (con Banca Prealpi e Credito Cooperativo di Brendola), Lago, Studio 4 Marmicolor e Fornace Morandi (il cliente è Bruno Stocco?).
  - "Anas" è citato solo come cantiere di Girardini a Carpane.
  - Le foto di cantiere mostrano mezzi e marchi di Salima, Martini Silvestro e Volvo.
- **Didascalie da confermare.**
  - "Salima, Mirano (VE) · marzo 2023 · reportage di cantiere": il file si chiama "CAV Mirano" (CAV è il committente dell'opera?).
  - "Salima, Massenza (TN) · marzo 2022 · parco mezzi, Volvo FL250": dal nome del file.
  - "Girardini, Carpane (VI) · ottobre 2022 · cantiere Anas, reportage": il committente del cantiere di Carpane va verificato; nel dubbio si scrive "Cantiere Anas a Carpane (VI), reportage" senza Girardini.
  - "Artufficio, Banca Prealpi".
  - Sotto gli still life e sotto la scala e la Fornace c'è solo il nome del cliente: Calearo, Marijke, Calegaro, Superoro, Studio 4 Marmicolor, Fornace Morandi.
- **La foto della porta Cantieri** (stesa notturna con il semirimorchio Salima): il file dice "cantiere Giro Italia". Il luogo non è scritto in pagina: la scheda ipotizza Santa Giustina, non il Santo, e va verificato.
- **Frasi di servizio da confermare.**
  - "Veniamo in cantiere anche di notte": si basa sulle foto notturne pubblicate su aitistudio.it.
  - "In Veneto e in Trentino: Padova, Mirano, Carpane, Massenza": sono i luoghi dei file, non un elenco dichiarato. Va chiesto l'elenco vero delle zone, con il raggio che fanno.
  - "Vi rispondiamo con un preventivo": va chiesto in quanto tempo rispondono, per scriverlo.
  - I prodotti si portano in sala di posa a Mestrino o vanno fotografati in azienda? La pagina dice solo "Prodotti in sala di posa", come la scheda.
- **Orari e appuntamenti.** Non sono nelle fonti: lo studio riceve su appuntamento? Se sì, va scritto nel piede e nei contatti.
- **Numeri.** I quattro in pagina vengono dalle fonti: 1995, 2008, 2 persone (ais.it/contatti e ais.it/studio) e 6 banche e casse rurali arredate da Artufficio (portfolio di sa.com). Le 2 lauree Iuav ora sono scritte nel testo dello studio. Servono numeri più forti, da chiedere: quanti cantieri documentati, quante imprese, quanti mezzi con la livrea, da quanti anni con Salima, quanti prodotti fotografati in un anno.
- **Certificazioni e associazioni.** È ancora socio TAU Visual? Se sì, il marchio va nel piede con la didascalia.
- **Recapiti.**
  - Se info@aitistudio.it resta.
  - Il menu manda le email a info@aitistudio.it ("Scrivici a info@aitistudio.it", sul telefono) e la testata a 1440 a stefano@stefanoaiti.com ("Scrivici"): va deciso quale casella resta e per che cosa.
  - Il telefono di Giulia Morandin non è in pagina: su aitistudio.it ha una cifra di troppo, e serve il suo consenso.
- **Ragione sociale nel piede.** "Stefano Aiti Fotografo, ditta individuale" va confermata. La P.IVA e la PEC vengono dal piede di stefanoaiti.com. Il codice fiscale personale non è ripetuto.
- **Pagine da fare**: `privacy/` e `cookie/`, linkate nel piede.

## Foto da chiedere o rifare dal vero

Il materiale è suo e buono, ma i file web sono piccoli: 1900-2000 px, alcuni a 1200.

- **Gli originali ad alta risoluzione**, almeno 2400 px sul lato lungo. Servono per:
  - le tre porte d'apertura (stesa Salima, antenna Calearo, scala Marmicolor);
  - la sala di posa;
  - i lavori grandi (Scania a Mirano, Banca Prealpi);
  - le quattro schede di cantiere.

  Basta metterli al posto dei file in `assets/originali/` e rilanciare `build_finale.sh --immagini`, aggiungendo le larghezze 1600 e 2400 in `pro_img.py`.
- **La fascia di Mirano a tutta larghezza e la porta Cantieri grande** sono le due immagini più grandi della pagina (fino a 1600 px di larghezza a schermo): i file sono a 1900 px, quindi sugli schermi ad alta densità sono un po' morbide. Per queste due servono gli originali da almeno 3200 px.
- **Superoro** è a 1200 px, ritagliato a 1070x803: va chiesto l'originale.
- **Una foto di un sito web fatto da loro, vista su un telefono o uno schermo vero** (non un mockup). Servirebbe per dare ai siti una scheda propria: oggi stanno con i video.
- **La sala di posa a colori e orizzontale**, con un prodotto sul banco. Quella in pagina (`a4`) è vera e va bene, ma è in bianco e nero, e un'immagine di un lavoro in corso direbbe di più.
- **Stefano in cantiere, al lavoro con la fotocamera**, possibilmente di notte su una stesa: è la foto che manca per l'impresa.
- **Architettura più recente del 2017**, se c'è.

## Licenze

- **Caratteri**: Switzer (Indian Type Foundry, da Fontshare), pesi 400 e 700, ITF Free Font License, uso commerciale gratuito. I woff2 sono in `sito/fonts/`; il 700 è stato scaricato da Fontshare il 3/11/2026 (copia in `assets/fonts-scaricati/`).
- **Foto**: tutte di Stefano Aiti o di AIT Studio (vedi `assets/CREDITI.md`). Nessuna foto di repertorio: i segnaposto Pexels in `assets/esterne/` non sono usati.

## Loghi

- In testata c'è `sito/img/logo-ait.svg`, il solo segno AIT senza la riga STUDIO.
- Nel piede, sul nero, c'è `sito/img/logo-ait-studio-bianco.svg`: il logo completo tracciato (`assets/originali/logo-ait-studio-tracciato.svg`), con il nero passato al bianco e il grigio #AAAEAD lasciato com'è.
- Non ho trovato un vettoriale ufficiale: va chiesto lo SVG o l'AI originale, anche nella versione per fondo scuro.
