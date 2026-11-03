# Home, Peruzzo Grafiche: livello professionale (3/11/2026)

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, caratteri in `sito/fonts/`. La home di prima ("Stampare è un'arte" con The Private Eye in apertura e il disegno del dorso) e la sua nota sono copiate com'erano in `_prova/versione-1-originale/` (sito e screenshot).

Rifare tutto: `sh _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, controlli con `pro_controlli.mjs`, screenshot con `pro_shot.mjs`). Misure veloci a una larghezza: `node _prova/script/pro_misura.mjs <larghezza> <altezza> [mobile]`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (8189 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (12165 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Dove siamo" al piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e a 320, 768 e 1024.

## Livello professionale

Richiesta: "ancora troppo poco professionale e di design, e design funzionale all'attività"; foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezione B (difetti delle nostre home) e sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 (foglio `riferimenti.jpg`) e a 390 di tutti e 14, le pagine intere di barth e Cly-Del (a pezzi). Ordine seguito: prima l'uso (scheda `_prova/uso/SCHEDA.md`), poi l'identità, poi l'esecuzione.

### L'idea

Una tipografia industriale che si presenta come si presenta Cly-Del: in apertura la dichiarazione di mestiere in chiaro, accanto la loro fabbrica vera, sotto una riga di prove tecniche; poi i lavori con il nome dell'editore, le confezioni come una tabella da preventivista, il ciclo in casa su grafite pieno con il manifesto "Stampare è un'arte." in grande (il gesto di scala, preso dal loro Chi siamo), il modulo per il mestiere, Alberto Peruzzo, la sede di notte. Due blocchi grafite, due grigi chiari, il rosso del logo solo sui bottoni, sulle etichette e sul blocco "Ti chiamiamo noi". Nessun beige: il fondo è bianco.

### Struttura (A1, famiglia M, adattata)

1. **Testata fissa** (sticky, 88 px a 1440 e 72 a 390): logo 2022, quattro voci (Lavori, Confezioni e carte, Reparti, Dove siamo), il telefono come bottone con il numero e "Chiedi un preventivo". Sotto i 1240 px le voci vanno nella tendina "Menu" (si chiude con Esc o scegliendo una voce). Sul telefono il bottone del numero è bordato finché si vede il "Chiama" dell'apertura, poi diventa rosso pieno.
2. **Apertura**: occhiello "Peruzzo Grafiche, Mestrino (Padova), dal 1989"; H1 "Stampa e legatoria di libri, fumetti e cataloghi d'arte"; una riga su per chi e sul ciclo completo; a 1440 "Chiedi un preventivo" e "Chiama 049 9002884", poi email, indirizzo e "Ti chiamiamo noi"; a 390 tre bottoni a tutta larghezza Chiama, Scrivi un'email, Come arrivare, poi "Chiedi un preventivo" e "Ti chiamiamo noi". A destra, a filo del bordo, la loro legatoria (linea Müller Martini, il rosso della macchina è il rosso del marchio). Sotto, quattro prove: confezioni, stampa, carte, FSC.
3. **Cosa stampiamo e per chi** (grigio chiaro): titolo con le loro parole ("fumetti e libri di qualunque genere e qualunque formato"), quattro schede cliccabili con la foto del libro stampato, il tipo, il titolo, l'editore e "Anche per" con gli altri clienti; sotto, le aziende (Atala, Selle Royal, Calpeda) e i lavori semplici in parole semplici, con "Ti chiamiamo noi".
4. **Che confezione vi serve?** (bianco): punto metallico, brossura, cartonato con le varianti del loro modulo preventivi e un link che apre il modulo con la confezione già scelta; poi la tabella Stampa, Carte, Finiture, Legatoria, Certificazione (come la tabella delle macchine di DZStampi, sezione B13).
5. **Il ciclo in casa** (grafite): "Stampare è un'arte." in Piazzolla a 112 px con la frase loro sulla bagnatura e il registro; quattro reparti numerati come sul loro sito (.1-.4) con la foto del servizio 2018; cinque numeri (1989, 4 reparti, 3 confezioni, 70-170 g, 350 g).
6. **Preventivo** (grigio chiaro): cosa preparare, come mandare i file, il blocco rosso "Ti chiamiamo noi" (nome e telefono) e il modulo del mestiere.
7. **Chi c'è dietro** (bianco): Alberto Peruzzo al banco, l'inizio nel 1989 a 24 anni, i volumi Modern Art, "La carta è la nostra materia prima." in Piazzolla.
8. **Dove siamo** (grafite): la sede di notte, indirizzo con "Indicazioni stradali", i due telefoni, l'email e "Lavoro in corso? Scrivete qui" (email con oggetto e traccia), ritiri e consegne.
9. **Piede** in quattro colonne e riga legale.

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito completo in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Testata `position:sticky`, bottone "049 9002884" alto 48 px; a metà pagina, a 1440 e a 390, si vede e si tocca (`elementFromPoint`). 7 link `tel:` (due numeri).
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** 1440 x 900: H1 "Stampa e legatoria di libri, fumetti e cataloghi d'arte", "Mestrino (Padova)" e "dal 1989" nell'occhiello, "Chiedi un preventivo" a 525 px, la riga delle prove a 683-775 px, la foto intera (154-626 px). 390 x 844: stesso H1 e occhiello, "Chiama 049 9002884" largo quanto la colonna (350 px) a 395 px, poi Scrivi e Come arrivare; la foto comincia a 660 px.
3. **Immagine vera nell'apertura: passa.** La loro legatoria (servizio Canon EOS 6D del 2018, `2020-11-IMG_8866`, 2400 px), con il legatore al lavoro e le segnature sui bancali. Nessun oggetto scontornato, nessuna copertina di terzi in apertura (SCHEDA par. 7).
4. **Zero repertorio: passa.** `indicativ` compare 0 volte; nessun file Unsplash o Pexels in `sito/img/` né in pagina.
5. **Foto in serie: passa.** Tre formati: 3:2 (apertura, reparti, Alberto), 1:1 (i quattro libri), 2400:843 (la sede). Le foto di reparto sono tutte dello stesso servizio, con lo stesso trattamento (`pro_img.py`: tolta la dominante del neon, un po' di contrasto); i libri sono tutti foto di prodotto della loro pagina Prodotti con lo stesso trattamento. Nessuna didascalia, nessuna foto ingrandita oltre la misura d'origine.
6. **Palette dal marchio: passa.** `--rosso` #FF2A13 (logo e sito di oggi), `--rosso-scuro` #C41D0A per bottoni e testo, `--rosso-cupo` per il passaggio del mouse, `--grafite` #272727 (il grigio scuro del sito di oggi), poi bianco e cinque grigi neutri. Fondo bianco, nessun beige; i blocchi pieni sono grafite e grigio chiaro.
7. **Scala tipografica corta: passa.** 7 misure a 1440 (14, 17, 20, 26, 44, 64, 112) e 7 a 390 (14, 16, 18, 22, 30, 34, 56); testo corrente 17 px a 1440 e 16 a 390; nessun testo sotto i 14 px; H1 64/34 (fascia M: 60-70 e 34-40), H2 44/30.
8. **Due famiglie al massimo: passa.** Funnel Sans (400 e 700) per titoli, testo e interfaccia; Piazzolla 400 solo per le due frasi loro del manifesto ("Stampare è un'arte.", "La carta è la nostra materia prima."), come il serif per il manifesto di Holzrausch e Odermatt.
9. **Servizi in schede con la foto: passa.** Quattro schede dei lavori in 4 colonne (2 sotto i 1240 px, una per riga con la foto a sinistra sul telefono), stesso taglio quadrato, tutta la scheda è un link; anche i quattro reparti sono schede con la foto, tutte 3:2.
10. **Almeno tre tipi di prova: passa (3 su 4).** Cinque numeri aziendali; clienti con il nome (BeccoGiallo, Bao Publishing, Franco Cosimo Panini, Contini Art UK, più Coconino Press, Tunuè, Saldapress, Lucca Comics & Games, Il Castoro, Baldini e Castoldi, Galleria Contini, Vecchiato Arte, Atala, Selle Royal, Calpeda); la certificazione FSC con la sua didascalia nella tabella. Mancano le recensioni: non ce ne sono di pubbliche (SCHEDA, Reteimprese "Nessuna recensione") e non sono state inventate.
11. **I lavori hanno un nome: non passa del tutto.** Quattro lavori con titolo, tipo ed editore, ma senza anno e senza dati di tiratura (pagine, copie, confezione): non sono nelle fonti. Le foto sono a un quarto di pagina, non a metà: sono foto da telefono a 900-1200 px e ingrandite non reggono. Cosa chiedere è nel LEGGIMI.
12. **Ritmo a blocchi: passa.** Due blocchi grafite (reparti e dove siamo) e due grigi chiari (lavori e preventivo), più il blocco rosso "Ti chiamiamo noi". Spazio tra le sezioni 128 px a 1440 e 72 a 390; margini 80 px a 1440 e 20 a 390 (contenitore di 1440 px al massimo).
13. **Un solo sistema di bottoni: passa.** Pieno rosso e con il bordo, raggio 3 px ovunque, 56 px (48 in testata, 52 i tre dell'apertura sul telefono), testo 17 px (16 sul telefono); i bottoni di chiamata contengono il numero.
14. **Modulo e "dove" per il mestiere: passa.** Il modulo chiede nome, casa editrice o azienda, email, telefono, tipo di lavoro, confezione, formato chiuso, pagine dell'interno (multipli di 4), copie, carta, stampa, quando serve, link ai file e note; l'allegato (A6, famiglia M) è risolto così: i PDF si allegano all'email che il modulo compone, i file pesanti con un link di trasferimento nel campo apposito. Controlla nome ed email prima di comporre (avviso e fuoco sul primo campo vuoto). Indirizzo con "Indicazioni stradali" (Google Maps, percorso). Nessun iframe di mappa.
15. **Piede completo: non passa.** Quattro colonne a 1440, testo di almeno 14 px, ragione sociale, P.IVA 05078210282, indirizzo, telefoni ed email cliccabili, sede con la mappa, FSC, Privacy e Cookie. Mancano gli orari: non sono pubblicati e non sono stati inventati (LEGGIMI).

### Compiti della scheda d'uso (par. 8)

- *Editore, 1440*: nella prima schermata "Stampa e legatoria" e "libri, fumetti, cataloghi d'arte", "case editrici, gallerie e aziende"; "Chiedi un preventivo" porta con un clic al modulo (provato); brossura, cucita, cartonato, usomano e patinate sono già nella riga delle prove a 685 px, e la tabella completa è subito dopo i lavori. Come mandare i file: l'email è nella prima schermata, le istruzioni nel blocco preventivo (5235 px a 1440, dalla voce "Chiedi un preventivo"). Quattro lavori con il nome dell'editore e la foto della legatoria in apertura.
- *Lavoro in corso, 390*: Chiama (52 px, `tel:+390499002884`), Scrivi un'email (`mailto:` con oggetto) e Come arrivare (percorso per Via Marco Polo 10, Mestrino) nella prima schermata, più il numero sempre in testata; in "Dove siamo" anche "Lavoro in corso? Scrivete qui" con la traccia titolo, editore, cosa serve. Gli orari accanto all'indirizzo mancano (non pubblicati): al loro posto "Prima di passare per un ritiro o una consegna, chiamateci."
- *Non del mestiere, 390*: "libri e fumetti, cataloghi per le mostre, riviste, volantini e brochure" a 1596 px (meno di due scorrimenti); "Ti chiamiamo noi" nella prima schermata, porta al blocco con solo nome e telefono, che compone l'email "Ti chiamiamo noi" (provato); i quattro libri stampati in foto prima dei contatti.
- Nessun popup e nessun banner sopra i bottoni.

### Applicati

- Titolo che dice il mestiere al posto di "Stampare è un'arte" (SCHEDA par. 7: la frase poetica va più sotto); la frase resta come manifesto in grande nel blocco dei reparti.
- Via la copertina di The Private Eye dall'apertura e il disegno del dorso: al loro posto la legatoria vera e le confezioni in chiaro.
- Via il beige (#F5F1E8): fondo bianco, blocchi grafite e grigio chiaro, rosso del logo.
- Via il foglio in oro con il marchio storico in chiusura (SCHEDA par. 7: confonde il marchio).
- Testata fissa con il numero come bottone; tre bottoni a tutta larghezza sul telefono.
- "Ti chiamiamo noi" (loro, su ogni pagina del sito di oggi) come blocco con due campi; modulo preventivo con i campi del loro modulo a tre passi.
- Contatti, mappa e indirizzo nella prima schermata a 1440 e a 390, non più solo in fondo.
- Persone in pagina: il legatore, i grafici, il tipografo con il contafili, il magazziniere, Alberto Peruzzo.

### Respinti, con il motivo

- Le recensioni (regola 10): non ce ne sono di pubbliche.
- L'anno e i dati di tiratura dei lavori (regola 11): non sono nelle fonti.
- Gli orari nel piede e accanto all'indirizzo (regola 15, SCHEDA par. 8): non pubblicati.
- Il parco macchine (3 Heidelberg 8 colori, raccoglitrice a 18 stazioni, Stampamedia 2014), i 22 dipendenti e il fatturato: dati vecchi o di aggregatori, da confermare; non in pagina.
- La PEC: trovata solo su aziende.it, da confermare; non in pagina.
- Peruzzo Editoriale, le Peruzzine e la parete degli autori: non si sa se sono attivi; tolti dalla pagina e dal piede finché non arriva conferma.
- La Fondazione Peruzzo: il legame con il fondatore è probabile ma non confermato.
- La foto dell'operatrice al controllo (`IMG_8093`, verticale): sarebbe un quarto formato.
- La foto con il camion: sulla fiancata c'è ancora "S.P.A." e il marchio storico.

### Caratteri e licenze

- **Funnel Sans** (NORD ID), Google Fonts, SIL Open Font License 1.1: uso commerciale e ospitalità consentiti. File variabile 300-800 servito dalla pagina: `sito/fonts/funnel-sans-latin.woff2` e `funnel-sans-latin-ext.woff2`; licenza in `sito/fonts/OFL-FunnelSans.txt`. In pagina pesi 400 e 700.
- **Piazzolla** (Huerta Tipográfica), Google Fonts, SIL Open Font License 1.1: `sito/fonts/piazzolla-latin.woff2`, licenza in `sito/fonts/OFL-Piazzolla.txt`. Peso 400, asse ottico 30. Il file `piazzolla-latin-ext.woff2` resta nella cartella ma la pagina non lo usa.
- Sono gli stessi due caratteri della versione 1.

### Foto, origine

Tutte di Peruzzo, dal loro sito (`assets/originali/`), solo per la proposta. Nessuna di repertorio, nessuna generata, nessun disegno. Tabella completa in `assets/CREDITI.md`.

| In pagina | File originale |
|---|---|
| Apertura | `2020-11-IMG_8866.jpg` (legatoria), tagliata a sinistra (via il ventilatore) |
| Lavori | `2017-11-La-Sposa-Yemenita_BeccoGiallo.jpg`, `2017-11-Paper-Girls-2_Bao-Publishing.jpg`, `2017-11-Ferrari-cerca-e-trova_Franco-Cosimo-Panini.jpg`, `2017-11-Helidon-Xhixha-Refractive-Vibes_Contini-Art-UK.jpg` |
| Reparti | `2018-04-prestampa_04.jpg`, `2018-04-stampa_02.jpg`, `2018-05-IMG_7955.jpg`, `2018-07-IMG_8357.jpg` |
| Chi c'è dietro | `2020-11-IMG_8479.jpg` |
| Dove siamo | `2017-11-Notturna-In-Alta2.jpg`, tolto il cielo nero in alto |
| Logo | `logo-peruzzo-grafiche-bianco-2022-686x165.png` ricolorato in grafite |

Le foto di reparto online sono a 800 px: nelle schede (309 px CSS a 1440, circa 2,6x) reggono, più grandi no.

### Controlli fatti (3/11/2026)

- `pro_controlli.mjs`: regole 1-10 e 12-14 superate nelle misure; 11 e 15 no (sopra). Prove d'uso: preventivo in un clic, confezione già scelta dal link della scheda, modulo vuoto fermato con l'avviso e il fuoco sul nome, email del preventivo composta con oggetto "Richiesta di preventivo: Fumetto o graphic novel, 1500 copie", "Ti chiamiamo noi" composto con nome e telefono, tendina aperta e chiusa con Esc; nessun errore di script. Nessuna email inviata.
- Scorrimento orizzontale: nessuno a 320, 390, 768, 1024, 1280, 1440 e 1920; nessuna sovrapposizione nell'apertura a quelle larghezze; screenshot guardati a pezzi a 320, 390, 768, 1024 e 1440.
- Collegamenti: `tel:+390499002884`, `tel:+390499002885`, `mailto:info@graficheperuzzo.it` (con oggetto "Richiesta dal sito", "Lavoro in corso", e quelli composti dai moduli), mappe `https://www.google.com/maps/dir/?api=1&destination=Peruzzo+Grafiche,+Via+Marco+Polo+10,+35035+Mestrino+PD` (percorso) e `.../maps/search/?api=1&query=...` (piede). Nessuna ancora senza destinazione.
- Nessun carattere U+2014 nella pagina, nei .md e negli script (controllato anche da `build_finale.sh`).
