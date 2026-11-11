# Proposta: pagina "MVR CARE" su evap.it

Pagina nuova per il servizio di assistenza MVR CARE, con le formule PURE e PLUS. Contenuti solo dalla brochure del cliente (`01-contenuti.md`) e dal sito (telefono ed email dei contatti). Design ricavato dal sito (`02-design-sito.md`).

- Anteprima: `anteprima/index.html` (testata e piede veri del sito, caratteri e colori del kit). Schermate: `screenshot/anteprima-1440.jpg`, `screenshot/anteprima-390.jpg`.
- Modello di Elementor: `elementor/mvr-care-template.json` (provato in WordPress 7.1.4 + Hello Elementor + Elementor 3.31.5: `screenshot/prova-wordpress/`).

## Indirizzo, menu, titolo

- **Indirizzo consigliato: `/servizi/mvr-care/`** (pagina "MVR CARE" con genitore "Servizi"). Tiene il servizio dentro i servizi, come si aspetta chi arriva dal menu, e lascia libero `/mvr-care/` se un giorno servisse una pagina di campagna. Se il cliente preferisce un indirizzo corto da stampare sulla brochure, `/mvr-care/` va bene lo stesso: cambia solo il genitore.
- **Menu**: voce "MVR CARE" **sotto "Servizi"**, come "Life Struvite" sta sotto "Progetti" (il menu JKit mostra la freccia e il sottomenu da solo). L'anteprima mostra già questa voce. In più, se il cliente vuole: un bottone "MVR CARE" in fondo al riquadro "Altri servizi" della pagina Servizi, e il collegamento dalla scheda "Assistenza Post-Vendita" della home.
- **Titolo SEO** (47 caratteri): `MVR CARE: assistenza per evaporatori MVR | EVAP`
- **Meta description** (150 caratteri): `MVR CARE è l'assistenza EVAP per il tuo evaporatore MVR: visite tecniche programmate, controllo remoto ogni settimana e rapporti. Formule PURE e PLUS.`
- Il sito non ha un plugin SEO: senza, WordPress mostra "MVR CARE – EVAP" come titolo e nessuna description. Vedi `LEGGIMI.md`.

## Struttura e testi, in ordine

Tono: "tu", come la brochure e la home ("I tuoi costi di smaltimento..."). Correzioni rispetto alla brochure, tutte senza fatti nuovi: punteggiatura del titolo della slide 3 ("performance: sempre sotto controllo"), articoli aggiunti ("Evita i fermi impianto imprevisti", "Segnalazione delle anomalie"), "ai propri clienti" diventa "ai suoi clienti", "programmate/anno" diventa "all'anno".

### 1. Apertura (H1)

Foto vera di un impianto EVAP con la velatura blu del sito, nella cornice bianca di 20 px. Testo allineato a sinistra.

- **H1**: MVR CARE
- **Testo**: Il servizio di assistenza EVAP per la massima affidabilità del tuo evaporatore MVR.
- **Bottone**: "Richiedi il canone" verso /contattaci/
- **Collegamento**: "Le due formule" verso `#formule` (la tabella più sotto)
- **Tre punti** in fondo alla foto, separati da filetti (niente icone): Continuità di produzione / Prestazioni costanti / Efficienza e sostenibilità

Niente briciole di pane "Home → Servizi → MVR CARE" sotto il titolo: in questa apertura starebbero tra il titolo e la frase. Se il cliente le vuole come nelle altre pagine, si aggiunge un Elenco icone sotto la frase (stesso stile del banner di Servizi).

### 2. Perché conta

Foto a sinistra (evaporatore EVAP con il quadro di controllo), testo a destra: come "Scopri perché EVAP" in home.

- **H2**: Un evaporatore efficiente è il cuore della tua produttività
- **Testo introduttivo** (18 px): L'evaporatore MVR è un impianto strategico per il trattamento e la valorizzazione degli effluenti industriali.
- **Testo**: Per garantirne nel tempo la massima efficienza e la continuità operativa, EVAP ha sviluppato MVR CARE: il servizio di assistenza tecnica dedicato ai suoi clienti.
- **Elenco** con quadratini azzurri e filetti:
  - Evita i fermi impianto imprevisti
  - Mantiene le performance progettuali
  - Riduce i costi operativi nel tempo

