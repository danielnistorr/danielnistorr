# FM Sistemi Srl: analisi per la nuova homepage

Ricerca del 19 ottobre 2026. Ogni fatto ha la fonte; quello che non ha fonte sta in "Da confermare" (sezione 8).

**Avviso al committente.** FM Sistemi **non è** un fornitore della moda e della pelletteria: è un'impresa di impianti (elettrici, termoidraulici, clima, pompe di calore, fotovoltaico) e di ristrutturazioni. Sta nella zona artigianale di Vigonovo, accanto a pelletterie e calzaturifici (sulla mappa del suo sito compare Paraga Pelli nella stessa via), ma il mestiere è un altro. Le sezioni 5, 6 e 7 sono quindi costruite sul loro mondo vero, non su pelle e accessori metallici.

**Accesso al sito.** Il blocco "IIS 10.0 Detailed Error 999.0 - AW Special Error" non si è ripresentato: il 19/10/2026 `curl` (con e senza user agent da browser) e Chromium hanno ricevuto 200. `https://fmsistemisrl.it`, `http://www.` e `http://` rimandano tutti con 301 a `https://www.fmsistemisrl.it/`. Il blocco visto prima dipende probabilmente da IP o frequenza delle richieste.

## 1. In breve

- **Chi sono:** F.M. Sistemi S.r.l., Vigonovo (VE), via del Lavoro 37, zona artigianale.
- **Cosa fanno:** impianti elettrici e termoidraulici, ristrutturazioni edili, energie rinnovabili, "Dalla A alla Z" in un solo interlocutore (sito). Sono Viessmann Partner per pompe di calore e sistemi ibridi, climatizzatori, trattamento aria, fotovoltaico residenziale, mobilità elettrica, trattamento acqua e impianti commerciali (pagina partner Viessmann).
- **Per chi:** privati che ristrutturano o cambiano caldaia e clima, più aziende ("Impianti commerciali") e almeno un ente pubblico (un appalto da 44.956 euro, settembre 2024). Nessun cliente nominato in pubblico.
- **Dove:** Vigonovo, Riviera del Brenta, provincia di Venezia; telefono con prefisso padovano 049.
- **Da quando:** il sito è del settembre 2015; l'anno di fondazione va confermato (2004 secondo un aggregatore, vedi sezione 8).
- **Quanti:** 17 dipendenti, fatturato di circa 2,0 milioni di euro nel 2024 e nel 2025 (aziende.it).

## 2. Il sito di oggi

**Pagine.** Una sola pagina, `index.html`, statica. Il menu porta ad ancore interne (HOME, CHI SIAMO, CONTATTI). `/robots.txt`, `/sitemap.xml` e ogni altra pagina provata rispondono 404.

**Testi veri (verbatim, sono tutti qui):**
- titolo: "FM Sistemi Srl"
- unico titolo in pagina (h3): "**Dalla A alla Z** / Impianti elettrici e termo-idraulici, / ristrutturazioni edili e complementi, impianti energie rinnovabili."
- og:description: "Dalla A alla Z. Ristrutturazione impianti idraulici, elettrici, climatizzazione e riscaldamento."
- meta keywords: "impianti idraulici, idraulica, fotovoltaico, sicurezza, allarmi, elettrici, climatizzazione, riscaldamento"
- pulsante: "Seguici su Facebook"
- piede: "FM Sistemi Srl / Via del lavoro 37, 30030 Vigonovo (VE), Italia / P.IVA 03807720283 / Email: info@fmsistemisrl.it | commerciale@fmsistemisrl.it / Tel: +39 049 8305354 / © 2019 FM Sistemi Srl"

Non ci sono servizi descritti, prodotti, marchi, certificazioni, numeri, foto di lavori né persone. La partnership Viessmann non è citata.

**Tecnologia.** HTML statico costruito sul kit "Startup" di Designmodo (Flat UI, Bootstrap 3, jQuery 1.10.2), ospitato su Microsoft IIS 10 / ASP.NET. Ultima modifica del file: 31/10/2019 (intestazione `last-modified`). Meta author "Nicola Riparelli". Nel codice restano funzioni del modello mai usate (link a facebook.com/enbagetools e vimeo.com/uqido).

