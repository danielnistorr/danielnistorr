# Tre Emme Manufatti: analisi per la nuova home

Sito: http://www.3emme.com/ (crawl di 145 pagine IT e screenshot del 20/10/2026). Fonti citate come URL + frase. Le pagine del sito sono indicate con il percorso dopo `3emme.com/it/`. Testi grezzi in `_prova/crawl/pages/`, schede prodotto estratte in `_prova/crawl/prodotti.json`.

## 1. In breve

- **Chi**: Tre Emme Manufatti S.r.l., via Lombardia 23, Saonara (PD). Nata nel 1981 "dall'intuizione di un giovanissimo Gianfranco Berto e di sua moglie" (`azienda`). È di famiglia anche oggi: nei contatti Gianfranco Berto è Direttore Generale, Laura, Sara e Manola Berto guidano acquisti, commerciale e amministrazione (`contatti`).
- **Cosa fa davvero**: produce **ruote per carrozzine** (a raggi attive da 20" a 32", anteriori da 4" a 8", ruote a dischi per carrozzine elettroniche), più freni, forcelle, mozzi, corrimano, assi a sgancio rapido, differenziali e ricambi. Il punto tecnico che rivendica è il **poliuretano espanso fatto in casa** per anelli e gomme piene antiforatura (`azienda`). Le bici a tre ruote (Bicitris ed e-bike) sono un ramo laterale, non il centro.
- **Per chi**: produttori di carrozzine e rivenditori (codici d'ordine, area riservata, "3-6 mesi per le aziende"), ma anche privati ("2 anni per i privati", `condizioni-di-vendita`). Altri usi dichiarati: pet-rehab, carrelli industriali, lavapavimenti, bike trailer, nordic walking (`azienda`, `prodotti/altre_applicazioni`).
- **Quanti**: 2.000 mq (`azienda`), 15 dipendenti e 3.688.625 euro di fatturato nel 2024, utile 706.316 euro (aziende.it, dati dal Registro Imprese). Si dice "il principale produttore di ruote per carrozzine per disabili in Italia" (`azienda`): è una loro affermazione.
- **Correzioni alla nota di partenza**: il "dal 1981" è giusto, ma il Registro Imprese dà iscrizione 30/09/1993 (sez. 3). L'ISO 9001 c'è solo per "due specifiche categorie dei nostri prodotti" (Emiplegico Light e ruote a dischi in alluminio con pneumatico), e i loghi ISO e Accredia sono commentati nel codice della testata: non va scritto "azienda certificata". Le foto prodotto non sono "decine" ma circa 490 file, e circa 200 sono scatti da studio sopra i 1600 px: il materiale è molto meglio di quanto sembri dal sito.
- **Il punto**: Tre Emme fa la parte che porta una persona, cioè la ruota. Il mozzo in alluminio tornito con i raggi colorati è già un oggetto bello: la home può essere un catalogo da gioielleria meccanica, chiaro, con il motto che hanno già, "Wheels for life!".

## 2. Il sito di oggi

**Pagine**: Home, Prodotti (Rehabilitazione con 20 famiglie, Altre applicazioni con 6), Azienda, Contatti, News (12 notizie, dal 02/02/2015 al 19/08/2023), Promozioni (vuota), Guestbook, Come ordinare, Note tecniche utili, Condizioni di vendita, Privacy. Circa 86 schede prodotto. Area riservata (`/Geweb/Autentica.asp`), pagina "Paga con carta di credito" (`/pay.asp`), versione inglese (il cambio lingua `lang.asp?NewLang=en` oggi risponde errore 500).

**Testi veri essenziali (verbatim)**:
- Titolo della pagina: "Ruote, differenziali e gomme poliuretaniche per carrozzine". Motto nel logo: "Wheels for life!".
- Azienda:
  - "Tre Emme Manufatti: oltre 40 anni di esperienza e innovazione nel settore delle ruote per carrozzine"
  - "l'azienda opera su una superficie di 2.000 mq, dotata di macchinari all'avanguardia e di personale altamente specializzato"
  - "offrire prodotti realizzati interamente in Italia, frutto della maestria e della tradizione manifatturiera che ci contraddistinguono"
  - "applichiamo la certificazione ISO 9001 a due specifiche categorie dei nostri prodotti: 1. Emipligico Light 2. Ruote a dischi in alluminio con pneumatico gonfiabile"
  - "Oltre alle ruote, produciamo freni, forcelle, assi a sgancio rapido (quick release) e boccole."
  - "Uno dei punti di forza dell'azienda è la realizzazione di poliuretano espanso di altissima qualità, impiegato nella produzione di anelli e gomme piene. Questa soluzione, antiforatura per eccellenza, [...] può essere personalizzata variando colore e durezza."
  - "La codifica è semplice ed intuitiva e permette di costruire la ruota completa"
- Come ordinare: la ruota si ordina per codice, con le varianti accodate: "T24A+S595P+AAL24" (Top Light 24x1 standard) e "T24A-M41N+S595P+AAL24" (stessa ruota con mozzo nero).
- Note tecniche: "prodotti per una velocità max di 6 km/h", ruote 3.00-8 e 260x85 "fino a 15 km/h"; coppie di serraggio "vite da 8mm 30/35 Nm", "10mm 30/40 Nm", "12mm 45/50 Nm"; spessori: "Anodizzazione dura 70 – 110 µm".
- Schede (esempi):
  - Top: "Ruota super leggera con cerchio in alluminio a doppia camera, 24 raggi acciaio neri Ø2mm, il mozzo Ø40 monta cuscinetti di precisione."
  - Dynamic Happy: "12 raggi in acciaio Ø3.5 rosso, blu, giallo, nero e bianco", "un'immagine divertente e gioiosa".
  - Dynamic-X: "esclusiva raggiatura mediante l'utilizzo di cavi in acciaio inossidabile intrecciato", 12 o 18 cavi.
  - Basket & Tennis: "un mozzo particolare che consente di inclinare la ruota fino a 20° gradi".
  - Beach: "Ruota studiata per la spiaggia, ma anche alle passeggiate in montagna."
  - Freno anti-ritorno: "con il nostro freno anti-ritorno potete solo andare avanti!!"
  - RAMPA#: "pensato per tutti coloro che non hanno abbastanza forza sulla braccia [...] dimezzare lo sforzo".
  - Golf wheel: "profilo sufficentemente largo per non bloccarsi nei BUNKER".
- Nessun elenco di macchine, nessun cliente nominato, nessuna fiera.

**Tecnologia**: ASP classico su IIS 10 e Plesk Windows, XHTML 1.0 Transitional, tabelle per l'impaginazione, jQuery 1.11.1 e 1.7.2 insieme, Lightbox, Google Analytics "UA-" (servizio dismesso), mappa Google incorporata nei contatti. `meta viewport` fisso a "width=994, initial-scale=0". HTTPS risponde, ma i link interni e la PEC sono in http. Il dominio treemmesrl.it porta a una pagina "Under Construction".

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, `prodotto-1440.jpg`, `azienda-1440.jpg`):
- Impianto largo 991 px a sinistra, fascia blu a destra, fondo grigio azzurro: aspetto 2011.
- La prima schermata è solo il logo "40 anni 1981-2021" dorato: non dice cosa fanno e non mostra una ruota.
- In testata convivono login dell'area riservata, bandiere, quattro link di servizio e un bollino "informazioni per l'acquisto".
- Le novità sono riquadri azzurri con testo maiuscolo blu e un URL nudo che esce dal riquadro.
- Le schede sono tabelle di 10 colonne con icone fucsia, foto da 210 px: le belle foto da 2000 px si vedono piccole.
- Azienda: foto della facciata che sembra presa da Street View, testo giustificato con asterischi Markdown rimasti nel testo ("**Emipligico Light**").
- Refusi: "Rehabilitazione", "Ruotea dischi", "Emipligico", "sabbiasi", "mantedendo".
- Il banner dei cookie copre il piede; nel guestbook ci sono due commenti di prova del 2014 ("prova outlink", "bellaaaaaaa").

