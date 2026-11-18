# Awwwards: siti premiati di aziende simili alle nostre

Ricerca del 3 novembre 2026. Siti premiati da Awwwards tra il 2023 e oggi, di aziende vere: manifattura e materiali, artigianato e lusso, cibo e bevande, imprese edili e del verde. Esclusi agenzie, portfolio, eventi, giochi.

Metodo:
- premio, data e voto letti sulla pagina Awwwards di ogni sito (WebFetch);
- ogni sito visitato sul suo dominio con Playwright, schermate in `alto/awwwards/`: `<sito>-1440.jpg` (prima schermata 1440x900), `<sito>-1440-intera.jpg` (pagina intera fino a 9000 px), `<sito>-390.jpg` (prima schermata 390x844). Molti siti mostrano il contenuto solo quando compare nella finestra, oppure non scorrono affatto (tela trascinabile, scorrimento orizzontale). Per questo la pagina intera è fatta di schermate 1440x900 impilate, prese scorrendo di 900 px alla volta. Dove la home è una tela fissa, la pagina intera ripete la stessa schermata, e questo è già un'informazione;
- banner dei cookie e avvisi legali chiusi quando possibile. Non ho superato i cancelli dell'età (anno di nascita o "sì, ho 18 anni") e non ho compilato moduli: i quattro siti di alcolici sono in tabella ma non analizzati;
- misure dal DOM con uno script (famiglie, misure e pesi del testo, titoli, peso della pagina). Il peso è quello trasferito in un caricamento con scorrimento fino a 9000 px, quindi è indicativo e per i video spesso sottostimato.

Per le Menzioni d'onore (HM) Awwwards non pubblica un voto complessivo, solo i 15 voti dei giurati: dove scrivo "circa" è la media di quei voti, calcolata da me, non un dato ufficiale.

---

## 1. Tabella

