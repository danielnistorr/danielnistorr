# Proposta, versione 3: landing page "MVR CARE" in stile sito

Storia: la versione 1 era una pagina di servizio nello stile del sito; il cliente, Roberto di EVAP, ha chiesto una **landing page commerciale** da poter anche sponsorizzare (versione 2, con l'identità grafica della brochure); vista la v2 ha chiesto di farla "così ma più in stile sito web". La **versione 3** tiene tutto della v2 (contenuti, ordine delle sezioni, inviti all'azione, modulo, coerenza tecnica) e cambia la veste: quella del sito evap.it, con due soli accenti della brochure. La v2 resta come alternativa.

## Le due versioni

| | **Versione 3, in stile sito** (principale) | Versione 2, "brochure" (alternativa) |
|---|---|---|
| Anteprima | `anteprima/index.html` | `anteprima/variante-brochure.html` |
| Schermate | `screenshot/anteprima-1440.jpg`, `-390.jpg` | `screenshot/variante-brochure-1440.jpg`, `-390.jpg` |
| Modello Elementor | `elementor/mvr-care-template.json` (lo scrive `genera_template.py`) | `elementor/mvr-care-template-brochure.json` (lo scrive `genera_template_brochure.py`) |
| Base visiva | kit del sito: titoli a peso 600, bottoni del sito (azzurro, spigoli vivi, 15/30 px), 1290 px, 100 px tra le sezioni, filetti sottili, riquadri a spigoli vivi | colori e forme della brochure: titoli a peso 800, bottoni verdi a pillola, angoli arrotondati |
| Apertura | fondo grigio chiarissimo del sito, immagine in cornice sottile, tre punti in una riga con filetti e icone lineari verdi | fondo azzurro, onda verde, fascia blu piena con i tre punti e le icone piene |
| Perché conta | frase del cliente sotto un filetto verde, benefici in una riga con filetti | frase in un riquadro verde chiaro, benefici in un riquadro azzurro |
| Monitoraggio | schermata del portatile, "28 kWh/m³" in verde peso 600 sopra un filetto | stessa schermata, numero a peso 800 |
| PURE e PLUS | schede bianche con bordo sottile e barra in alto (azzurro del sito PURE, verde PLUS), stesso peso | schede piene azzurro chiaro e verde chiaro |
| Canone e modulo | fascia blu del sito con la cornice bianca di 20 px (come "Qualità ed Affidabilità" in home), testo a sinistra, modulo su riquadro bianco a destra, campi del kit | fascia blu scura con onda verde, foglia e pillola verde, modulo su riquadro arrotondato |
| Accenti della brochure | navy dei titoli (`#070D57`), verde per spunte, icone, filetto della frase e scheda PLUS | tutta la palette |

Variante con lo schema facoltativo "Come funziona un evaporatore MVR": `anteprima/variante-schema.html` (versione 3).

- Testi: solo dalla brochure (`01-contenuti.md`) e dal messaggio del cliente (stesso file, ultima sezione). Telefono ed email dal sito.
- Modelli di Elementor: `elementor/mvr-care-template.json` (la pagina, v3), `elementor/mvr-care-grazie-template.json` (pagina di ringraziamento facoltativa, v3), `elementor/mvr-care-template-brochure.json` (la v2).
- Principio dei testi, dalle parole del cliente: MVR CARE non è un costo aggiuntivo di assistenza, è un investimento programmato per ridurre il rischio di inefficienze e interruzioni produttive.

## Indirizzo, menu, titolo

