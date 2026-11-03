# Termit, proposta di nuova home: leggimi

Proposta non richiesta di nuova homepage per Termit srl (Saonara, PD). Solo la home. Versione del 03/11/2026, "livello professionale": prima l'uso (chi riordina dal telefono, l'ufficio tecnico che cerca un prodotto, chi manda un disegno), poi la loro identità, poi l'esecuzione da studio. Regole in `_metodo/professionale/REGOLE.md`, famiglia M; esito regola per regola in `screenshot/home/NOTA.md`.

## Cosa c'è

- `sito/index.html`: la home, statica, si apre con file:///. Caratteri in `sito/fonts/`, immagini in `sito/img/` (solo il taglio ad acqua, il logo e la favicon).
- `screenshot/home/`: home-1440.jpg, home-1440-prima-schermata.jpg, home-390.jpg, home-390-prima-schermata.jpg, chiusura-1440.jpg, `NOTA.md`.
- `_prova/script/build_finale.sh`: rifà tutto (immagini `pro_img.py`, pagina `pro_build.py` dal modello `pro_modello.html`, screenshot `finale_screenshot.mjs`, controlli `pro_controlli.mjs` con esito in `_prova/pro_controlli.json`). `pro_schede_pdf.py` rilegge da termit.biz gli indirizzi delle pagine prodotto e dei PDF (`_prova/crawl/schede-pdf.json`). Le pagine delle otto famiglie scaricate il 03/11/2026 (conteggio delle schede) sono in `_prova/crawl/famiglie/`.
- `_prova/versione-1-originale/`: la home di prima (coppella disegnata, foto di repertorio, newsletter) con i suoi screenshot.
- `01-analisi.md` (fatti con le fonti, sez. 10 aggiunta il 03/11/2026), `_prova/uso/SCHEDA.md` (identità e uso), `assets/CREDITI.md`.

## Da chiedere o confermare con l'azienda (in pagina solo ciò che è nelle fonti)

