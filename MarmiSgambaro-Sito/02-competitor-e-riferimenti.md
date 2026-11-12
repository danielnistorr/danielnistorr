# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. 6 concorrenti cercati e 5 aperti, 20 siti di riferimento aperti con Playwright (Chromium) a 1440 e a 390 px. Screenshot in `_prova/ricerca/` (`c*-` concorrenti, `r-*` riferimenti), schermate scorse una alla volta in `_prova/ricerca/giro/` per i siti con animazioni allo scorrimento, pezzi ritagliati in `_prova/ricerca/ritagli/` (numerati 00-25 e citati qui sotto). Caratteri e colori dei siti letti dal browser (stile calcolato e font caricati), non a occhio. Script in `_prova/script/` (`shot.mjs`, `giro.mjs`, `font.mjs`, `verifica-conc.mjs`, `ritagli.py`).

Limiti incontrati, da sapere prima di riaprire i siti:
- Gli elenchi di imprese (Cylex, Pagine Gialle, Virgilio) bloccano il browser automatico (403 o Cloudflare). I concorrenti vengono dalla ricerca web e sono stati verificati aprendo i loro siti.
- **Marmistile** (Castelfranco Veneto, via Valsugana 128), che Pagine Gialle mette nella stessa lista di Marmi Sgambaro per Castelfranco: il dominio `marmistile.it` non risolve. Non fotografato.
- **Acemar** (Bassano del Grappa, cave dell'altopiano di Asiago): la home resta bianca al browser automatico (`c6-acemar-1440.png`). Non usato.
- **Grassi Pietre**: la prima visita ha caricato la pagina con dei vuoti (animazioni allo scorrimento); alla seconda il sito ha chiesto una verifica anti robot. Si usa la prima cattura.
- **Budri** e **EeStairs** restano su una schermata bianca o nera anche dopo 14 secondi; **Kreoo** risponde 403; **Il Casone** e **Marmi Faraone** non rispondono; `henraux.com` rimanda a una pagina http che il proxy rifiuta (usato `henraux.it/it/index.asp`).

## Premessa: che cosa è Marmi Sgambaro e con che cosa lavoriamo

Dal sito attuale (`https://marmisgambaro.it`, pagine scaricate in `_prova/crawl/sito/`):
- laboratorio di San Martino di Lupari (PD), via Leonardo da Vinci 36. La pagina Chi siamo dice che l'azienda nasce nel 1948 dall'interesse di Andrea Sgambaro per la scultura e che oggi è gestita dalla seconda generazione;
- "fornitura e trasformazione di marmi, pietre, graniti ed agglomerati (quarzi/resina)": scale, pavimenti, piani cucina, top bagno, rivestimenti, davanzali, portali, con progettazione, rilievi, trasporto e posa; arte funeraria (loculi e monumenti a terreno); studio tecnico che disegna in PDF e DWG;
- sei lavorazioni elencate: sabbiatura, spazzolatura, levigatura, lucidatura, rullatura, bocciardatura; pietre sinterizzate Neolith e Lapitec (in home anche il logo Laminam);
- **75 realizzazioni pubblicate, ognuna col nome della pietra e della finitura nel titolo**: "Scala interna in marmo San Pietro lucido spessore 8 cm", "Fioraia in pietra di Prun scalpellata a mano", "Scala esterna in quarzite Gaia Dark Mix fiammata e spazzolata". Contate dagli indirizzi delle pagine: 21 sono scale, 34 dicono lo spessore, 12 il profilo del gradino ("toro tondo"), 18 dicono "lucido", 17 "anticato", 13 "levigato", 8 "a mano". Il filtro della pagina ha 10 categorie: Bagni, Caminetti, Cancelli e recinzioni, Davanzali soglie e decorazioni, Pavimenti e rivestimenti esterni, Pavimenti e rivestimenti interni, Piani cucina, Scale esterne, Scale interne, Soggetti funebri e lapidi.

Il materiale che c'è (`ritagli/00-sgambaro-materiale-proprio.jpg`, `ritagli/01-sgambaro-realizzazioni-oggi.jpg`):
- **foto delle realizzazioni a 1024 x 768 px** (alcune verticali 576 x 768), scattate con fotocamere compatte nel 2018: luce piatta, colori veri della pietra. Quindi **mai foto a tutta larghezza a 1440**: al massimo 1024 px CSS, meglio colonne da 500-700 px;
- **il logo**: rosso **#C4161C** e nero **#231F20**, misurati sul file `logo-web90-1-1.png` (il rosso è lo stesso della barra in alto del sito). Il corallo #FE4641 dei pulsanti è il colore del tema, non dell'azienda. Il logo contiene "70" e "1948-2018 settant'anni di garanzia di qualità": il 1948 si tiene, il resto è scaduto **[DA CONFERMARE col cliente: versione del marchio senza il 70]**.

L'identità del nuovo sito nasce da qui: **la pietra chiamata per nome, con la finitura e lo spessore**, come sul cartellino di un campione, e **la scala** come lavoro più presente. Non da una tavolozza scelta a tavolino.

## 1. Concorrenti

| # | Concorrente | Zona | Cosa fa meglio di Sgambaro | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|
| 1 | [Marmo Arredo](https://www.marmoarredo.com/it/) | Tombolo (PD), via Sant'Antonio 66, e Fontaniva: a pochi chilometri | sito curato e coerente: lastra intera come apertura, blocchi scuri con titolo serif (Poly) e testo Frutiger, foto vera del laboratorio con le macchine, notizie aggiornate al 2026, materiali ordinati per colore e venatura, pagine Garanzia, Manutenzione, Download | carosello a sei pallini in apertura, testo grigio spaziato difficile da leggere, frasi che vanno bene per chiunque, "Da oltre 40 anni", © 2021 nel piè di pagina; nessuna scala in evidenza: parla di top cucina e superfici tecnologiche | `c1-marmoarredo-*.png`, `ritagli/23` |
| 2 | [Zaupa Marmi](http://www.zaupamarmi.it/ita/index.php) | Galliera Veneta (PD), via Olivari 3: a pochi chilometri | stessa offerta (arredo, arte funeraria, scale, pavimenti, restauro); dice quale macchina ha comprato e quando ("nel 2015 ... Intermac Master 33 Plus") e che un titolare frequenta corsi di scultura; una "libreria" di campioni divisa in marmi, graniti, quarziti, ardesie; P.IVA e indirizzo nel piè di pagina | sito senza meta viewport: a 390 px si impagina a 980 px (misurato); impianto a tabelle, icona Google+ (servizio chiuso), un video YouTube incorporato in home | `c2-zaupa-*.png`, `ritagli/21` |
| 3 | [Marmi Cavalletto](https://www.marmicavalletto.com/) | Codevigo (PD) | indirizzo e orari nella barra in alto ("Lun-Ven 8:00-12:00 / 13:30-18:30 Sabato 8:00-12:00"); otto famiglie con foto, compresa la scala e l'arte funeraria; telefono a un tocco su mobile | testo SEO con parole in grassetto ("lavorazione marmi a Codevigo in provincia di Padova") giustificato; griglia sfalsata con foto di misure diverse; pulsanti tondi marroni con freccia; Syncopate maiuscolo largo | `c3-cavalletto-*.png`, `ritagli/20` |
| 4 | [Mingrelli Marmi](https://www.marmipadova.it/) | Padova, laboratorio a Ponte San Nicolò | telefono ed email in testata con un tasto ciascuno; tasto chiamata fisso su mobile | arte funeraria come prima immagine, "Da oltre 50 anni" con un bollino grafico, foto di catalogo (scala sospesa, cactus), email gmail, un'immagine rotta a 390 (`prlx-red-400x266.jpg`), tre schede a punta | `c4-mingrelli-*.png`, `ritagli/24` |
| 5 | [Linea Pavimenti](https://www.lineapavimenti.it/) | Bassano del Grappa (VI), posa di marmo e pietra | una scala elicoidale in marmo come foto d'apertura; foto professionali di lavori (barche, negozi, ville); "Lavoriamo con" con i loghi di Margraf, Marmo Arredo, Lapitec | tre riquadri con icona in fila, elenco con le spunte di frasi generiche, "Oltre 30 anni di esperienza"; a 390 al posto del logo compare l'icona di immagine mancante e dopo lo scorrimento la pagina si allarga a 1896 px (misurato) | `c5-lineapavimenti-*.png`, `ritagli/22` |
| 6 | Marmistile | Castelfranco Veneto (TV) | | dominio non raggiungibile (vedi sopra) | |

Il sito attuale di Marmi Sgambaro, per confronto (`c0-sgambaro-1440.png`, `c0-sgambaro-390.png`): impianto del tema Impreza del 2018 (Open Sans, corallo #FE4641), quattro cerchi con icona in fila (Consulenza, Realizzazione, Posa, Ripristino), contatori "+70 anni, +200 tipologie, +2000 clienti soddisfatti, +50 partner" non verificabili, sei foto senza didascalia in home. I titoli ricchi delle 75 realizzazioni stanno solo nella pagina Realizzazioni, in miniatura. I problemi tecnici (numero di telefono demo nel link, pagine demo pubbliche) sono in 01.

**Cosa fanno i migliori:** foto vere del laboratorio e delle macchine (Marmo Arredo, Zaupa); indirizzo, orari e telefono sempre visibili, anche su telefono (Cavalletto, Mingrelli); una scala in apertura (Linea Pavimenti); il campionario diviso per tipo di pietra (Zaupa); una data e un fatto al posto di un aggettivo (Zaupa: 2015, Intermac).

**Cosa non fa nessuno, ed è spazio per Marmi Sgambaro:**
1. **Dire il nome della pietra, la finitura e lo spessore su ogni lavoro.** Sgambaro lo fa già nei titoli (34 su 75 con lo spessore). Nessun concorrente vicino mette una didascalia così sotto le foto: Marmo Arredo nomina le collezioni, gli altri mostrano foto senza nome.
2. **La scala come specialità dichiarata.** 21 realizzazioni su 75 sono scale, con i profili nominati (toro tondo, alzata con gola, battiscopa a scivolo, fianchetto sagomato). Cavalletto ha una voce "Scale" con una riga di testo; nessuno ha una pagina che spieghi le scale per profilo, spessore e finitura.
3. **Le finiture mostrate.** Sgambaro elenca sei lavorazioni; nessuno dei vicini le fa vedere con un campione. **[DA CONFERMARE: si possono fotografare sei campioni in laboratorio]**.
4. **Freschezza.** Marmo Arredo © 2021, Zaupa senza versione mobile, Linea Pavimenti che si allarga su telefono, Mingrelli con una email gmail. Un sito aggiornato, con i link di contatto giusti e la P.IVA in fondo, basta già a stare davanti ai vicini.

**Posizionamento proposto per 03 (bozza):** "Scale, pavimenti, bagni e piani cucina in marmo e pietra, lavorati e posati dal laboratorio di San Martino di Lupari, dal 1948." Contro Marmo Arredo (vicino, più grande, superfici tecnologiche e design) Sgambaro è il laboratorio che fa la scala su misura e la posa; contro Zaupa (stessa offerta, stessi chilometri) ha 75 lavori documentati per nome; contro Linea Pavimenti (solo posa) lavora e posa la stessa pietra.

**Copy da non ripetere** (visto nei concorrenti): i contatori che invecchiano ("Da oltre 40 anni", "50 anni di esperienza", "Oltre 30 anni"): si scrive "dal 1948"; "punto di riferimento" (lo usano in quattro su cinque); elenchi con le spunte di qualità dichiarate; parole chiave in grassetto per i motori di ricerca; i contatori "+2000 clienti soddisfatti" del sito attuale. Le parole di `PAROLE_VIETATE` (build.py), che ricorrono in tutti e cinque i siti, restano fuori.

## 2. Riferimenti premium

Marmi Sgambaro è un laboratorio di otto persone che taglia, lavora e posa pietra su misura: scale, pavimenti, bagni, piani cucina, caminetti, arte funeraria. Il riferimento giusto non è una casa di moda né un marchio d'arredo, ma le aziende della pietra con siti di livello alto: cave e laboratori italiani (Henraux, Grassi Pietre, Salvatori), aziende europee che fanno lo stesso mestiere (Ca' Pietra), produttori di materiali per architettura (SolidNature, Dzek). Li ho aperti tutti il 6 ottobre 2026. I migliori hanno in comune: **la pietra chiamata per nome accanto alla foto**, foto vere e non ingrandite, un grottesco senza grazie per il testo, un solo colore d'accento usato poco, nessun ornamento.

| Riferimento | Che cosa è | Il gesto preciso da riprendere | Dove nel sito Sgambaro | Cosa evitare | Ritagli |
|---|---|---|---|---|---|
| [Grassi Pietre](https://www.grassipietre.it/) | Pietra di Vicenza dalle cave di Nanto (VI), "dal 1850" | **Il cartellino del campione**: un quadrato di pietra con sopra, in maiuscoletto nero, il nome e la finitura ("PERLA DEI BERICI" e "LEVIGATA", separati da una lineetta), uno per pietra, in colonna. **La mano al lavoro**: una mano con la lana d'acciaio sulla lastra, accanto alla parete dei campioni, due foto della stessa altezza | il cartellino di ogni realizzazione e la pagina Lavorazioni (un campione per ognuna delle sei finiture). Sgambaro lavora la Pietra di Vicenza: "colonne in Pietra di Vicenza levigata" in una realizzazione | video in apertura che resta grigio, colonne che scorrono a scatti e lasciano vuoti, la lineetta lunga nel nome (qui si usa "·") | 02, 03 |
| [Salvatori](https://www.salvatori.it/) | pietra naturale lavorata, Querceta (LU) | **"Samples"**: lastre campione fotografate dall'alto, appoggiate su un pavimento di marmo, con titolo e link sopra la foto. **Didascalia d'apertura** in basso a destra: nome del pezzo con freccia, una riga sotto, contatore "2 / 10" su un filetto sottile; resta uguale a 390. Titoli in Atlas Grotesk Light: grandi ma leggeri | striscia delle sei finiture (campione dall'alto e nome); contatore "1 / N" nelle gallerie delle realizzazioni | carrello e prezzi in dollari, apertura a carosello con arredo da catalogo, chat che copre il testo, frase centrata di presentazione | 04, 05 |
| [SolidNature](https://www.solidnature.com/) | pietre per progetti e oggetti, Paesi Bassi | **Didascalia dentro la foto**: nell'angolo basso a destra, categoria in maiuscolo, nome del progetto, contatore "1 / 11" in grigio. Sotto la foto: a sinistra titolo e due righe, a destra il link in maiuscolo sottolineato con un pallino pieno. La foto sta dentro i margini della pagina | scheda della realizzazione: "SCALA INTERNA  Marmo San Pietro lucido, spessore 8 cm  1 / 3" sulla foto, testo e "Tutte le scale" sotto | titoli giganti in maiuscolo serif sopra la foto, foto a 1216 px (quelle di Sgambaro sono 1024), oggetti da galleria d'arte | 06 |
| [Henraux](https://www.henraux.it/it/index.asp) | marmo di Carrara, cave e laboratorio, Querceta, "dal 1821"; Fondazione Henraux per la scultura | **L'anno sotto il nome**: "HenrauX" e, piccolo, "1821" allineato a destra sotto la X. **Tessera materiali**: una lastra intera in verticale, sotto un'etichetta piccola spaziata ("I NOSTRI MATERIALI") e un nome grande. **Notizie**: data in maiuscolo spaziato, filetto corto a sinistra del titolo | marchio "Marmi Sgambaro" con "1948" sotto; il legame con la scultura in Chi siamo (dal testo attuale); data e filetto nelle notizie, se ci saranno | corsivo nei titoli e nei testi (vietato), riquadro scuro semitrasparente sul titolo d'apertura, otto voci di menu in maiuscolo spaziato | 07, 08, 09 |
| [Ca' Pietra](https://capietra.com/) (Artisans of Devizes) | pietra, piastrelle, pavimentazioni esterne, lastre, scale e piani cucina su misura; Devizes, Inghilterra: l'offerta più vicina a Sgambaro tra i riferimenti | **Quattro famiglie su una fascia scura** (Stone, Tiles, Paving, Slabs): foto verticale, nome in capitali da iscrizione (Garda Nova), "BROWSE" piccolo sottolineato. **"ARTISANS SINCE 1989"** come titolo: l'anno al posto del contatore | indice dei lavori in Home: Scale, Pavimenti e rivestimenti, Bagni e piani cucina, Caminetti e davanzali; "dal 1948" al posto di "settant'anni" | fondo panna #F5F0EC (è il crema bocciato su Benvegnù), chat che si apre da sola, collezione floreale, carrello | 10, 11 |
| [Dzek](https://www.dzekdzekdzek.com/) | materiali per architettura: Marmoreal (marmo ricomposto, con Max Lamb), ExCinere (con Formafantasma) | **Il percorso sopra il testo**: una riga piccola in maiuscolo, "CASE STUDIES → MARMOREAL", poi il testo del progetto; resta identica a 390. **Il menu aperto come indice**: sei colonne con le voci sotto ogni titolo | riga sopra ogni scheda: "REALIZZAZIONI → SCALE INTERNE"; menu su telefono come indice a colonne delle 10 categorie | testo giustificato (a 390 fa buchi tra le parole), tutto in bianco e nero (per Sgambaro il colore della pietra è un'informazione) | 12, 13 |

Gesti utili presi da siti che nel complesso non sono riferimenti:
- [Margraf](https://www.margraf.it/) (marmi, Chiampo): **lastre fotografate intere con il nome sotto** (Verde Alpi, Rosso Cardinale) e **la macchina che scava il profilo di un gradino** nel blocco (`ritagli/15`, `16`). Per Sgambaro: le pietre sinterizzate (Neolith, Lapitec) come lastre col nome; una foto della lavorazione di un gradino **[foto da fare]**. Da evitare: carosello 3D, menu a pillola arancio, angoli arrotondati, grassetti nei paragrafi.
- [Pibamarmi](https://www.pibamarmi.it/) (marmo per arredo, Vicentino): **una foto di bottega in bianco e nero** (lastra alla pinza, operaio) con tre notizie in basso, ognuna aperta da un filetto e da una data; P.IVA nel piè di pagina (`ritagli/14`). Da evitare: una home di una sola schermata, menu ad hamburger anche su desktop.
- [Antolini](https://www.antolini.com/) (pietre, Verona): il **piazzale delle lastre visto dall'alto** come prima immagine: il luogo dove si lavora (`ritagli/17`). Per Sgambaro: il laboratorio di via Leonardo da Vinci **[foto da fare]**. Da evitare: testo sopra foto piene di dettagli, ® ovunque.
- [Lithos Design](https://www.lithosdesign.com/) (Chiampo, VI): **il luogo in piccolo sopra il titolo del progetto** e lo studio sotto (`ritagli/18`). Per Sgambaro: il comune della realizzazione **[DA CONFERMARE: se i clienti lo permettono]**.
- [Morseletto](https://morseletto.com/) (Vicenza): "da oltre cent'anni i sarti del marmo": il mestiere detto con una parola concreta (`ritagli/19`). Il sito è datato (menu laterale, carosello).

Aperti e scartati: Lapicida (etichette in un riquadro sotto le foto di categoria, ma apertura vuota e quasi solo piastrelle), Siller Stairs (video vuoti, nuvola di link per i motori di ricerca, sfondo sfumato), Citco (interni di lusso lontani da un laboratorio di otto persone), Stone Source (finestra della newsletter sopra la pagina), Budri, EeStairs, Kreoo, Il Casone, Marmi Faraone (non caricati, vedi sopra).

## 3. Cosa si riprende

| Sezione del nuovo sito | Gesto | Da chi | Con quale materiale di Sgambaro |
|---|---|---|---|
| Testata | nome con "1948" sotto, piccolo; telefono ed email in chiaro con i link giusti (`tel:+390499461675`, `mailto:info@marmisgambaro.it`); su telefono un tasto Chiama | Henraux; Mingrelli, Cavalletto | logo attuale (rosso #C4161C, nero #231F20), dati da 01; orari **[DA CONFERMARE]** |
| Apertura Home | una scala fotografata a dimensione nativa (1024 px), accanto al titolo, con il cartellino sotto; niente carosello | Grassi, SolidNature, Linea Pavimenti (la scala in apertura) | `CIMG0582.jpg`, "Scala interna in marmo San Pietro lucido spessore 8 cm" |
| Indice dei lavori | quattro tessere: foto, nome, numero di realizzazioni, link sottolineato | Ca' Pietra, Henraux | le 10 categorie del filtro attuale raggruppate in quattro; conteggi da 01 |
| Realizzazioni | cartellino "TIPO · PIETRA · FINITURA · SPESSORE" in maiuscoletto, prima parola in rosso; percorso sopra il titolo; galleria con contatore "1 / N" | Grassi, Dzek, SolidNature, Salvatori | i 75 titoli attuali, scritti come cartellino |
| Scale (pagina) | profili nominati (toro tondo, alzata con gola, battiscopa a scivolo) con la scala che li usa | Margraf (profilo del gradino), Grassi | le 21 scale pubblicate e i loro titoli |
| Lavorazioni | sei campioni quadrati fotografati dall'alto, nome sotto | Salvatori ("Samples"), Grassi | elenco delle sei lavorazioni; **foto dei campioni da fare** |
| Pietre sinterizzate | lastra intera con il nome sotto, testo breve | Margraf | testi attuali su Neolith e Lapitec, loghi in scala di grigi |
| Chi siamo | "dal 1948" come titolo; una foto di bottega; studio tecnico che disegna in PDF e DWG | Ca' Pietra, Henraux, Pibamarmi, Grassi (la mano) | testo di Chi siamo; **foto del laboratorio da fare** |
| Piè di pagina | indirizzo, telefono, PEC, P.IVA | Pibamarmi, Henraux, Zaupa | Marmi Sgambaro S.r.l., P.IVA 04564690289, PEC da 01 |

Scartato per tutti: caroselli automatici, cerchi o riquadri con icona in fila (oggi in home), contatori non verificabili, foto stock, chat che si aprono da sole, corsivo, fondo crema, foto mostrate oltre la loro risoluzione.

## 4. Accoppiate

Che cosa usano davvero i siti visti (letto dal browser): Salvatori Atlas Grotesk (Light per i titoli); SolidNature Monument Grotesk per i testi e Mediaan, un serif, in maiuscolo per i titoli grandi; Ca' Pietra Garda Nova (capitali da iscrizione, con le grazie appena accennate) e Caslon Doric; Henraux un marchio serif con Gotham e Maison Neue; Pibamarmi Neue Haas Grotesk e Space Mono; Margraf Gantari; Dzek un grottesco proprio. **Il settore usa quasi solo grotteschi; il serif compare solo come capitale da iscrizione** (Ca' Pietra, SolidNature, il marchio Henraux), cioè la lettera incisa nella pietra: per un'azienda nata dalla scultura e che fa arte funeraria è un'origine vera, non un'abitudine. I concorrenti usano Open Sans (Sgambaro oggi), Poly e Frutiger (Marmo Arredo), Syncopate e Source Sans (Cavalletto), Montserrat (Mingrelli), Chapaza e Titillium (Linea Pavimenti): le accoppiate qui sotto non ne ripetono nessuno, né ripetono quelle degli altri siti di questo repository.

Prova di tutte e tre con testi e foto di Sgambaro: `_prova/ricerca/accoppiate-prova.png` (`ritagli/25`). Rapporti di contrasto calcolati con la formula WCAG 2.1. Il rosso del logo #C4161C su bianco fa 6,04:1, quindi **si può usare per il testo su fondo chiaro**; su nero fa 2,7:1, quindi **su fondo scuro mai come testo**, solo come fondo di un pulsante con testo bianco.

### A. "Cartellino": Host Grotesk, una famiglia (consigliata)

Da Salvatori (titoli grandi in un grottesco leggero, campioni come navigazione), SolidNature (didascalia dentro la foto con il contatore), Grassi (nome della pietra e finitura sul campione) e Dzek (la riga del percorso sopra il testo). È la più vicina a quello che Sgambaro ha già: 75 lavori che si chiamano come un cartellino.

- **Host Grotesk** (Google Fonts): 300 per i titoli (52-60 px su desktop, 34-38 su telefono), come l'Atlas Grotesk Light di Salvatori; 400 per testo e menu (17-18 px); 600 maiuscolo spaziato 0,08 em, 12-13 px, per cartellini, etichette e link. Nessun secondo carattere: il cartellino si distingue per maiuscolo e peso, come fa Grassi.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | Bianco #FFFFFF | |
| Fascia di servizio (lavorazioni, contatti) | Pietra chiara #EEEEEC (grigio neutro, non crema) | |
| Testo, titoli, filetti | Nero Sgambaro #231F20 (dal logo) | 16,3:1 su bianco; 14,03:1 su #EEEEEC |
| Testo secondario | Grigio #5E5A57 | 6,83:1 su bianco; 5,88:1 su #EEEEEC |
| Prima parola del cartellino, voce di menu attiva, link | Rosso Sgambaro #C4161C (dal logo) | 6,04:1 su bianco; 5,2:1 su #EEEEEC |
| Pulsante pieno | #C4161C con testo bianco | 6,04:1 |
| Fascia scura (una sola, vedi scelta) | #231F20 con testo bianco e secondario #C9C6C2 | 16,3:1 e 9,58:1 |

Hover: il pulsante rosso diventa nero #231F20 pieno; il link rosso diventa nero. Mai opacità.

### B. "Lapide": Marcellus + Schibsted Grotesk

Da Ca' Pietra (capitali da iscrizione per i nomi delle famiglie e per "Artisans since 1989"), Henraux (marchio serif con l'anno sotto) e SolidNature (serif maiuscolo per i titoli), e dalla storia di Sgambaro: la scultura del 1948 e l'arte funeraria, dove la lettera si incide nel marmo. È la più riconoscibile, ma la più rischiosa.

- **Marcellus** (Google Fonts, un solo peso): titoli brevi in maiuscolo, spaziatura 0,04 em, 48-54 px; nome del marchio. Mai corsivo, mai per frasi lunghe.
- **Schibsted Grotesk** (Google Fonts) 400 e 600: testo, menu, cartellini, pulsanti. È un grottesco di stampa vicino al Caslon Doric di Ca' Pietra.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo | Bianco #FFFFFF | |
| Fascia chiara | Pietra #E7E6E3 | |
| Testo e titoli | Nero #1E1D1C | 16,83:1 su bianco; 13,49:1 su #E7E6E3 |
| Testo secondario | Grigio #64605C | 6,23:1 su bianco; 4,99:1 su #E7E6E3 |
| Cartellino su fascia scura | #E7E6E3 su #1E1D1C, secondario #A8A39E | 13,49:1 e 6,73:1 |
| Link, voce attiva | Rosso #C4161C | 6,04:1 su bianco; 4,84:1 su #E7E6E3 |

Rischio: le capitali incise ripetute in ogni titolo fanno pensare a una lapide o a una spa. Solo titoli di poche parole, nessun fondo crema, nessun oro.

### C. "Bottega": Gantari + Space Mono

Da Margraf (Gantari, lastre su fondo nero, la macchina che scava il gradino) e Pibamarmi (Neue Haas Grotesk con Space Mono, foto di bottega in bianco e nero). È la più dura: pagine scure, le lastre come unica luce.

- **Gantari** (Google Fonts) 300 per i titoli, 400 e 500 per testo e menu; **Space Mono** 400, 12 px maiuscolo, per cartellini e codici ("SCALA INTERNA / SAN PIETRO LUCIDO / SP. 8 CM"). Mai mono per i paragrafi.

| Ruolo | Colore | Contrasto |
|---|---|---|
| Fondo delle fasce scure | #161616 | |
| Testo su scuro | #F2F2F0 | 16,14:1 |
| Testo secondario e cartellini su scuro | #A9A9A6 (#C9C6C2 per i paragrafi) | 7,68:1 (10,63:1) |
| Pulsante | #C4161C con testo bianco | 6,04:1 (il rosso su #161616 fa 3,0:1: mai come testo) |
| Pagine chiare | Bianco con testo #231F20 | 16,3:1 |

Rischio: le foto attuali (compatte, 1024 px, luce piatta) su nero mostrano di più i loro limiti; funziona solo con il servizio fotografico del laboratorio. Gantari è il carattere di Margraf, che Linea Pavimenti cita tra i fornitori: il sito somiglierebbe a quello di un fornitore.

### Scelta consigliata per la fase 2.3

**A**, con un innesto dalla **C**: una sola fascia scura #231F20 "Il laboratorio", con testo bianco e, quando ci saranno, foto di bottega in bianco e nero (lastra, macchina, mano), sul modello di Pibamarmi e della mano di Grassi. Dalla **B** si tiene solo l'idea dell'anno nel marchio ("1948" sotto il nome, come Henraux), non il carattere. Foto: realizzazioni a colori, mai oltre i 1024 px nativi, ognuna con il suo cartellino; nessun viraggio. Nel LEGGIMI va il brief delle foto da fare: sei campioni delle finiture fotografati dall'alto con luce radente, il laboratorio di via Leonardo da Vinci, una lastra in lavorazione, il dettaglio di un gradino con toro tondo, due o tre scale recenti con luce naturale.
