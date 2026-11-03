# Home "Recinzioni e cancelli, dalla vendita alla posa": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, screenshot con `pro_shots.mjs` e `pro_shots.py`, controlli con `pro_controlli.mjs`; con l'argomento `tutte` anche 320, 768 e 1024). La versione di prima ("La rete ondulata la facciamo noi") è copiata com'era in `_prova/versione-1-originale/` (pagina, immagini e screenshot).

Screenshot in questa cartella (ora simulata lunedì 2 novembre 2026, 10.00, quindi "Aperto ora"): `home-1440.jpg` (10015 px), `home-1440-prima-schermata.jpg` (1440 x 900), `home-390.jpg` (14465 px), `home-390-prima-schermata.jpg` (390 x 844), `chiusura-1440.jpg` (richiesta e piede).

## L'idea

Prima l'uso, poi l'identità, poi la forma. La scheda d'uso (`_prova/uso/SCHEDA.md`) dice chi apre il sito: il privato con la casa nuova, al telefono la sera (preventivo); l'impresa in furgone (è aperto adesso? che cosa tengono? come arrivo?); il tecnico al computer (Betafence, altezze, dove mando il disegno). La home risponde a tutti e tre nella prima schermata e poi si apre come un sito di servizi tecnici (famiglia S): testata fissa con il telefono come bottone, apertura con mestiere, luogo, prova e azioni, indice dei tre usi più il banco, preventivo in tre passi, lavori, prodotti in schede con foto loro, aziende e Betafence, banco, dove e orari, chi siamo con i numeri, chiusura con il telefono grande e il modulo, piede in quattro colonne.

Identità: le loro parole e il loro tono al "noi" e al "voi" ("Offriamo un servizio completo", "dalla più semplice ed economica a quella più complessa", "Per un preventivo senza impegno, vi invitiamo a contattarci", "Facilmente raggiungibile da corso Stati Uniti..."), il loro marchio (rombo di rete azzurra e F verde), il loro verde come colore delle azioni e l'antracite dei loro lavori in alluminio come colore dei blocchi scuri. Nessun gioco di parole, nessun campionario interattivo, nessun disegno al posto delle foto.

## La pagina, in ordine

1. **Testata fissa** (88 px a 1440, 72 a 390): marchio, "Recinzioni Formentin / Villatora di Saonara" (a 390 solo "Formentin", sotto i 380 px solo il marchio), Prodotti, Lavori, Aziende, Attrezzature edili, Dove siamo, l'email (da 1400 px) e il bottone "049 760801". Finché i bottoni dell'apertura sono in vista il bottone della testata è bordato, poi diventa verde pieno: un solo verde pieno alla volta. Sotto i 1180 px il menu va nel bottone "Menu".
2. **Apertura**: a 1440 testo a sinistra e il loro cancello scorrevole antracite (`canc082204`) a destra, 600 px CSS. Occhiello "Villatora di Saonara (PD)", H1 "Recinzioni e cancelli, dalla vendita alla posa" (64 px), "Dai primi anni Settanta, rivenditori e installatori ufficiali Betafence. La posa la esegue anche il nostro personale.", bottoni "Chiama 049 760801" e "Manda foto e misure" (email con oggetto e traccia), stato "Aperto ora, fino alle 12.00" con "Mappa", indirizzo ed email. A 390 la foto va in cima a tutta larghezza (293 px), poi lo stesso testo, i due bottoni a tutta larghezza e lo stato: tutto in 818 px.
3. **Indice su antracite**: Per la casa, Per le aziende, Per gli impianti sportivi, Per le imprese (con cinque categorie del banco). A 1440 comincia a 774 px, dentro la prima schermata.
4. **Come chiedere il preventivo** (grigio zinco): tre passi numerati (foto e misure, vi richiamiamo, venite a vedere i modelli; "Preventivo gratuito, previo appuntamento"), "Manda foto e misure", "Chiama", "Oppure compilate la richiesta".
5. **Lavori recenti** (antracite): sei lavori loro in alluminio, 4:3, con il nome del lavoro (a 390 i primi quattro), poi "Volete vedere i modelli dal vero? L'esposizione è in sede, su appuntamento." con "Appuntamento 049 760801" e "Indicazioni stradali".
6. **Prodotti** (bianco): sei schede con la foto loro, tutte cliccabili: Recinzioni in alluminio, Cancelli carrai e pedonali, Ringhiere parapetti e inferriate, Rete metallica e pali (portano al modulo con il tipo di lavoro già scelto), Betafence per aziende e impianti sportivi (porta alla sezione aziende), Attrezzature edili e ferramenta (porta al banco).
7. **Aziende, condomini, impianti sportivi**: "Rivenditori e installatori ufficiali Betafence", tabella dei sistemi (Securifor 2,0 e 2,4 m, su ordinazione 3,0; Nylofor; Decofor; maglia sciolta Extra Forte; ForFence), riquadro "Mandateci il disegno" con i dati che servono e l'email con la traccia per l'azienda; fascia Betafence, ForFence, EN 13241-1 con la didascalia.
8. **Attrezzature edili e ferramenta al banco** (grigio): dodici categorie, "Si eseguono lavori di carpenteria e lavorazione di grigliati elettrosaldati", riquadro con lo stato, gli orari, "Chiama" e "Indicazioni stradali".
9. **Dove siamo**: indirizzo grande, come arrivare, "Indicazioni stradali" e "Apri la mappa"; tabella degli orari con il giorno di oggi in verde e lo stato; telefono, cellulare, email.
10. **Chi siamo** (antracite): la frase della pagina Azienda e quattro numeri in azzurro a 96 px (50+ anni, 4 materiali, 3 usi, 3,0 m).
11. **Richiesta** (grigio): "Chiamateci o scriveteci", il telefono a 96 px, cellulare, email, orari; modulo che compone l'email.
12. **Piede** (antracite): marchio e riga, Prodotti, Orari, Contatti; riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie.

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività", e per le foto "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia S (servizi tecnici e imprese), struttura A1 adattata: le recensioni, la squadra e le zone servite non ci sono perché non sono nelle fonti (vedi LEGGIMI). Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 (`riferimenti.jpg` e i file `-390`), le pagine intere di Kline e Wilson a pezzi; confronto con la colonna di destra di `_invio/zona/home/livello-professionale.jpg` e le note di Unicar e Fornasiero.

