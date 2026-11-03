# Home Belletti

## Metodo ibrido (novembre 2026)

Rifatta il 3/11/2026 con il metodo ibrido scelto dal committente: prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`; sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola. La versione professionale è copiata com'era in `_prova/versione-pro/` (sito e screenshot). Direzione scritta prima dell'HTML in `_prova/alto/DIREZIONE.md`; riga del carattere aggiunta in coda a `_metodo/professionale/alto/REGISTRO-CARATTERI.md`.

### Direzione

- **Idea**: Belletti risponde anche quando gli uffici sono chiusi. La sede di Mestrino accesa di sera, con il furgone "Manutenzione Ascensori" davanti alla porta, e sopra la loro frase "in qualsiasi ora del giorno" (`assistenza.aspx`).
- **Modello Q** (riga di Belletti nel capitolo 5; riferimenti Schmitt + Sohn ed Emch, prime schermate rifatte in `_prova/alto/concorrenti/`). Strada di D2 "tra 800 e 1600 px": la foto più grande del mezzo è di 869x1263, quindi va alla misura vera, centrata, con il titolo sopra. Sta esattamente sulle colonne 3-10 della griglia (866x900 a 1440, scala 0,997) e va dal bordo alto al bordo basso dello schermo. La testata fissa è trasparente sopra la foto (sfumatura locale in alto) e diventa piena appena si scorre; senza JavaScript resta piena.
- **Gesto**: "In qualsiasi ora del giorno." in Outfit 300 a 144 px sull'asfalto della foto, che esce dai bordi della foto sul fondo notte. È l'unico elemento sopra i 100 px. La sera torna una volta sola, nel culmine (Galleria Cavour accesa, stesso fondo).
- **Registro**: Outfit (SIL OFL 1.1), una sola famiglia, 300 per i titoli, 400 per il testo, 500 per le etichette e il bottone. `h1` 144 px a 1440 e 52 a 390, `h2` 44 e 32, testo 19 e 17, didascalie e dati 16, interfaccia 14. Radio Canada esce. Outfit non è in nessun'altra delle home (`caratteri-usati.txt`, `REGISTRO-CARATTERI.md`).
- **Frase che torna**: "in qualsiasi ora del giorno" nell'`h1`, nella prima riga dell'assistenza e nei contatti.

### Che cosa è cambiato

- **Prima schermata a 1440**: logo, cinque voci (Manutenzione, Ammodernamento, Piattaforme e servoscala, Lavori, Contatti), "Uffici 049 508 2430" come link, un solo bottone "Guasti 24 ore 049 900 5131"; sotto, la foto, il titolo e una riga: "Ascensori, piattaforme e servoscala di qualsiasi marca. Mestrino, dal 1908." Tolti l'`h1` di 22 parole, l'occhiello, i due bottoni, i due link e le quattro garanzie in fila.
- **A 390**: la foto a tutto schermo, il titolo, la riga, e la barra fissa in basso con "Persona bloccata in cabina o guasto: 24 ore su 24, 365 giorni all'anno." e il bottone "Chiama i guasti 049 900 5131" (350x56 px), che resta in ogni schermata. Sopra solo logo e Menu.
- **Sotto la piega, sette sezioni in tutto** (prima quattordici): apertura; "Cosa succede dopo la chiamata" (i tre casi, la manutenzione in una frase, il cambio di manutentore, la zona con le sette province e il tecnico al quadro); "Per quale edificio?" (la scelta di Schmitt + Sohn: condominio, casa, negozi e aziende, edifici nuovi e di pregio, quattro tessere con la stessa foto 4:3, i prodotti e i loro dati dentro e il sopralluogo con il tipo già scelto nel modulo); il culmine (Galleria Cavour, foto 4:5 di 755x944, didascalia "Galleria Cavour, piazza Cavour, Padova / ottobre 2007", committente, cinque dati, progettisti); Ca' Michiel e Ca' della Nave con i loro dati e "Per i progettisti" con il mailto all'ufficio tecnico; "Un'impresa di famiglia, con i suoi tecnici" con l'ufficio e "Certificati e norme"; i contatti sul verde (l'unico blocco del colore del marchio) con il numero dei guasti grande, gli uffici, l'email, la sede, "Indicazioni stradali" e il modulo di cinque campi.
- **Una griglia sola**: 12 colonne, margini di 64 px a 1440 (20 a 390), contenuto da 64 a 1376 px in tutte le sezioni, foto con i due bordi sulle linee delle colonne.
- **Tolti** la fascia dei numeri (4, 35, 20+, 1997), tutti gli occhielli, le sei schede per prodotto, i doppioni dei numeri (ora ognuno al massimo due volte in vista), la colonna dei contatti nel piede, le due citazioni dell'ing. Viel sugli impianti.
- **Tolti perché da confermare**: "di norma i guasti si risolvono entro la stessa giornata" (LEGGIMI, punto 1; ora "I nostri tecnici analizzano le cause e ripristinano l'impianto nel più breve tempo", da `assistenza.aspx`), "4 generazioni" e "35 dipendenti" (punti 8 e 9). Il caso fuori orario resta come chiede la SCHEDA, con la sua domanda nel LEGGIMI.
- **Foto**: gli originali in `assets/originali/` erano spariti con il riavvio. Ho riscaricato il depliant del 2008 dal sito Belletti e rifatto le immagini con `pdfimages` (`assets/originali/depliant/`, stessi numeri). Ca' della Nave viene dalla copia della versione professionale (`assets/originali/dibaio/`), perché il redazionale DiBaio non è più online. Dieci foto, tre formati (apertura, 4:5, 4:3), un solo trattamento (`_prova/alto/script/immagini.py`), la targa del furgone sfocata, nessuna ingrandita, nessuna scurita in blocco. Provini in `_prova/alto/provini.jpg`.

### Misure

Con `node _prova/alto/misura-d.mjs`, che è `misura.mjs` della diagnosi esteso alle soglie D e del metodo ibrido (esito anche in `_prova/alto/misura-d.json`). Passano tutte e 31.

| Misura | 1440x900 | 390x844 | Soglia |
|---|---|---|---|
| Foto nella prima schermata | 60,2% (866x900, scala 0,997) | 100% | 60% o più; 50% a 390 |
| Cliccabili nella prima schermata | 8 | 3 | 8 (S); 4 |
| Bottoni nella prima schermata | 1 | 1 | 1 |
| Caratteri fuori dal menu | 151 | | 160 |
| Cifre di 30 px o più in apertura | 0 | 0 | 0 |
| `h1` | 5 parole, nessuna virgola | | 9 parole |
| Occhielli | 0 | | 1 con un fatto |
| Famiglie, elementi oltre i 100 px | 1 (Outfit), 1 | | 2, 1 |
| Parole | 857 | | 900 |
| Sezioni | 7 | | 7 |
| Altezza | 7.434 px | 11.028 px | 7.500 a 1440 |
| Numeri di 30 px o più in pagina | 1 (il numero dei guasti nei contatti) | | 1 |
| Foto, formati | 10, 3 | | 12, 3 |
| Fondi, sezioni verdi | 3 (notte, carta, verde), 1 | | 3, 1 |
| Spazi tra le sezioni | 96 e 144 px | 56 e 84 px | due valori, uno 1,5 volte l'altro |
| Numero dei guasti in vista | 2 (testata, contatti) | 2 (barra, contatti) | 2 |
| Numero degli uffici, email, indirizzo | 2, 2, 2 | 1, 2, 2 | 2 |
| Bottoni in pagina | 2 | 2 | 5 |
| Peso | 435 KB | 397 KB | 3 MB |
| Lista nera, "indicativ", U+2014 | 0, 0, 0 | | 0 |

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/controlli.mjs`): nessuno scorrimento orizzontale, nessun testo fuori dallo schermo, nessuna foto ingrandita, nessun errore di script. L'unica sovrapposizione che lo script segnala ("Note" con il riquadro della targa) è il campo dentro il `details` chiuso, che non si vede; aperto, finisce 118 px sopra il riquadro. Link `tel:` solo `+390499005131` e `+390495082430`; tre `mailto:` a info@bellettiascensori.it (ufficio tecnico con oggetto e traccia, copie dei certificati con oggetto e traccia, contatto semplice) più quello composto dal modulo. Menu sotto i 1100 px: si apre, mostra sei voci, si chiude al tocco e porta l'ancora sotto la testata. Modulo: il link "Sopralluogo per l'ammodernamento" sceglie il tipo, l'invio vuoto si ferma con l'avviso e il fuoco sul nome, l'email composta ha l'oggetto "Richiesta: Sopralluogo per ammodernamento, Selvazzano Dentro". Contrasti: testo secondario #575A5D su #F1F1EE 6,1:1, #B9BCBF su #16191C 9,3:1, bianco sul verde #007A43 5,4:1, link verde su carta 4,8:1, testo su carta 15:1; fuoco visibile con un contorno giallo di 3 px.

