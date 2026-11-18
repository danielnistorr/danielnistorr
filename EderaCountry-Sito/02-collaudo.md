# Edera Country House: collaudo della versione WordPress

Collaudo del 9 novembre 2026, in locale. Niente è stato pubblicato e il server di Edera non è stato toccato.

- **Ambiente**: WordPress 7.1.4 appena installato, PHP 8.3 con `php -S` (`upload_max_filesize` e `post_max_size` a 20M), database SQLite (plugin SQLite Database Integration 3.1.3), WP-CLI 2.12. WordPress e plugin stanno fuori dal repository; il login di prova esiste solo nel database locale.
- **Elementor**: 4.4.0, la versione gratuita, scaricata dallo script da WordPress.org.
- **Confronto**: l'originale scaricato in `originale/`, servito con `python3 -m http.server`, contro WordPress. Browser Chromium (Playwright).

## Installazione

`installa-su-server.sh` è lo stesso script che userà il committente, lanciato su un WordPress vuoto con lo zip del tema come quarto argomento.

- **Primo giro**:
  - tema installato e attivato, Elementor scaricato e attivato, italiano per pannello ed editor;
  - 9 foto e il PDF nella libreria media, tre pagine create in Elementor, Home come pagina iniziale, indirizzi `/%postname%/`;
  - sito nascosto ai motori di ricerca (sottodominio di prova).
- **Secondo giro**: nessun doppione (10 allegati e 3 pagine, come prima); le pagine non toccate vengono riscritte uguali.
- **Pagina modificata**: con un titolo cambiato, il giro successivo la lascia com'è ("Pagina modificata nell'editor, lasciata com'era"). Con `EDERA_RISCRIVI=1` torna quella del tema.
- **Indirizzi**: `/`, `/privacy/` e `/cookie/` rispondono 200; un indirizzo sbagliato dà la 404 del tema.
- **Zip del tema**: 62 file, 2,5 MB nella versione 1.0; 82 file, 4,6 MB nella 1.1 con le foto della planimetria. Dentro non ci sono credenziali, indirizzi locali né dati di prova; nessun file contiene U+2014.

## Le pagine in Elementor

| Pagina | Contenitori | Titolo | Editor di testo | Immagine | Pulsante | Elenco icone | Shortcode |
|---|---|---|---|---|---|---|---|
| Home | 45 | 43 | 17 | 8 | 5 | 1 | 1 (calcolatore) |
| Informativa privacy | 1 | 13 | 14 | | | | |
| Cookie | 1 | 8 | 8 | | | | |

Niente widget HTML. L'unico Shortcode è `[edera_preventivo]`, il calcolatore. Il banner cookie non c'è, come nell'originale: il sito non usa cookie.

**Editor di Elementor**, aperto in Playwright con il login di prova:
- la Home si carica nell'editor con la grafica vera, con 45 contenitori e 75 widget, calcolatore compreso;
- nel pannello Struttura le sezioni hanno un nome (Apertura, La location, Eventi, Gallery...);
- clic sul titolo "Il luogo giusto per dare spazio alle idee.": il pannello Titolo mostra il testo; scrivendo " (prova)" nel pannello, l'anteprima si aggiorna subito (non salvato);
- clic sulla foto del giardino: il pannello Immagine mostra la foto della libreria media (`casa-1250.webp`);
- clic su "Richiedi una stima": il pannello Pulsante mostra il testo; in Avanzate le classi `pulsante pulsante-verde`;
- nessun errore di console. La schermata è in `screenshot/editor-elementor.jpg`.

## Uguale all'originale?

Schermate a pagina intera, movimenti spenti (*Personalizza > Movimenti*). La differenza conta i pixel che cambiano più del 3%. Le immagini fianco a fianco e le mappe delle differenze sono in `screenshot/confronto/`.

| Larghezza | Home: altezza orig. / WP | Home: pixel diversi | Privacy | Cookie |
|---|---|---|---|---|
| 390 | 11095 / 11095 | 100 (0,002%) | 0 | 0 |
| 768 | 11208 / 11208 | 116 (0,001%) | 0 | 0 |
| 1024 | 7592 / 7592 | 96 (0,001%) | 0 | 0 |
| 1440 | 7641 / 7641 | 158 (0,001%) | 0 | 0 |
| 1920 | 7641 / 7641 | 158 (0,001%) | 0 | 0 |

