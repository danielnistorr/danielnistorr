# Crediti delle immagini

Aggiornato il 19 ottobre 2026.

## Foto esterne in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere di Area Systems]

Queste foto NON sono di Area Systems, del suo magazzino o dei suoi prodotti. Servono solo a mostrare la direzione artistica nella proposta e vanno sostituite con foto vere prima di qualsiasi uso pubblico (lo deve dire anche il LEGGIMI). Nessuna immagine generata dall'IA: una foto candidata che aveva l'aspetto di un render 3D (Unsplash `KlgHazXg2Ic`) è stata scartata per prudenza.

Nessuna di queste foto compare nei `CREDITI.md` delle altre cartelle `*-Sito` della campagna (controllato il 19/10/2026 per ID).

Licenze lette il 19/10/2026 sulla pagina di ogni foto:
- Unsplash: la pagina riporta "Free to use under the Unsplash License"; nessuna è Unsplash+. Licenza (https://unsplash.com/license): "All images can be downloaded and used for free", "Commercial and non-commercial purposes", "No permission needed (though attribution is appreciated!)"; non ammesso: "Images cannot be sold without significant modification." e "Compiling images from Unsplash to replicate a similar or competing service."
- Pexels: la pagina riporta "Free" con il rimando alla licenza (https://www.pexels.com/license/): uso libero, anche commerciale, attribuzione non obbligatoria, modifiche ammesse; non ammesso vendere copie non modificate o far credere che persone o marchi ritratti approvino il prodotto.

Scaricate dai CDN (`images.unsplash.com`, `images.pexels.com`) a 2400 px sul lato lungo.

| File | Pagina della foto | Autore | Scaricata | Direzione | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-CxW8a2ts8GE-matveev-ventola-nera-cemento.jpg` | https://unsplash.com/photos/a-computer-fan-sitting-on-top-of-a-white-surface-CxW8a2ts8GE | Andrey Matveev (@zelebb) | 2400x1800 | A, apertura | una ventola nera con cavo su cemento chiaro, luce morbida. ATTENZIONE: sul mozzo c'è il logo ID-COOLING (marchio di ventole): va ritoccato o coperto dal taglio |
| `esterne/unsplash-MenG-vuJr30-matveev-tre-ventole-bianche.jpg` | https://unsplash.com/photos/three-white-computer-fans-on-a-gray-surface-MenG-vuJr30 | Andrey Matveev (@zelebb) | 2400x1800 | A | tre ventole bianche su grigio: richiama il grigio RAL 7035 dei gruppi ASB. Logo ID-COOLING sul mozzo: da ritoccare |
| `esterne/unsplash-cI-2N2bV6Lo-pancrate-griglia-tonda-acciaio.jpg` | https://unsplash.com/photos/a-close-up-view-of-a-metal-object-cI-2N2bV6Lo | Steve Pancrate (@redaska) | 2400x1600 | A e B | griglia tonda su acciaio spazzolato: l'aria che entra ed esce |
| `esterne/unsplash-CQkoCt7taPo-pancrate-cuffia-sfiato-acciaio.jpg` | https://unsplash.com/photos/a-close-up-of-a-vent-on-a-metal-surface-CQkoCt7taPo | Steve Pancrate (@redaska) | 1600x2400 | A | cuffia di sfiato in acciaio, verticale: richiama le "cuffie di protezione" C08...C32X |
| `esterne/unsplash-NAchd3UmxXo-sime-quadro-aperto.jpg` | https://unsplash.com/photos/open-industrial-electrical-control-panel-with-wires-and-modules-NAchd3UmxXo | Raymond Sime (@raymond36) | 2400x1600 | B, apertura | quadro elettrico aperto, luminoso, cablaggio ordinato: il luogo dove vivono i loro prodotti. Marchi dei moduli piccoli e non leggibili a distanza: da controllare nel taglio |
| `esterne/unsplash-KDkU44ikiko-sime-quadro-cablaggio.jpg` | https://unsplash.com/photos/industrial-electrical-control-panel-with-wiring-and-electronic-components-KDkU44ikiko | Raymond Sime (@raymond36) | 2400x1600 | B | stesso quadro, inquadratura più stretta |
| `esterne/unsplash-GYDBZrVPRU8-sun-dissipatori-in-fila.jpg` | https://unsplash.com/photos/GYDBZrVPRU8 | Declan Sun (@declansun) | 2400x1134 | B | "Neatly arranged heat sinks": alette in fila, fascia orizzontale |
| `esterne/pexels-3520696-padrinan-dissipatore-su-nero.jpg` | https://www.pexels.com/photo/gray-metal-part-3520696/ | Miguel Á. Padriñán (@padrinan) | 2400x1596 | variante scura | dissipatore a raggiera su nero: solo se si sceglie una sezione scura |
| `esterne/pexels-31665486-shox-dissipatore-su-bianco.jpg` | https://www.pexels.com/photo/close-up-of-computer-cooling-heatsink-device-31665486/ | SHOX ART (@shox) | 2400x1800 | A | dissipatore alettato con heat pipe in rame su bianco: il tema "calore" (è un componente da PC, quindi solo segnaposto) |

## Immagini del sito attuale in `originali/`

Scaricate il 19/10/2026 da `https://www.areasystems.it/images/`, `/gallery/` e `/style/` (418 file, circa 10 MB), più 8 immagini estratte dal PDF del catalogo 2022 (`originali/catalogo-2022/`, il PDF da 74 MB è stato cancellato dopo l'estrazione). Inventario, misure, pagine, soggetto e voti in `_prova/inventario-immagini.json`.

Appartengono ad Area Systems o, più probabilmente, ai suoi fornitori: gli scontornati dei ventilatori ACDCFAN, Commonwealth, Jason Fan ed ECOFIT, degli alimentatori Mean Well e dei relè Relpol hanno l'aspetto di foto dei produttori; le 18 foto delle applicazioni (data center, eolico, CNC, fotovoltaico) sono di repertorio di origine ignota. I diritti d'uso vanno chiariti prima di riusarle (vedi 01-analisi, sezione 8).

## Uso nella home finale (`sito/`, 19/10/2026)

- `esterne/unsplash-NAchd3UmxXo-sime-quadro-aperto.jpg`: apertura (quadro aperto con le etichette), in `sito/img/quadro-*.webp` e `quadro-m-*.webp`. SEGNAPOSTO.
- `esterne/unsplash-KDkU44ikiko-sime-quadro-cablaggio.jpg`: fascia dei fili, in `sito/img/fili-*.webp`, tagliata a destra degli alimentatori di marca. SEGNAPOSTO.
- `originali/catalogo-2022/p13-gruppo-ventilazione.jpg` e `p53-resistenza.jpg`: i due pezzi grandi (`gruppo-*.webp`, `resistenza-*.webp`), diritti da chiarire.
- `originali/GT10023AB.png`, `Plafoniera-led-T5.png`, `ASVC200.jpg`, `Gruppi-ASB32S23ABE.png`, `DTV02-N.png`, `CTSH.png`: pezzi del cartellino (`p-*.webp`), diritti da chiarire.
- `originali/style-Area-System-logo.jpg`: marchio orizzontale (`marchio.webp`); serve il vettoriale.
- Le altre foto di `esterne/` non sono usate nella home finale.
