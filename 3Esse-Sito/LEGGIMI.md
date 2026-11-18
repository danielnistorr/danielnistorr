# Tre Esse S.r.l., proposta di nuova home

Proposta non richiesta, solo la home. Niente è stato pubblicato, inviato o mostrato all'azienda.

## Dove sono le cose

- `sito/index.html`: la home finale "Registro delle opere", costruita sulla bozza B scelta dal committente. È statica e si apre con file:///. In `sito/img/` ci sono solo le immagini usate (JPEG in più larghezze); in `sito/fonts/` Switzer con la licenza `FFL.txt`.
- `screenshot/home/`: `home-1440.jpg` e `home-390.jpg` (pagine intere), `home-1440-prima-schermata.jpg` (1440x900), `home-390-prima-schermata.jpg` (390x844), `chiusura-1440.jpg` (solo la chiusura: frase, recapiti, foto e piede) e `NOTA.md` (idea, caratteri, colori, interazione, foto, ispirazioni, controlli).
- `_prova/script/build_finale.sh` rifà tutto: immagini con `finale_b_img.py`, pagina da `finale_b_pagina.html` con i controlli, screenshot con `finale_b_prima.mjs` e `finale_b_chiusura.mjs`. La chiusura è stata rifatta il 20/10/2026 nello stile B scelto dal committente: la frase su cosa fa lo studio, i recapiti in poche righe e a destra la foto dell'arco di Wesley Li (Unsplash, segnaposto); il piede è una riga sola su carta (il perché è in `NOTA.md`). Di questa home non esiste una versione WordPress da rigenerare. Gli altri controlli sono in `finale_b_controlli.mjs`, gli esiti di `segnali.sh` in `_prova/segnali-finale/`.
- `_prova/home/a/` e `_prova/home/b/`: le due bozze. La versione costruita prima sulla A (scartata) ha gli script in `_prova/script/scartata-a/`.
- `01-analisi.md`: i fatti con le fonti. `assets/CREDITI.md`: l'origine di ogni immagine.

## Dati da confermare con l'azienda prima di pubblicare

In pagina ci sono solo fatti presi dal sito e dai due PDF (fonti in `01-analisi.md`, luoghi e anni dal portfolio del 2013). Restano da confermare:

- **Il registro delle opere**: 34 opere, tutte del portfolio del 2013 o delle pagine del sito. 26 hanno l'anno; le altre 8 (senza anno nelle fonti) stanno in fondo sotto "Altre opere", senza colonna dell'anno.
  - Rochdale (2012) e Birley Fields (2013) a Manchester sono ora due righe, come nel portfolio: facciate in acciaio ("courtain wall design (steel struct.)").
  - Centro direzionale Giotto: anno 2007 e Padova dal portfolio ("RETAIL AND BUSINESS CENTER GIOTTO, PADOVA", 2007). Centro commerciale Alimarket: Padova dal titolo della sua scheda nel sito.
  - Il ruolo di Tre Esse in ognuna. Nel portfolio quasi tutte sono "engineering and detailing"; il registro non lo scrive riga per riga.
  - Si possono citare tutte per nome?
  - Il KAFD di Riyad (facciata in acciaio e vetro): che lavoro ha fatto Tre Esse?
  - L'"Edificio industriale, Emirati Arabi Uniti, 8000 t" nel portfolio è di Danieli. Il nome del cliente resta fuori finché non c'è il permesso.
- **Opere dopo il 2013**: il portfolio si ferma lì. Senza lavori recenti il registro mostra uno studio fermo, quindi vanno chiesti e messi in testa.
  - Per questo l'estratto della prima schermata (Emirati 8000 t, Molino Stucky 250.000 m³, Adria 700 t) non mostra gli anni. Quando arrivano tre opere recenti con i loro numeri, vanno messe lì al posto di queste, con l'anno.
- **Anni mancanti** per le 8 "Altre opere": Ponte sul Brenta, Centro commerciale Alimarket, Chiesa di San Francesco, ex zuccherificio di Cavarzere, campanile di Montecchia di Crosara, centrali di Castegnero, Maleo e Meduno. Con l'anno passano nel registro principale.
  - Il "Ponte sul Brenta, Corte di Piove di Sacco" del sito è il "Bridge inox a Corte, Piove di Sacco, 2006" del portfolio? Se sì è in acciaio inox, non in cemento armato, e va spostato tra i ponti (i conteggi dei filtri cambiano).
- **Lasciate fuori di proposito**:
  - Nancy e Brest (2013), la stazione di Mons (Calatrava), Trecenta e Montegrotto, ILVA, ABS Udine, tralicci Terna, Acciaierie Venete;
  - i clienti (Danieli, Terna, Permasteelisa e gli altri della pagina Presentazione), i nomi del consiglio, i partner LAIRA e TSA.
  - Si possono citare?
