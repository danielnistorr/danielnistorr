# Bordin Garden & Vivai: analisi per la nuova home

Sito: https://www.bordingarden.it (crawl del 24/10/2026: home, Bordin, Garden, Vivai, Giardini, Album realizzazioni, News e 2 notizie, Contatti, Credits; più il book "I NOSTRI GIARDINI" su sfogliami.it). Le pagine del sito sono indicate col percorso dopo `bordingarden.it/`. Il sito ha un firewall BitNinja che, dopo poche richieste ravvicinate, risponde con una pagina CAPTCHA (403) o chiude la connessione: le pagine `bordin` e `vivai` le ho lette con WebFetch, le immagini e i file del tema li ho scaricati a mano uno ogni 12-15 secondi.

## 1. In breve

- **Chi**: un'azienda di famiglia a Saonara (PD) con due sedi sulla stessa strada: **Bordin Garden** (garden center, via dei Vivai 6) e **Bordin Vivai** (vivaio di produzione, via dei Vivai 14). Società: "Bordin Garden & Vivai S.n.c. di Bordin Omero e Giuliano Società Agricola" (registri, sez. 3).
- **Da quando**: dal 1955, "quando i due fratelli Saverio e Alcide" fondarono i Vivai Piante Bordin, prima piante da frutto e rose, poi "piante ornamentali di primissima qualità" (`bordin`). Il garden center è del **1996**, "uno dei primi Garden Center di Padova". Oggi lavora la terza generazione. La snc attuale è iscritta da circa 35 anni (atoka: "Operativa da 35 anni").
- **Cosa fa davvero**, tre mestieri:
  1. **Vivaio**: produce piante ornamentali "dai piccoli arbusti fino ad esemplari unici e di rara bellezza", vendute "sia in zolla che in vaso", spedite e messe a dimora "in qualsiasi parte d'Italia" (`vivai`).
  2. **Garden center**: "centro del verde a forma di piramide" con piante da interno ed esterno, bonsai, piante grasse, vasi in terracotta, arredo da giardino, "profumi, detergenti bio e raffinate idee regalo" (`garden`).
  3. **Giardini**: progetto e realizzazione "chiavi in mano" di giardini, parchi, terrazze e verde pensile; trapianto di piante esemplari; restauro di giardini storici; verde per uffici; manutenzione (`bordin`, `giardini`). 33 album di lavori sul sito, con foto "PRIMA, DURANTE, DOPO".
- **Per chi**: privati (il garden è aperto sei giorni su sette), e nel lavoro dei giardini anche "architetti, impresari" (book, p. 9).
- **Quanti**: microimpresa; 4 dipendenti per atoka, 5 per un estratto di ufficiocamerale (pagina non aperta, 403). Superfici del vivaio e fatturato non sono pubblici.
- **Correzione della nota di partenza**: il "riquadro verde vuoto" della home **non è un carosello rotto**. Lo slider funziona (19 voci di owl carousel, tre slide Garden, Vivai, Giardini con foto a 1920 px). Il riquadro vuoto delle schermate di valutazione nasce dal firewall, che ha bloccato `owl.carousel.min.js`, `bootstrap.min.js`, `wow.min.js` e `bordin.js` al browser automatico (registro in `_prova/attuale/`). Un visitatore normale probabilmente vede lo slider, ma va verificato da un telefono vero: se il firewall colpisce anche i visitatori veri, il problema è più grave di un carosello (sez. 9). Il resto della nota è giusto: famiglia dal 1955, via dei Vivai 6 e 14, foto proprie sul server.

## 2. Il sito di oggi

