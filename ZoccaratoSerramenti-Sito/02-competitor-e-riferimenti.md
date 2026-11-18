# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Siti aperti dal vivo con Playwright (Chromium attraverso il proxy) a 1440 e a 390 px, pagina intera fino a 9000 px di altezza. Screenshot grezzi in `_prova/ricerca/` (`c*-` concorrenti, `r-*` riferimenti), pezzi tagliati per la lettura in `_prova/ricerca/pezzi/`, ritagli dei gesti da riprendere in `_prova/ricerca/ritagli/`, prova delle tre accoppiate in `_prova/ricerca/campione-accoppiate-1440.png`.

I concorrenti sono stati trovati negli elenchi comunali di aziende.it (codici ATECO 25.12 "porte e finestre in metallo" e 43.32 "posa di infissi") per Borgoricco e i comuni vicini: Camposampiero, Campodarsego, Santa Giustina in Colle, Villanova di Camposampiero, Massanzago, San Giorgio delle Pertiche, Loreggia, Piombino Dese, Trebaseleghe, Cadoneghe, Vigodarzere. Su aziende.it nessuno ha il sito indicato: i domini sono stati verificati uno per uno.

## 1. Concorrenti

| # | Concorrente | Zona | Cosa vende | Cosa fa meglio di Zoccarato | Cosa fa peggio | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Serramenti Longato](https://www.longato.com/) | Piombino Dese (PD), via Pacinotti 45/b | serramenti in PVC e alluminio, scuri, portoncini, alzanti scorrevoli | sito responsive con barra fissa "Chiama / Dove trovarci / Contattaci" sul telefono; catalogo e "project book" scaricabili; articoli recenti (29 e 22 settembre 2026) con guide ai prezzi e alla scelta PVC o alluminio | l'apertura è il manifesto di una fiera (MAV Festival 2026), non un loro lavoro; in home foto da studio e nessuna realizzazione con un luogo; testo 14 px con spaziatura 1,4 px, faticoso; le tessere "I nostri prodotti" sono quasi bianche | `c1-longato-1440.png`, `c1-longato-390.png`, ritaglio `conc-longato-guide.jpg` |
| 2 | [Reale Infissi](https://www.realeinfissi.it/) | showroom Santa Giustina in Colle (PD), via Roma 25; sede operativa Villa del Conte (PD) | serramenti, scuri, porte, zanzariere | l'apertura è una foto vera del laboratorio con due persone che montano un telaio; modulo "Richiedi un preventivo" in 5 passi (misura LxH del vecchio serramento, tipologia, accessori, tipo di intervento, poi la telefonata del tecnico) con allegato di foto; gira su Elementor 4.3.4, lo stesso strumento che useremo | le schede prodotto compaiono solo con un'animazione allo scorrimento: nella cattura a pagina intera restano bianche, a 390 l'apertura sparisce; menu bianco poco leggibile sopra la foto; quattro caratteri diversi (Assistant, Raleway, Rubik, Open Sans) | `c2-reale-infissi-1440.png`, `c2-reale-infissi-390.png`, ritaglio `conc-reale-preventivo-passi.jpg` |
| 3 | [Aloox](https://www.aloox.it/) (Aloox srl, P.IVA 05370850280) | Santa Giustina in Colle (PD) | persiane e scuri in alluminio per rivenditori e serramentisti (B2B) | le tre famiglie (persiane, scuri, motorizzati) mostrate con foto del prodotto in bianco e nero su muro chiaro: si capisce subito cosa fanno | più fornitore che concorrente diretto; Inter ovunque; slogan generico sopra una foto velata di scuro; testo di presentazione vago | `c3-aloox-1440.png`, `c3-aloox-390.png`, ritaglio `conc-aloox-prodotti-bn.jpg` |
| 4 | [L'infisso](https://www.linfissodesign.it/) (P.I. 03338830288) | San Giorgio delle Pertiche (PD), via Ungheria 23/C | vendita e posa di finestre, scuri, portoncini, blindati, porte | telefono ed email sempre visibili nella barra in alto; i passi del servizio dichiarati (consulenza, sopralluogo, installazione, garanzia) | a 1440 il menu va a capo e "Contatti" resta da solo su una seconda riga; servizi in riquadri con icone; foto generiche (una riunione con portatile); promuove ancora "paga le tue nuove finestre la metà" con la cessione del credito Ecobonus, bloccata per i nuovi lavori dal DL 11/2023 | `c5-linfisso-1440.png`, `c5-linfisso-390.png` |
| 5 | [Zoccarato Giannino](https://www.zoccaratoserramenti.com/) ("Zoccarato Serramenti in PVC dal 1968") | Fagnano Olona (VA) | serramenti in PVC su misura | modulo "Prenota un appuntamento con Fabio" con la foto del titolare: si sa con chi si parla; pagina "Le nostre realizzazioni" | foto generiche di repertorio (metro da sarta, pollice alzato) con slogan generici; un video YouTube come apertura; consenso privacy ancora sul D.Lgs. 196/2003, lo stesso difetto del sito di Zoccarato | `c6-zoccarato-giannino-1440.png`, `c6-zoccarato-giannino-390.png` |
| 6 | [LASA Serramenti](https://www.lasaserramenti.it/) | sede in Villanova di Camposampiero (PD) per aziende.it, showroom a Noale (VE) | costruzione e montaggio serramenti | non valutabile: a 1440 la pagina è arrivata scomposta (scrollWidth 1872 su 1440), alla seconda visita il server ci ha bloccati con un captcha BitNinja | | `c4-lasa-1440.png`, `c4-lasa-390.png` |

**Cosa fanno i migliori:** foto vere del laboratorio e delle persone (Reale); il preventivo guidato, che dice al cliente quali misure prendere (Reale); il telefono a portata di pollice sul telefono (Longato); i prodotti fotografati come oggetti, uno per famiglia (Aloox); un nome e una faccia per l'appuntamento (Zoccarato Giannino).

**Cosa non fa nessuno (spazio per Zoccarato):**
1. il lavoro per l'industria: nessuno dei concorrenti visti mostra pensiline commerciali, monoblocchi prefabbricati o lavori per i distributori di carburante. Il sito attuale di Zoccarato ha una sezione intera "Lavorazioni per l'industria" e in "Chi siamo" scrive di aver collaborato "con le più note compagnie di distribuzione carburanti";
2. i mezzi propri: Zoccarato ha le foto della sua flotta (camion con gru e furgoni con le sponde blu e la scritta "ZOCCARATO", "Serramenti metallici", "Borgoricco (PD) - Brebbia (VA)"). Nessuno dei concorrenti visti mostra come arriva in cantiere;
3. l'intervento dopo un furto: "in caso di effrazioni e danni da furto assicura alla propria clientela un intervento in tempi rapidissimi e con l'assistenza di preventivazione per le compagnie assicurative" (Chi siamo). Nessuno dei concorrenti visti lo offre in modo visibile;
4. realizzazioni vere e tante: il sito attuale ha circa 180 foto di lavori e dell'azienda (1000x750, 750x1000, 1000x600 px), divise per tipo. I concorrenti visti usano foto da studio, foto generiche o una sola foto di laboratorio;
5. due sedi: Borgoricco e l'unità locale di Brebbia (VA); "Chi siamo" scrive che l'unità locale nella zona di Varese è stata aperta nel 1997. Nessuno dei concorrenti visti dichiara una sede in provincia di Varese.

**Attenzione al nome.** zoccaratoserramenti.com è di un'altra impresa (Zoccarato Giannino, PVC, Fagnano Olona) nella stessa provincia dell'unità locale di Brebbia. Il nuovo sito deve dire "alluminio" e "Borgoricco (PD) e Brebbia (VA)" già nel titolo della pagina e nella testata, come fanno i camion.

**Attenzione al colore.** Longato, il più grande fra i concorrenti trovati (fascia di fatturato F5 su aziende.it), usa un blu (#1972B9 misurato sul pulsante "Contattaci") molto vicino al blu di Zoccarato (#006BAC, dal foglio di stile attuale e dal logo). Il blu da solo non distingue: deve farlo il carattere tipografico, la flotta e i lavori per l'industria.

**Posizionamento proposto** (solo fatti presenti sul sito attuale): "Serramenti in alluminio, portoncini, oscuranti e pensiline. Per privati e per l'industria, da Borgoricco (PD) e Brebbia (VA). Dal 1974." Contro Longato (più grande, PVC e alluminio, catalogo) Zoccarato non compete sul catalogo ma sui lavori veri, sull'industria e sui mezzi propri; contro i rivenditori-installatori (L'infisso) è il costruttore; contro l'omonimo varesino è l'alluminio.

**Copy da evitare** (visto nei concorrenti): slogan sul "design che sfida il tempo", gli aggettivi senza prova, le percentuali di qualità, i riquadri con icone per servizi ovvi, i contatori di anni che invecchiano (il sito attuale scrive "esperienza quarantennale" ed "Ecobonus 2015": si scrive "dal 1974" e si toglie l'anno dalle agevolazioni).

Caratteri usati dai concorrenti, da non ripetere: Hind (Longato), Assistant, Raleway, Rubik e Open Sans (Reale), Inter (Aloox), Overpass e Poppins (LASA), Titillium Web e Montserrat (L'infisso), Catamaran (Zoccarato Giannino). Il sito attuale di Zoccarato chiede Open Sans in http e il browser lo blocca.

## 2. Riferimenti premium

Zoccarato è un costruttore di serramenti in metallo (ATECO 25.12.1) nato nel 1974 dalla lavorazione del ferro e passato all'alluminio nel 1982, con lavori per le case e per l'industria. I riferimenti giusti sono costruttori di serramenti e aziende di sistemi in alluminio e metallo con siti di livello alto, italiani dove possibile, non marchi di moda. Ne ho provati sedici: dodici si sono aperti con il loro contenuto, ne tengo otto. Hanno tutti alcune cose in comune: un solo carattere senza grazie, il prodotto o il lavoro finito come immagine principale, interfaccia piccola, nessuna decorazione, nomi dei prodotti scritti in chiaro.

### 2.1 Schüco Italia, [schueco.com/it](https://www.schueco.com/it/)
Sistemi in alluminio per finestre, porte e facciate; la filiale italiana ha sede a Padova (lo dice la home). Carattere Univers, nero e bianco, grigio chiaro per le fasce.
- **Cosa si riprende:** (a) la fascia grigia "seleziona la tua area" con quattro tessere bianche (Privati, Progettisti, Serramentisti, Investitori), che a 390 diventano quattro righe a tutta larghezza: per Zoccarato due porte, "Per privati" e "Per l'industria", la stessa separazione del menu attuale, subito sotto l'apertura; (b) i progetti con le etichette che dicono tipo di edificio e prodotto ("Casa privata", "Nuova costruzione", "Finestre", "Porte") e il contatore "01 / 05" con un filetto lungo: per Zoccarato ogni lavoro porta l'etichetta della sua categoria e del prodotto.
- **Cosa evitare:** le etichette su fondo traslucido sfocato (è glassmorphism, vietato); il testo di presentazione lungo e aziendale; l'apertura vuota quando il video non parte (nella nostra cattura è rimasta bianca sia a 1440 sia a 390).
- **Ritagli:** `schueco-scegli-area.jpg`, `schueco-390-apertura.jpg`, `schueco-griglia-prodotti.jpg`, `schueco-progetti-etichette.jpg`.

### 2.2 Reynaers Aluminium, [reynaers.it](https://www.reynaers.it/)
Sistemi in alluminio. Titoli in Faktum Wide (un grottesco largo) e testo in Faktum, blu notte #003C75 per titoli e fasce, testo quasi nero tendente al blu (#051939). È il precedente più vicino a quello che serve a Zoccarato: un'identità blu, con lettere larghe, in un'azienda di alluminio.
- **Cosa si riprende:** il titolo largo con la sola iniziale maiuscola, non urlato; la fascia piena blu notte che separa un pubblico dall'altro (lì "Architetti / Serramentisti", qui "Per l'industria"); la foto di due posatori che montano una finestra, cioè il lavoro in cantiere al posto della foto patinata.
- **Cosa evitare:** le icone dei prodotti dentro quadrati blu; i pulsanti a pillola; a 390 la barra della nazione e il banner dei cookie uno sopra l'altro coprono l'apertura.
- **Ritagli:** `reynaers-prodotti-e-titolo-largo.jpg`, `reynaers-fascia-blu-pubblici.jpg`.

### 2.3 Secco Sistemi, [seccosistemi.com](https://www.seccosistemi.com/it/)
Serramenti e sistemi in acciaio, ottone e corten, Preganziol (TV), fondata nel 1947 ([Wikipedia](https://en.wikipedia.org/wiki/Secco_Sistemi)). Il sito ha una protezione anti-robot: la versione desktop si è aperta solo con lo user agent di Safari.
- **Cosa si riprende:** la "bacheca" delle realizzazioni: foto nelle loro proporzioni (orizzontali e verticali mescolate), sfalsate su due colonne con molto bianco, sotto ognuna una parola piccola ("realizzazione") e il nome. Nessuna scritta sopra la foto. A 390 una colonna sola, stesso ordine. È il modo giusto per le foto di Zoccarato, che sono 1000x750 e 750x1000 e non reggono la larghezza piena: in bacheca stanno fra 450 e 600 px.
- **Cosa evitare:** i riquadri di Instagram con testo lungo mescolati ai lavori; la testata ridotta a "cerca / lista breve", che nasconde il menu (un privato non capisce dove andare).
- **Ritagli:** `secco-bacheca-realizzazioni.jpg`, `secco-390-bacheca.jpg`.

### 2.4 Capoferri, [capoferri.it](https://www.capoferri.it/)
Serramenti speciali in legno, bronzo e acciaio, Adrara San Martino (BG), dal 1894, impresa di famiglia nata come falegnameria ([The Plan](https://www.theplan.it/eng/design/storia-tradizione-e-versatilita)). Carattere Moderat, grigio caldo chiarissimo e nero. È la storia più vicina a quella di Zoccarato: un piccolo laboratorio di famiglia cresciuto un passo alla volta.
- **Cosa si riprende:** (a) il "cartellino": un riquadro bianco che morde l'angolo alto della foto di ogni progetto, con luogo, tipo ("Residenza privata") e progettista. Per Zoccarato: categoria e prodotto; il luogo solo dove l'azienda lo conferma [DA CONFERMARE]; (b) la scacchiera 50/50 che alterna foto e testo (Filosofia, Materiali, News): ogni foto è larga 720 px a 1440, sotto i 1000 px nativi delle foto di Zoccarato; (c) la fascia con un disegno tecnico in trasparenza dietro il testo, ma solo se Zoccarato fornisce un suo disegno (sezione di un profilo, un esecutivo di pensilina) [DA CONFERMARE]: non se ne disegna uno finto.
- **Cosa evitare:** i paragrafi lunghi in maiuscolo; "VIEW MORE" in inglese su un sito italiano; a 390 l'apertura è rimasta vuota nella nostra cattura.
- **Ritagli:** `capoferri-apertura-since.jpg`, `capoferri-fascia-disegno.jpg`, `capoferri-scacchiera.jpg`, `capoferri-cartellini-progetti.jpg`.

### 2.5 Sky-Frame, [sky-frame.com](https://www.sky-frame.com/)
Finestre scorrevoli senza telaio "sviluppate e prodotte in Svizzera" (dal sito). Testata nera sottile, Gotham maiuscolo.
- **Cosa si riprende:** le quattro schede prodotto: nome in maiuscolo, una riga che dice cos'è ("Finestre scorrevoli senza telaio", "Porta-finestra"), freccia in basso a destra, tutta la scheda è un link; a 390 diventano schede a tutta larghezza con lo stesso testo. Per Zoccarato: Finestre e abitazioni, Scorrevoli, Portoncini, Oscuranti, ciascuna con una riga presa dal sito attuale. Poi il blocco "Consulenza preliminare": la foto di una persona vera, due righe, un solo pulsante. Per Zoccarato: il sopralluogo, con la foto di Sante e Maurizio [foto da fare].
- **Cosa evitare:** il video in apertura (nella nostra cattura mostrava "Player error"); il bordo obliquo dell'apertura; il pulsante arancione del consenso.
- **Ritagli:** `skyframe-schede-prodotto.jpg`, `skyframe-consulenza-persona.jpg`.

### 2.6 Vitrocsa, [vitrocsa.com](https://www.vitrocsa.com/)
Finestre minimali svizzere ("Swiss engineering", dal sito). Fondo nero, Helvetica Neue regolare grande per l'elenco dei sistemi.
- **Cosa si riprende:** l'elenco dei sistemi come righe grandi separate da filetti sottili (Sliding, Curved, Invisible Frame, Pivoting, Guillotine, Turnable Corner), la riga aperta mostra due righe di testo e due link piccoli, la foto accanto cambia. A 390 l'elenco resta e la foto va sotto la riga aperta. Per Zoccarato: le sette lavorazioni per privati del menu attuale (abitazioni, pensiline, porte interne, portoncini, scorrevoli, oscuranti, speciali residenziali) come righe, ognuna con il link alla sua pagina.
- **Cosa evitare:** il nero e oro da lusso, i pulsanti beige; il testo nascosto nella fisarmonica: da noi tutte le righe sono link visibili anche senza JavaScript.
- **Ritaglio:** `vitrocsa-elenco-sistemi.jpg`.

### 2.7 panoramah!, [panoramah.com](https://www.panoramah.com/)
Finestre minimali in alluminio; nel piè di pagina c'è una sede a Ginevra. Titoli nel colore del marchio, in minuscolo, carattere geometrico (Chalet).
- **Cosa si riprende:** l'etichetta di sezione piccola nel colore del marchio seguita da un filetto lungo fino al margine ("what's new at panoramah!" e la linea); l'indice laterale a sinistra con i filetti sopra e sotto; i prodotti mostrati in sezione (spaccato del profilo), da usare solo se Zoccarato ha i disegni dei profili che monta [DA CONFERMARE].
- **Cosa evitare:** le parole ruotate in verticale sul bordo destro; i pulsanti rossi a pillola; i vuoti grandi fra una fila e l'altra (nella nostra cattura a 1440 quasi 300 px).
- **Ritagli:** `panoramah-indice-etichette.jpg`, `panoramah-spaccati-profilo.jpg`, `panoramah-reference-works.jpg`.

### 2.8 Oikos, [oikos.it](https://www.oikos.it/)
Porte d'ingresso, Oikos Venezia S.r.l., Gruaro (VE) (dal piè di pagina). Foto a tutta larghezza separate da fasce grigie, link piccoli in maiuscolo sottolineati.
- **Cosa si riprende:** la sezione "Arsenalità": una foto vera del laboratorio con le persone al lavoro, un titolo breve e un link. Per Zoccarato è il posto della foto della flotta (camion con gru davanti al capannone) e della foto storica in bianco e nero di un camion con una struttura in ferro, che ci sono già sul sito attuale.
- **Cosa evitare:** l'apertura con un'immagine che sembra un rendering; il testo bianco centrato sopra foto piene di dettagli (si legge male); l'indicatore "scroll".
- **Ritaglio:** `oikos-officina-arsenalita.jpg`.

### 2.9 Visti e scartati
- [Rimadesio](https://www.rimadesio.it/): sito molto curato ma linguaggio da arredamento e video di atmosfera. Si tiene un solo dettaglio per le porte interne: sotto il nome della famiglia l'elenco dei sottotipi ("Scorrevoli, scorrevoli a scomparsa, sistemi divisori, libro"). Ritaglio `rimadesio-collezione-sottotipi.jpg`.
- [Jansen](https://www.jansen.com/it/) (profili in acciaio, Oberriet): belle foto di verniciatura e saldatura, impaginazione aziendale generica.
- [Crittall](https://www.crittall-windows.co.uk/) (serramenti in acciaio dal 1849): utile solo il titolo dei casi ("Heritage-inspired self-build in St Albans by Metwin": luogo, tipo, posatore), il resto è un tema con pulsanti arancioni e icone.
- [Gibus](https://www.gibus.com/it) (pergole e tende da sole): pagina dentro un contenitore che scorre, la cattura si ferma all'apertura.
- carminatiserramenti.com: il dominio oggi ospita un sito di scommesse, scartato.
- keller-minimalwindows.com e foa.it (non raggiungibili dal proxy), ernstschweizer.ch/it/ (404). La versione desktop di reynaers.it ha risposto 403 alla prima prova e si è aperta con lo user agent di Safari.

## 3. Cosa si riprende

Il materiale di Zoccarato decide più dei riferimenti: circa 180 foto vere a 1000 px (nessuna più grande, tranne le 5 della home a 1680x850 e le fasce 1680x188), le foto della flotta, una foto storica in bianco e nero, il logo blu con i quattro punti e "dal 1974" (solo in jpg 320x76: serve il vettoriale [DA CONFERMARE]). Quindi: foto mai oltre 1000 px di larghezza, a tutta larghezza solo le foto della home; niente stock, niente rendering.

| Parte del nuovo sito | Gesto | Da chi | Con cosa di Zoccarato |
|---|---|---|---|
| Barra in alto e testata | barra sottile scura con le due sedi e il telefono, testata bianca con logo e menu su una riga | Sky-Frame (testata nera sottile), i camion di Zoccarato ("Borgoricco (PD) - Brebbia (VA)") | Borgoricco (PD) · Brebbia (VA) · 049 5798194 |
| Apertura home | foto vera a tutta larghezza, titolo largo con l'iniziale maiuscola, una riga di testo | Reynaers (titolo largo), Oikos (foto del lavoro) | una delle 5 foto 1680x850 della home attuale; titolo dal posizionamento |
| Due porte | fascia grigia chiara con due tessere grandi, a 390 una sotto l'altra | Schüco ("seleziona la tua area") | "Per privati" e "Per l'industria", le due voci del menu attuale |
| Lavorazioni per privati | righe grandi separate da filetti, ogni riga un link, una foto accanto | Vitrocsa (elenco sistemi), Sky-Frame (nome più una riga che dice cos'è) | le sette voci del menu attuale con una foto per voce |
| Lavorazioni per l'industria | fascia piena blu notte, divisa in due: testo e foto | Reynaers (fascia per pubblico) | pensiline commerciali, commerciali e industriali, monoblocchi prefabbricati; la frase sulle compagnie di distribuzione carburanti senza nomi di marchi |
| Realizzazioni | bacheca sfalsata con le foto nelle loro proporzioni, etichetta piccola e nome sotto; cartellino bianco che morde la foto per i lavori in evidenza | Secco Sistemi (bacheca), Capoferri (cartellino), Schüco (etichette tipo e prodotto) | le foto attuali divise per categoria; il luogo solo se confermato |
| Chi siamo | scacchiera foto e testo per le date vere (1974, 1982, 1997); la foto della flotta come momento del laboratorio | Capoferri (scacchiera), Oikos (laboratorio) | testi della pagina "Chi siamo" attuale, foto storica in bianco e nero, foto della flotta |
| Effrazioni | un solo blocco: foto, due righe, telefono | Sky-Frame (consulenza preliminare) | il servizio "intervento immediato in caso di effrazioni" e il preventivo per le assicurazioni |
| Contatti e preventivo | modulo guidato: misure del vecchio serramento, tipo, intervento, foto allegata | Reale Infissi (concorrente) | oggi la pagina contatti non ha un modulo |
| Etichette di sezione | parola piccola nel blu del marchio con filetto lungo fino al margine | panoramah! | "lavorazioni per privati", "lavorazioni per l'industria", "realizzazioni" |

**Il gesto di ogni sezione cambia** (larghezza, fondo, asse): apertura a tutta larghezza su foto; due porte su grigio chiaro; elenco a righe su bianco con foto a destra; fascia blu notte piena; bacheca sfalsata; scacchiera; blocco stretto per le effrazioni.

**Scartato:** lo slider automatico della home attuale (RoyalSlider); le aperture affidate a un video (Sky-Frame, Rimadesio) o a un contenuto che non carica (Schüco, vuota nella nostra cattura); le animazioni allo scorrimento (Reale); le icone nei riquadri (L'infisso, Reynaers); le etichette sfocate (Schüco); le parole ruotate (panoramah!); nero e oro (Vitrocsa); i rendering (Oikos); i riquadri social mescolati ai lavori (Secco); il testo bianco centrato su foto piene.

## 4. Accoppiate

Regole: solo Google Fonts, una famiglia per accoppiata, niente Inter, nessun serif. Nessuno degli otto riferimenti usa un serif o un corsivo: Schüco Univers, Reynaers Faktum e Faktum Wide, Capoferri Moderat, Secco Soho, Sky-Frame Gotham, Vitrocsa Helvetica Neue, panoramah! Chalet, Oikos Poppins. Un serif qui sarebbe un'abitudine, non una scelta del settore. Le tre accoppiate sono provate con testi e foto veri di Zoccarato in `_prova/ricerca/campione-accoppiate-1440.png`. Contrasti calcolati con la formula WCAG 2.

### A. "Flotta": Archivo largo e Archivo normale (proposta principale)
- **Caratteri:** [Archivo](https://fonts.google.com/specimen/Archivo) variabile (larghezza 62-125, peso 100-900). Titoli a larghezza 125, peso 600, con la sola iniziale maiuscola, interlinea 1,05; testo a larghezza 100, peso 400, 17-18 px; cartellini, etichette e numeri a larghezza 100, peso 600, maiuscolo 12-13 px con spaziatura 0,07 em. Una famiglia sola, due larghezze.
- **Perché:** Reynaers fa esattamente questo (Faktum Wide per i titoli, Faktum per il testo, blu notte); Schüco usa Univers, un grottesco nato come famiglia di larghezze; Capoferri usa Moderat, largo e asciutto. E soprattutto i camion di Zoccarato: "ZOCCARATO" in lettere larghe e piene, "SERRAMENTI METALLICI" in maiuscolo spaziato sopra (ritaglio `zoccarato-camion-scritte.jpg`). Il largo parla con il logo e con la flotta; il normale tiene il testo leggibile. Nessun concorrente lo usa. È anche lontano da Benvegnù (lì stretto e tutto maiuscolo, qui largo e con l'iniziale maiuscola).
- **Palette:**

| Ruolo | Colore | Uso | Contrasto |
|---|---|---|---|
| Blu Zoccarato | #006BAC | link, etichette, voce attiva, pulsanti pieni (dal foglio di stile attuale, uguale al logo e ai camion) | 5,68:1 su bianco; bianco su blu 5,68:1; 4,96:1 su #EDF0F2 |
| Blu notte | #0D2B4A | fascia "Per l'industria", barra in alto, piè di pagina | bianco 14,37:1; #B8C7D6 8,33:1; link #8CC4F0 7,71:1 |
| Inchiostro | #14202B | titoli e testo | 16,52:1 su bianco; 14,43:1 su #EDF0F2 |
| Secondario | #4D5A66 | didascalie, etichette dei lavori | 7,07:1 su bianco; 6,18:1 su #EDF0F2 |
| Grigio alluminio | #EDF0F2 | fasce chiare (due porte, modulo) | fondo |
| Filetto | #C5CED6 | filetti e bordi, mai per testo | 1,59:1 (solo decorativo) |
| Hover pulsante | #00527F | colore pieno all'hover, mai opacità | bianco 8,36:1 |

- **Rischi:** a 390 il titolo largo va portato a 32-34 px per non fare righe di due parole; "Borgoricco" e "prefabbricati" vanno provati a 390 per non sbordare.

### B. "Antracite": Hanken Grotesk leggero
- **Caratteri:** [Hanken Grotesk](https://fonts.google.com/specimen/Hanken+Grotesk). Titoli e righe dell'elenco peso 300-400, grandi (48-54 px), con la sola iniziale maiuscola; testo peso 400, 17 px.
- **Perché:** Vitrocsa (Helvetica Neue regolare grande sul nero per l'elenco dei sistemi), Sky-Frame (testata nera, nomi dei prodotti chiari), Oikos (fasce grigie fra le foto). È il colore dei profili: antracite e alluminio.
- **Palette:** antracite #24292D per le fasce scure (bianco 14,68:1, testo secondario #C2C9CF 8,78:1, link azzurro #79B8EA 6,89:1); bianco; testo #1B1F22 (16,59:1 su bianco, 15,07:1 su #F3F4F5); secondario #555E66 (6,61:1); alluminio #D3D8DC per i filetti (su di esso l'antracite fa 10,23:1); il blu #006BAC solo per link e stato attivo sul chiaro (5,68:1).
- **Rischi:** si allontana dal blu, che è l'unico patrimonio visivo dell'azienda (logo, camion); le foto di Zoccarato sono luminose e amatoriali e accanto a tanto scuro sembrano più povere; un tono da "lusso minimale" che non è quello dell'azienda. Da usare al massimo per una fascia.

### C. "Etichetta": Albert Sans in blu
- **Caratteri:** [Albert Sans](https://fonts.google.com/specimen/Albert+Sans), geometrico. Titoli peso 500 con la parte importante in 700, tutto in minuscolo come panoramah!, nel blu del marchio; testo peso 400, 18 px; etichette di sezione in minuscolo 14 px con filetto.
- **Perché:** panoramah! (titoli minuscoli nel colore del marchio, carattere geometrico, etichette con filetto), Secco Sistemi (etichette piccole in minuscolo sopra i nomi), Sky-Frame (Gotham, geometrico). Le lettere tonde di "serramenti" nel logo sono geometriche.
- **Palette:** bianco; blu Zoccarato #006BAC per i titoli (5,68:1 su bianco, 5,24:1 su #F4F6F7); inchiostro #1C2630 per il testo (15,34:1); secondario #5A6670 (5,88:1); grigio #F4F6F7 per le fasce; filetto #1C2630; hover #004F80 (bianco 8,64:1).
- **Rischi:** il più gentile dei tre, meno industriale: regge le case, meno le pensiline e i monoblocchi; titoli tutti blu diventano monotoni; somiglia a panoramah! se si prende anche il resto.

### Indicazione per la fase 2.3
Base **A**, con due innesti: da **C** le etichette di sezione in minuscolo con filetto lungo e la bacheca delle realizzazioni; da **B** nessun colore, solo l'elenco a righe grandi (su bianco, non su antracite). Foto: i colori come sono, nessun viraggio; il bianco e nero resta solo dove è già nell'originale (la foto storica). I quattro punti del logo, se servono, come unico segno grafico (voce attiva del menu o separatore), mai ripetuti come decorazione.
