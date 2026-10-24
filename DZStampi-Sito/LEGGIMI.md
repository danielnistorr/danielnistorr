# D.Z. Stampi: proposta di nuova home

Proposta non richiesta di nuova homepage per D.Z. Stampi S.r.l. (Grisignano di Zocco, VI). Solo la home, statica. Nessun contatto con l'azienda, nulla pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale; `sito/img/` (solo le immagini usate, JPEG e WebP in più larghezze); `sito/fonts/` (Bai Jamjuree 300, 400, 500 in WOFF2 con `OFL.txt`).
- `screenshot/home/`: screenshot a 320, 390, 768, 1024, 1440, 1920 e `NOTA.md` (idea, schermate, caratteri, colori, foto, controlli).
- `01-analisi.md`: fatti con fonti, voti delle foto, direzioni artistiche, riferimenti.
- `assets/CREDITI.md`: licenze delle foto; `assets/esterne/` le foto di repertorio, `assets/originali/` quelle del sito attuale.
- `_prova/script/build_finale.sh`: rifà tutto (scontorno dello stampo con `finale_scontorno.py`, immagini con `finale_img.py`, pagina da `finale_index.html`, screenshot con `finale_shots.mjs` e `finale_jpeg.py`, controlli con `rif_controlli.mjs`, che scrive `_prova/segnali-finale/controlli.json`). Lo stampo parte da `assets/esterne/unsplash-FizNN4mzOA0-3600.jpg`. Richiede Python con Pillow, NumPy e OpenCV, Node con Playwright. `rif_prova.mjs` fa screenshot di prova a qualunque larghezza.
- `_prova/home/a` e `_prova/home/b`: i due prototipi da cui è stata scelta la direzione A.

## Pagine di destinazione dei link (da creare nel sito nuovo)

La home punta a sezioni interne (`#settori`, `#lavorazioni`, `#macchine`, `#contatti`) e, dal piede, a queste pagine:

- `azienda.html` (Chi siamo) e `azienda.html#macchine` (Le macchine)
- `contatti.html` (Contatti): qui vanno i tre uffici con le loro email (Tecnico e commerciale dzstampi@dzstampi.com, Segreteria info@dzstampi.com, Amministrazione amministrazione@dzstampi.com), il fax e la PEC se confermata; in home restano solo telefono, info@, indirizzo con la mappa e fax
- `lavorazioni.html` con sei ancore: `#progettazione` (progettazione 2D e 3D), `#sls` (prototipi in sinterizzazione laser), `#pilota` (stampo pilota), `#multimpronte` (stampo definitivo multimpronte), `#collaudo`, `#manutenzione` (revisione e manutenzione)
- `settori.html` con tre ancore: `#medicale`, `#automotive`, `#alimentare` (qui va spiegato il sistema IML, che in home è solo nominato)
- `contatti.html#dove-siamo` (contatti e indicazioni dal casello A4)
- `area-riservata.html` (esiste oggi con utente e password: da chiedere se è ancora usata)
- `privacy.html`, `cookie.html`

Niente newsletter: l'azienda non ha notizie, fiere né cataloghi da comunicare e lavora solo con clienti aziendali su commessa. Niente colonna social: non ne esistono.

## Dati da confermare con l'azienda

- **REA**: "17248/V" nel piede del sito attuale contro "VI 181505" nei registri (companyreports.it). Per questo non è nella riga legale.
- **PEC** dzstampi@legalmail.it: compare solo in una pagina orfana (`en/home_eng.html`). Non messa.
- **Uffici ed email**: l'abbinamento Tecnico e commerciale dzstampi@, Segreteria info@, Amministrazione amministrazione@ segue l'ordine della tabella della pagina Contatti; da confermare. In home c'è solo info@ (indirizzo generale del piede del sito attuale); le altre due vanno nella pagina Contatti. Numeri diretti degli uffici: non pubblicati.
- **Macchine**: l'elenco è fermo al 2021 (11 macchine). È ancora quello? La Rettifica 500U non ha misure; le corse sono riportate come scritte nel sito (la ONA ha tre misure, la Mazak diametro e lunghezza).
- **Prototipazione SLS**: fatta in casa o commissionata? Il testo dice che progetti e lavorazioni sono realizzati "esclusivamente all'interno dell'azienda"; su questo si basano la frase della prima schermata ("Progetto e lavorazioni restano nella nostra officina"), quella del medicale e quella della sezione delle tappe.
- **Automotive**: in home c'è solo "Stampi per componenti dell'automobile"; quali componenti si possono nominare (e con quali foto) è da chiedere.
- **Settori**: quali pezzi medicali e automotive si possono nominare; clienti nominabili; certificazioni (ISO 9001?).
- **Pressofusione**: nei meta tag del sito c'è "pressofusione", nei testi no. Fanno anche stampi per pressofusione?
- **Orari d'ufficio**: non pubblicati, quindi assenti dalla chiusura.
- **Dimensioni e peso massimi degli stampi**, numero massimo di impronte, acciai e trattamenti: oggi non scritti; sarebbero la prova più forte da mettere in home.
- **Lingue**: la versione inglese (e le altre tre) servono ancora? La pagina delle bandierine va tolta comunque.
- **Diritti delle foto del sito attuale**: matrici e stampo aperto sembrano loro; le 11 macchine sono foto dei costruttori; `segretaria.jpg` è repertorio.

