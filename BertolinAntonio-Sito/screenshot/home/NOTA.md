# Antonio Bertolin Srl: nota sulla home finale

Versione finale della home, costruita sulla bozza B ("Il telaio"), che ha scelto il committente. Dopo il giudizio cieco (50 su 80, non passa) è stata rifinita senza cambiare idea, prima schermata, trattamento delle immagini, carattere e colori, come chiede il committente. Cosa è cambiato e cosa no è nella sezione "Rifinitura dopo il giudizio cieco".

File:
- la pagina: `sito/index.html`, con `sito/img/` e `sito/fonts/`;
- la sorgente: `_prova/script/pagina-finale.html`;
- lo script che rifà tutto: `bash _prova/script/build_finale.sh`, che rifà immagini, logo, caratteri, pagina, controlli sul testo, screenshot, segnali e controlli finali (`_prova/controlli/verifica.txt`).

## L'idea

La fabbrica vera come prova. La pagina si apre sul telaio di ossidazione caricato di boccole, a tutta larghezza, con due palloncini numerati come in un disegno d'assieme e la loro distinta sotto la foto. Sopra, su bianco, c'è il nome del mestiere in una riga sola che occupa tutta la giustezza: "Ossidazione anodica".

Poi vengono:
- chi sono;
- il colore, che sul titanio è uno spessore e sull'alluminio un pigmento, mostrato sui loro pezzi;
- i sei trattamenti, che si filtrano per metallo;
- l'impianto del 2018, lo stabilimento di Tombelle e i recapiti sulla scala dei colori del titanio, la cui ultima barretta è una targhetta (vedi "La chiusura").

Su questa pagina il nome di un concorrente non reggerebbe: le foto, i colori dichiarati, il 2018 e l'indirizzo sono tutti di Bertolin.

## Le prime due schermate

**A 1440** (`home-1440-prima-schermata.jpg`):
- la testata ha il logo (SVG), quattro voci, "Scriveteci" (mailto) e il telefono;
- il titolo è a 134 px, largo quanto la gabbia;
- sotto, dalla settima colonna, tre righe su cosa fanno e dove, con la Type II;
- poi il telaio da bordo a bordo, alto 700 px e mostrato a 1:1, con i palloncini 1 e 2 sul pezzo.

Nella seconda schermata ci sono la distinta ("1 Barra del telaio", "2 Boccola tornita"), la didascalia alla settima colonna, il paragrafo grande su chi sono e "Per chi lavoriamo". Il colore arriva alla terza: a 1440 il titolo sul titanio è a y 1761 e la minuteria comincia a y 1925. Prima il titolo era a y 2972.

**A 390** (`home-390-prima-schermata.jpg`):
- la testata ha il logo, "Trattamenti", "Scriveteci" e il telefono; sotto i 380 px resta "Trattamenti" col telefono;
- il titolo va su due righe a 47 px, seguito dalle righe di testo;
- il telaio è in un taglio verticale 4:5 a filo, con gli stessi due palloncini, e la prima schermata finisce sulla foto.

**Altezza della pagina** (sei sezioni contando il piede):

| Larghezza | Altezza |
|---|---|
| 320 | 6059 px |
| 390 | 5955 px |
| 768 | 5652 px |
| 1024 | 5405 px |
| 1440 | 6015 px |
| 1920 | 6016 px |

## Cosa era già cambiato rispetto alla bozza B

Prima del giudizio cieco, sulla bozza B erano già stati fatti questi interventi.
- **Telaio**: tagliato a 1:1 sulla parte a fuoco della foto (x 0-1440 su 2560), fondo schiarito e lisciato dalle bande JPEG solo sui punti chiari, maschera di contrasto leggera; la fascia ha sempre la proporzione 1440:700.
- **Legende**: tolta "3 Pinza", che non indicava niente di leggibile; "Boccola tornita" invece di "in alluminio", perché il metallo non è confermato.
- **Trattamenti**: il selettore a pillola è diventato la frase "Il pezzo è in alluminio, titanio o acciaio?" con tre bottoni veri; nella colonna delle misure restano solo i valori veri (0-400 nm, 5-20 micron, grigio scuro, citrico o nitrico).
- **Colore**: aggiunto "Sull'alluminio il colore è un pigmento" in parallelo al titanio; i tubi sono ripuliti dalla polvere.
- **Contatti** (dalla bozza A): la riga del preventivo con info@bertolinantonio.it e l'indirizzo come titolo.
- **Dati**: "in provincia di Venezia" come scrive il sito; "metropolitane, tram, filobus e Ferrovie dello Stato" dal "ferroviario, tranviario, filoviario" del sito.
- **Accessibilità**: link "Vai al contenuto", grigio delle note a #565A60 (5,6:1 sul campo), oro dei link scurito a #8F6B1D.
- **Non applicato allora** (valeva solo per la bozza A): Switzer, il piede chiaro, l'interruttore Titanio/Alluminio, l'apertura sui tondini.

