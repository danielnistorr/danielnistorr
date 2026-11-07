# Melsped: analisi per la nuova home

Sito: https://melsped.it (crawl e screenshot del 20/10/2026: home, 7 pagine di menu, 5 notizie, 5 slide, versione inglese). Il sito è una copia statica HTTrack del 31/01/2022 ("Mirrored from www.melsped.it/ by HTTrack Website Copier/3.x [XR&CO'2014], Mon, 31 Jan 2022") servita da Sucuri. Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `melsped.it/it/`. Testi estratti in `_prova/crawl/testi/`.

## 1. In breve

- **Chi**: Melsped Srl, viale Veneto 9, 35020 Saonara (PD), zona industriale. È una casa di spedizioni: organizza il trasporto e fa le pratiche, con un magazzino proprio e con "partners e corrispondenti dislocati in tutti paesi europei" (`servizi`). ATECO 52.26, "Altre attivita' di supporto ai trasporti" (aziende.it).
- **Cosa fa davvero**: groupage camionistico door-to-door in import ed export, "tratte giornaliere e camion completi e dedicati", spedizioni espresse; spedizioni aeree e marittime, anche "groupage su container"; dogana completa ("Inbarchi e sbarchi, operazioni doganali nei porti e negli aeroporti italiani"), Modelli Intrastat; logistica in un magazzino che "supera i 1.400 metri quadri", con ritiro e riconsegna.
- **Dove arriva**: "Germania, Francia, Regno Unito, Belgio, Olanda, Spagna, Austria, Svizzera e gran parte dei paesi dell'Est Europa", con un rapporto "estremamente enfatizzato" con "Ungheria, Bulgaria e Romania" (`servizi/spedizioni-camionistiche`). Aereo e mare "in ogni angolo del mondo industrializzato".
- **Per chi**: aziende che importano ed esportano, anche quelle "che comincia[no] il suo rapporto con l'estero" (`servizi`). Nessun cliente nominato, nessun privato.
- **Da quando e quanti**: "Nata nel 1975" (`azienda/profilo-aziendale`); la srl risulta iscritta il 02/01/1978. Ha 7 dipendenti, un fatturato 2025 di 2.746.194 euro (+5,8%) e un utile di 244.830 euro (aziende.it, dati Registro Imprese).
- **Correzioni alla nota**: Melsped non trasporta "su camion, aereo e nave" con mezzi propri. È uno spedizioniere: organizza la spedizione e la dogana e le affida a "partners e corrispondenti". Il sito non parla di una flotta: dice che "dispone di ampi spazi e mezzi" per ritiro e riconsegna, e in foto si vede un solo mezzo, un furgone Iveco col logo. Il "camion" della slide è un fotomontaggio. Il Joomla è del 2013 ("In 38 anni", `azienda/l-azienda`). Il materiale è povero ma non solo sede e mezzi: c'è anche un planisfero da parete con il logo stampato, e ci sono due ritratti in ufficio.

## 2. Il sito di oggi

**Pagine**: Home; Chi siamo (`azienda`), con L'Azienda e Profilo Aziendale; Servizi, con Camionistici, Aerei & Marittimi, Logistica & Dogana e Web (`servizi/tecnologia-nelle-spedizioni`); News; Contatti. Versione inglese in `/en/`. Le News sono 5 cronache di pallavolo del 2012 della squadra sponsorizzata "Melsped Medoacus". Non ci sono pagine Privacy né Cookie.

**Testi veri essenziali (verbatim)**:
- Testata: "IL PARTNER IDEALE PER I VOSTRI TRASPORTI DAL 1975", "YOUR BEST PARTNER IN SHIPMENTS SINCE 1975".
- Slide: "Simbolo di esperienza ed efficienza nel mercato internazionale.", "una soluzione veloce e sicura per i vostri trasporti", "Un servizio completo di IMPORT & EXPORT che copre ogni vostra singola esigenza.", "Quello che contraddistingue Melsped è la costante attenzione data alle vostre richieste."
- Servizi:
  - "Melsped fornisce consulenze professionali mirate ad ottimizzare il reparto spedizioni nella vostra azienda."
  - "Il pacchetto di servizi comprende ogni singolo aspetto delle spedizioni IMPORT&EXPORT comunitarie e intracomunitarie."
  - "La richiesta del mercato ha portato Melsped a specializzarsi nelle tratte comunicanti con il nord e l'est Europa"
  - "Melsped garantisce il servizio di dogana in ogni maggior snodo commerciale."
  - Le due note in fondo alla pagina spiegano cosa sono il "Groupage" e il "Modulo Intrastat".
