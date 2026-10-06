# 01. Analisi del sito attuale (www.iltorchioantico.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare, **[DA CONFERMARE]** dato da chiedere al cliente prima di usarlo.
Materiale di lavoro: pagine scaricate in `_prova/crawl/pagine/` (145 file HTML), testi estratti in `_prova/crawl/testi_it.txt`, misure Playwright in `_prova/attuale/misure-1440.json` e `misure-390.json`, screenshot in `_prova/attuale/`, inventario foto in `_prova/inventario-immagini.json`.

## In breve

- Sito statico a tabelle, largo 1000 px fissi, senza meta viewport in nessuna delle 145 pagine: da telefono la pagina viene rimpicciolita al 39% (scrollWidth 1001 su 390 px) e il menu da 16 px appare a circa 6 px. Colori blu `#1B3776` e giallo `#FCEB08`, Arial, logo in corsivo giallo. [Certo]
- Contenuti fermi alla primavera 2024: in home "Prossimi eventi" e "Menù Turistici" mostrano ancora "Pasqua 2024 ... Domenica 31 Marzo"; l'ultima news è San Valentino 2024; piede "© 2008 - 2024". Le foto degli eventi arrivano da `fotonews.iltorchioantico.it`, dominio che non esiste più (NXDOMAIN): 2 immagini rotte in home, 19 in Eventi, 18 in News, 10 in Turismo a tavola, 8 in Partner. [Certo]
- Il sito è stato ricostruito da una copia d'archivio: `ristorante.htm` carica i pulsanti Facebook e Twitter da `web.archive.org` (istantanea del 5 ottobre 2013) e un iframe della pagina Catering cita il dominio `webarchive.iltorchioantico.com`. Il certificato HTTPS più vecchio è del 27 gennaio 2024. [Certo per i riferimenti, Probabile per la ricostruzione]
- Il patrimonio vero è il luogo: le barchesse e il portico di Villa Godi Malinverni (prima villa di Palladio), il torchio di legno del 1780 che dà il nome, il giardino. Le foto ci sono (circa 80 del ristorante, della cucina e degli allestimenti, più 64 della villa) ma sono del 2008-2013 e piccole: 620-690 px la galleria, 1000-1010 px solo in strisce basse (1000x330, 1010x545). Nessuna regge un'apertura a tutta larghezza. [Certo]
- Le uniche foto recenti e di livello (2025, 930-1400 px, fotografo Marco Gnata / Artelugo) sono su villagodi.com, sito di un'altra società (Palladium SAS): da usare solo con permesso. [Certo]
- Società solida per un ristorante: Le Colline del Palladio S.r.l., 519.029 euro di ricavi nel 2024, 18 dipendenti, PEC nota. La P.IVA non compare nel piede del sito. [Certo]

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home IT | `/` (doppioni identici `/index.html`, `/index.htm`) | testo istituzionale, "Prossimi eventi" e "Menù Turistici" fermi a Pasqua 2024 con foto rotta, tabella orari, colonna laterale con contatti, foto staff, modulo "Richiesta informazioni" |
| Ristorante | `/ristorante.htm` | testo "Dal 1960 nelle Barchesse...", tabella orari, posti, attrezzature, slider di 30 foto (2,6 MB) |
| Matrimoni & Cerimonie | `/banchetti_nozze.htm` | due paragrafi, slider di 9 foto |
| Catering & Banqueting | `/catering_banqueting_vicenza.html` | quattro paragrafi (matrimoni, privati, aziende), slider di 9 foto, pulsante "Posta" di X |
| Gallery | `/foto_gallery_ristorante_catering_vicenza.html` | slider di 30 foto, nessun testo |
| Preventivi | `/info_preventivi.html` | modulo con data evento, numero ospiti, location (Villa Godi Malinverni, Ristorante Il Torchio Antico, Altra) |
| Eventi | `/eventi_da_non_perdere.html` | elenco 2020-2024, ultimo "2024-03-31: Pasqua 2024", Pasqua 2023 ripetuta tre volte, tutte le miniature rotte |
| News | `/news_eventi.html` | elenco 2018-2024, ultima "2024-02-14: San Valentino 2024", miniature rotte |
| Turismo a tavola | `/menu_turismo_a_tavola.html` | menu 2012-2024 (Lonedo, Palladiano, Primavera-Estate, alla carta 2020) |
| Offerte & promozioni | `/offerte_e_promozioni.html` | "Al momento non vi sono promozioni in corso" |
| Come arrivare | `/come_arrivare.html` | mappa OpenStreetMap (Leaflet), distanze dalle città |
| Partner | `/partner.htm` | 8 fornitori (fotografi, musica, viaggi, candele, vini), loghi rotti, titolo quasi invisibile |
| Dettagli evento | `/news_eventi_NNN_*.htm(l)`, `/eventi_da_non_perdere_NNN_*.htm`, `/menu_turismo_a_tavola_NNN_*.htm` | 55 pagine, ognuna in doppia copia `.htm` e `.html` per l'ultima |
| Aiuti di Stato | `/news_eventi_191_aiuti_di_stato.htm` | unica pagina con ragione sociale e codice fiscale |
| Inglese | `/english/` (10 pagine + 40 dettagli evento) | traduzione delle pagine principali; i box eventi restano in italiano; i 40 dettagli evento hanno il titolo "Villa Godi Malinverni in Lugo di Vicenza" |
| Tedesco, spagnolo, francese | `/de/`, `/es/`, `/fr/` (7-8 pagine ciascuna) | traduzioni delle pagine principali |
| Sito satellite catering | `http://www.torchiocatering.it/` (anche `.com`), 6 pagine | sito del 2014 ("Torchio Catering © 2014"), solo http, linkato dal piede alla voce "Catering" |

Non esistono: `robots.txt`, `sitemap.xml` (404), pagina privacy, pagina cookie.

## Testi reali (verbatim, con i refusi originali)