Dalla versione 1 tengo: i colori del marchio (azzurro #5A94F7 e verde #08B508 nel marchio, il verde scurito per le azioni), il carattere Geologica (una sola famiglia), il marchio ridisegnato, le foto loro dei lavori in alluminio, il telefono e l'email con i loro numeri. Tolgo: il titolo "La rete ondulata la facciamo noi" (la scheda d'uso lo indica come prodotto di nicchia e registro da grafico), il campionario di maglie disegnato in SVG, la foto Pexels della chiusura, la calce beige, il verde petrolio #0B5A4C, le due foto della rete ondulata in apertura di sezione.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs <cartella>` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 1280, 1024, 768, 390 e 320.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky 88/72 px, bottone "049 760801" alto 48 px; a metà pagina, a 1440 e a 390, il bottone si vede e si tocca (`elementFromPoint`). 12 link `tel:`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 "Recinzioni e cancelli, dalla vendita alla posa", occhiello "Villatora di Saonara (PD)", prova "Dai primi anni Settanta, rivenditori e installatori ufficiali Betafence", "Chiama 049 760801". A 390 il bottone è largo quanto la colonna (350 px) e alto 56; a 390 si vedono anche "Manda foto e misure", lo stato e "Mappa".
3. **Immagine vera nell'apertura: passa, con riserva.** È un loro lavoro (`canc082204`, cancello scorrevole e recinzione antracite) e non un oggetto scontornato; ma non mostra persone, mezzi o la sede, e il file è di 800 px (a 1440 è a 600 px CSS, 1,33x). La foto da fare è nel LEGGIMI.
4. **Zero repertorio: passa.** "indicativ" 0 volte; nessuna immagine da `assets/esterne`, Unsplash o Pexels; in `sito/img/` solo foto loro e il marchio.
5. **Foto in serie: passa.** 13 foto, un solo formato (4:3), stesso trattamento in `pro_img.py` (chiari compressi sopra 200, colore 0,9, contrasto 1,04); nessuna didascalia: le righe sotto i lavori e le schede sono i loro nomi, non didascalie. Restano foto da telefono di giorni e luci diverse: la serie vera la fa la giornata di foto del LEGGIMI.
6. **Palette dal marchio: passa.** Colori: `--verde` #0A7A32 (F del marchio, scurito: 5,5:1 sul bianco), `--verde-scuro` per il passaggio del mouse, `--azzurro` #5A94F7 (rete del marchio, solo cifre grandi e frecce su antracite), `--antracite` #2B3134 (il colore dei loro lavori in alluminio); neutri bianco, grigio zinco #EEF1F2, grigi di testo e filetti. Nessun colore scritto fuori da `:root` (a parte i due colori del marchio dentro l'SVG). Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 96) e 7 a 390 (14, 17, 20, 24, 30, 36, 44); testo corrente 19 px a 1440 e 17 a 390; niente sotto i 14 px; H1 64/36, H2 48/30.
8. **Due famiglie al massimo: passa.** Una: Geologica 400 e 700, anche per campi e bottoni.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 768-1023, 1 al telefono), sei schede con la foto loro in 4:3, nome a 23 px, riga e link; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono i numeri (50+ anni, 4 materiali, 3 usi, 3,0 m) e la fascia dei fornitori con la didascalia (Betafence, ForFence, EN 13241-1). Mancano le recensioni (le frasi trovate sono copie da directory, da ricontrollare su Google Maps e da usare solo con il permesso: LEGGIMI) e i clienti con il nome (nessuno nelle fonti). Non inventati.
11. **I lavori hanno un nome: non passa.** Sei lavori con il nome del lavoro, ma senza luogo né anno (non sono nelle fonti), e le foto sono di 800 px: a 405 px CSS per restare nitide, non a metà pagina. Da chiedere (LEGGIMI).
12. **Ritmo a blocchi: passa.** Tre blocchi antracite oltre al piede (indice, lavori, chi siamo) e tre grigi (preventivo, banco, richiesta); sezioni a 120 px a 1440 e 64 px a 390; margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato, raggio 4 px, 56 px (48 in testata), testo 17 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa in parte.** Modulo in home con tipo di lavoro, comune e via, metri lineari, altezza, cancelli, quando serve (urgenza), descrizione e la riga sulle foto (un mailto non porta allegati: si allegano nella mail che si apre); controllo di nome, telefono e indirizzo. Nessun iframe di mappa. Manca l'elenco dei comuni serviti: la zona di posa non è nelle fonti (LEGGIMI).
15. **Piede completo: passa in parte.** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA (da atoka, da confermare), indirizzo che apre la mappa, telefono, cellulare ed email cliccabili, orari, Betafence, Privacy e Cookie. Mancano le zone servite (come al punto 14).