- Profilo aziendale:
  - "ABBATTI I CONFINI: LE ESIGENZE DEL CLIENTE AL PRIMO POSTO"
  - "si posiziona ai primi posti tra le aziende private del Nord Est Italia che operano in questo settore"
  - "Tramite l'offerta di servizi espressi, groupage, tratte giornaliere e camion completi e dedicati, nonchè servizi aerei e marittimi"
- Camionistici: "servizi continuativi groupage door-to-door in IMPORT e in EXPORT"; "si estende nei maggiori scali commerciali dell'Est Europa, anche fuori dalla Comunità Europea".
- Marittimi: "prevedendo pure l'assemblaggio di spedizioni in groupage su container".
- Logistica: "Stoccaggio e magazzinaggio sono resi possibili da uno spazio che supera i 1.400 metri quadri", "il servizio veloce e sicuro di ritiro e riconsegna è sempre attivo".
- Web: Melsped "sarà in grado di fornire un servizio di "tracking"". È scritto al futuro: non risulta un tracking attivo (sez. 9).
- Chi siamo: "Il futuro della Melsped è garantito dal nostro staff giovane ed altamente qualificato".
- Contatti: "Il nostro staff è sempre a tua diposizione".
- Sul sito non ci sono certificazioni (AEO, ISO), numeri di spedizioni o mezzi, né orari.

**Tecnologia**:
- Joomla ("generator" Joomla!) con il framework Gantry, il template "theme939" di TemplateMonster, K2 per le slide, il menu Superfish e RokBox.
- Caratteri: Bebas e Angelina in webfont, il resto in Arial.
- Google Maps API v3 con `sensor=false`, oggi senza chiave, quindi la mappa è rotta.
- L'email è nascosta in JavaScript ("Questo indirizzo email è protetto dagli spambots").
- C'è un pixel di tracciamento `script.whoseesyou.com/trasp2.aspx?cliente=MELSPED` e nessun banner cookie.
- Nel piede c'è il logo del fornitore Nova Systems.
- Refusi in pagina: "riposta", "serizio", "prorpria", "Inbarchi", "diposizione", "conttattarci", "Meoacus"; nel titolo della pagina logistica "MLESPED".

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, prima schermata in `home-1440-primo.jpg`, pagina interna in `profilo-1440.jpg`):
- Il contenuto sta in una colonna di 940 px. Il logo JPEG occupa 250x212 a sinistra; a destra c'è lo slogan in Arial grigio grassetto, con "1975" in corsivo.
- Le icone di Facebook, Google+ e Twitter sono a colori e Google+ è chiuso dal 2019.
- La slide è una foto di 660 px appoggiata a sinistra su una fascia nera, con l'altra metà vuota.
- Seguono tre colonne (Melsped, Servizi, Recapiti): nella terza c'è il riquadro grigio "Spiacenti, si è verificato un problema. Google Maps non è stata caricata correttamente", con l'indirizzo sovrapposto.
- Nel piede il logo Nova Systems è più grande del testo legale.
- Le pagine interne sono muri di testo giustificato in Arial piccolo, con titoli maiuscoli.

