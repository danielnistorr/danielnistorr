# Tek.Lam S.r.l., proposta di nuova home

Proposta non richiesta: solo la home, da mostrare all'azienda. Non è pubblicata e l'azienda non è stata contattata.

- `01-analisi.md`: azienda, sito di oggi, fatti con le fonti, materiale visivo, direzioni artistiche, riferimenti.
- `sito/`: la home finale (`index.html`, `img/`, `fonts/`). Si apre con file:///.
- `screenshot/home/`: home intera e prima schermata a 1440 e a 390, più `NOTA.md` (idea, caratteri, colori, interazione, foto, controlli).
- `assets/originali/`: le immagini del sito teklam.it. `assets/esterne/`: foto Unsplash e Pexels usate solo come segnaposto, con le licenze in `assets/CREDITI.md`.
- `_prova/`: lavoro di servizio (crawl, riferimenti, prototipo A, script). `bash _prova/script/build_finale.sh` rifà immagini, pagina, controlli e screenshot.

## L'idea in una riga

Il raggio rosso del logo (taglio e piega in un tratto) esce dal logo, scende accanto al titolo e gira a 90 gradi. Diventa la quota 3000 del foglio, e il foglio è la cornice della loro foto di saldatura sull'inox col film blu.

## Da confermare con Tek.Lam prima di pubblicare (oggi non a vista in pagina)

- Spessori massimi del laser: la home dice 20/15/10 mm (ferro, inox, alluminio), la pagina Attrezzature 25/15-20/12 mm. Finché non si sceglie restano fuori. Quando arriva il dato, nella scheda Taglio laser va il selettore ferro, inox, alluminio con lo spessore massimo come barra in scala reale (innesto della direzione B), come unico elemento interattivo della scheda.
- Portata delle piegatrici: la home dice 3100 × 100 t e 3100 × 125 t, Attrezzature 3100 × 120 t e 3100 × 100 t. In pagina c'è solo la lunghezza utile, 3100 mm.
- La foto Trumpf TrumaBend V170 caricata nel 2024: è una macchina nuova in officina? Se sì, l'elenco delle attrezzature è vecchio e la scheda Piegatura va aggiornata.
- Zincatura: tolta dalla pagina. Attrezzature cita solo verniciatura e cromatura su impianti esterni.
- Cesoia Gasparini: in pagina solo "fino a 3000 mm di lunghezza". Lo spessore ("sp. 6 8") è da chiarire.
- Autocarro centinato: "7,5 di pianale", unità da chiarire (non in pagina). L'autocarro con gru è scritto "35 q complessivi", come nella fonte.
- Indirizzo: "Via del Lavoro, 68" (contatti) o "Viale del Lavoro, 68" (privacy). In pagina c'è Via.
- PEC e data di costituzione della S.r.l., da aggiungere nel piede.
- Lavorano per la moda o la pelletteria del distretto? Non scritto.
- Certificazioni, numero di macchine, superficie dell'officina, clienti citabili, anni o pezzi di un lavoro con nome: oggi non ci sono. Un lavoro con nome e anno sarebbe il contenuto più forte da aggiungere.
- Dati Atoka (8 dipendenti, 1,0 milioni di ricavi): non usati senza consenso.
- Le righe sotto i settori vengono dalle schede di Realizzazioni del loro sito: chiedere se sono ancora rappresentative.
- Link Privacy e Cookie: puntano alle pagine di oggi su teklam.it, da rifare con il nuovo sito.

## Foto

Sono loro quasi tutte quelle in pagina: slide1, slide3, slide4, laserbystronic, fabbrica, automezzi, scaricate da teklam.it. L'uso e il consenso delle persone ritratte (il saldatore, la mano sulla piegatrice) vanno confermati. È di repertorio solo la foto della scheda Taglio laser (Clayton Cardinalli, Unsplash License), segnata "Foto indicativa".

