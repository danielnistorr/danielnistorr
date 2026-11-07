# Distilleria Rizzi, home HE (7 novembre 2026, secondo giro)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (Besley, SIL OFL 1.1; Excon, ITF Free Font License 2.0; licenze accanto), le immagini WebP in `sito-he/img/` (27 file, tolti quelli non piu' usati: tanica, titolari, bottiglie a 460 e 920, spaccio a 860). Cartella `sito-he` 2,1 MB. La `sito/` di oggi e il kit master non sono toccati. Direzione artistica in `DIREZIONE-HE.md` (aggiornata dove descriveva cose tolte).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8792`, server fermato), `foglio-1440.jpg` e `foglio-390.jpg` (16 fotogrammi ciascuno), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-2.0/6.5/8.5/11.5.jpg` e `fotogrammi-pieni-390-1.0/6.0/10.0.jpg` (a piena misura, estratti con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il motto e' salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare (dalla cartella `DistilleriaRizzi-Sito`): immagini con `python3 -I _prova/he/script/immagini.py` (legge `assets/originali/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url> > _prova/he/prove-finale.json`; spostamenti con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate `node _prova/he/script/prima.mjs <url> screenshot/he`.

## Secondo giro: giudizio 7,1 e cosa e' cambiato

Il giudice: design 6,5, creativita' 7, usabilita' 8, contenuto 7,5. "Il modello serif grande su carta con bottiglia scontornata, fatto bene; sotto la piega una brochure con foto da telefono." Interventi fatti, nell'ordine:

