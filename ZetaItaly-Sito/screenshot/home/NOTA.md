# Zeta S.r.l., home: nota

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shot.mjs` all'ora simulata lunedì 2 novembre 2026 alle 10, poi `pro_controlli.mjs`). Per vedere lo stato a un'altra ora: `sito/index.html?ora=2026-11-02T19:00`.

La versione di prima ("Cristal", la busta ricostruita con "Trasparente come il vetro") è copiata com'era in `_prova/versione-1-originale/` (sito e screenshot, con la sua nota).

Screenshot in questa cartella (stessi nomi di prima): `home-1440.jpg` (6236 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10570 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (dal preventivo al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti (prime schermate di tutti e 14 nel foglio `riferimenti.jpg`; pagine intere di barth, Cly-Del e Holzrausch), e a 320, 768 e 1024. Provati a parte: il menu aperto a 390 alle 13.00 ("Chiusi ora", pallino ambra), il riquadro "La richiesta è pronta" dopo l'invio del modulo, lo stato a 10.00, 13.00, 18.00, venerdì 19.00, 8 dicembre e 24 dicembre.

## Livello professionale, ritocco finale (3/11/2026)

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso). Il ritocco parte dal giudizio del controllore (voto 6: "un buon modello B2B riempito con cura", non "firmata da uno studio") e dalle prove dei due clienti tipo (tipografia-legatoria a 1440, cliente abituale a 390).

### Che cosa è cambiato in questo ritocco

- **Apertura con un gesto di scala.** Non più titolo a sinistra e foto tagliata a destra. Ora il mestiere è un titolo di 70 px in due righe ("Articoli su misura / in PVC e polipropilene"), con il motto sotto; accanto, alla stessa altezza, la foto del tavolo **intera, nel suo formato panoramico 2,4:1** (1200x500, in pagina 519x216: a 2x è nitida, prima era un ritaglio di 579x500 ingrandito). Sotto, su due colonne: chi sono a sinistra; "Chiedete un preventivo", "Chiamate 049 774299" e che cosa mandare a destra, sotto la foto. L'apertura è più bassa di 107 px: a 1440x900 si vedono le prime quattro foto dei prodotti intere (655-856 px) **e i loro nomi** (872-898 px).
- **Tipografia con due ruoli netti.** General Sans 700 solo per titoli e cifre, con l'interlinea stretta e la spaziatura negativa (-0,035 em sull'H1); Switzer 400 per il testo e Switzer 700 per etichette, bottoni e modulo. Pesi 400 e 700, come chiede A4 (prima 400 e 600 in due grotteschi quasi uguali).
- **Foto nei loro formati.** Prodotti in 3:2 (tutti uguali), tavolo 2,4:1, linea dell'azienda 3:2 larga al massimo 560 px (file 1024: circa 1,8x, prima 0,9 tagliata in verticale con mezzo muro). Due formati di prodotto e reparto, nessuna foto ingrandita oltre il file a 1x. La scheda "Articoli medicali" ora ha il salva taschino per camice della stessa serie 2019 (stesso fondo grigio scuro, al posto della scatola con l'espanso che aveva grana e grigi diversi); la copertina è tagliata più in basso e non ha più i pezzi arancio in alto.
- **Prove, senza inventare.** Sopra le date, quattro cifre grandi prese dalle fonti: 1969, 3 generazioni, 5 materiali, 8 siti nazionali. Le date sono diventate un elenco a due colonne (1986, 1994, 2010, 2015, 2019, 2022). Sotto, la fascia "Materiali certificati" con didascalia: OK Compost (la bioplastica dei loro articoli, dal 2019) e ISCC PLUS (il PVC di origine vegetale, con il numero del certificato del fornitore). È scritto che sono certificati dei materiali, non dell'azienda.
- **Su misura meno "interfaccia".** Le quattro voci sono numerate (01-04); i settori non sono più pillole con il bordo ma un elenco tipografico con filetti, 4 colonne a 1440, 2 a 768, 1 a 390. Nelle finiture ci sono le goffrature con le loro parole ("goffratura liscia, buccia d'arancia o similpelle", dalla scheda dei raccoglitori).
- **Ritmo.** Tra apertura e prodotti 40 + 64 px (prima 48 + 40); il titolo "I nostri articoli" ha 64 px sopra.
- **Uso (dalle prove dei clienti tipo).**
  - Modulo: il campo del disegno ha un bottone "Scegli il file" in italiano e il nome del file accanto, con la riga "Il file non parte da qui: lo allegate voi all'email che si apre". Dopo "Prepara l'email della richiesta" compare nella pagina il riquadro "La richiesta è pronta" con il testo già scritto (destinatario, oggetto, campi) e i bottoni "Copia il testo" e "Copia l'indirizzo": chi non ha un programma di posta non resta fermo. L'etichetta dei formati ora corrisponde ai file accettati (PDF, DXF, DWG, AI, EPS, JPG o PNG).
  - 390: sotto i bottoni c'è l'indirizzo info@zetaitaly.com con "Copia l'indirizzo"; "Scriveteci" apre un'email con oggetto "Ordine o file di stampa" e le righe Azienda, Riferimento ordine o articolo, Quantità.
  - Stato aperto/chiuso: pallino colorato (verde "Aperti ora", ambra #8A5A00 "Chiusi ora"), ricalcolo ogni minuto e quando si torna sulla pagina, elenco `CHIUSURE` pronto per le ferie aziendali (vuoto finché Zeta non dà le date, LEGGIMI).
  - Sede: "Il campione da rifare speditelo a questo indirizzo: ve lo rendiamo." sotto l'indirizzo.
  - Menu aperto: le voci hanno tutte lo stesso spazio (prima "Prodotti" era attaccata e le altre avevano 80 px vuoti, per un `gap` ereditato).
  - Testi: "I pannelli fotovoltaici sui nostri tetti" (la fonte dice "stabilimenti", il numero va confermato); nella scheda "Custodie e accessori" la riga comincia con "Cartelle per campionari", che è ciò che mostra la foto.

### Esito regola per regola (`_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. Testata fissa a tutte le larghezze (84 px a 1440, 72 a 390); il bottone "049 774299" (48 px a 390, 52 a 1440) si vede e si tocca a metà pagina; "Preventivo" nel menu. 4 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA. H1 "Articoli su misura in PVC e polipropilene"; occhiello "Zeta S.r.l. · Padova, dal 1969"; prova: dal 1969, tre generazioni della famiglia Sacerdoti; azione: a 1440 "Chiedete un preventivo" a 368-420 px, a 390 "Chiamate 049 774299" a tutta larghezza (350 su 350 px utili) a 461-513 px.
3. **Immagine vera nell'apertura**: PASSA. Una persona al loro tavolo di lavoro, nel reparto (servizio 2023), intera nel suo formato. In pagina 519x216 da un file di 1200x500 (2,3x). Non è un oggetto scontornato.
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da Unsplash o Pexels; tutte da `assets/originali` di Zeta.
5. **Foto in serie**: PASSA. Prodotti 2019: stesso fondo grigio scuro, stessa luce, stesso taglio 3:2. Reparto 2023: due foto dello stesso servizio. Formati in pagina a 1440: 2,4:1 e 3:2, cioè 2. Didascalie 0.
6. **Palette dal marchio**: PASSA. Verde del logo #0A6B42 (bottoni, occhielli, blocco dei numeri), il suo scuro #0C241A (prodotti e piede), verde chiaro #8FD3B0 solo su fondo scuro, ambra #8A5A00 solo per "Chiusi ora"; poi bianco, grigio chiaro #EEF1EF, inchiostro e grigio del testo. Niente beige.
7. **Scala corta e leggibile**: PASSA. 1440: 96, 70, 44, 22, 18, 16, 14 px (7). 390: 48, 34, 28, 22, 19, 17, 16, 14 (8). Testo 18 a 1440 e 17 a 390. I 14 px sono solo occhielli in maiuscolo spaziato e note legali. H1 70 px (fascia M 60-70), 34 a 390.
8. **Due famiglie con ruoli fissi**: PASSA. General Sans 700 solo per titoli e cifre; Switzer 400 per il testo e 700 per etichette, bottoni e modulo. Pesi 400 e 700.
9. **Servizi in schede con la foto**: PASSA. Otto schede in 4 colonne (2 sotto i 900 px), tutte cliccabili verso la categoria vera, foto del prodotto con lo stesso taglio 3:2, nome di 22 px con la freccia e una riga.
10. **Almeno tre tipi di prove**: NON PASSA (2 tipi su 4, ne servono 3). Ci sono 4 numeri aziendali (1969, 3 generazioni, 5 materiali, 8 siti nazionali) e la fascia dei materiali certificati con didascalia (OK Compost; ISCC PLUS del fornitore). Recensioni: nessuna nelle fonti (Zeta vende solo ad aziende). Clienti con il nome: solo marchi nelle foto, non pubblicabili senza permesso. I numeri che una manifattura mostra di solito (addetti, metri quadrati, paesi, pezzi l'anno) non sono nelle fonti: niente inventato, va tutto chiesto (LEGGIMI).
11. **Lavori con un nome**: NON PASSA, per mancanza di fonti: nessun lavoro con cliente, anno e dati; da chiedere (LEGGIMI, punto 2).
12. **Ritmo a blocchi**: PASSA. Prodotti su verde scurissimo, numeri sul verde pieno del logo, preventivo su grigio chiaro, piede scuro. Spazi tra le sezioni 120 px a 1440 e 72 a 390; tra apertura e prodotti 40 + 64 = 104 px a entrambe le larghezze. Margini 80 e 20 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno verde e solo bordo, raggio 4 px, altezza 52 px (48 per telefono e Menu in testata a 390), testo 16 px. Ogni bottone di chiamata ha il numero. "Copia" e "Copia l'indirizzo" accanto alla mail sono link di testo.
14. **Modulo e "dove e quando" per il mestiere**: PASSA. Modulo M con nome, azienda, email, telefono, articolo, materiale, misure, quantità, disegno o foto (PDF, DXF, DWG, AI, EPS, JPG, PNG) e messaggio. Compone un'email con oggetto "Richiesta di preventivo: articolo, azienda" e tutti i campi, e mostra nella pagina lo stesso testo da copiare; il file si allega a mano. Va collegato a un servizio (LEGGIMI). Sede con indirizzo, orari in tabella, stato di adesso, "Apri nelle mappe" e telefono. Nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni dell'azienda (non ne hanno; quelle dei materiali sono nel blocco dei numeri). Quattro colonne: Zeta (logo in bianco, telefono, mail, indirizzo con le mappe, orari), Prodotti, Azienda e LinkedIn, Lingua; riga legale con ZETA S.r.l., P.IVA e C.F., Registro Imprese, capitale sociale, Privacy e Cookie. Testo di 16 px, note legali di 14.

### Prove d'uso della SCHEDA (par. 8) e dei due clienti tipo

- V1, 1440: il mestiere nel titolo; 4 famiglie con la foto intera e il nome sopra i 900 px (prima solo 163 px di foto, senza nome); custodie per vinile e portadocumenti auto a un clic (riga "Anche" e schede); che cosa mandare sotto i bottoni; modulo con il file, testo da copiare se la posta non si apre, mail con "Copia"; EN in testata. Riescono, e il compito 3 del primo cliente tipo non dipende più dal programma di posta.
- V2, 390: "Chiamate 049 774299" di 52 px con il fondo a 513 px (prima 521); tel in testata di 48 px; stato con orari a 447 px; "Scriveteci" e l'indirizzo da copiare nella prima schermata. Riescono, e meglio di prima.
- V3, 390: il menu aperto ha "Apri nelle mappe", gli orari con lo stato e il numero, tutto nella parte alta; nella sezione del preventivo il campione "ve lo rendiamo" è anche sotto l'indirizzo, con orari, telefono e mappe nello stesso riquadro. Riescono.
- Stato: lunedì 10.00 "Aperti ora, fino alle 12.30"; 13.00 "riapriamo oggi alle 14.00"; 18.00 "riapriamo domani alle 8.30"; venerdì 19.00 "riapriamo lunedì"; 8 dicembre chiuso; 24 dicembre aperto (ferie di Natale non note). Senza JavaScript restano gli orari scritti.

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440 e 1920. Sovrapposizioni: nessuna (a 320 "Portadocumenti" va a capo con il trattino morbido; il campo file nascosto, che allargava la pagina, è corretto).
- Collegamenti: `tel:+39049774299`; `mailto:info@zetaitaly.com` (anche con oggetto e corpo); mappe `https://www.google.com/maps/search/?api=1&query=Zeta+S.r.l.+Viale+della+Navigazione+Interna+55+35129+Padova`; categorie e pagine sul sito vero (`https://www.zetaitaly.com/...`, verificate il 3/11/2026 sulla sitemap); lingue sui loro domini.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script toccati. Nessun segnaposto in pagina.

### Caratteri e licenze

General Sans 700, Switzer 400 e Switzer 700, Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito, anche web), serviti dalla pagina in `sito/fonts/`. General Sans 700 e Switzer 700 scaricati il 3/11/2026 da Fontshare (`api.fontshare.com`, copie in `assets/fonts-scaricati/`); Switzer 400 è lo stesso file di prima. Tolti General Sans 600 e Switzer 600.

