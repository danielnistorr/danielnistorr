# Bordin Garden & Vivai: proposta di nuova homepage

Proposta non richiesta, solo la home. Non è stato contattato nessuno, niente è pubblicato.

- **Home**: `sito/index.html` (statica, si apre col browser), `sito/img/`, `sito/fonts/`. Livello professionale del 3 novembre 2026, con il ritocco finale dello stesso giorno (apertura a tutta altezza, 1955 grande, lavori uno per riga con un prima e dopo vero, pagina a 390 più corta); la versione 1 di prima è in `_prova/versione-1-originale/`.
- **Screenshot**: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440) e la nota `screenshot/home/NOTA.md` (sezione "Livello professionale", con l'esito delle 15 regole).
- **Rifare tutto**: `bash _prova/script/build_finale.sh --immagini` (immagini `pro_img.py`, screenshot `pro_shoot.mjs`, controlli `pro_controlli.mjs`); prove d'uso (stato aperto/chiuso, menu, modulo, JavaScript spento): `node _prova/script/pro_uso.mjs`.
- Analisi con le fonti: `01-analisi.md`; scheda d'uso: `_prova/uso/SCHEDA.md`; crediti delle immagini: `assets/CREDITI.md`.

## Il modulo da collegare

Il modulo "Chiedete un sopralluogo" oggi **non invia nulla da solo**: il bottone "Apri l'email già scritta" compone un'email (mailto a info@bordingarden.it, oggetto "Richiesta di sopralluogo, comune (tipi)", nel testo nome, telefono, comune, metri quadri, che cosa serve e le due righe) che il visitatore spedisce dal suo programma di posta. Nel sito vero va collegato a un servizio di invio (per esempio il modulo del CMS, Formspree o un piccolo script sul server) che:

- accetti l'**allegato** (foto o disegno dello spazio; oggi va aggiunto a mano all'email o mandato su WhatsApp);
- mandi la richiesta a chi la segue davvero e una conferma al cliente;
- abbia l'informativa privacy e la casella del consenso.

**La prima cosa da chiedere** (il cliente tipo dei giardini non ha trovato la risposta, ed è la ragione per cui era venuto): **chi risponde alle richieste di giardino ed entro quando**, e se il sopralluogo è gratuito. Una recensione del 2023 racconta un preventivo chiesto e mai richiamato. Con la risposta, una frase sopra il modulo e nel messaggio dopo l'invio, per esempio "Vi richiama [nome], che segue i giardini, entro [due giorni lavorativi]": oggi in pagina non c'è, perché non è nelle fonti. Chiedere anche se l'indirizzo giusto è info@bordingarden.it o un altro. Finché resta il mailto, chi non ha un programma di posta vede solo il messaggio con l'alternativa (email scritta a mano o WhatsApp).

## Da chiedere all'azienda

1. **Recensioni**: oggi in pagina non ce n'è nessuna (nel markup, in fondo alla storia, un commento segna dove vanno). Nelle fonti ci sono solo sintesi degli estratti (voto Google 4,3 su 95 recensioni secondo Angoli Verdi, 4,23 su 136 su Cylex): chiedere il link alla scheda Google e il permesso di citare 3 o 4 recensioni intere con nome e comune (quelle sulle commesse, sull'assortimento, sull'aiuto a imballare). Con quelle la regola delle prove passa.
2. **Lavori con i dati**: per Villa Palladiana, il Giardino a Venezia e l'aiuola del prima e dopo (pagine 12 e 13 del book): anno, comune, metri quadri, che cosa hanno fatto (progetto, impianto, trapianto, manutenzione), e se i nomi si possono citare. Per Villa Palladiana e Venezia servono anche le foto del **prima** (gli album le hanno, ma con il logo stampato e il sito di oggi blocca lo scarico): con quelle ogni lavoro avrebbe la sua coppia prima e dopo. Il giardino con l'acero (`Giardini_3ok`, dalla slide "Giardini") è tolto dalla pagina finché non confermano che è un loro lavoro; lo stesso per la corte con la pergola di `Giardini_4` (è il giardino di Venezia o un altro?).
3. **Clienti, fornitori, associazioni**: architetti o imprese con cui lavorano (il book li cita senza nomi), **i marchi di vasi, terricci e arredo che vendono nel Garden** (per una fascia "Nel Garden trovate" con i nomi scritti in un solo colore), associazioni (florovivaisti, garden center): con il permesso, una fascia di nomi. Nella foto del reparto delle piante grasse (G8) il cartello dice "Garden Bordin, socio A.I.A.S.": sono ancora soci dell'associazione degli amatori delle piante succulente? Se sì, è una prova da scrivere (oggi non è in pagina).
4. **Garanzia d'attecchimento di un anno** (book "I nostri giardini"): vale ancora e per quali piante? In pagina è nei numeri ("1 anno") e sotto i 4 passi.
5. **Orari**: stagionali, domeniche di primavera (Cylex segnala domeniche mattina), chiusure estive, festività (oggi nei giorni di festa la pagina dice "Oggi è festa: chiamate prima di passare"). Il sabato del vivaio è ancora "mattina, su appuntamento"? Se cambiano, vanno cambiati nell'oggetto `ORARI` dello script in fondo alla pagina, nelle due tabelle e nel piede.
6. **Consegna a domicilio**: Google la dichiara per il Garden; non è in pagina finché non la confermano. Il cliente tipo del Garden l'ha cercata (vasi grandi, terriccio): appena confermata, una voce nell'elenco del Garden e una riga nella scheda.
7. **Ragione sociale nel piede**: ho messo quella dei registri (Bordin Garden & Vivai S.n.c. di Bordin Omero e Giuliano Società Agricola, P.IVA 01315760288, REA PD-231319). Va chiarito il ruolo di Commerciale Garden Bordin snc (P.IVA 02463340287, via dei Vivai 6) per il Garden e per i giardini. PEC e capitale sociale non trovati.
8. **Privacy e cookie**: l'indirizzo dell'informativa iubenda (nel piede oggi "Privacy e cookie" è scritto ma non è un link). Nella riga legale manca anche il **credito dello studio**: va aggiunto quando è deciso il nome con cui firmiamo (nel modello della PEC è ancora "[Agenzia]").
9. **Terza generazione**: nomi e ruoli, se vogliono comparire (con una foto delle persone la storia sarebbe loro davvero).
10. **Firewall del sito attuale** (BitNinja): verificare da un telefono in 4G se blocca anche i visitatori veri (analisi, sez. 9). Il link "Tutti i 33 album" porta al sito di oggi.
11. **Tempi e manutenzione**: nel passo 3 "Tempi" manca un ordine di grandezza (entro quanto fate il sopralluogo, in che mesi si pianta); il book parla solo di "manutenzioni straordinarie": fate anche la manutenzione ordinaria? Con le risposte si riscrivono i passi 3 e 4.