**Problemi a 390** (`home-390.jpg`, `home-390-primo.jpg`, `servizi-390.jpg`):
- Il logo e lo slogan riempiono tutta la prima schermata. Lo slogan si accavalla su se stesso ("IDEALE" sotto "PER I", "TRASPORTI" sotto "DAL 1975").
- Il menu è sempre aperto, con tutte le sottovoci, e occupa la seconda schermata.
- La slide è ridotta a una striscia. La mappa è rotta, e il logo Nova Systems copre le bandierine.
- La home è alta 2657 px. Non c'è scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Melsped Srl | piede di ogni pagina: "Melsped Srl - Viale Veneto, 9 35020 SAONARA (PD)"; aziende.it/melsped-s-r-l: "Ragione Sociale Melsped Srl", "SOCIETA' A RESPONSABILITA' LIMITATA" |
| P.IVA / CF | IT00606650281 | piede: "P.IVA: IT00606650281"; aziende.it: "Codice Fiscale 00606650281" |
| REA | PD-127485 | aziende.it: "REA PD-127485"; piede: "C.C.I.A.A. 127485 Trib. Padova 11446" |
| Capitale sociale | 110.000,00 euro interamente versato | piede: "Cap Sociale € 110.000,00 I.V." |
| PEC | melsped@pec.it | aziende.it: "PEC melsped@pec.it" (non è sul sito) |
| Codice SDI | T04ZHR3 | aziende.it: "Codice Destinatario SDI T04ZHR3" |
| Indirizzo | viale Veneto 9, 35020 Saonara (PD) | piede; aziende.it: "Viale Veneto 9, 35020 Saonara (PD) · fonte VIES". Coordinate nella mappa del sito: 45.381175, 11.957872 |
| Telefono | +39 049 8791919 | testata: "tel.: +39 049.87.91.919"; `contatti`: "via telefono: :+39 049.87.91.919" |
| Fax | +39 049 8792024 | `contatti`: "via fax: +39 049.87.92.024" |
| Email | info@melsped.it | `contatti`, ricomposta dallo script anti-spam: `'&#105;nf&#111;' + '&#64;'` + `'m&#101;lsp&#101;d' + '&#46;' + '&#105;t'` |
| Orari | non pubblicati | |
| Anno | 1975 (sito); iscrizione della srl il 02/01/1978 | `azienda/profilo-aziendale`: "Nata nel 1975"; aziende.it: "Data Iscrizione 02/01/1978", "ATECO 52.26 dal 1978" |
| Attività | ATECO 52.26 | aziende.it: "Altre attivita' di supporto ai trasporti" |
| Fatturato e utile | 2025: 2.746.194 euro, utile 244.830; 2024: 2.595.647, utile 183.592; 2021: 3.083.210 | aziende.it, "Ultimi 3 bilanci disponibili", "Fonte: Registro Imprese" |
| Dipendenti | 7 (2024 e 2025) | aziende.it, tabella dei bilanci |
| Magazzino | oltre 1.400 mq | `servizi/logistica-e-servizi-doganali`: "uno spazio che supera i 1.400 metri quadri" |
| Paesi | Germania, Francia, Regno Unito, Belgio, Olanda, Spagna, Austria, Svizzera, Est Europa; Ungheria, Bulgaria, Romania in evidenza | `servizi`, `servizi/spedizioni-camionistiche` |
| Sponsorizzazione | Melsped Medoacus, pallavolo femminile, promossa in serie C nel 2012 | `news`: "La Melsped Medoacus ... è stata meritatamente promossa in Serie C" |
| Fornitore del sito | Nova Systems | piede: link a novasystems.it |

## 4. Materiale visivo

