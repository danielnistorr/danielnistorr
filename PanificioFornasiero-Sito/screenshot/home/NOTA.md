# Home, Panificio Galileo Fornasiero: versione 1 con l'uso (2 novembre 2026, sera)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), caratteri in `sito/fonts/`. Screenshot e controlli si rifanno con `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche le immagini); prove d'uso con `node _prova/script/v1uso_prova.mjs`, misure della prima schermata con `node _prova/script/v1uso_misura.mjs <larghezza> <altezza> [mobile] [ora]`. La versione 1 com'era prima di questo passaggio è in `_prova/versione-1-originale/` (sito, screenshot, script, LEGGIMI).

Screenshot, all'ora di Roma simulata lunedì 2 novembre 2026 alle 10.00 (`index.html?ora=2026-11-02T10:00`, stagione delle prenotazioni di Natale): `home-1440.jpg` (6442 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8831 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Gli screenshot interi sono fatti con la pagina in cima: la testata, che ora resta in alto, compare una volta sola.

## Ritocco con l'uso, dopo le prove dei clienti tipo (2 novembre 2026)

I tre clienti tipo della scheda (`_prova/uso/SCHEDA.md`) hanno provato questa versione accanto alla versione 2 (`_prova/uso/prova-v1-prima-0/1/2/`): voti 6,5, 5,5 e 7, un compito fallito (chi prenota le Feste non vedeva la foto della focaccia entro uno scorrimento). Ho applicato i difetti bloccanti e importanti e i minori facili restando nella versione 1: stessi caratteri (Sentient e General Sans), stessa scala, stessa griglia, mollica, carta, bruno, spiga e blu; il titolo "Siamo Fornasiero, fornai anche nel nome" con "Forna/forna" nel colore delle spighe, la focaccia scontornata nel gradino e il fondo mollica restano.

