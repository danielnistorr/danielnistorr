# Home di Bordin Garden & Vivai: nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in tre larghezze più un JPEG di riserva), caratteri in `sito/fonts/`. La versione 1 com'era prima di questo passaggio (sito e screenshot) è copiata in `_prova/versione-1-originale/`. Per Bordin non c'era una versione 1 con l'uso: l'uso della scheda (`_prova/uso/SCHEDA.md`) è risolto qui per la prima volta.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home, Bordin compare due volte: istantanee dei campi e mestieri in righe di testo), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Union e Petersham Nurseries (a pezzi) e la prima parte di Joseph Brot; il foglio `_invio/zona/home/livello-professionale.jpg` (colonna di destra: Unicar, Oby, Fornasiero) e la nota di Fornasiero.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, poi `pro_controlli.mjs`). Prove d'uso: `node _prova/script/pro_uso.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (7.900 px circa), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11.400 px circa), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (dal Vivai al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e a 320, 768 e 1024.

### Che cosa è cambiato

- **La faccia è il Garden, non il vivaio** (SCHEDA, par. 1): apertura con la piramide (G6, la loro foto migliore, 6/6) e non più con le zolle; il titolo "Produciamo natura" passa alla sezione Vivai, che è il suo posto.
- **Titolo**: "Passione per il verde dal 1955", la loro frase (book "I nostri giardini", p. 3), con l'occhiello "Garden center, giardini e vivai a Saonara, Padova": mestiere, luogo e prova nella prima riga. Zodiak 400, 86 px a 1440 e 42 px a 390 (fascia della famiglia B); minuscolo come la scritta del logo, non maiuscolo.
- **Prima schermata, telefono 390x844**: testata fissa con il logo vero e "Chiama 049 8791098" (44 px); occhiello, titolo, la riga di stato in Zodiak 24 px con il pallino verde ("Il Garden è aperto, chiude alle 12:30", "Il Garden ora è chiuso, riapre domani alle 8:30", "Oggi è festa: chiamate prima di passare"), l'orario di oggi, "Chiama il Garden 049 8791098" a tutta larghezza (48 px), "Indicazioni" (Google Maps, percorso su via dei Vivai 6) e "WhatsApp"; sotto, la piramide in 3:2 (da 498 a 758 px). Tutto nei primi 844 px.
- **Prima schermata, 1440x900**: titolo su una riga; a sinistra stato, orario di oggi, i tre bottoni, una riga loro ("Venite a visitarci...") e le due porte, "Volete un giardino? Vedete i lavori e chiedete un sopralluogo" e "Vivai, esemplari in zolla, per professionisti: 049 640156"; a destra la piramide in 4:3 (756x567). La porta dei Giardini e quella dei Vivai si vedono senza scorrere. Due colonne fino a 901 px; sotto, in colonna.
- **Seconda schermata: i tre servizi in schede** (regola 9): Garden (il reparto delle piante grasse e dei bonsai, con i vasi in terracotta e il cartello Bordin), Giardini (la barchessa di Villa Palladiana), Vivai (le zolle in rete); stessa foto 4:3, nome, una riga, il telefono giusto per ognuno e il link; tutta la scheda è cliccabile.
- **Il Garden**: "Il Garden, una piramide di vetro dal 1996", le loro parole, i sei reparti dal loro elenco, la scheda della sede con la tabella degli orari (oggi evidenziato), Chiama, Indicazioni, WhatsApp e email; tre tessere fotografiche dei reparti (piante da interno, piante da esterno, vasi, arredo e idee regalo).
- **La storia su blocco scuro**: la loro frase "Siamo sempre alla ricerca di nuove specie botaniche e piante particolari, che testiamo nei nostri vivai" (book) come manifesto, la storia in tre righe e cinque numeri veri in verde foglia (1955, 1996, 3ª generazione, 33 album, 1 anno di garanzia).
- **Giardini**: "Affidatevi alla nostra esperienza" (la loro slide), tre lavori con il nome e la foto (Villa Palladiana grande, Giardino a Venezia, un giardino privato) e il link ai 33 album sul sito di oggi; poi "Come nasce un giardino" con i 4 passi del book e la garanzia, accanto al modulo "Chiedete un sopralluogo".
- **Modulo** (B: tipo di richiesta): nome, telefono, comune, sei caselle (giardino nuovo, terrazzo o verde pensile, trapianto di esemplari, giardino storico, manutenzione, piante per uffici), due righe; "Prepara l'email" compone un mailto a info@bordingarden.it con oggetto "Richiesta di sopralluogo, comune (tipi)" e tutti i campi nel testo; foto o disegno da allegare all'email o da mandare su WhatsApp (link precompilato con il comune). Da collegare a un servizio (LEGGIMI).
- **Vivai su blocco scuro**: "Produciamo natura", le loro frasi (zolla o vaso, spedizione e messa a dimora in tutta Italia, anche grandi esemplari, architetti e impresari), "Chiama il vivaio 049 640156", WhatsApp 350 5859658, "Mandate la lista delle piante" (mailto a info@bordinvivai.it con oggetto), la gru che solleva l'olivo in zolla (BB1) con una didascalia, gli orari del vivaio in tabella e "Indicazioni per il vivaio".
- **Piede** in quattro colonne: marchio, Garden, Vivai (indirizzo con mappa, telefono, WhatsApp, email, orari), Bordin (sezioni, lavora con noi, Facebook e Instagram "novità e promozioni"); riga legale.
- **Tolti**: l'interruttore "In vivaio / In giardino", "Tre mestieri sulla stessa strada", "Dal vivaio al giardino", la newsletter che non inviava nulla, il fondo carta #F3F0E8, i link a `#`, le foto VB4 e Giardini_3ok con il filtro del giro di prima (Giardini_3ok resta come terzo lavoro, con la vignettatura compensata).