Tengo 25 file (1,8 MB) in `assets/originali/`, dopo aver tolto 8 doppioni identici. L'inventario con URL, pagine, misure, soggetto e voti (qualità / forza come apertura, da 1 a 10) è in `_prova/inventario-immagini.json`; i fogli provino sono in `_prova/fogli/`. Non ci sono video. La foto più grande è di 863 px (la squadra di pallavolo); le foto del mestiere arrivano al massimo a 660x435.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Scatolone davanti al furgone col logo, portoni del magazzino (`magazzino.jpg`) | 1 | 660x435 | 6 | 3 | la più fotografica, con profondità di campo e luce pulita. Sullo scatolone c'è il marchio di un'altra azienda (losanga rossa) |
| Ritratto di un'impiegata al portatile, planisfero alle spalle (`slide__customer-care-ritratto.jpg`) | 1 | 660x435 | 6 | 2 | professionale; persona riconoscibile, serve il consenso |
| Planisfero da parete con il logo stampato (`mappa.jpg`, più una variante) | 2 | 660x435 | 5 | 3 | è l'oggetto più loro, ma piccolo e morbido |
| Facciata della sede con l'insegna (`azienda2.jpg`, ritaglio `melsped.jpg`) | 2 | 400x266, 340x180 | 5 | 3 | vera, luce morbida; serve solo come traccia per rifarla |
| Furgone Iveco alla baia di carico (`furgone.jpg`, ritaglio `servizi.jpg`) | 2 | 400x266, 340x180 | 5 | 3 | l'unico mezzo vero |
| Fiancata del furgone, scritta inclinata (`logob.jpg`) | 1 | 660x435 | 5 | 2 | grafica, solo scritta |
| Open space con impiegata (`ufficio.jpg`) | 1 | 400x266 | 4 | 1 | grandangolo, neon |
| Fotomontaggio: trattore DAF col logo su strada mossa e cielo giallo (`camion.jpg`) | 1 | 660x426 | 3 | 1 | datato, da non usare |
| Repertorio virato in giallo (aereo, rimorchio, nave) e mani su tastiera | 4 | 158-220 px | 1 | 0 | da non usare |
| Squadra Melsped Medoacus | 1 | 863x517 | 4 | 0 | non è il mestiere |
| Logo: JPEG del sito, PNG sfumato del tema, PNG Facebook, mio ricalco SVG | 4 | 229-457 px | 3-6 | 0 | vedi sez. 8 |
| Icone social, bandierina, logo Nova Systems | 5 | piccole | 1-3 | 0 | da non usare |

**Verdetto**: il materiale **non regge** una home di alta gamma. Media 4 su 10 sulle foto del mestiere, nessuna sopra i 660 px. Le foto vere del 2013 sono fatte bene (un fotografo, luce controllata), quindi la direzione giusta è chiara: rifarle oggi a piena risoluzione. Per la proposta servono i segnaposto della sez. 6. Per il sito vero serve mezza giornata di fotografie:
- il furgone e un camion di un partner alla baia, con luce del mattino;
- la facciata con l'insegna;
- i portoni sezionali e il magazzino da 1.400 mq;
- un bancale filmato pronto per il groupage, in still life;
- il planisfero col logo, ripreso in piano e a tutta risoluzione;
- due ritratti in ufficio, con il consenso.

## 5. Due direzioni artistiche

**Il soggetto**: una spedizione che parte da Saonara e passa un confine. L'oggetto vero è il mezzo fermo alla baia o un bancale pronto. Il racconto è fatto di tre modi (strada, aereo, mare), della dogana e di un elenco di paesi già scritto da loro. Il giallo del logo (#F7CF0A circa) è l'unico accento che serve.

