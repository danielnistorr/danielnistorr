# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Tutti i siti sono stati aperti con Playwright (Chromium, attraverso il proxy) a 1440 e a 390 px e guardati a pezzi. In `_prova/ricerca/` ci sono gli screenshot interi (`00-vescovi-*` il sito attuale, `c*-` i concorrenti, `r-*` i siti provati come riferimento, `*-top.png` il primo schermo, `*-info.json` caratteri e colori letti dal browser), in `_prova/ricerca/ritagli/` i 29 pezzi da riprendere (numerati e citati qui sotto), in `_prova/ricerca/accoppiate-prova.png` la prova delle tre accoppiate con testi e foto veri dell'albergo.

Siti visitati: 6 concorrenti dell'Altopiano più 2 non raggiungibili, 22 siti di alberghi alpini provati come riferimento, 8 tenuti. Limiti da sapere prima di riaprirli:
- il proxy ha restituito una volta "upstream request failed" (Paradiso e Waldhaus a 390): rifatti, i tentativi falliti sono in `x-*-proxy-fallito.png`;
- molti alberghi aprono con un video (Waldhaus, Krone, Rote Wand, Meltar, Erica): il Chromium di prova non lo riproduce e l'apertura esce grigia o bianca. Si giudica il resto della pagina;
- i siti con animazioni allo scorrimento escono bianchi nella cattura a pagina intera: sono stati fotografati una schermata alla volta e cuciti (`_prova/script/passi.cjs` e `cuci.py`); nei pezzi cuciti la testata fissa si ripete ogni 900 px;
- Hotel Vecchia Stazione (Roana) è dietro una verifica Cloudflare; `asiagosportinghotel.it` e `.com` sono domini parcheggiati da GoDaddy (`x-sporting-*`), il sito ufficiale dell'Asiago Sporting Hotel non è stato trovato; Ciasa Salares esce vuota a 1440.

Albergo Vescovi in breve, per il confronto (dal sito attuale, dettagli in 01): "moderno hotel di tre stelle" in Via Don Viero 80, "a 900 metri dal centro di Asiago immerso nel verde della piana Ave"; camere doppie (16 m²), triple e quadruple, "alcune con balcone", mansardate con travi a vista o classiche con parquet; centro benessere con "sauna finlandese all'eucalipto, bagno turco di vapore, vasca idromassaggio, zona relax, docce emozionali, tisaneria e frutta fresca", su prenotazione "dalle ore 15:00 fino alle 19:00" con "€ 10 di supplemento che comprende accappatoio e ciabatte in spugna"; "cucina tradizionale"; garage e parcheggio privato; "aperto stagionalmente o su prenotazione anche in altri periodi dell'anno". Prenotazioni con il motore Persefone (barra date in home, due script: `phpbookinghotel.it/4055-vescovi/...` e `widget.booking-engine.it/maschera.php?hotel_id=53...`). Materiale (inventario in 01): le foto del sito arrivano a 1024 x 768 (camere, 2018) e 800 x 600 (piatti), mentre la scheda Booking.com ha un servizio professionale di 31 scatti a 3000 x 1996 (camere rinnovate in abete chiaro e pietra, stube con la stufa, sala, reception in legno, sauna, facciata, prati della Piana) [DA CONFERMARE che siano del cliente]. I loghi sono due: il gotico della testata e uno tondo con il profilo di un monte, verde bosco #293F1C e oliva #727949 [DA CONFERMARE quale è ufficiale].

## 1. Concorrenti

Concorrenti diretti: alberghi dell'Altopiano dei Sette Comuni con centro benessere e ristorante, quelli che un ospite confronta su un portale prima di scegliere. La categoria è quella mostrata nel logo o nel titolo di ciascun sito.

