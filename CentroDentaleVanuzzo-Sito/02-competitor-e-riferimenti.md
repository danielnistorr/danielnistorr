# 02. Concorrenti e riferimenti di design

Ricerca del 13 ottobre 2026. Ho aperto con Playwright 8 siti di concorrenti e 31 siti di riferimento, a 1440 e a 390 px (prima schermata e pagina intera). Per ognuno ho misurato caratteri, colori e larghezza della pagina a telefono (`scrollWidth`). Ho guardato gli screenshot uno per uno, a colonne e a pezzi.

- screenshot dei concorrenti: `_prova/ricerca/concorrenti/<nome>-1440.png`, `-390.png`, `-1440-schermo.png`, `-390-schermo.png`
- screenshot dei riferimenti: `_prova/ricerca/riferimenti/` (stessi nomi)
- ritagli dei pezzi da riprendere: `_prova/ricerca/ritagli/` (26 file, elencati sotto per riferimento)
- misure di caratteri e colori: `_prova/ricerca/*/misure-*.json`
- prova a schermo delle accoppiate: `_prova/ricerca/accoppiate.html` e `accoppiate-1440.png`

Bloccano l'accesso automatico: M2 Dental Team (Camposampiero, verifica "I am human"), Centro San Leonardo (pagina vuota), Neko Health (controllo Vercel), Yorkshire Dental Suite (errore dell'applicazione), Straumann e Planmeca (403). Non li ho usati.

Nella stessa cartella `_prova/ricerca/` ci sono anche gli screenshot di una ricerca precedente, fatta nella notte fra il 12 e il 13 ottobre (file `c*-*.png`, `r-*.png`, `*.jsonl`, `passi/`). Li ho guardati tutti. Due di quei siti, Smile Tandvård e Santagostino, li ho rifotografati oggi e li uso in 2.10; gli altri (studi tedeschi e americani dai toni scuri o da catena, produttori come Zeiss, Ivoclar, EMS) non aggiungono gesti a quelli scelti.

## 1. Concorrenti

Il Centro Dentale Vanuzzo ha due sedi: Via Vigonovese 137 a Padova (CAP 35127, sulla strada verso Saonara e Vigonovo) e lo studio associato di Via Rialto 15/2 a Camposampiero (fonte: pagina Contatti del sito attuale). Ho cercato concorrenti attorno a tutte e due.