## Rifinitura dopo il giudizio cieco

**Applicato**
- **Le legende dell'apertura**: le etichette in pillola bianca somigliavano a quelle di Area Systems, che è dello stesso giro e dello stesso paese. Ora sulla foto restano solo un punto, un filo e un palloncino col numero, come in un disegno d'assieme di un'officina meccanica. I nomi stanno nella distinta sotto la foto, sulla sinistra, e la didascalia è alla settima colonna, allineata con il testo d'apertura.
- **Il colore prima**: la sezione "Sul titanio il colore è uno spessore" viene subito dopo chi sono, prima dei trattamenti. La minuteria colorata è alla terza schermata, non più alla quinta. Anche la navigazione segue il nuovo ordine.
- **La minuteria**: il taglio è più stretto sul gruppo centrale (1100 x 1040 della foto, senza il pezzo argentato tagliato sul bordo) e la foto esce a destra fino al bordo della gabbia larga. I pezzi sono circa una volta e mezza più grandi di prima. Il paragrafo sta 36 px sotto il titolo, non più in basso a 720 px. A 390 restano due legende, Blu e Oro.
- **Il logo**: è un SVG ridisegnato dal PNG del sito (`_prova/script/logo_svg.py`: ingrandimento 8 volte, contorni con OpenCV). È in linea come `<symbol>` nella testata (il piede ora è una riga di testo e non lo ripete). A DPR 2 i bordi sono netti, "srl" e "MECCANICHE" si leggono. Resta da chiedere il vettoriale vero.
- **Nessun file ingrandito**: tolto `telaio-largo-1920`, che era un ingrandimento del 1440. Oltre i 1440 px la fascia del telaio resta larga 1440 e centrata, come i tubi. Ogni file servito è al massimo grande quanto il suo taglio nell'originale.
- **Lo stabilimento**: l'aerea è un quadrato di 421 px sulle colonne 1-4 accanto al 2018 (prima 755 px). A 768 sta sulle colonne 1-5 accanto ai dati, e a 390 è un taglio 16:9 a filo.
- **La griglia**: testo d'apertura, "Per chi lavoriamo", didascalia del telaio, testo sull'alluminio e blocco dei contatti partono tutti alla colonna 7 (x 732 a 1440). La colonna 6 resta solo alla tabella dei trattamenti.
- **La testata sotto i 1024**: a 768 ci sono le quattro voci, e ci stanno da 681 px in su. Sotto i 680 px resta "Trattamenti" accanto a "Scriveteci" e al telefono. Le voci non vanno più a capo e l'area da toccare è alta 44 px.
- **Le righe spente**: il grigio spento ora è #767A80, cioè 3,5:1 sul campo alluminio (prima 2,7:1).
- **L'esito del filtro**: ora dice "Scegliete di nuovo lo stesso metallo per vederli tutti.", che va bene sia col dito sia col mouse.
- **Il testo d'apertura**: "Di titanio e alluminio. Poi Type II, passivazione, brillantatura e sabbiatura, su minuteria di precisione per il medicale e l'industria. Il reparto è a Tombelle di Vigonovo, in provincia di Venezia." La Type II non manca più.
- **Le indicazioni**: sotto l'indirizzo c'è il link "Indicazioni stradali" a Google Maps.

**Non applicato, con il motivo**
- **Aprire su un solo pezzo di titanio scontornato al posto del telaio, con il titolo "Sul titanio il colore è uno spessore"**: il committente ha scelto questa bozza e ha chiesto di non ripensare la prima schermata, quindi titolo e fascia restano. Ho fatto quello che sta dentro l'idea: i palloncini al posto delle pillole e il colore due schermate prima.
- **Due punti veri per punto CSS a DPR 2 su telaio e minuteria**: il limite è nelle foto. La parte nitida del telaio è larga 1440 px e il gruppo della minuteria 1100 px, e ingrandirle sarebbe peggio. A DPR 2 telaio e minuteria hanno 1 punto vero per punto CSS, i tubi 1,5 e l'aerea 2,3. Al telefono sono tutte a 2 o più (`_prova/controlli/verifica.txt`). Per il resto servono le foto rifatte dal vero (vedi LEGGIMI).
- **Il telaio in gabbia a 1312 px**: a 1440 resterebbe comunque a 1:1, e la fascia da bordo a bordo è la prima schermata scelta. Oltre i 1440 non si allarga più.

