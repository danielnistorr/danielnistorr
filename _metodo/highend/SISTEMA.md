# Sistema HE: home di fascia alta, da studio di design

Obiettivo: home che un direttore creativo di uno studio di Milano o di Copenaghen firmerebbe, all'altezza di un sito premiato su Awwwards nel settore dell'azienda. Non home "ordinate e corrette": home con un'idea, una regia e un movimento.

## 1. Perché le home di prima erano banali (da non ripetere)

- Tetti fissi (6 cliccabili, 160 caratteri, una griglia sola, 900 parole) e clienti tipo dentro il ciclo di progetto: premiavano la pagina prevedibile.
- Sezioni con lo stesso scheletro: titolo a sinistra, testo a destra, filetto, righe. Nessun cambio di scala, nessun culmine.
- Pagine ferme: nessuna regia del tempo. I siti di fascia alta si leggono anche come un film.
- Foto piccole messe grandi e trattate come in un catalogo.

Qui cambia: i tetti cadono, i clienti tipo restano solo come **controllo finale d'uso** (sotto), il movimento è ammesso con una grammatica precisa.

## 2. Vincoli che restano (del committente, non si discutono)

- Mai: gradienti viola-blu, testo sfumato, emoji nei titoli, Inter, schede con il bordo sinistro colorato, vetro smerigliato, tema scuro a basso contrasto, tre riquadri con icona in fila, etichetta sopra il titolo, icone Lucide ovunque, componenti shadcn non toccati, sezioni che compaiono in dissolvenza scorrendo, effetti che seguono il cursore, bottoni che sbiadiscono al passaggio, spazi incoerenti, lineette lunghe (U+2014), parole da agenzia, corsivi serif per le parole d'accento.
- Fatti solo dalle fonti della cartella (01-analisi, LEGGIMI, NOTA, sito di oggi). Quello che è "da confermare" non va in pagina.
- Foto: prima quelle dell'azienda. Nessuna immagine generata. Foto di repertorio con licenza libera solo per materiali e dettagli astratti (una venatura, una superficie), al massimo due, mai presentate come lavori dell'azienda, scritte in `CREDITI.md` e nel LEGGIMI come "foto indicative".
- Ogni foto alla misura vera o poco più: al massimo 1,25 volte la sua larghezza nativa sugli schermi normali. Le foto deboli si usano in cornici medie, ritagliate sui dettagli, con un trattamento unico (grana, toni) per tutta la pagina.

## 3. Direzione artistica, prima del codice

Scrivi `DIREZIONE-HE.md` nella cartella dell'azienda:
1. **La cosa vera**: una frase sul segno che solo loro hanno (un lavoro, un materiale, un gesto, una data con una prova).
2. **Riferimenti**: 4 siti di fascia alta del loro settore e 2 premiati su Awwwards in settori vicini. Guardali davvero (prima schermata e uno scorrimento), scrivi per ognuno 2 mosse da prendere. Per l'arredo: Molteni&C, Minotti, Poliform, Cassina, Henrytimi, Riva 1920, Porro, Salvatori, Hays Woodworking, Siegesmund. Per l'ospitalità e la tavola: Sambonet, Christofle, Ginori 1735, Bernardaud, Alessi, Rosenthal, Puiforcat, Jars Céramistes.
3. **Carattere**: una coppia (display e testo) da Fontshare (licenza ITF, uso commerciale libero) o da Google Fonts (OFL), registrata in `_metodo/professionale/alto/REGISTRO-CARATTERI.md` (al massimo 2 home su 45 con lo stesso carattere). Il display si usa grande davvero: almeno un titolo oltre i 140 px a 1440.
4. **Colore**: 3 o 4 colori presi dai loro materiali (legno, ottone, ferro, carta, smalto), più il nero e la carta. Un colore pieno al massimo su una sezione.
5. **Movimento**: un **gesto d'apertura** e al massimo tre movimenti di sostegno, scelti dalla grammatica (sotto) per una ragione legata al mestiere.
6. **Ritmo**: l'elenco delle sezioni con, per ognuna, uno scheletro diverso dalle altre. Una sezione "firma" che è il culmine della pagina.

## 4. Grammatica del movimento (kit `_metodo/highend/kit/`)

Tutto si compone con attributi nell'HTML: vedi l'intestazione di `he.js`. Con "riduci movimento" la pagina resta completa e ferma (è un requisito, va provato).

| Movimento | Attributo | Quando ha senso |
|---|---|---|
| Foto che si allarga dalla cornice alla pagina | `data-he-scale` | apertura su un lavoro o un luogo che merita la pagina intera |
| Titolo che sale riga per riga | `data-he-split` | il titolo d'apertura e al massimo altri due momenti di testo |
| Foto che si scopre con un taglio netto | `data-he-wipe` | lavori, quando entrano per la prima volta (non tutte le foto) |
| Parallasse leggera | `data-he-parallax` | foto larghe di luoghi, mai sui testi |
| Galleria orizzontale fissata | `data-he-horizontal` | una serie di lavori o di prodotti da sfogliare |
| Racconto con la foto ferma | `data-he-story` | un processo in passi, un materiale, una storia in date |
| Prima e dopo | `data-he-compare` | restauri, rifacimenti, trasformazioni |
| Indice con anteprima ferma | `data-he-index` | servizi o categorie |
| Nastro lento | `.he-nastro` | materiali, essenze, marchi trattati |
| Sipario d'ingresso | `data-he-intro` | solo se il marchio o il nome è il gesto (una volta per visita) |
| Testata che si nasconde | `data-he-header` | sempre, con il tema che cambia sopra le foto |

Vietato: dissolvenze in serie su ogni sezione, effetti legati al cursore, rimbalzi, rotazioni, movimenti senza motivo. Il movimento è lento e preciso (curve "expo"), mai più di uno alla volta nello schermo.

