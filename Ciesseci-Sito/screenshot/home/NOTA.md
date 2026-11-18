# Home Ciesseci (CSC Factory): livello professionale, ritocco finale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. La home del 24 ottobre ("Il segno sul capo", con la maglietta di Pexels in apertura) è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot, con la sua NOTA).

Rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche le foto con `pro_img.py`). Gli screenshot sono all'ora simulata martedì 3 novembre 2026 alle 10:00 (`index.html?ora=2026-11-03T10:00`); poi `pro_controlli.mjs` scrive l'esito in `_prova/pro_controlli.json`.

Screenshot: `home-1440.jpg` (8286 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13570 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Orari e dove" al piede). Li ho guardati a pezzi a 1440 e a 390, accanto alle prime schermate dei 14 riferimenti e alle pagine intere di barth e Cly-Del. Ho controllato anche 320, 768 e 1024.

## Che cosa è cambiato nel ritocco finale (3 novembre 2026)

Il controllore aveva dato 6 su 10: "seria e ordinata, ma un titolare non pensa la voglio così". Ecco cosa ho cambiato.

1. **Prima schermata sgombra.** La tavola dei fatti è uscita dall'apertura e ora è una fascia grigia sua, in 4 colonne: Orari e dove, In negozio, Il tuo logo, Shop online. L'apertura ha due colonne, una per mestiere:
   - a sinistra il negozio: occhiello, titolo, mestiere in grassetto, stato, Chiama, WhatsApp e Come arrivare;
   - a destra lo showroom e, sotto, chi ha un logo: "Il preventivo è gratuito, anche per pochi pezzi", un solo bottone pieno "Manda il logo su WhatsApp", il link "oppure mandalo per email" e "Il logo non ce l'hai? Abbiamo uno studio di grafica".

   A 1440x900 la schermata finisce pulita a 788 px: sotto c'è solo il bordo della fascia grigia.
2. **Un solo bottone pieno per schermata.** Sopra i 900 px è pieno "Manda il logo su WhatsApp", perché da computer l'azione principale è mandare una richiesta (famiglia M). Sul telefono è pieno "Chiama 049 634423", a tutta larghezza. Gli altri bottoni hanno il solo bordo.
3. **Il gesto di scala.** Dopo i fatti c'è una fascia antracite con le parole della loro insegna di Via Zanella, a 96 px (64 a 1024, 40 a 390): "Servizio grafico · Servizio stampa" porta a "Il tuo logo", "Abbigliamento lavoro · Tempo libero" porta al negozio. Il punto è nel verde fluo della felpa 82. Sono testo, non un'immagine.
4. **Foto squadrate e meno foto.** Ho tolto il raggio da tutte le foto e dal riquadro del modulo; i 6 px restano solo su bottoni e campi. Ho tolto anche le due foto che non reggevano: i ricami RicaMarty (affollati, con la scritta tagliata) e il bancone vuoto con i neon. "È per un regalo?" è ora un blocco di tipografia con le categorie dello shop. In "Chi siamo" le cifre stanno accanto al testo. Lo showroom in apertura è tagliato 16:9 dal basso, così il soffitto si vede meno.
5. **Cifre vere al posto dei riempitivi.** Ho tolto "1 pezzo", "6 giorni" e "2019". Restano 1982 e 50 mm, e ho aggiunto "13 lavorazioni scritte sul nostro furgone" (l'elenco del furgone, SCHEDA par. 5) e "25 marche in negozio". Le marche sono 25 perché ho aggiunto Angiolina, che è tra i loghi del loro sito (01-analisi). 1982 ora compare nell'occhiello, nelle cifre e nel piede, non più sei volte.
6. **Meno ripetizioni.** Ho tolto il secondo stato da "Orari e dove" (resta la tabella con "oggi" e l'avviso delle ferie) e "Come arrivare" dalla fascia dei fatti. Il titolo di "Chi siamo" non ripete più il 1982.
7. **Uso.**
   - Con la scelta "lo mando su WhatsApp" il modulo compone un messaggio WhatsApp con la richiesta, in una nuova scheda, e il bottone dice "Prepara il messaggio WhatsApp".
   - Dopo l'invio compare il testo pronto con "Copia il testo", per chi usa solo la webmail.
   - Tutti i link WhatsApp e Instagram si aprono in una nuova scheda.
   - L'avviso delle ferie scrive l'anno.
   - Ad agosto e dal 20 dicembre al 7 gennaio, se in elenco non c'è una chiusura per quel periodo, sotto lo stato compare "Ad agosto e nelle feste di fine anno chiudiamo per qualche giorno: prima di venire, chiamaci."
   - Nella fascia dei fatti c'è anche "I cataloghi dei capi".
8. **Colore.** Il quarto token è ora `--fluo` #39E26B, il verde fluo della felpa 82 (01-analisi, direzione B), e prende il posto del verde scuro che serviva solo al passaggio del mouse (ora `filter:brightness(.82)`). È usato solo per il pallino "Aperto ora", i numeri dei passi del preventivo e i segni sull'antracite.

## Struttura

1. **Testata fissa** (80 px, 72 sul telefono): coccarda, "CSC Factory / Ciesseci, Mestrino", cinque voci (Negozio, Il tuo logo, Preventivo, Shop, Orari e dove) e "Chiama 049 634423". Il bottone ha il solo bordo finché si vede quello dell'apertura, poi diventa pieno.
2. **Apertura**, su due colonne:
   - a sinistra il negozio: "Mestrino (PD), dal 1982", poi "Stampa e ricamo: diffondiamo il tuo brand.", poi "**Abbigliamento da lavoro, scarpe antinfortunistiche e DPI**, con il tuo logo e il tuo nome.", lo stato calcolato e i bottoni Chiama, WhatsApp e Come arrivare;
   - a destra il logo: lo showroom vero, il preventivo gratuito, Manda il logo su WhatsApp, l'email e lo studio grafico.
3. **In breve** (grigio): orari e indirizzo, marche e cataloghi, i supporti del logo (ognuno è un link), lo shop.
4. **L'insegna** (antracite): i due mestieri a 96 px.
5. **In negozio** (bianco): le categorie in righe cliccabili, la foto loro di scarpe e giacche, "Le marche che trattiamo" in testo.
6. **Su cosa mettiamo il tuo logo** (antracite): quattro schede con le loro foto, poi "E poi" e lo studio grafico.
7. **Mandaci il logo** (verde del logo): tre passi, WhatsApp ed email, il modulo.
8. **È per un regalo?** (bianco, solo tipografia): categorie dello shop, foto caricata dal cliente, spedizione, RicaMarty.
9. **Chi siamo** (grigio): i tre amici di Rubano, Via Zanella dal 2019, quattro cifre.
10. **Orari e dove**: indirizzo, Come arrivare, Chiama, avviso ferie, tabella degli orari con "oggi", recapiti, la facciata con l'insegna.
11. **Piede** antracite in quattro colonne.

## Le 15 regole, una per una

Le misure vengono da `node _prova/script/pro_controlli.mjs`; in più ho guardato gli screenshot a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** La testata è `sticky` e il bottone "Chiama 049 634423" è alto 52 px. A metà pagina, a 1440 e a 390, si vede, è pieno e si tocca (`elementFromPoint`). Ci sono 6 link `tel:`, tutti `tel:+39049634423`.
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.**
   - A 1440x900: H1 con "scarpe antinfortunistiche", "Mestrino (PD), dal 1982", stato, Chiama (top 528), WhatsApp, Come arrivare e Manda il logo su WhatsApp, che è il bottone pieno.
   - A 390x844: Chiama largo 350 px su 350, a 409 px dall'alto.
3. **Immagine vera nell'apertura: passa, con riserva.** È lo showroom di Via Zanella, foto loro del 2019, in 16:9 tagliato dal basso: 628x353 a 1440, 350x233 a 390, mai ingrandito. Resta una foto da telefono e va rifatta (LEGGIMI).
4. **Zero repertorio: passa.** "indicativ", "unsplash", "pexels" e "stock" compaiono 0 volte. In `sito/img/` ci sono 7 foto loro e il logo; nessuna viene da `assets/esterne/`.
5. **Foto in serie: non passa per la luce.**
   - Passa sui formati: 2 a 1440 (16:9 in apertura, 3:2 nelle altre) e 1 a 390, con 1 didascalia su 7 foto e nessuna ingrandita.
   - Non passa sulla luce, che resta diversa: neon nello showroom, luce di finestra sul flat lay del 2018, cielo coperto su furgone e facciata, macro scura della ricamatrice.
   - Ho provato un bilanciamento del bianco comune: cambia pochissimo e sulla ricamatrice fa virare il verde, quindi non l'ho applicato. Ho tolto le due foto più lontane dalla serie (RicaMarty, bancone).
   - Serve il servizio fotografico del LEGGIMI.
6. **Palette dal marchio: passa.** I colori sono 4: il verde scuro della coccarda #00622B, il verde chiaro della coccarda #72BA6A, l'antracite del furgone e della facciata #24292C e il verde fluo della felpa 82 #39E26B, solo come segno. I neutri sono freddi, il fondo è bianco, non c'è beige.
7. **Scala corta e leggibile: passa.**
   - Misure: 8 a 1440 (14, 17, 20, 24, 32, 44, 64, 96) e 8 a 390 (14, 16, 18, 20, 24, 28, 34, 40).
   - Testo corrente a 17 e 16 px, niente sotto i 14 px.
   - H1 a 64 e 34 px, H2 a 44 e 28 px, l'insegna a 96 e 40 px.
8. **Due famiglie al massimo: passa.** Ce n'è una sola, Archivo. I titoli e l'insegna sono a larghezza 112 in 700, il testo e l'interfaccia a 100 in 400 e 700.
9. **Servizi in schede con la foto: passa.** Quattro schede in quattro colonne (due a 1024, una a 390), tutte cliccabili, con lo stesso taglio 3:2, ora squadrate. Le categorie del negozio restano righe di testo, perché per voce non ci sono foto vere.
10. **Almeno tre tipi di prove: non passa (2 su 4).**
    - Ci sono le cifre (1982, 50 mm, 13 lavorazioni, 25 marche) e la fascia "Le marche che trattiamo".
    - Mancano recensioni (nessuna leggibile), clienti con il nome e certificazioni. Non li ho inventati: sono chiesti al punto 12 del LEGGIMI.
11. **Lavori con un nome: non passa.** Nelle fonti non c'è nessun lavoro con cliente, luogo e anno. Nel LEGGIMI c'è la richiesta precisa: 3 lavori con nome, comune, anno, capi e tecnica, e dove metterli.
12. **Ritmo a blocchi: passa.**
    - I fondi si alternano: bianco, grigio (in breve), antracite (insegna), bianco (negozio), antracite (logo), verde pieno (preventivo), bianco (shop), grigio (chi siamo), bianco, piede antracite. Le sezioni a colore pieno, piede escluso, sono 3.
    - Le sezioni hanno 120 px sopra e sotto (96 la fascia in breve) a 1440, e 72 (64) a 390.
    - I margini sono di 80 e 20 px.
13. **Un solo sistema di bottoni: passa.**
    - I bottoni sono di due tipi, pieno e con il bordo, con raggio 6 px, alti 52 px e con testo a 17 px (16 sul telefono).
    - Ogni bottone di chiamata ha il numero.
    - Nell'apertura c'è un solo bottone pieno per larghezza.
14. **Modulo e "dove e quando" per il mestiere: passa, con riserva.**
    - Il modulo chiede su cosa va il logo (11 voci), quanti pezzi, per quando, il logo (lo allego alla mail, lo mando su WhatsApp, non ce l'ho) e l'idea.
    - Con il modulo vuoto risponde "Mancano: nome e cognome, telefono, su cosa va il logo."
    - Compilato, compone un'email con l'oggetto "Preventivo: supporto, nome", oppure un messaggio WhatsApp se si è scelto WhatsApp, e mostra "Copia il testo".
    - Il file non si allega (un mailto non porta allegati): il campo file va aggiunto quando il modulo si collega a un servizio (LEGGIMI).
    - Gli orari sono in tabella, "Come arrivare" apre il percorso su Google Maps, non c'è nessun iframe.
15. **Piede completo: passa.** Quattro colonne a 1440, testo di almeno 14 px. Ci sono ragione sociale, P.IVA e C.F., REA, capitale, sede legale, sede operativa, telefono, cellulare, email, orari, Come arrivare, lavorazioni, social con il sottotitolo, Privacy e Cookie. Certificazioni: nessuna nelle fonti.

## Compiti della scheda d'uso (par. 8): nessuno peggiora

- **Artigiano, 390x844.**
  - Senza scorrere ci sono lo stato "Aperto ora, chiude alle 12:30, riapre alle 14:00", Chiama (52 px, a tutta larghezza e pieno), WhatsApp e Come arrivare.
  - "Sabato 8:00-11:00" è a 1272 px e "Diadora" in testo a 1458 px, tutti e due entro due schermate (prima erano a 1059 e 1329).
  - Lo stato è giusto in 11 prove, tra cui 13:00 "riapre alle 14:00", sabato 11:30 "riapre lunedì", 8 dicembre e Pasquetta festivi, e 12 agosto 2025 "Chiuso per ferie, riapre lunedì 25 agosto". Il 21 luglio 2025 l'avviso dice "chiuso dal 7 agosto al 24 agosto 2025"; la vigilia di Natale 2026 compare l'invito a chiamare prima di venire.
- **Logo da applicare, 1440x900.**
  - Nella prima schermata ci sono "logo", "Stampa" e "ricamo", "Il preventivo è gratuito, anche per pochi pezzi", Manda il logo su WhatsApp (nuova scheda, testo pronto), l'email con l'oggetto e lo studio grafico (prima era a 3286 px).
  - Furgone, vetrine, striscioni, targhe, timbri e zerbini sono nominati e linkati a 961 px (prima 856).
  - I cataloghi sono anche nella fascia dei fatti, a circa 1000 px.
  - Il modulo con la scelta WhatsApp ora apre WhatsApp, non la posta.
- **Regalo, 390x844.** "Entra nello shop" con "la carichi tu" e "Spediamo in tutta Italia" è a 1826 px, entro due scorrimenti (prima 1700). Più in basso c'è la sezione dello shop, con le categorie, RicaMarty e Instagram.
- **Per tutte.**
  - Nessuna foto di repertorio, nessuna frase loro tra virgolette, nessun popup.
  - Nessuno scorrimento orizzontale a 320, 360, 390, 768, 1024, 1280, 1440 e 1920 px, e nessuna sovrapposizione.
  - Console senza errori.

## Controlli generali

- Collegamenti:
  - telefono: `tel:+39049634423`;
  - WhatsApp: `https://wa.me/393278831747`, sempre in una nuova scheda, anche con il testo "vi mando il logo";
  - email: `mailto:info@ciessecisrl.it`, con l'oggetto;
  - mappa, una sola: `https://www.google.com/maps/dir/?api=1&destination=Via+Zanella+1,+35035+Mestrino+PD`.

  Nessuna ancora è senza destinazione.
- Nessun U+2014 nella pagina, negli script, in questa nota, nel LEGGIMI e nei crediti.
- Dato strutturato `Store` con indirizzo, telefono e orari.

## Caratteri e licenze

- **Archivo** (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero. È servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`, licenza in `sito/fonts/OFL-Archivo.txt`).
- Foto: solo materiale del loro sito (`assets/originali/`), da usare con il loro permesso. Il logo è il PNG originale ridotto. Nessuna foto di repertorio, nessuna immagine generata, nessun disegno.

## Non applicato, apposta

- **Togliere gli orari dalla fascia dei fatti** (proposta del controllore): li ho tenuti, perché la scheda d'uso chiede "Sabato 8:00-11:00" entro due schermate sul telefono e la tabella completa è a circa 11.000 px. Ho tolto invece "Come arrivare" e il secondo stato.
- **Togliere "In negozio" dalla fascia dei fatti**: l'ho tenuto, perché la marca cercata ("Diadora") deve stare in testo entro uno scorrimento; nella sezione del negozio arriverebbe dopo i 2000 px.
- **Nascondere il "Chiama" della testata finché si vede quello dell'apertura** (proposta del cliente tipo): l'ho tenuto visibile con il solo bordo, perché la regola 1 vuole il telefono sempre nella testata.
- **Fascia dell'insegna su due righe a 96 px**, come proposto: a quella misura "Servizio grafico · Servizio stampa" è largo circa 2000 px. L'ho composta su due righe per ogni mestiere, come sull'insegna.
- **Apertura a tutto schermo** (barth, Odermatt, Budri): la foto migliore è di 1024 px e a tutta larghezza si ingrandirebbe. Il gesto di scala è l'insegna in tipografia.
- **Progetti con il nome, clienti in fascia, certificati** (famiglia M, punti 6, 7 e 8): non sono nelle fonti.
- **Classi di sicurezza delle scarpe (S1P, S3) e taglie in negozio**: non sono nelle fonti, quindi sono da chiedere (LEGGIMI).