**Problemi a 1440** (`_prova/attuale/home-1440.png`, pezzi `home-1440-0/1.jpg`):
- l'apertura è una foto di repertorio con una pianta in inglese ("lobby", "W.C", "boiler"), martello e chiodi: dice "carpenteria generica", non "impianti", e non dice nulla di FM;
- sotto c'è solo una frase centrata in mezzo a 300 px di bianco, poi una fascia azzurro Facebook a tutta larghezza, poi una mappa Google alta 550 px: tre quarti della pagina sono riempitivo;
- Roboto è chiesto in `http://` e il browser lo blocca come contenuto misto: il testo esce in Helvetica/Arial;
- nessun h1, meta description vuota, logo con `alt=""`, nessuna informativa privacy o cookie, mappa con `pointer-events:none`.

**Problemi a 390** (`_prova/attuale/home-390.png`, pezzi `home-390-0/1.jpg`):
- la foto d'apertura si riduce a una striscia di 140 px;
- la frase va a capo male ("termo- / idraulici");
- `user-scalable=no` impedisce lo zoom, un problema di accessibilità;
- il telefono è in fondo, dopo la mappa: per chiamare bisogna scorrere tutta la pagina.

## 3. Dati aziendali con fonti

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | F.M. Sistemi S.r.l. | aziende.it, https://www.aziende.it/f-m-sistemi-s-r-l ("F.m. Sistemi S.r.l.", "SOCIETA' A RESPONSABILITA' LIMITATA"); pagina partner Viessmann ("F.M. SISTEMI S.R.L.") |
| P.IVA e codice fiscale | 03807720283 | sito, piede: "P.IVA 03807720283"; aziende.it |
| Indirizzo | Via del Lavoro 37, 30030 Vigonovo (VE) | sito: "Via del lavoro 37, 30030 Vigonovo (VE), Italia"; Viessmann: "Via del Lavoro - z.a. 37 30030 Vigonovo VE" |
| Telefono | +39 049 8305354 | sito: "Tel: +39 049 8305354" |
| Email | info@fmsistemisrl.it, commerciale@fmsistemisrl.it | sito, piede |
| PEC | fmsistemisrl@legalmail.it | aziende.it |
| Orari | "LUN SAB 8.30 - 19.00 / chiuso domenica" | https://fm-sistemi-srl.partner-viessmann.it/ |
| Specialità | "Pompe di calore e sistemi ibridi, Climatizzatori, Trattamento aria, Fotovoltaico residenziale, Mobilità elettrica, Trattamento acqua, Impianti commerciali"; servizi: "Installazione sistemi di riscaldamento e acqua calda sanitaria", "Installazione sistemi di condizionamento" | pagina partner Viessmann (screenshot in `_prova/crawl/viess.png`) |
| ATECO | 43.22.07 "Installazione di impianti di riscaldamento e di condizionamento dell'aria" | aziende.it; reportaziende.it, https://www.reportaziende.it/fm_sistemi_srl_ve_03807720283 |
| Dipendenti | 17 (2024 e 2025) | aziende.it |
| Fatturato | 2.030.159 euro (2025), 2.015.426 euro (2024), circa 2,5 milioni (2023), 2.443.945 euro (2021) | aziende.it; il 2023 da reportaziende.it |
| Utile | 43.498 euro (2025), 35.366 euro (2024), 92,9 mila euro (2023) | aziende.it; reportaziende.it |
| Appalti pubblici | 1, CIG B2F30D7E49, 12/09/2024, 44.956 euro (ente e oggetto non indicati) | aziende.it |
| Recensioni Google | 4,1 stelle su 13 recensioni | scheda Google Maps incorporata nel sito, visibile in `_prova/attuale/home-1440-0.jpg` |
| Facebook | pagina "FM-Sistemi-SRL-865904943478639" | link nel sito; il contenuto richiede il login e non è stato letto |
| Sito online dal | settembre 2015 | timestamp della mappa incorporata (1442141802322 = 13/09/2015) ed EXIF di header.jpg (13/09/2015) |

## 4. Materiale visivo

Scaricato in `assets/originali/`, inventario in `_prova/inventario-immagini.json`. Sul sito non c'è nessun video.

| File | Misure | Soggetto | Qualità | Forza in apertura |
|---|---|---|---|---|
| `header.jpg` | 1920x906 (EXIF 2480x1224) | foto di repertorio: pianta in inglese, martello, chiodi, metro | 6/10: nitida e pulita | 2/10: generica, in inglese, di un altro mestiere |
| `logo.png` | 480x80, solo raster | arco blu e "SISTEMI" in bastoni sottili | 4/10: niente vettoriale, fondo bianco | non è una foto |
| `favicon-192.png` | 192x192 | icona | 3/10 | non è una foto |