### 3. Cosa facciamo

Fascia blu `primary` nella cornice bianca, come "Qualità ed Affidabilità" in home. Titolo a sinistra, le quattro attività a destra in due colonne, ognuna sotto un filetto, con la parte in grassetto della brochure.

- **H2**: Controllo, prevenzione, performance: sempre sotto controllo
- **Monitoraggio e verifiche periodiche** dei principali parametri operativi.
- **Diagnosi preventiva** e individuazione tempestiva di eventuali criticità.
- **Interventi mirati** per mantenere la massima efficienza, sicurezza e affidabilità.
- **Report e raccomandazioni** per l'ottimizzazione dell'esercizio.

### 4. Le due formule (ancora `#formule`)

- **H2**: Scegli il livello di servizio più adatto alle tue esigenze
- **Testo**: Due formule flessibili, con la qualità e l'esperienza EVAP.
- **Tabella** fatta di righe (contenitori di Elementor, non un'immagine): a 1440 tre colonne (voce 34%, PURE 33%, PLUS 33%, la colonna PLUS su fondo `#F5F6F8`, filetto azzurro di 3 px sotto l'intestazione); **sul telefono la voce va su una riga sua e PURE e PLUS restano affiancate al 50%**, così il confronto si legge senza scorrere di lato (`screenshot/anteprima-390.jpg`).

| Voce | MVR CARE PURE | MVR CARE PLUS |
|---|---|---|
| Visite tecniche programmate | **4** all'anno | **12** all'anno |
| Controllo remoto | 1 ogni settimana | 1 ogni settimana |
| Verifica dello stato di esercizio e della manutenzione | Compresa | Compresa |
| Anomalie | Segnalazione delle anomalie e azioni raccomandate | Analisi delle anomalie e delle perdite di produttività |
| Rapporto | Rapporto sintetico di verifica | Rapporto tecnico mensile |

I numeri delle visite sono nel carattere `secondary` (47 px), come i numeri della home: sono l'unica differenza "a colpo d'occhio".

### 5. Richiesta del canone (ancora `#canone`)

Riquadro grigio chiaro con il filetto azzurro sotto (le schede evidenziate del sito); a destra telefono, email e bottone, come il riquadro dei contatti nella colonna di Servizi.

- **H2**: Scopri il canone a te riservato
- **Testo**: Il canone di MVR CARE è particolarmente vantaggioso. Chiedi a EVAP quello riservato a te, per la formula PURE o per la PLUS.
- **Telefono**: +39 0444 1276355 (collegamento `tel:`), **email**: tecnico2@evap.it (dal piede e dalla pagina Contattaci)
- **Bottone**: "Richiedi il canone" verso /contattaci/

Modulo: il sito ne ha uno (MetForm, id 135, pagina Contattaci) ma è di un plugin, non di Elementor gratuito. Il modello porta quindi al modulo esistente con il bottone. Se il cliente vuole il modulo dentro la pagina, si sostituisce il bottone con il widget MetForm scegliendo il modulo "Contattaci" (istruzioni in `LEGGIMI.md`); conviene allora aggiungere ad "Argomento" una voce "MVR CARE".

### 6. Domande frequenti

Solo quattro, tutte con risposte già nella brochure; testo sempre visibile (niente fisarmoniche che si aprono).

- **Che differenza c'è tra PURE e PLUS?** Entrambe comprendono un controllo remoto ogni settimana e la verifica dello stato di esercizio e della manutenzione. PURE prevede 4 visite tecniche programmate all'anno, la segnalazione delle anomalie con le azioni raccomandate e un rapporto sintetico di verifica. PLUS prevede 12 visite all'anno, l'analisi delle anomalie e delle perdite di produttività e un rapporto tecnico mensile.
- **A chi è rivolto MVR CARE?** È il servizio di assistenza tecnica che EVAP dedica ai suoi clienti, per mantenere nel tempo l'efficienza e la continuità operativa dell'evaporatore MVR.
- **Che cosa ricevo dopo i controlli?** Report e raccomandazioni per l'ottimizzazione dell'esercizio: con PURE un rapporto sintetico di verifica, con PLUS un rapporto tecnico mensile.
- **Quanto costa?** Il canone è riservato e particolarmente vantaggioso: per conoscerlo scrivi a EVAP (collegamento a /contattaci/) o chiama il +39 0444 1276355.

