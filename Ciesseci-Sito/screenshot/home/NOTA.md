# Home finale Ciesseci (CSC Factory): "Il segno sul capo", con la felpa 82

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `build_img.py`, carattere, screenshot con `shots.mjs`). Pagina alta 5869 px a 1440 (piede compreso), 7876 px a 390.

Base: il prototipo A scelto dal giudice (impianto, Archivo, carta, inchiostro e verde, schede delle tecniche, chiusura, piede). Innesto da B: l'idea del 1982 come numero di maglia, fotografata ed eseguita come in A.

## Idea

Il mestiere di Ciesseci è mettere un segno su un capo. L'oggetto unico è il loro capo: la felpa grigia CSC Factory con "82" stampato in verde fluo e il marchio CSC Factory dentro l'8. È la loro storia (il 1982) stampata come un numero di maglia, e con il nome di un concorrente la pagina non regge: sul capo c'è il loro marchio.

## Le prime due schermate

1. Apertura (1440x900), tutta su carta. A sinistra il loro titolo "Stampa e ricamo: diffondiamo il tuo brand." in tre righe, Archivo a 98 px larghezza 116; sotto le due righe di A, il bottone verde "Chiedi un preventivo" e il telefono 049 634423 (`tel:+39049634423`). A destra la felpa vista dall'alto, scontornata sulla carta con un'ombra di contatto morbida: entra dal bordo destro e da quello basso, il cappuccio è il suo contorno vero. Il verde fluo è l'unica macchia di colore della schermata. In basso, accanto al capo e non sopra la foto, la didascalia "La felpa CSC Factory: il 1982 stampato come un numero di maglia."
2. Lavorazioni: "Su tessuto, plex, legno e metallo", "Undici lavorazioni..." (il conto vero: cinque schede più le sei della riga sotto, grafica compresa), le cinque schede e la foto a tutta larghezza in 2,25:1 con la frase della tecnica.

Seguono: abbigliamento e DPI (foto a filo del bordo sinistro), 1982 grande con la frase dei tre amici e le due date affiancate (1982 Rubano, 2019 Via Zanella 1) con un filetto verde sottile, le quattro righe per chi lavorano, la chiusura e il piede.

