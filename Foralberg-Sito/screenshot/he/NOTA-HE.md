# Foralberg, home HE (5 novembre 2026)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), caratteri in `sito-he/fonts/`, immagini WebP in `sito-he/img/`. La `sito/` di oggi non è toccata. Direzione artistica: `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8731`, ora simulata martedì 3/11/2026 alle 10.00 con `?ora=2026-11-03T10:00`), `foglio-1440.jpg` (37 fotogrammi) e `foglio-390.jpg` (34), i fotogrammi uno al secondo, `prima-schermata-1440.jpg` e `-390.jpg`, `riduci-movimento-1440-prima-schermata.jpg` e `-390`. Pagine intere ferme e prime schermate a 768, 1024 e 1920 in `_prova/he/prove/`; script delle prove e delle immagini in `_prova/he/script/`.

## Idea

**Firmato Foralberg.** La firma corsiva del logo di oggi è la stessa dipinta a mano sul cassone dell'OM Lupetto 30 delle prime consegne, e sulla portiera dello stesso furgone ci sono già i capitoli del catalogo: "porcellane, cristallerie, posaterie, art. vari cucina". La pagina segue la firma: si scrive nel sipario, è dipinta sul furgone che riempie la pagina, dà il titolo all'indice del catalogo, torna enorme nel culmine e passa al cliente, perché Foralberg personalizza i piatti con il marchio del locale ("Il tuo biglietto da visita? Un piatto su misura.", catalogo p. 103).

## Riferimenti

Schermate a 1440 (prima schermata e tre scorrimenti) in `_prova/he/riferimenti/`: Puiforcat, Christofle, Bernardaud, Alessi (tavola e ospitalità); Kevala Ceramics (Menzione d'onore Awwwards, 22/2/2024) e The Olly (Menzione d'onore, 12/9/2024). Mosse prese, due per sito, in `DIREZIONE-HE.md`. Non raggiungibili oggi: Sambonet (500 e 502), Ginori 1735 (403 anti-robot), Rosenthal (500), Jars (rimanda a Google), awwwards.com (502).

## Carattere

- **Jost** (Indestructible Type, Google Fonts, SIL OFL 1.1, `fonts/OFL-Jost.txt`), 400 e 500: titoli, cifre, righe dell'indice, bottoni, menu. È il geometrico delle scritte dipinte sugli stand Foralberg in fiera ("pirofile - porcellane / cristallerie - posaterie" sulla XXXVI, "PADOVA VIA S. FERMO-16" sulla 38a).
- **Source Serif 4** (Adobe, Google Fonts, SIL OFL 1.1, `fonts/OFL-SourceSerif4.txt`), 400 e 600 con l'asse ottico: testo, didascalie, orari.
- La firma è sempre il disegno vettoriale del logo (tracciati del catalogo), mai un carattere. Niente corsivi, niente maiuscolo spaziato.
- Registro: riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (Jost: 2 home su 45 con Lab247, altra zona; Source Serif 4: nessuna).

## Colore

Porcellana #F4F3EF (fondo), inchiostro #131415 (16,6:1; sipario, progetti, piede), blu Foralberg #0082B9 della copertina, pieno a #00719F (bianco 5,4:1) **solo sulla sezione firma**, acciaio #5D6166 (5,6:1) per testo secondario e filetti, #A7ACB1 sul nero, verde #1C7A3D solo per "Aperto ora". Foto: archivio in bianco e nero neutro (neri 20, luci 244), catalogo a colore smorzato (saturazione 0,84, neri alzati a 16), grana del kit su tutte le cornici.

## Movimento

- **Gesto d'apertura, "la firma, poi il furgone"**: sipario nero (`data-he-intro`, una volta per visita) in cui la firma bianca si scrive da sinistra a destra in 0,78 s (taglio CSS sincronizzato con il tempo del kit); il sipario sale, il titolo sale riga per riga (`data-he-split data-he-subito`), il furgone è incorniciato sulla cabina con la portiera "porcellane, cristallerie, posaterie, art. vari cucina" e scorrendo si allarga a tutta pagina (`data-he-scale`, fissato per 110 % di altezza) fino a mostrare la firma sul cassone; entra la didascalia (`data-he-scale-entra`). Il testo dell'apertura esce nel primo terzo dello scorrimento con una tween della pagina (GSAP del kit, `start: 0`, fine a 0,36 altezze), così non si sovrappone alla foto che cresce.
- **Sostegno**: titoli riga per riga su tre testi (apertura, chi siamo, culmine); indice con anteprima ferma (`data-he-index`, sopra i 900 px); storia con la foto ferma (`data-he-story`, sei date). Testata che si nasconde scendendo (`data-he-header`).
- Nessuna parallasse, taglio, nastro o galleria orizzontale.
- **Riduci movimento** (provato con `reducedMotion: 'reduce'`): niente sipario, apertura ferma con il furgone incorniciato e la didascalia sotto, storia come serie di sei stampe con le date sotto, tutto il resto uguale. Pagina completa a 390, 768, 1024, 1440, 1920.
- Sotto i 900 px: nessuna sezione fissata; l'apertura è titolo, foto 3:2, didascalia, testo, "Chiama 049 760955"; l'indice ha una miniatura per riga e non carica le anteprime grandi; la storia mette ogni stampa sopra la sua data.

