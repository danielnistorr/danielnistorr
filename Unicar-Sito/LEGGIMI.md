# Unicar: proposta di nuova home

Proposta non richiesta di una nuova homepage per Unicar srl (assistenza carrelli elevatori, via Canada 12, Padova). Solo la home.

- Pagina: `sito/index.html` con `sito/privacy.html`, `sito/cookie.html`, `sito/img/` e `sito/fonts/`; si apre direttamente nel browser. È la versione scelta dal committente, con le aggiunte per l'uso descritte in "Versione 1 con l'uso" più sotto; la copia di prima è in `_prova/versione-1-originale/`.
- Screenshot: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440) e la nota di progetto `screenshot/home/NOTA.md`.
- Analisi con le fonti: `01-analisi.md`. Giudizio sui prototipi: `_prova/giudizio.json`.
- Per rifare tutto: `sh _prova/script/build_finale.sh`.
- Prove: `node _prova/script/v1uso_misure.mjs` (apertura da 320 a 2560, bottone di chiamata, collegamenti, stato aperto o chiuso, menu), `node _prova/script/finale_prova.mjs` (promemoria con clic, frecce e tocco, menu, piede), `node _prova/script/finale_larghezze.mjs` (scorrimento orizzontale da 320 a 2560, impaginazione dell'apertura, collegamenti), `node _prova/script/finale_viste.mjs` (larghezze di confine e righello, scrive in `_prova/tmp-finale/`, da cancellare).

## Da confermare con Unicar (non messo in pagina, o messo solo nella forma sicura)

- **Prima di tutto**: se Unicar esiste ancora come società a sé. La P.IVA 01014160285 non risulta attiva nel VIES (24/10/2026), Cami2 è in maggioranza del Gruppo Selini dal 5/11/2024 e il furgone del service porta la livrea Toyota e Cami2. Se Unicar è stata fusa in Cami2, la proposta va rivolta a Cami2.
- "Messa in funzione entro 24 ore dalla chiamata": è nel loro testo del 2012. Non è in pagina; se lo confermano, può tornare come titolo ("In funzione entro 24 ore dalla chiamata") e "Consulenti, più che riparatori" passa alla chiusura.
- Zona degli interventi: in pagina "Padova e provincia" (dal loro testo); se arrivano anche a Venezia, va detto.
- Se sono ancora assistenza autorizzata BT e Cesab, cioè Toyota Material Handling; quanti furgoni e tecnici ha oggi Unicar da sola (12 mezzi nel 2012).
- I numeri del gruppo (cami2.it/azienda/: 25 tecnici esterni con furgone, circa 3500/4000 carrelli dei clienti tra Padova e Venezia, sede di oltre 4000 mq; 3000 mq nel 2009 secondo la pagina storia): non sono più in pagina dal passaggio "con l'uso", perché confondevano chi è chi. Possono tornare solo detti come Cami2 e riconfermati.
- Se fanno ancora la formazione dei carrellisti e con quale ente; le certificazioni di Unicar (quelle trovate sono di Cami2: ISO 9001, Toyota A.S.E.C., OHSAS).
- Anno di costituzione (stima intorno al 1982, non in pagina), PEC, un numero per le emergenze: non trovati, non in pagina. Gli orari ora sono in pagina: vedi "Versione 1 con l'uso".
- Il promemoria riprende la loro "Nota informativa" sull'art. 71 del D.Lgs. 81/2008 (funi e catene ogni tre mesi, tagliando annuale, registro conservato tre anni): il testo e il calcolo vanno fatti rileggere a loro prima della pubblicazione.
- Il link "Vendita e noleggio (cami2.it)": se nel sito nuovo vendita e noleggio restano un rimando a Cami2.

## Foto da rifare dal vero (una mattina in via Canada)

Tutte le foto della home sono segnaposto tranne la sede, che è loro ma piccola (in pagina un taglio di 455 x 249 dalla striscia di 939 x 249, mai ingrandito). L'apertura è un segnaposto a tutti gli effetti: un carrello Toyota qualunque, usato, da Unsplash. È progettata perché ci vada il loro.
1. **Il carrello dell'apertura** (oggi Reding, Unsplash): un carrello appena revisionato in officina Unicar, pulito, fotografato intero (montante, cabina, contrappeso e ruote dentro l'inquadratura, con margine), di tre quarti da dietro come quello della pagina, a 1,2 m da terra, parcheggiato dentro una corsia gialla vera del loro pavimento, su fondo il più possibile neutro (un muro chiaro o il cielo coperto), luce diffusa del mattino, obiettivo 50-85 mm per non deformare, ripresa a 24 MP o più. Serve anche uno scatto con il solo fondo per scontornare. Con i vetri della cabina chiusi e puliti si evita il vetro fumé ricostruito. Se possibile un Toyota o un BT di un cliente, senza adesivi di altri concessionari.
2. **L'officina** (oggi Yurtman, Unsplash, in piccolo): un tecnico Unicar in tuta da lavoro sul montante o sulle catene, mani e attrezzo in primo piano, luce naturale dai lucernari, formato orizzontale 4:3 almeno 3000 px di lato.
3. **La sede** (oggi un taglio della striscia del loro vecchio sito): la palazzina di via Canada con l'insegna UNICAR, i furgoni dell'assistenza allineati sul piazzale, cielo sereno o coperto chiaro, panoramica orizzontale ad almeno 4000 px di lato; per la chiusura serve un taglio 3:2 di almeno 2000 px sulla palazzina con l'insegna UNICAR, che in pagina potrà crescere fino a metà larghezza.
4. Per le altre pagine: il magazzino ricambi, un furgone attrezzato aperto, il pavimento d'officina con la corsia gialla.