Home:
1. Titolo testata (H1, uguale in tutte le pagine): "Ristorante & Catering a Lugo di Vicenza"
2. "Il Torchio Antico è una cornice unica per i vostri pranzi, colazioni di lavoro, cene aziendali, semplici rinfreschi, matrimoni, battesimi, comunioni o per uno splendido pranzo nuziale."
3. "Nelle antiche e suggestive barchesse di Villa Godi Malinverni - prima villa di Palladio del 1542 - da oltre 50 anni il Ristorante Torchio Antico offre ai suoi ospiti splendidi ed indimenticabili momenti di festa e di serenitè; è la cornice ideale per matrimoni, battesimi, comunioni e tutte le occasioni di festa con amici e parenti. Le sale interne e la barchessa esterna restano unici per pranzi e cene con amici."
4. "La qualità del servizio, la grande professionalitè del nostro staff sono oggi a disposizione di tutti i clienti anche in altra location, dalla casa privata alle ville, con il servizio di banqueting: il Torchio Antico offre un catering personalizzato di grande serietà e qualità, con la sicurezza di poter degustare le pietanze di una cucina raffinata e sempre al vostro servizio presso il ristorante aperto al pubblico."
5. Tabella: "Orario di servizio: Aperto tutto l'anno - mezzogiorno e sera / Giorno di chiusura: Lunedì e Martedì / Chiusura per ferie: 1 settimana Novembre e 1 settimana Gennaio / Posti a sedere: Sale interne: 150 - Porticato: 180 - Giardino: 300 / Tipo di cucina: Cucina veneta con menu stagionali e prodotti del territorio"
6. Colonna laterale: "Ristorante Il Torchio Antico / Via Palladio, 46 - Lugo di Vicenza (VI) / Info & Prenotazioni / Telefono: +39.0445860358 / Cellulare: +39.3393429942 / Skype: villagodi / Mail: info@iltorchioantico.com"

Ristorante (`/ristorante.htm`):
7. "Dal 1960 nelle Barchesse realizzate dal Palladio, dove un tempo vi erano le scuderie, si trova oggi il Ristorante Il Torchio Antico, nome che nasce dalla presenza di un bellissimo antico Torchio del 1780."
8. "Il Torchio Antico è una cornice unica per i Vostri pranzi, colazioni di lavoro, cene aziendali, semplici rinfreschi, matrimoni, battesimi, comunioni o per una semplice cena romantica. Il felice connubio tra arte, natura ed eleganza crea una piacevole atmosfera, unica ed indimenticabile, dove una dolce sensazione di tranquillità Vi accompagna durante la permanenza nel rustico."
9. "Attenzione particolare è dedicata alla qualità, alla stagionalità ed alla tipicità dei cibi: piatti semplici, ma capaci di trasmettere delicate sensazioni grazie all'accurata preparazione che i nostri chef sono impegnati giornalmente a svolgere."
10. In più rispetto alla home: "Attrezzature: Impianto audio-video per meeting, videoproiettore / Carte di credito: Tutte"
11. Versione inglese, con un dettaglio che manca in italiano: "It takes its name from the beautiful antique press, dating 1780, which can be seen under the magnificent portico."

Matrimoni & Cerimonie (`/banchetti_nozze.htm`):
12. Titolo: "Banchetti di Nozze, Matrimoni, Cerimonie". Sottotitolo: "Una scenografia [aggettivo della lista PAROLE_VIETATE, omesso qui] per il Vostro Matrimonio"
13. "Immerso nel verde domina la Valle dell'Astico con un paesaggio naturale di rara bellezza: Ristorante Il Torchio Antico è particolarmente consigliato per il vostro banchetto nuziale per l'ampiezza delle sue sale e per il lungo porticato. Il ristorante Il Torchio Antico in questa occasione vi riserva il locale e vi propone un menu personalizzato."
14. "Nel periodo estivo si utilizza la barchessa all'esterno, creando un'atmosfera di sicuro effetto, donando un tocco prezioso al vostro giorno più importante. Il ristorante Il Torchio Antico inoltre può occuparsi degli addobbi floreali e dell'ingaggio di gruppi musicali o solisti."

Catering & Banqueting (`/catering_banqueting_vicenza.html`):
15. "Per Matrimoni o Cerimonie, il banqueting de Il Torchio Catering può servire i propri piatti all'interno delle Vostre dimore o all'interno di indimenticabili Ville, tra le quali Villa Godi Malinverni, Villa Capra Bassani, il Castello di Thiene o il Monastero di San Biagio."
16. "Per i Privati, il servizio Catering de Il Torchio Antico è la scelta giusta per ogni festa, dal Battesimo al Compleanno, dalla Cresima alla Laurea: la ristorazione a domicilio de Il Torchio Antico vi offrirà professionalità e competenza direttamente a casa vostra"
17. "Per le Aziende, Cocktail, buffet, cene di gala, presentazione di prodotti: lo staff de Il Torchio Antico di Lugo di Vicenza è a completa disposizione del Vostro Business. La decennale esperienza nell'organizzazione di eventi, dalle fiere a convegni, dai meeting alle sfilate, è la nostra proposta vincente"

Preventivi (`/info_preventivi.html`):
18. "Compila il form per ricevere un preventivo personalizzato". Campi: Nome, Cognome, Città, Provincia, E-Mail *, Telefono, Data evento, Nr Ospiti, Location (Villa Godi Malinverni / Ristorante Il Torchio Antico / Altra), Richiesta, "Inserisci la somma di 1 + 9".
19. "I dati personali forniti nel presente form saranno trattati nel rispetto delle disposizioni di cui al D. Lgs. 196/2003 e successive modificazioni"

Come arrivare: "Distanza dalle principali località turistiche: Vicenza: 28 km / Marostica: 16 km / Bassano del Grappa: 24 km / Padova: 60km / Verona: 80 km / Venezia: 92 km". Mappa centrata su 45.74633, 11.53486.

Offerte: "Al momento non vi sono promozioni in corso / Torna presto a trovarci per scoprire le nostre offerte."

