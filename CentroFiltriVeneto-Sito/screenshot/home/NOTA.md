# Home finale di Centro Filtri Veneto

Pagina: `sito/index.html` (statica, si apre con un doppio clic), immagini in `sito/img/`. Si rigenera con `_prova/script/build_finale.sh`: monta la pagina dal modello `_prova/script/finale.src.html` con la mappa in linea e rifà i quattro screenshot. Le foto del banco escono da `_prova/script/prepara_finale.py`; le altre immagini sono quelle del prototipo "banco" (`_prova/script/prepara_banco.py`).

Base: il prototipo "banco", scelto dal giudice. Ho applicato tutte le sue indicazioni e preso da "ripiano" la costa gialla con i cartellini e i marchi divisi per famiglia.

## Idea

La home parla come si parla al banco. In apertura ci sono le tre persone vere di CFV dietro il banco di Vigonovo, con gli scaffali pieni alle spalle. La foto si chiude sul bordo del piano. Sotto, il frontale del banco è disegnato con le pennellate oblique del logo: ocra, crema e azzurro, inclinate di 22 gradi. Il blu pieno dell'insegna parte dall'ultima pennellata, proprio dove nella foto c'è la prima giuntura del frontale (16,6 % della larghezza). Su quel blu si chiede il filtro nei tre modi in cui lo si chiede davvero al banco: col codice, col mezzo o col pezzo vecchio. Gli "sportelli" sono divisi da filetti bianchi di 1 px.

Il frontale vero (IMG_1589) ha tre giunture, al 16,6 %, al 52,0 % e all'87,4 % della larghezza, quindi solo due pannelli interi. Per questo i filetti sono messi così:
- l'inizio del blu cade sulla prima giuntura;
- il filetto tra "Hai il codice?" e "Hai solo il mezzo?" cade sulla giuntura centrale (52 %);
- il secondo filetto divide a metà lo spazio che resta. L'ultimo pannello vero (12,6 %) è troppo stretto per un testo.

Da 641 a 1180 px il codice occupa tutta la riga e il filetto fra mezzo e pezzo vecchio resta sulla giuntura del 52 %.

## Prime due schermate

**1440x900**
- Testata: logo, Filtri per mezzo, Marchi, Ricambisti e privati, Dove siamo, 049 9801910 cliccabile.
- Foto del banco, 1440x440. Tra la testa più alta e la testata ci sono circa 52 px d'aria: il ritaglio parte 68 px più in alto nell'originale.
- Frontale a pennellate, alto 36 px.
- Fascia blu:
  - titolo su una riga, "Portaci il codice, il mezzo o il filtro vecchio", in bianco, condensato 800 a 64 px;
  - due righe a 17 px in inchiostro, con i mezzi e sei marchi;
  - i tre sportelli. "Hai il codice?" ha il campo e il bottone giallo "Chiedi su WhatsApp", e sotto il link per l'email. "Hai solo il mezzo?" ha 049 9801910 e WhatsApp 320 6125425 in grande. "Hai il filtro vecchio?" ha "Portalo al banco", Via del Lavoro 30, Tombelle e il link "Come arrivare". La strada da Padova Est non c'è più: è nella sezione Dove siamo.
- Tutta la fascia sta nella prima schermata.

**Seconda schermata a 1440**
- "Dal trattore alla pompa a vuoto" viene subito dopo la fascia. Ci sono due ripiani di filtri ritagliati dalla foto della piramide, ognuno sulla sua costa gialla #FEED00 con un cartellino bianco centrato sotto il filtro:
  - su strada e in campo: PowerCore (Donaldson, aria), LF3883 (Fleetguard, olio), 33119 (gasolio, 5 micron);
  - impianti e reparti: CS-150-P25-A (MP Filtri), SH 51054 (HIFI), filtri a pannello (aria di reparto).
- Accanto a ogni ripiano ci sono i mezzi e le famiglie. I testi dei due ripiani partono dalla stessa colonna.
- Poi vengono le due porte: "Ricambisti e officine" (portale, account, resi a 30 giorni, EXW) e "Privati" (Castrol, telefono, "passa al banco a Vigonovo").
- Seguono i marchi divisi per cinque famiglie, con la piramide intera chiusa nella griglia, e la corsia del magazzino: più di 4000 filtri pronti e più di 15000 gestiti, dal 1985, gennaio 2016, "ISO 9001:2015, TÜV Rheinland, ID 9000034903".
- In fondo la mappa disegnata e il piede con i dati societari.

