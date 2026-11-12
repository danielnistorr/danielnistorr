# 01. Analisi del sito attuale (www.lavoro-salute.it)

Analisi del 18 ottobre 2026. Legenda: **[Certo]** visto nella fonte, **[Probabile]** inferenza forte, **[DA CONFERMARE]** da verificare con il cliente (va nel LEGGIMI).

## In breve

- Lavoro & Salute srl, Via S. Felice e Fortunato 26, 35010 Limena (PD), P.IVA 04074830284, capitale sociale 40.000 euro. Società "costituita nel 2006" che fa due mestieri sotto lo stesso tetto: **medicina del lavoro e sicurezza per le aziende** (medico competente, sorveglianza sanitaria, formazione D.Lgs 81/2008, DVR e indagini ambientali, tarature e certificazioni) e un **poliambulatorio privato** su appuntamento con 13 specialità elencate. Amministratore dal 2006 e direttore sanitario (secondo un PDF del 2016) è il Dott. Marco Lo Savio, medico del lavoro ed esaminatore aeromedico ENAC. [Certo]
- La home attuale è già "a due porte": una foto di stock di una scrivania azzurra con la cartellina al centro, il logo, una frase e due bottoni, **LAVORO** (arancio) e **SALUTE** (blu). Dietro ci sono due siti diversi nello stesso WordPress: Salute con testata orizzontale blu, Lavoro con colonna laterale arancio. [Certo]
- Il sito è un tema comprato (**MediGroup** di Mikado Themes, 2016) su **WordPress 5.3.26**, WPBakery, Slider Revolution 6.1.7 e **WooCommerce 4.0.4**, messo in piedi nel marzo 2020 senza togliere la demo: **54 delle 147 pagine in sitemap sono ancora in inglese con "Lorem ipsum"** (dentista, veterinario, oculista, "Contact info" con indirizzo di New York e telefoni finti, negozio con 15 creme e occhiali in sterline). Sono tutte pubbliche e indicizzabili. [Certo]
- **Non c'è nessuna foto della struttura.** Le uniche foto vere sono il logo (PNG a 3368 px) e i ritratti di 7 medici, di qualità molto diversa (dalla Leica Q2 di Lo Savio al ritratto sgranato di Di Nino). Tutto il resto, 73 foto, è stock generico: elicotteri del 118, provette, pance, martelletti da giudice, la Basilica del Santo. [Certo]
- Problemi misurati: testo grigio #959595 su bianco (contrasto 3,0:1, sotto il minimo 4,5:1) su tutte le pagine; nessun numero di telefono cliccabile (`tel:` assente in tutto il sito); home pesante 1,1 MB e 97 richieste per 42 parole; Google Maps caricata prima del consenso (44 richieste a Google sulla pagina Salute); informativa privacy del 2003 con il dominio sbagliato (`salute-lavoro.it`); numeri promozionali non verificabili ("3247 Pazienti Soddisfatti", "15 Anni di Esperienza" fermo al 2021); testi di medicina estetica con promesse e nomi commerciali di farmaci. [Certo]

## Pagine esistenti

Sitemap Yoast (`/sitemap_index.xml`, 14 sotto-sitemap): 109 pagine, 5 articoli, 7 medici, 6 reparti, 16 prodotti, 29 portfolio della demo. Copie in `_prova/crawl/pagine/` (HTML), `testi/` (testo estratto), `corpo/` (solo contenuto). Le pagine vere sono queste:

| Area | Pagina | URL | Contenuto | Ultima modifica (sitemap) |
|---|---|---|---|---|
| Ingresso | Home "Welcome" | `/` | logo, frase "costituita nel 2006", bottoni LAVORO e SALUTE su foto stock | 10/03/2020 |
| Salute | Poliambulatorio | `/salute/` | slider (2 foto stock), tre colonne "Medici Qualificati / 14 Specializzazioni / 15 Anni di Esperienza", visite a domicilio, 13 servizi a schede, notizie (2013-2015), carosello dei medici, contatori, modulo "Fissa appuntamento" con campi in inglese, mappa | 10/03/2020 |
| Salute | 13 specialità | `/chirurgia/` `/dermatologia/` `/cografiae/` (sic, è la diagnostica ecografica) `/fisiatria/` `/ginecologia/` `/aeronautica/` `/estetica/` `/legale/` `/oculistica/` `/ortopedia/` `/otorinolaringoiatria/` `/psicologia/` `/dietologia-e-scienze-dellalimentazione/` | descrizione della disciplina, elenco prestazioni, "I nostri specialisti" | 09/03/2020 (fisiatria 30/06/2026) |
| Salute | Carta dei servizi | `/carta_servizi/` | principi, diritti e doveri del paziente | 09/03/2020 |
| Salute | Medici | `/doctor/dott-marco-losavio/` `/doctor/dottssa-stefania-bano/` `/doctor/dott-ivan-turco/` `/doctor/dott-arcangelo-di-nino/` `/doctor/dott-ssa-raffaella-riviezzo/` `/doctor/dott-ssa-loreta-greco/` e l'archivio `/doctor/` | curriculum lunghi | 2020, Lo Savio 29/06/2026, Greco e Riviezzo 30/06/2026 |
| Salute | Reparti | `/department/{dermatologia,fisiatria,medicina-del-lavoro,medicina-legale,otorinolaringoiatria,venereologia}/` | solo il medico collegato | 2020-2026 |
| Lavoro | Area aziende | `/lavoro/` | slider, tre colonne, 5 servizi a schede, contatori "67 / 82 / 347", download di 2 PDF, modulo "Lavora con noi" con curriculum | 10/03/2020 |
| Lavoro | Servizi | `/formazione/` `/formazionefinanziata/` `/formazionegratuita/` `/corsiprimosoccorso/` `/medicinadellavoro/` `/sorveglianzasanitaria/` `/medicinalavoropd/` `/medicinalavorovi/` `/sicurezza/` `/altriservizi/` | testi di servizio, due pagine "Padova" e "Vicenza" quasi identiche (scritte per la ricerca locale) | 10/03/2020 |
| Notizie | 5 articoli | `/online-il-nuovo-sito/` (2013) `/formazione-finanziata/` (2013) `/corso-di-primo-soccorso-aziendale/` (2013) `/partenership-con-aziende-turistiche/` (2015) `/prevenzione-del-melanoma/` (2015) | ultimo articolo del 13/03/2015 | 2013-2015 |
| Legale | Privacy e cookie | `/privacy-policy/` | condizioni d'uso con registrazione utenti, D.Lgs 196/2003 | 10/04/2020 |
| Demo | 54 pagine | `/dentist-home/` `/veterinarian-home/` `/contact-page/` `/shop/` `/product/...` `/elements/...` `/about-us/` `/working-hours/` `/pricing-packages/` ... | Lorem ipsum in inglese | 2016 |

Menu Salute: "Home / Poliambulatorio / News / Chi Siamo / Contatti / Pagina Iniziale", tutte ancore della stessa pagina `/salute/#...`: non esistono pagine Chi siamo e Contatti. Menu Lavoro: "Home / Servizi / Download / Lavora con noi / Pagina iniziale". Nella testata Salute c'è anche un carrello WooCommerce "0 items £0.00". [Certo]