Screenshot rifatti con gli stessi nomi, più `home-1024-prima-schermata.jpg` e `home-768-prima-schermata.jpg`. Guardati a pezzi accanto alla versione professionale e a Schmitt + Sohn ed Emch (`_prova/alto/confronto-1440.jpg`).

### I compiti della SCHEDA, dove stanno ora

- **Visitatore 1, telefono.** Chiamare i guasti: barra fissa in basso, bottone `tel:+390499005131` di 350x56 px visibile all'apertura e toccabile a metà pagina. "24 ore su 24, 365 giorni all'anno" e "persona bloccata in cabina" scritti nella barra, accanto al bottone; il numero degli uffici non è in prima schermata, quindi non si confonde (nei contatti ha l'etichetta "Uffici e sopralluoghi"). I tre casi "dopo la chiamata" sono la prima sezione sotto l'apertura: da 1125 a 1571 px, 447 px contro 657 utili, interi in uno schermo al primo scorrimento. "Qualsiasi marca" nella riga sotto il titolo, senza scorrere.
- **Visitatore 2, computer.** Manutenzione, ammodernamento, piattaforme e servoscala: nel menu della prima schermata, e "qualsiasi marca" nella riga sotto il titolo. Zona: le sette province e il Friuli a 1412 px, nella seconda schermata. Fiducia entro due schermate: "dal 1908" e Mestrino in apertura, "Dal 1997 la linea diretta" nella prima riga dell'assistenza; ISO 9001 e la Galleria Cavour più giù (5842 e 2888 px), un clic da "Lavori" nel menu. Sopralluogo: "Uffici 049 508 2430" nella testata a 1440, il modulo a un clic da "Contatti" e dai link delle tessere, con il tipo già scelto.
- **Visitatore 3, progettista.** "Lavori" nel menu porta al culmine con la scheda completa di Galleria Cavour; Ca' Michiel e Ca' della Nave subito dopo, con i cinque dati. L'indirizzo dell'ufficio tecnico è scritto per intero con il mailto, l'oggetto e cosa allegare. "Certificati e norme" a un clic dal piede, con le prime emissioni e la richiesta delle copie aggiornate.

### Problemi aperti

- **La foto d'apertura è del 2008 e di 869 px**: il 60,2% passa di poco e solo perché la foto va da bordo a bordo sotto la testata trasparente. A 1920 la quota scende al 45%, sugli schermi 2x la foto è morbida. Serve il servizio fotografico del LEGGIMI (la squadra davanti alla sede, al crepuscolo, almeno 4000 px).
- **Il mestiere nel titolo**: risolto nel ritocco qui sotto ("Ascensori, in qualsiasi ora del giorno."). Il controllo D1 con persone vere resta da fare.
- **La "persona bloccata" a 1440 non è nella prima schermata**: il tetto dei 160 caratteri non lascia posto. Il bottone dice "Guasti 24 ore" e la frase completa sta nella prima riga della sezione dopo e nei contatti.
- **"Casa"**: la foto (`d-029`) mostra un piccolo ascensore accanto a una scala in pietra; non so se è una piattaforma o un'abitazione privata, e l'alt dice solo quello che si vede. Va chiesta una foto vera di una piattaforma in una casa.
- Anni di fine lavori di Ca' Michiel e Ca' della Nave: ancora mancano (LEGGIMI, punto 14); dopo il ritocco la seconda voce delle didascalie è la data del redazionale (2008) e del concorso (2006).
- Gli orari degli uffici mancano ancora (punto 2), quindi niente stato aperto o chiuso in testata.
- Il controllo dell'ondata D4 (media delle prime schermate della zona) va rifatto quando ci sono le altre home di Rubano e Mestrino.

