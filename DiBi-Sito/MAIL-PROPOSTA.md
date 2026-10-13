# Mail di proposta: Di Bi

Bozza pronta da copiare e inviare dal committente. Non è stata inviata e l'azienda non è stata contattata in nessun modo.
Per Di Bi non c'è ancora un sito demo online: la mail allega l'anteprima della pagina iniziale e propone di completare il sito.

## Destinatario

- **Consigliato: dibi@dibispa.com.** È l'indirizzo generale che l'azienda pubblica oggi sul proprio sito: pagina Contatti
  (`http://www.dibispa.com/contatti-2/`, sotto "Contatti DI BI SpA", accanto a indirizzo e telefono), testo della pagina
  Catalogo ("sending an email to dibi@dibispa.com") e descrizione della pagina Contatti. Riverificato il 7 ottobre 2026 sul
  sito vivo, a 1440 e a 390 px (5 occorrenze nell'HTML della pagina Contatti), e di nuovo nel controllo avversario dello
  stesso giorno: visibile a 390 e a 1440 sotto il titolo della pagina. Sul sito è scritto, non è un link cliccabile.
- **PEC: dibispa@pec.trive.net.** Fonte: aziende.it (dati del Registro Imprese, aggiornati al 7/9/2026). Non è pubblicata
  sul sito. È la casella PEC della società presso il suo gestore (Trivenet), non un indirizzo del fornitore: usarla solo
  dopo il controllo su INI-PEC (inipec.gov.it), se il committente preferisce la PEC come per Benvegnù.
- Telefono, per la chiamata dopo l'invio: +39 0424 534099 (pagina Contatti e fondo di ogni pagina).
- **Da non usare:** reportingdibi@gmail.com (pagina Certificazioni) è il canale per le segnalazioni di condotte illecite,
  non un contatto commerciale; il modulo "Catalogo" e il modulo dei contatti del sito (non si compilano moduli). Nessun
  indirizzo di persone fisiche è pubblicato sul sito e non ne vanno cercati.

## Oggetto

Nuovo sito per Di Bi S.p.A.: anteprima della pagina iniziale in allegato

## Testo

Gentili Signori,

mi chiamo [Nome Cognome] e con [Agenzia] realizziamo siti per aziende. Guardando www.dibispa.com abbiamo notato alcune cose che oggi rendono più difficile trovarVi e contattarVi:

- da smartphone il menu non si apre, e dalle altre pagine non si arriva a Contatti, Azienda e Certificazioni;
- la pagina News riporta "No posts were found." e in fondo a ogni pagina c'è ancora "© 2018";
- nel sito italiano il testo della pagina Catalogo è in inglese, e il modulo dei contatti ha 15 campi, 11 obbligatori, con voci in italiano e in inglese.

Abbiamo quindi preparato, di nostra iniziativa, la pagina iniziale di un nuovo sito: la trovate in allegato, in due versioni, per computer e per telefono. Le foto sono Vostre, i dati sono pubblici: li usiamo solo per questa proposta. Se l'impostazione Vi convince, completeremmo il sito con contenuti e prove, non solo immagini:

- Oro, Argento e Tessuto: famiglie di catene per nome, carature e leghe;
- le sei fasi di lavorazione, dalla fusione alla galvanica, con le Vostre foto;
- le prove: certificazione RJC con numeri e validità, documenti RJC da scaricare, fiere con le date che ci indicherete;
- i settori serviti: gioiellerie, grossisti e importatori, catene di negozi, produttori;
- menu e telefono che funzionano con un tocco da smartphone, un modulo breve per il catalogo (in italiano e in inglese) e i vecchi indirizzi collegati ai nuovi, così i link su Google restano validi.

I testi sono bozze da verificare con Voi: per esempio i titoli, i settori serviti, che tutte le fasi si svolgano in azienda, le carature in produzione, l'uso dei marchi RJC e il catalogo da inviare.

Se la proposta Vi interessa, possiamo passare a Cassola per mostrarVela in venti minuti, oppure sentirci al telefono quando preferite. Se invece non Vi interessa, basta rispondere a questo messaggio: cancelliamo l'anteprima e non Vi scriveremo più.

Cordiali saluti,

[Nome Cognome]
[Agenzia]
[telefono] · [email]

## Allegati

| File | Da | Misure | Peso |
|---|---|---|---|
| `DiBi-Sito/allegati-mail/dibi-home-computer.jpg` | `_prova/direzioni/giro2/racconto/proto-1440.png` | 1440 x 5422 px, JPEG qualità 80 | 700.649 byte (0,67 MB) |
| `DiBi-Sito/allegati-mail/dibi-home-telefono.jpg` | `_prova/direzioni/giro2/racconto/proto-390.png` | 390 x 4850 px, JPEG qualità 80 | 230.924 byte (0,22 MB) |

Totale 0,89 MB, sotto il limite di 1,5 MB per file. Si allegano solo i due JPG: non `proto.html`, che ha link segnaposto
(ancore interne come `#oro` e `#catalogo`, nessuna pagina vera dietro) e prende le immagini da una cartella locale.

## Variante quando la demo completa è online

Si sostituisce solo il paragrafo che comincia con "Abbiamo quindi preparato" (fino ai due punti prima dell'elenco); il resto
resta uguale. In questo caso i due allegati si possono togliere.

> Abbiamo quindi preparato, di nostra iniziativa, il nuovo sito completo. Potete vederlo qui:
>
> [link]
> Password di accesso: [password]
>
> È un'anteprima privata, non indicizzata sui motori di ricerca. Le foto sono Vostre, i dati sono pubblici: li usiamo solo per questa proposta. Il sito comprende contenuti e prove, non solo immagini:

Con la demo online, nell'ultima voce dell'elenco va scritto ciò che c'è davvero (per esempio il numero di pagine e di
indirizzi vecchi collegati), e nella riga dei testi da verificare si può aggiungere "Il sito è pronto: se decidete di
acquistarlo, può andare online sul Vostro dominio in pochi giorni" solo se è vero.

## Prima dell'invio (non va nella mail)

### Da dire solo a voce, mai per iscritto

- **Script estraneo nella home.** Nel contenuto della home italiana ci sono 3 tag `<script src="//plankjock.com/20c1f9347f59cf976e.js">`
  (pagina modificata il 3/10/2025). Ancora presenti il 7/10/2026: letti nell'HTML con curl, il file non è stato aperto né
  eseguito, e nel browser di verifica le richieste verso quel dominio sono state bloccate. È il modo in cui di solito si
  presentano le iniezioni di codice nei WordPress non aggiornati: consigliare di farlo controllare dal loro tecnico, senza
  ipotesi sull'origine.
- Il sito risponde solo in http (il 7/10/2026 `https://www.dibispa.com` non stabilisce la connessione): il browser lo segna
  "Non sicuro", anche sulle pagine con i moduli.
- Software fuori supporto: PHP 5.6.40 (intestazione `x-powered-by`, ramo senza aggiornamenti di sicurezza da gennaio 2019)
  e WordPress 5.1.19 (`meta generator`, ramo del 2019), ricontrollati il 7/10/2026.
- "Privacy Policy" e "Cookie Policy" in fondo alle pagine aprono una pagina iubenda "Document not found" (404, ricontrollato
  il 7/10/2026), e in basso a destra di ogni pagina resta l'icona di avviso di iubenda con il punto esclamativo rosso; i moduli
  non hanno informativa. Google Analytics parte alla prima visita senza nessuna scelta (5 cookie `__utm*` scritti al primo
  caricamento): è il vecchio codice `ga.js` con la proprietà UA-96943901-1, che Google non elabora più dal 1° luglio 2023,
  quindi i cookie si scrivono ma le statistiche non arrivano da nessuna parte.
- Un'osservazione in più, innocua, verificata oggi: il logo DIBI non compare in testata, né a 1440 né a 390 (5 immagini
  "Logo" con `visibility:hidden`, un errore JavaScript del tema blocca anche il menu). Nell'anteprima il logo c'è: si può
  farlo notare quando si mostra la proposta.

