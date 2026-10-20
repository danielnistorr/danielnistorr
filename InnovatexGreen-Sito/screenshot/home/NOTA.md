# Innovatex, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`.
Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `home-finale.html`,
misure, prova del gesto, larghezze da 320 a 2560, segnali, screenshot, chiusura con `chiusura.mjs`). Altezza a 1440: 5.621 px.
A 390: 5.318 px.

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
  "Dodici materiali". La chiusura non si intitola più "Contatti": vedi sotto.
- **Mani col collante:** arancio dello sfondo meno saturo del 32 % e bianchi un poco più caldi, come lo scaffale.

## La chiusura: la frase del sito, i recapiti, la corsia del magazzino (stile B, "con foto")

Storia. Le chiusure di tutte le home della campagna erano uguali (titolo di luogo, telefono gigante su fascia, colonnine,
piede a quattro colonne). Le avevo rifatte come un oggetto del mestiere disegnato che porta i recapiti: qui l'etichetta
del rotolo pronto alla spedizione, con il codice a barre. Il committente le ha bocciate. Fra i due campioni mostrati su
Hambro e Bazzato (`../Hambro-Sito/_prova/chiusure-campioni/` e `../Bazzato-Sito/_prova/chiusure-campioni/`) ha scelto
lo stile B, "con foto". Ho rifatto solo la chiusura in quello stile; il resto della pagina non cambia.

**Com'è fatta** (testo sopra, foto a tutta larghezza sotto, come il campione di Bazzato):
- **La frase**, grande nel carattere dei titoli (Hanken Grotesk 400, 66 px a 1440, 47 a 1024, 40 a 768, 38 a 390,
  34 a 320, spaziatura -0,035 em, a capo bilanciati): "Ordini la mattina, ricevi il materiale nel pomeriggio." È la
  frase della home del sito, intera ("Tutto disponibile a pronta consegna: ordini la mattina, ricevi il materiale nel
  pomeriggio", `01-analisi.md`); in apertura c'è nella forma breve. È il punto forte che dichiarano e dice come lavorano.
  Fa da titolo della sezione (`#contatti`, il menu ci porta ancora). Non c'è più la parola "Contatti".
- **I recapiti**, a destra della frase su computer e sotto da 900 px in giù, in quattro righe di testo: il telefono
  049 502 1268 in peso 500 (36 px a 1440, 28 a 1024 e 768, 32 a 390, 30 a 320, `tel:+390495021268`), l'email
  (`mailto:info@innovatexgreen.com`), l'indirizzo Via Cristoforo Colombo 24, 30030 Vigonovo (VE) che è esso stesso il
  collegamento a Google Maps, e l'orario "Lunedì-venerdì, 8:30-12:30 e 14:30-18:30" (gli orari non si spezzano).
  Niente riquadri, filetti, campi in maiuscolo, logo o codice a barre.
- **La foto**: la corsia del magazzino con il carrello elevatore fra gli scaffali di rotoli su pallet, a tutta larghezza
  (2:1 su computer, 1440 x 720 a 1440; quadrata sul telefono, centrata sul carrello), con la didascalia della pagina
  sotto: "Una corsia del magazzino, febbraio 2026". È l'immagine che la frase promette: il materiale che parte.
  Sopra la chiusura c'è la storia, aperta dalle mani col collante: foto diversa, nessuno spostamento necessario.
- **Il piede** resta una riga sulla stessa carta, sotto un filetto: Innovatex S.r.l. con la sede legale di Cittadella,
  P.IVA e C.F., REA, capitale sociale, PEC e Privacy, in 13 px grigio #5C5E59. A 1440 sta in una riga, a 1024 e 768 su
  due, sul telefono va a capo come un testo.

**La foto: origine, licenza, lavorazione.** `A7406863` (`assets/originali/A7406863-scaled.jpg`, 2560 x 1707), dal
servizio fotografico di Innovatex pubblicato sul loro sito (Sony ILCE-7M4; EXIF della copia sul sito 11/2/2026 12:12, come
la canapina e il collante). È una loro foto, non repertorio: nessuna licenza esterna, nessun file di `assets/esterne`.
In `01-analisi.md` aveva 7 su 5 ("scura e grandangolare"); a tutta larghezza in fondo funziona, ed è la più nitida
delle foto non ancora in pagina (le forme nelle gabbie forse sono di un cliente, la latta Mastek è su nero con marchi di
terzi). Lavorata in `finale_img.py` con lo stesso tono dello scaffale (colore 0,9, luce +5 %, neri sollevati) e la luce
rossa di sicurezza del carrello meno satura del 30 %, come l'arancio delle forme nella banda delle mani. File:
`magazzino-900/1440/2200.jpg` e `magazzino-tel-480/900.jpg`. Nella foto c'è una persona al volante: va chiesto a
Innovatex se va bene in home (è già sul loro sito).

**Tolto:** l'etichetta del rotolo (modulo a filetti, campi in maiuscolo, logo, codice a barre, "Pronta consegna"),
il titolo "Contatti", la frase a 24 px accanto.

**Controlli della chiusura** (`_prova/script/chiusura.mjs`, nel build), a 1440, 1024, 768, 390 e 320: la frase e i
recapiti non si sovrappongono, nessuna riga dei recapiti trabocca, la foto è caricata e larga quanto la finestra,
nessuno scorrimento orizzontale (anche sulle 26 larghezze da 320 a 2560 di `larghezze.mjs`). Collegamenti: tel:,
mailto:, Google Maps, privacy. Contrasti sulla carta #F2F0EB: inchiostro 15,1:1, grigio della didascalia e del piede
5,8:1. Guardata a pezzi a tutte e cinque le larghezze (`_prova/tmp-finale/chiusura/`); la chiusura a 1440 è in
`screenshot/home/chiusura-1440.jpg`.

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
il testo a destra alla stessa altezza; la chiusura con la frase "Ordini la mattina, ricevi il materiale nel pomeriggio.",
i recapiti e la corsia del magazzino a tutta larghezza; il piede in una riga.

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
  px), filetti #D6D3CB, cartellino #FBFAF7, ombre in un bruno caldo rgba(60,45,30). Verde del marchio #0F4621 solo nel logo e nel bottone. Il colore vero lo
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
- Chiusura: corsia del magazzino con il carrello elevatore `A7406863`, tono dello scaffale, luce rossa attenuata.
Le foto da rifare dal vero e come sono nel `LEGGIMI.md`.

## Le ispirazioni del committente (Graziella, N19): quanto le ho usate

Poco, circa un terzo (come scritto in `01-analisi.md`), e solo nella struttura, come nella bozza. Innovatex è un distributore tecnico B2B di rinforzi e
collanti, non un marchio di moda o di lusso: i suoi clienti lavorano per la moda, ma la pagina deve parlare come un
magazzino che conosce i materiali. Ho preso il fondo chiaro e il grottesco molto grande (N19) e un solo oggetto vero,
grande e nitido, accanto al titolo (Graziella). Ho lasciato fuori il nero, il corsivo, il menu a tutta pagina, le
comparse, il suono e il verde acido. Il registro è quello del fornitore: nomi, versioni, densità, orari.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti su 10. Area foto 46,7 % (con la corsia del magazzino in chiusura), una sola famiglia, nessun carattere vietato, nessun
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
