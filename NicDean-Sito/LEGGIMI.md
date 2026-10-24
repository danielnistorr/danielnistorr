# Nic Dean: proposta di nuova home

Proposta non richiesta di una nuova homepage per Nic Dean S.r.l., calzaturificio della famiglia Nicoletto a Villatora di Saonara (PD). Solo la home.

- **Pagina finale**: `sito/index.html`, statica, con `sito/img/` e `sito/fonts/`.
- **Screenshot e nota**: in `screenshot/home/` (nota in `screenshot/home/NOTA.md`).
- **Analisi con le fonti**: `01-analisi.md`. Prototipi e voti del giudice: `_prova/home/a` e `_prova/home/b`.
- **Rifare tutto**: `bash _prova/script/build_finale.sh`.

## Prima di tutto: verificare che l'azienda venda ancora scarpe

La home presuppone che calzaturificio e spaccio di via Lombardia 29 siano attivi. Per i registri la società oggi ha:
- ATECO 68.20 (affitto di immobili propri);
- 1 dipendente;
- 20.918 euro di fatturato nel 2025;
- la sede legale in via Emilia 2 a Padova;
- un sito fermo al 2017.

**La home si manda solo dopo un sopralluogo o una visura**, senza contattare l'azienda finché non si decide. Se lo spaccio è chiuso non c'è un cliente per questa home.

## Dati da confermare (oggi in pagina o legati alla pagina)

- **Il presente "Produciamo" e "si comprano"**: va bene solo se produzione e vendita continuano.
- **Titolo "Scarpe fatte a Villatora dal 1975"**: al posto di "Scarpe da donna", che contraddiceva il loro "Per donna, uomo e ragazzo" e non risulta dalle fonti. Il presente "fatte" vale solo se la produzione continua. Se si conferma che la produzione propria è soprattutto da donna, si può tornare a "da donna" togliendo "uomo e ragazzo" dalla sezione spaccio.
- **Mercati**: "per i negozi d'Europa e del Nord America" viene dal sito del 2017. Va confermato che sia ancora vero.
- **Spaccio**:
  - orari di oggi: il sito dice lunedì-venerdì 8-12 e 14:30-17, ma anche "aperti tutta la settimana", quindi va chiesto se c'è il sabato;
  - chiusura di agosto: la news del sito non ha anno;
  - pagamento in contanti e carta;
  - appuntamento per mail o telefono;
  - se vende ancora solo produzione propria;
  - la frase "Lo spaccio è dentro l'azienda, in via Lombardia 29": spaccio e azienda risultano allo stesso indirizzo sul loro sito, ma va confermato che lo spaccio sia nello stesso edificio.
- **La fila delle décolleté**:
  - modello e nomi dei colori;
  - se il pitone è vero o stampato;
  - se gli altri quattro sono in camoscio (la didascalia lo dice);
  - "collezione estate 2017" (galleria del loro sito) è stato tolto dalla pagina e dall'oggetto della mail: un modello di nove anni fa faceva sembrare fermo il catalogo. Se il modello è ancora in vendita, va confermato con loro;
  - il link della didascalia ora è "Chiedi se c'è in spaccio" (mailto con oggetto "Décolleté con plateau, colore arancio" e simili).
- **Fiere**: tolte dalla home (l'ultima documentata, MICAM e GDS di marzo 2012 con padiglione e stand, faceva sembrare l'azienda ferma). L'elenco va in `storia.html#fiere`, con le date vere; in home resta solo "Per negozi, fiere ed eventi" con il mailto.
- **Telefono e fax**: 049 640672 e 049 8791084 vengono dal sito. Va verificato che rispondano ancora.
- **Riga legale**: C.F. e P.IVA 02707240285, REA PD-300932, capitale 51.000 euro i.v. Vanno riscontrati con una visura. La sede legale (via Emilia 2, Padova) e la PEC nicdean@pec.nicdean.it non sono in pagina: vanno decise con loro.
- **Chi della famiglia Nicoletto guida l'azienda** e se vuole comparire.
- **Facebook "Nic Dean Shop"** (https://www.facebook.com/NicDeanShop): va verificato se la pagina esiste ancora. Se non esiste, la colonna "Seguici" si toglie.
- **Marchio NIC DEAN**: se è registrato e chi lo usa oggi.
- **Fuori dalla pagina**:
  - "Riviera del Brenta" è il loro modo di dire, ma Saonara è ai margini del distretto;
  - il refuso "Riviera del Brente" non va riportato;
  - "Lo stesso modello" non è in pagina, perché era una deduzione.

## Stato "aperto o chiuso" dello spaccio

Lo script c'è ma è **spento** (`STATO_ACCESO = false` in fondo a `sito/index.html`). Oggi la riga sotto "Orari dello spaccio" dice solo "Dal lunedì al venerdì, 8-12 e 14:30-17".
- **Quando accenderlo**: solo dopo la conferma che lo spaccio è aperto e con questi orari.
- **Cosa esclude**: il sabato, la domenica, agosto e i festivi nazionali (Capodanno, Epifania, Pasquetta, 25 aprile, 1 maggio, 2 giugno, Ferragosto, Ognissanti, 8 dicembre, Natale, Santo Stefano, e il 4 ottobre dal 2026).
- **Cosa resta da aggiungere a mano**: la festa del patrono locale e le chiusure straordinarie. Il 4 ottobre come festa nazionale dal 2026 va ricontrollato al momento di accenderlo.

## Newsletter

Nel piede c'è "Le novità dello spaccio": campo email, bottone e casella del consenso privacy.
- **Non funziona finché non si collega a un servizio** (Brevo, Mailchimp o simili) con doppio consenso. Oggi il modulo non invia nulla.
- **Testo dell'informativa**: va scritto in `privacy.html`, con il titolare, la finalità e la cancellazione.
- **Se lo spaccio è chiuso**: la newsletter si toglie.

## Pagine del sito nuovo a cui puntano i link della home

- `collezioni.html` (menu "Collezioni"), `collezioni/primavera.html`, `collezioni/estate.html`, `collezioni/autunno-inverno.html`. Le collezioni per stagione oggi sono solo link: le pagine vanno fatte con foto loro.
- `storia.html`, con l'ancora `#fiere` (l'elenco delle fiere con il loro anno, tolto dalla home).
- `spaccio.html` (orari, come arrivare, pagamenti).
- `negozi.html` (ordini per negozi, fiere, eventi).
- `privacy.html` e `cookie.html`: oggi non esistono; vanno scritte.
- Le ancore interne della home: `#spaccio` (dentro la sezione storia), `#storia`, `#negozi`, `#contatti` ("Orari dello spaccio" e "Orari e indirizzo" portano a `#contatti`, dove ci sono gli orari).