Privacy e Cookie sono identiche al pixel a tutte le larghezze, con le stesse altezze. Nella Home l'unica differenza sono i tre punti "·" della riga "Meeting · Convention · Team building · Celebrazioni" nella fascia verde, spostati di meno di un pixel. Nell'originale le voci sono quattro `<span>`; in WordPress è un Titolo con spazi unificatori, più semplice da cambiare nell'editor. A occhio non si vede.

**Errori e scorrimento orizzontale**: a 390, 768, 1024, 1440 e 1920, sia l'originale sia WordPress, con i movimenti accesi e spenti:
- nessun errore di console;
- nessuna richiesta fallita;
- nessuno scorrimento orizzontale.

**Cookie**: dopo aver visitato le tre pagine e scorso la home, il browser non ha cookie, `localStorage` né `sessionStorage` del sito.

## Il calcolatore

Le stesse azioni sull'originale e su WordPress (spazi, partecipanti, durata, data, poi "Prepara la richiesta" con il consenso). Si leggono totale, voci della stima, campo partecipanti con il suo massimo, stato della mezza giornata e testo della mail (`mailto`).

| # | Prova | Risultato (originale) | WordPress |
|---|---|---|---|
| 1 | Apertura della pagina: Rustico, partecipanti vuoti | **400 €**: Rustico 400 €, Partecipanti (esempio) 20, Giornata intera; mezza spenta | uguale |
| 2 | Rustico, 50 persone (capienza piena) | **850 €**: Rustico 850 €, Partecipanti 50 | uguale |
| 3 | Rustico, 60 persone (oltre la capienza) | **850 €**: torna a 50, anche nel campo | uguale |
| 4 | Rustico, 0 persone | **400 €**: vale come l'esempio, 20 | uguale |
| 5 | Rustico, 25,5 persone (decimali) | **482,5 €** | uguale |
| 6 | Rustico + Serra, 70 persone | **1350 €**: Rustico 850 €, Serra 500 €; massimo 120 | uguale |
| 7 | Solo Piscina, 30 persone, mezza giornata | **300 €**: Mezza giornata | uguale |
| 8 | Solo Piscina, 1 persona, giornata intera | **400 €**; mezza possibile | uguale |
| 9 | Piscina + Spazio esterno, 150 persone (capienza piena) | **1000 €**: Piscina 400 €, Spazio esterno 600 € | uguale |
| 10 | Rustico + Spazio esterno, 35 persone, 15/11/2027 (stagione) | **1137,5 €**: Rustico 750 € (625 + 125), Spazio esterno 387,5 € | uguale |
| 11 | Le stesse, 15/04/2027 (fuori stagione) | **1012,5 €**: Rustico 625 €, Spazio esterno 387,5 € | uguale |
| 12 | Serra, 21 persone, 31/03/2027 (ultimo giorno di stagione) | **380 €**: 255 + 125 | uguale |
| 13 | Tutti e quattro, 300 persone (oltre 270), mezza, 10/01/2027 | **2375 €**: Rustico 975 €, Serra 500 €, Piscina 300 €, Spazio esterno 600 €; campo a 270 | uguale |
| 14 | Piscina + Serra con la mezza, poi tolgo la piscina | **350 €**: la mezza si spegne, torna Giornata intera | uguale |
| 15 | Tolgo tutti gli spazi | **400 €**: l'ultimo (Rustico) resta scelto | uguale |

**15 prove su 15 danno gli stessi numeri e lo stesso testo della mail.** In WordPress i numeri vengono da `config/preventivo.php`, non sono più scritti nello script.

## Movimenti

Accesi (è il valore di partenza): il titolo d'apertura sale riga per riga, la foto grande della Gallery si scopre con un taglio, la testata si nasconde scendendo (da 900 px).

- **A movimento finito la pagina è quella dell'originale**:
  - prima schermata dopo 3 secondi: 8 pixel diversi a 390, 136 a 1440 (bordi delle lettere del titolo);
  - Gallery dopo il taglio: 0 pixel diversi a 390 e a 1440.