**Problemi a 390** (`home-390.jpg`, `prodotto-390.jpg`): la pagina si disegna a 994 px e viene rimpicciolita, testo illeggibile, menu non toccabile, due terzi dello schermo vuoti.

**Igiene**: `sitemap.xml` contiene 39.973 indirizzi `list.php?page=...` che non esistono (oggi 404), traccia probabile di una vecchia intrusione con pagine spam; le pagine d'errore IIS dettagliate sono pubbliche (estratto in `_prova/crawl/sitemap-estratto.xml`). Da segnalare con tatto.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Tre Emme Manufatti S.r.l. | piede di ogni pagina: "Tre Emme Manufatti S.r.l." |
| P.IVA e CF | 00043870286 | piede: "P.IVA/C.F. IT00043870286"; aziende.it/tre-emme-manufatti-s-r-l: "Codice Fiscale 00043870286" |
| REA | PD-245090 | aziende.it (stessa pagina): "REA PD-245090" |
| Capitale sociale | 99.000 euro i.v. | piede: "Capitale Sociale €99.000,00 i.v." |
| Indirizzo | via Lombardia 23, 35020 Saonara (PD) | piede: "Via Lombardia n° 23 - 35020 Saonara (PD) Italy" |
| Telefono e fax | 049 8790210, fax 049 8791868 | piede: "Tel. +39 049 8790210 - Fax +39 049 8791868" |
| Email | info@3emme.com; laura.berto@, sara.berto@, manola.berto@3emme.com | piede e `contatti` |
| PEC | 3emme@cert.neispa.com | piede: "pec: 3emme@cert.neispa.com"; aziende.it: "PEC 3emme@cert.neispa.com" |
| Anno | fondata nel 1981; iscrizione al Registro Imprese 30/09/1993 | `azienda`: "nasce nel 1981"; aziende.it: "Data Iscrizione 30/09/1993" |
| Attività | ATECO 30.92.3, "Fabbricazione di veicoli per invalidi (incluse parti e accessori)" | aziende.it |
| Numeri | 15 dipendenti; fatturato 2024 3.688.625 euro (2022: 4.168.411); utile 2024 706.316 euro; 2.000 mq | aziende.it: "Anno Fatturato [...] 2024 € 3.688.625 [...] 15"; `azienda`: "superficie di 2.000 mq" |
| Persone | Gianfranco Berto (Direttore Generale), Laura Berto (acquisti), Sara Berto e Chiara Autunno (commerciale Italia ed estero), Manola Berto (amministrazione) | `contatti` |
| Contributi | 61.500 euro dal bando regionale 2021 "PMI a prevalente partecipazione femminile" | aziende.it, sezione aiuti di Stato (fonte RNA) |
| Orari | non pubblicati | |
| Social | solo un canale YouTube con due video | sez. 8 |

