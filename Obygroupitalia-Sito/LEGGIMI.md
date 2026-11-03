# Oby Group Italia: proposta di nuova home

Proposta non richiesta di una nuova homepage, solo la home, per OBY GROUP ITALIA Srl (www.obygroupitalia.com). Non è pubblicata e l'azienda non è stata contattata.

**Pagina da consegnare: `sito/index.html`, metodo ibrido (3 novembre 2026).** Prima schermata secondo la sezione D di `_metodo/professionale/ALTO-LIVELLO.md` (la frase "Alle pratiche pensiamo noi." su carta, il numero sempre in vista), sotto i contenuti e le funzioni della versione professionale su una griglia sola. La sezione **"Metodo ibrido"** qui sotto vale prima di tutte le altre; la sezione "Livello professionale" resta valida per le domande all'azienda, il modulo e le foto da fare. La versione professionale com'era è in `_prova/versione-pro/` (pagina, immagini, Onest, screenshot).

- Pagina: `sito/index.html`, statica, si apre con file:///. Immagini in `sito/img/` (sei foto vere in WebP con srcset e i due loghi), caratteri in `sito/fonts/` con le licenze, i due PDF in `sito/doc/`.
- Direzione: `_prova/alto/DIREZIONE.md`. Screenshot e nota: `screenshot/home/` (`NOTA.md`, sezione "Metodo ibrido", con le misure e i problemi aperti).
- Si rifà con `python3 -I _prova/alto/script/img_ibrido.py` (foto), `node _prova/alto/script/screenshot.mjs` (screenshot) e `node _prova/alto/misura-d.mjs` (misure della sezione D e controlli a 320-1920). La pagina si modifica a mano.
- Analisi con le fonti: `01-analisi.md`.

## Metodo ibrido (3 novembre 2026)

**Caratteri.** Escono Onest e i suoi file. Entrano **Fraunces** 600 per i titoli (SIL Open Font License 1.1, Undercase Type; file "opsz" di @fontsource-variable/fraunces 5.2.9, licenza in `sito/fonts/OFL-fraunces.txt`) e **Atkinson Hyperlegible** 400 e 700 per il testo (SIL OFL 1.1, Braille Institute; @fontsource/atkinson-hyperlegible 5.2.8, licenza in `sito/fonts/OFL-atkinson.txt`). Riga nel registro dei caratteri del metodo.

**Foto.** Gli originali di `assets/originali/` non ci sono più (la cartella contiene solo `CREDITI.md`): le sei foto in pagina sono rifatte dalle versioni lavorate rimaste (`sito-v2/img/` e `_prova/versione-pro/sito/img/`), con un solo trattamento. Vanno richiesti i file originali all'azienda.
- Escono dall'apertura il tetto bruciato visto dall'alto (ora tagliato 16:9 nella serie dei danni) e non c'è più nessuna foto nella prima schermata.
- Entrano, dal loro sito, il locale tecnico allagato, la mansarda con l'infiltrazione e il tetto in fibrocemento (serie dei danni, come nella versione 2): **confermare che sono loro interventi**.
- Il condominio ponteggiato con il telo Oby è la foto del culmine (sezione Azienda): **chiedere comune e anno** per la didascalia, che oggi dice solo "Condominio di undici piani, ponteggio su tutta la facciata / Cantiere Oby Group Italia, con il nostro telo sul ponteggio".
- La foto Starflex è tagliata 16:9 dalla fascia di 1701 px: resta la domanda se è di Oby o di MPM.
- Per l'apertura vera serve la foto degli otto della squadra in divisa davanti alla sede (modello Q pieno): con quella la foto prende il 60% o più della prima schermata e la frase resta sopra.

**Testi nuovi o cambiati, da far rileggere** (oltre a quelli del punto 10 dei dati da confermare):
1. Il titolo d'apertura "Alle pratiche pensiamo noi.", accorciato da "Nessuna incombenza burocratica, pensiamo noi a tutto" e "Adempimento di pratiche burocratiche"; torna come terzo passo dopo la chiamata.
2. La riga d'apertura "Ripristino e bonifiche dopo incendi, allagamenti, grandine e amianto. Da Longare (VI)."
3. "Siamo pronti a intervenire in ogni tipo di scenario" (dal loro "Siamo sempre pronti ad intervenire in ogni tipo di scenario").
4. Le righe dei danni: allagamenti "dall'aspirazione dei liquidi alla sanificazione" (dai nove passaggi) e grandine e maltempo "Infiltrazioni e tetti danneggiati".
5. Le descrizioni brevi dei lavori industriali e i nomi accorciati ("Smaltimento rifiuti pericolosi e non pericolosi", "Demolizioni, barriere tagliafuoco e opere edili").
6. Il testo della sezione Azienda, che unisce "personale esclusivamente interno" (brochure 2026) e "Fin da subito stabiliamo con il cliente un rapporto di fiducia" (sito di oggi).
7. Le quattro strade dei contatti ("Compagnie, periti e amministratori", "Foto del danno", "Aziende e impianti", "Sede operativa a Longare (VI)") e "Se non risponde, l'altro cellulare".

