# Impreservice, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP in più larghezze), caratteri in `sito/fonts/`. Rigenerazione: `bash _prova/script/build_finale.sh` (immagini con `_prova/script/finale_img.py`, controlli, screenshot). Parte dal prototipo A "Il clic" con le indicazioni del giudice e gli innesti da B.

## L'idea

Il prodotto di Impreservice è un oggetto preciso: due bussole e un perno che si agganciano a scatto. La prima schermata lo mostra da solo, grande, in esploso lungo la diagonale, su calcestruzzo chiaro, con tre legende (1 Bussola, 2 Perno, 3 Bussola) e il titolo loro "Sistemi di connessione". Un interruttore Aperto / Agganciato fa scorrere le bussole sul perno: il nome del prodotto, Easy Click, diventa il gesto della pagina. Con il nome di un concorrente la pagina non regge, perché il pezzo, il brevetto e i 42 cantieri sono loro.

## Cosa è cambiato rispetto al prototipo A

- **Prima schermata ripensata (K0 a 7)**: il disegno CAD grigio a contorni neri è diventato un pezzo in luce. Dai disegni dell'azienda ho tolto i contorni (ricostruendo le facce sotto), ammorbidito le facce, portato i grigi in un grigio caldo opaco con i pieni più profondi, lasciato gli spigoli appena accennati, aggiunto un'ombra morbida e un'ombra di contatto sul fondo, e dietro il pezzo una luce appena più chiara del fondo, come un piano di posa in studio. Il pezzo è sceso al 92 % circa: la bussola 3 ora finisce a 1.376 px, sul margine destro. La didascalia "Easy Click Smart" ha la linea di base allineata a quella dei bottoni (misurata: 831 px tutte e due a 1440x900).
- **Bocca della bussola destra**: non è più disegnata a mano. È presa dal disegno vero della bussola (`12-bussola-smart.png`, la vista dall'alto con il foro e il filetto) e portata nella prospettiva dell'assieme con una trasformazione affine (cerchio su cerchio, esatta per il bordo; la profondità del filetto è approssimata). Il resto del pezzo è il disegno originale.
- **Carattere**: Switzer servito in locale aveva ancora gli spazi collassati ("Pontie viadotti", "Tuttii", "quest o anno": lo stesso difetto dal CDN e dai woff2 statici, provato in pagina di test). Passato a Geologica, titoli 300 con spaziatura -0,035em, testo 400, etichette 500.
- **Sezione 2**: al posto dell'operaio in posa, la galleria di metropolitana di Max Mishin, schiarita e desaturata, taglio 2,4:1 a tutta larghezza; la legenda "Giunto tra due conci" cade su un giunto longitudinale vero, controllato ingrandendo la foto. A 390 la legenda si nasconde (nel taglio verticale non c'è un giunto leggibile) e la didascalia dice "Le linee sottili sono i giunti".
- **Chiusura**: lo scudo della fresa sulla culla (Mpikakis) al posto dei tubi in cemento, in 4:3; vuoto tra frase e telefono a 104 px; aggiunta la riga "Tempi di consegna secondo quantità. Per i costi, scriveteci.".
- **Piede**: riga su chi sono di B, YouTube con la piccola icona disegnata, "Fiere e notizie" in Azienda, "Segnalazioni D.Lgs. 24/2023" nella riga legale.

## Le prime due schermate

1. **1440x900**: testata chiara (simbolo vero + nome composto, menu, telefono). "Sistemi di / connessione" a 124 px in alto a sinistra; il connettore attraversa lo schermo dal basso a sinistra all'alto a destra con le tre legende; in basso a destra la frase "Easy Click unisce e allinea i conci prefabbricati delle gallerie scavate con la fresa..." e l'interruttore; in basso a sinistra la didascalia con il brevetto IT 1391815. **390x844**: titolo in due righe con lo spazio tra le parole, il pezzo a tutta larghezza sotto, legende più corte, frase, interruttore a tutta riga, didascalia.
2. "Conci attrezzati con tecnologia Easy Click" (dal titolo del loro video) e la galleria a conci a tutta larghezza con la legenda sul giunto; poi il testo dal comunicato del 2013 e quattro righe di dati (versioni, Smart HD 480 kN, Hybrid L140 passo 5 mm, brevetto con la data).

Poi: "Dal Brennero a Brisbane" con il pozzo dall'alto e tre elenchi corti (Italia 24, Europa 8, Mondo 10, sei voci ciascuno) e "Tutti i 42 cantieri"; "Giunti per ponti e viadotti" con il viadotto; chiusura "Copriamo consegne in tutto il mondo" (frase loro, pagina Prodotti) con telefono, due email, indirizzo, mappa, tempi di consegna, e la foto dello scudo a destra fino al bordo; piede.

Altezze: 6.025 px a 1440, 6.440 px a 390, 5.405 px a 1024, 6.789 px a 1920 (piede compreso).

## Caratteri e colori

