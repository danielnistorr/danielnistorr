# Nic Dean, home: nota

## Livello professionale (con il ritocco finale del 3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La versione 1 com'era prima del livello professionale è copiata in `_prova/versione-1-originale/` (sito e screenshot). Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Petersham e Poilâne (a pezzi, nel ritocco finale) e prima di Union e Joseph Brot.

Rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche le immagini con `pro_img.py`); i controlli della sezione C e le prove d'uso sono in `_prova/script/pro_controlli.mjs`. Gli screenshot sono fatti all'ora simulata martedì 3 novembre 2026 alle 10 (`index.html?ora=2026-11-03T10:00`, spaccio aperto).

Screenshot (stessi nomi di prima): `home-1440.jpg` (5635 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (7375 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Per negozi, fiere ed eventi" al piede). Guardati a pezzi a 1440 e 390, e a 320, 768, 1024, 1280 e 1920, più il menu aperto e il sabato a 390.

### Il ritocco finale: che cosa è cambiato e perché

Il controllore aveva dato 5 come agenzia: apertura con lo schema delle altre home (titolo a sinistra, scheda a destra, foto in un rettangolo grigio su bianco con 286 px vuoti), nessun gesto di scala, foto di tre luci diverse, testo corrente a 16 px.
- **Apertura a tutta fascia.** Il fondo dell'apertura è ora lo stesso grigio del fondo della loro fila (#EBEBE9): la foto non è più un riquadro, le scarpe poggiano sul bordo basso della fascia, che a 1440x900 riempie lo schermo (fila 845x374 px, da y 526 a 900). La didascalia "Décolleté con plateau, firma NicDean sul sottopiede. Chiedi se c'è il tuo numero" sta nella colonna di destra, all'altezza delle suole, con un bersaglio di 44 px; anche la foto è il link alla mail. A 390 la fila va da bordo a bordo (390x172, finisce a 817 px, dentro la prima schermata).
- **Una sola serie di foto.** Le otto tessere sono ora sullo stesso grigio della fila (il fondo bianco moltiplicato per #EBEBE9 in `pro_img.py`), su una sezione bianca: come le tessere di Poilâne. Tolta la foto dello spaccio (compatta, voto 3, finestre bruciate): non reggeva per qualità e rompeva la serie. La sezione dello spaccio è solo tipografia, con la tabella degli orari a 28 px.
- **Il gesto di scala.** In "Chi siamo" restano solo le due cifre vere, 1975 e 2013, a 200 px (120 da tavoletta e al telefono). Tolti "3" e "Tutti", che erano riempitivi.
- **Testo corrente a 19 px** (17 al telefono) ovunque: prima schermata, tessere, modulo, piede. Restano a 16 px solo etichette, menu, bottoni, "Chiedi il tuo numero" e le label del modulo.
- **H2 a 56 px** (44 da tavoletta, 30 al telefono), interlinea 1; testata a 72 px al telefono.
- **Ritmo**: apertura grigia, scarpe bianche, spaccio grigio, chi siamo rosso, negozi nero, piede bianco.
- **Dai clienti tipo**: "Aperto ora" in nero con il solo punto verde; testo senza JavaScript "Aperto lunedì-venerdì, chiuso sabato, domenica e agosto"; nelle mail delle scarpe la riga per la città "per chiedere se si può spedire" e "Altro colore, se c'è" al posto di "Colore"; nella mail della décolleté i cinque colori; nell'introduzione "Se abiti lontano, scrivi anche la tua città e chiedi se si può spedire" e "Sono alcuni modelli delle ultime collezioni, quasi tutti da donna: allo spaccio trovi anche uomo e ragazzo ... chiedi se ci sono ancora"; sotto le schede "Se la mail non si apre, scrivi a info@nicdean.it"; "Chiedi il tuo numero" in nero con la freccia, sottolineato solo al passaggio; i passaggi del mouse solo dove c'è il mouse e il bottone Menu che si rilascia dopo il tocco; nello script l'elenco `CHIUSURE` per le chiusure straordinarie; "Fuori orario" tolto (il loro sito dice solo "Se vuoi puoi prendere un appuntamento per mail o telefono").

### Struttura (famiglia B adattata)

1. **Testata fissa** (80 px, 72 al telefono): logo; "Spaccio e orari" prima voce, poi "Le scarpe", "Per negozi ed eventi", "Chi siamo"; da 1280 px lo stato breve; bottone rosso con il numero. Sotto 1101 px il menu va dietro "Menu" e il bottone del telefono resta.
2. **Apertura** (fascia grigia a tutto schermo): occhiello "Calzaturificio e spaccio di fabbrica, Villatora di Saonara (PD)", titolo a 88 px (42 al telefono); a destra "Lo spaccio, oggi": stato calcolato a 28 px, orari su tre righe, "Chiama 049 640672" e "Indicazioni", indirizzo, "Per donna, uomo e ragazzo ... Paghi in contanti o con carta.", "preventivo gratuito", e in basso la didascalia della fila; sotto il titolo la fila fino al bordo della fascia.
3. **Le scarpe** (fondo bianco, tessere grigie): otto schede in 4 colonne (2 sotto 900 px), ognuna un link mailto con il nome nell'oggetto; "Preferisci chiedere a voce?" con il Chiama.
4. **Lo spaccio di via Lombardia** (fondo grigio): dal 5 ottobre 2013, quattro fatti, indirizzo, Chiama e Indicazioni; a destra la tabella degli orari a 28 px con la riga di oggi in grassetto.
5. **Chi siamo** (blocco rosso): il manifesto "Calzature prodotte interamente in azienda, di tutti i tipi e di tutti i numeri.", tre righe di storia, 1975 e 2013 a 200 px.
6. **Per negozi, fiere ed eventi** (blocco nero): le loro parole su ordini e preventivo gratuito; email con oggetto e telefono; modulo con il tipo di richiesta che compone un'email.
7. **Piede** in 4 colonne: chi sono, lo spaccio (indirizzo, orari, Indicazioni), contatti (telefono, fax, email), le voci della pagina e la privacy; riga legale con ragione sociale, P.IVA, REA e capitale.

Rispetto alla A1 mancano, apposta: i racconti foto e testo (nessuna foto loro di persone o laboratorio), le novità di stagione (nessuna nelle fonti), la foto della facciata nel blocco dello spaccio (quella che c'è sembra Street View) e la newsletter (non inviava nulla).

### Uso (scheda, par. 8): come riescono i compiti

- **Cliente dello spaccio, 390x844, senza scorrere**: lo stato a 24 px in nero con il punto verde se aperto (y 289); "Chiama 049 640672" (`tel:+39049640672`, 194x52 px) e "Indicazioni" (Google Maps, percorso verso via Lombardia 29) a y 388; "Sabato e domenica chiuso" sempre scritto; "uomo e ragazzo" e "carta" a 515 px; la fila intera finisce a 817.
- **Chi vuole una scarpa senza andare**: la décolleté della prima schermata (foto e link di 44 px); le otto schede dalla seconda schermata (sezione a 817 px, prima scheda a 1250); ogni scheda ha un nome e apre una mail con il nome nell'oggetto e le righe per numero, nome, telefono e città. Se spediscono non è nelle fonti: la pagina non lo promette, fa solo chiedere (LEGGIMI).
- **Negozio o evento, 1440x900**: "Per negozi ed eventi" nel menu e "preventivo gratuito" nella prima schermata; nella sezione il mailto ha l'oggetto "Richiesta di preventivo"; nel piede ragione sociale, P.IVA 02707240285 e indirizzo.
- **Stato provato** a 11 ore e giorni (martedì 7:30, 10, 13, 15, 17:30; venerdì sera; sabato; domenica; 12 agosto; 8 dicembre; Pasquetta 2027): tutti giusti.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata `position:sticky`; a 390, a metà pagina, il bottone 115x48 px resta in alto; 6 link `tel:`; prima voce "Spaccio e orari".
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844 (occhiello con mestiere e comune, "dal 1975", Chiama e Indicazioni; a 390 i due bottoni riempiono la riga, sotto 375 px uno sotto l'altro a tutta larghezza).
3. **Immagine vera nell'apertura**: PASSA per la famiglia B, con il limite delle foto che hanno. La loro fila di décolleté non è più un oggetto su fondo chiaro: è la scena dell'apertura, a tutta fascia, sul suo stesso fondo, fino al bordo (845 px nativi del taglio, mai ingrandita sul file). Non mostra persone o laboratorio: non ci sono foto loro che lo facciano (LEGGIMI, foto da fare).
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da Pexels o Unsplash; nessuna illustrazione.
5. **Foto in serie**: PASSA. 9 foto, 2 formati (2,26:1 la fila, 4:3 le tessere), 1 didascalia. Stesso fondo #EBEBE9 e stesso trattamento per fila e tessere; tolta la foto dello spaccio, che aveva un'altra luce. La luce della fila (studio) e delle tessere (Olympus 2001) resta diversa sotto il fondo comune: la serie vera arriva con le foto nuove (LEGGIMI).
6. **Palette dal marchio**: PASSA. Bianco, inchiostro #141414, rosso #C21F28 (il rosso del logo #EE252F scurito), verde #2E6B3A solo per il punto "Aperto", grigi #EBEBE9, #595956 e filetto. Nessun beige.
7. **Scala corta e leggibile**: PASSA. 1440: 200, 88, 56, 28, 22, 19, 16, 14 px (otto); 390: 120, 42, 30, 24, 19, 17, 16, 14 px (otto). Testo corrente 19 px a 1440 e 17 a 390; a 16 px solo etichette, menu, bottoni e label; 14 px le note legali e, al telefono, l'occhiello maiuscolo.
8. **Al massimo due famiglie**: PASSA. Una sola, League Spartan, pesi 400 e 700.
9. **Servizi in schede con foto**: PASSA. Otto scarpe in 4 colonne (passo 24 px), foto 4:3 uguale per tutte, nome a 22 px, colore, "Chiedi il tuo numero"; tutta la scheda è il link.
10. **Almeno tre tipi di prove**: NON PASSA. Ci sono solo due cifre vere (1975, 2013). Recensioni, certificazioni, fornitori e clienti con il nome non sono nelle fonti: non inventati, da chiedere (LEGGIMI, "Prove che mancano").
11. **Lavori con un nome**: NON SI APPLICA (spaccio, nessun lavoro su commessa nelle fonti).
12. **Ritmo a blocchi**: PASSA. Grigio, bianco, grigio, rosso pieno, nero pieno, piede bianco; 128 px tra le sezioni a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno rosso e con il bordo, raggio 4 px, 52 px (48 in testata), testo 16 px 700; ogni Chiama ha il numero.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta in caselle, che compone un'email (da collegare a un servizio, LEGGIMI); orari in tabella, Indicazioni e Chiama; nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). 4 colonne (2 al telefono), testo 19 px, note legali 14 px.

### Caratteri e licenze

League Spartan (The League of Moveable Type), da Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), testo in `sito/fonts/OFL.txt`; file woff2 latin e latin-ext, pesi 400-700, serviti dalla pagina.

### Controlli generali

- **Scorrimento orizzontale**: nessuno a 320, 360, 375, 390, 414, 600, 768, 900, 1024, 1100, 1280, 1440, 1600, 1920 e 2560.
- **Sovrapposizioni**: nessuna negli screenshot a 320, 390, 768, 1024, 1280, 1440 e 1920. Corretta durante il ritocco: a 1280x800 la didascalia della fila finiva sopra "preventivo gratuito" (ora ha una sua riga della griglia). Limite noto: a 1280x800 la fila esce dalla prima schermata per circa un quarto, perché la colonna di destra è più lunga della fascia.
- **Collegamenti**: `tel:+39049640672` (6), 11 `mailto:info@nicdean.it` con oggetto e 2 semplici; mappe `google.com/maps/dir/?api=1&destination=Via Lombardia 29, 35020 Villatora di Saonara PD`; nessuna ancora senza destinazione.
- **Nessun carattere U+2014** nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script (controllo in `build_finale.sh`).

---

## Versione 1 (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `build_img.py`, caratteri, screenshot con `scatti.mjs`, controllo U+2014 e segnali da IA). Parte dal prototipo A, "La décolleté", con le indicazioni del giudice e gli innesti da B.

### L'idea

La loro fila vera di décolleté con plateau (pitone, arancio, senape, oliva, lilla, firma NicDean sul sottopiede) posata sul gesso della pagina, senza riquadro, e il titolo sotto, come la base su cui stanno le scarpe. Sotto ogni scarpa il suo colore: un tocco spegne le altre quattro (in grigio) e propone "Chiedi se c'è in spaccio", cioè il loro modo di vendere ("cerca la scarpa che ti piace e inviaci il nome per email"). Con il nome di un concorrente la pagina non regge: la foto e la firma sono loro.

Il giudice aveva dato K0 6: la prima schermata è stata ripensata dentro la stessa direzione, non ritoccata.
- **Prima** (prototipo): titolo in alto a sinistra, fila sotto, legenda in basso. Era lo stesso impianto di Hambro, Agnoletto e FM Sistemi; la didascalia galleggiava e la foto era ingrandita fino a 1,6 volte.
- **Ora**: la fila apre la pagina subito sotto la testata. Il titolo "Scarpe fatte a Villatora dal 1975" chiude la schermata in basso a sinistra, le tre righe su chi sono e "Orari dello spaccio" stanno in basso a destra. La didascalia "Cinque colori" è allineata in basso con la riga delle pastiglie, che stanno sotto l'asse di ogni scarpa.
- **Foto rifatta**: ingrandimento 1,09 volte a 1440 (massimo 1,3 sui file), nitidezza leggera (raggio 1,2, 60 %), segni d'uso attenuati su lilla e oliva, confini pitone-arancio e arancio-senape decisi anche dal colore.

### Le schermate

1. **1440x900.** Testata: logo, Spaccio, Storia, Per i negozi, Collezioni, telefono. Sotto, la fila larga 1060 px fino a 24 px dal bordo destro, con le cinque pastiglie; a sinistra "Cinque colori" a 28 px con "Décolleté con plateau, firma NicDean sul sottopiede." e "Tocca un colore per vederlo da solo". In basso il titolo "Scarpe fatte a Villatora dal 1975" in League Spartan 300 a 120 px su due righe; a destra le tre righe, "Orari dello spaccio" (porta a `#contatti`) e la riga degli orari "Dal lunedì al venerdì, 8-12 e 14:30-17" (link alla mappa).
2. **Sotto la piega**, quattro blocchi soltanto:
   - **storia e spaccio in una sezione di solo testo**: "Dal 1975 la famiglia Nicoletto fa scarpe a Villatora di Saonara", due righe sul prodotto e le tre date con filetti (1975, 1997, 2013); poi "Lo spaccio di via Lombardia" e la loro frase "Per donna, uomo e ragazzo. Da ginnastica, eleganti e sportive." a 80 px, come immagine tipografica, e tre righe su pagamento e appuntamento;
   - **"Per negozi, fiere ed eventi"**: testo sopra, poi la foto delle mani al montaggio a tutta larghezza (1440x756);
   - **la chiusura** "Calzature di tutti i tipi e di tutti i numeri" (frase loro): telefono grande, email, indirizzo e mappa, orari e pagamento, con i tronchetti a destra fino al bordo;
   - **il piede**.
3. **390.**
   - Testata: logo, bottone "Menu" (aria-expanded, bordo 1 px, al passaggio inverte i colori) e telefono.
   - La fila ingrandita 1,75 volte: tre scarpe intere e le due esterne tagliate.
   - Le cinque pastiglie a 22 px, poi "Cinque colori" e il testo sotto a 15 px.
   - Il titolo a 52 px, le tre righe e gli orari: tutto nella prima schermata da 844 px.
- **Altezze**: 4606 px a 1440, 5100 a 390, 5302 a 320, 4720 a 768, 4663 a 1024, 4660 a 1920 (da 4429 a 5447 tra 320 e 2560).

### Caratteri e colori

- **League Spartan** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una sola famiglia, servita dalla pagina in woff2 (latin e latin-ext, pesi 300-500 variabili).
  - Pesi: 300 per titolo, titoli di sezione, anni e telefono grande; 400 per il testo; 500 per menu, link e bottoni.
  - Perché: è un geometrico di impianto Futura che sta accanto alla scritta stencil del logo senza imitarla. Il riferimento è il geometrico leggero di Pollini e di ViBi Venezia: una scarpa, fondo chiaro, poche parole.
  - Zodiak di B non è stato portato: due voci indebolivano il gesto unico.
  - League Spartan non ha cifre tabellari vere: orari e recapiti sono su righe brevi allineate con la griglia (`dl` a due colonne).
- **Colori**:
  - gesso #F2EEE7 su tutta la pagina;
  - gesso scuro #E9E3DA solo nel piede, per staccarlo dalla chiusura;
  - inchiostro #1C1A17;
  - grigio caldo #625C53 per le note: 5,7:1 sul gesso e 5,2:1 sul gesso scuro;
  - rosso #C21F28 solo al passaggio sui link (5,2 e 4,7:1);
  - rosso del logo solo nel marchio;
  - verde #2E6B3A per il punto "aperto", che oggi non compare.

  Il colore lo portano le scarpe.

### Interazione

Cinque bottoni veri (`aria-pressed`), uno per colore.
- **Tocco o clic**: la foto passa di colpo alla versione con quel colore acceso e gli altri in grigio (saturazione al 18 %, schiariti di un quinto), senza dissolvenza. Sono sei immagini preparate con PIL e caricate dopo la pagina.
- **Didascalia**: (`aria-live`) dice il colore e il modello e offre "Chiedi se c'è in spaccio", con l'oggetto già scritto ("Décolleté con plateau, colore arancio", mailto a info@nicdean.it).
- **Tastiera**: secondo tocco o Esc riportano tutte le scarpe a colori; le frecce passano da un colore all'altro.
- **Telefono**: la foto scorre fino a mettere al centro la scarpa scelta, senza ingrandire oltre 1,75 volte (a 2,2 volte la foto da 1024 px mostrava i bordi delle maschere).
- **Stato attivo**: anello di 2 px, senza transizioni.

Nient'altro si muove: niente animazioni allo scorrere, niente effetti che seguono il cursore.

**Stato dello spaccio (innesto da B, spento).** Il codice c'è ma oggi la riga mostra solo gli orari, come chiesto, finché non si conferma che lo spaccio è aperto. Per accenderlo basta `STATO_ACCESO = true` nello script della pagina. Il calcolo usa l'ora italiana ed esclude il sabato, la domenica, agosto e i festivi nazionali: Pasquetta compresa, e il 4 ottobre dal 2026. Il testo è del tipo "Chiuso, riapre lunedì alle 8:00". Non c'è nessuna barra delle ore disegnata.

### Foto: origine e licenza

| File in sito/img/ | Origine | Licenza | Lavorazione |
|---|---|---|---|
| fila-*.jpg (6 stati, 760/1060/1264/1600/2120) | Nic Dean, `assets/originali/nuovo_images_index_foto1.jpg` (1024x683, loro sito di prova) | da chiarire: EXIF "Software: Google", autore ignoto | muro e piano portati al gesso; chiazze di luce e di colore attenuate su tutto il camoscio (lilla e oliva al 90 %, arancio e senape al 60 %); confini tra le scarpe disegnati, corretti sul colore e sfumati di 2,4 px; quattro scarpe in grigio per ogni stato, fondo invariato; 1600 e 2120 ingranditi con Lanczos e nitidezza proporzionale per gli schermi 2x |
| negozi-largo-*.jpg (960/1440/1600) e negozi-*.jpg (600/900/1200, telefono) | Fernanda Simões, Pexels 13524888 | Pexels License | taglio largo sulle mani e taglio 4:5; più calda, azzurri al 55 % di saturazione, velo di gesso al 10 % |
| chiusura-*.jpg | José Martin Segura Benites, Pexels 27256471 | Pexels License | taglio 1300x1625 sul risvolto, sopra l'arco dello specchio; più calda, velo di gesso all'8 % |
| logo-nicdean.png | rendering 4x del vettoriale del Flash `indice_nic.swf` (`assets/originali/logo-flash-reso-4x.png`) | dell'azienda | bianco reso trasparente, alto 96 px (2x del piede) |

Le foto di repertorio sono in `assets/CREDITI.md` (licenza verificata il 24/10/2026) e non compaiono nei CREDITI delle altre home della campagna (controllato di nuovo). Nessuna immagine generata. Nessuna foto di repertorio ha una didascalia o un testo che la faccia passare per loro: la sola didascalia è sulla fila, che è loro. I mocassini di repertorio, che stavano accanto a "prodotte interamente in azienda", sono stati tolti. La foto della chiusura non compare altrove nella pagina.

### Piede

- **In alto**: a sinistra il logo e una riga su chi sono; a destra la newsletter "Le novità dello spaccio" su una riga (campo, bottone inchiostro) con il consenso sotto.
- **Sotto un filetto, quattro colonne**:
  - Azienda: Storia, Fiere, Spaccio di fabbrica, Per i negozi;
  - Collezioni: Primavera, Estate, Autunno e inverno;
  - Contatti: telefono, fax, email, indirizzo in due righe;
  - Seguici: solo Facebook, come parola.
- **Riga legale**: "Nic Dean S.r.l., C.F. e P.IVA 02707240285, REA PD-300932, capitale sociale 51.000 euro i.v." con Privacy e Cookie a destra; a 390 diventa un testo continuo.
- **Newsletter**: sì, perché lo spaccio ha clienti privati e il loro sito dava già collezioni per stagione, sconti e chiusure per ferie. Il browser controlla email e consenso (campi obbligatori, con il suo avviso accanto al campo); se sono a posto una riga `aria-live` dice "Grazie, la newsletter sarà attiva a breve." Non invia nulla finché non si collega un servizio (LEGGIMI).

### Giro finale: cosa è cambiato dopo il giudice cieco (57 su 80)

- **La fila**: chiazze attenuate su tutto il camoscio, non solo sulla punta di lilla e oliva; file da 1060, 1600 e 2120 px nello srcset (prima il più grande era 1264). Resta una foto da 1024 px: nitida a 1x, non un 2x vero. La foto in studio è la condizione per mandare la home (LEGGIMI).
- **Il gesto**: scarpe spente in grigio invece che bianco latte, fondo che resta gesso; tolta la scheggia marrone a sinistra del tacco arancio (il colore decide solo dove l'arancio è chiaro e saturo) e i puntini grigi sul bordo destro dell'arancio; confini senape-oliva e oliva-lilla lisciati (media su 31 righe), niente più scaletta; al telefono niente ingrandimento a 2,2 volte.
- **Date vecchie fuori dalla pagina**: tolti "collezione estate 2017" (didascalia e oggetto della mail) e la riga della fiera di marzo 2012.
- **Niente più zig-zag**: storia e spaccio sono una sola sezione di testo; "Per negozi" ha il testo sopra e la foto a tutta larghezza sotto; solo la chiusura ha testo e foto affiancati. Tolta la foto dei mocassini.
- **Parole**: titolo "Scarpe fatte a Villatora dal 1975" (al posto di "Scarpe da donna", che contraddiceva "Per donna, uomo e ragazzo"); tolto "di livello medio-fine".
- **Foto**: negozi scaldata con gli azzurri spenti; chiusura ritagliata sopra l'arco dello specchio e scaldata.
- **Minori**: "Orari dello spaccio" porta a `#contatti`; nella chiusura testo dall'alto con 64 px tra titolo e recapiti (niente più vuoto da space-between); a 768 il testo d'apertura va su tutta la riga (52ch); newsletter con risposta; a 320 orari su una colonna.

### Controlli

- **Larghezze guardate a pezzi**: 1440 intera, 390 intera, 320 intera, 768, 1024 e 1920 (prime schermate e pagine). `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 414, 600, 768, 900, 1024, 1100, 1280, 1440, 1600, 1920 e 2560 (`_prova/script/controlli.mjs`).
- **Gesto provato** con Playwright: Invio, frecce destra e sinistra, Esc, spazio due volte; tocco a 390 su oliva, lilla, pitone e secondo tocco; `aria-pressed`, immagine caricata, didascalia e oggetto della mail corretti in ogni stato. Stati guardati ingranditi tre volte nei punti dove le scarpe si toccano.
- **Collegamenti**: `tel:+39049640672`, `mailto:info@nicdean.it` (anche con oggetto), mappa Google su via Lombardia 29, Facebook; nessuna ancora interna senza destinazione. Menu del telefono: si apre, si chiude col link e con Esc.
- **Segnali da IA**: `segnali.sh` dà 0 soglie bloccanti e 0 da guardare. Foto oltre il 35 % della pagina, una famiglia, H2 di 5 misure, 6 filetti larghi, nessuna freccia, nessuna etichetta maiuscola.
- **Nessun U+2014** in pagina, nota, LEGGIMI e script.
- **Divieti del committente**: nessun gradiente viola, nessuna card, nessuna icona, nessuna dissolvenza, nessun corsivo d'accento.
- **Limite noto**: la fila resta una foto da 1024 px con cinque scarpe ritagliate a mano; con una foto per colore dalla stessa posizione il gesto diventa esatto (LEGGIMI, prima foto da rifare).