1. **Email, prima di pubblicare.** In pagina info@termit.biz (condizioni di fornitura e post LinkedIn), anche nella prima schermata ("Ordini per scritto a info@termit.biz") e in tutti i mailto; il piede del sito di oggi scrive info@termitisolanti.com, che non risponde in https. Gli ordini scritti sono l'unico canale valido per le condizioni di fornitura: far confermare a Termit l'indirizzo per gli ordini e mandare una mail di prova. Se sono attivi tutti e due, usare quello indicato da loro e mettere l'altro in copia nei mailto (`&cc=`, in `_prova/script/pro_build.py`).
2. **Ordini per fax.** Le condizioni ammettono il fax (049 644900): è ancora attivo? In pagina non c'è; gli ordini sono "per scritto, via email".
3. **Ritiro al banco.** Si può ritirare a Saonara? Non è scritto da nessuna parte: in pagina c'è solo "Come arrivare" al magazzino.
4. **Mezzi propri o trasportatori.** Chi siamo dice "il più delle volte con propri mezzi", le condizioni "trasportatori specializzati" con automezzi di circa 10 metri. In pagina i camion di circa 10 m sono dei trasportatori ("Trasportatori con camion di circa 10 m") e "il più delle volte con propri mezzi" resta solo come frase di Chi siamo (citazione in Consegne e fatto "Consegne rapide" nell'apertura): quanti camion propri ci sono, con il logo, e quando consegnano loro e quando i trasportatori?
5. **Zone servite e tempi tipici.** In pagina solo "da 1 a 7 giorni" dal ritiro in magazzino (condizioni). Consegnano in tutta Italia? Quanto ci vuole di solito nel Veneto?
6. **Pezzi su misura.** Formati accettati per il disegno (PDF, DXF, STEP?), tempi in giorni, spessori massimi della macchina ad acqua. In pagina "disegno quotato in allegato" senza formati.
7. **Orari e chiusure.** Chiusure estive, settimana di Natale, ponti e patrono di Saonara: lo stato "Aperti ora / Chiusi" conosce solo i festivi nazionali e il lunedì dell'Angelo, quindi in un giorno di chiusura aziendale direbbe "Aperti". Chiedere il calendario e aggiungere le date all'elenco `festivo()` nello script della pagina. Nell'ultima mezz'ora lo stato dice "Aperti ancora per N minuti".
8. **Numeri.** In pagina: più di cinquant'anni (Chi siamo), ISO 9001 dal 2004 (certificato RINA), 251 schede a catalogo (contate sul sito), 11 dipendenti (aziende.it, 2025). Confermare gli 11 dipendenti e l'anno di inizio dell'attività (la srl è iscritta il 03/01/2000; LinkedIn dice "oltre 55 anni"). Superficie del magazzino e numero di referenze a stock, se si possono dire: sarebbero due numeri forti per la fascia verde. Il fatturato (13,3 milioni, aziende.it) non è in pagina.
9. **Recensioni.** Nessuna trovata (Google Maps e Pagine Gialle non si aprono in automatico). Guardare a mano la scheda Google e chiedere se si possono citare due o tre clienti con nome e comune.
10. **Clienti e lavori con nome.** La famiglia M dei riferimenti mostra progetti con cliente, luogo e anno: chiedere 3 lavori su misura (per esempio un forno, una cabina insonorizzata, un cantiere navale) con il permesso di citarli e una foto ciascuno.
11. **EcoVadis** (anno della medaglia di bronzo) ed **EIIF** (adesione ancora attiva). Il certificato Ogyre è intestato ad ANICTA: non è citato.
12. **Partner.** In pagina le marche come le scrive la pagina Partners; la ricerca, scrivendo una marca, mostra le schede che la nominano e quelle della famiglia che la pagina Partners le associa (K-Flex per l'elastomero, Ursa per la lana di vetro...). Confermare l'abbinamento marca e famiglia, o dare il marchio di ogni scheda.
13. **Schede.** 138 schede nella ricerca (crawl del 24/10/2026), 126 con il PDF del produttore e 137 con la pagina su termit.biz; la pagina di Termit Isolbag 039 risponde 404. Sul loro sito la pagina AL CLAD lastra punta a "ALCLAD - Copy 1.pdf", che risponde 404: in home porta a ALCLAD.pdf ("TUBO e LASTRA AL CLAD"), da far correggere anche sul loro sito. I numeri sopra le otto famiglie (25, 24, 23, 15, 11, 15, 13, 22) sono contati sulle pagine di categoria del 03/11/2026 e non coincidono con i conteggi della ricerca (per esempio "lana di vetro" ne trova 25), che usa solo le 138 schede del crawl: nel sito vero la ricerca va letta dal catalogo, così i numeri tornano. Unifrax e Morgan non sono nominati in nessuna scheda: la ricerca lo dice e mostra le schede per alte temperature; chiedere quali prodotti di quelle marche hanno a magazzino.
14. **Link.** Le famiglie, i settori, Chi siamo, il certificato e le condizioni di fornitura aprono le pagine vere di termit.biz di oggi. Privacy e Cookie puntano a `privacy/` e `cookie/`, da scrivere (oggi l'informativa sta su un dominio esterno).
15. **Logo vettoriale.** Esiste solo in raster (PNG 539x85, ricolorato nel verde #51B038): chiederlo al grafico o a Two Made srl.
16. **Diritti della foto del taglio ad acqua.** È l'unica foto loro: confermare che sia scattata da Termit nel loro capannone.

17. **Recensioni, clienti e lavori** (regole 10 e 11 dello studio, non passano): in pagina ci sono solo numeri, certificazioni e partner. Servono 2-3 recensioni con nome e comune (con il permesso) e 3 lavori con cliente o luogo, anno e una foto larga.

## Modulo di contatto: da collegare

Il modulo in home ("Richiesta a Termit": ordine, offerta o listino, pezzo su misura, consiglio tecnico; nome, azienda, telefono, email, codici o materiale e quantità, indirizzo di consegna, messaggio) oggi **non invia nulla**: controlla nome, azienda e telefono e compone un'email a info@termit.biz con oggetto e campi già scritti, che il visitatore controlla e invia dal suo programma di posta. Il disegno si allega a quell'email. Per il sito vero va collegato a un servizio (per esempio il modulo del CMS con invio SMTP, o Formspree) con l'allegato del file, la ricevuta automatica e l'informativa privacy. Anche i bottoni "Scrivi un ordine", "Mandateci il disegno" e "Chiedete il listino" sono email con oggetto e traccia già compilati.

## Foto da fare dal vero (una giornata in azienda)

Per decisione del committente in pagina non c'è nessuna foto di repertorio e nessun disegno: la home si regge su tipografia, il verde del marchio e i fatti. L'unica foto è il taglio ad acqua del loro sito (1000 px, scattata col telefono), ritagliata a 1000x639 per togliere le righe chiare in fondo e mostrata al massimo a 656 px, senza didascalia. Le foto da fare, in ordine di importanza, con un solo fotografo e la stessa luce:

1. **Il magazzino** con le pile di rotoli, pannelli e coppelle, corsia in prospettiva, persone al lavoro che non guardano l'obiettivo. Orizzontale 3:2, almeno 3000 px, con zone scure dove stare sul nero: va nell'apertura nera a 1440, a tutta larghezza tra i quattro fatti e il catalogo, e a 390 sotto la ricerca (regola 3).
2. **La macchina ad acqua in funzione** con luce controllata, le teste 1, 2, 3 leggibili e un pezzo appena tagliato con il bordo netto. Orizzontale, almeno 2800 px: va al posto della foto da telefono nella sezione Su misura.
3. **Un camion carico vero** davanti al magazzino, con il logo se c'è (quello del sito di oggi è un fotomontaggio): va nella sezione Consegne.
4. **I materiali in sezione**, in macro, stesso fondo e taglio quadrato: lana di roccia, lana di vetro, elastomero, aerogel, calcio silicato, lamierino, una coppella, un nastro. Vanno sopra le otto famiglie del catalogo (oggi solo testo, regola 9).
5. **La squadra** (ufficio, magazzino, taglio), ritratto in magazzino: per la fascia verde "Una storia lunga più di cinquant'anni".
6. **Tre pezzi su misura finiti** per i lavori con il nome (punto 10 sopra).

## Licenze

- Caratteri: Zalando Sans Expanded (titoli) e Zalando Sans (testo), SIL Open Font License 1.1, da Google Fonts, serviti dalla pagina (`sito/fonts/OFL.txt`). Uso commerciale libero.
- Foto: solo la foto del taglio ad acqua del sito Termit e il loro logo (da confermare, punto 16). Nessuna foto di repertorio, nessuna immagine generata dall'IA, nessun disegno. Dettagli in `assets/CREDITI.md`.
