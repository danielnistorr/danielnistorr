# 01. Analisi del sito attuale (www.albergovescovi.com)

Analisi del 6 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).

Materiale di lavoro: pagine scaricate in `_prova/crawl/pagine/`, testi estratti in `_prova/crawl/testi/`, libreria media completa (126 file) in `_prova/crawl/media/`, misure Playwright in `_prova/attuale/misure-1440.json` e `misure-390.json`, screenshot in `_prova/attuale/NN-pagina-1440|390.png`, inventario immagini in `_prova/inventario-immagini.json`.

## In breve

- **Che cos'è.** Hotel 3 stelle con ristorante e centro benessere in Via Don Viero 80 ad Asiago, nella Piana Ave a 900 m dal centro. Lo gestisce **Albergo Vescovi Fabio S.r.l.** (P.IVA 04435970241), la stessa società dell'Albergo Rendola e del Centro Rendola (bowling, pizzeria, sala giochi) in Via Rendola 41. [Certo]
- **Il sito.** WordPress **4.9.3** (febbraio 2018) con tema Llorix One Lite + figlio "One Edge", Elementor 1.9.0, Elementor Pro 1.12.2, Contact Form 7 4.9.2, Yoast 6.1: tutto fermo al 2017-2018. Fatto e ospitato da **Persefone.it**, che fornisce anche il motore di prenotazione. [Certo]
- **Il difetto più visibile.** Ogni pagina (anche le sitemap e le API JSON) comincia con un errore PHP, prima del `<!DOCTYPE>`: *Warning: "continue" targeting switch is equivalent to "break"... in /home/mhd-01/www.albergovescovi.com/htdocs/wp-includes/pomo/plural-forms.php on line 210*. A 390 px si legge in cima a ogni pagina (screenshot), a 1440 resta sotto la barra fissa. Il browser va in modalità quirks (`document.compatMode = BackCompat`) e la sitemap non è XML valido. [Certo]
- **Contenuti fermi.** La pagina Ristorante contiene ancora il testo segnaposto di Elementor ("Sono un blocco di testo... Lorem ipsum") dal 27 dicembre 2017; la home dichiara **45 camere**, il registro regionale ne conta **24 (39 posti letto)**. Mancano P.IVA, CIN, privacy e cookie policy. [Certo]
- **Il materiale vero sta su Booking.** Le foto del sito sono di 1024x768 (camere, 2018), 900 px (spa), 800x600 (piatti). La scheda Booking.com dell'hotel ha invece un **servizio fotografico professionale di 31 scatti a 3000x1996** (camere rinnovate, ristorante, reception, spa, facciata) più 6 foto a 2000-3000 px: scaricate in `assets/esterne/`. Con quelle si può fare un sito a tutta larghezza; senza, no. [Certo per le dimensioni, DA CONFERMARE che le foto siano del cliente]
- **Prenotazioni.** Il pulsante PRENOTA porta (dopo due redirect, il primo in http) al motore Persefone `https://www.booking-engine.it/Scripts/index.pl?hotel_id=53`; in home c'è anche il widget `widget.booking-engine.it/maschera.php?hotel_id=53`. Il nuovo sito deve usare lo stesso motore. [Certo]

## Pagine esistenti

Elenco completo dalla sitemap Yoast (`/index.php/page-sitemap.xml`, 10 URL) e dall'API `/index.php/wp-json/wp/v2/pages` (10 pagine pubblicate, nessun articolo). [Certo]

| Pagina | URL | Pubblicata / modificata | Stato |
|---|---|---|---|
| Home | `/` | 27/12/2017, mod. 24/10/2025 | testata con foto di Asiago, testo di benvenuto, centro benessere (foto stock), 3 camere, ristorante, loghi contributi |
| Camere | `/index.php/camere/` | 27/12/2017, mod. 22/06/2018 | testo + carosello + 3 blocchi Doppia, Tripla, Quadrupla |
| Doppia | `/index.php/camere/doppia/` | 09/01/2018 | galleria di 15 foto, superficie, servizi in camera |
| Tripla | `/index.php/camere/tripla/` | 09/01/2018 | galleria, superficie, servizi |
| Quadrupla | `/index.php/camere/quadrupla/` | 09/01/2018, mod. 19/06/2018 | galleria, superficie, servizi |
| Ristorante | `/index.php/ristorante/` | 27/12/2017, mai modificata | testo segnaposto Lorem ipsum + 6 foto di piatti a 300 px |
| Centro benessere | `/index.php/centro-benessere/` | 27/12/2017, mod. 22/06/2018 | testo, orari, prezzo, 3 riquadri con foto |
| Contatti | `/index.php/contatti/` | 27/12/2017, mod. 09/01/2018 | indirizzo, telefono, fax, mappa Google, modulo |
| Progetto POR FESR | `/index.php/progetto-por-asse-3-competitivita-dei-sistemi-produttivi/` | 21/06/2021 | pagina obbligatoria di pubblicità del contributo, con barra laterale WordPress predefinita (Accedi, RSS, WordPress.org) |
| CSR 2023-2027 | `/index.php/complemento-regionale-lo-sviluppo-rurale-2023-2027/` | 24/10/2025 | pagina obbligatoria del contributo GAL, stessa barra laterale |

