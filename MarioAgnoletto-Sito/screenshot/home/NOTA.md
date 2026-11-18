# Home finale di Mario Agnoletto, "Tavola dei campioni": nota

Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (WebP in più larghezze, tre SVG), carattere in `sito/fonts/`. La pagina non chiede nulla ad altri domini. Tutto si rifà con `bash _prova/script/build_finale.sh`: maschere (se mancano), immagini, logo, pagina, controlli, segnali e screenshot.

Screenshot (JPEG 85):
- `home-1440.jpg` e `home-390.jpg`: pagine intere;
- `home-1440-prima-schermata.jpg` (1440x900) e `home-390-prima-schermata.jpg` (390x844);
- prime schermate anche a 320x640, 768x1024, 1024x768 e 1920x1080 (`home-<larghezza>-prima-schermata.jpg`);
- `filtro-1440-zama.jpg`, `filtro-390-ottone.jpg`: la tavola filtrata; `menu-1024.jpg`: la tendina aperta;
- `chiusura-1440.jpg`: solo la chiusura a 1440, dall'inizio della sezione D alla fine della pagina.

Le pagine intere, le prime schermate a 390 e 1440 e la chiusura sono state rifatte dopo il cambio della chiusura. Le altre prime schermate, i filtri e il menu sono del giro prima: la chiusura non vi compare.

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
- Contatti e piede sono stati poi rifatti del tutto: vedi "Chiusura nuova" qui sotto. Il 1979 resta, in piccolo, solo nell'apertura, ed è nel LEGGIMI tra i dati da confermare.

## Chiusura nuova: la sede e una frase loro (stile B, "con foto")

La chiusura è stata rifatta due volte. Prima tutte le home finivano allo stesso modo (titolo del luogo, telefono gigante su fascia scura, colonnine, piede scuro a quattro colonne). Poi ogni home ha avuto un oggetto del mestiere disegnato che portava i recapiti: qui era la scheda d'archivio col timbro MA impresso. Il committente ha bocciato anche quella e, tra i due campioni fatti su Hambro e Bazzato, ha scelto lo stile B, "con foto". Questa è la chiusura in quello stile.

**Cosa c'è ora** (sezione D, "Dove siamo", su cartone come il resto della pagina):
- **A sinistra la foto**, a filo del bordo sinistro della pagina, larga sei colonne: l'ingresso dell'officina a Tombelle di Vigonovo, con l'insegna "Incisore meccanico Mario Agnoletto", la pensilina e le vetrate. A 1440 è 708x763 px.
- **A destra**, in alto, la piccola indicazione "D, Dove siamo", come le sezioni A, B e C. Sotto la frase, grande, in Host Grotesk 300 come gli altri titoli (60 px a 1440, 36-40 px sul telefono):
  - "Seguiamo il pezzo dal progetto alla serie".
  - È presa dalla frase d'apertura ("Seguiamo il pezzo dal progetto alla serie, in zama, ottone, alluminio e acciaio") ed è quella che dice meglio come lavorano: seguono il pezzo del cliente fino alla produzione.
  - Una prima versione in due frasi ("Si parte da un'idea del cliente. Seguiamo il pezzo...") è stata scartata, perché lo strumento dei segnali la segna come titolo in due frasi.
- **A destra, in basso**, i recapiti in quattro righe di testo, senza etichette, riquadri o filetti:
  - il telefono 049 98 00 985 (`tel:`), da 28 a 38 px, alto 48 px;
  - l'email info@marioagnoletto.it (`mailto:`);
  - l'indirizzo "Via dell'Artigianato 18, 30030 Tombelle di Vigonovo (VE)", con "Apri in Google Maps" sotto;
  - "Fax 049 50 31 72", in grafite-2.
  - Orari non ce ne sono: il sito dell'azienda non li dà.
- **Sotto i 900 px** prima vengono la frase e i recapiti, poi la foto a tutta larghezza, quadrata (al massimo 640 px di altezza), che chiude la pagina sopra il piede. Così la sezione C (foto, cartellino, didascalia) non è seguita subito da un'altra foto.
- **Piede**: una riga sola su cartone con un filetto sopra, come prima. Porta ragione sociale (Agnoletto Mario, impresa individuale), P.IVA 00802440271, PEC marioagnoletto@pec.it e la riga sulla foto della fresa di repertorio. La privacy non c'è perché la pagina non esiste ancora (vedi LEGGIMI).

