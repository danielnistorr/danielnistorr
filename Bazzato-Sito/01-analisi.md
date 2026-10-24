# Bazzato: analisi per la nuova home

Sito: https://www.bazzato.it (crawl e screenshot del 19/10/2026: home, 12 pagine della sitemap, blog). Fonti citate come URL + frase; le pagine del sito sono indicate con il percorso dopo `bazzato.it/`.

Nota sul blocco: il server (IIS 10) risponde "999" a chi si presenta come browser (`curl -A "Mozilla/5.0"` dà 999, 4,5 KB) e risponde 200 al curl normale. Il sito quindi si legge; gli screenshot sono stati fatti con Chromium dalle pagine scaricate e dal vivo.

## 1. In breve

- **Chi**: Bazzato snc di Bazzato Andrea e Paolo & C., autofficina in viale Serenissima 3, località Tombelle, Vigonovo (VE), "nella nuova zona artigianale" (`contatti.html`).
- **Cosa fa davvero**: è un'officina auto multimarca di paese, non un'azienda industriale. Tagliandi, meccanica, elettrauto con diagnosi, revisione in sede ("in 45 minuti", € 79), gomme, ricarica clima, batterie, assistenza GPL Landi, carrozzeria, vendita auto, auto sostitutiva. È un "Centro di Riparazione Eurorepar Car Service" (meta description della home) e si è sempre presentata come officina Opel (titolo di `tagliando…`: "Autorizzato Opel"; le schede di directory la chiamano "Opel Service"). Se il marchio Opel sia ancora attivo nel 2026 va confermato (sez. 8).
- **Per chi**: automobilisti privati della Riviera del Brenta, tra Padova e Venezia. Il sito parla in seconda persona, con prezzi, orari e WhatsApp.
- **Da quando, quanti**: la snc risulta fondata nel 2005 (companyreports.it), "Anzianità 21 anni" e 5 dipendenti (atoka.io). Fatturato non pubblico.
- **Il punto**: il registro giusto è quello di un servizio di fiducia, chiaro e onesto, non quello del lusso. La loro frase migliore è già sul sito: "Prezzi chiari, sconti chiari".

## 2. Il sito di oggi