**Prima schermata, telefono 390x844**
- Titolo da 44 a 35 px (clamp 32-40 px), sempre su quattro righe, "Forna" sopra "forna", la focaccia di 112 px nel gradino a destra di "Siamo". Lo stato sale da 327 a circa 290 px.
- Stato: le parole in grassetto sono in Sentient 500; "Aperto ora", "Aperti ora tutti e due i negozi", "Aperto" nelle righe di oggi e nelle schede della chiusura sono in verde scuro #2A6234 (5,8:1 sulla mollica, 6,9:1 sulla carta, AA anche in corpo piccolo); "Ora chiusi" e "Oggi è domenica" restano nel bruno, in 500. Il verde è l'unico colore nuovo ed è solo su quelle parole.
- Scheda di via Vigonovese: sotto il nome la striscia dell'insegna di legno "FORNASIERO Galileo" (350x33, taglio 640x60 della loro foto della vetrina, alla misura nativa; l'alternativo dice "a pochi metri dal semaforo"). Solo sotto i 600 px: a 768 e oltre la vetrina intera è in "Chi siamo".
- Righe di oggi: il mercoledì via Vigonovese "Chiuso, oggi 8.30-13.45, pomeriggio chiuso", il sabato via Alsazia "Aperto, oggi 8.30-13.30, pomeriggio chiuso" (regola nello script: un solo orario che finisce entro le 14).
- Eccezioni della settimana in bruno pieno (11,7:1 invece di 5,8:1), 16 px da 601 px in su, 15 px sul telefono perché "Mercoledì pomeriggio chiuso. Sabato: chiamate." stia su una riga; il cellulare 338 660 06 64 è un bersaglio di 50 px.
- I quattro link "Mappa" e "Apri nella mappa" si aprono in una scheda nuova (`target="_blank" rel="noopener"`).
- Testata: resta in alto (`position:sticky`), alta 64 px sul telefono, 88 px da 601 a 1100, 72 px da 1101 in su; un filetto sotto quando la pagina scorre. Sul telefono "Chiama" è un bottone blu pieno di 44 px (prima una parola di 26 px) e "Menu" ha la stessa altezza; "Chiama" chiama via Alsazia quando è aperta solo lei, come prima. Ogni sezione arriva 24 px sotto la testata (`scroll-margin-top`).
- Fascia delle Feste: piena, nel bruno delle scritte (#33261F) con il testo in mollica (11,7:1), a tutta larghezza (il fondo esce dai margini con box-shadow e clip-path, senza allargare la pagina), con il bottone mollica "Chiama 049 870 26 58" e "Come si prenota", alti 48 px. Chiude l'apertura senza la striscia gialla sotto.
- Misure a 390x844: lunedì 2/11 alle 10 la fascia finisce a 813 px, domenica 15/11 (stato su tre righe) a 838; a 430x932 a 831. Tutti i tel: dei negozi (48 px), il cellulare, le due mappe (48 px) e la fascia con il suo tel: stanno nella prima schermata. A 360x780 la fascia finisce a 898: si vede scorrendo poco.

**Prima schermata, 1440x900**: stessa composizione; la testata scende a 72 px e la formula del titolo è ritoccata perché la fascia, ora più alta, chiuda la schermata a 887 px: il titolo passa da 140 a 137 px. Lo stato in verde e la fascia piena sono gli unici cambi a vista.

**Natale e Pasqua**
- In stagione (dal 1 novembre al 23 dicembre alle 13; a Pasqua dai 40 giorni prima al sabato alle 13) lo script sposta la sezione subito dopo l'apertura, prima di "Chi siamo"; fuori stagione resta dopo pasta e dolci. Con JavaScript spento resta dov'era.
- Sul telefono la foto del panettone viene subito dopo il titolo, poi il testo, i bottoni e la focaccia (`display:contents` sulla griglia e sul dittico, `order`, solo sotto i 600 px). Arrivando da "Come si prenota" si vedono titolo, panettone intero e il testo.
- La seconda foto del dittico non è più il sacco con il bordo della focaccia: è la focaccia di Natale intera sul sacco del cinquantesimo, con l'etichetta accanto (taglio quadrato della stessa foto Nikon), didascalia "Focaccia di Natale, sul sacco del cinquantesimo, 1963-2013".
- Titolo e testo cambiano con la stagione: Natale "A Natale, la ricetta di Galileo"; Pasqua "A Pasqua, colomba e focaccia"; fuori stagione "Natale e Pasqua". Dal 15 dicembre (e a Pasqua dai 7 giorni prima) il testo dice "chiamate per sapere se c'è ancora posto", come la fascia.
- Nel testo il numero non è più un link di 21 px: resta scritto, il bottone "Chiamaci e ordina" è subito sotto.

**Il pane, pasta e dolci, forniture, chiusura**
- "Il pane di oggi" diventa "Il pane di ogni giorno". Gli altri quindici pani sono un elenco in due colonne in General Sans 17 px nel bruno, con i nomi interi e, per pane al latte e pane biscotto, le varianti del sito ("pane arabo e bocconcini", "bianco, integrale, ai cereali"); sotto, "In tutto sono oltre 30 tipi: per gli altri chiedete al banco." Etichetta "E ogni giorno", come "I pani con il nome di casa".
- Pasta, pizze e dolci: tolta la fascia delle tagliatelle di repertorio; restano le tre righe nome e descrizione.
- Forniture: la riga "Per i locali, chiamate il laboratorio per sapere se arriviamo fino a voi, in che giorni e a che ora." in bruno 500, come domanda guida; "Camin e dintorni" resta scritto solo per le consegne alle famiglie, come sul sito di oggi (la zona per i locali è da chiedere, non la invento). "Vedi i pani che facciamo" su una riga a sé (44 px). A destra "Oppure scrivete a", la mail a 18 px con 6 px sopra e sotto, "oggetto: Fornitura pane" sotto.
- Chiusura: al posto dei panini Unsplash nei sacchetti, il loro pane a fette nel cesto con il sacchetto "Galileo Fornasiero srl" dietro, con la stessa correzione della luce delle tartarughe; didascalia "Pane a fette, nel cesto del banco." (corta, perché a 1024 una didascalia su due righe finiva sotto la foto).
- Menu e righe "ruolo": `word-spacing:.08em`.
- Ora in pagina non c'è nessuna foto di repertorio: tutte vengono da `assets/originali/`.

**Non applicati, apposta**: il titolo su una riga o cambiato in "Fornasiero, a Camin dal 1963", il titolo a 1440 tra virgolette come citazione e la vetrina al posto della focaccia nell'apertura (il committente ha scelto proprio titolo, focaccia e idea della versione 1; la vetrina è entrata come striscia dell'insegna nella scheda del negozio); la didascalia della focaccia sul telefono (non c'è posto senza far uscire la fascia dalla schermata; la focaccia di Natale ora è nominata nel dittico e nella fascia); "Consegniamo in zona Camin e dintorni, ai locali e anche alle famiglie" (la zona per i locali non è scritta da nessuna parte); "E altri pani secondo la giornata" (non detto da loro: al suo posto il loro "oltre 30 tipologie"); un link "Per bar, alberghi e ristoranti" sotto i negozi (c'è nella testata, che ora resta in alto); a 360x740 la fascia nella prima schermata (servirebbe togliere altro).

