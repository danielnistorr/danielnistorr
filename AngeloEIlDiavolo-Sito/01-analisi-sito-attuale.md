# 01. Analisi del sito attuale (www.angeloeildiavolo.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).

## In breve

- Osteria, pizzeria ed enoteca in Piazza Castello 41/A a Marostica, sotto i portici della Piazza degli Scacchi. Titolare Roberto "Apo" Ambrosi, oste e cantautore; impresa individuale iscritta dal 16/04/1991. Cucina romana e veneta, porcetto al forno a legna, pizza. [Certo]
- Sito statico di 4 pagine più la pagina del contributo FESR, scritto a mano in HTML su server IIS. Da computer regge (foto a tutta pagina); da telefono no: **manca il meta viewport**, la pagina è larga 988 px e il telefono la rimpicciolisce al 39%, così menu, numero per prenotare e P.IVA si leggono a **circa 5,5 px**. Il sito **non risponde in https** e per il dominio non è mai stato emesso un certificato. [Certo]
- Contenuti fermi al 2012-2013: foto del 10/11/2012 (Foto Bittante), jQuery del 2013, facciata vecchia nella gallery mentre quella vera è stata rifatta; in tutto **303 parole** nelle 4 pagine principali. Orari diversi tra sito, Google e portale del Comune. [Certo]
- Identità già forte e nuova, ma assente dal sito: **stemma con ali d'angelo e tridente del diavolo**, rosso vino **#A02B46** su nero **#070E14**, scritta "L'Angelo e il Diavolo / l'osteria di APO / Marostica - Piazza degli Scacchi"; la stessa grafica è sulla facciata (in oro), sul menu e sulla tovaglietta. Il sito usa ancora il bordeaux #800920 e il font Josefin Sans. [Certo]
- Materiale fotografico: 4 sfondi a 2000 px (3 di Foto Bittante, 2012), 32 foto di gallery a 800 px (19 professionali del 2012, 10 da smartphone, 2 illustrazioni, 1 ingresso), 3 ritratti piccoli, più 5 immagini recenti e grandi pubblicate dall'azienda fuori dal sito (logo attuale, facciata 4032 px, sala 2023, funghi in piazza, tagliolini ai finferli). [Certo]

## Pagine esistenti

| Pagina | URL | Contenuto | Ultima modifica (header) |
|---|---|---|---|
| Home | `/` e `/index.htm` | poesia "Vieni con me stasera andiamo..." su foto di Apo al banco, rimando a "Voci dal Cuore", striscia loghi FESR a 150x31 px | 03/07/2026 (aggiunta del banner FESR) |
| L'Angelo e il Diavolo | `/l-angelo-e-il-diavolo.htm` | frase sul locale, tre schede: Roberto APO Ambrosi, Bruna Quintano, Lorenzo Ambrosi; gallery di 9 foto | 07/06/2024 |
| Ristorante | `/ristorante.htm` | frase sulla cucina, schede Porcetto e Specialità romane; gallery di 23 foto | 07/06/2024 |
| Contatti | `/contatti.htm` | indirizzo, telefono, orari, email, link Tripadvisor e Facebook, mappa Google incorporata | 07/06/2024 |
| Progetto FESR | `/Bando_pr_veneto.htm` | pubblicità obbligatoria del contributo PR Veneto FESR 2021-2027: titolo, importi, descrizione, foto della cucina | 03/07/2026 |

Fogli e script: `css/main.css` (modificato il 03/07/2026), `jquery/jquery-1.9.0.min.js`, `jquery/jquery.mousewheel-3.0.6.pack.js`, `js/jquery.fancybox.js?v=2.1.4` con gli helper buttons, thumbs e media. Nessuna sitemap, nessun robots.txt, nessuna favicon (tutti 404). Cartelle `/images/`, `/js/`, `/css/` chiuse (403). Prove: `_prova/crawl/*.htm`, `*.h` (intestazioni HTTP).

## Testi reali (verbatim, con i refusi originali)

Home:
1. Titolo: "Benvenuti"
2. Poesia: "“Vieni con me stasera andiamo / disse il diavolo all’Angelo restio / e tenendolo ben saldo per la mano / lo sottrasse al regno del suo Dio. / È fu così che l’Angelo di cui si ignora il sesso / col diavolo in un angolo parlò di compromesso. / Dio cerca di scovare quell’Angelo perduto, / ma tu lo puoi lo puoi trovare col diavolo seduto / tra vino e cibi vari, tra musica e poesia / In PIAZZA degli SCACCHI / dove ha aperto un’osteria!”"
3. Riquadro: "Entra nel progetto musicale realizzato per l'associazione "30 Nodi per il fegato"."