### Alto livello: ritocco dopo il giudice e i clienti tipo (3/11/2026)

Il giudice da agenzia aveva dato 6,5 (prima 5,5): apertura riconoscibile, ma il mestiere non si legge nella miniatura (D1), `h1` a 122,56 px e non a 144 (D5), foto d'apertura senza didascalia (D10), culmine con 600 px di nero vuoto, Ca' Michiel e Ca' della Nave sfalsate, tessere con trattamenti diversi e link ad altezze diverse, logo illeggibile e barra alta 112 px a 390, bottone appeso a metà testata a 1024. I clienti tipo non trovavano: a 390 i tre casi "dopo la chiamata" finivano sotto la barra dei guasti (dopo il menu, terzo caso fino a 799 px con la barra a 721) e non c'era un link nella prima schermata; a 1440 zona, ISO 9001 e Galleria Cavour non c'erano entro due schermate; dopo "Lavori" la scheda di Cavour non stava intera nello schermo. La sezione D non torna indietro: dove un cliente chiedeva di più nella prima schermata, la risposta è in testata, nel menu o nella seconda schermata. La pagina di prima è copiata in `_prova/alto/ritocco/index-prima-del-ritocco.html`, le immagini tolte in `_prova/alto/ritocco/vecchie/`.

**Applicati**

- **Mestiere nel titolo (D1, D7)**: `h1` "Ascensori, in qualsiasi ora del giorno." (6 parole, 1 virgola), su due righe a 144 px da 64 a 1349 px. La miniatura a 300 px (`_prova/alto/ritocco/miniatura-300.jpg`) ha "Ascensori" alto circa 21 px. Il titolo parte ora dal margine (64 px) e non dalla colonna 2: a 144 px "Ascensori, in qualsiasi" è largo 1285 px e da 175 non ci sta.
- **Scala (D5)**: `font-size:clamp(52px,10vw,144px)`, cioè 144 px a 1440 e 1920, 102 a 1024, 52 a 390.
- **Riga e didascalia d'apertura (D10)**: sopra i 1100 px, dove il menu nomina già manutenzione, ammodernamento, piattaforme e servoscala, la riga è "Impianti di qualsiasi marca, dal 1908."; la didascalia a due voci "La sede di Mestrino / depliant 2008" sta nelle colonne 11-12, sul fondo notte, con il fondo allineato alla riga. "2008" è l'anno del depliant da cui viene la foto, non la data dello scatto. Fino a 1100 px la riga resta "Piattaforme e servoscala di qualsiasi marca. Mestrino, dal 1908." (il menu è chiuso) e la didascalia si toglie sotto i 900. Caratteri a 1440: 159 su 160.
- **Culmine**: Galleria Cavour tagliata più bassa dall'originale (`d-037`, 948x839, rapporto 1,13), mostrata 867x767 sulle colonne 1-8 (scala 0,91). Nelle colonne 9-12 il manifesto "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito" in alto a filo della foto (52 px, 4 righe); in basso, a filo del fondo della foto, la didascalia e la scheda. Vuoto nella colonna destra: circa 165 px. Dopo "Lavori" nel menu la foto parte a 88 px e la scheda sta da 526 a 855 px su 900. A 1024 il manifesto va su tutta la riga e foto e scheda sotto (colonne 1-7 e 8-12).
- **Ca' Michiel e Ca' della Nave**: Ca' della Nave rifatta 789x551 (rapporto 1,43), le due foto alte 527 px; le due colonne sono un `subgrid` a quattro righe, quindi didascalie (4579/4580) e dati (4800/4800) cadono alla stessa altezza. La seconda voce delle didascalie è ora una data delle fonti (LEGGIMI, punto 14): "redazionale del 2008" e "concorso del 2006"; "palazzo gotico" ed "ex scuderie di Villa Grimani Morosini" sono passati nel testo.
- **Tessere "Per quale edificio?"**: rifatte con `_prova/alto/script/immagini-ritocco.py`, stesso trattamento per le quattro (bianco più forte verso il neutro, saturazione 0,85, poi R e B portati a G+6 e G-6): differenza R-B media 12, 12, 12 e 11. Righe in `subgrid`: i quattro link partono alla stessa altezza (2587 px a 1440).
- **Chi siamo**: tolta la foto dell'ufficio con i monitor del 2008; la citazione dell'ing. Viel è il manifesto a 32 px nelle colonne 8-12, accanto al racconto. Foto in pagina: 9.
- **Testata e barra a 390**: logo largo 100 px (prima 45); barra alta 69 px (prima 112): a sinistra "Persona bloccata o guasto: / 24 ore su 24, 365 giorni" a 14 px su due righe fisse, a destra il bottone "Chiama i guasti 049 900 5131" (147x52). Sotto i 340 px la frase si toglie e il bottone prende tutta la larghezza.
- **Testata a 1024**: il bottone dei guasti finisce a 872 px, 21 px prima di "Menu" (893).
- **Clienti tipo, telefono**: nella prima schermata a 390 c'è il link "Cosa succede dopo la chiamata" (quarto cliccabile, il tetto è 4) che porta i tre casi da 285 a 732 px, sopra la barra (775); lo stesso dal menu "Manutenzione". Il `lead` scende a 17 px sotto i 600 px.
- **Clienti tipo, computer**: la seconda schermata ha la zona nel `lead` ("nelle province del Veneto e in parte del Friuli", a 1063 px) e un riquadro "A Mestrino dal 1908" sotto la zona: "ISO 9001 dal 4 novembre 1997, prima emissione", con il link a certificati e norme, e la Galleria Cavour per il Comune di Padova, con il link al culmine (1596-1782 px, dentro le due schermate).
- **Istruzioni a 14 px (D7)**: "Per un guasto non scrivete..." e "Allegatele all'email..." ora a 14 px. In `misura-d.mjs` le classi `.avv` e `.allega` sono escluse dal controllo del testo corrente (16 px o più), perché sono istruzioni e D7 le vuole a 14.

**Respinti, con il motivo**

