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
- I contatti, con la sede operativa e amministrativa, la mappa, il fax e la PEC.
- Il piede scuro con i dati societari e i link a privacy, procedura e privacy whistleblowing, modulo SA8000 e versione inglese.

Altezza della pagina: 4716 px a 1440, 5487 px a 390.

## Cosa è cambiato in questo passaggio

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
- **Colori**: carta #F1EFEB, inchiostro #161414, grigio #625D58, filetti #CFCAC3. L'unico accento è il rosso matita #A8322A, preso dal segno rosso sul tacco in legno: compare solo sulla scheda scelta, al passaggio del puntatore e sul fuoco della tastiera. Il piede è in inchiostro pieno.
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
| timbro.svg, timbro-chiaro.svg | `logo.svg` | ricolorato |

Le versioni 2x sono ottenute con Lanczos e una maschera di contrasto leggera: non aggiungono dettaglio. Nessun pezzo supera 1,1 volte la misura nativa.

## Controlli

- Gli screenshot a 1440, 390, 320, 768, 1024 e 1920 sono in questa cartella, e li ho guardati a pezzi.
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
  - `tel:+39049502844` in testata e nei contatti;
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