PDF pubblicati (in `_prova/crawl/pdf/`): `docum_mecessaria_visita_ame_2016.pdf` (documenti per la visita di idoneità al volo, intestato "POLIAMBULATORIO, DIRETTORE SANITARIO: Dott. Lo Savio Marco", con fax e capitale sociale), `modulo-richiesta-visita-medicina-aeronautica.pdf` (modulo ENAC del 2013), `primo_soccorso.pdf` (allegati del DM 388/2003), `Accordo_21-12-2011_formazione_lavoratori.pdf` (scansione di 21 pagine, superato dal nuovo Accordo Stato-Regioni del 2025). [Certo]

## Testi reali (verbatim, con i refusi originali)

Home:
1. "Lavoro & Salute è una società costituita nel 2006 con l’obbiettivo di fornire ad aziende e cittadino servizi medici e consulenza in materia di sicurezza sul lavoro."
2. Bottoni: "LAVORO" / "SALUTE". Titolo della pagina: "Welcome - Lavoro & Salute".

Testata e piede:
3. Salute: "Lunedì - Venerdì 09:00 - 19:00 / Sabato e Domenica - CHIUSO", "+ 39 049 88 43 927 / info@lavoro-salute.it", "Via S. Felice e Fortunato 26 / 35010 - Limena (PD)", "Seguici su :".
4. Lavoro: "Lun - Ven 09:00 - 12:30 / Lun - Ven 14:30 - 19:00", "Seguici su".
5. Piede: "Lavoro & Salute srl - P.iva : 04074830284", "Privacy & Cookies Policy", "Made with [cuore] by Iacopo Trezzi".

Salute (`/salute/`):
6. "Medici Qualificati / Le persone vengono Prima": "I medici che collaborano con la Struttura sono disponibili per le visite negli orari di apertura del Poliambulatorio prendendo appuntamento in sergreteria."
7. "14 Specializzazioni / Al Servizio del Paziente": "L’attività del Poliambulatorio prevede la possibilità di avere la refertazione degli esami istologici nell’eventualità vengano fatte delle biopsie e la possibilità di effettuare gli esami del sangue su appuntamento."
8. "15 Anni di Esperienza / In Continuo Aggiornamento": "Il Poliambulatorio Lavoro & Salute è autorizzato del 2006 ed ha incrementato le specialità autorizzate avvalendosi di nuovi specialisti per offrire un servizio completo all’utenza."
9. "Scegli con Tranquillità / Il Posto ideale in cui ricevere le dovute attenzioni": "Le visite specialistiche possono essere prenotate direttamente presso la segreteria del Poliambulatorio o chiamando il numero 049.8843927 dal lunedì al venerdì dalle 9,00 alle 12,30 e dalle 14,30 alle 19,00."
10. "A Tua Disposizione / I nostri pazienti vengono prima": "Il Poliambulatorio è disponibile, per gli utenti che non sono in grado di raggiungere la struttura, la programmazione della visita a domicilio."
11. "I Nostri Servizi / Leggi la nostra CARTA SERVIZI"; ogni scheda ripete "AFFIDATI A LAVORO & SALUTE ED AI SUOI PROFESSIONISTI QUALIFICATI." e "Leggi di Più".
12. "I Nostri Dottori": "Siamo qui per Te. Questi sono i volti dei professionisti che ti seguiranno in Lavoro&Salute".
13. Contatori: "3247 Pazienti Soddisfatti", "13 Dipartimenti", "75 Servizi Differenti".
14. Modulo: "Siamo qui per te. / Fissa Appuntamento", campi "Select Department / Select Doctor / Your Full Name / Phone / Date / Time / Special request...", bottone "Richiedi".

Lavoro (`/lavoro/`):
15. "Sicurezza sul Lavoro / Le persone vengono Prima": ripete la frase della home.
16. "Servizi alle Aziende / Sempre Aggiornati": "All’interno dell’area sicurezza collaborano tecnici specializzati, medici del lavoro e altri specialisti allo scopo di offrire alle aziende un servizio completo, flessibile ed integrato."
17. "Servizi al Cittadino / Rapidi ed Efficienti": "Il Poliambulatorio offre agli utenti un servizio qualificato e puntuale per fornire le prestazioni di alto livello senza tempi di attesa e a un prezzo contenuto."
18. Contatori: "67 Servizi Differenti", "82 Corsi Organizzati", "347 Attestati Consegnati".
19. "Download / Documentazione utile per i servizi di Lavoro & Salute.": "Cassetta di pronto Soccorso (DM 388/04)", "Accordo Stato Regioni (21 Dicembre 2011)".
20. "Lavora con Noi": specializzazioni "medicina del lavoro / formazione / specialista ambulatoriale / sicurezza sul lavoro", informativa ai sensi del "D.L. n. 196 del 30.06.2003".

Medicina del lavoro (`/medicinadellavoro/`, `/medicinalavoropd/`):
21. "Lavoro & Salute, con l’obbiettivo di fornire alle Aziende un servizio completo in termini di salute e prevenzione, offre ai dipendenti ed ai famigliari la possibilità di usufruire delle prestazioni erogate dal Poliambulatorio a condizioni vantaggiose. Il Poliambulatorio Lavoro & Salute mette a disposizione la propria struttura e gli specialisti che vi collaborano offrendo la possibilità di effettuare le visite specialistiche e i trattamenti medico estetici ad un prezzo vantoaggioso e senza lista di attesa."
22. "ATTIVITA’ DI MEDICINA DEL LAVORO: Incarico Medico Competente; Esecuzione di esami strumentali: Audiometria, Spirometria, Screening visivo, ECG, ecc.; Valutazione clinico-funzionale del: Rachide, Arto superiore; Valutazione ergoftalmologica per gli addetti al videoterminale; Prelievi ematici e raccolta campioni biologici; Gestione completa degli esami di chimica clinica e tossicologica: Test per la verifica di assenza di assunzione alcol e droghe; Formazione addetti al primo soccorso secondo la normativa vigente; Altre visite specialistiche (ortopedica, oculistica, otorino, dermatologica ecc.) presso il nostro Poliambulatorio; Visite ed esami possono essere effettuati presso la sede delle aziende o nei nostri ambulatori."
23. Padova: "Visite mediche preventive e/o per cambio mansione eseguite entro 24 ore dalla comunicazione alla segreteria." "Lavoro & Salute offre la possibilità di effettuare una Convenzione con le aziende che prevede agevolazioni economiche per i dipendenti delle aziende e i loro familiari [...]". Il percorso: Documento di Valutazione dei Rischi, individuazione del medico competente, sopralluogo, programmazione della sorveglianza sanitaria, erogazione (in sede o in azienda), documentazione, riunione periodica ("nelle Aziende con più di 15 dipendenti"), scadenze, consulenze specialistiche, primo soccorso (DM 388/2003), formazione "attraverso la società L&S Formazione e Sicurezza", cartella sanitaria e di rischio, "Gestione rapporti con lo SPISAL".
24. La pagina Vicenza è la copia di Padova e dice ancora "presso i nostri ambulatori di Padova" e "Medicina del Lavoro Padova".

