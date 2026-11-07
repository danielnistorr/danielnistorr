# Overdrive Customs, home: nota

## Metodo ibrido (novembre 2026)

3 novembre 2026. Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale com'era (sito intero e screenshot) è in `_prova/versione-pro/`. Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`; riga del registro in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`; provini delle foto: `_prova/alto/provini.jpg`.

Rifare: `python3 -I _prova/alto/script/img_ibrido.py` (immagini nuove), `python3 -I _prova/alto/script/build.py` (pagina dal modello `ibrido.tpl.html`), `node _prova/alto/misura-d.mjs [ora=AAAA-MM-GGTHH:MM]` (misure, esito in `_prova/alto/misure/misure-d.json` e `riassunto.txt`), `node _prova/alto/script/shot.mjs` (screenshot, ora simulata martedì 3/11/2026 alle 10), `node _prova/alto/script/posizioni.mjs` (posizioni dei compiti).

### Secondo giro (3 novembre 2026, notte)
Dopo il ritocco il giudice da agenzia dava 7, ma i clienti tipo erano scesi rispetto alla versione professionale (cliente 2 da 7,5 a 7, cliente 1 da 7,5 a 8 con dei compiti più lenti). Questo giro tiene la prima schermata della sezione D e lavora su due cose: i compiti persi e l'esecuzione sotto la piega. Copia di prima: `_prova/alto/rit2/prima/` (index.html e modello). Rifare: `python3 -I _prova/alto/script/rit2_img.py` (taglio verticale di Matteo per il telefono, Hagane nel campo con il trattamento della serie), poi `build.py`, `misura-d.mjs`, `shot.mjs`. Prove della barra e degli arrivi dal menu: `node _prova/alto/rit2/barra.mjs`; posizioni: `node _prova/alto/rit2/pos2.mjs`.