**Pagine** (menu: Home, Bordin, Garden, Vivai, Giardini, News, Contatti, più Facebook, Instagram e una ricerca):
- `bordin.html` "Una storia di passione!": storia, Mission, I nostri servizi, 5 foto.
- `garden.html` "Venite a visitarci!": testo, elenco dei prodotti, "Galleria Articoli" (8 foto).
- `vivai.html` "Produciamo Natura!": "La nostra produzione", "Galleria esemplari" (7 foto).
- `giardini.html` "Affidatevi alla nostra esperienza!": testo, link al book sfogliabile, `giardini/album-realizzazioni/` con 33 album (Biolago, Giardino a Venezia, Giardino in un'isola veneziana, Villa Palladiana, Parco Villa Veneta, Impianto esemplari, Lago naturale, Giardino per un Ristorante, Rustico con piscina...), ognuno diviso in DOPO, DURANTE, PRIMA.
- `news/`: due notizie, "Lavora con Noi!" (02/08/2025) e "Seguici su Facebook e Instagram" (08/03/2023).
- `contatti.html`: telefoni, indirizzi, modulo (nome, email, telefono, messaggio, consenso privacy).
- `credits.html`, Privacy e Cookie su iubenda.

**Testi veri essenziali (verbatim)**:
- Slide della home: "GARDEN / Venite a visitarci! Troverete il valore aggiunto della cortesia e della grande esperienza Bordin."; "VIVAI / Produciamo Natura! Abbiamo la competenza, l'organizzazione e la professionalità garantita dal marchio Bordin!"; "GIARDINI / Affidatevi alla nostra esperienza! Realizzate il vostro spazio verde con l'esperienza e la qualità offerti da Bordin!"
- Storia (`bordin`): "Le radici dell'azienda vennero formate nell'ormai lontano 1955, quando i due fratelli Saverio e Alcide"; "specializzandosi soprattutto in piante ornamentali di primissima qualità"; "sviluppò competenze nella progettazione e nella fornitura chiavi in mano di importanti Parchi e Giardini"; "Nel 1996 vennero ampliati i servizi offerti creando Bordin Garden Center, uno dei primi Garden Center di Padova"; "Negli ultimi anni è entrata in azienda la terza generazione che sta portando nuove energie, idee e competenze"; "Lo scopo è arricchire coloro che si affidano a Bordin".
- Servizi (`bordin`): "Progettazione e realizzazione "chiavi in mano" di giardini, di parchi, di terrazze e di verde pensile"; "Trapianti e messa a dimora di piante esemplari"; "Restauro di giardini storici"; "Allestimenti per uffici con piante da interno"; "Produzione di piante ornamentali ed esemplari unici".
- Vivai: "vanta più di sessant'anni di attività nella produzione di rare piante ornamentali e di assoluta qualità"; "piante uniche, dalle più comuni alle poco conosciute"; "commercializzati sia in zolla che in vaso"; "gestendo anche la parte logistica della spedizione (anche di grandi esemplari)"; "pronti per essere spediti in tutta Italia."
- Garden: "Sin dal 1996, anno della sua inaugurazione, l'obiettivo principale è quello di offrire un luogo piacevole e immerso nel verde a due passi da Padova"; "questo particolare e unico centro del verde a forma di piramide"; "Sono migliaia le proposte da scoprire"; elenco: "Vasta scelta di piante sia da interno che da esterno.", "Collezione di bonsai e molti accessori", "Pregiati vasi in terracotta.", "Collezione di piante grasse, dalle più piccole alle più grandi, anche di rare varietà.", "Eleganti elementi d'arredo per il giardino e gli spazi verdi.", "Profumi, detergenti bio e raffinate idee regalo."
- Giardini: "risultati affascinanti, attraenti ed originali, in giardini e parchi di qualsiasi dimensione e tipo"; "creando giardini che crescono armoniosamente"; "I giardini sono progettati e realizzati in ogni minimo dettaglio, con una scrupolosa scelta delle piante"; "uno spazio verde che possa essere un valore aggiunto, un investimento per il proprio ambiente e per la propria qualità di vita".
- Book "I NOSTRI GIARDINI" (sfogliami, 13 pagine pubblicate): "Passione per il verde dal 1955"; "Desideriamo migliorare la vostra vita attraverso la Natura"; "Tutte le piante utilizzate, a prova della loro qualità, hanno una garanzia d'attecchimento di un anno"; "Siamo sempre alla ricerca di nuove specie botaniche e piante particolari che testiamo nei nostri vivai"; "In ogni stagione ci saranno sempre fiori, colori o profumi particolari"; il metodo in 4 passi: "Sopralluogo in cantiere", "Visione della proposta progettuale e relativo preventivo 'Chiavi in mano'. Visita in vivaio per vedere dal vivo le piante proposte", "Accettazione del preventivo e definizione delle tempistiche", "Manutenzioni straordinarie per seguire la crescita corretta del giardino". Due pagine "Prima" e "Dopo" della stessa aiuola.
- Orari (home e contatti). Garden: lunedì 15:00-19:00; martedì-venerdì 08:30-12:30 e 15:00-19:00; sabato 9:00-12:30 e 15:00-19:00; domenica chiuso. Vivai: lunedì-venerdì 08:00-12:00 e 14:00-18:00; sabato mattina su appuntamento.
- Lavora con noi: "Se sei appassionato di piante e giardinaggio e desideri lavorare con la natura inviaci il tuo curriculum".
- Non ci sono numeri (ettari, specie, giardini fatti), certificazioni, premi o nomi di clienti.

**Tecnologia**:
- CMS proprietario di PARTE srl / Medianteam (Padova): "Engineered & Powered by PARTE srl" (`credits`), copyright fermo a "© 2016".
- Bootstrap 3.3.6, jQuery 2.2.4, Owl Carousel 2.3.1, Cycle2, WOW.js con waypoints, Font Awesome 4.5, AddThis (servizio chiuso dal 2023).
- Font Google: Capriola, Roboto, Roboto Condensed, Cardo, Courgette (il corsivo calligrafico dei sottotitoli).
- Iubenda per cookie e privacy, WhatsApp con link `wa.me`, `theme-color` #00CC00.
- Nessuna meta description; titoli "Home - BORDIN Garden & Vivai"; nessuna sitemap.xml (404).
- Firewall BitNinja sul server: CAPTCHA e connessioni chiuse dopo poche richieste.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `home-1440-prima.jpg`, resa con i file del sito serviti dal disco; `valutazione-home-1440.jpg` è la schermata della valutazione col firewall attivo):
- Testata verde chiaro, logo piccolo (180 px), menu maiuscolo a 8 voci più icone.
- Slider a tutta larghezza alto 600 px con testo bianco centrato e ombreggiato sopra foto chiare (il disegno del progetto, l'interno del garden): si legge male. Sottotitolo in Courgette corsivo.
- Sotto, tutto su fondo verde texture "foglia": tre pulsanti a pillola con icone al tratto, un riquadro notizie con ombra e la notizia "Seguici su Facebook e Instagram" del 2023.
- Otto riquadri bianchi con orari, telefoni e indirizzi, titoli in Cardo con icone Font Awesome: le informazioni utili ci sono, ma pesano come un modulo.
- Nessuna frase su cosa fanno, nessuna foto di esemplari, nessun giardino, nessuna data "1955" a parte il logo. La pagina è alta 1760 px.
- Piede nero a dente di sega con copyright 2016.

**Problemi a 390** (`home-390.jpg`):
- Logo e hamburger centrati in una testata di 120 px; slider alto 310 px.
- Durante il cambio di slide i due testi si sovrappongono e diventano illeggibili.
- Gli orari in 8 riquadri impilati allungano la pagina a 2913 px; i telefoni si toccano bene.
- Nessuno scorrimento orizzontale. Il bottone fisso di iubenda copre un pulsante.
- Se il firewall blocca gli script (`valutazione-home-390.jpg`), la home diventa un fondo verde vuoto di 2800 px.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale sul sito | BORDIN Garden & Vivai Snc | piede di ogni pagina: "Copyright © 2016 BORDIN Garden & Vivai Snc" |
| Ragione sociale nei registri | Bordin Garden & Vivai S.n.c. di Bordin Omero e Giuliano Società Agricola | atoka.io/public/it/azienda/bordin-garden-vivai-snc-di-bordin-omero-e-giuliano-societa-agricola/588c5d2bcf5b; icribis.com (scheda PD231319) |
| P.IVA e CF | 01315760288 (cifra di controllo valida) | piede: "Partita IVA e Codice Fiscale: 01315760288"; atoka: "P.IVA: 01315760288" |
| REA | PD-231319 | icribis: "REA: PD - 231319" |
| Forma, attività | snc, società agricola; ATECO 01.30 "Riproduzione delle piante" | icribis; atoka: "La gestione e la conduzione di terreni agricoli per attivita' vivaistiche e florovivaistiche in genere." |
| Sede legale | via dei Vivai 14, 35020 Saonara (PD) | atoka, icribis |
| Garden | via dei Vivai 6, Saonara (PD) | home e `contatti`: "BORDIN Garden Via dei Vivai, 6, Saonara (PD)" |
| Vivai | via dei Vivai 14, Saonara (PD) | `contatti`: "BORDIN Vivai Via dei Vivai, 14, Saonara (PD)" |
| Telefoni | Garden 049 8791098, WhatsApp 350 1376907; Vivai 049 640156, WhatsApp 350 5859658 | `contatti` (link `tel:0039049/8791098`, `wa.me/00393501376907`, `tel:0039049/640156`, `wa.me/00393505859658`) |
| Email | info@bordingarden.it (Garden), info@bordinvivai.it (Vivai e curricula) | `contatti`; `news/2025/08/lavora-con-noi.html` |
| Mappe | Garden 45.38608, 11.961015; Vivai 45.3857, 11.9625 | link Google Maps nel piede della home |
| Anno | 1955 la famiglia; 1996 il garden center | `bordin`; book p. 3 "Passione per il verde dal 1955" |
| Dipendenti | 4 | atoka: "Dipendenti: 4" (5 secondo un estratto di ufficiocamerale, non aperto) |
| Società collegata | Commerciale Garden Bordin di Bordin Omero e C. S.n.c., P.IVA 02463340287, REA PD-231259, via dei Vivai 6, iscritta il 04/11/1991, ATECO 81.3 "Cura e manutenzione del paesaggio" | aziende.it/commerciale-garden-bordin-di-bordin-omero-e-c-s-n-c-c-con-sigla-comm-garden-bordin-s-n-c |
| PEC, capitale sociale, fatturato | non trovati (snc: capitale non obbligatorio) | ufficiocamerale, reportaziende, informazione-aziende rispondono 403 o 429 |

## 4. Materiale visivo

Scaricati in `assets/originali/` (versioni della cache), `assets/originali/grandi/` (originali fino a 2128 px), `assets/originali/album/` (campione di 2 album su 33, firewall permettendo) e `assets/originali/book/` (13 pagine del book). Inventario con misure, soggetto e voti in `_prova/inventario-immagini.json`. Nessun video sul sito. Il firewall ha impedito di scaricare 9 originali, che ho solo nella versione 960x600.

| Gruppo | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|
| Garden center: la piramide in vetro con un olivo potato a nuvole davanti e le aiuole di aromatiche (`G6`) | 1920x1080 | 6 | 6 | la foto vera migliore: di giorno, pulita, riconoscibile e solo loro |
| Alberi appena zollati, le zolle in rete in fila sul prato (`VB2`) | 2128x1416 | 6 | 6 | racconta il mestiere ("in zolla") meglio di tutto; luce piatta, sfondo disordinato |
| Trapianti: gru che solleva un olivo con la zolla (`BB1`), esemplari multitronco con trattore (`VBesemplariR`), camion davanti a una villa veneta (`3-Cartolina`) | 1600-1920 px | 4-5 | 3-5 | storie forti, foto da cantiere datate e sature |
| Campi di produzione, filari in primavera e in inverno (`VB4`, `VB5`, `V6`) | 960-2128 px | 5 | 4 | pulite, senza un soggetto |
| Garden center: interno, laghetto, serra, fiori recisi (`G1`, `G2`, `G5`, `G8`, `G10`, `garden-1/2b/3b`) | 960-1920 px | 3-5 | 1-4 | affollate, luce mista |
| Album Villa Palladiana: arco in pietra tra bosso e rose, barchessa con torre colombara (`album/121--DO_Mix_146`, `148`) | 1624x1080 | 6 | 5 | i lavori più belli trovati, ma con il logo Bordin stampato nell'angolo: servono gli originali puliti |
| Album Giardino a Venezia: corte tra case rosse, pergola, camminamento in pietra (`album/172--...`) | 1920-3000 px | 4-5 | 3-4 | panoramiche da telefono, logo stampato |
| Altri giardini fatti (`Giardini_3ok`, `Giardini_4`, `F1`-`F6`) | 960-1960 px | 3-5 | 2-4 | lavori di livello (corte di palazzo, villa moderna, piscina); foto con filtri e vignettature |
| Giardino formale con Roma e San Pietro sullo sfondo (`Fronte_2RID`) | 2000x1349 | 4 | 4 | scansione velata; se è un lavoro loro è un argomento forte |
| Disegni del progetto con matite e cartellino Bordin (`DSC_1200`) | 1920x967 | 5 | 4 | racconta la progettazione |
| Vedute aeree del garden e del vivaio (`1-Cartolina`, `4-Cartolina`) | 1920x1200 | 4 | 2-3 | scansioni da pellicola; dominano strada e parcheggio |
| Macro generiche (foglie variegate, gardenia, tronchi) | 1920 px | 4-5 | 2-3 | belle ma di repertorio, non dicono Bordin |
| Book "I NOSTRI GIARDINI" | 1024x721 | 3 | 1 | pagine con testo stampato: utili per i testi |
| Logo | PNG 360x126 | 3 | 0 | solo raster: serve il vettoriale |

**Verdetto**: il materiale vale **4,5 su 10** e da solo **non regge** una home di alta gamma, ma è vero e ha due soggetti forti che nessun concorrente ha: la **piramide** del garden e **gli esemplari in zolla** spostati con la gru. Per la proposta: `G6` e `VB2` si possono usare, ripuliti e ritagliati, come prove "dal vero" dentro la pagina; l'apertura va fatta con un segnaposto (sez. 6). Per il sito vero serve una giornata di foto: un esemplare in zolla ritratto su fondo neutro, la piramide all'alba, i filari, due o tre giardini finiti in luce radente.

## 5. Due direzioni artistiche

Il soggetto visivo: un albero intero con la sua zolla avvolta nella rete è già una scultura, ed è il loro mestiere in un'immagine ("sia in zolla che in vaso", "trapianti di piante esemplari", "garanzia d'attecchimento di un anno"). L'altro segno è la piramide di vetro del 1996.

Ispirazioni Graziella e N19: le uso pochissimo. Un vivaio con garden center non è moda: ne prendo solo l'aria e le etichette piccole in maiuscoletto, non i menu a tutta pagina né le comparse animate.

**Direzione A, "L'esemplare" (chiara, un solo oggetto vero)**
- Idea visiva: il ritratto di un solo albero, intero, con la zolla in rete, scontornato su carta calda, grande e nitido come in un erbario. Accanto, il titolo "Produciamo natura dal 1955" e tre legende fini con i fatti veri (zolla in rete, spedito e messo a dimora in tutta Italia, attecchimento garantito un anno).
- Immagini: un esemplare per sezione, luce morbida da nord, fondo neutro; sotto, un solo giardino finito a tutta larghezza. Segnaposto: Dittrich (esemplare in vaso), Austvika (olivo), Akira (ombra sul muro); dal vero `VB2`.
- Tipografia: Zodiak (Fontshare, serif da titoli, pesi 300-400 dritti, mai corsivo) per i titoli; Switzer (Fontshare) per il testo; numeri tabellari per gli orari.
- Colore: carta #F3F0E8, inchiostro verde quasi nero #1F2A1F, grigio del logo #5A5959, juta #B39A72 per filetti e legende; il verde del logo #39A559 solo nella foglia.
- Gesto: "In zolla / Messo a dimora": un interruttore a due voci che cambia la foto dello stesso esemplare, dal piazzale del vivaio al giardino finito (dal vero: le coppie PRIMA e DOPO degli album). Cambio netto, nessuna dissolvenza.

**Direzione B, "Via dei Vivai" (chiara e luminosa, il luogo)**
- Idea visiva: la home come una visita: una grande foto luminosa del vivaio in primavera, il titolo "Passione per il verde dal 1955", e poi tre luoghi (Garden, Vivai, Giardini) presentati con una foto ciascuno e una riga, in un ordine pulito a due colonne larghe, non tre box.
- Immagini: la piramide di vetro (rifatta dal vero), i filari, una serra luminosa, vasi in terracotta, un giardino formale restaurato. Segnaposto: Nauwelaerts (serra), Smith (vivaio), Spratt (terracotta), Goodman (giardino formale), Leongsan (graminacee).
- Tipografia: Cabinet Grotesk (Fontshare) per i titoli, grandi e compatti; Satoshi (Fontshare) per il testo; etichette in maiuscoletto spaziato per orari e indirizzi.
- Colore: bianco caldo #FAF8F3, verde bosco #23402B per testi e bottoni, terracotta #B5562E come unico accento, salvia #C9D3C1 per i fondi chiari.
- Gesto: "Aperto adesso": una riga sotto il titolo che legge gli orari veri e dice "Il Garden è aperto fino alle 19:00" o "Riapre martedì alle 8:30", con il link alla mappa. Utile ogni giorno, nessuna animazione.

## 6. Immagini sostitutive

Dieci foto Unsplash in `assets/esterne/` (al massimo 2400 px di lato), licenza letta sulla pagina di ognuna il 24/10/2026: "Free to use under the Unsplash License", nessuna Unsplash+. URL, autori e date in `assets/CREDITI.md`. Nessuna compare nei CREDITI delle altre home della campagna; nessuna è generata dall'IA; nessun marchio in vista.
- A, apertura: Dittrich, esemplare potato a nuvole in vaso (`dittrich-esemplare-vaso.jpg`); alternativa Austvika, olivo in vaso contro un muro chiaro. Altre per A: Akira, albero e ombra su muro bianco; Dittrich, esemplare in piena terra; Elliott, acero giapponese (dettaglio).
- B, apertura: Smith, alberelli in vaso davanti alle serre (`smith-vivaio.jpg`) o Nauwelaerts, serra luminosa. Altre per B: Spratt, vasi in terracotta; Goodman, giardino formale a siepi; Leongsan, graminacee in controluce.
- Limiti: le due foto Dittrich sono state scattate in Vietnam (pagoda di Bái Đính), lo sfondo va tagliato stretto; manca un albero in zolla con la rete su fondo neutro, che sarebbe l'apertura perfetta: va fotografato da Bordin (non l'ho trovato libero su Unsplash e Pexels).

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/` (JPEG, qualità 78), aperte il 24/10/2026; caratteri letti dal codice.

1. **Tom Stuart-Smith Studio** (tomstuartsmith.co.uk, progettista di giardini).
   - Alta gamma: una sola foto a tutto schermo del Barn Garden in luce di sera, il nome dello studio piccolo in alto a sinistra, quattro voci di menu in Neuzeit. A 390 cambia foto e resta composta. Niente testo sopra la foto.
   - Da non riprendere: nessuna frase né invito in prima schermata; per un'azienda che vende serve almeno il titolo e il telefono.
2. **Margheriti Piante** (margheriti.it, vivaio di Chiusi, Toscana).
   - Alta gamma: foto dei filari di esemplari al tramonto incorniciata con margini bianchi, titolo "Una vera industria del verde" grande; è il riferimento più vicino a Bordin Vivai.
   - Da non riprendere: Playfair Display bianco sopra la foto, la linguetta verticale "CATALOGO", le bandierine delle lingue.
3. **Piet Oudolf** (oudolf.com, paesaggista).
   - Alta gamma: la prima schermata è solo l'elenco dei giardini fatti, enorme, in Univers Light grigio con la sigla del paese: i lavori come titolo. Moltissima aria.
   - Da non riprendere: le immagini che compaiono dentro le lettere al passaggio del mouse; a 390 è un elenco senza fine.
4. **Sarah Price Landscapes** (sarahpricelandscapes.com).
   - Alta gamma: una foto ravvicinata di iris in controluce a tutta larghezza, nome in maiuscoletto Futura PT spaziato, menu minuscolo; Freight Big per i titoli.
   - Da non riprendere: il carosello con le frecce, il menu grigio chiaro quasi illeggibile.
5. **Clifton Nurseries** (clifton.co.uk, garden center e servizio giardini a Londra dal 1851).
   - Alta gamma: è lo stesso modello di Bordin (negozio, giardini su misura, storia lunga) e lo dice in una riga: "Inspiring Gardeners since 1851", con logo a stemma; foto vera della serra.
   - Da non riprendere: i due bottoni verdi pieni in alto, i social sopra il logo, il menu in maiuscolo piccolo.

Scartati (in `riferimenti/scartati/`): Petersham Nurseries (la prima schermata è un avviso del ristorante), Great Dixter (avviso a tutta pagina), Vivai Capitanio (foto scurita e parola d'accento in corsivo); Van den Berk, Terrain e Giorgio Tesi non si sono aperti (cookie a muro, accesso bloccato, slider nero) e non li ho tenuti.

## 8. Per il piede

- **Logo**: solo PNG 360x126 con trasparenza (`assets/originali/logo-bordin-360x126.png`): "Bordin" in un serif classico grigio #5A5959, foglia verde #39A559 al posto del punto della i, "1955" in verticale verde a sinistra, filetto verde, "GARDEN & VIVAI" in maiuscolo spaziato. Icona quadrata 310 px con la sola foglia (`logo-icona-310.png`). Nessun SVG nel codice, nessun PDF. Un SVG fedele si può ricostruire (foglia più testo), ma il carattere della scritta va riconosciuto prima; altrimenti il PNG a 2x basta fino a 180 px di larghezza.
- **Voci di menu di oggi**: Home, Bordin, Garden, Vivai, Giardini, News, Contatti; nel piede Privacy Policy, Cookie Policy, Credits.
- **Social che esistono** (linkati dal sito): Facebook https://www.facebook.com/BordinGarden, Instagram https://www.instagram.com/bordingardenvivai/. Più due WhatsApp. Numeri di follower non leggibili (login e 429).
- **Newsletter**: oggi non c'è. **Ha senso**: clienti privati del garden, "novità e promozioni" annunciate sui social, stagioni e fioriture, un book dei giardini. Campo email, bottone, consenso privacy; da collegare a un servizio (sez. 9).
- **Dati per l'ultima riga**: BORDIN Garden & Vivai Snc (nei registri "Bordin Garden & Vivai S.n.c. di Bordin Omero e Giuliano Società Agricola"), P.IVA e CF 01315760288, REA PD-231319, Privacy e Cookie (iubenda). Capitale sociale e PEC non trovati.

## 9. Da confermare

- Se il firewall BitNinja blocca anche i visitatori veri (provare da un telefono in 4G aprendo tre o quattro pagine di fila): in quel caso la home appare vuota anche ai clienti.
- Il rapporto tra le due società (Bordin Garden & Vivai snc agricola e Commerciale Garden Bordin snc, P.IVA 02463340287, stesso indirizzo): quale ragione sociale va nel piede del garden.
- Dipendenti (4 o 5), superficie del vivaio, numero di specie: non pubblici.
- PEC e capitale sociale.
- Il giardino con la cupola di San Pietro sullo sfondo (`Fronte_2RID`): è un lavoro loro a Roma? Si può dire?
- Nomi e luoghi dei giardini degli album (Villa Palladiana, Venezia, isola veneziana): si possono citare? E gli originali delle foto degli album senza il logo stampato nell'angolo.
- La "garanzia d'attecchimento di un anno" (book): vale ancora e per quali piante?
- La terza generazione: nomi e ruoli, se vogliono comparire.
- Diritti delle foto aeree e delle cartoline (`1-Cartolina`, `4-Cartolina`): sono loro?
- Il logo vettoriale (chi l'ha disegnato) e il carattere della scritta.
- La newsletter: quale servizio (Brevo, Mailchimp) e chi la scrive.
- Orari stagionali (domeniche di primavera, chiusure estive) e se il sabato del vivaio è ancora su appuntamento.
- Le pagine del book oltre la 13 (il visualizzatore ne dichiara 66, sul server ce ne sono 13).