**Pagine**: Home, Eurorepar (link esterno a eurorepar.it), Servizi (Gommista, Revisione auto, Tagliando, Ricarica Clima, Soccorso stradale), Batterie auto (Opel originale, QParts Start-Stop, Energy+, EVO), Contatti, Blog (4 articoli, l'ultimo del 26/3/2020), informativa privacy, pagina di ringraziamento.

**Testi veri essenziali (verbatim)**:
- Home: titolo h1 "Autofficina Bazzato a Vigonovo assistenza e diagnosi multimarca"; nella foto "Autofficina multimarca e vendita"; sotto il logo "Assistenza e Vendita Auto".
- Home, "ALCUNI DEI NOSTRI SERVIZI": "Tagliandi su tutte le auto", "Manutenzione rapida", "Elettrauto con diagnostico multimarca", "Ricarica e assistenza clima R134a", "Revisione in sede in 45 minuti", "Tester e ricarica batterie", "Assistenza Autorizzata GPL Landi", "Interventi sulla carrozzeria", "Vendita auto", "Vendita e assistenza gomme", "Assetto computerizzato", "Invio promemoria scadenza revisione", "Si accettano bancomat e carta di credito", "Noleggio auto sostitutiva", "Preventivi e resoconto dettagliato delle operazioni compiute", "Prezzi chiari, sconti chiari".
- Orari (home): "OFFICINA: da Lunedì al venerdì dalle 08.00 alle 12.00 e dalle 14.00 alle 18.00"; "UFFICI: da Lunedì al venerdì dalle 08.00 alle 12.30 e dalle 14.00 alle 19.00 venerdì chiusura ore 18"; "SABATO CHIUSO". In pagina c'è ancora "CHIUSO PER FERIE da giovedì 6 a venerdì 21 agosto compresi".
- Revisione: "REVISIONE AUTO IN SEDE € 79,00", "PRE-REVISIONE GRATIS", "E' possibile aspettare (circa 45 minuti)", "la prima revisione per un auto deve essere effettuata dopo 4 anni entro il mese di prima immatricolazione. Successivamente ogni 2 anni", "Potremo proporti subito e gratuitamente un preventivo per la riparazione!". Appuntamenti "primo appuntamento 09:00, ultimo appuntamento alle 11:00", "primo appuntamento 14:30, ultimo appuntamento 16:00".
- Tagliando: "La revisione non è il tagliando"; modulo di preventivo con targa, km, sigla motore.
- Gomme: "ampia gamma di gomme premium delle migliori marche", "PRONTI A CONFRONTARCI SUI PREZZI ANCHE AL TELEFONO!", prezzi "TUTTO COMPRESO: manodopera per il montaggio, materiale di consumo e valvole, equilibratura e contributo ambientale".
- Clima: "Dal 2017 tutte le auto nuove utilizzano per il climatizzatore solo gas R1234YF"; controllo e ricarica "circa € 70" (R134A) e "circa € 180" (R1234YF).
- Soccorso: per le Opel nei primi 2 anni "il servizio è gratuito 24 ore su 24, 365 giorni all'anno" tramite "Numero Verde 800 836063"; poi tre soccorritori della zona consigliati.
- Batterie: cartellini QParts da € 80 a € 185 "prezzo iva compresa, manodopera per montaggio esclusa"; Opel originali "GARANZIA 2 ANNI".
- Nessuna certificazione, nessun numero di auto, anni o persone. Le persone non compaiono mai: né Andrea né Paolo hanno una faccia sul sito.

**Tecnologia**: Incomedia WebSite X5 Pro 2022.3.7 (meta generator), file statici su IIS 10 / ASP.NET, ultima modifica della home 4 agosto 2026. Font Arial e Rajdhani; Facebook Pixel; mappa Google Maps incorporata in `contatti.html`; moduli di preventivo propri; link WhatsApp `wa.me/390499830115`. I link interni della sitemap sono ancora in http.

**Problemi a 1440** (`_prova/attuale/home-1440.jpg`, pezzi in `_prova/attuale/pezzi/`):
- L'apertura è una foto stampa della Opel Corsa-e con la scritta "Autofficina multimarca e vendita" sopra il cofano: un'auto in vendita, non l'officina.
- Sotto c'è un blocco centrato di orari in rosso e nero, con fasce "SABATO CHIUSO" e "CHIUSO PER FERIE" di agosto ancora in pagina a ottobre.
- La stessa foto della Corsa torna una seconda volta, enorme, a tutta larghezza.
- I servizi sono 16 righe centrate di testo piccolo; a destra due foto di repertorio, una con angoli stondati irregolari.
- Il banner dei cookie copre le righe centrali della prima schermata.
- Revisione (`revisione-1440.jpg`): titolo bianco sopra lo spaccato tecnico Opel, poi un buco bianco di circa 350 px dove il fondo si sposta; testi tutti centrati e spezzati a mano riga per riga.
- Batterie (`batteria-1440.jpg`): 3979 px di cartellini rossi, gialli e verdi su fondo nero, uno sotto l'altro.
- Non c'è un pulsante per prenotare: il telefono è in una fascia rossa e il CTA "A TUA DISPOSIZIONE ANCHE PER UNA CONSULENZA O UN PREVENTIVO" non è un link.

**Problemi a 390** (`home-390.jpg`, pezzi `home-390-0/1.jpg`):
- Il titolo sulla foto va su tre righe e copre l'auto; il banner dei cookie copre gli orari.
- Il menu è un hamburger rosso piccolo sotto il logo.
- Il telefono "Tel 049 9830115" è una fascia rossa ma il numero non è cliccabile come pulsante evidente.
- Pagina alta 2520 px, nessuno scorrimento orizzontale.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Bazzato snc di Bazzato Andrea e Paolo & C. (in sigla Bazzato snc) | piede di ogni pagina: "Bazzato snc di Bazzato Andrea e Paolo & C."; companyreports.it/bazzato-snc-di-bazzato-andrea-e-paolo-c-03599300278: "Ragione Sociale: BAZZATO SNC DI BAZZATO ANDREA E PAOLO & C. IN SIGLA BAZZATO SNC" |
| P.IVA e C.F. | 03599300278 | piede: "P.I. e C.F. 03599300278" |
| REA | VE 322146 | companyreports (stessa pagina): "il numero REA VE 322146" |
| Forma, ATECO | snc, 95.31.10 | companyreports: "SOCIETA' IN NOME COLLETTIVO", "Codice ATECO: 95.31.10 - Riparazione e manutenzione meccanica, elettrica ed elettronica di autoveicoli" |
| Indirizzo | viale Serenissima 3, 30030 Vigonovo (VE), località Tombelle | piede: "Viale serenissima, 3 - 30030 Vigonovo (VE)"; home: "Ci trovi a Vigonovo (VE) località Tombelle nella Zona artigianale Viale Serenissima 3" |
| Telefono e WhatsApp | 049 9830115 | piede: "049 9830115"; immagine e link WhatsApp "In contatto su whatsapp allo 049 9830115", `wa.me/390499830115` |
| Email | info@bazzato.it | piede: "info@bazzato.it" |
| PEC | non trovata | |
| Anno | 2005 | companyreports: "Fondazione 2005"; atoka.io/public/it/azienda/bazzato-snc-di-bazzato-andrea-e-paolo-c-in-sigla-bazzato-snc/5d08a8c04f4f: "Anzianità 21 anni" |
| Dipendenti | 5 | atoka (stessa pagina) indica 5 dipendenti (dato del fornitore, da confermare) |
| Stato | attiva | companyreports: "Stato Attività Attiva" |
| Rete | Eurorepar Car Service | home, meta description: "è un Centro di Riparazione Eurorepar Car Service"; eurorepar.it/riparatore-bazzato-snc-di-bazzato-andrea-e-paolo-vigonovo-11669.html: scheda "BAZZATO SNC DI BAZZATO ANDREA E PAOLO, Eurorepar car service", "0/5 (0 Recensione)" |
| Opel | "Autorizzato Opel" | titolo di `tagliando-preventivo-cambio-olio-code-82-insp.html`: "Tagliando e Assistenza multimarca, Autorizzato Opel"; local.motorionline.com/officine/veneto/venezia/vigonovo/14919/: "Bazzato.It Opel Service Autofficina Revisioni in Sede" |
| Pirelli | rivenditore autorizzato | misterimprese.it/veneto/venezia/vigonovo/autofficine-e-centri-assistenza/855523.html: "rivenditore autorizzato pirelli." (non detto sul sito) |
| GPL | assistenza autorizzata Landi | home: "Assistenza Autorizzata GPL Landi" |
| Social | Facebook | facebook.com/autofficina.bazzato.vigonovo.revisione.gomme, titolo "Autofficina Bazzato a Vigonovo, Revisioni, Gomme, Assistenza Multimarca"; follower non leggibili |
| Fatturato, superficie, numero di ponti | non trovati | |

## 4. Materiale visivo

Scaricati 63 file (circa 17 MB) in `assets/originali/`; inventario con misure, soggetto, provenienza e voti (qualità / forza come apertura, da 1 a 10) in `_prova/inventario-immagini.json`; fogli provino in `_prova/fogli/`. Nessun video.

| Gruppo | Quanti | Misure | Qualità | Apertura | Giudizio |
|---|---|---|---|---|---|
| Vano motore di una Corsa a benzina, da telefono (`BAZZATO-OFFICINA-OPEL-VIGONOVO`, `BATTERIE-AUTO-…`) | 2 | 3984x1625, 2016x1134 | 5 | 3 | le uniche foto loro di lavoro: nitide ma piatte, HDR da telefono, etichette ovunque |
| Facciata della sede con insegna Eurorepar (scheda Eurorepar) | 1 | 640x480 | 5 | 2 | l'unica foto vera del luogo: piccola, storta, ma dice "siamo qui" |
| Foto stampa Opel: Corsa-e, Grandland X, Insignia, spaccato, motore | 7 | 272-2048 px | 7-8 | 1-2 | belle ma non sono loro né l'officina, diritti Opel |
| Campagna Opel "tagliando", batteria Opel, filtri | 3 | 709-1434 px | 5-6 | 1 | materiale del marchio |
| Repertorio: F1 al pit stop, mani col portatile, triangolo, ragazza in autostop, pulsante start | 5 | 420-1280 px | 3-4 | 0 | fuori registro |
| Cartellini prezzo QParts, banner caratteristiche, grafiche clima (offerta giugno 2021) | 22 | 524-1088 px | 3 | 0 | grafiche promozionali, alcune scadute |
| Biglietti dei soccorritori, schema clima, miniature blog | 8 | 300-1043 px | 2-3 | 0 | da non usare |
| Logo (scritta su fascia azzurra #00C3EF con 4 icone), divisori, WhatsApp, favicon | 15 | | 1-4 | 0 | logo solo raster: serve il vettoriale |

**Verdetto**: il materiale **non regge** una home di alta gamma: in media 3 su 10. Non c'è una foto dell'officina dentro, del ponte, delle persone o di un lavoro fatto bene; il meglio è materiale Opel che non è loro. Per la proposta servono i segnaposto della sez. 6. Per il sito vero serve mezza giornata di foto: l'officina vuota e pulita al mattino con un'auto sul ponte, un oggetto singolo su fondo chiaro (disco freno nuovo, gomma nuova), mani al lavoro, la linea revisione, i due titolari, la facciata dritta.

## 5. Due direzioni artistiche

**Le ispirazioni del committente** (Pelletteria Graziella, Studio N19, prime schermate aperte il 19/10/2026): Graziella è nero pieno con una serif enorme e parole in corsivo, cioè il registro della pelletteria per le maison e per di più con il corsivo d'accento vietato; per un'officina di paese è fuori luogo e non la uso. Di Studio N19 prendo solo un tratto: il titolo grande e sicuro in grotesk su fondo chiaro con tanta aria. Niente sfocature animate, niente parole che si muovono. Il soggetto non è moda né lusso, quindi l'alta gamma qui è chiarezza, ordine e una foto vera fatta bene.

**Direzione A, "Prezzi chiari" (chiara, un oggetto)**
- Idea visiva: fondo bianco caldo, un solo oggetto vero grande e nitido al centro (un disco freno nuovo o una gomma nuova fotografati in studio sul bianco), titolo "Prezzi chiari, sconti chiari." accanto, sotto solo telefono e orario di oggi.
- Immagini: still life su fondo chiaro con ombra morbida; poi una sola foto larga dell'officina luminosa con un'auto sul ponte. Segnaposto: Mclean disco forato, Bélanger bussole, Razumov officina chiara (solo come luce), Yvette S battistrada.
- Tipografia: Archivo (Google Fonts, OFL) con l'asse di larghezza, titoli in Expanded 700, testo 400; IBM Plex Mono (Google Fonts, OFL) piccolo per prezzi, orari e targhe.
- Colore: carta #F6F4EF, inchiostro #151515, grigio cemento #8C8A85, un solo accento: il rosso segnaletico del sito attuale (#C00000) per il telefono e la revisione.
- Gesto: "Quando scade la tua revisione?": scegli mese e anno di immatricolazione o dell'ultima revisione e la pagina risponde con il mese di scadenza, con le regole che sono già sul loro sito (4 anni, poi ogni 2) e un link per chiamare.

**Direzione B, "Il ponte" (luminosa, documentaria)**
- Idea visiva: l'officina vera come protagonista: una foto larga, chiara e dritta dell'officina vuota al mattino con un'auto alzata sul ponte, titolo grande in basso "Officina multimarca a Tombelle.", poi poche sezioni come le pagine di un registro di lavoro.
- Immagini: reportage onesto in luce naturale (ponte, mani, ruote, la linea revisione, i titolari), niente auto da depliant. Segnaposto: Razumov officina, Masth mani sulla gomma, Brunner disco e pinza, wal_ gomme impilate.
- Tipografia: General Sans (Fontshare, ITF Free Font License) per titoli e testo; i numeri grandi (45 minuti, € 79, 08.00) in cifre tabellari dello stesso carattere.
- Colore: grigio cemento chiaro #E9E8E4, bianco, nero #111, accento l'azzurro del loro logo #00C3EF usato solo per lo stato "aperto ora".
- Gesto: una riga di stato in testata, "Aperto, chiude alle 12.00" o "Chiuso, riapre alle 14.00", calcolata dagli orari reali dell'officina, con il numero cliccabile accanto.

Entrambe: 5 sezioni (apertura, servizi in righe pulite con il prezzo dove c'è, revisione, l'officina e le reti Eurorepar/GPL Landi, dove siamo e orari), pagina alta circa 5000 px a 1440. Niente tre box con icone, niente slider.

## 6. Immagini sostitutive

Otto foto in `assets/esterne/` (6 Unsplash, 2 Pexels), 2400 px di lato lungo, licenza letta sulla pagina di ogni foto, mai usate in un'altra home della campagna; URL, autori e licenze in `assets/CREDITI.md`. Sono segnaposto e il LEGGIMI dovrà dirlo; nessuna è generata dall'IA.
- A, apertura provvisoria: Mclean, disco forato su scocca chiara (`EpT-ZetoKm8`). Altre per A: Bélanger bussole cromate, Yvette S battistrada.
- B, apertura provvisoria: Razumov, officina bianca con auto sul ponte (`pexels-33814736`), con la scritta "SKODA" sul portellone: va rifatta comunque. Altre per B: Brunner disco e pinza, wal_ gomme impilate, Buehner mani nel motore.
- Comuni: Masth mani che montano una ruota.
- Scartate perché con marchi in primo piano: ruote Toyota/Bridgestone di Mclean, pinza Brembo di Hall, officina Nissan di Chen.
- Manca, e solo loro possono darla: la facciata dritta, i titolari, la loro linea revisione.

## 7. Riferimenti di alta gamma nel mestiere

Prime schermate a 1440 e 390 in `riferimenti/` (JPEG 78), aperte dal vivo il 19/10/2026.

1. **Lunaz** (lunaz.design, restauro ed elettrificazione di auto classiche, Silverstone).
   - Alta gamma: tre auto vere in uno studio grigio chiaro, luce morbida, un titolo corto "Timeless." in basso a sinistra, menu piccolo in maiuscolo. È la ricetta "un oggetto vero, chiaro, tanta aria".
   - Da non riprendere: il corsivo d'accento "By Design." e il sito costruito su Wix che a 390 taglia le auto.
2. **Kalmar Automotive** (kalmarautomotive.com, officina danese di restomod).
   - Alta gamma: una sola auto in un capannone buio con la luce delle finestre, nessun testo oltre al logo e a "Start Exploring". Dimostra che l'officina stessa può essere la scenografia.
   - Da non riprendere: il nero totale (qui il committente lo boccerebbe) e il pulsante a pillola vuoto.
3. **Alfaholics** (alfaholics.com, specialisti Alfa Romeo: officina, ricambi e restauro).
   - Alta gamma: foto vera e luminosa di una Giulia in strada, il mestiere detto senza giri; è un'officina, come Bazzato, che vende anche servizio e ricambi.
   - Da non riprendere: la fascia blu "OUR LATEST PRODUCTS" con il "New" in trasparenza, il condensato maiuscolo e il menu a 8 voci.
4. **Polestar** (polestar.com/it, marchio auto: preso per il registro dei testi e della tipografia).
   - Alta gamma: un'auto chiara, titolo corto e due righe, due pulsanti con contorno sottile, carattere proprietario sobrio, testo in italiano diretto.
   - Da non riprendere: la foto scura di costa (è pubblicità di prodotto, non servizio) e la barra promozionale in alto.

Scartati: Singer, Canepa, Tuthill (bloccano i browser automatici), Kaege (è un concessionario Mazda), Garage Italia ed Everrati (video non caricato), Pirelli, Brembo, RUF e Theon (apertura nera o vuota dietro i cookie), Mechatronik (slider vuoto), Fixter (viola e blu con box e icone: è proprio ciò che il committente vieta).

## 8. Da confermare

- Se Bazzato è ancora officina autorizzata Opel nel 2026 o solo Eurorepar (Eurorepar è una rete multimarca di Stellantis; il sito usa ancora loghi e materiale Opel).
- "Vendita auto": nuove, usate, di quale marca?
- Rivenditore autorizzato Pirelli: lo dice solo misterimprese, non il sito.
- Prezzi ancora validi: revisione € 79, clima "circa € 70" e "circa € 180", batterie da € 80 a € 185 (le grafiche clima citano un'offerta di giugno 2021).
- Le chiusure per ferie da togliere o da gestire in automatico.
- Dipendenti (5 secondo atoka), anno 2005 (companyreports), PEC: non verificati in visura.
- Chi sono Andrea e Paolo e se vogliono comparire in foto.
- Il servizio di carrozzeria è interno o affidato fuori?
- Il logo vettoriale e se il cliente vuole tenere le quattro icone.
- I diritti delle foto Opel, QParts e dei biglietti dei soccorritori.
- Il numero verde Opel Assistance "800 836063" è ancora valido.
