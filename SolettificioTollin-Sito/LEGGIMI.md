# Solettificio Tollin: proposta di nuova home

Proposta non richiesta, solo la home. Non è stata inviata né pubblicata; l'azienda non è stata contattata.

- Pagina: `sito/index.html` (statica, si apre con file:///). Immagini in `sito/img/`, carattere in `sito/fonts/` (con `OFL.txt`).
- Screenshot: `screenshot/home/` (1440 intera e prima schermata, 390 intera e prima schermata, da "Dove siamo" al piede a 1440). Scelte, regole ed esiti in `screenshot/home/NOTA.md`, sezione "Livello professionale".
- Si rifà tutto con `bash _prova/script/build_finale.sh` (con `--tieni` restano le prove a 320, 768 e 1024 in `_prova/tmp-build/`). Controlli delle 15 regole e delle prove d'uso: `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`).
- Versione precedente (il foglio in negativo, 24/10/2026): `_prova/versione-1-originale/`.
- Analisi con le fonti: `01-analisi.md`. Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`.

## Da collegare prima di pubblicare

- **Il modulo "Richiesta di campionatura"** oggi compone una mail a info@tollin.it nel programma di posta di chi lo compila (mailto con oggetto "Richiesta di campionatura, <calzaturificio>" e tutti i campi nel testo). Va collegato a un servizio di invio (per esempio il modulo del sito nuovo o un servizio di form) con il consenso privacy e, se serve, il caricamento del file della forma o del disegno: oggi si chiede di allegarlo alla mail.
- **"English"** porta alla versione inglese del sito di oggi (`https://www.tollin.it/welcome.html`): quando il sito nuovo avrà la sua versione inglese, il link va cambiato.
- **Privacy e Cookie** (`privacy.html`, `cookie.html`) nel piede: pagine da fare.

## Da chiedere all'azienda

1. **Gli orari** dell'ufficio e dei ritiri: non sono pubblicati da nessuna parte. In pagina c'è solo "per ritiri e consegne chiamate prima di passare"; appena li danno, vanno in "Dove siamo" e nel piede, in tabella.
2. **Come si comincia una campionatura**: si manda la forma fisica, un file (quale formato), un modello o un campione? Quali tempi? Chi risponde? In pagina c'è solo "si parte dalla forma del vostro modello" (dal loro testo) e "chiedeteci al telefono come mandarli".
3. **Le 12 persone**: il numero è quello del 2024 (visurissima). Va confermato che vogliono mostrarlo (si può scrivere "una dozzina").
4. **I nomi dei materiali dei fornitori** (Ocram, Texon, Adhegel, Greenlife, fisca): sono nelle didascalie del loro catalogo di oggi e restano nei nomi dei tipi; si possono mostrare? Nella foto della scatola (reparto Supervisione) si legge "Tecno-Sint" sulla pianta: la foto non è più ritoccata. Se non si può mostrare, va rifatta.
5. **Le macchine** (plotter Comelz CN, tranciatrice Comelz CM44S, pressa Comec SPM12), lette nelle foto del 2016 o prima: sono ancora queste? Ce ne sono altre?
6. **Il taglio**: il testo italiano parla di laser e anche di punzone e lama oscillante; in pagina ci sono punzone e lama oscillante. C'è anche un laser?
7. **Il fax** 049 644643: Pagine Bianche lo dà ancora; in pagina c'è (senza link). Lo usano?
8. **Clienti, settori e lavori** (regole 10 e 11 del livello professionale): si possono nominare dei calzaturifici o delle fasce (lusso, serie, bambino)? Tre lavori con cliente o luogo, anno e due-tre dati (per esempio un tipo di sottopiede per una collezione) darebbero la prova che oggi manca.
9. **Recensioni o referenze**: nessuna in rete (Pronto Imprese "Recensioni 0"). Se un cliente accetta di dare una frase con nome e comune, va in pagina.
10. **Certificazioni** dei materiali o dell'azienda: nessuna nelle fonti.
11. **La storia**: chi ha fondato nel 1970 e dove, il passaggio dalla ditta Tollin Gianfranco alla S.r.l. nel 2011, chi sono oggi "i titolari".
12. **Il logo ufficiale**: impronte verdi con "SOLETTIFICIO TOLLIN" o riquadro azzurro "Dal 1970"? In pagina ci sono le impronte (e una versione con le lettere bianche per il piede scuro). Serve il file vettoriale.
13. **Il civico**: in pagina il 15 (sito e tutte le schede pubbliche); la mappa del sito di oggi punta al 12 e va corretta anche lì (e sulla scheda Google, se c'è).

## Foto da fare dal vero

Le foto di oggi sono vere ma piccole (850 x 600 con la cornice dentro il file, 227 x 367 per il catalogo) e del 2016 o prima: in pagina non sono mai ingrandite oltre la loro misura, ma sugli schermi ad alta densità sono morbide. Serve mezza giornata in reparto e mezza di still life, con un solo fotografo e la stessa luce (finestra laterale o luce morbida del capannone), tutte orizzontali 3:2 salvo il catalogo, almeno 3000 px di lato lungo, persone che guardano il lavoro e non l'obiettivo.

1. **Apertura**: le mani di un titolare che controllano o sistemano i sottopiedi garbati nella scatola, come `supervisione2` ma con luce migliore e senza bande nere; meglio se si vede il tacco del sottopiede.
2. **I quattro reparti**: il foglio che esce dal plotter della modelleria; la tranciatrice con il foglio tagliato sul nastro; gli stampi della pressa con le forme; il controllo al banco. Stessa distanza e stessa luce per tutte e quattro.
3. **Il catalogo**: i nove tipi uno per uno, sullo stesso cartoncino arancione (lo stesso colore per tutti, niente fasce di ritocco), dall'alto e alla stessa scala, più uno di profilo per i garbati da tacco; almeno 1200 px di lato lungo.
4. **La scatola dei sottopiedi garbati**: dall'alto e di tre quarti, con la luce che segue la curva; con il lato senza stampa in vista se i marchi dei fornitori non si possono mostrare.
5. **Dove siamo**: il furgone giallo TOLLIN davanti al capannone di via Irpinia, in una bella giornata, porte aperte e cartoni; e l'ingresso con il civico 15, utile a chi arriva per la prima volta.

## Licenze

- **Carattere**: Commissioner (Kostas Bartsokas), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file servito dalla pagina, licenza in `sito/fonts/OFL.txt`.
- **Foto e logo di Tollin**: dal sito tollin.it, diritti dell'azienda; usati solo per questa proposta.
- **Repertorio**: nessuna foto di repertorio nella home. Quelle scaricate per i prototipi del 24/10 sono elencate in `assets/CREDITI.md` e non sono usate.
- Nessuna immagine generata con l'IA, nessuna illustrazione.

## Niente newsletter, niente social

Tollin vende solo ai calzaturifici e non ha notizie, fiere, cataloghi né clienti privati: una newsletter non avrebbe niente da mandare. Nessun profilo social trovato: nel piede non c'è "Seguici".