**Giudizio: 1/10. Il materiale non regge una home di alta gamma, e nemmeno una home normale.** Non c'è una sola foto loro: niente cantieri, locali tecnici, quadri, sede, furgoni o persone. L'unico segno proprio è l'arco blu del logo, che si può ridisegnare. La proposta deve stare in piedi su foto sostitutive dichiarate (sezione 6) e chiedere un servizio fotografico: 6-8 scatti di dettaglio su due cantieri bastano.

## 5. Il soggetto visivo

**Cosa del loro mondo regge un'immagine da rivista:**
- il **rame** brasato: curve, raccordi a T, la fiamma azzurra della brasatura, il colore che vira dal rosa al bruno;
- il **collettore in ottone** del riscaldamento a pavimento, con le spire dei tubi stese sull'isolante prima del massetto: un disegno grafico se visto dall'alto;
- il **quadro elettrico** cablato con cura: marrone, blu e giallo-verde pettinati in parallelo, le etichette scritte a mano;
- la **griglia della pompa di calore**, macro della ventola in controluce;
- i **moduli fotovoltaici** sui coppi veneti a luce radente;
- il **risultato invisibile**: una stanza a 20 gradi, la luce sul pavimento, nessun impianto in vista.

**Il dettaglio solo loro** è il "Dalla A alla Z": una sola impresa per elettricista, idraulico, muratore e rinnovabili, con un solo numero da chiamare. L'arco blu del logo (una curva di tubo, un orizzonte) può diventare il segno grafico di tutta la home.

**Direzione A: "Materia", l'atlante dei materiali**
- Idea: la home come un atlante. Ogni mestiere è un materiale fotografato da vicino, su un fondo quasi nero.
- Immagini: macro da still life con luce di studio (rame, ottone, cavi, griglia della pompa di calore); tagli stretti, mai un cantiere disordinato.
- Tipografia: grottesco netto in due pesi, per esempio Schibsted Grotesk o Inter Tight, con un monospazio (JetBrains Mono) per le sigle tecniche (kW, COP, classe).
- Colore: grafite #141414, rame #B87333 come luce delle foto, blu FM #046EA2 solo per l'arco e i collegamenti.
- Interazione: un indice A-Z sotto l'apertura. Si accendono solo le lettere che hanno un servizio vero (C clima, E elettrico, F fotovoltaico, P pompe di calore, R ristrutturazioni...); un clic cambia foto e riga di testo, senza animazioni allo scorrere.

**Direzione B: "Clima", la casa temperata**
- Idea: raccontare il risultato, non l'impianto. Una casa silenziosa, alla temperatura giusta, con l'impianto che non si vede.
- Immagini: interni architettonici in luce naturale (cemento, calce, parquet, sole radente), con un solo dettaglio tecnico per sezione.
- Tipografia: un serif editoriale per i titoli (Instrument Serif o Newsreader), un sans tranquillo per il testo, cifre grandi per gradi e kW.
- Colore: calce #F2EEE7, pietra #CFC6B8, ombra #2B2A28; il blu FM resta solo nel logo.
- Interazione: un selettore "Inverno / Estate" nell'apertura. Un clic cambia foto, il numero (20 gradi / 26 gradi) e la frase (riscaldamento / raffrescamento), con un taglio netto.

## 6. Immagini sostitutive

Otto foto Pexels scaricate a 2400 px in `assets/esterne/`. Licenza "Free" verificata sulla pagina di ogni foto. URL, autori e note sono in `assets/CREDITI.md`. Sono segnaposto da sostituire con foto vere, e il LEGGIMI lo dirà. Nessuna è generata dall'IA.
- **A:** `pexels-3721272` (raccordo in rame su nero, la più forte, 8/10 come apertura), `pexels-17072947` (cavi su nero), `pexels-20046689` (locale tecnico con pompa di calore, marchio concorrente: solo segnaposto), `pexels-29226620` (mani che montano un radiatore).
- **B:** `pexels-38344729` (stanza in cemento con sole radente, 8/10 come apertura), `pexels-35776702` (soggiorno con radiatore), `pexels-30440447` (fotovoltaico su coppi), `pexels-22133540` (riserva, debole).
- Scartata una foto "fotovoltaico" che sulla pagina risulta una serra.
- Mancano su Pexels: un collettore in ottone e un quadro elettrico ordinato. Sono i primi due scatti da chiedere all'azienda.

## 7. Riferimenti di alta gamma

