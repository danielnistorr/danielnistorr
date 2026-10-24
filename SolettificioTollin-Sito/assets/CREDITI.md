# Crediti immagini: Solettificio Tollin

## `originali/`: materiale del sito dell'azienda

Scaricato il 24/10/2026 da https://www.tollin.it (cartella `immagini/` del sito). Misure, soggetto e voti in `_prova/inventario-immagini.json`. Diritti dell'azienda: si usano solo nella proposta per Tollin.

- `originali/logo-tollin-piedi-en.png`, `logo-tollin-dal1970.png`: ritagliati da `immagini/zona_logo.jpg` (900x117, JPEG). `logo-tollin-piedi-it.png`: ritagliato da `immagini/logo2pag.jpg`. Nessun vettoriale trovato sul sito; la favicon (16x16) non è il logo.

## `esterne/`: segnaposto di repertorio

Nessuna è di Tollin, del suo reparto o dei suoi sottopiedi: servono solo a mostrare la direzione visiva nella proposta, e il LEGGIMI dovrà dirlo. Nessuna è generata dall'IA. Licenza letta sulla pagina di ogni foto il 24/10/2026 (Unsplash: "Free to use under the Unsplash License", nessuna Unsplash+; Pexels: "Free", licenza Pexels). Controllato che nessuna sia già in un altro `*-Sito/assets/CREDITI.md` della campagna. Scaricate con curl dalle CDN (`images.pexels.com`, `images.unsplash.com`) a 2400 px di lato lungo al massimo.

| File | Pagina della foto | Autore | Licenza | Misura salvata (originale) | Uso previsto |
|---|---|---|---|---|---|
| `esterne/pexels-36589768-ivantsov-decollete-su-blocco.jpg` | https://www.pexels.com/photo/elegant-brown-leather-heels-on-display-36589768/ | Valentin Ivantsov (pexels.com/@valentin-ivantsov-2154772556) | Pexels License | 1600x2400 (3417x5125) | direzione A, apertura: décolleté color cuoio su un cubo di legno, fondo bianco; il sottopiede in pelle forato si vede bene, nessun marchio |
| `esterne/pexels-36581188-ivantsov-sandali-tacco-bianco.jpg` | https://www.pexels.com/photo/elegant-brown-leather-strap-heeled-sandals-36581188/ | Valentin Ivantsov | Pexels License | 2400x1600 (5760x3840) | stesso paio, orizzontale: taglio per il telefono o per la chiusura |
| `esterne/pexels-26965818-segura-sandali-dall-alto.jpg` | https://www.pexels.com/photo/studio-shot-of-three-leather-sandals-in-various-colors-26965818/ | José Martin Segura Benites (pexels.com/@jose-martin-segura-benites-1422456152) | Pexels License | 2000x2000 (2000x2000) | tre sandali dall'alto su bianco, sottopiedi in vista ("sottopiede per sandalo"). Sul sottopiede nero c'è un piccolo marchio impresso ("Gimo"): da togliere col ritocco se la foto va in pagina |
| `esterne/unsplash-GPdWubhjq-Q-berg-sagoma-sottopiede.jpg` | https://unsplash.com/photos/person-tracing-leather-pattern-with-pen-GPdWubhjq-Q | Cohen Berg (@cohenberg) | Unsplash License | 2400x1600 | mani che tracciano una sagoma di sottopiede forata su pelle: la modelleria. È un'altra foto della stessa serie usata da Hambro (`an44PeEll_w`), non la stessa |
| `esterne/unsplash-dtx5yLi-vZU-karathanasis-forme.jpg` | https://unsplash.com/photos/shoe-lasts-and-other-items-in-a-heap-dtx5yLi-vZU | Vagelis Karathanasis (@urbantosea) | Unsplash License | 1596x2400 | mucchio di forme da calzatura in bianco e nero: la forma da cui parte il disegno del sottopiede |
| `esterne/unsplash-iWpdAFdKV0-evomao-forme-in-fusti.jpg` | https://unsplash.com/photos/stacked-rusty-metal-barrels-with-blue-objects-inside--iWpdAFdKV0 | EvoMao (@evomao) | Unsplash License | 2400x1600 | forme in plastica dentro fusti metallici (didascalia dell'autore: "corner of wasted shoe lasts", Dongguan): solo di riserva, tono scuro |
| `esterne/pexels-39332406-ivantsov-rotoli-feltro.jpg` | https://www.pexels.com/photo/colorful-rolled-felt-fabrics-in-close-up-view-39332406/ | Valentin Ivantsov | Pexels License | 2400x1600 (5760x3840) | rotoli di feltro colorato: i materiali (lana, tessuti) |
| `esterne/pexels-18358663-ganaj-sughero.jpg` | https://www.pexels.com/photo/close-up-of-a-cork-board-18358663/ | Petr Ganaj (pexels.com/@ganajp) | Pexels License | 2400x1600 (8256x5504) | grana di sughero agglomerato: materiale, fondo per una fascia |
| `esterne/pexels-35240765-idrissi-forma-riflesso.jpg` | https://www.pexels.com/photo/elegant-wooden-shoe-trees-with-reflection-35240765/ | Moussa Idrissi (pexels.com/@mographe) | Pexels License | 2400x1600 (3543x2362) | tendiscarpe in legno con riflesso, scuro: riserva |

Scartate dopo il controllo: Jez Timms `mLr4_8ioypQ` e Raoul Ortega `2JtF6pYAOOI` (già nella home del Tacchificio Riviera), Simões 13524778 (già usata), Hush Puppies 28157683, Billionaire 38786817, Corio 31935097 e 31935098, Vivaia 32496673 (marchi leggibili in primo piano).

## Uso nella home finale (`sito/`, aggiornato il 24/10/2026 nella rifinitura)

- Solo foto di Tollin da `originali/immagini/`: `modelleria2` (apertura, il foglio scontornato), `modelleria1`, `lavorazione2`, `cambratura3`, `supervisione2` (le quattro schede dei reparti), `supervisione1` (la scatola), `supervisione3` (il furgone della chiusura). Trattamento in `_prova/script/finale_img.py`.
- Nessuna foto di `esterne/` è più nella home: il segnaposto Pexels `pexels-36581188` (Ivantsov) dell'apertura è stato tolto. `pexels-36589768` e `unsplash-GPdWubhjq-Q` restano solo nei prototipi.