- `h1` su tre righe, come proponeva il giudice: a 144 px copriva il furgone. Due righe dal margine tengono il furgone libero.
- Accorciare i link delle tessere a "Sopralluogo": il `subgrid` li allinea già e il testo lungo dice che cosa si chiede.
- "Piani serviti" uguale a "Fermate": è la parola del redazionale di Ca' Michiel, resta com'è.
- Anni di fine lavori di Ca' Michiel e Ca' della Nave: le fonti non li danno; in didascalia ci sono le date vere del redazionale e del concorso.
- Zona nella prima schermata a 1440: con il titolo, la riga, la didascalia e i due numeri si arriva a 159 caratteri su 160; la zona va nella prima riga della seconda schermata.
- Quota della foto a 1920 (45%): la foto è di 869 px e non si ingrandisce; resta il servizio fotografico.

**Misure finali** (`node _prova/alto/misura-d.mjs`, 31 controlli, passano tutti)

| Misura | 1440x900 | 390x844 |
|---|---|---|
| Foto nella prima schermata | 60,2%, scala 0,997 | 100% |
| Cliccabili, bottoni | 8, 1 | 4, 1 |
| Caratteri fuori dal menu | 159 | |
| `h1` | 144 px, 6 parole, 1 virgola | 52 px |
| Parole | 899 | |
| Altezza | 7.149 px | 10.759 px |
| Foto, formati, ingrandite | 9, 3, 0 | |
| Famiglie, elementi oltre i 100 px | 1 (Outfit), 1 | |
| Fondi, sezioni verdi, spazi | 3, 1, 96 e 144 px | 56 e 84 px |
| Tre casi in uno schermo | 376 su 820 px | 447 su 711 px |
| Peso | 434 KB | 379 KB |
| U+2014, lista nera, "indicativ" | 0, 0, 0 | |

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/controlli.mjs`): nessuno scorrimento orizzontale, nessun testo fuori dallo schermo, nessuna foto ingrandita, nessun errore di script; menu, ancore e modulo come prima. Resta segnalata solo la sovrapposizione del campo "Note" chiuso nel `details`, che non si vede. Posizioni dei difetti del giudice con `_prova/alto/ritocco/posizioni.mjs`. Screenshot rifatti con gli stessi nomi (`home-1440.jpg` ora 7.149 px, `home-390.jpg` 10.828 px) e guardati a pezzi.


### Secondo giro (3/11/2026)

Dopo il primo ritocco il giudice da agenzia era a 6,5 e i clienti tipo erano scesi sotto la versione professionale (cliente 1 da 8 a 7,5, cliente 2 da 8 a 6,5). Questo giro ha due obiettivi insieme: rimettere ai clienti tipo quello che avevano perso senza rompere i tetti D3, e dare sotto la piega l'esecuzione che il giudice chiedeva. La pagina di prima è in `_prova/alto/ritocco2/index-prima-del-secondo-giro.html`, le immagini tolte in `_prova/alto/ritocco2/vecchie/`. Le nuove foto vengono da `_prova/alto/script/immagini-secondo-giro.py`; i controlli nuovi sono in `_prova/alto/ritocco2/posizioni2.mjs` e `schermate.mjs`.

**Per i clienti tipo**

- **Testata (difetto bloccante del giudice)**: ora è una fila sola, logo, menu e numeri, che non si accavalla a nessuna larghezza. Sopra i 1360 px dopo lo scorrimento c'è "Uffici 049 508 2430" (area di 48 px), con almeno 42 px di distanza dal menu: a 1366 sono 42, a 1440 sono 110. Tra 1151 e 1359 px il numero degli uffici resta nei contatti. Fino a 1150 px il menu va nel pannello. Nella prima schermata a 1440 resta un solo numero, quello dei guasti, e i cliccabili scendono a 7.
- **Stato della linea**: nel bottone dei guasti e nella barra del telefono c'è un punto verde chiaro, con l'etichetta "linea attiva 24 ore su 24" per i lettori di schermo. È sempre acceso perché la linea risponde 24 ore su 24 (`assistenza.aspx`). Per gli uffici non c'è nessuno stato: gli orari non sono pubblicati (LEGGIMI, punto 2).
- **Menu con le parole del cliente**: a 1440 le voci sono Manutenzione, Ammodernamento, Piattaforme e servoscala, Lavori e Contatti, e ognuna porta in un punto diverso:
  - Manutenzione arriva con "Dove interveniamo" in vista;
  - Ammodernamento arriva sulla riga 01, "Condominio: manutenzione e ammodernamento";
  - Piattaforme e servoscala arriva sulla riga 02, "Casa: piattaforme e servoscala";
  - Lavori arriva con nome, luogo, data, committente e i cinque dati di Galleria Cavour, da 347 a 724 px su 900;
  - Contatti arriva con il modulo intero, bottone compreso.
- **Pannello del menu (telefono e fino a 1150 px)**: la prima voce è "Guasti: cosa succede dopo la chiamata", poi Chi siamo. In fondo ci sono due righe di 54 px con l'etichetta: "Guasti 24 ore 049 900 5131" e "Uffici 049 508 2430".
- **Tre casi a 390**: il link della prima schermata e la prima voce del menu portano all'elenco (`#casi`). Dopo il tocco i tre casi stanno da 152 a 599 px, sopra la barra che parte a 775. "Qualsiasi marca" è nella riga sotto il titolo.
- **Seconda schermata a 1440 (cliente 2)**: "Dal 1908 Belletti si occupa di ascensori; dal 1997 la linea diretta..." sta a 1063 px. È la frase del depliant, e sostituisce "A Mestrino dal 1908", che il giudice dava per sbagliata. "Dove interveniamo", con le sette province e "in parte del Friuli", sta a 1445 px. ISO 9001 con la prima emissione del 4 novembre 1997 sta a 1760 px. Mestrino è nella riga dell'apertura. "Certificati e norme" non è più ripetuto: c'è una volta sola, nella fascia sotto l'assistenza, e il piede ci porta con un clic.
- **Contenuti della versione professionale riportati**: la citazione dell'ing. Viel sugli anni '60 e '70 ("Non basta conoscere le norme attuali...") torna nella riga del condominio, accanto al link del sopralluogo. Torna anche la voce del menu che apre una riga con la parola "ammodernamento" nel titolo.
- **Finiture d'uso**:
  - i link di uffici, email e indicazioni nei contatti hanno un'area di 48 px;
  - il facoltativo del modulo ha un segno "+" che diventa "−" quando si apre;
  - la riga della foto della targa non ha più il bordo tratteggiato, che sembrava una zona dove trascinare un file;
  - i pulsanti di scelta sono bianchi e a 390 vanno in colonna;
  - "Quando" occupa tutta la riga.