## 5. Funzioni che non si perdono

Telefono da toccare (e in testata), email, indirizzo con il link alla mappa, orari se ci sono, il modulo o la richiesta che la versione professionale aveva, i dati legali nel piede, privacy e cookie. Su telefono: niente sezioni fissate che bloccano lo scorrimento, gallerie che si sfogliano con il dito, testata compatta con il numero.

## 6. Tecnica

- Cartella nuova `<Azienda>-Sito/sito-he/` (la `sito/` di oggi resta com'è finché il committente non sceglie). Kit copiato in `sito-he/kit/` (he.css, he.js, vendor/), caratteri e immagini in locale quando la licenza lo permette.
- Prestazioni: al primo caricamento al massimo 2,5 MB a 1440 e 1,5 MB a 390; la foto d'apertura precaricata; nessuno spostamento del layout.
- Prove: a 390, 768, 1024, 1440 e 1920 nessuno scorrimento orizzontale della pagina e nessun errore di script; con `prefers-reduced-motion` la pagina è completa.
- Video: `node _metodo/highend/kit/registra.mjs http://127.0.0.1:<porta>/<Azienda>-Sito/sito-he/index.html <Azienda>-Sito/screenshot/he 1440 900` e lo stesso a 390 844. Servi il repository con `python3 -m http.server`. Il foglio dei fotogrammi è quello che guarda il giudice.

## 7. Giudizio (direttore creativo)

Guarda il foglio dei fotogrammi a 1440 e a 390, le prime schermate ferme e, per confronto, le prime schermate dei riferimenti. Voti da 1 a 10, come su Awwwards:
- **Design (40%)**: idea, tipografia, impaginazione, trattamento delle foto, coerenza.
- **Creatività (25%)**: il gesto, la sezione firma, quanto non somiglia a un modello.
- **Usabilità (25%)**: si capisce il mestiere in 5 secondi, si chiama in un tocco, il movimento aiuta e non ostacola, il telefono è progettato e non rimpicciolito.
- **Contenuto (10%)**: fatti veri e specifici, testi brevi e loro.

Soglia: media pesata almeno 8. Sotto, il giudice scrive i 5 interventi che valgono di più, in ordine, e si fa un giro di ritocco. Il giudice dice anche quanto della distanza dipende dalle foto.

Controllo d'uso finale (non un voto): un cliente tipo dal telefono deve trovare in meno di 10 secondi il numero, l'indirizzo e che cosa fanno.

## 8. Lezioni dei piloti (Bottega dell'Arte 6,7, Foralberg 7,4, Ruffatti 7,5 al primo giudizio)

- **Nitidezza, non solo pixel.** Il tetto di 1,25 misura i pixel, non la nitidezza. Prima di dare a una foto la pagina intera o la fine del gesto d'apertura, guardala al 100% a 1440: se è morbida va in una cornice media (`data-he-scale-zoom="1"`, `data-he-scale-fine="inset(...)"`). Riscarica sempre gli originali più grandi dalla libreria media del sito.
- **L'idea va nel display, mai in didascalia.** La frase che regge la pagina sta in grande, nel carattere display.
- **Il kit non è una lista.** Indice, prima e dopo, racconto con foto ferma e galleria orizzontale in fila fanno la demo del kit. Bastano un gesto e al massimo due sostegni; gli altri cambi di ritmo si fanno con scala e impaginazione.
- **Due sezioni di fila non hanno lo stesso schema.** Per esempio foto a sinistra e testo a destra due volte. Niente vuoti di mezza pagina intorno a foto piccole: o la foto cresce fino alla misura nativa, o la sezione si stringe.
- **La sezione firma è un'idea con una prova fotografica**, non il logo ingrandito.
- **Nessuna etichetta sopra i titoli**, nemmeno numeri "01" o categorie in maiuscoletto, nemmeno solo sul telefono.
- **Bottoni:** si invertono di colpo, non sbiadiscono.
- **Un solo trattamento delle foto** per tutta la pagina.
- **Carattere display solo nei momenti forti.** Gli h2 di servizio vanno nel carattere del testo.
- **Testi grandi:** un testo di 30 parole e più non va oltre i 30 px, altrimenti sembra una pagina pubblicitaria.
- **Niente sipario d'ingresso** che ritardi la pagina oltre 1 s.
- **Fatti "da confermare" fuori anche dalla prima schermata**, compresi indirizzi e date.
- **Un fornitore non si veste da maison.** "Più fashion" per un fornitore vuol dire mostrare il mestiere con la cura di una maison (disegno, prototipo, serie, misure), non pezzi con didascalie di colore da catalogo. Sotto la piega la pagina deve restare all'altezza della prima schermata.
- **Niente frasi che non vengono dalle fonti**, nemmeno di raccordo ("sulla scarpa va il nome della griffe"). Niente toni da brochure ("i sogni del cliente", "grande realtà artigiana").
- **Il gesto deve scoprire qualcosa.** Un gesto di scala su una foto già intera all'inizio è solo un cambio di sfondo: la fine del gesto mostra qualcosa che prima non si vedeva (la cornice parte stretta su un dettaglio).
- **La sezione firma non è un negozio.** Niente bottoni "acquista" o "shop" dentro il culmine; le didascalie non ripetono la stessa parola su ogni pezzo.
- **Il voto che il costruttore si dà è in media 0,7 sopra quello del giudice** (8,1 contro 7,4). Non fidarti dell'autovoto: guarda i fotogrammi a piena misura come li guarderebbe un estraneo.
- **Le foto pesano per il 40-60% della distanza da un 9.** Nella nota va sempre la lista delle foto da rifare: è materiale per vendere un servizio fotografico.