Partner (`/partner.htm`), titolo "Partner Villa Godi Malinverni - Lonedo Lugo di Vicenza": Torchio Catering ("La grande qualità e professionalità di uno staff qualificato al vostro servizio."); CAPOZZO VIAGGI, Breganze ("progetto LISTE DI NOZZE per Villa Godi Malinverni"); Confraternita De. Co. ("La Magnifica Confraternita dei Ristoratori De.Co. nasce da un'idea dei ristoratori Confartigianato della provincia di Vicenza che hanno sempre creduto e condiviso un obiettivo comune: quello di promuovere il nostro territorio in tutte le sue forme ed espressioni."); WeAreFamous (Pigato Paolo Photography); Candele e Affini (Vicenza); Black & Wine (Malo); Artefoto snc di Rita e Pierluigi Abriani, Servizi fotografici (Lugo di Vicenza); Antonio Gallucci, Jazz Music.

Menu (Turismo a tavola, testi integrali in `_prova/crawl/testi_it.txt`):
20. Pasqua 2024, l'ultimo evento: "IL TORCHIO ANTICO - VILLA GODI MALINVERNI Domenica 31 Marzo ore 12h00 / CALICE DI PROSECCO CON APERITIVI / TARTARA DI VITELLO SCOTTATA CON INSALATA DI ASPARAGI BIANCHI DI BASSANO, UOVO DI QUAGLIA E FROLLA DI PARMIGGIANO / GNOCCHI DI POLENTA CON RAGU' DI CORTILE E CRESCIONE FRESCO / RISOTTO MANTECATO CON ASPARAGI VERDI, PISELLI E SEPPIOLINE / ... / ACQUE MINERALI E VINI IN ABBINAMENTO BREGANZE DOC / € 50 p.p. / Visita a Villa Godi Malinverni e Musei omaggio / Bambini under 12 con menù baby (aperitivi, lasagne al ragù, cotoletta con patate, colomba): €30 / Caparra alla conferma 50% / Ristorante Il Torchio Antico / Via Palladio 44, Lugo di Vicenza"
21. Menù Lonedo (2017): "servizio al tavolo per piccoli gruppi, individuali e coppie ... Il menù si compone di un primo, un secondo, un dolce a scelta tra quelli proposti ... Bucatini alla Lughese ... Galletto arrosto con patate di Posina e Insalata Oppure Marsoni fritti "dell'Astico" con Polenta di Mais "Marano" ed Insalata ... Costo "Palldiobynight Card" Euro 20,00 p.p. ... Costo al pubblico a partire da Euro 28,00 p.p."
22. Menu Turistico Palladiano (2013): "Un menu alla scoperta degli antichi sapori, verdure ed alimenti del '500 (prima dell'influenza Americana) / Saor de Trutelle (Avagnotti di Trotella in Saor) / Riso, Capretto, Pisacan e Raise de Fossi (Risotto al Capretto, Topinambur e Tarassaco) / Tagliatura de Carne salada e Pastinaca / ... / Bussolà del Fasolo al Zabaione ... in omaggio una Stampa su Andrea Palladio" (25,00 o 27,00 euro con vino).
23. Menu alla carta (26/11/2020), con prezzi: per esempio "Bucatini alla lughese d.e.co. in cocotte: € 12", "Baccala' alla vicentina con polenta alla brace: € 22", "Filetto di manzo alla vicentina: € 23", "Crocchetta di zucca e castagne di Lonedo con fonduta al Morlacco e Blu61 ai mirtilli rossi: € 15", "Coperto con aperitivo offerto della casa: € 3 p.p." e la nota "in assenza di prodotti freschi, verranno utilizzati prodotti congelati/surgelati. Per intolleranze/allergie, il personale e' a Vostra disposizione."
24. Riapertura (20/05/2020): "Da venerdì 22 maggio riapriamo in massima sicurezza. Il grande Portico Palladiano, i giardini di Villa Godi Malinverni e le ampie scuderie potranno accoglierVi nel rispetto della distanza con la nostra cucina tradizionale veneta."
25. Capodanno 2018: "Vi aspettiamo al cenone di Capodanno all'interno delle scuderie di Villa Godi Malinverni, Ristorante Il Torchio Antico." Natale 2018: "il tradizionale ed elegante pranzo di Natale sarà servito all'interno dei Saloni Affrescati di Villa Godi Malinverni ... Aperitivi a buffet nelle vecchie cucine del Cinquecento".

Sito satellite www.torchiocatering.it (2014):
26. "Una cucina espressa in azienda, per festeggiare le ricorrenze, in occasione di meeting e di convegni o di inaugurazioni." / "Perchè anche l'azienda profuma di casa, di famiglia e di cucina."
27. "Un servizio esclusivo di ristorazione a domicilio, per un banchetto o un ricevimento presso le vostre case. Una cucina tradizionale, la grande qualitàei prodotti selezionati con la grande professionalità vi accompagneranno a tavola con i vostri ospiti, a casa, in villa, in azienda, in ogni occasione di festa. Compleanni, battesimi, comunioni, cresime, diciottesimi, lauree ..."
28. Contatti: "Le Colline del Palladio srl / Villa Godi Malinverni / Via Palladio 44 / 36030 Lugo di Vicenza (VI) - Italy"

Fonte terza, solo per confronto (villagodi.com, pagina "Ristorante Il Torchio Antico", Palladium SAS):
29. "Dove un tempo sorgevano le scuderie, nella Barchessa palladiana del 1533, nel 1968 sono state allestite dallo stesso proprietario, il prof. Malinverni, una Taverna ed una Tavernetta con un servizio di bar e ristorante ... La Taverna può contenere fino a 160 persone; durante il periodo estivo anche il grande sottoportico può accogliere altre 100 persone e così il prato antistante." e in home "da oltre 60 anni il Ristorante Torchio Antico". Contraddice "Dal 1960" e "da oltre 50 anni" del sito del ristorante e i 150/180/300 posti: vedi Da confermare.