Menu: Home, Camere, Centro benessere, Ristorante, Contatti. Barra in alto: "Contattaci: +39 0424 462614" e icona Facebook (`facebook.com/AlbergoVescovi`). Piede: indirizzo, "Centro benessere", menu, banner POR FESR, "Powered by Persefone.it". Solo italiano, nessuna versione in altre lingue (il registro regionale dichiara inglese e francese parlati).

## Testi reali (verbatim, con i refusi originali)

Home:
1. Titolo e sottotitolo della testata: "Hotel Vescovi" / "Benvenuti"; pulsante "PRENOTA". Testo nascosto per lettori di schermo nello stesso pulsante: **"Etichetta del pulsante nella Testata:PRENOTA"** (segnaposto del tema mai sostituito).
2. "Se pensate ad una vacanza in un luogo tranquillo, lontano dai rumori del traffico ma vicinissimo al centro della città, l'albergo Vescovi fa al caso Vostro. Un moderno hotel di tre stelle situato in una delle zone più suggestive di Asiago, dispone di 45 camere alcune con balcone, servizi privati, TV, telefono diretto con l'esterno; sauna finlandese, ascensore, garage e parcheggio privato."
3. "Aperto stagionalmente o su prenotazione anche in altri periodi dell'anno, offre ai suoi ospiti un soggiorno ideale ed un ottimo servizio frutto di una lunga tradizione alberghiera. L'hotel Vescovi situato a 900 metri dal centro di Asiago immerso nel verde della piana Ave, comodo anche per passeggiare nei boschi, è un ambiente familiare per farvi trascorrere nel migliore dei modi il Vostro soggiorno in montagna."
4. "Centro benessere": Sauna finlandese, Vasca idromassaggio, Docce emozionali, Bagno turco, Tisaneria, Zona relax, Palestra.
5. "Le nostre camere": "Doppia: Camera in stile classico con TV a schermo piatto e bagno privato." / "Tripla: Camera tripla con TV a schermo piatto." / "quadrupla: Camera quadrupla con TV a schermo piatto." Pulsanti "dettaglio".
6. "Il nostro ristorante": "Lasciati trasportare dai sapori della nostra cucina tradizionale. I nostri piatti sono prepari con amore dal nostro chef." Pulsante "Scopri i nostri piatti".

Camere:
7. "Il nostro hotel dispone di 45 camere alcune con balcone, kit con servizi privati, TV a schermo piatto, telefono diretto con l'esterno, ascensore, Wi-FI, bagno con doccia e/o vasca."
8. "Offriamo stanze sia mansardate con travi a vista e moquette sia in stile classico con parquet."
9. "Dal balcone esterno è possibile godere di un'ottima vista del paese di Asiago e la piana ave con la sua distesa di prati."
10. "DOPPIA: Camera in stile classico con TV a schermo piatto e bagno privato. Possibilità di stanze comunicanti per famiglie." TRIPLA e QUADRUPLA ripetono "Camera in stile classico con TV a schermo piatto e bagno privato."

Doppia, Tripla, Quadrupla:
11. Doppia: "bagno privato / Superficie camera 16 m² / Camera in stile classico con TV a schermo piatto e bagno privato. / Siete pregati di specificare la tipologia di letto desiderata al momento della prenotazione. / Servizi in camera: asciugacapelli,scrivania, prodotti da bagno in omaggio, WC, bagno privato,riscaldamento, vasca o doccia, TV a schermo piatto,armadio/guardaroba, bidet,asciugamani, biancheria per la casa,carta igienica, lettini e culle per bambini / WiFi gratis!"
12. Tripla: "Superficie camera 20 m² / Camera tripla con TV a schermo piatto." Stessi servizi più "piani superiori accessibili tramite ascensore".
13. Quadrupla: "Superficie camera 30 m² / Camere di 30 m²." Servizi con "vasca o/e doccia" e "lettini e culle per bambini."

Ristorante:
14. "Sono un blocco di testo. Fai clic sul pulsante modifica per cambiare questo testo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo." (unico testo della pagina, più 6 foto di piatti)