A 390: titolo, due righe, bottone e telefono, poi la felpa a tutta larghezza sulla carta, che si vede già nella prima schermata (il cappuccio; l'82 arriva scorrendo, perché lo scatto è verticale).

### Perché la felpa non occupa il 55-60 % della larghezza

L'unico scatto della felpa ripresa dall'alto e piana è `2018-02-csc-factory-26.jpg`, e lì la felpa occupa solo 324 x 680 px sul bordo destro di un flat lay da tavolo. L'altro scatto (`-14`, quello di B) è più grande ma preso di sbieco, con il tessuto tagliato su tre lati: scontornato resterebbe un rettangolo con un angolo tolto, cioè di nuovo "la foto in un box a destra". Ho scelto lo scatto dall'alto e l'ho mostrato a 1,3x (421 x 923 px), il massimo prima che diventi morbido; a 1440 il capo prende circa il 26 % della larghezza e tutta l'altezza. Con lo scatto vero da rifare (sotto) la felpa intera potrà occupare il 55-60 % e uscire dai bordi con le maniche.

## Caratteri e colori

- Una famiglia: **Archivo** (Omnibus-Type, Google Fonts), variabile in peso e larghezza, servita dalla pagina in `sito/fonts/archivo-latin-var.woff2` (sottoinsieme latino, 90 KB). Licenza SIL Open Font License 1.1, uso commerciale libero; il testo è in `sito/fonts/OFL-Archivo.txt`.
- Titoli larghi (wdth 112-118, peso 460-560, spaziatura da -0,02 a -0,03em) come le lettere della coccarda CSC; etichette strette e maiuscole (wdth 68) come "FACTORY" sotto il logo; testo a wdth 100; cifre tabellari per telefoni, orari, date, "50 mm", "1982". Niente corsivi.
- Riferimenti: Stanley/Stella per il tono (il capo basico trattato come un prodotto di valore, titolo grande e pulito); Hand & Lock per l'idea che un solo capo o dettaglio fotografato bene basta in apertura; delle home amate, l'oggetto scontornato sulla carta di Hambro e di Mario Agnoletto.
- Colori: carta #F4F3EF, piede #EAE8E2, inchiostro #151714, testo secondario #4A4C47 (8,1:1 su carta, 7,4:1 sul piede), didascalie #5C5E58 (6,1:1 su carta, 5,6:1 sul piede), verde del logo #0B6B35 per bottone, link e scheda attiva (6,1:1; testo carta sul verde 6,1:1). Il verde fluo resta solo sulla felpa, il verde chiaro solo nel logo. Nessuna fascia nera, nessun maiuscolo condensato.
- Riga legale e didascalie a 14 px, titoletti del piede a 13 px in #4A4C47.

## Interazione

Le cinque schede delle lavorazioni (Ricamo, Serigrafia, Sublimazione, Stampa UV, Incisione laser) sono veri bottoni con ruolo tab: al clic o al tocco cambiano di netto foto, frase e supporti, senza dissolvenze; i pannelli hanno la stessa altezza, così la pagina sotto non salta. Da tastiera: Tab entra nella fila, frecce destra e sinistra, Home e Fine; il fuoco è visibile. Provato con `_prova/script/gesto_finale.mjs` (clic su Stampa UV, freccia a Incisione laser, Home e frecce). Il menu si apre con un bottone sotto i 1100 px. Nessuna animazione allo scorrere, nessun effetto che segue il cursore.

## Foto: origine e licenza

Trattamento unico: tutte a colori, luci portate al colore carta, neri all'inchiostro, saturazione appena ridotta (0,88-0,9); la felpa tiene il fluo pieno. Esportate in più larghezze con srcset (`_prova/script/build_img.py`).

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Apertura, felpa 82 | `img/felpa82-421.jpg`, `-324.jpg` | Ciesseci, `2018-02-csc-factory-26.jpg`: ritaglio della felpa, scontorno GrabCut, carta e ombra di contatto | materiale del cliente |
| Scheda Ricamo, coni di filo | `img/tec-ricamo-*.jpg` | PJ Wallace, Unsplash KAMaLRggG9g (segnaposto): taglio più stretto sui coni a fuoco, tolte con inpaint le scritte del marchio dei fili sui coni | Unsplash License |
| Scheda Serigrafia, telaio alla finestra | `img/tec-serigrafia-*.jpg` | emarts, Unsplash ZCTh4f4mv18 (segnaposto) | Unsplash License |
| Scheda Sublimazione, maglietta sulla pressa | `img/tec-sublimazione-*.jpg` | Compagnons, Unsplash EY0BPl2rpME (segnaposto): tolta con inpaint l'etichetta del produttore sul collo | Unsplash License |
| Scheda Stampa UV, plexiglass stampati | `img/tec-stampa-uv-*.jpg` | Ciesseci, `2019-10-sld-stampe-plexiglass.jpg` (lavoro loro) | materiale del cliente |
| Scheda Incisione laser | `img/tec-laser-*.jpg` | Ciesseci, `2018-02-csc-factory-15.jpg` (macchina loro) | materiale del cliente |
| Abbigliamento, caschi e gilet | `img/dpi-*.jpg` | Tanya Paquet, Unsplash wjHdeYmI-XU (segnaposto, da sostituire con i DPI veri del loro showroom) | Unsplash License |
| Chiusura, showroom di Via Zanella | `img/showroom-*.jpg` | Ciesseci, `2019-02-ciesseci-nuova-sede-2.jpg` | materiale del cliente |
| Logo | `img/logo-csc-128.png`, `-240.png` (2x) | Ciesseci, `logo-badge-500x486.png` | marchio del cliente |

Nessuna immagine generata dall'IA. Le foto di repertorio sono controllate contro i `CREDITI.md` delle altre home della campagna (nessuna ripetuta); la foto della chiusura è solo di questa home e non compare sopra. Tolte dalla versione A la foto Unsplash del telaio in apertura e la felpa nella sezione 1982. Sulla parete dello showroom si leggono in piccolo i marchi che vendono (Snickers, Sparco, Dike, Giasco): è il loro negozio, ma va chiesto se va bene.

## Chiusura e piede

- Chiusura "b con foto": "Ti aspettiamo a Mestrino" (frase loro dalla home), testo a sinistra, foto dello showroom fino al bordo destro; telefono grande `tel:+39049634423`, cellulare `tel:+393278831747` e WhatsApp, email `mailto:`, indirizzo con "Apri la mappa", orari. Nessun riquadro, nessuna tabella.
- Piede su #EAE8E2: logo PNG a 2x con una riga su chi sono e i recapiti; colonne Lavorazioni, Abbigliamento, Azienda; newsletter "Novità e promozioni" (email, bottone, consenso; non invia nulla finché non si collega a un servizio, vedi LEGGIMI); Seguici con i quattro profili veri come parole; riga legale CIESSECI SRL, sede legale Via Cavour 8 Rubano, P.IVA e C.F. 03866700283, REA PD-343821, capitale sociale 10.200,00 €, Privacy, Cookie. A 390 le colonne si impilano in ordine.

## Controlli

- Screenshot guardati a pezzi: 1440, 390, 320, 768, 1024, 1920. Nessuno scorrimento orizzontale (larghezza di scorrimento uguale alla finestra a tutte le misure), nessun elemento di testo fuori finestra, nessuna sovrapposizione. Carattere caricato dalla pagina.
- Link telefonici corretti in `tel:+39049634423` in tutti e tre i punti.
- Nessun U+2014 nella pagina, negli script e nei .md.
- Strumento dei segnali (`kit/segnali.sh`, home a 1440): 16 soglie su 18 OK. Da correggere: area foto 31,1 % (soglia 35 %): la felpa vera non si può ingrandire oltre 1,3x senza diventare morbida e il giudice ha chiesto di togliere la foto dalla sezione 1982; ho allargato la foto dei DPI e quella della chiusura. Da guardare: due misure di H2 (58 e 66 px), lasciate così. "Passione" (parola da brochure) tolta dalla frase dei tre amici.
- Altezza a 1440: 5869 px, dentro 5500-6200.

## Da confermare con il cliente

- Lo scatto della felpa: va rifatto (sotto) e va detto se la felpa 82 è ancora il loro merchandising.
- L'apertura sulla felpa invece che su un lavoro per un cliente.
- "Dal 1982" (attività dei tre amici) contro la srl del 2003.
- Il cellulare: 327 8831747 (sito e WhatsApp) contro 347 8831747 (locandina 2019).

## Da rifare dal vero

- **Felpa 82**, la foto più importante: felpa intera stesa piana su fondo chiaro (carta o tela grezza), ripresa dall'alto in perpendicolare, luce naturale laterale da finestra; una vista intera con le maniche aperte e un macro della stampa fluo e del marchio dentro l'8; almeno 3000 px sul lato lungo, a fuoco su tutto il capo, senza altri oggetti attorno.
- Le cinque schede con le loro macchine e lo stesso taglio 2,25:1 (coni sulla loro ricamatrice, racla sul loro telaio, termopressa con un capo, piano della stampante UV con un pezzo, laser su una targa), almeno 2400 px; i DPI del loro showroom al posto dei caschi; lo showroom con luce del mattino, senza grandangolo spinto.
