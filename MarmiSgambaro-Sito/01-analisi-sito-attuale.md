# 01. Analisi del sito attuale (marmisgambaro.it)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente.
Prove: HTML di tutte le pagine in `_prova/crawl/pagine/` (355 indirizzi scaricati), API WordPress in `_prova/crawl/wpjson_*.json`, misure di Playwright in `_prova/attuale/misure.json`, screenshot a 1440 e 390 in `_prova/attuale/`, pagine demo in `_prova/attuale/prove/`, schede esterne in `_prova/crawl/esterni/` e `_prova/crawl/google/`.

## In breve

- Marmeria artigiana di San Martino di Lupari (PD) che il sito fa nascere nel 1948 dal lavoro di scultore di Andrea Sgambaro, oggi alla seconda generazione: scale, pavimenti e rivestimenti, piani cucina, bagni, caminetti, davanzali e decorazioni, arte funeraria; lavora anche pietre sinterizzate (Neolith, Lapitec) e lastre Laminam. [Certo]
- Sito WordPress **4.9.29** con tema Impreza 5.0.1, WPBakery 5.4.7 e Slider Revolution 5.4.7.2, contenuti fermi al 2018 (titolo "1948-2018 Settant'anni di garanzia di qualità", copyright 2018, logo dei 70 anni). Responsive: a 390 px non scorre in orizzontale e il menu si apre. [Certo]
- Il problema più grave è concreto e verificabile: **su tutte le pagine con il footer (344 su 354 scaricate) ogni link telefonico chiama +3211234567** (il numero di esempio del tema), l'email del footer apre **info@example.com** e l'indirizzo del footer apre su Google Maps il **Google Building 41 di Mountain View, California**. Restano pubblici 107 indirizzi di pagine demo e archivi del tema (prezzi in dollari, "Meet the Team", carrello, "Ciao mondo!") e una bozza con la scritta "TESTI DA RISCRIVERE IN QUANTO RILEVATI DA WEB". [Certo]
- Il patrimonio vero è l'archivio lavori: **75 realizzazioni descritte con materiale, finitura e spessore** (oltre 40 marmi e pietre nominati: San Pietro, Biancone e Verdello di Asiago, Silva Oro, Calacatta, Piasentina, quarziti...) e **212 foto** in galleria, più 9 foto in libreria mai mostrate (tra cui l'unica ad alta risoluzione) e una foto storica del fondatore. [Certo]
- Foto: quasi tutte da fotocamere compatte 2009-2011, ridotte a **1024 px** (verticali a 576 px) prima del caricamento. Si possono mostrare fino a circa 1000 px su schermo normale, 500 px su retina. **Una sola foto ad alta risoluzione** (villa con doppia scala esterna, 4320x3240) può aprire una pagina a tutta larghezza. Nessuna foto recente del laboratorio, della sede o delle persone. [Certo]
- Identità esistente: rosso **#C4161C** (logo e barra in alto), nero caldo #231F20 e grigio #6D6E71 del logo, monogramma "MS". Il logo esiste solo come PNG 331x92 nella versione dei 70 anni; il vettoriale va chiesto. [Certo]

## Pagine esistenti

Menu principale (uguale a 1440 e a 390): Home, Chi Siamo, Realizzazioni, Lavorazioni, Contatti. In alto una barra rossa con telefono, email e Facebook. [Certo]

| Pagina | URL | Stato |
|---|---|---|
| Home | `/` | slider di 5 foto con titoli in HTML, 4 blocchi (Consulenza, Realizzazione, Posa, Ripristino), invito al contatto, 6 "Recenti realizzazioni", fascia rosso scuro "1948-2018" con 4 contatori, loghi Neolith, Lapitec, Laminam. Nessun H1. Ultima modifica 27/06/2018 |
| Chi Siamo | `/pages/chi-siamo/` | storia in 6 righe con foto d'epoca del fondatore, contatori, testi Partner, Studio tecnico, Produzione (elenco di 12 voci), Sistema produttivo, Posa in opera e trattamenti. Modifica 26/06/2018 |
| Realizzazioni | `/marmi-sgambaro-lavorazione-marmi-e-pietre-da-arredamento-realizzazione-scale-in-marmo-e-rivestimenti-in-pietra-naturale/` | griglia di 75 lavori con 11 filtri (Tutto + 10 categorie). URL di 124 caratteri. Modifica 11/05/2018 |
| Schede realizzazione | `/portfolio/<slug>/` (75) | galleria di 1-9 foto con ingrandimento, "Descrizione" (materiale, finitura, spessore), "Progetti simili" |
| Categorie realizzazioni | `/portfolio_category/<categoria>/` (10) | Bagni, Caminetti, Cancelli e recinzioni, Davanzali soglie e decorazioni, Pavimenti e rivestimenti esterni, Pavimenti e rivestimenti interni, Piani cucina, Scale esterne, Scale interne, Soggetti funebri e lapidi (`lapidi`). Titolo della pagina "Categorie portfolio: ..." |
| Lavorazioni | `/pages/services/` | testo sui materiali e sulle finiture, sezioni "Lavorazione pietre sinterizzate" (Neolith, Lapitec) e "Lavorazione lastre ceramica" (Laminam). Tre H1. Modifica 26/06/2018 |
| Contatti | `/pages/contact/` (anche `/contact/`) | mappa Google, indirizzo, telefono, email, modulo Nome/Email/Messaggio con casella privacy. Unica pagina toccata dopo il 2018: 12/02/2024 |
| Lapidi | `/portfolio/lapidi-2/` | scheda nella categoria lapidi con un testo proprio "Realizzazione lapidi" e 1 foto |
| Bozza "Vendita" | `/pages/vendita/` | pubblica: copia di Chi Siamo con il titolo "TESTI DA RISCRIVERE IN QUANTO RILEVATI DA WEB", una linea del tempo 1948-2017 con testo lorem ipsum e segnaposto del tema |
| Copia della Home | `/sample-page-2-2/` | pubblica: versione precedente della home con il blocco "Detrazioni 50%" e "View Full Portfolio" |
| Demo del tema e archivi | 107 URL | `/pages/pricing/` (Free $0, Standard $20, Business $45, Professional $80 per month), `/pages/team/` "Meet the Team", `/shop/`, `/cart/`, `/checkout/`, `/my-account/`, `/elements/...` (25 pagine di componenti), blog demo in inglese del 2013, `/ciao-mondo/`, `/hello-world/`, `/wordpress-tutorial-german-with-impreza/`, `/events/` (calendario eventi vuoto) |

Nessuna sitemap (`/sitemap.xml` e `/wp-sitemap.xml` rispondono 404), nessuna versione in altre lingue, nessun PDF o catalogo scaricabile. [Certo]

## Testi reali (verbatim, con i refusi originali)

Testi completi pagina per pagina in `_prova/crawl/testi/*.txt`. Qui quelli che servono al nuovo sito. Le parole tra virgolette sono dell'azienda: "passione", "missione", "innovativi" e "rivoluzionaria" compaiono nei loro testi e **non vanno riportate** nel nuovo sito (parole da evitare in `build.py`).

Home (slider, 5 slide con titolo in due righe e pulsante "CONTATTACI"):
1. "Rivestimenti e pavimentazioni / in marmo e pietra naturale per esterni"
2. "Scale per esterni / in pietra sinterizzata, marmo, granito e pietra naturale"
3. "Scale interne / tradizionali ed elicoidali in gres, marmo, granito e pietra naturale"
4. "Allestimento bagni / in pietra sinterizzata, gres, marmo, granito e pietra naturale"
5. "Piani per cucine / in gres, pietra sinterizzata, marmo, granito e agglomerati"

Home (quattro blocchi con icona):
6. Consulenza: "Il nostro supporto inizia dalla fase di scelta delle soluzioni e dei materiali. Vi affidiamo a validi e creativi partner che vi guideranno alla soluzione più adeguata all'ambiente da allestire."
7. Realizzazione: "Realizziamo pavimenti, scale, bagni, cucine e rivestimenti interni ed esterni in materiali naturali tecnologici: Marmo, Gres, Cotto, Parquet, Mosaico, Ceramica e Lapitech."
8. Posa: "Ci affidiamo a validi professionisti per la posa dei vostri pavimenti, scale e rivestimenti Interni ed Esterni in Marmo, Gres, Cotto, Parquet, Mosaico, Ceramica"
9. Ripristino: "Restauro e ripristino di pavimenti, scale e strutture in marmo e pietra. Pulizia di davanzali e stipiti utilizzando i più recenti prodotti dedicati alla manutenzione."
10. Invito: "Contattaci per richiedere informazioni o preventivi / +049.9461675 / info@marmisgambaro.it / Contattaci"; poi "Recenti realizzazioni" e il pulsante "Archivio realizzazioni".
11. Fascia rossa: "1948-2018 / Settant'anni di garanzia di qualità" con i contatori "+70 anni di attività", "+200 tipologie di materiali", "+2000 clienti soddisfatti", "+50 partner coinvolti" (valori nel codice: `data-target` 70, 200, 2000, 50; senza JavaScript si legge "+0").
12. Testata (nel codice, non visibile a 1440): "Lavorazione marmi e pietre naturali per l'arredamento".

