# Home versione 2 (scheda d'uso), Panificio Galileo Fornasiero, 2 novembre 2026

Pagina: `sito-v2/index.html` (statica, si apre con file:///), immagini in `sito-v2/img/` (WebP a più larghezze con srcset), caratteri in `sito-v2/fonts/`. Costruita sulla scheda `_prova/uso/SCHEDA.md`, non sulla home precedente (`sito/`, che resta com'è). Tutto si rifà con `bash _prova/uso/script/build_v2.sh` (immagini, screenshot, prove d'uso).

Screenshot (ora simulata lunedì 2 novembre 2026 alle 10.00, ora di Roma): `home-1440.jpg` (6987 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-320.jpg`, `home-768.jpg`, `home-1024.jpg`. La pagina legge l'ora di Roma; per le prove si forza con `index.html?ora=2026-11-15T10:00`.

## Per ogni visitatore della scheda: cosa trova e dove

**1. Il cliente di Camin (telefono, spesso anziano, di fretta).** Tutto nei primi 844 px a 390, senza scorrere:
- la vetrina di via Vigonovese con l'insegna di legno "FORNASIERO Galileo" e Galileo e Fidalma sulla porta, sotto la testata (160 px): il posto si riconosce prima di leggere;
- "Panificio Fornasiero, a Camin dal 1963" e una riga su cosa fanno;
- la frase di stato in corpo 21 (34 a 1440), calcolata sull'ora di Roma: "Aperti ora tutti e due i negozi, fino alle 13.45.", "Ora chiusi. Alle 16.30 apre via Alsazia 3. Via Vigonovese il mercoledì pomeriggio è chiusa.", "Aperto ora in via Alsazia 3, chiude alle 13.30." (sabato), "Oggi è domenica: chiamate prima di passare. Domani apriamo alle 8.30.";
- i due negozi, uno per riga: nome, "Aperto" o "Chiuso" con l'orario di oggi, un bottone "Chiama" con il numero di quel negozio (tel:+390498702658, tel:+390498705107) e un bottone "Mappa" con l'indirizzo di quel negozio; bersagli alti 52 px;
- "Tutti gli orari e il cellulare di via Alsazia": un tocco porta alla chiusura con l'orario della settimana dei due negozi (il mercoledì pomeriggio, il sabato), e il 338 660 06 64.
A 1440 lo stesso nella colonna di sinistra, con l'orario della settimana già scritto sotto ogni negozio; a destra le tartarughe davanti al sacchetto "Fornasiero srl Camin-Padova". Il menu ha "Negozi e orari" come prima voce.

**2. Chi prenota le Feste (telefono, novembre e dicembre).** Nella prima schermata, sotto i negozi, la fascia bordeaux "Panettone e focaccia di Natale, si prenotano adesso: come si prenota" (fondo a 800 px su 844). Un tocco, o uno scorrimento, porta alla sezione: il panettone tagliato sul sacco di juta (foto loro), il titolo con le parole della Bacheca di Romina "Non è Natale senza i panettoni e le focacce", "preparati con l'antica ricetta di Galileo Fornasiero. Si prenotano in negozio o al telefono.", il bottone "Chiamaci e ordina: 049 870 26 58" (le loro parole) e il numero di via Alsazia, la frase di Fidalma sulle focacce "preparate come 50 anni fa", la focaccia sul sacco del cinquantesimo. A 1440 la fascia chiude la prima schermata a tutta larghezza con il bottone "Chiama". Dal 1 novembre al 24 dicembre la sezione sta subito dopo l'apertura; nei 40 giorni prima di Pasqua diventa "Colomba e focaccia di Pasqua"; fuori stagione la fascia sparisce e la sezione, "Natale e Pasqua", scende dopo il pane (provato con il 15 giugno e il 20 marzo 2027).

**3. Il gestore di bar, ristorante o albergo (computer).** Voce "Per bar e ristoranti" nella testata, un clic. Sezione con i panini nel cesto davanti al sacchetto con l'indirizzo, il titolo "Per bar, alberghi, ristoranti e rivendite", le loro due frasi del sito (fornitura e consegne in zona Camin e dintorni), la prova "Per decenni abbiamo dato il pane a tante aziende della zona, agli operai delle Officine Meccaniche Stanga, della Snia Viscosa." (Mattino 2023), "Chiama il laboratorio: 049 870 26 58" e "Scrivete per una fornitura" (mailto con oggetto "Fornitura pane" e una traccia: locale, indirizzo, pani e quantità, giorni, telefono). L'elenco dei pani è un link alla sezione del pane, dove ci sono i 20 pani del sito con i cinque dai nomi di casa in grande.

Le altre sezioni, poche e nell'ordine della scheda: il pane di ogni giorno (pani, pasta fresca, pizze e focacce, panini, dolci, in righe semplici e senza foto di repertorio); "Siamo aperti dal 1963" (la vetrina con Galileo e Fidalma a 1440, quattro date, la frase di Galileo "fornai anche nel nome"); la Bacheca di Romina con i suoi tre dolci nuovi, le sue frasi e la firma; la chiusura con la frase di Galileo "Non abbandonerei mai Camin, qui è la mia famiglia, il mio mondo, il mio lavoro.", i due negozi con indirizzo, mappa, telefoni grandi e orari, la mail, e la foto dei pani tondi davanti al sacchetto "panificio Galileo Fornasiero srl"; il piede.

## Idea

La bottega di via Vigonovese, come la si vede dal marciapiede. La testata è l'insegna: una fascia del legno bruno della vetrina con "FORNASIERO" in maiuscole spaziate bianche, come sopra la porta. La pagina è il bianco del loro sacchetto di carta, con le scritte brune; le Feste hanno il bordeaux della scritta "Fornasiero dal 1963" del loro sito; il piede torna al legno dell'insegna. Il testo più grande dopo il nome è la risposta alla domanda che fanno tutti: è aperto, quale negozio, fino a che ora. Ogni foto è loro e quasi tutte mostrano il loro nome (sul sacchetto, sull'insegna, sull'etichetta del sacco di juta): con il nome di un altro forno la pagina non sta in piedi.

Scelte nuove rispetto alle altre home della campagna: il titolo d'apertura non è uno slogan ma lo stato del negozio, calcolato; la testata e il piede presi dall'insegna di legno; l'ordine delle sezioni cambia con la stagione; il fondo bianco carta del sacchetto (niente beige, niente oggetto scontornato, niente legende numerate).

Registro: prima persona plurale, frasi corte, cortesia di bottega ("chiedete al banco o al telefono", "Chiamaci e ordina", "Ti aspetto, Romina"). I titoli sono parole loro dove esistono: "Siamo aperti dal 1963", "Non è Natale senza i panettoni e le focacce", "Per bar, alberghi, ristoranti e rivendite"; le citazioni sono tra virgolette con chi le ha dette e quando. Niente giochi di parole.

## Caratteri e colori

- Erode 400 e 500 (Indian Type Foundry, da Fontshare, ITF Free Font License, uso commerciale gratuito): titoli, nomi dei negozi e dei pani, citazioni. Una serif dritta, calda e un po' rustica, vicina alle lettere dipinte delle vecchie insegne; mai in corsivo.
- Fira Sans 400, 500 e 600 (Carrois Apostrophe per Mozilla, da Google Fonts, SIL Open Font License 1.1): testo, stato, orari, bottoni, piede. Un bastone umanistico nato per gli schermi piccoli, aperto e leggibile per clienti anziani, con cifre tabellari (orari e telefoni allineati) e lo zero senza barra. Ho provato prima Atkinson Hyperlegible Next e Inclusive Sans: lo zero barrato faceva sembrare i numeri di telefono un codice.
- I file sono serviti dalla pagina in `sito-v2/fonts/`. Nessun carattere delle liste da evitare della guida, nessuno di quelli già più usati nella campagna.
- Colori (contrasti WCAG): carta del sacchetto #FBFAF7 con inchiostro bruno #2A1E17 (15,5:1) e testo secondario #5C4A3E (8,0:1); legno dell'insegna #4A2E1F per testata, bottoni e piede (bianco sul legno 12,3:1; crema #E7DACB sul legno 9,0:1); bordeaux della scritta #733129 per la fascia delle Feste e le date (bianco sul bordeaux 9,5:1; bordeaux sulla carta 9,1:1); verde #2C6A3C solo per "aperto" (6,2:1); un grigio caldo #F3EFE8 per la sola fascia di "Chi siamo". Tutto AA, quasi tutto AAA.

## Interazione

Un solo gesto, quello che serve: la pagina sa che ora è a Camin e lo dice. Lo stato e le righe "oggi" dei due negozi si calcolano sugli orari scritti dal panificio; dove l'orario non è scritto (sabato di via Vigonovese, domenica) la pagina non dice "chiuso" ma "chiedete l'orario al telefono". Il menu del telefono è un vero bottone con aria-expanded e si chiude toccando una voce. Transizioni solo di colore su link e bottoni; niente comparse allo scorrere, niente effetti al cursore.

## Foto, origine e licenza

Tutte del Panificio Galileo Fornasiero, prese dal loro sito (`assets/originali/`, scaricate da static.wixstatic.com il 24/10/2026, voti in `_prova/inventario-immagini.json`). Nessuna foto di repertorio, nessuna immagine generata. Trattamento comune in `_prova/uso/script/v2_img.py`: luce verso il bianco della carta, colore trattenuto, tagli che lasciano fuori la sessola di plastica.
- Prima schermata a 390 e "Chi siamo" a 1440: la vetrina con Galileo e Fidalma (`617993_02eb45f6...`), 640x319, mai ingrandita nel file.
- Prima schermata a 1440 e pane a 390: le tartarughe nel cesto davanti al sacchetto (`617993_28aa18bc...`).
- Feste: il panettone tagliato (`b56ebf_5b27b00f...`, Nikon D3300, dicembre 2020) e la focaccia sul sacco del cinquantesimo (`b56ebf_fabcdffb...`).
- Pane a 1440: pane a fette nel cesto (`617993_f35f170e...`).
- Forniture: panini nel cesto davanti al sacchetto con l'indirizzo (`617993_f2c61f63...`).
- Bacheca: pan di Spagna con le albicocche (`b56ebf_c01687dd...`), tortino di mele e cioccolato (`b56ebf_da6ff058...`), plumcake (`b56ebf_78f7070d...`), foto da telefono della Bacheca di Romina.
- Chiusura: pani tondi davanti al sacchetto "panificio Galileo Fornasiero srl" (`617993_f78248a8...`).
- Logo nel piede: il logo a cesto del sito a una tinta crema, PNG a 2x e 3x (112 px a vista); non ricostruito in SVG perché il disegno ha ombre e sfumature.
Licenza: sono foto del panificio pubblicate sul suo sito; per usarle nel sito nuovo serve il loro consenso (va chiesto insieme a quello per la foto con Galileo e Fidalma). Le foto della libreria Wix e le Unsplash di `assets/esterne/` non sono usate.

## Piede

Logo e una riga su chi sono; "Gli avvisi di Romina" (una email quando si aprono le prenotazioni di Natale e di Pasqua: campo, bottone e consenso privacy, tenuti piccoli perché il canale vero è il telefono; il modulo non invia nulla e lo dice); quattro colonne: Il panificio (storia, Bacheca, forniture), Prodotti (ancore della home), I negozi (i due telefoni, gli orari, la mail), Seguici (solo Instagram, l'unico social collegato dal loro sito); riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie. A 390 le colonne si impilano nell'ordine. Nella testa della pagina c'è anche il dato strutturato con i due negozi, CAP 35127 e orari (il sito di oggi ha CAP 35024 e un solo negozio).

## Controlli (2 novembre 2026)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, chiusura, 320, 768, 1024.
- Prove d'uso (`_prova/uso/script/v2_prova.mjs`): stato a lunedì 7.00, 10.00, 14.30, 19.45, 21.00, mercoledì 10.00, 14.30, 17.00, venerdì 21.00, sabato 7.30, 10.00, 15.00, domenica 10.00; a 390x844 il 15 novembre due tel: diversi alti 52 px, due mappe, la fascia delle Feste e la vetrina sono tutti dentro i primi 844 px (stato finisce a 418, fascia a 800); fuori stagione la fascia non c'è e le Feste scendono dopo il pane; a 1440 la fascia finisce a 898 px su 900; menu del telefono.
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 599, 600, 768, 1024, 1099, 1100, 1280, 1440, 1920, 2560; nessuna ancora rotta.
- Segnali da IA (`_metodo/kit/segnali.sh` a 1440): 0 soglie bloccanti su 10, 0 da guardare su 8; foto al 35,1 % della pagina, una sola etichetta maiuscola sopra un titolo (la Bacheca), nessuna freccia, nessun mono, nessuna numerazione.
- Divieti del committente: nessun gradiente, nessuna icona, nessuna card con ombra, niente vetro, niente corsivo, niente badge, niente dissolvenze.
- Nessun carattere U+2014 in pagina, negli script e in questa nota.

## Cosa resta da confermare

- Il sabato di via Vigonovese e le domeniche dei due negozi (la pagina dice "chiedete l'orario al telefono"), le ferie, gli orari dei giorni di festa e del periodo di Natale.
- Se via Alsazia 3 è ancora aperta e chi risponde al 338 660 06 64.
- Le date delle prenotazioni di Natale e Pasqua (inizio e ultimo giorno) e se si possono dire pezzature o prezzi; le date della fascia (oggi 1 novembre-24 dicembre e i 40 giorni prima di Pasqua) sono una mia scelta.
- Il consenso a usare le loro foto, la foto della vetrina con Galileo e Fidalma e i loro nomi, e le citazioni dal Mattino di Padova; come vogliono essere nominati (chi guida oggi la bottega, Filippo, Romina).
- Se la ricetta di Galileo vale anche per colomba e focaccia di Pasqua (in pagina è scritta solo per il Natale).
- "Oltre 30 tipi di pane" (il sito ne elenca 20) e quali si fanno ogni giorno.
- Fornitura e consegne: zona, giorni, quantità minime, se il pane e il Mattino a casa esistono ancora.
- Il marchio da usare (logo a cesto, insegna, scritta del sacchetto) e un file vettoriale; REA (companyreports dice PD 235130, serve una visura), PEC e capitale sociale per la riga legale.
- Se vogliono gli avvisi per email e con quale servizio; Instagram è ancora attivo? La pagina Facebook trovata in ricerca è loro?