**390x844**
- Foto del banco, 390x199: chi parla (a sinistra) e il ragazzo al centro, tutti e due interi, senza nessuno tagliato a metà.
- Frontale a pennellate di 22 px; il blu parte sulla giuntura, che in questo ritaglio cade al 23,7 %.
- Titolo su tre righe, campo del codice, bottone, email e 049 9801910 nella prima schermata. 320 6125425 è sul bordo.
- Sotto vengono il pezzo vecchio e poi le righe con i mezzi e i marchi. I tre modi sono divisi da filetti bianchi orizzontali.

## Caratteri e colori

- **Pathway Extreme** (Google Fonts, asse della larghezza 75-100), una famiglia sola:
  - titoli in condensato 800, testo in 400, codici e telefoni in 600 con cifre tabellari;
  - la scelta viene dai siti del settore letti in 02: titoli in grottesco condensato pesante e testo in grottesco neutro (MANN-FILTER, HIFI FILTER, DT Spare Parts, Kramp);
  - scala: 64/52/44/36/30/28/24/22/18/17/15/14 px;
  - l'audacia sta in un punto solo, il titolo bianco sul blu.
- **Blu #0099E1**, l'ultima pennellata del logo e l'insegna. È pieno solo nella fascia del banco. In bianco ci sono solo le misure grandi (titolo, numeri a 30 px); il testo piccolo è in inchiostro #17191B, con contrasto 5,6:1.
- **Pennellate del logo**: ocra #E9C177, crema #F4E1BC, azzurro #9FCCF4. Compaiono solo nel frontale del banco.
- **Giallo sole #FEED00**, il tondo "CFV". Lo usano il bottone della richiesta, la costa dello scaffale e il punto sulla mappa.
- **Fondi**: inchiostro #17191B su bianco caldo #FBF8EF; bianco puro nelle sezioni con i ritagli su bianco (filtri e marchi); piede in inchiostro.

## Foto: origine e licenza

Tutte le foto sono di CFV e sono scaricate dal sito attuale (`assets/originali/`). Non ci sono foto di stock né immagini generate (vedi `assets/CREDITI.md`).

- `2015-04-IMG_1589.jpg` (banco, iPhone, 2016, 4032x3024).
  - A 1440 è un ritaglio di 4032x1232 mostrato a 1440x440 (2880 su retina).
  - A 390 è un ritaglio di 2660x1362 mostrato a 390x199.
  - Ha un leggero autocontrasto.
- `2017-01-magazzino_centrofiltriveneto.jpg` (corsia, Nikon, 2017). È mostrata a 1440x900 con `object-fit`; sorgente di 1800 px, 2880 su retina.
- `2015-04-home_factory_slider_bg.jpg` (piramide, iPhone, 2016).
  - La piramide intera è mostrata a circa 740 px, con sorgente di 1520 o 2400 px.
  - I sei ritagli sono mostrati a 300 px (prima fila) e 224 px (seconda fila) di altezza. Così su retina restano entro la misura nativa: MP 490 px su 448, HIFI 446 su 448, 33119 562 su 600 (1,07 volte, è il solo caso).
- Logo `2015-11-centrofiltriveneto_logo.png`, ridotto a 720 px.
- Mappa disegnata in SVG dai dati OpenStreetMap (ODbL), con l'attribuzione sulla mappa.

## Controlli fatti

- Screenshot guardati tutti a pezzi: 1440 e 390 interi, 768 e 1024 interi.
- Correzioni fatte dopo averli guardati:
  - altezza della fascia (la riga dell'email ora sta nella prima schermata);
  - cartellini che si sovrapponevano a 390 e a 1024 (a 390 resta solo il codice; nella seconda fila la seconda riga dei cartellini è solo la marca);
  - colonne dei testi dei ripiani allineate;
  - "TÜV Rheinland" tenuto su una riga.
- Scorrimento orizzontale: nessuno a 390, 768, 1024, 1440 e 1920 (`_prova/script/larghezze.mjs`, `scrollWidth == innerWidth`). Le "immagini ingrandite" che lo script segnala con dpr 2 sono un falso positivo: con `srcset` in `w`, `naturalWidth` è già diviso per la densità.
- `segnali.sh` esce con 0 e nessuna soglia bloccante:
  - area foto 35,1 %, Pathway Extreme 100 %, 3 misure di H2, 0 etichette sopra i titoli, 0 frecce;
  - da guardare: 6 fasce di fondo, con ruoli diversi (banco, filtri, porte, marchi, magazzino e dove siamo, piede);
  - da guardare: "titolo a sinistra e paragrafo a destra" in 2 sezioni (le due porte affiancate e il testo sotto la foto del magazzino).
- Nessun U+2014 nella pagina, nel modello e nei .md. Nessun segnaposto a vista.
- Dati corretti come chiesto dal giudice: 33119 "5 micron", come è stampato sul filtro ("5 MICRON FINAL FILTER"). Per i privati la promessa del ritiro è tolta.
