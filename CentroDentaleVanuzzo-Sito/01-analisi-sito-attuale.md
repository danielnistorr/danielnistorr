# 01. Analisi del sito attuale (www.centrodentalevanuzzo.it)

Analisi del 13 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare, **[DA CONFERMARE]** dato da chiedere al cliente prima di usarlo.
Materiale di lavoro: 32 pagine HTML in `_prova/crawl/pagine/` (+ 3 pagine di sistema Jimdo `_prova/crawl/pagine-j-*.html`), testi estratti in `_prova/crawl/testi/`, esito dei link in `_prova/crawl/link.json`, misure Playwright in `_prova/attuale/misure2.json` (1440 e 390 su 33 pagine) e `_prova/attuale/rete.json` (peso al primo caricamento, 3 giri), screenshot in `_prova/attuale/`, inventario foto in `_prova/inventario-immagini.json`, foto esterne in `assets/esterne/manifest.json`.
Nei testi verbatim le parole della lista `PAROLE_VIETATE` (build.py) sono sostituite da **[PV]**: il nuovo sito non le riprende.

## In breve

- Sito Jimdo Creator con un template "classico" del 2017 (`layout.css?t=1500569401`, 20/07/2017), largo 984 px fissi, **senza meta viewport in nessuna delle 32 pagine**. Da telefono (390 px) la pagina resta larga 984 px e viene rimpicciolita al 39,6%: il testo da 15 px si legge a **5,9 px**; dove il browser del telefono ingrandisce da solo i paragrafi (22 px) si arriva a 8,8 px. Colori del logo: verde acqua `#0DA797`, verde scuro `#09776A`, fascia petrolio `#015C61` sotto la testata; testo in Verdana/Arial (dichiarati nel CSS), nome in corsivo dentro l'immagine della testata. [Certo]
- I contenuti sono fermi: l'ultima cosa datata è la newsletter ANDI del **25 maggio 2018** nella pagina "Questo mese..."; i curricula si fermano al 2013 (Dott.ssa Silvia Vanuzzo), 2015 (igienista) e 2017 (Dott. Nicola Vanuzzo). Il sito però è ancora curato a mano: foto caricate il 9/03/2024 (ritratto del Dott. Nicola Vanuzzo) e il 28/07/2025 (immagini di Endodonzia e Protesi). [Certo]
- La pagina **"Informazioni legali"** (`/about/`) mostra ancora il testo predefinito di Jimdo ("Questo è un sito creato con Jimdo Creator!..."): mancano sede legale, REA, P.IVA, PEC. La P.IVA compare solo nella pagina Contatti, non nella home né nel piede. [Certo]
- L'apertura della home è un **collage di volti di attori e attrici famosi** (lo stesso, a colori, nella pagina Estetica): problema di diritti d'immagine, da dire con tatto. [Certo]
- Il materiale fotografico vero c'è, ed è migliore di quanto il sito lasci vedere: **12 foto reali dello studio, 11 a 1820x1208 e una verticale 850x1280** (servizio fotografico Nikon D90 del 2013, caricate nel 2015) nascoste in uno slider da 481 px nella pagina Fotogallery, più **3 foto dello stesso servizio a 2048 px** caricate dal proprietario sul profilo Google. Persone: Dott. Nicola Vanuzzo al microscopio, Dott.ssa Silvia Vanuzzo con un bambino, le tre assistenti, un operatore con occhiali ingranditori. Quasi tutte le altre immagini delle pagine sono di repertorio, grafica o testo in immagine. [Certo]
- Testi forti e veri: il curriculum lungo dei due odontoiatri (lauree a Padova 2001 e 2003, master in Odontologia Forense, microscopia operativa a Genova), la pagina Tecnologia (scanner intraorale, cone beam, laser, microscopio "meglio vedi, meglio lavori"), la pagina bambini, la frase della Filosofia ("il nostro patrimonio più grande sono i nostri pazienti... la migliore pubblicità sono le loro parole"). [Certo]
- Società: Centro Dentale Vanuzzo S.a.s. di Vanuzzo Nicola & C., P.IVA 03717000289, iscritta il 01/10/2002, ATECO 86.23, 4 dipendenti (2022). Secondo studio a Camposampiero (Studio Dentistico Associato Grego, Vanuzzo, Vanuzzo, P.IVA 04200880286). Email non pubblicata (solo modulo), PEC non trovata. [Certo]

## Pagine esistenti

Menu di 11 voci, 19 sottopagine, più "Informazioni legali" e la sitemap. Tutte le 35 URL elencate rispondono 200; nessun link interno rotto.