### Foto: decisione "niente"

Nessuna foto di repertorio, nessuna illustrazione. Restano solo foto vere di Bordin (`assets/originali/`), nei formati che reggono, con un solo trattamento (`pro_img.py`: nero non schiacciato, gamma 0,97, saturazione -8 %, -18 % su BB1 e Giardini_3ok, un filo più calde, maschera di contrasto leggera). Due formati in tutta la pagina: 4:3 e 3:2.

| In pagina | File | Origine | Taglio |
|---|---|---|---|
| Apertura | `garden-piramide-43`, `garden-piramide-32` | G6, 1920x1080 | 4:3 da 1440x1080 (computer), 3:2 da 1620x1080 (telefono e tablet) |
| Scheda Garden | `garden-grasse-43` | G8 (piante grasse, bonsai, terracotta) | 4:3 |
| Scheda Giardini | `giardini-villa-43` | album Villa Palladiana, DO_Mix_148 | 4:3 sotto il logo stampato (da y = 150) |
| Scheda Vivai | `vivai-zolle-43` | VB2 | 4:3 |
| Reparti | `garden-interno-43`, `garden-esterno-43`, `garden-regali-43` | G5, G1, G10 | 4:3 |
| Lavori | `lavoro-villa-32`, `lavoro-venezia-32`, `lavoro-acero-32` | DO_Mix_146, DO_MorosiniDopo4, Giardini_3ok | 3:2, sotto il logo stampato |
| Vivai | `vivai-gru-43` | BB1, 1600x1200 | intera |
| Logo | `logo-bordin-360.png` | PNG 360x126 | 150 px in testata, 112 a 390, 170 nel piede |

