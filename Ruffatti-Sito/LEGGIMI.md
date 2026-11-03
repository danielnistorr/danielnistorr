# Fratelli Ruffatti: proposta di nuova homepage

Proposta non richiesta di una nuova home per ruffatti.com (solo la home). Non è stata inviata, pubblicata o mostrata all'azienda.

Versione attuale: **alto livello, prova della sezione D** (3/11/2026): il logotipo d'ottone sul mogano come apertura, l'organo della Uppsala Cathedral come culmine, 568 parole e 5 sezioni, costruita sulla direzione `_prova/alto/DIREZIONE.md` e sulla sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; scelte ed esito di ogni regola D in `screenshot/home/NOTA.md`. La versione di prima ("livello professionale, con il ritocco finale") è conservata com'era, con pagina, immagini, caratteri e screenshot, in `_prova/versione-pro/`. Quella ancora precedente ("Una canna") è in `_prova/versione-1-originale/`.

## Dove sono le cose

- **Home**: `sito/index.html`, con `sito/img/` (solo le immagini usate, WebP in due larghezze) e `sito/fonts/` (EB Garamond 400-500 in woff2, con la licenza `OFL-EBGaramond.txt`). Si apre con file:///, senza server.
- **Screenshot**: `screenshot/home/` (pagine intere home-1440, home-1024, home-768, home-390, home-320; prime schermate a 1440, 1024, 768, 390 e 320; chiusura-1440).
- **Rifare tutto**: `sh _prova/alto/build.sh`. Rifà le immagini (`_prova/alto/script/alto_img.py`), controlla U+2014 e le immagini mancanti o inutili, misura la sezione D (`_prova/alto/misura-d.mjs`, esito in `_prova/alto/misura-d.txt`), fa i controlli a sei larghezze (`_prova/alto/controllo.mjs`) e rifà gli screenshot (`_prova/alto/shot.mjs`). **Non usare più `_prova/script/build_finale.sh`**: è della versione di prima e riscriverebbe `sito/img` e gli screenshot.
- **Materiali di lavoro**: analisi con le fonti in `01-analisi.md`, scheda d'uso in `_prova/uso/SCHEDA.md`, inventario e voti delle foto in `_prova/inventario-immagini.json`, crediti in `assets/CREDITI.md`, pagine del concorso e delle testimonianze e l'elenco dei video YouTube scaricati il 3/11/2026 in `_prova/crawl/pro/`.

## Il modulo di contatto va nella pagina Contatti

Nella home nuova il modulo non c'è più (regola D12): restano tre strade con il loro contatto, cioè l'email per un organo nuovo con oggetto e traccia, il telefono e l'email con le foto per un restauro, il Concorso di Miami per gli organisti. Il modulo della versione di prima (in `_prova/versione-pro/sito/index.html`) va nella pagina Contatti del sito nuovo. Com'era fatto: **non invia nulla**: controlla i campi obbligatori e poi apre il programma di posta di chi scrive con un'email già composta per organs@ruffatti.com (oggetto "Richiesta: tipo, istituzione, città"; nel testo nome, istituzione, ruolo, luogo, email, telefono, organo di oggi, idea di dimensione, richiesta, messaggio e la riga "Allego: ..." con le caselle spuntate). Pianta e foto si allegano a mano, perché un link mailto non porta allegati.
Nel sito vero va collegato a un servizio di invio (il Contact Form 7 che usano oggi, oppure Formspree, Brevo o simili) con caricamento dei file: le tre caselle "Che cosa potete mandarci" (pianta della chiesa, foto della cantoria, foto della consolle e della targhetta) diventano un campo `input type=file` (PDF, JPG, DWG, più file). Poi informativa privacy e un messaggio di conferma. Il modulo di oggi in inglese chiede anche "Institution" e "Position": i campi della home sono gli stessi.

## Da chiedere all'azienda

In pagina c'è solo ciò che ha una fonte (`01-analisi.md`, `_prova/uso/SCHEDA.md`, pagine del loro sito). Restano da chiedere:

