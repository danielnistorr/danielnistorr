# B.C.M. Enologia: proposta di nuova home

È una proposta non richiesta: una nuova homepage per B.C.M. Enologia S.r.l. di Saonara (PD), torchi, martinetti DAVID, gabbie, pompe Volumex con inverter e pigiatrici. Riguarda solo la home.

- **Pagina**: `sito/index.html`. È statica, si apre con un doppio clic. Le immagini sono in `sito/img/` e i caratteri in `sito/fonts/`.
- **Screenshot e nota**: `screenshot/home/`. La nota (`NOTA.md`, sezione "Livello professionale") dice regola per regola che cosa passa e che cosa no.
- **Rifare tutto**: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shots.mjs` all'ora simulata lunedì 2 novembre 2026 alle 10, controlli con `pro_controlli.mjs`). La pagina prende anche `?ora=AAAA-MM-GGTHH:MM` (ora di Roma) per provare lo stato "Aperto ora".
- **Versione di prima** (il torchio sulla carta con il selettore): `_prova/versione-1-originale/` (sito, screenshot, LEGGIMI).
- **Analisi con le fonti**: `01-analisi.md`; chi apre il sito e perché: `_prova/uso/SCHEDA.md`.

Nessun contatto con l'azienda, nessun modulo inviato, niente pubblicato.

## Il modulo di contatto va collegato a un servizio

Il modulo "Scrivici" (tipo di richiesta, macchina e modello, quantità, nome, azienda, email, telefono, messaggio, allegato con le foto della targhetta e del pezzo) oggi **non invia nulla**: compone un'email a info@bcmenologia.com con l'oggetto ("Ricambio o assistenza: Torchio idraulico 60, Mario Rossi", oppure "Rivenditori: listino e condizioni, <azienda>") e i campi già scritti, e la apre nel programma di posta di chi scrive. Il campo dell'allegato serve solo a scrivere nel corpo i nomi dei file scelti: un mailto non può allegare nulla, quindi le foto vanno allegate a mano nell'email (la pagina lo dice due volte).
- Nel sito vero va collegato a un servizio di invio (per esempio il modulo del CMS con SMTP, Formspree o Netlify Forms), con il caricamento delle foto (targhetta e pezzo, JPEG fino a 10 MB), l'informativa privacy e una risposta automatica.
- Va deciso con BCM chi legge le richieste e in quanto tempo risponde: in pagina non c'è nessuna promessa di tempi perché non è nelle fonti.

## Da chiedere o confermare con BCM prima di inviare

- **Stato della società**: un estratto la diceva cessata, mentre aziende.it la dà "Attiva" e reportaziende pubblica ricavi 2025. Va verificato per primo.
- **Ragione sociale e civico**: in pagina "B.C.M. Enologia S.r.l." (registro) e viale Veneto 10-12 (cataloghi e registro; il sito dice 10).
- **Orari e chiusure**: lo stato "Aperto ora" usa lunedì-venerdì 8-18 e chiude nei festivi nazionali e a Pasquetta. Vanno chiesti la pausa pranzo, le ferie d'agosto e di Natale e l'orario in vendemmia. Le ferie si scrivono nell'elenco `chiusure` dello script in fondo alla pagina (coppie di date, per esempio `[['2027-08-09','2027-08-20']]`): in quei giorni lo stato dice "Chiusi per ferie, riapriamo il ...". Oggi l'elenco è vuoto.
- **Fuori orario**: quando è chiuso, la pagina propone di mandare le foto per email. Va chiesto se vogliono aggiungere una promessa ("ti richiamiamo il giorno dopo"): oggi non c'è, perché non è nelle fonti.
- **Ricambi**: in pagina "da oltre 30 anni teniamo i ricambi e facciamo la manutenzione di ogni singolo componente" e "compatibilità con il passato", parole loro, più una riga di esempi presa dai componenti delle loro macchine ("il manometro del DAVID, i listelli e i cerchi della gabbia, i tappi e le mezzelune, la girante della pompa"): va confermata. Vanno chiesti anche dove sta la targhetta su torchi e pompe, l'elenco dei ricambi più richiesti (martinetti, manometri, listelli, cerchi, tappi e mezzelune, giranti e tenute delle pompe), se tengono anche i pezzi delle macchine della vecchia B.C.M. snc e un esempio vero di macchina vecchia rimessa in funzione.
- **WhatsApp**: se BCM ha un numero per ricevere le foto della targhetta, va messo accanto a "Manda le foto per email". Oggi non c'è perché non è nelle fonti.
- **Vendita diretta e rivenditori**: in pagina "Per prezzi e disponibilità chiamaci", "Spediamo in tutto il mondo" (chi-siamo, ora nei contatti) e la fascia "Dove trovi le macchine BCM" con quattro rivenditori con il nome (Vivi in Campagna ed Enologys in Italia, Kidonakis ad Atene, KOL-Technik in Austria: vendono BCM, vedi SCHEDA). Va chiesto se BCM vende anche ai privati, se vuole i rivenditori nominati in home (e il loro permesso), quali sono quelli ufficiali, con il paese e il sito da linkare.
- **Rivenditori e importatori**: quattro righe, in italiano, inglese, tedesco e francese: "cataloghi, schede e condizioni" a info@bcmenologia.com o al +39 049 640372, con gli orari. Va chiesto in quali lingue rispondono davvero: se non rispondono in tedesco o in francese, quelle due righe vanno tolte o devono dire "we answer in Italian and English". Va chiesto anche se c'è un listino per i rivenditori (l'oggetto del modulo dice "listino e condizioni").
- **Brevetto DAVID**: in pagina solo "progettato e brevettato negli anni 80, oggi marchio registrato". Non c'è scritto che il brevetto sia in vigore.
- **"Li produciamo nella nostra officina di Saonara"**: confermare che forgiatura dei perni, gabbie e montaggio sono tutti in casa.
- **Didascalia dell'officina**: "Meccanismi in ghisa sul banco dell'officina, viale Veneto, 2022". Va chiesto se sono corpi del DAVID o teste dei torchi a cricco.
- **2011 o 2012**: la srl è iscritta nel 2011 (registro), il sito dice "nel 2012" per le pompe; in pagina c'è 2012 solo per le pompe.
- **Vite del modello 45**: la brochure dà 45 mm, il catalogo generale 50 mm.
- **Lingue delle brochure ZIP**: torchi, martinetti e gabbie contengono italiano e inglese (controllato); per le altre sei non lo so e in pagina c'è solo il peso.
- **SIMEI 2026** (Fiera Milano, 17-20 novembre 2026): se ci vanno, la riga "In fiera" va aggiornata con date e padiglione.
- **PEC e fax** (bcmenologia@pec.it, 049 5018355): non sono in pagina e vanno confermati prima di metterli.

## Che cosa manca per il livello pieno (da chiedere, non inventato)

- **Recensioni**: nessuna trovata (Google Maps, Facebook e Pagine Gialle non hanno restituito nulla). Chiedere 3 o 4 frasi vere di clienti (una cantina, un hobbista, un rivenditore) con nome e comune e il permesso di pubblicarle.
- **Lavori con il nome**: nessuno nelle fonti. Chiedere 3 cantine che usano un torchio o una pompa BCM, con il nome, il comune, l'anno e 2 dati (modello, quintali lavorati), e una foto larga per ognuna.
- **Certificazioni**: nessuna nelle fonti. Se le pompe hanno dichiarazioni CE o MOCA (girante per uso alimentare), vanno messe in PDF nella fascia dei cataloghi.
- **Persone**: nessuna foto della squadra; un ritratto in officina con i nomi e gli anni di mestiere renderebbe la pagina loro.

## Foto da rifare dal vero

La decisione del committente sulle foto è "niente": in pagina non c'è nessuna foto di repertorio e nessuna illustrazione. Ci sono solo foto di BCM dal loro sito: la fila di torchi in magazzino e la fila di meccanismi in officina (galleria "In azienda", giugno 2022, scatti da telefono) e gli scontornati del sito. Reggono per una proposta, non per il sito vero. Basta una giornata di scatti, tutti con la stessa luce:

1. **Apertura**: i torchi pronti in magazzino come oggi (wa0000), con la luce del pomeriggio ma senza imballi e scatole sullo sfondo, in verticale 4:5 (almeno 2.400x3.000 px, oggi in pagina c'è un taglio di 980x1225 da uno scatto WhatsApp) e in 16:9 per il telefono; meglio ancora una persona di BCM che monta un martinetto su un torchio.
2. **Le otto linee** (oggi gli scontornati del catalogo, senza ombra, sul piano grigio #E6E5E2): torchio idraulico, torchio a cricco, DAVID, gabbia, pompa Volumex, pompa con inverter, pigiatrice, pressafrutta, sullo stesso fondo grigio chiaro, con la stessa luce laterale da finestra e alla stessa altezza di ripresa, in quadrato, 3.000 px; oggi pompe e pigiatrici hanno riflessi duri da catalogo.
3. **Ricambi**: il martinetto DAVID di fronte, con la targhetta nitida e leggibile (oggi la foto è 781 px), e un dettaglio della targhetta da sola: è la foto che spiega che cosa mandare.
4. **Officina**: la fila di meccanismi sul banco con luce naturale, pavimento pulito, niente neon né teli colorati, in 16:9 a 4.000 px; mani al lavoro sulla forgiatura dei perni e sulla gabbia in faggio.
5. **Una cantina vera** con un torchio BCM in vendemmia, con il nome della cantina se acconsente (serve anche per "lavori con il nome").

## Pagine del sito nuovo

I link della home portano alle sezioni della home o alle pagine e ai file del sito attuale bcmenologia.com: le linee (`/it/prodotti/linea-torchi`, `linea-martinetti`, `linea-gabbie`, `linea-pompe-standard`, `linea-pompe-automatizzate-con-inverter`, `linea-inverter-universale-pronto-all-uso`, `linea-pigiatrici-e-pigiadiraspatrici`, `linea-frutta`), i 4 cataloghi PDF in `/images/guida-alluso/` e le 10 brochure ZIP in `/images/prodotti/` (pesi letti il 3/11/2026), `/it/gallery/in-fiera`, `/it/privacy-policy`, `/it/cookies`. Nel sito nuovo vanno tenuti gli stessi percorsi o messi i redirect.
- **Inverter universale**: `linea-inverter-universale-pronto-all-uso` oggi rimanda (301) al suo unico prodotto, `.../41-filocontrollo-14`. In home non ha una scheda propria (la griglia è di otto) ed è citato nella scheda delle pompe con inverter: nel sito nuovo gli serve una pagina di linea.
- **Ricambi e assistenza**: pagina nuova (oggi è solo una frase nelle schede), con il modulo e il caricamento delle foto.
- **Versione inglese**: i cataloghi sono già in quattro lingue, ma `/en/` oggi dà errore 404. In home c'è "Catalogues EN · DE · FR" in testata, che porta ai PDF.

## Licenze

- **Foto**: tutte dell'azienda (`assets/originali/`, scaricate dal sito bcmenologia.com). Va chiesto a BCM di confermarne i diritti. Le foto di repertorio di `assets/esterne/` (licenze in `assets/CREDITI.md`) non sono usate.
- **Caratteri** (serviti dalla pagina da `sito/fonts/`): Sofia Sans e Sofia Sans Condensed (Lettersoup, Google Fonts, SIL Open Font License 1.1). Zodiak, della versione di prima, è tolto.

## Logo

- Il logo in pagina è il PNG bianco del sito (170x96): in inchiostro in testata e bianco nel piede scuro, a 85x48 (2x). Non l'ho ricostruito in SVG per non tradirlo.
- Va chiesto il file vettoriale, e quale versione usano oggi: quella bianca del sito o quella rossa dei cataloghi 2022 ("BCM Enologia s.r.l.").
- Manca anche una favicon decente: oggi è 16x16.
