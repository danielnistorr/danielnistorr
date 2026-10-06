# 02. Concorrenti e riferimenti di design

Ricerca del 6 ottobre 2026. Tutti i siti sono stati aperti con Playwright (Chromium, attraverso il proxy), fotografati a 1440 e a 390 px e guardati a pezzi. Screenshot interi in `_prova/ricerca/` (`c*` concorrenti, `r-*` home dei riferimenti, `p-*` pagine prodotto dei riferimenti, `00-wirmec-*` il sito attuale), ritagli dei pezzi da riprendere in `_prova/ricerca/ritagli/`, prova delle accoppiate in `_prova/ricerca/accoppiate-prova.png`.

Siti visitati: 5 concorrenti (più una pagina prodotto di Mecal) e 28 siti di costruttori provati per i riferimenti, di cui 7 tenuti, con 6 pagine prodotto fotografate a 1440 e 390. Knipex (verifica di sicurezza), Kern Microtechnik (blocco Vercel) e Weidmüller (connessione rifiutata) non si aprono in modo automatico; Trotec risponde 404 all'indirizzo italiano; Formlabs apre con una finestra di scelta del paese.

Wirmec in breve, per il confronto (dal sito attuale): Ponte San Nicolò (PD), "Wirmec realizza macchine per l'aggraffatura automatica e manuale su cavi di varia sezione", payoff "...the right partner for Harness Makers", linee WirTool (applicatori), WirPress (semiautomatiche da banco), WirStrip (taglia e spela automatiche), WirAM (taglia spela aggraffa automatiche), Accessori Macchina, WirTest (controllo qualità: W100 dinamometro 1000N, W200 laboratorio di micrografia).

## 1. Concorrenti

Nella zona (Padova, Vicenza, Treviso, Verona) la ricerca ha restituito aziende di cablaggio e di componenti, nessun altro costruttore di presse e applicatori con un sito da confrontare. Wirmec si confronta quindi con costruttori nazionali e internazionali che vendono la stessa gamma agli stessi clienti, i cablaggisti.

