# Crediti delle immagini

Aggiornato il 20 ottobre 2026.

## Foto esterne in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere di De Checchi Luciano]

Queste foto NON sono di De Checchi Luciano, dei suoi battiscopa o del suo stabilimento. Servono solo a mostrare la direzione artistica nella proposta e vanno sostituite con foto vere dell'azienda prima di qualsiasi uso pubblico (lo dirà anche il LEGGIMI). Nessuna immagine generata dall'IA: ho scartato i candidati marcati "render" o "digital image" (Unsplash `pwnfeq6FT1c`, `NDQIHPA9Iv0`) e tutti quelli Unsplash+.

Licenze lette il 20/10/2026 sulla pagina di ogni foto:
- Unsplash: ogni pagina riporta "Free to use under the Unsplash License"; nessuna è Unsplash+. Licenza (https://unsplash.com/license): uso libero commerciale e non commerciale, senza permesso; non ammesso vendere le foto senza modifiche sostanziali né ricreare un servizio concorrente.
- Pexels: la pagina della foto indica "Free" (Pexels License). Licenza (https://www.pexels.com/license/): "All photos and videos on Pexels are free to use.", "Attribution is not required.", "You can modify the photos and videos from Pexels."; non ammesso "Don't sell unaltered copies of a photo or video", "Don't imply endorsement of your product by people or brands on the imagery.".

Nessuna di queste foto compare nei `CREDITI.md` delle altre home della campagna (controllato il 20/10/2026 su tutte le cartelle `*-Sito/assets/CREDITI.md`). Scaricate dai CDN `images.unsplash.com` e `images.pexels.com` con il lato lungo a 2400 px.

| File | Pagina della foto | Autore | Misura | Uso previsto | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-aHIImdulgtw-sayless-corridoio-battiscopa-alto.jpg` | https://unsplash.com/photos/an-elegant-hallway-with-a-potted-plant-and-archway-aHIImdulgtw | Sayless studios (@saylessstudio) | 1600x2400 | A, apertura o chiusura | corridoio bianco con arco, battiscopa alto sagomato e rovere chiaro: il battiscopa come architettura |
| `esterne/pexels-15226296-designecologist-parete-pavimento.jpg` | https://www.pexels.com/photo/wooden-flooring-against-white-wall-15226296/ | Designecologist (Pexels) | 1600x2400 | A | parete bianca, battiscopa bianco basso, pavimento in legno: la linea tra muro e pavimento. Il pavimento sembra un laminato, possibile foto composta |
| `esterne/pexels-7865621-galeano-corridoio-luminoso.jpg` | https://www.pexels.com/photo/empty-interior-with-white-walls-and-wooden-floor-7865621/ | Gustavo Galeano Maz (@fotografiagmazg, Pexels) | 2400x1600 | A | appartamento vuoto, pareti bianche, battiscopa in legno lungo tutto il corridoio |
| `esterne/unsplash-etUfoBKNRaM-debartolo-corridoio-zoccolino.jpg` | https://unsplash.com/photos/a-modern-hallway-with-an-abstract-painting-and-recessed-lighting-etUfoBKNRaM | Franco Debartolo (@francotheshooter) | 1600x2400 | A e B | corridoio grigio chiaro con zoccolino e boiserie, quadro illuminato |
| `esterne/unsplash-nn1xCtRvUOs-dudeck-luce-al-pavimento.jpg` | https://unsplash.com/photos/black-wooden-floor-with-white-light-nn1xCtRvUOs | Joe Dudeck (@joetography) | 2400x1600 | B, apertura possibile | buio, una lama di luce radente sul legno all'altezza del pavimento: la luce di Woodled come idea |
| `esterne/unsplash-hBudOBV8TUg-putra-luce-radente-parquet.jpg` | https://unsplash.com/photos/sofa-corner-casting-shadows-on-floor-hBudOBV8TUg | Kadek Brahmana Nawa Putra (@kadkbram) | 1800x2400 | B | angolo di divano e luce calda radente sul parquet |
| `esterne/unsplash-6j3laFTi8wg-eiermann-listelli-impilati.jpg` | https://unsplash.com/photos/a-stack-of-wooden-planks-stacked-on-top-of-each-other-6j3laFTi8wg | Georg Eiermann (@georgeiermann) | 2400x1602 | A e B | listelli grezzi impilati in fila: il magazzino, "punto forza" dell'azienda |
| `esterne/unsplash-32NXAlY6iBU-lantaikayu-tre-essenze.jpg` | https://unsplash.com/photos/32NXAlY6iBU | lantai kayu indonesia (@woodfloorindonesia) | 2400x1600 | A | tre campioni di legno di tono diverso su fondo nero: le essenze |
| `esterne/unsplash-0yfG1HXRN5U-watts-venatura-chiara.jpg` | https://unsplash.com/photos/a-close-up-of-a-light-brown-wood-grain-texture-0yfG1HXRN5U | Colin Watts (@colinwatts) | 2400x1600 | A e B | venatura chiara, fondo per testi o per il gesto delle finiture |

## Immagini del sito attuale in `originali/`

Scaricate il 20/10/2026 da `https://www.dechecchiluciano.it/wp-content/uploads/` (232 file, circa 25 MB), elenco ricavato dall'API WordPress (`/wp-json/wp/v2/media`) e dalle pagine del crawl. Inventario, misure, soggetto e voti in `_prova/inventario-immagini.json`. Appartengono a De Checchi Luciano o a Unydeco; due foto (falegname con sega circolare, `2015-05_slide1.jpg` e `2014-05_background_contact.jpg`) sono di repertorio; gli ambienti delle notizie 2025 (Wall-Dec, Battiscopa porta LED) hanno l'aspetto di immagini generate e non vanno usate.

## Logo

- `originali/logo-dechecchi-positivo.svg` e `originali/logo-dechecchi-negativo.svg`: ricostruiti in vettoriale dai tracciati originali contenuti nel depliant Woodled24 (`https://www.dechecchiluciano.it/wp-content/uploads/2020/02/depliant_ITA_WEB.pdf`, pagina 4), senza ridisegnare nulla; colori presi dal PNG del sito (#1D1D1B testo, #E84E0E e #F39200 marchio, #DDDDDD lastra). Manca la riga "SKIRTING AND PROFILES" del logo del sito. Script: `_prova/script/logo_svg.py`.
- `originali/logo-dechecchi-sito-444x152.png`: il logo del sito di oggi (`2017/04/DeChecchi_2017.png`), con la riga "SKIRTING AND PROFILES".

## Uso nel prototipo B della home (`_prova/home/b/`)

Nessuna foto nuova scaricata. Dalle esterne: Debartolo `etUfoBKNRaM` (apertura, di giorno; tolta la presa elettrica dalla boiserie), Dudeck `nn1xCtRvUOs` (apertura, di sera), Putra `hBudOBV8TUg` (chiusura). Dalle originali: `2019-12_woodled_24_DeChecchi_3.jpg` (Woodled24, con una versione "spenta" simulata con PIL per il cursore d'intensità) e `2017-05_De_Checchi_Tecnologia_1.jpg` (reparto). Script: `_prova/script/proto_b_img.py`.

## Uso nella home finale (`sito/`)

Nessuna foto nuova scaricata e nessuna foto esterna usata: le Unsplash e Pexels di `esterne/` restano solo nei prototipi. Tutte le foto della home finale sono di De Checchi Luciano, dal loro sito (diritti e autore da confermare con l'azienda, vedi LEGGIMI):
- apertura: `originali/2017-04_slide_DeChecchi_2.jpg`, ritagliata e posata sulla carta (`_prova/script/finale_maschera.py`, `finale_img.py`);
- fascia delle linee: `originali/2017-04_slide_DeChecchi_3.jpg` (campioni Trattline);
- stabilimenti: `originali/2017-05_De_Checchi_Tecnologia_1.jpg` (reparto);
- chiusura: `originali/2019-12_woodled_24_DeChecchi_3.jpg` (Woodled24 acceso);
- logo: `originali/logo-dechecchi-positivo.svg`.

Carattere: SUSE (Google Fonts, SIL Open Font License 1.1), testo della licenza scaricato il 20/10/2026 da `https://raw.githubusercontent.com/google/fonts/main/ofl/suse/OFL.txt` in `_prova/crawl/ext/suse/OFL.txt` e copiato in `sito/fonts/OFL-SUSE.txt`.