### Respinti o non applicati, con il motivo

- Recensioni, clienti con il nome, lavori con cliente e anno, numeri come addetti e metri quadrati (regole 10 e 11): non ci sono nelle fonti; non inventati, chiesti nel LEGGIMI.
- Logotipo Zeta enorme in apertura (variante b del controllore): il logo esiste solo come PNG, non c'è il vettoriale; si è scelta la variante con il titolo grande e la foto intera.
- Foto vera di una custodia per vinile nella scheda "Custodie e accessori": l'unica loro (`2025_01_custodia-dischi-vinile.jpg`) è su fondo bianco, con luce da ufficio e la copertina riconoscibile di un disco: rompe la serie e mostra un marchio altrui. Resta la vaschetta con la riga riordinata; la foto va fatta (LEGGIMI).
- Tempi di risposta e quantità minime in pagina: non sono nelle fonti (LEGGIMI, punto 6).
- Riga "file oltre 10 MB con WeTransfer": è una regola di lavoro di Zeta che non conosciamo; da chiedere.
- Togliere il campo del file dal modulo: la regola 14 lo chiede per la famiglia M; ora dice chiaramente che il file va allegato all'email.
- Formato STEP nel modulo: nelle loro pagine si parla di misure, disegni, foto e campioni, mai di modelli 3D.
- Newsletter: no (lavorano su commessa, nessuna notizia da mandare; LinkedIn basta).
