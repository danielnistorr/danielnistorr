# Area Systems: proposta di nuova home

Proposta non richiesta di una nuova homepage per Area Systems srl (Tombelle di Vigonovo, VE). Riguarda solo la home. L'azienda non è stata contattata, nessun modulo è stato inviato e niente è pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale (statica, si apre con file:///). Accanto ci sono `sito/img/` (solo le immagini usate, WebP in più larghezze) e `sito/fonts/` (Overpass woff2 e la licenza OFL).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg` e `NOTA.md` (idea, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà tutto, cioè immagini (`finale_img.py`), controllo U+2014, prova del gesto e del menu (`prova_gesto_finale.mjs`), screenshot e misura dei segnali.
- `_prova/home/a/` e `_prova/home/b/`: le due bozze. Il committente ha scelto la B, "Il quadro aperto", e la home finale parte da lì.
- `01-analisi.md`: fatti con le fonti, il sito di oggi, i voti delle foto, i riferimenti.
- `assets/CREDITI.md`: licenze delle foto.

## Da confermare con l'azienda (in pagina non c'è niente di inventato)

1. **Il titolo** "Il clima giusto dentro il quadro" è una nostra proposta e va approvato.
2. **Chi produce le linee con sigla propria** (ASB, ASVC, ASVE, ASRC, ASTH, AS-CC, AS-T5) e cosa vuol dire "ideata da Area Systems" per l'ASRC. In pagina non scriviamo "le nostre serie", ma solo i nomi.
3. **I marchi distribuiti** (ACDCFAN, Commonwealth, Jason Fan, ECOFIT, Mean Well, Relpol, Lonyung, MAUS Stixx): bisogna sapere se sono distributori ufficiali e se possono nominarli. In pagina compaiono come "i marchi che distribuiamo".
4. **La serie dei due pezzi del catalogo 2022**: il gruppo con griglia cromata e telaio nero (pag. 13) è ASB, GB/F o GA? La resistenza alettata (pag. 53) è CTSH, ASTH o STH? Le didascalie restano generiche finché non lo sappiamo.
5. **Dove va ogni pezzo nel quadro.** Le frasi del cartellino sono indicazioni di montaggio generali, da far rileggere a loro:
   - torrino sul tetto;
   - lampada sotto il tetto;
   - condizionatore sulla porta o sul fianco;
   - gruppo con filtro sulla porta, in basso;
   - termostato e resistenza sulla guida DIN.

   La guida DIN da 35 mm è scritta nella scheda CTSH; per i termostati DTV/DTR la scheda non dice come si montano.
6. **Numeri pubblicabili**: clienti, articoli a magazzino, tempi di consegna. Oggi la pagina non ne ha nessuno di loro, solo misure di prodotto.
7. **"Dal 2016"** (nel piede) viene da aziende.it, cioè dal codice ATECO, e non dal sito. C'era un'attività precedente dei soci?
8. **Le sedi**: Saonara è solo sede legale? A Tombelle si ricevono clienti e c'è un magazzino? Servono anche gli orari.
9. **La PEC** area.systems@pec.it viene da aziende.it e non dal sito: va confermata.
10. **I collegamenti esterni**: i PDF dei cataloghi puntano a `areasystems.it/files/` e le schede alle pagine di oggi; privacy e cookie puntano alla policy iubenda 25167846. Vanno ricontrollati al passaggio al nuovo sito. Oggi rispondono tutti 200.
11. **Il diritto d'uso** degli scontornati del sito (sembrano dei produttori) e delle due foto del catalogo 2022.
12. **Il carattere, per la campagna**: Overpass è usato anche nel sito finale di 3Esse e nel WordPress di Gardens Pav. È rimasto qui perché il committente ha scelto questa bozza così. Se ogni azienda deve avere un carattere suo, va cambiato in uno dei tre siti.

## Logo

In pagina c'è il marchio orizzontale (le ali con la scritta AREA SYSTEMS a destra), ricostruito dal JPEG più grande del sito (`style-Area-System-logo.jpg`, 1047 x 592) a 2x, con il fondo bianco reso trasparente. Regge a 41 px di altezza, ma è un ripiego. **Va chiesto il vettoriale** (SVG, PDF o AI) e va chiesto se esiste già una versione orizzontale ufficiale.

## Foto da rifare dal vero

Nessuna foto in apertura è di Area Systems. La foto del quadro e la fascia dei fili sono **segnaposto** di Unsplash (Raymond Sime): non sono loro quadri e nessun pezzo inquadrato è loro. Vanno sostituite prima di ogni uso pubblico. Serve mezza giornata di scatti.

1. **Il quadro aperto (apertura)**:
   - un loro quadro vero in RAL 7035, porta aperta a sinistra, fotografato frontale e un po' da sinistra come la foto di oggi (luce piatta e uniforme, niente ombre dure, almeno 3000 px di larghezza);
   - montati e ben visibili: un gruppo ASB sulla porta in basso, un condizionatore ASVC sulla porta o sul fianco, un torrino GT sul tetto, una lampada AS-T5 sotto il tetto, una resistenza CTSH e un termostato DTV sulla guida DIN, alimentatori Mean Well;
   - il cablaggio ordinato e meno fitto di quello della foto di oggi; nessun marchio di altri in primo piano.
   - Con lo scatto vero le etichette indicano pezzi veri: basta spostare i sei punti, cioè le coordinate `--x/--y` e `--mx/--my` nel file.
2. **La fascia**: lo stesso quadro, da vicino, sulla fila dei fili con le etichette e i loro alimentatori Mean Well. Taglio orizzontale circa 3:1, almeno 2400 px di larghezza.
3. **I pezzi in still life**, al posto delle foto del catalogo e degli scontornati del cartellino:
   - gruppo con filtro, resistenza alettata, torrino, condizionatore, termostato, lampada;
   - fondo grigio chiaro uniforme, luce laterale morbida, ombra corta, frontale o di tre quarti, almeno 2400 px sul lato lungo;
   - pezzi puliti dalla polvere.
4. Se c'è un magazzino a Tombelle: una foto degli scaffali con le scatole e le sigle leggibili. Sarebbe la prima prova visiva dell'azienda.

## Licenze

- **Overpass**: The Overpass Project Authors (Red Hat), SIL Open Font License 1.1, da Google Fonts, servito dalla pagina (`sito/fonts/OFL.txt`).
- **Foto Unsplash** (`NAchd3UmxXo`, `KDkU44ikiko`, Raymond Sime): Unsplash License, uso commerciale libero e senza attribuzione obbligatoria, verificata sulla pagina di ogni foto il 19/10/2026. Il dettaglio è in `assets/CREDITI.md`.
- **Foto del catalogo 2022 e scontornati del sito**: di Area Systems o dei produttori, diritti da chiarire (punto 11).

## Note di progetto

- **Una riga "da guardare" dei segnali**: le misure degli H2 sono solo due (64 e 132 px). È voluto: l'elemento grande è il titolo d'apertura e il numero di telefono chiude la pagina.
- **Il cartellino a 1440** è fermo in basso a destra, sopra la fila dei moduli, perché non copra nessuna etichetta. Sotto i 1180 px passa sotto la foto.
- **A 1920 la fascia dei fili** è ingrandita di 1,4 volte: la sorgente non ha altri pixel senza il marchio dei loro alimentatori concorrenti. Con lo scatto vero il problema sparisce.
