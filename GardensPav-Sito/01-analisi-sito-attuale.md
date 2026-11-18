# 01. Analisi del sito attuale (www.gardenspav.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare, **[DA CONFERMARE]** dato da chiedere al cliente (va nel LEGGIMI).
Materiale di lavoro: crawl in `_prova/crawl/`, screenshot e misure in `_prova/attuale/` (`misure.json`), immagini in `assets/originali/` con `manifest.json`, inventario in `_prova/inventario-immagini.json`, URL in `_prova/url-vecchi.tsv`.

## In breve

- **Grafica del 2012 mai rifatta.** CMS proprietario della web agency Omniaweb (PHP su Apache, jQuery 1.7.1 del 2011), impaginazione XHTML a tabelle larga 930 px, fogli di stile e logo datati luglio-ottobre 2012. Nessun meta viewport: sul telefono la pagina viene disegnata a 980 px e rimpicciolita al 39,8%, il menu finisce a 4,8 px effettivi. Solo http: il certificato https è un autofirmato con nome "IT", scaduto l'11/03/2022. [Certo]
- **Contenuti danneggiati.** Le pagine italiane "L'Azienda" e "Caratteristiche e vantaggi" sono diventate righe di punti interrogativi (`Gardens - Pav Srl ????????`). In 54 delle 227 pagine scaricate (4 lingue) ci sono link nascosti verso 49 siti di orologi replica; in 4 pagine il testo estraneo si vede a schermo. Il titolo della home è "home italiano" e la sua meta description inizia con "Superreplica Miller-horloge". Sito quasi certamente violato: **argomento da dire a voce, non nella PEC né nella PROPOSTA scritta.** [Certo il contenuto, Probabile la causa]
- **Il patrimonio vero è tecnico.** Due linee di prodotto ben documentate: manufatti in calcestruzzo armato vibrato per il trattamento delle acque (10 schede con tabelle di misure, pesi e volumi) e piattaforme prefabbricate brevettate per autolavaggi (8 modelli con forniture comprese ed escluse, accessori, personalizzazioni). In più **36 realizzazioni** con galleria fotografica: Italia, Svizzera, Slovacchia, Francia, San Marino. [Certo]
- **Identità esistente.** Logo con simbolo "GP" in cerchio arancio **#F38239** e grigio **#58585A**, scritta GARDENS-PAV arancio, payoff "opere in calcestruzzo"; sfondo del sito in bianco e nero con anelli di calcestruzzo. Il segno più riconoscibile del prodotto è nelle foto: superficie antiscivolo a rombi del calcestruzzo grigio con il grigliato verde in vetroresina. [Certo]
- **Foto: tante e oneste, non professionali.** 398 file scaricati alla risoluzione massima: 262 foto di cantiere delle realizzazioni (68 a 1600 px, 20 a 900x1200, le altre a 800 px), 11 foto di prodotto e trasporto tra 1285 e 1600 px, 20 render dei manufatti a 1600 px su fondo bianco, 25 disegni quotati, 2 sfondi in bianco e nero a 1800 px. Nessuna foto dello stabilimento, della produzione o delle persone. Fuori dal sito nessuna foto: Google, Europages e Archilovers non ne espongono. [Certo]
- **Dati societari:** Gardens Pav S.r.l., P.IVA 03963070283, REA PD-351148, PEC **gardenspav@legalmail.it** (da registro, via aziende.it). Il certificato ISO 9001 pubblicato è **scaduto il 20/10/2025**: rinnovo [DA CONFERMARE]. [Certo]

## Pagine esistenti

Sito italiano (`www.gardenspav.it`), 82 URL validi. Menu alto: L'Azienda, Prodotti, Dove siamo, News, Contatti. Menu prodotti: Vasche prefabbricate monoblocco, Depurazione, Piattaforme per autolavaggi.

| Pagina | URL | Stato |
|---|---|---|
| Home | `/` (doppioni `/home`, `/home/`) | slider di 5 immagini (una è un volantino con testo), 3 riquadri con didascalia, nessun testo; link spam nascosti |
| L'Azienda | `/l-_azienda` | testo distrutto (punti interrogativi), elenco norme leggibile solo nei numeri, link a certificato ISO e Politica qualità (PDF) |
| Prodotti | `/prodotti` | griglia di 9 render con didascalia, nessun testo |
| Vasche prefabbricate monoblocco | `/vasche_prefabbricate_monoblocco` | 3 riquadri: rettangolari, circolari, trattate con resine epossidiche |
| Depurazione | `/depurazione` | 7 riquadri: dissabbiatore, separatore grassi, Imhoff, separatore oli, separatore oli per autorimesse, prima pioggia, depuratori biologici |
| Schede manufatti (10) | `/manufatti_per_la_depurazione_it/*.php` | testo tecnico, tabella dati, render e foto; spam nascosto in quasi tutte, visibile in 2 |
| Piattaforme per autolavaggi | `/piattaforme_per_autolavaggi` | slider di 3 foto, testo introduttivo, numero di brevetto, menu laterale di 12 voci |
| Caratteristiche e vantaggi | `.../caratteristiche_e_vantaggi.php` | testo distrutto (punti interrogativi), tabella attrito chiusa in un'immagine, foto "MAI PIÙ COSÌ!" |
| Schede piattaforme (8) | `.../piattaforma_per_pista_self_mod_450.php` ecc. | descrizione, forniture comprese, opzionali ed escluse, rendering e galleria |
| Esempio di posa | `.../esempio_di_posa.php` | solo un'immagine con didascalie dentro |
| Isola di aspirazione | `.../isola_di_aspirazione.php` | testo breve e 2 render |
| Personalizzazione (+3 sottopagine) | `.../personalizzazione.php` | calcestruzzo colorato, riscaldamento integrato, travi di rialzo |
| Realizzazioni | `.../realizzazioni.php` | griglia di 36 cantieri, ognuno con pagina e galleria (4,1 MB) |
| Dove siamo | `/dove_siamo` | mappa Google incorporata, nessun indirizzo scritto |
| News | `/news` | una sola voce, senza data, che porta a una pagina vuota; box newsletter Mailant |
| Contatti | `/contatti` (doppione `/contatti/`) | modulo con captcha, foto stock di un'operatrice |
| Privacy | `/privacy` | informativa GDPR; testo estraneo visibile |
| Cookie | `/cookie_info/` | informativa cookie generica |
| Pagina dell'agenzia | `/web-agency/omniaweb.php` | testo promozionale di Omniaweb |
| PDF | `/UserFiles/files/ISO-9001-...pdf`, `/UserFiles/files/politica_qualita.pdf` | certificato DNV 2022-2025, Politica per la Qualità 2018 |

Altre lingue, raggiungibili solo dalle bandierine IT e EN (DE e FR non hanno bandierina ma sono indicizzate da Google):

