# Bottega dell'Arte, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, screenshot con `scatti_finale.cjs`, controllo dei segnali). Altezza a 1440: 4818 px compreso il piede; a 390: 5601 px.

Base: il prototipo A, "Prima e dopo", scelto dal giudice, con la prima schermata ripensata (il K0 era 6,5) e gli innesti da B (porte del Bo, maniglione in chiusura, piede impilato, carattere in locale).

## L'idea

Il portone d'ingresso che hanno restaurato, raddrizzato e scontornato, sta in piedi nella prima schermata come in una stanza: muro di calce sopra, pavimento appena più scuro sotto, e la riga del pavimento passa esattamente al piede della porta. Sotto la porta, sul pavimento, due bottoni Prima / Dopo scambiano di netto le due foto vere dello stesso portone, e la riga di stato dice cosa è stato fatto con le parole della loro scheda. È il restauro mostrato, non raccontato: con il nome di un concorrente la pagina non regge, perché servono le due foto del loro portone.

## Le prime due schermate

- **1440, prima schermata.** A sinistra il titolo con la loro frase di bottega, "L'arte di lavorare il legno come nel passato" (Zodiak 92 px, tre righe), e una riga su chi sono. A destra il portone alto circa 670 px, con sopra solo il titoletto "Restauro di un portone d'ingresso" allineato al suo bordo sinistro e due legende corte (filo di 72 px): "Ferramenta nuova" a sinistra sul maniglione, "Tre mani di vernice all'acqua" a destra. Sul pavimento, sulla stessa riga, il bottone "Chiama 049 900 4916" con l'email a sinistra e i bottoni Prima / Dopo larghi 288 px centrati sull'asse della porta a destra; sotto, la riga di stato in inchiostro a 16 px. Lo stato iniziale è Dopo.
- **Rispetto al prototipo:** niente più bottoni in alto attaccati al menu, tre legende diventate due e divise ai due lati (non più la fila a destra di Agnoletto), la riga del pavimento che dà scala al pezzo, ombra dipinta corta e posata a terra invece dell'alone. Nello stato Prima resta una legenda sola, "Ferramenta consumata dal tempo", sui fori della ferramenta tolta; la riga dice "Prima: la ferramenta consumata dagli agenti atmosferici e dal tempo." Tolte le legende inventate ("Vernice vecchia, scurita", "Il fondo segnato dal tempo").
- **1440, seconda schermata.** "Su misura, in stile o moderni" e tre lavori veri in 4:5 con la stessa resa: il sottoscala stretto sulla nicchia in ottone, la porta a bilico senza il letto e il cantiere, le porte a vetri piombati senza prese e interruttori. Una riga per lavoro e il link alla pagina.
- **Poi:** le porte scorrevoli del Palazzo del Bo a filo del bordo sinistro (704 px) con "Legno vecchio, della stessa essenza", gommalacca e la riga sul Bo e Gio Ponti; i due soci in una frase di quattro righe e le finiture scritte come parole; la chiusura; il piede.
- **390.** Titolo in tre righe, il portone a sinistra con titoletto e legende a destra, poi sul pavimento i bottoni Prima / Dopo a tutta larghezza, la riga di stato, il bottone del telefono e l'email: tutto dentro i primi 844 px (controllato anche a 320 x 640, dove il telefono resta sotto la piega di pochi pixel). I lavori: il primo a tutta larghezza, gli altri due affiancati.
- **Chiusura "b con foto".** "Vi aspettiamo nella nostra bottega" (dalla loro pagina Azienda), il telefono grande con tel:, i cellulari di Mauro e Giuliano, l'email con mailto:, l'indirizzo con "apri la mappa"; a destra, a filo del bordo, il maniglione in ottone sulla venatura (592 x 569 px), tagliato senza le finestre del capannone, con la didascalia della loro scheda. Niente orari: non sono pubblicati. Il capannone con il furgone è uscito dalla home.
- **Piede.** Fascia #ECE8DF (lo stesso tono del pavimento della prima schermata), niente ombra. Logo vero PNG a 2x largo 260 px con una riga su chi sono; colonne Lavorazioni, Bottega, Contatti su una griglia a 12 colonne; titoletti a 14 px, voci a 15 px con interlinea 2, sottolineatura e cambio di colore pieno al passaggio; l'indirizzo porta alla mappa. In fondo ragione sociale, sede legale, P.IVA, Privacy, Cookie e "Torna su". A 390 le colonne si impilano in ordine.
- **Niente Seguici:** non hanno social. **Niente newsletter:** il sito è fermo al 2021 e non hanno novità, fiere, cataloghi o collezioni da comunicare; il privato compra un armadio o un restauro ogni tanti anni.

## Caratteri e colori, con i riferimenti

