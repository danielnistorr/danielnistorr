# Home di Bordin Garden & Vivai: nota

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in tre larghezze più un JPEG di riserva), caratteri in `sito/fonts/`. La versione 1 com'era prima del livello professionale (sito e screenshot) è copiata in `_prova/versione-1-originale/`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (in fogli di confronto) e le pagine intere di Petersham Nurseries e Union, a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, poi `pro_controlli.mjs`). Prove d'uso: `node _prova/script/pro_uso.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8.270 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10.060 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (dal Vivai al piede). Guardati a pezzi a 1440 e 390, e a 320, 768 e 1024.

### Ritocco finale (3 novembre 2026, dopo il controllore e i due clienti tipo)

- **Apertura senza riquadro.** Sopra i 900 px la piramide (G6, nuovo taglio 10:9 da 1200x1080) esce fino al bordo destro e sale fino alla testata, alta quanto la finestra meno la testata (812 px a 1440x900). A sinistra, sulla colonna: occhiello, titolo su tre righe ("Passione / per il verde / dal 1955", 86 px), lo stato, l'orario di oggi, i tre bottoni in una riga, le due porte in fondo. Tolto il vuoto sotto "Venite a visitarci": la frase è passata all'inizio del testo del Garden. Sotto i 900 px l'ordine non cambia (bottoni sopra la foto, come chiede la SCHEDA).
- **Gesto di scala.** Nella storia, su verde bosco, "1955" in Zodiak a 240 px nel verde della foglia (210 a 1300, 180 a 1100, 128 a 390, 112 sotto 375 px), con la riga dei fratelli Saverio e Alcide; gli altri quattro numeri restano in fila sotto.
- **Testata a 390**: alta 72 px; logo a 112 px davvero (`.logo{flex:none}`), il bottone dice solo "049 8791098" da 375 a 700 px (la parola "Chiama" resta nell'aria-label e torna sotto 375, dove sparisce il numero); bottone e Menu alti 48 px.
- **Lavori uno per riga**, foto in 7 colonne (755 px a 1440) e testo in 4, alternati a sinistra e a destra. Il "Giardino privato" (Giardini_3ok, con il filtro e non confermato) è tolto: al suo posto **un'aiuola prima e dopo**, le due foto delle pagine 12 e 13 del loro book "I nostri giardini", affiancate in 3:2 con le didascalie "Prima" e "Dopo" (le scritte stampate nelle foto restano fuori dal taglio). Tolta la riga "Nell'album: prima, durante e dopo".
- **Foto in serie**: la gru (BB1) tagliata stretta sulla zolla e sulla chioma (920x690 da 1600x1200, via il camion arancione e l'asfalto), saturazione 0,78. Nel Garden una quarta tessera, "Piante grasse e bonsai" (G8 in un taglio più stretto sui cactus e sul cartello del Garden), e "Vasi, arredo e idee regalo" diventa "Vasi e idee regalo" (la foto mostra un banco di regali, non arredo).
- **Pagina a 390 più corta**: da 11.431 a 10.060 px. Schede dei servizi in riga (foto 4:3 di 136 px, nome, telefono e link, la riga sotto), reparti 2x2, elenco del Garden su due colonne, caselle del modulo su due colonne, prima e dopo affiancati, spazio tra le sezioni 64 px, nel piede tolte le voci che ripetono il menu, la riga del marchio e gli orari (sono nelle sezioni). Non sono sceso sotto gli 8.500 px: il resto è il contenuto che serve ai compiti della SCHEDA (orari, quattro passi, modulo, vivaio).
- **Caratteri con ruoli fissi**: i nomi dei reparti e dei quattro passi ora sono in Zodiak a ogni larghezza (prima, a 390, i reparti passavano a Switzer 600, e i passi erano in Switzer). Spazio tra le parole +0,1 em su tutta la pagina ("Garden e orari", non più "Gardene orari"); crenatura spenta nell'occhiello maiuscolo, dove "PADOVA" si apriva tra O e V.
- **Modulo**: quattro caselle (giardino nuovo, terrazzo o verde pensile, trapianto di esemplari, manutenzione), nuovo campo corto "Metri quadri, circa" (SCHEDA par. 3), bottone "Apri l'email già scritta"; l'esito dice "Dovrebbe aprirsi la vostra email... Se non si apre nulla, scrivete a info@bordingarden.it o usate WhatsApp"; sotto il titolo "Con la foto sul telefono fate prima su WhatsApp". Passo 2 riscritto senza la frase monca ("Vi presentiamo la proposta e il preventivo; poi venite in vivaio a vedere dal vivo le piante proposte").
- **Uso**: WhatsApp del Garden con il testo pronto ("Buongiorno, vorrei sapere se avete "); negli ultimi 30 minuti lo stato dice "Il Garden chiude tra 10 minuti, alle 19:00"; "Tutti gli orari" ha un'area di tocco di 44 px; le ancore arrivano sotto la testata senza la striscia della sezione prima (`scroll-padding-top` uguale alla testata).
- **Nel markup** un commento segna il posto per tre recensioni nella storia, da riempire solo con quelle autorizzate (LEGGIMI).

### Foto: decisione "niente"

Nessuna foto di repertorio, nessuna illustrazione. Solo foto vere di Bordin (`assets/originali/`, compreso il loro book), con un solo trattamento (`pro_img.py`: nero non schiacciato, gamma 0,97, saturazione -8 %, -12/-22 % su BB1 e sulle pagine del book, un filo più calde, maschera di contrasto leggera). Tre formati in tutta la pagina: 4:3, 3:2 e il 10:9 dell'apertura da 901 px in su.

| In pagina | File | Origine | Taglio |
|---|---|---|---|
| Apertura (da 901 px) | `garden-piramide-109` | G6, 1920x1080 | 1200x1080 da x = 400, esce fino al bordo destro |
| Apertura (telefono e tablet) | `garden-piramide-32` | G6 | 3:2 da 1620x1080 |
| Scheda Garden | `garden-grasse-43` | G8 (piante grasse, bonsai, terracotta) | 4:3 |
| Scheda Giardini | `giardini-villa-43` | album Villa Palladiana, DO_Mix_148 | 4:3 sotto il logo stampato (da y = 150) |
| Scheda Vivai | `vivai-zolle-43` | VB2 | 4:3 |
| Reparti | `garden-interno-43`, `garden-esterno-43`, `garden-cactus-43`, `garden-regali-43` | G5, G1, G8 (taglio stretto), G10 | 4:3 |
| Lavori | `lavoro-villa-32`, `lavoro-venezia-32` | DO_Mix_146, DO_MorosiniDopo4 | 3:2, sotto il logo stampato |
| Prima e dopo | `aiuola-prima-32`, `aiuola-dopo-32` | book "I nostri giardini", pagine 12 e 13 (1024x721) | 3:2, 945x630 sopra le scritte "Prima" e "Dopo" |
| Vivai | `vivai-gru-43` | BB1, 1600x1200 | 4:3, 920x690 sulla zolla e sulla chioma |
| Logo | `logo-bordin-360.png` | PNG 360x126 | 150 px in testata, 112 a 390 (100 sotto 375), 170 nel piede |

Limite dichiarato: la serie non è di un solo fotografo. Le foto del Garden (G1, G5, G6, G8, G10) hanno la stessa luce di giorno; BB1, gli album e il book hanno colori e mezzi di altri anni, e il "Dopo" del book ha ombre dure. Il trattamento comune avvicina, non uguaglia: per questo nel LEGGIMI c'è la giornata di foto.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa**: PASSA. "Garden e orari" è la prima voce del menu; a 390, a metà pagina, il bottone "049 8791098" in testata è visibile e toccabile (125x48 px, aria-label "Chiama il Garden, 049 8791098"); sotto 375 px dice "Chiama". 9 link `tel:` in pagina.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844 (occhiello "Garden center, giardini e vivai a Saonara, Padova", "dal 1955" nel titolo, "Chiama il Garden 049 8791098", a 390 a tutta larghezza, 48 px).
3. **Immagine vera nell'apertura**: PASSA. La piramide del Garden, foto loro, a tutta altezza fino al bordo destro a 1440 (708x812) e a 390 (390x260). Nessuna persona: è il limite delle foto che hanno (LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" 0, nessun Unsplash o Pexels, tutte le immagini da `assets/originali` con `pro_img.py`.
5. **Foto in serie**: PASSA IN PARTE. 13 foto a 1440, tre formati (4:3, 3:2, 10:9), tre didascalie (Prima, Dopo, la gru); la luce non è una sola (vedi il limite sopra). La gru più stretta e senza camion e il giardino con il filtro tolto la rendono più unita di prima.
6. **Palette dal marchio**: PASSA. Foglia #39A559 (logo: pallino "aperto", il 1955 grande, i numeri, gli occhielli sul blocco scuro, il fuoco), bosco #17432A (bottoni, blocchi scuri), neutri bianco, nebbia #F1F3EF, inchiostro #1C2420, grigio del logo #5A5959. Niente beige.
7. **Scala corta e leggibile**: PASSA. 1440: 240, 86, 56, 30, 22, 18, 16 px; 390: 128, 42, 32, 24, 20, 17, 16 px (il 14 px dell'occhiello sul telefono è tolto). Testo 18/17 px; nessun testo sotto 14 px.
8. **Due famiglie con ruoli fissi**: PASSA. Zodiak 400 per titoli, nomi (schede, reparti, passi, lavori, porte), cifre e stato a ogni larghezza; Switzer 400/600 per testo, etichette, bottoni e modulo.
9. **Servizi in schede con foto**: PASSA. Tre colonne a 1440, foto 4:3 uguali, nome, riga, telefono e link, scheda tutta cliccabile; a 390 in riga con la foto a sinistra.
10. **Almeno tre tipi di prove**: NON PASSA. Un tipo: cinque numeri veri (1955 grande, 1996, 3ª generazione, 33 album, 1 anno di garanzia). Recensioni con nome e comune, fornitori e clienti con il nome non sono nelle fonti: non li invento, li chiedo (LEGGIMI). Il cartello "socio A.I.A.S." nella foto G8 è una prova possibile, da confermare prima di scriverla.
11. **Lavori con un nome**: NON PASSA del tutto. Tre lavori, tutti con foto da 755 px su 1440 (più di metà pagina): Villa Palladiana e Giardino a Venezia con il luogo, l'aiuola con il prima e il dopo; mancano anno, comune dell'aiuola e dati (metri, piante, tempi): non sono nelle fonti.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: Garden e sopralluogo su nebbia, storia e Vivai su bosco; l'apertura ha la foto a tutta altezza; spazi 120 px a 1440 e 64 px a 390; margini 64 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e a filo, raggio 3 px, 52 px a 1440 e 48 a 390 (anche in testata e il Menu), testo 16 px; ogni Chiama ha il numero.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta in quattro caselle e i metri quadri; Garden e Vivai con tabella degli orari, Indicazioni (percorso Google Maps) e Chiama; nessun iframe.
15. **Piede completo**: PASSA IN PARTE. Quattro colonne, ragione sociale, P.IVA, REA, sede, telefoni, email, WhatsApp, orari, le due sedi, social con il sottotitolo, testo da 16 px. "Privacy e cookie" non è ancora un link (manca l'indirizzo dell'informativa) e manca il credito dello studio (il nome dello studio non è deciso: nel modello della PEC è ancora "[Agenzia]"); certificazioni: nessuna nelle fonti.

### Uso: i compiti della scheda

- Cliente del Garden (390): stato, Chiama, Indicazioni e WhatsApp senza scorrere (entro 490 px); il numero resta in testata; la scheda Garden con "piante grasse, bonsai, vasi in terracotta" e la loro foto è a 898 px; i reparti con le foto, ora anche "Piante grasse e bonsai", al terzo scorrimento. Stato giusto a 11 orari provati (`pro_uso.mjs`, compreso "chiude tra 1 minuto" alle 12:29), festività con "Oggi è festa: chiamate prima di passare"; con JavaScript spento la riga dice gli orari della settimana. WhatsApp si apre con "Buongiorno, vorrei sapere se avete ".
- Chi vuole un giardino (1440): la porta "Volete un giardino?" nella prima schermata; tre lavori veri, uno con il prima e il dopo affiancati; 4 passi e garanzia accanto al modulo; modulo di 4 campi corti più caselle, foto via email o WhatsApp. Ancora da risolvere: chi risponde ed entro quando (va deciso dall'azienda, LEGGIMI) e il prima e dopo degli altri due lavori.
- Professionista (1440): la porta Vivai con il numero nella prima schermata; nella sezione Vivai zolla o vaso, spedizione in tutta Italia, anche grandi esemplari, 049 640156, WhatsApp, info@bordinvivai.it con oggetto, orari e indicazioni per via dei Vivai 14.

### Controlli generali

- Scorrimento orizzontale: 0 a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 px (anche con l'emulazione del telefono a 320 e 768, dove prima le schede in riga e il 1955 allargavano la pagina: corretti).
- Collegamenti: `tel:+390498791098`, `tel:+39049640156`; `mailto:info@bordingarden.it` (anche dal modulo, con oggetto), `mailto:info@bordinvivai.it`; mappe `google.com/maps/dir/?api=1&destination=` sulle coordinate del Garden (45.38608, 11.961015) e dei Vivai (45.3857, 11.9625); WhatsApp 350 1376907 e 350 5859658; nessuna ancora rotta, nessun `href="#"`.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI e negli script. Console senza errori.

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
