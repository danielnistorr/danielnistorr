# La Termica, proposta di nuova home

Proposta non richiesta di una nuova homepage per La Termica snc di Camporese Mario (Mestrino, PD). Nessun contatto con l'azienda, niente pubblicato, nessun modulo inviato.

## Dove sono le cose

- `sito/index.html`: la home finale, statica (livello professionale, 3/11/2026). Accanto ci sono `sito/img/` (solo le foto loro usate, WebP alla misura giusta, logo PNG a 3x e logo negativo per il piede) e `sito/fonts/` (Host Grotesk woff2 e `OFL.txt`).
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (che cosa è cambiato, le 15 regole una per una, i compiti della scheda d'uso, caratteri, foto, controlli).
- `_prova/script/build_finale.sh`: rifà immagini (`pro_img.py`), controlli delle 15 regole (`pro_controlli.mjs`, esito in `_prova/pro_controlli.json`) e screenshot (`pro_shoot.mjs`; `pro_mosaico.py` affianca i pezzi delle pagine strette per guardarle).
- `_prova/versione-1-originale/`: la home di prima ("Rame sui coppi"), con pagina, immagini, caratteri, schermate e nota, com'era prima di questo giro.
- `_prova/uso/SCHEDA.md`: chi apre il sito e che cosa viene a fare. `01-analisi.md`: fatti con le fonti. `assets/CREDITI.md`: origine e licenza di ogni immagine.

## Da chiedere all'azienda, in ordine di importanza

1. **Orari del magazzino e del banco.** Sono la prima domanda del privato e dell'installatore e oggi non sono in pagina: le schede pubbliche non concordano ("lun-ven 8-12:15" su trova-aperto, "8-12, 14-18" su infobel). Appena arrivano vanno in tre punti: la tavola dell'apertura (al posto di "Magazzino e banco", con lo stato "aperto ora / chiuso ora"), la chiusura accanto all'indirizzo e la colonna Contatti del piede. Chiedere anche sabato, chiusure estive e festivi, e se il banco ha orari diversi dalla posa.
2. **Zone servite** per posa, pulizia e spazzacamino: l'elenco dei comuni (per esempio Mestrino, Rubano, Selvazzano, Padova ovest, est vicentino, se è così). Va in un elenco sotto i servizi e nel piede. Oggi non c'è perché non è nelle fonti.
3. **Recensioni.** Non ce ne sono di pubbliche leggibili (Pagine Gialle "Nessuna recensione"). Se hanno una scheda Google con recensioni, o lettere di amministratori e imprese, servono testo, nome e comune, con il permesso. Non sono state inventate.
4. **Lavori con un nome.** Per tre o quattro lavori: luogo (comune o via, se si può dire), anno, e due o tre dati (per esempio altezza della canna, numero di appartamenti, diametro, numero di canne nel traliccio). Oggi le schede dei lavori dicono solo il tipo.
5. **Clienti con il nome**: condomini, imprese o aziende che si possono citare, con il permesso.
6. **Abilitazioni precise**: oltre a "autorizzati dalla camera di commercio", quali hanno (con il numero, se si può citare) e quali certificati rilasciano per l'installazione. Servono per una fascia di certificazioni con la didascalia.
7. **Marchi**: le stufe e i termocamini di oggi (il sito del 2014 dice CLAM, Eva Calor e Calux) e il produttore delle canne (i cataloghi PDF portano "MULTICLIMA"). Se sono ancora quelli, vanno in una fascia "Fornitori" con la didascalia. Oggi non sono in pagina perché non confermati.
8. **WhatsApp**: lo usano per ricevere liste e foto? Se sì, un bottone accanto a "Chiedete disponibilità".
9. **Forma societaria**: in pagina c'è "La Termica snc di Camporese Mario", come nel registro LEI e nell'informativa del 10/2023; l'"srl" di atoka e legnadoc sembra un errore degli aggregatori. Da confermare, con REA e PEC per la riga legale.
10. **1978 e la famiglia**: va bene "dal 1978" in apertura (è l'anno della ditta, nata nelle coibentazioni)? I nomi e i ruoli dei due figli si possono scrivere?
11. **Facebook**: la pagina `facebook.com/latermica.caminiinox` è loro e attiva? Se sì, va nel piede con il sottotitolo di che cosa si trova lì.
12. **Pronto Lamiera e abbattitori di fuliggine**: sono servizi ancora attivi? Sono in pagina perché sono sul loro sito di oggi.
13. **Email e fax**: info@latermicacamini.com resta quella giusta anche con il dominio latermica.it? Il fax 049 9007617 è ancora attivo (oggi non è in pagina)?
14. Dipendenti (4) e ricavi (749.000 €) vengono da atoka.io: non sono in pagina e non vanno messi senza conferma.

## Il modulo da collegare

Il modulo "Richiesta di preventivo o di sopralluogo" in chiusura oggi **compone un'email** (`mailto:` a info@latermicacamini.com con l'oggetto "Richiesta dal sito: <tipo>, <ditta o nome>" e tutti i campi nel testo) e non invia niente da solo: controlla nome e telefono, poi apre il programma di posta di chi scrive. Un mailto non porta allegati: per questo la nota dice di allegare all'email pianta, disegno e foto.

Prima di andare in linea va collegato a un servizio di invio (il modulo del CMS, per esempio Contact Form 7 che usano già, oppure Formspree o un servizio con server in UE), con:
- un vero campo file per pianta, disegno e foto (PDF, JPG, DWG), con un limite di misura;
- la casella del consenso e il link all'informativa, che va aggiornata con il trattamento dei dati del modulo;
- la risposta automatica a chi scrive e, se l'azienda la vuole dare, la promessa dei tempi di risposta (oggi non c'è perché non è nelle fonti).

