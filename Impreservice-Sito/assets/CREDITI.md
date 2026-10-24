# Crediti delle immagini: Impreservice

## assets/esterne/ (segnaposto per la proposta)

Foto di repertorio scaricate il 24/10/2026. Su ogni pagina ho controllato la licenza: le Pexels sono indicate come "Free" (Licenza Pexels, uso commerciale gratuito, attribuzione non obbligatoria); le Unsplash come "Free to use under the Unsplash License" e non sono Unsplash+. Nessuna è generata dall'IA. Nessuna compare nei CREDITI.md delle altre home della campagna (controllato per identificativo). Sono segnaposto: per il sito vero servono foto di Impreservice (vedi 01-analisi.md, sez. 4 e 9).

| File | Pagina della foto | Autore | Licenza | Misura | Uso pensato | Nota |
|---|---|---|---|---|---|---|
| `esterne/pexels-34842262-sharma-galleria-conci-chiara.jpg` | https://www.pexels.com/photo/engineer-inspecting-subway-construction-tunnel-34842262/ | Anil Sharma (@shootsaga) | Pexels, Free | 2400x1600 | A, apertura | galleria a conci appena posata, chiara e luminosa, un tecnico in fondo. I giunti tra i conci sono leggibili |
| `esterne/pexels-11424325-mishin-galleria-metro-conci.jpg` | https://www.pexels.com/photo/interior-of-metro-tunnel-11424325/ | Max Mishin (@maxmishin) | Pexels, Free | 2400x1600 | B, apertura | galleria di metropolitana rivestita a conci, anelli in prospettiva, toni scuri |
| `esterne/pexels-16227437-ballidag-pozzo-gru-istanbul.jpg` | https://www.pexels.com/photo/sunlit-borehole-and-beams-16227437/ | Sururi Ballıdağ Director (@drector) | Pexels, Free | 2400x1600 | A e B, referenze | pozzo di partenza di una fresa visto dall'alto, carroponte giallo, Istanbul |
| `esterne/pexels-36520209-nadirsyah-tbm-erettore-giacarta.jpg` | https://www.pexels.com/photo/tunnel-boring-machine-with-engineer-in-jakarta-36520209/ | Nadirsyah Nadirsyah | Pexels, Free | 2400x1600 | B, dettaglio | dentro la fresa, la zona dell'erettore che posa i conci. Molto colorata: va desaturata o usata piccola |
| `esterne/pexels-10321271-mishin-testa-fresa-mosca.jpg` | https://www.pexels.com/photo/worker-on-a-construction-10321271/ | Max Mishin (@maxmishin) | Pexels, Free | 2400x1600 | B, referenze | testa di scavo di una fresa con un operaio, Mosca |
| `esterne/pexels-27808651-nagda-viadotto-sotto.jpg` | https://www.pexels.com/photo/the-underside-of-a-bridge-with-two-pillars-27808651/ | Kewal Nagda | Pexels, Free | 2400x1802 | A e B, ponti e viadotti | intradosso di due viadotti gemelli, simmetrico, luce calda e nebbia |
| `esterne/pexels-17048866-hofer-anelli-cemento-berna.jpg` | https://www.pexels.com/photo/close-up-of-cement-blocks-in-row-17048866/ | Harri Hofer (@harri) | Pexels, Free | 2400x1600 | A, dettaglio o chiusura | elementi prefabbricati ad anello impilati al sole, Berna |
| `esterne/unsplash-mFmRXUBb11g-gomezangel-galleria-zurigo.jpg` | https://unsplash.com/photos/mFmRXUBb11g | Ricardo Gomez Angel (@rgaleriacom) | Unsplash License | 2400x1431 | A e B, chiusura | galleria pedonale in calcestruzzo con luce calda in fondo, Zurigo |
| `esterne/unsplash-CPI7JAIVaDU-mpikakis-anello-avdou.jpg` | https://unsplash.com/photos/a-couple-of-men-standing-next-to-a-giant-object-CPI7JAIVaDU | Evangelos Mpikakis (@mpikman) | Unsplash License | 2400x1600 | B, cantiere | scudo ad anello di una fresa su una culla bianca, due operai, luce di giorno, Creta |
| `esterne/pexels-20818874-dvoretskyi-calcestruzzo-chiaro.jpg` | https://www.pexels.com/photo/smooth-gray-concrete-texture-20818874/ | Артем Дворецкий (@834934396) | Pexels, Free | 3200x3200 (originale 5000x5000) | apertura della home finale | superficie di calcestruzzo chiaro con pori e grana fine, luce piatta. Scaricata il 24/10/2026, licenza controllata sulla pagina, non segnata come generata dall'IA, non presente nei CREDITI.md delle altre home |

Scaricate da images.pexels.com e images.unsplash.com con curl, alla larghezza di 2400 px.

## assets/originali/ (dal sito di oggi)

Scaricate da impreservicesrl.it il 24/10/2026: elenco, misure e voti in `_prova/inventario-immagini.json`. Molte non sono di Impreservice (Pexels, Unsplash, Pixabay, foto stampa di progetti, render Alstom, catture di altri siti): non vanno riusate senza chiarire i diritti. Il fotogramma `90-youtube-jxtiioap3hc-maxres.jpg` è la copertina del loro video YouTube (il video non è stato scaricato).

## Uso nella home finale (sito/img/)

- `sez-sx-*`, `sez-dx-*`, `sez-dx-b-*` (apertura): i due conci sono la superficie di calcestruzzo di Dvoretskyi, Pexels 20818874 (due ritagli diversi, grana tenuta, macchie larghe tolte, tono caldo); il connettore Easy Click Smart è reso dallo script `_prova/script/sezione_img.py` come solido di rivoluzione, con i profili misurati sui disegni CAD dell'azienda (`12-bussola-smart.png`, `13-asm-smart.jpg`, `14-perno-smart.png`) e il colore nero dei loro render (`34/35/36-Senza-nome`). Nessuna immagine generata dall'IA.
- `galleria-*`: Mishin, Pexels 11424325 (sezione Easy Click).
- `viadotto-*`: Nagda, Pexels 27808651 (ponti e viadotti).
- `scudo-*`: Mpikakis, Unsplash CPI7JAIVaDU (chiusura).
- `logo-simbolo-*`: simbolo dell'azienda (`logo-impreservice-icona-blu-1000.png`).
- Non più in pagina: il pozzo di Ballıdağ (Pexels 16227437) e i livelli `ec-*` ricavati dai disegni CAD.
