# MVR CARE: istruzioni

Pagina nuova per evap.it: il servizio di assistenza MVR CARE con le formule PURE e PLUS. Qui sotto: cosa c'è nella cartella, come mettere la pagina sul sito, cosa chiedere al cliente prima di pubblicare.

## Cosa c'è nella cartella

| File | Cosa è |
|---|---|
| `01-contenuti.md` | I testi della brochure, trascritti parola per parola, e cosa la brochure non dice |
| `02-design-sito.md` | Com'è fatto il sito oggi: colori, caratteri, misure, testata, piede, pagine |
| `03-proposta.md` | La pagina: indirizzo, menu, titolo SEO, sezioni e testi, foto |
| `ILLUSTRAZIONI-BROCHURE.md` | Le immagini della brochure (sembrano generate al computer) e quando si potrebbero usare |
| `anteprima/index.html` | La pagina come sarà sul sito, con testata e piede veri. Si apre nel browser (meglio da un piccolo server: `python3 -m http.server` dalla cartella `anteprima`). Con `?carattere=sito` in fondo all'indirizzo si vede come apparirebbe oggi, col carattere che non si carica |
| `screenshot/` | Schermate dell'anteprima a 1440 e a 390 px; in `prova-wordpress/` quelle della prova del modello |
| `elementor/mvr-care-template.json` | **Il modello da importare in Elementor** |
| `elementor/genera_template.py` | Il programma che scrive il modello (se cambiano i testi: si modificano lì e si lancia `python3 genera_template.py`) |
| `riferimenti/` | Schermate delle pagine attuali del sito |
| `originali/` | La brochure e le sue immagini: solo sul computer, **non vanno in git** (lo impedisce `Evap-Sito/.gitignore`) |

## 1. Importare il modello

Serve un utente amministratore. Il modello usa solo Elementor gratuito (contenitori, Titolo, Editor di testo, Immagine, Pulsante, Elenco icone): va bene con Elementor 3.31.5, con o senza Pro.

1. Nella bacheca di WordPress: **Modelli > Modelli salvati** (in inglese "Templates > Saved Templates").
2. In alto: **Importa modelli** ("Import Templates").
3. **Scegli file**: `mvr-care-template.json`, poi **Importa ora** ("Import Now").
4. Elementor mostra due avvisi:
   - "I file JSON potrebbero non essere sicuri" ("JSON files may be unsafe"): **Continua**. Il file è nostro.
   - "Abilita il caricamento di file non filtrati" ("Enable Unfiltered File Uploads"): **Importa senza abilitare** ("Import Without Enabling"). Il modello non contiene SVG né file JSON di animazioni, non serve abilitare niente.
5. Nell'elenco compare "MVR CARE" di tipo Pagina.

Durante l'importazione Elementor **copia le due foto** nella libreria media (diventano `IMG_9042-1536x1152-1.jpg` e `IMG_7517-768x1024-1.jpg`). Va bene così; chi vuole tenere la libreria pulita può, dopo, aprire la pagina in Elementor, scegliere per l'apertura e per la foto di "Perché conta" le immagini originali già presenti (`IMG_9042`, `IMG_7517`) e cancellare le due copie dalla libreria.

## 2. Creare la pagina

