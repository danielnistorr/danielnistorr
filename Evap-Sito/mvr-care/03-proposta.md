# Proposta, versione 2: landing page "MVR CARE"

La prima versione (pagina di servizio nello stile del sito) è stata approvata nella struttura. Il cliente, Roberto di EVAP, ha chiesto di trasformarla in una **landing page commerciale** che si possa anche sponsorizzare, con l'identità grafica della brochure. Questa è la versione 2. Le sue richieste esplicite prevalgono sui vincoli di design generali: per questo ora ci sono l'onda blu e verde della brochure, le icone dei tre punti della copertina e dei benefici, gli spigoli arrotondati delle schede.

- Testi: solo dalla brochure (`01-contenuti.md`) e dal messaggio del cliente (stesso file, ultima sezione). Telefono ed email dal sito.
- Anteprima: `anteprima/index.html`; schermate `screenshot/anteprima-1440.jpg` e `screenshot/anteprima-390.jpg`. Variante con lo schema facoltativo: `anteprima/variante-schema.html`.
- Modelli di Elementor: `elementor/mvr-care-template.json` (la pagina) e `elementor/mvr-care-grazie-template.json` (pagina di ringraziamento facoltativa).
- Principio dei testi, dalle parole del cliente: MVR CARE non è un costo aggiuntivo di assistenza, è un investimento programmato per ridurre il rischio di inefficienze e interruzioni produttive. La brochure resta il riferimento visivo e tecnico; la pagina ne sviluppa il messaggio e porta al contatto.

## Indirizzo, menu, titolo

