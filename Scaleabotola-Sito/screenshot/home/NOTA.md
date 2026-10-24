# Home finale Scalarredo, "Alzata e pedata": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, pagina, screenshot; con `controlli` anche 320, 768, 1024, 1920 e il menu aperto a 390). Sorgente: `_prova/script/home_finale.src.html` più `marchio.part` (marchio SVG) e `quote.part` (quote della foto), composti da `build_finale.py`; immagini da `finale_img.py`.

Pagina alta 5.479 px a 1440 compreso il piede, 6.729 px a 390. Parte dal prototipo B scelto dal giudice, con le sue indicazioni applicate una per una.

## Idea

La home è una tavola d'architetto. In apertura la loro Montreal bianca, vera, vista di fianco come un prospetto, con tre quote blu disegnate sui fili veri della scala: la pedata tra il filo frontale di un gradino e il filo del gradino sopra, l'alzata dal piano di una pedata al piano della successiva, la freccia che tocca la fascia da 8 mm. Il titolo "Scale a misura" sta sul muro bianco a destra. Il disegno torna nella sezione "Dove va il foro?", dove la retrattile è una sezione quotata che cambia col tipo di foro.

## Le prime due schermate

1. A 1440: foto a tutta larghezza (1440 x 853) con la testata sottile sopra; titolo in Archivo 300 a 104 px sul muro, sotto la riga "Ogni scala nasce dalle misure del foro e della stanza", il bottone nero "Chiama lo 049 900 00 99" e il link "Dove va il foro?"; tre quote, nient'altro sulla foto; sotto, la didascalia in riga semplice e "Negozio e showroom sulla statale 11 Padova-Vicenza". A 390: testata con marchio, telefono sottolineato e bottone "Menu" vero (aria-expanded, apre le quattro voci, si chiude con Esc o scegliendo una voce), foto quasi quadrata con le quote più grandi, titolo, testo e bottone nella prima schermata.
2. Due frasi grandi su chi sono: "Da due generazioni disegniamo scale da interno sul foro e sulla stanza..." e la seconda, grigia, accorciata a una riga e mezza ("Le retrattili, in magazzino o fuori misura, partono ogni giorno."). Poi la Montreal antracite a filo del bordo sinistro, ritagliata solo sulla rampa e sui gradini bianchi, con a destra "Scale da interno, una per casa" e gli otto modelli a due colonne con le misure vere.

Poi: retrattili (testo e fascia del frassino della PLUS a 1440 x 560, non più alta), "Dove va il foro?" (unico gesto), chiusura con la frase loro e la foto dell'elicoidale, piede.

## Caratteri e colori

