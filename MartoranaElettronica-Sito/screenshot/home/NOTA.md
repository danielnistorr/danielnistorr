# Martorana Elettronica, home finale "Corretto o scarto"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, controlli, screenshot con `shoot_finale.mjs`, segnali). Base: prototipo A, con le indicazioni del giudice e gli innesti da B.

## Idea

Ogni collaudo Martorana finisce su due pulsanti serigrafati: CORRETTO e SCARTO. Il titolo è quella scritta, grande e su una riga; sotto c'è il pannello vero del Mod. 1294/P, che finisce sotto la "o" finale del titolo, e due soli filetti partono dai due pulsanti e finiscono sulle parole "Corretto" in verde e "Scarto" in rosso. Le due parole del titolo sono le due scritte del pannello. Il resto della pagina tiene lo stesso alluminio chiaro, gli stessi scontornati con una sola ombra e i colori dell'esito (verde, grigio, rosso) solo dove c'è un esito.

## Prime due schermate

1. **Apertura** (ripensata, non ritoccata: il K0 del prototipo era 7). Via i sette pallini numerati e l'elenco delle legende, che ripetevano la tavola a richiami di Area Systems e Agnoletto. Ora: "Corretto o scarto" a 148 px; a sinistra solo due righe, il bottone "Chiama 049 9003655" e "Scrivete una email"; a destra il pannello, mostrato al massimo a 746 px (metà dei 1492 px del file: nitido anche sugli schermi 2x) e allineato alla fine del titolo; in basso una sola riga allineata: la didascalia "Mod. 1294/P, stazione da banco" e le due legende. L'ombra sfuma fino a zero dentro l'immagine (150 px di margine sotto, alfa 0 ai bordi verificato dallo script): il taglio netto a y=829 non c'è più. A 390: titolo su due righe, pannello a tutta larghezza tagliato a destra con 24 px sopra e 40 sotto, le due legende, poi testo e bottone, tutto nella prima schermata.
2. **Azienda**: il titolo è la loro frase sulla stazione Zanussi, "Concetti così lungimiranti che per molti versi sono ancora validi", con accanto la foto d'archivio degli anni '70 trattata come una stampa (150 px, file nativo da 202 px e versione a 2x). Sotto, una riga su chi sono e tre righe a filetti: 1973 e l'ing. Vincenzo Martorana; le normative CEI, VDE, EN, UL; i mercati. Il fondo dei fatti è allineato al fondo della stampa: niente più vuoto sotto il testo.

