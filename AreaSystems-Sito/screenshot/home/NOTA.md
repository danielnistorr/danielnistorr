# Area Systems, home finale: "Il quadro aperto"

Pagina: `sito/index.html` (statica, si apre con file:///, CSS e script nel file, immagini in `sito/img/`, carattere in `sito/fonts/`). Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, controllo U+2014, prova del gesto e del menu, misure della rifinitura, screenshot, misura dei segnali).

Parte dalla bozza B, scelta dal committente. Ne restano l'idea, la prima schermata, il trattamento delle foto, il carattere e i colori. Questa è l'ultima rifinitura dopo il giudizio cieco (52 su 80): sono stati corretti i difetti di esecuzione e di dati; la prima schermata non è stata ripensata, per la scelta del committente.

## Idea

Area Systems vende il clima del quadro elettrico. La home apre il quadro e mostra, con sei etichette, dove va ogni loro pezzo: il torrino sul tetto, la lampada sotto il tetto, il condizionatore e il gruppo con filtro sulla porta, il termostato e la resistenza sulle guide DIN libere. Toccando un'etichetta cambia la legenda accanto al titolo: il pezzo scontornato, dove va, tre dati dalle schede del sito e il collegamento alla scheda vera.

## Cosa è cambiato in questa rifinitura

- **La legenda non copre più la foto.** Prima era un cartellino bianco con l'ombra, sopra la foto in basso a destra. Ora sta sulla carta, nella colonna destra dell'apertura, sotto la frase, con un filetto sopra. Ha un'altezza fissa (180 px a desktop, 244 a tablet, 222 al telefono, 260 sotto i 360 px), quindi non salta quando si cambia pezzo. La foto resta tutta libera, a tutta larghezza. La prova automatica controlla a ogni larghezza che legenda e foto non si tocchino.
- **Il titolo a 1280.** Il corpo ora è `clamp(92px, 8,9vw, 128px)`, quindi da 1181 a 1440 il titolo sta sempre su due righe. Sotto i 1400 px la testata è più bassa (84 px) e la frase scende a 16 px. A 1280 x 720 la foto parte a y = 404 (prima a 513); a 1440 x 900 parte a 421 e le sei etichette stanno tutte nella prima schermata.
- **Telefono.** Le etichette 1, 3 e 4 sono state spostate dentro la foto (1 a `--my:7`, 3 e 4 a `--mx:9`). Sopra la legenda c'è una riga breve, "Scegliete un numero sulla foto.", che compare sotto i 1180 px, dove la legenda sta sotto la foto.
- **Sezione dei pezzi a 1024.** Le famiglie restano nella colonna destra, accanto al gruppo con filtro, e non vanno più in fondo. Non c'è più la colonna vuota di circa 600 px. Il gruppo con filtro ora è largo otto colonne invece di sette.
- **La fascia dei fili è stata tolta.** Ripeteva l'armadio dell'apertura con una luce più calda, e la sorgente utile era di 1338 px, quindi era ingrandita a 1440 e a 1920. Al suo posto ci sono due elementi:
  - **la fascia "il quadro chiuso"**: due ante grigie con le feritoie per l'aria (Victor Ferreira, Unsplash `pLvgCVtwbls`). La sorgente è di 4928 px ed è esportata a 1440, 1920 e 2880, con lo stesso trattamento freddo e desaturato dell'apertura. Sull'anta destra c'era un cartello di pericolo in portoghese: è coperto da lamiera liscia, ricostruita con la luce dell'anta e la grana dell'anta sinistra (`finale_img.py`). Racconta il quadro da fuori, dopo il quadro aperto: è da lì che passa l'aria;
  - **"Gruppi ASB in cinque misure"**: i cinque gruppi della serie ASB disegnati in scala tra loro (114, 150, 204, 250 e 325 mm di lato), con la sigla, la misura e la portata di ogni taglia, prese dalla tabella della scheda ASB. Due righe di testo dicono come si montano (a scatto, senza viti, nelle dime standard), la griglia apribile per il filtro e i due grigi RAL. È una linea con la loro sigla e le misure diventano il disegno. Il disegno è in CSS, senza immagini e senza quote in monospazio.
- **Dato corretto.** La riga della ventilazione diceva "da 24 a 1500 m³/h", ma i ventilatori assiali arrivano oltre (GW280H 1870 mc/h, Jason Fan FJ28082MAB 2040 mc/h). Ora dice "gruppi e torrini da 24 a 1500 m³/h", che vale per ASB, GB/F, GA e GT.
- **Contatti chiari.** La fascia nera in fondo ora è lamiera chiara #E7E9E7 con il numero in inchiostro a 96 px (era bianco su nero a 132 px). La pagina è chiara dalla testata al piede.
- **Il torrino nella legenda**: "aspira l'aria calda e la porta fuori", più corto, per stare su una riga.
- **Altezza**: 5720 px a 1440 (era 4756), 6612 a 390.

## Prime due schermate

- **1440 x 900**: testata chiara con il marchio orizzontale, quattro voci di menu e il telefono. A sinistra il titolo "Il clima giusto dentro il quadro", a 128 px su due righe, peso 300, spaziatura -0,038em. A destra, in alto, tre righe su cosa vendono e da dove; sotto, dopo un filetto, la legenda del pezzo scelto (all'inizio il gruppo con filtro ASB). Sotto, il quadro aperto a tutta larghezza con le sei etichette, tutte visibili.
- **390 x 844**: il titolo a 46 px su due righe, la frase, poi il quadro in un taglio quasi quadrato con sei numeri tondi da 44 px di area di tocco. La riga "Scegliete un numero sulla foto." e la legenda cominciano sotto la foto.
- **Poi**: i due pezzi veri del loro catalogo, grandi su grigio lamiera, con le quattro famiglie; la fascia del quadro chiuso; i gruppi ASB in scala; per chi lavorano; "Nello stesso quadro"; i cataloghi PDF veri; il telefono e le sedi su lamiera chiara; il piede con i dati societari.

## Caratteri e colori

- **Overpass** (Delve Withrington per Red Hat; Google Fonts; SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`). Una sola famiglia, woff2 variabile servito dalla pagina (latin e latin-ext). Nasce dall'Highway Gothic della segnaletica stradale: è il carattere delle targhette e delle etichette dei componenti. Titoli in 300 con spaziatura negativa, testo in 400, nomi in 600. Cifre tabellari per misure, portate, sigle, telefono e partita IVA. Niente monospazio.
- Attenzione, campagna: Overpass è anche il carattere del sito finale di 3Esse e del WordPress di Gardens Pav. È stato tenuto perché il committente ha scelto questa bozza così com'è (vedi LEGGIMI, punto 12).
- Riferimenti d'impianto: maxon (una sola foto tecnica enorme, grottesco grande, menu corto) e, per le etichette sul pezzo, la home di Mario Agnoletto amata dal committente.
- Colori: carta #FAFAF8; lamiera chiara #E7E9E7 (il RAL 7035 dei loro gruppi, schiarito) per i pezzi e i contatti; i gruppi ASB disegnati in #DADDDA con filo #7E8587; filetti #C9CDCB e #D2D5D3; inchiostro #15171A; grigio #575C5F per le didascalie (contrasto 6,5:1 sulla carta, 5,5:1 sulla lamiera). Il rosso #A03A2B del logo compare solo sul punto e sul numero del pezzo scelto e al passaggio sui collegamenti. Nessun blocco scuro.

## Interazione

Le sei etichette sono un gruppo di schede (role tablist). Si usano con il clic o il tocco, e da tastiera con frecce, Inizio e Fine; il fuoco è visibile, con un contorno rosso. La legenda cambia di colpo, con le immagini precaricate. La transizione è di 120 ms solo sul colore dell'etichetta. Nessuna animazione allo scorrere, niente che segue il cursore, nessun passaggio che sbiadisce.

## Foto: origine e licenza

- **Apertura**: Raymond Sime, quadro aperto, Unsplash `NAchd3UmxXo` (Unsplash License, verificata il 19/10/2026). Esportata a 1440, 1920 e 2400 px; per il telefono un taglio quasi quadrato a 390, 780 e 1170. **Segnaposto**: non è un loro quadro e nessun pezzo inquadrato è loro; le etichette indicano dove vanno i loro prodotti.
- **Quadro chiuso**: Victor Ferreira, Unsplash `pLvgCVtwbls` (Unsplash License, verificata il 19/10/2026 sulla pagina della foto: "Free to use under the Unsplash License", non Unsplash+). Cartello tolto. **Segnaposto.**
- **Pezzi grandi**: il gruppo di ventilazione (pag. 13) e la resistenza alettata (pag. 53) del catalogo Area Systems 2022, scontornati, ripuliti dalla polvere e trattati.
- **Pezzi della legenda**: gli scontornati del sito (GT10023AB, plafoniera T5, ASVC200, gruppo ASB32, DTV02-N, CTSH), mostrati a 88-120 px.
- **Trattamento** (lo stesso della bozza B, con PIL): saturazione abbassata, ombre aperte, bianco neutro freddo, nitidezza leggera; WebP in più larghezze con srcset.
- Nessuna immagine generata dall'IA. Nessuna di queste foto è in un'altra home della campagna (controllato per ID nei `CREDITI.md` delle altre cartelle).

## Ispirazioni del committente (Pelletteria Graziella, Studio N19)

Usate pochissimo, e il giudice è d'accordo. Area Systems è un piccolo distributore di componenti per quadri: il registro è tecnico, non di lusso. Il serif contrastato, il corsivo, il nero e le foto di moda di Graziella sarebbero un travestimento, e il corsivo d'accento è anche tra i divieti. Da Studio N19 restano solo il bianco con molta aria e il titolo grande e sicuro. Il resto segue il catalogo tecnico fatto bene.

## Difetti del giudice non applicati, e perché

- **Apertura con un solo pezzo loro, scontornato, al posto del quadro** (bloccante) e **struttura diversa da Bertolin Antonio** (bloccante): non applicati. Il committente ha scelto la bozza B e ha chiesto di non ripensare la prima schermata. Le correzioni proposte (pezzo scontornato al centro, niente foto a tutta larghezza, legende a filo) cambiano idea e impaginazione. Un intervento va comunque nella direzione del giudice: la legenda ora sta sulla carta, accanto al titolo, e non più sulla foto, quindi sopra la foto c'è una riga con titolo, frase e legenda e non solo titolo e frase come da Bertolin. Le etichette bianche sulla foto restano: sono il gesto della bozza scelta. Il problema vero resta la foto: va fatto lo scatto di un loro quadro con i loro pezzi montati (LEGGIMI, "Foto da rifare dal vero"); allora ogni etichetta toccherà il pezzo che nomina.
- **Marchio ridisegnato in SVG** (minore): non applicato. Ridisegnare il logo di un'azienda è un lavoro da fare con loro, e un ricalco del JPEG avrebbe gli stessi difetti (serif marrone, ali sfumate). Il marchio in pagina è a 2x (1054 x 192 px per 224 px di larghezza), quindi non è sgranato. Il vettoriale va chiesto (LEGGIMI).

## Controlli

- Altezza: 1440: 5720 px; 390: 6612; 320: 6802; 768: 5839; 1024: 5706; 1280: 5615; 1920: 6171.
- Prima schermata (`_prova/script/misure_rifinitura.mjs`, a 16 larghezze da 320 a 2560): titolo su due righe ovunque; legenda di altezza costante con tutti e sei i pezzi e senza testo che trabocca; legenda e foto mai sovrapposte; scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 768, 900, 1024, 1180, 1181, 1280, 1366, 1440, 1600, 1920 e 2560.
- Gesto (`_prova/script/prova_gesto_finale.mjs`, a 320, 390, 768, 1024, 1440, 1920): tocco o clic, frecce, Inizio, Fine, fuoco sull'etichetta giusta, etichette dentro la foto, menu del telefono che si apre e si chiude dopo la scelta. Tutto a posto, senza errori in console.
- Collegamenti: `tel:+390497960705` (due volte), `mailto:info@areasystems.it`, mappa Google sulla via San Marco 10 di Tombelle, otto PDF dei cataloghi e sei schede su areasystems.it (risposta 200 il 19/10/2026), privacy e cookie iubenda 25167846.
- Screenshot guardati a pezzi a 320, 390, 768, 1024, 1280, 1440 e 1920. PNG temporanei cancellati.
- U+2014: zero nella pagina, negli script, in questa nota, nel LEGGIMI e nei crediti (il controllo è nello script di build).
- Segnali da IA (`segnali.sh` a 1440): 0 soglie bloccanti. Area foto 35,8 %; un solo carattere, Overpass, al 100 %; monospazio 0 %; 27 filetti; 4 fasce di fondo; nessuna freccia, nessun numero grande con etichetta, nessuna numerazione 01/02. Resta una riga da guardare: le misure degli H2 sono 2 (64 e 96 px). È una scelta: un solo elemento grande, il titolo, e il numero di telefono come chiusura.
- A occhio: nessun badge, nessuna fila di tre box con icona, nessun gradiente, nessun corsivo, nessuna emoji, nessuna nota di lavorazione a vista.
- Dati ricontrollati su `_prova/crawl/testi.txt`:
  - ASB: da 114 a 325 mm; per misura 24-36, 56-60, 120-211, 198-430 e 550-700 mc/h; a scatto senza viti, dime standard, griglia apribile per il filtro, RAL 7035 o 7032 su richiesta, IP54, da -10 a +70 °C, cuscinetti a sfera, 50.000 ore a 40 °C;
  - gruppi e torrini da 24 a 1500 mc/h (ASB, GB/F, GA, GT);
  - torrini: da 500 a 1500 mc/h, da 324 x 324 a 540 x 390 mm;
  - AS-T5: alluminio da 0,8 mm, staffe o magneti, maschio e femmina;
  - ASVC: da 350 a 4000 W, compressore rotativo, IP54, "porta o pannelli laterali dei quadri di qualsiasi marca";
  - DTV02/N NO e DTR02/N NC, da 0 a +60 °C, "unità di ventilazione o riscaldamento";
  - CTSH: da 25 a 150 W, PTC autoregolante, da -45 a +70 °C, guida DIN da 35 mm;
  - Mean Well da 10 a 960 W, Relpol fino a 12 A, spie da 22 mm, MAUS Stixx a 380 °C;
  - settori, sedi, P.IVA, REA, capitale, PEC.