- **Indirizzo**: `/servizi/mvr-care/`; pagina di ringraziamento `/servizi/mvr-care/grazie/`.
- **Menu**: voce "MVR CARE" sotto "Servizi" (l'anteprima la mostra). Per le campagne sponsorizzate l'indirizzo da usare è lo stesso, eventualmente con `?formula=pure` o `?formula=plus` (vedi "Formula già scelta").
- **Titolo SEO**: `MVR CARE: assistenza programmata per il tuo evaporatore MVR | EVAP`
- **Meta description** (153 caratteri): `MVR CARE è l'assistenza EVAP per il tuo evaporatore MVR: visite programmate e controllo remoto settimanale. Richiedi la tua proposta e una call gratuita.`

## Struttura e testi completi

Il bottone è sempre lo stesso, in tutta la pagina: **"Richiedi la tua proposta MVR CARE"** (nella v3 il bottone del sito, nella v2 verde a pillola), e porta alla sezione `#richiedi-proposta` con il modulo.

### 1. Apertura

Fondo grigio chiarissimo del sito (`#F5F6F8`). A sinistra il testo, a destra il ritaglio dell'impianto dalla copertina della brochure (autorizzato dal cliente) in una cornice con un filetto sottile, a misura vera o poco più (342 x 408 px mostrati a 428 x 510). Sotto, i tre punti della copertina in una riga con un filetto sopra, filetti verticali tra le voci e piccole icone lineari verdi (orologio, grafico, lampadina: Font Awesome "regular", le sole lineari di Elementor gratuito). Nella v2: fondo azzurro, onda verde e fascia blu piena.

- **H1**: MVR CARE
- **Pay off**: Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.
- **Bottone**: Richiedi la tua proposta MVR CARE
- **Sotto il bottone**: Fissa una call gratuita con i nostri tecnici per una consulenza di diagnosi gratuita e senza impegno.

**I tre punti della copertina**: Continuità di produzione / Prestazioni costanti / Efficienza e sostenibilità.

### 2. Perché conta (slide 2)

Testo a sinistra, foto vera di un evaporatore EVAP a destra; sotto, i benefici in una riga con filetti e icone lineari verdi (calendario, bersaglio, banconota). Nella v2: riquadro azzurro con icone piene.

- **H2**: Un evaporatore efficiente è il cuore della tua produttività
- **Testo introduttivo**: L'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione degli effluenti industriali.
- **Testo**: Per garantirne nel tempo la massima efficienza e continuità operativa, EVAP ha sviluppato **MVR CARE**: il servizio di assistenza tecnica dedicato ai suoi clienti.
- **Frase del cliente** (sotto un filetto verde di 3 px, 21 px peso 600; nella v2 in un riquadro verde chiaro): MVR CARE non è un costo aggiuntivo di assistenza: è un investimento programmato per ridurre il rischio di inefficienze e interruzioni produttive.
- **Benefici**: Evita fermi impianto imprevisti / Mantiene le performance progettuali / Riduce i costi operativi nel tempo.

### 3. Controllo, prevenzione, performance (slide 3, la sezione del monitoraggio)

Fondo grigio chiarissimo del sito. A sinistra le quattro attività con icone lineari verdi (occhio, appunti, salvagente, documento) tra filetti sottili; a destra la **schermata "MVR Monitoring" ricostruita** in un portatile disegnato (è già un elemento da web e resta uguale nelle due versioni), e sotto, oltre un filetto, il dato grande.

- **H2**: Controllo, prevenzione, performance: sempre sotto controllo
- **Monitoraggio e verifiche** periodiche dei principali parametri operativi.
- **Diagnosi preventiva** e individuazione tempestiva di eventuali criticità.
- **Interventi mirati** per mantenere massima efficienza, sicurezza e affidabilità.
- **Report e raccomandazioni** per l'ottimizzazione dell'esercizio.
- **Bottone**: Richiedi la tua proposta MVR CARE
- **Schermata** (disegno SVG, nitido a ogni misura, stessi elementi e colori della brochure): logo EVAP della loro libreria media, "MVR Monitoring", foto vera di un impianto EVAP, "Consumo specifico **28 kWh/m³**" grande in verde, "Impianto in esercizio" con la spunta, grafico a barre verdi senza numeri sugli assi. Sul telefono e sul tablet la stessa schermata senza il portatile, in colonna.
- **Dato grande**: **28 kWh/m³** (in verde, peso 600, con l'unità più piccola), didascalia "consumo specifico".
- **Didascalia**: Controllo remoto settimanale dei principali parametri operativi. (Così la schermata non fa pensare a un monitoraggio continuo.)

**Il dato "28 kWh/m³" va confermato da EVAP, parola per parola**, prima di pubblicare: in una pagina sponsorizzata dev'essere esatto. Da chiedere: è un valore misurato o "fino a"? È riferito a un impianto tipo, a un impianto preciso o a una media? In quali condizioni (tipo di effluente, portata)? Si può scrivere accanto una nota con il riferimento? Finché non c'è risposta, il dato resta in pagina come lo vuole il cliente, ma è il primo punto della lista di conferme in `LEGGIMI.md`. Anche il nome "MVR Monitoring" va confermato (è il nome di un loro strumento o solo un titolo della brochure?).

### 4. Le due formule, come due proposte

Due schede d'offerta affiancate, **con lo stesso peso visivo** (nessuna "consigliata": la brochure non lo dice): fondo bianco, bordo sottile, **barra in alto azzurra (colore del sito) per PURE e verde per PLUS**, nome grande, la loro linea dell'anno compatta, le voci della brochure con le spunte verdi tra filetti e il bottone del sito. "A chi si rivolge" non c'è: la brochure non lo dice. Nella v2: schede piene azzurro chiaro e verde chiaro con il riquadro bianco interno.

- **H2**: Scegli il livello di servizio più adatto alle tue esigenze
- **Testo**: Due formule flessibili, con la qualità e l'esperienza EVAP.
- **Scheda MVR CARE PURE**: linea dell'anno con 4 visite e 52 controlli settimanali; ✓ **4 visite tecniche programmate all'anno** ✓ **1 controllo remoto ogni settimana** ✓ Verifica dello stato di esercizio e manutenzione ✓ Segnalazione anomalie e azioni raccomandate ✓ Rapporto sintetico di verifica; bottone "Richiedi la tua proposta MVR CARE" con la formula PURE già scelta nel modulo.
- **Scheda MVR CARE PLUS**: linea dell'anno con 12 visite, 52 controlli settimanali e 12 rapporti mensili; ✓ **12 visite tecniche programmate all'anno** ✓ **1 controllo remoto ogni settimana** ✓ Verifica dello stato di esercizio e manutenzione ✓ Analisi anomalie e perdite di produttività ✓ Rapporto tecnico mensile; bottone con la formula PLUS già scelta.
- **Legenda** sotto le schede: Controllo remoto, 1 ogni settimana / Visita tecnica programmata / Rapporto tecnico mensile (PLUS). Nota: "Le date delle visite sono indicative: si concordano con il cliente." (da confermare).

La linea dell'anno è rimasta, ma **dentro ogni scheda** invece che in un grafico separato: così non appesantisce e il 4 contro 12 si vede accostando le due schede. Le visite PURE sono disegnate a intervalli regolari perché la brochure non dice quando si fanno; il rapporto sintetico di PURE non ha una frequenza e quindi non ha tacche.

**Formula già scelta.** I bottoni delle schede portano a `?formula=pure#richiedi-proposta` e `?formula=plus#richiedi-proposta`. Poche righe di JavaScript (widget HTML accanto al modulo, `elementor/grafici/modulo-formula.html`) leggono il parametro e scelgono la formula nel campo "Formula di interesse". Funziona anche dalle campagne: un annuncio può portare direttamente a `https://evap.it/servizi/mvr-care/?formula=plus#richiedi-proposta`.

### 5. Richiesta del canone e modulo (ancora `#richiedi-proposta`)

La chiusura commerciale più importante. **Fascia blu del sito** (`#1D365C`, colore globale "primary") con la cornice bianca di 20 px, come la fascia "Qualità ed Affidabilità" della home: a sinistra titolo, testo di Roberto, bottone (azzurro, al passaggio bianco) e la proposta della call; a destra il modulo su un riquadro bianco, con i campi del kit del sito (bordo 1 px, spigoli vivi) e il bottone del sito. Nessuna decorazione da stampa. Nella v2: fascia blu scura con onda, foglia e pillola verde.

- **H2**: Scopri il canone a te riservato, particolarmente vantaggioso. (nella v2 le ultime due parole erano nella pillola verde)
- **Testo**: Ogni evaporatore ha caratteristiche ed esigenze operative specifiche. Scopri la formula MVR CARE più adatta al tuo impianto e richiedi una proposta economica personalizzata, senza impegno.
- **Bottone**: Richiedi la tua proposta MVR CARE (porta al modulo)
- **Sotto il bottone, oltre un filetto**: **Fissa una call gratuita con i nostri tecnici** / Una consulenza di diagnosi gratuita e senza impegno, finalizzata alla quotazione del servizio MVR CARE per il tuo impianto. / Preferisci telefonare? +39 0444 1276355. Oppure scrivi a tecnico2@evap.it
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

## Veste grafica della versione 3

- **Base del sito** (kit 11, vedi `02-design-sito.md`): Plus Jakarta Sans; H1 80/60/44 px e H2 38/35/30 px a **peso 600** come le altre pagine, senza maiuscole iniziali su ogni parola; testo con i caratteri e il colore globali; bottoni del sito (azzurro `#3798E2`, testo bianco 16 px peso 500, 15/30 px, spigoli vivi; al passaggio blu del sito `#1D365C`, sul fondo blu bianco con testo blu, di colpo); contenuto largo 1290 px; 100 px tra le sezioni (60 sul telefono); fondo grigio chiarissimo `#F5F6F8` alternato al bianco; filetti 1 px `#1D365C26`; riquadri a spigoli vivi, nessuna ombra; fascia blu con la cornice bianca di 20 px per la chiusura.
- **Accenti della brochure**: navy dei titoli `#070D57`; verde per le spunte e le icone `#138D2D`, per la barra della scheda PLUS e il filetto della frase del cliente `#2B880A`, per il dato "28 kWh/m³" `#057905`.
- **Bottone senza maiuscole iniziali**: il kit del sito mette le maiuscole a ogni parola dei bottoni; qui no, perché "Richiedi la tua proposta MVR CARE" è la frase del cliente (in Elementor: Tipografia > Trasforma "Nessuna").
- **Icone lineari**: Font Awesome "regular" della libreria di Elementor gratuito (contorno), piccole (26 px), verdi.
- **Esclusi**: onde, fasce sagomate, foglia, evidenziatore a pillola, gradienti, ombre, animazioni, dissolvenze, effetti col cursore, etichette sopra i titoli, carattere U+2014.
- **Testata e piede** del sito.

## Veste della versione 2 "brochure" (alternativa)

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
