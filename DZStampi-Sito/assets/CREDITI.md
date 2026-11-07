# Crediti delle immagini

Aggiornato il 24 ottobre 2026. Licenza letta sulla pagina di ogni foto il 24 ottobre 2026 con WebFetch: tutte riportano "Free to use under the Unsplash License" (nessuna è Unsplash+). Nessuna immagine è generata dall'IA.

## Foto di repertorio in `esterne/` (segnaposto, da sostituire con foto vere di D.Z. Stampi)

Nessuna mostra D.Z. Stampi, il suo capannone, le sue macchine o i suoi stampi: servono solo a far vedere la direzione artistica nella proposta, e il LEGGIMI dovrà dirlo. In pagina vanno senza didascalie che le attribuiscano all'azienda.

Licenza Unsplash (https://unsplash.com/license): uso libero anche commerciale, senza obbligo di attribuzione, modifiche ammesse; non si possono vendere le foto non modificate né usarle per un servizio concorrente di Unsplash. Scaricate con curl dal CDN `images.unsplash.com` a 2400 px sul lato lungo (qualità 82).

Controllo doppioni: nessuno di questi ID compare nei `CREDITI.md` delle altre cartelle `*-Sito` (verificato il 24/10/2026). Scartata `8MBTn3Z71zI` (Jelifer Maniago) perché già usata nella home di Mario Agnoletto.

Nota sull'autore "Mastars": è il profilo di un'azienda cinese di stampi e stampaggio ("founded in 1998", injection moulding, tooling, die casting, sito mastars.com). Le foto sono scontornati su fondo grigio chiaro senza marchio visibile, quindi non mostrano un concorrente riconoscibile; restano comunque solo segnaposto.

| File | Pagina della foto | Autore | Misura | Direzione | Soggetto |
|---|---|---|---|---|---|
| `esterne/unsplash-Uvj8utkx9Lo.jpg` | https://unsplash.com/photos/Uvj8utkx9Lo | Mastars | 2400x1602 | A, apertura | blocco in alluminio fresato con canali e tasche, luce morbida su grigio chiaro: nitidissimo. È un pezzo lavorato, non uno stampo: solo foto indicativa |
| `esterne/unsplash-fGaYOyRaijs.jpg` | https://unsplash.com/photos/fGaYOyRaijs | Mastars | 2400x1602 | A | lo stesso tipo di blocco fresato visto di fronte, in verticale |
| `esterne/unsplash-Epi5exvDtkU.jpg` | https://unsplash.com/photos/Epi5exvDtkU | Mastars | 2400x1602 | A | componente auto stampato in plastica nera su grigio chiaro: il "pezzo che esce dallo stampo" (automotive) |
| `esterne/unsplash-Ec1mAEzKtRw.jpg` | https://unsplash.com/photos/Ec1mAEzKtRw | Mastars | 2400x1602 | A | due pezzi tecnici in plastica bianca su grigio chiaro (registro medicale) |
| `esterne/unsplash-Rg0KmrUPB_Q.jpg` | https://unsplash.com/photos/Rg0KmrUPB_Q | Diana Polekhina | 2400x1600 | A | piccolo vasetto con tappo azzurro su bianco: pezzo stampato a parete sottile, molta aria |
| `esterne/unsplash-1SutQMy6UVU.jpg` | https://unsplash.com/photos/1SutQMy6UVU | Diana Polekhina | 2400x1600 | A e B | siringhe in plastica su fondo azzurro chiaro (settore medicale) |
| `esterne/unsplash-FizNN4mzOA0.jpg` | https://unsplash.com/photos/FizNN4mzOA0 | hosein fayton | 1920x2400 | B, apertura | stampo vero a più impronte con il golfare di sollevamento, quasi monocromo con dominante verde (da neutralizzare) |
| `esterne/unsplash-O5rSp_U-Pa0.jpg` | https://unsplash.com/photos/O5rSp_U-Pa0 | Jelifer Maniago | 2400x1350 | B | fresa a spianare su un pezzo in alluminio, refrigerante in controluce, fondo scuro sfocato |
| `esterne/unsplash-FizNN4mzOA0-3600.jpg` | https://unsplash.com/photos/FizNN4mzOA0 | hosein fayton | 3600x4500 | finale, apertura | la stessa foto di `FizNN4mzOA0` scaricata il 24/10/2026 (rifinitura) dal CDN a 3600 px di larghezza (`images.unsplash.com/photo-1676646606766-f8325cac7faf?w=3600`), per esportare lo stampo a 2400 px; licenza riletta sulla pagina: "Free to use under the Unsplash License" |
| `esterne/unsplash-sxtClAGwRck.jpg` | https://unsplash.com/photos/sxtClAGwRck | aluminum Zheng ji | 2400x1602 | B | centro di lavoro che fresa una piastra in alluminio con getto di refrigerante, luce chiara d'officina |

## Immagini del sito attuale in `originali/`

Scaricate il 24 ottobre 2026 da `https://www.dzstampi.com/images/` (65 file, 2 MB). Inventario, misure e voti in `_prova/inventario-immagini.json`. Le foto di stampi e pezzi sembrano scattate in azienda; le 11 foto delle macchine sono immagini di catalogo dei costruttori; `segretaria.jpg` è una foto di repertorio. I diritti vanno chiariti prima di riusarle (01-analisi, sezione 9).

## Uso nella home finale (`sito/`, 24 ottobre 2026)

| Foto | Dove | Trattamento |
|---|---|---|
| `FizNN4mzOA0` (hosein fayton), file a 3600 px | apertura | stampo scontornato con OpenCV (maschera tracciata sull'originale 1920x2400 e ingrandita), grigio dal colore, curva morbida con neri sollevati, tinta acciaio appena calda, moncone della seconda colonna tagliato fuori; WebP con trasparenza a 800, 1200, 1800 e 2400 px (`stampo-*.webp`) |
| `1SutQMy6UVU` (Diana Polekhina) | settori, medicale | fondo portato al grigio del campo e allargato |
| `Epi5exvDtkU` (Mastars) | settori, automotive | come sopra |
| `Rg0KmrUPB_Q` (Diana Polekhina) | settori, alimentare | come sopra, azzurro tolto del tutto e contenitore schiarito (è un vasetto da cosmetici, non un pezzo IML decorato: solo segnaposto) |
| `sxtClAGwRck` (aluminum Zheng ji) | lavorazioni | quasi monocromo, banda 5:2 e taglio per il telefono |
| `Ec1mAEzKtRw` (Mastars) | chiusura | fondo portato al grigio del campo, verticale e orizzontale |

Non usate nella home finale: `Uvj8utkx9Lo`, `fGaYOyRaijs`, `O5rSp_U-Pa0`. Nessuna foto nuova scaricata per la versione finale: su Unsplash e Pexels (ricerca del 24/10/2026) non c'è una foto gratuita di uno stampo su fondo chiaro, per questo `FizNN4mzOA0` è stata scontornata.

## Rifinitura del 24 ottobre 2026

- Fondo dei settori, della lavorazione e della chiusura portato a un grigio caldo (#DEDCD7) al posto del grigio freddo; il bordo alto delle foto dei settori prende esattamente il colore della sezione.
- Cercata una foto gratuita di una vaschetta o di un secchiello alimentare decorato (IML) per sostituire il vasetto: su Unsplash e Pexels (WebSearch e WebFetch del 24/10/2026) nessuna adatta. Scartate: `D9L_ftLzvGk` (Nathan Dumlao, contenitori rossi con marchio Rubbermaid leggibile), `Bm40O5riOYc` (Kate Trifo, contenitori da frigo di un marchio d'arredo, cibo dentro), `zqjaFIu5KKw` (Viktor Talashuk, bicchieri di carta in vetrina, fondo scuro), Pexels 13968287 e 13968346 (Ibrahim Plastic Industry, contenitori in posa con foglie e paglia; l'autore è un produttore di plastica), Pexels 8015465 (flaconi cosmetici). Nessuna scaricata in `assets/`.
