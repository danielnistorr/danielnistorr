# Servalli Padova, home finale

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini (`finale_img.py`), pagina (`home_finale.html` copiata in `sito/index.html`), caratteri e screenshot (`finale_shoot.mjs`). Controlli: `node _prova/script/finale_controlli.mjs <percorso di sito/index.html>`.

Altezza della pagina, piede compreso: 5252 px a 1440, 6385 px a 390.

## L'idea

Il Tabriz annodato a mano del loro negozio (marchio Alans) sta al centro, in asse, come si guarda un tappeto: un tappeto persiano è simmetrico, e la prima schermata lo è con lui. Il titolo lo attraversa come la trama attraversa l'ordito, una parola per lato: "Tessile | casa" sulla prima riga, "dal | 1895" sulla seconda. Anche la testata è in asse: menu a sinistra, stemma al centro sopra le frange, telefono a destra. Sotto, la biancheria bianca (la parte più grande del lavoro) e l'albergo; poi la storia come prova, un anno alla volta.

Il fondo non è più la carta beige: è il bianco della biancheria d'albergo, #F7F6F2. La ragione si vede nella seconda sezione, dove il bianco pieno delle lenzuola e della spugna è portato esattamente al bianco della pagina e le foto ci finiscono dentro senza bordo. Il rosso robbia del bottone e degli anni viene dal campo del tappeto.

Nella campagna nessuna home è impaginata così: tutte hanno il titolo a sinistra e l'oggetto a destra o sotto. Qui l'oggetto sta nell'asse della pagina e il titolo gli si divide intorno; il corpo del titolo nasce dalla larghezza del lato (circa 120 px a 1440, 180 px a 1920).

## Le prime due schermate

1. A 1440 x 900 il tappeto è largo 552 px e alto 852 (dal sotto-testata a 48 px sotto la piega, dove resta il frangiato di fondo); occupa il 34 % della schermata, e titolo e tappeto insieme coprono tutta la larghezza utile. Le parole del titolo stanno a 48 px dal tappeto, a sinistra e a destra.
   - A sinistra, allineata verso il tappeto: "Biancheria per la casa e per l'albergo, piumini, coperte, tende e tappeti annodati a mano." In basso la didascalia: "Tabriz ghali, lana annodata a mano con inserti in seta, 205 × 298 cm, marchio Alans. I tappeti li importiamo direttamente dagli anni 70."
   - A destra: "All'ingrosso da quattro generazioni, a Padova, e anche online.", il bottone "Il negozio online" (porta a `negozio/`) e il link "Per alberghi e rivenditori".
   - Nessuna legenda, quota o scritta sopra la foto; niente ombra finta sotto il tappeto.
   - Sotto i 900 px resta in asse: "Tessile casa" sopra il tappeto, "dal 1895" sotto, poi le due righe, il bottone e la didascalia. A 390 il bottone entra nella prima schermata.
2. "Circa ventimila articoli, dal letto al tappeto", con una riga sola sull'assortimento e i quattro marchi. Poi le due foto della stessa altezza, a filo dei bordi:
   - "Per la casa": la pila di lenzuola bianche (Pinales);
   - "Per alberghi e rivenditori": gli asciugamani di spugna (Hansen), con un taglio stretto sulla spugna al sole, il riccio nitido e le ombre alzate senza spianarle.

Seguono la storia con l'archivio (l'unica interazione), i riconoscimenti in una riga, la chiusura e il piede.

## Chiusura e piede

- **Chiusura** ("b con foto"). La frase è loro, dalla pagina Forniture alberghiere: "Possiamo fornire tutti i prodotti tessili di cui potreste avere bisogno". Sotto il telefono grande in Caslon (tel:), l'email (mailto:), l'indirizzo con il link alla mappa e "al Centro Grossisti, zona industriale", gli orari. A destra la pila di tappeti, quadrata e a filo del bordo. Niente riquadri.
- **Piede**, sullo stesso bianco:
  - logo intero e una riga su chi sono;
  - Azienda (Storia, Riconoscimenti, Marchi, Arte tessile);
  - Prodotti (le 6 categorie vere del negozio);
  - Servizi (Alberghi e contract, Rivenditori e grossisti, Negozio online, Contatti, telefono ed email cliccabili);
  - Newsletter con campo, bottone e consenso. Ha senso perché dal 2022 vendono online ai privati e hanno offerte e stagioni. Non funziona finché non si collega a un servizio (vedi LEGGIMI).

  In fondo la riga legale (ragione sociale, P.IVA e C.F., capitale sociale, Registro imprese di Padova), Privacy, Cookie, Condizioni di vendita. Nessuna colonna Seguici: i social del sito di oggi puntano alle home generiche dei servizi. A 390 le colonne si impilano con la stessa distanza (36 px).

## Caratteri e colori

- **Libre Caslon Display** 400 per titoli, anni e telefono; **Golos Text** 400, 500 e 600 per testi, menu, didascalie e piede, con le cifre tabellari per misure, codici e orari. Un Caslon da titolo ad alto contrasto sta accanto alle grazie dei tappeti e al lineare spaziato del logo, come i serif di Pratesi e Frette nei riferimenti (01-analisi, sez. 7).
  - Licenza: SIL Open Font License 1.1 (uso commerciale libero), da Google Fonts, serviti dalla pagina in `sito/fonts/` (woff2 latin e latin-ext).
  - Libre Caslon Display non ha corsivo: `font-synthesis: none`, niente corsivi.
