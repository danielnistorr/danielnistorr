# Unicar, home finale: "Al suo posto"

File: `sito/index.html` (statico, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot con `finale_shoot.py`); le prove sono `finale_prova.mjs` (gesti), `finale_larghezze.mjs` (larghezze, impaginazione dell'apertura, collegamenti) e `finale_viste.mjs` (larghezze di confine e righello). Pagina alta 4893 px a 1440 compreso il piede, circa 6350 px a 390.

## Idea

Il carrello è parcheggiato al suo posto, dentro la corsia gialla dipinta sul pavimento d'officina. La corsia non è più un filo: è una banda a terra alta un quarto della finestra (216 px a 1440 x 900), su cui poggiano le due ruote, con l'ombra di contatto sul giallo. Sopra c'è il cemento lisciato, dove il titolo poggia sulla stessa linea delle ruote; dentro la corsia stanno il testo e il bottone del telefono. La stessa linea gialla torna più sotto come righello dei controlli di legge. Il giallo (vicino al RAL 1023 delle segnaletiche a terra) è la sicurezza del parco carrelli, cioè il mestiere di Unicar; il fondo grigio chiaro è il pavimento, e lo si capisce perché il carrello ci sta sopra.

## Cosa è cambiato in questo passaggio (giudizio cieco del 2 novembre e richiesta "più alta gamma, meno uguali")

- **Impaginazione dell'apertura** (K6): non più "titolo in alto a sinistra, oggetto a destra, riga tecnica piccola sotto". Ora la prima schermata è divisa in orizzontale tra cemento e corsia: il carrello intero (dalla cima del montante alle ruote) sta in piedi dentro la banda gialla, il titolo è in basso, poggiato sul bordo della corsia, e sopra resta un campo vuoto di cemento; paragrafo, bottone e link sono stampati dentro la corsia, nero su giallo. Nessuna delle 13 home amate né delle copertine di Est e Grisignano ha una banda di colore a terra su cui stanno insieme oggetto e testo.
- **Scontorno del carrello** (difetti bloccanti): sotto la traversa bassa dello schienale ora si vede la ruota anteriore (restano i pixel scuri di gomma, parafango e traversa, va via solo il fondo); i vetri della cabina sono un vetro fumé uniforme, grigio scuro e un po' più chiaro in alto, al posto del velo dell'8 % che lasciava il volante bucato; il volante ha la corona chiusa (chiusura morfologica dei soli pixel scuri); tolti tergicristallo anteriore e posteriore e lo specchietto, che restavano schegge sospese. Controllato a 300 % sul file da 1300 px e nelle prime schermate a 1440, 1024, 768 e 390.
- **Niente riga tecnica in apertura**: tolta la frase sul tagliando "di novembre" (presentava un'ipotesi come fatto); resta il link "Le date dei controlli".
- **Titolo** più grande: fino a 110 px (7,4 vw), interlinea 0,95.
- **Il carrello non tocca mai la testata**: se il montante cadrebbe sotto il numero di telefono, il carrello si abbassa e la cima del montante resta sotto gli 84 px (provato da 901 a 2560 di larghezza con altezze da 700 a 1440).
- **Servizi**: il blocco dei ricambi segue il paragrafo a 80 px (prima c'era un vuoto di circa 250 px).
- **Officina**: tono uniformato all'apertura (ombre alzate, niente dominante calda, contrasto più morbido); la foto non è più ingrandita: al massimo 520 px a 1440 e 645 px sul tablet, dal taglio di 645 px dell'originale.
- **Sede**: la frase dice "nella sede che Unicar condivide con la consociata Cami2, oggi di oltre 4000 mq" (cami2.it/azienda/), non più "3000 mq dal 2009"; i numeri tra Padova e Venezia sono detti "delle due aziende insieme".
- **Righello**: tacca "oggi" e mesi già passati in chiaro (asse velato, tacche ed etichette a opacità 0,35).
- **Chiusura**: sotto il titolo una frase centrata su Unicar ("Interventi rapidi e risolutivi, perché il ciclo produttivo non si fermi", dalla pagina Assistenza: "concludendo l'intervento in modo rapido e risolutivo", "garantire continuità al ciclo produttivo del cliente"); Cami2 resta solo nella nota della sede e nel piede (Vendita e noleggio). Recapiti in due colonne (telefono, email, fax; indirizzo, mappa, zona). La foto è un taglio della palazzina con le insegne UNICAR e BT CESAB, senza l'insegna Cami2, 455 x 249 alla misura nativa, a filo del bordo destro; non viene mai ingrandita, neanche sul tablet.
- **Logo**: mostrato a 96 px in testata e nel piede (densità 2,5x del PNG da 241 px). Il logo della testata porta a "./".
- **Privacy e Cookie** puntano a `privacy.html` e `cookie.html` (pagine da fare, nel LEGGIMI); nessun href="#" in pagina.

## Prime due schermate

- **1440 x 900**: testata a sinistra (logo, menu, telefono rosso). Il carrello, alto 920 px e largo 729, esce a destra; la cima del montante è a 28 px. Cemento fino a 684 px, poi la corsia gialla fino a 900. Il titolo Archivo a 107 px su tre righe, "Consulenti, più che riparatori" (dalla loro home: "affiancare il cliente come consulenti più che di riparatori"), finisce 44 px sopra la corsia. Nella corsia: le tre righe su cosa fanno e dove arrivano i tecnici, il bottone "Chiamate lo 049 8792361" e il link alle date dei controlli.
- **Seconda schermata**: "Riparazione, ricambi, controlli" a sinistra con la frase dei ricambi sotto; a destra i servizi del loro sito in tre gruppi.
- **390**: logo, telefono e Menu; titolo a 51 px; il carrello largo quanto lo schermo, con le ruote che entrano nella corsia gialla; nella corsia il testo e il bottone.

## Caratteri e colori

- **Archivo** (Omnibus-Type, Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), famiglia variabile servita dalla pagina. Titoli a larghezza 118 % e peso 470-500, testo a 100 % e peso 400, enfasi 600; cifre tabellari per telefono, date, mesi e dati societari. Perché: il grottesco largo dei costruttori del settore (le maiuscole larghe di Scania e Fendt, 01-analisi.md sez. 7) e le lettere bastone larghe del logo UNICAR.
- **Colori**: cemento #E5E6E2 (il pavimento); giallo corsia #F2B807 (la banda a terra e il righello); registro #F6F6F3 solo per il promemoria; grafite #1B1D1F per titoli, bottoni e testo nella corsia; testo #2A2D30 e #4F5358; rosso #C8141C solo per il telefono e i numeri dei passi. Contrasti: grafite su giallo 9,4:1, testo #2A2D30 su giallo 7,7:1, testo secondario su cemento 6,2:1, rosso su cemento 4,7:1. Nessun gradiente, nessuna ombra su riquadri.

## Interazione

Un solo gesto, il promemoria dei controlli dalla loro "Nota informativa" sull'art. 71 del D.Lgs. 81/2008: si sceglie il mese dell'ultimo tagliando tra gli ultimi dodici (pulsanti radio, frecce da tastiera o dito; a 390 griglia 6 x 2 con bersagli di 54 px). La pagina scrive il prossimo controllo di funi e catene e il prossimo tagliando e li segna sul righello giallo, con la tacca "oggi"; "Mettete le date in calendario" scarica un file .ics; il bottone chiama. Transizioni di 120 ms solo su bottoni e mesi; nessuna animazione allo scorrere, nessun effetto che segue il cursore.

## Foto

- **Apertura**: Mathias Reding, Unsplash `r4Y_VNKzAbw` (Unsplash License, `assets/CREDITI.md`). È un segnaposto: un carrello Toyota qualunque, usato, non di Unicar. L'apertura è disegnata perché funzioni con il loro carrello revisionato fotografato sulla loro corsia (LEGGIMI, foto 1). Ritocchi: adesivi SOFIMA e corda sul contrappeso tolti, fango e graffi puliti, vetro fumé, scontorno rifatto attorno alla ruota anteriore, ombra di contatto morbida. WebP con trasparenza a 520, 760, 1040, 1300 px.
- **Officina**: Cemrecan Yurtman, Unsplash `GjmQzjPuF30`: taglio stretto su mani, avvitatore, catene e testa del montante, nessun volto; tolta la scritta TCM. 520 e 645 px, più un taglio verticale da 612 px per il telefono.
- **Chiusura**: la sede vera di via Canada 12 dal loro sito (`testata/007.jpg`), taglio 455 x 249 sulla palazzina con le insegne Unicar e BT Cesab, mai ingrandito.
- Nessuna di queste foto è nei CREDITI delle altre home della campagna (controllo per ID il 2/11/2026). Nessuna immagine generata.

## Piede

Logo PNG originale a 96 px con una riga su chi sono; colonne Servizi, Azienda, Contatti con le voci del loro menu; "Vendita e noleggio (cami2.it)" dichiara il link esterno; a 390 si aprono a fisarmonica con veri bottoni (`aria-expanded`). Nessuna colonna Seguici: Unicar non ha profili social. **Niente newsletter**: lavorano solo per aziende, le notizie del sito sono due del 2012, non fanno fiere, cataloghi o collezioni e non hanno clienti privati; il contatto utile è il promemoria dei controlli. Riga legale: Unicar srl, via Canada 12, 35127 Padova, P.IVA e C.F. 01014160285, REA PD 170490, capitale sociale 100.000,00 euro, Privacy, Cookie.

## Controlli fatti (2/11/2026, dopo le modifiche)

- Screenshot a 320, 390, 768, 901, 1024, 1181, 1280, 1440 e 1920 guardati a pezzi: nessuna sovrapposizione, il testo della corsia sta dentro la corsia a ogni misura, il titolo non tocca il carrello, il montante non tocca il telefono della testata.
- `finale_larghezze.mjs`: scrollWidth uguale a innerWidth a 23 misure da 320 x 640 a 2560 x 1440; un solo numero `tel:+390498792361`, `mailto:unicar@protec.it`, la mappa `google.com/maps?cid=7853003542386361464`; nessun href="#".
- `finale_prova.mjs`: promemoria provato con clic e con le frecce a 1440 e con il tocco a 390 (bersagli di almeno 53 px), file .ics generato, menu e fisarmonica a 390; nessun errore di script in console. `finale_viste.mjs`: con ultimo tagliando a maggio 2026 il righello mostra in chiaro mag 26 e ago 26, "oggi" su nov 26 e in evidenza nov 26 (funi e catene) e mag 27 (tagliando).
- Nessun U+2014 in pagina, nei .md e negli script.
- `segnali.sh`: 17 soglie su 18 senza problemi (carattere, monospazio, etichette, titoli, H2, filetti 21, frecce 0, numerazioni 0, didascalie, contenuto datato); 5 fasce di colore pieno, una in più della soglia indicativa, perché la corsia gialla dell'apertura ora è una banda. Resta fuori l'area foto, 14,5 % contro 35 %: il protagonista è un oggetto scontornato, che lo strumento conta poco, e le due foto piccole non vengono più ingrandite oltre la misura nativa. La soglia si raggiunge solo con le riprese del LEGGIMI (officina e sede in alta risoluzione).
- Dati: ogni fatto in pagina viene da 01-analisi.md.
