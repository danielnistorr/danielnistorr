# Crediti delle immagini

Aggiornato il 19 ottobre 2026.

## Foto esterne in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere di Hambro]

Queste foto NON sono di Hambro, del suo magazzino o dei suoi articoli. Servono solo a mostrare la direzione artistica nella proposta e vanno sostituite con foto vere dell'azienda prima di qualsiasi uso pubblico (lo dice anche il LEGGIMI). Nessuna immagine generata dall'IA.

Licenza letta il 19/10/2026 sulla pagina di ogni foto: tutte riportano "Free to use under the Unsplash License"; nessuna è Unsplash+.
Licenza Unsplash (https://unsplash.com/license): "All images can be downloaded and used for free", "Commercial and non-commercial purposes", "No permission needed (though attribution is appreciated!)"; non ammesso: "Images cannot be sold without significant modification." e "Compiling images from Unsplash to replicate a similar or competing service."

Versioni scaricate dal CDN `images.unsplash.com` a 2400 px di larghezza (la dimensione originale non è indicata sulla pagina).

| File | Pagina della foto | Autore | Scaricata | Direzione | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-FXVC26csSz4-rodrigues-fibbia-oro-riflesso.jpg` | https://unsplash.com/photos/golden-buckle-reflecting-on-a-shiny-surface-FXVC26csSz4 | Ruan Richard Rodrigues (@ricdeoliveira) | 2400x3600 | A, apertura | fibbia dorata su piano a specchio, fuoco cortissimo, luce calda |
| `esterne/unsplash-hqGQcZnEvy0-rodrigues-fibbie-oro-argento.jpg` | https://unsplash.com/photos/two-shiny-metal-belt-buckles-on-a-reflective-surface-hqGQcZnEvy0 | Ruan Richard Rodrigues (@ricdeoliveira) | 2400x3600 | A | due fibbie, oro e nichel: il tema delle finiture |
| `esterne/unsplash-CkeOwnoLK5U-rodrigues-fibbia-argento.jpg` | https://unsplash.com/photos/a-shiny-metal-buckle-on-a-reflective-surface-CkeOwnoLK5U | Ruan Richard Rodrigues (@ricdeoliveira) | 2400x3600 | A | fibbia nichelata su specchio, riflessi dorati |
| `esterne/unsplash-2hWmYcG26E8-rodrigues-fibbie-borchie-bianco.jpg` | https://unsplash.com/photos/two-gold-buckles-with-pyramid-studs-and-a-detached-piece-2hWmYcG26E8 | Ruan Richard Rodrigues (@ricdeoliveira) | 2400x3600 | B, apertura | fibbie dorate con borchie su bianco, ombra netta di sole |
| `esterne/unsplash-WL8DY_Dm7X8-compagnons-grana-nera.jpg` | https://unsplash.com/photos/close-up-of-textured-black-leather-material-WL8DY_Dm7X8 | Compagnons (@sigmund) | 2400x1800 | A | grana di pelle nera: fondo per i testi |
| `esterne/unsplash-DmxTTqZtDds-karimov-grana-cuoio.jpg` | https://unsplash.com/photos/close-up-of-textured-brown-leather-material-DmxTTqZtDds | Igor Karimov (@ingvar_erik) | 2400x1340 | A e B | cuoio marrone con pieghe, macro |
| `esterne/unsplash-wMZgJ7RyvuQ-junojo-nastri-appesi.jpg` | https://unsplash.com/photos/wMZgJ7RyvuQ | Juno Jo (@junojo) | 2400x1800 | B | nastri e fettucce appesi per colore: i nastri per tracolla |
| `esterne/unsplash-cgkmLypPQ84-chan-bobine-nastro.jpg` | https://unsplash.com/photos/cgkmLypPQ84 | Devon Chan (@devonchan) | 2400x1600 | B | bobine di nastro in fila: il campionario |
| `esterne/unsplash-an44PeEll_w-berg-mani-cartamodello.jpg` | https://unsplash.com/photos/person-tracing-shoe-pattern-on-leather-an44PeEll_w | Cohen Berg (@cohenberg) | 2400x1600 | A e B | mani che tracciano un cartamodello su pelle: il laboratorio "su richiesta del cliente" |
| `esterne/unsplash-eWIHPOZIFU0-tepavac-corda-avvolta.jpg` | https://unsplash.com/photos/eWIHPOZIFU0 | Tanja Tepavac (@ttepavac) | 2400x3600 | A e B | corda avvolta stretta: richiama le bobine di laccio e tondino |

## Immagini del sito attuale in `originali/`

Scaricate il 19/10/2026 da `https://www.hambro.it/immagini/full/` (139 file). Inventario, misure, soggetto e voti in `_prova/inventario-immagini.json`. Appartengono a Hambro o ai suoi fornitori: 10 sono scansioni di pagine del catalogo di terzi "ASTOR" e almeno 3 (le foto dello slider) hanno l'aspetto di foto da catalogo di un produttore; i diritti d'uso vanno chiariti prima di riusarle (vedi 01-analisi, sezione 8).

## Uso nella home finale (`sito/`, 19/10/2026)

Rielaborate con `_prova/script/finale_img.py` (ritaglio, gradazione sulla carta, nitidezza, più larghezze); nessuna immagine generata.
- Rodrigues `2hWmYcG26E8`: apertura, specchiata (tagli 1440+, tablet, telefono). Ritoccata: tolta la borchia sciolta in basso a destra, che nel taglio 16:10 entrava tagliata dal bordo (la Unsplash License permette di modificare la foto).
- Rodrigues `hqGQcZnEvy0`: la fibbia oro del dittico "il metallo", fondo ripulito dal rumore.
- Karimov `DmxTTqZtDds`: la pelle del dittico e la striscia del banco, portate sul cuoio #8A5230.
- Berg `an44PeEll_w`: semilavorati.
- Da `originali/` (hambro.it, diritti da chiarire): `2020082819b510e6283f3e7a1a998eb253a83ccd.jpeg` (bobina di laccio) e `20200828c559dc21f28d28e6c910602764e6d35f.jpeg` (bobina di tondino) per la Tav. 2; 11 scontornati del catalogo per il cassetto (elenco in `finale_img.py`).
- Non usate nella home finale: Tepavac, Juno Jo, Devon Chan, Compagnons, Rodrigues `FXVC26csSz4` e `CkeOwnoLK5U`.
