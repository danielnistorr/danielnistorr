# Bottega dell'Arte: home HE, nota

Pagina: `sito-he/index.html` (5 novembre 2026, ritoccata lo stesso giorno dopo il giudizio), con il kit in `sito-he/kit/` (he.css, he.js, vendor/), le immagini in `sito-he/img/` (WebP), i caratteri in `sito-he/fonts/` con le licenze. La versione professionale `sito/` non è stata toccata. Direzione scritta prima del codice in `DIREZIONE-HE.md`: dove questa nota e la direzione non coincidono (il Bo, i caratteri degli `h2`), vale questa nota.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (il film dello scorrimento, `_metodo/highend/kit/registra.mjs`), `foglio-1440.jpg` e `foglio-390.jpg` (i fotogrammi, uno al secondo), `fotogrammi-1440-NN.jpg` e `fotogrammi-390-NN.jpg`, le prime schermate ferme `prima-schermata-1440.jpg`, `prima-schermata-390.jpg` e le stesse con "riduci movimento" (`-fermo`).

Rifare: `python3 -m http.server <porta>` dalla radice del repository, poi `node _metodo/highend/kit/registra.mjs http://127.0.0.1:<porta>/BottegaDellArte-Sito/sito-he/index.html BottegaDellArte-Sito/screenshot/he 1440 900` e lo stesso con `390 844`. Immagini: `python3 -I _prova/he/he_img.py assets/originali _prova/he/lavorazione sito-he/img`. Prove di larghezza, errori e peso: `node _prova/he/prova.mjs <url> <cartella> <larghezza> <altezza> moto|fermo`.

## Giro di ritocco (giudice: 6,7 su 10, soglia 8)

I cinque interventi del giudice, in ordine, più uno sul ritmo della pagina.

1. **Apertura.** `data-he-scale-zoom="1"`: niente più ingrandimento iniziale, la nicchia nella cornice è a 1,0 della foto (1600 px) a 1440. Cornice `inset(44% 38% 33.5% 23%)`, regolata sulla foto: l'ottone con le fughe intorno, circa 30 px di anta per lato. `.ap-nota` sotto la cornice (`left:23%; top:calc(66.5% + 12px)`). Controllata a 1440 sulla schermata a piena misura: nitida quanto lo permette il file del telefono.
2. **Foto** (`he_img.py`). Tagli sui dettagli: (05) le mensole intagliate, i cassetti e le specchiature della credenza, senza la parete a righe verdi e senza le sedie (660x330); (07) l'attacco tra il sedile in frassino e le gambe in ferro, senza la vetrina (344x344); (08) la venatura che gira sul bordo del lavabo (300x400); (02) le teste dei telai sul carrello (480x360). Un trattamento unico per tutte: colore a 0,6, ogni canale da un nero all'80 per cento del noce #2A1D14 fino alla carta #F1ECE3 (i bianchi delle foto diventano il fondo della pagina). Grana `.he-grana` a .22, impostata nella pagina (il kit resta a .16). I tagli mostrati alla misura vera hanno una passata leggera di nitidezza e qualità WebP 88.
3. **Il Bo.** Tolto `data-he-story`. Sotto "Le porte di Gio Ponti" le quattro foto in fila, 312 px a 1440 (700x500, cioè 0,45 della misura vera), ognuna con il numero (01)-(04) accanto al titolo del passo e la sua riga. Tra 900 e 1180 px due per riga. Sul telefono si sfogliano con il dito (`scroll-snap` nativo, 304 px a 390). Resta l'unica sezione a colore pieno (noce).
4. **Restauro.** Le due foto raddrizzate tagliate sui pannelli con i fori della maniglia, la serratura e il maniglione nuovo (464x580, da y 460 a 1040, controllato: le specchiature coincidono), mostrate a misura vera. "Prima" e "dopo" ai lati, sulla riga di mezzo della foto, alla stessa altezza della maniglia del cursore (56 px). Tolta la riga "Lo stesso portone, dalle due foto raddrizzate"; gli `alt` dicono "due pannelli di un portone", senza dire che è lo stesso (da confermare).
5. **Tipografia.** Gloock solo su titolo e didascalia d'apertura, indice dei mestieri, "Prima" e "dopo", titolo del Bo e telefono della chiusura. Gli `h2` del restauro (ora allineato a sinistra), "Sette lavori, su ventidue", l'indirizzo e "Chiedi un preventivo" in Satoshi 500 a 36 px (28 sul telefono); gli `h3` del Bo in Satoshi 500 a 26 px (22 sul telefono). Sotto i 900 px la didascalia d'apertura è in Satoshi 15 px, non in maiuscolo. I numeri 01-04 dell'indice stanno sulla linea di base del nome, accanto (anche sul telefono); quelli del Bo sono nel titolo del passo. "In laboratorio", "La posa", "Per le finiture" sono l'inizio della frase in Satoshi 500, non più un'etichetta sopra il testo.
6. **Ritmo** (guardata la pagina intera dopo i cinque interventi). Il Bo, ora una fila di quattro foto, andava subito nella galleria orizzontale dei lavori: due file di foto di seguito, lo stesso ritmo. In mezzo c'è uno **stacco**: una pagina vuota alta quanto lo schermo, con un solo dettaglio di legno alla misura vera (576x720 da `porte-interne.jpg`, 1836x3264: la venatura dell'anta e la maniglia a incasso, fino allo stipite). Nessun movimento aggiunto.

