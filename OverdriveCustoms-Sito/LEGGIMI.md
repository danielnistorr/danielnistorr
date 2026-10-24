# Overdrive Customs: proposta di nuova home

Proposta non richiesta di nuova homepage per Overdrive Customs, officina moto di Matteo a Vigonovo (VE). Solo la home. Nessun contatto con l'azienda, nulla pubblicato.

## Cosa c'è
- `sito/index.html`: la home finale (HTML e CSS in un file, un piccolo script per il selettore delle moto). Si apre direttamente nel browser.
- `sito/img/`: solo le immagini usate, in WebP a più larghezze.
- `sito/fonts/`: Archivo variabile (woff2 latin e latin-ext) con la licenza `OFL-Archivo.txt`.
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg, più le prime schermate a 320, 768, 1024, 1920 e il selettore; `NOTA.md` spiega idea, scelte, controlli e cosa è cambiato dopo il giudizio cieco.
- `_prova/script/build_finale.sh`: rifà tutto (scontorno di Hagane, immagini, pagina, screenshot, controllo dei segnali). Script usati: `finale_taglio.py`, `fit_ruote.py`, `finale_img.py`, `finale_pagina.py` con il modello `finale_pagina.tpl.html`, `finale_shot.mjs`, `finale_prove.mjs` (larghezze, tastiera, tocco, link, risoluzione), `finale_jpg.py`.
- `01-analisi.md`: fatti con le fonti; `_prova/home/a` e `_prova/home/b`: i due prototipi giudicati.

