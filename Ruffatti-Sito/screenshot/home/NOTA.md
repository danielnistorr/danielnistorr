# Fratelli Ruffatti, home

## Alto livello, prova della sezione D (3/11/2026)

Richiesta: "non è ancora super professionale" (giudice da agenzia a 6). Regole: sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (cap. 4), che vince su A e C; direzione artistica in `_prova/alto/DIREZIONE.md` (modello N, il nome come immagine). La home di prima, intera e con i suoi screenshot, è in `_prova/versione-pro/`.

Pagina: `sito/index.html` riscritta da capo, statica, si apre con file:///. Alta 5.961 px a 1440 e 7.038 a 390. Peso 498 KB in 16 file (pagina, un carattere, 14 immagini WebP). Screenshot in questa cartella, stessi nomi di prima: home-1440, home-1024, home-768, home-390, home-320 (pagine intere), le prime schermate a 1440, 1024, 768, 390 e 320, chiusura-1440.

### Che cosa è cambiato

- **Apertura.** Il logotipo corsivo "Fratelli Ruffatti" in ottone #D4B06A a 1120x246 sul mogano #3E1406 (358x79 a 390), dentro l'`h1` con la loro riga "Costruttori e restauratori d'organi a canne" (40/48 a 1440: la direzione diceva 32, l'ho alzata come prevede il suo rischio 1, perché nella miniatura a 300 px a 32 px il mestiere non si leggeva). Sotto, "Padova, dal 1940" in maiuscoletto; in basso a sinistra la didascalia "Il nome della targhetta d'ottone / sulle consolle dei nostri organi". Ai due bordi le due coppie di filetti d'intarsio in CSS, che scendono per tutta la pagina. Niente foto nella prima schermata a 1440.
- **Testata**: Organi nuovi, Restauro, Ascolta, EN, il numero (testo a 1440, bottone bordato a 390) e un solo bottone, "Scriveteci". A 390 il menu è un `<details>`: funziona anche senza script.
- **Culmine (sezione 2, alta 1.488 px)**: "Da Padova abbiamo raggiunto negli anni tutti i continenti." e la riga sui Paesi del ventunesimo secolo, poi l'organo della Uppsala Cathedral (900x1600) a 540x960, con "Uppsala Cathedral, Svezia / 2009 · quattro manuali · trasmissione elettrica" (dalla loro scheda PDF). A 390 la foto viene prima del titolo ed entra nella prima schermata.
- **Organi nuovi**: la riga del mestiere e il link alle 86 opere significative; un indice di tre strumenti dal 2022 (Pershore Abbey 2023, con i dati "secondo Pershore Abbey" e il link alla loro pagina; Notre Dame Seminary e Santa Caterina da Siena 2022, con "La notizia"); la serie di quattro organi in 4:5 con la didascalia a due voci (New Orleans, Wayne, Buckfast 2017, Boteå contratto del 2015); la riga Ascolta con «I Principali cantano.» di Joyce Jones (Baylor University) e tre link.
- **Laboratorio**: "Costruiamo ogni componente possibile in laboratorio / dai somieri alle canne ad anima e ad ancia, fino ai particolari più minuti.", la famiglia con i nomi, la foto d'archivio, e quattro passi numerati in 3:2 con il nome tecnico (Il legname, Lastre per canne, Canne ad anima, Canne ad ancia), ognuno verso la sua pagina. Le righe vengono dalle pagine loro, scaricate il 3/11/2026 in `_prova/alto/fonti/` (API WordPress).
- **Restauro** (unico fondo pietra): la foto vera della targhetta, che chiude il gesto dell'apertura; "Restauro filologico di organi antichi" e la frase dei costruttori restaurati con l'elenco aggiornato al 2020; due link.
- **Scriveteci**: tre strade (Un organo nuovo con il mailto e la traccia; Un restauro o un organo Ruffatti in chiesa con "Chiamate 049 750 666" e "Scrivete con le foto"; Per gli organisti con il Concorso di Miami in una frase). Il modulo esce dalla home (D12): va nella pagina Contatti.
- **Piede** come biglietto da visita: logotipo, frase-firma, sede con "Indicazioni", telefono ed email, pagine, social, English e Русский, P.IVA, Maestro d'Arte e Mestiere 2020, Cookie.
- **Tolti**: la frase con le cifre del 2016, il secondo bottone dell'apertura, l'email e "che cosa mandarci" in apertura, i due ingressi descritti, la riga degli ultimi strumenti, la fascia di sei cifre, la fascia della citazione di Michela e la sua seconda citazione (permesso da chiedere), due delle tre testimonianze, quattro dei cinque video, la fila dei quattro riconoscimenti, le tre cifre grandi del concorso, il telefono a 64 px, il modulo di dieci campi, "Visite su appuntamento". Grand Rapids e Coral Ridge escono dalla home: le loro date non hanno una fonte certa (vedi sotto).
- **Carattere**: EB Garamond 400-500 (SIL OFL 1.1), una sola famiglia, in `sito/fonts/` con `OFL-EBGaramond.txt`. Escono Gambetta e Switzer. Nessun corsivo in pagina: il corsivo è solo il logotipo.
- **Foto**: 11 più il logotipo, tutte loro, in WebP, mai ingrandite, con lo stesso trattamento (`_prova/alto/script/alto_img.py`: colore 0,88, bianco a metà strada verso il neutro, curva calda leggera, luminosità verso 118; l'archivio in bianco e nero). Tre formati: 9:16, 4:5, 3:2.

### Esito delle regole D

Misure con `_prova/alto/misura-d.mjs` (esteso da `alto/diagnosi/misure/vp.mjs` e `misura.mjs`); uscita in `_prova/alto/misura-d.txt` e `misura-d.json`. Le misure "prima" vengono dalla diagnosi (`alto/diagnosi.md` e `diagnosi/misure/nostre-*.json`) e, dove serve, dallo stesso script lanciato sulla copia in `_prova/versione-pro/` (`misura-d-prima.txt`).

| Regola | Prima | Dopo | Esito |
|---|---|---|---|
| D1 idea e gesto | il logotipo sotto la piega | il logotipo d'ottone è l'apertura e torna con la foto della targhetta nel restauro | scritto in DIREZIONE; la prova con tre persone sulla miniatura non è fatta |
| D2 foto nella 1ª schermata a 1440 | 26% (New Orleans 519x649 dalla foto di 574) | 0%; Uppsala apre la seconda a 540x960 dalla foto di 900 | passa |
| D2 foto ingrandite | nessuna | 0 su 13 immagini a 1440 e a 390 (misurati i pixel veri del file scelto dal `srcset`) | passa |
| D3 cliccabili / bottoni a 1440 | 18 / 3 | 6 / 1 (Organi nuovi, Restauro, Ascolta, EN, il numero, Scriveteci) | passa |
| D3 caratteri fuori dal menu a 1440 | 731 | 122 (172 con la testata) | passa |
| D3 cifre di 30 px nella 1ª schermata | 0 | 0 | passa |
| D3 a 390: cliccabili / bottoni / foto | 9 / 4 / 19% | 3 / 1 (la chiamata) / 56,7% (Uppsala 390x477) | passa |
| D5 famiglie | Switzer e Gambetta | 1, EB Garamond (nessuna altra home la usa) | passa |
| D5 elementi oltre 100 px | 0 (il titolo a 64 px, il logotipo sotto la piega) | 1, il logotipo | passa |
| D5 testo corrente a 1440 | 14 px nelle note, 17 nel testo | 20 px il testo, 17 il minimo (didascalie 16, piede 16-17) | passa |
| D6 occhielli sopra h1 e h2 | 6 | 0 ("Padova, dal 1940" sta sotto l'`h1`) | passa |
| D7 h1 | 6 parole | 8 parole, 0 virgole: il logotipo (alt) e la riga | passa |
| D7 lista nera, lineetta lunga | 0, 0 | 0, 0 | passa |
| D7 frase-firma | 2 | 2: apertura e piede, crema su mogano sotto il logotipo | passa |
| D7 frasi d'istruzione sopra i 14 px | "Si apre il vostro programma di posta..." | nessuna | passa |
| D8 parole | 1.083 | 568 a 1440, 554 a 390 | passa |
| D8 sezioni dopo l'apertura | 8 | 5 | passa |
| D8 bottoni in pagina | 7 a 1440, 8 a 390 | 2 e 2 | passa |
| D8 altezza a 1440 | 9.200 px | 5.961 px | passa, con 39 px di margine |
| D8 culmine di almeno 900 px | nessuno | Uppsala, 1.488 px | passa |
| D9 cifre di 30 px o più in pagina | 10 (fascia dei numeri, concorso, telefono) | 0; tre numeri del concorso in una frase | passa |
| D9 lavori con nome, luogo e anno | in parte | tutti e 8 (Uppsala, i 3 dell'indice, i 4 della serie); Boteå con l'anno del contratto | passa |
| D10 foto, formati, "indicativ" | 10 foto, 4 formati | 11 foto, 3 formati (9:16, 4:5, 3:2), 0 | passa |
| D10 un trattamento, didascalia a due voci solo su apertura e lavori | 0,8 di colore | 0,88; due voci su apertura, Uppsala, 4 lavori e targhetta | passa (la targhetta ripete la didascalia dell'apertura) |
| D11 fondi oltre al piede | 4 | 3 (mogano, carta, pietra) | passa |
| D11 sezioni col colore del marchio | 3 fasce scure (apertura, numeri, contatti) e una bordeaux (Ascolta) | 1, l'apertura | passa |
| D11 spazi tra le sezioni | 96 ovunque | 80 e 128 (culmine), 1,6 volte | passa |
| D12 tel: / "Indicazioni" / telefono grande e modulo | 5 / 0 / sì e sì | 3 (testata, contatti, piede) / 1 (piede) / no e no | passa |
| D12 contatto per bisogno | modulo unico | 3 strade, ognuna con il suo contatto | passa in parte: manca la persona e l'orario, non sono nelle fonti |
| D12 peso, video, pop-up, testo senza JS | 844 KB, 0 | 498 KB, 0, nessuno, tutto il testo c'è anche senza script | passa |
| D4 modello per zona | | N, come da tabella del capitolo 5 | si controlla sull'ondata, non sulla singola home |

**Controlli a 320, 390, 768, 1024, 1440 e 1920** (`_prova/alto/controllo.mjs`): nessuno scorrimento orizzontale, nessuna sovrapposizione di testo, nessun testo o immagine fuori dalla finestra, nessun errore di script; il telefono della testata fissa è cliccabile a metà pagina; il menu a 390 si apre (11 voci), si chiude al tocco e porta "Restauro" sotto la testata; il focus si vede (bordeaux su carta, ottone su mogano). Contrasti: crema su mogano 13,6:1, ottone su mogano 7,8:1, grigio caldo #5A4E44 su carta 7,0:1 e su pietra 6,3:1, bordeaux su carta 11:1. `tel:+39049750666` in tutti e tre i link; i tre `mailto:` hanno oggetto, e i due delle strade anche la traccia.

**Guardata accanto a Rieger, Flentrop, Robbe & Berking, Clayworks e al foglio dei 12** (`_prova/alto/giri/lontano.jpg`, `lontano-390.jpg`): da lontano a 1440 è il nome sul legno, come Knupfer con il nome a tutta larghezza; Rieger e Clayworks restano più forti perché hanno una foto da servizio fotografico. A 390 regge accanto a Rieger.

### Problemi aperti

- **Il mestiere a 1440 lo dice solo la riga sotto il logotipo**: va fatta la prova D1 con tre persone. Se non basta, la strada è far salire il bordo alto dell'organo di Uppsala nella prima schermata (sotto il 12%), non rimettere testo.
- **Le foto sono piccole**: Uppsala 900 px, i quattro lavori tra 484 e 606 px, il laboratorio a 800 px. Sopra l'8 serve il servizio fotografico (LEGGIMI).
- **Contatto senza persona e senza orario**: chi risponde e quando non è nelle fonti (LEGGIMI 6).
- **Pershore**: l'anno e i dati vengono dalla pagina di Pershore Abbey e sono scritti "secondo Pershore Abbey". Grand Rapids e Coral Ridge sono fuori dalla home finché l'azienda non dà anno e dati.
- **Il registro dei caratteri** (`_metodo/professionale/alto/REGISTRO-CARATTERI.md`) dice 32/40 per la riga dell'`h1`: in pagina è 40/48 a 1440 e 34/42 a 1024. Le misure di carattere sono sette (16, 17, 18, 19, 20, 32, 40), non tre.
- **L'altezza a 1440** passa per 39 px: se si aggiunge una riga, va tolta altrove.
- **EN** porta ancora al sito inglese di oggi.

---

## Storia: la versione "livello professionale"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh`. Alta 9200 px a 1440 e 13578 a 390, compreso il piede. Screenshot: home-1440, home-390, home-320, home-768, home-1024 (pagine intere), le prime schermate a 1440, 390 e 320, chiusura-1440.
La versione precedente ("Una canna", con la canna ad ancia smontata e il gioco Noce / Canaletto / Piede) è conservata com'era, con la sua nota, in `_prova/versione-1-originale/`.

## Livello professionale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; poi "non rappresentano bene l'identità e l'utilizzo corretto"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Ordine seguito: uso, identità, alta gamma.
Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, e le pagine intere di barth e Budri a pezzi. Scheda d'uso: `_prova/uso/SCHEDA.md`.

### Che cosa è cambiato rispetto alla versione 1

- **Via la canna smontata in apertura** e il gioco delle tre parti (la scheda d'uso le indica come cosa "da grafico": nessuno dei tre visitatori viene per un componente). Via le frasi di sintesi messe tra le loro ("Le nostre nascono in laboratorio, parte per parte", "Qui si fondono le lastre..."), le tre "misure" a metà pagina, il fondo grigio stagno #E7E8E2 e la bicromia dell'archivio, la newsletter con il modulo finto, "Apri la mappa" come invito in chiusura.
- **Apertura come la vuole la scheda.** A sinistra la loro riga "Costruttori e restauratori d'organi a canne" come titolo, l'occhiello "Padova, dal 1940", la loro frase sul primato americano ("Nell'esigente mercato statunitense abbiamo costruito oltre 50 strumenti..."), "Scriveteci" e "Chiamate 049 750 666", l'email, le due strade Organi nuovi e Restauro, e la riga "Ultimi strumenti: Grand Rapids 2026, Pershore 2023, Coral Ridge 2023". A destra l'organo del Notre Dame Seminary di New Orleans (2022) nella sua chiesa, alla misura d'origine, con didascalia di luogo, anno e manuali.
- **Struttura della famiglia M adattata.** Testata sobria con Contatti, lingue e telefono; dichiarazione di competenza con la foto; ultimi strumenti con committente, luogo, anno, manuali e registri (i progetti di barth); quattro schede dei mestieri con la foto (competenze e processi); i numeri aziendali in una fascia scura; testimonianze degli organisti con nome e istituzione e i video (Ascolta); il restauro con "Avete un organo Ruffatti?"; la famiglia con i riconoscimenti e la stampa in fascia; il concorso di Miami; i contatti con il modulo per il mestiere; il piede in quattro colonne.
- **Colori del marchio**: bordeaux del logo #6A0C10 (la scritta della targhetta sulla consolle), ottone #C29A5B delle trombe per le cifre sul fondo scuro, mogano scurissimo #1C1311 per i blocchi scuri e il testo, bianco delle chiese per il fondo. Grigi: #5A5552 (testo secondario, 7,4:1 sul bianco e 6,6:1 sul grigio chiaro), #B9B1AC (note sul mogano, 8,6:1); ottone sul mogano 7,0:1, bianco sul bordeaux 12,6:1, #E2DEDB (filetti), #F3F2F1 (blocchi chiari). Nessun beige.

### Ritocco finale (3/11/2026)

Dal controllo del livello professionale (voto 6,5) e dalle prove dei due clienti tipo (commissione americana a 1440, parroco a 390).

- **Menu a pannello riparato** (era il difetto bloccante): la riga flex ora vale solo per `.testata > .wrap`. Provato con `_prova/script/ritocco_prova.mjs` a 320, 390, 768 e 1024: sei voci in colonna alte 56 px, tutte toccabili, le lingue in fondo, filo d'ottone sotto il pannello; il tocco su "Restauro di organi antichi" chiude il menu e porta l'etichetta della sezione 31 px sotto la testata.
- **Gesto di scala e identità.** Testata e apertura su mogano, con il logo in ottone: è la scritta della targhetta d'ottone sulla consolle. L'organo bianco e oro di New Orleans stacca sul fondo scuro come il pezzo di Budri. In fondo all'apertura il logotipo corsivo a tutta larghezza (1280 px, ricavato dalla maschera a 5024 px della newsletter 2020, ripulito dai puntini della scansione) con la riga "La scritta della targhetta d'ottone sulle consolle dei nostri organi": il parroco riconosce il nome che legge sulla sua consolle. La didascalia dell'apertura è ridotta a luogo, anno e manuali.
- **Correzione di un dato.** La notizia "Nuovi organi in USA del 2022" dice che l'organo del Notre Dame Seminary è "a due manuali": la versione di prima scriveva tre. Ora c'è "Due manuali". Dalla stessa notizia il nome della chiesa di Wayne: Santa Caterina da Siena, con due consolle. Le due righe hanno il link "La notizia" alla pagina loro.
- **Foto in serie.** `pro_img.py` dà a tutte le foto a colori lo stesso trattamento: bilanciamento del bianco a metà strada verso il grigio medio, colore 0,8 (0,7 per le canne ad ancia, senza la dominante rossa), la stessa curva calda leggera, la luminosità media a metà strada verso 118. La consolle di Wayne è ritagliata più in basso e a destra (727 px): via le vetrate colorate e il soffitto.
- **Testi.** Restauro: "Restauro filologico di organi antichi, in Italia e all'estero" e "Restauriamo organi di ogni epoca e anche di altri costruttori, da Giovanni Guglielmi (Roma, Vallicella, 1612) a Gaetano Callido e Girolamo Zavarise..." (pagina Opere eseguite, aggiunta a `01-analisi.md`). Via "Da mezzo secolo", che non era datato. Nell'apertura i numeri hanno l'anno ("dati del 2016") e l'Italia viene prima degli Stati Uniti. Testimonianze con il ruolo della fonte ("già direttore della musica e organista", "già docente"). "Maestro d'Arte e Mestiere 2020" al singolare. "86 opere significative" al posto di "Tutte le realizzazioni: 86 strumenti". Nel riquadro del restauro "Organo muto, sporco o da revisionare?" (nessun servizio promesso). Citazione di Michela Ruffatti con il link a Rockit. Sotto l'email dell'apertura, a 1440, la riga su che cosa mandare con il link ai contatti.
- **Modulo.** In più "Idea di dimensione (manuali, registri, tempi del progetto)" e le caselle "Che cosa potete mandarci" (pianta della chiesa, foto della cantoria, foto della consolle e della targhetta), riportate nell'email come "Allego: ...". Il mailto del restauro dice "[Allegate qui le foto della consolle e della targhetta]".
- **Tipografia.** Pesi 400 e 600 (Switzer 600 al posto del 500). Tutti i titoletti (h3, i riconoscimenti, il riquadro della targhetta) in Switzer 600 a 22 px; Gambetta solo per h1, h2, cifre e citazioni. Il testo descrittivo passa da 16 a 17 px sopra i 640 px. L'anno dei riconoscimenti non va più a capo in grigio.
- **Ritmo.** Spazio tra le sezioni 96 px a 1440 e 64 a 390 (era 128 e 72); salti alle ancore senza il vuoto sopra l'etichetta. Piede: aree di tocco di 44 px, "La scheda" di Homo Faber su una riga sua, "Visite su appuntamento" sotto l'indirizzo.
- **EN** ha il titolo "Il sito inglese di oggi (current English site)": la home inglese non è fatta (vedi LEGGIMI).

### Le 15 regole, una per una (dopo il ritocco)

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), le prove del menu di `_prova/script/ritocco_prova.mjs`, e gli screenshot guardati a pezzi a 1440, 1024, 768, 390 e 320.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky di 89 px a 1440 e 73 a 390, bottone "049 750 666" alto 48 px bordato di bianco sul mogano. A metà pagina si vede e si tocca a 320, 390, 768 e 1024 (113x48 a 390). 5 link `tel:`; voce Contatti nel menu.
2. **Mestiere, luogo, prova, azione nella prima schermata: passa.** 1440x900: "Padova, dal 1940", H1, i numeri con l'anno, "Scriveteci" (pieno bianco) e "Chiamate 049 750 666", l'email con che cosa mandare, Organi nuovi e Restauro, gli ultimi strumenti, la foto con la didascalia. 390x844: "Chiamate 049 750 666" pieno a tutta larghezza, l'email, i due bottoni, gli ultimi strumenti, l'inizio della foto.
3. **Immagine vera nell'apertura: passa.** L'organo di New Orleans nella sua cappella, foto loro. Resta di 574 px: va chiesto l'originale.
4. **Zero repertorio: passa.** `grep -ci indicativ` dà 0 (il campo del modulo si chiama "Idea di dimensione" proprio per questo); nessun file di banche d'immagini; nessun disegno.
5. **Foto in serie: passa, con riserva.** 8 foto in 2 formati (4:5 e 4:3; il terzo formato contato dal controllo è il logotipo, che non è una foto), 2 didascalie, nessuna ingrandita, un solo trattamento. Restano scatti di anni diversi: la serie vera va fatta dal vero (LEGGIMI).
6. **Palette dal marchio: passa.** Bordeaux del logo #6A0C10, ottone #C29A5B (logo della testata, logotipo, cifre), mogano #1C1311, bianco; grigi #5A5552, #B9B1AC, #E2DEDB, #F3F2F1. Fondo del body bianco, nessun beige.
7. **Scala tipografica: passa.** 8 misure a 1440 (14, 17, 18, 22, 28, 44, 64, 96) e 8 a 390 (14, 16, 17, 20, 24, 30, 38, 48). Testo corrente 18 / 17, descrittivo 17; niente sotto i 14. H1 64 / 38, H2 44 / 30.
8. **Due famiglie con ruoli fissi: passa.** Gambetta 400 per h1, h2, cifre e citazioni; Switzer 400 e 600 per testo, titoletti e interfaccia.
9. **Servizi in schede con la foto: passa.** 4 schede 4:5 tutte cliccabili (2 colonne sotto i 1200 px).
10. **Tre tipi di prova: passa (4 su 4).** Testimonianze con nome, ruolo e istituzione; 6 numeri datati; riconoscimenti e stampa con didascalia; committenti con il nome.
11. **Lavori con un nome: passa.** 5 strumenti con committente, luogo, anno e dati; ora anche Wayne ha il nome della chiesa; foto della consolle larga 727 px (50,5 % di 1440). Mancano le foto di Grand Rapids, Pershore e Coral Ridge.
12. **Ritmo a blocchi: passa.** Su fondo pieno, oltre al piede: apertura (mogano), numeri (mogano), Ascolta (bordeaux), Contatti (mogano); Realizzazioni e Famiglia su #F3F2F1. Sezioni 96 px a 1440 e 64 a 390; margini 80 e 22.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 2 px, 56 px (48 in testata), testo 17 px (16 a 390); sul fondo scuro il pieno è bianco con il testo bordeaux. I bottoni di chiamata hanno il numero.
14. **Modulo e "dove" per il mestiere: passa.** Istituzione, ruolo, luogo, tipo di richiesta, organo di oggi, idea di dimensione, le caselle degli allegati (pianta, foto della cantoria, della consolle e della targhetta), messaggio; controllo dei campi obbligatori provato. "Vai alla mappa" nel piede, nessun iframe. Il file vero si allega quando il modulo sarà collegato a un servizio (LEGGIMI).
15. **Piede completo: non passa.** Quattro colonne, testo di almeno 14 px, indirizzo con "Visite su appuntamento" (fonte Homo Faber, da confermare), mappa, telefono, email, pagine, social con sottotitolo, lingue, P.IVA, Maestro d'Arte e Mestiere 2020, Cookie. Mancano ragione sociale completa, orari e Privacy: non sono nelle fonti (LEGGIMI 1, 2, 11).

### Compiti della scheda d'uso

- *Commissione, computer 1440*: in prima vista organi nuovi e restauro scritti (titolo e strade), Padova dal 1940, la foto di New Orleans con luogo, anno e manuali, EN in testata (porta a ruffatti.com/en/, con il titolo "Il sito inglese di oggi"), Scriveteci, il telefono, l'email con che cosa mandare, la riga degli ultimi strumenti (un clic porta alla lista). Poi i cinque strumenti 2022-2026 con manuali e registri (due con il link alla notizia), "86 opere significative" e "Gli organi restaurati". Ascolta è a un clic (menu) e i video a due. In Contatti email, telefono e "Che cosa mandarci".
- *Parrocchia, telefono 390*: bottone di chiamata a tutta larghezza e numero in testata senza scorrere; Restauro in prima vista, e ora anche dal menu (riparato); nella sezione Restauro "restauro filologico", "anche di altri costruttori" con i nomi di Guglielmi, Callido e Zavarise, circa 120 restauri con località, anno e autore, "Elenco dei restauri", la targhetta "Fratelli Ruffatti" in foto, che cosa preparare per la prima telefonata, "Chiamate 049 750 666" e "Scrivete con le foto" (email con la traccia).
- *Organista, telefono 390*: Menu, poi "Concorso di Miami" (provato: la sezione arriva in vista e il menu si chiude), primo premio US$ 5.000, under 30, "Bando e iscrizione 2027"; Instagram nella stessa sezione, YouTube in Ascolta, tutti e tre i social nel piede.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione tra testata, titolo, testo, bottoni, strade e foto dell'apertura a tutte queste larghezze. A 320 l'EN passa nel menu (nella testata non c'è posto) e i bottoni Organi nuovi e Restauro scendono appena sotto la prima vista.

### Caratteri e licenze

- **Gambetta** e **Switzer** di Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito, anche sul web), serviti dalla pagina in `sito/fonts/` (gambetta-400, switzer-400, switzer-600 in woff2; il 600 scaricato da Fontshare il 3/11/2026 in `assets/fonts/`). Sono le due famiglie della versione 1, tenute.
- **Foto**: solo loro, dalla libreria media di ruffatti.com (elenco in `assets/CREDITI.md`). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Collegamenti

- `tel:+39049750666` in testata, apertura, restauro, contatti e piede; `mailto:organs@ruffatti.com` con oggetto (e nel restauro con la traccia dei dati); il modulo compone l'email e va collegato a un servizio (LEGGIMI).
- Mappa: `https://www.google.com/maps/search/?api=1&query=Via+Facciolati+166+35127+Padova`, solo nel piede (l'indirizzo va confermato).
- Lingue: ruffatti.com/en/ e /ru/ (rispondono 200). Video: tre video del canale YouTube "Ruffatti organs" (dal feed del canale) e il canale; CD, Dicono di noi, Concorso di Miami, Opere eseguite e Procedure di restauro sono pagine del sito di oggi. Nessuna ancora senza destinazione; nessun U+2014 in pagina, nei .md e negli script.
