# Unicar, home v2 (scheda d'uso)

Pagina: `sito-v2/index.html`. Costruita sulla scheda `_prova/uso/SCHEDA.md`, non è un ritocco della home in `sito/`. Rifinita il 2/11/2026 dopo le prove di tre clienti tipo e del giudice d'identità, poi ricomposta lo stesso giorno con due caratteri, una scala a otto livelli e un impianto diverso per ogni sezione (paragrafo "Caratteri, scala e impaginazione"). Altezza a 1440: 5968 px compreso il piede; a 390: 8098 px. Per rifare tutto: `sh _prova/uso/script/build_v2.sh`.

Screenshot in questa cartella: `home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, più `home-320`, `home-768`, `home-1024` (intere e prima schermata). Prove automatiche (`_prova/uso/script/v2_prova.mjs`): nessuno scorrimento orizzontale da 320 a 2560, né a pagina scorsa con la testata compatta; a 320-430 il bottone di chiamata sta tra 186 e 287 px dall'alto, alto da 85 a 94 px; tutti i `tel:` della pagina alti almeno 48 px; prima voce del menu "Chiamate 049 8792361" (56 px); dopo lo scorrimento la testata resta in vista con "Chiama" sul telefono, con il numero e Cami2 a 1280 e 1440; orari visibili senza dati esterni; richiesta ricambio composta e "Copia il testo"; nessun link locale o ancora senza destinazione.

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
- Caratteri: prima Barlow al posto di Sofia Sans (già in BCM, Daisyplast, Molon e Teklam); poi, su richiesta del committente, l'accoppiata Big Shoulders Display e Asap (paragrafo seguente).

## Caratteri, scala e impaginazione (2/11/2026)

Richiesta del committente: "usa più accoppiate di font e grandezze e layout mescolati". Prima la pagina aveva una famiglia sola (Barlow) e cinque sezioni di fila con la stessa griglia: titolo nelle colonne 1-5, testo nelle colonne 7-12. Ora ha due caratteri con ruoli fissi, otto livelli di scala e sei impianti diversi. L'uso non cambia: stessi testi, stessi link, stesso ordine sul telefono. La copia della pagina di prima è in `_prova/uso/prima-tipografia-index.html`.

**L'accoppiata, e perché**
- **Big Shoulders Display** (Patric King, Xotype; Google Fonts, SIL Open Font License 1.1, `sito-v2/fonts/OFL-BigShoulders.txt`). Fa i titoli, i numeri di telefono, le marche e le cifre dei controlli; mai sotto i 28 px. È un grottesco stretto nato dalla segnaletica industriale di Chicago: ha il passo delle scritte sui mezzi da lavoro e delle targhe di portata, e riprende il condensato della loro vecchia testata ("AFFIDABILI DI NATURA") senza il gioco grafico. Stretto vuol dire anche pratico: sul telefono il numero nel bottone rosso cresce da 44 a 45-50 px nella stessa altezza di riga, e a 1440 lo stesso numero arriva a 172 px in otto colonne.
- **Asap** (Omnibus-Type; Google Fonts, SIL Open Font License 1.1, `sito-v2/fonts/OFL-Asap.txt`). Fa il testo, il menu, i bottoni, il modulo, gli orari e le didascalie. È una grottesca da schermo, aperta e con l'altezza della x alta (0,52), quindi leggibile a 15-17 px. Le cifre tabellari sono di serie, così gli orari e il fax stanno in colonna. Ha uno scheletro diverso dal titolo, largo dove l'altro è stretto, e non si confondono.
- Due famiglie, non tre: un monospazio per i dati sarebbe un segnale da IA (guida, regola a.3), e le cifre tabellari di Asap bastano. Due file variabili (latin) serviti dalla pagina, 79 KB in tutto. Pesi usati: Big Shoulders 700 e 800; Asap 400, 500 e 600. Nessuno dei due è in un'altra home della campagna né nelle liste b della guida (controllato il 2/11/2026; Antonio, l'altro condensato possibile, è già in Nardi e Belletti).
- Le pagine `privacy.html` e `cookie.html` usano gli stessi due caratteri.

**La scala (a 1440 e a 390)**

| Livello | Uso | Carattere | 1440 | 390 |
|---|---|---|---|---|
| 1 | il numero dell'officina in apertura | Big Shoulders 800 | 172 px | 45 px, nel bottone |
| 2 | "Toyota, BT, Cesab" | Big Shoulders 800 | 168 px | 64 px |
| 3 | le scadenze dei controlli (3 mesi, 1 anno, 3 anni) | Big Shoulders 800 | 150 px | 72 px |
| 4 | titoli di sezione e della chiusura | Big Shoulders 700-800 | 76-107 px | 40-48 px |
| 5 | frasi grandi da sole (carrelli sostitutivi, contratto) | Asap 400-600 | 38 px | 24 px |
| 6 | paragrafo d'apertura di sezione, ingressi | Asap 400 e Big Shoulders 700 | 22 e 31 px | 19 e 28 px |
| 7 | testo, menu, bottoni, recapiti | Asap 400-600 | 16-18 px | 16-17 px |
| 8 | didascalie, etichette, fonti, riga legale | Asap 500-600 | 14-15 px | 14-15 px |

I numeri di telefono hanno un corpo proprio in ogni punto: 31 px in testata, 172 in apertura, 30 accanto al preventivo, 58 nel magazzino ricambi, 68 nella chiusura, 30 nel piede. Sono sempre in Big Shoulders 800 e sempre in rosso.

**Un impianto per sezione (nessuna griglia uguale a quella prima)**
1. *Apertura* (invariata nella struttura): otto colonne al titolo e al numero, quattro ai fatti; sotto, gli ingressi in quattro colonne e la sede al bordo destro.
2. *Assistenza*, tipografica a tutta larghezza: il titolo, poi "Toyota, BT, Cesab" a 168 px con accanto "e tutte le altre marche, elettrici e diesel" in piccolo; il testo a scalino dalla colonna 5; i sei servizi su tre colonne; infine "Carrelli sostitutivi" come una frase grande da sola, rientrata di una colonna. Chi cerca la sua marca la vede da lontano.
3. *Ricambi*, due colonne sbilanciate sotto un titolo largo: quattro colonne al testo e al magazzino (numero a 58 px, indirizzo, orari), sette al modulo.
4. *Manutenzione e controlli*, una tavola di cifre sulla fascia d'intonaco: le tre scadenze della loro Nota informativa in cifre grandi su tre colonne uguali (sul telefono la cifra sta accanto alla sua riga); sotto, il contratto come frase grande con il bottone a sinistra e le due note strette a destra.
5. *Chi siamo*, testo a scalino: il titolo nelle colonne 1-7, il testo che parte dalla colonna 6 una riga più in basso; sotto, la riga larga verso Cami2 con "cami2.it" a 60 px.
6. *Chiusura*, la foto a sinistra: la squadra a filo del bordo sinistro (in apertura la sede è a filo del destro), "Via Canada 12, Padova" a 107 px sotto la foto e i recapiti a destra.
7. *Piede*: logo e riga su chi sono, poi Servizi, Azienda, Contatti in colonne di larghezza diversa, con il numero in Big Shoulders.

**L'uso è rimasto dov'era** (misure in `_prova/uso/misure-prima-tipografia.json` e `misure-dopo-tipografia.json`, script `_prova/uso/script/v2_misure.mjs`)
- A 390 e a 430 il titolo, il bottone di chiamata (193-284 px a 390), gli orari, le 24 ore, la zona, le marche, l'indirizzo con l'email e "Scrivete all'officina" stanno agli stessi pixel di prima. A 360 è tutto uguale; a 320 tutto più in alto, da 3 a 46 px.
- Per tenere le altezze, sul telefono il numero nel bottone usa la stessa altezza di riga di prima, e sotto i 380 px la lista dei fatti è stretta di un centesimo di em. Asap infatti è un po' più larga di Barlow e avrebbe mandato a capo due righe.
- `v2_prova.mjs` passa tutto: nessuno scorrimento orizzontale da 320 a 2560 px, tutti i `tel:` alti almeno 48 px, menu, testata, modulo e "Copia il testo". Nessun U+2014.
- `segnali.sh` a 1440 dà due famiglie con ruoli fissi (Asap 91 %, Big Shoulders 9 %), nessun carattere delle liste b, nessun monospazio e nessuno schema "titolo a sinistra e paragrafo a destra" (prima erano cinque sezioni). Resta bloccante l'area delle foto, al 5,7 %: le uniche foto vere sono due strisce di 939 x 249 che non si ingrandiscono, e il giudice d'identità ha fatto togliere quella di repertorio. Si risolve solo con le foto da rifare (LEGGIMI). Da guardare: i titoli in 700-800. La guida li ammette per il settore delle macchine (c1), e un condensato regge meglio un peso pieno di un peso leggero.

## Cosa trova ciascun visitatore, e dove

**1. Il capo magazzino con il carrello fermo, al telefono (390 x 844).** Senza scorrere vede il logo e "Assistenza carrelli elevatori, Padova", poi "Carrello fermo?" e il bottone rosso "Chiamate l'officina 049 8792361 r.a." (da 193 a 284 px). Sotto ci sono lo stato di oggi e gli orari, le 24 ore, la zona, marche e tipi, i carrelli sostitutivi, l'indirizzo e l'email. Più in basso, il bottone "Scrivete all'officina: carrello fermo" (a circa 640 px) e la sede vera. Scorrendo, "Chiama" resta in testata.

**2. L'impiegato acquisti, al computer (1440 x 900).** Nella prima schermata trova "Ricambi: Originali e di altre marche, gomme e batterie" e il menu. Con un clic arriva a "Qualsiasi ricambio, anche uscito di produzione", al blocco "Magazzino ricambi" (numero, via Canada 12, orari) e alla richiesta già composta, con "Prepara l'email" e "Copia il testo".

**3. Il responsabile di stabilimento o l'RSPP, al computer.** Nella prima schermata ha marche, tipi, zona, orari e Cami2 in testata. Con un clic arriva a manutenzione e controlli: il contratto, il registro, funi e catene, la formazione carrellisti, il preventivo per email o per telefono e "Cambiate assistenza?". Chi siamo spiega in una riga il rapporto con Cami2. La riga di vendita porta a cami2.it, la porta accanto.

## Idea

Il sito serve a far chiamare, e quindi il protagonista è il numero. A 1440 "049 8792361" è composto a 172 px in Big Shoulders Display 800, in rosso, ed è il link di chiamata. Sul telefono lo stesso numero diventa il bottone. È la scelta d'impaginazione che manca nelle altre home della campagna: la scala tipografica è costruita su un recapito, non su un titolo. Le due foto vere, strisce panoramiche di 939 x 249, toccano i due bordi opposti, a misura d'origine: la sede in apertura arriva al bordo destro, la squadra in chiusura parte dal sinistro.

Niente legende numerate, niente carrello scontornato, niente promemoria .ics, niente numeri del gruppo, nessuna foto di repertorio.

## Colori

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
