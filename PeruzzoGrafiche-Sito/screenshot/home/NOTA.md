# Home, Peruzzo Grafiche: livello professionale, ritocco finale (3/11/2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La home di prima ("Stampare è un'arte" con The Private Eye in apertura e il disegno del dorso) e la sua nota sono copiate com'erano in `_prova/versione-1-originale/` (sito e screenshot).

Rifare tutto: `sh _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, controlli con `pro_controlli.mjs`, screenshot con `pro_shot.mjs`). Il modulo a passi e il riquadro "email pronta" si guardano con `node _prova/script/pro_passi.mjs <cartella>`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (9151 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (13753 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e a 320, 768 e 1024; guardati anche il passo 2 del modulo con il cartonato e il riquadro "email pronta" a 1440 e 390.

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Riferimenti guardati: le prime schermate di tutti e 14 (fogli di confronto a 1440 e 390 in `_prova/pro-controllo/`) e le pagine intere di barth e Cly-Del, a pezzi. Ordine seguito: prima l'uso (scheda `_prova/uso/SCHEDA.md`), poi l'identità, poi l'esecuzione.

### L'idea

Una tipografia industriale che si presenta come Cly-Del: dichiarazione di mestiere in chiaro, la loro fabbrica vera accanto, e la prima schermata che si chiude su un blocco grafite pieno con le prove e il rosso del marchio. Poi un lavoro in evidenza grande come un progetto di barth, gli altri in serie su fondo chiaro, le confezioni come una tabella da preventivista, il ciclo in casa su grafite con il manifesto "Stampare è un'arte." in grande, il modulo del mestiere a tre passi, Alberto Peruzzo, la sede di notte. Nessun beige: il fondo è bianco.

### Che cosa cambia nel ritocco finale

- **Prima schermata**: la riga delle prove è diventata una fascia grafite a tutta larghezza che chiude l'apertura, con un filetto rosso #FF2A13 sopra ogni voce; la foto della legatoria poggia sulla fascia, a filo del bordo destro. Al posto della voce "Carte" c'è **"Stampiamo per"** (Bao Publishing, BeccoGiallo, Coconino Press, Franco Cosimo Panini); le carte restano nella voce "Stampa e carte" (70-170 g, copertine fino a 350 g), così il compito 1 dell'editore non perde nulla.
- **Foto d'apertura** tagliata più stretta (finestra 3:2 di 1800x1200 da x 420, y 400): via controsoffitto, neon, cavi e cartello antincendio; linea e legatore più grandi.
- **Lavori**: un lavoro in evidenza (Il porto proibito, Bao Publishing) con la foto quadrata a 737 px su 1440 (oltre metà pagina) e accanto gli altri titoli Bao della loro pagina Prodotti; sotto quattro schede (La sposa yemenita, Ferrari cerca e trova, David Begbie per Contini Art UK, Tag Contract Project per Siloma). Via Paper Girls (fondo grigio caldo) e Xhixha (fondo nero); i cinque lavori hanno lo stesso trattamento e lo stesso fondo chiaro neutro (il verde di Ferrari era colpa del trattamento: ora il bianco di riferimento è la mediana di una cornice di 20 px, l'angolo è 237, 241, 240). Il gruppo "stampati per aziende" ha la sua scheda. A 390 le schede restano in colonna con la foto a tutta larghezza.
- **Numeri**: quattro senza ripetizioni di specifiche: 1989, 4 reparti, 3 confezioni in legatoria, 48 clienti con il marchio nella loro Libreria. Tolte le grammature (erano ripetute tre volte); il testo del reparto Legatoria non ripete più le confezioni.
- **Modulo del preventivo a tre passi**, come quello di oggi: 1 Il lavoro (tipo, confezione, formato, pagine, copie), 2 Carte e finiture (carta interno, stampa, carta e grammatura copertina, finitura copertina, e per il cartonato dorso, cartone 2, 2,5 o 3 mm e sovracoperta, data), 3 Contatti e file. Indicatore 1-2-3, Avanti e Indietro; senza script resta un modulo unico. Le pagine non multiple di 4 si fermano con "Le pagine dell'interno vanno in multipli di 4: intendete 196 o 200?". Dopo il clic resta in pagina il riquadro "La vostra email è pronta" con il testo, "Copia il testo" e "Apri di nuovo l'email", anche per "Ti chiamiamo noi". I link delle confezioni preselezionano "Brossura, fresata o cucita" (e analoghi), non più la cucita.
- **Lavoro in corso, 390**: sotto i tre bottoni dell'apertura il link "Lavoro in corso? Scrivete qui" (49 px, email con titolo, editore, cosa serve); il bottone email mostra l'indirizzo ("Scrivete a info@graficheperuzzo.it"); nel menu in fondo "Chiamate 049 9002884" e "Come arrivare".
- **Dove siamo**: titolo "Dove siamo e come raggiungerci" (non ripete più l'indirizzo); accanto all'indirizzo "Orari di ufficio e di carico e scarico: telefonate prima di passare." con il bottone "Chiamate 049 9002884"; "Telefono, due linee"; "PEC e recapiti per l'amministrazione: chiedeteli allo stesso numero."; link alti almeno 44 px a 390 in Dove siamo, nel piede e nell'apertura; nel piede la mappa apre il percorso (maps/dir) come negli altri due punti.
- **Voi in tutta la pagina**: "Chiedete un preventivo", "Chiamate 049 9002884", "Scrivete a"; resta "Ti chiamiamo noi", la loro dicitura.
- **Come mandare i file**: aggiunta la riga "Per le specifiche degli esecutivi (PDF, abbondanze, profilo colore) chiedete alla prestampa allo 049 9002884 prima di chiudere i file." Le specifiche vere non sono nelle fonti (LEGGIMI).

### Struttura (A1, famiglia M, adattata)

1. **Testata fissa** (sticky, 88 px a 1440 e 72 a 390): logo 2022, Lavori, Confezioni e carte, Reparti, Dove siamo, il numero come bottone e "Chiedete un preventivo". Sotto i 1240 px la tendina "Menu" (si chiude con Esc o scegliendo una voce), con in fondo Chiamate e Come arrivare. Sul telefono il bottone del numero diventa rosso pieno quando non si vede più il "Chiamate" dell'apertura.
2. **Apertura**: occhiello "Peruzzo Grafiche, Mestrino (Padova), dal 1989"; H1 "Stampa e legatoria di libri, fumetti e cataloghi d'arte"; riga su per chi e sul ciclo completo; a 1440 "Chiedete un preventivo" e "Chiamate 049 9002884", poi email, indirizzo e "Ti chiamiamo noi"; a 390 Chiamate, Scrivete a info@..., Come arrivare a tutta larghezza, poi Lavoro in corso, preventivo e "Ti chiamiamo noi". La legatoria a destra; sotto la fascia grafite delle prove.
3. **Cosa stampiamo e per chi** (grigio chiaro): il lavoro in evidenza e quattro schede, poi gli altri clienti e "Ti chiamiamo noi".
4. **Che confezione vi serve?** (bianco): le tre confezioni con il link al modulo e la tabella Stampa, Carte, Finiture, Legatoria, Certificazione.
5. **Il ciclo in casa** (grafite): manifesto in Piazzolla a 112 px, quattro reparti .1-.4, quattro numeri.
6. **Preventivo** (grigio chiaro): cosa preparare, come mandare i file, "Ti chiamiamo noi" su rosso, il modulo a tre passi.
7. **Chi c'è dietro** (bianco): Alberto Peruzzo al banco, 1989 a 24 anni, Modern Art, "La carta è la nostra materia prima."
8. **Dove siamo** (grafite): la sede di notte, indirizzo con indicazioni e riga sugli orari, due linee, email e lavoro in corso, consegne con i loro mezzi.
9. **Piede** in quattro colonne e riga legale.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata sticky, bottone "049 9002884" alto 48 px; a metà pagina si vede e si tocca a 1440 e a 390 (`elementFromPoint`), a 390 è pieno. 10 link `tel:`; accanto "Chiedete un preventivo" (la "Richiesta" della famiglia M).
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440x900: H1 a 64 px, "Mestrino (Padova)" e "dal 1989" nell'occhiello, "Chiedete un preventivo" a 525 px, foto 219-691 px, fascia delle prove 691-847 px con "Stampiamo per" e FSC. 390x844: stesso H1 a 34 px, "Chiamate 049 9002884" largo 350 px (tutta la colonna) a 395 px, poi Scrivete e Come arrivare; la foto comincia a 709 px.
3. **Immagine vera nell'apertura: passa.** La loro legatoria (servizio Canon 2018, `2020-11-IMG_8866`), ora tagliata sul legatore e sulla linea Müller Martini, senza controsoffitto. Nessun oggetto scontornato, nessuna copertina di terzi in apertura.
4. **Zero repertorio: passa.** `indicativ` 0 volte; nessun file Unsplash o Pexels in `sito/img/` né in pagina; i 28 file di `sito/img/` sono tutti loro e tutti usati.
5. **Foto in serie: passa.** Tre formati a 1440 e a 390: 3:2 (apertura, reparti, Alberto), 1:1 (i cinque lavori), 2,85:1 (la sede). Zero didascalie. I cinque lavori ora sono tutti su fondo chiaro neutro con lo stesso trattamento (fondo dalla cornice di 20 px allo stesso grigio, saturazione -10%); niente più fondo verde, grigio caldo o nero. Nessuna foto ingrandita oltre la misura d'origine.
6. **Palette dal marchio: passa.** `--rosso` #FF2A13 (logo), `--rosso-scuro` #C41D0A (bottoni e testo), `--rosso-cupo` (passaggio del mouse), `--grafite` #272727, bianco e cinque grigi neutri. Fondo bianco; blocchi pieni grafite, grigio chiaro e rosso. Il rosso del logo ora si vede anche nella prima schermata, sui filetti della fascia grafite.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 26, 44, 64, 112) e 7 a 390 (14, 16, 18, 22, 30, 34, 56); testo corrente 17/16 px; nessun testo sotto i 14 px; H1 64/34, H2 44/30.
8. **Due famiglie al massimo: passa.** Funnel Sans per titoli, testo, bottoni e campi; Piazzolla solo nelle due frasi loro ("Stampare è un'arte.", "La carta è la nostra materia prima.").
9. **Servizi in schede con la foto: passa.** Griglia a 4 colonne: il lavoro in evidenza su tutta la riga e quattro schede, tutte link interi con foto 1:1, tipo, titolo, editore e link; i quattro reparti in schede 3:2.
10. **Almeno tre tipi di prova: passa (3 su 4).** Quattro numeri aziendali (1989, 4 reparti, 3 confezioni, 48 clienti in Libreria); clienti con il nome (Bao Publishing, BeccoGiallo, Coconino Press, Franco Cosimo Panini già nella prima schermata, poi Contini Art UK, Siloma, Tunuè, Saldapress, Lucca Comics & Games, Il Castoro, Baldini e Castoldi, Galleria Contini, Vecchiato Arte, Atala, Selle Royal, Calpeda); FSC con la didascalia nella tabella. Le recensioni non ci sono: non ce ne sono di pubbliche e non sono state inventate.
11. **I lavori hanno un nome: non passa del tutto.** Cinque lavori con titolo, tipo ed editore; il lavoro in evidenza ha la foto a 737 px su 1440 (oltre metà pagina) e l'elenco degli altri titoli stampati per Bao. Mancano l'anno e i 2-3 dati (confezione, pagine, copie): non sono nelle fonti, sono tra le cose da chiedere (LEGGIMI punto 4).
12. **Ritmo a blocchi: passa.** Blocchi grafite: la fascia delle prove, Reparti, Dove siamo; grigi chiari: Lavori e Preventivo; rosso: "Ti chiamiamo noi". Spazio tra le sezioni 128 px a 1440 e 72 a 390; margini 80 e 20 px; gesto di scala: il manifesto a 112 px e il lavoro in evidenza.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e con il bordo, raggio 3 px ovunque, 48 px in testata e 52-56 altrove, testo 17/16 px; tutti i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Modulo a tre passi con i campi del loro modulo di oggi (compresi copertina, finitura, dorso, cartone e sovracoperta); l'allegato (A6, M) è risolto con i PDF allegati all'email composta e il campo per il link di trasferimento. Prove: un clic su "Chiedete un preventivo" porta al modulo; "Preventivo per una brossura" imposta "Brossura, fresata o cucita"; 198 pagine si fermano con l'avviso; modulo vuoto fermato con "Manca: Nome e cognome." e il fuoco sul campo; email composta "Richiesta di preventivo: Fumetto o graphic novel, 1500 copie" con tutte le righe; riquadro "email pronta" visibile. Indirizzo con "Indicazioni stradali" (percorso). Nessun iframe.
15. **Piede completo: non passa.** Quattro colonne a 1440, testo di almeno 14 px, ragione sociale, P.IVA, indirizzo con il percorso, due telefoni, email, FSC, Privacy e Cookie. Gli orari veri mancano (non pubblicati): al loro posto "Orari di ufficio e di carico: telefonate prima di passare", che non è un orario. Il controllo resta onestamente negativo finché l'azienda non li dà.

### Compiti della scheda d'uso

- *Editore, 1440*: nella prima schermata mestiere, per chi, "Stampiamo per" con quattro editori, le confezioni (brossura fresata o cucita, cartonato), usomano e patinate 70-170 g, copertine fino a 350 g, FSC: tutto senza scorrere. Preventivo in un clic, modulo a tre passi con la sua lingua; avviso sulle pagine; riquadro con il testo pronto se la posta non si apre. Come mandare i file a 5986 px, un clic dal bottone; le specifiche degli esecutivi restano da chiedere (c'è il numero della prestampa). Tempi e tirature: non nelle fonti, nel LEGGIMI.
- *Lavoro in corso, 390*: Chiamate, Scrivete (con l'indirizzo scritto), Come arrivare e "Lavoro in corso? Scrivete qui" nella prima schermata; il numero sempre in testata; nel menu Chiamate e Come arrivare. Orari: accanto all'indirizzo la riga "telefonate prima di passare" con il bottone del numero; gli orari veri mancano (LEGGIMI punto 1). PEC: "chiedeteli allo stesso numero" finché l'azienda non conferma l'indirizzo.
- *Non del mestiere, 390*: "libri e fumetti, cataloghi per le mostre, riviste, volantini e brochure" a 1605 px; "Ti chiamiamo noi" nella prima schermata, con solo nome e telefono e il riquadro di conferma; cinque lavori in foto a tutta larghezza prima dei contatti.
- Nessun popup e nessun banner sopra i bottoni.

### Applicati (dal controllore e dai due clienti tipo)

- Regola 5: lavori in serie su fondo chiaro neutro, corretto il verde di Ferrari (`pro_img.py`, `cornice()` e `prodotto()`), via Xhixha e Paper Girls.
- Regola 11 (parte possibile): lavoro in evidenza oltre metà pagina; a 390 foto dei lavori a tutta larghezza.
- Numeri senza specifiche ripetute; prove con "Stampiamo per" su fascia grafite con il rosso del marchio; foto d'apertura ritagliata.
- Scheda per gli stampati aziendali (Siloma); una sola scheda di fumetti in senso stretto più la graphic novel.
- Bottoni al voi; titolo di "Dove siamo" senza ripetere l'indirizzo.
- Modulo a tre passi, campi di copertina, finitura e cartonato, avviso delle pagine in italiano, riquadro "email pronta" con "Copia il testo", preselezione neutra della confezione.
- Riga sugli orari accanto all'indirizzo e nel piede con il bottone del numero; PEC rimandata all'amministrazione al telefono; "Telefono, due linee"; "Lavoro in corso" nella prima schermata a 390; indirizzo scritto nel bottone email; Chiamate e Come arrivare nel menu; bersagli di almeno 44 px; maps/dir anche nel piede.
- Riga sulle specifiche degli esecutivi (chi chiamare).

### Respinti o rimandati, con il motivo

- Anno, confezione, pagine e copie dei lavori (regola 11): non sono nelle fonti; le date dei file (2017-11) sono di caricamento, non di stampa.
- Orari veri (regola 15, SCHEDA par. 8), tempi di produzione e tirature minime, specifiche degli esecutivi: non pubblicati, non inventati.
- PEC e fax: la PEC viene solo da aziende.it e il fax è da confermare; in pagina solo il rimando all'amministrazione.
- Recensioni (regola 10): non ce ne sono di pubbliche.
- Parco macchine, dipendenti e fatturato: dati vecchi o di aggregatori, fuori dalla pagina.
- Invio vero del modulo e caricamento dei file: con un mailto non si può; va collegato a un servizio (LEGGIMI).
- Pagine interne (`lavori.html`, `prestampa.html` e le altre): la home punta alle pagine del sito nuovo, elencate nel LEGGIMI; non le ho fatte perché il compito è la home.
- Peruzzo Editoriale, le Peruzzine, la parete degli autori, la Fondazione: non confermati.
- Foto con il camion (marchio storico "S.P.A." sulla fiancata) e foto verticale dell'operatrice (quarto formato).

### Caratteri e licenze

- **Funnel Sans** (NORD ID), Google Fonts, SIL Open Font License 1.1: uso commerciale e ospitalità consentiti. File variabile 300-800 servito dalla pagina: `sito/fonts/funnel-sans-latin.woff2` e `funnel-sans-latin-ext.woff2` (preload con `crossorigin`); licenza in `sito/fonts/OFL-FunnelSans.txt`. In pagina pesi 400 e 700.
- **Piazzolla** (Huerta Tipográfica), Google Fonts, SIL Open Font License 1.1: `sito/fonts/piazzolla-latin.woff2`, licenza in `sito/fonts/OFL-Piazzolla.txt`. Peso 400, asse ottico 30.
- Sono gli stessi due caratteri della versione 1.

### Foto, origine

Tutte di Peruzzo, dal loro sito (`assets/originali/`), solo per la proposta. Nessuna di repertorio, nessuna generata, nessun disegno. Tabella completa in `assets/CREDITI.md`.

| In pagina | File originale |
|---|---|
| Apertura | `2020-11-IMG_8866.jpg` (legatoria), finestra 1800x1200 da x 420, y 400 |
| Lavoro in evidenza | `2017-11-Il-porto-Proibito_Bao-Publishing.jpg` |
| Lavori | `2017-11-La-Sposa-Yemenita_BeccoGiallo.jpg`, `2017-11-Ferrari-cerca-e-trova_Franco-Cosimo-Panini.jpg`, `2017-11-David-Begbie_Contini-Art-UK.jpg`, `2017-11-Tag-Contract-Project_Siloma.jpg` |
| Reparti | `2018-04-prestampa_04.jpg`, `2018-04-stampa_02.jpg`, `2018-05-IMG_7955.jpg`, `2018-07-IMG_8357.jpg` |
| Chi c'è dietro | `2020-11-IMG_8479.jpg` |
| Dove siamo | `2017-11-Notturna-In-Alta2.jpg`, tolto il cielo nero in alto |
| Logo | `logo-peruzzo-grafiche-bianco-2022-686x165.png` ricolorato in grafite |

Le foto di reparto online sono a 800 px: reggono nelle schede (302 px a 1440) e come miniature a 390, più grandi no. Il lavoro in evidenza è a 900 px per 737 px in pagina: regge a 1x, per gli schermi 2x serve la foto rifatta (LEGGIMI).

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-14 superate; 11 e 15 no (sopra). Prove d'uso tutte riuscite (sopra), tendina aperta e chiusa con Esc, nessun errore di script. Nessuna email inviata.
- Scorrimento orizzontale: nessuno a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura. Screenshot guardati a pezzi a 320, 390, 768, 1024 e 1440.
- Collegamenti: `tel:+390499002884`, `tel:+390499002885`, `mailto:info@graficheperuzzo.it` (con oggetto "Richiesta dal sito", "Lavoro in corso" e quelli dei moduli), una sola mappa `https://www.google.com/maps/dir/?api=1&destination=Peruzzo+Grafiche,+Via+Marco+Polo+10,+35035+Mestrino+PD` in tutti i punti. Nessuna ancora senza destinazione, nessuna immagine inutile in `sito/img/`.
- Nessun carattere U+2014 nella pagina, nei .md e negli script (controllato anche da `build_finale.sh`).
