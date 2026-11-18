# Distilleria Rizzi, nuova home

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///; è la sorgente, si modifica a mano). La versione 1 com'era prima del livello professionale («L'etichetta in piano», sito e screenshot) è in `_prova/versione-1-originale/`. L'uso viene dalla scheda `_prova/uso/SCHEDA.md`.
Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 di tutti e 14 (in un foglio), Union a 1440 e a pagina intera a pezzi, Joseph Brot a pagina intera a pezzi.

Rifare tutto: `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, caratteri, screenshot all'ora simulata martedì 3 novembre 2026 alle 10 con `pro_shot.mjs`, poi `pro_controlli.mjs`). Prove d'uso: `node _prova/script/pro_uso.mjs` (stato dell'ufficio a varie ore, vigilie di Natale e Capodanno, fascia del centenario e avviso di Natale a varie date, gusti chiusi sul telefono, pagina senza JavaScript).

Screenshot: `home-1440.jpg` (9963 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13958 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da «Spaccio e orari» al piede). Guardati a pezzi a 1440 e 390, e a 320, 768, 1024 e 1440x790 (finestra vera di un portatile).

### Ritocco finale (3 novembre 2026), dal controllore del livello e dai clienti tipo

- **Apertura rifatta (difetto bloccante)**: non più lo schema comune della campagna (serif a sinistra, foto 4:5 in un riquadro di 411 px, pallino verde). Ora sono due metà a tutta altezza della finestra: a sinistra un blocco pieno nel rosso del marchio con la scritta a pennello in bianco larga 520 px (il gesto di scala, a 390 è larga 300 px), poi l'occhiello, l'H1 bianco a 86 px, il biglietto, lo stato dell'ufficio in un'etichetta bianca e i bottoni (pieno bianco con il testo rosso, bordo bianco). A destra lo spaccio vero a tutto campo (originale 1600x1600, mai ingrandito) e sotto la foto, sull'inchiostro, il blocco per pasticcerie, bar, ristoranti e distributori con l'ufficio e «Gusti, formati e listino». L'altezza segue la finestra: a 1440x790 (portatile vero) il blocco del professionista e i suoi bottoni restano dentro la prima schermata. Logo della testata portato a 240 px (142 a 390, di più non ci sta accanto al bottone del telefono e al menu).
- **Niente più tessere bianche**: le bottiglie sono WebP con l'alfa, ricavati dai PNG originali, tutte alla stessa scala (il Pinalpe da 75 cl resta più basso), direttamente sul grigio della sezione, con il nome e la frase sotto un filetto. I tre gruppi della pasticceria stanno direttamente sull'inchiostro, in 4:3 (prima 4:5 in riquadri bianchi da 411x514): il blocco scuro non ha più buchi bianchi e i gusti salgono.
- **Testo delle schede a 18 px (17 a 390)**: frasi delle bottiglie, date della storia, clienti, numeri, stampa e gusti. 16 px solo per etichette, gradi, «Prenota per SMS», «Nel catalogo», le voci dei gusti (dt) e i bottoni.
- **Un solo H2 «Oltre 40 aromi...»**: nel blocco dell'apertura c'è un occhiello e un paragrafo («Sciroppi di zucchero, aromi alcolici a 70°, creme e vini per la pasticceria»), non un secondo titolo. L'occhiello è lo stesso della sezione: «Per pasticcerie, bar, ristoranti e distributori».
- **Per il professionista**: la striscia dei numeri sta subito sotto il titolo della sezione e la scheda «Listino su richiesta», prima delle famiglie (dopo il clic su «Gusti, formati e listino» si vede già); i numeri sono 40+ aromi, 20 gusti di sciroppi, 2 L, 5-225 L (il «12 bottiglie per cartone» è diventato una riga della scheda del listino: «Liquori e amari anche in cartoni da 12 bottiglie da 100 cl»). «Il catalogo completo è sul sito di oggi» è diventato «Catalogo completo della pasticceria su distilleriarizzi.com ↗», che si apre in una nuova scheda come «Nel catalogo».
- **Gusti apribili**: ogni elenco dei gusti è un `<details>` «Tutti i gusti», aperto sul computer e chiuso sul telefono (senza JavaScript resta aperto).
- **Per il privato**: «aperto anche ai privati» nella riga dello spaccio dell'apertura e sotto le bottiglie; nella scheda «Regali e cofanetti» cosa si regala («Cofanetti da 3 bottigliette da 20 cl, e liquori, amari, punch e grappe in bottiglia da 100 cl»), il prezzo «per SMS o al telefono» e, dal 1 novembre al 24 dicembre, «Le aperture dello spaccio prima di Natale le annunciamo su Facebook» con il link. Le otto bottiglie portano a quella scheda («Prenota per SMS»), non più in fondo alla pagina; sotto la griglia restano Chiama e Indicazioni.
- **«Non sono prodotti da "bere"»** (frase della loro pagina `amari`, ambigua su un sito di liquori) è diventata «Non sono liquori da bere di fretta: assaggiali, scoprili, innamorati».
- **La sede per riconoscerla**: in «Spaccio e orari» la foto della facciata è in cima alla scheda (anche sul telefono, dove prima era in fondo), con la didascalia «L'ingresso dello spaccio in via G. Negri 7...». È a 9829 px a 390 (prima 10496).
- **Stato dell'ufficio il 24 e il 31 dicembre**: «Orari del 24 dicembre da confermare, chiamaci o guarda Facebook»; il giorno prima «riapre domani 24 dicembre, orari da confermare».
- **Taglio del nastro più piccolo**: 4:5 stretto sui due volti, a 400 px a 1440 (prima 517x646), da rifare dal vero.
- **Minori**: `strong,b{font-weight:600}` (niente più 700 sintetico); miniature delle bottiglie a 390 tutte 104x130 (`aspect-ratio:4/5`, `align-self:flex-start`); a 1024 e 768 le bottiglie restano in quattro colonne; a 320 la fascia del centenario non va più su due righe e i numeri si impilano.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. «Spaccio e orari» prima voce; a 390, a metà pagina, il bottone «049 900 0053» della testata si vede e si tocca (48 px; a 1440 52 px). 11 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844 (e a 1440x790). Mestiere nell'H1, «Mestrino, Padova, dal 1926» nell'occhiello, la fascia dei 100 anni, «Chiama 049 900 0053» (a 390 a tutta larghezza, 358 su 358) e «Indicazioni». A 1440 anche il blocco del professionista con «Gusti, formati e listino».
3. **Immagine vera in apertura**: PASSA. Lo spaccio vero (`2025-08-5.jpg`) a tutto campo nella metà destra, a 1440 circa 650x515 px da un originale di 1600; a 390 4:3 a tutta larghezza. La qualità resta media (HDR da telefono): vedi LEGGIMI, foto 1.
4. **Zero repertorio**: PASSA. «indicativ» 0; nessuna immagine da `assets/esterne/`, Unsplash o Pexels; nessuna illustrazione.
5. **Foto in serie**: PASSA sui formati e sulle didascalie, CON IL LIMITE del materiale sulla luce. Formati: a 1440 tre (lo spaccio circa 1,26 secondo l'altezza della finestra, 0,80 bottiglie e taglio del nastro, 1,33 sede e gruppi della pasticceria); a 390 due (1,33 e 0,80). Una didascalia su 14 foto. Stesso trattamento per le tre foto da telefono (`pro_img.py`), bottiglie tutte scontornate alla stessa scala sul fondo della sezione; la luce degli scatti resta diversa (spaccio e sede in HDR, nastro al flash): va rifatta dal vero, LEGGIMI.
6. **Palette dal marchio**: PASSA. Rosso #DD0000 (sito, banco dello spaccio, scudo RIZZI), inchiostro #1C1815 (scritta a pennello), verde #17743A solo per «aperto ora», bianco e due grigi neutri. Niente beige.
7. **Scala corta e leggibile**: PASSA. 1440: 200, 86, 56, 26, 21, 18, 16, 14 px; 390: 96, 42, 32, 22, 18, 17, 16, 14 px. Testo corrente 18/17 px, ora anche nelle schede; 14 px solo nella riga legale. H1 86 px interlinea 1,0 (390: 42 px).
8. **Due famiglie**: PASSA. Zodiak 400 per titoli, nomi, cifre e date; Switzer 400 e 600 per testo, etichette, bottoni e modulo. Due pesi, senza più il 700 sintetico.
9. **Schede con la foto**: PASSA. Otto bottiglie in quattro colonne, tutte 4:5, con nome, grado, frase e «Prenota per SMS» (tutta la scheda è un link alla scheda dei regali); tre schede della pasticceria in 4:3 con nome, gusti e «Nel catalogo» (tutta la scheda cliccabile, il sommario dei gusti resta toccabile sopra).
10. **Almeno tre tipi di prove**: PASSA. Numeri (40+, 20 gusti, 2 L, 5-225 L e le date 1926, 1945, 2022, 2024), sei clienti con il nome, tipo e comune, «Dove ci avete conosciuto» (stampa, mostra, due fiere) al posto delle certificazioni che non hanno. Recensioni: nessuna nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: NON SI APPLICA (bottega e liquorificio, nessun lavoro su commessa nelle fonti). Al loro posto la storia in quattro date.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: l'apertura (rosso e inchiostro), la pasticceria nell'inchiostro, il centenario nel rosso; liquori e spaccio su grigio chiaro. Spazio tra le sezioni 120 px a 1440 e 64 px a 390; margini 80 e 16 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno (rosso; bianco sul rosso) e con il bordo, raggio 4 px, 52 px a 1440 e 48 px a 390, testo 16 px; ogni bottone di chiamata contiene il numero.
14. **Modulo e «dove e quando»**: PASSA. Modulo con il tipo di richiesta (4 caselle), compone un'email con oggetto e campi (mailto), da collegare a un servizio (LEGGIMI). Spaccio: foto della facciata, stato, tabella degli orari con la riga di oggi, Chiama, Indicazioni (`google.com/maps/dir` con nome e via Guido Negri 7), cellulari. Nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Logo, ragione sociale, P.IVA, PEC, indirizzo con Indicazioni, orari, telefono ed email cliccabili, prodotti, social con il sottotitolo, consumo responsabile, Privacy e Cookie; quattro colonne, testo di almeno 14 px.

### Uso (compiti della SCHEDA e dei clienti tipo)

- Privato, 390x844: senza scorrere Chiama (testata e apertura, 48 px), «Ufficio aperto ora, fino alle 12:30» alle 10 di martedì, «Spaccio in via G. Negri 7, aperto anche ai privati: chiamaci prima di passare», Indicazioni a tutta larghezza, la fascia «15 dicembre: compiamo 100 anni». I bottoni SMS dei regali sono a 1785 px (entro due scorrimenti; prima 1605, la scheda dice ora anche cofanetti, formati e Facebook). Nessun prezzo in pagina.
- Professionista, 1440x900 e 1440x790: senza scorrere il blocco con le famiglie, i formati, l'ufficio e «Gusti, formati e listino»; dopo il clic la striscia dei numeri è già nella finestra (a 661 px), con la scheda «Listino su richiesta» (orari, telefono, email con oggetto, cartoni da 12x100 cl, catalogo su distilleriarizzi.com) accanto al titolo.
- Chi li ha appena conosciuti, 390: ogni liquore ha foto, nome e una frase loro; «Prenota per SMS» porta ai bottoni SMS; sotto la griglia Chiama e Indicazioni; il centenario rimanda a telefono, Facebook e Instagram.
- `pro_uso.mjs`: stato giusto alle 8:15, 10, 12:45, 15, 17:30, venerdì sera, sabato, 8 dicembre, 23 dicembre sera, 24, 25 e 31 dicembre, Pasquetta 2027; fascia visibile fino al 15 dicembre compreso; avviso di Natale dal 1 novembre al 24 dicembre; gusti chiusi a 390; senza JavaScript lo stato mostra gli orari, la fascia resta e i gusti sono aperti.

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 390, 414, 600, 601, 768, 1024, 1099, 1100, 1280, 1440 e 1920.
- Nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024, 1440x790 e 1440x900.
- Collegamenti: `tel:+390499000053`, `tel:` e `sms:` ai due cellulari, `mailto:` (anche con oggetto) e PEC, Google Maps sul percorso per via Guido Negri 7. Ancore interne tutte presenti.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI e negli script toccati.

### Caratteri e licenze

Zodiak (400) e Switzer (400, 600), Indian Type Foundry, da Fontshare, ITF Free Font License 2.0 (uso commerciale gratuito, anche serviti dal proprio sito): file in `sito/fonts/` con il testo della licenza `LICENZA-ITF-FFL.txt`.

### Non applicato, apposta

- Foto della sede accanto a «Indicazioni» nell'apertura (proposta dal cliente tipo): l'apertura tiene lo spaccio, che è il luogo dei regali in questa stagione e passa la regola 3; la facciata è in cima a «Spaccio e orari», con la didascalia per riconoscere l'ingresso.
- Togliere i cellulari dalla scheda dello spaccio (ripetuti): restano, perché la SCHEDA li vuole anche fra i contatti; la pagina a 390 è passata da 13873 a 13958 px per le righe nuove dei regali, pur con i gusti chiusi.
- Ombra di appoggio sotto le bottiglie: non aggiunta, sarebbe finta (la versione 1 l'aveva tolta per questo).
- Recensioni e certificazioni: non ce ne sono nelle fonti.

---

## Versione 1 (24 ottobre 2026), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-originale/`.


Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (solo quelle usate, WebP e JPEG in più larghezze), caratteri in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini, caratteri, pagina, screenshot). Alta 4717 px a 1440 (piede compreso), 6206 px a 390.