Refusi e incoerenze da non riportare: "serenitè", "professionalitè", "PARMIGGIANO", "SALMOME AFFUMICATO", "Palldiobynight Card", "Appuntameno in giardino", "avrá", "Topinanbur", "Selvatco", "qualitàei prodotti", "Banquenting" (alt), "stafff" (firma); caratteri rotti in 12 pagine ("Bussol�", "Caff�", "venerd�") e "CittÃ" nel modulo laterale delle pagine di dettaglio. Il nome compare come "Ristorante Il Torchio Antico", "Ristorante Torchio Antico", "Il Torchio Antico", "Torchio Catering", "Il Torchio Catering", "TorchioCatering": nel nuovo sito **Il Torchio Antico** (e "Il Torchio Antico, catering" per il servizio esterno, [DA CONFERMARE] se il marchio Torchio Catering va tenuto).

## Cosa fanno (servizi, spazi, cucina)

| Servizio | Cosa dicono le fonti | Fonte |
|---|---|---|
| Ristorante aperto al pubblico | pranzo e cena, aperto tutto l'anno, chiuso lunedì e martedì, ferie 1 settimana a novembre e 1 a gennaio; Google: mercoledì-domenica 9-23:30 | home, ristorante.htm, scheda Google |
| Matrimoni e banchetti | il locale riservato agli sposi, menu personalizzato, barchessa esterna d'estate, addobbi floreali e musica su richiesta | banchetti_nozze.htm |
| Cerimonie e feste | battesimi, comunioni, cresime, compleanni, lauree, diciottesimi | home, catering, torchiocatering.it |
| Catering e banqueting | a domicilio, in ville (Villa Godi Malinverni, Villa Capra Bassani, Castello di Thiene, Monastero di San Biagio), in azienda (cocktail, buffet, cene di gala, presentazioni, fiere, convegni, sfilate) | catering_banqueting_vicenza.html, torchiocatering.it |
| Pranzi di lavoro e meeting | colazioni di lavoro, cene aziendali; impianto audio-video e videoproiettore | home, ristorante.htm |
| Menu a tema e turistici | Natale e Capodanno "con Palladio", Pasqua, San Valentino, Festa della donna, Carnevale; Menu Palladiano, Menu Lonedo, degustazione di asparagi; spesso con visita alla villa e ai musei inclusa | eventi, news, turismo a tavola |

Spazi: sale interne 150 posti, porticato 180, giardino 300 (sito del ristorante); il portico della barchessa con colonne e il torchio del 1780; il giardino con la vera da pozzo; le sale affrescate della villa per alcuni eventi (Natale 2018 "nei Saloni Affrescati"). [Certo per quanto dichiarato, DA CONFERMARE i numeri]

Cucina: "Cucina veneta con menu stagionali e prodotti del territorio". Prodotti nominati nei menu: asparagi bianchi di Bassano, Morlacco del Grappa, tartufo nero dei Berici, broccolo Fiolaro, castagne e limone di Lonedo, mais Marano, patate di Posina e di Rotzo, Asiago, soppressa, baccalà alla vicentina, marsoni dell'Astico, bucatini alla lughese De.Co., vini Breganze DOC, colomba di Oliviero Olivieri. Prezzi storici: Pasqua 2024 50 euro, Pasqua 2019 45 euro, menu alla carta 2020 da 5 a 24 euro a piatto. Nessun prezzo attuale: [DA CONFERMARE] qualsiasi prezzo.

Marchi e certificazioni: nessuna certificazione dichiarata. Compare la Confraternita De.Co. (ristoratori Confartigianato Vicenza) tra i partner e i "Bucatini alla lughese d.e.co." nel menu. [Certo]

## Immagini usate oggi

La cartella `/images/` del server ha l'elenco dei file aperto: 405 file dal 2008 al 2024, molti del vecchio sito della villa (che stava sullo stesso server). Scaricati tutti; 151 foto utili copiate in `assets/originali/` con nomi parlanti, inventario completo (soggetto, misure, larghezza massima, uso, diritti) in `_prova/inventario-immagini.json`.

| Tipo | Quantità | Misura | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Testate 1000x330 del ristorante (portico apparecchiato, sala interna ad archi rossi) | 2 (+1 eventi) | 1000x330 | discrete ma basse e compresse (100-120 KB) | strisce o mezza larghezza; a tutta larghezza su 1440 sgranano |
| Galleria del ristorante (`torchio_antico_NNb`) | 30 + 5 versioni 2008 diverse | 627-713 px (3 verticali 354-435 px) | foto 2008-2013, luce vera del luogo; le migliori: portico di sera con il torchio, portico apparecchiato, giardino col pozzo, staff sulla scalinata | mezza larghezza o colonna fino a circa 690 px (345 px su retina) |
| Il torchio del 1780 (`ristorante_3b`) | 1 | 421x480 | soggetto identitario, nitida | colonna stretta o dettaglio |
| Catering e cucina (vassoi, buffet, mise en place) | 14 | 620-690 px | piatti datati (specchi dorati, sushi), mise en place buona | dettagli piccoli |
| Allestimenti e matrimoni (`banchetti_NNb`) | 26 | 600-620 px | in gran parte nel giardino e nelle sale della villa; sposi riconoscibili in 4 | galleria piccola, con liberatoria per le persone |
| Sito torchiocatering.it | 13 | 630-1010 px | le più larghe del materiale aziendale: giardino con aiuole 1010x545, salone affrescato 1010x545, sposi sotto il portico 1010x545 (mossa) | mezza larghezza fino a 1010 px |
| Villa Godi Malinverni (affreschi, sale, parco, museo, incisioni, banner) | 64 | 300-1000 px | buone per il contesto, ma soggetto e probabilmente diritti della villa | [DA CONFERMARE] con il cliente; non usate come foto del ristorante |
| Logo: scritta gialla su blu 295x49 JPG; marchio col torchio e quattro stelle 227x95 JPG | 2 | minuscoli, raster | serve il vettoriale | riferimento per ridisegno o richiesta al cliente |
| Foto staff 235x225 nella colonna laterale | 1 | 235 px | doppione piccolo di `torchio_antico_20b` (642x430) | usare la 642 |