**Controlli del ritocco**
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024 intere; arrivo da "Come si prenota" a 390, da "Per bar e ristoranti" e "Il pane" a 1440 (`_prova/script/ritocco_ancora.mjs`). Nessuna sovrapposizione (corretta la didascalia della chiusura a 1024), nessuno scorrimento orizzontale da 320 a 2560 (`v1uso_prova.mjs`).
- `v1uso_prova.mjs`: stato e righe di oggi a 21 ore e giorni (mercoledì pomeriggio e sabato con "pomeriggio chiuso"); Feste il 31/10, 15/11, 16/12, 23/12 alle 12 e alle 14, 15/6, 20/3, 25/3 e 27/3/2027; JavaScript spento; collegamenti (tel:, mailto: con oggetto, mappe, nessuna ancora rotta, nessuna pagina locale).
- `ritocco_misura.mjs`: ordine delle sezioni il 15/6 (apertura, storia, pane, forno, feste, forniture, negozi), il 16/12 e il 20/3/2027 (apertura, feste, storia...), con titolo e testo della sezione giusti per ciascuna data; altezze di stato, insegna, "Chiama" e "Menu" (44 px) a 390.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- PNG temporanei cancellati.

## Versione 1 con l'uso: cosa è cambiato

Il committente, viste le due versioni, ha scelto questa (la 1): grafica, caratteri, colori, impaginazione, la focaccia, il titolo "Siamo Fornasiero, fornai anche nel nome" e l'idea del gradino restano. Dalla versione 2 (`sito-v2/`) ho ripreso solo quello che i clienti tipo dovevano trovare e dove (scheda `_prova/uso/SCHEDA.md`), ridisegnato con i caratteri, la scala, i colori e la griglia di questa pagina. Niente caratteri nuovi, niente icone; niente colori nuovi in quel passaggio (il verde di "Aperto" arriva con il ritocco sopra).

