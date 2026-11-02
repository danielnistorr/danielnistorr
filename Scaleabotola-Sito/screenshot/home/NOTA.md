# Home finale Scalarredo, "Alzata e pedata": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, disegno, pagina, screenshot; con `controlli` anche 320, 768, 1024, 1920, il menu aperto a 390 e `controlli.mjs`). Sorgente: `_prova/script/home_finale.src.html` più `marchio.part` (marchio SVG), `quote.part` (quota della foto d'apertura) e `disegno.part` (scritto da `disegno.py`), composti da `build_finale.py`; immagini da `finale_img.py`.

Pagina alta 4.843 px a 1440 compreso il piede (6.678 a 390, 4.331 a 1024, 7.451 a 768, 5.728 a 1920).

## Idea

La home è una tavola d'architetto: il prodotto vero con le sue misure vere disegnate sopra, poi lo stesso linguaggio nel disegno in sezione di "Dove va il foro?". In apertura la PLUS a pantografo vista dall'alto dentro il foro della botola: il bianco della scala sul parquet di rovere, una quota blu sul primo gradino (10 cm, la profondità del gradino in acciaio stampato) e la scritta "pannello 18 mm" sul pannello della botola. Il titolo "Si chiude in soffitta e non ingombra" viene dalla loro pagina della PLUS ("Una volta chiusa, la scala si chiude in soffitta e non ingombra spazio utile"); "Dove va il foro?" è accanto al bottone del telefono, nella prima schermata.

## Le prime due schermate

1. A 1440: testata sottile; a sinistra il titolo in Archivo 300 a 86 px, una riga su chi sono (retrattili e scale da interno), il bottone nero "Chiama lo 049 900 00 99" e il link "Dove va il foro?", in basso un cartiglio con tre dati in cifre tabellari (5 giorni dal magazzino, 2-6 settimane fuori misura, 150 kg di portata e collaudo a 260 kg) col filo allineato al fondo della foto; a destra la foto fino al bordo (835 x 846). Sotto, la didascalia che spiega le due misure. A 390: foto a tutta larghezza con quota e scritta, poi titolo, testo e bottone nella prima schermata.
2. Retrattili: testo a sinistra, il gradino in frassino della PLUS a destra fino al bordo (709 px, file da 1180), poi "Dove va il foro?".

