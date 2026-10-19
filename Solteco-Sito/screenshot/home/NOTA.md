# Solteco, home finale: "Quello che non si vede"

Versione finale costruita sulla bozza B, scelta dal committente. La prima schermata, l'idea, il trattamento delle foto, il carattere e i colori sono quelli della B; sono cambiati l'esecuzione, i dati non verificati, la lunghezza e le sezioni che il giudice aveva segnalato come deboli.

File: `sito/index.html` (statico, si apre anche come file:///), `sito/img/` (20 JPEG, tre foto in più larghezze), `sito/fonts/` (Host Grotesk e la licenza `OFL.txt`). Si rigenera tutto con `sh _prova/script/build_finale.sh tutte`, che rifà le immagini (`finale_b_img.py`), copia la pagina (`finale_b_index.html`) e scatta le schermate. La prova del gesto è `prova_interruttore_finale.mjs`.

Schermate: `home-1440.jpg` (5490 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5703 px), `home-390-prima-schermata.jpg` e `chiusura-1440.jpg` (solo i contatti e il piede, 927 px).

## L'idea

Il lavoro di Solteco finisce in una riga di un millimetro: il punto in cui la tomaia è incollata alla suola. Se l'incollaggio è fatto bene, quella riga non si nota. L'apertura mostra proprio quella riga in macro, su grafite caldo, con un punto e un filo che la indicano. Il titolo dice la stessa cosa: "La colla buona non si vede". Il resto della pagina è chiaro e racconta il come: i quattro passaggi del reparto, acqua o solvente con la scheda della linea AquaGum P/030 e il marchio Frabo accanto, i contatti. Il nero sta solo nella prima schermata: anche il piede ora è chiaro.

## Le prime due schermate

1. **Apertura** (come nella B): fondo grafite #171615 e testata con nome, tre voci, email e telefono. Il titolo è a 132 px (da 94 a 132 px secondo la finestra) su due righe a sinistra; a destra tre righe dicono chi è Solteco e cosa fa. La punta della scarpa entra dal basso e sfuma nel fondo; il filo porta alla legenda "Qui la tomaia è incollata alla suola", allineata al margine della griglia anche a 1920. A 390 la composizione è la stessa in verticale: titolo e testo in alto, la scarpa intera di punta (guardolo, occhielli) e la legenda in basso, il telefono in testata.
2. **Processo**: si passa alla carta #EDEBE6. Il titolo è "Dalla suola alla pressa, in quattro passaggi", seguito da una sola frase dal sito di Solteco: "Con AquaGum, prima della riattivazione, il tunnel cold dry toglie l'acqua dalla colla e l'umidità dalla scarpa". Poi la foto a tutta larghezza (600 px a 1440) della colla stesa a pennello sul bordo del fondo. I quattro passaggi non sono più in quattro colonne strette: sono un indice a righe con filetti (numero, nome a 34 px, una riga di spiegazione).

Poi vengono le suole sul banco a larghezza di griglia e "Acqua o solvente": l'elenco delle quattro categorie e, sotto, la scheda della linea AquaGum P/030 in sette righe. Accanto, nello stesso formato, "Frabo Adesivi" con quattro righe di scheda. Chiude l'etichetta del fusto con i recapiti e, sotto, il piede su una riga (vedi "La chiusura: l'etichetta del fusto").

## La chiusura: l'etichetta del fusto

Il committente ha notato che quasi tutte le home della campagna chiudevano allo stesso modo: titolo, telefono gigante, una riga di colonnine con indirizzo, email e orari, piede scuro a quattro colonne. Anche questa ci cadeva (telefono a 96 px, tre colonnine Email, Sede, Per chi, piede a quattro colonne). Ora la chiusura è un oggetto del mestiere di Solteco: l'etichetta di un fusto di colla.

- A sinistra resta il titolo "Per una scheda tecnica o un problema d'incollaggio"; a destra, dalla colonna 7 come le schede sopra (x 732 a 1440), c'è l'etichetta: carta più chiara #F7F5F1, bordo d'inchiostro da 2 px, filetti d'inchiostro tra i campi. Sotto 900 px il titolo va sopra e l'etichetta prende la larghezza (al massimo 640 px).
- I campi sono quelli di un'etichetta, riempiti con i recapiti veri: in testa il prodotto ("Solteco sas", "Adesivi a base acqua per calzature e pelletteria") chiuso da un filetto spesso 6 px; poi "Telefono" con 331 335 8858 a 64 px (54 a 1024, 44 a 390, 35 a 320), collegamento `tel:` sottolineato; "Email" con `mailto:` e "Distribuito da" con l'indirizzo e "Apri la mappa"; in fondo le righe piccole come le avvertenze di un'etichetta: "Impiego" (calzaturifici e pelletterie), "Linea" (AquaGum di Frabo Adesivi), "Avvertenze" ("Prima dell'uso leggere la scheda tecnica: si chiede per telefono o per email", dal pannello del solvente: le schede si chiedono a Solteco).
- Perché l'etichetta: è l'oggetto che il cliente di Solteco ha davanti in reparto, e una scheda d'etichetta è già il linguaggio della pagina (la scheda di P/030 e di Frabo). Così i recapiti sono l'ultima scheda della pagina, con un bordo che la fa diventare un oggetto, e non un blocco di contatti generico. Un solo oggetto, nessun disegno del fusto, nessun codice a barre o lotto inventato.
- Il piede è una riga sola sulla carta, sotto un filetto d'inchiostro: "Solteco sas di Longhin Giuseppe & C.", "P.IVA e C.F. 04037310275", "REA VE 359812". La PEC non c'è (non trovata) e non c'è ancora una pagina privacy: sono nel LEGGIMI. A 390 e 320 la riga va a capo in due.
- Tolti: il telefono a 96 px, la riga delle tre colonnine (Email, Sede, Per chi), il piede a quattro colonne con indirizzo ed email ripetuti e "Costituita nel 2011" (resta nel blocco di Frabo). Nessun dato nuovo: ogni testo dell'etichetta era già in pagina.
- Contrasti AA sull'etichetta: inchiostro 16:1, testo #3A3834 10,7:1, grigio delle voci #67635C 5,5:1; sul piede il grigio è 5:1 sulla carta. Il cuoio del passaggio sui link è 4,9:1.
- La modifica è in `_prova/script/chiusura_etichetta.py`, già applicata a `finale_b_index.html` (non va rilanciato).

## Cosa è cambiato rispetto alla bozza B

- Tolta ogni nota di lavorazione dalla pagina: "Foto indicativa" non c'è più, né nella legenda né nelle didascalie. Che le foto siano segnaposto è scritto nel LEGGIMI.
- Tolta la frase "Solteco segue la linea dal primo all'ultimo", che andava oltre la fonte.
- Tolte la coppia di foto quadrate (la cardatura e la linea con le sneaker e l'operaio, fuori contesto) e la riga di statistiche in quattro colonne. Le foto sotto l'apertura ora sono due, con lo stesso trattamento.
- La foto del pennello è presa dall'originale grande (4480 px). L'inquadratura è più larga, con la mano, il pennello e il fondo, e i rossi e i rosa del fondo cardato sono riportati verso il cuoio: non sembra più carne. L'apertura viene dall'originale da 4600 px e ha una nitidezza più alta.
- La scheda di AquaGum P/030 viene dalla bozza A, con dati tutti della notizia del 24/01/2016 sul sito di Solteco, e prende il posto delle righe di codici.
- L'interruttore non è più una pillola nera: sono due voci di testo con un filetto da 2 px sotto quella attiva, nel registro dei filetti della pagina.
- Tolta la classe dei numeri tabellari: le cifre di Host Grotesk sono già tutte larghe uguali (650 unità, misurato nel file).
- Contrasti: il grigio delle righe spente è passato da #9C978E (2,4:1) a #85807A (3,3:1, sopra 3:1 per il testo grande); le descrizioni restano in #67635C (5:1).
- Aggiunti il link "Vai al contenuto", il caricamento anticipato del carattere e `fetchpriority` sull'immagine d'apertura.
- Lunghezza: da 6242 a 5886 px a 1440 e da 6679 a 6026 px a 390.
- Le due foto sotto l'apertura hanno lo stesso taglio 2:1 e lo stesso tono. Nella colla al banco (poi sostituita nell'ultimo giro) il tappetino da taglio verde acqua era portato a grafite. Nel pennello il fondo cardato, che desaturato tirava al rosa, è riportato verso l'ambra del cuoio.

## Ultimo giro: cosa è cambiato dopo il giudice cieco

La prima schermata non è stata ripensata, per la scelta del committente (bozza B): idea, macro della giunzione, titolo, carattere e colori restano quelli. Sono cambiati esecuzione, dati, telefono e quota di scuro.

- Titolo d'apertura: `font-size:clamp(94px,9.2vw,132px)`. Da 1181 a 1440 resta su due righe ("La colla buona / non si vede"): 204 px a 1181, 221 a 1280, 236 a 1366, 248 a 1440. Sopra 1180 l'apertura è alta al massimo quanto la finestra (`min(62.5vw, max(100vh, 640px))`), così a 1280x720 la legenda finisce a 636 px, sopra la piega. A 320 il titolo è a 44 px e torna su due righe.
- Colonne destre: processo, categorie, scheda P/030 e Frabo partono tutte dalla colonna 7 (x 732 a 1440, x 522 a 1024, misurato con getBoundingClientRect).
- Interruttore: i due pannelli sono impilati nella stessa cella di griglia e quello spento è `visibility:hidden`. L'altezza della pagina non cambia più (5434 px a 1440 e 5670 a 390, prima e dopo il click e il tap). Il link nel pannello spento non riceve il fuoco.
- Foto del pennello: taglio 2,4:1 sul gesto (pennello, bordo del fondo, le due mani), alta 600 px a 1440, senza la metà destra fuori fuoco.
- La colla al banco di Tarazevich, scura per metà e con una seconda coppia di mani, è sostituita dalle suole di Fernanda Simões (Pexels 13524733), chiare e nitide, a larghezza di griglia (64 px di margine) e non a tutta pagina. Stesso trattamento delle altre.
- Quota di scuro: i pixel con L* sotto 30 sono il 19,7 % della pagina a 1440 (prima circa 43 % come aree scure) e il 16,4 % a 390. Restano scure solo l'apertura e le ombre delle foto; il piede è passato dalla grafite alla carta con un filetto d'inchiostro.
- Telefono in apertura: la foto è scalata di circa 0,7 e mostra punta, guardolo e occhielli con i lacci: a 390x844 si legge "scarpa". Punto della legenda ricalcolato (45 %, 92,3 %).
- Frabo non ha più una sezione: è un blocco accanto alla scheda, sotto gli adesivi, nello stesso formato di P/030 ("Frabo Adesivi", una riga su Solteco e quattro righe di scheda). Tolta la voce "Frabo" dal menu.
- Numero di telefono nei contatti da 136 a 96 px.
- Dati: la scheda si intesta "Linea AquaGum P/030", perché la notizia del 24/01/2016 descrive insieme P/030, P/031 LR, P/035 R e P/075; P/030 da solo è "adesivo poliuretanico monocomponente a base acqua" (Frabo). La frase senza fonte "il reparto ha un passaggio in più" è sostituita da quella del sito di Solteco: "Con AquaGum, prima della riattivazione, il tunnel cold dry toglie l'acqua dalla colla e l'umidità dalla scarpa". Il passo 02 ora dice "La scarpa ne esce pronta per la riattivazione" (dal sito: "rendendo la calzatura pronta per la riattivazione").
- "P/035 R e P/075" non si spezza più: l'ultima riga non resta mai con "P/075." da sola.
- Il trattino largo di Host Grotesk sembrava una lineetta lunga: "Tunnel cold dry" senza trattino, e nel piede "REA VE 359812".
- Piede: tolto "Solteco" ripetuto; resta la ragione sociale in 18 px 500, con "Costituita nel 2011".

Respinto: rifare l'apertura chiara con le suole di Simões scontornate su carta (difetto bloccante del giudice). È la direzione A, che il committente ha scartato scegliendo la B, e la consegna dice che la prima schermata non si ripensa. Il soggetto delle suole a griglia entra comunque nella pagina, come seconda foto.

## Caratteri e colori

- **Host Grotesk** (Element Type), da Google Fonts, licenza SIL Open Font License 1.1, che consente anche l'uso commerciale; il testo è in `sito/fonts/OFL.txt`. È un carattere variabile usato in 400 e 500, e la pagina serve i file woff2 latin e latin-ext. Una famiglia sola. I titoli sono in 400 con spaziatura da -0,02 a -0,045em, il testo è a 19 px con interlinea 1,55. Non è Inter e non è nelle liste della guida.
- Riferimenti: Collano (grande titolo grottesco regolare, parole esatte) per la voce; Kenda Farben per il prodotto chimico mostrato come materia sulla scarpa, in macro e su fondo scuro, senza il suo corsivo e il maiuscolo spaziato; Tek.Lam "Scintilla e spessore" per il registro scuro ma pulito, limitato alla prima schermata.
- Colori: grafite #171615 (solo apertura), carta #EDEBE6, inchiostro #1B1A18, grigio #67635C per le didascalie e le etichette delle schede, filetti #CFCBC3, cuoio #9A5B34 solo per il passaggio sui link e il contorno del fuoco. Il colore vero lo fanno la pelle e la colla nelle foto.

## Interazione

Un solo gesto: "A base acqua / A solvente" sopra le quattro categorie che il sito di Solteco elenca (AquaGum a pennello, AquaGum a spruzzo, neoprenici, poliuretanici). Le righe dell'altra famiglia passano a grigio e sotto cambia il pannello: per l'acqua la scheda di P/030, per il solvente la storia della linea Frabo e le schede tecniche a richiesta. I comandi sono due `button` con `aria-pressed` e un'area di tocco alta 44 px. Il cambio è netto: cambiano solo colore e filetto, in 0,12 s, senza opacità. I due pannelli occupano la stessa cella di griglia, quello spento è `visibility:hidden`: la pagina non cambia altezza e niente salta sotto il dito. Provato con la tastiera (Tab, Invio e Spazio a 1440) e col dito (tap a 390): stato, righe e pannello cambiano come previsto, l'altezza resta 5434 px a 1440 e 5670 a 390, e non c'è scorrimento orizzontale. Non ci sono animazioni allo scorrere né effetti sul cursore.

## Foto

Tutte segnaposto da Pexels, licenza "Free" letta sulla pagina di ogni foto. Nessuna è generata dall'IA e nessuna compare nelle altre home della campagna (dettagli in `assets/CREDITI.md`).

| Dove | Foto | Origine e licenza |
|---|---|---|
| Apertura | punta di una scarpa in pelle, la linea tra tomaia e suola | breakermaximus, Pexels 10855838, licenza Pexels |
| Processo | colla stesa a pennello sul fondo della scarpa montata | Fernanda Simões, Pexels 30725646, licenza Pexels |
| Adesivi | due suole col fondo a griglia sul banco di un calzaturificio, a larghezza di griglia | Fernanda Simões, Pexels 13524733, licenza Pexels |

Il trattamento è quello della B, in `finale_b_img.py`: i blu e gli azzurri sono portati quasi al grigio, i neutri sono scaldati verso la grafite e la curva è morbida. In più, i rossi e i rosa sono riportati verso il cuoio, e c'è una maschera di contrasto dopo ogni riduzione. L'apertura è composta su fondo #171615 con una sfumatura dall'alto. Le immagini sono servite con `srcset` (1440, 2160 e 2880 per l'apertura, 800-2880 per il pennello, 800-2624 per le suole, tagli quadrati per il telefono). Le foto del sito attuale non reggono (fotogrammi di video sotto 1027 px con le scritte impresse, voti 1-3 su 10). Cosa rifare dal vero è scritto nel LEGGIMI.

## Le ispirazioni del committente (Graziella, Studio N19)

Le ho usate pochissimo, e per scelta. Solteco è un agente tecnico di adesivi per calzaturifici, non un marchio di moda: il nero di lusso, il serif e le parole in corsivo di Graziella qui sarebbero fuori registro. Ho preso due tratti: da Graziella il telefono e l'email già nella testata, giusti per un'azienda di una persona che si chiama al telefono; da N19 il grande titolo grottesco con molta aria. Il nero dell'apertura non viene da Graziella ma dalla macro, e dura una schermata. Non ci sono menu a tutta pagina né testi che compaiono.

## Controlli della chiusura nuova

- Chiusura guardata a pezzi a 1440, 1024, 768, 390 e 320: nessuna sovrapposizione, nessun testo fuori dall'etichetta, il telefono non va a capo (scrollWidth del collegamento uguale alla sua larghezza a tutte le misure).
- `scrollWidth` uguale a `innerWidth` a 320, 360, 375, 390, 414, 600, 768, 820, 900, 901, 1024, 1180, 1181, 1280, 1440 e 1920.
- Altezza: 5490 px a 1440, 5703 a 390, 5617 a 320, 5447 a 768, 5002 a 1024, 5915 a 1920. Il gesto non cambia l'altezza (`controlli_ultimo.mjs`, `prova_interruttore_finale.mjs` rilanciati: tutto come prima, colonne a 732 e 522, ancore tutte esistenti).
- Collegamenti nella chiusura: `tel:+393313358858` (area 433x72 px a 1440, 291x51 a 390), `mailto:info@solteco.it`, Google Maps.
- Nessun U+2014, nessun gradiente, ombra di vetro, emoji, icona, badge, bordo sinistro colorato, opacità o animazione nella chiusura.

## Controlli (ultimo giro)

- Schermate guardate a pezzi a 320, 390, 768, 1024, 1440 e 1920, più le prime schermate a 1280x720, 1366x768 e 1024x768: nessuna sovrapposizione, la legenda resta sulla giunzione e sopra la piega.
- `scrollWidth` uguale a `innerWidth` a 320, 340, 360, 375, 390, 414, 600, 700, 768, 820, 900, 1024, 1180, 1181, 1280, 1366, 1440, 1600, 1920 e 2560 (`_prova/script/controlli_ultimo.mjs`).
- Altezza: 5434 px a 1440 (richiesto tra 4500 e 6500), 5670 a 390, 5561 a 320, 5370 a 768, 4995 a 1024, 5835 a 1920.
- Titolo d'apertura su due righe da 320 a 2560; colonne destre allineate (x 732 a 1440, 522 a 1024).
- Interruttore: Tab, Invio e Spazio a 1440, tap a 390; `aria-pressed`, righe e pannello cambiano, altezza della pagina invariata, area di tocco 103x44 px (`controlli_ultimo.mjs` e `prova_interruttore_finale.mjs`).
- Collegamenti: `tel:+393313358858` (testata e contatti), `mailto:info@solteco.it`, Google Maps su "Vicolo Amerigo Vespucci 12 30030 Vigonovo VE", ancore #processo, #adesivi, #contatti tutte esistenti.
- Scuro: pixel con L* sotto 30 il 19,7 % della pagina a 1440, il 16,4 % a 390.
- Segnali da IA (`_prova/segnali-finale/`): 0 soglie bloccanti su 10; foto 37,7 % della pagina. Due voci da guardare, volute: gli H2 hanno tutti la stessa misura (l'elemento grande è il titolo d'apertura) e 01-04 numerano una procedura vera.
- Nessun U+2014 né U+2013 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

## Controlli dei giri precedenti

- Larghezze 320, 390, 768, 1024, 1440 e 1920, guardate a pezzi: nessuno scorrimento orizzontale, nessuna sovrapposizione. La legenda dell'apertura resta sulla linea di colla a tutte le misure.
- Altezza nel giro precedente: 5886 px a 1440, 6026 a 390, 6617 a 1920.
- Corretti nell'ultimo giro: a 320 il titolo del processo usciva di 11 px (ora scende a 33 px sotto i 350 px di finestra); a 1920 la foto della colla si fermava a 1440 px (ora è a tutta larghezza come il pennello); il `srcset` della colla puntava a un file inesistente.
- Gesto provato con `_prova/script/prova_interruttore_finale.mjs` (Tab e Invio a 1440, tap a 390, area di tocco 103x44 px) e larghezze controllate con `_prova/script/largo_finale.mjs` (320, 340, 360, 375, 390, 414: nessun elemento esce dalla finestra).
- Segnali da IA (`_prova/segnali-finale/`): nessuna soglia bloccante su 10. Due voci sono da guardare: gli H2 hanno tutti la stessa misura, ed è voluto (l'elemento grande è il titolo, il secondo è il telefono); 01-04 numerano una procedura vera.
- Nessun carattere U+2014 nella pagina, negli script e in questi file. Nessuna nota di lavorazione a vista. Nessuna violazione dei divieti: niente gradienti, badge, box con icona, card con bordo colorato, glassmorphism, dissolvenze allo scorrere.
- Dati: ogni fatto in pagina viene da 01-analisi.md, cioè dal sito di Solteco, da fraboadesivi.com e dai registri. Ciò che è dubbio è nel LEGGIMI e non in pagina.
