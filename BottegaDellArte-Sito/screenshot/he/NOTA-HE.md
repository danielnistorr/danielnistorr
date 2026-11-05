# Bottega dell'Arte: home HE, nota

Pagina: `sito-he/index.html` (5 novembre 2026), con il kit in `sito-he/kit/` (he.css, he.js, vendor/), le immagini in `sito-he/img/` (WebP in più larghezze), i caratteri in `sito-he/fonts/` con le licenze. La versione professionale `sito/` non è stata toccata. Direzione scritta prima del codice in `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (il film dello scorrimento, `_metodo/highend/kit/registra.mjs`), `foglio-1440.jpg` e `foglio-390.jpg` (i fotogrammi, uno al secondo), `fotogrammi-1440-NN.jpg` e `fotogrammi-390-NN.jpg`, le prime schermate ferme `prima-schermata-1440.jpg`, `prima-schermata-390.jpg` e le stesse con "riduci movimento" (`-fermo`).

Rifare: `python3 -m http.server 8765` dalla radice del repository, poi `node _metodo/highend/kit/registra.mjs http://127.0.0.1:8765/BottegaDellArte-Sito/sito-he/index.html BottegaDellArte-Sito/screenshot/he 1440 900` e lo stesso con `390 844`. Immagini: `python3 -I _prova/he/he_img.py assets/originali _prova/he/lavorazione sito-he/img`. Prove di larghezza, errori e peso: `node _prova/he/prova.mjs <url> <cartella> <larghezza> <altezza> moto|fermo`.

## Idea

**"In stile o moderni."** È il loro titolo di oggi ("arredamenti su misura, in stile o moderni"), detto a 216 px. La pagina mette accanto le due mani del mestiere: il pezzo nuovo e il pezzo restaurato. Il culmine è il Bo, dove il restauro tocca le porte e le pareti che portano la firma di Gio Ponti.

Il gesto d'apertura parte dall'ottone. La nicchia del sottoscala sta incorniciata come una fessura d'oro tra "In stile" (in alto a sinistra) e "o moderni." (in basso a destra). Scorrendo, la cornice si apre su tutta la stanza: le otto ante a push sotto la scala in ferro battuto, cioè "in stile e moderni" nella stessa foto.

## Riferimenti

Guardati a 1440 (prima schermata e tre passi di scorrimento) in `_prova/he/riferimenti/`. Del settore: Molteni&C, Minotti, Porro, Salvatori, Poliform e Henrytimi. Premiati su Awwwards: Schreinerei Siegesmund e Hays Woodworking. Le due mosse prese da ciascuno sono in `DIREZIONE-HE.md`, sezione 2. In pagina si vedono soprattutto queste:
- Molteni: foto medie fuori asse, numerate tra parentesi da (01) a (10), con la didascalia doppia (lavoro in nero, materiale o categoria in grigio);
- Porro e Hays: i mestieri come indice di righe enormi in serif, con l'anteprima che cambia;
- Salvatori: la frase sola nel vuoto, cioè il manifesto della bottega, e la didascalia che nomina il materiale;
- Henrytimi: il rettangolo d'immagine piccolo al centro, prima che si allarghi;
- Siegesmund: l'idea "moderno fatto come una volta", detta qui con le loro parole, e la galleria di tanti lavori;
- Minotti: un'unica pagina intera, il sottoscala, con il titolo corto sopra.

## Carattere

- **Gloock 400** (Duarte Pires, Google Fonts, SIL OFL 1.1) per il titolo, il titolo del Bo, le righe dell'indice, "Prima" e "dopo", gli `h2`, il telefono della chiusura e la didascalia d'apertura.
- **Satoshi 400, 500, 700** (Indian Type Foundry, Fontshare, ITF Free Font License 2.0) per il manifesto, il testo, l'interfaccia, le didascalie e il modulo.
- I file sono in locale (`fonts/gloock-latin*.woff2`, `fonts/satoshi-*.woff2`), con `OFL-Gloock.txt` e `FFL-Satoshi.txt`. La FFL ammette il self-hosting per il proprio sito.
- Nessuna delle due famiglie è usata in un'altra home della cartella. Riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.
- Il manifesto è passato da Gloock a Satoshi 400 dopo il primo giro: in Gloock, sette righe a 52 px facevano un blocco troppo nero.

## Colore