## Pagine che il sito nuovo avrà (link del piede e del menu)
Oggi i link portano alle sezioni della home (Privacy e Cookie puntano già a `/privacy` e `/cookie`, che in locale non esistono). Nel sito vero andranno a:
- `/officina` (tagliandi, riparazioni motori, ripristino sinistrati, pneumatici, trasporto; customizzazioni, motoristica, restauro)
- `/moto` con una pagina per moto: `/moto/hagane`, `/moto/special-k`, `/moto/883-old-style`, `/moto/drakkar`, `/moto/envy` (e, se Matteo vuole, Bonebreaker, Night Train, La Morelia, la Road King ex ElectraGlide con l'elenco delle sei modifiche del post del 09/07/2022)
- `/riviste` (Ferro, Bikers Life, Kustom World, Bigtwin, con le date)
- `/contatti` (con mappa e orari)
- `/privacy` e `/cookie` (oggi rispondono 404 anche sul sito attuale: vanno scritte)

## Newsletter
Nel piede c'è "Fiere e moto nuove": campo email, bottone, casella del consenso privacy; sotto, "Seguici" con Instagram. Ha senso perché l'officina ha fiere fisse ogni anno (Biker Fest di Lignano a maggio, American Dream a Padova in autunno, Motor Bike Expo a Verona a gennaio), presenta lì le moto nuove e ha clienti privati.
- **Non funziona finché non si collega a un servizio** (Brevo, Mailchimp o simile, con doppia conferma dell'iscrizione e registro dei consensi). Oggi il modulo non invia nulla.
- Va tenuta solo se Matteo la scrive davvero due o tre volte l'anno; altrimenti si toglie e resta il rimando a Instagram.
- Serve l'informativa privacy a cui punta la casella del consenso.

## Dati da confermare (non sono a vista in pagina, o lo sono con la fonte indicata)
- Ragione sociale, forma giuridica, P.IVA, REA, PEC e cognome di Matteo: non sono pubblici. Vanno nell'ultima riga del piede (oggi c'è solo nome e indirizzo).
- Orari (martedì-venerdì 9:30-13 e 15:30-19, dal sito) e "solo su appuntamento" (regola scritta nel 2020): sono ancora così?
- WhatsApp sullo stesso numero 340 251 0434 (il sito dice "WhatsApp 3402510434"): confermare.
- Pagina Facebook (https://www.facebook.com/p/Overdrive-Customs-100063689226764/): è loro ed è attiva? Tolta dal piede finché non è confermata (va in "Seguici" accanto a Instagram). Il Pinterest "overdrivecustom" non è verificato e non è in pagina.
- "La Morelia, King of metric cat." all'American Dream 2022: è un primo posto? Tolta dalla riga dei primi posti finché non è confermato; se sì, va rimessa ("Special K e La Morelia 2022").
- Drakkar: si possono citare il kit di Killer Custom e la vernice grigio Carrara (dalle didascalie del 2021)?
- Il 1° posto "freestyle" di Hagane del 21/04/2025: in quale evento (non usato).
- Lo shop online dei cappellini citato nel 2023 e la rivendita Kustomstore: non sono in home; dire se vanno aggiunti.
- La sede di via IV Novembre 3 e il numero 342 761 3224 (2015): chiusi?
- In `01-analisi.md` (sezione 1) c'è scritto "concorsi del Nordest": il Kustom Kulture è a Cesena, in pagina ho scritto "Nord Italia".
- Il titolo "Special, dal telaio in su" è una sintesi del post del 20/06/2024 ("Frame, front fork, etc.. built by us"): Matteo lo sente suo? In alternativa "Telaio e forcella, fatti qui".
- Le legende di Hagane dicono chi ha fatto ogni pezzo (telaio e forcella Overdrive Customs, motore e ruote da una Suzuki DR650, sella Cisco Leather), come nel post: confermare che il telaio sia interamente loro.

## Foto: permessi e cosa rifare dal vero
Tutte le foto in pagina sono dell'azienda (sito e Instagram), molte di fotografi terzi citati nelle didascalie; le copertine sono delle riviste. Prima di pubblicare:
- **permessi e originali ad alta risoluzione** da @boemphoto (Special K, 883 con Matteo), @madnessphotography.nl (Hagane, servizio del 2024-2025); autore della foto di Hagane nel campo (post del 22/05/2024), della Drakkar davanti alla lamiera (post del 16/08/2021, senza firma), della Envy (post del 21/11/2018) e della copertina del sito a 2560 px (Matteo in officina, oggi in chiusura); permesso di Kustom World e Bigtwin per le copertine.
- **Hagane per l'apertura (la più importante)**: oggi è uno scontorno da un file Instagram di 1080 px, fatto a script (`finale_taglio.py`: ellissi vettoriali per gomme e cerchi, raggi veri presi dal pixel originale, bordo levigato, ombre aggiunte). Regge a 860 px ma da vicino si vede il limite. Due strade: l'originale del fotografo, oppure una mezza giornata in studio:
  - moto esattamente di fianco, lato destro con la ruota anteriore verso sinistra come nella foto di oggi, ruote dritte, cavalletto alzato o nascosto;
  - fondo bianco o grigio chiaro senza giunte (fondale di carta da 2,7 m o parete bianca con pavimento chiaro), la moto staccata dal fondo di almeno 2 m;
  - luce morbida: due grandi bank laterali a 45° e un diffusore dall'alto, niente sole diretto; una lastra bianca sotto il motore per aprire i neri senza appiattirli;
  - fotocamera all'altezza dei mozzi (circa 50 cm), obiettivo 85-100 mm equivalente da 6-8 m per non deformare, diaframma f/8-f/11, ISO base, treppiede;
  - almeno 6000 px sul lato lungo, file RAW; uno scatto con tutta la moto e l'ombra a terra, più i dettagli: saldature del telaio, forcella, sella Cisco Leather, serbatoio, motore DR650.
- **Selettore**: Special K, 883, Envy e Drakkar con la stessa luce e la stessa inquadratura di Hagane (3:2, di fianco), così le quattro schede diventano tutte "sul bianco" e sembrano un solo servizio. Oggi sono due coppie (Envy e Drakkar davanti alla lamiera, Special K e 883 in studio); Special K e 883 sono a 720 e 704 px e su schermi retina sono morbide; la foto della Drakkar è allungata in alto di 103 px di lamiera (specchiata dalla foto stessa) per stare nel 3:2: con lo scatto nuovo non serve più.
- **Chiusura**: oggi c'è la copertina del sito (2560x1440), a tutta larghezza. Regge; su schermi retina larghi servirebbe l'originale (almeno 3000 px). Se si rifà, stessa luce del capannone, Matteo non a filo del bordo destro.
- Le copertine delle riviste vanno bene come sono, piccole.

## Caratteri, licenze, loghi
- Archivo, Omnibus-Type, da Google Fonts, SIL Open Font License 1.1: uso commerciale libero, servito dalla pagina (`sito/fonts/`), licenza in `sito/fonts/OFL-Archivo.txt`.
- Nessuna foto di repertorio in questa versione: i segnaposto Unsplash in `assets/esterne/` (licenza in `assets/CREDITI.md`) non sono usati.
- Logo: `assets/originali/logo-customs-ricostruito.svg`, ricostruito dal post del 01/09/2018, controllato a vista: fedele. In pagina è inline (testata in nero, piede in chiaro). Va sostituito con il file vettoriale originale se Matteo lo ha. Il vecchio marchio col teschio (favicon) non è usato.
- Favicon: non messa; da fare dal logo vettoriale originale.

## Controlli fatti
- `_metodo/kit/segnali.sh`: 0 soglie bloccanti, 0 da guardare (foto 36 % dell'area, Archivo 100 %, 0 monospazio, 2 filetti, 0 frecce, 3 misure di H2, date presenti).
- Nessuno scorrimento orizzontale da 320 a 2560 px (18 larghezze); screenshot guardati a pezzi a 1440 e 390, prime schermate a 320, 768, 1024, 1920.
- Selettore e menu provati con tastiera e tocco; link tel, mailto, WhatsApp, mappa e Instagram controllati; nessuna ancora rotta.
- Contrasto AA su tutti i testi (calcolato, valori nella NOTA).
- Nessun U+2014 nei file consegnati.
