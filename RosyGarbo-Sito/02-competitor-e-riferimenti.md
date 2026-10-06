# 02. Concorrenti e riferimenti di design

Ricerca dal vivo del 6 ottobre 2026. Ogni sito è stato aperto con Playwright (Chromium, 1440 e 390 px di larghezza),
con screenshot a pagina intera e ritagli dei pezzi da riprendere:

- concorrenti: `_prova/ricerca/<nome>-1440.png` e `<nome>-390.png`;
- riferimenti: `_prova/ricerca/premium/<nome>-1440.png` e `<nome>-390.png`;
- ritagli: `_prova/ricerca/ritagli/*.jpg` (i nomi dicono il gesto: `frankel-02-fascia-spaziata-e-dittico.jpg`);
- script: `_prova/script/scatta.js` (pagina intera), `ritaglia.js` (finestra su un punto preciso), `ritagli.py`, `contrasto.py`.

Visitati 6 siti di concorrenti e 22 siti di riferimento. Non valutabili quel giorno:
Giuseppe Papini (errore del server ASP.NET "The network path was not found"), Monique Lhuillier, Jenny Packham,
Vera Wang, Carlo Pignatelli, Emilia Wickstead, Luisa Beccaria e Venini (verifica anti-robot Cloudflare),
Galia Lahav (accesso negato), Antonio Riva e Alessandra Rinaudo (non raggiungibili attraverso il proxy);
aimee.it oggi è un blog che non c'entra con l'atelier.
Dove l'apertura di un sito è un video, Chromium di prova spesso non lo riproduce (non ha i codec proprietari):
quelle fasce risultano vuote negli screenshot e non sono state giudicate, salvo quando manca anche un'immagine di riserva.

