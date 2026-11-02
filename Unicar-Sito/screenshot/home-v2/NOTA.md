# Unicar, home v2 (scheda d'uso)

Pagina: `sito-v2/index.html`. Costruita sulla scheda `_prova/uso/SCHEDA.md`, non è un ritocco della home in `sito/`. Rifinita il 2/11/2026 dopo le prove di tre clienti tipo e del giudice d'identità. Altezza a 1440: 4887 px compreso il piede; a 390: 7500 px. Per rifare tutto: `sh _prova/uso/script/build_v2.sh`.

Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-320`, `home-768`, `home-1024` (intere e prima schermata). Prove automatiche (`_prova/uso/script/v2_prova.mjs`): nessuno scorrimento orizzontale da 320 a 2560, né a pagina scorsa con la testata compatta; a 320-430 il bottone di chiamata sta tra 189 e 287 px dall'alto, alto da 85 a 94 px; tutti i `tel:` della pagina alti almeno 48 px; prima voce del menu "Chiamate 049 8792361" (56 px); dopo lo scorrimento la testata resta in vista con "Chiama" sul telefono, con il numero e Cami2 a 1280 e 1440; orari visibili senza dati esterni; richiesta ricambio composta e "Copia il testo"; nessun link locale o ancora senza destinazione.

## Cosa è cambiato dopo le prove

**Compiti falliti, ora riusciti**
- *"So se oggi sono aperti"* (capo magazzino) e *"dove e quando ritiro il ricambio"* (ufficio acquisti) fallivano: la riga degli orari era spenta. Ora gli orari sono testo fisso, sempre visibile senza JavaScript: "Dal lunedì al venerdì, 8-12.30 e 14-18.30, sabato e domenica chiuso". Compaiono nell'apertura, nel blocco "Magazzino ricambi", in "Orari e contatti" e nel piede. Lo script aggiunge sopra "Aperto ora, fino alle 12.30" oppure "Chiuso ora, riapre domani alle 8", calcolato sull'ora di Padova. La fonte è la scheda di Cami2 (stessa sede, stesso centralino) su oraridiapertura24.it, aggiornata il 9/9/2026, ed è il secondo punto da confermare nel LEGGIMI.

**Uso**
- Testata fissa, alta 76 px a 1440 e 64 sul telefono. Sul telefono, appena il bottone rosso esce dallo schermo, al posto della riga descrittiva compare un bottone rosso "Chiama" di 48 px. Sul computer restano in vista il numero e "Vendita e noleggio: Cami2".
- Il menu del telefono si apre con "Chiamate 049 8792361" a tutta larghezza. La voce "Dove siamo" diventa "Orari e contatti", e porta a una sezione che si apre con "Via Canada 12, Padova" e non più con uno slogan.
- Tutti i `tel:` sono alti almeno 48 px. Il numero non è più ripetuto in mezzo al testo dei carrelli sostitutivi.
- L'email della chiusura ha lo stesso bottone "Scrivete all'officina: carrello fermo" dell'apertura, con la traccia.
- Prima schermata a 1440: aggiunti indirizzo ed email. La striscia della sede ora parte dalla colonna 5 della griglia a 12 (la stessa della foto della squadra in chiusura). Il vuoto sotto la didascalia è sparito.
- Ricambi: gli anelli gommati sono nel testo e negli ingressi. Il blocco "Magazzino ricambi" ha il numero in grande, l'indirizzo e gli orari. L'indirizzo email nell'introduzione è cliccabile. I campi sono in ordine (pezzo prima della quantità) e c'è "Referente e telefono". Il nuovo bottone "Copia il testo" serve a chi usa la posta web. Una riga dice che le foto si allegano nel programma di posta. Il corpo dell'email non dice più "Allego".
- Manutenzione: la prima riga dice cosa fa il contratto. È aggiunta la formazione carrellisti (dal loro elenco di servizi, da confermare), con "Chiedeteci le prossime date". Il preventivo chiede anche il comune, l'alimentazione, le ore di lavoro, cosa serve e l'assistenza attuale. Sotto c'è "Cambiate assistenza?" con la loro frase sull'esame tecnico di ogni nuova unità.
- Tipi di carrello: "elettrici e diesel, frontali e da magazzino" nella prima schermata e nell'elenco Assistenza (Cami2: "Assistenza carrelli elevatori elettrici e diesel"). Il gas non c'è, perché non è citato.
- Zona: "Interventi su Padova e provincia", come scrivono loro, più "Fuori provincia? Chiamateci.".
- Il bottone principale dà del voi, "Chiamate l'officina", come il resto della pagina.
- Da 1180 a 1340 px la testata nasconde "Chi siamo" (resta nel piede e nel menu) e accorcia il link in "Vendita: Cami2", così Cami2 non sparisce sui portatili.
- `privacy.html` e `cookie.html` ora esistono: brevi, dicono solo cose vere della pagina.

**Identità**
- Tolta la foto di repertorio dei retrattili BT (Duc LE, Unsplash), che era l'immagine più grande della pagina, con la dicitura "Foto indicativa". Le uniche foto ora sono le loro: la sede in apertura e la squadra in chiusura. La sezione Assistenza parte dal titolo.
- "Consulenti, più che riparatori" non è più un titolo. Il titolo di Chi siamo è "L'assistenza tecnica di Cami2, in via Canada", e la loro frase è nel testo ("vogliamo affiancarle come consulenti, più che come riparatori").
- Corretta la contraddizione "Siamo nella stessa sede" contro "Cami2, via Canada 16": ora c'è "Siamo in via Canada al 12, Cami2 è al 16".
- "In grado di intervenire anche nei casi più ostici" non è più il titolo della chiusura: è nel testo di Assistenza, intera.
- I carrelli sostitutivi hanno un titoletto e il testo è a misura di paragrafo (22 px), non più un paragrafo da brochure a 33 px.
- Tolte le piccole aggiunte non loro: "Preventivi: per telefono o per email" (al suo posto "Tipi di carrello"), "In azienda o in officina", "in tutta Padova".
- "Messa in funzione entro 24 ore" resta, ma non più in grassetto, con un commento nel file. È il primo punto da confermare.

**Esecuzione**
- Carattere: Barlow al posto di Sofia Sans, che era già in BCM, Daisyplast, Molon e Teklam. Barlow non è usato in nessun'altra home della campagna (controllato il 2/11/2026).

## Cosa trova ciascun visitatore, e dove

**1. Il capo magazzino con il carrello fermo, al telefono (390 x 844).** Senza scorrere vede il logo e "Assistenza carrelli elevatori, Padova", poi "Carrello fermo?" e il bottone rosso "Chiamate l'officina 049 8792361 r.a." (da 193 a 284 px). Sotto ci sono lo stato di oggi e gli orari, le 24 ore, la zona, marche e tipi, i carrelli sostitutivi, l'indirizzo e l'email. Più in basso, il bottone "Scrivete all'officina: carrello fermo" (a circa 640 px) e la sede vera. Scorrendo, "Chiama" resta in testata.

**2. L'impiegato acquisti, al computer (1440 x 900).** Nella prima schermata trova "Ricambi: Originali e di altre marche, gomme e batterie" e il menu. Con un clic arriva a "Qualsiasi ricambio, anche uscito di produzione", al blocco "Magazzino ricambi" (numero, via Canada 12, orari) e alla richiesta già composta, con "Prepara l'email" e "Copia il testo".

**3. Il responsabile di stabilimento o l'RSPP, al computer.** Nella prima schermata ha marche, tipi, zona, orari e Cami2 in testata. Con un clic arriva a manutenzione e controlli: il contratto, il registro, funi e catene, la formazione carrellisti, il preventivo per email o per telefono e "Cambiate assistenza?". Chi siamo spiega in una riga il rapporto con Cami2. La riga di vendita porta a cami2.it, la porta accanto.

## Idea

Il sito serve a far chiamare, e quindi il protagonista è il numero. A 1440 "049 8792361" è composto a 148 px in rosso, con cifre tabellari, ed è il link di chiamata. Sul telefono lo stesso numero diventa il bottone. È la scelta d'impaginazione che manca nelle altre home della campagna: la scala tipografica è costruita su un recapito, non su un titolo. Le due foto vere, strisce panoramiche di 939 x 249, partono dalla stessa colonna della griglia a 12 e arrivano al bordo destro, a misura d'origine.

Niente legende numerate, niente carrello scontornato, niente promemoria .ics, niente numeri del gruppo, nessuna foto di repertorio.

## Caratteri e colori

- **Barlow** di Jeremy Tribby (Google Fonts, SIL Open Font License 1.1, `sito-v2/fonts/OFL.txt`), in quattro pesi (400, 500, 600, 700), solo il sottoinsieme latin, servito dalla pagina. È una grottesca nata dalle scritte stradali e dei mezzi da lavoro, vicina al lettering dei furgoni dell'assistenza. Nelle cifre grandi tiene il numero compatto e leggibile da lontano.
- Il fondo `#FAFAF8` è il bianco dei furgoni dell'assistenza, che si vedono nella foto della sede. La fascia dei controlli e il piede sono in `#ECEEEE`, l'intonaco grigio della palazzina di via Canada. L'inchiostro è `#141617` e il testo secondario `#53575B` (oltre 6:1 su tutti e due i fondi).
- Il rosso `#D7141A` è quello della C del logo, scurito quanto basta perché il bianco sul bottone passi AA (5,24:1). È l'unico colore della pagina, e compare solo dove si chiama.

