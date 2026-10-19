# Area Systems: proposta di nuova home

Proposta non richiesta di una nuova homepage per Area Systems srl (Tombelle di Vigonovo, VE). Riguarda solo la home. L'azienda non è stata contattata, nessun modulo è stato inviato e niente è pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale (statica, si apre con file:///). Accanto ci sono `sito/img/` (solo le immagini usate, WebP in più larghezze) e `sito/fonts/` (Overpass woff2 e la licenza OFL).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (solo contatti e piede) e `NOTA.md` (idea, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà tutto, cioè immagini (`finale_img.py`), controllo U+2014, prova del gesto e del menu (`prova_gesto_finale.mjs`), misure della prima schermata da 320 a 2560 (`misure_rifinitura.mjs`), screenshot e misura dei segnali.
- `_prova/home/a/` e `_prova/home/b/`: le due bozze. Il committente ha scelto la B, "Il quadro aperto", e la home finale parte da lì.
- `01-analisi.md`: fatti con le fonti, il sito di oggi, i voti delle foto, i riferimenti.
- `assets/CREDITI.md`: licenze delle foto.

## Da confermare con l'azienda (in pagina non c'è niente di inventato)

1. **Il titolo** "Il clima giusto dentro il quadro" è una nostra proposta e va approvato.
2. **Chi produce le linee con sigla propria** (ASB, ASVC, ASVE, ASRC, ASTH, AS-CC, AS-T5) e cosa vuol dire "ideata da Area Systems" per l'ASRC. In pagina non scriviamo "le nostre serie", ma solo i nomi.
3. **I marchi distribuiti** (ACDCFAN, Commonwealth, Jason Fan, ECOFIT, Mean Well, Relpol, Lonyung, MAUS Stixx): bisogna sapere se sono distributori ufficiali e se possono nominarli. In pagina compaiono come "i marchi che distribuiamo".
4. **Le portate dei gruppi ASB per misura** (sezione "Gruppi ASB in cinque misure"): 24-36, 56-60, 120-211, 198-430 e 550-700 m³/h, prese dalla tabella della scheda ASB raggruppando i modelli per lato. Da far rileggere a loro, come le sigle brevi ASB08...ASB32 usate per le cinque taglie.
5. **La serie dei due pezzi del catalogo 2022**: il gruppo con griglia cromata e telaio nero (pag. 13) è ASB, GB/F o GA? La resistenza alettata (pag. 53) è CTSH, ASTH o STH? Le didascalie restano generiche finché non lo sappiamo.
6. **Dove va ogni pezzo nel quadro.** Le frasi della legenda sono indicazioni di montaggio generali, da far rileggere a loro:
   - torrino sul tetto;
   - lampada sotto il tetto;
   - condizionatore sulla porta o sul fianco;
   - gruppo con filtro sulla porta, in basso;
   - termostato e resistenza sulla guida DIN.

   La guida DIN da 35 mm è scritta nella scheda CTSH; per i termostati DTV/DTR la scheda non dice come si montano.
7. **Numeri pubblicabili**: clienti, articoli a magazzino, tempi di consegna. Oggi la pagina non ne ha nessuno di loro, solo misure di prodotto.
8. **"Dal 2016"** (nel piede) viene da aziende.it, cioè dal codice ATECO, e non dal sito. C'era un'attività precedente dei soci?
9. **Le sedi**: Saonara è solo sede legale? A Tombelle si ricevono clienti e c'è un magazzino? Servono anche gli orari.
10. **La PEC** area.systems@pec.it viene da aziende.it e non dal sito: va confermata.
11. **I collegamenti esterni**: i PDF dei cataloghi puntano a `areasystems.it/files/` e le schede alle pagine di oggi; privacy e cookie puntano alla policy iubenda 25167846. Vanno ricontrollati al passaggio al nuovo sito. Oggi rispondono tutti 200.
12. **Il diritto d'uso** degli scontornati del sito (sembrano dei produttori) e delle due foto del catalogo 2022.
13. **Il carattere, per la campagna**: Overpass è usato anche nel sito finale di 3Esse e nel WordPress di Gardens Pav. È rimasto qui perché il committente ha scelto questa bozza così. Se ogni azienda deve avere un carattere suo, va cambiato in uno dei tre siti.

## Logo

