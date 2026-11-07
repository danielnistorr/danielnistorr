# Distilleria Rizzi, home HE (7 novembre 2026, primo giro)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (Besley, SIL OFL 1.1; Excon, ITF Free Font License 2.0; licenze accanto), le immagini WebP in `sito-he/img/` (31 file). Cartella `sito-he` 2,1 MB. La `sito/` di oggi e il kit master non sono toccati. Direzione artistica in `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8788`, server fermato), `foglio-1440.jpg` (18 fotogrammi) e `foglio-390.jpg` (17), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` e `-390-*.jpg` (a piena misura, estratti dal video con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il motto è salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare (dalla cartella `DistilleriaRizzi-Sito`): immagini con `python3 -I _prova/he/script/immagini.py` (legge `assets/originali/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); spostamenti con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate `node _prova/he/script/prima.mjs <url> screenshot/he`; nitidezza dell'apertura a dpr 1 e 2 `node _prova/he/script/retina.mjs <url> <cartella>`; riferimenti `node _prova/he/script/riferimenti.mjs _prova/he/riferimenti nome=url ...`.

## Idea

"Oggi come una volta" (la loro frase, pagina `amari`) in Besley a 166 px accanto al Bitter: la cornice parte stretta sull'etichetta, sulla fascia RIZZI e sul corsivo, e scorrendo si allarga alla bottiglia intera. Poi la gamma messa in scala, "Da 11 a 70 gradi": otto bottiglie vere, ciascuna sul suo grado di un righello, dall'Aperizzi alla Vodka 70° della pasticceria.

## Sezioni (scheletri diversi)

