# Home "Recinzioni e cancelli, dalla vendita alla posa": nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, screenshot con `pro_shots.mjs` e `pro_shots.py`, controlli con `pro_controlli.mjs`; con l'argomento `tutte` anche 320, 768 e 1024). `largo.mjs` trova gli elementi che escono dalla larghezza. La versione di prima ("La rete ondulata la facciamo noi") è in `_prova/versione-1-originale/`.

Screenshot in questa cartella (ora simulata lunedì 2 novembre 2026, 10.00, quindi "Aperto ora"): `home-1440.jpg` (10668 px), `home-1440-prima-schermata.jpg` (1440 x 900), `home-390.jpg` (12856 px), `home-390-prima-schermata.jpg` (390 x 844), `chiusura-1440.jpg` (richiesta e piede).

## L'idea

Prima l'uso, poi l'identità, poi la forma. La scheda d'uso (`_prova/uso/SCHEDA.md`) dice chi apre il sito: il privato con la casa nuova, al telefono la sera (preventivo); l'impresa in furgone (è aperto adesso? che cosa tengono? come arrivo?); il tecnico al computer (Betafence, altezze, dove mando il disegno). La home risponde a tutti e tre nella prima schermata e poi si apre come un sito di servizi tecnici (famiglia S).

Identità: le loro parole e il loro tono al "noi" e al "voi", il loro marchio (rombo di rete azzurra e F verde), il loro verde come colore dei blocchi pieni e delle azioni, l'azzurro della rete per le cifre e i filetti sui blocchi scuri, l'antracite dei loro lavori in alluminio. Nessuna foto di repertorio, nessun disegno al posto delle foto.

## Ritocco del 3 novembre (controllo del livello professionale, voto 6)

Fatto, in ordine di peso:
- **Fascia delle quattro garanzie** in fondo all'apertura, con le loro parole: "Preventivo gratuito", "Posa del nostro personale", "Ampia esposizione in sede", "Betafence ufficiale". A 1440 è dentro la prima schermata (y 700-825), a 390 è una griglia 2x2 con i soli titoli.
- **La prova si vede da sola**: un riquadro verde pieno sopra l'angolo della foto, "50+ anni di mestiere, dai primi anni Settanta" (il gesto del voto di Kline, con l'unico numero vero che hanno). La riga sotto il titolo ora parla al privato ("Recinzioni in alluminio, cancelli e ringhiere per la casa, con la posa del nostro personale"); Betafence sta nella fascia delle garanzie e nella sezione aziende.
- **Foto di apertura ritagliata in 16:10** (cy 0,42): via un terzo del piazzale di cemento, cancello e casa riempiono il riquadro; 640 px CSS da un file di 800.
- **Il colore del marchio fa i blocchi**: l'indice dei quattro usi e la chiusura "Chiamateci o scriveteci" (telefono bianco a 96 px, modulo su carta bianca) sono su verde #0A7A32; i filetti dei blocchi scuri sono nell'azzurro della rete.
- **Ritmo**: la sezione aziende passa su antracite (il riquadro "Mandateci il disegno" resta bianco). Sequenza a 1440: bianco, verde, grigio, antracite, bianco, antracite, grigio, bianco, antracite, verde, piede antracite; nessuna coppia di fondi uguali di fila. A 390 dopo i lavori (antracite) viene l'indice verde: niente più blocco scuro di 1470 px.
- **Numeri di riempitivo tolti** ("4 materiali", "3 usi", "3,0 m"): in Chi siamo resta solo "50+" a 96 px in azzurro, con la storia in tre tappe (gli inizi, la specializzazione, oggi) scritta con le frasi della pagina Azienda.
- **Lavori**: 4 invece di 6 (uscite `canc082203` e `canc082206`, doppioni delle schede), in due colonne da 624 x 468 a 1440, senza didascalie; ogni foto apre la versione da 800 px (anche sul telefono, dove restano 2 x 2 per stare nei due scorrimenti). Occhiello "Alcuni nostri lavori" e titolo "Recinzioni e cancelli in alluminio per abitazioni": non diciamo più "recenti" né "posati", che le fonti non confermano.
- **Schede dei prodotti a 390** in righe (foto 4:3 da 128 px, nome e link, tutta la riga cliccabile): la sezione scende da 3281 a circa 1000 px.
- **Marchi e norme**: titolo visibile, Betafence ed EN 13241-1 ("certificazione del produttore dei cancelli pedonali e carrai in kit"); ForFence esce dalla fascia e resta solo tra i sistemi. Nel piede una voce "Marchi e norme" a sé.
- **Preventivo detto in un modo solo**: 1. foto e misure ("Per email" è un link alla mail già scritta), 2. vi richiamiamo e fissiamo l'appuntamento in sede, 3. "Vedete i modelli, avete il preventivo": in sede vi diamo il preventivo, gratuito. Tolta la frase vuota "Per un preventivo senza impegno, vi invitiamo a contattarci" (ora "Gratuito e senza impegno. Bastano due o tre foto e le misure."). Il cellulare compare anche qui.
- **Fuori orario** (sera, notte, domenica, festivi, chiusure) il bottone pieno diventa "Manda foto e misure", "Chiama" passa al bordo e sotto compare "Fuori orario: mandateci foto e misure, vi richiamiamo noi." Il sabato resta "Chiama" (su appuntamento, chiamate prima).
- **Stato degli orari**: sopra i bottoni (a 390 finisce a y 610, dentro i 664 px di Safari con le barre); il link accanto apre la navigazione (`maps/dir`) con zona di tocco allargata; nella mezz'ora prima di ogni chiusura dice "Aperto, chiude alle 12.00: chiamate prima"; c'è un elenco `CHIUSURE` per ferie e chiusure straordinarie, vuoto finché l'azienda non dà le date.
- **Imprese**: sotto i bottoni, a 390, il link "Imprese: attrezzature edili al banco" porta diretto al banco; nel riquadro del banco c'è anche il cellulare.
- **Menu**: prima voce "Preventivo". L'email della testata compare da 1600 px; a 1440 è nell'apertura, sotto i bottoni.
- **Modulo**: aggiunti email (facoltativa), "Foto e misure" (le allego / non ancora) e "Giorni preferiti per l'appuntamento" (lun-ven), tutti nel testo dell'email.
- **Ripetizioni**: tolti gli orari dal blocco di chiusura, che rimanda a "Dove siamo".

