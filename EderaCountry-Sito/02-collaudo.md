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
- **Zip del tema**: 62 file, 2,5 MB. Dentro non ci sono credenziali, indirizzi locali né dati di prova; nessun file contiene U+2014.

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