**La foto.** È `assets/originali/photos_large_company.jpg`, la foto della sede pubblicata sul sito attuale dell'azienda (1920x1080). Come le altre foto loro, va usata col loro permesso, che è da confermare. In `sito/img/` diventa:
- `sede-720` e `sede-1020`: riquadro 360,0-1380,1080, verticale, per i larghi;
- `sede-q-480`, `sede-q-780` e `sede-q-1080`: riquadro 300,0-1380,1080, quadrato, per telefono e tablet.

Le fa `finale_img.py` con la stessa gradazione delle altre foto della pagina (saturazione all'80 %, curva a S leggera, neri a 14, luci a 246, tono appena caldo, maschera di contrasto).
- Perché questa: è la foto più nitida che hanno (le foto prodotto sono da telefono, con qualche macchia), è vera, e per "Dove siamo" mostra proprio il posto. L'insegna col monogramma rosso riprende il rosso del timbro.
- La foto sopra la chiusura è l'ottone inciso della sezione C, quindi le due foto sono diverse e non c'è stato niente da spostare.
- Nessuna foto nuova scaricata. Nessuna foto della serie di Ruan Richard Rodrigues.

**Cosa è stato tolto.** La scheda d'archivio con la sua ombra, il doppio filetto, le etichette maiuscole (Telefono, Email, PEC, Fax, Officina), i filetti tra le righe e il timbro impresso (`img/timbro-impresso.svg`). Il file non è più in `sito/img/` e il build non lo rifà più. `finale_timbro_impresso.py` resta tra gli script, ma il build non lo lancia. Tolti anche il colore carta #F4F2ED, il titolo "Tombelle di Vigonovo, nella Riviera del Brenta" e la riga sui clienti ("Lavoriamo soprattutto per calzaturifici e pelletterie...").
- I dati sono tutti quelli di prima: telefono, email, fax, indirizzo e mappa nella chiusura; PEC, ragione sociale e P.IVA nel piede.

**Controlli della chiusura.**
- Guardata a pezzi a 1440, 1024, 768, 390 e 320 (`_prova/script/finale_chiusura.mjs`):
  - a 1440 foto 708x763, testo a destra largo 533 px;
  - a 1024 foto 503x560, testo largo 379 px;
  - a 768, 390 e 320 la frase e i recapiti stanno sopra, poi la foto a tutta larghezza (768x640, 390x390, 320x320).
  - La frase va a capo così: "Seguiamo il pezzo / dal progetto / alla serie" sui larghi, "Seguiamo il pezzo / dal progetto alla serie" sul telefono.
- Nessuno scorrimento orizzontale da 320 a 2560. `finale_controlla.mjs` ora guarda anche l'indicazione D, ogni riga dei recapiti, la foto e il piede: nessuna sovrapposizione.
- Contrasto AA su cartone:
  - grafite #2A2A28 11,3:1 (frase, recapiti);
  - grafite-2 #5B5852 5,6:1 (fax, indicazione D, piede);
  - rosso #C8102E 4,6:1 (solo il passaggio sui link).
- Nessun U+2014, nessun gradiente, nessuna animazione, nessun corsivo, nessuna icona, nessun riquadro.
- Nitidezza: a 1440 con DPR 2 la foto ha 1020 px per 708 px di schermo (1,44x): è la risoluzione vera della foto.

## Le prime due schermate

1. **Apertura.**
   - A sinistra "Incisore meccanico" in Host Grotesk 300 a 136 px (fino a 152 sopra i 1600 px). Sotto: la frase con cosa fanno, il bottone "Chiama 049 98 00 985", "Tombelle di Vigonovo (VE), dal 1979" e, in basso, la legenda "01".
   - A destra il tacco, alto quanto la finestra, con il timbro sulla punta e quattro richiami numerati con il filetto: 1 Anello, 2 Lamelle, 3 Asola, 4 Stelo.
   - A 390 il pezzo è ruotato di 90 gradi: entra dal bordo alto, tra il logo e "Menu", ed esce dal bordo sinistro. Sotto ci sono titolo, frase e bottone.
2. **Campionario (A).** Titolo, filtro con i campioni di colore dei metalli e il conteggio, poi la tavola. In alto la gabbia in grande e quattro piccoli (punzoni, fustelle, ruote, bigiotteria), sotto due larghi (accessori, stampa su pelle). Ogni campione ha numero, nome, metalli e una riga presa dal sito.

Seguono "Dal disegno alla serie" (dittico a tutta larghezza), "Punzoni anche in 24 ore" (foto a tutta larghezza con il cartellino), "Dove siamo" (la sede a sinistra, la frase e i recapiti a destra) e il piede in una riga.

## Caratteri e colori, con il riferimento

- **Host Grotesk** (Element Type, SIL Open Font License 1.1, da Google Fonts). Una sola famiglia, woff2 variabile 300-800, sottoinsieme latino, servito dalla pagina in `fonts/`.
  - Riferimento: **De Castelli** (metallo lavorato), che usa Gramatika, un grottesco quieto. Host Grotesk ha le cifre tabellari: telefoni, numeri di catalogo e P.IVA si allineano.
  - Pesi: 300 per i titoli, 400 per il testo, 500 per i nomi dei campioni, i numeri dei richiami e i bottoni.
- **Cartone #E7E4DD** come fondo, **#DCD8CF** per le caselle dei campioni, **grafite #2A2A28** per testo, bottoni e filetti.
- **Rosso #C8102E**, preso dal logo: solo il timbro MA (sul pezzo e nel dritto e rovescio), il punto sui campioni accesi dal filtro e il passaggio sui link.

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
| `sede-*`, `sede-q-*` | foto della sede del sito (`photos_large_company.jpg`), ingresso dell'officina con l'insegna | dell'azienda, da usare col suo permesso | D, chiusura |
| `logo.svg`, `timbro.svg`, `timbro-grafite.svg` | ricalco in SVG del `logo.png` del sito (500x100) | marchio dell'azienda | testata, timbro, dritto e rovescio |

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
- **Collegamenti**: `tel:+390499800985` (testata, apertura, cartellino, chiusura), `mailto:info@marioagnoletto.it`, `mailto:marioagnoletto@pec.it`, Google Maps su "Via dell'Artigianato 18 Tombelle di Vigonovo", ancore #lavorazioni, #serie, #punzoni, #contatti. Nessun link a "#" a parte il logo, che riporta in cima.
- **Lineette lunghe (U+2014)**: zero in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- **Errori in console e file mancanti**: nessuno.
- **Segnali da IA** (`segnali.sh`, home a 1440, rapporto in `_prova/finale/segnali/`): 0 soglie bloccanti.
  - Dopo la chiusura con la foto: foto al 55,8 % della pagina, una sola famiglia, monospazio 0 %, 0 titoli col punto, 2 filetti larghi, 0 frecce, nessuna fascia di fondo oltre al cartone.
  - Da guardare, e voluti:
    - H2 di tre misure (66, 48 e 60 px): i titoli di sezione, il cartellino e la frase della chiusura.
    - Numerazione 01-07 (più lo 01 della legenda): è il numero di catalogo dei campioni, l'idea stessa.
    - 5 gradienti: i campioni di colore dei metalli nel filtro.

## Critico severo

- Il pezzo d'apertura è vero e li distingue, ma è una foto da telefono: a 1440 su uno schermo ad alta densità si vede che viene da 1920x1080, e l'ottone grezzo ha qualche macchia. Non è stato ritoccato, perché i pixel aggiunti sarebbero inventati. Solo lo scatto vero lo risolve.
- Il giudice chiedeva di rifare l'apertura sul dritto e rovescio. Non è stato fatto, perché il committente ha scelto questa prima schermata. Il dritto e rovescio ora è nella sezione C.
- A 768 la metà destra della prima schermata resta cartone libero sotto il telefono: è il prezzo di avere il bottone nella prima schermata senza rimpicciolire il titolo.
