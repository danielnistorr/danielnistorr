# Home finale di Mario Agnoletto, "Dritto e rovescio": nota

Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (WebP in più larghezze e tre SVG), caratteri in `sito/fonts/`. La pagina non chiede nulla ad altri domini. Tutto si rifà con `bash _prova/script/build_finale.sh`, che rigenera immagini, logo, pagina, controlli e screenshot.

Screenshot (JPEG 85): `home-1440.jpg` (intera), `home-1440-prima-schermata.jpg` (1440x900), `home-390.jpg` (intera, telefono), `home-390-prima-schermata.jpg` (390x844). Ci sono anche `home-1440-dritto.jpg` e `home-390-dritto.jpg`, la prima schermata dopo aver premuto Dritto.

## L'idea

Un punzone porta il segno a rovescio e lo lascia dritto sulla pelle: ogni lavoro di Agnoletto esiste due volte.
La home si apre con il nome inciso a specchio in ottone sopra una striscia di pelle nera, come la testa di un punzone posata sul pezzo da stampare.
Un solo interruttore, Rovescio e Dritto, lo stampa nella pelle e scambia, più sotto, la foto grande e la piccola di ogni coppia.

È il prototipo A scelto dal committente. Idea, prima schermata, trattamento delle foto, caratteri e colori sono rimasti quelli. Ho corretto esecuzione, dati, telefono e nitidezza, e da B ho preso tre cose: il telefono in apertura, le miniature delle loro foto nell'indice, il logo in SVG.

## Le prime due schermate

1. **Apertura.**
   - Fondo nero conceria pieno; la pelle nera, con la luce radente da sinistra, c'è solo nella striscia a filo dei due bordi dove il nome si stampa (a 390 e a 768 in verticale è una colonna a sinistra, alta quanto l'apertura).
   - "Agnoletto" in Bodoni Moda 500, specchiato, in ottone pieno, con l'asse ottico fermo a opsz 40: grazie e filetti escono più spessi e non si perdono nella grana (che ora è anche più morbida, sfocatura 1,3 px). Il rilievo ora ha due soli livelli di spessore (1 e 2 px) e un'ombra corta (10 px di sfocatura, opacità 0,5): sembra metallo appoggiato, non una scritta 3D.
   - In alto a sinistra, a 12 px, lontano dal nome: "Incisore meccanico a Tombelle di Vigonovo" (l'anno è sceso nel testo, perché è da confermare). A destra una riga spiega il gesto.
   - In basso, la legenda su un filetto: attrezzi per la pelle, pezzi sul prodotto, un pezzo vero e l'interruttore "Stampa". Il pezzo vero è un ritaglio 4:3 della foto 1 (punzoni in ottone con la scritta a specchio, "Sul banco: punzoni in ottone, a rovescio"); con Dritto diventa la striscia di cuoio stampata a caldo della foto 6 ("Sul cuoio: la scritta impressa a caldo"). Sotto l'interruttore c'è "Chiamate il 049 98 00 985", in ottone chiaro, collegato al telefono.
   - Con Dritto il nome si gira in 240 ms e diventa un'impronta: lamina opaca, spigolo scuro sopra, labbro chiaro sotto. Questa parte non l'ho toccata.
   - Testata: logo SVG a sinistra; menu e telefono a destra, con il telefono allineato al margine. La copia dell'interruttore in testata è tolta dal flusso finché si vede quella dell'apertura; quando compare entra **a sinistra** del telefono (`order`), così telefono e Menu non si spostano.
   - **A 390** il nome corre in verticale sulla colonna di pelle. Nella colonna accanto: l'etichetta e la riga del gesto in alto, il pezzo vero al centro, sotto le due famiglie a 13 px e l'interruttore largo 52 px. "Metalli" è nel testo di "Lavorazioni". Testata: logo, telefono (14 px, alto 44 px) e "Menu". Scorrendo, il logo diventa il solo monogramma e l'interruttore (alto 44 px) entra a sinistra del telefono: il telefono resta a x 227 prima e dopo (misurato). Sotto i 380 px, in quella fase, il telefono lascia il posto all'interruttore (resta in apertura e nei contatti). Con altezze sotto i 700 px (320x640) il pezzo vero si nasconde, perché l'interruttore resti nella prima schermata.
   - **A 768** in verticale la composizione è quella del telefono: il pezzo vero (440 px) riempie la colonna destra, che prima aveva 600 px di pelle vuota; i vuoti ora stanno sotto i 150 px.
2. **"Ogni pezzo esiste due volte".**
   - Tre coppie: "Punzone e impronta", "Tacco e scarpa", "Prototipo e serie". La terza sostituisce le tre colonne numerate di prima ed è comandata dallo stesso interruttore.
   - In ogni coppia la foto grande va a filo del bordo. La colonna stretta ha in alto il titolo, un'etichetta e una frase, e in basso la foto piccola. La foto piccola è allineata in basso con la grande e le due didascalie stanno sulla stessa riga: i vuoti di 230 e 300 px non ci sono più.
   - A 390 la foto piccola sta a destra e la sua didascalia occupa la colonna di sinistra.

Seguono il campo avorio "Lavorazioni": il titolo "Lavorazioni" segue l'interruttore (a specchio in Rovescio, dritto in Dritto, 240 ms), la fascia delle fibbie larga 1280 px e l'indice delle otto lavorazioni con le miniature; "Targhe", l'unica senza foto, ha il titolo allineato agli altri. Poi i contatti sulla stessa pelle dell'apertura, con il timbro MA rosso una sola volta, l'invito "Per un preventivo mandate il disegno o il logo a info@marioagnoletto.it" (mailto con l'oggetto già scritto) e il piede con i dati societari.

