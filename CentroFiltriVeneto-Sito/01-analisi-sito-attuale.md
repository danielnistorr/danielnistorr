# 01. Analisi del sito attuale (www.centrofiltriveneto.com)

Analisi del 18 ottobre 2026, fatta solo in funzione della nuova home. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare col cliente (va nel LEGGIMI, mai a vista nella pagina).

## In breve

- **Chi sono.** Centro Filtri Veneto S.r.l. (CFV) è un grossista di filtri e ricambi a Tombelle di Vigonovo (VE), Via del Lavoro 30, "a 10 minuti dal centro di Padova". La società è stata iscritta al registro imprese il 17/02/2016 e ha 18 dipendenti. Ha fatturato 5,22 milioni di euro nel 2024 (+10,5%). Porta avanti l'attività della "Casa del Filtro Veneta", di cui il sito dice "specialisti che lavorano dal 1985". [Certo]
- **Cosa vendono.** Filtri per auto, veicoli industriali, movimento terra e agricoltura, filtri idraulici e oleodinamici, separatori e ricambi per pompe a vuoto, filtri per aria e fumi di reparto, lubrificanti Castrol ("rivenditore autorizzato"), accumulatori, ricambi aftermarket, chimica e accessori. A magazzino ci sono "più di 4000 filtri diversi disponibili in pronta consegna e più di 15000 gestiti". [Certo]
- **A chi vendono.** Soprattutto ai professionisti: ricambisti, officine, flotte e industria. I ricambisti hanno un portale B2B con login. Le condizioni di vendita sono EXW e prevedono spese di gestione sotto i 100 euro di fattura. Per i privati il menu rimanda a un secondo dominio (`cfvfilter.com`), che oggi non risponde. [Certo]
- **Una prova forte che il sito non mostra.** CFV è certificata **ISO 9001:2015 da TÜV Rheinland** (ID 9000034903, verificato su Certipedia). Lo dice solo il portale B2B: il sito principale non ne parla. [Certo]
- **Il sito.** È un WordPress 6.0 con tema Betheme (Muffin group, demo "Factory"), WPBakery e Slider Revolution, fermo al 2016-2017. Le ultime modifiche risalgono al luglio 2021 (pagine Parker e Baldwin). La home pesa **6,8 MB**, di cui 3,5 MB per una sola foto di 4032 px. Non ha un H1 e non ha un numero di telefono cliccabile. Mancano gli orari, la privacy policy e il banner cookie. Il modulo di contatto stampa a video il testo "[recaptcha]". [Certo]
- **Il materiale vero.** Sul sito ci sono quattro foto dell'azienda: la piramide di filtri (scattata con iPhone, buona), il magazzino (Nikon, buona), il banco con tre persone (discreta) e la sede (scarsa). C'è anche il logo orizzontale in PNG a 2440 px. Tutto il resto è demo del tema, loghi dei marchi o immagini dei produttori. [Certo]

## Pagine esistenti

| Pagina | URL | Contenuto | Ultima modifica (REST API) |
|---|---|---|---|
| Home | `/` | foto della piramide di filtri, frase "dal 1985", blocco giallo, 5 famiglie con illustrazione, "Solo 10 minuti da Padova" con mappa statica e recapiti | 14/01/2017 |
| L'azienda | `/lazienda/` | profilo (fondazione 2015, Casa del Filtro Veneta, 4000/15000 filtri), foto della sede e del magazzino | 14/01/2017 |
| Marchi e prodotti | `/marchi-prodotti/` | 16 schede di marchi più Castrol, FAAM e ricambi | 18/07/2021 |
| Filtrazione | `/marchi-prodotti/filtrazione/` | doppione della pagina marchi, con un **lorem ipsum** nella scheda Fleetguard | 09/03/2016 |
| 12 pagine di marchio | `/marchi-prodotti/<marchio>/` | testo copiato dal produttore, listino in PDF dove c'è, modulo di contatto | 2015-2021 |
| Contatti | `/contatti/` | recapiti, indicazioni "Da Padova Est", modulo, mappa Google (rotta) | 14/01/2017 |
| About | `/about/` | pagina di esempio di WordPress in inglese, ancora pubblicata e in sitemap | 20/10/2015 |
| E-COMMERCE | `/category/uncategorized/` | il menu porta qui: una pagina di categoria vuota ("Uncategorized", autore "admin") | |
| RICAMBISTI (sottomenu) | `ecommerce.centrofiltriveneto.com` | portale B2B Proger ClipParts con login (vedi sotto) | |
| PRIVATI (sottomenu) | `www.cfvfilter.com` | non raggiungibile il 18/10/2026 (503 in http, connessione chiusa in https) | |