## 4. Materiale visivo

Ho scaricato 492 file (148 MB) in `assets/originali/`: tutte le immagini delle pagine IT (12 link rotti, 404). L'inventario con misure, pagine, soggetto e voti (qualità / forza come apertura, da 1 a 10) è in `_prova/inventario-immagini.json`; i 15 fogli provino numerati sono in `_prova/fogli/`. Video: due su YouTube (sez. 8), non scaricati.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Mozzo Dynamic-X con cavi inox intrecciati (`dynamiX-12-cavi-…`, `dynamiX-18-cavi-…`) | 2 | 2130 e 1914 px | 7 | 8 | il pezzo più bello: alluminio tornito e lucido, fori, cavi come gioielli. Fondo grigio chiaro da pulire |
| Ruote Dynamic Happy intere e mozzi con raggi colorati (blu, giallo, rosso) | 10 | 1860-2440 px | 7 | 7 | colore vero e ruota intera di tre quarti; segni di penna blu sul mozzo e luce da catalogo |
| Ruote FAT (cerchio giallo o nero con fori rossi, tassellato) | 5 | 1800 px | 7 | 7 | scontornate pulite, grafiche |
| Altri scatti da studio: ruote intere, mozzi, freni, forcelle, assi, boccole, tappi | circa 200 | 1500-3070 px | 6 | 4-5 | nitidi e coerenti, fondo bianco sporco non uniforme. Ottimi come catalogo e come seconde immagini |
| Macro di dettaglio (scritta Camel, attacchi del corrimano, cuscinetti) | circa 50 | 1200-2600 px | 6 | 5 | buone per una sezione "di vicino" |
| Camere d'aria e valvole | 6 | 4000x3000 | 5 | 2 | nitide, soggetto povero |
| RAMPA# e Jolly su telo stropicciato | 14 | 600-4032 px | 4 | 2-3 | luce di fortuna, pieghe sul fondo |
| Bici a tre ruote ed e-bike fotografate col telefono contro un muro | 16 | 460-1000 px | 3 | 2 | istantanee |
| Battistrada, profili di cerchio, disegni tecnici | circa 80 | 200-500 px | 4 | 1 | i profili "AS 23 / ETRTO 17" sono belle grafiche, ma piccole |
| Banner dello slider (Beach, Golf, Country, Fat "No limit", Rampa, cane "Why not") | 10 | 956x341 | 2 | 0 | collage con foto di repertorio di terzi |
| Squadra in officina "dal 1981 / since 1981 / team" (`FotoHQ_slide_manufatti.jpg`) | 1 | 714x253 | 3 | 2 | l'unica foto di persone e reparto: da rifare |
| Facciata dello stabilimento | 1 | 974x345 | 2 | 1 | sembra una cattura di Street View (targhe sfocate) |
| Clip-art (omini 3D, carrello sul portatile, cuscinetti su disegno), banner prevenzione | 8 | 300-1000 px | 1-2 | 0 | da eliminare |
| Loghi | 3 | 274x163 JPEG, favicon 184x184 | 3 | 0 | sez. 8 |

