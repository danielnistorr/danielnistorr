# Innovatex, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`.
Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `home-finale.html`,
misure, prova del gesto, larghezze da 320 a 2560, segnali, screenshot, chiusura con `chiusura.mjs`). Altezza a 1440: 5.224 px.
A 390: 5.344 px.

Base: la bozza A, "La canapina", scelta dal committente. Prima schermata, impianto, trattamento delle foto, carattere e
colori restano quelli della bozza. Ho cambiato l'esecuzione, i dati, il telefono e i dettagli. La versione precedente
in `sito/` partiva dall'idea della "cartella di campionario", che cambiava la prima schermata: l'ho sostituita del tutto.

## L'idea

Innovatex vende ritagli di mestiere: il campione tagliato con le forbici zigzag e il suo cartellino.
In apertura c'è un solo ritaglio di canapina, steso in piano, grande e nitido, appena ruotato, su carta chiara. Si legge la garza.
Tutta la pagina è un campionario. Ogni materiale è un ritaglio con il suo cartellino numerato, il magazzino e il
gesto del collante vanno a tutta larghezza.

## Ultimo passaggio: cosa è cambiato dopo il giudizio cieco

La prima schermata resta quella della bozza scelta dal committente (titolo su tre righe a sinistra, un ritaglio a destra,
cartellino, carta chiara, Hanken Grotesk). Ho corretto l'esecuzione:
- **Il ritaglio è un oggetto coerente.** Prima era un rettangolo tagliato dal drappeggio `A7406712-1`, con le pieghe che
  arrivavano al bordo e lo tagliavano dritte. Ora dentro lo zigzag c'è la macro in piano della stessa canapina
  (`A7406706`): tessuto steso, nessuna piega che il bordo debba seguire, come un campione vero appoggiato sulla carta.
  Taglio al 72 % perché la garza resti più grande del passo dello schermo (niente moiré a 1x), larghezze 400, 560, 720
  e 1080 con srcset. Stessa regola nel campionario: jersey, microfibra base, microfibra suede e tele di cotone passano
  dai drappeggi alle loro macro in piano (`A7406741`, `A7406682`, `A7406688`, `A7406727`).
- **Ombra corta e calda**, da tessuto steso: `rgba(60,45,30,.20)` a 1 px e `.14` a 8/14 px, al posto dell'ombra
  fredda e lunga che lo faceva galleggiare. Stessa tinta sui cartellini e nel campionario.
- **Colore:** misurato con un campione di pixel, il ritaglio di prima aveva già il colore dell'originale (media
  157,169,181 contro 154,165,177 dell'originale nello stesso taglio). Ora la lavorazione è neutra (colore 1,0, contrasto
  +2 %) e la macro in piano è più chiara (163,173,185). L'azzurro grigio è il colore vero della canapina fotografata:
  non l'ho scaldato, sarebbe un falso sul prodotto.
- **Il fatto proprio sale nella prima schermata:** sotto il titolo, in peso 500, "Ordini la mattina, ricevi nel
  pomeriggio." La terza sezione ora si intitola "Tutto disponibile a pronta consegna" (frase del sito).
- **Telefono, apertura:** il ritaglio è largo l'84 % (318 px a 390) e il cartellino è in flusso sotto, a destra: copre
  il 5,5 % del ritaglio (30 px del bordo inferiore, compresa la rotazione). A 320 copre il 7 %.
- **Campionario fino a 900 px:** l'indice è una lista e il campione si apre sotto la voce toccata (prima solo fino a
  600: a 768 l'immagine cambiava fuori dallo schermo). La voce resta sotto il dito (scorrimento compensato: salto 0 px a
  768, 390 e 320). Un secondo tocco, Invio o Spazio sulla voce aperta la chiude.
- **Voci 10 e 11** (puntali e contrafforti, schiuma di lattice e gel): ora sono bottoni come gli altri, con il loro
  cartellino e le frasi del sito. Non c'è lo scatto: su computer resta il posto del campione, una cornice tratteggiata;
  sul telefono si apre solo il cartellino. Tolto "Campione su richiesta".
