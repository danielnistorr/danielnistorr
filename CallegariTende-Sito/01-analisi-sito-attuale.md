# 01. Analisi del sito attuale (www.callegaritende.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).
Nelle citazioni verbatim le parole della lista PAROLE_VIETATE sono spezzate da un punto mediano (es. "lea·der"): il testo originale le contiene intere. Il trattino medio dei testi originali è reso con "-".
Prove (HTML, PDF, screenshot, misure) in `_prova/crawl/`, `_prova/attuale/` e `_prova/inventario-immagini.json`. Testi completi di tutte le pagine in `_prova/crawl/testi-verbatim.txt`, testi dei PDF in `_prova/crawl/pdf-testo/`.

## In breve

- **Sito PHP del 2010** fatto da Neroavorio srl (CMS proprietario "iceberg", PHP 7.0.33 fuori supporto dal gennaio 2019, XHTML 1.0 Transitional, impaginazione a tabelle), **nessun meta viewport** su nessuna delle 601 pagine: a 390 px la pagina resta larga 996 px e il telefono la rimpicciolisce al 39%, il testo base da 12 px arriva a circa 5 px. HTTPS c'è e funziona (Let's Encrypt, http reindirizza a https). [Certo]
- **Contenuti fermi e pezzi rotti visibili**: copyright 2010, "Sito ottimizzato per Firefox"; l'ultimo depliant è del 2019 (La Rotonda, caricato il 07/10/2019), moduli d'ordine del 2010 e 2013; i tre listini più recenti in home (Tende Tecniche 2019, Filò 2021, Tempo / Sistemi integrazione 2021) aprono **pagine vuote**; in 5 listini il catalogo sfogliabile Issuu mostra **"Not Found - Could not find the requested document"**; un link vuoto presente nel menu di ogni pagina apre una pagina con **errore SQL di MariaDB** in chiaro. [Certo]
- **Dati societari non aggiornati**: il footer ha P.IVA, REA e registro (bene) ma capitale sociale 46.481,12 euro contro 50.000 nel registro; la pagina Azienda dice "50 dipendenti", il registro 16 dipendenti nel 2024 (fascia 10-19); nessuna PEC sul sito. [Certo]
- **Cosa vendono**: produttori e grossisti per rivenditori (tende confezionate su misura, tessuti, bastoni, binari e sistemi in alluminio, tende tecniche, tende da sole), rete vendita con agenti in tutta Italia, ordini con moduli via fax e numero verde fax. Il catalogo online ha **10 listini, 48 linee, 532 schede** con codici, finiture e dati tecnici. [Certo]
- **Materiale fotografico**: sul sito solo foto piccole (535 foto prodotto a 436 px, 5 foto di testata da 700 a 1000 px, 3 foto della sede a 88 px). Il materiale vero è nei **9 PDF dell'Area Downloads**: 267 foto estratte, 193 dai depliant 2014-2019 (foto di studio di tende confezionate, credito "foto Sabbadin"), **98 larghe almeno 850 px, 23 almeno 1000 px** (massimo 1613). Nessuna foto adatta a un'apertura a tutta larghezza a 1440 senza ritaglio; buone per mezze pagine e griglie. Il **logo esiste in vettoriale** dentro il PDF delle condizioni di vendita. Nessuna foto di persone, laboratorio, magazzino o sede in misura utile. [Certo]
- **Identità oggi**: logo con monogramma "C" corsivo bianco in un rombo nero e scritta "Callegari" in un serif grigio; payoff "100% Prodotto italiano" con filetto tricolore; palette sabbia (#dfd3b5, #cdc4aa), testa di moro (#252118, #403b2d), oro ocra (#be8b06) per titoli e link, crema (#f6f4eb). Titoli in Americana BT e menu in Corbel corsivo (tramite Cufon), testo in Arial; nei PDF Rotis Sans Serif. [Certo]

Correzioni rispetto alla scheda di ricerca ricevuta: AddThis e flowplayer 3.1.1 sono **nel codice ma dentro commenti HTML** su tutte le pagine: il browser non li carica (0 richieste verso addthis.com nelle misure). jQuery 1.4 invece è caricato davvero. Le voci di menu non sono immagini ma testo disegnato con Cufon (canvas). Il resto della scheda è confermato.

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home | `/` (doppioni `/index.php`, `/index.php?pag=home`) | testata con 5 foto a dissolvenza, riquadro Login/Password, menu, box "rivenditore più vicino", numero verde fax, testo di presentazione, 10 copertine di listino |
| Azienda | `/index.php?pag=azienda` | storia, elenco di 5 attività, 3 miniature della sede (88x89 px) |
| Listini e Cataloghi | voce di menu `/index.php?pag=cataloghi` | **non ha una pagina sua**: risponde 301 verso `http://www.callegaritende.it/` (la home, passando da http). Sotto-menu con i 10 listini |
| Listini (10) | `/index.php?pag=cataloghi&l=N` | Tempo 2017 (18 linee, 159 schede), Bastoni 2017 (26 linee, 76 schede), Sistemi 2017 (4 famiglie, 15 schede), Album Tessuti (19 collezioni, 187 schede), Ago e Filo 2017 (11 gruppi, 58 schede), Evoluzione Sole 2020 (5 gruppi, 18 schede), Rullo Dek 2013 (19 schede); **Tende Tecniche 2019, Filò 2021, Tempo / Sistemi integrazione 2021: pagina vuota** (solo copertina e titolo) |
| Linee / categorie | `/index.php?pag=cataloghi&l=N&cat=N` | 48 pagine con elenco schede a sinistra e prima scheda aperta |
| Schede prodotto | `/index.php?pag=cataloghi&l=N&cat=N&prid=N` | 532 schede: nome, testo tecnico (finiture, misure, codici), una foto a 436 px; nessun prezzo |
| Area Downloads | `/index.php?pag=listini-e-moduli` | 9 PDF (Album 6 Iridium 2010 e 8 depliant 2014-2019) e 15 moduli d'ordine (2010 e 2013) |
| Contatti | `/index.php?pag=contatti` (conferma `/?pag=contatti&sent=ok`) | email, modulo (nome, cognome, azienda, indirizzo, CAP, città, telefono, email, messaggio), due consensi sì/no, captcha a immagine |
| Dove Siamo | `/index.php?pag=dove` | indicazioni stradali dalla A4 e mappa Google con indicatore |
| Privacy | `/index.php?pag=privacy` (doppione `/?pag=privacy`) | informativa ai sensi del D.Lgs. 196/2003 e cookie |
| Condizioni | `/index.php?pag=condizioni` | solo nella sitemap: pagina vuota. 6 PDF di condizioni di vendita del 2010 in `/pdf/` |
| Area riservata | riquadro Login/Password su ogni pagina; CMS in `/iceberg/acl_manager/users/login` (risponde 500) | contenuto non visibile, probabilmente listini prezzi per rivenditori [DA CONFERMARE] |

In tutto 601 pagine HTML raggiungibili dai link, 24 PDF nell'Area Downloads, 6 PDF e 2 pagine solo nella sitemap (`/google_sitemap.xml`, 154 URL in http). Le pagine inesistenti (es. `?pag=qualsiasi`) rispondono 200 con contenuto vuoto. [Certo]

## Testi reali (verbatim, con i refusi originali)

Home:
1. Titolo: "Callegari Tende"
2. "Siamo produttori nazionali e grossisti di **tende da interno, bastoni decorativi, tende tecniche e tende da esterno** e ci rivolgiamo agli specialisti dell'arredamento e del design con una gamma completa di prodotti che possono **soddisfare la clientela più esigente**."
3. "Le varie collezioni di tende e accessori raccolte all'interno dei nostri cataloghi esprimono tutta la creatività messa in campo da Callegari, divenuta un'**azienda lea·der nel suo settore** grazie a importanti collaborazioni con interior designers e con produttori di tessuti d'arredamento  e soluzioni tecniche di livello internazionale come **Parà** e **Arquati**."
4. "Le tende, i bastoni decorativi e accessori, le tende tecniche e tende da sole sono visibili presso i nostri **rivenditori di zona** che saranno a disposizione per aiutarvi nella scelta e nella corretta installazione dei nostri prodotti."
5. "CONSULTA I NOSTRI CATALOGHI"
6. Box laterale su ogni pagina: "Se vuoi conoscere il rivenditore più vicino alla tua zona contattaci. / La nostra rete vendita è presente in tutta Italia. / TEL. 0498872588"; immagine "Numero Verde Fax 800-019885".
7. Payoff nella testata (immagine): "100% Prodotto italiano".

Azienda:
8. Sottotitolo: "La storia del tendaggio Made in Italy"
9. "Nata alla fine degli **anni '60** da un'intuizione del maestro tappezziere Francesco Callegari è cresciuta via via fino a diventare **azienda lea·der in Italia** nella produzione e commercializzazione di:" Sartoria per tendaggi e coordinati per la casa; Collezioni di tessuti classici e moderni per tendaggi, drappeggi, imbottiti e passamanerie; Sistemi in alluminio e tende tecniche; Bastoni decorativi; Tende da sole.
10. "Oggi possiamo contare sulla collaborazione di **50 dipendenti** distribuiti in due complessi produttivi con una **superficie totale di 3000 mq** . I nostri agenti seguono costantemente i rivenditori che coprono tutto il territorio nazionale offrendo consulenza ad alta specializzazione su tessuti e soluzioni tecniche."
11. "Alle collezioni esclusive di tessuti, al taglio o in pezza, affianchiamo un laboratorio di confezione e sartoria supportato da **tecnologie innova·tive** e animato da una **grande pas·sione** , in grado di realizzare modelli originali e creativi, di testare i materiali e garantirne l'affidabilità."
12. "Vantiamo una gamma di bastoni decorativi dal design esclusivo, tra le più ricche e complete presenti sul mercato nazionale, forti di un'**esperienza quarantennale** nel settore specifico. Il **servizio di consegna è sempre puntuale e tempestivo** garantito da mezzi di trasporto propri, corrieri espressi e soprattutto  da un magazzino sempre rifornito."

Descrizioni dei listini:
13. Bastoni 2017: "Linea completa di bastoni e accessori decorativi per stili tradizionali e per le più svariate esigenze. In vari materiali dall'acciaio, ferro, ferro forgiato artigianalmente, alluminio, ottone, vetro e legno. Tutto il materiale è disponibile in pronta consegna dal nostro magazzino. Questi sono alcuni dei modelli più rappresentativi della vasta gamma offerta dalla ditta Callegari."
14. Tempo 2017: "Linee innova·tive progettate dopo lunga ricerca in collaborazione con vari studi di design. Propone soprattutto acciaio inox e alluminio dalle linee essenziali e uniche."
15. Sistemi 2017: "Sistemi in alluminio confezionati o sfusi garantiti e tecnologicamente all'avan·guardia. Di facile installazione e manutenzione per l'utilizzatore finale."
16. Ago e Filo 2017: "Sartoria "creativa", che abbina ad un'esperienza ventennale su tessuti di qualsiasi genere una qualità e professionalità artigianali. Vasta gamma di collezioni a disposizione: dal classico al moderno al "futurista" per ogni esigenza e gusto. All'interno di queste pagine troverete tendaggi, tessuti, bordi e passamanerie [...]" e "MAGGIORAZIONI: Aumento listino del 10% su tutte le confezioni e/o maggiorazioni a partire dal 01/10/2017 sul listino Ago e Filo Febbraio 2017."
17. Evoluzione Sole 2020: "Le tende utilizzano viterie e bullonerie in acciao inox. Disponibili con motorizzazioni e automatismi. Garanzia di 5 anni su tende e strutture. [...] Tutti i materiali ed automatismi utilizzati nella costruzione delle tende da sole sono di qualità certificata e collaudata dalla ns. trentennale esperienza. Utilizziamo tessuti delle più importanti aziende sul mercato (Parà, Arquati, ecc...)"
18. Album Tessuti: "Strumento per il professionista che raccoglie tutto il nuovo e aggiornato Album 6 Iridium, a colori, delle più rappresentative confezioni, tessuti e sistemi decorativi prodotti dalla nostra azienda." / "* Modelli validi solo per confezione, tessuti esauriti."
19. Rullo Dek 2013: "Ultima versione del Listino Rullo DEK con tutti i nuovi MODULI ORDINE RULLI AGGIORNATI."

Esempi di schede (testo tecnico, il tono del catalogo):
20. Evoluzione Sole, T31 SPRING: "TENDA PER FINESTRA A CADUTA / Struttura a copertura verticale con minimo ingombro funzionante a catenella, con braccetti rotanti. Profili in alluminio e particolari in resine termoplastiche. Il telo raccolto è racchiuso completamente nel cassonetto."
21. Ago e Filo, Palloncino: "Var. AF2 vers. per bastoni: Arricciatura irregolare con effetto a palloncino nei due lati del telo su nastrino trasparente (H. 1 cm.) e anellini in nylon ogni 8 cm. finito a piombo."
22. Album Tessuti, Collezione Capricci pag. 08: "Dimensioni: Sottotenda L. 170 x H. 260 - Calata L. 120 x H. 280 / Sistema: Più Sting doppio scorrevoli cm. 170 fin. S75 con 2 supporti a parete +2561 / Confezione: Sottotenda modello Faldone Rovescio con balza riportata e applicazione laccio [...]"
23. Bastoni, Linea Time ø10: "GLOBO CON ANELLI FIN. S.300 ARDESIA"

Area Downloads:
24. "I listini ed i prezzi **potrebbero subire variazioni** per effetto di aumenti / diminuzioni o aggiornamenti, si prega pertando di verificare **SEMPRE** l'attendibilità di tali prezzi o chiedere conferma in azienda per eventuali ordini. Ove non diversamente specificato tutti i listini si intendono **IVA ESCLUSA**."

Dove Siamo:
25. "Dall'autostrada **A4 MILANO-VENEZIA** uscire a **PADOVA EST** e prendere la tangenziale per **Castelfranco**, uscire per **Reschigliano/Campodarsego** (quarta uscita) e percorrere via Pontarola fino a sbucare nella **SS del Santo**. Da lì, dopo aver svoltato a sinistra, potrete facilmente raggiungere la ns. **sede principale** di via Meucci n.4, situata nella zona artigianale di Cadoneghe."

Contatti, privacy, cookie:
26. Modulo: "La compilazione del presente form sottintende l'avvenuta lettura e comprensione di quanto descritto nella pagina dedicata alla privacy." Consensi "Consenso all'archiviazione dei dati nel database" e "Autorizzazione all'invio di materiale commerciale" (acconsento / non acconsento).
27. Barra cookie: "Questo sito web utilizza cookie tecnici per migliorare il servizio. Proseguendo la navigazione acconsenti all'uso dei cookie. Per maggiori informazioni o per disabilitarne l'utilizzo clicca su Privacy Policy." Pulsanti "OK" e "Privacy Policy".
28. Privacy: "Callegari Francesco Srl ha il massimo rispetto per i diritti degli Utenti. [...] Informativa sulla privacy ai sensi del D. Lgs. 30 giugno 2003, n. 196" e "* AGGIORNAMENTO 1/1/2023: QUESTO SITO NON FA PIÙ USO DI COOKIES RICONDUCIBILI A GOOGLE ANALYTICS."
29. Footer: "Copyright © 2010 Callegari Francesco srl / Via Meucci, 4 - 35010 Cadoneghe (PD) - ITALY / Tel.: +39 049 8872588 - Fax: +39 049 8872059 - Nr. Verde Fax 800 019885 - info@callegaritende.it / C.F. e P.IVA 02006730283 - Cap. Soc. € 46.481,12 i.v. - Reg. Impr. PD n. 02006730283 - REA n. 196376" e "Sito ottimizzato per Firefox®".

Dai PDF del sito (depliant 2018 Bliss, il testo più curato che hanno):
30. Jacquard Onda: "Sinuosi giochi curvilinei caratterizzano la fantasia di questo tessuto. Le linee eleganti e semplici del modello conferiranno brio ad ogni ambiente senza risultare invadenti."
31. Splendor Devorè Jacquard: "La tradizione di classe del design italiano si contraddistingue per signorilità e buongusto. Un gioco di sovrapposizioni e di lavorazioni sartoriali dà corpo al tessuto creando un tendaggio raffinato e dal grande impatto visivo."
32. Condizioni di vendita bastoni/tempo (2010): "IMPORTANTISSIMO / PER ORDINARE IL MATERIALE USARE SEMPRE I MODULI ORDINE FAX / ORARIO PER RITIRO MATERIALE E TRASMIS·SIONE ORDINI TELEFONICI 08:30 / 12:30 • 14:00 / 18:00" e "NON ACCETTEREMO CONTESTAZIONI SUI MATERIALI, TRASCORSI 5 GIORNI LAVORATIVI DALLA CONSEGNA".
33. Condizioni tessuti Filò (2010): "TELEFONO DIRETTO SARTORIA 049 8875260 / FAX VERDE DIRETTO SARTORIA 800-700525" e "Callegari Francesco s.r.l. Via Antoniana, 27 - Z.I. 35010 Cadoneghe (PD)".

Refusi e incoerenze da non riportare: "pertando", "acciao inox", "nuoviMODULI" (a capo mancante), "module ordine cappottine", "interior designers", spazi prima di virgole e punti ("3000 mq .", "pas·sione ,"), nei titoli delle schede "Coupè" e "Devorè" con accento sbagliato e codifica rotta in 98 pagine ("FIL COUPæ FLY", "DIVA DEVORæ"), "Fréer". Esperienza dichiarata in tre modi diversi: "ventennale" (Ago e Filo), "trentennale" (Sole), "quarantennale" (bastoni), con fondazione a "fine degli anni '60": nel nuovo sito si usano solo date verificabili [DA CONFERMARE l'anno di inizio attività del fondatore]. Il nome compare come "Callegari Francesco srl", "Callegari Francesco Srl", "Callegari Francesco s.r.l.", "Callegari s.r.l.", "ditta Callegari": nel nuovo sito **Callegari Francesco S.r.l.** per i dati legali e **Callegari Tende** come nome breve.

## Cosa fanno o vendono

Produttore e grossista che vende **solo tramite rivenditori** ("specialisti dell'arredamento e del design"): il privato viene mandato al rivenditore di zona. Agenti sul territorio nazionale, ordini con moduli PDF da inviare via fax (numero verde fax 800-019885), ritiro in sede o consegna con mezzi propri e corrieri, magazzino con pronta consegna per i bastoni. [Certo]

| Famiglia (listino) | Cosa contiene | Schede online |
|---|---|---|
| Bastoni 2017 | bastoni decorativi in ferro forgiato, ottone, alluminio, acciaio, legno; 26 linee (Time, New Classic, Le Forme, Ottone Classico, I Bronzi, Fréer, Nouveau, Antenati, Clessidra, Ferri Vecchi, Revival legno, materiale per punto vendita), terminali con nomi propri (Globo, Sirio, Oriente, Pastorale, Girandola...) | 76 |
| Tempo 2017 | linee contemporanee in acciaio inox e alluminio: Alluminium Plus (PQ, PS, PG, Più, PT, PL), Alluminium, Universo, Design, Eureka, C acciaio, Irony, Metallika, Stilo, Collezione Tempo (Arco, Crono, Kriss, Metro, Ring, Spazio, Tram); terminali in vetro e legno; espositori per punto vendita | 159 |
| Sistemi 2017 | binari in alluminio per tende arricciate (Best 421, Arco 490/2, Ghibli, Slalom 430), a motore, a pacchetto (Basic 427, Rotary 444/1 e 449, Scirocco, Tornado, Tramontana), a pannello (Sereno Plus, Vento) | 15 |
| Album Tessuti (Album 6 Iridium) | tende confezionate fotografate in ambiente, 19 collezioni dal 2010 al 2018 (Bliss, Life, Click, Spring, Home, Start, Light, Hope, Dettagli, Capricci, Tentazioni, Essenze...), con misure, sistema, confezione e articoli tessuto | 187 |
| Ago e Filo 2017 (sartoria) | modelli di confezione disegnati a mano: arricciature esclusive, tradizionali, con passanti, con occhioli, tende a vetro, finiture/ricami/bracciali, pannelli, pacchetti, mantovane, drappeggi | 58 |
| Evoluzione Sole 2020 | tende da sole: a bracci (BQ1, Q4500), con cassonetto (Maxi Cover), a caduta (CA, CG guide, Nuvola, T11 e T31 Spring, Venezia, Win.Or, Win.Zip), cappottine (K50, KD 50, KS 50, Tond, TUB), pensiline (C-Pensi); garanzia 5 anni su tende e strutture, motorizzazioni | 18 |
| Rullo Dek 2013 (tende tecniche) | tende a rullo Linea Dek e Linea R, plissè, veneziane 16-25 mm, verticali 127 mm, espositore Expo Dek | 19 |
| Filò 2021, Tempo / Sistemi integrazione 2021, Tende Tecniche 2019 | solo copertina, pagina vuota | 0 |
| Depliant collezioni | Hope 2014, Light 2015, Start 2016, Click 2017, Spring 2017, Life 2018, Bliss 2018, La Rotonda 2019 (PDF da 12 a 40 pagine) | PDF |

Partner citati: **Parà** e **Arquati** (tessuti e soluzioni tecniche; un'insegna "Callegari / Arquati" è in una delle foto della sede). Non sono marchi di Callegari: nel nuovo sito si citano come fornitori di tessuti [DA CONFERMARE il rapporto e l'uso dei loghi]. "Rullo Dek", "Tempo", "Filò", "Ago e Filo", "Evoluzione Sole" sono i nomi dei listini Callegari. Nessuna certificazione dichiarata. [Certo]

## Immagini usate oggi

| Tipo | Quantità | Misura | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Foto prodotto bastoni e sistemi (Bastoni, Tempo, Sistemi, Sole, Rullo Dek) | 290 | 436x300 o 436x581 | nitide ma piccole; fondi misti (bianco, grigio chiaro, qualche sfondo sfumato); bastoni fotografati di tre quarti con supporto e anelli, rendering per sole e binari | griglie di prodotto fino a 436 px (218 px su retina) |
| Foto d'ambiente Album Tessuti | 187 | 436x581 | foto di studio di tende confezionate, buone ma piccole | miniature; per le collezioni 2014-2018 c'è la versione più grande nei PDF |
| Figurini Ago e Filo | 58 | 414-436 px | disegni a matite colorate dei modelli di confezione su fondo bianco: materiale insolito e riconoscibile | pagina sartoria, griglia dei modelli fino a 436 px |
| Foto di testata (`images/slide/`) | 5 | 1000x625 (2), 700x1050 (3) | foto di studio di bastoni e pannelli, colori vivi, buone | fino a 1000 px o 700 px; non a tutta larghezza |
| Testata con logo (`images/header.jpg`) | 1 | 1915x164 | logo raster bianco su foto di tessuto grigio, payoff tricolore | solo riferimento: il logo c'è in vettoriale |
| Foto della sede (pagina Azienda) | 3 | 88x89 GIF | due edifici e un'insegna "Callegari / Arquati": troppo piccole | non usare; servono foto nuove |
| Miniature di listini e linee (GIF e JPEG) | 58 | 86-112 px | inutilizzabili | non usare |
| **Foto dai depliant PDF 2014-2019** | 193 | 505-1570 px: 19 da almeno 1000, 72 tra 850 e 999, 68 tra 600 e 849 | foto di studio di tende confezionate in ambienti allestiti (credito "foto Sabbadin", impaginazione Neroavorio), pulite; JPEG per il web a 120 ppi | mezze pagine fino a circa 900-1000 px, colonne a piena larghezza sul telefono, dettagli di tessuto |
| Foto dall'Album 6 Iridium (PDF 2010) | 74 | 505-1613 px, quasi tutte 633x830 | stile più vecchio (pareti colorate, 2010), più rendering tecnici di tende a rullo e da sole | solo dove serve una famiglia non coperta dai depliant |
| Logo vettoriale (PDF condizioni di vendita 2010) | 1 | vettoriale (reso anche PNG 889x1067 a 800 dpi) | ottimo | testata e footer, da ridisegnare in SVG |

Dettaglio file per file, con soggetto, qualità e larghezza massima: `_prova/inventario-immagini.json` (878 voci). Originali: `assets/originali/sito/` (611 file, `manifest.json`), `assets/originali/pdf/` (267 foto, `manifest.json` con PDF e pagina), `assets/originali/logo/`. Nessuna foto oggi è mostrata più grande della sua misura (misurato con Playwright su 12 pagine): il problema è che sono piccole. Fuori dal sito non c'è materiale pubblicato dall'azienda (vedi `assets/esterne/manifest.json`). [Certo]
I depliant sono la fonte migliore ma sono versioni web: gli originali in alta risoluzione vanno chiesti al cliente, insieme alla conferma dei diritti d'uso delle foto del fotografo (Sabbadin) [DA CONFERMARE].

## Problemi tecnici da segnalare al cliente

Misure del 6 ottobre 2026 con Chromium (Playwright), finestra 1440x900 e telefono 390x844. Screenshot in `_prova/attuale/`, numeri in `_prova/attuale/misure.json` (la riga `03-cataloghi` è un artefatto della nostra rete: quella voce reindirizza a http).

1. **Telefono**: nessun `<meta name="viewport">` nelle 601 pagine. A 390 px `document.documentElement.scrollWidth` vale 996 su tutte le pagine misurate e la scala della pagina è 0,39: menu, riquadro login e testo (12 px Arial) diventano di circa 5 px, i link dei PDF sono bersagli di pochi pixel. Prova: `01-home-390-vista-telefono.png`, `08-area-downloads-390-vista-telefono.png`, `06-scheda-album-tessuti-390-vista-telefono.png`. [Certo]
2. **Cataloghi che non si aprono**: nelle pagine Bastoni 2017, Tempo 2017, Sistemi 2017, Album Tessuti e Ago e Filo 2017 il catalogo sfogliabile Issuu incorporato mostra "Not Found / Could not find the requested document / Explore more on Issuu". Prova: `prova-issuu-l30.png` ... `prova-issuu-l36.png`, `04-listino-bastoni-2017-1440.png`. [Certo]
3. **Listini più recenti vuoti**: Tende Tecniche 2019, Filò 2021 e Tempo / Sistemi integrazione 2021, cioè tre delle dieci copertine in home e nel menu, aprono una pagina con la sola copertina. Prova: `07-listino-filo-2021-1440.png`. Probabilmente i listini sono riservati ai rivenditori registrati, ma la pagina non lo dice [Certo per la pagina vuota, Probabile per il motivo].
4. **Errore del database in chiaro**: il menu di ogni pagina contiene un link vuoto (`index.php?pag=cataloghi&=`); aprirlo mostra "Query error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 6". Il link non si vede (testo vuoto) ma i motori di ricerca e i programmi automatici lo seguono. Prova: `12-menu-voce-vuota-1440.png`. Non abbiamo fatto altre prove sul database. [Certo]
5. **Contenuti fermi**: copyright 2010 e "Sito ottimizzato per Firefox" con link a mozilla.com/it su tutte le pagine; Area Downloads con ultimo aggiornamento 07/10/2019 (depliant La Rotonda), moduli d'ordine del 06/10/2010 e 09/12/2013, Album 6 Iridium del 07/10/2010; listino Rullo Dek "2013"; avviso "Aumento listino del 10% [...] a partire dal 01/10/2017"; PDF delle condizioni di vendita del 28/09/2010 (metadati). [Certo]
6. **Dati societari**: il footer riporta ragione sociale, sede, C.F./P.IVA, Registro Imprese e REA (i dati chiesti dall'art. 2250 c.c. ci sono), ma il capitale sociale "€ 46.481,12 i.v." non corrisponde ai 50.000 euro del registro, il civico è "4" invece di "4/a" (VIES e registro), manca la PEC. La pagina Azienda dichiara "50 dipendenti" contro i 16 del bilancio 2024. [Certo]
7. **Privacy e cookie**: informativa scritta sul D.Lgs. 196/2003 (con rinvio all'art. 7, abrogato) senza riferimenti al Regolamento UE 2016/679; barra cookie col consenso implicito "Proseguendo la navigazione acconsenti", senza rifiuto. Prima di qualsiasi scelta la pagina Dove Siamo fa 27 richieste a Google (19 maps.googleapis.com, 4 maps.gstatic.com, 4 Google Fonts) e le pagine listino 22 richieste a Issuu. Cookie scritti dal sito: solo `PHPSESSID`. [Certo; valutazione legale da far fare al loro consulente]
8. **Google e struttura**: nessun H1 in nessuna pagina; 591 pagine su 601 hanno lo stesso titolo "Callegari - Tende e Complementi - Listini e Cataloghi"; meta description vuota su tutte; la voce di menu "Listini e Cataloghi" risponde 301 verso la home in http; pagine doppie (`/`, `/index.php`, `/index.php?pag=home`); pagine inesistenti con risposta 200; sitemap di 154 URL in http, ferma: contiene una linea tolta dal menu (Linea Tekna) e un listino che risponde "Listino non disponibile!"; robots.txt indica la sitemap in http; 98 pagine con lettere corrotte nei titoli ("COUPæ"). [Certo]
9. **Tecnologia superata**: PHP 7.0.33 dichiarato nell'intestazione `X-Powered-By` (fuori supporto dal 10/01/2019), Plesk su Linux, nginx; CMS "iceberg" di Neroavorio con pannello in `/iceberg/acl_manager/users/login` (risponde errore 500); XHTML 1.0 Transitional, layout a tabelle (6 tabelle nella home, 33 in un listino); jQuery 1.4 (2010), Shadowbox 2.0, titoli e menu disegnati con Cufon (122 elementi canvas nella home, tecnica del 2009 per i font non web); codice del 2010 copiato da un altro sito ("JS for italwin.it" in `js/callegari.js`); nessuna intestazione di sicurezza (HSTS, CSP, X-Frame-Options). [Certo]
10. **HTTPS**: certificato Let's Encrypt valido dal 16/09/2026 al 15/12/2026 per callegaritende.it, www.callegaritende.it, callegaritende.com e www.callegaritende.com; http e dominio senza www reindirizzano a https://www.callegaritende.it/. Bene. Il riquadro Login/Password è su https. [Certo]
11. **Peso e tempi** (indicativi, rete del 6/10): home 962 KB e 49 richieste (775 KB sono le 5 foto della testata), evento `load` fra 2,7 e 4,1 s; listino Bastoni 2,4 MB e 88 richieste (con Issuu), fino a 4,5 s; Dove Siamo 1,5 MB e 67 richieste; il server risponde in 0,5-0,7 s. Il peso non è il problema principale. Nessun errore JavaScript in console; solo avvisi di Google Maps (caricamento non asincrono, `google.maps.Marker` deprecato). [Certo]
12. **Testi chiusi in immagini**: logo, nome dell'azienda e payoff "100% Prodotto italiano" esistono solo dentro la foto di testata (sfondo CSS, nessun testo alternativo); numero verde fax in GIF; titoli dei listini sulle copertine GIF. [Certo]
13. **Link esterni**: tutti rispondono, ma le guide cookie per Internet Explorer e Opera rimandano a pagine inglesi generiche; firma "powered by neroavorio" in ogni pagina. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Callegari Francesco S.r.l. (registro: CALLEGARI FRANCESCO S.R.L.) | footer; VIES; aziende.it [Certo] |
| Nome commerciale | "Callegari Tende e Complementi" (titolo del sito), "Callegari Tende" (home), "Callegari Francesco Tendaggi" (Google) | sito, Google Maps [Certo] |
| P.IVA e C.F. | 02006730283 (valida su VIES il 06/10/2026) | footer; VIES [Certo] |
| REA | PD-196376 | footer; aziende.it [Certo] |
| Sede | Via Meucci 4/a, 35010 Cadoneghe (PD) | VIES, aziende.it, Google ("Via Meucci, 4A"); il sito scrive "Via Meucci, 4" [Certo] |
| Secondo sito | Via Antoniana 27, Z.I., 35010 Cadoneghe (PD): sartoria, tel. diretto 049 8875260, fax verde 800 700525 | PDF condizioni tessuti Filò 2010; elenco impresaitalia.info ("Callegari Francesco Snc") [DA CONFERMARE se ancora attivo; il sito parla di "due complessi produttivi"] |
| Telefono | +39 049 8872588 | sito, Google [Certo] |
| Fax | +39 049 8872059; numero verde fax 800 019885 | sito [Certo; DA CONFERMARE se il fax si usa ancora] |
| Email | info@callegaritende.it | sito [Certo] |
| PEC | callegaripec@pec.it | aziende.it (dato del Registro Imprese) [Certo sulla fonte; verificare su INI-PEC prima dell'invio] |
| Codice SDI | J6URRTW | aziende.it [Certo] |
| Forma e capitale | S.r.l., capitale sociale 50.000 euro (il sito dice 46.481,12 i.v.) | aziende.it [Certo] |
| ATECO | 25.12.2 Fabbricazione di strutture metalliche per tende da sole, tende alla veneziana e simili | aziende.it [Certo] |
| Iscrizione | 27/09/1985, CCIAA di Padova; il sito racconta l'inizio "alla fine degli anni '60" con il maestro tappezziere Francesco Callegari | aziende.it; sito [Certo il 1985; DA CONFERMARE l'anno di inizio] |
| Fatturato | 2.027.447 euro (2024, -15,6%), 2.403.504 euro (2023), 2.264.142 euro (2021); fascia 2-5 milioni | aziende.it [Certo] |
| Utile | 22.529 euro (2024), 61.978 euro (2023) | aziende.it [Certo] |
| Dipendenti | 16 (2024), fascia 10-19; il sito dice 50 | aziende.it [Certo] |
| Superficie | "due complessi produttivi con una superficie totale di 3000 mq" | pagina Azienda [Certo che lo dichiarano; DA CONFERMARE] |
| Orari | lunedì-venerdì 8:30-12:30 e 14:00-18:00, sabato e domenica chiuso | Google Maps; stessi orari per ritiro del materiale e ordini telefonici nel PDF condizioni bastoni 2010 [Certo] |
| Rete vendita | agenti e rivenditori "in tutta Italia" | sito [Certo che lo dichiarano; elenco rivenditori non pubblico] |
| Garanzie | tende da sole: "Garanzia di 5 anni su tende e strutture" (listino Sole 2020); PDF 2010: copertura 100% primi 2 anni, poi 60%, 50%, 35% | sito, PDF condizioni sole [Certo; DA CONFERMARE quale vale oggi] |
| Partner | Parà, Arquati (tessuti, soluzioni tecniche) | home, listino Sole [Certo che li citano] |
| Certificazioni | nessuna dichiarata | [Certo] |
| Canali | nessun profilo social collegato o trovato; scheda Google "Callegari Francesco Tendaggi", categoria "Fabbricazione e vendita tende", 4,8 su 19 recensioni, solo foto Street View, link "Rivendica questa attività" visibile | Google Maps letto il 06/10/2026 [Certo] |
| Web agency attuale | Neroavorio srl (autore del sito e dei depliant) | meta author, footer, PDF [Certo] |

## Cosa manca e decisioni aperte

- **Foto da fare** (nessuna esiste in misura utile): sede e insegna di Via Meucci, laboratorio di sartoria al lavoro (taglio, cucitura, piombatura), magazzino bastoni, dettagli di finiture e terminali in ottone e ferro forgiato, campionari tessuti, consegna con i mezzi propri. Le 3 foto della sede sul sito sono 88 px.
- **Da chiedere al cliente**: originali in alta risoluzione dei depliant 2014-2019 e diritti d'uso web (fotografo Sabbadin, impaginazione Neroavorio); file vettoriale del logo (in alternativa si ricava dal PDF); listini Filò 2021, Tempo / Sistemi integrazione 2021, Tende Tecniche 2019 e cataloghi 2022-2026 se esistono; se l'area riservata e i moduli fax si usano ancora; dipendenti, capitale e civico corretti; se Via Antoniana 27 è ancora attiva; anno di inizio del fondatore; rapporto con Parà e Arquati; garanzia attuale delle tende da sole; elenco rivenditori pubblicabile o solo "contattaci".
- **Decisione di contenuto**: il catalogo ha 532 schede con dati tecnici veri. Il nuovo sito non deve rifarle tutte: famiglie e linee con le foto migliori, e i listini PDF aggiornati scaricabili (o in area riservata) per i rivenditori.
- **Non riuscito**: Wayback Machine (web.archive.org non raggiungibile dalla rete di lavoro: connessione chiusa e 429), quindi nessuna versione storica confrontata; cataloghi Issuu (documenti non più pubblici, issuu.com risponde 403 alla nostra rete); PagineGialle e registroaziende.it (403); PEC non verificata su INI-PEC (richiede captcha).

## URL vecchi

Tutti gli URL raggiungibili trovati dal crawl e dalla sitemap (635), da usare per `plugin/redirect-301.csv`. Elenco completo uno per riga in `_prova/crawl/url-vecchi.txt`. Gli URL sono tutti `index.php` con parametri: il redirect va fatto sulla query string (`pag`, `l`, `cat`, `prid`), quindi serve un plugin che legga i parametri o regole in `.htaccess` / nginx.

```
# pagine istituzionali e tecniche
/
/index.php   (doppione della home)
/index.php?pag=home   (doppione della home)
/index.php?pag=azienda
/index.php?pag=cataloghi   (301 verso http://www.callegaritende.it/, voce di menu "Listini e Cataloghi")
/index.php?pag=listini-e-moduli
/index.php?pag=contatti
/?pag=contatti&sent=ok   (conferma invio modulo)
/index.php?pag=dove
/index.php?pag=privacy
/?pag=privacy   (doppione della privacy)
/index.php?pag=condizioni   (solo nella sitemap, pagina vuota)
/index.php?pag=cataloghi&=   (link vuoto nel menu: errore SQL)
/captchapage.php   (immagine captcha del modulo)
/google_sitemap.xml

# listini (10 dal menu + 1 solo in sitemap)
/index.php?pag=cataloghi&l=36   (Tempo 2017)
/index.php?pag=cataloghi&l=30   (Bastoni 2017)
/index.php?pag=cataloghi&l=35   (Sistemi 2017)
/index.php?pag=cataloghi&l=145   (Tempo / Sistemi integrazione 2021, pagina vuota)
/index.php?pag=cataloghi&l=31   (Album Tessuti)
/index.php?pag=cataloghi&l=144   (Filò 2021, pagina vuota)
/index.php?pag=cataloghi&l=33   (Ago e Filo 2017)
/index.php?pag=cataloghi&l=32   (Evoluzione Sole 2020)
/index.php?pag=cataloghi&l=142   (Tende Tecniche 2019, pagina vuota)
/index.php?pag=cataloghi&l=34   (Rullo Dek 2013)
/index.php?pag=cataloghi&l=82   (solo sitemap: "Listino non disponibile!")

# categorie (48 + 1 solo in sitemap)
/index.php?pag=cataloghi&l=36&cat=54   (Tempo 2017 / Linea Alluminium Plus PQ)
/index.php?pag=cataloghi&l=36&cat=55   (Tempo 2017 / Linea Alluminium Plus PQ 2010)
/index.php?pag=cataloghi&l=36&cat=56   (Tempo 2017 / Linea Alluminium Plus PS)
/index.php?pag=cataloghi&l=36&cat=57   (Tempo 2017 / Linea Alluminium Plus PG)
/index.php?pag=cataloghi&l=36&cat=58   (Tempo 2017 / Linea Alluminium Plus Più)
/index.php?pag=cataloghi&l=36&cat=59   (Tempo 2017 / Linea Alluminium Plus PT)
/index.php?pag=cataloghi&l=36&cat=60   (Tempo 2017 / Linea Alluminium Plus PL)
/index.php?pag=cataloghi&l=36&cat=61   (Tempo 2017 / Linea Alluminium)
/index.php?pag=cataloghi&l=36&cat=62   (Tempo 2017 / Linea Universo alluminio-COLOR)
/index.php?pag=cataloghi&l=36&cat=63   (Tempo 2017 / Linea Design)
/index.php?pag=cataloghi&l=36&cat=64   (Tempo 2017 / Linea Eureka)
/index.php?pag=cataloghi&l=36&cat=65   (Tempo 2017 / Linea C acciaio)
/index.php?pag=cataloghi&l=36&cat=66   (Tempo 2017 / Linea Irony)
/index.php?pag=cataloghi&l=36&cat=67   (Tempo 2017 / Linea Universo Acciaio)
/index.php?pag=cataloghi&l=36&cat=69   (Tempo 2017 / Linea Metallika)
/index.php?pag=cataloghi&l=36&cat=70   (Tempo 2017 / Collezione Tempo)
/index.php?pag=cataloghi&l=36&cat=71   (Tempo 2017 / Materiale per il Punto Vendita Tempo)
/index.php?pag=cataloghi&l=36&cat=83   (Tempo 2017 / Linea Stilo)
/index.php?pag=cataloghi&l=30&cat=88   (Bastoni 2017 / Linea Time ø 10)
/index.php?pag=cataloghi&l=30&cat=89   (Bastoni 2017 / Linea New Classic Astine allungabili ø 10)
/index.php?pag=cataloghi&l=30&cat=90   (Bastoni 2017 / Linea New Classic Bastoncini ottone ø 10)
/index.php?pag=cataloghi&l=30&cat=91   (Bastoni 2017 / Linea New Classic Astine allungabili ø 7)
/index.php?pag=cataloghi&l=30&cat=92   (Bastoni 2017 / Linea Le Forme ottone ø 10)
/index.php?pag=cataloghi&l=30&cat=93   (Bastoni 2017 / Linea Le Forme ottone ø 20)
/index.php?pag=cataloghi&l=30&cat=94   (Bastoni 2017 / Linea New Classic ottone ø 20)
/index.php?pag=cataloghi&l=30&cat=95   (Bastoni 2017 / Linea Ottone Classico ø 20)
/index.php?pag=cataloghi&l=30&cat=96   (Bastoni 2017 / Linea Ottone Classico ø 30)
/index.php?pag=cataloghi&l=30&cat=97   (Bastoni 2017 / Linea I Bronzi ottone bronzato graffiato ø 20)
/index.php?pag=cataloghi&l=30&cat=98   (Bastoni 2017 / Linea Time ø20 AA anelli alluminio)
/index.php?pag=cataloghi&l=30&cat=99   (Bastoni 2017 / Linea Time ø20 AR anello rettangolo)
/index.php?pag=cataloghi&l=30&cat=100   (Bastoni 2017 / Linea Time ø20 SC scorrevoli)
/index.php?pag=cataloghi&l=30&cat=101   (Bastoni 2017 / Linea Time ø30 AA anelli alluminio)
/index.php?pag=cataloghi&l=30&cat=102   (Bastoni 2017 / Linea Time ø30 SC scorrevoli)
/index.php?pag=cataloghi&l=30&cat=103   (Bastoni 2017 / Linea Fréer ferro forgiato artigianalm. (pieno) ø18)
/index.php?pag=cataloghi&l=30&cat=104   (Bastoni 2017 / Linea Nouveau ferro ø18 forgiato)
/index.php?pag=cataloghi&l=30&cat=105   (Bastoni 2017 / Linea Antenati 2 ferro ø18 forgiati anticati)
/index.php?pag=cataloghi&l=30&cat=106   (Bastoni 2017 / Linea Clessidra ferro ø20)
/index.php?pag=cataloghi&l=30&cat=107   (Bastoni 2017 / Linea Bastoncini anticati ø10)
/index.php?pag=cataloghi&l=30&cat=108   (Bastoni 2017 / Linea C ferro anticato ø 20)
/index.php?pag=cataloghi&l=30&cat=109   (Bastoni 2017 / Linea Ferri Vecchi ottone-ferro ø15)
/index.php?pag=cataloghi&l=30&cat=110   (Bastoni 2017 / Linea Ferri Vecchi ø20)
/index.php?pag=cataloghi&l=30&cat=111   (Bastoni 2017 / Linea Ferri Vecchi ø30)
/index.php?pag=cataloghi&l=30&cat=112   (Bastoni 2017 / Linea Revival legno classico ø35)
/index.php?pag=cataloghi&l=30&cat=113   (Bastoni 2017 / Materiale per il Punto Vendita Bastoni)
/index.php?pag=cataloghi&l=35&cat=119   (Sistemi 2017 / SISTEMI PER TENDE ARRICCIATE)
/index.php?pag=cataloghi&l=35&cat=120   (Sistemi 2017 / SISTEMI PER TENDE ARRICCIATE A MOTORE)
/index.php?pag=cataloghi&l=35&cat=121   (Sistemi 2017 / SISTEMI PER TENDE A PACCHETTO)
/index.php?pag=cataloghi&l=35&cat=122   (Sistemi 2017 / SISTEMI PER TENDE A PANNELLO)
/index.php?pag=cataloghi&l=36&cat=68   (solo sitemap: Tempo 2017 / Linea Tekna)

# documenti PDF (Area Downloads)
/iceberg/document_manager/documents/download/108/1/modordinerullostandard
/iceberg/document_manager/documents/download/109/1/modordinerullodoppio
/iceberg/document_manager/documents/download/110/1/modordinerullodoppio2
/iceberg/document_manager/documents/download/111/1/modordinerullosormonto
/iceberg/document_manager/documents/download/112/1/modordinerullostandard2
/iceberg/document_manager/documents/download/117/1/depliant_hope02web
/iceberg/document_manager/documents/download/120/1/depliant_light_2015_web
/iceberg/document_manager/documents/download/121/1/depliant_start_2016_web
/iceberg/document_manager/documents/download/126/1/depliant_spring_2017_web
/iceberg/document_manager/documents/download/130/1/depliant_click_web
/iceberg/document_manager/documents/download/136/1/depliant_life_2018
/iceberg/document_manager/documents/download/140/1/depliant_collezione_2018_bliss
/iceberg/document_manager/documents/download/146/1/depliant_la_rotonda_2019web
/iceberg/document_manager/documents/download/68/1/modulo_ordine_bastoni
/iceberg/document_manager/documents/download/69/1/modulo_ordine_sistemi
/iceberg/document_manager/documents/download/70/1/modulo_ordine_tessuti_filo
/iceberg/document_manager/documents/download/72/1/modulo_ordine_tende_tecniche
/iceberg/document_manager/documents/download/74/1/modulo_ordine_veneziane
/iceberg/document_manager/documents/download/76/1/modulo_ordine_confezione_mantovane
/iceberg/document_manager/documents/download/77/1/modulo_ordine_sole_teli_confezionati
/iceberg/document_manager/documents/download/78/1/modulo_ordine_sole_tende_bracci
/iceberg/document_manager/documents/download/79/1/modulo_ordine_confezione_tessuti
/iceberg/document_manager/documents/download/80/1/modulo_ordine_sole_cappotte
/iceberg/document_manager/documents/download/87/1/album_6_iridium

# PDF condizioni di vendita 2010 (solo sitemap)
/pdf/condizioni_ago_e_filo.pdf
/pdf/condizioni_bastoni_-_tempo.pdf
/pdf/condizioni_rullo_dek_tecniche.pdf
/pdf/condizioni_sistemi_tende_tecniche.pdf
/pdf/condizioni_sole.pdf
/pdf/condizioni_tessuti_filo.pdf

# schede prodotto (532): /index.php?pag=cataloghi&l=L&cat=C&prid=P, intervalli di prid per linea
l=30&cat=88  (Bastoni 2017 / Linea Time ø 10, 3 schede)  prid=469-471
l=30&cat=89  (Bastoni 2017 / Linea New Classic Astine allungabili ø 10, 5 schede)  prid=472-476
l=30&cat=90  (Bastoni 2017 / Linea New Classic Bastoncini ottone ø 10, 4 schede)  prid=477-480
l=30&cat=91  (Bastoni 2017 / Linea New Classic Astine allungabili ø 7, 3 schede)  prid=481-483
l=30&cat=92  (Bastoni 2017 / Linea Le Forme ottone ø 10, 4 schede)  prid=484-487
l=30&cat=93  (Bastoni 2017 / Linea Le Forme ottone ø 20, 3 schede)  prid=488-490
l=30&cat=94  (Bastoni 2017 / Linea New Classic ottone ø 20, 2 schede)  prid=491-492
l=30&cat=95  (Bastoni 2017 / Linea Ottone Classico ø 20, 2 schede)  prid=493-494
l=30&cat=96  (Bastoni 2017 / Linea Ottone Classico ø 30, 2 schede)  prid=495-496
l=30&cat=97  (Bastoni 2017 / Linea I Bronzi ottone bronzato graffiato ø 20, 2 schede)  prid=497-498
l=30&cat=98  (Bastoni 2017 / Linea Time ø20 AA anelli alluminio, 2 schede)  prid=499-500
l=30&cat=99  (Bastoni 2017 / Linea Time ø20 AR anello rettangolo, 2 schede)  prid=501-502
l=30&cat=100  (Bastoni 2017 / Linea Time ø20 SC scorrevoli, 2 schede)  prid=503-504
l=30&cat=101  (Bastoni 2017 / Linea Time ø30 AA anelli alluminio, 2 schede)  prid=505-506
l=30&cat=103  (Bastoni 2017 / Linea Fréer ferro forgiato artigianalm. (pieno) ø18, 3 schede)  prid=508-510
l=30&cat=104  (Bastoni 2017 / Linea Nouveau ferro ø18 forgiato, 2 schede)  prid=511-512
l=30&cat=105  (Bastoni 2017 / Linea Antenati 2 ferro ø18 forgiati anticati, 5 schede)  prid=513-517
l=30&cat=106  (Bastoni 2017 / Linea Clessidra ferro ø20, 2 schede)  prid=518-519
l=30&cat=107  (Bastoni 2017 / Linea Bastoncini anticati ø10, 3 schede)  prid=520-522
l=30&cat=108  (Bastoni 2017 / Linea C ferro anticato ø 20, 3 schede)  prid=466-468
l=30&cat=109  (Bastoni 2017 / Linea Ferri Vecchi ottone-ferro ø15, 4 schede)  prid=523-526
l=30&cat=110  (Bastoni 2017 / Linea Ferri Vecchi ø20, 8 schede)  prid=527-534
l=30&cat=111  (Bastoni 2017 / Linea Ferri Vecchi ø30, 2 schede)  prid=535-536
l=30&cat=112  (Bastoni 2017 / Linea Revival legno classico ø35, 2 schede)  prid=537-538
l=30&cat=113  (Bastoni 2017 / Materiale per il Punto Vendita Bastoni, 4 schede)  prid=462-465
l=31&cat=40  (Album Tessuti / Collezione Capricci, 10 schede)  prid=94-103
l=31&cat=41  (Album Tessuti / Collezione Tendine a vetro 2010, 3 schede)  prid=104-106
l=31&cat=42  (Album Tessuti / Collezione Brio Uniti e Ignifughi, 10 schede)  prid=107-108,110-117
l=31&cat=43  (Album Tessuti / Collezione Tentazioni, 9 schede)  prid=118-126
l=31&cat=44  (Album Tessuti / Collezione Immagini di Primavera, 5 schede)  prid=127-131
l=31&cat=45  (Album Tessuti / Collezione Immagini, 3 schede)  prid=132-134
l=31&cat=46  (Album Tessuti / Collezione Attimi di Primavera, 2 schede)  prid=135,145
l=31&cat=47  (Album Tessuti / Collezione Attimi, 9 schede)  prid=136-144
l=31&cat=48  (Album Tessuti / Collezione Essenze, 4 schede)  prid=146-149
l=31&cat=49  (Album Tessuti / Ex Collezione Mix (sostituito da Brio Uniti e Ignifughi), 3 schede)  prid=150-152
l=31&cat=132  (Album Tessuti / Collezione Dettagli, 17 schede)  prid=596-612
l=31&cat=133  (Album Tessuti / Collezione Hope, 11 schede)  prid=613-623
l=31&cat=134  (Album Tessuti / Collezione Light, 15 schede)  prid=624-638
l=31&cat=135  (Album Tessuti / Collezione Start, 15 schede)  prid=639-653
l=31&cat=136  (Album Tessuti / Collezione Home, 14 schede)  prid=654-667
l=31&cat=137  (Album Tessuti / Collezione Spring, 23 schede)  prid=668-690
l=31&cat=138  (Album Tessuti / Collezione Click, 9 schede)  prid=691-699
l=31&cat=146  (Album Tessuti / Collezione Life, 11 schede)  prid=700-710
l=31&cat=147  (Album Tessuti / Collezione Bliss, 14 schede)  prid=711-724
l=32&cat=123  (Evoluzione Sole 2020 / Tende a bracci, 2 schede)  prid=559-560
l=32&cat=124  (Evoluzione Sole 2020 / Tende a bracci con cassonetto, 1 schede)  prid=561
l=32&cat=125  (Evoluzione Sole 2020 / Tende a caduta, 8 schede)  prid=562-569
l=32&cat=126  (Evoluzione Sole 2020 / Cappottine, 5 schede)  prid=570-574
l=32&cat=127  (Evoluzione Sole 2020 / Pensiline, 2 schede)  prid=575-576
l=33&cat=73  (Ago e Filo 2017 / Arricciature Esclusive, 8 schede)  prid=162,164-170
l=33&cat=74  (Ago e Filo 2017 / Arricciature Tradizionali, 6 schede)  prid=171-176
l=33&cat=75  (Ago e Filo 2017 / Arricciature con Passanti, 3 schede)  prid=177-179
l=33&cat=76  (Ago e Filo 2017 / Tende a Vetro, 3 schede)  prid=183-185
l=33&cat=77  (Ago e Filo 2017 / Finiture - Ricami - Bracciali, 9 schede)  prid=186-194
l=33&cat=78  (Ago e Filo 2017 / Pannelli, 8 schede)  prid=195-202
l=33&cat=79  (Ago e Filo 2017 / Pacchetti, 4 schede)  prid=203-206
l=33&cat=80  (Ago e Filo 2017 / Drappeggi per Bastoni, 6 schede)  prid=212-217
l=33&cat=81  (Ago e Filo 2017 / Drappeggi per Sistemi in Alluminio, 3 schede)  prid=218-220
l=33&cat=84  (Ago e Filo 2017 / Arricciature con Occhioli, 3 schede)  prid=180-182
l=33&cat=85  (Ago e Filo 2017 / Mantovane Base, 5 schede)  prid=207-211
l=34&cat=128  (Rullo Dek 2013 / Prodotti Rullo Dek Tecniche, 19 schede)  prid=577-595
l=35&cat=119  (Sistemi 2017 / SISTEMI PER TENDE ARRICCIATE, 6 schede)  prid=543-545,551-553
l=35&cat=121  (Sistemi 2017 / SISTEMI PER TENDE A PACCHETTO, 7 schede)  prid=547-550,554-556
l=35&cat=122  (Sistemi 2017 / SISTEMI PER TENDE A PANNELLO, 2 schede)  prid=557-558
l=36&cat=54  (Tempo 2017 / Linea Alluminium Plus PQ, 17 schede)  prid=221-230,240-246
l=36&cat=55  (Tempo 2017 / Linea Alluminium Plus PQ 2010, 9 schede)  prid=231-239
l=36&cat=56  (Tempo 2017 / Linea Alluminium Plus PS, 4 schede)  prid=247-250
l=36&cat=57  (Tempo 2017 / Linea Alluminium Plus PG, 5 schede)  prid=251-255
l=36&cat=58  (Tempo 2017 / Linea Alluminium Plus Più, 9 schede)  prid=256-264
l=36&cat=59  (Tempo 2017 / Linea Alluminium Plus PT, 7 schede)  prid=265-271
l=36&cat=60  (Tempo 2017 / Linea Alluminium Plus PL, 9 schede)  prid=272-280
l=36&cat=61  (Tempo 2017 / Linea Alluminium, 21 schede)  prid=281-289,291-301,387
l=36&cat=62  (Tempo 2017 / Linea Universo alluminio-COLOR, 10 schede)  prid=302-311
l=36&cat=64  (Tempo 2017 / Linea Eureka, 2 schede)  prid=323-324
l=36&cat=65  (Tempo 2017 / Linea C acciaio, 7 schede)  prid=325-327,343-346
l=36&cat=66  (Tempo 2017 / Linea Irony, 19 schede)  prid=328-342,347-350
l=36&cat=67  (Tempo 2017 / Linea Universo Acciaio, 6 schede)  prid=351-356
l=36&cat=69  (Tempo 2017 / Linea Metallika, 5 schede)  prid=363-367
l=36&cat=70  (Tempo 2017 / Collezione Tempo, 10 schede)  prid=368-377
l=36&cat=71  (Tempo 2017 / Materiale per il Punto Vendita Tempo, 9 schede)  prid=378-386
l=36&cat=83  (Tempo 2017 / Linea Stilo, 10 schede)  prid=313-322
```