## Sezioni (scheletri diversi)

1. **Apertura**: titolo a 147 px a tutta larghezza, a sinistra la riga sul mestiere, "Chiedete un preventivo", "Il catalogo 2026/2027" e le due sedi con lo stato; a destra la cornice sul furgone che diventa la pagina.
2. **Chi siamo**: la frase "Dal 1953 consulenti dell'ospitalità. Ci piace pensare di essere più di un semplice fornitore." su sette colonne, testo spostato di una colonna, foto alta e stretta (catalogo p. 4) più in basso a destra; quattro cifre su filetto nero (800 m², 30.000, 6.000, 11).
3. **Indice del catalogo**: titolo con le quattro voci della portiera in minuscolo; 14 righe come l'indice di un libro (capitolo, marchi, pagina del PDF), anteprima ferma a destra; marchi trattati, Disponibilità e Campionatura verso il modulo.
4. **Progetti e impianti** (inchiostro): i quattro tempi del catalogo a gradini, ogni tempo due colonne più a destra; che cosa guardiamo; "Mandaci la planimetria" e il telefono.
5. **Storia**: 1953, 1960, 1962, 1963, 1964, Oggi; anni a 104 px, stampe d'archivio intere su carta.
6. **Sezione firma, culmine** (blu pieno): la firma bianca larga 1296 px; "Nel 1963 la nostra firma viaggiava sul cassone del Lupetto. Sui vostri piatti può stare la vostra."; il piatto su marmo (catalogo p. 8) e "Il tuo biglietto da visita? Un piatto su misura." a 72 px con le tecniche e il link a p. 103.
7. **Showroom e orari**: "via Cile 2" e "via Vigonovese 93" a 104 px (link alle indicazioni), sotto in tre colonne chi è, stato, orari con la riga di oggi, Chiama, Indicazioni, tangenziale, shop online, lista nozze, Facebook.
8. **Richiesta**: il modulo della versione professionale con le stesse funzioni (tipo, settore, area, campi del progetto, allegato, email composta, testo da copiare), recapiti a sinistra.
9. **Acquisti PA**: sei portali in griglia, la frase sull'abilitazione, "Chiedete l'abilitazione".
10. **Piede** (inchiostro): logo bianco, ragione sociale, P.IVA, indirizzo, orari, telefoni ed email, LinkedIn, Facebook di La Vetrinetta, Lavora con noi, Privacy, Cookie, Note legali.

Funzioni mantenute: 12 link `tel:` (049 760955 in testata sempre, 335 142 6521, 049 8700975), 6 `mailto:`, 4 link alle indicazioni su Google Maps, 18 link ai PDF (catalogo 2026/2027 alla pagina del capitolo e Buffet 2025, col peso scritto), stato aperto o chiuso sull'ora di Roma con i festivi, La Vetrinetta (testata, apertura, sezione dove, modulo con "Privato", piede), dati legali, Privacy e Cookie, JSON-LD dei due negozi.

## Foto usate

| In pagina | File originale (in `assets/originali/`, fuori da git) | Native | Mostrata a 1440 |
|---|---|---|---|
| Apertura, il furgone | `storia_camion2_foralberg.jpg`, foralberg.it/it/company | 4205x3208 | 1440 (file 1920 e 2560 per gli schermi densi) |
| Storia 1963, la firma sul cassone | stesso file, ritaglio | 1670x940 | 746 |
| Storia 1953, stand XXXVI Fiera | `storia_fiera_1954_foralberg.jpg` | 4857x2662 | 746 |
| Storia 1960, stand 38a Fiera | `storia_fiera_1_foralberg.jpg` | 4059x3012 | 746 |
| Storia 1962, via San Fermo | `storia_via_san__fermo.jpg` (cartolina) | 1000x705 | 746 |
| Storia 1964, stand 42a Fiera | `storia_fiera_2_foralberg.jpg` | 4088x2943 | 746 |
| Storia oggi, copertina 2026/2027 | `00__FB_CP25__COMPLETO__LowRes-1.jpg`, it/cataloghi | 2480x3507 | 441 |
| Chi siamo, piatto ovale verde | Catalogo 2026/2027 p. 4 (pdfimages) | 1660x2345 | 416 |
| Culmine, piatto bianco su marmo | Catalogo p. 8, ritaglio quadrato | 1660x1660 | 526 |
| Indice, 14 anteprime 4:5 | Catalogo pp. 91, 103, 182, 232, 290, 352, 391, 400, 412, 448, 464, 470, 494, 498 | da 1030 a 2369 px di lato | 526 |