Centro benessere:
15. "Il nostro centro benessere è dotato di sauna finlandese all'eucalipto, bagno turco di vapore, vasca idromassaggio, zona relax, docce emozionali, tisaneria e frutta fresca. La spa è aperta dal 7 luglio ed è disponibile per gli ospiti del hotel su prenotazione durante il pomeriggio dalle ore 15:00 fino alle 19:00 ad un costo di € 10 di supplemento che comprende accappatoio e e ciabatte in spugna."
16. "Idromassaggio: Uno dei principali benefici idromassaggio è senza dubbio la capacità di sciogliere lo stress e le tensioni muscolari dal corpo. Merito delle bollicine gassose che a contatto con la cute provocano un naturale micromassaggio in grado di stimolare la circolazione e donare una piacevole sensazione di relax."
17. "Doccia emozionale: Dopo una seduta di sauna l'ideale è il Bucket Shower di origine tirolese prevede che un getto di acqua gelata contenuto in un secchio "appeso" al soffitto e rovesciato tramite una catenella venga versato in modo improvviso sul corpo, in modo da creare uno shock termico per l'organismo talmente forte da irrobustirlo."
18. "Bagno Turco: Il bagno turco è un ambiente chiuso con umidità tra il 90 e il 100% e una temperatura di 50°C. favorisce una profonda pulizia e purificazione della pelle"

Contatti e piede:
19. "Albergo Vescovi / Via Don Viero, 80 36012 Asiago (VI) – Italy / Tel. 0424.462614 / Fax 0424.462840". Modulo: "Il tuo nome (richiesto)", "La tua email (richiesto)", "Oggetto", "Il tuo messaggio", casella "Accetto privacy" senza collegamento a nessuna informativa, pulsante "Invia".
20. Piede: "Centro benessere / Scopri il nostro centro benessere. / Vai alla pagina"; "Powered by Persefone.it".

Pagine contributi (da conservare, vedi Problemi):
21. POR FESR: "ASSE 3 "Competitività dei sistemi produttivi" / AZIONE 3.3.4/B-Sostegno alla competitività delle imprese nelle destinazioni turistiche attraverso interventi di qualificazione dell'offerta e innovazione di prodotto/servizio, strategica ed organizzativa. / Titolo del progetto: ALTOPIANO ACTIVE TOURS". Segue l'elenco dei 12 partecipanti della rete scritto senza spazi ("i partecipantiALBERGO COL DEL SOLE SNC DI VALENTE ANTONIO E PESAVENTO A- RIANNAALLEVATORI ALTIPIANO...", tra cui "ALBERGO VESCOVI DI VESCOVI DOMENICO") e 7 obiettivi ("essere più facilmente individuati dal turista rispetto ai competitors che non aderiscono al Club", "Incrementare l'occupazione delle camere"...).
22. CSR 2023-2027: "Codice intervento: ISL03 / Nome intervento: Investimenti extra agricoli in aree rurali / Descrizione operazione: Acquisto di nuove attrezzature / Finalità: Incentivare lo sviluppo di attività imprenditoriali extra agricole nelle aree rurali [...] / Risultati ottenuti: Efficientamento energetico e miglioramento dell'offerta commerciale / Tipo di sostegno: Rimborso delle spese ammissibili / Importo finanziato: 35.752,50 euro".

Motore di prenotazione Persefone (`booking-engine.it`, hotel_id=53), testi visibili:
23. "Sito ufficiale: Miglior prezzo garantito"; "Tripla: 20 Mq | Max adulti: 3"; "Doppia: 16 Mq | Max adulti: 2"; "Quadrupla: 23 Mq | Max adulti: 4" con descrizione "Superficie camera 30 m²". Servizi elencati: Aria condizionata, Bagno in camera, Minibar, Free wifi, Parcheggio gratis, Cassaforte (Tripla, Quadrupla), Doccia, Colazione inclusa (Doppia, Quadrupla), Vasca bagno e Accesso disabili (Doppia).

