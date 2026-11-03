# Home di AIT Studio, Stefano Aiti: livello professionale, ritocco finale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La home di prima ("Comunicazione silenziosa"), con la sua NOTA, è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot).

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs`, poi `pro_controlli.mjs`). Prove d'uso della scheda: `node _prova/script/pro_uso.mjs`. Scorrimento orizzontale, elemento per elemento: `node _prova/script/trova_largo.mjs <larghezza>`. Larghezze delle lettere in Chromium: `node _prova/script/kern_prova.mjs`.

Screenshot (stessi nomi di prima): `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (dal preventivo al piede). Misure: circa 10100 px a 1440 e 12700 a 390.

## Livello professionale

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati per questo ritocco: le prime schermate a 1440 e 390 di tutti e 14 e le pagine intere di Odermatt, Budri e Holzrausch, a pezzi (prima erano state viste Cly-Del e barth).

### Che cosa cambia nel ritocco finale (dal controllo del livello e dalle prove dei clienti tipo)

- **Un gesto di scala in apertura.** Prima le foto erano tre tessere di 411x308 a 1440 e tre miniature di 96x96 a 390. Ora:
  - a 1440 il titolo sta a sinistra (8 colonne) e a destra ci sono la riga del luogo e i due bottoni impilati;
  - sotto, la porta Cantieri è grande (7 colonne, 737x414, 16:9): la stesa notturna con il semirimorchio Salima, con il marchio leggibile;
  - accanto, Prodotti e Architettura sono due porte più piccole, con la foto e i clienti, e sotto c'è la riga dei matrimoni;
  - a 390 la porta Cantieri è a tutta larghezza (350x197) e le altre due sono righe con la miniatura da 80 px. Tutte e tre stanno nella prima schermata.