Riepilogo: circa 80 foto del ristorante, della cucina e degli allestimenti alla massima risoluzione trovata. La larghezza massima reale è **690 px** per le foto normali e **1000-1010 px** solo per strisce basse (rapporto 3:1 o 1,85:1). Su schermi retina la metà. Nessuna foto adatta a un'apertura a tutta pagina. [Certo]

Foto fuori dal sito (`assets/esterne/manifest.json`):
- villagodi.com, pagina del ristorante: 8 foto del 2025 (portico apparecchiato e crudi a 1400x787, catering e salone a 930x620), EXIF "GNATA", nel piede "Credits Foto: Marco Gnata/ARTELUGO". Pubblicate da Palladium SAS, altra società: **materiale di terzi**, da usare solo con permesso del cliente e del fotografo. Una nona foto (cuoco che impiatta) ha l'aspetto di un'immagine di repertorio: esclusa.
- Scheda Google "Il Torchio Antico": 70 foto 2019-2026 fino a 4032x3024, scattate da utenti con lo smartphone (piatti, visite alla villa; una mostra il torchio sotto il portico). Non scaricate in alta risoluzione: non sono del cliente.
- Facebook (`facebook.com/iltorchioantico`) chiede l'accesso; matrimonio.com (due schede, ristorante e banqueting) risponde 403; nessun profilo Instagram del ristorante (l'icona nelle pagine inglesi porta a `instagram.com/VillaGodi`).
- Wayback Machine: il 6/10/2026 non raggiungibile da qui (connessione chiusa, poi 429). Il server conserva comunque anche le versioni 2008 (file `.jpg.1`) alla stessa misura: improbabile trovare foto più grandi in archivio. Da riprovare per le locandine degli eventi su `fotonews.iltorchioantico.it`.

Foto da chiedere o da fare (per il LEGGIMI): originali delle foto 2025 di Artelugo; il portico e il torchio di giorno e di sera; il giardino apparecchiato; le sale interne; piatti di stagione; lo staff oggi; il logo in vettoriale.

## Problemi tecnici da segnalare al cliente

Misure del 6/10/2026 con Playwright (Chromium) e curl, attraverso un proxy: i tempi sono indicativi.

