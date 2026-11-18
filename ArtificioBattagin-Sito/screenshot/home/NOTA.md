# L'Artificio Battagin, home

## Livello professionale, con il ritocco finale

Pagina: `sito/index.html` (statica, si apre con file:///; 8.367 px a 1440, 11.179 px a 390). La home di prima (cornice d'apertura con il titolo dentro) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot). L'uso viene dalla scheda `_prova/uso/SCHEDA.md`, seguita punto per punto; le prove dei due clienti tipo sono in `_prova/pro-prova-0/` e `_prova/pro-prova-1/`.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 di tutti e 14 (foglio `riferimenti.jpg`), le prime schermate a 390 della famiglia B (Joseph, Union, Poilâne, Petersham), le pagine intere di Joseph Brot e Union a pezzi.

Rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche `sito/img/` con `pro_img.py`); dentro ci sono gli screenshot (`pro_shoot.mjs`, JPEG senza PNG temporanei) e i controlli (`pro_controlli.mjs`, 63 su 63). Elementi che escono a destra: `node _prova/script/pro_largo.mjs <index.html> <larghezza>`.

Screenshot: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove siamo" al piede). Guardati a pezzi a 1440 e 390, e a 320, 768 e 1024; misurata la prima schermata anche a 1100, 1280 e 1920.

### Ritocco finale (3/11/2026): che cosa è cambiato

Dal controllo del livello professionale (voto 6, regole 7, 10, 14 e 15 non passate) e dalle prove dei due clienti tipo.