1. **Chi siamo**: tolta la foto del taglio del nastro coi palloncini. Due colonne: la frase dei ricettari a 28 px a sinistra (colonne 1-6), h2 e storia a destra (colonne 8-12); sul telefono una colonna.
2. **Firma**: tolta la tanica, al 70 restano "70°" e "Vodka". `--H` a `clamp(300px,40vw,600px)`: bottiglie alte 576 px a 1440 e 600 a 1920, con file da 600 e 1200 px (rapporto 0,96 a 1440 e 1,0 a 1920 sugli schermi normali). Nello script tutte le bottiglie hanno lo stesso tono (bianco neutro preso dalle luci senza colore, livelli comuni) e lo stesso taglio dei tappi (via i lembi dei sigilli che sporgevano da un lato, taglio piano dove il tappo arriva al 92% della sua larghezza). Il righello ora va da 9 a 42 gradi sul 92,4% della larghezza: a ogni misura le bottiglie non si toccano (Leone e Bitter, a 4 gradi, restano le piu' vicine) e il 70 chiude sul margine destro. 64 px sotto `.piede-scala`. Tolta l'etichetta "% vol." (i gradi hanno gia' l'unita').
3. **Cornice iniziale** (calcolata nella pagina prima del kit, solo dal CSS): bordo alto sulla cima della "O" di "Oggi" (testata + 9svh + 0,1035 em), bordo basso sul fondo del biglietto (7svh, il fondo del bottone "Chiama"), bordo destro sul margine, bordo sinistro staccato dal motto. A 1440x900 la cornice e' 467x667 px, ingrandimento 2,59; la scritta RIZZI ha il centro al 31% dell'altezza della cornice (terzo alto) e la scritta "casa fondata nel 1850" del tondo col leone resta sotto il bordo basso, anche a dpr 2 (provato: si vede solo la cima del tondo). Dove lo spazio non basta (1024x768) la cornice si accorcia dal basso e finisce sulla prima riga del biglietto. Rapporto con il file all'inizio del gesto: 1,02 a 1440, 1,20 a 1920 (sul retina e' morbida). Trovato un difetto del kit: GSAP legge male un `inset()` con zeri finali ("18.90%" diventa 189%): la pagina scrive i valori senza zeri finali; il kit master non e' toccato.
4. **h2 di servizio** di laboratorio, pasticceria e chi siamo: Excon 400, `clamp(30px,3vw,44px)`, -0,01em. Il titolo del laboratorio sta ora nella colonna di destra sopra il testo.
5. **Spaccio**: 4:3 con `object-position: 60% 15%` e un nuovo taglio dell'originale (`2025-08-5.jpg`, 580x464 dagli scaffali di mezzo e di sotto): fuori il fiocco di Natale, il Felsina dello scaffale alto e l'albero. **Dittico**: due foto uguali (3:4) sulla stessa base, nessun margine sfalsato. Didascalie dei becher senza tempi: "Alcolato di fiori di sambuco in un becher da 500 ml" e "L'alcolato ambrato, «la base per la produzione del liquore ai fiori di sambuco»".
6. **Contenuto**: "dal 1926" tolto dalla prima schermata, dal piede e dalla descrizione della pagina (ora "A Mestrino (PD)" e, nel piede, "a due passi da Padova", dalla loro home). Tolti "verdastro", "pronti all'uso", "piano terra", "ti diciamo quando trovarci", "perfetto per lo spritz classico" (ora "liquore per aperitivi", dalla scheda) ed "esaltare" (la frase della pasticceria ora cita solo «pensata per laboratori artigianali, professionisti e appassionati»). "Spaccio in via G. Negri 7" apre la mappa.

Nota sulle fonti: "verdastro", "pronti all'uso", "piano terra" e "perfetto per lo spritz classico" erano frasi del sito di oggi (articolo sul sambuco, pagina pasticceria, pagina dell'apertura dello spaccio, scheda Aperizzi), ma non dei file della cartella: tolte lo stesso. Restano dal sito di oggi, riletto il 7/11/2026 dall'API di WordPress: "liquore per aperitivi" (scheda `aperizzi`), "la base per la produzione del liquore ai fiori di sambuco" e "alcolato ambrato" (articolo `lo-riconosci`), i mobili "dall'antica sartoria Vogue 80 di via Roma, a Padova" e «ai soli professionisti del settore, quali bar, pasticcerie, ristoranti» (pagina `apertura-spaccio`), "Contattare per disponibilita'" (pagina `contact`), "Bottiglia in vetro da 75cl" del Pinalpe (scheda `pinalpe`).

## Idea

"Oggi come una volta" (la loro frase, pagina `amari`) in Besley a 166 px accanto all'etichetta del Bitter: la cornice parte sulla fascia RIZZI e sul corsivo, allineata al titolo e al biglietto, e scorrendo si allarga alla bottiglia intera. Poi la gamma messa in scala, "Da 11 a 70 gradi": sette bottiglie vere, ciascuna sul suo grado di un righello, e il 70 della Vodka per la pasticceria in fondo.

## Sezioni (scheletri diversi)

1. **Apertura** (carta, fissata per il gesto): motto a sinistra, cornice sull'etichetta a destra dalla cima della "O" al fondo del biglietto, mestiere e telefono in basso; a fine gesto la bottiglia intera e la didascalia del Bitter. Sul telefono: motto sopra, bottiglia e mestiere affiancati, nessun fissaggio.
2. **Laboratorio** (carta): dittico uguale dell'alcolato a sinistra; a destra il titolo loro, la frase delle ricette dei fondatori, l'estrattore e l'essiccatore.
3. **Firma, "Da 11 a 70 gradi"** (carta): grafico a tutta larghezza, bottiglie in piedi sul righello SVG, grado in Besley e nome sotto. Sul telefono si sfoglia di lato.
4. **Pasticceria** (blu etichetta, l'unico campo pieno): testo a sinistra, tre famiglie, gusti chiusi in `<details>`; i quattro bottiglioni a destra.
5. **Chi siamo** (carta, due colonne di solo testo): una volta a sinistra, oggi a destra.
6. **Spaccio e contatti** (carta): telefono in Besley a 135 px, indirizzo con la mappa, orari, email, cellulari, PEC, la foto degli scaffali in 4:3.
7. **Piede** (inchiostro): scritta a pennello, link, social, dati legali, avvertenza sugli alcolici, Privacy, Cookie.

## Caratteri

Besley 400 (display, tre momenti: motto 166 px, firma 171 px con i gradi a 37, telefono 135) ed Excon 400/500 (tutto il resto; h2 di servizio 400 a 30-44 px; testo 18/28).

## Foto in pagina

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| Bitter dell'apertura | `2023-01-bott-bitterclassico.png` | 498x2010 (file 496x1966 dopo il taglio del tappo) | 505 px di larghezza all'inizio del gesto (1,02), 195 a fine gesto (0,39) |
| Sette bottiglie della scala | Aperizzi 490x1884, Carciofo 765x2802, Leone 944x3767, Bitter 498x2010, Punch Arancio 1088x4016, Prugna 1096x4147, Pinalpe 1350x3124 | | alte 576 px (Pinalpe 461), file da 600 e 1200 |
| Bottiglioni della pasticceria | `2024-01-aromi.png` | 2084x2084 | 620 px (0,52 del file da 1188) |
| Alcolato, dittico | `2023-06-20230530_180130-01.jpeg`, `..._175656-01.jpeg` | 2084x4624, taglio 2084x2780 | 368 px ciascuna |
| Scaffali dello spaccio | `2025-08-5.jpg` | 1600x1600, taglio 580x464 | 313x235 |

Rapporto massimo tra misura mostrata e file piu' grande: 0,62 a 390, 1,02 a 1440, 1,20 a 1920 (sempre l'etichetta all'inizio del gesto).

## Pesi e prove (sezione 6)

- **Peso al primo caricamento**: 635 KB a 1440 e 675 KB a 390 (soglie 2,5 e 1,5 MB); 902 a 768, 742 a 1024, 816 a 1920.
- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", nessuno scorrimento orizzontale, nessun elemento oltre il bordo, nessun errore di script, di console o di rete. Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (3.564 caratteri da 1024 in su, 3.502 sul telefono, dove manca il secondo bottone di chiamata); con il movimento l'unico elemento nascosto all'inizio e' la didascalia del Bitter, che entra col gesto.
- **Layout stabile**: CLS da 0 a 0,0003 a tutte le larghezze; con la rotella 0 a 1440 e 0,0007 a 390.
- **Controllo d'uso dal telefono**: in prima vista "Oggi come una volta", la bottiglia, "Liquori, amari, sciroppi e aromi per la pasticceria. A Mestrino (PD), di Maddalena e Alessandro.", "Spaccio in via G. Negri 7" (apre la mappa) e "Chiama 049 900 0053" nella testata, che resta.
- U+2014: nessuno, nella pagina, nello script delle immagini, in questa nota e nella direzione.

## Fotogrammi guardati da estraneo

1440 a 2,0, 6,5, 8,5 e 11,5 s (apertura ferma, laboratorio, firma e pasticceria, chi siamo e contatti); 390 a 1, 6 e 10 s; piu' le prime schermate a 1920x1080, 1536x864, 1280x800 e 1024x768.
- L'apertura ora e' una composizione: titolo a sinistra, etichetta a destra, due bordi in comune con il testo (cima della "O" e fondo del bottone) e il margine destro della testata. La firma regge di piu' con le bottiglie grandi e i tappi uguali.
- Corretti dopo averli guardati: GSAP non disegnava la cornice (zeri finali in `inset()`); a 1024 e 1280 l'immagine d'apertura sceglieva il file piccolo (`sizes` a 60vh da 900 px in su); a 1024x768 la cornice finiva a meta' del mestiere (ora sulla sua prima riga); il 70 usciva dal margine destro; "di Maddalena / e Alessandro" andava a capo nel mestiere; vuoto di 350 px tra laboratorio e firma (ora circa 250).
- Resta: chi siamo e' solo testo e il laboratorio ha due foto da telefono. Sul retina l'etichetta all'inizio del gesto e' morbida (circa 2 volte il file).

Stima personale circa 7,8, da leggere con lo scarto medio di 0,7 del SISTEMA: atteso 7,1-7,6. Della distanza da un 9, piu' di meta' e' nelle foto.

## Problemi aperti

- **1850 sull'etichetta**: fuori dalla cornice iniziale; a fine gesto la bottiglia intera e' piccola e il tondo non si legge. La data resta da confermare.
- **Fondazione e centenario**: l'anno e la festa del 15 dicembre 2026 non sono in pagina finche' non arriva la conferma.
- **Titolari**: solo i nomi; i cognomi aspettano il loro si'.
- **Scala**: Pinalpe a 0,8 dell'altezza stimato dalla foto di gruppo; va confermato che le sette bottiglie siano tutte in vendita.
- **Spaccio**: nella foto restano due cartellini con i prezzi e un'etichetta rossa con la renna.
- **Privacy e Cookie**: le pagine non esistono ancora (404).
- **Link al catalogo**: puntano alle pagine del sito di oggi.

## Foto da rifare (in ordine di valore)

1. **Still life delle sette bottiglie e della tanica** in studio, alla stessa distanza, 6000 px, luce morbida da sinistra, polarizzatore; piu' la **macro dell'etichetta del Bitter** (fascia RIZZI e corsivo) a 6000 px: e' la prima schermata ferma, oggi a 1,02 del file e morbida sul retina.
2. **Il laboratorio in orizzontale**: l'alcolato nel becher in controluce, l'estrattore e l'essiccatore con le scorze, le mani di Maddalena e Alessandro. E' la foto che darebbe alla pagina il momento grande sotto la piega.
3. **Maddalena e Alessandro** di giorno, in laboratorio o sulla porta dello spaccio: chi siamo oggi e' solo testo.
4. **I ricettari del fondatore**, scansione piana o foto frontale, accanto alla loro frase.
5. **Lo spaccio di giorno**, senza addobbi e con i cartellini girati.
6. **I prodotti per la pasticceria** uno per famiglia, stessa luce degli still life.
7. **Il vecchio marchio col leone** in vettoriale o a 600 dpi, se la questione del 1850 si chiarisce.