## Foto da rifare dal vero

Oggi la pagina usa solo foto di Bordin prese dal loro sito, ma non sono una serie: luci e anni diversi, due album con il logo stampato nell'angolo (tagliato). Serve una giornata di foto con un solo fotografo, macchina su cavalletto, 6000 px di lato lungo, file RAW, stessa luce (mattino presto o cielo velato), senza auto e cartelli in vista.

1. **L'apertura (la più importante)**: la piramide dal punto di vista di G6, con l'olivo a nuvole, in formato 4:3 e 3:2, cielo velato o luce radente del mattino, piazzale vuoto.
2. **Le persone**: le commesse al banco o tra i bancali mentre aiutano un cliente (lo lodano tutte le recensioni), la famiglia davanti alla piramide, la squadra dei giardini con il mezzo.
3. **I reparti, tutti 4:3 con la stessa luce**: piante grasse e bonsai, terracotta, piante da interno, piante da esterno, arredo e regali.
4. **I giardini**: gli originali senza logo degli album (Villa Palladiana, Venezia), meglio se in coppia prima e dopo con la stessa inquadratura; due o tre giardini finiti in luce radente. Le due foto del prima e dopo del book sono scansioni a 1024 px con ombre dure: vanno sostituite dagli originali.
5. **Il vivaio**: un trapianto con la gru rifatto oggi, i filari, un esemplare in zolla in primo piano; il cartello o il camion con il marchio.

## Licenze

- **Foto in pagina**: tutte di Bordin Garden & Vivai (dal sito bordingarden.it e dal loro book "I nostri giardini" su sfogliami.it), usate come materiale loro: G6, G8, G5, G1, G10, VB2, BB1, gli album Villa Palladiana (DO_Mix_146 e 148) e Giardino a Venezia (DO_MorosiniDopo4), le pagine 12 e 13 del book (prima e dopo), il logo. Nessuna foto di repertorio, nessuna illustrazione, nessuna immagine generata dall'IA (decisione del committente: "niente").
- **Caratteri**: Zodiak (400) e Switzer (400, 600), Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale libero; i file non vanno ridistribuiti da soli). Serviti dalla pagina in `sito/fonts/`.

## Loghi

- Esiste solo il PNG 360x126 con trasparenza (`assets/originali/logo-bordin-360x126.png`): in pagina è a 150 px nella testata (112 sul telefono, 100 sotto i 375 px) e a 170 px nel piede, cioè a 2x o più. Basta fino a 180 px.
- Serve il **vettoriale** (SVG o PDF): chiedere a chi l'ha disegnato e il nome del carattere della scritta "Bordin".

## Pagine che il sito nuovo deve avere

Oggi i link portano alle sezioni della home (e il link agli album al sito di oggi); nel sito vero vanno a queste pagine: La storia; Garden (reparti, orari); Giardini con le voci di servizio (progetto chiavi in mano, trapianto di esemplari, giardini storici, piante per uffici, manutenzione) e l'album dei 33 giardini; Vivai (produzione, esemplari, spedizione); Lavora con noi; Privacy e Cookie.
