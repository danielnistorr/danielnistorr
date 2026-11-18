# Servalli Padova, home

## Livello professionale (ritocco finale del 3 novembre 2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze, mai ingrandite), caratteri in `sito/fonts/`. La versione 1 com'era prima del passaggio "livello professionale" (il Tabriz al centro con il titolo diviso ai lati) è copiata in `_prova/versione-1-originale/` (sito e screenshot, con la sua NOTA).

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 e le pagine intere di Joseph Brot e Union (a pezzi). Il controllo del livello professionale e le prove dei clienti tipo sulla versione precedente (voto agenzia 6; privato 7, albergo 8) sono la base di questo ritocco.

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `home_pro.html`, screenshot con `pro_shoot.mjs` all'ora di Roma simulata lunedì 2 novembre 2026 alle 10, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`, controllo della lineetta lunga). Misure rapide delle posizioni: `_prova/script/ritocco_misura.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8938 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (14055 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari, sede e richieste" al piede). Guardati a pezzi a 390 e 1440, e interi a 320, 768, 1024 e 1920.

### Che cosa cambia in questo ritocco

- **Apertura**: tolta la trapunta SINFONIA (foto Molina, di terzi, ingrandita 1,58 volte a 1440 e ridotta a una striscia di 150 px a 390). Al suo posto la foto loro con il marchio: la Fiat 500 Giardiniera "Manifatture Tessili Servalli, tessuti ingrosso" davanti al negozio di Padova nel 1967, nella stessa bicromia dell'archivio. A 1440 riempie la colonna destra (600 x 690, carica la 1024 e la riduce: mai ingrandita); a 390 è a tutta larghezza in 3:2 (390 x 260).
- **Categorie**: non più sei riquadri grigi solo testo in 6 colonne, ma un indice tipografico del negozio in 3 colonne per 2 righe, con filetto nero, nome in Caslon a 32 px su una riga, la riga descrittiva a 17 px e la freccia; tutta la voce è cliccabile. A 390 un elenco in due colonne con filetti e nome a 24 px.
- **Prodotti**: non più quattro schede bianche vuote, ma un listino a righe con filetti (categoria, nome in Caslon e misura, prezzo in cifre tabellari allineato a destra, "Vedi nel negozio"), tutta la riga cliccabile. Subito sotto, "Prima di scegliere" con le due guide (piuma, piumino e piumetta; classi EN 12934) e "Per un consiglio: 049 761943 o info@servalli.net". "le nostre guide" è un link.
- **Gesto di scala e una sola cronologia**: il manifesto "Passione per il tessile da quattro secoli." a 88 px, accanto la spiegazione con le loro parole (le radici nel Seicento, il paramento con lo stemma al Museo della Basilica di Gandino, l'azienda dal 1895), così il motto non sembra in contraddizione con "1895". Le date stanno in un'unica cronologia (1895, 1949, 1967, 1982, 1994, 2022) e la riga "Oggi" sotto. I numeri sono diventati una fascia su nero con quattro quantità a 144 px (1895, 4 generazioni, circa 20.000 articoli, 3 marchi registrati), nella stessa sezione dei marchi e dei riconoscimenti.
- **Archivio**: telai jacquard, camion MADIVAL in Val Gandino (nuova, 6/5 nell'inventario) e tessitrice in Persia, tutte 4:3 in bicromia, con una sola didascalia che spiega anche la foto d'apertura.
- **Testo**: descrizioni, citazioni del blog, didascalie, orari, note e modulo da 16 a 17 px; a 16 restano solo etichette, menu, bottoni, date e campi.
- **Testata** a 390 alta 72 px (più il filetto).
- **Marchi** alla stessa altezza ottica (56 px a 1440, 36 a 390) invece che alla stessa larghezza.
- **Arte tessile**: i tre articoli come voci con filetto e non più schede bianche vuote.
- **Dai clienti tipo**: "Reso entro 14 giorni" porta alle condizioni di vendita; "Ai privati vendiamo online" sta nella prima schermata anche a 390; menu con "Le guide" e "Orari e contatti"; nel blocco alberghi il link "Tutte le forniture alberghiere" e i link visibili sul fondo arancio; dopo "Chiedete un preventivo" il fuoco va su "Nome e cognome"; dopo "Prepara l'email" compare sotto il modulo il testo dell'email pronto, con "Copia il testo", per chi non ha un programma di posta (webmail).

### L'idea, in breve

Un grossista di famiglia che vende online ai privati e all'ingrosso a negozi e alberghi. La pagina lo dice nell'ordine in cui la usano: prima il negozio (indice e listino con i prezzi, le guide subito sotto), poi gli alberghi, poi i tappeti, poi chi sono, i numeri e i marchi, le guide per intero, dove sono e come scrivere. Senza foto di prodotto che reggano, la pagina si regge su tipografia (Caslon grande, cifre a 144 px, indice e listino a filetti), sui colori dello stemma (arancio e nero a blocchi pieni) e sulle foto vere d'archivio in una sola bicromia. Il registro è quello di un commerciante esperto: titoli loro o descrizioni piane, il "voi" ai professionisti, nessuna parola da atelier.

Struttura (A1, famiglia B, adattata):
1. **Testata fissa**: stemma, cinque voci (Negozio online, Alberghi e strutture, Rivenditori, Le guide, Orari e contatti), stato dell'ufficio sull'ora di Roma, Carrello, telefono in un bottone. A 390: stemma, "049 761943" e Menu.
2. **Apertura**: occhiello con mestiere, prova e luogo; "BIANCHERIA E TESSILE CASA DAL 1895"; l'assortimento e "Ai privati vendiamo online"; "Entra nel negozio"; spedizione gratuita sopra i 150 euro e reso; stato dell'ufficio (fino a 1360 px); "Per alberghi e strutture: su misura, con il vostro logo". A destra la Giardiniera del 1967.
3. **Nel negozio online**: indice delle sei categorie.
4. **Listino** su grigio chiaro: FIORDO 90, M.B., ISLANDA, PIETRA, con le due guide e il consiglio.
5. **Alberghi e strutture** su arancio; sotto, rivenditori e grossisti.
6. **Tappeti** su nero con il Tabriz.
7. **Chi siamo**: manifesto e spiegazione, archivio, cronologia.
8. **In numeri, marchi e riconoscimenti** su nero.
9. **Arte tessile**: tre articoli del blog.
10. **Orari, sede e richieste**: sede con stato, tabella degli orari, "Chiama", "Indicazioni", email; il modulo.
11. **Piede** nero in 4 colonne.

### Esito regola per regola (`_prova/script/pro_controlli.mjs`, `_prova/pro_controlli.json` e screenshot)

1. **Telefono in testata fissa, sempre visibile: PASSA.** Testata 89 px a 1440 e 73 a 390 (72 più il filetto). Bottone "049 761943" alto 48 px; a 390, a metà pagina, si vede e si tocca (`elementFromPoint`). Voce "Orari e contatti". 6 link `tel:`, tutti `tel:+39049761943`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** A 1440x900: occhiello e H1 (tessile per la casa, Centro Grossisti di Padova, 1895), "Entra nel negozio" (186 x 52), link alberghi, telefono e stato in testata; l'indice comincia a 820 px. A 390x844: lo stesso, il bottone a tutta colonna (350 x 52, top 675), spedizione e reso (741-792), "Ufficio lun-ven 9:00-17:30: aperto ora" (798-823).
3. **Immagine vera nell'apertura: PASSA.** La Giardiniera con la scritta "Manifatture Tessili Servalli" davanti al loro negozio di Padova, 1967: mezzo con il marchio e sede, foto loro. Non è ingrandita (1024 x 768 mostrata a 600 x 690 a 1440, 480 x 360 a 390 x 260). Riserva: è un documento d'archivio, non la squadra di oggi; la foto del magazzino con le persone resta da fare (LEGGIMI).
4. **Zero repertorio: PASSA.** "indicativ" 0, nessun file da Unsplash o Pexels; tolta anche la SINFONIA (foto Molina). Nessuna illustrazione o immagine generata.
5. **Foto in serie: PASSA.** Cinque foto: quattro d'archivio nella stessa bicromia nero-bianco caldo (apertura, telai, MADIVAL, Persia) e il Tabriz a colori, l'unico articolo loro. Formati a 1440: 0,87 (apertura a tutta colonna), 0,65 (tappeto), 1,33 (archivio), cioè 3; a 390: 1,5, 0,65, 1,33, cioè 3. Una sola didascalia per cinque foto.
6. **Palette dal marchio: PASSA.** Arancio #D86C30 e oro #E4B448 dello stemma, nero #17140F della scritta; fondo bianco, nessun beige; grigi neutri. Nessun colore fuori da `:root`.
7. **Scala corta e leggibile: PASSA.** 1440: 144, 88, 56, 32, 19, 17, 16, 14 (8 misure); 390: 64, 42, 32, 24, 17, 16, 14 (7). Testo corrente 19 e 17 px, descrizioni a 17; 14 px solo nella riga legale. H1 88 px maiuscolo, interlinea 1,0 (42 a 390).
8. **Due famiglie: PASSA.** Libre Caslon Display (titoli, cifre, prezzi, anni) e Golos Text (testo, interfaccia, bottoni, modulo), pesi 400 e 700.
9. **Servizi in schede con foto: NON PASSA (limite dichiarato).** Indice delle categorie in 3 colonne e listino a righe, tutto cliccabile, ma senza foto: le foto di prodotto del negozio sono piccole (261-800 px), scontornate e di fornitori diversi, e il committente ha deciso "niente" repertorio. Invece di schede da foto con la foto tolta, la sezione è un indice tipografico. Lo still life da fare è nel LEGGIMI.
10. **Almeno tre tipi di prove: NON PASSA (2 su 4).** Quattro numeri aziendali e la fascia dei marchi registrati e dei tre riconoscimenti con la didascalia. Recensioni e clienti con il nome non sono nelle fonti: non inventati, da chiedere (LEGGIMI).
11. **Lavori con un nome: NON PASSA.** Nessuna fornitura con cliente, anno e quantità nelle fonti. Da chiedere (LEGGIMI).
12. **Ritmo a blocchi: PASSA.** Fondi pieni oltre al piede: alberghi (arancio), tappeti (nero), numeri, marchi e riconoscimenti (nero); listino e arte tessile su grigio chiaro. Sezioni a 112 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 4 px, 52 px (48 in testata), testo 16 px; i bottoni di chiamata contengono il numero.
14. **Modulo e "dove e quando" per il mestiere: PASSA.** Tipo di richiesta in caselle, Società, Ruolo e P.IVA per i professionisti, telefono, email, messaggio, riga sugli allegati. Compone un'email (mailto con oggetto e campi) e mostra il testo pronto da copiare; va collegato a un servizio (LEGGIMI). Sede con stato, tabella degli orari, "Chiama" e "Indicazioni"; nessun iframe.
15. **Piede completo: PASSA, senza certificazioni** (l'azienda non ne ha). Logo, ragione sociale, indirizzo, telefono ed email cliccabili, orari, mappa, categorie del negozio, pagine per i professionisti e dell'azienda, condizioni di vendita, privacy, cookie, P.IVA e C.F., capitale sociale, Registro imprese, marchi registrati; 4 colonne, testo di 16 px (14 nella riga legale).

### Compiti della scheda d'uso (par. 8), prima e dopo il ritocco

- **Privato, 390x844.** Senza scorrere: biancheria e tessile per la casa, "Ai privati vendiamo online", "Entra nel negozio", spedizione gratuita e reso (con il link alle condizioni), stato dell'ufficio. "Piumini e trapunte" a 987 px (prima 839); FIORDO 90 con prezzo e misura a 1519-1638 px (prima 1577, con la misura oltre la prima schermata scorsa: ora la misura finisce a 1621, dentro i 1688). Le due guide sul piumino sono a 2089 px (prima circa 8650); l'articolo si apre con un tocco anche dalla sezione Arte tessile. Telefono sempre in testata.
- **Albergo, 1440x900.** Senza scorrere: la voce "Alberghi e strutture" e il link dell'apertura. In un solo blocco: logo, ricamato o stampato, su misura, ignifuga, sempre pronto, consegna in tutta Italia. Un clic su "Chiedete un preventivo" porta al modulo con il tipo già scelto, Società, Ruolo e P.IVA in vista e il fuoco sul nome; logo ed elenco a info@servalli.net; dopo "Prepara l'email" il testo resta pronto da copiare. "Tutte le forniture alberghiere" porta alla loro pagina. "Quattro generazioni" e "1895" sono in pagina, con la spiegazione del motto.
- **Rivenditore, 390x844.** Senza scorrere: il numero in testata e "Ufficio lun-ven 9:00-17:30: aperto ora" (o "chiuso ora"). "Indicazioni" apre il percorso su Via Portogallo 11, 35127 Padova. "Rivenditori e grossisti: condizioni a voi riservate" con il bottone al modulo.
- **Identità.** Ogni frase in grande è loro o descrive fatti loro; lo stemma a colori in testata; i colori vengono dallo stemma; la foto d'apertura ha il loro nome sulla fiancata.
- Prove dello stato: lunedì 10:00 aperto; martedì 8:15 "riapre alle 9:00"; martedì 18:00 "riapre domani"; venerdì 17:45 e sabato "riapre lunedì"; 8 dicembre e Pasquetta "oggi è festivo". Menu a 390 aperto e chiuso toccando una voce; invio vuoto fermato con l'avviso; email composta e testo da copiare letti senza inviare; 0 errori di script.

### Controlli generali

- Nessuno scorrimento orizzontale da 320 a 2560 px (14 larghezze, misurato su `clientWidth`); nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1440 e 1920. Corretti durante il ritocco: le cifre a 390 che uscivano dalla colonna in due colonne (ora una), il nome "Lenzuola e copripiumini" troncato a 768, il logo Colorcasa a capo a 390, i link sottolineati in arancio sul fondo arancio.
- Collegamenti: `tel:+39049761943`; `mailto:info@servalli.net` (anche con oggetto per logo e quantità); Google Maps percorso e ricerca; nessuna ancora senza destinazione; prodotti e categorie ai percorsi veri del negozio Ecwid, articoli ai percorsi veri del blog, "Reso entro 14 giorni" a `negozio/pages/terms`, "Tutte le forniture alberghiere" a `alberghi`.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script (lo controlla `build_finale.sh`).

### Caratteri e licenze

Libre Caslon Display (400) e Golos Text (variabile, usato a 400 e 700), da Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), file woff2 latin e latin-ext serviti dalla pagina in `sito/fonts/`. Sono le stesse due famiglie della versione 1.

### Foto

Solo foto vere dell'azienda, alla misura che reggono (voti in `_prova/inventario-immagini.json`):
- Giardiniera, Padova 1967 (`manifatture_tessili_Servalli_Padova_1967web.jpg`, 1024 x 768, 5/4), apertura, in bicromia;
- telai jacquard (`Servalli1895-59539f29.jpg`, 6/6), camion MADIVAL in Val Gandino (`MadivalMicheleFrancescoServalli.jpg`, 6/5), tessitrice in Persia con la firma "© Franco Servalli" (`IMG_2245-...JPG`, 5/6), archivio, in bicromia 4:3;
- Tabriz ghali Alans (`negozio/4126147316.jpg`, 7/6), scontornato, su nero, al massimo 380 px.
Tolta la trapunta SINFONIA (marca Molina). Diritti e permessi da chiarire: LEGGIMI.

### Non applicato, apposta

- Foto nelle voci del negozio, nel listino e nel blocco alberghi (regola 9 e clienti tipo): non ci sono foto loro che reggano, e il committente ha escluso il repertorio. Le foto scontornate del negozio (261-800 px) non sono state messe; quelle della spugna della versione 1 erano di repertorio (Hansen). Da fare dal vero (LEGGIMI).
- Recensioni, clienti e lavori con il nome (regole 10 e 11): non nelle fonti, non inventati.
- Metodi di pagamento accanto alla spedizione: non verificati, non scritti (LEGGIMI).
- Prezzi letti dal negozio in automatico: in una pagina statica restano scritti con la data; nel sito vero vanno letti da Ecwid (LEGGIMI).
- Apertura a tutto schermo (A1, punto 2): resta in due colonne come chiede la scheda, perché il privato deve trovare negozio, spedizione e orario nella stessa schermata; la foto riempie comunque la colonna destra fino al bordo.
- Codice BENVE10: non messo, la validità non è confermata (LEGGIMI).
