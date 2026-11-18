# Meccanica Masi, home

## Ritocco finale del livello professionale (3 novembre 2026)

Fatto sul giudizio del controllore (voto 6: "un buon tema fatto bene, non un progetto d'agenzia con un'identità") e sulle prove dei due clienti tipo (`_prova/pro-prova-0/`, `_prova/pro-prova-1/`). Regole: `_metodo/professionale/REGOLE.md`, famiglia M. Riguardati i riferimenti: le prime schermate di tutti e 14 (foglio unico) e le pagine intere di barth e Cly-Del, a pezzi. Le modifiche sono negli script `_prova/script/ritocco_css.py`, `ritocco_html.py`, `ritocco_js.py` (sostituzioni controllate sulla pagina scritta a mano) e in `pro_img.py` (foto). Si rifà tutto con `bash _prova/script/build_finale.sh`.

### Che cosa è cambiato

- **Identità e gesto di scala** (da barth e Cly-Del): titolo d'apertura a 70 px, Mona Sans larga al 116 % (asse di larghezza del file variabile), su nove colonne; titoli di sezione al 115 %. La fascia dei numeri ha quattro cifre a 120 px (larghezza 120 %), e la pagina chiude su un blocco rosso pieno con il telefono come titolo a 120 px (64 px tra 601 e 899, 44 px al telefono). Il testo d'apertura è nero, non più grigio da didascalia.
- **Le due porte come due blocchi pieni**, con il colore della sezione dove portano: "In azienda da voi" nera come la sezione Manutenzione, "In officina da noi" grigia come "Mandateci il disegno". Foto a 550 px da originali di 598 (non più 598 su 598). A 1440 l'unico bottone rosso pieno della prima schermata è quello della testata; nelle porte i bottoni hanno il solo bordo.
- **Foto d'apertura dell'officina**: al posto della Soraluce col pezzo arrugginito, il tornio CNC al lavoro su una puleggia (loro, qualità 5). La scheda Tornitura ora mostra il rullo pinza sul banco (loro, 1600x900): così anche il rullo pinza, prima solo citato, ha una foto.
- **Foto in serie**: due soli formati (2:1 nelle porte, 4:3 in schede e lavori; al telefono le schede in 2:1). I tre lavori piccoli passano da 4:5 a 4:3 e tutti i lavori sono tagliati più stretti sul pezzo. Trattamento comune più deciso in `pro_img.py`: autocontrasto 0,5 %, bianco al grigio neutro per l'80 %, saturazione 0,45, contrasto 1,05, leggero viraggio freddo; tappetino verde, carta bianca, banco nero e neon di reparto diventano grigi vicini e il rosso del marchio è l'unico colore forte.
- **Numeri veri, non riempitivi**: 6 persone in azienda, 6 torni (1 a controllo numerico), 1 fresatrice CNC industriale a 3 assi, 3 m la lamiera più lunga. Tolti "3 assi", "5 materiali" e "4 regioni servite sul posto" (dato da confermare).
- **Dati dei lavori solo dalle fonti**: tolti "alluminio 6082 o 7075", "Fresatura CNC a 3 assi e tornitura", "cuscinetto a rullini montato a pressione", "Ganasce a settori e molle di richiamo", "nastri in PVC, curve a 90°" e "Alluminio, tornitura e fresatura" (venivano dal crawl del vecchio sito, che non c'è più). La leva ora dice "In foto appena fresata, poi verniciata a polvere" (la foto è il pezzo grezzo).
- **Chi ha una macchina ferma**: toccando "Chiedete un intervento" (o scegliendo manutenzione o installazione nel modulo) la sezione del modulo cambia titolo e istruzioni: "Richiesta di intervento. Una macchina da sistemare o da installare? Scriveteci." con che cosa scrivere (macchina, marca e modello, dove si trova, che cosa non va) e "Se è ferma, chiamate". Fuori orario, accanto allo stato, c'è "Lasciateci la richiesta per email", che apre il modulo già impostato. Nella sezione Manutenzione: "Tempi e costi dipendono dalla macchina e dalla distanza: chiedeteli al telefono" e il rimando "Indirizzo, orari e mappa".
- **Modulo**: il campo del disegno è un bottone del sistema ("Scegliete il disegno") con il nome dei file scelti accanto e la frase "Da qui il file non parte: allegatelo all'email che si apre"; dopo "Prepara l'email" compare il testo composto con "Copia il testo", per chi non ha un programma di posta.
- **Officina**: materiali, quantità e "Misure massime: ve le diciamo al telefono, macchina per macchina" sopra le quattro schede, così si leggono subito dopo il clic su Lavorazioni.
- **Minori**: "Mandateci il disegno" (il voi, come il resto della pagina) in tutte le occorrenze; il verde del pallino è il token `--aperto` ("solo segnale di stato"); i salti dal menu partono dal bordo della sezione (`scroll-padding-top` uguale alla testata).

### Le 15 regole dopo il ritocco

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`) e screenshot guardati a pezzi a 1440 e 390, prime schermate a 320, 768 e 1024 con lo stato di sabato alle 13.

1. **Telefono come bottone nella testata fissa: passa.** 48 px, visibile e toccabile a metà pagina a 1440 e 390; 8 link `tel:`.
2. **Mestiere, luogo, prova e azione: passa.** H1 con i due mestieri, Padova nell'occhiello, "6 torni e una fresatrice CNC a 3 assi" (a 1440 nella porta dell'officina, al telefono nel testo d'apertura), Chiama in testata e "Mandateci il disegno" a 804-856 px a 1440; al telefono Chiama a tutta larghezza a 457-509 px.
3. **Immagine vera in apertura: passa.** Interno di una macchina da stampa e il tornio al lavoro, 345-620 px a 1440; a 390 la prima foto a 646-821 px. Ancora senza persone (foto da fare, LEGGIMI).
4. **Zero repertorio: passa.** "indicativ" 0, nessuna banca d'immagini, nessuna illustrazione.
5. **Foto in serie: passa.** Formati 2:1 e 4:3 (2 a 1440 e a 390), nessuna didascalia, stesso trattamento colore su tutte e 16. Restano foto da telefono di giorni diversi: la serie vera viene dal servizio fotografico.
6. **Palette dal marchio: passa.** Rosso #ED1C24 e nero #231F20 del logo, rosso pieno #C8141C, bianco, grigi neutri; il verde di stato è un token dichiarato.
7. **Scala corta: passa.** 1440: 14, 17, 18, 21, 23, 44, 70, 120 px (8); 390: 14, 16, 17, 20, 28, 38, 44, 64 px (8). Testo corrente 18 e 16 px, nulla sotto i 14 px; H1 70 e 38 px.
8. **Due famiglie al massimo: passa.** Una sola, Mona Sans, pesi 400 e 700.
9. **Servizi in schede con foto: passa.** 3 + 4 schede, tutte cliccabili, stesso taglio.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Quattro numeri veri e la fascia dei costruttori delle attrezzature con didascalia; recensioni leggibili e clienti con il nome non sono nelle fonti. Da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Cinque lavori veri con foto loro, ma senza anno e cliente (solo il Veneto per la linea giornali). Da chiedere (LEGGIMI).
12. **Ritmo a blocchi: passa.** Bianco, nero, bianco, rosso, grigio, bianco, nero, grigio, rosso, piede nero; mai due fondi uguali vicini. 120/72 px tra le sezioni, margini 110/20 px.
13. **Un solo sistema di bottoni: passa.** Pieno e con il bordo, raggio 4 px, 48-52 px, testo 17/16 px; ogni bottone di chiamata ha il numero.
14. **Modulo e "dove" per il mestiere: passa.** Campi M con l'allegato del disegno, campo macchina per manutenzione e installazione, mailto con oggetto e campi (da collegare a un servizio, LEGGIMI); nessun iframe; "Apri la mappa" e "Indicazioni stradali".
15. **Piede completo: passa, senza certificazioni.** Quattro colonne, ragione sociale, P.IVA e C.F., REA, SDI, indirizzo, telefono ed email cliccabili, orari, zone, Privacy. Il link Cookie non c'è: l'indirizzo della cookie policy iubenda non è nelle fonti e un link vuoto non serve (LEGGIMI).

### Compiti dei clienti tipo, dopo il ritocco

- *Macchina ferma, 390*: come prima (Chiama a 457-509 px, stato giusto sabato alle 13, testata fissa), in più dal sabato pomeriggio si può lasciare la richiesta per email e "Chiedete un intervento" porta a un titolo di intervento, non di disegno. Zone a 1024 px (entro una schermata di scorrimento).
- *Pezzo da fare, 1440*: "Mandateci il disegno" nella prima schermata; materiali, quantità e misure subito sotto il titolo delle lavorazioni; dopo l'invio, il testo da copiare se la posta non si apre.
- *Candidato, 390*: invariato ("Lavora con noi" dal menu in un tocco).

### Respinti, con il motivo

- Recensioni, clienti con il nome, anni dei lavori, certificazioni: non sono nelle fonti; non inventati.
- Link Cookie: indirizzo della cookie policy non noto; si rimette con iubenda sul sito vero.
- Esempi sotto "Cosa facciamo sul posto" (cuscinetti, cinghie, ingranaggi): non sono nelle loro frasi; restano le loro quattro voci.
- Tempo d'intervento concreto ("in giornata nel padovano"): non confermato.
- Pagine progetto cliccabili per i lavori: la home non deve rimandare a pagine che non esistono.

---

## Livello professionale (3 novembre 2026), passaggio prima del ritocco

Le righe qui sotto descrivono la pagina prima del ritocco finale; dove sono in conflitto con la sezione sopra, vale quella sopra (numeri, formati delle foto, porte, contatti).

Richiesta del committente: "ancora troppo poco professionale e di design, e design funzionale all'attività" e "secondo me non rappresentano bene l'identità e l'utilizzo corretto di quello che dovrebbe essere il sito". Foto: "niente" (nessuna foto di repertorio, nessun disegno al posto delle foto). Regole: `_metodo/professionale/REGOLE.md`, famiglia M (manifattura e fornitori del lusso), sezioni A, B e C. Scheda d'uso: `_prova/uso/SCHEDA.md`.

Riferimenti guardati: le prime schermate a 1440 e a 390 di tutti e 14 i siti; le pagine intere di Cly-Del e barth, a pezzi. Da Cly-Del: la dichiarazione di competenza come titolo, i blocchi pieni alternati (chiaro, scuro, colore), le schede di servizio in griglia, il piede scuro in quattro colonne. Da barth: la fascia dei numeri dell'azienda e i lavori con il nome sotto la foto grande. Dalla famiglia S (Kline, Wilson): il telefono come bottone in una testata fissa, perché il primo visitatore di Masi ha una macchina ferma.

La versione 1 com'era prima di questo passaggio (pagina "Pezzi dal pieno, su disegno" con la leva scontornata e l'interruttore) è copiata in `_prova/versione-1-originale/` (sito e screenshot). Una "versione 1 con l'uso" per Masi non era stata fatta: l'uso della scheda è stato messo in pagina in questo stesso passaggio.

Pagina: `sito/index.html`, statica, si apre con file:///. Si rifà tutto con `bash _prova/script/build_finale.sh` (immagini con `pro_img.py`, screenshot con `pro_shot.mjs` all'ora simulata martedì 3 novembre 2026 alle 10, controlli con `pro_controlli.mjs`, esito in `_prova/pro_controlli.json`). Per provare lo stato a un'altra ora: `index.html?ora=2026-11-07T13:00`.

Screenshot (stessi nomi di prima): `home-1440.jpg` (9221 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (15241 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (contatti e piede). Guardati a pezzi a 1440 e 390 accanto ai riferimenti, e a 320, 768 e 1024 (sabato alle 13, stato "Chiuso ora: riapriamo lunedì alle 8").

### Com'è fatta (struttura M adattata a un'officina con due mestieri)

1. **Testata fissa** (80 px a 1440, 72 a 390): logo, cinque voci con le loro parole (Manutenzione, Lavorazioni, Lavori, Lavora con noi, Contatti), lo stato "Aperto ora, fino alle 18" e il bottone rosso "Chiama 348 169 34 51". Al telefono: logo, bottone con il numero e "Menu".
2. **Apertura**: occhiello "Officina meccanica a Padova, per tutto il Nord Est"; titolo "Manutenzione sul posto e pezzi su disegno" (la scheda, par. 4); a fianco le loro parole "Interveniamo dove serve, quando serve", le macchine e la prova "6 torni e una fresatrice CNC a 3 assi". Sotto, **due porte** con una foto vera ciascuna: "In azienda da voi" (interno di una macchina da stampa, zone, "veniamo noi da voi", Chiama) e "In officina da noi" (la Soraluce con un pezzo grande, lavorazioni, "Mandaci il disegno"). Al telefono, prima delle porte: Chiama a tutta larghezza, lo stato, "Mandaci il disegno".
3. **Manutenzione sul posto** (blocco nero): "Non chiediamo di smontare, imballare e spedire nulla. Veniamo noi da voi."; "Fermare una linea di produzione costa"; tre schede con foto dei loro interventi (macchine da stampa offset e flexo, sacchettifici e confezionatrici, nastri trasportatori rulli e guide); cosa fanno sul posto; l'installazione in cinque fasi; dove arrivano, con Chiama e lo stato.
4. **In officina** (bianco): "Dai vostri disegni al componente finito"; quattro schede con foto del loro reparto (tornitura, fresatura CNC, lamiera, saldatura), ciascuna con il dato vero; materiali e quantità.
5. **Numeri** (blocco rosso): 6 persone, 6 torni, 3 assi, 3 m, 5 materiali, 4 regioni.
6. **Mandaci il disegno** (grigio): che file, cosa scrivere, a chi; modulo per il mestiere.
7. **Lavori su commessa** (bianco): due grandi (supporto Man-Roland, pulegge dal pieno) e tre (leva in ghisa, mandrino espansibile, linea di spedizione giornali), ognuno con due o tre dati; gli altri lavori in una riga.
8. **Chi siamo** (nero): "Siamo una piccola realtà, e ne andiamo fieri.", Matteo e il padre, "Chi ci chiama parla con chi lavora", il link alle recensioni su Google; la fascia "Le nostre attrezzature" con i costruttori.
9. **Lavora con noi** (grigio): "Cerchiamo manutentori meccanici, idraulici ed elettrici", CCNL Metalmeccanica Industria, candidatura per email e Chiama.
10. **Contatti** (bianco): telefono grande con stato e tabella degli orari (oggi in grassetto), email, sede con "Apri la mappa" (la loro scheda Google) e "Indicazioni stradali".
11. **Piede** (nero) in quattro colonne.

### Che cosa è cambiato rispetto alla versione 1, e perché

- **Titolo**: da "Pezzi dal pieno, su disegno" a "Manutenzione sul posto e pezzi su disegno". Il titolo di prima diceva un solo mestiere e lasciava fuori il visitatore principale (la scheda, par. 7: la manutenzione arrivava a circa 4000 px). Il nuovo dice i due mestieri e comincia da quello registrato (ATECO 33.12.59).
- **Via la leva scontornata e l'interruttore "Appena fresato / Verniciato"**: oggetto scontornato su fondo chiaro (REGOLE B2) e gioco "da grafico" secondo la scheda. La foto della leva resta, intera e come è stata scattata, tra i lavori.
- **Via il fondo verde grigio del tappetino** (#E1E6DE): non è un colore del marchio. Ora bianco e un grigio neutro #F1F1F1, il nero #231F20 e il rosso #ED1C24 del logo (il rosso pieno #C8141C per bottoni ed etichette, perché il bianco sopra il rosso del logo fa 4,4:1).
- **Via "A Padova dal 1977"**: data non confermata (il loro sito ne scrive quattro diverse).
- **Restano**: Mona Sans (una sola famiglia), il logo vettoriale, le foto vere che reggono, le loro frasi.
- **Foto**: nessuna di repertorio (anche prima non ce n'erano più). Tutte loro, mai ingrandite oltre la misura del taglio, con un trattamento comune (bianco portato verso il grigio neutro, saturazione 0,82, contrasto 1,06) e tre soli formati: 2:1 nelle porte, 4:3 in schede e lavori grandi, 4:5 nei lavori piccoli (4:3 al telefono). Tolte dai tagli le scritte "SHOT ON MI".

### Le 15 regole, una per una

Misure di `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`), più gli screenshot guardati a pezzi.

1. **Telefono come bottone nella testata fissa: passa.** Bottone "Chiama 348 169 34 51" alto 48 px; a metà pagina, a 1440 e a 390, si vede e si tocca (`elementFromPoint`). 8 link `tel:`, tutti `tel:+393481693451`. Per la famiglia M c'è anche "Mandaci il disegno" (la "Richiesta").
2. **Mestiere, luogo, prova e azione nella prima schermata: passa.** A 1440x900: titolo con i due mestieri, Padova nell'occhiello, "6 torni" e "fresatrice CNC a 3 assi" nel testo, Chiama a 780-832 px e "Mandaci il disegno". A 390x844: lo stesso, Chiama largo quanto la colonna (350 px) a 449-501 px, stato e "Mandaci il disegno" sotto.
3. **Immagine vera nell'apertura: passa, con riserva.** Due foto loro fatte dentro le macchine (interno di una macchina da stampa, la Soraluce con un pezzo grande), tutte e due nella prima schermata a 1440 (325-624 px), a 390 la prima a 638-813 px. Non ci sono persone né la sede con l'insegna: le foto da fare sono nel LEGGIMI. Sono 598 px di larghezza e restano a 598 px.
4. **Zero repertorio: passa.** "indicativ" 0 volte; nessuna immagine da banche (`assets/esterne/` non è usata); nessuna illustrazione.
5. **Foto in serie: passa, con il limite delle foto.** Stesso trattamento colore su tutte; tre formati (2:1, 4:3, 4:5); nessuna didascalia. Sono foto da telefono di giorni diversi: la serie vera viene dal servizio fotografico del LEGGIMI.
6. **Palette dal marchio: passa.** Quattro colori (rosso del logo, rosso pieno, nero del logo, bianco) più i grigi neutri; nessun beige, nessun colore scritto fuori da `:root` salvo il verde del pallino "Aperto".
7. **Scala corta e leggibile: passa.** 1440: 14, 17, 18, 21, 23, 44, 64 px; 390: 14, 16, 17, 20, 28, 34, 44 px. Testo corrente 18 e 16 px; nessun testo sotto i 14 px; titolo 64 px a 1440 e 34 a 390 (fascia M).
8. **Due famiglie al massimo: passa.** Una sola, Mona Sans, pesi 400 e 700; titoli e cifre in larghezza 108 %, testo e interfaccia al 100 %.
9. **Servizi in schede con la foto: passa.** Tre schede di manutenzione (3 colonne) e quattro di lavorazione (4 colonne), stesso taglio 4:3 (2:1 al telefono), nome, riga e link; tutta la scheda è un link che porta al modulo con la richiesta già scelta (manutenzione con la macchina, oppure pezzo con la lavorazione), così toccare una scheda non apre per sbaglio la posta o il telefono.
10. **Almeno tre tipi di prova: non passa (2 su 4).** Ci sono i sei numeri dell'azienda e la fascia dei costruttori delle loro attrezzature con la didascalia. Recensioni leggibili e clienti con il nome non sono nelle fonti: non inventati; il link porta alla loro scheda Google. Da chiedere (LEGGIMI).
11. **Lavori con un nome: non passa.** Cinque lavori veri con foto grandi e due o tre dati ciascuno, ma senza anno e senza cliente (solo la linea giornali ha il luogo, il Veneto): le fonti non li danno (le schede del vecchio sito avevano "Wallahia Inc., 2015" del tema). Da chiedere (LEGGIMI).
12. **Ritmo a blocchi: passa.** Blocchi pieni oltre al piede: manutenzione e chi siamo in nero, numeri in rosso; disegno e lavora con noi in grigio. Spazio tra le sezioni 120 px a 1440 e 72 a 390; contenitore di 1220 px con margini di 110 px a 1440, 20 px a 390.
13. **Un solo sistema di bottoni: passa.** Pieno rosso e con il solo bordo, raggio 4 px, 52 px (48 in testata), testo 17 px (16 al telefono); ogni bottone di chiamata ha il numero.
14. **Modulo e "dove" per il mestiere: passa, con riserva.** Modulo con richiesta (pezzo su disegno, a campione, rullo, manutenzione, installazione), nome, azienda, email, telefono; per i pezzi lavorazione, materiale, quantità, consegna, tolleranze e il campo del disegno (PDF, DXF, DWG, STEP, foto); per manutenzione e installazione la macchina e dove si trova. Controlla nome, azienda ed email (avviso e fuoco sul campo). Compone un'email (mailto) con oggetto e campi; un mailto non porta allegati, quindi il nome del file finisce nel testo e la pagina dice di allegarlo: va collegato a un servizio (LEGGIMI). Zone: Padova e provincia, Veneto, Friuli, Trentino, Emilia-Romagna (non hanno un elenco di comuni). Nessun iframe di mappa.
15. **Piede completo: passa, senza certificazioni.** Logo, ragione sociale, P.IVA e C.F., REA, SDI, indirizzo con la mappa, telefono ed email cliccabili, orari, zone, Privacy, in quattro colonne con testo di 14 px. Certificazioni: nessuna nelle fonti.

### Compiti della scheda d'uso (par. 8)

- *Macchina ferma, telefono 390x844*: "Chiama 348 169 34 51" a 449-501 px (sotto i 750), alto 52 px, `tel:+393481693451`; lo stato subito sotto; "manutenzione" e quattro tipi di macchina nella prima schermata; zone e "veniamo noi da voi" a 991 px (entro una schermata di scorrimento); il Chiama resta nella testata fissa. Sabato alle 13 la pagina dice "Chiuso ora: riapriamo lunedì alle 8".
- *Pezzo da fare, 1440x900*: "In officina da noi" e "Mandaci il disegno" nella prima schermata; un clic porta alle istruzioni (formati e cosa scrivere) e al modulo, che accetta PDF, DXF, DWG, STEP e foto; lavorazioni con i dati e materiali in una sezione; cinque lavori veri con foto loro.
- *Candidato, 390*: "Lavora con noi" nel menu e in una sezione della home; dal menu, un tocco porta al titolo "Cerchiamo manutentori meccanici, idraulici ed elettrici" con il CCNL.
- *Tutti*: indirizzo con "Apri la mappa" sulla loro scheda Google (`maps.google.com/?cid=1922531916466824828`, il luogo del loro QR delle recensioni), non una ricerca generica; nessuna parola del tema, nessuna data non confermata, nessuna foto di repertorio o generata.

### Controlli generali

- Scorrimento orizzontale: nessuno a 320, 360, 390, 768, 1024, 1280, 1440, 1920.
- Sovrapposizioni in testata e apertura (confronto dei riquadri): nessuna alle stesse larghezze; negli screenshot a pezzi nessuna in tutta la pagina. Corretti durante il lavoro: lo stato in testata che andava a capo, "Chiama348" senza spazio, i bottoni di "Lavora con noi" uno sotto l'altro a 1440, il piede con le colonne sfalsate, le foto delle porte ingrandite a 768 (ora restano affiancate fino a 601 px).
- Stato sull'ora di Roma, nove casi provati: martedì 10 aperto fino alle 18; 7.30 "apriamo alle 8"; 18.05 "riapriamo domani alle 8"; venerdì 19 "domani alle 8" (sabato); sabato 11 aperto fino alle 12; sabato 13 e domenica: lunedì; 8 dicembre e Pasquetta 2027 "oggi è festivo". Senza JavaScript resta scritto "Chiamate dal lunedì al venerdì 8-18, il sabato 8-12".
- Modulo: la scheda "Fresatura CNC" sceglie la lavorazione; invio vuoto fermato con "Manca il nome" e il fuoco sul campo; email composta e letta, senza inviarla, con oggetto "Richiesta: Un pezzo su disegno, Prova srl", materiale, quantità e il nome del file; la scheda dei sacchettifici passa alla richiesta di manutenzione e mostra il campo della macchina.
- Collegamenti: 8 `tel:+393481693451`, 4 `mailto:info@meccanicamasi.it` (con oggetto), 5 mappe (scheda Google con il CID, indicazioni con `maps/dir`). Nessun link a pagine che non esistono: le schede e il piede puntano alle sezioni della home; Privacy alla loro pagina di oggi.
- Nessun errore di script; nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.

### Caratteri e licenze

- **Mona Sans** (GitHub, distribuita da Google Fonts), SIL Open Font License 1.1, uso commerciale libero: file woff2 variabili serviti dalla pagina in `sito/fonts/`.
- **Jost** (Google Fonts, SIL OFL 1.1): solo le lettere "SRL" del logo, convertite in tracciati dentro l'SVG; non è servito dalla pagina.
- Foto: solo materiale della loro libreria media (`assets/originali/`), da usare con il loro permesso; elenco in `assets/CREDITI.md`.

### Respinti, con il motivo

- Recensioni in pagina (regola 10): non sono leggibili nelle fonti (Google blocca la lettura); c'è il link alla scheda.
- Clienti con il nome, anni dei lavori (regole 10 e 11): non sono nelle fonti; da chiedere.
- Certificazioni (regola 15): nessuna nelle fonti (il NADCAP del vecchio sito è del tema).
- Foto di persone, squadra o sede con l'insegna in apertura (regola 3, A7): non ce ne sono di vere; le due esterne della sede sembrano catture di Street View. Niente repertorio, niente illustrazioni (decisione del committente).
- Elenco dei comuni serviti (regola 14, famiglia S): il loro sito parla di regioni, non di comuni.
- Tempi d'intervento e prezzi: non sono pubblici; resta "nel minor tempo possibile".
- WhatsApp sul 348: non confermato.
- "A Padova dal 1977" e "Masi Macchine Grafiche": da confermare, non in pagina.

---

## Versione 1, "Dal pieno" (2 novembre 2026), prima del livello professionale

Descrive la versione copiata in `_prova/versione-1-originale/`.

Pagina: `sito/index.html`, si rigenera con `bash _prova/script/build_finale.sh`. Alta 5850 px a 1440, piede compreso (7545 a 390). Ultimo passaggio del 2 novembre 2026, dopo il giudizio cieco (`_prova/cieco.json`) e la richiesta del committente "più alta gamma, meno uguali tra loro".

### Idea

Un pezzo ricavato dal pieno e finito bene è già un oggetto da guardare. La loro leva con settore dentato in ghisa sta da sola al centro della prima schermata, appena fresata, con i segni dell'utensile nella tasca e la dentatura ad arco; un interruttore la mostra verniciata. Sotto il pezzo il titolo "Pezzi dal pieno, su disegno" corre esattamente da margine a margine e gli fa da basamento. Il pezzo, la coppia grezzo e verniciato e il verde del loro banco sono di Masi: con il nome di un concorrente la pagina non regge.

### Cosa è cambiato in questo passaggio

- **Impaginazione dell'apertura** (bloccante del giudice, K6): non più titolo a sinistra e pezzo scontornato a destra con le legende, lo schema che si ripeteva nella campagna (Agnoletto, DZ Stampi, BCM, Plastificazione Bastianello). Ora tutto sta sull'asse: pezzo al centro, didascalia in basso a sinistra e interruttore in basso a destra sulla stessa linea di base del pezzo, titolo su una riga sola a tutta misura (146 px a 1440, 164 px a 1920, corpo calcolato dalla larghezza del titolo in em, 8,99), sotto il testo a sinistra e la chiamata a destra. Nessun'altra home della campagna ha la composizione simmetrica né un titolo che misura esattamente la riga (controllato su `_invio/zona/home/copertine-est-grisignano.jpg` e sulle prime schermate dei `*-Sito`).
- **Titolo** (bloccante, K1): "Precisione in officina, continuità in produzione" (slogan del sito di oggi) diventa "Pezzi dal pieno, su disegno"; il testo sotto dice officina meccanica a Padova, le quattro lavorazioni, i rulli per la stampa offset e flexo e gli interventi in azienda.
- **Prima e dopo leggibile** (bloccante): tolto lo specchio della foto grezza (mostrava un pezzo che non esiste) e anche la rotazione; ognuna delle due foto è com'è stata scattata. Bottoni "Appena fresato" e "Verniciato", didascalia "Lo stesso pezzo, visto da due lati". La pagina apre sul pezzo appena fresato, il più bello.
- **Niente legende numerate sull'oggetto** (richiesta del committente): via pallini, filetti e numeri, sia a 1440 sia a 390. Resta una didascalia sobria: "Leva con settore dentato in ghisa. Fresata CNC dal pieno, alesatura H7. Lo stesso pezzo, visto da due lati."
- **Colore di fondo dal mestiere** (richiesta del committente): non più carta beige #F2F0EB ma #E1E6DE, il verde grigio del tappetino da banco su cui posano i loro pezzi nelle foto (pulegge #647062, misurato sulla foto, schiarito). Il motivo si vede: le pulegge della chiusura, il supporto Man-Roland e il mandrino stanno sullo stesso verde. Piede #D2D9CF. Le foto hanno un trattamento comune che porta il verde e l'azzurro del banco verso il verde della pagina e riporta a grigio le luci del metallo (l'alluminio accanto al verde tirava al rosa).
- **Ombra e bordi del pezzo** (importante): ogni leva su una tela stretta attorno a sé con 110 px di fondo in più sotto, quindi l'ombra sfuma e non è più tagliata da una riga dritta; ombra della leva bianca più corta (meno macchia grigia a sinistra del manicotto); sul verde la leva bianca ha contrasto pieno.
- **Fresatrice di repertorio tolta** (importante): al suo posto, a tutta larghezza, il loro gruppo mandrino espansibile smontato sul banco (inventario: qualità 5, apertura 5). Nella home non c'è più nessuna foto di repertorio né "Foto indicativa".
- **Sezione "veniamo noi da voi"** (importante): titolo in alto su dieci colonne, poi foto (colonne 1-6) e fasi (8-12) allineate in alto alla stessa quota; niente più vuoti accanto al titolo.
- **Lavorazioni**: quattro colonne, solo le lavorazioni d'officina e ognuna con un dato vero in testa (6 torni, 1 a CNC; 3 assi; da 10 cm a 3 m; TIG, MIG/MAG, elettrodo). Manutenzione e installazione stanno nella loro sezione. Cifre allineate senza tabellari (lo zero tabellare di Mona Sans è puntato).
- **Frasi ripetute** (minore): la commessa dei giornali resta solo nel progetto; "senza subappalti" una volta sola; "dal montaggio al collaudo" una volta; "nastri trasportatori, rulli e guide" una volta; la riga "Officina meccanica a Padova, dal 1977" non è più accanto all'email ma in chiusura ("A Padova dal 1977").
- **Logo** (importante): era già corretto dal passaggio precedente (`finale_logo.py`): "SRL" in tracciati, nessun `<text>`, nessun contorno bianco. Verificato con grep.
- **Legenda che toccava l'email a 1024** e **squilibrio del grezzo a 390** (minori): non esistono più; il pezzo sta in un riquadro fisso, allineato in basso al centro, quindi la distanza dal titolo è la stessa nei due stati e a ogni larghezza.

### Prime due schermate

- **1440** (`home-1440-prima-schermata.jpg`): testata (logo, Settori, Lavorazioni, Progetti, Contatti, telefono). La leva in ghisa al centro, alta 526 px; a sinistra in basso la didascalia, a destra in basso l'interruttore; il titolo da 64 a 1376 px; sotto, il testo d'apertura su tre righe a sinistra, "Chiama 348 169 34 51" e l'email a destra. Tutto entro i 900 px.
- **Seconda schermata**: "Dalla stampa ai trasporti industriali" e l'indice dei quattro settori, poi il mandrino a tutta larghezza.
- **390** (`home-390-prima-schermata.jpg`): la leva al centro alta 335 px, la didascalia, l'interruttore a tutta larghezza, il titolo su due righe a 52 px, poi il testo; telefono e Menu in testata.

### Chiusura e piede

- Chiusura ("b con foto", testo a sinistra e foto fino al bordo destro): "Un'officina che c'era ieri, c'è oggi e sarà qui domani" (Chi siamo), telefono grande in rosso #D8121A con tel:, email con mailto:, indirizzo come link alla mappa, orari, la loro frase "Chi ci chiama parla con chi lavora, e chi lavora conosce il mestiere." e "A Padova dal 1977". Foto vera delle pulegge dal pieno sul loro banco verde.
- Piede su #D2D9CF: logo vero con una riga su chi sono; quattro colonne Azienda, Lavorazioni (sette voci), Progetti, Contatti; riga legale con ragione sociale, indirizzo, P.IVA e C.F. 05200110285, REA PD-450853, codice SDI M5UXCR1, Privacy, Cookie. A 390 fisarmonica con veri bottoni (`aria-expanded`, `aria-controls`).
- **Niente colonna Seguici**: nessun profilo social vero (l'Instagram del sito porta a "#").
- **Niente newsletter**: lavorano su commessa per altre aziende, senza fiere, cataloghi, collezioni né clienti privati; il plugin newsletter del sito è installato e mai usato.

### Caratteri e colori

- **Mona Sans** (GitHub, distribuita da Google Fonts, SIL Open Font License 1.1, uso commerciale libero), una sola famiglia, file variabili serviti dalla pagina in `sito/fonts/`. Titolo d'apertura 500 a larghezza 82 %, interlinea 0,86, spaziatura -0,024em; h2 500 a 85 %; testo 400 a larghezza piena; h3 e bottoni 600. Riferimenti: il maiuscolo stretto di Hermle e l'HelveticaNeue condensato di Fehlmann (`riferimenti/`); il pezzo solo con la sua ombra da Hermle; la composizione centrata con un solo oggetto e poco testo da Vaucher.
- Colori e contrasti (WCAG): inchiostro #141A16 su fondo 13,9:1, su piede 12,3:1; grigio #48514A 6,5:1 e 5,7:1; rosso scuro #A5101A (numeri delle fasi, passaggio su bottoni e link) 6,2:1; rosso del logo #D8121A solo per il telefono da 48 px della chiusura, 4,1:1 (testo grande); bottone nero con testo chiaro 13,9:1. AA ovunque.

### Interazione

Un solo gesto: l'interruttore "Appena fresato / Verniciato" sulla linea di base del pezzo. Due bottoni veri con `aria-pressed`, frecce sinistra e destra da tastiera, tocco su telefono; cambio netto della foto, senza dissolvenze. Il bottone di chiamata diventa rosso scuro al passaggio, mai sbiadito. Nient'altro si muove: nessuna animazione allo scorrere, nessun effetto sul cursore. Su telefono il menu è un bottone "Menu" e il piede si apre a fisarmonica.

### Controlli (2 novembre 2026)

- `finale_controlli.mjs` a 2560, 1920, 1440, 1280, 1024, 768, 390, 320: scrollWidth uguale a innerWidth a tutte le larghezze; nessuna sovrapposizione tra il pezzo (riquadro calcolato da object-fit), didascalia, interruttore, titolo, testo e bottoni, nei due stati. Clic (schermi grandi) e tocco (768, 390, 320) su Verniciato: `aria-pressed` passa e la foto grezza si nasconde. Tastiera a 390: freccia destra da Verniciato porta il fuoco e lo stato su Appena fresato, freccia sinistra torna a Verniciato. Fisarmonica: Lavorazioni si apre, le altre restano chiuse.
- Altezze: 2560 e 1920 = 6149 px, 1440 = 5850, 1280 = 5497, 1024 = 5449, 768 = 7151, 390 = 7545, 320 = 7855.
- Collegamenti: tel:+393481693451 (4 volte), mailto:info@meccanicamasi.it (3), mappa Google con l'indirizzo (2).
- `segnali.sh` a 1440: 0 soglie bloccanti, 0 da guardare; area foto 35,2 %, Mona Sans 100 %, monospazio 0 %, 18 filetti, 0 frecce, 0 numeri grandi, 0 etichette sopra i titoli, una sola sezione con titolo a sinistra e testo a destra (Lavorazioni), una data nel corpo (1977).
- Screenshot guardati a pezzi a 1440 e 390, prime schermate nei due stati a 320, 390, 768, 1024, 1440 e 1920. Nessun U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script. Divieti del committente: nessun gradiente, nessuna emoji, niente Inter, niente card col bordo sinistro, niente vetro, niente tre box con icona, niente badge sopra il titolo, niente icone Lucide, niente dissolvenze allo scorrere, niente effetti sul cursore, niente bottoni che sbiadiscono, niente corsivo d'accento, niente legende numerate sull'oggetto.