Riscaricati anche, e non usati: le sei foto dello slider della home (1400x500, dei fornitori), i blocchi 800x400, le copertine degli altri cataloghi, i sei banner di La Vetrinetta (1920x700, con scritte e marchi altrui; le miniature dei prodotti dello shop escono solo a 160 px). Il PDF del catalogo (56 MB) è in `assets/originali/catalogo/` con le foto estratte. Nessuna foto di repertorio, nessuna immagine generata. Tutte sotto 1,25 volte la loro larghezza nativa.

**Foto da rifare, in ordine di valore**:
1. Un piatto bianco personalizzato con il marchio di un cliente vero, dall'alto, in luce naturale: sostituisce il piatto del catalogo nel culmine ed è la prova dell'idea (la firma che passa al cliente).
2. Lo showroom di via Cile, frontale come gli stand in fiera: per "Oggi" nella storia, al posto della copertina, e per la sezione dove.
3. Una tavola apparecchiata nello showroom, stessa luce: per "chi siamo", al posto della p. 4.
4. Le persone (servizio clienti, progettista sul disegno, agente al banco), il magazzino dei 6.000 articoli in pronta consegna, un furgone di oggi con la firma se c'è, la facciata di La Vetrinetta, una cucina consegnata con il nome del locale.
5. L'archivio in scansione a 1200 dpi con il retro delle stampe, per fissare gli anni.

## Misure

- Caratteri a 1440: 147 (titolo), 104 (anni, indirizzi), 72 (culmine), 63 (titoli di sezione), 36 (righe dell'indice, tempi), 24, 19 (testo), 16, 14. A 390: 57, 46, 35, 25, 22, 19, 17 (testo), 16, 14.
- Margini 72 px a 1440 (5 vw), 20 a 390; canalino 24; respiro tra le sezioni 158 px a 1440, 88 a 390.
- Altezza: 15.625 px a 1440 (con i 990 px dell'apertura fissata), 16.721 a 390.
- Peso al primo caricamento (rete a riposo, misurato in Playwright): 1,14 MB a 1440 (soglia 2,5), 0,55 MB a 390 (soglia 1,5). Foto d'apertura precaricata con `imagesrcset`, carattere Jost precaricato; tutte le immagini hanno larghezza e altezza.
- Prove: nessuno scorrimento orizzontale e nessun errore di script a 390, 768, 1024, 1440, 1920, con e senza riduci movimento; titoli e testo dell'apertura controllati anche a 1366x768 (regola per gli schermi bassi). Nessun carattere U+2014 nella pagina, nella direzione e in questa nota.

## Autovalutazione da direttore creativo

Design 8, creatività 8,5, usabilità 8, contenuto 8,5: media pesata 8,2. Metà della distanza da un 9 dipende dalle foto: il presente è raccontato con le foto del catalogo (di bella qualità ma dei fornitori, con luci diverse) e non con lo showroom, le persone e un piatto personalizzato vero.

## Problemi aperti

- **Foto del presente**: vedi sopra. Le foto del catalogo sono quelle che Foralberg pubblica, ma molte vengono dai fornitori: chiedere se si possono usare sul sito.
- **Diritti dell'archivio** ("Foto Giordani") e originali a piena risoluzione.
- **Date**: la 36a Fiera non ha anno in pagina (1953 sul sito, 1958 nel catalogo); il furgone è nella riga del tempo al 1963 ma porta "via Trieste 11"; restano da confermare come in `01-analisi.md`.
- **Modulo**: come nella versione professionale compone un'email e mostra il testo da copiare; va collegato a un servizio che riceva anche i file (LEGGIMI).
- **Link legali**: puntano alle pagine di oggi su foralberg.it (Privacy, Cookie, Note legali, Lavora con noi); nel sito nuovo vanno rifatte, e le Note legali di oggi citano ancora "Selco".
- **Catalogo da 56 MB**: ogni riga apre il PDF alla pagina giusta, ma sul telefono è pesante; meglio un PDF per capitolo.
- **Sipario**: ritarda la pagina di circa 1,7 s alla prima visita della sessione; se il committente lo trova lungo, si toglie senza toccare il resto (la firma resta nel culmine).
- **Due blu vicini**: l'ultima data della storia mostra la copertina blu subito prima della sezione blu; è voluto (la firma piccola della copertina diventa quella grande), ma con una foto dello showroom al posto della copertina il culmine guadagna sorpresa.
- **Numeri**: "11 agenti e commerciali" e "oltre 30.000 articoli" sono del sito e del catalogo; Atoka e LinkedIn danno cifre diverse (LEGGIMI).
- **Righe senza marchio** nell'indice (Melamina, Pasticceria, Pizzeria, Stoccaggio, Piccoli macchinari): i marchi vanno chiesti all'azienda, non inventati.