Da rifare dal vero (mezza giornata di fotografo in officina, luce naturale dai portoni più due lampade morbide, niente flash diretto, file da almeno 3000 px di lato lungo):
1. Apertura, al posto di slide1 (che è un fotogramma da telefono di 1330 px). Stessa scena: saldatura TIG su un pezzo inox col film blu stampato. Ripresa orizzontale 2:1 a mezzo busto, la torcia a due terzi verso destra, lo sfondo d'officina sfocato (f/2.8). Più una versione verticale 1:2 stretta sulle mani e sulla torcia per il telefono.
2. Un pezzo vero di Tek.Lam tenuto in mano davanti al foglio da cui è uscito (idea presa da Bystronic): per esempio un case elettromedicale o un telaio per banco frigo. Fondo grigio neutro, a fuoco il pezzo. Può diventare l'apertura.
3. La Byspeed intera in orizzontale con una lamiera tagliata sul piano e lo scheletro del nesting. Sostituisce la foto di repertorio della scheda Taglio laser.
4. La SG6 con il pezzo separato e impilato all'uscita (oggi c'è la macchina di fronte, con il marchio in primo piano e la luce piatta).
5. La piegatrice: la mano sulla lamiera contro gli utensili, più luminosa di slide4 (oggi sottoesposta e morbida), sia orizzontale 2:1 sia verticale 4:5.
6. Tubi e profili: la Pedrazzoli con un tubolare curvato, e le barre tagliate dalla OMES. Oggi la scheda ha solo il disegno delle sezioni.
7. Sede e mezzi a 3000 px: la palazzina con l'acero rosso e i due autocarri, in una giornata coperta. Oggi sono a 470 px.
8. Sandro e Dimitri Volpato in officina, ripresi sul lavoro e non in posa.

## Caratteri e licenze

- Mona Sans (Google Fonts), SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL-MonaSans.txt`.
- Foto di repertorio: Unsplash License (dettagli e URL in `assets/CREDITI.md`).

## Loghi

Il logo in testata e nel piede è ritagliato dal PNG verticale del loro sito (`2020-07-logo-TEKLAM.png`, 1772 px): il segno a 120 px di altezza, la scritta a 64 px. Serve il logo vettoriale (SVG o PDF) da Tek.Lam. Il punto del raggio da cui parte la linea rossa è preso dal segno (ugello al 44,6 % della larghezza, 62 % dell'altezza): se il logo cambia, va ritarato nello script della pagina.

## Righe "da guardare" dei controlli (segnali.sh)

- H2 di due misure (72 e 124 px): voluto. Un elemento grande per vista, il titolo d'apertura e "Mandaci il disegno" sul campo rosso.
- "1 altro gradiente": è il tratteggio del raggio rosso, non una sfumatura.
- Area foto al 35 %, sulla soglia: salirà con le foto nuove a piena risoluzione.

## Prototipo B, "Scintilla e spessore" (`_prova/home/b/`)

Seconda direzione per la home, da mostrare accanto a quella in `sito/`: apertura nera con la foto di un taglio laser e "Lamiera conto terzi" in grande, poi lo spessore massimo di taglio (ferro 20, inox 15, alluminio 10 mm) disegnato in millimetri veri con un interruttore. Idea, caratteri, foto e controlli in `_prova/home/b/nota.md`.

Da confermare prima di mostrarla come definitiva: gli spessori (la home di oggi dice 20/15/10, Attrezzature 25/15-20/12: il prototipo usa 20/15/10 ed è l'unica pagina dove il dato è a vista); la forma "la famiglia Volpato lavora il metallo dal 1978"; il taglio OMES "fino a 120 mm" (diametro o lato); l'uso delle foto slide1 e automezzi.

## Prototipo A, "Il foglio annidato" (`_prova/home/a/`)

Rifatto da zero dopo la bocciatura del primo A (in `_prova/home/vecchio-a/`). La prima schermata è un foglio di inox spazzolato 3000 x 1500 in proporzione vera (1500 x 3000 sul telefono): TEK.LAM tagliato e già uscito, sei pezzi ancora annidati, uno per lavorazione; si tocca un pezzo, si stacca e il cartellino sul resto del foglio mostra macchina e misure. Idea, caratteri, foto e controlli in `_prova/home/a/nota.md`. Si rifà con `python3 -I _prova/script/proto_a_img.py` e `python3 -I _prova/script/proto_a_build.py`.

Da confermare prima di mostrarlo come definitivo (oggi non a vista):
- spessori massimi del laser (20/15/10 o 25/15-20/12 mm) e portata delle piegatrici (100, 120 o 125 t): in pagina solo campo di lavoro e lunghezza utile 3100 mm;
- portata dell'autocarro con gru (la fonte dice "35 qli complessivi") e "7,5 di pianale" del centinato: in pagina solo "autocarro con gru" e "50 quintali di portata utile";
- se la TrumaBend V170 della foto del 2024 è in officina: allora la riga Piegatura va aggiornata;
- se `2020-08-pc.jpg` (render CAD) è un modello del loro ufficio tecnico: oggi la didascalia resta generica;
- la cesoia Gasparini ("fino a mm 3000 di lungh. x sp. 6 8"): in pagina solo la lunghezza;
- i link "La lavorazione per esteso" puntano a pagine che non esistono ancora (`lavorazioni/...`).