In pagina c'è il marchio orizzontale (le ali con la scritta AREA SYSTEMS a destra), ricostruito dal JPEG più grande del sito (`style-Area-System-logo.jpg`, 1047 x 592) a 2x, con il fondo bianco reso trasparente. Regge a 41 px di altezza, ma è un ripiego. **Va chiesto il vettoriale** (SVG, PDF o AI) e va chiesto se esiste già una versione orizzontale ufficiale. Il giudice ha proposto di ridisegnarlo in SVG: non l'abbiamo fatto, perché il logo è loro e un ricalco del JPEG ne copierebbe i difetti.

## Foto da rifare dal vero

Nessuna foto in apertura è di Area Systems. La foto del quadro aperto (Raymond Sime) e la fascia del quadro chiuso (Victor Ferreira, con il cartello di pericolo tolto) sono **segnaposto** di Unsplash: non sono loro quadri e nessun pezzo inquadrato è loro. Vanno sostituite prima di ogni uso pubblico. Serve mezza giornata di scatti.

1. **Il quadro aperto (apertura)**:
   - un loro quadro vero in RAL 7035, porta aperta a sinistra, fotografato frontale e un po' da sinistra come la foto di oggi (luce piatta e uniforme, niente ombre dure, almeno 3000 px di larghezza);
   - montati e ben visibili: un gruppo ASB sulla porta in basso, un condizionatore ASVC sulla porta o sul fianco, un torrino GT sul tetto, una lampada AS-T5 sotto il tetto, una resistenza CTSH e un termostato DTV sulla guida DIN, alimentatori Mean Well;
   - il cablaggio ordinato e meno fitto di quello della foto di oggi; nessun marchio di altri in primo piano.
   - Con lo scatto vero le etichette indicano pezzi veri: basta spostare i sei punti, cioè le coordinate `--x/--y` e `--mx/--my` nel file.
2. **La fascia del quadro chiuso**: lo stesso quadro, chiuso, frontale, con il loro gruppo ASB incassato nella porta in basso e la griglia di uscita in alto (o il torrino sul tetto). Luce piatta e fredda come l'apertura, taglio orizzontale circa 3:1, almeno 2880 px di larghezza, nessun cartello o marchio di altri.
3. **I pezzi in still life**, al posto delle foto del catalogo e degli scontornati della legenda:
   - gruppo con filtro, resistenza alettata, torrino, condizionatore, termostato, lampada;
   - fondo grigio chiaro uniforme, luce laterale morbida, ombra corta, frontale o di tre quarti, almeno 2400 px sul lato lungo;
   - pezzi puliti dalla polvere.
4. Se c'è un magazzino a Tombelle: una foto degli scaffali con le scatole e le sigle leggibili. Sarebbe la prima prova visiva dell'azienda.

## Licenze

- **Overpass**: The Overpass Project Authors (Red Hat), SIL Open Font License 1.1, da Google Fonts, servito dalla pagina (`sito/fonts/OFL.txt`).
- **Foto Unsplash** (`NAchd3UmxXo` di Raymond Sime, `pLvgCVtwbls` di Victor Ferreira): Unsplash License, uso commerciale libero e senza attribuzione obbligatoria, modifiche ammesse, verificata sulla pagina di ogni foto il 19/10/2026. La foto `KDkU44ikiko` (fascia dei fili) non è più usata. Il dettaglio è in `assets/CREDITI.md`.
- **Foto del catalogo 2022 e scontornati del sito**: di Area Systems o dei produttori, diritti da chiarire (punto 12).

## Note di progetto

- **La legenda del pezzo scelto** sta sulla carta, nella colonna destra dell'apertura, sotto la frase, con altezza fissa: non copre la foto. Sotto i 1180 px passa sotto la foto, con la riga "Scegliete un numero sulla foto.".
- **La chiusura è l'etichetta dati del quadro**: telefono, email e sedi stanno in campi su un adesivo bianco, sulla lamiera chiara; il piede è una riga sola con i dati societari, la PEC e privacy e cookie. Ha sostituito il telefono a 96 px, la riga di tre colonne e il piede a quattro colonne. Gli H2 hanno una sola misura (64 px).
- **La prima schermata non è stata ripensata** nonostante il giudizio cieco (che la trovava troppo vicina a quella di Bertolin Antonio e chiedeva un solo pezzo loro scontornato): il committente ha scelto questa bozza. Il rimedio vero è lo scatto del punto 1 qui sopra.
