# Crediti delle immagini

Aggiornato il 19 ottobre 2026.

## Foto esterne in `esterne/` [SEGNAPOSTO, DA SOSTITUIRE con foto vere dell'officina Bazzato]

Queste foto NON sono dell'officina Bazzato, dei suoi spazi o delle auto dei suoi clienti. Servono solo a mostrare la direzione artistica nella proposta e vanno sostituite con foto vere prima di qualsiasi uso pubblico (lo dirà anche il LEGGIMI). Nessuna immagine generata dall'IA. Nessuna è già usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 19/10/2026).

Licenze lette il 19/10/2026 sulla pagina di ogni foto:
- Unsplash: tutte riportano "Free to use under the Unsplash License"; nessuna è Unsplash+. Licenza (https://unsplash.com/license): uso libero anche commerciale, senza permesso; non ammesso vendere le foto senza modifiche sostanziali o usarle per un servizio concorrente.
- Pexels: la pagina riporta "Free" con rimando a https://www.pexels.com/license/ (uso libero anche commerciale, attribuzione non obbligatoria; non ammesso rivendere le foto non modificate o far credere che persone o marchi ritratti approvino il prodotto).

Versioni scaricate dai CDN `images.unsplash.com` e `images.pexels.com` a 2400 px di lato lungo.

| File | Pagina della foto | Autore | Misura | Direzione | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-EpT-ZetoKm8-mclean-disco-freno-forato.jpg` | https://unsplash.com/photos/EpT-ZetoKm8 | Erik Mclean (@introspectivedsgn) | 2400x1603 | A, apertura provvisoria | disco forato e pinza su scocca bianca, luce chiara; nessun marchio leggibile |
| `esterne/unsplash-al01Ad0f_KI-brunner-disco-pinza-luce-calda.jpg` | https://unsplash.com/photos/al01Ad0f_KI | Benjamin Brunner (@ben_brunner) | 2400x1600 | B, apertura provvisoria | disco e pinza di un'auto comune, smontati, luce calda radente; nessun marchio |
| `esterne/unsplash-yULLNDpatrc-belanger-bussole-cromate.jpg` | https://unsplash.com/photos/chrome-socket-wrench-heads-on-rails-yULLNDpatrc | Danielle-Claude Bélanger (@dcbelanger) | 2400x1600 | A | bussole cromate in fila sul fondo chiaro: il banco attrezzi |
| `esterne/unsplash-tLEUi4OaQmQ-yvettes-battistrada-macro.jpg` | https://unsplash.com/photos/a-close-up-of-a-tire-tLEUi4OaQmQ | Yvette S (@photography_yeti) | 2400x1600 | A e B | macro del battistrada: il servizio gomme |
| `esterne/pexels-37002235-gomme-impilate-bn.jpg` | https://www.pexels.com/photo/stacked-vehicle-tires-in-black-and-white-37002235/ | wal_ 172619 | 2400x1600 | B | gomme impilate in bianco e nero, nessun marchio leggibile |
| `esterne/unsplash-9uHal2Dd9aE-masth-mani-gomma.jpg` | https://unsplash.com/photos/a-man-working-on-a-tire-in-a-garage-9uHal2Dd9aE | Jimmy Nilsson Masth (@jimmynilssonmasth) | 2400x1600 | A e B | mani con guanti che montano una ruota |
| `esterne/unsplash-Fd6osyVbtG4-buehner-mani-chiave-motore.jpg` | https://unsplash.com/photos/hands-working-on-car-engine-Fd6osyVbtG4 | Christian Buehner (@christianbuehner) | 2400x1800 | B | mani unte con chiave nel vano motore, luce calda |
| `esterne/pexels-33814736-razumov-officina-chiara-ponte.jpg` | https://www.pexels.com/photo/modern-car-repair-shop-interior-with-vehicle-33814736/ | Renee Razumov | 2400x1600 | A e B | officina bianca e luminosa con un'auto sul ponte. Attenzione: sul portellone si legge "SKODA" in piccolo al centro: solo come riferimento di luce, da non pubblicare così |

Scartate dopo la verifica: due foto di Erik Mclean con una ruota su muro bianco (coprimozzo Toyota e gomma Bridgestone in primo piano), una di Toby Hall (pinza Brembo da corsa), quella di Winston Chen (officina Nissan con le auto in primo piano), quella di Osmany Leyva (cerchio con logo).

## Foto e grafiche del sito attuale in `originali/`

Scaricate da https://www.bazzato.it il 19/10/2026, più la foto della sede dalla scheda Eurorepar (https://www.eurorepar.it/riparatore-bazzato-snc-di-bazzato-andrea-e-paolo-vigonovo-11669.html). Molte sono materiale stampa Opel, grafiche del fornitore QParts o biglietti di terzi: i diritti vanno chiariti (vedi `_prova/inventario-immagini.json`). Il PNG da 10 MB del vano motore è stato convertito in JPEG di qualità 90 per spazio.

## Uso nel prototipo A della home (`_prova/home/a/img/`, script `_prova/script/proto_a_img.py`)

- `disco-*.webp`: Mclean (Unsplash EpT-ZetoKm8), disco e pinza scontornati con GrabCut e bordo ellittico, fondo trasparente, ombra morbida aggiunta, colore smorzato. Modifica sostanziale, sempre segnaposto.
- `officina-*.jpg`, `officina-v-*.jpg`: Razumov (Pexels 33814736), tolti con ritocco (inpaint) le scritte SKODA e SUPERB sul portellone e i marchi WÜRTH e MIRKA sulle attrezzature; ritaglio 2:1 e verticale. Solo come luce di riferimento: va rifatta nell'officina di viale Serenissima.
- `battistrada-*.jpg`: Yvette S (Unsplash tLEUi4OaQmQ), bianco e nero, ritaglio 5:2.

## Uso nel prototipo B della home (`_prova/home/b/`)

Lavorate con `_prova/script/proto_b_img.py` (toni neutri appena freddi, saturazione ridotta). Ritocchi fatti, ammessi dalle licenze Unsplash e Pexels: nella foto di Razumov tolte le scritte SKODA e SUPERB sul portellone, WURTH sull'avvolgitubo e MIRKA sul carrello, con una velatura chiara sul pavimento; nella foto di Masth tolto il marchio sul guanto. Usate anche le bussole di Bélanger in taglio panoramico. Restano segnaposto da sostituire.

## Aggiunte per la versione finale della home (19/10/2026)

Licenze lette il 19/10/2026 sulla pagina di ogni foto; nessuna delle due è già usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md`, anche per autore).