Chi Siamo:
13. "Nata nel 1948 dalla passione per la scultura di SGAMBARO ANDREA. / Oggi gestita dalla seconda generazione, la MARMI SGAMBARO vanta un´esperienza di oltre 60 anni."
14. "L´azienda si è sviluppata matendendo le caratteristiche di laboratorio artigianale: l´incessante ricerca di nuovi materiali direttamente alla fonte ed il controllo della lavorazione durante le fasi del ciclo produttivo, consentono alla MARMI SGAMBARO di essere riconosciuta ed apprezzata dai propri clienti." (lo stesso testo è nel footer di ogni pagina sotto "Azienda")
15. "Marmi Sgambaro è attualmente apprezzata nell'arredamento per interni e nell'arte funeraria. / Nell'arredamento per interni oltre a realizzare piani per cucine e top per bagni, è specializzata nel ripristino di pavimenti, realizzando rivestimenti su misura con relativa posa. / Nell'arte funeraria vengono realizzati loculi e monumenti a terreno."
16. PARTNER: "Collaboriamo con numerosi professionisti del settore quali geometri, architetti, ingegneri, designer e arredatori, sviluppando assieme numerosi progetti di abitazioni, arredo urbano, strutture commerciali ed hotels sia in Italia che all'estero. Seguiamo interamente i progetti dai rivestimenti, facciate esterne, pavimenti e rivestimenti interni, creazione componenti di arredo quali colonne, balaustre, lavelli a massello ed oggetti artistici e decorativi." Segue: "La nostra missione è sviluppare ed approfondire le collaborazioni con professionisti, mettendo a disposizione la nostra decennale esperienza ed il nostro studio tecnico."
17. STUDIO TECNICO: "La nostra decennale esperienza / I nostri tecnici potranno sviluppare e trasformare qualsiasi tipo di progetto in PDF o DWG con i più recenti sistemi di disegno AUTOCAD," (frase tronca; nella bozza "Vendita": "AUTOCAD E RINOCEROS")
18. PRODUZIONE: "Sviluppiamo e realizziamo per ingegneri, architetti, designer e geometri,i loro progetti per abitazioni private, arredo urbano, strutture commerciali ed hotels, come:" seguito da 12 voci: pavimenti, rivestimenti, bagni, "pareti in marmo e pareti pietra", scale, rivestimenti caminetti, "rivestimenti camini moderni", "mattonelle per bagno", rivestimenti per esterni e per interni, "creazione di colonne in marmo e colonne in pietra", "lavelli a massello ed oggetti artistici e decorativi".
19. SISTEMA PRODUTTIVO: "Nel nostro laboratorio disponiamo del ciclo completo di lavorazione interno con il supporto di macchinari di ultima generazione quali contornartici, sagomatrici automatiche e controlli numerici per soddisfare in maniera rapida anche le richieste più particolari. / Questa scelta impegnativa ci consente oggi di poter gestire qualsiasi lavoro o progetto in maniera completamente autonoma garantendo perciò un severo controllo su tutte le fasi di lavorazione."
20. POSA IN OPERA E TRATTAMENTI: "La decennale esperienza dei posatori che collaborano a stretto contatto con la nostra azienda potrà garantirvi un servizio di posa in opera puntuale ed ad alto tasso tecnico per qualsiasi tipo di lavoro in Italia ed all'estero accompagnato da un servizio di trattamento con il supporto del nostro partner FILA" e l'elenco "pavimenti e rivestimenti su progetto anche di grandi dimensioni / scale normali e su sagoma a massello / pavimenti sopraelevati / rivestimenti ventilati".

Attenzione: la bozza pubblica `/pages/vendita/` contiene gli stessi testi 16-20 sotto il titolo **"TESTI DA RISCRIVERE IN QUANTO RILEVATI DA WEB"**. L'azienda stessa dichiara che quei paragrafi sono presi da altri siti: nel nuovo sito si usano i fatti (studio tecnico, CNC, posatori, FILA, pavimenti sopraelevati, facciate ventilate), non le frasi. Dalla stessa bozza viene una frase propria: "Nasce dalla passione per la scultura di Andrea Sgambaro l'attuale azienda che dopo 70 anni continua l'attività con soluzione artigianali, basate sulla lavorazione manuale, seppur coadiuvata di impianti CNC e lavorazioni di precisione." [Certo]

Lavorazioni:
21. "La nostra azienda si occupa della fornitura e trasformazione di marmi, pietre, graniti ed agglomerati (quarzi/resina). / Il nostro lavoro è rivolto ad arredatori, architetti, designer, privati ed imprese edili."
22. "Ci occupiamo della realizzazione di scale, pavimenti, piani cucina, top bagno, rivestimenti esterni ed interni, davanzali, portali per abitazioni private e attività in genere. / Grazie all'esperienza maturata in diversi anni di attività, effettuaiamo anche opere pubbliche in genere."
23. "Realizziamo soluzioni personalizzate e seguiamo il cliente nella fasi della realizzazione (progettazione, disegni, rilievi), nel trasporto e nella posa in opera di quanto prodotto avvalendoci di personale altamente qualificato."
24. "La nostra missione è soddisfare le necessità del cliente, dando dei consigli sull'uso e la manutenzione dei materiali scelti. Tutti i nostri prodotti sono pezzi unici, realizzati su misura in base ai singoli desideri."
25. "Sulle lastre di marmo è possibile eseguire varie lavorazioni al fine di esaltarne la qualità e la naturalezza del marmo: sabbiatura / spazzolatura / levigatura / lucidatura / rullatura / bocciardatura"
26. Lavorazione pietre sinterizzate: "La continua ricerca di soluzioni e prodotti innovativi, ci ha permesso di specializzarsi nella lavorazione dei nuovi materiali e pietre sinterizzate: Neolith® e Lapitech®." Poi due descrizioni di prodotto riprese dai produttori (Neolith "categoria di prodotto nuova e rivoluzionaria composta al 100% con elementi naturali..."; "Lapitec® è una pietra naturale sinterizzata a 1200°C, prodotta a "tutta massa" in lastre mediante una tecnologia esclusiva brevettata.") e: "La lavorazione delle pietre sinterizzate necessita di una notevole conoscenza del prodotto e delle tecniche di lavorazione estremante accurate e precise. / Effettuiamo queste lavorazione per conto di rivenditori ed installatori di pavimenti e rivestimenti realizzando qualsiasi articolo o rivestimento realizzabile con la pietra sinterizzata."
27. Lavorazione lastre ceramica: "Laminam è la rivoluzionaria lastra ceramica Made in Italy: 1620x3240mm di puro grès porcellanato compattati in uno spessore di 12mm. Ideale per il top della cucina, è un "tagliere" su cui lavorare gli alimenti utilizzando lame, liquidi, olio, vino e pentole roventi. Tutto questo senza rinunciare all'estetica ricercata disponibile in oltre 40 finiture, per creare ambienti di forte personalità." (testo del produttore: dati tecnici da ricontrollare sul catalogo Laminam attuale)

Contatti:
28. "Informazioni / Via Leonardo Da Vinci, 36 - 35018 San Martino di Lupari - PD / +39.049.9461675 / info@marmisgambaro.it"
29. "Contattaci / Per richiedere informazioni sui nostri prodotti e lavorazioni o per richiedere un preventivo, compilate il modulo sottostante oppure contattateci ai recapiti riportati a lato." Campi: "Nome", "Email *", "Messaggio *", casella "Accetta la Privacy Policy", pulsante "Invia messaggio".

Footer (tutte le pagine):
30. "Contatti / info@marmisgambaro.it / Tel. +39.049.9461675 / Fax +39.049.5952371 / Via Leonardo Da Vinci, 36 - 35018 San Martino di Lupari - PD", icona Facebook, "© 2018 Marmi Sgambaro Srl by et.ics", "Privacy Policy", "Cookie Policy".

