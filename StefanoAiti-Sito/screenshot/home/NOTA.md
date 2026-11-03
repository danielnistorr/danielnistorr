# Home di AIT Studio, Stefano Aiti: livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La home di prima ("Comunicazione silenziosa"), con la sua NOTA, è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot).

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot con `pro_shoot.mjs`, poi `pro_controlli.mjs`). Prove d'uso della scheda: `node _prova/script/pro_uso.mjs`. Scorrimento orizzontale, elemento per elemento: `node _prova/script/trova_largo.mjs <larghezza>`.

Screenshot (stessi nomi di prima): `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da Matrimoni al piede). Misure: 9128 px a 1440, 13293 a 390.

## Livello professionale

Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Cly-Del e barth (a pezzi), e la prova già vista dal committente (Unicar, Oby, Fornasiero, colonna di destra di `_invio/zona/home/livello-professionale.jpg`).

### Che cosa è cambiato, in breve

- **Uso prima di tutto (scheda `_prova/uso/SCHEDA.md`).** La home di prima apriva con un aforisma, un indice di nomi alla maniera di una galleria e i cantieri a due terzi della pagina. Ora:
  - in testata, fissa, c'è il bottone "Chiama 348 748 58 71" (a 390 il numero con la cornetta) e, a 1440, "Scrivici" (mailto con oggetto);
  - l'apertura dice il mestiere e il luogo e ha le tre porte con foto vere: Cantieri e mezzi, Prodotti in sala di posa, Architettura e interni, ognuna con i suoi clienti;
  - sotto le porte c'è l'uscita "Matrimoni: Stefano Aiti Weddgraphy, 4,9 su 5 su Matrimonio.com".
- **Struttura M adattata a uno studio fotografico:**
  1. testata sobria con le cinque voci e i due bottoni;
  2. apertura con la dichiarazione del mestiere (H1 "Foto e video per le aziende: cantieri, prodotti, architetture") e le tre porte, che fanno da settori;
  3. lo studio (la sala di posa vera, `a4`, con Stefano e Giulia) e quattro numeri: 1995, 2008, 2 lauree Iuav, 5 servizi per le costruzioni;
  4. cantieri e mezzi su blocco nero: quattro schede di servizio con foto (reportage, foto aziendali, livree, video e siti) e tre lavori con il nome del cliente e il luogo;
  5. prodotti in sala di posa: tre still life con il nome del cliente;
  6. architettura e interni: tre lavori con il cliente;
  7. clienti per campo, su nero, e in chiusura la frase di Stefano, usata una volta sola;
  8. matrimoni: voto, prezzo, tre recensioni vere, Weddgraphy e "Chiama per la data";
  9. preventivo: modulo per il mestiere, telefono grande, email, indirizzo con "Vai alla mappa", zone;
  10. piede in quattro colonne.
- **Foto, decisione "niente".** Nessuna foto di repertorio (i Pexels di `assets/esterne/` non erano e non sono usati), nessuna illustrazione, nessuna schermata di sito o mockup usati come foto. Sono 19 foto, tutte di Stefano Aiti o di AIT Studio, in tre formati. Le foto di cantiere di aitistudio.it sono calmate come serie: saturazione all'86 % e contrasto al 96 %, perché l'HDR è spinto.
- **Colori del marchio.** Tolto il fondo carta #F6F5F2 (beige di comodo). Ora ci sono:
  - il bianco;
  - il nero del logo (#0B0A0A, dal #040000);
  - il grigio del logo #AAAEAD per filetti e testo secondario sul nero;
  - il chiaro #EDEFEE, lo stesso grigio schiarito, per i blocchi chiari;
  - il grigio dei testi secondari #565A59 (7:1 sul bianco).
- **Caratteri.** Resta la sola famiglia della home di prima, Switzer, con due pesi distanti: 400 e 600 (il 500 è tolto).

### Esito regola per regola (controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile: PASSA.**
   - Testata `position:sticky`. A 390, scorsa a metà pagina, il bottone "348 748 58 71" (48 px) si vede e si tocca.
   - In pagina ci sono 5 link `tel:`. La voce di richiesta della famiglia M c'è: "Scrivici" in testata, "Chiedi un preventivo" nell'apertura e "Preventivo e contatti" nel menu del telefono.
2. **Prima schermata con mestiere, luogo, prova, azione: PASSA** a 1440x900 e 390x844.
   - Il mestiere è nell'H1; il luogo e la prova sono nell'occhiello ("Stefano Aiti, studio fotografico a Mestrino (PD), dal 2008"); i clienti stanno sotto ogni porta.
   - L'azione è "Chiama Stefano 348 748 58 71", che a 390 è a tutta larghezza (350 px).
   - A 390 si vedono anche le tre porte intere e il link ai matrimoni.
3. **Immagine vera nell'apertura: PASSA.**
   - La prima porta è la stesa notturna con il semirimorchio Salima: un mezzo con il marchio, in cantiere. Accanto ci sono l'antenna Calearo e la scala di Studio 4 Marmicolor.
   - L'antenna è un oggetto su fondo bianco, ma qui è il lavoro stesso che lo studio vende, ed è una sua foto da 9 su 10.
   - Le persone (Stefano e Giulia nella sala di posa) sono il primo blocco dopo l'apertura.
4. **Zero repertorio: PASSA.** "indicativ" compare 0 volte; Pexels, Unsplash ed `esterne/` 0 volte.
5. **Foto in serie: PASSA, con un limite dichiarato.**
   - Tre formati: 4:3 (porte, schede, lavori), 1:1 (solo le miniature delle porte sul telefono) e 16:9 (la sala di posa, nel suo formato nativo).
   - Ci sono 6 nomi di lavoro sotto 19 foto, quindi meno di una didascalia ogni tre foto.
   - Il trattamento è comune dentro ogni sezione: i cantieri sono calmati insieme, gli still life e l'architettura sono lasciati con la loro luce pulita.
   - Il limite: la luce non può essere una sola, perché lo studio vende tre generi diversi (notte di cantiere, bianco di sala di posa, interni). Ogni genere sta nella sua sezione.
6. **Palette dal marchio: PASSA.** Cinque token, cioè bianco, nero e grigio del logo, più due grigi neutri. Niente beige.
7. **Scala corta e leggibile: PASSA.**
   - A 1440 ci sono 6 misure: 64, 44, 24, 18, 16, 14. A 390 ce ne sono 8: 44, 34, 28, 20, 17, 16, 15, 14.
   - Il testo corrente è a 18 px a 1440 e a 17 a 390; le introduzioni a 24 e 20. Il 16 è solo per etichette, dati sotto le foto e piede.
   - Niente sotto i 14 px; il 14 è solo nelle etichette in maiuscolo spaziato e nella riga legale.
   - Il titolo è a 64 px a 1440 e a 34 a 390, nella fascia M (60-70 e 34-40).
8. **Due famiglie al massimo: PASSA.** Una sola, Switzer, come barth: 600 per titoli, nomi, cifre e bottoni, 400 per il testo.
9. **Servizi in schede con foto: PASSA.**
   - Quattro schede per le costruzioni, in 4 colonne a 1440 (2 a 1024 e 768, 1 a 390), con foto 4:3, nome, una riga con le loro parole e "Chiedi un preventivo". Tutta la scheda è un link.
   - Il link porta al modulo con il tipo di lavoro già scelto: provato con `pro_uso.mjs`, "Livree dei mezzi" arriva nel campo.
   - I siti web stanno nella scheda "Video e siti web", perché non c'è una foto di un sito che non sia una schermata.
10. **Almeno tre tipi di prove: PASSA (3 su 4).**
    - Recensioni: tre testi veri da Matrimonio.com con nome, mese e fonte. Il comune non è nella fonte.
    - Numeri: quattro (1995, 2008, 2, 5).
    - Clienti con il nome: 17, divisi per campo.
    - Certificazioni: non ne hanno. Il socio TAU Visual va confermato ed è nel LEGGIMI.
11. **I lavori hanno un nome: PASSA IN PARTE.**
    - Sei lavori con il cliente e il luogo o l'oggetto, per esempio "Salima, Mirano (VE), cantiere stradale all'alba, reportage" e "Girardini, Cantiere Anas a Carpane". In ogni sezione ce n'è uno largo più di metà pagina (845 px a 1440).
    - Manca l'anno di ogni lavoro: le fonti dicono solo che il materiale di cantiere è di aitistudio.it (2024-2025) e il portfolio del 2017. Va chiesto (LEGGIMI).
12. **Ritmo a blocchi: PASSA.**
    - Oltre al piede ci sono due blocchi neri (cantieri, clienti) e tre chiari (studio, architettura, matrimoni).
    - Spazio tra le sezioni: 128 px a 1440 e 72 a 390. Margini: 80 px a 1440 e 20 a 390.
13. **Un solo sistema di bottoni: PASSA.**
    - Due varianti, piena e con il bordo, raggio 2 px ovunque. Altezza 52 px (48 in testata), testo 16 px in 600.
    - Ogni bottone di chiamata contiene il numero: "Chiama 348 748 58 71", "Chiama Stefano 348 748 58 71", "Chiama per la data 348 748 58 71".
14. **Modulo e "dove e quando": PASSA.**
    - Il modulo ha i campi di uno studio che lavora su commessa: nome, azienda, telefono, email, cosa fotografare (tendina con i sette lavori più "Altro"), dove, entro quando, per quale uso e due righe sul lavoro.
    - "Prepara l'email" compone un mailto a stefano@stefanoaiti.com con l'oggetto "Richiesta di preventivo: tipo, azienda" e tutti i campi nel testo. Va collegato a un servizio (LEGGIMI).
    - L'allegato: un mailto non porta file, quindi la riga sotto il bottone dice di allegare planimetrie, logo o foto dei mezzi nella mail che si apre.
    - Le zone: "In Veneto e in Trentino: Padova, Mirano, Carpane, Massenza". L'indirizzo ha il bottone "Vai alla mappa" (Google Maps). Nessun iframe.
15. **Piede completo: PASSA, senza orari né certificazioni** (non sono nelle fonti).
    - Quattro colonne: logo e mestiere, lavori, lo studio (indirizzo, mappa, zone), contatti (telefono, due email, preventivo).
    - Riga legale: "Stefano Aiti Fotografo, ditta individuale, P.IVA 04257170284, PEC", Privacy, Cookie. Testo di almeno 14 px.
    - Il logo AIT STUDIO è quello tracciato, con il nero passato al bianco per il fondo nero.

### Prove d'uso della scheda (`_prova/script/pro_uso.mjs` e screenshot)

- **Impresa di costruzioni, 390x844.**
  - Senza scorrere ci sono "Cantieri e mezzi" con la foto della stesa Salima e due `tel:`: la testata e il bottone a tutta larghezza.
  - Un tocco sulla porta porta alla sezione.
  - Livree dei mezzi, video e i nomi Salima, Girardini e Martini Silvestro sono già nell'introduzione della sezione, nella prima schermata. Le schede di livree e video stanno a 1548 e 1983 px dall'inizio della sezione.
  - Le zone (Veneto e Trentino) sono nell'introduzione e nei contatti.
- **Azienda o architetto, 1440x900.**
  - Senza scorrere ci sono il mestiere, i tre generi, Mestrino, il telefono e "Scrivici" (mailto).
  - Un clic su "Prodotti in sala di posa" porta a tre still life con il cliente (Marijke, Calegaro, Superoro).
  - Il preventivo dice cosa scrivere e ha l'indirizzo con la mappa.
  - La sala di posa vera, con le due persone, è il primo blocco dopo l'apertura.
- **Coppia di sposi, 390x844.**
  - Il link ai matrimoni con il voto è nella prima schermata e "Matrimoni" è nel menu.
  - Dalla sezione si vedono 4,9 su 5, il prezzo da 1.000 euro, "Chiama per la data" e "Vai a Weddgraphy" senza scorrere.

### Controlli generali

- Screenshot guardati a pezzi a 1440 e 390 (interi e prime schermate) accanto ai riferimenti, e a 320, 768, 1024, 1280 e 1920. Guardati anche il menu aperto a 390 e l'àncora del preventivo.
- **Scorrimento orizzontale**: nessuno a 320, 390, 768, 1024, 1280, 1440 e 1920. Trovati e corretti durante il lavoro:
  - la testata a 390 (il nome accanto al logo e la parola "Chiama" sono tolti sotto 600 px, e il nome è passato nell'occhiello);
  - la griglia dei lavori e i bottoni lunghi a 320.
- **Sovrapposizioni**: nessuna.
- **Immagini ingrandite oltre la misura del file**: nessuna, a nessuna larghezza. Corretti i `sizes` per 1920.
- **Collegamenti**:
  - `tel:+393487485871`, 5 volte;
  - `mailto:` per stefano@stefanoaiti.com (con oggetto), info@aitistudio.it, info@weddgraphy.it e la PEC;
  - Google Maps su Via Galileo Galilei 40, 35035 Mestrino;
  - https://www.weddgraphy.it e la scheda di Matrimonio.com;
  - nessuna àncora rotta. Restano i link a `privacy/` e `cookie/`, pagine da fare.
- **U+2014**: nessuno, nella pagina, in questa NOTA, nel LEGGIMI, nei CREDITI e negli script nuovi.

### Caratteri e licenze

Switzer (Indian Type Foundry, da Fontshare), pesi 400 e 600, con la ITF Free Font License, che permette l'uso commerciale gratuito. I file woff2 sono serviti dalla pagina in `sito/fonts/`. Il 600 è stato scaricato il 3/11/2026 da Fontshare; la copia è in `assets/fonts-scaricati/`.