- **Adria**: il portfolio scrive "Steel weight: 700 tons, Diametr: 90m" per l'intera opera. Bisogna confermare che i 90 m siano il diametro della cupola della foto.
- **Anno di fondazione**: 1999 per il sito, 1990 per il profilo. In pagina non c'è.
- **Certificazione ICIM ISO 9001 n. 2213/7**: il certificato pubblicato è scaduto il 05/03/2026. In pagina non c'è finché non arriva il rinnovo, con il numero giusto (2213/7 o 2213/6).
- **Sede**: Via San Marco 14 a Vigonovo è in pagina come "Ufficio". È sede legale o operativa? L'ufficio di Via del Cristo 378 a Padova (citato nel profilo) esiste ancora?
- **Email**: in pagina c'è info@3essesrl.com (dal sito); il profilo dà tre.esse.srl@libero.it.
- **Fax 049 87 05 572**: è ancora attivo? Se no si toglie.
- **Studio**: le 24 postazioni, i software (SAP2000, CDM Dolmen, SuperSAP, Straus7, Tecnometal, Bocad, Prosteel) e gli strumenti (Trimble 5503, Zeiss DiNi 11, Larson Davis LD-831) vengono dalla pagina Presentazione e in pagina sono una tabella (Calcolo, Disegno, Rilievo, Acustica). Sono ancora quelli? Il titolo "Ventiquattro postazioni a Vigonovo" dà per scontato che le postazioni siano tutte nella sede di Vigonovo: se una parte è a Padova (Via del Cristo) il titolo diventa "Ventiquattro postazioni".
- **Privacy**: manca la pagina dell'informativa. Il link nel piede va aggiunto quando c'è.

## Foto da rifare dal vero

Le due foto grandi della home (apertura e fascia) sono **segnaposto di repertorio** (Unsplash, Helsinki e Vancouver): non sono opere di Tre Esse e in pagina non hanno didascalia. Non si pubblica finché non sono sostituite con foto delle loro opere. Il trattamento resta lo stesso (`finale_b_img.py`: basta cambiare il file sorgente e il taglio).

1. **Apertura**: il cavalcaferrovia Sarpi o il Ponte Verde a Padova, a pochi chilometri dalla sede. È la correzione più importante: oggi la prima schermata mostra un ponte di Helsinki e con il nome di un concorrente reggerebbe uguale. Il materiale dell'azienda che c'è non basta (le foto del Sarpi nel portfolio sono di notte e larghe 922 px; quelle del sito sono a 500 px con la filigrana).
   - Quando c'è la foto vera, sotto l'immagine va una legenda piccola con nome e anno dell'opera (per esempio "Cavalcaferrovia Sarpi, Padova, 2008"), come le righe del registro.
   - Visti da sotto, in asse con l'impalcato, così che l'acciaio occupi la metà alta e le pile o le spalle scendano verso il titolo.
   - Mattino con cielo coperto chiaro (il cielo deve diventare la carta), obiettivo 24-35 mm, treppiede, almeno 6000 px di lato lungo.
   - Serve anche un taglio verticale per il telefono, centrato sull'appoggio.
2. **Fascia**: un nodo bullonato o una controventatura di una loro opera in acciaio, vista dal basso contro lo stesso cielo chiaro. Almeno 3200 px di larghezza: il segnaposto di oggi è la stessa foto Unsplash scaricata a 3200 px, nitida anche su schermo 2x.
3. **Cupola di Adria**: il ritaglio del portfolio è di 1155x865 px, un po' grigio e compresso. In pagina ora è intera, larga al massimo 800 px, ripulita dai blocchi JPEG e con più contrasto locale: a 1x è nitida, su schermo 2x è ancora un po' morbida. Servono l'originale senza compressione, oppure una foto nuova dal centro della cupola, in asse con l'oculo, con luce diffusa e almeno 2400 px.
4. Le 223 foto della galleria del sito attuale sono a 500 px con la filigrana "3 Tre Esse s.r.l." e non sono usabili: chiedere gli originali.
5. Diritti: le foto del portfolio sono dell'azienda o dei fotografi delle imprese e dei committenti? Va chiarito prima di usare la cupola.

## Logo

In pagina il marchio è "Tre Esse" scritto in Switzer 500. Il logo vero (il "3" verde) esiste solo dentro l'immagine della testata del sito attuale (1024x267, su fondo sfumato). Serve il vettoriale (AI, EPS, SVG o PDF); poi si decide se usarlo nella testata.

## Licenze

- Carattere: Switzer (Indian Type Foundry), da Fontshare, ITF Free Font License 2.0, testo in `sito/fonts/FFL.txt`. Ammette l'uso commerciale e il self-hosting sul sito dell'azienda; i file non vanno modificati né convertiti. Al momento di pubblicare conviene che l'azienda scarichi i file da fontshare.com a suo nome.
- Foto di repertorio: Unsplash License (uso commerciale libero, attribuzione non richiesta, non si rivendono le foto così come sono). Dettagli in `assets/CREDITI.md`.
- Materiale di Tre Esse (cupola di Adria): l'uso va confermato con l'azienda.
- Nessuna immagine generata dall'IA.
