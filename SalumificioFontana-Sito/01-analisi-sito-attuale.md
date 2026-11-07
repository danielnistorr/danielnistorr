# 01. Analisi del sito attuale (www.salumificiofontana.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte o misurato, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare, **[DA CONFERMARE]** dato da chiedere al cliente (va nel LEGGIMI).
Prove: `_prova/crawl/` (HTML, `prove-tecniche.txt`, `testi-verbatim.txt`, `fonti/`), `_prova/attuale/` (screenshot e `misure*.json`), `_prova/inventario-immagini.json`.

## In breve

- Sito Joomla **3.8.10 del giugno 2018** (ramo 3 senza aggiornamenti da agosto 2023), tema YOOtheme "Balance" a larghezza fissa **980 px**, immagini caricate sul server il 23/09/2018 (Last-Modified). Funziona solo in **http**: in https il server presenta un certificato `*.shellrent.com`. [Certo]
- Da telefono il sito **non** si apre rimpicciolito come scriveva la ricerca iniziale: con user agent iPhone o Android il server manda una vecchia **versione mobile generica** (pulsante in inglese "Switch to Desktop Version", nessun logo, nessun piede con indirizzo, P.IVA ed email, mappa in errore, captcha assente). La versione desktop a 980 px senza viewport arriva invece a **tablet** (iPad: scrollWidth 980, scala 0,84) e a chi chiede il sito desktop dal telefono (scala 0,40). [Certo]
- Contenuti fermi: la Storia cita come anno più recente il **2009**, il logo e le meta description dicono ancora **"F.lli Fontana S.n.c."**, mentre la società è **Salumificio Giovanni Fontana S.r.l.** (VIES); la sigla S.r.l. non compare in nessuna pagina. La home non ha testo, solo due immagini. [Certo]
- Il materiale buono c'è, ma quasi tutto fuori dal sito: 4 foto del portale regionale Veneto Around Me (fino a **2560 px**, una del fotografo Stefano Aiti, una di Giovanni Milani), 11 foto professionali di Valsana del 2025 (di terzi), e dal sito **45 foto prodotto scontornate a 450 px**, 4 banner fotomontaggio da 1212 px, 4 foto storiche (960 e 260 px). [Certo]
- L'azienda oggi fa più di quello che il sito racconta: **visite guidate con degustazione** (lun-ven ore 10:00 e 15:30, su prenotazione), vendita diretta, arrosti nuovi (Porchetta e Filetto cotti al naturale, **Filetto della Timpa** con foglie di limone di Acireale), guida della terza generazione (Paola Fontana e il marito Marcello). Niente di questo è sul sito. [Certo, da fonti pubbliche]

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home IT | `/it/` (anche `/it`, `/` reindirizza qui) | slideshow di 2 immagini 960x386 con testo fuso (date 1919, 1941, 1974), nessun testo, nessun H1 |
| Storia azienda | `/it/storia-azienda` | banner collage 970x195, 4 paragrafi, 3 foto storiche 260x400 |
| Prodotti | `/it/prodotti` | banner, 4 categorie con miniatura (63-130 px) ed elenco nomi in maiuscolo, una frase sul commercio di carni |
| Stagionati | `/it/prodotti/stagionati` | banner 1211x487, 15 foto prodotto con nome |
| Freschi | `/it/prodotti/freschi` | banner, 4 foto prodotto (l'elenco in Prodotti ne nomina 10) |
| Cotti | `/it/prodotti/cotti` | banner, 16 foto prodotto |
| Affumicati | `/it/prodotti/affumicati` | banner, 10 foto prodotto (2 nomi ripetuti) |
| Contatti | `/it/contatti` | indirizzo, 2 telefoni, mappa Google in errore, modulo con captcha che non compare |
| Eventi (orfana) | `/it/8-eventi`, `/it/8-eventi/4-eventi` | fuori dal menu, trovata con la ricerca interna: Bad Windsheim (Germania), luglio 2013, 3 foto |
| Versione inglese | `/en/`, `/en/company-history`, `/en/products`, `/en/products/cured`, `/fresh`, `/cooked`, `/smoked`, `/en/contacts` | storia tradotta; nomi prodotto in italiano; titolo "CONTATTI" in italiano nella pagina Contacts |
| Ricerca | `/it/component/search/` | ricerca Joomla nella barra del menu |
| Amministrazione | `/administrator/` | pagina di accesso pubblica |

La Wayback Machine non è raggiungibile da questo ambiente (web.archive.org chiude la connessione, archive.org risponde 429): versioni precedenti del sito non consultate. [Certo]

## Testi reali (verbatim, con i refusi originali)

Home: nessun testo nel corpo. Testo dentro le immagini (trascritto): slide 1 "Montagnana, 1919" ed "Este, 1941" in corsivo sotto il logo; slide 2 "1974" su una foto aerea dello stabilimento.

Testata (immagine): "SALUMIFICIO FONTANA dei F.LLI FONTANA S.N.C." e "Azienda associata al Consorzio di Tutela del Prosciutto Veneto Berico-Euganeo DOP" con il leone e la scritta "VENETO". Logo tondo: "SALUMIFICIO FONTANA ESTE . PADOVA" con un castello.

Piede (desktop): "35042 ESTE (PD) - via Schiavin, 9 / TEL. 0429 2164 4386 - FAX 0429 4386 / P. IVA 00228620282 / info@salumificiofontana.it"

Storia azienda (`/it/storia-azienda`):
1. "La storia del Salumificio Fontana di Este inizia a Montagnana, dove, nel 1919, i fratelli Giovanni e Attilio Fontana fondano la loro prima attività di produzione salumi."
2. "E' Giovanni Fontana, in seguito alla divisione dell'attività con il fratello, ad avviare la produzione nel 1941 a Este, dando vita a una delle aziende storiche di questo comune. Acquistata sul finire degli anni trenta una barchessa adibita a magazzino di cereali, Giovanni, classe 1890, trasforma lo stabile in salumificio iniziando la produzione di prosciutti e salumi in genere."
3. "All'inizio dell'attività l'azienda occupa una decina di persone ed ha un carattere fortemente stagionale con un numero limitato di prodotti. Dopo appena due anni di vita la fabbrica viene requisita dall'esercito tedesco e gestita per due anni dai soldati per rifornire di salumi e di carni i vari comandi militari della zona. L'attività riprende immediatamente nel 1945, dopo la liberazione."
4. "Nel 1951 a causa di una infermità, il capofamiglia deve passare le redini dell'azienda nelle mani della moglie Lea Vezzù, maestra in pensione, che la gestisce fino a quando, uno dopo l'altro, i figli, ancora giovani, non cominciano a occuparsene in prima persona. Il salumificio è ora condotto dai fratelli Giuseppe, Francesco e Bruno (Mario è scomparso nel settembre 2009), ma la terza generazione Fontana è già entrata nell'azienda di famiglia."

Prodotti (`/it/prodotti`), elenchi per categoria (così, in maiuscolo, separati da trattini):
- Stagionati: "BONDIOLE - COPPACOLLI - FIOCCHI - LINGUE SALMISTRATE BOVINO - PANCETTE ARROTOLATE - PANCETTE ARROTOLATE AL PEPE - PROSCIUTTO VENETO DOP - PROSCIUTTO STAGIONATO MEC - SALAME NOSTRANO - SALAME NOSTRANO CASERECCIO - SALAME TIPO UNGHERESE - SALAMETTI TURISTI - SOPRESSE - SOPRESSE MAXI"
- Freschi: "BONDIOLE - BONDIOLE CON LINGUA SALMISTRATA SUINO - COTECHINI - COTECHINI CON LINGUA SALMISTRATA SUINO - ROSSETTI - SALAME NOSTRANO DA FERRI - SALSICCIA D'ARROSTO - SALSICCIA TIPO MODENA - SALSICCIA TIPO TREVISO - ZAMPONI CRUDI"
- Cotti: "COPPA DI TESTA - COTECHINO PRECOTTO - COSCE SUINO COTTE AL NATURALE - FESA DI TACCHINO ARROSTITA - LINGUE SALMISTRATE BOVINO PRECOTTE - LIONER FARCITO - MORTADELLA PURO SUINO SENZA POLIFOSFATI - PORCHETTA COTTA - PROSCIUTTO COTTO DI SCAMONE - PROSCIUTTO COTTO SENZA POLIFOSFATI - ROSTINO SUINO SENZA POLIFOSFATI - ROASTBEEF ALL'INGLESE - SALAME ROSA - SPALLE COTTE - SPALLE COTTE DA TOAST - SPALLE COTTE SENZA COTENNA - PROSCIUTTI MIGNON - STINCHI COTTI SUINO - STRUTTO E CICCIOLI - ZAMPONE COTTO"
- Affumicati: "GUANCIALE SUINO - LOMBI SUINO - PANCETTA STUFATA - PANCETTA CRUDA - SALSICCIA TIPO NAPOLI - SPECK - WÜRSTEL"
- Frase finale: "Il Salumificio Fontana commercializza carne suina e bovina, sia fresca che congelata, in quarti o confezioni sottovuoto ed altre specialità gastronomiche."

Didascalie delle schede con foto:
- Stagionati: "PROSCIUTTO VENETO BERICO EUGANEO DOP", "PROSCIUTTO VENETO BERICO EUGANEO DOP DISOSSATO", "PROSCIUTTO CRUDO STAGIONATO MEC", "PROSCIUTTO CRUDO STAGIONATO MEC DISOSSATO", "COPPA STAGIONATA", "FIOCCO STAGIONATO", "LINGUA SALMISTRATA CRUDA", "PANCETTA ARROTOLATA", "PANCETTA ARROTOLATA AL PEPE", "PANCETTA COPPATA", "SALAME NOSTRANO", "SALAME NOSTRANO CASERECCIO", "SALAME UNGHERESE", "SALAMETTO TURISTA", "SOPRESSA VENETA".
- Freschi: "COTECHINO", "SALAME DA FERRI", "SALSICCIA D'ARROSTO", "SALSICCIA MODENA".
- Cotti: "COPPA DI TESTA", "COSCIA DI SUINO COTTA", "FESA DI TACCHINO ARROSTITA", "LINGUA BOVINA SALMISTRATA COTTA", "LIONER FARCITO", "MORTADELLA", "PORCHETTA", "PROSCIUTTO COTTO DI SCAMONE E PROSCIUTTO MIGNON", "PROSCIUTTO COTTO SENZA POLIFOSFATI", "ROASTBEEF", "SALAME ROSA", "SPALLA COTTA DA TOAST", "CICCIOLI", "COTECHINO COTTO", "STINCO COTTO", "ZAMPONE COTTO".
- Affumicati: "GOLE CON COTENNA AFFUMICATE", "LOMBO SUINO AFFUMICATO", "PANCETTA AFFUMICATA COTTA" (due volte), "PANCETTA AFFUMICATA CRUDA", "SALSICCIA NAPOLI" (due volte), "SPECK INTERO", "SPECK MEZZO", "WÜRSTEL".

Contatti (`/it/contatti`): "CONTATTI / Indirizzo / Via Schiavin, 9 / Este / Padova / 35042 / Italia / Informazioni sul contatto / +39 0429 2164 / +39 0429 4386 / http://www.salumificiofontana.it / Altre informazioni / Modulo contatti / Invia un'email. Tutti i campi contrassegnati da asterisco (*) sono obbligatori." Campi: Nome, Email, Oggetto del messaggio, Inserire un messaggio, Invia una copia alla tua email, Captcha.

Eventi (pagina orfana): "Il Salumificio Fontana a Bad Windsheim - Germania, durante l'Altstadtfest (05 - 07 luglio 2013)".

Inglese: storia tradotta per intero (aggiunge "the four young sons" e "The Salumificio Fontana is now run by 3 brothers"), poi "Salumificio Fontana sells pork and beef, both fresh and frozen, vacuum-packed or in quarters, and other specialties."

Testi nelle etichette delle foto prodotto (leggibili): "Sopressa Veneta", "Salametto Turista", "Coppa di testa", "Coscia suino cotta al naturale", "Roastbeef cotto all'inglese", "Mortadella senza polifosfati", "Brunnenspeck", "I Sapori della Tradizione" (scatole di cotechino, stinco e zampone cotti), "Salumificio Fontana Este (PD) Tel. 0429/2164 - 4386".

Refusi e incongruenze da non riportare: "E' Giovanni" (È); "SOPRESSA" e "soppressaVeeneta" (nome file) accanto a "SOPRESSE"; "ed ha"; "sia fresca che congelata"; due telefoni scritti come "TEL. 0429 2164 4386 - FAX 0429 4386" (il 4386 è telefono in Contatti e fax nel piede e sul sito del Consorzio); "PROSCIUTTO VENETO DOP" nell'elenco e "VENETO BERICO EUGANEO DOP" nelle schede; "S.N.C." in logo, meta description e testi alternativi. Nel nuovo sito: **Salumificio Giovanni Fontana S.r.l.**, marchio "Salumificio Fontana", "Prosciutto Veneto DOP" (nome registrato "Prosciutto Veneto Berico-Euganeo").

Da riallineare con il cliente [DA CONFERMARE]: il sito dice barchessa "acquistata sul finire degli anni trenta"; Valsana (2025) riporta che Giovanni "acquista l'immobile" nel 1941 e che la barchessa è del 1910, dormitorio della Legione Euganea negli anni '30; Stayinveneto scrive "caserma militare dal 1933 al 1935". Chi conduce oggi l'azienda (il sito dice Giuseppe, Francesco e Bruno; Valsana dice Paola Fontana con il marito Marcello, con il padre Francesco ancora in azienda).

Testo pubblico utile (Valsana, blog 26/08/2025, citabile solo come fonte, non da copiare): suini "rigorosamente italiani, provenienti per il 90% da allevamenti veneti"; legatura a mano; "Lavoriamo tutto il maiale, come una volta"; macellazione interna fino agli anni '90; dalle finestre del salumificio si vede il Duomo; visite dal 2012 (un tour operator tedesco), studenti dell'Università di Padova e della Boston University, team building, corsi di affettamento. Marcello chiede di non descrivere l'azienda con la parola più abusata del settore (è in `PAROLE_VIETATE`) e propone "storia, studio, formazione; curiosità, sperimentazione; accoglienza, viaggi, amicizia": è una direzione di tono già scelta dal cliente.

## Cosa fanno e cosa vendono

| Categoria | Nomi in Prodotti | Schede con foto | Note |
|---|---|---|---|
| Stagionati | 14 | 15 | Prosciutto Veneto Berico-Euganeo DOP intero e disossato, crudo MEC, coppa, fiocco, pancette, salami, sopressa |
| Freschi | 10 | 4 | cotechini, salami da ferri, salsicce; zamponi crudi e bondiole solo per nome |
| Cotti | 20 | 16 | mortadella e prosciutto cotto senza polifosfati, porchetta, coppa di testa, stinco e zampone in scatola |
| Affumicati | 7 | 10 | pancette, lombo, speck, salsiccia Napoli, würstel |
| Commercio carni | 1 frase | 0 | carne suina e bovina fresca e congelata, in quarti o sottovuoto (anche categoria PagineBianche "Carni fresche e congelate") |

Fuori dal sito, da fonti pubbliche:
- **Arrosti nuovi** (Valsana, 2025): Porchetta cotta al naturale (circa 13 ore di cottura), Filetto cotto al naturale (7 ore), **Filetto della Timpa** (5 ore; paprika affumicata, pepe di Timut, coriandolo, avvolto in foglie di limone raccolte nel limoneto di famiglia sulla Timpa di Acireale). [Certo come fonte, DA CONFERMARE come gamma attuale]
- **Visite guidate e degustazioni**: Veneto Around Me, lun-ven partenze alle 10:00 e alle 15:30, kit (camice, calzari, berretto), visita ai luoghi di produzione del Prosciutto Veneto DOP, degustazione con vino e pane locali; Consorzio: "È possibile organizzare visite guidate e visite con degustazione previo appuntamento"; eventi con Stayinveneto (23 marzo e 26 ottobre 2024, 20 euro a persona, prezzo dell'organizzatore; un'immagine del 2026 annuncia un'edizione del 19 aprile [Probabile]) e con il Comune di Este ("Este da Gustare", 9 giugno 2025). Al termine si possono acquistare i prodotti; edificio storico con barriere architettoniche; parcheggio privato di fronte all'ingresso. [Certo]
- **Prosciutto Veneto DOP**: il sito lo mostra intero e disossato; Valsana (2025) scrive che "lo sviluppo della linea dei prosciutti crudi richiede tanto tempo e tante risorse, un processo da fare gradualmente" e che per questo non può ancora raccontarlo. Quanta produzione DOP c'è oggi e se è in vendita va chiesto. [DA CONFERMARE]
- **Vendita diretta** lun-ven 8.00-12.00 e 14.00-18.00 (scheda del Consorzio "Contatti e vendita diretta"). [Certo]
- **Marchi e appartenenze dichiarate**: socio del Consorzio di Tutela del Prosciutto Veneto Berico-Euganeo DOP (testata del sito e elenco produttori del Consorzio). Nessuna altra certificazione dichiarata. [Certo]
- Estero: evento a Bad Windsheim (Germania) nel 2013; contributo "Progetto SEI" di Venicepromex (internazionalizzazione) nel 2025, dal Registro nazionale aiuti. [Certo, uso commerciale DA CONFERMARE]

## Immagini usate oggi

Inventario completo con misure, soggetto, qualità e larghezza massima: `_prova/inventario-immagini.json` (86 file). Originali in `assets/originali/` (69 file, `manifest.json`), esterne in `assets/esterne/` (17 file, `manifest.json`).

| Tipo | Quantità | Misura nativa | Giudizio | Larghezza massima senza sgranare |
|---|---|---|---|---|
| Foto prodotto scontornate (PNG con trasparenza, still life da studio) | 45 | 450x450 | nitide, coerenti, etichette leggibili; mostrate oggi a 300-350 px | 450 px, 225 px CSS su retina |
| Banner di categoria (fotomontaggi su piano scuro, angoli arrotondati nel file) | 4 | 1211-1212x487 | puliti ma "pubblicitari"; oggi mostrati a 908 px | 1200 px, 600 su retina |
| Slide Home (logo e date fusi; foto aerea 1974 seppia) | 2 | 960x386 | testo dentro l'immagine; la foto 1974 è materiale d'archivio vero | 960 px; la 1974 ritagliata sopra la scritta |
| Foto storiche in bianco e nero (salami, uomo in camice, prosciutti) | 3 | 260x400 | belle, piccole, angoli arrotondati nel file | 260 px, 130 su retina |
| Strisce collage (Storia, Prodotti) e miniature categoria | 2 + 4 | 970x195, 381x219 | basse, ridondanti | non usabili |
| Logo testata, logo tondo, logo piede, castello, favicon "SF" | 5 | da 16 a 1186 px | raster, testata con "S.N.C." | serve il vettoriale |
| Sfondo con il logo ripetuto | 1 | 1800x6708, 2,6 MB | pesa più di metà della home | non usabile |
| Foto evento 2013 (compatta Canon) | 3 | 3072x2304 | amatoriali | non adatte |
| **Esterne: portale regionale Veneto Around Me** (stagionatura prosciutti di Stefano Aiti 2023; tagliere "FONTANA ESTE"; soppresse di Giovanni Milani con firma; crostini) | 4 | 1900x1267, 2560x1707, 1707x2560, 2560x1707 | le migliori disponibili; due con autore dichiarato | 1900-2560 px; permesso di cliente e autori |
| Esterne: logo tondo 2025 dal Consorzio | 1 | 400x400 | raster pulito | 200 px CSS su retina |
| Esterne di terzi: Valsana 2025 (ritratti di Paola e Marcello, laboratorio, legatura, spezie, stagionatura, Duomo dalla finestra) | 11 | 1460x1096 | servizio professionale, solo riferimento | non usabili senza licenza |
| Esterna di terzi: profilo Google, corridoio di stagionatura (2024) | 1 | 3060x4080 | buona, autore probabilmente terzo | non usabile |

Nessuna immagine del sito è mostrata più grande della sua misura (solo le bandierine 18 px a 20 px). Il problema è l'opposto: file grandi mostrati piccoli (miniature da 381 px mostrate a 63-130 px, prodotti da 450 px a 300 px, nella versione mobile a 142-164 px) e PNG pesanti dove basterebbe un JPEG. Facebook e Instagram dell'azienda esistono (`facebook.com/SalumificioGiovanniFontana`, `instagram.com/salumificiogiovannifontana`) ma non sono leggibili senza accesso: nessuna foto presa da lì.

Manca: una foto ampia e recente della sede o della corte su via Schiavin, ritratti della famiglia di proprietà del cliente, foto della sala visite e della degustazione, foto dei nuovi arrosti. Brief fotografico nel LEGGIMI.

## Problemi tecnici da segnalare al cliente

Misure prese il 6/10/2026 con Playwright (Chromium) e curl. Le richieste http passano da un relay, quindi i tempi sono indicativi; pesi e numero di richieste sono esatti.

1. **HTTPS non funzionante.** `https://www.salumificiofontana.it` presenta il certificato `CN=*.shellrent.com` (Sectigo, valido dal 25/09/2026 al 21/03/2027), che non copre il dominio: curl esce con errore 60 "no alternative certificate subject name matches", il browser mostra un avviso di sicurezza. Il sito funziona solo in http, quindi anche il modulo contatti invia nome, email e messaggio in chiaro. [Certo, `prove-tecniche.txt`]
2. **Due siti in uno, entrambi vecchi.** Desktop: nessun meta viewport, `body { min-width: 980px }`, testo a 12 px. Su iPad (user agent Safari iPadOS) la pagina resta larga 980 px e viene ridotta a 0,84; dal telefono in modalità "sito desktop" a 0,40. Telefoni (iPhone, Android, Samsung Internet, browser di Facebook): versione mobile del tema del 2012 con scrollWidth 390 corretto, ma senza logo (in alto c'è la scritta "www.salumificiofontana.it"), con il pulsante in inglese "Switch to Desktop Version", **senza piede** (niente indirizzo, email e P.IVA in nessuna pagina mobile) e con la home ridotta a una sola immagine di 310x125. [Certo, `attuale/*-390.png`, `*-ipad820.png`, `*-390desktop.png`, `crawl/ua.txt`]
3. **CMS fuori supporto.** `/administrator/manifests/files/joomla.xml`: `<version>3.8.10</version>`, `<creationDate>June 2018</creationDate>`. Mancano tutti gli aggiornamenti di sicurezza dei rami 3.9 e 3.10; Joomla 3 non ne riceve più da agosto 2023. Il file di versione e la pagina di accesso `/administrator/` sono pubblici. [Certo per la versione, Probabile per il rischio]
4. **Modulo contatti inutilizzabile.** Lo script del captcha (`https://www.google.com/recaptcha/api/js/recaptcha_ajax.js`, reCAPTCHA v1 chiuso da Google nel 2018) risponde 404; in console "Recaptcha is not defined" e il campo obbligatorio "Captcha *" resta vuoto. Il modulo non è stato inviato (divieto), ma senza captcha Joomla rifiuta l'invio. [Certo per il 404 e il campo vuoto, Probabile per l'invio]
5. **Mappa in errore.** La mappa Widgetkit carica Google Maps senza chiave (`NoApiKeys` in console) e mostra "Oops! Something went wrong. This page didn't load Google Maps correctly." sia su desktop che su mobile. [Certo, `08-contatti-1440.png`]
6. **Peso e richieste** (desktop 1440, peso trasferito):

| Pagina | Richieste | Peso | Versione mobile |
|---|---|---|---|
| Home | 67 | 4,45 MB | 39 richieste, 1,74 MB |
| Storia azienda | 69 | 4,30 MB | 40, 1,08 MB |
| Prodotti | 70 | 4,11 MB | 41, 0,94 MB |
| Stagionati | 82 | 6,68 MB | 52, 2,94 MB |
| Freschi | 71 | 4,81 MB | 41, 0,90 MB |
| Cotti | 83 | 7,36 MB | 53, 3,62 MB |
| Affumicati | 77 | 6,04 MB | 47, 2,26 MB |
| Contatti | 81 | 3,43 MB | 53, 0,71 MB |

   Lo sfondo `images/background.png` (motivo del logo ripetuto, 1800x6708) pesa **2,6 MB** su ogni pagina desktop: il 57% della home. I banner di categoria sono PNG da 1,0-1,2 MB, le foto prodotto PNG da 100-320 KB. Evento "load" tra 2,8 e 7,5 s (indicativo); HTML della home in 0,41 s. Ogni pagina carica jQuery e jQuery Migrate, Contatti anche MooTools. [Certo, `attuale/misure.json`]
7. **Privacy e cookie.** Nessuna informativa privacy, nessuna cookie policy, nessun banner: alla prima visita Google Analytics imposta `_ga`, `_gid`, `_gat` e `_ga_DFMERP30PF` senza consenso (codice `UA-46512978-1` nella pagina). Il modulo contatti non ha informativa né consenso. [Certo]
8. **Dati societari.** Il piede desktop riporta la P.IVA 00228620282 ma la ragione sociale scritta è "F.LLI FONTANA S.N.C." (in immagine e nelle meta description); "S.r.l." non compare in nessuna pagina; mancano il numero di iscrizione al Registro Imprese (REA) e il capitale sociale, che l'art. 2250 c.c. chiede alle società di capitali anche nel sito internet. Nella versione mobile non c'è nessun dato societario. [Certo]
9. **Contenuti fermi.** Anno più recente nel testo: 2009 ("Mario è scomparso nel settembre 2009"); unica notizia: un evento del luglio 2013 rimasto fuori dal menu; nessun copyright nel piede; file caricati tutti il 23/09/2018. La pagina Freschi mostra 4 prodotti su 10 nominati. Visite, degustazioni, nuovi arrosti e la terza generazione non ci sono. [Certo]
10. **Testi chiusi in immagini.** Date della storia (1919, 1941, 1974), nome dell'azienda, appartenenza al Consorzio e logo sono solo dentro immagini: non leggibili dai motori di ricerca né dai lettori di schermo. La home ha 0 caratteri di testo nel corpo. [Certo]
11. **SEO di base.** Titoli delle pagine "HOME", "STORIA AZIENDA", "COTTI" (senza il nome dell'azienda); nessun H1 tranne in Contatti; 20 immagini su 22 senza testo alternativo in Stagionati (21 su 23 in Cotti); `robots.txt` blocca `/images/`, quindi le foto prodotto non entrano in Google Immagini; nessuna sitemap (`/sitemap.xml` va in 404); `salumificiofontana.it` senza www non reindirizza (contenuti doppi); pagine inglesi con nomi in italiano. [Certo]
12. **Nessun collegamento ai canali dell'azienda.** Nessun link a Facebook, Instagram, alla scheda del Consorzio o all'offerta sul portale regionale. [Certo]
13. **Omonimi.** `salumificiofontana.com` è un'altra azienda (Salumificio Fontana, Petilia Policastro KR, P.IVA 03022720795, con negozio online); Attilio Fontana Prosciutti di Montagnana (`fontanaprosciutti.it`, con ogni probabilità il ramo del fratello Attilio citato nella Storia [Probabile]) è nello stesso elenco del Consorzio; esistono Fontana Ermes (Parma) e altri "Fontana". Chi cerca il marchio si confonde: il nuovo sito deve dire sempre "Salumificio Giovanni Fontana, Este". [Certo]

Link interni rotti: nessuno (tutte le 20 pagine trovate rispondono 200); i file inesistenti sotto `/images/` reindirizzano a `/it/images/...` e poi 404. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | SALUMIFICIO GIOVANNI FONTANA S.R.L. | VIES (servizio UE di verifica delle partite IVA), 06/10/2026: partita IVA valida |
| P.IVA e codice fiscale | 00228620282 | VIES; piede del sito |
| Sede | Via Schiavin 9, 35042 Este (PD) | VIES; sito; Consorzio |
| Telefono | 0429 2164 (+39 0429 2164) | sito, Consorzio, Google, Veneto Around Me |
| Secondo numero | 0429 4386: telefono in Contatti, fax nel piede e sul Consorzio | [DA CONFERMARE] se è ancora attivo e se è fax |
| Email | info@salumificiofontana.it | sito, Consorzio, Veneto Around Me |
| PEC | salumificiofontana@interfreepec.it | visurissima.it (dati Registro Imprese); [DA CONFERMARE] su INI-PEC prima dell'invio |
| REA, capitale sociale | PD 88891, 296.000 euro i.v. | visurissima.it |
| Codice SDI | M5UXCR1 | aziende.it, visurissima.it |
| Iscrizione, ATECO | 13/09/1961 (inizio attività; visurissima indica iscrizione 11/12/1961), 10.13 produzione di prodotti a base di carne | aziende.it, visurissima.it |
| Ricavi e risultato | 2021: 1.980.920 euro, utile 3.344; 2022: 2.165.576, perdita 167.555; 2023: 2.038.260, perdita 198.947; **2024: 1.287.443, perdita 250.377** | visurissima.it (Registro Imprese, aggiornato al 06/10/2026); 2023 anche su aziende.it |
| Dipendenti | 17 (2023), **11 (2024)**; Valsana 2025: "oltre a loro in azienda lavorano altre 8 persone" | visurissima.it; Valsana |
| Orari | lun-ven 8.00-12.00 e 14.00-18.00 (vendita diretta); sabato [DA CONFERMARE] | Consorzio; Google conferma martedì 08-12, 14-18 |
| Visite guidate | lun-ven ore 10:00 e 15:30, su prenotazione | Veneto Around Me; Consorzio |
| Anni | 1919 inizio a Montagnana con il fratello Attilio; 1941 Este; 1951 guida di Lea Vezzù; 1974 foto dello stabilimento | sito (testo e immagini) |
| Persone | Giovanni Fontana (classe 1890), Lea Vezzù; figli Giuseppe, Francesco, Bruno, Mario (sito); oggi Paola Fontana (terza generazione, amministrazione e accoglienza) e il marito Marcello (produzione dal 2015, accoglienza), Francesco ancora in azienda, Mauro in lavorazione | sito; Valsana 26/08/2025; Stayinveneto [DA CONFERMARE per l'uso dei nomi] |
| Profilo Google | "Salumificio Giovanni Fontana SRL", categoria "Negozio di prosciutti", rivendicato dal proprietario | Google Maps, place id ChIJ47aknuIdf0cRkwXbuKiFUQU |
| Social | Facebook `SalumificioGiovanniFontana`, Instagram `@salumificiogiovannifontana` | ricerca web; contenuti non letti (login) |
| Consorzio | socio del Consorzio di Tutela del Prosciutto Veneto Berico-Euganeo DOP | sito; prosciuttoveneto.it/produttori |

Capacità di spesa: tre esercizi in perdita (2022-2024) e ricavi 2024 scesi del 37% sul 2023. Valsana riporta la scelta di sviluppare la linea dei crudi "gradualmente ... per evitare di mettere in crisi finanziariamente l'azienda". La proposta va dimensionata di conseguenza.

## URL vecchi (per `plugin/redirect-301.csv`)

```
/                                  (oggi 301 verso /it/)
/it
/it/
/it/storia-azienda
/it/prodotti
/it/prodotti/stagionati
/it/prodotti/freschi
/it/prodotti/cotti
/it/prodotti/affumicati
/it/contatti
/it/8-eventi
/it/8-eventi/4-eventi
/it/component/search/
/en
/en/
/en/company-history
/en/products
/en/products/cured
/en/products/fresh
/en/products/cooked
/en/products/smoked
/en/contacts
/index.php?option=com_content&view=article&id=2    (Prodotti)
/index.php?option=com_content&view=article&id=3    (Home)
/index.php?option=com_content&view=article&id=4    (Eventi 2013)
/index.php?option=com_content&view=article&id=8    (Storia)
/index.php?option=com_content&view=article&id=13   (Stagionati)
/index.php?option=com_content&view=article&id=14   (Freschi)
/index.php?option=com_content&view=article&id=15   (Cotti)
/index.php?option=com_content&view=article&id=16   (Affumicati)
/index.php?option=com_content&view=article&id=21   (Contatti senza mappa)
```
Più l'host senza www (`http://salumificiofontana.it/...`) da reindirizzare tutto su `https://www.salumificiofontana.it/`.

## Fonti

- Sito attuale: http://www.salumificiofontana.it/it/ (crawl in `_prova/crawl/`, 20 pagine + 9 articoli per id)
- VIES: https://ec.europa.eu/taxation_customs/vies/rest-api/ms/IT/vat/00228620282
- Registro Imprese tramite: https://www.visurissima.it/aziende/SALUMIFICIO-GIOVANNI-FONTANA-S.R.L._00228620282.html e https://www.aziende.it/salumificio-giovanni-fontana-s-r-l
- Consorzio: https://www.prosciuttoveneto.it/produttori/salumificio-fontana-s-r-l/
- Veneto Around Me (Regione Veneto): https://venetoaroundme.regione.veneto.it/it/node/101472
- Valsana, "Incontri con il produttore", 26/08/2025: https://www.valsana.it/blog/salumificio-giovanni-fontana
- Stayinveneto: https://www.stayinveneto.com/experiences/246-sabato-23-marzo-prosciutto-experience-salumificio-fontana-este; PadovaOggi 09/10/2024
- Comune di Este, comunicato "Este da Gustare" (6/6/2025): https://este-api.cloud.municipiumapp.it/s3/2661/allegati/cs_este-da-gustare.pdf
- Google Maps, scheda "Salumificio Giovanni Fontana SRL"; PagineBianche