## Licenze

- Foto Unsplash (Reding `r4Y_VNKzAbw`, Yurtman `GjmQzjPuF30`): Unsplash License, uso commerciale libero, attribuzione non obbligatoria; dettagli, ritocchi e avvertenze sui marchi in `assets/CREDITI.md`.
- Sede (`assets/originali/testata/007.jpg`) e logo: materiale del loro sito, da usare con il loro permesso.
- Carattere Archivo: SIL Open Font License 1.1 (`sito/fonts/OFL.txt`), servito dalla pagina.

## Logo

C'è solo il PNG 241 x 100 del vecchio sito (`assets/originali/logo-unicar-241x100.png`), usato ritagliato ai bordi e mostrato a 96 px in testata e nel piede (densità 2,5x). Non è ricostruito in SVG perché la versione piatta perderebbe il rilievo grigio delle lettere. Serve il vettoriale originale; manca anche la favicon.

## Pagine che il sito nuovo dovrà avere (i link della home oggi puntano alle sezioni)

- Servizi: Assistenza e riparazione, Manutenzione programmata, Batterie e caricabatterie, Controlli di sicurezza, Formazione carrellisti.
- Ricambi.
- Chi siamo, Dove siamo (con la mappa), Normative e controlli (la nota sull'art. 71 riscritta).
- Privacy (`privacy.html`) e Cookie (`cookie.html`): ci sono in forma breve (dicono solo cose vere della pagina), da riscrivere per il GDPR con il titolare giusto (l'informativa di oggi cita ancora il D.Lgs. 196/2003).
- Vendita e noleggio: link esterno a cami2.it.

## Newsletter

Non c'è e non serve: lavorano solo per aziende, non comunicano novità, fiere o cataloghi e non hanno clienti privati. Il gesto utile per i clienti è il promemoria dei controlli, che scarica le date nel calendario.

## Versione 1 con l'uso

Il committente ha scelto questa home ("no preferisco versione 1"). Grafica, carattere Archivo, colori, corsia gialla, carrello, titolo "Consulenti, più che riparatori" e idea restano. Dalla versione 2 è stato preso solo ciò che serve ai clienti tipo della scheda (`_prova/uso/SCHEDA.md`), ridisegnato con gli elementi che la pagina aveva già. Cosa è cambiato, misura per misura: `screenshot/home/NOTA.md`, paragrafo "Versione 1 con l'uso". Per tornare indietro: `_prova/versione-1-originale/` (pagina, immagini, caratteri, screenshot e LEGGIMI di prima).

Secondo ritocco, lo stesso giorno, dopo la prova dei tre clienti tipo accanto alla versione 2 (`_prova/uso/prova-v1-prima-0..2/`): i tre compiti che non riuscivano (in quanto tempo arrivano, il tipo di carrello, vendita e noleggio subito) ora riescono. Dettagli e misure in `screenshot/home/NOTA.md`, "Secondo ritocco con l'uso".

- **Telefono**: sopra il titolo l'occhiello "Assistenza carrelli elevatori, Padova". Sotto il titolo, entro i 400 px, il bottone grafite "Chiamate l'officina 049 8792361 r.a." e subito sotto il bottone bordato "Scrivete all'officina: carrello fermo" (email con oggetto e traccia). Poi stato di oggi, orari, "Sabato e domenica chiuso", "Fuori orario? Scriveteci" quando è chiuso, e quattro righe con il filetto: messa in funzione entro 24 ore dalla chiamata, Padova e provincia (fuori provincia chiamateci), carrello sostitutivo, Toyota BT Cesab e le altre marche. Tutto senza scorrere; il carrello resta della stessa misura, subito sotto. Nella corsia: "Ricambi: cosa mandarci", "Le date dei controlli", "Vendita e noleggio: Cami2". La testata resta in vista quando si scorre, con il numero alto 48 px.
- **Computer**: stessa prima schermata, con l'occhiello, "elettrici e diesel" nel testo, "r.a." nel bottone e i collegamenti "Scrivete: carrello fermo", "Ricambi: cosa mandarci", "Vendita e noleggio: Cami2". Quando si scorre la testata resta fissa e a destra compare "Vendita e noleggio: Cami2". In testata "Orari e contatti" al posto di "Dove siamo".
- **Servizi**: Toyota, BT e Cesab anche qui; "Carrelli elettrici e diesel, anche da magazzino, di ogni marca"; carrello sostitutivo; le righe dei controlli portano ai controlli; il corso carrellisti ha una riga di spiegazione e un'email "Corso carrellisti".
- **Ricambi**: originali Toyota, BT e Cesab e di tutte le altre marche, con gli anelli gommati tra i consumabili; cosa mandare; il bottone "Chiedete un ricambio" (email "Richiesta ricambio" con la traccia); "oppure 049 8792361" grande; l'indirizzo email in chiaro per la posta web; il magazzino in via Canada 12 con gli orari, più leggibile.
- **Controlli**: il contratto di manutenzione programmata e "Cambiate assistenza?" in due righe, il bottone "Chiedete un preventivo" (email "Preventivo manutenzione programmata") con "oppure 049 8792361"; il promemoria resta a destra per chi è già cliente.
- **Chi siamo**: una riga su Unicar e Cami2 al posto dei numeri del gruppo, ora a 16 px, e "Comprare o noleggiare un carrello: cami2.it". Il piede "Chi siamo" porta lì.
- **Orari e contatti** (chiusura): "Messa in funzione entro 24 ore dalla chiamata" con il carrello sostitutivo, stato di oggi, orari della settimana, "Fuori orario? Scriveteci", email con oggetto, "Scrivete all'officina: carrello fermo", "Apri la mappa", "Indicazioni stradali", tutti alti almeno 48 px. Orari anche nel piede.
- **Foto**: il carrello e l'officina (Unsplash) restano con "Foto indicativa"; la sede vera resta in chiusura.
- **Riga legale**: senza P.IVA, REA e capitale finché non si sa chi è il titolare oggi.
- Per rifare tutto: `sh _prova/script/build_finale.sh` (ora lancia anche `v1uso_misure.mjs`; gli screenshot passano da `_prova/script/v1uso_shoot.mjs`, copia del kit senza scorrimento morbido).

### Da confermare per la versione 1 con l'uso (in ordine di importanza)

1. **Gli orari**: in pagina "Lunedì-venerdì 8-12.30 e 14-18.30, sabato e domenica chiuso", con "Aperto ora" o "Chiuso ora" calcolato sull'ora di Roma. Vengono dalla scheda di Cami2 (stessa sede e stesso centralino) su oraridiapertura24.it, aggiornata il 9/9/2026 (01-analisi.md, dati), non da una fonte di Unicar. Vanno confermati per l'officina e per il magazzino ricambi, con i festivi e la chiusura estiva, che lo script non conosce. Se cambiano si correggono in due posti: la variabile `ORARI` nello script in fondo a `sito/index.html` e i testi fissi (apertura, ricambi, chiusura, piede).
2. **Un numero per le emergenze o una reperibilità del sabato**: non trovati. Se c'è, va accanto al bottone di chiamata, al posto di "Chiuso ora".
3. **"Messa in funzione entro 24 ore dalla chiamata"** (loro testo del 2012, pagina `azienda`): ora è in pagina, nella prima schermata del telefono e in "Orari e contatti", con un commento nel codice. Va confermato che valga oggi e per quale zona; se non vale, si toglie in due punti (la riga in `ul.pronto` dell'apertura e il paragrafo `.sotto` della chiusura). Lo stesso vale per "Fuori provincia? Chiamateci.", che è solo un invito: se fuori provincia non vanno, si toglie.
4. **Chi è il titolare oggi** (P.IVA non valida nel VIES): da lì la riga legale, la privacy e il destinatario della proposta (Unicar o Cami2).
5. **La riga su Cami2**: "Unicar è l'officina a cui la consociata Cami2 affida l'assistenza tecnica dei carrelli; Cami2, al numero 16, li vende e li noleggia" (da cami2.it/azienda/storia/). Va fatta rileggere, soprattutto se Unicar è stata assorbita.
6. **Il magazzino ricambi**: se si ritira al banco di via Canada 12 negli stessi orari, se spediscono o porta il tecnico, se c'è un indirizzo email per i ricambi. In pagina c'è solo "Magazzino ricambi in via Canada 12, Padova" con gli orari: le parole "ritiro al banco" chieste dal cliente tipo entrano solo se lo confermano.
6a. **Il corso carrellisti**: in pagina "Corso teorico e pratico per conduttori di carrelli elevatori. Chiedeteci le prossime date" (dalla loro notizia sul corso, con un'email "Corso carrellisti"). Va confermato che lo facciano ancora e con quale ente; se no, resta solo la voce "Formazione per carrellisti" o si toglie anche quella.
6b. **I tipi di carrello**: in pagina "elettrici e diesel, anche da magazzino" (cami2.it, pagina Assistenza: "elettrici e diesel"; i retrattili BT del corso). Il gas non è in nessuna fonte, anche se il carrello segnaposto dell'apertura è un Toyota a gas: se seguono anche quelli, va aggiunto.
6c. **"Fuori orario? Scriveteci con i dati del carrello"**: la versione 2 prometteva "vi richiamiamo alla riapertura"; qui non c'è, perché non l'hanno scritto loro. Se leggono la posta alla riapertura e richiamano, si può aggiungere.
7. **Il preventivo**: se la traccia dell'email chiede le cose giuste (comune, carrelli, ore di lavoro, cosa serve, assistenza attuale).
8. Gli altri punti di sopra restano: zona, autorizzazione BT e Cesab, formazione carrellisti, testo sull'art. 71 da rileggere, permesso per le foto e il logo.

### Foto da rifare dal vero per la versione 1 con l'uso

Le stesse di "Foto da rifare dal vero" più sopra, nello stesso ordine: il carrello dell'apertura e l'officina oggi sono Unsplash con "Foto indicativa", e la dicitura si toglie solo quando ci sono le loro. Per il telefono, il carrello dell'apertura va ripreso con un po' di margine sopra il montante: in pagina è largo l'88 % dello schermo, sotto il bottone di chiamata.

## Versione 2 (scheda d'uso)

Una seconda home, costruita sulla scheda d'identità e d'uso (`_prova/uso/SCHEDA.md`) e non sulla home precedente, che resta com'è in `sito/`. Rifinita il 2/11/2026 dopo le prove di tre clienti tipo e del giudice d'identità, poi ricomposta lo stesso giorno con due caratteri, otto livelli di scala e un impianto diverso per sezione, senza spostare nulla di ciò che serve sul telefono (cosa è cambiato: `screenshot/home-v2/NOTA.md`).

- Pagina: `sito-v2/index.html`, con `sito-v2/privacy.html`, `sito-v2/cookie.html`, `sito-v2/img/` e `sito-v2/fonts/`; si apre direttamente nel browser.
- Caratteri, serviti dalla pagina: Big Shoulders Display (Patric King, Xotype) per titoli, numeri di telefono e cifre grandi, e Asap (Omnibus-Type) per testo, menu, bottoni e dati. Tutti e due da Google Fonts, SIL Open Font License 1.1, uso commerciale libero (`fonts/OFL-BigShoulders.txt`, `fonts/OFL-Asap.txt`). Il perché, la scala e l'impianto di ogni sezione sono nella NOTA.
- Screenshot e nota di progetto: `screenshot/home-v2/` e `screenshot/home-v2/NOTA.md`.
- Per rifare tutto: `sh _prova/uso/script/build_v2.sh` (immagini con `v2_img.py`, caratteri, controllo dei caratteri vietati, prove con `v2_prova.mjs`, screenshot con `v2_shoot.py`; `v2_menu.mjs` fotografa il menu aperto a 390; `v2_misure.mjs` misura dove stanno bottone, orari e recapiti nella prima schermata da 320 a 430, e `v2_largo.mjs` cerca gli elementi che escono a destra).
- In breve: sul telefono, nei primi 300 px, il bottone rosso a tutta larghezza "Chiamate l'officina 049 8792361 r.a.". Sotto: gli orari con "Aperto ora" o "Chiuso ora, riapre...", le 24 ore, la zona, le marche e i tipi di carrello, i carrelli sostitutivi, indirizzo ed email, e il bottone "Scrivete all'officina: carrello fermo" con la traccia già scritta. La testata resta in vista: sul telefono, appena il bottone rosso esce dallo schermo, compare "Chiama". A 1440 il numero è il titolo grande della pagina (172 px, in Big Shoulders Display), sopra la loro sede; più giù "Toyota, BT, Cesab" a 168 px, le scadenze dei controlli in cifre grandi e la chiusura con la squadra a filo del bordo sinistro.

### Da confermare per la versione 2 (in ordine di importanza)

1. **"Messa in funzione entro 24 ore dalla chiamata"** (prima schermata, dal loro testo del 2012): se vale ancora oggi e su quale zona. Nel file c'è un commento accanto alla riga. Se non arriva conferma, sostituirla con "Furgoni attrezzati per l'intervento in azienda".
2. **Gli orari**: in pagina ci sono "Dal lunedì al venerdì, 8-12.30 e 14-18.30, sabato e domenica chiuso". Vengono dalla scheda di Cami2 (stessa sede e stesso centralino) su oraridiapertura24.it, aggiornata il 9/9/2026, e non da una fonte di Unicar. Vanno confermati per l'officina e per il magazzino ricambi, insieme ai festivi e alla chiusura estiva. Se cambiano, si correggono in due posti: la variabile `ORARI` nello script in fondo a `index.html` (calcola "Aperto ora" sull'ora di Padova) e i testi fissi (apertura, magazzino ricambi, dove siamo, piede). Va chiesto anche se esiste un numero per le emergenze o una reperibilità del sabato.
3. **Chi è il titolare oggi** (P.IVA non valida nel VIES): la riga legale non porta P.IVA, REA né capitale finché non si sa. Le pagine `privacy.html` e `cookie.html` dicono solo cose vere della pagina (nessun cookie, il modulo non invia nulla) e vanno riscritte per il GDPR con il titolare giusto.
4. **Il ritiro dei ricambi**: se si ritirano al magazzino di via Canada 12 negli stessi orari, se li spediscono o li porta il tecnico con il furgone, e se c'è un interno o un indirizzo email dedicato ai ricambi.
5. **Tipi di carrello**: in pagina "elettrici e diesel, frontali e da magazzino" (Cami2: "Assistenza carrelli elevatori elettrici e diesel"). Se seguono anche i carrelli a gas, i transpallet e i commissionatori, si aggiungono.
6. **Zona**: in pagina "Interventi su Padova e provincia" e "Fuori provincia? Chiamateci.". Se coprono anche Venezia, va scritto.
7. **Formazione carrellisti**: in pagina, nei controlli, come "corso teorico e pratico per i conduttori di carrelli elevatori" con "Chiedeteci le prossime date". È nel loro elenco di servizi ma la notizia è del 2012: confermare che lo fanno ancora e con quale ente; se no, togliere la riga, la voce del piede e "corso carrellisti" dall'email del preventivo.
8. **Manutenzione programmata**: in pagina "i controlli e il tagliando si fanno alle scadenze concordate con voi". Confermare se il registro lo compilano e lo tengono loro e se il controllo trimestrale di funi e catene è compreso nel contratto; solo allora si può scrivere "ve lo ricordiamo noi".
9. Se sono ancora assistenza autorizzata BT e Cesab (Toyota Material Handling) e per i caricabatterie; il testo sull'art. 71 da far rileggere.
10. Le indicazioni per arrivare in via Canada (zona industriale, uscita da prendere): non trovate, non in pagina. Ci sono i link "Indicazioni stradali" e "Apri in Google Maps".

### Pagine che il sito nuovo dovrà avere (link della versione 2)

- Oggi i link puntano alle sezioni della home: `#assistenza`, `#ricambi`, `#controlli`, `#chi-siamo`, `#dove` (Orari e contatti). Nel sito vero diventano Assistenza e riparazione, Ricambi (con il modulo di richiesta), Manutenzione programmata e controlli, Batterie e caricabatterie, Formazione carrellisti, Chi siamo, Dove siamo (con la mappa e gli orari) e Normative (la nota sull'art. 71).
- `privacy.html` e `cookie.html` esistono già in `sito-v2/` in forma breve, da riscrivere per il GDPR.
- Vendita e noleggio: link esterno a https://www.cami2.it/.
- Il modulo "Chiedete un ricambio" non invia nulla: prepara l'email (o la copia negli appunti per chi usa la posta web). Se nel sito vero si vuole un invio diretto con le foto allegate, va collegato a un servizio di posta del sito.

### Foto da rifare dal vero per la versione 2

1. **La sede per l'apertura**: la palazzina di via Canada con l'insegna Unicar e i furgoni allineati, panoramica orizzontale di almeno 4000 px di lato, oppure l'originale ad alta risoluzione della foto di oggi se Unicar o Cami2 ce l'hanno. Stesso taglio della striscia di oggi (circa 3,8:1) più un taglio 2:1 sull'ingresso per il telefono. Luce del mattino, cielo coperto chiaro. Oggi la striscia è 939 px e su schermi retina è morbida.
2. **Un tecnico al lavoro**: un tecnico Unicar in tuta sul carrello di un cliente, con il furgone aperto alle spalle. Orizzontale, almeno 3000 px, luce naturale, senza marchi di altri concessionari. Va nella sezione Assistenza, dove oggi non c'è nessuna foto (la foto di repertorio dei retrattili è stata tolta).
3. **Il magazzino ricambi**: gli scaffali o il banco, per la sezione Ricambi.
4. **La squadra per la chiusura**: la stessa foto di gruppo davanti all'ingresso, rifatta ad alta risoluzione (almeno 4000 px), con i volti leggibili.
5. Il furgone del service con la livrea che userà Unicar, e il logo in vettoriale.
