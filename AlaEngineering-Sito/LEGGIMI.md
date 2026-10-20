# Ala Engineering: proposta di nuova home

Proposta non richiesta di una nuova homepage per ALA Engineering S.r.l. (Saonara, PD). Solo la home; nessun contatto con l'azienda, niente pubblicato.

## Dove sono le cose

- `sito/index.html`: la home finale (si apre con file:///). `sito/img/`: solo le immagini usate, JPEG in più larghezze e il logo PNG. `sito/fonts/`: Encode Sans (SIL OFL 1.1, licenza in `sito/fonts/OFL.txt`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, e `NOTA.md` (idea, schermate, caratteri, colori, interazione, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`finale_img.py`), pagina (`finale_pagina.py` dal modello `finale_home.html`, con le posizioni delle legende in `legende.json`) e screenshot (`finale_shot.mjs`); con `extra` anche i controlli a 320, 768, 1024 e 1920 in `_prova/controlli/`. `finale_stati.mjs` fotografa i cinque stati del selettore e prova la tastiera.
- `01-analisi.md`: fatti con le fonti; `assets/CREDITI.md`: licenze delle foto; `_prova/home/a` e `_prova/home/b`: i due prototipi (scelto A).

## Dati da confermare prima di pubblicare

In pagina c'è solo ciò che ha una fonte; queste cose sono rimaste fuori o vanno verificate.

- **ISO 9001** DNV C607235: il certificato pubblicato è scaduto il 26/06/2026. In pagina non c'è; se è stato rinnovato si aggiunge una riga nella sezione Azienda o nel piede.
- **Anno di fondazione**: 1994 (companyreports, Kompass, LinkedIn) o 21/04/2005 (fatturatoitalia). In pagina c'è solo "da oltre 30 anni", che è loro (`perch-sceglierci`): va bene così o preferiscono un anno?
- **Numeri**: 300/200/100/30 in home, "oltre 500" in home e nell'articolo Assodel, "più di 350 personalizzazioni" in `prodotti`. Nessuno è in pagina; quale è giusto oggi?
- **ALASUPPLY**: dati del selettore presi dalle pagine prodotto (ingresso, tensioni, correnti). ALASUPPLY-3FM: la pagina dice 5.000 W, il nome della foto 4000W; in pagina 5.000 W. Le sigle a catalogo sono tutte in produzione (ALASUPPLY, ALADC, ALAMULTI, ALABAT, ALASTAB, ALACONV 3.0 e 3.0 D, ALAEMERGENCY, ALABUFFER-M, ALAWIN, ALAGREEN, ALAEV-3FX)?
- **Nomi dei componenti nelle legende** (trasformatore, induttori toroidali, piastra di dissipazione, dissipatore alettato, condensatori elettrolitici, connettori dei segnali, etichetta di collaudo, morsetti, barre in rame, contenitore in alluminio): letti dalle foto, da far confermare all'ufficio tecnico.
- **Misure delle schede**: solo la ALASUPPLY-1FL ha le misure nella scheda tecnica (130 x 325 x 65 mm, 2,2 kg). Senza le altre non si può mostrare la scala vera: le cinque schede sono sullo stesso piano, con la stessa ombra e lo stesso punto di vista, ma ognuna riempie il suo riquadro. Con le misure (o con lo scatto nuovo, sotto) il selettore mostrerebbe anche quanto cresce la scheda con la potenza.
- **Clienti nominati** (Siemens, Enel, Fiamm, Carlo Gavazzi, Socomec, La Cimbali, DAB, Findus, Scame, Fracarro, Flaem, Cebi, Itelco, ROJ, PhysisPEB, Plug The Sun, Frecciarossa con RTI Ansaldo Breda / Bombardier): si possono nominare in home? La frase del cliente sugli "artigiani dell'elettronica" va bene in home?
- **"Da oltre 10 anni"** sui gasdotti europei: viene da un testo non datato della pagina dei rack.
- **"2021"** per le colonnine ALAEV-3FX e gli altri anni delle applicazioni: presi dalle date degli articoli; confermare che siano gli anni giusti.
- **Riga legale**: REA PD 354666 (solo registri non ufficiali), capitale sociale (15.500 euro solo da Kompass), PEC: non in pagina finché non arrivano confermati; poi vanno accanto alla P.IVA.
- **Orari** di apertura: non pubblicati, quindi non in pagina. Se li danno, una riga sotto l'indirizzo nella chiusura.
- **Referente**: chi risponde al telefono e alla mail? Nella chiusura si può aggiungere un nome.

## Pagine del sito nuovo (link della home e del piede)

`perche-sceglierci.html`, `progetti.html`, `news.html`, `download.html`, `lavora-con-noi.html`, `privacy.html`, `cookie.html`, `prodotti/alimentatori.html`, `prodotti/caricabatterie.html`, `prodotti/stabilizzatori.html`, `prodotti/convertitori-di-frequenza.html`, `prodotti/alimentatori-tamponati.html`, `prodotti/rack.html`, `prodotti/energie-rinnovabili.html`, `prodotti/schede-su-misura.html`. Il menu e "Parlateci del vostro prodotto" puntano alle sezioni della home (`#catalogo`, `#applicazioni`, `#contatti`). Esterni: LinkedIn, YouTube e la pagina vetrina LinkedIn sulle rinnovabili (gli unici profili che esistono), la mappa di Google.

**Newsletter**: non c'è, per scelta. Vendono solo ad aziende e su progetto, pubblicano tre o quattro news l'anno e il canale vivo è LinkedIn. Se in futuro vogliono mandare le schede tecniche nuove, si aggiunge nel piede un campo email con il consenso privacy, da collegare a un servizio (non funziona finché non si collega).

## Foto da rifare dal vero

Le foto loro sono vere ma a 1024 px, con il flash frontale; reggono come anteprima onesta, non come versione definitiva.

1. **Le cinque ALASUPPLY e le otto famiglie** (still life, una giornata): stesso fondo di carta chiara opaca (o bianco caldo, da portare a #F4F3EF), stessa inquadratura di tre quarti dall'alto a circa 30 gradi, **stessa distanza e stessa focale per tutte** (così la scala tra le schede è vera e il selettore mostra anche la crescita della scheda), luce laterale morbida da sinistra con un pannello di schiarita a destra, niente flash, ombra corta sul piano, diaframma chiuso (f/11-f/16) o fuoco a pila per avere tutta la scheda nitida, file da 6000 px. Prima la 3FH, che apre la pagina.
2. **Banco di collaudo** (mezza giornata): il tecnico al banco con le due file di schede, luce naturale o diffusa, **senza il poster** (nella foto attuale è stato tolto in fotoritocco solo per questa proposta: va dichiarato o rifatto), senza portatile e pannello attrezzi in vista, inquadratura orizzontale larga 5:4, file da 6000 px.
3. **Applicazioni**: il Frecciarossa e la seggiovia sono segnaposto Unsplash. Se esistono foto loro di un'applicazione installata (rack su una stazione del gas, convertitore in una cabina ENEL, caricabatterie di una seggiovia), vanno al loro posto; altrimenti servono il permesso dei clienti o foto fatte da loro.
4. **Diritti**: confermare che le foto dei prodotti e del laboratorio siano di Ala Engineering (o del loro fotografo) e si possano usare.

## Licenze

- **Encode Sans**: Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file in `sito/fonts/`, licenza in `sito/fonts/OFL.txt`.
- **Foto Unsplash** (segnaposto, da sostituire): Frecciarossa ETR1000 di Edoardo Bortoli (https://unsplash.com/photos/high-speed-train-on-railway-tracks-8l8viRGA7-Q) e seggiovia nella nebbia di Verstappen Photography (https://unsplash.com/photos/a-couple-of-ski-lifts-hanging-from-a-wire-WlM5jTXIgXM), Unsplash License: uso gratuito anche commerciale, senza obbligo di citazione. Dettagli in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.
- **Foto dei prodotti e del laboratorio**: dal sito alaengineering.it, presumibilmente di Ala Engineering (da confermare).

## Logo

Usato il PNG originale `assets/originali/logo-ala-600x180.png` (il più grande pubblicato), mostrato a 200 px nel piede e a 58 px di altezza nella testata, quindi nitido anche sugli schermi 2x. Non esiste un vettoriale nel codice né nei PDF, e la "A" pennellata non si ricostruisce fedelmente in SVG: **chiedere il logo vettoriale** (SVG, PDF o AI) e, se c'è, una versione a una sola tinta.

## Note di lavoro

- I PNG dei due prototipi in `_prova/home/a` e `_prova/home/b` (fino a 3 MB) sono rimasti dove li ha lasciati chi ha fatto i prototipi; si possono cancellare quando non servono più al confronto.
- Le scelte sui segnali da IA: `segnali.sh` dà 0 soglie da correggere e 0 da guardare (dettagli in `screenshot/home/NOTA.md`).
