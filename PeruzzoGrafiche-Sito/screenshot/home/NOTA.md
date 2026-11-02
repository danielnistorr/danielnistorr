# Home finale, Peruzzo Grafiche: "Stampare è un'arte"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, prove e screenshot con `finale_shot.mjs`; misure veloci a più larghezze con `rapido.mjs`). Parte dal prototipo A scelto dal giudice; dopo il giudizio cieco del 24/10/2026 l'apertura è stata rifatta dentro la stessa direzione (sotto, "Cosa è cambiato").

Screenshot in questa cartella: `home-1440.jpg` (4512 px, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5332 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (chiusura e piede).

## Idea

Il libro finito è l'oggetto del mestiere di Peruzzo, e la prima schermata ne mostra uno loro: The Private Eye, un cartonato che hanno stampato per Bao Publishing (dalla pagina Prodotti del loro sito), con la copertina arancio, grande e a colori. Il fondo bianco della foto di prodotto diventa esattamente la carta della pagina, così non c'è un riquadro: c'è il libro posato sul tavolo, con la sua ombra corta. Il titolo preso dal loro Chi siamo, "Stampare è un'arte", si appoggia nel vuoto in alto a sinistra della foto; sotto il titolo, nella stessa schermata, l'unico gesto della pagina: le tre confezioni del loro modulo preventivi.

Con il nome di un concorrente la pagina non regge: il libro in apertura e i tre della sezione editori sono lavori loro, il titolo e le frasi sono loro (Chi siamo e il poster "La carta stampata è la nostra storia"), le confezioni e le varianti vengono dal loro modulo, la legatoria è la loro linea di raccolta e cucitura e la chiusura è il loro foglio stampato in oro.

## Prime due schermate

- 1440, prima schermata: testata con logo 2022 ricolorato in nero caldo, quattro voci (Confezioni, Editori, Reparti, Contatti) e il telefono. A sinistra "Stampare è un'arte" in Piazzolla a 116 px su due righe, due righe su chi sono (Mestrino, 1989, i quattro reparti, i prodotti), poi "Che confezione vi serve?" con le schede Punto metallico, Brossura, Cartonato, la sezione del dorso disegnata, la variante e il bottone rosso "Chiedi un preventivo". A destra, da y 130 a 700, il cartonato arancio di tre quarti: il dorso scende in diagonale verso il basso a sinistra e lascia il posto al titolo, che gli si appoggia accanto. Didascalia: "The Private Eye per Bao Publishing, cartonato."
- 1440, seconda schermata: "Fumetti, libri e cataloghi d'arte per case editrici di tutta Italia", poi tre loro lavori posati sulla stessa carta (Paper Girls 2 per Bao Publishing, Il club delle baby-sitter per Il Castoro, La sposa yemenita aperta per BeccoGiallo) con titolo ed editore sotto, poi i nomi degli editori in serif come un colophon.
- Dopo: i quattro reparti numerati come sul loro sito (.1 ... .4) con le misure vere, la foto della legatoria dentro la griglia, la chiusura e il piede.
- 390, prima schermata: titolo a 60 px su due righe, le due righe di presentazione, il libro a tutta larghezza (taglio stretto) con la didascalia; le schede e il disegno del dorso seguono subito sotto.
- 1024 e 768: titolo, presentazione, libro a tutta larghezza, poi le schede. Tra 1240 e 1380 px il libro si stringe (65vw) per non toccare il titolo.

## Caratteri e colori

- Titoli, schede, nomi degli editori, titoli dei lavori, telefono grande: **Piazzolla** 400 e 500 (Huerta Tipográfica), asse ottico a 30 nelle misure grandi. È un serif disegnato per la stampa e per i libri: il registro degli editori d'arte dei riferimenti (TASCHEN, Ofset Yapımevi), non quello di una startup. Niente corsivi.
- Testo, menu, didascalie, dati, etichette del disegno del dorso: **Funnel Sans** 400 e 500 (NORD ID), cifre tabellari per telefono, grammature, P.IVA. Nessuna delle due è nelle liste b della guida né in un'altra home finita della campagna.
- Licenza: tutte e due SIL Open Font License 1.1, si possono ospitare e usare commercialmente. File serviti dalla pagina: `sito/fonts/piazzolla-latin.woff2`, `piazzolla-latin-ext.woff2`, `funnel-sans-latin.woff2`, `funnel-sans-latin-ext.woff2`, scaricati da Google Fonts il 24/10/2026; testi della licenza in `sito/fonts/OFL-Piazzolla.txt` e `OFL-FunnelSans.txt`.
- Colori: carta #F5F1E8, nero caldo #1B1916 (15,6:1), grigio #5A5650 per il testo secondario e le etichette del disegno (6,5:1), schede non scelte #6E6A63 (4,8:1), filetti #D6D0C4. Il rosso Peruzzo #FF2A13 solo sul filetto della scheda scelta; il bottone e i numeri dei reparti in #C41D0A (5,3:1 sulla carta, testo bianco sopra 5,95:1). Il colore vero arriva dai libri: l'arancio di The Private Eye, il rosa di Paper Girls, il giallo del Club delle baby-sitter, i rossi, blu e ocra della Sposa yemenita, l'oro della chiusura.
- Riferimenti: TASCHEN per il libro come unico oggetto su un fondo pieno; Graphicom per il libro a destra con il titolo a sinistra; Corraini per la prima schermata chiara con il titolo grande; Ofset Yapımevi per la tipografia che parla come un editore.

## Interazione

Un solo gesto, nella prima schermata: tre schede (`role="tablist"`) con le opzioni vere del modulo preventivi. Ogni scheda mostra la sezione del dorso disegnata a tratto nero (300 x 140 px, con tre o quattro etichette: copertina e fogli piegati con il punto nella piega; copertina, blocco e colla sul dorso; cartone, blocco, dorso arrotondato e unghiatura), la variante (a punto sella o a punto omega; fresata o cucita, copertina al vivo o con le alette; fresato o cucito, con il risguardo o autorisguardato) e il bottone "Chiedi un preventivo" che porta a `preventivi.html?confezione=...`: nel sito nuovo il modulo deve aprirsi già impostato su quella confezione. Clic, tocco, frecce, Home e Fine; cambio netto, senza dissolvenze; al passaggio cambia solo il colore. Niente animazioni allo scorrere, niente effetti sul cursore.

La foto del libro non cambia con le schede: tra i loro lavori fotografati non ci sono un punto metallico, una brossura e un cartonato con la stessa luce e la stessa inquadratura, e mescolarli darebbe tre foto diverse a ogni clic. Il disegno del dorso fa il lavoro; quando arriveranno le tre foto di still life chieste nel LEGGIMI, ogni scheda potrà mostrare anche la sua.

Altro: link "Vai al contenuto" come primo elemento della tastiera; sotto i 900 px il menu è un bottone con `aria-expanded` che diventa "Chiudi" quando è aperto e si chiude con Esc o scegliendo una voce; sotto i 640 px le colonne del piede si aprono a fisarmonica con un vero bottone. Bottoni senza l'evidenziazione blu di WebKit al tocco.

## Foto, origine e licenza

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Apertura (desktop e telefono) | `apertura-*`, `apertura-tel-*` | Peruzzo, `2017-11-The-Private-Eye_Bao-Publishing.jpg` (1200x885, pagina Prodotti), fondo portato alla carta della pagina | dell'azienda; copertina di Bao Publishing e degli autori |
| Editori | `lavoro-paper-girls-*`, `lavoro-baby-sitter-*`, `lavoro-sposa-yemenita-*` | Peruzzo, pagina Prodotti (1200 e 900x1200), stesso trattamento | dell'azienda; copertine e tavole degli editori |
| Legatoria | `legatoria-*` | Peruzzo, `2020-11-IMG_8866.jpg`, Canon EOS 6D, 16/01/2018, schiarita, tolto l'azzurro del neon, ritagliata da x 500 (fuori estintore e scatoloni) | dell'azienda |
| Chiusura | `chiusura-*` | Peruzzo, `2018-07-IMG_8364.jpg` (1200x800, ritaglio 1053x800): foglio stampato in oro con frasi scritte a mano e il marchio storico | dell'azienda |
| Logo | `logo-peruzzo-grafiche.png` | Peruzzo, `logo-peruzzo-grafiche-bianco-2022-686x165.png` ricolorato | dell'azienda |

Trattamento, uguale per tutti i libri: `finale_img.py` stima il fondo della foto con una superficie liscia (polinomio di secondo grado sui pixel lontani dal libro), divide e moltiplica per il colore carta. Il fondo diventa #F5F1E8, l'ombra corta resta; per la Sposa yemenita aperta le pagine più chiare del fondo vanno verso il bianco, così il foglio si stacca dalla carta della pagina. Bordi sfumati, nessun riquadro. Le foto restano a colori. Nessuna foto di repertorio in pagina, nessuna immagine generata; nessuna di queste foto è in un'altra home della campagna.

Risoluzione: le foto di prodotto sono a 1200 px. A 1440 il libro dell'apertura è largo circa 1037 px CSS (1,14x), i tre lavori 421 px CSS (2,3x); la legatoria è a 1900 px per 1312 px CSS (1,45x); la chiusura a 1053 px per 676 px CSS (1,56x). Sugli schermi retina l'apertura è un po' morbida: va rifatta con lo still life chiesto nel LEGGIMI.

## Newsletter

Niente newsletter: servirebbe per Peruzzo Editoriale, le Peruzzine e le fiere del fumetto, ma l'ultimo titolo dello shop è del 2018, la pagina News è rotta e peruzzine.com non risponde. Se confermano che l'editoriale è attivo si aggiunge nel piede (campo email, bottone, consenso privacy, collegata a un servizio).

## Cosa è cambiato dopo il giudizio cieco (24/10/2026)

1. **Apertura** (K1, K6, K7): via la foto di repertorio Pexels in monocromia con "Foto indicativa"; al suo posto The Private Eye, un cartonato che Peruzzo ha stampato per Bao, a colori, posato sulla carta. Il libro sale fino all'altezza del titolo (da y 130) e sta a destra quasi a filo del bordo; il titolo si appoggia nel vuoto della foto, un solo blocco. Niente più vuoto sotto il testo di destra: il testo è tutto a sinistra.
2. **Schede delle confezioni** (gesto debole): spostate nella prima schermata, sotto il titolo; ogni scheda cambia il disegno in sezione del dorso, la variante e il bottone del preventivo. La sezione separata sotto la foto non c'è più.
3. **Sezione editori** (colonna destra vuota): tolto il disegno con la dedica (200 px, appoggiato in basso); al suo posto tre loro lavori nello stesso trattamento dell'apertura, in tre colonne uguali, poi l'elenco degli editori. Il disegno può tornare se l'azienda dà il permesso (LEGGIMI).
4. **Chiusura**: foto da 862 a 1053 px di larghezza, mostrata a 676 x 514 px CSS (1,56x); didascalia che dichiara il marchio storico "Peruzzo Industrie Grafiche" sul foglio.
5. **Legatoria**: dentro la griglia (1312 x 560 a 1440), ritagliata senza estintore e scatoloni.
6. **Piede**: sotto i 1240 px il logo prende una riga e le colonne sono quattro da tre colonne di griglia (due per riga sotto i 900 px); l'email ha un punto di a capo dopo la @ e `overflow-wrap:anywhere`. Misurato: bordo destro dell'email 930 su 976 a 1024, 564 su 736 a 768.
7. **Testata**: niente evidenziazione blu al tocco su "Menu" e sulle schede; il bottone dice "Chiudi" quando il menu è aperto.
8. Ritmo verticale un po' più ampio tra le sezioni (160-184 px) per tenere la pagina tra 4500 e 7000 px a 1440 dopo aver tolto la sezione delle schede.

Non cambiato: i social nel piede (Facebook e Instagram). Ho provato a verificare l'ultimo post, ma Instagram risponde 401 ("require_login") e Facebook rimanda al login: non si può vedere da qui. I link sono quelli del sito di oggi; la verifica resta nel LEGGIMI, da fare prima di pubblicare.

## Controlli

- Altezze: 4512 px a 1440 (tra 4500 e 7000), 5332 a 390, 5299 a 320, 5537 a 768, 4886 a 1024, 5003 a 1920.
- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 768, 900, 1024, 1241, 1280, 1366, 1440, 1600, 1920 e 2560; nessun testo oltre il margine (`rapido.mjs`); nessuna sovrapposizione negli screenshot guardati a pezzi (320, 390, 768, 1024, 1280, 1440, 1920).
- Schede, provate con Playwright: all'avvio Cartonato; clic su Punto metallico cambia disegno, variante e link (`?confezione=punto-metallico`); freccia destra porta il fuoco e la scelta su Brossura (`?confezione=brossura`); Fine porta a Cartonato, Home a Punto metallico; a 390 il tocco su Brossura la sceglie. Primo Tab: "Vai al contenuto". Menu a 390: al tocco si apre e dice "Chiudi", con Esc si chiude, il fuoco torna sul bottone e torna "Menu". Fisarmonica del piede: si apre al tocco.
- Collegamenti: `tel:+390499002884`, `tel:+390499002885`, `mailto:info@graficheperuzzo.it`, mappa `https://www.google.com/maps/search/?api=1&query=Peruzzo+Grafiche+Via+Marco+Polo+10+35035+Mestrino`.
- `segnali.sh` (paragrafo f della guida): 0 soglie bloccanti, 0 da guardare; foto al 35,2 % della pagina, Funnel Sans 83 % e Piazzolla 17 %, 4 filetti larghi, nessun monospazio, nessuna etichetta maiuscola, una sola sezione con titolo a sinistra e paragrafo a destra (i reparti).
- Contrasti AA (valori sopra). Nessun carattere U+2014 nella pagina, negli script e nei testi (controllato da `build_finale.sh`).
- Divieti del committente: niente gradienti, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, modo scuro, tre box con icona, badge, icone Lucide, comparse allo scorrere, effetti sul cursore, bottoni che sbiadiscono, serif corsivo. I tre lavori della sezione editori sono foto di libri con titolo ed editore, senza riquadri né icone.
