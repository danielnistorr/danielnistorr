# Home finale Argenteria Varotto Alfredo, "Luce d'argento"

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/` (WebP in più larghezze), caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `pagina.html`, screenshot, misure con `finale_misura.mjs`, prova del selettore con `finale_gesto.mjs`).

## Idea

Carta fredda e un solo pezzo d'argento vero, grande e nitido. Sotto il pezzo, la prova che ha solo Varotto: i tre punzoni (925 e 800, stella 364 PD, VAROTTO ALFREDO in corsivo), ridisegnati in blu notte dalle GIF del loro sito, con la loro frase "tutti perfettamente riconoscibili a occhio nudo e impressi sull'oggetto". Con il nome di Greggio o di Zaramella la prima schermata non regge, perché la stella 364 PD è il punzone di Varotto.

## Le prime due schermate

- 1440: testata con il logo vero, cinque voci, telefono e Shop online. Titolo "Fabbrica d'argenteria / dal 1974" in Boska 124 px; a destra tre righe su cosa fanno, il bottone blu "Chiama 049 870 07 09" e l'email. Sotto, il vassoio Sheffield inciso dello shop largo 1210 px, intero sopra i 900 px. In fondo, su una riga a filo del margine sinistro, i tre punzoni alti 28 px con la frase; a destra, su una riga, la didascalia "Vassoio Sheffield a godrons con incisione floreale. Dal nostro shop.". Restano 64 px d'aria prima del bordo. Niente legende numerate e niente "Tav. 1".
- Seconda schermata a 1440: "Lavorato a mano, tutto a Padova" con la storia di Alfredo Varotto in due paragrafi ("seguiamo ogni richiesta particolare del cliente", parole loro), poi l'elenco vero della produzione in Boska 38 px e per chi lavorano.
- 390: titolo su tre righe, testo, bottone, email; il vassoio tagliato più grande (incisione e manico destro, a filo dei bordi); i quattro punzoni su una riga, la frase e la didascalia. Tutto dentro 844 px.
- Poi: titoli e punzoni (foto a filo sinistro alta quanto la colonna, didascalia 24 px sotto, selettore a destra), i cinque marchi con l'alzata vera alta quanto l'elenco, la riparazione (foto a filo sinistro, testo a destra, materiali come parole), la chiusura "b con foto", il piede chiaro.
- Altezze: 6037 px a 1440 piede compreso; 7230 a 390; 7321 a 320; 7807 a 768; 5506 a 1024; 6352 a 1920.

## Caratteri e colori

- Titoli, numeri e telefono: **Boska** (Fontshare, Indian Type Foundry, ITF Free Font License 2.0, uso commerciale gratuito, `sito/fonts/FFL.txt`). Serif dritta ad alto contrasto: richiama il titolo in serif nera su bianco di Puiforcat e il maiuscolo con grazie di "ARGENTERIA" nel loro logo. Cifre allineate e tabellari (`lnum tnum`) per 1974, 925, 364 PD, le categorie e il telefono. Nessun corsivo d'accento.
- Testo, menu, didascalie, piede: **Rethink Sans** (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL-RethinkSans.txt`). Il suo corsivo compare solo nel punzone VAROTTO ALFREDO, che sul loro sito è corsivo.
- Colori: carta #F4F3F0, carta del piede #ECEBE7, inchiostro #17181B, grigio #55595F (5,9:1 sul piede, AA), filo #D4D5D6, blu notte #13294B (dal blu del marchio #00265a) solo per bottoni e punzoni. Neri delle foto mai sotto #2A2C30.
- Riferimenti: Puiforcat (un gruppo di pezzi d'argento con tanto vuoto, serif nera), Christofle (posate su carta chiara), Georg Jensen (luce), Greggio come confronto diretto del distretto padovano. Della famiglia delle home amate dal committente: Agnoletto chiaro e Hambro (un oggetto vero grande su carta, titolo sicuro, tanta aria), senza riprenderne le legende numerate e la "Tav.".

## Interazione

Un solo gesto: il selettore "925 / 800 / Sheffield / Alpacca" (ruolo tablist, frecce, Home e Fine, tocco). Cambia di netto la foto, il nome grande, la riga che spiega il metallo, la didascalia e il numero nel punzone del titolo; su Sheffield e alpacca la nota dice che i punzoni sono quelli dell'argento 925 e 800. L'altezza della sezione non cambia tra le schede (645 px a 1440, provato con `finale_gesto.mjs`). Le etichette sotto i punzoni sono le loro: "Garanzia del titolo legale", "Identità del produttore", "Marchio originale". Transizioni di 0,15 s solo su bottoni e schede; nessuna animazione allo scorrere, nessun effetto sul cursore. Il menu del telefono si apre con un vero bottone.

## Foto, origine e licenza

| Dove | Foto | Origine e licenza |
|---|---|---|
| Apertura | Vassoio rettangolare Sheffield, godrons, incisione floreale | shop varottoshop.com, `assets/originali/shop/5bc4dd90ffe48e0d7e8b7e69.jpg`, materiale dell'azienda (diritti da confermare) |
| Selettore 925 | Coppa su stelo in argento | Unsplash, Stephanie Harvey, `_srndYorq1s`, Unsplash License |
| Selettore 800 | Cucchiaio liscio in argento | Unsplash, Anna Kumpan, `sL1E3sUxcAs`, Unsplash License (aggiunta in questo giro) |
| Selettore Sheffield | Salsiera su vassoio a godrons | Unsplash, Deleece Cook, `QQkf_GZFwVA`, Unsplash License |
| Selettore alpacca | Tre forchette con le ombre | Unsplash, Abhishek Tewari, `g1wGg1U483s`, Unsplash License |
| Marchi | Alzata per torta argentata | shop, `5d68f02bffe48ef84b8b458f.jpg`, materiale dell'azienda |
| Riparazione | Mano con fresa da lucidatura | Unsplash, Tahlia Doyle, `bfk68pL0EJ0`, Unsplash License; tagliata a destra per togliere il bracciale dell'orologio, neri alzati a #2A2C30 |
| Chiusura | Due forchette incrociate | Unsplash, Ben Lodge, `1jowiwnmFKE`, Unsplash License |

Tutte desaturate in un argento freddo con lo stesso trattamento (`finale_img.py`); gli scontornati hanno il fondo portato al colore carta, così stanno sulla pagina senza riquadro. Le foto Unsplash hanno la didascalia "Foto indicativa". La sfera di Liao è tolta. Nessuna foto è generata dall'IA, nessuna compare nei CREDITI delle altre home della campagna. Dettagli in `assets/CREDITI.md`.

## Piede

Sotto la chiusura, sul colore #ECEBE7: logo vero (PNG originale, contenuto 75x96 mostrato a 48 px, cioè un 2x pieno; il vettoriale va chiesto) con il nome "Argenteria Varotto Alfredo" in Boska 22 px e una riga su chi sono; newsletter (ha senso: esiste già sul sito di oggi, promette nuovi articoli e promozioni, hanno privati e collezioni) con email, bottone, scelta Italiano o English e casella del consenso; quattro colonne Azienda, Collezioni, Servizi, Contatti con Facebook e Pinterest come parole ("I profili dello shop Varottostore"); riga legale con Varotto & Co. di Varotto Luca, indirizzo, P.IVA 04724430287, Privacy, Cookie, English. "Fiere" è tolta finché la pagina è vuota; Instagram è fuori finché non è verificato. A 390 le colonne si impilano una per volta nell'ordine.

## Controlli

- `segnali.sh` a 1440: 17 soglie su 18 OK. Resta la soglia 1, area foto 26,4 % contro 35 %: è voluta. La ricetta del committente chiede un solo oggetto vero e poche sezioni pulite, e l'azienda non ha foto grandi del laboratorio; la sezione "Lavorato a mano, tutto a Padova" è solo testo e nel sito vero prenderà la foto del laboratorio a tutta larghezza (servizio fotografico nel LEGGIMI), che porta l'area sopra il 35 %. Aggiungere oggi un'altra foto di repertorio avrebbe tolto forza al pezzo vero.
- Fatti: tutti da `01-analisi.md` (1974 dalla testata "Since 1974", storia, produzione, punzoni, marchi e numeri delle categorie dal sito di oggi, riparazione dalla pagina Assistenza, recapiti e P.IVA dal piede e dai contatti). Nessun orario (non pubblicati), nessun "Dal 1974 in Corso Stati Uniti".
- Nessuno scorrimento orizzontale e nessun testo sovrapposto a 320, 390, 768, 1024, 1440, 1920 (`finale_misura.mjs`); screenshot guardati a pezzi a tutte le larghezze.
- Nessun U+2014 in pagina, script, NOTA, LEGGIMI e CREDITI. Apostrofi tipografici in pagina.
- Divieti: niente gradienti, glassmorphism, Inter, Lucide, badge, card, dissolvenze, hover che sbiadisce, etichette maiuscole sopra i titoli, frecce scritte; un solo titolo a sinistra con paragrafo a destra.
- Contrasti: grigio #55595F 6,3:1 sulla carta e 5,9:1 sul piede; segnaposto del campo #62666C 4,8:1; bianco sul blu notte 14:1.
