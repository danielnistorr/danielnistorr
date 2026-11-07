# Fratelli Ruffatti, home HE (7 novembre 2026)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` con le licenze OFL, le immagini WebP in `sito-he/img/` (36 file, cartella `sito-he` 2,4 MB). La `sito/` di oggi non è toccata. Direzione artistica in `DIREZIONE-HE.md`, scritta prima del codice e aggiornata alla fine (la banda di Boteå e la parallasse spostata lì).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8781`), `foglio-1440.jpg` (26 fotogrammi) e `foglio-390.jpg` (27), i fotogrammi uno al secondo, `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo che il titolo è salito), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `Ruffatti-Sito`; legge `assets/originali/wp/`, fuori da git); prove con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; controllo d'uso dal telefono con `node _prova/he/script/uso.mjs <url>`; riferimenti con `node _prova/he/script/riferimenti.mjs`. Segnali da IA: `_metodo/kit/segnali.sh <url> _prova/he/segnali ruffatti-he`.

## Idea

**Prima di partire, ogni organo si monta qui.** "Ogni strumento Ruffatti, anche di grande dimensione, viene premontato in fabbrica" (pagina `l'interno di un organo Ruffatti`). Il gesto d'apertura lo fa vedere: la cornice mostra canne di facciata e cassa di mogano, come in chiesa; scorrendo si apre sulla falegnameria di Padova, con i banchi, i neon e tre artigiani: è l'organo della Cattedrale di Aguascalientes prima della partenza. La sezione firma è il registro che il loro sito inglese chiama "the signature stop of Fratelli Ruffatti": la Trompette en chamade, trombe d'ottone costruite in casa, con la prova fotografica (le 61 trombe di Uppsala e la saldatura del padiglione in laboratorio).

## Sezioni (scheletri diversi)