**Verdetto**: per il **prodotto** il materiale **regge** una home di alta gamma, voto medio 6, punte da 7 e 8 (mozzi Dynamic-X e Dynamic Happy, ruote FAT). Prima di usarle vanno scontornate o pulite sul fondo, e vanno tolti i segni di penna. Non c'è invece niente su persone, reparto, macchine e stabilimento: lì servono segnaposto (sez. 6). Per il sito vero servono una mezza giornata in reparto (torni, stampaggio del poliuretano, montaggio dei raggi, la famiglia Berto) e qualche foto d'uso con clienti veri e liberatoria.

## 5. Due direzioni artistiche

Graziella e N19 (`_metodo/ispirazione-graziella-n19.md`): non le uso. Tre Emme non è moda né lusso, e il registro giusto è quello dei componenti di precisione (meccanica fine, ciclismo di alta gamma), non quello della pelletteria; tengo solo l'idea generale di poche parole e tanta aria, che è già nella ricetta del committente.

**Direzione A, "Il mozzo" (chiara, un solo oggetto vero)**
- Idea visiva: su carta calda quasi bianca, il mozzo Dynamic-X (o una ruota Dynamic Happy blu) grande e nitido, scontornato, con ombra morbida vera e poche legende a filo sottile (mozzo Ø65x80, 12 cavi inox Ø2,5, corrimano ovale, cerchio doppia camera lega 6082), come la tavola di Mario Agnoletto. Titolo grande "Ruote per carrozzine, dal 1981" e sotto, piccolo, "Wheels for life!".
- Immagini: solo le loro, scontornate. Una sezione di tre famiglie (attive, elettroniche, poliuretano) con una ruota ciascuna su carta, una sezione "di vicino" con due macro.
- Tipografia: una grotesk netta e larga per i titoli (Switzer di Fontshare, o Schibsted Grotesk di Google), una mono piccola per codici e misure (IBM Plex Mono): il codice "T24A+S595P+AAL24" diventa un elemento grafico.
- Colore: carta #F4F3EF, inchiostro #15181D, blu del logo ripulito #0B3F94 come unico accento; il colore pieno arriva solo dai raggi (blu, giallo, rosso) e dai cerchi FAT.
- Gesto: "componi la ruota". Toccando cerchio, mozzo, corrimano o gomma cambia la variante sulla foto e il codice d'ordine si compone sotto (T24A, M41N, S595P, AAL24), con un bottone "Copia il codice". È il loro sistema di ordine reso visibile.