| # | Concorrente | Zona | Cosa fa meglio di Vanuzzo | Cosa fa peggio | A 390 px |
|---|---|---|---|---|---|
| 1 | [Clinica Odontoiatrica Risita (COR)](https://www.clinicarisita.it/) | Padova, Via Ottavio Munerati 2 | sito rifatto da poco. In apertura c'è la direttrice sanitaria con il numero di iscrizione all'albo ("Albo di Padova n. 01289"). Le cure sono presentate a partire dal bisogno del paziente ("Mi mancano uno o più denti", "Cerco un dentista per mio figlio", "Ho paura del dentista"). Il team ha foto omogenee, con nome e ruolo. C'è un metodo in 4 passi, ci sono le domande prima della visita, e il blocco "Parla con la segreteria" ha telefono, WhatsApp, orari e indirizzo | titolo enorme con interlinea e spaziatura strette (115 px, `Segoe UI`, un font di sistema, quindi cambia aspetto da un computer all'altro); nella cattura a pagina intera l'apertura esce vuota perché i contenuti entrano con un'animazione; fondo crema #FBF9F4 e sfumature menta | 390, corretta |
| 2 | [Vigodent](https://www.vigodent.it/) | Vigonovo (VE), Via Veneto 15, sulla stessa direttrice | foto vera della facciata e della sala d'attesa; "Prenota un appuntamento" sempre in testata; telefono, email e P.IVA in fondo | foto stock per tutti i trattamenti (modelle con guanti blu); titolo generico "Valorizza il tuo sorriso"; titolo in Audiowide, un carattere da videogioco; un riquadro video nero a tutta larghezza in home | 390, corretta |
| 3 | [DentalPro Padova](https://www.dentalpro.it/centri/dentista-padova/) | Padova, Via Trieste 27 (catena nazionale) | orari completi, sabato 9-13 compreso, con il calendario degli orari speciali giorno per giorno; direttore sanitario con iscrizione all'albo; listino prezzi pubblicato; a 390 px una barra fissa in basso con Prenota, telefono, WhatsApp e chat (ritaglio `conc-dentalpro-barra-mobile.jpg`) | nessuna foto delle persone né del centro (al posto della foto c'è una mappa); testi uguali per tutti i centri; nella pagina di uno studio dentistico c'è una sezione di medicina estetica (filler) | 390, corretta |
| 4 | [Medical Center Padova](https://www.medicalcenterpadova.it/) | Padova, Via N. Tommaseo 67/b (poliambulatorio) | telefono in testata; modulo che fa scegliere il servizio; finanziamento delle cure spiegato (Appago) | foto stock; dentisti mescolati a sonno, specialisti e chirurgia estetica; a 390 il banner dei cookie copre metà della prima schermata; Montserrat e Poppins, due verdi acqua e un blu | 390, corretta |
| 5 | [Centro Odontoiatrico Amato (idealsmile clinic)](https://www.studiodentisticoamato.it/) | Borgoricco, via Roma 73, a pochi km da Camposampiero | data di inizio dichiarata ("dal 1983"); casi clinici reali; telefono e WhatsApp fissi sul lato | slider in apertura, tre box con icona in fila, Raleway maiuscolo, newsletter: impianto di dieci anni fa | 390, corretta |
| 6 | [Studio Dentistico Poli](https://www.studiodentisticopoli.it/) | Camposampiero e Portogruaro | apre con le due sedi, ognuna col suo telefono, proprio la situazione di Vanuzzo con Padova e Camposampiero; storia con una data (1991) | contatori di risultati ("+2.331 sorrisi perfetti", "+4.102 carie sconfitte"); riquadri con icona; due sezioni restano su un'icona di caricamento | **401 px: scorre di lato** |

Ho visto anche lo [Studio Dentistico Gobbato](https://www.studiodentisticogobbato.it/) (Campo San Martino, vicino a Camposampiero): ha una foto vera di tutto lo staff e gli orari giorno per giorno, ma usa quattro box con icona e un titolo in corsivo serif ("Prenditi *cura* dei tuoi denti"). Screenshot in `concorrenti/gobbato-*`.

**Cosa fanno i migliori:** dicono chi è il direttore sanitario, col numero di iscrizione all'albo (COR, DentalPro). Mettono telefono e orari a portata di pollice a telefono (DentalPro, COR). Fanno entrare il paziente dal suo problema, non dall'elenco delle branche (COR). Mostrano le persone vere con foto coerenti (COR, Gobbato). Con due sedi, danno due telefoni (Poli).

**Cosa non fa bene nessuno (spazio per Vanuzzo):**
1. Un set di ritratti già fatto e coerente. Vanuzzo ha sul sito i ritratti dei due medici, dell'igienista e delle assistenti, e una galleria di 14 foto a 1820x1208 caricate il 29/09/2015 (dettagli dello studio, giochi per i bambini, il microscopio). Solo COR, e in parte Gobbato con una foto di gruppo, hanno qualcosa di simile; gli altri usano foto stock.
2. Due sedi spiegate bene. Poli dà solo due numeri. Vanuzzo ha Padova e lo studio associato di Camposampiero (Dott. Andrea Grego con i due Vanuzzo) con due P.IVA diverse, quindi va spiegato chi si trova dove [DA CONFERMARE con lo studio: quali medici e quali giorni a Camposampiero].
3. Le convenzioni. Nessun concorrente locale le spiega. Vanuzzo ha due pagine: Cadiprof/ANDI ("Per i dipendenti degli Studi Professionali") e Mutua Certa (Unione Provinciale Artigiani di Padova).
4. I bambini. COR ha una porta d'ingresso ("Cerco un dentista per mio figlio"), Vanuzzo ha una sezione intera con tre pagine (Ambienti, Attenzioni particolari, Ortodonzia intercettiva) e la Dott.ssa Silvia Vanuzzo che, secondo la sua pagina, si occupa di pedodonzia e ortodonzia.
5. La tecnologia spiegata al paziente. Vanuzzo ha già i testi su impronta digitale intraorale, radiologia tridimensionale cone beam e laser, e il Dott. Nicola Vanuzzo è indicato come microscopista. I concorrenti la nominano in una scheda o in una riga.

**Cosa manca a Vanuzzo e hanno quasi tutti:** gli orari (non compaiono in nessuna pagina del sito attuale: [DA CONFERMARE]), il direttore sanitario in vista (oggi è solo nella pagina Contatti), un telefono toccabile a 390 px, una pagina leggibile da telefono (oggi è larga 984 px, vedi 01).

**Attenzione a COR.** COR usa un petrolio (#075B62 sul pulsante) molto vicino a quello storico di Vanuzzo (#015C61, misurato sulla testata del sito attuale). Il petrolio è nella testata del sito attuale di Vanuzzo e il teal nel logo, caricato il 17/09/2013: sono colori suoi, non presi da COR. Però il nuovo sito non deve sembrare un parente di COR. Per distinguerlo: fondo bianco e non crema, ritratti in bianco e nero e non a colori, niente sfumature menta, niente titolo gigante compresso.

**Copy da evitare** (visto nei concorrenti e nel sito attuale): "Valorizza il tuo sorriso", "Il tuo sorriso è il nostro", "Un sorriso da STAR?", contatori di "sorrisi perfetti", "il tuo studio dentistico di fiducia", le parole dell'elenco `PAROLE_VIETATE` di build.py. Il sito attuale ne usa diverse (Cosa facciamo, Il team, le pagine dei due medici): si riscrivono con le frasi concrete delle stesse pagine.

## 2. Riferimenti premium

Il Centro Dentale Vanuzzo è uno studio di Padova che si descrive come "una Grande Famiglia" (pagina Il team), con 4 dipendenti (aziende.it, 2022); sul sito compaiono due medici, un'igienista e tre assistenti. Cura adulti e bambini e ha una sezione tecnologia. I riferimenti giusti quindi sono studi dentistici veri, con siti curati, più due aziende del settore dentale (tecnologia e igiene orale). Le case di moda, gli hotel e le cliniche estetiche di lusso non c'entrano.

Ho cercato fra i vincitori del ZWP Designpreis ("Deutschlands schönste Zahnarztpraxis", il premio tedesco per lo studio dentistico più bello: un buon filtro, perché uno studio che cura l'architettura di solito cura anche il sito), fra gli studi citati nelle rassegne dei migliori siti dentistici, fra i marchi dentali con identità forte e fra gli studi europei con impianto sobrio.

Una cosa è emersa subito. I siti europei migliori (Amburgo, Zurigo, Copenaghen, Svizzera) usano tutti un grottesco senza grazie e foto vere delle persone. Serif e corsivi compaiono solo nei marchi americani di consumo (Tend, Dentologie, One Medical) e negli studi cosmetici inglesi e americani (Harley Street Dental Studio, East River, Bespoke Smile, con Playfair, Cormorant o un corsivo dorato). È proprio il "lusso" generico che l'utente ha già bocciato.

### 2.1 32 reasons ZAHNTEAM, Amburgo
[32reasons.de](https://32reasons.de/). Ha vinto il ZWP Designpreis 2025 ([zwp-online.info, 12/09/2025](https://www.zwp-online.info/zwpnews/dental-news/branchenmeldungen/das-ist-die-schonste-zahnarztpraxis-deutschlands-2025)). Usa un solo carattere, Manrope (500 per i titoli a 31-39 px, 400 per il testo), su bianco con campi beige #DDD4C3 e lilla chiaro #E6ECFF.
- **Gesto da riprendere:** il team a scacchiera. Ogni medico ha un ritratto quadrato e accanto un quadrato di testo della stessa misura (nome, di cosa si occupa, una frase). Riga per riga foto e testo si scambiano di posto. Sotto, il resto dello staff è in una griglia più piccola a tre colonne, con nome e ruolo. A 390 la scacchiera diventa foto sopra e testo sotto, sempre in quest'ordine (`32reasons-team-scacchiera.jpg`, `32reasons-assistenti-griglia.jpg`, `32reasons-team-390.jpg`).
- **Secondo gesto:** la tecnologia in blocchi "etichetta piccola, titolo, testo, una foto", su un campo di colore pieno, una tecnologia per blocco (CEREC, PRGF, laboratorio interno; `32reasons-tecnologia-blocchi.jpg`).
- **Per Vanuzzo:** pagina Il team e blocco team in home. Dott.ssa Silvia Vanuzzo, Dott. Nicola Vanuzzo e l'igienista Loretta Romanato a scacchiera, le assistenti nella griglia piccola. Le frasi vengono dalle loro pagine sul sito attuale, non si inventano.
- **Da evitare:** l'apertura è un video mp4 (in un browser senza quel codec la prima schermata resta bianca); le citazioni bianche su beige hanno contrasto 1,47:1 e quelle color sabbia su lilla 1,95:1 (illeggibili); c'è una griglia di 12 icone di servizi; i due pastelli insieme.

### 2.2 D-Clinic, Zurigo
[d-clinic.ch](https://www.d-clinic.ch/). Studio di chirurgia orale e medicina orale del Dr. med. dent. Dejan Dragisic. Roboto 300 a grandi dimensioni (titolo da 131 px, sezioni da 59 px con spaziatura -1,8 px), verde salvia #526653 su grigio freddo #EEEFF0 (5,39:1), pulsanti neri.
- **Gesto da riprendere:** le cure come elenco di righe separate da filetti sottili, con il nome grande a sinistra e un "+" a destra che apre la riga, senza icone né riquadri. A fianco, il titolo della sezione su due righe (`dclinic-trattamenti-elenco.jpg`). La foto vera dello studio è una sola, grande, e il testo le sta accanto (`dclinic-apertura-arco.jpg`).
- **Per Vanuzzo:** la pagina e il blocco Cosa facciamo, con le nove branche che il sito attuale ha già: Conservativa, Endodonzia, Chirurgia e parodontologia, Implantologia, Protesi, Ortodonzia, Gnatologia, Estetica, Igiene e motivazione. Ogni riga porta alla sua pagina.
- **Da evitare:** il titolo che scorre di lato all'infinito; il ritaglio a mezzo cerchio delle foto; il peso 300 per il testo corrente (va bene solo sopra i 40 px); i titoli verdi #658055 su grigio (3,82:1, solo per testo grande).

### 2.3 Tend, New York
[hellotend.com](https://www.hellotend.com/). Catena di studi con un'identità curata. Nantes (serif) per i titoli, Founders Grotesk per il testo, salvia #5C7570.
- **Gesto da riprendere:** il blocco sulle assicurazioni. Un elenco semplice delle assicurazioni accettate, con un segno di spunta, e accanto la domanda pratica ("la mia copre la visita?") (`tend-convenzioni-assicurazioni.jpg`). Poi l'elenco delle sedi, una per riga con il conteggio, accanto alla mappa (`tend-sedi-elenco.jpg`). In apertura, anche a 390, il telefono è un secondo pulsante accanto a "Book now" (`tend-apertura-telefono.jpg`).
- **Per Vanuzzo:** Convenzioni come elenco semplice (Cadiprof/ANDI per i dipendenti degli studi professionali, Mutua Certa per gli associati UPA Padova) con la domanda "Sono iscritto: cosa devo portare?" [DA CONFERMARE la risposta con lo studio]. Le due sedi, Padova e Camposampiero, una per riga, ognuna col suo telefono. "049 760636" toccabile già nella prima schermata.
- **Da evitare:** la barra di frasi che scorre in alto; le foto ritagliate ad arco; i modelli sorridenti; i pulsanti a pillola blu elettrico; il serif Nantes, che è la voce di un marchio americano di consumo e non di uno studio padovano.

### 2.4 Mundwerk, Albstadt
[mundwerk-albstadt.de](https://mundwerk-albstadt.de/). Ha vinto il ZWP Designpreis 2016 (il marchio del premio è sul sito; [zwp-online.info, 05/09/2016](https://www.zwp-online.info/zwpnews/dental-news/branchenmeldungen/zwp-designpreis-2016-die-schoenste-ist-einem-fabrikgebaeude)). Roboto 300 e Lato.
- **Gesto da riprendere:** tutto il team (13 persone) in ritratti in bianco e nero con la stessa inquadratura, lo stesso fondo e la stessa luce, in una griglia di quadrati a quattro colonne senza didascalie sovrapposte (`mundwerk-team-bianconero.jpg`). Una griglia così dice "squadra" senza bisogno di aggettivi.
- **Per Vanuzzo:** i ritratti attuali sono già in bianco e nero. Le foto a colori della galleria hanno dominanti diverse (gialla, verde, azzurra): in bianco e nero diventano un set coerente. È anche la risposta alla pagina del team attuale, che dice "aria di Casa, aria di Famiglia".
- **Da evitare:** il fondo nero su tutta la pagina; i numeri serif giganti 01-05 riempiti di foto; i titoli serif maiuscoli spaziati; l'arancio.

### 2.5 Apa Aesthetic, New York
[apaaesthetic.com](https://apaaesthetic.com/). Studio di odontoiatria estetica con sedi a New York, Los Angeles, Miami e Dubai. D-DIN 700 maiuscolo a 24 px con spaziatura 2 px per i titoli, Brandon Grotesque per il testo.
- **Gesto da riprendere:** il ritratto in bianco e nero del medico, a tutta altezza della fascia, con il testo breve accanto e un link in maiuscolo sottolineato al posto del pulsante (`apa-ritratto-bianconero.jpg`). Poi tre passi, ognuno sopra una foto dello studio, con il titolo numerato in maiuscolo (`apa-tre-passi-ambienti.jpg`).
- **Per Vanuzzo:** il ritratto del Dott. Nicola Vanuzzo al microscopio (fotogallery-01, 1820x1208, convertito in bianco e nero) o quello della Dott.ssa Silvia Vanuzzo in home, con la frase della pagina Filosofia ("ti offriremo la nostra professionalità ed il nostro tempo, per ascoltarti").
- **Da evitare:** lo skyline in apertura, la galleria prima/dopo, il muro di copertine di riviste, il tono da lusso cosmetico. Di Apa si prende solo il modo di mostrare una persona.

### 2.6 Dentologie, Chicago e Seattle
[dentologie.com](https://www.dentologie.com/). Studi di quartiere con interni progettati. Playfair Display e Inter su #F5F3F0.
- **Gesto da riprendere:** gli ambienti veri come protagonisti. In apertura c'è la reception con il logo sul banco; prima di "trova la sede" c'è un mosaico di stanze vere (`dentologie-apertura-ambiente.jpg`, `dentologie-mosaico-ambienti.jpg`). In fondo, le domande frequenti a fisarmonica (`dentologie-domande.jpg`).
- **Per Vanuzzo:** la galleria ha dettagli veri (riuniti con i giochi, le farfalle sul vetro, il microscopio, gli attestati). Per l'apertura servono però foto nuove della facciata e della sala d'attesa: brief nel LEGGIMI.
- **Da evitare:** il titolo in Playfair con una parola in corsivo ("A *better* dental experience"): è il cliché che l'utente ha bocciato; i fondi pesca e pastello; le card di servizio con foto stock.

### 2.7 3Shape, Copenaghen (settore vicino: tecnologia dentale)
[3shape.com](https://www.3shape.com/). Produttore degli scanner intraorali TRIOS. Roobert 300 a 48 px per le frasi lunghe, Karbon, petrolio scuro #003650.
- **Gesto da riprendere:** il flusso digitale spiegato in passi con un nome ciascuno (Scan, Send, Deliver, Document) e una frase lunga in carattere leggero grande che dice il senso di tutto (`3shape-fasi-schede.jpg`). Lo scanner è fotografato da solo su fondo chiaro (`3shape-scanner-numeri.jpg`).
- **Per Vanuzzo:** la pagina Tecnologia. Il testo attuale descrive già un flusso: scansione a "20 fotogrammi al secondo", "modello tridimensionale", materiali "CAD CAM", poi cone beam e laser. Si presenta come sequenza di passi tipografici, perché le immagini della pagina attuale sono piccole (300x200, 336x150, 277x182) e non reggono una foto grande.
- **Da evitare:** i pannelli sfocati sopra la foto (glassmorphism, vietato), le schede che cambiano da sole, i numeri di mercato.

### 2.8 Curaprox, Svizzera (settore vicino: igiene orale per la famiglia)
[curaprox.ch](https://curaprox.ch/). Marchio di Curaden. Futura PT, blu #003DA5.
- **Gesto da riprendere:** le categorie come campi di colore pieno con gli oggetti veri dentro, compresa "Neonati e Bambini" (`curaprox-campi-colore.jpg`). L'elenco "Salute orale" è fatto di argomenti in testo grande e leggero accanto a una sola foto (`curaprox-salute-orale-elenco.jpg`).
- **Per Vanuzzo:** un solo campo di colore pieno, l'acqua #87CBCA della scritta "Centro" del logo, per la sezione Speciale bambini. Dentro, le foto vere dei giochi sui riuniti (fotogallery-02 e 03).
- **Da evitare:** quattro colori saturi insieme, le illustrazioni stagionali, il commercio elettronico.

### 2.9 Visti e scartati

| Sito | Perché no |
|---|---|
| [Harley Street Dental Studio](https://www.harleystreetdentalstudio.com/), [East River Dental](https://www.eastriverdental.com/), [Bespoke Smile](https://bespokesmile.co.uk/) | serif con parole in corsivo ("*Relax,* this is no ordinary dental clinic"), Cormorant, scritte a mano dorate: il cliché del lusso |
| [Marylebone Smile Clinic](https://marylebonesmileclinic.co.uk/), [London Smile Clinic](https://www.londonsmile.co.uk/), [Dental House](https://dentalhouse.com.au/) | prima/dopo ovunque, contatori, nero e fucsia o viola: marketing cosmetico |
| [Istituto Stomatologico Italiano](https://www.isimilano.eu/), [zahnarztzentrum.ch](https://zahnarztzentrum.ch/), [swiss smile](https://www.swiss-smile.com/), [Malo Clinic](https://www.maloclinics.com/), [Dental Clinics](https://www.dentalclinics.nl/), [Colosseum Tannlege](https://colosseumtannlege.no/) | istituzionali o di catena: muri di testo, box arrotondati, nessun gesto preciso da prendere |
| [KU64](https://ku64.de/) | studio di Berlino noto per l'architettura, ma il sito è disordinato: banner dei cookie giallo a tutta pagina, card stock |
| [Green Door Dental](https://www.greendoordental.com.au/), [Sprout Pediatric Dentistry](https://sproutdentalga.com/), [30 Beaumont Street](https://www.30beaumontstreet.co.uk/) | forme decorative, finestra di chat sopra l'apertura, impianto da modello |
| [Smile Solutions](https://www.smilesolutions.com.au/) | sotto l'apertura la pagina resta bianca: i contenuti compaiono solo scorrendo |
| [One Medical](https://www.onemedical.com/) | medicina generale americana: serif GT Super e illustrazioni |
| [ten.co.uk](https://www.ten.co.uk/) | oggi è uno studio di pilates, non più dentale |

### 2.10 Riferimenti funzionali

| Riferimento | Cosa fa | Cosa si prende | Ritaglio |
|---|---|---|---|
| [Smile Tandvård](https://www.smile.se/) (catena svedese) | "Hitta rätt behandling": l'elenco dei trattamenti, una riga ciascuno con una freccia, accanto a un solo ritratto in bianco e nero | la prova che A (elenco a righe) e il ritratto in bianco e nero stanno bene insieme anche in uno studio per famiglie; anche "Tandläkare för barn och ungdomar" è solo una riga dell'elenco, non una sezione a parte | `smilese-trattamenti-elenco-bn.jpg` |
| [Santagostino, Odontoiatria](https://www.santagostino.it/it/specialita/odontoiatria-e-ortodonzia) (rete di poliambulatori, Milano) | separa le visite (prenotabili subito) dalle prestazioni, alle quali "è necessario effettuare una visita specialistica" prima; ogni voce ha la sua scheda informativa | la stessa logica della pagina Filosofia di Vanuzzo ("PRENOTA una visita... per ascoltarti, capire le tue esigenze"): prima la visita, poi il piano di cura. La pagina Prezzi attuale non ha prezzi: o si pubblicano quelli veri [DA CONFERMARE con lo studio], o la pagina diventa "Prima visita e preventivo" | `santagostino-prestazioni-prezzi.jpg` |

## 3. Cosa si riprende

| Sezione del nuovo sito | Riferimento | Gesto | Materiale di Vanuzzo |
|---|---|---|---|
| Apertura home | Tend, COR | telefono "049 760636" come secondo pulsante accanto a "Prenota una visita", già a 390; sotto il titolo una riga "Direttore Sanitario Dott.ssa Silvia Vanuzzo" | testi del sito attuale; numero di iscrizione all'albo [DA CONFERMARE]; foto della facciata [DA FARE] |
| Ritratto in home | Apa | un medico in bianco e nero a tutta altezza della fascia, frase breve accanto, link sottolineato | fotogallery-01 (Nicola al microscopio, 1820x1208) o il ritratto della Dott.ssa Silvia Vanuzzo; frase dalla pagina Filosofia |
| Cosa facciamo | D-Clinic | nove righe a filetto, nome grande, "+" a destra, nessuna icona | le nove pagine delle branche già esistenti |
| Il team | 32 reasons, Mundwerk | scacchiera ritratto e testo per i due medici e l'igienista; griglia di quadrati in bianco e nero per le assistenti | ritratti attuali e foto della galleria (fotogallery-13: le tre assistenti della pagina Le nostre assistenti) convertiti in bianco e nero; curriculum dalle pagine personali |
| Tecnologia | 3Shape, 32 reasons | passi con nome (impronta intraorale, modello 3D, CAD CAM), poi cone beam, laser, microscopio, uno per blocco | testi della pagina Tecnologia; foto del microscopio (tecnologia.jpg 640x427, fotogallery-01) |
| Speciale bambini | Curaprox | un campo acqua #87CBCA pieno, con foto vere dei giochi sui riuniti | testi delle tre pagine; fotogallery-02, 03, 07 |
| Convenzioni | Tend | elenco semplice delle convenzioni e una domanda pratica | pagine Cadiprof/ANDI e Mutua Certa |
| Dove siamo | Tend, Poli | due sedi una sotto l'altra, ognuna col suo indirizzo, telefono e P.IVA | pagina Contatti; orari [DA CONFERMARE] |
| Domande prima della visita | COR, Dentologie | fisarmonica con 4-6 domande | risposte da far scrivere allo studio [DA CONFERMARE]: senza risposte vere la sezione non c'è |
| Telefono a 390 | DentalPro | barra bassa con Chiama e Prenota (Chiama prima) | numero fisso dello studio |

**Scartato:** video in apertura, titoli che scorrono, prima/dopo (lo studio non ne ha pubblicati), contatori e numeri, recensioni (non ne abbiamo di verificate da citare), icone dei servizi, riquadri con icona in fila, ritagli ad arco, pannelli sfocati, serif e corsivi d'accento, sezioni che compaiono in dissolvenza (il caso di Smile Solutions mostra perché).

## 4. Accoppiate

Tutte e tre le accoppiate partono dai colori che Vanuzzo usa già, misurati sui file del sito attuale: teal #00A392 (le finestre della casa nel logo), petrolio #015C61 (la fascia della testata) e acqua #87CBCA (la parola "Centro" nel logo). Il logo è stato caricato il 17/09/2013; la data della testata non è disponibile. Il teal sul bianco ha contrasto 3,16:1, quindi non va mai usato per il testo: solo per filetti, segni e campi con testo scuro sopra.

Caratteri: solo grotteschi, perché lo sono tutti i riferimenti europei visti (Manrope, Roboto, Roobert, Futura). Nessun concorrente locale usa quelli proposti: i concorrenti usano Segoe UI, Audiowide/Ubuntu, Jost/Inter, Montserrat/Poppins, Raleway, Saira/Roboto, Open Sans/Playfair. Tutti e tre i caratteri proposti sono su Google Fonts (verificato, risposta 200).

Le tre accoppiate sono provate a schermo con testi e foto veri di Vanuzzo in `_prova/ricerca/accoppiate-1440.png`.

### A. "Ambulatorio chiaro": Hanken Grotesk + Atkinson Hyperlegible Next (consigliata)
- **Titoli:** Hanken Grotesk 500, spaziatura -0,02 em, interlinea 1,05. **Testo:** Atkinson Hyperlegible Next 400 e 600, 18 px, interlinea 1,6. **Elenchi** (cure, sedi): Hanken Grotesk 400 a 26 px.
- **Perché:** Hanken è un grottesco neutro e calmo, dello stesso tipo del Roboto di D-Clinic e del Roobert di 3Shape. Atkinson Hyperlegible è stato disegnato per il Braille Institute per chi vede poco: le lettere che si confondono (I l 1, 0 O) sono distinte. Per uno studio dentistico con pazienti dai bambini agli anziani, il cui sito oggi si legge a circa 5 px da telefono, il testo leggibile è l'argomento più forte.
- **Palette:** bianco #FFFFFF, ghiaccio #EDF1F0 per le fasce di servizio (il grigio freddo di D-Clinic, non crema), inchiostro #10272A, testo secondario #4A5F61, petrolio #015C61 per link, pulsanti e una fascia piena, teal #00A392 solo per i filetti delle righe.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #10272A | bianco | 15,61:1 |
| inchiostro #10272A | ghiaccio #EDF1F0 | 13,70:1 |
| secondario #4A5F61 | bianco | 6,77:1 |
| secondario #4A5F61 | ghiaccio | 5,95:1 |
| petrolio #015C61 (link) | bianco | 7,76:1 |
| bianco (pulsante, fascia) | petrolio #015C61 | 7,76:1 |
| acqua chiara #CFE7E4 (testo secondario in fascia) | petrolio | 5,99:1 |
| teal #00A392 | bianco | 3,16:1: solo filetti, mai testo |

### B. "Acqua del logo": Albert Sans, una famiglia
- **Titoli:** Albert Sans 600, spaziatura -0,025 em. **Testo:** Albert Sans 400, 18 px.
- **Perché:** Albert Sans è un grottesco geometrico scandinavo, più tondo e amichevole di A, vicino al Futura di Curaprox e al Founders Grotesk di Tend. Porta il campo di colore pieno di Curaprox nella parte "famiglia" dello studio (bambini, igiene), con l'acqua che il logo ha già. È adatta se lo studio vuole spingere su bambini e prevenzione.
- **Palette:** acqua #87CBCA (campo pieno), acqua chiara #E3F0EF, bianco, inchiostro #0F2E30, secondario #4C6366, link #006B61, teal #00A392 per i segni.
- **Rischio:** un'acqua a tutta pagina ricorda le sfumature menta di COR. Va usata a campi netti, mai sfumata, e mai per più di una sezione per pagina.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro #0F2E30 | bianco | 14,45:1 |
| inchiostro #0F2E30 | acqua #87CBCA | 7,86:1 |
| inchiostro #0F2E30 | acqua chiara #E3F0EF | 12,37:1 |
| secondario #4C6366 | bianco | 6,39:1 |
| secondario #4C6366 | acqua chiara | 5,47:1 |
| link #006B61 | bianco | 6,41:1 |
| link #006B61 | acqua chiara | 5,49:1 |
| inchiostro #0F2E30 | teal #00A392 | 4,58:1 (solo testo grande o grassetto) |

### C. "Ritratto": Red Hat Display + Red Hat Text
- **Titoli:** Red Hat Display 700, spaziatura -0,02 em. **Testo:** Red Hat Text 400, 18 px. È una famiglia nata in due tagli, uno per i titoli e uno per il testo.
- **Perché:** dà più carattere ai nomi delle persone. È l'accoppiata dei ritratti in bianco e nero di Mundwerk e Apa: una fascia scura dedicata solo al team, con i ritratti a tutta altezza e il nome grande.
- **Palette:** nero #141414 (solo la fascia del team), bianco, grigio #F1F2F2, grigio testo #5E5E5E, grigio chiaro #B5B5B5 sul nero, teal #00A392 per filetti e bordi sul nero, petrolio #015C61 per i link su fondo chiaro.
- **Rischio:** più di una fascia nera per pagina porta verso il lusso cosmetico (Apa, London Smile). Una sola, nel team.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero #141414 | bianco | 18,42:1 |
| nero #141414 | grigio #F1F2F2 | 16,43:1 |
| grigio testo #5E5E5E | bianco | 6,48:1 |
| grigio testo #5E5E5E | grigio #F1F2F2 | 5,78:1 |
| bianco | nero #141414 | 18,42:1 |
| grigio chiaro #B5B5B5 | nero | 8,98:1 |
| teal #00A392 | nero | 5,84:1 |
| petrolio #015C61 (link) | bianco | 7,76:1 |

### Raccomandazione
A come base, con un innesto da B: il campo acqua #87CBCA pieno, solo nella sezione Speciale bambini (testo inchiostro #0F2E30, 7,86:1). È la combinazione più vicina ai riferimenti che contano (D-Clinic per l'ordine, 32 reasons e Mundwerk per le persone, 3Shape per la tecnologia). Usa i colori del logo e della testata di Vanuzzo. Mette al centro le foto che lo studio ha già. Risolve il problema misurato del sito attuale, la leggibilità da telefono.

Le foto: tutte in bianco e nero per le persone (unifica le dominanti diverse delle foto della galleria), a colori solo i giochi dei bambini e gli oggetti dove il colore è un'informazione. Mai mostrate oltre la loro misura: i ritratti delle pagine personali sono a 1279x850 e 1154x1023 px, la galleria a 1820x1208.