- **Colori** (contrasto sul fondo):
  - bianco biancheria #F7F6F2, un solo fondo per tutta la pagina;
  - nero seppia #23201B, 15,0:1;
  - grigio caldo #675F55 per note e didascalie, 5,8:1;
  - rosso robbia #9A2E22, dal campo del tappeto, solo per il bottone, l'anno scelto e "Iscriviti": 7,0:1; il bianco sul bottone 7,5:1.

## Interazione

Sotto la foto d'archivio una riga di cinque anni: 1895 Gandino, 1949 Madival, 1967 Padova, Anni 70 Persia, 1994 Tehran. Clic, tocco o frecce cambiano foto, anno grande e frase (tra virgolette, da `storia`; quella del 1895 è verbatim, con "(BG)"). Cambio netto, `aria-pressed` sui bottoni, scheda `aria-live`. Il menu si apre con un bottone vero sotto i 1100 px e si chiude con Esc o toccando una voce; l'hover del bottone vale solo con il puntatore, quindi sul telefono non resta nero. Niente animazioni allo scorrere né effetti sul cursore; transizioni di 0,12-0,15 s solo sul colore di bottoni e anni.

## Foto, origine e licenza

- **Tabriz** (prima schermata): `assets/originali/negozio/4126147316.jpg`, dal loro negozio Ecwid (marchio Alans, 205 x 298 cm), scontornato con PIL e messo in verticale. Il ritaglio è 749 x 1155 px: a 2x è ingrandito, quindi va rifotografato (LEGGIMI). Diritti da chiarire.
- **Archivio**: cinque foto della pagina `storia`, tagliate 4:3 e virate allo stesso seppia, con le luci sul bianco della pagina. Uso da chiedere.
- **Segnaposto**, da sostituire con foto vere; licenze verificate il 24/10/2026, in `assets/CREDITI.md`; nessuna usata in un'altra home della campagna, nessuna generata dall'IA:
  - Per la casa: juan pinales, Pexels 31902663;
  - Per alberghi: Mads Leif Hansen, Unsplash qPNgpYUCW0c (sostituisce Araujo, che era sfocato e aveva l'etichetta di un marchio);
  - Chiusura: bahareh moradian, Unsplash NvdxYHt5CHM.
- **Logo**: `logo-servalli-stemma.png` (1920 x 823), bianco reso trasparente, WebP a 2x; in testata senza la sottoriga, nel piede intero.

## Cosa è cambiato in quest'ultimo passaggio (2 novembre)

Dal giudizio cieco (56 su 80) e dalla richiesta del committente "più alta gamma, meno uguali tra loro":
- prima schermata rifatta dentro la stessa idea: il Tabriz al centro in asse, il titolo diviso ai due lati, testata in asse, didascalia vicino al tappeto; tolte le quote, l'ombra e la piccola foto d'archivio;
- fondo da carta beige #F2EDE4 a bianco biancheria #F7F6F2, con le foto di biancheria portate allo stesso bianco;
- foto degli asciugamani rifatta (taglio stretto, riccio nitido, ombre alzate senza grigio);
- già nel passaggio precedente: link del negozio a `negozio/`, elenco dell'assortimento tolto, rientri della coppia uguali, una sola voce "Alberghi e rivenditori", riconoscimenti in una riga, hover solo con il puntatore, citazione del 1895 verbatim, piede a 390 con spaziature uguali.

## Controlli

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920.
- `finale_controlli.mjs`, da 320 a 2560 px (14 larghezze): scrollWidth uguale a innerWidth a tutte; tappeto in asse (scarto 0 px); parole del titolo a 36-48 px dal tappeto; didascalia sopra la piega da 1024 in su. Riga degli anni provata con clic, frecce (anche il giro) e tocco a 390; menu con tocco, Esc e voce toccata; newsletter nei tre casi; 0 errori JS. L'unico messaggio in console è il preload del font bloccato perché la pagina è aperta come file://.
- Collegamenti: `tel:+39049761943`, `mailto:info@servalli.net`, mappa Google su Via Portogallo 11, 35127 Padova; tutte le ancore hanno una destinazione; i quattro link al negozio vanno a `negozio/`.
- `segnali.sh` (kit): 0 soglie bloccanti su 10. Foto 38,4 %, Caslon 8,6 % e Golos 91,4 %, una sola fascia di fondo, 4 filetti larghi, 0 etichette maiuscole sopra i titoli, 0 frecce. Da guardare: "numero grande con etichetta" conta 2, ma sono il 1895 del titolo e l'anno dell'archivio.
- Nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (lo controlla `build_finale.sh`).
- Divieti del committente rispettati: niente gradienti, testi in gradiente, emoji, Inter, card con bordo colorato, glassmorphism, icone, badge, dissolvenze allo scorrere, effetti sul cursore, lineette lunghe, corsivi d'accento; niente legende numerate con pallino e filetto.
- Tutti i fatti in pagina vengono da `01-analisi.md` e dal crawl di `storia`, `informazioni`, `partners` e `alberghi`. I dubbi sono nel LEGGIMI.
