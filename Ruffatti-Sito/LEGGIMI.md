# Fratelli Ruffatti: proposta di nuova homepage

Proposta non richiesta di una nuova home per ruffatti.com (solo la home). Non è stata inviata, pubblicata o mostrata all'azienda.

Versione attuale: **livello professionale, con il ritocco finale** (3/11/2026: menu riparato, testata e apertura su mogano con il logo e il logotipo in ottone, foto trattate in serie, dati corretti; dettagli in `screenshot/home/NOTA.md`), costruita sulla scheda d'uso `_prova/uso/SCHEDA.md` e sulle regole di `_metodo/professionale/REGOLE.md` (famiglia M, manifattura e fornitori del lusso). La versione precedente ("Una canna", con la canna ad ancia smontata in apertura) è conservata com'era in `_prova/versione-1-originale/` (pagina, immagini e screenshot).

## Dove sono le cose

- **Home**: `sito/index.html`, con `sito/img/` (solo le immagini usate, JPEG in una o due larghezze) e `sito/fonts/` (Gambetta 400, Switzer 400 e 600 in woff2). Si apre con file:///, senza server.
- **Screenshot**: `screenshot/home/` (pagine intere home-1440, home-1024, home-768, home-390, home-320; prime schermate a 1440, 390 e 320; chiusura-1440). Scelte, controlli e l'esito delle 15 regole sono in `screenshot/home/NOTA.md`, sezione "Livello professionale".
- **Rifare tutto**: `sh _prova/script/build_finale.sh`. Rifà le immagini (`pro_img.py`), controlla U+2014 e le immagini mancanti o inutili, misura le 15 regole (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`) e rifà gli screenshot (`pro_shot.mjs`). Le prove del menu a pannello e dei salti alle ancore sono in `_prova/script/ritocco_prova.mjs`.
- **Materiali di lavoro**: analisi con le fonti in `01-analisi.md`, scheda d'uso in `_prova/uso/SCHEDA.md`, inventario e voti delle foto in `_prova/inventario-immagini.json`, crediti in `assets/CREDITI.md`, pagine del concorso e delle testimonianze e l'elenco dei video YouTube scaricati il 3/11/2026 in `_prova/crawl/pro/`.

## Il modulo di contatto va collegato

Il modulo "Scriveteci" nella sezione Contatti **non invia nulla**: controlla i campi obbligatori e poi apre il programma di posta di chi scrive con un'email già composta per organs@ruffatti.com (oggetto "Richiesta: tipo, istituzione, città"; nel testo nome, istituzione, ruolo, luogo, email, telefono, organo di oggi, idea di dimensione, richiesta, messaggio e la riga "Allego: ..." con le caselle spuntate). Pianta e foto si allegano a mano, perché un link mailto non porta allegati.
Nel sito vero va collegato a un servizio di invio (il Contact Form 7 che usano oggi, oppure Formspree, Brevo o simili) con caricamento dei file: le tre caselle "Che cosa potete mandarci" (pianta della chiesa, foto della cantoria, foto della consolle e della targhetta) diventano un campo `input type=file` (PDF, JPG, DWG, più file). Poi informativa privacy e un messaggio di conferma. Il modulo di oggi in inglese chiede anche "Institution" e "Position": i campi della home sono gli stessi.

## Da chiedere all'azienda

In pagina c'è solo ciò che ha una fonte (`01-analisi.md`, `_prova/uso/SCHEDA.md`, pagine del loro sito). Restano da chiedere:

1. **Ragione sociale completa** con forma giuridica, REA, capitale sociale e PEC: non trovati. Nel piede ci sono solo "Fratelli Ruffatti" e la P.IVA 00207160284.
2. **Orari e visite.** Gli orari non sono pubblici, quindi non ci sono (la regola 15 del piede per questo non passa). Nel piede ora c'è "Visite su appuntamento", dalla scheda Homo Faber ("By appointment only"): va confermato, insieme a via Facciolati 166 e al link "Vai alla mappa" (Homo Faber scrive "Address upon request").
3. **Numeri di oggi.** "Oltre 500 organi in Italia" e "oltre 50 negli Stati Uniti" vengono da testi del 2016; "circa 120 restauri" dall'elenco aggiornato al 2020. In pagina sono datati con una nota sotto la fascia dei numeri. Quanti sono oggi, e quanti organi in tutto? Quante persone lavorano in laboratorio?
4. **Ultimi strumenti** (dati dalla scheda d'uso, fonti The Diapason, Pershore Abbey, Main Line Tonight): confermare per ciascuno nome esatto del committente, anno di inaugurazione, manuali e registri.
   - Sacred Heart, Grand Rapids: 3 manuali, 39 file, 2780 canne, intonazione da gennaio 2026 (in pagina con l'anno 2026: va confermato se è già inaugurato).
   - Pershore Abbey: 3 manuali, 33 registri, 2023.
   - Coral Ridge Presbyterian Church, Fort Lauderdale: restauro, 5 manuali, 117 file, 2023.
   - Notre Dame Seminary, New Orleans, 2022: la loro notizia del 13/10/2022 dice "organo a due manuali" (la versione di prima della home scriveva tre: corretto). Quanti registri?
   - Santa Caterina da Siena, Wayne, Pennsylvania: 3 manuali, 37 registri, due consolle, 2022 (nome della chiesa dalla stessa notizia).
   - Per Grand Rapids, Pershore e Coral Ridge servono le pagine o gli articoli a cui collegare le righe (oggi sono cliccabili solo New Orleans e Wayne, verso le loro notizie) e, per un comitato, la disposizione fonica di ciascuno.
   - La ricostruzione per la cattedrale di Tucson non è in pagina: la fonte dice solo "canne in Italia da inizio 2026". Va chiesto a che punto è.
5. **Manutenzione e accordatura.** Seguono gli organi Ruffatti già installati (in Italia e negli USA, anche i Rodgers/Ruffatti)? Fanno sopralluoghi? Se sì, va scritto nel riquadro "Avete un organo Ruffatti?"; finché non lo confermano, il riquadro dice solo cosa preparare per la prima telefonata.
6. **Chi risponde** a organs@ruffatti.com e al telefono (Michela?), e in quali lingue: in pagina non c'è.
7. **Testimonianze e citazioni.** I ruoli degli organisti sono quelli della pagina "Dicono di noi" ("Ex Direttore della Musica e Organista", reso con "già"); manca per ciascuna l'anno e lo strumento: se ci sono citazioni sugli strumenti 2022-2026, sono le più utili. **Citazioni di Michela Ruffatti** (Rockit, 13/05/2026: "Ogni organo è diverso..." nella fascia dei numeri e "Prestiamo grande attenzione all'utilizzo degli stessi materiali usati in origine" nella sezione Restauro): conferma che si possono usare. Vale lo stesso per le tre testimonianze di "Dicono di noi" (Joyce Jones, Diane Bish, Frederick Swann), riportate dalla loro pagina in italiano.
8. **Maestro d'Arte e Mestiere 2020** e **Homo Faber**: permesso di citarli; il marchio della Fondazione Cologni non è usato.
9. **Recensioni.** Non hanno recensioni Google o simili (la sede non riceve pubblico): le prove sono le testimonianze degli organisti, i committenti con il nome e la stampa. Se hanno lettere più recenti di committenti (Pershore, Grand Rapids, Coral Ridge), sono la cosa più utile da aggiungere.
10. **Video per "Ascolta".** Il canale YouTube ha sette video (2016-2020: laboratorio, canne ad ancia da 32', restauro di La Valletta, visita della fabbrica): nessuno fa sentire un organo recente. Servono uno o due video o registrazioni degli strumenti 2022-2026 (anche di terzi, con il permesso), e il link a una piattaforma con le incisioni dei CD.
11. **Le pagine del sito nuovo.** I link della home portano alle pagine di oggi (Come costruiamo, Canne ad ancia, Il legname, Realizzazioni, Opere eseguite, Procedure di restauro, Dicono di noi, CD, Concorso di Miami, Ultime notizie, Cookie, versioni EN e RU). Mancano una pagina Privacy e un elenco delle realizzazioni filtrabile per manuali e Paese (il filtro del prototipo B in `_prova/home/b` è pronto: "86 strumenti in 14 Paesi" va dichiarato come conteggio dell'elenco "Alcune opere significative").
12. **Newsletter**: è ancora attiva? L'ultimo numero è del 2020. Nella home non c'è più il modulo finto; se la riprendono, si aggiunge nel piede collegata a un servizio vero.
13. **Logo vettoriale**: in pagina c'è il PNG a 2x ricavato dalla maschera della newsletter 2020 (`assets/originali/logo-newsletter2020-1bit-5024.png`). Va chiesto il file originale.

## Foto: che cosa c'è e che cosa va fatto

In pagina ci sono solo foto loro, dalla libreria media di ruffatti.com, mai ingrandite, tutte con lo stesso trattamento (`pro_img.py`: bilanciamento del bianco, colore 0,8, stessa curva calda, stessa luminosità media), che le avvicina ma non le rende una serie vera; nessuna foto di repertorio, nessuna illustrazione, nessuna immagine generata. Vanno confermati i diritti delle foto delle installazioni (forse di fotografi dei committenti).

| Foto in pagina | File originale | Problema | Che cosa chiedere o rifare |
|---|---|---|---|
| Apertura, Notre Dame Seminary, New Orleans | `2022_10_notre-dame.jpg`, 574x744 | in pagina a 519 px: nitida a 1x, morbida sugli schermi retina | l'originale ad alta risoluzione (è la foto della copertina di The Diapason) o il file del fotografo |
| Consolle di Santa Caterina da Siena, Wayne | `2022_10_consolle.jpg`, 843x605 | ritagliata a 727x545 per togliere vetrate e soffitto; morbida su retina | l'originale; e una foto dell'organo intero nella chiesa (quella del sito, `cantoriajpg`, è di 843 px con luce mista) |
| Le quattro schede (Uppsala, canne ad ancia, falegnameria, organo antico restaurato) | `2016_02_home-ruffatti4`, `2016_04_xSfondo-trombe-2`, `2016_04_falegnami-21`, `2016_03_xFile0149` | buone a 302 px, ma di epoche e luci diverse; l'organo restaurato non ha luogo né anno | una serie unica dal vero: stesso fotografo, luce naturale di giorno, formato 4:5, almeno 3000 px; per il restauro un organo restaurato di recente con luogo e anno |
| Targhetta "Fratelli Ruffatti" tra i pomelli | `2016_04_xP1050195.jpg`, 800x633 | 800 px, a 519 in pagina | rifarla dal vero su una consolle, luce radente da una finestra, senza flash, 4:3 |
| Maestranze davanti alla fabbrica | `2016_03_storia1-575.jpg`, 900x575 | piccola; anno ignoto (un nome di file dice 1960) | scansione dell'originale a 1200 dpi e l'anno |

Foto che mancano e servono di più: **Pershore Abbey, Grand Rapids e Coral Ridge** (una per strumento, l'organo intero nella sua chiesa, di giorno, 4:3, almeno 3000 px): con queste la sezione "Ultimi strumenti" diventa una galleria di lavori con foto per ognuno. Poi **mani al lavoro in laboratorio** (fusione delle lastre, tornitura delle noci, intonazione), con una sola luce e lo stesso fotografo.

## Licenze

- **Caratteri**: Gambetta e Switzer di Indian Type Foundry, da Fontshare, con licenza ITF Free Font License (uso commerciale gratuito, anche sul web), serviti dalla pagina in `sito/fonts/`.
- **Foto**: tutte della Fratelli Ruffatti o dei committenti dei loro strumenti. Le foto Unsplash e Pexels di `assets/esterne/` non sono in pagina e non vanno usate (restano solo come materiale dei prototipi, licenze in `assets/CREDITI.md`).

## Ritocco finale: che cosa resta fuori e perché

- **Versione inglese della home.** Per una commissione americana o inglese è il difetto più grave rimasto: EN porta al sito inglese di oggi (ora con il titolo "Il sito inglese di oggi (current English site)"). La home inglese (en/index.html, stessi blocchi: Recent instruments, Listen, Testimonials, What to send us, modulo con Institution e Position) va fatta quando la proposta italiana è approvata; molti testi esistono già in inglese sul loro sito (testimonianze, notizie, pagina contatti).
- **Un organo che suona.** I sette video del canale sono laboratorio, canne da 32' e il restauro di La Valletta: nessuno fa sentire uno strumento recente. Vanno chiesti un video di un concerto o di un'inaugurazione (Wayne, New Orleans, Pershore, Grand Rapids) con luogo, anno, organista e brano, il link alla puntata precisa di Pipedreams e un CD con estratto ascoltabile (punto 10).
- **Elenco filtrabile delle realizzazioni**: resta da fare nella pagina Realizzazioni del sito nuovo (punto 11); in home il link si chiama ora "86 opere significative, da una a sei tastiere", per non contraddire "oltre 500 organi in Italia".
- **Manutenzione e accordatura**: il riquadro del restauro chiede "Organo muto, sporco o da revisionare?" senza promettere il servizio; "Dicono di noi" cita "l'assistenza dopo l'installazione" (Mons. O'Doherty, Miami), ma va confermato con loro prima di scriverlo (punto 5).
- **Un restauro italiano documentato** in home (per esempio Villa Cortese 2021 o Modena 2019, dagli articoli diocesani citati nella scheda d'uso): servono il permesso e il link alla fonte.
