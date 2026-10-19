# Hambro, proposta di nuova home (preparazione)

- 01-analisi.md: azienda, sito di oggi, dati con fonti, materiale visivo con voti, soggetto e due direzioni artistiche, riferimenti, cose da confermare.
- assets/originali/: 139 immagini scaricate da hambro.it (inventario, misure e voti in _prova/inventario-immagini.json). Diritti da chiarire prima di riusarle.
- assets/esterne/: 10 foto Unsplash usate SOLO come segnaposto per mostrare la direzione artistica. Non sono foto di Hambro e vanno sostituite con foto vere dell'azienda prima di qualsiasi uso pubblico. Autori e licenze in assets/CREDITI.md.
- _prova/ (fuori da git): crawl del sito, screenshot del sito attuale (attuale/), screenshot dei riferimenti (riferimenti/, scartati in riferimenti/scartati/), script.

## Prototipo A della home, "Sotto la pelle" (_prova/home/a/)

- `proto.html`, immagini in `img/`, nota con idea, caratteri, foto e controlli in `nota.md`. Script delle immagini: `_prova/script/proto_a_img.py`.
- Foto segnaposto in pagina: Rodrigues (fibbia oro, fibbia nichel, coppia oro e nichel), Karimov (cuoio), Berg (mani sul cartamodello), tutte Unsplash License. Foto di Hambro in pagina: occhielli e rivetti dello slider, fibbie lucide e brunite, bobina di laccio a taglio vivo (diritti da chiarire).
- Foto da rifare dal vero: la stessa fibbia di Hambro in ogni finitura, su vetro nero, cavalletto fisso e una luce radente, per il selettore Oro e Nichel; la coppia nuda e ricoperta della fibbia da ricoprire; occhielli e rivetti in macro ad alta risoluzione; la bobina di laccio su fondo nero; le mani in laboratorio a Vigonovo.
- Da confermare: orari; finiture disponibili oltre oro e nichel; "sp.0.7/1.1" delle nappe e dei vitelli lavabili (due spessori o un intervallo); che cosa misurano i mm 40, 50, 60 delle fibbie da ricoprire; codici dei rivetti 00, 033, 034, 036; minuteria nichel free; Satab; "Nostre creazioni", "Occasioni macchine" e "Nuovi arrivi" (esclusi dall'indice); logo vettoriale.
- Caratteri: Gilda Display ed Encode Sans (Google Fonts, SIL OFL 1.1), da servire da `sito/fonts` nella versione finale.

## Home finale (sito/)

- `sito/index.html`, immagini in `sito/img/` (solo quelle usate, JPEG in più larghezze), caratteri in `sito/fonts/` (Mona Sans, SIL OFL 1.1, testo della licenza in `sito/fonts/OFL.txt`). Nota con idea, schermate, caratteri, colori, interazione, foto e controlli: `screenshot/home/NOTA.md`.
- Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini con `finale_img.py`, pagina da `finale_pagina.html`, screenshot in `screenshot/home/`. I PNG di controllo vanno in `_prova/screenshot-tmp/` e si cancellano a mano. Il banco si prova con `node _prova/script/prova_pagina.mjs`.
- Base: il prototipo B "Campionario al millimetro" (`_prova/home/b/`). Da A vengono il dittico metallo e pelle con le sagome in scala e il telefono come targa nei contatti.

### Dati da confermare con Hambro (in pagina non ci sono segnaposto)
- **1979.** In pagina è sempre "Giorgio Gastaldello, nella pelletteria dal 1979", mai l'anno della srl. Va chiesto l'anno di costituzione della società.
- **Fibbie da ricoprire mm40, 50 e 60.** Le sagome della Tav. 3 sono larghe quanto la misura. Va chiesto se la misura è la luce del passante (la larghezza della cintura) o l'esterno della fibbia, e la proporzione vera di ogni sagoma.
- **Strisce a taglio vivo.** Il cursore si aggancia alle misure a catalogo (2, 3, 3,5, 4, 16, 20, 25, 30, 40, 50, 60). Se tagliano a qualsiasi millimetro tra 2 e 60, basta togliere l'aggancio. Per il tubolare: oltre a 2, 3, 4 e 16, quali misure ci sono?
- **Nastri.** I sei colori del banco (rosso, giallo, salvia, viola, grigio, nero) vengono dalla loro foto dei rotoli: vanno chiesti i colori disponibili oggi. Satab: la rappresentanza è ancora valida?
- **Altri dati in pagina.**
  - Rivetti 00, 033, 034, 036 e occhielli piatti e bombati;
  - nappe e vitelli lavabili "sp. 0,7 e 1,1": due spessori o un intervallo?
  - minuteria nichel free;
  - bottoni Yvette e a pressione.
- **Le bobine della Tav. 2.** Che siano il loro magazzino; che la bobina chiara sia tondino in pelle.
- **Contatti.** Telefono principale 049 980 2326. Il 049 980 2330 è il fax? Gli orari (venerdì solo mattina, sabato e domenica chiusi) vanno confermati. Mancano la pagina privacy e il link Facebook definitivo.
- **Fuori pagina.**
  - PEC, dipendenti, superficie, clienti;
  - sede storica di Noventa Padovana;
  - e-shop annunciato;
  - "Nostre creazioni" e "Occasioni macchine";
  - rapporto con Astor.

### Foto da rifare dal vero (indicazioni di scatto)
Tutte sulla stessa carta avorio opaca (vicina a #F2EDE4), con sole vero o un'unica luce dura da sinistra a circa 30 gradi, ombra netta a destra. Macro 100 mm su cavalletto, f/8-f/11, file almeno 4000 px.
1. **Apertura.** Una fibbia Hambro in zama ad ardiglione, smontata (telaio, ardiglione, passante), posata come nella Tav. 1. Inquadratura orizzontale 16:10 con la carta libera nel terzo sinistro per il titolo, più uno scatto verticale con la fibbia intera al centro per il telefono. È la foto che manca perché la prima schermata arrivi a 8.
2. **Finiture.** La stessa fibbia in oro, nichel, brunito e ramato, stesso punto e stessa luce, per il selettore di finitura (oggi non in pagina).
3. **Nuda e ricoperta.** La stessa fibbia da ricoprire da 40, 50 e 60 mm, prima in metallo nudo e poi ricoperta in pelle, con un righello nel campo. Prende il posto del dittico Rodrigues e Karimov.
4. **Strisce a taglio vivo.** In macro, una per misura (2, 4, 16, 30, 60), stese in piano sulla carta: il fiore e il taglio devono leggersi. Servono per la striscia del banco al posto della grana di Karimov.
5. **Bobine.** In magazzino o in studio, la bobina intera e un dettaglio dei giri, stessa luce, niente scaffale. Prendono il posto delle due foto da telefono della Tav. 2.
6. **Cassetto.** Gli 11 oggetti del cassetto rifotografati alla stessa scala (stessa distanza, stesso obiettivo), dall'alto, sulla stessa carta.
7. **Laboratorio di Vigonovo.** Le mani di chi ricopre una fibbia e un semilavorato sul banco. Prendono il posto della foto di Berg.

### Licenze e loghi
- Foto Unsplash in pagina (Rodrigues `2hWmYcG26E8` e `hqGQcZnEvy0`, Karimov `DmxTTqZtDds`, Berg `an44PeEll_w`): Unsplash License, solo segnaposto, da sostituire prima di qualsiasi uso pubblico. Le foto di fibbie dorate di Rodrigues restano a questa home. Dettagli in `assets/CREDITI.md`.
- Foto e scontornati presi da hambro.it: i diritti vanno chiariti (gli scontornati sembrano foto di produttore).
- Logo: in pagina c'è la scritta HAMBRO in Mona Sans, color cuoio, al posto del JPEG 175x98. Serve il logo vettoriale.
- Mona Sans: SIL Open Font License 1.1, uso commerciale libero, file serviti dalla pagina.

### Soglie "da guardare" di segnali.sh e perché restano
- 5 fasce di fondo: apertura, banco cuoio, carta, contatti cuoio, piede. Sono un fondo e due campi nel colore della casa, voluti.
- 2 numeri grandi: la lettura del banco, che è lo strumento, e il 1979, sempre con il nome di Gastaldello.
- La numerazione 01-11 del cassetto è l'indice del campionario, non una procedura.