### Dati del prototipo da confermare con l'azienda

- Tutti i titoli sono nostri, non dell'azienda: "Le catene della vostra vetrina", "Quelle che il cliente chiede per nome",
  "Il Tessuto si sceglie con le mani" (da "through touch" del testo inglese del Tessuto), "Dalla fusione alla galvanica, in
  azienda", "Quando vi chiedono da dove viene l'oro", "Il catalogo, su richiesta".
- "Le produciamo a Cassola per gioiellerie, grossisti e produttori": i clienti sono dedotti dalle voci del modulo contatti
  (Retailer, Importer-Wholesaler-Chains stories, Manufacture), non dichiarati dall'azienda. Vale anche per i settori serviti promessi nella mail.
- Che tutte e sei le fasi, dalla fusione alla galvanica, si facciano in azienda: il sito le elenca e scrive "placcatura
  eseguita in azienda", ma non dice che tutto è interno.
- Abbinamento foto e fase: "macchina catenaria" e "mani della finitura" sono nostre interpretazioni delle foto.
- Carature 8, 9, 10, 14, 18, 21 e 22 kt e leghe gialla, bianca e rosè: testo del 2017-2018, da confermare se valgono ancora
  per "ogni modello".
- "Rolo, spiga, grumetta e figaro" in oro e in argento: il sito dà la figaro solo per l'argento; per l'oro viene dai cataloghi
  del 2022.