## Idea

**"In stile o moderni."** È il loro titolo di oggi ("arredamenti su misura, in stile o moderni"), detto a 216 px. La pagina mette accanto le due mani del mestiere: il pezzo nuovo e il pezzo restaurato. Il culmine è il Bo, dove il restauro tocca le porte e le pareti che portano la firma di Gio Ponti.

Il gesto d'apertura parte dall'ottone. La nicchia del sottoscala sta incorniciata come una fessura d'oro tra "In stile" (in alto a sinistra) e "o moderni." (in basso a destra). Scorrendo, la cornice si apre su tutta la stanza: le otto ante a push sotto la scala in ferro battuto, cioè "in stile e moderni" nella stessa foto.

## Riferimenti

Guardati a 1440 (prima schermata e tre passi di scorrimento) in `_prova/he/riferimenti/`. Del settore: Molteni&C, Minotti, Porro, Salvatori, Poliform e Henrytimi. Premiati su Awwwards: Schreinerei Siegesmund e Hays Woodworking. Le due mosse prese da ciascuno sono in `DIREZIONE-HE.md`, sezione 2. In pagina si vedono soprattutto queste:
- Molteni: foto medie fuori asse, numerate tra parentesi, con la didascalia doppia (lavoro in nero, materiale o categoria in grigio);
- Porro e Hays: i mestieri come indice di righe enormi in serif, con l'anteprima che cambia;
- Salvatori: la frase sola nel vuoto, cioè il manifesto della bottega, e la didascalia che nomina il materiale;
- Henrytimi: il rettangolo d'immagine piccolo al centro, prima che si allarghi, e di nuovo nello stacco dell'anta;
- Siegesmund: l'idea "moderno fatto come una volta", detta qui con le loro parole, e la galleria di tanti lavori;
- Minotti: un'unica pagina intera, il sottoscala, con il titolo corto sopra.

## Carattere

- **Gloock 400** (Duarte Pires, Google Fonts, SIL OFL 1.1) solo per: titolo e didascalia d'apertura, righe dell'indice, "Prima" e "dopo", titolo del Bo, telefono della chiusura.
- **Satoshi 400, 500, 700** (Indian Type Foundry, Fontshare, ITF Free Font License 2.0) per tutto il resto: manifesto, `h2` e `h3`, testo, interfaccia, didascalie e modulo.
- I file sono in locale (`fonts/gloock-latin*.woff2`, `fonts/satoshi-*.woff2`), con `OFL-Gloock.txt` e `FFL-Satoshi.txt`. La FFL ammette il self-hosting per il proprio sito.
- Nessuna delle due famiglie è usata in un'altra home della cartella. Riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.

## Colore

Carta #F1ECE3, inchiostro #16120E, noce #2A1D14 (solo la sezione del Bo, l'unica a colore pieno), ottone #B48C3C (numeri, link e filetti sul noce, 5,3:1), ottone scuro #7C5A1C (link e numeri sulla carta, 5,4:1), rovere #CBB28A (fondi delle foto mentre caricano), ferro #4B4741 (testi secondari, 7,8:1).

