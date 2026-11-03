# Servalli Padova, home

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze, mai ingrandite), caratteri in `sito/fonts/`. La versione 1 com'era prima di questo passaggio (il Tabriz al centro con il titolo diviso ai lati) è copiata in `_prova/versione-1-originale/` (sito e screenshot, con la sua NOTA).

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Scheda d'uso e d'identità: `_prova/uso/SCHEDA.md`. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 e le pagine intere di Joseph Brot, Poilâne e Union (a pezzi); la prova su Unicar, Oby e Fornasiero (`_invio/zona/home/livello-professionale.jpg` e le loro NOTE).

Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `home_pro.html`, screenshot con `pro_shoot.mjs` all'ora di Roma simulata lunedì 2 novembre 2026 alle 10, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`, controllo della lineetta lunga).

Screenshot (stessi nomi di prima): `home-1440.jpg` (7927 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13455 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari, sede e richieste" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e interi a 320, 768, 1024 e 1920.

### L'idea, in breve

Un grossista di famiglia che vende online ai privati e all'ingrosso a negozi e alberghi. La pagina lo dice nell'ordine in cui la usano: prima il negozio (categorie e prezzi), poi gli alberghi, poi i tappeti, poi chi sono, le loro guide, dove sono e come scrivere. Il registro è quello di un commerciante esperto: titoli loro o descrizioni piane, il "voi" ai professionisti, nessuna parola da atelier.

Struttura della famiglia B adattata (A1):
1. **Testata fissa** con lo stemma, cinque voci (Negozio online, Alberghi e strutture, Rivenditori, Arte tessile, Orari e sede), lo stato dell'ufficio sull'ora di Roma ("Aperto ora, fino alle 17:30"), Carrello e il telefono in un bottone. A 390: stemma, bottone "049 761943" e Menu.
2. **Apertura** in due colonne: occhiello con mestiere, prova e luogo ("Grossisti e importatori di tessile per la casa, dal 1895. Centro Grossisti di Padova."), il titolo del loro sito in maiuscolo "BIANCHERIA E TESSILE CASA DAL 1895", la riga sull'assortimento, "Entra nel negozio", la spedizione gratuita sopra i 150 euro e il reso, il link "Per alberghi e strutture: su misura, con il vostro logo". A destra la foto vera del loro negozio (trapunta SINFONIA). Sotto, già nella prima schermata, le 6 categorie del negozio.
3. **Prodotti con il prezzo** su grigio chiaro: FIORDO 90, M.B. oca bianca, ISLANDA, PIETRA, con misura, prezzo e link alla scheda.
4. **Alberghi e strutture** su blocco arancio dello stemma: titolo della scheda, la loro frase tra virgolette, "Chiedete un preventivo" (apre il modulo già impostato) e "Chiamate 049 761943"; a destra sei righe (che cosa, su misura, logo ricamato o stampato, ignifughi, sempre pronto e consegna in Italia, logo e quantità a info@servalli.net). Sotto, "Rivenditori e grossisti: condizioni a voi riservate".
5. **Tappeti** su nero: il Tabriz del loro negozio scontornato su fondo scuro, l'importazione diretta dagli anni 70, la scheda con il prezzo, il link alla categoria e la loro guida ai formati.
6. **Chi siamo**: il loro motto come manifesto ("Passione per il tessile da quattro secoli."), la loro frase sulle quattro generazioni, sei numeri, tre foto d'archivio 4:3 nella stessa bicromia con una sola didascalia, quattro date.
7. **Marchi e riconoscimenti** su nero: Servalli, Alans e Colorcasa in bianco, con la riga "marchi registrati"; i tre premi con anno e chi li ha dati.
8. **Arte tessile**: tre articoli del loro blog con data, titolo, una frase loro e "Leggi".
9. **Orari, sede e richieste**: ufficio e magazzino con indirizzo, stato, tabella degli orari con la riga di oggi, "Chiama 049 761943", "Indicazioni" (Google Maps, percorso), email, la riga "Ai privati vendiamo solo online"; accanto il modulo.
10. **Piede** nero in 4 colonne.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile: PASSA.** Testata fissa 89 px a 1440 e 69 a 390; bottone "049 761943" alto 48 px. A 390, a metà pagina, si vede e si tocca (`elementFromPoint`). C'è anche la voce "Orari e sede". 5 link `tel:`, tutti `tel:+39049761943`.
2. **Mestiere, luogo, prova e azione nella prima schermata: PASSA.** A 1440x900: occhiello e H1 (biancheria e tessile casa, Padova, 1895), "Entra nel negozio", il link per gli alberghi, telefono e stato in testata; le categorie cominciano a 862 px. A 390x844: lo stesso, il bottone del negozio largo quanto la colonna (350 px), spedizione e reso, link alberghi, "Ufficio lun-ven 9:00-17:30: aperto ora", e il titolo "Nel negozio online" con l'inizio delle tessere.
3. **Immagine vera nell'apertura: PASSA CON RISERVA.** È una foto vera del loro negozio online (dettaglio della trapunta in seta SINFONIA, 1500x1002, mostrata a 600x675 e mai ingrandita), a tutta altezza e non scontornata. Non mostra persone, sede o magazzino: non ne hanno. Niente illustrazioni, per decisione del committente. Le foto da fare sono nel LEGGIMI.
4. **Zero repertorio: PASSA.** "indicativ" 0; nessun file da Unsplash o Pexels in pagina (tolte Pinales, Hansen e Moradian, vedi `assets/CREDITI.md`).
5. **Foto in serie: PASSA.** Cinque foto in pagina, tre formati (apertura 3:2 tagliata in verticale, tappeto verticale, archivio 4:3); le tre d'archivio con la stessa bicromia nero-bianco caldo, le due a colori con la stessa correzione (`pro_img.py`); una sola didascalia, per le tre foto d'archivio.
6. **Palette dal marchio: PASSA.** Arancio #D86C30 e oro #E4B448 campionati sullo stemma, nero #17140F della scritta SERVALLI; bianco pieno come fondo (niente beige), più quattro grigi neutri. Nessun colore scritto fuori da `:root`. Tolto il rosso robbia della versione 1, che veniva dal tappeto. Il punto dello stato "aperto" è arancio, non verde.
7. **Scala corta e leggibile: PASSA.** 1440: 88, 56, 32, 24, 19, 16, 14 px (7 misure); 390: 42, 32, 24, 17, 16, 14 (6). Testo corrente 19 e 17 px; i 14 px solo nella riga legale. Titolo 88 px maiuscolo, interlinea 1,0 (42 px a 390).
8. **Due famiglie: PASSA.** Libre Caslon Display (titoli, cifre, prezzi, anni) e Golos Text (testo, interfaccia, bottoni, modulo), pesi 400 e 700 (prima 400, 500, 600).
9. **Servizi in schede con foto: NON PASSA (limite dichiarato).** Le 6 categorie e i 4 prodotti sono tessere tutte cliccabili in griglia (6 e 4 colonne a 1440), con nome, una riga e il link; i prodotti hanno misura e prezzo in grande. Senza foto: le foto di prodotto del negozio sono piccole (261-800 px), scontornate con riflessi finti e di fornitori diversi; per decisione del committente niente repertorio. Lo still life da fare è nel LEGGIMI.
10. **Almeno tre tipi di prove: NON PASSA (2 su 4).** Sei numeri aziendali (1895, 1967, 4 generazioni, circa 20.000 articoli, 3 marchi, 2022) e la fascia dei marchi registrati e dei tre riconoscimenti con la didascalia. Recensioni e clienti con il nome non sono nelle fonti: non inventati, da chiedere (LEGGIMI).
11. **Lavori con un nome: NON PASSA.** Nessuna fornitura con cliente, anno e quantità nelle fonti. Da chiedere (LEGGIMI): bastano tre alberghi serviti, con l'articolo e la quantità.
12. **Ritmo a blocchi: PASSA.** Blocchi pieni oltre al piede: alberghi (arancio), tappeti (nero), marchi e riconoscimenti (nero); prodotti e arte tessile su grigio chiaro. Sezioni a 112 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 4 px, 52 px (48 in testata), testo 16 px; i tre bottoni di chiamata contengono il numero.
14. **Modulo e "dove e quando" per il mestiere: PASSA.** Modulo con il tipo di richiesta in caselle (preventivo per albergo o struttura, condizioni per rivenditori e grossisti, consiglio o ordine online, altro), Società, Ruolo e Partita IVA solo per i professionisti, telefono, email, messaggio, la riga sugli allegati. Compone un'email (mailto con oggetto "tipo, nome (società)" e i campi): va collegato a un servizio (LEGGIMI). Sede con stato, tabella degli orari, "Chiama" e "Indicazioni"; nessun iframe.
15. **Piede completo: PASSA, senza certificazioni** (l'azienda non ne ha: OEKO-TEX e NOMITE sono dei prodotti). Logo, ragione sociale, indirizzo, telefono ed email cliccabili, orari, mappa, categorie del negozio, pagine per i professionisti e dell'azienda, condizioni di vendita, privacy, cookie, P.IVA e C.F., capitale sociale, Registro imprese, marchi registrati; 4 colonne, testo di 16 px (14 nella riga legale).

### Compiti della scheda d'uso (par. 8)

- **Privato, 390x844.** Senza scorrere: biancheria e tessile per la casa, "Entra nel negozio" (porta a `negozio/`), "Spedizione gratuita in Italia sopra i 150 euro". La tessera "Piumini e trapunte" è a 839 px, il primo piumino con prezzo e misura (FIORDO 90, 178,12 euro, link alla scheda) a 1577 px, entro una schermata di scorrimento. Il telefono è sempre in testata. L'articolo "100% piuma? Cosa intendi?" si apre con un tocco dalla sezione Arte tessile.
- **Albergo, 1440x900.** Senza scorrere: la voce "Alberghi e strutture" e il link "Per alberghi e strutture: su misura, con il vostro logo". In un solo blocco: "logo", "ricamato o stampato", "su misura", "ignifuga". Un clic su "Chiedete un preventivo" porta al modulo con il tipo già scelto e Società, Ruolo e P.IVA in vista; logo ed elenco a info@servalli.net. "Quattro generazioni", "1895" e "consegna in tutta Italia" sono in pagina.
- **Rivenditore, 390x844.** Senza scorrere: il numero in testata e "Ufficio lun-ven 9:00-17:30: aperto ora" (o "chiuso ora", calcolato sull'ora di Roma). Dalla sede, "Indicazioni" apre il percorso su Via Portogallo 11, 35127 Padova. Nel blocco alberghi la riga "Rivenditori e grossisti: condizioni a voi riservate" con il bottone al modulo (tipo già scelto).
- **Identità.** Ogni frase in grande è loro (titolo del sito, motto, frasi di `alberghi` e `informazioni` tra virgolette) o descrive fatti loro. In testata lo stemma a colori; i colori vengono dallo stemma.
- Prove dello stato: lunedì 10:00 aperto; martedì 8:15 "riapre alle 9:00"; martedì 18:00 "riapre domani"; venerdì 17:45 e sabato "riapre lunedì"; 8 dicembre e Pasquetta "oggi è festivo" (senza dire che sono chiusi: da confermare). Menu a 390 aperto e chiuso toccando una voce; invio del modulo vuoto fermato con l'avviso; email composta e letta senza inviarla; 0 errori di script.

### Controlli generali

- Nessuno scorrimento orizzontale da 320 a 2560 px (14 larghezze); nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1440 e 1920 (corretti durante il lavoro: il menu su due righe a 1440, il titolo su quattro righe a 768, le tessere di altezza diversa, la colonna dei tappeti vuota sotto il tappeto, il logo Colorcasa a capo a 1440).
- Collegamenti: `tel:+39049761943`; `mailto:info@servalli.net` (anche con oggetto per logo e quantità); Google Maps percorso (`maps/dir`, destinazione Via Portogallo 11, 35127 Padova) e ricerca (piede); nessuna ancora senza destinazione; i prodotti e le categorie puntano ai percorsi veri del negozio Ecwid (`negozio/...`), gli articoli ai percorsi veri del blog.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi (lo controlla `build_finale.sh`).

### Caratteri e licenze

Libre Caslon Display (400) e Golos Text (variabile, usato a 400 e 700), da Google Fonts, SIL Open Font License 1.1 (uso commerciale libero), file woff2 latin e latin-ext serviti dalla pagina in `sito/fonts/`. Sono le stesse due famiglie della versione 1.

### Foto

Solo foto vere dell'azienda, alla misura che reggono (voti in `_prova/inventario-immagini.json`):
- trapunta SINFONIA (`negozio/2656204814.jpg`, 7/4), apertura;
- Tabriz ghali Alans (`negozio/4126147316.jpg`, 7/6), scontornato, su nero, al massimo 380 px (originale del ritaglio 749 px);
- telai jacquard (`Servalli1895-59539f29.jpg`, 6/6), Giardiniera Padova 1967 (5/4, mostrata al massimo a 410 px), tessitrice in Persia con la firma "© Franco Servalli" (5/6).
Tolte le tre foto di repertorio della versione 1 (lenzuola Pinales, spugna Hansen, pila di tappeti Moradian). Diritti e permessi da chiarire: LEGGIMI.

### Non applicato, apposta

- Apertura a tutto schermo (A1, punto 2): resta in due colonne come chiede la scheda, perché il privato deve trovare il negozio e la spedizione nella stessa schermata.
- "Negozi e orari" come prima voce: ai privati vendono solo online; la voce è "Orari e sede" e sta in fondo al menu, mentre telefono e stato sono sempre nella testata.
- Codice BENVE10: non messo, perché non si sa se è ancora valido (LEGGIMI).
- Newsletter: tolta (non inviava nulla); in pagina c'è un solo modulo.
- Novità di stagione con foto: il blocco prodotti è dedicato ai piumini ("Piumini per l'inverno"), senza foto.