## Foto

| In pagina | Origine | Licenza |
|---|---|---|
| Apertura: la sede di via Canada 12 con i furgoni e due Cesab verdi | loro sito, `assets/originali/testata/007.jpg`, 939 x 249, voto 4 | materiale loro, da usare con il loro permesso |
| Chiusura: la squadra davanti all'ingresso | loro sito, `assets/originali/testata/008.jpg`, 939 x 249, voto 3 | materiale loro, da usare con il loro permesso |
| Logo in testata, nel piede e nelle pagine privacy e cookie | loro sito, `logo-unicar-241x100.png` | materiale loro |

Il trattamento (`_prova/uso/script/v2_img.py`) è leggero: livelli, poco contrasto e saturazione, nitidezza leggera. Nessun ingrandimento; WebP e JPEG. Il furgone del service di Cami2 (voto 5) non è usato: porta la livrea Toyota e Cami2 e servirebbe il loro permesso.

## Newsletter e social

Niente newsletter: lavorano solo per aziende e a contratto, non comunicano novità, fiere o cataloghi e non hanno clienti privati. Niente colonna Seguici: Unicar non ha profili social, e quelli di Cami2 non sono loro.

## Cosa resta da confermare

L'elenco completo, in ordine, è nel LEGGIMI ("Da confermare per la versione 2"). In breve:
- le 24 ore;
- gli orari (oggi quelli dell'elenco di Cami2) e i festivi;
- il titolare e la riga legale;
- il ritiro dei ricambi;
- i tipi di carrello e la zona;
- la formazione carrellisti;
- cosa comprende il contratto di manutenzione;
- l'autorizzazione BT e Cesab;
- il permesso per le foto.