- **Indirizzo**: `/servizi/mvr-care/`; pagina di ringraziamento `/servizi/mvr-care/grazie/`.
- **Menu**: voce "MVR CARE" sotto "Servizi" (l'anteprima la mostra). Per le campagne sponsorizzate l'indirizzo da usare è lo stesso, eventualmente con `?formula=pure` o `?formula=plus` (vedi "Formula già scelta").
- **Titolo SEO**: `MVR CARE: assistenza programmata per il tuo evaporatore MVR | EVAP`
- **Meta description** (153 caratteri): `MVR CARE è l'assistenza EVAP per il tuo evaporatore MVR: visite programmate e controllo remoto settimanale. Richiedi la tua proposta e una call gratuita.`

## Struttura e testi completi

Il bottone è sempre lo stesso, in tutta la pagina: **"Richiedi la tua proposta MVR CARE"**, verde a pillola, e porta alla sezione `#richiedi-proposta` con il modulo.

### 1. Apertura chiara, come la copertina

Fondo azzurro chiarissimo (il cielo della copertina, senza sfumatura). A sinistra il testo, a destra il ritaglio dell'impianto dalla copertina della brochure (autorizzato dal cliente) in una cornice con gli angoli arrotondati, a misura vera o poco più (342 x 408 px mostrati a 428 x 510). In fondo l'onda verde, poi la fascia blu.

- **H1**: MVR CARE
- **Pay off**: Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.
- **Bottone**: Richiedi la tua proposta MVR CARE
- **Sotto il bottone**: Fissa una call gratuita con i nostri tecnici per una consulenza di diagnosi gratuita e senza impegno.

**Fascia blu con i tre punti della copertina**, con le icone della brochure (ingranaggio, grafico che sale, foglia) e i filetti verticali: Continuità di produzione / Prestazioni costanti / Efficienza e sostenibilità.

### 2. Perché conta (slide 2)

Testo a sinistra, foto vera di un evaporatore EVAP a destra; sotto, il riquadro azzurro dei benefici con le icone e i filetti verdi, come nella brochure.

- **H2**: Un evaporatore efficiente è il cuore della tua produttività
- **Testo introduttivo**: L'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione degli effluenti industriali.
- **Testo**: Per garantirne nel tempo la massima efficienza e continuità operativa, EVAP ha sviluppato **MVR CARE**: il servizio di assistenza tecnica dedicato ai suoi clienti.
- **Riquadro verde chiaro** (parole del cliente): MVR CARE non è un costo aggiuntivo di assistenza: è un investimento programmato per ridurre il rischio di inefficienze e interruzioni produttive.
- **Benefici** (icone fabbrica, bersaglio, monete): Evita fermi impianto imprevisti / Mantiene le performance progettuali / Riduce i costi operativi nel tempo.

### 3. Controllo, prevenzione, performance (slide 3, la sezione del monitoraggio)

Fondo azzurro chiarissimo. A sinistra le quattro attività con le icone verdi della brochure (monitor, lente, ingranaggio, grafico) e i filetti; a destra la **schermata "MVR Monitoring" ricostruita** in un portatile disegnato, e sotto il dato grande.

- **H2**: Controllo, prevenzione, performance: sempre sotto controllo
- **Monitoraggio e verifiche** periodiche dei principali parametri operativi.
- **Diagnosi preventiva** e individuazione tempestiva di eventuali criticità.
- **Interventi mirati** per mantenere massima efficienza, sicurezza e affidabilità.
- **Report e raccomandazioni** per l'ottimizzazione dell'esercizio.
- **Bottone**: Richiedi la tua proposta MVR CARE
- **Schermata** (disegno SVG, nitido a ogni misura, stessi elementi e colori della brochure): logo EVAP della loro libreria media, "MVR Monitoring", foto vera di un impianto EVAP, "Consumo specifico **28 kWh/m³**" grande in verde, "Impianto in esercizio" con la spunta, grafico a barre verdi senza numeri sugli assi. Sul telefono e sul tablet la stessa schermata senza il portatile, in colonna.
- **Dato grande**: **28 kWh/m³**, didascalia "consumo specifico".
- **Didascalia**: Controllo remoto settimanale dei principali parametri operativi. (Così la schermata non fa pensare a un monitoraggio continuo.)

**Il dato "28 kWh/m³" va confermato da EVAP, parola per parola**, prima di pubblicare: in una pagina sponsorizzata dev'essere esatto. Da chiedere: è un valore misurato o "fino a"? È riferito a un impianto tipo, a un impianto preciso o a una media? In quali condizioni (tipo di effluente, portata)? Si può scrivere accanto una nota con il riferimento? Finché non c'è risposta, il dato resta in pagina come lo vuole il cliente, ma è il primo punto della lista di conferme in `LEGGIMI.md`. Anche il nome "MVR Monitoring" va confermato (è il nome di un loro strumento o solo un titolo della brochure?).

### 4. Le due formule, come due proposte

Due schede d'offerta affiancate, come nella brochure: **PURE in azzurro chiaro**, **PLUS in verde chiaro**, con il nome grande, la loro linea dell'anno, le voci della brochure con le spunte verdi su un riquadro bianco e il loro bottone. "A chi si rivolge" non c'è: la brochure non lo dice.

- **H2**: Scegli il livello di servizio più adatto alle tue esigenze
- **Testo**: Due formule flessibili, con la qualità e l'esperienza EVAP.
- **Scheda MVR CARE PURE**: linea dell'anno con 4 visite e 52 controlli settimanali; ✓ **4 visite tecniche programmate all'anno** ✓ **1 controllo remoto ogni settimana** ✓ Verifica dello stato di esercizio e manutenzione ✓ Segnalazione anomalie e azioni raccomandate ✓ Rapporto sintetico di verifica; bottone "Richiedi la tua proposta MVR CARE" con la formula PURE già scelta nel modulo.
- **Scheda MVR CARE PLUS**: linea dell'anno con 12 visite, 52 controlli settimanali e 12 rapporti mensili; ✓ **12 visite tecniche programmate all'anno** ✓ **1 controllo remoto ogni settimana** ✓ Verifica dello stato di esercizio e manutenzione ✓ Analisi anomalie e perdite di produttività ✓ Rapporto tecnico mensile; bottone con la formula PLUS già scelta.
- **Legenda** sotto le schede: Controllo remoto, 1 ogni settimana / Visita tecnica programmata / Rapporto tecnico mensile (PLUS). Nota: "Le date delle visite sono indicative: si concordano con il cliente." (da confermare).

La linea dell'anno è rimasta, ma **dentro ogni scheda** invece che in un grafico separato: così non appesantisce e il 4 contro 12 si vede accostando le due schede. Le visite PURE sono disegnate a intervalli regolari perché la brochure non dice quando si fanno; il rapporto sintetico di PURE non ha una frequenza e quindi non ha tacche.

**Formula già scelta.** I bottoni delle schede portano a `?formula=pure#richiedi-proposta` e `?formula=plus#richiedi-proposta`. Poche righe di JavaScript (widget HTML accanto al modulo, `elementor/grafici/modulo-formula.html`) leggono il parametro e scelgono la formula nel campo "Formula di interesse". Funziona anche dalle campagne: un annuncio può portare direttamente a `https://evap.it/servizi/mvr-care/?formula=plus#richiedi-proposta`.

### 5. Richiesta del canone e modulo (ancora `#richiedi-proposta`)

La chiusura commerciale più importante. Fascia blu scura con l'onda verde in alto e la foglia, come la fine della slide 4; sotto, il modulo su un riquadro bianco che sale sulla fascia.

- **H2**: Scopri il canone a te riservato, **particolarmente vantaggioso.** (le ultime due parole nella pillola verde, come nella brochure)
- **Testo**: Ogni evaporatore ha caratteristiche ed esigenze operative specifiche. Scopri la formula MVR CARE più adatta al tuo impianto e richiedi una proposta economica personalizzata, senza impegno.
- **Bottone**: Richiedi la tua proposta MVR CARE (porta al modulo)
- **Accanto al modulo**: **Fissa una call gratuita con i nostri tecnici** / Una consulenza di diagnosi gratuita e senza impegno, finalizzata alla quotazione del servizio MVR CARE per il tuo impianto. / Preferisci telefonare? +39 0444 1276355. Oppure scrivi a tecnico2@evap.it
- **Modulo** (widget Modulo di Elementor Pro, nome "Richiesta proposta MVR CARE"). Campi, con l'ID da usare:

| ID | Etichetta | Tipo | Obbligatorio | Opzioni |
|---|---|---|---|---|
| `nome` | Nome e cognome | testo | sì | |
| `azienda` | Azienda | testo | sì | |
| `ruolo` | Ruolo | testo | no | |
| `email` | Email | email | sì | |
| `telefono` | Telefono | telefono | sì | |
| `evaporatore` | Hai già un evaporatore MVR? | elenco | no | Sì, EVAP / Sì, di un altro costruttore / No, sto valutando |
| `settore` | Settore o tipo di effluente | testo | no | |
| `capacita` | Capacità dell'impianto (m³/giorno), facoltativo | numero | no | |
| `anno` | Anno di installazione, facoltativo | numero | no | da 1950 a 2100 |
| `formula` | Formula di interesse | elenco | no | PURE / PLUS / Non so, consigliatemi |
| `esigenza` | Esigenza principale | elenco | no | Evitare fermi impianto / Mantenere le prestazioni / Ridurre i costi operativi / Altro |
| `fascia` | Fascia oraria preferita per la call | elenco | no | Mattina / Pomeriggio / Indifferente |
| `messaggio` | Messaggio | area di testo | no | |
| `privacy` | Ho letto l'informativa privacy (collegamento a https://evap.it/privacy-policy/) e acconsento al trattamento dei miei dati per essere ricontattato. | accettazione | sì | |

  - **Pulsante**: Fissa la call di diagnosi gratuita
  - **Azioni dopo l'invio**: email a **tecnico2@evap.it** (da confermare), oggetto "Richiesta proposta MVR CARE dal sito evap.it", contenuto `[all-fields]`, "Rispondi a" l'email di chi scrive; raccolta nelle "Submissions" di Elementor.
  - **Messaggio di conferma**: Grazie, abbiamo ricevuto la tua richiesta. I tecnici EVAP ti contatteranno per fissare la call di diagnosi gratuita e senza impegno.
  - **Pagina di ringraziamento (facoltativa, per misurare le conversioni)**: l'indirizzo `https://evap.it/servizi/mvr-care/grazie/` è già scritto nel modulo; basta aggiungere l'azione "Reindirizzamento" e creare la pagina dal secondo modello (istruzioni in `LEGGIMI.md`). Testo della pagina: "Grazie, abbiamo ricevuto la tua richiesta" / "I tecnici EVAP ti contatteranno per fissare la call di diagnosi gratuita e senza impegno sul tuo evaporatore MVR." / recapiti / bottone "Torna a MVR CARE".
  - Le opzioni di "Fascia oraria" sono generiche (nessun orario di EVAP inventato): se EVAP preferisce fasce precise, si cambiano nel modulo.

### 6. Domande frequenti

Restano, con il tono nuovo, e chiariscono i limiti tecnici (controllo settimanale, non continuo).

- **Che differenza c'è tra PURE e PLUS?** Entrambe comprendono un controllo remoto ogni settimana e la verifica dello stato di esercizio e manutenzione. PURE prevede 4 visite tecniche programmate all'anno, la segnalazione delle anomalie con le azioni raccomandate e un rapporto sintetico di verifica. PLUS prevede 12 visite tecniche programmate all'anno, l'analisi delle anomalie e delle perdite di produttività e un rapporto tecnico mensile.
- **Il controllo remoto è continuo?** No: in entrambe le formule è previsto un controllo remoto ogni settimana dei principali parametri operativi, insieme alle visite tecniche programmate (4 all'anno con PURE, 12 con PLUS).
- **Cosa succede dopo la richiesta?** Fissiamo una call gratuita con i nostri tecnici: una consulenza di diagnosi gratuita e senza impegno, per individuare la formula MVR CARE più adatta al tuo impianto e prepararti una proposta economica personalizzata.
- **Quanto costa MVR CARE?** Il canone è riservato e particolarmente vantaggioso, e dipende dalle caratteristiche e dalle esigenze operative del tuo evaporatore. Richiedi la tua proposta personalizzata (collegamento al modulo), senza impegno.

La domanda "A chi è rivolto MVR CARE?" della prima versione è stata tolta: la brochure dice "dedicato ai propri clienti", mentre il modulo voluto dal cliente accetta anche impianti di altri costruttori. Va chiarito (vedi `LEGGIMI.md`).

## Controllo tecnico dei testi (punto 5 del cliente)

Ogni frase è stata riletta con questo filtro:
- visite: 4 (PURE) e 12 (PLUS) all'anno, "programmate"; controllo remoto: 1 ogni settimana, in entrambe;
- **nessun monitoraggio continuo**: la parola "monitoraggio" compare solo come nella brochure ("Monitoraggio e verifiche periodiche"); la schermata ha la didascalia "Controllo remoto settimanale"; una domanda frequente lo dice esplicitamente;
- **nessuna riparazione inclusa**: "Interventi mirati" è la frase della brochure, senza aggiungere che siano compresi nel canone;
- **nessun tempo d'intervento**: nessuna frase con tempi, reperibilità o "subito"; "ti contatteranno" non ha tempi;
- nessun numero oltre a quelli della brochure (4, 12, 1 a settimana, 52 tacche come conseguenza di "ogni settimana") e al dato di consumo specifico chiesto dal cliente e da confermare.

## Identità grafica

Colori della brochure, presi con un contagocce dalle immagini delle slide (mediana dei pixel pieni):

| Uso | Colore | Da dove |
|---|---|---|
| Titoli | `#070D57` | titoli delle slide 2-4 (`#030853`; "MVR CARE" in copertina `#02238C`) |
| Nome PURE | `#06316C` | slide 4 |
| Nome PLUS, riquadro della frase del cliente | `#0A5B2B` | slide 4 |
| Fascia blu dei tre punti | `#0054A0` | parte chiara della fascia, slide 4 |
| Fascia blu della chiusura | `#003868` | parte scura della fascia, slide 4 |
| Onda verde e filetti sotto i titoli | `#49A108` | onda della copertina |
| Bottoni | `#2B880A` | pillola "particolarmente vantaggioso" (`#2F9F00`) scurita quanto basta per il testo bianco (contrasto 4,5:1) |
| Spunte e icone verdi | `#138D2D` | slide 4 e slide 3 |
| Barre del grafico, dato "28" | `#5EBB15`, `#057905` | schermata della slide 3 |
| Scheda PURE / scheda PLUS | `#E0F0FC` / `#E8F8E4` | slide 4 |
| Riquadro dei benefici | `#E4F0F4` | slide 2 |
| Fondo chiaro di apertura e monitoraggio | `#F2F8FE` | cielo della copertina, senza sfumatura |
| Testo | colore globale del kit (`#4F5D72`) | sito |

- **Carattere**: Plus Jakarta Sans, quello del sito; titoli a peso 800 nel navy della brochure (H1 104/80/56 px, H2 44/38/31 px), testo con il carattere globale del kit. Il carattere del sito oggi non si carica (vedi `02-design-sito.md` e `LEGGIMI.md`): finché non si sistema, anche la landing si vedrà in Arial/Helvetica.
- **Forme**: schede, riquadri e foto con angoli arrotondati (24 e 16 px) come nella brochure; bottoni a pillola; onde fatte con il divisore "Waves" di Elementor in colore pieno (niente sfumature).
- **Restano dai vincoli generali**: niente animazioni o dissolvenze, niente effetti col cursore, bottoni che si invertono di colpo (verde, poi navy), niente ombre, niente etichette sopra i titoli, nessun carattere U+2014.
- **Testata e piede** restano quelli del sito: la landing è una pagina di evap.it.

## Immagini

| Dove | Immagine | Stato |
|---|---|---|
| Apertura | ritaglio dell'impianto dalla copertina della brochure, `anteprima/img/brochure-copertina-impianto.jpg` (342 x 408 px) | autorizzato dal cliente; nel modello è un segnaposto: va caricato nella libreria media e scelto (istruzioni nel LEGGIMI). In futuro: immagine generata dal cliente con i prompt di `PROMPT-IMMAGINI.md` |
| Perché conta | foto vera EVAP, `/wp-content/uploads/2025/10/IMG_7517-768x1024.jpg` | dalla loro libreria |
| Schermata "MVR Monitoring" | logo dalla libreria (`05e4e93b...-150x150.png`) e foto vera `IMG_9042-768x576.jpg` dentro il disegno | dalla loro libreria |

La foto scura dell'officina in testa (versione 1) è stata tolta, come chiesto. Le altre illustrazioni della brochure (manometro, laptop originale) non sono usate: vedi `ILLUSTRAZIONI-BROCHURE.md`.

## Schema facoltativo "Come funziona un evaporatore MVR"

Resta nella variante `anteprima/variante-schema.html`, dopo la sezione del monitoraggio, e va controllato da un tecnico EVAP prima di pubblicarlo. Codice pronto in `elementor/grafici/schema-mvr-facoltativo.html`.

## Grafici di consumi e risparmi

Oltre al dato "28 kWh/m³" voluto dal cliente, la pagina non mostra grafici di consumi, risparmi o percentuali: la brochure non ne ha e un grafico con valori di esempio sembrerebbe una promessa. Per farli con dati veri servono da EVAP: un report vero di MVR CARE anche anonimizzato, i consumi specifici medi reali degli impianti seguiti (prima e dopo gli interventi, con la fonte), i fermi impianto evitati o ridotti, e il permesso di pubblicarli.
