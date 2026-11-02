# Servalli Padova, home finale

Pagina: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini (`finale_img.py`), pagina (`home_finale.html` copiata in `sito/index.html`), caratteri e screenshot (`finale_shoot.mjs`). Prova dell'interazione: `node _prova/script/finale_prova_anni.mjs <percorso di sito/index.html>`.

Altezza della pagina, piede compreso: 5445 px a 1440, 6804 px a 390.

## L'idea

Base: il prototipo B, "Quattro secoli", con i quattro ritocchi del giudice. Il pezzo raro dell'azienda, il Tabriz annodato a mano del loro negozio (marchio Alans), sta in piedi sulla carta come in una tavola di catalogo: quasi intero, a filo del bordo destro, con le due quote vere, 205 e 298 cm. È un oggetto solo, con le sue misure e nient'altro sopra. Sotto, la biancheria bianca (la parte più grande del lavoro) e l'albergo; poi la storia come prova, un anno alla volta. Con il nome di un concorrente la pagina non regge, perché il tappeto, le misure, i marchi, le date e le foto d'archivio sono solo loro.

## Le prime due schermate

1. Testata chiara: logo con stemma e SERVALLI, senza la sottoriga "TESSILE CASA DAL 1895" (a 132 px era illeggibile); Prodotti, Alberghi e contract, Rivenditori, Storia, Negozio online; telefono. Il titolo è "Tessile casa dal 1895", la riga del loro logo e del titolo del sito, in Caslon a 120 px (cresce fino a 164 px sugli schermi larghi). Sotto ci sono una riga su cosa vendono (biancheria casa e albergo, piumini, coperte, tende, tappeti annodati a mano, circa 20.000 articoli all'ingrosso, quattro generazioni, Padova), il bottone "Il negozio online" e il link "Per alberghi e rivenditori". A destra il Tabriz in verticale, alto dal sotto-testata fino a 60 px dal fondo della schermata (461 x 712 px a 1440 x 900), con la quota "205 cm" sopra: finisce dove finisce il tappeto, cioè al bordo. La quota "298 cm" è sul fianco sinistro, staccata di 32 px. Le quote sono a inchiostro, 1 px, con le tacche. In basso a sinistra la didascalia vera dell'articolo. Le quattro legende del prototipo sono tolte.
   - A 390 il tappeto viene sotto titolo e riga, sempre a filo del bordo destro e con le due quote; il bottone entra nella prima schermata.
2. "Circa ventimila articoli, dal letto al tappeto". In Caslon a 40 px, due righe a 1440 e quattro a 390: "Lenzuola e biancheria per la casa, piumini e trapunte, coperte, asciugamani e accappatoi, tende, tappeti annodati a mano e altro". Sotto, in Golos piccolo, l'assortimento completo verbatim da `informazioni` e i quattro marchi. Poi due foto della stessa altezza e della stessa luce, a filo dei bordi:
   - "Per la casa": la pila di lenzuola bianche, presa da A.
   - "Per alberghi e rivenditori": gli asciugamani con l'iniziale ricamata, senza l'etichetta blu, schiariti al bianco caldo. La frase delle condizioni ora dice "Rivenditori, grossisti e alberghi", come la pagina Partners.

Seguono la storia con l'archivio (l'unica interazione), i tre riconoscimenti in una fascia, la chiusura e il piede.

## Chiusura e piede

- **Chiusura** ("b con foto"). La frase è loro, dalla pagina Forniture alberghiere: "Possiamo fornire tutti i prodotti tessili di cui potreste avere bisogno". Sotto ci sono:
  - il telefono grande in Caslon (tel:), a 64 px dalla frase;
  - l'email (mailto:);
  - l'indirizzo con il link alla mappa e "al Centro Grossisti, zona industriale";
  - gli orari.
  
  A destra la pila di tappeti, quadrata e a filo del bordo. Il testo è allineato al fondo della foto. Non c'è un riquadro né una card.
- **Piede**, con le stesse carte e lo stesso inchiostro della pagina:
  - logo intero e una riga su chi sono;
  - Azienda (Storia, Riconoscimenti, Marchi, Arte tessile);
  - Prodotti (le 6 categorie vere del negozio);
  - Servizi (Alberghi e contract, Rivenditori e grossisti, Negozio online, Contatti, più telefono ed email cliccabili);
  - Newsletter, con campo, bottone e casella del consenso. Ha senso perché dal 2022 vendono online ai privati, hanno offerte e stagioni, e il loro modulo contatti già chiede l'iscrizione. Non funziona finché non si collega a un servizio: vedi LEGGIMI.

  In fondo la riga legale completa (ragione sociale, P.IVA e C.F., capitale sociale, Registro imprese di Padova), poi Privacy, Cookie, Condizioni di vendita. Non c'è una colonna Seguici, perché i social del sito attuale puntano alle home generiche dei servizi. A 1024 il logo va su una riga sopra le quattro colonne. A 390 le colonne si impilano in ordine.

## Caratteri e colori

