# Tek.Lam S.r.l., proposta di nuova home

Proposta non richiesta: solo la home, da mostrare all'azienda. Non è pubblicata e l'azienda non è stata contattata.

- `01-analisi.md`: azienda, sito di oggi, fatti con le fonti, materiale visivo, direzioni artistiche, riferimenti.
- `sito/`: la home finale, "Scintilla e spessore" (`index.html`, `img/`, `fonts/`). Si apre con file:///. Viene dal prototipo B e sostituisce la versione "Il foglio annidato", bocciata.
- `screenshot/home/`: home intera e prima schermata a 1440 e a 390, più `NOTA.md` (idea, prime due schermate, caratteri, colori, interazione, foto, controlli).
- `assets/originali/`: le immagini del sito teklam.it. `assets/esterne/`: foto Unsplash e Pexels scaricate come segnaposto, licenze in `assets/CREDITI.md`. `assets/web/` contiene le immagini della versione bocciata e non serve alla home finale.
- `_prova/`: lavoro di servizio (crawl, riferimenti, prototipi A e B in `_prova/home/`, script). `bash _prova/script/build_finale.sh` rifà immagini, carattere, pagina, controlli (anche menu, righe del percorso e larghezze da 320 a 2560 con `rifinitura_prova.mjs`) e screenshot; gli script della versione bocciata sono in `_prova/script/vecchio-foglio/`.

## L'idea in una riga

L'officina di notte: la scintilla del laser su nero pieno, poi lo spessore che quel laser taglia disegnato in millimetri veri, con l'interruttore Ferro, Inox, Alluminio; il percorso del pezzo dal file al camion in sette righe, ognuna con lavorazione, macchina e misura.

## Da confermare con Tek.Lam prima di pubblicare

1. **Spessori massimi del laser, bloccante: non pubblicare senza la conferma scritta di Tek.Lam.** In pagina (interruttore e sezione disegnata in millimetri) ci sono quelli della home del loro sito, 20 mm ferro, 15 inox, 10 alluminio ("spessore max di taglio 20mm di ferro, 15mm inox, 10mm alluminio"). La pagina Attrezzature dice 25 (fe), 15/20 (inox) e 12 (alluminio). Il gesto della pagina si regge su questo dato. Per cambiarlo: `data-t` dei tre bottoni, le tre quote della legenda e delle guide in `_prova/script/finale_pagina.html`, e il controllo in `controlla_finale.py`.
2. Piegatrici: in pagina "Finn-Power 8 assi e Warcom, lunghezza utile 3100 mm". Le portate non coincidono (home "3100x100 T e 3100x125 T", Attrezzature "3100×120 t" e "3100×100 t") e non sono in pagina. La Trumpf TrumaBend V170 della foto caricata nel 2024 è in officina? Se sì, la riga 04 va aggiornata.
3. Riga 06, tubi e profili: in pagina "OMES, Ercolina, Pedrazzoli, curvatura 20 × 20 × 3" (dalla frase "quadro vuoto 20x20x3": è la sezione massima curvabile?). Troncatrice OMES "fino a 120 mm": diametro o lato? Non in pagina.
4. Riga 07: "Due autocarri propri, centinato da 50 q, con gru" (Attrezzature: "Autocarro centinato con 50 qli di portata utile", "Autocarro con gru da 35 qli complessivi"). Sono ancora due? I 35 quintali sono portata o massa?
5. Riga 03: "Finn-Power SG6, pezzo separato e impilato" riassume "completa di automazione di carico/scarico impilaggio e separazione". La cesoia Gasparini ("fino a mm 3000 di lungh. x sp. 6 8") non è più in pagina.
6. Verniciatura, cromatura, sabbiatura e zincatura: in pagina "le seguiamo noi su impianti esterni collegati", dalla pagina Attrezzature. Ancora vero?
7. La storia: in pagina "La famiglia Volpato lavora il metallo dal 1978: prima piccoli manufatti in ferro battuto come FDS Volpato S.n.c., dal 2020 lamiera come Tek.Lam S.r.l." Il sito dice "l'esperienza dei fondatori, dal 1978", "carpenteria di piccoli manufatti in ferro battuto" e il passaggio del testimone nel blog del 16/09/2020. Confermare anno, forma e data.
8. Settori e note: dalle schede Realizzazioni del 2020. Ancora attuali? Lavorano anche per la moda o la pelletteria del distretto? Non scritto.
9. Indirizzo: "Via del Lavoro, 68" (contatti) o "Viale del Lavoro, 68" (privacy). In pagina c'è Via. PEC e data di costituzione per il piede.
10. Sandro e Dimitri Volpato: in pagina con nome, ruolo ed email, come nella loro pagina Chi siamo. Va bene che restino in home?
11. Certificazioni, numero di macchine, superficie dell'officina, clienti citabili, un lavoro con nome e anno: oggi non ci sono. Un lavoro con nome e anno sarebbe il contenuto più forte da aggiungere.
12. Dati Atoka (8 dipendenti, 1,0 milioni di ricavi): non usati senza consenso.
13. Uso della loro foto `2020-08-slide1.jpg` (sezione Famiglia) e consenso del saldatore ritratto.
14. Link: Privacy e Cookie puntano alle pagine di oggi su teklam.it, da rifare con il nuovo sito.

