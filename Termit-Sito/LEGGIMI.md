# Termit, proposta di nuova home: leggimi

Proposta non richiesta di nuova homepage per Termit srl (Saonara, PD). Solo la home.

## Cosa c'è

- `sito/index.html`: la home finale, statica, si apre con file:///. Caratteri in `sito/fonts/`, immagini in `sito/img/` (solo quelle usate).
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`, con la coppella da `finale_coppella.py`), pagina (`build_pagina.py` dal modello `finale_modello.html`) e screenshot (`finale_screenshot.mjs`). `finale_prova_ricerca.mjs` prova la ricerca con tastiera e dito; `finale_shot.mjs` fotografa a più larghezze; `finale_controlli.mjs` misura lo scorrimento orizzontale da 320 a 2560 e controlla tel, mailto, mappa e ancore.
- `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni foto. `_prova/home/a` e `b`: i due prototipi.

## Dati da confermare con l'azienda (in pagina solo dove indicato)

- Anno di inizio dell'attività. In pagina c'è il loro titolo "Una storia lunga più di cinquant'anni" (Chi siamo); LinkedIn dice "oltre 55 anni", la srl è iscritta il 03/01/2000. Esisteva una ditta precedente?
- Email da mostrare: in pagina info@termitisolanti.com (piede del sito di oggi); le condizioni di fornitura scrivono info@termit.biz, e termitisolanti.com non risponde in https.
- Macchina da taglio ad acqua: è loro e sta a Saonara? Marca, piano di lavoro, spessori e materiali che taglia. In pagina solo "Pezzi su misura, lavorati in casa" (dal loro "lavorazione interna") e la didascalia delle teste.
- Mezzi propri: quanti camion, con il logo? In pagina "il più delle volte con mezzi propri" e "automezzi lunghi circa 10 metri" (condizioni di fornitura). "Con i nostri camion" non è usato.
- Validità della medaglia EcoVadis bronzo (anno) e adesione a EIIF.
- Grafia del deposito: in pagina "Dörken Delta" (il sito scrive "Dorken").
- Capitale sociale 5.000.000 € (aziende.it): non mostrato, alto per 11 dipendenti.
- Fax 049 644900: non mostrato, è ancora attivo?
- Le schede della ricerca (138 uniche, con spessori, λ ed Euroclasse) vengono dal crawl del 24/10/2026 e dalle schede dei produttori; nel sito vero vanno lette dal catalogo. La scheda FF (filo di ferro) aveva perso uno zero nell'estrazione: corretta in "0,5 e 1,0 mm" come scrive la scheda.
- La coppella dell'apertura: in pagina "Coppella in lana di roccia, in sezione", "Spessori 20-120 mm" e "λ da 0,037 a 0,044 W/mK", "Rivestimento in alluminio retinato". Sono i valori delle coppelle a catalogo nel crawl (K-ROCK ALU e POWER-TEK PS680 20-120 mm, THERMO-TEK PS PRO ALU λ 0,037, ISOCAMINO λ 0,044): confermare che siano a magazzino e quale coppella fotografare. Nessun codice di fornitore è mostrato in apertura.
- Nella ricerca le schede navali (SEA-TEK, POWER-TEK, THERMO-TEK) sono messe nella famiglia Lana di roccia, che è il loro materiale; "Navale" resta come esigenza.
- Tolta dalla chiusura la riga "Nuovo listino dal 28 marzo 2026" (notizia del crawl, non in `01-analisi.md`): il listino resta promesso dalla newsletter del piede.
- Il certificato Ogyre è intestato ad ANICTA: non è citato.
- "Leader", "pioniere", "tra le più importanti realtà nazionali": non usati, mancano i numeri.

## Foto da rifare dal vero (una giornata in azienda)

Tutte le immagini della home sono segnaposto tranne il taglio ad acqua. Pexels e Unsplash non hanno una coppella o un tubo coibentato in sezione su fondo chiaro senza marchi leggibili, né un magazzino di isolanti (ricerche annotate in `assets/CREDITI.md`). L'apertura è un'illustrazione: la fibra è una foto di repertorio (Akyurt, Pexels) avvolta in cerchio, rivestimento e tubo sono disegnati. Priorità 1: le foto 1 e 2.