- **Libre Caslon Display** 400 per titoli, anni e telefono della chiusura. **Golos Text** 400, 500 e 600 per testi, menu, didascalie e piede, con le cifre tabellari per misure, codici e orari. È la coppia della direzione B (01-analisi, sez. 5). Un Caslon da titolo ad alto contrasto sta accanto alle grazie dei tappeti e al lineare spaziato del logo, come i serif di Pratesi (Saol) e Frette (Butler) nei riferimenti (sez. 7). Golos è un grottesco calmo, non nelle liste b della guida.
  - Licenza: SIL Open Font License 1.1 (uso commerciale libero), scaricati da Google Fonts e serviti dalla pagina in `sito/fonts/` (woff2 latin e latin-ext).
  - Libre Caslon Display non ha corsivo: `font-synthesis: none`, niente corsivi.
- **Colori**:
  - carta #F2EDE4 su tutta la pagina (un solo fondo);
  - nero seppia #23201B, 13,9:1;
  - grigio caldo #675F55 per note e didascalie, 5,4:1;
  - rosso robbia #9A2E22, preso dal campo del tappeto, solo per il bottone, l'anno scelto e "Iscriviti": 6,5:1 su carta, il bianco sul bottone 7,5:1.

  Il bianco e nero è solo nelle foto d'archivio, virate al seppia. Tutto il testo passa AA.

## Interazione

Sotto la foto d'archivio c'è una riga di cinque anni: 1895 Gandino, 1949 Madival, 1967 Padova, Anni 70 Persia, 1994 Tehran. Con un clic, un tocco o le frecce sinistra e destra cambiano la foto, l'anno grande in robbia e la frase, presa tra virgolette da `storia`.
- Il cambio è netto, senza dissolvenza.
- I bottoni hanno `aria-pressed` e la scheda è `aria-live`.
- Le altre foto si caricano quando ci si avvicina alla riga.
- Provato con clic e tastiera (`finale_prova_anni.mjs`): nessun errore. Il menu si apre con un bottone vero sotto i 1100 px e si chiude con Esc.

Non ci sono animazioni allo scorrere né effetti sul cursore. Le transizioni, di 0,12-0,15 s, sono solo sul colore di bottoni e anni.

## Foto, origine e licenza

- **Tabriz** (prima schermata): `assets/originali/negozio/4126147316.jpg`, foto del loro negozio Ecwid (articolo marchio Alans, 205 x 298 cm), scontornata con PIL e messa in verticale. L'originale è 1500 px: a 2x è un poco ingrandita. I diritti vanno chiariti, perché la foto può essere del fornitore.
- **Archivio**: tutte dalla pagina `storia`, tagliate 4:3 e virate allo stesso seppia. L'uso va chiesto all'azienda.
  - `Servalli1895-59539f29.jpg` (alt del sito "Servalli 1910");
  - `MadivalMicheleFrancescoServalli.jpg`;
  - `manifatture_tessili_Servalli_Padova_1967web.jpg`;
  - `IMG_2245-ba4affe8-1ee72a8b.JPG`, tessitrice in Persia, firma "© Franco Servalli" lasciata;
  - `IMG_2252.jpg`, Tehran 1994.
- **Segnaposto**, da sostituire con foto vere. Licenze verificate sulla pagina di ogni foto il 24/10/2026 e annotate in `assets/CREDITI.md`. Nessuna è usata in un'altra home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md`) e nessuna è generata dall'IA.
  - Per la casa: juan pinales, Pexels 31902663, licenza Pexels;
  - Per alberghi: Antonio Araujo, Unsplash d0RbiJeEMQI, licenza Unsplash, tagliata sopra l'etichetta blu;
  - Chiusura: bahareh moradian, Unsplash NvdxYHt5CHM, licenza Unsplash.

  Tutte portate allo stesso bianco caldo, senza neri pieni (`finale_img.py`).
- **Logo**: `logo-servalli-stemma.png` (1920 x 823). Il bianco è reso trasparente con un "colore verso alfa" che lascia intatti i colori dello stemma. È esportato in WebP a 2x, testata (senza sottoriga) e piede. Non è ricostruito in SVG, perché lo stemma è un disegno dorato.

## Controlli

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920:
  - nessuno scorrimento orizzontale a nessuna larghezza (misurato: scrollWidth uguale alla finestra);
  - nessuna sovrapposizione;
  - a 768 la riga degli anni scende a 32 px per non toccarsi.
- `segnali.sh` (kit): 0 soglie bloccanti.
  - Foto 35,1 %, Caslon 12,6 % e Golos 87,4 %, una sola fascia di fondo, 4 filetti larghi, 0 etichette maiuscole sopra i titoli, 0 frecce.
  - Da guardare: "numero grande con etichetta" conta 2, ma sono il 1895 del titolo e l'anno dell'archivio. Il titolo non è un numero con etichetta.
- Nessun U+2014 nella pagina, nella NOTA e nel LEGGIMI (lo controlla `build_finale.sh`).
- Divieti del committente rispettati:
  - niente gradienti, testi in gradiente o emoji;
  - niente Inter, card con bordo colorato, glassmorphism o icone;
  - niente badge sopra il titolo, dissolvenze allo scorrere o effetti sul cursore;
  - niente lineette lunghe né corsivi d'accento.
- Tutti i fatti in pagina vengono da `01-analisi.md` e dal crawl di `storia`, `informazioni`, `partners` e `alberghi`. I dubbi sono nel LEGGIMI.