Carta #F1ECE3, inchiostro #16120E, noce #2A1D14 (solo la sezione del Bo, l'unica a colore pieno), ottone #B48C3C (cifre e filetti sul noce, 5,3:1), ottone scuro #7C5A1C (link e numeri sulla carta, 5,4:1), rovere #CBB28A (fondi delle foto, testi secondari sul noce, 8:1), ferro #4B4741 (testi secondari, 7,8:1).

Niente gradienti, salvo una velatura scura in fondo alla foto d'apertura sotto la didascalia bianca. Niente ombre, angoli tondi o vetro. Sulle foto un solo trattamento (`he_img.py`): neri un poco sollevati, colore all'86 per cento, appena più caldo. Sopra, la grana del kit (`he-grana`).

## Movimento

- **Apertura:** `data-he-scale` con la cornice `inset(41% 36.8% 28% 17.4%)` sulla nicchia e `data-he-split data-he-subito` sul titolo. Titolo, testo e didascalia piccola escono con `data-he-scale-via`; la didascalia grande entra con `data-he-scale-entra` ("Otto ante con apertura a push e una nicchia centrale in ottone..."). La sezione resta fissata per il 110 per cento di un'altezza di schermo. Sotto i 900 px non è fissata: la foto, un taglio verticale sulla nicchia, si assesta piano.
- **Sostegno 1:** prima e dopo del portone (`data-he-compare`), con il cursore a metà. Le due foto del sito, una con la porta sdraiata e una in piedi, sono raddrizzate in prospettiva sulla stessa cornice del pannello (`_prova/he/lavorazione/`). Coincidono pannelli, serratura e fori della vecchia maniglia. Una riga lo dichiara sotto la porta.
- **Sostegno 2:** il Bo in quattro passi (`data-he-story`): la foto ferma a sinistra cambia mentre il testo scorre. Il titolo del passo attivo è color carta, gli altri color rovere.
- **Sostegno 3:** sette lavori in galleria orizzontale fissata (`data-he-horizontal`), con la barra d'avanzamento in ottone. Il titolo resta fermo sopra. Sul telefono la fila si sfoglia con il dito e si ferma su ogni pezzo.
- Sempre: testata che si nasconde scendendo e torna con il fondo carta. Indice dei mestieri con l'anteprima ferma (`data-he-index`), solo come comando d'uso. `data-he-split` su tre testi: titolo, manifesto, titolo del Bo.
- **Riduci movimento**, provato con `emulateMedia` (`reducedMotion: 'reduce'`) a 390, 768, 1024, 1440 e 1920: la pagina è ferma e completa. L'apertura resta nella composizione incorniciata con la didascalia "(01)". Il Bo mostra la foto di ogni passo su due colonne (una sola sul telefono). La galleria scorre di lato con la barra del browser. Prima e dopo e indice funzionano.

## Sezioni (scheletri diversi)

1. **Apertura** fissata: titolo in diagonale, la fessura d'ottone in mezzo, testo e comandi in alto a destra (mestiere, "Chiama 049 900 4916", "Chiedi un preventivo", "Via Levico 18, Mestrino: indicazioni"). Si apre sulla stanza intera.
2. **La bottega:** il manifesto su nove colonne (Mauro Nosarini e Giuliano Saibene, cominciati da ragazzini in una falegnameria artigiana di Padova; disegni di architetti o schizzi, o progetto da zero). Sotto, tre fatti in colonna (laboratorio, posa, finiture) e fuori asse la foto (02) del laboratorio.
3. **Indice dei mestieri:** Arredo su misura, Serramenti e porte, Restauro, Negozi e locali, a 92 px, ognuno con l'elenco delle cose che fanno e il link alla sua pagina. A destra l'anteprima 4:5 ferma; sul telefono ogni riga ha la sua foto.
4. **Restauro, trittico:** "Prima" a sinistra in alto, il portone intero al centro con il cursore, "dopo" a destra in basso. Sotto, centrati: antitarlo, gommalacca, legno vecchio della stessa essenza, colore al campione, e "Manda una foto del pezzo".
5. **Il Bo, la firma** (noce): "Le porte di Gio Ponti" a 216 px, "Palazzo del Bo, Università di Padova", poi il racconto in quattro passi e il link alla scheda del lavoro.
6. **Lavori:** "Sette lavori, su ventidue" e la fila orizzontale, da (03) a (09).
7. **Chiusura:** "049 900 4916" a 190 px, da toccare; "Chiamate prima di passare" e l'email. Poi, in due colonne, la bottega (indirizzo, indicazioni sulla mappa, foto (10) del capannone, Mauro, Giuliano, email) e "Chiedi un preventivo", con il modulo della versione professionale (prepara l'email).
8. **Piede:** firma calligrafica, voci del sito, ragione sociale, sede legale, laboratorio con la mappa, P.IVA, Privacy (iubenda), Cookie (la loro pagina), "Torna su".