## Caratteri e colori

- **Bodoni Moda** (opsz attivo, 400 e 500, mai corsivo) per il nome, i titoli e il telefono grande.
  - È una scelta di mestiere: Bodoni incideva da sé i punzoni dei suoi caratteri, e il bodoniano è la lettera classica degli alfabeti per la stampa su pelle. Specchiato si riconosce subito come rovescio.
  - Riferimenti: il nome scritto anche a specchio di Ghidini 1961 e il serif ad alto contrasto su nero di Officine Gullo.
- **Mona Sans** per testo, didascalie ed etichette. Le etichette sono maiuscole a larghezza 118, piccole e spaziate .11em. È un grottesco industriale usato piccolo, come il Gramatika di De Castelli e il DIN di Giobagnara.
  - Ho tolto le cifre tabellari da telefono, fax e P. IVA: in Mona Sans lo zero tabellare è barrato e fa sembrare il numero codice di programma. In pagina nessun numero sta in colonna, quindi bastano le cifre allineate (`lining-nums`). Il telefono grande dei contatti è in Bodoni con le cifre tabellari.
- Licenze: tutte e due le famiglie sono SIL Open Font License 1.1 (Google Fonts). Sono servite da `sito/fonts/` come file variabili con il sottoinsieme latino.
- **Colori.**
  - Nero conceria #151311 e avorio pelle #EFE8DC sono i due campi.
  - L'ottone #B08D57 / #D9BC86 è riservato a nome, interruttore e telefono.
  - Il rosso del logo #C8161D compare solo nel monogramma e nel timbro dei contatti.
  - Riferimenti: il nero e la grana vengono dal macro di pelle di Mastrotto, il metallo che brilla da solo dagli still life di De Castelli.

## Interazione

- Interruttore `role="switch"` con le voci Rovescio e Dritto. Funziona con clic, dito, Invio e Spazio. Il contorno di fuoco è visibile e l'etichetta per i lettori di schermo cambia con lo stato. Ci sono due copie sincronizzate: apertura e testata.
- Il menu del telefono si apre e si chiude con il bottone "Menu"/"Chiudi" e si chiude anche con Esc o scegliendo una voce.
- Transizioni da 150 a 240 ms, solo su ciò che si tocca. Nessuna animazione parte allo scorrere e nessun effetto segue il cursore. Nessun hover abbassa l'opacità. Con `prefers-reduced-motion` non c'è nessuna transizione.

## Foto (origine e licenza; elenco completo in `assets/CREDITI.md`)

| In pagina | Origine | Licenza |
|---|---|---|
| pelle nera (apertura, contatti) | Unsplash Y5RNGe_xkAQ, Ayush Design | Unsplash License, segnaposto |
| banco con cliché, ruota e stampo (coppia 1, rovescio) | foto 1 del sito di Mario Agnoletto | da confermare |
| cuoio stampato a caldo (coppia 1, dritto) | foto 6 del sito di Mario Agnoletto | da confermare; la scritta può essere di un cliente |
| pezzo vero dell'apertura | foto 1 (Rovescio) e foto 6 (Dritto) | da confermare |
| tacchi gioiello (coppia 2, rovescio) | foto 12 del sito di Mario Agnoletto | da confermare |
| scarpa (coppia 2, dritto) | Unsplash 4kqacvbRq34, McFollis | Unsplash License, segnaposto |
| fresa e minuterie (coppia 3) | Unsplash pl95tzT0f7Y (mastars MT) e ALvgGEl8mEE (Ivan Di) | Unsplash License, segnaposto |
| fibbie in ottone (fascia "Finiture") | foto 13 del sito di Mario Agnoletto | da confermare |
| miniature dell'indice | foto 1, 12, 13, 15 e 17 del sito di Mario Agnoletto | da confermare |

