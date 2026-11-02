# Home finale Argenteria Varotto Alfredo, "Luce d'argento"

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/` (WebP in più larghezze, i pezzi dello shop con il canale alfa), caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py` e `alfa.py`, pagina da `pagina.html`, screenshot, misure con `finale_misura.mjs`, prova del selettore con `finale_gesto.mjs`).

## Idea

Il banco di posa dell'argentiere. In alto una parete chiara, sotto il piano su cui si appoggia l'argento: il titolo "Fabbrica d'argenteria dal 1974" sta in piedi sull'orizzonte (la linea di base delle lettere è il bordo tra parete e piano, le discendenti di "g" scendono nel piano), e il vassoio inciso è disteso sul piano con la sua ombra vera. La chiusura rimonta lo stesso banco: l'alzata per torta sta in piedi davanti all'orizzonte, il titolo della chiusura appoggiato sulla stessa linea. In mezzo, il piano continua sotto tutte le sezioni.

## Cosa è cambiato in questo passaggio (2 novembre)

Richiesta del committente: "fai più roba di alta gamma, meno uguali tra loro".

1. **Niente legende numerate**: nella pagina non ci sono pallini con filetto né "Tav.", solo una didascalia sobria sotto il vassoio.
2. **Colore dal mestiere**: il fondo non è più la carta #F4F3F0. È il blu del marchio Varotto (#00265a, il blu del loro sito e del marchio corsivo VAROTTO ALFREDO impresso sui pezzi) molto diluito: parete #F3F5F8, piano #E2E8EF, piede #D6DEE7. La ragione si vede: l'argento è uno specchio e prende il colore di ciò che ha intorno; i pezzi scontornati prendono metà del riflesso del piano, e i bottoni e i punzoni sono nello stesso blu, pieno (#13294B).
3. **Una scelta d'impaginazione che non c'è nelle altre home** (confronto con `_invio/zona/home/copertine-est-grisignano.jpg` e le prime schermate di Hambro, Agnoletto, FM Sistemi, Tek.Lam): la prima schermata è divisa in parete e piano da un orizzonte, e il titolo usa quell'orizzonte come linea di base (Boska con interlinea 0,71, cioè ascendente meno discendente: il fondo della riga coincide con la linea di base). Nelle altre home il titolo galleggia su un fondo unico e l'oggetto sta in un riquadro o scontornato sullo stesso fondo; qui l'oggetto è appoggiato su un piano diverso dal muro, con l'ombra che cade sul piano.
4. **Pezzi scontornati con l'alfa** (`_prova/script/alfa.py`): il fondo bianco delle foto dello shop è tolto riempiendo dal bordo, i buchi delle anse sono tolti con due semi, e l'ombra grigia originale della foto diventa un'ombra semitrasparente. Il vassoio, il sottopiatto e l'alzata stanno sul colore della pagina senza riquadro e senza rettangolo visibile.
5. **Chiusura**: era testo a sinistra e alzata su un fondo da studio a destra. Ora l'alzata scontornata, larga 660 px a 1440, sta in piedi davanti all'orizzonte della chiusura; il titolo "Soddisfiamo ogni tipo di richiesta particolare" è appoggiato sulla stessa linea, telefono e recapiti sul piano. È la variante "testo a sinistra e foto a destra", con il pezzo vero al posto di una foto rettangolare; non arriva al bordo perché è un oggetto in piedi su un piano, non una foto.

## Difetti del giudice cieco: stato

Il passaggio del 24 ottobre ne aveva già chiusi quasi tutti; verificati e completati oggi.