## Foto usate

Tutte dell'azienda, riscaricate il 5/11/2026 dalle 22 schede `/progetti/...` (e da `/azienda/` la foto del capannone e il logo) alla risoluzione più alta. Sono 218 file in `assets/originali/`, fuori da git: originali di WordPress senza `-NNNxNNN` e, dove esiste, l'originale più grande del `-scaled` (per esempio `porte-a-bilico-2.jpg` 1836x3264, `porte-moderne-4.jpg` 2592x4608). Nessuna foto di repertorio, nessuna immagine generata.

| In pagina | File originale (misura) | Taglio e misura in pagina a 1440 |
|---|---|---|
| Apertura, sottoscala | `2020-05_Bottega_dell_Arte_Armadiature-1.jpeg` (1600x900) | intera a tutta pagina: 1,0 a 1440 e 1,2 a 1920; nella cornice iniziale 1,28 per lo zoom del kit; sul telefono taglio 720x900 |
| (02) Laboratorio | `2020-06_Bottega_dell_Arte_Finestre-1.jpg` (1600x1200) | taglio 880x660 sulla pila di telai, mostrata a 540 px |
| Indice: arredo, serramenti, restauro, negozi | `Librerie-1.jpeg`, `Finestre-1.jpeg` (777x1600), `2020-10_Port1.jpg`, `Negozi_Pasticceria_Bolzano-4.jpg` | tagli 4:5, file da 640 px mostrati a circa 430 px |
| Prima e dopo | `2020-10_Port.4.jpeg` e `2020-10_Port-3.jpeg` (1200x1600) | raddrizzate su 464x1498, mostrate a 234x756 |
| Il Bo | `2020-06_universita02.jpg`, `09`, `03`, `01` (700x500) | 648x463, cioè 0,93 della misura vera |
| (03) Porta a bilico | `2020-06_porte-a-bilico-2.jpg` (1836x3264) | 2:3, 324x486 |
| (04) Porta laccata | `2020-06_porte-moderne-4.jpg` (2592x4608) | 3:4, 338x450 |
| (05) Credenza restaurata | `2020-06_Bottega_dell_Arte_Restauro_Mobili_Antichi.jpeg` (1600x777) | 2:1, 684x342 |
| (06) Controsoffitto | `2020-05_Bottega_dell_Arte_Controsoffitti-4.jpeg` (1200x1600) | 3:4, 338x450 |
| (07) Pasticceria vicino a Bolzano | `Negozi_Pasticceria_Bolzano-14.jpg` (1599x1200) | taglio quadrato senza l'insegna, 396x396 |
| (08) Mobile del bagno | `Mobili_del_Bagno-12.jpg` (1024x1821) | 3:4, 338x450 |
| (09) Porte restaurate | `2020-06_porte_restaurate-n1.jpg` (678x1024) | 2:3, 324x486 |
| (10) La bottega | `2020-05_falegnameria-a-padova.jpg` (1140x758) | 3:2, 520x347 |
| Logo e icona | `2020-05_logo_bottega_arte_HD.png` (1014x200), `cropped-logo_bottega_arte_HD.png` (512) | PNG a 400 e 800 px, icona a 64 e 180 |

Nessuna foto supera 1,25 volte la sua misura vera a 1440, salvo i 1,28 temporanei della cornice d'apertura, prima che scorrendo torni a 1,0.

**Foto da rifare** (con la lista del LEGGIMI, che resta valida):
1. Il sottoscala a 2400 px o più, senza lampadario e pianta del cliente. È la prima cosa che si vede e, nella cornice, oggi è morbido.
2. Il portone prima e dopo dallo stesso punto, frontale, su fondo neutro: oggi le due foto sono raddrizzate da due riprese diverse, una sdraiata e una in piedi.
3. Il Bo a piena risoluzione e con la luce ambiente, se l'Università lo permette (oggi 700x500, con il flash sulla bussola).
4. Mauro e Giuliano al banco, per la sezione della bottega, al posto della pila di telai.
5. Il laboratorio in ordine con un pezzo in lavorazione, e la gommalacca a tampone.
6. Dettagli in luce radente per le schede dell'indice: venatura, ottone, campione di colore.