1. **L'apertura a 1440 non è più un riquadro nel margine** (difetto bloccante). Testo a sinistra, a destra la foto dei cavalletti in faggio del reparto, a filo del bordo destro e alta quanto la prima schermata: da y 89 a y 900, 626 x 811 px a 1440 (736 x 860 a 1920). È l'unica foto loro abbastanza grande (originale 2560 x 1707, ritaglio 1366 x 1707, `apertura-cavalletti-800/1200.jpg`): mai ingrandita. La foto del reparto proposta dal controllore (`negozio-169-1000.jpg`) in quel riquadro sarebbe stata ingrandita 1,44 volte, perché è larga 1000 px ma alta solo 562. La foto degli scaffali resta nell'apertura del telefono (come chiede la SCHEDA) e passa, dal computer, nella sezione Chi siamo, dove sta in 16:9 a 709 px; sul telefono Chi siamo mostra i cavalletti. Così ogni foto compare una volta sola per larghezza (`<picture>` con `media`). Le porte partono 96 px sotto la foto.
2. **Gli orari non promettono quello che non c'è.** La riga dell'apertura dice "ORARI Chiamaci prima di venire." su una sola riga, tra i due filetti; il link "Tutta la settimana" è nascosto finché `ORARI` è null e ricompare, con l'etichetta "Orari di oggi" e la tabella, appena gli orari si scrivono nello script (provato con dati di prova). Il piede non ha più il link "Orari" verso una sezione senza orari: c'è "Orari: chiamaci prima di venire", che lo script sostituisce con gli orari della settimana. La sezione si chiama "Orari e dove siamo" (titolo), con "Il negozio" come etichetta, e non ripete più l'indirizzo nel titolo.
3. **Numeri senza ripetizioni**: tolti "1000 mq" (resta nell'occhiello e nel manifesto, parole loro) e "79 €" (condizione di spedizione, resta nelle righe dello shop); tolto "Anni '70", già nell'occhiello. Restano quattro numeri in una riga di 4 colonne a 1440 (2 x 2 sul telefono): 5 sedi, Oltre 20 (anni di mestiere di Matteo), 22 corsi nel 2026, **186** prodotti nello shop online (sitemap, `01-analisi.md`).
4. **Testo corrente a 17 px a 1440**: descrizioni dei corsi, etichette dei numeri, note, spedizioni, modulo, didascalia e piede passano da 16 a 17 px da 1200 px. Misure: 88, 56, 32, 24, 19, 17, 16, 14 (8); i 16 px restano per etichette, bottoni, campi e date.
5. **Identità**: il logo in testata passa a 150 px a 1440 (sorgente 250 px); prima del piede c'è una fascia bianca con il logo intero a 250 px e il loro claim "Per i professionisti e gli amanti dell'arte." in Gambetta 56 px, così il logo non sta più su un riquadro bianco nel piede scuro (lì ora c'è il nome scritto). Un terzo colore preso dal logo, l'oro della L-cornice (#D8A000), solo per due filetti: sopra i numeri sul verde e sopra i tre passi delle cornici; mai per il testo. Con i cavalletti in legno e il pavimento blu in apertura, la pagina non si confonde più con BordinGarden (verde scuro, campi).
6. **Telefono, prima schermata**: la striscia della foto sale a 150 px; "Shop online: spedizione 10 €, gratis oltre 79 €." ora si legge intera sopra la piega (finisce a y 824 su 844) e resta entro due schermate come chiede la SCHEDA. Dal computer quella riga non c'è più in apertura (meno interfaccia), resta nella sezione Belle arti.
7. **WhatsApp con il numero** sul bottone dell'apertura da 760 px in su ("WhatsApp 380 2308602"); sul telefono il bottone è largo 171 px e il numero non ci sta: resta nel Menu, nella sezione Dove e nel piede.
8. **Cornici**: sotto i bottoni WhatsApp e Chiama c'è "Via della Croce Rossa 5/a, Padova · ampio parcheggio privato · Come arrivare" (indicazioni Google Maps), per chi deve portare l'opera.
9. **News in una riga** sotto il calendario: "DALLE NEWS" e i tre titoli come link (alti 44 px), senza il blocco di tre titoli in serif.
10. **Piede**: voci alte 44 px (prima 36), testo 17 px a 1440.
11. Sotto i 360 px il suggerimento del campo di ricerca diventa "Marca o prodotto", così non si taglia.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs`, 63 su 63, e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata `sticky`; a 390, a metà pagina, il bottone "049 7811043" è a 12 px dall'alto, alto 48 px, e si tocca; da 400 px dice "Chiama 049 7811043". "Orari e dove siamo" è la prima voce del menu (famiglia B). 5 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. "Negozio di belle arti a Padova" nel titolo (88 px su tre righe a 1440, 40 px a 390), prova nell'occhiello (anni '70, 1000 mq), "Chiama 049 7811043" pieno; a 390 a tutta larghezza (350 su 350 px).
3. **Immagine vera nell'apertura**: PASSA. A 1440 i cavalletti in faggio del reparto (foto loro, 2023, luce di vetrata) a tutta altezza e a filo del bordo, 626 x 811 px, senza ingrandimento; a 390 la striscia del reparto belle arti alta 150 px (18% dello schermo, la SCHEDA chiede al massimo un terzo).
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da Unsplash o Pexels; nessuna illustrazione; tutte le sorgenti vengono da `assets/originali/`.
5. **Foto in serie**: PASSA. Otto foto dello stesso servizio del 2023 (stessa luce, il pavimento blu che torna); tre formati per larghezza (a 1440: verticale 0,77 dell'apertura, 4:3 delle porte, 16:9 dei racconti; a 390: striscia, 4:3, 16:9); una didascalia (Matteo) su otto foto.
6. **Palette dal marchio**: PASSA. Il verde di BATTAGIN (#17633A) per bottoni, link e blocco dei numeri; il turchese della parete degli angolari (#D9E8E4) per Cornici e "Orari e dove siamo"; l'oro della L del logo (#D8A000) solo in due filetti. Neutri: bianco, inchiostro, grigio, grigio chiarissimo del modulo. Fondo bianco, niente beige.
7. **Scala corta e leggibile**: PASSA (prima no). 1440: 88, 56, 32, 24, 19, 17, 16, 14 (8 misure); nessun blocco di testo corrente oltre 55 caratteri sotto i 17 px (controllo nuovo in `pro_controlli.mjs`); 390: 40, 32, 24, 17, 16, 14 (6), testo 17 px. Sotto i 16 px solo la riga legale (14). Titolo 88 px maiuscolo, interlinea 0,98.
8. **Due famiglie**: PASSA. Gambetta 400 (titoli, numeri, date, prezzi, marche, voci del Menu del telefono) e Switzer 400 e 600 (testo, etichette, bottoni, modulo).
9. **Servizi in schede con foto**: PASSA. Tre porte in tre colonne da 760 px (sul telefono righe con la miniatura 4:3), stessa foto 4:3, nome, riga utile e link; tutta la scheda è un link.
10. **Almeno tre tipi di prove**: NON PASSA, per un dato che manca (2 su 4). Ci sono quattro numeri veri e la fascia dei fornitori con la didascalia (14 marche in Gambetta 56 px). Le recensioni (689 su Google, media 4,5, riportate da itaglietti.it) non sono verificate e non sono in pagina; clienti con il nome e certificazioni non ne hanno (negozio al dettaglio). Nel LEGGIMI, punto 2, è scritto dove andrebbe la fascia delle recensioni e in che forma.
11. **Lavori con un nome**: NON SI APPLICA (negozio al banco, nessuna commessa nelle fonti, la famiglia B non ha questa sezione). Al loro posto i corsi con data, docente, posti e prezzo.
12. **Ritmo a blocchi**: PASSA. Tre blocchi pieni oltre al piede (numeri sul verde, Cornici e "Orari e dove siamo" sulla parete), più la fascia bianca del logo prima del piede scuro; spazi tra le sezioni 96-128 px a 1440 e 64 px a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno verde e con il bordo verde, raggio 4 px, alti 52 px (48 in testata), Switzer 600 16 px; i bottoni di chiamata contengono "049 7811043".
14. **Modulo e "dove e quando"**: NON PASSA del tutto, per un dato che manca. Il modulo c'è ("Che cosa ti serve?": Un prodotto, Una cornice su misura, Un corso, Altro; nome, telefono, email, messaggio; compone un'email a negozio@artificiobattagin.it con oggetto "Dal sito: <tipo>, <nome>", da collegare a un servizio). La scheda del negozio ha Indicazioni, Chiama, WhatsApp, parcheggio, ingresso accessibile; nessun iframe. Manca la tabella degli orari: è pronta nello script ma gli orari non sono pubblicati (LEGGIMI, punto 1). Finché mancano la pagina non promette più una tabella.
15. **Piede completo**: NON PASSA del tutto, per lo stesso dato. Nome, riga sul negozio, A.B. s.r.l., P.IVA 04191710286, REA PD 369492; Negozio, Artinpratica (con Instagram e Facebook), Contatti (telefono, WhatsApp, email e indirizzo cliccabili, voci alte 44 px); cinque link legali; quattro colonne a 1440, testo di 14-17 px. Gli orari sono "chiamaci prima di venire" finché non arrivano (poi li scrive lo script). Certificazioni: non ne hanno.

### Uso: le prove della scheda e dei clienti tipo

- Visitatore 1 (390x844, senza scorrere): "belle arti" e "Padova" nel titolo; "ORARI Chiamaci prima di venire." (il posto è segnato, nessun link che porta a una sezione vuota); `tel:+390497811043` alto 48 px; `https://wa.me/393802308602`; "Come arrivare" (indicazioni) e "parcheggio privato"; il campo di ricerca ("Liquitex" porta a `https://artificiobattagin.it/?s=Liquitex&post_type=product`); la riga delle spedizioni intera sopra la piega. Entro due schermate: sei marche e il costo della spedizione. Tutte OK, e il tocco sprecato su "Tutta la settimana" non c'è più.
- Visitatore 2: "Cornici su misura" a 1.116 px su 390 (seconda schermata); nella sezione tre passi, WhatsApp con il messaggio già scritto, "Prezzo e tempi te li dice Matteo, guardando l'opera o la foto" e ora anche indirizzo, parcheggio e "Come arrivare" subito sotto i bottoni.
- Visitatore 3: "Corsi" nel menu e la porta "Corsi Artinpratica"; i tre corsi con data, titolo, docente, orari, posti e prezzo; "Iscriviti" alla pagina dell'evento; "Tutto il calendario" e la nota sul materiale.
- Per tutti: il tu ovunque; nessun popup; nessuno scorrimento orizzontale a 320, 360, 375, 390, 430, 600, 768, 1024, 1100, 1280, 1440, 1920, 2560.

### Controlli generali

- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440. A 1280 x 800 la ricerca dell'apertura scende appena sotto la piega (y 861), i bottoni restano sopra.
- Collegamenti: `tel:+390497811043`, `https://wa.me/393802308602` (anche con il testo per le cornici), `mailto:negozio@artificiobattagin.it`, una sola mappa (`google.com/maps/dir/` su "L'Artificio Battagin, Via della Croce Rossa 5/a, 35129 Padova"); il vecchio 049 8721644 non c'è.
- Nessun errore in console, nessun file mancante.
- Contrasti: grigio 7,1:1 sul bianco e 5,6:1 sulla parete; verde 7,3:1 sul bianco e 5,8:1 sulla parete; testo chiaro sul verde 6,1:1. L'oro non porta testo.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

Gambetta 400 e Switzer 400 e 600, Indian Type Foundry, da Fontshare, **ITF Free Font License** (uso commerciale libero, anche sul web; i file non si possono rivendere), serviti dalla pagina in `sito/fonts/` in woff2.

### Respinti o non applicati, apposta

- **La foto del reparto a tutta altezza in apertura** (correzione del controllore con `negozio-169-1000.jpg`): sarebbe ingrandita 1,44 volte. Al suo posto i cavalletti, l'unica foto loro a 2560 px; la fascia a tutta larghezza alta 420 px (l'alternativa) non lasciava posto ai bottoni nella prima schermata.
- **Togliere la riga delle spedizioni dall'apertura del telefono** (correzione del controllore): la SCHEDA chiede il costo della spedizione entro due schermate e la sezione Belle arti è alla quinta; la riga resta, intera sopra la piega grazie alla riga degli orari accorciata.
- **La parete che passa a un neutro**: la parete degli angolari è il loro colore e regge Cornici e Dove; l'oro entra solo come filetto.
- **WhatsApp con il numero sul telefono**: non ci sta nel bottone da 171 px.
- **WhatsApp con il messaggio pronto nella porta Cornici**: la porta è tutta un link alla sezione; un link dentro un link non è valido. Il messaggio pronto è nel bottone della sezione Cornici.
- **Le misure nel messaggio WhatsApp** ("larghezza x altezza in cm"): solo dopo che il negozio conferma che sono quelle che servono (LEGGIMI).
- **Una mappa statica** in "Orari e dove siamo": servirebbe un'immagine della mappa con licenza; resta il bottone "Indicazioni" (come Union).
- **Accorciare la pagina sul telefono**: non tolto nulla che serva ai compiti; la pagina è di 11.179 px come prima, con le news in una riga e i numeri in 2 x 2.

