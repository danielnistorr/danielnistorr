# Home Ciesseci (CSC Factory): livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. La home di prima ("Il segno sul capo", con la maglietta di Pexels in apertura) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot, con la sua NOTA).

Rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche le foto con `pro_img.py`); screenshot all'ora simulata martedì 3 novembre 2026 alle 10:00 (`index.html?ora=2026-11-03T10:00`), poi `pro_controlli.mjs` (esito in `_prova/pro_controlli.json`).

Screenshot (stessi nomi di prima): `home-1440.jpg` (7576 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13464 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti; anche 320, 768 e 1024.

## Livello professionale (3 novembre 2026)

Richiesta: "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito" e "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente". Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di barth e Cly-Del (a pezzi), più le prove già fatte su Unicar, Oby e Fornasiero.

Per Ciesseci non esisteva una "versione 1 con l'uso": la home di prima era quella del 24 ottobre. In questo passaggio ho fatto insieme l'uso della scheda (`_prova/uso/SCHEDA.md`) e il livello professionale.

### L'idea

È un negozio di paese con il laboratorio dietro, che fa alla pari due mestieri, come dice l'insegna: vestire chi lavora (scarpe antinfortunistiche, divise, DPI) e mettere il logo su tutto. La pagina parte da lì: la prima schermata dice se è aperto, fa chiamare, scrivere su WhatsApp e arrivare in Via Zanella, mostra il loro showroom vero con la parete delle scarpe e fa mandare il logo. Dalla famiglia M prende l'impianto: dichiarazione di competenza grande, competenze in schede con le foto, cifre in fila, piede a quattro colonne. Dal bancone prende il tono: dal tu, frasi loro ("Ti aspettiamo a Mestrino", "Farti un preventivo per noi è rapido e non ti costerà nulla", "Su richiesta mettiamo anche il tuo nome e quello dei tuoi dipendenti"), nessuna frase tra virgolette.

### Struttura (famiglia M adattata)

1. **Testata fissa** (80 px, 72 sul telefono): coccarda, "CSC Factory / Ciesseci, Mestrino", cinque voci (Negozio, Il tuo logo, Preventivo, Shop, Orari e dove) e il bottone "Chiama 049 634423", bordato finché si vede quello dell'apertura, poi pieno.
2. **Apertura**: occhiello "Mestrino (PD), dal 1982"; titolo loro "Stampa e ricamo: diffondiamo il tuo brand." e, nello stesso H1, il mestiere "Abbigliamento da lavoro, scarpe antinfortunistiche e DPI, con il tuo logo e il tuo nome."; stato "Aperto ora / Chiuso ora" calcolato; Chiama, WhatsApp, Come arrivare; "Hai un logo da mettere su capi, furgoni o vetrine? Il preventivo è gratuito." con Manda il logo (WhatsApp con il testo pronto) e Per email (oggetto e traccia); a destra lo showroom vero. Sotto, la tavola di cinque fatti: Orari, Dove, In negozio (con le marche in testo), Il tuo logo (ogni supporto è un link), Shop online.
3. **In negozio** (grigio): abbigliamento da lavoro, scarpe per settore, DPI e alta visibilità, tempo libero, cataloghi, in righe tutte cliccabili; la foto loro degli scaffali di scarpe e giacche; la fascia "Le marche che trattiamo" in testo (scarpe, abbigliamento, capi da stampare).
4. **Su cosa mettiamo il tuo logo** (antracite, il grigio del furgone): quattro schede con le loro foto (capi e divise, ricamo, furgoni e vetrine, targhe plex e gadget), poi "E poi" con striscioni, zerbini, timbri, incisioni laser, tampografia, studio grafico, e "Il logo non ce l'hai? Abbiamo uno studio di grafica".
5. **Mandaci il logo** (verde del logo): tre passi, WhatsApp e email, il modulo per il mestiere.
6. **È per un regalo?**: shop, foto caricata dal cliente, "Spediamo in tutta Italia", RicaMarty.
7. **Chi siamo** (grigio): i tre amici di Rubano, Via Zanella dal 2019, il bancone con la coccarda; cinque cifre in verde a 64 px.
8. **Orari e dove**: indirizzo, Come arrivare, stato, tabella degli orari con "oggi", telefono, cellulare e WhatsApp, email; la facciata con l'insegna.
9. **Piede** antracite in quattro colonne.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs`, più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `sticky`, bottone "Chiama 049 634423" alto 52 px (sotto i 360 px solo il numero). A metà pagina, a 1440 e a 390, si vede e si tocca (`elementFromPoint`). 6 link `tel:`, tutti `tel:+39049634423`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440x900 e 390x844: H1 con "scarpe antinfortunistiche", "Mestrino (PD), dal 1982", stato, Chiama (a 390 largo 350 px su 350, a 409 px dall'alto), WhatsApp e Come arrivare; a 1440 anche Manda il logo e Per email.
3. **Immagine vera nell'apertura: passa, con riserva.** Lo showroom di Via Zanella (foto loro del 2019, 1024 px), mostrato a 628 x 471 a 1440 e 350 x 233 a 390, mai ingrandito. È una foto da telefono: va rifatta (LEGGIMI). Nessuna illustrazione.
4. **Zero repertorio: passa.** "indicativ" 0 volte; tolte le cinque foto Unsplash e Pexels (maglietta, coni, telaio, pressa, laser); in `sito/img/` solo foto loro e il logo.
5. **Foto in serie: passa.** Nove foto loro, stesso trattamento (`pro_img.py`: livelli, saturazione 0,94, nitidezza leggera); due formati a 1440 (4:3 nell'apertura, 3:2 altrove), uno solo a 390; una didascalia su nove foto (la facciata); nessuna ingrandita (file da 640 e 1020 px).
6. **Palette dal marchio: passa.** Verde scuro della coccarda #00622B (con il suo scuro per il passaggio del mouse), verde chiaro della coccarda #72BA6A solo su fondi scuri, antracite #24292C del furgone e della facciata; neutri freddi. Fondo bianco, nessun beige. Il rosa fluo della shopper e il verde fluo della felpa ci sono nelle loro foto, non come colori della pagina.
7. **Scala corta e leggibile: passa.** 7 misure a 1440 (14, 17, 20, 24, 32, 44, 64) e 7 a 390 (14, 16, 18, 20, 24, 28, 34); testo 17 e 16 px; nulla sotto i 14 px; H1 64 e 34 px, H2 44 e 28 (fascia della famiglia M).
8. **Due famiglie al massimo: passa.** Una sola, Archivo: titoli a larghezza 112 % in 700 (come le lettere della coccarda), testo e interfaccia al 100 % in 400 e 700.
9. **Servizi in schede con la foto: passa.** Quattro schede in quattro colonne (due a 1024, una a 390), tutte cliccabili, stesso taglio 3:2, con nome, riga e link. Le foto sono loro ma deboli (1024 px, telefono): da rifare.
10. **Almeno tre tipi di prove: non passa (2 su 4).** Cinque cifre dalle fonti (1982, 2019, 50 mm, 1 pezzo, 6 giorni) e la fascia delle marche con la didascalia. Mancano recensioni (nessuna leggibile: Google 429, Facebook con login, Rete Imprese "Nessuna recensione"), clienti con il nome e certificazioni: non inventati, da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Nelle fonti non c'è nessun lavoro con cliente, luogo e anno; il furgone e i plex sono loro. Da chiedere tre lavori con il permesso del cliente (LEGGIMI).
12. **Ritmo a blocchi: passa.** Grigio (negozio), antracite (logo), verde pieno (preventivo), grigio (chi siamo), piede antracite; sezioni a 120 px a 1440 e 72 a 390; margini 80 e 20 px.
13. **Un solo sistema di bottoni: passa.** Pieno e bordato, raggio 6 px, 52 px, testo 17 (16 sul telefono); sui fondi scuri la stessa forma in bianco; ogni chiamata ha il numero.
14. **Modulo e "dove e quando" per il mestiere: passa, con riserva.** Modulo con su cosa va il logo (11 voci), quanti pezzi, per quando, il logo (lo allego alla mail, lo mando su WhatsApp, non ce l'ho), idea; controlla nome, telefono e supporto e compone un'email con oggetto "Preventivo: supporto, nome". Il file non si allega dal modulo (un mailto non porta allegati): la pagina lo dice e porta a WhatsApp; il campo file va aggiunto quando si collega un servizio (LEGGIMI). Orari in tabella, "Come arrivare" al percorso Google Maps, nessun iframe.
15. **Piede completo: passa.** Quattro colonne a 1440, testo di almeno 14 px: ragione sociale, P.IVA e C.F., REA, capitale, sede legale, indirizzo operativo, telefono, cellulare, email, orari, Come arrivare, lavorazioni, social con il sottotitolo, Privacy e Cookie. Certificazioni: nessuna nelle fonti.

### Compiti della scheda d'uso (par. 8)

- **Artigiano, 390x844**: senza scorrere stato "Aperto ora, chiude alle 12:30, riapre alle 14:00", Chiama (`tel:+39049634423`, 52 px), WhatsApp (`wa.me/393278831747`), Come arrivare (Via Zanella 1, Mestrino), la foto dello showroom intera (233 px). "Diadora" in testo a 1326 px (meno di uno scorrimento oltre la prima schermata), "Sabato 8:00-11:00" a 1056 px; la riga delle ferie compare da 30 giorni prima della chiusura. Stato giusto in 11 prove: martedì 10:00 aperto, 13:00 "riapre alle 14:00", 19:00 "riapre domani alle 8:00", sabato 10:30 "chiude alle 11:00", sabato 11:30 "riapre lunedì", domenica, 8 dicembre e Pasquetta festivi, vigilia di Natale sera "riapre lunedì", 21 luglio 2025 con l'avviso "Chiusura estiva: chiuso dal 7 agosto al 24 agosto", 12 agosto 2025 "Chiuso per ferie, riapre lunedì 25 agosto alle 8:00".
- **Logo da applicare, 1440x900**: "logo", "Stampa" e "ricamo" nella prima schermata, Manda il logo (WhatsApp con il testo) e Per email (oggetto e traccia); furgone, vetrine, striscioni, targhe, timbri e zerbini nominati e linkati nella tavola dei fatti a 856 px; preventivo gratuito e "anche pochi pezzi" sopra i bottoni e nei fatti, "anche su singolo pezzo" nella scheda dei plex; Cataloghi nella sezione del negozio (1677 px).
- **Regalo, 390x844**: "Entra nello shop" con "la carichi tu" e "Spediamo in tutta Italia" a 1700 px (due scorrimenti), poi la sezione dello shop con RicaMarty e Instagram.
- **Per tutte**: nessuna foto di repertorio, nessuna frase loro tra virgolette, nessun popup, nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 px, nessuna sovrapposizione nell'apertura e nella testata.

### Controlli generali

- Collegamenti: `tel:+39049634423`, `https://wa.me/393278831747` (anche con il testo "vi mando il logo"), `mailto:info@ciessecisrl.it` (con oggetto), una sola mappa: `https://www.google.com/maps/dir/?api=1&destination=Via+Zanella+1,+35035+Mestrino+PD`. Nessuna ancora senza destinazione. Le pagine interne (`abbigliamento/...`, `pubblicita/...`, `shop/`) sono i percorsi del sito di oggi.
- Console senza errori; con JavaScript spento la riga dello stato mostra gli orari della settimana.
- Nessun U+2014 nella pagina, negli script, in questa nota, nel LEGGIMI e nei crediti.
- Dato strutturato `Store` con indirizzo, telefono e orari.

### Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`, licenza in `sito/fonts/OFL-Archivo.txt`).
- Foto: solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso; il logo è il PNG originale ridotto. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

### Non applicato, apposta

- Apertura a tutto schermo con il logotipo o una foto grande (barth, Cly-Del): la foto migliore è di 1024 px e a tutta larghezza si ingrandirebbe; il titolo resta il gesto tipografico e la foto sta a 628 px.
- Progetti con il nome del cliente, clienti in fascia, certificati scaricabili (punti 6, 7, 8 della famiglia M): non ci sono nelle fonti.
- Newsletter del piede: tolta (non inviava nulla); in pagina resta un solo modulo, quello del preventivo.
- Il "1982" gigante e la felpa 82 come segno grafico: la scheda d'uso li indica come cosa "da grafico"; il 1982 è nell'occhiello e nelle cifre, la felpa nella foto della prima scheda.
