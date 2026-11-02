# Meccanica Masi: proposta di nuova homepage

Proposta non richiesta, solo la home. Non è pubblicata, l'azienda non è stata contattata.

## Cosa c'è

- `sito/index.html`: la home finale, statica, si apre con file:/// o da qualsiasi server. Immagini in `sito/img/` (WebP in più larghezze), caratteri in `sito/fonts/` (Mona Sans).
- `screenshot/home/`: `home-1440.jpg` (5850 px), `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`; `NOTA.md` spiega idea, scelte e controlli.
- `_prova/script/build_finale.sh` rifà tutto: immagini (`finale_img.py`), logo (`finale_logo.py`), pagina (`finale_html.py`), screenshot (`finale_shot.mjs`), controlli (`finale_controlli.mjs` e `segnali.sh`).
- `01-analisi.md`: fatti con le fonti, foto con i voti, direzioni; `_prova/home/a` e `b`: i due prototipi da cui nasce la finale.

## Dati da confermare con l'azienda

Nessuno di questi è in pagina come segnaposto; dove serve, la pagina usa solo ciò che il sito dice già.

- **1977**: in pagina c'è "A Padova dal 1977" nella chiusura, dopo la frase "Chi ci chiama parla con chi lavora..." (non più nella prima schermata), preso da "Fondata nel 1977" e "A PADOVA DAL 1977" del sito di oggi. Il sito dice anche 35 anni, 30 anni, "quasi 50" e "oltre cinquant'anni"; la srl è iscritta il 01/04/2019. Va chiesto di che officina è il 1977 e che legame c'è con "Masi Macchine Grafiche S.R.L." del logo precedente. Se non torna, si toglie la riga.
- **Permesso per la leva in apertura**: la foto della leva con settore dentato (appena fresata e verniciata) è il centro della pagina; la didascalia dice "Fresata CNC dal pieno, alesatura H7", come la scheda del progetto. Chiedere se il pezzo si può mostrare (sul sito è già pubblicato nei Progetti) e se il cliente va nominato o no.
- **Orari** lun-ven 8-18, sab 8-12: sono dell'officina o solo delle chiamate.
- **REA**: in pagina c'è REA PD-450853 (aziende.it, companyreports.it); il sito di oggi scrive "Iscr. Reg. Imp. n. 307590256". Confermare quale vale.
- **Capitale sociale (30.000 euro) e PEC (meccanicamasisrl@pec.it)**: presi da aziende.it, non dal sito. Non sono in pagina; si aggiungono alla riga legale del piede dopo la conferma.
- **Camin e Matteo**: la storia del fondatore a Camin e di Matteo che "ha raccolto l'eredità del padre" non è usata in home; va bene per la pagina Chi siamo dopo la conferma (anche se la sede storica è la stessa di via dell'Artigianato). Il cognome di Matteo non va scritto senza conferma.
- **Titolo "Pezzi dal pieno, su disegno"**: riassume le loro pagine ("lavorazione CNC dal pieno", "Pulegge dal pieno", "realizziamo qualsiasi pezzo su richiesta"); va bene se lavorano davvero quasi sempre su disegno del cliente. Se no: "Pezzi dal pieno, su misura" (dallo slider "lavorazioni CNC su misura").
- **Linea di spedizione giornali**: in pagina "su commessa di una delle principali aziende di produzione giornali del Veneto". Il sito dice anche "abbiamo progettato e installato"; il giudice ha chiesto di non scrivere "progettata" finché non si conferma. Chiedere se il cliente è citabile.
- **Supporto Man-Roland**: alluminio "6082 o 7075" e la verifica con macchina di misura tridimensionale (CMM): la CMM non è citata in home finché non si sa se è loro o di un fornitore.
- **Gruppi stampa completi e prodotti brevettati** (piede del sito e Lavora con noi): non citati finché non si sa quali.
- **Macchine**: modelli veri dietro i loghi Soraluce, Anselmi, Dahlih, Thomas, New Drill, Bosch; in home ci sono solo "6 torni, 1 a CNC" e "3 assi", come sul sito.
- **Telefono**: c'è solo il cellulare 348 169 34 51; chiedere se esiste un fisso.
- **Social e scheda Google**: nessun profilo vero (l'Instagram del sito porta a "#"); c'è un QR "recensioni Google" in libreria. Se esiste una scheda Google, si può aggiungere il link alla mappa con la scheda.
- **Logo**: in pagina c'è la sola scritta vettoriale "meccanica Masi SRL" del loro SVG del 2026, senza gli ingranaggi in 3D (sono immagini raster dentro l'SVG). Chiedere quale marchio vogliono tenere (scritta con ingranaggi o ingranaggio rosso rotondo) e un vettoriale del marchio rotondo.

## Foto: cosa rifare dal vero e come

Le foto vere reggono a metà (voti in `_prova/inventario-immagini.json`); la home ora usa solo foto loro, nessuna di repertorio. Il fondo della pagina (#E1E6DE) è il verde grigio del loro tappetino da banco schiarito: se le foto nuove si fanno su un altro fondo, conviene ripensare anche il colore della pagina.

1. **Leva appena fresata e leva verniciata** (apertura e interruttore): oggi due foto da telefono di due lati diversi, la grezza dall'alto su carta, la verniciata di tre quarti su un fondale grigio. In pagina sono come sono state scattate (nessuno specchio) e la didascalia dice "Lo stesso pezzo, visto da due lati". Da rifare in still life sullo stesso fondo (cartoncino verde grigio chiaro, circa #E1E6DE, senza pieghe), **stessa inquadratura per le due fasi**, vista dall'alto come la grezza di oggi, dentatura in basso; luce morbida da sinistra con un pannello bianco a destra, ombra corta; obiettivo 70-100 mm, diaframma 11, almeno 4000 px di lato lungo. Così il prima e dopo coincide al millimetro e l'interruttore diventa un vero confronto.
2. **Mandrino espansibile** (fascia a tutta larghezza): foto a 1200 px su banco scuro, a 1440 è ingrandita di 1,2 volte. Chiedere l'originale o rifarla dall'alto, pezzo intero, banco pulito, luce di finestra; orizzontale 2:1.
3. **Supporto Man-Roland e pulegge**: oggi su tappetino verde da banco con segni e riflessi; il supporto è tagliato a sinistra già nella foto. Rifare sullo stesso set della leva, pezzo intero con margine.
4. **Linea di spedizione giornali**: foto da telefono con grandangolo, ritagli di carta a terra (tagliati fuori). Se si torna dal cliente: inquadratura ad altezza d'occhio sulla curva a 90 gradi, pavimento pulito, luce del reparto.
5. **Interno della macchina da stampa** (pulegge e cinghie): bella ma caricata a 598 px. Chiedere l'originale a piena risoluzione (scattata il 05/07/2023 secondo il nome del file).
6. **Reparto**: mezza giornata con luce di finestra per la pagina L'officina (fresatrice CNC a 3 assi con un pezzo in tavola, un tornio con il truciolo, la piegatrice), inquadrature orizzontali larghe 3:1 o 2:1.
7. **Un rullo per offset o flexo finito**: manca del tutto ed è la loro lavorazione più richiesta; serve per la pagina Rulli per la stampa.

## Licenze

- **Mona Sans** (GitHub, distribuita da Google Fonts): SIL Open Font License 1.1, uso commerciale libero; file woff2 variabili (peso e larghezza) serviti dalla pagina in `sito/fonts/`.
- **Foto dell'azienda**: scaricate dalla libreria media pubblica del loro sito; uso nella proposta da confermare.
- **Foto di repertorio**: nessuna nella home (la fresatrice di Connor Lucock, Pexels, è stata tolta il 2 novembre 2026). Dettagli in `assets/CREDITI.md`.
- **Jost** (Google Fonts, SIL Open Font License 1.1): solo le tre lettere "SRL" del logo, convertite in tracciati dentro l'SVG; il file del carattere non è servito dalla pagina.
- Nessuna immagine generata dall'IA: le cinque immagini Gemini della loro libreria sono escluse.

## Loghi

- `sito/img/logo-masi-scritta.svg`: la scritta vettoriale del loro `logo-meccanica-masi-srl-modificato.svg` (Inkscape, 2026), tracciati originali, rosso #ED1C24 e nero #231F20, tolti gli ingranaggi raster, i metadati e i contorni bianchi; riquadro stretto sulla scritta. "SRL", che nell'originale era un testo in Futura Heavy (il browser lo mostrava in Times), è in tracciati presi da Jost 800 nella stessa posizione e corpo. Da sostituire con il vettoriale vero del marchio quando l'azienda lo manda.
- Usata in testata (112 px) e nel piede (136 px) e come icona della scheda.

## Pagine del sito nuovo a cui puntano i link

La home ha già i link; le pagine sono da fare.

- `chi-siamo.html`, `officina.html`, `lavora-con-noi.html`
- `lavorazioni/`: `rulli-per-la-stampa.html`, `tornitura.html`, `fresatura-cnc.html`, `lamiera.html`, `saldatura.html`, `manutenzione-sul-posto.html`, `installazione-macchine.html` (sette schede)
- `progetti/` (elenco) e otto schede: `leva-settore-dentato.html`, `supporto-rullo-man-roland.html`, `pulegge-dal-pieno.html`, `basamento-braccio-robotico.html`, `svolgitore.html`, `linea-spedizione-giornali.html`, `mandrino-espansibile.html`, `rullo-pinza-fondellatrice.html` (la home ne linka sette: il mandrino espansibile compare solo come foto con la didascalia)
- `privacy.html`, `cookie.html` (oggi `privacy-policy-2` e iubenda)
- Contatti punta alla chiusura della home (`#contatti`); Settori a `#settori`.

## Newsletter

Non c'è: lavorano su commessa per altre aziende, non hanno fiere, cataloghi, collezioni né clienti privati da tenere informati (il plugin Hostinger Reach è installato ma mai usato).
