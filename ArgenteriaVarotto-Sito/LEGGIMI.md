# Argenteria Varotto Alfredo: proposta di nuova home

Proposta non richiesta, solo la home. Niente è stato inviato all'azienda né pubblicato.

- Pagina: `sito/index.html`, con `sito/img/` e `sito/fonts/`. Si apre anche da file.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`: in testa la sezione "Metodo ibrido (novembre 2026)" con le misure e i problemi aperti; sotto, la nota della versione professionale).
- Rigenerare (metodo ibrido): immagini `python3 -I _prova/alto/script/img.py` (dalle originali in `assets/originali/shop/`), provini `_prova/alto/script/provini.py`, misure della sezione D `node _prova/alto/misura-d.mjs` (esito in `_prova/alto/misure/`), screenshot `node _prova/alto/script/vista.mjs`, compiti della scheda `node _prova/alto/script/compiti.mjs`. La pagina è scritta a mano in `sito/index.html`. Gli script della versione professionale (`_prova/script/`, `_prova/crawl/`) non ci sono più sul disco dopo il riavvio; la pagina professionale è copiata in `_prova/versione-pro/`.
- Ultimo passaggio (3 novembre, livello professionale): via le foto di repertorio, il banco di posa e il selettore dei metalli; la home è ordinata per i tre visitatori della scheda d'uso (`_prova/uso/SCHEDA.md`): hotel e ristoranti, riparazione, shop. La versione precedente è in `_prova/versione-1-originale/`.
- Ritocco finale (3 novembre, dopo il controllo del livello professionale e due clienti tipo): apertura fatta di tipografia con i tre punzoni in grande al posto del riquadro del vassoio (che è passato nella sezione shop), fascia delle cifre su blu notte, schede hotel su grigio con le posate in alpacca e la scheda della riargentatura, prezzi pieni barrati come sullo shop, foto rifatte in una serie 3:2, via la foto della sede, segno del logo in SVG, campo per gli allegati nel modulo, "Dove siamo" nella riparazione, voce "Orari" nel piede. Dettagli regola per regola in `screenshot/home/NOTA.md`.
- Correzione dell'apertura (3 novembre): torna una foto vera del loro argento, un dettaglio a filo del vassoio Regina Anna in Sheffield (incisione e bordo a godroni, senza fondo e senza prezzo, al massimo 355 x 138 px perché il file è di 1280 px), e i tre punzoni passano a misura di marchio in una fila sotto i bottoni. Dettagli in `screenshot/home/NOTA.md`, in fondo alla sezione "Livello professionale".
- **Metodo ibrido (3 novembre, dopo "non è ancora super professionale")**: prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md`, modello T: i tre punzoni (stella e 364 PD, 925, 800) incisi in grande in un campo d'argento, con la loro frase "Riconoscibili ad occhio nudo, impressi sull'oggetto" come titolo, un solo bottone (Chiama, in testata). Sotto, i contenuti della versione professionale su una griglia sola: hotel e ristoranti, il culmine dello shop con il vassoio Regina Anna alla misura vera, chi siamo con i punzoni spiegati, riparazione, contatti per bisogno con il modulo. Via la fascia delle cifre, le tre porte, i prezzi barrati, gli occhielli. Caratteri: Bodoni Moda e Rethink Sans (Boska esce). Direzione in `_prova/alto/DIREZIONE.md`, versione professionale copiata in `_prova/versione-pro/`.
- Analisi con le fonti: `01-analisi.md`.

## Il modulo di contatto va collegato a un servizio

Il modulo "Scrivete la richiesta" oggi **non invia nulla**: controlla nome ed email e compone un'email (`mailto:info@varottoalfredo.com` con oggetto e tutti i campi) nel programma di posta di chi lo compila. Per il sito vero va collegato a un servizio di invio (Formspree, Brevo o il modulo del CMS che useranno), con:

