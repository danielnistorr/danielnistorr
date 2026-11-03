# Oby Group Italia, nuova home: nota

## Livello professionale (3 novembre), con il ritocco finale

Il committente: "ancora troppo poco professionale e di design, e design funzionale all'attività"; sulle foto: "niente". La home è stata rifatta regola per regola su `_metodo/professionale/REGOLE.md` (sezione C) con la struttura della famiglia S (servizi tecnici e imprese, sezione A1), confrontata con le prime schermate di tutti i 14 riferimenti e con le pagine intere di Kline ed Eggentaler guardate a pezzi. Poi un controllore del livello (voto 6 su 10, 7 regole su 15 non passate) e tre clienti tipo (danneggiato al telefono 7, ufficio sinistri 7, tecnico d'azienda) l'hanno provata contro la versione 1 con l'uso; questo ritocco finale corregge i loro difetti. La versione 1 con l'uso è copiata in `_prova/versione-1-uso/`; la pagina prima del ritocco in `_prova/script/finale-pagina-pro1.html`. Le sezioni più in basso sono storico.

Si rifà tutto con `sh _prova/script/build_finale.sh` (immagini con `finale_img_pro.py`, pagina da `finale-pagina.html`). Controlli: `node _prova/script/pro_controlli.mjs` (15 regole, scorrimento, sovrapposizioni, testo tagliato a 320, 390, 768, 1024, 1440; esito in `_prova/tmp-pro/controlli.json`), `node _prova/script/pro2_compiti.mjs <url>` (posizioni dei compiti dei clienti, barra in basso toccabile a 25, 50 e 75 %), `node _prova/script/pro2_barra.mjs <url>`. Screenshot: `home-1440.jpg` (8282 px, prima 8955), `home-1440-prima-schermata.jpg`, `home-390.jpg` (14731 px, prima 15886), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Guardati a pezzi a 320, 390, 768, 1024 e 1440.

**Cosa resta della versione 1:** il titolo "Eliminiamo ogni traccia del danno", Onest come unica famiglia (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL.txt`, servita dalla pagina), il rosso e il nero del logo, le loro parole (claim, otto punti, nove passaggi, 14 interventi, frasi di Starflex), i compiti della scheda d'uso: cellulare e uffici come bottoni nella prima schermata, "Manda le foto del danno" in mailto con oggetto, quattro tacche al telefono, tre porte (danno, compagnie, industria), la barra in basso "Cellulare / Uffici" al telefono, elenco industriale completo, Starflex con PDF, dati societari in chiaro.

**Ordine della pagina:** testata fissa · apertura (bianco) · pronto intervento (rosso) · interventi dopo un danno (bianco) · aziende e industria (nero) · Copertura Sicura Starflex (bianco) · azienda (nero) · contatti e modulo (grigio) · piede (nero).

**Cosa ha cambiato il ritocco finale**
- *Apertura.* La prova è tre fatti in 18 px nero con il filetto rosso: "Personale interno" (brochure 2026: "Personale esclusivamente interno"), "Civile e industriale" (loro otto punti), "Attrezzature e robot ATEX" (pagina Pronto intervento); prima era "14 tipi di intervento" in 15 px grigio. Tolto "Chiedi un sopralluogo" (si arriva al modulo dalle schede); "Manda le foto del danno: si apre la mail già pronta" e "Altro cellulare 393 911 4656" stanno su una riga a 1440, alti 48 px. "Longare (VI)" resta nell'occhiello, il paragrafo dice "Lavoriamo in Veneto e fuori regione". In apertura c'è il tetto bruciato con due operatori al lavoro (persone e mestiere), il condominio è sceso nel pronto intervento.
- *Pronto intervento subito dopo l'apertura* (titolo a y 1701 a 390, prima 3394; a 1440 nella seconda schermata) con quattro passi "Dopo la chiamata", fatti con le loro frasi: ci chiami o ci mandi le foto (indirizzo, tipo di danno, compagnia e numero del sinistro), sopralluogo e messa in sicurezza in tempi brevi, alle pratiche pensiamo noi, ripristino a nuovo; poi i nove passaggi e i bottoni "Chiama il cellulare" e "Manda le foto per mail". Nessun tempo in ore. La fascia delle tre garanzie è stata tolta: il suo contenuto è in questi passi.
- *Barra di chiamata in basso al telefono e al tablet* (fino a 900 px), come nella versione 1: "Cellulare 340 834 9597" pieno e "Uffici 0444 1329022" a bordo, 56 px, compare quando i bottoni dell'apertura escono dallo schermo; provata toccabile a 25, 50 e 75 % della pagina.
- *Industria su fondo nero:* sei schede con la descrizione (bonifiche industriali, ambienti confinati, fune, sabbiature, smaltimento rifiuti con la riga del nono passaggio, demolizioni e opere edili) a tre colonne e l'indice delle altre sei a righe con numero, nome e freccia, tutte cliccabili e con il tipo già scelto nel modulo; tolte le sette scatole con il solo titolo e il `min-height`. Al telefono le schede diventano righe a filetto: la sezione passa da 3319 a circa 1940 px. I bottoni "Manda capitolato e foto" e "Uffici" sono accanto al titolo. Tolta la foto in fune.
- *Starflex:* bottoni "Affidaci un sinistro" e "Scarica la documentazione tecnica", la riga "Per affidarci un sinistro chiama gli uffici, oppure scrivici con numero del sinistro e perizia" di nuovo in pagina, e sotto la foto "Documenti da scaricare" con documentazione tecnica e brochure di pari peso (formato e peso sotto ciascuno), aperti in una nuova scheda. Col menu "Starflex" a 1440 il bottone è a y 725-781 e i due documenti a y 691-844.
- *Azienda:* titolo e testo a sinistra, dati societari a destra in cima alla sezione (col menu "Azienda" la tabella è a y 112-521 a 1440); tolta la fascia "In numeri"; quattro qualifiche: personale interno, membrana STARFLEX® di MPM, attrezzature ATEX, documenti su richiesta.
- *Arrivi dai link interni:* le ancore sono sul contenuto e non sul bordo della sezione, quindi niente più fascia vuota sotto la testata.
- *Piede e modulo:* Privacy e Cookie puntano alle pagine del sito di oggi (`privacy-policy-obygroupitalia`, `cookie-policy`), che esistono; gli stili scritti dentro gli elementi sono passati nel foglio di stile; il grigio dei campi è un token.
- *Tacche* al telefono a filetto con la freccia, come le porte, non più un terzo tipo di bottone. *Porte* con la freccia rossa e il filetto che diventa rosso al passaggio del mouse.
- *Foto:* stesso trattamento per tutte e tre (livelli con taglio dell'1 % di ombre e luci, colore all'80 %, contrasto +4 %); il tetto bruciato non supera più la sua misura al tablet (al massimo 522 px).

**Esito delle 15 regole** (misure di `pro_controlli.mjs` a 1440x900 e 390x844, salvo dove è detto):

| # | Regola | Esito | Misura o motivo |
|---|---|---|---|
| 1 | Telefono bottone in testata fissa | passa | testata fissa (88 px a 1440, 72 a 390); a 1440 "Uffici" a bordo e "Cellulare" pieno, a 390 il cellulare in testata e in più la barra in basso con cellulare e uffici; a metà pagina bottoni visibili e toccabili; 18 link `tel:` |
| 2 | Prima schermata: mestiere, luogo, prova, azione | passa | occhiello "Bonifiche e ripristino dopo un sinistro · Longare (VI)"; prova "Personale interno · Civile e industriale · Attrezzature e robot ATEX" in 18 px nero (a 390 y 680-731); bottone del cellulare con il numero (fondo a y 588 a 1440, a y 497 a 390, largo 347 px). Una cifra forte (anno, iscrizione all'Albo) manca nelle fonti: chiesta nel LEGGIMI |
| 3 | Immagine vera in apertura | passa | il tetto bruciato con due operatori al lavoro, loro foto (519 px su 522 a 1440); a 390 sotto i bottoni, come chiede la scheda d'uso |
| 4 | Zero repertorio | passa | `indicativ` 0, nessuna immagine da banche; uscita anche la foto in fune di provenienza incerta |
| 5 | Foto in serie | passa in parte | 3 foto, un formato (1:1), 0 didascalie, un trattamento comune che avvicina i colori; la luce resta diversa (scatti da telefono): serve la giornata di fotografia del LEGGIMI |
| 6 | Palette dal marchio | passa | rosso #E41D25 e nero #231F20 del logo (più il rosso scuro del passaggio del mouse) e 8 grigi neutri; fondo bianco, niente `--carta` |
| 7 | Scala corta e leggibile | passa | 8 misure a 1440 (120, 76, 48, 24, 20, 18, 15, 14) e 8 a 390 (48,8, 40, 30, 21, 18, 17, 15, 14); testo corrente 18 e 17 px; 14 px solo nelle note legali; titolo 76 px a 1440 e 40 a 390, interlinea 1,04 |
| 8 | Due famiglie al massimo | passa | una sola, Onest, in 400 e 700 |
| 9 | Servizi in schede con foto | passa in parte | griglie a 4 colonne (danni) e 3 colonne (industria), passo 24 px, ogni scheda è un link intero con numero, nome, descrizione e azione, più l'indice di sei righe cliccabili; **senza foto** per la decisione "niente" e perché le foto dei singoli lavori non esistono |
| 10 | Almeno tre tipi di prova | non passa (1 su 4) | fascia personale, fornitori e qualifiche con didascalia; tolti i numeri di riempimento; recensioni, numeri aziendali veri e clienti con il nome non sono nelle fonti: chiesti nel LEGGIMI (punti 2, 3 e 8) |
| 11 | Lavori con un nome | non passa | nessun lavoro con cliente, luogo, anno e dati nelle fonti; non si inventa. Chiesti tre casi con il permesso del cliente |
| 12 | Ritmo a blocchi | passa | 3 sezioni a colore pieno oltre al piede (pronto nel rosso, industria e azienda nel nero) più i contatti in grigio; spazio tra le sezioni 120 px a 1440 e 64 a 390; margini 80 e 22 px |
| 13 | Un solo sistema di bottoni | passa | pieno rosso e a bordo, raggio 6 px, altezze 52 e 56 a 1440, 48 e 56 a 390, testo 18 e 17 px; i bottoni di chiamata contengono il numero; le tacche ora sono righe a filetto |
| 14 | Modulo e "dove" per il mestiere | passa in parte | modulo con tipo di intervento (17 voci), indirizzo, urgenza, compagnia e sinistro, foto (casella: si allegano alla mail), compone una mail con oggetto; nessun iframe; l'elenco dei comuni serviti non è nelle fonti (chiesto, con le cinque regioni della brochure 2022 da confermare) |
| 15 | Piede completo | passa in parte | 4 colonne, testo 15 px (14 la riga legale), ragione sociale, P.IVA, REA, indirizzo con mappa, telefoni ed email cliccabili, zona, Privacy e Cookie verso pagine che esistono; mancano orari e certificazioni (non pubblicati, chiesti) |

**Difetti segnalati e respinti, con il motivo**
- Comuni o regioni servite in pagina: l'unica traccia sono le sedi operative della brochure 2022, forse superate; non vanno a vista senza conferma (LEGGIMI, punto 5).
- "8 dipendenti" (atoka) come numero aziendale e "iscrizione categoria 4 / 5" (brochure 2022) come certificazione: dati da registri o da una brochure vecchia, non confermati dall'azienda; chiesti nel LEGGIMI (punti 3 e 8).
- "Parliamo con perito o liquidatore" nei passi dopo la chiamata (cliente tipo 1): nelle fonti c'è solo "pensiamo noi alle pratiche"; il passo dice questo.
- Voce di menu "Per le compagnie" al posto di "Starflex" (cliente tipo 2, minore): "Starflex" funziona già nel compito e la porta "Compagnie assicurative" è nella prima schermata, ora con la freccia.
- Foto in fune come prova del cantiere industriale (scheda d'uso, tecnico d'azienda): non è certo che sia loro; resta solo il tetto bruciato con gli operatori in quota. Torna se l'azienda la conferma.

**Compiti dei clienti tipo dopo il ritocco** (`pro2_compiti.mjs`): al telefono cellulare e uffici sopra la piega (bottoni a y 441-561), foto per mail a y 567-618, "allagamento" e "Longare (VI)" entro y 419, la tacca Allagamento porta la scheda a y 92-329, "Cosa succede quando ci chiami" a y 1701 (prima 3394), la barra in basso con cellulare e uffici toccabile mentre si scorre (come nella versione 1); a 1440 Starflex in un clic con documentazione tecnica e brochure nella finestra d'arrivo, dati societari nella finestra d'arrivo di "Azienda" senza numeri davanti, "30 anni" solo nella tabella Starflex attribuito a MPM; Ctrl+F trova escavatori a risucchio, serbatoi, ambienti confinati, ATEX, fune, reti gas; ogni scheda e riga dell'indice apre il modulo con il tipo scelto. Nessuna "esclusiva", nessun "24 ore".

**Controlli generali:** nessuno scorrimento orizzontale a 320, 390, 768, 1024 e 1440; nessuna sovrapposizione e nessun testo tagliato; nessun U+2014 nella pagina, negli script, in questa nota e nel LEGGIMI. Altezze: 320 px 15607, 390 px 14731, 768 px 12123, 1024 px 8880, 1440 px 8282.

---

## Storico

Versione finale della direzione A, "Ogni traccia", rifinita dopo il giudizio cieco (50/80, non passava). Pagina statica in `sito/index.html` (si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`. Tutto si rifà con `sh _prova/script/build_finale.sh` (immagini con `finale_img.py`, pagina da `finale-pagina.html`, screenshot; `finale_chiusura.mjs` per la chiusura, `finale_prova_gesto.mjs` per provare il gesto con tastiera, mouse e dito, i link e la misura delle tacche). Le modifiche di questo giro sono scritte in `rifinitura_pagina.py`, che parte dalla copia `finale-pagina-prima-del-giudizio.html`.

Screenshot: `home-1440.jpg` (8001 px compreso il piede; prima del giro "con l'uso" 5663), `home-1440-prima-schermata.jpg`, `home-390.jpg` (10541 px; prima 6631), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. La versione 1 com'era prima del giro qui sotto è copiata in `_prova/versione-1-originale/` (pagina, immagini, caratteri, screenshot e `finale-pagina.html`).

## Versione 1 con l'uso (2 novembre)

Il committente, viste le due versioni, ha scelto questa ("no preferisco versione 1"), con l'uso. Restano la grafica, Onest come unica famiglia, i colori gesso, inchiostro e rosso, la griglia a 12 colonne, l'immagine d'apertura (la copertura piana STARFLEX), il titolo "Eliminiamo ogni traccia del danno" con il suo peso 300 e l'idea del bianco del lavoro finito. La versione 2 (`sito-v2/`) è servita solo come elenco di cosa deve trovare chi apre il sito (`_prova/uso/SCHEDA.md`); del suo aspetto non è stato ripreso niente (Big Shoulders, Atkinson, campo rosso, apertura a tre colonne). Tutti i pezzi nuovi usano gli stili che la pagina aveva già: il bottone rosso e quello a bordo, i filetti dell'elenco, l'occhiello in 600, le didascalie in cenere, i link sottolineati a 1 px.

Il giro è stato fatto due volte. Il primo ha aggiunto bottoni, porte, barra e voci industriali; poi tre clienti tipo (danneggiato da telefono, ufficio sinistri, tecnico d'azienda) hanno provato la pagina accanto alla versione 2 e le hanno dato 5 su 10 (la v2 9): falliti "capire se fanno il mio danno e dove arrivano", "cosa succede dopo e chi segue le pratiche", "capire Starflex in un minuto". Il secondo giro, qui sotto, corregge quei compiti. Copia del primo giro: `_prova/script/finale-pagina-uso1-giro1.html`.

**Cosa trova ora ogni visitatore**

1. *Il danneggiato, da telefono (390x844), senza scorrere:* il titolo (y 64-244), subito sotto la riga che dice cosa e dove, "Incendi, allagamenti, grandine e maltempo, amianto: in case, condomini, negozi e capannoni. Mettiamo in sicurezza, puliamo e ricostruiamo, e alle pratiche burocratiche pensiamo noi. Da Longare (VI), in Veneto e fuori regione." (y 244-397); il bottone rosso "Chiama il cellulare 340 834 9597" (y 417-471), "Chiama gli uffici 0444 1329022" a bordo (y 479-533), "Manda le foto del danno per mail" ora a bordo come un bottone più basso (48 px, y 541-589; oggetto e traccia invariati), "Altro cellulare 393 911 4656" (44 px, y 591-635); poi la copertura STARFLEX nella sua striscia 16:9 (y 651-871, ancora nella prima schermata). Sotto, quattro tacche a filetto Incendio, Allagamento, Grandine e tetti, Amianto (52 px, due colonne), che portano alla voce giusta dell'elenco, e le tre porte. In testata il numero dice "Uffici". La barra fissa in basso ora osserva solo il bottone del cellulare: compare appena esce dallo schermo (da circa 480 px di scorrimento a 390), quindi non c'è più il tratto in cui resta toccabile solo il numero degli uffici. "Nessuna incombenza burocratica, pensiamo noi a tutto" è il titolo del pronto intervento, a y 1479 (seconda schermata). A 320x640 i due bottoni stanno a y 455-571.
2. *Il pronto intervento:* occhiello "Pronto intervento · Cosa succede quando ci chiami", titolo "Nessuna incombenza burocratica, pensiamo noi a tutto", poi il loro claim "Quando il danno diventa serio, noi entriamo in azione" in testa al paragrafo, che dice anche "Seguiamo noi le pratiche burocratiche; se il danno è assicurato, dicci la compagnia e il numero del sinistro". I nove passaggi sono un elenco numerato tutto in vista, numeri 01-09 in rosso e filetti come l'elenco degli interventi (due colonne a computer, una al telefono): niente più righello da toccare. La cucina "Foto indicativa" viene dopo l'elenco.
3. *L'ufficio sinistri, da computer (1440x900):* la testata ora resta fissa in cima (stesso gesso, filetto sotto appena si scorre), con il menu e "Uffici 0444 1329022" sempre lì. Il salto "Copertura Starflex" mostra in una finestra: il paragrafo riscritto con le parole della brochure ("posata sopra la guaina esistente. Per la compagnia: risarcimenti più bassi e chiusura dei sinistri più veloce"), una tabella a filetti di cinque righe (Guaina, Smaltimento, Posa a freddo senza fiamme libere, Supporto anche umido o bagnato con STARFLEX HYBRID, Durata 30 anni dichiarati da MPM per STARFLEX ULTRA), il bottone a bordo "Scarica la documentazione tecnica" con "PDF, 10 pagine, giugno 2026, 2,8 MB" (y 527-579), la brochure, la richiesta di visura e abilitazioni. A sinistra, sotto il titolo, "Per affidarci un sinistro chiama gli uffici... oppure scrivici per mail". Tolto "in tempi rapidissimi". Sotto la foto, "Meno costi oggi. Meno sinistri domani." (loro, brochure 2026) e "Affidaci un sinistro per mail".
4. *Il perito o il tecnico che verifica l'impresa:* il salto "Azienda" arriva su una tabella con ragione sociale, P.IVA e CF, REA, sede operativa con mappa, sede legale, uffici, mail e "Documenti: Chiedi visura, iscrizioni e abilitazioni per mail" (mailto con oggetto "Richiesta documenti dell'impresa" e una traccia che nomina Albo gestori ambientali e categorie, amianto, ATEX, ambienti confinati, lavori in fune). Le abilitazioni non sono scritte come possedute. Il titolo della sezione ora è la loro frase "Ripristiniamo a nuovo e tutto torna come prima". Nei contatti "Sede" è diventato "Sede operativa".
5. *Il tecnico d'azienda:* nel menu c'è "Industria" (salto sull'etichetta del gruppo); l'etichetta "Aziende e industria" ha la misura di un titolo (24 px, 600) e non sembra più la coda dei danni. Accanto alle due foto vere una riga su attrezzature e robot certificati ATEX ed escavatori a risucchio e la stessa richiesta di visura, iscrizioni e abilitazioni.

**Altri ritocchi:** "Bonifiche post alluvione" diventa "Bonifiche dopo allagamenti e alluvioni" (anche nel piede); la voce "Danni da eventi atmosferici" nomina grandine e maltempo e rimanda a Starflex per i tetti; "una squadra di tecnici è sempre pronta a intervenire" diventa "interviene in tempi brevi"; nel piede "Starflex (PDF)" diventa "Documentazione tecnica Starflex (PDF)"; tra 901 e 1100 px la voce di menu si accorcia in "Starflex" per stare su una riga.

**Respinto, con il motivo**
- Il claim "Quando il danno diventa serio, noi entriamo in azione" al posto del titolo, in peso 600: il committente ha scelto la versione 1 con il suo titolo. Il claim apre il paragrafo del pronto intervento, nella seconda schermata.
- Sostituire la copertura STARFLEX d'apertura con il condominio ponteggiato o il tetto bruciato, e lasciarla solo nella sezione Starflex: è l'immagine principale scelta. Al telefono è solo scesa sotto i bottoni, sempre nella prima schermata; a computer è dov'era.
- Togliere la cucina e la stanza Pexels o metterci le foto vere piccole: sono grafica della versione scelta, già dichiarate "Foto indicativa"; il tetto bruciato (567 px) e il locale allagato (850 px) non reggono le fasce 21:9 e 5:4. La cucina è scesa sotto l'elenco dei passaggi. Restano tra le foto da rifare.
- Una riga di descrizione per le voci industriali che hanno solo il titolo: nei loro testi non c'è, e non si scrive al posto loro.
- Stato "aperto ora / chiuso ora", orari, "24 ore su 24": niente di pubblicato.

**Controlli** (`node _prova/script/uso1_prova.mjs <url> <cartella>` e `node _prova/script/uso2_misure.mjs <url> <cartella>`)
- Nessuno scorrimento orizzontale a 320, 360, 390, 414, 640, 641, 768, 900, 901, 1024, 1100, 1280, 1440, 1920. Schermate guardate a pezzi a 390 e 1440 (pagina intera, `home-390.jpg` 10541 px, `home-1440.jpg` 8001 px) e a 320, 768, 1024: nessuna sovrapposizione, menu su una riga da 901 a 1920.
- Salti con la testata fissa (1440): Starflex col bottone del PDF a y 527-579, Azienda con la tabella a y 439-798, Industria sull'etichetta a y 140, Pronto intervento sul titolo a y 139; testata alta 96 px. Le quattro tacche al telefono portano la voce a y 24.
- Link: 8 `tel:+3904441329022`, 4 `tel:+393408349597`, 3 `tel:+393939114656`; mailto con oggetto e traccia per le foto del danno (2), la richiesta d'intervento (2), l'incarico da compagnia (2), la richiesta di documenti (3); 3 mailto semplici; 3 link a Google Maps; i due PDF locali (2 link ciascuno). Nessuna ancora senza destinazione.
- Ctrl+F: escavatori a risucchio, serbatoi, ambienti confinati, ATEX, fune, reti gas, il claim, "pensiamo noi a tutto", P.IVA, Longare, guaina, a freddo, condomini, Veneto. Assenti: "esclusiva", "24 ore", "Fig.", "certificata", "rapidissimi", "sempre pronta". Nessun U+2014 in pagina, negli script, in questa nota e nel LEGGIMI.
- Nessuna immagine nuova, nessun JavaScript per i passaggi (la pagina usa script solo per il menu, il filetto della testata e la barra; senza JavaScript la barra resta visibile). `finale_prova_gesto.mjs` provava il righello e non vale più.
- Carattere invariato: Onest, Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL.txt`), servito dalla pagina.
- Le sezioni qui sotto descrivono la versione 1 di partenza; dove parlano del righello, di "Fig.", di "30 anni di durabilità certificata", di "nasce nel 2018", del bottone "Chiama lo 0444 1329022" o delle foto della tabella, vale quanto scritto in questa sezione.

## Idea

Il bianco del lavoro finito. La pagina è chiara e ordinata come un ambiente dopo l'intervento, e la prima cosa che si vede è un lavoro loro: la copertura piana rivestita di bianco con la membrana STARFLEX, con il torrino e il parapetto rivestiti, presa dal loro sito. Sopra c'è il titolo "Eliminiamo ogni traccia del danno". Con il nome di un'impresa di bonifica qualsiasi la prima schermata non regge più: la copertura Starflex è il servizio su cui Oby punta dal 2026. Poi la pagina racconta il percorso: il danno (la cucina bruciata) e i nove passaggi del loro pronto intervento, le aree, Starflex, l'azienda, e in chiusura la stanza rifatta con la loro frase "Ti riconsegnamo il tuo bene nelle condizioni originarie".

## Cosa è cambiato dopo il giudizio cieco

- **Apertura rifatta.** Via il respiratore Pexels e i tre richiami a punto e filetto (gesto già visto in altre home della campagna, e non leggevano l'oggetto). Ora il titolo sta sul gesso, su due righe a 108 px; sotto ci sono la riga sui sinistri (incendio, allagamento, grandine, bonifica industriale) e il bottone rosso. Più sotto la copertura Starflex è a tutta larghezza, alta fino al bordo dello schermo, con la didascalia "Fig. 1". Non c'è più il muro grigio #CBCAC5 con lo stacco a y=900: la foto è un rettangolo netto e voluto, e la membrana è il punto più chiaro della pagina. Non ci sono più il logo sul cappuccio a 1024 né la testata sopra la foto.
- **Niente prima e dopo finto.** Il cursore con due ambienti diversi è stato tolto. Pronto intervento ha una sola foto, la cucina dopo un incendio in fascia 21:9 ("il punto da cui si parte"), e sotto il righello dei nove passaggi. La stanza rifatta è passata in chiusura.
- **Chiusura senza tuta né maschera.** Ora c'è la stanza rifatta, pareti bianche e porta finestra, a filo del bordo destro: è quello che la frase promette.
- **Starflex asciugata.** Restano il titolo, il paragrafo, la foto (ora il fibrocemento rivestito accanto al fotovoltaico, l'altra foto Starflex del loro sito, in 5:2) e una sola riga, "30 anni di durabilità certificata per STARFLEX® ULTRA", con il PDF. Le due liste sono passate alla pagina /copertura-sicura-starflex/. Il "30" grande non c'è più.
- **Azienda senza i quattro "fatti".** Restano il titolo e il paragrafo, sfalsato sotto il titolo dalla colonna 7.
- **Un solo registro, il tu**, come nei loro testi: "Chiama lo 0444 1329022", "Cosa succede quando ci chiami", "tocca un numero o scorri il righello".
- **Piede:** ogni voce della colonna Interventi punta alla sua riga (#danni-post-incendio e così via). Privacy e Cookie puntano a /privacy-policy/ e /cookie-policy/.
- **Tacche** alte 48 px a ogni larghezza (a 390 misurano 39x48).
- **Titoli** con `text-wrap: balance`: niente parole sole a fine riga.

## Le prime due schermate

1. **Apertura.** A 1440 si vedono la testata sul gesso (logo, menu, "Uffici 0444 1329022"), il titolo in Onest 300 a 108 px su due righe, il paragrafo a sinistra e il bottone rosso a destra, e da y=504 la copertura a tutta larghezza fino al bordo dello schermo (altezza `100vh - 280px`, minimo 420 px). A 1920 la foto è alta 720 px e il testo resta sulla griglia di 1440. A 390, nei primi 844 px, ci sono la testata con il telefono e un vero bottone Menu, il titolo su tre righe ("Eliminiamo / ogni traccia / del danno"), la copertura in un taglio quadrato centrato sul torrino, la didascalia e il bottone rosso. Tra 641 e 900 px il paragrafo e il bottone vanno uno sotto l'altro.
2. **"Cosa succede quando ci chiami".** Titolo e due righe su 6 colonne, poi la cucina bruciata larga quanto la griglia, poi il righello 01-09 a cifre tabellari. La tacca attiva è rossa e sotto c'è il nome del passaggio. La pagina si apre sul passaggio 01, "Sopralluogo e consulenza nell'immediato".

Poi vengono:
- **Interventi.** Le nove aree vere in una lista a filetti, ognuna con il suo id.
- **Copertura Sicura Starflex.** Titolo a sinistra e paragrafo a destra, la foto a tutta larghezza, una riga e il PDF.
- **Azienda.**
- **Chiusura "b con foto".** Testo a sinistra e stanza rifatta a destra fino al bordo.
- **Piede.**

Un solo fondo per tutta la pagina; il gesso scuro compare solo nel piede.

## Caratteri e colori

- **Onest** (Google Fonts, SIL Open Font License 1.1; licenza in `sito/fonts/OFL.txt`) è l'unica famiglia. È variabile 100-900 e viene servita dalla pagina (`sito/fonts/onest-latin.woff2`, `onest-latin-ext.woff2`). Titoli in 300-340 con spaziatura da -0,03 a -0,045em, testo in 400, etichette in 600, cifre tabellari su tutta la pagina (`tabular-nums`) per telefoni, tacche e "30 anni". Il riferimento sono i titoli enormi di poche parole di Petzl e il registro calmo, in prima persona, di Gasparoli. Onest è un grottesco neutro con curve morbide: serio senza allarme, e non sta nelle liste b della guida. Geist, proposto nell'analisi, è stato scartato perché è il carattere di serie di Next.js e v0.
- **Colori:**
  - gesso #F4F3F0 (fondo) e gesso scuro #EBE9E4 (solo piede);
  - inchiostro #1D1C1B, dal nero del logo #231F20;
  - cenere #64615B per i testi secondari e le tacche non ancora fatte (5,6:1 sul gesso);
  - rosso #C8161D per bottone, telefoni e tacca attiva: è il rosso del logo #E41D25 scurito quanto basta per l'AA con il bianco (5,8:1). Il rosso pieno resta solo nel logo.
  - Il legno di B è stato tolto: un colore d'accento in meno. Nella prima schermata gli unici colori forti sono il rosso del bottone e del logo.
- **Trattamento unico delle foto** (PIL, `finale_img.py`): saturazione da -10 a -20 %, nero sollevato a 16, un velo del 3 % verso il gesso. Le due coperture hanno in più una piccola correzione della dominante blu del cielo; quella dell'apertura ha anche una curva che apre solo i toni alti, così la membrana resta bianca senza bruciare. La cucina ha una schiarita leggera. Ogni foto è esportata in due o tre larghezze con srcset, e al telefono con tagli suoi.

## Interazione

Una sola: il righello dei nove passaggi del loro pronto intervento. Le nove tacche sono veri bottoni in un gruppo con tabindex mobile: un solo tasto Tab per entrare e uscire, le frecce spostano il passaggio e il fuoco, Home e Fine vanno al primo e all'ultimo. Si può toccare una tacca, oppure trascinare il dito o il mouse lungo il righello (pointer events, `touch-action: pan-y`, così la pagina continua a scorrere in verticale). Il nome del passaggio è in un'area `aria-live`, e ogni tacca ha un `aria-label` con il suo passaggio e `aria-current="step"` su quella attiva. Le transizioni riguardano solo il colore delle tacche (.12 s) e il fondo del bottone rosso. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto che segue il cursore, nessuna dissolvenza.

## Foto: origine e licenza

| In pagina | File sorgente | Origine | Licenza |
|---|---|---|---|
| Apertura (1440 e telefono) | `assets/originali/9e96e5_520d02be…webp` | sito di Oby (forse foto di MPM) | da confermare con l'azienda |
| Pronto intervento, cucina ("Foto indicativa") | `assets/esterne/pexels-10252682.jpg` | F. Hektor, Pexels | Licenza Pexels, uso commerciale libero |
| Starflex | `assets/originali/9e96e5_c7d17813…webp` | sito di Oby (forse foto di MPM) | da confermare con l'azienda |
| Chiusura, stanza rifatta ("Foto indicativa") | `assets/esterne/pexels-7031621.jpg` | Max Vakhtbovych, Pexels | Licenza Pexels |
| Industria, fune su pala eolica (dal 2 novembre) | `assets/originali/9e96e5_4e684abe…jpg` | sito di Oby | da confermare che sia un loro lavoro |
| Industria, cunicolo (dal 2 novembre) | `assets/originali/9e96e5_ec8a1c18…jpg` | sito di Oby | da confermare; tagliato sotto il logo della tuta |

Tutte sono già in `assets/CREDITI.md`, con la licenza Pexels verificata sulla pagina della foto. Non ne è stata scaricata nessuna nuova, e nessuna compare nei CREDITI delle altre home della campagna (controllato il 24/10/2026). Nessuna è generata dall'IA e nessuna ha marchi in primo piano. La copertura dell'apertura è tagliata sotto le torri, così l'insegna sul fondo non entra a nessuna larghezza. Nella pagina non c'è più nessuna persona di repertorio. Le foto da rifare dal vero sono nel LEGGIMI.

## Piede

- Logo vettoriale vero (`sito/img/logo-obygroup.svg`, estratto senza ridisegnarlo dalla brochure Starflex 2026) con una riga su chi sono.
- Colonna Azienda: Chi siamo, Pronto intervento, Copertura Starflex, Brochure PDF.
- Colonna Interventi: le nove aree vere, ognuna con il link alla sua riga della lista; su due colonne a 390.
- Colonna Contatti: "Uffici" sopra il telefono in rosso semibold, poi cellulari, email, sede operativa con link alla mappa, sede legale. Tutto è cliccabile.
- Colonna Seguici: solo Facebook, l'unico social trovato.
- Riga legale: ragione sociale, P.IVA e CF, REA, capitale sociale, Privacy (/privacy-policy/) e Cookie (/cookie-policy/).
- A 390 le colonne si impilano in ordine.
- **Niente newsletter:** è un servizio d'emergenza su chiamata e non ha novità periodiche da comunicare. Per le assicurazioni basta il PDF di Starflex.

## Controlli (dopo la rifinitura)

- `segnali.sh` (kit): 0 soglie bloccanti su 10. Foto al 35,8 %, Onest al 100 %, mono 0 %, 11 filetti, 0 frecce, 0 etichette maiuscole, 0 numeri grandi con etichetta, 2 fasce di fondo, una data (2018). Prima della correzione la soglia "titolo a sinistra e paragrafo a destra" segnava due sezioni: Azienda ora ha il paragrafo sotto il titolo, e resta solo Starflex. Due righe da guardare, con il loro motivo:
  - gli H2 hanno due misure (60 e 56 px), perché la pagina punta sul titolo d'apertura da 108 px e sulla foto;
  - c'è una numerazione 01-09, perché sono i nove passi in ordine del loro pronto intervento.
- **Larghezze guardate a pezzi:** 1440, 390, 320, 768, 1024 (prima schermata), 1920. scrollWidth è uguale a innerWidth a 320, 360, 390, 414, 640, 641, 768, 900, 901, 1024, 1100, 1280, 1440, 1680, 1920 e 2560. Nessuna sovrapposizione. A 768 il bottone non va più a capo (`white-space: nowrap`, sotto il paragrafo).
- **Gesto, provato con Playwright** (`finale_prova_gesto.mjs`):
  - a 1440: freccia destra due volte (02, 03), freccia sinistra (02), Fine (09), Home (01), Tab che esce dal righello verso il link del PDF, clic sulla tacca 03, trascinamento dal 5 al 62 % (06); il contorno rosso di 2 px è visibile al fuoco da tastiera;
  - a 390, al tocco: Menu che si apre e si chiude sul link, tacca 09, tacca 05; tacche di 39x48 px.
- **Link:** `tel:+3904441329022`, `tel:+393408349597`, `tel:+393939114656`, `mailto:info@obygroupitalia.com`, due link a Google Maps per via Ghizzole 41, Longare. Nessuna ancora senza destinazione; l'unico `href="#"` è il logo che riporta in cima.
- Nessun U+2014 in pagina, negli script, nella NOTA, nel LEGGIMI e nei CREDITI. Nessun segnaposto in pagina. Ogni fatto viene da `01-analisi.md`.
- **Contrasto AA sui testi:** la cenere sul gesso fa 5,6:1, il grigio del piede #55524D sul gesso scuro 6,4:1, il bianco sul rosso 5,8:1.
- **Peso:** `sito/` pesa 3,8 MB, con 20 immagini JPEG più il logo SVG, tutte usate dalla pagina. La foto d'apertura a 1440 pesa 330 KB: è la texture della membrana, che sotto quella qualità si impasta.