- **Geologica** (Monokrom, Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia variabile, servita dalla pagina in `sito/fonts/` (latin e latin-ext, file presi da Google Fonts). Titoli 300, testo 400, etichette e bottoni 500; cifre tabellari (`tabular-nums`) per telefono, kN, mm, codici, P.IVA. Motivo: i riferimenti del mestiere usano grotesk neutre e larghe (Univers da Herrenknecht, Akkurat da Knight Architects); Geologica ha la stessa calma con un disegno proprio, non è Inter e non è in nessuna lista dei caratteri da IA della guida.
- **Colori** (direzione A): calcestruzzo `#ECEAE5` fondo unico di tutta la pagina, luce `#F4F2EE` solo dietro il pezzo, inchiostro `#14171A`, grigio testo `#4F5256` (6,5:1 sul fondo, 7,0:1 sulla luce), blu del logo `#075A9E` (5,9:1) nel simbolo, nei passaggi del mouse e nel fuoco da tastiera. Niente nero pieno, niente fasce colorate: le fasce le fanno le foto.
- Impaginazione: Dissing+Weitling e Knight Architects (foto grandi a filo, poche parole, un colore); la home chiara di Mario Agnoletto amata dal committente (un pezzo vero con le legende) e Hambro (oggetto in luce con l'ombra).

## Interazione

Interruttore Aperto / Agganciato: due bottoni nativi con `aria-pressed`, stato letto da `aria-live`. La pagina si apre in vista aperta; con "Agganciato" le due bussole scorrono in 300 ms lungo l'asse del perno e alla fine compare l'assieme originale; con "Aperto" si separano. Le legende viaggiano con i pezzi. Con `prefers-reduced-motion` il cambio è immediato (verificato: durata 0 s). Provato con Tab, Invio, Spazio e con il tocco a 390. È l'unico gesto della pagina; nessuna animazione allo scorrere, nessun effetto sul cursore. Menu a 390 con vero bottone (`aria-expanded`), piede a fisarmonica con veri bottoni.

## Immagini

| In pagina | Origine | Licenza | Lavorazione |
|---|---|---|---|
| Easy Click Smart (apertura, 4 livelli `ec-*`) | disegni CAD del loro sito: `13-asm-smart.jpg` (assieme), `14-perno-smart.png` (perno), `12-bussola-smart.png` (bocca della bussola) | dell'azienda | ripuliti (tolta la scritta "1858 x 920" e la cornice della finestra CAD), perno allineato, bussole separate lungo l'asse, contorni tolti e facce ricostruite, grigio caldo opaco, ombre; WebP con trasparenza a 1x e 2x |
| Galleria di metropolitana a conci | Max Mishin, Pexels 11424325 | Pexels, gratuita | ombre aperte, desaturata, un filo calda; 2,4:1 e verticale per il telefono; srcset 1200/1800/2400 |
| Pozzo di partenza | Sururi Ballıdağ, Pexels 16227437 | Pexels, gratuita | desaturata; 2,4:1 e verticale |
| Viadotto | Kewal Nagda, Pexels 27808651 | Pexels, gratuita | desaturata; 2:1 e verticale |
| Chiusura, scudo della fresa sulla culla | Evangelos Mpikakis, Unsplash CPI7JAIVaDU | Unsplash License | desaturata; 4:3; srcset 800/1200/1600 |
| Logo | `logo-impreservice-icona-blu-1000.png` del loro sito | dell'azienda | ritagliato, PNG a 160 e 240 px (2x e 3x della misura in pagina) |

Tutte le foto di repertorio sono in `assets/esterne/` con pagina e licenza in `assets/CREDITI.md`; nessuna compare nei CREDITI.md delle altre home della campagna (controllato per identificativo), nessuna è generata dall'IA. La fresa nella foto di chiusura ha macchine di cantiere sullo sfondo, nessun marchio leggibile in primo piano; i costruttori di frese non sono concorrenti di Impreservice. La foto di chiusura non compare altrove nella pagina. Le didascalie non citano la fonte.

## Newsletter

Non c'è. Impreservice vende a imprese di scavo e prefabbricatori, ha due notizie in dieci anni (Viatec 2013, WTC 2022), nessun catalogo da scaricare e nessun cliente privato; il blocco newsletter di oggi con ogni probabilità non è collegato a niente. Meglio il contatto diretto, e la pagina "Fiere e notizie" per fiere e nuovi prodotti.

## Controlli

- Nessuno scorrimento orizzontale a 320, 390, 768, 1024, 1440, 1920 (larghezza del documento uguale alla finestra); nessuna sovrapposizione, guardato a pezzi.
- `segnali.sh` del kit a 1440: 0 soglie da correggere su 10, 0 da guardare su 8 (foto 47,5 % della pagina, una famiglia, niente mono, niente etichette sopra i titoli, 11 filetti larghi). Unica nota: un gradiente, la luce dietro il pezzo, voluto.
- Contrasto AA: testo `#4F5256` 6,5:1, blu 5,9:1, bottone attivo 15:1.
- Nessun U+2014 in pagina, nella NOTA e nel LEGGIMI; nessun segnaposto in pagina.
- Divieti del committente: niente gradienti viola-blu, testo in gradiente, emoji, Inter, card con bordo colorato, glassmorphism, tre box con icona, badge sopra il titolo, icone Lucide, dissolvenze allo scorrere, effetti sul cursore, corsivi d'accento.

## Da confermare (dettagli nel LEGGIMI)

"Una per concio" (lettura del disegno); il rivestimento in materiale composito (fonte del 2013); Smart HD e Hybrid ancora in produzione; la linea ponti ancora attiva; il colore vero del pezzo (nei loro render è nero, qui è il grigio del CAD).