Il menu a 1440 px mostra HOME, AZIENDA, MARCHI, E-COMMERCE, CONTATTI. RICAMBISTI e PRIVATI sono un sottomenu a tendina di E-COMMERCE, che da solo porta alla categoria vuota. Prove: `_prova/crawl/*.html`, `pages.json`, `sm-pages.xml`.

**Il portale B2B** (`ecommerce.centrofiltriveneto.com`, Proger ClipParts su IIS 8.5 / ASP.NET, con dati TecDoc) mostra nella prima schermata il marchio TÜV ISO 9001:2015, il riquadro "ACCEDI / ACQUISTA IN SICUREZZA" e "Non hai un account? Clicca Qui". Seguono i riquadri MP Filtri, Fleetguard, MANN, Donaldson e UFI, poi "DISTRIBUTORI GFT FILTERS" e le news ("NUOVA POLITICA RESI", "CONDIZIONI DI VENDITA" del 21/02/2025, "Poiltica per la qualità"). SERVIZI, CATALOGHI e PROMOZIONI rispondono "questa funzionalità è attiva solo dopo l'autenticazione". Nell'HTML c'è un avviso nascosto, "Il servizio di ClipParts è temporaneamente sospeso", e un link rotto `http://http://shop-terra.com/gftkatalog/`. Su un telefono il portale non si usa: manca il meta viewport, la pagina è larga 1170 px e a 390 px resta bianca sotto la testata (`05-ecommerce-390-schermata.png`). [Certo]

## Testi reali (verbatim, con i refusi)

Home:
1. Titolo della pagina: "CFV – Centro Filtri Veneto S.r.l. – Distributore Filtri Padova e Venezia"
2. "Centro Filtri Veneto S.r.l. ha specialisti che lavorano dal 1985 nel settore della filtrazione e ricambi."
3. "Abbracciamo diversi settori della filtrazione: dall'automotive ai veicoli industriali, dal movimento terra all'agricoltura, dall'abbattimento fumi alla depolverazione"
4. "Centro Filtri Veneto Srl è realtà nel panorama della filtrazione e nei ricambi e la nostra forza è essere sempre pronti a dare una risposta a qualsiasi richiesta nel settore!"
5. "APPLICAZIONI PER PRODOTTI DI FILTRAZIONE", poi cinque famiglie:
   - "Filtri per mezzi industriali movimento terra e agricoltura": "Settore di primaria importanza a cui dedichiamo particolare attenzione perchè soggetto a repentini cambiamenti."
   - "Filtri Idraulici": "Una vasta gamma di elementi filtranti idonei a qualsiasi applicazione oleodinamica e industriale ci permettono di soddisfare qualsiasi esigenza."
   - "Filtri Separatori e Pompe Vuoto": "Filtri Separatori e ricambi per Pompe Vuoto da noi proposti sono realizzati con le medesime caratteristiche e materiali del prodotto originale."
   - "Filtri trattamento aria e fumi": "Una corretta filtrazione nei reparti produttivi garantisce un ambiente privo di ogni pericolo di contaminazione e assicura l'integrità e il benessere delle persone."
   - "Chimica e accessori generici": "La gamma di prodotti detergenti per autotrazione e industria di altissimo livello, garantiscono la massima resa nel rispetto dell'ambiente."