- **Testata**: a 1440 scendendo prende la classe `nascosta`; salendo torna, con il fondo chiaro. A 390 resta `position: absolute`, come nell'originale.
- **Riduci movimento**: niente movimenti; schermate a pagina intera uguali a quelle a movimenti spenti (da 96 a 158 pixel, i soliti tre punti).
- **Senza JavaScript**: prima schermata identica all'originale a 390 e 1440 (0 pixel).
- **Interruttore**: con *Movimenti* spento il tema non carica né il kit né GSAP.
- **Film dello scorrimento** (`_metodo/highend/kit/registra.mjs`), nessun errore di script:
  - WordPress: `screenshot/wp/foglio-1440.jpg` e `foglio-390.jpg`;
  - originale: `screenshot/originale/foglio-1440.jpg` e `foglio-390.jpg`.
  I video (`scorrimento-*.mp4`) e i fotogrammi singoli restano sul disco, fuori da git (`screenshot/.gitignore`), come per le home HE.

## Peso al primo caricamento

Senza compressione, come lo dà `php -S`:

| | Telefono (390) | Computer (1440) |
|---|---|---|
| Originale | 8 richieste, 419 KB | 11 richieste, 805 KB |
| WordPress | 35 richieste, 1001 KB (444 KB di script) | 38 richieste, 1386 KB (444 KB di script) |

Gli script in più sono di Elementor (con jQuery) e del kit dei movimenti.

## Cosa non si è potuto provare qui

- **Elementor Pro**: è a pagamento. Il tema usa solo widget della versione gratuita e nessuna funzione che Pro cambi; i fogli di stile di Pro non toccano i widget usati.
- **Server vero**: MySQL, Apache con `.htaccess` (riscrittura degli indirizzi e rinvii dei vecchi indirizzi), installazione di WordPress da cartella vuota (il ramo dello script che chiede i dati del database).

## Tema 1.1: la planimetria (10 novembre 2026)

La sezione è tutta in widget di Elementor gratuito (4.4.0): contenitore della mappa con la foto dall'alto (Immagine), 6 pallini (Pulsante in posizione assoluta, offset in %), legenda (Elenco icone), titolo "Rustico", 5 foto (Galleria di base con il lightbox di Elementor), Pulsante "Scegli nel preventivo". Niente shortcode e niente widget HTML. Il pallino del Rustico apre il lightbox della galleria con un link d'azione di Elementor (`#elementor-action:action=lightbox`, che legge le foto dalla galleria della pagina).

**Installazione da zero** con `installa-su-server.sh` e il tema 1.1:
- 16 allegati (15 foto e il PDF) e 3 pagine, planimetria nella Home dopo la sezione 01, numeri 01-07;
- rilanciato: nessun doppione, "La planimetria è già nella Home".

**Aggiornamento da 1.0 a 1.1**, come lo farà il committente, nel browser:
- partenza: WordPress con il tema 1.0 installato e un titolo della Home cambiato a mano ("Domande frequenti, e risposte.");
- *Carica tema*, poi "Sostituisci quello attuale con quello caricato": tema aggiornato;
- *Aggiungi la planimetria alla Home*: 6 foto caricate, numeri portati da 02-06 a 03-07, sezione inserita dopo la 01, il titolo cambiato a mano è rimasto;
- secondo clic: "già nella Home", niente cambia.

**Editor di Elementor** (login di prova, niente salvato):
- la sezione si apre con 6 pallini e 5 foto;
- un pallino trascinato di 48 x 28 px cambia offset da 33 / 53,14% a 41,69 / 58,21%, e sulla pagina si sposta di quanto è stato trascinato;
- il testo di un pallino si cambia dal pannello e l'anteprima segue;
- nessun errore.

L'offset verticale in % Elementor lo calcola sulla larghezza del contenitore. Per questo i pallini stanno in un contenitore quadrato largo quanto la foto, con la y convertita (y x 1604 / 981). Senza questo accorgimento un pallino trascinato saltava di 230 px.

**Pagina**, a 390, 600, 601, 768, 900, 901, 1024, 1280, 1299, 1300, 1366, 1440 e 1920 px:
- pallini ed etichette sempre dentro la foto e mai accavallati;
- sul telefono e fra 901 e 1299 px restano i numeri, con i nomi nella legenda;
- nessun errore di console, nessuno scorrimento orizzontale.

**Lightbox** dal pallino del Rustico, a tutte le larghezze:
- si apre su "1 / 5" con la foto da 1600 px; la freccia porta a "2 / 5"; Esc chiude;
- mentre è aperto la pagina sotto resta ferma (regola del tema); alla chiusura il focus torna al pallino.