- Archivo (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile latino con assi peso e larghezza servito dalla pagina in `fonts/archivo-latin.woff2`. Una sola famiglia: titoli 300 a larghezza 104 % con spaziatura da -0,03 a -0,045em, testo 400, voci e bottoni 500-600, cifre tabellari per misure, prezzi, orari e telefono. Le scritte delle quote nell'SVG hanno `text-rendering: geometricPrecision` e corpo ricalcolato per larghezza (circa 13 px da 390 a 1920): nessuna parola con la spaziatura rotta (controllato a 390, 768, 1024, 1440, 1920).
- Colori: carta #F7F6F3 (calda come il muro della foto, che è stato portato a un neutro appena caldo, circa #F1F1EF), inchiostro #14171A, grigio #565B62 (AA su carta e sul piede), blu del marchio scurito #1F4FA8 per quote, marchio e scheda attiva, giallo del logo solo nel logo del piede, piede su #EDECE8. Contrasti: titolo e testo sul muro dell'apertura circa 16:1; grigio sul piede 5,7:1; blu sul muro circa 7:1.
- Riferimenti: Marretti (bianco, una scala enorme, menu leggero), EeStairs (didascalia in riga sotto la foto); Kvadrat e Zahner per il rigore di griglia e il piede a colonne.

## Interazione

"Dove va il foro?": quattro schede vere (Soffitto, Parete, Terrazzo, Soppalco; `role="tab"`, frecce, Home e Fine, clic o dito) che cambiano di netto il disegno in sezione e i dati (foro, altezza, spazio a terra, nota del modello, prezzo di partenza del negozio dove c'è). Unica transizione: il colore delle schede e dei bottoni al passaggio (150 ms, spenta con prefers-reduced-motion). Niente animazioni allo scorrere, niente effetti che seguono il cursore. Il bottone Menu sotto i 1024 px è l'unico altro elemento attivo.

## Foto: origine, licenza, lavorazione

| File in `img/` | Origine | Licenza | Lavorazione |
|---|---|---|---|
| `montreal-1440/1630`, `montreal-tel-780/940` | `assets/originali/scalarredo/scale-giorno-Montreal-1.jpg` (foto loro, da telefono) | dell'azienda, da confermare | riduzione del rumore leggera; nastri grigi decorativi tolti dal muro e correnti del parapetto ricostruiti lungo la loro direzione (niente cuciture); due puntini e una vite sotto la scritta "pedata" tolti; muro lisciato fuori dai bordi, bordi dei gradini tenuti nitidi; curva di tono che porta il muro a un bianco appena caldo e lascia i gradini più chiari del muro |
| `antracite-640/955` | `scalarredo/montreal-012.jpg` (foto loro, reflex) | dell'azienda, da confermare | ritaglio solo sulla rampa e sui gradini bianchi (fuori divano, cucina, tavolino e oggetti in legno), luce schiarita, colore smorzato |
| `frassino-800/1440/1600`, `frassino-tel-780` | `scaleabotola/banner-bg2.jpg` (PLUS vera, 1600 x 757) | dell'azienda o del fornitore, da confermare | bianco del pantografo neutralizzato, fascia 1600 x 622 ridotta (mai ingrandita) |
| `elicoidale-720/1000/1349` | `assets/esterne/dhea-elicoidale-bianca-alto.jpg`, Gayatri Dhea su Pexels, https://www.pexels.com/photo/elegant-curved-staircase-in-ubud-boutique-hotel-32501209/ | Pexels, uso commerciale libero (in `assets/CREDITI.md`) | ritaglio 1349 x 1170, tinta appena scaldata; segnaposto, non è un loro lavoro e non ha didascalia; non compare in nessun'altra home della campagna |
| `scritta-blu.png` | scritta "Scalarredo scale" estratta dal logo PNG vero | dell'azienda | dal giallo al trasparente, blu #1F4FA8 |
| `logo-scalarredo-272.png` | `logo-scalarredo-765x625.png` | dell'azienda | ridotto a 2x per i 136 px del piede |

Il marchio a triangolo della testata è un SVG tracciato dai contorni del PNG vero (fedele). Nessuna immagine generata dall'IA, nessuna nuova scaricata in questo passaggio, nessuna foto di fibbie di Ruan Richard Rodrigues.

## Chiusura e piede

Chiusura: "Vieni a vedere la tua scala nel negozio di Mestrino" (verbatim da scaleabotola.com/contatti.html) a sinistra, telefono grande con tel:, email con mailto:, indirizzo con il link alla mappa, orari; a destra la foto dell'elicoidale fino al bordo, con il fondo del testo allineato al fondo della foto. Il CAP 35035 non compare più (non è scritto sul loro sito).

Piede: logo vero PNG 2x con una riga su chi sono; colonne Scale da interno, Scale retrattili, Azienda, Contatti con Seguici (solo YouTube, l'unico social che esiste); riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, sede legale, PEC, Privacy e Cookie. A 390 le colonne si impilano in quest'ordine, una sotto l'altra; da 1024 a 1180 il logo sta sopra e le quattro colonne sotto. Niente newsletter: non pubblicano novità, fiere o collezioni e una scala si compra una volta; al suo posto il link al catalogo PDF delle retrattili.

## Controlli

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920; nessuna sovrapposizione (screenshot guardati a pezzi a tutte le larghezze, più il menu aperto a 390).
- Nessun U+2014 nella pagina, negli script e nei .md.
- `segnali.sh`: 0 soglie bloccanti. Da guardare: H2 in due misure (56 e 63 px), scelta voluta con un solo elemento grande; nessun contenuto con data o nome, perché non c'è un fatto sicuro da mettere (vedi LEGGIMI). Area foto 39,4 %, una sola famiglia, 3 filetti.
- Dati confrontati con `01-analisi.md`: la norma UNI EN 14975 è tolta finché non la confermano; resta "portata 150 kg, collaudo a 260 kg".