## La chiusura: la scala del titanio e la targhetta

Il committente ha notato che quasi tutte le home della campagna finivano allo stesso modo: un titolo di luogo, il telefono gigante su una fascia scura, una riga di colonnine con indirizzo, email e orari, poi un piede scuro a quattro colonne. Anche qui il piede era grafite a quattro colonne (logo, sede legale, stabilimento, email), e i recapiti erano una pila di righe sotto il 2018. Ora la chiusura nasce dal mestiere, ed è un oggetto solo.

**Cosa c'è** (`chiusura-1440.jpg`, dall'inizio della sezione del reparto alla fine della pagina):
- l'aerea dello stabilimento e il 2018 restano dove erano, con le stesse parole;
- sotto il 2018, alla colonna 7 come gli altri testi, c'è la scala dei colori che il titanio prende man mano che l'ossido cresce: Naturale, Oro, Blu, Rosa, quattro barrette in fila dall'alto, ognuna col suo foro come un provino appeso al telaio;
- l'ultima barretta, la verde, è una targhetta anodizzata con quattro fori agli angoli. Porta "Stabilimento", Viale Serenissima 15, "Zona artigianale, 30030 Tombelle di Vigonovo (VE)", "Indicazioni stradali" (Google Maps), poi un filetto inciso e sotto il telefono 049 503240 a 40 px (collegamento `tel:`, sottolineato) e l'email (`mailto:`);
- a sinistra, sotto l'aerea e allineato in basso con la riga del telefono, c'è "Scriveteci o chiamate" con "Per un preventivo mandate disegno, materiale e quantità.";
- il piede è una riga sola sul bianco, sopra un filetto grigio: Antonio Bertolin Srl, la sede legale di Padova, la P.IVA e "Privacy" a destra. La PEC non c'è perché non la conosciamo (domanda 13 del LEGGIMI).

**Perché questa**: la pagina racconta che sul titanio il colore è uno spessore. La scala lo mostra un'ultima volta, senza foto, e l'ultimo gradino diventa la targhetta che un'officina di trattamenti consegnerebbe davvero. L'ordine delle barrette è quello in cui i colori compaiono al crescere dell'ossido (il secondo oro, che sul titanio torna dopo il blu, è lasciato fuori per tenere la scala semplice). Non ci sono nanometri sulle barrette: in pagina c'è solo il campo da 0 a 400 nm, e dare un valore a ogni colore sarebbe un dato nuovo.

