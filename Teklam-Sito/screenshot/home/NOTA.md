# Tek.Lam, home finale: "Scintilla e spessore"

Versione finale dal prototipo B (`_prova/home/b/`), scelto dal committente. Sostituisce in `sito/` la versione "Il foglio annidato", bocciata (i suoi script sono in `_prova/script/vecchio-foglio/`).
Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh`.
Screenshot: `home-1440.jpg` (intera, 4749 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (intera, 5145 px), `home-390-prima-schermata.jpg`.

## L'idea

L'officina di notte: il fascio attraversa la lamiera e la scintilla si apre, su nero pieno. Subito dopo, lo spessore che quella macchina sa tagliare, disegnato come in una tavola tecnica e in millimetri. Il resto della pagina parla la stessa lingua: sette righe per i sette passi del pezzo, le note numerate dei settori, le misure in cifre tabellari.

## Ultima rifinitura (dopo il giudizio cieco)

- **Prima schermata e sezione dello spessore**: conservate, per scelta del committente. Nello spessore solo difetti di esecuzione: la lamiera ora finisce dentro il margine con il bordo destro disegnato (prima usciva dalla finestra); sotto 1100 px "Ferro, spessore massimo di taglio" sta accanto a "20 mm" e non più all'altro capo della riga; la didascalia non dice più "Scala 1:1" ma "In millimetri ... su un monitor a 96 dpi è spessa quanto il foglio vero".
- **Il percorso del pezzo**, più corto e pulito. Tolta la fascia fotografica di repertorio (360 px senza informazione). I sette passi non sono più sette colonne da 187 px con tre livelli di testo e nomi a capo: sono sette righe accanto al titolo, ognuna con numero, lavorazione, macchina e misura, ognuna su una riga sola. Filetto nero sopra e sotto, filetti chiari tra le righe. Alta 573 px a 1440 (era 899), 930 a 390 (era 1235). Sotto 820 px ogni riga ha il nome sopra e macchina e misura in una frase sotto. I numeri sono in bronzo `#8a5a1c` a 5:1 sul fondo chiaro (prima grigi a 2,6:1).
- **Menu sotto 820 px**: c'era solo il telefono. Ora c'è un bottone "Menu" (`aria-expanded`, `aria-controls`) che apre i quattro link su nero; si chiude con Esc, con un secondo tocco o scegliendo una voce. Il bottone sta prima del menu nel codice, quindi Tab dal bottone aperto entra nei link. Sotto 380 px il telefono esce dalla testata ed entra nel menu. Senza script i link restano visibili in una riga sotto il marchio.
- **Famiglia**: tolto il vuoto di circa 330 × 500 px a sinistra della foto. Titolo a sinistra e storia a destra sulla stessa riga, poi la loro foto a tutta larghezza, didascalia e persone sotto, allineate alla griglia.
- **Contatti**: un velo nero dal basso sotto i recapiti (contrasto del testo bianco misurato pixel per pixel: almeno 7:1 a 390, 1024, 1440 e 1920; il grigio dei dettagli almeno 4,4:1 sul pixel più chiaro, 6,3:1 al 99 %), e la dicitura "Foto indicativa" anche qui, perché è di repertorio.

## Le prime due schermate

1. Nero a tutta larghezza. La foto del taglio laser riempie la finestra, le scintille in alto, la lamiera e il buio in basso. "Lamiera conto terzi" in Sofia Sans 200 a 170 px e, sulla stessa riga a destra, "1978" alla stessa misura, con sotto "la famiglia Volpato in officina, da allora". Un filetto, una riga di testo (cosa fanno, dove) e il link "Fino a che spessore tagliamo". A 390 la foto prende i due terzi alti, stretta sull'ugello, e il titolo sta sul nero sotto, a 68 px.
2. Ancora nero: "Lo spessore, a grandezza vera". A sinistra il Bystronic Byspeed 4400 W, il campo 3000 × 1500 mm e l'interruttore Ferro 20, Inox 15, Alluminio 10; a destra la lettura grande (20 mm) e la lamiera in sezione, tratteggiata a 45 gradi, alta 20, 15 o 10 mm accanto a una scala con una tacca per millimetro.

Poi: il percorso del pezzo su fondo chiaro, sette righe; i settori come una frase sola in grande con sei note; "Dal ferro battuto alla lamiera" con la loro foto vera a tutta larghezza; i contatti col telefono a 160 px sulla foto dell'ugello; il piede con ragione sociale e P.IVA.

## Caratteri e colori