**Cosa non c'è più in pagina:** il peso dei PDF nelle righe dei documenti, l'elenco degli interventi nel piede, le quattro qualifiche della sezione Azienda (il loro contenuto è nel testo e nella sezione Starflex), il campo email e la scelta dell'urgenza nel modulo (restano nome, telefono, tipo, compagnia e sinistro, indirizzo, descrizione).

## Livello professionale (3 novembre)

Il committente ha chiesto una home più professionale e "funzionale all'attività", e sulle foto ha deciso: "niente" (nessuna foto di repertorio, nessuna illustrazione al loro posto). La pagina ha la struttura dei siti di imprese di servizi tecnici scelti dallo studio (Kline, Wilson, Eggentaler): testata fissa con i numeri come bottoni, apertura con mestiere, luogo, tre fatti e due bottoni di chiamata, pronto intervento subito dopo (cosa succede dopo la chiamata e i nove passaggi), interventi in schede, industria su fondo nero, Starflex per le compagnie con i documenti da scaricare, azienda con i dati societari in alto, chiusura con il cellulare in grande e il modulo, piede a quattro colonne. Al telefono, scorrendo, compare in basso la barra con "Cellulare" e "Uffici". Dettaglio ed esito regola per regola in `screenshot/home/NOTA.md`.

**Ritocco finale (stesso giorno), dopo il controllo del livello e la prova dei tre clienti tipo:** tolti la fascia "In numeri" (14 interventi e 9 passaggi contavano voci della pagina, "2 sedi" era riempimento, "30 anni" è un dato di MPM e ora resta solo nella tabella Starflex) e la fascia delle tre garanzie (il loro contenuto è nei quattro passi "Dopo la chiamata"); le dodici voci industriali sono sei schede con la descrizione e un indice delle altre sei; il pronto intervento è salito subito dopo l'apertura; la brochure è un documento da scaricare con lo stesso peso della documentazione tecnica; i link Privacy e Cookie puntano alle pagine del sito di oggi.

**Foto in pagina (solo del loro sito, nessuna di repertorio):** il tetto bruciato con i due operatori (apertura: è l'unica con persone al lavoro e mostra il mestiere), il condominio ponteggiato con il telo Oby (pronto intervento), il fibrocemento rivestito accanto al fotovoltaico (Starflex). Tutte quadrate, con lo stesso trattamento (livelli uguali, colore all'80 %), mai ingrandite oltre la loro misura. Uscite dalla pagina: i tecnici in fune sulla pala eolica (provenienza incerta, qualità bassa: vedi punto 9), la copertura di Milano (forse di MPM), la cucina e la stanza Pexels "Foto indicativa", il cunicolo (logo forse incollato). Le foto Pexels restano in `assets/esterne/` ma non sono usate.

### Il modulo di richiesta va collegato a un servizio