- invio a info@varottoalfredo.com (e, se la tipologia è estera o la lingua è inglese, a export@);
- **allegati** (foto del pezzo da riparare, elenchi, disegni): il campo "Foto del pezzo, disegni o elenchi" c'è già (`input type=file`, più file, immagini e PDF), ma con il `mailto:` i file non partono: oggi l'email composta riporta solo i nomi dei file e l'avviso chiede di allegarli a mano. Con il servizio di invio il campo spedisce davvero i file (limite di misura da decidere, per esempio 10 MB);
- casella del consenso privacy collegata alla nuova informativa (quella di oggi cita ancora il D.Lgs. 196/2003);
- una risposta automatica con i tempi in cui richiamano (da chiedere, punto 9).

Anche i bottoni "Mandate le foto del pezzo" e "Preventivo per quantità" aprono un'email già compilata: vanno bene così anche nel sito vero.

## Da chiedere o confermare con l'azienda (non è a vista in pagina, o lo è nella forma più prudente)

1. **Orari** di apertura e se ricevono privati in sede. Un elenco online (trova-aperto.it) dà lunedì-venerdì 8.30-13.15: non sono in pagina e non vanno pubblicati finché non li confermano. Il posto c'è: nel piede la voce "Orari" (oggi "Prima di passare, chiamate il 049 870 07 09"), nei Contatti e in "Dove siamo" della riparazione la stessa frase. Con gli orari veri lì va una tabella giorni e orari.
2. **WhatsApp +39 392 502 4576**: è quello dello shop. Vale anche per le foto dei pezzi da riparare? Se sì, accanto a "Mandate le foto per email" si aggiunge "Mandate le foto su WhatsApp".
3. **Recensioni**: la regola 10 chiede recensioni con nome e comune. Nelle fonti c'è solo il negozio eBay "varottoshop" (circa 630 vendite e 100 % di giudizi positivi, due frasi di acquirenti: "Arrivato il prodotto è in ottime condizioni spedizione molto veloce, venditore affidabile" e "Article magnifique fabriqué en Italie"), letto tramite ricerca: la pagina eBay non si apre da qui. Possiamo citare i giudizi eBay? Se sì, in Chi siamo (la fascia delle cifre non c'è più) va una riga "Su eBay: circa 630 vendite, 100 % di giudizi positivi" con le due frasi, la fonte (ebay, negozio varottoshop) e la data di lettura, con i numeri riletti quel giorno. Hanno recensioni Google o lettere di clienti (hotel, ristoranti) da pubblicare con il nome?
4. **Clienti e lavori con il nome**: almeno tre hotel, ristoranti, pasticcerie o catering forniti, ognuno con città, anno e che cosa (per esempio "buffet della colazione, 40 alzate e 12 vassoi"), meglio con una foto della sala allestita e il permesso di nominarli; e qualche riparazione fatta (che pezzo, che lavoro, prima e dopo). Sono le prove che mancano (regole 10 e 11): con questi dati si aggiunge una sezione "Lavori" tra hotel e riparazione.
5. **Numeri aziendali**: persone in laboratorio e in magazzino, metri quadri dello stabilimento, paesi in cui esportano, articoli in catalogo, pezzi riparati o riargentati in un anno. Con il metodo ibrido la fascia "Varotto Alfredo in cifre" è tolta (regola D9): i numeri veri, quando arrivano, vanno al massimo tre dentro una frase, ognuno con l'unità e il periodo.
6. **Prezzi dello shop**: in pagina ci sono dieci prezzi letti sullo shop il 3/11/2026 (IVA inclusa), solo sotto la prima schermata; con il metodo ibrido si mostra solo il prezzo scontato, senza il prezzo pieno barrato, e la nota dice "scontati come sullo shop": quel giorno tutti gli articoli usati erano scontati di circa il 18 %. È uno sconto fisso o una promozione? I prezzi cambiano: vanno riletti prima di pubblicare, o la pagina li va a prendere dallo shop. Per i professionisti la nota dice "Per forniture e quantità vi facciamo un preventivo": c'è un listino per rivenditori o per hotel?
7. "Dal 1974": in pagina c'è "dal 1974" come nella testata di oggi ("Since 1974"); il testo Azienda dice "agli inizi degli anni '70". Quale preferiscono?
8. **Da confermare prima di pubblicare, perché ora è il gesto d'apertura**: chi è Luca Varotto rispetto ad Alfredo, a chi è intestato il punzone 364 PD e se la produzione in Corso Stati Uniti è dell'impresa (l'attività registrata è "commercio all'ingrosso di metalli non ferrosi"). In pagina c'è la loro frase "Tutta la produzione dell'argenteria è eseguita all'interno del nostro stabilimento di Padova".
9. Riparazioni: tempi tipici, se fanno il ritiro e come si spedisce un pezzo. Oggi la pagina dice solo che "l'incaricato" dà fattibilità, ritiro e tempi, come la loro pagina Assistenza.
10. Royal Queen, Royal England, Sweet Home, VarottoHotellerie e TEN sono marchi loro? Le righe dei marchi in pagina descrivono ciò che si vede sullo shop.
11. PEC e REA per la riga legale.
12. Area clienti: l'indirizzo della pagina di oggi (area riservata per le proposte d'ordine) o una pagina nuova. In pagina il link porta a `area-clienti/`.
13. Social: Facebook (varottostore) e Pinterest (lucavarotto) sono dello shop e nel piede sono scritti così. Vanno tenuti? Instagram non è verificato e non c'è.
14. Il vecchio indirizzo "Varotto Alfredo, via del Santo 75, 049 8761205" (impresaitalia.info): un negozio in centro che esiste ancora?
15. **Fiere**: la pagina di oggi è vuota. Se partecipano ancora (Homi, Ambiente, Vicenzaoro), una data con città e stand va in home.
16. **Posate per hotel**: in pagina la scheda "Posate per hotel e ristoranti" mostra la forchetta da tavola in alpacca stile Inglese (Sweet Home, € 38,84) e porta alla linea Inglese in alpacca dello shop. C'è una linea pensata per gli alberghi (acciaio VarottoHotellerie, alpacca) da mettere al suo posto, o una categoria dello shop dedicata?
17. **Riargentatura del materiale di sala**: nella home ibrida è un blocco di solo testo accanto agli articoli per la sala, senza foto. Servono una foto vera (un vassoio consumato e lo stesso riargentato) e, se si può, un ordine di grandezza dei tempi per un hotel.

