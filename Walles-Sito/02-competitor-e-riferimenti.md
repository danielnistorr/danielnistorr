# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Ogni sito è stato aperto dal vivo con Playwright (Chromium attraverso il proxy) a 1440 e a 390 px e fotografato a pagina intera, dopo aver accettato i cookie e chiuso le finestre di newsletter e di scelta del paese. Visitati 8 concorrenti e 15 siti di riferimento, più 11 pagine interne (8 utili: le altre rispondono con una verifica antirobot o rimandano alla home); tenuti 6 concorrenti, 6 riferimenti premium e 3 funzionali.

File: screenshot in `_prova/ricerca/` (`w0-walles` il sito attuale, `c*` concorrenti, `r-*` home dei riferimenti, `p-*` pagine interne), ritagli dei gesti in `_prova/ricerca/ritagli/` (27 file numerati), campione delle tre accoppiate con foto vere di Walles in `_prova/ricerca/campioni/accoppiate-1440.png` e `accoppiate-390.png` (sorgente `accoppiate.html`). Script: `_prova/script/foto.mjs` (scatti), `ritagli.py`, `panoramica.py`, `guarda.py`, `foglio.py`.

Due avvertenze sugli scatti. Il Chromium di Playwright non ha il codec H.264: i video d'apertura in MP4 (Soldini, Fratelli Rossetti, Barrett, Zamberlan) escono neri o grigi e Soldini mostra il testo "Media error". Non è un difetto dei loro siti e non lo conto. I prezzi appaiono in dollari perché il proxy esce dagli Stati Uniti.

**Chi è Walles, per scegliere i riferimenti** (solo dal sito attuale, `_prova/crawl/`): calzaturificio di Rossano Veneto (Via Ramon 70/III). "Dal 1959 Walles realizza calzature di qualità secondo metodi tradizionali utilizzando una lavorazione artigianale italiana"; "Oggi, dopo tre generazioni, i fratelli Giacometti guidano l'azienda". Tre marchi propri: **Walles Club** ("Il valore dell'eleganza", anche pellami esotici: coccodrillo, tejus, struzzo, "nel rispetto delle norme internazionali CITES"), **Fratelli Giacometti** ("La tradizione artigianale e il gusto internazionale", "lavorazione Goodyear a mano") e **Marmolada** (lavorazione Norvegese "esclusivamente a mano", "colorazione a mano personalizzata", "trattamenti vintage"). Cinque lavorazioni spiegate con testo proprio: Goodyear, Norvegese, Mocassino tubolare, Blake, Finiture. Un outlet aperto al pubblico in Via Ramon 70/D: martedì-venerdì 14.00-19.00, sabato 9.00-13.00, lunedì e domenica chiuso.

Il materiale fotografico decide molto: 30 foto prodotto (7 Fratelli Giacometti, 8 Marmolada, 15 Walles Club), tutte quelle controllate 800x600, scattate su un fondo salvia sfumato i cui angoli sono esattamente **#93B1AF** in tutte le foto campionate, lo stesso colore del fondo pagina del sito attuale. In ogni foto è stampato a destra un cartellino "MODELLO FG105 / DESCRIZIONE Versione 1" (codici visti: FG105, FG231, 01405). In più 15 foto delle lavorazioni (tre per lavorazione, `blake1.jpg` è 536x534), una foto dello stabilimento (802x534) e i tre loghi (220x147). Nessuna foto supera gli 802 px: i riferimenti giusti sono quelli che mostrano il prodotto in schede di misura contenuta, non quelli che vivono di fotografie a tutto schermo.

Per questo i riferimenti sono **calzaturifici con fabbrica e marchio propri**, con Goodyear o Norvegese, origini di montagna o di campagna e uno spaccio di fabbrica: Paraboot, Ludwig Reiter, J.M. Weston, Heschung, Tricker's, Cheaney. Non case di moda.

## 1. Concorrenti

