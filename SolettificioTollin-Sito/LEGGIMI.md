# Solettificio Tollin: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata inviata né pubblicata; l'azienda non è stata contattata.

- Pagina: `sito/index.html` (statica, si apre con file:///), **home ibrida del 3/11/2026** (prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`, sotto i contenuti della versione professionale). Immagini in `sito/img/` (WebP), caratteri in `sito/fonts/` (Commissioner con `OFL.txt`, Azeret Mono con `OFL-AzeretMono.txt`). Direzione in `_prova/alto/DIREZIONE.md`.
- Screenshot: `screenshot/home/` (1440 intera e prima schermata, 390 intera e prima schermata, prime schermate a 1024 e 768, da "Dove siamo" al piede a 1440). Scelte, misure ed esiti in `screenshot/home/NOTA.md`, sezione "Metodo ibrido (novembre 2026)"; sotto resta quella del livello professionale.
- Immagini: `python3 _prova/alto/script/immagini.py` (dagli originali in `assets/originali/immagini/`, riscaricati da tollin.it il 3/11/2026). Misure della sezione D: `node _prova/alto/misura-d.mjs` (esito in `_prova/alto/misure/esito.json`); prove d'uso: `node _prova/alto/uso.mjs`; screenshot: `node _prova/alto/finali.mjs`. Gli script della versione professionale (`_prova/script/`) sono andati persi con il riavvio.
- Versione professionale (3/11/2026, da cui parte l'ibrida): `_prova/versione-pro/` (sito e screenshot). La versione 1 (il foglio in negativo, 24/10/2026) in `_prova/versione-1-originale/` non c'è più dopo il riavvio.
- Analisi con le fonti: `01-analisi.md`. Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`.

## Da collegare prima di pubblicare

- **Il modulo "Richiesta di campionatura"** oggi compone una mail a info@tollin.it nel programma di posta di chi lo compila (mailto con oggetto "Richiesta di campionatura, <calzaturificio>" e tutti i campi nel testo; obbligatorio solo il calzaturificio). Va collegato a un servizio di invio (per esempio il modulo del sito nuovo o un servizio di form) con il consenso privacy; con il servizio, il campo "Forma o disegno del modello" diventa un caricamento del file (PDF, DXF o immagine): oggi chi scrive dice se lo allega alla mail, se ha la forma o se ne parla al telefono.
- **Il link "Indicazioni"** (bottone di Dove siamo, l'unico in pagina: nella prima schermata sul telefono "Via Irpinia 15" porta lì) apre Google Maps con il percorso verso "Via Irpinia 15, 35020 Villatora di Saonara PD". Da qui Google non si apre: va provato a mano da un telefono che lo spillo cada sul 15 e non sul 12. Se non ci cade, usare le coordinate del cancello o il place_id della scheda Google corretta.
- **"English"** porta alla versione inglese del sito di oggi (`https://www.tollin.it/welcome.html`): quando il sito nuovo avrà la sua versione inglese, il link va cambiato.
- **Privacy e Cookie** (`privacy.html`, `cookie.html`) nel piede: pagine da fare.

## Da chiedere all'azienda

1. **Gli orari** dell'ufficio (a che ora rispondono al telefono) e dei ritiri: non sono pubblicati da nessuna parte. In pagina c'è solo "per ritiri e consegne chiamate prima di passare"; appena li danno, vanno in tabella in "Dove siamo", nella riga dell'apertura e nel piede.
2. **Come si comincia una campionatura**: si manda la forma fisica, un file (quale formato), un modello o un campione? Quali tempi? Chi risponde? In pagina c'è solo "si parte dalla forma del vostro modello" (dal loro testo) e "chiedeteci al telefono come mandarli".
3. **I numeri**: nella home ibrida la fascia delle cifre non c'è più e le 12 persone (dato del 2024, visurissima) non sono in pagina. Se l'azienda vuole un numero vero in più (persone, paia o pezzi l'anno, calzaturifici serviti, paesi), va in una frase nel blocco "Dal 1970, a conduzione familiare", con l'unità e il periodo.
4. **I nomi dei materiali dei fornitori** (Ocram, Texon, Adhegel, Greenlife, fisca): sono nelle didascalie del loro catalogo di oggi e restano nei nomi dei tipi; si possono mostrare? Nella foto della scatola (oggi la foto del culmine, "Dal 1970, a conduzione familiare") si legge "Tecno-Sint" sulla pianta: la foto non è ritoccata. Se non si può mostrare, va rifatta; nel frattempo il culmine passa a `img/r2-taglio-807.webp` (tranciatura, didascalia "Tranciatura CAD/CAM / Reparto lavorazione, Villatora di Saonara") e il reparto 02 a `lavorazione1`.
5. **Le macchine** (plotter Comelz CN, tranciatrice Comelz CM44S, pressa Comec SPM12), lette nelle foto del 2016 o prima: sono ancora queste? Ce ne sono altre? In pagina sono scritte come "Le macchine nelle foto dei reparti" finché non c'è la conferma.
5 bis. **L'anno delle foto**: la didascalia del culmine (la scatola dei sottopiedi garbati) dice cosa e dove ma non l'anno, che non è scritto da nessuna parte (le foto non hanno dati EXIF).
6. **Il taglio**: il testo italiano parla di laser e anche di punzone e lama oscillante; in pagina ci sono punzone e lama oscillante. C'è anche un laser?
7. **Il fax** 049 644643: Pagine Bianche lo dà ancora; in pagina c'è (senza link). Lo usano?
8. **Clienti, settori e lavori** (regole 10 e 11 del livello professionale): si possono nominare dei calzaturifici o delle fasce (lusso, serie, bambino)? Servono almeno tre lavori, ognuno nel formato "calzaturificio o fascia, anno, tipo di sottopiede, numerata o quantità", con una foto: andrebbero in una fascia su antracite tra Lavorazioni e Azienda. È la prova che oggi manca di più.
9. **Recensioni o referenze**: nessuna in rete (Pronto Imprese "Recensioni 0"). Serve almeno una frase di un cliente, con nome, ruolo e comune, data per iscritto: va nella stessa fascia dei lavori.
10. **Certificazioni** dei materiali o dell'azienda: nessuna nelle fonti.
11. **La storia**: chi ha fondato nel 1970 e dove, il passaggio dalla ditta Tollin Gianfranco alla S.r.l. nel 2011, chi sono oggi "i titolari".
12. **Il logo ufficiale**: impronte verdi con "SOLETTIFICIO TOLLIN" o riquadro azzurro "Dal 1970"? In pagina ci sono le impronte, a 216 px in testata (150 sul telefono), ritagliate dal JPEG di 420 px del sito di oggi, e una versione con le lettere bianche per il piede scuro. Serve il file vettoriale: appena arriva, sostituisce il PNG.
13. **Il civico**: in pagina il 15 (sito e tutte le schede pubbliche); la mappa del sito di oggi punta al 12 e va corretta anche lì (e sulla scheda Google, se c'è).

## Foto da fare dal vero

Le foto di oggi sono vere ma piccole (850 x 600 con la cornice dentro il file, 227 x 367 per il catalogo) e del 2016 o prima: in pagina non sono mai ingrandite oltre la loro misura, ma sugli schermi ad alta densità sono morbide. Serve mezza giornata in reparto e mezza di still life, con un solo fotografo e la stessa luce (finestra laterale o luce morbida del capannone), tutte orizzontali 3:2 salvo il catalogo, almeno 3000 px di lato lungo, persone che guardano il lavoro e non l'obiettivo.

1. **Apertura** (home ibrida): un sottopiede garbato per il tacco, di profilo, sullo stesso cartoncino arancione del catalogo (tono di #B4491E), con luce morbida e almeno 1600 px di lato lungo. Oggi la tavola usa `foto7prod` a 227 x 151 px, alla misura vera: si vede morbida sugli schermi ad alta densità. Se l'azienda ha il file CAD del sottopiede, il disegno vero si può mettere accanto alla foto (modello D del capitolo 5); senza file, niente disegno.
1 bis. **Supervisione**: le mani di un titolare che sistemano i sottopiedi garbati nella scatola, come `supervisione2` ma con luce migliore, senza dominante gialla e senza bande nere (oggi è la foto del reparto 4).
2. **I quattro reparti**: il foglio che esce dal plotter della modelleria; la tranciatrice con il foglio tagliato sul nastro; gli stampi della pressa con le forme; il controllo al banco. Stessa distanza e stessa luce per tutte e quattro.
3. **Il catalogo**: i nove tipi uno per uno, sullo stesso cartoncino arancione (lo stesso colore per tutti, niente fasce di ritocco; oggi il fondo è uniformato in pagina all'arancio #B4491E, conviene scegliere un cartoncino di quel tono), dall'alto e alla stessa scala, più uno di profilo per i garbati da tacco; almeno 1200 px di lato lungo. Le foto di oggi sono 227 x 367: in pagina sono a 128 px e non si possono ingrandire per mostrare un incastro a ragno o una fisca da vicino.
4. **La scatola dei sottopiedi garbati**: dall'alto e di tre quarti, con la luce che segue la curva; con il lato senza stampa in vista se i marchi dei fornitori non si possono mostrare.
5. **Dove siamo**: il furgone giallo TOLLIN davanti al capannone di via Irpinia, in una bella giornata, porte aperte e cartoni; e l'ingresso con il civico 15, utile a chi arriva per la prima volta.

## Licenze

- **Caratteri**: Commissioner (Kostas Bartsokas), Google Fonts, SIL Open Font License 1.1, licenza in `sito/fonts/OFL.txt`; Azeret Mono (Displaay, The Azeret Project Authors), Google Fonts, file da `@fontsource/azeret-mono` 5.1.0, SIL Open Font License 1.1, licenza in `sito/fonts/OFL-AzeretMono.txt`. Uso commerciale libero, file serviti dalla pagina.
- **Foto e logo di Tollin**: dal sito tollin.it, diritti dell'azienda; usati solo per questa proposta.
- **Repertorio**: nessuna foto di repertorio nella home. Quelle scaricate per i prototipi del 24/10 sono elencate in `assets/CREDITI.md` e non sono usate.
- Nessuna immagine generata con l'IA, nessuna illustrazione.

## Niente newsletter, niente social

Tollin vende solo ai calzaturifici e non ha notizie, fiere, cataloghi né clienti privati: una newsletter non avrebbe niente da mandare. Nessun profilo social trovato: nel piede non c'è "Seguici".