## Foto da rifare dal vero

In ordine di importanza:

1. **La fila delle décolleté in studio**, la prima di tutte. **Senza questa foto la home non si manda**: è l'unico oggetto della prima schermata e oggi non è nitido.
   - **Come**: cinque colori dello stesso modello, camoscio nuovo, fondo continuo chiaro e caldo (carta color gesso), luce morbida da sinistra e ombra corta, macchina all'altezza del plateau, almeno 4000 px di lato.
   - **Meglio ancora**: una foto per colore dalla stessa posizione, cavalletto fisso, cambiando solo la scarpa. Così il gesto delle pastiglie diventa esatto, senza confini disegnati.
   - **Perché**: la foto di oggi è 1024 px, ha segni d'uso sul camoscio ed è di autore ignoto (EXIF "Software: Google"). Le chiazze sono state attenuate con PIL e i file da 1600 e 2120 px per gli schermi 2x sono ingranditi con Lanczos e nitidezza: reggono meglio del ricampionamento del browser, ma non sono un 2x vero. Con la foto nuova (almeno 3000 px di lato) si rifanno con `build_img.py` gli stessi file (`fila-<colore>-760/1060/1264/1600/2120.jpg`), senza toccare la pagina.
2. **Macro della firma NicDean sul sottopiede**, stessa luce.
3. **Lo spaccio** in luce naturale: scaffali di scatole, il banco, una scarpa in mano a un cliente. Oggi la parte sullo spaccio è solo testo (i mocassini di repertorio sono stati tolti: accanto a "prodotte interamente in azienda" li facevano passare per loro). Se arriva una foto vera, può tornare una foto larga sotto la frase "Per donna, uomo e ragazzo".
4. **Le mani al montaggio a Villatora**: orizzontale largo (circa 1,9:1, almeno 3200 px) per la foto a tutta larghezza, più un taglio verticale 4:5 per il telefono; luce da finestra, banco e forme. Sostituisce la foto di Fernanda Simões (laboratorio fuori dall'Italia) in "Per negozi, fiere ed eventi". Se la produzione è cessata, la sostituisce una scarpa loro in studio.
5. **Una scarpa loro per la chiusura**, per esempio un tronchetto o uno stivale invernale su legno chiaro, verticale 4:5, luce calda. Sostituisce i tronchetti di Segura (Pexels), oggi tagliati stretti sul risvolto per togliere l'arco dello specchio.
6. **Una scarpa per stagione**, per le pagine delle collezioni, sempre su fondo continuo.

## Foto di repertorio in pagina (segnaposto)

Le foto non sono di Nic Dean. Autori, link e licenze sono in `assets/CREDITI.md`, con licenza verificata il 24/10/2026 (Pexels License: uso libero, attribuzione non richiesta).
- Fernanda Simões, Pexels 13524888: per i negozi (a tutta larghezza; al telefono taglio 4:5), scaldata e con gli azzurri spenti.
- José Martin Segura Benites, Pexels 27256471: la chiusura, taglio stretto sul risvolto in camoscio, scaldata.
- I mocassini di Mr Abrar visuals (Pexels 31935085) non sono più in pagina.

Nessuna compare in un'altra home della campagna. In pagina nessuna è descritta come loro.

## Caratteri

League Spartan (The League of Moveable Type, Google Fonts), SIL Open Font License 1.1, uso commerciale libero.
- **File serviti dalla pagina**: `sito/fonts/league-spartan-latin.woff2` e `league-spartan-latin-ext.woff2`.
- **Licenza**: `sito/fonts/OFL.txt`.

## Loghi

- **In pagina**: `sito/img/logo-nicdean.png` (390x96, trasparente). È il rendering 4x del disegno vettoriale dentro il loro Flash `indice_nic.swf`; il blocchetto rosso resta in prospettiva come nel Flash.
- **Da chiedere**: il logo vettoriale originale e la versione piatta ufficiale, all'azienda o a Medialine Group, l'agenzia del Flash.
- **SVG**: non l'ho ridisegnato a mano, perché senza la fonte non sarebbe fedele. Si può ricavare esportando le forme dei `.swf` con un convertitore SWF-SVG.
- **Firma**: la firma "NicDean" in corsivo del sottopiede non esiste in digitale.
