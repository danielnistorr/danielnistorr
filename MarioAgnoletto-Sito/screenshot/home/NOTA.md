# Home finale di Mario Agnoletto, "Tavola dei campioni": nota

Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (WebP in più larghezze, tre SVG), carattere in `sito/fonts/`. La pagina non chiede nulla ad altri domini. Tutto si rifà con `bash _prova/script/build_finale.sh`: maschere (se mancano), immagini, logo, pagina, controlli, segnali e screenshot.

Screenshot (JPEG 85):
- `home-1440.jpg` e `home-390.jpg`: pagine intere;
- `home-1440-prima-schermata.jpg` (1440x900) e `home-390-prima-schermata.jpg` (390x844);
- prime schermate anche a 320x640, 768x1024, 1024x768 e 1920x1080 (`home-<larghezza>-prima-schermata.jpg`);
- `filtro-1440-zama.jpg`, `filtro-390-ottone.jpg`: la tavola filtrata; `menu-1024.jpg`: la tendina aperta.

## L'idea

La home è un campionario d'archivio dell'incisore: i pezzi stanno sul cartone grigio, numerati e con la legenda, come nella tavola di un catalogo.
In apertura c'è un loro tacco gioiello a lamelle in ottone, scontornato e posato sulla pagina, così grande che esce dai bordi. Il monogramma MA del logo è battuto sulla punta del pezzo come un marchio di controllo.
Il gesto è il filtro per metallo: scegli zama, ottone, alluminio o acciaio e in tavola restano solo i campioni fatti in quel metallo.

La prima schermata è quella del prototipo B che il committente ha approvato: stessa composizione, stesso carattere, stessi colori. In quest'ultimo giro sono cambiati esecuzione, foto, dati e telefono.

## Cosa è cambiato in quest'ultimo giro

Dal giudizio cieco (48/80), con la prima schermata tenuta com'è per scelta del committente.

**Prima schermata**
- Il timbro MA non galleggia più nel vuoto tra testo e pezzo: è battuto sulla punta dell'anello, a 1440 come a 390. La posizione la calcola lo script delle immagini su un punto del pezzo, come i richiami.
- La legenda non usa più "Tav. 1", che è il sistema della home di Hambro. Ora porta il numero di catalogo del campione: "01, Tacco gioiello a lamelle in ottone". 01 è proprio la lavorazione "Tacchi gioiello" della tavola. Le sezioni sotto sono indicate con le lettere A, B, C, D, come gli alfabeti dei punzoni.
- Il richiamo "Asola d'innesto" diventa "Asola": la parola descrive solo quello che si vede. Il richiamo "Anello" ora indica il bordo dell'anello e lascia la punta al timbro.
- Tra 601 e 900 px il pezzo è largo al massimo 430 px: a 768x1024 il bottone "Chiama" finisce a 968 px, dentro la prima schermata (prima a 1157). Il pezzo non si deforma più e la legenda non esce dal bordo.

**Campionario (A)**
- Tutti i campioni sono scontornati dalla loro foto e posati sullo stesso cartone, con la stessa ombra corta del tacco d'apertura. Prima c'erano tre fondi diversi (tappetino grigio, pelle stampata, tessuto nero).
  - I pezzi restano dove sono nella foto. Dove la foto li taglia, il taglio cade sul bordo della casella.
  - L'unica eccezione è "Stampa e foratura su pelle": lì la pelle è il prodotto, quindi resta foto intera.