Poi: "Otto prove, un esito" (il gesto), "Quattro famiglie di prova" (innesto da B: cinque righe a filetti senza miniature, l'ultima è il su misura), alimentatori e software, la chiusura con foto e il piede. Altezza a 1440: 5052 px compreso il piede (390: 7432 px).

## Caratteri e colori

- **Hubot Sans** (titoli, larghezza 104-108 %, peso 520-560, spaziatura da -0,02 a -0,04em) e **Mona Sans** (testo, 400-600), la stessa famiglia in due tagli. Licenza SIL Open Font License 1.1, scaricati da Google Fonts e serviti da `sito/fonts/` (latin e latin-ext, woff2). Perché: le scritte serigrafate dei pannelli Martorana ("STAZIONE DI COLLAUDO", "mod.1294/P") e il logo sono grottesche larghe con le curve tese; Hubot ha quella larghezza. Le cifre dei titoli vengono da Mona Sans (unicode-range), perché lo zero di Hubot è barrato. Riferimenti: Zurich Instruments (un grottesco chiaro, un solo blu, lo strumento da banco come apertura) e Teenage Engineering (un apparecchio solo, nessuna scritta sopra). Niente monospazio, niente Inter.
- **Colori**: alluminio #EEF0EF, un solo fondo per tutta la pagina, inchiostro #16191C e #464C52, filetti #C9CECD, blu Martorana #1D5FB8 preso dagli armadi (bottone e piede), verde #1F7A45 e rosso #B3261E solo come esito, grigio #8A9190 per "non rilevato". Contrasti: verde su alluminio 4,9:1, rosso 5,6:1, #DCE6F6 sul blu del piede 4,9:1 (AA anche a 14 px), bianco sul blu 6,2:1.

## Interazione

"Otto prove, un esito": l'elenco delle prove del Mod. 1200 (terra, rigidità dielettrica, isolamento, dispersione, assorbimento, pressione e portata, microperdite, differenziale). Al tocco si accende il pallino verde della riga e accanto compaiono la stazione che la fa, cosa misura e quali modelli la fanno, con le misure vere dove ci sono (Mod. 1200G 70 mbar e 1200 l/h, M0704N 396 cc/h e 0,1 %FS, M1294A_EXP1 115 e 230 Vac). Il dettaglio parte allineato alla prima riga dell'elenco; le immagini hanno una scala comune (alte 280 px, larghe al massimo 520). Bottoni veri con aria-expanded, frecce su e giù da tastiera, una sola prova aperta, di partenza Dispersione (il 0586_AD con i display rossi); a una colonna il dettaglio si apre sotto la riga toccata e lo scorrimento si compensa, così la riga resta ferma sotto il dito. Nessuna animazione allo scorrere, nessun effetto sul cursore, hover solo con cambio di colore in 0,15 s.

## La chiusura e il piede

- **Chiusura** ("b con foto", testo a sinistra e foto a destra fino al bordo): "Al primo posto, le specifiche del cliente" (dal loro "ponendo sempre al primo posto le esigenze e le specifiche del cliente"), il telefono a 48 px con tel:, l'email con mailto:, l'indirizzo con il link a Google Maps e la riga "Per una stazione nuova, mandateci il prodotto da provare". Niente orari: non sono pubblici. La foto è il cestello di lavatrice di Vlad Deep, il prodotto dei loro clienti; non compare altrove nella pagina né in altre home della campagna.
- **Piede**: blu degli armadi, logo bianco (PNG originale ritagliato, 471x143, mostrato a 180 px: più di 2x), una riga su chi sono, quattro colonne (Azienda, Stazioni di collaudo, Software e assistenza, Contatti) con le pagine del sito nuovo, riga legale con ragione sociale, P.IVA, indirizzo, Privacy, Cookie. A 390 le colonne si impilano due a due nell'ordine. Niente "Seguici": l'azienda non ha profili social. **Niente newsletter**: fanno macchine su misura per pochi clienti industriali, non pubblicano notizie, fiere o cataloghi e non hanno clienti privati.

## Foto, origine e licenza

- **Dell'azienda** (martoranaelettronica.com, da far confermare): Mod. 1294/P dal collage 7 dello slider (PNG a 256 colori: retinatura tolta con mediana, bordo ammorbidito, ombra unica, mostrato sotto la misura del file); moduli 0586_TN, 0586_RN, 0586_AD; Mod. 1200 Climatizzata e Inverter; M1294A_EXP1, Mod. 1200G (senza ombra), M0704N, Mod. 0507 (scontornato della scheda, neri della fiancata alzati a 18, mostrato al massimo a 484 px, metà del file); stazione anni '70 (202x541, mostrata a 150 px); logo bianco 485x158.
- **Segnaposto Unsplash**: solo il cestello di Vlad Deep (https://unsplash.com/photos/ykivphUagM4, Unsplash License verificata il 24/10/2026, riga in `assets/CREDITI.md`). Tolti la striscia dei settori (cestello, piano cottura, saldatore con la maschera, scheda LED) e il pannello tedesco di Dittrich con la scritta di un altro costruttore. Nessuna immagine generata dall'IA.

## Rifinitura finale (giudice cieco: K0 7, non passa)

Cosa è cambiato, difetto per difetto:
1. **Foto d'apertura morbida** (bloccante): il Mod. 1294/P è mostrato al massimo a 746 px CSS dal file da 1492, quindi a 2x ogni pixel del file vale un pixel. Le scritte grandi del pannello (STAZIONE DI COLLAUDO, mod.1294/P, i display) ora sono nette; le scritte minute restano quelle di un PNG a 256 colori e si sistemano solo con lo still life (LEGGIMI, foto da rifare). Non ho ridisegnato a mano le serigrafie in vettoriale: sarebbe un falso del pannello.
2. **"Quattro famiglie"**: via le miniature e le didascalie, cinque righe (nome, modelli, una riga che non ripete il gesto), "Anche su misura" come quinta riga. Sezione di circa 650 px a 1440; home a 390 a 7432 px (era 8334).
3. **Mod. 0507**: al massimo 484 px, non più tagliato al bordo; neri della fiancata alzati da 0 a 18 in `finale_img.py`.
4. **Mod. 1200G**: tolta l'ombra staccata sotto il raccordo; scala comune per tutte le immagini del gesto.
5. **Salto a 390**: lo scorrimento si compensa al tocco. Provato con Playwright a 390 su sette coppie (aperta sopra e tocco sotto, e il contrario): spostamento del bottone 0 px in tutti i casi (`_prova/script/prova_gesto.mjs`).
6. **1024**: tra 901 e 1200 px "cosa misura" e "la fanno" sono impilati; il paragrafo sta in 2 o 3 righe da 482 px.
7. **Vuoto a 1440 in Azienda**: la stampa parte a 72 px dalla tabella, larga 150 px (202 px nativi, 404 per i 2x).
8. **Due grigi di fondo**: un solo fondo #EEF0EF, sezioni separate dall'aria.
9. **"Costruite a Mestrino dal 1973"**: ora "Dal 1973, oggi a Mestrino" nell'apertura, nel piede e nella descrizione; la domanda è nel LEGGIMI.
10. **"La fanno" del Mod. 1294/P**: tolto da tutte le prove finché l'azienda non conferma.
11. **Prova aperta di partenza**: Dispersione, con il 0586_AD (display rossi e pulsanti verde e rosso), non più il 0586_TN con PASS e FAIL.
12. **Telefono ripetuto nel piede**: la colonna Contatti ha solo telefono ed email in corpo normale; l'indirizzo è nella riga legale.

In più: la foto della chiusura arriva al bordo destro anche oltre i 1440 px; "serie /NET" non va più a capo; il margine sotto l'apertura è uguale a quello tra le sezioni (104 px).

## Controlli

- Screenshot guardati a pezzi a 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 1024 e 1920: nessuna sovrapposizione, nessun vuoto non voluto.
- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 900, 901, 1024, 1200, 1280, 1440, 1441, 1680, 1920 e 2560 (`_prova/script/larghezze.mjs`); la foto di chiusura tocca il bordo destro a ogni larghezza.
- Gesto: tocco a 390 senza salti (0 px), frecce su e giù con il giro dall'ultima alla prima, Invio sui bottoni, focus visibile; menu a 390 con un vero bottone e aria-expanded.
- Collegamenti: tel:+390499003655 (testata, apertura, chiusura, piede), mailto:martorana@martoranaelettronica.com, indirizzo con il link di ricerca di Google Maps.
- Nessun U+2014 nella pagina, nella NOTA, nel LEGGIMI e negli script.
- `segnali.sh` a 1440: 17 soglie su 18 a posto. Resta fuori l'**area foto, 16,6 %** contro il 35 %: è scesa perché, come chiesto dal giudice, le due immagini grandi dell'azienda ora sono mostrate alla metà della misura del file per essere nitide. Non è un segnale da IA ma un limite del materiale: non ho aggiunto foto di repertorio per arrivare alla soglia; sale con il servizio fotografico (apertura a tutta altezza, una stazione installata per famiglia, chiusura).
- Dati: ogni fatto viene da `01-analisi.md`. In pagina non ci sono il 38 %, i nomi dei clienti, gli orari, PEC, REA e capitale sociale.