| Sito | Azienda e mestiere | Premio e data | Voto |
|---|---|---|---|
| [primeasialeather.com](https://www.awwwards.com/sites/primeasia-leather) | PrimeAsia, concerie (pelle per Nike, Vans, Camper, Carhartt), dal 1985 | Site of the Day, 21 mag 2025 | 7,66 |
| [gufram.it](https://www.awwwards.com/sites/gufram) | Gufram, mobili e oggetti in poliuretano, Torino | Site of the Day e Developer Award, 10 feb 2025 | 7,55 (Dev 7,41) |
| [donmolinico.es](https://www.awwwards.com/sites/don-molinico) | Don Molinico (Grupo Viru), conserve di peperoni, Navarra, dal 1987 | Site of the Day, 25 apr 2026 | 7,35 |
| [owlfurnitureandobjects.com](https://www.awwwards.com/sites/owl-1) | OWL, laboratorio di mobili e oggetti in legno, Barcellona | Site of the Day, 29 set 2023 | 7,31 |
| [oakame.com](https://www.awwwards.com/sites/oakame) | Oakame, mobili fatti in Francia | Site of the Day, 1 nov 2024 | 7,31 (non visitabile: il firewall risponde 403) |
| [houseofcorto.com](https://www.awwwards.com/sites/house-of-corto) | House of Corto, sedie e tavoli scultorei, Parigi | Site of the Day e Developer Award, 3 dic 2025 | 7,26 (Dev 7,67) |
| [marvellco.com.au](https://www.awwwards.com/sites/marvell-tile-stone) | Marvell Tile & Stone, posa di piastrelle e pietra, Perth | Site of the Day, 7 mag 2026 | 7,26 |
| [postfamiliar.com](https://www.awwwards.com/sites/post-familiar-wine-2) | Post Familiar, cantina di vino naturale | Site of the Day e Developer Award, 18 gen 2024 | 7,26 (non analizzato: cancello 21+) |
| [coffee-tech.com](https://www.awwwards.com/sites/coffeetech-r) | CoffeeTech, costruttore di tostatrici da caffè, Israele | Site of the Day, 16 lug 2026 | 7,18 |
| [theolly.it](https://www.awwwards.com/sites/the-olly) | The Olly, panetteria e pasticceria, Como, dal 1956, 5 negozi | Menzione d'onore, 12 set 2024 | circa 8,05 |
| [isleofskyewhisky.com](https://www.awwwards.com/sites/isle-of-skye-whisky) | Isle of Skye, whisky | Menzione d'onore, 5 ago 2024 | circa 8,04 (non analizzato: chiede l'anno di nascita) |
| [knupfer-metallbau.de](https://www.awwwards.com/sites/knupfer-metallbau) | S. Knupfer Metallbau, carpenteria metallica, porte, finestre, facciate, Blaustein (Ulm), dal 1991 | Menzione d'onore, 30 mag 2025 | circa 8,0 |
| [bernicebakery.com](https://www.awwwards.com/sites/bernice-bakery) | Bernice, pasticceria e caffè, Montréal | Menzione d'onore, 28 feb 2025 | circa 7,83 |
| [mgg.ski](https://www.awwwards.com/sites/mgg) | MGG, maglieria in merino fatta in Europa | Menzione d'onore, 14 ott 2025 | circa 7,75 |
| [sirchillgin.be](https://www.awwwards.com/sites/sir-chill-gin) | Sir Chill, gin, Belgio | Menzione d'onore, 12 gen 2024 | circa 7,72 (non analizzato: cancello dell'età) |
| [arcprojects.build](https://www.awwwards.com/sites/arc-1) | Arc (Architectural Renovations & Carpentry), impresa edile e falegnameria, Sydney | Menzione d'onore, 1 ott 2025 | circa 7,54 |
| [akkeknitwear.com](https://www.awwwards.com/sites/akke) | AKKE, maglieria tecnica, Marche | Menzione d'onore, 8 apr 2025 | circa 6,73 |
| [schreinerei-siegesmund.de](https://www.awwwards.com/sites/siegesmund) | Schreinerei Siegesmund, falegnameria di mobili su misura in legno antico | Menzione d'onore, 15 lug 2024 | n.d. (voti singoli da 5,8 a 9,3) |
| [hayswoodworking.com](https://www.awwwards.com/sites/hays-woodworking-group-inc) | Hays Woodworking, arredi su misura (cucine, bagni, locali), Mississauga | Menzione d'onore, 26 giu 2025 | n.d. (da 6,1 a 8,7) |
| [kevalaceramics.com](https://www.awwwards.com/sites/kevala-ceramics) | Kevala, ceramiche da tavola per hotel e ristoranti, Bali, 150 artigiani | Menzione d'onore, 22 feb 2024 | n.d. |
| [palet.shop](https://www.awwwards.com/sites/palet-bespoke-ceramic-tiles) | Palet, piastrelle smaltate su ordinazione, Paesi Bassi | Menzione d'onore, 4 apr 2024 | n.d. (da 5,0 a 9,9) |
| [coffeecollective.dk](https://www.awwwards.com/sites/coffee-collective) | Coffee Collective, torrefazione e caffetterie, Copenaghen | Menzione d'onore, 26 set 2025 | n.d. (da 6,0 a 9,7) |
| [assemblycoffee.co.uk](https://www.awwwards.com/sites/assembly-specialty-coffee) | Assembly, torrefazione, Londra (Brixton), dal 2015 | Menzione d'onore, 20 ott 2025 | n.d. (da 5,7 a 9,9) |
| [myne.eco](https://www.awwwards.com/sites/myne-circular-metals) | Myne (già Reukema), riciclo dei metalli, Harderwijk | Menzione d'onore, 27 nov 2023 | n.d. (da 6,4 a 9,0) |
| [artisansdegeneve.com](https://www.awwwards.com/sites/artisans-de-geneve) | Artisans de Genève, laboratorio di personalizzazione orologi, dal 2005 | Menzione d'onore, 13 dic 2025 | n.d. (da 6,2 a 9,8) |
| [cedarsprings.net](https://www.awwwards.com/sites/cedar-springs-landscapes) | Cedar Springs, progettazione e costruzione di giardini, Oakville | Menzione d'onore, 20 nov 2025 | n.d. (da 6,7 a 10) |
| [acaciadesign.com.au](https://www.awwwards.com/sites/acacia-landscaping-design) | Acacia, giardini progettati e costruiti, Ballarat | Menzione d'onore, 30 giu 2023 | n.d. (da 6,8 a 9,3) |
| [sestalaioles.com](https://www.awwwards.com/sites/ses-talaioles-winery) | Finca Ses Talaioles, cantina, Maiorca | Menzione d'onore, 28 giu 2024 | n.d. (non analizzato: cancello dell'età) |

28 siti trovati, 23 visitati e analizzati. Scartati dopo la verifica: Regar (è un sito per le assunzioni, solo Nominee), Hangar Metal (configuratore su un indirizzo vercel.app, non il sito dell'azienda), Litecom (service per eventi), Formigari (premio del 2017).

Peso misurato delle home (MB trasferiti, indicativo): Artisans de Genève 144, Kevala 52 (22,7 s prima del contenuto), Myne 31, PrimeAsia 27, Coffee Collective 19, OWL 15, Knupfer 14,5, Cedar Springs 11,6, Gufram 10,8, Acacia 9,3, The Olly 9,2, Marvell 8,3, Assembly 7,3 (439 richieste), Siegesmund 7,2, AKKE 4,9, MGG 4,8, Arc 4,5, Palet 3,3, Bernice 3,0, House of Corto 2,6, Hays 2,3, Don Molinico 2,2, CoffeeTech 1,8.

---

## 2. Schede

### Arc (arcprojects.build)
- **Che cosa fa:** impresa edile e di falegnameria per ristrutturazioni d'architetto, case con molto legno, Redfern (Sydney).
- **Prima schermata:** a 1440 è solo foto: una casa tra gli eucalipti, al crepuscolo, a tutto schermo (100%). In alto a sinistra 5 voci di menu in colonna (Projects, Profile, Process, Impact, Contact) a 12 px. In alto a destra il logotipo "Arc." alto circa 120 px. Nient'altro: 3 elementi. La frase arriva sotto la piega. A 390 la foto prende metà altezza e sotto ci sono la frase e il link "See Our Profile".
- **Struttura:** foto; frase in due colori ("Architecture, Built for Life." in ruggine, poi "We're architectural builders committed to responsible construction of timber-rich projects." in nero); 3 progetti in fila, foto verticali; foto della squadra in ufficio con le polo dell'azienda; "Collaborative Craftsmen"; scala in legno grande e una foto di cantiere piccola; "Architecture that lasts" con foto larga; due progetti; piede nero con newsletter.
- **Foto:** servizi veri, fatti dai fotografi d'architettura dei progetti. Luce naturale, colori caldi non spinti. Tre formati: tutta larghezza, verticale 3:4, quadrata. Circa 10 foto.
- **Tipografia:** una sola famiglia, Neue Haas Grotesk Display, un solo peso (500). Tre misure in tutta la home: 12, 16 e 33 px. Interlinea 1,0. Niente maiuscolo. Il logotipo è l'unico gesto di scala.
- **Colori:** bianco, nero, un ruggine (circa #b5481b) solo per la prima riga delle frasi e per il quadratino di "torna su", piede antracite.
- **Griglia e margini:** margine laterale di 16 px anche a 1440, foto al vivo o in griglia di 3 colonne con passo di 8 px.
- **Dettagli da studio:** didascalia sotto ogni progetto con due voci: nome del lavoro in nero e studio d'architettura in grigio ("Smash Repair House / Matt Elkan", "Paddington St. Terrace / Trias"). Un filetto solo prima di "See All Projects". Non ci sono bottoni, icone, cifre, recensioni.
- **Prove:** i nomi degli architetti con cui lavora, la squadra in foto, la ragione sociale nel piede.
- **Contatto:** email e indirizzo nel piede, voce Contact. Niente telefono in home.
- **Cosa si trasferisce:** la didascalia doppia (lavoro e committente o progettista) per i nostri edili e impiantisti; tre misure e un peso; il colore del marchio solo sulla prima riga di ogni blocco. **Cosa no:** la foto a tutto schermo senza testo funziona solo con un servizio fotografico vero; con le foto dei nostri clienti (poche, piccole) la prima schermata resterebbe muta. Il telefono assente non va bene per un'impresa che lavora su chiamata.

### Hays Woodworking (hayswoodworking.com)
- **Che cosa fa:** arredi su misura per case e locali (cucine, bagni, armadi, bar), Mississauga, Canada.
- **Prima schermata:** foto di cucina finita al 100% della larghezza e circa 65% dell'altezza, il logo in un riquadro bianco in alto a sinistra, menu in maiuscolo piccolo (12 px) diviso da filetti verticali. Titolo in basso a sinistra sulla foto, "Custom millwork for homes and businesses" a 65 px, peso 350; a destra una frase di 22 px e il link "About Hays Woodworking". 4 elementi.
- **Struttura:** apertura; "Carving the future, rooted in tradition" con foto di soggiorno; "Featured Projects" con tre foto sfalsate e il nome della via; citazione del fondatore su foto scura di un bar; "Services" come elenco di 7 righe; "Start your custom journey" con il bottone rosso "Request a quote"; foto di dettagli (cassetti dei coltelli); piede.
- **Foto:** servizio d'interni professionale, luce di giorno, bianchi puliti. Circa 12 foto, verticali e orizzontali.
- **Tipografia:** Archivo in pesi leggeri (300 e 350), titoli 65 e 50 px, righe dei servizi 43 px, testo 21,6 px. Interlinea 1,0 sui titoli. Menu e link in maiuscolo piccolo.
- **Colori:** bianco, nero, il rosso del monogramma (circa #a3242a) solo sul bottone del preventivo.
- **Griglia:** una colonna stretta a sinistra di circa 100 px per il logo, con un filetto verticale che corre per tutta la pagina; il contenuto parte da lì.
- **Dettagli da studio:** i progetti hanno il nome della via ("Woodlawn", "Balmoral Ave", "McTague 2"); la citazione è firmata "Chris Hay, Hays Woodworking Group Inc., Founder" e porta il nome del locale fotografato ("Prettyugly Bar"); i servizi sono righe di indice con freccia, una si annerisce al passaggio e mostra la foto.
- **Prove:** lavori con il nome, il fondatore con nome e ruolo.
- **Contatto:** piede con "Hays Woodworking Group Inc." a 36 px, indirizzo, email e telefono a 22 px sottolineati.
- **Cosa si trasferisce:** quasi tutto. Elenco dei servizi come righe di indice (per Belletti, FratelliZuin, MeccanicaMasi che oggi hanno elenchi di testo); i lavori con il nome della via o del cliente; il piede-biglietto da visita. **Cosa no:** la foto che compare al passaggio non esiste a 390, quindi va messa in riga.

### Knupfer Metallbau (knupfer-metallbau.de)
- **Che cosa fa:** carpenteria metallica, porte, finestre, facciate in alluminio, protezione antincendio. Fondata nel 1991 da Josef Knupfer.
- **Prima schermata:** video dell'officina (capannone, furgoni con il logo) scurito, al 100%. Sopra, il nome "Knupfer" a 346 px (Urbanist 600) e "Metallbau" a 105 px allineato a destra. Sotto, una frase di 20 px. Testata con 5 voci, due icone tondi (telefono, email) e il bottone "Kontakt". 5 elementi.
- **Struttura:** apertura; "Über uns" con la storia in una frase di 45 px; foto aerea della sede; "Unsere ausgewählten Leistungen" 01-04 con foto piccola a sinistra e nome a 45 px; "Aktuelle Projekte" a 350 px che scorre; progetti con didascalia; blocco scuro "Haben Sie eine Idee für ein Metallbau-Projekt?" con "Jetzt kontaktieren"; "Wir suchen Verstärkung" (assunzioni); piede.
- **Foto:** mescolate. Il video e la foto aerea sono veri; le foto dei lavori sono buone ma non da servizio unico; una ("Glaserker mit Ausblick") sembra un render. Circa 12 immagini.
- **Tipografia:** una famiglia, Urbanist, pesi 400-600. Testo 20 px con interlinea 1,5, titoli 45 e 66 px, due gesti giganti (346 e 350 px).
- **Colori:** quasi bianco (#fcfcfc), nero, fasce scure del video. Il blu e l'arancio del logo non entrano nella pagina.
- **Griglia:** margine 60 px, servizi a due colonne (foto e testo), filetti orizzontali tra le righe.
- **Dettagli da studio:** numerazione 01-04; didascalia dei progetti con lavoro e luogo a sinistra e categoria a destra ("Aluminium-Treppenhausfassade & Eingangsbereich, Mehrfamilienhaus Ulm / Fensterlösungen"); un quadratino colorato prima delle etichette di sezione.
- **Prove:** anno e fondatore, sede in foto, lavori con il luogo, il fatto che assumono.
- **Contatto:** telefono ed email in testata come icone, bottone Kontakt, chiusura con invito.
- **Cosa si trasferisce:** è il caso più vicino alle nostre officine. Il nome dell'azienda come immagine quando la foto è debole; la storia in una frase grande; servizi numerati; didascalie con luogo e categoria; la sezione assunzioni (per molte delle nostre è un bisogno vero). **Cosa no:** il video di sfondo pesa 13 MB; meglio una foto ferma dell'officina. I testi compaiono solo allo scorrere (vietato); a 390 i titoli a 350 px vanno ridotti.

### Kevala Ceramics (kevalaceramics.com)
- **Che cosa fa:** progetta e produce ceramiche su misura per hotel e ristoranti; laboratorio a Sanur e negozi a Ubud e Uluwatu.
- **Prima schermata:** dopo un caricamento lungo (22,7 s, percentuale a schermo), foto macro di una ciotola a grana, al 100%. Logotipo al centro, menu a sinistra, "Showcase", ricerca, lingua. Frase in basso al centro a 27 px: "We design and manufacture custom ceramics for the global hospitality and F&B industry". Numerazione verticale "01-04" della serie. 5 elementi.
- **Struttura:** apertura a scorrimento di 4 foto; due foto di piatti in servizio con "Showcase"; video del laboratorio; "Experience Bespoke Ceramic Tableware" con "Start your project"; tre punti (design, quantità ridotte, qualità) su una foto; mani che incidono una tazza e una ciotola su fondo pesca; "Trusted by 150+ Hotels and 200+ Restaurants, Handmade by 150 Artisans" con "Book your consultation"; fascia di loghi (Six Senses, Waldorf Astoria, Raffles, Ritz-Carlton, Capella); lavori in carosello; negozi; piede.
- **Foto:** servizio vero e coerente: macro della materia, piatti in servizio su tavoli scuri, mani al lavoro, prodotto su fondo colorato. Luce laterale morbida. Circa 25 foto.
- **Tipografia:** un grottesco (TT Commons Pro) e un carattere disegnato per il marchio. Testo a 11-13 px: troppo piccolo.
- **Colori:** crema (#f2ede1), nero, sabbia (#cdc7b2) per caricamento e piede, i colori delle smaltature.
- **Griglia:** margine 33 px, impaginazione libera a due colonne sfalsate.
- **Dettagli da studio:** lavori con cliente e anno ("Cantina Kahlo, Ritz Carlton Bahrain / 2024", "Rosewood Doha / 2026", "InterContinental Danang / 2026"); pallino nero prima delle etichette; numerazione della serie.
- **Prove:** la frase con i numeri, i loghi di catene alberghiere, i lavori nominati.
- **Contatto:** "Book your consultation", WhatsApp fisso, orari (lunedì-venerdì 8-17) e indirizzo nel piede.
- **Cosa si trasferisce:** per ArgenteriaVarotto (fornisce hotel e ristoranti) è il modello: cliente e anno sotto ogni lavoro, una frase con i numeri al posto della fascia di cifre, i loghi dei clienti con il permesso. **Cosa no:** 52 MB e 22 secondi di attesa, testo a 11 px: tutto il contrario di quello che serve.

### The Olly (theolly.it)
- **Che cosa fa:** panetteria e pasticceria di Como dal 1956, cinque punti vendita (Como, Erba, Lurate Caccivio), anche bar e pranzo.
- **Prima schermata:** il timbro tondo del logo al centro su grigio chiarissimo, nient'altro; è un caricamento. Poi la foto del forno a tutta larghezza. A 390 il logo e un filetto rosso verticale.
- **Struttura:** logo; pane nel forno a tutta larghezza; blocco rosso con la frase "Radicata nella tradizione del pane artigianale..." a 80 px che si colora scorrendo; tre voci (pane, dolci, caffè); "Colazione, pranzo, merenda e apericena" in maiuscolo serif rosso con prodotti scontornati; foto del laboratorio; blocco rosso con la frase sui cinque negozi e la firma "Oliviero Silvani"; i cinque negozi; "Panetteria", "Siciliano", "Brioche del mese" come titoli giganti; "#theollypeople"; piede.
- **Foto:** servizio vero nel laboratorio (forno, carrelli, pala), luce calda, poca profondità di campo. Prodotti scontornati per la sezione dei pasti. Circa 20 foto.
- **Tipografia:** Inter per i testi e le frasi grandi (80 px, peso 500, spaziatura stretta), Noto Serif Display Extra Condensed in maiuscolo per le parole del menu (150 px). Etichette in maiuscolo spaziato rosso a 10-11 px.
- **Colori:** rosso del logo (circa #e32428) pieno su blocchi interi, grigio chiarissimo, un rosso scuro per i filetti.
- **Griglia:** colonna centrale, negozi in griglia di 3 colonne. Filetti verticali sottili che collegano un blocco al successivo.
- **Dettagli da studio:** ogni negozio è una scheda di testo con nome, indirizzo e telefono in maiuscolo, tabella degli orari (giorni a sinistra, ore a destra), e il tipo ("Panetteria, pasticceria, bar e caffetteria"); un bollino "Gustati qui un pranzetto!" solo su quello che fa pranzo; la firma del titolare.
- **Prove:** l'anno 1956, il nome del fondatore, cinque negozi veri.
- **Contatto:** 5 link `tel:`, uno per negozio.
- **Cosa si trasferisce:** le schede negozio con la tabella degli orari (PanificioFornasiero ce l'ha già, qui è più chiara); il colore del logo su blocchi interi; la firma del titolare. **Cosa no:** il caricamento con il logo, i testi che si riempiono di colore scorrendo (vietato), le parole in serif accanto a Inter (Inter dappertutto è vietato).

### Coffee Collective (coffeecollective.dk)
- **Che cosa fa:** torrefazione con una decina di caffetterie a Copenaghen, vendita online, forniture a bar e ristoranti.
- **Prima schermata:** barra in alto "Orders placed by 13.00 ship the same day (Mon-Fri)"; video di un coltivatore in Colombia al 100%; titolo "Origin Trip Colombia" a 54 px in due pesi; bottone chiaro "See the story". Menu a 7 voci a sinistra, logo al centro, "Wholesale" a destra. 5 elementi.
- **Struttura:** apertura; "Latest Coffees" con le confezioni su riquadri chiari uguali; blocco verde scuro per l'abbonamento con elenco a frecce; "Brew at home" con gli attrezzi; blocco color bacca "Fruity and sweet" per un caffè; "Become a wholesale partner" con elenco dei vantaggi e "Get in touch"; "Visit our shops" con le facciate; piede.
- **Foto:** due mondi tenuti separati: prodotto su fondo crema sempre uguale, e reportage (origine, negozi) in luce naturale. Circa 25 foto.
- **Tipografia:** NB International Pro in un peso, titoli 48-54 px, testo 14-16 px. Nessun maiuscolo tranne il menu.
- **Colori:** crema (#faf6ed), verde scuro (#2f3833), rosso bacca (circa #b0545f) che cambia con il caffè.
- **Griglia:** margine 40 px, schede prodotto in fila da 5 con passo di 10 px, blocchi a metà schermo foto e colore.
- **Dettagli da studio:** freccette triangolari come punto elenco; il colore del blocco viene dal profilo del caffè; nel piede il CVR (la partita IVA danese) e l'elenco delle caffetterie.
- **Prove:** "Transparency" e "Inspection Reports" nel menu e nel piede, i negozi con il nome.
- **Contatto:** modulo per i grossisti, "Contact us" nel piede. Un pop-up della newsletter copre la pagina.
- **Cosa si trasferisce:** la promessa operativa nella barra in alto (per una bottega: "Ordini entro le 13, ritiro il giorno dopo"; per un'officina: "Preventivo entro 48 ore"); la sezione grossisti con i vantaggi in elenco per chi vende anche a bar e negozi; le facciate dei negozi fotografate allo stesso modo; la partita IVA nel piede. **Cosa no:** video da 14 MB, pop-up.

### Palet (palet.shop)
- **Che cosa fa:** piastrelle da parete smaltate su ordinazione, campioni su misura.
- **Prima schermata:** foto macro di due piastrelle smaltate in diagonale, al 100%; titolo centrato "Unique by design ceramic tiles." a 96 px, peso 400, interlinea 0,85, color pesca; link "Design your tile". Logotipo grande a sinistra, 4 voci, "Cart". 4 elementi.
- **Struttura:** apertura; frase di fatti a 58 px; due metà colorate (cipria e marrone) "Create your own tiles" e "Curated sample"; cucina con le piastrelle posate; "Whether you are a professional..."; "Read more" con tre schede; piede.
- **Foto:** servizio vero, materia in macro e piastrelle posate in cucine vere.
- **Tipografia:** Founders Grotesk e la sua versione condensata. Titoli 96 e 58 px, testo 15 px. Etichette in maiuscolo piccolo dentro un riquadro a filo ("OUR STORY", "CUSTOM SAMPLE").
- **Colori:** bianco caldo, marrone (circa #4a2a20), pesca (#e8a57a), cipria.
- **Griglia:** margine 32 px, filetto sotto la testata, blocchi a metà.
- **Dettagli da studio:** la frase "Made-to-order ceramic wall tiles, available from 1 square meter with lead times starting at 8 weeks." dice in una riga minimo d'ordine e tempi; le etichette a riquadro.
- **Prove:** i fatti di produzione, le cucine posate.
- **Contatto:** "Professional" nel menu, catalogo scaricabile con nome, azienda ed email.
- **Cosa si trasferisce:** la frase con minimo d'ordine e tempi di consegna (per DZStampi, EtichettificioVeneto, Daisyplast, ConceriaEuropa è un dato che il cliente cerca); le etichette di sezione a riquadro; due metà di colore per due strade (privati e professionisti). **Cosa no:** il pop-up del catalogo che si apre da solo.

### Acacia Landscaping + Design (acaciadesign.com.au)
- **Che cosa fa:** progetta e costruisce giardini a Ballarat, città di provincia.
- **Prima schermata:** colonna nera di 76 px a sinistra con il logo e una freccia; il resto è un video (in cattura resta il fondo sfumato grigio del caricamento); in basso "LANDSCAPING CONSTRUCTION + DESIGN" in maiuscolo spaziato a 22 px. 3 elementi.
- **Struttura:** apertura; "Quality, detail, pride" e "Who Are We" in serif a 128 px con un paragrafo; filetto; "Projects / Our Work" con griglia di 6 lavori a due colonne sfalsate; "Contact us" con foto; piede nero.
- **Foto:** servizio vero di giardini finiti in luce radente, tono caldo.
- **Tipografia:** PP Eiko (serif sottile) per due titoli grandi, PP Neue Montreal per il resto; etichette 14 px maiuscolo spaziato; testo 20 px.
- **Colori:** grigio chiarissimo (#f7f7f7), antracite, bianco.
- **Griglia:** colonna fissa a sinistra con filetto verticale, contenuto rientrato di circa 160 px.
- **Dettagli da studio:** i lavori si chiamano con la via ("Raglan St", "Errard St", "Clyde St", "Kelsall Terrace"); il contatto si rivolge per nome a chi scrive: "Potential clients, landscape designers, architects and builders".
- **Prove:** solo i lavori.
- **Contatto:** telefono ed email nel piede, link Contact.
- **Cosa si trasferisce:** per BordinGarden e GardensPav: nomi dei lavori con la via, contatto che elenca i tipi di cliente. **Cosa no:** la prima schermata dipende tutta dal video; se non carica resta un grigio vuoto, come in cattura.

### Cedar Springs Landscapes (cedarsprings.net)
- **Che cosa fa:** giardini e spazi esterni di lusso (piscine, cucine all'aperto), Oakville e Burlington.
- **Prima schermata:** foto al crepuscolo di un giardino illuminato al 100%, una fascia destra di 220 px con la foto sfocata, "scroll" e i social. Titolo "get away every day" a 88 px peso 300, minuscolo. In testata il link "Start Your Backyard Resort". 4 elementi.
- **Struttura:** apertura; progetto in evidenza "fire, water & alfresco" con frecce (8 progetti con nome); "design is just the beginning" accanto alla pianta tecnica di un giardino; "start the process today"; "inspired by nature, guided by experience, defined by character"; piede.
- **Foto:** servizio professionale coerente, tutto al crepuscolo con le luci accese. 
- **Tipografia:** Akzidenz-Grotesk Next, pesi 300-400, titoli 64-88 px, testo 12-16 px.
- **Colori:** bianco, nero, fasce antracite.
- **Dettagli da studio:** l'H1 nascosto è "Award-Winning Landscaping in Oakville, Burlington": il titolo che vedi è uno slogan, quello che legge Google dice mestiere e luogo. La pianta del giardino disegnata dallo studio è usata come immagine.
- **Contatto:** telefono, email e indirizzo nel piede, "Get In Touch".
- **Cosa si trasferisce:** H1 con mestiere e luogo anche se il titolo grande è altro; i disegni tecnici veri dell'azienda (piante, tavole CAD, esplosi) come immagine quando le foto mancano: sono documenti del lavoro, non illustrazioni. **Cosa no:** 11,6 MB e 13,7 s; il titolo in minuscolo e senza mestiere a vista.

### CoffeeTech (coffee-tech.com)
- **Che cosa fa:** progetta e costruisce tostatrici per caffè da negozio, da laboratorio e industriali.
- **Prima schermata:** fondo quasi nero, "Coffee Roasting Reinvented" su tre righe a 216 px (Inter 500, interlinea 0,95) centrato. In testata "Products" pieno arancio e "Contact Us" a filo, lingua. Scorrendo, la tostatrice esce dal buio. 4 elementi.
- **Struttura:** titolo; macchina; ritratto del fondatore con firma e frase; "Beyond your expectations" che scorre; "[Our Products]" con 4 macchine su riquadri grigi; "[Our Specialty]" caffè, cacao, frutta secca; "[Testimonials]" numerati; "[Our Approach]" tre righe con freccia; blog; "Interested in learning more?" con "Products Catalog" e "Contact Us"; piede nero "Get in touch".
- **Foto:** render delle macchine su grigio, foto dei chicchi, ritratti veri.
- **Tipografia:** solo Inter (vietato da noi), titoli 216, 63 e 51 px peso 500-600, testo 14 px.
- **Colori:** nero (#0d0e13), crema, grigio caldo (#e7e2de), arancio del logo (#d0613e).
- **Dettagli da studio:** etichette tra parentesi quadre "[Our Products]"; testimonianza con il numero "01" a 63 px, nome e torrefazione cliente ("Mark Jones, Java Jones Roasters"); categoria della macchina in un'etichetta a pillola.
- **Prove:** testimonianze con nome e azienda, fondatore in foto.
- **Contatto:** "Contact Us" in testata, catalogo, indirizzo nel piede.
- **Cosa si trasferisce:** testimonianza grande con nome e azienda del cliente, una alla volta e numerata, al posto di una griglia di recensioni; il catalogo scaricabile accanto al contatto (per i nostri costruttori di macchine). È leggero (1,8 MB). **Cosa no:** Inter da solo, la macchina che compare con lo scorrimento.

### PrimeAsia (primeasialeather.com)
- **Che cosa fa:** gruppo di concerie in Asia, pelle per marchi di calzature e abbigliamento.
- **Prima schermata:** fondo animato (WebGL) di pelle in movimento; "Accelerate Ahead." a 137 px peso 300; due tessere "About Primeasia" e "Our Facilities" con foto; in basso una barra "Your Future-Forward Tannery Partner." e "Our Leathers". 5 elementi.
- **Struttura:** apertura; collezione con i campioni di pelle come oggetti su grigio, ognuno con nome ("Churchill WP") e scheda (grana, nappa, pigmentata); sostenibilità con foto del depuratore; notizie (impianto solare, obiettivi SBTi, bilancio di sostenibilità); marchi clienti con le loro scarpe (Adidas, Vans, Nike, Camper, Carhartt); piede arancio.
- **Foto:** campioni fotografati come sculture, stessa luce; foto vere degli impianti.
- **Tipografia:** Lausanne peso 300 per i titoli, Inter per il testo a 16 px.
- **Colori:** grigio caldo (#efede8), blu notte per il testo, arancio (#ffa63a).
- **Dettagli da studio:** la scheda tecnica di tre righe accanto a ogni campione; i clienti mostrati con il loro prodotto, non con il logo.
- **Prove:** clienti, impianti, certificazioni climatiche.
- **Contatto:** menu a pallini, nessun telefono.
- **Cosa si trasferisce:** per ConceriaEuropa e i fornitori di materiale: il campione come oggetto con 3 righe di scheda (si fotografa con una finestra e un cartoncino); i clienti mostrati con il prodotto finito. **Cosa no:** 27 MB, sfondo WebGL, menu nascosto.

### Don Molinico (donmolinico.es)
- **Che cosa fa:** conserve di peperoni del piquillo ripieni, marchio di Grupo Viru, dal 1987.
- **Prima schermata:** caricamento rosso pieno con il logo dorato; poi foto dall'alto di una tavola apparecchiata con i vasetti al 100%, il logo in un rettangolo rosso al centro in alto, 4 voci in oro. 3 elementi.
- **Struttura:** "La importancia del pimiento" con foto ruotate; vasetto in primo piano; formati (frasco, lata, bolsa, pandereta) su giallo; campagna premiata; social; piede con il cofinanziamento europeo (FEADER, Governo di Navarra).
- **Foto:** servizio vero di cibo, luce dura e colori saturi, mani in scena.
- **Tipografia:** un condensato (super-med) in maiuscolo per tutto, 14-29 px e titoli a 216 px.
- **Colori:** quelli della confezione: rosso (#d70321), oro, crema (#fbf5e7), giallo.
- **Dettagli da studio:** la palette è il packaging; il piede porta la dicitura obbligatoria del finanziamento europeo con i loghi, impaginata bene.
- **Contatto:** voce Contactico, nessun telefono.
- **Cosa si trasferisce:** i colori presi dall'etichetta o dall'insegna (CaseificioSanVito, DistilleriaRizzi, IlTorchioAntico); la dicitura PSR o POR FESR nel piede, impaginata come parte del sito e non come un'aggiunta. **Cosa no:** caricamento, contenuto che appare solo scorrendo, molte sezioni vuote finché non animate.

### Siegesmund (schreinerei-siegesmund.de)
- **Che cosa fa:** falegnameria che costruisce a mano mobili su misura in legno antico.
- **Prima schermata:** foto di un salotto con due poltrone e tre cornici al centro, larga 880 px su fondo grigio chiaro con filetti verticali di griglia; scorrendo le cornici si riempiono di legno. Logotipo serif, "Kontakt" e "Menü". 3 elementi.
- **Struttura:** apertura; "Möbel aus antikem Holz nach Maß. 100% Handarbeit. 100% Qualität."; foto di attrezzi e mani; manifesto con parole in corsivo; griglia di 20 lavori; foto di mani con lo scalpello; "Vom antiken Holz bis zum fertigen Stück."
- **Foto:** miste: l'apertura e alcune foto (mani, bosco) sembrano di repertorio, i lavori (bagni, tavoli) sono foto vere da telefono. La griglia le rende omogenee con lo stesso taglio.
- **Tipografia:** Satoshi per il testo, Taviraj in corsivo per le parole d'accento (vietato da noi). Titoli 51-80 px peso 300.
- **Colori:** grigio chiaro (#f8f8f8), nero, rosso sul bottone.
- **Dettagli da studio:** filetti verticali di griglia visibili per tutta la pagina; griglia di lavori con lo stesso formato 4:3.
- **Contatto:** 2 link telefono e 2 email.
- **Cosa si trasferisce:** la griglia di 20 lavori presi col telefono, tutti nello stesso taglio, che insieme sembrano una serie. **Cosa no:** l'apertura di repertorio (vietata), il corsivo d'accento, le animazioni allo scorrere. È la prova che la giuria premia anche cose che a noi sono vietate: non è un modello da copiare.

### Myne (myne.eco)
- **Che cosa fa:** riciclo dei metalli con selezione automatica; prima si chiamava Reukema.
- **Prima schermata:** foto del nastro dell'impianto in un riquadro con bordi bianchi (margine 30 px), "A new future in metals has arrived" a 100 px peso sottile, una frase a destra, un riquadro con video. 4 elementi.
- **Struttura:** apertura; video dell'impianto; "About Myne" con frase grande; la macchina "The Xorter" su foto di rottami; "From waste to high-quality product in 5 revolutionary steps"; "Introducing 100% circular aluminium"; "On demand, on recipe and at lowest cost"; "Insights" con date; parola che scorre con un circuito.
- **Foto:** servizio vero nell'impianto, luce industriale fredda.
- **Tipografia:** TT Hoves in due pesi (thin e regular), 5 misure in tutto.
- **Colori:** bianco con una punta di lilla, blu notte, bottoni a filo color corallo.
- **Contatto:** un telefono, un'email, voce Contact.
- **Cosa si trasferisce:** il processo in 5 passi con il nome della macchina; le notizie con data e luogo ("Harderwijk, September 1, 2023"). **Cosa no:** 31 MB di video.

### Artisans de Genève (artisansdegeneve.com)
- **Che cosa fa:** laboratorio indipendente che personalizza orologi su richiesta dei proprietari, dal 2005.
- **Prima schermata:** avviso legale obbligatorio da chiudere; poi foto macro di un cronografo al 100%, "New Personalization: Feather" a 64 px serif peso 300, link "Discover the project of M. Eliud Kipchoge". Testata con 6 voci e "Make a request". 4 elementi.
- **Struttura:** apertura; "What We Create Lives Once"; "A Tailor-Made Approach To Watchmaking" (fondazione 2005); "A Step-by-Step Guide"; "The 7 Departments Dedicated To Your Project"; "The Artisans Behind The Craft"; "Our Bespoke Projects" con nome del progetto e del cliente; "Our Warranties" (rapporto TIMELAB e garanzia 7 anni); "Our Clients Say It Best" con ritratti; "Begin Your Personalization"; piede con l'avviso legale ripetuto.
- **Foto:** servizio vero di laboratorio e macro, toni bruni.
- **Tipografia:** Victor (serif sottile) per i titoli, Futura per il testo. 6 misure.
- **Colori:** crema, marrone cioccolato, bottone taupe.
- **Dettagli da studio:** i reparti contati (7); la garanzia con il nome del laboratorio di prova; i progetti chiamati con un nome e il cliente con le iniziali ("Val Viola, The project of Mr. A.N.J.").
- **Contatto:** "Make a request" in testata, indirizzo ed email nel piede.
- **Cosa si trasferisce:** per un laboratorio di riparazione (ArgenteriaVarotto riparazione, orafi): le fasi del lavoro numerate, la garanzia scritta con i suoi termini, i lavori con un nome. **Cosa no:** 144 MB di video, testo grigio chiaro sottile a 16 px.

### Bernice Bakery (bernicebakery.com)
- **Che cosa fa:** pasticceria e caffè a Montréal, biscotti e torte, vendita online e ritiro.
- **Prima schermata:** foto dall'alto di fette di torta al 100%, "A Baking Love Affair" in maiuscolo nero pesante a 173 px, bollino rosa "Indulge", menu a 6 voci in maiuscolo. 4 elementi.
- **Struttura:** apertura; frase su comfort e quartiere; più venduti in archi; scritta che gira; biscotti in schede con quantità e "Add to cart"; citazioni della stampa (Eater, Time Out, MTL Blog); "Celebrate with cake"; come si ordina una torta (24 ore di preavviso); newsletter; piede con il nome a tutta larghezza.
- **Foto:** servizio vero, prodotto su marmo, stessa luce.
- **Tipografia:** Apfel Grotezk e balto; 16 misure (troppe).
- **Colori:** bianco caldo, blu petrolio (#147c98), rosa (#f9a8e6), quasi nero.
- **Dettagli da studio:** la stampa citata con la frase e la testata; disegni al tratto di fette di torta come decorazione, accanto alle foto e non al loro posto.
- **Contatto:** indirizzo, email, telefono, Uber Eats e DoorDash nel piede.
- **Cosa si trasferisce:** le citazioni della stampa locale con la testata (Il Gazzettino, Corriere del Veneto, se esistono); le regole d'ordine scritte ("ordina 24 ore prima"); il nome a tutta larghezza nel piede. **Cosa no:** 16 misure, scritte che girano.

### Assembly Coffee (assemblycoffee.co.uk)
- **Che cosa fa:** torrefazione a Brixton (Londra) dal 2015, vendita, formazione, forniture.
- **Prima schermata:** due barre in alto (spedizione gratuita; "Coffees Released Since Launch: 353"); foto di una scatola nera su tessuto ruggine al 100%; a sinistra elenco di 4 novità. 5 elementi più il pop-up.
- **Struttura:** apertura; "Independent specialty coffee roaster founded in 2015 and based in Brixton, London."; prodotti su fondo nero; corsi SCA; recensioni con nome e stelle; tazze artigianali; "Assembly Coffee Served At" con i bar clienti e la città; blog; Instagram; piede.
- **Tipografia:** GT America e ID00 Serif in corsivo per titoli (vietato da noi); 12 misure.
- **Colori:** nero, crema, oliva, ruggine.
- **Dettagli da studio:** il contatore vero delle miscele uscite; "Served At" con foto della facciata del bar, nome e città ("Four Boroughs, Multiple Sites", "Just Between Friends, Manchester"); B Corp nel piede.
- **Contatto:** 20 link email, chat, "Wholesale".
- **Cosa si trasferisce:** per chi fornisce bar, negozi o rivenditori: "Dove trovarci" con la facciata del cliente, nome e comune; un contatore vero (lotti, pezzi, anni) nella barra in alto. **Cosa no:** 439 richieste, 19 s, pop-up ripetuto, corsivo.

### OWL (owlfurnitureandobjects.com)
- **Che cosa fa:** laboratorio di Alfredo Lopez a Barcellona, mobili e oggetti unici in legno.
- **Prima schermata:** striscia orizzontale infinita di foto a tutta altezza, logotipo "OWL" bianco a sinistra, una linea orizzontale a metà, 4 voci a 12 px. 3 elementi.
- **Struttura:** la home è solo la striscia di foto; si scorre in orizzontale.
- **Foto:** un fotografo, nel laboratorio, fondi colorati pieni (verde, giallo, rosso), luce dura. Le foto dicono tutto.
- **Tipografia:** ABC Diatype a 14 px, una misura.
- **Cosa si trasferisce:** l'idea che la serie di foto è il marchio, quando la serie c'è. **Cosa no:** senza servizio fotografico non esiste; niente testo, niente contatto in home, 15 MB.

### House of Corto (houseofcorto.com)
- **Che cosa fa:** sedie e tavoli scultorei disegnati da Jessica Miller, Parigi.
- **Prima schermata:** griglia infinita trascinabile di foto verticali dei mobili, ognuna con due etichette a 7-11 px (categoria a sinistra, nome a destra: "Seat / Love"). Logo al centro, 4 voci.
- **Foto:** tutte nello stesso appartamento parigino, stesso parquet, stessa luce, stesso taglio verticale. Possono essere render; non l'ho verificato.
- **Tipografia:** un solo carattere (canada-type-gibson 900) a 7 e 11 px.
- **Cosa si trasferisce:** la regola della serie: stesso fondo, stesso taglio, stessa etichetta a due voci sotto ogni foto. **Cosa no:** la tela trascinabile, il testo a 7 px.

### Gufram (gufram.it)
- **Che cosa fa:** mobili e oggetti in poliuretano (il Cactus, il Bocca), Torino.
- **Prima schermata:** i prodotti scontornati sparsi nello spazio su bianco, trascinabili; testata a riquadro con menu, logo e ricerca; interruttore "Spazio / Griglia". 4 elementi.
- **Foto:** prodotti scontornati da studio, ombra uguale.
- **Cosa si trasferisce:** l'interruttore per passare dalla vista libera alla griglia è un'idea, ma non serve a noi. **Cosa no:** tutto è effetto: la home non dice chi sono né cosa fare; 10,8 MB.

### Marvell Tile & Stone (marvellco.com.au)
- **Che cosa fa:** posa di piastrelle e pietra per case di pregio, Perth.
- **Prima schermata:** fondo grigio caldo con una griglia bianca sottile che imita le fughe delle piastrelle; foto di lavori che galleggiano e si spostano; "Marvell Tile & Stone" a 256 px bianco al centro; menu a pillola scura con 3 voci. 4 elementi.
- **Struttura:** la home è la tela; nient'altro sotto.
- **Foto:** lavori veri (cucine, bagni), qualità media.
- **Tipografia:** Neue Montreal 700, 4 misure.
- **Dettagli da studio:** la griglia del fondo è il mestiere stesso, una fuga di piastrelle.
- **Cosa si trasferisce:** un fondo che richiama il mestiere fatto in CSS (la fuga per un posatore, la quadrettatura per un disegnatore tecnico, la riga del foglio per una tipografia). **Cosa no:** la tela che si muove, 11,8 s prima di vedere qualcosa, nessun testo né telefono.

### AKKE (akkeknitwear.com)
- **Che cosa fa:** maglieria in fibre tecniche, Marche.
- **Prima schermata:** campagna di moda su rocce vulcaniche al 100%, "New Collection" in condensato a 216 px, frecce del carosello, barra promo.
- **Struttura:** apertura; manifesto su verde salvia con un disegno di montagna al tratto; uomo e donna; più venduti con modello su fondo grigio; "Everest Akke Limited"; newsletter; piede con la partita IVA.
- **Tipografia:** Humane Grotesque condensato in maiuscolo per i titoli, Inter per il testo.
- **Dettagli:** i capi hanno nomi di rocce (Basalt, Granite, Magma, Dolomia).
- **Cosa si trasferisce:** dare ai prodotti di serie un nome della stessa famiglia. **Cosa no:** è un negozio di moda, lontano dalle nostre aziende; voto medio basso (circa 6,7).

### MGG (mgg.ski)
- **Che cosa fa:** maglieria in merino disegnata in Svizzera e fatta in Europa.
- **Prima schermata:** foto di due modelli su fondo grigio; "Quality you can feel." a 24 px; due link; pop-up dello sconto che copre tutto.
- **Struttura:** apertura; recensioni Trustpilot (4,91 su 138); campagna; testate che ne hanno scritto (The Scotsman, Monocle, GQ, Powder); categorie; documentario; piede con contatore degli alberi piantati.
- **Tipografia:** Hanken Grotesk in un peso, testo 14 px.
- **Cosa si trasferisce:** il voto con il numero delle recensioni e la fonte, scritto per intero. **Cosa no:** pop-up, 24,6 s di caricamento.

---

## 3. Le costanti

### I migliori 8 per noi
Arc, Hays, Knupfer, Kevala, The Olly, Coffee Collective, Palet, Acacia. Scelti per quanto fanno per chi compra, non per il voto.

**Prima schermata**
- Una foto vera a tutta larghezza (6 su 8) oppure il nome dell'azienda come immagine sopra una foto scurita (Knupfer). Mai il titolo a sinistra con la foto a destra in un riquadro.
- Il testo sta sulla foto in basso a sinistra (Hays, Coffee Collective, Acacia, Knupfer) o subito sotto (Arc).
- Da 3 a 5 elementi in tutto: logo, menu, una frase, al massimo un link o un bottone. Nessuno ha due bottoni, una fila di ingressi o una fascia di cifre in prima schermata.
- Il mestiere è detto in una frase sola, non in un titolo più un sottotitolo più un occhiello.

**Tipografia**
- Una famiglia sola in 5 su 8 (Arc, Hays, Knupfer, Coffee Collective, Palet con la sua condensata); due in 3 (The Olly, Kevala, Acacia).
- Pesi leggeri o normali: 300-500. Il nero pesante è quasi assente.
- Titoli tra 50 e 130 px con interlinea da 0,85 a 1,1; un solo gesto più grande (logotipo o parola di sezione a 250-350 px).
- Arc usa 3 misure in tutta la home, Knupfer 10 contando i giganti.
- Etichette di sezione piccole e regolari: maiuscolo spaziato (Acacia), riquadro (Palet), pallino o quadratino (Kevala, Knupfer).

**Foto**
- Una serie per sito: stesso fotografo, stessa luce (crepuscolo per Cedar Springs, luce di finestra per Hays, macro radente per Kevala e Palet).
- Prodotto e reportage tenuti separati (Coffee Collective: confezioni su crema, origine e negozi in luce naturale).
- Sotto le foto dei lavori: nome del lavoro, luogo o cliente, a volte l'anno. Mai una frase descrittiva.

**Griglia e ritmo**
- Margini piccoli (Arc 16 px, Palet 32, Kevala 33, Coffee Collective 40, Knupfer 60) e foto al vivo.
- Alternanza fissa: foto grande, bianco con una frase, griglia di 3 lavori, blocco di colore pieno, piede. 6-9 sezioni.
- I filetti servono a dividere le righe di un elenco, non le sezioni.

**Testi**
- Brevi e con fatti: anni, nomi di persone, vie, clienti, quantità, tempi. "Available from 1 square meter with lead times starting at 8 weeks" (Palet). "Trusted by 150+ Hotels and 200+ Restaurants, Handmade by 150 Artisans" (Kevala). "1991 wurde Knupfer Metallbau von Josef Knupfer gegründet" (Knupfer).
- Gli slogan ci sono ("get away every day", "Architecture, Built for Life.") ma sono una riga, e la seconda riga dice il mestiere.

### Effetti da giuria: a una piccola azienda fanno perdere clienti
- **Caricamenti con percentuale o logo** (Kevala 22,7 s, The Olly, Don Molinico, Marvell 11,8 s). Chi cerca un'officina dal telefono in cantiere non aspetta. Da non fare mai.
- **Video di sfondo** (Artisans de Genève 144 MB, Myne 31, Coffee Collective 19, Knupfer 14). Sul 4G di un artigiano è un minuto di traffico; quando non carica resta un grigio vuoto (Acacia in cattura). Una foto ferma fa lo stesso lavoro.
- **WebGL, tele trascinabili, scorrimento orizzontale** (PrimeAsia, Gufram, Marvell, OWL, House of Corto). La home non dice chi sei, non ha telefono, non si legge a 390. Servono alla giuria, non al cliente.
- **Contenuto che appare solo scorrendo** (Knupfer, Siegesmund, Don Molinico, The Olly). Nelle catture metà pagina è bianca: se lo script si blocca, il cliente vede il vuoto. È già vietato dal committente.
- **Pop-up di newsletter e sconti** (Assembly, MGG, Palet, Coffee Collective): coprono la pagina alla prima visita.
- **Testo minuscolo** (Kevala 11 px, House of Corto 7-11 px, CoffeeTech e MGG 14 px): a giudicare è un designer su un monitor grande, non il cliente.
- **Menu nascosto dietro "Menu" anche a 1440** (Kevala, PrimeAsia, Cedar Springs): un passaggio in più per trovare "Contatti".
- **Il corsivo serif per le parole d'accento** (Siegesmund, Assembly) e **Inter dappertutto** (CoffeeTech) sono premiati lo stesso: il voto non è una garanzia di gusto, e restano vietati da noi.

---

## 4. Le 10 mosse per le nostre home

Il problema delle nostre home è uno schema ripetuto: titolo a sinistra, foto a destra, due bottoni, fila di ingressi, fascia di cifre. Le mosse rompono quello schema senza chiedere foto che non abbiamo.

1. **Prima schermata a tre elementi.** Una foto vera a tutta larghezza (o mossa 2), una frase sola sulla foto in basso a sinistra che dice mestiere e luogo, un solo link. Il telefono resta nella testata fissa. Via il secondo bottone, la fila di ingressi e le cifre dalla prima schermata.
   *Esempio:* Hays (foto della cucina, frase di 65 px in basso a sinistra, un link); Coffee Collective; Arc.
   *Serve:* la foto orizzontale migliore che l'azienda ha, anche vecchia, purché nitida a 1440; impaginazione.

2. **Se la foto è debole, il nome diventa l'immagine.** Il nome dell'azienda a 250-350 px sopra una foto dell'officina o della sede scurita al 50-60%, con il mestiere in una riga sotto.
   *Esempio:* Knupfer ("Knupfer" a 346 px e "Metallbau" sopra il video del capannone); Marvell (nome a 256 px).
   *Serve:* una foto qualsiasi della sede o del reparto, anche da telefono, perché finisce scurita e sotto il testo; solo impaginazione.

3. **I lavori con il nome, il luogo e l'anno.** Ogni foto di lavoro ha sotto due voci regolari: a sinistra il lavoro e il luogo (o il cliente), a destra la categoria o l'anno. Tutte le foto nello stesso taglio.
   *Esempio:* Kevala ("Cantina Kahlo, Ritz Carlton Bahrain / 2024"); Arc ("Smash Repair House / Matt Elkan"); Knupfer ("Mehrfamilienhaus Ulm / Fensterlösungen"); Acacia (il nome della via).
   *Serve:* l'elenco dei lavori dal titolare (testo, con il permesso di nominare il cliente) e foto anche da telefono, ritagliate tutte 4:3 o 3:4.

4. **Una frase-prova al posto della fascia di cifre.** I numeri dentro una frase intera, vicina all'azione: quanti clienti, il minimo d'ordine, i tempi, l'anno di fondazione con il nome del fondatore.
   *Esempio:* Palet ("available from 1 square meter with lead times starting at 8 weeks"); Kevala ("Trusted by 150+ Hotels and 200+ Restaurants"); Knupfer (la fondazione del 1991 in una frase di 45 px).
   *Serve:* dati veri chiesti al titolare; solo testo.

5. **Una famiglia di caratteri, tre-cinque misure, pesi 400-500.** La gerarchia si fa con la misura del titolo e con lo spazio, non con 9 misure e il grassetto.
   *Esempio:* Arc (Neue Haas Grotesk Display 500, solo 12, 16 e 33 px); Hays (Archivo 350); Myne (TT Hoves, 5 misure).
   *Serve:* solo CSS. Scelta per famiglia: un grottesco con una larghezza condensata per M, un grottesco morbido per S, per B il carattere che richiama l'insegna.

6. **Il colore del marchio pieno su un blocco intero, una volta per pagina.** Non sui bottoni e sui filetti, ma come fondo di una sezione (manifesto, negozi, chiusura).
   *Esempio:* The Olly (rosso del logo pieno per il manifesto e i cinque negozi); Don Molinico (rosso e giallo della confezione); Coffee Collective (blocco color bacca per un caffè).
   *Serve:* il colore preso dal logo, dall'insegna, dall'etichetta o dalla livrea dei mezzi; solo CSS.

7. **I servizi come righe di indice, numerate.** Una riga per servizio, nome a 40-45 px, freccia a destra, filetto sotto; a 1440 la foto può comparire nella riga, a 390 sta sopra il nome.
   *Esempio:* Hays (7 righe "Architectural Features... Workspaces"); Knupfer (01-04 con foto piccola); CoffeeTech (Technology, Efficiency, Sustainability).
   *Serve:* solo impaginazione; le foto sono facoltative, e questo risolve i servizi senza foto di MeccanicaMasi, Belletti, BordinGarden.

8. **Negozi e sedi come schede con la tabella degli orari.** Nome, indirizzo e telefono, poi gli orari giorno per giorno, poi che cosa si trova lì; la facciata in foto se c'è.
   *Esempio:* The Olly (5 schede con orari e tipo, il bollino solo sul negozio che fa pranzo); Coffee Collective e Assembly (la facciata fotografata con il nome sotto).
   *Serve:* gli orari veri e una foto della facciata da telefono, presa di giorno e dritta; impaginazione.

9. **Una persona con nome e frase.** Il titolare con una sua frase firmata, o la squadra con le divise; per chi fornisce aziende, il cliente con nome e ditta.
   *Esempio:* Hays (citazione firmata "Chris Hay, Founder"); The Olly (firma "Oliviero Silvani"); CoffeeTech (ritratto del fondatore con firma; testimonianza "01" con "Mark Jones, Java Jones Roasters"); Arc (la squadra in polo).
   *Serve:* una frase vera del titolare o di un cliente, con il permesso; un ritratto anche da telefono, vicino a una finestra.

10. **Il piede come biglietto da visita.** Ragione sociale a 30-40 px, poi indirizzo, telefono ed email a 20-22 px cliccabili, partita IVA, la dicitura dei finanziamenti europei impaginata come il resto; il nome a tutta larghezza se l'azienda ha un logotipo forte.
    *Esempio:* Hays ("Hays Woodworking Group Inc." grande, contatti a 22 px); Arc (ragione sociale legale); Coffee Collective (il CVR); Don Molinico (FEADER e Navarra); Bernice (nome a tutta larghezza).
    *Serve:* solo testo e impaginazione.

Da tenere a lato: il fondo che richiama il mestiere (la fuga delle piastrelle di Marvell, fatta con due righe di CSS) e i disegni tecnici veri dell'azienda come immagine (la pianta di Cedar Springs). Sono documenti del lavoro, non illustrazioni al posto delle foto. Si usano in un solo punto della pagina e solo se il disegno esiste davvero.