- **Sofia Sans** (Google Fonts, SIL Open Font License 1.1), una famiglia sola: 200 per titoli e numeri grandi, 400 per il testo, 500 e 600 per numeri dei passi, macchine e intestazioni piccole. Servita dalla pagina (`sito/fonts/sofia-latin.woff2`, `sofia-latin-ext.woff2`), licenza in `sito/fonts/OFL-SofiaSans.txt`. Viene dal DIN, la scritta dei disegni tecnici e delle targhe delle macchine; Zahner fa i titoli in un grottesco peso 200 su telaio scuro. Cifre tabellari per misure, numeri dei passi e telefono. Nessun monospazio.
- Colori: nero `#050403` (dal fondo della foto d'apertura), bianco caldo `#f4f1ea`, grigio caldo `#a59e93` sul nero; fondo chiaro `#efece6` con inchiostro `#16130f` e grigio `#625b52`; un solo accento, paglia `#e2b46c`, la prima tinta di rinvenimento dell'acciaio, solo nel gesto e nei link dei contatti, scurita in bronzo `#8a5a1c` per i numeri sul chiaro. Il rosso resta nel logo.
- Riferimenti (`_prova/riferimenti/`): Zahner (telaio scuro, titolo enorme e leggero), De Castelli (il metallo protagonista, poche parole), Bystronic (il pezzo davanti a tutto: qui la sezione in millimetri), Laserhub (le promesse misurabili in riga, qui le misure dei passi).

## Interazione

Un gesto solo, quello approvato: l'interruttore Ferro, Inox, Alluminio (`role="radiogroup"`, frecce, Home e Fine, fuoco visibile, bottoni da 48 px, 76 px al telefono). Cambia la lettura, il nome del metallo, il tratteggio e l'altezza della sezione, con una transizione di 0,22 s solo sulla sezione. Provato con `_prova/script/finale_prova.mjs`: clic su Inox 15 mm (56,7 px), freccia destra Alluminio 10 mm, Home Ferro 20 mm, Fine Alluminio; tocco a 390 su Inox, 15. Il menu sotto 820 px è provato con `_prova/script/rifinitura_prova.mjs`: tocco a 390 (si apre, "Settori" porta a #settori e chiude), Invio, Tab ed Esc a 768. Il percorso non ha interazione: si legge e basta. Nessuna animazione allo scorrere, nessun effetto sul cursore. Il millimetro del CSS è vero solo a 96 dpi: la didascalia lo dice.

## Foto: origine e licenza

| In pagina | File in `sito/img/` | Origine | Licenza |
|---|---|---|---|
| Apertura | `apertura-*`, `apertura-v-*` | Le Trung, Unsplash, https://unsplash.com/photos/fBCQz7OUUww; tagliata sotto per togliere la firma | Unsplash License |
| Famiglia | `officina-*` | `2020-08-slide1.jpg` di teklam.it (saldatura TIG sul cassone inox col film stampato), panoramica, monocromo caldo | di Tek.Lam, uso da confermare |
| Contatti (fondo) | `contatti-*`, `contatti-m-800` | Cemrecan Yurtman, Unsplash, https://unsplash.com/photos/qk2i7n39-B0; tolto il marchio del costruttore stampato sull'ugello | Unsplash License |
| Logo | `logo-segno.png`, `logo-scritta-chiara.png` | ritagli del PNG verticale del loro sito | di Tek.Lam |

Trattamento unico, da `_prova/script/finale_img.py`: neri caldi chiusi, luci color paglia, blu e verdi spenti, grana leggera; la foto vera di Tek.Lam in monocromo caldo. Ogni foto in tre o quattro larghezze con srcset, JPEG. Le due foto di repertorio portano "Foto indicativa" in pagina; nessuna ritrae Tek.Lam o le sue macchine; nessuna immagine generata dall'IA; nessuna foto nuova scaricata (elenco completo in `assets/CREDITI.md`). Uscita nell'ultima rifinitura: la piegatrice di Yurtman (`w7w4T9M0TXg`) sopra il percorso.

## Controlli

- `segnali.sh` a 1440: 0 soglie bloccanti. Foto 47,1 % dell'area, una famiglia (Sofia Sans 100 %), 0 monospazio, 0 frecce, 0 etichette maiuscole, 0 titoli col punto, H2 di tre misure (78, 72, 17 px), 3 fasce di fondo, 20 filetti larghi (erano 12: sono i filetti tra le righe del percorso), un numero grande con etichetta (20 mm), date con nome (1978, 2020). Da guardare, con la ragione: la numerazione 01-07 è l'ordine vero in cui il pezzo attraversa l'officina, dal file al camion. Le sette righe del percorso hanno l'aspetto di una tabella: la guida ammette una tabella in home dove il dato è il prodotto, e qui il prodotto di un terzista sono le macchine e le loro misure.
- Altezze per sezione (`_prova/script/finale_misure.mjs`), a 1440: apertura 900, spessore 691, percorso 573, settori 654, famiglia 1086, contatti 704, piede 142. A 390: 819, 986, 930, 733, 704, 733, 242.
- `rifinitura_prova.mjs`: scrollWidth uguale a innerWidth a 320, 360, 390, 414, 640, 641, 768, 820, 821, 1024, 1100, 1180, 1240, 1280, 1440, 1680, 1920 e 2560; ogni nome del percorso su una riga a tutte le larghezze; la lamiera finisce dentro la finestra; ancore interne tutte presenti.
- Larghezze guardate a pezzi: 320, 390, 768, 1024, 1440, 1920; menu aperto a 390 e 320. Nessuno scorrimento orizzontale, nessun elemento fuori dalla finestra, nessuna sovrapposizione.
- `controlla_finale.py`: nessun U+2014 in pagina, nei .md e negli script; nessun segnaposto; spessori 20, 15, 10; 16 immagini, tutte usate, 1,7 MB in totale.