| Pagina | URL | Stato |
|---|---|---|
| Home | `/` | pulsante Facebook, collage di volti famosi (512x384), "Un sorriso da STAR?", video YouTube bloccato finché non si accettano i cookie, link "PRENOTA UNA VISITA!" verso Contatti, citazione di Charlie Chaplin |
| Filosofia | `/filosofia/` | due frasi e un paragrafo, foto di repertorio (specchietto e sonda) |
| Il team | `/il-team/` | paragrafo "aria di Casa", immagine di repertorio (evidenziatore sulla parola "team") |
| Dott.ssa Silvia Vanuzzo | `/il-team/dott-ssa-silvia-vanuzzo/` | ritratto in bianco e nero (caricato l'1/03/2018), presentazione, curriculum 2001-2013 |
| Dott. Nicola Vanuzzo | `/il-team/dott-nicola-vanuzzo/` | ritratto al microscopio in bianco e nero (caricato il 9/03/2024), curriculum 2003-2017, due link ad associazioni (domini che non esistono più) e tre indirizzi scritti come testo (due non funzionano) |
| Igienista Romanato Loretta | `/il-team/igienista-romanato-loretta/` | collage in bianco e nero, curriculum 2003-2015 |
| Le nostre assistenti | `/il-team/le-nostre-assistenti/` | collage in bianco e nero delle tre assistenti, tre righe di testo |
| Cosa Facciamo | `/cosa-facciamo/` | titolo "Un servizio completo...a [PV]°", elenco in quattro punti, pittogramma del dente |
| Conservativa, Endodonzia, Chirurgia e Parodontologia, Implantologia, Ortodonzia, Protesi, Estetica, Igiene e Motivazione, Gnatologia | `/cosa-facciamo/<voce>/` | 9 pagine di un paragrafo ciascuna con firma del medico ("Dott.ssa Vanuzzo", "Dott Vanuzzo", "Romanato Loretta") e un'immagine di repertorio; Estetica ha in più il collage di volti famosi a colori e un elenco di 7 trattamenti |
| Speciale Bambini | `/speciale-bambini/` | tre righe e foto di repertorio |
| Ambienti, Ortodonzia Intercettiva, Attenzioni Particolari | `/speciale-bambini/<voce>/` | un paragrafo ciascuna; Attenzioni Particolari ha la foto vera della Dott.ssa Silvia Vanuzzo con un bambino |
| Tecnologia | `/tecnologia/` | quattro blocchi: impronta digitale intraorale, radiologia cone beam, laser, microscopio operatorio; immagini piccole dei produttori (277-336 px) |
| Gallery | `/gallery/` | solo il video YouTube dello studio (servizio Telenuovo, 20/02/2019) |
| Fotogallery | `/gallery/fotogallery/` | slider di 14 immagini: logo, 12 foto vere dello studio, una schermata clinica; nessun testo |
| Convenzioni | `/convenzioni/` | solo un'immagine con la scritta "Convenzioni" |
| Convenzione Mutua Certa | `/convenzioni/convenzione-mutua-certa/` | volantino in immagine, un indirizzo scritto come testo, link a un PDF che non esiste più |
| Convenzione Cadiprof/ANDI | `/convenzioni/convenzione-cadiprof-andi/` | titolo "Per i dipendenti degli Studi Professionali", banner Cadiprof, link con certificato non valido |
| Prezzi | `/prezzi/` | nessun prezzo: testo sul "vero risparmio", simbolo dell'euro in 3D |
| Questo mese... | `/questo-mese/` | titolo "NEWS ANDI DAL TUO DENTISTA", newsletter ANDI del 25/05/2018 in immagine (413 px, illeggibile), pulsante "Impronta Digitale Intraorale" verso una pagina 404, foto vera di un'impronta digitale |
| Contatti | `/contatti/` | dati delle due sedi, due mappe Google bloccate finché non si accettano i cookie, modulo (Nome, Ditta, Email, telefono, Messaggio, codice di controllo) |
| Informazioni legali | `/about/` | testo predefinito di Jimdo, nessun dato dello studio |
| Sitemap | `/sitemap/` | elenco delle pagine |
| Pagine di sistema Jimdo nel piede | `/j/privacy`, `/j/legal-guarantee`, `/j/withdrawal` | informativa generica di Jimdo; "Garanzia legale" e "Recedere dal contratto" sono pagine da negozio online, fuori luogo per uno studio dentistico |

In tutte le pagine: testata-immagine con il nome e "... il TUO studio Odontoiatrico!", menu a sinistra, colonna destra con "Il Dentista... proprio come lo vorresti!" (due H1), pulsanti per condividere su Facebook e X, logo piccolo con "Home". Sullo sfondo una slideshow di 22 immagini 1280x720 (20/07/2017) quasi bianche, con piccole bocche in bianco e nero ai lati.

Non esistono: blog o notizie aggiornate, orari, email, pagina privacy dello studio, pagina cookie dello studio, versione in altre lingue, prezzi.

## Testi reali (verbatim, con i refusi originali)

Le lineette "–" del sito sono rese con "-". "[PV]" = parola della lista vietata, omessa.

### Home
1. Titolo della pagina: "Clinica Odontoiatrica Padova - Centro Dentale Vanuzzo, Odontoiatria e Qualità a Padova". Description: "Finalmente uno studio dentistico a cui importa veramente la tua salute orale. Vieni per una visita gratuita a Padova"
2. H1 "Un sorriso da STAR?" / H2 "...oggi è più facile di quanto tu creda!!!" / "Vieni a scoprire le nuove tecniche per avere un SORRISO ...a prova di "PRIMO PIANO""
3. "PRENOTA UNA VISITA!" (nel codice è spezzato in due: "PRENOTA UNA VISI" + "TA!"; a schermo si legge intero)
4. "Perché "Un giorno senza un sorriso è un giorno perso"" / "Charlie Chaplin"
5. Colonna destra, in ogni pagina: "Il Dentista..." / "proprio come lo vorresti!". Testata: "Centro Dentale Vanuzzo ... il TUO studio Odontoiatrico!" (dentro l'immagine).

### Filosofia
6. "Perché il nostro patrimonio più grande sono i nostri pazienti...." / "....la migliore pubblicità sono le loro parole."
7. "PRENOTA una visita al Centro Dentale Vanuzzo, ti offriremo la nostra professionalità ed il nostro tempo, per ascoltarti, capire le tue esigenze e poterti proporre le soluzioni terapeutiche più adatte al tuo caso, in modo che TU possa scegliere la terapia su misura per te, perché ogni paziente è unico."
8. Titolo della pagina: "IL DENTISTA MODERNO: la nostra interpretazione filosofica". Description: "Il nostro patrimonio sono i nostri pazienti, la migliore pubblicità sono le loro parole"

### Il team
9. "Ci piace pensare che al Centro Dentale Vanuzzo si respiri aria di "Casa", aria di "Famiglia", perchè è così che ci sentiamo: una Grande Famiglia."
10. "Come un squadra lavoriamo insieme ormai da molti anni, ognuno con il proprio ruolo. Questo è indispensabile per poter gestire al meglio ogni singolo caso in tutti i suoi aspetti. Se un componente della squadra non svolgesse i propri compiti, tutta la squadra ne risentirebbe e i risultati non arriverebbero."
11. "Ed è con fierezza che vi presentiamo i componenti del nostro team, con la loro professionalità e la [PV] per quello che fanno."

### Dott.ssa Silvia Vanuzzo
12. "Odontoiatra e Direttore Sanitario della struttura, specializzata nella cura e nel recupero dello stato di salute dei vostri denti. Utilizza strumenti [PV] per ottenere risultati di [PV] in endodonzia e conservativa. Formidabile con i bambini si occupa con [PV] di pedodonzia e ortodonzia."
13. "Laureata in Odontoiatria e Protesi Dentaria presso l'Università di Padova nel 2001, è iscritta all'albo dei Medici e Chirurghi ed Odontoiatri di Padova."
14. Corsi (elenco del sito): "STRUMENTI D'AVAGUARDIA E TECNICHE EVOLUTE DELL'ENDODONZIA MODERNA (2002)"; "ORTOGNATODONZIA OGGI: DALLA DIAGNOSI ALLA TERAPIA (2002-2003)"; "CORSO DI ORTODONZIA INTERCETTIVA E PREVENTIVA (2003)"; "CORSO TEORICO PRATICO DI ENDODONZIA CLINICA DALLA PREPARAZIONE ALL'OTTURAZIONE CANALARE (2003)"; "STRUMENTI ROTANTI NI-TI SISTEMA MTWO (2004)"; "THE ULTIMATE ENDO-RESTORATIVE DENTISTRY (2004)" e "(2005)"; "CORSO TEORICO PRATICO INTRODUTTIVO ALLA TECNOLOGIA LASER (2004)"; "CORSO DI PERFEZIONAMENTO IN ENDODONZIA (2004)"; "ODONTOIATRIA RESTAURATIVA CONSERVATIVA ADESIVA (2005)"; "APPROFONDIMENTI DI ODONTOIATRIA CONSERVATRICE (2005-2006)"; "CERTEZZE CONTROVERSIE E PROSPETTIVE FUTURE IN ENDODONZIA (2006)"; "UTILIZZO DEI FILLER NELLA PRATICA ODONTOIATRICA (2011)"; "BELLEZZA CON SICUREZZA Andi (2013) utilizzo dei filler nel periorale"; "Socio di POIESIS (perioral and oral integrated esthetic sciente italian society)"; "Socio ANDI (Associazione Nazionale Dentisti Italiani)".
15. "Dal 2001 ad oggi esercita la libera professione occupandosi principalmente di conservativa, endodonzia , ortodonzia ed estetica periorale."
16. "Si dedica con [PV] alla pedodonzia, con metodi di relazione e approccio adatti ai piccoli pazienti."
17. "Relatrice a numerosi incontri presso asili, scuole, farmacie, e altro, su una corretta informazione odontoiatrica di prevenzione e cura per i bambini fin dalla nascita e nelle varie tappe della crescita."
18. Description: "La Dott.ssa Silvia Vanuzzo si occupa della salute orale dei piccoli e grandi pazienti. Esperta in odontoiatria infantile, ortodonzia, conservativa, endodonzia"

### Dott. Nicola Vanuzzo
19. "Odontoiatra, Professore a C. presso l'UNIVERSITA' DI GENOVA, si occupa di protesi e chirurgia, intervenendo per risolvere, recuperare e migliorare situazioni dentarie compromesse, utilizzando strumenti, materiali e tecniche di [PV] per ottenere i migliori risultati sia funzionali sia estetici. E' microscopista e si occupa di Chirurgia con approccio mininvasivo, Protesi ed Iplantologia con tecniche digitali."
20. "Laureato con lode in Odontoiatria e Protesi Dentaria presso l'Università di Padova nel 2003, è iscritto all'albo dei Medici e Chirurghi ed Odontoiatri di Padova."
21. Corsi (elenco del sito, 28 voci 2003-2017, alcune): "ADVANCED TECNIQUE AND BIOLOGICAL ASPECTS IN IMPLANTOLGY (New Jersey 2003)"; "ONE DAY IMPLANT (2004)"; "III CONGRESSO INTERNAZIONALE PARODONTOLOGIA LASER ASSISTITA (2004)"; "LA CHIRURGIA MUCOGENGIVALE STATO DELL'ARTE (2005)"; "G.I.R. DAY ROMA CHIRURGIA IN DIRETTA (2005)"; "5TH WORLD CONGRESS OF OSSEOINTEGRATION (2007)"; "IL CARICO IMMEDIATO IN IMPLANTOLOGIA (2007)"; "10° CONGRESSO NAZIONALE AIOM (accademia italiana odontoiatria microscopica) (2007)"; "CHIRURGIA PRE-IMPLANTOLOGICA NELLA RIABILITAZIONE ESTETICA DELLE GRAVI ATROFIE DEI MASCELLARI (2008)"; "FOTOGRAFIA DIGITALE IN ODONTOIATRIA (2009)"; "MASTER II LIVELLO IN ODONTOLOGIA FORENSE presso Università di Firenze (2012)"; "Corso di perfezionamento in "MICROSCOPIA OPERATIVA ODONTOIATRICA" presso università di Genova (2013)"; "Corso di perfezionamento in "UTILIZZO DEL LASER E DELLE NUOVE TECNOLOGIE IN ODONTOSTOMATOLOGIA"(2014)"; "°Tutor Al Master di "Laser e Nuove Tecnologie" università di Genova (2015-2016-2017)".
22. "Dal 2003 ad oggi esercita la libera professione, occupandosi principalmente di Protesi e Chirurgia. Professore a C. presso il reparto di odontostomatolgia dell'UNIVERSITA' DI GENOVA, Microscopista e frequentatore della New Jersey Dental School. Socio Attivo e segretario Nazionale del GIR (Groop for Implant Reserch). Socio Attivo dell'AIOM (Accademia Italiana di Odontoiatria Microscopica), Master di II livello in Odontologia Forense, esperto in tecnologie digitali e relatore in diversi corsi e conferenze."
23. In fondo, scritti come testo: `http://www.sympla-gtb.it/nicola-vanuzzo/`, `http://www.dossiersalute.com/centri-medici/odontoiatria-e-implantologia/dott-nicola-vanuzzo/`, l'articolo su dental-tribune.com.
24. Titolo della pagina: "Dott. Nicola Vanuzzo: Odontoiatria Digitale-Implantologia guidata e a Carico Imediato- Protesi estetica". Description: "Professore A.C. presso Università di Genova, esperto in chirurgia microscopica mininvasiva e tecnologie digitali, odontologo forense"

### Igienista Romanato Loretta
25. "Dottoressa in Igiene Dentale si occupa del mantenimento dello stato di salute dei vostri denti e delle vostre gengive, con sedute di igiene professionale, motivando e insegnando al paziente anche il corretto utilizzo degli strumenti di pulizia quotidiana."
26. "Laureata a pieni voti in Igiene Dentale presso l'Università di Bologna nel 2003" (segue elenco di 15 corsi 2004-2015, tra cui "LAUREA SPECIALISTICA IN SCIENZE DELLE PROFESSIONI SANITARIE TECNICHE ASSISTENZIALI, presso l'Università degli studi di Firenze (2008)", "CORSO DI PERFEZIONAMENTO IN "Laser e nuove tecnologie nel distretto facciale", Genova (2014)", "CORSO DI AGGIORNAMENTO PROFESSIONALE IN "Approccio Olistico in Odontostomatologia", Università degli studi di Milano, ... Novembre 2014- Marzo 2015").

### Le nostre assistenti
27. Titolo: "Le Nostre Super-Assistenti". Didascalia: "Il team odontoiatrico". "Fabiola, Monica e Patrizia: Assistono, coadiuvano e coordinano tutti iservizi dellostudio,dalle attività cliniche alla disinfezione degli ambienti e sterilizzazione dello strumentario, alla presa degli appuntamenti per soddisfare il più possibile le vostre esigenze e rispondere a tutte le vostre richieste."

### Cosa Facciamo
28. H1 "Un servizio completo...a [PV]°" / H2 "Tutta l'odontoiatria e la cura della salute e dell'estetica della tua bocca"
29. "Perchè il nostro obiettivo è dare al paziente tutto quello che serve per: -Fare una corretta DIAGNOSI della sua situazione orale e generale -Conoscere quali sono le sue ESIGENZE, richieste, difficoltà e problemi -Studiare con lui il più corretto PIANO DI TRATTAMENTO tra i moltissimi possibili -Mettere in campo tutta l'esperienza e la professionalità dei nostri operatori, impegno e le TECNOLOGIE di ultima generazione per lavorare con la massima QUALITA' ai minimi COSTI"

### Le nove pagine di "Cosa Facciamo"
30. Conservativa: "Parte dell'odontoiatria che si occupa della cura di carie, erosioni, abrasioni cercando di conservare il più possibile i denti naturali del paziente e ricostruendo tali lesioni con materiali da restauro secondo tecniche affinate per garantire il miglior risultato estetico e funzionale. -Dott.ssa Vanuzzo -"
31. Endodonzia: "Quando l'insulto batterico arriva alla polpa del dente causa pulpiti,lesioni periapicali,granulomi e ascessi. Della risoluzione di tali patologie si occupa l'endodonzia: con tecniche [PV] permette la devitalizzazione degli elementi dentari malati, con la rimozione della polpa infetta e la detersione e disinfezione del complesso sistema di canali che costituiscono l'endodonto e la loro otturazione. Se alla fine del trattamento il dente è troppo debole è possibile inserire nei canali radicolari un perno in fibra di vetro o carbonio che faccia da anima solida per rendere più efficiente il successivo restauro protesico o conservativo. -Dott.ssa Vanuzzo -"
32. Chirurgia e Parodontologia: "Interventi di chirurgia orale vengono svolti con grande professionalità ed esperienza, dalle semplici estrazioni ad operazioni più complesse come la chirurgia preprotesica o preimplantare. Interventi di chirurgia paradontale atti a migliorare il supporto dei denti naturali (osso e gengive) con la rimozione dei tessuti infetti e la possibilità di eseguire innesti d'osso ed interventi di gengivo-plastica per recuperare e mantenere il più possibile lo stato di salute e di bellezza del sorriso del paziente. -Dott Vanuzzo -"
33. Implantologia (didascalia "Centro di [PV] in implantologia"): "I nostri denti sono un bene prezioso e nulla può sostituirli appieno...ma quando uno o più elementi dentari sono andati persi un ottima soluzione è quella di inserire nell'osso dei mascellari degli impianti: "viti" in titanio che grazie alla grande biocompatibilità di questo materiale si osteointegrano diventando un "tuttuno" con l'osso di sostegno. Una volta osteointegrato un impianto viene utilizzato come supporto protesico, dal singolo dente fino alla protesi totale. - Dott Vanuzzo -"
34. Ortodonzia: "Lo sviluppo delle ossa mascellari e della dentatura è un processo lungo e complesso che spesso non avviene in armonia ed equilibrio. Questo si traduce in malocclusioni dentarie. La maggior parte di queste trova origine in disarmonie scheletriche mascellari o mandibolari che possono essere corrette solo in fase di sviluppo. Per questo motivo vanno intercettate con le più aggiornate tecniche di cefalometria in fase infantile ed adolescenziale e corrette con i più appropriati apparecchi fissi o mobili. Molti problemi dentali possono poi essere corretti anche in età adulta. - Dott.ssa Vanuzzo-"
35. Protesi: "Quando un dente è troppo danneggiato per essere ricostruito o quando è andato perso: capsule, ponti e protesi più estese vengono studiate e realizzate per restituire al meglio la funzionalità e l'estetica della bocca del paziente. Ogni problema presenta più soluzioni e diversi materiali per realizzarle: verranno discusse tra medico e paziente per trovare quella più adatta alle esigenze di quest'ultimo. -Dott Vanuzzo-"
36. Estetica: "Il trattamento odontoiatrico si compone di riabilitazioni funzionali, ma anche ESTETICHE. Nella nostra società è sempre più importante apparire ed il nostro sorriso è il primo biglietto da visita. Al Centro Dentale Vanuzzo si eseguono trattamenti atti a migliorare l'estetica dei denti con faccette e sbiancamenti, delle gengive con interventi di gengivoplastica e dei tessuti periorali con Filler." Elenco: "Sbiancamento / Ricostruzioni Estetiche / Faccette / Filler / Corone integralmente in Ceramica (metal Free) / Ortodonzia Invisibile / Smile design Digitale". Chiusa: "Oggi avere un sorriso da STAR è più facile di quanto tu creda! Vieni per una visita, così da poter valutare il tuo caso."
37. Igiene e Motivazione: "Il punto di partenza per la salute di una bocca è l'igiene: quella quotidiana che ciascun paziente deve svolgere con spazzolino e filo interdentale, e quella professionale da svolgere almeno ogni 6mesi nello studio. Tale pulizia rimuove il tartaro che fisiologicamente si forma sui denti, nei solchi e nelle tasche gengivali con effetti irritanti e destruenti per denti e gengive. Utilizza strumenti ultrasonici e courette. Mediante l'utilizzo di polvere di bicarbonato spruzzata ad alta pressione è poi possibile eliminare macchie di caffè, the o nicotina. Per chi lo desidera lo studio offre un servizio di richiamo periodico quando si avvicina il momento di ripetere una pulizia. -Romanato Loretta-"
38. Gnatologia (titolo "Gnatologia e Riabilitazione Miofunzionale"): "La terapia gnatologica consiste nel ristabilire i normali rapporti fra condilo mandibolare, disco articolare e fossa glenoide. Pertanto è la posizione mandibolare reciprocamente al cranio che fa la differenza tra successo ed insuccesso. Allo scopo servono manufatti prevalentemente di resina (Ortotici Miofunzionali) che riposizionano la mandibola producendo allo stesso tempo un rilassamento muscolare dei muscoli masticatori e di tutti gli altri muscoli interessati. Una volta eliminate le contratture si procede alla terapia di stabilizzazione dei risultati, che può prevedere la correzione occlusale per apposizione, per sottrazione o per modifica tramite ausili che possono andare da un semplice molaggio selettivo per eliminare interferenze (a volte causate da restauri malposti), ad un ripristino delle corrette altezze tramite onlays, corone o delle edentulie tramite protesi, infine si possono modificare posizioni dentali tramite ortodonzia."

### Speciale Bambini
39. "Se ogni paziente è unico... i "piccoli" pazienti rappresentano proprio un mondo a parte, che richiede: - ambienti idonei - tecniche particolari - attenzioni speciali". Description: "Pazienti "speciali" come i bambini richiedono attenzioni particolari"
40. Ambienti Dedicati: "Pazienti "Speciali"come i bambini richiedono ambienti dedicati, idonei a metterli a proprio agio. Certo tali ambienti devono essere dotati di tutte le più recenti attrezzature e permettere il mantenimento del più alto grado di disinfezione e sterilizzazione. Ma tutto ciò può essere fatto senza impressionare o traumatizzare i nostri piccoli pazienti."
41. Ortodonzia Intercettiva: "La fase della crescita è una fase molto delicata. Molte cose possono accadere nello sviluppo di mandibola, mascelle, palato, masticazione. Proprio in questa fase possono essere corretti alcuni equilibri muscolo-scheletrici e rapporti dentali, in modo semplice e rapido, sfruttando proprio la spinta della crescita. Certi problemi, se prevenuti in tempo, sono di facile soluzione...se trascurati, in età adulta possono causare serie disfunzioni o richiedere invasivi interventi chirurgici."
42. Attenzioni particolari (didascalia "Dr.ssa Vanuzzo e i suoi piccoli pazienti", alt "I pazienti più piccoli richiedono le più grandi attenzioni"): "I bambini nascono senza paure, e queste gli possono venire trasmesse solo dalle persone che gli stanno intorno (genitori, amici, parenti...),o da esperienze traumatiche. Per questo i bambini devono essere considerati pazienti che vanno trtattati con Attenzioni Particolari, in modo da non accumulare traumi. Per loro deve essere quasi un gioco andare dal dentista. In questo modo si trasformano nei migliori pazienti che si possa avere. E La dr.ssa Silvia Vanuzzo, con la sua professionalità e l'esperienza decennale in "baby Pazienti", riesce sempre a trovare la sintonia necessaria con i tanti bambini che si recano nel nostro studio, come solo una mamma sa fare."

### Tecnologia
43. Impronta Digitale Intraorale: "Perché sopportare minuti interminabili con un cucchiaio di pasta gommosa, soffocante e spesso di sapore poco gradevole, quando oggi la tecnologia ci ha messo a disposizioni uno strumento [PV]: lo scanner intraorale?. Tale strumento, mediante una scansione che unisce 20 fotogrammi al secondo, crea un modello tridimensionale della cavità orale. Ciò permette non solo un confort mai provato durante la presa dell'impronta, ma soprattutto una precisione e l'accesso diretto a nuovi materiali Hi Tech che sfruttano il massimo delle potenzialità CAD CAM."
44. Radiologia Tridimensionale Cone Bean: "Nuova generazione di strumenti radiologici che permette la ricostruzione in 3D dei tessuti orali e periorali, con assoluta precisione e dosi assolutamente basse di radiazioni, dosaggi fino a poco tempo fa impensabili anche per esami molto meno approfonditi. Tale tipo di indagini radiologiche apre nuovi orizzonti per l'integrazione digitale dei sistemi tecnologici dello studio odontoiatrico. Permette la programmazione di interventi con altissima precisione e predicibilità e radiologicamente guidati."
45. "Nuova frontiera per odontoiatria: la luce Laser": "La tecnologia Laser permette oggi interventi, anche senza anestesia, con guarigioni sorprendenti e veloci. Le caratteristiche principali di tale sorprendente tecnologia sono la capacità di lavorare sui tessuti duri e molli, lasciando un substrato esangue, sterile e con una intensa biostimolazione dei tessuti verso la guarigione. Mediante questi strumenti, alcuni interventi sono stati rivoluzionati: - Piccole e grandi chirurgie - Desensibilizzazione - Pulizia delle tasche parodontali che permette il mantenimento dei propri denti. - Gengivoplastica - Frenulectomia - Herpes Labialis e tante altre possibilità."
46. Microscopio Operatorio: "Con la possibilità di vedere il proprio operato ingrandito fino a 20 volte, con una illuminazione coassiale, è possibile vedere tutto quello che a occhio nudo non è possibile fare. Al Centro Dentale Vanuzzo il microscopio è un ausilio di routine, nella convinzione che: "meglio vedi, meglio lavori""

### Convenzioni
47. Mutua Certa: solo didascalia "Mutua Certa" e l'indirizzo `http://www.upa.padova.it/sp/certa.3sp` scritto come testo; il volantino porta al PDF `slidemutuacerta5.0DEF.pdf` (404).
48. Cadiprof/ANDI: H1 "Per i dipendenti degli Studi Professionali" e il banner Cadiprof; nessun testo.

### Prezzi
49. "Se questa è una delle prime pagine del nostro sito che avete visitato, forse non vi state prendendo cura della vostra salute orale nel modo più corretto. Nonostante viviamo tempi difficili in cui è importante il risparmio, dobbiamo però interrogarci su quale sia il "VERO RISPARMIO". Il "prezzo più basso" non rappresenta necessariamente un risparmio...soprattutto se non siamo in grado di valutare bene per cosa dobbiamo pagare. Non c'è euro più sprecato di un euro speso per qualcosa che non volevate."
50. "E' importante che troviate professionisti competenti (valutate i loro curricola), che si preoccupino prima di fare una diagnosi corretta, e che in seguito vi propongano tutte le alternative terapeutiche possibili per risolvere il vostro problema (spesso queste alternative sono molte), in modo che solo voi possiate scegliere, con cognizione di causa, quella più adatta al vostro caso. Inoltre dovete cercare un Centro Odontoiatrico al quale affidarvi con FIDUCIA, con professionisti che rispondono del proprio operato dandovi garanzia e supporto nelle fasi post-intervento. Un Centro Odontoiatrico che impieghi il massimo della tecnologia prima per migliorare la qualità dei suoi trattamenti e poi per diminuirne i costi. Al Centro Dentale Vanuzzo troverete tutto questo."
51. "I nostri prezzi? non sono aumentati di un euro negli ultimi 5 anni. Anzi grazie al nostro continuo programma di investimento in nuove tecnologie e le conseguenti semplifiazioni procedurali, siamo riusciti a ridurre molti costi e molti dei prezzi delle nostre prestazioni. Ma se volete un preventivo personalizzato, per il piano di trattamento adatto al vostro caso, venite per una visita senza impegno. Studieremo eventualmente anche la formule di pagamento più convenienti o pià adatte alle vostre esigenze."

### Questo mese...
52. H2 "NEWS ANDI DAL TUO DENTISTA"; pulsante "Impronta Digitale Intraorale" (porta a `dossiersalute.com/arcata-dentale-i-vantaggi-dellimpronta-digitale/`, 404). Il resto è dentro le immagini (vedi sotto).

### Contatti
53. "Centro Dentale Vanuzzo s.a.s. di Vanuzzo Nicola & C. / Direttore Sanitario Dr.ssa Vanuzzo Silvia / Via Vigonovese 137 / 35127 / Padova / PI 03717000289 / Tel: +39 049 760636 / Fax: +39 049 760636"
54. "Camposampiero: / Studio Dentistico Associato / Grego dr Andrea, Vanuzzo dr.ssa Silvia, Vanuzzo dr Nicola / Via Rialto 15/2 / 35012 / Camposampiero PD / PI 04200880286 / Tel: +390495792133 / Fax: +390495792133"
55. Modulo: "Nome / Ditta / Email* / telefono / Messaggio*", "Per favore, inserisci il codice:", "Si applica la nostra Dichiarazione sulla privacy.", "Nota: I campi con l'asterisco sono richiesti".

### Informazioni legali e piede
56. `/about/`: H2 "Questo è un sito creato con Jimdo Creator!" / "Jimdo Creator è il modo più facile, veloce e conveniente di creare il tuo sito web professionale. Richiedi subito il tuo sito gratis: scegli il nome del sito e inserisci il tuo indirizzo email al sito it.jimdo.com."
57. Piede di ogni pagina: "Informazioni legali | Privacy | Informativa sui cookie | Sitemap | Garanzia legale | Recedere dal contratto" e "Accesso". Nessun nome, indirizzo, P.IVA o anno.
58. Banner cookie (Jimdo): "Informativa sui cookie" con i pulsanti "Accetto tutti i cookie", "Accetto solo i cookie selezionati", "Rifiuto tutti i cookie".

### Testi chiusi nelle immagini (trascritti)
- Testata (958x121): "Centro Dentale Vanuzzo" / "... il TUO studio Odontoiatrico!"
- Newsletter ANDI (413x584, 25/05/2018): intestazione "Dott. Nicola Vanuzzo via Vigonovese 137 35127 Padova", testata "Il tuo dentista informa", articoli "Sostieni la Fondazione ANDI onlus", "Abituarsi sin da giovani a prendersi cura di denti e gengive per evitare problemi e costi futuri", "Il tuo dentista consiglia", "Lo sapevi che", "Neymar si prepara ai mondiali", piede "Il network che conta 25.000 Dentisti Italiani / NETWORK ANDI". Testo dell'ANDI, non dello studio.
- Volantino Mutua Certa (706x563): "certa! LA SALUTE SOPRA TUTTO", "CERTA È IL SERVIZIO DI SANITÀ INTEGRATIVA RISERVATO A TUTTI GLI ASSOCIATI ALL'UNIONE PROVINCIALE ARTIGIANI DI PADOVA IN COLLABORAZIONE CON MUTUA ARTIERI", "UNIONE PROVINCIALE ARTIGIANI PADOVA Confartigianato", "www.upa.padova.it".
- Banner Cadiprof (1028x196): "CADIPROF", "Cassa di Assistenza Sanitaria Integrativa per i Lavoratori degli Studi Professionali".
- Immagine Convenzioni (457x318): "Convenzioni".
- Tecnologia, immagine dello scanner (336x150): "The Future in Motion" (pubblicità del produttore).
- Collage Ambienti: orso con fumetto "divertiamoci lavando i denti" e marchio "GUM".
- Logo (937x575): "Centro Dentale Vanuzzo" sopra il disegno di una villa a due piani con balcone e siepe.

### Refusi e cose da non riportare
- Refusi: "Come un squadra", "perchè", "D'AVAGUARDIA", "sciente italian society", "endodonzia , ortodonzia", "Iplantologia", "Imediato" (titolo), "TECNIQUE", "IMPLANTOLGY", "ODONTOLIGURIA", "odontostomatolgia", "Groop for Implant Reserch", "MEMORIL BIAGGI", "ITALIAN EDITINO", "PER I D L'IGIENISTA", "PARODONTALE TE COMPROMESSO", "iservizi dellostudio,dalle", "pulpiti,lesioni", "chirurgia paradontale", "un ottima soluzione", "tuttuno", "ogni 6mesi", "courette" (curette), "the" (tè), "trtattati", ""Speciali"come", "a disposizioni", "scanner intraorale?.", "Cone Bean" (cone beam), "confort", "semplifiazioni", "la formule", "pià".
- Il fax ha lo stesso numero del telefono in entrambe le sedi: nel nuovo sito si scrive una volta sola, [DA CONFERMARE] se il fax esiste ancora.
- "Professore a C." e "segretario Nazionale del GIR" sono incarichi scritti anni fa: [DA CONFERMARE] se sono ancora in corso prima di ripeterli.
- "Visita gratuita" (description della home) e "visita senza impegno" (Prezzi): [DA CONFERMARE] se valgono ancora.
- "I nostri prezzi non sono aumentati di un euro negli ultimi 5 anni": affermazione senza data, non si riprende.
- Toni da non ripetere: "Un sorriso da STAR", "Super-Assistenti", "Centro di [PV] in implantologia", la citazione attribuita a Chaplin, "Formidabile con i bambini", "come solo una mamma sa fare". Per la comunicazione di uno studio sanitario è più sicuro restare sui fatti: il nuovo sito fa così.

## Cosa fanno (servizi, tecnologia, persone, convenzioni)

Studio odontoiatrico privato (ATECO 86.23) su Via Vigonovese, a sud-est del centro di Padova; il logo è il disegno di una casa a due piani con balcone, probabilmente la sede [Probabile, DA CONFERMARE]. Due odontoiatri (Silvia e Nicola Vanuzzo), un'igienista, tre assistenti, più un secondo studio associato a Camposampiero con il Dott. Andrea Grego. [Certo dal sito]

Servizi dichiarati sul sito:
- **Conservativa**, **Endodonzia** (anche perni in fibra), **Ortodonzia** (fissa e mobile, cefalometria; "Ortodonzia Invisibile" nell'elenco Estetica): Dott.ssa Silvia Vanuzzo.
- **Chirurgia orale e parodontale** (estrazioni, chirurgia preprotesica e preimplantare, innesti d'osso, gengivoplastica), **Implantologia** (impianti in titanio, dal dente singolo alla protesi totale; il titolo della pagina del Dott. Nicola parla di implantologia guidata e carico immediato), **Protesi** (capsule, ponti, protesi estese): Dott. Nicola Vanuzzo.
- **Estetica**: sbiancamento, ricostruzioni estetiche, faccette, filler periorali, corone integralmente in ceramica (metal free), ortodonzia invisibile, smile design digitale.
- **Igiene e motivazione**: igiene professionale almeno ogni 6 mesi, ultrasuoni e curette, bicarbonato ad alta pressione per le macchie, **richiamo periodico** su richiesta: igienista Loretta Romanato.
- **Gnatologia e riabilitazione miofunzionale**: ortotici in resina, molaggio selettivo, onlays.
- **Speciale bambini**: pedodonzia, ortodonzia intercettiva, ambienti dedicati; la Dott.ssa Silvia Vanuzzo tiene incontri di prevenzione in asili, scuole e farmacie.

Tecnologia dichiarata: scanner intraorale per l'impronta digitale (20 fotogrammi al secondo, CAD CAM), radiologia tridimensionale cone beam, laser (chirurgia, desensibilizzazione, tasche parodontali, gengivoplastica, frenulectomia, herpes labialis), microscopio operatorio fino a 20 ingrandimenti, usato "di routine". Marche e modelli non dichiarati [DA CONFERMARE]. [Certo per quanto dichiarato]

Persone e titoli (dal sito, [DA CONFERMARE] se aggiornati):
- Dott.ssa Silvia Vanuzzo: odontoiatra e Direttore Sanitario, laureata a Padova nel 2001, socia ANDI e POIESIS. Intervistata da Telenuovo (video sul canale YouTube dello studio, 20/02/2019).
- Dott. Nicola Vanuzzo: odontoiatra, laureato con lode a Padova nel 2003, Master di II livello in Odontologia Forense (Firenze, 2012), perfezionamento in Microscopia operativa (Genova, 2013) e in Laser (2014), tutor al master "Laser e Nuove Tecnologie" di Genova 2015-2017, socio attivo AIOM e GIR. Autore del caso clinico "Prosthetic rehabilitation with short GTB implants: A case report with nine-year follow-up" su Dental Tribune (1/06/2022; pubblicato su "implants" vol. 23, n. 1/2022). [Certo, fonte pubblica]
- Loretta Romanato: igienista dentale, laurea a Bologna nel 2003, laurea specialistica a Firenze nel 2008.
- Assistenti: Fabiola, Monica e Patrizia.
- Studio di Camposampiero: Dott. Andrea Grego con i due Vanuzzo.

Convenzioni: Mutua Certa (sanità integrativa dell'Unione Provinciale Artigiani di Padova, Confartigianato, con Mutua Artieri); Cadiprof (cassa sanitaria dei dipendenti degli studi professionali), presentata come "Convenzione Cadiprof/ANDI". [DA CONFERMARE] se ancora attive e se ce ne sono altre.

Recensioni pubbliche (Google, 13/10/2026): 4,8 su 4 recensioni. Frasi di pazienti: "La mia famiglia ed io frequentiamo questo centro ormai da 20 anni", "Struttura molto pulita, luminosa e facilmente raggiungibile, con parcheggio interno". Sono di terzi: utili per capire lo studio, da non pubblicare senza permesso; il parcheggio interno è [DA CONFERMARE].

Certificazioni: nessuna dichiarata.

## Immagini usate oggi

Tutte le immagini del sito sono state scaricate all'originale caricato su Jimdo (`transf/none`, la risoluzione massima che Jimdo conserva) con `_prova/script/immagini.py`: 71 immagini in `assets/originali/` con `manifest.json` (URL, pagina, testo alternativo, misura mostrata, data di caricamento ricavata dal numero di versione Jimdo). Inventario completo con soggetto, qualità, larghezza massima e uso in `_prova/inventario-immagini.json` (77 voci, comprese le 6 esterne).

| Tipo | Quantità | Misura | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Foto vere dello studio, servizio del 2013 (Fotogallery) | 12 (+ logo e una schermata clinica) | 1820x1208 (una verticale 850x1280) | nitide a 100%, luce morbida, colori un po' caldi; una (operatore con occhiali ingranditori) ha grana e dominante verde. Soggetti: Dott. Nicola Vanuzzo al microscopio, Dott.ssa Silvia Vanuzzo con un bambino, le tre assistenti, operatore al lavoro, pupazzetti sul riunito, manipoli, pannello comandi, diplomi con rose, lampadario, farfalla d'arredo, ortensie | base del nuovo sito: aperture a mezza pagina o colonna larga fino a 1820 px a schermo normale (910 px su retina). Il bambino è riconoscibile: serve la liberatoria [DA CONFERMARE] |
| Le stesse persone in bianco e nero nelle pagine team | 5 | 1000-1279 px, collage | il ritratto della Dott.ssa Silvia Vanuzzo (1154x1023, 2018) è l'unico frontale di lei; gli altri sono versioni desaturate o collage delle foto a colori | ritratto di Silvia fino a circa 1150 px; per gli altri usare gli originali a colori; l'igienista ha solo un ritratto di circa 310 px dentro un collage |
| Foto vera dell'impronta digitale (Questo mese) | 1 | 472x315 | piccola, paziente riconoscibile | solo miniatura, liberatoria [DA CONFERMARE] |
| Immagini di repertorio nelle pagine servizi, filosofia, team, prezzi, bambini (+ una schermata di analisi in Gnatologia) | 13 + 1 | 625-1280 px | sorrisi, apparecchi, rendering 3D, spazzolino, euro dorato, bambine sul prato: generiche, in gran parte da banche immagini | non usare |
| Collage di volti famosi (home ed Estetica) | 2 | 1024x768 | attori e attrici riconoscibili, senza diritti | **non usare** |
| Immagini dei produttori in Tecnologia | 4 | 277-640 px | piccole, una con slogan pubblicitario | non usare; il microscopio (640 px) solo se è quello dello studio [DA CONFERMARE] |
| Testi in immagine (convenzioni, newsletter ANDI, testata) | 5 | 413-1028 px | materiale di terzi o grafica del template | non usare; i contenuti vanno scritti in HTML |
| Slideshow di sfondo | 22 | 1280x720 | fondo bianco con piccole bocche di repertorio negli angoli | non usare |
| Logo | 3 versioni (937x575 nel sito, 761x761 su Facebook, 937x527 su Google) + pittogramma del dente 501x475 + favicon 32x32 | raster | bordi morbidi, nessun vettoriale pubblico | riferimento; chiedere il vettoriale [DA CONFERMARE] |

Come le mostra il sito oggi: Jimdo serve ogni immagine alla misura della colonna (fino a 520 px), quindi a schermo normale **nessuna immagine è ingrandita** (rapporto mostrata/naturale sempre 1,00 o meno). Su schermo retina 18 immagini sono sotto la risoluzione necessaria (originale meno del doppio della misura mostrata), tra cui le tre immagini di Tecnologia (277-336 px), la newsletter ANDI e la foto dell'impronta (413 e 472 px), il pittogramma di Cosa Facciamo. Le 12 foto belle sono mostrate solo in uno slider a 481x319 px (il 26% della loro larghezza) nella pagina Fotogallery, che però le scarica tutte all'originale: 6,5 MB di immagini per vedere foto da 481 px. [Certo]

Riepilogo: **12 foto vere utilizzabili a 1820 px** (più 3 a 2048 px da Google) e **1 ritratto a 1154 px**: abbastanza per un sito vero, non per aperture a tutta larghezza su schermi grandi (a 1440 px una foto da 1820 regge a schermo normale, non su retina). Mancano: l'esterno della sede, la sala d'attesa, le sale operative intere, ritratti recenti e coerenti di tutto lo staff, il Dott. Andrea Grego, la sede di Camposampiero. [Certo]

Foto fuori dal sito (`assets/esterne/manifest.json`):
- Profilo Google "Centro Dentale Vanuzzo": 9 foto dichiarate, 4 esposte nei dati pubblici, tutte del proprietario. Tre sono del servizio del 2013 (Nikon D90, scatti del 13/03 e 22/04/2013) a **2048 px**: calle davanti ai diplomi (verticale, soggetto che sul sito non c'è), manipoli in verticale, pannello comandi (versione più grande della foto del sito). La quarta è il logo (2020). La macchina scattava a 4288x2848: gli originali del servizio sono la prima cosa da chiedere.
- Facebook `facebook.com/Centrodentalevanuzzo.it`: 565 follower, immagine del profilo = logo (761x761); post e copertina non visibili senza accesso.
- YouTube: canale "Centro Dentale Vanuzzo" (@centrodentalevanuzzo4958) con un solo video, "CENTRO DENTALE VANUZZO" (servizio Telenuovo, 20/02/2019, 222 visualizzazioni), incorporato nella home e in Gallery. Anteprima 480x360: utile come rimando al video, non come foto.
- Instagram: nessun profilo collegato dal sito; ricerca per nome non verificabile (richiede l'accesso).
- Dental Tribune: foto cliniche del caso del Dott. Nicola Vanuzzo, non adatte a un sito per pazienti, non scaricate.
- Wayback Machine: bloccata da questa rete il 12 e il 13/10/2026 (connessione chiusa e "Blocked by egress policy"). Poiché Jimdo conserva gli originali caricati, è improbabile trovare in archivio foto più grandi; resta da provare per vedere eventuali versioni del sito precedenti al 2017.

Foto da chiedere o da fare (per il LEGGIMI): gli originali del servizio del 2013; l'esterno della sede di Via Vigonovese con l'ingresso; la sala d'attesa; una sala operativa intera con il microscopio e lo scanner; ritratti aggiornati, con la stessa luce, dei due odontoiatri, dell'igienista, delle assistenti e del Dott. Grego; la sede di Camposampiero; il logo in vettoriale; le liberatorie per il bambino e la paziente già fotografati.

## Problemi tecnici da segnalare al cliente

Misure del 12-13/10/2026 con Playwright (Chromium) e curl attraverso un proxy: i tempi sono indicativi.

1. **Telefono**: nessuna delle 32 pagine ha il meta viewport (`grep` su tutto il crawl: 0; Playwright: `viewport` nullo). A 390 px, emulando un iPhone, la pagina resta larga 984 px (`scrollWidth` 984; 1077 sulla pagina del Dott. Nicola Vanuzzo, dove l'indirizzo dell'articolo di Dental Tribune, scritto per intero con il parametro `fbclid` di Facebook, esce dalla colonna) ed è rimpicciolita al 39,6%: il testo mediano da 15 px si vede a **5,9 px**, i titoletti da 13,5 px a 5,4 px, i paragrafi che il telefono ingrandisce da sé (22 px) a 8,8 px; il menu a sinistra (15 px) si vede a 5,9 px, i link del piede sono ancora più piccoli; i numeri di telefono sono link `tel:` ma, rimpiccioliti, vanno ingranditi prima di poterli toccare. Prova: `_prova/attuale/01-home-390-schermo.png`, `05-dott-nicola-vanuzzo-390-schermo.png`, `28-prezzi-390-schermo.png`, `30-contatti-390-schermo.png` (primo schermo del telefono) e `NN-*-390.png` (pagina intera come sul telefono). [Certo]
2. **Dati societari e "Informazioni legali"**: la pagina `/about/` contiene solo il testo predefinito "Questo è un sito creato con Jimdo Creator!" con il logo Jimdo (`31-informazioni-legali-1440.png`). La P.IVA 03717000289 compare solo in Contatti; non c'è in home né nel piede (l'art. 35 del DPR 633/1972 la chiede nella home del sito). Mancano anche sede legale, REA PD-331651 e PEC. [Certo]
3. **Privacy**: la "Dichiarazione sulla privacy" (`/j/privacy`) è il testo generico di Jimdo su reCAPTCHA e statistiche: non nomina il titolare del trattamento, non dà contatti, non parla del modulo di Contatti, che raccoglie nome, email, telefono e un messaggio libero dove un paziente può scrivere dati sulla sua salute. Il banner cookie di Jimdo c'è e funziona (anche "Rifiuto tutti i cookie"), e mappa e video restano bloccati finché non si accetta: questa parte va bene. [Certo]
4. **Diritti d'immagine**: l'apertura della home e la pagina Estetica usano un collage di volti di attori e attrici famosi (`home.jpg`, `estetica.jpg`, caricati il 3/02/2014). Le altre immagini delle pagine servizi sono di repertorio senza indicazione di licenza. [Certo per l'uso, Probabile per l'assenza di licenza]
5. **Contenuti fermi**: ultima data visibile il 25/05/2018 (newsletter ANDI in "Questo mese..."); curricula fermi al 2013, 2015 e 2017; pagina Prezzi senza prezzi; pagina Convenzioni con sole immagini; nessun orario sul sito (Google li ha). Template del 20/07/2017. Nel piede nessun anno di copyright. [Certo]
6. **Link rotti**: sulla pagina del Dott. Nicola Vanuzzo `aiom-micro.it` e `girassociation.it` non esistono più (DNS: NXDOMAIN), `sympla-gtb.it` (scritto come testo) neppure, la scheda su `dossiersalute.com` dà 404; il pulsante "Impronta Digitale Intraorale" di "Questo mese..." porta a una pagina 404 di dossiersalute.com; il volantino Mutua Certa porta a un PDF che non esiste più (404 dopo il rinvio a confartigianatopadova.it); il link Cadiprof (`www2.cadiprof.it`) apre con un certificato non valido per quel nome. Nessun link interno rotto (35 URL su 35 rispondono 200). Dettaglio in `_prova/crawl/link.json`. [Certo]
7. **Peso e richieste** (rete di Playwright, primo caricamento, 3 giri): home 48 richieste e **2,2 MB**, di cui 1,9 MB di immagini (le 22 immagini della slideshow di sfondo, quasi bianche, si scaricano tutte all'apertura); Fotogallery 74 richieste e **6,8 MB** (14 foto all'originale per mostrarle a 481 px); Contatti 30 richieste e 1,1 MB (il segnaposto della mappa è un PNG di 733 KB); le altre pagine circa 25 richieste e 0,4 MB. Tempi: primo byte 0,3-0,8 s, evento load della home 1,7-2,2 s, della Fotogallery 2,5-7,0 s. Lo script statistico Jimdo (`at.prod.jimdo.systems`) viene interrotto a ogni pagina. [Certo, tempi indicativi]
8. **Errori in console**: nessuno su 33 pagine, né a 1440 né a 390. [Certo]
9. **HTTPS**: funziona. Certificato Google Trust Services WE1 per `centrodentalevanuzzo.it` e `*.centrodentalevanuzzo.it`, valido dal 21/08/2026 al 19/11/2026 (rinnovo automatico di Jimdo, certificati registrati dal 2016). http e dominio senza www vanno su `https://www.` con un 301; HSTS attivo (7 giorni). Server Cloudflare davanti a Jimdo. [Certo]
10. **CMS e dominio**: Jimdo Creator (`meta generator`, intestazione `x-jimdo-wid: s4ea61a7637d33cd5`), pacchetto a pagamento (`isFreePackage: false`), layout "classico" a 984 px con trucchi per Internet Explorer 6 nel CSS. DNS gestiti da Jimdo (NS1, `hostmaster.jimdo.com`) e **posta del dominio su Jimdo** (`mx1.jimdo.com`, `mx2.jimdo.com`): prima di spostare il dominio va verificato se lo studio usa caselle `@centrodentalevanuzzo.it` [DA CONFERMARE]. [Certo]
11. **Immagini**: a schermo normale nessuna è ingrandita; su retina 18 sono sotto risoluzione (vedi sopra). La newsletter ANDI a 413 px non si legge nemmeno da computer. [Certo]
12. **Testi chiusi in immagini**: la testata con nome e slogan, le due convenzioni (volantino Mutua Certa, banner Cadiprof), la scritta "Convenzioni", la newsletter ANDI, lo slogan del produttore in Tecnologia: invisibili ai motori di ricerca e illeggibili da telefono. [Certo]
13. **SEO**: 25 pagine su 32 senza meta description; in ogni pagina due H1 uguali nella colonna destra ("Il Dentista...", "proprio come lo vorresti!") e 20 pagine senza un H1 proprio; tre pagine con lo stesso titolo "Speciale Bambini"; un refuso nel titolo del Dott. Nicola Vanuzzo ("Carico Imediato"); nessuna delle 14 immagini della Fotogallery ha un testo alternativo; il link "PRENOTA UNA VISITA!" è spezzato nel codice in "PRENOTA UNA VISI" + "TA!". [Certo]
14. **Pagine fuori luogo**: nel piede "Garanzia legale" e "Recedere dal contratto" (pagine Jimdo da negozio online, con modulo di recesso "Numero d'ordine o di prenotazione") e "Accesso" (login dell'editor). [Certo]
15. **Contatti**: nessuna email pubblicata, solo il modulo; il fax ha lo stesso numero del telefono; i numeri sono link `tel:` ma minuscoli da telefono; due mappe Google vuote finché non si accettano i cookie, senza indirizzo cliccabile per il navigatore. [Certo]
16. **Pubblicità sanitaria**: in Contatti c'è il Direttore Sanitario (Dr.ssa Vanuzzo Silvia); non compaiono gli estremi dell'autorizzazione sanitaria della struttura. Da verificare con il cliente cosa va indicato [DA CONFERMARE]; slogan come "Un sorriso da STAR" e "Centro di [PV] in implantologia" non sono adatti. [Ipotesi da verificare]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | CENTRO DENTALE VANUZZO S.A.S. DI VANUZZO NICOLA & C. | VIES (valida il 12/10/2026), aziende.it (Registro Imprese), sito |
| Forma giuridica | società in accomandita semplice | aziende.it |
| P.IVA e codice fiscale | 03717000289 | VIES, aziende.it, sito (Contatti) |
| REA | PD-331651, CCIAA di Padova, iscrizione 01/10/2002 | aziende.it |
| Sede legale e operativa | Via Vigonovese 137, 35127 Padova (PD) | VIES, aziende.it, sito, Google |
| Attività | ATECO 86.23, attività degli studi odontoiatrici | aziende.it |
| Dipendenti | 4 (2022), fascia 0-9 | aziende.it (aggiornato al 5/07/2026) |
| Fatturato | non pubblico (società di persone) | aziende.it |
| Codice destinatario SDI | A4707H7 | aziende.it |
| Direttore Sanitario | Dott.ssa Silvia Vanuzzo | sito (Contatti) |
| Telefono | +39 049 760636 (anche fax) | sito, Google |
| Email | non pubblicata (solo modulo); il dominio ha la posta su Jimdo | sito, DNS |
| PEC | **non trovata**: aziende.it la vende a pagamento, INI-PEC chiede un codice di verifica non automatizzabile. Cercare a mano su www.inipec.gov.it con P.IVA 03717000289 | [DA CONFERMARE] |
| Orari | sul sito nessuno. Google: lun 9-13 e 14-20, mar 9-12 e 15-20, mer 9-13, gio 9-13 e 14-20, ven 9-15, sab e dom chiuso | Google Maps, 12/10/2026; [DA CONFERMARE] |
| Anni di attività | società iscritta il 01/10/2002; la Dott.ssa Silvia Vanuzzo esercita "Dal 2001", il Dott. Nicola Vanuzzo "Dal 2003"; una recensione Google parla di una famiglia in cura "da 20 anni" | aziende.it, sito, Google; [DA CONFERMARE] l'anno da comunicare |
| Secondo studio | Studio Dentistico Associato Grego dr Andrea, Vanuzzo dr.ssa Silvia, Vanuzzo dr Nicola, Via Rialto 15/2, 35012 Camposampiero (PD), P.IVA 04200880286 (valida in VIES), tel. +39 049 5792133 (anche fax); scheda Google "Studio Dentistico Associato Grego Dr A..." | sito, VIES, Google Maps |
| Scheda Google | "Centro Dentale Vanuzzo", categoria Dentista, 4,8 su 4 recensioni, place_id ChIJWZYlmzLFfkcRYII1pSQO7xw, segnalato l'ingresso accessibile in sedia a rotelle | Google Maps, 12/10/2026 |
| Social | facebook.com/Centrodentalevanuzzo.it (565 follower); YouTube @centrodentalevanuzzo4958 (1 video, 2019); Instagram non trovato | Facebook, YouTube |
| Dominio | centrodentalevanuzzo.it su Jimdo (DNS NS1/Jimdo, MX Jimdo, Cloudflare); certificati HTTPS registrati dal 2016 | dns.google, crt.sh |
| Associazioni (dal sito) | ANDI e POIESIS (Dott.ssa Silvia Vanuzzo); AIOM e GIR (Dott. Nicola Vanuzzo) | sito; [DA CONFERMARE] se attuali |
| Convenzioni (dal sito) | Mutua Certa (UPA Padova, Confartigianato), Cadiprof | sito; [DA CONFERMARE] |
| Certificazioni | nessuna dichiarata | sito |

Da confermare con il cliente (va nel LEGGIMI): PEC; email da pubblicare; orari di Padova e di Camposampiero; se il fax esiste ancora; staff attuale (assistenti, igienista, Dott. Grego) e incarichi universitari e associativi ancora in corso; convenzioni attive; se la prima visita è gratuita; marche e modelli di scanner, cone beam, laser e microscopio; estremi dell'autorizzazione sanitaria; parcheggio interno e accessibilità; gli originali del servizio fotografico del 2013 e le liberatorie; il logo vettoriale; se il dominio ha caselle email attive su Jimdo.

## URL vecchi

Servono per `plugin/redirect-301.csv`. Tutti rispondono 200 (13/10/2026). Le destinazioni sono indicative: dipendono dalla mappa del nuovo sito (03).

| URL vecchio | Contenuto | Destinazione probabile |
|---|---|---|
| `/` | home | home |
| `/filosofia/` | filosofia di lavoro | studio (chi siamo) |
| `/il-team/` | team | team |
| `/il-team/dott-ssa-silvia-vanuzzo/` | Dott.ssa Silvia Vanuzzo | team, scheda Silvia Vanuzzo |
| `/il-team/dott-nicola-vanuzzo/` | Dott. Nicola Vanuzzo | team, scheda Nicola Vanuzzo |
| `/il-team/igienista-romanato-loretta/` | igienista | team |
| `/il-team/le-nostre-assistenti/` | assistenti | team |
| `/cosa-facciamo/` | elenco servizi | cure |
| `/cosa-facciamo/conservativa/`, `/endodonzia/`, `/chirurgia-e-parodontologia/`, `/implantologia/`, `/ortodonzia/`, `/protesi/`, `/estetica/`, `/igiene-e-motivazione/`, `/gnatologia/` | 9 servizi | cure (o la singola cura se avrà una pagina) |
| `/speciale-bambini/` e le 3 sottopagine | bambini | bambini |
| `/tecnologia/` | tecnologia | tecnologia (o studio) |
| `/gallery/`, `/gallery/fotogallery/` | video e foto | studio |
| `/convenzioni/` e le 2 sottopagine | convenzioni | contatti o pagina convenzioni |
| `/prezzi/` | testo sui prezzi | prima visita / contatti |
| `/questo-mese/` | newsletter 2018 | home |
| `/contatti/` | contatti | contatti |
| `/about/` | informazioni legali (vuota) | note legali |
| `/sitemap/` | sitemap | home |
| `/j/privacy` | privacy | privacy |
| `/j/legal-guarantee`, `/j/withdrawal` | pagine da negozio Jimdo | home |

Elenco completo (anche in `_prova/crawl/url-vecchi.txt`; host canonico `https://www.centrodentalevanuzzo.it`, già 301 da http e dal dominio senza www):

```
/
/filosofia/
/il-team/
/il-team/dott-ssa-silvia-vanuzzo/
/il-team/dott-nicola-vanuzzo/
/il-team/igienista-romanato-loretta/
/il-team/le-nostre-assistenti/
/cosa-facciamo/
/cosa-facciamo/conservativa/
/cosa-facciamo/endodonzia/
/cosa-facciamo/chirurgia-e-parodontologia/
/cosa-facciamo/implantologia/
/cosa-facciamo/ortodonzia/
/cosa-facciamo/protesi/
/cosa-facciamo/estetica/
/cosa-facciamo/igiene-e-motivazione/
/cosa-facciamo/gnatologia/
/speciale-bambini/
/speciale-bambini/ambienti/
/speciale-bambini/ortodonzia-intercettiva/
/speciale-bambini/attenzioni-particolari/
/tecnologia/
/gallery/
/gallery/fotogallery/
/convenzioni/
/convenzioni/convenzione-mutua-certa/
/convenzioni/convenzione-cadiprof-andi/
/prezzi/
/questo-mese/
/contatti/
/about/
/sitemap/
/j/privacy
/j/legal-guarantee
/j/withdrawal
```

Le pagine di sistema Jimdo `/app/...` e `/j/...` sono escluse da `robots.txt`; `/index.html`, `/privacy/`, `/news/` danno già 404 e non vanno redirette.

## Cosa manca e cosa chiedere

- Foto: esterno, sala d'attesa, sale operative intere, ritratti aggiornati e coerenti dello staff, sede di Camposampiero; originali del servizio del 2013; liberatorie.
- Dati: PEC, email, orari delle due sedi, staff attuale, convenzioni attive, prima visita gratuita o no, autorizzazione sanitaria.
- Logo vettoriale (oggi solo JPG/PNG raster).
- Testi da aggiornare con i medici: curricula dopo il 2017, eventuali nuove tecnologie, la pagina prezzi (cosa si può dire: prima visita, preventivo, pagamenti rateali se esistono).

## Fonti e file di lavoro

- Sito: `https://www.centrodentalevanuzzo.it/sitemap.xml` (31 URL) e link interni; crawl con `_prova/script/crawl.py`, testi con `estrai.py`, immagini con `immagini.py`, link con `link.py`.
- Misure: `_prova/script/misura2.cjs` (screenshot e misure a 1440 e 390), `rete.cjs` (peso e tempi al primo caricamento), `telefono.cjs` (pagina intera come sul telefono), `sborda.cjs`.
- Registri: VIES (`_prova/crawl/esterne/vies-*.json`), aziende.it (`aziende-it-scheda.html`); ufficiocamerale.it, registroaziende.it, reportaziende.it bloccano l'accesso automatico.
- Google Maps: `_prova/crawl/esterne/gplace*.{json,txt,png}` e `g2/`; Facebook (plugin pubblico della pagina), YouTube (oEmbed e pagina del video), Dental Tribune (`dental-tribune.html`), crt.sh, dns.google.
