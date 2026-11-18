# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Aperti con Playwright (Chromium) a 1440 e a 390 px: il sito attuale, 4 concorrenti e 23 siti di riferimento (3 non raggiungibili, vedi sotto). Screenshot in `_prova/ricerca/` (`c*-` concorrenti, `r-*` riferimenti; `-vista` è la prima schermata, senza suffisso la pagina intera), pezzi ritagliati in `_prova/ricerca/ritagli/` (numerati, citati qui sotto). Caratteri e colori dei siti sono letti dal browser (stile calcolato e font caricati, script `_prova/script/ricerca.mjs`, `css.mjs`, `colore.mjs`), i contrasti sono calcolati con la formula WCAG 2.1.

Limiti incontrati, da sapere prima di riaprire i siti:
- Hotel Elephant (Bressanone) non risponde attraverso il proxy (`ERR_TUNNEL_CONNECTION_FAILED`); La Subida (Cormons) mostra un captcha; Dolada (Alpago) risponde "We couldn't verify the security of your connection". Non usati.
- Locanda Cipriani, Echaurren e Butterfield & Robinson aprono con un video che al browser automatico dà "Player error": giudicati sul resto della pagina.
- Waldhaus Sils resta bianco a 1440 (contenuti che entrano in animazione) e non si carica a 390. Non usato.
- Ca' Rocca a 390 blocca la cattura a pagina intera: fotografato con una finestra alta 2400 px (`c4-carocca-390.png`).
- Bouillon Chartier scorre dentro un contenitore, la cattura a pagina intera si ferma a 900 px: fotografato con finestra alta 5000 px (`r-chartier-1440-alta.png`).

## Premessa: che cosa è il Leon d'Oro e con che cosa lavoriamo

Dal sito attuale (pagine in `_prova/crawl/`): Albergo Ristorante "Leon d'Oro", Viale Fiume 20, 35042 Este (PD), tel. 0429 602949, prenotazioni@leondoroeste.it, P.IVA 04185510288. Albergo 2 stelle "sorto agli inizi del 900 nei pressi della Porta Vecchia", gestito dalla "4° generazione della famiglia Rubini". Ristorante di cucina tipica veneta "secondo la tradizione, senza rivisitazioni" (Musso con polenta, Baccalà alla vicentina, Bigoli alla boscaiola, Fegato alla veneziana), menù di pesce il venerdì sera ("è gradita la prenotazione"), chiuso la domenica, "le nostre proposte variano ogni giorno". Listino 2026 pubblicato: singola 50,00 €, doppia/matrimoniale 75,00 €, mezza pensione 65,00 € e pensione completa 80,00 € a persona, bevande incluse. Bike hotel con garage privato, collaborazione con il Team Este Bike (ritrovo in piazza alle 9.00 d'inverno, 8.30 d'estate), ciclovia E2. Una pagina intera per chi deve andare all'ospedale (Ospedali Riuniti Padova Sud "Madre Teresa di Calcutta", a Schiavonia).

