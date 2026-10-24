# Crediti delle immagini

Aggiornato il 24 ottobre 2026.

## Foto esterne in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere di Etichettificio Veneto]

Queste foto NON mostrano etichette stampate da Etichettificio Veneto, i suoi reparti o le sue macchine. Servono solo a mostrare la direzione artistica nella proposta e vanno sostituite con foto vere prima di qualsiasi uso pubblico (lo dirà anche il LEGGIMI). Nessuna immagine generata dall'IA: ho scartato i rendering 3D trovati nelle ricerche (flaconi e vasetti "mockup").

Attenzione in pagina: due foto mostrano etichette di marchi veri (AESOP Wines, la bottiglia di Nadi Spasibenko con etichetta illustrata) e una mostra vasetti di miele di un mercato agricolo americano. Nessuno è un concorrente, ma in pagina non devono far credere che quelle etichette le abbia stampate Etichettificio Veneto: niente didascalie del tipo "un nostro lavoro".

Licenze lette il 24/10/2026 sulla pagina di ogni foto:
- Unsplash: tutte riportano "Free to use under the Unsplash License"; nessuna è Unsplash+. Licenza (https://unsplash.com/license): uso libero commerciale e non commerciale, senza permesso; non è ammesso vendere le foto senza modifiche sostanziali o usarle per un servizio concorrente.
- Pexels: la pagina riporta "License: Free" con il rimando alla Pexels License (https://www.pexels.com/license/): uso libero, attribuzione non obbligatoria; non ammesso vendere copie non modificate o far credere che le persone ritratte approvino un prodotto.

Scaricate dai CDN `images.unsplash.com` e `images.pexels.com`, al massimo 2400 px sul lato lungo. Nessuna è già usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 24/10/2026, per identificativo e per hash del file CDN).

| File | Pagina della foto | Autore | Misura | Uso pensato | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-4kzCp4By8HY-aesop-bottiglia-rosato-etichetta.jpg` | https://unsplash.com/photos/white-and-blue-labeled-bottle-4kzCp4By8HY | AESOP. Wines© (@aesopwines) | 1600x2400 | A, apertura | bottiglia di rosato su bianco, etichetta grafica "20 19"; a sinistra dei gigli da tagliare. Il nome del marchio è minuscolo sul bordo dell'etichetta |
| `esterne/unsplash-vKHbJgYXmc0-spasibenko-bottiglia-luce-dura.jpg` | https://unsplash.com/photos/vKHbJgYXmc0 | Nadi Spasibenko (@nadispasibenko) | 1586x2400 | A o B, chiusura | bottiglia chiara con etichetta illustrata, sole radente e ombra lunga su fondo caldo |
| `esterne/pexels-8982957-jordan-etichetta-vino-macro.jpg` | https://www.pexels.com/photo/grayscale-photo-of-lettering-on-a-wine-bottle-8982957/ | Brett Jordan | 2400x1800 | B | macro di un'etichetta nera con lettere bianche in rilievo: il dettaglio di stampa |
| `esterne/unsplash-shLU6SZfIQY-kier-foglia-oro.jpg` | https://unsplash.com/photos/shLU6SZfIQY | Kier in Sight Archives (@kierinsightarchives) | 1800x1800 | B | foglia d'oro vera stropicciata: richiama il cold foil ("lamine dorate ed argentate") e la facciata dorata della sede. Ridotta da 2400 a 1800 per peso |
| `esterne/unsplash-zDcJ2DFew9M-roberts-etichette-in-macchina.jpg` | https://unsplash.com/photos/worker-feeding-labels-into-a-machine-zDcJ2DFew9M | Anthony Roberts (@arcreates) | 1600x2400 | A e B | mano che guida un nastro di etichette in macchina: la produzione |
| `esterne/pexels-9550363-criiv-macchina-da-stampa.jpg` | https://www.pexels.com/photo/close-up-of-a-printing-machine-9550363/ | Criiv India | 2400x1800 | B | macchina da stampa a fogli in funzione (non è una flexo da bobina: segnaposto) |
| `esterne/pexels-5532716-cottonbro-etichettatrice-bobine.jpg` | https://www.pexels.com/photo/automated-production-of-beer-labels-5532716/ | cottonbro studio | 1600x2400 | A e B | etichettatrice con le bobine di etichette montate: dove finiscono le loro bobine |
| `esterne/pexels-6250876-shvets-striscia-codici-a-barre.jpg` | https://www.pexels.com/photo/a-person-holding-barcodes-on-pink-background-6250876/ | Anna Shvets | 1600x2400 | A | striscia di etichette con codice a barre su fondo rosa: le etichette per la sicurezza e i bar code |
| `esterne/unsplash-9HajXdvKpIk-bartlett-vasetti-miele.jpg` | https://unsplash.com/photos/9HajXdvKpIk | Amelia Bartlett (@ameliabartlett) | 2400x1590 | A | vasetti di miele con etichetta stampata, luce naturale: il settore alimentare |

### Aggiunte per la home finale (24/10/2026)

Licenze lette il 24/10/2026 sulla pagina di ogni foto: Unsplash "Free to use under the Unsplash License", non Unsplash+; Pexels "Free" con rimando alla Pexels License. Nessuna è usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` per identificativo e nome dell'autore). Nessuna è generata dall'IA.

| File | Pagina della foto | Autore | Misura | Uso | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-ThjUa4yYeX8-element5-bobina-etichette.jpg` | https://unsplash.com/photos/white-and-black-rolled-sticker-on-white-surface-ThjUa4yYeX8 (la stessa foto è anche su Pexels, n. 1550336) | Element5 Digital (@element5digital) | 3600x2403 | apertura della home finale | bobina di etichette tonde srotolata su fondo bianco. In origine sono adesivi elettorali americani ("I VOTED", stelle e strisce): con `_prova/script/bobina_neutra.py` ho tolto scritta e stelle (riempite con i pixel vicini) e virato il rosso delle strisce in oro; il blu resta inchiostro pieno, portato verso il blu del logo. Poi `immagini_finale.py` uniforma il fondo alla carta della pagina e specchia l'immagine. La licenza Unsplash consente le modifiche. In pagina c'è "Foto indicativa" |
| `esterne/pexels-35389955-maram-vasetti-marmellata.jpg` | https://www.pexels.com/photo/homemade-blueberry-and-strawberry-jam-jars-35389955/ | Maram (@maram-145487840) | 2400x3200 | scheda Alimentare | due vasetti di marmellata su un telo bianco, vista dall'alto; etichette "Blueberry Jam" e "Strawberry Jam", nessun marchio. Nella rifinitura finale: ruotata di 46 gradi perché i due vasetti stiano in fila, scritte a mano tolte; i due angoli scoperti dalla rotazione sono riempiti con il telo riflesso |
| `esterne/pexels-20140032-leeloo-flaconcini-etichette.jpg` | https://www.pexels.com/photo/healthcare-medicine-bottles-20140032/ | Leeloo The First (@leeloothefirst) | 2400x3595 | scheda Multipagina | flaconcini di vetro con etichette stampate su un piano chiaro, luce dura; sulle etichette nomi di prodotto generici ("Stress", "Focus"), nessun marchio. Scritte tolte nella rifinitura finale |

### Aggiunte per la rifinitura finale (24/10/2026)

Licenze lette il 24/10/2026 sulla pagina di ogni foto (Unsplash "Free to use under the Unsplash License", non Unsplash+; Pexels "Free" con rimando alla Pexels License). Nessuna è usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` per identificativo; di Katie Harp la home di Bertolin Antonio usa un'altra foto, `vdEXeB_hSCw`). Nessuna è generata dall'IA.

| File | Pagina della foto | Autore | Misura | Uso | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-Em96eDRJPD8-harp-lamina-oro.jpg` | https://unsplash.com/photos/Em96eDRJPD8 | Katie Harp (@kharp) | 2400x1596 | apertura della home finale | foto vera di lamina oro ("gold metallic foil texture background"). Con `_prova/script/etichetta_oro.py` diventa la faccia di un'etichetta autoadesiva in lamina, con sopra il logo dell'azienda stampato in blu e l'angolo in basso a sinistra che si solleva (geometria calcolata, ombre calcolate). È un fotomontaggio, non una foto di un loro lavoro: in pagina c'è "Le immagini della pagina sono indicative" e nel LEGGIMI lo scatto vero è la foto n. 1 |
| `esterne/pexels-20140036-leeloo-bottiglia-etichetta.jpg` | https://www.pexels.com/photo/healthcare-medicine-bottles-20140036/ | Leeloo The First (@leeloothefirst) | 2400x3595 | scheda Cosmesi e chimico | bottiglia di vetro e quattro flaconcini dall'alto su fondo bianco, stessa serie della foto dei flaconcini. Scritte inglesi delle etichette ("Stop Burnout", "Stress Kit") tolte con `pulisci_testo()` in `immagini_finale.py`; resta il codice a barre. Ruotata di 90 gradi |

Lavorazioni comuni delle quattro foto dei settori (`immagini_finale.py`): scritte delle etichette tolte, dominante del fondo neutralizzata e bianco portato alla carta della pagina #F3F1EC. Sui vasetti di Maram tolte anche le scritte a mano "Blueberry Jam" e "Strawberry Jam"; sulla striscia di Anna Shvets il fondo rosa è portato al bianco carta. Le licenze Unsplash e Pexels consentono le modifiche.

Nella home finale non si usano più: la bobina di Element5 Digital (era l'apertura fino al giudizio cieco), la foglia d'oro di Kier in Sight Archives (era la scheda Cosmesi), la bottiglia AESOP, il miele di Bartlett, l'etichetta nera di Jordan (scritte sul vino), la macchina di Criiv, l'etichettatrice di cottonbro e la bottiglia di Spasibenko. Restano qui per i prototipi.

## Immagini del sito attuale in `originali/`

Scaricate il 24/10/2026 da `https://www.etichettificioveneto.com/wp-content/uploads/` e dal tema `MotivoNewtork5.9` (31 file: 23 foto, 4 file del logo, 1 grafica, 3 PDF). Inventario, misure, soggetto e voti in `_prova/inventario-immagini.json`. Tutte le foto sono di repertorio tranne la facciata della sede (`2015-11-sld02.jpg`); i diritti delle foto di repertorio sono legati alla licenza acquistata a suo tempo dall'agenzia del sito e non vanno riusate. I loghi e i certificati sono dell'azienda.