**Direzione A, "Il piazzale" (chiara, un solo oggetto)**
- Idea visiva: un solo semirimorchio bianco fermo su un piazzale di cemento chiaro sotto un cielo pulito, grande e nitido, e sopra il loro titolo "Il partner ideale per i vostri trasporti, dal 1975". Sotto, poche sezioni: i modi di spedire, dogana e magazzino, i paesi, la chiusura.
- Immagini: foto documentarie in luce di giorno, un oggetto per inquadratura (il mezzo, la baia, il bancale, l'aereo cargo sul piazzale). Segnaposto: Dextar `4PyLDWMC6A8` (apertura), Krupenin `4n2Tvf8ZKVM` (baie), AFINIS `OnbSOhz0oig` (magazzino), Peaky `PEf3deR3l_U` (aereo), Venti Views `1cqIcrWFQBI` (mare).
- Tipografia: Archivo (Google Fonts, OFL), con l'asse di larghezza: Archivo SemiExpanded 600 per i titoli, come una scritta su un rimorchio, e Archivo 400 per il testo. IBM Plex Mono piccolo per P.IVA, codici e misure ("1.400 mq").
- Colore: cemento chiaro #F4F2EE, asfalto #1D1E20 per il testo, grigio #8A8780 per le legende, il giallo #F7CF0A solo come campitura dietro testo scuro (sul bianco non passa AA). Niente nero pieno.
- Gesto: un selettore Strada, Aereo, Mare, Dogana. Al tocco cambia di netto la foto grande e cambiano le due righe di testo verbatim del servizio, senza dissolvenze.

**Direzione B, "Groupage" (chiara, la porta del container)**
- Idea visiva: la porta di un container, con aste e ganci di chiusura in verticale, a tutta larghezza sotto un titolo grande su fondo bianco: "Abbatti i confini" (titolo del loro profilo). Il ritmo verticale delle aste diventa la griglia della pagina.
- Immagini: dettagli dell'acciaio e delle chiusure, il piazzale dei container, le baie di carico in luce radente. Segnaposto: Milo `ajgOnWhzD1k` (apertura), Fejuz `q6j5mSRpi50`, OSG `uyDNkvdIKv8`, Jackson `SJGC3NNOqU4`. Per il sito vero: il planisfero col logo rifotografato, con le legende dei paesi come nella home amata di Mario Agnoletto.
- Tipografia: Barlow Semi Condensed 600 (Google Fonts, OFL) per i titoli, che ricorda le marcature dei container; Barlow 400 per il testo; IBM Plex Mono per i codici.
- Colore: bianco gesso #F6F6F3, inchiostro #15191C, il blu acciaio della foto (#2F5F86) solo nei link, il giallo del logo in un punto solo (il bottone del telefono, con testo scuro).
- Gesto: le parole "groupage" e "Intrastat" nel testo sono sottolineate. Al tocco si apre la loro definizione, presa dalle note a piè di pagina del sito di oggi, in una riga sotto la frase. È un vero bottone con `aria-expanded`.

**Ispirazioni Graziella e N19**: non le uso. Spedizioni e dogana sono un servizio B2B, non moda né lusso. Ne resta solo il principio dell'aria e di un oggetto per schermata, che è già nella ricetta del committente.

## 6. Immagini sostitutive

Ci sono 10 foto Unsplash in `assets/esterne/`, con il lato lungo a 2400 px. Su ogni pagina ho controllato la licenza ("Free to use under the Unsplash License", nessuna Unsplash+). Nessuna compare nei CREDITI delle altre home della campagna (elenco in `_prova/usate-campagna.txt`). URL, autori, licenza e marchi da ritoccare sono in `assets/CREDITI.md`. Sono segnaposto e il LEGGIMI lo dirà; nessuna è generata dall'IA.
- A, apertura: Dextar `4PyLDWMC6A8` (semirimorchio bianco sul piazzale). Alternativa: Dextar `2wpx8Bl0mwM` (stesso mezzo, più cielo). Altre per A: Krupenin `4n2Tvf8ZKVM`, AFINIS `OnbSOhz0oig`.
- B, apertura: Milo `ajgOnWhzD1k` (porta di container blu). Altre per B: OSG `uyDNkvdIKv8`, Fejuz `q6j5mSRpi50`, Jackson `SJGC3NNOqU4`.
- Comuni: Peaky `PEf3deR3l_U` (747 cargo bianco, aereo) e Venti Views `1cqIcrWFQBI` (portacontainer dall'alto, mare).
- Da ritoccare se si usano grandi:
  - la stella Mercedes e un indirizzo web sulla visiera del camion Dextar;
  - il marchio dell'handling sulla scaletta dell'aereo;
  - i nomi delle società di noleggio sui container di Fejuz.
- Manca una foto di dogana, perché in banca immagini ci sono solo timbri e moduli finti. Va raccontata con le parole o con una foto vera dell'ufficio.

## 7. Riferimenti di alta gamma nel mestiere

Ho aperto i siti dal vivo il 20/10/2026, accettando i cookie dove il bottone si trovava. Le prime schermate a 1440 e 390 sono in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (JPEG 78). I caratteri li ho letti dal codice con `_prova/script/font.mjs`. Il mestiere delle spedizioni non ha veri siti "di lusso". I più belli sono quelli degli spedizionieri d'arte (Momart, Gander & White) e di due spedizionieri digitali (Forto, Flexport).

1. **Momart** (momart.com, trasporto e magazzino di opere d'arte, Londra).
   - Cosa lo rende di alta gamma:
     - una sola foto vera a tutta larghezza, chiara: sculture in acciaio corten in magazzino, una avvolta nel film, una cassa di legno a fianco, cioè il lavoro, non la pubblicità;
     - il marchio è una parola sola centrata, Founders Grotesk Text 600, con il menu in un'icona;
     - in fondo c'è un'unica fascia blu notte con "Request an estimate".
   - È il registro più vicino alla direzione A: un oggetto vero, luce di giorno, niente slogan.
   - Da non riprendere: il menu nascosto anche su desktop e la foto a 390 sgranata.
2. **Gander & White** (ganderandwhite.com, spedizioni d'arte dal 1933, Londra).
   - Cosa lo rende di alta gamma:
     - un titolo maiuscolo enorme, "CUSTODIANS OF THE IRREPLACEABLE", in Freight Big 300 (serif), con "Est. 1933" in turchese;
     - il loro furgone col logo, fotografato sotto gli alberi;
     - testi in Roc Grotesk.
   - L'anno di fondazione dato come firma è la stessa cosa del "dal 1975" di Melsped.
   - Da non riprendere: il fondo nero, lo stemma reale e il logo in corsivo calligrafico; per Melsped sarebbe un costume.
3. **Forto** (forto.com, spedizioniere digitale, Berlino).
   - Cosa lo rende di alta gamma: prima schermata bianca, un titolo grande e corto "Global shipping made easy", una riga di testo, due bottoni e una portacontainer dall'alto ritagliata in una forma. A 390 regge identico.
   - Da non riprendere:
     - i cubi isometrici disegnati intorno alla foto;
     - la barra promozionale in alto;
     - Raleway e Inter insieme.
4. **Flexport** (flexport.com, spedizioni e dogana, San Francisco).
   - Cosa lo rende di alta gamma: un titolo centrato molto sottile (Zalando Sans 200, 58 px) su una foto di mare quasi monocroma, e il menu in maiuscolo mono spaziato.
   - Da non riprendere:
     - il campo email "Request a demo" in prima schermata;
     - la schermata dell'applicazione sovrapposta alla foto;
     - il testo bianco sottile sulla foto, poco leggibile;
     - il banner privacy che copre metà schermo.
5. **Kuehne+Nagel** (kuehne-nagel.com, il riferimento mondiale del mestiere).
   - Cosa funziona:
     - i tre modi (Sea, Air, Road) come bottoni semplici in un'unica riga;
     - il tracking in prima schermata;
     - un solo carattere (Suisse Intl) e un solo blu.
   - Va preso come confronto di funzione più che di stile.
   - Da non riprendere:
     - le tre colonne di notizie sopra una foto scurita;
     - il riquadro bianco con l'ombra;
     - il popup dei cookie a tutto schermo.

Scartati:
- Gebrüder Weiss (gw-world.com): slider con ritratto di repertorio, chat flottante e barra social laterale.
- DSV: video di un tunnel e un modulo di preventivo a tre colonne.
- Cargo-partner: fotomontaggio con persone in posa.
- Fercam: banner del mezzo usato e pannello dei cookie a metà schermo.
- Gruber Logistics e Hasenkamp: non rispondono dal proxy ("upstream request failed").

## 8. Per il piede

- **Logo**: il migliore trovato è il PNG 457x457 della foto profilo Facebook (`assets/originali/logo-facebook-457x457.png`, file del 2022). È giallo piatto con il contorno, con MELSPED e la riga "SPEDIZIONI INTERNAZIONALI". Il sito non ha un SVG, il favicon non esiste (404) e non ci sono PDF.
  - Ne ho fatto un ricalco a due colori, `logo-melsped-ricalco-da-facebook.svg` (#1A1A18, #F7CF0A). È fedele fino a circa 450 px di larghezza, quindi va bene nel piede; più grande i bordi ondulano.
  - Per la testata serve il vettoriale originale, oppure un ridisegno geometrico (il marchio è fatto di archi e rette).
  - Gli altri file sono `logo-sito-250x212.jpg` (testata di oggi, senza la riga) e `logo-sito-sfumato-229x180.png` (da non usare).
- **Menu di oggi**: Home; Chi Siamo (L'Azienda, Profilo Aziendale); Servizi (Camionistici, Aerei & Marittimi, Logistica & Dogana, Web); News; Contatti; IT e EN. Nel piede di oggi ci sono indirizzo, telefono, fax, P.IVA, capitale sociale e C.C.I.A.A.
- **Pagine del sito nuovo da linkare** (proposta):
  - Azienda: Chi siamo, dal 1975.
  - Servizi: Strada (groupage Europa, camion completi e dedicati, espressi, Est Europa), Aereo, Mare, Dogana e Intrastat, Logistica e magazzino.
  - Paesi serviti.
  - Contatti.
  - Privacy, Cookie (oggi mancano).
  - English.
- **Social**:
  - LinkedIn esiste: https://www.linkedin.com/company/melsped ("Melsped", sede "VIALE VENETO, 9 Saonara"). La descrizione è la stessa meta description del sito, il settore è sbagliato ("Government Administration") e non c'è il logo.
  - La pagina Facebook esiste (id 140914439402355, ora facebook.com/melsped, foto profilo del 2022), ma i contenuti non si leggono senza login.
  - Twitter/X `@Melsped` è linkato dal sito; X chiede il login e non ho potuto verificare se l'account esiste ancora.
  - Google+ è chiuso.
  - Nel piede propongo solo LinkedIn, più Facebook se confermano che è attiva.
- **Newsletter**: oggi non c'è e non ha senso. Melsped è uno spedizioniere B2B con 7 persone, senza fiere, senza cataloghi né clienti privati, e le sue sole "notizie" sono cronache di pallavolo del 2012. Nel piede va un'altra riga: il numero di telefono e l'email.
- **Riga legale**: Melsped Srl, viale Veneto 9, 35020 Saonara (PD), P.IVA e C.F. IT00606650281, REA PD-127485, capitale sociale 110.000,00 euro i.v., PEC melsped@pec.it, Privacy, Cookie.

## 9. Da confermare

- L'anno: il sito dice "1975", il Registro Imprese dà l'iscrizione della srl al 02/01/1978. Quale scrivere? Il 1975 è l'anno di una ditta precedente?
- Il "Tracking" della pagina Web è scritto al futuro ("sarà in grado"): oggi esiste un tracciamento online o un'area clienti?
- Quali servizi sono ancora attivi oggi, dato che il testo è del 2013: le tratte giornaliere, i camion completi, l'aereo e il mare. È ancora vero il rapporto con Ungheria, Bulgaria e Romania?
- Il magazzino: è ancora "oltre 1.400 metri quadri"?
- Certificazioni: hanno lo status AEO (Operatore Economico Autorizzato) o una ISO 9001? Sul sito non c'è nulla.
- Numeri da mostrare: spedizioni l'anno, paesi, corrispondenti. Non sono pubblici; i dipendenti sono 7 (2025).
- Orari d'ufficio e di magazzino; se il fax 049 8792024 è ancora in uso; quale email usare (info@melsped.it).
- I social: Facebook è attiva? L'account Twitter/X esiste ancora? La pagina LinkedIn va corretta (settore e logo)?
- La sponsorizzazione della pallavolo (Melsped Medoacus): è ancora attiva? Va citata?
- I diritti delle foto del 2013: chi è il fotografo? Esistono gli originali ad alta risoluzione? Le due impiegate ritratte hanno dato il consenso? Sono ancora in azienda?
- Il marchio sullo scatolone di `magazzino.jpg`: è un cliente? Va tolto.
- Il logo vettoriale originale e il giallo ufficiale: nel PNG Facebook è #F7CF0A circa, nel JPEG del sito è più arancio.
- Il pixel di tracciamento whoseesyou.com e l'assenza del banner cookie: nel sito nuovo vanno chiariti con il loro consulente privacy.