Lo scorrimento col dito è quello di Elementor (Swiper): con i tocchi simulati del browser di prova la foto non è cambiata, quindi non è verificato qui. Va provato su un telefono vero.

**Fuori dalla sezione nuova la pagina non cambia.** Schermate a pagina intera dell'originale e di WordPress, togliendo la sezione nuova. La sezione è fissata a un'altezza intera, perché quello che segue stia alla stessa frazione di pixel. Restano solo i tre "·" della fascia e, da 1400 px, i numeri delle sezioni rinumerate:

| Larghezza | Altezza orig. / WP senza la sezione | Pixel diversi | Sezione nuova |
|---|---|---|---|
| 390 | 11095 / 11095 | 102 | 1541 px |
| 768 | 11208 / 11208 | 116 | 1976 px |
| 1024 | 7592 / 7592 | 96 | 978 px |
| 1440 | 7641 / 7641 | 391 (numeri 03-07) | 1233 px |
| 1920 | 7641 / 7641 | 391 (numeri 03-07) | 1230 px |

Senza fissare l'altezza, tutto quello che viene dopo si sposta di meno di mezzo pixel e il confronto pixel per pixel conta differenze di sfumatura, invisibili.

**Peso aggiunto al primo caricamento** (tema 1.1 contro 1.0, stessa Home):

| | Senza compressione | Con gzip (come su Plesk) |
|---|---|---|
| 390 | 449 KB | 183 KB |
| 1440 | 520 KB | 255 KB |

- Foto: la mappa (70 KB a 390, 141 KB a 1440) e 5 miniature da 3-5 KB.
- Le foto grandi si caricano solo nel lightbox.
- Il resto sono gli script e gli stili del lightbox di Elementor (Swiper 140 KB, lightbox 76 KB, finestra e stili 60 KB). Elementor li carica appena nella pagina c'è un link a una foto con il lightbox.

**Schermate**: `screenshot/planimetria/`
- Home a pagina intera a 390, 768, 1440 e 1920; la barra fissa del telefono è nascosta, perché a pagina intera finirebbe a metà;
- la sezione da sola;
- il lightbox aperto a 1440 e a 390.

**Film**: `screenshot/wp/foglio-1440.jpg` e `foglio-390.jpg`, rifatti con la planimetria, nessun errore di script.

## Tema 1.1.1: foto su qualunque pallino (10 novembre 2026)

La regola sta in poche righe di `assets/sito.js`: un clic su un link `#foto-<nome>` apre il lightbox di Elementor sulla galleria con ID CSS `foto-<nome>`. Il tema simula un clic sul primo link della galleria, così si apre lo slideshow nativo con tutte le sue foto.

