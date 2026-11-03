# Foralberg, home finale

## Ritocco finale (3 novembre 2026, dopo il controllo del livello professionale)

Il controllore (voto agenzia 6) e le due prove con i clienti tipo (compratore a 1440, voto 7; titolare che apre un locale a 390, voto 7,5) hanno chiesto: un gesto di scala e una tipografia con carattere, testo corrente a 17 px, schede dei prodotti meno da foglio di calcolo, la citazione dei piatti in evidenza, cifre pulite, un solo sistema di bottoni, fascia delle aree chiusa dentro la prima schermata, testata più alta sul telefono e un modulo che non dica cose false. Pagina rifatta con `bash _prova/script/build_finale.sh` (la sorgente `_prova/script/index.sorgente.html` è identica a `sito/index.html`); prova del modulo con `node _prova/script/ritocco_modulo.mjs <percorso>/sito/index.html <cartella>`.

Screenshot rigenerati (stessi nomi): `home-1440.jpg` (9427 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (15427 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Guardati a pezzi a 1440 e 390, e interi a 320, 768 e 1024, accanto alle prime schermate dei 14 riferimenti e alle pagine intere di Union e Joseph Brot.

### Che cosa è cambiato

- **Due famiglie con ruoli fissi** (A4 per le botteghe): Newsreader 400 con l'asse ottico per H1, H2, H3, cifre, date e citazione; Schibsted Grotesk 400 e 700 (quella della versione 1) per testo, etichette, bottoni, menu e piede. Il titolo "Forniture alberghiere dal 1953" a 88 px ora ha la voce di una casa dell'ospitalità, non di un modello aziendale.
- **Gesto di scala** nel blocco blu: "Più di / 6.000 / articoli in pronta consegna" con la cifra a 232 px (200 a 1024, 168 a 768, 120 a 390), un fatto vero (catalogo p. 3, pagina Company).
- **Cifre pulite**: tolti 1953 (già nel titolo e nella riga del tempo) e "516 pagine"; restano oltre 800 m² di showroom a Padova, oltre 30.000 articoli, 11 agenti e commerciali, 6 portali e albi della PA (il conteggio dell'elenco in Acquisti PA). "oltre" sta piccolo sopra la cifra.
- **Testo corrente a 17 px a 1440** (`--t6`), 16 px sul telefono. Misure a 1440: 232, 88, 56, 32, 24, 19, 17, 14 (otto); a 390: 120, 44, 32, 24, 20, 17, 16, 14 (otto).
- **Schede dei prodotti come blocchi**: fondo nebbia, padding 32 px, nome in Newsreader a 32 px, marchi in una riga in grassetto, capitoli in un elenco compatto con una sola linea in testa e la pagina a destra, in fondo due bottoni con il bordo, "Disponibilità" e "Campionatura" (prima un solo link che sceglieva sempre Disponibilità); Impianti con "Mandaci la planimetria". Schede alte uguali. Sul telefono i capitoli restano chiusi in "Apri".
- **La citazione** «Il tuo biglietto da visita? Un piatto su misura.» è un blocco a sé a 56 px (32 a 390), con accanto la personalizzazione e il link "Piatti personalizzati, catalogo p. 103 (PDF, 56 MB)".
- **Marchi**: Cambro solo con il nome (il sito non lo descrive), RAK "Porcellana" (capitolo del catalogo), "Revol e altri" diventato "Revol".
- **Un solo sistema di bottoni**: le voci "Che cosa guardiamo" non hanno più bordo e raggio da bottone, sono un elenco a due colonne con il filetto in alto.
- **Testata**: tolta la voce "Cataloghi" (portava allo stesso punto di Prodotti); restano 5 voci, "Privati: La Vetrinetta" e il telefono. Sul telefono la testata è alta 72 px (prima 64).
- **Prima schermata 1440**: la fascia blu delle aree finisce a 862 px, con i marchi (Steelite, RAK, Revol, Rona, BIT, Wüsthof, Berto's). Il secondo bottone si chiama "Capitoli del catalogo 2026/2027": dice che porta all'elenco dei capitoli, non a un download.
- **Ancore**: arrivando da un link su una sezione (#prodotti, #pa, #negozi...) il contenuto parte circa 44 px sotto la testata, non più dopo una banda vuota di 130 px.
- **Modulo** (difetto bloccante delle due prove):
  - i link "Mandaci la planimetria", "Disponibilità", "Campionatura" e "Fissate una visita" portano direttamente al modulo (#modulo), non al titolo e ai recapiti;
  - con "Progetto o impianto" l'allegato sale subito sotto i tipi, con il bottone "Scatta o scegli la planimetria", seguito da spazio, pasti e tipologia di cucina (a 390 l'allegato è a 309 px dall'alto dopo il tocco);
  - sul telefono i recapiti vanno sotto il modulo;
  - prima del clic: "Si apre il vostro programma di posta con la richiesta già scritta per servizioclienti@foralberg.it: l'allegato, se c'è, va aggiunto lì";
  - dopo il clic niente più "Si è aperta l'email": la pagina dice che ha provato ad aprire la posta e, se non si è aperta, di copiare il testo e mandarlo a servizioclienti@foralberg.it o di chiamare il 335 142 6521; mostra il testo pronto (destinatario, oggetto, campi) con "Copia il testo" e "Copia l'indirizzo email";
  - se la condivisione del telefono viene annullata, si ripiega sull'email invece di non dire nulla;
  - "Copia" anche accanto a servizioclienti@foralberg.it nei recapiti; il messaggio è dichiarato facoltativo.
  Provato in Playwright a 390 e 1440: tipo "Progetto o impianto", mailto con oggetto "Richiesta: Progetto o impianto, Ristorante o banqueting, Mario Rossi", testo pronto visibile, nessun errore in console.

### Esito regola per regola (`_prova/pro_controlli.json` e screenshot)

1. **Telefono in testata fissa**: PASSA. Bottone "049 760955" di 48 px in testata `position:sticky`, alta 88 px a 1440 e 72 px a 390; a metà pagina a 390 si vede e si tocca; 12 link `tel:`; prima voce "Showroom e orari".
2. **Prima schermata**: PASSA. Occhiello "Consulenti dell'ospitalità, a Padova", H1 "Forniture alberghiere dal 1953", oltre 30.000 articoli e 800 m², "Chiedi un preventivo" (1440) e "Chiama 049 760955" largo 350 px (390).
3. **Immagine vera nell'apertura**: PASSA, con riserva. Il furgone OM Lupetto 30 con la firma, archivio Foralberg; a 390 sotto le due sedi, quindi appena visibile nella prima schermata. Manca una foto di oggi (LEGGIMI).
4. **Zero repertorio**: PASSA. "indicativ" 0; immagini: furgone, stand della 38a Fiera, due loghi.
5. **Foto in serie**: PASSA. Due foto d'archivio, stesso trattamento, un formato (4:3), nessuna didascalia.
6. **Palette dal marchio**: PASSA. Blu #00699A (dalla copertina del catalogo), blu scuro per il passaggio del mouse, inchiostro, verde solo per "Aperto ora"; neutri; fondo bianco.
7. **Scala corta e leggibile**: PASSA (prima non passava). Otto misure a 1440 e otto a 390; testo corrente 17 px a 1440 e 16 a 390; nulla sotto i 14 px (a 14 solo etichette, note del modulo e riga legale); H1 88 px (fascia B 85-90) e 44 px a 390 (40-46).
8. **Due famiglie**: PASSA. Newsreader per i titoli e le cifre, Schibsted Grotesk per testo e interfaccia.
9. **Schede con la foto del lavoro**: NON PASSA (limite dichiarato). Sei schede in tre colonne, blocchi pieni con nome, marchi, capitoli e bottoni, senza foto (decisione del committente: niente repertorio, niente disegni) e non cliccabili per intero perché ognuna ha più link ai capitoli. Le foto da fare sono nel LEGGIMI.
10. **Prove di almeno tre tipi**: NON PASSA (2 su 4). Quattro cifre più il 6.000 grande, e la fascia dei marchi con la didascalia (più i portali PA). Recensioni con nome e clienti con il nome non sono nelle fonti: da chiedere (LEGGIMI), non inventati.
11. **Lavori con un nome**: NON PASSA. Nessun lavoro con cliente, luogo, anno e dati nelle fonti; da chiedere.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni: fascia delle aree e marchi in blu, progetti e chi siamo in inchiostro, richiesta in nebbia; sezioni 128 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e con il bordo, raggio 4 px, 52 px (48 in testata), testo 17 px (16 sul telefono) in 700; le voci non cliccabili non sembrano più bottoni; i bottoni di chiamata hanno il numero.
14. **Modulo e "dove e quando"**: PASSA. Tipo di richiesta in caselle, settore, allegato; per le due sedi stato, tabella degli orari, Chiama e Indicazioni; nessun iframe.
15. **Piede completo**: PASSA (senza certificazioni, che non hanno: c'è "Fornitore abilitato PA"). Quattro colonne, testo 17 px, riga legale 14 px.

### Prove d'uso, dopo il ritocco

- Compratore, 1440: categorie e sette marchi su otto nella prima schermata (Cambro nel blocco Marchi); Porcellana in due clic con "(PDF, 56 MB)" scritto prima; Disponibilità e Campionatura scelgono il tipo giusto; email del servizio clienti copiabile con un clic; PA in un clic dal menu.
- Nuova apertura, 390: Chiama senza scorrere; "progettiamo, installiamo e assistiamo" a 1713 px e "Mandaci la planimetria" a 1801 px (due scorrimenti); il tocco porta al modulo con il tipo scelto e l'allegato in testa; lo showroom con stato, tabella e Indicazioni in un tocco.
- Privato, 390: La Vetrinetta con lo stato nella prima schermata.
- Stato aperto o chiuso giusto alle otto ore di prova (`?ora=`).

### Controlli generali

- Nessuno scorrimento orizzontale da 320 a 2560 (14 larghezze); nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1440 (corretto durante il lavoro: la riga "Capitoli nel catalogo (PDF, 56 MB) Apri" a 320, ora senza il peso sotto i 375 px, dove i capitoli dicono comunque che aprono il PDF del catalogo).
- Console senza errori; nessuna ancora senza destinazione; nessun carattere U+2014 nella pagina, negli script, in questa nota e nel LEGGIMI.

### Caratteri e licenze

- Newsreader (Production Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/newsreader-latin.woff2`, `newsreader-latin-ext.woff2`, variabile con l'asse ottico 6-72, peso 400; licenza in `sito/fonts/OFL-Newsreader.txt`).
- Schibsted Grotesk (Schibsted, Bakken & Bæck), Google Fonts, SIL Open Font License 1.1; `sito/fonts/schibsted-*.woff2`, pesi 400 e 700; licenza in `sito/fonts/OFL.txt`.
- Foto: solo archivio Foralberg; nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Non applicato, apposta

- Tutta la scheda cliccabile (regola 9): ogni scheda ha da uno a cinque link ai capitoli; rendere cliccabile la scheda li annullerebbe.
- Foto a tutto schermo nell'apertura: l'unica foto che regge è d'archivio e la scheda d'uso la vuole accanto al testo.
- Asteria & Nyx e "Nuovo catalogo 2026/2027" come novità: la linea compare solo nei post LinkedIn, senza marca né area certa; nel LEGGIMI.
- Invio vero del modulo: va collegato a un servizio (LEGGIMI); la pagina ora non promette più che l'email sia partita.

## Livello professionale, prima del ritocco finale (3 novembre 2026)

Quello che segue descrive la pagina prima del ritocco qui sopra; i numeri e le misure non sono più quelli attuali.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (due foto d'archivio in JPEG a quattro larghezze e i due loghi SVG), caratteri in `sito/fonts/`. La versione 1 com'era prima di questo passaggio è in `_prova/versione-1-originale/` (sito e screenshot). Rifare tutto: `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, pagina da `index.sorgente.html`, screenshot con `pro_shots.mjs` all'ora simulata martedì 3 novembre 2026 alle 10.00, poi `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`).

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Union e Joseph Brot a pezzi. Dalla famiglia B ho preso la struttura che serve a un grossista con showroom e negozio: "Showroom e orari" come prima voce del menu, le due sedi con stato, tabella degli orari, Chiama e Indicazioni (come i negozi di Union), il modulo che chiede il tipo di richiesta, il piede in quattro colonne. Dalla manifattura (barth, Cly-Del) la fascia dei numeri e l'indice tipografico al posto delle foto che non ci sono.

Screenshot (stessi nomi): `home-1440.jpg` (8894 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (15070 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Showroom e orari" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e interi a 320, 768, 1024 e 1920.

### Che cosa è cambiato

- **Uso prima di tutto (scheda `_prova/uso/SCHEDA.md`)**. La versione 1 apriva sul furgone e su "I capitoli del catalogo", un PDF da 56 MB; non c'erano modulo, marche, orari, La Vetrinetta, PA. Ora:
  - 1440 (compratore): testata fissa con "Showroom e orari", Prodotti, Marchi, Progetti e impianti, Cataloghi, Acquisti PA, "Privati: La Vetrinetta" a parte e il bottone 049 760955; titolo "Forniture alberghiere dal 1953" (le loro parole, home di oggi e copertina del catalogo) con "Consulenti dell'ospitalità, a Padova" come occhiello; la riga su cosa e per chi; "Chiedi un preventivo" e "Catalogo 2026/2027"; il furgone accanto al testo, non sopra; le due sedi con lo stato ("Per i professionisti, Showroom, via Cile 2, Aperto ora" e "Per i privati, La Vetrinetta, via Vigonovese 93"); in fondo alla schermata la fascia blu delle sei aree con le marche scritte (Steelite, RAK, Revol, Rona, BIT, Wüsthof, Berto's) a y=778.
  - 390 (nuova apertura e privato): testata fissa con "049 760955" e Menu; titolo su tre righe a 44 px, riga, "Chiama 049 760955" e "Preventivo o progetto" a tutta larghezza, le due sedi con lo stato (La Vetrinetta finisce a 711 px su 844); poi il furgone, la fascia delle aree e subito il blocco Progetti e impianti (sul telefono sale prima dei prodotti: testo a 1746 px, "Mandaci la planimetria" a 1834, entro due scorrimenti).
  - Prodotti: sei schede (Tavola, Bar e mixology, Sala e buffet, Cucina, Gastronorm e trasporto pasti, Impianti professionali) con la riga del catalogo, le marche in testo e i capitoli con la pagina vera del catalogo 2026/2027 (indice di p. 7: Porcellana 10, Posateria 182, Vetro 232, Bar e mixology 290, Sala 352, Buffet e catering 378, Melamina 400, Cucina 412, Pasticceria 448, Pizzeria 464, Gastronorm 470, Stoccaggio 494, Piccoli macchinari 498; personalizzazione p. 103), ognuno con "(PDF, 56 MB)" scritto prima del clic; il Buffet 2025 (6,9 MB); "Chiedi disponibilità o campionatura" che apre il modulo con tipo e area già scelti. Sul telefono i capitoli sono chiusi in un "Apri" (il PDF intero è un muro).
  - Modulo in home: tipo di richiesta (Preventivo, Campionatura, Disponibilità, Progetto o impianto, Visita in showroom), Settore (le voci del modulo di oggi più Ente pubblico e Privato, che mostra La Vetrinetta), area, nome, locale, telefono, email, messaggio, allegato; con "Progetto o impianto" compaiono spazio, pasti e tipologia di cucina (i criteri del catalogo, p. 5). Obbligatori solo nome, telefono e settore. Compone un'email a servizioclienti@foralberg.it con oggetto e campi; con un file, sul telefono che lo permette apre la condivisione con il file allegato, altrimenti l'email e l'avviso di allegarlo. Va collegato a un servizio (LEGGIMI). Accanto, servizio clienti 335 142 6521, servizioclienti@foralberg.it in chiaro (selezionabile con un clic), centralino e vendite.
  - Showroom e orari: due schede, "Per i professionisti" (via Cile 2, stato, tabella con la riga di oggi, Chiama, Indicazioni, le uscite 13 e 14 della tangenziale Est come le scrive la pagina Contatti, "Fissate una visita") e "Per i privati" (La Vetrinetta, via Vigonovese 93, "aperto anche il sabato", tabella, Chiama 049 8700975, Indicazioni, shop online, lista nozze, Facebook). Stato calcolato sull'ora di Roma e sui festivi nazionali e Pasquetta.
  - Acquisti PA: i sei portali in elenco e "Non ci trovate sul portale della vostra regione? Contattateci e provvederemo all'abilitazione immediata" con il bottone.
- **Identità**: le loro parole ("Forniture alberghiere dal 1953", "Consulenti dell'ospitalità", "ci piace pensare di essere più di un semplice fornitore", "Dall'ascolto al piatto, un progetto su misura", i quattro tempi in "tu", "Il tuo biglietto da visita? Un piatto su misura."), "voi" nel resto, nessuna frase sul logo o sul design. Il blu della copertina del catalogo è il colore della pagina (fascia delle aree, blocco dei numeri e dei marchi, bottoni), non un solo bottone. Le foto sono solo le loro.
- **Foto, decisione "niente"**: tolte le sei Pexels dell'indice (Çelik, Irina P, Kovaleva, Çoban, Starostin, Filirovska); nessuna illustrazione al loro posto. Restano due foto d'archivio, stessa serie (bianco e nero, neri #1A1A1A, luci #F4F5F5), stesso formato 4:3: il furgone nell'apertura e lo stand della 38a Fiera in "Chi siamo", con la scritta stampata sulla foto ("38a Fiera di Padova, foto Giordani") al posto della didascalia. Le foto dei marchi del vecchio slider (Steelite, Eme, Rona, Berto's) non le ho messe: sono dei fornitori, larghe e basse (1400x500), con luci diverse, e avrebbero rotto la serie.
- **Colori**: niente bianco porcellana di comodo: fondo bianco, nebbia #EFF2F4 per le schede e il modulo, blu #00699A (il #0082B9 della copertina scurito per il testo bianco, 6,0:1), inchiostro #15191C per due blocchi scuri, verde #1C7A3D solo per "Aperto ora".
- **Tipografia**: la stessa famiglia della versione 1, Schibsted Grotesk, ora in due pesi distanti (400 per titoli e testo, 700 per etichette, bottoni, nomi). Sette misure a 1440 (88, 56, 32, 24, 19, 16, 14) e sette a 390 (44, 32, 24, 20, 17, 16, 14).

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Bottone "049 760955" alto 48 px in testata `position:sticky`; a 390, a metà pagina, si vede e si tocca (`elementFromPoint`). "Showroom e orari" è la prima voce del menu. 12 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA. 1440x900: H1 "Forniture alberghiere dal 1953" (mestiere e prova), "a Padova" nell'occhiello, "Chiedi un preventivo" e il telefono. 390x844: lo stesso, "Chiama 049 760955" largo quanto la colonna (350 px) a 401 px.
3. **Immagine vera nell'apertura**: PASSA. Il furgone OM Lupetto 30 con la firma Foralberg, foto d'archivio dell'azienda, 628x471 a 1440 accanto al testo; a 390 a tutta larghezza dopo le due sedi. Manca una foto di oggi (showroom, persone): vedi LEGGIMI.
4. **Zero repertorio**: PASSA. "indicativ" 0 volte, nessuna immagine da banche; in `sito/img/` solo furgone, fiera38 e i loghi.
5. **Foto in serie**: PASSA. Due foto, stessa serie e stesso trattamento, un solo formato (4:3), nessuna didascalia in HTML.
6. **Palette dal marchio**: PASSA. Quattro colori (blu, blu scuro per il passaggio del mouse, inchiostro, verde dello stato) più i neutri; il blu viene dalla copertina del catalogo; nessun beige.
7. **Scala corta e leggibile**: PASSA. 7 misure a 1440 e 7 a 390; testo corrente 19/17 px; nulla sotto i 14 px; titolo 88 px (fascia B 85-90), 44 px a 390 (40-46). Il titolo non è in maiuscolo come nei riferimenti B (e come sul sito di oggi): tenuto in tondo come nella versione 1, più cordiale e leggibile su tre righe.
8. **Al massimo due famiglie**: PASSA. Una sola, Schibsted Grotesk, 400 e 700.
9. **Servizi in schede con la foto del lavoro**: NON PASSA (limite dichiarato). Sei schede in tre colonne, con nome, riga, marche, capitoli con le pagine e link, ma senza foto: per decisione del committente niente repertorio e niente disegni, e le foto dei fornitori non fanno serie. Le foto da fare sono nel LEGGIMI.
10. **Almeno tre tipi di prove**: NON PASSA (2 su 4). Ci sono sei numeri (1953, 800 m², 30.000, 6.000, 11, 516) e la fascia dei marchi trattati con la didascalia, più i portali PA abilitati. Mancano recensioni con nome e clienti con il nome: non sono nelle fonti (le recensioni Google non si leggono da qui, quelle aggregate sono di La Vetrinetta), non inventati (LEGGIMI).
11. **Lavori con un nome**: NON PASSA. Nessun lavoro con cliente, luogo, anno e dati nelle fonti; le forniture storiche (Venezia 1959, Costa Smeralda 1960) sono nella riga del tempo, senza nomi di alberghi. Da chiedere (LEGGIMI).
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: fascia delle aree e marchi in blu, progetti e chi siamo in inchiostro, modulo in nebbia; spazio tra le sezioni 128 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e con il bordo (bianchi sui blocchi scuri), raggio 4 px, 52 px (48 in testata), testo 16 px in 700; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta e il settore (più l'allegato e i campi del progetto); per ognuna delle due sedi stato, tabella degli orari con la riga di oggi, "Chiama" e "Indicazioni" (`google.com/maps/dir`); nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno; al loro posto "Fornitore abilitato PA: MePA Consip e portali regionali"). Quattro colonne a 1440 (due a 1024 e 768, una sul telefono con i prodotti in due colonne): ragione sociale, P.IVA, indirizzo, telefoni ed email cliccabili, orari di showroom e negozio, le due sedi, LinkedIn con il sottotitolo, La Vetrinetta su Facebook, Lavora con noi, Privacy, Cookie, Note legali; testo di 16 px (14 nella riga legale).

### Prove d'uso della scheda (par. 8)

- Compratore, 1440: in prima schermata cosa vendono e a chi, 049 760955 e "Chiedi un preventivo"; Ctrl+F "Steelite", "Rona", "Berto's", "Wüsthof" a y=835 (fascia delle aree), "Cambro" a 3133, "MePA" a 6867; Porcellana in due clic ("Catalogo 2026/2027", poi "Porcellana p. 10", `#page=10`) con "(PDF, 56 MB)" scritto prima; richiesta con settore, tipo, messaggio e allegato con 3 campi obbligatori; l'email del servizio clienti scritta in chiaro.
- Nuova apertura, 390: Chiama senza scorrere; "progettiamo, installiamo e assistiamo" e "Mandaci la planimetria" entro due scorrimenti; il tocco apre il modulo con "Progetto o impianto" scelto, i campi del progetto e l'allegato (immagini, PDF, DWG, DXF); dalla riga "Showroom, via Cile 2" un tocco porta alla scheda con stato, riga di oggi in grassetto e Indicazioni.
- Privato, 390: "Per i privati, La Vetrinetta, via Vigonovese 93" con lo stato nella prima schermata, sotto "Per i professionisti, Showroom, via Cile 2"; un tocco porta a indirizzo, orari (sabato aperto, lunedì mattina chiuso), 049 8700975, shop online e lista nozze.
- Stato a ore diverse (provato con `?ora=`): martedì 10.00 aperti tutti e due; 13.10 "Chiuso ora, riapre alle 14.30" e "riapre alle 15.00"; sabato 10.00 showroom "riapre lunedì alle 8.30", Vetrinetta aperta; domenica "riapre domani"; lunedì 10.00 Vetrinetta "apre alle 15.00"; 25 dicembre e Pasquetta 2027 "Chiuso oggi, festivo"; venerdì 19.00 showroom chiuso, Vetrinetta aperta fino alle 19.30.

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 390, 430, 600, 768, 860, 1024, 1100, 1240, 1280, 1440, 1920, 2560; nessuna sovrapposizione negli screenshot (corretti durante il lavoro: la riga delle sedi a 768 su due colonne strette, ora una colonna; la colonna Contatti del piede sul telefono che spezzava numero ed email; l'"Apri" comparso anche su "Come lavoriamo").
- Console senza errori con file://; nessuna ancora senza destinazione.
- Collegamenti: `tel:+39049760955`, `tel:+393351426521`, `tel:+390498700975`; `mailto:servizioclienti@foralberg.it` (anche con oggetto per l'abilitazione PA e dal modulo con oggetto e campi), `mailto:ldesiderio@foralberg.it`, `mailto:lavetrinetta@foralberg.it`; mappe `google.com/maps/dir/?api=1&destination=` su "Foralberg via Cile 2 35127 Padova" e "La Vetrinetta via Vigonovese 93 35127 Padova".
- Nessun carattere U+2014 nella pagina, negli script nuovi, in questa nota, nel LEGGIMI e nei crediti.

### Caratteri e licenze

- Schibsted Grotesk (Schibsted, Bakken & Bæck), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/schibsted-latin.woff2`, `schibsted-latin-ext.woff2`, licenza in `sito/fonts/OFL.txt`), pesi 400 e 700.
- Foto: archivio Foralberg ("foto Giordani" sullo stand), diritti da chiedere all'azienda. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Non applicato, apposta

- Apertura a tutto schermo con una foto (famiglia B, punto 2): l'unica foto che regge è d'archivio e la scheda la vuole accanto al testo, non al posto del messaggio.
- Racconti foto e testo alternati (B, punto 4) e novità di stagione con foto (B, punto 6): senza foto di oggi; la stagione c'è come riga del tempo (2026, HospitalityRiva) e catalogo nuovo.
- Newsletter: tolta (non inviava nulla; la scheda chiede di toglierla finché non è collegata).
- Recensioni, clienti con il nome, lavori con il nome, certificazioni: non nelle fonti, da chiedere.
- Il titolo "Consulenti dell'ospitalità" della versione 1: non è più l'H1 (da solo non dice il mestiere, scheda par. 7) ma resta come occhiello dell'apertura e come titolo di "Chi siamo" ("Dal 1953 consulenti dell'ospitalità").

## Versione 1 originale (2 novembre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/` (sito e screenshot). Le sezioni sono scese di un livello.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot). Altezza a 1440: 5396 px piede compreso.

### L'idea

La firma corsiva del logo di oggi è già dipinta sul cassone dell'OM Lupetto 30 delle prime consegne. La home apre su quella foto d'archivio, a tutta larghezza e subito sotto il logo in testata: firma di allora sotto logo di oggi, si legge in due secondi senza didascalia. Con il nome di un concorrente la pagina non regge: il furgone, la portiera con le voci del catalogo, lo stand della 38a Fiera e la frase di chiusura sono solo loro.

### Cosa è cambiato in questa rifinitura (2 novembre)

Dal giudizio cieco (K0 7, K6 6, 57 su 80) e dalla richiesta del committente "più alta gamma, meno uguali tra loro".
- **Fondo dal mestiere**: via la carta beige #F3F1EC. La pagina è bianco porcellana #F5F6F5, il bianco della porcellana da tavola che è il primo capitolo del catalogo ("il bianco valorizza il cibo", catalogo p. 47). La ragione si vede: le luci di tutte le foto finiscono esattamente su quel bianco (il furgone, lo stand, il piatto, le posate, il calice con la sua ombra), così gli oggetti stanno sulla pagina come sulla tovaglia.
- **Impaginazione che non c'è nelle altre home** (controllate le copertine di Est-Grisignano e Mestrino e le prime schermate della campagna): la foto parte dal filo della testata, a tutta larghezza, prima del titolo; il titolo viene dopo, sotto la foto. Nelle altre home il titolo sta sopra o accanto all'oggetto. In più la pagina si chiude a specchio con un'altra foto d'archivio a tutta larghezza (chiusura con testo sopra e foto sotto), e tra le due c'è un solo blocco diviso foto e testo (l'indice).
- **Apertura** (K6): titolo "Consulenti dell'ospitalità" (dalla home di oggi, "Dal 1953 Consulenti dell'Ospitalità") al posto della formula "X dal 1953"; foto subito sotto la testata, didascalia del furgone sopra la piega nella colonna destra, poi la riga su cosa vendono, il bottone "I capitoli del catalogo" e "Vieni in via Cile 2". Logo in testata a 52 px.
- **Ponte tra archivio e catalogo**: l'introduzione dell'indice cita la portiera del Lupetto ("porcellane, cristallerie, posaterie, art. vari cucina", letto sull'originale) e dice che oggi sono i capitoli del catalogo.
- **Foto dell'indice** (bloccante): sei soggetti diversi, uno per capitolo e nominato nella sua riga: piatto piano bianco dall'alto (Çelik), forchette d'argento (Irina P), calice da grappa con l'ombra (Kovaleva), coppe da cocktail e shaker (Çoban), chafing dish in acciaio (Starostin), gastronorm con le posate (Filirovska). A colori naturali smorzati, luci neutre sul bianco della pagina; il piatto, nato in bianco e nero, con la grana attenuata e il piano schiarito. L'archivio resta in bianco e nero: la voce del passato contro quella del presente.
- **Viraggio dell'archivio**: neri a #1A1A1A, nessuna apertura locale delle ombre (via l'aspetto HDR dell'arco).
- **Storia e chiusura** (bloccante): tolta la sezione storia con lo stand della 38a e tolta la foto della 42a (mangani e lavatrici). Resta una sola foto di stand, la 38a con porcellane, posate e tavoli apparecchiati, in chiusura a tutta larghezza sotto la frase e i recapiti. Tolta la frase ambigua sui "fratelli Desiderio".
- **Numeri**: una frase per chi lavorano (con la PA) e quattro cifre grandi in riga (800 m², 30.000, 6.000, 11), cifre proporzionali perché le tabellari di Schibsted allargavano il punto ("30 . 000").
- **Progetto**: i quattro tempi in righe a filetto (numero e titolo a 30 px, riga a destra), non più quattro colonne da modello.
- **Minori**: bottone rinominato; "(PDF, 56 MB)" accanto al link del capitolo; menu Cataloghi e Chi siamo verso le pagine del sito nuovo; altezza dell'indice costante a ogni capitolo e a ogni larghezza (lo script misura il testo più lungo e fissa l'altezza della scheda); a 1024 la foto dell'indice è alta quanto la colonna di testo (nessun vuoto sotto); link del piede alti almeno 29 px a schermo largo e 35 px fino a 860, colonna Contatti in grigio con il solo telefono in inchiostro; tolto il preload del font (nessun errore in console con file://); foto di apertura e chiusura più alte (37,5vw fino a 56vh, e 64vw fino a 940 px) e ritmo tra le sezioni a 132 px.

### Le prime schermate

- **1440**: testata con logo vettoriale, menu corto e 049 760955. Foto del furgone da y=88 a 592: firma, monogramma, via Trieste 11, i marchi rappresentati, la portiera e la calandra con "Lupetto 30". Sotto, a sinistra, "Consulenti dell'ospitalità" a 106 px su due righe; a destra la didascalia del furgone, la riga su cosa vendono, il bottone e il link, tutto sopra la piega (il bottone finisce a y=895).
- **390**: foto quadrata sul cassone (firma, monogramma, marchi, portiera), titolo a 46 px su due righe, didascalia, riga e bottone dentro la prima schermata.
- Poi: numeri, indice del catalogo (il gesto), progetto in quattro tempi, chiusura, piede.

### Caratteri e colori

- **Schibsted Grotesk** (Google Fonts, SIL Open Font License 1.1, testo in `sito/fonts/OFL.txt`), una famiglia sola servita dalla pagina in woff2 variabile: 400 per titoli e testo, 500 per menu, bottoni e didascalie in grassetto. Grottesco da giornale accanto ai caratteri dipinti degli stand e del furgone, senza fare a gara con la firma corsiva. Cifre tabellari solo sui numeri di pagina dell'indice e sulla P.IVA.
- Bianco porcellana #F5F6F5, inchiostro #161616 (17,1:1), grigio #5A5A5A (6,5:1), filetti al 16 %, blu Foralberg scurito #00699A (5,8:1 sul fondo, bianco sul blu 6,0:1; il #0082B9 della copertina non regge AA col testo bianco) solo per bottoni, pagina del capitolo attivo e numeri dei passi.
- Riferimenti (sez. 7 dell'analisi): Serax e Robbe & Berking per la misura, tanto bianco, un'immagine per schermata, poche parole; Zwiesel per il vetro raccontato in luce; Schönwald per la porcellana bianca protagonista, qui portata nel colore della pagina.

### Interazione

Un solo gesto: l'indice del catalogo 2026/2027 con le pagine vere (Porcellana p. 10, Posateria 182, Vetro 232, Bar e mixology 290, Buffet e catering 378, Gastronorm 470). Clic, tocco, frecce, Home e Fine cambiano di colpo la foto, la riga del capitolo e il link "Apri il capitolo nel catalogo, p. N (PDF, 56 MB)", che apre il PDF del sito a #page=N. Bottoni veri con aria-pressed, area di 526x73 px a 1440 e 168x67 a 390; a 390 le voci stanno in due colonne sopra la foto. Nessuna dissolvenza, nessuna animazione allo scorrere; transizioni di 0,12 s solo sul colore di ciò che si tocca. Prova: `node _prova/script/finale_gesto.mjs <percorso>/sito/index.html`.

### Foto

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura, il furgone (largo, e quadrato per il telefono) | archivio Foralberg, `storia_camion2_foralberg.jpg` da foralberg.it/it/company | proprietà dell'azienda; diritti da chiedere |
| Chiusura, stand alla 38a Fiera di Padova | archivio Foralberg, `storia_fiera_1_foralberg.jpg`, "foto Giordani" | come sopra |
| Indice, Porcellana | Yusuf Çelik, Pexels 18677610 | Pexels License, verificata il 24/10/2026 |
| Indice, Posateria | Irina P, Pexels 12021478, ruotata | Pexels License |
| Indice, Vetro | Polina Kovaleva, Pexels 7283407 | Pexels License |
| Indice, Bar e mixology | Gülsüm Çoban, Pexels 33174185, tagliata senza la ciotola di frutta | Pexels License, verificata il 02/11/2026 |
| Indice, Buffet e catering | Sergei Starostin, Pexels 39388324 | Pexels License, verificata il 02/11/2026 |
| Indice, Gastronorm | Julia Filirovska, Pexels 7140435 | Pexels License |

Nessuna foto di repertorio è usata in un'altra home della campagna (controllo per ID su tutti i `*-Sito/assets/CREDITI.md` il 02/11/2026); nessuna immagine generata da IA; nessun marchio concorrente in primo piano. Nessuna legenda numerata sugli oggetti: solo didascalie sobrie sotto le foto d'archivio.

### Chiusura e piede

- Chiusura "b con foto", testo sopra e foto a tutta larghezza sotto (922 px a 1440): "Ci piace pensare di essere più di un semplice fornitore" (dalla home di oggi); 049 760955 grande con tel:+39049760955; Servizio clienti 335 142 6521 (tel:+393351426521) e servizioclienti@foralberg.it; "Vendite e showroom" ldesiderio@foralberg.it; via Cile 2 con "Apri la mappa"; orari di uffici e showroom.
- Piede: logo orizzontale vettoriale (monogramma e firma) con una riga su chi sono; newsletter "Novità e cataloghi" (email, bottone, casella del consenso; non invia nulla finché non è collegata a un servizio); quattro colonne Prodotti, Servizi (con "Acquisti PA, MePA e portali regionali"), Azienda (con La Vetrinetta e il suo Facebook, l'unico social verificato), Contatti; riga legale con Foralberg s.r.l., via Cile 2, P.IVA 00210840286, Privacy, Cookie, Note legali. Niente colonna Seguici: Foralberg non collega profili. A 390 Prodotti a sinistra, Servizi e Azienda a destra, Contatti a tutta larghezza.

### Controlli (2 novembre)

- Screenshot guardati a pezzi: 1440 (5396 px), 390 (5728), 320 (6015), 768 (6113), 1024 (4915), 1920 (5515). Nessuna sovrapposizione, nessun vuoto non voluto.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 560, 768, 860, 1024, 1180, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/finale_controlli.mjs`); console senza errori con file://.
- Gesto: clic, tocco, freccia giù, Fine e Home danno sempre foto, voce attiva e pagina coerenti a 1440 e a 390; altezza di #catalogo identica sui sei capitoli a ogni larghezza.
- Collegamenti: tel:+39049760955, tel:+393351426521, mailto:servizioclienti@foralberg.it, mailto:ldesiderio@foralberg.it, mappa Google su "Foralberg via Cile 2 35127 Padova".
- U+2014 assente dalla pagina, dagli script, da questa nota e dal LEGGIMI.
- `segnali.sh` a 1440: 0 soglie bloccanti su 10 (foto 35,6 %, una famiglia, mono 0 %, 19 filetti, nessuna etichetta sopra i titoli, nessuna freccia). Da guardare: H2 di una sola misura (56 px, più i 21 px del piede), voluto: la gerarchia la fanno il titolo a 106 px e le foto; quattro numeri grandi con etichetta, chiesti dal giudice al posto del paragrafo di numeri.
- A occhio: niente badge, tre box con icona, card col bordo, corsivo d'accento, gradienti, dissolvenze, hover che sbiadiscono, icone Lucide, legende a pallino.