- Il campione 01 non ripete più il pezzo d'apertura. È la gabbia in acciaio della stessa foto, da sola, girata in verticale nella casella grande. Il tacco a lamelle e il tacco cromato sono stati tolti.
- La casella grafite "Vetrina" delle targhe, un segnaposto a vista, è stata tolta. Le targhe stanno nel testo: "In tavola ce ne sono sette; l'ottava sono le targhe da esposizione, in alluminio, ottone e plexiglas." Il titolo "Otto lavorazioni, quattro metalli" resta vero.
- Ogni campione ha la sua riga descrittiva, anche a 390.
- Gli attributi `sizes` tengono conto della griglia a due colonne tra 601 e 900 px. Ogni campione è esportato fino alla risoluzione vera della foto: 700-1080 px i piccoli, 660x1000 la gabbia, 1180 e 960 i larghi.
- **Filtro.** Con un metallo scelto, in tavola restano solo i campioni accesi, tutti della stessa misura. Gli altri scendono in una riga di caselle piccole col numero e il nome ("Non in zama: 01 Tacchi gioiello, 02 ...").
  - Con Zama la sezione è alta 1075 px, cioè 1,19 volte la finestra a 1440x900. Prima c'erano 7 caselle vuote, alte fino a 809 px.
  - Scegliere un metallo aggiorna l'indirizzo (`#metallo=ottone`). L'indirizzo viene letto anche a pagina aperta, con `hashchange`.

**Dal disegno alla serie (B)**
- La foto di repertorio delle minuterie zigrinate (che non sono un loro prodotto) è stata tolta. Al suo posto, sotto "Serie", ci sono due pezzi loro dalla foto 13: una fibbia a catena cromata e una placca in ottone con l'inserto martellato.
- La fresa resta l'unica foto di repertorio della pagina. La didascalia lo dice ("Foto di repertorio") e lo ripete il piede.

**Punzoni (C)**
- La foto di repertorio di Jos Zwaan è stata tolta. A tutta larghezza c'è ora la foto 2 del loro sito: ottone inciso, con un cliché a foglie, due bordi a spina e un blocchetto forato sopra una lastra traforata. È il materiale più caldo che hanno, e la didascalia lo descrive.
- Nel cartellino c'è il dritto e rovescio dell'analisi: il monogramma MA in grafite, a specchio ("Sul punzone, a rovescio"), e lo stesso in rosso, leggibile ("Sulla pelle, dritto").

**Testata, contatti, piede**
- Il link "Metalli", che portava nello stesso punto di "Lavorazioni", è stato tolto dal menu. Al suo posto c'è "Punzoni" (#punzoni).
- Sotto i 1240 px il menu sta a destra accanto al telefono, e la tendina si apre sotto il suo comando. Si chiude scegliendo una voce, con Esc (il focus torna su "Menu") e toccando fuori.
- Privacy, Cookie ed English, che erano link morti, sono stati tolti dal piede: vanno rimessi con le pagine vere (vedi LEGGIMI).
- Nei recapiti l'etichetta "Dal 1979" diventa "Ditta". Il 1979 resta, in piccolo, nell'apertura e nel piede, ed è nel LEGGIMI tra i dati da confermare.

## Le prime due schermate

1. **Apertura.**
   - A sinistra "Incisore meccanico" in Host Grotesk 300 a 136 px (fino a 152 sopra i 1600 px). Sotto: la frase con cosa fanno, il bottone "Chiama 049 98 00 985", "Tombelle di Vigonovo (VE), dal 1979" e, in basso, la legenda "01".
   - A destra il tacco, alto quanto la finestra, con il timbro sulla punta e quattro richiami numerati con il filetto: 1 Anello, 2 Lamelle, 3 Asola, 4 Stelo.
   - A 390 il pezzo è ruotato di 90 gradi: entra dal bordo alto, tra il logo e "Menu", ed esce dal bordo sinistro. Sotto ci sono titolo, frase e bottone.
2. **Campionario (A).** Titolo, filtro con i campioni di colore dei metalli e il conteggio, poi la tavola. In alto la gabbia in grande e quattro piccoli (punzoni, fustelle, ruote, bigiotteria), sotto due larghi (accessori, stampa su pelle). Ogni campione ha numero, nome, metalli e una riga presa dal sito.