**Il materiale di partenza di Rosy Garbo**, che decide cosa ha senso riprendere (dettagli in 01):
- 16 fogli della collezione New York e 23 della collezione Villa Contarini, doppie pagine di catalogo da 1125x800 px:
  ogni metà è una foto verticale di circa 562x800 px, oppure una pagina col logo su fondo **nero (#000000, New York)**
  o **argento (#C5C6C8, Villa Contarini)** (`ritagli/rosygarbo-00-catalogo-pagina-nera-e-argento.jpg`);
- foto in esterni veri: strade e tetti di Manhattan (a colori e in bianco e nero), saloni affrescati di Villa Contarini;
- sei testate di collezione da 450x140 px (New York, Villa Contarini, Milano, Venezia, Padova, Messico) con il nome
  in un **senza grazie sottile maiuscolo**;
- il logo: "rosyGarbo" in un **carattere con grazie**, sopra tre filetti verde, bianco, rosso (#39AB49, #F0F0F0, #FF0000).

Le foto sono di buona qualità ma piccole: nessuna può andare a tutto schermo a 1440 senza essere ingrandita.
È il vincolo più importante per il design, e i riferimenti scelti qui sotto mostrano tutti le foto alla loro misura.

## 1. Concorrenti

| # | Concorrente | Zona | Cosa vende | Cosa fa meglio di Rosy Garbo oggi | Cosa fa peggio | Prove |
|---|---|---|---|---|---|---|
| 1 | [Atelier Veronica](https://atelierveronica.com/) | Padova, Viale Felice Cavallotti 24 | sartoria sposa e cerimonia, noleggio, su misura | sito che funziona a 390 px; indirizzo, telefono e "Prenota appuntamento" in home; P.IVA nel piè di pagina | email su gmail.com; menu a tendina anche a 1440 (solo icona); a 390 la scritta "Matrimonio Civile \| Secondo Look" va su tre righe e tocca i bordi del riquadro, il fumetto WhatsApp copre la foto "Abiti da Sposa"; tre riquadri con testo in Cormorant sopra la foto | `veronica-1440.png`, `ritagli/conc-veronica-01..02` |
| 2 | [Creazioni Mani di Fata](https://www.creazionimanidifata.it/) | Limena (PD) | atelier alta moda sposa | due premi di matrimonio.com in vista | fatto con WebSite X5; nella nostra cattura a 1440 il menu compare due volte come elenco di link blu non formattati; testi in corsivo calligrafico (Great Vibes) su foto; fondo azzurro | `manidifata-1440.png`, `ritagli/conc-manidifata-01-telefono.jpg` |
| 3 | [Fausto Sari](https://faustosari.com/) | Ponte di Piave (TV), "dal 1988" | atelier sposa e sposo: linee proprie e marchi di altri | collezioni come navigazione con il conteggio ("14 abiti"); modulo per il catalogo con data del matrimonio; orari completi con stato "Chiuso, riapre domani alle 9.00"; due porte "Sposa / Sposo" | è soprattutto un rivenditore (16 collezioni, tra cui Rosa Clará ed Elisabetta Polignano); Playfair Display su fondo nero; contatori che invecchiano ("38 anni di storia"); apertura con video YouTube che senza consenso lascia la scritta "YouTube non disponibile" sotto il titolo | `faustosari-1440.png`, `ritagli/conc-faustosari-00..02` |
| 4 | [Elisabetta Polignano](https://www.elisabettapolignano.com/) | Oleggio (NO) | griffe sposa con produzione propria e rete di negozi | **stesso modello di Rosy Garbo**: tre linee con foto e nome sotto; barra in alto "Sei un rivenditore? Registrati o Accedi" e "Stores & flagship"; modulo appuntamento con data delle nozze e città | apertura vuota per circa 650 px a 390 (video); Mukta e Roboto; finestra cookie al centro della pagina | `polignano-1440.png`, `ritagli/conc-polignano-01..02` |
| 5 | [Peter Langner](https://www.peterlangner.com/) | Milano, atelier in Via Bigli 19 | griffe sposa e sera, sartoria a Milano | **mostra la rete all'estero**: schede "Trunk Show" con negozio, date, indirizzo e telefono (Dallas, New Jersey, Florida) | testo bianco su beige #E1CAB6 nel modulo: contrasto 1,6:1; a 390 la home è lunga 14.020 px; recensioni a stelle; citazione d'apertura con una delle parole di `PAROLE_VIETATE`; alla seconda visita una verifica anti-robot | `langner-1440.png`, `ritagli/conc-langner-01..02` |

Tutti e cinque, a 390 px, hanno `scrollWidth` uguale alla finestra (390). Il sito di Rosy Garbo misura 990 px
a 390: su telefono è l'unico dei sei che non si legge.

**Cosa fanno i migliori:** linee o collezioni come prima navigazione, con foto e nome; appuntamento con la data
delle nozze; indirizzi e orari concreti; la rete di vendita mostrata (Langner, Polignano).

**Cosa non fa bene nessuno (spazio per Rosy Garbo):**
1. **dire dove si produce e come.** Rosy Garbo ha già il testo: "La produzione viene completamente eseguita nella sede
   veneta [...] I ricami e le applicazioni sono realizzate a mano". Fausto Sari e Atelier Veronica vendono soprattutto
   collezioni di altri; Langner lo dice in una riga;
2. **collezioni legate a un luogo vero.** New York e Villa Contarini sono servizi fotografici sul posto; i concorrenti
   usano foto di studio o le campagne dei marchi che rivendono;
3. **la rete internazionale.** Rosy Garbo elenca atelier e rivenditori a New York, Atene, Salonicco, Berlino,
   Budapest, Città del Messico, Mosca e Dubai (elenco fermo alla copia del 2020: [DA CONFERMARE]). Solo Langner fa
   qualcosa di simile. Nota: nella pagina "Meet the Designers" di Kleinfeld (scaricata il 6/10/2026) il nome Rosy Garbo
   non compare nel sorgente; l'elenco potrebbe essere caricato via script, quindi la verifica non è conclusiva;
4. **una tipografia propria.** I concorrenti usano Playfair Display (Fausto Sari, Langner), Cormorant (Veronica),
   Great Vibes (Mani di Fata), Mukta e Roboto (Polignano). Il nuovo sito non userà nessuno di questi caratteri.

**Copy evitato** (visto nei concorrenti): "Dove il sogno prende forma", "Il tuo Sì comincia da qui", "Libera di essere
ciò che sei", "abito dei tuoi sogni", "da oltre trent'anni" come contatore (si scrive l'anno, se confermato),
la citazione d'apertura di Langner, "Premium quality". Anche "sognamo le vostre idee", la frase del logo attuale,
resta solo dentro il logo: non diventa un titolo.

## 2. Riferimenti premium

Rosy Garbo disegna e produce abiti da sposa, da cerimonia e di alta moda e li vende nei suoi atelier e attraverso
rivenditori, anche all'estero. I riferimenti giusti sono quindi **maison sposa che producono e vendono tramite negozi**,
più una casa veneziana di artigianato d'arte, perché è l'azienda stessa a scrivere che le sue linee sono "ispirate alle
bellezze artistiche dei palazzi veneti ed alla cultura e tradizione veneziana, con qualche richiamo anche all'antica arte
vetraria di Murano". Nessuna casa di moda generica, nessun sito d'albergo o di gioielli.

### 2.1 Danielle Frankel Studio, New York
[daniellefrankelstudio.com](https://www.daniellefrankelstudio.com/). Abiti da sposa "made to order in the Garment District
of New York", due sedi (New York e Los Angeles).

- **Misurato:** un solo carattere con grazie, dritto e leggero (Canela Light), titoli a 28 px grigio #575757, menu
  in maiuscolo da 14 px con spaziatura 1,5 px; fondo #F8F8F4.
- **Gesto da riprendere:** la foto verticale **mostrata alla sua misura dentro un campo pieno**, non allargata a tutto
  schermo: in apertura un ritratto di circa 548x685 px centrato su una fascia piena; poi un **dittico**, metà pagina con
  la foto a filo e l'altra metà con una foto di 576x720 px incorniciata nel campo. Le sezioni si separano con una fascia
  sottile e un'etichetta in maiuscolo spaziato. Le sedi: per ognuna una riga sola sopra la foto
  ("NEW YORK 260 West 39th Street, 14th floor...") e sotto un link sottolineato "Book an Appointment".
- **Per Rosy Garbo:** è la soluzione onesta per foto da 562x800 px. Il dittico rifà il loro catalogo: una metà foto,
  l'altra metà campo nero (New York) o argento (Villa Contarini). Le sedi alla Frankel servono per Padova e Cona.
- **Da evitare:** la finestra newsletter all'apertura; la carta calda e virata (con gli abiti bianchi tira al crema);
  testi lunghi da 14 px grigi e centrati; la spaziatura estrema delle lettere ("C O L L E C T I O N").
- **Ritagli:** `frankel-01-apertura-foto-incorniciata.jpg`, `frankel-02-fascia-spaziata-e-dittico.jpg`,
  `frankel-03-due-sedi-indirizzo-sopra-foto.jpg`, `frankel-04-telefono.jpg` (a 390 il dittico diventa foto a filo
  e poi foto incorniciata, una sotto l'altra, senza perdere il margine).

### 2.2 Laure de Sagazan, Parigi
[lauredesagazan.com](https://www.lauredesagazan.com/). Maison di abiti da sposa su misura, "Entreprise du Patrimoine
Vivant", tutte le collezioni fatte nell'atelier di Parigi.

- **Misurato:** Jost (geometrico, famiglia Futura) per testo e menu, 17 px con spaziatura 0,6 px; fondo crema #F9F7EF.
- **Gesto da riprendere:** **tre capi in fila a filo**, senza spazio tra le foto, con il nome in maiuscolo piccolo sotto
  ognuna; poi coppie di foto affiancate che mescolano colore e bianco e nero, con un'etichetta sotto ciascuna.
  Il testo sulla produzione è diviso in paragrafi con sottotitolo in grassetto ("Robes de mariée sur-mesure",
  "Fabriquées en France", "Des tissus luxueux").
- **Per Rosy Garbo:** la pagina sul marchio si costruisce così, con le loro frasi divise per tema (tessuti italiani,
  ricami e applicazioni a mano, produzione nella sede veneta). La mescolanza colore e bianco e nero c'è già nella
  collezione New York.
- **Da evitare:** l'apertura affidata solo a un video: nella nostra cattura a 1440 restano circa 1.900 px di fondo vuoto, con due soli
  pulsanti, prima della prima foto: il video non parte e non c'è un'immagine di riserva; il fondo crema; il corsivo con grazie
  nel titolo della newsletter; il testo lungo centrato.
- **Ritagli:** `sagazan-01-tre-capi-nome-maiuscolo.jpg`, `sagazan-02-testo-fabbricato-in-atelier.jpg`.

### 2.3 Rime Arodaky, Parigi
[rimearodaky.com](https://www.rimearodaky.com/). Maison di abiti da sposa con atelier e archivio.

- **Misurato:** Cormorant e Amiri su fondo #F3F2EC.
- **Gesto da riprendere:** **quattro look in fila**, foto verticali unite senza spazio, tutte sullo stesso muro di
  studio, con il nome del modello in maiuscoletto da 10-11 px sotto, allineato a sinistra. Lo stesso fondo in tutte le
  foto fa leggere la fila come una collezione.
- **Per Rosy Garbo:** le 23 foto di Villa Contarini e le 16 di New York sono già serie con un fondo comune (i saloni
  della villa, le strade di Manhattan): file di quattro, con didascalia piccola. I nomi dei modelli non sono pubblici:
  [DA CONFERMARE] con l'azienda; fino ad allora la didascalia è il nome della collezione.
- **Da evitare:** proprio l'accoppiata Cormorant e fondo crema, che è il cliché bocciato; pulsanti a contorno sottile
  con testo chiaro sopra la foto (quasi illeggibili in apertura).
- **Ritaglio:** `arodaky-01-quattro-look-con-nome.jpg`.

### 2.4 Jesus Peiro, Spagna
[jesuspeiro.com](https://www.jesuspeiro.com/). "Redefining Bridal Couture since 1988" (dal sorgente della pagina):
abiti da sposa fatti in Spagna, boutique monomarca, negozi multimarca e presenza internazionale. È il modello più
vicino a Rosy Garbo (attiva dal 1989, produzione in Veneto, atelier monomarca e rivenditori).

- **Misurato:** Franklin Gothic in maiuscolo spaziato per i titoli (42 px, spaziatura 0,1 em); testo da 12 px grigio
  #817A72, contrasto 4,23:1.
- **Gesto da riprendere:** il blocco **"Tu tienda de vestidos de novia más cercana"**: foto in bianco e nero di un
  negozio a sinistra, titolo maiuscolo a destra, tre righe di testo e un link sottolineato "Conocer puntos de venta".
  Nel piè di pagina una colonna per i professionisti ("Conviértete en distribuidor", "Acceso B2B").
- **Per Rosy Garbo:** un blocco "Dove trovare Rosy Garbo" che porta alla pagina degli atelier; nel piè di pagina una
  riga per i rivenditori con l'email esistente, solo se l'azienda vuole ancora nuovi rivenditori [DA CONFERMARE].
- **Da evitare:** le **tre icone in fila** "Made in Spain / Established in 1988 / Premium quality" (divieto di METODO §3);
  l'apertura affidata a un video Vimeo, che nella nostra cattura mostra al suo posto la pagina d'errore "We couldn't
  verify the security of your connection"; il testo da 12 px a 4,2:1.
- **Ritagli:** `peiro-01-blocco-punti-vendita.jpg`, `peiro-02-tre-icone-da-evitare-e-area-professionisti.jpg`.

### 2.5 Marchesa, New York
[marchesa.com](https://www.marchesa.com/). Abiti da sera e da cerimonia in due linee (Marchesa Notte, Marchesa Rosa).
Serve per la parte "cerimonia e alta moda" di Rosy Garbo.

- **Misurato:** Cormorant per i titoli, Jost per menu e didascalie; foto prodotto su fondo grigio chiarissimo, nome in
  due righe sotto.
- **Gesto da riprendere:** **le linee come schede**: due nomi affiancati, quello attivo sottolineato, che cambiano la fila
  di abiti sotto. Poi le due linee affiancate a metà pagina, ognuna con foto, nome, un paragrafo breve e un link piccolo.
  In apertura un servizio di strada a New York a colori: lo stesso tipo di foto della collezione New York di Rosy Garbo.
- **Per Rosy Garbo:** le tre linee del menu attuale (moda sposa, alta moda, arte; le ultime due oggi danno 404) possono
  diventare schede di questo tipo. Il contenuto delle linee alta moda e arte va chiesto all'azienda [DA CONFERMARE].
- **Da evitare:** saldi, codici sconto e riquadri promozionali; il nome della linea scritto sopra il viso della modella;
  le frecce del carosello sopra le foto.
- **Ritagli:** `marchesa-01-schede-delle-due-linee.jpg`, `marchesa-02-due-linee-affiancate.jpg`.

### 2.6 Fortuny, Venezia
[fortuny.com](https://www.fortuny.com/). Tessuti d'arte "handmade in Venice since 1921" nella fabbrica della Giudecca.
È il settore vicino che l'azienda stessa indica (tradizione veneziana, palazzi veneti).

- **Misurato:** un solo senza grazie (Atlas Grotesk) a 16 px con spaziatura 0,06 em; menu in maiuscolo spaziato;
  fondo #F8F8F8, testo nero (19,8:1).
- **Gesto da riprendere:** **la scheda**: foto, nome (un luogo: Giudecca, Archipelago, Laotze), una riga di descrizione,
  e sotto un codice in piccolo grigio spaziato. Titoli di sezione piccoli e calmi, con l'origine detta in una frase
  ("From Giudecca, with love": la fabbrica originale sull'isola della Giudecca).
- **Per Rosy Garbo:** anche qui le collezioni portano nomi di luoghi (New York, Villa Contarini, Venezia, Padova, Milano,
  Messico). Scheda collezione = foto, nome del luogo, una riga su dove è stata fotografata, numero di foto contate dal
  catalogo; nessun codice inventato. Una frase sola sull'origine: la sede veneta dove si produce.
- **Da evitare:** pulsanti verde scuro ed etichette "NEW" turchesi (non sono di Rosy Garbo); il logo esteso; immagini
  che arrivano sfocate e restano tali se si scorre in fretta (successo nella prima cattura).
- **Ritagli:** `fortuny-01-nome-descrizione-codice.jpg`, `fortuny-02-dalla-giudecca-quattro-tessuti.jpg`.

### 2.7 Visti e scartati

| Sito | Perché no |
|---|---|
| [Halfpenny London](https://www.halfpennylondon.com/) | buono il blocco "Make an appointment" con foto del negozio, ma due finestre (newsletter e cookie) sopra l'apertura; niente che Frankel e Peiro non facciano meglio |
| [Rembo Styling](https://www.rembo-styling.com/) | collage di foto sovrapposte e titoli color oro chiaro a basso contrasto |
| [Viktor&Rolf](https://www.viktor-rolf.com/) | moda e profumi, la parte sposa è secondaria; all'apertura chiede il paese di spedizione |
| [Elie Saab](https://eliesaab.com/) | la home è il negozio di prêt-à-porter |
| [Kleinfeld](https://www.kleinfeldbridal.com/) | è un rivenditore (Rosy Garbo lo elenca tra i suoi punti vendita a New York); sito da grande magazzino con Playfair e Roboto |

## 3. Cosa si riprende

| Gesto | Da chi | Dove nel sito Rosy Garbo | Perché proprio qui |
|---|---|---|---|
| Foto verticale alla sua misura in un campo pieno | Danielle Frankel | apertura della Home e delle pagine collezione | le foto sono 562x800 px: mostrarle più grandi le sgrana |
| Dittico: metà foto, metà campo nero o argento | Danielle Frankel, catalogo Rosy Garbo | collezioni New York (nero) e Villa Contarini (argento) | rifà le doppie pagine del loro catalogo |
| Fila di quattro look uniti, didascalia piccola sotto | Rime Arodaky, Laure de Sagazan | pagine collezione | le foto di ogni collezione hanno già lo stesso fondo |
| Le linee come schede che cambiano la fila | Marchesa | Home e pagina Linee | sostituisce le due voci di menu che oggi danno 404 |
| Scheda collezione: luogo, una riga, numero di foto | Fortuny | indice delle collezioni | le collezioni hanno nomi di luoghi veri |
| Testo sulla produzione diviso per temi | Laure de Sagazan | pagina Il marchio | il testo esiste già, verbatim, sul loro sito |
| Sede: indirizzo in una riga sopra la foto, link sotto | Danielle Frankel | Atelier di Padova, showroom di Cona | due sedi italiane, come New York e Los Angeles |
| "Dove trovarci" con link alla rete | Jesus Peiro, Peter Langner (trunk show) | Home e pagina Atelier nel mondo | la rete estera è il dato che i concorrenti locali non hanno |
| Appuntamento con data delle nozze | Fausto Sari, Polignano, Langner | pagina Contatti | è il modo in cui si compra un abito da sposa |
| Etichette di sezione in maiuscolo spaziato su una fascia sottile | Danielle Frankel, Fortuny | tra le sezioni lunghe | sostituisce titoli grandi e ripetuti |

**Scartato:** video d'apertura senza immagine di riserva; finestre newsletter; contatori ("500+ abiti", "38 anni di
storia"); recensioni a stelle; tre icone in fila; testo bianco su beige; caroselli automatici; nomi sopra i volti;
corsivo con grazie; orari "aperto/chiuso" finché l'azienda non conferma gli orari (oggi non sono pubblicati).

## 4. Accoppiate

Tre proposte, tutte con caratteri di Google Fonts presenti nell'elenco di Elementor 4.3.3 (controllato nel file
`includes/fonts.php` di un'istanza di prova): Libre Franklin, Newsreader, Jost. Nessuna usa Inter, nessuna usa un
corsivo. Rapporti di contrasto calcolati con `_prova/script/contrasto.py` (WCAG 2.x; minimo 4,5:1 per il testo).

### A. Pagine nere e argento (solo senza grazie)

- **Caratteri:** **Libre Franklin** per tutto. 300 maiuscolo, spaziatura 0,08 em, per i nomi delle collezioni
  (40-64 px a desktop, 30-36 a 390); 600 maiuscolo, spaziatura 0,14 em, per etichette e menu (12-13 px);
  400 per il testo (17 px, interlinea 1,6).
- **Da dove viene:** Jesus Peiro (Franklin Gothic maiuscolo spaziato, maison sposa con lo stesso modello di vendita);
  Fortuny (un solo senza grazie, didascalie piccole); le testate delle collezioni Rosy Garbo, già in senza grazie
  sottile maiuscolo; le pagine nere e argento del loro catalogo.
- **Palette:** nero #0E0E0E, bianco #FFFFFF, argento #C5C6C8 (pagina del catalogo Villa Contarini), grigio testo
  #5C5D61, grigio su argento #3A3B3E, grigio su nero #9A9BA0, filetto #D9DADC. Il tricolore resta solo nel logo.
- **Foto:** New York (colore e bianco e nero) su campo nero; Villa Contarini su campo argento.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero #0E0E0E | bianco #FFFFFF | 19,30:1 |
| nero #0E0E0E | argento #C5C6C8 | 11,29:1 |
| grigio #5C5D61 | bianco #FFFFFF | 6,58:1 |
| grigio #3A3B3E | argento #C5C6C8 | 6,55:1 |
| bianco #FFFFFF | nero #0E0E0E | 19,30:1 |
| argento #C5C6C8 | nero #0E0E0E | 11,29:1 |
| grigio #9A9BA0 | nero #0E0E0E | 6,96:1 |
| filetto #D9DADC | bianco | 1,40:1 (solo linee, mai testo) |

Carattere: moderno, da casa di moda con atelier a New York. Rischio: troppo freddo per la sposa se le foto non
fanno il loro lavoro; serve il campo argento per non diventare un sito tutto nero.

### B. Dittico (grazie dritte e geometrico)

- **Caratteri:** **Newsreader** (ottica display, 300 e 400, mai corsivo) per titoli e nomi delle collezioni, solo
  sopra i 28 px; **Jost** 400 e 500 per testo (17 px), menu ed etichette in maiuscolo spaziato 0,12 em.
- **Da dove viene:** Danielle Frankel (un solo carattere con grazie, dritto e leggero, su tutto il sito; foto
  incorniciate); Laure de Sagazan e Marchesa (Jost per testo e interfaccia); il logo Rosy Garbo, che è un carattere
  con grazie. Il serif qui è motivato da siti sposa veri, non dall'abitudine "lusso = serif".
- **Palette:** bianco #FFFFFF, carta grigia #F4F4F1 (più fredda del #F8F8F4 di Frankel e del #F9F7EF di Sagazan:
  niente crema), pietra #DCDAD5 per i campi delle foto incorniciate, inchiostro #212121, grigio #5E5E5B.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #212121 | bianco #FFFFFF | 16,10:1 |
| inchiostro #212121 | carta #F4F4F1 | 14,61:1 |
| inchiostro #212121 | pietra #DCDAD5 | 11,53:1 |
| grigio #5E5E5B | bianco #FFFFFF | 6,51:1 |
| grigio #5E5E5B | carta #F4F4F1 | 5,90:1 |
| bianco #FFFFFF | inchiostro #212121 | 16,10:1 |
| grigio chiaro #8A8A86 | carta #F4F4F1 | 3,14:1 (solo linee e numeri grandi, mai testo) |

Carattere: atelier sartoriale, più morbido. Rischio: è la direzione più vicina al tentativo bocciato. Regge solo con
carta grigia fredda, nessun corsivo, foto vere incorniciate e titoli brevi.

### C. Marchio e testate (innesto, la proposta da valutare per prima in 2.3)

- **Caratteri:** **Newsreader** 300 solo per i nomi delle collezioni e il titolo d'apertura; **Libre Franklin** per
  tutto il resto (testo 400, etichette e menu 600 maiuscolo spaziato).
- **Da dove viene:** dal materiale di Rosy Garbo prima che dai riferimenti: il logo ha le grazie, le testate delle
  collezioni no, le pagine del catalogo sono nere e argento. Conferme dai riferimenti: Marchesa (titoli con grazie,
  interfaccia senza), Jesus Peiro (Franklin maiuscolo con una sola frase con grazie).
- **Palette:** quella di A (nero, bianco, argento, grigi) più la carta grigia #F4F4F1 di B per le pagine di testo lungo.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero #0E0E0E | bianco #FFFFFF | 19,30:1 |
| nero #0E0E0E | carta #F4F4F1 | 17,52:1 |
| nero #0E0E0E | argento #C5C6C8 | 11,29:1 |
| grigio #5C5D61 | carta #F4F4F1 | 5,97:1 |
| argento #C5C6C8 | nero #0E0E0E | 11,29:1 |
| bianco | velatura nera al 55% su foto Contarini (media #A8A4A3) | circa 7,9:1 (senza velatura 2,47:1: testo mai diretto sulla foto) |

Carattere: una maison italiana con atelier a Padova e rivenditori a New York; tiene insieme il logo con grazie e le
testate senza. Rischio: due famiglie vanno dosate; il serif solo per i nomi, mai per testo o pulsanti.

**Regole comuni alle tre:** foto mai più grandi della loro misura (circa 560 px di larghezza per una metà di catalogo:
a 1440 si mostrano incorniciate o in fila, non a tutto schermo; su schermi retina restano a 1x finché 01 non trova
originali più grandi); nessun testo bianco diretto sulle foto; hover a colore pieno, mai in opacità; spaziature da una
sola scala; nessuna sezione che compare in dissolvenza.
