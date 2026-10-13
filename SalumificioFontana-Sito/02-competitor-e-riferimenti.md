# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Ogni sito è stato aperto dal vivo con Playwright (Chromium) a 1440 px e a 390 px con user agent iPhone. In `_prova/ricerca/` ci sono, per ogni sito, la pagina intera (`<nome>-1440.png`, `<nome>-390.png`, tagliate a 12.000 px), la prima schermata (`<nome>-<larghezza>-schermo.png`) e un `.json` con caratteri, corpi e colori calcolati dal browser. I pezzi da riprendere sono ritagliati in `_prova/ricerca/ritagli/` (20 file). Script: `_prova/script/ricerca.mjs` (screenshot) e `_prova/script/ritagli.py` (ritagli).

Visitati: 7 concorrenti, il sito attuale di Fontana e il sito del Consorzio; 31 siti candidati come riferimento. Non usati perché bloccati o vuoti nella cattura automatica: Antica Macelleria Falorni, Cobble Lane Cured, Brandt & Levie, Acetaia Giusti (verifica Cloudflare); Antica Corte Pallavicina, Prolongo, Coati (apertura video o slider che resta vuota).

## 1. Concorrenti

L'elenco viene dalla pagina Produttori del Consorzio ([prosciuttoveneto.it/produttori](https://www.prosciuttoveneto.it/produttori/), letta il 6 ottobre 2026). Ci sono 9 aziende: 4 a Montagnana (Attilio Fontana Prosciutti, Daniolo Desiderio, Prosciuttificio Soranzo, Salumificio Brianza), King's a Sossano, Crosare a Pressana, Ducale a Barbarano Mossano, San Marco a Meledo di Sarego e, unica a Este, il Salumificio Giovanni Fontana. Daniolo non ha sito (solo un indirizzo email), Soranzo risponde con una pagina vuota (codice 202, 167 byte). Bertelli Salumi non è nell'elenco del Consorzio ma è un salumificio di Montagnana con una gamma simile.