- Bloccante 1 (vassoio placcato accanto ai punzoni dell'argento): risolto con la strada B. In prima schermata non ci sono più punzoni disegnati; la didascalia dice "Vassoio in Sheffield, metallo argentato". Il 364 PD resta solo come parola nel testo su ciò che producono in 925 e 800.
- Bloccante 2 (composizione come FM Sistemi e Hambro): niente più testo e bottone in alto a destra, niente riga di etichette sul fondo; ora c'è il banco di posa descritto sopra. Non ho messo i tre punzoni grandi accanto al titolo come proponeva il giudice: accanto a un vassoio placcato contraddirebbero il bloccante 1. Torneranno in apertura con la foto di un pezzo loro in 925 (LEGGIMI, foto 1 e 2).
- Sheffield e alpacca nel selettore: i punzoni si spengono (restano nello spazio, invisibili, così l'altezza non cambia) e al loro posto c'è "Non è argento massiccio: non porta il titolo legale né il punzone 364 PD". Provato con `finale_gesto.mjs`: altezza della sezione 764 px a 1440 e 1093 a 390 su tutte e quattro le schede.
- Coppa ossidata con la candela: sostituita dal calice sbalzato di Michele Wales.
- Forchette d'acciaio in chiusura: sostituite dall'alzata vera dello shop. Nei Marchi c'è il sottopiatto con bordo barocco dello shop.
- Mano con la fresa e dominante blu: sostituita da mani alla pulitrice di Isaac Burke, grigio neutro (R, G, B medi 120, 123, 126 dopo la mappatura sul piano), luminanza media 48 %.
- Logo illeggibile in testata: accanto al segno c'è il nome "Varotto Alfredo" in Boska 22 px.
- "I tre punzoni" con quattro segni: non più in prima schermata; nel selettore i segni sono tre (titolo, stella 364 PD, marchio).
- Titolo "Lavorato a mano, tutto a Padova": ora "L'argento, lavorato a mano a Padova".
- Linee di posate legate al 925: ora su una riga a parte, "Linee di posate: ...".
- Tablet a 768: due colonne da 700 px in su per Titoli, Marchi e Riparazione; altezza 5778 px (era 7807).
- Menu del telefono: sei voci, con "Shop online".
- `sizes` dell'alzata e del vassoio corretti; l'originale del vassoio ad almeno 2500 px è chiesto nel LEGGIMI.
- Preload del font con errore CORS da file://: tolto.

## Le prime due schermate

- 1440: testata sulla parete (logo, nome, cinque voci, telefono, Shop online). Titolo Boska 116 px su una riga, linea di base sull'orizzonte a 226 px. Sul piano: vassoio largo 1160 px, la didascalia a destra, poi il testo su cosa fanno a sinistra e "Chiama 049 870 07 09" con l'email a destra. Tutto entro 830 px.
- 390: titolo su tre righe (Fabbrica / d'argenteria / dal 1974), ultima linea di base sull'orizzonte a 254 px; il vassoio esce dal bordo sinistro e mostra incisione e manico destro; didascalia, testo, bottone, email. Tutto dentro 844 px.
- Poi: "L'argento, lavorato a mano a Padova" con la storia e l'elenco della produzione; titoli e punzoni (foto a filo sinistro, selettore a destra); i cinque marchi con il sottopiatto; la riparazione; la chiusura sul banco di posa; il piede.
- Altezze: 6267 px a 1440 piede compreso; 7409 a 390; 7445 a 320; 5778 a 768; 5584 a 1024; 6653 a 1920; 7261 a 2560.

## Caratteri e colori

- Titoli, numeri e telefono: **Boska** (Fontshare, Indian Type Foundry, ITF Free Font License 2.0, uso commerciale gratuito, `sito/fonts/FFL.txt`). Serif dritta ad alto contrasto: richiama il titolo in serif nera su bianco di Puiforcat e il maiuscolo con grazie di "ARGENTERIA" nel loro logo. Cifre allineate e tabellari (`lnum tnum`). Nessun corsivo d'accento.
- Testo, menu, didascalie, piede: **Rethink Sans** (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL-RethinkSans.txt`). Il corsivo compare solo nel punzone VAROTTO ALFREDO, che sul loro sito è corsivo.
- Colori: parete #F3F5F8, piano #E2E8EF, piede #D6DEE7, inchiostro #15181D, grigio #474D56, filo #C2CBD6, blu notte #13294B solo per bottoni e punzoni. Contrasti: inchiostro 14,4:1 sul piano; grigio 6,9:1 sul piano e 6,3:1 sul piede; segnaposto del campo #555B64 5,0:1 sul piede; bianco sul blu 14,5:1.

## Interazione

Un solo gesto: il selettore "925 / 800 / Sheffield / Alpacca" (ruolo tablist, frecce, Home e Fine, tocco). Cambia di netto foto, nome grande, riga sul metallo, didascalia e numero nel punzone; su Sheffield e alpacca i punzoni si spengono e compare la riga "Non è argento massiccio". Transizioni di 0,15 s solo su bottoni e schede; nessuna animazione allo scorrere, nessun effetto sul cursore. Il menu del telefono si apre con un vero bottone (`aria-expanded`).

## Foto, origine e licenza

| Dove | Foto | Origine e licenza |
|---|---|---|
| Apertura | Vassoio rettangolare Sheffield, godrons, incisione floreale | shop varottoshop.com, `assets/originali/shop/5bc4dd90ffe48e0d7e8b7e69.jpg`, materiale dell'azienda (diritti da confermare) |
| Selettore 925 | Calice in argento sbalzato | Unsplash, Michele Wales, `ncoTigCF7Rc`, Unsplash License |
| Selettore 800 | Cucchiaio liscio in argento | Unsplash, Anna Kumpan, `sL1E3sUxcAs`, Unsplash License |
| Selettore Sheffield | Salsiera su vassoio a godrons | Unsplash, Deleece Cook, `QQkf_GZFwVA`, Unsplash License |
| Selettore alpacca | Tre forchette con le ombre | Unsplash, Abhishek Tewari, `g1wGg1U483s`, Unsplash License |
| Marchi | Sottopiatto con bordo barocco | shop, `5dbd540406e58e80118b456b.jpg`, materiale dell'azienda |
| Riparazione | Mani alla pulitrice | Unsplash, Isaac Burke, `Iih-Q2ZdA6o`, Unsplash License |
| Chiusura | Alzata per torta argentata | shop, `5d68f02bffe48ef84b8b458f.jpg`, materiale dell'azienda |

Tutte in argento neutro con lo stesso trattamento (`finale_img.py`): bianchi delle foto rettangolari portati al colore del piano, neri mai sotto #2C2C2D. Le foto Unsplash hanno la didascalia "Foto indicativa". Nessuna è generata dall'IA e nessuna compare nei CREDITI delle altre home della campagna (controllato per ID). Dettagli in `assets/CREDITI.md`.

## Piede

Sotto la chiusura, sul piede #D6DEE7 con un filo in alto: logo vero (PNG originale, contenuto 75x96 mostrato a 48 px, un 2x pieno; il vettoriale va chiesto) con il nome "Argenteria Varotto Alfredo" in Boska 22 px e una riga su chi sono; newsletter (ha senso: esiste già sul sito di oggi, promette nuovi articoli e promozioni, hanno privati e collezioni) con email, bottone, Italiano o English e casella del consenso; quattro colonne Azienda, Collezioni, Servizi, Contatti, con Facebook e Pinterest come parole ("I profili dello shop Varottostore"); riga legale con Varotto & Co. di Varotto Luca, indirizzo, P.IVA 04724430287, Privacy, Cookie, English. A 390 le colonne si impilano una per volta nell'ordine.

## Controlli (2 novembre)

- `segnali.sh` a 1440: 16 soglie OK, una da guardare, una da correggere. Da correggere: area foto 24,9 % contro 35 %. È voluta: la ricetta chiede un solo oggetto vero, gli scontornati contano solo per la loro sagoma, e la sezione "L'argento, lavorato a mano a Padova" prenderà la foto del laboratorio a tutta larghezza (LEGGIMI, foto 4), che porta l'area sopra il 35 %. Un'altra foto di repertorio oggi toglierebbe forza al vassoio. Da guardare: cinque campi di colore a tutta larghezza; sono la parete e il piano del banco di posa e il piede, cioè l'idea della pagina.
- Nessuno scorrimento orizzontale da 320 a 2560 (320, 360, 390, 560, 700, 768, 900, 1024, 1180, 1280, 1440, 1920, 2560: scrollWidth uguale alla larghezza). Nessun testo sovrapposto (a 768 lo script segnala "area clienti / shop online": sono due link nella stessa frase che vanno a capo, non si toccano). Screenshot guardati a pezzi a 320, 390, 768, 1024, 1440 e 1920.
- Selettore provato con tastiera (tre frecce a destra, Fine, Home) e con il tocco a 390; menu del telefono aperto con il tocco: sei voci, `aria-expanded` vero.
- Collegamenti: `tel:+390498700709` in testata, apertura, riparazione, chiusura e piede; `mailto:` per info@ ed export@; "Apri la mappa" e l'indirizzo del piede vanno a Google Maps con "Corso Stati Uniti 23/A 35127 Padova".
- Fatti: tutti da `01-analisi.md`. Nessun orario (non pubblicati).
- Nessun U+2014 in pagina, script, NOTA, LEGGIMI e CREDITI. Apostrofi tipografici in pagina.
- Divieti: niente gradienti, glassmorphism, Inter, Lucide, badge, card, legende numerate, dissolvenze, hover che sbiadisce, etichette maiuscole sopra i titoli, frecce scritte.