**Direzione B, "Ovunque" (chiara, fotografica e di vita)**
- Idea visiva: una sola grande foto luminosa di una persona in carrozzina all'aperto (segnaposto Kyra-Derksen sul lago o Virtuel al canyon), il titolo "Wheels for life!" o "Ruote per ogni terreno" sul cielo chiaro, la ruota giusta scontornata accanto come una didascalia.
- Immagini: segnaposto di vita all'aperto in luce naturale (da sostituire con clienti veri), più le loro ruote scontornate per terreno: Beach, Country, Golf, FAT, poliuretano per interni.
- Tipografia: una grotesk calda e umana (Cabinet Grotesk di Fontshare o Bricolage Grotesque di Google), testo in Instrument Sans, cifre tabellari per pollici e diametri.
- Colore: bianco caldo #F7F5F0, inchiostro #1A1C1E, verde lago smorzato #3E5A4C per i link, giallo FAT #F2C230 come accento raro.
- Gesto: selettore di terreno sobrio (Città, Spiaggia, Montagna, Prato, Interni): un clic cambia la ruota consigliata e due righe di scheda vere ("Ruota studiata per la spiaggia, ma anche alle passeggiate in montagna"), senza animazioni d'entrata.

Consiglio la **A**: mette al centro il prodotto vero e le loro foto migliori, e non ha bisogno di foto di persone che oggi non hanno.

## 6. Immagini sostitutive

