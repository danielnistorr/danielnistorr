# Home finale, Peruzzo Grafiche: "Stampare è un'arte"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, prove e screenshot con `finale_shot.mjs`). Parte dal prototipo A scelto dal giudice; la prima schermata è stata ripensata dentro la stessa direzione.

Screenshot in questa cartella: `home-1440.jpg` (4516 px, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg` (5019 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (chiusura e piede).

## Idea

Il libro finito è l'oggetto del mestiere di Peruzzo: la prima schermata ne mostra uno solo, un cartonato visto dallo spigolo, grande e nitido, posato sulla carta della pagina come su un tavolo di legatoria. La foto è stampata "a un colore", inchiostro su carta: il fondo bianco della foto diventa esattamente il colore della pagina, quindi non c'è un riquadro, c'è solo il libro. Sopra, il titolo preso dal loro Chi siamo, "Stampare è un'arte". Sotto, l'unico gesto della pagina: le tre confezioni del loro modulo preventivi.

Con il nome di un concorrente la pagina non regge: il titolo e le frasi sono le loro (Chi siamo e il poster "La carta stampata è la nostra storia"), le confezioni e le varianti vengono dal loro modulo, gli editori e il disegno con la dedica sono loro, la legatoria è la loro linea Müller Martini e la chiusura è il loro foglio stampato in oro.

## Prime due schermate

- 1440, prima schermata: testata con logo 2022 ricolorato in nero caldo, quattro voci (Confezioni, Editori, Reparti, Contatti) e il telefono. A sinistra "Stampare è un'arte" in Piazzolla a 116 px su due righe; a destra due righe su chi sono (Mestrino, 1989, i quattro reparti, i prodotti) e un solo bottone rosso, "Chiedi un preventivo". Sotto, a tutta larghezza, lo spigolo del cartonato: il cartone della copertina che sporge, il blocco delle pagine, la copertina nera sotto. Il libro entra dal bordo sinistro e occupa circa il 60 % della larghezza; il resto è carta.
- 1440, seconda schermata: la didascalia minuta ("Cartonato, visto dallo spigolo..." a sinistra, "Foto indicativa" a destra), poi "Che confezione vi serve?" con le schede Punto metallico, Brossura, Cartonato; poi "Fumetti, libri e cataloghi d'arte per case editrici di tutta Italia" con i nomi degli editori in serif come un colophon e, accanto alla base dell'elenco, il disegno con la dedica a 200 px con la sua didascalia.
- Dopo: i quattro reparti numerati come sul loro sito (.1 ... .4) con le misure vere, la foto della legatoria a tutta larghezza, la chiusura e il piede.
- 390, prima schermata: titolo a 60 px su due righe, le due righe di presentazione, il bottone, poi il taglio verticale dello spigolo (a fuoco, in alto a destra) con la didascalia. Le schede e la riga della variante con il link seguono subito sotto la foto.

## Caratteri e colori

- Titoli, schede, nomi degli editori, telefono grande: **Piazzolla** 400 e 500 (Huerta Tipográfica), asse ottico a 30 nelle misure grandi. È un serif disegnato per la stampa e per i libri: il registro degli editori d'arte dei riferimenti (TASCHEN, Ofset Yapımevi), non quello di una startup. Niente corsivi.
- Testo, menu, didascalie, dati: **Funnel Sans** 400 e 500 (NORD ID), cifre tabellari per telefono, grammature, P.IVA. Nessuna delle due è nelle liste b della guida né in un'altra home finita della campagna.
- Licenza: tutte e due SIL Open Font License 1.1, si possono ospitare e usare commercialmente. File serviti dalla pagina: `sito/fonts/piazzolla-latin.woff2`, `piazzolla-latin-ext.woff2`, `funnel-sans-latin.woff2`, `funnel-sans-latin-ext.woff2`, scaricati da Google Fonts il 24/10/2026; testi della licenza in `sito/fonts/OFL-Piazzolla.txt` e `OFL-FunnelSans.txt`.
- Colori: carta #F5F1E8 (più calda del #F4F2EE del prototipo, senza arrivare al crema di B), nero caldo #1B1916 (15,6:1), grigio #5A5650 per il testo secondario (6,5:1), schede non scelte #6E6A63 (4,8:1), filetti #D6D0C4. Il rosso Peruzzo #FF2A13 solo sul filetto della scheda scelta; il bottone e i numeri dei reparti in #C41D0A (5,3:1 sulla carta, testo bianco sopra 5,95:1).
- Riferimenti: TASCHEN per il libro come unico oggetto su un fondo pieno; Graphicom per il libro a filo del bordo; Corraini per la prima schermata chiara con il titolo grande; Ofset Yapımevi per la tipografia che parla come un editore.

## Interazione

Un solo gesto: tre schede (`role="tablist"`) con le opzioni vere del modulo preventivi. Punto metallico (a punto sella o a punto omega), Brossura (fresata o cucita, copertina al vivo o con le alette), Cartonato (fresato o cucito, con il risguardo o autorisguardato). Clic, frecce, Home e Fine cambiano la riga della variante e il link al preventivo, che porta a `preventivi.html?confezione=...`: nel sito nuovo il modulo deve aprirsi già impostato su quella confezione. Cambio netto, senza dissolvenze; al passaggio cambia solo il colore. Niente animazioni allo scorrere, niente effetti sul cursore.

Le schede non cambiano la foto, ed è voluto: non ho trovato su Unsplash e Pexels un punto metallico e una brossura con la stessa luce, lo stesso fondo e la stessa inquadratura del cartonato (le prove con un quaderno pinzato e un tascabile aperto erano più deboli e diverse). Quando arriveranno le tre foto di still life chieste nel LEGGIMI, ogni scheda potrà mostrare la sua.

Altro: link "Vai al contenuto" come primo elemento della tastiera; sotto i 900 px il menu è un bottone "Menu" con `aria-expanded` che si chiude con Esc o scegliendo una voce; sotto i 640 px le colonne del piede si aprono a fisarmonica con un vero bottone.

## Foto, origine e licenza

| In pagina | File | Origine | Licenza |
|---|---|---|---|
| Apertura (desktop e telefono) | `apertura-*`, `apertura-tel-*` | Allec Gomes, https://www.pexels.com/photo/corner-of-white-book-in-hardcover-binding-10939170/ (3456x5184), in monocromia | Pexels License, verificata il 24/10/2026; "Foto indicativa" in pagina |
| Dedica | `dedica-400.jpg` | Peruzzo, `2018-05-IMG_8470.jpg` (533x800), vignettatura tolta | dell'azienda, autore del disegno da identificare |
| Legatoria | `legatoria-*` | Peruzzo, `2020-11-IMG_8866.jpg`, Canon EOS 6D, 16/01/2018, schiarita, tolto l'azzurro del neon | dell'azienda |
| Chiusura | `chiusura-*` | Peruzzo, `2018-07-IMG_8364.jpg` (1200x800): foglio stampato in oro a caldo con la frase scritta a mano e il logo | dell'azienda |
| Logo | `logo-peruzzo-grafiche.png` | Peruzzo, `logo-peruzzo-grafiche-bianco-2022-686x165.png` ricolorato | dell'azienda |

Regola del trattamento: la sola foto di repertorio è in monocromia, così si fonde con la pagina e si capisce che è un segnaposto; le foto di Peruzzo restano a colori, e la chiusura in oro è l'unico colore caldo della pagina oltre al rosso. La foto della chiusura non compare sopra e non è usata in nessun'altra home della campagna; la foto di repertorio non compare in nessun altro CREDITI.md (controllo per ID e autore). Niente immagini generate.

## Newsletter

Niente newsletter: servirebbe per Peruzzo Editoriale, le Peruzzine e le fiere del fumetto, ma l'ultimo titolo dello shop è del 2018, la pagina News è rotta e peruzzine.com non risponde. Se confermano che l'editoriale è attivo si aggiunge nel piede (campo email, bottone, consenso privacy, collegata a un servizio).

## Controlli

- Altezze: 4516 px a 1440 (tra 4500 e 5000 come chiesto), 5019 a 390, 5068 a 320, 5186 a 768, 4473 a 1024, 4956 a 1920.
- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920; nessuna sovrapposizione negli screenshot guardati a pezzi.
- Schede: clic e tastiera provati (freccia destra da Punto metallico porta a Brossura con il link `?confezione=brossura`; Fine porta a Cartonato). Primo Tab: "Vai al contenuto". Menu a 390: si apre, si chiude con Esc e il fuoco torna sul bottone. Fisarmonica del piede: si apre.
- `segnali.sh` (paragrafo f della guida): 0 soglie bloccanti, 0 da guardare; foto al 36,3 % della pagina, Funnel Sans 85,2 % e Piazzolla 14,8 %, 4 filetti larghi, nessun monospazio, nessuna etichetta maiuscola.
- Contrasti AA (valori sopra). Nessun carattere U+2014 nella pagina, negli script e nei testi (controllato da `build_finale.sh`).
- Divieti del committente: niente gradienti, testo in gradiente, emoji, Inter, card con bordo colorato, vetro, modo scuro, tre box con icona, badge, icone Lucide, comparse allo scorrere, effetti sul cursore, bottoni che sbiadiscono, serif corsivo.
