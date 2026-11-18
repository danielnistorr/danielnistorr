# Mail di proposta: Conceria Europa

Bozza pronta da copiare e inviare dal committente. Non è stata inviata e l'azienda non è stata contattata in nessun modo.
Per Conceria Europa non c'è ancora un sito demo online: la mail allega l'anteprima della pagina iniziale (computer e
telefono) e propone di completare il sito. Non va scritto né detto che il sito completo è pronto.

## Destinatario

- **Consigliato: info@conceriaeuropa.it.** È l'indirizzo generale che l'azienda pubblica oggi sul proprio sito: nel piè
  di pagina della home (link cliccabile, accanto a telefono e P.IVA) e nella finestra "contatti" (`it/contatti.php`), dove
  è indicato come "Accoglienza". Riverificato il 7 ottobre 2026 sul sito vivo: con curl su `index.php?it` e
  `it/contatti.php`, e con Playwright nel testo del piè di pagina a 390 e a 1440 px.
- Alternative pubblicate nella stessa finestra "contatti" (verificate oggi), da non usare come primo indirizzo:
  - faggiana.luigi@conceriaeuropa.it, "Ufficio Commerciale": è nominativo (Luigi Faggiana). Utile solo se dopo il primo
    contatto l'azienda indica lui come referente;
  - amministrazione@conceriaeuropa.it, "Ufficio Amministrativo";
  - qualitaambiente@conceriaeuropa.it, "Ufficio Ambiente";
  - rezzante.paolo@conceriaeuropa.it, "Tesoreria e Finanza" (nominativo, non adatto a una proposta).
- **PEC: conceriaeuropa@pec.confindustriavicenza.it.** Fonte: visurissima.it (dati del Registro Imprese aggiornati al
  7/10/2026), annotata in `_metodo/CONTATTI.md`. Non è sul sito né su aziende.it: una sola fonte, non riletta da qui (la
  ricerca di visurissima carica i risultati via script). È la casella PEC della società presso il servizio di
  Confindustria Vicenza, non un indirizzo del fornitore. Usarla solo dopo il controllo su INI-PEC (inipec.gov.it) con la
  P.IVA 00166680249, se il committente preferisce la PEC come per Benvegnù.