## Misure

- **Scala a 1440 / 390:** titolo 216/68 px; titolo del Bo 216/66; telefono della chiusura 190/52; "Prima" e "dopo" 134/55; righe dell'indice 92/37; titolo dei lavori 75/39; `h2`, indirizzo e preventivo 52/28; manifesto 49/28 (Satoshi); titoli dei passi 32/22; didascalia d'apertura 32 (a 390 diventa una didascalia da 13 sotto la foto); testo 18/17; didascalie 13 in maiuscolo.
- **Margini:** 60 px a 1440, 20 px a 390 (kit `--he-m`). Respiro tra le sezioni 201 px a 1440 (kit `--he-sez`).
- **Altezza:** 13.825 px a 1440 con il movimento (compresi gli spazi delle sezioni fissate), 9.557 px fermi; 10.568 px a 390.
- **Peso al primo caricamento:** 749 KB a 1440 e 664 KB a 390 (limiti 2,5 e 1,5 MB). Con tutta la pagina scorsa, circa 1,1 MB. Cartella `sito-he` 2,4 MB.
- **Foto d'apertura precaricata** con `media` diverso per telefono e schermo. Spostamento del layout misurato: 0,005 a 1440 e 0 a 390.
- **Prove** (`_prova/he/prove/finale*`): a 390, 768, 1024, 1440 e 1920, con e senza movimento, nessuno scorrimento orizzontale (larghezza del documento uguale alla finestra) e nessun errore di script, di console o di rete. Le registrazioni a 1440 e 390 non hanno errori.
- **Comandi:** 6 link `tel:` (testata, apertura, chiusura e i tre numeri della bottega), 3 `mailto:` più il modulo, 3 link alla mappa (apertura, chiusura, piede).
- **Controllo d'uso dal telefono:** nella prima schermata a 390 ci sono il numero in testata e "Chiama 049 900 4916", il mestiere ("Falegnameria a Mestrino, Padova. Arredi su misura, serramenti e restauro") e "Via Levico 18, Mestrino: indicazioni". Si trovano tutti sotto i 10 secondi, senza scorrere.

## Stima mia (non il voto del giudice)

Design 8, creatività 8, usabilità 8,5, contenuto 8: media pesata circa 8,1. Quasi tutta la distanza dai riferimenti viene dalle foto. Molteni e Minotti hanno servizi fotografici veri; qui sono foto di telefono, tenute in cornici medie e trattate allo stesso modo. Con il servizio fotografico della lista sopra, il design salirebbe di un punto senza toccare il codice.

## Problemi aperti

- **Morbidezza dell'apertura:** nella cornice iniziale la nicchia è mostrata a 1,28 (lo zoom del kit su una foto di 1600 px). Serve la foto rifatta, oppure una cornice più piccola.
- **"Lo stesso portone":** che `Port.4` e `Port-3` siano lo stesso portone lo dicono la scheda e le specchiature che coincidono dopo il raddrizzamento. Resta da confermare con loro (LEGGIMI).
- **Permessi:** il permesso di nominare in home Palazzo del Bo, Università di Padova e Gio Ponti, e di pubblicarne le foto. Il nome della pasticceria: in pagina è "vicino a Bolzano" e la foto è tagliata senza l'insegna.
- **Ragione sociale:** "Snc" come nella versione professionale. La forma giuridica e la sede legale vanno confermate in visura (LEGGIMI).
- **Modulo:** prepara un'email e non invia nulla. Va collegato a un servizio di invio, con allegati e consenso (LEGGIMI).
- **Pagine interne:** i link ai mestieri, alle schede e alle 22 realizzazioni portano ancora al sito WordPress di oggi. Le pagine interne vanno fatte con lo stesso sistema.
- **Testata sul telefono:** si nasconde scendendo, come chiede il kit, e il numero torna appena si risale. In fondo c'è il numero a tutta larghezza. Se il committente lo vuole sempre visibile, basta togliere `data-he-header`.
- **Fondo della testata:** compare con la dissolvenza di 0,4 s del kit; in un fotogramma a 390 si vede il testo sotto il logo per un istante.
- **Anteprima dell'indice:** "Restauro" usa il maniglione del portone, che torna nel prima e dopo. È voluto (è il dettaglio più bello che hanno), ma con una foto in più si potrebbe evitare.
- **Orari, recensioni, anni dei lavori:** non nelle fonti, quindi non in pagina. "40 anni di esperienza" è tolto apposta, perché è da riconfermare.
