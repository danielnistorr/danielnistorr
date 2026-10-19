# Tre Esse S.r.l., proposta di nuova home

Proposta non richiesta, solo la home. Niente è stato pubblicato, inviato o mostrato all'azienda.

## Dove sono le cose

- `sito/index.html`: la home finale "La tavola" (statica, si apre con file:///). `sito/img/` solo le immagini usate (WebP e JPEG in più larghezze), `sito/fonts/` Overpass con la licenza `OFL.txt`.
- `screenshot/home/`: `home-1440.jpg` e `home-390.jpg` (intere), `home-1440-prima-schermata.jpg` (1440x900), `home-390-prima-schermata.jpg` (390x844), più le due prime schermate nello stato "Opera" dell'interruttore. `NOTA.md` spiega idea, caratteri, colori, interazione, foto e controlli.
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (`finale_pagina.html`, con i controlli) e screenshot (`finale_prima.mjs` per i due stati dell'apertura).
- `01-analisi.md`: fatti con le fonti, materiale visivo, direzioni, riferimenti. `assets/CREDITI.md`: origine di ogni immagine.
- `_prova/home/a/` e `_prova/home/b/`: i due prototipi da cui è nata la versione finale (vince A).

## Dati da confermare con l'azienda prima di pubblicare

In pagina ci sono solo fatti presi dal sito e dai due PDF (fonti in `01-analisi.md`). Restano da confermare:

- Il cartiglio dell'apertura: "Calcolo e disegni costruttivi: Tre Esse" traduce "engineering and detailing" del portfolio (pagina 28). Va confermato il ruolo esatto nel Sarpi, e allo stesso modo nella cupola di Adria e nelle altre opere della tabella.
- I richiami della tavola (1 Arco, 2 Imposta) sono letti dal disegno: vanno confermati da chi l'ha fatto.
- Le dieci opere della tabella vengono dal portfolio del 2013. Nomi da verificare: "Ponte Komo" (nel PDF "Bridge Komo a Kango, Gabon"), "Centro congressi KAFD, facciata in acciaio e vetro" (nel PDF senza la dicitura "engineering and detailing": che lavoro ha fatto Tre Esse?), "Edificio industriale, Emirati Arabi Uniti" (nel PDF è di Danieli: il nome del cliente resta fuori finché non c'è il permesso).
- Opere dopo il 2013: il portfolio si ferma lì. Se ci sono lavori recenti vanno in testa alla tabella.
- Il link "Il portfolio completo" punta al PDF del 2013 sul sito attuale (http://www.3essesrl.com/pdf/Company-Project-Portfolio.pdf): va sostituito con una pagina opere o con un PDF aggiornato.
- Anno di fondazione: 1999 (sito) o 1990 (profilo). In pagina non c'è.
- Certificazione ICIM ISO 9001 n. 2213/7: il certificato pubblicato è scaduto il 05/03/2026. In pagina non c'è finché non arriva quello rinnovato (e il numero giusto, 2213/7 o 2213/6).
- Sede: Via San Marco 14 a Vigonovo è in pagina come "Ufficio"; è sede legale o operativa? L'ufficio di Via del Cristo 378 a Padova (profilo) esiste ancora?
- Email da pubblicare: in pagina info@3essesrl.com (sito); il profilo dà tre.esse.srl@libero.it.
- Fax 049 87 05 572: è ancora attivo?
- Le 24 postazioni, i software e gli strumenti (Trimble 5503, Zeiss DiNi 11, Larson Davis LD-831) vengono dalla pagina Presentazione: sono ancora quelli?
- Fuori dalla pagina, di proposito: clienti (Danieli, Terna, Permasteelisa e gli altri), la stazione di Mons di Calatrava, i nomi del consiglio, i partner LAIRA e TSA. Si possono citare?

## Foto e disegni da rifare dal vero

Tutto ciò che è in pagina è materiale di Tre Esse preso dal PDF del portfolio (2013). I diritti vanno confermati: sono dell'azienda o dei fotografi delle imprese e dei committenti?

1. **La tavola del Sarpi (apertura).** Oggi è ricostruita da un raster a 220 ppi. Servono i file originali: DWG o DXF, oppure il PDF vettoriale della tavola. Esportati in SVG o in PNG a 3600 px di lato lungo, il tratto sarà perfetto anche sugli schermi retina. Va bene anche una seconda tavola (Ponte Verde, Versa) per alternare.
2. **Il Sarpi finito (stato "Opera" dell'interruttore).** Oggi è la foto all'ora blu del PDF, 931 px, morbida. Da rifare in mezza giornata (il ponte è a Padova, a pochi chilometri dalla sede):
   - di mattina, cielo chiaro, in asse con l'arco, obiettivo 24-35 mm, almeno 6000 px, treppiede, nessuna auto in primo piano;
   - di sera, con lo stesso taglio della foto attuale (riflesso nell'acqua, ora blu, 20-30 minuti dopo il tramonto), esposizione lunga.
3. **La cupola di Adria.** Il ritaglio del PDF è 1155x865 e un po' grigio. Servono gli originali senza filigrana o una foto nuova da sotto, in asse con l'oculo, luce diffusa, almeno 4000 px.
4. **Per una fascia fotografica in più** (oggi le immagini coprono il 21 % della pagina a 1440): il Ponte Verde a Padova, la cupola di Adria da fuori, oppure una tavola stampata fotografata dall'alto su un piano di lavoro, in luce radente.
5. Le 223 foto della galleria del sito attuale sono a 500 px con la filigrana "3 Tre Esse s.r.l.": non sono usabili. Chiedere gli originali.

## Logo

Il "3" verde con "Tre Esse S.r.l." oggi è composto col carattere della pagina (il verde #2E7D4F è preso dal "3" della testata). Il logo vero esiste solo dentro l'immagine della testata del sito attuale (1024x267, con sfondo sfumato): serve il vettoriale (AI, EPS, SVG o PDF).

## Licenze

- Carattere: Overpass (Delve Withrington per Red Hat), SIL Open Font License 1.1, da Google Fonts; i file woff2 sono serviti dalla pagina e la licenza è in `sito/fonts/OFL.txt`. Uso commerciale libero.
- Immagini: solo materiale di Tre Esse (vedi sopra). Nessuna foto di repertorio, nessuna immagine generata. Le foto Unsplash scaricate per l'analisi in `assets/esterne/` non sono usate nella home finale.