1. **Apertura, in fabbrica** (fissata sopra i 900 px): composizione in asse come una facciata. Cornice sulle canne al centro, "Organi a canne" a 207 px sotto, su una riga; in alto a sinistra nome, "Padova, dal 1940" e via Facciolati 166 (apre la mappa); in alto a destra il mestiere in italiano e in inglese, "Restauro di organi antichi" e "Write to us in English". La cornice si apre a tutta pagina ed entra la didascalia su un blocco di pietra.
2. **Manifesto**: la loro frase "costruiamo ogni componente possibile in laboratorio" a 45 px su dieci colonne, la stessa frase dal loro sito inglese sotto.
3. **La materia, "Tutte le canne sono costruite in casa"**: quattro foto sfalsate alla loro misura, dal tronco di sipo (con un uomo accanto, la scala) alla lastra colata sul banco di marmo, alle canne al 95% di stagno, alle noci tornite una per una; ognuna con una frase loro.
4. **Stacco alla misura vera**: una pagina di pietra quasi vuota con una canna ad ancia smontata a 800x603, la sua misura nativa; il fondo bianco della foto è portato esattamente alla pietra, così l'oggetto sta sulla pagina. Accanto la loro frase e il video della Bombarda di 32 piedi.
5. **Firma, "Trompette en chamade"** (mogano pieno, l'unico colore pieno): il titolo in ottone a 215 px largo tutta la griglia, le trombe di Uppsala a 760 px, la frase inglese e quella italiana, il dato dalla disposizione fonica (Trompette en Chamade 8′, 61 canne, quarta tastiera) e la saldatura del padiglione.
6. **Un luogo a tutta pagina**: la chiesa di Boteå, l'organo grigio perla sotto le volte bianche, con la parallasse.
7. **Dove suonano, "Da Padova abbiamo raggiunto tutti i continenti"**: Uppsala intera a sinistra; a destra otto luoghi in forma di disposizione fonica (nome e città, puntini di guida, tastiere e anno), da Monreale (sei tastiere) a New Orleans 2022, e la citazione di Frederick Swann.
8. **Restauro** (pietra più scura): cinque organi di altri costruttori in fila per data (1579 La Valle, 1612 Guglielmi, Callido, 1802 Zavarise, 1904 Telford), che sul telefono si sfogliano col dito; sotto, che cosa preparare per la prima telefonata, "Chiamate 049 750 666" e "Scrivete con le foto".
9. **Concorso di Miami**: una fascia, la finale dell'undicesima edizione il 5 febbraio 2027, i premi, il bando e la pagina.
10. **Chiusura**: il telefono a 115 px in Imbue da toccare, email e indirizzo con la mappa; "Un organo nuovo: che cosa mandarci" con l'email composta, "Writing from abroad" in inglese con la sua email composta e il modulo inglese di oggi; la foto d'archivio delle maestranze con la famiglia in una riga.
11. **Piede** (inchiostro): logotipo corsivo dalla maschera della newsletter 2020, sede con la mappa, contatti, sito, Altrove (Instagram, YouTube, Facebook, English, Русский), P.IVA, Maestro d'Arte e Mestiere 2020, Privacy e cookie.

## Caratteri e colore

- **Imbue** (Tyler Finck, SIL OFL 1.1, file variabile con asse ottico) solo nei tre momenti forti: titolo d'apertura (207 px a 1440, 109 a 390), "Trompette en chamade" (215 / 82), telefono della chiusura (115 / 60). Bodoniano stretto: in "Organi a canne" le aste stanno in fila come le canne di una facciata.
- **Wix Madefor Text** (Dalton Maag, SIL OFL 1.1) per tutto il resto: `h2` 42 / 28 in peso 500, manifesto 45 / 25, testo 18 / 17, didascalie 15. Nessun corsivo, nessun maiuscolo spaziato, nessuna etichetta o numero sopra i titoli (gli anni del restauro stanno sulla riga del nome).
- Registro: riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Imbue è la seconda home su 45 (l'altra è Tacchificio Riviera, altra zona, con un altro testo); Wix Madefor Text nessuna. Nessuna delle due è nelle liste di `_metodo/CARATTERI-E-SEGNALI-IA.md`.
- Colori: pietra #F2EEE6, inchiostro #1A1511, mogano sipo #3D170E (solo la firma), ottone #D9B56E sul mogano e #7A5A1E sulla pietra, stagno #6B655D per i testi secondari.

## Movimento

- Gesto: `data-he-scale` con `data-he-scale-zoom="1"` (nessun ingrandimento: la foto è del 2005, 1597 px) e `data-he-split data-he-subito` sul titolo.
- Sostegno 1: `data-he-split` sul titolo della firma. Sostegno 2: `data-he-parallax="0.05"` su Boteå, l'unica foto larga di un luogo.
- Testata che si nasconde scendendo da 900 px in su; sul telefono resta, con il numero. Nient'altro: niente sipario, indice, prima e dopo, racconto con foto ferma, galleria fissata, dissolvenze. Bottoni che si invertono di colpo, senza transizioni né opacità.
- Due eccezioni al kit, scritte nello `<style>` della pagina: sotto i 900 px l'apertura non è a tutta altezza (titolo, testo, poi la foto ritagliata 4:5); la banda di Boteå usa `top:-8%` e `height:116%` invece del `margin-top:-12%` del kit, perché un margine in percentuale si calcola sulla larghezza e su un contenitore largo taglia la cima della foto (vedi problemi aperti).

## Foto usate

Tutte della Fratelli Ruffatti, riscaricate il 7/11/2026 dalla libreria media di WordPress (`/wp-json/wp/v2/media`, 453 voci, le varianti più grandi) in `assets/originali/wp/`; anche le schede PDF e le newsletter sono state aperte (`assets/originali/pdf/`), ma non contengono foto più grandi. Nessuna foto di repertorio, nessuna immagine generata. Un trattamento solo (`immagini.py`): bianco a metà verso il grigio, colore 0,82, una curva dal nero inchiostro al bianco pietra, grana del kit a 0,14.

| In pagina | File originale | Misura nativa | Mostrata a 1440 / 1920 |
|---|---|---|---|
| Apertura, Aguascalientes in falegnameria | `2016_04_falegnami-21.jpg` | 1597x1198 | 1440 (0,90) / 1920 (1,20); telefono: ritaglio 900x1125 |
| Il legname | `2016_03_xFoto-Sipo-2.jpg` | 800x544 | 648 / 794 |
| La lastra | `2016_04_xFusione-6modif.jpg` | 800x798 | 648 / 794 |
| Canne ad anima | `2016_04_xOFFSETS-95MODIF.jpg` | 800x905 | 536 / 657 |
| Noci tornite | `2016_04_xImmagine-006.jpg` | 640x512 | 536 / 657 (1,03) |
| Canna ad ancia smontata | `2016_04_xtrompette3.jpg` | 800x603 | 800 / 800 (1,0) |
| Trombe di Uppsala | `2016_04_xDSC_00860001.jpg` | 800x532 | 760 / 931 (1,16) |
| Saldatura del padiglione | `2016_04_xchamades-sald.jpg` | 576x485 | 424 / 520 |
| Boteå, a tutta pagina | `2018_11_P1270600-1.jpg` | 3264x2448 | 1440 / 1920 (file da 1920) |
| Uppsala intera | `2016_02_home-ruffatti2.jpg` (la `home-ruffatti4` ha 245 px di bianco a sinistra) | 900x1600 | 536 / 657 |
| Restauro: La Valletta, Vallicella, Corinaldo, Isera, Cobh | `xDSC_0011`, `xP1050744`, `xFile0149`, `xFile0145`, `xP1070186` | 800 di larghezza (Cobh 800x600, ritaglio 450x600) | 244 / 301, ritagli 2:3 |
| Maestranze, archivio | `2016_03_storia1-575.jpg` | 900x575 | 424 / 520 |
| Logotipo | maschera a 1 bit 5024x1172 della newsletter 2020 | | PNG 360 in testata, 960 nel piede |

Nessuna foto oltre 1,25 volte la sua larghezza nativa: la peggiore è l'apertura a 1920 (1,20).

## Misure e prove (sezione 6)

- **Scorrimento orizzontale e errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento": larghezza del documento uguale alla finestra, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma; testo identico con e senza movimento (6.808 caratteri a 1440, 6.740 a 390), nessun elemento nascosto. L'apertura resta incorniciata con la didascalia a sinistra sotto il nome.
- **Peso al primo caricamento** (rete a riposo, senza scorrere): 550 KB a 1440 e 422 KB a 390 (soglie 2,5 e 1,5 MB); 497 a 768, 467 a 1024, 593 a 1920. Foto d'apertura e due caratteri precaricati, con `media` diverso per telefono e schermo; tutte le altre immagini pigre.
- **Layout stabile**: CLS 0 a tutte e cinque le larghezze, con e senza movimento (tutte le immagini hanno larghezza e altezza).
- **Altezza**: 12.504 px a 1440 con l'apertura fissata, 11.514 fermi; 12.978 a 390. 983 parole in `main`.
- **Segnali da IA** (`segnali.sh`, 18 soglie): 0 bloccanti; area delle foto 35,4%, 23 filetti, nessuna etichetta sopra i titoli, nessun titolo col punto, una sola famiglia di testo. Resta "da guardare" il numero di fasce di fondo (6: pietra, mogano, pietra con Boteå, restauro, pietra, piede).
- **Funzioni**: 5 link `tel:` (testata fissa compresa), 5 `mailto:` di cui 3 con oggetto e traccia (organo nuovo, restauro, in inglese), 3 link alla mappa, modulo inglese di oggi, P.IVA, Privacy e cookie, EN e RU.
- **Controllo d'uso dal telefono** (`uso.mjs`, 390x844): nella prima vista ci sono il numero (testata), "Organi a canne", il mestiere e via Facciolati 166 con la mappa; tutte le aree di tocco sono di almeno 44 px; il menu si apre, porta al restauro e si chiude; a metà pagina il numero è ancora in testata.
- U+2014: nessuno, nella pagina, negli script, nella direzione e in questa nota.

## Giudizio da solo (griglia della sezione 7)

Guardati `foglio-1440.jpg`, `foglio-390.jpg`, le prime schermate e cinque fotogrammi a piena misura estratti dal video a 1440 (1 s apertura, 5 s apertura aperta, 13 s firma, 16 s Boteå, 23 s chiusura) e tre a 390, accanto alle prime schermate di Rieger, Fisk, Knupfer e Artisans de Genève.

- **Design 7,8**: idea leggibile, tipografia con un solo carattere forte usato tre volte, impaginazioni diverse sezione per sezione, un trattamento solo. Il limite è la qualità delle foto: compatte del 2005-2016, 800 px, neon; la falegnameria a tutta pagina regge come documento, non come servizio fotografico.
- **Creatività 8,2**: il gesto è la cosa vera (dalla chiesa apparente al laboratorio), la firma è un registro con la sua prova, lo stacco della canna alla misura vera, i luoghi in forma di disposizione fonica.
- **Usabilità 8,5**: numero sempre in testata, "Scriveteci" e EN in prima vista, restauro a un tocco, indirizzo con la mappa, nessuna sezione fissata sul telefono, la fila del restauro si sfoglia col dito.
- **Contenuto 8,5**: fatti precisi con fonte (61 trombe a Uppsala, 95% di stagno, sipo stagionato cinque anni, 1579-1904, The Diapason 2022), testi loro.

Media pesata circa 8,1. Correzioni fatte dopo questo giro di sguardi: titolo della firma portato a tutta griglia; foto della materia ingrandite fino alla misura nativa; banda di Boteå aggiunta (e parallasse spostata su di lei da Uppsala, che è alta); Uppsala nella proporzione nativa; righe vuote tra testo e disposizione tolte; didascalia ferma dell'apertura spostata a sinistra per non toccare il titolo a 1280x720; bottoni dell'apertura diventati collegamenti; aree di tocco a 44 px; titolo in due frasi diviso.

## Problemi aperti

- **Foto**: da qui viene circa due terzi della distanza dall'8,5. Tutto il laboratorio è a 800 px, compatta e flash; la falegnameria a 1920 è a 1,20; le trombe di Uppsala a 1920 a 1,16.
- **Indirizzo e mappa**: in pagina come chiede il brief (e come nel piede del loro sito), ma Homo Faber scrive "Address upon request" e "By appointment only": va confermato con loro (LEGGIMI).
- **Citazione di Frederick Swann** e foto delle installazioni (Uppsala, Boteå, i restauri): permessi e autori da chiedere (LEGGIMI 7).
- **Cobh**: in pagina c'è solo che l'organo è stato smontato e portato in laboratorio (notizia del 2016); che il restauro sia finito non è nelle fonti.
- **Callido**: l'anno dell'organo di Corinaldo non è nelle fonti; nella fila c'è "Settecento", che è il secolo dell'autore secondo la loro pagina.
- **Concorso**: "biennale" sulla pagina italiana, "triennial" nel bando 2027: in pagina nessuno dei due.
- **Numeri** (oltre 500 in Italia, oltre 50 negli USA, oltre cento restauri, "da mezzo secolo"): da confermare, quindi fuori dalla pagina.
- **Inglese**: le righe del mestiere, della premontatura, del manifesto, della firma e dei contatti sono in inglese (dal loro sito inglese); una home inglese intera non c'è e EN porta al sito inglese di oggi.
- **Русский** nel piede è nel carattere di sistema: i file dei caratteri sono solo latini.
- **Kit**: `.he-parallax > img{margin-top:-12%}` in `he.css` si calcola sulla larghezza del contenitore: su una banda larga taglia la cima della foto. Qui è corretto nella pagina; nel kit andrebbe `position:relative; top:-12%`.
- **Modulo**: come nella versione di oggi, le strade del contatto sono email composte; il modulo vero (con allegati) va nella pagina Contatti del sito nuovo (LEGGIMI).

## Foto da rifare (in ordine di valore)

1. **Un organo in premontaggio nella falegnameria**, di giorno, frontale, a 4000 px o più, con due o tre persone al lavoro: è il gesto d'apertura, oggi una compatta del 2005 con i neon.
2. **Le trombe en chamade** di un organo recente, dal basso e di lato, a piena risoluzione (l'originale di Uppsala, o la saldatura del padiglione rifatta in luce radente).
3. **Una canna ad ancia smontata** su fondo bianco, macro a 3000 px: lo stacco alla misura vera oggi è a 800 px.
4. **La colata della lastra e la tornitura delle noci**, con lo stesso fotografo e la stessa luce.
5. **Gli originali delle installazioni** (Uppsala, Wayne, New Orleans, Pershore) e una foto dell'organo di Pershore Abbey.
