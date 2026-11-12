# Tacchificio Riviera, home finale: "Il tacco come scultura"

Pagina: `sito/index.html` (statica, si apre con file:///). Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini (`finale_img.py`, con il ritocco dello stiletto in `ritocco_stiletto.py`), pagina (sorgente `_prova/finale/index.html`), caratteri, screenshot e controlli (`finale_scatti.mjs`). Base: la bozza chiara con lo stiletto, quella scelta per questa azienda; la prima schermata è rimasta com'era, cambiano l'esecuzione e i dettagli.

## L'idea

Un tacco presentato come una scultura: un solo pezzo vero dell'azienda, grande e in piedi su un piano color carta, sotto un titolo bodoniano stretto che ha la stessa verticalità dello stiletto. Tutti i pezzi in pagina vengono dalla loro galleria e sono trattati come oggetti da museo, con didascalie e legende. Con il nome di un altro tacchificio la pagina non regge più: il tacco in ottone ha "RIVIERA" inciso sul piano, la storia è quella dei Boldrin e la foto d'archivio è la loro.

## Le prime due schermate

1. **Apertura, 1440x900.**
   - In testata ci sono il timbro con la firma di Valentino Boldrin, "Stra e Vigonovo, Riviera del Brenta", quattro voci e il telefono.
   - Sotto, centrato, c'è il titolo "Tacchi per le calzature di lusso" a 132 px.
   - Al centro c'è lo stiletto a calice nero, alto 551 px (1,1 volte la misura nativa, il massimo).
   - In basso, sulla stessa linea a 848 px, ci sono il bottone "Inviaci il disegno", le tre schede (Legno, Prototipo, Serie) e la didascalia. Sopra il bottone c'è la frase su cosa fanno e per chi.
2. **Apertura, 390x844.** Il titolo va su due righe, lo stiletto è alto 276 px e sotto ci sono le tre schede, poi la didascalia, la frase e il bottone, tutti dentro la prima schermata.
3. **Seconda schermata.** C'è una sola pausa fotografica: il fiore inciso a mano su un tacco in metallo, in 2:1, dentro i margini della griglia (1328 px a 1440); sul telefono è in 4:5.

Il resto della pagina:
- "Dal disegno al tacco": il paragrafo e una sola riga con le cinque fasi legate da un filetto (sotto i 1100 px diventa un elenco a righe).
- "Il nostro nome, inciso sul piano": il tacco in ottone grande, senza riquadro, con due legende a filetto da 1 px e pallini vuoti da 10 px. Sul telefono diventano un elenco numerato.
- "Tre generazioni di Boldrin", con la foto d'archivio in bianco e nero a sinistra.
- I sistemi certificati, con lo scopo SGS.
- La chiusura, stile B "con foto": a sinistra, a filo del bordo della pagina, il controllo di un prototipo davanti agli scaffali dei modelli; a destra la frase "Il cliente presenta un disegno con la sua idea: noi la interpretiamo e la realizziamo." e i recapiti in poche righe (vedi sotto).
- Il piede in una riga sola su carta: ragione sociale, sede legale, P.IVA, REA, capitale sociale e i link a privacy, whistleblowing (procedura e privacy), modulo SA8000 e versione inglese.

Altezza della pagina: 4821 px a 1440, 5281 px a 390 (con la chiusura con foto).

## La chiusura: stile B, con foto (20 ottobre 2026)

Le chiusure "oggetto del mestiere disegnato che porta i recapiti" (qui il piano del tacco) sono state bocciate dal committente. Sui due campioni di Hambro e Bazzato ha scelto lo stile B, "con foto": una frase dell'azienda grande, i recapiti in poche righe pulite, una sola foto grande, il piede in una riga. Qui è applicato così.

- **La frase**, in Imbue (il carattere dei titoli) a 65 px a 1440, 46 a 1024, 36 al telefono: "Il cliente presenta un disegno con la sua idea: noi la interpretiamo e la realizziamo." Viene dal paragrafo di "Dal disegno al tacco", che a sua volta riprende il loro sito ("Il cliente presenta un disegno con la sua idea, viene interpretata e realizzata", pagina Ispirazioni). È la frase che dice meglio come lavorano: sul disegno del cliente. Esce "Diamo forma alla tua idea?", che era una domanda d'invito, e la riga sul piano del tacco.
- **I recapiti**, in Hanken a corpo di testo, in fondo alla colonna e allineati al piede della foto: il telefono +39 049 502844 a 36 px (28 px sotto i 1120 px; `tel:`, area toccabile alta 44 px), l'email (`mailto:`, va a capo solo dopo la @), la sede operativa "Viale Serenissima 30, 30030 Vigonovo (VE)" con "Apri la mappa" (Google Maps), poi in grigio il fax e la PEC (`mailto:`). Orari: l'azienda non li pubblica, quindi non ci sono. Niente riquadri, card, filetti tra le voci, etichette maiuscole o disegni.
- **La foto**: `sito/img/prototipo-scaffali-{640,960,1440,1920}.jpg`, da `assets/originali/background/nascita-desktop.jpg` (1920x1080), lo sfondo della sezione "Nascita" del loro sito tacchificioriviera.it: due persone esaminano un prototipo di tacco segnato in rosso, davanti agli scaffali dei modelli. È una foto dell'azienda (licenza: la loro, come tutte le altre in pagina; il permesso d'uso e quello delle persone ritratte vanno chiesti, vedi LEGGIMI). Nessuna foto esterna, nessuna foto nuova.
  - **Perché questa.** La più bella e nitida del materiale è l'incisione del fiore, ma è già la pausa fotografica della seconda schermata (approvata così): ripeterla in chiusura sarebbe un doppione, e spostarla vorrebbe dire toccare il resto della pagina. Tra le altre foto piene a 1920 (il CAD, la sede al crepuscolo, questa) è la più nitida sulle mani e sul pezzo, e racconta proprio la frase accanto: il prototipo segnato in rosso (lo stesso rosso matita dell'accento della pagina) che passa di mano in mano. Sopra la chiusura ci sono i certificati, senza foto: nessun doppione vicino.
  - **Trattamento** uguale all'incisione (`finale_img.py`): antiblocchi (mediana 3x3 al 60 % e sfocatura di 0,5 px, la fonte è un JPEG molto compresso), gradazione neutra appena desaturata (0,88), qualità 88. Si esporta l'inquadratura intera e la pagina la taglia con `object-fit`, centrata sulle mani e sul tacco (`object-position: 57% 35%`): le due facce restano dentro da 900 a 2560 px.
