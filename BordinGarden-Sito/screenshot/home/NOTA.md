# Home finale di Bordin Garden & Vivai: nota

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
