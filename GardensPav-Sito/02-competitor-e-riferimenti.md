# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. 5 concorrenti e 28 siti di riferimento aperti con Playwright (Chromium) a 1440 e a 390 px; screenshot in `_prova/ricerca/` (`c*-` concorrenti, `r-*` riferimenti), pezzi ritagliati in `_prova/ricerca/ritagli/` (numerati 00-24, citati qui sotto). Caratteri e colori dei siti letti dal browser (stile calcolato e font caricati), non a occhio.

Limiti incontrati, da sapere prima di riaprire i siti:
- Gazebo blocca il browser automatico da desktop con un captcha BitNinja (`c4-gazebo-1440-vista.png`): la versione da telefono si è caricata ed è quella analizzata.
- Escofet ha risposto bene al primo accesso (pagina intera a 1440 e prima schermata a 390), poi 503: il carattere esatto non è stato letto dal browser, è descritto da quello che si vede.
- Decomo, Stradal, Baraclit, Concrete Canvas restano bianchi al browser automatico, Ronveaux non risponde, IBF mostra un video in errore. Non usati.

## Premessa: che cosa è Gardens Pav e con che cosa lavoriamo

Dal sito attuale (`http://www.gardenspav.it`, pagine scaricate in `_prova/crawl/`): Gardens - Pav S.r.l., "opere in calcestruzzo" (sotto il logo), Via Romea 154/A, Legnaro (PD), tel. 049 641591. Tre famiglie nel menu:
- **Vasche prefabbricate monoblocco**: rettangolari, circolari, trattate con resine epossidiche;
- **Depurazione**: dissabbiatore statico, separatore grassi CE, vasca Imhoff, separatore oli CE con filtro a coalescenza, separatore oli CE per autorimesse e garages, impianti di trattamento acque di prima pioggia, depuratori biologici;
- **Piattaforme per autolavaggi**: pannelli prefabbricati per pista self (mod. 450, 500, 500 doppia griglia) e per portale (mod. 1-5), "Brevetto per invenzione industriale depositato n° 275.271".

Le pavimentazioni per esterni, che il nome farebbe pensare, non hanno una pagina nel sito attuale: **[DA CONFERMARE]** se le producono ancora.