Testata e piede (tutte le pagine):
4. "Prenota ora il tuo tavolo : 0424.72312"
5. Menu: "HOME / L'ANGELO E IL DIAVOLO / RISTORANTE / CONTATTI"
6. "L’Angelo E Il Diavolo L’Osteria Di Apo Oste In Marostica Di Ambrosi Roberto - P.IVA 02198470243"
7. "Si riposa il lunedì perché il fegato respiri, aperto tutti gli altri dì tra brindisi e sospiri."

L'Angelo e il Diavolo:
8. Titolo: "l'Angelo e il Diavolo"
9. "Un angolo di sorrisi e simpatia. Un luogo dove non si confonde l’ASSAPORARE (gustare) con il masticare. Dove CUCINARE non significa cuocere e dove si mangia per GODERE e non per sopravvivere!"
10. "Roberto APO Ambrosi": "“Un’oste di passaggio, una vita di emozioni, sogni e canzoni tra santi, bugiardi e cialtroni.”"
11. "Bruna Quintano": "“Le idee, la fantasia e la cucina. Il motore dell’Angelo e il Diavolo.“"
12. "Lorenzo Ambrosi": "“Il nuovo che arriva. La simpatia e il futuro dell’Angelo e il Diavolo.“"
13. Pulsante: "Guarda la gallery"

Ristorante:
14. Titolo: "Ristorante"
15. "Proponiamo piatti classici e pietanze speciali, come il porcetto e le specialità romane. Il menù è sempre abbinato a un’apia carta dei vini per accompagnare il piacere dei nostri piatti col piacere del bere sano."
16. "PORCETTO": "Porcetto cotto su forno a legna. Tutte le domeniche o su prenotazione."
17. "Specialità ROMANE": "Bruna, deportata da APO a Marostica, ha deciso di portare un po' di cultura culinaria romana nel Veneto. Cacio e pepe, matriciana, gricia, aglio & olio, carbonara e tante altre specialità."
18. Meta description: "Vieni ad assaggiare il nostro PROCETTO cotto su forno a legna e le nostre specialità romane."

Contatti:
19. "Piazza Castello, 41/A - Marostica (VI) Italia - Tel. 0424.72312 / orari di apertura: 10.00-15.00 18.00-24.00 / Turno di chiusura il lunedì tranne i mesi estivi"
20. "Scrivi la tua recensione su [Tripadvisor]" / "Seguici e prenota il tuo tavolo: [Facebook]" / "Email: robertoapoambrosi@gmail.com"