## Foto da rifare dal vero

Tutte le foto della proposta sono segnaposto Unsplash ("Foto indicativa" in pagina). Nessuna mostra D.Z. Stampi. Serve una giornata di fotografia in officina, con fondo continuo grigio chiaro e caldo (circa il #DEDCD7 della pagina), una luce grande e morbida dall'alto a sinistra e un taglio radente per far leggere i segni di fresa:

1. **Apertura**: una matrice finita di D.Z. Stampi (meglio la metà con le impronte e le colonne di guida, golfare montato), in piedi, vista di fronte e leggermente di tre quarti, scattata intera e larga in modo da poterla far uscire dal bordo destro e da quello in basso; acciaio pulito, senza grasso, impronte lucide. Esposizione chiara, nessun nero pieno sul fondo, tutta a fuoco (diaframma chiuso: la foto di repertorio ha il lato destro sfocato). Serve almeno 4000 px sul lato lungo. Le tre legende (golfare, colonna di guida, impronte) sono posate in percentuale sulla foto (`style` dei `.punto` e `.filo` in `finale_index.html`) e in `cqw` nel CSS (`.legenda .l1`, `.l2`, `.l3`): con la foto vera vanno rimisurate, e il testo della legenda 3 va adattato al numero di impronte vero.
2. **Settori**: per ognuno il pezzo stampato su fondo grigio chiaro, se possibile accanto alla sua impronta: medicale (i bisturi monouso che già mostrano nel sito, o un pezzo autorizzato), automotive (un componente vero), alimentare (una vaschetta o un secchiello IML decorato vero: il vasetto della proposta, schiarito e reso neutro, è un vasetto da cosmetici di repertorio e non è IML; una foto gratuita adatta non esiste su Unsplash e Pexels, vedi `assets/CREDITI.md`). Il fondo della sezione è il grigio caldo #DEDCD7.
3. **Lavorazioni**: un centro di lavoro Parpas a 5 assi in lavoro, mandrino e fresa sul pezzo, refrigerante in controluce, luce d'officina chiara; inquadratura larga e bassa (rapporto 3:1).
4. **Chiusura**: due o tre pezzi stampati finiti su grigio chiaro, oppure lo stampo aperto in luce pulita; deve essere diversa dalla foto dell'apertura.
5. **Sede**: la facciata di via del Lavoro 24/26, per la pagina Contatti.

Le due foto di Mastars usate nella home (`Epi5exvDtkU` e `Ec1mAEzKtRw`) vengono dal profilo di un'azienda cinese di stampi: nessun marchio visibile, ma vanno tolte prima della pubblicazione.

## Licenze

- **Foto**: Unsplash License (uso libero anche commerciale, senza obbligo di attribuzione, modifiche ammesse), verificata sulla pagina di ogni foto; elenco, autori e URL in `assets/CREDITI.md`. Nella home finale: `FizNN4mzOA0` (hosein fayton, scaricata a 3600 px, scontornata e schiarita), `1SutQMy6UVU` e `Rg0KmrUPB_Q` (Diana Polekhina), `Epi5exvDtkU` e `Ec1mAEzKtRw` (Mastars), `sxtClAGwRck` (aluminum Zheng ji).
- **Carattere**: Bai Jamjuree di Cadson Demak, da Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), servito dalla pagina in `sito/fonts/` con `OFL.txt`.

## Logo

Esiste solo `DZlogo.png` del sito attuale (352x172, PNG con trasparenza): monogramma "DZ" a pennello con ombre, D corallo e Z viola, più "STAMPI s.r.l.". Un SVG fedele non è realistico (pennellata con sfumature), quindi in testata è mostrato a 112 px e nel piede a 176 px, cioè a 2x. Serve il vettoriale dall'azienda (e un favicon, che oggi non c'è). Gli allori degli anniversari (25, 30, 35, 40 anni) non sono usati: in pagina c'è "dal 1985".
