# 01. Analisi del sito attuale (www.villapollini.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[Ipotesi]** da verificare con il cliente, **[DA CONFERMARE]** dato che non si può usare finché il cliente non lo conferma.

## In breve

- Villa veneta dell'Ottocento a Luvigliano di Torreglia (PD), sui Colli Euganei, già residenza estiva del pianista Cesare Pollini. Oggi è una location per matrimoni ed eventi con cucina interna gestita dal proprietario, Alberto Piacentini ("Chef Alberto"), enoteca Vinus, vino della tenuta e 4 appartamenti. Marchio attuale: **Villa Pollini The Real Wedding**. [Certo]
- Il sito è un WordPress 4.8.32 con tema Enfold 4.1 e Slider Revolution 5.4.6 (2017). È responsive (nessuno scorrimento orizzontale a 390 px), ma è fermo: ultimo articolo del 1/5/2020, in home tre articoli su Coronavirus e Covid-19, ultima modifica a una pagina il 5/7/2021. [Certo]
- Il materiale fotografico vero c'è ed è più ricco del previsto: 239 foto dell'azienda nella libreria del sito, di cui 48 larghe almeno 1600 px, più 4 foto caricate dal proprietario su Google (una della barchessa a **5436x3624**, nitida e professionale) e un fotogramma 1280x720 dal canale YouTube. Ma oggi il sito apre con immagini stock: due delle tre immagini dello slider della home sono schermate di video stock (la terza è una foto vera del viale, 800 px allargata a 1440), la fascia "Wedding" è una foto stock, la "Carta dei Vini" è una foto Fotolia. [Certo]
- Identità attuale: emblema circolare con grappolo stilizzato in malva #8b647a e grigio caldo #a89b94 (colori del file del logo) e scritta "VILLAPOLLINI The Real Wedding" in serif maiuscolo spaziato. Il tema usa marrone caldo #786258 per pulsanti e footer (196 occorrenze nel CSS dinamico `avia_vinus.css`), fondo #efefec, testi #39342d, piede #2b2822; titoli in Fjalla One, testi in Laila. Il carattere Laila disegna gli accenti gravi come acuti: a schermo si legge "piú", "é", "cittá" su tutte le pagine. Esiste anche un disegno a matita della villa (1921x1208) usato come sfondo della pagina La Villa. [Certo]
- Privacy ferma al D.Lgs. 196/2003, banner con consenso implicito, Google Analytics, Pixel di Facebook e YouTube caricati prima di qualsiasi scelta: 11 cookie di Google Analytics, Facebook, YouTube e reCAPTCHA al primo caricamento della home. [Certo]
- **Rischio sull'attività**: l'ultima traccia pubblica verificata è una recensione su matrimonio.com del 13/10/2023 per un matrimonio dell'8/9/2023. Dopo, niente di verificabile senza login (Facebook e Instagram). Google non la segna chiusa. Prima di costruire la demo l'utente deve controllare Instagram e Facebook con il suo account. Dettagli sotto. [Certo per le date, Ipotesi sull'attività di oggi]

## L'attività è ancora aperta? Cosa dicono le fonti

| Fonte | Ultima traccia | Cosa dice |
|---|---|---|
| Sito villapollini.it (API REST) | articolo 1/5/2020, pagina 5/7/2021, file caricati fino al 1/5/2020 | fermo [Certo] |
| matrimonio.com, scheda e51751 | recensione 13/10/2023 (matrimonio 8/9/2023), recensione 21/9/2023; foto caricate fino al 3/3/2022 | 52 recensioni, 4,7/5, "94% consiglia"; nessun segno di chiusura [Certo] |
| Google Maps, "Villa Pollini The Real Wedding" (place_id ChIJaze8G4Agf0cRs4EcriVVBLo) | foto del proprietario del 6/1/2022; recensioni più rilevanti "3, 4, 5 anni fa" | 4,1 stelle, 137 recensioni, 533 foto; non segnata "chiusa definitivamente"; orario "Aperto 24 ore su 24" (non significativo) [Certo] |
| YouTube "Villa Pollini The Real Wedding" | video del 17/5/2022 | 15 video, testimonianze di sposi del 2021 [Certo] |
| Facebook facebook.com/villapollini ("Villa Pollini Weddings") | non leggibile senza login | 1.846 follower, 1.359 "were here" (meta pubblici letti il 6/10/2026) [Certo] |
| Instagram instagram.com/villapollini | non leggibile senza login | [DA CONFERMARE] |
| Certificato HTTPS | rinnovo Let's Encrypt emesso il 9/9/2026 (crt.sh) | hosting attivo; non prova che l'attività lavori [Certo] |
| agriturismi.it | data ignota | titolo della scheda "Struttura non attiva" (riguarda l'agriturismo, cioè gli appartamenti) [Certo per il titolo] |
| vinus.eu | oggi | dominio in vendita (Nameshift): l'indirizzo esther@vinus.eu usato nel 2018-2019 non funziona più [Probabile] |

Conclusione: attività documentata fino all'autunno 2023. Da lì in poi nessuna prova pubblica, né di apertura né di chiusura. Prima della demo: l'utente controlla data dell'ultimo post su Instagram e Facebook e la scheda Google da telefono. Se l'ultimo segnale resta il 2023, la proposta va riformulata o sospesa.

## Pagine esistenti

Il menu ha 9 voci: WELCOME, La Villa, Matrimoni ed eventi, Enoteca, Stanze, Ristorazione, informazioni, Il Blog di Alberto Piacentini, Contatti. Tutte le pagine rispondono 200. [Certo]

| Pagina | URL | Ultima modifica | Contenuto |
|---|---|---|---|
| Home ("Welcome") | `/` | 8/1/2020 | slider di 3 immagini stock, testo di presentazione, carosello del blog (articoli Covid), 3 riquadri La Villa / Matrimoni / Enoteca, fascia "Wedding" stock, 3 blocchi Villa / Cucina / Vini, popup modulo |
| Matrimoni ed eventi | `/matrimoni/` | 5/7/2021 | slider, "La giusta Location", badge matrimonio.com 2017, "Sposarsi a Luvigliano", galleria di foto di ricevimenti, modulo "Richiedi informazioni", "Le Portate" (galleria piatti con stock), "I Vini" |
| La Villa | `/matrimoni/la-villa/` | 20/10/2017 | storia della villa raccontata dalla mascotte "Cesarino", disegno della villa |
| Le Stanze | `/matrimoni/stanze/` | 20/10/2017 | 4 appartamenti (Pometto, Melograno, Uva Rossa, Uva Bianca) illustrati con foto stock di frutta, servizi, dintorni |
| informazioni | `/matrimoni/informazioni/` | 20/10/2017 | "Perchè villa Pollini": spazi e capienza, servizi, ristorazione, altri servizi |
| Contatti | `/matrimoni/contatti/` | 5/7/2021 | modulo con scelta del servizio, mappa Google |
| Enoteca | `/enoteca/` | 21/10/2017 | testo Vinus, galleria (in gran parte stock), "I Vini", "Le Portate" |
| Ristorazione | `/ristorazione/` | 16/10/2017 | La cucina, Lo Chef, I menù, "Un menù per ogni richiesta"; fascia vuota di circa 650 px (immagine di sfondo in 404) |
| Il Blog di Alberto Piacentini | `/news-ed-eventi/` | 8/1/2020 | elenco dei 25 articoli |
| Doppione dell'Enoteca | `/matrimoni-in-villa/` | 11/4/2019 | stessa pagina dell'Enoteca con titolo "Enoteca" e slug "matrimoni-in-villa", fuori menu |
| Privacy Policy | `/privacy-policy-informativa-sui-cookies/` | 16/10/2017 | informativa ex D.Lgs. 196/2003 |
| 25 articoli | `/enoteca/...`, `/la-villa/...`, `/matrimoni-ed-eventi/...` | 2015-2020 | eventi 2014-2019 e "Dal mio Blog" di Alberto (dicembre 2019 - maggio 2020) |
| Archivi | 3 categorie, 28 tag, 3 autori | | pagine automatiche di WordPress |
| Demo del tema | 10 pagine `/portfolio-articoli/...` | | contenuti dimostrativi di Enfold mai cancellati ("MacBook Air & Juice", "Cam", "Pill Pack", "Juicey. An illustration that I did a while back") |

Screenshot a 1440 e 390 di 12 pagine (più una demo) in `_prova/attuale/` (`NN-pagina-1440.png`, `-390.png`, `-top.png`), misure in `NN-pagina-LARGHEZZA.json`.

## Testi reali (verbatim, con i refusi originali)

Testi copiati dal sorgente HTML. A schermo gli accenti gravi appaiono acuti per colpa del carattere (vedi problemi). Dove il testo originale contiene una formula generica della lista `PAROLE_VIETATE` è sostituita da `[...]`; il testo completo di ogni pagina è in `_prova/crawl/testi/`.

Home:
1. Titolo della finestra: "Villa Pollini - Enoteca Villa Pollini" (trattino medio nell'originale). Slider: "Matrimoni ed Eventi", "La Villa", "Enoteca", ognuno con il sottotitolo in inglese del tema dimostrativo "Dedicated. Inspired. Passionate."
2. "Villa Pollini è l’unica location a offrire un parco dentro al parco dei colli Euganei, con enoteca e cucina gestita dal proprietario della villa, cucina che parte dai piatti della tradizione veneta realizzata con prodotti del territorio, arricchita da ingredienti personalmente selezionati in diverse regioni d’Italia."
3. "Circondata da colline e rigogliosi vigneti, potrai festeggiare The Real Wedding, il matrimonio che vuoi tu, grazie alla nostra capacità di accogliere e ascoltare le tue richieste e realizzare il tuo evento in un contesto intimo e familiare, senza rinunciare ad eleganza e professionalità. In più, in esclusiva solo per te una soluzione in caso di maltempo in cui il verde rimane l’indiscusso protagonista del tuo ricevimento."
4. "A differenza di ville austere con ambienti enormi, parchi dispersivi e cucine con menù scontati o che si affidano a catering esterni, Villa Pollini con i suoi spazi avvolgenti, saprà soddisfare le tue esigenze di ricercatezza e accoglienza."
5. Riquadri: "LA VILLA. Dimora del famoso pianista Cesare Pollini già al primo impatto dona subito una sensazione magica, un melange di poesia e musica. Abbracciata da lussureggianti parchi e ricchi vigneti,…" / "MATRIMONI ED EVENTI. Villa Pollini propone agli sposi un servizio [...]. Dal pranzo ai vini, dall’allestimento ai fiori, dalla musica ai fuochi artificiali." / "ENOTECA. Tanti vini di qualità aspettano solo di essere scoperti ed apprezzati."
6. "Wedding. La location ideale per il vostro giorno più bello"
7. "Cenni strorici e / Curiosità sulla Villa. Il pittoresco borgo di Luvigliano ospita la nostra Villa, dapprima appartenuta al celebre pianista Cesare Pollini, ora un piccolo angolo di paradiso enogastronomico, ricco di sapori e cultura nostrana. Un ambientazione suggestiva, con alle spalle una maestosa Villa dei Vescovi, scolpiscono in questo edificio padronale un ambientazione di altri tempi, quasi a riportare i nostri ospiti indietro nel tempo a più di un secolo fa."
8. "La Cucina / Il Sapore della tradizione. Se da una parte la Villa ricorda tempi antichi, per la cucina è tutta invece riservata una raffinata attualità. Certo, le basi dei nostri piatti attingono dalla cultura gastronomica che va dai classici veneti e non solo, arrivando però ad accarezzare ricette e impiattamenti della cucina moderna. Tutto qui è di prima qualità con materie prime fresche e ricercate."
9. "La nostra prestigiosa / Carta dei Vini. Se si parla di Colli Euganei non si può non fare un cenno alle profumate note delle nostre prestigiose etichette. Un eccellente selezione di vini pregiati di produzione propria e non solo, accompagnano gli eventi marchiati Villa Pollini."
10. Popup a ogni pagina: "Scopri i segreti del matrimonio a Villa Pollini" con Nome, Email, Telefono (richiesti).
11. Footer: "VINUS / Vinus di Alberto Piacentini - Azienda Agricola Villa Pollini - Via Cesare Pollini 2/4 - 35038 Torreglia (Padova) - Italia / P.IVA 04167920281 - 01982980284 Tel. +39 348/4162004 E-Mail: esther@villapollini.it / Powered by Netbanana" (nel sito i separatori sono trattini medi).

Matrimoni ed eventi:
12. Slider: "L'Eleganza al vostro servizio / Matrimoni ed Eventi".
13. "La giusta Location. Situata sugli esclusivi Colli Euganei, da tempo meta di molti padovani alla ricerca di relax e paesaggi mozzafiato, Villa Pollini è location ideale per il giorno del tuo matrimonio o per altri eventi indimenticabili. [...] Barchesse e terrazze diventano palcoscenici adatti alle più svariate scenografie."
14. "Villa Pollini offre un servizio banqueting personalizzato, elegante, raffinato e professionale in grado di realizzare il ricevimento dei Vostri sogni. Villa Pollini con la sua cantina ricca di vini di propria produzione e Vinus, con la sua prestigiosa carta dei vini provenienti da tutta Italia, consentono di arricchire il vostro banchetto con un wine banqueting tutto personalizzato."
15. "Offriamo inoltre quattro comodi appartamenti arredati in stile per gli sposi e i loro ospiti che vorranno soffermarsi e godere delle magiche atmosfere della Villa."
16. "Sposarsi a Luvigliano. La romantica Chiesa a pochi passi dai nostri cancelli é ideale per celebrare il rito religioso. La convenzione stipulata con il Comune di Torreglia potrà rendere realtà il sogno di sposarvi circondati dalla natura in una ambientazione elegante ed unica." (qui "é" è nel sorgente)
17. "Dal pranzo ai vini, dall’allestimento ai fiori, dalla musica ai fuochi artificiali. La comodità di scegliere una location che organizza tutto senza intoppi ne lacune. Nulla è lasciato al caso, per darti la serenità di vivere questa giornata al pieno lasciando gli invitati alle cure del nostro staff, pronto a risolvere ogni necessità con professionalità e cortesia."
18. "Le Portate. Dalla cucina internazionale ai piatti della nostra tradizione, nulla è lasciato al caso. Antipasti ricercati a base di pesce, proposte di cucina etnica e piatti regionali fanno parte delle nostra proposta."
19. "I Vini. Una carta dei vini di tutto rispetto per Villa Pollini, che raccoglie etichette dalla pregiata cantina Vinus, provenienti dalle cantine del nostro Parco Colli e dalle altre regioni del nostro Bel Paese."

La Villa (raccontata dalla mascotte "Ciao! io sono Cesarino"):
20. Slider: "L'arte, la natura e la musica si incontrano / Villa Pollini". Titolo: "Un pò di storia".
21. "Nel pittoresco borgo di Luvigliano, frazione di Torreglia, si trova la bella Villa che prende il nome, come me, dal suo primo illustre proprietario, il pianista Cesare Pollini (1858-1912). La bianca e luminosa costruzione sorge tra i rigogliosi vigneti della collina e la si raggiunge tramite una stradina laterale della via che sale verso la chiesa parrocchiale, dirimpetto alla monumentale e nota Villa dei Vescovi."
22. "La dimora fu per molti anni punto d’incontro dei più rinomati artisti veneti tra cui il famoso pittore Roberto Ferruzzi e l’ancor più conosciuto scrittore Antonio Fogazzaro."
23. "La Villa ha una struttura a “L” con l’edificio padronale che si affaccia verso sud e gli annessi rivolti verso ovest. La parte padronale presenta la tipica struttura delle ville venete dell’ Ottocento, con un’architettura semplice e lineare, sviluppata su due piani, con una spaziosa sala di ingresso aperta sui due lati dell’edificio e a cui si accede tramite una porta decorata da un arco a tutto sesto in pietra."
24. "L’elegante barchessa che si appoggia al fianco occidentale della casa è resa molto luminosa dagli ampi archi in mattoni che lasciano entrare la luce sul lato che dà sul parco interno. Un tempo questa struttura era utilizzata per lo stoccaggio dei raccolti agricoli e ospitava i contadini che lavoravano le terre dei proprietari. Oggi invece è adibita alla realizzazione di esclusive cerimonie e banchetti, così come il lussureggiante giardino all’italiana antistante la casa padronale. Nella bella stagione vengono organizzati anche concerti di musica classica, spesso in memoria di Cesare Pollini."
25. "Attualmente la Villa ha tra le sue attività la produzione e la vendita di pregiati vini, con varie etichette DOC e DOCG. Offre inoltre la possibilità di soggiornare all’interno di alcuni appartamenti ricavati nelle adiacenze, ristrutturate con grande cura."
26. Iscrizione sulla parete: "“In questa villa, dai cocenti meriggi estivi al morir dell’autunno, per molti anni visse Cesare Pollini. L’avita nobiltà del suo spirito tradusse, rivelò, profuse in sublimi armonie.”"

Le Stanze:
27. Slider: "Appartamenti caratteristici per una vacanza all’insegna del Relax / Le Stanze". Nomi: Pometto, Melograno, Uva Rossa, Uva Bianca.
28. "Dall’adiacente rustico, sobrio e dal raffinato stile country, sono stati ricavati i nostri quattro deliziosi appartamenti, ideali per trascorrere una vacanza tranquilla tra il verde, le attività sportive e rilassanti cure termali; senza però trascurare le visite alle città d’Arte di cui gode il luogo. Lasciatevi conquistare dal pittoresco ambiente che circonda Villa Pollini dove… …ogni finestra è un quadro!"
29. "Tutti i nostri appartamenti sono composti da soggiorno con angolo cottura, stanza da letto e bagno." Servizi offerti: "Pernottamento da 2 a 4 persone / Parcheggio / TV satellitare / Wi-fi gratuito / Vini e Prodotti tipici". Nelle vicinanze: "Terme / Passeggiate / Golf, maneggio e piscina / Città d’arte / Stazione FFSS e Autobus".

informazioni ("Perchè villa Pollini"):
30. "Spazi e capienza. Eleganti e raffinati sono i saloni della villa al cui interno si caratterizzano per la presenza di ampie vetrate ed un arredo in stile che rende molto caldo ed intimo l’ambiente che a tutt’oggi è abitato. All’esterno terrazza e barchessa si affacciano sul parco ricco dei colori di fiori e piante da Marzo ad Ottobre inoltrato. [...] I nomi prendono il nome dai prodotti locali della zona, tra cui Uva Bianca, Uva Rossa, Il Melograno e il Pometto."
31. "Servizi offerti. Lo staff di Villa Pollini per il vostro evento è in grado di prepararvi un allestimento personalizzato e una mise en place raffinata. Agili e flessibili nell’adattare la situazione in base alle condizioni del tempo, Vi seguiremo in ogni minimo dettaglio consigliandoVi ma lasciando anche al Vostro estro e fantasia la massima libertà in modo da ottenere un ricevimento su misura."
32. "Ristorazione. I prodotti locali di ottima qualità e freschezza, sempre di stagione, rielaborati nei migliori piatti della tradizione e/o della cucina internazionale, vi verranno proposti per il banchetto nuziale accostati ai vini di propria produzione (Merlot, Pinot, Cabernet, Seprino, Manzoni Bianco, Chardonnay brut, Fior d’Arancio Spumante e Passito) e di tutta Italia, disponibili anche nel proprio punto vendita in azienda."
33. "Altri servizi. A Villa Pollini avrete inoltre l’opportunità di poter celebrare anche la Vostra cerimonia. Che sia essa religiosa o civile potrete usufruire della vicina Chiesa di S.Martino così come della Villa stessa che dal 2014 è convenzionata con il Comune di Torreglia. In questo secondo caso forniremo noi quanto necessario per l’allestimento (fiori esclusi) sempre compreso nel prezzo."
34. "Il nostro lavoro è quello di darVi una Villa in “splendida forma” e un servizio banqueting impeccabile. Ma a richiesta saremo in grado di assisterVi su tutto, grazie alla nostra partnership con i migliori operatori del settore (fiori, musica, animazione e assistenza bimbi, nolo auto d’epoca, agenzia viaggi, …) con i quali verrete messi direttamente in contatto senza ulteriori costi aggiuntivi."

Contatti:
35. "Contattaci per informazioni". Menu del modulo "Quale servizio ti interessa*": "matrimonio / banchetto / buffet aziendale / pernottamento / altro...".

Enoteca:
36. Slider: "Le pregiate etichette Vinus e non solo… / Enoteca".
37. "Tanti vini di qualità aspettano solo di essere scoperti ed apprezzati. Tanti produttori aspirano a vedere il frutto del loro appassionato lavoro in vigna e in cantina premiato nel modo più gratificante, con il piacere di chi lo beve, con la soddisfazione di chi lo propone."
38. "Questo è il credo di VINUS che presenta il meglio del patrimonio enologico italiano attraverso l’esperienza di produttori emergenti che con attenzione, [...] e rispetto della tradizione hanno raggiunto l’[...] a livello locale e forti della freschezza delle loro idee iniziano ad affermarsi a livello nazionale. Un lavoro di ricerca prezioso nelle aree vinicole d’Italia più vocate, dalle austere colline delle Langhe, alle raffinate “sciare” dell’Etna."
39. "Un viaggio alla ricerca di Nisa, il monte leggendario, lussureggiante e fertile dove Bacco trovò la vite e imparò a coltivarla. [...] Il piacere di vivere e saper vivere. [...] Vini allegri… vini lussureggianti… vini felici di essere bevuti!"

Ristorazione:
40. Slider: "Il connubio tra i sapori del passato e l’innovazione gastronomica / La Cucina".
41. "La cucina rivisita i piatti della cucina tradizionale italiana proponendoli in una chiave contemporanea, in una sapiente combinazione di sapori e contrasti. Che si tratti di un lussuoso ricevimento di matrimonio o di una particolare serata a tema, caratteristica indiscussa è la stagionalità delle proposte per garantire la freschezza di ogni portata e l’adeguatezza al periodo in cui viene proposta."
42. "Lo Chef. Competenza, esperienza nel settore del banqueting di lusso e fantasia sono le doti di Chef Alberto che assieme ai suoi collaboratori darà vita a creazioni che sapranno personalizzare e rendere speciale il Vostro menù."
43. "I menù sono strutturati per sfruttare appieno le caratteristiche di una location dalle molteplici ambientazioni. L’aperitivo davanti alla Villa, i grandi buffet ad isole nel Parco, i primi e i secondi seduti in Barchessa e i trionfi di dolci e frutta sono un punto fermo su cui inserire di volta in volta le proposte gastronomiche in base alle Vostre richieste e ai Vostri gusti."
44. "Quando la nostra cucina non basta per tutti siamo pronti a soddisfare anche le singole richieste di ogni Vostro invitato. Ecco allora che vegani, vegetariani, ciliaci, tutti si troveranno a proprio agio con piatti a loro dedicati, così come i piccoli ospiti che saranno coccolati come a casa loro."

Blog e articoli (titoli e frasi utili):
45. Testata degli articoli: "L’INGREDIENTE SEGRETO / Il Blog di Alberto Piacentini". Firma: "Contact Esther / Tel. +393484162004 / mail: esther@villapollini.it / Alla prossima! / Alberto".
46. "Vino e matrimonio: una coppia che deve tornare vincente!" (7/12/2019): "lavoro nel mondo del vino praticamente da sempre. Prima produttore e venditore al dettaglio. Poi anche venditore distributore all’ingrosso. Poi ancora wine banqueting manager per la ditta che ho creato nel 2007, la ditta Vinus, fino all’inizio della attività di wedding in villa, sempre creata da me". E: "Mettete il vino al centro del vostro ricevimento!!"
47. "#cheFusion. D'Italia & d'Amore. Il mio Perchè in cucina!" (1/5/2020): "una cucina ti ricordo dedicata solo al mondo del wedding". Dentro l'articolo compare la scritta tedesca di Facebook "Gepostet von Villa Pollini Weddings am Freitag, 3. April 2020".
48. "Domeniche a Villa Pollini" (28/10/2018): "Domenica 11 novembre alle 14:30 diamo ufficialmente il via al progetto “Domeniche in Villa Pollini” curato da Villa Pollini e l’associazione culturale Fantalica di Padova con il Patrocinio del Comune di Torreglia." Visita guidata "a cura di Esther Messina", degustazione del serprino "a cura di Alberto Piacentini". "Biglietti: 12 euro, gratuito fino a otto anni. Ridotto 6 euro".
49. "Giornate del FAI a Villa Pollini" (20/2/2018): "le giornate nazionali del FAI che si terranno il 24 e 25 Marzo 2018 ci vedranno protagonisti assieme a Villa dei Vescovi!"
50. "50° mostra dei vini 2019" (25/10/2019): "Dal 26 ottobre fino al 10 novembre a Villa Pollini si terrà la 50° mostra dei vini dei Colli Euganei".
51. "Se ancora non conosci Villa Pollini" (11/5/2015): "Una perla nel verde, un luogo dove ritrovare pace e i piaceri della buona tavola."

Testo dell'azienda su matrimonio.com (fonte esterna, scritto da loro):
52. "Villa Pollini è l'unica location in cui il proprietario è anche lo chef e segue i vini della cantina prodotti dai vigneti della tenuta. Per voi sposi ciò significa cucina e vini di alta qualità."
53. "Villa Pollini vi mette a disposizione senza limiti di tempo e limiti alcuni i seguenti spazi: l'elegante barchessa, la limonaia, i due giardini, i vigneti, la casa nel bosco per i vostri ospiti più piccoli e un gazebo di rose per il rito civile."
54. "da noi non piove mai perché grazie a un incredibile piano B che troverete solo qui." Menù tipo: "Brindisi d'arrivo, aperitivo, gran buffet ad isole, due primi, secondo, contorni, carta dei vini, dolce della sposa e buffet frutta, servizio open bar". Storia: "Costruita alla fine del 1600 Villa Pollini nasce come confraternita della Curia di Padova. [...] Nel 1972 con l'acquisto da parte della famiglia Ghedini torna allo splendore degli anni in cui il pianista visse qui." [DA CONFERMARE: la data di costruzione del 1600 contrasta con "ville venete dell'Ottocento" del sito]

Refusi e incoerenze da non riportare nel nuovo sito: "Cenni strorici", "Un ambientazione", "Un eccellente selezione", "Un pò", "Perchè", "ciliaci", "Seprino" (è Serprino), "senza intoppi ne lacune", "delle nostra proposta", "I nomi prendono il nome", "ristrutturate" riferito agli appartamenti, "dell’ Ottocento", "50° mostra" (50ª), "é" al posto di "è" nella frase sulla chiesa, sottotitolo inglese del tema "Dedicated. Inspired. Passionate.", voce di menu "WELCOME" in inglese e "informazioni" minuscolo. Il nome dell'attività compare in quattro forme: Villa Pollini, Villa Pollini The Real Wedding, Vinus, Enoteca Villa Pollini; il nuovo sito usa **Villa Pollini** con il sottotitolo "The Real Wedding" del logo [DA CONFERMARE].

## Cosa fanno e cosa vendono

- **Matrimoni in villa, tutto compreso**: location, cucina interna, vini della tenuta, allestimento; rito civile in villa (convenzione con il Comune di Torreglia dal 2014) o religioso nella vicina chiesa di S. Martino di Luvigliano. Capienza 10-170 invitati, un solo evento al giorno, esclusiva sul catering, suite nuziale (matrimonio.com). [Certo]
- **Spazi**: villa padronale a L con sale interne (carta da parati floreale, camini, collezione di piatti alle pareti, lampadari), barchessa ad archi in mattoni, terrazza, limonaia, giardino all'italiana con bossi a palla, due parchi con ortensie e cedri, pergola per il rito, vigneti, "casa nel bosco" per i bambini, gazebo di rose. Vista sulla Villa dei Vescovi (FAI) e sul campanile di Luvigliano. [Certo, da testi e foto]
- **Cucina** di Chef Alberto Piacentini: tradizione veneta e italiana, pesce, buffet a isole nel parco (barca di sushi, ostriche, taglio del prosciutto), menù per vegani, vegetariani, celiaci; marchio della cucina "cheFusion. D'Italia & d'Amore". [Certo]
- **Vino**: vini della tenuta (Merlot, Pinot, Cabernet, Serprino, Manzoni Bianco, Chardonnay brut, Fior d'Arancio Spumante, Passito; etichette Villa Pollini fotografate per Passito e Serprino) ed enoteca **Vinus** con etichette di altre regioni (Langhe, Etna; in foto una cassetta Caparzo). Punto vendita in azienda. [Certo]
- **Ospitalità**: 4 appartamenti (Uva Bianca, Uva Rossa, Il Melograno, Il Pometto) da 2 a 4 persone, soggiorno con angolo cottura, camera e bagno; parcheggio, TV satellitare, Wi-fi. Stato attuale [DA CONFERMARE]: agriturismi.it segna la struttura "non attiva".
- **Eventi** (storici): Mostra dei vini DOC e DOCG dei Colli Euganei ospitata in villa (45ª nel 2014, 50ª dal 26/10 al 10/11/2019), Giornate FAI 24-25 marzo 2018 con Villa dei Vescovi, "Domeniche a Villa Pollini" 2018-2019 con l'associazione Fantalica, serate "Candle time", cesti natalizi, buffet aziendali. [Certo]
- Persone: **Alberto Piacentini** (titolare, chef, "architetto" secondo matrimonio.com) ed **Esther** (Esther Messina nell'articolo del 2018), riferimento per sposi e visite. [Certo per i nomi, ruolo di Esther DA CONFERMARE]

## Immagini usate oggi

Fonte: libreria WordPress esposta da `/wp-json/wp/v2/media`, 379 file (331 JPEG, 42 PNG, 1 GIF, 4 video MP4, 1 PDF), caricati tra il 2016 e il 1/5/2020. Tutti scaricati alla dimensione originale (WordPress 4.8 non riduce gli originali). Classificazione completa con soggetto, qualità e larghezza utile in `_prova/inventario-immagini.json`. [Certo]

| Gruppo | Quantità | Risoluzione | Giudizio e uso nel nuovo sito |
|---|---|---|---|
| Foto dell'azienda, scatti grandi (villa, barchessa, sale, parco, buffet) | 48 con larghezza da 1600 a 4092 px | sale e barchessa 1800-1900 px; piatti da iPhone 2366-3827 px; panoramica del parco 4092x1127 | utilizzabili fino a circa 900-1200 px CSS su retina; la facciata (`villa-facciata-viale-bossi-0617.jpg`, 1800x1200) regge una mezza pagina, non un'apertura retina a tutta larghezza. La panoramica 4092 px è da telefono, con effetto acquerello a 100%: solo striscia stretta |
| Foto dell'azienda, piccole (800-1500 px) | 59 | foto professionali di matrimoni a 800 px (fotografo, una con crediti Alessandro Capuzzo), ritratti di Alberto 1100-1400 px, appartamenti 300-1300 px | miniature, gallerie, ritratto piccolo |
| Serie da smartphone 2016 | 110 | 533x948 o 948x533 | solo miniature; molti volti di sposi e ospiti |
| Grafiche dell'azienda | 23 | logo attuale PNG 290 px ed emblema 500 px, loghi storici "Vinus", disegno a matita della villa 1921x1208, mascotte Cesarino, locandine, badge matrimonio.com | serve il logo vettoriale; il disegno della villa è un elemento identitario vero da riprendere |
| Escluse (stock, demo, prese dal web, doppioni) | 110 immagini + 5 file video e PDF | | 50 sono usate oggi nel sito: slider della home, fascia "Wedding", "Carta dei Vini", galleria "Le Portate", foto delle frutta degli appartamenti, galleria Enoteca. Non vanno riprese |
| Foto del proprietario su Google | 4 | **5436x3624** (barchessa apparecchiata, 2020), 1242x890 (sala), 1170x738 (tavoli nel parco al tramonto, firma di uno studio fotografico tagliata), 1080x1920 | la 5436 px è l'unica foto adatta a un'apertura a tutta larghezza anche su retina (fino a 2718 px CSS) |
| Fotogramma YouTube del canale aziendale | 1 | 1280x720 | "Mise en place" sotto il portico, dettaglio |

Immagini sgranate oggi (larghezza mostrata a 1440 contro larghezza naturale): slider della home `IMG_79334.png` 800 px allargata a 1440 (1,8 volte); slider di Matrimoni `portico-vinus.png` 645 px a 1440 (2,2 volte) e `0854-EL8A9241.png` 800 px a 1440; slider di La Villa e informazioni `20160618_182741.jpg` 533 px a 1440 (2,7 volte); slider delle Stanze `Stanza-fisheye1.jpg` 453 px a 1440 (3,2 volte); slider di Ristorazione 948 px a 1440. I tre riquadri della home usano ritagli 800x321. [Certo, misura in `_prova/attuale/*-1440.json`]

Fuori dal sito: matrimonio.com ha circa 140 foto caricate dall'azienda tra aprile 2019 e marzo 2022 (elenco in `_prova/crawl/esterne/mcom/urls.txt`), non scaricabili perché il CDN risponde 403 alla nostra rete; Facebook e Instagram richiedono login. Da chiedere al cliente: originali delle foto professionali (fotografi dei matrimoni, Alessandro Capuzzo, studio della foto del 2022), logo vettoriale. Le foto di utenti terzi su Google non sono state scaricate. La Wayback Machine non era raggiungibile dalla rete di lavoro (connessione chiusa e risposta 429 il 6/10/2026): non serve per le foto, perché la libreria del sito è già completa agli originali.

## Problemi tecnici da segnalare al cliente

1. **Software del 2017**: WordPress 4.8.32 (meta generator), tema Enfold 4.1 (`style.css` versione 4.1.2), Slider Revolution 5.4.6, Contact Form 7 5.1.1, Cookie Notice 1.2.39, Holler Box 1.5.0, Pixel Caffeine 2.1.1. L'API pubblica elenca i 3 utenti del pannello (`admin`, `daniele`, `piacentini_editore`) e tutta la libreria media. `xmlrpc.php` è chiuso (403). [Certo]
2. **Contenuti fermi**: ultimo articolo 1/5/2020 ("Matrimonio e Covid-19. La prima guida per te!" e "#cheFusion"), in home il carosello mostra 3 articoli su Coronavirus e Covid; ultima pagina modificata 5/7/2021; badge "Consigliato 2017"; 10 pagine dimostrative del tema ancora pubbliche (`/portfolio-articoli/cam/`, `/portfolio-articoli/macbook-air/`...); pagina doppione `/matrimoni-in-villa/` con il testo dell'Enoteca. Nessun copyright con anno, solo "Powered by Netbanana". [Certo]
3. **Privacy e cookie**: informativa "ex art. 13 d.lgs. 196/2003", nessuna menzione del Regolamento UE 2016/679 (0 occorrenze), pagina del 16/10/2017; banner "Per offrirti il miglior servizio possibile questo sito utilizza cookies. Continuando la navigazione nel sito autorizzi l’uso dei cookies." senza pulsante di rifiuto. Al primo caricamento della home, prima di ogni clic, il browser riceve Google Analytics (`analytics.js` e `G-VT3HRBC3MZ`), il Pixel di Facebook (`fbevents.js`), YouTube, reCAPTCHA e Google Fonts, e salva 11 cookie di servizi esterni: `_ga`, `_gid`, `_gat`, `_ga_VT3HRBC3MZ`, `_fbp`, `fr`, `_GRECAPTCHA`, `YSC`, `VISITOR_INFO1_LIVE`, `__Secure-YNID`, `__Secure-ROLLOUT_TOKEN` (log di rete in `_prova/attuale/01-home-1440.json`). La mappa Google della pagina Contatti si carica subito. I tre moduli (popup, "Richiedi informazioni", Contatti) chiedono nome, email e telefono senza richiamo all'informativa. [Certo]
4. **Dati personali esposti nella libreria pubblica**: due foto di un verbale SIAE del 18/6/2016 con nome, data di nascita e firma del titolare sono scaricabili da `/wp-content/uploads/2017/10/20160618_200637.jpg` e `..._200643.jpg` e compaiono nell'elenco pubblico `/wp-json/wp/v2/media`. Non sono collegate a nessuna pagina. Da segnalare con discrezione e da far cancellare; non sono state copiate in `assets/`. [Certo]
5. **Peso e velocità** (Chromium, misura da rete di lavoro, indicativa): home 100 richieste e 7,2 MB a 1440 (immagini 5,6 MB; le due immagini dello slider sono PNG da 1,5 e 1,0 MB), primo byte in 1,1 s, evento load a 7,6 s; Matrimoni 164 richieste e 11,8 MB; La Villa 6,8 MB. Un popup con modulo si apre a ogni pagina e copre la prima schermata, a 1440 e a 390. [Certo]
6. **Foto stock al posto delle foto vere**: slider della home = due schermate di video stock (`Schermata-2017-10-16-alle-10.02.23.png`, fotogramma di `wedding.mp4` con la sposa che corre nel bosco, e `...10.02.37.png`, bottiglie in cantina) più la foto vera del viale a 800 px; in libreria ci sono anche due schermate con la filigrana shutterstock ancora visibile; fascia "Wedding" = sposi con bicicletta (stock); "Carta dei Vini" = foto Fotolia (IPTC "Valentyn Volkov"); galleria "Le Portate" con almeno 6 piatti da shutterstock o presi dal web; galleria dell'Enoteca in gran parte stock (bottiglie, tappi, vigneto al tramonto, calici); appartamenti illustrati con mele, melograno e uva stock; il riquadro "Matrimoni ed eventi" della home usa `gallery_MATRIMONIO-meridiana-larghezza-max-1000px...jpg`, probabilmente presa dal sito di un'altra location. [Certo per IPTC e filigrane, Probabile per le altre]
7. **Errori e link rotti**: 3 file in 404 (`shutterstock_333578129.png`, sfondo della pagina Ristorazione, che lascia una fascia vuota di circa 650 px; `anguilla-lago-fenicottero-rosa-pesca-sportiva-roma.jpg` nell'articolo sul pesce; `Villa-pollini-Lacquario-di-Chef-Alberto.jpg` nel CSS del tema figlio); la pagina Matrimoni fa 20 richieste a `test.kriesi.at`, il server dimostrativo dell'autore del tema, che finiscono in errore `ERR_TOO_MANY_REDIRECTS`; il CSS cita ancora il dominio di sviluppo `vinus.dev.netbanana.it`. L'icona Facebook in testata porta all'indirizzo "facebook.com/Enoteca-Villa-Pollini-241577372566522", diverso dalla pagina attiva facebook.com/villapollini ("Villa Pollini Weddings") [se siano la stessa pagina rinominata: DA CONFERMARE]. Gli articoli 2018-2019 indicano `esther@vinus.eu`, ma vinus.eu oggi è un dominio in vendita. Pagine interne: tutte 200 (86 URL distinti, nessun 404). [Certo]
8. **Mobile (390 px)**: viewport presente (`width=device-width, initial-scale=1, maximum-scale=1`: impedisce lo zoom), `scrollWidth` = 390 su 12 pagine su 12, nessuno scorrimento orizzontale. Ma: il popup copre la prima schermata; i tre riquadri della home diventano tre tessere da 130 px con il testo nascosto; il titolo dello slider delle Stanze esce dallo schermo ai due lati; la pagina Matrimoni è alta 21.057 px. [Certo, screenshot `_prova/attuale/*-390.png`]
9. **Testo e ricerca**: il carattere Laila mostra gli accenti gravi come acuti su tutte le pagine (ritaglio `_prova/pezzi/accenti.jpg`); H1 della home vuoto, H1 "Gallery" su Matrimoni ed Enoteca; meta description assente su 12 pagine su 12; titolo della home "Villa Pollini - Enoteca Villa Pollini" senza la parola matrimoni; 12 immagini su 13 della home senza testo alternativo; nessuna sitemap (`/sitemap.xml` e `/wp-sitemap.xml` in 404); nessun tag Open Graph né dati strutturati. Testi chiusi in immagini: locandine degli eventi, grafiche "Candle time ultimi posti disponibili" e "Il matrimonio dopo il Covid-19", didascalia del disegno della villa. [Certo]
10. **HTTPS**: attivo, `http://` e dominio senza www rimandano con 301 a `https://www.villapollini.it/`. Il certificato servito il 6/10/2026 (Let's Encrypt YR2) scade il 9/10/2026; crt.sh mostra un rinnovo emesso il 9/9/2026 non ancora installato sul server. [Certo]
11. **Dati societari**: P.IVA presente nel footer, ma sono due numeri (04167920281 e 01982980284) senza dire a quale soggetto appartengono (Vinus di Alberto Piacentini, Azienda Agricola Villa Pollini). [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | "Vinus di Alberto Piacentini - Azienda Agricola Villa Pollini" (due soggetti, abbinamento con le P.IVA [DA CONFERMARE]) | footer del sito |
| P.IVA | 04167920281 e 01982980284: cifra di controllo valida, ufficio di Padova (codice 028); su VIES risultano non abilitate alle operazioni intracomunitarie, il che non dice nulla sull'attività | footer, controllo VIES del 6/10/2026 |
| Sede | Via Cesare Pollini 2/4, 35038 Torreglia (PD), località Luvigliano; Google: Via C. Pollini, 2; Plus Code 8PR6+FC | footer, Google |
| Telefono | +39 348 416 2004 (sito, Google, articoli) | sito, Google |
| Altri recapiti | cellulare 346 8515037, fax 049 9903707, info@vinus.eu sulla scheda della Regione Veneto [vecchi, DA CONFERMARE] | venetoaroundme.regione.veneto.it |
| Email | esther@villapollini.it; esther@vinus.eu negli articoli 2018-2019 (dominio non più attivo) | sito |
| PEC | non trovata: cercare su INI-PEC (inipec.gov.it) con le due P.IVA (ricerca protetta da captcha, non fatta) | |
| Orari | non pubblicati; Google indica "Aperto 24 ore su 24" [DA CONFERMARE] | Google |
| Persone | Alberto Piacentini, titolare e chef; Esther (Esther Messina), contatto per sposi e visite [ruolo DA CONFERMARE] | sito, articolo del 28/10/2018 |
| Anni | ditta Vinus creata nel 2007; villa convenzionata per i riti civili dal 2014; "vent'anni di esperienza nel mondo dei matrimoni" (testo non datato); acquisto della villa dalla famiglia Ghedini nel 1972 [DA CONFERMARE] | articolo del 7/12/2019, pagina informazioni, matrimonio.com |
| Marchi | Villa Pollini The Real Wedding (logo attuale), Vinus (enoteca), cheFusion D'Italia & d'Amore (cucina), L'ingrediente segreto (blog) | sito |
| Riconoscimenti | badge matrimonio.com "Wedding Awards 2015" e "Consigliato 2017" (immagini sul sito); matrimonio.com 4,7/5 su 52 recensioni; Google 4,1 su 137 recensioni | sito, matrimonio.com, Google |
| Social | facebook.com/villapollini (1.846 follower), instagram.com/villapollini, YouTube @villapollinitherealwedding8056 (15 video, ultimo 17/5/2022) | sito, YouTube |
| Fatturato, dipendenti | non pubblicati | |
| Certificazioni | nessuna dichiarata | |

Omonimia da evitare: esiste una "Villa Pollini" a Cagliari (sede della Soprintendenza), che compare nei risultati di ricerca.

## URL vecchi

86 URL distinti (più gli alias `/?p=NNN` di ogni pagina e articolo). Elenco completo con destinazione proposta in `_prova/url-vecchi.tsv`, da allineare con la mappa del nuovo sito (03) e poi da trasformare in `plugin/redirect-301.csv`. [Certo]

| Gruppo | URL | Destinazione proposta |
|---|---|---|
| Pagine | `/`, `/matrimoni/`, `/matrimoni/la-villa/`, `/matrimoni/stanze/`, `/matrimoni/informazioni/`, `/matrimoni/contatti/`, `/enoteca/`, `/ristorazione/`, `/news-ed-eventi/`, `/matrimoni-in-villa/`, `/privacy-policy-informativa-sui-cookies/` | home, matrimoni, villa, appartamenti, matrimoni, contatti, vini, cucina, home, matrimoni, privacy |
| Articoli (25) | `/enoteca/<slug>/` (6), `/la-villa/<slug>/` (6), `/matrimoni-ed-eventi/<slug>/` (13) | pagina tematica più vicina (vini, cucina, villa, matrimoni) |
| Archivi | `/category/enoteca/`, `/category/la-villa/`, `/category/matrimoni-ed-eventi/` (e `/page/2/`), 28 `/tag/<slug>/` (con alcune `/page/2/`), `/author/admin/`, `/author/daniele/`, `/author/piacentini_editore/` | home o pagina tematica |
| Demo del tema (10) | `/portfolio-articoli/cam/`, `coffe-notebook`, `imac-revolution`, `ipad-iphone-freebie`, `macbook-air`, `macbook-pro-ssd`, `pill-pack`, `plant-plant`, `power-pills`, `sunglasses` | 410 (rimossi) |
| File | `/wp-content/uploads/2017/11/INVITO.pdf` | nessuno (evento del 2017) |

Il sito non ha sitemap e `robots.txt` contiene solo `User-agent: *`.

## Fonti e file di lavoro

- Crawl completo: `_prova/crawl/html/` (131 pagine HTML), testi estratti in `_prova/crawl/testi/`, API REST in `_prova/crawl/api/`, libreria media in `_prova/crawl/media/` con `media-elenco.json` ed EXIF in `media-exif.json`.
- Schede esterne: `_prova/crawl/esterne/` (Google Maps, Regione Veneto, YouTube, matrimonio.com), foto esterne in `assets/esterne/` con `manifest.json`.
- Immagini dell'azienda alla massima risoluzione: `assets/originali/` (262 file con nome parlante e id WordPress), inventario in `_prova/inventario-immagini.json`.
- Screenshot del sito attuale: `_prova/attuale/` (1440 e 390), pezzi guardati in `_prova/pezzi/`.
- Script: `_prova/script/` (crawl, estrazione testi, misure Playwright, classificazione immagini).