Respinto o lasciato com'è, con il motivo:
- *Lavori a 390 in una sola colonna da 350 px con 3 foto*: il quarto lavoro finirebbe oltre i due scorrimenti, e il compito del privato ("4 lavori in al più 2 scorrimenti") peggiorerebbe. Restano 2 x 2, ma ingrandibili.
- *"Indice" riportato subito dopo l'apertura a 390*: allontanerebbe passi e lavori del privato; ho scelto l'altra correzione proposta (indice verde) e il link diretto al banco nell'apertura.
- *Un grande lavoro a 1280 px*: i file sono di 800 px, a 1280 sarebbero sgranati.
- *Foto di apertura `l-sera`*: è di sera, con le case dei vicini; `canc082204` ritagliata è più chiara e più frontale.
- *Gesto di scala a 160-200 px per "50+"*: sarebbe la nona misura di carattere (regola 7); resta a 96 px, come il telefono della chiusura.
- *Promessa dei tempi di risposta accanto al modulo*: non è nelle fonti; è nel LEGGIMI.

## La pagina, in ordine

1. **Testata fissa** (89 px a 1440, 73 a 390): marchio, "Recinzioni Formentin / Villatora di Saonara", Preventivo, Prodotti, Lavori, Aziende, Attrezzature edili, Dove siamo, email (da 1600 px) e il bottone "049 760801" (bordato finché i bottoni dell'apertura sono in vista). Sotto i 1280 px il menu va nel bottone "Menu".
2. **Apertura** (bianco): occhiello "Villatora di Saonara (PD)", H1 64 px, riga per il privato, stato con "Mappa" (navigazione), "Chiama 049 760801" e "Manda foto e misure", indirizzo ed email; a destra il loro cancello scorrevole in 16:10 con il riquadro verde "50+"; sotto, le quattro garanzie.
3. **Indice** (verde): Per la casa, Per le aziende, Per gli impianti sportivi, Per le imprese (cinque categorie del banco).
4. **Come chiedere il preventivo** (grigio zinco): tre passi, "Manda foto e misure", "Chiama", "Oppure compilate la richiesta", cellulare.
5. **Alcuni nostri lavori** (antracite): quattro foto grandi, poi "Volete vedere i modelli dal vero? L'esposizione è in sede, su appuntamento." con "Appuntamento 049 760801" e "Indicazioni stradali".
6. **Prodotti** (bianco): sei schede con la foto loro, tutte cliccabili.
7. **Aziende, condomini, impianti sportivi** (antracite): Betafence, tabella dei sistemi, riquadro bianco "Mandateci il disegno", fascia "Marchi e norme".
8. **Attrezzature edili e ferramenta al banco** (grigio): dodici categorie, carpenteria e grigliati, riquadro con stato, orari, "Chiama", "Indicazioni stradali", cellulare.
9. **Dove siamo** (bianco): indirizzo grande, come arrivare, navigazione e mappa; tabella degli orari con il giorno di oggi in verde; telefono, cellulare, email.
10. **Chi siamo** (antracite): "Dai primi anni Settanta", "50+" a 96 px, la frase sul servizio completo, la storia in tre tappe.
11. **Richiesta** (verde): "Chiamateci o scriveteci", telefono bianco a 96 px, cellulare, email; modulo che compone l'email.
12. **Piede** (antracite): marchio, riga, Marchi e norme; Prodotti; Orari; Contatti; riga legale con ragione sociale, indirizzo, P.IVA, Privacy e Cookie.

## Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs <cartella>` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi a 1440, 1024, 768, 390 e 320.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky 89/73 px, bottone "049 760801" 127 x 48 a 390; a metà pagina si vede e si tocca (`elementFromPoint`) a 1440 e a 390. 14 link `tel:`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** H1 "Recinzioni e cancelli, dalla vendita alla posa", occhiello "Villatora di Saonara (PD)", prova visibile da sola ("50+ anni di mestiere, dai primi anni Settanta" in verde pieno, più "Betafence ufficiale" nelle garanzie), "Chiama 049 760801" largo 350 px su 350 a 390.
3. **Immagine vera nell'apertura: passa con riserva.** È un loro lavoro (`canc082204`), non un oggetto scontornato, ora in 16:10 senza il piazzale; non mostra persone, mezzi o la sede. Senza servizio fotografico (e senza illustrazioni, esclusi dal committente) resta così: LEGGIMI, Foto da fare, punto 1.
4. **Zero repertorio: passa.** "indicativ" 0 volte; nessuna immagine da `assets/esterne`, Unsplash o Pexels; in `sito/img/` 11 foto loro e il marchio.
5. **Foto in serie: passa in parte.** Formati: 2 (4:3 e 16:10 dell'apertura). Didascalie: 0. Luce: non ancora una serie (due lavori al crepuscolo, due di giorno, banco ed esposizione al neon del 2014-2015); il trattamento comune di `pro_img.py` attenua ma non basta. La serie vera la fa la giornata di foto del LEGGIMI.
6. **Palette dal marchio: passa.** `--verde` #0A7A32 (F del marchio scurita, ora anche in due blocchi pieni), `--verde-scuro` per il passaggio del mouse, `--azzurro` #5A94F7 (rete: cifre e filetti sui blocchi scuri), `--antracite` #2B3134; neutri bianco, grigio zinco #EEF1F2, grigi di testo e filetti (sul verde, il bianco trasparente). Nessun colore fuori da `:root` a parte i due del marchio nell'SVG. Nessun beige.
7. **Scala tipografica corta: passa.** 8 misure a 1440 (14, 17, 19, 23, 32, 48, 64, 96) e 7 a 390 (14, 17, 20, 24, 30, 36, 44); testo corrente 19 px a 1440 e 17 a 390; niente sotto i 14 px; H1 64/36.
8. **Due famiglie al massimo: passa.** Una: Geologica 400 e 700, anche per campi e bottoni.
9. **Servizi in schede con la foto: passa.** Griglia di 3 colonne a 1440 (2 a 768-1023, righe con la foto a sinistra al telefono), sei schede in 4:3, nome a 23 px, link con freccia; tutta la scheda è un link.
10. **Almeno tre tipi di prova: non passa (1 su 4).** C'è la fascia "Marchi e norme" con la didascalia (Betafence, EN 13241-1). I numeri aziendali non sono 4 (c'è solo "50+": gli altri tre erano riempitivi e sono usciti). Mancano recensioni e clienti con il nome: non sono nelle fonti verificabili (LEGGIMI, punti 4, 6 e 13). Non inventati.
11. **I lavori hanno un nome: non passa.** Quattro lavori con foto larga quasi metà pagina (624 px a 1440), ma senza luogo, anno né dati: non sono nelle fonti (LEGGIMI, punto 5).
12. **Ritmo a blocchi: passa.** Cinque blocchi pieni oltre al piede (indice e richiesta verdi; lavori, aziende e chi siamo antracite), nessun fondo uguale due volte di fila a 1440 e a 390; sezioni a 120 px a 1440 e 64 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno verde e bordato, raggio 4 px, 56 px (48 in testata), testo 17 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: non passa (manca solo la zona).** Modulo con nome, telefono, email, tipo di lavoro, comune e via, metri, altezza, cancelli, foto (le allego / non ancora), urgenza, giorni preferiti e descrizione; nessun iframe. Manca l'elenco dei comuni serviti: non è nelle fonti (LEGGIMI, punto 3).
15. **Piede completo: non passa (manca solo la zona).** Quattro colonne, testo di almeno 14 px, ragione sociale, P.IVA (da atoka, da confermare), indirizzo con la mappa, telefono, cellulare ed email cliccabili, orari, "Marchi e norme", Privacy e Cookie. La colonna "Dove posiamo" è preparata (commento nel codice) e si aggiunge con l'elenco dei comuni.

## Compiti della scheda d'uso

- *Privato, 390 x 844*: senza scorrere la foto del loro cancello, "dalla vendita alla posa", "Villatora di Saonara", lo stato, "Chiama 049 760801" (350 x 56) e "Manda foto e misure" (`mailto:` con oggetto e traccia). Fuori orario il bottone pieno è "Manda foto e misure". Con uno scorrimento i tre passi (y 1215) e il link "Per email" (y 1322). Quattro lavori loro entro due scorrimenti (il quarto comincia a y 2342), ingrandibili. "L'esposizione è in sede, su appuntamento" e "Indicazioni stradali" subito sotto.
- *Impresa, 390 x 844*: lo stato nella prima schermata, sopra i bottoni, giusto a lunedì 10.00, 12.30 e 17.15, venerdì 18.00, sabato, domenica, 8 dicembre, Pasquetta e 24 dicembre sera. "Mappa" apre la navigazione con un tocco. "Imprese: attrezzature edili al banco" nella prima schermata; "Per le imprese" con cinque categorie a y 3205, entro tre scorrimenti; il banco dal menu.
- *Tecnico, 1440 x 900*: telefono in testata ed email nell'apertura; "Betafence ufficiale" nella prima schermata; nella sezione aziende i sistemi con le altezze, "Mandateci il disegno" con i dati che servono e la mail con oggetto "Richiesta per azienda o impianto sportivo".
- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 768, 1024, 1280, 1440 e 1920 (controllato sulla larghezza vera, non sulla finestra del telefono che si allarga); nessuna sovrapposizione in testata e apertura; zoom permesso.

## Caratteri e licenze

- **Geologica** (Google Fonts, SIL Open Font License 1.1, uso commerciale libero), file variabile `sito/fonts/geologica-latin-var.woff2` servito dalla pagina, licenza in `sito/fonts/OFL.txt`. Pesi 400 e 700, cifre tabellari per numeri e orari.
- Foto: solo materiale del loro sito, da usare con il loro permesso e, per le case riconoscibili, con quello dei clienti.

| In pagina | File d'origine (`assets/originali/`) |
|---|---|
| Apertura (16:10) | `gallery_cancelli_canc082204.jpeg` |
| Lavori | `canc082202`, `canc082201`, `ringh082202`, `ringh082203` |
| Schede | `ringh082201` (alluminio), `canc082207` (cancelli), `gallery_ringhiere_img_1061.jpg` (ringhiere), `gallery_reti-ondulate_IMG_1130-1.JPG` (rete), `uploads_2016_01_20151223_103842n.jpg` (esposizione Betafence), `uploads_2014_04_IMG_1135.jpg` (banco) |

## Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1, 2, 4, 6-9, 12 e 13 superate nelle misure; 3 e 5 con riserva (vedi sopra); 10, 11, 14 e 15 no, per materiali che mancano. Compiti d'uso, collegamenti, ancore, larghezze, errori di script: tutti a posto.
- Collegamenti: `tel:+39049760801`, `tel:+393357740278`, `mailto:info@recinzioniformentin.it` con oggetto (e traccia dove serve), Google Maps `search` e `dir` su via Lombardia 17.
- Modulo: invio vuoto fermato con l'avviso e il fuoco sul nome; con i campi pieni compone `mailto:` con oggetto "Preventivo: <tipo>" (letto nella prova, non aperto); le schede scelgono il tipo di lavoro.
- Stato fuori orario guardato a venerdì 20.30 a 390 (bottoni scambiati e riga "Fuori orario").
- Screenshot guardati a pezzi a 1440 e a 390, pagine intere a 320, 768 e 1024. Nessun U+2014 in pagina, nei .md e negli script.