## Versione precedente: "Il miglior vestito" (terza versione, 2/11/2026)

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/` (sito e screenshot), prima del livello professionale.

Pagina: `sito/index.html` (6.018 px a 1440 con il piede, 7.360 px a 390). Rigenerazione: `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, prova del gesto con clic, tastiera e tocco, larghezze, collegamenti, segnali).

Questa versione rifinisce la seconda (stesso giorno) secondo il giudizio cieco (K0 7, K1 7, 59 su 80). L'idea resta quella: la loro frase è il quadro dentro la cornice. Cambia la proporzione della cornice, che ora è un quadro e non uno striscione, e la pagina si accorcia di un elenco.

## L'idea

La loro frase, "Ogni quadro ha bisogno del suo miglior vestito" (post "Laboratorio di cornici artigianali" del 30/03/2023), non sta accanto a una cornice: **è il quadro dentro la cornice**. Il titolo è stampato sul foglio, dentro un passepartout con la finestra tagliata a 45° (la loro particolarità, dalla pagina Cornici), e sul passepartout, in basso a destra e in piccolo come una firma a matita, c'è "Taglio a 45°, laboratorio di via della Croce Rossa". Si cambia profilo come in negozio: quattro angolari rivestono il titolo di netto. Il profilo di partenza è il rosso e oro della cornice che Matteo tiene in mano nella foto subito sotto: la prima e la seconda schermata si parlano, e con il nome di un altro corniciaio la pagina non regge (la firma e la cornice di Matteo sono solo loro).