Se il cliente risponde alle domande di `LEGGIMI.md` (durata, interventi compresi, chi può aderire), le risposte vere possono diventare altre domande frequenti. Senza conferma, no.

## Scelte di design

- **Stesso sito**: solo colori e caratteri del kit 11 (nel modello sono collegati con `__globals__`, quindi se EVAP cambia un colore globale la pagina lo segue), bottoni del kit (azzurro, testo bianco, 15/30 px, spigoli vivi, maiuscole iniziali come tutti i bottoni del sito), contenuto a 1290 px, 100 px tra le sezioni, cornice bianca di 20 px, filetti `#1D365C40`, schede `#F5F6F8` con filetto azzurro di 3 px, quadratini azzurri.
- **Un gradino più curata**: apertura con il nome del servizio grande a sinistra invece del titolo centrato; tre punti della copertina come filetti in fondo alla foto invece di icone; attività come frasi in grassetto sotto filetti invece di riquadri con icona; una tabella vera per il confronto; ogni sezione ha uno schema diverso da quella prima (foto piena, foto e testo, fascia blu a due colonne, tabella, riquadro chiaro, domande).
- **Vincoli del committente** (`_metodo/highend/SISTEMA.md` §2): niente tre riquadri con icona in fila, niente etichette sopra i titoli (il sito le usa, qui no), niente dissolvenze o animazioni d'ingresso, niente effetti col cursore, i bottoni si invertono di colpo (durata della transizione 0 nel modello), nessun carattere U+2014 nei testi e nei file, nessun gradiente, nessuna ombra.
- **Titoli H2 senza maiuscole iniziali**: stesse misure dell'H2 del kit (38/35/30 px, 600) ma `text-transform: none`, come i titoli della home. È l'unico punto in cui il modello non usa un carattere globale "così com'è".

## Foto

Tutte e due dalla libreria media di evap.it, foto vere di impianti EVAP in officina (nessuna foto di repertorio, nessuna illustrazione della brochure):

| Dove | File sul sito | Misura usata | Misura originale |
|---|---|---|---|
| Apertura (sfondo) | `/wp-content/uploads/2025/10/IMG_9042-1536x1152.jpg` (sul telefono `IMG_9042-1024x768.jpg`) | 1400 px di larghezza a 1440 | 2560 x 1920 |
| Perché conta | `/wp-content/uploads/2025/10/IMG_7517-768x1024.jpg` | circa 490 x 580 px | 1920 x 2560 |

La prima è un evaporatore con lo scambiatore orizzontale, il separatore e il quadro elettrico (la stessa foto, ritoccata, è nella fascia a scorrimento della home); la seconda un evaporatore con il quadro di controllo. Nessuna è presentata come "evaporatore MVR" nelle didascalie: il testo alternativo dice "Evaporatore EVAP con il quadro di controllo, in officina". Le foto restano entro la misura vera. Le foto di repertorio con licenza libera non servono.

Foto della libreria **scartate**: le immagini generiche prese dal web (`depuratore-sciacca`, `IMPIANTI-DI-TRATTAMENTO-ACQUE-REFLUE-INDUSTRIALI`, `Grey-Water-Treatment-Plant...`, `NETZSCH...`, `Water-Treatment-Plants...`, `treatment-tour...`, `3524633_water_treatment_plant...`, `depurazione-acqua`), le immagini del modello grafico (`construction*`, `Building-01`, `placeholder*`) e `life-struvite.jpg` (mani con il concime, non un impianto).

Le illustrazioni della brochure: vedi `ILLUSTRAZIONI-BROCHURE.md`.