Formazione e sicurezza:
25. Formazione: "Ai sensi dell’articolo 37 del D. Lgs. 81/2008, tutti i lavoratori [...] devono ricevere a cura del proprio datore di lavoro una formazione sufficiente e adeguata in materia di salute e sicurezza." Figure: "Addetti Primo Soccorso / Addetti prevenzione e lotta antincendio / Responsabile Servizio Prevenzione e Prevenzione (RSPP) / Rappresentante dei Lavoratori per la Sicurezza (RLS) / Carrellisti / Pimus / Formazione annuale sulla sicurezza ai dipendenti".
26. Articolo 2013: "corsi di Primo Soccorso per le Aziende classificate nei gruppi A-B-C ai sensi del Decreto Ministeriale 388/2003 della durata di 12-16 ore ed i corsi di aggiornamento della durata di 4-6 ore", "simulazioni con il manichino", "Il Corso si svolgono in Azienda o presso le nostre aule di formazione".
27. Formazione gratuita: "Tutti i costi di Lavoro & Salute – FORMAZIONE E SICUREZZA saranno a carico direttamente del Fondo: la nostra consulenza risulterà, quindi, completamente gratuita per l’azienda." (con il trattino medio, da non riportare).
28. Sicurezza: indagini (movimentazione carichi, fonometrie, rischi elettromagnetici, stress lavoro-correlato, rischio chimico, vibrazioni, collaudi acustici, polveri, amianto), documentazione (DVR, nomine, piani di evacuazione, PIMUS, POS-PSC, registri esposti, DUVRI), autorizzazioni (CPI, scarichi, emissioni), marcatura prodotto, HACCP.
29. Altri servizi: "Taratura degli strumenti di misura / Verifiche impianti messa a terra 462/01 / Attestazione SOA / Rischi 231/01 / Utilizzo razionale dell’energia / Sistemi di gestione ISO 14001 – 9001 – OHSAS 18001 – BRC – ISO TS".
30. Articolo 2015, aziende turistiche: servizio medico per villaggi, campeggi e alberghi, "un medico da un’ora al giorno oppure per tutte le ventiquattro ore", "medici che parlano correntemente inglese, tedesco o francese". Oggi attivo? [DA CONFERMARE]

Specialità (prestazioni elencate, testo completo in `_prova/crawl/corpo/<pagina>.txt`):
31. Diagnostica ecografica: addome superiore, inferiore, completo, pelvica, testicolare, renale, tessuti molli, tiroide, mammaria, prostatica transrettale, intravaginale; Eco Doppler: tronchi sovraortici, aorta addominale, venoso e arterioso arti inferiori.
32. Chirurgia ambulatoriale: "Il centro ha a disposizione un ambulatorio chirugico per interventi che non necessitano di degenza [...] in anestesia locale come ad esempio asportazione di piccoli lipomi o cisti sebacee, nevi, xantelasmi." Visita chirurgica e proctologica, unghie incarnite, flebectomie, verruche, legatura emorroidi.
33. Dermatologia: diagnosi e terapia, "Mappatura mediante dermatoscopia", dermatologia pediatrica, assistenza in gravidanza, crioterapia, diatermocoagulazione, peeling chimico superficiale; venereologia.
34. Ginecologia e ostetricia: visite, pap-test, ecografie pelviche, colposcopia, citologia dell'endometrio, biopsie, HPV, IUD; visite ed ecografie ostetriche.
35. Medicina aeronautica: "Il dott. Marco Lo Savio è Esaminatore Aeromedico (AME) autorizzato da ENAC [...]" per licenze di II classe (PPL, LAPL), equipaggio di cabina, paracadutismo, droni (SAPR); "I tempi per eseguire tutti gli esami previsti sono di circa 30 minuti"; **"Tariffe: Certificazioni Tipo 1-3 Euro 90,00 / Certificazione tipo 2 Euro 65,00"** (unici prezzi del sito; la dicitura "tipo 1-3" è incomprensibile).
36. Medicina estetica: acne, cellulite, rughe, calvizie, biorivitalizzanti, fosfatidilcolina, mesoterapia, filler, tossina botulinica, peeling, luce pulsata.
37. Medicina legale: danno da infortunio e responsabilità civile, responsabilità professionale, INAIL, INPS, invalidità civile, mobbing.
38. Oculistica: 20 prestazioni, tra cui fondo oculare, tonometria, refrazione, "Visita oculistica per il rinnovo patente", idoneità alle lenti corneali.
39. Ortopedia: visita, valutazione posturologica, infiltrazioni articolari, mesoterapia.
40. Otorinolaringoiatria: visite ORL, audiologica e foniatrica, audiometria, impedenzometria, protesi acustiche, acufeni, laringoscopia, vestibolare e manovre liberatorie; "La sezione Audioprotesica".
41. Psicologia e psicoterapia: valutazione neuropsicologica, sostegno individuale, di coppia e alla famiglia.
42. Dietologia e scienze dell'alimentazione: visita, plicometria e bioimpedenziometria, educazione alimentare, diete; nomina il "Dott. Salvatore Iacopetta" e un "servizio analisi interno".
43. Fisiatria: visita, riabilitazione ortopedica e neurologica, prescrizione di terapia fisica, terapia antalgica.

Refusi da non riportare: "obbiettivo", "sergreteria", "autorizzato del 2006", "chirugico", "Polimabulatorio", "Aereonautiche", "in estetismi", "Bio-Rivitalizazzione", "acice" ("protesi acustice"), "vantoaggioso", "legare" (legate), "Qual’ora si necessario", "c’è ne sono", "in’azienda", "Partenership", "Responsabile Servizio Prevenzione e Prevenzione" (e Protezione), "cografiae" nell'indirizzo, "Ginocologia" nel nome del file, maiuscole a caso ("Le persone vengono Prima"), punti dopo i titoli ("Dermatologia."), "D.L. n. 196" (è un D.Lgs), il dominio "salute-lavoro.it" nella privacy. Il nome compare come "Lavoro & Salute", "Lavoro e Salute", "Lavoro&Salute", "L&S": nel nuovo sito si usa **Lavoro & Salute** come nel logo.

## Cosa fanno

Per le aziende (area **Lavoro**), dal 2006: [Certo dal sito]
- **Medico competente e sorveglianza sanitaria**: nomina, sopralluogo, protocollo sanitario, visite preventive, periodiche e per cambio mansione, giudizi di idoneità, cartella sanitaria e di rischio, riunione periodica, scadenzario, rapporti con lo SPISAL. In sede a Limena o in azienda, province di Padova e Vicenza.
- **Esami per la medicina del lavoro**: audiometria, spirometria, screening visivo, ECG, valutazione del rachide e dell'arto superiore, ergoftalmologia per videoterminalisti, prelievi, test alcol e droghe.
- **Formazione** D.Lgs 81/2008: lavoratori, primo soccorso (gruppi A, B, C), antincendio, RSPP, RLS, carrellisti, PIMUS, lavoro in quota; in aula o in azienda; formazione finanziata con i fondi interprofessionali (Fondimpresa citato), con la società o marchio **"L&S Formazione e Sicurezza"** (rapporto con Lavoro & Salute srl [DA CONFERMARE]).
- **Sicurezza**: DVR, DUVRI, POS, PSC, PIMUS, piani di emergenza, indagini ambientali e fonometriche, stress lavoro-correlato, rischio chimico e vibrazioni, pratiche CPI, scarichi, emissioni, HACCP, marcatura.
- **Altri servizi**: tarature, verifiche messa a terra (DPR 462/01), SOA, modello 231, sistemi ISO. Sono probabilmente fatti con partner esterni [DA CONFERMARE se sono ancora offerti].
- **Convenzione aziendale**: condizioni agevolate al poliambulatorio per dipendenti e familiari delle aziende seguite.
- **Cassette di pronto soccorso** e reintegri (DM 388/2003).
- Servizio medico per strutture turistiche (articolo del 2015) [DA CONFERMARE].