| # | Concorrente | Dove | Cosa vende (dal loro sito) | Cosa fa meglio di Walles oggi | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Diemme](https://diemme.com/) | Onè di Fonte (TV), circa 10 km in linea d'aria (stima) | scarponi e calzature per il tempo libero ispirati agli scarponi da lavoro e da montagna; "We make all Diemme products under one roof at our family factory in Onè di Fonte" (pagina About) | sito responsivo e venduto online; il racconto delle Dolomiti e della fabbrica di famiglia; un modello si chiama Marostica, cioè usa i nomi del territorio | la home sono due foto editoriali e il marchio gigante: nessun prodotto, nessuna lavorazione, nessuna fabbrica; testi in inglese | `c1-diemme-*` |
| 2 | [Zamberlan](https://www.zamberlan.com/it-it) | Torrebelvicino (VI), circa 39 km, stima ([aziende.it](https://www.aziende.it/calzaturificio-zamberlan-s-r-l)) | scarponi da trekking, caccia e lavoro; "Collezione Icona: Scarponi in pelle fatti a mano con classica costruzione norvegese cucita" | nomina la costruzione Norvegese in home, accanto ai prodotti; "Da tre generazioni" e "dal 1929" scritti come fatti; prodotti con nome e colore ("TOFANE GTX RR NW - Mattone"); guida alla manutenzione; voce Outlet nel menu | home lunghissima e affollata (stampa, recensioni, più caroselli); arancio e mondo tecnico: per una scarpa classica è il registro sbagliato | `c8-zamberlan-*`, ritaglio `24` |
| 3 | [Lemargo](https://www.lemargo.it/) (Calzaturificio Saint Ferry) | Montegranaro (FM) | calzature uomo e donna tinte in capo | spiega il suo colore: "le calzature Lemargo vengono immerse in vasche di colore seguendo un processo di colorazione tinto-capo"; foto in bianco e nero delle mani; schede prodotto su grigio chiaro con codice; fiere con date | titolo bianco su foto chiara nell'apertura, poco leggibile anche da telefono; striscia scorrevole di parole inglesi ("MATERIAL. DEPTH. FORM."); testo in Inter | `c5-lemargo-*`, ritaglio `25` |
| 4 | [Barrett](https://www.barrett.it/) | Parma | scarpe da uomo, "Made in Italy dal 1917" | negozio online con nomi che dicono la finitura ("Mocassino frangione in pelle anticata verde", "Derby in pelle spazzolata nera"): è il tema delle Finiture di Walles; servizio di personal shopper | modello Shopify standard; carosello in apertura; griglia Instagram; in home non si vede come sono fatte le scarpe | `c4-barrett-*` |
| 5 | [Calzaturificio Fratelli Soldini](https://calzaturificiosoldini.it/) | Capolona (AR) | più marchi: Soldini, Antica Cuoieria, Soldini Professional, Soldini80 | ha lo stesso problema di Walles, più marchi sotto un'azienda, e lo risolve con una tessera per marchio (logo, testo, "Scopri", "Trova negozio"); storia con date; fondo pagina completo; certificazioni | testi lunghi e superlativi nei titoli; foto piccole in bianco e nero; da telefono lunghi muri di testo | `c3-soldini-*`, ritaglio `26` |
| 6 | [Moreschi](https://moreschi.com/) | marchio nato a Vigevano; oggi "un marchio di Glam S.r.l.", Milano (fondo pagina) | scarpe e accessori da uomo, "dal 1946" | fotografa le scarpe tra le forme di legno: un'immagine vera del mestiere; boutique di Milano con indirizzo e orari nel fondo pagina | quattro icone di servizio in fila; sezione "Le nostre recensioni" vuota nel nostro scatto; la home non nomina più Vigevano, da dove secondo [Il Giorno](https://www.ilgiorno.it/economia/ultimaora/chiude-la-produzione-della-moreschi-addio-scarpe-a-vigevano-143b3e1f) (12 marzo 2024) la produzione è stata spostata | `c2-moreschi-*`, ritaglio `27` |

Aperti e non valutabili: [Fratelli Rossetti](https://www.fratellirossetti.com/) (apertura video, nel nostro browser nera, poi una lunga fascia vuota) e [Artioli](https://artioli.com/) (il menu esce senza stile e copre la pagina). [Fracap](https://fracap.com/) è un dominio in vendita; il dominio di Bettanin & Venturi rimanda a una pagina di parcheggio.

Tutti i concorrenti sono leggibili da telefono. Walles oggi no: a 390 px la pagina è larga 1001 px (`w0-walles-390.png`).

**Cosa fanno i migliori:**
- dicono la costruzione accanto al prodotto (Zamberlan: "classica costruzione norvegese cucita");
- danno al prodotto un nome che dice pelle e finitura (Barrett, Zamberlan);
- spiegano il proprio trattamento del colore (Lemargo, "tinto-capo");
- mettono in fila i propri marchi, uno per tessera (Soldini);
- nominano il luogo e la famiglia (Diemme, Zamberlan).

**Cosa non fa nessuno (lo spazio per Walles):**
1. **quattro costruzioni e la finitura spiegate con parole proprie.** Zamberlan nomina la Norvegese per una collezione, Lemargo spiega il colore; nessuno mette Goodyear, Norvegese, Blake e Mocassino tubolare una accanto all'altra. Walles ha già i testi e tre foto per ognuna;
2. **un marchio per lavorazione o materiale.** Fratelli Giacometti è Goodyear a mano, Marmolada è Norvegese a mano con colore a mano, Walles Club è pellame pregiato ed esotico. Soldini divide i marchi per linea e pubblico, nessuno per come è fatta la scarpa;
3. **uno spaccio in fabbrica con orari.** Nessun concorrente mostra in home un negozio di fabbrica con indirizzo e orari; Walles ce l'ha, in Via Ramon 70/D, lo stesso civico dello stabilimento (70/III);
4. **dire dove.** Moreschi ha tolto Vigevano dal racconto; Walles può scrivere Rossano Veneto in ogni pagina.

**Posizionamento proposto** (solo fatti del sito attuale): "Calzature classiche da uomo fatte a Rossano Veneto dal 1959. Goodyear, Norvegese, Blake e Mocassino tubolare, tre marchi propri e un outlet aperto al pubblico." Contro Diemme e Zamberlan (vicini, scarponi) Walles non gioca sul tecnico ma sulla scarpa classica e sullo scarpone Marmolada fatto in Norvegese a mano; contro Barrett e Moreschi (marchi classici con negozio online) gioca sulla fabbrica, sulle costruzioni e sul negozio sul posto. Il negozio online non c'è e non va promesso.

**Copy da evitare** (visto nei concorrenti): i superlativi dell'elenco `PAROLE_VIETATE` di `build.py` (Soldini e Moreschi li hanno nei titoli), "eleganza senza tempo", "trasforma ogni passo in un'emozione", gli slogan inglesi. Anche il sito attuale di Walles usa due parole dell'elenco (nella pagina Azienda e nella scheda Goodyear): nella riscrittura si tolgono e restano i fatti ("dopo tre generazioni", "fatta esclusivamente a mano", "due cuciture").

**Caratteri dei concorrenti** (da non usare, per distinguersi): Diemme HaasGrotesk; Moreschi Montserrat e Cabin; Soldini Roboto e Open Sans; Barrett DM Sans e Outfit; Lemargo Hepta Slab e Inter; Fratelli Rossetti Montserrat; Zamberlan Monda e Work Sans. Il sito attuale di Walles usa Georgia, corsivo nel menu.

## 2. Riferimenti

### 2.1 Riferimenti premium

Tratti comuni ai sei: fondo bianco o grigio caldo chiarissimo, interfaccia piccola, il colore lo portano la pelle e le foto. Il nome del modello è la parola più grande della scheda, sotto c'è una riga che dice pelle, colore o suola. La fabbrica si vede, con foto vere e il nome del luogo. Nessuno usa crema e corsivo.

#### Paraboot: [paraboot.com](https://www.paraboot.com/)
"Calzolaio francese dal 1908". Ateliers a Saint Jean de Moirans, in Isère, "entre les massifs du Vercors et de la Chartreuse": pedemontana come Rossano Veneto. Austin Light (graziato dritto, leggero) per titoli e nomi dei modelli, Maison Neue per il resto; verde scuro #153E35 per pulsanti e testi, fondo pagina #0A2C2B. Nella pagina "Nos ateliers": "Nos chaussures cousues Goodyear, cousues Norvégien ainsi qu'une partie de nos chaussures cousues Blake sont fabriquées à Saint Jean de Moirans", cioè tre delle quattro costruzioni di Walles. Lo scarpone Avoriaz "à l'origine technique, est inspiré des marches d'approche en montagne": lo stesso posto che ha FG105 tra i modelli Marmolada.
- **Gesto da riprendere:** (1) il nome del modello grande in graziato leggero e sotto una sola riga "pelle, suola" (`Chambord`, "Seta nera, suola in gomma"), alternato a destra e a sinistra della foto; (2) la pagina dell'atelier che nomina le costruzioni in neretto dentro il testo e le affianca a foto in bianco e nero di forme sugli scaffali; (3) il **Lessico**: indice delle parole in cinque colonne, poi una definizione per riga, separate da filetti; (4) tre porte in fondo alla home con foto d'archivio: "I nostri negozi", "La nostra storia", "Prodotto in Francia".
- **Da evitare:** l'apertura video con effetti al neon; i caroselli di prodotti a frecce; quattro icone di servizio in fila; la cartolina d'archivio su fondo verde funziona solo con un archivio vero, che Walles oggi non ha pubblicato.
- **Ritagli:** `01-paraboot-modello-pelle-suola`, `02-...-schede-nome-pelle-suola`, `03-...-tre-porte-archivio`, `04-...-atelier-goodyear-norvegese-blake`, `05-...-archivio-su-fondo-verde`, `06-...-lessico`, `07-...-avoriaz-scarpone-da-montagna`. Da telefono le schede scorrono di lato con la successiva tagliata (`r-paraboot-390.png`).

#### Ludwig Reiter: [ludwig-reiter.com](https://www.ludwig-reiter.com/de/)
"Wiener Familienbetrieb seit 1885" (dal testo della home), con modelli da escursione e dai nomi alpini (Gröbminger, Sport Hiking, Touring). Ubuntu: etichette 11-16 px in maiuscolo spaziato 1,2 px; ardesia #31323E per testata e fondo pagina; foto d'ambiente su fondo cammello. Schede prodotto su quadrati grigio caldo #E4E3DF, sotto: nome in neretto, **codice articolo**, pelle e colore, prezzo. Nella pagina dei negozi lo **spaccio di fabbrica** ("Ludwig Reiter Fabriksverkauf", Weingartenallee 2, Vienna) sta in fila con i negozi del centro: foto della casa, indirizzo, telefono, email. Orari del servizio clienti nel fondo pagina.
- **Gesto da riprendere:** (1) la scheda su campo uniforme con codice sotto il nome: Walles ha i codici (FG105, FG231, 01405) e un campo uniforme già nelle foto, il salvia; (2) lo spaccio presentato come un negozio, con la sua foto e i suoi recapiti; (3) quattro porte quadrate con un'etichetta (Handwerk, Geschichte, News, Stores), che da telefono diventano una griglia 2x2.
- **Da evitare:** a 1440 la pagina scorre di lato di 10 px (scrollWidth 1450); le etichette dentro riquadri bordati sopra le foto; il cammello per tutte le foto d'ambiente.
- **Ritagli:** `08-reiter-schede-codice-pelle`, `09-reiter-spaccio-di-fabbrica-tra-i-negozi`, `10-reiter-quattro-porte`.

#### J.M. Weston: [jmweston.com](https://jmweston.com/)
"French Master Shoemaker since 1891". Radiant EF (bastone a forte contrasto) per titoli e menu, Maison Neue per il testo; blu #3C4981 per i titoli di sezione. Scheda: foto su grigio #F1F2F3, nome, una riga di materiale ("Brown suede calfskin and brown sport calfskin"), numero di colori. Famiglie con il numero di modelli sotto il nome: "Loafers / 84 models", "Derbies / 32 models", "Boots / 21 models". Pagina "History & Savoir-faire": nove tessere quadrate con l'etichetta in basso.
- **Gesto da riprendere:** (1) la famiglia con il numero di modelli, per i tre marchi di Walles; (2) l'indice a tessere per la parte Azienda e Lavorazioni (storia, lavorazioni, finiture, outlet).
- **Da evitare:** la finestra di scelta del paese all'apertura; la cornice dorata spostata dietro le foto; tre servizi con icona in fila; testo a 12 px.
- **Condizione:** il numero di modelli per marchio non è pubblicato. Oggi il sito ha 7, 8 e 15 foto, non modelli: senza conferma il numero non si scrive [DA CONFERMARE].
- **Ritagli:** `11-weston-schede-con-materiale`, `12-weston-famiglie-con-numero-di-modelli`, `13-weston-indice-storia-e-mestiere`.

#### Heschung: [heschung.com](https://www.heschung.com/)
"Fabricant français de chaussures depuis 1934"; "les héritiers d'un savoir-faire historique du véritable cousu Norvégien et cousu Goodyear". Helvetica Neue in tutto il sito. Schede su quadrati grigio caldo #ECE8E5 con un'etichetta verticale piccola sul bordo ("TIMELESS", "NEW"). Il derby Crocus fotografato sul banco di lavoro, sotto i rocchetti di filo. Pagina del savoir-faire: tre capitoli con titolo in maiuscolo e testo, alternati a foto delle mani alla cucitura.
- **Gesto da riprendere:** (1) il capitolo del mestiere: titolo piccolo maiuscolo, testo breve, una foto delle mani alla cucitura; (2) il prodotto fotografato in fabbrica, sul banco, come brief per le foto nuove.
- **Da evitare:** la griglia sparsa di foto Instagram; testo centrato e chiaro; l'etichetta verticale "NEW" che invecchia.
- **Ritagli:** `17-heschung-schede-su-fondo-caldo`, `18-heschung-prodotto-sul-banco`, `19-heschung-cucitura-norvegese`.

#### Tricker's: [trickers.com](https://trickers.com/)
"Made in England since 1829". Sweet Sans Pro 600 maiuscolo per i titoli (largo, da incisore), Helvetica Neue Light per il testo; blu notte #101E2B. Pannello "Northampton through & through": metà fondo scuro con titolo e quattro righe ("every shoe and boot is made from start to finish in our Northampton factory"), metà foto di un operaio al banco. Negozi: tre facciate fotografate con città in maiuscolo e una riga. Prodotti su bianco con nome e finitura nel nome: "Bourton Country Shoe - Acorn Antique", "Espresso Burnished".
- **Gesto da riprendere:** (1) il pannello fabbrica, mezzo scuro e mezzo foto, per "Rossano Veneto, dal 1959"; (2) il nome della finitura come parte del nome del prodotto: è il tema delle Finiture di Walles (spruzzato, scurito, sfumato, vintage).
- **Da evitare:** le recensioni dei clienti in carosello (Walles non ne pubblica, non si inventano); il titolo bianco sopra la foto d'apertura; stemmi e mandati reali.
- **Ritagli:** `14-trickers-pannello-fabbrica`, `15-trickers-negozi-con-foto`, `16-trickers-nome-e-finitura`. La pagina "Our factory" risponde con una verifica antirobot.

#### Cheaney: [cheaney.co.uk](https://www.cheaney.co.uk/) (pagina [Factory Outlet](https://www.cheaney.co.uk/factory-outlet-i121))
"Handcrafted in Northamptonshire since 1886". Della home non si riprende l'aspetto (Playfair Display, il carattere del lusso generico). Si riprende la pagina dello **spaccio di fabbrica**: a sinistra ragione sociale, indirizzo, telefono, email e tabella degli orari (Mon-Fri 10:00-17:00, Sat, Sun), a destra la mappa; sotto una nota onesta, "Please note not all styles featured on the website are available in the factory shop"; poi i servizi in negozio (lucidatura, riparazioni) e tre foto del negozio, fuori e dentro.
- **Gesto da riprendere:** la pagina Outlet di Walles, uguale nell'ordine: chi, dove, quando, mappa, com'è dentro.
- **Da evitare:** Playfair Display; finestra newsletter; i servizi in negozio se Walles non li offre.
- **Condizione:** la nota "non tutti i modelli sono in outlet" e qualunque servizio in negozio vanno confermati [DA CONFERMARE]; le foto dell'outlet non esistono: brief nel LEGGIMI.
- **Ritagli:** `20-cheaney-spaccio-orari-mappa`, `21-cheaney-spaccio-foto-del-negozio`.

### 2.2 Riferimenti funzionali (contenuto giusto, aspetto da non riprendere)

| Riferimento | Cosa fa | Cosa si prende | Cosa no |
|---|---|---|---|
| [Crockett & Jones](https://www.crockettandjones.com/) (Northampton, "founded in 1879") | pagina [In the Making](https://www.crockettandjones.com/pages/in-the-making): otto fasi, ognuna su una fascia alterna grigio e bianco, testo da un lato e foto dall'altro; in home una fila di guide (forme, calzata, suole, materiali) | le cinque lavorazioni di Walles come capitoli alterni, una fascia ciascuno, ognuno con le sue tre foto | titoli in corsivo calligrafico ("Stage One"), cornici sottili sopra le foto, icone disegnate per le guide. Nel nostro scatto le foto delle fasi non si caricano. Ritagli `22`, `23` |
| [Sanders](https://www.sanders-uk.com/) (Rushden, "Made in England since 1873") | blocco "Fifth Generation Family Business" con la foto di famiglia; fondo pagina con ragione sociale e numero di registro | "dopo tre generazioni, i fratelli Giacometti" con una foto vera dei titolari [foto DA CONFERMARE] | blu notte, menu in graziato neretto; usa Spectral con Karla: la coppia intera non si riprende |
| [Viberg](https://viberg.com/) ("Canadian Bootmaker since 1931") | una frase sola, centrata, tra due foto grandi ("Each pair is made to withstand the elements...") | il ritmo foto e frase per la pagina Azienda | vive di foto a tutto schermo, che Walles non ha; a 1440 scorre di lato di 1 px |

### 2.3 Aperti e scartati

- [Saint Crispin's](https://saintcrispins.com/): scarpe in cassette di legno, belle, ma interfaccia generica e finestra newsletter.
- [Stefano Bemer](https://stefanobemer.com/): fondo crema e titolo enorme a forte contrasto: è il cliché bocciato.
- [Enzo Bonafè](https://www.enzobonafe.com/) (Norvegese, Bologna): sito senza viewport, da telefono largo 980 px come Walles.
- [Meindl](https://meindl.de/): scarponi da montagna, ma Roboto Slab ovunque e pagina che scorre di lato.
- [Church's](https://www.church-footwear.com/) e [Carmina](https://www.carminashoemaker.com/): pagina bianca o errore nel nostro browser; [John Lobb](https://www.johnlobb.com/) risponde 403 alla richiesta automatica.
- Edward Green e Valextra sono già i riferimenti di Benvegnù: non ripresi apposta, perché Walles deve avere un'altra faccia.

## 3. Cosa si riprende

| Gesto | Da | Dove nel sito di Walles | Con quale materiale vero | Condizione |
|---|---|---|---|---|
| Scheda su campo uniforme: foto, sotto marchio, codice e versione | Ludwig Reiter, Heschung | Collezioni (tre marchi), striscia prodotti in Home | 30 foto 800x600 su salvia #93B1AF; codici FG105, FG231, 01405 e "Versione 1" letti dal cartellino nelle foto | mai oltre 400 px CSS sui telefoni e schermi retina, 800 sugli altri; il cartellino stampato nella foto va tolto (ritaglio a 640x600 quando la scarpa lo permette) oppure servono gli originali senza scritta; pelle, colore e suola per modello [DA CONFERMARE] |
| Nome grande del marchio o del modello in graziato leggero e una riga sotto con la lavorazione | Paraboot | apertura di ogni marchio: "Marmolada / Norvegese a mano, colorazione a mano"; "Fratelli Giacometti / Goodyear a mano"; "Walles Club / pellami pregiati ed esotici" | testi delle tre pagine marchio | solo le lavorazioni scritte sul sito per quel marchio |
| Le costruzioni nominate in neretto dentro un testo breve, accanto a foto vere del reparto | Paraboot (Nos ateliers), Heschung (savoir-faire) | Home, fascia "Come sono fatte" | frasi del sito: "due cuciture", "fatta esclusivamente a mano", "in un unico passaggio mediante una cucitura" | foto delle lavorazioni a 536 px al massimo |
| Cinque capitoli alterni, uno per lavorazione, con indice in alto | Crockett & Jones (In the Making), indice a tessere di J.M. Weston | pagina Lavorazioni: Goodyear, Norvegese, Mocassino tubolare, Blake, Finiture | testi attuali (corretti, senza le parole dell'elenco) e 15 foto (tre per lavorazione) | niente numeri di fase: sono costruzioni alternative, non passaggi in sequenza; niente corsivo |
| Lessico: indice delle parole e una definizione per riga, tra filetti | Paraboot (Le lexique) | in fondo a Lavorazioni | solo parole che il sito già spiega: guardolo ("una striscia di cuoio morbido"), increna, sottopiede, intersuola, specchio e piegoline (tubolare), profilo a treccia (Norvegese), spruzzato, scurito, sfumato | ogni definizione presa dai testi Walles; le altre [DA CONFERMARE] |
| Pannello fabbrica: metà fondo scuro con titolo e quattro righe, metà foto | Tricker's | Home e Azienda: "Rossano Veneto, dal 1959" | "Dal 1959...", "dopo tre generazioni, i fratelli Giacometti", foto dello stabilimento 802x534 o una foto di reparto | foto mai oltre la sua misura; una sola fascia scura per pagina |
| Il nome della finitura dentro il nome del prodotto | Tricker's, Barrett | schede Marmolada e Finiture | "spruzzato, scurito, sfumato", "vintage" dal testo Finiture | quale finitura ha ogni modello [DA CONFERMARE] |
| Lo spaccio di fabbrica come un negozio: chi, dove, quando, mappa, foto | Cheaney (Factory Outlet), Ludwig Reiter (Fabriksverkauf) | pagina Outlet; blocco in Home; orari nel fondo pagina come Ludwig Reiter | Via Ramon 70/D, orari, telefono +39 0424 235890, outlet@walles.it, il cellulare di Ivana pubblicato sul sito attuale (se ripubblicarlo [DA CONFERMARE]) | foto dell'outlet da fare (brief nel LEGGIMI); servizi in negozio e assortimento [DA CONFERMARE] |
| Tre porte in fondo alla Home | Paraboot (Informazioni), Ludwig Reiter (quattro porte) | Azienda, Lavorazioni, Outlet | foto stabilimento, una foto di lavorazione, foto outlet quando c'è | niente foto d'archivio finché il cliente non le fornisce |
| Marchio con numero di modelli | J.M. Weston | Collezioni | | solo con numeri confermati [DA CONFERMARE] |
| Prodotto fotografato sul banco, tra fili e forme | Heschung (Crocus), Moreschi (forme di legno) | brief delle foto nuove nel LEGGIMI | | non con foto d'archivio altrui né stock |

Non importato: video d'apertura, caroselli automatici, recensioni, loghi di clienti, newsletter in finestra, icone di servizio in fila, etichette "NEW", corsivo calligrafico, crema, sezioni in dissolvenza.

## 4. Accoppiate

Campione con testi e foto veri di Walles: `_prova/ricerca/campioni/accoppiate-1440.png` e `accoppiate-390.png`. Le foto prodotto vi sono mostrate intere a 400x300 px, metà della loro misura. Contrasti calcolati con la formula WCAG.

Il campione ha mostrato una cosa da sapere per tutte e tre: le foto hanno i bordi laterali e gli angoli esattamente #93B1AF, ma il bordo alto, al centro, è più chiaro (#B4C8C7). Su una fascia salvia piena si vede quindi una riga chiara in alto. Si risolve facendo partire la fascia salvia esattamente dal bordo alto delle foto, oppure con le foto come schede staccate su un altro fondo (B e C).

### A. "Campo salvia": Spectral + Sofia Sans (consigliata)

- **Caratteri:** Spectral 300 (graziato dritto, mai corsivo) per titoli, nomi dei marchi e dei modelli: 48-60 px a desktop, 34-40 px da telefono. Sofia Sans 400 per il testo (17-18 px), 500 per menu e link. Sofia Sans Condensed 600 maiuscolo, 13 px, spaziatura 0,08-0,1 em, solo per etichette brevi: lavorazione, codice modello, giorni dell'outlet.
- **Palette:** bianco #FFFFFF; salvia #93B1AF, il fondo delle foto e del sito attuale, per la fascia dei prodotti; salvia chiara #E3EBEA per fasce di servizio (lessico, outlet); verde notte #1B2A28 per testo, testata e fondo pagina; grigio verde #4A5856 per il testo secondario. Nessun altro colore: il cuoio delle scarpe fa il resto.

| Testo | Fondo | Contrasto |
|---|---|---|
| verde notte #1B2A28 | bianco | 14,9:1 |
| verde notte #1B2A28 | salvia #93B1AF | 6,5:1 |
| verde notte #1B2A28 | salvia chiara #E3EBEA | 12,3:1 |
| grigio verde #4A5856 | bianco | 7,4:1 |
| grigio verde #4A5856 | salvia chiara #E3EBEA | 6,1:1 |
| bianco | verde notte #1B2A28 | 14,9:1 |
| salvia #93B1AF | verde notte #1B2A28 | 6,5:1 |
| grigio verde #4A5856 | salvia #93B1AF | 3,2:1: solo testi di almeno 24 px, meglio evitarlo |
| bianco | salvia #93B1AF | 2,3:1: vietato |

- **Da dove viene:** Paraboot (graziato leggero per i nomi dei modelli e un bastone neutro per il resto, verde scuro #153E35 e #0A2C2B, la stessa famiglia di verdi del salvia di Walles); J.M. Weston (titoli leggeri, Maison Neue per il testo); Sanders, calzaturificio inglese, usa proprio Spectral per i titoli. Sofia Sans è un bastone neutro come Maison Neue (Paraboot, Weston, Viberg) e ha una versione stretta per le etichette, come le etichette maiuscole di Ludwig Reiter. Il salvia non è una scelta di gusto: è il colore in cui sono state scattate tutte le foto di Walles.
- **Perché per Walles:** è il registro della scarpa classica da uomo che usano i calzaturifici con marchio proprio; tiene insieme lo scarpone Marmolada e il mocassino Walles Club; continua l'identità che il sito attuale ha già (fondo salvia, testata scura) e la rende leggibile. Nessun concorrente usa questi caratteri.
- **Rischio:** Spectral leggero sotto i 28 px si assottiglia: sotto quella misura si usa Sofia Sans. Il salvia pieno su intere pagine stanca: solo dove ci sono le scarpe.

### B. "Officina": Jost, una famiglia

- **Caratteri:** Jost 500 maiuscolo, spaziatura 0,06-0,16 em, per titoli, nomi dei marchi, menu e link; Jost 400 per il testo (17-18 px). Jost riprende il Futura.
- **Palette:** bianco; pietra #E4E3DF (il grigio delle schede di Ludwig Reiter) per le fasce dei prodotti; nero #121212 (la testata del sito attuale e lo stemma Walles Club); grigio #4F4C47 per il testo secondario; cuoio #7B4614, preso dalla tomaia colorata a mano del modello FG231, solo per codici, sottolineature e voce attiva. Il salvia resta dentro le foto.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero #121212 | bianco | 18,7:1 |
| nero #121212 | pietra #E4E3DF | 14,6:1 |
| grigio #4F4C47 | bianco | 8,5:1 |
| grigio #4F4C47 | pietra #E4E3DF | 6,7:1 |
| cuoio #7B4614 | bianco | 7,7:1 |
| cuoio #7B4614 | pietra #E4E3DF | 6,0:1 |
| bianco | nero #121212 | 18,7:1 |
| bianco | cuoio #7B4614 | 7,7:1 |
| nero #121212 | salvia #93B1AF | 8,2:1 |

- **Da dove viene:** le scritte dei marchi di Walles stesse: "MARMOLADA" e il "MADE IN ITALY" sotto Fratelli Giacometti sono maiuscole geometriche di tipo Futura. Poi i titoli maiuscoli larghi di Tricker's (Sweet Sans), le etichette spaziate di Ludwig Reiter e di Crockett & Jones (Proxima Nova).
- **Perché per Walles:** il sito parla con le stesse lettere dei suoi marchi; le schede su pietra fanno risaltare il salvia delle foto come tessere.
- **Rischio:** nero, bianco e un solo colore caldo è lo schema di Benvegnù (nero, bianco, rosso cuoio): la faccia rischia di somigliare. Il maiuscolo spaziato su titoli lunghi pesa ("GOODYEAR, NORVEGESE, BLAKE, MOCASSINO TUBOLARE" va su quattro righe a 1440): solo titoli brevi.

### C. "Fondo scuro": Sofia Sans e Sofia Sans Condensed

- **Caratteri:** Sofia Sans 300 per i titoli grandi (56-60 px a desktop), 400 per il testo, 500 per i nomi dei marchi; Sofia Sans Condensed 600 maiuscolo per le etichette. Nessun graziato.
- **Palette:** verde Marmolada #10211F per testata, apertura e fascia dei prodotti; salvia #93B1AF per etichette su fondo scuro; salvia chiara #C9D6D4 per il testo su scuro; pietra #ECE8E5 (il grigio delle schede di Heschung) per le fasce chiare; ardesia #2E3138 (vicino al #31323E di Ludwig Reiter) per il testo su chiaro.

| Testo | Fondo | Contrasto |
|---|---|---|
| bianco | verde Marmolada #10211F | 16,7:1 |
| salvia chiara #C9D6D4 | verde Marmolada #10211F | 11,2:1 |
| salvia #93B1AF | verde Marmolada #10211F | 7,3:1 |
| ardesia #2E3138 | pietra #ECE8E5 | 10,7:1 |
| ardesia #2E3138 | bianco | 13,0:1 |
| verde Marmolada #10211F | salvia #93B1AF | 7,3:1 |
| bianco | ardesia #2E3138 | 13,0:1 |

- **Da dove viene:** il fondo pagina verde scuro di Paraboot (#0A2C2B) e la fascia d'archivio su verde; il pannello blu notte di Tricker's (#101E2B); il bastone unico di Heschung e Viberg.
- **Perché per Walles:** nel campione è la versione in cui le foto si vedono di più: le schede salvia sul verde scuro sembrano accese. Il verde viene dal salvia scurito, quindi dalla stessa famiglia delle foto.
- **Rischio:** più di una fascia scura per pagina appesantisce; senza graziato la scarpa classica perde un po' di registro; i titoli a 300 vanno tenuti sopra i 40 px.

### Raccomandazione

A, con un innesto di C: la base è bianca e salvia con Spectral e Sofia Sans; il verde notte della testata e del fondo pagina si allarga in una sola fascia scura per pagina, il pannello fabbrica "Rossano Veneto, dal 1959" di Tricker's, dove le foto salvia risaltano come in C. B resta l'alternativa se il cliente trova il graziato troppo formale, sapendo che è la più vicina a Benvegnù.
