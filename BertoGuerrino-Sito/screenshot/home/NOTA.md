# Berto Guerrino: metodo ibrido (novembre 2026)

Home ibrida del 3/11/2026: prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale (copiata intera in `_prova/versione-pro/`), rimessi su una griglia sola. Direzione scritta prima dell'HTML in `_prova/alto/DIREZIONE.md`; riga del registro in `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Screenshot di questa cartella rifatti alla stessa ora simulata (martedì 3/11/2026 alle 10) con `_prova/alto/scatti.mjs`.

## Alto livello: ritocco dopo il giudice da agenzia (3/11/2026)

Il giudice ha dato 6,5 alla home ibrida (gesto troppo piccolo, culmine sulla foto più debole, tipografia senza un punto di scala, finiture). Ritocco di `sito/index.html` e di `_prova/alto/script/immagini.py`, senza tornare indietro sulla sezione D. Copia della pagina di prima in `_prova/alto/ritocco/index-prima-del-ritocco.html`, verifiche in `_prova/alto/ritocco/verifica.mjs`.

**Applicati**
- **La targa** (gesto D1, D4, D5, D7): il titolo sta dentro un rettangolo giallo pieno a spigolo vivo, con il filetto nero all'interno come i cartelli gialli delle loro macchine, appoggiato sulla foto a x=104 (24 px dentro) e sporgente di 32 px sotto il bordo: `h1` maiuscolo 500 a 48 px su due righe e sotto la riga del mestiere. 737x198 px a 1440 (154x41 nella miniatura a 300 px, `_prova/alto/ritocco/miniatura-300.jpg`); l'`h1` sta a x=136, non più a 80. Sta sull'angolo **basso** e non su quello alto, come proponeva il giudice: in alto a sinistra ci sono il trattore, la macchina e il cartello, in basso solo i solchi della terra. A 1024-1279 l'`h1` scende a 40 px per restare su due righe; sotto i 1024 la targa scende sotto la foto e la copre di 48 px.
- **La frase-firma torna** con lo stesso trattamento: la stessa targa con "Attrezzature vivaistiche da noi prodotte" apre il piede. La targhetta "Instruments for professionals" dell'Azienda è tolta (il payoff resta nel logo del piede), così la targa porta un testo solo.
- **Il giallo pieno è passato alla targa**: Orari e contatti sono su bianco, aperti da un filetto nero di 2 px, con le righe degli orari in grigio e il modulo su #F1F2F4. Sezioni con il colore del marchio: 0; fondi: bianco e #F1F2F4.
- **La foto d'apertura intera**: 1280x704 alla sua misura (prima tagliata 2:1), 69,5% della prima schermata a 1440. I 4 pixel del bordo, scuriti dalla compressione di YouTube, sono ripetuti dalla prima colonna buona (stessa misura del file).
- **A 390**: la targa sta sopra, la foto scende fino alla barra fissa (si sovrappone di 2 px: nessuna striscia grigia) ed è un nuovo taglio verticale 600x704 da x=400 (`piragna-campo-v-600/450.webp`): retro della Piragna con la targhetta BERTO, il vomere e la prima fila di astoni a destra. Foto sul 58,9% dello schermo. L'`h1` va su "ATTREZZATURE / VIVAISTICHE / DA NOI PRODOTTE" (spazi unificatori in "da noi prodotte"), anche a 320.
- **Culmine**: la trapiantatrice intera (1,82:1, nessun taglio) su 8 colonne, 845x465 px (scala 0,66, file da 960); accanto, su 4 colonne, l'elenco dei video e sotto la zolla e gli astoni a 194 px. La didascalia dice "dal nostro video pubblicato a novembre 2024" (è la data di pubblicazione, non delle riprese). Nessun fotogramma oltre gli 845 px fuori dall'apertura.
- **Punto di scala (D5)**: la frase della presentazione, "Siamo costruttori di macchine ed attrezzature agricole...", è il manifesto dell'Azienda a 34 px su 10 colonne; gli `h2` scendono da 32 a 28 px (23 a 390), il titolo dello sterrapiante a 28.
- **Contatto per bisogno (D12)**: sopra il modulo due strade con il filetto, "Macchine per vivai" (prezzo, scheda tecnica e video: "Chiedete il prezzo") e "Negozio, officina e ricambi" ("Chiedete un ricambio"); ognuna apre il modulo con la voce giusta già scelta (provato). Il numero è uno solo, a sinistra, per tutte e due: non lo ripeto nelle strade (tetto di 2 volte nel testo italiano). Nessuna persona: i nomi si aggiungono quando Berto dice chi fa che cosa.
- **Indicazioni una volta per larghezza**: la parola "Indicazioni" resta solo nella targa a 390; nei contatti il link al percorso è l'indirizzo stesso.
- **Piede completo** (C15): colonna Contatti con `tel:`, e-mail, "lun-ven 8-12 e 14-19, sab 8-12 (orari di Google)" e YouTube; la "e" di "Privacy e cookie" ha il colore dei link. Il `tel:` del paragrafo inglese è tolto (il numero con +39 resta scritto): i `tel:` restano 3 (testata, contatti, piede).
- **Allineamenti**: tutte le frasi accanto agli `h2` partono da x=732 (c7-12) e stanno sulla linea di base dell'ultima riga del titolo (`align-items:last baseline`), anche nel culmine e nell'Azienda; la riga del mestiere è dentro la targa, su una riga sola a 1440.
- **Foto in studio**: lo sfondo di tutte e otto riportato a #F1F2F4 (guadagno per canale dopo il trattamento; nel WebP 241,243,244). **Zolla e astoni** più morbidi: contrasto 0,92, luci sopra 200 compresse, sfocatura 0,35 px, per stare accanto ai fotogrammi.
- **Parole** tenute sotto 900 (895): tolti i doppioni (Stihl nella riga "Di tutto di più", "YouTube" su ogni video, la riga accanto al culmine accorciata).