- Telefono, per la chiamata dopo l'invio: +39 0444 44 01 53 (due linee); fax +39 0444 64 88 79.
- **Da non usare:** gli indirizzi dei fornitori citati sul sito (Net Evolution per il sito, iubenda per i cookie,
  A11y Studio per l'accessibilità, Larese & Associati per la privacy). Il sito non ha moduli di contatto; non si
  compilano moduli altrove.

## Oggetto

Nuovo sito per Conceria Europa S.r.l.: anteprima della pagina iniziale in allegato

## Testo

Gentili Signori,

mi chiamo [Nome Cognome] e con [Agenzia] realizziamo siti per aziende. Guardando www.conceriaeuropa.it abbiamo notato alcune cose che oggi rendono più difficile trovarVi e contattarVi:

- da smartphone il sito appare come la versione da computer ridotta a un terzo, il numero di telefono non si chiama con un tocco e, ruotando lo schermo, la pagina passa all'inglese;
- aprendo "Fasi di lavorazione" le 28 foto del reparto non compaiono: si vede solo lo sfondo;
- in "Controllo qualità" il certificato aperto dal logo riporta la scadenza del 12/12/2014, e i loghi della finestra "certificati" non aprono documenti.

Abbiamo quindi preparato, di nostra iniziativa, la pagina iniziale di un nuovo sito: la trovate in allegato, da computer e da telefono. È fatta con le Vostre foto e i Vostri dati pubblici, usati solo per questa proposta. Se l'impostazione Vi convince, completeremmo il sito con informazioni e prove, non solo immagini:

- i settori serviti (arredamento, automotive, aviazione), ognuno con le sue pelli, dai kit tagliati su disegno alle pelli ignifughe;
- le certificazioni ICEC e Leather Working Group, con numero, validità e documento scaricabile;
- le prove: il laboratorio interno con le prove fisiche e le norme per le pelli ignifughe (F.A.R. A e B, Classe 1 IM, Crib 5);
- le fasi di lavorazione, dalla pelle grezza alla rifinita, con le foto del reparto;
- italiano, inglese e tedesco, telefono da chiamare con un tocco, vecchi indirizzi collegati ai nuovi.

I testi sono bozze da verificare con Voi: per esempio i titoli, l'aviazione come settore attivo, il referente commerciale, lo stato delle certificazioni, capitale sociale e PEC nel piè di pagina.

Se la proposta Vi interessa, possiamo passare a Montebello per mostrarVela in venti minuti, oppure sentirci al telefono quando preferite. Se invece non Vi interessa, basta rispondere a questo messaggio: cancelliamo l'anteprima e non Vi scriveremo più.

Cordiali saluti,

[Nome Cognome]
[Agenzia]
[telefono] · [email]

## Allegati

| File | Da | Misure | Peso |
|---|---|---|---|
| `ConceriaEuropa-Sito/allegati-mail/conceria-home-computer.jpg` | `_prova/direzioni/giro2/fotografia/proto-1440.png` | 1440 x 4242 px, JPEG qualità 80 | 601.213 byte (0,57 MB) |
| `ConceriaEuropa-Sito/allegati-mail/conceria-home-telefono.jpg` | `_prova/direzioni/giro2/fotografia/proto-390.png` | 390 x 4540 px, JPEG qualità 80 | 256.792 byte (0,24 MB) |

Totale 0,82 MB, ciascun file sotto il limite di 1,5 MB. Si allegano solo i due JPG: non `proto.html`, che prende le
immagini da una cartella locale, ha 18 link segnaposto ("#") e un bottone "Mandateci il vostro capitolato" che apre una
mail vera verso faggiana.luigi@conceriaeuropa.it.

## Variante quando la demo completa è online

Si sostituisce solo il paragrafo che comincia con "Abbiamo quindi preparato" (fino ai due punti prima dell'elenco); il
resto resta uguale. In questo caso i due allegati si possono togliere.

> Abbiamo quindi preparato, di nostra iniziativa, il nuovo sito completo. Potete vederlo qui:
>
> [link]
> Password di accesso: [password]
>
> È un'anteprima privata, non indicizzata sui motori di ricerca, fatta solo con le Vostre foto e i Vostri dati pubblici, usati solo per questa proposta. Il sito comprende informazioni e prove, non solo immagini:

Con la demo online l'elenco va riscritto con ciò che c'è davvero (per esempio il numero di pagine, quali certificati
sono scaricabili, quanti dei 116 indirizzi vecchi sono collegati), e alla riga delle bozze si può aggiungere "Il sito è
pronto: se decidete di acquistarlo, può andare online sul Vostro dominio in pochi giorni" solo se è vero.

## Prima dell'invio (non va nella mail)

### Come sono state verificate le tre osservazioni (7 ottobre 2026)

Script e risultati in `_prova/mail-verifica/`: `verifica.cjs` e `verifica.json`, `ruota.cjs` e `ruota.json`,
screenshot `home-390.png`, `home-1440.png`, `fasi-390.png`, `fasi-1440.png`, `qualita-1440.png`,
`certificati-1440.png`, `ruotato-844x390.png`. Playwright (Chromium) sulla home italiana `index.php?it`, a 390x844
(telefono, tocco) e a 1440x900; nessun modulo, nessun invio.

1. **Telefono.** Nessun meta viewport; a 390 px la pagina è larga 1126 px e viene mostrata in scala 0,346 (circa un
   terzo): il piè di pagina da 10 px si legge a 3,5 px. Nessun link `tel:` in tutta la pagina (0 a 390 e a 1440); anche
   nella finestra contatti il numero è solo testo. Ruotando da 390x844 a 844x390 la pagina si ricarica da
   `index.php?it` (lingua "it") a `index.php` (lingua "en"): curl conferma che `index.php` senza parametro è inglese.
2. **Fasi di lavorazione.** Toccando (390) e cliccando (1440) il riquadro "fasi di lavorazione pelli", la galleria con
   28 foto (elenco `api_images` nel frammento, prima foto `1_grezzo.jpg`) viene creata ma resta sotto lo sfondo:
   contenitore `position: static`, foglio di stile della galleria non caricato; negli screenshot si vede solo la pelle
   beige di copertina.
3. **Certificati.** In "Controllo qualità" il logo apre `pdf/certificato-Page0001.jpg`: certificato ICEC
   CERT-058-1999-QMS-ICEC, ISO 9001:2008, intestato alla s.a.s., "data di scadenza 12.12.2014" (letto oggi sul file).
   L'altro link, "CERTIFICATO QUALITA' pdf", è una targa "We have invested in quality" della s.a.s., senza date visibili. La
   finestra "certificati" ha 8 immagini e 0 link.

### Da dire solo a voce, mai per iscritto

- Cookie di Google Analytics alla prima visita, prima del consenso, con il vecchio tag Universal Analytics
  `UA-42251414-20` (ancora nell'HTML oggi; Google non lo elabora più dal 2023). La privacy del sito (2018) dice che non
  si usano cookie di tracciamento e indica come titolare la s.a.s. (dal 01, 6/10).
- Software fuori supporto: il server risponde `X-Powered-By: PHP/7.4.33` (letto oggi), senza aggiornamenti dal 2022.
  Il sottosito `products.conceriaeuropa.it` gira su WordPress 3.9 e PHP 5.6, con certificato https scaduto
  l'11/12/2025 e una versione vecchia di Revolution Slider (dal 01, 6/10, non riverificato oggi): consigliare un
  controllo del fornitore, senza entrare nei dettagli.
- Il badge Leather Working Group pubblicato nella finestra "certificati" riporta "Expiry date: 13 May 2026" (visto oggi):
  chiedere se è stato rinnovato, non scriverlo.
- Sul certificato del 2014: presentarlo come informazione vecchia rimasta online, non come un'accusa. I loghi in
  "certificati" (ISO 9001:2015, 14001:2015, 45001, TS 406) fanno pensare che i certificati attuali ci siano.
- Il bollino "Scopri" del POR FESR in italiano mostra solo la parola "prova" sopra una mappa (`it/por.php` letto oggi
  con curl); in tedesco "File not found." (dal 01). Le regole dei fondi FESR 2014-2020 chiedono al beneficiario una
  breve descrizione del progetto sul proprio sito: citarlo con cautela, come probabile.
- La dichiarazione di accessibilità dell'azienda (1/7/2026) dice "Parzialmente conforme" con 5 criteri non rispettati:
  il nuovo sito li risolve.
- La galleria delle fasi probabilmente si sistemerebbe anche solo collegando il suo foglio di stile: dirlo, se chiedono,
  per onestà.

### Dati del prototipo da confermare con l'azienda

- Tutti i titoli sono nostri, costruiti dai loro testi: "Dal grezzo al finito" (da "dalla pelle grezza al prodotto
  finito"), "Le pelli entrano salate ed escono finite, nello stesso stabilimento", "Il kit arriva tagliato sul vostro
  disegno", "Per l'imbottito, un fiore che resta naturale", il bottone "Mandateci il vostro capitolato".
- Frasi riscritte da noi: "Siamo tra le poche concerie della zona di Arzignano che fanno tutto il ciclo in casa." (dal
  loro "una delle poche realtà del comprensorio"); "I kit per volanti arrivano pronti per la sellatura"; "La rifinizione
  protegge dall'usura e lascia la mano morbida"; nel piede "Conceria a ciclo completo, fondata nel 1969".
- Aviazione come settore attivo: è nella riga d'apertura e nel piede, ma sul sito principale compare solo negli H1
  nascosti e nella scheda "aviation" con lo stesso testo dell'ignifugo. Vale anche per i settori promessi nella mail.
- Luigi Faggiana come referente dell'Ufficio commerciale (la sua mail è in vista nella sezione contatti del prototipo e
  dietro il bottone).
- Forma e dati legali: "Conceria Europa S.r.l." (sul sito SRL nel piè di pagina, s.a.s. nella privacy e nei
  certificati), "REA VI-107752" (sul sito "VI - 0107752"), "fondata nel 1969 dai fratelli Faggiana" (dal loro testo;
  iscrizione del 25/07/1969 su aziende.it).
- Segnaposto visibili nell'allegato computer e telefono: "capitale sociale [DA CONFERMARE]" (500.000 euro sul sito,
  78.000 nel sottosito) e "PEC [DA CONFERMARE]" nella riga legale del piede. Sono citati nella mail.
- Link segnaposto ("#"): voci del menu laboratorio e azienda, "en" e "de" (le versioni non esistono ancora), "Le fasi di
  lavorazione", "Le pelli per l'automotive", "Le pelli per l'arredamento", nel piede "Certificati", "Politica del
  sistema integrato (PDF)", "Progetto POR FESR 2014-2020", "Dichiarazione di accessibilità", "Privacy", "cookie".
- Stato attuale delle certificazioni (numeri e scadenze ICEC, rinnovo LWG dopo il 13/05/2026): la home non le cita, ma
  la mail promette di mostrarle con numero e validità.
- Norme delle pelli ignifughe (F.A.R. A, F.A.R. B, Classe 1 IM, Crib 5): sul sito sono un "esempio di capitolato".
- Logo: PNG 514x169 del sottosito; la versione bianca del piede l'abbiamo ricavata noi. Serve il vettoriale e il colore
  ufficiale.
- Foto: tutte dell'azienda (metamorfosi, tintura, kit tagliato, pelli piegate, facciata), ritagliate da noi; per lo
  schermo retina servono gli originali senza scritte.
- Testi alternativi delle foto: descrizioni nostre.
- Non promessi nella mail perché non ci sono dati pubblici: clienti, paesi serviti, numeri di produzione, orari.

### Controlli da fare

- Riverificare le tre osservazioni il giorno dell'invio con `node _prova/mail-verifica/verifica.cjs <cartella>` e
  `ruota.cjs`: se una non è più vera, toglierla o sostituirla (per esempio con il POR FESR "prova").
- Compilare [Nome Cognome], [Agenzia], [telefono] e [email]. La mail parte dal committente, non da noi.
- Se si usa la PEC: verificarla prima su INI-PEC.
- Aprire i due JPG dal telefono prima di inviarli: sono pagine lunghe (4242 e 4540 px) e vanno scorse.
- Non scrivere né dire che il sito completo è pronto: esiste solo la pagina iniziale. Decidere tempi e prezzo prima
  dell'eventuale incontro.
- Per la visita a Montebello (Via Lungochiampo 129): orari non pubblicati, telefonare prima.
- Quando la demo sarà online: password, nessuna indicizzazione, e attenzione ai link mailto e a un eventuale modulo, che
  non devono scrivere davvero all'azienda.
- Non citare "da oltre 40 anni" del sito attuale (dal 1969 sono 57) e non usare parole da agenzia.