Seguono "Dal disegno alla serie" (dittico a tutta larghezza), "Punzoni anche in 24 ore" (foto a tutta larghezza con il cartellino), "Dove siamo" (l'unico fondo scuro) e il piede con i dati societari.

## Caratteri e colori, con il riferimento

- **Host Grotesk** (Element Type, SIL Open Font License 1.1, da Google Fonts). Una sola famiglia, woff2 variabile 300-800, sottoinsieme latino, servito dalla pagina in `fonts/`.
  - Riferimento: **De Castelli** (metallo lavorato), che usa Gramatika, un grottesco quieto. Host Grotesk ha le cifre tabellari: telefoni, numeri di catalogo e P.IVA si allineano.
  - Pesi: 300 per i titoli, 400 per il testo, 500 per i nomi dei campioni, i numeri dei richiami e i bottoni.
- **Cartone #E7E4DD** come fondo, **#DCD8CF** per le caselle dei campioni, **grafite #2A2A28** per testo, bottoni, filetti e contatti.
- **Rosso #C8102E**, preso dal logo: solo il timbro MA, il punto sui campioni accesi dal filtro e il passaggio sui link.

## Interazione, provata

Script `_prova/script/finale_filtro.mjs`, risultati in `_prova/finale/filtro.txt`.
- Tastiera a 1440: Tab su Zama e Invio dà "Zama: 1 lavorazione su 7" e l'indirizzo `#metallo=zama`; Tab fino ad Acciaio e Spazio dà 5 su 7. Il focus si vede.
- Indirizzo cambiato a pagina aperta (`#metallo=ottone`): la tavola passa a 4 su 7.
- Dito a 390: Ottone dà 4 su 7. I bottoni sono alti 44 px.
- Pagina aperta con `#metallo=alluminio`: 3 su 7.
- Menu a 1024: si apre sotto il comando (tendina 619-839 px, comando 801-839), si chiude al clic su una voce e con Esc.
- L'unica transizione è quella di 160 ms sul colore del bottone toccato. Non ci sono animazioni allo scorrimento, effetti che seguono il cursore o bottoni che sbiadiscono.

## Foto, origine e licenza

| File in `img/` | Origine | Licenza | Dove |
|---|---|---|---|
| `tacco-l-*`, `tacco-p-*` | foto 12 del sito (`photos_large_12.jpg`), tacco a lamelle in ottone, scontornato | dell'azienda, da usare col suo permesso | apertura |
| `t-tacchi-*` | foto 12, gabbia in acciaio, scontornata e girata di 90 gradi | come sopra | campione 01 |
| `t-punzoni-*`, `t-fustelle-*`, `t-ruote-*` | foto 1: cliché col cavallo, stampo a due fiori, ruota forata, scontornati. Il quadrotto col monogramma a rovescio è tolto | come sopra | campioni 02, 03, 04 |
| `t-bigiotteria-*` | foto 17, farfalle traforate, scontornate | come sopra | campione 05 |
| `t-accessori-*` | foto 13, due fibbie in ottone, scontornate. La fibbia con la scritta e il pezzo col motivo che ricorda un marchio sono fuori quadro | come sopra | campione 06 |
| `t-stampa-*` | foto 15, pelle argento goffrata e cuoio stampato a rilievo | come sopra | campione 07 |
| `finiture-*` | foto 13, fibbia a catena e placca martellata, su pelle stampata | come sopra | B, Serie |
| `ottone-*` | foto 2, ottone inciso e lastra traforata | come sopra | C, Punzoni |
| `fresa-*` | Unsplash pl95tzT0f7Y, mastars MT | Unsplash License | B, Prototipo (segnaposto) |
| `logo.svg`, `timbro.svg`, `timbro-grafite.svg` | ricalco in SVG del `logo.png` del sito (500x100) | marchio dell'azienda | testata, piede, timbro, dritto e rovescio |

Nessuna foto della serie di Ruan Richard Rodrigues (riservata a Hambro): lo script delle immagini si ferma se ne trova una. Nessuna immagine generata dall'IA.

**Scontorni.**
- Le maschere vengono da BiRefNet lite (rete di segmentazione, licenza MIT, modello in `_prova/crawl/modelli/`). Gli script sono `finale_scontorno.py` per il tacco e `finale_scontorno_campioni.py` per i campioni.
- Il modello non genera pixel: dice solo quali pixel sono metallo. Il colore resta quello della foto.
- Poi, con PIL e OpenCV: si tengono solo i pezzi scelti (indicati da un punto), il bordo si stringe di un pixel e prende il colore del metallo vicino, si applica la gradazione comune e un'ombra corta in due strati, larga e di contatto.

**Trattamento comune** (PIL): saturazione all'80 %, curva a S leggera, neri sollevati a 14, luci contenute a 246, tono appena caldo, maschera di contrasto. Ogni foto ha 2-4 larghezze servite con srcset.

## Controlli

- **Scorrimento orizzontale**: scrollWidth uguale a innerWidth da 320 a 2560 px, provato ogni 20 px fino a 1300 e ogni 80 px oltre (`finale_controlla.mjs`).
- **Sovrapposizioni**: nessuna tra testi, richiami, timbro, bottoni e didascalie, alle stesse larghezze.
  - A 320 il timbro scende a 58 px e il logo a 140 px, così non toccano il richiamo "Anello" e lo stelo.
- **Prima schermata a 768x1024**: il bottone finisce a 968 px. A 601 finisce a 828 px, a 900 a 990 px.
- **Nitidezza** (`finale_nitidezza.mjs`): a 768 con DPR 2 il browser sceglie il file più grande disponibile per ogni casella. I campioni piccoli hanno almeno 700 px per 686 px di schermo.
  - Restano sotto 2x solo le foto la cui risoluzione vera è più bassa: il tacco d'apertura (744 px), la gabbia (660), la stampa su pelle (960) e le finiture (670). Si risolve solo con le foto nuove (vedi LEGGIMI).
- **Guardate a pezzi**: le pagine intere a 1440, 1024 e 390; le prime schermate a 320, 390, 768, 1024, 1440 e 1920; i filtri Zama, Acciaio e Ottone; il menu aperto a 1024.
- **Collegamenti**: `tel:+390499800985` (testata, apertura, cartellino, contatti), `mailto:info@marioagnoletto.it`, `mailto:marioagnoletto@pec.it`, Google Maps su "Via dell'Artigianato 18 Tombelle di Vigonovo", ancore #lavorazioni, #serie, #punzoni, #contatti. Nessun link a "#" a parte il logo, che riporta in cima.
- **Lineette lunghe (U+2014)**: zero in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- **Errori in console e file mancanti**: nessuno.
- **Segnali da IA** (`segnali.sh`, home a 1440, rapporto in `_prova/finale/segnali/`): 0 soglie bloccanti.
  - Foto al 52 % della pagina, una sola famiglia, monospazio 0 %, 2 filetti larghi, 0 frecce, 2 fasce di fondo.
  - Da guardare, e voluti:
    - H2 di due misure (66 e 48 px): una misura grande più il cartellino.
    - Numerazione 01-07 (più lo 01 della legenda): è il numero di catalogo dei campioni, l'idea stessa.
    - 5 gradienti: i campioni di colore dei metalli nel filtro.

## Critico severo

- Il pezzo d'apertura è vero e li distingue, ma è una foto da telefono: a 1440 su uno schermo ad alta densità si vede che viene da 1920x1080, e l'ottone grezzo ha qualche macchia. Non è stato ritoccato, perché i pixel aggiunti sarebbero inventati. Solo lo scatto vero lo risolve.
- Il giudice chiedeva di rifare l'apertura sul dritto e rovescio. Non è stato fatto, perché il committente ha scelto questa prima schermata. Il dritto e rovescio ora è nella sezione C.
- A 768 la metà destra della prima schermata resta cartone libero sotto il telefono: è il prezzo di avere il bottone nella prima schermata senza rimpicciolire il titolo.