### Idea

Su un fondo color carta c'è una sola bottiglia vera di Rizzi, ritta su un filo sottile che attraversa la pagina come il piano di un tavolo d'archivio. Il patrimonio di Rizzi sono le sei etichette di casa, non un alambicco che oggi non c'è più. Con il nome di un concorrente la pagina non regge, perché le etichette sono solo loro. La pagina si chiude sul manifesto storico «i classici prodotti Rizzi Padova»: Bitter, Pinalpe e Crema Marsala disegnati in un'altra epoca.

### Cosa è cambiato in questo giro (dal giudizio cieco)

- **Legende tolte del tutto**, con i pallini e i filetti (erano lo stesso gesto della home di Mario Agnoletto). Via anche la funzione `legende()` e i dati delle posizioni. Resta un solo gesto: i sei nomi che scambiano la bottiglia.
- **Prima schermata ricomposta in tre parti**: titolo e nomi nelle colonne 1-6, la bottiglia al centro delle colonne 7-9, a destra (colonne 10-12) la sua scheda con il grado grande in Zodiak 300 (92 px, cifre tabellari), il nome in Zodiak a 22 px e uso e formato in Switzer. Il grado vero diventa l'elemento grafico che cambia con la scelta. A 1440 accanto alla bottiglia non c'è nessun filetto né pallino.
- **Bottiglie rifatte** (`finale_img.py`): tolta l'ombra portata laterale, resta solo l'ombra di contatto ellittica sul filo (circa 12 px a schermo, opacità 0,25). Scontorno più stretto di circa 5 px sull'originale e sfumato. Mediana e sfocatura leggera sull'originale prima della riduzione, per togliere gli aloni della maschera di contrasto del telefono e la grana del liquido. Tolto il lembo chiaro del sigillo di carta sul lato destro del tappo della Felsina e del Punch, che a schermo sembrava un alone. La bottiglia è alta 700 px al massimo (prima 755).
- **Alchermes ridotto** da 730 a 450 px, senza didascalia, ritto sullo stesso filo che chiude la sezione pasticceria, a destra delle famiglie. Nessuna bottiglia della seconda schermata supera i 450 px.
- **Striscia delle spezie Pexels tolta**, con la sua didascalia sbagliata (nominava agrumi e mele che nel taglio non c'erano).
- **Sezione "mestiere" rimessa in griglia**: tre righe che partono tutte dal margine di 64 px. Pasticceria (titolo, famiglie, Vodka e link a sinistra, Alchermes a destra); "Facciamo tutto noi, dall'inizio alla fine" con il titolo nelle colonne 1-6 e il testo nelle 7-12, prima riga allineata; una riga nuova sul "per chi" con la frase grande "Lavoriamo soprattutto con pasticcerie, bar, ristoranti e distributori del Veneto" e lo spaccio aperto ai privati dal 29/09/2024 (fatti da `01-analisi.md`, sez. 1 e 3).
- **Chiusura con un prodotto Rizzi**: al posto della bottiglia generica di Pexels c'è il manifesto storico «i classici prodotti RIZZI PADOVA» (Bitter, Pinalpe, Crema Marsala all'uovo), dalla foto della mostra «Padova da gustare» 2025 nella libreria media dell'azienda. Raddrizzato in prospettiva con PIL sui quattro angoli interni della cornice misurati a zoom 3x, ritagliato dentro la cornice, HDR del telefono calmato. Sta a destra fino al bordo, nelle sue proporzioni (nessun taglio), con una didascalia che dice cos'è e di chi è la collezione.
- **Difetti di esecuzione**: "1926-2026" nel piede con il trattino non separabile (U+2011); tra 1001 e 1180 px il logo del piede va su una riga propria e le colonne sono larghe 3/12 (a 1024 nessuna voce va a capo); sotto i 1000 px la chiusura resta a due colonne ma il manifesto tiene le sue proporzioni e si appoggia al piede, quindi a 768 il titolo sta su 3 righe e l'indirizzo su una; la newsletter scrive un riscontro in un `role="status"` dopo l'invio; la voce "Liquori e amari" della testata va a `/liquori-e-amari/`; il bottone Menu diventa "Chiudi" quando è aperto e il menu si chiude anche con Esc (il fuoco torna sul bottone); tolti i due `link rel=preload` dei caratteri (con `font-display:swap` il guadagno era minimo e in file:// davano errori CORS).
- A 1024x768 l'apertura scende a 760 px e la bottiglia si riduce con l'altezza della finestra, così il filo resta nella prima schermata.

### Caratteri e colori

- **Zodiak** 300 e 400 (Indian Type Foundry, Fontshare) per titoli, nomi delle etichette, gradi, anni e telefono: serif dritto ad alto contrasto, mai corsivo, vicino alle lettere dello scudo RIZZI. Riferimenti: Fernet-Branca e Cocchi (la bottiglia storica accanto a un titolo grande e sicuro), Marzadro (bianco e serif).
- **Switzer** 400 e 500 (stessa fonderia) per testi e piede, dai pacchetti completi con la crenatura. Le cifre sono tabellari: gradi, orari, P.IVA e formati incolonnati.
- **Licenza**: ITF Free Font License 2.0, uso commerciale gratuito anche in self-hosting. Testo in `sito/fonts/LICENZA-ITF-FFL.txt`.
- Colori: carta #F3EEE6, inchiostro #1C1815 (15,3:1), grigio testi #5B524A (6,6:1 sulla carta, 6,2:1 sul piede #ECE6DC), rosso etichetta #B8231C solo per il nome scelto, il campo del centenario (carta su rosso 5,5:1) e il passaggio sui link.

### Interazione (un solo gesto)

I sei nomi formano un gruppo di scelta (role radio): tocco, clic, frecce, Home e Fine, fuoco visibile in rosso. Al cambio la bottiglia si scambia di netto, senza dissolvenza (immagini precaricate nella misura giusta), e cambiano grado, nome, uso e formato nella scheda (`aria-live`). Le sole transizioni, di 0,12 s, riguardano il colore dei nomi e del bottone della newsletter. Niente animazioni allo scorrere, niente effetti sul cursore.

### Foto, origine e licenza

- Bottiglie Felsina, Fernet, Garofano, Pinalpe, Prugna, Punch Arancio (`assets/originali/2024-02-*.png`) e Alchermes (`2023-02-bott-alchermes.png`): di Distilleria Rizzi, dalla libreria media del loro sito. WebP con alfa a 480, 760 e 1000 px.
- Manifesto storico: foto `2025-04-1000098150-01.jpeg` della libreria media dell'azienda (mostra «Padova da gustare», Palazzo Santo Stefano, 2025). L'originale è della collezione di Simone Marzari: i diritti di riproduzione vanno chiesti a lui (vedi LEGGIMI). JPEG a 400 e 588 px (588 è la misura nativa dopo il raddrizzamento, nessun ingrandimento).
- Le due foto Pexels del giro precedente (spezie di Kunuk, bottiglia di Reding) non sono più in pagina. Nessuna immagine è generata dall'IA; nessuna foto di repertorio.
- Logo: PNG ricolorati in inchiostro (scritta a pennello nella testata, calice e scritta nel piede), non ricostruiti in SVG perché il tratto a pennello non si rifà in modo fedele.
- Newsletter: c'è, perché ci sono il centenario, i cofanetti delle feste, le fiere e i clienti privati dello spaccio. Non invia nulla finché non è collegata a un servizio (LEGGIMI).

### Controlli fatti

- Screenshot a 1440 e 390 (consegna) e a 320, 768, 1024 e 1920 (controlli in `_prova/tmp-finale/controlli/`), guardati a pezzi da 1600 px. Nessuna sovrapposizione: a 768 la scheda non tocca più la bottiglia, a 1024 il manifesto non è tagliato.
- scrollWidth uguale a innerWidth a 320, 360, 390, 414, 600, 700, 701, 768, 900, 1000, 1001, 1024, 1180, 1181, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/collaudo_finale.mjs`).
- Gesto da tastiera a 1440: frecce su tutte e sei le bottiglie (grado, nome e file cambiano), Fine, Home e freccia a sinistra dal primo all'ultimo. Al tocco a 390 (dpr 2): Punch, Pinalpe, Garofano, Felsina; aree di tocco alte 44 px. Menu a 390: "Chiudi" con aria-expanded true, Esc lo chiude e riporta il fuoco.
- Newsletter: dopo l'invio con email e consenso compare "Grazie: ti scriveremo per confermare l'iscrizione."
- Collegamenti: tel:+390499000053 (testata, menu, chiusura), mailto:info@distilleriarizzi.com, mappa Google con l'indirizzo di via G. Negri 7; ancore interne tutte presenti. Nessuna immagine rotta.
- Console: nessun errore servendo la cartella con `python3 -m http.server`, e nessun errore neanche in file:// (preload tolti).
- Carattere U+2014: nessuno in pagina, negli script, in questa nota e nel LEGGIMI.
- Segnali da IA (`segnali.sh`): 17 soglie su 18 passano; il titolo a sinistra con paragrafo a destra ora compare una volta sola. Resta fuori l'area coperta da foto: 13,8 % contro il 35 %. È voluto: il giudice ha chiesto di togliere la striscia di repertorio e di ridurre l'Alchermes perché nulla facesse concorrenza al solo oggetto, e lo strumento conta solo in parte le bottiglie scontornate su carta. Non ho aggiunto foto di riempimento.