- **Luogo e prova in chiaro.** L'occhiello dice "AIT Studio, Stefano Aiti" (chi conosce AIT Studio dai mezzi ha subito la conferma). Sotto il titolo, in 18 px nero (17 a 390): "Studio fotografico a Mestrino (PD), dal 2008. Lavoriamo in Veneto e in Trentino."
- **Bottoni senza doppi spazi.** L'etichetta è chiusa in un solo span ("Chiama Stefano 348 748 58 71", "Chiama per la data 348 748 58 71").
- **Spaziatura delle lettere.** "Stef ano", "St udio", "Mest rino": Chromium su Linux arrotondava le larghezze delle lettere (la f a 16 px passava da 4,8 a 7 px, misurato con `kern_prova.mjs`). Con `text-rendering:geometricPrecision` sul body la f torna a 5,1 px e le parole si chiudono.
- **Pesi distanti.** Switzer 400 e 700 (prima 400 e 600), come chiede A4.
- **Cantieri senza schemi ripetuti.** Dopo le quattro schede, "Lavori recenti 2022-2023" apre con la foto di Mirano a tutta larghezza (fino a 1600 px, 16:9) e prosegue con Carpane e Massenza affiancati (6+6). "Avete un cantiere da documentare? Scriveteci" viene dopo le foto, non prima.
- **Lavori con anno e tre dati.** "Salima, Mirano (VE) · marzo 2023 · reportage di cantiere", "Girardini, Carpane (VI) · ottobre 2022 · cantiere Anas, reportage", "Salima, Massenza (TN) · marzo 2022 · parco mezzi, Volvo FL250". Mese e anno vengono dall'EXIF dei file originali. Tolto "all'alba" da Mirano: l'EXIF dice ore 19:19.
- **Prodotti con quattro foto e il nome.** Testo a lato (4 colonne, fermo mentre si scorre) e quattro still life in 2x2: Calearo (prima c'era solo nella porta, senza nome), Marijke, Calegaro, Superoro. A 390 restano in 2x2, così la sezione è corta.
- **Architettura speculare e con Studio 4 Marmicolor.** Foto grande a destra (Artufficio, Banca Prealpi), a sinistra la scala di Studio 4 Marmicolor e la Fornace Morandi, ognuna con il nome. Tolta Brendola, che ripeteva Artufficio.
- **Clienti come testo.** I nomi sono composti in 44 px (28 a 390), separati da un punto, con il campo in 14 px maiuscolo sopra ogni gruppo. Prima erano tre colonne in 24 px.
- **Numeri veri.** Tolti "2 lauree" e "5 servizi". Ora: 1995, 2008, "2 persone: ideazione, scatto ed editing, tutto fatto da noi", "6 banche e casse rurali arredate da Artufficio, fotografate da noi" (01-analisi, sez. 1). Le lauree Iuav sono nel testo dello studio.
- **Ritmo.** Il chiaro passa da #EDEFEE a #E2E4E3 (stesso grigio del logo), così i blocchi chiari si distinguono dal bianco. Il testo secondario #565A59 sul chiaro resta a 5,5:1.
- **Menu e contatti.** Il menu ora ha Cantieri e mezzi, Prodotti, Architettura, Clienti, Matrimoni, Preventivo (6 voci); sul telefono c'è anche "Scrivici a info@aitistudio.it". "Lo studio" è il primo blocco dopo l'apertura e non serve nel menu. Le email nei contatti sono bersagli alti 44 px.
- **Modulo.** La tendina parte da "Scegli il tipo di lavoro". L'email va a info@aitistudio.it per i lavori di cantiere e a stefano@stefanoaiti.com per gli altri, e sotto il bottone è scritto a quale indirizzo parte. La frase sugli allegati è in nero a 16 px.
- **Matrimoni dopo il preventivo.** Per chi viene per lavoro non è più un intoppo tra i clienti e il modulo. Chi cerca i matrimoni ha la riga in apertura e la voce nel menu.

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile: PASSA.** Testata `position:sticky`, 80 px a 1440 e 72 a 390. A 390, scorsa a metà pagina, il bottone "348 748 58 71" (48 px) si vede e si tocca. In pagina ci sono 5 link `tel:`. Voce di richiesta M: "Preventivo" nel menu e "Scrivici" in testata a 1440.
2. **Prima schermata con mestiere, luogo, prova, azione: PASSA** a 1440x900 e 390x844. Mestiere nell'H1; luogo e prova ("Mestrino (PD), dal 2008") nella riga in 18 px nero sotto il titolo; azione "Chiama Stefano 348 748 58 71", a 390 a tutta larghezza.
3. **Immagine vera nell'apertura: PASSA.** La stesa notturna di AIT Studio con il semirimorchio Salima, grande: 737x414 a 1440, 350x197 a 390. Accanto l'antenna Calearo e la scala di Studio 4 Marmicolor, foto loro.
4. **Zero repertorio: PASSA.** "indicativ", Pexels, Unsplash ed `esterne/` compaiono 0 volte. Le uniche immagini non fotografiche sono i due SVG del logo.
5. **Foto in serie: PASSA IN PARTE, con una deroga dichiarata.**
   - Formati: 2 a 1440 (16:9 e 4:3), 3 a 390 (16:9, 4:3 e 1:1 per le due miniature).
   - Didascalie: 18 foto, 10 con il nome sotto (3 lavori di cantiere con i dati, 4 still life, 3 di architettura), cioè circa 1 ogni 2. La prima stesura diceva "6 su 19": il conteggio era sbagliato. Le righe che descrivevano solo ciò che si vede ("vaso di cubetti metallici", "la facciata in mattoni" e simili) sono tolte.
   - Deroga: per un fotografo il nome del cliente sotto la foto è il fatto che conta (A7: cliente, luogo, anno), e la scheda chiede "ogni foto con il nome del cliente". Restano solo nomi e dati, mai descrizioni.
   - Luce: non può essere una sola, perché lo studio vende tre generi (notte di cantiere, bianco di sala di posa, interni). Ogni genere sta nella sua sezione, e le foto di cantiere sono calmate insieme (saturazione 86 %, contrasto 96 %).
6. **Palette dal marchio: PASSA.** Cinque token: bianco, nero del logo (#0B0A0A dal #040000), grigio del logo #AAAEAD, chiaro #E2E4E3 (lo stesso grigio schiarito), testo secondario #565A59. Niente beige.
7. **Scala corta e leggibile: PASSA.** 6 misure a 1440 (64, 44, 24, 18, 16, 14) e 8 a 390 (44, 34, 28, 20, 17, 16, 15, 14). Testo corrente 18 px a 1440 e 17 a 390. Niente sotto i 14 px. H1 64 px a 1440 (fascia M 60-70) e 34 a 390 (34-40).
8. **Due famiglie al massimo: PASSA.** Una sola, Switzer, come barth: 700 per titoli, nomi, cifre e bottoni, 400 per il testo.
9. **Servizi in schede con foto: PASSA.** Quattro schede per le costruzioni, 4 colonne a 1440 (2 a 1024 e 768, 1 a 390), foto 4:3, nome, una riga con le loro parole e "Chiedi un preventivo". Tutta la scheda è il link e porta al modulo con il tipo già scelto (provato: "Livree dei mezzi" arriva nel campo, e l'email va a info@aitistudio.it).
10. **Almeno tre tipi di prove: PASSA (3 su 4).** Clienti con il nome (17, per campo, come testo grande); quattro numeri dalle fonti (1995, 2008, 2 persone, 6 banche e casse rurali); tre recensioni vere con nome, mese e fonte (Matrimonio.com, solo dei matrimoni; il comune non è nella fonte). Certificazioni: nessuna (TAU Visual da confermare, nel LEGGIMI).
11. **I lavori hanno un nome: PASSA.** Tre lavori di cantiere con cliente, luogo, mese e anno e il tipo di servizio; Mirano è a tutta larghezza (1440 px), Carpane e Massenza a 628 px ciascuno. In più tre lavori di architettura con il cliente (anni da chiedere, nel LEGGIMI).
12. **Ritmo a blocchi: PASSA.** Due blocchi neri (cantieri, clienti) più il piede, tre chiari (studio, architettura, matrimoni) e tre bianchi alternati. Spazio tra le sezioni 128 px a 1440 e 72 a 390. Margini 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: PASSA.** Pieno e con il bordo, raggio 2 px ovunque, 52 px (48 in testata), testo 16 px in 700. I bottoni di chiamata contengono il numero, senza doppi spazi.
14. **Modulo e "dove e quando": PASSA IN PARTE.** Nome, azienda, telefono, email, cosa fotografare (tendina vuota all'inizio, con sette lavori più "Altro"), dove, entro quando, per quale uso, messaggio; mailto con oggetto e campi (provato). Indirizzo con "Vai alla mappa", zone scritte, nessun iframe. Manca il campo allegato chiesto per M: un mailto non porta file e un campo finto non funzionerebbe. È il primo campo da aggiungere quando il modulo sarà collegato a un servizio (LEGGIMI).
15. **Piede completo: PASSA, senza orari né certificazioni** (non sono nelle fonti, chiesti nel LEGGIMI). Quattro colonne: logo e mestiere, lavori, lo studio, contatti; riga legale con ragione sociale, P.IVA, PEC, Privacy e Cookie; testo di almeno 14 px.

### Prove d'uso della scheda (`_prova/script/pro_uso.mjs` e screenshot)

- **Impresa di costruzioni, 390x844.** Senza scorrere: "AIT Studio" nell'occhiello, "cantieri" nel titolo, la stesa Salima grande e leggibile, due `tel:` (testata e bottone a tutta larghezza). Un tocco sulla porta porta alla sezione. Livree, video, Salima, Girardini e Martini Silvestro sono nell'introduzione della sezione; le zone sono lì e nei contatti. Nel menu c'è "Scrivici a info@aitistudio.it". Come prima o meglio.
- **Azienda o architetto, 1440x900.** Senza scorrere: mestiere, i tre generi, Mestrino, telefono e "Scrivici". Un clic su "Prodotti" porta a quattro still life con il cliente sotto, Calearo compreso; un clic su "Architettura" a tre lavori con il cliente, Studio 4 Marmicolor compreso. "Clienti" e "Preventivo" sono nel menu. Il preventivo dice cosa scrivere e ha l'indirizzo con la mappa; il blocco matrimoni non sta più in mezzo.
- **Coppia di sposi, 390x844.** "Matrimoni" è nel menu (un tocco: voto 4,9, prezzo, "Chiama per la data" e "Vai a Weddgraphy" visibili) e c'è la riga con il voto subito sotto le porte, all'inizio della seconda schermata.

### Controlli generali

- Screenshot guardati a pezzi a 1440 e 390 (interi e prime schermate) e a 320, 768 e 1024; il menu aperto a 390.
- **Scorrimento orizzontale**: nessuno a 320, 390, 768, 1024, 1280, 1440 e 1920. Trovato e corretto durante il lavoro: i nomi dei clienti senza spazi tra i separatori (ora il punto resta attaccato al nome che lo precede e non apre mai una riga).
- **Immagini ingrandite oltre la misura del file**: nessuna, a nessuna larghezza (corretti i `sizes` per 1024, 1280 e 1920).
- **Collegamenti**: `tel:+393487485871` 5 volte; `mailto:` per stefano@stefanoaiti.com (con oggetto), info@aitistudio.it, info@weddgraphy.it e la PEC; Google Maps su Via Galileo Galilei 40, 35035 Mestrino; weddgraphy.it e la scheda di Matrimonio.com; nessuna àncora rotta. Restano i link a `privacy/` e `cookie/`, pagine da fare.
- **U+2014**: nessuno, nella pagina, in questa NOTA, nel LEGGIMI, nei CREDITI e negli script.

### Caratteri e licenze

Switzer (Indian Type Foundry, da Fontshare), pesi 400 e 700, con la ITF Free Font License, che permette l'uso commerciale gratuito. I file woff2 sono serviti dalla pagina in `sito/fonts/`. Il 700 è stato scaricato da Fontshare il 3/11/2026; la copia è in `assets/fonts-scaricati/`.
