# Area Systems, home finale: "Il quadro aperto"

Pagina: `sito/index.html` (statica, si apre con file:///, CSS e script nel file, immagini in `sito/img/`, carattere in `sito/fonts/`). Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini, controllo U+2014, prova del gesto e del menu, screenshot, misura dei segnali).

Parte dalla bozza B, scelta dal committente. Ne restano l'idea, la prima schermata, il trattamento delle foto, il carattere e i colori. La versione che c'era prima in `sito/` era costruita sulla bozza A: è stata tolta del tutto.

## Idea

Area Systems vende il clima del quadro elettrico. La home apre il quadro e mostra, con sei etichette, dove va ogni loro pezzo: il torrino sul tetto, la lampada sotto il tetto, il condizionatore e il gruppo con filtro sulla porta, il termostato e la resistenza sui due tratti di guida DIN rimasti liberi. Toccando un'etichetta si apre il cartellino del pezzo, con tre dati presi dalle schede del sito e il collegamento alla scheda vera.

## Cosa è cambiato rispetto alla bozza B

- **Le etichette puntano solo a posti vuoti.** Nella bozza "3 Alimentatori" stava sugli alimentatori di un concorrente di Mean Well, "5 Condizionatore" su una canalina e la lampada su una lampada che non è loro. Ora ogni punto sta dove il pezzo si monta: il tetto, la porta, le due guide DIN libere della parete sinistra. Il cartellino dice "Va sulla porta, in basso", "Va sulla guida DIN", e non "questo è". Gli alimentatori escono dal gesto e restano, con il marchio Mean Well, in "Nello stesso quadro". Al loro posto entra la resistenza CTSH (da 25 a 150 W, PTC, guida DIN da 35 mm), che è un pezzo loro.
- **Il cartellino non copre più un terzo della foto.** Prima era largo 388 px e si spostava accanto all'etichetta. Ora è largo 328 px ed è fermo in basso a destra, sopra la fila dei moduli. Lì non ci sono etichette, quindi non ne copre nessuna; la prova automatica lo controlla a ogni larghezza. Sotto i 1180 px sta sotto la foto, come prima.
- **Dati.** La didascalia del gruppo con griglia cromata (pag. 13 del catalogo, serie non identificata) non riporta più le caratteristiche della scheda ASB: ora dice solo quello che si vede. Il cartellino del gruppo mostra lo scontornato della pagina ASB, quindi i dati ASB lì sono giusti. Lo sticker MAUS Stixx "spegne l'incendio" come dice la scheda. Tutti i dati in pagina sono ricontrollati su `_prova/crawl/testi.txt` (elenco in fondo).
- **Dalla A**: "tra Padova e Venezia" nella frase d'apertura, il capitale sociale e i collegamenti a privacy e cookie (iubenda, gli stessi del sito di oggi) nel piede.
- **Esecuzione.** Il marchio è a 2x (1054 x 192 px dal JPEG più grande del sito), con il fondo trasparente, alto 41 px. Sui due pezzi del catalogo è stata tolta la polvere. La fascia dei fili è alla risoluzione nativa (1338 px) e non più ingrandita a 1440. Il taglio per il telefono non mostra più i controllori di marca. Il contatto scuro è più basso (510 px invece di 590). Il menu del telefono si apre a tutta larghezza e si chiude dopo la scelta o con Esc. Non ci sono più a capo orfani nella frase d'apertura né "AS-" spezzato.
- **Altezza**: 4756 px a 1440 (era 4943), 5556 px a 390 (era 6095).

## Prime due schermate

- **1440 x 900**: testata chiara con il marchio orizzontale, quattro voci di menu e il telefono. Il titolo "Il clima giusto dentro il quadro" è a 128 px su due righe, peso 300, spaziatura -0,038em. A destra, allineate alla base del titolo, tre righe su cosa vendono e da dove. Sotto, il quadro aperto a tutta larghezza fino al bordo della finestra, con le sei etichette sulla porta, sul tetto e sulle guide libere. In basso a destra il cartellino del gruppo con filtro ASB, già aperto, così il gesto si capisce senza istruzioni.
- **390 x 844**: il titolo a 46 px su due righe, la frase, poi il quadro in un taglio quasi quadrato (porta, parete, guide, moduli) con sei numeri tondi da 44 px di area di tocco. Il cartellino comincia sotto la foto, dentro la prima schermata.
- **Seconda schermata**: due pezzi veri del loro catalogo, grandi su grigio lamiera (la resistenza alettata e il gruppo con griglia cromata), con le quattro famiglie e i loro campi. Poi la fascia dei fili, per chi lavorano con tre settori, "Nello stesso quadro", i cataloghi PDF veri, il telefono grande e le sedi, il piede con i dati societari.

## Caratteri e colori

- **Overpass** (Delve Withrington per Red Hat; Google Fonts; SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`). È una sola famiglia, woff2 variabile servito dalla pagina (latin e latin-ext). Nasce dall'Highway Gothic della segnaletica stradale: è la famiglia delle targhette e delle etichette dei componenti, quella che un quadrista legge ogni giorno. Titoli in 300 con spaziatura negativa, testo in 400, nomi in 600. Cifre tabellari per misure, portate, telefono e partita IVA. Niente monospazio.
- Attenzione, campagna: Overpass è anche il carattere del sito finale di 3Esse (`3Esse-Sito/sito/index.html`) e del WordPress di Gardens Pav (`GardensPav-Sito/_sorgente/contenuti.py`). La nota della bozza B diceva il contrario e sbagliava. È stato tenuto perché il committente ha scelto questa bozza così com'è. Se in campagna serve un carattere diverso per ogni azienda, va cambiato in uno solo dei tre siti.
- Riferimenti d'impianto: maxon (una sola foto tecnica enorme, grottesco grande, menu corto) e, per le etichette sul pezzo, la home di Mario Agnoletto amata dal committente.
- Colori: carta #FAFAF8; lamiera chiara #E7E9E7 (il RAL 7035 dei loro gruppi, schiarito) per la sezione dei pezzi; filetti #C9CDCB e #D2D5D3; inchiostro #15171A; grigio #575C5F per le didascalie (contrasto 6,5:1 sulla carta, 5,5:1 sulla lamiera). Il rosso #A03A2B del logo compare solo sul punto e sul numero del pezzo scelto e al passaggio sui collegamenti. Il colore pieno arriva solo dai fili nella foto. L'unico blocco scuro è il contatto, in fondo, con testo bianco.

## Interazione

Le sei etichette sono un gruppo di schede (role tablist). Si usano con il clic o il tocco, e da tastiera con frecce, Inizio e Fine; il fuoco è visibile, con un contorno rosso. Il cartellino cambia di colpo, con le immagini precaricate: il pezzo scontornato, dove va, tre dati e il collegamento alla scheda su areasystems.it. La transizione è di 120 ms solo sul colore dell'etichetta. Nessuna animazione allo scorrere, niente che segue il cursore, nessun passaggio che sbiadisce. Prova automatica: `_prova/script/prova_gesto_finale.mjs` a 320, 390, 768, 1024, 1440 e 1920 controlla clic e tocco, tastiera, etichette dentro la foto e non coperte, menu del telefono, scorrimento orizzontale. Tutto a posto, senza errori in console.

## Foto: origine e licenza

- **Apertura**: Raymond Sime, quadro aperto, Unsplash `NAchd3UmxXo` (Unsplash License, verificata il 19/10/2026, in `assets/CREDITI.md`). Esportata a 1440, 1920 e 2400 px; per il telefono un taglio quasi quadrato a 390, 780 e 1170. **Segnaposto**: non è un loro quadro e nessun pezzo inquadrato è loro. Le etichette indicano solo dove vanno i loro prodotti.
- **Fascia dei fili**: Raymond Sime, Unsplash `KDkU44ikiko`. Il taglio comincia a destra degli alimentatori, il cui marchio (concorrente di Mean Well) resta fuori. A 1920 è ingrandita di 1,4 volte: la sorgente non ha più pixel senza quel marchio.
- **Pezzi grandi**: il gruppo di ventilazione (pag. 13) e la resistenza alettata (pag. 53), dal catalogo Area Systems 2022. Sono scontornati, ripuliti dalla polvere e trattati.
- **Pezzi del cartellino**: gli scontornati del sito, cioè GT10023AB, plafoniera T5, ASVC200, gruppo ASB32, DTV02-N e CTSH. Sono piccoli, da 200 a 460 px, e mostrati a 96-120 px.
- **Trattamento** (lo stesso della bozza B, con PIL): saturazione abbassata, ombre aperte, bianco neutro freddo, nitidezza leggera; WebP in più larghezze con srcset.
- Nessuna immagine generata dall'IA. Nessuna di queste foto è in un'altra home della campagna (controllato per ID nei `CREDITI.md` delle altre cartelle).

## Ispirazioni del committente (Pelletteria Graziella, Studio N19)

Usate pochissimo, come nelle bozze, e il giudice è d'accordo. Area Systems è un piccolo distributore di componenti per quadri: il registro è tecnico, non di lusso. Il serif contrastato, il corsivo, il nero e le foto di moda di Graziella sarebbero un travestimento, e il corsivo d'accento è anche tra i divieti. Da Studio N19 restano solo il bianco con molta aria e il titolo grande e sicuro. Il resto segue il catalogo tecnico fatto bene.

## Controlli

- Altezza: 1440: 4756 px; 390: 5556 px; 320: 5739; 768: 5286; 1024: 5166; 1920: 5175. Nessuno scorrimento orizzontale e nessuna sovrapposizione a nessuna larghezza; screenshot guardati a pezzi a 320, 390, 768, 1024, 1440 e 1920.
- U+2014: zero nella pagina, negli script, in questa nota e nel LEGGIMI (il controllo è nello script di build).
- Segnali da IA (`segnali.sh` a 1440): 0 soglie bloccanti. Area foto 40,6 %; un solo carattere, Overpass, al 100 %; monospazio 0 %; 17 filetti; 4 fasce di fondo; nessuna freccia, nessun numero grande con etichetta, nessuna numerazione 01/02. Resta una riga da guardare: le misure degli H2 sono 2 (64 e 132 px). È una scelta: un solo elemento grande, il titolo, e il numero di telefono come chiusura.
- A occhio: nessun badge, nessuna fila di tre box con icona, nessun gradiente, nessun corsivo, nessuna emoji. Nessuna nota di lavorazione a vista.
- Dati ricontrollati su `_prova/crawl/testi.txt`:
  - ASB: da 114 a 325 mm, da 24 a 700 mc/h, 50.000 ore a 40 °C, IP54;
  - torrini: da 500 a 1500 mc/h, da 324 x 324 a 540 x 390 mm;
  - AS-T5: alluminio da 0,8 mm, staffe o magneti, maschio e femmina;
  - ASVC: da 350 a 4000 W, compressore rotativo, IP54, "porta o pannelli laterali dei quadri di qualsiasi marca";
  - DTV02/N NO e DTR02/N NC, da 0 a +60 °C, "unità di ventilazione o riscaldamento";
  - CTSH: da 25 a 150 W, PTC autoregolante, da -45 a +70 °C, guida DIN da 35 mm;
  - Mean Well da 10 a 960 W, Relpol fino a 12 A, spie da 22 mm, MAUS Stixx a 380 °C;
  - settori, sedi, P.IVA, REA, capitale, PEC.
  - I PDF dei cataloghi e le sei schede collegate rispondono 200 (controllo del 19/10/2026).
