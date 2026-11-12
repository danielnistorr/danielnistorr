# Nardi, home: metodo ibrido e livello professionale

## Metodo ibrido (novembre 2026)

3/11/2026. Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (modello L della riga di Nardi nel capitolo 5); sotto, i contenuti e le funzioni della versione professionale, rimessi su una griglia sola a 12 colonne. Direzione scritta prima dell'HTML in `_prova/alto/DIREZIONE.md`; la versione professionale è copiata intatta in `_prova/versione-pro/` (`sito/` e `screenshot/home/`). Si rifà tutto con gli script di `_prova/alto/script/` (vedi LEGGIMI).

### Alto livello: ritocco dopo il giudice da agenzia (3/11/2026)

Il giudice aveva dato 6,5 (prima schermata 5,5): sotto la piega "il lavoro di uno studio serio", in apertura sei tessere mezze vuote "da e-commerce", nessun punto di scala, tre tagli di colonna. Le prove dei clienti tipo avevano due compiti non riusciti: le scatole dell'apertura non si toccavano (il privato tocca "Fughe" e non succede niente) e a 390 i campi di ricerca erano due. Questo giro corregge `sito/index.html` direttamente: dove i punti 1, 4 e 7, le misure e i controlli delle sezioni più sotto dicono altro, vale questo ritocco.

**Attenzione**: `_prova/alto/script/build.py` rimonta la pagina da `home.html` e `script.js`, che non hanno questo ritocco. Non va rilanciato; se serve, prima si riportano lì le modifiche di `sito/index.html`.