| Sottodominio | URL | Stato |
|---|---|---|
| Inglese `eng.gardenspav.it` | 56 | home e azienda tradotte; schede manufatti con titoli in italiano ("Vasche a pianta rettangolare EN"); "Supports for fences: Sezione in fase di aggiornamento."; 5 realizzazioni linkate sono pagine vuote; privacy ancora sul D.lgs. 196/2003 |
| Tedesco `deu.gardenspav.it` | 58 | home e pagina "Azienda (German)" **in italiano** (è l'unica copia rimasta del testo italiano originale), piattaforme in tedesco |
| Francese `fra.gardenspav.it` | 33 | home in francese, pagina "Azienda" in italiano, "Caractéristiques et avantages" in francese |

## Testi reali (verbatim, con i refusi originali)

Le citazioni sono copiate dalle pagine; tra parentesi quadre le mie note. Dove il testo contiene una parola della lista `PAROLE_VIETATE` la sostituisco con `[...]`; il trattino medio spaziato del sito è reso con un trattino semplice. Nel sito il nome compare in sei grafie: "Gardens - Pav S.r.l." (footer), la stessa con il trattino medio U+2013 tra le due parole, "GARDENS-PAV S.r.l.", "Gardens-Pav", "Gardens Pav", "GARDENS PAV S.R.L." (registro). Proposta per il nuovo sito: **Gardens Pav S.r.l.** come ragione sociale, **Gardens-Pav** solo come scritta del logo [DA CONFERMARE].

### Home
1. Nessun testo. Didascalie dei tre riquadri: "VASCHE PREFABBRICATE IN CEMENTO", "DEPURAZIONE", "PIATTAFORME PER AUTOLAVAGGI".
2. Home tedesca, ancora in italiano (`deu.gardenspav.it/home_de`): "Gardens - Pav S.r.l. opera nel campo della prefabbricazione offrendo i suoi prodotti al mercato nazionale e internazionale. L'azienda è specializzata nella produzione in calcestruzzo armato vibrato: Manufatti per il trattamento dei reflui domestici, industriali e delle acque meteoriche / Piattaforme per autolavaggi / Supporti per recinzione".
3. Home inglese: "Gardens - Pav S.r.l. works in the field of prefabrication offering its products to national and international markets. The company specialises in Products for the treatment of domestic and industrial waste water and rainwater / Platforms for car washes / Wall supports".
4. Volantino nello slider della home (testo chiuso nell'immagine, trascritto): "NOVITA' DAI LAVAGGI AUTO / PISTE DI LAVAGGIO PREFABBRICATE / • ANTISCIVOLO, SICURO APPOGGIO DEL PIEDE ANCHE CON PAVIMENTO BAGNATO • ANTIGHIACCIO, CON IL SISTEMA RADIANTE DI RISCALDAMENTO DEL PAVIMENTO • MONTAGGIO ULTRAVELOCE, IDEALE PER RISTRUTTURARE UN AUTOLAVAGGIO • CALCESTRUZZO RCK45 PER UNA MAGGIORE DURATA DELLE PISTE • PREDISPOSIZIONE DELLE TUBAZIONI PER LO SCARICO DELLE ACQUE PLUVIALI, DELLE LANCE E PER IL PASSAGGIO DEI CAVI DI ALIMENTAZIONE • ASSISTENZA AL MONTAGGIO CON NOSTRO PERSONALE • POSSIBILITÀ DI SMONTAGGIO E RIMONTAGGIO / GARDENS-PAV® opere in calcestruzzo / Via Romea, 154/a - 35020 LEGNARO - PD / Tel. +39 049 641591 - Fax +39 049 641913 - www.gardenspav.it - info@gardenspav.it".

### L'Azienda
La pagina italiana di oggi è illeggibile. Il testo originale italiano sopravvive in `deu.gardenspav.it/azienda_de` e `fra.gardenspav.it/azienda_fr`:

5. "Gardens - Pav S.r.l. opera soprattutto nel campo della prefabbricazione di manufatti in calcestruzzo armato per il trattamento dei reflui domestici, industriali e delle acque meteoriche."
6. "Ha raggiunto in quanto a produzione una posizione di [...] nel proprio settore grazie ad una continua ricerca di standard qualitativi rispondenti alle normative ed alle attese delle committenze più esigenti." [frase da non riprendere]
7. "Realizza inoltre piattaforme prefabbricate per autolavaggi e supporti per recinzioni in calcestruzzo armato. L'aggiornamento degli impianti e la costante innovazione dei processi produttivi costituiscono l'asse portante di una strategia che assicura competitività in un mercato in rapida trasformazione."
8. "La produzione mirata alla qualità, si avvale delle attuali e più avanzate tecnologie."
9. "L'impianto di calcestruzzo computerizzato a standard elettronicamente controllati miscela inerti, cemento, acqua e additivi chimici determinando un calcestruzzo con resistenza caratteristica cubica Rck 45 N/ mm2 e classe di consistenza S4. Il calcestruzzo è armato con acciaio B450C con copriferro di spessore cm.3."
10. "Le materie prime acquistate sono in possesso di tutti i requisiti di conformità e i manufatti sono realizzati nel rispetto delle seguenti normative:" D.M. 14/01/2008 "Norme tecniche sulle costruzioni"; Circolare n. 617 del 02/02/2009; UNI EN 206-1:2006; Linee Guida sul calcestruzzo preconfezionato (edizione Febbraio 2003); UNI 11104:2004; Circolare del 04/07/1996 n. 156 AA.GG./STC; D.M. 16/01/1996; "Uni En 858-1:2005 'Impianti di separazione per liquidi leggeri'"; "Uni En 1825-1:2005 'Separatori di grassi parte 1^'".
11. La versione italiana danneggiata di oggi era stata aggiornata: dai numeri ancora leggibili risultano D.M. 17/01/2018, Circolare 21/01/2019 n. 7 C.S.LL.PP., UNI EN 206-1:2016, UNI 11104:2016, UNI EN 1992-1-2, Regolamento 305/2011 (CPR), UNI EN 858-1:2005, UNI EN 1825-1:2005 e la certificazione "UNI EN ISO 9001:2015". Il testo di queste righe va riscritto con il cliente [DA CONFERMARE].
12. Europages (testo del profilo aziendale, probabilmente fornito dall'azienda): "L'azienda è specializzata nella produzione in calcestruzzo armato vibrato di: - Separatori Fanghi, Separatori Oli, Impianti per il trattamento delle acque di prima pioggia e delle acque reflue degli autolavaggi, Separatori Grassi, Vasche Imhoff, Depuratori Biologici ad ossidazione totale. - Vasche di accumulo per recupero acqua piovana, per impianti antincendio, raccolta acqua della piscina ad uso compensazione. - Piattaforme per postazioni di lavaggio auto prefabbricate, progettate per essere utilizzate come pavimentazione per autolavaggi, ottenendo nel giro di poche ore la pavimentazione operativa dell'autolavaggio self - service, del lavaggio auto per autorimesse, concessionarie, officine meccaniche, carrozzerie. Gardens - Pav progetta, produce ed installa le Piattaforme in Italia e in Europa con personale specializzato."
13. Politica per la Qualità (PDF, "Legnaro, lì 08/02/2018", firmata "L'Amministratore (Paolo Boato)"): "La ditta GARDENS PAV S.R.L., con un'ottica fortemente [...] e con mentalità costantemente rivolta allo sviluppo, pone al centro delle proprie attività la piena soddisfazione del Cliente [...]". "Il raggiungimento degli obiettivi aziendali è garantito dall'esperienza maturata nel settore in molti anni di attività, da continui investimenti in mezzi ed attrezzature [...]". Traguardi: "rispetto delle tempistiche contrattuali; consolidamento della presenza sul territorio; rafforzamento dei rapporti con i propri fornitori".
14. Campo applicativo del certificato DNV: "Fabbricazione di manufatti in calcestruzzo armato per il trattamento dei reflui domestici, industriali e delle acque meteoriche. Fabbricazione di piattaforme in calcestruzzo armato per autolavaggi".

### Manufatti per la depurazione
15. Paragrafo comune a vasche rettangolari, circolari, resinate e dissabbiatore: "Le vasche prefabbricate di tipo monolitico GARDENS-PAV S.r.l. sono realizzate in calcestruzzo armato vibrato in cassero tramite vibratore ad immersione ad alta frequenza, calcestruzzo in classe di resistenza a compressione C35/45 (RCK 45 N/mm2) conforme alle prescrizioni previste dalla norma UNI EN 206-1 per le classi di esposizione XC4 (resistente alla corrosione delle armature indotta da carbonatazione) XS1-XD2 (resistente alla corrosione delle armature indotta da cloruri anche di provenienza marina) XF1 (resistente all' attacco dei cicli di gelo/disgelo con o senza disgelanti) XA2 (resistente ad ambienti chimici aggressivi nel suolo naturale e nell' acqua presente nel terreno) e alle normative vigenti in materia antisismica (D.M. 14.01.2008 "Norme Tecniche per le Costruzioni" e D.M. 17.01.2018 Aggiornamento delle "Norme Tecniche per le Costruzioni"). Armature interne in acciao ad aderenza migliorata tipo B450C"
16. "Le vasche prodotte dalla GARDENS-PAV sono a tenuta idraulica e possono essere utilizzate per il recupero dell'acqua piovana, acque di prima pioggia, acqua potabile e accumulo per impianti antincendio."
17. Dissabbiatore: "I Dissabbiatori sono costituiti da una vasca monolitica a tenuta idraulica circolare o rettangolare corredata all'interno di un deflettore in pvc posto nel foro d'ingresso che rallenta il flusso dell'acqua. Qui il materiale pesante quale fanghi e/o sabbie si deposita sul fondo lasciando defluire l'acqua ed i liquidi leggeri verso l'uscita."
18. Separatore grassi: "I separatori grassi monoblocco prefabbricati costruiti secondo la Norma Europea UNI EN 1825-1:2005, vengono utilizzati ogni qualvolta sia necessario separare i grassi e gli oli di origine vegetale e animale dalle acque reflue di: Cucine per ristorazione collettiva e grandi stabilimenti di fornitura di pasti, per esempio presso alberghi, locande, stazioni di servizio in autostrade, mense; Impianti per grigliare, arrostire e friggere; Punti di distribuzione alimenti (con stoviglie a rendere); Macellerie con o senza impianti di macellazione; Stabilimenti di lavorazione carni e salumifici [...]; Impianti di macellazione pollame, di preparazione fast-food, di produzione patate e patatine fritte, di tostatura arachidi". "I Separatori grassi sono comprensivi di fori di entrata/uscita, raccordi in pvc con guarnizioni in gomma elastomerica sigillati a tenuta idraulica, deflettori di calma in pvc, parete divisoria centrale e paratie in acciao inox per il controllo del flusso e la separazione dei grassi e degli oli"
19. Vasca Imhoff: "Le fossa biologica Imhoff in cemento prefabbricata viene generelmente utilizzata come impianto di trattamento primario delle acque reflue di tipo domestico e/o assimilato, nei piccoli o medi impianti di depurazione. La principale funzione è quella di separare i materiali grossolani e di effettuare una prima fase di depurazione delle acque nere e cioè quelle provenienti dai servizi igenici (WC)". Segue la spiegazione dei due compartimenti (sedimentazione sopra, digestione sotto) e del funzionamento.
20. Separatore oli per superfici scoperte: "I separatori oli monoblocco prefabbricati con filtro a coalescenza e dispositivo di chiusura automativa vengono utilizzati per raccogliere le acque inquinate dal dilavamento di piazzali di officine meccaniche, stazioni di rifornimento carburante, autolavaggi, autodemolizioni."
21. Separatore oli per autorimesse: "I Separatori sono utilizzati per raccogliere le acque inquinate dalle eventuali perdite d'olio e idrocarburi delle autovetture in sosta durante il lavaggio pavimenti e rampe d' accesso, sono completi di filtro a coalescenza in acciaio inox. Trattano le acque da idrocarburi come previsto dal D.Lgs. 152/2006 [...] e i limiti del Decreto Ministeriale del 30/07/1999 per acque che recapitano nella Laguna di Venezia." "Sono conformi a quanto prescritto [...] (Decreto Ministeriale 01/02/1986) 'Norme di sicurezza antincendio per la costruzione e l'esercizio di autorimesse e simili'."
22. Prima pioggia: "Le superfici impermeabili o piazzali allo scoperto possono essere fonte d' inquinamento dovuto al dilavamento meteorico." "Vengono considerate acque di Prima Pioggia 'quelle corrispondenti per ogni evento meteorico ad una precipitazione di 5 mm uniformemente distribuita sull' intera superficie scolante servita dalla rete di drenaggio'". "L'acqua di prima pioggia defluisce alle vasche di accumulo nelle quali permane per un tempo di 48 ore per garantire la separazione del materiale pesante che si deposita sul fondo." "Si garantisce un'acqua in uscita con contenuto di oli minerali ed idrocarburi non superiore a 5 mg/litro."
23. Depuratori biologici: "Gli impianti di depurazione biologica ad ossidazione totale fanghi attivi vengono utilizzati per il trattamento delle acque reflue a servizio di case sparse, lotizzazioni private, campeggi, villaggi turistici, ristoranti, ospedali, scuole ed altre attività non servite da rete fognaria." "La digestione aerobica non produce odori molesti e il livello di rumorosità è contenuto entro limiti accettabili." Motivi della scelta: "L'esiguo numero di abitanti serviti. L'esemplificazione delle operazioni di manutenzione."
24. Chiusura ripetuta in quasi tutte le schede: "PER PORTATE SUPERIORI CONTATTARE IL NOSTRO UFFICIO TECNICO".

Dati delle tabelle (in `_prova/crawl/tabelle.json`, da ricopiare tali e quali nelle schede): vasche rettangolari da 205x120x150h (2,40 mc) a 1050x243x263h (50 mc, 27 t); circolari da Ø 148x206h (2,30 mc) a Ø 242x282h (9,80 mc); separatore grassi da 3 a 38 l/s; Imhoff da 5 a 70 abitanti equivalenti; separatore oli da 3 a 30 l/s; separatore per autorimesse fino a 7.000 mq e 450 posti auto (scarico in acque superficiali) e 2.300 mq e 180 posti (Laguna di Venezia); prima pioggia da 400 a 10.000 mq di superficie; depuratori BIO7-BIO20 e BIO5L-BIO15L (Laguna).

### Piattaforme per autolavaggi
25. "Gli autolavaggi self service richiedono fra le altre cose, una pavimentazione solida, su cui l'autoveicolo possa sostare, e inclinata per favorire il deflusso dell'acqua caduta e/o spruzzata sull'autoveicolo."
26. "Le nuove Piattaforme prefabbricate Gardens - Pav sono state progettate per essere utilizzate come pavimentazione per autolavaggi. Per ottenere la pavimentazione vengono accostati contrapposti quattro pannelli per la postazione di lavaggio per portali e due pannelli per la postazione di lavaggio per piste self."
27. "Le Piattaforme sono state studiate e realizzate con lo scopo di: realizzare pavimentazioni, aventi la finitura superficiale adeguata al deflusso dell'acqua e ad impedire scivolamenti; realizzare pavimentazioni senza necessità di allestire casseforme o strutture di contenimento; realizzare pavimentazioni senza deformazioni superficiali; realizzare pavimentazioni aventi la struttura, di calcestruzzo e di armatura, corretta e maturata senza sbalzi di temperatura e/o umidità. ridurre i tempi di realizzazione dell'autolavaggio.Infatti è sufficiente allestire il pozzetto centrale di scarico, gli scarichi e il sottofondo di appoggio e i pannelli vengono posati in breve tempo, ottenendo nel giro di poche ore la pavimentazione operativa dell'autolavaggio."
28. "BREVETTO PER INVENZIONE INDUSTRIALE DEPOSITATO N° 275.271" (nel sito inglese: "patent for industrial invention - application n° PD2011A000169").
29. Mod. 450: "La Piattaforma per postazione di lavaggio per pista Self Mod. 450 di dimensioni cm. 450x650 è costituita da n. 2 pannelli ad incastro di dimensioni ciascuno di cm. 228x650 dello spessore di cm. 20 e peso cadauno di Ton. 5,90. La piattaforma viene fornita completa della vasca di raccolta acque da lavaggio in calcestruzzo armato di dimensioni cm. 400x100x110h. e di grigliato in vetroresina anticorrosivo con superficie antiscivolo al quarzo, silice, in moduli di dimensioni cm. 200x100 con maglia 3,8x3,8x3,8h. di colore verde."
30. Forniture comuni a tutti i modelli: "SONO COMPRESI NELLA FORNITURA: La fascia in giuntoplasto adesivo per l'appoggio dei pannelli sul bordo della vasca. Le staffe e le viti in acciaio inox per il bloccaggio dei pannelli. I supporti porta grigliato in acciaio zincato. Il servizio di personalizzazione della piattaforma con tubazioni predisposte all'interno dei pannelli per lo scarico delle acque dei pluviali e delle lance, e per il passaggio dei cavi per l'energia elettrica. Il disegno con le fasi da seguire prima del posizionamento della piattaforma: tracciatura contorni della piazzola, posa vasca, esecuzione cordoli perimetrali, posa pannelli. L'installazione delle piattaforme in loco con il nostro personale. La relazione strutturale, la scheda tecnica, il piano di manutenzione. SERVIZI OPZIONALI: Trasporto con automezzi con e senza grù / Noleggio autogrù. SONO ESCLUSE DALLA FORNITURA: Opere edili in genere (scavo, sbancamento, piano di posa, realizzazione cordolo perimetrale per appoggio piattaforme) e relazioni di calcolo per opere edili."
31. Modelli: pista self Mod. 450 (450x650, 2 pannelli 228x650, 5,90 t); Mod. 500 (500x650, 2 pannelli 253x650, 6,70 t); Mod. 500 doppia griglia (2 vasche di raccolta); portale Mod. 1 (500x1200, 4 pannelli 253x600, 6,70 t); Mod. 2 (500x1100, 4 pannelli 253x550, 6,00 t, pozzetto escluso); Mod. 3 "sistema con lavaggio CHASSIS" (500x1200, 2 vasche); Mod. 4 "con area prelavaggio" e Mod. 5 (500x1300/1800, 6 pannelli, Rck 45, spessore 20 cm).
32. Isola di aspirazione: "Si tratta di una piastra prefabbricata, posata su un sottofondo predisposto a sostenerla, destinata ad essere basamento per impianti di aspirazione di modeste dimensioni È costituita da un unico elemento in calcestruzzo con resistenza caratteristica cubica Rck 45 N/mm2, spessore cm. 25, peso Ton. 2,50."
33. Calcestruzzo colorato: "Ogni tipologia di piattaforma (portale o self) può essere realizzata in calcestruzzo colorato con ossidi di ferro. Colori disponibili: ROSSO, VERDE, GIALLO, MARRONE."
34. Riscaldamento: "MAGGIOR SICUREZZA Attraverso un sistema di riscaldamento a pavimento (installato da Gardens Pav) si evita la formazione del ghiaccio a terra alle basse temperature." Esempi citati: "AUTOLAVAGGIO LUCENEC - SLOVACCHIA", "CENTRO DI LAVAGGIO SCI JANY WASH - FRANCIA".
35. Travi di rialzo: "Si tratta di una trave rovescia posizionata in parallelo alle piattaforme di autolavaggio e destinata ad essere basamento per eventuali sovrastrutture in acciaio. È costituita da un unico elemento in calcestruzzo con resistenza caratteristica cubica Rck 45 N/mm2, spessore cm. 30, peso Ton. 3,20."
36. Caratteristiche e vantaggi: l'italiano è perso; versione inglese: "DRAMATIC REDUCTION in car-wash construction times / DELIVERY of a standard products that can even be put into service on the day of construction / EASY INSTALLATION / SPECIAL SURFACE DESIGN ensures rapid water drainage and provides a secure grip for footwear even when wet / PIPING PROVIDED For the drainage of rainwater and washing water, and for [...] electrical power cable passages. / 45 N/MM2 CONCRETE For greater mechanical strength". Tabella attrito (chiusa in un'immagine, trascritta): coefficiente medio 0,64 su asciutto e 0,88 su bagnato riferito alla gomma 4S; 0,64 e 0,89 riferito al cuoio; limite D.M. 236 del 14/06/1989 art. 8.2.2: maggiore di 0,40.
37. Esempio di posa (didascalie dentro l'immagine): "piazzola prefabbricata 650x50 cm" [refuso: 650x500], "griglie in vetroresina PRFV", "supporti portagriglia in acciaio zincato", "sistema trattamento acque", "vasca sottopista di dimensioni 400x100x110h cm", "pietrisco tipo 4/8 spessore 20 cm", "cordolo perimetrale di magrone", "magrone di appoggio vasca sottopista".
38. Foto "MAI PIÙ COSÌ!": timbro arancio su un pavimento di autolavaggio rovinato (il messaggio è dentro l'immagine).

### Realizzazioni (36 nella pagina italiana)
39. Autolavaggi S. Mauro Pascoli (FC); Autofficina Poschiavo (Svizzera); Autolavaggio Abano Terme (PD); Autofficina Vezza D'Oglio (BS); Autolavaggio Biella; Carrozzo S.A.S. - Avetrana (TA); Autolavaggio Budrio (BO); Autolavaggio Cesena (FC); Autolavaggio Gavardo (BS); Autolavaggio Livorno; Autolavaggio Lucenec (Slovacchia); Autolavaggio Mottola (TA); Autolavaggio Piacenza; Autolavaggio Ponsacco (PI); Autolavaggio presso S.S. Esso Rovigo; Autolavaggio Rivalta (TO); Autolavaggio Rubano (PD); Autolavaggio S.Giovanni Persiceto (BO); Autolavaggio Tivoli Terme (ROMA); Autolavaggio Verona; Autotrasporti Verona; Concessionaria Crema; Lavaggio Auto Montanera (CN); Autolavaggio DPK S.R.L. - Milano (MI); Lavaggio Self Service Grugliasco (TO); Autolavaggio Fioretti - Borgosatollo (BS); Guglielmi Autocaravan - Alonte (VI); S.S. Q8 Easy - Cornate d'Adda (BG); Autolavaggio Pozzobon - Altivole (TV); Centro di Lavaggio Elite Wash Francia; Centro di Lavaggio Sci Jany Wash Francia; Autolavaggio Verduci F&C S.N.C. - Aosta (AO); Rossi Service S.r.l. - San Marino (RSM); Aquarama Gest S.r.l. - Pistoia (PT); Aquarama Gest S.r.l. - Viareggio (LU); Euroslam Service S.r.l. - San Lazzaro di Savena (BO).
40. Citati altrove ma senza pagina: "AUTOLAVAGGIO POPRAD AUTOUMYVARKA CARMINATI JEL" (Slovacchia, pagina vuota), Brendola (VI), Alessandria, "Portale Autosilver Crema", "Albocar Olbia" (pagine vuote nel sito inglese). Le pagine dei cantieri contengono solo foto: nessun anno, nessun modello, nessuna descrizione [DA CONFERMARE con il cliente anno e modello di ogni cantiere; nomi dei clienti da usare solo con il loro consenso].

### Contatti, News, Dove siamo, footer
41. Contatti: "Richiedi subito ulteriori informazioni, compila il modulo e sarai ricontattato al più presto:" campi Nominativo, Azienda, Provincia, Città, Telefono, Email, Note, codice di controllo, "Accetto il trattamento dei dati personali".
42. News: unica voce "INSTALLAZIONE CON TRAVI DI RIALZO E LOCALE TECNICO" (pagina vuota); box "Iscriviti alla newsletter". Sito inglese: "New Website / We are pleased to announce the publication of our website. Here's what you'll find: Simplified navigation / Optimized photos to show every detail / The most comprehensive product data sheets / Optimized for tablets and smartphones".
43. Dove siamo: solo la mappa Google e "Visualizzazione ingrandita della mappa".
44. Footer: "Gardens - Pav S.r.l. / sede legale e operativa: Via Romea, 154/A, 35020 Legnaro (Pd) / Tel. 049/641591 - Fax. 049/641913 | E-mail: info@gardenspav.it / Re. Impr. /C.F. e P.IVA 03963070283". Sotto: "Realizzato da Omniaweb".
45. Banner cookie: "Questo sito utilizza i cookie per migliorare servizi e esperienza dei lettori. Se decidi di continuare la navigazione consideriamo che accetti il loro uso." pulsanti "informativa" e "accetto".

Refusi da non riportare: "acciao" (acciaio, in 5 schede), "generelmente", "igenici", "suferficiali", "automativa", "lotizzazioni", "esemplificazione" (semplificazione), "Le fossa biologica", "La fosse Imhoff", "autolavaggio.Infatti", "grù", "N/ mm2", "in moduli di . 200x16", "con area prelavaggi" (menu) contro "prelavaggio" (pagina), "Autolavaggi S. Mauro Pascoli", "S.Giovanni", "650x50 cm", "ccGardens" (pagina tedesca), "Ai sensi dall'art. 13" (privacy), "Contact us to get more informations". Titolo pagina "Separatore Oli per il trattamento delle acque..." diverso dall'H1 "Separatore Oli CE con Filtro a Coalescenza".

## Cosa fanno o vendono

Produttore (non rivenditore) di manufatti in calcestruzzo armato vibrato, sede e stabilimento a Legnaro (PD), Via Romea 154/A. [Certo]

1. **Manufatti per il trattamento delle acque** (reflui domestici e industriali, acque meteoriche): vasche monoblocco rettangolari (11 misure) e circolari (6 misure), vasche trattate con resine epossidiche, dissabbiatori statici, separatori grassi CE (UNI EN 1825-1), vasche Imhoff, separatori oli CE con filtro a coalescenza (superfici scoperte e autorimesse, anche per scarico in Laguna di Venezia), impianti prima pioggia con accumulo e rilancio, depuratori biologici a ossidazione totale. Usi delle vasche: recupero acqua piovana, prima pioggia, acqua potabile, accumulo antincendio; da Europages anche "raccolta acqua della piscina ad uso compensazione". [Certo]
2. **Piattaforme prefabbricate per autolavaggi** (brevetto dichiarato): piste self 450 e 500, portali mod. 1-5, isole di aspirazione, travi di rialzo; personalizzazioni (calcestruzzo colorato in 4 colori, riscaldamento a pavimento antighiaccio, tubazioni predisposte). Clienti: autolavaggi self service, autorimesse, concessionarie, officine, carrozzerie, autotrasporti. [Certo]
3. **Supporti per recinzioni** in calcestruzzo armato: citati in home e Azienda (versioni DE e FR) e in EN ("Wall supports"), con una sola foto 202x133; la sezione è "in fase di aggiornamento" in tutte le lingue. Ancora in produzione? [DA CONFERMARE]
4. **Servizi**: ufficio tecnico per portate maggiori, installazione delle piattaforme con personale proprio in Italia e all'estero, relazione strutturale, scheda tecnica, piano di manutenzione, trasporto con e senza gru, noleggio autogrù, assistenza al montaggio, smontaggio e rimontaggio. [Certo, dal sito]
5. **Materiale**: calcestruzzo C35/45 (Rck 45 N/mm2), classe di consistenza S4, classi di esposizione XC4, XS1-XD2, XF1, XA2, acciaio B450C, copriferro 3 cm, impianto di betonaggio computerizzato. [Certo, dal sito]

Nota sul settore indicato nella scheda di partenza ("pavimentazioni per esterni, prefabbricati"): sul sito non compaiono pavimentazioni da giardino o autobloccanti; l'unica "pavimentazione" è quella delle piattaforme per autolavaggi. Il nome "Gardens Pav" fa pensare a un'origine diversa [Ipotesi], da chiedere al cliente, non da scrivere.

## Immagini usate oggi

Tutto in `assets/originali/` (398 file, nomi parlanti, `manifest.json` con URL di origine). Per le gallerie è stato preso il file caricato in origine, che il CMS conserva sopra la cartella `_bigPhotos`: 109 immagini sono così più grandi di quelle mostrate dal sito (75 arrivano a 1600 px, 22 a 900x1200, le altre da 500 a 600 px). Inventario completo con larghezza massima d'uso in `_prova/inventario-immagini.json`.

| Tipo | Quantità | Risoluzione | Giudizio e uso nel nuovo sito |
|---|---|---|---|
| Foto di cantiere delle realizzazioni (36 cantieri) | 262 | 68 a 1600x1200 o 1600x900, 20 a 900x1200, 174 a 800 px (alcune verticali 800x1066 e 800x1422) | Foto amatoriali ma vere: posa con autogru, pannelli nuovi, grigliati verdi, cantieri con recinzioni arancio. Luce varia, spesso cielo grigio, a volte l'ombra del fotografo. Le 1600 px reggono una mezza pagina a 1440 (800 px su retina); le 800 px solo griglia o card. Migliori: Altivole (TV), Pistoia, San Lazzaro, Milano DPK, Cornate d'Adda, Aosta. |
| Foto di prodotto, produzione e trasporto | 21 | 11 tra 1285 e 1600 px (trasporto vasca con autogru e montagne, autoarticolato carico, distesa di vasche circolari, batteria di vasche rettangolari, interni resinati rossi e azzurri, piattaforma riscaldata nella neve), 7 tra 594 e 901 px (due posa con autogru verticali), 3 miniature da 202 px | Le più forti per un'apertura: `foto-trasporto-vasca-autogru-cielo.jpg` (nitida al 100%, logo dipinto sulla vasca), `foto-vasche-circolari-piazzale-panoramica.jpg`, interni in resina rossa (colore pieno, unico nel materiale). |
| Slider piattaforme e gallerie dei modelli | 18 | 4 a 1600 px, 2 a 900x1200, 12 a 600 px | `foto-piattaforme-slide-2.jpg` e `-3.jpg`: dettaglio superficie a rombi e grigliato verde, nitidi; sono il "materiale" del marchio. |
| Sfondi in bianco e nero | 2 | 1800x1263 | Anelli di calcestruzzo e piattaforma: fascia larga fino a 1800 px (900 su retina). |
| Render dei manufatti su fondo bianco | 21 grandi + 19 piccoli | 20 a 1600x793 o 1600x731, trave di rialzo 1377 px; icone 190x145, sezioni 300-610 px | Stile coerente (vasche grigie con raccordi arancio). Ottimi per le schede prodotto; quelli in sezione con acqua blu e bordo rosso sono più vecchi e piccoli, da non mescolare. |
| Disegni quotati (piante ed esplosi delle piattaforme, colori) | 25 | 610 px circa, 4 a 1600 px | Utili nelle schede tecniche così come sono; testi piccoli dentro. |
| Testo chiuso in immagini | 4 | volantino 1600x1132, "MAI PIÙ COSÌ!" 1072x718, esempio di posa 623x480, tabella attrito 492x99 | Il testo va trascritto in HTML (fatto sopra, punti 4, 36, 37, 38). |
| Logo | 1 | PNG 358x75 | Troppo piccolo per retina; serve il vettoriale [DA CONFERMARE]. Colori misurati: arancio #F38239, grigio #58585A. |
| Marchio certificazione DNV ISO 9001 | 1 | 1302x1137 | Usabile solo se il certificato è in corso [DA CONFERMARE]. |
| Stock | 5 | onda blu, onda grigia con logo, operatrice con cuffia, euro, sveglia | Non usare. |
| Documenti | 2 PDF + 2 miniature | certificato DNV, Politica qualità 2018 | Il certificato è scaduto il 20/10/2025. |

Mancano: foto dello stabilimento di Legnaro, del piazzale con le vasche in luce buona, del getto e della vibratura, del personale al montaggio, di un autolavaggio finito e in uso, della superficie antiscivolo in macro. Brief da scrivere nel LEGGIMI.

Foto esterne: nessuna (dettagli in `assets/esterne/manifest.json`). La scheda Google è del proprietario ma espone solo una panoramica sferica del 28/07/2022, non scaricabile.

## Problemi tecnici da segnalare al cliente

Misure del 6/10/2026 con Chromium (Playwright) da rete cloud, cache vuota per ogni pagina, 19 pagine principali a 1440 e 390 px (`_prova/attuale/misure.json`, screenshot `NOME-1440.png` e `NOME-390.png`).

1. **Telefono: il sito non si adatta.** Nessun `<meta name="viewport">` su 19 pagine su 19. A 390 px il browser impagina a 980 px (`scrollWidth` 980, `innerWidth` 980) e rimpicciolisce al 39,8%: il menu da 12 px diventa 4,8 px effettivi, le tabelle tecniche da 13 px diventano 5,2 px; i paragrafi lunghi vengono ingranditi dal browser in modo disordinato. Prova: `home-390-come-sul-telefono.png`, `vasche-rettangolari-390-come-sul-telefono.png`. Il sito inglese dice "Optimized for tablets and smartphones". [Certo]
2. **Niente HTTPS.** Il sito risponde solo in http; su https il server presenta un certificato autofirmato "CN=IT", scaduto l'11/03/2022, e risponde 403. Chrome segna le pagine "Non sicuro"; il modulo contatti invia nome, telefono ed email in chiaro (`form method="POST" action="/contatti..."` su http). Prova: `_prova/attuale/https-prova.txt`. [Certo]
3. **Contenuti danneggiati e testo estraneo** (da dire a voce): "L'Azienda" e "Caratteristiche e vantaggi" in punti interrogativi (`prova-testo-rovinato-*.png`); testo di orologi replica visibile in "Vasche circolari" ("Jaeger-LeCoultre-replica-horloge"), "Privacy" ("Jaeger-LeCoultre Replica Watches", "bozidar"), "Dissabbiatore" ("[url=https://vcbeste.com]Vacheron Constantin Reissue Uhren[/url]"), "Portale Mod. 4" ("IWC replica watches" al posto della riga sui supporti zincati); link nascosti in 54 pagine verso 49 domini; meta description della home "Superreplica Miller-horloge...". Prova: `prova-spam-*.png`, `_prova/crawl/testi.txt` (righe `[SPAM: ...]`). [Certo]
4. **Privacy e cookie.** Google Analytics (`UA-33484881-1`) e Google Fonts partono su tutte le 19 pagine prima di qualsiasi consenso (2 o 3 richieste a `www.google-analytics.com` per pagina); "Dove siamo" carica la mappa Google prima del consenso (40 richieste per la mappa, 65 in tutto). Il banner considera consenso il "continuare la navigazione" e non ha un pulsante per rifiutare. Universal Analytics è stato dismesso da Google il 1/07/2023: lo script raccoglie dati che nessuno vede più. La privacy inglese cita ancora il D.lgs. 196/2003. Il banner (alto 51 px) copre il menu principale e metà del logo finché non si clicca "accetto": prova `testata-prima-del-consenso-1440.png` e `testata-dopo-il-consenso-1440.png`. [Certo il comportamento; la valutazione legale spetta al cliente]
5. **Dati societari incompleti nel footer.** Ci sono ragione sociale, sede, telefono, fax, email e "Re. Impr. /C.F. e P.IVA 03963070283"; mancano il capitale sociale (100.000 euro a registro, versato [DA CONFERMARE]) e l'ufficio del Registro Imprese (Padova), che l'art. 2250 c.c. chiede anche nel sito delle società. Non ci sono nemmeno REA (PD-351148) e PEC, non obbligatori ma utili a un cliente B2B. [Certo la mancanza]
6. **Contenuti fermi.** Certificato ISO 9001 pubblicato con validità "21 ottobre 2022 - 20 ottobre 2025" (scaduto da quasi un anno); Politica qualità del 08/02/2018; una sola news, senza data, che porta a una pagina vuota; "Supporti per recinzioni: Sezione in fase di aggiornamento." in tre lingue; nessun anno di copyright; ultimo file caricato il 28/09/2023 (intestazione `Last-Modified` del PDF ISO), grafica del 2012 (`base.css` 08/10/2012). [Certo]
7. **Pagine vuote e lingue a metà.** 2 link italiani portano a pagine vuote (news, Poprad), 5 nel sito inglese; ogni indirizzo inesistente risponde 200 con una pagina vuota (anche `robots.txt` e `sitemap.xml`, che quindi non esistono). DE e FR non sono nel menu ma sono indicizzati, con pagine in italiano. [Certo]
8. **Peso e velocità: accettabili tranne due pagine.** Pagine da 180 KB a 1,4 MB ("L'Azienda"), evento `load` tra 0,8 e 2,5 s. Eccezioni: "Realizzazioni" 4,1 MB e 57 richieste perché 13 foto da 1600 px sono mostrate come miniature da 150 px; "Dove siamo" 6,4 s per la mappa. Nessun errore in console (0 su 19 pagine), nessuna risorsa rotta, nessuna immagine ingrandita oltre la dimensione naturale a 1440. [Certo]
9. **Motori di ricerca.** Titolo della home "home italiano", nessun H1 in home, `keywords` vuote, testi alternativi delle foto "001.jpg", "002.jpg"; stesso contenuto su 4 sottodomini; l'indirizzo e gli orari non sono scritti in nessuna pagina (solo dentro la mappa). Scheda Google: categoria "Impianto depurazione acque" (sono un produttore), 3,3 su 4 recensioni. [Certo]
10. **Testi chiusi in immagini.** I 7 vantaggi delle piste (volantino), la tabella di attrito, le didascalie dell'esempio di posa, "MAI PIÙ COSÌ!": invisibili ai motori di ricerca e illeggibili sul telefono. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | GARDENS PAV S.R.L. (registro); "Gardens - Pav S.r.l." nel footer | aziende.it (fonte Registro Imprese, aggiornamento 08/07/2026); sito [Certo] |
| Forma | Società a responsabilità limitata | aziende.it [Certo] |
| P.IVA e C.F. | 03963070283 | footer del sito, aziende.it, Atoka [Certo] |
| REA | PD-351148 | aziende.it [Certo] |
| Iscrizione | 01/01/2005, CCIAA di Padova ("dal 2005"); Atoka indica 21 anni di anzianità | aziende.it, Atoka [Certo]. Data di costituzione esatta [DA CONFERMARE] |
| Sede legale e operativa | Via Romea 154/A, 35020 Legnaro (PD); coordinate 45.3389, 11.9733 (plus code 8XQF+H8) | footer, certificato DNV, Google [Certo] |
| Telefono | 049 641591 (+39 049 641591) | footer, volantino, Google [Certo] |
| Fax | 049 641913 | footer [Certo] |
| Email | info@gardenspav.it | footer, privacy [Certo] |
| PEC | gardenspav@legalmail.it | aziende.it, dato del Registro Imprese [Certo da fonte secondaria; verificabile su INI-PEC] |
| Codice destinatario SDI | J6URRTW | aziende.it [Certo da fonte secondaria] |
| ATECO | 23.61 Fabbricazione di prodotti in calcestruzzo per l'edilizia | aziende.it, Atoka [Certo] |
| Capitale sociale | 100.000 euro | aziende.it, Atoka [Certo; versato DA CONFERMARE] |
| Dipendenti | 12 (2024, aziende.it), 11 (Atoka); Europages dice "20-49" (profilo vecchio) | [Certo le fonti, numero da non pubblicare] |
| Fatturato | 2.167.025 euro (2024), 2.470.717 euro (2022) | aziende.it [Certo, da non pubblicare] |
| Amministratore | "L'Amministratore (Paolo Boato)" firma la Politica qualità del 2018; Atoka indica un Amministratore Unico senza nome | PDF sul sito [Certo per il 2018; attuale DA CONFERMARE] |
| Orari | lun-ven 08-12 e 14-18; sabato e domenica chiuso | Google Business, letto il 06/10/2026 [Certo; nel sito non ci sono] |
| Certificazione | ISO 9001:2015, DNV, n. 207763-2016-AQ-ITA-ACCREDIA, primo rilascio 19/10/2016, validità 21/10/2022-20/10/2025 | PDF sul sito [Certo; rinnovo DA CONFERMARE] |
| Brevetto | "BREVETTO PER INVENZIONE INDUSTRIALE DEPOSITATO N° 275.271"; EN: "application n° PD2011A000169" | sito [dichiarato dall'azienda, non verificato in banca dati brevetti] |
| Marchio | "GARDENS-PAV®" nel volantino | immagine sul sito [registrazione DA CONFERMARE] |
| Mercati | Italia (22 sigle di provincia nelle realizzazioni, dalla Valle d'Aosta alla Puglia), Svizzera, Slovacchia, Francia, San Marino | pagina Realizzazioni [Certo] |
| Lingue del sito | italiano, inglese, tedesco, francese | sottodomini [Certo] |
| Social | nessun link dal sito; nessuna pagina trovata su LinkedIn e YouTube; Facebook non verificabile senza accesso | [Certo per quanto controllato] |

Concorrenti indicati da Atoka come aziende simili in provincia (spunto per 02): Mengato, Prefabbricati Zanon, Valente, Micheletto, MS Depurazione, Manufatti Polonio.

## URL vecchi

228 URL validi, elenco completo con titolo in `_prova/url-vecchi.tsv` (82 italiani, 56 inglesi, 58 tedeschi, 33 francesi). Tutti http. Per `plugin/redirect-301.csv` servono almeno questi italiani:

```
/   /home   /home/   /l-_azienda   /prodotti   /dove_siamo   /news   /contatti   /contatti/   /privacy   /cookie_info/
/vasche_prefabbricate_monoblocco   /depurazione   /piattaforme_per_autolavaggi   /web-agency/omniaweb.php
/UserFiles/files/ISO-9001-207763-2016-AQ-ITA-ACCREDIA-3-it-IT-20221012-20221012085353.pdf
/UserFiles/files/politica_qualita.pdf
/manufatti_per_la_depurazione_it/vasche_rettangolari.php
/manufatti_per_la_depurazione_it/vasche_circolari.php
/manufatti_per_la_depurazione_it/vasche_trattate_con_resine_epossidiche.php
/manufatti_per_la_depurazione_it/dissabbiatore_statico.php
/manufatti_per_la_depurazione_it/separatore_grassi.php
/manufatti_per_la_depurazione_it/vasca_imhoff.php
/manufatti_per_la_depurazione_it/separatore_oli_in_continuo.php
/manufatti_per_la_depurazione_it/separatore_oli_ce_con_filtro_a_coalescenza_per_aut.php
/manufatti_per_la_depurazione_it/impianti_trattamento_per_acque_di_prima_pioggia.php
/manufatti_per_la_depurazione_it/depuratori_biologici_ossidazione_totale_fanghi_att.php
/piattaforme_per_autolavaggi/caratteristiche_e_vantaggi.php
/piattaforme_per_autolavaggi/piattaforma_per_pista_self_mod_450.php
/piattaforme_per_autolavaggi/piattaforma_per_pista_self_mod_500.php
/piattaforme_per_autolavaggi/piattaforma_per_pista_self_mod_500_doppia_griglia.php
/piattaforme_per_autolavaggi/piattaforma_per_portale_mod_1.php
/piattaforme_per_autolavaggi/piattaforma_per_portale_mod_2.php
/piattaforme_per_autolavaggi/piattaforma_per_portale_mod3_sistema_lavaggio.php
/piattaforme_per_autolavaggi/piattaforma_per_portale_mod_4_con_area_prelavaggio.php
/piattaforme_per_autolavaggi/piattaforma_per_portale_mod_5.php
/piattaforme_per_autolavaggi/esempio_di_posa.php
/piattaforme_per_autolavaggi/isola_di_aspirazione.php
/piattaforme_per_autolavaggi/personalizzazione.php
/piattaforme_per_autolavaggi/piattaforme_in_calcestruzzo_colorato.php
/piattaforme_per_autolavaggi/piattaforme_con_riscaldamento_integrato.php
/piattaforme_per_autolavaggi/installazione_con_travi_di_rialzo.php
/piattaforme_per_autolavaggi/installazione_con_travi_di_rialzo_e_locale_tecnico.php   (vuota)
/piattaforme_per_autolavaggi/poprad_autoumyvarka_carminati_jel_2.php                  (vuota)
/piattaforme_per_autolavaggi_5/autolavaggio_albocar_olbia_ot.php                      (vuota)
/piattaforme_per_autolavaggi/realizzazioni.php
```

Le 36 pagine dei cantieri (`/piattaforme_per_autolavaggi/<cantiere>.php`): aquarama_gest_srl_-_pistoia_pt, aquarama_gest_srl_-_viareggio_lu, autofficina_poschiavo_-_svizzera, autofficina_vezza_d-oglio_-_bs, autolavaggio_abano_terme_-_pd, autolavaggio_biella, autolavaggio_budrio_-_bo, autolavaggio_cesena_-_fc, autolavaggio_dpk_srl_-_milano_mi, autolavaggio_elite_wash, autolavaggio_fioretti_-_borgosatollo_bs_, autolavaggio_gavardo_-_bs, autolavaggio_livorno, autolavaggio_lucenec_-_slovacchia, autolavaggio_mottola_-_ta, autolavaggio_piacenza, autolavaggio_ponsacco_-_pi, autolavaggio_pozzobon_-_altivole_tv, autolavaggio_presso_ss_esso_rovigo, autolavaggio_presso_ss_q8_easy_-_cornate_d-adda_bg, autolavaggio_rivalta_-_to, autolavaggio_rubano_-_pd, autolavaggio_s_mauro_pascoli_-_fc, autolavaggio_sci_jany_wash, autolavaggio_sgiovanni_persiceto_-_bo, autolavaggio_tivoli_terme_-_roma, autolavaggio_verduci_-_aosta_ao_, autolavaggio_verona, autotrasporti_verona, carrozzo_sas_-_avetrana_ta, concessionaria_crema, euroslam_service_srl_-_san_lazzaro_di_savena_bo, guglielmi_autocaravan_-_alonte_vi, lavaggio_auto_montanera_-_cn, lavaggio_self_service_grugliasco_to, rossi_service_srl_-_san_marino_rsm.

I sottodomini `eng.`, `deu.` e `fra.gardenspav.it` vanno reindirizzati in blocco (alle pagine italiane o a una futura versione inglese) [DA CONFERMARE se il cliente vuole tenere l'inglese].

Fonti: sito www/eng/deu/fra.gardenspav.it (crawl del 06/10/2026); https://www.aziende.it/gardens-pav-s-r-l (dati Registro Imprese); https://atoka.io/public/it/azienda/gardens-pav-srl/3acfbaaae1f4; https://www.europages.it/GARDENS-PAV-SRL/00000003899039-187083001.html; https://www.archilovers.com/teams/70280/gardens-pav.html; scheda Google https://www.google.com/maps/place/?q=place_id:ChIJbQ_ElZHDfkcRCaj8RLz7rzQ. Wayback Machine non raggiungibile da questo ambiente (HTTP 429): da riprovare per foto più vecchie.