1. **Ragione sociale completa** con forma giuridica, REA, capitale sociale e PEC: non trovati. Nel piede ci sono solo "Fratelli Ruffatti" e la P.IVA 00207160284.
2. **Orari e visite.** Gli orari non sono pubblici, quindi non ci sono. "Visite su appuntamento" (dalla scheda Homo Faber, "By appointment only") è uscito dalla home finché non lo confermano. Nel piede restano via Facciolati 166 (dal piede del loro sito) e un solo link "Indicazioni" a Google Maps: va confermato, perché Homo Faber scrive "Address upon request".
3. **Numeri di oggi.** "Oltre 500 organi in Italia" e "oltre 50 negli Stati Uniti" vengono da testi del 2016: nella home nuova non ci sono più. Resta "circa 120 restauri", scritto "aggiornato al 2020". Quanti sono oggi, e quanti organi in tutto? Quante persone lavorano in laboratorio?
4. **Ultimi strumenti** (dati dalla scheda d'uso, fonti The Diapason, Pershore Abbey, Main Line Tonight): confermare per ciascuno nome esatto del committente, anno di inaugurazione, manuali e registri. Nella home nuova ci sono solo Pershore Abbey (2023, tre manuali e 33 registri, scritto "secondo Pershore Abbey" con il link a pershoreabbey.org.uk/?p=7451), New Orleans e Wayne (dalle loro notizie). Grand Rapids e Coral Ridge sono usciti: per Grand Rapids la parrocchia annuncia la dedicazione il 25 marzo senza che si capisca l'anno, e il Pipe Organ Database scrive 2025; per Coral Ridge l'anno non ha una fonte certa.
   - Sacred Heart, Grand Rapids: 3 manuali, 39 file, 2780 canne, intonazione da gennaio 2026 (in pagina con l'anno 2026: va confermato se è già inaugurato).
   - Pershore Abbey: 3 manuali, 33 registri, 2023.
   - Coral Ridge Presbyterian Church, Fort Lauderdale: restauro, 5 manuali, 117 file, 2023.
   - Notre Dame Seminary, New Orleans, 2022: la loro notizia del 13/10/2022 dice "organo a due manuali" (la versione di prima della home scriveva tre: corretto). Quanti registri?
   - Santa Caterina da Siena, Wayne, Pennsylvania: 3 manuali, 37 registri, due consolle, 2022 (nome della chiesa dalla stessa notizia).
   - Per Grand Rapids, Pershore e Coral Ridge servono le pagine o gli articoli a cui collegare le righe (oggi sono cliccabili solo New Orleans e Wayne, verso le loro notizie) e, per un comitato, la disposizione fonica di ciascuno.
   - La ricostruzione per la cattedrale di Tucson non è in pagina: la fonte dice solo "canne in Italia da inizio 2026". Va chiesto a che punto è.
5. **Manutenzione e accordatura.** Seguono gli organi Ruffatti già installati (in Italia e negli USA, anche i Rodgers/Ruffatti)? Fanno sopralluoghi? Se sì, va scritto nel riquadro "Avete un organo Ruffatti?"; finché non lo confermano, il riquadro dice solo cosa preparare per la prima telefonata.
6. **Chi risponde** a organs@ruffatti.com e al telefono (Michela?), e in quali lingue: in pagina non c'è.
7. **Testimonianze e citazioni.** Nella home nuova restano solo «I Principali cantano.» di Joyce Jones (Baylor University) e nessuna citazione di Michela Ruffatti. I ruoli degli organisti sono quelli della pagina "Dicono di noi" ("Ex Direttore della Musica e Organista", reso con "già"); manca per ciascuna l'anno e lo strumento: se ci sono citazioni sugli strumenti 2022-2026, sono le più utili. **Citazioni di Michela Ruffatti** (Rockit, 13/05/2026: "Ogni organo è diverso..." nella fascia dei numeri e "Prestiamo grande attenzione all'utilizzo degli stessi materiali usati in origine" nella sezione Restauro): conferma che si possono usare. Vale lo stesso per le tre testimonianze di "Dicono di noi" (Joyce Jones, Diane Bish, Frederick Swann), riportate dalla loro pagina in italiano.
8. **Maestro d'Arte e Mestiere 2020** e **Homo Faber**: permesso di citarli; il marchio della Fondazione Cologni non è usato.
9. **Recensioni.** Non hanno recensioni Google o simili (la sede non riceve pubblico): le prove sono le testimonianze degli organisti, i committenti con il nome e la stampa. Se hanno lettere più recenti di committenti (Pershore, Grand Rapids, Coral Ridge), sono la cosa più utile da aggiungere.
10. **Video per "Ascolta".** Il canale YouTube ha sette video (2016-2020: laboratorio, canne ad ancia da 32', restauro di La Valletta, visita della fabbrica): nessuno fa sentire un organo recente. Servono uno o due video o registrazioni degli strumenti 2022-2026 (anche di terzi, con il permesso), e il link a una piattaforma con le incisioni dei CD.
11. **Le pagine del sito nuovo.** I link della home portano alle pagine di oggi (Come costruiamo, Canne ad ancia, Il legname, Realizzazioni, Opere eseguite, Procedure di restauro, Dicono di noi, CD, Concorso di Miami, Ultime notizie, Cookie, versioni EN e RU). Mancano una pagina Privacy e un elenco delle realizzazioni filtrabile per manuali e Paese (il filtro del prototipo B in `_prova/home/b` è pronto: "86 strumenti in 14 Paesi" va dichiarato come conteggio dell'elenco "Alcune opere significative").
12. **Newsletter**: è ancora attiva? L'ultimo numero è del 2020. Nella home non c'è più il modulo finto; se la riprendono, si aggiunge nel piede collegata a un servizio vero.
13. **Logo vettoriale**: in pagina c'è il PNG a 2x ricavato dalla maschera della newsletter 2020 (`assets/originali/logo-newsletter2020-1bit-5024.png`). Va chiesto il file originale.

## Foto: che cosa c'è e che cosa va fatto

In pagina ci sono solo foto loro, dalla libreria media di ruffatti.com, mai ingrandite, tutte con lo stesso trattamento (`_prova/alto/script/alto_img.py`: bilanciamento del bianco, colore 0,88, stessa curva calda, stessa luminosità media; 11 foto in tre formati), che le avvicina ma non le rende una serie vera; nessuna foto di repertorio, nessuna illustrazione, nessuna immagine generata. Vanno confermati i diritti delle foto delle installazioni (forse di fotografi dei committenti).

| Foto in pagina | File originale | Problema | Che cosa chiedere o rifare |
|---|---|---|---|
| Culmine, Uppsala Cathedral (2009, quattro manuali, trasmissione elettrica: dalla scheda PDF del loro sito) | `2016_02_home-ruffatti2.jpg`, 900x1600 | a 540x960 a 1440: nitida a 1x, morbida su retina; a 390 ritaglio basso 900x1100 | l'originale ad alta risoluzione, e chi l'ha scattata |
| Notre Dame Seminary, New Orleans | `2022_10_notre-dame.jpg`, 574x744 | 296x370 in pagina: regge a 1x, non a 2x | l'originale (è la foto della copertina di The Diapason) o il file del fotografo |
| Consolle di Santa Caterina da Siena, Wayne | `2022_10_consolle.jpg`, 843x605 | ritagliata a 484x605 sulla consolle | l'originale; e una foto dell'organo intero nella chiesa |
| Buckfast Abbey, organo Quire | `2018_11_756A0922-3.jpg`, 1028x758 | ritaglio 606x758 sulle casse a nord; forse del fotografo dell'abbazia | i diritti |
| Chiesa parrocchiale di Boteå | `2018_11_P1270600-1.jpg`, 3264x2448 | morbida al 100%, pulita a 592 px | l'anno di inaugurazione (in pagina c'è il contratto del 2015) |
| Il legname, Lastre per canne, Canne ad anima, Canne ad ancia | `2016_03_xfoto-fabbrica-catasta-legname-1`, `2016_04_xFusione-2`, `2016_04_xOFFSETS-95MODIF`, `2016_04_xP1190212` | 800 px, compatta e flash, ritagliate a 3:2 | una giornata in laboratorio con luce naturale e lo stesso fotografo |
| Targhetta "Fratelli Ruffatti" tra i pomelli | `2016_04_xP1050195.jpg`, 800x633 | ritaglio 800x533, a 520 in pagina | rifarla dal vero su una consolle, luce radente, senza flash |
| Maestranze davanti alla fabbrica | `2016_03_storia1-575.jpg`, 900x575 | piccola; anno ignoto | scansione dell'originale a 1200 dpi e l'anno |

Il trattamento comune ora è `_prova/alto/script/alto_img.py` (colore 0,88). Il logotipo in ottone #D4B06A viene dalla maschera della newsletter 2020, come prima.

Foto che mancano e servono di più: **Pershore Abbey, Grand Rapids e Coral Ridge** (una per strumento, l'organo intero nella sua chiesa, di giorno, 4:3, almeno 3000 px): con queste la sezione "Ultimi strumenti" diventa una galleria di lavori con foto per ognuno. Poi **mani al lavoro in laboratorio** (fusione delle lastre, tornitura delle noci, intonazione), con una sola luce e lo stesso fotografo.

## Licenze

- **Caratteri**: EB Garamond (The EB Garamond Project Authors), SIL Open Font License 1.1, da google/fonts (`ofl/ebgaramond`), ridotto ai pesi 400-500 e ai caratteri latini e cirillici, in `sito/fonts/` con la licenza accanto (`OFL-EBGaramond.txt`). Gambetta e Switzer, della versione di prima, sono rimasti in `_prova/versione-pro/sito/fonts/`.
- **Foto**: tutte della Fratelli Ruffatti o dei committenti dei loro strumenti. Le foto Unsplash e Pexels di `assets/esterne/` non sono in pagina e non vanno usate (restano solo come materiale dei prototipi, licenze in `assets/CREDITI.md`).

## Ritocco finale: che cosa resta fuori e perché

- **Versione inglese della home.** Per una commissione americana o inglese è il difetto più grave rimasto: EN porta al sito inglese di oggi (ora con il titolo "Il sito inglese di oggi (current English site)"). La home inglese (en/index.html, stessi blocchi: Recent instruments, Listen, Testimonials, What to send us, modulo con Institution e Position) va fatta quando la proposta italiana è approvata; molti testi esistono già in inglese sul loro sito (testimonianze, notizie, pagina contatti).
- **Un organo che suona.** I sette video del canale sono laboratorio, canne da 32' e il restauro di La Valletta: nessuno fa sentire uno strumento recente. Vanno chiesti un video di un concerto o di un'inaugurazione (Wayne, New Orleans, Pershore, Grand Rapids) con luogo, anno, organista e brano, il link alla puntata precisa di Pipedreams e un CD con estratto ascoltabile (punto 10).
- **Elenco filtrabile delle realizzazioni**: resta da fare nella pagina Realizzazioni del sito nuovo (punto 11); in home il link si chiama ora "86 opere significative, da una a sei tastiere", per non contraddire "oltre 500 organi in Italia".
- **Manutenzione e accordatura**: il riquadro del restauro chiede "Organo muto, sporco o da revisionare?" senza promettere il servizio; "Dicono di noi" cita "l'assistenza dopo l'installazione" (Mons. O'Doherty, Miami), ma va confermato con loro prima di scriverlo (punto 5).
- **Un restauro italiano documentato** in home (per esempio Villa Cortese 2021 o Modena 2019, dagli articoli diocesani citati nella scheda d'uso): servono il permesso e il link alla fonte.