**Prima schermata, telefono 390x844 (il cliente di Camin, il primo visitatore della scheda)**
- La focaccia resta, ma passa nel gradino che sul telefono il titolo lascia libero: a destra di "Siamo", alta come le prime due righe (97 px a 390, tra 70 e 112 px da 320 a 430, mai a meno di 12 px dalle lettere). Il titolo resta su quattro righe con "Forna" e "forna" uno sopra l'altro, a 44 px invece di 52, così tutto quello che serve sta nei primi 844 px.
- Sotto il titolo, come prima, una riga su chi siamo, accorciata: "Pane, pasta fresca, pizze, focacce e dolci dal nostro laboratorio, a Camin dal 1963."
- La riga di stato non è più piccola e in fondo: è in Sentient a 21 px (28 px a 1440), il testo più grande dopo il titolo, calcolata sull'ora di Roma e sui festivi ("Aperti ora tutti e due i negozi, fino alle 13.45.", "Aperto ora in via Alsazia 3, chiude alle 19.30.", "Oggi è festa: chiamate prima di passare. Domani apriamo alle 8.30.").
- I due negozi, uno sotto l'altro, separati dallo stesso filetto delle schede della chiusura: nome in Sentient, "oggi" con l'orario del giorno ("Aperto, oggi 8.30-13.45 e 16.30-20.00"), l'eccezione della settimana sempre in vista (via Vigonovese "Mercoledì pomeriggio chiuso. Sabato: chiamate."; via Alsazia "Sabato 8.30-13.30. Cellulare 338 660 06 64"), il bottone blu "Chiama" con il numero di quel negozio (48 px) e "Mappa" con il filetto bruno, come il bottone "Menu" della testata (48 px). Il bottone blu che c'era prima è diventato il "Chiama" di via Vigonovese.
- In stagione (dal 1 novembre al 23 dicembre alle 13; a Pasqua dai 40 giorni prima al sabato alle 13) l'apertura chiude con una riga a tutta larghezza sotto un filetto: "Panettone e focaccia di Natale: si prenotano in negozio o al telefono." e "Come si prenota", che porta alla sezione di Natale. Dal 15 dicembre: "chiamate per sapere se c'è ancora posto." Fuori stagione la riga non c'è; con JavaScript spento dice "Natale e Pasqua: panettone, colomba e focacce si prenotano in negozio o al telefono."
- Misure a 390x844 (lunedì 10.00): stato finisce a 378 px, i due tel: dei negozi a 48 px, le due mappe a 48 px, la riga delle Feste finisce a 790 px. Domenica 15 novembre (stato su tre righe) finisce a 816.
- "Chiama" in testata: chiama via Vigonovese, o via Alsazia quando è aperta solo lei (mercoledì pomeriggio, sabato mattina).

