# Crediti delle immagini: 247LAB

## Immagini dell'azienda (`originali/`)

Scaricate il 20/10/2026 da `static.wixstatic.com` (il sito www.247lab.it è su Wix).

- `originali/scelte-2400/F*.jpg`: 32 foto scelte, ridotte a 2400 px sul lato lungo. Il codice F corrisponde all'inventario `_prova/inventario-immagini.json`.
- `_prova/crawl/media800/*.img`: tutte le 736 immagini del sito (JPEG a 800 px sul lato lungo, solo per l'inventario e i fogli provino). Le 3 che non si sono scaricate sono PNG che Wix rifiuta ("bad file").
- `originali/cataloghi/`: i tre cataloghi 2026 in PDF (Twentyfour7, RB, G-label), dalla pagina `cataloghi` del sito.
- `originali/logo-*`: logo 247LAB (PNG bianco originale 2246x455, SVG ricostruito, WebP 320 px bianco e nero), logo RB (PNG oro 2366x1977 e SVG), pittogramma del faretto su binario usato come favicon (PNG 2500x2500 e SVG).

- `originali/hi/F346-full.jpg`, `F713-full.jpg`, `F042-full.jpg`: le stesse foto F346, F713 e F042 alla misura piena del CDN Wix (4573x3049, 3177x2118, 4608x3072), scaricate il 20/10/2026 per l'apertura e le foto a tutta larghezza del prototipo A; PNG convertiti in JPEG qualità 93.
- `originali/cataloghi-foto/glabel-*.jpg`: tre foto estratte con `pdfimages` dal catalogo `G-label_Catalogo_2026_ITA.pdf` (pagine 2 e 3): SPOT G-6 e LINEA L-20 su binario verticale (1584x2190), mano che orienta il faretto (3976x2695). Autore non indicato nel catalogo.

Diritti da chiarire prima di pubblicare (vedi `01-analisi.md`, sezione 9):
- le foto dei progetti portano sul sito il nome del fotografo (per esempio Pietro Savorelli, Hufton+Crowl, Max Zambelli, Alessandro Cusano, Marco Zonta, Flavio Ricci): servono il permesso e il credito;
- nelle foto dei negozi compaiono marchi di terzi (Fendi, Dolce&Gabbana, Casadei, Valentino, Givenchy, Alaïa): sono clienti, non concorrenti, ma il loro uso in home va concordato;
- l'autore delle foto di prodotto e dei ritratti di Roberto e Marco non è indicato.

## Immagini sostitutive (`esterne/`)

Scaricate il 20/10/2026 con curl dal CDN (`images.unsplash.com`, `images.pexels.com`) a 2400 px sul lato lungo. La licenza è stata controllata sulla pagina di ogni foto con WebFetch: per Unsplash "Free to use under the Unsplash License" (nessuna Unsplash+), per Pexels "Free" con il rimando alla licenza Pexels. Nessuna è generata dall'IA. Nessuna compare nei `CREDITI.md` delle altre home della campagna (controllo sugli ID, 20/10/2026). Sono segnaposto: dove possibile vanno sostituite da foto vere di 247LAB.

| File | Pagina della foto | Autore | Misura | Uso | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-QjBZPbZqn-8-liao-ottone-su-bianco.jpg` | https://unsplash.com/photos/brass-mechanical-device-with-wing-nut-QjBZPbZqn-8 | Spencer Liao (@spencerliao) | 2400x1600 | A, dettaglio | un piccolo meccanismo in ottone con vite e galletto su fondo bianco: il "pezzo in ottone" su chiaro, in attesa di un macro vero dei loro snodi |
| `esterne/unsplash-RIQ96s3Uzso-possingham-luce-finestra-parete.jpg` | https://unsplash.com/photos/window-shadow-on-wall-RIQ96s3Uzso | Alexander Possingham (@allexx54) | 2400x3600 | A, fondo | luce calda di finestra su una parete chiara |
| `esterne/unsplash-u7VDgNGb78w-hermant-luce-geometrica-cemento.jpg` | https://unsplash.com/photos/concrete-wall-with-geometric-light-and-shadow-u7VDgNGb78w | Bernard Hermant (@bernardhermant) | 2400x3600 | A, fondo | luce geometrica su cemento chiaro |
| `esterne/unsplash-qO_1O_2mg4k-ismail-matita-su-carta.jpg` | https://unsplash.com/photos/qO_1O_2mg4k | Qeis Ismail (@trileafu) | 2400x3598 | A e B | matita su carta: lo schizzo da cui parte ogni lampada (sostituibile con il loro tavolo di lavoro F042) |
| `esterne/unsplash-rIKWHwHWQrg-liao-banco-seghetto-metallo.jpg` | https://unsplash.com/photos/person-using-jewelers-saw-at-workbench-rIKWHwHWQrg | Spencer Liao (@spencerliao) | 2400x1600 | A e B, laboratorio | mani con seghetto da orafo su metallo al banco; il volto si vede: solo come riferimento, da rifare nel loro laboratorio |
| `esterne/unsplash-ADMBRR2RKu4-lopatin-lama-di-luce-parete-scura.jpg` | https://unsplash.com/photos/the-shadow-of-a-window-on-a-wall-ADMBRR2RKu4 | Ivan Lopatin (@gingray) | 2400x1603 | B, fondo | una lama di luce calda su parete scura: "We don't fear the dark" |
| `esterne/unsplash-Hjp111tSqKc-watts-foglia-oro.jpg` | https://unsplash.com/photos/a-textured-golden-surface-with-light-reflections-Hjp111tSqKc | Colin Watts (@colinwatts) | 2400x1600 | B, materia | superficie in foglia d'oro con riflessi; non è ottone: solo come fondo per il selettore delle finiture |
| `esterne/pexels-14593018-fishsteakfries-viti-ottone.jpg` | https://www.pexels.com/photo/pile-of-golden-screws-14593018/ | Fish Steak Fries (profilo Pexels) | 2400x1600 (originale 5760x3840) | A e B, materia | mucchio di viti e raccordi in ottone: la materia prima |
| `esterne/pexels-5023995-santiago-tubo-ottone-legno-scuro.jpg` | https://www.pexels.com/photo/close-up-of-a-golden-pipe-5023995/ | Shawn Santiago | 2400x1600 (originale 6240x4160) | B | un tubo in ottone tornito su legno scuro, luce bassa |

Cercate e scartate (20/10/2026): Unsplash P8CGvIQB1uo (tubi color ottone: è il motore di un SR-71), m6aXFCYBJz0 (tornio a Mumbai, sporco e fuori registro), GwtQGmTOCIE (mani su metallo: già usata in un'altra home della campagna), UbsDLjqZ9RM, 26_e1IXEsaE, UYdtwfoKZQY (oggetti in ottone ornamentali, fuori registro); foto di lampade di altri marchi (ricerca "brass lamp", "brass light fixture"): escluse perché sarebbero prodotti concorrenti riconoscibili.

## Prototipo B (`originali/b-2400/`)

Scaricate il 20/10/2026 da `static.wixstatic.com` (sito di 247LAB), come le altre foto dell'azienda: F001 (profilo 1111), F018 (Roberto al banco), F024 e F024-3200 (BOATY S accesa), F026 (BOATY terra), F044, F045, F046 (MINA nelle tre finiture), F056, F066 (CIUCCIO), F075, F428-2880 e F496-2880 (Harry's Piccolo, Trieste 2025, foto Roberto Pastrovicchio). Stessi diritti da chiarire della sezione sopra. Nessuna foto di repertorio nel prototipo B.