| # | Concorrente | Dove | Categoria, motore | Fa meglio di Vescovi | Fa peggio di Vescovi | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Hotel Paradiso](https://www.hotelparadisoasiago.it/) | Via Monte Valbella 33, Asiago | 3 stelle S, "Wellness & Family Hotel"; motore su `booking.hotelparadisoasiago.it` | il concorrente più simile: famiglia (i Rigoni, radici "sin dai primi anni del '900"), benessere, cucina. Racconta la storia; nomina i piatti ("polenta con i funghi", "tosela", "strudel di mele", "marmellate fatte in casa"); menu diviso in Soggiornare, Gusto, Benessere, Vivere; tre lingue | a 1440 c'è solo l'hamburger e la pagina è più larga della finestra (scrollWidth 1780, poi 7020: il menu laterale `nav.bauen-menu` resta fuori schermo); testo in Didact Gothic 16 px grigio #777777 su bianco, 4,48:1, sotto la soglia; Oswald maiuscolo spaziato; slogan generici | `c7-paradiso-*` |
| 2 | [Relax Hotel Erica](https://www.relaxhotelasiago.it/) | Via Garibaldi 55, Asiago (centro) | categoria non scritta in home; Ericsoft | "400 mq di benessere naturale"; "da oltre 70 anni"; usa il nome cimbro di Asiago ("Sléghe"); a 390 una barra fissa Chiama, Prenota, Mappa; mappa e modulo in home | l'apertura è un video: nel browser di prova è rimasta vuota e il logo e il menu, bianchi, spariscono sul fondo crema #EFE9E3; crema e Crimson Pro, il cliché "di lusso"; una formula della lista `PAROLE_VIETATE` nel testo del benessere; bolla WhatsApp sopra il testo | `c1-erica-*` |
| 3 | [Linta Hotel Wellness & Spa](https://lintahotelwellness.it/) | Asiago | 4 stelle S, gruppo BLU Hotels; BookingExpert | "103 camere", "centro benessere di 2.000 mq", piscina esterna panoramica ("novità 2025"), ristorante panoramico; grandi foto vere della stessa Piana che si vede da Vescovi | due banner cookie insieme (BLU Hotels e NextRoll): a 390 coprono lo schermo (844 px e 465 px) e la pagina scorre di lato (scrollWidth 724 su 390); pulsanti azzurro petrolio tutti uguali; testi da depliant ("vista mozzafiato", "Lasciati incantare") | `c3-linta-*` |
| 4 | [Meltar Boutique Hotel](https://www.meltarhotel.com/it/) | nel Golf Club Asiago | 4 stelle S; Beddy | storia del luogo ("un'antica casa colonica cimbra"); barra date sempre visibile in basso; foto professionali | titolo d'apertura in inglese su pagina italiana ("The secret is out / Listen to the silence"); finestra "Autumn Yoga Retreat" in inglese che a 390 copre l'apertura; sezioni che scorrono di lato e nascondono il contenuto; Cormorant e color tortora, il "lusso" di serie | `c6-meltar-*` |
| 5 | [Hotel Da Barba](https://www.dabarba.it/it/) | "a 2 minuti d'auto dal centro di Asiago" | 3 stelle Superior, B&B; Ericsoft | un pubblico chiaro (famiglie, "Villaggio degli Gnomi"); pagina prezzi e offerte; collegamento a TripAdvisor | in home "La tua casa in montagna ora è chiusa per ristrutturazione: Ti aspettiamo da giugno 2027"; stile datato: pulsanti verdi a pillola, icone colorate, carosello a 15 punti, corsivi Georgia | `c4-dabarba-*` |
| 6 | [Kleos Hotel Gaarten](https://www.hotelgaarten.com/) | Via Kanotole 13/15, Gallio (VI) | 4 stelle (nel manifesto); Wix, BookingExpert | P.IVA, indirizzo, telefono ed email in fondo a ogni pagina; WhatsApp | la home è una finestra di iscrizione alla newsletter sopra una foto di camera; manifesto "Ci stiamo rifacendo il look", "la piscina sarà disponibile da dicembre"; banner cookie in inglese | `c5-gaarten-*` |

Non raggiungibili: Hotel Vecchia Stazione a Roana (verifica Cloudflare), Asiago Sporting Hotel & Spa (domini parcheggiati).

Caratteri dei concorrenti, letti dal browser: Playfair Display (Linta, Gaarten, e anche Vescovi lo carica), Crimson Pro e Josefin Sans (Erica), Cormorant e Cormorant Garamond (Meltar), Oswald e Didact Gothic (Paradiso), Ubuntu e Georgia (Da Barba). Vescovi oggi mescola Cabin, Roboto Condensed, Ubuntu, Open Sans e Roboto. Le accoppiate del paragrafo 4 non usano nessuno di questi.

**Cosa fa già bene Vescovi** (da tenere):
- le informazioni sul benessere sono le più precise dell'Altopiano: orario (dalle 15:00 alle 19:00, su prenotazione), prezzo (€ 10 con accappatoio e ciabatte), elenco dei servizi, perfino il "Bucket Shower di origine tirolese". Nessuna home dei concorrenti visti dà orario e prezzo della spa;
- la barra date di Persefone è già in home: chi arriva può cercare la disponibilità subito, come da Meltar;
- la posizione è detta con un numero (900 metri dal centro) e un luogo (la Piana Ave), non con un aggettivo;
- la scheda della doppia ha la superficie (16 m²) e l'elenco dei servizi in camera;
- da telefono la pagina regge: niente finestre sopra l'apertura, barra Prenota fissa in basso.

**Cosa fa peggio di tutti** (da `00-vescovi-*`, misure in 01): l'avviso PHP in cima a ogni pagina, a 1440 e a 390; "Etichetta del pulsante nella Testata:PRENOTA" e, nella pagina Ristorante, "Sono un blocco di testo... Lorem ipsum"; foto delle camere al massimo 1024 x 768 del 2017 e 2018, mentre la scheda Booking.com ha 31 foto professionali che il sito non usa; pulsante PRENOTA verde #4CAF50 con testo bianco a 2,78:1; "45 camere" contro le 24 del registro regionale [DA CONFERMARE].

**Cosa non fa bene nessuno (spazio per Vescovi):**
1. dire quando si è aperti: Vescovi è "aperto stagionalmente", ma nessuna home dei concorrenti visti scrive le date della stagione estiva e invernale, l'ora di arrivo e partenza, l'orario della cena. I riferimenti migliori lo fanno (Waldhaus, Schwanen, Tannerhof). Date e orari [DA CONFERMARE];
2. un primo schermo pulito da telefono: Linta, Meltar, Gaarten ed Erica lo coprono con banner, finestre o un video che non parte;
3. un tre stelle detto con onestà: i concorrenti vendono "lusso", "boutique", "wellness & spa". Vescovi può essere l'albergo di famiglia preciso: camere con balcone sui prati, sauna nel pomeriggio, cucina di casa, garage;
4. la Piana Ave: Linta la fotografa, nessuno la usa come segno del sito (un profilo dell'orizzonte, una mappa).

**Copy da non usare** (visto nei concorrenti): le formule già nella lista `PAROLE_VIETATE` di `build.py`, più "vista mozzafiato", "Lasciati incantare", "luogo da Fiaba", "piccolo gioiello di ospitalità", "rifugio esclusivo", "relax al 100%", "miglior tariffa garantita", titoli in inglese. Si scrivono i fatti del sito attuale: metri, orari, prezzi, servizi.

**Posizionamento proposto:** "Albergo a tre stelle ad Asiago, a 900 metri dal centro nella Piana Ave. Camere con balcone sui prati, sauna e bagno turco nel pomeriggio, cucina tradizionale." Contro Linta e Meltar (grandi o di lusso) Vescovi non compete sui metri quadri della spa ma sulla calma e sul prezzo da tre stelle; contro Paradiso (stessa categoria, famiglia, benessere) sulla posizione nel verde e sulla chiarezza delle informazioni.

## 2. Riferimenti premium

Vescovi è un albergo di famiglia di montagna con ristorante e una piccola spa. Il riferimento giusto non sono i resort né le catene, ma gli alberghi alpini di famiglia, con ristorante e sauna, che hanno i siti migliori del settore: Engadina, Alto Adige, Bregenzerwald, Baviera. Hanno quasi tutti le stesse caratteristiche, misurate dal browser: fondo bianco (solo Tannerhof usa il crema), un solo colore della casa usato su pulsanti e titoli, per i titoli un carattere con grazie diritto (cinque su otto, mai in corsivo) oppure un senza grazie (Krone, Schwanen, Berghotel), un senza grazie per le informazioni, foto vere di camere, piatti e paesaggio, informazioni pratiche scritte per intero (stagioni, orari, metri quadri, prezzi "da").

| # | Riferimento | Cos'è | Caratteri e colori (dal browser) | Ritagli |
|---|---|---|---|---|
| 1 | [Waldhaus Sils](https://www.waldhaus-sils.ch/) | albergo storico a Sils-Maria (Engadina), "A family affair since 1908", aperto per stagioni | Larken (titoli in maiuscolo) e Inter; verde #1E5E42 su bianco, pulsanti a pillola | `01`-`05` |
| 2 | [Berghotel Sexten](https://www.berghotel.com/it/) | 4 stelle S a Sesto (BZ), "Il Berghotel a Sesto con la Meridiana di Sesto" | Exo e Open Sans; verde #065544 su bianco | `06`-`09` |
| 3 | [Zirmerhof](https://www.zirmerhof.com/it/) | "Albergo storico" a Redagno (BZ), "a 1.560 m di altitudine", famiglia Perwanger, ristorante e maso | Bembo e Raleway; ocra #865300, bruno #48310C, fasce #F3F0ED | `10`-`13`, `27` |
| 4 | [Tannerhof](https://natur-hotel-tannerhof.de/de) | albergo a Bayrischzell (Baviera), "Seit 1905. Vier Generationen" | Galliard e Gotham Narrow; fondo #FCF8F2, pulsanti neri | `14`-`17`, `29` |
| 5 | [Krone Hittisau](https://www.krone-hittisau.at/) | albergo e ristorante nel Bregenzerwald, "seit 1838 am Dorfplatz von Hittisau", con casa della sauna | Roboto Condensed; bordeaux #630F0E solo sul pulsante Anfrage / Buchen | `18`-`19` |
| 6 | [Biohotel Schwanen](https://biohotel-schwanen.com/) | albergo con ristorante a Bizau (Bregenzerwald) | Interstate Condensed e Minion Bold Condensed; verde #77AF53 nei contorni | `20`-`22` |
| 7 | [Schgaguler](https://www.schgaguler.com/) | albergo a Castelrotto (BZ) | Canela e Maison Neue; grigi chiari | `23`-`24`, `28` |
| 8 | [Muottas Muragl](https://www.muottasmuragl.ch/de) | Romantik Hotel in Engadina sopra St. Moritz, "auf 2'456 Metern", raggiunto da una funicolare del 1907 | nyght Serif e Roboto Condensed; grigio azzurro | `25`-`26` |

## 3. Cosa si riprende

Per ognuno: il gesto preciso, dove andrebbe nel sito di Vescovi, cosa non si prende. Si prende l'idea, non il disegno.

### 3.1 Waldhaus Sils
- **Gesto: le camere a fisarmonica** (`ritagli/02`). Il titolo "ZIMMER" grande in maiuscolo, sotto un elenco di tipi separati da filetti: quello aperto mostra due righe di testo, gli altri solo il nome; accanto una sola foto grande, sotto un pulsante verde. Per Vescovi i tipi sono esattamente tre: Doppia (16 m²), Tripla, Quadrupla [superfici di tripla e quadrupla DA CONFERMARE]. In Elementor gratuito è il widget Accordion; la foto accanto resta una sola (la migliore), a telefono va sotto l'elenco.
- **Le sale del ristorante in fila** (`03`): foto verticali, sopra il titolo un'etichetta piccola in maiuscolo ("Gediegen", "Lieblingsort"), sotto il nome della sala e una riga. Per Vescovi: la fila dei piatti dalla cucina (le foto 800 x 600 del sito attuale), etichetta "Primo", "Antipasto", nome del piatto [nomi DA CONFERMARE con la cucina].
- **Le stagioni nel piede** (`04`): "Sommersaison 11.06.2026 - 25.10.2026", "Wintersaison 11.12.2026 - 04.04.2027", in verde, accanto all'indirizzo. Per Vescovi è la risposta più utile a "aperto stagionalmente" [date DA CONFERMARE].
- **Testata e telefono** (`01`, `05`): voci di menu in testo piccolo a sinistra, nome al centro, a destra la stagione e "Buchen" in una pillola verde; da telefono due pillole fisse in basso, il numero e "Buchen". Per Vescovi: 0424 462614 e Prenota (Persefone).
- **Evitare**: l'apertura a video (Vescovi non ha video e il video pesa), le scritte verticali "MENU" e "KONTAKT" sui bordi, la spa da 1500 m² come misura del racconto.

### 3.2 Berghotel Sexten
- **Gesto: il profilo delle cime numerate** (`06`). Una linea verde disegna l'orizzonte e i numeri 8, 9, 10, 11, 12, 1 stanno sopra le cime della Meridiana di Sesto: il paesaggio diventa il segno del sito, senza foto. Per Vescovi: il profilo dell'orizzonte visto dal balcone sulla Piana Ave ("dal balcone esterno è possibile godere di un'ottima vista del paese di Asiago e la piana ave"), disegnato in SVG a un colore da una foto vera (il panorama della Piana con l'albergo, `assets/originali/panorama-piana-ave-hotel.jpg`, 2000 x 600, o i prati della Piana del servizio Booking) e messo sopra il piede. Il logo tondo ha già il profilo di un monte: la linea lo prolunga. I nomi delle cime solo se confermati [DA CONFERMARE, serve la foto dal balcone].
- **La barra date con una domanda** (`07`): "Quando vi prendete il tempo?", due date, "avanti", su una fascia verde. Per Vescovi la barra di Persefone c'è già: le si dà un titolo semplice e i colori del sito (lo script accetta `sfondo`, `testo`, `pulsante`, `testopulsante` nell'indirizzo, già usati oggi).
- **La giornata a orari** (`08`, a telefono `09`): una linea con i punti "ore 07:30", "ore 10:00", "ore 17:00"; a telefono si scorre con frecce. Per Vescovi solo con orari veri: benessere dalle 15:00 alle 19:00 (dal sito); colazione e cena [DA CONFERMARE].
- **Evitare**: la colonna di linguette verticali a destra (Verificare disponibilità, Last Minute, Buono regalo, Webcam, Top Impressions) che a 390 copre il testo; la home di 27.000 px; i "big 5" numerati.

### 3.3 Zirmerhof
- **Gesto: il collage di foto piccole** (`10`). Sei foto di misure diverse, sparse su fondo bianco, alcune appoggiate su rettangoli grigi, ognuna mostrata piccola. È la soluzione giusta per le foto del sito attuale, che arrivano al massimo a 1024 x 768 (piatti 800 x 600): ogni foto resta sotto la sua misura nativa e insieme raccontano camera, bagno, sauna, piatti e paese. Per Elementor: griglia con foto di larghezze diverse, senza sovrapposizioni, che a telefono diventa due colonne.
- **La cuoca con il nome** (`11`): "Piatti della cuoca Hanna Perwanger". Il sito di Vescovi dice "I nostri piatti sono preparati con amore dal nostro chef": il nome di chi cucina rende vera la frase [DA CONFERMARE].
- **Il panorama inciso sopra il piede** (`12`): alternativa più ricca al profilo di Berghotel; se ne usa uno solo.
- **Le offerte con il prezzo "da"** (`13`): foto, titolo, "da 495,00 € a persona", Prenota e Richiedi. Per Vescovi solo se l'albergo fornisce offerte e prezzi [DA CONFERMARE]; oggi l'unico prezzo pubblico è il supplemento spa di € 10.
- **A telefono** (`27`): barra fissa divisa a metà, "RICHIESTA" e "PRENOTARE".
- **Evitare**: l'insieme beige, ocra e Bembo (il più vicino al cliché crema e serif), la colonna di icone sul bordo destro, lo slogan "l'originale da oltre 900 anni".

### 3.4 Tannerhof
- **Gesto: estate e inverno nella testata** (`14`): un interruttore con sole e fiocco di neve accanto alla lingua. Lo usano anche Waldhaus ("Sommer") e Berghotel. Asiago vive di due stagioni e l'unica foto di paesaggio del sito attuale è d'inverno. Per Vescovi conviene la versione più semplice di Muottas Muragl (3.8): l'interruttore dentro la sezione su Asiago, non in testata.
- **La striscia check-in e check-out** (`17`): una riga nera sopra il piede, "Check-in: ab 15 Uhr | Check-out: bis 11 Uhr". Per Vescovi: arrivo, partenza e orario della spa nella stessa riga [arrivo e partenza DA CONFERMARE].
- **L'anno e la foto d'archivio** (`16`): "Seit 1905 und vier Generationen", una foto in bianco e nero, un pulsante "Geschichte erkunden". Per Vescovi c'è la "lunga tradizione alberghiera": anno di apertura e foto d'archivio solo se la famiglia li fornisce [DA CONFERMARE].
- **A telefono** (`29`): "Anfragen" e "Buchen" fissi in basso, uno vuoto e uno pieno.
- **Evitare**: il fondo crema con il Galliard, la bolla della chat che copre le foto, il collage con foto minuscole sparse su tutta la larghezza (`15`): Zirmerhof lo fa meglio.

### 3.5 Krone Hittisau
- **Gesto: il mosaico con le etichette-frase** (`19`). Foto grandi accostate con un margine sottile, ognuna con un'etichetta bianca a pillola in basso a sinistra: "Herrlich schlafen", "Essen gut, alles gut", "Dem Körper Raum geben" (la casa della sauna). È la navigazione della home fatta con le foto. Per Vescovi tre o quattro tessere verso Camere, Ristorante, Benessere, Asiago, con etichette che dicono un fatto: "Camere con balcone sulla Piana", "Cucina tradizionale", "Sauna all'eucalipto". Con le foto del servizio Booking (stube, camera in legno chiaro, sauna, albergo sul prato) le tessere possono essere grandi come da Krone [DA CONFERMARE l'uso delle foto]; con le sole foto 2018 restano piccole.
- **L'apertura** (`18`): il luogo ("Bregenzerwald"), tre parole, un paragrafo che dice dove sta l'albergo e da quando ("seit 1838 am Dorfplatz"). Per Vescovi: "Asiago, Piana Ave" e il paragrafo del sito attuale, corretto.
- **Il colore della casa solo sul pulsante**: il bordeaux #630F0E compare solo su "Anfrage / Buchen" (13,08:1 con il bianco).
- **Evitare**: Roboto Condensed su tutto, la bolla "Kronen-Langzeit-Glück", il video in apertura.

### 3.6 Biohotel Schwanen
- **Gesto: gli orari come titolo** (`20`, `21`). "ÖFFNUNGSZEITEN BIOHOTEL SCHWANEN: Geöffnet bis 8. November 2026 sowie ab 11. Dezember 2026", e per il ristorante giorni, orari della cucina, giorni di chiusura, scritti per intero accanto a una foto della sala. Per Vescovi: "Quando siamo aperti" (stagioni) e "Centro benessere: dalle 15:00 alle 19:00, su prenotazione, € 10" accanto alla foto della sauna; il ristorante solo se aperto anche a chi non dorme in albergo [DA CONFERMARE].
- **I contatti in fila** (`22`): telefono, email, richiesta, tre colonne con un'icona piccola e il testo in grassetto. Per Vescovi: 0424 462614, info@albergovescovi.com, Prenota.
- **Evitare**: i pulsanti a contorno verde #77AF53 (2,61:1 con il bianco), i riquadri neri dei video, gli slogan scherzosi.

### 3.7 Schgaguler
- **Gesto: la barra date sotto l'apertura** (`23`, a telefono `28`): tre caselle grigie Arrivo, Partenza, Persone e "Jetzt buchen", larghe quanto il testo, subito sotto la foto; a telefono si impilano. Per Vescovi è il posto della barra Persefone: sotto l'apertura, non sopra la foto.
- **La didascalia sotto la foto** (`24`): quattro foto in due colonne, titolo e tre righe centrate sotto ogni foto, nessuna scritta sopra l'immagine. Con foto vecchie e di qualità mista la didascalia sotto non ha bisogno di velature scure.
- **Evitare**: il Canela sottile bianco sopra le foto, il testo grigio #909090 su bianco (3,2:1), i loghi delle riviste di design.

### 3.8 Muottas Muragl
- **Gesto: estate e inverno dentro la sezione** (`26`): due bottoni "Sommer" e "Winter" sopra il titolo "Bergerlebnis Sommer erleben"; cambiano testo e foto solo lì. Per Vescovi: la sezione Asiago con due schede, Estate (prati, sentieri) e Inverno (neve, la foto del sito attuale). In Elementor gratuito è il widget Tabs, senza codice.
- **Le camere con i metri quadri davanti** (`25`): nome della camera e sotto "12 m² mit gemütlichem Charme", "16 m² mit privater Dachterrasse". Per Vescovi: "Doppia, 16 m², alcune con balcone" (dal sito attuale).
- **Evitare**: i titoli in due toni di grigio azzurro, la bolla della chat.

### 3.9 Considerati e scartati
Forestis (Bressanone): foto a coppie in una colonna stretta, bello ma da resort di lusso e quasi senza informazioni. Rote Wand (Lech): rosso del nome della montagna su titoli enormi, troppo forte per un tre stelle. Hirschen (Schwarzenberg): fondo nero e foto da rivista, è un'altra categoria. Theiner's Garten: parole d'accento in serif corsivo, esattamente il divieto. Pfösl, Bühelwirt, Hubertus: finestre e widget che coprono la pagina. Adler (Schwarzenberg): crema e serif, il cliché, anche se l'elenco delle categorie di camere è chiaro. Hotel Fex (Val Fex): orari di albergo, ristorante e chiosco chiari ma pagina debole. Paxmontana, Bellevue (Cogne), Post Bezau (solo in inglese): datati o generici. Hotel Menardi (Cortina): stessa categoria, tre stelle con benessere e regole della spa scritte, ma impaginato da modello.

### 3.10 Dove va cosa (proposta per la mappa in 03)

| Parte del sito | Gesto | Da |
|---|---|---|
| Testata | menu in testo, nome al centro, telefono e Prenota a pillola; a telefono Chiama e Prenota fissi in basso | Waldhaus `01` `05`, Zirmerhof `27`, Tannerhof `29` |
| Apertura | luogo e paragrafo vero, foto non oltre la sua misura, barra Persefone sotto con un titolo | Krone `18`, Schgaguler `23`, Berghotel `07` |
| Com'è da noi | collage di foto piccole su griglia | Zirmerhof `10` |
| Navigazione | tessere foto con etichetta che dice un fatto | Krone `19` |
| Camere | fisarmonica Doppia, Tripla, Quadrupla con m² | Waldhaus `02`, Muottas `25` |
| Benessere | orari e prezzo come titolo, giornata a orari solo con orari veri | Schwanen `20`, Berghotel `08` |
| Ristorante | piatti in fila con etichetta, nome di chi cucina, didascalia sotto | Waldhaus `03`, Zirmerhof `11`, Schgaguler `24` |
| Asiago | schede Estate e Inverno nella sezione | Muottas `26`, Tannerhof `14` |
| Piede | profilo dell'orizzonte, stagioni, arrivo e partenza, contatti in fila | Berghotel `06`, Waldhaus `04`, Tannerhof `17`, Schwanen `22` |

**Regola per le foto** (tutti i riferimenti mostrano foto vere, nessuno le ingrandisce). Due livelli, secondo la conferma del cliente:
- con il servizio Booking (3000 x 1996, dettaglio vero fino a circa 2250 px secondo 01): apertura e fasce a tutta larghezza a 1440 su schermi normali, su retina non oltre circa 1100 px di larghezza; sono le foto per apertura, tessere, camere, benessere e ristorante;
- con le sole foto del sito (camere 2018 a 1024 x 768, piatti 800 x 600, panorama d'inverno 1600 x 1066): niente tutta larghezza, collage, file e tessere piccole, non oltre 512 px su retina.
La foto della sauna in home (`centrpbenessere.jpg`) è con ogni probabilità stock (01) e non si usa. Le foto che mancano comunque (la vista dal balcone sulla Piana, la Piana d'estate dall'albergo, i piatti su fondo neutro) vanno nel brief del LEGGIMI.

## 4. Accoppiate

Tre accoppiate, provate con i testi del sito e le foto del servizio Booking in `_prova/ricerca/accoppiate-prova.png` (sorgente in `_prova/ricerca/prova/accoppiate.html`, caratteri caricati da Google Fonts). Tutte su fondo bianco, come sette riferimenti su otto. Nessun corsivo. Il logo è quello che il cliente indica come ufficiale (il gotico della testata o il tondo con il monte) [DA CONFERMARE], in un colore solo.

### A. "Abete" (consigliata)
- **Caratteri**: titoli in **Source Serif 4** 600, taglio Display (ottico automatico), i titoli di sezione in maiuscolo ("CAMERE", "BENESSERE") come i titoli in Larken di Waldhaus, i sottotitoli in tondo minuscolo; testo, menu, orari, prezzi e pulsanti in **Schibsted Grotesk** 400, 500 e 600, testo a 16-17 px.
- **Colori**: Verde Vescovi #263F12 (il verde della testata di oggi; il logo tondo usa #293F1C, quasi uguale) per titoli, pulsanti e una fascia piena per pagina; bianco #FFFFFF di fondo; Pietra #F1F2EE per le fasce di servizio (orari, barra date); Inchiostro #1B2117 per il testo; Grigio #585F52 per le note; Stelle #EEE43E (il giallo delle stelle del logo) solo sulle fasce verdi; filetti #C9D0BF.
- **Perché**: Waldhaus (verde #1E5E42 su bianco, serif per i titoli e senza grazie per le informazioni) e Berghotel (verde #065544 su bianco) mostrano che un albergo alpino di famiglia sta bene con un verde solo, su bianco. Il verde di Vescovi c'è già, quindi è continuità e non un colore nuovo. Il serif per i titoli viene da Waldhaus (Larken), Zirmerhof (Bembo) e Tannerhof (Galliard), tutti diritti; Source Serif 4 è più robusto del Cormorant di Meltar e del Playfair di Linta, e nessuno dei concorrenti visti lo usa. Schibsted Grotesk fa il lavoro di Inter in Waldhaus senza essere Inter.
- **Contrasti**: Inchiostro su bianco 16,45:1; Grigio su bianco 6,62:1; Verde su bianco e bianco su Verde 11,65:1; Inchiostro su Pietra 14,63:1; Grigio su Pietra 5,88:1; Verde su Pietra 10,36:1; Stelle su Verde 8,77:1; filetto #C9D0BF su Verde 7,36:1.
- **Barra Persefone**: `sfondo=F1F2EE&testo=1B2117&pulsante=263F12&testopulsante=FFFFFF`.
- **Rischio**: con poche foto buone il verde pieno può pesare; una sola fascia verde per pagina.

### B. "Bacheca"
- **Caratteri**: titoli, orari, prezzi e etichette in **Archivo Narrow** 700 maiuscolo (600 per le righe degli orari); testo in **Newsreader** 400 a 18 px, con grazie, da leggere.
- **Colori**: bianco #FFFFFF; Inchiostro #211C16 per titoli e testo; Larice #7A4512 (il legno delle camere rinnovate, della reception e della stube) per pulsanti ed etichette; Pietra #F2F1EE per le fasce; Grigio #5E554B per le note; il Verde Vescovi resta solo nel logo.
- **Perché**: Schwanen scrive titoli e orari in un senza grazie stretto (Interstate Condensed) e i sottotitoli in un serif (Minion Bold Condensed); Krone usa un senza grazie stretto e un solo colore scuro e caldo sul pulsante (#630F0E); Zirmerhof usa un ocra bruno (#865300). Le maiuscole strette di Archivo Narrow sono vicine alle lettere alte e strette del logo tondo. È l'accoppiata più "da bacheca dell'albergo": orari, prezzi e metri quadri in evidenza, in accordo con il legno delle camere e i piatti fotografati sul bianco.
- **Contrasti**: Inchiostro su bianco 16,90:1; Grigio su bianco 7,30:1; Larice su bianco e bianco su Larice 7,81:1; Inchiostro su Pietra 14,97:1; Larice su Pietra 6,92:1; Grigio su Pietra 6,46:1.
- **Barra Persefone**: `sfondo=F2F1EE&testo=211C16&pulsante=7A4512&testopulsante=FFFFFF`.
- **Rischio**: titoli stretti in maiuscolo e un colore solo ricordano l'impianto di Benvegnù; il testo in serif e il bruno al posto del rosso lo tengono distinto, ma va controllato nella proposta di direzione (2.3).

### C. "Neve"
- **Caratteri**: titoli in **Libre Caslon Display** 400 (solo da 40 px in su, in tondo); testo e informazioni in **Albert Sans** 300 e 400, etichette in 600 maiuscolo.
- **Colori**: bianco #FFFFFF; Neve #EDF1F3 per le fasce; Notte #1C2630 per titoli e testo; Grigio #56616B per le note; Verde Vescovi #263F12 solo per il pulsante Prenota; filetti #C9D2D8.
- **Perché**: Schgaguler (Canela sottile e Maison Neue, grigi chiari) e Muottas Muragl (serif per i titoli, grigio azzurro) mostrano la montagna d'inverno, luce fredda e molta aria; tra le foto dell'albergo ci sono Asiago con la neve al tramonto e l'albergo nella neve (Booking, 2000 x 1500).
- **Contrasti**: Notte su bianco 15,34:1; Grigio su bianco 6,33:1; Notte su Neve 13,49:1; Grigio su Neve 5,57:1; Verde su Neve 10,25:1; bianco su Notte 15,34:1; bianco su Verde 11,65:1.
- **Barra Persefone**: `sfondo=EDF1F3&testo=1C2630&pulsante=263F12&testopulsante=FFFFFF`.
- **Rischio**: è la più vicina al "lusso" di Meltar e promette un albergo diverso da un tre stelle con cucina di casa; il serif sottile non regge sotto i 40 px. Terza scelta.

**Scelta consigliata: A "Abete"**, con due innesti da B: le righe degli orari e dei prezzi con i filetti (Schwanen) e il colore della casa usato solo sui pulsanti e su una fascia (Krone). Il bruno Larice e il serif sottile di C restano fuori.
