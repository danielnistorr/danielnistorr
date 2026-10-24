# Home finale Poli-Art, "Grezzo e finito"

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini, pagina, screenshot). Parte dal prototipo A scelto dal giudice, con tutte le sue indicazioni e gli innesti da B.

Altezza a 1440: **4792 px** compreso il piede (giro prima 5207, prototipo 6299). A 390: 5766 px.

## L'idea

Il polistirolo è bianco, e il mestiere di Poli-Art è farlo diventare altro. La pagina è color polistirolo (#F5F4F1) e la testa a facce piane ci è posata sopra, scontornata, con la sua ombra, come su un banco di laboratorio. Un solo gesto: la legenda "Finito · Grezzo" sotto il pezzo mostra la stessa testa prima cromata con occhi e bocca dorati, poi bianca, in polistirene. Con il nome di un concorrente la pagina non regge: la testa e la sua coppia di foto sono solo loro.

## Le sezioni

1. **Apertura (1440x900)**. Logo vero, menu di quattro voci (Lavorazioni, Come lavoriamo, Realizzazioni, Contatti), telefono. La **testa cromata** sta al centro, alta 650 px, posata sulla carta con un'ombra di contatto. Il titolo è spezzato attorno al pezzo: "Polistirolo scolpito" in alto a sinistra, "e rifinito" in basso a destra, con la base delle lettere sulla linea d'appoggio della testa. In basso a sinistra, sulla stessa linea, la frase con le lavorazioni, le macchine a controllo numerico, la mano, Grisignano e il 1986. Sotto il pezzo, centrata come una legenda, la scelta "Finito · Grezzo": due parole, quella attiva sottolineata, e la didascalia sotto. Niente pillola, niente commutatore in un angolo.
   - A 390: "Polistirolo scolpito" a sinistra, "e rifinito" allineato a destra sulla terza riga, la testa al centro, la legenda e la didascalia; tutto nella prima schermata (844 px), la frase subito sotto.
2. **"Finiture a prova di curiosi"** (frase del sito, `scenografie/`): quattro lavorazioni su due file, nella stessa fila la stessa altezza, tutte foto rettangolari con lo stesso trattamento (scenografie e stand, loghi in volume; prototipi e mockup con la chaise longue bianca scolpita, edilizia e decori) e una riga per torte finte e stampa 3D.
3. **"Dal file al pezzo finito"** (`#come-lavoriamo`): la foto del volume curvo in montaggio dentro la cornice, alta 440 px al massimo, e sotto il titolo a sinistra con due righe a destra (progetto 3D del cliente o solido virtuale elaborato da loro, taglio a controllo numerico, scultura a mano). Niente passi numerati.
4. **Chiusura "b con foto"** e piede.

## Cosa è cambiato in questo giro (giudizio cieco: K0 7, K6 6, 58 su 80)

- **Prima schermata ricomposta** (bloccante: ricalcava Marin Assemblaggi, titolo a sinistra, pezzo a destra, pillola in basso a sinistra). Ora testa al centro, titolo spezzato attorno, legenda di due parole sottolineate sotto il pezzo. Confrontata con le miniature della campagna (`_prova/cieco/campagna.jpg`): nessuna ha titolo a sinistra, oggetto a destra e commutatore in basso a sinistra; la parentela più vicina è il titolo spezzato di Daisyplast, ma lì la pagina è scura e senza gesto, qui chiara con la legenda sotto il pezzo.
- **Stessa inquadratura nei due stati**. La foto del grezzo (`Face-of-GOD2`) è presa dall'altro lato: in `finale_img.py` la tela del grezzo è **specchiata** e spostata di 20 px, così naso, occhi e bocca guardano a destra come nel finito. Prova di sovrapposizione al 50 % a 2x: gli occhi e la bocca cadono negli stessi punti della tela (`_prova/script/prova_specchio.py`). Il finito resta più di profilo: per la coppia perfetta servono le due foto dal vero (LEGGIMI).
- **Macchia d'oro sulla guancia tolta**: la saturazione dell'oro ora agisce solo dentro tre zone (occhio destro, bordo dell'occhio aperto, bocca, `ZONE_ORO`); il riflesso giallo sulla guancia torna metallo neutro. Controllato a 2x.
- **Chiusura**: la frase loro completata con il minimo, "Un prodotto riproposto in dimensioni più grandi suscita la curiosità del passante" (`mockup/`), accanto alla foto del **pallone abitabile in fiera** con la persona accanto, con il suo sfondo vero, ritagliata 4:3 senza lo striscione col marchio, e una didascalia. Frase e foto ora si spiegano a vicenda. Tolta la sala vuota (`Pawson2`).
- **Griglia**: il pallone scontornato (bordi rozzi, unico pezzo senza riquadro) è uscito; al suo posto la **chaise longue bianca** (`Chesslong`), foto rettangolare come le altre, voce "Prototipi e mockup".
- **Come lavoriamo**: la fascia del cantiere non è più a tutta larghezza (660 px) ma nella cornice, alta da 280 a 440 px; i tre passi 1-2-3 sono diventati due righe; il menu e il piede dicono "Come lavoriamo" e non più "Laboratorio".
- **Bianchi pareggiati** (`pareggia` in `finale_img.py`): il fondo misurato di ogni foto portato verso #EFEDE9 con una curva e un leggero contrasto locale. Lettere: fondo da RGB 167 a 233; stand da 130 a 188 (le luci della lampada non si spingono oltre); cornici da 129 a 202; chaise da 163 a 228.
- **Legenda attaccata al pezzo**: niente più 150 px vuoti tra la frase e il comando; la frase e "e rifinito" stanno sulla linea d'appoggio della testa, la legenda 13 px sotto la tela.
- **Piede**: voci con `padding:4px 0`, bersagli alti almeno 28 px (misurati: minimo 34 px a 390).
- Pagina da 5207 a 4792 px a 1440.

## Caratteri e colori

- **Mona Sans** (GitHub Next, Google Fonts, **SIL Open Font License 1.1**, uso commerciale libero), file woff2 serviti dalla pagina da `sito/fonts/` (variabile, pesi 200-900, larghezze 75-125 %). Una famiglia sola: titoli in 320-340 allargati a 108-118 % con spaziatura da -0,035 a -0,045em, testo 400, voci e didascalie 500. La larghezza 118 % riprende le lettere larghe e geometriche del logo POLI·ART; il grottesco chiaro e grande su fondo bianco viene dai riferimenti del mestiere: HiLT Projects (Helvetica Neue, i lavori parlano da soli) e Window France (Helvetica leggera grande su grigio chiarissimo). Non è Inter e non è nelle liste della guida. Cifre allineate (`lining-nums`); in pagina non ci sono colonne di numeri.
- **Colori**: carta #F5F4F1 (il bianco caldo del polistirolo), inchiostro #1B1D22 (15,3:1), grigio #55585F per didascalie e testo secondario (6,6:1 sulla carta, 6,0:1 sul piede), ardesia #4E5F7D dal blu del logo scurito per l'AA (sottolineature e passaggio sui link), piede #ECEAE5. Il colore pieno arriva solo dalle finiture vere: cromo e oro, rosso delle lettere, oro delle cornici. Niente fasce scure.

## Interazione

Legenda a due bottoni veri (`aria-pressed`) in un gruppo con etichetta; Tab per arrivarci, frecce sinistra e destra per passare dall'uno all'altro; la didascalia è in una regione `aria-live`. Bottoni alti 44 px, comodi col dito; la parola attiva è sottolineata con un filo di 2 px. Il cambio d'immagine è netto, senza dissolvenza; le due teste hanno la stessa tela (1120x1500), lo stesso appoggio e lo stesso orientamento (il grezzo è specchiato), quindi al clic cambia la materia e non la posa; il grezzo si precarica dopo il caricamento della pagina. Le uniche transizioni (0,12 s) sono sul colore delle parole e del telefono toccati; nessuna animazione allo scorrere, niente che segue il cursore, `prefers-reduced-motion` rispettato. Menu a scomparsa sotto i 900 px con un vero bottone (`aria-expanded`, chiusura con Esc).

## Chiusura e piede

- **Chiusura "b con foto"**: testo a sinistra, il pallone abitabile in fiera a destra fino al bordo (4:3), con la didascalia "Il pallone abitabile, in fiera. La persona accanto dà la misura." Frase loro (pagina `mockup/`), completata con il soggetto: "Un prodotto riproposto in dimensioni più grandi suscita la curiosità del passante", che lega con "a prova di curiosi". Sotto, a 56 px dal titolo: telefono grande con `tel:`, email con `mailto:`, indirizzo con il link a Google Maps. Orari non in pagina (non confermati).
- **Piede**: logo vero (PNG del sito ritagliato, 360 e 720 px per 180 px a schermo, cioè a 2x e oltre), una riga su chi sono, quattro colonne (Lavorazioni, Azienda con Chi siamo, Realizzazioni e Come lavoriamo, Contatti, Seguici con Instagram e Facebook a parole, i due social linkati dal sito); riga legale con "Poli-Art di Zigliotto Manuel, impresa individuale, P.IVA", Privacy, Cookie. A 390 le colonne si impilano nell'ordine Lavorazioni, Azienda, Contatti, Seguici. Tolta la voce "Eventi con Palloncini WOW" finché la collaborazione non è confermata.
- **Niente newsletter**: Poli-Art lavora su commessa e non pubblica notizie, cataloghi, collezioni o fiere proprie (`/wp-json/wp/v2/posts` è vuoto); i clienti privati (feste, torte) li segue già Instagram.

## Foto: origine e licenza

Tutte le foto in pagina sono **di Poli-Art**, dalla libreria media del sito attuale (`assets/originali/`, voti in `_prova/inventario-immagini.json`). Nessun segnaposto esterno, nessuna foto di repertorio, nessuna immagine generata dall'IA. Sul sito vero si usano con il loro consenso.

| In pagina | Originale | Lavorazione (`_prova/script/finale_img.py`) |
|---|---|---|
| testa cromata (apertura) | `Face-of-GOD-scaled.jpg` 1920x2560 | contorno a poligono (`contorni/finale-testa-finita.json`), occhio aperto tagliato, curva a S sul metallo, oro saturato solo in occhi e bocca, ombra di contatto |
| testa grezza (legenda) | `Face-of-GOD2.jpg` 1536x2048 | contorno a poligono (`contorni/finale-testa-grezza.json`), due fori degli occhi, luminanza rimappata su bianco caldo; **specchiata** e spostata di 20 px per avere lo stesso orientamento del finito |
| scenografie e stand | `Oggetti2-scaled.jpg` | ritaglio senza soffitto e lampada, fondo pareggiato verso la carta, contrasto locale |
| loghi in volume | `3Db-scaled.jpg` | ritaglio verticale, fondo portato sopra RGB 225 |
| prototipi e mockup | `Chesslong.jpg` | ritaglio 5:4 stretto sul pezzo, fondo pareggiato, saturazione più bassa (pavimento meno arancio) |
| edilizia e decori | `CorniciORO4.jpg` | ritaglio senza l'auto e il piazzale, luci pareggiate |
| come lavoriamo | `Pawson3.jpg` | ritaglio largo, nella cornice |
| chiusura | `Pallone1.jpg` | ritaglio 4:3 senza lo striscione col marchio, verde del prato meno saturo |

WebP in tre larghezze con `srcset` e `sizes`; le teste a 560, 840 e 1120 px (a schermo 485 px a 1440, al massimo 493: il 1120 è oltre il 2x; un 1680 sarebbe solo un ingrandimento della foto, che non ha quel dettaglio). Pagina intera: 1,5 MB tra pagina, immagini e caratteri.

## Controlli (questo giro)

- Screenshot guardati a pezzi a 1440, 390, 320, 768, 1024 e 1920, nei due stati della legenda; prime schermate 1440 e 390 nei due stati; ingrandimenti a 2x delle due teste e della guancia (`_prova/script/finale_prove.mjs`).
- `scrollWidth` uguale a `innerWidth` a 320, 360, 390, 414, 600, 768, 900, 999, 1000, 1024, 1280, 1440, 1680, 1920 e 2560.
- Le sole intersezioni misurate sono tra il margine trasparente della tela della testa e il titolo o i bottoni (4-6 px), nessuna sul pezzo visibile.
- Tastiera: Tab arriva a "Finito", freccia destra passa a "Grezzo" (`aria-pressed`, immagine e didascalia aggiornate), freccia sinistra torna, Invio su "Grezzo" funziona. Tocco a 390 su "Grezzo" e "Finito": funziona. Menu a 390: si apre al tocco, si chiude con Esc.
- Collegamenti: `tel:+390444614719`, `mailto:info@poli-art.it`, Google Maps con "Via Tesinella 7 36040 Grisignano di Zocco VI"; ancore `#lavorazioni`, `#come-lavoriamo`, `#contatti`, `#contenuto` tutte presenti.
- Bersagli toccabili: legenda 44 px, voci del piede almeno 34 px.
- `segnali.sh`: 0 soglie bloccanti su 10, 0 da guardare su 8 (foto al 38,5 % della pagina, una sola famiglia, 2 filetti, una sezione titolo a sinistra e paragrafo a destra, data 1986).
- Nessun carattere U+2014 nella pagina, nei .md e negli script; nessun segnaposto in pagina; nessuna dissolvenza, nessun badge, nessuna icona, nessun gradiente.
- Ogni fatto in pagina viene da `01-analisi.md`. P.IVA (da aggregatore) e "dal 1986" restano da confermare con la visura (LEGGIMI, punti 1 e 3).
- File consegnati in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-1440-prima-schermata-grezzo.jpg` e `home-390-prima-schermata-grezzo.jpg` per lo stato dopo il clic.