1. **Apertura** (carta, a tutta altezza, fissata per il gesto): manifesto, motto su due righe a sinistra, bottiglia alta l'86% della finestra al 72% della larghezza, mestiere e telefono in basso, didascalia del Bitter che entra alla fine del gesto. Sul telefono: motto sopra, bottiglia e mestiere affiancati, nessun fissaggio.
2. **Laboratorio** (carta): "Facciamo tutto noi, dall'inizio alla fine." a tutta larghezza; dittico sfalsato dell'alcolato di fiori di sambuco (poche ore, due settimane) a sinistra, testo a destra.
3. **Firma, "Da 11 a 70 gradi"** (carta): grafico a tutta larghezza, bottiglie in piedi sul righello SVG (un trattino per grado da 8 a 42, interruzione, 70), grado in Besley e nome sotto. Sul telefono si sfoglia di lato.
4. **Pasticceria** (blu etichetta, l'unico campo pieno): testo a sinistra, tre famiglie in una riga, gusti e aromi chiusi in `<details>`, telefono e email; i quattro bottiglioni a destra sul bordo del campo.
5. **Chi siamo** (carta, centrata come una lettera): la frase sui ricettari del fondatore, la foto di Maddalena e Alessandro, "Dal 14 dicembre 2022 Distilleria Rizzi prosegue con Maddalena e Alessandro", lo spaccio e i mobili della sartoria Vogue 80.
6. **Spaccio e contatti** (carta): il telefono in Besley a 135 px, indirizzo con la mappa, orari in tabella, email, cellulari, PEC, la foto degli scaffali.
7. **Piede** (inchiostro): scritta a pennello, link, social, ragione sociale, via, P.IVA, PEC, "Bevi responsabilmente. Alcolici venduti solo ai maggiorenni." (come la versione di oggi), Privacy, Cookie.

Negozio online: la versione di oggi non ha il link (il WooCommerce del sito è vuoto e da confermare), quindi non c'è.

## Caratteri

Besley 400 (display, tre momenti: motto 166 px, firma 171 px con i gradi a 37, telefono 135) ed Excon 400/500 (tutto il resto, testo 18/28). Riga in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`: nessuna altra home usa le due famiglie.

## Foto: originali trovati e misura in pagina

Riscaricata tutta la libreria media (123 voci, 159 file con le varianti) in `assets/originali/`. La scoperta: le immagini che WordPress mostra ritagliate (suffisso `-e<numero>`, alte 500 px) e quelle `-scaled` hanno l'originale grande sul server.

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| Bitter dell'apertura | `2023-01-bott-bitterclassico.png` (sul sito 124x500) | 498x2010 | 193x774 a fine gesto (0,39); all'inizio 280 px di larghezza (0,56; 1,13 sul retina simulato) |
| Otto bottiglie della scala | Aperizzi 490x1884, Carciofo 765x2802, Leone 944x3767, Bitter 498x2010, Punch Arancio 1088x4016, Prugna 1096x4147, Pinalpe 1350x3124, Vodka in tanica 1286x1932 | | alte 446 px (Pinalpe 0,8, tanica 0,7), file da 460 e 920 px |
| Bottiglioni della pasticceria | `2024-01-aromi.png` | 2084x2084 | 594x620 (0,29) |
| Alcolato, dittico | `2023-06-20230530_180130-01.jpeg`, `..._175656-01.jpeg` (sul sito -scaled 1154x2560) | 2084x4624, taglio 2084x2780 | 312 e 424 px di larghezza |
| Maddalena e Alessandro | `2024-10-1000070154-02.jpeg` | 1200x1600, taglio 1000x750 | 440x330 |
| Scaffali dello spaccio | `2025-08-5.jpg` | 1600x1600, taglio 860x860 | 313x313 |

Controllo al 100% a 1440 e a dpr 2 (`retina.mjs`): l'etichetta all'inizio del gesto è nitida sullo schermo normale e appena morbida sul retina (1,13, scatto da telefono); la bottiglia intera è ridotta e nitida. Rapporto massimo tra misura mostrata e file: 0,42 a 390, 0,57 a 1440, 0,68 a 1920.

## Pesi e prove (sezione 6)

- **Peso al primo caricamento**: 586 KB a 1440 e 625 KB a 390 (soglie 2,5 e 1,5 MB); 853 a 768, 625 a 1024, 682 a 1920. Bottiglia d'apertura precaricata (`imagesrcset`), caratteri precaricati.
- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", nessuno scorrimento orizzontale, nessun elemento oltre il bordo (la scala del telefono scorre nel suo contenitore), nessun errore di script, di console o di rete. Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (3.753 caratteri a 1440, 3.691 a 390, dove manca il secondo bottone di chiamata dell'apertura); con il movimento l'unico elemento nascosto all'inizio è la didascalia del Bitter, che entra col gesto.
- **Layout stabile**: CLS da 0 a 0,0003 a tutte le larghezze; con la rotella 0 a 1440 e 0,0007 a 390, con l'apertura fissata (`pinType: "transform"`).
- **Controllo d'uso dal telefono**: in prima vista "Oggi come una volta", la bottiglia, "Liquori, amari, sciroppi e aromi per la pasticceria. A Mestrino dal 1926, di Maddalena e Alessandro.", "Spaccio in via G. Negri 7" e "Chiama 049 900 0053" nella testata, che resta.
- U+2014: nessuno, nella pagina, negli script, in questa nota, nella direzione, nei CREDITI e nel registro.

## Fotogrammi guardati da estraneo

1440 a 2, 5, 8, 11, 14 e 17 s (apertura all'inizio e alla fine del gesto, firma, pasticceria, contatti, piede); 390 a 1, 6 e 10 s.
- L'apertura regge da sola: il motto grande, l'etichetta come un francobollo che diventa bottiglia, il mestiere leggibile in basso. La firma è la schermata più forte: otto etichette vere sullo stesso piano, i gradi in Besley.
- Corretti dopo averli guardati: il righello stava sotto le didascalie e non sotto le bottiglie (ora le bottiglie poggiano sul righello e i gradi stanno sotto); sul telefono il testo del laboratorio copriva il dittico; vuoti di mezza schermata prima e dentro il laboratorio (spazi ridotti); "Chi siamo" era foto a sinistra e testo a destra dopo la pasticceria con lo schema speculare (ora è centrata, e la frase sui ricettari viene prima della foto: prima "una volta", poi "oggi"); la cornice d'apertura era piccola e bassa (ingrandimento da 1,34 a 1,45, più in alto, mai sopra le lettere); la foto dello spaccio era il banco di Natale in HDR (ora gli scaffali); la foto dei titolari ridotta a 440 px; tolto il doppio "Chiama" sul telefono.
- Tolte tre frasi che non venivano dalle fonti: "Ogni bottiglia sta sul suo grado", "restano i clienti di sempre", "Gradazioni dalle schede dei prodotti".
- Resta: sotto la firma la pagina è più quieta, perché le foto di persone e di luoghi sono scatti da telefono; il video ha bande di colore sulla carta dovute alla compressione, la pagina no.

Stima personale circa 8,1 (design 8, creatività 8, usabilità 8,5, contenuto 8), da leggere con lo scarto medio di 0,7 che il SISTEMA registra tra costruttore e giudice: atteso 7,4-7,6. Della distanza da un 9, metà almeno è nelle foto.

## Problemi aperti

- **1850 sull'etichetta**: il tondo col leone sull'etichetta del Bitter porta "casa fondata nel 1850"; nella cornice d'apertura sul retina si legge, piccolissimo. È l'etichetta vera, non un nostro testo, ma la data è da confermare: se il committente preferisce, la cornice si può fermare sopra il tondo.
- **Centenario**: il 15 dicembre 2026 non è in pagina (la festa e la data di fondazione sono da confermare). Confermato, va in una riga sotto il motto.
- **Titolari**: solo i nomi, come nella loro home; i cognomi aspettano il loro sì.
- **Scala**: Pinalpe a 0,8 dell'altezza stimato dalla foto di gruppo `2024-01-liquori.png`; la tanica sta dopo l'interruzione del righello e la sua misura non è in scala. Va confermato che le otto bottiglie siano tutte in vendita.
- **Spaccio**: nella foto degli scaffali si intravedono i cartellini con i prezzi e un Felsina sull'ultimo ripiano.
- **Privacy e Cookie**: le pagine non esistono ancora (404), come per la versione di oggi.
- **Link al catalogo**: "Tutti i liquori e gli amari" e il piede puntano alle pagine del sito di oggi.

## Foto da rifare (in ordine di valore)

1. **Still life delle otto bottiglie e della tanica** in studio, alla stessa distanza (così le altezze sono vere), 6000 px, luce morbida da sinistra, polarizzatore; più la **macro dell'etichetta del Bitter** (fascia RIZZI e corsivo) a 6000 px: è dove parte il gesto e oggi sul retina è a 1,13.
2. **Il laboratorio in orizzontale**: l'alcolato nel becher alla stessa luce del dittico, l'estrattore e l'essiccatore con le scorze, le mani di Maddalena e Alessandro. Manca un momento fotografico a tutta pagina: questa è la foto che lo darebbe.
3. **Maddalena e Alessandro** di giorno, in laboratorio o sulla porta dello spaccio, al posto del taglio del nastro al flash.
4. **I ricettari del fondatore**, scansione piana o foto frontale: accanto alla loro frase daranno la prova di "una volta".
5. **Lo spaccio di giorno**, senza addobbi, cartellini girati, i mobili della sartoria Vogue 80 in vista.
6. **I prodotti per la pasticceria** uno per famiglia (sciroppo, aroma a 70°, Marsala), stessa luce degli still life.
7. **Il vecchio marchio col leone** in vettoriale o scansione a 600 dpi (oggi 392 px), se la questione del 1850 si chiarisce.