## Pagine del sito nuovo (destinazioni dei link della home)

| Link | Pagina |
|---|---|
| Area clienti (proposte d'ordine dei rivenditori) | `area-clienti/` |
| English | `en/` |
| Privacy, Cookie | `privacy/`, `cookie/` |
| Famiglie del catalogo, prodotti, categorie per chi regala, "Apri lo shop" | varottoshop.com (esterno): `buffet.html`, `bar-pasticceria.html`, `buffet/vassoi-rettangolari.html`, `buffet/secchielli-champagne-ghiaccio.html`, `posateria/posate-inglese-alpacca.html`, `posateria.html`, `tavola-e-cucina/sottopiatti-in-vetro.html`, `buffet/vassoi-ovali.html`, `buffet/alzate-e-piatti-dolce-con-campane-in-vetro.html`, `buffet/chafing-dish.html`, `complementi-arredo/bomboniere.html`, `oggettistica/prima-infanzia.html`, `oggettistica.html`, `complementi-arredo/centrotavola.html`, `-offerte.html` e cinque schede prodotto |

Le voci del menu Hotel e ristoranti, Shop online, Riparazione, Chi siamo e Contatti portano alle sezioni della home (Shop online porta al culmine con i pezzi, che ha "Apri lo shop"). Quando ci saranno le pagine interne (Riparazione, Hotel e ristoranti, Storia e punzoni) le stesse voci possono portare lì.

## Foto da fare dal vero

Oggi in pagina ci sono solo dieci foto di catalogo dello shop (sul bianco, al massimo 1280 px): nove nella stessa tela 3:2 e il vassoio Regina Anna intero alla sua misura (1280 x 557) nel culmine. Non c'è nessuna foto che dica chi lavora e dove: per questo l'apertura è fatta dei punzoni incisi (tipografia, nessuna foto), e la foto della sede (500 x 301, vecchia, con il cielo bruciato) resta fuori. Una giornata con un fotografo basta, con una sola luce per tutta la serie:

1. **Laboratorio**: mani che lucidano o riargentano un vassoio al banco, luce di finestra laterale, fondo del laboratorio leggibile ma non disordinato, 3:2 orizzontale, almeno 2400 px. Con il metodo ibrido va in testa alla sezione Riparazione, o diventa il culmine della pagina; l'apertura resta dei punzoni.
2. **Riparazione**: la stessa serie, tre scatti: un pezzo rovinato com'è arrivato, il lavoro (pulitrice, bagno galvanico se c'è, martello), il pezzo finito. 3:2, stessa luce. Rendono vera la sezione su blu e la scheda della riargentatura, che oggi sono solo testo.
3. **La sede**: facciata di Corso Stati Uniti 23/A con l'insegna, di giorno con cielo coperto, più l'ingresso per chi arriva in auto. 3:2, almeno 2000 px. Torna in "Dove siamo" e nei Contatti, accanto alla mappa.
4. **Hotel e ristoranti**: un buffet o un tavolo di pasticceria allestito con i loro pezzi (alzate, vassoi, campane), meglio in un hotel cliente con il permesso di nominarlo: è anche il "lavoro con un nome" che manca.
5. **Punzoni**: macro dei tre punzoni impressi su un pezzo in 925, luce radente da un lato, obiettivo macro 1:1, almeno 2400 px. È la foto che più serve: con una macro così l'apertura passa dal modello T al modello M (la macro del dettaglio) a tutta larghezza, con la didascalia del pezzo.
6. **Catalogo**: le foto dello shop reggono come miniature; per le schede servono a 1600 px, tutte con lo stesso fondo, la stessa ombra e la stessa inquadratura (oggi alcune hanno l'ombra e altre no; la forchetta in alpacca è solo 600 x 400).
7. **Il vassoio inciso** Regina Anna ad almeno 2500 px: quello dello shop è 1280 px e il ritaglio aveva un alone grigio sopra il bordo (tolto da `pro_img.py`). Serve al culmine: con il file di oggi il vassoio regge solo fino a 1280 px a 1x; meglio ancora una macro dell'incisione a luce radente, 3:2, almeno 2400 px.

## Licenze

- Caratteri: Bodoni Moda (Indestructible Type, SIL Open Font License 1.1, file variabile con l'ottica da `@fontsource-variable/bodoni-moda` 5.1.0, `sito/fonts/OFL-BodoniModa.txt`); Rethink Sans (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL-RethinkSans.txt`). Serviti dalla pagina. Boska non è più usata (tolta da `sito/fonts/`).
- Foto: solo materiale dell'azienda (dieci foto dello shop varottoshop.com), diritti da confermare: alcune foto dello shop potrebbero essere dei fornitori. Elenco in `assets/CREDITI.md`. Le foto Unsplash della proposta precedente non sono più usate.

## Loghi

- In testata e nel piede c'è il **segno a onde** del loro logo ridisegnato in SVG dal PNG del sito (`assets/originali/logo-varotto-alfredo-130x153.png`, oggi non più sul disco dopo il riavvio, dove il segno è alto circa 32 px), accanto al nome "Varotto Alfredo" in Bodoni Moda. Il PNG intero non è più in pagina: a 46 px le lettere non si leggevano. Serve il **vettoriale** del logo (SVG, PDF o AI) per rifare il segno identico e per il favicon, che oggi manca.
- I tre punzoni sono ridisegnati in SVG dalle GIF del sito (`logo-punzone-364PD.gif`, `logo-punzoni-925-800.gif`): forma fedele, numeri in Bodoni Moda. Con il metodo ibrido sono il gesto della prima schermata, alti circa 200 px e incisi nel campo argento con un filtro SVG; il marchio VAROTTO ALFREDO è scritto in Chi siamo. Con i punzoni veri in alta definizione (o i file dell'incisore) vanno rifatti identici, e prima va confermato a chi è intestato il 364 PD (punto 8).