**Prima schermata, 1440x900**
- Stessa composizione: titolo su tutta la larghezza, la focaccia nel gradino sotto "Siamo", tutto il resto che pende dalla F di "Fornasiero". Il titolo scende da 145 a 140 px (si ridimensiona con l'altezza dello schermo, non sotto 104 px), la focaccia da 403 a 388 px.
- Sotto il titolo: la riga su chi siamo su una riga sola, lo stato in Sentient a 28 px, i due negozi affiancati su due colonne con filetto, "oggi", eccezione, "Chiama" (54 px, come il bottone di prima) e "Mappa"; la riga delle Feste chiude la schermata a 870 px su 900.
- In testata la voce "Per bar e ristoranti" (porta alla sezione nuova delle forniture); "I negozi e gli orari" diventa "Negozi e orari" per far stare la voce. Sotto 1300 px sparisce "panificio dal 1963" accanto al nome, sotto 1100 px il numero in testata (resta nei bottoni dell'apertura), sotto 900 px il menu del telefono come prima.
- 768 e 1024: anche qui la focaccia sta nel gradino sotto "Siamo" (prima a 768 stava sopra il titolo, a 368 px); i negozi su due colonne sotto, a tutta larghezza; sotto 720 px uno sotto l'altro.

**Gli altri compiti, a un tocco dalla prima schermata**
- Natale e Pasqua ("Come si prenota" nella riga delle Feste, "Natale e Pasqua" in testata): alla sezione che c'era ho aggiunto "Pezzature, prezzi e ultimo giorno utile: chiedete al banco o al telefono." e i due numeri, "Chiamaci e ordina: 049 870 26 58" (bottone blu, sono le loro parole della Bacheca) e "Via Alsazia 3: 049 870 51 07". Arrivando dal link, a 390 e a 1440 si vedono i due tel: e la foto vera del panettone. La sezione resta dov'era (dopo pasta e dolci): in stagione ci si arriva dalla riga dell'apertura.
- Forniture e consegne, sezione nuova prima della chiusura, nello stile delle altre (titolo in Sentient come "Pasta fresca, pizze e dolci", testo in General Sans grigio, a destra il telefono grande come nella chiusura): "Per bar, alberghi, ristoranti e rivendite", la loro frase sulla fornitura, gli operai della Stanga e della Snia Viscosa (Galileo e Fidalma al Mattino di Padova, 30/03/2023, copia in `_prova/crawl/stampa/camin_pane_mattino_panificio_fornasiero-.html`), le consegne a domicilio in zona Camin e dintorni, "Chiamate il laboratorio per sapere se arriviamo fino a voi, in che giorni e a che ora", il link all'elenco dei pani, il telefono del laboratorio e la mail scritta in chiaro con oggetto "Fornitura pane" e la traccia (locale, indirizzo, pani e quantità, giorni, telefono). La riga sulle forniture che stava sotto le schede dei negozi è tolta (portava a una pagina che non c'è).
- Negozi e orari (testata e piede): le schede della chiusura restano com'erano, con lo stato calcolato con lo stesso orologio dell'apertura (festivi compresi) e una riga in più per ciascuno: via Vigonovese "Sabato e domenica: chiedete al telefono", via Alsazia "Domenica: chiedete al telefono".
- Mappe: tutte e quattro con il nome del negozio (`query=Panificio Fornasiero Via Vigonovese 116 35127 Padova` e `...Via Alsazia 3 Camin 35127 Padova`).

**Invisibili**
- Lo script dello stato è quello della versione 2, adattato: ora di Roma, festivi nazionali, Pasqua e Pasquetta calcolate, 13 giugno, un elenco `FERIE` da riempire, le date delle prenotazioni in tre variabili in cima (`NATALE_DA`, `FINE_PRENOTAZIONI`, `SPEGNI`), "Sotto Natale gli orari possono cambiare" dal 20 dicembre; nei giorni non scritti (sabato di via Vigonovese, domenica) la pagina non dice né aperto né chiuso. Si aggiorna ogni minuto; per le prove `?ora=`.
- Dato strutturato (schema.org Bakery) con i due negozi, CAP 35127 e orari.
- Nessun link a pagine locali che non esistono: "La storia dal 1963" porta a Chi siamo, "Per bar, alberghi e ristoranti" e "Consegne a domicilio" alla sezione nuova, La Bacheca di Romina, Privacy e Cookie alle pagine del sito di oggi.
- Le foto di repertorio restano due, tutte e due con "Foto indicativa" in didascalia: le tagliatelle (come prima) e i panini nei sacchetti della chiusura (prima senza didascalia, ora "Pane nei sacchetti di carta. Foto indicativa."). La versione 2 non ha foto vere per la pasta e per la chiusura (la vetrina, l'unica che servirebbe lì, è 640x319 e sta già in Chi siamo): non c'era niente di loro da mettere al posto.

**Cosa non ho toccato, apposta**: il titolo, la focaccia scontornata e la sua didascalia, il fondo mollica, Chi siamo, il pane, pasta e dolci, il dittico di Natale, la frase di Galileo nella chiusura, il piede (anche il modulo degli avvisi di Romina, vedi LEGGIMI).

## Controlli (versione 1 con l'uso)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024 intere, 1280x720 e 1920 in alto; nessuna sovrapposizione, nessuno scorrimento orizzontale. A 1280x720 i negozi stanno nella piega, la riga delle Feste finisce a 746 px.
- `v1uso_prova.mjs`: stato a 21 ore e giorni (lunedì 10.00, 13.40, 14.15, 19.45, 21.00; mercoledì 10.00, 14.30, 17.00; venerdì 20.30; sabato 7.30, 10.00, 14.00; domenica; 8/12, 7/12 sera, 25/12, 31/12 sera, 1/1, Pasquetta 2027, 13/6, 15/8): nei festivi nessun "Aperto". Prima schermata a 390x844 e 430x932: due tel: dei negozi e il cellulare, due mappe, le due eccezioni e la riga delle Feste dentro la schermata. Feste il 31/10, 15/11, 16/12, 23/12 alle 12 e alle 14, 15/6, 20/3 e 25/3/2027, 27/3/2027 alle 14; JavaScript spento. Arrivo da #feste, #forniture, #negozi, #pane a 390 e a 1440.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 601, 640, 720, 721, 768, 900, 901, 1024, 1100, 1101, 1280, 1440, 1680, 1920, 2560 (a 901-1100 e a 1101 la voce nuova del menu faceva scorrere: corretto).
- Collegamenti: tel:+390498702658, tel:+390498705107, tel:+393386600664, mailto:info@panificiogalileofornasiero.it (semplice e con oggetto "Fornitura pane"), quattro link mappa ai due negozi, nessuna ancora rotta, nessuna pagina locale.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- PNG temporanei cancellati.

Quello che segue è la nota della versione 1 com'era prima di questo passaggio; dove è cambiato vale quanto scritto sopra.

## Idea

La frase di Galileo al Mattino di Padova, "Siamo Fornasiero, fornai anche nel nome", è l'impaginazione: la seconda e la terza riga del titolo partono esattamente sotto la F di "Fornasiero", così "Forna" e "forna" stanno una sopra l'altra, nel colore delle spighe. Nel gradino che resta libero sotto "Siamo" c'è la loro focaccia veneta, intera, vista dall'alto. Titolo e oggetto si incastrano: con il nome di un altro forno la pagina non sta in piedi.

## Cosa è cambiato in questo passaggio

Prima schermata (bloccante e importanti del giudice, più la richiesta del committente del 2 novembre):
- Via il panino di repertorio su lino grigio, la foto a tutta larghezza con la sfumatura e "Foto indicativa". L'oggetto ora è un prodotto loro: la focaccia veneta con la glassa di zucchero e le mandorle (foto Nikon del panificio, dicembre 2020), scontornata intera con GrabCut (`_prova/script/scontorna_focaccia.py`; dove la focaccia appoggia sull'etichetta del sacco il bordo è letto a mano sul file originale), con un'ombra morbida a destra e in basso come la luce di finestra della foto. A 1440 è larga 403 px e alta 412 (il 46 % dello schermo); nessun bordo tocca la testata o i lati: la cupola sta 256 px sotto la testata, sotto la prima riga del titolo, il bordo sinistro è sul margine di pagina (72 px) e tra il bordo destro e la colonna del testo restano 43 px.
- Nessuna sfumatura linear-gradient sulle foto, in nessun punto della pagina.
- Il fondo dell'apertura e del piede non è più la carta: è la mollica (#F4E6B5), il giallo di uova e burro dentro la focaccia e il panettone. La ragione si vede: la fetta del panettone nel dittico di Natale e le tagliatelle all'uovo hanno lo stesso giallo. Il resto della pagina resta la carta bianca del sacchetto della bottega (#FAF9F6), che si vede dietro le tartarughe. Niente beige di comodo.
- La scelta di impaginazione nuova per la campagna: l'oggetto sta dentro il gradino del titolo, non a destra e non sopra; il titolo è a 145 px su tre righe e occupa tutta la larghezza utile (1296 px a 1440). Nessuna delle copertine di `_invio/zona/home/` e delle home amate ha un titolo a gradino con l'oggetto nel gradino, né un fondo giallo preso dal prodotto. Niente legende numerate, pallini o filetti sull'oggetto: solo una didascalia sotto ("La focaccia delle Feste, con la glassa e le mandorle.").
- La riga di stato di riserva ora dice "Dal lunedì al venerdì dalle 8.30. Il sabato mattina via Alsazia 3 è aperta.", senza far credere che via Vigonovese il sabato sia chiusa. Il link agli orari va a capo pulito sotto.
- A 1280x720 tutta l'apertura sta nella piega (bottone e stato finiscono a 668 px); a 1920 l'apertura è centrata in altezza e non supera 860 px; a 390 la focaccia sta sopra, centrata, e il titolo su quattro righe con "Fornasiero" e "fornai" allineati; tutto il blocco, bottone e stato compresi, sta nei primi 844 px.

Parte centrale:
- Chi siamo: la frase è "Galileo Fornasiero è arrivato a Camin il primo aprile del 1963. Fidalma è al banco da sessant'anni." (Filippo, Romina e Michele Daniele tolti finché il panificio non dà il permesso). Le date stanno a destra della vetrina, allineate in alto alla foto.
- Il pane di oggi: le tartarughe sono ridotte a 6 colonne (636x707 a 1440), tagliate da x 320 (fuori il pangrattato a sinistra e la sessola di plastica a destra), con la scritta "Fornasiero srl Camin-Padova" in alto; la dominante gialla della lampada è corretta verso il bianco delle foto di Natale; la didascalia è sotto la foto. A sinistra, nella stessa altezza: titolo, i cinque pani con il nome di casa uno per riga in Sentient a 56 px, come sulla lavagna del banco, e in fondo gli altri quindici pani. Nessuna colonna vuota.
- Pasta, pizze e dolci: le forniture sono uscite dalla sezione (ora il titolo dice il vero) e stanno in una riga sotto le schede dei negozi, con il link a `fornitura.html`. Restano tre voci, in tre righe nome e descrizione, sotto una fascia a tutta larghezza di tagliatelle all'uovo (segnaposto con "Foto indicativa" in didascalia).
- Natale: il dittico è panettone e sacco del cinquantesimo (l'etichetta 1963-2013 con il bordo della focaccia), per non ripetere la focaccia intera dell'apertura. Le due didascalie hanno lo stesso rientro (var(--m) dal bordo della propria foto).
- Chiusura: la foto di repertorio fredda con i quadretti blu è sostituita da panini nei sacchetti di carta, luce calda; la foto è alta esattamente quanto la colonna del testo (posizione assoluta dentro la cella), e la colonna distribuisce frase, schede e riga delle forniture dall'alto in basso. A 1440 testo e foto finiscono alla stessa riga. I due pannelli delle schede occupano la stessa cella: cambiando negozio la pagina non salta.
- Piede: logo a 120 px (PNG a 2x e 3x), la scritta sotto il cesto si legge; tra la fascia alta e il filetto delle colonne 44 px; a 390 ogni link delle colonne è alto 40 px (padding 9 px sopra e sotto).

## Caratteri e colori

- Titoli, nomi dei pani, telefoni: Sentient 400/500. Testo: General Sans 400/500. Tutti e due di Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito), file serviti dalla pagina in `sito/fonts/`. Una serif dritta e piena, senza corsivi, che regge il titolo a 145 px come una scritta da bottega; il riferimento per la coppia serif grande e bastone piccolo è il piede di Poilâne. Cifre tabellari per orari e telefoni.
- Colori: mollica #F4E6B5 (apertura e piede), carta #FAF9F6, inchiostro bruno #33261F (13,9:1 sulla carta, 11,7:1 sulla mollica), testo secondario #645349 (6,9:1 e 5,8:1), spiga #9A5320 per "Forna/forna" e le date (5,5:1 e 4,6:1), blu #2E4D7B per bottone, campo del modulo e fuoco (8,1:1 e 6,8:1; bianco sul blu 8,5:1). Tutti AA.

## Interazione

Un solo gesto: le schede dei due negozi nella chiusura. Veri bottoni con ruolo tab, frecce, Home e Fine da tastiera, cambio netto senza dissolvenze; per ognuno lo stato di adesso calcolato sull'ora di Roma, il telefono grande con tel:, gli orari, mailto: e "Apri nella mappa". Se all'apertura è aperto solo via Alsazia, la scheda mostra quello. Transizioni solo di colore su link, schede e bottoni; niente comparse allo scorrere, niente effetti al cursore.

## Foto, origine e licenza

- Apertura: la focaccia veneta, foto del panificio (`b56ebf_fabc...`, Nikon D3300, dicembre 2020), scontornata.
- Chi siamo: la vetrina con Galileo e Fidalma, loro, 640x319 alla misura nativa.
- Il pane di oggi: tartarughe della galleria del sito del panificio, loro.
- Pasta fresca: Karen Sewell, https://unsplash.com/photos/T6vI65xwoNA, Licenza Unsplash. SEGNAPOSTO, con "Foto indicativa" in didascalia.
- Natale: panettone sul sacco di juta e l'etichetta del cinquantesimo, foto loro.
- Chiusura: Victoria Nazaruk, https://unsplash.com/photos/ytxRXkY8QE4, Licenza Unsplash. SEGNAPOSTO, ora con "Foto indicativa" in didascalia. Non usata in altre home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 2/11/2026); idem Sewell.
- Logo nel piede: il PNG del sito a una tinta, nel bruno del sacchetto; non ricostruito in SVG perché il disegno ha ombre e sfumature.
- Nessuna immagine generata dall'IA. Trattamento comune con PIL in `_prova/script/finale_img.py`.

## Piede

Logo e una riga su chi sono; newsletter "Gli avvisi di Romina" (prenotazioni delle Feste e dolci nuovi: ha senso, hanno clienti privati e notizie che tornano ogni anno), con campo, bottone e consenso, che non invia nulla finché non si collega a un servizio; quattro colonne (Il panificio, Prodotti, I negozi, Seguici con il solo Instagram, l'unico social collegato dal loro sito); riga legale con ragione sociale, indirizzo e P.IVA, Privacy e Cookie. Il REA non c'è finché non arriva una visura. A 390 le colonne si impilano nell'ordine Il panificio, Prodotti, I negozi, Seguici.

## Controlli (2 novembre 2026)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024, 1280x720, 1920.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 601, 768, 900, 901, 1024, 1100, 1101, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/controlli.mjs`).
- Altezza a 1440: 6255 px compreso il piede.
- Gesto (`_prova/script/prova_gesto.mjs`, orologio finto, ora di Roma): lunedì 10.00 e 14.30, mercoledì 10.00 e 17.00 (si apre su via Alsazia), venerdì 21.00, sabato 10.00 (via Alsazia aperta, via Vigonovese "meglio chiamare") e 15.00, domenica 10.00; frecce, Home e Fine da tastiera; tocco a 390; menu del telefono.
- Collegamenti: tel:+390498702658, tel:+390498705107, tel:+393386600664, mailto:info@panificiogalileofornasiero.it, due link alla mappa (via Vigonovese 116 e via Alsazia 3), nessuna ancora rotta.
- Segnali da IA (`_metodo/kit/segnali.sh`): 0 soglie bloccanti su 10, 0 da guardare su 8; foto al 38,4 % della pagina, 3 misure di H2, un solo titolo col punto (la citazione di Galileo), 4 filetti larghi, nessun mono, nessun badge, nessuna freccia, nessuna numerazione.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- Divieti del committente: nessun gradiente, nessun titolo in gradiente, niente Inter, niente icone, niente card, niente vetro, niente corsivo serif d'accento, niente legende numerate.
- PNG temporanei cancellati (anche quelli grandi in `_prova/cieco/`).
