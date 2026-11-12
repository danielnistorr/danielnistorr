# 01. Analisi del sito attuale (www.piovene.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente.

Materiale di lavoro (fuori da git): pagine scaricate in `_prova/crawl/pagine/` (299 indirizzi seguiti dai link) e `_prova/crawl/attachment/pagine/` (453 indirizzi trovati provando gli ID da 1 a 1700), testi estratti in `_prova/crawl/testi-*.txt`, misure in `_prova/attuale/misure.json`, screenshot `_prova/attuale/NN-pagina-1440.png` e `-390.png` (29 pagine), inventario immagini in `_prova/inventario-immagini.json`, elenco completo degli URL in `_prova/crawl/url-vecchi.txt`.

## In breve

- **Il sistema non è più aggiornato.** WordPress 4.6.30 (ramo del 2016; ultimo rilascio del ramo 17/07/2025; l'API di wordpress.org lo classifica "insecure"), PHP 7.4.10 (ramo fuori supporto dal 28/11/2022), plugin multilingua WPML 2.3.3, tema "Haze" 1.2, jQuery 1.12.4. Piè di pagina "© 2012", sito di Studio Cru. [Certo]
- **Contenuti fermi.** Ultime notizie del 2018 più una riga del 2023, pagina Premi ferma alle guide 2012 (con il refuso "Frà i broli 20089"), 128 dei 244 file caricati risalgono al 2012. Le schede tecniche più recenti sono del 2022 (annate 2019-2021). [Certo]
- **Pezzi rotti misurati.** Mappa della pagina Contatti che mostra "404. That's an error." di Google; riquadro "Che tempo fa a Toara" vuoto in tutte le pagine (bloccato dal browser); le 5 foto dell'alloggio portano a pagine che rispondono HTTP 500 e i loro originali non esistono più; a 390 px cinque pagine scorrono in orizzontale e in tutte le schede vino la bottiglia è tagliata; Google Analytics e 7 cookie di profilazione partono prima di qualsiasi clic sul banner. [Certo]
- **Materiale.** Il patrimonio vero sono 12 bottiglie fotografate in studio su fondo bianco a 2362x3543 (servizio professionale del 2012), il logo a 3300 px, un archivio di famiglia (foto d'epoca della villa, della scalinata, dei trattori) e circa 60 foto reali di villa, barchesse, cantina e vigne in 8 gallerie "portfolio" **non collegate dal menu**. Ma la maggior parte delle foto è tra 640 e 1024 px: nessuna regge un'apertura a tutta larghezza su schermo retina. Non ci sono foto utilizzabili dell'alloggio (restano solo miniature 150x150). [Certo]
- **Identità che c'è già.** Stemma con leone rampante e corona sormontata da un leone, scritta "PIOVENE PORTO GODI" in maiuscoletto lapidario; nelle schede tecniche 2013-2022 un vinaccia scuro (circa #7A1A2A) con titoli serif; nelle foto la villa gialla, le colonne rosse della barchessa, le volte in mattoni della cantina. [Certo per gli elementi, colori campionati da PDF e scansioni]
- **Numeri dichiarati.** 220 ettari, 28 di vigneto, vigne fino a circa 250 m (sito). Gambero Rosso (21/04/2022) scrive "about forty hectares of vineyards" e "about 120,000 bottles": la somma delle bottiglie nelle schede 2022 fa circa 121.500. Vini certificati biologici secondo le schede 2022 (organismo IT BIO 006, operatore n. E2347). [Certo per le fonti; ettari di vigneto DA CONFERMARE]

## Pagine esistenti

Menu italiano (le voci di primo livello Azienda, Prodotti, Ospitalità, Territorio non portano a una pagina). Su telefono il menu diventa un `<select>`.

| Voce | URL | Stato |
|---|---|---|
| Home | `/` | 1 foto 660 px, testo sul vigneto, elenco vini, link "Download Logo" |
| Azienda > Storia | `/storia/` | testo storia della famiglia, foto d'epoca 290x390 |
| Azienda > L'essenza | `/profilo/` | testo sull'accoglienza, foto della villa 384 px (titolo pagina "Piovene Porto Godi") |
| Azienda > La lezione del tempo | `/mission/` | testo su anni 90 e Thovara, foto 290x390 |
| Azienda > Vigne e Vini | `/` | rimanda alla home (nel menu a tendina del telefono la home risulta "– Vigne e Vini") |
| Azienda > Video | `/profilo/video/` | immagine di repertorio di un televisore con filigrana "dreamstime.com", 2 link YouTube |
| Azienda > Visita virtuale all'azienda | `/visita-virtuale-allazienda/` | tour Street View di Nicola Zanettin (vicenzafotografia.it), funziona |
| Azienda > Premi | `/premi/` | elenco premi 2006-2012 (guide 2012), due bottiglie magnum coricate |
| Prodotti > 11 vini | `/riveselle-tai-rosso/`, `/lola-tai-rosso/`, `/thovara-tai-rosso/`, `/pozzare-cabernet/`, `/fra-i-broli-merlot/`, `/polveriera-rosso-taglio-bordolese/`, `/campigie-sauvignon/`, `/fostine-sauvignon/`, `/polveriera-bianco-pinot-bianco/`, `/garganego-riveselle/`, `/thovara-bianco-passito/` | bottiglia coricata 640x190, testo, link a scheda PDF e a immagine bottiglia. Riveselle, Lola e Garganega senza immagine |
| Prodotti > Olio | `/olio/` | bottiglia Laudo coricata 640x150, testo sui due oli |
| Ospitalità > Degustazioni | `/degustazioni/` | testo breve, foto 225x265 |
| Ospitalità > Agriturismo | `/agriturismo/` | testo sull'alloggio nella colombara, foto verticale, 5 miniature 150x150 che portano a pagine in errore 500 |
| Territorio > Colli Berici | `/colli-berici/` | testo, foto vigneto a terrazze |
| Territorio > Vicenza | `/vicenza/` | testo turistico, foto 300 px |
| Territorio > Padova | `/padova/` | testo turistico, foto 300 px |
| News | `/blog/` | 30 articoli dal 2012 al 2023 (2 pagine) |
| Contatti | `/contatti/` | dati, mappa Google rotta (404) |
| Privacy e Cookie Policy | `/privacy-cookie-policy/` | informativa ferma al D.Lgs. 196/2003 |

Pagine pubblicate ma **non raggiungibili dal menu** (trovate provando gli ID, rispondono 200):

| URL | Contenuto |
|---|---|
| `/psr/` | contributi PSR Veneto 2014-2020 ricevuti (misure 4.1.1 e 11.1.1, conversione al biologico), con i loghi obbligatori; il link al decreto punta a `file:///C:/Documents and Settings/...` (un file sul computer di chi ha scritto la pagina) |
| `/shop/` | rimando a Vinix Grassroots Market per acquistare online |
| `/comunicazione/` | link al logo in alta definizione e al marchio |
| `/vino/` | doppione della home con il refuso "Enzo xxx" al posto di "Enzo Mazzocco" |
| `/prodotti/`, `/territorio/`, `/ospitalita/` | pagine vuote |
| `/blog/progetto-69-0001-866-2020-...` | pagina "turismo sostenibile" (progetto FSE 2023) |
| `/portfolio/villa-e-barchesse/`, `/portfolio/la-bottaia-2/` (Cucina e cantina), `/portfolio/il-portico/` (Guardandosi attorno), `/portfolio/autunno-sui-colli/` (Vigne), `/portfolio/inverno-a-toara/`, `/portfolio/prova/` (Poesia in vigna), `/portfolio/saluti-da-toara/`, `/portfolio/amarcord/` | 8 gallerie fotografiche con le foto migliori del sito, nessun link dal menu |
| `/2012/09/ciao-mondo/` | primo articolo ("Piccole grandi soddisfazioni") rimasto all'indirizzo dell'articolo di prova di WordPress |

Versione inglese (`?lang=en`, 25 pagine + 4 articoli del 2013): traduzione di menu e pagine; la home EN ripete due volte "The position is perfect" e nell'elenco vini manca Fra' i Broli; nella scheda Thovara EN un link ha come indirizzo l'intero paragrafo di testo. [Certo]

## Testi reali (verbatim, con i refusi originali)

Il testo integrale di tutte le pagine, articoli e gallerie è in `_prova/crawl/testi-it-pagine.txt`, `testi-it-vini.txt`, `testi-articoli.txt`, `testi-nascoste.txt`. Qui sotto i testi delle pagine principali. Le poche parole che compaiono nella lista PAROLE_VIETATE (anche come parte di parola) sono sostituite da "[...]": nel testo originale ci sono.

**Home, "Nel cuore della DOC Colli Berici"**
1. "Ci sono luoghi che sanno trasmettere più di altri. Come a Toara, che significa terra buona, dove crescono le vigne Piovene Porto Godi. 220 ettari di terreni, tra superfici coltivate a seminativi, un oliveto e bosco, con 28 ettari di vigneti aziendali."
2. "La posizione è perfetta. Siamo nel cuore della DOC, riparati in un anfiteatro naturale nella parte sud dei Colli Berici. I vigneti si estendono dal piede della collina fino a una quota di circa 250 m."
3. "Le varietà coltivate presso l'azienda Piovene sono: il Tai (Tocai) Rosso, vitigno tradizionale ed esclusivo dei Colli Berici, il Cabernet Franc e Sauvignon ed il Merlot. Per le uve bianche, invece, sono presenti il Sauvignon, il Pinot Bianco e la Garganega."
4. "Senza dimenticare il prezioso lavoro degli enologi. Enzo Mazzocco, Flavio Prà e Giovanni Nordera."

**Storia, "Una famiglia, un luogo, un vino"**
5. "Ogni storia ha un suo inizio. Per i vini della casa Alessandro Piovene Porto Godi la memoria corre talmente lontano nel tempo che ha bisogno di un testimone: una mappa del 1584. Qui si può vedere l'impronta di quella che oggi è l'azienda agricola, in una pianta della casa circondata dal cortile. Tutto intorno viti e alberi da frutto, come racconta un documento degli stessi anni."
6. "Proprietario era allora Flavio Barbarano, che per discendenza diretta arriva fino agli attuali proprietari. Negli anni solo il suo cognome si è estinto per lasciare spazio prima a Conti e poi all'attuale Piovene Porto Godi. Alessandro, che dà il nome all'azienda, è padre di Mariantonio e Tomaso, gli attuali proprietari. Con loro i figli Emanuele, Alessandra, Giovanni, Filippo, Chiara."
7. "Una famiglia indigena di viticoltori e un patrimonio di sapienza generata in decenni di lavoro in vigna. Un passaggio di padre in figlio che ha coinvolto anche le persone che lavorano con la famiglia Piovene: oggi in cantina e ad occuparsi delle viti, infatti, hanno ereditato il lavoro nipoti e figli dei dipendenti stessi."
8. "Il vino di una famiglia, ma anche il vino di un paese. La gente della zona sceglie ancora oggi il vino sfuso della cantina, come era da tradizione commercializzarlo qualche anno fa. Tradizione che non si è persa ma che si accompagna oggi a bottiglie importanti."
9. "Oggi Piovene Porto Godi è un punto di riferimento per chi cerca vini di alta qualità. Come testimoniano i numerosi premi e riconoscimenti ricevuti."

**L'essenza, "Le porte della cantina sono sempre aperte"**
10. "Immaginate di entrare nella corte di una cascina rossa che profuma di passato. Immaginate le persone che hanno abitato questi luoghi, intrecciando storie nobili e contadine. Immaginate un luogo di silenzio dove la voce è solo dei vini e il ritmo quello delle campane. Tutto questo nella natura ancora integra dei Colli Berici."
11. "L'essenza dell'ospitare è racchiusa in questa corte. Meglio se davanti a un bicchiere di vino. Perché alle famiglie che qui si sono succedute è sempre toccato in sorte di fare il vino. E lo fanno con la naturalezza di chi ha visto fare questa cosa da sempre e che pensa che questo sia la vita stessa."
12. "Le porte della cantina sono sempre aperte. La gente del luogo è sempre passata di qui per acquistare il vino, ma anche solo per fare due chiacchiere con i produttori. E non sarà strano incontrare persone da lontano, molto lontano, che hanno lasciato tutto per venire a Toara, in questo luogo senza tempo."
13. "Dove vite e storia raccontano la stessa trama."

**La lezione del tempo, "La lezione dei vini dei Colli Berici"**
14. "Nei vini Piovene Porto Godi si scopre la lezione del tempo: bisogna avere pazienza, saper attendere per poter essere ricordati. Perché c'è un segreto per creare vini di elevata qualità: permettere al frutto di invecchiare, di raccontare la sua storia. Dentro ogni bottiglia c'è il ritmo della terra, la forza di un vitigno, la voce del sole. Bisogna lasciar solo che il tempo si esprima, senza dimenticare di seguire la vocazione di un luogo, come la preferenza dei Colli Berici per i vini rossi."
15. "La svolta del tempo per i vini Piovene Porto Godi è agli inizi degli anni novanta. La vigna si rinnova, con i vigneti reimpiantati secondo moderni sistemi qualitativi. Filari più ravvicinati e una resa per pianta più bassa, con impianti fitti a potatura corta con tutti i trattamenti eseguiti nel massimo rispetto per l'ambiente. E nel frattempo in cantina l'uva si lascia imbottigliare e affinare per lunghi mesi."
16. "Non tarda ad arrivare nemmeno l'intuizione di Tomaso di dare vita al primo vino da lungo invecchiamento prodotto con le uve di Tai Rosso, il Thovara. Il Tai Rosso, vitigno autoctono dei Colli Berici, era diffuso fino a quel momento come un vino leggero, di facile beva. Si è scelto di recuperare la vocazione di questo vitigno, affinando il vino per lunghi mesi, al fine di ottenere vini importanti e longevi."

**Video**
17. "Per spiegarvi meglio la nostra essenza vi proponiamo questi video che vi sapranno raccontare quello che succede in cantina… Ecco la vendemmia del 2013 e un tipico imbottigliamento…per altri video guardate il nostro canale youtube vini piovene porto godi! Non dimenticate, però, che il miglior modo per capirci resta, sempre, una visita in cantina…vi aspettiamo!"

**Visita virtuale all'azienda**
18. "Se non siete ancora riusciti a venire a trovarci, se è passato troppo tempo ed avete nostalgia, se siete semplicemente curiosi in questa pagina potete visitare virtualmente la nostra azienda! (riprese a cura di www.vicenzafotografia.it)"

**Premi, "Un riferimento per i vini di qualità"** (elenco completo, refusi compresi)
19. "I vini Piovene Porto Godi nel tempo hanno maturato una loro importanza. Questo l'elenco dei premi, riconoscimenti, recensioni ricevuti negli ultimi anni."
- Guida "Vini buoni d'Italia 2006" – corona al vino "Thovara tocai rosso DOC Colli Berici 2003"
- V Concorso Nazionale Merlot d'Italia 2007 – primo classificato, categoria DOC-DOCG – Annate precedenti con il vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2004"
- Mondial du merlot, Lugano 2008 – médaille d'argent al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2006"
- "Guida al vino quotidiano 2009", edizioni Slow food – etichetta per l'ottimo rapporto tra qualità e prezzo al vino "Tai rosso DOC Colli Berici, vigneto Riveselle 2008"
- Mondial du merlot, Lugano 2009 – médaille d'or al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2007"
- VIII Concorso Nazionale Merlot d'Italia 2010 – primo classificato, categoria DOC-DOCG – Annate precedenti con il vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2008"
- Guida "Vini d'Italia 2010", edizioni Gambero rosso – due bicchieri rossi al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2007" e al vino "Thovara tocai rosso DOC Colli Berici 2007"
- Guida "Annuario dei migliori vini italiani" di Luca Maroni, edizione 2010 – 92 punti al vino "Thovara tocai rosso DOC Colli Berici 2007"
- Guida "Berebene low cost 2010", edizioni Gambero rosso – segnalazione "Tai rosso DOC Colli Berici, vigneto Riveselle 2008"
- Terroir Vino, edizioni 2010-2011 – "azienda del cuore 2011" per la consolidata costanza qualitativa
- IX Concorso Nazionale Merlot d'Italia 2011 – diploma di gran menzione al vino "Merlot DOC Colli Berici Frà i Broli 2009"
- Guida "Vini d'Italia 2011", edizioni Gambero rosso – tre bicchieri al vino "Cabernet DOC Colli Berici, vigneto Pozzare 2007", due bicchieri rossi al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2008"
- "Annuario dei migliori vini italiani 2011" di Luca Maroni – 89 punti al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2008"
- Guida "Duemilavini 2011", edizioni Associazione Italiana Sommelier – quattro grappoli al vino "Thovara Passito 2008" e al vino "Merlot DOC Colli Berici, vigneto Frà i broli 2008"
- Guida "Il Golosario" di Paolo Massobrio e Marco Gatti – premio "Top Hundred 2011, i 100 migliori vini d'Italia" al vino "Thovara Tai rosso DOC Colli Berici 2008"
- Guida "I vini di Veronelli 2011" – segnalazione "vino – buono, ottimo o eccellente – che entra per la prima volta in guida" dei vini "Merlot DOC Colli Berici, vigneto Frà i broli 2008" e "Thovara tai rosso 2007" e segnalazione "vino buono" del vino "Tai rosso DOC Colli Berici, vigneto Riveselle 2009"
- "I vini d'Italia 2012 – Le guide de l'Espresso" – punteggio di 16/20 al vino "Cabernet DOC Colli Berici, vigneto Pozzare 2009" e al vino "Sauvignon DOC Colli Berici, vigneto Fostine 2010" e punteggio di 15.5/20 al vino "Thovara Tai rosso DOC Colli Berici 2008"
- Guida "Slow wine 2011. Storie di vita, vigne, vini in Italia", edizioni Slow food – moneta rapporto qualità prezzo all'azienda
- Guida "Vini d'Italia 2012", edizioni Gambero rosso – due bicchieri rossi al vino "Merlot DOC Colli Berici, vigneto Frà i Broli 2009" e al vino "Cabernet DOC Colli Berici, vigneto Pozzare 2008"
- Guida "Annuario dei migliori vini italiani" di Luca Maroni, edizione 2012 – 90 punti al vino "Thovara Tai rosso DOC Colli Berici 2008"
- Guida "Duemilavini 2012", edizioni Associazione Italiana Sommelier – quattro grappoli al vino "Thovara Tai rosso DOC Colli Berici 2008", al vino "Merlot DOC Colli Berici, vigneto Frà i broli 20089" e al vino "Cabernet DOC Colli Berici, vigneto Pozzare 2009"
- "I vini d'Italia 2012 – Le guide de l'Espresso" – punteggio di 16/20 (vino ottimo) a Sauvignon Vigneto Fostine 2011 e Tai Rosso Vigneto Riveselle 2011; punteggio di 15,5 (buono) a Cabernet Vigneto Pozzare 2010 e Tai Rosso Thovara 2009.
- Guida "Vini d'Italia 2012", edizioni Gambero rosso – due bicchieri a Tai RossoThovara 2009 (in finale per i tre bicchieri), al Cabernet Vigneto Pozzare 2010, al Merlot Frà I Broli 2010 e al Riveselle 2011
- Guida "Duemilavini 2012" – quatto grappoli a Tai Rosso Thovara 2009, Merlot Fra' i Broli 2010 e Cabernet Pozzare 2010
- Guida "Slow wine 2011. Storie di vita, vigne, vini in Italia", edizioni Slow food – premio Vino Quotidiano a Tai Rosso Riveselle 2011

Dall'articolo del 21/09/2012 "Piccole grandi soddisfazioni": "Il nostro Merlot Colli Berici Doc "Fra i Broli" ha conquistato il secondo posto nella decima edizione di "Merlot d'Italia"." e "il nostro Tai Rosso Riveselle è stato segnato con il colore azzurro per indicare una bottiglia dall'eccellente rapporto tra la qualità e il prezzo (fino a 10 € in enoteca)." (guida Slow Wine).

**Schede vino (testo del sito)**
20. Riveselle, Tai Rosso (pagina senza titolo e senza foto): "È sul Tai (Tocai) Rosso, la varietà autoctona [...] dei Colli Berici, che l'azienda ha scommesso, per creare un vino-emblema di questo territorio. L'uva è una stretta parente del Grenache francese e della Garnaccia spagnola e fu introdotta nei Berici probabilmente ad opera dei canonici di Barbarano, in contatto con i vescovi di Avignone. Il Tocai rosso è un vino delicato con profumi floreali e marcato sentore di ciliegia, fragola e nota di pepe. Un vino di pronta beva ma provvisto di buona struttura e concentrazione, insuperabile compagno del baccalà alla vicentina."
21. Rosato IGT Veneto (Lola): "Il rosato è ottenuto dalla vinificazione in rosato di uve Tai (Tocai) Rosso. Viene affinato in acciaio a contatto con le sue fecce fini per garantire una maggior complessità degli aromi. Colore e profumi evocano in modo nitido la Rosa. In bocca si presenta fresco e bilanciato con sfumature minerali, sentori di fragola e lampone. Ideale per un fresco aperitivo o con delicati primi piatti, perfetto con il pesce specialmente con i "crudi"."
22. Thovara – Tai Rosso Colli Berici DOC: "Il Tai Rosso Thovara è espressione originale e compiuta del vino autoctono dei Colli Berici. Un prodotto importante, ottenuto da uve raccolte al massimo livello di maturazione, con resa di soli 35 quintali/ettaro, vinificato e maturato in tonneau francesi per un anno. Un vino di spessore ed eleganza in cui si fondono sapidità, freschezza e potenza alcolica."
23. Pozzare – Cabernet Colli Berici DOC: "Il Cabernet è un vitigno che nei Berici si è adattato da oltre un secolo, tanto da poter essere ormai considerato autoctono. Il Pozzare è un blend di Cabernet Franc e Cabernet Sauvignon. Affina per oltre un anno in piccoli fusti di rovere francese. Di colore violaceo molto intenso, vi si trovano marcati sentori di mora, tabacco, vaniglia e cannella. Il vino è adatto ad accompagnare piatti dal sapore molto intenso, come carni rosse e selvaggina."
24. Fra' i Broli – Merlot Colli Berici DOC: "Il Merlot Fra' i Broli, vino profondo e dagli intensi profumi, è ottenuto da tre cloni diversi di Merlot. Riposa per 12-15 mesi in barrique. E' un vino longevo, con colore intenso, tendente al violaceo, che sprigiona al naso sentori di frutta rossa matura e di ciliegia, da accompagnare con carni rosse. Ha vinto nel 2007 il primo premio assoluto alla mostra dei Merlot d'Italia di Aldeno."
25. Polveriera – Rosso Veneto IGT: "Vino robusto ed elegante ottenuto da un blend di Cabernet franc, Cabernet sauvignon, Carmenére e Merlot. Vino equilibrato e armonico con profumo vinoso, sentori di frutti di bosco, fragola e ciliegia, leggero sentore di pepe, fragola e peperone. Viene prodotto attraverso una macerazione con le bucce per 8 giorni con follatura. Va servito giovane, ma può invecchiare per alcuni anni."
26. Campigie – Sauvignon IGT Veneto: "Il Campigie è un Sauvignon che viene affinato in barrique, ottenuto dalla raccolta di uve sovramature in un vigneto policlonale. Riposa per sei-otto mesi in legni di diverse essenze (acacia e rovere) e per almeno altri sei in bottiglia. È un vino molto personale, possente nella struttura ed [...] morbido che, con la vendemmia tardiva, perde le note vegetali caratteristiche del Sauvignon per acquisire sentori di frutta matura."
27. Fostine – Sauvignon Colli Berici DOC: "Il Fostine è un Sauvignon ottenuto da un vigneto policlonale. Al colore si presenta giallo paglierino con riflessi verdognoli. Ha un profumo intenso tipico del Sauvignon con sentori di salvia, erbe officinali e marcate sensazioni fruttate di pesca, albicocca e agrumi. In bocca rivela una buona mineralità, bilanciando efficacemente morbidezza e acidità. Un vino di grande piacevolezza."
28. Polveriera – Pinot Bianco Colli Berici DOC: "Vino ottenuto da un impianto del 1994-1995 allevato a cordone speronato. La potatura corta, la bassa carica di gemme, riducono la resa a 60 q.li per ettaro. Il colore è giallo paglierino tendente al dorato. Al naso è elegante e delicato con profumi di mela matura, pera e fiori. Al gusto si ritrova una marcata pulizia e delicatezza di sapori."
29. Garganega – Colli Berici DOC: "L'uva Garganega è tipica del Veneto e ha trovato anche nei Colli Berici le condizioni ideali per sviluppare ottimamente le proprie qualità. Nell'azienda l'uva viene prodotta con una bassa resa e con vendemmia tardiva. Il vino prodotto ha colore dorato con profumo tipico con sentori di fiori. Il sapore è asciutto, leggermente minerale e di notevole freschezza. In chiusura è leggermente amarognolo con un retrogusto di miele."
30. Thovara passito – Bianco passito Veneto IGT: "Elegante vino ottenuto dalle uve passite di Sauvignon e Garganega; avvolgente, vellutato, intenso con un fondo di miele d'acacia e un bouquet di frutta candita, un vino mai stucchevole, con un finale raffinato. Grande abbinamento con i formaggi."

**Olio, "Una spremuta di Colli Berici"**
31. "L'olio di oliva extra vergine è prodotto da ulivi secolari. Le olive sono raccolte unicamente a mano, molite a freddo, con mezzi meccanici e tassativamente entro le 48 ore successive alla raccolta. Il sapore è quello tipico di questo territorio: delicato e fruttato, leggermente amarognolo."
32. "Sono due gli oli prodotti: Delfo e Laudo. Entrambi extra vergine di oliva, Delfo è anche Origine Protetta. Si tratta di un blend, le varietà presenti sono: Rasara 40%, Frantoio 20%, Leccino 20% e mix di varietà precoci 20%. Un prodotto armonico e ben strutturato che si caratterizza per gli aromi di erbe di campo, cardo e mandorla e per il gusto di oliva matura e mandorla che danno una sensazione di amaro e piccante persistente."
33. "L'olio dell'azienda Piovene Porto Godi è particolarmente indicato per consumo a crudo su carni alla brace, sul risotto al tartufo nero, sulla polenta calda del Baccalà alla Vicentina a fine cottura, con il Broccolo Fiolaro di Creazzo o il Radicchio di Asigliano, ma anche sul minestrone e la Panà vicentina."

**Degustazioni, "Prendetevi il vostro tempo"**
34. "Due chiacchiere con la famiglia, un giro per l'azienda o una degustazione con l'enologo. Sono diverse le possibilità per conoscere da molto vicino l'azienda Piovene Porto Godi. La cantina è aperta per visite e degustazioni a singoli o gruppi. Anche in inglese."
35. "Si organizzano degustazioni personalizzate, assaggiando diverse annate o in abbinamento ai prodotti locali. Ci sono stanze attrezzate o il grande porticato in giardino per le giornate di sole. È gradita la prenotazione."

**Agriturismo, "Splendidi alloggi tra le colline di Vicenza"**
36. "L'antica colombara adiacente alla villa è stata ristrutturata ed adattata per l'ospitalità. Luogo ideale per chi cerca l'esperienza di vivere in una dimora di campagna tra le colline di Vicenza, completamente immersi nella natura. Con le stelle che non si possono vedere in città e il suono delle campane a scandire il tempo."
37. "L'alloggio si sviluppa su due piani, gli spazi sono quelli ampi delle dimore di una volta. Al piano terra si trova una camera matrimoniale, un bagno e una ampia cucina-sala da pranzo. Una scala a chiocciola porta al primo piano dove è presente un'altra camera da letto matrimoniale, un bagno e un ampio soggiorno."
38. "L'alloggio può essere affittato soltanto per periodi superiori a 4 giorni. Per informazioni, disponibilità e prenotazioni inviare una mail a: agriturismo@piovene.com oppure chiamare il 340 8543966"

**Colli Berici, "Colline del silenzio. In bici, a piedi, a passo d'asino"**
39. "Ci troviamo nella parte più a sud dei Colli Berici, tra Vicenza e Padova. La sensazione che si prova vivendo questi luoghi è davvero unica. Toara ha un fascino particolare, un paesino abbracciato dal verde, con gli alberi che al tramonto disegnano il profilo delle colline. E tutto intorno il silenzio e la tranquillità che non abbandonano mai chi si avventura in queste splendide zone."
40. "Da qui potrete scegliere di partire per un itinerario, a piedi, in bicicletta o a passo d'asino. Attraversando le colline, tra filari di vigne, olivi secolari e piante di gelso. Sono numerosi i sentieri tracciati in mezzo ai boschi, meravigliosi in primavera e in autunno. Da non perdere una visita alle Grotte di San Donato o una passeggiata nella Valle dei Mulini a Mossano. Ma anche Villa Fracanzan Piovene di Orgiano, costruita dal Muttoni, con la sua famosa cucina che Napoleone voleva portare al Louvre. Qui incontrerete un interessante museo sulla vita contadina."
41. "Quasi non sembra di star così vicino a Padova e Venezia, ma in un attimo si raggiungono. Così come gli splendidi borghi di Montagnana, Este o Arquà Petrarca."

**Vicenza, "Piccola cittadina medievale dall'architettura unica"**
42. "Unica per la sua architettura, romantica per i suoi scorci, ricercata per il silenzio delle sue colline. La città di Vicenza incanta per i suoi gioielli architettonici, veri musei a cielo aperto. Ville, palazzi, piazze. Cuore della città è Piazza dei Signori, dove si affaccia la Basilica Palladiana, ma il posto che bisogna assolutamente vedere è il Teatro Olimpico [...] dall'Accademia Olimpica. Se poi vi capita di partecipare ad uno spettacolo della rassegna olimpica capirete quanto è grande questo luogo."
43. "Tra le vie del centro si respira storia, vita e cultura. Basta avere la pazienza di camminare senza una meta precisa. Appena fuori dal centro non dimenticatevi di visitare Villa Valmarana ai Nani, dove ammirare gli affreschi del Tiepolo, ma anche la Rotonda, esempio dell'arte del Palladio. E proprio da qui comincia una lunga pista ciclabile che arriva vicino alla nostra cantina. Un modo diverso per raggiungerci."

**Padova, "Padova è la città del sapere"**
44. "La fama di Padova è dovuta per gran parte alla sua università. Qui ha studiato Galileo Galilei e si è laureata la prima donna al mondo: Elena Lucrezia Cornaro in filosofia. Padova è anche "la città del caffè senza porte, del prato senza erba e del santi senza nome", dove il santo più importante è Sant'Antonio, il prato senza erba è Prato della Valle, ed il caffè senza porte è il celebre Pedrocchi che rimaneva sempre aperto, anche di notte."
45. "Un luogo da non perdere è la Cappella degli Scrovegni con il ciclo di affreschi di Giotto. Per una passeggiata scegliete le tre piazze principali: Piazza dei Signori, Piazza delle Erbe e Piazza della Frutta. Qui troverete qualche venditore di cibo di strada. Assaggiate il folpetto alla veneta e sarete padovani per un giorno."

**Contatti**
46. "Piovene Porto Godi Alessandro SS / Via Villa 14 / 36021 Toara di Villaga (VI) / Tel. 0444 885142 / Fax 0444 1783664 / cell. 340 8543966 – 348 1492876 – 348 3035515 / mail: info@piovene.com"
47. Piè di pagina: "Piovene Porto Godi A. SS / Via Villa 14 / 36021 Toara di Villaga (VI) / Tel. 0444 885142 / Fax 0444 1783664 / cell. 340 8543966 / 348 1492876 / 348 3035515 / mail: info@piovene.com" e "© 2012 - Piovene Porto Godi Alessandro SS P.IVA 00763110244 - Sito realizzato da Studio Cru | Privacy e Cookie Policy"

**Banner cookie**
48. "Utilizziamo i cookie per essere sicuri che tu possa avere la migliore esperienza sul nostro sito. Se continui ad utilizzare questo sito noi assumiamo che tu ne sia felice." (unico pulsante: "Ok")

**PSR (pagina non collegata)**
49. "Nell'ambito del Piano di sviluppo rurale attualmente in vigore, in questa pagina specifichiamo i finanziamenti ricevuti:" Misura 4.1.1, acquisto di "sarchiatore [...] per effettuare il diserbo meccanico nelle colture praticate; carro spandiletame, per la concimazione organica delle colture; cimatrice, per una gestione più agevole dei vigneti aziendali", con finalità "un primo passo verso l'adeguamento del parco macchine alle nuove necessità a seguito dell'adesione al metodo di coltivazione dell'"agricoltura biologica"", "Importo finanziato: € 34.776,94"; Misura 11.1.1, "CONVERSIONE ALL'AGRICOLTURA BIOLOGICA", "Risultati ottenuti: sensibile riduzione degli input produttivi .", "Importo finanziato: € 73.703,55 annui".

**Progetto Regione Veneto (articolo del 20/07/2023, una riga)**
50. "Abbiamo partecipato al Progetto 69-0001-866-2020 "Turismo sostenibile nell'area Berica" – Regione Veneto e FSE DGR 866 30 giugno 2020 – Bando: Ri-partiamo! Per il rilancio del turismo in Veneto"

**Dagli articoli (frasi utili, verbatim)**
51. Le tagliatelle della Sissi (2012): "Sissi ha 90 anni e un'energia incredibile. Da sempre vive con noi a Toara, anzi dire il vero lei qui ci è arrivata prima di noi. Ci aiuta con la casa e con la cucina, ma è molto di più, fa parte della nostra famiglia." e "I nostri vini non hanno ancora trovato un piatto in abbinamento che possa superare le lasagne al ragù della Sissi."
52. Vinitaly 2013: "come da tanti anni ormai, ci troverete al Padiglione 4 Stand G4".
53. Cantine aperte 2014: "visite alla cantina e alle barricaie, con una mostra di fotografie scattate da Simone Settimo durante la vendemmia".
54. Cantine aperte 2017: "Alle undici e alle tre vi portiamo a fare una passeggiata tra i vigneti, per farvi vedere le vigne nuove e quelle più vecchie e per farvi conoscere i nostri amici a quattro zampe, il musso Ciuchino, la capretta Pia, le galline e le pecore!"
55. Festival Ville Venete 2014: "Ti aspettiamo a Toara alle ore 19.00 sotto la barchessa per ascoltare alcune poesie e brindare assieme!"
56. Serata Aqua Crua 2015: "Avremo il piacere di ospitare nella nostra saletta degustazione Giuliano e Mattia, chef e sommelier del ristorante Aqua Crua di Barbarano Vicentino".

**Dalle schede tecniche PDF 2022 (testo dell'azienda)**
57. Tai Rosso Riveselle 2021: "Il Tai Rosso è il vino tipico dei Colli Berici. Dal vecchio vitigno Tocai Rosso, della famiglia della Grenache francese e del Cannonau sardo, forse importato nella zona dai canonici di Barbarano in contatto con i vescovi di Avignone nel dodicesimo secolo, si ottiene un vino fresco e leggero, da apprezzare in ogni stagione." e "Il tradizionale abbinamento è con il baccalà alla vicentina".
58. Intestazione in fondo a ogni scheda: "Società Agricola Piovene Porto Godi Alessandro S.S. via Villa 14 · 36021 Toara di Villaga · VI T. +39 0444 885142 F. +39 0444 1783664 www.piovene.com info@piovene.com"

**Refusi e incoerenze da non riportare nel nuovo sito**
- "Frà i broli 20089" (Premi), "quatto grappoli", "Tai RossoThovara", "del santi senza nome" (Padova), "Questi sito utilizza cookie" e "sui dei cookie" (Privacy), "E' un vino longevo", "Enzo xxx" (pagina `/vino/`), titolo pagina "Polveria Bianco".
- Il nome del Merlot compare in quattro grafie (Fra' i Broli, Frà i Broli, Fra i Broli, Frà I Broli); la Garganega anche come "Garganego Riveselle"; il Tai Rosso anche come "Tocai rosso" e "tocai rosso". Nel nuovo sito: **Fra' i Broli**, **Garganega**, **Tai Rosso** (con "Tocai Rosso" solo come nome storico del vitigno) [DA CONFERMARE la grafia preferita].
- Il nome dell'azienda compare come "Piovene Porto Godi Alessandro SS", "Piovene Porto Godi A. SS", "Piovene Porto Godi Alessandro S.S.", "Società Agricola Piovene Porto Godi Alessandro S.S." (schede 2022, forma completa da usare nei dati legali).
- Thovara: il sito dice "resa di soli 35 quintali/ettaro", la scheda 2015 "Resa 4000 kg/ha". Rosato 2021: la scheda PDF riporta per errore "Classificazione del Vino: Garganega DOC Colli Berici". Riveselle: il sito dice "probabilmente", la scheda 2021 "nel dodicesimo secolo".

## Cosa fanno e vendono

Azienda agricola di famiglia a Toara di Villaga, nel sud dei Colli Berici: vino DOC Colli Berici e IGT Veneto da sole uve aziendali, olio extravergine, ospitalità (degustazioni, alloggio nella colombara, eventi in barchessa). [Certo]

| Vino | Denominazione (scheda più recente) | Uve | Affinamento | Bottiglie dichiarate | Biologico in scheda |
|---|---|---|---|---|---|
| Riveselle | Tai Rosso DOC Colli Berici, vigneto Riveselle | Tocai Rosso | acciaio | 30.000 (annata 2021) | sì |
| Lola | Rosato IGT Veneto | Tai Rosso | acciaio, sulle fecce fini | 4.500 (2021) | sì |
| Thovara | Tai Rosso DOC Colli Berici | Tai (Tocai) Rosso, impianto 1999-2000, 220 m, esposizione sud | 12 mesi in tonneau di rovere francese, alcol 15,5% | 8.000 (2015, scheda più recente) | non indicato (scheda 2015) |
| Pozzare | Cabernet DOC Colli Berici | Cabernet Sauvignon e Cabernet Franc | barrique di rovere francese | 9.000 (2019) | sì |
| Fra' i Broli | Merlot DOC Colli Berici | cloni di Merlot | barrique di rovere francese, 12-15 mesi (sito) | 9.000 (2019) | sì |
| Polveriera rosso | Rosso IGT Veneto, taglio bordolese | Cabernet Franc, Cabernet Sauvignon, Merlot, Carmenère | acciaio e legno | 40.000 (2020) | sì |
| Campigie | Sauvignon, Bianco IGT Veneto | Sauvignon policlonale, uve sovramature | barrique (sito: acacia e rovere) | 3.000 (2020) | sì |
| Fostine | Sauvignon DOC Colli Berici | Sauvignon policlonale | acciaio | 10.000 (2021) | **non indicato** nella scheda 2021 |
| Polveriera bianco | Pinot Bianco DOC Colli Berici | Pinot Bianco, impianto 1995, cordone speronato, 60 q/ha | acciaio | 7.000 (2021) | sì |
| Garganega (Riveselle) | Garganega DOC Colli Berici | Garganega | acciaio | 9.000 (2021) | sì |
| Thovara passito | Bianco passito IGT Veneto | Sauvignon e Garganega, 70 m, impianto 1983-1986 | acciaio | 2.100 da 0,5 l (2013, scheda più recente) | non indicato (scheda 2013) |
| Olio Delfo e Laudo | extravergine; "Delfo è anche Origine Protetta" | Rasara 40%, Frantoio 20%, Leccino 20%, precoci 20% | | | |

Fonte: pagine del sito e schede PDF in `assets/originali/pdf/` (le schede 2022 riportano "Vino Biologico, Organismo di controllo IT BIO 006, Operatore controllato n. E2347"). Le annate e le quantità sono quelle stampate nelle schede: quelle attuali vanno chieste [DA CONFERMARE].

Altro dichiarato dall'azienda:
- **Visite e degustazioni** per singoli e gruppi, anche in inglese, con prenotazione; "stanze attrezzate", "il grande porticato in giardino", "saletta degustazione"; eventi in barchessa (concerti, danza, letture, Cantine Aperte, Il vino è donna, I suoni dei Berici). [Certo, ultimo evento pubblicato 2018]
- **Vendita**: vino sfuso alla gente del posto (Storia), shop online tramite Vinix Grassroots Market (pagina `/shop/`, 2018), presenza a Vinitaly "Padiglione 4 Stand G4" (2013, 2014). Vendita in cantina e prezzi: non pubblicati [DA CONFERMARE].
- **Alloggio**: un appartamento su due piani nella colombara (2 camere matrimoniali, 2 bagni, cucina-sala da pranzo, soggiorno), soggiorni sopra i 4 giorni. Se sia ancora attivo [DA CONFERMARE] (su Google la scheda è nella categoria "Fattoria").
- **Corsi**: nel 2014 due corsi di Sandro Sangiorgi (Porthos) a Toara. [Certo, evento passato]

Nota sulla villa: la casa di Toara non va confusa con la Villa Piovene palladiana di Lugo di Vicenza (Patrimonio UNESCO), che è un'altra villa della stessa famiglia storica e compare nei risultati di ricerca. Il sito parla di "villa", "colombara", "barchessa", "corte", "cascina rossa", senza nome né data della villa [DA CONFERMARE se e come chiamarla].

## Immagini usate oggi

Scaricate tutte le immagini caricate nel sito (pagine, articoli, gallerie non collegate, pagine allegato): 244 file originali richiesti, 205 presenti, 39 rispondono 404 (6 PDF e 33 immagini con l'originale cancellato: per 31 immagini è stata recuperata la misura ridotta più grande rimasta, spesso 1024 px). Le immagini dell'azienda sono in `assets/originali/` con nomi parlanti (122 file) e i PDF in `assets/originali/pdf/` (29); l'inventario completo con dimensioni, soggetto, qualità e larghezza massima mostrabile è in `_prova/inventario-immagini.json`.

| Gruppo | Quanti | Dimensioni | Giudizio e uso nel nuovo sito |
|---|---|---|---|
| Bottiglie verticali su bianco (servizio professionale 2012) | 12 (Thovara, Pozzare, Pozzare magnum, Fra' i Broli, Campigie, Fostine, Polveriera bianco e rosso, Garganega, Thovara passito, Lola; Riveselle estratta dalla scheda PDF 2012) | 2362x3543 (Polveriera rosso 1812x3281, Riveselle 1198x3543) | **il materiale migliore**: nitide, scontornabili, reggono qualsiasi uso. Etichette con annate vecchie (es. Thovara 2009): verificare se le etichette attuali sono uguali [DA CONFERMARE] |
| Bottiglie coricate | 15 | 640x190 (magnum 940 e 3543 px) | testate delle schede attuali, piccole; non servono se si usano le verticali |
| Olio Laudo | 1 | 640x150 | unica immagine dell'olio, piccola; nessuna foto del Delfo |
| Logo | 3 | 3300x1172 (nero, raster), stemma a colori 222x333 (scansione), PNG 220 px | il 3300 px basta per ridisegnare il logo in SVG; manca il vettoriale |
| Vigne e paesaggio | 30 | da 526 a 4000 px; 11 foto Olympus E-420 a 3648x2736 (morbide e rumorose al 100%, reggono circa 1600-1800 px); 1 aerea 4000x3000 (regge circa 2000 px); banner vigneto 2000x633 nitido; il resto 800-1024 px | stagioni (autunno rosso, neve, nebbia in bianco e nero, primavera in fiore) e terrazze: buone per fasce e mezze larghezze, non per un'apertura retina a tutta pagina |
| Villa, barchesse, corte, giardino | 25 | 500-1024 px (Nikon D50 del 2007 a 800x532; Nicola Zanettin 1024x681 con originali cancellati) | colonne rosse della barchessa, porticato, scalinata: soggetti forti ma al massimo a mezza larghezza; 6 file 384-500 px con nomi nello stile di Flickr, provenienza [DA CONFERMARE] |
| Cantina e cucina | 11 | 225-1024 px | barricaia sotto volta in pietra e cucina storica (Zanettin, 1024 px) utilizzabili a mezza larghezza; le altre 640 px o meno |
| Archivio di famiglia | 14 | 290-1750 px (scansioni d'epoca: calesse, gruppo sulla scalinata, villa nella neve, trattori anni 70-80; Sissi in bianco e nero 756 px) | materiale raro e vero per la pagina Storia, da mostrare come archivio (formato piccolo, cornice, didascalia) |
| Ospitalità | 6 | foto verticale 1770x2832 (tavolo con bottiglia e calici); 5 miniature 150x150 dell'alloggio | **manca tutto l'alloggio**: gli originali delle 5 foto non esistono più |
| Obblighi (PSR, FSE) | 2 | 500 e 393 px | loghi da mantenere nella pagina dei contributi |
| Non dell'azienda (non copiati in `assets/originali/`) | circa 70 | | locandine di eventi, loghi di terzi (Vinitaly, Vinix, Cantine Aperte, Locanda Le Muse), foto di Villa Valmarana e Fracanzan, foto turistiche di Vicenza e Padova (1024 px, provenienza sconosciuta), clip art del televisore con filigrana dreamstime.com: restano solo in `_prova/crawl/media-grezzi/` |

Foto fuori dal sito (`assets/esterne/manifest.json`):
- Canale YouTube dell'azienda ("vini piovene porto godi"): fotogramma 1280x720 del video della vendemmia 2013 (uva sul nastro davanti alla barchessa rossa con loggia in legno). Materiale del cliente, morbido; per usarlo servono i file video originali.
- Google Maps: scheda rivendicata dal proprietario, ma le 26 foto esposte sono tutte di utenti terzi (2020-2026: villa, scalinata, barricaia, galleria sotterranea, degustazione sotto il portico, scaffale con le etichette attuali). Scaricate a 1000 px **solo come riferimento per il brief fotografico**: non si pubblicano.
- Facebook (`facebook.com/PiovenePortoGodiVini`): accesso solo con login, nessuna foto. Instagram: nessun profilo ufficiale trovato. Wayback Machine: non raggiungibile dal nostro ambiente il 06/10/2026 (connessione chiusa a ogni tentativo); il sito conserva comunque gli originali del 2012 quasi tutti.

Conclusione: per le bottiglie e il marchio il materiale c'è ed è ottimo; per luoghi e persone ci sono soggetti veri e riconoscibili ma in piccolo formato. Il nuovo sito deve usare le foto di luogo a mezza larghezza o in griglie, mai a tutta pagina sopra i 1024 px, e il LEGGIMI deve chiedere: gli originali di Nicola Zanettin e del servizio del 27/06/2010 (nome file "franco-cogoli", Canon EOS-1Ds Mark II), le foto attuali dell'alloggio, la foto del Delfo, i file del video della vendemmia.

## Problemi tecnici da segnalare al cliente

Misure prese il 06/10/2026 con Chromium (Playwright) a 1440x900 e 390x844, passando dal proxy del nostro ambiente: i tempi sono indicativi.

1. **Software fuori supporto.** Meta generator e versioni degli script: WordPress 4.6.30. Su wordpress.org/download/releases l'ultimo rilascio del ramo 4.6 è del 17/07/2025, mentre il ramo 4.7 ha avuto aggiornamenti fino alla 4.7.37 del 22/09/2026 e la versione corrente è la 7.1.3 (06/10/2026); l'API ufficiale `api.wordpress.org/core/stable-check/1.0/` restituisce "4.6.30": "insecure". Intestazione `X-Powered-By: PHP/7.4.10` (rilascio del 03/09/2020; php.net/eol: ramo 7.4 senza aggiornamenti dal 28/11/2022). Altri componenti: WPML 2.3.3, tema Haze 1.2, jQuery 1.12.4, plugin Cookie Notice 1.2.31. `/wp/readme.html` e `/wp/wp-login.php` rispondono 200. [Certo]
2. **Contenuti fermi e datati.** "© 2012" nel piè di pagina; riquadro "Ultime notizie" con 4 eventi del 2018 e "progetto regione Veneto" (2023, una riga); pagina Premi ferma alle guide 2012; 128 dei 244 file caricati sono del 2012; 8 gallerie fotografiche e 8 pagine pubblicate ma non raggiungibili dal menu, 3 delle quali vuote. [Certo]
3. **Mappa rotta nella pagina Contatti.** L'iframe punta a una vecchia mappa "My Maps" (`maps.google.it/maps/ms?msid=211753876600912776116...`), che oggi rimanda a `google.com/maps/d/embed?mid=...` e risponde 404: in pagina si legge "404. That's an error." (screenshot `60-contatti-1440.png`). [Certo]
4. **Riquadro meteo vuoto in ogni pagina.** "Che tempo fa a Toara" carica in un iframe una pagina `http://www.ilmeteo.it/box/...` (citta=7917) dentro una pagina https: la console di Chromium segnala "Mixed Content: ... requested an insecure frame ... This request has been blocked" e il riquadro resta bianco su tutte le 29 pagine misurate. È l'unico errore in console nella maggior parte delle pagine; Contatti ne ha un secondo (404 della mappa), Visita virtuale un secondo innocuo (permesso accelerometro dello Street View); ogni pagina ha inoltre 2 avvisi di contenuto misto per il logo caricato in http. [Certo]
5. **Foto dell'alloggio rotte.** Le 5 miniature della pagina Agriturismo portano a `/agriturismo/dsc_0302/` ... `/dsc_0310/`, che rispondono **HTTP 500** con la pagina troncata dopo il menu; gli originali `DSC_0302.jpg` ... `DSC_0310.jpg` rispondono 404. Dell'alloggio restano solo miniature 150x150. [Certo]
6. **Telefono: pagine più larghe dello schermo e foto tagliate.** Il sito ha il meta viewport e la home sta in 390 px, ma `document.documentElement.scrollWidth` a 390 vale: Premi 985, Visita virtuale 985, Olio 685, Contatti 470, Agriturismo 404 (scorrimento orizzontale). Nelle 8 schede vino con foto e nella pagina Olio la bottiglia coricata (640 px) è tagliata a metà dentro lo schermo, e nella home la foto del vigneto mostra solo metà della scena (screenshot `*-390.png`). Nella pagina Agriturismo il testo si riduce a una colonna di una parola accanto alla foto. Il menu su telefono è un menu a tendina `<select>` di 32 voci che sulla home mostra "– Vigne e Vini". [Certo]
7. **Privacy e cookie.** Il banner ha solo "Ok" ("Se continui ad utilizzare questo sito noi assumiamo che tu ne sia felice"), nessun rifiuto né scelta. Prima di qualsiasi clic partono `googletagmanager.com/gtag/js?id=G-407J3TXLVQ`, `ssl.google-analytics.com/ga.js` (il vecchio Universal Analytics, dismesso da Google nel 2023) e la richiesta `google-analytics.com/g/collect` (risposta 204), e il browser riceve 7 cookie di analisi (`_ga`, `_ga_407J3TXLVQ`, `__utma`, `__utmb`, `__utmc`, `__utmt`, `__utmz`, scadenza fino al 10/11/2027) (`_prova/attuale/cookie-e-consenso.json`). L'informativa cita ancora "Decreto legislativo 30 giugno 2003 n.196" e "art.7 D.Lgs 196/2003", oltre a Google Plus e "advertising". [Certo per i fatti; la valutazione legale spetta al cliente]
8. **Velocità.** Home: 37 richieste, 374 KB trasferiti, di cui 169 KB (45%) per lo script di Google; 20 script e 8 fogli di stile separati; tempo al primo byte circa 1,0-1,2 s (curl: 0,95 s), evento load tra 3,4 e 3,9 s in tre misure a riposo. Il peso è basso: la lentezza viene dal server e dalla catena di script. [Certo, tempi indicativi]
9. **Link rotti o vecchi.** Interni: i link della barra "I nostri vini" puntano a `http://www.piovene.com/wp/<vino>/`; con https vengono corretti, ma chi li segue in http senza HSTS (per esempio un crawler) finisce sulla home (`http://.../wp/thovara-tai-rosso/` → `https://www.piovene.com/index.php` → `/`). Nella pagina Pozzare c'è un link vuoto a `/wp-content/uploads/2018`. Nella pagina PSR il link al decreto punta a `file:///C:/...`. Esterni (34 controllati): 404 la pagina della cena con delitto a Villa Valmarana, il depliant AIS 2013, la privacy di Pinterest; 503 `bevidoc.it` (consorzio) e `gustus.stradavinicolliberici.it`; non rispondono `bevicosavedi.it` e `faberest.com`. [Certo]
10. **Immagini piccole e ingrandite.** Nessuna foto della home supera 660 px a 1440 di schermo (2 immagini in tutto: logo 220 px e vigneto 660 px). Le foto delle pagine interne sono 225-390 px. Su telefono le bottiglie da 390 px vengono mostrate a 640 px (ingrandite e tagliate). La pagina Video usa un'immagine di repertorio con la filigrana "dreamstime.com" ancora visibile. [Certo]
11. **SEO di base.** Nessun H1 nelle 29 pagine misurate, nessuna meta description, titolo della home "Piovene Porto Godi |" e della pagina L'essenza "Piovene Porto Godi | Piovene Porto Godi", nessuna sitemap (`/sitemap.xml` 404), 32 immagini visibili su 68 senza testo alternativo, "Garganego" e "Polveria" nei titoli. [Certo]
12. **Testi chiusi in immagini e PDF.** Le schede tecniche 2013-2017 (Campigie 2013, Fostine 2015 e 2016, Polveriera 2015, Thovara passito 2013) sono PDF fatti di sole immagini: `pdftotext` estrae 2 caratteri, il testo non si cerca né si legge da telefono. Etichette e locandine degli eventi sono immagini. [Certo]
13. **Dati societari.** La P.IVA c'è nel piè di pagina (00763110244). La ragione sociale è abbreviata ("Piovene Porto Godi Alessandro SS"): la forma completa usata nelle schede è "Società Agricola Piovene Porto Godi Alessandro S.S.". La pagina dei contributi PSR (obbligo di pubblicità per i beneficiari) esiste ma non è raggiungibile dal menu. [Certo per i fatti, DA CONFERMARE l'obbligo specifico]
14. **HTTPS ok.** Certificato RapidSSL (DigiCert) per www.piovene.com e piovene.com, valido dal 31/10/2025 al 25/11/2026; redirect 301 da http e da piovene.com verso https://www.piovene.com; intestazione HSTS presente. Il certificato scade tra 7 settimane (rinnovo probabilmente automatico) [DA CONFERMARE]. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Società Agricola Piovene Porto Godi Alessandro S.S. | schede tecniche PDF 2022 (piè di pagina); sul sito "Piovene Porto Godi Alessandro SS", sull'informativa "Piovene Porto Godi Alessandro S.S." |
| P.IVA | 00763110244 | piè di pagina del sito |
| Codice SDI | M5ITOJA | brief di ricerca, non ricontrollato [DA CONFERMARE] |
| PEC | non pubblicata sul sito; da cercare su INI-PEC (ricerca con captcha, non automatizzabile da qui) | [DA CERCARE] |
| Sede | Via Villa 14, 36021 Toara di Villaga (VI) | sito, schede, Google |
| Coordinate | 45.3886, 11.5150 | Google Maps (place id ChIJk8-iPco8f0cR_op-GH9BjvQ) |
| Telefono | 0444 885142 | sito, schede, Google |
| Fax | 0444 1783664 | sito, schede |
| Cellulari | 340 8543966 (anche per l'alloggio), 348 1492876, 348 3035515 | sito [DA CONFERMARE quali sono ancora attivi] |
| Email | info@piovene.com; agriturismo@piovene.com (alloggio); negli articoli 2015-2018 anche pioveneportogodivini@gmail.com | sito |
| Orari | lunedì-sabato 9-12 e 14-18, domenica chiuso | solo scheda Google; il sito dice "È gradita la prenotazione" [DA CONFERMARE] |
| Famiglia | Alessandro (dà il nome all'azienda), padre di Mariantonio e Tomaso, "gli attuali proprietari"; figli Emanuele, Alessandra, Giovanni, Filippo, Chiara | pagina Storia (testo del 2012) [DA CONFERMARE se aggiornato] |
| Enologi | Enzo Mazzocco, Flavio Prà, Giovanni Nordera | home [DA CONFERMARE se attuali] |
| Storia | mappa del 1584 con la casa e il cortile; proprietario Flavio Barbarano, poi Conti, poi Piovene Porto Godi; svolta "agli inizi degli anni novanta" con il reimpianto; Thovara come primo Tai Rosso da lungo invecchiamento, intuizione di Tomaso | pagine Storia e La lezione del tempo |
| Superfici | 220 ettari (seminativi, oliveto, bosco), 28 ettari di vigneto, vigne fino a circa 250 m | home. Gambero Rosso (21/04/2022): "more than 200 hectares ... about forty hectares of vineyards" [DA CONFERMARE] |
| Produzione | circa 120.000 bottiglie | Gambero Rosso 2022; somma schede 2022 circa 121.500 |
| Certificazione | vino biologico, organismo di controllo IT BIO 006, operatore controllato n. E2347; conversione al biologico finanziata dal PSR (misura 11.1.1) | schede PDF 2022, pagina `/psr/` |
| Denominazioni | DOC Colli Berici, IGT Veneto; olio "Delfo è anche Origine Protetta" | sito, schede |
| Dipendenti | 10-19 | aziende.it (dal brief di ricerca) |
| Fatturato | non pubblico (società semplice, nessun bilancio depositato) | brief di ricerca |
| Canali | facebook.com/PiovenePortoGodiVini; YouTube @vinipioveneportogodi6555 (2 video); scheda Google rivendicata dal proprietario | sito, YouTube, Google |
| Sito attuale | realizzato da Studio Cru (studiocru.com), articoli firmati "Piovene" e "studiocru" | piè di pagina, articoli |

## URL vecchi

Elenco completo con titoli in `_prova/crawl/url-vecchi.txt` (622 indirizzi in categorie). Per `plugin/redirect-301.csv` servono questi; tutti gli indirizzi rispondono anche con il prefisso `/wp/` e con `?p=ID` (redirect di WordPress).

Pagine italiane (menu):
`/`, `/storia/`, `/profilo/`, `/mission/` (indirizzo esistente della pagina "La lezione del tempo"), `/profilo/video/`, `/visita-virtuale-allazienda/`, `/premi/`, `/riveselle-tai-rosso/`, `/lola-tai-rosso/`, `/thovara-tai-rosso/`, `/pozzare-cabernet/`, `/fra-i-broli-merlot/`, `/polveriera-rosso-taglio-bordolese/`, `/campigie-sauvignon/`, `/fostine-sauvignon/`, `/polveriera-bianco-pinot-bianco/`, `/garganego-riveselle/`, `/thovara-bianco-passito/`, `/olio/`, `/degustazioni/`, `/agriturismo/`, `/colli-berici/`, `/vicenza/`, `/padova/`, `/blog/`, `/blog/page/2/`, `/contatti/`, `/privacy-cookie-policy/`

Pagine italiane non collegate:
`/psr/`, `/shop/`, `/comunicazione/`, `/vino/`, `/prodotti/`, `/territorio/`, `/ospitalita/`, `/blog/progetto-69-0001-866-2020-turismo-sostenibile-nellarea-berica-regione-veneto-e-fse-dgr-866-30-giugno-2020-bando-ri-partiamo-per-il-rilancio-del-turismo-in-veneto/`

Gallerie: `/portfolio/villa-e-barchesse/`, `/portfolio/la-bottaia-2/`, `/portfolio/il-portico/`, `/portfolio/autunno-sui-colli/`, `/portfolio/inverno-a-toara/`, `/portfolio/prova/`, `/portfolio/saluti-da-toara/`, `/portfolio/amarcord/`

Articoli (30):
`/2012/09/ciao-mondo/`, `/2012/11/alla-locanda-le-muse/`, `/2012/11/le-tagliatelle-della-sissi/`, `/2013/03/veneto-al-300x100/`, `/2013/03/vinitaly-padiglione-4-stand-g4/`, `/2013/03/vinix-grassroots-market/`, `/2013/05/aspettando-il-giro-ditali/`, `/2013/05/cantine-aperte-2013/`, `/2013/06/visita-virtuale/`, `/2014/01/corsi-in-partenza-a-toara/`, `/2014/03/vi-aspettiamo-al-vinitaly/`, `/2014/05/cantine-aperte-2014/`, `/2014/09/1033/`, `/2015/05/cantine-aperte-2015/`, `/2015/09/uno-spettacolo-di-danza-in-cantina/`, `/2015/11/serata-aqua-crua-in-saletta/`, `/2016/06/sorsi-dautore-a-villa-valmarana/`, `/2016/09/cena-con-delitto-a-villa-valmarana/`, `/2016/11/cena-con-delitto-a-villa-valmarana-ai-nani-la-seconda/`, `/2017/03/cena-con-delitto-a-villa-valmarana-la-terza/`, `/2017/03/il-vino-e-donna/`, `/2017/03/un-giorno-in-villa/`, `/2017/05/cantine-aperte-2017/`, `/2017/10/cartoline-uno-spettacolo-di-danza-itinerante-della-d-d-t-dna-dance-theatre/`, `/2018/03/il-vino-e-donna-2018/`, `/2018/06/quadro-nuevo-a-toara/`, `/2018/09/a-cittadella-per-cittadellartevino/`, `/2018/09/gustus-vini-e-sapori-dei-colli-berici-2018/`, `/2018/09/i-suoni-dei-berici-2018/`, `/2023/07/progetto-regione-veneto/`

Versione inglese (con `?lang=en`):
`/?lang=en`, `/history/`, `/the-essence/`, `/the-lesson-of-the-time/`, `/wine-and-vineyard/`, `/riveselle-tai-rosso-2/`, `/lola-tai-rosso-2/`, `/thovara-tai-rosso-2/`, `/pozzare-cabernet-2/`, `/fra-i-broli-merlot-2/`, `/polveriera-rosso-blend/`, `/campigie-sauvignon-2/`, `/fostine-sauvignon-2/`, `/polveriera-pinot-bianco/`, `/garganego-riveselle-2/`, `/thovara-bianco-passito-2/`, `/oil/`, `/tasting/`, `/farm-holidays/`, `/around/`, `/berici-hills/`, `/padua/`, `/vicenza-2/`, `/contacts/`, `/news/`, articoli `/2013/01/650/`, `/2013/01/big-satisfactions/`, `/2013/01/sissis-lasagna/`, `/2013/03/776/`

Archivi (da reindirizzare in blocco alla pagina notizie o alla home): 69 tag e categorie (`/tag/...`, `/category/...`), 30 archivi per data (`/AAAA/` e `/AAAA/MM/`), 315 pagine allegato (`/<nome-file>/` e `/<articolo>/<nome-file>/`, per esempio `/storia/conti/`, `/agriturismo/dsc_0310/`), i feed (`/feed/`, `/comments/feed/`).

File con link esterni probabili (schede tecniche): `/wp/wp-content/uploads/2022/10/5TAIROSSOriv2021.pdf`, `.../2022/10/7MERLOT2019.pdf`, `.../2022/10/8CABERNET19.pdf`, `.../2022/10/0ROSATO2021.pdf`, `.../2022/10/1GARGANEGA2021.pdf`, `.../2022/10/3SAUVIGNON2021.pdf`, `.../2022/10/4CAMPIGIE2020.pdf`, `.../2022/04/2PINOT2021.pdf`, `.../2022/04/6POLVERIERA2020.pdf`, `.../2018/06/10.Tai-Rosso-DOC-Colli-Berici-Thovara-2015.pdf`, `.../2017/04/11_scheda_passito_thovara2013.pdf`, `.../2012/12/logo_Piovene_cru.jpg` (logo scaricabile).

## Da confermare con il cliente

- Ettari di vigneto (28 sul sito, circa 40 secondo Gambero Rosso 2022) e bottiglie annue.
- Annate in commercio, schede tecniche aggiornate (Thovara e passito fermi al 2015 e 2013), etichette attuali (le foto delle bottiglie sono del 2012), grafia dei nomi dei vini, se il Fostine è certificato biologico.
- Oli Delfo e Laudo: ancora prodotti? Denominazione esatta del Delfo.
- Alloggio nella colombara: ancora affittato? Foto attuali.
- Orari di apertura della cantina e del punto vendita, prezzi delle degustazioni (non pubblicati).
- Famiglia ed enologi attuali (testi del 2012).
- Numeri di cellulare attivi, PEC, codice SDI.
- Provenienza delle 6 foto con nomi nello stile di Flickr (pagina L'essenza e galleria "Saluti da Toara") e delle foto di Vicenza e Padova.
- Originali ad alta risoluzione: servizio di Nicola Zanettin, servizio del 27/06/2010 (vigneto e calici), foto di "Lele" (Olympus), video della vendemmia 2013.
- Shop: Vinix è ancora attivo? Vendita online o solo in cantina.

## Fonti

- Sito attuale www.piovene.com: 299 indirizzi seguiti dai link, 1700 ID provati (`?attachment_id=N`), 244 file di `wp-content/uploads`, 29 PDF.
- wordpress.org/download/releases e api.wordpress.org/core/stable-check/1.0/ (06/10/2026); php.net/eol.php e php.net/releases (PHP 7.4.10 del 03/09/2020).
- Google Maps, scheda "Piovene Porto Godi Alessandro s.s." (dati, orari, foto di terzi), letta il 06/10/2026.
- YouTube, canale @vinipioveneportogodi6555 (oEmbed dei due video collegati dal sito).
- Gambero Rosso International, "The discreet charm of Colli Berici a territory to discover, full of surprises", 21/04/2022 (gamberorossointernational.com/?p=395588).
- Non raggiungibili: Facebook (login), Wayback Machine (connessione chiusa), registri camerali e INI-PEC (captcha o blocco 403/429).
