# Fratelli Ruffatti, home HE (7 novembre 2026, dopo il giro di ritocco)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, compreso `data-he-scale-fine`; vendor senza Flip), i caratteri in `sito-he/fonts/` con le licenze OFL, le immagini WebP in `sito-he/img/` (30 file, cartella `sito-he` 2,1 MB). La `sito/` di oggi non è toccata. Direzione artistica in `DIREZIONE-HE.md` (prima stesura; le modifiche del giro di ritocco sono scritte qui sotto).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8782`), `foglio-1440.jpg` (24 fotogrammi) e `foglio-390.jpg` (27), i fotogrammi uno al secondo, `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il titolo è salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `Ruffatti-Sito`; legge `assets/originali/wp/`, fuori da git; con un nome, per esempio `sipo`, rifà solo quella); prove con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; controllo d'uso dal telefono con `node _prova/he/script/uso.mjs <url>`; riferimenti con `node _prova/he/script/riferimenti.mjs`. Segnali da IA: `_metodo/kit/segnali.sh <url> _prova/he/segnali ruffatti-he`.

## Idea

**Prima di partire, ogni organo si monta qui.** "Ogni strumento Ruffatti, anche di grande dimensione, viene premontato in fabbrica" (pagina `l'interno di un organo Ruffatti`). Il gesto d'apertura lo fa vedere: la cornice mostra canne di facciata e cassa di mogano, come in chiesa; scorrendo si apre sulla falegnameria di Padova, con i banchi, i neon e tre artigiani: è l'organo della Cattedrale di Aguascalientes prima della partenza. Il gesto si ferma in una cornice media e sotto, nella fascia di pietra, la frase dell'idea è scritta in grande nel carattere display. La sezione firma è il registro che il loro sito inglese chiama "the signature stop of Fratelli Ruffatti": la Trompette en chamade, trombe d'ottone costruite in casa, con la prova fotografica (le 61 trombe di Uppsala).

## Sezioni (scheletri diversi)

