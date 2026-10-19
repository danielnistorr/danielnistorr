# Crediti delle immagini

Aggiornato il 19 ottobre 2026 (home finale). Licenza letta sulla pagina di ogni foto il 19 ottobre 2026: tutte riportano "Free to use under the Unsplash License" (nessuna è Unsplash+).

## Foto di repertorio in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere di Mario Agnoletto]

Nessuna è di Mario Agnoletto, della sua officina o dei suoi pezzi: servono solo a far vedere la direzione artistica nella proposta, e il LEGGIMI lo dirà. Nessuna immagine generata dall'IA.

Licenza Unsplash (https://unsplash.com/license): uso libero anche commerciale, senza obbligo di attribuzione, modifiche ammesse; non si possono vendere le foto non modificate né ricostruire con esse un servizio concorrente di Unsplash. Versioni scaricate a 2400 px di lato corto o lungo dal CDN `images.unsplash.com`.

| File | Pagina della foto | Autore | Scaricata | Direzione | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-FXVC26csSz4.jpg` | https://unsplash.com/photos/FXVC26csSz4 | Ruan Richard Rodrigues | 2400x3600 | A, apertura | ESCLUSE: la stessa serie è nella home di Hambro, stesso paese e stesso mestiere. Non usare in nessuna pagina di Mario Agnoletto |
| `esterne/unsplash-hqGQcZnEvy0.jpg` | https://unsplash.com/photos/hqGQcZnEvy0 | Ruan Richard Rodrigues | 2400x3600 | A | ESCLUSE: la stessa serie è nella home di Hambro, stesso paese e stesso mestiere. Non usare in nessuna pagina di Mario Agnoletto |
| `esterne/unsplash-aNe3TXdpHMg.jpg` | https://unsplash.com/photos/aNe3TXdpHMg | Ruan Richard Rodrigues | 2400x3600 | A | ESCLUSE: la stessa serie è nella home di Hambro, stesso paese e stesso mestiere. Non usare in nessuna pagina di Mario Agnoletto |
| `esterne/unsplash-4kqacvbRq34.jpg` | https://unsplash.com/photos/4kqacvbRq34 | McFollis | 2400x3133 | A | décolleté dorata riflessa su fondo scuro: il tacco gioiello nel prodotto finito |
| `esterne/unsplash-Y5RNGe_xkAQ.jpg` | https://unsplash.com/photos/Y5RNGe_xkAQ | Ayush Design | 2400x2400 | A e B | grana di pelle nera, fondo neutro per i pezzi |
| `esterne/unsplash-_ifvZpJieZ4.jpg` | https://unsplash.com/photos/_ifvZpJieZ4 | Jos Zwaan | 2400x1597 | B, apertura | punzoni in acciaio con disegno inciso su banco di legno |
| `esterne/unsplash-GwtQGmTOCIE.jpg` | https://unsplash.com/photos/GwtQGmTOCIE | Hasan Mrad | 2400x1600 | B | mani che incidono a bulino un pezzo di metallo (bottega, non officina meccanica) |
| `esterne/unsplash-pl95tzT0f7Y.jpg` | https://unsplash.com/photos/pl95tzT0f7Y | mastars MT | 2400x1600 | B | fresa su pezzo in rame, sfondo sfocato caldo |
| `esterne/unsplash-8MBTn3Z71zI.jpg` | https://unsplash.com/photos/8MBTn3Z71zI | Jelifer Maniago | 2400x1478 | B | mandrino che lavora un pezzo in alluminio, refrigerante in controluce |
| `esterne/unsplash-ALvgGEl8mEE.jpg` | https://unsplash.com/photos/ALvgGEl8mEE | Ivan Di | 2400x1800 | B | mucchio di minuterie zigrinate in ottone: la "serie" |

## Immagini del sito attuale in `originali/`

Scaricate il 19 ottobre 2026 da `https://www.marioagnoletto.it/img/` (logo, sfondi, 18 foto prodotto, foto della sede). Inventario, misure e voti in `_prova/inventario-immagini.json`. Sono di Mario Agnoletto (le foto prodotto sembrano scattate in azienda con uno smartphone); lo sfondo con i brillantini (`background_background.jpg`) è un'immagine di repertorio di origine sconosciuta e non va riusata. La foto `photos_large_6.jpg` mostra il marchio di una maison su un cliché: non pubblicarla senza permesso.

## Usate nella home finale (`sito/img/`), versione B "Tavola dei campioni"

Aggiornato il 19 ottobre 2026, ultimo giro. Le foto della serie di Ruan Richard Rodrigues (aNe3TXdpHMg, FXVC26csSz4, hqGQcZnEvy0, 2hWmYcG26E8 e la stessa serie) sono ESCLUSE: sono riservate alla home di Hambro. Restano nella cartella solo come traccia, e `_prova/script/finale_img.py` si ferma se una di loro entra in pagina.
- Per la home finale non è stata scaricata nessuna foto nuova.
- È stato scaricato solo il modello di segmentazione BiRefNet lite (licenza MIT, da github.com/danielgatis/rembg/releases) in `_prova/crawl/modelli/`. Produce le maschere di trasparenza del tacco e dei campioni; non genera pixel.
- Nell'ultimo giro sono uscite dalla pagina due foto di repertorio: le minuterie zigrinate di Ivan Di (ALvgGEl8mEE), che non sono un prodotto dell'azienda, e i punzoni di Jos Zwaan (_ifvZpJieZ4). Restano in `esterne/` ma non sono usate.

| File in `sito/img/` | Origine | Licenza | Dove |
|---|---|---|---|
| `tacco-l-*`, `tacco-p-*` | `originali/photos_large_12.jpg`, tacco gioiello a lamelle in ottone (riquadro 880,0-1920,700), scontornato e posato sul cartone con un'ombra; a 1440 ribaltato sull'antidiagonale, a 390 ruotato di 90 gradi | foto di Mario Agnoletto, permesso da confermare | apertura |
| `t-tacchi-*` | `originali/photos_large_12.jpg`, gabbia in acciaio (riquadro 580,420-1580,1080), scontornata e girata di 90 gradi; tolti il tacco a lamelle e il tacco cromato | come sopra | campione 01 |
| `t-punzoni-*`, `t-fustelle-*`, `t-ruote-*` | `originali/photos_large_1.jpg`: cliché col cavallo, stampo a due fiori, ruota forata, scontornati; il quadrotto d'acciaio col monogramma a rovescio è tolto | come sopra | campioni 02, 03, 04 |
| `t-bigiotteria-*` | `originali/photos_large_17.jpg`, farfalle traforate, scontornate | come sopra | campione 05 |
| `t-accessori-*` | `originali/photos_large_13.jpg`, due fibbie in ottone (riquadro 0,0-1180,590), scontornate; la fibbia cromata con la scritta "SHY" è fuori quadro | come sopra | campione 06 |
| `t-stampa-*` | `originali/photos_large_15.jpg`, pelle argento goffrata e cuoio stampato a rilievo (riquadro 380,0-1340,480) | come sopra | campione 07 |
| `finiture-*` | `originali/photos_large_13.jpg`, fibbia a catena e placca martellata (riquadro 1250,0-1920,820); il pezzo col motivo che ricorda un marchio è fuori quadro | come sopra | sezione B, Serie |
| `ottone-*` | `originali/photos_large_2.jpg`, ottone inciso e lastra traforata, foto intera | come sopra | sezione C, Punzoni |
| `fresa-*` | Unsplash pl95tzT0f7Y, mastars MT | Unsplash License | sezione B, Prototipo (segnaposto) |
| `logo.svg`, `timbro.svg`, `timbro-grafite.svg` | ricalco in SVG di `originali/logo.png` (script `_prova/script/proto_b_logo.py`; la versione grafite è lo stesso tracciato con un altro colore) | logo di Mario Agnoletto, da approvare | testata, piede, timbro, dritto e rovescio |