Per le persone (area **Salute**, poliambulatorio privato, su appuntamento): [Certo dal sito]
- 13 specialità elencate: chirurgia ambulatoriale, dermatologia (e venereologia), diagnostica ecografica (con eco doppler), fisiatria, ginecologia (e ostetricia), medicina aeronautica, medicina estetica, medicina legale, oculistica, ortopedia, otorinolaringoiatria, psicologia e psicoterapia, scienze dell'alimentazione. Con la medicina del lavoro sono 14, il numero scritto in "14 Specializzazioni".
- Esami del sangue su appuntamento, refertazione istologica delle biopsie, visite a domicilio per chi non può muoversi.
- Prenotazione solo per telefono (049 8843927) o in segreteria; il modulo "Fissa appuntamento" ha campi in inglese e elenca solo 6 reparti (Dermatologia, Fisiatria, Medicina del Lavoro, Medicina Legale, Otorinolaringoiatria, Venereologia).
- Nessun prezzo, tranne i certificati di medicina aeronautica (90 e 65 euro). Nessuna convenzione con il Servizio sanitario nazionale dichiarata: è una struttura privata. [Probabile]

### Medici (fonte: sito; nessuno con orari di presenza)

| Medico | Specialità sul sito | Pagina | Dati dichiarati sul sito | Conferme esterne |
|---|---|---|---|---|
| Dott. Marco Lo Savio | Medicina del lavoro, Medicina aeronautica (AME) | sì, CV lunghissimo | laurea Padova 13/10/1999, specializzazione in medicina del lavoro Padova 19/12/2005, Ordine dei medici di Padova dal 25/01/2000 n. PD-8617, elenco medici competenti del Ministero n. 16735, ENAC AME IT-1012-AME dal novembre 2015, amministratore di Lavoro & Salute dal gennaio 2006; medico competente di scuole e uffici pubblici del Veneto | PDF 2016: "Direttore sanitario: Dott. Lo Savio Marco". Albo FNOMCeO non interrogato [DA CONFERMARE] |
| Dott.ssa Stefania Bano | Dermatologia e venereologia | sì | laurea Padova 22/03/2001 (110 e lode), specializzazione 15/12/2005, Ordine di Padova da aprile 2002; email stefania.bano@lavoro-salute.it | MioDottore: "Lavoro & Salute S.R.L., Via Santi Felice e Fortunato 26, Limena", anche tricologa e medico estetico, 84 recensioni |
| Dott. Ivan Turco | Otorinolaringoiatria | sì | CV con incarichi ULSS 2007-2012, "consulente per Medicina del Lavoro, Poliambulatorio Lavoro e Salute, Limena" | nessuna |
| Dott. Arcangelo Di Nino | Medicina legale | sì | laurea Padova 17/03/2003, Albo di Venezia dal 28/01/2004, specializzazione 19/01/2009, CTU Tribunale di Venezia dal 10/09/2009 n. 122; email "rcangelo.dinino@lavoro-salute.it" (refuso, manca la "a") | nessuna |
| Dott.ssa Raffaella Riviezzo | Fisiatria | sì | laurea Padova 27/03/2000, specializzazione 21/12/2004, Ordine di Padova n. 8842; ambulatorio INAIL alle Terme Preistoriche dal 2009 | nessuna |
| Dott.ssa Loreta Greco | Fisiatria (pavimento pelvico) | sì, aggiunta il 29/06/2026 | laurea Padova 23/07/2018, Ordine di Padova da marzo 2019, specializzazione in medicina fisica e riabilitativa 10/11/2025 | iDoctors: fisiatra in Via Santi Felice e Fortunato 26, riabilitazione del pavimento pelvico 120 euro a seduta |
| Dott.ssa Vuga Ana Grgic | Oculistica | **no**: solo nel carosello di `/salute/` e nella pagina Oculistica | nessun dato; link a un profilo LinkedIn | nessuna. Lavora ancora qui? [DA CONFERMARE] |
| Dott. Salvatore Iacopetta | Dietologia (nominato nel testo) | no | nessuno | nessuna [DA CONFERMARE] |

Specialità senza medico nominato: chirurgia ambulatoriale, diagnostica ecografica, ginecologia, medicina estetica, ortopedia, psicologia. Le pagine di chirurgia, ecografia ed estetica mostrano come "I nostri specialisti" Lo Savio e Bano, che non sono chirurghi né ecografisti: è il blocco predefinito del tema, non un'informazione. [Probabile] Chi fa queste prestazioni oggi è da chiedere [DA CONFERMARE].

## Immagini usate oggi

Inventario completo con soggetto, qualità e uso: `_prova/inventario-immagini.json` (105 file in `assets/originali/`, provini in `_prova/provini/foglio-1..4.jpg`).