6. "Solo 10 minuti da Padova" / "Via Del Lavoro, 30 30030 - Vigonovo (VE) Tel: 049 9801910 Fax: 049 504099 info@centrofiltriveneto.com P. IVA e C.F. 04320460274" / "Contattaci" / "Vai alla nostra pagina contatti"
7. Piede: "Menù" (Home, L'azienda, Marchi e Prodotti, Recapiti, Contatti e Mappa); "Prodotti" (Filtri, Lubrificanti Castrol, Accumulatori Vipiemme, Ricambi aftermarket, Chimica e accessori); "Applicazioni Filtrazione" (Coopers Fiamm by Sogefi, Starline, Donaldson Filtration Solutions, Virgis Filter, Fleetguard Cummins); "© 2026 CFV - Centro Filtri Veneto S.r.l. - Distributore Filtri Padova e Venezia. All Rights Reserved. Muffin group"

L'azienda (lo stesso testo è sul portale B2B):
8. "Centro Filtri Veneto Srl viene fondata nel 2015. Svolge la medesima attività della precedente "Casa del Filtro Veneta" ed è operativa nella stessa sede da Gennaio 2016."
9. "A seguito dei 20 anni e più della precedente esperienza nel settore, ha acquisito conoscenza e preparazione per rispondere alle richieste di un mercato sempre più articolato ed esigente."
10. "Il nostro magazzino conta più di 4000 filtri diversi disponibili in pronta consegna e più di 15000 gestiti."
11. "Qualità, flessibilità e servizio sono i punti di forza della nostra azienda capace di cogliere e seguire i vari cambiamenti del mercato, pronti a dare una risposta a qualsiasi richiesta!"

Marchi e prodotti:
12. "Il nostro magazzino offre la maggior parte di prodotti e ricambi in pronta consegna e l'esperienza di Centro Filtri Veneto al tuo servizio."
13. "Tutti i nostri filtri" / "Per mezzi industriali, movimento terra, agricoltura, auto, trattamento aria e fumi"
14. Castrol: "Centro Filtri Veneto Srl ne è rivenditore autorizzato"
15. Ricambi: "Centro Filtri Veneto Srl offre una delle più ampie gamme di ricambi "aftermarket"."
16. In ogni pagina di marchio: "Contatta il nostro negozio ed un membro del nostro staff sarà immediatamente a tua disposizione per guidarti nella scelta del prodotto migliore per le tue necessità."

Contatti:
17. "Da Padova Est / 1. Prendi SR308, Corso Argentina e Uscita Via Vigonovese in direzione di Via Statuto dei Lavoratori a Vigonovo / 2. Segui Via Statuto dei Lavoratori in direzione di Via del Lavoro a Località Zona Tombelle I"
18. "Domande? Scrivici! Compila correttamente i campi sottostanti e ti contatteremo nel minor tempo possibile con la soluzione alla tua richiesta."
19. "Siamo a Tombelle di Vigonovo (VE) - a 10 minuti dal centro di Padova"

Condizioni di vendita (PDF del portale, `_prova/crawl/condizioni-vendita.pdf`):
20. "I Prodotti s'intendono venduti Ex Works (EXW) e, quindi, la consegna s'intende perfezionata presso l'unità produttiva di Centro Filtri Veneto Srl"
21. "In caso di Fatture differiti di importo inferiore ad € 100.00 + iva Centro filtri Veneto srl si riserva di Addebitare € 10.00 + iva per spese di gestione"
22. Il cliente è "responsabile in via esclusiva della scelta dei Prodotti commissionati e, di conseguenza, anche dell'esatta individuazione dei Prodotti idonei per ciascun veicolo".

Refusi e incoerenze da non riportare: "perchè", "Doanaldson", "nebbie olesoe", "FIAAM", "Poiltica", "primo equipaggiaamento", "I autoricambi", "percorso evolutivo che percorso evolutivo", "è realtà nel panorama". Gli accumulatori sono "Vipiemme" nel menu e "FAAM" nella pagina. Il link "Argo Hytos" porta alla pagina Virgis. Le schede C.F.V., HYDAC e GFT portano a "#". I link del piede Coopers Fiamm e Starline danno 404. Il testo dei marchi è copiato dai produttori ed è pieno di parole vietate (leader, eccellente, missione, passione): non si riusa.

## Cosa fanno (per la home)

**Famiglie** (dal sito): filtri per veicoli industriali, movimento terra e agricoltura; filtri auto; filtri idraulici e oleodinamici per macchine mobili e impianti; filtri separatori e ricambi per pompe a vuoto; filtri per aria e fumi di reparto e depolverazione; lubrificanti Castrol; accumulatori; ricambi aftermarket; chimica (detergenti per autotrazione e industria) e accessori. La foto dei ricambi mostra anche catene da neve, lampeggianti e prodotti Paraflu e Motorsil, ma il sito non li elenca: [DA CONFERMARE]. [Certo]

**Mezzi e macchine** citati: auto, autocarri e veicoli industriali, macchine movimento terra, trattori e macchine agricole, impianti oleodinamici, pompe a vuoto, reparti produttivi (aria e fumi). [Certo]

**Marchi elencati dal sito** (citabili per nome come marchi trattati; per i loghi serve la conferma di distributore o l'autorizzazione, vedi LEGGIMI):
- piede e home: Coopers Fiamm (Sogefi), Starline, Donaldson, Virgis Filter, Fleetguard (Cummins), Castrol, Vipiemme;
- pagina Marchi: MP Filtri, Argo Hytos, Filtrec, MANN-Filter, SF Filter, UFI Filters (ex Sofima), HIFI Filter, Sogefi Group, Parker (logo Parker Racor), HYDAC, GFT Filter, Baldwin, FAAM;
- portale B2B: "DISTRIBUTORI GFT FILTERS" (l'unico marchio per cui l'azienda si dichiara distributore, oltre a "rivenditore autorizzato" Castrol).
Nella foto della piramide si leggono anche Hengst, Delphi, Iveco, Wix e Hydac Ecomicron, che il sito però non elenca come marchi trattati. [Certo]

**Listini scaricabili** ancora pubblici: Coopers Fiamm, Donaldson, Fleetguard e MANN in PDF del novembre-dicembre 2015 (`/wp-content/uploads/2015/..`). Nella libreria media ci sono anche Starline, Virgis, Castrol (ottobre 2015) e FBN. Il link al catalogo Virgis 2016 dà 404. Sono prezzi di undici anni fa. [Certo]

**Come si ordina oggi**: il professionista si registra sul portale B2B e ordina dopo il login. Gli altri canali sono telefono, WhatsApp, email e il modulo di contatto. Non c'è un modo di chiedere un codice o un equivalente, né una ricerca per codice o per mezzo sul sito pubblico. Ritiro al banco: le condizioni sono EXW, e la foto IMG_1589 mostra un banco vendita. Orari del banco [DA CONFERMARE]. [Certo]

**Resi** (PDF "Resi per Errata Ordinazione" del portale, `_prova/crawl/politica-resi.pdf`): si chiedono "SOLO tramite l'area dedicata "Gestione RMA"" del portale oppure a resi@centrofiltriveneto.com. Il rimborso è pieno entro 30 giorni dalla consegna; fra 30 e 60 giorni si trattiene il 15%, con un minimo di 5 euro. Sugli articoli sotto i 20 euro si addebitano 5 euro fissi. Non si rendono i filtri Baldwin, i filtri "Clean" e gli articoli ordinati apposta. Il testo parla di articoli "venduti e spediti": oltre al ritiro, CFV spedisce [Probabile; modalità e zone DA CONFERMARE].

## Immagini

Inventario completo: `_prova/inventario-immagini.json` (92 file in `assets/originali/`, scaricati dalla libreria media REST e dalle pagine, alla risoluzione massima disponibile; uno è 404).

| Tipo | N. | Misure | Giudizio | Uso nella nuova home |
|---|---|---|---|---|
| Piramide di filtri (`home_factory_slider_bg.jpg`, doppione `section_bg`) | 1 | 4032x3024, 3,5 MB | **foto vera** (iPhone 6s, 21/07/2016), nitida al 100%, scontornata su bianco; circa 40 filtri di forme e marche diverse | la foto più forte: dice "abbiamo tutto" in un colpo d'occhio; ritagli per breakpoint, mai ingrandita |
| Magazzino (`magazzino_centrofiltriveneto.jpg`) | 1 | 3813x2471 | **foto vera** (Nikon D3100, 14/01/2017), buona, corsia centrale con scaffali pieni | prova del "4000 in pronta consegna"; fascia fino a 1900 px |
| Banco con tre persone (`IMG_1589.jpg`) | 1 | 4032x3024 | **foto vera** (iPhone 6s, 14/05/2016), discreta: neon piatto, rumore | mezza larghezza; persone e banco da rifotografare [DA CONFERMARE chi sono, consenso] |
| Sede (`azienda.jpg`, `home_factory_subheader.jpg`) | 2 | 1060x614, 1415x435 | scarsa, ha l'aspetto di un fotogramma Street View | solo riferimento; da rifare |
| Logo orizzontale (`centrofiltriveneto_logo.png`) | 1 | 2440x305, PNG trasparente | buono | testata; chiedere il vettoriale |
| Marchio tondo "CFV" sole giallo (`centrofiltriveneto_logo_big.png`) | 1 | 639x379 | buono | è l'insegna sulla sede; favicon, timbro |
| Loghi dei marchi | 30 | 63-1280 px, raster | piccoli, misti | solo con autorizzazione; meglio i vettoriali ufficiali o i nomi in testo |
| Foto promozionali dei produttori (Mann, Donaldson, Fleetguard, Sogefi, Baldwin, Parker, FAAM, Castrol, collage) | 15 | 500-3843 px | materiale dei produttori | non sono foto dell'azienda; no |
| Illustrazioni delle famiglie (escavatore e trattore, idraulici, separatori, filtri a tasche, ricambi, chimica) | 8 | 350-1255 px | scontorni da cataloghi o dal web, origine ignota, bassa qualità | no |
| Demo del tema Betheme Factory (icone gialle, ritratti stock "our_team", sfondi, BeFACTORY) | 25 | | demo | no; i 4 ritratti stock non sono persone dell'azienda |

Cosa manca: foto attuali della sede e dell'insegna, del banco con le persone, del magazzino di oggi, di filtri singoli per famiglia (pesante, idraulico, separatore, tasche aria) su fondo neutro e di un furgone in consegna, se c'è. Le foto 2016-2017 vanno bene per una proposta, ma hanno nove-dieci anni.

## Colori, logo, caratteri

- Logo: scritta "Centro Filtri Veneto" in nero corsivo neretto su sei pennellate oblique che passano da ocra (#E9C177) e crema (#F4E1BC, #FBF5E8) ad azzurro (#DBECFC, #9FCCF4) e blu **#0099E1**. Il marchio tondo è un sole giallo **#FEED00** con "CFV". Insegna e furgone usano la stessa grafica. [Certo, colori misurati sui PNG]
- Sito: testata blu notte #192533, fascia #324968, giallo pieno **#FFF000** con un nastro zebrato giallo e nero (della demo Factory), grigio #F4F5F7. Caratteri Roboto e, caricati senza uso evidente, Lato, Open Sans, Indie Flower e Oswald. [Certo]
- Il giallo e il nero sono già dell'azienda (sole del logo, insegna): un colore deciso che si può tenere senza inventarlo.

## Problemi tecnici (misure del 18/10/2026)

Chromium (Playwright) a 1440x900 e 390x844 come telefono, cache vuota. File: `_prova/attuale/misure.json`, screenshot `NN-pagina-1440.png`, `-390.png`, `-schermata.png`.

1. **Home pesante**: 6.796 KB in 55 richieste, evento load a 4,5 s (1440) e 3,8 s (390). Lo sfondo della piramide pesa da solo 3.549 KB (4032x3024 servito anche al telefono); il riquadro grigio quasi vuoto accanto al blocco giallo è un PNG di 1.124 KB (`WorkshopAir5_Desktop.png`). La pagina Azienda pesa 7.078 KB (magazzino 2.097 KB). [Certo]
2. **Nessun H1 in home**: due H2 ("Centro Filtri Veneto", "Solo 10 minuti da Padova"). Tutte le pagine hanno la stessa meta description. Mancano Open Graph e dati strutturati (LocalBusiness). L'attributo `lang="it-IT"` c'è. [Certo]
3. **Telefono non cliccabile in home**: zero link `tel:` e `mailto:` a 1440 e a 390. Nella pagina Contatti ce n'è uno. Il WhatsApp +39 320 6125425 compare solo nella pagina Contatti. [Certo]
4. **Due numeri diversi**: 049 9801910 ovunque, ma +39 049 9800655 nel riquadro giallo sopra la mappa dei Contatti. [Certo; quale è giusto DA CONFERMARE]
5. **Orari assenti**: il sito e il portale non indicano mai l'orario del banco o del magazzino. [Certo]
6. **Leggibilità**: il testo delle famiglie è a 14 px, grigio #919699 su quasi bianco (contrasto circa 3:1, sotto il 4,5:1 di WCAG AA), con 7 blocchi in testo giustificato e buchi visibili tra le parole (`pezzi/01-home-1440-1.jpg`). Il titolo "Solo 10 minuti da Padova" ha le righe sovrapposte (interlinea più bassa del corpo, a 1440 e a 390). [Certo]
7. **Telefono**: la home a 390 px non sborda (scrollWidth 390), ma è lunga 6.327 px. La piramide è tagliata in alto e il sole "CFV" esce dall'inquadratura. Le cinque famiglie vanno in colonna, con illustrazioni a tutta larghezza e spazi vuoti di circa 200 px tra una e l'altra. [Certo]
8. **Menu E-COMMERCE**: la voce porta a una categoria WordPress vuota ("Uncategorized", "admin"). RICAMBISTI va al portale, PRIVATI a un dominio che non risponde. Chi cerca "dove ordino" trova tre strade, due delle quali non portano a niente. [Certo]
9. **Contenuti lasciati a metà**: la pagina di esempio `/about/` ("This is an example of a WordPress page...") è pubblica e in sitemap. C'è un lorem ipsum nella pagina Filtrazione. Ci sono due link 404 nel piede di ogni pagina (Coopers Fiamm, Starline) e il link Argo Hytos porta alla pagina Virgis. Nella pagina Marchi c'è un'immagine rotta accanto al blocco giallo (`pezzi/03-marchi-1440-0.jpg`). [Certo]
10. **Modulo di contatto rotto**: nel modulo dei Contatti e in quello di ogni pagina di marchio il codice "[recaptcha]" appare come testo, perché lo shortcode non viene interpretato. Il modulo non chiede il consenso privacy. La mappa Google dei Contatti dà "This page can't load Google Maps correctly" (ApiProjectMapError) e la copre la scritta "For development purposes only". [Certo]
11. **Privacy e cookie**: non ci sono informativa privacy, informativa cookie né banner sul sito principale. Google Analytics (`analytics.js`, proprietà Universal `UA-31305350-1`, dismessa da Google nel 2023) e Google Fonts si caricano subito su ogni pagina; i Contatti fanno 38 richieste (1440) e 22 (390) a domini Google Maps prima di qualsiasi consenso. Il portale B2B ha invece banner e informativa. [Certo]
12. **Dati societari**: P.IVA e C.F. sono nel piede di ogni pagina. Mancano REA, capitale sociale e PEC (`centrofiltriveneto@pec.it`, da aziende.it). [Certo]
13. **Tecnologia ferma**: PHP 7.4.33, fuori supporto dal novembre 2022, WordPress 6.0.15, Slider Revolution 6.4.11 e il plugin "recent-tweets-widget". Il dominio senza www e quello in http fanno un redirect 301 corretto. robots.txt contiene solo un crawl-delay per Bing. [Certo]
14. **Listini del 2015 pubblici**: quattro PDF di prezzi (Coopers Fiamm, Donaldson, Fleetguard, MANN) linkati dalle pagine dei marchi, del novembre-dicembre 2015. [Certo]
15. **Portale B2B non usabile da telefono**: manca il meta viewport, la pagina è larga 1170 px a 390, il contenuto non appare e i testi sono a 11,2 px; 8,7 MB in 115 richieste, con un solo script da 6,1 MB. [Certo]
16. **Immagini**: nessuna è mostrata più grande del naturale a 1440. Il problema è l'opposto: sono servite troppo grandi. [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Centro Filtri Veneto S.r.l. (sigla CFV) | sito; VIES ("CENTRO FILTRI VENETO SRL") |
| P.IVA e C.F. | 04320460274, valida al 18/10/2026 | VIES REST `ec.europa.eu/taxation_customs/vies`; `_prova/crawl/esterne/vies.json` |
| REA | VE-401159, CCIAA di Venezia | aziende.it (aggiornato al 07/07/2026) |
| Iscrizione | 17/02/2016; il sito dice "fondata nel 2015", operativa da gennaio 2016 | aziende.it; pagina L'azienda |
| Storia | prosegue l'attività della "Casa del Filtro Veneta" nella stessa sede; "specialisti che lavorano dal 1985" | sito (home, L'azienda) |
| Forma, capitale | S.r.l., capitale sociale 20.000 euro | aziende.it |
| ATECO | 46.86.9 commercio all'ingrosso di altri prodotti intermedi | aziende.it |
| Fatturato | 5.220.578 euro nel 2024 (+10,5%), utile 211.065 euro | aziende.it, dal bilancio 2024 |
| Dipendenti | 18 (fascia 10-19) | aziende.it |
| Certificazione | ISO 9001:2015, TÜV Rheinland, ID 9000034903; ambito: "Wholesale of filters for transportation vehicles, materials and goods handling, spare parts for cars, motorbikes, transportation vehicles and materials handling in general." | Certipedia `certipedia.com/quality_marks/9000034903`; marchio sul portale B2B; scadenza [DA CONFERMARE] |
| Sede | Via del Lavoro 30, 30030 Vigonovo (VE), località Tombelle | sito; VIES |
| Telefono | 049 9801910; fax 049 504099; WhatsApp +39 320 6125425; nei Contatti compare anche 049 9800655 | sito |
| Email | info@centrofiltriveneto.com, amministrazione@centrofiltriveneto.com | sito |
| PEC | centrofiltriveneto@pec.it | aziende.it [verificare su INI-PEC] |
| Social | facebook.com/centrofiltriveneto (risponde, ma va fatto il login per vederla) | sito |
| E-commerce | `ecommerce.centrofiltriveneto.com` (B2B Proger ClipParts, login, dati TecDoc); `cfvfilter.com` per i privati, non raggiungibile | sito; prove in `_prova/crawl/` |
| Condizioni di vendita | EXW; 10 euro + IVA di spese di gestione sulle fatture differite sotto i 100 euro + IVA; versione del 21/02/2025 | PDF del portale |
| Resi | entro 30 giorni dalla consegna, via area RMA del portale o resi@centrofiltriveneto.com | PDF del portale |
| Dominio | centrofiltriveneto.com, registrato il 19/10/2015, scade il 19/10/2027, DNS Netsons | RDAP Verisign |
| Orari | non pubblicati da nessuna parte | [DA CONFERMARE] |
| Google | scheda "Centro Filtri Veneto" presente sulla mappa in Via del Lavoro; il pannello con orari, voto e numero di recensioni non si è caricato e la ricerca Google ha risposto con il controllo anti-robot | [DA CONFERMARE] |

## URL vecchi (per i redirect, se poi si rifà tutto il sito)

`/`, `/lazienda/`, `/marchi-prodotti/`, `/marchi-prodotti/filtrazione/`, le 12 pagine `/marchi-prodotti/<marchio>/` (sogefi-group, filtrec, donaldson-filtration-solutions, virgis-filter, mann-filter, fleetguard-cummins-filtri, mp-filtri, hi-fi-filter, sofima-filter, sf-filter, baldwin-filters-2, parker-filters), `/contatti/`, `/about/` (da togliere), `/category/uncategorized/`, i PDF in `/wp-content/uploads/2015/11/` e `/2015/12/`.

## Da confermare col cliente

- Orari del banco e del magazzino; se c'è il ritiro al banco per i privati.
- Quale numero è giusto tra 049 9801910 e 049 9800655; se il fax serve ancora.
- Stato di `cfvfilter.com` (negozio per i privati?) e del portale B2B (l'avviso "ClipParts temporaneamente sospeso" è nascosto, ma c'è).
- Elenco attuale dei marchi trattati e per quali c'è un contratto di distribuzione, prima di mostrare i loghi. Accumulatori: Vipiemme o FAAM? Starline e Coopers Fiamm hanno pagine 404.
- Scadenza del certificato ISO 9001 e permesso di usare il marchio TÜV in home.
- Se "dal 1985" si può dire così (Casa del Filtro Veneta), e il nome di chi c'era.
- Consegna con mezzi propri o corriere, zone servite, tempi: oggi le condizioni dicono solo EXW.
- Chi sono le tre persone della foto al banco e se sono d'accordo a comparire; foto nuove della sede e del magazzino.
- Logo in vettoriale; colori ufficiali (blu #0099E1 e giallo #FEED00 misurati sui PNG).
- Recensioni Google (voto e numero) e PEC su INI-PEC.

## Fonti e file di lavoro

- Crawl in `_prova/crawl/`: pagine `.html` e testo `.txt`, `pages.json` e `media-*.json` (REST WordPress), sitemap, `links-stato.txt`, testi e PDF del portale B2B. Le fonti esterne sono in `esterne/`: VIES, aziende.it, Certipedia, RDAP, tentativo Google Maps.
- Script in `_prova/script/`: `testo.py`, `misura.cjs`, `dettagli.cjs`, `ecom*.cjs`, `gmaps*.cjs`, `provino.py`, `inventario.py`.
- Screenshot in `_prova/attuale/` (pezzi tagliati in `pezzi/`), provini delle immagini in `_prova/provini/`.
- Non raggiungibili da questa sessione: `cfvfilter.com` (timeout e reset), pannello di Google Maps e ricerca Google (anti-robot), Facebook (login), reportaziende e ufficiocamerale (429/403), Overpass e crt.sh (errore di rete).