1. **Telefono**: nessuna delle 145 pagine ha il meta viewport. A 390 px la pagina è larga 1001 px (`scrollWidth` 1001, scala 0,39): menu da 16 px visto a circa 6 px, colonna contatti a 15 px vista a circa 6 px, piè di pagina a 10 px visto a circa 4 px. Prova: `_prova/attuale/01-home-390-telefono.png`, `03-matrimoni-390-telefono.png`, `11-come-arrivare-390-telefono.png`. I numeri di telefono non sono cliccabili (0 link `tel:` nel sito). [Certo]
2. **Contenuti fermi**: home con "Pasqua 2024 ... Domenica 31 Marzo" in "Prossimi eventi" e in "Menù Turistici"; Eventi con ultimo evento 2024-03-31 e "Pasqua 2023" ripetuta tre volte; News con ultima voce 2024-02-14; Offerte "Al momento non vi sono promozioni in corso"; piede "© 2008 - 2024". [Certo]
3. **Immagini rotte**: le miniature degli eventi e i loghi dei partner vengono da `fotonews.iltorchioantico.it`; `dns.google` risponde NXDOMAIN per `iltorchioantico.it`, `fotonews.` e `fotogallerynews.`. Al loro posto si legge il testo alternativo: 2 in home, 19 in Eventi, 18 in News, 10 in Turismo a tavola, 8 in Partner, 1 per dettaglio. [Certo]
4. **Errori JavaScript a ogni caricamento** in 13 pagine su 14 misurate, sia a 390 sia a 1440: home, inglese e offerte "Unexpected token ','" (il conto alla rovescia in testata ha la data vuota: `new Date(,  - 1 , , 23, 59, 59)`); ristorante, matrimoni, catering, gallery, preventivi "SyntaxHighlighter is not defined"; eventi, news, turismo, partner, dettagli "Invalid or unexpected token". [Certo]
5. **Pagine ricopiate dall'archivio**: `ristorante.htm` carica i widget Facebook e Twitter da `web.archive.org/web/20131005123804/...` (bloccati, risposta 502 e ERR_BLOCKED_BY_ORB); l'iframe Facebook di Catering cita `webarchive.iltorchioantico.com`. [Certo]
6. **HTTPS**: certificato Let's Encrypt valido (emesso il 13/09/2026, scade il 12/12/2026, nomi `iltorchioantico.com`, `.it` e `www`); il primo certificato registrato è del 27/01/2024. Il passaggio da http a https è un 302 (temporaneo) e non un 301. Contenuto misto: Matrimoni, Catering, Gallery, Preventivi caricano script `http://` di Facebook e Twitter, bloccati dal browser. Nessuna intestazione HSTS. [Certo]
7. **CMS e server**: nessun CMS, pagine HTML a tabelle con modulo in Perl (`/cgi-bin/readform.cgi`) e jQuery con tre slider diversi (flexslider, tn3, GalleryView). Server "Apache/2.4.41 (Ubuntu)" dichiarato nell'intestazione. Elenco dei file aperto su `/images/`, `/css/`, `/js/`, `/slider/` (si vedono 405 file, anche PDF e foto del 2008). Nessuna intestazione di cache sulle immagini. [Certo]
8. **Peso e richieste** (rete di Playwright): home 33 richieste, 258 KB; ristorante 68 richieste, 2,6 MB; gallery 63 richieste, 2,7 MB (30 foto caricate tutte all'apertura); matrimoni 42 richieste, 954 KB; catering 52 richieste, 1,15 MB. Evento load della home tra 5,4 e 9,7 s; ristorante e gallery tra 6 e 23 s; primo byte dell'HTML 0,7-1,0 s (curl, 5 prove). [Certo, tempi indicativi]
9. **Foto ingrandite**: lo slider stira ogni foto a 682 px: 21 foto su 30 sono mostrate più grandi del naturale, le verticali fino a 1,9 volte (354 px mostrata a 682). Su retina tutte le foto della galleria sono sotto la risoluzione necessaria. [Certo]
10. **Link rotti**: "Villa Godi Malinverni" nel testo della home porta a `/villa_godi_malinverni.html` (404); "Partner" nel piede di 52 pagine inglesi porta a `/english/partner.html` (404); il pulsante "dove siamo" delle 7 pagine tedesche a `/de/unsere_lage.html` (404); "<< Torna a elenco IlTorchioAntico.com" in 95 pagine di dettaglio evento (italiane e inglesi) porta a `/.html` (403); i 4 feed RSS (`/news_feed_*.rss`) rispondono 500; i siti di due partner non esistono più (`candeleeaffini.com`, `confraternitadeco.it`: NXDOMAIN); il link Twitter risponde 520. [Certo]
11. **Privacy e cookie**: nessuna informativa privacy, nessuna cookie policy, nessun banner. I widget di Facebook e X partono senza consenso su Catering, Offerte e dettagli evento (richieste a `facebook.com`, `fbcdn.net`, `twitter.com`); le pagine evento inglesi caricano il contatore `accessi.it`. Il modulo laterale (in tutte le pagine) raccoglie nome, email e telefono senza informativa; quello dei preventivi cita il D. Lgs. 196/2003 e non il Regolamento UE 2016/679; nessuna casella di consenso. [Certo]
12. **Dati societari mancanti**: il piede riporta solo "© 2008 - 2024 Ristorante Il Torchio Antico - Lugo di Vicenza (VI)". Ragione sociale e codice fiscale compaiono solo nella news "Aiuti di Stato" del 2022; la P.IVA non è in nessun piè di pagina (obbligatoria sul sito per le società). [Certo]
13. **Testi chiusi in immagini**: il nome nel logo (JPG 295x49), il marchio nel piede (JPG 227x95), il pulsante "DOVE SIAMO", i pulsanti "ulteriori dettagli"; sul sito del catering la striscia "CHIAMACI PER UN PREVENTIVO 0445860358". Le locandine degli eventi erano immagini e sono perse con il dominio. [Certo]
14. **Contatti superati e incoerenti**: "Skype: villagodi" (Skype è stato chiuso da Microsoft a maggio 2025); indirizzo "Via Palladio, 46" in testata e "Via Palladio 44" nella pagina Pasqua 2024, nel Registro Imprese, in VIES e su Google. [Certo]
15. **SEO**: 66 pagine con lo stesso titolo "Ristorante Torchio Antico - Matrimoni e Cerimonie - Lonedo Lugo di Vicenza"; 124 pagine su 145 senza meta description; stesso H1 in testata ovunque; 16 immagini su 33 della home senza alt o con alt vuoto; `/`, `/index.html` e `/index.htm` identiche; dettagli evento in doppia copia `.htm` e `.html`; 40 pagine inglesi con il titolo della villa. [Certo]
16. **Leggibilità**: il titolo della pagina Partner è `#DAE8EF` su bianco, contrasto circa 1,25:1 (quasi invisibile, screenshot `12-partner-1440.png`); testi giustificati con buchi larghi da telefono. [Certo]
17. **Schede esterne**: la scheda Google (4,5 stelle, 292 recensioni) mostra "Rivendica questa attività": probabilmente non gestita dal ristorante [Probabile]; due schede su matrimonio.com da verificare a mano.

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | LE COLLINE DEL PALLADIO S.R.L. | news "Aiuti di Stato" sul sito; aziende.it (Registro Imprese); VIES |
| P.IVA e codice fiscale | 03658730241 (valida in VIES il 6/10/2026) | VIES, aziende.it, sito |
| REA | VI-343305, CCIAA di Vicenza, iscrizione 07/03/2012 | aziende.it |
| Sede legale | Via Palladio 44, 36030 Lugo di Vicenza (VI) | VIES, aziende.it |
| Indirizzo del ristorante dichiarato | Via Palladio, 46 - Lugo di Vicenza (VI) (testata); Via Palladio 44 (Pasqua 2024, torchiocatering.it, Google) | sito; [DA CONFERMARE] quale usare |
| Nome commerciale | Il Torchio Antico (ristorante), Torchio Catering (catering) | sito, torchiocatering.it |
| Attività | ATECO 56.11.11, ristoranti con servizio al tavolo | aziende.it |
| Telefono | +39 0445 860358 | sito, Google, villagodi.com |
| Cellulare | +39 339 3429942 | sito |
| Email | info@iltorchioantico.com | sito |
| PEC | lecollinedelpalladiosrl@legalmail.it | aziende.it (Registro Imprese) |
| Codice destinatario SDI | X2PH38J | aziende.it |
| Orari | aperto tutto l'anno a pranzo e cena; chiuso lunedì e martedì; ferie 1 settimana a novembre e 1 a gennaio; Google: mer-dom 9:00-23:30 | sito, Google; [DA CONFERMARE] orari di cucina |
| Posti | sale interne 150, porticato 180, giardino 300 | sito; villagodi.com dice 160 + 100: [DA CONFERMARE] |
| Anni di attività | "Dal 1960" e "da oltre 50 anni" (sito); "nel 1968" e "da oltre 60 anni" (villagodi.com); società attuale iscritta nel 2012 | [DA CONFERMARE] l'anno da usare |
| Dati economici | ricavi 519.029 euro (2024), 572.939 euro (2022), -9,4%; utile 3.216 euro (2024); 18 dipendenti; capitale 10.000 euro | aziende.it, fonte Registro Imprese, aggiornato 8/7/2026 |
| Contributi pubblici | elenco 2020-2021 pubblicato sul sito (news "Aiuti di Stato") | sito |
| Dominio | iltorchioantico.com registrato il 25/06/2001, scade il 25/06/2027; iltorchioantico.it non risolve più | RDAP Verisign, dns.google |
| Social | facebook.com/iltorchioantico, twitter.com/iltorchioantico (non raggiungibile); nessun Instagram del ristorante | sito |
| Scheda Google | "Il Torchio Antico", Via Andrea Palladio 44, Ristorante italiano, 4,5 stelle su 292 recensioni, place_id ChIJlTUrQFbIeEcRQDGLzNLFPq4 | Google Maps, 6/10/2026 |
| Luogo | barchesse di Villa Godi Malinverni, prima villa di Andrea Palladio (1542), Lonedo di Lugo di Vicenza; villa gestita oggi da Palladium SAS (P.IVA 12924220150) | sito, villagodi.com |
| Certificazioni | nessuna dichiarata | sito |

Da confermare con il cliente (va nel LEGGIMI): anno di apertura (1960 o 1968); indirizzo del ristorante (44 o 46); posti a sedere; orari e giorni di chiusura attuali; se il catering si chiama ancora "Torchio Catering" e se torchiocatering.it va chiuso o rediretto; diritti sulle foto della villa e sulle foto 2025 di Artelugo; logo in vettoriale; listino attuale (nessun prezzo dal 2024); se pubblicare la valutazione Google; elenco aggiornato dei partner; se tenere le lingue straniere (oggi 4).

## URL vecchi

Servono per `plugin/redirect-301.csv`. Pagine principali:

| URL vecchio | Contenuto | Destinazione probabile |
|---|---|---|
| `/`, `/index.html`, `/index.htm` | home | home |
| `/ristorante.htm` | ristorante | ristorante |
| `/banchetti_nozze.htm` | matrimoni | matrimoni |
| `/catering_banqueting_vicenza.html` | catering | catering |
| `/foto_gallery_ristorante_catering_vicenza.html` | galleria | galleria o ristorante |
| `/info_preventivi.html` | preventivi | contatti/preventivo |
| `/come_arrivare.html` | mappa | contatti |
| `/partner.htm` | partner | matrimoni (o pagina partner) |
| `/eventi_da_non_perdere.html`, `/news_eventi.html`, `/offerte_e_promozioni.html`, `/menu_turismo_a_tavola.html` | eventi, news, offerte, menu | eventi e menu |
| `/english/*`, `/de/*`, `/es/*`, `/fr/*` | traduzioni | home o versione in lingua, [DA CONFERMARE] |
| `/news_eventi_NNN_*`, `/eventi_da_non_perdere_NNN_*`, `/menu_turismo_a_tavola_NNN_*`, `/english/eng_*_NNN_.htm` | 95 dettagli evento e menu | eventi |

Elenco completo dei 146 URL che rispondono 200 (anche in `_prova/crawl/url-vecchi.txt`):

```
/
/banchetti_nozze.htm
/catering_banqueting_vicenza.html
/come_arrivare.html
/de/catering_banqueting.html
/de/fotogalerie.html
/de/index.htm
/de/index.html
/de/informationen.html
/de/restaurant.html
/de/zeremonien.html
/english/catering_banqueting.html
/english/eng_eventi_da_non_perdere.html
/english/eng_eventi_da_non_perdere_179_.htm
/english/eng_eventi_da_non_perdere_180_.htm
/english/eng_eventi_da_non_perdere_182_.htm
/english/eng_eventi_da_non_perdere_183_.htm
/english/eng_eventi_da_non_perdere_184_.htm
/english/eng_eventi_da_non_perdere_185_.htm
/english/eng_eventi_da_non_perdere_187_.htm
/english/eng_eventi_da_non_perdere_188_.htm
/english/eng_eventi_da_non_perdere_189_.htm
/english/eng_eventi_da_non_perdere_190_.htm
/english/eng_eventi_da_non_perdere_192_.htm
/english/eng_eventi_da_non_perdere_193_.htm
/english/eng_eventi_da_non_perdere_194_.htm
/english/eng_eventi_da_non_perdere_195_.htm
/english/eng_eventi_da_non_perdere_196_.htm
/english/eng_eventi_da_non_perdere_197_.htm
/english/eng_eventi_da_non_perdere_198_.htm
/english/eng_eventi_da_non_perdere_200_.htm
/english/eng_eventi_da_non_perdere_201_.htm
/english/eng_eventi_da_non_perdere_202_.htm
/english/eng_menu_turismo_a_tavola.html
/english/eng_news_eventi.html
/english/eng_news_eventi_173_.htm
/english/eng_news_eventi_175_.htm
/english/eng_news_eventi_178_.htm
/english/eng_news_eventi_179_.htm
/english/eng_news_eventi_180_.htm
/english/eng_news_eventi_182_.htm
/english/eng_news_eventi_183_.htm
/english/eng_news_eventi_184_.htm
/english/eng_news_eventi_185_.htm
/english/eng_news_eventi_186_.htm
/english/eng_news_eventi_187_.htm
/english/eng_news_eventi_188_.htm
/english/eng_news_eventi_191_.htm
/english/eng_news_eventi_194_.htm
/english/eng_news_eventi_195_.htm
/english/eng_news_eventi_196_.htm
/english/eng_news_eventi_197_.htm
/english/eng_news_eventi_198_.htm
/english/eng_news_eventi_200_.htm
/english/eng_news_eventi_201_.htm
/english/eng_offerte_e_promozioni.html
/english/index.htm
/english/index.html
/english/information.html
/english/location.html
/english/photo_gallery.html
/english/restaurant.htm
/english/restaurant.html
/english/wedding_ceremonies.htm
/english/wedding_ceremonies.html
/es/catering_banqueting.html
/es/ceremonias.html
/es/fotos.html
/es/index.htm
/es/index.html
/es/informacion.html
/es/restaurante.html
/es/ubicacion.html
/eventi_da_non_perdere.html
/eventi_da_non_perdere_179_pasqua_2020_-_villa_godi_malinverni.htm
/eventi_da_non_perdere_180_il_torchio_antico_-_menu_alla_carta_.htm
/eventi_da_non_perdere_182_riapertura_il_torchio_antico_-_da_venerdì_22_maggio.htm
/eventi_da_non_perdere_183_natale_con_palladio_2020.htm
/eventi_da_non_perdere_184_san_valentino_2021.htm
/eventi_da_non_perdere_185_carnevale_2021.htm
/eventi_da_non_perdere_187_natale_con_palladio_2021_-_villa_godi_malinverni.htm
/eventi_da_non_perdere_188_san_valentino_2022__sabato_12_,_domenica_13_e_lunedi_14.htm
/eventi_da_non_perdere_189_festa_della_donna_-__8_marzo_2022.htm
/eventi_da_non_perdere_190_pasqua_2022_-_il_torchio_antico_villa_godi_malinverni.htm
/eventi_da_non_perdere_192_arti_in_villa_2022_-_associazione_prolugo.htm
/eventi_da_non_perdere_193_natale_con_palladio_2022_-_villa_godi_malinverni.htm
/eventi_da_non_perdere_194_san_valentino_2023_-_martedí_14_febbraio.htm
/eventi_da_non_perdere_195_pasqua_2023_.htm
/eventi_da_non_perdere_196_pasqua_2023_.htm
/eventi_da_non_perdere_197_pasqua_2023_.htm
/eventi_da_non_perdere_198_appuntamento_in_giardino_2023_-_villa_godi_malinverni_domenica_4_giugno.htm
/eventi_da_non_perdere_200_natale_con_palladio_2023__-_villa_godi_malinverni.htm
/eventi_da_non_perdere_201_san_valentino_2024.htm
/eventi_da_non_perdere_202_pasqua_2024.htm
/foto_gallery_ristorante_catering_vicenza.html
/fr/catering_banqueting.html
/fr/ceremonies.html
/fr/galerie_de_photos.html
/fr/index.htm
/fr/index.html
/fr/informations.html
/fr/restaurant.html
/fr/situation.html
/index.htm
/index.html
/info_preventivi.html
/menu_turismo_a_tavola.html
/menu_turismo_a_tavola_172_natale_con_palladio_2018_-_villa_godi_malinverni.htm
/menu_turismo_a_tavola_173_capodanno_con_palladio_2018_-_il_torchio_antico.htm
/menu_turismo_a_tavola_180_il_torchio_antico_-_menu_alla_carta_.htm
/menu_turismo_a_tavola_194_san_valentino_2023_-_martedí_14_febbraio.htm
/menu_turismo_a_tavola_196_pasqua_2023_.htm
/menu_turismo_a_tavola_197_pasqua_2023_.htm
/menu_turismo_a_tavola_19_degustazione_di_asparagi.htm
/menu_turismo_a_tavola_202_pasqua_2024.html
/menu_turismo_a_tavola_202_pasqua_2024.htm
/menu_turismo_a_tavola_2_degustazione_asparagi_.htm
/menu_turismo_a_tavola_5_menù_lonedo:_servizio_al_tavolo_per_piccoli_gruppi,_individuali_e_coppie.htm
/menu_turismo_a_tavola_6_menu_turistico_primavera_-_estate.htm
/menu_turismo_a_tavola_7_menu_turistico_palladiano.htm
/news_eventi.html
/news_eventi_173_capodanno_con_palladio_2018_-_il_torchio_antico.htm
/news_eventi_175_pasqua_21_aprile_2019.htm
/news_eventi_178_vicenzaè_-_villa_godi_malinverni.htm
/news_eventi_179_pasqua_2020_-_villa_godi_malinverni.htm
/news_eventi_180_il_torchio_antico_-_menu_alla_carta_.htm
/news_eventi_182_riapertura_il_torchio_antico_-_da_venerdì_22_maggio.htm
/news_eventi_183_natale_con_palladio_2020.htm
/news_eventi_184_san_valentino_2021.htm
/news_eventi_185_carnevale_2021.htm
/news_eventi_186_festa_della_donna_2021.htm
/news_eventi_187_natale_con_palladio_2021_-_villa_godi_malinverni.htm
/news_eventi_188_san_valentino_2022__sabato_12_,_domenica_13_e_lunedi_14.htm
/news_eventi_191_aiuti_di_stato.htm
/news_eventi_194_san_valentino_2023_-_martedí_14_febbraio.htm
/news_eventi_195_pasqua_2023_.htm
/news_eventi_196_pasqua_2023_.htm
/news_eventi_197_pasqua_2023_.htm
/news_eventi_198_appuntamento_in_giardino_2023_-_villa_godi_malinverni_domenica_4_giugno.htm
/news_eventi_200_natale_con_palladio_2023__-_villa_godi_malinverni.htm
/news_eventi_201_san_valentino_2024.htm
/news_eventi_202_pasqua_2024.html
/news_eventi_202_pasqua_2024.htm
/offerte_e_promozioni.html
/partner.htm
/ristorante.htm
```

Linkati ma rotti (da non redirigere, solo da sapere): `/villa_godi_malinverni.html`, `/english/partner.html`, `/de/unsere_lage.html` (404), `/.html` (403), `/news_feed_eventi.rss`, `/news_feed_news_marketing.rss`, `/news_feed_eventi_eng.rss`, `/news_feed_news_marketing_eng.rss` (500). Sito satellite: `http://www.torchiocatering.it/` con `index.html`, `torchio_catering_matrimoni.html`, `torchio_catering_ricevimenti.html`, `torchio_catering_in_azienda.html`, `torchio_catering_foto_gallery.html`, `torchio_catering_contatti.html` (e lo stesso su `torchiocatering.com`).
