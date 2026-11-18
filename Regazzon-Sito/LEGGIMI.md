# F.lli Regazzon Officine Meccaniche: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata pubblicata né inviata all'azienda.

## Cosa c'è

- `sito/index.html`: la home finale, statica, si apre con file:///. Immagini in `sito/img/` (JPEG e WebP in più larghezze), caratteri in `sito/fonts/`.
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg e `NOTA.md` (idea, schermate, caratteri, colori, gesto, foto, controlli).
- `_prova/script/build_finale.sh`: rifà logo, immagini, pagina e screenshot, misura la pagina a otto larghezze (da 320 a 2560) e prova i gesti. Usa `finale_img.py`, `index-finale.html`, `logo_raster.mjs`, `finale_shot.py`, `finale_controlla.mjs`, `finale_prova.mjs` (schede, altezza costante, menu del telefono, fisarmonica).
- Ultima rifinitura: 2 novembre 2026 (apertura sulla copertina della brochure, chiusura con il pezzo intero, correzioni del giudice cieco). Il dettaglio è in `screenshot/home/NOTA.md`.
- `01-analisi.md`: fatti con fonti. I prototipi sono in `_prova/home/a` (scelto) e `_prova/home/b`.

## Dati da confermare con l'azienda (oggi fuori dalla pagina o solo nella forma sicura)

- **Tornitura verticale**: Ø max 2000 o 2100 mm? In pagina c'è solo "da Ø 250 mm, altezza fino a 1500 mm".
- **Rettifica ingranaggi**: Ø max 1200 o 1500 mm? In pagina c'è solo "fino a modulo 25".
- **Alesatura**: altezza 1600 o 2500 mm? In pagina c'è solo "8000 × 3000 mm".
- **Parco macchine di oggi**: le marche in pagina sono quelle del sito (2015). Il catalogo 2012 cita anche Olivetti e CMC.
- **Saldatura**: i patentini citati sul sito (EN 287.1) sono superati dalla EN ISO 9606-1. Sono aggiornati? In pagina c'è solo "saldatori patentati".
- **Anno d'inizio**: la srl è del 1975, ma i testi dicono "cinquant'anni" già nel 2011. In pagina non c'è nessun anno di fondazione e nessun "da oltre 50 anni". Chi sono i fratelli Regazzon e da quando lavorano?
- **Riduttori in piccole serie**: li fanno ancora, con montaggio e collaudo? Sono in pagina perché sono nella pagina Azienda di oggi.
- **Settori**: in pagina ci sono quelli della pagina Azienda. Le otto "Applicazioni" (eolico, navale, ecc.) restano fuori finché non sono confermate. Ci sono clienti o progetti che si possono nominare?
- **Orari d'ufficio**: non sono pubblicati, quindi non sono in pagina.
- **Fax 049 8700189**: è ancora attivo? Non è in pagina.
- **Il pezzo della copertina**: in didascalia è "corona a dentatura interna, con le marcature incise sul fianco". È la lettura della foto, la stessa corona di `dentatura-int-1` sul sito. Che pezzo è, per quale cliente? Le marcature ("19/11", "F1555B", "01917475") si possono mostrare? Modulo e diametro non sono noti e non sono in pagina.
- **Frase sulla qualità**: "Materiali di prima qualità, impianti di livello tecnologico elevato e controlli rigorosi durante le varie fasi di lavorazione" riscrive la frase della pagina Azienda di oggi. Va bene così?
- **Certificato RINA**: il link porta al PDF 2024-2027 del sito attuale (`regazzon.it/assets/Uploads/...`). Nel sito nuovo va spostato nella pagina Download.
- **Lingue**: servono ancora le versioni EN e DE? Chi traduce? I link EN e DE puntano a `en/` e `de/`.

## Pagine del sito nuovo a cui puntano i link

Menu e piede portano a sezioni della home (`#chi`, `#reparti`, `#qualita` sulla sezione "Trasmettiamo qualità" con il certificato, `#contatti`) o a queste pagine, da fare:
- Azienda:
  - `azienda/` (Chi siamo);
  - `qualita/` (Controllo e qualità: Zeiss e ISO 9001);
  - `settori/` (da scrivere: oggi le Applicazioni sono vuote);
  - `download/` (catalogo, brochure, certificato).
