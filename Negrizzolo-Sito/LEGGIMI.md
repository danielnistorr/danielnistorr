# Officine Negrizzolo: proposta di nuova home

Proposta non richiesta di una nuova homepage per Negrizzolo S.a.S. di Negrizzolo ing. Paolo & C. (Grisignano di Zocco, VI). Solo la home. Versione "livello professionale" del 03/11/2026.

## Dove sono le cose

- `sito/index.html`: la home (statica, si apre con file:///). `sito/img/`: solo foto loro, WebP in due larghezze, e il logo SVG (chiaro e scuro). `sito/fonts/`: Archivo variabile in woff2 e la licenza `OFL.txt`.
- `screenshot/home/`: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` e `NOTA.md` (esito delle 15 regole nella sezione "Livello professionale").
- `_prova/script/build_finale.sh`: copia `pro_index.html` in `sito/index.html`, rifà gli screenshot (all'ora simulata martedì alle 10) e lancia `pro_controlli.mjs` (regole della sezione C, prove d'uso della scheda, orari, scorrimento orizzontale; esito in `_prova/pro_controlli.json`). Con `--immagini` rifà anche le foto (`pro_img.py`). `_prova/script/ritocco_prova.mjs` prova i link "ricambio" che scelgono il tipo nel modulo e il nome del file nel corpo dell'email.
- `_prova/versione-1-originale/`: la home di prima (sito e screenshot), com'era prima di questo passaggio.
- `_prova/uso/SCHEDA.md`: chi apre il sito e per fare che cosa; `01-analisi.md`: fatti con le fonti.

## Il modulo "Richiesta" va collegato a un servizio

Oggi il modulo in fondo alla home non invia nulla: compone un'email (mailto) con oggetto e campi già scritti e la apre nel programma di posta di chi compila, che la manda lui. Il modulo ha già il campo dei file (`input type=file`, più file, etichetta che cambia col tipo: "Disegno" per il laser, "Foto del pezzo" per il ricambio): un mailto non può portare i file, quindi l'email composta elenca i nomi dei file scelti ("File da allegare: ...") e sotto il campo è scritto "Con l'email che si apre il file non parte da solo: allegatelo voi.". Le richieste di taglio laser vanno a laser@negrizzolo.it, tutte le altre a info@negrizzolo.it. Nel sito vero va collegato a un servizio di invio (per esempio il modulo del gestore del sito o un servizio come Formspree o Netlify Forms) che **accetti il campo `file`** (allegati multipli, con un limite di peso), mandi una conferma a chi scrive e tenga la stessa divisione per indirizzo; a quel punto la frase sotto il campo va tolta. I link "Magazzino ricambi: chiedete un pezzo" e "Chiedete un ricambio" scelgono "Ricambio" nel modulo con un piccolo script (attributo `data-tipo`).

## Pagine che il sito nuovo dovrà avere

I link della home e del piede puntano a queste pagine (oggi non esistono nella proposta): `rimorchi-ribaltabili`, `rimorchi-fissi`, `carribotte`, `vasche-inox-uva`, `applicazioni-speciali`, `usato`, `riparazioni`, `taglio-laser`, `chi-siamo`, `privacy`, `cookie` (tutte `.html`). Le tabelle complete dei modelli (19 ribaltabili, 18 fissi, 13 carribotte) vanno nelle pagine dei prodotti.

## Cosa chiedere all'azienda

1. **Formati dei disegni per il laser**: quali accettano (DXF, DWG, PDF, STEP?). In pagina non c'è nessun formato, c'è solo "allegate il disegno", e il campo dei file del modulo accetta qualsiasi file: appena confermati vanno scritti nella sezione laser e sotto il campo, e messi nell'attributo `accept` del campo.
2. **Spessori e piano di lavoro del laser** per ogni materiale, e la macchina: è l'informazione che manca di più all'ufficio tecnico.
3. **Fax**: lo 0444 614515 è indicato come "Tel/Fax" sul sito di oggi; in pagina c'è "Telefono e fax" nei contatti e "Tel. e fax" nel piede. Confermare che il fax sia ancora attivo, altrimenti togliere la parola.
4. **Email del laser**: laser@negrizzolo.it (piede del sito di oggi, usata qui, una sola in tutta la pagina) o tecnico@negrizzolo.it (pagina Contatti di oggi). Se pubblicare il cellulare 347 2386150 del biglietto (non usato).
5. **L'usato**: se il rimorchio agricolo 60 q.li a 7.800 € è ancora in vendita (è nella home, nella seconda schermata e nell'indice della prima a 1440); chi aggiorna l'usato e quanto spesso.
6. **Recensioni**: nessuna trovata (Google Maps non leggibile, elenchi senza recensioni). Chiedere se si possono raccogliere su Google, con nome e comune del cliente: oggi la regola delle prove (almeno tre tipi) non passa, ce ne sono due (numeri e la fascia "Certificazioni e stampa").
7. **Clienti con il nome e lavori con il nome**: aziende agricole, cantine, contoterzisti o enti (idrosemina di argini) che si possono citare, con luogo, anno e due o tre dati (portata, assi, ettolitri). Oggi non c'è nessun lavoro con un nome in pagina.
8. **Anno di nascita della ditta**: in pagina c'è "dagli anni '50" e "a metà degli anni '50" (AgroNotizie 2008 scrive "fin dal 1950"). Se c'è un anno preciso, va nell'apertura.
9. **"Prima in Veneto" per cisterne e carribotte**: frase di chi-siamo, è il titolo della fascia dei numeri; chiedere se c'è un ricordo o un documento.
10. **Modelli a listino**: se le tre tabelle (50 modelli) sono ancora tutte valide; se i carribotte si fanno solo zincati. Il numero 50 e i "250 hl" della fascia dei numeri vengono da queste tabelle.
11. **Certificazioni**: in pagina solo quello che scrive il sito ("carribotte certificati CE ed omologati per la circolazione stradale", "vasche certificate CE"). Se ci sono altre certificazioni o abilitazioni (officina autorizzata, saldatura, ISO), servono i documenti da scaricare.
12. **Uscita A4**: in pagina "uscita A4 Grisignano di Zocco" come riferimento per arrivare; confermare che sia il percorso che consigliano ai clienti col trattore o col camion.
13. **Civico**: 14 (sito, usato qui) o 14/D (registro delle imprese).
14. **Orari**: chiusure estive, ponti e festa del patrono (lo stato "Aperti ora" tiene conto dei festivi nazionali e di Pasquetta, non di queste).
15. **Famiglia**: in pagina "dalla fine degli anni '80 c'è Giovanni", "all'inizio del 2000 arriva Paolo, figlio di Giovanni". Non si dice che Giovanni sia figlio di Riccardo: da chiedere se si vuole scrivere "tre generazioni".
16. **Logo**: il file vettoriale originale, se esiste (oggi ricostruito dal biglietto); e quale versione usare, "NEGRIZZOLO OFFICINA MECCANICA" (qui) o "Officine NEGRIZZOLO" (testata del sito di oggi).
17. **Foto d'archivio**: l'originale della foto del carrobotte sotto i portici (oggi una miniatura di 300 px, mostrata alla sua misura) e la sua data.
18. **AgroNotizie 2008**: in pagina c'è la frase dell'articolo ("assistenza e riparazione sempre rapido e professionale") con testata e data in Chi siamo, e il titolo dell'articolo nella fascia "Certificazioni e stampa"; chiedere se va bene citarla e se ci sono altri articoli o fiere.
19. **PEC**: non trovata; capitale sociale non pubblico (sas).

## Foto da rifare dal vero

Le foto della home sono tutte loro, intere, prese dal sito di oggi (1000 px, piazzale con auto e tralicci, luci diverse): reggono la proposta alla loro misura, non un sito di alta gamma. Una giornata di scatto, con un solo fotografo e la stessa luce (cielo coperto o fine pomeriggio), risolve:

1. **Apertura**: la facciata blu con l'insegna NEGRIZZOLO e un loro rimorchio rosso intero davanti (timone compreso), senza auto né tralicci, almeno 4000 px; una versione orizzontale 10:7 e una più stretta per il telefono. Oggi è la foto del dumper del sito (1000x700), tagliata a 854x598 per togliere il traliccio e il trattore: regge a 631 px, non oltre; con una persona dell'officina accanto al mezzo sarebbe meglio ancora.
2. **Le cinque schede in 4:3**, stessa altezza e distanza (oggi luci diverse: sole, cielo velato, tramonto; la dominante arancio della vasca è stata solo attenuata): ribaltabile con sponde, fisso a pianale carico, carrobotte zincato con la pompa, vasca inox piena d'uva in vendemmia, una macchina speciale al lavoro.
3. **Riparazioni**: le mani su una riparazione in corso nell'officina, il magazzino ricambi, un trattore di un'altra marca in officina.
4. **Taglio laser**: la loro macchina al lavoro su un loro pezzo e alcuni pezzi tagliati e piegati (oggi nessuna foto: quella del sito è del costruttore della macchina e non è usata).
5. **Persone**: Giovanni e Paolo in officina, per Chi siamo.
6. **Usato**: ogni usato fotografato di profilo e di tre quarti nel piazzale libero (nella foto di oggi del 60 q.li si vedono due auto dietro il timone, che non si tolgono senza tagliare il rimorchio).
7. **Dettagli** per le pagine prodotto: zincatura, saracinesca, pompa, cerniere delle sponde, la scritta "NE GRI ZZO LO" a luce radente.

## Licenze

- **Archivo**: Omnibus-Type, Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito da `sito/fonts`, licenza in `sito/fonts/OFL.txt`. Nessuna richiesta a Google Fonts dalla pagina.
- **Foto dell'azienda**: dal sito negrizzolo.it, solo per la proposta.
- **Foto segnaposto**: nessuna nella home. Le otto foto di `assets/esterne/` non sono usate (`assets/CREDITI.md`).

## Perché niente newsletter

Non pubblicano notizie, cataloghi o fiere, l'usato ha un solo annuncio e i clienti sono aziende agricole che telefonano. Se l'usato crescerà, un "avvisami quando c'è un usato" potrà prenderne il posto nel piede, collegato a un servizio di invio.