Poi: scale da interno (la Montreal antracite a filo del bordo sinistro, l'attacco "Da due generazioni..." e gli otto modelli con le misure vere), chiusura con la Montreal bianca, piede.

## Caratteri e colori

- Archivo (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile latino con assi peso e larghezza servito dalla pagina in `fonts/archivo-latin.woff2`. Una sola famiglia: titoli 300 a larghezza 104 % con spaziatura da -0,03 a -0,042em, testo 400, voci e bottoni 500-600, cifre tabellari per misure, prezzi, orari e telefono. Scritte della foto a 16,5 px (13,5 a 390), scritte del disegno a 15,5 unità (circa 15 px a 1440, 13 px a 390).
- Colori: carta #F7F6F3, inchiostro #14171A, grigio #565B62 (AA su carta e sul piede), blu del marchio scurito #1F4FA8 per quote, marchio e scheda attiva, piede su #EDECE8. Il caldo viene dalle foto: il parquet sotto la botola e il gradino in frassino.
- Riferimenti: Marretti (bianco, una scala grande, menu leggero), EeStairs (didascalia in riga sotto la foto); Kvadrat e Zahner per il rigore di griglia e il piede a colonne.

## Interazione

"Dove va il foro?": quattro schede vere (Soffitto, Parete, Terrazzo, Soppalco; `role="tab"`, frecce, Home e Fine, clic o dito) che cambiano di netto il disegno in sezione e i dati (foro, altezza, spazio a terra, nota del modello, prezzo di partenza del negozio dove c'è). Unica transizione: il colore di schede e bottoni al passaggio (150 ms, spenta con prefers-reduced-motion). Niente animazioni allo scorrere, niente effetti che seguono il cursore. Il bottone Menu sotto i 1024 px è l'unico altro elemento attivo.

## Foto: origine, licenza, lavorazione

| File in `img/` | Origine | Licenza | Lavorazione | Densità a 1440 su schermo 2x |
|---|---|---|---|---|
| `plus-800/1120` | `assets/originali/scalarredo/PLUS-pantografo.jpg` (2000 x 1335, sul loro sito, probabile foto di catalogo) | dell'azienda o del fornitore, da confermare | ritaglio 1120 x 1135 dentro la botola (fuori la ringhiera in ferro battuto e la sedia rossa del piano di sotto), contrasto locale leggero, appena più calda, nitidezza fine; nessuna riduzione del rumore | 1,34x (a 390: 2,9x) |
| `frassino-640/1180` | `scaleabotola/banner-bg2.jpg` (PLUS vera, 1600 x 757) | dell'azienda o del fornitore, da confermare | taglio stretto sul gradino frontale e sulla struttura bianca (fuori molla e lamiere), bianco neutralizzato | 1,66x |
| `antracite-640/955` | `scalarredo/montreal-012.jpg` (foto loro, reflex) | dell'azienda, da confermare | solo rampa e gradini bianchi, taglio abbassato di 70 px (fuori il triangolo di muro scuro), luce schiarita, colore smorzato | 1,35x (più larga entra lo sgabello) |
| `montreal-760/1240` | `scalarredo/scale-giorno-Montreal-1.jpg` (foto loro, da telefono) | dell'azienda, da confermare | riduzione del rumore dimezzata rispetto al giro precedente e microcontrasto sui bordi; nastri grigi tolti dal muro e correnti ricostruiti, una vite tolta; taglio sopra la sedia e la pianta | 1,51x |
| `scritta-blu.png` | scritta "Scalarredo scale" estratta dal logo PNG vero | dell'azienda | dal giallo al trasparente, blu #1F4FA8 | |

Il marchio a triangolo è un SVG tracciato dai contorni del PNG vero (fedele). Nessuna immagine generata dall'IA, nessuna foto di repertorio in pagina, nessuna nuova scaricata, nessuna foto di fibbie di Ruan Richard Rodrigues.

## Chiusura e piede

Chiusura: "Vieni a vedere la tua scala nel nostro negozio di Mestrino", adattata da scaleabotola.com/contatti.html ("Vieni a vedere la tua scala presso il nostro negozio di Mestrino PD"), a sinistra; telefono grande con tel:, email con mailto:, indirizzo con il link alla mappa, orari; a destra la Montreal bianca fino al bordo con la sua didascalia.

Piede: marchio SVG blu con la scritta e una riga su chi sono; colonne Scale da interno, Scale retrattili, Azienda, Contatti con Seguici (solo YouTube, l'unico social che esiste); riga legale con ragione sociale, P.IVA e C.F., REA, capitale sociale, sede legale, PEC, Privacy e Cookie. A 390 le colonne si impilano in quest'ordine. Niente newsletter: non pubblicano novità, fiere o collezioni e una scala si compra una volta; al suo posto il link al catalogo PDF delle retrattili.

## Cosa è cambiato in questa rifinitura (dal giudizio cieco)

- Apertura rifatta: al posto della Montreal bianca da telefono, troppo ripulita e servita a 1,13x, la PLUS a pantografo nitida e calda, a destra fino al bordo invece che a tutta larghezza (così il file regge meglio); titolo nuovo preso dai loro testi e legato alla retrattile; cartiglio con tre dati.
- Quote con valori: "10 cm" sul gradino, disegnata sui due spigoli veri del gradino (controllati su un ingrandimento), e "pannello 18 mm"; scritte a 16,5 px in cifre tabellari. Le vecchie quote senza numero sono tolte.
- Chiusura: tolta la foto Pexels dell'elicoidale di Ubud; al suo posto la Montreal bianca, prodotto loro, riesportata più nitida.
- Retrattili: il frassino non è più una fascia a tutta larghezza da 1440 x 560 ma una colonna di 709 px col taglio stretto sul gradino.
- Disegno in sezione rifatto da `disegno.py`: scala come due montanti paralleli con 12 gradini a passo costante, tutti i tratti a 1,25 px, niente zig-zag; tolti gli archi senza etichetta; parete con il foro aperto nel muro, la portina chiusa tratteggiata e quella aperta incernierata in basso con l'arco "la portina ruota di circa 170°"; soppalco senza le quote 140/170 a terra; "170 cm per aprirla" scritto per esteso.
- Tolta la fascia delle due frasi grandi: "Da due generazioni..." apre la sezione delle scale da interno.
- Antracite: taglio abbassato di 70 px.
- Schede del foro a 390 su una riga (20 px, spazio 16); sotto i 375 px su due righe a griglia.
- Piede: logo SVG blu più grande al posto del quadrato giallo PNG.
- Tolto il preload del carattere (errore CORS aperto da file://): console senza errori.
- Questa nota: la frase della chiusura è dichiarata "adattata", non "verbatim".

## Controlli

- `controlli.mjs`: nessuno scorrimento orizzontale a 320, 360, 390, 414, 600, 768, 900, 1023, 1024, 1180, 1280, 1440, 1680, 1920, 2560, con ognuna delle quattro schede aperta; tastiera sulle schede (frecce, Home, Fine: aria-selected, pannello e disegno giusti, tabindex 0/-1); schede provate anche col tocco; menu a 390 aperto col tocco ("Chiudi", aria-expanded true) e chiuso con Esc col fuoco che torna al bottone; collegamenti tel:+390499000099, mailto:scalarredo@scalarredo.it, mailto della PEC, mappa Google su "Scalarredo Via Marco Polo 2 Mestrino"; nessuna ancora rotta; nessun errore in console.
- Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440, 1920, il menu aperto a 390 e le quattro schede a 1440.
- Nessun U+2014 nella pagina, negli script e nei .md.
- `segnali.sh`: una soglia sotto il valore, l'area foto al 30,9 % (soglia 35 %). Scelta voluta: per servire le foto più nitide (da 1,34x a 1,66x su schermo 2x) non le ho allargate oltre; la sezione col disegno in sezione (circa 750 x 600 px) non conta come foto. Il giro precedente arrivava al 39 % con foto a 1,1x, che il giudice ha bocciato come morbide. Si risolve con le foto nuove dello showroom (vedi LEGGIMI), che permettono foto più grandi alla stessa nitidezza. Da guardare: H2 in due misure (56 e 63 px), voluto; nessun contenuto con data o nome perché non c'è un fatto sicuro (vedi LEGGIMI). Una sola famiglia, 4 filetti, nessuna etichetta maiuscola sopra i titoli.
- Dati confrontati con `01-analisi.md` (aggiunte le tre frasi della pagina PLUS a pantografo con la fonte): la norma UNI EN 14975 resta fuori finché non la confermano.