Lapidi (`/portfolio/lapidi-2/`):
31. "Realizzazione lapidi / L'azienda MARMI SGAMBARO SRL ha una lunga esperienza nella realizzazione di lapidi, loculi, tombe, cappelline gentilizie con rivestimenti di marmo, granito e pietra. / Siamo in grado di fornire diversi modelli, di varie dimensioni e colorazioni, soddisfacendo le richieste più particolari dei clienti. Su richiesta vengono fatti disegni tecnici e prospetti grafici in modo da visualizzare il lavoro finito. / Come tutti i nostri articoli di arte funeraria, anche le lapidi possono essere personalizzate con incisioni e immagini sacre. / Il tutto viene realizzato con grande cura, operiamo con competenza e professionalità, forti della solida esperienza maturata nel settore."

Fuori dal sito, scheda PagineBianche "Azienda verificata" (testo dell'azienda o scritto per lei da Italiaonline):
32. "Marmi Sgambaro è una storica azienda che fin dal lontanissimo 1948 opera nel settore della lavorazione di marmi italiani e materiali affini per la realizzazione di rivestimenti per l'edilizia, elementi per l'arredamento di interni, e manufatti di arte funeraria. [...] Si occupa di ripristino di pavimenti con soluzioni su misura, top in marmo per bagno e cucina, pavimentazioni civili di interni ed esterni, loculi e monumenti funebri a terreno, rivestimenti, vasche in marmo, e lavorazione anche su misura di marmo bianco di Carrara, pietra bianca, ardesia e calcare per l'edilizia, marmo leggero, e marmo statuario Il Sabato mattina si riceve previo appuntamento."

Realizzazioni: titolo e descrizione di ogni scheda, verbatim (tra parentesi quadre il numero di foto in galleria):

*Scale interne* (18):

- "Scala interna in marmo San Pietro lucido": "Scala interna in marmo San Pietro lucido spessore 8 cm" [6 foto]
- "Scala interna in marmo San Pietro anticato": "Scala interna in marmo San Pietro anticato di spessore 3 cm con pedata e alzata al dritto e lavorazione a 45°. Pavimento in marmo San Pietro anticato spessore 2 cm formato 30 cm a correre. Rivestimento in Quarzite a spacco Giza white." [2 foto]
- "Scala in marmo bianco Namibia": "Scala in marmo bianco Namibia spessore 2 cm" [2 foto]
- "Scala in aglomarmo" [2 foto] (nessuna descrizione)
- "Scala interna in marmo Malaga anticato": "Scala interna in marmo Malaga anticato spessore 4 cm con toro tondo, alzata con gola, fianchetti sagomati e battiscopa a scivolo" [3 foto]
- "Scala interna in marmo rosa-beige lucido": "Scala interna in marmo rosa-beige lucido spessore 4 cm con toro tondo, alzata con gola, fianchetti sagomati e battiscopa a scivolo. Pavimento in marmo rosa-beige lucido spessore 2 cm formato 30 cm a correre." [2 foto]
- "Scala interna in marmo verdello di Asiago anticata": "Scala interna in marmo verdello, anticato, martellinato a mano con lavorazione per effetto finta usura. Spessore 4 cm ed alzata da 3 cm." [2 foto]
- "Scala interna in marmo Biancone anticato": "Scala interna in marmo Biancone anticato di spessore 4 cm con toro tondo, alzata da 3 cm con gola, fianchetto sagomato e battiscopa a scivolo." [2 foto]
- "Scala interna in marmo biancone": "Scala interna, con estensione del primo gradino e caminetto in marmo biancone lucido spessore 4 cm, toro tondo, alzata con gola, fianchetto sagomato e battiscopa a scivolo. Caminetto" [3 foto]
- "Scala interna in marmo biancone levigata a mano": "Scala interna in marmo biancone levigata a mano spessore 4 cm, toro tondo, alzata con gola, fianchetto sagomato e battiscopa a scivolo." [3 foto]
- "Scala interna in pietra Piasentina anticata": "Scala interna in pietra Piasentina anticata spessore 3 cm." [6 foto]
- "Scala interna in marmo San Pietro levigato": "Scala interna in marmo San Pietro levigato, spessore 3 cm pedata e alzata al dritto, battiscopa e fianchi." [3 foto]
- "Scala interna in marmo Silva Oro giallo lucido": "Scala interna in marmo Silva Oro giallo lucido, spessore 4 cm con toro tondo e alzate sagomate con gola" [3 foto]
- "Scala interna in marmo Beige Atlantide lucido": "Scala interna in marmo Beige Atlantide lucido, spessore 4 cm con toro tondo e alzata liscia" [6 foto]
- "Scala interna in marmo Bianco Lasa lucido": "Scala interna in marmo Bianco Lasa lucido, spessore 4 cm con toro tondo e alzata sagomata con gola e battiscopa a scivolo" [3 foto]
- "Scala interna in marmo Biancone lucido": "Scala interna in marmo Biancone lucido, spessore 4 cm con toro tondo e alzata dritta" [3 foto]
- "Scala interna elicoidale in marmo Silva Oro Giallo lucido": "Scala interna elicoidale in marmo Silva Oro Giallo lucido, spessore 4 cm con toro tondo e alzata" [3 foto]
- "Scala monumentale interna in marmo Calacata lucido": "Scala monumentale interna in marmo Calacata lucido, spessore 6 cm con toro tondo e alzata sagomata con gola. Balaustre tornite e corrimano sagomato con sigle intarsiate in marmo Rosso Francia." [9 foto]

*Scale esterne* (3):

- "Scala esterna in marmo Crema Nova": "Scala esterna in marmo Crema Nova rullato e anticato spessore 6 cm pedata e alzata al dritto. Fioraia in marmo San Pietro levigato." [2 foto]
- "Scala esterna in marmo San Pietro": "Scala esterna in marmo San Pietro rullato spessore 5 cm con toro tondo, battiscopa e corrimano in marmo Silva Oro anticato." [3 foto]
- "Scala esterna in quarzite Gaia Dark Mix fiammata e spazzolata": "Scala esterna in quarzite Gaia Dark Mix fiammata e spazzolata, spessore 2 cm con pedata e alzata al dritto." [3 foto]

*Pavimenti e rivestimenti interni* (5):

- "Pavimento interno in marmo Rosal": "Pavimento interno in marmo Rosal di spessore 2 cm e formato 60×30 cm" [1 foto]
- "Pavimento interno in marmo San Pietro": "Pavimento interno in marmo San Pietro spessore 2 cm e formato 80×40 cm" [1 foto]
- "Pavimento interno in marmo Crema nova": "Pavimento interno in marmo Crema nova rullato e spazzolato in spessore 2 cm e multiformato" [2 foto]
- "Pavimento interno in marmo San Pietro e tozzetti in granito Azul Macaubas": "Pavimento interno in marmo San Pietro e tozzetti in granito Azul Macaubas. Spessore 2 cm." [3 foto]
- "Rivestimento interno in quarzite a spacco Giza White" [1 foto]

*Pavimenti e rivestimenti esterni* (16):

- "Pavimento e scala esterna": "Pavimento esterno in pietra di Prun Bianca anticata e scale esterne in marmo Verdello/Chiarofonte di Asiago anticato." [6 foto]
- "Pavimento esterno in marmo Travertino Navona": "Pavimento esterno in marmo Travertino Navona levigato e colonne in pietra di Vicenza levigata" [6 foto]
- "Pavimento in pietra" [1 foto]
- "Pavimento in travertino Navona anticato": "Pavimento in travertino Navona anticato, zoccolatura in marmo San Pietro levigato" [1 foto]
- "Pavimento esterno in porfido e Rustic Green (Grigio Olivo)": "Pavimento esterno in porfido a cubetti e Rustic Green (Grigio Olivo) fiammato e spazzolato." [2 foto]
- "Pavimento esterno in marmo Verdello e Rosso di Asiago": "Pavimento esterno in marmo Verdello e Rosso di Asiago rullato." [3 foto]
- "Basamento colonna in marmo Malaga levigato" [1 foto]
- "Pavimento esterno in quarzite Vintage Gold": "Pavimento esterno in quarzite Vintage Gold a spacco naturale e burattata spessore 2 cm" [9 foto]
- "Pavimento rivestimento parete, fioraia e ripiano di appoggio": "Pavimento in quarzite a spacco Lime Gray spessore 2 cm. Rivestimento parete, fioraia e ripiano di appoggio in marmo San Pietro levigato." [6 foto]
- "Pavimento esterno in marmo Crema Nova": "Pavimento esterno in marmo Crema Nova rullato e anticato spessore 2 cm in multiformato." [9 foto]
- "Pavimento e rivestimento esterno": "Pavimento esterno in marmo Giallo Istria multiformato lavorato con bocciardatura, carteggiatura e rullatura, spessore 2 cm. Rivestimento in marmo San Pietro spessore 2 cm." [6 foto]
- "Rivestimento esterno in quarzite Giza Yellow": "Rivestimento esterno in quarzite Giza Yellow a spacco naturale con spessore irregolare." [3 foto]
- "Pavimento esterno in porfido del Trentino": "Pavimento esterno in porfido del Trentino a spacco con formato a mattoncino" [1 foto]
- "Rivestimento in pietra e marmo": "Rivestimento in pietra e marmo in formato naturale a spacco e martellinato a mano. Colonnine e coprimuretti sagomati in marmo Silva Oro levigato." [3 foto]
- "Pavimento eterno in Quarzite Gaia Dark Mix fiammata": "Pavimento eterno in Quarzite Gaia Dark Mix fiammata, spessore 2 cm formato 30 cm a correre." [9 foto]
- "Portale e contorni finestre in marmo Verdello di Asiago bocciardato" [1 foto]

*Piani cucina* (6):

- "Piano cucina e lavello in marmo": "Piano cucina e lavello in marmo verdello di Asiago bocciardato e invecchiato. Lavorazioni, finiture e decorazioni effettuate a mano." [3 foto]
- "Piano cucina e rivestimento in marmo Trani": "Piano cucina in marmo Trani lucido spessore 4 cm, rivestimento in marmo Trani da 10×10 cm burattato" [3 foto]
- "Piano cucina in marmo Giallo Silva Oro": "Piano cucina in marmo Giallo Silva Oro anticato con lavabo spessore 20 cm" [3 foto]
- "Piano cucina in granito": "Piano cucina in granito spessore 3 cm lucido" [3 foto]
- "Tavolo in marmo Rosso di Asiago": "Tavolo in marmo Rosso di Asiago anticato con bordo esterno bocciardato e anticato." [3 foto]
- "Piano cucina in marmo Giallo Reale": "Piano cucina in marmo Giallo Reale spessore 4 cm anticato. Lavabo a massello sagomato spessore 20 cm" [3 foto]

*Bagni* (8):

- "Piano per mobile da bagno, rivestimenti e pavimenti": "Piano per mobile da bagno, rivestimenti e pavimenti in marmo biancone di Asiago anticato e spazzolato con inserto in marmo rosso di asiago" [3 foto]
- "Lavello a ciotola, piano mobile da bagno e rivestimento": "Lavello a ciotola e piano mobile da bagno in marmo giallo Silva Oro anticato. Rivestimento in marmo calacatta lucido." [1 foto]
- "Lavello e piano in marmo": "Lavello e piano in marmo Verdello di Asiago ricavato da unico massello di spessore 25 cm martellinato ed invecchiato a mano. Rivestimento ricavato da lastra dello stesso marmo di spessore 3 cm martellinata ed invecchiata." [2 foto]
- "Rivestimento bagno in travertino": "Rivestimento bagno in travertino di spessore 1 cm, formato 60x30cm, spazzolato ed anticato" [3 foto]
- "Rivestimento e pavimento bagno": "Rivestimento bagno in travertino Navona di spessore 2cm, formato 30 cm a correre, anticato, spazzolato e stuccato a resina bianca. Pavimento in marmo San Pietro, spessore 2cm, formato 30 cm a correre, anticato e spazzolato." [1 foto]
- "Rivestimento bagno in ardesia nera italiana": "Rivestimento bagno in ardesia nera italiana a spacco naturale spessore 1cm, formato 60x15cm" [3 foto]
- "Lavello e rivestimento bagno": "Lavello in marmo rosal levigato ricavato da unico massello, altezza 86 cm e diametro 52 cm. Rivestimento in marmo grigio ash spessore 4cm a lastra unica." [3 foto]
- "Piano per mobile da bagno in marmo": "Piano per mobile da bagno in marmo biancone spessore 4 cm spazzolato e anticato" [2 foto]

*Caminetti* (10):

- "Caminetto in marmo verdello di Asiago massello martellinato a mano e invecchiato" [2 foto]
- "Rivestimento caminetto in marmo Biancone anticato" [2 foto]
- "Rivestimento caminetto e basamento": "Rivestimento caminetto e basamento in marmo Biancone lucido" [1 foto]
- "Rivestimento caminetto in quarzite grigia": "Rivestimento caminetto in quarzite grigia Gaia Gray" [3 foto]
- "Rivestimento caminetto in marmo Rosal": "Rivestimento caminetto in marmo Rosal lucido" [1 foto]
- "Cornice per caminetto in marmo bianco di Carrara" [1 foto]
- "Basamento per stufa in marmo moleanos lucido" [2 foto]
- "Caminetto  in marmo calacatta lucido": "Caminetto in marmo calacatta lucido" [3 foto]
- "Rivestimento per caminetto in marmo giallo Silva Oro lucido" [1 foto]
- "Rivestimento caminetto in marmo calacatta lucido" [1 foto]

*Davanzali, soglie e decorazioni* (6):

- "Fioraia in pietra di Prun scalpellata a mano" [2 foto]
- "Contorno finestra in marmo Silva Oro levigato" [1 foto]
- "Stemma di famiglia su pietra Orsera levigata" [2 foto]
- "Contorno finestra in marmo Silva Oro levigato" [1 foto]
- "Davanzale sagomato in marmo San Pietro levigato" [3 foto]
- "Cornice in marmo Biancone di Asiago" [1 foto] (nessuna descrizione)

*Cancelli e recinzioni* (2):

- "Rivestimento in marmo Trani carteggiato." [3 foto]
- "Inserti cancello e rivestimenti": "Inserti cancello e rivestimenti in granito nero fiammato" [2 foto]

*Soggetti funebri e lapidi* (1):

- "Lapidi" [1 foto] (nessuna descrizione)


Refusi e incoerenze da non riportare: "matendendo", "un´esperienza", "L´azienda" e "l´incessante" (accento acuto al posto dell'apostrofo), "effettuaiamo", "nella fasi", "ci ha permesso di specializzarsi", "estremante", "queste lavorazione", "contornartici" (contornatrici), "geometri,i loro", "pareti pietra", "ed ad alto tasso tecnico", "soluzione artigianali", frase "AUTOCAD," lasciata a metà, "Lapitech" accanto a "Lapitec®", "Calacata" accanto a "calacatta", "aglomarmo", "Pavimento eterno", "Caminetto  in" (doppio spazio), "moleanos" e "rosal" minuscoli, telefono scritto "+049.9461675". Gli anni non tornano: "oltre 60 anni" in Chi Siamo, "+70" nei contatori, "Settant'anni" nel titolo; dal 1948 a oggi sono 78. Il nuovo sito scrive "dal 1948", mai un numero di anni che invecchia. Il nome compare come MARMI SGAMBARO, Marmi Sgambaro Srl, MARMI SGAMBARO SRL: nel nuovo sito **Marmi Sgambaro S.r.l.** (forma del Registro Imprese). Negli estratti sopra gli apostrofi tipografici (’) sono resi con quello semplice; gli accenti acuti (´) sono quelli dell'originale.

## Cosa fanno o vendono

Laboratorio di trasformazione con posa, non rivendita di lastre: "fornitura e trasformazione di marmi, pietre, graniti ed agglomerati (quarzi/resina)". [Certo]

| Ambito | Cosa (dalle loro pagine) | Fonte |
|---|---|---|
| Scale | interne ed esterne, "tradizionali ed elicoidali", a sbalzo, monumentali con balaustre tornite, "scale normali e su sagoma a massello"; 18 schede di scale interne e 4 di scale esterne | Home, Chi Siamo, Realizzazioni [Certo] |
| Pavimenti e rivestimenti | interni ed esterni, multiformato, "a correre", tozzetti, facciate, "pavimenti sopraelevati", "rivestimenti ventilati", ripristino e restauro di pavimenti esistenti | Chi Siamo, Home, Realizzazioni [Certo] |
| Cucine e bagni | piani cucina, lavelli e lavabi ricavati da un unico massello (fino a 25 cm di spessore), top bagno, rivestimenti, vasche in marmo | Lavorazioni, Realizzazioni, PagineBianche [Certo] |
| Caminetti | cornici e rivestimenti di caminetti, basamenti per stufe (10 schede) | Realizzazioni [Certo] |
| Davanzali e decorazioni | davanzali sagomati, contorni finestra, portali, cornici, fioriere scalpellate a mano, colonne, stemmi di famiglia scolpiti, tavoli | Realizzazioni, Chi Siamo [Certo] |
| Cancelli e recinzioni | inserti per cancelli, rivestimenti di muri e colonnine | Realizzazioni [Certo] |
| Arte funeraria | lapidi, loculi, tombe, "cappelline gentilizie", "monumenti a terreno", incisioni e immagini sacre, disegni e prospetti su richiesta | Chi Siamo, scheda Lapidi [Certo] |
| Superfici tecniche | lavorazione di pietre sinterizzate **Neolith** e **Lapitec** (anche per conto di rivenditori e posatori) e lastre ceramiche **Laminam** | Lavorazioni, loghi in Home [Certo]. Rapporto commerciale con i tre marchi [DA CONFERMARE] |
| Servizi | consulenza sui materiali, studio tecnico (disegni PDF e DWG con AutoCAD), rilievi, produzione interna con contornatrici, sagomatrici automatiche e controlli numerici (CNC), trasporto, posa con posatori di fiducia, trattamenti con il partner **FILA**, consigli su uso e manutenzione, pulizia di davanzali e stipiti | Chi Siamo, Lavorazioni, Home [Certo] |
| Finiture | sabbiatura, spazzolatura, levigatura, lucidatura, rullatura, bocciardatura; nelle schede anche anticatura, martellinatura a mano, fiammatura, burattatura, carteggiatura, spacco naturale, "effetto finta usura" | Lavorazioni, Realizzazioni [Certo] |

Clienti dichiarati: "arredatori, architetti, designer, privati ed imprese edili", geometri e ingegneri, rivenditori e installatori; "opere pubbliche in genere"; progetti "sia in Italia che all'estero" (nessun esempio estero nominato) [Certo per la dichiarazione, opere e lavori all'estero DA CONFERMARE].

Materiali nominati nelle 75 schede (utili per filtri e testi): marmi San Pietro, Biancone e Biancone di Asiago, Verdello di Asiago, Rosso di Asiago, Chiarofonte di Asiago, Silva Oro (giallo), Crema Nova, Travertino Navona, Trani, Rosal, Malaga, Bianco Lasa, Calacatta, Beige Atlantide, rosa-beige, bianco Namibia, Giallo Reale, Giallo Istria, Moleanos, bianco di Carrara, Rosso Francia (intarsi), rosa Portogallo, grigio ash; pietre di Prun (bianca), di Vicenza, Piasentina, Orsera; quarziti Giza White, Giza Yellow, Gaia Dark Mix, Gaia Gray, Vintage Gold, Lime Gray; porfido (anche del Trentino), Rustic Green (Grigio Olivo), graniti (Azul Macaubas, nero fiammato), ardesia nera italiana, agglomarmo. [Certo]

Numeri dichiarati dall'azienda sul sito (non verificabili): "+200 tipologie di materiali", "+2000 clienti soddisfatti", "+50 partner coinvolti". Nel nuovo sito solo se il cliente li conferma. [DA CONFERMARE]

## Immagini usate oggi

Scaricate tutte alla risoluzione più alta esistente sul server (originale senza `-WxH`, controllato anche `srcset`, sfondi CSS e la libreria media dell'API): **247 file in `assets/originali/`** con `manifest.json` (URL di origine, pagine in cui compaiono). Più 13 file da portali in `assets/esterne/` con il loro `manifest.json`. Inventario completo con soggetto, qualità e larghezza massima in `_prova/inventario-immagini.json`; provini numerati in `_prova/provini/`. [Certo]

| Tipo | Quantità | Dimensioni | Giudizio sulla risoluzione | Uso nel nuovo sito |
|---|---|---|---|---|
| Foto delle 75 realizzazioni (gallerie) | 212 | 1024x768 o 1024x683 (orizzontali), 576x768 e 768x1024 (verticali) | Fotocamere compatte Casio, Ricoh e Canon degli anni 2009-2011, ritocco Photoshop CS6, ridotte a 1024 px prima del caricamento: non esiste sul server un originale più grande. Nitide fino a circa 900-1000 px su schermo normale, circa 500 px su retina. Luce spesso piatta, qualche dominante, oggetti di casa in vista. JPEG pesanti: in media 374 KB, fino a 1,1 MB per una foto da 1024 px | schede lavoro, griglie a 2-3 colonne, blocchi a mezza pagina. Mai a tutta larghezza |
| Foto in libreria non mostrate | 9 (+6 versioni del 2014 e 4 vecchie slide) | da 576 a **4320x3240** | Una sola foto ad alta risoluzione: `media-non-usata-cimg0567.jpg`, villa con doppia scala esterna curva (stessa serie della scheda "Scala esterna in marmo San Pietro"), regge fino a circa 3900 px | **apertura a tutta larghezza** della Home o di Scale esterne |
| Slide della home | 5 (+4 vecchie) | 1600x668 | Ritagli ingranditi da foto compatte: morbidi e rumorosi al 100% (`_prova/esame/hero1-crop100.jpg`); una mostra flaconi e oggetti personali | al massimo 1000 px, meglio non usarle |
| Foto storica, probabilmente del fondatore (senza didascalia) [Probabile] | 1 | 800x878 | Riproduzione di una stampa d'epoca in bianco e nero, grana visibile; fino a circa 600 px | pagina Azienda, storia dal 1948 |
| Copertine in griglia | 4 | 1024 | come le foto delle gallerie | copertine |
| Logo | 1 | PNG 331x92 | versione celebrativa "70°" con payoff "1948-2018 settant'anni di garanzia di qualità" in immagine, illeggibile a mobile (mostrato a 72x20 px) | solo riferimento: **chiedere il vettoriale** del monogramma "MS" |
| Favicon | 1 | 32x29 | monogramma MS rosso | riferimento |
| Logo storico "MS Marmi Sgambaro" (PagineBianche) | 2 | 250 e 400 px | riquadro rosso con monogramma e scritta in corsivo | riferimento per l'identità |
| Loghi Neolith, Lapitec, Laminam | 3 | 600x176, 600x75 | buoni | striscia dei materiali lavorati |
| Texture marmo nero venato (sfondo footer) | 1 | 1600x668 | nitida, ma non è un lavoro dell'azienda: origine sconosciuta | non usarla come prova di lavoro [DA CONFERMARE origine] |
| Foto su Google Business (proprietario, 10/07/2018) | 4 | ritagli quadrati 434-589 px | doppioni più piccoli di foto del sito | nessuno |
| Foto su PagineBianche | 7 | ritagli quadrati 400-596 px | doppioni | nessuno |

Le foto più forti per il nuovo sito (file in `assets/originali/`, larghezza massima su schermo normale):
- villa con doppia scala esterna curva: `media-non-usata-cimg0567.jpg` (3900 px, l'unica per un'apertura piena);
- scala elicoidale in Silva Oro vista dall'alto: `realizzazione-scala-interna-elicoidale-...-01.jpg` (1000 px), e la gemella in Beige Atlantide (`...beige-atlantide...-04.jpg`);
- scala monumentale in Calacatta con balaustre tornite: 9 foto `realizzazione-scala-monumentale-...-01..09.jpg`, tra cui **la fresa a ponte che taglia i gradini curvi** (`-09`) e i gradini finiti nel laboratorio (`-08`): le uniche foto del laboratorio;
- fondatore al lavoro su un bassorilievo: `sito-chi-siamo-001.jpg` (600 px);
- cantiere: colonne in pietra di Vicenza sollevate con la gru (`realizzazione-pavimento-esterno-in-marmo-travertino-navona-...-04..06.jpg`, verticali 576 px);
- serra in ferro e vetro su gradoni in pietra di Prun (`realizzazione-pavimento-esterno-in-pietra-di-prun-...`), scala a sbalzo in San Pietro spessore 8 cm (`realizzazione-scala-interna-in-marmo-san-pietro-lucido-spessore-8-cm-01..06.jpg`), scala in pietra Piasentina scura (`...piasentina...-02..05.jpg`);
- dettagli materici: stemma scolpito su pietra Orsera, bordo bocciardato del tavolo in Rosso di Asiago, lavabo cilindrico in Rosal da un unico massello, lavello in Verdello da massello di 25 cm.

Mancano: foto recenti (dopo il 2011), laboratorio e macchinari attuali, sede, persone, lavori funerari (1 sola foto), materiali in lastra, lavori in pietra sinterizzata o Laminam (nessuna foto). Va scritto il brief delle foto da fare nel LEGGIMI. [Certo]

## Problemi tecnici da segnalare al cliente

Misurati il 6/10/2026 con Playwright (Chromium, 1440x900 a densità 1 e 390x844 a densità 2) e curl, attraverso la rete della sessione: i tempi assoluti includono il proxy, il confronto con google.com (0,19 s) dà il riferimento.

1. **Contatti che portano a dati di esempio del tema** [Certo]. Su tutte le 344 pagine con il footer:
   - "Tel. +39.049.9461675" e "Fax +39.049.5952371" puntano a `tel:+3211234567`; nei 344 file scaricati compaiono 1.376 link telefonici e **tutti** chiamano +3211234567. Il numero in testata ("049.9461675") e quello in home ("+049.9461675") non sono cliccabili: da telefono non c'è un solo tocco che chiami l'azienda. Prova: `_prova/attuale/misure.json`, campo `link`, a 1440 e a 390; `grep -o 'href="tel:[^"]*"' _prova/crawl/pagine/*.html`.
   - il testo "info@marmisgambaro.it" del footer apre `mailto:info@example.com` (le email in testata e in home invece sono giuste).
   - l'indirizzo del footer apre `https://goo.gl/maps/dfYWcXD5Upw`, che reindirizza a "Google Building 41, 1600 Amphitheatre Pkwy, Mountain View, CA" (intestazione `Location` letta con curl).
2. **Pagine demo e bozze pubbliche** [Certo]. 107 indirizzi del tema rispondono 200: listino "Plans & Pricing" in dollari, "Meet the Team" con Michael Doe e Clark Kent, Shop, Cart, Checkout, My Account, 25 pagine "elements", 16 articoli demo del 2013 (in inglese, uno sul tema in tedesco), "Ciao mondo!" ("Benvenuto in WordPress. Questo è il tuo primo articolo. Modificalo o eliminalo, e inizia a creare il tuo blog!"), "Hello world!", "WordPress Tutorial German with Impreza". L'API `wp-json` elenca 65 pagine e 17 articoli. In più la bozza `/pages/vendita/` con "TESTI DA RISCRIVERE IN QUANTO RILEVATI DA WEB" e lorem ipsum, e la vecchia home `/sample-page-2-2/`. Screenshot: `_prova/attuale/prove/*.png`, sintesi in `_prova/attuale/pezzi/prove-demo.jpg`.
3. **Software fermo al 2018** [Certo]. Meta generator "WordPress 4.9.29" (l'ultima versione oggi è la 7.1.3, dall'API di wordpress.org), tema Impreza 5.0.1, WPBakery Page Builder 5.4.7, Slider Revolution 5.4.7.2, Contact Form 7 5.0.1, The Events Calendar 4.6.13, jQuery 1.12.4; intestazione `x-powered-by: PHP/7.4.33` (ramo 7.4 senza aggiornamenti di sicurezza dal novembre 2022). L'API pubblica `wp-json/wp/v2/users` mostra il nome utente dell'amministratore ("admin"). Rischi concreti non verificati: non si è fatto nessun test di intrusione.
4. **Contenuti fermi al 2018** [Certo]. Titolo della home "Marmi Sgambaro – 1948-2018 – Settant'anni di garanzia di qualità", "© 2018" nel footer, logo dei 70 anni; i 42 file della libreria media visibili dall'API sono stati caricati tra il 29/03/2018 e il 26/06/2018 e 227 delle 247 immagini stanno nella cartella `uploads/2018/05`; le foto sono state scattate nel 2009-2011 (EXIF). Unico intervento successivo: la pagina Contatti, modificata il 12/02/2024 (casella privacy nel modulo).
5. **Dati societari mancanti** [Certo]. La partita IVA non compare in nessuna delle 354 pagine scaricate (0 occorrenze di "P.IVA" o "04564690289"): c'è solo nella privacy policy esterna di iubenda, che però indica "Via Leonardo Da Vinci, **76**" invece di 36 (ultima modifica 4/7/2022). Mancano anche PEC, REA e capitale sociale. Il fax è 049 5952371 sul sito e 049 5952370 su PagineBianche [DA CONFERMARE].
6. **Peso e velocità** [Certo].

   | Pagina | Larghezza | Richieste | Peso | Evento load |
   |---|---|---|---|---|
   | Home | 1440 | 57 | 3,3 MB | 6,1 s |
   | Home | 390 | 52 | 4,2 MB | 6,6 s |
   | Realizzazioni | 1440 | 117 | 5,8 MB | 11,6 s |
   | Realizzazioni | 390 | 171 | **29,2 MB** (139 immagini) | 13,6 s |
   | Scheda scala monumentale | 390 | 54 | 4,0 MB | 7,1 s |
   | Contatti | 1440 | 78 | 1,3 MB | 7,9 s |

   Da telefono la griglia Realizzazioni scarica le foto originali da 1024 px (fino a 1,1 MB l'una) per riquadri di 342 px. La prima risposta HTML arriva in 1,2-1,7 s (curl, tre prove) contro 0,19 s di google.com sulla stessa rete: nessuna cache di pagina.
7. **Immagini ingrandite oltre la loro misura** [Certo]. Nella categoria Scale interne a 1440 px, 6 foto su 10 sono mostrate a 816 px pur essendo larghe 576 o 640 px (ingrandimento fino a 1,42 volte: `RIMG1960.jpg`, `RIMG1956.jpg`, `RIMG1922.jpg`, `RIMG1871.jpg`, `IMG_1697.jpg`, `IMG_20171022_142426.jpg`). Le slide della home sono banner 1600x668 ricavati da foto compatte e risultano morbide a 1440. Il logo a 390 px è largo 72 px: il payoff è illeggibile. Prova: `misure.json`, campo `immagini`.
8. **Privacy e cookie** [Certo]. Banner iubenda con "Accetta" e "Rifiuta", privacy e cookie policy linkate, nessun cookie scritto prima del consenso: va bene. Però la pagina Contatti carica la mappa Google prima di qualsiasi consenso (31 richieste a maps.googleapis.com e 5 a maps.gstatic.com con il banner ancora aperto) e tutte le pagine caricano i caratteri da fonts.googleapis.com. Prova: `_prova/script/terze.mjs`.
9. **SEO e accessibilità** [Certo]. Nessuna meta description in nessuna pagina; nessun H1 in Home e Contatti, tre H1 in Lavorazioni; **tutte** le immagini delle pagine principali hanno `alt=""` (16 su 16 in home, 77 su 77 in Realizzazioni); nessuna sitemap; URL della pagina Realizzazioni di 124 caratteri, pagine aziendali sotto `/pages/`; titoli delle categorie "Categorie portfolio: ...".
10. **Testi chiusi in immagini** [Certo]. Solo il payoff del logo ("1948-2018 settant'anni di garanzia di qualità"). I titoli delle slide sono testo vero.
11. Cose che funzionano, da dire con onestà [Certo]: meta viewport presente, `scrollWidth` 390 su 390 in tutte e 7 le pagine misurate, menu mobile che si apre, HTTPS valido (Let's Encrypt, scade il 6/11/2026 con rinnovo automatico), http e www reindirizzati con 301 su `https://marmisgambaro.it/`, compressione gzip attiva, nessun errore JavaScript del sito in console (solo errori CORS dello script iubenda in alcune prove a 390), tutti i link interni e le 233 immagini delle pagine reali rispondono 200.

## Dati aziendali

| Dato | Valore | Fonte e certezza |
|---|---|---|
| Ragione sociale | **Marmi Sgambaro S.r.l.**, società a responsabilità limitata, attiva | Registro Imprese tramite aziende.it (https://www.aziende.it/marmi-sgambaro-s-r-l), VIES [Certo] |
| Partita IVA e codice fiscale | **04564690289** (valida su VIES il 6/10/2026, nome "MARMI SGAMBARO S.R.L.") | aziende.it, VIES (`_prova/crawl/esterni/vies-04564690289.json`), privacy iubenda [Certo] |
| REA | PD-399990, CCIAA di Padova, iscrizione 02/05/2011 | aziende.it [Certo] |
| Società storica | Marmi Sgambaro snc di Sgambaro R. e C., P.IVA 00373040286, REA PD-120414, iscritta dal 01/01/1974, stesso indirizzo, oggi ATECO 68.2 (affitto di immobili propri) | aziende.it (https://www.aziende.it/marmi-sgambaro-snc-di-sgambaro-r-e-c) [Certo]. Rapporto con la S.r.l. [DA CONFERMARE] |
| Sede | Via Leonardo da Vinci 36, 35018 San Martino di Lupari (PD); coordinate Google 45.6448, 11.8589 | sito, Google, VIES [Certo] |
| Telefono | 049 9461675 (+39 049 946 1675) | sito, Google, PagineBianche [Certo] |
| Cellulare e WhatsApp | 327 1687135 | solo PagineBianche [DA CONFERMARE] |
| Fax | 049 5952371 (sito, privacy) oppure 049 5952370 (PagineBianche) | [DA CONFERMARE] |
| Email | info@marmisgambaro.it | sito, privacy [Certo] |
| PEC | **marmisgambarosrl@legalmail.it** | aziende.it (Registro Imprese) [Certo]; da riscontrare su INI-PEC prima dell'invio |
| Codice SDI | P62QHVQ | aziende.it [Certo] |
| Orari | lunedì-venerdì 8-12 e 14-18; sabato e domenica chiuso; "Il Sabato mattina si riceve previo appuntamento" | Google Business (letto il 6/10/2026) e PagineBianche [Certo]; il sito non riporta orari |
| Attività | ATECO 23.70.1 "Segagione e lavorazione delle pietre e del marmo"; Google: "Ditta specializzata in marmi", "Ditta specializzata in pavimentazioni" | aziende.it, Google [Certo] |
| Anni di attività | fondata nel 1948 da Andrea Sgambaro, scultore; oggi seconda generazione | sito (Chi Siamo, bozza Vendita), PagineBianche [Certo come dichiarazione dell'azienda]. Nomi dei titolari attuali [DA CONFERMARE] |
| Dimensione | 8 dipendenti; ricavi 566.930 € nel 2024 (utile 9.822 €), 845.170 € nel 2022 (utile 28.241 €), 724.765 € nel 2021; capitale sociale 100.000 € | aziende.it, bilanci del Registro Imprese [Certo] |
| Aiuti pubblici | 9 per 303.385 € tra 2021 e 2025: tra questi Nuova Sabatini (macchinari, 2021, 9.689 €) e bando INAIL ISI 2023 (130.000 €, 17/01/2025); il resto garanzie su prestiti e contributi Covid | Registro Nazionale Aiuti tramite aziende.it [Certo]. Cosa è stato acquistato [DA CONFERMARE] |
| Marchi lavorati | Neolith, Lapitec, Laminam (loghi in home); trattamenti FILA ("nostro partner") | sito [Certo] |
| Certificazioni | nessuna dichiarata | sito, schede esterne [Certo] |
| Recensioni | Google 4,7 su 9 recensioni | Google Maps, 6/10/2026 [Certo]. Testi di terzi: non usarli senza permesso |
| Canali | Facebook facebook.com/marmisgambaro (richiede login, contenuti non letti); scheda Google Business con 4 foto del proprietario; scheda PagineBianche "Azienda verificata" con 8 foto | [Certo] |
| Sito fatto da | "by et.ics" (link a etics.it, oggi reindirizzato a sys-datgroup.com) | footer [Certo] |

Fonti non raggiungibili: Wayback Machine (web.archive.org risponde 429 o chiude la connessione a ogni tentativo), Instagram (429), Paginegialle (403). Le versioni del sito precedenti al 2018 esistevano (file caricati nel 2014 e nel 2016 ancora sul server) ma non si sono potute vedere. [Certo]

## URL vecchi

Elenco completo e classificato in `_prova/crawl/url-vecchi.tsv` (204 righe). Per `plugin/redirect-301.csv`:

**Pagine reali (8)**: `/` (Home), `/pages/chi-siamo/`, `/marmi-sgambaro-lavorazione-marmi-e-pietre-da-arredamento-realizzazione-scale-in-marmo-e-rivestimenti-in-pietra-naturale/` (Realizzazioni), `/pages/services/` (Lavorazioni), `/pages/contact/` e il doppione `/contact/` (Contatti), `/sample-page-2-2/` (vecchia home, verso la Home), `/pages/vendita/` (bozza, verso Azienda).

**Categorie (10)**: `/portfolio_category/scale-interne/`, `/portfolio_category/scale-esterne/`, `/portfolio_category/pavimenti-e-rivestimenti-interni/`, `/portfolio_category/pavimenti-e-rivestimenti-esterni/`, `/portfolio_category/piani-cucina/`, `/portfolio_category/bagni/`, `/portfolio_category/caminetti/`, `/portfolio_category/soglie-davanzali-e-decorazioni/`, `/portfolio_category/cancelli-e-recinzioni/`, `/portfolio_category/lapidi/`.

**Schede realizzazione (75)**, tutte sotto `/portfolio/`, nell'ordine della griglia:

- `/portfolio/pavimento-esterno-in-pietra-di-prun-bianca-anticata-e-scale-esterne-in-marmo-verdello-chiarofonte-di-asiago-anticato/` (Pavimenti e rivestimenti esterni, Scale esterne)
- `/portfolio/scala-interna-in-marmo-san-pietro-lucido-spessore-8-cm/` (Scale interne)
- `/portfolio/pavimento-esterno-in-marmo-travertino-navona-levigato-e-colonne-in-pietra-di-vicenza-levigata/` (Pavimenti e rivestimenti esterni)
- `/portfolio/piano-cucina-e-lavello-in-marmo/` (Piani cucina)
- `/portfolio/fioraia-in-pietra-di-prun-scalpellata-a-mano/` (Davanzali, soglie e decorazioni)
- `/portfolio/scale-interne-13/` (Pavimenti e rivestimenti interni, Scale interne)
- `/portfolio/scala-in-marmo-bianco-namibia-rhino/` (Scale interne)
- `/portfolio/scala-interna-in-aglomarmo-capri-ricavata-da-lastre-di-spessore-di-2-cm-con-finitura-semilucida-con-pedata-ed-alzata-a-90-gradi-completa-di-battiscopa/` (Scale interne)
- `/portfolio/pavimento-interno-in-marmo-rosal/` (Pavimenti e rivestimenti interni)
- `/portfolio/pavimento-interno-in-marmo-san-pietro/` (Pavimenti e rivestimenti interni)
- `/portfolio/pavimento-interno-in-marmo-crema-nova-rullato-e-spazzolato-in-spessore-2-cm-e-multiformato/` (Pavimenti e rivestimenti interni)
- `/portfolio/pavimento-interno-in-marmo-san-pietro-e-tozzetti-in-granito-azul-macaubas/` (Pavimenti e rivestimenti interni)
- `/portfolio/rivestimento-interno-in-quarzite-a-spacco-giza-white/` (Pavimenti e rivestimenti interni)
- `/portfolio/scala-interna-in-marmo-malaga-anticato-spessore-4-cm-con-toro-tondo-alzata-con-gola-fianchetti-sagomati-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-rosa-beige-lucido-spessore-4-cm-con-toro-tondo-alzata-con-gola-fianchetti-sagomati-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-verdello-anticato-martellinato-a-mano-con-lavorazione-per-effetto-finta-usura-spessore-4-cm-ed-alzata-da-3-cm/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-biancone-anticato-di-spessore-4-cm-con-toro-tondo-alzata-da-3-cm-con-gola-fianchetto-sagomato-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-biancone-lucido-spessore-4-cm-toro-tondo-alzata-con-gola-fianchetto-sagomato-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-biancone-levigata-a-mano-spessore-4-cm-toro-tondo-alzata-con-gola-fianchetto-sagomato-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-pietra-piasentina-anticata-spessore-3-cm/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-san-pietro-levigato-spessore-3-cm-pedata-e-alzata-al-dritto-battiscopa-e-fianchi/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-silva-oro-giallo-lucido-spessore-4-cm-con-toro-tondo-e-alzate-sagomate-con-gola/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-beige-atlantide-lucido-spessore-4-cm-con-toro-tondo-e-alzata-liscia/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-bianco-lasa-lucido-spessore-4-cm-con-toro-tondo-e-alzata-sagomata-con-gola-e-battiscopa-a-scivolo/` (Scale interne)
- `/portfolio/scala-interna-in-marmo-biancone-lucido-spessore-4-cm-con-toro-tondo-e-alzata-dritta/` (Scale interne)
- `/portfolio/scala-interna-elicoidale-in-marmo-silva-oro-giallo-lucido-spessore-4-cm-con-toro-tondo-e-alzata/` (Scale interne)
- `/portfolio/scala-monumentale-interna-in-marmo-calacata-lucido-spessore-6-cm-con-toro-tondo-e-alzata-sagomata-con-gola-balaustre-tornite-e-corrimano-sagomato/` (Scale interne)
- `/portfolio/scala-esterna-in-marmo-crema-nova-rullato-e-anticato-spessore-6-cm-pedata-e-alzata-al-dritto-fioraia-in-marmo-san-pietro-levigato/` (Scale esterne)
- `/portfolio/scala-esterna-in-marmo-san-pietro-rullato-spessore-5-cm-con-toro-tondo-battiscopa-e-corrimano-in-marmo-silva-oro-anticato/` (Scale esterne)
- `/portfolio/scala-esterna-in-quarzite-gaia-dark-mix-fiammata-e-spazzolata-spessore-2-cm-con-pedata-e-alzata-al-dritto/` (Scale esterne)
- `/portfolio/pavimento-in-pietra/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-in-travertino-navona-anticato-zoccolatura-in-marmo-san-pietro-levigato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-porfido-e-rustic-green-grigio-olivo/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-marmo-verdello-e-rosso-di-asiago-rullato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/basamento-colonna-in-marmo-malaga-levigato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-quarzite-vintage-gold-a-spacco-naturale-e-burattata-spessore-2-cm/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-in-quarzite-a-spacco-lime-gray-spessore-2-cm-rivestimento-parete-fioraia-e-ripiano-di-appoggio-in-marmo-san-pietro-levigato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-marmo-crema-nova-rullato-e-anticato-spessore-2-cm-in-multiformato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-marmo-giallo-istria-multiformato-lavorato-con-bocciardatura-carteggiatura-e-rullatura-spessore-2-cm/` (Pavimenti e rivestimenti esterni)
- `/portfolio/rivestimento-esterno-in-quarzite-giza-yellow-a-spacco-naturale-con-spessore-irregolare/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-esterno-in-porfido-del-trentino-a-spacco-con-formato-a-mattoncino/` (Pavimenti e rivestimenti esterni)
- `/portfolio/rivestimento-in-pietra-e-marmo-in-formato-naturale-a-spacco-e-martellinato-a-mano/` (Pavimenti e rivestimenti esterni)
- `/portfolio/pavimento-eterno-in-quarzite-gaia-dark-mix-fiammata-spessore-2-cm-formato-30-cm-a-correre/` (Pavimenti e rivestimenti esterni)
- `/portfolio/contorno-finestra-in-marmo-silva-oro-levigato/` (Davanzali, soglie e decorazioni)
- `/portfolio/stemma-di-famiglia-su-pietra-orsera-levigata/` (Davanzali, soglie e decorazioni)
- `/portfolio/contorno-finestra-in-marmo-silva-oro-levigato-2/` (Davanzali, soglie e decorazioni)
- `/portfolio/davanzale-sagomato-in-marmo-san-pietro-levigato/` (Davanzali, soglie e decorazioni)
- `/portfolio/cornice-in-marmo-biancone-di-asiago-levigato/` (Davanzali, soglie e decorazioni)
- `/portfolio/piano-cucina-in-marmo-trani-lucido-spessore-4-cm-rivestimento-in-marmo-trani-da-10x10-cm-burattato/` (Piani cucina)
- `/portfolio/piano-cucina-in-marmo-giallo-silva-oro-anticato-con-lavabo-spessore-20-cm/` (Piani cucina)
- `/portfolio/piano-cucina-in-granito-spessore-3-cm-lucido/` (Piani cucina)
- `/portfolio/tavolo-in-marmo-rosso-di-asiago-anticato-con-bordo-esterno-bocciardato-e-anticato/` (Piani cucina)
- `/portfolio/piano-cucina-in-marmo-giallo-reale-spessore-4-cm-anticato-lavabo-a-massello-sagomato-spessore-20-cm/` (Piani cucina)
- `/portfolio/rivestimento-in-marmo-trani-carteggiato/` (Cancelli e recinzioni)
- `/portfolio/inserti-cancello-e-rivestimenti-in-granito-nero-fiammato/` (Cancelli e recinzioni)
- `/portfolio/caminetto-in-marmo-verdello-di-asiago-massello-martellinato-a-mano-e-invecchiato/` (Caminetti)
- `/portfolio/rivestimento-caminetto-in-marmo-biancone-anticato/` (Caminetti)
- `/portfolio/rivestimento-caminetto-e-basamento-in-marmo-biancone-lucido/` (Caminetti)
- `/portfolio/rivestimento-caminetto-in-quarzite-grigia-gaia-gray/` (Caminetti)
- `/portfolio/rivestimento-caminetto-in-marmo-rosal-lucido/` (Caminetti)
- `/portfolio/cornice-per-caminetto-in-marmo-bianco-di-carrara/` (Caminetti)
- `/portfolio/basamento-per-stufa-in-marmo-moleanos-lucido/` (Caminetti)
- `/portfolio/caminetto-in-marmo-calacatta-lucido/` (Caminetti)
- `/portfolio/caminetto-2/` (Caminetti)
- `/portfolio/portale-e-contorni-finestre-in-marmo-verdello-di-asiago-bocciardato/` (Pavimenti e rivestimenti esterni)
- `/portfolio/rivestimento-caminetto-in-marmo-calacatta-lucido/` (Caminetti)
- `/portfolio/piano-per-mobile-da-bagno-rivestimenti-e-pavimenti-in-marmo-biancone-di-asiago-anticato-e-spazzolato-con-inserto-in-marmo-rosso-di-asiago/` (Bagni)
- `/portfolio/lavello-a-ciotola-e-piano-mobile-da-bagno-in-marmo-giallo-silva-oro-anticato-rivestimento-in-marmo-calacatta-lucido/` (Bagni)
- `/portfolio/lavello-e-piano-in-marmo-verdello-di-asiago-ricavato-da-unico-massello-di-spessore-25-cm-martellinato-ed-invecchiato-a-mano/` (Bagni)
- `/portfolio/bagno-in-pietra-rosa-2-2-2-2-2/` (Bagni)
- `/portfolio/rivestimento-bagno-in-travertino-navona-di-spessore-2cm-formato-30-cm-a-correre-anticato-spazzolato-e-stuccato-a-resina-bianca/` (Bagni)
- `/portfolio/rivestimento-bagno-in-ardesia-nera-italiana-a-spacco-naturale-spessore-1cm-formato-60x15cm/` (Bagni)
- `/portfolio/lavello-in-marmo-rosal-levigato-ricavato-da-unico-massello-altezza-86-cm-e-diametro-52-cm/` (Bagni)
- `/portfolio/piano-per-mobile-da-bagno-in-marmo-biancone-spessore-4-cm-spazzolato-e-anticato/` (Bagni)
- `/portfolio/lapidi-2/` (Soggetti funebri e lapidi)

**Demo del tema e archivi (107)**, da reindirizzare alla home o lasciare in 410:

`/2013/`, `/2013/01/`, `/2013/02/`, `/2013/03/`, `/2013/04/`, `/2013/07/`, `/2013/08/`, `/2013/09/`, `/2013/10/`, `/2013/11/`, `/2013/12/`, `/2018/`, `/2018/03/`, `/another-interesting-single-post/`, `/author/admin/`, `/blog-cards-masonry/`, `/blog-classic-grid/`, `/blog-compact/`, `/blog-flat-masonry/`, `/blog-side-image/`, `/blog-tiles-masonry/`, `/cart/`, `/category/coding/`, `/category/senza-categoria/`, `/category/social-marketing/`, `/category/web-design/`, `/category/web-design/photography/`, `/category/wordpress/`, `/checkout/`, `/ciao-mondo/`, `/elements/`, `/elements/accordion/`, `/elements/actionbox/`, `/elements/button/`, `/elements/chart/`, `/elements/codelights/`, `/elements/columns/`, `/elements/counter/`, `/elements/gallery/`, `/elements/google-maps/`, `/elements/iconbox/`, `/elements/logos-showcase/`, `/elements/message-box/`, `/elements/person/`, `/elements/pricing-table/`, `/elements/progress-bar/`, `/elements/separator/`, `/elements/sharing-buttons/`, `/elements/single-image/`, `/elements/slider/`, `/elements/social-links/`, `/elements/tabs/`, `/elements/testimonials/`, `/elements/tour/`, `/elements/video-player/`, `/error-404/`, `/events/`, `/hello-world-2-2/`, `/hello-world/`, `/home-2/`, `/home-3/`, `/home-4/`, `/imagination-encircles-the-world/`, `/just-a-single-post/`, `/my-account/`, `/one-more-post/`, `/pages/`, `/pages/blank/`, `/pages/contact-2/`, `/pages/faq-page/`, `/pages/login-page/`, `/pages/maintenance-page/`, `/pages/person-page/`, `/pages/pricing/`, `/pages/sidebar-left/`, `/pages/sidebar-right/`, `/pages/tables/`, `/pages/team/`, `/pagina-di-esempio/`, `/portfolio-grid-1/`, `/portfolio-grid-2/`, `/portfolio-grid-4/`, `/portfolio-grid-5/`, `/portfolio-styles/`, `/portfolio/`, `/post-with-interesting-picture/`, `/post-with-separate-sections/`, `/post-with-trendy-fullwidth-preview/`, `/post-without-preview/`, `/post-without-sidebar/`, `/satisfaction-lies-in-the-effort/`, `/shop/`, `/shop/shop-without-sidebar/`, `/sticky-post/`, `/tag/branding/`, `/tag/business/`, `/tag/coding-2/`, `/tag/design/`, `/tag/image/`, `/tag/music/`, `/tag/photography-2/`, `/tag/social/`, `/tag/video/`, `/tag/wordpress-2/`, `/this-post-looks-beautiful-even-with-long-interesting-title/`, `/typography-examples/`, `/wordpress-tutorial-german-with-impreza/`