| Tipo | Quantità | Dimensioni | Giudizio | Uso nel nuovo sito |
|---|---|---|---|---|
| Logo attuale (segno a S arancio e blu, "LAVORO & SALUTE", "www.lavoro-salute.it") | 3 versioni | PNG trasparente 3368x2382; 400 px; segno 250 px | buono, colori misurati: blu **#214194**, arancio **#E94E1B**, nero per l'indirizzo | logo e colori del nuovo sito; manca il vettoriale (ridisegnare in SVG o chiederlo) |
| Loghi storici "Poliambulatorio Lavoro & Salute" e "L&S Formazione Sicurezza" | 1 | 2413x600 | grafica vecchia, colori diversi | solo documento |
| Ritratti dei medici | 7 (+ doppioni) | Lo Savio 2270x2705 (Leica Q2, 2022); Greco 1179x1795 (2026); Bano, Riviezzo, Turco, Di Nino, Grgic 600x541 | Lo Savio e Greco buoni; Bano e Riviezzo discreti; Turco compresso; Di Nino sgranato e sovra-nitido; Grgic è un autoscatto inclinato. Fondi tutti diversi (bianco, azzurro, arancio, marrone) | ritratti piccoli e uniformati nel taglio; brief per ritratti nuovi tutti uguali (stesso fondo, stessa luce) |
| Foto dermatoscopio su neo | 1 | 3821x2067, Nikon D600, 27/12/2012 | buona; usata nell'articolo "Prevenzione del melanoma" | se è della struttura, è l'unica foto clinica vera [DA CONFERMARE chi l'ha scattata] |
| Testate e schede delle specialità (stock) | 45 | 2400x800 (velate di bianco) e 800x580 | generiche, molte fuori tema: elicottero del 118 per la medicina aeronautica, laboratorio con provette per la medicina legale, Basilica del Santo e panorama di Vicenza per la medicina del lavoro | nessuno; licenza sconosciuta |
| Sfondi home e slider (stock) | 6 | 1920x1080-1200 | scrivania azzurra della home, mano che scrive, riunione dall'alto | nessuno |
| Immagini della demo MediGroup | 4 | 800-1920 px | infermiera con anziana, mani, medici con velo blu: immagini del tema, non licenziate per il cliente come foto proprie | nessuno |
| Vecchio sito 2013-2015 (stock con scritte) | 14 | 980x445 | pance, post-it, iniezioni, aereo | nessuno |
| Icone 30x30 dei servizi | 16 | 30x30 | grafica del tema | nessuno |

**Cosa manca, e serve**: la facciata e l'ingresso di Via S. Felice e Fortunato 26, la segreteria, la sala d'attesa, gli ambulatori (ecografo, poltrona ORL, cabina audiometrica, lettino chirurgico), l'aula di formazione, un sopralluogo in azienda, le persone della segreteria. Il nuovo sito deve reggersi su logo, colori, tipografia, ritratti e informazione finché non ci sono queste foto; il brief va nel LEGGIMI. Nessuna foto vera della struttura è pubblicata online (sito, Google, MioDottore). La scheda Google ha foto proprie? [DA CONFERMARE: la galleria di Maps non è leggibile da qui].

## Problemi tecnici da segnalare al cliente

Misure del 18/10/2026 con Chromium (Playwright) a 1440x900 e a 390x844 come iPhone, cache vuota per pagina, rete attraverso un proxy (i tempi sono quindi indicativi, i pesi no). File: `_prova/attuale/misure.json`, screenshot `_prova/attuale/NN-pagina-1440.png`, `-390.png`, `-schermata.png`, pezzi in `_prova/attuale/pezzi/`. Script: `_prova/script/misura.cjs`, `vista.cjs`.

1. **Mezzo sito è ancora la demo del tema.** 54 pagine su 147 della sitemap sono in inglese con "Lorem ipsum", tutte pubbliche e senza `noindex`: `/contact-page/` mostra "Office@Medigroup.com", "34th Avenue New York", "EMERGENCY CONTACT (Free call 24/7) +123 655 655"; `/shop/` vende 15 prodotti di cosmetica e occhiali in sterline ("Balancing Cleanser £24.99"); `/working-hours/`, `/pricing-packages/` ("Save up to 40%"), `/dentist-home/`, `/veterinarian-home/`. In testata Salute c'è il carrello "0 items £0.00". Prova: `09-contact-page-1440.png`, `10-shop-1440.png`, `_prova/crawl/sitemap/`. [Certo]
2. **Testo poco leggibile.** Il testo di base è Open Sans 14 px grigio #959595 su bianco: contrasto **3,0:1** (WCAG AA chiede 4,5:1) su tutte le pagine. Nell'area Lavoro il testo bianco sta su un riquadro grigio #B2B2B2: **2,1:1**. A 390 px la frase della home è a **11 px**. Prova: `misure.json` (`fontBody`, `piccoli`), `03-lavoro-1440.png`. [Certo]
3. **Telefono non cliccabile.** Nessun link `tel:` in tutto il sito (0 su 147 pagine) e nessun `mailto:`. A 390 px il numero non compare nella prima schermata di Salute né di Lavoro: si vedono solo hamburger, logo e una foto stock. Per un poliambulatorio che prenota solo per telefono è il difetto più costoso. Prova: `02-salute-390-schermata.png`, `03-lavoro-390-schermata.png`. [Certo]
4. **Home vuota e pesante.** La home ha 42 parole, nessun H1, nessuna meta description, ma carica **1,1 MB in 97 richieste** (Slider Revolution, WooCommerce, mappa Google) per mostrare una foto e due bottoni. A 390 px la foto finisce a 585 px e sotto resta una fascia bianca. La pagina Salute pesa **4,2 MB in 176 richieste** (4,5 MB a 390), Lavoro 3,0 MB in 153. Evento load tra 5 e 10 secondi attraverso il proxy. Prova: `01-home-390.png`, `misure.json`. [Certo]
5. **Due siti diversi nello stesso sito.** Salute ha testata blu orizzontale, Lavoro una colonna laterale arancio e il piede spostato a destra; i due menu non si parlano e quello di Salute porta solo ad ancore della stessa pagina ("Chi siamo" e "Contatti" non sono pagine). Orari diversi tra le due aree: "Lunedì - Venerdì 09:00 - 19:00" (testata Salute) contro "09:00 - 12:30 / 14:30 - 19:00" (testata Lavoro e testo delle prenotazioni). [Certo; orario vero DA CONFERMARE]
6. **Numeri e promesse non verificabili.** Contatori "3247 Pazienti Soddisfatti", "13 Dipartimenti", "75 Servizi Differenti" (Salute) e "67 Servizi Differenti", "82 Corsi Organizzati", "347 Attestati Consegnati" (Lavoro); "15 Anni di Esperienza" scritto nel 2020-2021 e mai aggiornato; "14 Specializzazioni" accanto a un elenco di 13; "senza tempi di attesa e a un prezzo contenuto", "prestazioni di alto livello", "senza lista di attesa", "entro 24 ore". Per la comunicazione sanitaria sono da togliere (vedi 03-norme). [Certo]
7. **Medicina estetica: testi a rischio.** Nomi commerciali di farmaci ("Il Botulino (vistabex)", "lipostabil"), promesse ("il trattamento è ben tollerato e non è doloroso", "Non vi sono controindicazioni all’uso della tossina", "naturale e privo di effetti collaterali", "la pelle diventerà morbida e senza peli superflui per parecchio tempo", "decisamente più giovane"); in dietologia "ti aiuteranno a risolvere tutti i problemi legati all’alimentazione". Vanno riscritti o tolti, non ripresi. [Certo]
8. **Privacy e cookie.** La mappa Google si carica prima di qualsiasi consenso: 44 richieste a domini Google sulla pagina Salute (www.google.com 11, maps.googleapis.com 22, maps.gstatic.com, places.googleapis.com), 6 anche sulla home. Il banner "Utilizzando il sito, accetti l'utilizzo dei cookie" è il vecchio consenso implicito, senza "Rifiuta". L'informativa cita il D.Lgs 196/2003 e non il Regolamento UE 2016/679, parla di "www.salute-lavoro.it" (dominio sbagliato), di registrazione utenti con password che non esiste, di Google Analytics e StatCounter che nel sito non ci sono. I moduli "Fissa appuntamento" e "Lavora con noi" (con caricamento del curriculum) raccolgono dati senza informativa aggiornata e il primo chiede data e motivo della visita. La chiave API di Google Maps è pubblica e non autorizzata al Geocoding (errore in console su `/contact-page/`). Prova: `misure.json` (`domini`, `console`). [Certo]
9. **Tecnologia ferma al 2020.** WordPress 5.3.26 (ramo del 2019), WooCommerce 4.0.4, Slider Revolution 6.1.7, WPBakery, tema MediGroup del 2016, plugin "eu-cookie-law". 16 avvisi di contenuto misto per pagina (logo chiamato in `http://`). Errore JavaScript e immagine di testata 404 (`doctors-profile-title-parallax.jpg`) nelle pagine dei medici. L'endpoint pubblico `/wp-json/wp/v2/users` elenca i nomi utente (Giech79). `/wp-login.php` raggiungibile. Il dominio senza www (`lavoro-salute.it`) risponde in http con un 302 verso www, ma in https chiude la connessione: il certificato Let's Encrypt copre solo `www.lavoro-salute.it`. [Certo]
10. **SEO di base debole.** Nessuna meta description sulle pagine vere (Yoast installato ma vuoto), nessun H1 su home, Salute e Lavoro; titoli "Salute - Lavoro & Salute", "Welcome - Lavoro & Salute"; dati strutturati solo generici di Yoast (nessun `MedicalClinic` o `Physician`); 54 pagine demo indicizzabili; due pagine Padova e Vicenza quasi identiche; alt vuoti o "mkd-team-image" sui ritratti, "a" sul logo. [Certo]
11. **Contenuti vecchi.** Ultima notizia del 13/03/2015, la prima "Online il nuovo sito" del 2013 è ancora in home Salute; il PDF dell'Accordo Stato-Regioni del 2011 è superato; il modulo ENAC è del 2013. Sulla pagina Lavoro i social sono anche link vuoti (`https://www.facebook.com/`, `https://www.youtube.com/`, `https://twitter.com/`). [Certo]
12. **Moduli e lingua.** Il modulo di prenotazione è in inglese ("Select Department", "Your Full Name", "Special request..."), elenca 6 reparti su 13 specialità e la Venereologia come reparto a sé. Non è stato inviato (regola della campagna). [Certo]
13. **Immagini.** Nessuna immagine ingrandita oltre la misura naturale a 1440 (controllo su `misure.json`); il problema non è la risoluzione ma il contenuto: zero foto della struttura, 73 foto di stock. Il ritratto di Di Nino è mostrato a 600 px da solo su una riga del carosello, sgranato (`pezzi/02-salute-1440-3.jpg`). [Certo]
14. **Nota sugli screenshot.** Nelle catture a pagina intera le fasce con sfondo in parallasse (notizie, contatori) e la mappa escono vuote, con il testo bianco su grigio: è un difetto della cattura, non del sito. Le stesse fasce fotografate a finestra fissa sono a posto: `02-salute-1440-notizie.png`, `02-salute-1440-contatori.png` (la mappa mostra "Poliambulatorio Lavoro & Salute, 4,3 stelle, 6 recensioni"). [Certo]

## Dati aziendali

| Dato | Valore | Fonte |
|---|---|---|
| Ragione sociale | Lavoro & Salute srl (anche "Lavoro & Salute s.r.l.", "Lavoro & Salute S.R.L.") | piede del sito; PDF AME 2016; MioDottore |
| P.IVA, C.F. e n. Registro imprese | 04074830284 (lo stesso numero per i tre) | piede; PDF AME 2016 ("C.F. P.I. e n° Reg. Imp. 04074830284") |
| VIES | "isValid: false" (18/10/2026): la partita IVA non è iscritta all'archivio VIES degli scambi intracomunitari. Non dice che la società sia cessata | `ec.europa.eu/taxation_customs/vies`, risposta in `_prova/crawl/esterne/vies.json` |
| Capitale sociale | 40.000,00 euro | PDF AME 2016 |
| Costituzione | 2006 ("società costituita nel 2006"); Lo Savio amministratore "da gennaio 2006" | home; CV Lo Savio. Data esatta e REA [DA CONFERMARE su Registro imprese: i servizi pubblici hanno risposto 403, 404 o 429] |
| Sede | Via S. Felice e Fortunato 26, 35010 Limena (PD) (scritto anche "Via S.S. Felice e Fortunato" e "Via Santi Felice e Fortunato") | sito; PDF; MioDottore; iDoctors; Google Maps |
| Telefono | 049 8843927 (+39 049 88 43 927) | sito; PDF |
| Fax | 049 8599298 | PDF AME 2016 [DA CONFERMARE se attivo] |
| Email | info@lavoro-salute.it; stefania.bano@lavoro-salute.it | sito |
| PEC | non pubblicata; INI-PEC non interrogabile in automatico [DA CONFERMARE] | |
| Direttore sanitario | Dott. Marco Lo Savio | PDF AME 2016 ("DIRETTORE SANITARIO: Dott. Lo Savio Marco"); oggi [DA CONFERMARE] |
| Autorizzazione sanitaria | "Il Poliambulatorio Lavoro & Salute è autorizzato del 2006"; estremi non pubblicati. In Veneto l'autorizzazione all'esercizio di un ambulatorio privato è del Comune (L.R. 22/2002); non è nell'elenco delle strutture accreditate trovato | sito; ricerca web. Numero e data [DA CONFERMARE] |
| Convenzioni | convenzione aziendale per dipendenti e familiari delle aziende seguite; nessuna convenzione SSN o con assicurazioni dichiarata | sito [DA CONFERMARE] |
| Orari | segreteria e prenotazioni lun-ven 9,00-12,30 e 14,30-19,00; sabato e domenica chiuso (la testata Salute dice 9-19 continuato) | sito [DA CONFERMARE] |
| Specialità | 13 elencate (14 con la medicina del lavoro) | sito |
| Medici | 6 con pagina + Grgic (oculistica) senza pagina + Iacopetta (dietologia) citato nel testo | sito; vedi tabella sopra |
| Zona servita (aziende) | province di Padova e Vicenza | pagine Medicina del lavoro Padova e Vicenza |
| Settori seguiti | ceramiche, servizi, studi professionali, farmacie, edilizia e impianti, tipografie, metalmeccaniche, confezioni, commercio, florovivaistiche, autofficine, carrozzerie, centri revisione, autotrasporti, piscine, pasticcerie, logistica | CV Lo Savio |
| Clienti pubblici citati | ACI-PRA del Triveneto (2007-2018), gruppo UniCredit per il Triveneto (dal 2010), Ragionerie territoriali dello Stato di Padova, Verona, Vicenza, Treviso, Belluno, ENAC Verona e Venezia, Archivi di Stato, Soprintendenze, una ventina di istituti comprensivi del Padovano | CV Lo Savio (incarichi suoi come medico competente; usarli come referenze dell'azienda [DA CONFERMARE] e con permesso) |
| Marchio collegato | "L&S Formazione e Sicurezza" / "Lavoro & Salute - FORMAZIONE E SICUREZZA" | pagine formazione; logo storico [DA CONFERMARE se è una società separata] |
| Google | "Poliambulatorio Lavoro & Salute", 4,3 su 6 recensioni (18/10/2026) | riquadro della mappa incorporata, `02-salute-1440-contatori.png` |
| Social | Facebook `facebook.com/poliambulatorio.lavoroesalute`, Instagram `@poliambulatorio.lavoroesalute`, Twitter/X `@PLavoroesalute`, LinkedIn `company/lavoro-salute` | link del sito (attività non verificata: richiedono login) |
| Sito | WordPress realizzato da "Iacopo Trezzi" (piede), utente editore "Giech79"; certificato Let's Encrypt fino all'11/12/2026; hosting Apache su 46.254.34.192, dominio nudo su IP Aruba | piede; intestazioni; DNS |

## L'anteprima Netlify (lavoro-salute-anteprima.netlify.app)

Letta per intero: **50 pagine**, tutte raggiungibili (49 risposte 200 più la home), copie in `_prova/crawl/anteprima/` (`p_*.html`, `testi/`, `corpo/`), screenshot `_prova/attuale/anteprima-*.png`. È il sito Eleventy costruito nella sessione Claude dell'11-14 settembre (vedi sotto): Archivo e Fraunces, home divisa in due metà con foto (saldatore a sinistra, reception di lusso a destra), titoli in serif, pagine Lavoro e Salute lunghe, 13 schede di specialità, 6 medici, moduli Netlify. Il testo è attento (niente prezzi, niente orari), ma contiene dati che vanno controllati uno per uno.

| Dato dell'anteprima | Stato | Fonte che conferma |
|---|---|---|
| Lavoro & Salute srl, P.IVA 04074830284, Via S. Felice e Fortunato 26, 35010 Limena, 049 884 3927, info@lavoro-salute.it | confermato | sito attuale |
| "Dal 2006 a Limena", "autorizzato dal 2006" | confermato | sito attuale (home, Salute) |
| "tredici specialità", elenco delle 13 | confermato | sito attuale (elenco Salute) |
| "6 medici specialisti", i sei nomi e le specialità | **parziale**: il sito ne mostra 7 nel carosello (manca la Dott.ssa Vuga Ana Grgic, oculistica) e cita il Dott. Iacopetta | sito attuale; [DA CONFERMARE] chi riceve oggi |
| Fisiatria: Greco e Riviezzo; ORL Turco; Medicina legale Di Nino; Dermatologia Bano; Aeronautica Lo Savio | confermato | pagine dei medici; MioDottore (Bano); iDoctors (Greco) |
| Profili dei medici (lauree, specializzazioni, n. Ordine PD-8617, n. 16735, IT-1012-AME, CTU Venezia 2009) | confermato come dichiarato dal sito; non verificato sugli albi | pagine `/doctor/` del sito attuale |
| "2 province servite, Padova e Vicenza" | confermato | pagine Medicina del lavoro PD e VI |
| Settori "Metalmeccanica, Ceramica, Edilizia e impianti, Tipografie, Confezioni, Commercio, Farmacie, Studi professionali, Florovivaismo, Servizi" | confermato | CV Lo Savio |
| Storia: "2006 costituzione e autorizzazione", "2006 primi incarichi di medico competente per le aziende di Padova e Vicenza", "2015 certificazione ENAC: nasce la medicina aeronautica" | 2006 e 2015 confermati; "Padova e Vicenza" nel 2006 e "nasce la medicina aeronautica" sono deduzioni | home e CV Lo Savio; resto [DA CONFERMARE] |
| Primo soccorso "gruppo A 16 ore, gruppi B e C 12 ore; aggiornamento ogni tre anni (6 h / 4 h)" | confermato | articolo 2013 del sito; DM 388/2003 (fonte pubblica) |
| Antincendio "livelli 1, 2 e 3", "D.M. 2 settembre 2021", "aggiornamento ogni cinque anni" | norma pubblica corretta; che Lavoro & Salute faccia tutti e tre i livelli e la prova pratica di spegnimento | [DA CONFERMARE] |
| "Accordo Stato-Regioni 17 aprile 2025" | norma pubblica corretta | Conferenza Stato-Regioni |
| Visite a domicilio, esami del sangue su appuntamento, refertazione istologica | confermato | sito attuale (Salute) |
| Convenzione aziendale per dipendenti e familiari | confermato | sito attuale (Medicina del lavoro) |
| Riunione periodica sopra i 15 lavoratori, SPISAL, cassette DM 388/2003, cartella sanitaria | confermato | sito attuale (Medicina del lavoro Padova) |
| "Ti richiamiamo entro un giorno lavorativo", "Preventivo scritto entro un giorno lavorativo", "Bastano due minuti", "Sette campi, nessun impegno" | **non confermato**: promessa di servizio inventata | [DA CONFERMARE] |
| "Una sola segreteria per aziende e pazienti", "Ogni servizio ha un referente", "Il medico ha nome e cognome, prima e dopo la visita", "Le scadenze le teniamo noi" | stesso numero e stessa sede confermati; il resto è formula | [DA CONFERMARE] |
| "Aziende di Padova e Vicenza, da cinque a qualche centinaio di persone" | non confermato | [DA CONFERMARE] |
| "nei nostri ambulatori di Limena o nella tua sede, con la strumentazione portatile per gli esami" | visite in azienda confermate; strumentazione portatile no | [DA CONFERMARE] |
| "la visita si paga al termine, senza impegnativa", "la fattura viene rilasciata a chi sostiene la spesa", "La tariffa te la dice la segreteria" | non confermato | [DA CONFERMARE] |
| "Rispondiamo dal lunedì al venerdì", "Chiusure festive comunicate su questa pagina" | lun-ven confermato dagli orari del sito; il resto no | [DA CONFERMARE] |
| "Lavora con noi: cerchiamo medici specialisti ambulatoriali, medici del lavoro, formatori e tecnici della sicurezza" (in un'altra pagina "e personale di segreteria") | le prime quattro figure confermate dal modulo del sito; "personale di segreteria" no | [DA CONFERMARE] |
| Documenti "Fac-simile per l'incarico al medico competente", "in aggiornamento", "in preparazione" | non esistono sul sito attuale | [DA CONFERMARE] |
| Dichiarazione di accessibilità "Ultimo aggiornamento: 13 settembre 2026" | è dell'anteprima, non dell'azienda | togliere |
| Foto: sala d'attesa con sedute in legno (alt "Sala d'attesa contemporanea..."), reception bianca con orchidee, corridoio curvo con poltrone, ambulatorio, aula, saldatore, firma di documenti | **non sono della struttura**: foto di stock presentate come il poliambulatorio; licenza non indicata | da non riusare senza licenza verificata e senza la dicitura [DA SOSTITUIRE] |
| Ritratti dei sei medici | confermato | sono quelli del sito attuale |
| Medicina aeronautica senza le tariffe di 90 e 65 euro; paracadutismo e droni non citati | omissione | sito attuale (pagina Aeronautica) |
| Orari | assenti nell'anteprima | sito attuale, [DA CONFERMARE] |

Difetti dell'anteprima rispetto ai divieti del committente (utili per non ripeterli): lineette lunghe U+2014 nel testo (nel titolo della home tra "Lavoro & Salute" e "Medicina del lavoro", e in tutti i riferimenti di legge "D.Lgs 81/2008, art. 37 [lineetta] formazione dei lavoratori"), serif corsivo per la frase d'accento in testata ("Da che parte cominciamo?"), foto di stock fredde e di lusso che non sono Limena, pagine lunghe (Lavoro oltre 1.000 parole), sezioni "I numeri della struttura" con contatori, passi numerati 01-04 ripetuti in molte pagine, slogan a tre parole ("Visitati. Ascoltati. Seguiti.", "Idonei. Formati. Sicuri.").

## La sessione precedente (session_01RNEjtUx2Yr9E9LrUfUvWWA)

Metadati: titolo "Lavoro-salute.it UX/UI redesign audit", creata l'11/09/2026 alle 11:55, chiusa il 14/09/2026 alle 22:07, archiviata, modello Opus 5 a sforzo massimo, lavorava sul Mac del committente in `/Users/danielnistor/Desktop/LoSavio/site` (Eleventy, `npx eleventy`, `scripts/check.mjs`, moduli Netlify). È la sessione che ha prodotto l'anteprima Netlify.

**Quanto ho letto**: lo strumento legge gli eventi solo all'indietro, 100 per volta, e ogni pagina copre circa cinque minuti; la sessione dura tre giorni e mezzo. Ho letto le ultime tre pagine (dalle 21:34 alle 22:07 del 14/09, testo estratto in `_prova/crawl/sessione/p01.txt` e `p02.txt`). **L'audit UX/UI iniziale dell'11 settembre non l'ho letto**: per arrivarci servirebbero centinaia di chiamate, senza un cursore dall'inizio. Il riassunto qui sotto vale solo per la parte letta.

Cosa contiene la parte letta:
- Le regole che il committente aveva dato a quel lavoro: "nessun dato inventato, ciò che non è confermato resta nascosto"; i sei medici scritti "Dott. Marco Lo Savio, Dott. Ivan Turco, Dott. Arcangelo Di Nino, Dott.ssa Stefania Bano, Dott.ssa Loreta Greco, Dott.ssa Raffaella Riviezzo"; "le foto di persone in camice sono solo i sei ritratti veri"; registro "tu", apostrofo tipografico, niente emoji; un file `QUALITA.md` con voci da A1 a G3 e una sezione B di tratti da evitare. La Dott.ssa Grgic era già esclusa: perché, non si legge nella parte letta [DA CONFERMARE].
- **Il giudizio del committente sull'anteprima** (14/09, 21:56): "on è over complicatissimo secondo te? troppo poco moderno e troppo testo?" e poi "secondo me meno testo e meno riferimenti a decreti e cose nella home salute è meglio, accorcia i testi dappertutto o togli sezioni che sono troppo lunghe e che portano comunque sd approfondimenti". È la stessa direzione della richiesta di oggi: più moderno, meno testo.
- La risposta di quella sessione: troppo testo sì (`/lavoro/` alta quasi 10.000 px a 1600, 1.345 parole contro una mediana di 348; "D.Lgs 81/2008" 85 volte nel sito), troppe impaginazioni diverse nella stessa pagina ("nove modi di presentare contenuto"), "poco moderno" no. Il taglio fatto: `/lavoro/` da 1.345 a 1.120 parole e da 23 a 6 riferimenti a decreti, tolto il modulo di preventivo duplicato (1.675 px), FAQ da sei a tre, `/salute/` da 1.019 a 900 parole. Sono state tolte anche durate dei corsi non confermate ("4 / 8 / 16 h") rimaste scritte a mano. Commit `94a526f`.
- Un ciclo automatico ("ralph loop") ha continuato a rilanciare il lavoro contro la volontà del committente ("smetti ralph loop stai bruciando token"): niente cicli automatici su questo cantiere.

## URL vecchi

Da reindirizzare con 301 (destinazioni da fissare in 03 e in `plugin/redirect-301.csv`); elenco completo nella sitemap salvata in `_prova/crawl/sitemap/`.

| URL vecchio | Contenuto |
|---|---|
| `/` | home a due porte |
| `/salute/` (e le ancore `#poli`, `#news`, `#chisiamo`, `#contatti`) | poliambulatorio |
| `/lavoro/` | area aziende |
| `/chirurgia/` `/dermatologia/` `/cografiae/` `/fisiatria/` `/ginecologia/` `/aeronautica/` `/estetica/` `/legale/` `/oculistica/` `/ortopedia/` `/otorinolaringoiatria/` `/psicologia/` `/dietologia-e-scienze-dellalimentazione/` | 13 specialità |
| `/carta_servizi/` | carta dei servizi |
| `/doctor/` `/doctor/dott-marco-losavio/` `/doctor/dottssa-stefania-bano/` `/doctor/dott-ivan-turco/` `/doctor/dott-arcangelo-di-nino/` `/doctor/dott-ssa-raffaella-riviezzo/` `/doctor/dott-ssa-loreta-greco/` | medici |
| `/department/dermatologia/` `/department/fisiatria/` `/department/medicina-del-lavoro/` `/department/medicina-legale/` `/department/otorinolaringoiatria/` `/department/venereologia/` | reparti (verso la specialità) |
| `/medicinadellavoro/` `/sorveglianzasanitaria/` `/medicinalavoropd/` `/medicinalavorovi/` | medicina del lavoro |
| `/formazione/` `/formazionefinanziata/` `/formazionegratuita/` `/corsiprimosoccorso/` | formazione |
| `/sicurezza/` `/altriservizi/` | sicurezza, tarature e certificazioni |
| `/privacy-policy/` | privacy |
| `/online-il-nuovo-sito/` `/formazione-finanziata/` `/corso-di-primo-soccorso-aziendale/` `/partenership-con-aziende-turistiche/` `/prevenzione-del-melanoma/` e `/category/...` | articoli (melanoma verso Dermatologia, primo soccorso verso Formazione, gli altri verso la home dell'area) |
| `/wp-content/uploads/2020/03/*.pdf` (4 PDF) | documenti: tenere i due della medicina aeronautica, sostituire l'Accordo 2011 |
| 54 pagine demo (`/dentist-home/`, `/contact-page/`, `/shop/`, `/product/...`, `/elements/...` ...) | 410 o redirect alla home |

## Da confermare col cliente

- Orari della segreteria (9-12,30 e 14,30-19 o 9-19 continuato) e se ci sono aperture il sabato.
- Medici che ricevono oggi e in quali giorni; la Dott.ssa Vuga Ana Grgic (oculistica) e il Dott. Salvatore Iacopetta (dietologia) ci sono ancora? Chi fa ecografie, chirurgia ambulatoriale, ginecologia, ortopedia, psicologia, medicina estetica?
- Direttore sanitario attuale; estremi dell'autorizzazione all'esercizio (Comune di Limena, 2006) e delle specialità autorizzate in seguito.
- PEC, REA, data di costituzione; fax 049 8599298 ancora attivo?
- Rapporto con "L&S Formazione e Sicurezza" (stessa società o società collegata).
- Servizi ancora offerti: tarature, SOA, ISO, 231, servizio medico per strutture turistiche, sezione audioprotesica, prelievi.
- Tariffe pubblicabili (oggi solo aeronautica 90 e 65 euro; MioDottore e iDoctors riportano 180 euro per la biorivitalizzazione e 120 euro per la riabilitazione del pavimento pelvico); pagamento e fattura; convenzioni con assicurazioni o fondi sanitari.
- Medicina estetica: va tenuta nel nuovo sito? I testi attuali vanno riscritti secondo le norme (vedi 03).
- Numeri: aziende seguite, lavoratori visitati, corsi l'anno. I contatori attuali non vanno ripresi senza una fonte.
- Referenze: si possono citare enti pubblici e aziende seguite (UniCredit, ACI-PRA, Ragionerie dello Stato, istituti comprensivi)?
- Foto: chi ha scattato la foto del dermatoscopio (2012)? Esistono foto della sede, della sala, degli ambulatori, dell'aula? Permesso per un servizio fotografico; ritratti nuovi e uniformi per tutti i medici.
- Logo in vettoriale e colori ufficiali (misurati: blu #214194, arancio #E94E1B).
- Accesso alla scheda Google e ai social per foto e recensioni (4,3 su 6 recensioni).
- Cosa tenere dell'anteprima Netlify (testi delle schede, struttura delle pagine) e conferma che le sue foto non sono della struttura.

## Fonti e file di lavoro

- Crawl: `_prova/crawl/sitemap/` (14 sitemap), `pagine/` (148 HTML), `testi/` e `corpo/` (testo), `pdf/` (4 PDF), `anteprima/` (50 pagine dell'anteprima e 7 foto), `esterne/vies.json`, `sessione/` (estratto della sessione precedente).
- Script: `_prova/script/testo.py` (testo visibile), `corpo.sh` (solo contenuto), `misura.cjs` (misure e screenshot a 1440 e 390), `vista.cjs` (cattura a finestra fissa di una fascia), `provini.py` (fogli provini), `inventario.py` (inventario immagini), `sessione.py` (lettura degli eventi della sessione).
- Screenshot: `_prova/attuale/` (10 pagine a 1440 e 390, prima schermata, fasce in parallasse, anteprima), pezzi in `_prova/attuale/pezzi/`.
- Immagini: `assets/originali/` (105 file), `_prova/inventario-immagini.json`, provini `_prova/provini/`.
- Fonti esterne usate: VIES (Commissione europea), MioDottore (pagina Limena: Dott.ssa Bano presso Lavoro & Salute S.R.L.), iDoctors (fisiatri a Limena: Dott.ssa Greco), Google Maps (riquadro incorporato nel sito), L.R. Veneto 22/2002. Non raggiungibili o senza risultati da qui: Registro imprese e aggregatori (403, 404, 429), INI-PEC, albo FNOMCeO, elenco regionale delle strutture autorizzate, Facebook e Instagram (login), galleria completa di Google Maps.
