# Meccanica Masi, home finale "Dal pieno"

Pagina: `sito/index.html`. Parte dal prototipo A (scelto dal giudice) con gli innesti di B: indice dei settori, due progetti con le foto vere, chiusura con le pulegge, piede su fondo più scuro. Alta 5760 px a 1440, piede compreso.

## Idea

Un pezzo ricavato dal pieno e finito bene è già un oggetto da guardare. La loro leva con settore dentato, scontornata dalla foto vera, domina la prima schermata dall'alto; un interruttore Grezzo / Finito fa vedere lo stesso pezzo appena fresato in ghisa e poi verniciato, con la dentatura e l'alesatura lasciate in metallo. È il dettaglio che ha solo Masi (analisi, sezione 5): con il nome di un concorrente la pagina non regge, perché il pezzo e il prima e dopo sono loro.

## Prime due schermate

- **1440, prima schermata** (`home-1440-prima-schermata.jpg`): fondo carta calda #F2F0EB. La leva bianca alta circa 720 px, sull'asse a due terzi della pagina, scende fino alla fascia dell'interruttore; due legende a filo sottile: "Settore dentato, fresato con fresa modulo" e "Alesatura H7". In basso a sinistra il titolo su due righe, "Precisione in officina, / continuità in produzione", a 94 px, con la base allineata alla base del pezzo: il pezzo domina, il titolo lo regge. In alto a sinistra, piccoli, il testo d'apertura, il bottone nero "Chiama 348 169 34 51" e la riga con l'email e "Officina meccanica a Padova, dal 1977" (la riga che nel prototipo stava sopra il titolo). Sotto il pezzo, centrato sul pezzo, l'interruttore; a destra la didascalia.
- **Stato Grezzo**: la stessa leva in ghisa appena fresata, ruotata e specchiata perché abbia lo stesso verso della finita (dentatura a sinistra, foro del manicotto in basso a destra); sta sopra la quota del titolo e non lo tocca a nessuna larghezza.
- **Seconda schermata**: "Dalla stampa ai trasporti industriali", una riga di testo loro ("Lavoriamo anche per sacchettifici, confezionatrici e trasporti industriali") e l'indice tipografico dei quattro settori a filetto: Stampa offset e flexo, Giornali, Sacchetti e confezioni, Trasporti e automazione, nome grande a sinistra e una riga a destra.
- **390** (`home-390-prima-schermata.jpg`): titolo su due righe a 44 px, la leva a tutta larghezza con i numeri 1 e 2 sul pezzo, l'interruttore a due bottoni larghi e l'elenco delle due legende, tutto entro gli 844 px; il telefono è in testata. Poi testo, bottone di chiamata, email.