Limite dichiarato: la serie non è di un solo fotografo. Le foto del Garden (G1, G5, G6, G8, G10) hanno la stessa luce di giorno; BB1 e gli album hanno colori e mezzi di un'altra epoca. Il trattamento comune avvicina, non uguaglia: per questo nel LEGGIMI c'è la giornata di foto.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa**: PASSA. "Garden e orari" è la prima voce del menu; a 390, a metà pagina, "Chiama 049 8791098" in testata è visibile e toccabile (187x44 px); sotto 375 px dice "Chiama". 9 link `tel:` in pagina.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844 (occhiello "Garden center, giardini e vivai a Saonara, Padova", "dal 1955" nel titolo, "Chiama il Garden 049 8791098", a 390 a tutta larghezza).
3. **Immagine vera nell'apertura**: PASSA. La piramide del Garden, foto loro, intera nella prima schermata a 1440 (756x567) e a 390 (390x260).
4. **Zero repertorio**: PASSA. "indicativ" 0, nessun Unsplash o Pexels in pagina.
5. **Foto in serie**: PASSA con il limite sopra. 11 foto a 1440, due formati (4:3 e 3:2), una sola didascalia (la gru); le altre hanno il nome come scheda.
6. **Palette dal marchio**: PASSA. Foglia #39A559 (logo: pallino "aperto", numeri, occhielli sul blocco scuro, fuoco), bosco #17432A (suo verde scuro: bottoni, blocchi scuri), neutri bianco, nebbia #F1F3EF, inchiostro #1C2420, grigio del logo #5A5959. Niente beige. Contrasti: bianco su bosco 11,2:1; foglia su bosco 3,6:1 solo per le cifre da 56 px e le etichette in grassetto.
7. **Scala corta e leggibile**: PASSA. 1440: 86, 56, 30, 22, 18, 16 px; 390: 42, 32, 24, 20, 17, 16, 14 px. Testo 18/17 px. Il 14 px è nella riga legale e nell'occhiello dell'apertura sul telefono.
8. **Due famiglie**: PASSA. Zodiak 400 (titoli, nomi, cifre, stato) e Switzer 400/600 (testo, etichette, bottoni, modulo). Pesi tolti: Zodiak 300 e Switzer 500; aggiunto Switzer 600 (Fontshare, 3/11/2026, copia in `assets/fonts-scaricati/`).
9. **Servizi in schede con foto**: PASSA. Tre colonne, foto 4:3 uguali, nome, riga, telefono e link, scheda tutta cliccabile.
10. **Almeno tre tipi di prove**: NON PASSA. C'è un tipo: cinque numeri aziendali veri. Recensioni con nome e comune: nelle fonti solo sintesi degli estratti (voto Google 4,3 su un aggregatore), non le invento e non metto il voto finché non è verificato; certificazioni e fornitori: nessuno nelle fonti; clienti con il nome: nessuno (i lavori hanno il luogo). Da chiedere (LEGGIMI).
11. **Lavori con un nome**: NON PASSA del tutto. Tre lavori con il luogo dall'album (Villa Palladiana, Giardino a Venezia) e uno senza (giardino privato), la foto grande è a 867 px su 1440 e le altre a 644; mancano anno e dati (metri, piante, tempi): non sono nelle fonti.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: Garden e sopralluogo su nebbia, storia e Vivai su bosco; spazi 120 px a 1440 e 72 px a 390; margini 64 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e a filo, raggio 3 px, 52 px a 1440 e 48 a 390 (44 in testata), testo 16 px; ogni Chiama ha il numero.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta in caselle; Garden e Vivai con tabella degli orari, Indicazioni (percorso Google Maps) e Chiama; nessun iframe.
15. **Piede completo**: PASSA in parte. Quattro colonne, ragione sociale, P.IVA, REA, sede, telefoni, email, WhatsApp, orari, le due sedi, social con il sottotitolo, testo da 16 px (14 la riga legale). "Privacy e cookie" è scritto ma non è un link: l'indirizzo dell'informativa iubenda non l'ho letto (sito con firewall); certificazioni: nessuna nelle fonti.

### Uso: i compiti della scheda

- Cliente del Garden (390): stato, Chiama, Indicazioni e WhatsApp senza scorrere; "Chiama" resta in testata; la scheda Garden con "piante grasse, bonsai, vasi in terracotta" e la loro foto del reparto è a 896 px (al primo scorrimento); i reparti con le foto subito dopo. Stato giusto a 10 ore e giorni provati (`pro_uso.mjs`: lunedì mattina chiuso, lunedì pomeriggio, martedì prima delle 8:30, pausa, sera, sabato, domenica, 8 dicembre e Pasquetta 2027 "Oggi è festa: chiamate prima di passare"); con JavaScript spento la riga dice gli orari della settimana.
- Chi vuole un giardino (1440): la porta "Volete un giardino?" nella prima schermata; tre giardini veri con il luogo nella schermata dopo la storia; 4 passi e garanzia accanto al modulo; modulo di 4 campi più caselle, foto via email o WhatsApp. Il prima e il dopo affiancati non ci sono: gli album con PRIMA e DOPO non sono tutti scaricati (firewall), e gli originali senza logo vanno chiesti.
- Professionista (1440): la porta Vivai con il numero nella prima schermata; nella sezione Vivai zolla o vaso, spedizione in tutta Italia, anche grandi esemplari, 049 640156, WhatsApp, info@bordinvivai.it con oggetto, orari e indicazioni per via dei Vivai 14.