Le schede dei servizi portano al modulo con il tipo già scelto: i valori sono quelli della tendina (`data-tipo`).

## Collegamenti che dipendono dal sito di oggi

- I 15 cataloghi tecnici puntano ai PDF già online (`https://www.latermica.it/wp-content/uploads/2014/05/01-...pdf` ... `15-...pdf`). Nel sito nuovo vanno tenuti agli stessi indirizzi o copiati, altrimenti l'elenco delle serie si rompe.
- Le schede dei lavori e la riga "Altre gallerie" portano alle gallerie di oggi (`/galleria-canne-fumarie-inox/lavori-ultimati/`, `camini-autoportanti/`, `impianto-atex/`, `tubo-doppia-parete-radiante/`, `non-camini/`, `armadi/`). Nel sito nuovo diventano le pagine dei lavori per tipo.
- L'informativa privacy punta a `https://www.latermica.it/informativa-sulla-privacy/`.

## Foto da fare dal vero

Le foto in pagina sono tutte loro, ma sono del 2012-2014, da compatta e telefono. Mezza giornata con un fotografo basta, con la stessa luce per tutta la serie (giornata di cielo coperto chiaro o mattina presto), formati 4:5 e 4:3, tutto a piena risoluzione:

1. **La squadra con il furgone**: Mario Camporese e i figli, in divisa o con la maglia con il logo, davanti al furgone con la livrea "camini inox" e al capannone di Via Bologna. È la foto d'apertura che manca (regola 3: persone e mezzo con il marchio). Una orizzontale per il computer, una verticale per il telefono.
2. **Il banco e gli scaffali** ordinati, con luce calda, e una persona al banco con un cliente: per il magazzino e per chi viene a comprare.
3. **Una foto per ogni servizio**, stesso taglio 4:3 o quadrato, per fare delle sei schede dei servizi schede con la foto (regola 9): canna fumaria nuova per una stufa a pellet in una casa; spazzacamino al lavoro sul tetto con la spazzola; la telecamera della video ispezione con lo schermo (oggi c'è un fotogramma del 2014); intubamento di una canna vecchia; una stufa installata da loro; un abbattitore di fuliggine montato.
4. **Tre o quattro lavori recenti** visti da fuori, con il teleobiettivo e le verticali dritte: un condominio, un camino autoportante, un tetto di centro storico, un impianto industriale. Con luogo e anno da scrivere sotto (vedi sopra).
5. **Un armadio inox su misura** in laboratorio, su fondo chiaro, con luce diffusa da un lato.
6. **La facciata con l'insegna** di oggi (quella in pagina è del 2014, larga solo 1200 px), per "Dove siamo".

## Caratteri e licenze

- **Host Grotesk** (Element Type) da Google Fonts, licenza SIL Open Font License 1.1: uso commerciale libero, anche servito dal proprio sito. File e licenza in `sito/fonts/`. Brygada 1918 della versione 1 non è più usato.
- **Foto**: tutte di La Termica, dal loro sito. Le foto di repertorio in `assets/esterne/` (Unsplash e Pexels, licenze in `assets/CREDITI.md`) non sono usate.

## Logo

Il logo in testata è un PNG trasparente a 480 e 640 px (3x per 160 px), ricavato dal JPEG a 3000x938 del loro sito; nel piede scuro c'è la stessa immagine con la scritta "camini inox" portata al bianco. Il sito non ha un SVG: al grafico o all'azienda va chiesto il logo vettoriale (AI, EPS, PDF o SVG), anche in versione negativa.
