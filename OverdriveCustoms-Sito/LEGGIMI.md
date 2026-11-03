# Overdrive Customs: proposta di nuova home

Proposta non richiesta di nuova homepage per Overdrive Customs, officina moto di Matteo a Vigonovo (VE). Solo la home. Nessun contatto con l'azienda, nulla pubblicato.

## Cosa c'è
- `sito/index.html`: la home, livello professionale con il ritocco finale del 3/11/2026 (apertura nera con la foto dell'officina a tutta larghezza, tre racconti delle special, fascia delle riviste; HTML, CSS e un piccolo script in un file: stato di oggi, menu del telefono, modulo). Si apre direttamente nel browser.
- `sito/img/`: solo foto dell'azienda, in WebP a più larghezze.
- `sito/fonts/`: Archivo variabile (woff2 latin e latin-ext) con la licenza `OFL-Archivo.txt`.
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg, selettore-1440.jpg (ora la sezione "Le special"), prime schermate a 320, 768, 1024, 1920, menu-390.jpg; `NOTA.md` con l'esito delle 15 regole, le prove d'uso e la storia della versione di prima.
- `_prova/script/build_finale.sh`: rifà tutto (`--immagini` per rifare anche le immagini). Script: `pro_img.py`, `pro_pagina.py` con il modello `pro_pagina.tpl.html`, `pro_shot.mjs`, `pro_jpg.py`, `pro_controlli.mjs` (esito in `_prova/pro-controlli.json`), `ritocco_misure.mjs` (posizioni a 390 e 1440).
- `_prova/pro-controllo/`: gli screenshot del controllo fatto prima del ritocco (la versione con il titolo a sinistra e la foto a destra).
- `_prova/versione-1-originale/`: la home di prima (Hagane scontornata, selettore), con screenshot e il LEGGIMI di allora; i suoi script sono ancora in `_prova/script/` (`finale_*`).
- `_prova/uso/SCHEDA.md`: chi apre il sito e per fare cosa; `01-analisi.md`: i fatti con le fonti (sezione 10 aggiunta per questa versione).

## Il modulo va collegato
Il modulo "Preferisci l'email?" in "Orari e dove" oggi non invia nulla da solo: compone un'email (`mailto:overdrivecustoms@live.com`, oggetto "tipo di richiesta, nome", nel testo tipo, nome, telefono, email, moto e messaggio) che il visitatore manda dal suo programma di posta. Nel sito vero va collegato a un servizio (il modulo della piattaforma Aruba che usano oggi, oppure Formspree, Netlify Forms o simili) con l'informativa privacy e la casella del consenso. Il canale che Matteo chiede resta WhatsApp: tutti i bottoni principali aprono `wa.me/393402510434` con un messaggio già scritto per quel caso (generico "ti scrivo per la mia moto" in testata e in apertura, tagliando, riparazione, restauro, ritiro, trasformazione per famiglia, foto della moto).

## Cosa chiedere a Matteo (non è in pagina, o lo è in forma prudente)
- **Ragione sociale, P.IVA, REA, PEC** e cognome: non sono pubblici. Vanno nell'ultima riga del piede (oggi c'è solo "© Overdrive Customs, Vigonovo (VE)"). Senza la P.IVA il piede non passa la regola 15.
- **Orari**: martedì-venerdì 9:30-13 e 15:30-19, solo su appuntamento (sito e post del 2020): sono ancora così? Nei festivi (fissi e Pasquetta) la pagina ora scrive "Oggi chiuso per festa, riapre ... alle 9:30": confermare che nei festivi l'officina è chiusa, e se chiude per ferie (agosto, Natale) per aggiungere le date.
- **WhatsApp** sullo stesso numero 340 251 0434 (il sito dice "WhatsApp 3402510434"): confermare.
- **Ritiro col furgone**: in quale zona, con quale preavviso, se si paga a parte. In pagina c'è solo "Ritiro e consegna della moto col furgone dell'officina. Scrivimi dove sei".
- **Come si comincia una trasformazione**: la pagina dice "mandami una foto della moto e l'idea su WhatsApp, poi ne parliamo in officina, su appuntamento; si può andare da un kit fino al telaio fatto qui". Matteo lavora così? Si può aggiungere "il preventivo si fa dopo aver visto la moto" (dalla scheda, non confermato, quindi non in pagina) e, se vuole, tempi indicativi.
- **Sportster 48 "Jericho"** (post del 08/01/2021, ora nella scheda Sportster): il post dice solo il nome. Che cosa è stato fatto (sella, scarichi, serbatoio, ruote)? Con 3-4 lavori la scheda diventa come quella dell'Electra Glide. Lo stesso per la Heritage bobber del 2020: la scheda oggi cita i lavori di altri post su altre Heritage e su una Dyna.
- **Le trasformazioni in pagina**: confermare che si possono mostrare queste moto di clienti (Softail Springer in manutenzione, Sportster dopo la caduta, Road King restaurata, Heritage bobber, Electra Glide diventata Road King) e che la 883 chopper, la Heritage bobber e la Sportster del ripristino sono lavori loro come dicono i post. Se i clienti sono d'accordo, il nome del cliente e il comune renderebbero le schede più forti (regola 11).
- **Recensioni**: non ne ho trovate di leggibili (Paginegialle e Cylex 403, Facebook senza login). Se Matteo ha una scheda Google con recensioni, tre recensioni vere con nome, comune e stelle vanno in "Chi c'è dietro", sotto i numeri: con quelle la regola 10 passa (oggi ci sono 2 tipi di prova su 4: numeri e fornitori; riviste, copertine e premi non contano tra i 4 tipi). Anche due o tre clienti con il nome (con il loro permesso) vanno bene.
- **Premi**: "La Morelia, King of metric cat." all'American Dream 2022 è un primo posto? Il primo posto "freestyle" di Hagane del 21/04/2025, in quale evento? Oggi l'albo conta 8 primi posti dal 2018 al 2024 senza questi due.
- **Fiere 2027**: date e numero dello stand di Motor Bike Expo, Biker Fest e American Dream, per una riga "Ci vediamo a..." nella sezione delle fiere.
- **Accessori, oli, cappellini**: lo shop online dei cappellini citato nel 2023 esiste ancora? Kustomstore va tenuto in "Lavoro con"?
- **Facebook** (https://www.facebook.com/p/Overdrive-Customs-100063689226764/): è loro ed è attivo? Oggi nel piede c'è solo Instagram.
- **La sede di via IV Novembre 3 e il numero 342 761 3224** (2015): chiusi? Non sono in pagina.
- Il cognome "Massaro" compare solo in un articolo di autoevolution: non è in pagina.

## Foto: permessi e cosa rifare dal vero
Tutte le foto in pagina sono dell'azienda (sito e Instagram), alcune di fotografi terzi citati nelle didascalie; le copertine sono delle riviste. Nessuna foto di repertorio, nessuna illustrazione. Prima di pubblicare:
- **Permessi e originali**: autore della copertina del sito (Matteo in officina, 2560x1440, l'apertura); @boemphoto (883 con Matteo, Special K); @luciodebiase (ritratto di Matteo in bianco e nero, 703 px); autore della foto di Hagane nel campo (post del 22/05/2024); Kustom World e Bigtwin per le copertine.
- **Una mezza giornata di foto, la cosa più utile**: le schede sono già quasi una serie (moto di fianco davanti al portone di lamiera del capannone), ma sono file Instagram da 1080 px con HDR e colori spinti. Da rifare con lo stesso schema, una sola luce:
  - sei-otto moto di clienti e loro, esattamente di fianco, ruota davanti a destra, davanti al portone grigio, a metà mattina con cielo coperto o all'ombra (niente sole diretto sulle cromature);
  - fotocamera all'altezza dei mozzi (circa 50 cm), 50-85 mm da 5-6 m, treppiede, RAW, almeno 4000 px di lato lungo; inquadratura 16:9 con 10 % d'aria intorno alla moto, così il taglio delle schede non mangia le ruote (oggi Restauro e Ripristino sono un po' strette);
  - per famiglia: una Sportster, una Softail o Dyna, una Touring, una giapponese, più una moto sul ponte in manutenzione e una in ripristino;
  - **mancano del tutto**: Matteo al lavoro (mani su un motore, cambio gomme alla macchina), il **furgone** col logo davanti all'officina (prova del ritiro: oggi c'è solo la copertina di un video da 640 px), la **facciata** con l'insegna e il numero civico (per chi arriva: andrebbe nella scheda "Orari e dove"), il banco con accessori, oli e cappellini.
- **Apertura**: la copertina del sito regge; per schermi grandi e retina servirebbe l'originale di almeno 3000 px. Se si rifà, stessa luce del capannone, Matteo non a filo del bordo destro, un po' d'aria sopra la testa per il taglio 3:2 del telefono.
- La 883 e Special K vengono da un servizio in studio su fondo bianco (file da 704 e 720 px), ora vicine tra le special: la 883 è mostrata a 737 px a 1440, un filo più del file. Con gli originali di @boemphoto reggono anche più grandi.
- La serie non è ancora una sola luce (regola 5): Hagane è nel campo al sole di mezzogiorno, il ritratto di Matteo è in bianco e nero, le schede sono davanti alla lamiera. Con la mezza giornata di foto qui sopra (stessa luce coperta, stesso portone, stessa altezza) e Hagane rifatta davanti al portone, la regola passa.

## Caratteri, licenze, loghi
- Archivo, Omnibus-Type, da Google Fonts, SIL Open Font License 1.1: uso commerciale libero, servito dalla pagina (`sito/fonts/`), licenza in `sito/fonts/OFL-Archivo.txt`.
- Logo: `assets/originali/logo-customs-ricostruito.svg`, ricostruito dal post del 01/09/2018, fedele; inline nella pagina (nero in testata, bianco nel piede). Va sostituito con il file vettoriale originale se Matteo lo ha. Favicon da fare dal logo vero.
- I segnaposto Unsplash in `assets/esterne/` (licenza in `assets/CREDITI.md`) non sono usati in pagina.

## Pagine che il sito nuovo avrà
Oggi i link della home portano alle sezioni. Nel sito vero: `/officina`, `/trasformazioni` (una pagina per famiglia, con più casi), `/moto/hagane` e le altre special, `/contatti`, `/privacy` e `/cookie` (oggi 404 anche sul sito attuale: vanno scritte; nella proposta aperta da file i link Privacy e Cookie del piede non si aprono).

## Controlli fatti
- 15 regole della sezione C con `pro_controlli.mjs` e a vista: 12 passano; non passano la 5 (luce delle foto: serve il servizio fotografico), la 10 (recensioni o clienti con il nome) e la 15 (ragione sociale e P.IVA). Tutte e tre aspettano materiale dall'azienda. Dettaglio in `screenshot/home/NOTA.md`.
- Prove d'uso della scheda: stato di oggi a 9 date e ore, posizioni a 390x844 (le quattro famiglie di trasformazioni entro tre scorrimenti: 2474-3294 px), link WhatsApp, telefono, mappa, email.
- Nessuno scorrimento orizzontale da 320 a 2560 px; screenshot guardati a pezzi a 1440 e 390, prime schermate a 320, 768 e 1024.
- Nessun U+2014 nei file consegnati.