- **Contrasti:** numeri dell'indice e dei cartellini in #5C5E59 (5,76:1). Il grigio #A6A7A1 non c'è più.
- **Testi:** tolte la riga "Campioni" della tabella (resta la nota sotto l'indice), "Tutto disponibile a pronta
  consegna." come riga a sé, e la frase senza fonte "Oggi gli scaffali servono calzaturifici e pelletterie". La riga
  "Collanti" della tabella, che ripeteva il cartellino 12, diventa "Marchi: Distributori dei prodotti Mastek e
  Intercom." e il cartellino 12 porta la base (solvente o acqua). "Dodici materiali, tutti a magazzino" diventa
  "Dodici materiali". I contatti si intitolano "Contatti", a 64 px.
- **Mani col collante:** arancio dello sfondo meno saturo del 32 % e bianchi un poco più caldi, come lo scaffale.

## La chiusura: l'etichetta del rotolo pronto alla spedizione

Il committente ha notato che quasi tutte le home della campagna finivano uguali: titolo, telefono gigante su una fascia,
tre o quattro colonnine con indirizzo, email e orari, piede scuro a quattro colonne. Anche qui c'erano le quattro
colonne uguali e il piede a quattro blocchi con il logo. Ho rifatto solo la chiusura, il resto della pagina non cambia.

**L'idea.** La pagina è un campionario: ogni materiale ha il suo cartellino. Il passo dopo il campione è il rotolo che
parte dal magazzino, e il rotolo porta un'etichetta. I recapiti sono scritti su quella etichetta, un solo oggetto:
carta #FBFAF7 con gli angoli tondi della fustella, ruotata di 0,8 gradi (0,5 sul telefono) con la stessa ombra corta e
calda dei cartellini, e dentro il modulo stampato a filetti d'inchiostro da 1 px. I campi dell'etichetta (articolo,
metri, lotto) diventano i campi dei recapiti:
- in testa il logo, come il fornitore stampato sull'etichetta;
- **Magazzino** (Via Cristoforo Colombo 24, 30030 Vigonovo (VE), con "Apri in Google Maps") e **Orari** affiancati,
  uno sotto l'altro sul telefono;
- **Telefono** al posto dei metri: è il campo grande, 56 px a 1440, 48 a 1024, 40 a 390, 35 a 320, inchiostro su
  carta chiara. Tutta la cella è il collegamento `tel:` (688 x 120 px a 1440, 334 x 98 a 390, 264 x 93 a 320);
- **Email** a 28 px (20 sul telefono), collegamento `mailto:`;
- in fondo il **codice a barre disegnato**: un Interleaved 2 of 5 vero del numero di telefono (0495021268, SVG
  nascosto ai lettori di schermo), e accanto "Pronta consegna", come il timbro del magazzino.
A sinistra, accanto all'etichetta, "Contatti" a 64 px e la frase del sito "Ordini la mattina, ricevi nel pomeriggio."
a 24 px: è la promessa che l'etichetta mantiene. Nessun dato nuovo: sono tutti quelli che la pagina aveva già.

**Il piede** è una riga sola sulla stessa carta, sotto un filetto: Innovatex S.r.l. con la sede legale di Cittadella,
P.IVA e C.F., REA, capitale sociale, PEC e Privacy, in 13 px grigio #5C5E59 (5,76:1 sulla carta). A 1440 sta in una
riga; a 1024 e 768 va su due, sul telefono scorre a capo come un testo. Il logo del piede non c'è più (è sull'etichetta).

**Tolto:** le quattro colonnine uguali dei contatti con i titoletti, il piede a quattro blocchi (logo più tre colonne)
sulla carta più scura #E7E4DC. Non c'era e non c'è un telefono gigante su fascia scura.

**Controlli della chiusura** (`_prova/script/chiusura.mjs`, nel build): a 1440, 1024, 768, 390 e 320 nessuna cella
dell'etichetta si sovrappone a un'altra o trabocca, nessuno scorrimento orizzontale (anche sulle 26 larghezze di
`larghezze.mjs`). Contrasti: inchiostro su etichetta 16,4:1, grigio dei campi su etichetta 6,3:1, grigio del piede
sulla carta 5,8:1. Guardata a pezzi a tutte e cinque le larghezze (`_prova/tmp-finale/chiusura/`); la chiusura a 1440
è in `screenshot/home/chiusura-1440.jpg`. Le maiuscole piccole dei campi sono i nomi dei campi di un modulo, non
etichette sopra un titolo (segnali: 0).

## Le prime due schermate

