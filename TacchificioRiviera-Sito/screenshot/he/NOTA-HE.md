# Tacchificio Riviera, home HE (7 novembre 2026)

Pagina: `sito-he/index.html`, con il kit copiato in `sito-he/kit/` (he.css e he.js identici a `_metodo/highend/kit/`, vendor senza Flip), i caratteri in `sito-he/fonts/` (woff2 ufficiali Fontshare, licenza ITF in `FFL-ITF.txt`), le immagini WebP in `sito-he/img/` (22 file più il timbro SVG). Cartella `sito-he` 0,7 MB. La `sito/` di oggi non è toccata. Direzione artistica in `DIREZIONE-HE.md`.

In questa cartella: `scorrimento-1440.mp4` e `scorrimento-390.mp4` (registrati con `_metodo/highend/kit/registra.mjs`, repository servito con `python3 -m http.server 8783`, server fermato), `foglio-1440.jpg` (21 fotogrammi) e `foglio-390.jpg` (15), i fotogrammi uno al secondo, `fotogrammi-pieni-1440-*.jpg` e `-390-*.jpg` (fotogrammi a piena misura estratti dal video con ffmpeg), `prima-schermata-1440.jpg` e `-390.jpg` (con il movimento, dopo il gesto), `riduci-movimento-1440-prima-schermata.jpg` e `-390`.

Rifare: immagini con `python3 -I _prova/he/script/immagini.py` (dalla cartella `TacchificioRiviera-Sito`; legge `assets/originali/`, fuori da git); prove della sezione 6 con `node _prova/he/script/prove.mjs <url>` (uscita in `_prova/he/prove-finale.json`); spostamenti del layout con la rotella `node _prova/he/script/cls2.mjs <url> 1440 900`; prime schermate con `node _prova/he/script/prima.mjs <url> screenshot/he`; riferimenti con `node _prova/he/script/riferimenti.mjs _prova/he/riferimenti nome=url ...`.

## Idea

**Il tacco come oggetto di moda.** La pagina mostra i pezzi come le maison mostrano le loro scarpe: da soli, alla misura della foto, in mezzo a molto spazio, sotto una tipografia forte. Si apre con la parola "Tacchi" a 461 px e lo stiletto a calice nero, alla sua misura nativa, in piedi sulla linea di base tra le due "c": il gambo passa davanti alle lettere. Il culmine è la loro frase "Ogni forma è unica", con la prova: sei pezzi della loro galleria che passano uno dopo l'altro su schede avorio, in un campo rosso matita spento, l'ultimo è l'ottone con RIVIERA inciso sul piano.

## Sezioni (scheletri diversi)