## Cosa è cambiato rispetto alla seconda versione

1. **La cornice è un quadro in 4:3**: 860 x 640 px a 1440 (era 1.200 x 488, un rapporto da striscione), a filo del margine sinistro della testata (x 80). Titolo Gambetta 84 px su tre righe dentro la finestra ("Ogni quadro ha / bisogno del suo / miglior vestito"). A destra, nella colonna x 1004-1360, il mestiere, il testo, il telefono e i campioni, tutto entro i 900 px della prima schermata; sotto si vede l'inizio della foto di Matteo.
2. **La firma del laboratorio sul passepartout**: il legame con loro si vede senza leggere la didascalia. Sotto i 360 px resta solo "Taglio a 45°".
3. **Il mestiere in apertura**: la colonna si apre con "Negozio di belle arti con laboratorio di cornici, a Padova." in Gambetta 28 px (l'ATECO è 47.62.20, la cornice è uno dei reparti), poi "Colori, carte e pennelli per chi dipinge, disegna e incide. E un laboratorio interno dove tagliamo e assembliamo cornici su misura, in via della Croce Rossa 5/a."
4. **Tolto il laccato blu**: era un'estrusione sintetica di una sezione, si vedeva accanto all'oro e all'argento fotografati. Restano quattro profili, tutti ritagliati da foto loro.
5. **La parete degli angolari non è più ingrandita**: la sorgente è larga 1000 px e ora si mostra al massimo a 1000 px CSS, a filo del bordo destro; il titolo "Gli angolari campione, appesi in negozio" diventa la sua didascalia, a sinistra, ancorato alla base della foto.
6. **Le cinque vie in un paragrafo**: niente più elenco numerato. "Una famiglia amante dell'arte" è un titolo e un solo paragrafo in Gambetta 29 px con le vie nel testo, dalle parole della pagina Il negozio; "Dal 2007 siamo in via della Croce Rossa" in verde. Sparisce la voce vuota "In seguito, Via Cavalletto". Elenchi in pagina: tre (lavorazioni, reparti, calendario).
7. **La chiusura senza vuoto**: frase e recapiti sono un solo blocco centrato in verticale sulla foto, con il telefono a 48 px dalla frase. La foto è ritagliata solo sul legno (fuori i neon e il controsoffitto): il dettaglio della cassetta-cavalletto in faggio, con il leggio, i galletti in ottone e il cassetto a coda di rondine, alta 628 px a 1440.
8. **Matteo intero**: la foto è quasi quadrata (1080 x 1020), con tutta la cornice dentro e il banco dei listelli in basso a sinistra. A 1024 foto e titolo partono dalla stessa riga.
9. **Piede al telefono**: le voci delle colonne hanno un bersaglio di 39 px (padding 8 px sopra e sotto), 31 px sul computer.

## Rispetto alla campagna (richiesta del 2 novembre)

- **Niente legende sull'oggetto**: nessun pallino, nessun filetto numerato. Sotto i campioni una sola didascalia, il nome del profilo con una frase della pagina Cornici.
- **Il fondo viene dal mestiere**: il turchese della parete degli angolari del loro negozio, schiarito in #D9E8E4. La parete vera si vede dietro Matteo e nella foto degli angolari, con lo stesso colore: la pagina è il muro del laboratorio su cui la cornice è appesa. Il piede passa al bianco del passepartout (#F8F6F0).
- **Un'impaginazione che nella campagna non c'è**: il titolo sta **dentro** l'oggetto, come opera incorniciata, e l'oggetto è un quadro appeso a sinistra con una colonna stretta da cartellino di galleria a destra, invece del titolo a sinistra con l'oggetto scontornato a destra. Nel corpo, la parete degli angolari a filo del bordo destro con il titolo come didascalia, la storia in un solo paragrafo grande, il calendario a una riga per appuntamento a tutta larghezza.

## Prima schermata a 1440

- Testata: logo PNG a 120 px, cinque voci di menu, telefono.
- Cornice 860 x 640 (rosso e oro, listello 60 px); passepartout con margini 56, 56 e 76 px (più largo in basso, come si fa in bottega); finestra 628 x 388 con lo smusso chiaro in basso e a sinistra e in ombra in alto e a destra (luce dall'alto a destra, la stessa dei listelli); il foglio è un poco più caldo del passepartout.
- Titolo Gambetta 400 a 84 px, interlinea 1,02, spaziatura -0,022em, centrato su tre righe.
- Colonna a destra larga 356 px: mestiere in Gambetta 28 px, testo Switzer 17 px, bottone verde "Chiamate lo 049 7811043" (tel:) e "Shop online"; poi un filetto, "Provate un altro profilo sul titolo", i quattro campioni da 64 px e la didascalia, che finisce a 50 px sopra la base della cornice.
- Tecnica: la cornice è un `border-image` disegnato fuori dal passepartout (`border-image-outset`), con i quattro listelli tagliati a 45° e il tratto centrale ripetuto senza giunte (`round`). Cambiare profilo cambia solo il listello: finestra e titolo restano fermi al pixel (provato: h1 sempre in 216,298 con i quattro profili).
- A 1920 la tavola si ferma a 1.600 px: cornice 956 x 711, colonna da 396 px. Da 960 a 1199 la stessa composizione con la colonna più stretta e campioni da 54 px; da 700 a 959 la cornice va in tavola sopra (titolo su tre righe) e sotto il testo a sinistra e i campioni a destra.

## Prima schermata a 390

Testata con logo a 88 px, "Menu" e telefono; la cornice a tutta larghezza meno 16 px (listello a metà spessore), il titolo a 37 px su quattro righe dentro la finestra e la firma; poi i quattro campioni da 60 px, la didascalia, il mestiere, il testo e il bottone del telefono, tutto nella prima schermata da 844 px. A 320 il titolo scende a 28 px e la firma si accorcia.

## Caratteri e colori

- **Gambetta 400** (titoli, mestiere, storia, reparti, corsi, telefono grande), mai in corsivo; **Switzer 400 e 500** (testo, menu, didascalie, date e prezzi: le cifre di Switzer sono tabellari, tutte larghe 576 unità). Tutti e due di Indian Type Foundry, da Fontshare, **ITF Free Font License** (uso commerciale libero, anche sul web; i file non si possono rivendere), serviti da `sito/fonts/` in woff2.
- Perché: Gambetta è un serif da libro con grazie taglienti e occhio largo, vicino alle insegne serif dei corniciai storici (Bourlet, Lowy, Cornelissen) senza l'aria da moda di lusso; dentro la finestra sembra davvero un foglio stampato. Switzer è un grottesco neutro che non sta nelle liste della guida.
- Colori: muro #D9E8E4, passepartout #F8F6F0, foglio #F1EDE4, inchiostro #1F1B17 (13,5:1 sul muro), grigio #4A5553 (6,1:1 sul muro, 7,2:1 sul passepartout), verde Battagin #17633A (il verde di BATTAGIN nel logo, scurito: 5,8:1 sul muro, 6,7:1 sul passepartout; bianco sul verde 7,3:1). Contrasti AA per testo normale.
- Riferimenti: Bourlet (un solo angolo di cornice grande, frase serif, il verde), Arnold Wiggins (telefono e indirizzo in chiaro), Cornelissen (il negozio di colori raccontato come istituzione), Sennelier (un oggetto solo con molta aria).

## Interazione

"Provate un altro profilo sul titolo": quattro bottoni radio (rosso e oro, oro barocco, argento barocco, nero intagliato). Al clic o al tocco la cornice cambia di netto e la didascalia cambia frase (testi dalla pagina Cornici). Tastiera: frecce, Home e Fine, focus visibile verde; al telefono bottoni da 60 px. I listelli degli altri profili si caricano dopo la pagina, così il cambio è immediato. Nessuna animazione allo scorrere, niente effetti che seguono il cursore, nessuna dissolvenza.

## Foto, origine e licenza

Tutte le immagini sono dell'azienda, prese dal loro sito (servizio fotografico del 2023 e foto del 2023-2024); nessuna foto di repertorio, nessuna immagine generata dall'IA, nessuna usata in altre home della campagna.
- Listelli della cornice e campioni: ritagliati dalle loro foto. Rosso e oro: il lato alto della cornice di Matteo (`2023-05_339083708_...jpg`, raddrizzata di 28,2°); oro e argento barocco: i listelli sul banco (`2023-04_cornici-1.jpg`); nero intagliato: un angolare della parete nella foto di Matteo. È una composizione grafica, da sostituire con le scansioni vere (LEGGIMI).
- Matteo: `2023-05_339083708_...jpg`, 1080 x 1020. Parete degli angolari: `2023-05_cornici-per-grafica.jpg` intera, mostrata al massimo a 1000 px CSS. Cassetta-cavalletto: `2024-07_IMG_0393-scaled.jpg` (2560 px), solo la cassetta aperta, scontornata con ombra morbida sul colore del muro, al 54 % della larghezza. Matite: `2023-04_matite-1.jpg` (tagliata in alto a destra per togliere l'etichetta del marchio), a 1:1. Chiusura: `2023-07_IMG_7395-2-scaled.jpg` ritagliata a 1712 x 1307 dal basso a sinistra (solo il legno della cassetta-cavalletto).
- Esportate con PIL in più larghezze (srcset): 620-1440 px in JPEG qualità 80-84, listelli e campioni in WebP.

## Chiusura e piede

- Chiusura "b con foto", testo a sinistra e foto a destra fino al bordo: "Da sempre luogo dove si danno appuntamento artisti e appassionati d'arte" (descrizione della categoria Workshop del loro calendario) in Gambetta 60 px; a 48 px il 049 7811043 grande in verde (tel:), cellulare 380 2308602 (tel:), negozio@artificiobattagin.it (mailto:), Via della Croce Rossa 5/a con il link alla mappa, "Ampio parcheggio privato". Niente orari: non sono confermati.
- Piede sul bianco del passepartout: logo PNG a 125 px (2x) con una riga su chi sono; a destra la newsletter (sì: hanno clienti privati, 22 corsi nel 2026, promozioni e un articolo quasi ogni mese, e una newsletter ce l'hanno già) con campo, bottone verde e consenso; sotto quattro colonne: Negozio, Artinpratica, Contatti, Seguici (solo Instagram e Facebook, in parole); in fondo A.B. s.r.l., P.IVA 04191710286, REA PD 369492, Condizioni di vendita, Resi e rimborsi, Spedizioni e pagamenti, Privacy, Cookie. A 390 le colonne vanno a due a due. Il modulo non invia nulla finché non è collegato, e lo dice.

## Controlli (2/11/2026)

- Guardati a pezzi: 1440 (intera e prima schermata), 390 (intera e prima schermata), 320, 768, 960, 1024 (intera), 1920.
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 430, 600, 699, 700, 768, 900, 959, 960, 1024, 1099, 1100, 1199, 1200, 1280, 1440, 1600, 1920 e 2560 (`_prova/script/controlli_finali.mjs`).
- Gesto: clic sui quattro profili, frecce, Fine, Home a 1440 (`prova_gesto.mjs`) e tocco a 390: cornice, radio e didascalia corrette, h1 fermo, nessun errore in console, nessun file mancante. Menu del telefono: si apre e aria-expanded passa a true.
- Collegamenti: tel:+390497811043, tel:+393802308602, mailto:negozio@artificiobattagin.it, la mappa di Google su "Via della Croce Rossa 5/a, 35129 Padova".
- `_metodo/kit/segnali.sh` a 1440: 17 soglie su 18 a posto. L'unica segnata è l'area coperta da foto, 34,2 % contro 35 %: lo strumento conta solo `img` e sfondi, non il `border-image` della cornice d'apertura, che è fatta di listelli fotografati e copre 860 x 640 px; contandola si arriva a circa 40 %. Non è un segnale vero: la pagina ha sei foto loro più la cornice. Switzer 73 %, Gambetta 27 %; 4 misure di H2; 2 fasce (il muro e il piede); 16 filetti larghi; nessuna freccia, nessuna etichetta maiuscola, nessuna numerazione.
- Nessun carattere U+2014 nella pagina, nella NOTA, nel LEGGIMI e nei CREDITI.
- Dati: tutti da `01-analisi.md` e dal crawl (`il-negozio/`, `cornici/`, `belle-arti/`, `contatti/`, `events.json`, piede del sito). Lo sconto del 15 %, gli orari, il capitale sociale e la PEC restano fuori dalla pagina e sono nel LEGGIMI.