- **Vincolo Hambro.** Ho tolto la foto delle fibbie di Ruan Richard Rodrigues (hqGQcZnEvy0). In pagina non c'è nessuna foto di quella serie. Al suo posto c'è la foto 13 dell'azienda, in taglio panoramico (1250x536) sopra la fibbia cromata con la scritta "SHY", che resta fuori quadro.
- **Impronta.** Ora viene dalla foto 6: la striscia di cuoio con una scritta impressa a caldo, girata di 180 gradi perché si legga. Ritaglio 640x640; nello stato Dritto il riquadro si ferma a 768 px (1,2 volte). La foto 15 (pelle con brillantini) non è più in una coppia.
- **Trattamento unico**, con `_prova/script/finale_img.py`: meno saturazione, tono caldo, neri portati verso #151311, luce che cala da sinistra a destra, maschera di contrasto fine. Fresa e minuterie sono state scurite e scaldate come le altre.
- **Didascalie.** Nessuna presenta un segnaposto come pezzo loro: la scarpa dice "Il tacco, una volta montato, resta a vista"; fresa e minuterie dicono "Il prototipo nasce sotto la fresa" e "Poi la produzione in serie" (nessun "lo stesso pezzo"). La foto 12 dice "Tre tacchi gioiello: stelo, gabbia e lamelle" (forme, nessun materiale attribuito). Nel piede una riga dice quali foto sono di repertorio.
- Nessuna immagine generata dall'IA.

## Giro di rifinitura del 19 ottobre 2026 (giudizio cieco 58,5/80)

Applicati:
- Coppia "Punzone e impronta": via il punzone Unsplash e la pelle con i brillantini; ora tutte e due le foto sono dell'azienda (foto 1: cliché, ruota, stampo; foto 6: scritta impressa a caldo su cuoio), con didascalie che dicono solo ciò che si vede.
- Didascalie di scarpa, fresa e minuterie riscritte: nessuna attribuisce all'azienda ciò che la foto non mostra.
- Prima schermata: un pezzo vero (punzoni in ottone) accanto all'interruttore, che con Dritto diventa la scritta stampata sul cuoio.
- Prima schermata: fondo nero pieno e pelle solo nella striscia del nome; così non condivide più il fondo a tutta pagina con la home di Paraga Pelli.
- 768 in verticale: il vuoto di 600 px è riempito dal pezzo vero.
- "Lavorazioni" segue l'interruttore (titolo a specchio e dritto).
- "Targhe" allineata agli altri titoli.
- "Dal 1979" tolto dalla prima schermata, resta nel testo, da confermare.
- Testata a 390: telefono fermo, interruttore alto 44 px.
- Tolto il `preload` del Bodoni (errore CORS in file://): console senza errori.
- Bodoni con opsz 40 e grana più morbida sotto il nome.
- Invito al preventivo con mailto e oggetto.
- Righe piatte riscritte ("Ruote in acciaio e rulli, fatti su disegno"; tacchi gioiello non più ripetuto due volte).

Non applicati: la coppia con "lo stesso segno" in metallo e sulla pelle (non esiste una foto vera: non l'ho simulata; è lo scatto 1 del LEGGIMI); la riduzione delle coppie da tre a due (la terza regge l'idea grezzo e finito finché arrivano le foto vere).

## Controlli

- `_prova/script/finale_controlla.mjs`: a 320, 390, 768, 1024, 1440 e 1920, in Rovescio e in Dritto, nessuno scorrimento orizzontale, nessun testo o immagine che si sovrappone, testata scorsa dentro la larghezza (gli elementi ora si confrontano in ordine visivo).
- `_prova/script/finale_verifica.mjs`: scrollWidth uguale a innerWidth da 320 a 2560 px (passo 20 fino a 1100, poi 80), nei due stati; a 390 tocco sull'interruttore dell'apertura e su quello della testata (stato, `aria-checked` e titolo "Lavorazioni" cambiano), telefono della testata fermo (x 227, largo 96, prima e dopo lo scorrimento); a 1440 tastiera (Tab fino all'interruttore, Spazio e Invio, contorno di fuoco visibile); collegamenti `tel:+390499800985`, `mailto:info@marioagnoletto.it` (anche con oggetto), Google Maps sull'indirizzo; console senza errori in file://.
- Screenshot guardati a pezzi: 1440 intera e prima schermata nei due stati, 390 intera, testata scorsa a 390, prime schermate a 320, 768, 1024 e 1920.
- `segnali.sh`: 0 soglie bloccanti su 10. Foto al 51,1 % della pagina, Mona Sans al 92,2 % e Bodoni Moda al 7,8 %, monospazio 0 %, 14 filetti, nessuna freccia, nessun numero grande.
- Una sola riga DA GUARDARE: gli H2 hanno due misure, 89 e 135 px. È voluto: c'è un solo elemento grande per sezione e il nome dell'apertura sta sopra a tutti.
- Divieti: nessun gradiente, nessun corsivo, nessun badge, nessun "tre box con icona" (le tre colonne numerate sono diventate la terza coppia), nessuna icona, nessuna dissolvenza.
- U+2014: zero nella pagina, nella NOTA e nel LEGGIMI.

## Cosa manca per portare la prima schermata a 8

La prima schermata resta quella del prototipo scelto, come chiesto. Ora ha un pezzo vero, ma piccolo e da telefono: il nome resta soprattutto un effetto tipografico.
Per la versione definitiva servono le foto vere:
- la macro di un loro punzone in ottone con le lettere a specchio, a luce radente su pelle nera;
- la stessa scritta impressa nella pelle.

Con quelle foto le coppie diventano la prova dell'idea dell'apertura e la pagina smette di dipendere dai segnaposto. Le indicazioni di scatto sono nel LEGGIMI.