**Cosa è stato tolto**: il piede grafite a quattro colonne col logo bianco (ora c'è solo la riga), il telefono e l'email ripetuti nel piede, il titolo con l'indirizzo e la pila di righe dei recapiti sotto il 2018. Non ci sono fasce scure né colonnine uguali. I dati sono gli stessi di prima: nessun recapito nuovo, il fax resta fuori.

**Alle varie larghezze**:
- a 1024 la scala sta sulle colonne 6-12 come gli altri testi, e sulla targhetta telefono ed email vanno uno sotto l'altro;
- a 768 l'aerea e il 2018 restano affiancati, poi "Scriveteci o chiamate" e la scala a tutta gabbia;
- a 390 e 320 tutto va in colonna; "Serenissima 15" non si spezza e il piede va su tre righe a 390, su quattro a 320.

## Caratteri e colori

**Carattere**: Mona Sans (GitHub, distribuito da Google Fonts), una sola famiglia variabile.
- Usi:
  - i titoli sono a larghezza 112 % e peso 430, con interlinea 0,92 e spaziatura -0,035em sul titolo grande;
  - il testo è a larghezza 100 % e peso 400, a 18 px;
  - le misure dei trattamenti sono a 30 px, larghezza 112 %.
- Riferimenti: il titolo leggero e spaziato di Medartis (impianti in titanio) e la pulizia di Ressence, nella sezione 7 dell'analisi.
- File: serviti dalla pagina in `sito/fonts/` (`monasans-latin.woff2`, `monasans-latin-ext.woff2`).
- Licenza: SIL Open Font License 1.1, il cui testo è in `sito/fonts/OFL-Mona-Sans.txt` (scaricato da github.com/google/fonts). Uso commerciale libero; "Mona" è un nome riservato, quindi i file non vanno modificati e poi ripubblicati con quel nome.
- Attenzione: Mona Sans è anche il carattere di testo della home di Paraga Pelli, nella stessa zona. Qui la differenza è nei titoli semi-espansi.
- Le cifre sono allineate e proporzionali. Le tabellari di Mona Sans hanno lo zero barrato da monospazio e darebbero l'aria da codice che la guida sconsiglia. Le misure stanno una per riga e allineate a destra, quindi non serve incolonnarle.

**Colori**:

| Colore | Uso |
|---|---|
| bianco #FFFFFF | la pagina |
| alluminio naturale #E6E7E8 | il solo campo pieno, i trattamenti |
| grafite #1C1E21 | testo, anche sulla targhetta |
| grigio #565A60 | le note |
| spento #767A80 | i trattamenti che non valgono per il metallo scelto (3,5:1 sul campo) |
| oro #8F6B1D | solo al passaggio sui link |

Il colore pieno lo danno le foto dei pezzi anodizzati e, nella chiusura, la scala del titanio: cinque tinte piatte prese dai pezzi in foto e scelte per il contrasto del testo che portano.

| Barretta | Tinta | Testo sopra |
|---|---|---|
| Naturale | #BDBBB6 | grafite, 8,7:1 |
| Oro | #D9AA3F | grafite, 7,8:1 |
| Blu | #1F5FAE | bianco, 6,4:1 |
| Rosa | #B9406F | bianco, 5,2:1 |
| Verde, la targhetta | #5DBDB0 | grafite, 7,5:1 |

Non ci sono gradienti, ombre o vetri.

## L'interazione

È una sola: "Il pezzo è in alluminio, titanio o acciaio?", sopra l'elenco dei sei trattamenti.
- Un tocco spegne in grigio i trattamenti che non valgono per quel metallo. Quelli che restano accesi sono 2 per l'alluminio, 5 per il titanio e 2 per l'acciaio, secondo le schede del sito.
- Una riga sotto dice l'esito, per esempio "Per l'alluminio: 2 trattamenti su 6. Scegliete di nuovo lo stesso metallo per vederli tutti."
- Un secondo tocco sullo stesso metallo riaccende tutto.
- Sono bottoni veri con `aria-pressed`, alti 44 px, e l'esito è letto dai lettori di schermo (`aria-live`).
- Provata da `finale_shoot.mjs` col dito a 390, 320 e 768 e con Invio e Spazio a 1440, 1024 e 1920. `verifica_finale.mjs` la prova anche partendo da capo con il solo Tab (10 Tab per arrivare a "titanio", poi Invio e Spazio) e col dito su "acciaio" a 390.
- Cambia solo il colore, in 0,12 s. È l'unico gesto della pagina: i palloncini sul telaio non si toccano, sono disegno. Non ci sono dissolvenze, animazioni allo scorrere o effetti che seguono il cursore.

## Foto: origine e licenza

Tutte le foto in pagina sono di Antonio Bertolin Srl, scaricate dal loro sito il 19/10/2026 (`assets/originali/`, inventario in `_prova/inventario-immagini.json`). Non ci sono foto di repertorio né immagini generate. Lavorate da `_prova/script/finale_img.py`, esportate in JPEG, in più larghezze per `srcset`.

| In pagina | Originale (voto qualità/apertura) | Lavorazione |
|---|---|---|
| `telaio-largo` 960/1440 | `DSC_0029-scaled.jpg` (6/6) | taglio 1:1 sulla parte a fuoco (x 0-1440), fondo schiarito e lisciato, saturazione 0,85. Nessun ingrandimento: oltre i 1440 px la fascia resta larga 1440 |
| `telaio-alto` 390/780/1060 | lo stesso | verticale 4:5 sulle prime due file, a 1:1 |
| `minuteria` 550/825/1100 | `minuteria-medicale-scaled.jpg` (6/7) | bianchi puliti, taglio stretto sul gruppo centrale (x 600-1700, y 300-1340) |
| `tubi` 720/1440/2180 | `acciaio-scaled.jpg` (6/5) | solo i tubi, senza la base con la scritta rossa, polvere tolta |
| `reparto` 480/720/960 e `reparto-largo` 400/800/1280 | `foto_aerea_bertolin-scaled.jpg` (6/3) | verde spento a 0,6; quadrato accanto al 2018, 16:9 al telefono |
| `logo.svg` (in linea) | `logo-footer-bertolin.png` | contorni ridisegnati con `logo_svg.py`. Serve il vettoriale vero |

Le foto Unsplash e Pexels di `assets/esterne/` non sono usate. Quali foto vanno rifatte dal vero, e come, è scritto nel `LEGGIMI.md`.

## Le ispirazioni del committente (Pelletteria Graziella, Studio N19)

Le ho usate per un solo tratto, ed è una scelta. Antonio Bertolin è un'officina di trattamenti di superficie per il medicale e l'industria, non un marchio di moda o del lusso.
- Di Studio N19 resta il fondo chiaro con un titolo molto grande e tanta aria intorno. È quello che fa l'apertura.
- Di Pelletteria Graziella non c'è niente: il nero pieno, la serif col corsivo e il tono da maison sono fuori registro per un'officina che lavora per il medicale.

Il registro viene dal mestiere: la foto di reparto, i palloncini e la distinta del disegno meccanico, le misure vere, i colori che il sito dichiara.

## Controlli

Tutti rifatti dopo la rifinitura, con `build_finale.sh`.
- **Scorrimento orizzontale**: nessuno. `scrollWidth` è uguale a `innerWidth` su 21 larghezze da 320 a 2560 (`verifica_finale.mjs`).
- **Larghezze guardate a pezzi** con `slice.py`: 1440 e 390 (consegna), 320, 768, 1024 e 1920 (`_prova/controlli/`). Nessun elemento esce dalla finestra, nessun testo si sovrappone a un altro e nessuna legenda o palloncino esce dalla sua foto.
- **La chiusura**, rifatta: guardata a pezzi con `slice.py` a 1440, 1024, 768, 390 e 320 (`_prova/controlli/chiusura-*.jpg`). Nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun foro sopra il testo. Contrasto misurato da `verifica_finale.mjs` sul fondo vero di ogni testo: minimo 5,2:1 (Rosa, bianco sul rosa), la targhetta 7,5:1, il piede 6,9:1. Altezza da toccare: telefono 50 px, email 44 px, indicazioni 47 px.
- **Collegamenti**:
  - `tel:+39049503240` in testata e sulla targhetta (50 px di altezza da toccare);
  - `mailto:info@bertolinantonio.it` in testata ("Scriveteci") e sulla targhetta;
  - "Indicazioni stradali" porta a Google Maps su "Viale Serenissima 15, 30030 Tombelle di Vigonovo VE";
  - "Privacy", nella riga del piede, porta alla pagina del sito di oggi.
- **Interazione**: tastiera (Tab, Invio, Spazio) a 1440, 1024 e 1920; dito a 390, 320 e 768. Esiti in `verifica.txt` e nel registro della build.
- **Misure del giudice**:
  - i cinque testi spostati partono a x 732 a 1440;
  - tra il titolo del colore e il suo paragrafo ci sono 36 px;
  - l'aerea è larga 421 px;
  - sopra y 900 l'unica immagine larga 1440 è il telaio, per scelta del committente.
- **Testo**:
  - nessun U+2014 in pagina, script, LEGGIMI, NOTA e CREDITI;
  - nessun segnaposto;
  - nessuna nota di lavorazione a vista.
- **Segnali da IA** (`_prova/controlli/segnali/`, strumento del kit a 1440): 0 soglie bloccanti e 0 da guardare.

| Soglia | Valore |
|---|---|
| Area foto | 35,1 % |
| Famiglie di caratteri | Mona Sans al 100 % |
| Monospazio | 0 % |
| Etichette maiuscole | 0 |
| Misure di H2 | 3 (64, 40, 34 px) |
| Fasce di fondo | 3 |
| Filetti | 13 |
| Frecce | 0 |
| Numeri grandi | 1 (2018) |
| Contenuto datato | 2018 |
| Divieti | nessuno |

- **A occhio**: niente badge, tre box con icona, corsivo d'accento, card col bordo sinistro, glassmorphism o gradienti.
- **Peso della cartella `sito/`**: 1,8 MB.