## Foto da rifare dal vero

In pagina ci sono due foto di repertorio con la dicitura "Foto indicativa" (apertura e fondo dei contatti) e una loro foto, un fotogramma da telefono di 1330 px allargato a tutta la finestra (sopra i 1440 px si vede morbida). La fascia della piegatrice sopra il percorso è uscita. Mezza giornata di fotografo in officina, di sera o a portoni chiusi, luce della macchina più una lampada calda radente, file da almeno 3000 px di lato lungo:

1. **L'apertura**: il loro Byspeed che taglia ferro spesso, ripreso basso al livello della lamiera, ugello al centro, scintille ai due lati, sotto almeno un terzo di buio per il titolo; tempo breve (1/250 o meno) per le scie nitide, f/4. Più una versione verticale 4:5 per il telefono, stretta sull'ugello. Con la foto vera la dicitura "Foto indicativa" sparisce dalla prima schermata.
2. **La famiglia**: la saldatura TIG sul cassone col film blu, stessa scena di `slide1` a piena risoluzione e in orizzontale largo (almeno 2,4:1 di ritaglio, perché va a tutta larghezza), e Sandro e Dimitri Volpato in officina al lavoro, non in posa.
3. **I contatti**: l'ugello del loro laser sul piano a punte, fermo, macchina spenta, luce radente; deve reggere scurito al 60 % sotto il testo, con la parte bassa calma (lì ci sono i recapiti).
4. Facoltativa: il bordo vero di una lamiera da 20 mm appena tagliata, in macro con luce radente, per affiancare la sezione disegnata.

## Caratteri e licenze

- Sofia Sans (Google Fonts), SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL-SofiaSans.txt`. Nessun altro carattere.
- Foto di repertorio: Le Trung e Cemrecan Yurtman (una foto), Unsplash License; URL, autori e note in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.

## Loghi

Il segno e la scritta in testata e nel piede sono ritagliati dal PNG verticale del loro sito (`2020-07-logo-TEKLAM.png`, 1772 px). Serve il logo vettoriale (SVG o PDF) da Tek.Lam per la versione definitiva e per confermare il rosso.

## Prototipi

`_prova/home/a/` ("Il foglio annidato") e `_prova/home/b/` ("Scintilla e spessore", scelto), ognuno con la sua `nota.md`. La prima schermata (scintille, "Lamiera conto terzi", "1978") resta com'è per scelta del committente, anche dopo il giudizio cieco che chiedeva di portarci lo spessore. Dal B la home finale tiene prima schermata, spessore e palette; il percorso del pezzo è rifatto da capo due volte (l'ultima: senza fascia fotografica, sette righe da 54 px, 573 px in tutto a 1440) e la pagina è passata da 9841 a 4749 px a 1440.