Sette foto in `assets/esterne/`, lato lungo 2400 px, licenza verificata sulla pagina di ognuna (Unsplash License o Pexels License, nessuna Unsplash+), mai usate nelle altre home della campagna. Dettagli in `assets/CREDITI.md`.
- Persone, per la direzione B e per la chiusura: Kyra-Derksen (donna in carrozzina attiva sul lago, 8/10, apertura), Virtuel (Grand Canyon, 8/10), Centre for Ageing Better (uomo in città, 7/10), Knudsen (carrozzina elettrica davanti al mare, 6/10).
- Gesto e dettaglio: Marcus Aurelius su Pexels (mano sul corrimano, 7/10), McKoy (raggi in controluce, 6/10), De Grandi (mozzo su fondo arancio, 5/10, solo come riserva).
- Per la direzione A non servono foto esterne: l'oggetto è loro.
- Manca il reparto: non ho trovato foto libere decenti di torni o stampaggio del poliuretano, e comunque va fotografato il loro.

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/<nome>-1440.jpg` e `-390.jpg` (JPEG q78), caratteri letti dal codice in `<nome>.json`. Aperti dal vivo il 20/10/2026.

1. **Spinergy** (spinergy.com, ruote per carrozzine e bici).
   - Alta gamma: due foto vere a tutta altezza, una persona vera in carrozzina con raggi colorati e una in bici; una sola parola enorme per lato (Oswald 500) e un bottone. Il prodotto si vede in uso.
   - Da non riprendere: fascia nera e icone del negozio, scritte bianche sopra la foto, il tono da sport americano.
2. **Küschall** (kuschall.com, carrozzine attive svizzere).
   - Alta gamma: sotto il video, una carrozzina scontornata su bianco con il titolo "DRIVING PERFORMANCE" in grotesk larga e corsiva; testo in Titillium, molto bianco. È il più vicino alla direzione A.
   - Da non riprendere: il video di apertura (a 1440 resta un rettangolo nero finché non carica), il menu tutto in corsivo.
3. **Chris King** (chrisking.com, mozzi e componenti torniti, Portland).
   - Alta gamma: il mozzo arancio anodizzato in primo piano su una bici vera, profondità di campo corta, logo in Gotham. Dimostra che un mozzo può reggere una prima schermata.
   - Da non riprendere: titolo maiuscolo corsivo nero 900, finestra newsletter che si apre da sola sopra la foto, banner arancio "fake websites".
4. **Motion Composites** (motioncomposites.com, carrozzine in carbonio, Canada).
   - Alta gamma: foto luminosa e vera di ragazzi allo skatepark con la carrozzina in mezzo, DIN 2014 leggero in maiuscolo; sotto, colonne pulite con i marchi della casa.
   - Da non riprendere: il bottone rosso pieno, le colonne a riquadri, il titolo bianco sopra il cielo chiaro (si legge male).
5. **Campagnolo** (campagnolo.com, ruote e gruppi, Vicenza).
   - Alta gamma: un'azienda veneta di componenti che si presenta come un marchio di lusso; logo corsivo storico, DIN 2014, foto di movimento.
   - Da non riprendere: foto scurita con il velo, logo del prodotto in caratteri tecnici, troppe icone in testata.

Scartati, con gli screenshot in `riferimenti/scartati/`: Panthera (impianto datato con slider), ENVE (ripete Spinergy e Campagnolo), Batec Mobility (video e titolo centrato), progeo.it (oggi è un altro mestiere).

## 8. Per il piede

- **Logo**: esiste solo in raster. `assets/originali/logo-tre-emme-274x163.jpg` (mezza ruota a raggi grigia, mozzo con i colori della bandiera, asse azzurro, "Tre Emme Manufatti S.r.l." in blu #0A3F96 circa, "Wheels for life!" in corsivo rosso); `logo-favicon-184.ico` e `logo-marchio-184.png` (solo il marchio della ruota, 184x184). Il `favicon.ico` alla radice è l'icona di default di IIS (ingranaggi), non loro. Gli SVG ISO e Accredia contengono solo un PNG incorporato. Il JPEG da 274 px basta per un logo largo 137 px a 2x; il marchio a mezza ruota è geometrico e si può ridisegnare fedele in SVG, la scritta va chiesta in vettoriale (sembra un Ubuntu Bold, da verificare).
- **Menu e pagine di oggi**: Home, Prodotti (Rehabilitazione, Altre applicazioni), Azienda, Contatti, News, Promozioni; servizio: Come ordinare, Note tecniche utili, Condizioni di vendita, Privacy, Area riservata, Paga con carta di credito; Guestbook.
- **Colonne proposte**: Azienda (Chi siamo, Dal 1981, Qualità, News); Prodotti (Ruote a raggi attive, Ruote per carrozzine elettroniche, Ruote anteriori, Freni, Forcelle, Ricambi e poliuretano, Bici a tre ruote, Altre applicazioni); Per ordinare (Come ordinare, Note tecniche, Condizioni di vendita, Area riservata, Pagamento con carta); Contatti (telefono, email, indirizzo con mappa). Seguici: solo YouTube.
- **Social che esistono**: YouTube "Tre Emme Manufatti srl", https://www.youtube.com/@BIRBA0507 (video "RAMPA System" e "RAMPA# SYSTEM & ONEWAY BRAKES / FRENI ANTI-RITORNO", dati oEmbed). Facebook, Instagram e LinkedIn: non trovati. La notizia del 07/05/2021 cita "@WelfareCare", non un loro profilo.
- **Newsletter**: ha senso, in piccolo. Pubblicano novità di prodotto (12 notizie, l'ultima del 19/08/2023: e-bike, corrimano ovale, Dynamic Happy), hanno clienti privati oltre a rivenditori e produttori, ed esportano (commerciale "Italia&Estero", schede su medicalexpo.com). Proposta: "Novità dall'officina", poche uscite l'anno. Da collegare a un servizio; non funziona finché non si collega.
- **Riga legale**: Tre Emme Manufatti S.r.l., P.IVA e CF 00043870286, REA PD-245090, capitale sociale 99.000 euro i.v., PEC 3emme@cert.neispa.com, Privacy, Cookie.

## 9. Da confermare

- Anno: 1981 (fondazione) e 1993 (iscrizione al Registro Imprese, forse trasformazione in srl). La P.IVA così bassa fa pensare a una ditta precedente.
- ISO 9001: ente, numero e validità del certificato, e su quali prodotti di preciso. I loghi sono nascosti nel codice: è ancora valido?
- "Principale produttore di ruote per carrozzine per disabili in Italia": su che base lo dicono?
- Cosa producono in casa e cosa assemblano o comprano (cerchi, pneumatici Cheng Shin e Schwalbe, bici a tre ruote); quali macchine ci sono nei 2.000 mq.
- Clienti: produttori di carrozzine, ortopedie, privati? Si possono nominare? Esportano dove?
- Orari di apertura e se ricevono privati in sede.
- Il logo vettoriale e il carattere della scritta.
- I diritti delle foto dello slider (foto di repertorio di terzi) e la facciata da Street View.
- Le foto prodotto con "DA-RITOCCARE" o "DA-RIFARE" nel nome: c'è una versione ritoccata?
- La versione inglese (oggi errore 500) e se serve anche il tedesco.
- La sitemap con 39.973 indirizzi spam: va pulita, e va controllato il server.
- Il canale YouTube "@BIRBA0507" è proprio quello ufficiale?
- Dipendenti e fatturato vengono da aziende.it: da confermare sul bilancio.
