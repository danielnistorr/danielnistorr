# 01. Analisi del sito attuale (www.dibispa.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).
Nelle citazioni verbatim le parole della lista PAROLE_VIETATE sono spezzate da un punto mediano (es. "Lea·der"): il testo originale le contiene intere. Il trattino medio dei testi originali è reso con "-". Nell'indirizzo della frase 31 (Cassola 36022) lo spazio è indivisibile: con lo spazio normale la stringa contiene una sequenza della lista ("a", spazio, "360") e fa scattare il controllo delle parole vietate; nel nuovo sito l'indirizzo va scritto "36022 Cassola (VI)".
Prove (HTML, PDF, screenshot, misure) in `_prova/crawl/`, `_prova/attuale/` (screenshot `<pagina>-1440.png` e `-390.png` con i `.json` delle misure, `prove-js.txt`), `_prova/inventario-immagini.json`, `_prova/url-vecchi.txt`.

## In breve

- **Sito WordPress 5.1.19 su PHP 5.6.40, solo http.** Tema Bridge 11.0 (Qode Interactive), WPBakery 5.1.1, Slider Revolution 5.4.1, WPML 4.1.2. Contenuti in gran parte del 2017-2018 (file in `uploads/2017` e `2018`, footer "© 2018"), aggiornati solo Certificazioni (gennaio 2026), Contatti e Catalogo (ottobre 2025). Sulla porta 443 non risponde nessun HTTPS valido e nei registri pubblici dei certificati (crt.sh) non risulta **nessun certificato mai emesso** per dibispa.com: il browser segna ogni pagina "Non sicuro", anche quelle con i moduli. [Certo]
- **Tre guasti visibili a chiunque, con causa trovata**: il tag `<body>` di tutte le pagine è senza classi, il JavaScript del tema si interrompe (`qodeGridWidth`, "Cannot read properties of undefined (reading 'match')") e di conseguenza **il logo non compare mai** (5 immagini alt="Logo" con `visibility:hidden`), **il menu a hamburger su telefono non si apre** (altezza 0 dopo il tocco) e i nomi delle 6 fasi di lavorazione in Azienda restano nascosti. [Certo, in Chromium desktop e mobile]
- **Privacy rotta**: i link "Privacy Policy" e "Cookie Policy" del footer portano a una pagina iubenda "Document not found" (404); i moduli (contatti con 15 campi, catalogo, newsletter) non hanno informativa né consenso; alla prima visita, senza nessuna scelta, partono Google Analytics (cookie `__utma`, `__utmz`...), il riquadro Facebook e la chat Smartsupp. [Certo]
- **Uno script esterno sconosciuto nella home**: tre tag `<script src="//plankjock.com/20c1f9347f59cf976e.js">` dentro un blocco di testo della home italiana (pagina modificata il 3 ottobre 2025). Il dominio oggi risponde con errore 444. È il modo in cui di solito si presentano le iniezioni di codice nei WordPress non aggiornati: va fatto controllare dal tecnico del sito. [Certo per la presenza, Probabile per l'origine]
- **Materiale fotografico di ottimo livello**: 11 foto prodotto di studio su carta avorio, 10 delle quali **a 2.000-2.500 px** e nitide al 100% (catene oro, argento, Tessuto, quattro colorazioni), 7 foto di lavorazione in bianco e nero a 1.500-3.543 px (fusione, macchina catenaria, diamantatura, mani; la galvanica è solo una cattura schermo da 491 px), la sede in bianco e nero, il logo PNG a 2.075 px. Manca il vettoriale del logo, mancano foto di persone e reparti a colori. [Certo]
- **Identità oggi**: monogramma "DB" bianco in cerchio oro **#c59910** con la scritta DIBI grigia **#70767a**, payoff "Gold & Silver Italian Jewellery" (nelle grafiche delle fiere e nei cataloghi), fondo grigio chiarissimo #f6f6f6, riquadri crema #fce7be, font Palanquin. Linea di punta dichiarata: **Tessuto**. [Certo]

## Pagine esistenti

| Pagina | URL | Stato |
|---|---|---|
| Home IT | `/` | slider di 4 foto prodotto senza testo, frase "Lea·der nella produzione di catene in oro e argento", 3 riquadri Gold / Tessuto / Silver in inglese, riquadro NEWS vuoto, riquadro Facebook vuoto (circa 600 px), newsletter |
| Azienda | `/azienda/` | due colonne di testo istituzionale, foto della sede in bianco e nero, griglia di 6 foto di lavorazione con i nomi delle fasi visibili solo al passaggio del mouse |
| Collezioni | `/collezioni/` | tre blocchi foto + testo: Argento, Oro, Tessuto, pulsanti SCOPRI |
| Oro | `/oro/` | Basic Oro e Fantasie, pulsante CATALOGO |
| Argento | `/argento/` | Basic e Fantasie, pulsante CATALOGO |
| Tessuto | `/tessuto/` | citazione di Ursula K. Le Guin in italiano, testo descrittivo **in inglese**, pulsante CATALOGO |
| Catalogo | `/catalogo/` | solo un modulo "You can request our catalog..." **in inglese** (nome, email, oggetto, messaggio) |
| Certificazioni | `/certificazioni/` | Responsible Jewellery Council: testo, loghi COP e COC, 4 pulsanti (membership, annual report, supply chain policy, policy diritti umani), canale segnalazioni |
| News | `/news/` | "News ed Eventi di Dibi Spa" e "No posts were found." (0 articoli in tutto il sito) |
| Contatti | `/contatti-2/` | indirizzo, telefono, email, modulo di 15 campi misto italiano/inglese, nessuna mappa |
| Note legali | `/note-legali/` | testo legale su copyright e marchi |
| Sitemap | `/sitemap/` | mostra lo shortcode grezzo `[simple-sitemap types=”page”]` invece dell'elenco |
| Pagine di servizio pubbliche | `/thank-you/`, `/mc4wp-form-preview/` | conferma newsletter; anteprima del modulo con lo shortcode grezzo `[mc4wp_form]` |
| Inglese | `/?lang=en`, `/company/`, `/collections/`, `/gold/`, `/silver/`, `/tessuto/`, `/catalogo-2/`, `/news/`, `/contacts/` (tutte con `?lang=en`) + `/certifications/` | traduzioni del 2018-2019; Company ha un paragrafo in più sul distretto; News EN ha il titolo in italiano; Certifications ha il testo in italiano |
| Documenti | 5 PDF RJC linkati in `/wp-content/uploads/` (più 4 copie del 2022 non linkate) + 2 cataloghi PDF non linkati | vedi URL vecchi |

Menu: Azienda, Collezioni (Oro, Argento, Tessuto), Certificazioni, News, Catalogo, Contatti. Footer: icone social (Facebook, LinkedIn, Google+, YouTube, Instagram, Pinterest), newsletter, Note legali, Sitemap, Privacy Policy, Cookie Policy, ricerca, dati societari. [Certo]

## Testi reali (verbatim, con i refusi originali)

Home:
1. Titolo (H3): "Lea·der nella produzione di catene in oro e argento". In inglese (H1): "Lea·der in the production of gold and silver chains".
2. Riquadri: "Gold / See our collection", "Tessuto / See our collection", "Silver / See our collection"; "News"; "Follow us on social network".
3. Newsletter: "Iscriviti Alla nostra Newsletter / Inserisci qui il tuo indirizzo per rimanere sempre aggiornato sulle Nostre Novità!" e nel footer "Email Address to subscribe at our Newsletter / Subscribe".
4. Meta description: "Dibi spa è da sempre specializzata nella produzione di catene in oro e argento. Nel settore si contraddistingue per la produzione di catene base e di fancy, e per il Tessuto."

Azienda (testo intero, due colonne):
5. "Dibi nasce oltre trent’anni fa, creata dai fratelli Bizzotto, maestri nella produzione di catene in oro e in argento. La loro aspirazione è sempre stata quella di realizzare monili che trasmettessero l’eleganza ed il gusto del design italiano, coniugando l’arte della tradizione artigiana con la più alta innovazione tecnologica. Dibi ha da sempre avuto come obiettivo quello di comunicare emozioni e stati d’animo positivi attraverso l’oro e l’argento, esaltandone l’eleganza e la raffinatezza, trasferendo cultura, piacere del bello, gioia di vivere, di sedurre e di sognare. La nostra crescita aziendale è stata sicuramente favorita dal particolare contesto ambientale in cui di Dibi opera: il nord est italiano e, in particolare, l’area vicentino-bassanese, il più importante distretto orafo del mondo. Il vicentino è noto da sempre nel mondo per la tradizione della lavorazione dell’oro che risale al XIV secolo. Della corporazione degli orafi vicentini abbiamo come primo cenno una citazione nello statuto del comune del 1339. Nel 1776 gli orafi danno vita ad una autonoma corporazione degli orafi di Bassano e da quel tempo si specializzano nella produzione di catename in oro. Oggi, la lavorazione dell’oro nel vicentino, rappresenta la più vasta concentrazione specializzata al mondo, con un indotto che coinvolge sia settori di supporto tecnico (meccanica strumentale, stampistica, galvanica, ecc.), che di servizio (trasporto e corrieri specializzati, sistemi di sicurezza, ecc.). La lucentezza, la facilità di lavorazione, la virtuale indistruttibilità hanno permesso all’oro di ritagliarsi un ruolo speciale nella storia dell’umanità nei secoli. Dibi è erede e promotrice della tradizione della lavorazione dell’oro e dell’argento in italia e nel mondo."
6. "Alla base del successo di Dibi c’è sempre stata la capacità di coniugare creatività e strategie imprenditoriali, l’antico “saper fare” e il moderno “kno·w-how”, il sapore del “fatto a mano”, del pezzo unico, e la perfezione industriale. Oggi, Dibi rappresenta una delle maggiori e più dinamiche realtà dell’oreficeria e dell’argenteria Made-in-italy. Tecnologie sempre aggiornate e flessibilità hanno consentito lo sviluppo di una gamma di articoli ampia e differenziata, tale da soddisfare le esigenze dei diversi mercati e da favorire l’esportazione in tutto il mondo. La grande varietà di fantasie e applicazioni, unita alla quantità delle nuove proposte, rappresenta forse il tratto che più caratterizza dibi rispetto alle aziende che operano nello stesso comparto. Il passaggio rapido e tempestivo dalla fase ideativa e progettuale a quella esecutiva consente il costante adeguamento alle tendenze del gusto e alle richieste della clientela. L’altissimo grado di flessibilità a tutti i livelli, la preparazione e il dinamismo di tutti i collaboratori permettono di diversificare l’offerta in funzione delle varie realtà in cui Dibi si trova a competere. La produzione è controllata severamente in ogni fase: selezione delle materie prime, lavorazioni, confezionamento, placcatura eseguita in azienda. Tutto questo garantisce per Dibi qualità e valore in tutti gli articoli prodotti."
7. Le 6 fasi (didascalie delle foto, visibili solo al passaggio del mouse): "FUSIONE LAMINAZIONE-TRAFILATURA", "PRODUZIONE A MACCHINA", "SALDATURA", "DIAMANTATURA", "FINITURA", "GALVANICA". In inglese: "FUSION LAMINATION - DRAWING", "MACHINE PRODUCTION", "WELDING", "DIAMOND", "FINISHING", "GALVANIC".
8. Solo nella versione inglese (Company): "In all Vicenza region there are almost 800 gold companies with above 10.000 employees." e "DiBi was established thirty years ago and specialized in the production of gold and silver chains. Since the beginning DiBi aimed at reaching the height of the field through the technological innovation and the quality of the product and service."

Collezioni:
9. ARGENTO: "Dibi spa si è da sempre ispirata alla tradizione orafa della rinomata zona di appartenenza quale il vicentino-bassanese, uno dei più grandi distretti orafi del mondo. Qualità, eleganza e precisione si fondono nelle sue Collezioni in Oro e in Argento realizzate da mani esperte e competenti. Dibi spa realizza catene in argento in diverse modelli, forme, misure e colorazioni galvaniche. Utilizzando diversi metodi di lavorazione Dibi spa riesci a posizionarsi nei gradini più alti tra i produttori di catene, fregiandosi di numerosi brevetti internazionali e contraddistinguendosi per gli elevati standard di qualità e pregio."
10. ORO: "La linea ORO offre al cliente articoli tecnicamente evoluti e dal gusto sofisticato che nascono dalla simbiosi fra tradizione orafa e produzione industriale. Vengono creati sempre nuovi modelli, all’ avan·guardia del design e al di fuori degli schemi convenzionali. Dibi produce tutti i propri modelli nelle carature 8 - 9- 10-14-18-21-22 kt, e con lega gialla, bianca e rosè."
11. TESSUTO: "Il TESSUTO è il fiore all’ occhiello della produzione di Dibi spa, un intreccio di artigianalità ed eleganza si fondono per creare un prodotto che si distingue da più di 15 anni per la sua unicità e bellezza “ senza tempo”."

Oro:
12. BASIC ORO: "La linea ORO è presente in Dibi spa soprattutto attraverso le forme delle catene più tradizionali, quali le catene rolo, le catene spiga e grumetta e tanti altri modelli che rendono la gamma di prodotti di Dibi Spa completa in ogni tipologia."
13. FANTASIE: "La linea Oro si contraddistingue anche per la famiglia di catene Fantasia, disponibili in diversi modelli e colorazioni galvaniche, realizzate attraverso metodologie varie di lavoro e diamantature innova·tive, oltre all’ utilizzo di semilavorati leggerissimi." (in inglese: "innova·tive mirror-polish finishes, as well as extremely light semi-finished items")

Argento:
14. BASIC: "La produzione dell’Argento rappresenta ormai un punto di riferimento indiscusso per l’intero settore. Proponiamo un ampia gamma di prodotti : dalla CATENE IN ARGENTO dalle linee classiche della grumetta, delle figaro, del rolo ai prodotti più contemporanei sviluppati sempre attraverso le migliori tecnologie presenti sul mercato."
15. FANTASIE: "La linea Argento si contraddistingue anche per la famiglia di catene fantasia, disponibili in diversi modelli e colorazioni galvaniche, realizzate attraverso metodologie varie di lavoro e diamantature, per proporre sempre modelli che rispondano alle tendenze del mercato."

Tessuto (pagina italiana):
16. Citazione: "Non si puo’ cambiare niente dall’esterno. Stando al di fuori, guardando dall’alto, con un colpo d’occhio generale puoi scorgere le linee del disegno. Vedi cosa e’ sbagliato, cosa manca. Vorresti aggiustarlo,ma non puoi annodare i fili. devi esserci dentro, tesserli. Tu stesso devi esser parte del tessuto. / Ursula K. Le Guin"
17. Testo (in inglese anche nella pagina italiana): "WITHIN THE MATERIAL OF THE SENSES LIES TESSUTO. Just like the very structure of the Whole, akin to the movements of the cosmos, there is nothing random about “Tessuto”. It’s a revolution, and like any other movement - be it physical or human - there are reasons, laws, purposes behind it. It’s a revelation, and all the more deserving of admiration because, like any other extraordinary change, there’s an intuition behind it. A timeless concept of jewellery is emerging, brought to life through the eyes, indeed more so through touch, through contact with the skin. A pleasantly mystifying surprise that stimulates the senses, engendering sensations of wellbeing and harmony, time and again."
18. Meta description: "Tessuto è il prodotto di punta della famiglia Dibi, ideato e creato interamente in Azienda, migliorato nel corso degli anni ha ricevuto grossi riscontri da parte del mercato internazionale, rimanendo ancora oggi un punto fermo nell'intera collezione di Dibi."

Altre meta description (testi dell'azienda non visibili in pagina):
19. Collezioni: "Dibi Spa offre da sempre una vasta gamma nella sue Collezioni in Oro e in Argento, dalle catene base, nella quale si contraddistingue, alle catene fancy sempre più ricercate ed elaborate."
20. Oro: "Dibi Spa realizza da sempre catene in Oro sia basiche che fantasie, apportando sempre migliorie costanti che le permettono nel tempo di rimanere nella vetta delle azienda produttrici di Catename."
21. Argento: "Vieni a scoprire la Collezione di Catene in Argento di Dibi Spa, da oltre trent'anni specializzata nella progettazione e realizzazione di catene sia basiche che con fantasie sempre più studiate e ricercate per dare al cliente sempre un miglior prodotto."
22. News: "Scopri tutti gli Eventi di Dibi Spa, potrai rimanere sempre in contatto con Noi e avere la possibilità di incontrare il Nostro team Dibi."

Certificazioni:
23. "RESPONSIBLE JEWELLERY COUNCIL / RJC MEMBERSHIP / Siamo lieti di annunciare che Dibi Spa è ufficialmente entrata a far parte del Responsible Jewellery Council, l’ente internazionale no-profit che stabilisce gli standard etici dell’intera filiera dell’oro e della gioielleria. Decisione presa per sottolineare l’importanza data dall’azienda al rispetto delle norme etiche, sociali e ambientali."
24. Pulsanti: "RJC MEMBERSHIP", "ANNUAL REPORT", "SUPPLY CHAINS POLICY", "RJC POLICY".
25. Canale segnalazioni: "Per inviare segnalazioni di condotte illecite in ragione del rapporto di lavoro e violazioni o irregolarità che ledono l’integrità di una società, è possibile utilizzare il seguente indirizzo mail reportingdibi@gmail.com oppure tramite Raccomandata riservata a DI BI SpA c/o Via Grande 89 - 36022 Cassola (VI). Ogni segnalazione verrà gestita garantendo la riservatezza del segnalante e verrà vietato nei suoi confronti ogni atto intimidatorio e di discriminazione."
26. Meta description: "È con grande piacere e soddisfazione che Dibi Spa può annunciare a fornitori e clienti di essere entrati a far parte del Responsible Jewellery Council."

Documenti RJC (PDF del sito, firmati "La Direzione"):
27. Supply chain Policy (15/01/2025): "DIBI SPA. opera nella produzione di gioielli finiti in oro e argento. La vi·sione della Direzione è di mantenere il posizionamento e accrescerlo [...]". "DIBI SPA ha adottato gli standards Code of Practice RJC/COP e si fa garante di promuovere prassi responsabili dal punto di vista etico, dei diritti umani, sociale e ambientale in tutta la filiera dell'oro e dei platinoidi." "Ci impegniamo a condividere le linee guida OCSE (Responsible Supply Chains of Minerals from Conflict-Affected and High-Risk Areas) [...]".
28. Annual Report (20/02/2025, italiano e inglese): "DIBI SPA ha svolto la due diligence nei confronti dei propri partner commerciali al fine di verificare eventuali deviazioni dalle linee guida dell'OCSE ed inoltre non sono stati rilevati rischi per i diritti umani. Le transazioni considerate sono a basso rischio e le verifiche effettuate sono conformi ai principi RJC."
29. Politica per i diritti umani (15/01/2025): "DIBI SPA rifiuta il lavoro minorile e il lavoro forzato. Incoraggia la libertà di espressione dei dipendenti. Incoraggia il dialogo e rispetta l’esercizio delle libertà sindacali. Promuove un ambiente di lavoro privo di qualsiasi tipo di molestia."

Catalogo:
30. "You can request our catalog by filling out the form or sending an email to dibi@dibispa.com / Your name: / Your email: / Subject: / Your messagge: / Invia".

Contatti:
31. "Contatti DI BI SpA / Via Grande 89, Cassola 36022 Vicenza / +39 0424534099 / dibi@dibispa.com". Modulo: "Il tuo nome, Indirizzo, ZIP, Company, Titolo (Owner, President, Manager, Buyer), La tua email, Attività principale (Manufacture, Retailer, Importer-Wholesaler-Chains stories, Private, Other), Commento, Il tuo cognome, Città, Paese, Provincia, Numero telefonico, website, Altro / Invia". Meta: "Dibi Spa Via Grande 89, Cassola, 36022 Vicenza - I nostri contatti: Tel. +39 0424534099 Email: dibi@dibispa.com www.dibispa.com".

Footer (tutte le pagine):
32. "© 2018 Dibi S.p.A - Produzione di catene in oro e argento - Tutti i diritti riservati / Via Grande, 89 / 36022 Cassola (Vicenza) Italia / Tel. +39 0424 534099 / Fax +39 0424 533396 / Capitale Sociale € 1.500.000,00 i.v. / Cod. fiscale/Part. Iva e nr. reg. imprese VI 00509720249 / R.E.A. di Vicenza N° 133841 / Nr. Meccanografico 014394".

Testi chiusi in immagini (trascritti):
33. Intestazione dei cataloghi PDF: "DIBI S.p.A. Gold & Silver Italian Jewellery / via grande, 89 36022 cassola (vicenza) italy / tel. (+39) 0424 534099 fax (+39) 0424 533396 / www.dibispa.com - E-mail: dibi@dibispa.com".
34. Grafiche fiere (nella libreria media, oggi non pubblicate), tutte con "Visit us:" e il logo "DIBI Gold & Silver Italian Jewellery": HKTDC Hong Kong 1-5 marzo 2018 (Italian Pav. N. 3 CON 158); Vicenzaoro 18-23 gennaio 2019 (Pav. 4, Booth N. 170); Hong Kong 28 febbraio-4 marzo 2019 (Italian Pav. N. 3 CON 158); OroArezzo 6-9 aprile 2019 (Pav. Chimera, Booth N. 642); Vicenzaoro 7-11 settembre 2019 (Pav. 4, Booth N. 170); Hong Kong 16-22 settembre 2019 (Italian Pav. N. 3 CON 158); Vicenzaoro 17-22 gennaio 2020 (Pav. 4, Booth N. 170); Hong Kong 4-8 marzo 2020 (Italian Pav. N. 3 CON 158); OroArezzo 18-21 aprile 2020 (Pav. Chimera, Booth N. 642); Vicenzaoro 5-9 settembre 2020 (Pav. 4, Booth N. 170); Hong Kong 15-19 settembre 2020 (Hall 3FG, Booth 3G 424); Vicenzaoro 10-14 settembre 2021 (Pav. 7, Booth N° 806); JCK Las Vegas 10-13 giugno 2022 (Sands Expo & The Venetian, Pav. Italian, Booth Nr. 21024); JGW Jewellery & Gem World Singapore 27-30 settembre 2022 (Italian Pavilion, Booth 4C34); Vicenzaoro 9-13 settembre 2022 (Pav. 4, Booth N. 180).
35. Video YouTube "Dibi Diamond Cut" (6 giugno 2017), descrizione: "La verità è che tutto ciò che si può dire su un diamante riguarda le sue imperfezioni. Il diamante davvero perfetto sarebbe composto di sola luce."

Testi alternativi delle immagini: "catene in argento", "Fantasie in argento", "Gold Chains Fancy", "Gold Chains Basic-Dibispa", "gold", "Produzione di oro e argento", "Tessuto in oro", "Dibi SPA", "Logo".

Refusi e incoerenze da non riportare: "in cui di Dibi opera"; "catename"; "in italia", "Made-in-italy", "dibi" minuscolo; "in diverse modelli"; "Dibi spa riesci a posizionarsi"; "all’ avan·guardia", "all’ occhiello", "all’ utilizzo" (spazio dopo l'apostrofo); "“ senza tempo”"; "un ampia gamma"; "dalla CATENE IN ARGENTO"; "prodotti :"; "Non si puo’", "cosa e’ sbagliato", "aggiustarlo,ma", "devi" minuscolo dopo il punto; "Your messagge"; "Importer-Wholesaler-Chains stories" (sono le catene di negozi, "chain stores"); "nella sue Collezioni"; "nella vetta delle azienda produttrici"; carature scritte "8 - 9- 10-14-18-21-22 kt". Anni di attività in tre versioni: "oltre trent’anni" (Azienda, testo del 2017-2018), "thirty years ago" (inglese), iscrizione al registro dal 1976 (vedi Dati aziendali): nel 2026 sono circa 50. Il nome compare in nove grafie fra sito e documenti (Dibi S.p.A, Dibi S.p.a., Dibi spa, Dibi Spa, Dibi SpA, DiBi, DIBI SPA, DI BI SpA, DIBI S.p.A.); la ragione sociale del registro è **DI BI S.P.A.**: nel nuovo sito si propone **Di Bi S.p.A.** per i dati legali e **DIBI** come marchio, come nel logo [DA CONFERMARE].

Parole dei testi originali che il nuovo sito non riprende (PAROLE_VIETATE): "lea·der" (frase 1), "kno·w-how" (frase 6), "avan·guardia" (frase 10), "innova·tive" (frase 13), "vi·sione" (frase 27).

## Cosa fanno o vendono

- **Producono catene in oro e argento** a Cassola (VI), nel distretto orafo vicentino-bassanese: "Production of gold and silver chains" è anche l'attività certificata da RJC; la Supply chain Policy dice "produzione di gioielli finiti in oro e argento". [Certo]
- **Tre linee**: **Oro** (Basic: rolo, spiga, grumetta "e tanti altri modelli"; Fantasie con diamantature e semilavorati leggerissimi), **Argento** (Basic: grumetta, figaro, rolo; Fantasie diamantate) e **Tessuto**, presentato come "fiore all’ occhiello" e "prodotto di punta [...] ideato e creato interamente in Azienda", sul mercato "da più di 15 anni" (testo del 2018-2021). [Certo]
- **Leghe e titoli**: "carature 8 - 9- 10-14-18-21-22 kt, e con lega gialla, bianca e rosè"; colorazioni galvaniche (nelle foto: oro giallo, rosa, rutenio nero, argento); "placcatura eseguita in azienda". Catalogo oro in AU 585 (14 kt), catalogo argento in AG 925. [Certo]
- **Ciclo produttivo interno** (6 fasi della pagina Azienda): fusione, laminazione e trafilatura; produzione a macchina; saldatura; diamantatura; finitura; galvanica. [Certo]
- **Cataloghi PDF di settembre 2022** (sul server ma non linkati): oro 91 pagine, circa 880 codici articolo; argento 313 pagine, circa 2.900 codici (conteggio dei codici unici estratti dal testo). Per ogni articolo: codice, descrizione tecnica, peso in grammi, lunghezza, titolo; nessun prezzo. Famiglie (nomi dei titoli di sezione): adjustable chains, ball chain, box, cable, choker, cross, curb (grumetta), figaro, forzatina, franco, heart, herringbone, hollow, infinity, magic designs, miami cuban, multifile, nuovo cuore, popcorn, prince of wales, real snake, religious items, rolo, rope, round omega, saturn, singapore, spiga, traversino, trilly, tubetti, twisted magic, Y chains; solo in argento anche bismark, bizantina, cleopatra, fox tail, sugar chain, tiger, tulipano, wave. Il catalogo Tessuto (`2022/04/CATALOGO TESSUTO.pdf`) è nella libreria ma il file non esiste più (404). [Certo]
- **Clienti**: solo professionali. Il modulo contatti chiede ruolo (Owner, President, Manager, Buyer) e attività (Manufacture, Retailer, Importer-Wholesaler, catene di negozi, Private); il catalogo si chiede via modulo o email. [Certo]
- **Mercati e fiere**: "favorire l’esportazione in tutto il mondo"; dalle grafiche 2018-2022: Vicenzaoro (gennaio e settembre), HKTDC Hong Kong (marzo e settembre), OroArezzo, JCK Las Vegas, JGW Singapore. Partecipazioni dopo il 2022 [DA CONFERMARE]. [Certo per 2018-2022]
- **Brevetti**: "fregiandosi di numerosi brevetti internazionali" (Collezioni): numero e oggetto non indicati [DA CONFERMARE].
- **Responsible Jewellery Council**: membro da marzo 2022, certificato Code of Practices e, da novembre 2025, anche Chain of Custody (dettagli in Dati aziendali). Pubblicano policy filiera, diritti umani, annual report e un canale per le segnalazioni. [Certo]

## Immagini usate oggi (con giudizio sulla risoluzione)

Inventario completo con misure, soggetto, qualità e larghezza massima in `_prova/inventario-immagini.json` (47 voci); file in `assets/originali/` (con `manifest.json`) e `assets/esterne/` (con `manifest.json`). Il sito pubblica versioni ritagliate da WordPress (suffisso `-e1527...`, 1.500 px): togliendo il suffisso si scaricano gli originali a 2.500 px. [Certo]

| Tipo | Quantità | Misura massima trovata | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Foto prodotto di studio su carta avorio (oro zig-zag, oro basic, Tessuto nastri, Tessuto geometrico, quattro colori, argento grumetta e rolo, argento fantasia) | 11 (di cui 3 varianti dello stesso scatto) | 2.500x1.875 | **ottime**, nitide al 100%, luce morbida e ombre lunghe coerenti in tutta la serie | aperture a tutta larghezza fino a 1.440 px anche su schermi retina (2.500 px reali), schede delle linee. È il materiale più forte |
| Foto di lavorazione in bianco e nero (fusione, mani con pinza, macchina catenaria, mano e fili, bobina di grumetta, diamantatura, finitura a mano) | 7 | 1.500x1.500; la finitura a mano 3.543x2.362 | ottime (la fusione un po' granulosa) | sequenza delle fasi in quadrati fino a 750 px su retina; la finitura a mano anche a tutta larghezza |
| Reparto galvanica | 1 | 491x491 (è una cattura schermo) | **scarsa** | solo miniatura; serve una foto nuova |
| Sede di Via Grande 89, bianco e nero | 1 (+ copia su Google) | 3.543x2.230, probabilmente ingrandita da 2.048 (la copia su Google) | discreta, bordi morbidi | fino a circa 1.800 px; pagina Azienda o Contatti |
| Logo: DIBI + monogramma DB in cerchio oro; varianti orizzontale oro, monogramma positivo | 5 PNG | 2.075x815 | buona, **manca il vettoriale** | testata e footer; il cerchio oro diventa sigillo o favicon |
| Marchi RJC (COP 0000 6883 e COC C0000 6884) | 3 varianti | 2.480x767 | buona | Certificazioni e footer, rispettando le regole d'uso RJC |
| Grafiche fiere 2018-2022 (testo nell'immagine, CMYK) | 15 | 1.265x743 | grafiche, non foto | nessun uso diretto; fonte dei fatti sulle fiere |
| Foto articolo nei cataloghi PDF | circa 1.200 strisce | circa 800 px di larghezza | **scarse** (scansioni compresse, fondo bianco sporco) | al massimo miniature da 300-400 px; meglio di no |
| Profilo Google del titolare | 2 | 2.048 e 2.000 px | buone, ma sono varianti di foto già sul sito | nessuna in più |
| YouTube "Dibi Diamond Cut" (2017) | 1 video, 1 fotogramma | 1.280x720 | discreto, logo impresso | video incorporabile in Azienda o Diamantatura |

Foto pubblicate nella libreria ma mai mostrate dal sito: mani con pinza, bobina di grumetta, Tessuto geometrico, argento grumetta e rolo intera, le due varianti "AU-BASE" e "AU-TESSUTO". Mancano del tutto: persone e squadra, reparti a colori, macchine in campo largo, il Tessuto indossato, il magazzino o la spedizione. Facebook e Instagram (@dibi_spa) chiedono il login: non è stato possibile vedere se lì ci sono foto più recenti [DA CONFERMARE]. La Wayback Machine (web.archive.org) è bloccata dalla rete di questa sessione: nessuna versione storica consultata.

Colori e caratteri di oggi: oro del logo #c59910 (titoli del sito #c5980c, hover #af7a04), grigio della scritta #70767a, fondo #f6f6f6, riquadri crema #fce7be, pulsanti beige #ccc2b0; testo Palanquin 14 px grigio #818181; il tema carica anche Raleway, Roboto Mono e Great Vibes in tutti i pesi. [Certo]

## Problemi tecnici da segnalare al cliente

1. **Nessun HTTPS.** `https://www.dibispa.com` e `https://dibispa.com`: la connessione si chiude durante la negoziazione TLS ("SSL_ERROR_SYSCALL"); crt.sh non elenca nessun certificato per dibispa.com né per i sottodomini (controllo del 6/10/2026, lo stesso servizio elenca regolarmente i certificati di altri domini). Il sito si apre solo in http e il browser lo segna "Non sicuro"; i moduli contatti, catalogo e newsletter inviano i dati in chiaro. `dibispa.com` reindirizza a `www.` con 301. [Certo]
2. **Logo invisibile, menu mobile bloccato, didascalie nascoste.** Su tutte le pagine il tag è `<body>` senza classi; il file del tema `default.min.js` si ferma in `qodeGridWidth` con "Cannot read properties of undefined (reading 'match')". Il CSS del tema nasconde il logo (`.q_logo a {visibility:hidden}`) finché il JavaScript non lo mostra: risultato, testata senza logo a 1440 e a 390. A 390 px il menu a hamburger non si apre (menu alto 0 px dopo tocco e clic, 9 voci nel codice). I nomi delle 6 fasi in Azienda compaiono solo al passaggio del mouse, quindi mai su telefono. Prove: `home-1440.png`, `menu-home-390-*.png`, `prove-js.txt`. [Certo in Chromium; il difetto è nel codice HTML, quindi vale per ogni browser: Probabile]
3. **Script esterno non riconducibile all'azienda.** Nel contenuto della home italiana ci sono 3 tag `<script src="//plankjock.com/20c1f9347f59cf976e.js" async>` in un blocco di testo (visibili anche nell'API `wp-json/wp/v2/pages`, pagina modificata il 3/10/2025). Il dominio risponde 444. Non è stato aperto né analizzato; va rimosso e va controllata l'installazione, che gira su software fuori supporto (punto 4). [Certo per la presenza; origine da verificare]
4. **Software fuori supporto.** Intestazione `x-powered-by: PHP/5.6.40-trivenet-custom` (il ramo 5.6 non riceve aggiornamenti di sicurezza da gennaio 2019); `<meta name="generator" content="WordPress 5.1.19">` (ramo 5.1 del 2019); tema Bridge 11.0, WPBakery 5.1.1, Slider Revolution 5.4.1, WPML 4.1.2, Contact Form 7 5.1.6; `readme.html` di WordPress pubblico. [Certo]
5. **Privacy e cookie.** "Privacy Policy" e "Cookie Policy" del footer aprono `iubenda.com/privacy-policy/20822814` e `/cookie-policy`: pagina "Document not found" (HTTP 404). I moduli non hanno informativa né casella di consenso. Alla prima visita, senza nessuna scelta, il sito chiama Google Analytics e imposta i cookie `__utma`, `__utmb`, `__utmc`, `__utmt`, `__utmz` (vecchio ga.js, proprietà UA-96943901-1: Universal Analytics, che Google ha smesso di elaborare nel luglio 2023, quindi oggi raccoglie cookie senza dare statistiche), carica il riquadro Facebook e la chat Smartsupp (la chat non si collega: WebSocket rifiutato con codice 400). La barra "Questo sito utilizza i cookie: Leggi di più." è nel codice ma non offre scelte e nella prima schermata non compare. La configurazione iubenda dei consensi dei moduli ha un errore di sintassi ("Unexpected token 'true'") e non parte. Prove: `prima-visita-home-1440.png/.json`, `_prova/crawl/esterni/iubenda-*.html`. [Certo]
6. **Contenuti fermi o rotti.** Footer "© 2018" su tutte le pagine; News: "No posts were found." (0 articoli, feed RSS vuoto) e in home un riquadro NEWS vuoto e un riquadro Facebook vuoto alto circa 600 px; icona Google+ (servizio chiuso nel 2019; il link porta a un blog di Google); la pagina Sitemap mostra lo shortcode `[simple-sitemap types=”page”]`; la pagina pubblica `/mc4wp-form-preview/` mostra `[mc4wp_form]`; le grafiche delle fiere si fermano a settembre 2022. [Certo]
7. **Lingue mescolate.** Nella versione italiana: "See our collection", "Gold", "Silver", "Follow us on social network", "Subscribe", la pagina Catalogo e il testo del Tessuto in inglese; nella versione inglese: News con titolo italiano, Certifications con testo italiano, voce di menu "Catalogo". [Certo]
8. **Lentezza.** Tempo di prima risposta del server 1,68-1,71 s sulla home (curl, 5 prove) e 1,4-2,0 s su tutte le pagine (Chromium); nessuna cache di pagina. Ogni pagina fa 117-137 richieste, di cui 76-78 script (716-727 KB di JavaScript) e 26-29 fogli di stile. Peso: 1,1-1,9 MB per le pagine interne, 3,0 MB la home, **6,2 MB la pagina Azienda** a 1440 (la foto della sede è un JPEG di 3,3 MB e 3.543 px mostrato a 1.100 px). Evento load fra 3,9 e 8,5 s sulle pagine interne; la home 5,9 s in una misura e 17,7-17,9 s in altre due (lo slider aspetta tutte le immagini). Le foto da 1.500 px sono scaricate per riquadri da 281 px. [Certo]
9. **Leggibilità.** Testo dei paragrafi grigio #818181 su #f6f6f6 a 14 px: contrasto **3,60:1** (il minimo WCAG AA è 4,5:1); sui riquadri crema 3,21:1; titoli e link oro #c5980c su #f6f6f6: 2,47:1. Il viewport `user-scalable=no` impedisce di ingrandire con le dita. [Certo]
10. **Mobile.** A 390 px nessuno scorrimento orizzontale su 13 pagine (scrollWidth 390); restano i difetti del punto 2, il modulo contatti di 15 campi in ordine misto (nome, indirizzo, CAP, azienda... poi cognome) e su retina il monogramma del footer (150 px) mostrato a 144 px, cioè 288 pixel fisici: ingrandito quasi del doppio. [Certo]
11. **Link e file rotti.** iubenda privacy e cookie (404); 3 icone del sito `cropped-logo-DB-*.png` (404); la favicon principale è presa da `demo.velvetmedia.it`, il dominio di prova dell'agenzia che ha fatto il sito; LinkedIn `company-beta/11084104` porta al login; `CATALOGO TESSUTO.pdf` e altri tre file della libreria media in 404. Su 79 link unici controllati: 42 rispondono 200, 31 reindirizzano (301 o 302), 5 danno 404, 1 dà 403 (`wp-login.php`, protetto) (`_prova/crawl/link-stato.txt`). [Certo]
12. **SEO.** Nessun H1 in Home, Azienda, Collezioni, Tessuto, Catalogo, News; l'unico H1 della home inglese è "Lea·der in the production of gold and silver chains"; nessuna `og:image` (le anteprime sui social escono senza foto); titolo della pagina Contatti "Dibi Spa | Telefono | DIBI SPA | Per maggiori informazioni"; meta description assente in Catalogo, Note legali, Sitemap, Company. Catalogo PDF da 20 MB e 6,5 MB sul server ma non collegati da nessuna pagina. [Certo]
13. **Dati societari: presenti.** Il footer riporta ragione sociale, sede, capitale sociale interamente versato, codice fiscale e partita IVA, numero REA: da questo lato il sito è in regola. La ragione sociale è scritta "Dibi S.p.A" invece di "DI BI S.P.A." del registro. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | DI BI S.P.A. (sul sito "Dibi S.p.A", "DI BI SpA"; su Google "DIBI S.p.a.") | aziende.it (dati Registro Imprese, aggiornati al 7/9/2026), footer del sito |
| Forma | Società per azioni, attiva | aziende.it |
| Partita IVA e codice fiscale | 00509720249 | footer del sito, aziende.it |
| REA | VI-133841 | footer ("R.E.A. di Vicenza N° 133841"), aziende.it |
| Capitale sociale | € 1.500.000,00 i.v. | footer, aziende.it |
| Iscrizione | 01/11/1976, CCIAA di Vicenza ("dal 1976") | aziende.it. Il sito dice "oltre trent’anni fa" [DA CONFERMARE l'anno di fondazione da scrivere] |
| Fondatori | "i fratelli Bizzotto" (nomi non indicati) | pagina Azienda [DA CONFERMARE i nomi, se li vogliono citare] |
| Sede | Via Grande 89, 36022 Cassola (VI); coordinate 45.73928, 11.78465 | footer, Contatti, profilo Google |
| Telefono | +39 0424 534099 | footer, Contatti, profilo Google |
| Fax | +39 0424 533396 | footer, cataloghi |
| Email | dibi@dibispa.com | Contatti, cataloghi |
| PEC | dibispa@pec.trive.net | aziende.it (non è sul sito) |
| Segnalazioni (whistleblowing) | reportingdibi@gmail.com, o raccomandata riservata in sede | pagina Certificazioni |
| Codice destinatario SDI | USAL8PV | aziende.it |
| Nr. meccanografico | 014394 | footer [DA CONFERMARE se va riportato nel nuovo sito] |
| Orari | lunedì-venerdì 8:00-17:30, sabato e domenica chiuso | profilo Google [DA CONFERMARE: non sono sul sito] |
| Profilo Google | "DIBI S.p.a.", categoria "Orafo", 4,2 stelle su 9 recensioni | Google Maps, place_id ChIJg8B22UjXeEcR66HuN3P_BtY |
| Attività dichiarata | ATECO 32.12.2 | aziende.it |
| Fatturato | € 22.713.079 (2024, +15,4%); € 19.686.978 (2023); € 21.391.484 (2022) | aziende.it (bilanci depositati) |
| Utile 2024 | € 138.413 | aziende.it |
| Dipendenti | 38 (2024), fascia 20-49 | aziende.it |
| Marchi e linee | DIBI (logo con monogramma DB), payoff "Gold & Silver Italian Jewellery", linea **Tessuto** | sito, cataloghi, grafiche fiere [DA CONFERMARE se "Tessuto" è un marchio registrato] |
| Responsible Jewellery Council | membro da marzo 2022, forum "Jewellery and watch manufacturer and/or wholesaler" | responsiblejewellery.com/member/dibi-spa/ |
| Certificato RJC COP | n. 0000 6883, Code of Practices dicembre 2024, ricertificazione, audit 29/09/2025, rilasciato 17/11/2025, valido fino al 03/11/2028, materiali oro e argento, ente Bureau Veritas Italia; attività "Production of gold and silver chains". Il precedente era il n. 0000 4414 (03/11/2022-03/11/2025) | PDF del certificato sul sito RJC (`assets/esterne/rjc-certificato-cop-0000-6883.pdf`) |
| Certificato RJC Chain of Custody | n. C0000 6884, standard dicembre 2024, certificazione iniziale, audit 13/10/2025, rilasciato 17/11/2025, valido fino al 03/11/2028, materiali argento e oro | PDF del certificato sul sito RJC (`assets/esterne/rjc-certificato-coc-c0000-6884.pdf`) |
| Canali social | facebook.com/dibispa, instagram.com/dibi_spa, linkedin (company 11084104), YouTube "Dibi spa" (1 video del 2017, 118 visualizzazioni), Pinterest Dibispa_1 (4 pin, 2 follower), Google+ (chiuso) | link del footer |
| Fiere | Vicenzaoro, HKTDC Hong Kong, OroArezzo (2018-2022), JCK Las Vegas e JGW Singapore (2022) | grafiche nella libreria media |
| Brevetti | "numerosi brevetti internazionali", senza dettagli | pagina Collezioni [DA CONFERMARE] |

Ricerca web generale non disponibile (motori non utilizzabili da questa sessione): i dati vengono dal sito, da aziende.it, dal sito RJC e dal profilo Google; nessun altro portale di settore consultato.

## URL vecchi

Elenco completo, con stato e data di ultima modifica, in `_prova/url-vecchi.txt` (servirà per `plugin/redirect-301.csv`). Il sito è solo http: i redirect vanno impostati per `http://www.dibispa.com` e `http://dibispa.com`.

| URL vecchio | Pagina | Nota |
|---|---|---|
| `/` | Home IT | |
| `/azienda/` | Azienda | |
| `/collezioni/` | Collezioni | |
| `/oro/` (e `/oro`) | Oro | |
| `/argento/` (e `/argento`) | Argento | |
| `/tessuto/` (e `/tessuto`) | Tessuto | |
| `/catalogo/` (e `/?page_id=56`) | Catalogo | |
| `/certificazioni/` | Certificazioni | |
| `/certifications/` | Certificazioni EN | testo italiano |
| `/news/` | News | vuota |
| `/contatti-2/` | Contatti | |
| `/note-legali/` | Note legali | |
| `/sitemap/` | Sitemap | shortcode rotto |
| `/thank-you/`, `/mc4wp-form-preview/` | servizio newsletter | da togliere |
| `/?lang=en` | Home EN | |
| `/company/?lang=en` | Company | |
| `/collections/?lang=en` | Collections | |
| `/gold/?lang=en` | Gold | |
| `/silver/?lang=en` | Silver | |
| `/tessuto/?lang=en` | Tessuto EN | |
| `/catalogo-2/?lang=en` (e `/catalog/?lang=en`, `/catalogo/?lang=en`) | Catalog | |
| `/news/?lang=en` | News EN | |
| `/contacts/?lang=en` | Contacts | |
| `/feed/`, `/comments/feed/`, `/feed/?lang=en` | feed RSS | vuoti |
| `/sitemap_index.xml`, `/page-sitemap.xml`, `/post-sitemap.xml`, `/portfolio_page-sitemap.xml` | sitemap Yoast | |
| `/wp-content/uploads/2-Rendicontazione-It-En.pdf` | Annual Report RJC 2025 | linkato da Certificazioni |
| `/wp-content/uploads/3-Supply-chain-Policy-politica-RJC.pdf` | Supply chain policy 2025 | linkato da Certificazioni |
| `/wp-content/uploads/POLITICA-RJC-PER-I-DIRITTI-UMANI.pdf` | Politica diritti umani 2025 | linkato da Certificazioni |
| `/wp-content/uploads/RJC-POLICY.pdf`, `/wp-content/uploads/SUPPLY-CHAIN-POLICY.pdf` | versioni precedenti | linkati da Certifications |
| `/wp-content/uploads/SUPPLY-CHAIN-POLICY-1.pdf`, `-2.pdf`, `ANNUAL-REPORT-1.pdf`, `RJC-POLICY-1.pdf` | copie 2022 | non linkate |
| `/wp-content/uploads/CAT.AU_SEP.LIGHT_.pdf`, `/wp-content/uploads/CAT.AG_SEP.LIGHT_.pdf` | cataloghi oro e argento 2022 | non linkati; da decidere col cliente se restano pubblici |
