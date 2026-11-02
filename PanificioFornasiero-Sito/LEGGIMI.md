# Panificio Galileo Fornasiero: proposta di nuova home

Proposta non richiesta di una nuova homepage per il Panificio Galileo Fornasiero S.r.l. di Camin (Padova). Solo la home. Non è pubblicata, l'azienda non è stata contattata.

## Versione 1 con l'uso

Il committente, viste le due versioni, ha scelto la versione 1 (`sito/`): grafica, caratteri, colori, impaginazione, la focaccia, il titolo e l'idea restano. Il 2 novembre sera le ho aggiunto, nel suo stile e con il minimo di cambiamenti a vista, quello che nelle prove della versione 2 serviva ai visitatori della scheda `_prova/uso/SCHEDA.md`. La versione 1 com'era prima è copiata in `_prova/versione-1-originale/` (sito, screenshot, script, LEGGIMI) per poter tornare indietro; la versione 2 resta in `sito-v2/` come promemoria.

Cosa c'è di nuovo (dettagli, misure e controlli in `screenshot/home/NOTA.md`):
- Prima schermata, telefono: la focaccia passa nel gradino a destra di "Siamo", il titolo resta su quattro righe; sotto, la riga su chi siamo, lo stato di adesso in grande (ora di Roma, festivi compresi), i due negozi con l'orario di oggi, l'eccezione della settimana (mercoledì pomeriggio, sabato, cellulare di via Alsazia), "Chiama" e "Mappa" ciascuno, e in stagione la riga delle prenotazioni di Natale o di Pasqua con "Come si prenota". Tutto nei primi 844 px a 390.
- Prima schermata, 1440: la stessa composizione con il titolo a 140 px invece di 145; sotto la F di "Fornasiero" la riga su chi siamo, lo stato, i due negozi affiancati; la riga delle Feste chiude la schermata. In testata "Per bar e ristoranti".
- Natale e Pasqua: come si prenota, pezzature e prezzi da chiedere, "Chiamaci e ordina: 049 870 26 58" e il numero di via Alsazia.
- Sezione nuova "Per bar, alberghi, ristoranti e rivendite": la fornitura, le consegne a domicilio, cosa chiedere, il telefono del laboratorio e la mail con oggetto "Fornitura pane" e traccia.
- Nelle schede dei negozi lo stato con lo stesso orologio e "chiedete al telefono" per sabato e domenica dove l'orario non è scritto.
- La foto di repertorio della chiusura ora ha "Foto indicativa" come quella della pasta.
- Nessun link a pagine che non esistono: storia e fornitura portano alle sezioni della home, Bacheca, Privacy e Cookie alle pagine del sito di oggi. Le pagine da fare restano quelle elencate sotto.
- Dato strutturato con i due negozi, CAP 35127 e orari.

Script: `_prova/script/build_finale.sh` rifà gli screenshot all'ora simulata lunedì 2 novembre alle 10 (con `--immagini` anche le immagini); `v1uso_prova.mjs` prova lo stato a 21 ore e giorni, la prima schermata, la riga delle Feste a date diverse, JavaScript spento, l'arrivo dai link, lo scorrimento orizzontale da 320 a 2560 e i collegamenti; `v1uso_misura.mjs` misura la prima schermata. Per vedere un'altra ora: `index.html?ora=2026-12-16T10:00`.

Da aggiornare in cima allo script della pagina, sotto "Da aggiornare con il panificio": `FERIE`, `FESTIVI`, `NATALE_DA`, `FINE_PRENOTAZIONI`, `SPEGNI` (oggi 1 novembre, 15 dicembre, 23 dicembre alle 13: date scelte nella proposta). Le finestre di Pasqua (dai 40 giorni prima, "chiamate per sapere" dai 7 giorni prima, fino al sabato alle 13) sono scritte nello script.