Che cosa è cambiato:
1. **Tessere rifatte** (`_prova/alto/ritocco/tessere.py`, sulle stesse sei sorgenti 1600 x 1226 del loro sito): la scatola è scontornata dal fondo da studio (maschera colonna per colonna: stretta sul colore e sul nero della scatola, larga solo sul bordo alto), senza alone e senza riflesso, e posata su un grigio piatto unico (240, 240, 238). Stesso taglio per tutte, 713 x 1193 (1:1,67): scatola larga il 92% della tessera, la più alta all'86%, posata al 7% dal fondo. A 1440 la tessera è 213 x 357; dentro le colonne della scatola il tratto di fondo uniforme più lungo è di 48-51 px (prima la metà alta, circa 300 px, era fondo allungato). File 240, 360, 480 e 713 px; i vecchi `scatola-*` sono tolti.
2. **Titolo sopra la fila**: l'`h1` "Stucchi, gessi e malte da Tombelle di Saonara" (28/36) sta sopra le sei scatole, e il blocco è centrato nella prima schermata (strada D2 "800-1600": oggetti alla loro misura, mai ingranditi, titolo sopra, molta aria). La regola del 60% con sei scatole in fila non torna: la larghezza della colonna fissa l'altezza della scatola. Le tessere coprono il 35,3% a 1440 (39,6% a 390), quindi la misura cade nella fascia 15-55%: è una scelta dichiarata, perché gonfiarle avrebbe voluto dire o ingrandire i file o rimettere il fondo vuoto. A 1920 l'`h1` sta a 260 px e la fila finisce a 850 (sopra i 1080); a 1024 l'`h1` sta a 229. Le tessere hanno `max-height` legata a `100svh`, e `sizes` è corretto (294 px a 1920, `(100vw - 160px) / 6` da 1024, tre per riga fino a 1023).
3. **Le sei scatole sono link** (`<a href="#cerca" data-lavoro>`): un tocco apre i prodotti di quel lavoro, con per primo il prodotto della scatola in foto (anche dalle righe dei lavori: prima "Riempire crepe e buchi" metteva per primo lo stucco in pasta, ora lo stucco in polvere per interni della scatola magenta). Senza JavaScript portano a "Cosa devi fare?". Didascalia con la freccia, sottolineata al passaggio. **Eccezione a D3**: la fila conta 6 cliccabili e 1 "fila di ingressi", ma è il gesto di D1, non una fila di ingressi generica (a 1440 i cliccabili sono 12, 6 senza le scatole; a 390 sono 10, 4 senza le scatole).
4. **Testata**: logo sulla griglia; campo, voci e telefono in una riga flessibile (il campo è largo tre colonne, da col 3 a col 5). Lo stato non va più a capo (`white-space:nowrap`) e i testi sono più corti: "Chiuso, riapre domani alle 8", "Chiuso, riapre lunedì alle 8", "Festivo, riapre domani alle 8", "Ferie, riapre ... alle 8", "Chiuso, riapre alle 14". Il menu completo compare da 1280 px; tra 1024 e 1279 "Menu" sta a destra accanto al telefono.
5. **Scala tipografica**: quattro misure a 1440, 14/20 (didascalie, dati, tabelle, interfaccia), 18/28 (testo, nomi a 600, menu, bottoni), 28/36 (`h1`, `h2`) e 44/52 per la frase-firma. Tutte le interlinee in px su un passo di 4. La frase-firma "Prodotti per l'edilizia professionale e il fai da te" è l'unico punto di scala: 44 nel culmine e, con lo stesso trattamento, nel piede (36 sotto i 1024 px, 28 a 390). A 390: 14, 17/28, 24/32 e 28/36.
6. **Culmine**: la sede a 1360 x 420 con `object-position: 50% 35%` (meno piazzale, la facciata lilla con gli attrezzi in centro, bordo basso della facciata a circa il 63% dell'altezza); sotto, la frase-firma su col 1-5 e il testo dell'azienda da col 7, alti uguali (120 px). Tolto il paragrafo secondario (fotovoltaico, Made in Italy); "dipinta come la scatola" passa nella didascalia.
7. **Un solo taglio di colonna**: in tutte le sezioni a due colonne la sinistra è col 1-5 e la destra parte da col 7 (728 px a 1440). Nell'indice di Prodotti la descrizione parte da col 9 (957 px), e nella tabella dei codici la seconda colonna cade sullo stesso filo; "Codici e schede" nelle righe è diventato "Codici". Il magazzino è sceso da 7 a 5 colonne, i tre passi sono saliti da 4 a 6.
8. **Colonne corte**: il blocco di "Cosa devi fare?" (titolo, campo e Cerca larghi fino a 597 px) e quello dei contatti sono `sticky` sotto la testata; la sezione della ricerca non ha più il margine sopra (l'apertura finisce con la sua aria).
9. **Bottoni**: "Apri l'elenco dei codici", "Chiedi il listino" e "Schede tecniche Artelinea" sono diventati righe-link con la freccia. Restano Cerca, Scarica il catalogo codici, Diventa rivenditore e Prepara l'email: 4 a 1440, 3 a 390 (più il telefono in testata).
10. **Un solo campo a 390**: nella prima schermata il campo "Cerca un prodotto o un codice" sotto le scatole; il campo di "Cosa devi fare?" e la sua riga d'istruzioni si nascondono sotto i 600 px (restano i sei lavori). A 768 e 1024 resta come prima.
11. **Testi tolti** (da 737 a 650 parole): i cinque negozi "che la vendono, tra gli altri" (LEGGIMI punto 3: non sappiamo se comprano da Nardi e manca il permesso di nominarli, D9), la riga "Per quantità e consegna chiama gli ordini" (il telefono è in testata), il paragrafo secondario del culmine.

Misure finali (`node _prova/alto/misura-d.mjs`, esito in `_prova/alto/misure-d.txt` e `misure-d.json`): 34 controlli passano, 5 sono eccezioni dichiarate, nessuno non passa.
- Prima schermata 1440 x 900: 12 cliccabili (6 senza le scatole), 0 bottoni, 132 caratteri, 1 fila (le scatole), nessuna cifra di 30 px; tessere al 35,3% con il titolo sopra, nessuna immagine ingrandita; dentro le tessere, il 24,9% della prima schermata è scatola e non fondo (misura sui pixel della schermata, `_prova/alto/ritocco/sonda.mjs`). 390 x 844: 10 cliccabili (4 senza le scatole), 1 bottone (il telefono), tessere al 39,6%.
- Registro: una famiglia (Kumbh Sans), misure a 1440 solo 14, 18, 28 e 44, interlinee 20, 24, 28, 36 e 52, testo corrente 18, niente oltre i 44 px, 0 occhielli, `h1` di 8 parole con una virgola, frase-firma 2 volte.
- Pagina: 650 parole a 1440 (618 a 390), 5.770 px a 1440 (prima 6.201), 7 sezioni, 4 bottoni, una griglia (40/1400, 12 colonne) con tutti i bordi sullo stesso filo, 8 foto in 3 formati (0,60, 1,78 e 3,24), nessuna ingrandita, 2 fondi oltre al piede, spazi 112 e 176, telefono scritto 2 volte con 3 link, 603 KB a 1440 e 475 KB a 390, nessun errore, nessun U+2014.

Controlli (`node _prova/alto/script/controlli.mjs`, esito in `_prova/alto/controlli.json`, schermate in `_prova/alto/prove/`): a 320, 390, 768, 1024, 1440 e 1920 nessuno scorrimento orizzontale, nessun testo fuori dal riquadro, nessuna sovrapposizione, nessun testo sopra le foto, nessun errore. 43 prove d'uso su 43, tra cui le nuove: stato su una riga a 1440 e a 1024 alle 19.30 di venerdì, l'8 dicembre e alle 19.40 di martedì (testata alta 77 px, `testata-chiuso-*.jpg`); un clic su ognuna delle sei scatole a 1440 mette per primo il prodotto giusto; a 390 un tocco sulla scatola rossa apre lo stucco per fughe (risultati a 76 px, `tocco-fughe-390.jpg`); un solo campo di ricerca a 390. Le ricerche del privato ora passano dal campo della prima schermata. Schermate di `screenshot/home/` rifatte con gli stessi nomi e guardate a pezzi.

Respinto o rimasto aperto:
- **Il 60% di D2** (vedi punto 2): con le foto di oggi si arriva solo cambiando oggetto. Le sei foto del materiale fotografato piatto (LEGGIMI, "Foto da fare dal vero") riempirebbero tessere quadrate senza questo limite.
- **Il giudice indicava la firma su col 1-7 e il testo su col 8-12**: ho tenuto il taglio unico a col 7 anche nel culmine, perché l'altra correzione chiedeva una sola colonna destra per tutta la pagina; alla misura di 44 px le due colonne vengono comunque alte uguali.
- **Il modulo dei contatti resta più alto della colonna dei dati** (906 contro 452 px): la colonna corta è `sticky`, come la seconda strada della correzione; il modulo su tre colonne a tutta griglia avrebbe allungato la pagina.
- **D1 con tre persone, D4 dell'ondata, la didascalia a due voci dell'apertura e la data EXIF del magazzino** restano come prima.

### Che cosa è cambiato

1. **Apertura: le sei scatole Briko Line da 1 kg in fila**, una per lavoro, in sei tessere alte 213 x 619 px a 1440 (due righe da tre a 390), tutte con lo stesso taglio, lo stesso fondo da studio e lo stesso trattamento; sotto ogni tessera una parola, il lavoro (Crepe e buchi, Fissaggi, Fughe, Muri, Caminetti, Calchi). Sotto la fila, solo l'`h1` "Stucchi, gessi e malte da Tombelle di Saonara" a 32 px. Nessun bottone, nessuna cifra, nessun occhiello. La riga del capitolo 5 chiedeva le tessere del materiale fotografato piatto: quella foto non esiste, quindi le tessere sono i rendering delle scatole del loro sito, tagliati su 704 px della sorgente e mostrati a 213 (mai ingranditi). Sopra la scatola il fondo da studio è allungato con il colore delle sue righe di bordo (#F0F0F0 uniforme): è solo fondo.
2. **Testata fissa con i compiti che lasciano l'apertura**: a 1440 logo, campo "Cerca un prodotto o un codice", tre voci che dicono che cosa si trova ("Codici e schede", "Diventa rivenditore", "Contatti e orari") e "Ordini 049 879 0626" con lo stato aperto o chiuso sotto. A 390 logo, "049 879 0626" (l'unico bottone) e "Menu", con tutte le voci (anche "Dove lo compro?" e "Schede tecniche Artelinea"); il campo di ricerca sta nella prima schermata, sotto la frase.
3. **Sotto la piega, sette sezioni su una griglia sola** (margini 40 px a 1440, 32 a 768, 16 a 390; colonne di 12 con 16 px di passo; tutti i bordi destri sullo stesso filo): Cosa devi fare? (ricerca grande, i sei lavori come righe d'indice con il prodotto sotto, le altre sei scatole da 1 kg per nome, i risultati con le quattro righe d'uso e le schede in PDF), Quattro linee e 96 prodotti (righe d'indice, catalogo PDF, elenco dei 193 codici filtrabile), Per i negozi (il magazzino in 16:9 con la didascalia a due voci, i tre passi, "Diventa rivenditore" e "Chiedi il listino", Dove si compra con i cinque negozi in una frase), Professionisti (testo, "Schede tecniche Artelinea", la dichiarazione di prestazione E180 in una tabella a filetti), il culmine con la sede a tutta griglia (1360 x 496 su una sorgente di 1920, didascalia "La sede di Nardi a Tombelle di Saonara, al civico 24 / maggio 2016") e la frase-firma, Contatti e modulo, piede.
4. **Carattere**: Kumbh Sans 400 e 600 (SIL OFL 1.1) al posto di Encode Sans; Hanken Grotesk, indicato dal capitolo 5, è già in due home. Niente oltre i 32 px.
5. **Colore**: fondo bianco, grigio gesso #F0F0F0 solo per la ricerca e il modulo, verde scuro solo nel piede; il verde del logo è l'unico accento. I colori pieni vengono dalle scatole.
6. **Tolto**: la fascia delle cifre (1985, 96, 89, 2011), la griglia delle dodici scatole, le quattro schede-linea con le foto, gli occhielli sopra i titoli, la foto dello scaffale con i prezzi, il sacco dell'E180 in un riquadro grigio, le fasce grigie, verde e lilla alternate, il telefono ripetuto (da 10 link a 3, scritto 2 volte), "Diventa rivenditore" in tre punti (ora 2), l'indirizzo e l'email ripetuti, il testo d'interfaccia sopra il modulo (ora accanto al bottone a 14 px).
7. **Frase-firma**: "Prodotti per l'edilizia professionale e il fai da te", dallo stand in fiera (`NARDI-AZIENDA-768x543.jpg`, citata in `01-analisi.md`); torna nel culmine e nel piede con lo stesso trattamento (28 px, 400).

### Misure

`node _prova/alto/misura-d.mjs` (copiato da `_metodo/professionale/alto/diagnosi/misure/misura.mjs` ed esteso), esito in `_prova/alto/misure-d.json` e `misure-d.txt`: 34 controlli su 34 passano.
- **Prima schermata 1440 x 900**: 6 cliccabili (logo, ricerca, tre voci, telefono), 0 bottoni, 132 caratteri, nessuna fila di ingressi, nessuna cifra di 30 px; foto sul 61,1%; `h1` di 8 parole con una virgola; una famiglia; testo corrente 19 px; niente oltre i 32 px; 0 occhielli.
- **Prima schermata 390 x 844**: 4 cliccabili (logo, telefono, Menu, ricerca), 1 bottone (il telefono), foto sul 52,1%.
- **Pagina**: 727 parole a 1440 (714 a 390), 7 sezioni, 6.201 px a 1440, una griglia (40/1400, 12 colonne) con i bordi destri e sinistri di tutte le sezioni sullo stesso filo, 8 foto da 3 formati (tessera 1:2,9, 16:9, panoramica 2,74:1), nessuna mostrata più grande del file, 2 fondi oltre al piede, due spazi tra le sezioni (112 e 176 px), nessun numero di 30 px o più, nessuna parola della lista nera, frase-firma 2 volte; telefono scritto 2 volte e 3 link `tel:`; info@, sicurezza@, indirizzo, rivenditore, catalogo, dichiarazione, stato e ricerca al massimo 2 volte; navigatore 1; 582 KB a 1440 e 453 KB a 390; nessun errore di script; nessun U+2014.

### Controlli e compiti

`node _prova/alto/script/controlli.mjs`, esito in `_prova/alto/controlli.json`, schermate di prova in `_prova/alto/prove/`.
- A 320, 390, 768, 1024, 1440 e 1920: nessuno scorrimento orizzontale, nessun testo che esce dal suo riquadro, nessuna sovrapposizione tra testi, nessun testo sopra le foto, nessun errore in console; un solo `tel:+390498790626`, `mailto:` solo a info@ e sicurezza@ con l'oggetto, il navigatore su `google.com/maps/dir`.
- 29 prove d'uso su 29 riuscite. Negoziante (1440): telefono e "Aperto ora, fino alle 12" senza scorrere; il codice 4302010 scritto nella testata dà il gesso murario con confezione e bancale (un'azione, meno di un secondo); "gesso murario" dà la scheda di sicurezza in un clic; catalogo PDF in due clic; elenco filtrato per linea; "Diventa rivenditore" dalla testata apre il modulo con il tipo già scelto; modulo vuoto si ferma, pieno compone l'email e lascia il testo; stato giusto alle 13.10, 19.30, di sabato, l'8 dicembre e a Pasquetta. Privato (390): ricerca nella prima schermata (campo fino a 773 px); i sei lavori nella seconda schermata (da 1086 px), mentre la prima mostra le sei scatole con il nome del lavoro; "fughe", "calco", "crepa", "caminetto", "stuko", "alabastrno" e "scatola elettrica" danno per primo il prodotto giusto; un tocco su "Caminetti e stufe" mette per prima la malta refrattaria Briko Line; le altre scatole da 1 kg aprono la loro scheda con la foto; "Dove lo compro?" a un tocco dal menu con "Non la trovi? Chiama gli ordini". Professionista: telefono a un tocco a metà pagina; "Schede tecniche Artelinea" dal menu apre l'elenco filtrato con 81 PDF; "Apri la sede nel navigatore" dal menu Contatti; dichiarazione E180 con norma, classe e PDF.
- Schermate rifatte in `screenshot/home/` con gli stessi nomi (più `home-1024-prima-schermata.jpg` e `home-768-prima-schermata.jpg`), guardate a pezzi accanto a quelle della versione professionale (`_prova/versione-pro/screenshot/home/`) e alla prima schermata di Clayworks e Tierrafino rifatta sul loro dominio (`_prova/alto/concorrenti/`).

### Dove stanno ora i compiti della scheda d'uso

| Compito | Prima (versione professionale) | Ora |
|---|---|---|
| Negoziante: telefono, orari, stato | apertura e testata | testata fissa (numero e stato), Contatti (orari) |
| Negoziante: codice e confezione | ricerca nella fascia dell'apertura, elenco | campo nella testata fissa a ogni altezza, ricerca grande nella seconda schermata, elenco in Prodotti |
| Negoziante: catalogo PDF | apertura, Prodotti, piede | Prodotti e piede |
| Negoziante: diventa rivenditore, listino | apertura, testata, Per i negozi | voce della testata (modulo con il tipo scelto), Per i negozi |
| Negoziante: scheda di sicurezza | risultati, elenco, piede | uguale |
| Privato: ricerca e sei lavori | prima schermata a 390 | ricerca nella prima schermata; sei scatole con il lavoro nella prima, sei lavori cliccabili nella seconda |
| Privato: come si usa | risultati | uguale (quattro righe d'uso e scheda tecnica) |
| Privato: riconoscere la scatola | dodici scatole in Prodotti | sei scatole in foto nell'apertura e nei lavori, le altre sei per nome subito sotto; ogni risultato ha la foto |
| Privato: dove comprarlo | link nell'apertura a 390, sezione | voce "Dove lo compro?" del menu, blocco in Per i negozi con "Non la trovi? Chiama gli ordini" |
| Professionista: schede Artelinea | Professionisti, menu | voce del menu a 390, Professionisti, righe di Prodotti |
| Professionista: dichiarazione E180 | riquadro in Professionisti | tabella in Professionisti, piede |
| Professionista: chiamare, arrivare in sede | testata, Contatti | testata fissa, Contatti con "Apri la sede nel navigatore" |

### Problemi aperti

- **Le tessere sono rendering delle confezioni, non foto del materiale.** Il modello L chiedeva alabastrino, scagliola e stucco in pasta fotografati piatti: finché quelle foto non ci sono, le scatole fanno il lavoro, e la metà alta di ogni tessera è fondo da studio. La misura del 61% conta tutta la tessera: a occhio le scatole occupano circa il 35% della prima schermata. Con le sei foto del materiale (LEGGIMI, "Foto da fare dal vero") le tessere si riempiono senza cambiare la pagina.
- **Il magazzino**: la didascalia dice "in magazzino" e la data dello scatto (EXIF, 27/5/2016, Canon EOS 1100D), non di chi è il magazzino. `IMG_4232` viene subito dopo `IMG_4228`, la foto della sede, ed è dello stesso giorno della `TESTATA6`: è probabile che sia il loro, ma va confermato (LEGGIMI punto 10).
- **La data della sede** ("maggio 2016") viene dal file `TESTATA6.jpg` salvato il 27/5/2016 con Photoshop: è la data del ritocco, lo scatto può essere di poco prima.
- **A 768 e 1024** la prima schermata non ha il campo di ricerca (a 1024 è in testata, a 768 è nella sezione subito sotto): il campo nella prima schermata c'è solo sotto i 600 px.
- **Sotto la prima schermata i lavori non hanno più la miniatura della scatola**: la foto è nell'apertura, la riga dice il prodotto. Le dodici scatole in foto sono diventate sei in foto e sei per nome.
- **Restano da confermare** i punti del LEGGIMI: il numero degli ordini (049 879 0626 contro 049 879 9070), la vendita diretta ai negozi, i cinque negozi (in pagina solo come "la vendono, tra gli altri", come dicono i loro siti), le chiusure aziendali per lo stato, il magazzino e la sede.
- **Il controllo D1 con tre persone e il controllo D4 dell'ondata** (aperture sovrapposte della zona) non si possono fare da qui: vanno fatti con le altre home di Saonara, Villatora, Tombelle e Vigonovo.

---

*Nota della versione professionale, invariata.*

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Tutto si rifà con `bash _prova/script/build_finale.sh`. La versione precedente ("Una scatola sola", con il selettore delle sei famiglie e la foto Unsplash delle mani) è copiata intatta in `_prova/versione-1-originale/`.

Screenshot: `home-1440.jpg` (circa 8.000 px, piede compreso), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti, modulo e piede). Guardati a pezzi a 1440 e a 390; prime schermate e pagine intere anche a 320, 768, 1024 e 1920; stati della ricerca ("fughe" a 390, "gesso murario" a 1440), elenco dei codici aperto con il filtro Artelinea, menu aperto a 390.

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M, adattata a un produttore che vende ai negozi. Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (fogli di contatto), le pagine intere di Cly-Del e barth a pezzi. Il controllore aveva dato 5 su 10 ("sembra il portale di un e-commerce"): questo giro applica i suoi difetti e quelli delle due prove d'uso (negoziante e privato).

### Che cosa è cambiato

1. **Apertura come i riferimenti M**: una dichiarazione e un gesto. A sinistra occhiello, H1 "Stucchi, gessi e malte" su una riga (68 px), la frase della scheda d'uso, il blocco ordini con lo stato, "Ordini 049 879 0626" pieno a 58 px e "Diventa rivenditore" bordato; a destra il **magazzino di Nardi a vivo** fino al bordo dello schermo (720x514 a 1440, metà pagina), con i bancali Briko Line. Lo scaffale del negozio è passato in "Dove si comprano", dove dice il vero.
2. **Ricerca e sei lavori in una fascia grigia a tutta larghezza** in fondo alla prima schermata (label, campo e Cerca su una riga, sei tessere in una riga). A 390 l'ordine resta quello di prima: ricerca e lavori senza scorrere, poi il telefono.
3. **Gesto di scala: la fascia dei numeri** su verde scuro subito dopo l'apertura, quattro cifre vere (1985, 96 prodotti, 89 schede tecniche in PDF, 2011 fotovoltaico) a 120 px (64 a 390), etichette a 17 px, filetti verticali. Tolte le due cifre di riempimento (4 linee e 12 pezzi restano nel testo di Prodotti e Per i negozi).
4. **Rendering rifatti** (`_prova/script/pro_rendering.py`): fondo grigio sfumato sostituito da bianco pieno, riflesso e ombra sotto la confezione tolti (taglio sul bordo basso inclinato, colonna per colonna), confezione centrata e alta il 75% del riquadro in tutte. Le tre foto da studio non da rendering (`Q48A8102`, `Q48A8140`) sono sostituite dai rendering Artelinea dello stesso prodotto; il cemento grigio Artelinea (`Q48A8038`) resta senza miniatura. "Altri prodotti" ora mostra il mastice per vetri, "Artelinea" il sacco da 25 kg dell'E180, "Gli speciali" lo stucco per grossi spessori.
5. **Foto in serie** (`pro_img.py`): un solo trattamento per magazzino, scaffale e sede (bianco neutro, arancio delle scaffalature desaturato del 30%, stessa curva, stessa desaturazione), tutte in 4:3; la sede è tagliata stretta su ingresso, fasce lilla e pilastro NARDI e mostrata al massimo a 533 px (sorgente 747).
6. **Tessere dei lavori** alte 72 px, miniatura 64 px su bianco, nome a 17 px in larghezza normale, bordo 1 px e raggio 4 come i bottoni (freccia sotto i 1024 px).
7. **"Riconosci la scatola"** (dalla prova del privato): dodici scatole Briko Line da 1 kg con il nome sotto, in Prodotti; ogni scatola apre la sua scheda nei risultati.
8. **Professionisti**: la dichiarazione di prestazione è un riquadro a sé con il sacco, "Dichiarazione di prestazione n. 1 - E180 - 2017", prodotto, norma UNI EN 13279-1, reazione al fuoco classe A1 e "Scarica il PDF"; le righe-link sono diventate bottoni del sistema.
9. **Logo** 180x41 a 1440 e 128x29 a 390.
10. **Catalogo codici in PDF vero** (`sito/catalogo-codici-nardi.pdf`, 5 pagine A4, 184 KB, fatto da `pro_catalogo.mjs` con la stessa tabella): intestazione con logo, ragione sociale, indirizzo, ordini, orari, email e "aggiornato al 3 novembre 2026", piede con il numero di pagina, senza filtri, bottoni né colonna schede. Si scarica dalla sezione codici, dai passi del negoziante e dal piede.
11. **Confezioni scritte in un modo solo** ("1 kg x 12 pz, bancale 720 kg", "750 g x 12 pz, bancale 768 pz", "1 l x 12 pz"); gli ossidi hanno "500 g x 6 pz" (da `01-analisi.md`), mordenti e due righe della polvere ceramica "confezione: chiedere al 049 879 0626".
12. **Ricerca**: ogni lavoro mette prima il prodotto che gli dà il nome e la scatola Briko Line (Fughe: prima lo stucco per fughe); parole dei lavori (calco, crepa, scatola elettrica, caminetto, stufa...) che valgono più del testo libero; radice solo da 6 lettere; una lettera sbagliata tollerata (stuko, alabastrno). Le righe d'uso sono sempre le stesse quattro (acqua, tempi, spessore, uso), con "vedi scheda tecnica" dove la scheda non dà il dato; "30%" diventa anche "circa 300 g d'acqua per 1 kg".
13. **Modulo**: oggetto senza parentesi annidate ("Diventare rivenditore: Ferramenta Rossi, Este (PD)"); dopo "Prepara l'email" resta sempre un riquadro con il testo pronto, "Copia il testo", l'indirizzo e il telefono, per chi non ha un programma di posta. "Richiesta" in testata sceglie "Ordine".
14. **Varie**: "Scritto sulle confezioni Briko Line" (non più "su ogni"); passo 3 dei negozi con il link alle schede di sicurezza e la voce "Schede di sicurezza" nel piede; sezioni a colori che si fermano esattamente sotto la testata (niente striscia bianca); script dello stato pronto per le chiusure aziendali (elenco vuoto finché Nardi non le dà).

### Struttura

Testata fissa · apertura (bianco, magazzino a vivo) e fascia della ricerca (grigio) · numeri (verde scuro) · Per i negozi (bianco: tre passi) · Prodotti (grigio: quattro linee, scatole, elenco codici e catalogo PDF) · Professionisti (bianco, riquadro E180 grigio) · Dove si comprano (grigio, scaffale e cinque negozi) · Azienda (lilla, sede) · Contatti e modulo (grigio) · piede (verde scuro).

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky` di 89 px a 1440 e 73 a 390; bottone "Ordini 049 879 0626" alto 48 px (a 390 solo il numero); a metà pagina a 390 si vede e si tocca (`elementFromPoint`). 10 link `tel:`, tutti `tel:+390498790626`. "Richiesta" bordato accanto.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1, "Produttori dal 1985, Tombelle di Saonara (PD)", il telefono ordini pieno, "Diventa rivenditore", lo stato, la ricerca e i sei lavori. 390 x 844: H1 a 40 px, ricerca entro 404 px, lavori entro 654, telefono pieno a tutta larghezza (350 px) da 788. La prova resta l'anno: le altre non ci sono nelle fonti.
3. **Immagine vera nell'apertura: passa a 1440.** Il magazzino di Nardi (`IMG_4232`) a vivo sulla metà destra, 720x514. A 390 la foto viene dopo il telefono (1034 px), per lasciare ricerca e lavori nella prima schermata come chiede la scheda d'uso. Mancano ancora persone e produzione: è la prima foto da fare (LEGGIMI).
4. **Zero repertorio: passa.** `indicativ` 0 volte, nessun file Unsplash o Pexels, nessun disegno.
5. **Foto in serie: passa.** Due formati (4:3 per le tre foto, 1:1 per i rendering su bianco pieno), una didascalia su 26 immagini, un trattamento solo per le tre foto. La luce dei tre scatti resta diversa: la serie vera richiede il servizio fotografico.
6. **Palette dal marchio: passa.** `--verde` #276E59 (dal logo #46A589), `--verde-scuro` #173F33, `--lilla` #9396C8 della facciata, `--lilla-chiaro`; neutri freddi; nessun colore fuori da `:root` (anche il foglio di stampa usa i token). Fondo bianco.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 68, 120) e 8 a 390 (14, 16, 17, 19, 24, 30, 40, 64); testo corrente 19 a 1440 e 17 a 390; niente sotto i 14 px; H1 68/40 (fascia M), H2 48/30.
8. **Due famiglie al massimo: passa.** Una sola, Encode Sans: stretta (75 %) a 700 per titoli, numeri e telefono; normale a 400 e 700 per testo e interfaccia (tessere comprese).
9. **Servizi in schede con foto: passa.** Quattro linee in 4 colonne (2 a 390), passo 28 px, confezione quadrata su bianco per tutte, nome a 23 px, riga e "Codici e schede"; tutta la scheda è un link. In più dodici scatole in 6 colonne.
10. **Almeno tre tipi di prova: passa, con riserva (3 su 4).** Quattro numeri aziendali in fascia; la dichiarazione di prestazione E180 in un riquadro con il PDF; cinque negozi con nome e comune (da confermare, LEGGIMI punto 3). Recensioni: nessuna nelle fonti, non inventate.
11. **Lavori con un nome: non passa.** Nessun lavoro con cliente, luogo e anno nelle fonti; nessun segnaposto in pagina (LEGGIMI punto 5).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: numeri in verde scuro e Azienda in lilla; fascia della ricerca, Prodotti, Dove e Contatti in grigio, alternati al bianco. Sezioni a 120 px a 1440 e 72 a 390; margine 80 a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 4 px; altezze 48 (testata, filtri), 56 e 58 (telefono e "Diventa rivenditore" in apertura); testo 17 px (16 a 390, 32 e 24 nel telefono grande); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Tipo di richiesta, nome, negozio, città, partita IVA, telefono, email, prodotti e codici, messaggio; il mailto non porta allegati, quindi la pagina chiede di allegare l'ordine all'email e il LEGGIMI chiede il campo nel servizio. Nessun iframe; sede con "Sede nel navigatore" e "Apri la sede nel navigatore".
15. **Piede completo: passa.** Quattro colonne (marchio e indirizzo; Prodotti con schede di sicurezza e catalogo PDF; Azienda con la dichiarazione E180; Contatti con telefono, fax, due email, orari e stato) e riga legale; niente sotto i 14 px.

### Compiti della scheda d'uso (`_prova/uso/SCHEDA.md`, par. 8)

`node _prova/script/pro_shots.mjs`: 51 prove su 51 riuscite.
- *Negoziante, 1440*: telefono ordini, orari e stato senza scorrere (martedì 10.00 "Aperto ora, fino alle 12"); "Codici, confezioni e catalogo in PDF" apre l'elenco dei 96 prodotti (179 link PDF), filtro Artelinea; il catalogo in PDF vero si scarica in due clic; "Diventa rivenditore" sceglie il tipo nel modulo, vuoto si ferma, pieno compone l'email e lascia il testo da copiare; "gesso murario" dà la scheda di sicurezza in un clic; il codice 4302010 trova il gesso murario.
- *Privato, 390*: ricerca e "Chiama" senza scorrere; "Fughe e piastrelle" apre per primo lo stucco per fughe Briko Line; "fughe", "calco", "crepa", "scatola elettrica", "caminetto", "stuko" e "alabastrno" danno per primo il prodotto giusto; la scatola della malta refrattaria apre la sua scheda; "Dove lo compro?" nella prima schermata; dal menu "Dove si comprano" si ferma sotto la testata.
- *Professionista*: "Schede tecniche Artelinea" apre l'elenco filtrato; la sede si apre nel navigatore in un tocco.
- *Orari*: 13.10, 19.30, sabato, 8 dicembre, Pasquetta e 15.00 danno il messaggio giusto.

### Caratteri e licenze

- **Encode Sans** (The Encode Project Authors), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file variabili serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, larghezze 100 % e 75 %.
- **Foto**: solo materiale di Nardi dalla libreria media di narditalia.com (magazzino, scaffale, sede, rendering delle confezioni, logo). Nessuna foto di repertorio, nessuna immagine generata, nessun disegno (`assets/CREDITI.md`).

### Controlli fatti (3/11/2026)

- Screenshot guardati a pezzi a 1440 e a 390, prime schermate a 320, 768 e 1024, risultati della ricerca a 1440, prime due pagine del catalogo PDF.
- Nessuno scorrimento orizzontale e nessun testo che esce dal suo riquadro a 320, 390, 768, 1024, 1440 e 1920 (controllo anche sui singoli nodi di testo); nessun errore di script.
- `tel:+390498790626` ovunque; `mailto:` con oggetto; mappe con `google.com/maps/dir`; nessun U+2014 in pagina, nei .md e negli script (controllo nel `build_finale.sh`).
- Dati: ogni fatto in pagina viene da `01-analisi.md`, dalla scheda d'uso o dalle schede prodotto del loro sito; quello che è dubbio sta nel LEGGIMI.
