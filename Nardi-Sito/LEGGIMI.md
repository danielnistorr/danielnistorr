# Nardi S.r.l. Unipersonale: proposta di nuova homepage

Proposta non richiesta di una nuova home per narditalia.com. Solo la home; nessun contatto con l'azienda, niente pubblicato.

- **Pagina**: `sito/index.html` (si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`.
- **Screenshot e nota**: `screenshot/home/` (`NOTA.md` spiega idea, schermate, caratteri, colori, interazione, foto e controlli).
- **Rigenerare tutto**: `bash _prova/script/build_finale.sh` (immagini, caratteri, screenshot, controlli, segnali). La pagina è scritta a mano in `sito/index.html`.
- **Ultimo passaggio**: corretti i difetti del giudice cieco (`_prova/cieco.json`); l'elenco di cosa è cambiato è nella NOTA.
- **Analisi e fonti**: `01-analisi.md`; schede prodotto riassunte in `_prova/crawl/prodotti.json`; prototipi in `_prova/home/a/` e `_prova/home/b/`.

## Dati da confermare prima di qualsiasi uso

- **Telefono in grande**: in pagina c'è 049 879 0626, quello del sito di oggi (fax 049 830 4579). Schede tecniche (2016), scheda di sicurezza (2019) e Reteimprese danno tel 049 879 9070 e il 049 879 0626 come fax. Quale numero va in grande?
- **Il magazzino nella chiusura** (`IMG_4232`, dalla libreria media del sito): che sia il magazzino di Via S. Antonio 24/a e che i bancali siano di produzione Nardi (in didascalia c'è solo "In magazzino: bancali di scatole Briko Line"). La facciata con il pilastro NARDI (`TESTATA6`) non è più in home: va confermata prima di usarla nella pagina Azienda.
- **Dichiarazione di prestazione** dell'Artestucco E180 (UNI EN 13279-1, reazione al fuoco A1, del 2017): è ancora valida? Le schede tecniche (2016-2019) sono aggiornate? Quali prodotti sono fuori produzione?
- **Dati del selettore**, presi dalle schede: alabastrino inizio presa 15-25 min, acqua/gesso 100/140; stucco cementizio grossi spessori strati da 1 a 5 cm, impasto 2 ore; malta pronta grigia tempo di impiego 2 ore, acqua d'impasto 18 % (la scheda della malta grigia dice "Colore Bianco": refuso da correggere); cemento rapido acqua/cemento 20/100, almeno 3 MPa a 30 minuti; colla per piastrelle consumo 3-4 kg/m², pedonabile in 24 ore. Tempi della lista dei gessi: murario 5-8, alabastrino 15-25, polvere ceramica 20-25, stucco per interni 60, scagliola 60-90 min.
- **Formati**: la scatola della colla per piastrelle porta scritto "1 Kg", ma la scheda Briko Line elenca solo confezioni da 5, 10 e 25 kg; lo stucco cementizio grossi spessori è nella linea "Gli speciali" ma esce anche in scatola Briko Line da 1 kg. Finché non c'è conferma, le didascalie del selettore per colla e stucco non dicono il formato.
- **La gamma**: 96 articoli in quattro linee (Briko Line 43, Artelinea 41, Gli speciali 6, Altri prodotti 6), come sul sito di oggi. Quali produce Nardi e quali rivende (latta GESCOL e solfato di calcio sono di terzi; schiuma poliuretanica, rete, secchielli)?
- **Fotovoltaico**: in pagina c'è solo "Dal 2011 un impianto fotovoltaico dà energia alla produzione". La frase del sito "riducendo a zero le emissioni inquinanti" è rimasta fuori finché l'azienda non la conferma (potenza dell'impianto, quota coperta).
- **Dove si comprano**: elenco o zone dei rivenditori, catene servite, vendita diretta in sede ai privati? Oggi la chiusura dice solo "Chiamateci per sapere dove trovare i prodotti".
- Titolare attuale (Leonardo Nardi secondo Reteimprese?) e se Benito Nardi è ancora in azienda; anno di costituzione della srl rispetto al 1985 della ditta; PEC; dipendenti; macchinari.
- Social: esiste una pagina Facebook vera? Oggi nel piede non c'è nessuna colonna Seguici.
- **Sito compromesso**: 2809 articoli di spam e 717 categorie spam sono ancora pubblici (per esempio `news/serbia-woman-help/`). Vanno tolti prima di qualsiasi migrazione, con i redirect 301 delle schede prodotto.

## Pagine del sito nuovo a cui puntano i link

In proposta i link sono ancore della home o `#`. Nel sito vero:
- **Prodotti**, con le quattro linee (Briko Line, Artelinea, Gli speciali, Altri prodotti) e le 96 schede; i link della fila delle scatole vanno alle schede.
- **Pagine per gesso**: Alabastrino, Scagliola, Polvere ceramica, Gesso bologna, Gesso murario (colonna "Gessi" del piede).
- **Schede tecniche e di sicurezza**: i 395 PDF esistono già (184 schede tecniche, 210 schede di sicurezza, 1 dichiarazione di prestazione).
- **Azienda**: la storia dal 1985, l'energia dal sole, il magazzino.
- **Dove siamo e Contatti**, con la mappa; meglio ancora una pagina "Dove trovarli" o "Diventa rivenditore".
- **Privacy** e **Cookie** (oggi "Privacy Policy" porta alla cookie e "Note legali" dà 404).
- **Newsletter: no**. Nardi non ha notizie, cataloghi, fiere datate o collezioni da annunciare, e i clienti comprano in negozio o ordinano per telefono. Il motivo è anche nella NOTA.

## Foto da rifare dal vero

Mezza giornata di still life basta per tutta la home:
- **La scatola protagonista**, una per famiglia (alabastrino, stucco cementizio, malta pronta, cemento rapido, colla per piastrelle) più il secchiello dell'ossido rosso: di tre quarti, come i rendering attuali, luce naturale morbida da sinistra, fondo carta color gesso chiaro (vicino a #F4F1EA), ombra vera a terra; almeno 2400 px di altezza. Oggi a 1440 la scatola è larga 415 px e il rendering più grande (784 px, già ingrandito 1,15x dal nativo 680) la regge a 1,9x sul retina. In alternativa, i file di stampa delle confezioni per rifare i rendering in grande.
- **La fila delle 12 scatole**: stessa luce e stesso angolo, una scatola per scatto, così si possono accostare.
- **I sei barattoli degli ossidi**: frontali, stessa altezza di camera; meglio ancora sei mucchietti di pigmento davanti ai barattoli.
- **Lo stucco sulla spatola** (oggi segnaposto Unsplash, senza didascalia in pagina: è l'unica foto non di Nardi e va sostituita prima di pubblicare): mani vere con una spatola e uno stucco Nardi, la scatola o il secchiello visibili accanto, fondo di parete chiara, luce laterale.
- **La facciata della sede** (per la pagina Azienda; in home non c'è più): dal basso, in verticale sul pilastro NARDI e sulle fasce lilla, con un cielo pulito e senza il piazzale in primo piano; almeno 2000 px di altezza (oggi la sorgente è alta 700 px).
- **Il magazzino** (oggi nella chiusura, sorgente 4272x2848 tagliata a 1752x1165): rifarlo con luce migliore, inquadratura frontale sui bancali Briko Line, senza cellophane lucido, almeno 3000 px di larghezza; meglio ancora una foto della produzione o del confezionamento.
- Diritti da chiarire: chi ha fatto i rendering delle confezioni e le foto "Q48A"; `slide-nardi-2.jpg` (betoniera) sembra di repertorio.

## Licenze

- **Caratteri**: Encode Sans (Impallari, Torresi, Le Bailly), Google Fonts, SIL Open Font License 1.1: uso commerciale libero, file serviti dal sito in `sito/fonts/`.
- **Foto di Nardi**: rendering delle scatole e dei barattoli e foto del magazzino, dalla libreria media di narditalia.com (`assets/originali/`). Appartengono all'azienda.
- **Segnaposto esterno**: una sola foto in pagina, Sasun Bughdaryan, Unsplash (Unsplash License, uso commerciale libero senza attribuzione obbligatoria); dettagli in `assets/CREDITI.md`. Va sostituita con la foto vera prima di pubblicare.
- Nessuna immagine generata dall'IA.

## Loghi

- Il logo esiste solo raster: in pagina c'è `logo-nardi-bianco-500x139.png` del sito tagliato sul disegno (436x100) e con la maschera ricolorata nel verde #276E59, a circa 3x in testata (129 px) e nel piede (146 px). Il verde del sito di oggi (#45a488) è stato scurito per il contrasto AA.
- Non è stato ricostruito in SVG: il corsivo "nardi" è a mano libera e senza il file originale non sarebbe fedele. Da chiedere all'azienda il logo vettoriale (AI, EPS, PDF o SVG).
