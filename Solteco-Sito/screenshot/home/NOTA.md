# Solteco, home finale: "Quello che non si vede"

Versione finale costruita sulla bozza B, scelta dal committente. La prima schermata, l'idea, il trattamento delle foto, il carattere e i colori sono quelli della B; sono cambiati l'esecuzione, i dati non verificati, la lunghezza e le sezioni che il giudice aveva segnalato come deboli.

File: `sito/index.html` (statico, si apre anche come file:///), `sito/img/` (19 JPEG, tre foto in più larghezze), `sito/fonts/` (Host Grotesk e la licenza `OFL.txt`). Si rigenera tutto con `sh _prova/script/build_finale.sh tutte`, che rifà le immagini (`finale_b_img.py`), copia la pagina (`finale_b_index.html`) e scatta le schermate. La prova del gesto è `prova_interruttore_finale.mjs`.

Schermate: `home-1440.jpg` (5766 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (6026 px), `home-390-prima-schermata.jpg`.

## L'idea

Il lavoro di Solteco finisce in una riga di un millimetro: il punto in cui la tomaia è incollata alla suola. Se l'incollaggio è fatto bene, quella riga non si nota. L'apertura mostra proprio quella riga in macro, su grafite caldo, con un punto e un filo che la indicano. Il titolo dice la stessa cosa: "La colla buona non si vede". Il resto della pagina è chiaro e racconta il come: i quattro passaggi del reparto, acqua o solvente con la scheda di AquaGum P/030, Frabo e i contatti.

## Le prime due schermate

1. **Apertura** (come nella B): fondo grafite #171615 e testata con nome, quattro voci, email e telefono. Il titolo è a 132 px su due righe a sinistra; a destra tre righe dicono chi è Solteco e cosa fa. La punta della scarpa entra dal basso e sfuma nel fondo; il filo porta alla legenda "Qui la tomaia è incollata alla suola", allineata al margine della griglia anche a 1920. A 390 la composizione è la stessa in verticale: titolo e testo in alto, la punta e la legenda in basso, il telefono in testata.
2. **Processo**: si passa alla carta #EDEBE6. Il titolo è "Dalla suola alla pressa, in quattro passaggi", seguito da una sola frase da reparto: "Con un adesivo a base acqua il reparto ha un passaggio in più: togliere l'acqua dalla colla prima di riattivarla". Poi la foto a tutta larghezza della colla stesa a pennello sul fondo. I quattro passaggi non sono più in quattro colonne strette: sono un indice a righe con filetti (numero, nome a 34 px, una riga di spiegazione).

Poi vengono la colla lattiginosa sul cuoio a tutta larghezza e "Acqua o solvente": l'elenco delle quattro categorie e, sotto, la scheda di AquaGum P/030 in sette righe; il 5 % di CAT/1598 è diventato la settima riga. Seguono "Il marchio è Frabo Adesivi", con un paragrafo e una scheda di cinque righe al posto della riga di statistiche, i contatti con il telefono a 136 px (l'unico numero grande della pagina) e il piede grafite con i dati societari.

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
- Lunghezza: da 6242 a 5766 px a 1440 e da 6679 a 6026 px a 390.

## Caratteri e colori

- **Host Grotesk** (Element Type), da Google Fonts, licenza SIL Open Font License 1.1, che consente anche l'uso commerciale; il testo è in `sito/fonts/OFL.txt`. È un carattere variabile usato in 400 e 500, e la pagina serve i file woff2 latin e latin-ext. Una famiglia sola. I titoli sono in 400 con spaziatura da -0,02 a -0,045em, il testo è a 19 px con interlinea 1,55. Non è Inter e non è nelle liste della guida.
- Riferimenti: Collano (grande titolo grottesco regolare, parole esatte) per la voce; Kenda Farben per il prodotto chimico mostrato come materia sulla scarpa, in macro e su fondo scuro, senza il suo corsivo e il maiuscolo spaziato; Tek.Lam "Scintilla e spessore" per il registro scuro ma pulito, limitato alla prima schermata.
- Colori: grafite #171615 (solo apertura e piede), carta #EDEBE6, inchiostro #1B1A18, grigio #67635C per le didascalie e le etichette delle schede, filetti #CFCBC3, cuoio #9A5B34 solo per il passaggio sui link e il contorno del fuoco. Il colore vero lo fanno la pelle e la colla nelle foto.

## Interazione

Un solo gesto: "A base acqua / A solvente" sopra le quattro categorie che il sito di Solteco elenca (AquaGum a pennello, AquaGum a spruzzo, neoprenici, poliuretanici). Le righe dell'altra famiglia passano a grigio e sotto cambia il pannello: per l'acqua la scheda di P/030, per il solvente la storia della linea Frabo e le schede tecniche a richiesta. I comandi sono due `button` con `aria-pressed` e un'area di tocco alta 44 px. Il cambio è netto: cambiano solo colore e filetto, in 0,12 s, senza opacità. Provato con la tastiera (fuoco e Invio a 1440) e col dito (tap a 390): stato, righe e pannello cambiano come previsto e non c'è scorrimento orizzontale. Non ci sono animazioni allo scorrere né effetti sul cursore.

## Foto

Tutte segnaposto da Pexels, licenza "Free" letta sulla pagina di ogni foto. Nessuna è generata dall'IA e nessuna compare nelle altre home della campagna (dettagli in `assets/CREDITI.md`).

| Dove | Foto | Origine e licenza |
|---|---|---|
| Apertura | punta di una scarpa in pelle, la linea tra tomaia e suola | breakermaximus, Pexels 10855838, licenza Pexels |
| Processo | colla stesa a pennello sul fondo della scarpa montata | Fernanda Simões, Pexels 30725646, licenza Pexels |
| Adesivi | adesivo lattiginoso steso a spatola sul cuoio | Anna Tarazevich, Pexels 5963144, licenza Pexels |

Il trattamento è quello della B, in `finale_b_img.py`: i blu e gli azzurri sono portati quasi al grigio, i neutri sono scaldati verso la grafite e la curva è morbida. In più, i rossi sono riportati verso il cuoio e c'è una maschera di contrasto dopo ogni riduzione. L'apertura è composta su fondo #171615 con una sfumatura dall'alto. Le immagini sono servite con `srcset` (1440, 2160 e 2880 per l'apertura, tagli quadrati per il telefono). Le foto del sito attuale non reggono (fotogrammi di video sotto 1027 px con le scritte impresse, voti 1-3 su 10). Cosa rifare dal vero è scritto nel LEGGIMI.

## Le ispirazioni del committente (Graziella, Studio N19)

Le ho usate pochissimo, e per scelta. Solteco è un agente tecnico di adesivi per calzaturifici, non un marchio di moda: il nero di lusso, il serif e le parole in corsivo di Graziella qui sarebbero fuori registro. Ho preso due tratti: da Graziella il telefono e l'email già nella testata, giusti per un'azienda di una persona che si chiama al telefono; da N19 il grande titolo grottesco con molta aria. Il nero dell'apertura non viene da Graziella ma dalla macro, e dura una schermata. Non ci sono menu a tutta pagina né testi che compaiono.

## Controlli

- Larghezze 320, 390, 768, 1024, 1440 e 1920, guardate a pezzi: nessuno scorrimento orizzontale, nessuna sovrapposizione. La legenda dell'apertura resta sulla linea di colla a tutte le misure.
- Altezza a 1440: 5766 px (richiesto tra 4500 e 6500).
- Segnali da IA (`_prova/segnali-finale/`): nessuna soglia bloccante su 10. Due voci sono da guardare: gli H2 hanno tutti la stessa misura, ed è voluto (l'elemento grande è il titolo, il secondo è il telefono); 01-04 numerano una procedura vera.
- Nessun carattere U+2014 nella pagina, negli script e in questi file. Nessuna nota di lavorazione a vista. Nessuna violazione dei divieti: niente gradienti, badge, box con icona, card con bordo colorato, glassmorphism, dissolvenze allo scorrere.
- Dati: ogni fatto in pagina viene da 01-analisi.md, cioè dal sito di Solteco, da fraboadesivi.com e dai registri. Ciò che è dubbio è nel LEGGIMI e non in pagina.