**Per i clienti tipo**
- **Seconda schermata sul nero**: subito sotto la foto d'apertura, sempre nell'apertura, le famiglie di moto (Harley-Davidson: Sportster, Softail e Dyna, Touring; custom giapponesi: Shadow, Dragstar e XVS; altre moto) e due strade, "Trasformazioni: bobber, chopper, bagger" e "Tagliandi, gomme, riparazioni". Sul telefono le famiglie stanno a 780-1000 px (prima a 3390-4363; la scheda chiede entro due schermate, 1688), le due strade a 1017-1113, sotto la barra e fuori dal tetto di D3. A 1440 la fascia parte a 871 px: il nero arriva oltre la piega e non c'è più la riga bianca.
- **Trasformazioni prima dei servizi**: l'ordine ora è apertura, Matteo, trasformazioni, "Mandami una foto", officina, special, orari. Sul telefono le schede hanno la foto a tutta colonna (350x197, prima 120x68) e le quattro famiglie cominciano a 2088, 2505, 2921 e 3338 px (prima 3390-4363, la scheda chiede circa 3.400).
- **Fin dove si arriva**: la riga sotto il titolo delle trasformazioni dice "da un kit fino al telaio fatto qui, come per Hagane, la special in apertura" con il link "Hagane e le altre special"; la didascalia d'apertura è "Hagane, Suzuki DR650 · telaio e forcella fatti qui"; in Le special Hagane ha di nuovo la sua foto nel campo. La 883 Old Style nella scheda Sportster è un link all'albo.
- **Barra in basso**: mentre si guardano le trasformazioni o i tre passi diventa "Manda la foto della tua moto" con il messaggio della trasformazione; altrove resta "Scrivi su WhatsApp" con il messaggio generico (cambia al passaggio, senza dissolvenza e senza IntersectionObserver).
- **Testata**: alta 60 px sul telefono; numero e Menu, "Moto ferma? Chiedi il ritiro" e tutti i link con la freccia ora hanno 48 px da toccare. Sul computer lo stato ha un punto verde quando è aperto e rosso chiaro con "Chiuso" o "In pausa" in grassetto quando è chiuso. Le voci del menu nominano quello che si cerca: "Orari e dove", "Tagliandi e riparazioni", "Trasformazioni", "Special e premi" (sul telefono anche "Moto ferma? Ritiro", "Come si comincia", "Le special e i premi"). Nel pannello lo stato di oggi ha lo stesso punto colorato.
- **Stato di oggi in apertura** sul telefono: la mattina aggiunge "Oggi anche 15:30-19.", prima delle 9:30 "Oggi 9:30-13 e 15:30-19.".
- **Orari e dove**: titolo, indirizzo e Indicazioni subito sotto; arrivando dal menu Indicazioni sta a 332 px dall'alto dello schermo (prima 481).
- **Tornati dalla versione professionale**: Hagane nel campo, la riga delle riviste (Ferro, Bikers Life, Kustom World, Special Cafe), gli oli e gli accessori di Kustomstore (nel piede, sotto l'indirizzo).

**Sotto la piega**
- **Una griglia, una giuntura**: tutti i blocchi su 72-1368 a 1440; il culmine parte attaccato al nero a tutte le larghezze, sotto ha 120 px a 1440 e niente filetto; sul telefono Matteo è un taglio verticale 0,86 (390x451, prima una striscia di 390x219) con la didascalia vera per quel taglio ("con una Sportster; l'officina è aperta dal 2 maggio 2015"), sul computer resta "accanto alla Ducati Envy, 1° Streetfighter al Biker Fest 2019".
- **Le special culminano**: Hagane nel campo a 1076x606 (c1-10, alla misura del file) con la didascalia nella colonna di margine (c11-12, a filo del fondo della foto): nome, anno, telaio e forcella fatti da noi, 1° Metric a Lignano 2024. Sotto, la Drakkar con il gesto dell'apertura che torna una volta: DRAKKAR in Unbounded 500 posato sul pavimento della foto, a 96 px (sotto il tetto dei 100), con la didascalia a due voci; accanto le due copertine e le riviste in una riga. L'albo va a tutta griglia, una riga per premio con Anno, Moto, Premio, Dove (sul telefono il luogo sotto il premio).
- **Teste di sezione diverse**: Trasformazioni con il titolo a sinistra e la riga a destra; "Mandami una foto" sul rosso; Officina con titolo, testo e il riquadro nero del ritiro nella colonna di sinistra (c1-5) e i tre servizi come righe d'indice senza foto a destra (c7-12, titolo, frase, link); Le special con il titolo a sinistra e la frase-firma a destra; Orari con il titolo sopra e tre colonne sotto.
- **Tolto perché ripetuto**: le famiglie dentro Officina (ora nella seconda schermata), il primo paragrafo di Officina che ripeteva l'h1, la tabella "Sulle riviste" (una riga sotto le copertine), il racconto di Hagane e di Drakkar doppio rispetto alle didascalie, "Vigonovo" due volte nella riga d'apertura, le tre foto dei servizi.
- **Finiture**: h2 con `text-wrap:balance` e `&nbsp;` sulle ultime parole ("della tua&nbsp;moto", "Vigonovo&nbsp;(VE)", "di&nbsp;Matteo"); "testa… Li creo io!" con U+2026 (la fonte ha quattro punti); la E di HAGANE staccata di 0,035 em dalla N (uno span vuoto, il corpo ricalcolato su 5,315: l'inchiostro resta 206-1234 a 1440, 20-370 a 390, 446-1474 a 1920); h1 a 21 px da 1100 px (22 non entra su una riga accanto alla didascalia); "Altre moto" senza maiuscola dentro la frase; nel piede il © su una riga sua e Privacy e Cookie insieme sul telefono.

**Misure finali** (`misura-d.mjs`, martedì alle 10; passano tutte le 35 soglie): 1440 foto 67%, 6 cliccabili, 1 bottone, 153 caratteri, 0 cifre di 30 px; 390 4 cliccabili, 1 bottone, foto e gesto al 53,5%; Chivo e Unbounded, testo a 18 px, un solo elemento sopra i 100 px (HAGANE a 193,4 px), 0 occhielli, h1 di 9 parole e 1 virgola visibile a 1440 e a 390, lista nera 0; 827 parole (prima 849), 7 sezioni, 7.440 px a 1440 (prima 7.481) e 10.685 a 390 (prima 10.199, per le foto delle trasformazioni a tutta colonna); griglia 72-1368 a 12 colonne; 10 foto (prima 12), formati 4:3, 16:9, 4:5 a 1440 e 0,86, 16:9, 4:5 a 390, 0 ingrandite da 320 a 1920; fondi nero, bianco e rosso, rosso su un blocco; `tel:` 2, Indicazioni 1, WhatsApp generico 2, ritiro 2, email 2, Instagram 1, numero in vista 2; 4 bottoni; 869 KB a 1440 e 475 KB a 390; 0 scorrimenti orizzontali, 0 sovrapposizioni, 0 errori di script, 0 U+2014.

**Aperto dopo questo giro**
- A 1920 la foto d'apertura torna al 42% della schermata: sotto c'è la fascia nera delle famiglie, non più il culmine. Il nero non è vuoto (c'è il testo per i clienti), ma la soluzione vera resta il file di Hagane a 2000 px o più.
- Il voto del giudice e dei clienti tipo su questa versione non è stato rifatto.
- D8 resta sopra la soglia della sezione D (827 parole, 7.440 px), dentro quella dell'ibrido (900 e 7.500).

### Ritocco dopo il giudice da agenzia (3 novembre 2026, sera)
Il giudice dava 6,5 (5,5 alla versione professionale): l'apertura ha un gesto suo, ma restavano la foto da telefono in fiera, una pagina che tornava a sembrare un modello sotto la piega e la finitura. Prima schermata della sezione D invariata nella sostanza (6 cliccabili, 1 bottone, 157 caratteri a 1440). Copia di prima: `_prova/alto/rit/prima/` (index.html, modello e foto d'apertura). Rifare: `python3 -I _prova/alto/script/rit_img.py` (foto d'apertura, copertine, Drakkar), poi `build.py`, `misura-d.mjs`, `shot.mjs`; `_prova/alto/script/inchiostro.mjs` misura dove cade l'inchiostro di HAGANE.

**Applicato**
- **Didascalia d'apertura**: "Suzuki DR650 costruita a Vigonovo · **in mostra nel 2025**" (l'anno del post e della targa, certo). Non contraddice più la targa "Official Custom Show 2025". Il "1° Metric, Biker Fest di Lignano 2024" è passato nel racconto di Hagane e resta nell'albo. Il Freestyle non si scrive finché Matteo non dice l'evento.
- **Foto d'apertura ritrattata** dall'originale 1080x810 (`rit_img.py`), senza togliere niente: tolto il 22% del dettaglio di media scala (l'HDR del telefono), alte luci giù del 16% circa nel terzo superiore (il soffitto al neon), spalla sulle alte luci, poi lo stesso trattamento della serie (saturazione 0,88, contrasto 0,97). Sfumatura sotto il nome più piena da 1100 px (48%, da .92 a 0): il tappeto col logo tra le lettere quasi non si legge più.
- **HAGANE sui bordi**: corpo calcolato su 5,28 e attacco a 0,077 em. L'inchiostro va da 206 a 1234 a 1440 (h1 a 206, didascalia fino a 1234), da 20 a 370 a 390 (h1 e didascalia 20-370), da 446 a 1474 a 1920. La riga sotto non si allarga più quando il nome sborda (colonna `minmax(0,1fr)`).
- **Tablet**: la foto si ferma 150 px sopra il fondo invece di 92. A 1024x768 l'h1 finisce a 643 e la didascalia a 671, la barra di WhatsApp comincia a 699; a 768x1024 la didascalia finisce a 645 e la barra parte da 955.
- **1920**: il nero si chiude sulla foto e il culmine parte subito sotto (sopra i 1600 px la sezione non ha spazio in alto). A 1920x1080 la foto occupa il 61% della schermata (prima il 42%, nella fascia vietata).
- **Il culmine è una sezione a sé**, subito dopo l'apertura: Matteo in officina al vivo, 1440x810 a 1440 (file da 2560, mai ingrandito; 1920x1080 a 1920), didascalia a due voci sulla griglia a 72 px, 144 px sopra e sotto, nessun filetto dopo. È l'unica foto al vivo della pagina sul computer. Sul telefono resta 16:9 a tutta larghezza (390x219), così la didascalia con la Ducati Envy resta vera e i formati restano 3.
- **Nuova sezione "Tagliandi, riparazioni e restauri, sulla tua moto"**: famiglie, tre servizi con i messaggi WhatsApp, il ritiro col furgone, oli e accessori. Il menu "Officina" porta qui.
- **Le special con la foto della Drakkar** (960x540 dalla versione professionale, la serie davanti alla lamiera), alla misura vera in c1-6 con la didascalia "Drakkar, Road King bagger / 1° Bagger, American Dream Padova 2021", e la frase-firma sotto. A destra (c7-12) i racconti di Hagane e Drakkar e le copertine. Sotto, l'albo a tutta griglia (una riga per premio). Le riviste in righe corte sotto la frase. Foto in home: 12.
- **Copertine ritagliate sul loro rettangolo**, senza il margine bianco del post, tutte e due 4:5 e alla stessa altezza (306x383 a 1440, bordi a 732 e 1062 come le loro didascalie). Il 1:1 non c'è più: i formati sono 4:3, 16:9 e 4:5 (al telefono 0,86, 16:9 e 4:5).
- **Teste di sezione diverse**: tutti gli h2 su c1-6 (72-708). Testo a destra solo in Officina e in Trasformazioni; "Mandami una foto" passa da c1-5 a c1-6; in Le special il titolo sta da solo; in "Orari e dove" il testo sta sotto l'h2, nella stessa colonna. Il culmine non ha testa.
- **Colonne**: dentro Le special solo 6/6 e la riga intera dell'albo, niente più 8/4.
- **Virgolette e apostrofi tipografici** nel testo visibile e nel modello `ibrido.tpl.html`: “ ” per tutte le citazioni, ’ per gli apostrofi. Controllo: nel testo visibile 0 virgolette dritte, 0 apostrofi dritti (i messaggi WhatsApp già scritti restano come li scriverebbe chi li manda).
- **Modulo chiuso** in un `<details>`: "Preferisci l’email? Apri il modulo". Si apre anche dal link "Il modulo per l’email" del piede (l'ancora `#scrivi` lo apre). L'email per riviste e fiere resta in vista. Bottoni in pagina: 4. La pagina passa da 7.445 a 7.481 px a 1440, con il culmine al vivo e la Drakkar in più; a 390 da 10.761 a 10.199.
- **Strada "Riviste e fiere"** con la persona e l'orario: "Matteo, per email; in officina su appuntamento, martedì-venerdì."
- **Menu del telefono** (per i clienti tipo, senza toccare la prima schermata): sotto le voci lo stato di oggi e l'indirizzo, "Aperto ora, fino alle 13, solo su appuntamento. Via San Francesco 8/a, Vigonovo (VE)". Senza JavaScript dice gli orari della settimana.
- **Le special al telefono e al tablet** in quest'ordine: Drakkar, racconti, copertine, frase-firma, riviste, albo.
- **Misure**: in `misura-d.mjs` quello che sta dentro un `<details>` chiuso non conta come visibile (prima il modulo chiuso risultava sovrapposto al piede).

**Respinto, con il motivo**
- **Hagane al vivo, a 2000 px o più**: non c'è il file. Serve l'originale del fotografo o lo scatto nuovo davanti al portone (LEGGIMI). È più della metà della distanza dal 7,5 secondo il giudice.
- **Ruote tagliate dal bordo nelle schede**: sono i tagli dei file 960x540 della serie. Gli originali da cui ritagliarli più larghi sono stati cancellati dal riavvio. `object-fit: contain` lascerebbe bande vuote. Si rifà con i file pieni o con il servizio fotografico.
- **Una sola luce per la serie**: non si ottiene col trattamento colore. Serve il servizio fotografico.
- **Le quattro scelte del modulo in vista fuori dal `<details>`**: sarebbero un secondo modulo a metà. In vista restano l'email (strada "Riviste e fiere") e WhatsApp.

### Le misure dopo il ritocco (`misura-d.mjs`, martedì alle 10; tutte le 35 soglie passano)
1440: foto 67%, 6 cliccabili, 1 bottone, 157 caratteri, 0 cifre di 30 px o più, HAGANE a 194,7 px (unico sopra i 100). 390: 4 cliccabili, 1 bottone, foto e gesto al 53,5%. 1920: foto 61%. Due famiglie (Chivo, Unbounded), testo a 18 px, 0 occhielli, h1 di 9 parole e 1 virgola visibile a 1440 e a 390, lista nera 0. 849 parole, 7 sezioni (apertura, culmine e 5), 7.481 px a 1440. Griglia 72-1368 a 12 colonne. 12 foto, 3 formati per larghezza, 0 ingrandite da 320 a 1920. Fondi nero, bianco e rosso, rosso su un blocco, spazi 0 (culmine sopra i 1600 px), 96 e 144. `tel:` 2, Indicazioni 1, WhatsApp generico 2, ritiro 2, email 2, Instagram 1, numero in vista 2. 4 bottoni in pagina. 710 KB a 1440, 492 KB a 390. 0 scorrimenti orizzontali, 0 sovrapposizioni, 0 errori di script, 0 U+2014.

Posizioni sul telefono (390x844): h1 a 517-563, stato a 616-695, ritiro a 697-741; famiglie a 3390-4363 (prima 3287-4259, in mezzo ora c'è il culmine come sezione); Indicazioni a 8136, a un tocco da Menu, "Orari e dove". A 1440: officina a 2006, trasformazioni a 3214, special a 4444, albo a 5486, orari a 6004.

### Che cosa era cambiato nel primo passaggio ibrido
- **Idea e gesto** (D1): il nome della special, HAGANE, in Unbounded 500, largo esattamente quanto la sua foto e posato sul pavimento, bianco su una sfumatura scura locale. Modello N, riferimento Fuller Moto ("THE RAPTOR T"). Sotto il nome, sulla stessa foto, una riga: a sinistra l'`h1` "Officina Harley-Davidson e custom giapponesi a Vigonovo" (9 parole con "Overdrive Customs," nascosto per i lettori di schermo), a destra "Suzuki DR650 · 1° Metric, Biker Fest di Lignano 2024".
- **Foto d'apertura** (D2): Hagane in mostra, post Instagram del 21/04/2025 (`DItlSo1tnWX`, 1080x810), ripreso dal sito dell'azienda insieme alla copertina del sito a 2560x1440 (la cartella `assets/originali/` era stata cancellata dal riavvio). Alla misura vera, centrata su 10 colonne: 1076x807 a 1440, il 67% della prima schermata. Sul telefono lo stesso scatto tagliato in verticale sul davanti (700x810, a 390x451). Hagane nel campo, la foto della versione di prima, esiste solo a 1080x608: alla misura vera sarebbe stata il 51%, nella fascia vietata.
- **Testata** (D3): logo non cliccabile, quattro voci (Orari e dove, Officina, Trasformazioni, Le special), lo stato di oggi in breve ("Aperto, su appuntamento", "In pausa fino alle 15:30", "Chiuso, riapre martedì"), il numero 340 251 0434 cliccabile e un solo bottone, WhatsApp. Sul telefono e sul tablet: logo, numero, Menu; WhatsApp diventa la barra fissa in basso (lo stesso link, spostato).
- **Culmine**: Matteo in officina (la copertina del sito) a tutta griglia, 1296x729 a 1440, didascalia "Matteo in officina, via San Francesco 8/a, Vigonovo / accanto alla Ducati Envy, 1° Streetfighter al Biker Fest 2019". La sezione è alta 2141 px, con 144 px di spazio sopra e sotto contro i 96 delle altre.
- **Sotto la piega** tornano dalla versione professionale: le famiglie di moto, i tre servizi con il messaggio WhatsApp per caso, il blocco del ritiro col furgone, gli oli e gli accessori di Kustomstore, le quattro trasformazioni con i lavori fatti, i tre passi con "Manda la foto della tua moto", le copertine di Kustom World e Bigtwin, Hagane e Drakkar in due righe, l'albo dei primi posti (7 righe), le riviste, gli orari con lo stato e il giorno di oggi, indirizzo e Indicazioni, il contatto diviso in due strade (officina e ritiro; riviste e fiere con le tre fiere), il modulo che prepara l'email. Il piede è un biglietto da visita con la frase-firma.
- **Tolto**: il titolo grande in apertura, il secondo bottone, l'occhiello, la fascia dei quattro fatti sotto la foto, la fascia delle cifre (2015, 8, 3, 3), le citazioni con il bordo rosso, il ritratto in bianco e nero, le foto in studio della 883 e di Special K (restano nell'albo), la foto della Drakkar, la seconda citazione di Matteo, i doppioni di telefono, Indicazioni, WhatsApp e email nel piede e nell'apertura.
- **Griglia**: una sola, 12 colonne, margini di 72 px a 1440 (32 dal tablet, 20 sul telefono), colonne di 86 px con 24 di spazio; tutti i blocchi partono a 72 e finiscono a 1368, anche i filetti tra le sezioni.
- **Caratteri**: Unbounded 500 e Chivo 400-600 al posto di Archivo (licenze in `sito/fonts/`). Sono incorporati nella pagina come data URI: da `file://` Chrome blocca i woff2 esterni con un errore CORS (lo misura `misura-d.mjs`; con ogni probabilità succedeva anche alla versione professionale).
- **Frase-firma**: "I mostri non sono nella vostra testa.... Li creo io!" (Matteo, ottobre 2023), uguale in "Le special" e nel piede.

### Le misure del primo passaggio ibrido, prima del ritocco
| Controllo | Soglia | Valore |
|---|---|---|
| Foto nella prima schermata a 1440 | 60% o più, o sotto il 12% | 67% (1076x807, file 1080) |
| Foto o gesto a 390 | almeno 50% | 53,5% |
| Cliccabili e bottoni a 1440 | 6 e 1 | 6 e 1 |
| Cliccabili e bottoni a 390 | 4 e 1 | 4 e 1 (numero, Menu, WhatsApp, "Moto ferma? Chiedi il ritiro") |
| Caratteri fuori dal menu a 1440 | 160 | 146-156 secondo lo stato di oggi (provati festa, pausa, chiuso, prima dell'apertura) |
| Cifre di 30 px o più | 0, salvo il gesto | 0 |
| Elementi sopra i 100 px | 1 | 1 (HAGANE, 192 px a 1440, 67 a 390) |
| Famiglie di caratteri | 2 | Chivo, Unbounded |
| Testo corrente a 1440 | almeno 17 px | 18 px |
| Occhielli sopra `h1` e `h2` | al massimo 1 | 0 |
| `h1` | 9 parole, 1 virgola | 9 parole, 1 virgola, visibile a 1440 e a 390 |
| Parole | 900 | 887 |
| Sezioni | 7 | 6 più il piede |
| Altezza a 1440 | 7.500 px | 7.445 px (prima 10.567); a 390 circa 10.800 (prima 14.085) |
| Griglia | un bordo sinistro e uno destro | 72 e 1368, 12 colonne ovunque |
| Foto ingrandite | 0 | 0 a 320, 390, 768, 1024, 1440, 1920 |
| Foto e formati | 12 e 3 | 11; 4:3, 16:9, 1:1 (a 390 il verticale dell'apertura al posto del 4:3) |
| Fondi oltre al piede | 3 | nero, bianco, rosso; rosso pieno su un blocco solo ("Come si comincia") |
| Spazi tra le sezioni | almeno due valori | 96 e 144 |
| Ripetizioni | al massimo 2 | `tel:` 2, WhatsApp generico 2, ritiro 2, email 2 (link e modulo), Indicazioni 1, Instagram 1, numero in vista 2 |
| Bottoni in pagina | 5 | 5 |
| Peso caricato | sotto 3 MB | 680 KB a 1440, 448 KB a 390 |
| Scorrimento orizzontale, sovrapposizioni, errori di script | 0 | 0 a 320, 390, 768, 1024, 1440, 1920 |
| U+2014, "indicativ", Inter, dissolvenze | 0 | 0 |

### I compiti della scheda nel primo passaggio ibrido (390x844 e 1440x900)
- **Motociclista, telefono**: mestiere e luogo nell'`h1` a 517-563 px, sotto il nome; stato di oggi e "Solo su appuntamento" a 616-695; WhatsApp nella barra fissa in basso e il numero in testata, da qualunque punto; "Moto ferma? Chiedi il ritiro" a 697-741, nella prima schermata (il blocco del ritiro a 2493); "Indicazioni" in "Orari e dove", prima voce del menu (a 7722 scorrendo).
- **Chi vuole trasformare, telefono**: le quattro famiglie a 3287-4259 px, con "Trasformazioni" nel menu; "da un kit fino al telaio fatto qui" nella riga sotto il titolo delle trasformazioni e nel passo 2, Hagane con telaio e forcella fatti in casa in "Le special"; i tre passi con "Come si comincia" nel menu; "Manda la foto della tua moto" apre WhatsApp con il messaggio già scritto, e la nota sulla graffetta è a 14 px accanto al bottone.
- **Appassionato e stampa, computer**: Hagane con il nome, il premio, la fiera e l'anno nella prima schermata; albo e copertine con "Le special" (un clic, a 4250); email per riviste e fiere e Instagram in "Orari e dove", l'email anche nel piede; le tre fiere con città e mese in "Orari e dove".

### Problemi aperti (aggiornati dopo il ritocco)
- **L'evento della foto d'apertura**: davanti alla moto c'è la targa "Official Custom Show 2025, 1° Freestyle". La didascalia ora dice solo "in mostra nel 2025". Va chiesto a Matteo l'evento; con l'evento diventa "Hagane in mostra a ..., 2025" e il Freestyle può entrare nell'albo.
- **1080 px**: a 1440 la foto è alla misura vera ma su uno schermo retina è morbida. A 1920 il culmine subito sotto porta la schermata al 61% di foto, ma Hagane resta di 1076 px al centro del nero. Serve l'originale del fotografo o uno scatto nuovo di Hagane davanti al portone: con quello l'apertura va al vivo.
- **Le quattro famiglie sul telefono** stanno a 3390-4363 px, cento più di prima, perché il culmine ora è una sezione a sé. Ci si arriva con un tocco da "Trasformazioni" nel menu.
- **Indicazioni una volta sola** (D12): sul telefono il menu ora mostra l'indirizzo e lo stato di oggi; il link è in "Orari e dove", prima voce del menu.
- **In testata a 1440 c'è il numero ma non la parola "Chiama"**, per stare nei 160 caratteri. Il link "Chiama 340 251 0434" scritto per intero è in "Orari e dove".
- **La luce delle foto non è una sola** e le schede hanno le ruote vicine al bordo: serve il servizio fotografico.
- **Due modelli N con la stessa grammatica nella zona** (questa e BCM): è il massimo, non va ripetuto in altre home.
- **Non rifatti**: il controllo D1 delle tre persone, la media delle prime schermate della zona (D4) e i nuovi voti del giudice e dei clienti tipo.
- **Da confermare** come prima: Kustomstore e i cappellini, orari, WhatsApp sullo stesso numero, ritiro (zona e costo), l'evento della foto d'apertura, ragione sociale e P.IVA nel piede.

---

## (Nota di prima) Livello professionale, con il ritocco finale (3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), carattere in `sito/fonts/`. La home di prima del livello professionale (Hagane scontornata sul bianco calce, titolo "Special, dal telaio in su", selettore delle moto) è in `_prova/versione-1-originale/`; quella del primo passaggio professionale, prima di questo ritocco, è in `_prova/pro-controllo/` (screenshot del controllore: home-1440-prima.jpg, home-390-prima.jpg e le pagine intere a pezzi).

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari) adattata a un'officina di quartiere che lavora su appuntamento, sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati di nuovo per il ritocco: le prime schermate a 1440 e 390 di tutti e 14 (`riferimenti.jpg`, `rif-tutti-390.jpg`, `rif-altri-1440.jpg`) e le pagine intere di Union e Joseph Brot, a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, pagina con `pro_pagina.py` dal modello `pro_pagina.tpl.html`, screenshot con `pro_shot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, JPEG con `pro_jpg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro-controlli.json`). Senza `--immagini` rifà solo pagina, screenshot e controlli. Misure rapide delle posizioni: `node _prova/script/ritocco_misure.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (10567 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (14085 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove" al piede), `selettore-1440.jpg` (la sezione "Le special", che ha preso il posto del selettore), prime schermate a 320, 768, 1024 e 1920, `menu-390.jpg` (menu aperto). Guardati a pezzi a 1440 e 390; prime schermate a 320, 768 e 1024 guardate una per una.

### Che cosa è cambiato nel ritocco

- **Apertura** (era lo schema delle home della campagna, titolo a sinistra e foto 801x451 a destra): ora è un blocco nero. Sul computer l'occhiello "Vigonovo (VE), Riviera del Brenta · dal 2015" e il titolo bianco "Officina Harley-Davidson e custom giapponesi" (88 px) stanno in alto su tutta la larghezza; sotto, su una riga, lo stato di oggi e i due bottoni; poi la foto vera dell'officina a tutta larghezza (1440x706, taglio 2,04:1 che tiene il cappello di Matteo e le ruote), larga al massimo 1600 px. Sotto la foto una fascia nera in quattro colonne con filo rosso: ritiro col furgone, indirizzo e Indicazioni, i lavori dell'officina, la prova "1° al Biker Fest 2024" con le copertine. A 1440x900 la foto occupa 1440x461 della prima schermata (prima 801x451). Sul telefono resta l'ordine voluto dalla scheda (foto in alto senza testo sopra, poi titolo, stato, WhatsApp, Chiama), ora su nero; "Moto ferma?" sale subito sotto i bottoni.
- **Testata nera** con logo bianco, menu, "WhatsApp" col bordo e "Chiama 340 251 0434" pieno; nel menu del telefono ci sono anche "Moto ferma? Ritiro" e "Come si comincia".
- **Scala**: testo corrente a 17 px a 1440 (prima 16); titoli delle sezioni principali a 56 px a 1440 e 28 a 390 (prima tutti a 32); il manifesto "I mostri non sono nella vostra testa.... Li creo io!" a 88 px su tutta la larghezza; "La tua moto, trasformata" ha l'intestazione al centro, titolo e testo uno sotto l'altro. Tolto il grigio dai testi lunghi (resta solo nelle note di una riga).
- **Trasformazioni**: la scheda Sportster ora è la Sportster 48 "Jericho" davanti alla lamiera (post del 08/01/2021), come le altre tre; la 883 con Matteo, in studio, è passata tra le special. Sul telefono le schede sono righe compatte (miniatura e titolo, testo e link sotto) e le quattro schede stanno a 2474, 2740, 3005 e 3294 px, con le etichette delle famiglie a 2487, 2753, 3018 e 3307 (prima 2839, 3250, 3685, 4167). La foto non è più un link: il link è "Ho una Sportster: scrivimi", alto 44 px. La scheda Softail dice i lavori dei post (cambio a mano "suicide shift", ruota da 21 pollici, scarichi Vance & Hines su una Dyna).
- **Le special**: tre racconti grandi alternati, foto 737 px a 1440: Hagane (foto a sinistra), Drakkar (a destra, con il kit di @killer.custom e la vernice "Carraragray"), 883 Old Style (a sinistra). Special K, dello stesso servizio in studio della 883, sta accanto all'albo dei primi posti.
- **Prove**: "3 copertine: Bikers Life 2021, Kustom World 2024, Bigtwin 2025" (prima "2", in contrasto con la scheda di Drakkar); nuova fascia "Riviste che hanno pubblicato le nostre moto" (Ferro 2015, Bikers Life dal 2018, Kustom World 2018-2024, Special Cafe 2023, Bigtwin 2025).
- **Come si comincia**: il passo 3 ora è un passo ("Si costruisce qui, con artigiani tra Padova e Venezia: selle di Cisco Leather, vernici di Rolling Paint"); sotto il bottone "Si apre WhatsApp con il messaggio pronto: allega la foto con la graffetta e invia."
- **Piccoli**: link della fascia d'apertura e del piede con un'area da toccare di 44 px; "Lavoro con" con i testi attaccati al nome; bottoni "Chiama 340 251 0434" senza il doppio stacco; nei festivi "Oggi chiuso per festa, riapre ... alle 9:30"; "Solo su appuntamento: scrivimi prima di passare" nel corpo normale, non più grigio; il messaggio WhatsApp principale è neutro ("Ciao Matteo, ti scrivo per la mia moto. È una: ").

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. A 390, a metà pagina, il bottone "340 251 0434" sta in alto (top 8, alto 48 px) e si tocca; 4 link `tel:` (testata, apertura, sede, piede); la prima voce del menu è "Orari e dove".
2. **Prima schermata con mestiere, luogo, prova e azione**: PASSA. 1440x900: "Vigonovo" e "dal 2015" a 121 px, "Harley" a 153, WhatsApp e Chiama a 349-401. 390x844: "Vigonovo" e "2015" a 345, "Harley" a 377, WhatsApp 633-685 largo 350 px, Chiama 695-747.
3. **Immagine vera nell'apertura**: PASSA. La copertina del sito (2560x1440, Matteo in officina, fascia rossa, cartello TRASPORTO), a tutta larghezza: 1440x706 a 1440, 390x260 a 390. Nessuno scontorno.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche (i segnaposto Unsplash di `assets/esterne/` non sono usati); nessuna illustrazione al posto delle foto.
5. **Foto in serie**: NON PASSA del tutto. Formati: 3 a 1440 (2,04:1 l'apertura, 16:9 le schede e i racconti, 1:1 copertine e ritratto) e 3 a 390 (3:2, 16:9, 1:1); 2 didascalie su 15 foto. La luce invece non è una sola e con le foto che hanno non può esserlo: ho raggruppato le foto per serie (officina e trasformazioni tutte di fianco davanti alla lamiera grigia, con lo stesso trattamento di `pro_img.py`; la 883 e Special K, servizio in studio di @boemphoto, vicine tra le special), ma restano Hagane nel campo al sole e il ritratto in bianco e nero. Serve la mezza giornata di foto descritta nel LEGGIMI.
6. **Palette dal marchio**: PASSA. Nero #151515, bianco #FFFFFF delle pareti, rosso #B3261E della fascia e degli scaffali, verde #22663A solo per "Aperto" (sul nero dell'apertura lo stesso verde schiarito, #7BD88F, per leggerlo); grigi lamiera (#26292C, #5B5F64, #A9ADB2, #D6D7D8, #EFF0F1). Niente `--carta`.
7. **Scala corta e leggibile**: PASSA. 1440: 88, 56, 32, 22, 19, 17, 14 px; 390: 40, 36 (numeri dei passi), 28, 20, 17, 16, 14 px. Testo corrente 17-19 px a 1440 e 16-17 a 390; 14 px solo per occhielli ed etichette in maiuscolo spaziato e la riga legale. H1 88 px maiuscolo, interlinea 0,95.
8. **Due famiglie al massimo**: PASSA, con una sola. Archivo: titoli in maiuscolo stretto (larghezza 75 %, peso 800), testo, etichette e bottoni a larghezza normale in 400 e 800.
9. **Servizi in schede con la foto del lavoro**: PASSA. "In officina": 3 colonne, 3 schede tutte cliccabili con foto 16:9 di quel lavoro, nome e link a WhatsApp. Le trasformazioni sono lavori e non servizi: lì la foto non è un link (richiesta della prova d'uso) e il link è in fondo alla scheda.
10. **Almeno tre tipi di prove**: NON PASSA. Dei quattro tipi della regola ce ne sono due: 4 numeri aziendali (2015, 8 primi posti, 3 copertine, 3 fiere fisse) e la fascia dei fornitori con didascalia ("Lavoro con": Cisco Leather, Rolling Paint, Kustomstore). In più ci sono prove forti fuori dai quattro tipi: la fascia delle 5 riviste, le copertine, l'albo dei primi posti. Recensioni con nome e comune e clienti con il nome non sono nelle fonti (Paginegialle e Cylex 403, Facebook senza login): non le invento, sono nel LEGGIMI tra le cose da chiedere. Con tre recensioni vere della scheda Google la regola passa.
11. **Lavori con un nome**: PASSA. Tre racconti con nome, anno, luogo (la fiera) e 2-3 dati, ognuno con la foto a 737 px su 1440 (più di metà pagina): Hagane 2024, Drakkar 2021, 883 Old Style 2023 (il file della 883 è di 704 px, mostrato a 737). In più Special K, l'albo di 7 righe e 4 trasformazioni con l'anno. Il cliente non ha il nome: nei post ci sono solo i profili Instagram dei proprietari, che non metto senza permesso.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: apertura nera, "Come si comincia" rossa, "Le special" nera; "In officina" e "Orari e dove" grigio chiaro, trasformazioni e "Chi c'è dietro" bianche. Spazio tra le sezioni 120 px a 1440 e 64 a 390; margini 64 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno (rosso; bianco sul rosso) e con il bordo; raggio 4 px; 52 px (48 in testata); testo 17 px a 1440 e 16 a 390, peso 800. I bottoni di chiamata hanno il numero (sotto 360 px quello della testata dice solo "Chiama").
14. **Modulo e "dove e quando"**: PASSA. Modulo in home con il tipo di richiesta in 4 caselle, nome, telefono, email, moto, messaggio; compone un'email (mailto con oggetto "tipo, nome" e tutti i campi), da collegare a un servizio (LEGGIMI). Scheda della sede con orari in tabella e il giorno di oggi in neretto, "Indicazioni" (Google Maps, percorso), "Chiama" e WhatsApp. Nessun iframe.
15. **Piede completo**: NON PASSA del tutto. Ci sono nome, indirizzo con Indicazioni, telefono, WhatsApp ed email cliccabili, orari, link della pagina, Instagram col sottotitolo, Privacy e Cookie, in 4 colonne a 1440 con testo di almeno 14 px e link alti 44 px. Mancano ragione sociale e partita IVA, che non sono pubbliche: non le invento (LEGGIMI). Certificazioni: non ne hanno. Privacy e Cookie puntano a `/privacy` e `/cookie`, pagine da scrivere (oggi 404 anche sul sito attuale).

In sintesi: 12 regole passano, 3 no (5 per la luce delle foto, 10 per le recensioni, 15 per la P.IVA). Tutte e tre dipendono da materiale che l'azienda deve dare.

### Uso (scheda `_prova/uso/SCHEDA.md`, paragrafo 8), dopo il ritocco

- **Visitatore 1, telefono 390x844**: "Harley-Davidson" e "Vigonovo" sopra 844 px; WhatsApp (`wa.me/393402510434`, "Ciao Matteo, ti scrivo per la mia moto. È una: ") alto 52 px a 633; `tel:+393402510434` a 695; stato di oggi a 545: martedì alle 10 "Aperto ora, fino alle 13. Solo su appuntamento: scrivimi prima di passare. Oggi 9:30-13 e 15:30-19."; alle 14 "In pausa, riapre alle 15:30"; venerdì alle 19:30 "Chiuso, riapre martedì alle 9:30"; domenica "Oggi chiuso, riapre martedì alle 9:30"; lunedì "riapre domani"; 8 dicembre e Pasquetta "Oggi chiuso per festa, riapre domani alle 9:30". "Moto ferma? La vengo a prendere col furgone. Chiedi il ritiro" a 767-823 (prima 925, fuori dalla prima schermata); "Indicazioni" a 826 (prima 764: ora sta sul bordo della prima schermata, sempre con un tocco). Link della fascia con area da toccare di 44 px (prima 17). Riesce come prima, il ritiro meglio.
- **Visitatore 2**: le quattro famiglie a 2474, 2740, 3005 e 3294 px: entro tre scorrimenti (3376 px) c'è un caso per famiglia con la foto e il titolo, anche senza passare dal menu (prima riusciva solo col menu). "Come si comincia" ha la sua voce nel menu; "Manda la foto della tua moto" apre WhatsApp con "Ciao Matteo, ti mando la foto della mia moto: vorrei trasformarla. L'idea è: " e la nota dice di allegare la foto. Toccare la foto di una scheda non apre più WhatsApp. Riesce meglio.
- **Visitatore 3, computer**: Hagane con premio, anno e le due copertine nello stesso racconto; Drakkar e la 883 con fiera e anno; le tre fiere col mese; Instagram ed email per la stampa in "Orari e dove" e nel piede. Riesce come prima.
- **Identità**: le frasi di Matteo citate così come le ha scritte ("I mostri non sono nella vostra testa.... Li creo io!", "In molti, visti i tempi, non avrebbero scommesso un euro su questo progetto.", "Non siamo importanti come gli altri...quelli grossi...ma ci siamo anche noi.", "now better than new", "artigiani tra Padova e Venezia"); prima persona di Matteo. L'apertura nera con la foto grande dell'officina dice "officina custom" e non più "servizio".

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 414, 600, 768, 899, 900, 1024, 1099, 1100, 1280, 1440, 1920, 2560 (`pro_controlli.mjs`).
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440, 1920. Corretto durante il lavoro: a 1440 il titolo andava su tre righe accanto ai bottoni (ora titolo su tutta la larghezza e bottoni sulla riga sotto); i link nel testo della fascia d'apertura con l'area di 44 px spezzavano l'interlinea (ora l'area è fatta con il padding).
- Collegamenti: `tel:+393402510434`; `https://wa.me/393402510434` con dieci messaggi diversi già scritti; `mailto:overdrivecustoms@live.com`; Google Maps in percorso su "Overdrive Customs, Via San Francesco 8/a, 30030 Vigonovo VE"; Instagram; nessuna ancora rotta (nuove: `#ritiro`, `#comincia`).
- Dato strutturato `MotorcycleRepair` (schema.org) con indirizzo, telefono, orari e Instagram.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

Archivo (Omnibus-Type), da Google Fonts, file variabile con gli assi di peso e larghezza servito da `sito/fonts/` (woff2 latin e latin-ext), SIL Open Font License 1.1 (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito.

### Non applicato, apposta

- Foto dell'apertura a tutta larghezza senza niente sopra fino al bordo della prima schermata (come Union e Joseph): a 1440x900 i bottoni devono stare nella prima schermata, quindi titolo e bottoni stanno sopra la foto, sul nero. Testo sopra la foto: no, la scheda vuole la foto senza testo e le pareti bianche non reggono un titolo bianco.
- Spostare "Orari e dove" prima di "Chi c'è dietro" (prova d'uso, minore): lo stato di oggi, gli orari brevi, l'indirizzo e Indicazioni sono già nella prima schermata; la tabella completa resta vicino al modulo e al piede, e il menu ci porta con un tocco.
- Novità di stagione: non c'è una fonte per la prossima fiera con le date.
- Recensioni, clienti con il nome, certificazioni, partita IVA, "il preventivo si fa dopo aver visto la moto", zona e costo del ritiro: non sono nelle fonti o sono da confermare; nel LEGGIMI.
- Newsletter: no, Instagram è il loro canale.

---

## Versione 1 originale (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Proposta non richiesta di nuova homepage (solo la home). Pagina in `sito/index.html`, immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `_prova/script/build_finale.sh`.

### L'idea
Una moto sola, sul bianco calce, con le legende che dicono chi ha fatto ogni pezzo: è Hagane, la chopper che ha vinto la categoria Metric al Biker Fest 2024 ed è finita in copertina su Kustom World e su Bigtwin. Il titolo è **Special, dal telaio in su**: viene dal loro post del 20/06/2024 ("Frame, front fork, etc.. built by us") e dalla loro parola per queste moto ("costruire special", post del 07/10/2023). Le tre legende fanno il resto: telaio e forcella di Overdrive Customs, motore e ruote da una Suzuki DR650, sella di Cisco Leather. Con il nome di un'altra officina la pagina non regge: la moto, le legende, il titolo e la chiusura sono loro.

Direzione A del prototipo ("La moto sul bianco"), scelta dal giudice; dalla B restano solo la voce (la frase dei mostri, l'H2 "Dal tagliando alla moto da concorso") e la foto vera dell'officina, ora in chiusura.

### Le prime due schermate
- **1440x900**: testata con il logo vero (SVG), menu (Officina, Le moto, Riviste, Dove siamo) e il telefono. Titolo su una riga a 100 px. Sotto, a destra, Hagane scontornata (immagine 867 px compresa l'ombra) con le tre legende in una fila sola, sulla stessa linea di base, e i fili verticali che scendono sui pezzi. A sinistra tre righe su chi sono, il bottone rosso "Chiama 340 251 0434", "Su appuntamento, da martedì a venerdì"; la didascalia di Hagane chiude all'altezza delle gomme.
- **Seconda schermata**: "Dal tagliando alla moto da concorso", la data di apertura (2 maggio 2015), due elenchi brevi (In officina, Su progetto); poi "Le moto premiate".
- **1024 e 768**: la pagina passa alla disposizione del telefono già a 1180 px: titolo, moto larga quanto il contenuto (920 px a 1024), i numeri sui pezzi con l'elenco sotto, poi testo e bottone.
- **390x844**: titolo su due righe a 50 px, Hagane a tutta larghezza con i numeri sui pezzi, l'elenco delle legende subito sotto, poi testo e bottone. Testata con logo, telefono e bottone "Menu".
- Pagina: 5092 px a 1440 (piede compreso), 5595 px a 390.

### Come è fatto lo scontorno
Script `_prova/script/finale_taglio.py`, solo pixel della foto originale (Instagram, 1080 px), niente generato:
- gomme e cerchi come ellissi vettoriali misurate sulla foto (`fit_ruote.py`), con sfumatura di 1 px;
- ruota davanti: ogni raggio è trovato sulla foto tra la flangia del mozzo e il cerchio, assestato al decimo di pixel e reso come linea piena e continua, del rosso bruno misurato sui raggi veri (prima erano puntinati);
- ruota dietro: disco, corona e catena tenuti per colore; i fori dell'erba hanno ora bordi tondi e puliti;
- gomme: il riflesso grigio sul fianco destro della gomma dietro è abbassato al tono della gomma; nella parte bassa delle due gomme, dove passava l'erba, il colore resta scuro e neutro; i puntini scuri sui cerchi rossi sono chiusi col rosso vicino;
- telaio: il tubo verticale dietro il motore, bucato dalla catena, è chiuso con i bordi misurati sulla foto;
- bordo del corpo levigato a doppia misura, colori del bordo presi dall'interno; bordo alto del serbatoio come curva liscia; tono: rosso meno saturo, neri più profondi, HDR attenuato; ombre morbide di contatto.
È ancora una foto da 1080 px: a 867 px regge, da vicino si vede il limite del file. La strada vera è nel LEGGIMI (originale del fotografo o scatto in studio).

### Caratteri e colori
- **Archivo** (Omnibus-Type, Google Fonts), un solo file variabile con gli assi di peso e larghezza, servito da `sito/fonts/` (woff2 latin e latin-ext). Licenza **SIL Open Font License 1.1** (`sito/fonts/OFL-Archivo.txt`): uso commerciale libero, si può incorporare e ridistribuire con il sito. Titoli a larghezza 106 % in peso 500, spaziatura da -0,03 a -0,035em; testo 400 a 17-19 px, interlinea 1,55; etichette e bottoni 600; cifre tabellari per telefono, anni e orari. Niente monospazio, niente corsivo, nessun secondo carattere. Riferimento: il grottesco largo dei marchi del mondo custom (Revival Cycles, la scheda "THE RELOAD 650" di Roland Sands) e i caratteri piccoli e ordinati di Auto Fabrica; il corsivo resta solo nel logo.
- **Colori**: bianco calce `#F3F1EC` (fondo), inchiostro `#151515`, grigio delle note `#5F6267` (5,4:1 sul calce), un solo accento rosso officina `#B3261E` sul bottone, sul punto della moto scelta e sul fuoco da tastiera; piede `#151515` con testo `#ECE9E2` e note `#AEABA4` (8:1), segnaposto della newsletter `#9C998F` (6,4:1), filo del campo `#8A8780` (5,1:1); bianco sul rosso del bottone 6,5:1. Tutto sopra AA.

### Interazione
Un gesto solo, in "Le moto premiate": quattro schede (Envy 2019, Drakkar 2021, Special K 2022, 883 Old Style 2023) cambiano la foto e il testo del premio con un cambio netto, senza dissolvenza. Si apre su Special K (foto in studio, chiara come l'apertura; la Envy è già nella foto della chiusura). Tablist vero: clic, dito, frecce, Home e Fine; con Tab si entra solo nella scheda attiva; il testo del premio è annunciato agli screen reader; il fuoco si vede (bordo rosso). I nomi delle moto nel piede aprono la scheda giusta.
Sotto i 900 px la testata ha un bottone "Menu" vero (`aria-expanded`, `aria-controls`): apre i quattro link a 66 px d'altezza l'uno, si chiude con un tocco su un link, con "Chiudi" o con Esc (il fuoco torna sul bottone). Le transizioni (0,15 s) sono solo cambi di colore su ciò che si tocca: nessuna animazione allo scorrere, nessun effetto sul cursore, nessun elemento che sbiadisce.

### Foto: origine e licenza
Solo foto dell'azienda, dal sito e dal profilo Instagram @overdrive_customs (`assets/originali/`, voti in `_prova/inventario-immagini.json`). Nessun segnaposto di repertorio, nessuna foto nuova scaricata, nessuna immagine generata dall'IA. Lavorate con PIL e OpenCV ed esportate in WebP a più larghezze con `srcset`, mai oltre la misura del file (tranne l'apertura, a doppia misura levigata dallo scontorno).
- Apertura: Hagane nel campo, `feed/20240522_C7QjkJVIRt0.jpg` (post del 22/05/2024, autore non indicato), scontornata.
- Selettore, riquadro fisso 3:2 largo al massimo 720 px. Envy `feed/20181121_BqcLrvEgKvp.jpg` e Drakkar `feed/20210816_CSo4M02INbn.jpg`, tutte e due di fianco davanti alla stessa lamiera grigia, con l'HDR attenuato e un filo più chiare; la Drakkar era 1080x617, la lamiera sopra il manubrio è allungata di 103 px specchiando e allungando le sue prime 50 righe (la moto non è toccata). Special K `feed/20230828_Cwfiz3-oi3b.jpg` e 883 Old Style con Matteo `feed/20231202_C0Wverwo_GZ.jpg` (foto @boemphoto), servizio in studio su fondo bianco, a 720 e 704 px.
- Copertine: Kustom World agosto 2024 (`feed/20240819_C-20QVBoqJR.jpg`) e Bigtwin aprile 2025 (`feed/20250327_DHsQHfYN4bp.jpg`).
- Chiusura: la copertina del sito di oggi, `copertina-sito-original.jpg` (2560x1440, Matteo in officina con la Envy e una Sportster, autore da chiedere), a tutta larghezza in 16:10, a 1440 mostrata a 1440 px CSS.
- Ogni moto compare una volta sola, tranne Hagane (apertura e le due copertine, che sono la prova) e la Envy (selettore e foto dell'officina, lontane).
- Licenza: sono foto dell'azienda e di fotografi terzi; le copertine sono delle riviste. Prima di pubblicare servono i permessi (vedi LEGGIMI).

### Chiusura e piede
- Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto: a sinistra la frase loro, "I mostri non sono nella vostra testa: li creo io" (post del 07/10/2023, "I mostri non sono nella vostra testa.... Li creo io!", punteggiatura adattata), e sotto "Sempre tanta voglia di fare e costruire special." (stesso post); a destra i recapiti: numero grande con `tel:`, WhatsApp, indirizzo con il link a Google Maps, orari e "Solo su appuntamento", email con `mailto:`. Sotto, la foto dell'officina con una didascalia.
- Piede: logo SVG ricostruito (fedele) con una riga su chi sono; colonne Officina, Le moto, Contatti, tutte della stessa misura; newsletter "Fiere e moto nuove" con email, bottone e consenso privacy, perché l'officina ha fiere fisse ogni anno, moto nuove presentate lì e clienti privati; sotto, "Seguici" con il solo Instagram (Facebook tolto finché non è confermato). Non invia nulla finché non si collega a un servizio (LEGGIMI). Ultima riga: nome, indirizzo, Privacy (`/privacy`), Cookie (`/cookie`); ragione sociale, P.IVA e REA non sono pubblici e vanno aggiunti appena Matteo li dà. A 768 le tre colonne in fila e la newsletter sotto; a 390 Officina e Le moto in due colonne, poi Contatti, poi la newsletter.

### Rifinitura dopo il giudizio cieco (ultimo passaggio)
Giudizio: K0 7, K6 6, non passava. Difetti, uno per uno:
1. **Titolo** (bloccante): "Il telaio lo facciamo noi" ricalcava la formula di Recinzioni Formentin. Ora "Special, dal telaio in su"; "facciamo noi" non c'è più in pagina.
2. **Scontorno** (bloccante): raggi davanti come linee piene, riflesso della gomma dietro abbassato, tubo del telaio chiuso (già avviati nel passaggio interrotto, verificati e tenuti); in più fori della ruota dietro puliti, parte bassa delle gomme ripulita, puntini sui cerchi chiusi. Resta il limite del file da 1080 px.
3. **Foto della chiusura** (importante): via la foto da 640 px; ora la copertina del sito da 2560 px a tutta larghezza.
4. **Envy doppia e fascia dell'officina** (importante): la fascia dopo "Dal tagliando alla moto da concorso" è tolta (la foto è andata in chiusura); il selettore si apre su Special K.
5. **Menu sotto i 900 px** (importante): bottone "Menu" con `aria-expanded` e `aria-controls`, provato con tocco, Invio, Tab ed Esc a 390 e 768.
6. **Foto del selettore disomogenee** (importante): la Drakkar nel negozio con le insegne è sostituita da una foto di fianco davanti alla lamiera; Envy e Drakkar con HDR attenuato. Ora due coppie coerenti (lamiera, studio); il servizio unico da rifare è nel LEGGIMI.
7. **Legende** (minore): tre legende con un fatto ciascuna (chi ha fatto il pezzo), nessuna ripete il titolo.
8. **La Morelia** (minore): tolta dai primi posti (resta da confermare nel LEGGIMI).
9. **Didascalia di Hagane** (minore): "Prima nella categoria Metric al Biker Fest di Lignano".
10. **1024** (minore): da 901 a 1180 px la disposizione impilata, moto a 920 px.
11. **Piede** (minore): Facebook tolto, Seguici sotto la newsletter, colonne della stessa altezza, Privacy e Cookie su `/privacy` e `/cookie`.
12. **"Le moto premiate"** (minore): titolo a sinistra e testo a destra sulla stessa riga, foto e schede che partono alla stessa altezza; niente più vuoto sopra la lista.
Per la soglia delle foto (paragrafo f) le copertine sono un po' più grandi (8 colonne) e la foto della chiusura è in 16:10: area coperta da foto 36 %.

### Controlli
- `_metodo/kit/segnali.sh` sulla pagina finale: 0 soglie bloccanti su 10, 0 da guardare su 8. Foto 36 % dell'area, Archivo 100 %, monospazio 0 %, 2 filetti, 0 frecce, 0 titoli col punto, 3 misure di H2, 2 fasce di fondo, date presenti.
- `_prova/script/finale_prove.mjs` (dentro `build_finale.sh`): larghezza del documento uguale alla finestra a 320, 360, 390, 414, 560, 600, 768, 900, 901, 1024, 1180, 1181, 1280, 1366, 1440, 1680, 1920 e 2560; selettore provato con frecce, Home, Fine e Tab, e con il tocco a 390; menu provato con tocco, Invio, Tab ed Esc; i nomi del piede aprono la scheda giusta; nessuna ancora rotta.
- Collegamenti: `tel:+393402510434`, `https://wa.me/393402510434`, `mailto:overdrivecustoms@live.com`, Google Maps su "Via San Francesco 8/a 30030 Vigonovo VE", Instagram.
- Risoluzione: a DPR 1 nessuna immagine è mostrata oltre la sua misura. A DPR 2 e 3 restano morbide le foto del selettore (file da 720 px) e un poco le copertine e la foto della chiusura a 1440x2 (2880 px chiesti, 2560 nel file): servono gli originali (LEGGIMI).
- Screenshot guardati a pezzi a 1440 e 390, più le prime schermate a 320, 768, 1024 e 1920 e il menu aperto a 390.
- Nessun U+2014 nella pagina, in questa nota e nel LEGGIMI; nessun segnaposto in pagina; nessun dato senza fonte in `01-analisi.md`.
- Divieti: niente gradienti viola, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, badge, tre box con icona, Lucide, shadcn, dissolvenze, effetti sul cursore, bottoni che sbiadiscono, lineette lunghe, parole da brochure, corsivi d'accento.