- Ingranaggi: `ingranaggi/dentatura/`, `ingranaggi/rettifica/`, `ingranaggi/cremagliere/`, `ingranaggi/riduttori/`.
- Lavorazioni: `lavorazioni/tornitura/`, `lavorazioni/fresatura/`, `lavorazioni/alesatura/`, `lavorazioni/rettifica/`, `lavorazioni/saldatura/`.
- Note legali: `privacy/` (da riscrivere: oggi cita ancora il D.lgs 196/2003), `cookie/`, `dati-legali/`.
- Versioni `en/` e `de/`.

Niente newsletter: è un'officina conto terzi senza novità periodiche, con clienti solo aziendali. Niente colonna social: non ne hanno.

## Foto

Tutte le foto in pagina sono dell'azienda, prese dal sito, dalla brochure e dal catalogo 2012 (servizio di Nicola Verardo e Vanni Dalla Via, concept Global Automation System, Padova). Sei sono state estratte il 2 novembre con pdfimages dai PDF del sito: lì le foto sono intere sotto le fasce grafiche, quindi più alte delle strisce del sito (elenco in `assets/CREDITI.md`). Il limite resta la risoluzione: nessuna supera 1024 px di lato.
- Apertura: la copertina della brochure (1024x709) a 1,134 volte; il resto è il suo fondale prolungato.
- Chiusura: pignone e corona dal catalogo (626x604) alla misura vera; 814 px per gli schermi ad alta densità.
- Le foto di reparto a 1440 sono ingrandite 1,31 volte; la Fig. di Chi siamo è alla misura vera.
- Reggono su schermi normali, non sui retina.

Da fare subito:
1. **Chiedere gli originali del servizio 2012** (al fotografo o all'agenzia) e il permesso di usarli sul web. Con quelli si rifanno le stesse immagini a piena nitidezza, senza cambiare la pagina.
2. **Rifare dal vero**, se gli originali non ci sono:
   - **Apertura**: la macro della copertina rifatta, una corona grande a dentatura interna vista di tre quarti, su fondale grigio a sweep.
     - Luce da studio morbida, più chiara a sinistra: lì sta il titolo.
     - L'arco occupa la metà destra del fotogramma ed esce in alto, in basso e a destra. Davanti ai denti resta il 45 % di fondale libero.
     - Formato 3:2 o più largo, almeno 6000 px di lato, a fuoco su tutti i denti (focus stacking).
   - **Chiusura**: pignone e corona, o un altro pezzo intero, sullo stesso fondale portato al grigio della pagina (#E9EBEC), con aria sopra e il riflesso sul piano.
   - **Reparti**: una foto per reparto nello stesso formato largo (3:1) e nella stessa luce pulita, con il pezzo in lavorazione in primo piano e niente disordine del capannone.
     - Dentatura: il creatore sulla dentatrice.
     - Rettifica: la Niles.
     - Tornitura: il tornio verticale con un pezzo grande.
     - Fresatura e alesatura: la Skoda.
     - Saldatura: le scintille su una ruota.
     - Controllo: la macchina Zeiss con il tastatore su una corona.
   - **Chi siamo**: l'operaio dentro la corona, rifatto in luce pulita e ferma, per dare la scala del pezzo. Oggi la foto è mossa.
   - In più: la facciata dell'officina in Via Lussemburgo, utile per la pagina Contatti.
3. Le testate delle "Applicazioni" del sito di oggi sono repertorio di provenienza ignota: non vanno riusate.

I segnaposto di repertorio in `assets/esterne/` (Unsplash e Pexels, licenze in `assets/CREDITI.md`) non sono usati nella home finale.

## Caratteri e licenze

- **General Sans** (Indian Type Foundry, da Fontshare), pesi 400, 500 e 600, file woff2 in `sito/fonts/`.
  - Licenza ITF Free Font License: uso commerciale consentito, anche sul sito.
  - I file non si possono ridistribuire: niente archivi pubblici con dentro i font.
- Nessun altro carattere, nessuna icona di libreria, nessun servizio esterno caricato dalla pagina. Il link alla mappa apre Google Maps solo al clic.

## Logo

- In pagina c'è il logo vettoriale originale estratto dalla brochure (`assets/originali/logo-regazzon-da-brochure.svg`, tracciati dell'impaginato Illustrator, non ridisegnato), reso in WebP trasparente a 720 px (3x).
- Da chiedere all'azienda:
  - il file vettoriale ufficiale. Il nostro SVG pesa 293 KB per gli 855 tracciati degli ingranaggi; con il file ufficiale si può servire in SVG leggero;
  - se il marchio "50 YEARS" va tolto. Nella proposta non c'è.