Da confermare con il panificio, per quello che questa versione mette a vista:
- Il sabato di via Vigonovese ("Sabato: chiamate"), le domeniche dei due negozi, le ferie, i festivi in cui chiudono (anche il 13 giugno, Sant'Antonio) e gli orari sotto Natale.
- Se via Alsazia 3 è ancora aperta, chi risponde al 338 660 06 64 e se su Google Maps c'è la scheda del negozio (i link mappa cercano "Panificio Fornasiero" con l'indirizzo; se la scheda non c'è, Google mostra comunque l'indirizzo).
- Le date delle prenotazioni di Natale e di Pasqua, se si possono dire pezzature e prezzi, e dove si ritira.
- Fornitura e consegne: zona, giorni, quantità minime; se le consegne a domicilio alle famiglie e il pane con il Mattino agli anziani si fanno ancora.
- Il consenso a usare in pagina la frase sugli operai della Stanga e della Snia Viscosa, detta al Mattino di Padova nel 2023, insieme a quello per le altre frasi e foto (vedi sotto).
- Il modulo "Gli avvisi di Romina" nel piede è rimasto com'era nella versione 1 e non invia nulla: o si collega a un servizio (vedi "Newsletter") o si toglie, come nella versione 2, e al suo posto va la riga "Le prenotazioni di Natale e di Pasqua si fanno al telefono".