1. **Apertura, "Tacchi"** (carta, a tutta altezza): parola in Melodrama a tutta larghezza, stiletto in moltiplica sulla carta, didascalia da museo; in basso il mestiere in italiano, "Inviateci il disegno", il mestiere in inglese. Gesto: la parola sale, lo stiletto si scopre dal basso, dalla punta al piano ("seguire le linee").
2. **Il mestiere**: "Il cliente presenta un disegno con la sua idea: noi la interpretiamo e la realizziamo." in Synonym a 52 px, l'inglese sotto; sfalsati, i due tacchi in legno alla misura nativa e le cinque fasi verificate con lo scopo SGS tra virgolette e i PDF ISO 14001 e 45001.
3. **Firma, "Ogni forma è unica"** (rosso matita spento, l'unico campo pieno): galleria orizzontale fissata, titolo in Melodrama a 193 px che sale riga per riga, sei schede da 560 px con forma e materia in italiano e inglese, la riga finale sull'ottone. Sul telefono il titolo resta fermo sopra e i pezzi si sfogliano col dito; con "riduci movimento" sullo schermo grande i pezzi vanno a capo in tre colonne.
4. **Seguire le linee**: titolo in alto e testo in basso in una colonna stretta, la mano che incide un fiore su un tacco in metallo (bianco e nero, 840x630) che si scopre da sinistra.
5. **1945**: l'anno a 432 px in Melodrama, la fondazione accanto (Giovanni e Valentino Boldrin, il primo tacco in legno); due foto d'archivio sfalsate; 1970 e la frase sulle griffe.
6. **Inviateci il disegno** (filetto nero sopra): telefono grande, email, sede operativa con la mappa, fax e PEC, bottoni "Scriveteci con il disegno" (email con oggetto, come nella versione di oggi) e "Chiamate"; accanto "Writing from abroad" in inglese, con l'email già intestata in inglese.
7. **Piede** (inchiostro): timbro chiaro con la firma Valentino Boldrin, ragione sociale, sedi, P.IVA e C.F., REA, capitale; nota sui cookie; Privacy, Cookie, Whistleblowing (procedura, privacy), English.

## Caratteri e colore

- **Melodrama** 300 (Shaily Patel, ITF, Fontshare) solo nei tre momenti forti: "Tacchi" (461 px a 1440, 133 a 390), "Ogni forma è unica" (193 / 74), "1945" (432 / 120). **Synonym** 400 e 500 (Hugo Dumont, ITF, Fontshare) per tutto il resto: `h2` di servizio 52 / 30, testo 18 / 17, didascalie e inglese 14-16. Nessun corsivo, nessuna etichetta sopra i titoli, maiuscolo spaziato solo nel marchio in testata. Riga aggiunta a `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (nessuna altra home con queste famiglie).
- Carta #F2EFEA, inchiostro #161413 (16:1), grigio #625C56 (5,7:1), rosso matita #A3322A per fuoco e pressione (6,0:1), rosso matita spento #5C1F18 pieno solo nella firma (testo #F4E9E2 a 10,6:1, inglese a 5,4:1), avorio #EDE6D9 per le schede.

## Foto

Riscaricate il 7/11/2026 da tacchificioriviera.it in `assets/originali/` (fuori da git, 47 file): i 17 still life della galleria, gli sfondi delle sezioni nelle tre misure, le tre foto della storia, le miniature del menu, il logo. **Originali più grandi: nessuno.** Provati i numeri della galleria da 1 a 40 (esistono solo i 17 della pagina), le varianti senza misura o grandi (`-big`, `_large`, `@2x`, `-hd`, `.png`, `.webp`, cartelle `big/`, `large/`, `hd/`, `original/`, `originali/`, `full/`, `zoom/`), le varianti degli sfondi (`-hd`, `-2x`, `-large`, `-full`, `-4k`, `-retina`, `.png`), gli indici delle cartelle (404) e la versione inglese (`/en/app/...` risponde con la pagina, non con le foto). Gli sfondi desktop di home, territorio, unico e certificazioni rispondono 404. Nei metadati degli still life c'è "Copyright SHOW LUX STUDIO" (Photoshop CC 2015): è il fotografo a cui chiedere i file del servizio.

| In pagina | Originale | Misura nativa | Mostrata a 1440 / 1920 |
|---|---|---|---|
| Stiletto a calice, apertura | `nascita/tacco_11.jpg` (macchia sul gambo tolta) | 800x650, pezzo 209x499 | 400x600 a 1,0 (telefono 260, ridotta) |
| Due tacchi in legno | `nascita/tacco_7.jpg` | 800x650 | 720x420 a 1,0 |
| Sei schede della firma | `nascita/tacco_2, _8, _29, _17, _22, _1.jpg` | 800x650 | finestre 560x560 a 1,0 (telefono 320, ridotte) |
| La mano che incide | `background/linee-desktop.jpg` (JPEG qualità 28) | 1920x1080, taglio 1000x750 | 840x630 (0,84), sullo schermo 760 |
| Archivio, tacco in mano davanti agli scaffali | `territorio/modal2.jpg` | 876x704 | 640 (0,73) |
| Archivio, pergamena e statuetta | `territorio/modal1.jpg` | 488x562 | 313 (0,64) |
| Timbro | `logo.svg`, ricolorato chiaro | vettoriale | 104 px nel piede |

Trattamento unico (`immagini.py`): still life a colore con il campo piatto (un polinomio stima la luce del fondo e la toglie: fondo bianco puro, ombra corta conservata), neri all'inchiostro, in moltiplica sulla carta o sull'avorio; mani e archivio in bianco e nero con la stessa curva (nero inchiostro, bianco carta) e la stessa grana, che copre i blocchi del JPEG. **Nessuna foto oltre 1,0 della misura nativa** (misurato da `prove.mjs`: rapporto massimo 1,0 a 1440 e a 1920). Nessuna foto a tutta pagina, nessuna immagine di repertorio, nessuna immagine generata.

## Misure e prove (sezione 6)

- **Scorrimento orizzontale ed errori**: a 390, 768, 1024, 1440 e 1920, con e senza "riduci movimento", larghezza del documento uguale alla finestra, nessun elemento oltre il bordo, nessun errore di script, di console o di rete (`_prova/he/prove-finale.json`). Testata provata anche a 320, 360 e 414: nessun elemento fuori (sotto i 380 px esce "Contatti", restano EN e Chiama). Le due registrazioni non hanno errori.
- **Riduci movimento**: pagina completa e ferma, stesso testo con e senza movimento (3.406 caratteri a 1440, 3.398 a 390), nessun elemento nascosto; la galleria va a capo in tre colonne sullo schermo grande.
- **Peso al primo caricamento** (rete a riposo, senza scorrere): 354 KB a 1440 e 302 KB a 390 (soglie 2,5 e 1,5 MB); 392 a 768, 421 a 1024, 354 a 1920. Stiletto e due caratteri precaricati (con `media` diverso per telefono e schermo), tutte le altre immagini pigre. Pagina intera con tutte le foto: circa 0,7 MB.
- **Layout stabile**: CLS 0 o 0,0003 a tutte le larghezze, con e senza movimento, anche scorrendo con la rotella. Il fissaggio della galleria con `position: fixed` dava 1,99 (uno spostamento di 1,0 all'inizio e alla fine): nella pagina, prima di `he.js`, `ScrollTrigger.defaults({ pinType: "transform" })`.
- **Funzioni**: `tel:` in testata (anche sul telefono, "Chiama", area di 44 px) e tre volte nei contatti; email generale, email con oggetto in italiano e in inglese, PEC; sede operativa con Google Maps in italiano e in inglese; sede legale, P.IVA, REA, capitale nel piede; Privacy (il loro documento), Cookie (nota nella pagina: nessun cookie, nessuna statistica, caratteri e immagini dal sito), whistleblowing, sito inglese. Orari: l'azienda non li pubblica.
- **Controllo d'uso dal telefono**: in prima vista "Tacchi", che cosa fanno e per chi, "Inviateci il disegno", Chiama in testata; "Contatti" in testata porta all'indirizzo con la mappa in un tocco.
- U+2014: nessuno, nella pagina, negli script, nella direzione, nel registro e in questa nota.

## Giudizio da solo (griglia della sezione 7)

Guardati il foglio a 1440 e a 390, le prime schermate e sei fotogrammi a piena misura dal video a 1440 (1,2 s il gesto a metà, 3 s apertura, 7,4 s ingresso della firma, 11 s pezzi, 14,6 s la mano, 17,4 s storia e contatti) e tre a 390, accanto alle prime schermate di Manolo Blahnik, Aquazzura, Pierre Hardy, PrimeAsia e House of Corto.

- **Design 8,0**: un'idea leggibile da sola nella prima schermata (la parola e il pezzo), un display vero usato tre volte, impaginazioni diverse, un trattamento delle foto. Limiti: il mestiere e i contatti sono corretti ma più ordinari del resto; gli still life a 800 px restano morbidi sugli schermi retina.
- **Creatività 7,8**: lo stiletto in piedi sulla linea di base tra le lettere è la mossa che non somiglia a un modello; la firma è una galleria orizzontale, tipologia nota, salvata dalla regola della serie (stessa finestra, stessa linea d'appoggio) e dal campo pieno.
- **Usabilità 8,4**: il mestiere in cinque secondi, il numero sempre in testata, il contatto in inglese, il movimento breve, il telefono progettato (titolo fermo sopra la galleria, pezzi a portata di dito).
- **Contenuto 8,2**: frasi loro (Ispirazioni, Unico, Linee, la storia), lo scopo SGS, 1945 e 1970, niente fatti da confermare.

Media pesata circa 8,1. Correzioni fatte dopo aver guardato i fotogrammi: la moltiplica dello stiletto non funzionava dentro il taglio (rettangolo bianco: spostata sul contenitore del taglio); la didascalia dello stiletto copriva una "c" (portata accanto al calice); il titolo della firma andava su tre righe e si tagliava (larghezza calcolata sulla parola); la galleria era lunga 4.400 px con otto pezzi (ora sei: esclusi il secondo sfumato e il metallo satinato, troppo vicini ad altri); sul telefono la galleria mostrava solo il titolo (ora titolo fermo e pezzi sotto); CLS 1,99 del fissaggio (ora 0); con "riduci movimento" sullo schermo grande la galleria non si poteva sfogliare (ora va a capo); le fasi con le etichette inglesi a destra sembravano una scheda tecnica (tolte); la frase della firma ripeteva il titolo; il testo della mano lasciava un vuoto sopra (titolo in alto, testo in basso); la riga sull'ottone diceva in generale che il nome sta sul piano (ora parla di questo pezzo); "Contatti" in testata sul telefono e aree di tocco di 44 px.

Quanto della distanza da un 9 dipende dalle foto: circa metà. L'impaginazione regge proprio perché le foto sono mostrate piccole; con gli originali del servizio a 4000 px i pezzi potrebbero crescere, essere nitidi sul retina e la firma potrebbe diventare a tutta altezza.

## Problemi aperti

- **Indirizzo**: in pagina "Viale Serenissima 30" (pagina Contatti del loro sito e mappa incorporata di Google); i certificati scrivono "Via". Solo nei contatti e nel piede, non nella prima schermata. Da confermare (LEGGIMI).
- **Didascalie dei pezzi**: forma e colore come si vedono ("Nero opaco, a onda", "Color avorio, a calla"); materie, altezze in millimetri e nomi dei modelli vanno chiesti. La materia dello stiletto d'apertura non è scritta (da confermare).
- **Retina**: gli still life sono a 1,0 a densità 1; sugli schermi 2x il browser li raddoppia e restano morbidi.
- **Riga sull'ottone**: "Sull'ottone, RIVIERA è inciso sul piano" si vede nella foto; se l'azienda incide il nome su tutti i pezzi, la riga può diventare il titolo della firma.
- **Privacy e cookie**: Privacy porta al loro documento Word; la loro pagina dei cookie non esiste (link vuoto), qui c'è una nota nella pagina. Servono pagine HTML vere.
- **Inglese**: righe del mestiere, della fondazione, della firma, didascalie e contatti in inglese; una home inglese intera non c'è, EN porta ai contatti inglesi e "English" al sito /en di oggi (con refusi).
- **Caratteri ITF**: la licenza permette di ospitarli ma non di ridurli: i tre file pesano 68 KB in tutto.
- **Permessi**: foto dello studio Show Lux, foto d'archivio (persone non nominate), mani dell'incisione.

## Foto da rifare (in ordine di valore)

1. **Gli originali del servizio still life** di Show Lux Studio (nei metadati): gli stessi 17 pezzi a 4000 px. È il guadagno più rapido: stessa luce, stesso fondo, la pagina resta uguale e diventa nitida sul retina.
2. **Se non ci sono, un servizio still life nuovo** sullo stesso fondo chiaro, a 4000 px, con la camera alla stessa altezza e distanza per tutti i pezzi (così stanno davvero alla stessa scala), 8-12 pezzi scelti con l'azienda, con nome del modello, materia e altezza per le didascalie.
3. **Lo stiletto a calice nero** per l'apertura, a 4000 px, a 90 gradi con un obiettivo lungo, esposto per leggere il nero.
4. **Il piano inciso dell'ottone "RIVIERA"** in macro, con luce radente: può diventare la prova della frase sul nome.
5. **L'incisione del fiore** a 6000 px (l'originale dello sfondo "Linee"), più un taglio verticale per il telefono.
6. **Le due foto d'archivio** scansionate dagli originali a 1200 dpi, con nomi e date.
7. Per una pagina futura sul processo: la pressa a iniezione e il controllo dei pezzi, con il permesso delle persone.