| File | Pagina della foto | Autore | Misura scaricata | Licenza | Note |
|---|---|---|---|---|---|
| `esterne/unsplash-oa68pmfG-qk-hmg-berlina-bianca-studio.jpg` | https://unsplash.com/photos/a-white-car-on-a-white-background-oa68pmfG-qk | Hyundai Motor Group (@hyundaimotorgroup) | 5000x5000 | "Free to use under the Unsplash License" (non Unsplash+) | berlina bianca (Hyundai Sonata) di tre quarti in studio bianco. Segnaposto per l'apertura: va sostituita con una foto vera |
| `esterne/pexels-8986138-podrez-auto-sul-ponte.jpg` | https://www.pexels.com/photo/white-car-in-a-garage-for-check-up-8986138/ | Artem Podrez | 2800x1867 (originale 6240x4160) | "Free", Pexels License | SUV bianco intero sul ponte a due colonne, officina luminosa. Segnaposto |

## Uso nella versione finale (`sito/img/`, script `_prova/script/finale_img.py`)

Versione finale costruita sulla bozza B, "Il ponte" (scelta del committente), il 19/10/2026. Sostituisce la versione costruita prima sulla bozza A: la berlina in studio di Hyundai Motor Group (Unsplash oa68pmfG-qk) resta scaricata in `esterne/` ma non è più usata.

- `officina-*.jpg`, `officina-alta-*.jpg` (apertura): Renee Razumov (Pexels 33814736), Pexels License. Ritocchi: tolte le scritte SKODA e SUPERB sul portellone, WURTH sull'avvolgitubo e MIRKA sul carrello; tolte la scala e le pistole appoggiate al muro a destra dell'auto; ripulito il vano targa; tolto il parafango bianco sfocato in primo piano in basso a sinistra, ricostruendo il pavimento con le piastrelle spostate lungo la prospettiva; gialli smorzati; toni neutri appena freddi, saturazione ridotta, velatura chiara sul pavimento. Taglio largo (2280 px) e verticale per il telefono.
- `ponte-*.jpg`, `ponte-alta-*.jpg`: Artem Podrez (Pexels 8986138), Pexels License. Tolti SUBARU e FORESTER dal portellone e BRIDGESTONE dal fianco della gomma; saturazione ridotta; inquadratura intera 3:2 e taglio quadrato. Il modello resta riconoscibile dalla forma.
- Non più usate nella home: Masth (mani sulla ruota), Mclean (disco), Bélanger (bussole), Yvette S (battistrada), Brunner, Buehner, wal_, Hyundai Motor Group.
- Tutte e due restano segnaposto: in pagina portano l'etichetta "Foto indicativa" e vanno rifatte dal vero (vedi `LEGGIMI.md`).

## Rifinitura della versione finale (19/10/2026, dopo il giudizio cieco)

| File | Pagina della foto | Autore | Misura scaricata | Licenza | Note |
|---|---|---|---|---|---|
| `esterne/pexels-8985667-podrez-auto-intera-sul-ponte.jpg` | https://www.pexels.com/photo/car-on-lift-at-auto-the-repair-shop-8985667/ | Artem Podrez | 4200x2363 (originale 6144x3456) | "Free", Pexels License (letta sulla pagina il 19/10/2026) | SUV bianco intero di fianco sul ponte, officina luminosa; a destra un meccanico, insegne appese col marchio Geely. Segnaposto. Non usata in nessun'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md`; la serie di Podrez compare solo in LavoroESalute tra le foto guardate e scartate, con un altro numero) |

Uso in `sito/img/` (script `_prova/script/finale_img.py`):
- `ponte-*.jpg`, `ponte-alta-*.jpg`: ora Podrez 8985667 al posto di Podrez 8986138. Ritocchi: tolta l'insegna appesa con il marchio e la scritta (al suo posto il soffitto subito a destra), tolta la scritta del modello sulla portiera; bianco riportato al neutro, saturazione ridotta; taglio 3:2 e 5:4 con il meccanico e l'altra insegna fuori dal quadro. La forma dell'auto resta riconoscibile.
- `officina-*.jpg`: stessa foto di Razumov, taglio più stretto (2040 px) e piastrelle grigio scuro schiarite a sinistra del pavimento.
- Podrez 8986138 resta in `esterne/` ma non è più usata.
- Guardate e scartate: Pexels 12185933 (Hyundai Motor Group, auto sul ponte in un'officina scura, marchio e modello sul portellone), 8986033 e 8985514 (Podrez, dettagli con marchi e fumo), 33814733 (marchio BMW in primo piano), 10126656 e 5158101 (scure); Unsplash Hv_gKPOXmwE (KC Shum, officina in disordine, targa leggibile).
