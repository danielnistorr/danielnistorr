# Crediti delle immagini: Negrizzolo

## Foto dell'azienda

`assets/originali/`: scaricate da http://www.negrizzolo.it il 24/10/2026 (foto, logo, immagine di condivisione). Sono dell'azienda; servono solo per la proposta. L'unica foto non loro è `images_02.jpg` (grano e papaveri, repertorio del vecchio sito) e `images_taglio-laser.jpg` (foto del costruttore della macchina): da non usare.
Il file `tema-industrypress-logo-wide-435x68.png` è il logo del modello ThemeForest rimasto nella cartella del sito: non è un'immagine dell'azienda.

## Foto segnaposto (assets/esterne/)

Licenza Unsplash (https://unsplash.com/license): uso libero anche commerciale, attribuzione non richiesta, modifiche ammesse; non si possono vendere le foto non modificate né usarle per un servizio concorrente. Ogni pagina, letta il 24/10/2026, riporta "Free to use under the Unsplash License" (nessuna è Unsplash+).
Licenza Pexels (https://www.pexels.com/license/): uso libero anche commerciale, attribuzione non richiesta, modifiche ammesse; non si possono rivendere le foto non modificate né far credere che persone o marchi ritratti approvino un prodotto. Ogni pagina, letta il 24/10/2026, riporta la licenza "Free".
Scaricate con curl da images.unsplash.com e images.pexels.com a 2400 px sul lato lungo. Nessuna è generata dall'IA (le pagine indicano fotocamera o autore, nessuna dicitura di immagine generata). Controllate contro tutti i `*-Sito/assets/CREDITI.md` della campagna: nessuna è già usata in un'altra home.

| File | Pagina della foto | Autore | Misure | Uso | Soggetto |
|---|---|---|---|---|---|
| `esterne/unsplash-schaefer-ApoYbda6_3Y.jpg` | https://unsplash.com/photos/white-grapes-in-vineyard-at-harvest-ApoYbda6_3Y | Thomas Schaefer | 2400x1600 | A e B, vasche per uva | uva bianca appena vendemmiata ammucchiata, luce d'oro e vigna sfocata dietro (Barossa Valley, 2016, Canon 5D Mark III) |
| `esterne/unsplash-cairone-lzM3pbQim70.jpg` | https://unsplash.com/photos/black-round-fruit-on-brown-wooden-stick-lzM3pbQim70 | Andrea Cairone | 2400x1350 | B, vendemmia | mani che tagliano un grappolo di Nebbiolo (Serralunga, 2020) |
| `esterne/pexels-myersmc16-31447951.jpg` | https://www.pexels.com/photo/picturesque-vineyard-landscape-in-italy-31447951/ | Gotta Be Worth It (@myersmc16) | 2400x1600 | B, paesaggio | colline a vigneto in Italia dall'alto, con un piccolo mezzo verde tra i filari (la pagina dice solo "Italy") |
| `esterne/pexels-frazier-27260999.jpg` | https://www.pexels.com/photo/a-tractor-is-driving-through-a-vineyard-27260999/ | Richard Frazier | 1600x2400 | B, verticale per il telefono | trattore piccolo in fondo a un filare verde, cielo nuvoloso |
| `esterne/unsplash-weiser-aDDFAlaHg2c.jpg` | https://unsplash.com/photos/tractor-hauling-trailer-full-of-hay-bales-aDDFAlaHg2c | Wolfgang Weiser | 2400x1350 | A e B, rimorchi fissi | pianale carico di rotoballe su stoppie, cielo blu (Hohenhorn, 2025). Trattore verde piccolo sullo sfondo: il marchio non si legge, ma il colore è riconoscibile; tagliare o tenerlo lontano |
| `esterne/unsplash-dittrich-HJIdwdWZoM.jpg` | https://unsplash.com/photos/an-aerial-view-of-a-farm-field-with-a-tractor--HJIdwdWZoM | Bernd Dittrich | 2400x1362 | B, fascia di respiro | campi visti dall'alto a piombo, una mietitrebbia che lascia una scia di polvere (Weinheim, 2024, drone DJI) |
| `esterne/unsplash-yurtman-CxGLY283rWs.jpg` | https://unsplash.com/photos/a-close-up-of-a-machine-cutting-a-piece-of-metal-CxGLY283rWs | Cemrecan Yurtman | 2400x1350 | A e B, taglio laser | ugello del laser radente su una lamiera, poche scintille, luce calda. Stessa serie (non la stessa foto) usata in Tek.Lam: se le due home vanno insieme, preferire la saldatura qui sotto |
| `esterne/unsplash-lambert-9Q_pLLP_jmA.jpg` | https://unsplash.com/photos/welder-working-on-metal-with-sparks-9Q_pLLP_jmA | Rob Lambert | 2400x1600 | A e B, carpenteria | saldatore con maschera e guanti, scintille azzurre (Grass Valley, 2016, Canon 7D) |

Nessuna foto segnaposto mostra un rimorchio o un carrobotte: quelli devono essere i loro. Nessun rimorchio di marchi concorrenti in primo piano (scartata per questo una foto Unsplash con un rimorchio J&M riconoscibile).

## Uso nella home finale (sito/), livello professionale del 03/11/2026

- Solo foto dell'azienda, intere, mai scontornate né ritoccate (stessa leggera curva di contrasto e saturazione per tutte, `_prova/script/pro_img.py`), mai oltre la loro misura:
  - `images_rimorchi-ribaltabili_e.jpg`: apertura (`apertura-*.webp`, 10:7 nativo, 1000 e 720 px);
  - `images_rimorchi-ribaltabili_q.jpg`, `images_rimorchi-fissi_gallery_6.jpg`, `images_carribotte_6.jpg`, `images_vasche-inox_1.jpg`, `images_applicazioni-speciali_5.jpg`: schede dei prodotti (4:3, 800 e 480 px);
  - `wfolder_filesusato_filekc_images_20240926_140048.jpg`: scheda dell'usato (4:3 tagliato dalla foto 4032x2268);
  - `images_esterno-negrizzolo.jpg`: la sede dall'alto in "Orari e contatti" (4:3, 720 e 480 px);
  - `images_foto-antica.jpg`: archivio, in bianco e nero alla sua misura (263x197);
  - logo SVG ricostruito da `images_og-negrizzolo.png` (`logo.svg`, e `logo-chiaro.svg` per il piede scuro).
- Tolte dalla home le versioni scontornate della versione 1 (dumper, ribaltabile, fisso, carrobotte, vasca con ombra disegnata) e il file `archivio-288.jpg`: restano in `_prova/versione-1-originale/`.
- Nessuna foto segnaposto: le otto foto Unsplash e Pexels di `assets/esterne/` non sono usate in nessun punto della home (decisione del committente sulle foto: "niente"); restano nella cartella solo come archivio delle ricerche, da non usare.
- Nessuna foto nuova scaricata.