1. **Apertura, in fabbrica** (fissata sopra i 900 px): composizione in asse come una facciata. Cornice sulle canne al centro, "Organi a canne" a 207 px sotto, su una riga; in alto a sinistra nome, "Padova, dal 1940" e via Facciolati 166 (apre la mappa); in alto a destra il mestiere in italiano e in inglese, "Restauro di organi antichi" e "Write to us in English". Scorrendo la cornice si apre e si ferma a `inset(0% 9% 17% 9%)` (`data-he-scale-fine`): a 1440 la foto è larga 1181 px e alta 747; sotto, nella fascia di pietra, "Prima di partire, ogni organo si monta qui." in Imbue 300 su una riga (84 px a 1440, 96 a 1920, allineata al bordo sinistro della foto) e, a destra, solo la prima frase della didascalia a 15 px (luogo, tastiere, anno). Tra 900 e 1199 px la fascia tiene solo l'idea. Il resto della didascalia (la frase sulla premontatura e l'inglese) resta nel testo per i lettori di schermo ed è in vista con "riduci movimento" e sul telefono. Oltre i 1597 px il riquadro della foto non cresce più (centrato): a 1920 la falegnameria è alla misura nativa invece che a 1,20.
2. **Manifesto**: la loro frase "costruiamo ogni componente possibile in laboratorio" a 29 px (22-30) nelle colonne 4-10, la stessa frase dal loro sito inglese sotto; spazio sopra e sotto dimezzato (94 e 86 px a 1440).
3. **La materia, "Tutte le canne sono costruite in casa"**: il titolo con il testo nelle colonne 1-4 resta fermo (`position:sticky`, 120 px dalla cima) mentre scorrono quattro ritagli 4:5 sul dettaglio, in una griglia 2×2 nelle colonne 5-8 e 9-12 (424×530 a 1440), con la colonna destra 160 px più in basso e 72 px tra le file: la testa del tronco di sipo con l'uomo che la misura, le mani sulla cassetta della lastra, le bocche delle canne, le noci tornite; ognuna con una frase loro. Sul telefono niente sticky e foto in colonna a tutta larghezza; a 768 alternate a sinistra e a destra, larghe al massimo 512 px.
4. **Stacco alla misura vera**: la canna ad ancia smontata a 800 px, la sua misura nativa, ritagliata sulla fascia dell'oggetto (800×360) e con il fondo bianco portato alla pietra; accanto la loro frase e il video della Bombarda di 32 piedi. Altezza naturale, 80 px sopra e sotto (prima era una schermata quasi vuota).
5. **Firma, "Trompette en chamade"** (mogano pieno, l'unico colore pieno): 86 px sopra e sotto a 1440 (56-96); il titolo in ottone a 215 px largo tutta la griglia; sotto, le trombe di Uppsala nelle colonne 6-12 che escono dal bordo della finestra come escono dalla cassa (820 px a 1440, 1,03 della nativa; a 1920 ferme a 1000 px, 1,25, sempre fino al bordo); a sinistra, nelle colonne 1-4 e in basso, la frase inglese, quella italiana e il dato dalla disposizione fonica (Trompette en Chamade 8′, 61 canne, quarta tastiera). Tolta la saldatura del padiglione. A 1440x900 titolo e trombe stanno in una schermata.
6. **Un luogo a tutta pagina**: la chiesa di Boteå, l'organo grigio perla sotto le volte bianche, con la parallasse.
7. **Dove suonano, "Da Padova abbiamo raggiunto tutti i continenti"**: Uppsala intera a sinistra; a destra otto luoghi in forma di disposizione fonica (nome e città, puntini di guida, tastiere e anno), da Monreale (sei tastiere) a New Orleans 2022, e la citazione di Frederick Swann. Sul telefono il titolo e il testo vengono prima della foto (32 px sopra la foto, 40 sopra la disposizione).
8. **Restauro** (pietra più scura): cinque organi di altri costruttori in fila per data (1579 La Valle, 1612 Guglielmi, 1766 Callido, 1802 Zavarise, 1904 Telford), che sul telefono si sfogliano col dito; sotto, che cosa preparare per la prima telefonata, "Chiamate 049 750 666" e "Scrivete con le foto".
9. **Concorso di Miami**: una fascia, la finale dell'undicesima edizione il 5 febbraio 2027, i premi, il bando e la pagina.
10. **Chiusura**: il telefono a 115 px in Imbue da toccare, email e indirizzo con la mappa; "Un organo nuovo: che cosa mandarci" con l'email composta, "Writing from abroad" in inglese con la sua email composta e il modulo inglese di oggi; la foto d'archivio delle maestranze con la famiglia in una riga.
11. **Piede** (inchiostro): logotipo corsivo dalla maschera della newsletter 2020, sede con la mappa, contatti, sito, Altrove (Instagram, YouTube, Facebook, English, Русский), P.IVA, Maestro d'Arte e Mestiere 2020, Privacy e cookie.

Due sezioni di fila non hanno più lo stesso schema: la firma (titolo a tutta griglia, testo a sinistra, foto a destra fino al bordo) non ripete più i luoghi (foto a sinistra, testo a destra).

## Caratteri e colore

- **Imbue** (Tyler Finck, SIL OFL 1.1, file variabile con asse ottico) solo nei momenti forti: titolo d'apertura (207 px a 1440, 109 a 390), la frase dell'idea (84 / 43 px; 42 px con "riduci movimento"), "Trompette en chamade" (215 / 82; al massimo 266 px), telefono della chiusura (115 / 60). Bodoniano stretto: in "Organi a canne" le aste stanno in fila come le canne di una facciata.
- **Wix Madefor Text** (Dalton Maag, SIL OFL 1.1) per tutto il resto: `h2` 42 / 28 in peso 500, manifesto 29 / 22 (35 parole: sotto il tetto dei 30 px), testo 18 / 17, didascalie 15. Nessun corsivo, nessun maiuscolo spaziato, nessuna etichetta o numero sopra i titoli (gli anni del restauro stanno sulla riga del nome).
- Registro: riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Imbue è la seconda home su 45 (l'altra è Tacchificio Riviera, altra zona, con un altro testo); Wix Madefor Text nessuna. Nessuna delle due è nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`.
- Colori: pietra #F2EEE6, inchiostro #1A1511, mogano sipo #3D170E (solo la firma), ottone #D9B56E sul mogano e #7A5A1E sulla pietra, stagno #6B655D per i testi secondari.

## Movimento

- Gesto: `data-he-scale` con `data-he-scale-zoom="1"` (nessun ingrandimento: la foto è del 2005, 1597 px), `data-he-scale-fine="inset(0% 9% 17% 9% round 0px)"` (la foto si ferma in una cornice media, non a tutta pagina) e `data-he-split data-he-subito` sul titolo. La didascalia entra con il gesto (`data-he-scale-entra`).
- Sostegno 1: `data-he-split` sul titolo della firma. Sostegno 2: `data-he-parallax="0.05"` su Boteå, l'unica foto larga di un luogo.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con il numero. Il titolo della materia fermo mentre scorrono le foto è `position:sticky` in CSS, non un movimento del kit. Nient'altro: niente sipario, indice, prima e dopo, racconto con foto ferma, galleria fissata, dissolvenze. Bottoni che si invertono di colpo, senza transizioni né opacità.
- Eccezioni al kit, scritte nello `<style>` della pagina: sotto i 900 px l'apertura non è a tutta altezza (titolo, testo, poi la foto ritagliata 4:5, poi l'idea in Imbue); la banda di Boteå usa `top:-8%` e `height:116%`; il riquadro della foto d'apertura ha `max-width:1597px`.

## Foto usate

Tutte della Fratelli Ruffatti, riscaricate il 7/11/2026 dalla libreria media di WordPress (`/wp-json/wp/v2/media`, 453 voci, le varianti più grandi) in `assets/originali/wp/`; anche le schede PDF e le newsletter sono state aperte (`assets/originali/pdf/`), ma non contengono foto più grandi. Nessuna foto di repertorio, nessuna immagine generata. Un trattamento solo (`immagini.py`): bianco a metà verso il grigio, colore 0,82, una curva dal nero inchiostro al bianco pietra, grana del kit a 0,14.

| In pagina | File originale | Misura nativa (ritaglio) | Mostrata a 1440 / 1920 |
|---|---|---|---|
| Apertura, Aguascalientes in falegnameria | `2016_04_falegnami-21.jpg` | 1597x1198 | resa a 1440 (0,90), finestra di 1181x747 a fine gesto / resa a 1597 (1,0), finestra 1310x896; telefono: ritaglio 900x1125 |
| La testa del tronco con l'uomo | `2016_03_xFoto-Sipo-2.jpg` | 800x544 (435x544) | 424 (0,97) / 512 (1,18) |
| Le mani sulla lastra | `2016_04_xFusione-6modif.jpg` | 800x798 (420x525) | 424 (1,01) / 512 (1,22) |
| Le bocche delle canne | `2016_04_xOFFSETS-95MODIF.jpg` | 800x905 (512x640) | 424 / 512 (1,0) |
| Le noci tornite | `2016_04_xImmagine-006.jpg` | 640x512 (410x512) | 424 (1,03) / 512 (1,25, il tetto: per questo le quattro foto sono larghe al massimo 512 px) |
| Canna ad ancia smontata | `2016_04_xtrompette3.jpg` | 800x603 (800x360) | 800 / 800 (1,0) |
| Trombe di Uppsala | `2016_04_xDSC_00860001.jpg` | 800x532 | 820 (1,03) / 1000 (1,25) |
| Boteå, a tutta pagina | `2018_11_P1270600-1.jpg` | 3264x2448 | 1440 / 1920 (file da 1920) |
| Uppsala intera | `2016_02_home-ruffatti2.jpg` (la `home-ruffatti4` ha 245 px di bianco a sinistra) | 900x1600 | 536 / 657 |
| Restauro: La Valletta, Vallicella, Corinaldo, Isera, Cobh | `xDSC_0011`, `xP1050744`, `xFile0149`, `xFile0145`, `xP1070186` | 800 di larghezza (Cobh 800x600, ritaglio 450x600) | 244 / 301, ritagli 2:3 |
| Maestranze, archivio | `2016_03_storia1-575.jpg` | 900x575 | 424 / 520 |
| Logotipo | maschera a 1 bit 5024x1172 della newsletter 2020 | | PNG 360 in testata, 960 nel piede |

Uscita dalla pagina: la saldatura del padiglione (`2016_04_xchamades-sald.jpg`, 576x485). Nessuna foto oltre 1,25 volte la sua larghezza nativa (misurato da `prove.mjs`): la peggiore è 1,25 a 1920 (noci e trombe), a 1440 1,03.

## Misure e prove (sezione 6)

- **Scorrimento orizzontale e errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento": larghezza del documento uguale alla finestra, nessun elemento oltre il bordo (le trombe della firma escono fino al bordo, non oltre), nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma; testo identico con e senza movimento (6.751 caratteri a 1440, 6.683 a 390), nessun elemento nascosto. L'apertura resta incorniciata, con l'idea in Imbue e la didascalia intera a sinistra sotto il nome. Con il movimento l'unico elemento a opacità 0 in cima alla pagina è la didascalia d'apertura, che entra con il gesto.
- **Peso al primo caricamento** (rete a riposo, senza scorrere): 499 KB a 1440 e 391 KB a 390 (soglie 2,5 e 1,5 MB); 414 a 768, 477 a 1024, 499 a 1920. Foto d'apertura e due caratteri precaricati, con `media` diverso per telefono e schermo; tutte le altre immagini pigre.
- **Layout stabile**: CLS 0 a tutte e cinque le larghezze, con e senza movimento (tutte le immagini hanno larghezza e altezza).
- **Misura vera delle foto**: la peggiore 1,03 a 1440 e 1,25 a 1920 (noci e trombe, al tetto); a 390 0,85.
- **Altezza**: 10.851 px a 1440 con l'apertura fissata, 9.861 fermi (prima 12.504 e 11.514); 12.868 a 390. 976 parole in `main`.
- **Funzioni**: 5 link `tel:` (testata fissa compresa), 5 `mailto:` di cui 3 con oggetto e traccia (organo nuovo, restauro, in inglese), 3 link alla mappa, modulo inglese di oggi, P.IVA, Privacy e cookie, EN e RU.
- **Controllo d'uso dal telefono** (`uso.mjs`, 390x844): nella prima vista ci sono il numero (testata), "Organi a canne", il mestiere e via Facciolati 166 con la mappa; nessuna area di tocco sotto i 44 px; il menu si apre, porta al restauro e si chiude; a metà pagina il numero è ancora in testata.
- U+2014: nessuno, nella pagina, negli script e in questa nota.

## Giudizio

**Primo giudizio del giudice: 7,5** (Design 7,0, Creatività 7,5, Usabilità 8,0, Contenuto 8,5), sotto la soglia di 8. Le foto pesano per circa il 60% della distanza; i cinque interventi valevano circa 0,6 punti senza foto nuove. Violazioni segnalate: lo spazio di `#luoghi` sul telefono, l'indirizzo in prima vista dato "da confermare", "Settecento" per Callido.

**Giro di ritocco** (in ordine):
1. `#apertura`: `data-he-scale-fine="inset(0% 9% 17% 9% round 0px)"` (il `round 0px` come nella cornice di partenza, perché le due forme si interpolino numero per numero); guardata al 100% a 1440, 1280x720, 1366x768, 1024x768 e 1920: la falegnameria resta morbida (compatta del 2005) ma in una cornice media non si legge più come foto di pagina; a 1920 il riquadro si ferma a 1597 px, così la foto non è più ingrandita. L'idea in Imbue 300 su una riga nella fascia di pietra; tolto il riquadro della didascalia, a destra solo la prima frase a 15 px. Con "riduci movimento" e sul telefono l'idea resta in vista in Imbue (42 e 43 px), con la didascalia intera.
2. `.firma`: trombe nelle colonne 6-12 fino al bordo, testo nelle colonne 1-4, tolta `.f-sald`, `padding-block:clamp(56px,6vw,96px)`.
3. `#materia`: quattro ritagli 4:5 sul dettaglio in `immagini.py`; titolo sticky nelle colonne 1-4; griglia 2×2 nelle colonne 5-8 e 9-12, colonna destra 160 px più in basso, `row-gap:72px`; tolti i `margin-top` di `.mf-*`; sul telefono niente sticky e foto in colonna.
4. `.manifesto` a `clamp(22px,2vw,30px)` nelle colonne 4-10 con il padding dimezzato; `.stacco` ad altezza naturale con 80 px.
5. `#luoghi` a 390: flex in colonna con `.l-testa` prima della foto.
6. Contenuti: l'indirizzo resta (vedi "Problemi aperti", è nel piede del sito di oggi); Callido ha la data dell'organo, 1766.

**Dopo il ritocco**, guardati il foglio nuovo a 1440 e a 390 e quattro fotogrammi a piena misura estratti dal video a 1440 (5,5 s fine del gesto, 9 s materia, 11 s stacco, 13 s fine della firma), più le viste a 1920, 1280x720, 1024x768 e 768. Corretto quello che era storto:
- a 1920 il titolo della firma (286 px) usciva dalla maschera dello split e perdeva la "e" finale: ora al massimo 266 px (il difetto c'era già nella prima stesura, il giudice aveva guardato solo 1440);
- tra 900 e 1199 px la prima frase della didascalia non stava accanto all'idea (8 righe in 168 px, oltre la fascia): lì resta solo l'idea; da 1200 px la frase dell'idea si stringe quanto serve (`min()` sul `clamp`) per lasciare 240 px alla didascalia;
- tra la fine della materia e la canna ad ancia c'erano ancora 400 px vuoti: padding sotto la materia da 158 a 43 px e canna ad ancia ritagliata sulla fascia dell'oggetto (la foto aveva 170 px di fondo vuoto sopra e 200 sotto);
- testo della firma allineato in basso, accanto al piede della foto, invece che attaccato alla discendente della "p" del titolo.

## Problemi aperti

- **Foto**: da qui viene circa il 60% della distanza dal 9 (giudice). Tutto il laboratorio è a 800 px, compatta e flash; la falegnameria è morbida anche alla misura nativa; i ritagli della materia sono fra 410 e 512 px di larghezza.
- **Indirizzo e mappa**: risolto. Il piede del sito di oggi (ruffatti.com, home e pagina "Opere eseguite", lette il 7/11/2026) pubblica "Recapiti Via Facciolati, 166 35127 Padova Tel. 049 750 666 organs@ruffatti.com P.Iva 00207160284", come già in `01-analisi.md` (sezione 3). Resta in pagina con la mappa. "Address upon request" e "By appointment only" di Homo Faber riguardano le visite: "su appuntamento" non è in pagina. (Il punto 2 del LEGGIMI, scritto per la `sito/`, dice ancora "va confermato": non è stato toccato.)
- **Callido**: risolto. Nell'elenco dei restauri della pagina "Opere eseguite" c'è "Corinaldo (Ancona) – S. Agostino 1987 Gaetano Callido, 1766" (colonne: località e chiesa, anno di restauro, autore ed epoca di costruzione), e la didascalia della stessa pagina dice che il Santuario di S. Maria Goretti è la "ex Chiesa del Convento di S. Agostino". In pagina: 1766.
- **Citazione di Frederick Swann** e foto delle installazioni (Uppsala, Boteå, i restauri): permessi e autori da chiedere (LEGGIMI 7).
- **Cobh**: in pagina c'è solo che l'organo è stato smontato e portato in laboratorio (notizia del 2016); che il restauro sia finito non è nelle fonti.
- **Concorso**: "biennale" sulla pagina italiana, "triennial" nel bando 2027: in pagina nessuno dei due.
- **Numeri** (oltre 500 in Italia, oltre 50 negli USA, oltre cento restauri, "da mezzo secolo"): da confermare, quindi fuori dalla pagina.
- **Inglese**: le righe del mestiere, della premontatura, del manifesto, della firma e dei contatti sono in inglese (dal loro sito inglese); una home inglese intera non c'è e EN porta al sito inglese di oggi.
- **Русский** nel piede è nel carattere di sistema: i file dei caratteri sono solo latini.
- **Kit**: il `margin-top:-12%` della parallasse che tagliava la cima delle foto larghe è corretto anche nel kit (`top:-12%`); la pagina tiene i suoi `top:-8%` e `height:116%` per Boteå.
- **Modulo**: come nella versione di oggi, le strade del contatto sono email composte; il modulo vero (con allegati) va nella pagina Contatti del sito nuovo (LEGGIMI).

## Foto da rifare (in ordine di valore)

1. **Un organo in premontaggio nella falegnameria**, di giorno, frontale, a 4000 px o più, con due o tre persone al lavoro: è il gesto d'apertura, oggi una compatta del 2005 con i neon, che per questo si ferma in una cornice media.
2. **Le trombe en chamade** di un organo recente, dal basso e di lato, a piena risoluzione (l'originale di Uppsala), e la saldatura del padiglione in luce radente, che è uscita dalla firma perché a 576 px non reggeva accanto alle trombe.
3. **I quattro dettagli della materia** con lo stesso fotografo e la stessa luce, verticali 4:5 a 3000 px: la testa del tronco con una persona, le mani sulla colata della lastra, le bocche delle canne, le noci al tornio. Oggi sono ritagli da 410-512 px di foto da 640-800.
4. **Una canna ad ancia smontata** su fondo bianco, macro a 3000 px: lo stacco alla misura vera oggi è a 800 px.
5. **Gli originali delle installazioni** (Uppsala, Wayne, New Orleans, Pershore) e una foto dell'organo di Pershore Abbey.
