# Bordin Garden & Vivai: proposta di nuova homepage

Proposta non richiesta, solo la home. Non è stato contattato nessuno, niente è pubblicato.

- **Home finale**: `sito/index.html` (statica, si apre col browser), `sito/img/`, `sito/fonts/`.
- **Screenshot**: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440) e la nota `screenshot/home/NOTA.md`.
- **Rifare tutto**: `bash _prova/script/build_finale.sh` (immagini `fin_img.py`, screenshot `fin_shoot.mjs`, segnali); prove di larghezze, tastiera, tocco e collegamenti: `node _prova/script/fin_prove.mjs`. Gli script dello scontorno (`fin_esemplare_vb2.py` e simili) restano solo come traccia: la home non li usa più.
- Analisi con le fonti: `01-analisi.md`. Prototipi e giudizio: `_prova/home/a`, `_prova/home/b`, `_prova/giudizio.json`. Crediti delle immagini: `assets/CREDITI.md`.

## Dati da confermare con l'azienda

In pagina ci sono senza segni di dubbio, ma vanno fatti rileggere:

1. **Garanzia d'attecchimento di un anno** (book "I nostri giardini": "Tutte le piante utilizzate ... hanno una garanzia d'attecchimento di un anno"): vale ancora? In pagina è una frase grande: "Tutte le piante dei nostri giardini hanno un anno di garanzia d'attecchimento".
2. **Foto dell'apertura (VB2)**: la didascalia dice "Vivai Bordin. Esemplari a foglia caduca appena zollati". È stata fatta nel loro vivaio (via dei Vivai 14)? Che specie sono? Se lo confermano, la didascalia può dire il luogo e la specie.
3. **"In zolla o in vaso, spediti in tutta Italia"** (didascalia dell'apertura) e "Spedizione in tutta Italia, anche dei grandi esemplari": dal sito (pagina Vivai), da far rileggere.
4. **Foto "In giardino"** (`home--Giardini_3ok`, dalla slide "Giardini" della loro home): è un giardino fatto da loro? Si può mostrare (casa privata riconoscibile)? Serve l'originale senza il filtro con la vignettatura. **Foto "In vivaio"** (VB4): sono i loro campi?
5. **Orari**: stagionali, domeniche di primavera, chiusure estive? Il sabato dei Vivai è ancora "mattina, su appuntamento"? La riga "aperto adesso" usa gli orari della pagina Contatti: se cambiano, vanno cambiati nello script in fondo alla pagina (oggetto `ORARI`) e nella tabella della chiusura.
6. **Ragione sociale nel piede**: ho messo quella dei registri (Bordin Garden & Vivai S.n.c. di Bordin Omero e Giuliano Società Agricola, P.IVA 01315760288, REA PD-231319). Va chiarito il ruolo di Commerciale Garden Bordin snc (P.IVA 02463340287, via dei Vivai 6) per il Garden. PEC e capitale sociale non trovati.
7. **Terza generazione**: nomi e ruoli, se vogliono comparire.
8. **Firewall del sito attuale** (BitNinja): verificare da un telefono in 4G se blocca anche i visitatori veri (analisi, sez. 9).

## Foto da rifare dal vero

Oggi la pagina usa solo foto di Bordin prese dal loro sito, ma nessuna è all'altezza della proposta. Serve una giornata di foto, con la macchina su cavalletto, 6000 px di lato lungo, file RAW.

1. **L'apertura (la più importante)**: la stessa scena di VB2 rifatta bene: la fila degli esemplari appena zollati sul prato, in primavera con le prime foglie o in autunno con la chioma colorata, in luce radente del mattino o con cielo velato; macchina bassa, all'altezza delle zolle, obiettivo da 35 a 50 mm, formato orizzontale 2:1 con una seconda inquadratura quadrata per il telefono; sfondo pulito (siepe, senza case e ghiaia), rete delle zolle nitida a 2x. Una seconda foto ravvicinata della zolla (rete e legatura) per le pagine interne.
2. **L'interruttore**: lo stesso esemplare due volte, nei campi del vivaio e messo a dimora nel giardino del cliente, stessa inquadratura e stessa ora del giorno; in alternativa le coppie PRIMA e DOPO degli album "Impianto esemplari", se ci sono gli originali senza logo.
3. **Il Garden**: la piramide all'alba o col cielo velato, senza auto, carrelli e cartelli, dal punto di vista di G6.
4. **La chiusura**: le bletille davanti all'ingresso in luce radente del mattino, con la piramide sfocata dietro, in formato quadrato o 4:5.
5. **Album dei giardini**: due o tre giardini finiti in luce radente, senza persone e senza logo stampato.

## Licenze

- **Foto in pagina**: tutte di Bordin Garden & Vivai (dal sito bordingarden.it), usate come materiale loro: VB2, VB4, Giardini_3ok, G6, G1, logo. Le foto Unsplash di `assets/esterne/` (con licenza in `assets/CREDITI.md`) non sono usate nella home finale; l'olivo di Marsiglia del prototipo A e lo scontorno di VB2 sono stati tolti.
- **Caratteri**: Zodiak e Switzer, Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale libero; i file non vanno ridistribuiti da soli). Serviti dalla pagina in `sito/fonts/`.

## Loghi

- Esiste solo il PNG 360x126 con trasparenza (`assets/originali/logo-bordin-360x126.png`): in pagina è a 150 px nella testata e a 180 px nel piede, cioè a 2x. Basta fino a 180 px.
- Serve il **vettoriale** (SVG o PDF): chiedere a chi l'ha disegnato e il nome del carattere della scritta "Bordin". Non l'ho ricostruito in SVG perché il carattere non è riconosciuto con certezza e il risultato non sarebbe fedele.

## Pagine che il sito nuovo deve avere (link del menu e del piede)

Oggi i link portano alle sezioni della home o a `#`; nel sito vero vanno a queste pagine:

- **La storia** (dal 1955, la famiglia, la terza generazione)
- **Vivai** (la produzione, gli esemplari, in zolla e in vaso, la spedizione)
- **Garden** (la piramide, i reparti, gli orari)
- **Giardini**, con le cinque voci di servizio: Progetto chiavi in mano, Trapianto di esemplari, Giardini storici, Piante per uffici, Manutenzione
- **Album dei giardini** (i 33 album, prima, durante, dopo)
- **Notizie**
- **Lavora con noi**
- **Privacy** e **Cookie** (oggi su iubenda)

## Newsletter

Il modulo "Notizie dal Garden" (email, bottone "Iscriviti", consenso privacy) **non invia nulla**: va collegato a un servizio (Brevo o Mailchimp), con doppia conferma dell'iscrizione e l'informativa privacy aggiornata. Da decidere chi la scrive e ogni quanto (novità, fioriture, piante appena arrivate).
