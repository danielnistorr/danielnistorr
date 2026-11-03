# Distilleria Rizzi, nuova home

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///; è la sorgente, si modifica a mano). La versione 1 com'era prima di questo passaggio («L'etichetta in piano», sito e screenshot) è copiata in `_prova/versione-1-originale/`. Per questa azienda non c'era una «versione 1 con l'uso» separata: l'uso viene dalla scheda `_prova/uso/SCHEDA.md` ed è stato costruito qui, insieme al livello professionale.
Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14 (in tre fogli), le pagine intere di Union e Joseph Brot a pezzi; come esempio del livello scelto, le note e il foglio di Unicar, Oby e Fornasiero.

Rifare tutto: `sh _prova/script/build_finale.sh` (immagini con `pro_img.py`, caratteri, screenshot all'ora simulata martedì 3 novembre 2026 alle 10 con `pro_shot.mjs`, poi `pro_controlli.mjs`). Prove d'uso: `node _prova/script/pro_uso.mjs` (stato dell'ufficio a varie ore, fascia del centenario a varie date, pagina senza JavaScript). Posizioni degli elementi: `node _prova/script/pro_misura.mjs <larghezza> <altezza> [mobile] [ora]`. Elementi che escono a destra: `node _prova/script/trova_largo.mjs <larghezza>`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (9818 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13873 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da «Spaccio e orari» al piede). Guardati a pezzi a 1440 e 390, accanto ai riferimenti, e a 320, 768 e 1024.

### Che cosa è cambiato, in breve

- **Struttura della famiglia B adattata a un liquorificio con spaccio**: fascia rossa «15 dicembre: la Distilleria Rizzi compie 100 anni» (si nasconde dal 16 dicembre); testata fissa con «Spaccio e orari» come prima voce e il bottone rosso con il numero dell'ufficio; apertura con il mestiere nel titolo, Mestrino e 1926 nell'occhiello, il loro biglietto («Distilleria Rizzi, di Maddalena e Alessandro: liquori, amari, sciroppi e aromi per la pasticceria a Mestrino dal 1926»), lo stato dell'ufficio calcolato sull'ora di Roma e sui festivi, la riga dei Contatti «Spaccio in via G. Negri 7: chiamaci prima di passare» con Chiama e Indicazioni, e la foto vera dello spaccio addobbato per Natale; subito sotto, su fondo scuro, il blocco per pasticcerie, bar e ristoranti (titolo loro, telefono d'ufficio, «Gusti e formati», le tre famiglie e i formati in una riga); poi «Allo spaccio» con i regali da prenotare per SMS e otto tessere di bottiglie; «Per la pasticceria» su fondo scuro (tre famiglie con i gusti per esteso, formati in cifre, «Listino su richiesta», clienti con il nome); il centenario su fondo rosso con la storia in quattro date; il manifesto e «Chi siamo» con Maddalena e Alessandro; «Spaccio e orari» come la scheda di un negozio di Union (foto della sede, stato, tabella degli orari, Chiama, Indicazioni, cellulari); «Scrivici» con il tipo di richiesta; piede in quattro colonne.
- **Tolti dalla versione 1**: il selettore delle sei bottiglie con il grado in cifre giganti (gioco da grafico, la SCHEDA lo dice falso per loro), il fondo color carta d'archivio, l'oggetto scontornato su fondo chiaro in apertura, «Lettere dalla distilleria» e la newsletter che non inviava nulla, il contatore delle 16.540 bottiglie (fermo a ottobre), il manifesto storico in chiusura (è di un collezionista, diritti da chiedere), il trattino lungo e i link a pagine che non esistono (i link vanno alle pagine vere del sito di oggi).
- **Tenuti dalla versione 1**: le due famiglie di caratteri (Zodiak e Switzer), il rosso del marchio, la scritta a pennello, le bottiglie vere del 2024, le parole loro. Il titolo «Liquori e amari dal 1926» è diventato «Liquori, amari e aromi per la pasticceria» (dal loro biglietto, così dice anche il mestiere che serve al professionista), con il 1926 nell'occhiello.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. «Spaccio e orari» prima voce; a 390, a metà pagina, il bottone «049 900 0053» della testata si vede e si tocca (48 px; a 1440 52 px). 11 link `tel:` (ufficio e i due cellulari).
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844. Mestiere nel titolo, «Mestrino, Padova, dal 1926» nell'occhiello, «Chiama 049 900 0053» pieno (a 390 a tutta larghezza, 358 su 358) e «Indicazioni». Anche lo stato dell'ufficio, la fascia dei 100 anni e, a 1440, il blocco per il professionista con le famiglie e i formati.
3. **Immagine vera in apertura**: PASSA. Lo spaccio vero, con il banco rosso, le confezioni regalo e le mensole delle loro bottiglie (`2025-08-5.jpg`, 4:5, a 412 px a 1440 da un originale di 1600, mai ingrandito; a 390 tagliata 4:3 sotto i bottoni). Nessun oggetto scontornato in apertura.
4. **Zero repertorio**: PASSA. «indicativ» 0; nessuna immagine da `assets/esterne/`, Unsplash o Pexels; nessuna illustrazione.
5. **Foto in serie**: PASSA con il limite del materiale. Due formati in pagina: 4:5 (spaccio, bottiglie, famiglie della pasticceria, taglio del nastro) e 4:3 (la sede). Le tre foto da telefono hanno lo stesso trattamento in `pro_img.py` (mediana leggera contro la nitidezza spinta dell'HDR, saturazione 0,84, contrasto 0,93); le bottiglie scontornate stanno tutte su tessere bianche alla stessa scala, così le altezze restano vere. Una sola didascalia (la sede, con la data) su 14 immagini. La luce non è la stessa (sono scatti diversi): va rifatta dal vero, vedi LEGGIMI.
6. **Palette dal marchio**: PASSA. Rosso #DD0000 (lo stesso del loro sito, del banco dello spaccio e dello scudo RIZZI; bianco su rosso 5,2:1), inchiostro #1C1815 della scritta a pennello, verde #17743A solo per «aperto ora», bianco e due grigi neutri (#F1F1EF per i fondi, #57534F per i testi secondari). Niente beige.
7. **Scala corta e leggibile**: PASSA. 1440: 200 (il «100» del centenario, il gesto di scala), 86, 56, 26, 21, 18, 16, 14 px; 390: 96, 42, 32, 22, 18, 17, 16, 14 px. Testo corrente 18/17 px; 14 px solo nella riga legale del piede. Titolo di apertura 86 px, interlinea 1,0 (390: 42 px).
8. **Due famiglie**: PASSA. Zodiak 400 per titoli, nomi, cifre e date; Switzer 400 e 600 per testo, etichette, bottoni e modulo. Due pesi.
9. **Schede con la foto**: PASSA. Otto tessere di liquori in quattro colonne (Carciofo, Garofano, Felsina, Prugna, Punch, Pinalpe, Fernet, Grappa Veneta), tutte 4:5, con nome, grado, frase loro e «Allo spaccio»; tutta la tessera è un link a «Spaccio e orari». Tre schede della pasticceria con foto 4:5, nome, gusti e «Nel catalogo» (tutta la scheda cliccabile). Sul telefono le tessere diventano righe con la stessa foto a sinistra.
10. **Almeno tre tipi di prove**: PASSA. Numeri (40+, 2 L, 5-225 L, 12 per cartone, e le date 1926, 1945, 2022, 2024); clienti con il nome (sei, presi dalla loro home «Fra i nostri migliori clienti», con tipo e comune); «Dove ci avete conosciuto» con La Difesa del Popolo, la mostra «Padova da gustare» e due fiere, al posto delle certificazioni che non hanno. Recensioni: nessuna nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: NON SI APPLICA (bottega e liquorificio, nessun lavoro su commessa nelle fonti). Il posto va alla storia in quattro date, con gli anni a 56 px.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: il professionista e la pasticceria nell'inchiostro, il centenario nel rosso; liquori e spaccio su grigio chiaro. Spazio tra le sezioni 120 px a 1440 e 64 px a 390; margini 80 px e 16 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno (rosso, bianco sul rosso) e con il bordo, raggio 4 px, 52 px a 1440 e 48 px a 390, testo 16 px; ogni bottone di chiamata contiene il numero.
14. **Modulo e «dove e quando»**: PASSA. Modulo in home con il tipo di richiesta (regalo o prenotazione allo spaccio, ordine o listino per pasticceria bar e ristorante, distribuzione, altro), nome, telefono, email, attività e comune, messaggio: compone un'email con oggetto e campi (mailto), da collegare a un servizio (LEGGIMI). Per lo spaccio: stato di adesso, tabella degli orari con la riga di oggi, Chiama, Indicazioni (`google.com/maps/dir` con il nome e via Guido Negri 7, per non finire alla Bonollo), SMS e telefono di Maddalena e Alessandro. Nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Logo, ragione sociale, P.IVA, PEC, indirizzo con Indicazioni, orari, telefono ed email cliccabili, prodotti, social con il sottotitolo, consumo responsabile, Privacy e Cookie; quattro colonne, testo di almeno 14 px.

### Uso (compiti della SCHEDA)

- Privato, 390x844: senza scorrere il bottone `tel:+390499000053` (48 px, testata e apertura), lo stato dell'ufficio («Ufficio aperto ora, fino alle 12:30» alle 10 di martedì), la riga «Spaccio in via G. Negri 7: chiamaci prima di passare», Indicazioni a tutta larghezza, la fascia «15 dicembre: compiamo 100 anni» e l'inizio della foto dello spaccio. I due SMS dei regali stanno a 1617 px, i primi cinque liquori finiscono a 2523 px (entro due scorrimenti, 2532). Nessun prezzo in pagina.
- Professionista, 1440x900: senza scorrere «Oltre 40 aromi e ingredienti per la pasticceria professionale», il telefono d'ufficio, «Gusti e formati», le tre famiglie e i formati (bottiglioni da 2 L, Vodka 70° da 5 a 225 L, listino su richiesta). Nella sezione: gusti per esteso, formati in cifre, telefono con gli orari, email cliccabile con oggetto «Richiesta listino pasticceria», link al catalogo vero.
- Chi li ha appena conosciuti, 390: ogni liquore della SCHEDA ha foto, nome e una frase loro; dalle tessere si arriva con un tocco a «Spaccio e orari», e sotto la griglia ci sono Chiama e Indicazioni; il centenario rimanda a telefono, Facebook e Instagram, nessun modulo.
- `pro_uso.mjs`: stato giusto alle 8:15, 10, 12:45, 15, 17:30, venerdì sera, sabato, 8 dicembre, Pasquetta 2027; fascia visibile fino al 15 dicembre compreso e nascosta dal 16 (il titolo diventa «Il 15 dicembre 2026 abbiamo compiuto 100 anni»); senza JavaScript lo stato mostra gli orari e la fascia resta.

### Controlli generali

- Nessuno scorrimento orizzontale a 320, 360, 390, 414, 600, 601, 768, 1024, 1099, 1100, 1280, 1440 e 1920 (corretto a 320 il bottone «SMS ad Alessandro», che usciva di 12 px).
- Nessuna sovrapposizione negli screenshot a 320, 390, 768, 1024 e 1440.
- Collegamenti: `tel:+390499000053`, `tel:+393513070422`, `tel:+393513858112`, `sms:` agli stessi cellulari con il testo pronto, `mailto:info@distilleriarizzi.com` (anche con oggetto), `mailto:distilleriarizzi@pec.it`, Google Maps sul percorso per «Distilleria Rizzi, Via Guido Negri 7, 35035 Mestrino PD». Ancore interne tutte presenti.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Zodiak (400) e Switzer (400, 600), Indian Type Foundry, da Fontshare, ITF Free Font License 2.0 (uso commerciale gratuito, anche serviti dal proprio sito): file in `sito/fonts/` con il testo della licenza `LICENZA-ITF-FFL.txt`. Switzer 600 scaricato il 3/11/2026 dal pacchetto completo (`_prova/crawl/fontshare/sw/`); tolti dalla pagina Zodiak 300 e Switzer 500.

### Non applicato, apposta

- Apertura a tutto schermo con una foto (famiglia B, punto 2): nessuna foto loro regge 1440x900; lo spaccio sta alla sua misura (412 px, nativa 1600).
- Facciata del negozio grande: la sede c'è solo la sera dell'inaugurazione, in HDR; è in «Spaccio e orari» a 628 px, non oltre.
- Novità di stagione con foto: il centenario è la novità, senza foto finché non c'è la festa.
- Newsletter e Instagram incorporato: tolti; i social sono link con il sottotitolo.
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