- **Impaginazione.** Sopra i 860 px la foto occupa le colonne 1-6 (1-7 sotto i 1100) ed esce fino al bordo sinistro della finestra anche oltre i 1440 px (`margin-left` con `max(0px, (100vw - 1440px) / 2)`); alta 677 px a 1440, tra 520 e 700. Il testo sta nelle colonne 8-12: la frase in alto, allineata alla cima della foto, i recapiti in basso, allineati al piede. Sotto gli 860 px la foto va sopra, a tutta larghezza da bordo a bordo, in 5:4, poi la frase e i recapiti.
- **Il piede** resta quello di prima, una riga sola a 1440 nel tono della pagina: ragione sociale, sede legale, P.IVA e C.F., REA, capitale sociale e i link a privacy, whistleblowing (procedura e privacy), modulo SA8000 e versione inglese. La PEC aggiunta lì lo mandava su due righe a 1440 (servono 1600 px), quindi resta tra i recapiti.
- **Dati**: tutti quelli che c'erano, nessuno nuovo, nessuno perso (tel, email, sede operativa con mappa, fax, PEC nei recapiti; sede legale e dati societari nel piede).
- **Controlli**: chiusura guardata a pezzi a 2560, 1440, 1024, 900, 768, 390 e 320; nessuno scorrimento orizzontale da 320 a 2560 (build); nessuna sovrapposizione di testi (controllo automatico del build); la foto parte da x=0 a ogni larghezza; contrasti: inchiostro sulla carta 16,0:1, grigio (fax, PEC, piede) sulla carta 5,7:1. Nessun U+2014. Segnali: 17 soglie su 18 OK; area foto 33,4 % (prima 26,9 %), 13 filetti, un titolo col punto (la frase della chiusura) su 6, dentro la soglia.
- **Come si rifà**: `_prova/script/chiusura_foto.py` è già applicato a `_prova/finale/index.html` (la pagina com'era prima, con il piano del tacco, è in `_prova/home/prima-della-foto/`); poi `bash _prova/script/build_finale.sh`.

## La chiusura precedente: il piano del tacco (sostituita il 20/10/2026)

Messe affiancate tutte le chiusure della campagna (`_metodo/chiusure-a-confronto.jpg`), il biglietto da visita con il timbro tondo era troppo vicino alla scheda d'archivio di Mario Agnoletto: tutte e due erano un cartoncino chiaro con l'ombra, il telefono grande e un timbro tondo impresso, sulla carta. E un biglietto da visita non è un oggetto del mestiere: lo ha qualunque azienda.

- **L'oggetto: il piano del tacco, visto dall'alto.** È la faccia del tacco che va contro la scarpa, quella dove l'azienda incide il nome (la sezione sopra: "Il nostro nome, inciso sul piano"). È disegnato a filo come sul disegno del cliente: contorno in inchiostro da 1,5 px, dorso tondo in alto, petto appena concavo in basso, una seconda linea tratteggiata #B9B2A8 all'interno, riempimento #F8F6F2 appena più chiaro della carta. Nessuna ombra, nessun rettangolo: è l'unica chiusura della campagna che non ha una forma squadrata. Il disegno è un SVG che si allarga con il contenuto (`preserveAspectRatio="none"`, tratto che non si deforma), quindi al telefono il piano si allunga come quello di uno stiletto.
- **Dentro il piano**, centrati come un'incisione: "Tacchificio Riviera" in Imbue 30 px; il telefono in Imbue 58 px (`tel:`, sottolineato a filo); l'email (`mailto:`, va a capo solo dopo la @); sotto un filetto, in piccolo, la sede operativa con "apri la mappa", il fax e la PEC (`mailto:`).
- **A sinistra** la domanda "Diamo forma alla tua idea?" e sotto una riga nuova che dice cos'è il disegno: "Inviaci il disegno. I recapiti sono sul piano del tacco, dove incidiamo il nostro nome." (riprende il bottone d'apertura "Inviaci il disegno" e la sezione del nome inciso).
- **Tolti**: il biglietto da visita, il timbro impresso nei contatti (il timbro resta nella testata), la riga "Stra e Vigonovo, Riviera del Brenta" del biglietto (è già nella testata). Nessun dato nuovo, nessun dato perso: sede, fax e PEC sono tutti nel piano; sede legale e dati societari nel piede.
- **Larghezze.** Sotto i 1100 px la domanda va sopra e il piano sotto, largo al massimo 640 px; sotto i 520 px il piano si allunga, il telefono scende a 32-42 px e le righe piccole vanno una per riga.
- **Controlli**: chiusura guardata a pezzi a 1440, 1024, 768, 390 e 320; nessuno scorrimento orizzontale da 320 a 2560 (build); nessun testo fuori dal contorno; contrasti: inchiostro sul piano 17,0:1, grigio sul piano 6,0:1, grigio sulla carta 5,7:1. Il disegno è `aria-hidden`. Segnali come prima (17 soglie su 18 OK, area foto 26,9 %, filetti 14). Nessun U+2014. Altezza della pagina: 4704 px a 1440, 5254 a 390.
- **Come si rifà**: `_prova/script/chiusura_piano.py` è già applicato a `_prova/finale/index.html` (la pagina com'era prima è in `_prova/home/prima-del-piano/`); poi `bash _prova/script/build_finale.sh`.

## La chiusura precedente: il biglietto da visita (sostituita)

Il committente ha notato che quasi tutte le home finivano allo stesso modo: titolo, telefono gigante, riga di colonnine con indirizzo, email e orari, piede scuro a quattro colonne. Anche qui era così (telefono a 56 px, quattro voci in due colonne, piede in inchiostro pieno con il timbro chiaro). La domanda "Diamo forma alla tua idea?" era già propria di un tacchificio che lavora sul disegno del cliente, quindi resta; cambia ciò che le risponde.

- **Un solo oggetto: il biglietto da visita dell'atelier.** A destra della domanda (colonne 7-12 a 1440) c'è un biglietto in proporzione 85:55, su un cartoncino appena più chiaro della pagina (#FBFAF7), con un filetto e un'ombra corta come un biglietto appoggiato sul banco. In alto il nome e "Stra e Vigonovo, Riviera del Brenta", e a destra il loro timbro impresso, girato di 8 gradi come un timbro dato a mano. Al centro il telefono in Imbue a 54 px (collegamento `tel:`, sottolineato a filo) e l'email (`mailto:`). Sotto un filetto, in piccolo: sede operativa con "Apri la mappa", fax e PEC (`mailto:`). Il pezzo è coerente con l'idea della pagina: come i tacchi, anche i recapiti sono un oggetto solo, presentato su carta.
- **Il piede è una riga sola**, nel tono della pagina: filetto, ragione sociale in inchiostro, poi sede legale, P.IVA e C.F., REA e capitale sociale (dati obbligatori per una S.r.l.) e i link legali a destra, a 13,5 px in grigio (5,7:1 sulla carta). A 1440 sta su una riga; sotto va a capo per voci intere.
- **Tolti**: il telefono grande da solo, la griglia di quattro voci (Scrivici, Sede operativa, PEC, Sede legale), il piede scuro con il timbro chiaro e le colonne di link (e quindi `timbro-chiaro.svg`, che lo script non genera più). La sede legale e la PEC non si perdono: la prima è nel piede, la seconda sul biglietto.
- **Dati**: tutti già in pagina prima, nessuno nuovo. Le due voci whistleblowing ora sono "Whistleblowing: procedura, privacy", con gli stessi due link.
- **Telefono**: 237x65 px toccabili a 1440, 178x51 a 390, 149x44 a 320.
- **Sotto i 1100 px** la domanda va sopra e il biglietto sotto, largo al massimo 640 px; sotto i 520 px il biglietto perde la proporzione fissa, il timbro scende a 76 px e le righe piccole vanno una per riga.
- **Controlli**: chiusura guardata a pezzi a 1440, 1024, 768, 390 e 320; nessuno scorrimento orizzontale da 320 a 2560, nessuna sovrapposizione di testi o di aree dei link nella chiusura (controllo automatico da 320 a 1440), contrasto AA (inchiostro 17,6:1 e grigio 6,2:1 sul biglietto, grigio 5,7:1 sulla carta). La chiusura da sola è in `chiusura-1440.jpg`.

## Cosa è cambiato nel passaggio precedente

- **Il gesto racconta il mestiere.** Le quattro materie (Legno, Prototipo, Plastica, Plexiglas) sono diventate tre stadi: Legno, Prototipo, Serie, con la Serie scelta all'apertura. Il plexiglas è uscito, perché sulla carta era slavato. Le didascalie sono "Legno grezzo, segnato a matita rossa", "Prototipo color avorio" e "Di serie: stiletto a calice, nero".
- **Lo stiletto ritoccato** (`ritocco_stiletto.py`):
  - la macchia bruna sul gambo è ricostruita colonna per colonna dal nero sopra e sotto;
  - il gambo è ripulito dai blocchi JPEG con una sfocatura solo verticale e solo dentro la sagoma;
  - il bordo è rifatto come un ritaglio. L'opacità viene dalla luminosità della foto originale, tranne sul piano superiore, dove il filo bruno e chiaro di 3-4 px diventa un bordo morbido di 1 px;
  - una curva più decisa, solo dentro la sagoma, apre i neri: ora si leggono il volume del calice e la luce sui due fianchi;
  - ultimo controllo a 200 %: sul bordo del piano restava un filo nero tratteggiato. Veniva da due cose: la media che estende il colore verso il bordo era calcolata a 8 bit (con un peso piccolo l'arrotondamento dava valori quasi neri) e la curva dei neri si applicava dopo, schiacciando quel filo a nero. Ora la media è in virgola mobile, la curva si applica prima, l'opacità del piano viene da un campo continuo (niente gradini) e un mediano 5x5 al 70 %, solo lontano dal bordo, toglie i puntini del rumore JPEG sul calice. Il ritaglio si controlla con `_prova/script/zoom.mjs` (ritaglio dello schermo a densità 1 o 2).
- **Il legno riempie il palco.** L'ombra lunga a sinistra sfuma entro 24 px dal pezzo. Il pezzo sale sopra la frase d'apertura (la base sta 130 px sopra il fondo del palco) e, a 1440, sta tra x=383 e x=1129 e tra y=331 e y=682. La frase finisce a x=356 e comincia a y=696, quindi non c'è sovrapposizione.
- **La foto dell'incisione non è più al vivo.** Sta dentro i margini della griglia, al massimo 1328 px, quindi la fonte da 1920 px viene sempre ridotta. Prima del ricampionamento passa un filtro antiblocchi (mediana 3x3 al 60 % e sfocatura di 0,6 px); l'esportazione è a qualità 88. A 200 % non si vedono blocchi sulle dita.
- **Dal disegno al tacco.** Le quattro colonne strette sono diventate una riga sola con le cinque fasi verificate: disegno del cliente, progettazione, stampaggio a iniezione, finissaggio, imballaggio. Sono usciti il CAD e la prova sotto la scarpa, che erano dedotti dalle foto.
- **Storia.** Al posto del doppione dei tacchi in legno c'è la foto d'archivio in bianco e nero (`territorio/modal1.jpg`, 488x562), mostrata a 440 px. La didascalia dice solo "Dall'archivio dell'azienda".
- **Testata.** Sotto i 1100 px le colonne seguono gli elementi visibili: il telefono finisce sul margine destro a 1100, 1024, 860, 768, 520, 390 e 320 (misurato).
- **Piede.**
  - "Segnalazioni (whistleblowing)" apriva il modulo SA8000. Ora ci sono tre voci: "Procedura whistleblowing" e "Privacy whistleblowing" (i due .docx che il loro sito pubblica) e "Segnalazioni SA8000" (il modulo ME.04).
  - REA e numeri di telefono non vanno più a capo, e la PEC va a capo solo dopo la @.
- **Tablet (521-860 px).** La didascalia sta centrata 8 px sotto le schede; frase e bottone vengono sotto.
- **Legende tra 861 e 1100 px.** Uscivano dalla pagina di 32 px a 900. Il capo ora occupa 4 colonne e le legende sono più corte.
- **Il tocco sulle schede** non lascia più l'evidenziazione azzurra del browser.

## Respinto

- **Titolo spezzato ai lati dello stiletto**, chiesto per allontanare l'apertura da quella di Antonio Bertolin. Il committente ha visto le due bozze e ha scelto questa prima schermata: per sua indicazione non si ripensa. La differenza con Bertolin ora sta nel gesto (gli stadi dal legno alla serie), nei pezzi e nella storia.
- **"Lo stesso tacco, stampato a iniezione"** come didascalia della Serie. Il prototipo avorio (`tacco_17`) e lo stiletto nero (`tacco_11`) hanno una forma a calla simile, ma non uguale: il piano è girato dall'altra parte e il gambo del prototipo è più grosso. Dire che sono lo stesso pezzo sarebbe un'invenzione, quindi resta da confermare (vedi LEGGIMI).

## Caratteri e colori

- **Imbue** (Google Fonts, SIL Open Font License 1.1): in tondo, peso 300, asse ottico automatico. Si usa solo per i titoli, gli anni e il telefono grande. È un bodoniano stretto e alto, con lo stesso stacco pieno-filo dello stiletto. Il riferimento è il titolo stretto ad alto contrasto di Pelletteria Graziella, preso senza il corsivo.
- **Hanken Grotesk** (Google Fonts, OFL 1.1): per il testo, il menu, le didascalie e le legende, con cifre tabellari per i codici dei certificati, le fasi e i recapiti.
- Tutti e due sono serviti dalla pagina in `sito/fonts/` (woff2, sottoinsieme latin), con le licenze in `sito/fonts/LICENZE.txt`. Non c'è Inter né un corsivo d'accento.
- **Colori**: carta #F1EFEB, inchiostro #161414, grigio #625D58, filetti #CFCAC3. L'unico accento è il rosso matita #A8322A, preso dal segno rosso sul tacco in legno: compare solo sulla scheda scelta, al passaggio del puntatore e sul fuoco della tastiera. Il piede è su carta, con un filetto.
- **Riferimenti**: Pelletteria Graziella (una frase, un prodotto, il luogo in testata), Studio N19 (il titolo enorme su un fondo quasi bianco), Maison Ernest (il tacchificio trattato da maison), Pierre Hardy (lo still life su un fondo neutro).

## Quanto ho usato le ispirazioni

Le ho usate molto, perché il soggetto del lusso le giustifica. Riviera fa tacchi per le griffe come Graziella fa pelletteria per le griffe, nello stesso distretto. Ho preso il titolo grande su chiaro e un solo prodotto. Ho lasciato il nero di Graziella, insieme al corsivo d'accento, al lettore audio, alle dissolvenze e al pallino che segue il cursore.

## Interazione (un solo gesto)

Sotto il pezzo ci sono tre schede: Legno, Prototipo e Serie. Con un clic o un tocco il pezzo al centro cambia subito, senza dissolvenza, e cambia anche la didascalia.
- Le schede sono un vero `tablist`: le frecce sinistra e destra (con ritorno al primo), Home e Fine spostano la scelta, `aria-selected` e `tabindex` seguono la scelta e il fuoco è visibile.
- L'unica transizione è sul colore e sul filetto della voce, e dura 0,12 s.
- Le foto non intercettano i clic (`pointer-events: none`).
- Con JavaScript spento resta lo stiletto. Con "riduci movimento" non ci sono transizioni.
- Non ci sono animazioni allo scorrere né effetti che seguono il cursore.

## Foto: origine, licenza, lavorazione

Tutte le foto in pagina sono del Tacchificio Riviera, prese dal loro sito tacchificioriviera.it. Non ci sono foto di repertorio né immagini generate, e le fibbie di Ruan Richard Rodrigues non sono usate.

| file in sito/img | origine | lavorazione (PIL) |
|---|---|---|
| tacco-plastica-1x/2x | galleria, `nascita/tacco_11.jpg` (800x650) | campo piatto, fondo bianco in moltiplica sulla carta; macchia sul gambo tolta, gambo ripulito, bordo rifatto, neri aperti solo dentro la sagoma |
| tacco-legno-1x/2x | `nascita/tacco_7.jpg` | campo piatto, ombra violacea portata a grigio, ombra lunga a sinistra sfumata |
| tacco-prototipo-1x/2x | `nascita/tacco_17.jpg` | campo piatto, piano sotto la base ripulito |
| tacco-ottone-1x/2x | `nascita/tacco_1.jpg` | campo piatto, ombre neutre; mostrato a 1,05x |
| incisione-800/1200/1920, -m-600/864 | `background/linee-desktop.jpg` (1920x1080) | antiblocchi, gradazione neutra, tagli 2:1 e 4:5, qualità 88 |
| archivio-488 | `territorio/modal1.jpg` (488x562) | grigio neutro, misura nativa, mostrata a 440 px |
| prototipo-scaffali-640/960/1440/1920 | `background/nascita-desktop.jpg` (1920x1080) | antiblocchi, gradazione neutra, inquadratura intera tagliata in pagina, qualità 88 (chiusura) |
| timbro.svg | `logo.svg` | ricolorato in inchiostro (testata) |

Le versioni 2x sono ottenute con Lanczos e una maschera di contrasto leggera: non aggiungono dettaglio. Nessun pezzo supera 1,1 volte la misura nativa.

## Controlli

- Gli screenshot a 1440, 390, 320, 768, 1024 e 1920 sono in questa cartella, e li ho guardati a pezzi; `chiusura-1440.jpg` è la sola chiusura.
- **Scorrimento orizzontale.** `scrollWidth` è uguale a `innerWidth` a 320, 360, 390, 414, 520, 600, 768, 860, 900, 1024, 1100, 1280, 1440, 1680, 1920 e 2560 px.
- **Testi.** Nessuna sovrapposizione (controllo automatico in `finale_scatti.mjs`).
- **Zoom a 200 %.** Sullo screenshot a 1440, lo stiletto non ha seghettatura né macchia, e l'incisione non ha blocchi 8x8.
- **Gesto, provato con il clic, il tocco a 390 e la tastiera:**
  - all'apertura è scelta la Serie;
  - un clic su Legno lo sceglie;
  - con le frecce si passa a Prototipo, poi a Serie, poi si torna a Legno;
  - Fine porta a Serie, Home a Legno, e la freccia sinistra dal primo porta all'ultimo;
  - la didascalia e l'immagine cambiano ogni volta.
- **Collegamenti.**
  - `tel:+39049502844` in testata e nei recapiti della chiusura;
  - `mailto:` all'indirizzo generale (con oggetto sul bottone) e alla PEC;
  - Google Maps sul Viale Serenissima 30 a Vigonovo;
  - i PDF dei tre certificati;
  - i due .docx whistleblowing: entrambi rispondono 206 con il tipo Word.
- **U+2014.** Nessun carattere nella pagina, negli script, nel LEGGIMI e in questa nota (lo controlla anche il build).
- **`segnali.sh`: 17 soglie su 18 sono OK.**
  - Fuori soglia c'è solo l'area foto, al 26,9 % contro il 35 %, come nella bozza scelta. La pagina è fatta di still life scontornati su carta, più una sola foto piena e una d'archivio, per scelta: un oggetto per volta, poche sezioni.
  - Hanken 91,3 %, Imbue 8,7 %, 12 filetti, nessuna freccia, nessun titolo col punto, nessuna etichetta maiuscola, nessuna numerazione 01, 02.
- **Dati.** Ogni fatto in pagina viene da `01-analisi.md`.
  - La ISO 9001 è fuori pagina perché il PDF è scaduto il 13/10/2026; per la 50001 non ci sono date.
  - Le fasi sono quelle dello scopo SGS e della frase del sito sul disegno del cliente.
  - "color avorio", non "in avorio"; sull'ottone niente "misura" né "brunito".
  - La materia dello stiletto e gli stadi delle schede sono da confermare (vedi LEGGIMI).
- **Ultimo giro (rifinitura finale).** Rifatti il build, gli screenshot (1440, 390, 320, 768, 1024, 1920, guardati a pezzi), il gesto (clic, tocco a 390, frecce, Home e Fine), la testata da 320 a 1440, lo scorrimento orizzontale da 320 a 2560 e i segnali: tutto come sopra. I link a certificati, privacy, whistleblowing e modulo SA8000 rispondono (206, tipo PDF o Word). Gli screenshot grandi dei prototipi in `_prova/home/` sono passati da PNG a JPEG.