Niente gradienti, salvo una velatura scura in fondo alla foto d'apertura sotto la didascalia bianca. Niente ombre, angoli tondi o vetro. Sulle foto un solo trattamento (`he_img.py`, sopra) e la grana a .22.

## Movimento

- **Apertura:** `data-he-scale` con la cornice `inset(44% 38% 33.5% 23%)` e `data-he-scale-zoom="1"`, `data-he-split data-he-subito` sul titolo. Titolo, testo e didascalia piccola escono con `data-he-scale-via`; la didascalia grande entra con `data-he-scale-entra`. La sezione resta fissata per il 110 per cento di un'altezza di schermo. Sotto i 900 px non è fissata: la foto, un taglio verticale sulla nicchia, si assesta piano.
- **Sostegno 1:** prima e dopo del portone (`data-he-compare`), con il cursore a metà. A sinistra si vedono i fori della vecchia maniglia; trascinando verso sinistra compare il maniglione nuovo nello stesso punto.
- **Sostegno 2:** sette lavori in galleria orizzontale fissata (`data-he-horizontal`), con la barra d'avanzamento in ottone. Sul telefono la fila si sfoglia con il dito e si ferma su ogni pezzo.
- Il Bo non ha più movimento: è una fila di foto ferma (sul telefono si sfoglia con il dito, come comando d'uso).
- Sempre: testata che si nasconde scendendo da 900 px in su (sul telefono resta, con il numero: lo fa il kit). Indice dei mestieri con l'anteprima ferma (`data-he-index`), solo come comando d'uso. `data-he-split` su tre testi: titolo, manifesto, titolo del Bo.
- **Riduci movimento**, provato con `reducedMotion: 'reduce'` a 390, 768, 1024, 1440 e 1920: la pagina è ferma e completa. L'apertura resta nella composizione incorniciata, la galleria scorre di lato con la barra del browser, prima e dopo e indice funzionano.

## Sezioni (scheletri diversi)

1. **Apertura** fissata: titolo in diagonale, la fessura d'ottone in mezzo, testo e comandi in alto a destra (mestiere, "Chiama 049 900 4916", "Chiedi un preventivo", "Via Levico 18, Mestrino: indicazioni"). Si apre sulla stanza intera.
2. **La bottega:** il manifesto (Mauro Nosarini e Giuliano Saibene, cominciati da ragazzini in una falegnameria artigiana di Padova; disegni di architetti o schizzi, o progetto da zero). Sotto, tre righe di fatti (laboratorio, posa, finiture) e fuori asse la foto (02) delle teste dei telai.
3. **Indice dei mestieri:** Arredo su misura, Serramenti e porte, Restauro, Negozi e locali, a 92 px, con il numero accanto. A destra l'anteprima 4:5 ferma; sul telefono ogni riga ha la sua foto.
4. **Restauro, trittico:** "Prima", i due pannelli a misura vera con il cursore, "dopo", sulla stessa riga. Sotto, a sinistra: antitarlo, gommalacca, legno vecchio della stessa essenza, colore al campione, e "Manda una foto del pezzo".
5. **Il Bo, la firma** (noce): "Le porte di Gio Ponti" a 216 px, "Palazzo del Bo, Università di Padova", poi le quattro foto in fila con i passi e il link alla scheda.
6. **Stacco:** una pagina vuota con la venatura di un'anta e la maniglia a incasso, 576x720 alla misura vera.
7. **Lavori:** "Sette lavori, su ventidue" e la fila orizzontale, da (03) a (09).
8. **Chiusura:** "049 900 4916" a 190 px, da toccare; "Chiamate prima di passare" e l'email. Poi, in due colonne, la bottega (indirizzo, indicazioni sulla mappa, foto (10) del capannone, Mauro, Giuliano, email) e "Chiedi un preventivo", con il modulo che prepara l'email.
9. **Piede:** firma calligrafica, voci del sito, ragione sociale, sede legale, laboratorio con la mappa, P.IVA, Privacy (iubenda), Cookie (la loro pagina), "Torna su".

## Foto usate

Tutte dell'azienda, riscaricate il 5/11/2026 dalle 22 schede `/progetti/...` (e da `/azienda/` la foto del capannone e il logo) alla risoluzione più alta, in `assets/originali/` (fuori da git). Nessuna foto di repertorio, nessuna immagine generata.

| In pagina | File originale (misura) | Taglio e misura in pagina a 1440 |
|---|---|---|
| Apertura, sottoscala | `2020-05_Bottega_dell_Arte_Armadiature-1.jpeg` (1600x900) | intera: 1,0 a 1440 (anche nella cornice) e 1,2 a 1920; sul telefono taglio 720x900 |
| (02) Laboratorio | `2020-06_Bottega_dell_Arte_Finestre-1.jpg` (1600x1200) | taglio 480x360 sulle teste dei telai, mostrato a 536 px (1,12; al massimo 600 px) |
| Indice: arredo, serramenti, restauro, negozi | `Librerie-1.jpeg`, `Finestre-1.jpeg`, `2020-10_Port1.jpg`, `Negozi_Pasticceria_Bolzano-4.jpg` | tagli 4:5, file da 640 px mostrati a circa 430 px |
| Prima e dopo | `2020-10_Port.4.jpeg` e `2020-10_Port-3.jpeg` (1200x1600), raddrizzate | 464x580 sui pannelli centrali, a misura vera |
| Il Bo | `2020-06_universita02.jpg`, `09`, `03`, `01` (700x500) | in fila a 312 px |
| Stacco, anta | `2020-06_porte-interne.jpg` (1836x3264) | 576x720 a misura vera |
| (03) Porta a bilico | `2020-06_porte-a-bilico-2.jpg` (1836x3264) | 2:3, 324x486 |
| (04) Porta laccata | `2020-06_porte-moderne-4.jpg` (2592x4608) | 3:4, 338x450 |
| (05) Credenza restaurata | `2020-06_Bottega_dell_Arte_Restauro_Mobili_Antichi.jpeg` (1600x777) | 660x330 su mensole, cassetti e specchiature, a 684 px (1,04) |
| (06) Controsoffitto | `2020-05_Bottega_dell_Arte_Controsoffitti-4.jpeg` (1200x1600) | 3:4, 338x450 |
| (07) Pasticceria vicino a Bolzano | `Negozi_Pasticceria_Bolzano-14.jpg` (1599x1200) | 344x344 sugli sgabelli, senza vetrina né insegna, a 396 px (1,15; al massimo 430) |
| (08) Mobile del bagno | `Mobili_del_Bagno-12.jpg` (1024x1821) | 300x400 sul bordo del lavabo, a 338 px (1,13; al massimo 375) |
| (09) Porte restaurate | `2020-06_porte_restaurate-n1.jpg` (678x1024) | 2:3, 324x486 |
| (10) La bottega | `2020-05_falegnameria-a-padova.jpg` (1140x758) | 3:2, 520x347 |
| Logo e icona | `2020-05_logo_bottega_arte_HD.png` (1014x200), `cropped-logo_bottega_arte_HD.png` (512) | PNG a 400 e 800 px, icona a 64 e 180 |

Nessuna foto supera 1,25 volte la sua larghezza nativa, a 1440 e a 1920 (i tagli piccoli hanno un tetto in pixel).

**Foto da rifare** (con la lista del LEGGIMI, che resta valida):
1. Il sottoscala a 2400 px o più, senza lampadario e pianta del cliente: nella cornice ora è a 1,0, ma il file del telefono resta morbido sugli oggetti d'ottone.
2. Il portone prima e dopo dallo stesso punto, frontale, su fondo neutro.
3. Il Bo a piena risoluzione e con la luce ambiente, se l'Università lo permette (oggi 700x500, con il flash sulla bussola).
4. Mauro e Giuliano al banco, per la sezione della bottega.
5. Il laboratorio in ordine con un pezzo in lavorazione, e la gommalacca a tampone.
6. Dettagli in luce radente: venatura, ottone, campione di colore. Lo stacco dell'anta è il primo di questi, e oggi è una foto di telefono.

## Misure

- **Scala a 1440 / 390:** titolo 216/68 px; titolo del Bo 216/66; telefono della chiusura 190/52; "Prima" e "dopo" 134/55; righe dell'indice 92/37; `h2` del restauro, dei lavori, indirizzo e preventivo 36/28 (Satoshi 500); `h3` del Bo 26/22 (Satoshi 500); didascalia d'apertura 32 Gloock (a 390, 15 Satoshi); testo 18/17; didascalie 13 in maiuscolo.
- **Margini:** 60 px a 1440, 20 px a 390 (kit `--he-m`). Respiro tra le sezioni 201 px a 1440 (kit `--he-sez`).
- **Altezza:** 12.181 px a 1440 con il movimento, 9.311 px fermi; 9.443 px a 390.
- **Peso al primo caricamento:** 697 KB a 1440 e 621 KB a 390 (limiti 2,5 e 1,5 MB). Con tutta la pagina scorsa, 1,08 MB a 1440 e 0,99 MB a 390. Cartella `sito-he` 2,0 MB.
- **Foto d'apertura precaricata** con `media` diverso per telefono e schermo. Spostamento del layout misurato: 0,006 a 1440 e 0 a 390.
- **Prove** (`_prova/he/prove/ritocco/`): a 390, 768, 1024, 1440 e 1920, con e senza movimento, nessuno scorrimento orizzontale (larghezza del documento uguale alla finestra, e nessun elemento oltre il bordo, controllato anche dentro il `body` che taglia) e nessun errore di script, di console o di rete. Le registrazioni a 1440 e 390 non hanno errori.
- **Comandi:** 6 link `tel:`, 3 `mailto:` più il modulo, 3 link alla mappa.
- **Controllo d'uso dal telefono:** nella prima schermata a 390 ci sono il numero in testata e "Chiama 049 900 4916", il mestiere e "Via Levico 18, Mestrino: indicazioni". La testata con il numero resta visibile per tutta la pagina.

## Problemi aperti

- **Morbidezza dell'apertura:** a 1,0 non c'è più l'ingrandimento, ma il file è una foto di telefono a 1600 px: sugli oggetti d'ottone si vede la compressione. Serve la foto rifatta.
- **"Lo stesso portone":** che `Port.4` e `Port-3` siano lo stesso portone lo dicono la scheda e le specchiature che coincidono dopo il raddrizzamento. In pagina non è più scritto, ma il confronto lo lascia intendere: resta da confermare con loro (LEGGIMI).
- **Maniglione nascosto a metà corsa:** il maniglione nuovo è sul bordo sinistro dei pannelli, quindi con il cursore a metà si vedono i fori vecchi e non il maniglione. È voluto (si scopre trascinando), ma una foto rifatta frontale potrebbe metterli al centro.
- **Stacco dell'anta:** la didascalia dice solo "Porta interna": l'essenza e il tipo di porta (a bilico o scorrevole) non sono nelle fonti.
- **Permessi:** il permesso di nominare in home Palazzo del Bo, Università di Padova e Gio Ponti, e di pubblicarne le foto. Il nome della pasticceria: in pagina è "vicino a Bolzano" e il taglio non mostra l'insegna.
- **Ragione sociale:** "Snc" come nella versione professionale. La forma giuridica e la sede legale vanno confermate in visura (LEGGIMI).
- **Modulo:** prepara un'email e non invia nulla. Va collegato a un servizio di invio, con allegati e consenso (LEGGIMI).
- **Pagine interne:** i link ai mestieri, alle schede e alle 22 realizzazioni portano ancora al sito WordPress di oggi.
- **Anteprima dell'indice:** "Restauro" usa il maniglione del portone, che torna nel prima e dopo.
- **`DIREZIONE-HE.md`** descrive ancora il Bo come racconto con la foto ferma e gli `h2` in Gloock: è la direzione scritta prima del codice, superata da questo ritocco.
- **File non usati** in `sito-he/img/`: `indice-*-960.webp` e `indice-serramenti-777.webp`, rimasti dal primo giro (non si caricano).
- **Orari, recensioni, anni dei lavori:** non nelle fonti, quindi non in pagina. "40 anni di esperienza" è tolto apposta, perché è da riconfermare.
