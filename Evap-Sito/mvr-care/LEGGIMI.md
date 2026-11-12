# MVR CARE: istruzioni (versione 2, landing page)

Landing page commerciale per il servizio di assistenza MVR CARE di EVAP, con le formule PURE e PLUS e il modulo per richiedere la proposta. Rifatta sulla base della risposta del cliente alla prima bozza: identità grafica della brochure, un solo invito ("Richiedi la tua proposta MVR CARE"), due schede d'offerta, modulo nella pagina. Qui: cosa c'è nella cartella, come metterla sul sito, cosa confermare prima di pubblicare.

## Cosa c'è nella cartella

| File | Cosa è |
|---|---|
| `01-contenuti.md` | I testi della brochure parola per parola, e i testi del messaggio del cliente usati nella pagina |
| `02-design-sito.md` | Com'è fatto il sito oggi (kit, testata, piede, pagine) e il problema del carattere che non si carica |
| `03-proposta.md` | **La landing**: struttura, testi completi, modulo, colori della brochure, immagini |
| `ILLUSTRAZIONI-BROCHURE.md` | Le illustrazioni della brochure: cosa si usa, a quali condizioni |
| `PROMPT-IMMAGINI.md` | Tre prompt (inglese e italiano) per far generare al cliente le immagini nello stile della copertina |
| `anteprima/index.html` | La landing come sarà sul sito, con testata e piede veri e il modulo statico. Meglio aprirla da un piccolo server: `python3 -m http.server` dalla cartella `anteprima`. Con `?carattere=sito` si vede col carattere che oggi non si carica |
| `anteprima/variante-schema.html` | La stessa landing con lo schema facoltativo "Come funziona un evaporatore MVR" |
| `anteprima/img/brochure-copertina-impianto.jpg` | Il ritaglio dell'impianto dalla copertina, per l'apertura (da caricare nella libreria media) |
| `screenshot/` | Schermate dell'anteprima e della variante a 1440 e a 390 px; in `prova-wordpress/` quelle della prova in WordPress |
| `elementor/mvr-care-template.json` | **Il modello della landing da importare** |
| `elementor/mvr-care-grazie-template.json` | Il modello della pagina di ringraziamento (facoltativa, per misurare le conversioni) |
| `elementor/genera_template.py`, `elementor/grafici.py` | I programmi che scrivono i modelli e i disegni (se cambiano testi o dati: si modificano lì e si lancia `python3 genera_template.py`) |
| `elementor/grafici/*.html` | Il codice dei widget HTML (linea dell'anno PURE e PLUS, legenda, schermata "MVR Monitoring", formula già scelta, schema facoltativo), pronto da incollare |
| `riferimenti/` | Schermate delle pagine attuali del sito |
| `originali/` | Brochure e immagini delle slide: solo sul computer, non vanno in git |

## Prima di cominciare

- Serve un utente amministratore e **Elementor Pro attivo** (sul sito c'è la 3.28): il modulo della landing è il widget **Modulo** di Elementor Pro. Tutto il resto è Elementor gratuito (contenitori, Titolo, Editor di testo, Immagine, Pulsante, Icona, Elenco icone, Divisore, HTML).
- I colori della brochure sono scritti nel modello come valori (per esempio `#2B880A` per i bottoni), perché nel kit del sito non ci sono. Se EVAP vuole poterli cambiare in un colpo solo: Elementor > Impostazioni del sito > Colori globali, aggiungere i colori della tabella in `03-proposta.md` e collegarli ai widget.

## 1. Caricare l'immagine dell'apertura

**Media > Aggiungi nuovo** e caricare `anteprima/img/brochure-copertina-impianto.jpg` (il ritaglio dell'impianto dalla copertina, autorizzato dal cliente). Testo alternativo: "Impianto di evaporazione, illustrazione della brochure MVR CARE".

## 2. Importare i modelli

1. **Modelli > Modelli salvati > Importa modelli**, scegliere `mvr-care-template.json`, **Importa ora**.
2. Elementor mostra due avvisi: "I file JSON potrebbero non essere sicuri" > **Continua**; "Abilita il caricamento di file non filtrati" > **Importa senza abilitare**.
3. Ripetere con `mvr-care-grazie-template.json` se si vuole la pagina di ringraziamento.

Durante l'importazione Elementor copia nella libreria la foto della sezione "Perché conta" (`IMG_7517-768x1024-1.jpg`): va bene, oppure si sceglie l'originale e si cancella la copia. Il logo e la foto dentro la schermata "MVR Monitoring" sono indirizzi della libreria già presenti, non vengono copiati.

## 3. Creare la pagina

1. **Pagine > Aggiungi nuova**, titolo `MVR CARE`, **Genitore** `Servizi`, **Modello** "Elementor a tutta larghezza" (come le altre pagine), indirizzo `mvr-care`. Salva come bozza, **Modifica con Elementor**.
2. Icona della cartella (**Aggiungi modello**) > **Modelli** > **Modelli del sito** > "MVR CARE" > **Inserisci**; alla domanda "Applicare anche le impostazioni di questa pagina?" rispondere **Applica**.
3. Nell'apertura, clic sull'immagine di destra (ora è il segnaposto grigio) > **Scegli immagine** > il ritaglio caricato al punto 1.
4. Controllare il modulo (punto 4), poi le viste tablet e telefono, poi **Pubblica**.

## 4. Il modulo (Elementor Pro)

Il modulo è nella sezione `#richiedi-proposta`, nel riquadro bianco sotto la fascia blu. Dopo l'importazione controllare in Elementor (clic sul modulo):
- **Campi**: 14 campi con gli ID della tabella in `03-proposta.md` (`nome`, `azienda`, `ruolo`, `email`, `telefono`, `evaporatore`, `settore`, `capacita`, `anno`, `formula`, `esigenza`, `fascia`, `messaggio`, `privacy`). L'ID del campo **`formula`** deve restare così: lo usa il piccolo script che sceglie la formula quando si arriva dal bottone di una scheda.
- **Pulsante**: "Fissa la call di diagnosi gratuita".
- **Azioni dopo l'invio**: Email (a **tecnico2@evap.it**, da confermare; oggetto "Richiesta proposta MVR CARE dal sito evap.it"; contenuto `[all-fields]`; "Rispondi a" il campo email) e Raccolta invii.
- **Messaggi**: conferma "Grazie, abbiamo ricevuto la tua richiesta. I tecnici EVAP ti contatteranno per fissare la call di diagnosi gratuita e senza impegno."
- **Invio di prova**: compilare il modulo dalla pagina pubblicata e controllare che l'email arrivi (e che non finisca nello spam: se succede, serve un plugin SMTP per WordPress).

**Se l'importazione non riconosce il modulo** (per esempio Pro non attivo, o una versione di Pro che legge le impostazioni in modo diverso: nella prova locale, senza Pro, Elementor lo scarta e importa il resto della pagina), si ricrea a mano in pochi minuti:
1. Nel riquadro bianco della sezione `#richiedi-proposta`, colonna di destra, trascinare il widget **Modulo** sopra il widget HTML che c'è già (lo script della formula: va lasciato).
2. Nome del modulo: "Richiesta proposta MVR CARE". Creare i campi della tabella di `03-proposta.md`, con lo stesso tipo, etichetta, ID (scheda Avanzate del campo), obbligatorietà, opzioni (una per riga) e larghezza (50% per nome, azienda, ruolo, email, telefono, evaporatore, capacità, anno, formula, esigenza; 100% per gli altri). Per la privacy: tipo "Accettazione", testo con il collegamento a https://evap.it/privacy-policy/.
3. Pulsante, azioni e messaggi come sopra.
4. Stile, come l'anteprima: etichette navy `#070D57` 15 px peso 600; campi fondo `#F5F8FB`, bordo 1 px `#1D365C40`, angoli 10 px; pulsante verde `#2B880A`, testo bianco 18 px peso 700, angoli 40 px, al passaggio `#070D57`; spazio tra i campi 20 px in orizzontale e 18 in verticale.

## 5. Pagina di ringraziamento e misura delle conversioni (facoltativo)

Serve se la landing viene sponsorizzata: la visita alla pagina di ringraziamento è la "conversione" da contare (Google Ads, Meta, Google Analytics).
1. Creare la pagina **Grazie**, genitore **MVR CARE**, indirizzo `grazie` (quindi `/servizi/mvr-care/grazie/`), modello "Elementor a tutta larghezza", e inserirvi il modello "MVR CARE, grazie" come al punto 3.
2. Nel modulo della landing: **Azioni dopo l'invio** > aggiungere **Reindirizzamento**. L'indirizzo `https://evap.it/servizi/mvr-care/grazie/` è già scritto nel modello (sezione "Reindirizzamento"); se non c'è, scriverlo. Con il reindirizzamento il messaggio di conferma non si vede più: lo sostituisce la pagina.
3. Non mettere la pagina Grazie nel menu; se c'è un plugin SEO, impostarla su "noindex".
4. Nello strumento delle campagne, creare la conversione "visita a /servizi/mvr-care/grazie/". Se la pagina dei cookie (Pressidium) blocca gli strumenti di misura finché il visitatore non accetta, le conversioni contate saranno meno di quelle vere: è normale.
5. Per sapere da quale campagna arriva una richiesta: si possono aggiungere al modulo campi nascosti con il valore preso dall'indirizzo (in Elementor Pro: campo "Nascosto" > Valore predefinito > tag dinamico "Parametro della richiesta", parametri `utm_source` e `utm_campaign`).

**Formula già scelta**: i bottoni delle schede PURE e PLUS portano a `?formula=pure#richiedi-proposta` e `?formula=plus#richiedi-proposta`; lo script nel widget HTML accanto al modulo sceglie la formula. Anche un annuncio può usare questi indirizzi.

## 6. Menu e titolo

- **Aspetto > Menu**: aggiungere "MVR CARE" e trascinarlo sotto "Servizi" come sottovoce. **Salva menu**.
- Il sito non ha un plugin SEO: WordPress userà "MVR CARE – EVAP" come titolo. Per una pagina sponsorizzata conviene installarne uno (Yoast SEO o Rank Math) e usare titolo e descrizione di `03-proposta.md`.

## 7. I disegni (widget HTML)

Nella landing ci sono cinque widget HTML: la schermata "MVR Monitoring", la linea dell'anno nella scheda PURE e in quella PLUS, la legenda sotto le schede, lo script della formula. In cima al codice di ognuno un commento spiega dove si cambiano numeri ed etichette. Il modo giusto per cambiarli è modificare i dati in `elementor/grafici.py` (sezioni `ANNO` e `MONITOR`), lanciare `python3 genera_template.py` e incollare il codice nuovo da `elementor/grafici/` nel widget (clic sul disegno > "Codice HTML"). I disegni hanno una versione larga (oltre 1024 px) e una compatta per tablet e telefono, con testi mai sotto gli 11 px. Nessuna animazione.

**Schema facoltativo "Come funziona un evaporatore MVR"** (`anteprima/variante-schema.html`): è uno schema di principio generico; **prima di pubblicarlo va fatto controllare a un tecnico EVAP**. Se va bene: dopo la sezione "Controllo, prevenzione, performance" aggiungere un contenitore largo 1290 px con un Titolo H2 "Come funziona un evaporatore MVR", un Editor di testo con la frase della variante e un widget HTML con il contenuto di `elementor/grafici/schema-mvr-facoltativo.html`.

## 8. Il carattere del sito (da sistemare, non della pagina)

Plus Jakarta Sans oggi **non si carica** su evap.it: il sito si vede in Arial/Helvetica e così si vedrebbe anche la landing (schermata `screenshot/anteprima-1440-come-oggi-senza-carattere.jpg`). Il foglio del carattere servito da LiteSpeed è vuoto e quello di Elementor punta al vecchio dominio di prova. Rimedio: Elementor > Strumenti > **Rigenera file e dati**, poi LiteSpeed Cache > **Svuota tutto**; se non basta, Elementor > Impostazioni > Avanzate: disattivare e riattivare "Carica Google Fonts in locale" e svuotare di nuovo la cache. Per una landing sponsorizzata vale la pena farlo prima della pubblicazione.

## 9. Da confermare prima di pubblicare

1. **Il dato "28 kWh/m³" e la sua formulazione esatta.** È misurato o "fino a"? Su un impianto preciso, su un impianto tipo o in media? In quali condizioni? In una pagina sponsorizzata dev'essere esatto ed eventualmente accompagnato da una nota. Si cambia in `grafici.py` (MONITOR) e nel titolo grande sotto la schermata.
2. **Il nome "MVR Monitoring"**: è uno strumento vero di EVAP o solo il titolo della brochure?
3. **L'email del modulo**: tecnico2@evap.it o un altro indirizzo (anche più di uno)? E un invio di prova riuscito.
4. **La pagina di ringraziamento**: la vogliono? Chi imposta la conversione nelle campagne?
5. **Le immagini AI**: il cliente le genera con `PROMPT-IMMAGINI.md`? Fino ad allora resta il ritaglio della copertina.
6. **I diritti delle illustrazioni usate**: il ritaglio della copertina è autorizzato; serve per iscritto chi l'ha prodotto, con quale programma e che la licenza permetta l'uso sul sito e negli annunci.
7. **A chi è rivolto**: la brochure dice "dedicato ai propri clienti", il modulo accetta anche impianti di altri costruttori. MVR CARE vale anche per loro?
8. **Le visite**: è giusto scrivere "Le date delle visite sono indicative: si concordano con il cliente"? Il rapporto sintetico di verifica di PURE quando arriva?
9. **Il canone**: resta su richiesta, senza prezzi in pagina?
10. **Le fasce orarie** del modulo (Mattina, Pomeriggio, Indifferente) vanno bene o preferiscono orari precisi?
11. **Il testo del consenso privacy** e il collegamento: va bene la pagina Privacy Policy o l'informativa clienti in PDF della pagina Contattaci?
12. **Grafici con dati veri** (facoltativo): per mostrare consumi, risparmi o fermi evitati servono un report vero anonimizzato, i consumi specifici medi reali e i fermi evitati, con il permesso di pubblicarli.

## Come è stato provato

In locale, fuori dal repository: WordPress 7.1.4, Hello Elementor 3.5.2, **Elementor 3.31.5 gratuito** su SQLite, con i colori e i caratteri globali del kit 11 ricreati e i colori e caratteri predefiniti disattivati come sul sito.
- Importati `mvr-care-template.json` e `mvr-care-grazie-template.json` dal pannello **Modelli salvati > Importa modelli**, con i due avvisi: nessun errore (`prova-wordpress/importazione-modelli-salvati.jpg`). Come previsto, senza Pro il widget Modulo viene scartato durante l'importazione; il resto della pagina c'è tutto, compresi i cinque widget HTML con stile, SVG e script.
- Creata la pagina `/servizi/mvr-care/` e scelta l'immagine dell'apertura; creata `/servizi/mvr-care/grazie/` dal secondo modello (`grazie-1440.jpg`).
- Inserito il modello anche dall'editor (Aggiungi modello > Modelli > Modelli del sito > Inserisci > Applica) e pubblicato: nessun errore (`editor-libreria-modelli.jpg`, `editor-modello-inserito.jpg`).
- Aperta nell'editor: 47 contenitori, 23 Titoli, 16 Editor di testo, 5 Pulsanti, 2 Immagini, 11 Icone, 3 Divisori, 2 Elenchi icone, 5 HTML, nessun errore di script (`editor-apertura.jpg`, `editor-widget-html-anno.jpg`).
- La pagina corrisponde all'anteprima a 1440 e a 390 px, tranne il modulo che senza Pro non c'è (`pagina-1440.jpg`, `pagina-390.jpg`); nessuno scorrimento laterale a 390, 768, 1024, 1440 e 1920 px; nei disegni il testo più piccolo misura 11 px.
- **Il widget Modulo di Elementor Pro non è stato provato** (Pro non era disponibile in locale): le sue impostazioni nel modello seguono il formato di Elementor Pro 3.x, ma vanno controllate sul sito come al punto 4.
