# Innovatex, home finale: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`.
Tutto si rifà con `bash _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `home-finale.html`,
misure, prova del gesto, segnali, screenshot). Altezza a 1440: 5.278 px. A 390: 5.394 px.

Base: la bozza A, "La canapina", scelta dal committente. Prima schermata, impianto, trattamento delle foto, carattere e
colori restano quelli della bozza. Ho cambiato l'esecuzione, i dati, il telefono e i dettagli. La versione precedente
in `sito/` partiva dall'idea della "cartella di campionario", che cambiava la prima schermata: l'ho sostituita del tutto.

## L'idea

Innovatex vende ritagli di mestiere: il campione tagliato con le forbici zigzag e il suo cartellino.
In apertura c'è un solo ritaglio di canapina, grande e nitido, appena ruotato, su carta chiara. Al 100 % si legge la garza.
Tutta la pagina è un campionario. Ogni materiale è un ritaglio con il suo cartellino numerato, il magazzino e il
gesto del collante vanno a tutta larghezza.

## Le prime due schermate

1. Testata chiara: logo vero (ricolorato nel verde #0F4621), quattro voci e il telefono. Titolo su tre righe,
   "Rinforzi e collanti / per calzatura / e pelletteria", a 104 px. A destra il ritaglio di canapina (520 px,
   ruotato di 2,5 gradi, ombra corta). Tra "collanti" e il ritaglio restano 53 px d'aria, misurati: il titolo non
   tocca più il tessuto. Il cartellino è un foglietto di carta (bordo sottile, ombra di 1 e 6 px, ruotato di 1
   grado), non più un riquadro con l'ombra larga. Porta il nome, il numero del campionario "07", la frase del sito e
   "Variante GRS". Sotto il titolo, una riga ("Microfibre, tele, canapina, salpa, espansi e collanti, a magazzino a
   Vigonovo."), un solo bottone verde "Chiama 049 502 1268" e l'orario.
   A 390: titolo a 46 px su tre righe e ritaglio a destra (250 x 325) con il cartellino che sporge a sinistra. Seguono
   la riga, il bottone e l'orario, interi dentro i 844 px (il fondo dell'orario è a 751 px).
2. "Dodici materiali, tutti a magazzino". A sinistra il ritaglio del materiale scelto, con il cartellino:
   nome, numero, frase del sito e le versioni in cifre tabellari a 14 px ("Densità 21, 50, HD"; "Versioni semplice,
   adesivo, termoadesivo, soluzionato"; "Variante riciclata GRS/RCS"). A destra l'indice dei dodici nomi a 34 px,
   numerati da 01 a 12 come il numero del cartellino. Puntali e contrafforti e schiuma di lattice e gel sono in grigio
   con "Campione su richiesta", senza un riquadro vuoto.

Poi: "Ordini la mattina, ricevi nel pomeriggio" a 84 px sopra lo scaffale a tutta larghezza; "Tutto disponibile a
pronta consegna." in testa a una tabella di tre righe (campioni, in produzione, collanti); le mani col collante sul
sottopiede a tutta larghezza; la storia, con il titolo a sinistra e il testo a destra alla stessa altezza; "Ordini e
campioni" con magazzino, telefono, email e orari; il piede con i dati societari.

## Cosa è cambiato rispetto alla bozza A

- Titolo a 104 px con gli a capo fissati: 53 px d'aria dal ritaglio (prima la "ti" entrava nella garza).
- Cartellino da riquadro con ombra a foglietto di carta numerato, con le versioni (la grammatica del cartellino del
  rotolo della bozza B, senza codici, senza "lana di vetro", senza pastiglie sulle foto).
- La frase della prima schermata non ripete più il titolo della terza sezione.
- Titolo della pronta consegna più corto, preso dalla B: "Ordini la mattina, ricevi nel pomeriggio". In pagina non
  c'è "entro 24 ore".
- L'orario compare due volte (accanto al bottone e nei contatti), non più tre: tolta la riga "Orari" dalla tabella.
- "Tutto disponibile a pronta consegna." non resta più orfano a sinistra: è in testa alla tabella, su una riga.
- Storia: niente più metà sinistra vuota. Il titolo torna vicino alla frase vera: "Il primo ordine arrivò prima dei
  prodotti".
- Contatti: "Vigonovo, nella Riviera del Brenta" diventa "Ordini e campioni". La Riviera del Brenta veniva dal sito di
  un'altra azienda.
- Scaffale: dall'originale a piena risoluzione, stretto sui due ripiani centrali, i più chiari, con i neri sollevati.
- Moltoprene, nylon, microfibra base e tela blu: ombre sollevate, perché la trama si legga.
- Piede su carta più scura #E7E4DC con l'inchiostro, invece del nero: la pagina resta tutta luce.
- A 390 il bottone e l'orario entrano interi nella prima schermata. A 1024 il titolo scende a 70 px e il ritaglio a
  370 px (63 px d'aria). A 320 il cartellino perde la frase e tiene nome e variante.
- Link "Privacy" alla pagina vera del sito (innovatexgreen.com/privacy-policy/).

## Caratteri e colori

- Hanken Grotesk (Google Fonts, SIL Open Font License 1.1: `sito/fonts/OFL-Hanken-Grotesk.txt`), una sola famiglia,
  file variabile 300-600 servito dalla pagina (`sito/fonts/hanken-latin.woff2`). Titoli 400 a 104, 84, 64, 56 e 96 px
  con spaziatura da -0,03 a -0,045 em, testo 400 a 18 px, cartellini 500. Cifre tabellari per telefono, orari,
  densità, numeri dell'indice e P.IVA. È la scelta c1 della guida (riferimento WEIMA: "solo con un titolo davvero
  grande"). Il tono "fornitore della moda che non fa moda" viene da Eurojersey (un tessuto e un indice di nomi) e da
  Carvico (titolo enorme in grottesco).
- Carta #F2F0EB, inchiostro #1A1C19, grigio #5C5E59, nomi non scelti #7A7C76, voci senza campione #A6A7A1, filetti
  #D6D3CB, cartellino #FBFAF7, piede #E7E4DC. Verde del marchio #0F4621 solo nel logo e nel bottone. Il colore vero lo
  danno i materiali.

## Interazione (un solo gesto)

Il campionario. Su computer, passando, toccando o arrivando con Tab su un nome cambiano di colpo, senza dissolvenza,
il ritaglio e il cartellino. Su telefono è una lista: toccando un nome, il ritaglio si apre sotto quel nome. I nomi
sono bottoni veri con `aria-expanded`, e il banco ha `aria-live`. Provato con `prova_gesto.mjs`: passaggio su
"Salpa", Tab e Maiusc+Tab, clic su "Moltoprene", tocco su "Collanti" a 390, sempre senza scorrimento orizzontale.
Le transizioni (0,12-0,15 s) toccano solo il colore di ciò che si tocca. Niente animazioni allo scorrere, niente
effetti sul cursore, niente opacità al passaggio.

## Foto: origine e licenza

Tutte dal servizio fotografico di Innovatex del 3/2/2026 (Sony ILCE-7M4, EXIF), pubblicato sul loro sito
(`assets/originali/`; lo scaffale dall'originale a piena risoluzione in `_prova/crawl/piena/`). Nessuna foto di
repertorio, nessuna immagine esterna, nessuna immagine generata. Lavorate con PIL (`finale_img.py`) con lo stesso
tono su tutte (colore 0,88-0,98, contrasto +4 %, ombre sollevate dove servono). Il bordo zigzag è cotto nell'immagine
(WebP con trasparenza). Due o tre larghezze con srcset, tagli quadrati per il telefono.
- Apertura: canapina in drappeggio `A7406712-1` (voto 8/6).
- Campionario: jersey `A7406749`, drill `A7406714`, microfibra base `A7406685`, microfibra suede `A7406702-1`,
  moltoprene `A7406669`, tela blu notte `A7406736`, canapina in piano `A7406706`, salpa `A7406765`, nylon `A7406758`,
  collanti `A7406392`.
- Pronta consegna: scaffale `A7406827-2`, due ripiani centrali.
- Chi siamo: mani col collante sul sottopiede `A7406469-1`.
Le foto da rifare dal vero e come sono nel `LEGGIMI.md`.

## Le ispirazioni del committente (Graziella, N19): quanto le ho usate

Poco, circa un quinto, e solo nella struttura, come nella bozza. Innovatex è un distributore tecnico B2B di rinforzi e
collanti, non un marchio di moda o di lusso: i suoi clienti lavorano per la moda, ma la pagina deve parlare come un
magazzino che conosce i materiali. Ho preso il fondo chiaro e il grottesco molto grande (N19) e un solo oggetto vero,
grande e nitido, accanto al titolo (Graziella). Ho lasciato fuori il nero, il corsivo, il menu a tutta pagina, le
comparse, il suono e il verde acido. Il registro è quello del fornitore: nomi, versioni, densità, orari.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti su 10. Area foto 35,4 %, una sola famiglia, nessun carattere vietato, nessun
  titolo col punto, una sola sezione con titolo a sinistra e testo a destra. Una voce "da guardare": l'indice
  numerato da 01 a 12. Lo tengo perché non è una finta procedura: è il numero di campionario che ogni cartellino porta
  ("07" sulla canapina in apertura).
- Misure (`misura_finale.mjs`): nessuno scorrimento orizzontale a 1920, 1440, 1024, 768, 390 e 320. Il cartellino
  non copre mai il testo. Aria titolo-ritaglio: 53 px a 1440 e 1920, 63 px a 1024.
- Guardate a pezzi le pagine intere a 1440 e 390 e le prime schermate a 1920, 1024, 768 e 320: nessuna sovrapposizione,
  nessun vuoto non voluto.
- A 320 x 640 il bottone entra intero, ma l'orario finisce sotto il bordo.
- Nessun U+2014 nella pagina, nella nota e nel LEGGIMI (controllo nello script). Nessuna nota di lavorazione a vista.
  Nessun dato fuori da `01-analisi.md`.
- Divieti del committente: nessun gradiente, nessun badge, nessuna icona, nessun box con icona, nessun corsivo, nessuna
  dissolvenza allo scorrere, nessun effetto sul cursore, niente Inter.
