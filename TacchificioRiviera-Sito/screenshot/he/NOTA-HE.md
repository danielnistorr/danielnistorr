# Tacchificio Riviera, home HE (7 novembre 2026, secondo giro)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (21 file più il timbro SVG). Cartella `sito-he` 0,68 MB. La `sito/` di oggi e il kit master in `_metodo/` non sono toccati. Direzione artistica in `DIREZIONE-HE.md` (questa nota la aggiorna dove il secondo giro ha cambiato qualcosa: anno, schede, mestiere, mano, storia).

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8785`, server fermato), `foglio-1440.jpg` (22 fotogrammi) e `foglio-390.jpg` (15), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` e `-390-*.jpg` (a piena misura, estratti dal video con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo il gesto), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `TacchificioRiviera-Sito`; legge `assets/originali/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`.

## Secondo giro (giudizio 7,4: "sopra la piega una maison, sotto una PMI, il mestiere non si vede")

1. **Forme (`#forme .scheda`)**: una regola sola per i sei pezzi, applicata nello script: lato lungo del pezzo (misurato senza l'ombra) a 400 px, scheda di 560, punto d'appoggio a 470 px, centrato; le ombre si spengono prima del bordo, nessun bordo toccato (l'ottone non è più tagliato). Scala: nero 1,09, viola 1,23 (sotto il tetto di 1,25), plexiglas 0,98, avorio 0,91, anima 0,98, ottone 0,83. Scheda da #EDE6D9 a #FAF8F5: il pezzo avorio si legge. Didascalie su due righe (`span{display:block}`), italiano sopra e inglese sotto, con la materia e la lavorazione dove le fonti le danno (01-analisi §1 e §4: plastica nera e sfumata, plexiglas, anima metallica, ottone a losanghe con RIVIERA e 37 incisi); per l'avorio la materia non c'è, resta "Color avorio, a calla". Tolta la riga `.fine` ("sulla scarpa va il nome della griffe", non nelle fonti). A 390 schede a 64vw, tolto "Sfogliate i pezzi con il dito": il secondo pezzo affiora a destra.
2. **Mestiere (`#mestiere`)**: tolti i filetti delle fasi. Impaginazione centrata, come una tavola: la frase del cliente, l'inglese, i due tacchi in legno al centro a misura nativa (720, ritaglio stretto: meno bianco sopra), le cinque fasi verificate in fila su cinque colonne, con il numero accanto alla fase, in grigio e sulla stessa linea; sotto, lo scopo SGS e i PDF ISO 14001 e 45001. Legno, prototipo e stiletto **non** sono messi in fila come stesso modello: il LEGGIMI lo dà da confermare.
3. **Stiletto e pezzo nero**: riesportati dagli originali con un nuovo trattamento dei neri. Il punto nero è il 2% più scuro del pezzo (20/255 nello stiletto, 33 nel nero a onda) e va all'inchiostro #161413; il resto della scala resta, e una curva (0,68) apre le ombre: si vedono la luce sul fianco del calice, il cilindro del gambo, la piastra del pezzo a onda. Puntini di polvere tolti con una mediana solo dentro il pezzo; la macchia sul gambo rifatta passando con gradualità dal tratto pulito sopra a quello sotto. WebP a qualità 90 per tutte le immagini. Controllo al 100% a 1440 e con deviceScaleFactor 2: a 400 px CSS sul retina il bordo del calice era morbido (ingrandimento 2), quindi lo stiletto ora è a 320x480 (0,8 della foto): sullo schermo normale è ridotto e nitido, sul retina riceve il file da 400 (srcset) e l'ingrandimento scende a 1,6; la punta resta sulla linea di base di "Tacchi" e il calice arriva all'altezza dell'asta della "h".
4. **La mano (`#mano`)**: cornice verticale 4:5 di 520x650 tagliata sul fiore (taglio 640x800 dallo sfondo "linee", ridotto a 0,81: i blocchi del JPEG a qualità 28 spariscono nella riduzione). Titolo, testo e inglese in un blocco solo, centrato in altezza accanto alla cornice: niente più vuoto tra titolo e testo. Tolta la frase "Realizziamo i sogni del cliente".
5. **Storia (`#storia`)**: tolta la foto con la pergamena (persona non identificata). La foto degli anni 80 è tagliata in verticale (410x512) sulle mani che reggono un tacco e sugli scaffali dei tacchi, senza volti, sotto l'anno, col bordo destro sul bordo destro del numero. Testo della fondazione, frase sulle griffe e testo del 1970 partono tutti dalla stessa colonna (955 px a 1440).
6. **Contenuto**:
   - **1945 fuori dalla pagina** (titolo, descrizione, prima schermata, numero gigante): 01-analisi §8 chiede ancora quale anno usare (1945 del marchio o 1985 della srl). Il momento grande della storia ora è **1970**, dal sito di oggi: Valentino Boldrin introduce la lavorazione delle materie plastiche, che è il mestiere certificato di oggi (tacchi in plastica stampati a iniezione). Il primo tacco in legno di Giovanni e Valentino Boldrin resta, senza anno. Lo zero di Melodrama ha la barra (anche nelle cifre minuscole); la licenza non permette di modificare il file, quindi a vista l'anno è scritto con una O maiuscola della stessa larghezza (792 unità) e per chi legge con la voce c'è "Nel 1970".
   - **Indirizzo**: il sito di oggi scrive "Viale Serenissima, 30" (contatti e privacy), i certificati SGS "Via Serenissima, 30". Le fonti non concordano, quindi in pagina c'è solo "Serenissima 30, 30030 Vigonovo (VE)" con il link alla mappa, nei contatti e nel piede: il nome della strada e il civico sono uguali in tutte le fonti, la sola parte incerta (Via o Viale) è tolta; senza il nome della strada l'indirizzo non si troverebbe.
   - Tolti i toni da brochure: "i sogni del cliente", "grande realtà artigiana". Resta la frase del sito sulle griffe, che è il "per chi" di 01-analisi §1.
   - **Telefono**: scritto in grande nei contatti (link `tel:`), di nuovo nel blocco inglese e in testata (sul telefono "Chiama"). I contatti non si ripetono più: nel blocco inglese solo email intestata in inglese, telefono e sito inglese, niente secondo indirizzo; tolti i filetti dell'elenco e il filetto nero sopra la sezione.
   - Prima schermata: "Progettiamo e produciamo tacchi per le calzature di lusso delle grandi griffe. A Vigonovo, nella Riviera del Brenta."

## Sezioni (scheletri diversi)

1. **Apertura, "Tacchi"** (carta, a tutta altezza): parola in Melodrama a tutta larghezza, stiletto a 320 px in moltiplica sulla carta, in piedi tra le due "c", didascalia da museo; in basso il mestiere in italiano, "Inviateci il disegno", il mestiere in inglese. Gesto: la parola sale, lo stiletto si scopre dal basso.
2. **Il mestiere** (carta, centrata): la frase del cliente, i due tacchi in legno, le cinque fasi in fila, lo scopo SGS.
3. **Firma, "Ogni forma è unica"** (rosso matita spento, l'unico campo pieno): galleria orizzontale fissata, sei schede da 560 con la stessa regola, didascalie di materia su due righe. Sul telefono titolo fermo sopra e pezzi a 64vw da sfogliare; con "riduci movimento" sullo schermo grande i pezzi vanno a capo in tre colonne.
4. **Seguire le linee** (carta): blocco di testo a sinistra, cornice 520x650 sul fiore inciso a destra, che si scopre da sinistra.
5. **1970** (carta): l'anno a 432 px a sinistra, il testo sulle materie plastiche a destra sulla linea di base; sotto, la foto d'archivio verticale e, nella stessa colonna di destra, il primo tacco in legno e la frase sulle griffe.
6. **Inviateci il disegno** (carta): telefono grande, email, sede operativa con la mappa, fax e PEC, "Scriveteci con il disegno"; accanto "Writing from abroad".
7. **Piede** (inchiostro): timbro chiaro, dati legali, nota sui cookie, link.

## Foto

Nessun originale più grande di quelli già noti (vedi il primo giro: provate tutte le varianti di nome e cartella). Nei metadati degli still life c'è "Copyright SHOW LUX STUDIO".

| In pagina | Originale | Misura nativa | Mostrata a 1440 |
|---|---|---|---|
| Stiletto a calice, apertura | `nascita/tacco_11.jpg` | 800x650, pezzo 209x500 | 320x480 (0,8; sul retina file da 400, 1,6) |
| Due tacchi in legno | `nascita/tacco_7.jpg` | 800x650 | 720x360 a 1,0 |
| Sei schede della firma | `nascita/tacco_2, _8, _29, _17, _22, _1.jpg` | 800x650 | 560x560, pezzo a 400 di lato lungo (0,83-1,23) |
| La mano che incide | `background/linee-desktop.jpg` (JPEG qualità 28) | 1920x1080, taglio 640x800 | 520x650 (0,81) |
| Archivio, mani e scaffali | `territorio/modal2.jpg` | 876x704, taglio 410x512 | 410 a 1,0 |
| Timbro | `logo.svg`, ricolorato chiaro | vettoriale | 104 px nel piede |

Misurato da `prove.mjs`: rapporto massimo 1,0 tra misura mostrata e file a 1440 e a 1920 (la scala 1,23 del viola è dentro il file da 560).

## Misure e prove (sezione 6)

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", nessuno scorrimento orizzontale, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (3.356 caratteri a 1440, 3.326 a 390), nessun elemento nascosto.
- **Peso al primo caricamento**: 374 KB a 1440 e 311 KB a 390 (soglie 2,5 e 1,5 MB); 407 a 768, 381 a 1024, 303 a 1920. Lo stiletto è precaricato con `imagesrcset` (260, 320, 400). Pagina intera circa 0,68 MB.
- **Layout stabile**: CLS da 0 a 0,0002 a tutte le larghezze; con la rotella a 1440, 0,00004.
- **Retina simulato** (deviceScaleFactor 2): stiletto accettabile a 320 px; le schede a 560 restano ingrandite 2 volte sul retina (limite delle foto a 800 px).
- **Controllo d'uso dal telefono**: in prima vista "Tacchi", che cosa fanno e per chi, "Inviateci il disegno", Chiama in testata; "Contatti" porta a numero, email e indirizzo con la mappa.
- U+2014: nessuno, nella pagina, nello script e in questa nota.

## Quattro fotogrammi guardati da estraneo (1440: 5,2 s il mestiere, 9,4 s le schede, 16,4 s mano e 1970, 18,2 s storia e contatti; più quattro a 390)

- Il mestiere si legge come una tavola: frase, oggetto, processo, certificato. Prima i filetti e la colonna di destra lo facevano sembrare una scheda tecnica.
- Le schede sono finalmente una serie: stessa altezza, stessa base, nessun taglio; la didascalia dice di che cosa è fatto il pezzo.
- Corretti dopo averli guardati: lo zero barrato di Melodrama (leggeva "197Ø"); la frase sulle griffe che cadeva in fondo alla colonna con un vuoto sopra (ora segue il testo della fondazione); la foto d'archivio lontana dal testo (ora sotto l'anno); "Brenta." e "da SGS." da sole a fine riga; il vuoto prima dei contatti (meno spazio in fondo alla storia).
- Resta: sotto la piega la pagina è più quieta della prima schermata, perché le sole immagini di processo vere sono i due legni e la mano; il pezzo nero a 560 sul retina è morbido.

Stima personale circa 8,0, da leggere con lo scarto medio di 0,7 che il SISTEMA registra tra costruttore e giudice.

## Problemi aperti

- **Anno**: 1945 (marchio) o 1985 (società) va confermato; finché manca la risposta la pagina usa solo il 1970.
- **Indirizzo**: "Via" o "Viale" Serenissima; in pagina solo "Serenissima 30".
- **Stesso modello**: se il prototipo avorio (`tacco_17`) e lo stiletto (`tacco_11`) sono lo stesso tacco, insieme al legno, la sezione del mestiere può metterli in fila sulla stessa base: è la prova più forte che manca.
- **Didascalie**: materie da 01-analisi; per l'avorio la materia non c'è; altezze, misure (il 37 dell'ottone) e nomi dei modelli vanno chiesti.
- **Lavorazioni in casa**: metallo, plexiglas e incisione sono interni o di fornitori? La pagina non lo dice.
- **Permessi**: foto dello studio Show Lux, foto d'archivio (persona di spalle non nominata), mani dell'incisione.
- **Privacy e cookie**: Privacy porta al loro documento Word; per i cookie c'è una nota nella pagina. Servono pagine HTML vere.

## Foto da rifare (in ordine di valore)

1. **Gli originali del servizio still life** di Show Lux Studio: gli stessi 17 pezzi a 4000 px. Le schede diventano nitide sul retina senza cambiare la pagina.
2. **Processo, alla stessa luce degli still life**: il legno segnato a matita rossa, il prototipo e il pezzo di serie dello stesso modello, in fila sulla stessa base. È la foto che fa vedere il mestiere (disegno, prototipo, serie) e che oggi manca.
3. **Lo stiletto a calice nero** a 4000 px, a 90 gradi con un obiettivo lungo, esposto per leggere il nero e la luce sul calice.
4. **Il disegno**: il disegno del cliente accanto al tacco finito, e lo schermo del progetto senza persone.
5. **La pressa a iniezione e il finissaggio**, con il permesso delle persone.
6. **Il piano inciso dell'ottone "RIVIERA 37"** in macro, con luce radente.
7. **L'incisione del fiore** a 6000 px (l'originale dello sfondo "Linee"), verticale.
8. **Le foto d'archivio** scansionate dagli originali a 1200 dpi, con nomi e date.