Il materiale che l'azienda ha già, ed è la base di tutto quello che segue (`ritagli/00-gardenspav-materiale-proprio.jpg`):
- **render 3D di ogni vasca e di ogni impianto di depurazione, 1500-1600 px di larghezza** (per le piattaforme ci sono solo foto), su fondo bianco, molti in sezione (si vede l'acqua, il fango, i tubi di ingresso e uscita). Calcestruzzo grigio freddo (misurato #C4C7C7 in media) e **tubi in PVC arancio** (#D76B03 circa);
- un **disegno al tratto arancio** di vasca circolare e vasca rettangolare (assonometria, 248 x 667 px: va ridisegnato in SVG);
- il **logo**: arancio #F38239 e grigio #58585A, misurati sul file, e la scritta "opere in calcestruzzo" spaziata in minuscolo;
- **foto del piazzale** (anelli in calcestruzzo, vasche bianche con i fori arancio, piattaforme con le griglie verdi): 930 x 400 px, quindi mai a tutta larghezza a 1440.

L'arancio del logo e l'arancio dei tubi nei render sono lo stesso segno: l'identità del nuovo sito nasce da qui, calcestruzzo grigio e tubo arancio, non da una tavolozza scelta a tavolino.

## 1. Concorrenti

| # | Concorrente | Zona | In comune con Gardens Pav | Cosa fa meglio | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Veneta Prefabbricati](https://www.venetaprefabbricatipadova.com/) | San Pietro Viminario (PD) | vasche in c.a. vibrato, separatori, prima pioggia UNI EN 858, depuratori anche per il lavaggio mezzi | telefono +39 0429 760173 in alto e in un riquadro dedicato; foto vere di consegna con camion gru; menu per tipo di cliente (civile, industriale) | template Italiaonline con tre box a icona, foto stock (mano che disegna, persona al computer), un numero fermo al 2012 ("a dicembre 2012 ... superava le 6.000 unità"), una chat AI che si apre da sola sopra i prodotti | `c1-veneta-1440.png`, `c1-veneta-390.png` |
| 2 | [Manufatti Polonio](https://www.manufattipolonio.it/) | Conselve (PD) | manufatti in cemento, anelli, pozzetti, caditoie | orari di apertura, telefono e mail in cima; ogni prodotto ha "Su preventivo" e i tasti telefono e WhatsApp (`ritagli/24`); vendita al dettaglio in sede detta chiaramente | la pagina del dominio non ha nemmeno un titolo e incorpora in un iframe il sito vero, ospitato su xlist.it; foto sgranate con filigrana, frase generica in apertura ("50 anni di esperienza, professionalità, servizio e qualità") | `c2-polonio-*.png` |
| 3 | [Micheletto](https://www.michelettopavimenti.it/) | San Giorgio delle Pertiche (PD) | pavimentazioni per esterni in calcestruzzo | dichiarazione EPD dei masselli, premi di design citati con l'anno (BIG SEE 2024 e 2025), primi piani della superficie del prodotto (graniglie, gocce sulla pietra) | slogan in inglese ("Elements of space"), schede a bordi tondi bianche su fondo nero, pulsanti fucsia e verdi, icone in cerchi arancio, testo giustificato a 390 con buchi tra le parole, sezione "I nostri marchi" vuota | `c3-micheletto-*.png` |
| 4 | [Gazebo S.p.A.](https://www.gazebo.it/) | Gatteo (FC), concorrente diretto nazionale | vasche monoblocco in c.a., depurazione, prima pioggia, sollevamento | ogni impianto ha una foto vera (vasca calata dalla gru, scavo, posa), il cliente e il dato tecnico (abitanti equivalenti, superficie scolante); progettazione BIM; barra fissa su telefono con Chiamaci, Scrivi, Catalogo (`ritagli/23`) | testo grigio centrato su tutta la pagina, lo stesso pulsante "approfondisci" ripetuto decine di volte, 17.871 px di pagina a 390; da desktop il browser automatico è stato fermato da un captcha | `c4-gazebo-390.png` |
| 5 | [Ferrari BK](https://ferraribk.it/) | Lugo di Grezzana (VR) | pavimentazioni, blocchi, cordoli in calcestruzzo | porta separata per il progettista (portale BIM, area download, manuali di posa) e per il privato (`ritagli/22`); casi realizzati con il nome del luogo; P.IVA in fondo pagina; versione mobile pulita | foto stock (ragazzo col monopattino, uomo col casco sul progetto), frasi generiche ("Qualità, affidabilità e durevolezza: i nostri prodotti in tre parole"), Inter come carattere unico | `c5-ferraribk-*.png` |

Il sito attuale di Gardens Pav, per confronto (`c0-gardenspav-1440.png`, `c0-gardenspav-390.png`): impaginazione fissa del 2008 a tabelle, a 390 si impagina a 980 px e si rimpicciolisce, nessun https; le tre famiglie sono in home ma con miniature da 202 px; i render da 1600 px stanno solo dentro le pagine prodotto. Caratteri del foglio di stile: Helvetica, Arial, Karla.

**Cosa fanno i migliori:** foto vere del prodotto posato o in consegna (Gazebo, Veneta); il dato tecnico vicino alla foto (abitanti equivalenti, metri quadri); un contatto a un tocco su ogni prodotto (Polonio, Gazebo); una porta per il progettista con documenti scaricabili (Ferrari BK, Gazebo con il BIM).

**Cosa non fa nessuno, ed è spazio per Gardens Pav:**
1. **Piattaforme prefabbricate per autolavaggio**: nessuno dei concorrenti visti le produce. Veneta e Gazebo trattano l'acqua del lavaggio, non fanno la pista. In una ricerca mirata ("piste di lavaggio prefabbricate", "pavimentazione prefabbricata per autolavaggio") non è uscito un altro produttore. Va detto con prudenza (non abbiamo verificato tutto il mercato), ma è la pagina che può portare richieste nuove.
2. **Il prodotto mostrato in sezione**: Gardens Pav ha i render di ogni vasca con l'acqua e i tubi dentro. Nessun concorrente locale li ha (Veneta usa foto di cantiere e stock, Polonio foto sgranate); solo i riferimenti esteri qui sotto mostrano il prodotto così.
3. **Le norme scritte vicino al prodotto**: la pagina azienda attuale cita UNI EN 858-1:2005, UNI EN 1825-1:2005, UNI EN ISO 9001:2015, Rck 45 N/mm2 **[DA CONFERMARE: la pagina è in parte illeggibile, i valori vanno ricontrollati col cliente]**. Messe su ogni scheda, con un PDF scaricabile, sono quello che cerca un progettista o un'impresa.
4. **Freschezza**: numeri fermi a un anno vecchio (Veneta), sezioni vuote (Micheletto), siti in iframe (Polonio). Basta un sito aggiornato e con https per stare davanti a tutti e tre i vicini.

**Posizionamento proposto per 03 (bozza):** "Vasche monoblocco, impianti di depurazione e piattaforme per autolavaggio in calcestruzzo, prodotti a Legnaro." Contro Veneta (vicina, stessa offerta) Gardens Pav si distingue con le piattaforme brevettate e con il prodotto mostrato in sezione; contro Gazebo (nazionale, grandi impianti) con la vicinanza e la consegna dal piazzale di Legnaro **[DA CONFERMARE: zona di consegna e posa con personale proprio, citata nella locandina della home attuale "assistenza al montaggio con nostro personale"]**.

**Copy da non ripetere** (visto nei concorrenti): frasi di apertura che vanno bene per chiunque ("depura il nostro pianeta", "50 anni di esperienza, professionalità, servizio e qualità", "i nostri prodotti in tre parole"), slogan in inglese, contatori che invecchiano. Si scrive l'anno o il numero di modello, non "da X anni". Le parole di `PAROLE_VIETATE` (build.py) restano fuori.

## 2. Riferimenti premium

Gardens Pav vende manufatti in calcestruzzo che finiscono sotto terra o sotto le ruote: chi compra è un'impresa, un idraulico, un progettista, il gestore di un autolavaggio. Il riferimento giusto non è un marchio di arredo, ma i produttori di prefabbricati in calcestruzzo e di sistemi per l'acqua che hanno siti di livello alto. Li ho aperti tutti il 6 ottobre 2026. Quelli buoni hanno in comune: il prodotto mostrato come un oggetto tecnico (render o disegno su fondo chiaro), il luogo e il dato scritti piccoli accanto alla foto, un grottesco senza grazie, un solo colore d'accento usato poco.

| Riferimento | Che cosa è | Il gesto preciso da riprendere | Dove nel sito Gardens Pav | Cosa evitare | Ritagli |
|---|---|---|---|---|---|
| [Jensen Precast](https://www.jensenprecast.com/) | prefabbricati in calcestruzzo per le infrastrutture, ovest degli Stati Uniti: pozzetti, tubi, vasche, intercettori e fosse settiche | **"Find Products Fast"**: griglia 4 x 2 di schede grigio chiaro, nome della famiglia in grassetto in alto, i sottoprodotti in piccolo separati da " · ", il render del prodotto al centro sul fondo della scheda, link piccolo in basso; a 390 diventa 2 colonne con la stessa scheda. **Cantieri**: luogo in grigio piccolo sopra il titolo ("Kent, Washington"). **Il tubo come cornice**: la foto dell'operatore inquadrata dentro un tubo | indice delle famiglie in Home e pagina Prodotti, con i render da 1600 px scontornati; pagina Piattaforme con i modelli elencati come sottoprodotti | pulsanti gialli e titoli ottanio, barra di ricerca sopra la foto d'apertura, illustrazioni 3D di persone | 05, 06, 07, 08 |
| [Escofet](https://www.escofet.com/) | arredo urbano e pavimenti in calcestruzzo prefabbricato, Spagna (gruppo Molins) | **Didascalia in monospazio maiuscolo** sotto ogni foto con il luogo ("LA EXPLANADA . ALICANTE . ES"), anche a 390 sopra la foto d'apertura. **Schede "Highlights"**: due colonne, foto a sinistra, titolo grande in alto e testo piccolo in basso a destra, ogni scheda chiusa da un filetto nero sottile. Prodotto fotografato dall'alto, nello spazio vero. L'arancio usato per una sola rubrica | didascalie dei render e delle foto con codice e misura ("MOD. 500 · DOPPIA GRIGLIA"); blocco "Documenti e norme" a schede con filetto | titoli giganti in peso leggero su più righe, menu tutto in monospazio minuscolo (un tecnico di fretta non lo legge), mosaico senza gerarchia | 01, 02, 03, 04 |
| [Rieder](https://www.rieder.cc/us/) | facciate in calcestruzzo fibrorinforzato, Maishofen (Austria) | **Schede prodotto senza foto**: campo pieno del colore del materiale, il pezzo disegnato al tratto sopra (formparts: cilindri e pieghe), nome al centro. **Campioni** fotografati dall'alto con didascalia sotto. **Il dettaglio costruttivo** mostrato com'è (staffe e ancoraggi). A 390 le schede vanno a zig-zag | il disegno al tratto arancio che Gardens Pav ha già (vasca circolare e rettangolare), ridisegnato in SVG, come segno delle famiglie; una foto del dettaglio (tubo di ingresso, griglia della piattaforma) per ogni prodotto quando ci saranno foto nuove | fondo panna #FCF9F6 (è il crema bocciato su Benvegnù), il serif display "Concrete loves timber", sezioni intere vuote. Caratteri: Tomato Grotesk e PP Grafier, non su Google Fonts | 09, 10, 11 |
| [Forterra](https://www.forterra.co.uk/) | laterizi e prefabbricati in calcestruzzo, Regno Unito | **Schede scure** con foto vera, filetto chiaro sopra il titolo, "Find out more" in basso separato da un secondo filetto; **foto della produzione** (mattoni sul nastro) dentro una fascia con contatore "01/04" | una fascia grafite "Dal piazzale di Legnaro" con le foto vere (anelli, vasche, piattaforme) a dimensione nativa | titoli condensati maiuscoli (Giorgio Sans): è la strada già presa per Benvegnù con Barlow Condensed, qui no; l'azzurro dei pulsanti | 12, 13 |
| [Mall Umweltsysteme](https://www.mall.info/) | vasche in calcestruzzo per acque meteoriche, separatori, depuratori, Germania: è l'equivalente tedesco di Gardens Pav | sito datato (Arial, foto stock di foglie e boschi), ma con due idee giuste: **l'illustrazione in sezione di un'area** (distributore, autolavaggio, capannone) con le vasche disegnate sotto terra per scegliere il prodotto da dove si usa; **strumenti per il progettista** (programmi di dimensionamento, questionari di progetto, download) | una sezione "Dove si usano" costruita con i render in sezione di Gardens Pav; un modulo di richiesta con i dati che servono per scegliere la vasca **[DA CONFERMARE con l'azienda quali dati chiede]** | foto stock della natura, verde acido, barra laterale di icone fissa | 14, 15 |
| [ACO](https://www.aco.it/) | drenaggio e trattamento acque, gruppo tedesco con sede italiana | **il ciclo dell'acqua in quattro verbi** in sequenza (Collect, Clean, Hold, Reuse) sopra una sezione del terreno | la pagina Depurazione ordinata per il percorso dell'acqua: raccogliere, separare (dissabbiatore, separatori), trattare (Imhoff, biologico), scaricare (prima pioggia), con i render | apertura vuota, pittogrammi in quadratini (icone in fila), foto di gruppo in posa | 16 |
| [Godelmann](https://www.godelmann.de/) | pietre e lastre in calcestruzzo, Germania | **la referenza nomina i prodotti usati**: una foto grande, il luogo, e il testo che dice quali pezzi sono stati posati e perché | pagina Realizzazioni, quando ci saranno foto e permesso dei clienti **[DA CONFERMARE]**; ogni realizzazione rimanda alla scheda del prodotto | titoli metà leggeri e metà grassetto, verde salvia, persone sorridenti in posa | 17 |
| [Kann](https://www.kann.de/) | pavimentazioni in calcestruzzo, Germania | **striscia di disegni assonometrici al tratto** dei prodotti come indice, con barra di avanzamento sottile; **il prodotto in sezione a strati** su fondo grigio | variante dell'indice famiglie su telefono (striscia scorrevole di disegni con `data-scorre`) | blu notte con foto stock di coppia, titoli maiuscoli condensati leggeri, bollini verdi | 18, 19 |

Gesti utili presi da siti che nel complesso non sono riferimenti:
- [SW Umwelttechnik](https://www.sw-umwelttechnik.com/) (prefabbricati per infrastrutture, Austria): il **piazzale di manufatti in calcestruzzo usato come fondale** dell'apertura (`ritagli/21`). Gardens Pav ha la foto degli anelli: va bene come fondale, non come foto da ingrandire.
- [ULMA Architectural](https://www.ulmaarchitectural.com/it-it) (canali di drenaggio, Spagna): **il prodotto fotografato nel suo posto con il terreno tagliato** sotto la foto (`ritagli/20`): stesso principio dei render in sezione di Gardens Pav.

Aperti e scartati: Metten (popup e sezioni che compaiono in dissolvenza), Rinn e Urbastyle (foto stock, scelta del paese prima del sito), Marshalls e Swisspearl (schede vuote, immagini non caricate), Istobal (apertura al neon), Christ Wash Systems (grandi vuoti), Kessel (viola e stock), Müller-Steinag (icone giganti in fila), Oldcastle Infrastructure (menu che si sovrappone al titolo), Idealwork (vuoti da dissolvenza), Decomo, Stradal, Baraclit, Concrete Canvas, Ronveaux, IBF (non caricati, vedi sopra).

## 3. Cosa si riprende (sezione per sezione)

| Sezione del nuovo sito | Gesto | Da chi | Con quale materiale di Gardens Pav |
|---|---|---|---|
| Testata | telefono 049 641591 e mail sempre visibili, su telefono un tasto "Chiama" fisso in basso che non copre i titoli | Gazebo (mobile), Polonio | dati dal piè di pagina attuale |
| Apertura Home | foto vera del piazzale a dimensione nativa (930 px) accanto a un titolo semplice, non a tutta larghezza | SW Umwelttechnik, Jensen | `gallery_home/_bigPhotos/005.jpg` (anelli), `006.jpg` (vasche) |
| Indice delle famiglie | griglia di schede chiare con render, nome, sottoprodotti in piccolo separati da " · " | Jensen | render da 1600 px scontornati (fondo bianco puro, si toglie in `prepara_immagini.py`) |
| Segno delle famiglie | disegno al tratto arancio del pezzo | Rieder, Kann | il loro disegno di vasca circolare e rettangolare, ridisegnato in SVG |
| Depurazione | percorso dell'acqua in quattro verbi, ogni passo con il suo render in sezione | ACO, Mall | render di dissabbiatore, separatori, Imhoff, prima pioggia, biologico |
| Piattaforme per autolavaggi | blocco foto + tre caratteristiche + "Vedi i modelli"; modelli elencati come sottoprodotti con didascalia in monospazio | Jensen (blocco "Reinforced Concrete Pipe"), Escofet | testi verbatim della pagina attuale, brevetto n° 275.271, foto `004.jpg` e locandina `002.jpg` |
| Didascalie | codice del modello, norma, misura in monospazio piccolo sotto il render | Escofet | dati delle pagine prodotto (da 01) |
| Documenti | schede con filetto, una per prodotto, con PDF scaricabile | Ferrari BK (porta del progettista), Mall | **[DA CONFERMARE]** schede tecniche e dichiarazioni di prestazione disponibili |
| Dal piazzale | una fascia scura con foto vere e filetto chiaro | Forterra | foto del piazzale (930 px) |
| Realizzazioni | luogo piccolo sopra il titolo, prodotti usati nominati | Jensen, Godelmann | **[DA CONFERMARE]**: oggi non ci sono referenze pubbliche |

Scartato per tutti: caroselli automatici, foto stock, chat AI che si apre da sola, tre box con icona, contatori animati, sezioni in dissolvenza, slogan in inglese, foto mostrate oltre la loro risoluzione.

## 4. Accoppiate

Nessuno dei riferimenti del settore usa un serif nei titoli (l'unico, Rieder, lo usa in uno slogan d'apertura, scartato): niente serif e niente fondo crema. Tutti usano un carattere senza grazie (Jensen il Neue Haas Grotesk, Forterra l'Akzidenz Grotesk, Rieder il Tomato Grotesk, Godelmann il Meta Pro); Escofet affianca un monospazio per le didascalie. I concorrenti usano Source Sans Pro (Veneta), Public Sans e Abel (Micheletto), Inter (Ferrari BK), Glacial Indifference (Polonio): le accoppiate qui sotto non ne ripetono nessuno. I colori partono dal materiale misurato: grigio freddo del calcestruzzo nei render (#C4C7C7) e arancio del logo (#F38239).

Rapporti di contrasto calcolati con la formula WCAG 2.1. L'arancio del logo su bianco fa 2,6:1: **non si usa mai per il testo su fondo chiaro**, solo per segni grafici grandi, per i tubi e come fondo di un pulsante con testo scuro.

### A. "Catalogo di cantiere": Archivo + IBM Plex Mono (consigliata)

Da Jensen (grottesco pieno, titoli in minuscolo in grassetto stretto, catalogo su schede chiare) ed Escofet (monospazio per le didascalie con il luogo). È la più vicina a quello che Gardens Pav vende: prodotti con un numero di modello, una norma e una misura.

- **Archivo** (Google Fonts) 700 per i titoli, in minuscolo, interlinea stretta; 400 e 500 per testo e menu. È un grottesco pieno, vicino al Neue Haas Grotesk di Jensen, con pesi da 100 a 900 e un asse di larghezza: si usa a larghezza normale (il condensato è la strada di Benvegnù).
- **IBM Plex Mono** (Google Fonts) 400 e 500, maiuscolo spaziato, 12-13 px: codici e modelli ("MOD. 500 · DOPPIA GRIGLIA"), norme ("UNI EN 858-1"), didascalie con luogo ("LEGNARO · PD"). Mai per i paragrafi.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | Bianco #FFFFFF | |
| Schede del catalogo, fasce di servizio | Calcestruzzo chiaro #EBECEB (il grigio dei render schiarito) | |
| Testo, titoli, fascia scura | Grafite #1D1E1F | 16,7:1 su bianco; 14,1:1 su #EBECEB |
| Testo secondario, didascalie | Grigio logo #58585A | 7,1:1 su bianco; 6,0:1 su #EBECEB |
| Link nel testo, voce di menu attiva | Arancio scuro #A6470A | 5,95:1 su bianco; 5,03:1 su #EBECEB |
| Segni, filetti da 3 px, pulsante pieno | Arancio Gardens Pav #F38239 | testo grafite sul pulsante 6,41:1; arancio su grafite 6,41:1 (numeri e filetti nella fascia scura) |
| Testo su fascia scura | Bianco #FFFFFF su #1D1E1F | 16,7:1 |

Hover: il pulsante arancio diventa grafite pieno con testo bianco; il link arancio scuro diventa grafite. Mai opacità.

### B. "Disegno al tratto": Hanken Grotesk, una famiglia

Da Rieder (schede prodotto fatte di un campo del colore del materiale e del pezzo disegnato al tratto; titoli grandi in peso regolare) e Kann (indice di disegni assonometrici), e dal disegno arancio che Gardens Pav ha già. È la più calma: funziona se le foto restano poche, ma chiede di ridisegnare in SVG almeno sei pezzi.

- **Hanken Grotesk** (Google Fonts) 300 e 400 per titoli grandi (come il Tomato Grotesk regolare di Rieder e il Meta Pro leggero di Godelmann), 400 per il testo, 600 per etichette e menu. Un solo carattere, nessun monospazio.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | Bianco #FFFFFF | |
| Campi delle schede prodotto | Cemento chiaro #D9DBDA | |
| Fascia scura, piè di pagina | Cemento bagnato #4A4D4D | testo bianco 8,54:1; #D9DBDA su #4A4D4D 6,14:1 |
| Testo | Inchiostro #191A1A | 17,44:1 su bianco; 12,54:1 su #D9DBDA |
| Testo secondario | Grigio #5A5D5D | 6,65:1 su bianco |
| Tratto dei disegni su bianco | Arancio tratto #C25A17 | 4,4:1 su bianco (oltre il 3:1 chiesto ai grafici) |
| Tratto dei disegni su fondo scuro | Arancio Gardens Pav #F38239 | 3,28:1 su #4A4D4D (solo grafica, mai testo) |

Rischio: i campi grigi pieni con il disegno sopra, se ripetuti in ogni sezione, diventano piatti (la critica alla prima versione di Benvegnù). Vanno usati solo nell'indice delle famiglie.

### C. "Officina": IBM Plex Sans + IBM Plex Mono

Da Forterra (schede scure con foto vera di produzione e filetto chiaro; il suo Akzidenz Grotesk è un grottesco industriale) e da Mall (il tono dello strumento tecnico). Una sola superfamiglia, disegnata per IBM: titoli, testo e dati parlano la stessa lingua. Più dura e più "da capitolato" della A.

- **IBM Plex Sans** (Google Fonts) 600 per i titoli, 400 per il testo; **IBM Plex Mono** 400 per dati, codici e tabelle delle misure.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fasce e schede scure | Grafite #202122 | testo bianco 16,13:1 |
| Testo secondario su scuro | Grigio render #C4C7C7 | 9,48:1 su #202122 |
| Numeri, filetti, voce attiva su scuro | Arancio Gardens Pav #F38239 | 6,19:1 su #202122 (anche per testo) |
| Fondo chiaro | Bianco #FFFFFF | testo grafite 16,13:1 |
| Testo secondario su chiaro | Grigio #646767 | 5,71:1 su bianco |
| Pulsante | #F38239 con testo #202122 | 6,19:1 |

Rischio: con le foto del piazzale a 930 px, molte fasce scure a foto piena non si possono fare senza ingrandire le immagini. Una fascia sola.

### Scelta consigliata per la fase 2.3

**A**, con due innesti: dalla **B** il disegno al tratto arancio (#C25A17 su bianco) come segno di ogni famiglia nell'indice e nelle intestazioni di pagina; dalla **C** una sola fascia grafite "Dal piazzale" con le foto vere e i numeri arancio. Foto: render a colori su fondo chiaro come prodotto (il colore del tubo è un'informazione), foto del piazzale a colori a dimensione nativa, nessun viraggio. Se in 01 non emergono foto più grandi di 930 px, nel LEGGIMI va il brief delle foto da fare: piazzale, una vasca calata dalla gru, una piattaforma posata con un'auto sopra, dettaglio dei tubi di ingresso e uscita.