Prima schermata a 1440x900 e 390x844 in `_prova/riferimenti/` (`<nome>-1440.png`, `<nome>-390.png`, affiancate in `coppia-<nome>.jpg`). Font letti dal codice (`document.fonts`, stile calcolato), dati in `<nome>.json`. Si sommano a Mobbin, non lo sostituiscono.

1. **Aira** (pompe di calore, sito italiano), https://www.airahome.com/it-it, `aira-1440.png`
   - Perché è di alta gamma: titolo enorme (94 px) in airaDisplay/airaText, tre righe a bandiera, bianco su nero; la foto è una macro della griglia della pompa di calore in luce color rame, la direzione A già fatta. A 390 tiene benissimo.
   - Da non riprendere: il badge Trustpilot, il pulsante arancio a pillola, il menu con cinque tendine.
2. **Quilt** (pompe di calore, USA), https://www.quilt.com/, `quilt-1440.png`
   - Perché è di alta gamma: Quilt Serif per il titolo e Quilt Sans per il testo; l'unità interna rivestita in legno dentro una casa vera; una citazione di stampa nella barra in alto come prova.
   - Da non riprendere: la scena posata con la persona e i fiori, i due pulsanti a pillola uguali.
3. **Buster + Punch** (interruttori e placche in metallo), https://www.busterandpunch.com/, `busterpunch-1440.png`
   - Perché è di alta gamma: macro di interruttori in ottone zigrinato su una parete scura, immagine divisa in due; museo-sans 900 maiuscolo spaziato. È la prova che un interruttore può essere un oggetto di lusso.
   - Da non riprendere: tre sovrapposizioni insieme (paese, cookie, chat) e la barra promozionale.
4. **Tubes Radiatori** (termoarredo italiano), https://www.tubesradiatori.com/it/, `tubes-1440.png`
   - Perché è di alta gamma: Radley (serif) a 96 px in maiuscolo con Barlow, fondo #222, pulsante con sfumatura cipria.
   - Da non riprendere: nel browser senza interfaccia l'apertura è rimasta vuota (video o carosello non caricato); frecce a quadrati neri; indicatore "Scorri".
5. **VOLA** (rubinetteria danese), https://www.vola.com/, `vola-1440.png`
   - Perché è di alta gamma: bagno in luce calda con rubinetto in ottone, ITC Avant Garde Gothic light, una frase centrata di quattro righe sotto la foto ("Since 1968..."); è la direzione B.
   - Da non riprendere: testo sottile bianco sulla foto, poco contrastato; i pallini del carosello.
6. **Basalte** (domotica e placche di lusso), https://www.basalte.be/en, `basalte-1440.png`
   - Perché è di alta gamma: Gilroy Light 45 px tutto minuscolo su nero, molto vuoto, l'architettura che entra dal basso.
   - Da non riprendere: il manierismo del minuscolo, il link "watch our love story" quasi illeggibile, il banner cookie centrale.

Visti e scartati: **Dornbracht** (`dornbracht-1440.png`: Helvetica Now, ma l'apertura è uno yacht fuori tema) e **tado** (`tado-1440.png`: immagine marcata "AI GENERATED" e video non caricato).

## 8. Da confermare

- Anno di costituzione (2004) e numero REA (VE 311085): vengono da un riassunto di ricerca, non letti su una fonte primaria. Serve la visura.
- ATECO: aziende.it e reportaziende.it dicono 43.22.07 (riscaldamento e condizionamento); un riassunto di ricerca citava 43.21.02 (impianti elettronici). Probabile cambio di codice con l'ATECO 2025.
- Secondo indirizzo "Via Padova 76, Vigonovo" e secondo telefono "049 9832336": compaiono solo in elenchi (Cylex, Pagine Gialle) non leggibili da qui (403).
- Fornitori, clienti e lavori di riferimento: nessuno è pubblico. Va chiesto se lavorano anche per le aziende della moda della zona (sarebbe un bel ponte, ma oggi non c'è prova).
- Certificazioni (F-gas, abilitazioni DM 37/08, SOA): nessuna fonte.
- Il "sicurezza, allarmi" delle meta keywords: è ancora un servizio?
- Titolari e soci: non pubblici sulle fonti gratuite.
- Licenza di `header.jpg` (foto di repertorio del 2015).
- Logo vettoriale e foto vere: da chiedere (collettore, quadro, rame, pompa di calore installata, un interno finito).
- Contenuto della pagina Facebook e foto su Google Maps: richiedono il login, non lette.
- Il blocco "999 AW Special Error" visto dal committente: non riprodotto il 19/10/2026.
