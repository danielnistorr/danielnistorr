# Unicar: proposta di nuova home

Proposta non richiesta di una nuova homepage per Unicar srl (assistenza carrelli elevatori, via Canada 12, Padova). Solo la home.

- Pagina: `sito/index.html` con `sito/img/` e `sito/fonts/`; si apre direttamente nel browser.
- Screenshot: `screenshot/home/` (home-1440, home-1440-prima-schermata, home-390, home-390-prima-schermata, chiusura-1440) e la nota di progetto `screenshot/home/NOTA.md`.
- Analisi con le fonti: `01-analisi.md`. Giudizio sui prototipi: `_prova/giudizio.json`.
- Per rifare tutto: `sh _prova/script/build_finale.sh`.
- Prove: `node _prova/script/finale_prova.mjs` (promemoria con clic, frecce e tocco, menu, piede), `node _prova/script/finale_larghezze.mjs` (scorrimento orizzontale da 320 a 2560, impaginazione dell'apertura, collegamenti), `node _prova/script/finale_viste.mjs` (larghezze di confine e righello, scrive in `_prova/tmp-finale/`, da cancellare).

## Da confermare con Unicar (non messo in pagina, o messo solo nella forma sicura)

- **Prima di tutto**: se Unicar esiste ancora come società a sé. La P.IVA 01014160285 non risulta attiva nel VIES (24/10/2026), Cami2 è in maggioranza del Gruppo Selini dal 5/11/2024 e il furgone del service porta la livrea Toyota e Cami2. Se Unicar è stata fusa in Cami2, la proposta va rivolta a Cami2.
- "Messa in funzione entro 24 ore dalla chiamata": è nel loro testo del 2012. Non è in pagina; se lo confermano, può tornare come titolo ("In funzione entro 24 ore dalla chiamata") e "Consulenti, più che riparatori" passa alla chiusura.
- Zona degli interventi: in pagina "Padova e provincia" (dal loro testo); se arrivano anche a Venezia, va detto.
- Se sono ancora assistenza autorizzata BT e Cesab, cioè Toyota Material Handling; quanti furgoni e tecnici ha oggi Unicar da sola (12 mezzi nel 2012).
- I numeri del gruppo in pagina sono di Cami2 e Unicar insieme (cami2.it/azienda/: 25 tecnici esterni con furgone, circa 3500/4000 carrelli dei clienti tra Padova e Venezia): in pagina sono detti "delle due aziende insieme"; vanno riconfermati.
- La metratura della sede: in pagina "oggi di oltre 4000 mq" (cami2.it/azienda/); la pagina storia di Cami2 dice che nel 2009 la sede è arrivata a 3000 mq. Va confermato il dato di oggi.
- Se fanno ancora la formazione dei carrellisti e con quale ente; le certificazioni di Unicar (quelle trovate sono di Cami2: ISO 9001, Toyota A.S.E.C., OHSAS).
- Anno di costituzione (stima intorno al 1982, non in pagina), orari dell'officina, PEC, un numero per le emergenze: non trovati, non in pagina. Se ci sono gli orari, vanno nella chiusura sotto l'indirizzo.
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
- Privacy (`privacy.html`) e Cookie (`cookie.html`), riscritte per il GDPR (l'informativa di oggi cita ancora il D.Lgs. 196/2003): i due link del piede puntano già a questi file.
- Vendita e noleggio: link esterno a cami2.it.

## Newsletter

Non c'è e non serve: lavorano solo per aziende, non comunicano novità, fiere o cataloghi e non hanno clienti privati. Il gesto utile per i clienti è il promemoria dei controlli, che scarica le date nel calendario.

## Versione 2 (scheda d'uso)

Una seconda home, costruita sulla scheda d'identità e d'uso (`_prova/uso/SCHEDA.md`) e non sulla home precedente, che resta com'è in `sito/`. Rifinita il 2/11/2026 dopo le prove di tre clienti tipo e del giudice d'identità (cosa è cambiato: `screenshot/home-v2/NOTA.md`).

- Pagina: `sito-v2/index.html`, con `sito-v2/privacy.html`, `sito-v2/cookie.html`, `sito-v2/img/` e `sito-v2/fonts/` (Barlow, SIL Open Font License 1.1, `fonts/OFL.txt`); si apre direttamente nel browser.
- Screenshot e nota di progetto: `screenshot/home-v2/` e `screenshot/home-v2/NOTA.md`.
- Per rifare tutto: `sh _prova/uso/script/build_v2.sh` (immagini con `v2_img.py`, caratteri, controllo dei caratteri vietati, prove con `v2_prova.mjs`, screenshot con `v2_shoot.py`; `v2_menu.mjs` fotografa il menu aperto a 390).
- In breve: sul telefono, nei primi 300 px, il bottone rosso a tutta larghezza "Chiamate l'officina 049 8792361 r.a.". Sotto: gli orari con "Aperto ora" o "Chiuso ora, riapre...", le 24 ore, la zona, le marche e i tipi di carrello, i carrelli sostitutivi, indirizzo ed email, e il bottone "Scrivete all'officina: carrello fermo" con la traccia già scritta. La testata resta in vista: sul telefono, appena il bottone rosso esce dallo schermo, compare "Chiama". A 1440 il numero è il titolo grande della pagina, accanto alla loro sede.

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
