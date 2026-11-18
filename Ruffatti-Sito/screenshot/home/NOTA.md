# Fratelli Ruffatti, home

## Metodo ibrido (novembre 2026)

Richiesta: il committente ha scelto il metodo ibrido dopo la prova della sezione D (giudice da agenzia a 7, clienti tipo giù di mezzo punto o un punto; nel secondo giro la commissione estera a 6,5 con 1 compito su 4). Prima schermata secondo la sezione D, tenuta com'era; sotto, i contenuti e le funzioni della versione professionale (`_prova/versione-pro/sito/index.html`) che i clienti tipo usavano, rimessi su una griglia sola. Direzione in `_prova/alto/DIREZIONE.md` (riscritta: la cartella `_prova/alto/` era sparita con il riavvio). La pagina della prova, prima di questo giro, è copiata in `_prova/alto/prima/index-alto.html`.

### Ritocco dopo il giudice da agenzia (3/11/2026, metodo ibrido, voto 7)

Il giudice ha dato 7 a questa versione: quadrante vuoto nella prima schermata, culmine diluito, foto con trattamenti diversi, targhetta tagliata male, pagina troppo lunga, due attacchi della colonna destra. La pagina prima del ritocco è in `_prova/alto/ibrido2/index-prima.html`, le immagini di prima in `_prova/alto/ibrido2/vecchie-img/`. La prima schermata resta secondo la sezione D: stessa testata, stesso logotipo, stessa riga dell'`h1`. Le misure dicono sempre 6 cliccabili e 1 bottone.

**Che cosa è cambiato**
- **Prima schermata, colonna destra**: il quadrante vuoto di 515x278 non c'è più. A x 736, alla stessa altezza della foto (y 670), c'è il titolo della sezione "Organi nuovi" (20/30 con il filetto, come "Dicono di noi" e "Video e CD"). Sotto c'è la loro frase "Da Padova abbiamo raggiunto negli anni tutti i continenti." a 32/40, in due righe bilanciate. È solo testo: i caratteri fuori dalla testata passano da 57 a 127 (tetto 160) e i cliccabili restano 6. Sotto la frase restano 85 px di carta.
- **Uppsala sta da sola alle colonne 1-6**: 624x693, dallo stesso file da 900 px (densità 1,44 a DPR 1), con lo spazio sopra la sezione portato da 80 a 48 px. Nella prima schermata se ne vede l'11,1% (prima l'11,2%) e la striscia arriva alle punte delle torri. Nella colonna destra, in basso e allineate al bordo della foto, ci sono la frase dei Paesi del ventunesimo secolo e la didascalia "Cattedrale di Uppsala, Svezia / 2009 · quattro manuali · trasmissione elettrica · la disposizione fonica, PDF". Il blocco del culmine misura 901 px, dall'inizio della sezione alla serie, e ha una foto sola. Dopo il culmine c'è una pausa di 160 px.
- **La serie è di quattro organi** in 4:5, a colonne di 3 (296x370): Wayne 2022, con un nuovo ritaglio 4:5 di 497x621 da `2022_10_cantoriajpg.jpg` senza la striscia bianca, poi New Orleans 2022, Buckfast 2017 e Boteå 2015. New Orleans ha "due manuali" e "la notizia" nella didascalia, così la riga dell'indice che la ripeteva è stata tolta. Sotto la serie ci sono Pershore Abbey 2023 (indice con la fonte, colonne 1-6) e "Le 86 opere significative" (colonne 7-12). Sono spariti il titolo "Organi nuovi, gli ultimi" e il blocco "manifesto" con l'h3 dei continenti, che aveva le basi sfalsate.
- **Una curva sola per le foto** (`_prova/alto/script/ibrido_img.py`, riscritto e ora completo, con i ritagli ritrovati da `trova_ritagli.py`). Tutte le foto a colori sono state rifatte dagli originali. Saturazione media HSV su 100x100 a 0,31 (prima andava da 0,31 a 0,53). Fa eccezione New Orleans, cassa bianca e oro, portata da 0,20 a 0,25. Dominante R-B tra 23,8 e 27 (prima da 17 a 44). Lo scarto massimo di saturazione è 0,06, sotto il limite di 0,08. L'archivio in bianco e nero non è cambiato. Confronto: `_prova/alto/ibrido2/foto-prima-dopo.jpg`.
- **La targhetta** è stata ritagliata di nuovo dal file intero `2016_04_xP1050195.jpg`: 762x508 in 3:2, da x 10 e y 125. La targhetta sta nel terzo basso, con 45 px di legno sotto, e Bordone dolce è intero: nessuna manopola è più tagliata sul bordo destro. Larghezze 358, 624 e 762. La didascalia ora è a una voce sola e nomina i registri che si vedono interi: Principal 16', Contra Principal 32', Contra Subbasso 32' e Bordone dolce 16'. Le finestre provate sono in `_prova/alto/ibrido2/targhetta-finestre.jpg`. Il giudice proponeva la finestra da y 100, che però taglia a metà Open Wood e Contre Violone. Con la finestra da y 125 si vedono solo i loro gambi e il fondo del pomello.
- **Didascalie a due voci solo sui lavori** (D10): falegnameria, targhetta e archivio hanno ora una frase sola, in grigio.
- **Pagina più corta**:
  - via la riga di Pipedreams (il link ai CD resta);
  - il concorso è il titolo più una frase ("per giovani organisti sotto i 30 anni. Finale il 5 febbraio 2027 sull'organo Ruffatti della chiesa; premi di US$ 5.000, 2.500 e 1.500"), con il bando, la pagina e Instagram in fila; via la tabella;
  - "Writing from abroad" è una frase a 17/25 con il telefono;
  - la famiglia è una frase, con il link;
  - "Per un restauro..." diventa "Un restauro, o un organo Ruffatti già in chiesa ↑";
  - due accorciamenti di frasi loro ("una canna per una"; via "con località, anno e autore dell'organo");
  - spazio delle sezioni da 96 a 80 px, con la pausa del culmine al doppio (160).
  
  Risultato: da 827 a 699 parole e da 6.951 a 6.256 px a 1440; 10.153 px a 390.
- **Un solo attacco della colonna destra**: x 736 (colonne 7-12) per tutti i blocchi. "Video e CD" passa da 845 a 736. Bordi sinistri in pagina: 80 e 736, più la targhetta centrata del restauro, che è il gesto e resta in asse come l'apertura.
- **Dettagli**:
  - via il doppio filetto sotto "Video e CD";
  - i filetti delle tre strade del contatto sono ora color filetto rgb(217,205,182) a 2 px invece del quasi nero (`giudice/bordi.mjs`: sulla carta due colori, filetto e link);
  - `text-wrap: balance` su titoli, frase del culmine e didascalia della targhetta: "laboratorio" non va più a capo da solo;
  - a 390 la riga legale del piede è in colonna, con Cookie a 44 px di tocco.

**Misure finali** (`_prova/alto/misura-d.mjs`, esteso con l'obiettivo del giudice, il blocco del culmine e gli attacchi; uscita in `misura-d.txt`): 49 passano, 0 no.
- D2 11,1%; D3 6 cliccabili, 1 bottone, 127 caratteri; a 390 4 cliccabili, 1 bottone, foto 56,5%.
- 699 parole e 6.256 px (obiettivo del giudice: 700 e 6.300); 6 sezioni; culmine 901 px con 1 foto; 8 foto, 3 formati (0,90, 0,80, 1,50); 0 ingrandite; 4 bottoni.
- Peso 1.547 KB.
- La D8 com'è scritta (650 parole, 6.000 px) ancora non passa: lo script la riporta come INFO.

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`controllo.txt`): nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore, nessuna area di tocco sotto i 44 px sotto i 900. Il testo è identico senza JavaScript (4.670 caratteri in tutti e due i casi). Screenshot rifatti in questa cartella con gli stessi nomi.