### Controlli generali

- Scorrimento orizzontale: 0 a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 px.
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024 e 1440. Corretti durante il lavoro: le righe "telefono / link" delle schede a 768 (ora vanno a capo), lo spazio mancante prima della freccia nei link a riga, l'apertura a 1024 (ora in due colonne fino a 901 px).
- Collegamenti: `tel:+390498791098`, `tel:+39049640156`; `mailto:info@bordingarden.it` (anche dal modulo, con oggetto), `mailto:info@bordinvivai.it` (con oggetto "Richiesta piante dal vivaio" e "Lavora con noi"); mappe `google.com/maps/dir/?api=1&destination=` sulle coordinate del Garden (45.38608, 11.961015) e dei Vivai (45.3857, 11.9625); WhatsApp 350 1376907 e 350 5859658; nessuna ancora rotta, nessun `href="#"`.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi. Console senza errori.

### Caratteri e licenze

Zodiak (400) e Switzer (400, 600), Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito; i file non vanno ridistribuiti da soli), serviti dalla pagina in `sito/fonts/`.

---

## Versione 1 originale (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (JPEG e WebP in tre larghezze), caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, screenshot, segnali); le prove di interazione e larghezze con `node _prova/script/fin_prove.mjs`. Base: il prototipo A "L'esemplare", scelto dal giudice (`_prova/giudizio.json`), rifinito dopo il giudizio cieco (ultimo giro, sotto).

## Idea

Gli esemplari dei Vivai Bordin con la zolla avvolta nella rete. La zolla in rete è il segno del loro mestiere ("sia in zolla che in vaso", "trapianti e messa a dimora di piante esemplari", "gestendo anche la parte logistica della spedizione"): la foto viene dal loro vivaio, non da un archivio. Il titolo è la loro frase, "Produciamo natura" (slide dei Vivai), con l'anno 1955. Poi la pagina segue la pianta: i tre mestieri sulla stessa strada, dal vivaio al giardino, il Garden, la visita.

## Ultimo giro: cosa è cambiato