### Compiti della scheda d'uso

- *Privato, 390 x 844*: senza scorrere la foto di un loro cancello e recinzione, "dalla vendita alla posa", "Villatora di Saonara", "Chiama 049 760801" (`tel:+39049760801`, 350 x 56) e "Manda foto e misure" (`mailto:` con oggetto "Preventivo recinzione" e la traccia: nome, telefono, indirizzo, metri, altezza, cancelli, "Allego le foto"). Con uno scorrimento i tre passi del preventivo (y 1122) e la mail (y 1673), con "Preventivo gratuito, previo appuntamento". Con due scorrimenti quattro lavori loro (y 2507). "L'esposizione è in sede, su appuntamento" e "Indicazioni stradali" subito sotto i lavori.
- *Impresa, 390 x 844*: lo stato nella prima schermata, giusto a lunedì 10.00 ("Aperto ora, fino alle 12.00"), lunedì 12.30 ("Chiuso ora, riapre alle 13.30"), venerdì 18.00 ("riapre lunedì alle 8.00"), sabato ("su appuntamento, chiamate prima"), domenica e festivi nazionali con Pasquetta. "Mappa" con un tocco nella prima schermata, "Indicazioni stradali" (navigazione verso via Lombardia 17) nel banco e in Dove siamo. "Per le imprese" con cinque categorie nell'indice (y 3275, entro tre scorrimenti) e la sezione del banco con dodici categorie dal menu.
- *Tecnico, 1440 x 900*: telefono ed email in testata e nell'apertura; "rivenditori e installatori ufficiali Betafence" nell'apertura e nell'indice "Per le aziende" e "Per gli impianti sportivi"; nella sezione aziende i sistemi con le altezze, "Mandateci il disegno" con i dati che servono (metri lineari e altezza, accessi, indirizzo, referente) e l'email con oggetto "Richiesta per azienda o impianto sportivo"; "La posa in opera è eseguita anche da nostro personale".
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione in testata e apertura; zoom permesso.

### Caratteri e licenze

- **Geologica** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile `sito/fonts/geologica-latin-var.woff2` servito dalla pagina, licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, cifre tabellari per numeri e orari.
- Foto: solo materiale del loro sito (gallerie e libreria media), da usare con il loro permesso e, per le case riconoscibili, con quello dei clienti. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

| In pagina | File d'origine (`assets/originali/`) |
|---|---|
| Apertura | `gallery_cancelli_canc082204.jpeg` |
| Lavori | `canc082201`, `canc082202`, `canc082203`, `ringh082202`, `ringh082203`, `canc082206` |
| Schede | `ringh082201` (alluminio), `canc082207` (cancelli), `gallery_ringhiere_img_1061.jpg` (ringhiere), `gallery_reti-ondulate_IMG_1130-1.JPG` (rete), `uploads_2016_01_20151223_103842n.jpg` (esposizione Betafence), `uploads_2014_04_IMG_1135.jpg` (banco) |

Ogni foto ha la versione da 400 px e quella da 700-800 px con `srcset` (a 1440 le schede sono a 405 px CSS: 2x).

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-9, 12 e 13 superate nelle misure; 10 e 11 no; 14 e 15 in parte (mancano i comuni). Compiti d'uso, collegamenti, ancore, larghezze, errori di script: tutti a posto.
- Collegamenti: `tel:+39049760801`, `tel:+393357740278`, `mailto:info@recinzioniformentin.it` con oggetto (e traccia dove serve), Google Maps `search` su "Recinzioni Formentin, Via Lombardia 17, 35020 Saonara PD" e `dir` su "Via Lombardia 17, 35020 Saonara PD".
- Modulo: invio vuoto fermato con l'avviso e il fuoco sul nome; con i campi pieni compone `mailto:` con oggetto "Preventivo: <tipo>" (letto nella prova, non aperto); le schede scelgono il tipo di lavoro.
- Menu a 390 aperto e chiuso dopo il tocco su una voce.
- Screenshot guardati a pezzi a 1440 e a 390, pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
- Niente newsletter e niente social: nessun profilo trovato, e una recinzione si compra una volta ogni vent'anni.