| # | Concorrente | Zona | Sito (misurato) | Cosa fa meglio di Fontana | Cosa fa peggio |
|---|---|---|---|---|---|
| 1 | [Attilio Fontana Prosciutti](https://www.fontanaprosciutti.it/) | Montagnana (PD), via Campana 8 | WordPress (tema Avada), https e viewport corretti, a 390 nessuno scorrimento orizzontale | "Prosciuttai dal 1919" come titolo; confronto ieri e oggi della stessa strada con un cursore; foto della famiglia tra i prosciutti appesi; pagina "Per Natale" | l'apertura è un video YouTube di sfondo: nella cattura, a 1440 e a 390, resta una fascia bianca di circa 600 px; Arial ovunque; ultima notizia del 1 aprile 2023; fa solo prosciutto |
| 2 | [Salumi King's](https://www.salumikings.it/) | Sossano (VI) | WordPress, https e viewport corretti | prodotti interi e tagliati fotografati sullo stesso set (Parma, Rebello); categorie sfogliabili (Arrosti e altre); ricette; link "Regolamenti e downloads" nel piede | apertura con video scuro; fregi ornamentali, scudi e curve su fondo quasi nero; titoli fatti di aggettivi generici; ultima notizia del 30 settembre 2025 |
| 3 | [Salumificio Brianza](http://www.salumificiobrianza.it/) | Montagnana (PD), via Luppia San Zeno 35 | WordPress 4.9.26 (dal meta generator), Playfair Display + Open Sans | catalogo con una foto per prodotto e la famiglia sotto il nome (Lardo, Prosciutto Crudo Veneto DOP, Speck, Fiocco, Arista, Bresaola); shop e idee regalo; foto della famiglia; un blocco dedicato al DOP | apre con una bistecca cruda su marmo nero, che non dice né Montagnana né salumificio; WordPress di una versione vecchia; testi pieni di aggettivi |
| 4 | [Prosciuttificio Crosare](https://www.prosciuttificiocrosare.it/) | Crosare di Pressana (VR) | WordPress (Astra), shop | tre famiglie con foto grandi subito sotto l'apertura (Prosciutti, Speck, Specialità); blocco "Il Marchio" con la foto del marchio DOP impresso sulla cotenna e due righe di spiegazione; "Fai un tour" con video; "Schede tecniche" nel piede | tre caratteri diversi (Abril Fatface, Arbutus Slab, Roboto); i contatori "CO2 risparmiata" e "Alberi salvati" restano a 0 nella cattura; banner cookie e iscrizione con sconto sopra i contenuti |
| 5 | [Prosciuttificio Ducale](https://www.prosciuttificioducale.it/) | Barbarano Mossano (VI) | WordPress, Revolution Slider 5.4.8 | racconta il Prosciutto Veneto con una fonte storica (Michele Savonarola, 1400) | a 390 la home mostra in chiaro "Revolution Slider Error: You have some jquery.js library include..."; nel codice della home c'è ancora il testo segnaposto "Lorem ipsum dolor amet"; a 1440 immagine rotta accanto a "Il Brand"; fondo a carta stropicciata |
| 6 | [Bertelli Salumi](https://www.bertellisalumi.it/) | Montagnana (PD) | Wix; a 390 il sito mobile è largo 320 px | foto d'archivio vera del laboratorio (le persone al tavolo di lavoro, la bilancia); le mura di Montagnana nel logo come segno del luogo | titoli in corsivo calligrafico (Dancing Script); fondo giallo a texture; riquadro nero vuoto di circa 650 px al posto del video nella cattura a 1440 |
| 7 | [Prosciuttificio San Marco](http://prosciuttificiosanmarco.it/) | Meledo di Sarego (VI) | WordPress 5.0.29; in https il server risponde con un errore TLS ("unrecognized name") | nulla di specifico | foto dello stabilimento montata in mezzo a un vigneto; blocchi con icona in cerchio; https che non funziona, come quello di Fontana |

**Fontana nella stessa prova** (`c0-fontana-attuale`): a 390 la pagina è larga 980 px (manca il meta viewport), nessun titolo (h1, h2, h3) nel codice, 8 immagini in tutta la home, caratteri Nobile e Maven Pro. Tutti e sette i concorrenti hanno il viewport e si leggono da telefono.

**Cosa fanno i migliori:** famiglie di prodotto come prima navigazione, con foto (Crosare, Brianza, King's); una scheda per prodotto con il nome della denominazione (Brianza); persone vere e foto d'archivio (Attilio Fontana, Bertelli); il marchio DOP spiegato con la foto della cotenna (Crosare); documenti per chi compra (Crosare "Schede tecniche", King's "Regolamenti e downloads").

**Cosa non fa bene nessuno (spazio per Fontana):**
1. La gamma intera per chi compra all'ingrosso. Tra i siti visti nessuno mostra la gamma per famiglie insieme ai formati di vendita (intero, disossato, mezzo, sottovuoto). Fontana ha già i nomi e 45 schede con foto scontornata: 15 stagionati, 4 freschi, 16 cotti, 10 affumicati (i 44 file scaricati sono tutti PNG trasparenti 450x450). Attenzione: l'elenco della pagina Prodotti e le pagine di famiglia non coincidono (Freschi: 10 nomi nell'elenco, 4 schede con foto). I conteggi definitivi si prendono da 01.
2. Este. È l'unico produttore DOP di Este nell'elenco del Consorzio e ha il castello nel marchio; gli altri parlano di Montagnana o dei Berici.
3. Una storia con date vere. Nelle home dei concorrenti c'è al massimo un anno di fondazione (Attilio Fontana 1919, King's 1907) o un "da oltre quarant'anni" (Crosare); Fontana ha una sequenza di fatti datati: 1919 Montagnana, 1941 Este e la barchessa, la requisizione, 1945, 1951 Lea Vezzù.
4. La cura. Notizie ferme al 2023 e al 2025, testo segnaposto pubblicato, contatori a zero, un errore di slider in chiaro. Il nuovo sito non avrà una sezione notizie se nessuno la aggiorna.

**Attenzione al nome.** Attilio Fontana Prosciutti (Montagnana, "dal 1919") e il Salumificio Giovanni Fontana (Este) hanno la stessa origine: la pagina Storia di Fontana dice che nel 1919 i fratelli Giovanni e Attilio Fontana fondano a Montagnana la prima attività e che Giovanni avvia la produzione a Este nel 1941. In più salumificiofontana.com è un altro salumificio, in Calabria. Il nuovo sito deve dire subito "Salumificio Giovanni Fontana, Este".

**Posizionamento proposto:** "Prosciutto Veneto Berico-Euganeo DOP e salumi stagionati, freschi, cotti e affumicati. Carne suina e bovina, fresca e congelata, in quarti o sottovuoto. A Este dal 1941." Tutto dal sito attuale. Contro Attilio Fontana (stessa origine, solo prosciutto, Montagnana) Fontana è la gamma intera; contro Brianza (gamma simile, Montagnana, shop per privati) è Este, la storia documentata e il banco per i professionisti [DA CONFERMARE: a chi vende oggi l'azienda e se vende anche ai privati].

**Copy evitato** (visto nei concorrenti): gli aggettivi dell'elenco `PAROLE_VIETATE` di `build.py`, che King's, Brianza e San Marco usano nei titoli; "il segreto", "l'arte del gusto", "la tavola di un Re", "capolavoro"; frasi tra virgolette attribuite a scrittori o clienti; contatori animati.

## 2. Riferimenti premium

Fontana è un salumificio di famiglia con un prosciutto DOP e una gamma larga, venduta al banco di macellerie, salumerie e ristoranti [DA CONFERMARE i canali]. I riferimenti giusti sono le case del prosciutto e dei salumi con siti di livello alto e una charcuterie con un catalogo fatto bene, non case di moda né siti di lusso generico. Hanno in comune: prodotti veri fotografati su un fondo coerente, interfaccia piccola, il colore preso dall'etichetta del prodotto, l'archivio usato come prova.

### 2.1 Joselito, prosciutto iberico, dal 1868 ([joselito.com](https://joselito.com/))
Cosa fa: apertura a tutta pagina con "DESDE 1868" piccolo e titolo bianco; sotto, filetti grigi sottili separano le sezioni. "Nuestra selección": tre prodotti fotografati in verticale su fondi pieni scuri o bordeaux, nome e prezzo sotto in piccolo; a 390 diventa una striscia che scorre con la scheda successiva che sporge. "Añadas especiales": un prosciutto appeso a una corda davanti a un muro, il nome della linea fuori scala, quattro caratteristiche in riquadri sottili. "Nuestros productos": categorie con il conteggio ("5 productos", "7 productos"). Link in maiuscolo piccolo sottolineati al posto dei pulsanti. Caratteri: SangBleu Kingdom (serif, sempre tondo) e Euclid Circular B.
**Gesto da riprendere:** il prodotto come ritratto (un solo pezzo, verticale, isolato su un fondo pieno) e le famiglie con il conteggio dei prodotti; filetti sottili e link sottolineati.
**Da evitare:** il tramonto in apertura, la parola che scorre in orizzontale, carrello e prezzi, il registro da lusso.
Ritagli: `joselito-prodotti-come-ritratti.jpg`, `joselito-parola-fuori-scala.jpg`, `joselito-categorie-con-conteggio.jpg`.

### 2.2 Pio Tosini, Prosciutto di Parma, Langhirano dal 1905 ([piotosini.it](https://piotosini.it/it/))
Cosa fa: il verde dell'etichetta diventa un campo pieno con logo e titolo; la cantina a tutta larghezza; "Una storia di oltre 120 anni" con il testo a sinistra e, a destra, una foto d'archivio della vecchia cantina con l'insegna "F. TOSINI"; "Le nostre selezioni" con tre prosciutti scontornati e la denominazione completa in maiuscolo sotto ("Prosciutto di Parma Tre Ghiande disossato pressato"); piede verde. Caratteri: ITC Benguiat Condensed (titoli), DIN Condensed (testo), Manrope.
**Gesto da riprendere:** il colore dell'etichetta del prodotto come colore del sito; la foto d'archivio accanto al racconto con le date; il prodotto scontornato con la denominazione completa.
**Da evitare:** la texture di carta, le foglie disegnate dietro le schede, la frase-citazione, la prima schermata a 390 che resta bianca con una linea finché non parte l'animazione.
Ritagli: `piotosini-colore-dell-etichetta.jpg`, `piotosini-storia-e-foto-d-archivio.jpg`, `piotosini-selezioni-scontornate.jpg`.

### 2.3 Villani, salumi dal 1886 ([villanisalumi.it](https://www.villanisalumi.it/))
È il riferimento con la gamma più vicina a Fontana (cotti, mortadelle, crudi, salami). Cosa fa: "Le specialità" mostra un prodotto alla volta, scontornato, con il nome commerciale sopra ("La Santo"), la denominazione sotto ("Mortadella Bologna IGP") e una riga di descrizione; frecce tonde per passare al successivo. "Tutti i prodotti": le famiglie come prima navigazione. "Maestri e mestieri": foto in bianco e nero di mani al lavoro, con un blocco di colore sfalsato dietro la foto. Caratteri: Lusitana e Lato.
**Gesto da riprendere:** la scheda in tre livelli (nome, denominazione, una riga) e le foto di lavoro in bianco e nero accanto ai prodotti a colori.
**Da evitare:** le maiuscole sottili spaziate tra due filetti, le famiglie dentro cerchi, le virgolette giganti, il fondo scuro dominante, il rame.
Ritagli: `villani-specialita-scontornata.jpg`, `villani-mestieri-bianco-nero.jpg`.

### 2.4 Levoni, Castellucchio (Mantova) ([levoni.it](https://www.levoni.it/))
Cosa fa: pannelli divisi a metà, da una parte un campo rosso pieno con il titolo maiuscolo condensato e un link tra due filetti verticali, dall'altra la foto del prodotto; il pannello successivo è sfalsato e si incastra con il primo. Una foto ravvicinata dei cartellini dei salami appesi ("Salame Vecchia Osteria") con una targa rossa sopra. Prima del piede, una foto d'archivio dello stabilimento in bianco e nero a tutta larghezza con la targa rossa "Oltre un secolo di Levoni". Caratteri: Oswald (titoli) e Courier (testo).
**Gesto da riprendere:** la targa piena del colore del marchio posata su una foto, come un'etichetta; la foto d'archivio come chiusura della home; il pannello diviso colore e foto.
**Da evitare:** Courier per il testo, il corsivo calligrafico "per tradizione", le texture, il timbro "100% italiano", le virgolette, le foto di repertorio (mani unite).
Ritagli: `levoni-pannello-diviso.jpg`, `levoni-cartellini-dei-salami.jpg`, `levoni-archivio-con-targa.jpg`.

### 2.5 Maison Verot, charcuterie dal 1930 ([maisonverot.fr](https://www.maisonverot.fr/))
Cosa fa: apertura con quattro foto verticali affiancate; poi i prodotti, fotografati dall'alto o tagliati in sezione, tutti sullo stesso fondo grigio chiarissimo, con nome e prezzo sotto in piccolo; a 390 restano due colonne. Carattere: Montserrat.
**Gesto da riprendere:** il fondo uniforme che rende coerente un catalogo di prodotti diversi. Fontana ha 45 foto scontornate su trasparente: su un grigio chiaro uguale per tutte diventano un catalogo ordinato. Due colonne di prodotti anche a 390.
**Da evitare:** i badge rosa sopra le foto, carrello e prezzi.
Ritagli: `verot-apertura-quattro-foto.jpg`, `verot-prodotti-dall-alto.jpg`.

### 2.6 Cinco Jotas, Jabugo 1879 ([cincojotas.com](https://www.cincojotas.com/))
Cosa fa: tre prodotti fotografati sullo stesso set (muro e piedistallo color pietra); sotto, una didascalia in tre righe: nome in maiuscolo piccolo, "De bellota 100% ibérico", "DESCUBRIR" sottolineato. "Visita nuestra bodega": una fascia foto con una sola riga di testo e una freccia. Caratteri: Manofa e Mint Grotesk.
**Gesto da riprendere:** la didascalia in tre righe (nome, denominazione o formato, link) e la visita come fascia con una sola riga.
**Da evitare:** l'apertura video che nella cattura resta nera, l'oro su blu notte, il carattere a stencil, la fotografia di moda.
Ritaglio: `cincojotas-prodotti-stesso-set.jpg`.

### 2.7 Riferimenti funzionali

| Riferimento | Cosa fa | Cosa si prende | Ritaglio |
|---|---|---|---|
| [Monte Nevado](https://www.montenevado.com/en/) (prosciutto, Spagna) | per ogni prosciutto, i formati in righe separate da filetti: con osso 4,5-9 kg, disossato 2-2,5 kg, affettato 85-255 g | per Prosciutto Veneto DOP e crudo MEC i formati del sito attuale (intero, disossato), per lo speck intero e mezzo; i pesi solo se l'azienda li dà [DA CONFERMARE]. Senza le icone | `montenevado-formati-e-pesi.jpg` |
| [Carrasco Ibéricos](https://carrascoibericos.com/) | una tabella sobria che confronta tre categorie (razza, alimentazione, stagionatura minima, etichetta) | una tabella DOP e crudo MEC con dati verificabili: per il DOP dal disciplinare, per il MEC [DA CONFERMARE]. Il resto del sito (arancione, pulsanti "COMPRAR") no | `carrasco-tabella-di-confronto.jpg` |
| [Dario Cecchini](https://www.dariocecchini.com/) (macelleria, Panzano) | disegno dell'animale con i tagli numerati | per la parte carni (suino e bovino in quarti) solo se l'azienda conferma quali tagli vende [DA CONFERMARE] | `cecchini-tavola-dei-tagli.jpg` |
| Crosare (concorrente) | foto del marchio DOP impresso e spiegazione in due righe; "Schede tecniche" nel piede | un blocco breve sul marchio del Consorzio con il link all'elenco produttori dove compare Fontana; schede tecniche scaricabili se esistono [DA CONFERMARE] | `crosare-spiegazione-marchio-dop.jpg` |
| Attilio Fontana (concorrente) | la stessa strada nel 1919 e oggi | Fontana ha la foto del cortile del 1974 (banner del sito attuale): servirebbe la foto di oggi dallo stesso punto [foto da fare]; affiancate, senza cursore da trascinare | `attilio-fontana-ieri-e-oggi.jpg` |
| Brianza (concorrente) | una foto per prodotto con nome e famiglia | conferma che chi compra cerca la scheda del singolo prodotto | `brianza-catalogo-per-prodotto.jpg` |

### 2.8 Scartati

| Sito | Perché |
|---|---|
| Olympia (charcuterie americana), La Quercia, Smoking Goose, Handl Tyrol, Citterio | negozi per il consumatore, foto di repertorio o registro pop: non c'entrano con un salumificio che vende al banco |
| Wolf Sauris, Vulcano, Pierre Oteiza, Arturo Sánchez | pagine affollate, popup e questionari sopra i contenuti; di Wolf resta solo l'idea delle sei famiglie fotografate sullo stesso muro |
| Consorzio del Prosciutto di Parma | colori pop e titoli in Oswald; utile solo per come usa il castello di Torrechiara come immagine del territorio |
| Ruliano, Dok Dall'Ava, Leporati, Julián Martín | fondo nero e slogan, oppure grandi vuoti lasciati dalle animazioni allo scorrimento; Julián Martín usa un castello nello stemma come Fontana, ma in una pagina troppo carica |

## 3. Cosa si riprende

**Il materiale di Fontana** (misurato sul sito attuale; l'elenco completo è in 01): logo 1186x221 con la ragione sociale superata (S.n.c.); due banner 960x386 (la cantina con il tondo e le scritte "Montagnana, 1919" ed "Este, 1941"; il cortile con "1974"); striscia della storia 970x195 e una foto verticale 260x400; 45 schede prodotto con foto scontornata 450x450. Sulle etichette dei prodotti il marchio FONTANA è rosso su fasce bianche e verdi (le fascette incrociate del prosciutto, l'etichetta della sopressa, la fascia della mortadella); il tondo è verde sulle etichette e blu nel logo del sito. Le foto misurate non superano 970 px di larghezza: nessuna va a tutta pagina a 1440.

| Gesto | Da chi | Come diventa per Fontana | Limite |
|---|---|---|---|
| Il colore dell'etichetta come campo pieno | Pio Tosini, Levoni | il verde delle fascette diventa il colore del sito, in due o tre fasce piene (apertura, famiglie, contatti); il rosso resta alla scritta del marchio e ai segni piccoli | colore campionato dalle foto; il valore esatto si prende da un'etichetta vera [DA CONFERMARE] |
| Prodotti scontornati su un fondo uniforme | Maison Verot, Pio Tosini, Villani | catalogo per famiglia: foto su grigio chiaro, nome in maiuscolo stretto come sull'etichetta, una riga sotto con il formato | foto a 450 px: riquadri di circa 300 px a 1440 (4 colonne), 2 colonne a 390; su schermi retina restano morbide, il brief per nuove foto va nel LEGGIMI |
| Il prodotto come ritratto | Joselito | in testa alla pagina del Prosciutto Veneto DOP, il prosciutto intero in verticale, isolato sul campo verde, accanto alla denominazione completa | massimo 450 px di altezza, mai ingrandito |
| Famiglie con il conteggio | Joselito | "Stagionati", "Freschi", "Cotti", "Affumicati" con il numero dei prodotti | i numeri da 01 (elenco e schede oggi non coincidono) |
| Scheda in tre livelli | Villani, Cinco Jotas | nome del prodotto, denominazione o formato ("intero", "disossato"), link | solo dati del sito attuale |
| Storia con date e foto d'archivio | Pio Tosini, Levoni | 1919 Montagnana, 1941 Este e la barchessa, la requisizione, 1945, 1951 Lea Vezzù, oggi Giuseppe, Francesco e Bruno con la terza generazione (testo fermo al 2009: [DA CONFERMARE] chi conduce oggi); accanto le foto della storia e il cortile del 1974 | le foto d'archivio sono piccole: si mostrano in colonna, alla loro misura |
| La targa sulla foto d'archivio | Levoni | chiusura della home: la cantina del banner con una targa verde "Montagnana, 1919. Este, 1941" (le parole del banner attuale) | banner 960 px: in una colonna, non a tutta pagina |
| Formati in righe con filetti | Monte Nevado | per il DOP e il crudo MEC: intero, disossato; per lo speck: intero, mezzo | pesi [DA CONFERMARE] |
| Il marchio DOP spiegato | Crosare | due righe e il link alla pagina Produttori del Consorzio, dove Fontana è l'unico produttore di Este | testo solo da fonti citate in 01 |
| Interfaccia piccola | Joselito, Cinco Jotas | link in maiuscolo piccolo sottolineati, filetti sottili tra le sezioni; un solo pulsante pieno, il telefono | |
| Mobile | Joselito, Maison Verot | striscia di prodotti che scorre con la scheda successiva che sporge (scroll-snap, `data-scorre`); catalogo a due colonne a 390 | |

**Cosa non si riprende, perché lo fanno quasi tutti e nella cattura si rompe:** l'apertura con video o slider (vuota o nera nella cattura in Attilio Fontana, Bertelli, Cinco Jotas, Prolongo, Coati; scura e sfocata in King's); le texture di carta (Pio Tosini, Levoni, Ducale, Bertelli); il corsivo calligrafico (Levoni, Bertelli, La Quercia); fregi e scudi (King's); virgolette giganti (Villani, Levoni); contatori (Crosare); famiglie in cerchi (Villani); oro su nero (King's, Cinco Jotas); comparse in dissolvenza che lasciano vuoti (Leporati, Pio Tosini a 390). Il corsivo del marchio FONTANA resta solo nel logo.

## 4. Accoppiate

Caratteri usati oggi dai concorrenti, da non ripetere: Arial (Attilio Fontana), Marcellus + Montserrat (King's), Playfair Display + Open Sans (Brianza), Abril Fatface + Arbutus Slab + Roboto (Crosare), Playfair Display + Montserrat (Ducale), DIN Next + Dancing Script + Futura (Bertelli), Montserrat + Lato (San Marco), Nunito Sans (Consorzio), Nobile + Maven Pro (Fontana oggi). Le tre accoppiate qui sotto non ne usano nessuno. Contrasti calcolati con la formula WCAG 2.1; minimo 4,5 per il testo corrente, 3 per i titoli grandi.

### A. "Fascetta" (consigliata)

Nasce dalle etichette dei prodotti Fontana: fasce bianche e verdi, la scritta FONTANA rossa, le denominazioni in maiuscolo stretto ("SOPRESSA VENETA", "MORTADELLA"). È lo stesso metodo di Pio Tosini e Levoni, che vestono il sito con il colore della propria etichetta, ma con il colore di Fontana.

- **Caratteri:** [Archivo](https://fonts.google.com/specimen/Archivo), una sola famiglia con larghezza variabile (62-125) su Google Fonts, in tre usi:
  - titoli: Archivo 800, larghezza 112, maiuscolo, interlinea 1, 64 px a 1440 e 38 px a 390; pesante e largo come "SALUMIFICIO" nel logo;
  - nomi prodotto e denominazioni: Archivo 700, larghezza 75, maiuscolo, 16 px, spaziatura 0,02 em, come le scritte delle etichette e come le denominazioni sotto i prodotti di Pio Tosini e Villani;
  - testo: Archivo 400, larghezza 100, 18 px, interlinea 1,6; menu 15 px 600.
- **Palette:** verde fascetta `#155A38` (campionato dalle etichette tra `#0C5430` e `#18603C`), rosso marchio `#C8202B` (la scritta, scurita per reggere il testo), bianco `#FFFFFF`, grigio banco `#EFEFEC` (fondo uniforme delle foto prodotto, come Maison Verot), inchiostro `#1C1D1B`, grigio testo `#5A5F5B`, verde chiaro `#C9E2D2` per il testo secondario sul verde.
- **Uso:** il verde come campo pieno in due o tre fasce; il rosso solo su numeri delle date, voce di menu attiva, stato di focus e marchio, mai in blocchi grandi; foto d'archivio in bianco e nero o seppia come sono, prodotti a colori.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro `#1C1D1B` | bianco | 16,92 |
| inchiostro `#1C1D1B` | grigio banco `#EFEFEC` | 14,69 |
| grigio testo `#5A5F5B` | bianco | 6,52 |
| grigio testo `#5A5F5B` | grigio banco | 5,66 |
| bianco | verde `#155A38` | 8,23 |
| verde `#155A38` | bianco | 8,23 |
| verde `#155A38` | grigio banco | 7,14 |
| verde chiaro `#C9E2D2` | verde `#155A38` | 5,99 |
| rosso `#C8202B` | bianco | 5,68 |
| rosso `#C8202B` | grigio banco | 4,93 |
| bianco | rosso `#C8202B` | 5,68 |

### B. "Cantina"

Più quieta, per un sito che parla soprattutto di stagionatura. Il serif qui non è un'abitudine: le case del prosciutto viste usano un serif tondo per i nomi e i titoli (Joselito con SangBleu Kingdom, Villani con Lusitana, Dario Cecchini con Libre Caslon, Monte Nevado con Gilda Display), sempre accanto a un bastoni per l'interfaccia. Niente corsivo, niente fondo crema.

- **Caratteri:** [Newsreader](https://fonts.google.com/specimen/Newsreader) per i titoli, tondo, peso 500, taglio ottico 72, solo da 32 px in su (56 px a 1440, 34 px a 390); [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk) per testo (18 px), menu, didascalie e nomi prodotto in maiuscolo 600 a 14 px.
- **Palette:** nero cantina `#1F1B18` (dai bruni della foto della cantina, scuriti), bianco `#FFFFFF`, grigio sale `#EDEDEA`, grigio testo `#625C57`, rosso marchio `#C8202B` solo per i segni piccoli; sul nero testo bianco e secondario `#BDB5AC`, rosso schiarito `#E9584F`.
- **Limite:** è il registro più vicino al lusso; per un salumificio che vende al banco è la seconda scelta.

| Testo | Fondo | Contrasto |
|---|---|---|
| nero cantina `#1F1B18` | bianco | 17,10 |
| nero cantina | grigio sale `#EDEDEA` | 14,58 |
| grigio testo `#625C57` | bianco | 6,59 |
| bianco | nero cantina | 17,10 |
| secondario `#BDB5AC` | nero cantina | 8,44 |
| rosso `#C8202B` | bianco | 5,68 |
| rosso schiarito `#E9584F` | nero cantina | 4,86 |

### C. "Tondo"

Nasce dal logo del sito e dall'insegna: il tondo blu con il castello di Este e la scritta rossa. È la scelta giusta se l'azienda riconosce come suo il blu e non il verde delle etichette [DA CONFERMARE quale dei due colori considera suo]. Riferimenti: Dario Cecchini e Levoni, che usano un solo colore del marchio come fascia piena con il testo bianco.

- **Caratteri:** [Schibsted Grotesk](https://fonts.google.com/specimen/Schibsted+Grotesk), un bastoni nato per i giornali, solido nei pesi alti: titoli 800 (60 px a 1440, 36 px a 390), testo 400 a 18 px, nomi prodotto 700 maiuscolo a 15 px.
- **Palette:** blu tondo `#0B3A8E` (dal logo, `#083890`), rosso `#D0102B`, bianco `#FFFFFF`, grigio `#ECEEF2`, inchiostro `#111A2E`, grigio testo `#5B6170`, azzurro chiaro `#C9D4EA` per il testo secondario sul blu.
- **Limite:** il blu non c'è sulle etichette dei prodotti, che il cliente vede al banco.

| Testo | Fondo | Contrasto |
|---|---|---|
| inchiostro `#111A2E` | bianco | 17,34 |
| grigio testo `#5B6170` | bianco | 6,20 |
| bianco | blu `#0B3A8E` | 10,45 |
| blu `#0B3A8E` | grigio `#ECEEF2` | 8,99 |
| azzurro chiaro `#C9D4EA` | blu | 7,01 |
| rosso `#D0102B` | bianco | 5,54 |
| bianco | rosso `#D0102B` | 5,54 |

**Raccomandazione:** A. Viene dal materiale che Fontana ha già e che i clienti vedono ogni giorno (le etichette), si distingue da tutti i concorrenti (nessuno usa Archivo né un verde pieno), regge foto piccole perché la scala la fa la tipografia, e si costruisce in Elementor gratuito con un solo carattere variabile. Da B si innestano le foto della cantina in bianco e nero o seppia; da C il castello del tondo, usato piccolo come segno di Este.