Il resto: una foto di officina a tutta larghezza (l'unica di repertorio, "Foto indicativa"), le sei lavorazioni 3x2 con una misura vera in testa a ogni cella (6 torni, 1 a CNC; 3 assi; da 10 cm a 3 m; TIG, MIG/MAG, elettrodo; offset, flexo, sacchettifici; dal montaggio al collaudo) e la riga dei materiali; i due lavori per la stampa con le loro foto (supporto Man-Roland grande, linea giornali stretta) e quattro link agli altri; "Non chiediamo di smontare, imballare e spedire nulla: veniamo noi da voi" con la foto vera dell'interno di una macchina da stampa e le cinque fasi d'installazione numerate (sono una procedura vera, dalla pagina Installazione); la chiusura; il piede.

## Chiusura e piede

- Chiusura ("b con foto", testo a sinistra e foto a destra fino al bordo): "Un'officina che c'era ieri, c'è oggi e sarà qui domani" (dalla loro pagina Chi siamo), telefono grande in rosso #E3141B con tel:, email con mailto:, indirizzo come link alla mappa, orari su due righe, sotto la loro frase "Chi ci chiama parla con chi lavora, e chi lavora conosce il mestiere". Foto vera delle pulegge dentate e del mozzo dal pieno, nitida, 708x504 a 1440: non compare altrove nella pagina.
- Piede su #E9E6DF: logo vero (la scritta vettoriale del loro SVG) con una riga su chi sono; quattro colonne con titoletti in tondo: Azienda, Lavorazioni (sette voci, compresa Rulli per la stampa), Progetti, Contatti; riga legale con ragione sociale, indirizzo, P.IVA e C.F. 05200110285, REA PD-450853, codice SDI M5UXCR1, Privacy, Cookie. Capitale sociale e PEC restano fuori finché non sono confermati (vengono da aziende.it). A 390 le colonne si aprono a fisarmonica con veri bottoni (`aria-expanded`, `aria-controls`).
- **Niente colonna Seguici**: non esiste un profilo social vero (l'Instagram del sito porta a "#").
- **Niente newsletter**: lavorano su commessa per altre aziende, senza fiere, cataloghi, collezioni né clienti privati; il plugin newsletter del sito è installato e mai usato.

## Caratteri e colori

- **Mona Sans** (GitHub, Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia, file variabili serviti dalla pagina in `sito/fonts/`. Titoli in peso 500 con larghezza 80-85 % e spaziatura da -0,016 a -0,022em; testo 400 a larghezza piena; h3 e bottoni 600. Riferimenti: il maiuscolo stretto di Hermle ("SIMPLE OPERATION IS ALWAYS BASED ON PRECISION.") e l'HelveticaNeue condensato di Fehlmann (cartella `riferimenti/`), qui in minuscolo e senza grassetti; la prima schermata con un solo pezzo scontornato e la sua ombra viene da Hermle, la precisione raccontata da un oggetto e da una luce da Vaucher. Cifre allineate (`lining-nums`); le tabellari di Mona Sans hanno lo zero puntato e in home non ci sono colonne di numeri.
- Colori: fondo #F2F0EB (più chiaro e caldo del grigio cemento del prototipo), piede #E9E6DF, inchiostro #171717 (15,7:1), grigio #55524D (6,8:1 sul fondo, 6,2:1 sul piede), filetti #CFCBC3, rosso del logo #E3141B solo per il telefono grande della chiusura (4,2:1, testo da 48 px), rosso scuro #B3121A per i numeri delle fasi e il passaggio su bottone e link (6,1:1). Contrasto AA ovunque.

## Interazione

Un solo gesto: l'interruttore Grezzo / Finito sotto il pezzo. Due bottoni veri con `aria-pressed`, frecce sinistra e destra da tastiera, tocco su telefono; cambio netto di foto, legende ed elenco, senza dissolvenze. Il bottone di chiamata diventa rosso #B3121A al passaggio, mai sbiadito; il bottone non premuto dell'interruttore prende un fondo appena più scuro. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto sul cursore. Su telefono il menu è un bottone "Menu" e il piede si apre a fisarmonica.

## Foto, origine e licenza

- Leva finita e leva grezza: Meccanica Masi (`assets/originali/2026-07_WhatsApp-Image-2026-06-08-at-20.40.35-1.avif` e `...20.40.41.avif`), scontornate con OpenCV (grabCut su un contorno tracciato a mano), bilanciamento del bianco, ombra presa dalla foto, WebP con trasparenza su due tele (2:1 da 901 px, quasi quadrata per il telefono).
- Supporto Man-Roland, linea di spedizione giornali (tagliata sopra i ritagli di carta a terra), interno della macchina da stampa, pulegge: Meccanica Masi, dal loro sito. Trattamento comune caldo e luminoso: un po' meno saturazione, neutro caldo, mezzitoni più chiari, neri appena sollevati.
- Fresatrice in officina: Connor Lucock, Pexels (https://www.pexels.com/photo/industrial-lathe-machine-in-action-28929513/), Pexels License, uso commerciale libero; unica foto di repertorio, con "Foto indicativa" nella didascalia; non usata in altre home della campagna.
- Nessuna immagine generata dall'IA; nessuna didascalia fa passare il repertorio per lavoro loro. Elenco completo in `assets/CREDITI.md`; foto da rifare dal vero nel `LEGGIMI.md`.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare; area foto 37 %, Mona Sans 100 %, monospazio 0 %, 18 filetti, 0 frecce, 0 numeri grandi, 0 etichette sopra i titoli, una sola sezione con titolo a sinistra e testo a destra (Lavorazioni), date in pagina: 1977.
- `finale_controlli.mjs` a 1920, 1440, 1280, 1024, 768, 390, 320: nessuno scorrimento orizzontale; la tela del pezzo esce di proposito a destra ed è tagliata al bordo della finestra; nessuna sovrapposizione visibile tra titolo, testo, legende e pezzo, nei due stati (lo script segnala solo riquadri di righe che si toccano senza testo sopra testo). Tastiera: la freccia a destra torna a "Finito"; fisarmonica: "Lavorazioni" si apre e le altre restano chiuse.
- Altezze: 1440 = 5760 px, 1920 = 5823, 1280 = 5504, 1024 = 5966, 768 = 7373, 390 = 8126, 320 = 8499.
- Screenshot guardati a pezzi a 1440 e 390, più le prime schermate e lo stato Grezzo a 320, 768, 1024 e 1920. Nessun U+2014 nella pagina, nei .md e negli script. Divieti del committente: nessun gradiente, nessun testo in gradiente, nessuna emoji, niente Inter, niente card col bordo sinistro, niente vetro, niente tre box con icona, niente badge sopra il titolo, niente icone Lucide, niente dissolvenze allo scorrere, niente effetti sul cursore, niente bottoni che sbiadiscono, niente corsivo d'accento.
