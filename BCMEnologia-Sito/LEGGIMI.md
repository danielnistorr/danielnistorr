# B.C.M. Enologia: proposta di nuova home

È una proposta non richiesta: una nuova homepage per B.C.M. Enologia S.r.l. di Saonara (PD), torchi, martinetti DAVID, gabbie, pompe Volumex con inverter e pigiatrici. Riguarda solo la home.

- **Pagina**: `sito/index.html`. È statica, si apre con un doppio clic. Le immagini sono in `sito/img/` e i caratteri in `sito/fonts/`. È la versione "alto livello" (prova della sezione D, 3/11/2026): DAVID a 220 px sopra le basi rosse dei torchi, "Compatibilità con il passato", cinque sezioni, 534 parole.
- **Screenshot e nota**: `screenshot/home/`. La nota (`NOTA.md`, sezione "Alto livello, prova della sezione D") dice regola per regola che cosa passa e che cosa no, con i numeri di prima e di dopo.
- **Rifare tutto**: `python3 -I _prova/alto/script/pro_img.py` (immagini), `node _prova/alto/shots.mjs` (screenshot all'ora simulata lunedì 2 novembre 2026 alle 10), `node _prova/alto/misura-d.mjs` (controlli della sezione D). La pagina prende anche `?ora=AAAA-MM-GGTHH:MM` (ora di Roma) per provare lo stato "Aperto ora". La direzione è in `_prova/alto/DIREZIONE.md`.
- **Versioni di prima**: il livello professionale con il ritocco finale (modulo, rivenditori, fascia delle cifre) in `_prova/versione-pro/`; il torchio sulla carta con il selettore in `_prova/versione-1-originale/`.
- **Analisi con le fonti**: `01-analisi.md`; chi apre il sito e perché: `_prova/uso/SCHEDA.md`.

Nessun contatto con l'azienda, nessun modulo inviato, niente pubblicato.

## Ricambi: email in home, modulo in una pagina nuova

In home non c'è più il modulo. Il bottone "Mandaci le foto per email" apre un'email a info@bcmenologia.com con l'oggetto "Ricambio per la mia macchina BCM" e la traccia già scritta (macchina e modello dalla targhetta, diametro della gabbia o della vite, pezzo da cambiare, nome e telefono); le foto si allegano a mano. Il modulo "Scrivici" della versione di prima (in `_prova/versione-pro/sito/index.html`) va nella pagina nuova Ricambi e assistenza.
- Nel sito vero quella pagina va collegata a un servizio di invio (per esempio il modulo del CMS con SMTP, Formspree o Netlify Forms), con il caricamento delle foto (targhetta e pezzo, JPEG fino a 10 MB), l'informativa privacy e una risposta automatica.
- Va deciso con BCM chi legge le richieste e in quanto tempo risponde: in pagina non c'è nessuna promessa di tempi perché non è nelle fonti.

## Da chiedere o confermare con BCM prima di inviare

- **Stato della società**: un estratto la diceva cessata, mentre aziende.it la dà "Attiva" e reportaziende pubblica ricavi 2025. Va verificato per primo.
- **Ragione sociale e civico**: in pagina "B.C.M. Enologia S.r.l." (registro) e viale Veneto 10-12 (cataloghi e registro; il sito dice 10).
- **Orari e chiusure**: lo stato "Aperto ora" usa lunedì-venerdì 8-18 e chiude nei festivi nazionali e a Pasquetta. Vanno chiesti la pausa pranzo, le ferie d'agosto e di Natale e l'orario in vendemmia. Le ferie si scrivono nell'elenco `chiusure` dello script in fondo alla pagina (coppie di date, per esempio `[['2027-08-09','2027-08-20']]`): in quei giorni lo stato dice "Chiusi per ferie, riapriamo il ...". Oggi l'elenco è vuoto.
- **Fuori orario**: quando è chiuso, la pagina propone di mandare le foto per email. Va chiesto se vogliono aggiungere una promessa ("ti richiamiamo il giorno dopo"): oggi non c'è, perché non è nelle fonti.
- **Ricambi**: in pagina "da oltre 30 anni teniamo i ricambi e facciamo la manutenzione di ogni singolo componente" e "Compatibilità con il passato", parole loro (scheda torchi e brochure martinetti). La riga di esempi dei pezzi della versione di prima è tolta dalla home finché BCM non la conferma. Vanno chiesti anche dove sta la targhetta su torchi e pompe, l'elenco dei ricambi più richiesti (martinetti, manometri, listelli, cerchi, tappi e mezzelune, giranti e tenute delle pompe), se tengono anche i pezzi delle macchine della vecchia B.C.M. snc e un esempio vero di macchina vecchia rimessa in funzione.
- **WhatsApp**: se BCM ha un numero per ricevere le foto della targhetta, va messo accanto a "Manda le foto per email". Oggi non c'è perché non è nelle fonti.
- **Vendita diretta e rivenditori**: in pagina restano "Spediamo in tutto il mondo" e "Per maggiori informazioni contattaci direttamente" (chi-siamo e sito). I quattro rivenditori (Vivi in Campagna ed Enologys in Italia, Kidonakis ad Atene, KOL-Technik in Austria) e le righe per rivenditori e importatori in quattro lingue sono usciti dalla home: vanno in una pagina "Dove trovare le macchine BCM" solo dopo il permesso dei rivenditori. Va chiesto se BCM vende anche ai privati, quali rivenditori sono ufficiali e in quali lingue rispondono davvero.
- **Cataloghi in quattro lingue**: in pagina "Ogni catalogo è in italiano, tedesco, inglese e francese" (controllato sui 4 PDF) e una riga "Catalogues in English. Kataloge auf Deutsch. Catalogues en français.", che dice dei cataloghi e non promette risposte in quelle lingue.
- **Brevetto DAVID**: in pagina solo l'occhiello "Brevettato negli anni 80" e "Oggi è un marchio registrato, e lo costruiamo solo noi" (brochure: "manifattura esclusiva di BCM Enologia"). Non c'è scritto che il brevetto sia in vigore, né che il DAVID vada anche su torchi non BCM.
- **"Li produciamo nella nostra officina di Saonara"**: tolto dalla home finché non è confermato che forgiatura dei perni, gabbie e montaggio sono tutti in casa. Resta la frase delle schede torchi, "la scelta del miglior legno di faggio..., la forgiatura a caldo dei perni e la sagomatura dei cerchi", senza dire dove.
- **Foto dell'officina**: in pagina l'alt dice "corpi in ghisa in fila", senza didascalia. Va chiesto se sono corpi del DAVID o teste dei torchi a cricco: finché non si sa, sotto non c'è scritto "DAVID".
- **Didascalia dell'apertura**: "Basi dei torchi con la vite / giugno 2022": la data viene dal nome del file (IMG-20220625), il soggetto dalla galleria "In azienda". Va confermato che sono basi dei loro torchi idraulici.
- **2011 o 2012**: in home non c'è più nessuna delle due date.
- **Vite del modello 45**: la brochure dà 45 mm, il catalogo generale 50 mm. Riguarda la tabella del torchio idraulico, che è uscita dalla home e va nella pagina Misure; la tabella del DAVID in home (A-50 per le viti da 45, 50 e 55) è quella della brochure.
- **Lingue delle brochure ZIP**: le brochure sono uscite dalla home (pagina Download); torchi, martinetti e gabbie contengono italiano e inglese (controllato), per le altre sei non lo so.
- **SIMEI 2026** (Fiera Milano, 17-20 novembre 2026): se ci vanno, il link "In fiera" del piede va accompagnato da date e padiglione (in home non c'è più la riga dei SIMEI).
- **PEC e fax** (bcmenologia@pec.it, 049 5018355): non sono in pagina e vanno confermati prima di metterli.

## Che cosa manca per il livello pieno (da chiedere, non inventato)

- **Recensioni**: nessuna trovata (Google Maps, Facebook e Pagine Gialle non hanno restituito nulla). Chiedere 3 o 4 frasi vere di clienti (una cantina, un hobbista, un rivenditore) con nome e comune e il permesso di pubblicarle.
- **Lavori con il nome**: nessuno nelle fonti. Chiedere 3 cantine che usano un torchio o una pompa BCM, con il nome, il comune, l'anno e 2 dati (modello, quintali lavorati), e una foto larga per ognuna.
- **Certificazioni**: nessuna nelle fonti. Se le pompe hanno dichiarazioni CE o MOCA (girante per uso alimentare), vanno messe in PDF nella sezione dei cataloghi.
- **Persone**: nessuna foto della squadra; un ritratto in officina con i nomi e gli anni di mestiere renderebbe la pagina loro.

## Foto da rifare dal vero

La decisione del committente sulle foto è "niente": in pagina non c'è nessuna foto di repertorio e nessuna illustrazione. Ci sono solo foto di BCM dal loro sito: la fila di torchi in magazzino e la fila di meccanismi in officina (galleria "In azienda", giugno 2022, scatti da telefono) e gli scontornati del sito. Reggono per una proposta, non per il sito vero. Basta una giornata di scatti, tutti con la stessa luce:

1. **Apertura**: le basi rosse dei torchi in fila con le viti (oggi `wa0002`, scatto WhatsApp del 2022 a 1920x1440, scurito di 2 stop perché DAVID e il titolo si leggano), rifatte con un apparecchio vero, almeno 4.000 px di lato lungo, in 16:9 e in 3:4, senza scatoloni e teli sullo sfondo, con lo spazio libero in alto a sinistra per il nome. Meglio ancora una persona di BCM che monta un DAVID sulla vite.
2. **Le linee** (oggi 4 scontornati del catalogo in tessere 3:4 sulla carta): torchio a cricco, pompa Volumex, pompa automatizzata, pigiadiraspatrice, tutte con la stessa luce laterale e alla stessa altezza di ripresa, 3.000 px; oggi la Volumex ha un alone scuro di scontorno e le pompe hanno riflessi duri da catalogo.
3. **Ricambi**: il martinetto DAVID di fronte, con la targhetta nitida e leggibile (oggi la foto è 781 px), e un dettaglio della targhetta da sola: è la foto che spiega che cosa mandare.
4. **Officina**: la fila di meccanismi sul banco con luce naturale, pavimento pulito, niente neon né teli colorati, in 16:9 a 4.000 px; mani al lavoro sulla forgiatura dei perni e sulla gabbia in faggio.
5. **Una cantina vera** con un torchio BCM in vendemmia, con il nome della cantina se acconsente (serve anche per "lavori con il nome").

## Pagine del sito nuovo

I link della home portano alle sezioni della home o alle pagine e ai file del sito attuale bcmenologia.com: le linee (`/it/prodotti/linea-torchi`, `linea-martinetti`, `linea-gabbie`, `linea-pompe-standard`, `linea-pompe-automatizzate-con-inverter`, `linea-inverter-universale-pronto-all-uso`, `linea-pigiatrici-e-pigiadiraspatrici`, `linea-frutta`), i 4 cataloghi PDF in `/images/guida-alluso/` e le 10 brochure ZIP in `/images/prodotti/` (pesi letti il 3/11/2026), `/it/gallery/in-fiera`, `/it/privacy-policy`, `/it/cookies`. Nel sito nuovo vanno tenuti gli stessi percorsi o messi i redirect.
- **Inverter universale**: `linea-inverter-universale-pronto-all-uso` oggi rimanda (301) al suo unico prodotto, `.../41-filocontrollo-14`. In home è nella riga 05 dell'indice ("inverter universale fino a 45 kW"), nel piede non ha una voce propria ed è citato nella scheda delle pompe con inverter: nel sito nuovo gli serve una pagina di linea.
- **Ricambi e assistenza**: pagina nuova (oggi è solo una frase nelle schede), con il modulo e il caricamento delle foto.
- **Versione inglese**: i cataloghi sono già in quattro lingue, ma `/en/` oggi dà errore 404. In home c'è la voce "Cataloghi IT DE EN FR" in testata, che porta ai PDF.

## Licenze

- **Foto**: tutte dell'azienda (`assets/originali/`, scaricate dal sito bcmenologia.com). Va chiesto a BCM di confermarne i diritti. Le foto di repertorio di `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono usate.
- **Caratteri** (serviti dalla pagina da `sito/fonts/`, con la licenza accanto): Saira Extra Condensed 600 (The Saira Project Authors, SIL Open Font License 1.1, `OFL-Saira-Extra-Condensed.txt`) solo per la parola DAVID, e Source Sans 3 variabile 400-600 (Adobe, SIL Open Font License 1.1, `OFL-Source-Sans-3.txt`) per tutto il resto. Sofia Sans e Sofia Sans Condensed della versione professionale sono tolte (sono già in 4 home della zona).
- **Foto del culmine**: il torchio idraulico 60 con il DAVID è estratto dal loro catalogo PDF (`assets/originali/cataloghi/catalogo-generale-torchi.pdf`, immagine di 2362x3543 in `_prova/alto/pdf/catalogo-generale-torchi-003.png`): è lo stesso scatto del sito, a risoluzione piena. Va chiesto se si può usare.

## Logo

- Il logo in pagina è il PNG bianco del sito (170x96), ricolorato in inchiostro per la testata e in carta per il piede, a 96x54 (68x38 al telefono). Non l'ho ricostruito in SVG per non tradirlo.
- Va chiesto il file vettoriale, e quale versione usano oggi: quella bianca del sito o quella rossa dei cataloghi 2022 ("BCM Enologia s.r.l.").
- Manca anche una favicon decente: oggi è 16x16.