**Respinti, con il motivo**
- **Scalare le macchine in studio all'80% della tessera**: scalzapneus, primi rami e porta innesti sono basse di larghezza perché alte; portarle all'80% della larghezza vorrebbe dire ingrandirle oltre il file (D2, D10) o tagliarle in alto.
- **Luogo e anno dei lavori (D9)**, **Fausto e Lorena con foto e lingue**, **nomi per le strade del contatto**: non sono nelle fonti (LEGGIMI, "Da chiedere"). Non inventati.
- **Foto vera in campo** (il 60% della distanza secondo il giudice): serve il servizio fotografico (LEGGIMI, "Foto da fare dal vero").
- **Lo sterrapiante nella prima schermata** (compito del vivaista): esiste solo in fotogrammi da 500 px, e la sezione D vuole una foto sola in apertura. Resta la prima macchina dopo "Macchine per vivai" nel menu.
- **D8 parole e altezza** (895 e 7119 px contro 450-650 e 4.000-6.000): deroga voluta dal metodo ibrido.

## Che cosa è cambiato

- **Idea**: la macchina gialla che costruiscono a Saonara, al lavoro tra le file del vivaio, alla sua misura vera; il negozio Honda e Stihl sempre a un tocco, in testata.
- **Modello F** (riga del capitolo 5, riferimento Damcon), nella strada di D2 per le foto tra 800 e 1600 px: la foto a 1280 px, centrata sulla griglia, con il titolo sopra. **Foto d'apertura**: la trincia Piragna gialla e blu tra le file di un vivaio, fotogramma del loro video "trincia piragna" (canale di Lorena Berto, pubblicato il 6/11/2024, `assets/originali/youtube/yt-5b_3K-YZ2zk-maxres.jpg`, 1280x720, bande nere tolte). Il capitolo 5 indicava lo sterrapiante, ma in campo esiste solo in fotogrammi di 500 px: a tutta larghezza sarebbe stato ingrandito 2,6 volte.
- **Gesto**: la didascalia è una targhetta gialla a spigolo vivo sull'angolo della foto, come il cartello "20 m" e il cartello BERTO delle loro macchine. Lo stesso trattamento torna una volta, su "Instruments for professionals" nella sezione Azienda.
- **Registro**: Familjen Grotesk (SIL OFL 1.1, `sito/fonts/OFL.txt`), una famiglia sola, al posto di Anybody. `h1` 500 maiuscolo 48 px, `h2` 500 32 px, testo 18 px, nessun testo oltre i 48 px.
- **Titolo**: "Attrezzature vivaistiche da noi prodotte", la loro frase della pagina `vivaio/` (5 parole). Mestiere e luogo nella riga accanto: "Saonara (PD), dal 1961. Honda e Stihl con assistenza e ricambi."
- **Tolto, come chiede il capitolo 5**: il secondo bottone e le due porte dell'apertura, la fascia delle quattro cifre (1961, 12, 11, 4,4), le tre recensioni senza la macchina (resta quella del tagliaerba, con il 4,4 su 58 in una frase), gli occhielli maiuscoli sopra ogni titolo, la fascia blu dell'Azienda, il grigio e il nero alternati, i doppioni ("Chiama" in tre sezioni, "Indicazioni" in quattro punti, la riga "Prezzo su richiesta" con due bottoni, il telefono gigante, il fax). Le sezioni Azienda e Altre lingue sono diventate una.
- **Tenuto dalla versione professionale**: stato aperto/chiuso calcolato sull'ora di Roma, orari della settimana, telefono, indicazioni, i sette lavori come comandi, lo sterrapiante con la tabella delle tre versioni in testo, le sette schede con Video e Prezzo (il prezzo apre il modulo con la macchina già scelta), i video, i marchi, Officina, Ricambi e Consigli, il modulo con mailto, oggetto e testo da copiare, inglese, tedesco e francese.
- **Telefono**: a 1440 è l'unico bottone, in testata; sotto i 600 px va in una barra fissa in basso con lo stato ("Aperto ora, chiude alle 12") e "Chiama 049 640282", che resta anche a metà pagina.
- **Foto**: dodici, tutte di Berto, in WebP con srcset (`_prova/alto/script/immagini.py`): due fotogrammi in campo a 1280x704 (Piragna in apertura, trapiantatrice a ruota nel culmine), due della galleria a 500 px (zolla, astoni), otto in studio a 700 e 420 px. Un solo trattamento (bilanciamento verso il neutro, saturazione 0,88, contrasto 1,05; maschera di contrasto leggera sui due fotogrammi). Nessuna ingrandita, nessuna scurita. `assets/originali/` era stata cancellata con il riavvio: ho riscaricato solo le anteprime dei video dal loro canale (`assets/originali/youtube/`).

## Sezioni (a 1440, 7119 px dopo il ritocco)

1. Apertura (testata, titolo, foto della Piragna).
2. Macchine per vivai: i sette lavori, lo sterrapiante con la tabella e "Chiedete il prezzo", sette schede, "E poi".
3. **Culmine**, al lavoro nei vivai (160 px sopra e sotto invece di 104): la trapiantatrice a ruota intera su 8 colonne con "Trapiantatrice a ruota, in un vivaio / dal nostro video pubblicato a novembre 2024"; accanto i video, la zolla e gli astoni.
4. Negozio e officina (grigio): Honda e Stihl, gli altri marchi, "di tutto di più", Officina, Ricambi e accessori, Consigli.
5. Azienda e altre lingue: "La nostra ditta nasce nel 1961.", Fausto e Lorena Berto, il manifesto (la presentazione a 34 px), In English, Auf Deutsch, En français.
6. Orari e contatti (su bianco, con il filetto): stato, orari, telefono, e-mail, indirizzo con il percorso, due strade per bisogno, modulo.
Piede: la targa con la frase-firma, logo con il payoff, ragione sociale, indirizzo, P.IVA, contatti (telefono, e-mail, orari, YouTube), pagine interne.
Sul telefono il Negozio sale subito dopo l'apertura.

