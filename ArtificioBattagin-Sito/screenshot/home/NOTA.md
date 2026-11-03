# L'Artificio Battagin, home

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///; 8.203 px a 1440, 11.168 px a 390). La home di prima (cornice d'apertura con il titolo dentro) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot). Per questa azienda non c'era una "versione 1 con l'uso": l'uso viene direttamente dalla scheda `_prova/uso/SCHEDA.md`, che è stata seguita punto per punto.

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (in due fogli), le pagine intere di Union e Joseph Brot a pezzi, il foglio `_invio/zona/home/livello-professionale.jpg` e le note di Unicar e Panificio Fornasiero.

Rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche `sito/img/` con `pro_img.py`); dentro ci sono gli screenshot (`pro_shoot.mjs`, JPEG senza PNG temporanei) e i controlli (`pro_controlli.mjs`). Elementi che escono a destra: `node _prova/script/pro_largo.mjs <index.html> <larghezza>`. Pagina lunga in colonne per guardarla: `python3 -I _prova/script/pro_mosaico.py`.

Screenshot (stessi nomi di prima): `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove siamo" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e interi a 320, 768, 1024, prima schermata a 1920.

### Che cosa è cambiato, in breve

- **Il negozio torna al centro.** Il titolo dice il mestiere e il luogo: "NEGOZIO DI BELLE ARTI A PADOVA", in maiuscolo come i titoli della famiglia B (Gambetta 88 px a 1440, 40 px a 390). L'occhiello è la prova: "Dagli anni '70 · 1000 mq in via della Croce Rossa". Sotto, una riga con i reparti, le cornici, i corsi e il loro claim "Per i professionisti e gli amanti dell'arte".
- **Il titolo di prima resta, al suo posto.** "Ogni quadro ha bisogno del suo miglior vestito" (post del 30/03/2023) è il titolo della sezione Cornici. In apertura diceva solo un reparto: la scheda lo segna come il primo difetto ("il negozio sparisce").
- **La prima schermata fa i compiti della scheda** (390x844, senza scorrere): testata con logo, "049 7811043" e Menu; la striscia della foto vera degli scaffali; titolo; "Orari di oggi" con il link agli orari della settimana; Chiama 049 7811043 a tutta larghezza; WhatsApp e Come arrivare affiancati; "Via della Croce Rossa 5/a · parcheggio privato"; il campo "Cerca marca o prodotto" che apre i risultati dello shop. A 1440 le stesse cose in due colonne con la foto del reparto a destra (608x456, sorgente 749 px).
- **Struttura della famiglia B adattata**: testata con "Orari e dove siamo" come prima voce; apertura; tre porte con foto loro (Belle arti, Cornici su misura, Corsi Artinpratica); manifesto e sei numeri su blocco verde; Belle arti con reparti e marche, la fascia delle marche in grande, ricerca e spedizioni; Cornici su misura su fondo parete, con Matteo e tre passi; i prossimi corsi con "Iscriviti" e le ultime tre news; Chi siamo con le cinque sedi; "Orari e dove siamo" con la scheda del negozio e il modulo "Scrivici" (tipo di richiesta); piede in quattro colonne.
- **Tolto**: la cornice disegnata con i listelli ritagliati, i quattro profili del gesto, la firma sul passepartout, la cassetta-cavalletto scontornata sul colore del muro, il fondo turchese su tutta la pagina, la newsletter nel piede (non inviava nulla; in pagina resta un solo modulo).

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs`, 62 su 62, e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata `sticky`; a 390, a metà pagina, il bottone "049 7811043" è a 12 px dall'alto, alto 48 px, e si tocca; da 400 px dice "Chiama 049 7811043". "Orari e dove siamo" è la prima voce del menu (famiglia B). 5 link `tel:` (tutti allo 049 7811043).
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Mestiere e luogo nel titolo, prova nell'occhiello (anni '70, 1000 mq), "Chiama 049 7811043" pieno; a 390 a tutta larghezza (350 su 350 px).
3. **Immagine vera nell'apertura**: PASSA. Il reparto belle arti con gli scaffali pieni sul pavimento blu (`2023-05_negozio-bellearti-2.jpg`, servizio fotografico del 2023): a 1440 in 4:3 a 608 px (sorgente 749 px, mai ingrandita), a 390 in striscia sotto la testata.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da Unsplash o Pexels; nessuna illustrazione.
5. **Foto in serie**: PASSA. Otto foto, tutte dello stesso servizio del 2023 (stessa luce di vetrata, grandangolo, il pavimento blu che torna); due formati in pagina (4:3 e 16:9, più la striscia dell'apertura sul telefono); una didascalia sola (Matteo) su otto foto.
6. **Palette dal marchio**: PASSA. Due colori: il verde di BATTAGIN nel logo (#17633A) per bottoni, link, blocco dei numeri; il turchese della parete degli angolari (#D9E8E4) per Cornici e "Orari e dove siamo". Neutri: bianco, inchiostro #1F1B17, grigio #505A58, grigio chiarissimo del modulo. Niente beige: il fondo è bianco.
7. **Scala corta e leggibile**: PASSA. 1440: 88, 56, 32, 24, 19, 16, 14 px (7 misure); 390: 40, 32, 24, 17, 16, 14 (6). Testo corrente 19 px a 1440 e 17 a 390; i 14 px solo nella riga legale; titolo 88 px maiuscolo, interlinea 0,98.
8. **Due famiglie**: PASSA. Gambetta 400 (titoli, numeri, date dei corsi, prezzi, marche) e Switzer 400 e 600 (testo, etichette, bottoni, modulo). Il 500 di prima è diventato 600, per due pesi distanti.
9. **Servizi in schede con foto**: PASSA. Tre porte in tre colonne da 760 px (sul telefono righe con la miniatura 4:3 a sinistra), foto 4:3 per tutte (matite numerate, parete degli angolari, spazio Artinpratica), nome, riga utile e link; tutta la scheda è un link alla sua sezione.
10. **Almeno tre tipi di prove**: PASSA IN PARTE (2 su 4). Ci sono sei numeri veri (1000 mq, anni '70, 5 sedi, oltre 20 anni di Matteo, 22 corsi nel 2026, spedizione gratis oltre 79 euro) e la fascia dei fornitori con la didascalia ("Alcune delle marche che trovi in negozio", 14 marche in Gambetta 56 px, che è anche il gesto di scala della pagina). Recensioni: le 689 recensioni Google (media 4,5) e le frasi dei clienti vengono da un sito terzo (itaglietti.it) e la scheda dice di usarle solo con fonte verificata: non sono in pagina, vanno verificate sul profilo Google con nome del cliente (LEGGIMI). Clienti con il nome e certificazioni: non ne hanno, è un negozio al dettaglio.
11. **Lavori con un nome**: NON SI APPLICA (negozio al banco, nessuna commessa nelle fonti). Il posto va ai corsi con data, docente e prezzo, e alla storia delle cinque sedi.
12. **Ritmo a blocchi**: PASSA. Tre blocchi pieni oltre al piede (numeri sul verde, Cornici e "Orari e dove siamo" sulla parete); spazi tra le sezioni 128 px a 1440 e 64 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno verde e con il bordo verde, raggio 4 px, alti 52 px (48 in testata e nelle scelte del modulo), testo Switzer 600 16 px; i quattro bottoni di chiamata hanno il numero. Il bottone "Cerca" non è più incollato al campo (aveva un raggio diverso).
14. **Modulo e "dove e quando"**: PASSA, con un limite. Modulo in home con "Che cosa ti serve?" (Un prodotto, Una cornice su misura, Un corso, Altro), nome, telefono, email e messaggio: compone un'email a negozio@artificiobattagin.it con oggetto "Dal sito: <tipo>, <nome>" (da collegare a un servizio, LEGGIMI). La scheda del negozio ha "Indicazioni" (Google Maps, percorso), Chiama, WhatsApp, email, parcheggio, ingresso accessibile. Nessun iframe. **Limite**: la tabella degli orari è pronta nello script (`ORARI`, provata con dati di prova: martedì alle 10 "Aperto ora, fino alle 12.30", sette righe con oggi in grassetto) ma resta vuota perché gli orari non sono pubblicati; finché mancano la pagina dice di chiamare o scrivere su WhatsApp.
15. **Piede completo**: PASSA. Logo, claim, A.B. s.r.l., P.IVA 04191710286, REA PD 369492; Negozio, Artinpratica (con Instagram e Facebook), Contatti (telefono, WhatsApp, email e indirizzo cliccabili, link agli orari); cinque link legali; quattro colonne a 1440, testo di almeno 14 px. Certificazioni: non ne hanno.

### Uso: le prove della scheda

- Visitatore 1 (390x844, senza scorrere): "belle arti" e "Padova" nel titolo; posto degli orari di oggi con link alla settimana; `tel:+390497811043` alto 48 px; `https://wa.me/393802308602`; la mappa e "parcheggio privato"; il campo di ricerca. "Liquitex" nel campo porta a `https://artificiobattagin.it/?s=Liquitex&post_type=product`. Entro due schermate: sei marche (scheda Belle arti) e "spedizione 10 €, gratis oltre 79 €" (sotto la ricerca). Tutte OK.
- Visitatore 2: "Cornici su misura" a 1.141 px su 390 (seconda schermata); nella sezione tre passi, WhatsApp con il messaggio già scritto ("Ciao, vorrei una cornice su misura..."), nessun prezzo o tempo inventato e "Prezzo e tempi te li dice Matteo, guardando l'opera o la foto".
- Visitatore 3: "Corsi" nel menu a 1440 (e nel Menu a 390, e la porta "Corsi Artinpratica"); i tre corsi letti dal calendario del sito il 3/11/2026 (`_prova/crawl/eventi-2026-11-03.json`) con data, titolo, docente, orari, posti, materiale e prezzo; "Iscriviti" porta alla pagina dell'evento con il ticket; "Tutto il calendario" e "Il materiale che serve per i corsi lo trovi in negozio".
- Per tutti: il tu ovunque, nessun "Chiamate", "Provate", "troverete"; nessun popup; nessuno scorrimento orizzontale a 320, 360, 375, 390, 430, 600, 768, 1024, 1100, 1280, 1440, 1920, 2560.

### Controlli generali

- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1440, 1920. Corretti durante il lavoro: il bottone Menu che usciva di 7 px a 375 e 390 (ora "Chiama" accanto al numero compare da 400 px), la colonna Contatti del piede a 360 (ora a tutta larghezza sotto i 760 px), la griglia dell'apertura e quella dello shop a 320, il calendario a quattro colonne troppo stretto a 768 (ora da 1000 px), il suggerimento del campo di ricerca tagliato a 390 (sotto i 430 px diventa "Cerca marca o prodotto").
- Collegamenti: `tel:+390497811043`, `https://wa.me/393802308602` (anche con il testo per le cornici), `mailto:negozio@artificiobattagin.it`, una sola mappa (`google.com/maps/dir/` su "L'Artificio Battagin, Via della Croce Rossa 5/a, 35129 Padova"); il vecchio 049 8721644 non c'è. Le pagine del sito puntano a `https://artificiobattagin.it/...` (indirizzi di oggi), così funzionano anche da file:///.
- Nessun errore in console, nessun file mancante (tolti i preload dei caratteri, che da file:/// fallivano per il crossorigin).
- Contrasti: grigio 7,1:1 sul bianco e 5,6:1 sulla parete; verde 7,3:1 sul bianco e 5,8:1 sulla parete; testo chiaro sul verde 6,1:1.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Gambetta 400 e Switzer 400 e 600, Indian Type Foundry, da Fontshare, **ITF Free Font License** (uso commerciale libero, anche sul web; i file non si possono rivendere), serviti dalla pagina in `sito/fonts/` in woff2. Switzer 600 scaricato il 3/11/2026 da Fontshare (copia in `assets/fonts-scaricati/`).

### Respinti o non applicati, apposta

- Apertura a tutto schermo con la foto (famiglia B, punto 2): le foto del servizio 2023 sono online a 1000 px; a tutta pagina a 1440 sarebbero ingrandite. Restano a 608 px (sorgente 749) e in striscia sul telefono.
- Facciata del negozio nella scheda: non c'è una foto della facciata; al suo posto l'open space con le tele.
- Recensioni con nome: vedi regola 10.
- Novità con foto: le foto dei post sono still life di marche altrui o locandine; restano tre titoli con la data.
- Newsletter: tolta dal piede (un solo modulo in pagina; il popup del 15% va confermato, LEGGIMI).

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