**Dove stanno i compiti**
- **V1, commissione**: tre strumenti recenti con luogo, anno, manuali e fonte, entro due schermate a 1440 (serie a y 1523-1893, Pershore a y 2077). Uppsala intera nella seconda schermata.
- **V2, parrocchia**: invariato (testata "Chiama", "Restauro di organi antichi →", lista e due strade).
- **V3, organista**: nel concorso restano età, finale, premi, bando e Instagram. Non c'è più l'edizione 2024 (Dawon Lee), che resta sulla pagina del concorso.

**Problemi aperti**
- Le foto restano il limite: il giudice ci mette il 60% della distanza dall'8,5. Serve il servizio fotografico (LEGGIMI).
- Nel culmine, tra la frase in alto e il testo in basso, la colonna destra lascia circa 400 px di carta accanto a Uppsala. È voluto, come la didascalia di Rieger, ma va guardato con il giudice.
- La foto di New Orleans resta fuori dall'intervallo 0,30-0,36, perché una cassa bianca più satura diventa gialla.
- I voti dei clienti tipo e del giudice vanno rifatti su questa versione.

### Che cosa è cambiato

- **Prima schermata**: identica (logotipo d'ottone sul mogano, riga dell'`h1`, "Padova, dal 1940", testata con 6 cliccabili e il solo bottone "Scriveteci", a 390 Menu, EN, "Chiama" e "Restauro di organi antichi →"). Unica differenza: Uppsala è ora larga 733 invece di 624, quindi il bordo che sale sotto il mogano pesa l'11,2% della schermata invece dell'8,5%.
- **Seconda schermata a 1440 (y 900-1800)**: Uppsala a colonne 1-7 (733x815 dal file da 900, l'organo intero sta in una finestra sotto la testata), con la didascalia "Cattedrale di Uppsala, Svezia / 2009 · quattro manuali · trasmissione elettrica · la disposizione fonica, PDF". A colonne 8-12, nella stessa fila e sotto la piega (parte a y 921): **l'organo recente con la foto**, Santa Caterina da Siena a Wayne, 2022 (`2022_10_cantoriajpg.jpg`, "La parte principale dello strumento, in cantoria" nella loro notizia del 13/10/2022), "tre manuali e 37 registri, due consolle · la notizia"; poi "Organi nuovi, gli ultimi" con Pershore Abbey 2023 (tre manuali e 33 registri, secondo l'abbazia, link all'abbazia) e Notre Dame Seminary 2022 (due manuali, il Grand'Organo in due sezioni, link alla notizia); sotto, "Le 86 opere significative". Poi la frase loro "Da Padova abbiamo raggiunto negli anni tutti i continenti" con i Paesi del ventunesimo secolo, e la serie di tre organi in 4:5 (New Orleans con "in copertina su The Diapason, ottobre 2022", Buckfast 2017, Boteå).
- **Tornano dalla versione professionale**: le tre testimonianze con nome, ruolo e istituzione (Joyce Jones, Diane Bish, Frederick Swann) accanto a "Video e CD" (Making 32' Reeds in laboratorio, il restauro di La Valletta, i CD, il canale, e Pipedreams in una riga); la lista "che cosa preparare" del restauro come elenco numerato, con "Organo muto, sporco o da revisionare?"; il **Concorso di Miami** come sezione (`#concorso`, dal menu) con le condizioni in quattro righe di testo, nessuna cifra grande: finale a Miami il 5 febbraio 2027 sull'organo Ruffatti della Church of the Epiphany, undicesima edizione (dal bando 2027 in PDF del loro sito); premi US$ 5.000, 2.500 e 1.500; il decimo concorso del 2024 vinto da Dawon Lee; poi "Il bando 2027, PDF in inglese", la pagina e Instagram; nei contatti "Un organo nuovo: che cosa mandarci" in quattro punti con l'email composta.
- **Il contatto in inglese** (il compito fallito nel secondo giro): nei contatti c'è "Writing from abroad" (`lang="en"`, `#english`), con che cosa scrivere, "Phone +39 049 750 666", il bottone "Write to us in English" (oggetto e traccia in inglese con Institution e Position) e "Contact form, English site" verso `ruffatti.com/en/contact-us/`. "Scriveteci" in testata porta lì: a 1440 il blocco inglese e il suo bottone stanno nella finestra d'arrivo. Nel menu del telefono c'è la voce "Contact us in English".
- **Una griglia sola**: 12 colonne, margine 80, gronda 32 a 1440. Tutti i blocchi partono e finiscono su una colonna, un solo bordo destro (1360). Le citazioni minori usano una sotto-griglia di 6 colonne con la stessa gronda, così restano sui terzi. Verificato da `misura-d.mjs`.
- **Ordine al telefono**: nel restauro la strada "Avete un organo Ruffatti in chiesa?" viene subito dopo la targhetta (dal titolo al bottone 874 px), nei contatti il testo prima della foto d'archivio, nel concorso le condizioni prima dei collegamenti (dal titolo al bando 686 px). Aree di tocco di 44 px anche a 768 (prima solo sotto i 700).
- **Restano fuori** (capitolo 5 e diagnosi): la frase con le cifre del 2016, la fascia delle sei cifre, il modulo di dieci campi (bastano i mailto con la traccia, D12), le cifre grandi del concorso, il video "factory tour", la citazione di Michela, tre dei quattro riconoscimenti, Grand Rapids e Coral Ridge, gli ingressi descritti, "Iscrizione" (le domande si chiudevano il 19/6/2026).
- **Foto**: una nuova, Wayne, trattata con `_prova/alto/script/ibrido_img.py` (ritaglio 3:2 828x552, larghezze 358, 515, 672 e 828, stesso trattamento descritto per la serie). Gli originali usati sono stati riscaricati il 3/11/2026 dalla libreria media di ruffatti.com in `assets/originali/` (la cartella era vuota); provini in `_prova/alto/provini.jpg`. Le altre immagini di `sito/img/` sono quelle della prova: lo script che le aveva fatte (`alto_img.py`) è andato perso.

### Misure (`_prova/alto/misura-d.mjs`, uscita in `misura-d.txt`: 46 passano, 0 no)

- Prima schermata 1440x900: foto 11,2% (sotto il 12%), 6 cliccabili, 1 bottone, 57 caratteri fuori dalla testata (56 nella testata), nessuna fila di ingressi, nessuna cifra grande, 0 occhielli, `h1` di 8 parole e 0 virgole. 390x844: 4 cliccabili, 1 bottone (la chiamata), foto 56,5%.
- Pagina: 827 parole a 1440 e 831 a 390 (tetto 900; la prova ne aveva 603), 6 sezioni dopo l'apertura (organi, video e CD, laboratorio, restauro, concorso, contatti), 6.951 px a 1440 (tetto 7.500; la prova 5.962), 10.785 a 390. Una famiglia (EB Garamond), nessun testo oltre i 100 px, testo corrente minimo 17 px. 0 cifre di 30 px o più. 8 foto, 3 formati (0,90, 4:5, 3:2), nessuna ingrandita a 1440 e a 390; la più grande è Uppsala (733x815). Fondi: carta, mogano (solo apertura e testata) e pietra (restauro); spazi 80/144 al culmine e 96 altrove. Il numero di telefono compare 2 volte in `main`, nessun collegamento identico più di 2 volte; 4 bottoni in pagina; 3 `tel:`, 4 `mailto:` tutti con oggetto, 0 "Indicazioni", 0 video, lista nera 0, U+2014 0, "indicativ" 0. Peso: 1.716 KB contando tutte le larghezze di tutte le immagini (a 1440 se ne scarica circa la metà).
- Controlli (`_prova/alto/controllo.mjs`, uscita in `controllo.txt`) a 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessuna sovrapposizione, niente fuori dalla finestra, nessun errore di script, `tel:+39049750666` in tutti e tre i link, il telefono della testata cliccabile a metà pagina, il menu (12 voci) si chiude dopo il tocco e porta il titolo del concorso a 129 px, nessuna area di tocco sotto i 44 px sotto i 900.

### I compiti della scheda d'uso, dove stanno ora

- **V1 commissione, 1440**: (1) mestiere, "costruttori e restauratori" e "Padova, dal 1940" nella prima vista; Uppsala intera con un colpo di rotella. (2) Entro due schermate tre strumenti recenti con luogo, anno, manuali e fonte: Wayne 2022 con la foto, Pershore 2023, New Orleans 2022, e "86 opere significative". (3) "Video e CD" in testata porta a testimonianze, video e CD. (4) EN, +39 049 750 666 e "Scriveteci" in testata; nei contatti che cosa mandare, l'email composta in italiano e quella in inglese, la pagina inglese dei contatti.
- **V2 parrocchia, 390**: "Chiama 049 750 666" in testata fissa; "Restauro di organi antichi →" nella prima vista e nel menu; nel restauro i costruttori antichi, i circa 120 restauri, la targhetta in foto, la lista, "Chiamate 049 750 666" e "Scrivete con le foto".
- **V3 organista, 390**: Menu, "Concorso d'organo di Miami", e la sezione con finale, premi, edizione 2024 e bando in una schermata; Menu, "Video e CD"; Instagram accanto al concorso; i social nel piede.
- Confronto: `_prova/alto/confronto.jpg` (Rieger prima e seconda schermata, Flentrop, la nostra prima e seconda schermata; catture dei concorrenti in `_prova/alto/concorrenti/`). La seconda schermata ora somiglia a quella di Rieger (carta avorio, filetti, una foto grande con il luogo); Rieger resta più forte in apertura perché ha una foto da servizio fotografico.

### Problemi aperti

- **Nessuna prova dei clienti tipo e del giudice su questa versione**: le misure passano, ma i voti vanno rifatti.
- **La foto d'apertura resta al limite**: 11,2% contro il tetto del 12%. Se si allarga ancora Uppsala, o si alza la piega, la D2 non passa.
- **A 1024** sotto il mogano salgono sia Uppsala sia la cima di Wayne (la D2 si misura a 1440).
- **Foto piccole**: Uppsala 900 px mostrata a 733 (densità 1,23, morbida su retina), Wayne 828 a 515. Per l'8 servono gli originali o un servizio fotografico (LEGGIMI).
- **Il concorso**: la pagina italiana dice "biennale", il bando 2027 "triennial"; in pagina non c'è nessuno dei due. Le domande per il 2027 sono chiuse dal 19/6/2026: il link si chiama "Il bando 2027".
- **Persona e orario nelle strade del contatto**: non sono nelle fonti (LEGGIMI 6). "Writing from abroad" non promette risposte in inglese.
- **La home inglese** non c'è: EN porta al sito inglese di oggi.
- **Il registro dei caratteri**: la riga aggiunta in coda a `_metodo/professionale/alto/REGISTRO-CARATTERI.md` ha due refusi ("un immagine", un apice in più dopo `h1`): non l'ho corretta per non riscrivere un file che altri agenti scrivono in parallelo.
- **Testimonianze**: il permesso di usarle va chiesto (LEGGIMI 7).

---

## Alto livello, prova della sezione D (3/11/2026)

Richiesta: "non è ancora super professionale" (giudice da agenzia a 6). Regole: sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (cap. 4), che vince su A e C; direzione artistica in `_prova/alto/DIREZIONE.md` (modello N, il nome come immagine). La home di prima, intera e con i suoi screenshot, è in `_prova/versione-pro/`.

Pagina: `sito/index.html` riscritta da capo, statica, si apre con file:///. Dopo il secondo giro è alta 5.962 px a 1440, 5.762 a 1024, 7.881 a 768, 8.483 a 390 e 8.642 a 320. Peso 555 KB in 15 file. Screenshot in questa cartella, stessi nomi di prima: home-1440, home-1024, home-768, home-390, home-320 (pagine intere), le prime schermate a 1440, 1024, 768, 390 e 320, chiusura-1440.

### Secondo giro (3/11/2026, dopo il voto 7 del giudice e le prove dei clienti tipo)

Il giudice cieco dava 7 (obiettivo 7,5-8); i clienti tipo erano scesi rispetto alla versione di prima (parrocchia da 8,5 a 7,5). Copia della pagina e dello script delle immagini prima di questo giro: `_prova/alto/giro2/index-prima.html` e `giro2/alto_img-prima.py`; prove, viste e verifiche nuove in `_prova/alto/giro2/` (`compiti.mjs`, `viste.mjs`, `bordi.mjs`, `rapido.sh`).

**Per i clienti tipo** (rifatti a mano i compiti della scheda d'uso con `giro2/compiti.mjs`)
- **Testata al telefono**: Menu, EN e il bottone "Chiama 049 750 666" (sotto i 360 px solo il numero; `aria-label` "Chiama il numero 049 750 666"). "Restauro" esce dalla testata, come chiedeva il giudice, e passa nell'apertura come una riga sola sotto "Padova, dal 1940": "Restauro di organi antichi →" (201x44, porta il titolo della sezione a 128 px). Cliccabili a 390: 4 (Menu, EN, Chiama, Restauro), un bottone; la foto di Uppsala resta al 56,7% dello schermo. A 1440 il numero è "+39 049 750 666", per la commissione estera.
- **Menu** nell'ordine della testata e della scheda, con voci che nominano le cose: Organi nuovi, Restauro di organi antichi, Video e CD, Il laboratorio, Concorso d'organo di Miami, "Contatti: chiamate o scriveteci".
- **Restauro con la sua strada**: sotto il testo e i due collegamenti c'è "Avete un organo Ruffatti in chiesa?" con che cosa preparare per la prima telefonata (chiesa e comune, costruttore e anno, foto della consolle e della targhetta, "e che cosa non funziona", come nella versione di prima), il bottone "Chiamate 049 750 666" e "Scrivete con le foto". È spostata dai contatti, non copiata: nei contatti resta un rimando "Per un restauro, o un organo Ruffatti già in chiesa... ↑". A 390 dal titolo al bottone ci sono 922 px (prima 1.249).
- **Aree di tocco** a 390: tutte le frecce, i collegamenti delle didascalie, le righe "Video e CD" e il piede almeno 44 px (verificato: nessuna sotto).
- **Commissione a 1440**: nella prima vista sale sotto il mogano la parte alta dell'organo di Uppsala (rosone e punte delle torri, 198 px, 8,5% della schermata); con un colpo di rotella l'organo intero e la didascalia stanno in vista (foto da y 102 a 795). Nella didascalia c'è ora "La disposizione fonica, PDF ↗" (la loro scheda Uppsala.pdf, già collegata da Alcune opere significative): i registri li legge lì, senza un conteggio fatto da me. New Orleans torna con "In copertina su The Diapason, ottobre 2022" e il dettaglio della loro notizia (il Grand'Organo in due sezioni, aperta e in cassa espressiva). "Video e CD" porta a quattro collegamenti: le parole di Diane Bish e Frederick Swann (Dicono di noi), i CD, il video di laboratorio con l'etichetta onesta "In laboratorio: Making 32' Reeds" e il canale. Nei contatti, accanto a "Scrivete a organs@ruffatti.com", c'è "Write to us in English" (`lang="en"`, oggetto e traccia in inglese con "Institution" e "Position" del loro modulo).
- **Piede**: via "Indicazioni ↗"; l'indirizzo resta come testo.

**Sotto la piega** (le correzioni del giudice)
- **Una griglia sola**: 12 colonne, margine 80, gronda 32. I blocchi partono a x 80 o 736 (metà) e finiscono a 704 o 1360; la serie e il piede usano i terzi e i sesti della stessa griglia (517, 955, 1173), la targhetta le colonne 4-9 (408-1032). Verificato con `giro2/bordi.mjs`: nessun bordo fuori griglia, le foto del laboratorio e dei contatti finiscono a 1360 e 704, i filetti dei passi hanno una lunghezza sola (80-704). Il doppio filetto ai lati diventa un filetto solo per lato.
- **Il culmine**: Uppsala apre la seconda schermata a colonne 1-6, 624x693 (ritaglio 9:10 da rosone a base, file da 900: densità 1,44 su retina, come chiedeva il giudice), alta quanto lo schermo sotto la testata; a destra, in basso, il titolo a 48/56, il paragrafo e la didascalia "Cattedrale di Uppsala, Svezia / 2009 · quattro manuali · trasmissione elettrica" sopra un filetto. È la foto più grande della pagina; la serie sotto è di tre tessere da 405. Il blu delle casse e il ciano del rosone sono smorzati (saturazione del blu 0,62, colore 0,82): saturazione media del blu 21%, il 90% sotto il 41%. Al telefono resta il taglio 9:11 con la volta (`<picture>`).
- **Niente doppioni**: New Orleans e Wayne non sono più due volte. L'indice dei lavori senza foto ha Pershore Abbey 2023 e Santa Caterina da Siena, Wayne, 2022 (tre manuali e 37 registri, due consolle, il Positivo diviso ai lati dell'altare maggiore, dalla loro notizia); la serie ha solo interni: New Orleans, Buckfast, Boteå. La consolle di Wayne esce (prodotto in mezzo al reportage). "Dicono di noi" e "CD, DVD e video" escono dal piede, perché stanno già nella riga "Video e CD".
- **Un solo sistema di numerazione**: i numeri 1-4 restano solo sui passi del laboratorio; gli indici usano l'anno. Un'etichetta sola per le notizie, "La notizia", con ↗ per i siti esterni e → per ruffatti.com, in una colonna fissa di 120 px.
- **Didascalie vere e non ripetute**: la falegnameria (`2016_04_falegnami-21.jpg`, 1597 px, dalla loro pagina "L'interno di un organo Ruffatti") sostituisce la macro sfocata delle canne: "La falegnameria, nel laboratorio di Padova / un organo montato tra i banchi di lavoro", cioè quello che si vede. La targhetta è la variante più stretta della stessa foto (`xP1050195-1.jpg`), con i registri che si leggono davvero: "Principal 16', Contra Principal 32' e Contra Subbasso 32'".
- **Il gesto torna una volta più giù**: il restauro è l'unica sezione centrata come l'apertura, con il titolo e la targhetta d'ottone in asse ("La targhetta d'ottone sulla consolle, con il nome del logotipo"); sotto, il testo a sinistra e la strada a destra. Il logotipo torna poi solo come firma: nel piede e nella testata fissa.
- **Testata fissa col marchio**: quando il logotipo grande esce dallo schermo compare al centro della testata il logotipo piccolo (160x34, sfondo CSS, link all'inizio). Senza script resta nascosto; nella prima schermata non c'è, quindi i cliccabili a 1440 restano 6. Nessun altro elemento fisso: a 1440 la testata copre solo i suoi 88 px, e le ancore si fermano sotto (`scroll-padding-top`).
- **Laboratorio**: titolo, "dai somieri..." a 12 px sotto e i passi a sinistra, la falegnameria a destra. La famiglia (1940, Piero e Francesco, Michela) diventa la didascalia lunga della foto d'archivio, che passa nei contatti: chi c'è dietro sta accanto a come si scrive.
- **Contatti**: due strade con la stessa struttura (titolo, che cosa preparare, un bottone, un collegamento), "Un organo nuovo" qui e "Avete un organo Ruffatti in chiesa?" nel restauro. Il Concorso di Miami esce dai contatti e va nel piede (era già nel menu).
- **Logotipo**: la maschera si pulisce con il massimo a blocchi e non più con un pixel ogni quattro, così il puntino sopra la R sparisce (nel file a 2240 la riga 0 è ora la punta della F, x 312-335, e non c'è più nessun pixel isolato sopra le lettere); una sfocatura leggera con una curva stretta arrotonda la scaletta della maschera a 1 bit. Il file è ora 1120x237.
- **Scala**: cinque misure di testo a 1440 (16, 17, 20, 32, 48: testo e testata 20/30, dati, link e didascalie 17/24-25, piede legale 16/22); spazi 80 e 144 per il culmine, 96 per le altre sezioni.

**Misure D finali** (`_prova/alto/misura-d.txt`, tutte passano): D2 8,5% di foto nella prima schermata a 1440, 0 ingrandite; D3 a 1440 6 cliccabili, 1 bottone, 57 caratteri, 0 cifre grandi; a 390 4 cliccabili, 1 bottone, 56,7% di foto; D5 una famiglia, 1 elemento oltre 100 px, testo corrente minimo 17 px, cinque misure; D6 0 occhielli; D7 h1 8 parole e 0 virgole, lista nera 0, U+2014 0, frase-firma 2; D8 603 parole a 1440 e 601 a 390, 5 sezioni, 3 bottoni, 5.962 px, culmine 917 px; D9 0 cifre grandi; D10 7 foto, 3 formati (0,90, 0,80, 1,50); D11 3 fondi, 1 sezione di marchio, spazi 80, 96 e 144; D12 3 tel:, 4 mailto con oggetto, 0 "Indicazioni", 0 video, 555 KB. Controlli a 320, 390, 768, 1024, 1440 e 1920 (`controllo.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione, niente fuori dalla finestra, telefono raggiungibile a metà pagina, menu che si apre (11 voci) e si chiude al tocco, nessun errore di script.

**Non fatto, con il motivo**
- **La home gemella in inglese** (`sito/en/`): è un sito a parte, non un ritocco; EN porta ancora al sito inglese di oggi.
- **Grand Rapids e Coral Ridge**: restano fuori finché l'azienda non conferma anno e dati (LEGGIMI 4). Il dato più recente in home resta Pershore 2023.
- **Il numero dei registri di Uppsala**: la loro scheda elenca registri prestati e trasmessi (en chamade dal Solo, Bourdon dello Swell al pedale), quindi un conteggio sarebbe mio; c'è il collegamento alla scheda.
- **Persona e orario nelle strade del contatto**: non sono nelle fonti (LEGGIMI 2 e 6).

### Ritocco dopo il giudice da agenzia (3/11/2026, voto 7)

Il giudice ha dato 7 (prima 6): il D1 non passa perché a 1440 né la prima né la seconda schermata mostrano un organo. Le prove dei due clienti tipo, rilanciate sulla pagina di prima, davano tre compiti non riusciti: nessuna foto d'organo nella prima vista a 1440 (commissione), "Restauro" non in vista a 390 (parrocchia), e dopo il ritocco anche "Ascolta" tolto dalla testata. La copia della pagina di prima è in `_prova/alto/ritocco/index-prima.html`; prove, fogli e verifiche nuove in `_prova/alto/ritocco/`.

**Applicati**
- **Culmine (bloccante).** L'Uppsala ora è il ritaglio basso (rosone e cassa) anche a 1440: 900x1100 da `2016_02_home-ruffatti2.jpg`, mostrato a 720x880 centrato (file da 720 e 900 px, mai ingrandito). La figura apre la sezione con 64 px sopra; sotto, sullo stesso asse, la didascalia centrata "Cattedrale di Uppsala, Svezia / 2009 · quattro manuali · trasmissione elettrica", il titolo (ora 48/56, per dare scala alla pagina dopo il logotipo) e il paragrafo. Verifica (`ritocco/verifica.mjs`): a scrollY 812 l'organo intero (canne, rosone e base) sta nella finestra 1440x900 e ne occupa il 64% dell'altezza visibile; con un colpo di rotella (scrollY 900) è ancora tutto in vista.
- **Il bordo alto della foto nella prima schermata.** L'apertura a 1440 è alta 700 px (`--piega:112px`): sotto il mogano salgono 47 px della volta di Uppsala (1,7% della schermata, sotto il 12% di D2). La commissione ora trova una foto loro già nella prima vista, e la pagina dice che sotto c'è qualcosa. Così si guadagnano anche i 112 px per restare sotto i 6.000.
- **Riga dell'h1** da 40/48 a 48/56 a 1440 (40/48 a 1024, 22/28 a 390; a 320 va a capo come "Costruttori e restauratori / d'organi a canne"). Nella miniatura a 300 px ora si legge (`ritocco/riconoscibilita-A-dopo.jpg`).
- **Didascalia dell'apertura** a due voci, 17 px: "Il nome della targhetta d'ottone" / "Qui sotto: l'organo della cattedrale di Uppsala, 2009".
- **Una colonna destra sola** per i blocchi a due colonne: indice degli organi, archivio, foto delle canne e testo del restauro attaccano tutti a x 736 (colonna 7); la foto della targhetta occupa le colonne 1-6 (624 px dal file da 800), quindi tra foto e testo resta la gronda di 32 px. Restano gli attacchi a terzi (x 517 e 955) delle tre strade dei contatti e del piede: è l'altro passo della stessa griglia, non un quarto allineamento.
- **I passi come indice di testo**: quattro righe numerate con filetto (Il legname, Lastre per canne, Canne ad anima, Canne ad ancia, ognuna verso la sua pagina), a colonne 1-6; accanto una sola foto, la macro delle canne ad anima a 592 px, la sua misura. Le quattro foto da fermo-immagine escono: in home le foto passano da 11 a 8, la serie dei quattro organi resta l'unica fila. La riga 3 usa la loro pagina ("Il metallo è battuto a mano...", "tutte le canne, grandi e piccole, vengono singolarmente lucidate").
- **"Ascolta" non promette più un suono.** In testata a 1440 la voce diventa "Video e CD" (a 390 nel menu, dopo Restauro). Il blocco è la citazione da sola, «I Principali cantano.» a 32/40 con 128 px sopra, e sotto una riga "Video e CD" con i tre collegamenti (CD incisi su organi Ruffatti, Making 32' Reeds su YouTube, il canale).
- **Restauro a 390 in prima vista**: in testata, accanto a "Menu", c'è "Restauro" (a 320 EN passa nel menu per fare posto). A 390 i cliccabili sono 4, il tetto di D3; il bottone resta uno, la chiamata.
- **Minori**: la didascalia della targhetta ora si verifica dalla foto ("Targhetta d'ottone tra i registri / Contra Principal 32', Contra Subbasso 32', Principal 16', Bordone dolce 16'"), e la frase dell'apertura compare una volta sola; Pershore: "Tre manuali e 33 registri." e il link "Fonte: l'abbazia"; "Cattedrale di Uppsala" e "organo del coro" al posto di "Uppsala Cathedral" e "Quire"; didascalia del culmine centrata come il titolo.
- **Immagini**: `_prova/alto/script/alto_img.py` aggiornato (uppsala-basso a 390, 720, 780 e 900; anima a 358 e 592; archivio anche a 592). Escono uppsala-540/900, legname, lastre, ancia e anima-296.

**Respinti, con il motivo**
- **L'ancora a #uppsala nella didascalia dell'apertura.** Con "Video e CD" in testata i cliccabili a 1440 sarebbero 7 (tetto 6). Ho tenuto la voce di testata, che serve il compito 3 della commissione, e la didascalia senza link; la foto che sale sotto la piega fa lo stesso lavoro.
- **Testata a 5 voci.** Sono 6 (Organi nuovi, Restauro, Video e CD, EN, numero, Scriveteci), dentro il tetto di D3: togliere "Video e CD" faceva fallire la prova della commissione ("Ascolta" in testata: 0).
- **La barra di mogano fissa** resta: la parrocchia deve avere il numero a un tocco anche a metà pagina (provato a 320, 390, 768 e 1024).
- **Rifare la prova "due persone su tre dicono organi"**: il foglio è rifatto, la prova con le persone non la posso fare io.

**Misure finali** (`_prova/alto/misura-d.txt`): tutte passano. D2 1,7% di foto nella prima schermata a 1440, 0 ingrandite; D3 a 1440 6 cliccabili, 1 bottone, 142 caratteri, 0 cifre grandi; a 390 4 cliccabili, 1 bottone, 56,7% di foto; D5 una famiglia, 1 elemento oltre 100 px, testo corrente minimo 17 px; D6 0 occhielli; D7 h1 8 parole, 0 virgole, lista nera 0, U+2014 0, frase-firma 2; D8 586 parole a 1440 e 568 a 390, 5 sezioni, 2 bottoni, 5.979 px, culmine 1.384 px; D9 0 cifre grandi; D10 8 foto, 3 formati (0,82, 0,80, 1,50); D11 3 fondi, 1 sezione di marchio, spazi 64, 80 e 128; D12 3 tel:, 3 mailto con oggetto, 1 "Indicazioni", 0 video, 602 KB. Controlli a 320, 390, 768, 1024, 1440 e 1920 (`controllo.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione, niente fuori dalla finestra, telefono raggiungibile a metà pagina, menu che si apre e si chiude, nessun errore.

**Clienti tipo dopo il ritocco** (`ritocco/prova-1/` e `ritocco/prova-2/`, le prove del giudice con la sola uscita spostata; nella prova 1 la voce si cerca come "Ascolta" o "Video"): commissione a 1440, una foto loro già nella prima vista (il bordo alto di Uppsala: è la volta, non ancora l'organo) e l'organo intero dopo un colpo di rotella, "Video e CD" in testata porta alla citazione e ai tre link, EN e Scriveteci in vista; parrocchia a 390, numero in testata, "Restauro" in vista senza scorrere, il menu porta a "Restauro filologico di organi antichi" a 486 px senza coprirlo, "Elenco dei restauri" e "Chiamate 049 750 666" nella sezione.

### Che cosa è cambiato

- **Apertura.** Il logotipo corsivo "Fratelli Ruffatti" in ottone #D4B06A a 1120x246 sul mogano #3E1406 (358x79 a 390), dentro l'`h1` con la loro riga "Costruttori e restauratori d'organi a canne" (40/48 a 1440: la direzione diceva 32, l'ho alzata come prevede il suo rischio 1, perché nella miniatura a 300 px a 32 px il mestiere non si leggeva). Sotto, "Padova, dal 1940" in maiuscoletto; in basso a sinistra la didascalia "Il nome della targhetta d'ottone / sulle consolle dei nostri organi". Ai due bordi le due coppie di filetti d'intarsio in CSS, che scendono per tutta la pagina. Niente foto nella prima schermata a 1440.
- **Testata**: Organi nuovi, Restauro, Ascolta, EN, il numero (testo a 1440, bottone bordato a 390) e un solo bottone, "Scriveteci". A 390 il menu è un `<details>`: funziona anche senza script.
- **Culmine (sezione 2, alta 1.488 px)**: "Da Padova abbiamo raggiunto negli anni tutti i continenti." e la riga sui Paesi del ventunesimo secolo, poi l'organo della Uppsala Cathedral (900x1600) a 540x960, con "Uppsala Cathedral, Svezia / 2009 · quattro manuali · trasmissione elettrica" (dalla loro scheda PDF). A 390 la foto viene prima del titolo ed entra nella prima schermata.
- **Organi nuovi**: la riga del mestiere e il link alle 86 opere significative; un indice di tre strumenti dal 2022 (Pershore Abbey 2023, con i dati "secondo Pershore Abbey" e il link alla loro pagina; Notre Dame Seminary e Santa Caterina da Siena 2022, con "La notizia"); la serie di quattro organi in 4:5 con la didascalia a due voci (New Orleans, Wayne, Buckfast 2017, Boteå contratto del 2015); la riga Ascolta con «I Principali cantano.» di Joyce Jones (Baylor University) e tre link.
- **Laboratorio**: "Costruiamo ogni componente possibile in laboratorio / dai somieri alle canne ad anima e ad ancia, fino ai particolari più minuti.", la famiglia con i nomi, la foto d'archivio, e quattro passi numerati in 3:2 con il nome tecnico (Il legname, Lastre per canne, Canne ad anima, Canne ad ancia), ognuno verso la sua pagina. Le righe vengono dalle pagine loro, scaricate il 3/11/2026 in `_prova/alto/fonti/` (API WordPress).
- **Restauro** (unico fondo pietra): la foto vera della targhetta, che chiude il gesto dell'apertura; "Restauro filologico di organi antichi" e la frase dei costruttori restaurati con l'elenco aggiornato al 2020; due link.
- **Scriveteci**: tre strade (Un organo nuovo con il mailto e la traccia; Un restauro o un organo Ruffatti in chiesa con "Chiamate 049 750 666" e "Scrivete con le foto"; Per gli organisti con il Concorso di Miami in una frase). Il modulo esce dalla home (D12): va nella pagina Contatti.
- **Piede** come biglietto da visita: logotipo, frase-firma, sede con "Indicazioni", telefono ed email, pagine, social, English e Русский, P.IVA, Maestro d'Arte e Mestiere 2020, Cookie.
- **Tolti**: la frase con le cifre del 2016, il secondo bottone dell'apertura, l'email e "che cosa mandarci" in apertura, i due ingressi descritti, la riga degli ultimi strumenti, la fascia di sei cifre, la fascia della citazione di Michela e la sua seconda citazione (permesso da chiedere), due delle tre testimonianze, quattro dei cinque video, la fila dei quattro riconoscimenti, le tre cifre grandi del concorso, il telefono a 64 px, il modulo di dieci campi, "Visite su appuntamento". Grand Rapids e Coral Ridge escono dalla home: le loro date non hanno una fonte certa (vedi sotto).
- **Carattere**: EB Garamond 400-500 (SIL OFL 1.1), una sola famiglia, in `sito/fonts/` con `OFL-EBGaramond.txt`. Escono Gambetta e Switzer. Nessun corsivo in pagina: il corsivo è solo il logotipo.
- **Foto**: 11 più il logotipo, tutte loro, in WebP, mai ingrandite, con lo stesso trattamento (`_prova/alto/script/alto_img.py`: colore 0,88, bianco a metà strada verso il neutro, curva calda leggera, luminosità verso 118; l'archivio in bianco e nero). Tre formati: 9:16, 4:5, 3:2.

### Esito delle regole D

Misure con `_prova/alto/misura-d.mjs` (esteso da `alto/diagnosi/misure/vp.mjs` e `misura.mjs`); uscita in `_prova/alto/misura-d.txt` e `misura-d.json`. Le misure "prima" vengono dalla diagnosi (`alto/diagnosi.md` e `diagnosi/misure/nostre-*.json`) e, dove serve, dallo stesso script lanciato sulla copia in `_prova/versione-pro/` (`misura-d-prima.txt`).

| Regola | Prima | Dopo | Esito |
|---|---|---|---|
| D1 idea e gesto | il logotipo sotto la piega | il logotipo d'ottone è l'apertura e torna con la foto della targhetta nel restauro | scritto in DIREZIONE; la prova con tre persone sulla miniatura non è fatta |
| D2 foto nella 1ª schermata a 1440 | 26% (New Orleans 519x649 dalla foto di 574) | 0%; Uppsala apre la seconda a 540x960 dalla foto di 900 | passa |
| D2 foto ingrandite | nessuna | 0 su 13 immagini a 1440 e a 390 (misurati i pixel veri del file scelto dal `srcset`) | passa |
| D3 cliccabili / bottoni a 1440 | 18 / 3 | 6 / 1 (Organi nuovi, Restauro, Ascolta, EN, il numero, Scriveteci) | passa |
| D3 caratteri fuori dal menu a 1440 | 731 | 122 (172 con la testata) | passa |
| D3 cifre di 30 px nella 1ª schermata | 0 | 0 | passa |
| D3 a 390: cliccabili / bottoni / foto | 9 / 4 / 19% | 3 / 1 (la chiamata) / 56,7% (Uppsala 390x477) | passa |
| D5 famiglie | Switzer e Gambetta | 1, EB Garamond (nessuna altra home la usa) | passa |
| D5 elementi oltre 100 px | 0 (il titolo a 64 px, il logotipo sotto la piega) | 1, il logotipo | passa |
| D5 testo corrente a 1440 | 14 px nelle note, 17 nel testo | 20 px il testo, 17 il minimo (didascalie 16, piede 16-17) | passa |
| D6 occhielli sopra h1 e h2 | 6 | 0 ("Padova, dal 1940" sta sotto l'`h1`) | passa |
| D7 h1 | 6 parole | 8 parole, 0 virgole: il logotipo (alt) e la riga | passa |
| D7 lista nera, lineetta lunga | 0, 0 | 0, 0 | passa |
| D7 frase-firma | 2 | 2: apertura e piede, crema su mogano sotto il logotipo | passa |
| D7 frasi d'istruzione sopra i 14 px | "Si apre il vostro programma di posta..." | nessuna | passa |
| D8 parole | 1.083 | 568 a 1440, 554 a 390 | passa |
| D8 sezioni dopo l'apertura | 8 | 5 | passa |
| D8 bottoni in pagina | 7 a 1440, 8 a 390 | 2 e 2 | passa |
| D8 altezza a 1440 | 9.200 px | 5.961 px | passa, con 39 px di margine |
| D8 culmine di almeno 900 px | nessuno | Uppsala, 1.488 px | passa |
| D9 cifre di 30 px o più in pagina | 10 (fascia dei numeri, concorso, telefono) | 0; tre numeri del concorso in una frase | passa |
| D9 lavori con nome, luogo e anno | in parte | tutti e 8 (Uppsala, i 3 dell'indice, i 4 della serie); Boteå con l'anno del contratto | passa |
| D10 foto, formati, "indicativ" | 10 foto, 4 formati | 11 foto, 3 formati (9:16, 4:5, 3:2), 0 | passa |
| D10 un trattamento, didascalia a due voci solo su apertura e lavori | 0,8 di colore | 0,88; due voci su apertura, Uppsala, 4 lavori e targhetta | passa (la targhetta ripete la didascalia dell'apertura) |
| D11 fondi oltre al piede | 4 | 3 (mogano, carta, pietra) | passa |
| D11 sezioni col colore del marchio | 3 fasce scure (apertura, numeri, contatti) e una bordeaux (Ascolta) | 1, l'apertura | passa |
| D11 spazi tra le sezioni | 96 ovunque | 80 e 128 (culmine), 1,6 volte | passa |
| D12 tel: / "Indicazioni" / telefono grande e modulo | 5 / 0 / sì e sì | 3 (testata, contatti, piede) / 1 (piede) / no e no | passa |
| D12 contatto per bisogno | modulo unico | 3 strade, ognuna con il suo contatto | passa in parte: manca la persona e l'orario, non sono nelle fonti |
| D12 peso, video, pop-up, testo senza JS | 844 KB, 0 | 498 KB, 0, nessuno, tutto il testo c'è anche senza script | passa |
| D4 modello per zona | | N, come da tabella del capitolo 5 | si controlla sull'ondata, non sulla singola home |

**Controlli a 320, 390, 768, 1024, 1440 e 1920** (`_prova/alto/controllo.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione di testo, nessun testo o immagine fuori dalla finestra, nessun errore di script; il telefono della testata fissa è cliccabile a metà pagina; il menu a 390 si apre (11 voci), si chiude al tocco e porta "Restauro" sotto la testata; il focus si vede (bordeaux su carta, ottone su mogano). Contrasti: crema su mogano 13,6:1, ottone su mogano 7,8:1, grigio caldo #5A4E44 su carta 7,0:1 e su pietra 6,3:1, bordeaux su carta 11:1. `tel:+39049750666` in tutti e tre i link; i tre `mailto:` hanno oggetto, e i due delle strade anche la traccia.

**Guardata accanto a Rieger, Flentrop, Robbe & Berking, Clayworks e al foglio dei 12** (`_prova/alto/giri/lontano.jpg`, `lontano-390.jpg`): da lontano a 1440 è il nome sul legno, come Knupfer con il nome a tutta larghezza; Rieger e Clayworks restano più forti perché hanno una foto da servizio fotografico. A 390 regge accanto a Rieger.

### Problemi aperti

- **Il mestiere a 1440** lo dicono la riga dell'h1 a 48 px e, dal secondo giro, la parte alta dell'organo di Uppsala che sale sotto il mogano: la prova D1 con tre persone sulla miniatura è ancora da fare.
- **Le foto sono piccole**: Uppsala 900 px (mostrata a 624), New Orleans 574, Buckfast 606, la targhetta 800. Per l'8 serve l'originale di Uppsala o un servizio fotografico di un organo recente (LEGGIMI).
- **Contatto senza persona e senza orario**: chi risponde e quando non è nelle fonti (LEGGIMI 6).
- **Pershore**: l'anno e i dati vengono dalla pagina di Pershore Abbey e sono scritti "secondo l'abbazia". Grand Rapids e Coral Ridge sono fuori dalla home finché l'azienda non dà anno e dati.
- **Il registro dei caratteri** (`_metodo/professionale/alto/REGISTRO-CARATTERI.md`) dice 32/40 per la riga dell'`h1`: in pagina è 48/56 a 1440 e 40/48 a 1024. Le misure a 1440 sono ora cinque (16, 17, 20, 32, 48).
- **L'altezza a 1440** passa per 38 px: se si aggiunge una riga, va tolta altrove.
- **EN** porta ancora al sito inglese di oggi; nei contatti c'è "Write to us in English".

---

## Storia: la versione "livello professionale"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh`. Alta 9200 px a 1440 e 13578 a 390, compreso il piede. Screenshot: home-1440, home-390, home-320, home-768, home-1024 (pagine intere), le prime schermate a 1440, 390 e 320, chiusura-1440.
La versione precedente ("Una canna", con la canna ad ancia smontata e il gioco Noce / Canaletto / Piede) è conservata com'era, con la sua nota, in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; poi "non rappresentano bene l'identità e l'utilizzo corretto"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Ordine seguito: uso, identità, alta gamma.
Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, e le pagine intere di barth e Budri a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Che cosa è cambiato rispetto alla versione 1

- **Via la canna smontata in apertura** e il gioco delle tre parti (la scheda d'uso le indica come cosa "da grafico": nessuno dei tre visitatori viene per un componente). Via le frasi di sintesi messe tra le loro ("Le nostre nascono in laboratorio, parte per parte", "Qui si fondono le lastre..."), le tre "misure" a metà pagina, il fondo grigio stagno #E7E8E2 e la bicromia dell'archivio, la newsletter con il modulo finto, "Apri la mappa" come invito in chiusura.
- **Apertura come la vuole la scheda.** A sinistra la loro riga "Costruttori e restauratori d'organi a canne" come titolo, l'occhiello "Padova, dal 1940", la loro frase sul primato americano ("Nell'esigente mercato statunitense abbiamo costruito oltre 50 strumenti..."), "Scriveteci" e "Chiamate 049 750 666", l'email, le due strade Organi nuovi e Restauro, e la riga "Ultimi strumenti: Grand Rapids 2026, Pershore 2023, Coral Ridge 2023". A destra l'organo del Notre Dame Seminary di New Orleans (2022) nella sua chiesa, alla misura d'origine, con didascalia di luogo, anno e manuali.
- **Struttura della famiglia M adattata.** Testata sobria con Contatti, lingue e telefono; dichiarazione di competenza con la foto; ultimi strumenti con committente, luogo, anno, manuali e registri (i progetti di barth); quattro schede dei mestieri con la foto (competenze e processi); i numeri aziendali in una fascia scura; testimonianze degli organisti con nome e istituzione e i video (Ascolta); il restauro con "Avete un organo Ruffatti?"; la famiglia con i riconoscimenti e la stampa in fascia; il concorso di Miami; i contatti con il modulo per il mestiere; il piede in quattro colonne.
- **Colori del marchio**: bordeaux del logo #6A0C10 (la scritta della targhetta sulla consolle), ottone #C29A5B delle trombe per le cifre sul fondo scuro, mogano scurissimo #1C1311 per i blocchi scuri e il testo, bianco delle chiese per il fondo. Grigi: #5A5552 (testo secondario, 7,4:1 sul bianco e 6,6:1 sul grigio chiaro), #B9B1AC (note sul mogano, 8,6:1); ottone sul mogano 7,0:1, bianco sul bordeaux 12,6:1, #E2DEDB (filetti), #F3F2F1 (blocchi chiari). Nessun beige.

### Ritocco finale (3/11/2026)

Dal controllo del livello professionale (voto 6,5) e dalle prove dei due clienti tipo (commissione americana a 1440, parroco a 390).

- **Menu a pannello riparato** (era il difetto bloccante): la riga flex ora vale solo per `.testata > .wrap`. Provato con `_prova/script/ritocco_prova.mjs` a 320, 390, 768 e 1024: sei voci in colonna alte 56 px, tutte toccabili, le lingue in fondo, filo d'ottone sotto il pannello; il tocco su "Restauro di organi antichi" chiude il menu e porta l'etichetta della sezione 31 px sotto la testata.
- **Gesto di scala e identità.** Testata e apertura su mogano, con il logo in ottone: è la scritta della targhetta d'ottone sulla consolle. L'organo bianco e oro di New Orleans stacca sul fondo scuro come il pezzo di Budri. In fondo all'apertura il logotipo corsivo a tutta larghezza (1280 px, ricavato dalla maschera a 5024 px della newsletter 2020, ripulito dai puntini della scansione) con la riga "La scritta della targhetta d'ottone sulle consolle dei nostri organi": il parroco riconosce il nome che legge sulla sua consolle. La didascalia dell'apertura è ridotta a luogo, anno e manuali.
- **Correzione di un dato.** La notizia "Nuovi organi in USA del 2022" dice che l'organo del Notre Dame Seminary è "a due manuali": la versione di prima scriveva tre. Ora c'è "Due manuali". Dalla stessa notizia il nome della chiesa di Wayne: Santa Caterina da Siena, con due consolle. Le due righe hanno il link "La notizia" alla pagina loro.
- **Foto in serie.** `pro_img.py` dà a tutte le foto a colori lo stesso trattamento: bilanciamento del bianco a metà strada verso il grigio medio, colore 0,8 (0,7 per le canne ad ancia, senza la dominante rossa), la stessa curva calda leggera, la luminosità media a metà strada verso 118. La consolle di Wayne è ritagliata più in basso e a destra (727 px): via le vetrate colorate e il soffitto.
- **Testi.** Restauro: "Restauro filologico di organi antichi, in Italia e all'estero" e "Restauriamo organi di ogni epoca e anche di altri costruttori, da Giovanni Guglielmi (Roma, Vallicella, 1612) a Gaetano Callido e Girolamo Zavarise..." (pagina Opere eseguite, aggiunta a `01-analisi.md`). Via "Da mezzo secolo", che non era datato. Nell'apertura i numeri hanno l'anno ("dati del 2016") e l'Italia viene prima degli Stati Uniti. Testimonianze con il ruolo della fonte ("già direttore della musica e organista", "già docente"). "Maestro d'Arte e Mestiere 2020" al singolare. "86 opere significative" al posto di "Tutte le realizzazioni: 86 strumenti". Nel riquadro del restauro "Organo muto, sporco o da revisionare?" (nessun servizio promesso). Citazione di Michela Ruffatti con il link a Rockit. Sotto l'email dell'apertura, a 1440, la riga su che cosa mandare con il link ai contatti.
- **Modulo.** In più "Idea di dimensione (manuali, registri, tempi del progetto)" e le caselle "Che cosa potete mandarci" (pianta della chiesa, foto della cantoria, foto della consolle e della targhetta), riportate nell'email come "Allego: ...". Il mailto del restauro dice "[Allegate qui le foto della consolle e della targhetta]".
- **Tipografia.** Pesi 400 e 600 (Switzer 600 al posto del 500). Tutti i titoletti (h3, i riconoscimenti, il riquadro della targhetta) in Switzer 600 a 22 px; Gambetta solo per h1, h2, cifre e citazioni. Il testo descrittivo passa da 16 a 17 px sopra i 640 px. L'anno dei riconoscimenti non va più a capo in grigio.
- **Ritmo.** Spazio tra le sezioni 96 px a 1440 e 64 a 390 (era 128 e 72); salti alle ancore senza il vuoto sopra l'etichetta. Piede: aree di tocco di 44 px, "La scheda" di Homo Faber su una riga sua, "Visite su appuntamento" sotto l'indirizzo.
- **EN** ha il titolo "Il sito inglese di oggi (current English site)": la home inglese non è fatta (vedi LEGGIMI).

### Le 15 regole, una per una (dopo il ritocco)

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), le prove del menu di `_prova/script/ritocco_prova.mjs`, e gli screenshot guardati a pezzi a 1440, 1024, 768, 390 e 320.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky di 89 px a 1440 e 73 a 390, bottone "049 750 666" alto 48 px bordato di bianco sul mogano. A metà pagina si vede e si tocca a 320, 390, 768 e 1024 (113x48 a 390). 5 link `tel:`; voce Contatti nel menu.
2. **Mestiere, luogo, prova, azione nella prima schermata: passa.** 1440x900: "Padova, dal 1940", H1, i numeri con l'anno, "Scriveteci" (pieno bianco) e "Chiamate 049 750 666", l'email con che cosa mandare, Organi nuovi e Restauro, gli ultimi strumenti, la foto con la didascalia. 390x844: "Chiamate 049 750 666" pieno a tutta larghezza, l'email, i due bottoni, gli ultimi strumenti, l'inizio della foto.
3. **Immagine vera nell'apertura: passa.** L'organo di New Orleans nella sua cappella, foto loro. Resta di 574 px: va chiesto l'originale.
4. **Zero repertorio: passa.** `grep -ci indicativ` dà 0 (il campo del modulo si chiama "Idea di dimensione" proprio per questo); nessun file di banche d'immagini; nessun disegno.
5. **Foto in serie: passa, con riserva.** 8 foto in 2 formati (4:5 e 4:3; il terzo formato contato dal controllo è il logotipo, che non è una foto), 2 didascalie, nessuna ingrandita, un solo trattamento. Restano scatti di anni diversi: la serie vera va fatta dal vero (LEGGIMI).
6. **Palette dal marchio: passa.** Bordeaux del logo #6A0C10, ottone #C29A5B (logo della testata, logotipo, cifre), mogano #1C1311, bianco; grigi #5A5552, #B9B1AC, #E2DEDB, #F3F2F1. Fondo del body bianco, nessun beige.
7. **Scala tipografica: passa.** 8 misure a 1440 (14, 17, 18, 22, 28, 44, 64, 96) e 8 a 390 (14, 16, 17, 20, 24, 30, 38, 48). Testo corrente 18 / 17, descrittivo 17; niente sotto i 14. H1 64 / 38, H2 44 / 30.
8. **Due famiglie con ruoli fissi: passa.** Gambetta 400 per h1, h2, cifre e citazioni; Switzer 400 e 600 per testo, titoletti e interfaccia.
9. **Servizi in schede con la foto: passa.** 4 schede 4:5 tutte cliccabili (2 colonne sotto i 1200 px).
10. **Tre tipi di prova: passa (4 su 4).** Testimonianze con nome, ruolo e istituzione; 6 numeri datati; riconoscimenti e stampa con didascalia; committenti con il nome.
11. **Lavori con un nome: passa.** 5 strumenti con committente, luogo, anno e dati; ora anche Wayne ha il nome della chiesa; foto della consolle larga 727 px (50,5 % di 1440). Mancano le foto di Grand Rapids, Pershore e Coral Ridge.
12. **Ritmo a blocchi: passa.** Su fondo pieno, oltre al piede: apertura (mogano), numeri (mogano), Ascolta (bordeaux), Contatti (mogano); Realizzazioni e Famiglia su #F3F2F1. Sezioni 96 px a 1440 e 64 a 390; margini 80 e 22.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 2 px, 56 px (48 in testata), testo 17 px (16 a 390); sul fondo scuro il pieno è bianco con il testo bordeaux. I bottoni di chiamata hanno il numero.
14. **Modulo e "dove" per il mestiere: passa.** Istituzione, ruolo, luogo, tipo di richiesta, organo di oggi, idea di dimensione, le caselle degli allegati (pianta, foto della cantoria, della consolle e della targhetta), messaggio; controllo dei campi obbligatori provato. "Vai alla mappa" nel piede, nessun iframe. Il file vero si allega quando il modulo sarà collegato a un servizio (LEGGIMI).
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, indirizzo con "Visite su appuntamento" (fonte Homo Faber, da confermare), mappa, telefono, email, pagine, social con sottotitolo, lingue, P.IVA, Maestro d'Arte e Mestiere 2020, Cookie. Mancano ragione sociale completa, orari e Privacy: non sono nelle fonti (LEGGIMI 1, 2, 11).

### Compiti della scheda d'uso

- *Commissione, computer 1440*: in prima vista organi nuovi e restauro scritti (titolo e strade), Padova dal 1940, la foto di New Orleans con luogo, anno e manuali, EN in testata (porta a ruffatti.com/en/, con il titolo "Il sito inglese di oggi"), Scriveteci, il telefono, l'email con che cosa mandare, la riga degli ultimi strumenti (un clic porta alla lista). Poi i cinque strumenti 2022-2026 con manuali e registri (due con il link alla notizia), "86 opere significative" e "Gli organi restaurati". Ascolta è a un clic (menu) e i video a due. In Contatti email, telefono e "Che cosa mandarci".
- *Parrocchia, telefono 390*: bottone di chiamata a tutta larghezza e numero in testata senza scorrere; Restauro in prima vista, e ora anche dal menu (riparato); nella sezione Restauro "restauro filologico", "anche di altri costruttori" con i nomi di Guglielmi, Callido e Zavarise, circa 120 restauri con località, anno e autore, "Elenco dei restauri", la targhetta "Fratelli Ruffatti" in foto, che cosa preparare per la prima telefonata, "Chiamate 049 750 666" e "Scrivete con le foto" (email con la traccia).
- *Organista, telefono 390*: Menu, poi "Concorso di Miami" (provato: la sezione arriva in vista e il menu si chiude), primo premio US$ 5.000, under 30, "Bando e iscrizione 2027"; Instagram nella stessa sezione, YouTube in Ascolta, tutti e tre i social nel piede.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra testata, titolo, testo, bottoni, strade e foto dell'apertura a tutte queste larghezze. A 320 l'EN passa nel menu (nella testata non c'è posto) e i bottoni Organi nuovi e Restauro scendono appena sotto la prima vista.

### Caratteri e licenze

- **Gambetta** e **Switzer** di Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito, anche sul web), serviti dalla pagina in `sito/fonts/` (gambetta-400, switzer-400, switzer-600 in woff2; il 600 scaricato da Fontshare il 3/11/2026 in `assets/fonts/`). Sono le due famiglie della versione 1, tenute.
- **Foto**: solo loro, dalla libreria media di ruffatti.com (elenco in `assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Collegamenti

- `tel:+39049750666` in testata, apertura, restauro, contatti e piede; `mailto:organs@ruffatti.com` con oggetto (e nel restauro con la traccia dei dati); il modulo compone l'email e va collegato a un servizio (LEGGIMI).
- Mappa: `https://www.google.com/maps/search/?api=1&query=Via+Facciolati+166+35127+Padova`, solo nel piede (l'indirizzo va confermato).
- Lingue: ruffatti.com/en/ e /ru/ (rispondono 200). Video: tre video del canale YouTube "Ruffatti organs" (dal feed del canale) e il canale; CD, Dicono di noi, Concorso di Miami, Opere eseguite e Procedure di restauro sono pagine del sito di oggi. Nessuna ancora senza destinazione; nessun U+2014 in pagina, nei .md e negli script.