Foto da rifare dal vero, per questa versione (oltre all'elenco "Foto da rifare dal vero" più sotto): i panini del mattino nei loro sacchetti bianchi con la scritta bruna, per la chiusura, al posto del repertorio con "Foto indicativa"; le tagliatelle e i bigoli sul banco infarinato, al posto del repertorio della pasta; la vetrina di via Alsazia 3, che oggi non ha nessuna foto; il laboratorio o le cassette della consegna per la sezione delle forniture, che oggi è solo testo.

## Dove sono le cose

- `sito/index.html`: la home finale, versione 1 con l'uso (statica, si apre con file:///). `sito/img/`: solo le immagini usate, WebP a più larghezze. `sito/fonts/`: Sentient e General Sans.
- Ultimo passaggio (2 novembre): apertura rifatta con la loro focaccia scontornata nel gradino del titolo, fondo mollica in apertura e nel piede, parte centrale ripulita. Cosa è cambiato e i controlli sono in `screenshot/home/NOTA.md`.
- `screenshot/home/`: screenshot a 1440 e 390 (intere e prima schermata), chiusura e piede a 1440, `NOTA.md` (idea, scelte, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`, che usa `scontorna_focaccia.py` per la focaccia dell'apertura) e screenshot (`finale_shot.mjs`); `prova_gesto.mjs` prova le schede dei negozi; `controlli.mjs` controlla lo scorrimento orizzontale da 320 a 2560 e i collegamenti; `trova_largo.mjs` cerca gli elementi che escono dalla pagina; `misura_apertura.mjs` misura titolo e focaccia.
- `01-analisi.md`: fatti con le fonti. `_prova/giudizio.json`: il giudizio sui prototipi. `_prova/home/a` e `b`: i due prototipi. `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Pagine che il sito nuovo dovrà avere (link del piede)

- `storia.html`: la storia dal 1963 (gli zii e il forno di Villatora del 1928, la bottega del 1963, le feste del 2013 e del 2023).
- `bacheca-di-romina.html`: la Bacheca di Romina (esiste già sul sito di oggi).
- `fornitura.html`: pane per bar, alberghi, ristoranti e rivendite, e le consegne a domicilio.
- `privacy-policy.html`, `cookie-policy.html`: da rifare (quelle di oggi citano Google Analytics Universal, che non esiste più).
- Il resto sono ancore della home: `#pane`, `#forno`, `#feste`, `#negozi`, `#forniture` (la riga sulle forniture e le consegne, sotto le schede dei negozi).

## Newsletter

"Gli avvisi di Romina" nel piede: una email quando si aprono le prenotazioni di Natale e Pasqua e quando arriva un dolce nuovo. Ha senso perché hanno clienti privati affezionati e notizie che tornano ogni anno. Oggi il modulo NON invia nulla: va collegato a un servizio (Brevo, Mailchimp o simili) con doppio consenso e registro dei consensi, e l'informativa privacy va aggiornata. Molti clienti sono anziani: il telefono resta il canale principale, per questo è il bottone dell'apertura.

## Da confermare con il panificio

In pagina oggi ci sono, presi dagli articoli pubblici del Mattino di Padova: i nomi di Galileo e Fidalma ("Galileo Fornasiero è arrivato a Camin il primo aprile del 1963. Fidalma è al banco da sessant'anni."), la foto della vetrina con loro due e le due citazioni di Galileo. Filippo, Romina come figlia e Michele Daniele NON sono in pagina (Romina compare solo come autrice della Bacheca e degli avvisi, come sul sito di oggi). Il resto dell'elenco non è scritto in pagina finché non arriva la risposta.


- Se si può usare come titolo la frase di Galileo al Mattino di Padova del 2013, "Siamo Fornasiero, fornai anche nel nome", e nella chiusura "Non abbandonerei mai Camin, qui è la mia famiglia, il mio mondo, il mio lavoro.".
- Il permesso di usare la foto della vetrina con Galileo e Fidalma e i loro nomi in pagina, e come vogliono essere nominati gli altri (Filippo, Romina, Michele Daniele) se li vogliono in pagina. Chi guida oggi la bottega.
- La focaccia dell'apertura: è la loro focaccia veneta delle Feste (foto del dicembre 2020); la didascalia dice "La focaccia delle Feste, con la glassa e le mandorle". Confermare il nome che usano al banco (focaccia veneta, focaccia di Natale, di Pasqua) e che le mandorle ci sono sempre.
- Il sabato di via Vigonovese (sul sito non è scritto: la pagina dice "Oggi meglio chiamare" nella scheda e, fuori orario, "Il sabato mattina via Alsazia 3 è aperta" senza dire nulla di via Vigonovese), le domeniche, le chiusure per ferie.
- Se il negozio di via Alsazia 3 è ancora aperto e chi risponde al 338 660 06 64.
- "Oltre 30 tipologie di pane": il sito ne elenca 20. Quali si fanno ogni giorno.
- La forma di maggiolini, stivaletto, zoccoletto e ciopeta (nella galleria non hanno il nome; in pagina c'è solo la foto delle tartarughe, l'unica certa).
- Se la ricetta di Galileo vale anche per colomba e focaccia di Pasqua (il sito lo dice solo per il Natale; in pagina è scritto solo per il Natale).
- Le date delle prenotazioni di Natale e Pasqua da scrivere in pagina.
- Fornitura a bar, alberghi e ristoranti e consegne a domicilio: zona, giorni, se il servizio "pane e Mattino" esiste ancora.
- REA (companyreports dice PD 235130, non è sul sito: serve una visura), PEC e capitale sociale per la riga legale. Oggi nel piede ci sono solo ragione sociale, indirizzo e P.IVA 02506350285.
- La pagina Facebook trovata in ricerca è loro e attiva? Su Instagram pubblicano ancora le ricette? Nel piede oggi c'è solo Instagram.
- Se vogliono la newsletter e con quale servizio.

## Marchio e logo

- Nel piede c'è il loro logo a cesto (PNG del sito, 667x579) reso a una tinta nel bruno delle scritte del sacchetto, 120 px a vista (sotto, la scritta del disegno non si legge), PNG a 2x e 3x. Non è ricostruito in SVG: il disegno originale è a colori con ombre e non si rifà fedele.
- Da chiedere quale sia il marchio ufficiale (il logo a cesto, l'insegna di legno "FORNASIERO Galileo" o la scritta del sacchetto) e se esiste un file vettoriale. Nella testata c'è la parola "Fornasiero" composta in Sentient, non un logo.

## Foto da rifare dal vero

Una mattina di riprese in luce naturale di finestra, senza flash, sempre con la stessa luce:
- Apertura: la focaccia di oggi è una loro foto del 2020 scontornata con un programma; il bordo in basso a sinistra, dove appoggiava sull'etichetta, è ricostruito a mano e un po' squadrato. Per il sito vero: la focaccia (o la tartaruga) fotografata dall'alto, a perpendicolo, su un foglio di carta o di stoffa uniforme del giallo della mollica o bianco, con almeno metà del diametro di fondo libero tutto intorno, luce da sinistra, file grande (almeno 4000 px sul lato lungo). Così lo scontorno è pulito e l'ombra è vera.
- I cinque pani dai nomi di casa (maggiolini, tartaruga, ciopeta padovana, stivaletto, zoccoletto), uno per foto, dall'alto, senza cesto, pangrattato e sessola di plastica: servono per dare un volto alla lista della sezione del pane.
- La tartaruga nel cesto di oggi ha la luce mista (lampada gialla e finestra): va rifatta con la sola luce di finestra, con il sacchetto della bottega dietro come ora.
- La vetrina e l'insegna di legno da marciapiede, di mattina, con Galileo e Fidalma sulla porta, ad alta risoluzione (quella di oggi è 640x319 e non si può ingrandire).
- Pasta fresca (oggi è un segnaposto Unsplash con "Foto indicativa"): le loro tagliatelle e i bigoli all'uovo sul banco infarinato, larga, dall'alto.
- Chiusura (oggi è un segnaposto Unsplash): il banco di via Vigonovese alle 7 o i panini del mattino nei loro sacchetti bianchi con la scritta bruna, quasi quadrata, chiara e calda.
- Natale e Pasqua: le foto di oggi reggono; per la versione vera il panettone e la colomba sul sacco di juta del cinquantesimo, dall'alto, con più aria intorno.
- Le tagliatelle su ardesia e le crostate con il prosecco del sito di oggi: chiedere se sono foto loro (non usate in home).

## Licenze

- Caratteri: Sentient e General Sans, Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito), file serviti dalla pagina.
- Foto: Unsplash T6vI65xwoNA (Karen Sewell, tagliatelle) e Unsplash ytxRXkY8QE4 (Victoria Nazaruk, panini nei sacchetti), Licenza Unsplash. Sono segnaposto da sostituire prima di qualsiasi uso pubblico. Pexels 4198047 e Unsplash W0PDHT_sYoQ, usate nella versione precedente, non sono più in pagina. Le altre foto in pagina sono del panificio, prese dal loro sito. Dettagli in `assets/CREDITI.md`.
- Le foto della libreria di Wix presenti sul sito di oggi non sono usate (licenza valida solo dentro Wix).

## Versione 2 (scheda d'uso)

Una seconda home, costruita sulla scheda d'identità e d'uso `_prova/uso/SCHEDA.md` (2 novembre 2026): prima l'uso, poi l'identità, poi l'esecuzione. La home precedente in `sito/` resta com'è.

- `sito-v2/index.html` (statica, si apre con file:///), `sito-v2/img/` (solo foto del panificio, WebP), `sito-v2/fonts/` (Josefin Sans e Fira Sans, SIL Open Font License 1.1; Erode, ITF Free Font License).
- `screenshot/home-v2/`: screenshot a 1440, 390, 320, 768, 1024, chiusura, e `NOTA.md` (cosa è cambiato dopo le prove, cosa trova ogni visitatore e dove, caratteri e colori, foto, controlli, cose da confermare).
- `_prova/uso/script/build_v2.sh` rifà tutto: immagini (`v2_img.py`), screenshot (`v2_shot.mjs`) e prove d'uso (`v2_prova.mjs`: stato a 26 ore e giorni, festivi compresi, prima schermata a 390 e 320, Feste a date diverse e con JavaScript spento, arrivo dai link, scorrimento orizzontale); `v2_misure.mjs` misura le sezioni, `v2_largo.mjs` trova gli elementi che escono dalla pagina. Le prove dei clienti tipo sono in `_prova/uso/prova-prima-0`, `-1`, `-2`.

In breve: a 390 la prima schermata è la vetrina con l'insegna e la didascalia "Via Vigonovese 116, vicino al semaforo", "Panificio Fornasiero, a Camin dal 1963", lo stato di adesso calcolato sull'ora di Roma e sui festivi ("Aperti ora tutti e due i negozi, fino alle 13.45.", "Oggi è festa: chiamate prima di passare."), i due negozi con l'orario di oggi e l'eccezione della settimana (mercoledì pomeriggio, sabato, il cellulare di via Alsazia), "Chiama" e "Mappa" ciascuno, e in stagione la fascia delle prenotazioni con il bottone per chiamare. Da 680 px la vetrina sta intera a misura nativa su un passe-partout, centrata, con lo stato e i due negozi sotto. Seguono le Feste (fuori stagione scendono dopo il pane), il pane, Chi siamo, Forniture e consegne, la Bacheca di Romina, "Vieni a trovarci" con i due negozi e gli orari della settimana, il piede. Tre caratteri con un compito fisso: Josefin Sans per la voce dell'insegna, Erode per i titoli, Fira Sans per testo e dati. Su richiesta del committente (più accoppiate di caratteri, misure e impaginazioni mescolate) ogni sezione ha un impianto diverso dalla precedente: apertura centrata, fascia a tutta riga, Feste con la foto a filo del bordo sinistro, il pane come una lavagna (i cinque pani padovani a 80 px su tutta la larghezza, la foto delle tartarughe a filo del bordo destro), Chi siamo centrato con la frase di Galileo a 58 px da sola e le date a 96 px, forniture in due colonne disuguali, Bacheca piccola e centrata, "Vieni a trovarci" a 96 px con i negozi accanto. Prima schermata, telefoni, orari e bottoni non sono stati spostati né rimpiccioliti. Scala e motivi in `screenshot/home-v2/NOTA.md`. Per provare un'altra ora: `index.html?ora=2026-12-08T10:00`.

Dopo le prove del 2 novembre (dettagli in `screenshot/home-v2/NOTA.md`): festivi e ferie nello stato, eccezioni della settimana sempre in prima schermata, "Chiama" in testata, fascia delle Feste con il numero e senza "adesso", "Negozi e orari" che arriva sugli orari, mail delle forniture in chiaro, prima schermata a 1440 rifatta sulla vetrina, citazioni del giornale da sei a due, quattro foto in meno, nessun link a pagine che non esistono, niente modulo degli avvisi.

Da aggiornare nello script della pagina (in cima, sotto "Da aggiornare con il panificio"): `FERIE` (le chiusure per ferie), `FESTIVI` (se chiudono anche altri giorni o tengono aperto in qualcuno), `NATALE_DA`, `FINE_PRENOTAZIONI` e `SPEGNI` (le date delle prenotazioni di Natale, oggi 1 novembre, 15 dicembre e 23 dicembre alle 13, scelte nella proposta).

Pagine che il sito nuovo dovrà avere: per ora la home non punta a nessuna pagina nuova. La Bacheca di Romina, la Privacy e i Cookie puntano alle pagine del sito di oggi (`/bacheca-di-romina`, `/privacy-policy`, `/cookie-policy`); "Chi siamo" e "Forniture e consegne" sono ancore della home (`#storia`, `#forniture`; le altre sono `#apertura`, `#chiama`, `#feste`, `#pane`, `#forno`, `#bacheca`, `#negozi`). Quando ci saranno, le pagine da fare sono: la storia dal 1928 di Villatora al 1963 di Camin e alle feste del 2013 e 2023 (lì può andare la frase sugli operai della Stanga con la fonte), la fornitura per bar, alberghi, ristoranti e rivendite, e Privacy e Cookie rifatte (quelle di oggi citano Google Analytics Universal, che non esiste più).

Newsletter: no in questa versione. "Gli avvisi di Romina" sono tolti: era un modulo che non inviava nulla, e i loro clienti prenotano al telefono e al banco. Al suo posto, nel piede, la riga "Le prenotazioni di Natale e di Pasqua si fanno al telefono: 049 870 26 58. Per sapere quando si aprono, seguiteci su Instagram." Se il panificio la vuole, va rimessa collegata a un servizio (Brevo, Mailchimp o simili) con doppio consenso, registro dei consensi e informativa aggiornata.

Da confermare con il panificio (dettagli in `screenshot/home-v2/NOTA.md`): il sabato di via Vigonovese, le domeniche, le ferie, i festivi (anche il 13 giugno) e gli orari di Natale; se via Alsazia 3 è aperta, chi risponde al 338 660 06 64 e se su Google Maps c'è la sua scheda; le date delle prenotazioni di Natale e Pasqua, pezzature, prezzi e dove si ritira; il consenso a usare le loro foto, la foto con Galileo e Fidalma, i loro nomi e le due frasi dette al Mattino di Padova; la ricetta di Galileo anche per Pasqua; "più di 30 tipi di pane"; zona e giorni della fornitura e delle consegne alle famiglie; il marchio e un vettoriale; REA, PEC e capitale sociale; Instagram e Facebook; se vogliono avvisi per email.

Foto da rifare dal vero per questa versione (una mattina, luce di finestra, niente flash); servono anche a riportare le foto oltre un terzo della pagina, oggi al 17 % perché le foto vere che reggono sono poche:
- la vetrina e l'insegna da marciapiede, di mattina, con chi sta al banco sulla porta, larga e ad alta risoluzione (quella di oggi è 640x319 e resta piccola anche a 1440); anche la vetrina di via Alsazia 3, che oggi non ha nessuna foto e non ha una riga che la descriva;
- le tartarughe e gli altri pani dai nomi di casa, uno per foto, nel loro sacchetto, senza pangrattato e sessola di plastica, con la sola luce di finestra;
- il banco con i panini imbottiti e i pani per bar e ristoranti nelle cassette o nei sacchi della consegna, per la sezione delle forniture, che oggi è solo testo;
- i dolci della Bacheca sul banco, con la stessa luce, al posto delle foto da telefono;
- panettone, focaccia e colomba sul sacco del cinquantesimo con più aria intorno (quelle di oggi reggono).