**Sotto la piega**

- **Una griglia sola, tre linee di partenza**: ogni blocco parte dalla colonna 1, 5 o 9 (64, 509 e 955 px a 1440). Le linee 843 e 1066 non si usano più. Le due foto grandi stanno sulle colonne 1-8, i testi a lato sulle 9-12.
- **Il gesto che torna una volta**: l'apertura è la sede di sera sulle colonne 1-8, con il fondo notte a destra e la didascalia a due voci "La sede, di sera / depliant 2008". Il culmine ripete lo stesso gesto: Galleria Cavour di sera, stessa misura (867x900, stesso formato), stesso posto e stesso fondo.
- **Titolo senza cuciture**: "Ascensori," a 144 px e "in qualsiasi ora del giorno." a 66 px stanno tutti dentro la foto, da 169 a 898 px, con la foto che finisce a 931. Nessuna lettera è tagliata dal bordo e il furgone resta libero. A 390 il titolo va su due righe: "Ascensori," a 64 px e il resto a 29 px su una riga.
- **Una riga sola per tutte le larghezze**: "Impianti di qualsiasi marca, da Mestrino (Padova)." Contiene il mestiere e il luogo, e non c'è più la doppia versione `largo`/`stretto`. Il 1908 è passato alla prima frase della seconda schermata. I caratteri nella prima schermata sono 148 su 160, non più 159.
- **Un culmine che culmina**: una foto dominante. A destra, in alto, il manifesto "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito". Sotto, la didascalia vera a due voci "Galleria Cavour, piazza Cavour, Padova / ottobre 2007", che apre la scheda: committente, descrizione, i cinque dati e i progettisti.
- **Moduli diversi, non cinque uguali**:
  - assistenza: testo a 7 colonne e un lato a 4, poi la fascia dei certificati;
  - "Per quale edificio?": a sinistra titolo e due foto, a destra un indice numerato da 01 a 04 con nome, testo e link diversi per ogni riga. Prima c'erano quattro schede uguali con due link uguali;
  - culmine: foto grande e colonna;
  - altri lavori: Ca' della Nave sulle colonne 1-7 e Ca' Michiel sulle 9-12, foto alte uguali (566 px) e didascalie allineate, poi la fascia dei progettisti;
  - chi siamo: la storia come una frase lunga a 29 px, senza citazione debole;
  - contatti: verde, con il modulo su due colonne.
- **Foto (D10)**: le foto sono 7 invece di 9. Sono uscite "Casa", che non si sa se sia una piattaforma, e "Edifici nuovi", che sembrava un rendering. Restano tre formati:
  - notte 0,963 per apertura e Cavour;
  - verticale 0,744 per Ca' Michiel e il tecnico;
  - 4:3 per Ca' della Nave, la scala d'epoca e il montauto.

  Il trattamento è uno solo per tutte: bianco verso il neutro, saturazione 0,88, la stessa curva e la stessa temperatura, con R-B medio tra 4 e 8 in tutte e sette (provini in `_prova/alto/ritocco2/provini-s2.jpg`). Nessuna foto è scurita in blocco e nessuna è ingrandita.
- **Ripetizioni tolte**:
  - il riquadro "A Mestrino dal 1908", con ISO e Cavour che erano detti due volte;
  - la zona nel piede, ora detta due volte: nella seconda schermata e nel menu;
  - la citazione "affiancamento dei giovani";
  - il secondo "Sopralluogo e preventivo".

  Ogni numero di telefono si vede al massimo due volte.