## Misure (`_prova/alto/misura-d.mjs`, risultati in `_prova/alto/misure/misura-d.json` e `esito.txt`): 68 soglie su 68 passano

| Soglia | Valore |
|---|---|
| D2 foto nella prima schermata | 69,5 % a 1440 (1280x704 visibili), 58,9 % a 390 (barra fissa esclusa) |
| D2 e D10 foto ingrandite | 0 (scala massima 1,0) |
| D3 a 1440 | 6 cliccabili (logo, tre voci, EN DE FR, telefono), 1 bottone, 144 caratteri fuori dal menu, 0 cifre grandi, nessuna fila di ingressi |
| D3 a 390 | 4 cliccabili (logo, Menu, Chiama, Indicazioni), 1 bottone |
| D5 | 1 famiglia, 0 elementi oltre i 100 px, testo corrente 18 px |
| D6 occhielli | 0 |
| D7 `h1` | 5 parole, 0 virgole, lista nera 0, istruzioni del modulo a 14 px |
| Pagina | 895 parole (tetto 900), 6 sezioni, 7119 px a 1440, 573 KB caricati |
| Griglia | un solo bordo di contenuto (80-1360 a 1440) e tutti i figli delle griglie sulle linee delle 12 colonne |
| D10 | 12 foto, 3 formati (1,82:1 dei fotogrammi, 4:3, 1:1), nessuna scurita, "indicativ" 0 |
| D11 | 2 fondi (bianco, grigio #F1F2F4), 0 sezioni gialle (il giallo è nelle due targhe), spazi tra le sezioni 104 e 160 px |
| D9 | nessuna cifra di 30 px o più ("1961" nell'`h2` ora a 28 px) |
| Ripetizioni | 3 link `tel:` (testata, contatti, piede), 2 link al percorso (targa a 390, indirizzo nei contatti) con la parola "Indicazioni" una volta, 3 mailto, telefono 2 volte nel testo italiano, 1961 due volte e 4,4 una volta, 4 bottoni in pagina |
| Controlli a 320, 390, 768, 1024, 1440, 1920 | nessuno scorrimento orizzontale, nessuna sovrapposizione, nessun errore, `tel:+39049640282` e mailto a bertopd@libero.it |

Confronto guardato a pezzi: `_prova/alto/confronto-1440.jpg` (professionale, ibrida, Damcon ed Egedal dal vivo, prime schermate in `_prova/alto/concorrenti/`).

## Compiti della scheda: dove stanno ora

| Compito | Dove |
|---|---|
| Cliente del negozio, 390: aperto adesso | barra fissa in basso, sempre visibile ("Aperto ora, chiude alle 12"); tabella della settimana in Orari e contatti, a un tocco da "Orari e contatti" nel menu |
| Chiamare senza scorrere e a metà pagina | "Chiama 049 640282" nella barra fissa (52 px) |
| Indicazioni senza scorrere | "Indicazioni: via Caovilla 27/B" nella targa, solo sotto i 600 px |
| Honda e Stihl con assistenza e ricambi | riga dentro la targa, nella prima schermata; Negozio e officina subito dopo l'apertura sul telefono e voce del menu |
| Vivaista, 1440: la macchina per il lavoro | voce "Macchine per vivai" in testata, poi i sette lavori come comandi |
| La tabella dello sterrapiante | prima macchina della sezione, in testo, intera sullo schermo dopo un tocco |
| Il video | link Video su ogni scheda che ne ha uno, elenco dei video nel culmine |
| Chiedere il prezzo | "Chiedete il prezzo" e "Prezzo" su ogni scheda aprono il modulo con la macchina scelta; il testo da copiare resta se la posta non si apre |
| Estero: la lingua | "EN DE FR" in testata (un link), In English, Auf Deutsch, En français nella sezione Azienda |
| Estero: chiamare e scrivere | "+39 049 640282" scritto e la e-mail con l'oggetto in inglese nel paragrafo In English; il `tel:` è in testata, sempre visibile a 1440 |

## Problemi aperti

- **La foto d'apertura è un fotogramma di video**: 1280 px, morbida, con la compressione di YouTube. Regge alla sua misura, ma sopra l'8 serve una foto vera in campo (LEGGIMI, "Foto da fare dal vero"). A 1920 la foto resta a 1280 px con il bianco ai lati, per non ingrandirla.
- **Didascalie senza luogo**: "in un vivaio" e l'anno di pubblicazione del video (2024). Il vivaio, il comune e l'anno vero delle riprese vanno chiesti a Berto.
- **Lingue di Fausto e Lorena**: la riga di Damcon ("le lingue parlate") non si può fare, perché nelle fonti non ci sono. Non ci sono nemmeno le loro foto.
- **Parole al limite**: 895 su 900, contando anche le voci del menu a tendina del modulo. Ogni testo nuovo va pagato togliendone un altro.
- **Il telefono**: `tel:` in testata, nei contatti e nel piede (3, il tetto di D12); nel paragrafo inglese il numero con +39 è scritto ma non è un link.
- **Indicazioni**: la parola compare una volta (targa a 390); il link al percorso c'è anche nei contatti, sull'indirizzo. Sono 2 link, uno per larghezza in vista nella prima schermata.
- **Screenshot interi a 390**: nella cattura a tutta pagina la barra fissa compare a metà dell'immagine (a 844 px): è un effetto della cattura, sul telefono resta in basso.
- **Il modulo non invia nulla** (mailto), come prima: va collegato a un servizio (LEGGIMI).
- Restano "da confermare" e non dati come certi: orari (in pagina con la nota "sono gli orari indicati su Google"), forma giuridica (in pagina non c'è più "S.a.s."), fax e ingresso in sedia a rotelle (tolti), vendita all'estero (tolta: le altre lingue dicono solo "vendiamo direttamente"), P.IVA (resta nel piede, dai registri pubblici: da verificare prima di pubblicare).

---

# Berto Guerrino, home finale: "Il pezzo giallo, in scala"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot e prove del gesto con `finale_shot.mjs`, JPEG con `finale_jpg.py`, misura dei segnali con `_metodo/kit/segnali.sh`). Parte dal prototipo A, poi rifinita dopo il giudice cieco (`_prova/cieco.json`).

## Idea

Lo sterrapiante Berto, giallo con il vomere blu, posato sulla linea di terra dentro l'ingombro delle sue tre versioni: tre riquadri MOD. 80, MOD. 85 e MOD. 100 con le quote vere di altezza e lunghezza, come in una tavola d'officina. È la cosa che solo Berto ha (lo stesso pezzo costruito in tre taglie per tre classi di trattore) e sta nella prima schermata, sotto il titolo, con i bottoni e le cifre accanto. Con il nome di un altro costruttore la pagina non regge: macchina, versioni, misure e frasi sono di Berto.

## Prima schermata

- **1440 (apertura fino a 964 px)**: testata con il logo vero (cartello giallo), quattro voci e il telefono. "Macchine speciali per vivai" in Anybody stretto a 136 px su una riga a tutta larghezza. Sotto, su otto colonne, il disegno in scala: linea di terra, i tre riquadri, la foto dello sterrapiante e le quote (160 cm, 230 cm con MOD. 85 attivo). Sulle quattro colonne di destra due righe di testo, i bottoni MOD. 80 / 85 / 100, trattore, larghezza e peso in cifre grandi, "Attacco a tre punti, PTO 540 giri", i link alla scheda e al video, il bottone "Chiama 049 640282". Tutto dentro i 900 px.
- **390**: titolo a 64 px su tre righe, il disegno a tutta larghezza, i tre bottoni larghi un terzo e le prime cifre dentro gli 844 px; testo e telefono subito sotto.
- **768 e 1024**: a 1024 disegno e comandi restano affiancati (sette e cinque colonne, menu a bottone); sotto i 900 il titolo va su due righe, il disegno a tutta larghezza, i bottoni sotto e le cifre accanto al testo.

Sezioni, in ordine: apertura con il gesto; la zolla (una foto alla sua misura di 500 px con il titolo "Il vomere passa sotto la fila, solleva la zolla e la apre" sotto, non accanto); le altre macchine (quattro pezzi su due colonne sulla stessa linea di terra, poi una riga con le altre sette); officina e negozio (una colonna sola, i marchi a 40 px); chiusura con foto; piede. Pagina di 5206 px a 1440 e 5067 a 390, piede compreso.

## Caratteri e colori

- **Anybody** (Etcetera Type Co., Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia variabile con gli assi di larghezza e peso, servita dalla pagina (`sito/fonts/anybody-latin.woff2`, sottoinsieme latin). Titoli a larghezza 72 % e peso 580; cifre grandi e marchi a larghezza 62 %; testo a larghezza 100 % peso 400, 18-19 px su 1,6. Cifre tabellari per misure, pesi, telefono e P.IVA. Il motivo: le lettere strette e piene del cartello BERTO, senza copiarle. Riferimenti del mestiere (sez. 7 di `01-analisi.md`): Sneeboer (officina di famiglia, titolo enorme, un solo colore del marchio) e Väderstad (una sola immagine forte, il giallo del marchio come unico colore).
- **Colori**: carta #F4F1E9, carta scura #EAE5D8 (solo il piede), inchiostro #1B1A17 (15,4:1 sulla carta, 13,8:1 sul piede), grigio #58544B per i testi secondari (6,7:1 sulla carta, 6,0:1 sul piede), grigio delle etichette dei riquadri spenti #6B665B (5,1:1), blu vomere #23324A per i link (11,4:1). Il giallo arriva solo dalle foto, il rosso solo dal logo. Nessun gradiente, nessuna ombra disegnata, nessuna icona.

## Interazione

Un gesto solo, in apertura: i bottoni MOD. 80, MOD. 85, MOD. 100 (`aria-pressed`, frecce sinistra e destra da tastiera, bersagli alti 56 px). Al clic o al tocco cambiano trattore (40/68, 60/100, 100/150 HP), larghezza (90, 110, 120 cm), peso (350, 500, 680 kg) e le quote (140 x 210, 160 x 230, 170 x 280 cm); il riquadro scelto diventa pieno e la foto si scala in modo uniforme dentro di lui (0,18 s, niente con "riduci movimento"). Provato da `finale_shot.mjs`: clic su MOD. 100, due frecce a sinistra fino a MOD. 80 (il fuoco segue, 350 kg), tocco su MOD. 100 a 390 (100/150 HP). Nient'altro si muove; menu a bottone sotto i 1024 px; colonne del piede a fisarmonica con bottoni veri sotto i 600 px (provata col tocco).

## Foto: origine e licenza

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Sterrapiante (nel disegno in scala) | `img/sterrapiante-700.jpg` | `vivaio/images/STERRAPIANTE.png` del sito (724 px): cornice e didascalia tolte, fondo grigio stimato con una superficie polinomiale e diviso, ombra tenuta, taglio sul punto d'appoggio. Solo alla misura nativa, mostrata fino a circa 690 px CSS: nessun ingrandimento | materiale dell'azienda, solo come prova |
| Quattro macchine | `img/porta-innesti, primi-rami, piragna, agevolatrice -420/640.jpg` | foto in studio delle schede, stesso trattamento, luminosità e croma della vernice avvicinate allo sterrapiante | materiale dell'azienda |
| La zolla | `img/zolla-500.jpg` | `vivaio/gallery/FOTO-3.jpg` (500x500), dominante marrone corretta con i livelli per canale, niente viraggio | materiale dell'azienda |
| Chiusura | `img/campo-640/960/1264.jpg` | anteprima del video YouTube `5b_3K-YZ2zk` del loro canale (trincia Piragna al lavoro tra le file), bande nere tolte, colori naturali, mai oltre la misura del file | materiale dell'azienda |
| Logo | `img/logo-berto.png`, `img/logo-berto-payoff.png` | ritagli di `images/apertura.png` (cartello giallo, 524 px), mostrati a 112 e 168 px | logo dell'azienda |

Nessuna immagine generata dall'IA e nessuna foto di repertorio in pagina.

## Piede

Logo con "Instruments for professionals" e una riga su chi sono; colonne Macchine per vivai (con le due rincalzatrici separate), Azienda, Contatti, Seguici (solo YouTube, l'unico social che esiste); in fondo ragione sociale, P.IVA, Privacy, Cookie. Link alti almeno 24 px. A 390 le quattro colonne si aprono a fisarmonica.

**Niente newsletter**: la pagina "Novità" del sito è vuota dal 2021, il canale YouTube ha 27 iscritti e non ci sono fiere né cataloghi da annunciare. Si aggiunge solo se confermano che manderebbero le offerte di stagione.

## Cosa è cambiato dopo il giudice cieco

- Apertura e versioni fuse: il disegno in scala con i bottoni sta sotto il titolo, nella prima schermata; non è più "titolo a sinistra e pezzo scontornato a destra con le legende", e la foto dello sterrapiante compare una volta sola.
- Tolta la quota "fino a 1 m fuori carreggiata" e le legende: nessuna quota che non corrisponda a un punto della macchina; il dato resta nel testo.
- Sterrapiante solo a 700 px, la misura del file: tolti i file 1160 e 1560 ingranditi (e anche il 400, non più usato).
- Zolla: non più foto da un lato e testo dall'altro; foto a 500 px con il titolo sotto, colore corretto (nessun fotogramma YouTube più nitido della zolla: le anteprime dello sterrapiante hanno riquadri incorniciati).
- Chiusura: al posto della foto di repertorio desaturata (Seymour) il fotogramma YouTube più nitido di una macchina Berto al lavoro, a colori naturali; a 1024 il passo sopra il titolo è 112 px come le altre sezioni.
- Altre macchine: da sei a quattro, su due colonne alla stessa altezza; trapiantatrice e fresatrice nella riga "E poi".
- Officina: titolo e testo in una colonna di 640 px; marchi a 40 px, sotto le macchine per gerarchia; link "Giardinaggio e marchi" su una riga sua.
- Piede: link e Privacy/Cookie alti almeno 24 px; "Rincalzatrice porta innesti" e "Rincalzatrice primi rami" separate.
- In quest'ultimo passaggio: scritte del disegno in scala più grandi dove il disegno si rimpicciolisce (da 901 a 1100 px, sotto i 760 e sotto i 360: a 320 le quote sono a circa 12 px invece di 10), zolla con la dominante corretta, tolto il riquadro azzurro del tocco su bottoni e link.

## Controlli

- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 700, 768, 820, 900, 1024, 1100, 1280, 1366, 1440, 1680, 1920 e 2560; nessuna sovrapposizione tra titolo, disegno, testo, bottoni e cifre; nessun elemento oltre il margine della colonna; nessun link del piede sotto i 24 px (controlli automatici in `finale_shot.mjs`). Screenshot a 1440 e 390 guardati a pezzi, prime schermate a 320, 768, 1024 e 1920 guardate.
- Collegamenti: `tel:+39049640282` (testata, apertura, chiusura, piede), `mailto:bertopd@libero.it`, mappa Google con "Via Caovilla 27/B 35020 Saonara PD".
- Nessun U+2014 nella pagina, negli script, nella NOTA e nel LEGGIMI.
- Segnali da IA (`_metodo/kit/segnali.sh` a 1440): 9 soglie bloccanti su 10 OK. Sotto soglia l'area delle foto, 19,8 % contro 35 %: lo strumento non conta la foto dentro lo SVG, e Berto non ha foto grandi (il meglio è a 724 px e 1280 px da un video SD). Come dice la guida per le aziende senza foto grandi, non si maschera ingrandendo: è la prima cosa da chiedere (brief nel LEGGIMI). Da guardare: tre numeri grandi (le cifre del gesto e il 1961 della chiusura), voluti; un titolo col punto (la frase loro della chiusura).
- Divieti del committente: nessun gradiente, testo in gradiente, emoji, Inter, bordo sinistro colorato, vetro, icone Lucide, badge, tre box, comparse allo scorrimento, effetti sul cursore, bottoni che sbiadiscono, serif corsivo.
- Aperta come file://, la console mostra un avviso CORS sulla `preload` del carattere: il carattere si carica comunque da `@font-face`; servita in http l'avviso sparisce.

## Livello professionale (3/11/2026)

Questa sezione sostituisce quanto sopra: la home "Il pezzo giallo, in scala" descritta nelle sezioni precedenti è conservata com'era in `_prova/versione-1-originale/` (sito e screenshot, compresi i tre `gesto-*.jpg`, che qui non ci sono più perché il gesto non c'è più).

Richiesta: "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" e "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), adattata a una bottega che fa due mestieri. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14, le pagine intere di barth, Cly-Del e Budri a pezzi; la colonna di destra di `_invio/zona/home/livello-professionale.jpg` (Unicar, Oby, Fornasiero). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`.

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot all'ora simulata martedì 3/11/2026 alle 10 con `pro_shot.mjs` e `pro_jpg.py`, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`, prove d'uso con `pro_uso.mjs`). Per vedere un'altra ora: `sito/index.html?ora=2026-11-08T10:00`.

### Che cosa è cambiato, in breve

- **Uso prima di tutto.** La versione 1 apriva sul solo sterrapiante e non aveva orari, indicazioni, lingue né negozio in vista. Ora la prima schermata a 390x844 ha, senza scorrere: lingua IT/EN/DE/FR (81 px), "Saonara (PD), dal 1961", il titolo con i due mestieri, lo stato calcolato sull'ora di Roma ("Aperto ora, chiude alle 12", 287 px) con "Orari della settimana", **Chiama 049 640282** a tutta larghezza (352-404 px), **Indicazioni: via Caovilla 27/B** (414-466 px, apre il percorso in Google Maps), "Concessionari Honda e Stihl. Assistenza e ricambi in officina." (482 px), le due porte Negozio e officina / Macchine per vivai (551-610 px) e la zolla in una striscia bassa (630-786 px). A 320x640 ci sono tutti fino alle porte (595 px). A 1440x900 le stesse cose a sinistra, la zolla a destra alla sua misura (500 px) e il titolo delle macchine a 839 px.
- **Identità.** Il giallo del cartello (#FEE800) torna il colore della ditta: apertura e "Orari e contatti" gialli, il blu dei vomeri (#172544) per l'azienda e i numeri, il rosso BERTO solo nel logo e nello stato "chiuso". Via la carta beige. Titoli con le loro parole: "Macchine speciali per vivai. Giardinaggio e officina." (il titolo della versione 1 più il secondo mestiere), "Attrezzature vivaistiche da noi prodotte", "Siamo concessionari", "Di tutto di più", "La nostra ditta nasce nel 1961.", "Telefonateci o inviateci una e-mail". Tolti la tavola in scala tratteggiata e i titoli da rivista ("Il vomere passa sotto la fila...").
- **Struttura M adattata.** Testata sobria con lingua e il telefono come bottone; apertura con la dichiarazione del mestiere e la loro foto in campo; competenze come macchine per lavoro (sterrare, scalzare, rincalzare, fresare, trapiantare, mettere a dimora, trinciare), ognuna con la foto in studio, il trattore, il peso, il video e la scheda; i video; negozio e officina con la fascia dei marchi e le recensioni; l'azienda con la loro presentazione e sei numeri; orari, contatti e modulo; le tre lingue; piede in quattro colonne.
- **Foto.** Solo materiale di Berto, mai ingrandito: la zolla (FOTO-3, 500x500) in apertura; le otto foto in studio delle schede, tutte nello stesso riquadro 4:3 sul grigio freddo #F1F2F4 (fondo sfumato reso uniforme, ombra tenuta, luce e colore avvicinati allo sterrapiante: è la loro serie di catalogo, non un ritaglio su carta); tre foto in campo della galleria (foto-7, FOTO-2, FOTO-5, quadrate). Tolti il fotogramma SD della Piragna ingrandito a mezza pagina e il disegno in scala. Nessuna foto di repertorio, nessuna illustrazione.

### Ritocco finale (3/11/2026, dopo il controllore del livello e i due clienti tipo)

Controllore: voto 6, regole 5, 10, 11 e 14 non superate; clienti tipo: negozio 8,5, vivaista 8. La pagina prima di questo ritocco è in `_prova/index-prima-del-ritocco-finale.html`. Le modifiche sono in `_prova/script/pro_ritocco_finale.py` (sostituzioni puntuali, valide una volta sola su quella pagina) più alcune rifiniture fatte dopo gli screenshot (spazi dell'apertura, ordine del telefono, testata, schede a 320 px); `sito/index.html` resta la pagina da cui si riparte. Le immagini con `pro_img.py`, il resto con `build_finale.sh`. Le misure della prima schermata scritte sopra in "Che cosa è cambiato" valgono per la versione prima del ritocco: quelle nuove sono qui.

- **Foto in campo, una sola correzione per le quattro** (`pro_img.py`, `campo()`): rapporti medi R/G e B/G portati a quelli di FOTO-2, la più neutra (guadagni tra 0,85 e 1,25), autocontrasto all'1 % sulla luminanza, saturazione meno 10 %, maschera di contrasto (raggio 1, quantità 60). Prima e dopo in `_prova/pro-controllo/campo-prima-dopo.jpg`. Nessun ingrandimento: restano 500 px.
- **Striscia dell'apertura sul telefono**: 500x250 (2:1) dalla metà alta di FOTO-3, con il corpo giallo dello sterrapiante, il volantino e la zolla; a 390 è 390x195, da 647 a 842 px, dentro gli 844.
- **Didascalia in apertura** (l'unica della pagina, 1 su 12 foto): "Lo sterrapiante al lavoro in un vivaio. MOD. 80, 85 e 100, per trattori da 40 a 150 HP: dati e video", link a `#sterrapiante`. Per chi arriva da YouTube lo sterrapiante torna nella prima schermata.
- **Prova in apertura**: la riga dei marchi ora dice "Concessionari Honda e Stihl, anche Goldoni, Grin, Etesia e Toro. Assistenza e ricambi in officina. 4,4 su Google, 58 recensioni" (link alla scheda Google), a 19 px (17 sul telefono), non più solo nell'occhiello di 14 px.
- **Prima schermata a 1440**: apertura 44/36 px, foto a 480 px, H2 delle macchine su una riga (9 colonne): occhiello e titolo finiscono a 891 px, dentro i 900. Spazio sopra la sezione 96 px (regola 12).
- **Salto a "Macchine per vivai"** (porta gialla e menu): l'ancora `#macchine` è sul titolo della sezione e non più sul suo margine; i sette lavori stanno in una riga sotto il testo. A 1440x900 la tabella delle tre versioni finisce a 874 px: si leggono tutti e tre i trattori senza un secondo clic.
- **Sul telefono il negozio viene subito dopo l'apertura** (ordine con `order` solo sotto i 601 px; nel codice e sul computer l'ordine resta: macchine, video, negozio). "Siamo concessionari" parte a 939 px invece che a circa 5400. Il negozio ha il fondo grigio freddo #F1F2F4, così ogni sezione cambia fondo anche nel nuovo ordine (giallo, grigio, bianco, inchiostro, blu, giallo, grigio, piede).
- **Numeri dell'azienda**: quattro su una riga (1961; 12 macchine e attrezzature per vivai nel catalogo; 11 marchi; 4,4 su Google con 58 recensioni). Tolti "14 video" e "4 lingue", riempitivi. Il 4,4 della sezione negozio scende a 48 px, così il gesto a 104 px non si ripete.
- **Un solo sistema di comandi**: le porte dell'apertura sono link a filetto senza fondo (al passaggio inchiostro e testo bianco, senza spostare il testo); i sette lavori sono alti 48 px, testo 17 px, bordo 2 px e raggio 4 px come i `.btn.bordo`.
- **Officina, ricambi, consigli sono link**: riquadri bianchi con il filetto, titolo a 32 px, tutta la superficie cliccabile e la freccia (Officina a `officina.html`, Ricambi al modulo con "Ricambi o accessori" già scelto, Consigli alla tabella degli orari). In Officina: "Per una macchina comprata altrove, chiamateci prima." (invito, non un fatto: la regola vera va chiesta, LEGGIMI). Tolti dalla sezione i due bottoni che ripetevano gli stessi link; resta Chiama più Indicazioni.
- **Schede delle macchine**: "Scheda →" in inchiostro (sottolineato al passaggio), non più grigio da link spento; ogni scheda ha "Prezzo", che apre il modulo con quella macchina già scelta. Sul telefono "Scheda →" non c'è (si tocca la scheda intera).
- **Modulo**: la nota sugli allegati sta sopra il bottone, a 17 px in neretto dentro un riquadro; sotto la tendina, se la macchina è lo sterrapiante, il promemoria "MOD. 80 per trattori da 40/68 HP, MOD. 85 da 60/100 HP, MOD. 100 da 100/150 HP" e "Torna allo sterrapiante". Dopo "Prepara l'e-mail" compare il riquadro "Si è aperta la posta?" con il testo già pronto, "Copia il testo", l'indirizzo e il telefono: su un PC senza programma di posta la richiesta non si perde.
- **Orari**: sopra la tabella il titolo visibile "Orari del negozio e dell'officina"; "Orari della settimana" e "Consigli" portano lì.
- **Testata**: "Scriveteci" (al modulo) accanto al telefono da 1400 px in su; il logo porta a `index.html`; "IT" non è più un link (span con `aria-current`).
- **Titolo sul telefono**: "Macchine speciali / per vivai. / Giardinaggio e officina." (i primi due vocaboli tenuti insieme), niente parola sola in prima riga.
- **Lunghezza**: a 390 la pagina passa da 14.186 a 14.909 px (il negozio in alto non la accorcia, la sposta; le schede macchina sono più alte per "Prezzo").

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`) dopo il ritocco, più gli screenshot guardati a pezzi a 1440, 390, 320, 768 e 1024 e le prime schermate a 1920.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa 88 px a 1440 e 64 a 390, bottone "Tel. 049 640282" alto 48 px; a metà pagina a 390 sta a 8 px dal bordo e `elementFromPoint` dà `tel:+39049640282`. 10 link `tel:`. Per M c'è anche "Scriveteci" in testata da 1400 px.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 con i due mestieri, "Saonara (PD), dal 1961", prove "dal 1961", "Concessionari Honda e Stihl" e "4,4 su Google, 58 recensioni" nel testo a 19/17 px; Chiama a tutta larghezza a 390 (350 px, 52 px di altezza) e Indicazioni.
3. **Immagine vera nell'apertura: passa, con riserva.** La zolla sollevata dallo sterrapiante giallo Berto, foto loro, a 480 px (file di 500); sul telefono la striscia 2:1 mostra la macchina. Non mostra persone né la sede (LEGGIMI, foto da fare).
4. **Zero repertorio: passa.** `indicativ` 0, nessuna immagine da banche, nessuna illustrazione.
5. **Foto in serie: passa, con riserva.** Due serie loro, ognuna con un trattamento unico: otto in studio sullo stesso grigio 4:3; quattro in campo con la stessa correzione del colore (vedi sopra). Formati 2 a 1440 (1:1, 4:3) e 3 a 390 (2:1, 4:3, 1:1); 1 didascalia su 12 foto. Riserva: i fotogrammi in campo restano di 500 px e morbidi; una serie fatta da un solo fotografo è nel LEGGIMI.
6. **Palette dal marchio: passa.** Giallo #FEE800 e rosso #DA251D dal cartello, blu #172544 dai vomeri, inchiostro #16171A, più bianco e grigi freddi. Niente `--carta`; nessun esadecimale fuori da `:root`.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 104) e 8 a 390 (14, 16, 17, 20, 24, 28, 36, 56); testo corrente 19/17 px; minimo 14; H1 64/36, H2 48/28. Gesto di scala: Honda e Stihl e i quattro numeri a 104 px.
8. **Due famiglie al massimo: passa.** Solo Anybody: larghezza 75 % e peso 700 per titoli e cifre, 100 % e 700 per etichette e comandi, 100 % e 400 per il testo.
9. **Servizi in schede con la foto: passa, con riserva.** Sterrapiante in grande con la tabella, poi 7 schede in 4 colonne con foto 4:3, nome, dati, Video, Prezzo e Scheda; tutta la scheda cliccabile. Officina, ricambi e consigli ora sono riquadri cliccabili, ma senza foto: le foto dell'officina non ci sono e non sono inventate.
10. **Almeno tre tipi di prove: non passa (2 su 4).** Numeri aziendali: 4, tutti veri e dell'azienda. Fornitori con didascalia: Honda "Concessionario vendita e assistenza" con il link alla scheda Honda, Stihl, altri nove. Recensioni: tre frasi vere da Google ma senza nome e comune; clienti con il nome: nessuno nelle fonti. Niente inventato: da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Nessun vivaio cliente, luogo o anno nelle fonti; al loro posto i video in campo. Da chiedere tre lavori con nome, comune, anno e macchina (LEGGIMI).
12. **Ritmo a blocchi: passa.** Pieni oltre al piede: apertura gialla, video inchiostro, azienda blu, contatti gialli; negozio e lingue su grigio freddo, macchine su bianco; ogni sezione cambia fondo, anche nell'ordine del telefono. Spazio sopra le sezioni 96-120 px a 1440 e 64-72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno e con il solo bordo, raggio 4 px, altezze 48, 52 e 56, testo 17/16 px; i bottoni di chiamata hanno il numero. I filtri dei lavori seguono lo stesso modello (48 px, 17 px, bordo 2 px); le porte sono link a filetto, non riquadri.
14. **Modulo e "dove e quando" per il mestiere: passa, con riserva.** In home, con tipo di richiesta, macchina (12 voci, con il promemoria dei modelli), trattore oppure marca e modello, nome, azienda, telefono, comune, messaggio; compone l'e-mail (mailto) con oggetto e campi e lascia il testo pronto da copiare. Orari in tabella con titolo, Indicazioni e mappa a link, nessun iframe. Riserva: per M serve l'allegato del disegno o della foto; un mailto non porta allegati, quindi c'è il riquadro "allegatele all'e-mail che si apre" e il campo `input type=file` va aggiunto quando il modulo sarà collegato a un servizio (LEGGIMI).
15. **Piede completo: passa, senza certificazioni.** Quattro colonne a 1440, ragione sociale, P.IVA, indirizzo, telefono, e-mail e indicazioni cliccabili, orari, YouTube con il sottotitolo, Privacy e Cookie; testo da 14 px in su. Certificazioni: nessuna nelle fonti.

### Compiti della scheda d'uso (par. 8)

- *Visitatore 1, telefono 390x844*: stato giusto a tutte le ore provate (`pro_uso.mjs`): martedì 10 "Aperto ora, chiude alle 12"; 12.30 "Chiuso ora, riapre alle 14"; 19.30 "riapre domani alle 8"; sabato 13 e domenica "riapre lunedì alle 8"; 8 dicembre e Pasquetta "Chiuso oggi, festivo. Riapre domani alle 8"; vigilia di Natale sera "riapre lunedì" (salta Natale, Santo Stefano e la domenica). Chiama (52 px) e Indicazioni senza scorrere; Honda e Stihl, più Goldoni, Grin, Etesia e Toro, nella prima schermata; la sezione Negozio e officina viene subito dopo l'apertura (939 px) con Officina, Ricambi e Consigli cliccabili; la tabella degli orari, con il suo titolo, a un tocco da "Orari della settimana".
- *Visitatore 2, computer 1440x900*: lo sterrapiante nella didascalia della foto in apertura, con i tre modelli e il link; titolo delle macchine nella prima schermata (fino a 891 px); dalla porta gialla la tabella delle tre versioni intera sullo schermo (fondo a 874 px); "Prezzo" in ogni scheda con la macchina già scelta, il promemoria dei modelli nel modulo e il testo pronto da copiare se la posta non si apre; i sette lavori come bottoni; lo sterrapiante con le tre versioni, il trattore e il peso in testo vero; "Guarda il video" accanto; "Chiedete il prezzo" e la riga "Prezzo su richiesta" con telefono e richiesta sotto le schede; il telefono resta nella testata. Sul telefono ogni macchina è una riga di circa 130-190 px con il video a un tocco.
- *Visitatore 3, in inglese*: EN nella testata a 1440 e nella prima riga dell'apertura sotto i 1180 px; porta a "In English" (elenco delle macchine con i dati, telefono +39 049 640282, e-mail con oggetto "Request from the website"); tedesco e francese con un paragrafo e i contatti.
- *Identità*: cartello giallo BERTO vero e una foto loro nella prima schermata; "1961" e "Saonara" prima del piede; nessuna metafora.

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920; nessuna sovrapposizione negli screenshot guardati a pezzi (corretti durante il lavoro: i numeri dell'azienda, che a 1440 su sei colonne si toccavano, ora su tre; la tabella delle versioni sul telefono, con il peso finito sulla riga sbagliata; il titolo a 1024 su quattro righe).
- Collegamenti: `tel:+39049640282` ovunque; `mailto:bertopd@libero.it` con oggetto (anche in inglese, tedesco, francese); Indicazioni `google.com/maps/dir/?api=1&destination=Berto Guerrino, Via Caovilla 27/B, 35020 Saonara PD`; mappa e recensioni con `maps/search`; video `youtu.be/...` del loro canale; nessuna ancora senza destinazione; nessun errore di script. Le pagine interne (`macchine/...`, `giardinaggio.html`, `officina.html`, `azienda.html`, `privacy.html`, `cookie.html`) sono quelle proposte del sito nuovo, come nella versione 1.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

- **Anybody** (Etcetera Type Co.), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; licenza in `sito/fonts/OFL.txt` (scaricata da github.com/google/fonts il 3/11/2026). Servito dalla pagina (`sito/fonts/anybody-latin.woff2`, variabile in larghezza e peso).
- Foto e logo: materiale del loro sito e della galleria, da usare con il loro permesso. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.