Oggi il modulo in fondo alla home ("Richiesta di sopralluogo o preventivo") **non invia niente**: compone una mail a info@obygroupitalia.com con oggetto ("Richiesta di sopralluogo: <tipo> (urgente)") e tutti i campi nel testo, e apre il programma di posta di chi lo compila. Le schede e le righe degli interventi aprono il modulo con il tipo già scelto. Prima di pubblicare va collegato a un servizio di invio (il modulo del sito nuovo, per esempio Contact Form 7 su WordPress, Formspree o un indirizzo del provider), con:
- invio vero a info@obygroupitalia.com e risposta automatica a chi scrive;
- **caricamento delle foto e dei capitolati** (oggi c'è solo la casella "li allego alla mail che si apre", perché una mail composta dal sito non può portare allegati);
- informativa privacy vera (il link del modulo e del piede punta per ora all'informativa del sito di oggi, `https://www.obygroupitalia.com/privacy-policy-obygroupitalia`, che è copiata da uno studio legale e va rifatta; Cookie punta a `https://www.obygroupitalia.com/cookie-policy`) e protezione dallo spam;
- se l'azienda lo conferma, la promessa dei tempi di risposta accanto al modulo (oggi non c'è perché nessuna fonte la dà).

### Cosa chiedere all'azienda per questa versione

Valgono tutti i punti da confermare delle sezioni sotto. In più, per le regole che oggi non si possono rispettare senza inventare:
1. **Lavori con il nome (regola 11, oggi assente):** tre interventi veri da mostrare, con il permesso del cliente: luogo (comune), anno, tipo di danno e due o tre dati (metri quadri, giorni di lavoro, piani, volumi smaltiti). Per esempio il condominio ponteggiato e il tetto bruciato: dove sono, che lavoro era, quando, cosa dice il telo ("Qui per voi"?).
2. **Recensioni e clienti (regola 10, oggi assenti):** recensioni Google o lettere di clienti con nome e comune; compagnie assicurative, amministratori o aziende che si possono nominare.
3. **Certificazioni e iscrizioni (regola 10 e piede):** Albo gestori ambientali con categorie e numero (la brochure 2022 scrive "Smaltimento rifiuti iscrizione categoria 4 / 5": è ancora valida? con quale numero?), abilitazioni per amianto, ambienti confinati e lavori in fune, eventuali ISO o SOA, con i PDF. Con questi la fascia "Personale, fornitori e qualifiche" diventa una fascia di certificazioni con i loghi e i PDF da scaricare (come Eggentaler), e nel piede va una riga con le iscrizioni.
4. **Orari (piede, oggi assenti) e reperibilità:** orari degli uffici e chi risponde al cellulare fuori orario. Nel piede vanno in una riga "Uffici: lunedì-venerdì ..." sotto Contatti.
5. **Comuni serviti (regola 14, oggi "in Veneto e fuori regione"):** l'unica traccia nelle fonti sono le sedi operative della brochure 2022 (Veneto, Lombardia, Emilia Romagna, Toscana, Friuli Venezia Giulia). Valgono ancora? Con la conferma si fa un elenco di regioni e province a righe nei contatti e nel piede.
6. **La squadra (struttura S, sezione Squadra, oggi assente):** nomi, ruoli e anni di mestiere delle persone che si possono presentare, compresa chi risponde al telefono.
7. **Frasi nostre da far rileggere:** i tre fatti dell'apertura ("Personale interno", "Civile e industriale", "Attrezzature e robot ATEX", presi dalla brochure 2026 e dalla pagina Pronto intervento); i quattro passi "Dopo la chiamata" ("Ci chiami o ci mandi le foto", "Sopralluogo e messa in sicurezza", "Alle pratiche pensiamo noi", "Ripristino a nuovo", con una riga ciascuno fatta con le loro frasi); il titolo della sezione industria; la riga della scheda "Smaltimento rifiuti" (presa dal nono passaggio del pronto intervento); "Scegli il tuo danno: si apre la richiesta di sopralluogo già impostata".
8. **Un dato forte per l'apertura e quattro numeri aziendali (regole 2 e 10):** oggi l'apertura ha tre fatti senza cifre e la pagina non ha una fascia di numeri, perché quelli di prima erano di riempimento. Da chiedere: anno di nascita (2018 o 2011), numero di persone in squadra (atoka dice 8 dipendenti), mezzi speciali (quanti escavatori a risucchio, robot ATEX), interventi l'anno veri. Con la conferma, il dato più forte va per primo tra i fatti dell'apertura e quattro numeri tornano nella sezione Azienda, accanto ai dati societari.
9. **Le foto:** confermare che il tetto bruciato e il condominio sono loro cantieri, e che il fibrocemento Starflex si può usare (Oby o MPM). La foto dei tecnici in fune sulla pala eolica è uscita: se l'azienda conferma che è un suo lavoro, può tornare nella sezione industria al massimo a 411 px, senza didascalia; meglio una foto nuova di un loro intervento in fune.

### Foto da fare dal vero, per questa versione

Con la decisione "niente" la pagina si regge senza repertorio, ma le foto vere sono piccole (522-733 px) e scattate col telefono, con luci diverse. Una giornata di fotografia, un solo fotografo, stessa luce morbida del giorno, tutte quadrate (1:1, 2400 px o più) più qualche 4:5 per il telefono:
1. **Apertura:** la squadra in tuta e DPI con il logo, davanti al furgone o al ponteggio con il telo Oby, su un cantiere vero; le persone guardano il lavoro, non l'obiettivo. Sostituisce il tetto bruciato, che oggi è piccolo (522 px) e scattato dall'alto col telefono.
2. **Schede dei quattro danni:** un ambiente vero per ciascuno (incendio, allagamento, tetto dopo la grandine, amianto compatto), il giorno del sopralluogo, nessun volto né oggetto personale del cliente; con queste le schede tornano ad avere la foto (regola 9).
3. **Industria:** la squadra dentro un serbatoio o un ambiente confinato, il robot ATEX, l'escavatore a risucchio al lavoro, un intervento in fune loro.
4. **Starflex:** una copertura finita da Oby vista dal drone.
5. **Squadra:** ritratti a mezzo busto, stesso fondo, per la sezione Squadra.
6. **Tre lavori con il nome** (punto 1 sopra): per ciascuno una foto larga del lavoro finito, vista da fuori.


## Dati da confermare con l'azienda

In pagina ci sono solo fatti presi dal loro sito, dalle brochure o dai registri (fonti in `01-analisi.md`). Restano da confermare:

1. **Anno di nascita.** In pagina c'è 2018, come nel sito e su atoka; la brochure 2022 dice "nata nel 2011".
2. **Sede operativa.** In pagina c'è Longare, via Ghizzole 41, come nel sito e nella brochure 2026. La brochure 2022 dava Grisignano di Zocco. Le sedi operative in Lombardia, Emilia Romagna, Toscana e Friuli esistono ancora? Oggi non sono in pagina.
3. **CAP della sede legale.** Il sito dice 25100, atoka 25121; in pagina c'è solo "via Solferino 55, Brescia".
4. **Starflex:**
   - si può usare il marchio STARFLEX® e il nome MPM?
   - la parola "esclusiva" è stata tolta, perché la nota di MPM sulla stessa pagina la smentisce;
   - i "30 anni" sono una dichiarazione del prodotto MPM;
   - chi rilascia la polizza postuma decennale? Finché non si sa, non è in pagina;
   - **le due foto delle coperture** (la copertura piana dell'apertura e il fibrocemento accanto al fotovoltaico) sono di lavori di Oby o di MPM, e si possono usare? Ora sono la prima immagine della home: è la domanda più urgente.
5. **Abilitazioni** (Albo gestori ambientali, categoria per l'amianto, ATEX, lavori in fune, ambienti confinati, ISO o SOA): non sono pubblicate, quindi non sono in pagina. Se ci sono, vanno nella sezione Azienda come prova.
6. **Reperibilità e orari.** Il servizio è attivo 24 ore su 24? Quali sono gli orari dell'ufficio? Oggi in chiusura non c'è nessun orario perché non è scritto da nessuna parte.
7. **Numeri del sito attuale** ("19.284 clienti", "2420 interventi per anno", "1407 progetti"): fuori dalla pagina finché non sono spiegati. Con 8 dipendenti e circa 2 milioni di fatturato non sono credibili.
8. **Contatti e social.** PEC (non trovata), nome dell'amministratore. La pagina Facebook è attiva? È l'unico social nel piede.
9. **Casi reali** con il permesso del cliente, e compagnie assicurative che si possono nominare.
10. **Frasi da far rileggere.**
    - La riga d'apertura ("mettiamo in sicurezza, puliamo e ricostruiamo, pratiche comprese") riassume testi loro.
    - La pagina dà del tu, come i loro testi ("Ti riconsegnamo il tuo bene nelle condizioni originarie", "Potrai riavere la tua casa"). Per questo sono cambiati il bottone ("Chiama lo 0444 1329022", prima "Chiamate"), il titolo "Cosa succede quando ci chiami" e la riga "Sono nove passaggi, dal sopralluogo allo smaltimento: tocca un numero o scorri il righello".
    - I nove passaggi e le nove aree sono abbreviati dalla pagina Pronto intervento, per esempio "Ripristino di apparecchiature elettroniche, impianti e macchinari" al posto di "Risanamento e ripristino apparecchiature elettroniche, impianti e macchinari".
    - Le didascalie sono nostre: "Copertura piana rivestita con la membrana liquida STARFLEX®: torrino, risvolti e parapetto compresi", "Una cucina dopo un incendio: il punto da cui si parte", "Fibrocemento rivestito accanto all'impianto fotovoltaico, che resta al suo posto".
11. **Privacy e Cookie.** L'informativa privacy di oggi è copiata da uno studio legale e va rifatta. Nella proposta i link del piede puntano già a /privacy-policy/ e /cookie-policy/, pagine che vanno scritte.

## Foto da rifare dal vero

Oggi la home usa due foto Starflex del loro sito (apertura e sezione Starflex) e due foto di repertorio Pexels come segnaposto dichiarati (la cucina bruciata e la stanza rifatta). Nella pagina non ci sono persone. Prima della pubblicazione servono una conferma e una giornata di fotografia su due o tre cantieri veri, con il permesso dei clienti.

1. **Apertura, la più importante.** Oggi c'è la copertura piana rivestita STARFLEX del loro sito. Se la foto è di Oby e si può usare, resta: va solo chiesto il file originale a risoluzione piena, perché quella del sito è larga 1701 px, poca per uno schermo da 1920 o per uno schermo retina.
   - Se va rifatta: una copertura finita da poco, nel primo pomeriggio di una giornata chiara, vista in obliquo da un punto un po' più alto del parapetto, con un elemento che dia la misura (torrino, lucernario, risvolto) a destra del centro.
   - Una fascia di tetti o di alberi in alto basta, senza insegne né torri riconoscibili.
   - Orizzontale 16:10 a 4000 px o più, più un quadrato dallo stesso punto per il telefono.
2. **Il danno, per Pronto intervento.** Un ambiente vero di un loro intervento dopo un incendio o un allagamento, il giorno del sopralluogo. Orizzontale larga (21:9 ricavabile), luce naturale, nessun volto né oggetto personale riconoscibile del cliente.
3. **Prima e dopo dello stesso ambiente.** È il racconto dell'azienda, e oggi in pagina non c'è perché mancano due foto vere. Stessa stanza, stesso punto di ripresa (cavalletto e segno a terra), stessa focale e stessa altezza, luce simile: una foto al primo sopralluogo e una alla consegna. Con questa coppia si possono rimettere il "prima" in Pronto intervento e il "dopo" in chiusura, oppure il cursore prima e dopo, ma solo con le due foto vere.
4. **Chiusura.** La stessa stanza del punto 3 alla consegna, chiara e ordinata, verticale o 5:4.
5. **Starflex.** Il fibrocemento accanto al fotovoltaico va bene se è loro; in alternativa una copertura industriale finita vista dal drone.
6. **Facoltative, per le pagine interne:** la squadra con i suoi DPI e i suoi mezzi, un intervento in fune, la sede e il furgone di Longare.

## Licenze

- **Foto Pexels** (F. Hektor 10252682, Max Vakhtbovych 7031621): Licenza Pexels, uso commerciale libero, attribuzione non obbligatoria. URL e verifica in `assets/CREDITI.md`. Le foto con persone (Roger Brown 11279905, Tima Miroshnichenko 6195952) non sono più in pagina.
- **Foto Starflex** (`assets/originali/9e96e5_520d02be…webp` in apertura, `9e96e5_c7d17813…webp` nella sezione Starflex): dal sito di Oby. Diritti da confermare (forse sono di MPM).
- **Carattere** Onest: Google Fonts, SIL Open Font License 1.1 (`sito/fonts/OFL.txt`), servito dalla pagina.
- **Nessuna immagine generata dall'IA.**

## Loghi

- Logo Oby: vettoriale vero estratto senza ridisegnarlo dai tracciati della copertina della brochure "Copertura Sicura Starflex" (PDF del sito, giugno 2026). In pagina è `sito/img/logo-obygroup.svg`; l'originale è `assets/originali/logo-obygroup-dal-pdf.svg`, la versione per fondi scuri `logo-obygroup-negativo.svg`. Va chiesto all'azienda il file del logo ufficiale per controllare che coincida.
- Non c'è il logo MPM né altri marchi di terzi. Il nome STARFLEX® è scritto come testo (vedi il punto 4 dei dati da confermare).

## Pagine del sito nuovo a cui punteranno i link

Oggi i link del menu e del piede portano alle sezioni della home (ancore; ogni voce della colonna Interventi punta alla sua riga, per esempio `#danni-post-incendio`). Privacy e Cookie puntano già a `/privacy-policy/` e `/cookie-policy/`. Nel sito nuovo i link andranno a queste pagine:

| Pagina | Percorso |
|---|---|
| Home | `/` |
| Pronto intervento (i nove passaggi) | `/pronto-intervento/` |
| Interventi, indice | `/interventi/` |
| Danni post incendio | `/interventi/danni-post-incendio/` |
| Bonifiche post alluvione | `/interventi/bonifiche-post-alluvione/` |
| Danni da eventi atmosferici | `/interventi/danni-eventi-atmosferici/` |
| Smaltimento amianto | `/interventi/smaltimento-amianto/` |
| Lavori in fune | `/interventi/lavori-in-fune/` |
| Ambienti confinati | `/interventi/ambienti-confinati/` |
| Bonifiche industriali | `/interventi/bonifiche-industriali/` |
| Sabbiature e verniciature | `/interventi/sabbiature-verniciature/` |
| Opere edili | `/interventi/opere-edili/` |
| Copertura Sicura Starflex (per le assicurazioni, con la documentazione tecnica, i supporti su cui si posa e il modo di posa, tolti dalla home) | `/copertura-sicura-starflex/` |
| Azienda | `/azienda/` |
| Contatti | `/contatti/` |
| Privacy | `/privacy-policy/` |
| Cookie | `/cookie-policy/` |

I due PDF (brochure Starflex 2026 e brochure aziendale 2022) oggi puntano ai file sul sito Wix: vanno ricaricati sul sito nuovo. La brochure 2022 riporta ancora la sede di Grisignano e l'anno 2011.

## Newsletter

Niente newsletter. Oby è un servizio d'emergenza su chiamata, chi lo cerca lo fa dopo un danno, e non ci sono novità, fiere o cataloghi periodici da comunicare. Per le compagnie assicurative basta il PDF di Starflex scaricabile.

## Righe "da guardare" dello strumento dei segnali

- **H2 di due misure (60 e 56 px):** la pagina punta su un solo elemento grande, il titolo d'apertura da 108 px con la foto.
- **Numerazione 01-09:** sono i nove passi in ordine del loro pronto intervento, dal sopralluogo allo smaltimento, quindi è una procedura vera.

## Versione 2 (scheda d'uso)

Seconda proposta di home, costruita sulla scheda di identità e d'uso (`_prova/uso/SCHEDA.md`) e non come ritocco della prima: prima si serve chi apre il sito (il danneggiato da telefono, l'ufficio sinistri e il tecnico d'azienda da computer), poi si fa sembrare loro, poi si cura l'esecuzione. La prima home (`sito/`) resta com'è.

- Pagina: `sito-v2/index.html` (statica, si apre con file:///); immagini in `sito-v2/img/` (solo foto del loro sito, lavorate e in più larghezze), carattere in `sito-v2/fonts/`, PDF Starflex in `sito-v2/doc/`.
- Schermate e nota di progetto: `screenshot/home-v2/` (`NOTA.md` dice cosa trova ogni visitatore e dove, l'idea, caratteri, colori, foto e controlli).
- Si rifà tutto con `sh _prova/uso/script/build_v2.sh` (immagini con `img_v2.py`, screenshot e misure con `misura_v2.mjs`; prova del gesto con `prova_gesto_v2.mjs`).

**Cosa cambia rispetto alla prima.** Prima schermata pensata per il telefono: tasto Chiama fisso, il loro claim "Quando il danno diventa serio, noi entriamo in azione" rimesso al suo posto, due bottoni grandi per cellulare e uffici, il link per mandare le foto per mail, quattro scorciatoie. A 1440 la loro foto del condominio ponteggiato a tutta altezza e tre accessi: Ho avuto un danno, Compagnie assicurative e Starflex, Aziende e bonifiche industriali. Poi i quattro danni con le loro righe, i nove passaggi tutti in vista su un campo nel rosso del logo, l'elenco industriale completo (14 voci più le righe della pagina Pronto intervento) con la richiesta che si compone segnando i lavori, Starflex per le compagnie con il PDF, chi siamo con i dati societari, chiusura con foto e recapiti, piede. Nessuna foto di repertorio: tutte le immagini sono del loro sito.

**Rifinitura dopo le prove (2 novembre).** Tre clienti tipo (danneggiato da telefono, ufficio sinistri, tecnico d'azienda) e il giudice d'identità hanno provato la v2; il dettaglio è nella `NOTA.md`, sezione "Dopo le prove". In breve: fondo bianco; apertura con il claim a tutta riga e tre colonne (telefoni e mail, la loro foto del tetto bruciato con due operatori a misura vera, tre porte); bottone "Manda le foto del danno" a tutta larghezza; barra fissa in basso sul telefono con "Cellulare" e "Uffici"; zona "in Veneto e fuori regione" nella riga d'apertura; tre passi per il cliente prima dei lavori di cantiere; Starflex con il nome del prodotto nel titolo, testo e PDF visibili subito dopo il salto, brochure aziendale accanto e mail precompilata per affidare un sinistro; fune e cunicolo accanto all'elenco industriale; chi siamo e contatti fusi in un blocco con la richiesta di visura, iscrizioni e abilitazioni; pagina a 5501 px a 1440 e 8205 a 390 (prima 6890 e 10909). Prove dei salti: `_prova/uso/script/prova_rifinitura.mjs`.

**Prima di mettere in linea la versione 2.**
- Il PDF Starflex (`sito-v2/doc/copertura-sicura-starflex-2026.pdf`) scrive "Un'esclusiva partnership", "Durabilità certificata 30 anni" e il refuso "Comagnie": la pagina li ha tolti perché la nota MPM smentisce l'esclusiva. Va chiesta a Oby e MPM un'edizione corretta prima di pubblicare il bottone.
- La brochure aziendale (`sito-v2/doc/brochure-aziendale-2022.pdf`, copiata dal sito di oggi) dà ancora la sede a Grisignano di Zocco e "nata nel 2011": in pagina è etichettata "edizione 2022"; va rifatta con Longare.

**Caratteri e impaginazioni (giro del 2 novembre, "più accoppiate di font e grandezze e layout mescolati").** Il dettaglio è nella `NOTA.md`, sezione "Caratteri, scala e impaginazioni".
- Due famiglie con ruoli fissi, tutte e due servite dalla pagina (`sito-v2/fonts/`): **Big Shoulders Display** per i titoli, le frasi grandi, i numeri dei passi e il cellulare grande della chiusura (Google Fonts, SIL Open Font License 1.1, `sito-v2/fonts/OFL-big-shoulders.txt`), un grottesco stretto da segnaletica, come la scritta di un mezzo d'emergenza; **Atkinson Hyperlegible Next** per testo, bottoni, telefoni da toccare, tabelle e didascalie (Google Fonts, SIL Open Font License 1.1, `sito-v2/fonts/OFL.txt`). Nessun monospazio.
- Scala di otto livelli, da 116 px (il claim) a 13,5 px (le didascalie), con le misure in variabili CSS.
- Un impianto diverso per ogni sezione: claim enorme sopra tre colonne; danni come indice a righe a tutta larghezza; campo rosso a scacchiera in due colonne sbilanciate con i numeri grandi dei passi e la frase sola; industria con titolo a tutta riga, elenco su tre colonne e mosaico di due foto di misure diverse; Starflex in due colonne sbilanciate più la foto in una fascia a tutta larghezza (nuove immagini `starflex-banda-*`); chiusura con il testo a sinistra e il condominio a destra fino al bordo.
- L'uso non cambia: a 390 bottoni di chiamata, mail delle foto, altro cellulare e scorciatoie sono 4 px più in alto di prima (misure con `_prova/uso/script/prima_390.mjs`); i salti "Compagnie assicurative" e "Aziende" arrivano sul PDF e sul bottone della richiesta senza scorrere. Pagina a 6910 px a 1440 e 8331 a 390.
- Da sapere: l'area coperta da foto scende al 21,1 % (prima 23,7 %), perché la tipografia più grande allunga la pagina; la giornata di fotografia qui sotto resta la cura.

**Da confermare in più per la versione 2** (l'elenco completo è nella `NOTA.md`):
1. Reperibilità fuori orario, orari degli uffici e PEC (in pagina non ci sono); se si può usare WhatsApp sul cellulare per le foto.
2. La zona servita: in pagina c'è solo "in Veneto e fuori regione"; la brochure 2022 elenca sedi operative in Veneto, Lombardia, Emilia Romagna, Toscana, Friuli Venezia Giulia. Qual è l'elenco di oggi?
3. Se "seguiamo noi le pratiche burocratiche" vale anche per il rapporto con l'assicurazione e il perito.
4. Quali foto sono di loro cantieri: il tetto bruciato dell'apertura (e i due operatori), il condominio della chiusura (il telo "Qui per voi" è loro? che lavoro e dove?), il cunicolo (il logo sulla tuta è vero? oggi è tagliato fuori), la mansarda usata per "infiltrazioni", la pala eolica; la foto Starflex del fibrocemento è di Oby o di MPM?
5. Se robot ATEX ed escavatori a risucchio sono mezzi loro; iscrizioni e abilitazioni con numero ed ente (Albo gestori ambientali e categorie, amianto, ambienti confinati, lavori in fune), da scrivere nella riga "Documenti" al posto della richiesta per mail.
6. Una riga di descrizione per le voci industriali che oggi hanno solo il titolo (digestori, escavatori a risucchio, reti gas, spazi a rischio inquinamento, smaltimento, manti stradali, fotovoltaico).

**Foto da rifare dal vero, per la versione 2.** Le foto vere ci sono ma sono piccole (da 450 a 1155 px) e da telefono: oggi coprono il 23,7 % della pagina a 1440, contro il 35 % dei siti di riferimento.
1. Apertura: un loro cantiere dopo un incendio con la squadra al lavoro (come il tetto bruciato di oggi, che è 567 px), dall'alto o dal ponteggio, 4:3 a 2500 px o più, luce naturale, nessun volto né oggetto del cliente riconoscibile; più un taglio orizzontale 21:9 per la striscia del telefono.
2. I quattro danni: un ambiente vero per ciascuno (incendio, allagamento, tetto dopo la grandine, amianto) il giorno del sopralluogo, orizzontali 4:3 a 2000 px, luce naturale, nessun volto né oggetto personale del cliente riconoscibile.
3. Industria: la squadra con i suoi DPI dentro un serbatoio o un ambiente confinato, il robot ATEX, l'escavatore a risucchio al lavoro, 4:5 a 2000 px.
4. Chiusura: un loro condominio o capannone ripristinato, con il telo, in verticale 3:4 a 3000 px; in industria un intervento in fune loro, quadrato a 2500 px.
5. Starflex: una copertura finita da Oby vista dal drone, 21:9 a 3000 px.

**Pagine del sito nuovo.** Valgono quelle della tabella qui sopra. Nella versione 2 i link del piede puntano alle sezioni della home (`#incendio`, `#allagamento`, `#maltempo`, `#amianto`, `#dopo`, `#bonifiche-industriali`, `#ambienti-confinati`, `#escavatori-a-risucchio`, `#lavori-in-fune`, `#sabbiature`, `#opere-edili`, `#assicurazioni`, `#azienda`, `#contatti`) e ai due PDF in `sito-v2/doc/`; nel sito vero andranno a `/interventi/...`, `/pronto-intervento/` e `/copertura-sicura-starflex/`. Privacy e Cookie puntano a `/privacy-policy/` e `/cookie-policy/`.

**Newsletter.** Anche qui niente newsletter, per lo stesso motivo: servizio d'emergenza su chiamata, nessuna novità periodica da comunicare.

## Versione 1 con l'uso

Il committente ha visto le due versioni e ha scelto la prima ("no preferisco versione 1"), con l'uso. La pagina è sempre `sito/index.html`, rifatta con `sh _prova/script/build_finale.sh` (sorgente `_prova/script/finale-pagina.html`, immagini con `finale_img.py`); misure, salti, barra e link si provano con `node _prova/script/uso1_prova.mjs <url> <cartella>` e `node _prova/script/uso2_misure.mjs <url> <cartella>`. Copie: `_prova/versione-1-originale/` (prima del giro) e `_prova/script/finale-pagina-uso1-giro1.html` (primo giro, prima delle prove dei clienti tipo). Dettaglio, misure e controlli in `screenshot/home/NOTA.md`, sezione omonima.

**Cosa resta com'era:** grafica, Onest, colori, griglia, la copertura STARFLEX dell'apertura (a computer dov'era, al telefono sotto i bottoni, sempre nella prima schermata), il titolo "Eliminiamo ogni traccia del danno", l'ordine delle sezioni, la cucina e la stanza "Foto indicativa", la chiusura e il piede.

**Cosa è stato aggiunto o cambiato, nello stile della pagina (due giri):**
- Apertura: subito sotto il titolo la riga "Incendi, allagamenti, grandine e maltempo, amianto: in case, condomini, negozi e capannoni. Mettiamo in sicurezza, puliamo e ricostruiamo, e alle pratiche burocratiche pensiamo noi. Da Longare (VI), in Veneto e fuori regione."; "Chiama il cellulare 340 834 9597" (rosso), "Chiama gli uffici 0444 1329022" (a bordo), "Manda le foto del danno per mail" (al telefono a bordo, oggetto e traccia già scritti), "Altro cellulare 393 911 4656"; al telefono e al tablet quattro tacche Incendio, Allagamento, Grandine e tetti, Amianto; le tre porte. In testata "Uffici" sopra il numero anche al telefono.
- Testata fissa a computer; nel menu anche "Industria".
- Telefono e tablet: barra fissa con Cellulare e Uffici, che compare appena il bottone del cellulare esce dallo schermo.
- Pronto intervento: titolo "Nessuna incombenza burocratica, pensiamo noi a tutto", il loro claim "Quando il danno diventa serio, noi entriamo in azione" in testa al paragrafo, chi segue le pratiche (compagnia e numero del sinistro), i nove passaggi come elenco numerato tutto in vista al posto del righello.
- Interventi in due gruppi con un'etichetta da titolo; "Bonifiche dopo allagamenti e alluvioni"; le voci industriali complete con la mail per capitolato e foto; fune e cunicolo con una riga su attrezzature ATEX ed escavatori a risucchio e la richiesta di visura, iscrizioni e abilitazioni.
- Starflex: paragrafo con le parole della brochure 2026 (sopra la guaina esistente; per la compagnia risarcimenti più bassi e sinistri chiusi prima), tabella di cinque righe (guaina, smaltimento, posa a freddo, supporto bagnato, 30 anni dichiarati da MPM), bottone della documentazione tecnica con "giugno 2026", brochure, richiesta documenti, contatto per affidare un sinistro; tolto "in tempi rapidissimi".
- Azienda: titolo "Ripristiniamo a nuovo e tutto torna come prima" e una tabella con ragione sociale, P.IVA, REA, sede operativa e legale, uffici, mail e "Chiedi visura, iscrizioni e abilitazioni per mail". Nei contatti "Sede operativa".
- Tolti "è sempre pronta a intervenire", i "Fig.", "nasce nel 2018"; "30 anni di durabilità dichiarata" al posto di "certificata".

**Respinto:** il claim al posto del titolo e un'altra foto al posto della copertura d'apertura (il committente ha scelto titolo e immagine della versione 1); togliere la cucina e la stanza Pexels (sono grafica della versione scelta e già dichiarate; le foto vere non reggono quelle misure); descrizioni inventate per le voci industriali con solo il titolo; lo stato "aperto ora / chiuso ora", gli orari e "24 ore su 24" (nessun dato pubblicato); il modulo a caselle della versione 2.

**Da confermare in più con l'azienda (prima di pubblicare):**
1. Orari degli uffici, chi risponde al cellulare fuori orario, se c'è reperibilità 24 ore su 24. Con gli orari veri si può aggiungere accanto ai bottoni lo stato "aperto ora / chiuso ora" calcolato sull'ora di Roma.
2. Se si può usare WhatsApp sul cellulare per le foto del danno (oggi solo mail).
3. La zona servita: in pagina c'è "in Veneto e fuori regione", dedotto dalle sedi operative della brochure 2022 (Veneto, Lombardia, Emilia Romagna, Toscana, Friuli Venezia Giulia). Qual è l'elenco di oggi? Con la risposta va riscritta la fine della riga d'apertura.
4. Se le pratiche che seguono comprendono il rapporto con la compagnia e il perito, e se il numero del sinistro serve davvero alla prima chiamata (in pagina: "se il danno è assicurato, dicci la compagnia e il numero del sinistro").
5. Che "case, condomini, negozi e capannoni" vada bene come elenco (dal loro "ambienti ed edifici di qualsiasi tipo" e dalla foto del condominio).
6. Iscrizioni e abilitazioni con numero ed ente (Albo gestori ambientali e categorie, amianto, ATEX, ambienti confinati, lavori in fune): oggi la pagina le fa chiedere per mail; quando arrivano vanno scritte nella riga "Documenti". Se robot ATEX ed escavatori a risucchio sono mezzi loro (in pagina: "lavoriamo con").
7. Le due foto vere dell'industria: la fune sulla pala eolica è un loro lavoro? Il cunicolo è loro, e il logo sulla tuta (tagliato fuori) è vero?
8. Le voci industriali con solo il titolo (digestori, escavatori a risucchio, reti gas, spazi a rischio inquinamento, smaltimento rifiuti, manti stradali, fotovoltaico): serve una riga loro per ciascuna.
9. I PDF in `sito/doc/` sono quelli del sito di oggi: la documentazione Starflex scrive "esclusiva", "durabilità certificata" e "Comagnie", la brochure 2022 dà Grisignano e il 2011. Vanno rifatti da Oby (e MPM) prima di pubblicare i link; "Meno costi oggi. Meno sinistri domani." è preso dalla stessa brochure.
10. Restano validi i punti 1-11 dei "Dati da confermare" qui sopra (l'anno di nascita non è in pagina).

**Foto da rifare dal vero, per questa versione:** valgono i punti di "Foto da rifare dal vero" qui sopra, con due priorità: (a) un loro ambiente dopo un incendio, orizzontale 21:9 a 2600 px o più, luce naturale, nessun volto né oggetto del cliente riconoscibile, al posto della cucina "Foto indicativa"; (b) lo stesso ambiente alla consegna, 5:4 a 2000 px, al posto della stanza "Foto indicativa". Per la parte industriale: la squadra in un serbatoio o un ambiente confinato con i DPI e un escavatore a risucchio al lavoro, 1:1 e 16:10 a 1200 px o più, al posto della fune e del cunicolo, che sono piccoli (582 e 450 px). Va anche chiesto se la copertura STARFLEX dell'apertura è un lavoro di Oby: se è di MPM, serve una loro copertura finita, 16:10 a 2800 px, presa dal drone o dal parapetto.

**Nessuna foto nuova di repertorio:** in questo giro non è stata aggiunta nessuna immagine; `assets/CREDITI.md` non cambia. Carattere: Onest, Google Fonts, SIL Open Font License 1.1, servito da `sito/fonts/`.