- Catalogo "codice, peso, lunghezza e titolo [...] in oro 14 carati e in argento 925": viene dai PDF di settembre 2022 sul loro
  server, non linkati; quale catalogo mandano oggi e a chi.
- RJC: numeri COP 0000 6883 e CoC C0000 6884 e validità "fino al 3 novembre 2028" verificati oggi sul registro RJC
  (responsiblejewellery.com/member/dibi-spa/: periodo 07/11/2025-03/11/2028 per tutti e due). Da confermare l'uso dei
  marchi RJC senza le righe "certified" e la frase "l'ente che fissa gli standard etici", nostra sintesi del loro testo.
- Grafia "Di Bi S.p.A." per i dati legali (registro: DI BI S.P.A.; sul sito nove grafie diverse) e "DIBI" come marchio.
- Il fax +39 0424 533396 è ancora attivo? Viene dal piede del 2018.
- "© 2026" nel piede del prototipo.
- Segnaposto del prototipo: tutti i link del menu (Oro, Argento, Tessuto, Lavorazione, Certificazioni, Azienda, Contatti), "EN"
  (la versione inglese non esiste ancora), i due bottoni "Richiedi il catalogo" (nessun modulo dietro), "Catene in oro",
  "Catene in argento", "Certificati e politiche RJC" e nel piede "Note legali", "Privacy", "Cookie", "Segnalazioni" sono
  ancore interne alla stessa pagina (`#oro`, `#catalogo`, `#certificazioni`...) o vuote (`#en`, `#privacy`, `#cookie`,
  `#note-legali`, `#segnalazioni`, il logo a `#`): nessuno porta a una pagina vera. Funzionano davvero solo il telefono
  (`tel:`), l'email (`mailto:`) e il pulsante "Menu" a 390. Privacy e cookie policy vanno scritte o fornite dall'azienda.
- Testi alternativi delle foto: descrizioni nostre.
- Non promessi nella mail perché non ci sono dati: fiere dopo il 2022, brevetti ("numerosi brevetti internazionali" senza
  numero né oggetto), anno di fondazione (registro dal 1976, il sito dice "oltre trent'anni fa"), se "Tessuto" è un marchio
  registrato.

### Controlli da fare

- Riverificare le tre osservazioni il giorno dell'invio: se una non è più vera, toglierla. Verifica del 7/10/2026 con
  Playwright (Chromium) a 1440 e a 390 px su home, News, Catalogo, Contatti, Certificazioni, Tessuto, e a 390 sui link
  visibili di 12 pagine. Script, misure e screenshot in `_prova/mail-verifica/` (`verifica.cjs` e `verifica.json`,
  `raggiungibili.cjs`, `link390.cjs`, `home-390-dopo-tap.png`, `news-390.png`, `catalogo-390.png`).
- Controllo avversario del 7/10/2026 (Playwright Chromium, 12 pagine a 390 con touch e densità 2 e a 1440; richieste verso
  plankjock bloccate), in `_prova/mail-verifica/avversario/`: menu a hamburger alto 0 px prima e dopo tocco e clic (9 voci
  nel codice); a 390 `/contatti-2/`, `/azienda/` e `/certificazioni/` compaiono solo come link della pagina a se stessa;
  "No posts were found." su News; "© 2018" nel piede di tutte le 12 pagine; su `/catalogo/` titolo e voci del modulo in
  inglese ("Your name", "Your email", "Subject", "Your messagge"), solo il bottone "INVIA" in italiano; modulo Contatti con
  15 campi, 11 con `aria-required="true"` (nome, cognome, indirizzo, ZIP, città, provincia, paese, titolo, email, attività,
  telefono).
- **Tolta dalla mail** la frase "il telefono in fondo alla pagina non si chiama con un tocco": il piede non ha link `tel:`,
  ma le pagine non hanno `<meta name="format-detection" content="telephone=no">` e Safari su iPhone rende cliccabili da sé i
  numeri di telefono. Chi apre il sito da iPhone vedrebbe il numero chiamabile: non va scritta né detta.
- Compilare firma, [Agenzia], [telefono] e [email]. La mail parte dal committente, non da noi.
- Se si usa la PEC: verificarla su INI-PEC prima.
- Aprire i due JPG dal telefono prima di inviarli: sono pagine lunghe (5422 e 4850 px) e vanno scorse.
- Non scrivere né dire che il sito completo è pronto: esiste solo la pagina iniziale. Decidere tempi e prezzo prima
  dell'eventuale incontro.
- Quando la demo sarà online: password, nessuna indicizzazione, e attenzione al modulo di richiesta del catalogo, che non
  deve scrivere davvero all'azienda.
- Per la visita a Cassola (Via Grande 89): orari lunedì-venerdì 8:00-17:30 dal profilo Google, non pubblicati sul sito.
- Non citare lo slogan della home attuale: contiene una parola della lista vietata.