- **Zodiak** 400 in tondo (Indian Type Foundry, Fontshare, ITF Free Font License, uso commerciale gratuito) per titoli, frase dei soci, finiture e telefono della chiusura; mai il corsivo. È una serif contrastata che sta accanto alla firma calligrafica del logo senza imitarla; riferimento Bottega Ghianda (serif d'ebanisteria con un solo mobile in apertura) e deVOL (registro domestico). Nota: Zodiak compare anche nelle home di BCM Enologia e Bordin Garden; il giudice ha chiesto di tenerlo.
- **Schibsted Grotesk** 400 e 500 (Google Fonts, SIL Open Font License 1.1) per testi, menu, legende, bottoni e piede, con cifre tabellari solo sui numeri di telefono (sulle frasi con punti e virgole le cifre tabellari allargano la punteggiatura). Sostituisce General Sans, che era già nella home di Bazzato. Tutti e due serviti dalla pagina in `sito/fonts/`, licenze in `sito/fonts/LICENZE.txt` e `OFL-Schibsted-Grotesk.txt`.
- **Colori:** calce #F4F2EC (muro), pavimento #ECE8DF (prima schermata e piede), inchiostro noce #2A2119 (14,1:1 sulla calce, 12,9:1 sul pavimento), grigio #5F574F per i testi secondari (6,3:1 e 5,8:1), un solo accento, il marrone del logo #6F3219 (8,7:1), sul bottone del telefono e al passaggio sui link. Contrasto AA ovunque.

## Interazione

Un solo gesto: i bottoni Prima / Dopo sotto il portone. `aria-pressed`, frecce sinistra e destra per passare dall'uno all'altro, riga con `aria-live`, bersagli alti 52 px. Lo scambio è netto, senza dissolvenza; l'unica transizione (0,12 s) è il colore del bottone toccato. Il menu a 900 px e meno si apre con un vero bottone (`aria-expanded`, Esc lo chiude). Nessuna animazione allo scorrimento, niente che segue il cursore, nessun hover con opacità.

## Foto: origine e licenza

Tutte dell'azienda, dalla libreria media del sito bottegadellartesnc.it (scaricate il 24/10/2026, `assets/originali/`), lavorate con PIL (`_prova/script/finale_img.py`: bilanciamento caldo sul muro o comune, stessa esposizione, contrasto 1,04 e saturazione 0,90 per tutte) ed esportate in WebP a più larghezze con srcset:
- portone dopo `2020-10_Port-3.jpeg` e prima `2020-10_Port.4.jpeg` (scheda `/progetti/portone-dingresso/`), raddrizzati sullo stesso rettangolo 600 x 1840, scontornati, con ombra corta di contatto;
- sottoscala `2020-05_Bottega_dell_Arte_Armadiature-1.jpeg`; porta a bilico `2020-06_porte-a-bilico-2-scaled.jpg`; porte piombate `2020-06_porte_restaurate-n1.jpg` (sensore sul muro coperto con il colore del muro);
- Palazzo del Bo `2020-06_universita08.jpg` (700 x 500; per gli schermi densi c'è una copia ingrandita 1,5x, morbida);
- maniglione `2020-10_Port1.jpg`; logo `logo-bottega-arte-1014.png`; icona `logo-monogramma-B-512.png`.

Nessun segnaposto esterno, nessuna foto di repertorio, nessuna immagine generata. Le foto da rifare sono nel LEGGIMI.

## Controlli

- Screenshot guardati a pezzi a 1440 e 390 interi, prime schermate a 320, 390, 768, 1024, 1440, 1920, stato Prima a 1440 e 390, menu aperto a 390: nessuno scorrimento orizzontale (larghezza del documento uguale alla finestra a tutte le misure), nessuna sovrapposizione visibile. Lo script segnala solo che la scatola del titolo e la legenda "Ferramenta nuova" si toccano: è il riquadro del blocco, i glifi restano a 48 px di distanza.
- Nessun U+2014 nella pagina, nella nota e nel LEGGIMI.
- `segnali.sh` a 1440: 17 soglie su 18 a posto (nessun carattere della lista b, mono 0 %, 0 etichette, 0 frecce, 3 filetti, 2 fasce di fondo, nessun divieto). Resta sotto soglia l'area foto, 22 %: la prima schermata è un pezzo scontornato su fondo chiaro, come chiede la ricetta del committente, e la soglia del 35 % torna solo con foto nuove e più grandi dei lavori. "Contenuto datato": nessuna data in pagina, perché l'anno 2004 e i "40 anni" sono da confermare; i nomi ci sono (Mauro Nosarini, Giuliano Saibene, Palazzo del Bo, Gio Ponti).
- A occhio: niente corsivo, niente badge, niente tre box con icona, niente card, niente gradienti, niente icone.