Refusi e incoerenze da non riportare: "prepari con amore" (preparati), "Wi-FI", "piana ave" minuscolo, "benefici idromassaggio" (dell'idromassaggio), "accappatoio e e ciabatte", "ospiti del hotel", periodo della doccia emozionale senza verbo principale, "favorisce" minuscolo dopo il punto, "kit con servizi privati", virgole senza spazio nei servizi in camera, "Camere di 30 m²." nella Quadrupla, "quadrupla" minuscolo in home, accenti doppi nel titolo POR ("Competitività̀", "più̀": un carattere U+0300 in più), nomi dei partecipanti incollati. Il nome compare come "Albergo Vescovi", "Hotel Vescovi", "albergo Vescovi", "hotel Vescovi": il registro regionale usa **ALBERGO VESCOVI**, Google e Booking **Hotel Vescovi**, il logo in testata dice "Hotel Vescovi" [DA CONFERMARE quale nome usare come principale].

Incoerenze di dati, tutte [DA CONFERMARE]:
- Camere: **45** (home, Camere, Yesalps: 10 doppie, 23 triple/quadruple, 12 familiari) contro **24 camere e 39 posti letto** nel registro regionale delle strutture ricettive (6/10/2026).
- Quadrupla: 30 m² (sito) contro 23 m² (motore di prenotazione, che nella stessa scheda scrive anche "Superficie camera 30 m²").
- Distanza dal centro: 900 m (sito), 1 km (Booking).
- "La spa è aperta dal 7 luglio": anno non indicato, testo del 2018.
- Aria condizionata: dichiarata dal motore di prenotazione e dal registro, mai nominata dal sito.

## Cosa fanno o vendono

Soggiorni in albergo 3 stelle ad Asiago, Altopiano dei Sette Comuni. Dalle fonti [Certo se non indicato]:
- **Camere** doppie (16 m², max 2 adulti), triple (20 m², max 3), quadruple (30 m² sul sito, max 4); "stanze sia mansardate con travi a vista e moquette sia in stile classico con parquet", alcune con balcone sulla piana; stanze comunicanti per famiglie; lettini e culle; TV, telefono, Wi-Fi, bagno con doccia o vasca, cassaforte e minibar secondo il motore di prenotazione.
- **Centro benessere** per gli ospiti: sauna finlandese all'eucalipto, bagno turco, vasca idromassaggio, docce emozionali, tisaneria con frutta fresca, zona relax, palestra; su prenotazione dalle 15:00 alle 19:00, supplemento di 10 euro con accappatoio e ciabatte (testo 2018, [DA CONFERMARE] orario e prezzo attuali).
- **Ristorante** di cucina tradizionale. Piatti fotografati sul sito: tagliatelle con verdure, minestra, pasta lunga al ragù, affettati e formaggio, spezzatino con polenta, stinco con patate, soppressa con polenta e formaggio. Nessun menu, nessun orario, nessun prezzo pubblicato. Le foto Booking mostrano due sale (una con stufa e perline, una grande con vetrate sui prati), una sala gialla con camino, bar e reception in abete, terrazza.
- **Servizi**: ascensore, garage e parcheggio privato (sito); colazione inclusa (motore di prenotazione); secondo il registro regionale anche servizio navetta, area fitness, animali ammessi, aria condizionata. Secondo portali terzi (Booking, Yesalps), da confermare: colazione a buffet dolce e salata, escursioni d'estate, sala giochi d'inverno, colonnina di ricarica per auto elettriche, cucina senza glutine e senza lattosio, pranzi al sacco, cani ammessi.
- **Apertura**: "Aperto stagionalmente o su prenotazione anche in altri periodi dell'anno" [DA CONFERMARE i periodi].
- **Prenotazione diretta** sul motore Persefone, che si presenta come "Sito ufficiale: Miglior prezzo garantito". Su Booking.com l'hotel ha 7,1/10 su 931 recensioni (6/10/2026): dato pubblico, da non riportare sul sito senza accordo col cliente.
- **Rete e contributi**: partecipante alla rete "Altopiano Active Tours" (POR FESR 2014-2020, turismo attivo: cicloturismo, trekking, orienteering, sci di fondo, escursionismo invernale) e beneficiario di 35.752,50 euro dal Complemento regionale per lo sviluppo rurale 2023-2027 tramite GAL Montagna Vicentina, per "Acquisto di nuove attrezzature" con risultato "Efficientamento energetico e miglioramento dell'offerta commerciale".

## Immagini usate oggi

La libreria media ha 126 file. 49 sono del tema demo e foto stock (compresa la foto della sauna in home), una trentina sono doppioni e ritagli delle stesse foto (camion, nave, stella marina, sciatori, coppie, persone in spa, ritratti, "Choose your image"): restano in `_prova/crawl/media/` e non si usano. Le immagini dell'azienda sono copiate con nomi parlanti in `assets/originali/` (43 file), quelle della scheda Booking in `assets/esterne/` (37 file, `manifest.json` con URL, data e provenienza). Per ognuna `_prova/inventario-immagini.json` dà soggetto, misure, nitidezza misurata e larghezza massima mostrabile.

| Tipo | Quantità | Misure | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Camere, foto del 2018 caricate su Booking e riprese dal sito (ID tipo 87318580) | 12 | 1024x768, una 1024x512 | nitide ma piccole: **massimo 1024 px**, cioè mezza colonna a 1440 e niente retina oltre 512 px CSS; arredi vecchi (moquette, copriletti a righe) | schede camera solo se le camere sono ancora così [DA CONFERMARE] |
| Bagni 2018 | 6 | 1024x768; `DSCN0125` doccia 4608x3456 | buoni, uno ad alta risoluzione; 2 mostrano il bagno vecchio | dettaglio nelle schede |
| Spa (IMGP4810, 4813, 4814 + idromassaggio 600x450) | 4 | 900x598, 900x1355, 600x450 | piccole e con luci colorate; oggi IMGP4810 è **ingrandita a 1105 px** (naturale 900) | sostituibili con le foto Booking |
| Piatti (IMG_3239...3266) | 7 | 800x600, stinco 2000x1203 | foto da telefono con flash su piatti quadrati; **massimo 800 px** | griglia piccola, oppure foto nuove |
| Esterno d'estate dal prato (`header.jpg`) | 1 | 2000x1020 | buona, non usata nelle pagine | apertura (meglio la versione Booking 3000x2250) |
| Panorama della piana con l'hotel (`header-2.jpg`) | 1 | 2000x600 | buona, striscia larga | fascia panoramica |
| Asiago d'inverno al tramonto (`asiago2.jpg`, oggi sfondo della testata) | 1 | 1600x1066 | buona, autore ignoto (salvata con Picasa) | solo se il cliente conferma che è sua [DA CONFERMARE] |
| Cresta innevata da telefono, 3/3/2015 | 1 | 1600x898 | discreta | fondo secondario |
| Foto della sauna in home (`centrpbenessere.jpg`) | 1 | 600x425 | con ogni probabilità stock, non è la sauna dell'albergo [Probabile] | non usare |
| Logo tondo "Hotel Vescovi" con monte e tre stelle | 4 file | PNG 4000x4000, PSD 3000x3000 a un solo livello raster | verde bosco #293F1C, verde oliva #727949; scontorno con alone semitrasparente, **manca il vettoriale** | favicon; da ridisegnare in SVG |
| Logo gotico "Hotel Vescovi" in testata + 3 stelle gialle #EEE43E | 4 varianti | PNG 2000x1000 | in uso a 230x115 px, ombre sporche | da ridisegnare o sostituire [DA CONFERMARE quale logo è quello ufficiale] |
| Loghi dei contributi e banner POR FESR | 2 | 688x116, 2830x1219 | obbligatori; il banner ha il testo chiuso nell'immagine | pagina contributi e piede |
| **Booking.com, servizio fotografico** (ID 501760528...501794427) | 31 | 3000x1996 o 1996x3000 | luce pulita, grandangolo, camere rinnovate in abete chiaro e pietra, ristorante, reception, spa, facciata; nitidezza misurata: dettaglio vero fino a circa **2250 px** (orizzontali) e 1500 px (verticali) | il materiale principale del nuovo sito, previa conferma |
| Booking.com, altre | 6 | 3000x2250 (esterno estate, facciata con dehors, 3 bagni già sul sito a 1024), 2000x1500 (hotel nella neve) | buone | aperture stagionali |

Abbinamento foto-tipologia: il motore Persefone usa 9 foto del 2018 (768x576) divise per Doppia, Tripla e Quadrupla, ma l'ordine nell'HTML non permette di dire con certezza quale gruppo va con quale camera; le foto professionali Booking non hanno didascalia di tipologia. [DA CONFERMARE col cliente quali camere sono rinnovate e di che tipo]

Foto non scaricate: 1 foto della scheda Google Maps (4032x3024, caricata da un utente con una recensione il 5/5/2025, materiale di terzi); Facebook visibile solo con login; Tripadvisor risponde 403. La Wayback Machine (web.archive.org) non è raggiungibile dalla nostra rete: nessuna versione precedente al 2017 consultata [DA CONFERMARE se esiste un sito più vecchio con altro materiale].

## Problemi tecnici da segnalare al cliente

Misure con Chromium (Playwright) il 6/10/2026; tempi presi attraverso il nostro proxy, utili per confrontare le pagine tra loro più che come tempo assoluto di un ospite in Italia.

| Pagina | Richieste (1440) | Peso (1440) | Caricamento 1440 | Caricamento 390 | Larghezza pagina a 390 |
|---|---|---|---|---|---|
| Home | 67 | 2,3 MB | 5,1 s | 4,9 s | 390 px |
| Camere | 63 | **28,3 MB** | 4,2 s | 5,2 s | 390 px |
| Doppia | 57 | 1,6 MB | 4,2 s | 4,3 s | **435 px** |
| Tripla | 51 | 1,3 MB | 3,2 s | 3,6 s | **435 px** |
| Quadrupla | 49 | 1,2 MB | 3,6 s | 4,3 s | **439 px** |
| Ristorante | 45 | 0,8 MB | 3,4 s | 3,6 s | 390 px |
| Centro benessere | 46 | 1,3 MB | 3,5 s | 3,5 s | 390 px |
| Contatti | 84 | 1,4 MB | 3,8 s | 3,8 s | **402 px** |
| POR FESR | 27 | 0,7 MB | 3,2 s | 5,4 s | 390 px |
| CSR 2023-2027 | 26 | 0,7 MB | 3,2 s | 3,1 s | 390 px |

1. **Errore PHP in cima a ogni pagina.** Il messaggio *Warning: "continue" targeting switch is equivalent to "break"* con il percorso del server (`/home/mhd-01/www.albergovescovi.com/htdocs/...`) è il primo contenuto di ogni risposta: pagine HTML, `/index.php/wp-json/...` e sitemap. Prove: `_prova/attuale/01-home-390.png` (righe in alto), `curl https://www.albergovescovi.com/ | head -2`. Effetti misurati: modalità quirks su tutte le pagine (`document.compatMode = "BackCompat"`), sitemap `page-sitemap.xml` non valida come XML ("junk after document element"). Causa: WordPress 4.9.3 su una versione di PHP più recente. [Certo]
2. **Software fermo al 2018.** WordPress 4.9.3 (generatore nella pagina e `/readme.html` pubblico), Elementor 1.9.0, Elementor Pro 1.12.2, Contact Form 7 4.9.2, Yoast SEO 6.1, jQuery 1.12.4. Per tutte queste versioni sono uscite da anni correzioni di sicurezza. Il nome utente dell'amministratore è leggibile da `/index.php/wp-json/wp/v2/users`; `wp-login.php` e `xmlrpc.php` sono aperti. Il sito dell'Albergo Rendola, della stessa società, è su WordPress 6.9.9. [Certo]
3. **Pagina Camere da 28,3 MB.** La foto `DSCN0125.jpg` (4608x3456, 6,8 MB) è caricata **4 volte** dal carosello per essere mostrata a 172x200 px. Su rete mobile la pagina è inutilizzabile. Prova: `_prova/crawl/reqs/misure-1440.json`. [Certo]
4. **A 390 px quattro pagine escono dallo schermo.** Doppia, Tripla e Quadrupla sono larghe 435-439 px (Doppia 450 e Quadrupla 454 px senza lo zoom del telefono) perché l'elenco dei servizi è scritto senza spazi dopo le virgole e "biancheria per la casa" non va a capo; Contatti è larga 402 px per i campi del modulo (`size="40"`). Il telefono rimpicciolisce la pagina e il piede risulta più stretto del resto. Prova: `_prova/attuale/03-doppia-390.png`. [Certo]
5. **Testo segnaposto pubblicato.** Ristorante: solo "Sono un blocco di testo... Lorem ipsum" dal 2017 (`06-ristorante-1440.png`). Home: il pulsante PRENOTA viene letto dai lettori di schermo come "Etichetta del pulsante nella Testata:PRENOTA". Le pagine dei contributi mostrano la barra laterale predefinita di WordPress (Cerca, Commenti recenti vuoto, Archivi vuoto, "Nessuna categoria", Meta con "Accedi" e "WordPress.org"): `09-por-fesr-1440.png`. [Certo]
6. **Prenotazione.** Il pulsante PRENOTA punta a `http://phpbookinghotel.it/4055-vescovi/check1.php...` (http, non https), che rimanda a `https://www.booking-engine.it/Scripts/index.pl?hotel_id=53`. In ogni pagina la barra di navigazione carica uno script dallo stesso indirizzo vecchio che ora risponde con una pagina HTML: il browser lo blocca (`net::ERR_BLOCKED_BY_ORB`, misurato su tutte e 10 le pagine), quindi quella maschera non compare mai. In home il widget nuovo (`widget.booking-engine.it`, hotel_id=53) è una barra fissa in basso alta 134 px a 1440 (15% della finestra) e 116 px a 390, con fondo grigio semitrasparente sopra il testo di benvenuto, e inserisce 4 script con `document.write` che bloccano il caricamento (avvisi in console). [Certo]
7. **Contenuto misto http.** Home e Centro benessere chiedono immagini in http (`IMG_3266.jpg`, `IMGP4810/4813/4814.jpg`): 2 e 6 avvisi "Mixed Content" in console. Le `og:image` di Doppia, Tripla e Ristorante puntano a `persefone.net/vescovi/...`, il dominio del fornitore. [Certo]
8. **Immagini.** 10 immagini su 11 senza testo alternativo in home, 7 su 8 nel Ristorante; la foto della spa `IMGP4810.jpg` (900 px) è mostrata a 1105 px; il logo in testata è un PNG di 2000x1000 mostrato a 230x115; il banner POR (2830x1219, 273 KB) è mostrato a 255x110 in ogni pagina. Nessuna foto delle camere supera 1024 px. [Certo]
9. **Caratteri.** Le pagine chiedono a Google Fonts quattro famiglie (Roboto, Roboto Slab, Roboto Condensed, Playfair Display) in 18 stili ciascuna: 463 KB di font in home, icone comprese. [Certo]
10. **Dati obbligatori mancanti.** In nessuna pagina compaiono ragione sociale, **P.IVA**, sede legale o PEC (obbligo per chi ha partita IVA), né il **CIN** IT024009A19GB3I2IC, il codice identificativo nazionale che le strutture ricettive devono esporre negli annunci dal 2025 [Probabile che valga anche per il sito, DA CONFERMARE]. Nessun copyright né anno. Il sito dell'Albergo Rendola, invece, li riporta in fondo pagina. [Certo]
11. **Privacy e cookie.** Nessuna informativa privacy, nessuna cookie policy, nessun banner. Il modulo Contatti ha la casella "Accetto privacy" senza collegamento a un'informativa. Senza alcun consenso la pagina Contatti carica Google Maps (`maps.google.com`, `maps.googleapis.com`, `places.googleapis.com`) e tutte le pagine caricano font da `fonts.googleapis.com`. Nel nostro test non sono stati salvati cookie. [Certo]
12. **SEO.** Nessuna meta description in nessuna pagina; due H1 per pagina (il logo è un H1 "Albergo Vescovi"), tre in home; titolo della home "Home - Albergo Vescovi"; tutti gli URL contengono `/index.php/`; `/robots.txt` e `/sitemap.xml` danno 404 (la sitemap vera è `/index.php/sitemap_index.xml`, non valida per l'errore del punto 1); nessun dato strutturato da hotel (solo `WebSite`). [Certo]
13. **Testi chiusi in immagini.** Banner "Progetto finanziato con il POR FESR 2014-2020 Regione del Veneto, Vai ai dettagli" e striscia dei loghi CSR; il logo stesso. Il resto è testo vero. [Certo]
14. **Contenuti fermi.** Ristorante non modificata dal 27/12/2017, Contatti dal 09/01/2018, Camere e Centro benessere dal 22/06/2018; la home è stata toccata il 24/10/2025 solo per aggiungere i loghi dei contributi. "La spa è aperta dal 7 luglio" senza anno. Le foto delle camere sono del 2018 mentre su Booking ci sono camere rinnovate. [Certo]
15. **Cose che funzionano.** HTTPS attivo con certificato Let's Encrypt valido fino all'11/11/2026, sia per `www` sia per il dominio nudo; `http://` rimanda a `https://www` (dal dominio nudo in due passaggi). Viewport mobile dichiarato (`width=device-width, initial-scale=1`), menu a hamburger a 390, nessun link interno rotto (58 link controllati: solo redirect 301 e il 302 di Facebook verso il login). [Certo]

Obblighi da non perdere nel nuovo sito: le due pagine dei contributi (POR FESR 2014-2020 e CSR 2023-2027 con GAL Montagna Vicentina) sono pubblicità obbligatoria dei finanziamenti ricevuti e vanno mantenute con i loghi, raggiungibili dalla home. [Probabile, DA CONFERMARE la durata dell'obbligo col cliente]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Albergo Vescovi Fabio S.r.l. (scritta anche "S.R.L.") | piede di albergorendola.it; paginebianche.it |
| Insegna | Albergo Vescovi / Hotel Vescovi, 3 stelle | sito; registro regionale; Google; Booking |
| P.IVA e C.F. | 04435970241 | piede di albergorendola.it ("C.F. e P.IVA 04435970241 - SDI WTYVJK9") |
| Codice SDI | WTYVJK9 | stesso |
| Sede | Via Don G. Viero, 80, 36012 Asiago (VI) | piede di albergorendola.it; registro regionale. Paginebianche scheda la società in Via Rendola 41 (sede dell'Albergo Rendola) |
| PEC | albergovescovifabiosrl@pec.it | piede di albergorendola.it |
| Telefono | 0424 462614 (+39 0424 462614) | sito; registro regionale; motore di prenotazione |
| Fax | 0424 462840 | sito |
| Email | info@albergovescovi.com | registro regionale; motore di prenotazione (non scritta sul sito) |
| CIN | IT024009A19GB3I2IC | registro regionale delle strutture ricettive, dati.veneto.it, aggiornato 6/10/2026 |
| Camere e posti letto | 24 camere, 39 posti letto (registro) contro 45 camere (sito) | [DA CONFERMARE] |
| Servizi nel registro | ristorante, parcheggio non custodito, aria condizionata, sauna, area fitness, animali ammessi, servizio navetta; inglese e francese parlati; niente piscina | registro regionale |
| Posizione | Piana Ave, 900 m dal centro; coordinate Google 45.86642, 11.50932 | sito; Google Maps |
| Scheda Google | "Hotel Vescovi", con risposte firmate "Hotel Vescovi (Proprietario)" [Probabile che sia rivendicata] | Google Maps |
| Social | facebook.com/AlbergoVescovi (solo con login); nessun Instagram trovato | sito |
| Orari | spa 15:00-19:00 su prenotazione (testo 2018); reception, check-in, check-out, ristorante e periodi di apertura non pubblicati | [DA CONFERMARE] |
| Anni di attività | non pubblicati. Il sito parla di "lunga tradizione alberghiera"; nel 2021 la rete Altopiano Active Tours elencava "ALBERGO VESCOVI DI VESCOVI DOMENICO", probabile ditta precedente | [DA CONFERMARE anno di apertura e storia della famiglia] |
| Altre attività della società | Albergo Rendola (Via Rendola 41, 3 stelle, 53 camere, 158 posti letto, CIN IT024009A1HPQMGI7E) e Centro Rendola: sala da tè, Hunger Burger, bowling a 8 piste, sala giochi, ristorante e pizzeria | albergorendola.it; registro regionale |
| Dimensione | fatturato 2025 1.605.836 euro, 35 dipendenti secondo la ricerca preliminare (ufficiocamerale.it, pagina ora 403); la ricerca web riporta 1.316.942 euro e 29 dipendenti per il 2024. Dati della società, quindi dei due alberghi insieme | [DA CONFERMARE, non per il sito] |
| Fornitore del sito e del motore | Persefone.it; motore `booking-engine.it`, hotel_id=53 (vecchio indirizzo `phpbookinghotel.it/4055-vescovi`) | sito; motore |
| Marchi e certificazioni | nessuno dichiarato | |

## URL vecchi

Tutti da mantenere con redirect 301 in `plugin/redirect-301.csv`. Il nuovo sito, se toglie `/index.php/`, deve reindirizzare ogni indirizzo qui sotto. La destinazione finale si decide in 03.

| URL vecchio | Stato oggi | Destinazione proposta |
|---|---|---|
| `/` | 200 | `/` |
| `/index.php/camere/` | 200 | `/camere/` |
| `/index.php/camere/doppia/` | 200 | `/camere/` (sezione Doppia) o pagina camera |
| `/index.php/camere/tripla/` | 200 | `/camere/` (sezione Tripla) o pagina camera |
| `/index.php/camere/quadrupla/` | 200 | `/camere/` (sezione Quadrupla) o pagina camera |
| `/index.php/ristorante/` | 200 | `/ristorante/` |
| `/index.php/centro-benessere/` | 200 | `/centro-benessere/` |
| `/index.php/contatti/` | 200 | `/contatti/` |
| `/index.php/progetto-por-asse-3-competitivita-dei-sistemi-produttivi/` | 200 | pagina contributi (conservare) |
| `/index.php/complemento-regionale-lo-sviluppo-rurale-2023-2027/` | 200 | pagina contributi (conservare) |
| `/index.php/doppia/`, `/index.php/tripla/`, `/index.php/quadrupla/` | 301 alle schede camera | come sopra |
| `/index.php/pagina-di-esempio/` | 301 a `/` | `/` |
| `/?p=2`, `/?p=46`, `/?p=90`, `/?p=93`, `/?p=95`, `/?p=150`, `/?p=192`, `/?p=193`, `/?p=344`, `/?p=348` | 301 (shortlink WordPress) | pagina corrispondente (2 home, 46 contatti, 90 camere, 93 ristorante, 95 centro benessere, 150 doppia, 192 tripla, 193 quadrupla, 344 POR, 348 CSR) |
| `/index.php/feed/`, `/index.php/comments/feed/`, `/index.php/pagina-di-esempio/feed/` | 200 | `/` |
| `/index.php/sitemap_index.xml`, `/index.php/page-sitemap.xml` | 200 (XML non valido) | nuova sitemap |
| `/wp-content/uploads/2017/12/...`, `/2018/01/...`, `/2018/06/...`, `/2021/06/...`, `/2025/10/...` | 200 (126 file, elenco in `_prova/crawl/media-urls.txt`) | facoltativo: le immagini più usate verso le nuove |
| pagine allegato (`/0001-jpg/` e simili, 126 indirizzi in `_prova/crawl/url-allegati.txt`) | già 404 | nessuno |

Indirizzi esterni da aggiornare: il pulsante PRENOTA e ogni link di prenotazione vanno puntati direttamente a `https://www.booking-engine.it/Scripts/index.pl?hotel_id=53` (oggi passano da `http://phpbookinghotel.it/4055-vescovi/check1.php`); il widget nuovo è `https://widget.booking-engine.it/maschera.php?hotel_id=53&...`.

Fonti: www.albergovescovi.com (pagine, API WordPress, sitemap); motore www.booking-engine.it (hotel_id=53); registro "Elenco delle Strutture Ricettive Turistiche della Regione Veneto" su dati.veneto.it (CSV del 6/10/2026, `_prova/crawl/fonti/strutture-ricettive-veneto.csv`); albergorendola.it (piede); paginebianche.it; booking.com/hotel/it/vescovi.it.html; yesalps.com; Google Maps.