1. Priorità 1. Apertura, la sezione: un tratto di tubo d'acciaio con la coppella in lana di roccia e il lamierino, tagliato netto a 90 gradi, appoggiato su un piano chiaro (carta grigio caldo, vicina a #F4F3EF). Vista di tre quarti o di fronte, perché si vedano gli anelli: tubo, coppella, nastro, lamierino. Luce morbida da un lato, un pannello bianco dall'altro, ombra corta. Almeno 4000 px sul lato lungo, a fuoco su tutto il taglio (diaframma chiuso o più scatti uniti). Va al posto dell'illustrazione della coppella, con lo stesso fondo #F4F3EF e lo stesso taglio (mezza coppella vista dal piano di taglio, legende sotto). Scattarla anche intera e lunga, per le pagine prodotto.
2. Priorità 1. La macchina da taglio ad acqua in funzione: orizzontale, almeno 2800 px, luce controllata (niente luce mista del capannone), le teste 1, 2, 3 leggibili e un pezzo appena tagliato con il bordo netto. Va al posto della foto da telefono di oggi nella sezione Su misura.
3. Il magazzino: pile di rotoli, pannelli e coppelle, corsia in prospettiva, verticale 4:5 per la chiusura (va al posto di Jochim).
4. Un camion carico vero, con il logo se c'è (quello del sito di oggi è un fotomontaggio).
5. I materiali in sezione, in macro, affiancati su fondo chiaro: lana di roccia, lana di vetro, elastomero, aerogel, calcio silicato, lamierino. Stessa luce e taglio quadrato: vanno sopra le otto famiglie della home (oggi solo testo) e nelle pagine delle famiglie.

## Licenze

- Caratteri: Zalando Sans e Zalando Sans Expanded, SIL Open Font License 1.1, da Google Fonts, serviti dalla pagina (`sito/fonts/OFL.txt`).
- Foto: Pexels "Free" (Akyurt 9893816 per la fibra della coppella, Jochim 36824351 per la chiusura), verificata sulla pagina di ogni foto il 24/10/2026; uso commerciale ammesso, attribuzione non obbligatoria. Dettagli in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- Foto del taglio ad acqua: dal sito Termit (versione 1000x800), da confermare che sia loro.

## Loghi

Il logo esiste solo in raster. In pagina il PNG bianco trasparente del sito (539x85) ricolorato in verde #51B038 per la testata e in grafite #1B1C1E per il piede, a circa 3x della misura mostrata. Serve il vettoriale (chiedere al grafico o a Two Made srl, autori del sito di oggi). Un SVG ridisegnato va confrontato al 400 % con il PNG prima di usarlo.

## Pagine del sito nuovo (link della home e del piede)

- Prodotti: `prodotti/lana-di-roccia/`, `lana-di-vetro/`, `elastomero-espanso/`, `isolanti-nanotecnologici/`, `protezione-al-fuoco/`, `fonoisolanti/`, `rivestimenti/`, `accessori/`, ciascuna con le schede e il PDF del produttore.
- Settori: `settori/industria/` (forni, serbatoi, coibentazioni industriali, impiantistica, fumisteria, insonorizzazione), `settori/edilizia/` (coperture industriali, tetti, sottotetti, controsoffitti, pavimenti, cappotto, pareti, canali d'aria, isolanti acustici), `settori/navale/` (SEA-TEK, POWER-TEK, THERMO-TEK, PYROGEL, FIRE-TEK); i pezzi su misura sono la sezione `#su-misura` della home.
- Azienda: `azienda/` (chi siamo), `azienda/certificazioni/`, `azienda/partner/`, `news/`, `condizioni-di-fornitura/`.
- `privacy/` e `cookie/`: da scrivere (oggi l'informativa sta su un dominio esterno e il piede non ha link Privacy né Cookie).

## Newsletter

"Listino e novità" nel piede: campo email, bottone, casella del consenso con il link all'informativa. Ha senso perché Termit pubblica ogni anno il nuovo listino e notizie di prodotto, e i clienti sono professionisti che riordinano. Non invia nulla: va collegata a un servizio (per esempio Brevo o Mailchimp) con doppia conferma e registro dei consensi; fino ad allora il modulo mostra solo un messaggio.

## Note sui controlli

- `segnali.sh`: tutte le soglie OK tranne l'area foto (26,6 % contro 35 %). Motivo: la coppella ha molta carta attorno, il taglio ad acqua da telefono non va mostrato oltre i 656 px e mancano foto vere dei materiali. Con gli scatti dei punti 1, 2 e 5 l'area supera il 35 %.
- Dettagli della rifinitura e dei controlli in `screenshot/home/NOTA.md`.