1. **Apertura senza scontorno.** Lo scontorno dell'albero (rami spezzati, aloni, bruno grigio) è tolto. Al suo posto la foto VB2 vera, intera e a colori: la fila delle zolle in rete sul prato, i fusti, la siepe dietro. Taglio largo 2,2:1 (1940x880 dall'originale 2128x1416, via la ghiaia a sinistra e la casa a destra) incorniciato nei margini della pagina come in Margheriti Piante; taglio quadrato per il telefono (art direction con `<picture>`). Saturazione quasi piena (0,98), cielo smorzato, maschera di contrasto leggera. Verde (tinta 70-160, saturazione sopra 50): 42,5 % del taglio largo, 29,5 % del quadrato (la siepe scura non conta).
2. **Composizione nuova, non più quella di Mario Agnoletto.** Tolti i tre segni punto-filetto-numero e la colonna delle legende. Ora: titolo a sinistra su due righe, a destra la riga su chi sono, il bottone e la riga "aperto adesso", sotto la foto a tutta la larghezza utile con una sola didascalia ("Vivai Bordin. Esemplari a foglia caduca appena zollati, la zolla avvolta nella rete." e, a destra, "In zolla o in vaso, spediti in tutta Italia"). Nessun elemento `.segno` o `.chiave` in pagina (controllato da `fin_prove.mjs`).
3. **Telefono.** A 390 l'ordine è testata, titolo, foto (quadrata, 390x390, da y = 210), didascalia, riga, bottone, "aperto adesso": tutto nei primi 844 px. A 768 la foto è a tutta larghezza (768x348). A 320 la foto parte a 248 px.
4. **Interruttore "In vivaio / In giardino"** (prima "In vivaio / Messo a dimora", con l'arco di pietra della Villa Palladiana che non mostrava una pianta messa a dimora). Ora: i filari di esemplari in foglia nei campi (VB4, primavera) e un giardino privato finito con un albero multitronco nel prato (Giardini_3ok, dalla slide "Giardini" della loro home, vignettatura del filtro compensata). Le due foto sono verdi e luminose e mantengono la promessa del testo: crescono nei campi, finiscono nei giardini. La foto VB2 non si ripete più.
5. **"Come nasce un giardino"**: i quattro passi ora sono righe a tutta larghezza come quelle dei mestieri (numero, titolo in Zodiak, una riga di testo dalla colonna x = 512); la frase della garanzia è allineata alla stessa colonna. A 1440 il testo dei passi sta in una colonna di 812 px, non più in quattro colonne da 306.
6. **Intro dei mestieri**: il titolo su una riga sola, il paragrafo nella colonna delle descrizioni sotto (x = 512).
7. **Chiusura più corta**: il Garden resta completo (telefono grande, indirizzo con mappa, email, WhatsApp, orari con "oggi"); i Vivai in tre righe (telefono, indirizzo con mappa, "Lun–ven 8–12 e 14–18 · sabato mattina su appuntamento"). Il bottone dell'apertura ora dice "Orari e indicazioni", così non ripete il titolo "Venite a visitarci".
8. **Piede a 1024**: logo e newsletter sulla prima riga, le tre colonne di link sotto.
9. **Testi**: la garanzia riportata vicino alla fonte ("Tutte le piante dei nostri giardini hanno un anno di garanzia d'attecchimento"); tolti "aperto sei giorni su sette", "villa palladiana" e la legenda "Dal vivaio di via dei Vivai 14".
10. **Preload dei caratteri tolti**: su file:// davano 4 errori CORS. Ora la console è vuota a tutte le larghezze.

## Le prime due schermate

1. **Apertura (1440x900)**: logo vero, cinque voci di menu, il telefono del Garden. "Produciamo / natura dal 1955" in Zodiak 300 a 92 px; a destra (colonne 8-12) la riga, il bottone "Orari e indicazioni" e "Garden, via dei Vivai 6: aperto, fino alle 19:00 · Indicazioni", calcolata con l'ora di Roma sugli orari veri (pallino pieno se aperto, vuoto se chiuso). La foto parte a 394 px, alta 588: nella prima schermata si vedono le zolle intere e il prato.
2. **Tre mestieri sulla stessa strada**: la storia in quattro righe (1955 Saverio e Alcide, 1996 il Garden, la terza generazione) e tre righe tipografiche, Vivai, Garden, Giardini, con l'indirizzo e un link.

Poi "Dal vivaio al giardino" con l'interruttore e la foto a tutta larghezza in 2,2:1, i 4 passi del book e la garanzia; "Il Garden, una piramide di vetro dal 1996" con G6; la chiusura "Venite a visitarci" con le bletille; il piede. Altezza: 6393 px a 1440, 6569 px a 390.

## Caratteri e colori

- **Zodiak** 300 e 400 (titoli, nomi dei mestieri e dei passi, le sedi; mai corsivo) e **Switzer** 400 e 500 (testo, menu, orari, didascalie; cifre tabellari dove ci sono numeri e orari). Indian Type Foundry, da Fontshare, serviti dalla pagina (`sito/fonts/*.woff2`); **licenza ITF Free Font License**, uso commerciale libero, i file non vanno ridistribuiti da soli. Motivo: un serif dritto e affilato accanto al serif classico del logo Bordin, come Freight Big accanto al Futura di Sarah Price Landscapes; il testo in un grottesco asciutto.
- **Colori**: carta #F3F0E8 (fondo unico), inchiostro verde quasi nero #1F2A1F, grigio #575653 (6,4:1 sulla carta), filetti al 16 % dell'inchiostro; il verde #39A559 resta solo nella foglia del logo. Il verde vero ora sta nelle foto.

## Interazione

- **In vivaio / In giardino**: due bottoni veri (`aria-pressed`, 48 px, frecce sinistra e destra), cambio netto senza dissolvenza, didascalia letta dagli screen reader.
- **Aperto adesso**: nessuna animazione, si calcola all'apertura; nella chiusura la riga di oggi negli orari del Garden è in nero con la parola "oggi".
- Altro script: il bottone "Menu" sotto i 900 px e i messaggi della newsletter (che non invia nulla).

## Foto: origine e licenza

Tutte le foto in pagina sono di Bordin (dal loro sito, `assets/originali/`). Nessuna foto di repertorio, nessuna immagine generata dall'IA, nessun marchio di altri. Trattamento (PIL e OpenCV, `_prova/script/fin_img.py`): luce sollevata appena, nero non schiacciato, azzurro del cielo smorzato; saturazione quasi piena nell'apertura, -10/-20 % altrove.

| In pagina | File | Origine | Lavorazione |
|---|---|---|---|
| Apertura | `zolle-largo-960/1440/1940`, `zolle-quadro-600/800/1010` | Bordin, pagina Vivai, `resources--32--VB2.jpg` (2128x1416) | taglio largo 1940x880 e quadrato 1010x1010, nessuno scontorno |
| In vivaio | `vivaio-campo-*` | Bordin, pagina Vivai, `resources--32--VB4.jpg` (2128x1416) | 2,2:1 sui filari |
| In giardino | `giardino-finito-*` | Bordin, home, `home--Giardini_3ok.jpg` (1960x1169) | 2,2:1, vignettatura compensata, saturazione -20 % |
| Il Garden | `garden-piramide-*` | Bordin, `resources--31--G6.jpg` | 1,85:1 a tutta larghezza |
| Chiusura | `garden-ingresso-*` | Bordin, `resources--31--G1.jpg` | quadrata, colore raddrizzato; a filo del bordo destro |
| Logo | `logo-bordin-360.png` | Bordin, PNG 360x126 | 150 px nella testata, 180 px nel piede (2x) |

**Limite dichiarato**: VB2 ha luce piatta ed è nitida solo a 1,5x a 1440 (1940 px per 1296 px CSS); a 2560 la foto è ingrandita. La foto dal vero descritta nel LEGGIMI la sostituisce.

## Piede

Logo vero con una riga su chi sono; colonne **Bordin** (La storia, Vivai, Garden, Giardini, Album dei giardini, Notizie, Lavora con noi), **Giardini** (le cinque voci di servizio), **Contatti** (due telefoni, due email, Orari); **Notizie dal Garden**: campo email, "Iscriviti", consenso privacy. La newsletter ha senso: il Garden ha clienti privati, annuncia novità sui social, ha stagioni e fioriture; non funziona finché non si collega a un servizio. Facebook e Instagram come parole. Ultima riga: ragione sociale dei registri, sede legale, P.IVA e C.F., REA, Privacy, Cookie. A 390 le colonne si impilano in ordine; tra 900 e 1200 px logo e newsletter sopra, link sotto.

## Controlli (ultimo giro)

- Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440 e 1920 (`screenshot/home/` tiene 1440, 390, le prime schermate e la chiusura).
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 768, 900, 1024, 1280, 1440, 1920 e 2560.
- Interruttore: freccia destra (passa a "In giardino", focus e `aria-pressed` giusti, didascalia cambiata), freccia sinistra, Tab e Invio, tocco a 390 con `hasTouch`. Menu a 390 aperto col tocco.
- Collegamenti: `tel:+390498791098`, `tel:+39049640156`, `mailto:info@bordingarden.it`, `mailto:info@bordinvivai.it`, mappe Google sulle coordinate del Garden (45.38608, 11.961015) e dei Vivai (45.3857, 11.9625), WhatsApp, Facebook, Instagram.
- Console: 0 errori su file:// a tutte le larghezze.
- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare. Foto 40,9 %, 19 filetti, Switzer 90 % e Zodiak 10 %, 3 misure di H2, nessun titolo col punto, nessuna etichetta maiuscola sopra i titoli, nessuna numerazione 01/02.
- Divieti del committente: niente gradienti, niente Inter, niente badge, niente icone, niente comparse allo scorrere, niente effetti sul cursore, niente riquadri con ombra, niente corsivo. Nessun carattere U+2014 in pagina, NOTA e LEGGIMI.
- Dati: tutti da 01-analisi.md. Da confermare (LEGGIMI): la garanzia d'attecchimento, i luoghi delle foto, il giardino di Giardini_3ok, la ragione sociale nel piede.
