# Solteco: proposta di nuova home

Proposta non richiesta di una nuova homepage (solo la home) per Solteco sas di Longhin Giuseppe & C., Vigonovo (VE). Non è pubblicata e l'azienda non è stata contattata.

## Dove sono le cose

- `sito/index.html`: la home finale, statica. Le immagini sono in `sito/img/`, i caratteri in `sito/fonts/` con la licenza.
- `screenshot/home/`: schermate a 1440 e 390 (intere e prima schermata) e `NOTA.md` con l'idea, le scelte e i controlli.
- `01-analisi.md`: i fatti con le fonti, il materiale visivo, le due direzioni e i riferimenti.
- `_prova/home/a/` e `_prova/home/b/`: le due bozze. Il committente ha scelto la B; la finale parte da lì.
- `_prova/script/build_finale.sh`: rifà immagini, pagina e schermate (`sh build_finale.sh tutte` scatta anche 320, 768, 1024 e 1920). La pagina si scrive in `finale_b_index.html` e le immagini si fanno con `finale_b_img.py`; `prova_interruttore_finale.mjs` prova il gesto con tastiera e dito, `largo_finale.mjs` cerca gli elementi che escono dalla finestra. Gli altri script `finale_img.py`, `finale_poly.py` e `finale_pagina.html` sono della versione sulla bozza A, scartata.
- `assets/CREDITI.md`: origine e licenza di ogni foto.

## Dati da confermare con Solteco prima di pubblicare

In pagina ci sono solo fatti con una fonte. Questi vanno comunque confermati:

1. **Frabo Adesivi**: che Solteco sia ancora agente di Frabo, per quale zona, e se si possono usare il nome Frabo e il marchio AquaGum® in pagina. Sul sito di Frabo Solteco non compare.
2. **Codici AquaGum**: P/030, P/031 LR, P/035 R, P/075 e CAT/1598 vengono dalla notizia del 24/01/2016 sul sito di Solteco; la scheda di P/030 (resistenza termica, riattivazione a bassa temperatura, suole e tomaie, primer, PVC e PU, 5 % di CAT/1598) viene dalla stessa notizia. Quali sono ancora in listino? Frabo oggi mostra anche "AQUAGUM NO FOG".
3. **Adesivi a solvente**: la pagina dice che Solteco tratta anche neoprenici e poliuretanici, perché la pagina Adesivi li elenca tra "le categorie di adesivi da noi utilizzate". Va confermato. Se non li tratta più, l'interruttore "Acqua o solvente" si toglie e resta la scheda di P/030.
4. **Come lavora Solteco**: in pagina c'è "segue il reparto sul processo d'incollaggio" e "ne porta gli adesivi in azienda e segue chi li usa", dal sito di oggi ("esperienza e consulenza", "servizio di consulenza"). Visite in reparto, prove, messa a punto delle macchine? Le macchine del processo (incollatrice a tre assi, tunnel cold-dry, riattivazione, pressa) sono di Solteco, dei clienti o di Frabo?
5. **Indirizzo**: in pagina c'è "Vicolo Amerigo Vespucci 12, 30030 Vigonovo (VE)", come nel registro e nel VIES; il sito di oggi scrive "Via Vespucci 12". Quale va mostrato, ed è una sede con magazzino o un recapito?
6. **Telefono**: c'è solo il cellulare 331 335 8858. Va bene in grande nella pagina? C'è un fisso? PEC non trovata.
7. **La persona**: Giuseppe Longhin? Da quando lavora nel settore (la "ventennale esperienza" del sito)? Vuole il nome e una foto in pagina? Oggi non ci sono.
8. **Clienti**: "molti brand a livello mondiale", senza nomi. Se ne può citare almeno uno, o un tipo di cliente?
9. **Fuori dalla pagina finché manca una fonte**: le frasi del sito attuale su salute ("non sono necessari esami clinici") e su risparmio energetico e di costi; la certificazione ZDHC di AquaGum citata da Frabo.
10. **Data di nascita**: in pagina "sas costituita a Vigonovo nel 2011" (companyreports.it: 24/02/2011; iscrizione 17/04/2012).

## Foto: tutte da rifare dal vero

Le tre foto in pagina sono segnaposto di Pexels (licenza "Free", vedi `assets/CREDITI.md`): non mostrano Solteco, i suoi clienti né i prodotti AquaGum. Prima di pubblicare vanno sostituite. Le foto del sito di oggi non si possono riusare: sono fotogrammi di un video, sotto 1027 px, con le scritte impresse, e i diritti sono da chiarire.

1. **Apertura, la macro della giunzione**: una scarpa finita di un calzaturificio cliente della Riviera (meglio una scarpa da città in pelle che uno scarponcino), il bordo dove la tomaia è incollata alla suola con AquaGum. Obiettivo macro, luce radente da un lato, fondo grafite opaco, scarpa ferma su un piano, almeno 6000 px sul lato lungo. Inquadratura orizzontale con la linea di colla nel terzo basso e spazio scuro in alto per il titolo; una seconda verticale per il telefono.
2. **Processo, la stesura**: in reparto, la colla stesa a pennello e quella spruzzata dall'incollatrice sul fondo della scarpa montata. Mani vere, luce di finestra, nessuna posa, fondo del reparto sfocato. Orizzontale 2:1 e un taglio quadrato.
3. **Adesivi, la colla come materia**: AquaGum fresca e lattiginosa sul fondo cardato o su un pezzo di cuoio, in still life su carta chiara o sul banco, luce morbida dall'alto. Meglio ancora il fondo con la griglia della spruzzatura, che è il soggetto più forte di Solteco (oggi esiste solo come fotogramma video). Panoramica 2,4:1 e un taglio quadrato.
4. Facoltative: il tunnel cold-dry, la pressa, la latta di AquaGum senza etichette in primo piano. Va anche chiesto a Frabo se ha foto di prodotto e di applicazione in alta risoluzione.

Una volta arrivate le foto, si mettono in `assets/` e si cambiano i percorsi in `_prova/script/finale_b_img.py`. Il trattamento (toni freddi spenti, neutri caldi, curva morbida, sfumatura sul grafite in apertura) resta lo stesso. Il punto della legenda in apertura si regola con `--x` e `--y` in `.legende`.

## Licenze

- Carattere: Host Grotesk (Element Type), Google Fonts, SIL Open Font License 1.1, uso commerciale consentito; testo in `sito/fonts/OFL.txt`. I file woff2 sono serviti dalla pagina.
- Foto: Pexels License (uso gratuito anche commerciale, attribuzione non obbligatoria; non si può rivendere la foto senza modifiche né far credere che le persone ritratte approvino un prodotto). Elenco completo in `assets/CREDITI.md`.

## Loghi

- In pagina il marchio di Solteco è scritto in testo ("Solteco sas"), perché il logo di oggi è un PNG da 179x53 px, azzurro con contorno e tre gocce. Serve il vettoriale, o va deciso se ridisegnarlo.
- Il logo di Frabo e il timbro "ISO 9001:2000" del sito di oggi non sono usati: sono del fornitore, e il timbro è superato (Frabo oggi è certificata UNI EN ISO 9001:2015). Per usare il marchio Frabo o AquaGum® serve il permesso di Frabo.