Prove con Elementor gratuito 4.4.0:
- **Partenza**: Home aggiornata da 1.0 a 1.1 con il bottone, con il titolo delle domande cambiato a mano.
- **Il vecchio link resta valido**: dopo il passaggio a 1.1.1 il Rustico (`#elementor-action...`) apre ancora "1 / 5"; la freccia porta a "2 / 5", Esc chiude.
- "Aggiungi la planimetria alla Home": "già nella Home", nessun cambiamento.
- **"Semplifica il link del Rustico"**: il link diventa `#foto-rustico` e la galleria prende l'ID CSS `foto-rustico`. Il secondo clic non fa niente ("già semplificato"). Il titolo cambiato a mano è rimasto. Il Rustico apre "1 / 5" a 1440 e a 390.
- **Serra** (con uno script che fa le stesse modifiche dell'editor): titolo e Galleria di base con 3 foto e ID CSS `foto-serra`, pallino con link `#foto-serra` e classi `pallino pallino-attivo`.
  - Galleria visibile: il pallino apre "1 / 3" con le sue foto, a 1440 e a 390; la freccia porta a "2 / 3", Esc chiude, la pagina non salta alla galleria.
  - Galleria nascosta su desktop, tablet e mobile: stesso risultato a 1440, 768 e 390.
- **Galleria che non c'è**: un pallino con `#foto-grill` non fa niente, senza errori.
- **Errori**: nessun errore di console in tutte le prove.
- **Editor**: i pallini con link si scelgono, si trascinano (circa 45 x 20 px, come il mouse) e cambiano testo dal pannello. Un clic su un pallino con link può far scorrere l'anteprima fino alla galleria: lo fa Elementor con i link interni (scritto nel LEGGIMI).


## Plugin "Edera Preventivo" 1.0 e tema 1.2 (12 novembre 2026)

Prove in locale con WordPress 7.1.4, Elementor 4.4.0 gratuito, PHP 8.3 e SQLite. Il sito di partenza è come quello vero: tema 1.1.1 installato con lo script, planimetria nella Home, e la Home modificata a mano (due testi cambiati) prima di tutto il resto.

**Le pagine non si toccano.** Prima dell'installazione ho preso le impronte (sha256) di `_elementor_data` e del contenuto di tutte le pagine, più una copia di `_elementor_data` della Home (37.549 byte). Le ho confrontate:
- dopo il caricamento e l'attivazione del plugin dal pannello (*Plugin > Carica plugin*);
- dopo l'aggiornamento del tema a 1.2 con "Sostituisci quello attuale";
- dopo plugin spento e riacceso;
- alla fine di tutte le prove (salvataggi, importazioni, ripristino, recapiti in Personalizza).

Ogni volta **identico byte per byte** (`cmp` e stesse impronte). Il plugin scrive solo la sua opzione, `edera_preventivo_regole`.

**Le 15 prove di sempre.** Originale contro WordPress, con lo stesso script del collaudo del calcolatore, 15 su 15 identiche (totale, voci, partecipanti, durata e testo della mail) in cinque situazioni:
- plugin attivo con il tema 1.1.1;
- plugin attivo con il tema 1.2;
- plugin spento (calcolatore del tema 1.2);
- dopo "Ripristina i valori iniziali";
- dopo "Salva le regole" senza cambiare niente.

All'attivazione il plugin ha preso i prezzi da `config/preventivo.php` del tema. Con il plugin attivo parte solo il suo script (`calcolo.js` e `preventivo.js` del plugin), anche con il tema 1.1.1. Con il plugin spento torna lo script del tema.

| # | Prova (valori iniziali del plugin) | Totale e voci, originale e plugin | Uguale |
|---|---|---|---|
| 1 | Apertura della pagina: Rustico, partecipanti vuoti (esempio 20) | **400 €**: Rustico 400 €, Partecipanti (esempio) 20, Durata Giornata intera | sì |
| 2 | Rustico, 50 persone (capienza piena) | **850 €**: Rustico 850 €, Partecipanti 50, Durata Giornata intera | sì |
| 3 | Rustico, 60 persone (oltre la capienza: torna a 50) | **850 €**: Rustico 850 €, Partecipanti 50, Durata Giornata intera | sì |
| 4 | Rustico, 0 persone (vale come esempio 20) | **400 €**: Rustico 400 €, Partecipanti 20, Durata Giornata intera | sì |
| 5 | Rustico, 25,5 persone (decimali) | **482,5 €**: Rustico 482,5 €, Partecipanti 25.5, Durata Giornata intera | sì |
| 6 | Rustico + Serra, 70 persone | **1350 €**: Rustico 850 €, Serra 500 €, Partecipanti 70, Durata Giornata intera | sì |
| 7 | Solo Piscina, 30 persone, mezza giornata | **300 €**: Piscina 300 €, Partecipanti 30, Durata Mezza giornata | sì |
| 8 | Solo Piscina, 1 persona, giornata intera | **400 €**: Piscina 400 €, Partecipanti 1, Durata Giornata intera | sì |
| 9 | Piscina + Spazio esterno, 150 persone (capienza piena) | **1000 €**: Piscina 400 €, Spazio esterno 600 €, Partecipanti 150, Durata Giornata intera | sì |
| 10 | Rustico + Spazio esterno, 35 persone, 15/11/2027 (stagione) | **1137,5 €**: Rustico 750 €, Spazio esterno 387,5 €, Partecipanti 35, Durata Giornata intera | sì |
| 11 | Rustico + Spazio esterno, 35 persone, 15/04/2027 (fuori stagione) | **1012,5 €**: Rustico 625 €, Spazio esterno 387,5 €, Partecipanti 35, Durata Giornata intera | sì |
| 12 | Serra, 21 persone, 31/03/2027 (ultimo giorno di stagione) | **380 €**: Serra 380 €, Partecipanti 21, Durata Giornata intera | sì |
| 13 | Tutti e quattro, 300 persone (oltre 270), mezza, 10/01/2027 | **2375 €**: Rustico 975 €, Serra 500 €, Piscina 300 €, Spazio esterno 600 €, Partecipanti 270, Durata Mezza giornata | sì |
| 14 | Piscina + mezza, poi tolgo la piscina (la mezza si spegne) | **350 €**: Serra 350 €, Partecipanti 40, Durata Giornata intera | sì |
| 15 | Tolgo tutti gli spazi (l'ultimo resta scelto) | **400 €**: Rustico 400 €, Partecipanti 10, Durata Giornata intera | sì |

**Regole nuove.** Dal modulo del pannello:
- una data esclusa (8 dicembre) e un supplemento del weekend del 10% sul totale, salvati;
- una percentuale di 150 rifiutata con il messaggio "Le percentuali vanno da 0 a 100", con il modulo che conserva quanto scritto.

Importati da file:
- chiusura dal 24 dicembre al 6 gennaio, lunedì chiuso, preavviso di 7 giorni, finestra di 12 mesi;
- sconto del 10% da due spazi, minimo di 30 partecipanti, arrotondamento per eccesso a 50 euro;
- servizi "Aperitivo di benvenuto" (8 € a persona) e "Grill" (80 €).

Esportato e reimportato: le regole restano uguali. Poi, sul sito ricaricato:

| Prova (regole nuove, importate dal pannello) | Atteso | Sul sito |
|---|---|---|
| Weekend +10% sul totale, stagionale, arrotondamento a 50: Rustico, 30 persone, sabato 28/11/2026: Rustico 675 €, Weekend 67,5 €, Arrotondamento 7,5 €; Partecipanti 30, Durata Giornata intera | 750 € | 750 € |
| Sconto 10% su due spazi, weekend, arrotondamento: Rustico + Serra, 70 persone, sabato 17/04/2027: Rustico 850 €, Serra 500 €, Weekend 135 €, Sconto per più spazi -148,5 €, Arrotondamento 13,5 €; Partecipanti 70, Durata Giornata intera | 1350 € | 1350 € |
| Minimo 30 partecipanti: Serra, 10 persone (diventano 30): Serra 300 €; Partecipanti 30, Durata Giornata intera | 300 € | 300 € |
| Servizio a persona (aperitivo 8 €) e arrotondamento: Rustico, 40 persone, mercoledì 05/05/2027: Rustico 700 €, Aperitivo di benvenuto 320 €, Arrotondamento 30 €; Partecipanti 40, Durata Giornata intera | 1050 € | 1050 € |
| Servizio fisso (grill 80 €) e minimo 30: Rustico, 20 persone (diventano 30), nessuna data: Rustico 550 €, Grill 80 €, Arrotondamento 20 €; Partecipanti 30, Durata Giornata intera | 650 € | 650 € |

Calendario (oggi è il 12 novembre 2026):

| Data nel calendario | Si può scegliere? |
|---|---|
| oggi 12/11 (prima del preavviso di 7 giorni) | no |
| domenica 15/11 (preavviso) | no |
| giovedì 19/11 (primo giorno utile) | sì |
| lunedì 23/11 (giorno chiuso) | no |
| martedì 08/12 (data esclusa) | no |
| domenica 27/12 (chiusura natalizia) | no |
| giovedì 07/01/2027 (dopo la chiusura) | sì |
| mercoledì 01/12/2027 (oltre 12 mesi) | no |

- Un clic sull'8 dicembre (barrato) non sceglie niente.
- Il 10 dicembre si sceglie e nella mail finisce come "10 dicembre 2026", con la riga "Servizi aggiuntivi: Aperitivo di benvenuto".
- Il campo si chiama "Data dell'evento"; senza regole sul calendario resta "Data indicativa", come oggi.
- **Prova** del pannello: per Rustico, 30 persone, sabato 28 novembre dà 742,5 €, gli stessi conti del sito prima dell'arrotondamento.
- **Recapiti** (tema 1.2): un telefono scritto in *Personalizza > Recapiti* compare nel piede; svuotato il campo, torna quello del file. La sezione si apre senza errori.
- **Errori e scorrimento**: nessun errore di console e nessuno scorrimento orizzontale a 1440 e a 390, sul sito (anche con il calendario aperto, che a 390 sta fra 47 e 362 px) e nel pannello.
- **Schermate**: `screenshot/preventivo/`, pannello a 1440 e a 390, prova, calcolatore e calendario a 1440 e a 390.

## Plugin "Edera Preventivo" 1.0.1: capienza superabile e fasce per numero di persone (12 novembre 2026)

In locale, con WordPress 7.1.4, Elementor 4.4.0 e il tema 1.2. Il punto di partenza è come il sito vero: plugin 1.0.0 attivo, regole già cambiate dal pannello (giorni esclusi, weekend, sconti, servizi), Home modificata a mano prima dell'installazione.

### Aggiornamento dalla 1.0.0

*Plugin > Aggiungi nuovo > Carica plugin*, `edera-preventivo.zip`, *Installa ora*. WordPress mostra il confronto (attuale 1.0.0, caricato 1.0.1) e il bottone *"Sostituisci quello attuale con quello caricato"*. Dopo l'aggiornamento il plugin resta attivo.

- **Regole salvate**: identiche. L'impronta sha256 dell'opzione `edera_preventivo_regole` è la stessa prima e dopo (72b31176...), anche dopo aver aperto il sito.
- Con quelle regole il sito dà gli stessi risultati della 1.0.0: 750, 1350, 300, 1050 e 650 €, e le stesse 8 risposte del calendario.
- **Home**: il contenuto di `_elementor_data` è identico byte per byte prima e dopo l'aggiornamento (37.549 byte, sha256 7f0436e867b6...). È anche identico alla Home modificata a mano all'inizio delle prove.
- **Altre pagine**: impronte di dati Elementor e contenuto di tutte le pagine uguali prima, dopo e a fine prove.

### Le 15 prove di sempre

Con i valori iniziali ("Limite rigido", nessuna fascia): **15 su 15** uguali all'originale (totale, voci, partecipanti, durata, testo della mail). La tabella è identica a quella della 1.0.0.

Lo stesso risultato, 15 su 15, anche dopo *Salva le regole* senza cambiare niente.

### Oltre la capienza

| Impostazione | Prova | Stima | Note nella stima e nella mail |
|---|---|---|---|
| con la stima | Rustico, 52 persone (capienza 50) | 880 € (400 + 32 × 15) | "52 persone, oltre la capienza indicata di 50: da valutare con la struttura." |
| con la stima | Piscina, 40 persone (capienza 30, prezzo fisso) | 400 € | la riga oltre capienza e "Piscina a prezzo fisso: l'importo indicato non tiene conto delle persone in più." |
| con la stima | Rustico + Serra, 130 persone (capienza 120) | 1550 € (Rustico 1000, Serra 550) | "130 persone, oltre la capienza indicata di 120..." |
| con la stima | Rustico, 50 persone (non supera) | 850 € | nessuna |
| senza importo | Rustico 52, Piscina 40, Rustico + Serra 130 | "Da valutare con la struttura" | la riga oltre capienza; nella mail "Stima location: Da valutare con la struttura" |
| senza importo | Rustico + Serra, 120 persone (non supera) | 1350 € | nessuna |
| con la stima, massimo assoluto 150 | Rustico, 151 persone | il campo torna a 150; 2350 € | sotto il campo il messaggio "oltre capienza" con 150 |

- Quando si può superare, sotto il campo compare "Capienza indicativa con gli spazi scelti: 50 persone. Per gruppi più numerosi la richiesta viene valutata." e la richiesta parte con il numero scritto.
- Nella mail la riga oltre capienza va sotto "Partecipanti", in tutte e due le modalità.

### Fasce per numero di persone

Fasce di prova:
- **Rustico**: 1-30 fisso 400 €, 31-50 a persona 15 €.
- **Serra**: 20-40 fisso 350 €, 41-70 a persona 6 €.
- **Piscina**: 1-15 fisso 300 € (mezza 200 €), 16-30 a persona 20 € (mezza 14 €).
- **Spazio esterno**: 1-60 fisso 500 €, da 61 senza limite a persona 4 €.
- In più un supplemento weekend del 10% sul totale e lo sconto del 10% su due spazi.

| Prova | Atteso | Sul sito | Riga dello spazio |
|---|---|---|---|
| Rustico, 30 persone (bordo) | 400 € | 400 € | Rustico (1-30 persone, prezzo fisso) |
| Rustico, 31 persone (bordo) | 465 € | 465 € | Rustico (31-50 persone, 15 € a persona) |
| Serra, 10 persone (fuori dalle fasce) | 250 € (prezzo standard) | 250 € | Serra; nota "Serra: per 10 persone non c'è una fascia di prezzo, la stima usa il prezzo standard dello spazio." |
| Rustico + Serra, 45 persone, sabato 17/04/2027 | 945 + weekend 94,5 - sconto 103,95 = 935,55 € | 935,55 € | Rustico (31-50 persone, 15 € a persona) 675 €; Serra (41-70 persone, 6 € a persona) 270 € |
| Rustico, 31 persone, sabato 13/11/2027 (stagionale + weekend) | 465 + 125 + 59 = 649 € | 649 € | Rustico (31-50 persone, 15 € a persona) |
| Piscina, 20 persone, mezza giornata | 280 € | 280 € | Piscina (16-30 persone, 14 € a persona) |
| Piscina, 10 persone, mezza giornata | 200 € | 200 € | Piscina (1-15 persone, prezzo fisso) |
| Piscina, 20 persone, giornata intera | 400 € | 400 € | Piscina (16-30 persone, 20 € a persona) |
| Con la stima: Rustico, 52 persone (nessuna fascia oltre 50) | da valutare | "Da valutare con la struttura" | nota oltre capienza |
| Con la stima: Spazio esterno, 130 persone (fascia "da 61") | 520 € | 520 € | Spazio esterno (da 61 persone, 4 € a persona) |
| Con la stima: Rustico + Spazio esterno, 180 persone | da valutare | "Da valutare con la struttura" | nota oltre capienza |
| Con la stima: Rustico, 45 persone (non supera) | 675 € | 675 € | Rustico (31-50 persone, 15 € a persona) |

- Nella mail la riga "Spazi:" scrive la fascia applicata, per esempio "Spazi: Rustico (31-50 persone, 15 € a persona), Serra (41-70 persone, 6 € a persona)". La nota fuori fascia va sotto "Partecipanti".

### Pannello

- Dal modulo:
  - "Si può superare, con la stima" e massimo assoluto 150;
  - due fasce per il Rustico, scritte in disordine, che al salvataggio si mettono in ordine;
  - due fasce per la Piscina, con l'importo della mezza giornata.
  Tutto salvato com'era scritto.
- **Errore**: una fascia 25-60 sopra le fasce 1-30 e 31-50.
  - In cima compare: *Le fasce dello spazio "Rustico" si sovrappongono: 1-30 e 25-60 persone. Ogni numero di persone deve stare in una fascia sola.*
  - Le regole salvate restano identiche (stessa impronta) e la bozza tiene le 3 fasce.
  - Tolta la fascia sbagliata, il salvataggio riesce.
- **Altri errori** controllati sulla funzione di controllo, tutti senza salvataggio:
  - "da" maggiore di "a";
  - importo o importo della mezza giornata negativo;
  - importo o "da" mancante;
  - fascia senza limite seguita da un'altra;
  - massimo assoluto negativo;
  - minimo di partecipanti sopra il massimo assoluto.
  Un file JSON esportato con la 1.0.0 si importa senza errori e resta in "Limite rigido".
- **Prova del pannello**:
  - Rustico 30: 400 €. Rustico 31: 465 €, con le etichette delle fasce.
  - Rustico 52: "Da valutare con la struttura", con la nota.
  - Piscina 40: 800 € (fascia "da 16"), con la nota.
  - Piscina 10, mezza giornata: 200 €.
  - Rustico 151: contate 150 persone.
- **Errori e scorrimento**: 22 casi sul sito, a 1440 e a 390, senza errori di console né scorrimento orizzontale. Lo stesso nel pannello, a 1440 e a 390.
- **Schermate** in `screenshot/preventivo/`:
  - `oltre-stima-1440.jpg`, `oltre-stima-390.jpg`, `oltre-senza-390.jpg`;
  - `fasce-1440.jpg`, `fasce-390.jpg`;
  - `pannello-fasce-1440.jpg`, `pannello-fasce-390.jpg`, `pannello-oltre-390.jpg`;
  - `pannello-errore-fasce-1440.jpg`, `pannello-prova-fasce.jpg`.