Il materiale che c'è già (`ritagli/00-leondoro-materiale.jpg`, `25-` e `26-leondoro-oggi`):
- **il logo**: un leone disegnato a tratto, criniera tratteggiata come un'incisione, e la scritta ALBERGO ★★ LEON D'ORO ESTE in un bastoncino nero pesante. Sul sito esiste solo dentro `images/presentazione_r3_c1.jpg`, 311 x 231 px, con la foto della torre dietro: per usarlo serve il file originale **[DA CONFERMARE]**;
- **la cartolina** (`foto/vecchia-cartolina.jpg`, 501 x 402 px): il viale in bianco e nero, con le scritte ALBERGO - RISTORANTE e LEON D'ORO in verde (misurato #2C6F33) su carta chiara (#F7FBE7);
- **la facciata** (`images/esterno.jpg`, 420 x 315 px, d'inverno, con la neve): muro giallo ocra (misurato #CEAE5A, in ombra), persiane verdi (#4E6D6E), cornici di pietra chiara (#C0BEBD), insegna in corsivo sul muro;
- **sala e camere** a 1200 x 800 px: travi di legno, tovaglie gialle e bianche, sedie in legno;
- **piatti** (baccalà 960 x 720 px; secondo l'analisi del sito fino a 2048 x 1536 in `/foto/`), video su Facebook.

Il giallo della facciata, il verde delle persiane e della cartolina, il leone a tratto: l'identità del nuovo sito nasce da qui, non da una tavolozza scelta a tavolino. Il limite è la risoluzione: cartolina e facciata sono piccole, nessuna delle due può fare da sfondo a tutta larghezza.

## 1. Concorrenti

Quattro strutture vere, nella stessa città o vicino all'ospedale di Schiavonia, che si contendono lo stesso ospite: chi visita i Colli in bici, chi lavora in zona, chi accompagna un ricoverato.

| # | Concorrente | Zona | In comune con il Leon d'Oro | Cosa fa meglio | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Hotel Beatrice](https://www.hotel-beatrice.com/) | Este, Viale Rimembranze 1 (3 stelle, "since 1966" nel logo) | stessa città, ospiti di passaggio e di lavoro | servizio fotografico professionale (firmato nel piede: Margherita Bonetti), due linee di camere (Style e Smart) con foto grandi, leggibile a 390 (scrollWidth 390), italiano, inglese e tedesco | nessun prezzo, il ristorante non compare in home, servizi come icone in griglia (`ritagli/23`), mappa vuota nello screenshot di "Come raggiungerci", refuso "maggiormente legale alla tipologia standard"; testo in Work Sans petrolio #005A70 (7,79:1, buono) | `c1-beatrice-1440.png`, `-390.png` |
| 2 | [Hotel Centrale](https://hotelcentraledeste.com/) | Este, Piazza Beata Beatrice 15 (3 stelle) | **stessa epoca dichiarata**: "aperto ancora nei primi anni del 900", titolo da telefono "Il più antico hotel di Este"; anche loro #bikehotel con deposito bici | cartoline storiche in apertura (`ritagli/20`), schede camere con ospiti, metri quadri e "Prenota" (`21`), pagina eventi, foto vere della stanza bici | testo in Roboto peso 100 grigio #878787 su bianco (3,59:1, sotto la soglia AA), link "Covid-19" ancora in testata nel 2026, widget eventi esterno che allunga la pagina a 10.292 px a 1440, niente ristorante | `c2-centrale-1440.png`, `-390.png` |
| 3 | [Blue Dream Hotel](https://www.bluedreamhotel.it/) | Monselice, Via Orti 7 (67 camere, dal 1984) | albergo con ristorante aperto agli esterni (Il Blue), nello stesso comune dell'ospedale di Schiavonia, pagina cicloturismo | "Prenota ora" e telefono sempre in vista, pagina cicloturismo con PDF dell'anello dei Colli e piantina scaricabili, offerte speciali, FAQ | l'ospedale non è nominato in home, servizi, FAQ e dove siamo; titolo in Audiowide minuscolo, occhiello grigio #97918C su #FAFAFA (2,98:1), bottoni "Discover more" in inglese nella versione italiana, carosello e riquadro "Eco-sostenibilità" sopra la foto; nessun menù né prezzo nella pagina del ristorante (`ritagli/24`) | `c3-bluedream-1440.png`, `-390.png` |
| 4 | [Ca' Rocca Relais](https://carocca.it/) | Monselice, Via Basse 2 (3 stelle, bed & breakfast) | ospiti di lavoro e di passaggio, punto di partenza per i Colli | calendario check-in/check-out nella prima schermata, prenotazione diretta (`ritagli/22`), novità datate ("sala colazioni rinnovata nel 2025"), P.IVA e SDI nel piede | **a 390 scorre di lato** (scrollWidth 407 su 390), niente ristorante, testo nel carattere di sistema, frasi generiche ("Un'oasi di tranquillità", "In una posizione strategica") | `c4-carocca-1440.png`, `-390.png` |

Il sito attuale del Leon d'Oro, per confronto (`c0-leondoro-*`, `ritagli/25` e `26`): a 390 la pagina resta larga 980 px e tutto è rimpicciolito (testo Verdana 12 px grigio #666666), il contenuto vive in un riquadro fisso di 800 px.

**Cosa fanno meglio del Leon d'Oro:** sono leggibili da telefono; mettono la prenotazione in vista (Ca' Rocca e Blue Dream con il calendario o il bottone fisso); mostrano le camere una per una con capienza e metri quadri (Centrale); usano foto fatte da un fotografo (Beatrice, Blue Dream); il Centrale racconta la stessa storia "primi del Novecento" con le cartoline.

**Cosa non fa nessuno (spazio per il Leon d'Oro):**
1. **prezzi in chiaro**: nessuno dei quattro pubblica un prezzo in home; il Leon d'Oro ha il listino 2026 e la mezza pensione con bevande incluse;
2. **una cucina vera, con i piatti per nome**: il Beatrice non mostra il ristorante, il Centrale e Ca' Rocca non lo hanno, Blue Dream non pubblica il menù. Il Leon d'Oro ha un menù lungo, il pesce del venerdì, il giorno di chiusura;
3. **l'ospedale**: nessuno lo nomina. Il Leon d'Oro ha già una pagina, da aggiornare (parla ancora di "nuovo polo ospedaliero" e "dal 5 novembre 2014");
4. **la bici come compagnia, non solo come deposito**: il Centrale ha una stanza bici, Blue Dream i PDF, solo il Leon d'Oro esce in gruppo con una squadra del posto (Team Este Bike, ritrovo in piazza) **[DA CONFERMARE che le uscite ci siano ancora]**;
5. **la famiglia**: quarta generazione della stessa famiglia, detta dal sito; tra i concorrenti solo Blue Dream racconta il suo fondatore (1984) e Ca' Rocca scrive "servizio famigliare"; il piede del Beatrice riporta una S.r.l. di Milano.

**Attenzione alla storia:** il Centrale si dice "il più antico hotel di Este" e "aperto nei primi anni del 900", la stessa epoca del Leon d'Oro. Il nuovo sito dice solo quello che il Leon d'Oro scrive di sé ("sorto agli inizi del 900 nei pressi della Porta Vecchia"), senza primati e senza un anno preciso finché la famiglia non lo conferma **[DA CONFERMARE l'anno]**.

**Posizionamento proposto:** "Albergo e trattoria a Este, della stessa famiglia da quattro generazioni. Cucina veneta come una volta, camere da 50 €, garage per le bici, vicino all'ospedale di Schiavonia." Contro il Beatrice (appena rinnovato, ma senza prezzi e senza cucina in vista) il Leon d'Oro vince su cucina e prezzo; contro il Centrale (stessa storia, niente ristorante) sulla tavola; contro Blue Dream e Ca' Rocca (Monselice, piscina) su centro di Este, famiglia e bici.

**Copy evitato** (visto nei concorrenti): "Un'oasi di tranquillità" (Blue Dream e Ca' Rocca, uguale), "un soggiorno davvero speciale", "in una posizione strategica", "Molto di più di un hotel", "dotate di ogni comfort", "ambiente elegante e raffinato", "il più antico".

## 2. Riferimenti premium

Il Leon d'Oro è un albergo di paese con trattoria, di famiglia, con prezzi bassi e una cucina che non si reinventa. I riferimenti giusti non sono gli hotel di lusso né le spa: sono le **trattorie e le locande storiche che hanno trasformato la loro semplicità in un'identità forte**, più un operatore di cicloturismo per la parte bici. Sette, tutti aperti e fotografati; per ognuno un gesto preciso e cosa non prendere.

### 2.1 Bouillon Chartier, Parigi (dal 1896)
[bouillon-chartier.com](https://www.bouillon-chartier.com/). Trattoria popolare storica: cucina francese di tradizione a prezzi bassi, tre sale a Parigi.
- **Gesto da riprendere:** apertura con una foto d'archivio in bianco e nero e sopra il titolo in maiuscolo bastoncino pesante, bianco, con la frase dei fondatori e l'anno ("Offrir un repas digne à un prix modeste. Les frères Chartier / 1896", `ritagli/01`). Poi **i fatti detti chiari**, in poche righe: "Ouvert 365 j/an, de 11h30 à minuit, service continu sans réservation" (`02`), "Des entrées à partir de 1 €, des plats à 7 €" (`03`). Un solo colore forte (rosso #C31729) su bianco, foto d'archivio in bianco e nero, foto di piatti a colori.
- **Per il Leon d'Oro:** la cartolina del viale come foto d'archivio, il leone come firma, il listino detto in una riga ("Singola 50 €, doppia 75 €, mezza pensione con bevande 65 € a persona").
- **Cosa evitare:** le foto ritagliate a nuvola, i titoli curvi, i bottoni a pillola, la frase in francese da manifesto: sono il loro tono, non il nostro, e sono fragili in Elementor. La foto a tutta larghezza: la cartolina è di 501 px.

### 2.2 St. JOHN, Londra (Smithfield)
[stjohnrestaurant.com](https://stjohnrestaurant.com/a/restaurants/smithfield). Ristorante di cucina britannica di tradizione, famoso proprio per non reinterpretarla.
- **Gesto da riprendere:** l'emblema inciso (un maiale disegnato a tratto, piccolo, in testata e ripetuto nel piede) accanto a un nome scritto semplice (`ritagli/04`). Nella pagina del locale: nome grandissimo, indirizzo, poi "Our menus are updated daily" e gli orari in due colonne (LUNCH, SUPPER) con la chiusura scritta per esteso ("Sunday evening: closed"). Sotto, tre regole di casa in tre colonne corte, con il prezzo esatto (tappo 32 sterline, torta portata da fuori 5 sterline a persona, servizio 12,5%, `05`). Un solo carattere (Georgia), nero su bianco, una foto della sala con le tovaglie bianche.
- **Per il Leon d'Oro:** il leone a tratto fa lo stesso lavoro del maiale; la frase del sito "Le nostre proposte variano ogni giorno" fa lo stesso lavoro di "updated daily"; "chiuso la domenica" e "il venerdì sera pesce, gradita la prenotazione" diventano le loro regole di casa.
- **Cosa evitare:** l'impaginazione da negozio online (carrello, iscrizione alla newsletter in due campi), il menù a tendina "View Menus", il serif piccolo nel piede.

### 2.3 Locanda San Lorenzo, Puos d'Alpago (Belluno)
[locandasanlorenzo.it](https://www.locandasanlorenzo.it/). "Ristorante e Albergo", "da quattro generazioni": la stessa forma del Leon d'Oro, in Veneto (il ristorante oggi è stellato, ma la forma è la stessa: "il ristorante è affiancato da un albergo", scrivono loro).
- **Gesto da riprendere:** **la prima schermata divisa in due porte**, a sinistra RISTORANTE, a destra ALBERGO, ognuna con una foto in bianco e nero a tutta altezza, una frase e la parola sottolineata come link (`ritagli/06`). A 390 le due metà si impilano e restano due blocchi a schermo pieno (`07`). Poco sotto, una barra con tre accessi: prenota tavolo, prenota camera, buono regalo. Nel piede c'è il CIN (codice identificativo nazionale) e il giorno di chiusura del ristorante.
- **Per il Leon d'Oro:** sala (1200 x 800) a sinistra, camera (1200 x 800) a destra, ognuna larga al massimo 720 px a 1440: la risoluzione basta.
- **Cosa evitare:** le icone a tratto sottile per "prenota tavolo" e "buono regalo", il testo grigio chiaro in Outfit Light, i piatti da ristorante stellato: il Leon d'Oro non deve sembrare quello che non è.

### 2.4 Trattoria Masuelli San Marco, Milano (dal 1921)
[masuellitrattoria.com](https://www.masuellitrattoria.com/). Trattoria milanese di famiglia.
- **Gesto da riprendere:** **un campo verde pieno** (misurato #154734) con il nome in maiuscolo stretto e "DAL 1921" sotto, piccolo, centrato (`ritagli/08`); il giallo arriva dal piatto, non dalla grafica (il risotto alla milanese nelle tessere, `09`). Le tessere della home sono poche e diverse tra loro: una verde con il logo, una nera, una bianca di solo testo, una foto.
- **Per il Leon d'Oro:** verde e giallo sono già i colori della casa (persiane e facciata), e il giallo delle tovaglie e della polenta sta nelle foto vere. È la conferma, da una trattoria storica vera, che verde pieno e giallo non sono un capriccio.
- **Cosa evitare:** il pannello "prenota un tavolo" che a 390 copre il nome; il bottone WhatsApp fisso sopra il contenuto; le tessere con bordo sottile.

### 2.5 Antica Trattoria della Pesa, Milano (dal 1880)
[anticatrattoriadellapesa.com](https://www.anticatrattoriadellapesa.com/). Locale Storico d'Italia, cucina lombarda.
- **Gesto da riprendere:** **la striscia delle informazioni subito sotto l'apertura**: a sinistra "Locale Storico d'Italia, dal 1880", al centro il bottone MENU, poi "Prenotazioni" con telefono ed email, poi "Lun-Sab, Domenica Chiuso, Pranzo 12.30-14.30, Cena 19.00-23.00" (`ritagli/10`). A 390 gli orari diventano il blocco più grande della pagina dopo il nome (`11`).
- **Per il Leon d'Oro:** telefono 0429 602949, "domenica chiuso", "venerdì sera pesce", listino, subito sotto le due porte. Gli orari di pranzo e cena non sono sul sito **[DA CONFERMARE]**.
- **Cosa evitare:** fondo crema #E6DCC8 con serif e corsivi in rosso: è la combinazione già bocciata nella seconda versione di Benvegnù, e qui funziona per un locale milanese dell'Ottocento con le sue maioliche, non per un albergo giallo e verde di Este.

### 2.6 Troisgros, Ouches (Loira)
[troisgros.fr](https://www.troisgros.fr/). Casa di famiglia (quattro generazioni, lo scrivono loro) con ristorante, albergo e gîte.
- **Gesto da riprendere:** la home in due capitoli, "Tables" e "Hospitalité", ognuno fatto di **righe con la foto a sinistra e il testo a destra**, separate da un filetto, con in fondo una riga di servizio in maiuscoletto preceduta da un trattino ("RESTAURANT GASTRONOMIQUE, À OUCHES", `ritagli/12` e `13`). Dove una foto non c'è o non serve, **un disegno a tratto** (la fattoria in assonometria, la siepe col cuoco): la pagina resta viva senza foto stock.
- **Per il Leon d'Oro:** le camere (singola, doppia/matrimoniale) e la tavola (menù di carne, venerdì pesce) come righe di questo tipo; il leone a tratto, non illustrazioni nuove inventate.
- **Cosa evitare:** il carattere disegnato su misura e i corpi sottili (Yoga Sans 300 su grigio #F5F5F5), il tono da tre stelle Michelin, l'apertura con un albero a tutto schermo senza informazioni.

### 2.7 DuVine, viaggi in bicicletta
[duvine.com, Italian Coast-to-Coast](https://www.duvine.com/tour/italy-sea-sea-bike-tour/). Operatore di cicloturismo di fascia alta.
- **Gesto da riprendere:** il "Ride Profile": una riga di quattro numeri grandi con l'etichetta sotto (dislivello medio, distanza media, dislivello totale, distanza totale) e sotto il profilo altimetrico di ogni tappa con il nome dei paesi (`ritagli/14`). In testa al viaggio, i fatti in righe brevi: giorni, livello, prezzo.
- **Per il Leon d'Oro:** la pagina bici con i numeri veri che il sito già dà: anello E2 70 km, ritrovo in piazza alle 9.00 (inverno) e 8.30 (estate), garage privato. Il profilo altimetrico solo con un tracciato vero (GPX del Team Este Bike o del Parco dei Colli) **[DA CONFERMARE]**, mai disegnato a occhio.
- **Cosa evitare:** le icone dentro cerchi gialli, il menu laterale "On this page", le stelle e le recensioni.

### Riferimento funzionale: il piede con P.IVA e CIN
[Hotel Gasthof Kohlern](https://www.kohlern.com/), Bolzano: una riga sola nel piede con nome, famiglia, indirizzo, telefono, email, P.IVA e CIN (`ritagli/15`). Lo fa anche la Locanda San Lorenzo. Il CIN va esposto da chi affitta camere (art. 13-ter del DL 145/2023); sul sito del Leon d'Oro non si trova **[DA CONFERMARE il codice]**.

### Visitati e scartati

| Sito | Perché no |
|---|---|
| [Rules](https://rules.co.uk/), Londra 1798 | fondo crema, EB Garamond corsivo, foto calde con ombre: è il cliché "lusso storico", da evitare |
| [Locanda Cipriani](https://locandacipriani.com/), Torcello | crema e Cormorant Garamond corsivo, stesso cliché; video in errore |
| [Hirschen](https://www.hotel-hirschen-bregenzerwald.at/), Schwarzenberg | nero di lusso, foto piccole su fondo nero, slogan in inglese: non è un 2 stelle |
| [Del Cambio](https://delcambio.it/), Torino 1757 | introduzione animata con illustrazioni e "skip intro" |
| [Krone](https://www.krone-hittisau.at/), [Cavallino d'Oro](https://www.cavallino.it/it/home.html), [Agli Amici](https://www.agliamici.it/), [Kohlern](https://www.kohlern.com/) | locande storiche vere ma siti medi: slider, corsivi decorativi, onde, testo centrato lungo (di Kohlern resta solo il piede) |
| [Echaurren](https://echaurren.com/), [Casa Gerardo](https://www.casagerardo.es/), [Antica Corte Pallavicina](https://www.anticacortepallavicinarelais.it/) | template generici; Casa Gerardo e Pallavicina scorrono di lato a 390 (417 e 405 px) |
| [Butterfield & Robinson](https://www.butterfield.com/) | i viaggi si caricano solo via script; DuVine mostra lo stesso contenuto meglio |

## 3. Cosa si riprende (sezione per sezione)

| Sezione del nuovo sito | Gesto | Da | Materiale vero | Limite da rispettare |
|---|---|---|---|---|
| Testata | leone a tratto piccolo + nome scritto semplice, telefono sempre visibile | St. JOHN, Blue Dream (telefono) | logo attuale | serve il logo originale; se non c'è, il leone va ridisegnato con il permesso della famiglia |
| Apertura Home | due porte affiancate, ALBERGO e RISTORANTE, a tutta altezza; a 390 una sopra l'altra | Locanda San Lorenzo | camera 1200 x 800, sala 1200 x 800 | ogni metà al massimo 720 px a 1440; niente slider |
| Striscia sotto l'apertura | telefono, "domenica chiuso", "venerdì sera pesce", listino in una riga | Pesa, Chartier | testi e listino 2026 del sito | orari del ristorante da confermare |
| Prezzi | detti in chiaro, in righe, con "bevande incluse" | Chartier | listino 2026 | si aggiornano a ogni stagione: un solo punto da cambiare |
| Ristorante | il menù come testo, "le proposte variano ogni giorno", regole di casa con il dettaglio pratico | St. JOHN | menù del sito, chiusura, venerdì pesce | niente PDF del menù, niente prezzi dei piatti se non li danno |
| Camere | righe foto a sinistra, testo a destra, filetto, riga di servizio in maiuscoletto (capienza, prezzo) | Troisgros, schede del Centrale | foto camere 1200 x 800, bagni | metri quadri solo se la famiglia li dà **[DA CONFERMARE]** |
| Storia | cartolina in bianco e nero alla sua misura, con il titolo grande accanto e la frase di famiglia | Chartier | cartolina 501 x 402, "4° generazione", "Porta Vecchia" | mai oltre 501 px; nessun anno inventato, nessun "il più antico" |
| Bici | riga di numeri grandi con etichetta, poi il ritrovo e il garage | DuVine | E2 70 km, ritrovo 9.00/8.30, garage | profilo altimetrico solo con GPX vero |
| Ospedale | una pagina pratica: come arrivarci, navetta, taxi, telefono | (nessun concorrente lo fa) | pagina attuale | dati 2014 da aggiornare **[DA CONFERMARE]** |
| Piede | una riga: ragione sociale, indirizzo, telefono, email, P.IVA, CIN | Kohlern, San Lorenzo | P.IVA 04185510288 | CIN da chiedere |

Scartato in tutte le sezioni: slider e caroselli, icone dei servizi in griglia, collage di cartoline, video in apertura, testo grigio sottile, popup sopra la foto, effetti allo scorrimento.

## 4. Accoppiate

Tre accoppiate di caratteri e colori, tutte da Google Fonts e tutte presenti nell'elenco dei font di Elementor 4.3.3 (verificato in `includes/fonts.php` di Elementor 4.3.3 nell'istanza di prova del kit `wp-gardenspav`, stessa versione; quella del Leon d'Oro non è ancora creata), con i colori misurati sul materiale dell'azienda. Prova a colori in `ritagli/31-accoppiate.png`, prova dei caratteri candidati in `ritagli/30-prova-caratteri.png`.

### A. "Facciata": Libre Franklin, una famiglia (consigliata)

- **Caratteri:** Libre Franklin 800 in maiuscolo per titoli e nome; Libre Franklin 400 e 600 per testo, menù, prezzi e bottoni.
- **Perché:** è la versione libera del Franklin Gothic, il grottesco disegnato da Morris Fuller Benton nel 1902, negli anni in cui, secondo il sito, nasceva il Leon d'Oro: un maiuscolo pesante e largo come le scritte della cartolina e del logo. È il gesto di Chartier (bastoncino maiuscolo pesante sopra la foto d'archivio) e di Masuelli (nome in maiuscolo su campo verde), con un carattere che nessun concorrente usa (Work Sans, Gilda Display, Roboto, Montserrat, Audiowide). Occhio medio alto (0,53 dell'em): si legge bene a 390, anche per chi non vede bene. Diversa da Benvegnù: lì una famiglia stretta in due larghezze, qui una famiglia larga in due pesi.
- **Palette** (dai colori misurati della casa):

| Ruolo | Colore | Da dove |
|---|---|---|
| verde persiana: testata, piede, una fascia piena, titoli su bianco | #263F40 | persiane #4E6D6E, stessa tinta scurita |
| giallo facciata: un solo campo per pagina (listino o "prenota"), mai testo su bianco | #D3AB45 | muro #CEAE5A misurato in ombra, schiarito **[DA CONFERMARE sul colore vero]** |
| bianco tovaglia: fondo | #FFFFFF | tovaglie della sala |
| pietra: fasce di servizio (orari, piede secondario) | #ECEAE5 | cornici delle finestre #C0BEBD, schiarite |
| inchiostro: testo | #1B201F | |
| grigio testo: note, didascalie | #5A615F | |

| Testo su fondo | Contrasto |
|---|---|
| inchiostro su bianco | 16,5:1 |
| verde persiana su bianco / bianco su verde persiana | 11,25:1 |
| inchiostro su pietra | 13,72:1 |
| verde persiana su pietra | 9,35:1 |
| inchiostro su giallo facciata | 7,6:1 |
| grigio testo su bianco | 6,34:1 |
| grigio testo su pietra | 5,28:1 |
| giallo facciata su verde persiana | 5,18:1 |
| giallo facciata su bianco | 2,17:1, **mai per testo** |

- **Foto:** la cartolina in bianco e nero alla sua misura; sala, camere e piatti a colori come sono, senza viraggi (il giallo delle tovaglie e della polenta è già il colore della casa); il leone a tratto in verde persiana o in bianco, mai sopra una foto.
- **Rischi:** troppo giallo diventa "Quarto di Litro" (la critica alla prima versione di Benvegnù): il giallo è un campo per pagina, il resto è bianco e verde. Libre Franklin non ha le cifre tabellari: i prezzi stanno in righe allineate a destra, non in colonne di numeri.

### B. "Tovaglia": Gelasio, una famiglia

- **Caratteri:** Gelasio 700 in maiuscolo spaziato per i titoli, Gelasio 400 per il testo; cifre allineate (`lnum`, presenti nel font) per prezzi e orari. Mai corsivo.
- **Perché:** Gelasio è costruito con le stesse misure di Georgia, il carattere di St. JOHN, il riferimento più vicino a "cucina di tradizione senza rivisitazioni"; un serif motivato da quel sito e dal menù come testo, non dall'abitudine. Su bianco puro, come St. JOHN, non su crema.
- **Palette:** nero #111111, bianco #FFFFFF, verde cartolina #245B2A (dalle scritte #2C6F33 della cartolina, scurito) per link, voce attiva e prezzi, grigio #5C5C5C per le note, fascia #F4F4F2. Il giallo resta nelle foto.

| Testo su fondo | Contrasto |
|---|---|
| nero su bianco | 18,88:1 |
| nero su fascia #F4F4F2 | 17,15:1 |
| verde cartolina su bianco / bianco su verde | 8,06:1 |
| verde cartolina su fascia | 7,32:1 |
| grigio su bianco | 6,69:1 |

- **Rischi:** è la più vicina al "classico" già bocciato su Benvegnù; tiene solo se resta bianca, nera e dritta. Funziona meglio per le pagine Ristorante e Menù che per la Home.

### C. "Insegna larga": Archivo Black + Public Sans

- **Caratteri:** Archivo Black (un solo peso, largo e nero) per il nome e i titoli brevi; Public Sans 400 e 600 per il testo, con cifre tabellari (`tnum`) per listino e orari. Public Sans deriva da Libre Franklin: stessa famiglia di forme di A.
- **Perché:** è il carattere più vicino alle lettere del logo LEON D'ORO (bastoncino largo e pesante, `ritagli/30`). Con un solo colore forte, come Chartier con il suo rosso: qui il verde della cartolina.
- **Palette:** verde cartolina #245B2A pieno, bianco, nero #121413, grigio fascia #F2F2F0, testo secondario #4F5552; giallo #D3AB45 solo in corpo grande sul verde.

| Testo su fondo | Contrasto |
|---|---|
| nero su bianco | 18,5:1 |
| nero su grigio fascia | 16,5:1 |
| nero su giallo | 8,53:1 |
| bianco su verde cartolina | 8,06:1 |
| testo secondario su bianco | 7,63:1 |
| verde su grigio fascia | 7,19:1 |
| giallo su verde cartolina | 3,72:1, **solo da 24 px (o 19 px in grassetto) in su** |

- **Rischi:** un carattere largo occupa molto a 390: "PRENOTAZIONI CAMERE" va a capo male; i titoli devono restare di una o due parole. Più vicino al tono di Chartier, più rumoroso del Leon d'Oro.

### Scelta consigliata per la fase 2.3

**A, "Facciata"**, con un innesto da B: le righe del menù e le regole di casa del ristorante impaginate come St. JOHN (testo, filetti, niente icone), ma in Libre Franklin. Motivi: è l'unica che usa insieme i due colori veri della casa (facciata e persiane) e un carattere della stessa epoca dell'albergo; si legge meglio a 390 per un pubblico anche anziano; Libre Franklin è nell'elenco di Elementor, nessun font da caricare a mano; non somiglia né a Benvegnù (stretto, nero e rosso cuoio) né ai concorrenti.

Da confermare con la famiglia prima della costruzione: logo originale (vettoriale o ad alta risoluzione), cartolina originale a risoluzione più alta, colore vero della facciata, orari del ristorante, CIN, anno di apertura se esiste, uscite in bici ancora attive, foto nuove della facciata (quella sul sito è 420 x 315 px).