1. **Pagine > Aggiungi nuova**. Titolo: `MVR CARE`.
2. Nel riquadro a destra, **Attributi pagina** (o "Pagina > Modello"):
   - **Genitore**: `Servizi` (così l'indirizzo diventa `/servizi/mvr-care/`);
   - **Modello**: **Elementor a tutta larghezza** ("Elementor Full Width"), lo stesso di tutte le altre pagine del sito: mostra la testata e il piede del sito (Sina) e lascia a Elementor il resto.
3. **Indirizzo (slug)**: `mvr-care`. Salva come bozza.
4. **Modifica con Elementor**.
5. Nell'area vuota, l'icona della cartella (**Aggiungi modello**) > scheda **Modelli** > **Modelli del sito** ("Templates > Site templates"; nelle versioni più vecchie "I miei modelli") > riga "MVR CARE" > **Inserisci**. Elementor chiede "Applicare anche le impostazioni di questa pagina?" ("Apply the settings of this Page too?"): rispondere **Applica** (nasconde il titolo della pagina, che nelle altre pagine non c'è).
6. Controllare con le icone del telefono e del tablet in alto, poi **Pubblica**.

Se il titolo "MVR CARE" di WordPress comparisse sopra la foto: nelle impostazioni della pagina in Elementor (ingranaggio in alto) attivare **Nascondi titolo**.

## 3. Mettere la pagina nel menu

1. **Aspetto > Menu**, scegliere il menu del sito ("Menu principale").
2. Nel riquadro **Pagine** spuntare "MVR CARE" e **Aggiungi al menu**.
3. Trascinare "MVR CARE" **sotto "Servizi" e un po' a destra**, così diventa una sottovoce (come "Life Struvite" sotto "Progetti"). Il menu della testata mostrerà da solo la freccia accanto a "Servizi".
4. **Salva menu**. Controllare anche il menu sul telefono (il bottone azzurro con le tre righe).

Facoltativo, ma utile: un collegamento a `/servizi/mvr-care/` dalla scheda "Assistenza Post-Vendita" della home e un bottone "MVR CARE" nel riquadro "Altri servizi" della pagina Servizi.

## 4. Titolo e descrizione per Google

Il sito non ha un plugin SEO, quindi oggi WordPress scrive come titolo "MVR CARE – EVAP" e nessuna descrizione. Va bene anche così. Se si installa un plugin SEO (per esempio Yoast SEO o Rank Math), usare:
- titolo: `MVR CARE: assistenza per evaporatori MVR | EVAP`
- descrizione: `MVR CARE è l'assistenza EVAP per il tuo evaporatore MVR: visite tecniche programmate, controllo remoto ogni settimana e rapporti. Formule PURE e PLUS.`

## 5. Cose facoltative

- **Modulo dentro la pagina**: il sito ha già il modulo MetForm "Contattaci" (id 135). Nel riquadro "Scopri il canone a te riservato" si può togliere il bottone e trascinare al suo posto il widget **MetForm**, scegliendo quel modulo. In MetForm conviene aggiungere "MVR CARE" tra gli argomenti, così le richieste si riconoscono. Il modello di base porta invece alla pagina Contattaci, senza toccare MetForm.
- **Briciole di pane** come nelle altre pagine (Home → Servizi → MVR CARE): un widget Elenco icone in linea sotto la frase d'apertura, testo `#DBDBDB`, freccia bianca.

## 6. Un problema del sito da sistemare (non della pagina)

Oggi il carattere del sito, Plus Jakarta Sans, **non si carica**: il sito si vede in Arial/Helvetica. Il foglio del carattere che LiteSpeed serve è vuoto e quello di Elementor punta ancora al vecchio dominio di prova (dettagli in `02-design-sito.md`). Rimedio: Elementor > Strumenti > **Rigenera file e dati**, poi LiteSpeed Cache > **Svuota tutto**; se non basta, Elementor > Impostazioni > Avanzate: disattivare e riattivare "Carica Google Fonts in locale" e svuotare di nuovo la cache. La pagina MVR CARE usa i caratteri globali del kit, quindi si sistema insieme al resto.

## 7. Prima di pubblicare: cosa chiedere al cliente

1. **Foto vere.** Le due foto usate sono della vostra libreria (evaporatori in officina). Confermate che vanno bene per MVR CARE? Avete foto di un **tecnico EVAP al lavoro su un impianto in esercizio**, di un **evaporatore MVR installato** presso un cliente, o una **schermata vera del controllo remoto**? Sarebbero le foto giuste per questa pagina.
2. **Illustrazioni della brochure.** Le immagini delle slide sembrano generate al computer (il manometro ha la scala sbagliata, il laptop mostra "28 kWh/m³", un valore inventato). Sono vostre e ne avete i diritti per il sito? Per ora non le usiamo (vedi `ILLUSTRAZIONI-BROCHURE.md`).
3. **Testi.** Confermate i testi di `03-proposta.md`, comprese le piccole correzioni (per esempio "performance: sempre sotto controllo") e le quattro domande frequenti.
4. **A chi è rivolto.** La brochure dice "dedicato ai propri clienti": MVR CARE vale solo per gli impianti costruiti da EVAP o anche per evaporatori MVR di altri costruttori?
5. **Canone.** Resta "su richiesta" ("Scopri il canone a te riservato"), senza prezzi in pagina? Oppure volete una cifra o un "a partire da"?
6. **Dettagli che la brochure non dà**, da aggiungere solo se li confermate: durata del contratto e rinnovo; se gli interventi mirati e i ricambi sono compresi nel canone; tempi di intervento; come funziona il controllo remoto.
7. **Contatti.** Per le richieste MVR CARE vanno bene +39 0444 1276355 e tecnico2@evap.it, o c'è un riferimento diverso?
8. **Menu e indirizzo.** Va bene "MVR CARE" sotto "Servizi", all'indirizzo `/servizi/mvr-care/`? Volete il modulo dentro la pagina o il bottone verso Contattaci?
9. **Carattere del sito.** Possiamo sistemare il caricamento di Plus Jakarta Sans (punto 6)? Cambia l'aspetto di tutto il sito, in meglio.

## Come è stato provato il modello

In locale, fuori dal repository, con WordPress 7.1.4, il tema Hello Elementor 3.5.2 ed Elementor 3.31.5 gratuito su SQLite:
- ricreati nel kit locale i 12 colori e i 14 caratteri globali del kit 11 di evap.it, con gli stessi id, e disattivati colori e caratteri predefiniti come sul sito;
- importato `mvr-care-template.json` **dal pannello Modelli salvati > Importa modelli**, con i due avvisi come sopra: importato senza errori, le due foto scaricate da evap.it e copiate nella libreria (`screenshot/prova-wordpress/importazione-modelli-salvati.jpg`);
- creata una pagina vuota con "Elementor a tutta larghezza", aperta in Elementor, inserito il modello da **Aggiungi modello > Modelli > Modelli del sito**, risposto "Applica" alla domanda sulle impostazioni e pubblicato: la pagina ha le sei sezioni, il titolo nascosto ed è identica, pixel per pixel, a quella creata copiando il contenuto del modello (`editor-libreria-modelli.jpg`, `editor-modello-inserito.jpg`). Nota: in locale la libreria di Elementor non raggiungeva i server di elementor.com (bloccati dall'ambiente di prova) ed Elementor 3.31.5 in quel caso va in errore aprendo la libreria; per la prova si sono messi dati vuoti al posto di quelli remoti. Sul sito vero, collegato a internet, non dovrebbe succedere;
- aperta la pagina nell'editor di Elementor: 56 contenitori, 34 Titoli, 13 Editor di testo, 3 Pulsanti, 1 Immagine, 1 Elenco icone, nessun errore di script; carattere e colore dei widget risultano collegati ai globali (`editor-apertura.jpg`, `editor-tabella-globali.jpg`);
- la pagina pubblicata corrisponde all'anteprima a 1440 e a 390 px (`pagina-1440.jpg`, `pagina-390.jpg`; nella prova la testata è quella di base di Hello, sul sito sarà quella di Sina), e non scorre di lato a 390, 768, 1024, 1440 e 1920 px.