- **Finiture del giudice**:
  - "Montacarichi e montaoggetti", senza la virgola;
  - Ca' Michiel con una sola coppia di due punti;
  - "pubblicato nel 2008" al posto di "redazionale del 2008";
  - le tabelle dei dati con lo stesso ritmo nei tre lavori, senza spazi distribuiti, e su una riga anche a 390;
  - `text-wrap:balance` sui titoli, per evitare parole sole ("tecnici", "in");
  - spazi indivisibili in "12 kg", "3 m/s", "EN 81-28", "365 giorni" e "ing. A. Viel";
  - riga legale allineata sulla linea di base;
  - rientro ottico della "A" del titolo;
  - il tecnico a tutta larghezza a 390;
  - il furgone intero a 390 (`object-position` all'82%);
  - nessun doppio filetto sotto l'indice.

**Misure finali** (`node _prova/alto/misura-d.mjs`, 31 controlli su 31)

| Misura | 1440x900 | 390x844 |
|---|---|---|
| Foto nella prima schermata | 60,2% (867x900, scala 0,998) | 100% |
| Cliccabili, bottoni | 7, 1 | 4, 1 |
| Caratteri fuori dal menu | 148 | |
| `h1` | 144 px ("Ascensori,"), 6 parole, 1 virgola | 64 px |
| Parole | 870 | 873 |
| Altezza | 7.240 px | 10.316 px |
| Foto, formati, ingrandite | 7, 3, 0 | |
| Famiglie, elementi oltre i 100 px | 1 (Outfit), 1 | |
| Fondi, sezioni verdi, spazi | 3, 1, 96 e 144 px | 56 e 84 px |
| Tre casi in uno schermo | 376 su 820 px | 447 su 711 px; dal link da 152 a 599 px, barra a 775 |
| Prove entro due schermate (1440) | 1908 a 1063 px, zona a 1445 px, ISO 9001 a 1760 px; Cavour a un clic | |
| Peso | 448 KB | 357 KB |
| U+2014, lista nera, "indicativ" | 0, 0, 0 | |

Controlli a 320, 390, 768, 1024, 1440 e 1920 (`_prova/alto/script/controlli.mjs`): nessuno scorrimento orizzontale, nessun testo fuori dallo schermo, nessuna foto ingrandita, nessun errore di script. Menu, ancore e modulo funzionano: il link del condominio sceglie "Sopralluogo per ammodernamento", l'invio vuoto si ferma con l'avviso, l'email composta è giusta. Le due sovrapposizioni segnalate non si vedono:
- "Ascensori," con la seconda riga del titolo: si toccano le scatole di riga, non le lettere;
- "Note" nel `details` chiuso.

Testata a 1101, 1151, 1200, 1280, 1300, 1339, 1340, 1366, 1440 e 1920, in alto e dopo lo scorrimento: nessuna sovrapposizione. Lo spazio minimo tra il menu e il numero o il bottone è di 40 px. Screenshot rifatti con gli stessi nomi (`home-1440.jpg` di 7.240 px, `home-390.jpg` di 10.316 px) e guardati a pezzi, insieme alle prime schermate a 320, 1024 e 1920.

**Resta aperto**

- Le parole sono 870: passano la soglia ibrida di 900, non le 750 della D8. Lo stesso vale per l'altezza, 7.240 px contro i 6.000 della D8. Per scendere ancora andrebbero tolti contenuti che servono ai clienti tipo (manutenzione, certificati, progettisti).
- A 1440 e soprattutto a 1920 la colonna a destra della foto d'apertura è fondo notte quasi vuoto, con il bottone in alto e la didascalia in basso. È voluto, perché il culmine fa lo stesso, ma si allarga solo con una foto più grande: il servizio fotografico del LEGGIMI.
- A 320x640 la parte bassa del titolo tocca le ruote del furgone, anche con il titolo ridotto a 48 px sui telefoni bassi. A 360 e 390 il furgone è libero.
- "Dal 1908 Belletti si occupa di ascensori" è la frase del depliant e del sito: in pagina è riportata così, e il punto 9 del LEGGIMI resta da chiedere.
- Nessun logotipo o insegna è stato ridisegnato in questo giro: il logo è quello vettoriale estratto dal depliant.


---

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh`: immagini con `pro_img.py`, controllo dei testi e delle immagini citate, screenshot con `shot_finale.mjs`, poi `pro_controlli.mjs` (le 15 regole, esito anche in `_prova/pro_controlli.json`) e `pro_prova.mjs` (menu, ancore, modulo). Le modifiche del ritocco finale alla pagina sono in `_prova/script/ritocco_css.py` e `ritocco_html.py` (sostituzioni esatte, già applicate).

La home di prima ("Il carattere dell'edificio", con la sua NOTA e i suoi screenshot) è copiata com'era in `_prova/versione-1-originale/`.

Screenshot, stessi nomi di prima: `home-1440.jpg` (10878 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (15581 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti (prime schermate di tutti e 14, pagine intere di Wilson ed Eggentaler); prime schermate e pagine intere anche a 320, 768, 1024 e 1920 (PNG cancellati dopo la lettura).

## Livello professionale, ritocco finale (3/11/2026)

Richieste del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; per le foto "niente" (nessun repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese). Scheda d'uso: `_prova/uso/SCHEDA.md`. Il ritocco parte dal controllo del livello professionale (voto 6, regole 5, 11, 12 e 14 non passate) e dalle due prove con i clienti tipo (voti 8 e 7,5).

### Che cosa è cambiato in questo ritocco

- **L'apertura ha un gesto suo.** Prima: titolo a sinistra, foto con il raggio a destra su fondo bianco, lo schema delle altre home della campagna. Ora l'apertura è un blocco antracite alto quanto lo schermo (fino a 812 px); la foto della sede di sera con il furgone (`d-027`) è al vivo nella metà destra, senza raggio, e sfuma nel fondo con un gradiente, così il notturno diventa atmosfera invece di un rettangolo nero. Sul telefono è una fascia che chiude lo schermo, sfumata dall'alto. Tolta la didascalia; dei tre link sotto i bottoni ne restano due ("Cosa succede dopo la chiamata", "Progettisti: i lavori con i dati tecnici").
- **Le garanzie continuano il blocco scuro**: quattro invece di tre, con "Qualità certificata dal 1997" (ISO 9001 dal 4 novembre 1997, Allegato XI dal 1999, link a "Qualità e norme"), separate dall'apertura da un filetto. Testo a 19 px. Sul telefono restano una fascia scura propria dopo l'assistenza, così il caso "fuori orario" resta entro uno scorrimento.
- **Assistenza**: il titolo è "Cosa succede dopo la chiamata" (prima "La marcia in più di Belletti", uno slogan), con le stesse parole del link della prima schermata; il link porta al titolo e sul telefono i tre casi stanno interi nello schermo (313-796 px su 844). I numeri dei casi sono a 48 px, il cambio di scala che mancava. Il caso 03 è detto più piano ("il tecnico interviene alla ripresa del normale orario di lavoro", da confermare). Nuova riga "Volete cambiare manutentore?". La zona dice "Per un sopralluogo fuori zona chiamate gli uffici... Per un guasto chiamate sempre lo 049 900 5131". Il tecnico sul telefono è in 4:5, con la testa (prima tagliata).
- **Testata**: il bottone verde dice "Guasti" anche sul telefono ("Guasti 049 900 5131", 48 px); il Menu sul telefono è un'icona di 48 px con l'etichetta per i lettori di schermo. A 320 px resta il solo numero.
- **Foto in serie.** Un solo trattamento in `pro_img.py`: bilanciamento del bianco a mondo grigio con una forza per foto (poca sui notturni, molta sul neon delle gallerie e sul tungsteno della scala d'epoca), poi la stessa curva per tutte (autocontrasto, saturazione 0,85, contrasto 1,04). Nelle schede la cabina tonda delle gallerie è sostituita dalla torre nell'atrio del depliant (`d-026`), la scala mobile con le stelle di Natale da una scala mobile senza addobbi (`fn000171`), la piattaforma è tagliata senza la sedia. Le schede sono più piccole (al massimo 270 px), così nessuna foto delle gallerie viene ingrandita.
- **Una persona di Belletti in più**: in "Chi siamo" l'ufficio tecnico di Mestrino con le impiegate (`d-043`, 4:3, 424 px, senza ingrandire).
- **Impianti nuovi**: titolo e testo a sinistra (fermi mentre si scorre), sei schede in tre colonne a destra. Titolo "Impianti nuovi, da 12 kg a 100 persone"; la loro frase "L'ascensore rispecchia il carattere dell'edificio" apre il paragrafo. Sul telefono una scheda per riga con la miniatura 4:3 di 120 px, il nome a 20 px e la descrizione visibile (prima due colonne da 167 px senza descrizione).
- **Chi siamo**: titolo "Un'impresa di famiglia, con i suoi tecnici" (prima "Ascensoristi da quattro generazioni": "dal 1908" e "4 generazioni" tornavano tre volte); i quattro numeri sono una fascia a tutta larghezza a 96 px.
- **Lavori**: "Committente: Comune di Padova" in grassetto bianco sotto il luogo di Cavour, "Progetto:" su una riga propria per tutti e tre, "ing. A. Viel" come nei redazionali. Ca' Michiel in 4:5 (737x921 da 790x988), così il vano verticale si legge intero.
- **Modulo**: cinque campi in vista (nome, telefono, comune e indirizzo, che cosa serve, quando), le note a scomparsa; il riquadro "Foto della targa in cabina o del vano" sopra il bottone; dopo il clic il testo pronto con "Copia il testo" e il numero degli uffici, per chi usa la posta via web.
- **Piede**: la colonna si chiama "Contatti" (gli orari degli uffici non sono pubblicati); i numeri sono bersagli di 48 px.

### Uso: i compiti della SCHEDA (par. 8), prima e dopo il ritocco

- **Visitatore 1, telefono 390x844.** Senza scorrere: testata con "Guasti 049 900 5131" (48 px, tel:+390499005131, a metà pagina si vede e si tocca); "Guasto o persona bloccata in cabina? L'assistenza risponde 24 ore su 24, 365 giorni all'anno."; bottone a tutta larghezza "Assistenza 24 ore 049 900 5131" (350x56 px, a 493 px), sotto il bottone bordato degli uffici. "Qualsiasi marca" nell'H1 (289 px). Il caso fuori orario è a 1535 px (prima 1564), dentro il primo scorrimento; con il link "Dopo la chiamata" i tre casi stanno interi nello schermo. Nessun compito peggiora.
- **Visitatore 2, computer 1440x900.** Nella prima schermata: manutenzione e ammodernamento nell'H1, i due numeri. Zona per esteso nell'H1 e nelle garanzie (da 901 px), elenco delle province a 1814 px; ISO 9001 dal 1997 ora nelle garanzie, a 901 px (prima a 8318). Piattaforme e servoscala nell'H1 e nella loro sezione (2475 px). Sopralluogo in un passo: tel: uffici nella prima schermata, mailto: con oggetto e traccia, oppure il modulo, ora di cinque campi più le note facoltative, con il testo da copiare se la posta non si apre. Il link "Chiedete un sopralluogo" della prima schermata è tolto: il modulo resta a un clic da "Contatti" nel menu e dai bottoni delle sezioni.
- **Visitatore 3, progettista.** "Progettisti: i lavori con i dati tecnici" nella prima schermata porta alla sezione con un clic; la prima scheda tecnica completa (Galleria Cavour) è a 437-990 px dopo il clic. Scorrendo a mano è a 3978 px, oltre i due scorrimenti, come prima. L'email all'ufficio tecnico è scritta per intero, con cosa allegare. Certificati: niente link a copie scadute, c'è la richiesta delle copie aggiornate.
- Provato con `pro_prova.mjs`: menu aperto e chiuso al tocco; ancore sotto la testata; "Dopo la chiamata" con i tre casi nello schermo; "Chiedete un sopralluogo" e la scheda Montauto scelgono il tipo nel modulo; invio vuoto fermato con l'avviso e il fuoco sul nome; cinque campi in vista; email composta con oggetto "Richiesta: Impianto nuovo: montauto, Selvazzano Dentro" e corpo completo, letta e non inviata; testo pronto da copiare visibile dopo l'invio; nessun errore di script.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs`, più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata fissa di 89 px a 1440 e 73 a 390. "Guasti 24 ore 049 900 5131" (a 390 "Guasti 049 900 5131") di 48 px; a metà pagina si vede e si tocca a 1440 e a 390. 16 link `tel:`, solo `+390499005131` e `+390495082430`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** Il mestiere nell'H1, Mestrino e "dal 1908" nell'occhiello, il bottone dei guasti (a 390 largo quanto la colonna, 350 px; a 320, 280 px). Nessuna sovrapposizione tra il testo e la foto a 1440.
3. **Immagine vera nell'apertura: passa.** La sede Belletti di sera con il furgone bianco e verde e il logo sulla fiancata, al vivo su fondo antracite (617x812 a 1440 da 869x1086, mai ingrandita). Riserva: è del 2008 e non mostra la squadra (foto da rifare nel LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` 0 volte, Unsplash e Pexels 0; nessuna immagine da `assets/esterne/`.
5. **Foto in serie: passa** (prima non passava). Tre formati (4:5, 4:3, la striscia del telefono); nessuna didascalia su 13 foto; un solo trattamento con il bianco corretto foto per foto; nelle schede tre foto del depliant 2008 e tre delle gallerie tagliate strette, senza addobbi né arredi in primo piano. Riserva: restano tre servizi diversi (depliant, gallerie, DiBaio) e la sera dei notturni accanto al giorno di Ca' della Nave; la serie vera viene solo dalle foto nuove.
6. **Palette dal marchio: passa.** Un solo colore, il verde del logo in tre toni (#007A43 bottoni e contatti, #009A54 sui fondi scuri, #00603A al passaggio del mouse), più antracite, il grigio del logo e neutri freddi. Nessun colore fuori da `:root`. Niente beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 24, 32, 48, 72, 96) e 7 a 390 (14, 17, 20, 24, 30, 40, 48). Testo corrente 19 px a 1440 e 17 a 390. Niente sotto i 14 px. H1 72 px (390: 40).
8. **Due famiglie al massimo: passa.** Una sola, Radio Canada, pesi 400 e 700; titoli e cifre in larghezza 88 %.
9. **Servizi in schede con la foto: passa.** Sei schede in tre colonne a 1440, 1024 e 768, tutte 4:3, con foto vera, nome, una riga e "Sopralluogo e preventivo"; tutta la scheda è un link. Riserva: il lavoro di ogni giorno (manutenzione, verifiche, riparazioni) resta un elenco nella sezione assistenza, perché ha la sua sezione con i tre casi della chiamata e non ci sono foto vere di quel lavoro oltre al tecnico.
10. **Almeno tre tipi di prova: passa (3 su 4).** Quattro numeri in fascia a 96 px (4, 35, 20+, 1997); "Qualità e norme" con didascalia, e ISO 9001 anche nelle garanzie; clienti e progettisti con il nome (Committente: Comune di Padova, in grassetto; Progetto: Zambusi, Danzi, Rigo). Le recensioni mancano: non ce ne sono nelle fonti (LEGGIMI, punto 10).
11. **Lavori con un nome: non passa.** Tre lavori con luogo, cinque dati e foto larga il 51 % della pagina (Ca' Michiel ora in 4:5). L'anno c'è solo per Cavour (ottobre 2007): per Ca' Michiel e Ca' della Nave le fonti non lo danno e non è inventato (LEGGIMI, punto 14).
12. **Ritmo a blocchi: passa** (prima non passava). Blocchi pieni oltre al piede: apertura e garanzie su antracite (un blocco solo a 1440), lavori su antracite, contatti su verde; assistenza e impianti su grigio chiaro. Spazio tra le sezioni 120 px a 1440 e 72 a 390; le garanzie chiudono con 96 px a 1440 e 64 a 390 (prima 64/72 e 40/48). Margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato (bianco sul fondo scuro), raggio 4 px ovunque, 56 px (48 in testata), testo a 17 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa in parte.** Ci sono tipo di intervento (10 voci), comune e indirizzo dell'impianto, urgenza (Appena possibile, Entro un mese, Senza fretta) e, per le foto, il riquadro sopra il bottone che dice di allegarle all'email; nessun iframe. Non c'è un vero campo foto (un mailto non porta allegati: va messo quando si collega il servizio, LEGGIMI) e la zona è per province, non per comuni (le fonti non danno comuni, LEGGIMI punto 3).
15. **Piede completo: passa.** Quattro colonne, testo di almeno 14 px: ragione sociale, P.IVA e C.F., REA, indirizzo con le indicazioni, i due telefoni (bersagli di 48 px) e l'email, l'orario che c'è (assistenza 24 ore su 24), le province, le certificazioni, YouTube con il sottotitolo, Privacy e Cookie, lo sponsor.

### Caratteri e licenze

- **Radio Canada** (The Radio-Canada Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero. Servita dalla pagina (`sito/fonts/radio-canada-latin.woff2` e `-latin-ext.woff2`), licenza in `sito/fonts/OFL.txt`. Una famiglia sola, la stessa della home di prima.
- **Foto**: solo materiale di Belletti (depliant 2008, gallerie del sito, redazionale DiBaio), con i diritti da chiedere (LEGGIMI). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno. Il logo è il vettoriale vero del depliant.

### Foto in pagina

| File in `sito/img/` | Soggetto | Origine | Mostrata al massimo |
|---|---|---|---|
| `apertura-sede-*` | sede di Mestrino di sera con il furgone | depliant, `d-027` (869x1263), targa sfocata | 617x812 su 869x1086 |
| `apertura-sede-striscia-*` | lo stesso, fascia per il telefono | `d-027`, taglio 869x420 | 390-900 px su 869 |
| `assistenza-tecnico-347` | tecnico al quadro | depliant, `d-033` (347x553), 4:5 | 347 px |
| `ammodernamento-scala-470` | scala del palazzo con la cabina d'epoca | depliant, `d-036` (470x704), 4:5 | 470 px |
| `ufficio-mestrino-424` | l'ufficio tecnico con le impiegate | depliant, `d-043` (633x318), 4:3 | 424 px |
| `lavoro-cavour-*` | Galleria Cavour di sera | depliant, `d-037` (948x1263), 4:3 | 737 px su 948 |
| `lavoro-camichiel-*` | Ca' Michiel, il vano col mosaico | depliant, `d-020` (790x1263), 4:5 | 737 px su 790 |
| `lavoro-cadellanave-*` | Ca' della Nave dalla corte | `01_DiBaio_Martellago.pdf` (942x694), senza le panchine, 4:3 | 737 px su 789 |
| `impianto-*` | torre nell'atrio, torre in vetro, montacarichi, montauto, piattaforma, scala mobile | depliant `d-026`, `d-002`, `d-030`; gallerie `fn000053`, `fn000257`, `fn000171` | 270 px (390: 120) su 335-600 |

### Respinti o fatti in parte, con il motivo

- **Togliere la Pallavolo Padova dal piede** (cliente tipo 2): la SCHEDA (par. 5) chiede di tenerla, perché ne vanno fieri; resta piccola e nel LEGGIMI c'è la domanda se lo sponsor è ancora attivo.
- **Cambiare il titolo dei lavori in "Tre lavori, con i dati tecnici"** (cliente tipo 2): la SCHEDA (par. 6, punto 4) chiede che la loro frase "Pensiamo che per presentarci bastino i lavori che abbiamo eseguito" resti come titolo. Il titolo degli impianti invece è cambiato, e la loro frase apre il paragrafo.
- **Togliere "Quando" per stare nei cinque campi**: la regola 14 chiede l'urgenza; sono le note facoltative a stare a scomparsa, così in vista restano cinque campi.
- **Un solo link sotto i bottoni** (controllore): ne restano due, perché "Progettisti: i lavori" è la strada del visitatore 3 verso le schede tecniche (che a mano stanno oltre due scorrimenti).
- **Pagina più corta sul telefono** (cliente tipo 1, minore): non fatto. Le schede degli impianti leggibili e la foto dell'ufficio allungano la pagina (15581 px, prima 14175); i compiti urgenti stanno tutti nei primi due schermi.
- **Recensioni, squadra con nomi, comuni serviti, anni di due lavori, vero campo foto**: non ci sono nelle fonti o richiedono il servizio d'invio; niente inventato, tutto nel LEGGIMI.
- **Scheda fotografica per la manutenzione**: non c'è una foto vera di quel lavoro oltre al tecnico già in pagina.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-15 superate nelle misure; 11 no (l'anno di due lavori); la 14 va letta con la riserva sopra. Nessuna ancora senza destinazione; nessun errore in console.
- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 (scrollWidth uguale alla finestra).
- Collegamenti: `tel:+390499005131` (assistenza) e `tel:+390495082430` (uffici); `mailto:info@bellettiascensori.it` con oggetto e traccia per sopralluogo, ufficio tecnico, certificati e modulo; Google Maps con Via della Tecnica 29, 35035 Mestrino; YouTube @BellettiAscensori.
- Contrasti sul fondo antracite: verde del logo 4,6:1 (solo occhielli in maiuscolo), grigio chiaro 8,8:1, bianco sul verde dei bottoni 5,4:1.
- Nessun U+2014 nella pagina, negli script, nella NOTA, nel LEGGIMI, nei CREDITI e in 01-analisi.