| # | Concorrente | Sede | Cosa vende in comune | Fa meglio di Wirmec | Fa peggio di Wirmec | Screenshot |
|---|---|---|---|---|---|---|
| 1 | [Mecal](https://www.mecal.net/) | Fubine Monferrato (AL), "fondata nel 1976" | applicatori, aggraffatrici, accessori, controllo di processo, "spella e aggraffa": la stessa gamma | apertura con una macro vera di terminali aggraffati; pagine per famiglia con tutte le macchine scontornate su bianco alla stessa scala; quattro lingue, pagina distributori, area clienti | la home è solo l'apertura e il piè di pagina, il menu è un hamburger anche a 1440; slogan generico ("Connettendo un mondo migliore"); nella griglia [Aggraffatrici](https://mecal.net/prodotti/aggraffatrici/) solo codici (TT, P107c, P020i...) senza forza né sezione, mentre Wirmec scrive "Aggraffatrice da banco 20kN" nel titolo; a 390 px nella pagina Aggraffatrici il logo non si carica (si legge "Logo") e le macchine compaiono una per schermo | `c1-mecal-*`, `c1b-mecal-aggraffatrici-*` |
| 2 | [GM Automazioni](https://www.gmautomazioni.eu/) | Busnago (MB) | "vendita e assistenza macchine taglia spela aggraffa", spelafili, miniapplicatori | dice in una riga cosa fa; elenca servizi concreti (corsi, installazione, riparazioni, campionature gratuite, manutenzioni programmate); modulo di contatto anche nel piè di pagina | tessere con velatura blu sopra le foto e testo condensato bianco; elenco con spunte verdi; numeri non verificabili ("+3.100 clienti soddisfatti"); email su gmail; a 390 px il menu è già aperto sopra l'apertura; piè di pagina fermo al 2018 e 2020 | `c2-gmautomazioni-*` |
| 3 | [Cembre](https://www.cembre.com/it) | Brescia | connettori, capicorda, utensili e presse per l'aggraffatura (sovrapposizione parziale) | foto prodotto professionali su nero; un numero concreto ("oltre 4.9 milioni di connessioni" al giorno); settori (Industry, Railway, Power) con foto vere; ricerca in testata | parole inglesi giganti a contorno usate come decoro dietro le sezioni (una è "Video", le altre sono nella lista `PAROLE_VIETATE`), parentesi d'angolo azzurre, carosello in apertura, Montserrat nero maiuscolo pesante ovunque | `c3-cembre-*` |
| 4 | [Schleuniger](https://www.komaxgroup.com/it/brands/schleuniger) (Komax Group) | Thun (CH), "founded in 1975" | taglia e spela, aggraffatura semiautomatica, periferiche, prova di trazione (come W100) | famiglie su fondo scuro con render illuminati; ogni modello con dati tecnici e PDF; premi di design (red dot, iF 2023) per l'interfaccia delle macchine | dall'indirizzo italiano la pagina è in inglese; titoli corporate ("For the Highest Demands", "The Road to Automation"); nella pagina del marchio nessun numero di telefono (nessun link tel:), il contatto passa da "Local Contacts" e, nelle schede, da "Talk to an Expert" | `c4-schleuniger-*` |
| 5 | [Metzner Maschinenbau](https://www.metzner.com/) | Germania | taglio e lavorazione di cavi e tubi (si sovrappone a WirStrip) | dichiarazione semplice ("Automation of cutting & processing"); foto vere dei tubi lavorati | home cortissima con due tessere velate di grigio; Frutiger Light condensato grigio chiaro poco leggibile; a 390 px la pagina scorre di lato (410 px su 390); piè di pagina con "2023"; a 390 px finestra privacy a tutto schermo | `c5-metzner-*` |

**Cosa fa già bene Wirmec** (da tenere): il dato nel titolo del prodotto ("W 1500 - Aggraffatrice da banco 20kN"); gamma completa fino al controllo qualità, come Schleuniger; brochure scaricabili; macchine vere fotografate e scontornate (in `/FotoHQ/`: `w1500_bianca.png` 600x650 con trasparenza, `am210futura.jpg` 744x650, `w200.jpg` 800x573, `wsc25.jpg` 366x650).

**Cosa fa peggio di tutti** (da `00-wirmec-*`): larghezza fissa di circa 992 px senza meta viewport, a 390 px il testo è minuscolo; elenco prodotti con miniature a pallino; login in home; piè di pagina fisso (`position:fixed; bottom:0` in `struttura.css`) che copre sempre il fondo dello schermo; grigio del testo #787B7E su bianco a 4,26:1.

**Cosa non fa bene nessuno (spazio per Wirmec):**
1. mostrare il risultato della macchina: il terminale aggraffato e la sua sezione al micrografo. Wirmec vende il W200 laboratorio di micrografia, nessun concorrente fa vedere una sezione;
2. dati confrontabili tra i modelli di una famiglia (forza in kN, sezioni, side feed o end feed): Mecal mostra solo codici, GM nessun dato;
3. un contatto umano diretto in ogni scheda: telefono e email per l'Italia, distributori per l'estero;
4. il telefono: Mecal, GM e Metzner hanno difetti visibili a 390 px.

**Copy da non usare** (visto nei concorrenti): le parole già nella lista `PAROLE_VIETATE` di `build.py`, più "connettendo un mondo migliore", "campioni nel preparare", "partner ideale", "punto di riferimento", "for the highest demands", contatori di anni ("da cinquanta anni"). Si scrivono i fatti: cosa fa la macchina, su che sezione, con che forza.

## 2. Riferimenti premium

Wirmec costruisce macchine da banco, applicatori e strumenti di controllo per chi fa cablaggi. Il riferimento giusto non sono le agenzie né la moda, ma i costruttori di macchine con i siti migliori: il primo del settore (Komax), costruttori di macchine utensili (Hermle, Trumpf, Salvagnini, che è a Sarego, in provincia di Vicenza), robot da banco (Universal Robots), sistemi di taglio (Zünd), connettori, cioè quello che i clienti di Wirmec aggraffano (LEMO). Hanno tutti le stesse caratteristiche: la macchina scontornata su grigio chiaro o bianco, il codice del modello come titolo, i dati tecnici in tabella, il PDF da scaricare, un contatto commerciale vicino al prodotto, il rosso (o il colore del marchio) usato poco.

| # | Riferimento | Pagina vista | Cosa fa | Ritagli |
|---|---|---|---|---|
| 1 | [Komax Group](https://www.komaxgroup.com/) (cablaggio) | [StripCrimp 208](https://www.komaxgroup.com/en-us/products/wire-processing/semi-automation-machines/wire-crimping/stripcrimp-208), l'equivalente della WSC 25 | pittogrammi del filo per dire cosa fa la macchina, tabella dati, scheda download | `01`, `02`, `03`, `04`, `05` |
| 2 | [Hermle](https://www.hermle.de/en/) (centri di lavoro, Gosheim) | [C 12 GEN2](https://www.hermle.de/en/machining-centres-automation/models/machining-centre-c-12-gen2/) | codice modello enorme su grigio studio, barra di ancore, il pezzo lavorato con i dati del materiale | `06`, `07`, `08` |
| 3 | [Universal Robots](https://www.universal-robots.com/it/) (robot collaborativi) | [UR7e-920](https://www.universal-robots.com/it/prodotti/ur7e-920/) e home | codice come titolo, frase con tre numeri, riquadro valori, due pulsanti; famiglia con tre numeri per scheda | `09`, `10` |
| 4 | [Salvagnini](https://www.salvagninigroup.com/it-IT) (lamiera, Sarego VI, [fonte](https://atoka.io/public/it/azienda/salvagnini-italia-spa/8bb04bc2a8c8)) | [Presse piegatrici B3](https://www.salvagninigroup.com/it-IT/prodotti/presse-piegatrici/B3) e home | tabella con tutti i modelli in colonna, panoramica a punti sulla foto, famiglie in apertura | `11`, `12`, `13` |
| 5 | [Zünd](https://www.zund.com/it) (sistemi di taglio, Svizzera) | home e [Product Finder](https://www.zund.com/it/sistemi-di-taglio/productfinder) | IBM Plex Sans su tutto il sito, percorso a passi per trovare la macchina, pannello scuro con la macchina tagliata dal bordo | `14`, `15` |
| 6 | [TRUMPF](https://www.trumpf.com/it_IT/) (macchine utensili) | [TruBend Serie 7000](https://www.trumpf.com/it_IT/prodotti/macchine-sistemi/piegatrici/trubend-serie-7000/), piegatrice compatta | colonna con telefono del reparto commerciale e brochure, schede della pagina, dettagli macro a scacchiera | `16`, `17` |
| 7 | [LEMO](https://www.lemo.com/) (connettori) | home | un filo sottile che scende tra le sezioni e finisce in un punto; il prodotto appoggiato sul bordo della fascia scura | `18`, `19` |

## 3. Cosa si riprende

Per ognuno: il gesto preciso, dove andrebbe nel sito Wirmec, cosa non si prende. Mai copiare: si prende l'idea, non il disegno.

### 3.1 Komax, StripCrimp 208
- **Gesto: "Processing capabilities"** (`ritagli/01`). Sei pittogrammi orizzontali dello stesso cavo, guaina bianca e rame scoperto, che dicono cosa fa la macchina: spelatura totale, parziale, multipla, aggraffatura, multipolare. È il disegno più "di settore" visto in tutta la ricerca e nessun concorrente italiano lo usa. Per Wirmec: un disegno del filo per famiglia, a linea, stessa scala, disegnato in SVG: WirStrip il filo spelato, WirTool e WirPress il filo con il terminale, WirAM taglio, spela e aggraffa in sequenza, WirTest il terminale in sezione. Va nelle schede famiglia della home e in apertura delle pagine famiglia. Sostituisce le icone, non si aggiunge a esse.
- **Tabella dati tecnici** (`02`): righe a fondo alterno appena percettibile, nome del modello in testa con un filetto nero, "Mostra tutto" per le righe oltre la sesta; a 390 px l'etichetta va sopra e il valore sotto. Per Wirmec: la scheda di ogni macchina.
- **Scheda download** (`04`): miniatura del PDF, nome, formato, lingua e peso, un solo pulsante. Per Wirmec: le brochure che il sito già offre.
- **Evitare**: l'animazione delle lettere dei titoli (negli screenshot la prima lettera resta tagliata), l'arancione Schleuniger, le card molto arrotondate su grigio sfumato (`05`), l'interruttore metrico e imperiale.

### 3.2 Hermle, C 12 GEN2
- **Gesto: apertura della scheda** (`06`). La macchina scontornata su un grigio uniforme che continua nell'ombra a terra, il codice del modello enorme a sinistra ("C 12 GEN2") con il nome della linea sotto e un filetto rosso corto. Il grigio della foto e il grigio della fascia sono lo stesso: la macchina non sta in un riquadro. Per Wirmec: "W 1500" grande e la macchina accanto sul grigio #E6E6E6, che è già il fondo dell'apertura del sito attuale.
- **Barra di ancore** sotto l'apertura (Technical data, Applications, Options, Downloads, Contact person); a 390 px diventa un menu a tendina con il contatto accanto. Per Wirmec: Dati tecnici, Applicatori compatibili [DA CONFERMARE], Download, Contatto.
- **"Applications"** (`07`): il pezzo lavorato in foto e sotto la didascalia tecnica (materiale, rugosità Ra 0,035 µm). Per Wirmec è il gesto che i concorrenti non hanno: il terminale aggraffato e la sua micrografia con sezione del filo e tipo di terminale. Le foto non esistono sul sito attuale: brief da mettere nel LEGGIMI [DA CONFERMARE].
- **Evitare**: dati in celle grigio scuro con testo centrato (`08`, si legge peggio di una tabella a righe); linguetta "CONTACT" verticale fissata al bordo; titoli lunghi in rosso.

### 3.3 Universal Robots, UR7e-920 e famiglia
- **Gesto: il codice è il titolo** (`09`). "UR7e-920" in condensato nero molto grande, sotto una frase che contiene i tre numeri che contano ("Carico utile di 7,5 kg, portata di 920 mm..."), a fianco un riquadro con quattro righe etichetta e valore, sotto due pulsanti affiancati: "Richiedi un preventivo" pieno e "Scarica la scheda tecnica" a contorno. Con foto Wirmec alte al massimo 650 px, è il codice in tipografia grande a dare la scala alla pagina, non la foto.
- **Famiglia** (`10`): schede con la macchina su grigio chiaro, codice, una riga, tre numeri piccoli con l'etichetta sopra. Per Wirmec: le pagine WirPress e WirStrip con forza, sezione e alimentazione per ogni macchina (valori dalle brochure [DA CONFERMARE]).
- **Evitare**: il badge "Novità" sopra la foto; l'azzurro UR; la galleria di miniature quando la macchina ha una sola foto; il modulo in iframe (da noi Contact Form 7).

### 3.4 Salvagnini, B3 (Sarego, Vicenza)
- **Gesto: tabella della famiglia** (`12`). Tutti i modelli in colonna, una riga per grandezza con l'unità tra parentesi ("Forza massima (t)", "Lunghezza di piega (mm)"): si confrontano i modelli con un'occhiata. Per Wirmec: una tabella per WirPress e una per WirTool, con i modelli in colonna. Su telefono la prima colonna resta ferma e la tabella scorre di lato dentro il suo contenitore, non la pagina.
- **Panoramica a punti** (`11`): la macchina su fondo scuro con quattro punti "+" sulla foto e a sinistra un elenco di cinque voci che si aprono. Per Wirmec, solo su una macchina con dati sicuri (WSC 25 o AM 210 Futura): punti numerati e testo sempre visibile sotto, niente contenuto che appare solo al passaggio del mouse.
- **Famiglie in apertura** (`13`): in fondo all'apertura della home i nomi delle famiglie come accesso diretto. Per Wirmec: WirTool, WirPress, WirStrip, WirAM, WirTest come prima navigazione.
- **Evitare**: blocchi rossi sfalsati dietro le foto, numeri giganti a contorno su fascia rossa (Wirmec non ha numeri pubblici verificati), la finestra della lingua che a 390 px copre la pagina, i render 3D astratti in apertura.

### 3.5 Zünd
- **Gesto: tipografia**. IBM Plex Sans su tutto il sito, titoli semibold con un filetto rosso corto, interfaccia piccola e regolare: un costruttore di macchine di precisione che parla come un manuale tecnico. È la base dell'accoppiata A.
- **"Trova la fresa che fa per te"** (`14`): un percorso a passi ("1 di 5") con domande sul lavoro del cliente. Per Wirmec, in versione semplice e senza script: "Cosa devi lavorare?" con tre risposte che portano alla famiglia giusta (spelare, aggraffare terminali in nastro, controllare l'aggraffatura).
- **Highlight** (`15`): pannello scuro con la foto della macchina tagliata dal bordo sinistro, famiglia sopra il nome in piccolo, frecce piccole e contatore "1 / 4".
- **Evitare**: maiuscolo molto spaziato su ogni etichetta, video in apertura (nella nostra prova non parte e resta un campo vuoto), pulsante "Contattateci!" fisso a lato.

### 3.6 TRUMPF, TruBend Serie 7000
- **Gesto: colonna del contatto** (`16`). A destra della scheda prodotto, in una colonna propria: "Reparto commerciale", il numero di telefono scritto per intero, la mail; più sotto la brochure con copertina, formato e peso. Per Wirmec: in ogni scheda "Tel. +39 049 718 464, info@wirmec.com" (dal piè di pagina attuale) e la brochure del modello. A 390 px la colonna scende sotto i dati.
- **Schede della pagina** (Panoramica, Applicazioni, Dati tecnici, Equipaggiamento...) che a 390 px scorrono di lato con una freccia.
- **Dettagli a scacchiera** (`17`): due foto macro dei particolari alternate al testo. Per Wirmec: l'applicatore WirTool da vicino (ottone, acciaio, targhetta rossa) è l'oggetto più bello che hanno, ma la foto attuale è piccola: va rifatta [DA CONFERMARE].
- **Evitare**: l'alone colorato sfumato sotto la macchina, testo centrato grigio chiaro in paragrafi lunghi, icone di servizio a linea in colonna, il verde lime.

### 3.7 LEMO
- **Gesto: il filo** (`19`). Una linea sottile che scende tra due blocchi e termina in un punto, come un conduttore con il suo terminale. Per Wirmec: una sola volta, in home, a collegare l'apertura alle famiglie; nel colore ardesia, non in un colore nuovo.
- **Prodotto sul bordo** (`18`): i connettori appoggiati sul bordo della fascia scura, metà dentro e metà fuori. Per Wirmec: una macchina scontornata (W 1500 o l'unità AM 0090, entrambe in PNG con trasparenza) che morde il bordo della fascia ardesia.
- **Evitare**: una parola del titolo colorata ("perfect match"), titolo bianco su fondo chiaro che dipende dal video (a 390 px "EMPOWERING" quasi non si legge), tessere scure con scritte verticali che si accendono al passaggio.

### 3.8 Considerati e scartati
Wera (nero e verde, tono da utensileria di consumo), Formlabs, Kistler, Datron, Harting, WAGO, ZwickRoell, Fluke, Bystronic, Comau, Breton, Tornos, Dallan, Festool, GF United Machining, Rennsteig, Wezag: siti corretti ma senza un gesto più preciso di quelli sopra, o con caroselli, finestre e promozioni in apertura. Scartati in generale: badge sopra i titoli, numeri a contorno, video in apertura, render 3D, aloni sfumati, linguette fisse ai bordi, testo che compare solo al passaggio, caroselli automatici.

## 4. Accoppiate

**Materiale di partenza di Wirmec** (dal CSS e dalle immagini del sito attuale):
- rosso del marchio #E20004 (33 occorrenze nel CSS), rossi scuri #D00F12 e #9B1517;
- ardesia #323A41 (la barra scura sotto il logo), grigio #787B7E (testi, 4,26:1 su bianco: troppo chiaro per testo piccolo), grigio chiaro #E6E6E6 (fondo dell'apertura e delle foto);
- caratteri attuali: Ropa Sans (menu, condensato), Voces (titoli), Tahoma (testo);
- miniature delle famiglie virate per colore: WirTool blu #477EAE, WirPress ambra #D59F19, WirStrip arancio #CC7A41, Accessori #D48F64, WirTest verde #6F9D50 (campionati dallo screenshot `00-wirmec-1440.png`). È un codice colore per linea che l'azienda usa già, e ricorda le guaine colorate dei pittogrammi Komax;
- foto: macchine vere, scontornate o su bianco, alte al massimo 650 px. Si mostrano sempre alla loro misura o più piccole, su grigio #E6E6E6 o su bianco; la scala della pagina la danno i codici modello in tipografia grande (Hermle, Universal Robots), non foto ingrandite.

Nessun costruttore visto usa un serif (Wera usa uno slab solo per il proprio marchio): niente serif, niente corsivi, niente crema. Solo Google Fonts. Tutte e tre sono provate con testi veri di Wirmec in `_prova/ricerca/accoppiate-prova.png`.

### A. "Scheda tecnica" (consigliata)
- **Caratteri**: IBM Plex Sans Condensed 600 per codici modello, titoli e menu; IBM Plex Sans 400 e 500 per testo e pulsanti; IBM Plex Mono 500 solo per i valori nelle tabelle e per i codici articolo (20 kN, 135,78 mm, AM 0090).
- **Perché**: Zünd usa IBM Plex Sans su tutto il sito; Komax, Salvagnini e Universal Robots trattano la pagina prodotto come una scheda tecnica, e Plex ha cifre tabellari e un mono della stessa famiglia; il condensato prosegue il Ropa Sans del menu attuale; è diverso da Benvegnù (Barlow).
- **Palette**: bianco #FFFFFF; grigio studio #E6E6E6 (lo stesso fondo delle foto, come Hermle); ardesia #323A41 per la fascia scura e i codici modello; testo #1F2429; testo secondario #5C6369; rosso #E20004 per il pulsante pieno, il filetto sotto il codice (Hermle, Zünd) e la voce di menu attiva; hover #9B1517 (dal CSS attuale, colore pieno, mai opacità); i colori delle famiglie solo come filetto di 4 px accanto al nome della linea, mai come testo o fondo.
- **Contrasti**: #1F2429 su bianco 15,64:1, su #E6E6E6 12,53:1; #5C6369 su bianco 6,10:1, su #E6E6E6 4,89:1; bianco su #323A41 11,56:1; #E6E6E6 su #323A41 9,26:1; bianco su #E20004 4,96:1 (pulsante, testo 15-16 px semibold); #E20004 su bianco 4,96:1 ma su #E6E6E6 solo 3,97:1, quindi i link rossi su grigio usano #9B1517 (6,69:1; 8,36:1 su bianco); #E20004 su #323A41 2,33:1: niente testo rosso sulla fascia ardesia. Filetti famiglia su bianco: #477EAE 4,32:1, #CC7A41 3,27:1, #6F9D50 3,17:1, #D59F19 2,39:1: sono segni accanto a un nome scritto in #1F2429, non portano informazione da soli.

### B. "Codice grande"
- **Caratteri**: Archivo con l'asse della larghezza: larghezza 62 e peso 800 per codici modello e titoli (W 1500, WSC 25), larghezza 100 per testo, tabelle e pulsanti, cifre tabellari.
- **Perché**: Universal Robots (Oswald per "UR7e-920") ed Hermle ("C 12 GEN2") mostrano che in questo settore il nome della macchina è il titolo; una sola famiglia in due larghezze, come Komax usa solo Helvetica (Now Display e Neue). Con foto piccole il codice molto condensato e molto grande riempie la scena senza ingrandire nulla.
- **Palette**: nero #111315, bianco, grigio studio #E6E6E6, testo secondario #5A5F64, rosso #E20004 solo come filetto 72x3 px sotto il codice e come voce attiva; pulsante pieno nero, hover #9B1517.
- **Contrasti**: #111315 su bianco 18,62:1, su #E6E6E6 14,92:1; #5A5F64 su bianco 6,45:1, su #E6E6E6 5,17:1; bianco su #111315 18,62:1; bianco su #9B1517 8,36:1.
- **Rischio**: più manifesto che scheda tecnica; il nero pieno toglie spazio al rosso e all'ardesia che sono di Wirmec.

### C. "Ardesia e grigio studio"
- **Caratteri**: Roboto Condensed 600 e 700 per codici e titoli, Roboto Flex 400 e 500 per il testo: sono esattamente i caratteri di Hermle (Roboto Condensed) e di Universal Robots (Roboto Flex).
- **Perché**: la scelta più sicura e leggibile, con fasce alternate ardesia e grigio come il bianco e nero di Salvagnini e le famiglie su scuro di Schleuniger; l'ardesia è quella della barra del sito attuale.
- **Palette**: ardesia #323A41 per le fasce scure con testo bianco o #E6E6E6; grigio studio #E6E6E6; bianco; testo #1F2429; rosso #E20004 per i pulsanti; testo secondario su ardesia #9EA2A7 solo da 16 px in su.
- **Contrasti**: bianco su #323A41 11,56:1; #E6E6E6 su #323A41 9,26:1; #9EA2A7 su #323A41 4,50:1 (al limite); #1F2429 su #E6E6E6 12,53:1; bianco su #E20004 4,96:1.
- **Rischio**: Roboto è il carattere più diffuso del web; corretto ma poco riconoscibile, il contrario di quello che serve a un'azienda che oggi non si distingue.

**Proposta**: A come base, con il gesto di B innestato (codice modello in Plex Sans Condensed molto grande accanto alla macchina, alla Universal Robots e Hermle), le fasce ardesia di C usate una o due volte per pagina, il disegno del filo di Komax al posto delle icone, la colonna del contatto di TRUMPF in ogni scheda. Da decidere nella fase 2.3 con i punteggi.