1. Testata chiara: logo vero (ricolorato nel verde #0F4621), quattro voci e il telefono. Titolo su tre righe,
   "Rinforzi e collanti / per calzatura / e pelletteria", a 104 px. A destra il ritaglio di canapina (520 px,
   ruotato di 2,5 gradi, ombra corta). Tra "collanti" e il ritaglio restano 53 px d'aria, misurati: il titolo non
   tocca più il tessuto. Il cartellino è un foglietto di carta (bordo sottile, ombra di 1 e 6 px, ruotato di 1
   grado), non più un riquadro con l'ombra larga. Porta il nome, il numero del campionario "07", la frase del sito e
   "Variante GRS". Sotto il titolo, una riga ("Microfibre, tele, canapina, salpa, espansi e collanti, a magazzino a
   Vigonovo."), un solo bottone verde "Chiama 049 502 1268" e l'orario.
   Sotto il titolo, la riga dei materiali e, in peso 500, "Ordini la mattina, ricevi nel pomeriggio."
   A 390: titolo a 46 px su tre righe, ritaglio largo l'84 % (318 x 413) e cartellino in flusso sotto, a destra.
   Seguono la riga, il bottone e l'orario, subito dopo la prima schermata (il numero è anche in testata).
2. "Dodici materiali, tutti a magazzino". A sinistra il ritaglio del materiale scelto, con il cartellino:
   nome, numero, frase del sito e le versioni in cifre tabellari a 14 px ("Densità 21, 50, HD"; "Versioni semplice,
   adesivo, termoadesivo, soluzionato"; "Variante riciclata GRS/RCS"). A destra l'indice dei dodici nomi a 34 px,
   numerati da 01 a 12 come il numero del cartellino. Puntali e contrafforti e schiuma di lattice e gel hanno il
   cartellino ma non lo scatto: resta il posto del campione, tratteggiato.

Poi: "Tutto disponibile a pronta consegna" a 84 px sopra lo scaffale a tutta larghezza e una tabella di due righe
(in produzione, marchi); le mani col collante sul sottopiede a tutta larghezza; la storia, con il titolo a sinistra e
il testo a destra alla stessa altezza; "Contatti" sull'etichetta del rotolo; il piede in una riga.

## Cosa era già cambiato rispetto alla bozza A

- Titolo a 104 px con gli a capo fissati: 53 px d'aria dal ritaglio (prima la "ti" entrava nella garza).
- Cartellino da riquadro con ombra a foglietto di carta numerato, con le versioni (la grammatica del cartellino del
  rotolo della bozza B, senza codici, senza "lana di vetro", senza pastiglie sulle foto).
- La frase della prima schermata non ripete più il titolo della terza sezione.
- La frase della B "Ordini la mattina, ricevi nel pomeriggio" (ora nella prima schermata). In pagina non c'è "entro
  24 ore".
- L'orario compare due volte (accanto al bottone e nei contatti), non più tre: tolta la riga "Orari" dalla tabella.
- Storia: niente più metà sinistra vuota. Il titolo torna vicino alla frase vera: "Il primo ordine arrivò prima dei
  prodotti".
- Contatti: tolta "Vigonovo, nella Riviera del Brenta". La Riviera del Brenta veniva dal sito di un'altra azienda.
- Scaffale: dall'originale a piena risoluzione, stretto sui due ripiani centrali, i più chiari, con i neri sollevati.
- Moltoprene, nylon, microfibra base e tela blu: ombre sollevate, perché la trama si legga.
- A 1024 il titolo scende a 70 px e il ritaglio a 370 px (63 px d'aria). A 320 il cartellino perde la frase e tiene
  nome e variante.
- Link "Privacy" alla pagina vera del sito (innovatexgreen.com/privacy-policy/).

## Caratteri e colori

- Hanken Grotesk (Google Fonts, SIL Open Font License 1.1: `sito/fonts/OFL-Hanken-Grotesk.txt`), una sola famiglia,
  file variabile 300-600 servito dalla pagina (`sito/fonts/hanken-latin.woff2`). Titoli 400 a 104, 84, 64 e 56 px
  con spaziatura da -0,03 a -0,045 em, testo 400 a 18 px, cartellini 500. Cifre tabellari per telefono, orari,
  densità, numeri dell'indice e P.IVA. È la scelta c1 della guida (riferimento WEIMA: "solo con un titolo davvero
  grande"). Il tono "fornitore della moda che non fa moda" viene da Eurojersey (un tessuto e un indice di nomi) e da
  Carvico (titolo enorme in grottesco).
- Carta #F2F0EB, inchiostro #1A1C19, grigio #5C5E59 (testo piccolo e numeri), nomi non scelti #7A7C76 (solo a 26-34
  px), filetti #D6D3CB, cartellino ed etichetta #FBFAF7, ombre in un bruno caldo rgba(60,45,30). Verde del marchio #0F4621 solo nel logo e nel bottone. Il colore vero lo
  danno i materiali.

## Interazione (un solo gesto)

Il campionario. Su computer (sopra 900 px), passando, toccando o arrivando con Tab su un nome cambiano di colpo, senza
dissolvenza, il ritaglio e il cartellino. Fino a 900 px (tablet e telefono) è una lista: toccando un nome, il ritaglio
si apre sotto quel nome e la voce resta ferma sotto il dito; un secondo tocco la chiude. I nomi sono bottoni veri con
`aria-expanded`, e il banco ha `aria-live`. Provato con `prova_gesto.mjs`: a 1440 passaggio su "Salpa" e "Puntali", Tab
e Maiusc+Tab (anche sulle voci 10 e 11), clic su "Moltoprene"; a 768, 390 e 320 tocchi su "Collanti", "Salpa",
"Lattice" e due volte "Salpa" (salto della voce 0 px, il banco parte subito sotto la voce, dentro la finestra), Invio e
Spazio a 768; sempre senza scorrimento orizzontale.
Le transizioni (0,12-0,15 s) toccano solo il colore di ciò che si tocca. Niente animazioni allo scorrere, niente
effetti sul cursore, niente opacità al passaggio.

## Foto: origine e licenza

Tutte dal servizio fotografico di Innovatex del 3/2/2026 (Sony ILCE-7M4, EXIF), pubblicato sul loro sito
(`assets/originali/`; lo scaffale dall'originale a piena risoluzione in `_prova/crawl/piena/`). Nessuna foto di
repertorio, nessuna immagine esterna, nessuna immagine generata. Lavorate con PIL (`finale_img.py`) con lo stesso
tono su tutte (colore 0,88-0,98, contrasto +4 %, ombre sollevate dove servono). Il bordo zigzag è cotto nell'immagine
(WebP con trasparenza). Due o tre larghezze con srcset, tagli quadrati per il telefono.
- Apertura e campionario 07: canapina in piano `A7406706`.
- Campionario, tutte macro in piano: jersey `A7406741`, drill `A7406714`, microfibra base `A7406682`, microfibra
  suede `A7406688`, moltoprene `A7406669`, tela blu notte `A7406727`, salpa `A7406765`, nylon `A7406758`; collanti
  `A7406392` (foto dritta, senza zigzag).
- Pronta consegna: scaffale `A7406827-2`, due ripiani centrali.
- Chi siamo: mani col collante sul sottopiede `A7406469-1`, arancio dello sfondo attenuato e bianchi scaldati.
Le foto da rifare dal vero e come sono nel `LEGGIMI.md`.

## Le ispirazioni del committente (Graziella, N19): quanto le ho usate

Poco, circa un terzo (come scritto in `01-analisi.md`), e solo nella struttura, come nella bozza. Innovatex è un distributore tecnico B2B di rinforzi e
collanti, non un marchio di moda o di lusso: i suoi clienti lavorano per la moda, ma la pagina deve parlare come un
magazzino che conosce i materiali. Ho preso il fondo chiaro e il grottesco molto grande (N19) e un solo oggetto vero,
grande e nitido, accanto al titolo (Graziella). Ho lasciato fuori il nero, il corsivo, il menu a tutta pagina, le
comparse, il suono e il verde acido. Il registro è quello del fornitore: nomi, versioni, densità, orari.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti su 10. Area foto 36,1 %, una sola famiglia, nessun carattere vietato, nessun
  titolo col punto, una sola sezione con titolo a sinistra e testo a destra. Una voce "da guardare": l'indice
  numerato da 01 a 12. Lo tengo perché non è una finta procedura: è il numero di campionario che ogni cartellino porta
  ("07" sulla canapina in apertura).
- Misure (`misura_finale.mjs`): il cartellino non copre mai il testo; copre l'8,5 % del ritaglio a 1440 e 1920, il
  15 % a 1024, il 7,3 % a 768, il 5,5 % a 390, il 7 % a 320. Aria titolo-ritaglio: 53 px a 1440 e 1920, 63 px a 1024.
- `larghezze.mjs`: scrollWidth uguale a innerWidth su 26 larghezze da 320 a 2560. Collegamenti: `tel:+390495021268`
  (testata, apertura, contatti), `mailto:info@innovatexgreen.com`, Google Maps su Via Cristoforo Colombo 24 30030
  Vigonovo VE, privacy del sito.
- Guardate a pezzi le pagine intere a 1440 e 390, le prime schermate a 1920, 1024, 768 e 320 e il campionario aperto
  a 1440 (puntali), 768 (collanti) e 390 (lattice): nessuna sovrapposizione, nessun vuoto non voluto.
- Il testo dei cartellini va a capo senza parole sole in fondo (`text-wrap: pretty`): "nappe / e vitelli." invece di "vitelli." da solo.
- Nessun U+2014 nella pagina, nella nota e nel LEGGIMI (controllo nello script). Nessuna nota di lavorazione a vista.
  Nessun dato fuori da `01-analisi.md`.
- Divieti del committente: nessun gradiente, nessun badge, nessuna icona, nessun box con icona, nessun corsivo, nessuna
  dissolvenza allo scorrere, nessun effetto sul cursore, niente Inter.