Progetto FESR (testo ufficiale, da ripubblicare com'è; copia integrale in `_prova/crawl/Bando_pr_veneto.htm`):
21. "Progetto finanziato con il PR Veneto FESR 2021-2027"
22. Titolo del progetto: "Marostica: Verso un Futuro Sostenibile tra Tradizione, Cultura e Innovazione." seguito da un paragrafo sull'aggregazione del Distretto del Commercio di Marostica (transizione ecologica, economia circolare, risparmio energetico).
23. Importi: "Spesa tecnica ammessa complessivamente al distretto € 318.976,27 / Contributo deliberato complessivamente al distretto € 194.185,97 / Spesa tecnica ammessa alla nostra impresa € 28.341,29 / Contributo deliberato alla nostra impresa € 19.989,96"
24. Descrizione del programma: testo del distretto, non dell'osteria, con tre punti ("Memoria Storica", "Ospitalità" e un punto sulle tecnologie). Contiene parole della lista vietata del metodo: non va riusato come testo del sito, solo copiato tale e quale nella pagina obbligatoria del progetto.

Testi chiusi nelle immagini (trascritti):
25. Illustrazione firmata "Don Backy 98" (`locale-01`): striscione "OSTERIA L'ANGELO E IL DIAVOLO"; fumetti "VORRÀ DIRE CHE IL BIANCO LO CHIAMEREMO L'ANGELO..." e "...E IL ROSSO IL DIAVOLO!!!"; sulla lira dell'angelo "APO". È l'origine del nome, oggi leggibile solo dentro una foto da 800 px.
26. Vignetta (`locale-08`, firma che sembra "Jacovitti"): "GOAL!!! e voi!!! OFFRITE LA CENA!!! (naturalmente da APO)", "TUMPT!", "GOAL!".
27. Targa (`locale-03`): "LEGGE FONDAMENTALE DEL CAPO / Art. 1 - Il Capo ha ragione / Art. 2 - Il Capo ha sempre ragione ..." (testo umoristico di serie, non dell'osteria).
28. Vecchia tovaglietta-menu (sfondo della pagina 02, foto del 2012): "Le nostre pizze", Margherita, Romana, Greca... da € 5,20 a € 7,50; "mozzarella di Bufala... Freschissima"; "prenotazione cucina tipica Romana e Sarda"; "euro 8,00"; "www.angeloeildiavolo.com". Prezzi del 2012: non riusabili.
29. Insegne (foto 2012 e facciata attuale): "L'Angelo e il Diavolo" (corsivo), "Enoteca Bar Caffè da Apo" (neon), "PIZZERIA" e "RISTORANTE PIZZERIA" (verticali), "L'osteria di APO" (pannello con lo stemma dorato), espositore "I RISTORANTI DELL'OCA".
30. Etichetta del vino della casa (`piatto-10`): "Il Rosso di Apo", con angelo e diavolo disegnati.

Testi pubblici dell'azienda fuori dal sito:
31. Descrizione del proprietario sulla scheda Google: "Ristorante con carne alla griglia, e con specialità tipiche Venete e Romane!"
32. Scheda sul portale comunale VisitMarostica: "Nella splendida Piazza degli scacchi si affaccia il Ristorante Pizzeria Angelo e Diavolo che ripropone piatti della tradizione romana con influenze venete. 50 coperti all'esterno [...] orario 10.00-15.00/18.00-24.00 Giorno chiusura Chiuso lunedì e martedì a pranzo Numero coperti 45 Specialità Cucina tipica Romana e Veneta, con prodotti stagionali (tartufo di Norcia, tartufo delle Langhe, Radicchio di Treviso, Asparagi di Bassano, piatti a base di Oca)."
33. Logo e menu attuali: "L'Angelo e il Diavolo / l'osteria di APO / Marostica - Piazza degli Scacchi".

Refusi da non riportare: "È fu così" (E fu così), "lo puoi lo puoi" (ripetizione, [DA CONFERMARE] se voluta nella poesia), "Un’oste" (un oste), "un’apia carta" (ampia), "PROCETTO", "cotto su forno" (nel forno), virgolette di chiusura rovesciate (“ al posto di ”), "Prenota ora il tuo tavolo :" con lo spazio prima dei due punti, "l'Angelo" minuscolo nel titolo, maiuscole a caso nel piede ("L’Angelo E Il Diavolo L’Osteria Di Apo Oste..."). Il nome compare come "L'Angelo e il Diavolo", "Angelo e Diavolo", "L'osteria di APO", "da Apo": nel nuovo sito si usa **L'Angelo e il Diavolo** con sottotitolo **l'osteria di APO**, come nel logo attuale.

## Cosa fanno

- **Osteria e ristorante** di cucina romana (cacio e pepe, matriciana, gricia, aglio e olio, carbonara) e veneta, con prodotti di stagione: tartufo di Norcia e delle Langhe, radicchio di Treviso, asparagi di Bassano, piatti a base di oca (fonte: VisitMarostica). [Certo per le fonti]
- **Porcetto cotto nel forno a legna**, "tutte le domeniche o su prenotazione" (sito); la tovaglietta del 2012 parlava di cucina "Romana e Sarda". Oggi è ancora così? [DA CONFERMARE]
- **Carne alla griglia** (descrizione Google del proprietario; foto recenti di tagliate e costolette). [Certo]
- **Pizzeria**: insegna "PIZZERIA" e poi "RISTORANTE PIZZERIA", foto di panetti e pizze (2012), 97 recensioni Google che citano la pizza. [Certo]
- **Enoteca, bar, caffè**: neon "Enoteca Bar Caffè da Apo", carta dei vini, vino della casa "Il Rosso di Apo". Il nome viene da qui: il bianco è l'Angelo, il rosso è il Diavolo (illustrazione di Don Backy, 1998). [Certo]
- **Dehors in piazza**: 50 coperti all'esterno e 45 all'interno secondo il portale del Comune. [DA CONFERMARE]
- **Musica e cause sociali**: Apo ha fondato l'associazione Voci dal Cuore (CD "Voci dal Cuore 3" con Paolo Rossi, Luca Barbarossa, Don Backy, Bruna Quintano e Lorenzo Ambrosi; ricavato alla fondazione "30 Nodi per il fegato"). Il sito dell'associazione è fermo al 2013. [Certo; attualità DA CONFERMARE]
- Storia della famiglia (fonte vocidalcuore.it, pagina "Roberto Apo Ambrosi"): Apo parte per Roma tra il 1974 e il 1976, ci resta sedici anni, sposa Bruna Quintano nel 1986, poi torna a Marostica con lei e il figlio Lorenzo; ha scritto un'autobiografia intitolata "Vita!". [Certo per la fonte]
- Prenotazione: solo telefono (0424 72312) o Facebook. Nessun menu online, nessun prezzo, nessuna prenotazione via web. [Certo]
- Marchi e riconoscimenti: nessuna certificazione dichiarata. L'espositore "I Ristoranti dell'Oca" compare in due foto davanti all'ingresso (2012 e oggi): adesione [DA CONFERMARE]. Sulla vetrina ci sono adesivi verdi tipo Tripadvisor, non leggibili.

## Immagini usate oggi

Inventario completo con soggetto, qualità e larghezza massima: `_prova/inventario-immagini.json`. File in `assets/originali/` (53) e `assets/esterne/` (12, con `manifest.json`).

| Tipo | Quantità | Dimensioni | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Sfondi a tutta pagina (Apo al banco, sala con tovaglietta, tagliatelle, piazza di notte) | 4 | 2000x1325-1333 | buone e nitide al 100%; 3 su 4 con EXIF Pentax K-5, scatto 10/11/2012, copyright FOTO_BITTANTE; la piazza senza autore dichiarato | aperture e fasce fino a 2000 px; a 1440 su retina si ingrandiscono 1,4 volte, meglio fasce non a tutto schermo o chiedere gli originali (la K-5 scatta a 4928 px) |
| Gallery "locale" | 9 | 800 px (una 1000x287) | 6 professionali (2012, due sono doppioni degli sfondi), 2 illustrazioni scansionate, 1 ingresso con facciata vecchia | mezza larghezza fino a 800 px (400 su retina); illustrazioni come documenti della storia |
| Gallery "ristorante" | 23 | 800x530 / 800x600 | 13 professionali (foto 4-16: dolci, vini, pizza, padelle, Bruna ai fornelli); 10 da smartphone con tovaglia a righe blu e luce piatta | le professionali in griglia fino a 800 px; le smartphone solo miniature o da rifare |
| Ritratti Apo, Bruna, Lorenzo | 3 | 448-591 px | buoni ma piccoli; Apo in bianco e nero | ritratti fino a 450-590 px; Bruna e Lorenzo vanno aggiornati se la squadra è cambiata [DA CONFERMARE] |
| Riquadri porcetto e rigatoni | 2 | 215x200 | ritagli inutili | si usano le versioni a 800 px |
| Cucina rinnovata (collage) | 1 | 1024x273 | 5 viste da 205 px affiancate | solo nella pagina FESR; servono foto nuove |
| Loghi FESR, icone social, Voci dal Cuore | 10 | piccoli | grafiche | loghi FESR da prendere vettoriali dal kit della Regione |

Trovate fuori dal sito, pubblicate dall'azienda:

| File | Dimensioni | Fonte | Giudizio |
|---|---|---|---|
| `visitmarostica-logo-attuale.jpg` | 1147x1659 | VisitMarostica, scheda del locale | logo attuale pulito; manca il vettoriale |
| `google-proprietario-facciata.jpg` | 4032x3024 | foto principale della scheda Google, caricata dal proprietario | buona: facciata rinnovata con stemma dorato, insegna e neon; leggermente storta |
| `visitmarostica-sala-tovaglie-quadri.jpg` | 3024x4032 (verticale) | VisitMarostica, iPhone 12, 18/10/2023 | buona: sala attuale, tovaglie a quadri rossi, maglia "TOTTI 10", menu nero con lo stemma |
| `visitmarostica-funghi-in-piazza.jpg` | 3024x4032 (verticale) | VisitMarostica | buona: ovoli e porcini con il Castello Inferiore e il leone di San Marco |
| `visitmarostica-tagliolini-finferli.jpg` | 3024x3780 | VisitMarostica, iPhone 12, pubblicata su Instagram il 31/08/2022 | buona: piatto davanti alla parete dei vini |
| `voci-dal-cuore-logo-storico.jpg` | 324x273 | vocidalcuore.it | vecchio logo (illustrazione di Don Backy + scritta), solo documento |

Le 6 foto `terzi-google-*` (piatti del 2026 dalla scheda Google) sono di autore non identificato, quasi certamente clienti: non vanno pubblicate, servono solo come riferimento per il brief fotografico. Diritti da chiarire col cliente: le foto di Paolo Bittante (licenza d'uso per il nuovo sito e originali ad alta risoluzione), l'illustrazione di Don Backy e la vignetta firmata "Jacovitti". La foto della piazza di notte mostra targhe d'auto leggibili: vanno sfocate.

Cosa manca: foto attuali della sala piena, del dehors in piazza, della cucina rinnovata, del forno a legna, della carta dei vini, della squadra di oggi, dei piatti di stagione con la nuova mise en place (tovaglia a quadri rossi, tovaglietta nera).

## Problemi tecnici da segnalare al cliente

Misure del 6/10/2026 con Chromium (Playwright) a 1440x900 e a 390x844 come iPhone, cache vuota per ogni pagina. File: `_prova/attuale/misure.json` e screenshot `_prova/attuale/NN-pagina-1440.png`, `-390.png`, `-390-schermata.png`.

1. **Telefono: pagina rimpicciolita, testo illeggibile.** Nessun `<meta name="viewport">` in nessuna pagina. A 390 px la pagina è larga 988 px (Home), 980 (02 e 04), 1001 (03), 1085 (FESR); il telefono la riduce al 39% (`visualViewport.scale` 0,395; 0,36 sulla pagina FESR). Il CSS ha regole per 768, 640, 480 e 360 px che non scattano mai; scatta solo quella per 1024 px, che rimpicciolisce ancora il menu a 14 px. Risultato a schermo: menu, "Prenota ora il tuo tavolo : 0424.72312" e piede con la P.IVA a **circa 5,5 px**, poesia a 7,9 px, testo FESR a 6,5 px. Il numero per prenotare non si legge e non è un link `tel:`. Prova: `01-home-390-schermata.png`. [Certo]
2. **Niente https.** `https://www.angeloeildiavolo.com` e `https://angeloeildiavolo.com`: SSL_ERROR_SYSCALL; dal gateway di rete "upstream connect error ... remote connection failure". Nei registri pubblici dei certificati (crt.sh) non c'è nessun certificato per `angeloeildiavolo.com` né `*.angeloeildiavolo.com`. I browser mostrano "Non sicuro". [Certo]
3. **Dominio in scadenza il 01/12/2026** (RDAP Verisign: registrato il 01/12/2008, registrar PDR Ltd / PublicDomainRegistry, DNS Seflow). Il rinnovo non va perso durante il passaggio. [Certo]
4. **Tecnologia ferma al 2013.** Server Microsoft-IIS/10.0 con intestazione X-Powered-By ASP.NET; pagine `.htm` statiche senza CMS; jQuery 1.9.0 (2013), fancybox 2.1.4, mousewheel 3.0.6; Google Fonts (Josefin Sans) chiamato in http. Nessun errore in console, nessuna risorsa rotta. [Certo]
5. **Contenuti vecchi e scarsi.** 89, 87, 85 e 42 parole nelle quattro pagine (303 in tutto). Foto del 2012; la gallery mostra la facciata con il neon rosa e l'insegna "PIZZERIA", che oggi non c'è più (facciata rifatta, foto del proprietario su Google). Nessun menu, nessun piatto di stagione, nessun evento; nessuna riga di copyright. Le recensioni Google recenti citano "Luca e i ragazzi in cucina": la squadra presentata sul sito potrebbe non essere più quella. [Certo; squadra DA CONFERMARE]
6. **Orari che non coincidono.** Sito: 10.00-15.00 e 18.00-24.00, chiuso il lunedì tranne d'estate. Google: lunedì chiuso, martedì 18-24, mercoledì-sabato 10-14:30 e 18-24, domenica 10-14:30 e 18-23. VisitMarostica: chiuso lunedì e martedì a pranzo. [Certo; orari veri DA CONFERMARE]
7. **Navigazione.** La voce "HOME" è marcata attiva su tutte le pagine (`class="active"` fisso). La pagina FESR si raggiunge solo da una striscia di loghi di 150x31 px in fondo alla Home, senza testo. Le gallery sono link `javascript:;`: senza JavaScript non si apre nulla e le 32 foto non sono nella pagina (invisibili anche ai motori di ricerca). [Certo]
8. **Leggibilità anche da computer.** Pagina Ristorante: il piede bianco cade sul piatto bianco della foto (`03-ristorante-1440.png`). Pagina FESR: testo bianco a tutta larghezza su una foto chiara, e lo stile in pagina annulla il `background-size: cover`, quindi la foto si ripete (`05-bando-1440.png`). [Certo]
9. **SEO di base assente.** Stesso `<title>` "L'Angelo e il Diavolo | Ristorante a Marostica" su 4 pagine su 5 e stessa meta description su 4 su 5; meta keywords; 4 H1 nella pagina 02, nessuno nella pagina FESR; nessun attributo `lang`; niente robots.txt, sitemap, favicon, dati strutturati Restaurant, Open Graph. Il dominio senza www risponde con le stesse pagine invece di reindirizzare. Alt generici ("APO", "BRUNA") o mancanti (loghi FESR). [Certo]
10. **Privacy e cookie.** Nessuna informativa privacy, nessuna informativa cookie, nessun banner. La mappa Google nella pagina Contatti si carica subito e fa 35-36 richieste a domini Google (www.google.com 12, maps.googleapis.com 19-20, maps.gstatic.com 2, places.googleapis.com 1, maps.google.it 1) prima di qualsiasi consenso; Google Fonts è chiamato da ogni pagina. [Certo]
11. **Dati societari.** Nel piede ci sono denominazione e P.IVA: l'obbligo minimo è rispettato. Mancano la sede legale (Corso Mazzini 21, diversa dal locale) e una PEC. [Certo]
12. **Peso e velocità: non sono il problema.** Cache vuota: Home 501 KB in 10 richieste, L'Angelo e il Diavolo 696 KB / 21, Ristorante 601 KB / 20, Contatti 1,2 MB / 51 (mappa), FESR 643 KB / 10; evento load tra 0,6 e 1,7 s (3,7 s per Contatti su telefono). Il file più pesante è sempre lo sfondo (452-506 KB). Va detto con onestà nella proposta. [Certo]
13. **Immagini.** Nessuna immagine mostrata più grande del naturale a 1440; le foto della gallery si aprono a 800 px, piccole per uno schermo moderno; gli sfondi da 2000 px coprono 1440 px a densità 1 ma non uno schermo retina. [Certo]
14. **Link esterni.** Facebook: il vecchio indirizzo `/pages/Langelo-e-il-diavolo/102752506511293` ora porta a `/p/Langelo-e-il-diavolo-100063717151643/` (con login). Tripadvisor in http, reindirizzato a https. `vocidalcuore.com` porta a `vocidalcuore.it`, fermo al 2013. Instagram (`@l_angelo_eil_diavolo`, stampato sulla tovaglietta) non è collegato dal sito. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | L'Angelo e il Diavolo L'Osteria di Apo Oste in Marostica di Ambrosi Roberto | piede del sito; VIES; aziende.it |
| Forma | impresa individuale, titolare Roberto Ambrosi ("Apo") | denominazione; aziende.it |
| P.IVA | 02198470243 (VIES: valida, interrogata il 06/10/2026) | VIES `ec.europa.eu/taxation_customs/vies` |
| REA | VI-213537, CCIAA di Vicenza | aziende.it (dato aggiornato al 27/09/2025) |
| Iscrizione | 16/04/1991 | aziende.it |
| ATECO | 56.10.11 Ristorazione con somministrazione | aziende.it |
| Dipendenti | 10-19 | aziende.it (27/09/2025) |
| Fatturato | non disponibile (impresa individuale, nessun bilancio depositato) | |
| Sede legale (VIES) | Corso G. Mazzini 21, interno 2, centro storico, 36063 Marostica (VI) | VIES |
| Locale | Piazza Castello 41/A, 36063 Marostica (VI); Plus Code PMW4+95 | sito; Google |
| Telefono | 0424 72312 (+39 0424 72312) | sito; Google; VisitMarostica |
| Email | robertoapoambrosi@gmail.com (sito); lorenzo.a7788@gmail.com (VisitMarostica) | |
| PEC | **da cercare su INI-PEC** (`inipec.gov.it`): il servizio ha respinto le richieste automatiche ("Request Rejected"); per un'impresa individuale iscritta al registro la PEC è obbligatoria | |
| Orari | vedi problema 6: tre versioni diverse | sito; Google; VisitMarostica |
| Coperti | 45 interni, 50 all'esterno | VisitMarostica [DA CONFERMARE] |
| Google | "L'Angelo e il Diavolo", categoria Ristorante veneziano (anche italiano e romano), 4,4 su 568 recensioni, 513 foto (06/10/2026) | scheda Google, place_id ChIJ_5tqOb7PeEcRgmJ0iY78u3E |
| Social | Facebook `facebook.com/p/Langelo-e-il-diavolo-100063717151643/`; Instagram `@l_angelo_eil_diavolo` (letto dal QR della tovaglietta); Tripadvisor d2626610 | |
| Contributo pubblico | PR Veneto FESR 2021-2027, progetto del Distretto del Commercio di Marostica: spesa ammessa all'impresa € 28.341,29, contributo € 19.989,96. La pagina di pubblicità va tenuta nel nuovo sito. | pagina `Bando_pr_veneto.htm` |
| Dominio | angeloeildiavolo.com, registrato il 01/12/2008, scade il 01/12/2026 | RDAP Verisign |
| Anni di attività | impresa iscritta dal 1991; il nome compare nell'illustrazione di Don Backy datata 1998. Apertura dell'osteria [DA CONFERMARE] | aziende.it; foto `locale-01` |

## URL vecchi

Da reindirizzare con 301 (le destinazioni si fissano in 03 e in `plugin/redirect-301.csv`):

| URL vecchio | Contenuto |
|---|---|
| `http://www.angeloeildiavolo.com/` | Home |
| `http://angeloeildiavolo.com/` | Home duplicata senza www |
| `/index.htm` | Home |
| `/l-angelo-e-il-diavolo.htm` | storia e persone |
| `/ristorante.htm` | cucina |
| `/contatti.htm` | contatti e mappa |
| `/Bando_pr_veneto.htm` | pubblicità del contributo FESR (da tenere) |
| `/images/locale/foto1.jpg` ... `foto9.jpg` | foto della gallery, eventualmente indicizzate da Google Immagini |
| `/images/ristorante/foto1.jpg` ... `foto23.jpg` | come sopra |

Il server è IIS e non distingue maiuscole e minuscole (`/images/Cucina4.jpg` risponde come `/images/cucina4.jpg`): i redirect vanno scritti anche per `/Bando_pr_veneto.htm` in minuscolo.

## Da confermare col cliente

- Orari reali, chiusura del lunedì d'estate, pranzo del martedì.
- Squadra di oggi (Bruna e Lorenzo in sala e in cucina? chi è Luca?) e nuove foto delle persone.
- Porcetto ogni domenica: c'è ancora? E la cucina sarda?
- Adesione a "I Ristoranti dell'Oca".
- Anno di apertura dell'osteria (impresa dal 1991).
- Logo in vettoriale; colori ufficiali (rosso vino #A02B46 e nero #070E14 misurati sul file del Comune).
- Licenza d'uso e originali delle foto di Paolo Bittante; permesso per l'illustrazione di Don Backy e la vignetta firmata "Jacovitti".
- Uso delle foto pubblicate sul portale del Comune e sulla scheda Google (sono loro?).
- PEC dell'impresa (da INI-PEC).
- Tenere o togliere il rimando a Voci dal Cuore e "30 Nodi per il fegato".
- Accesso a Instagram e Facebook per prendere foto recenti.

## Fonti e file di lavoro

Crawl completo in `_prova/crawl/` (pagine, intestazioni HTTP, `sito/images/`, pagine esterne in `esterne/`), script in `_prova/script/` (`misura.cjs` misure e screenshot, `galleria.cjs` prova della gallery, `gmaps.cjs` scheda Google, `organizza.py` inventario), screenshot in `_prova/attuale/`, provini delle foto in `_prova/provini/`. Non raggiungibili da questa sessione: Wayback Machine (bloccata dalla policy di rete), INI-PEC (richiesta respinta), Instagram e Facebook (login), Tripadvisor (403), galleria completa di Google Maps (modalità anonima limitata). La ricerca web generica non ha dato risultati utili; le fonti sono state aperte direttamente.
