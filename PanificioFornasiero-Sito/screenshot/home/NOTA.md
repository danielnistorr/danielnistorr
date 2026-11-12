# Home, Panificio Galileo Fornasiero: metodo ibrido (novembre 2026)

## Metodo ibrido (novembre 2026)

Pagina: `sito/index.html` (statica, si apre con file:///). La versione professionale com'era prima di questo passaggio è copiata in `_prova/versione-pro/` (sito intero e screenshot). Direzione scritta prima dell'HTML: `_prova/alto/DIREZIONE.md`; riga nel registro dei caratteri: `_metodo/professionale/alto/REGISTRO-CARATTERI.md`. Regole: sezione D di `_metodo/professionale/ALTO-LIVELLO.md` per la prima schermata; sotto, i contenuti e le funzioni della versione professionale su una griglia sola.

Rifare le misure: `node _prova/alto/misura-d.mjs [ora]` (copia estesa di `alto/diagnosi/misure/misura.mjs`; scrive `_prova/alto/misure/`). Controlli, prove d'uso e screenshot di questa cartella: `node _prova/alto/controlli.mjs`. Immagini: `python3 -I _prova/alto/script/alto_img.py`. Provini delle foto: `_prova/alto/provini.jpg`. Confronto delle prime schermate (professionale, ibrida, Tartine, Hart): `_prova/alto/confronto-1440.jpg`; schermate dei concorrenti rifatte il 3/11 in `_prova/alto/concorrenti/`.

Screenshot (stessi nomi, rifatti dopo il ritocco "Alto livello" qui sotto; ora simulata martedì 3 novembre 2026 alle 10, in stagione di Natale): `home-1440.jpg` (6972 px; prima del ritocco 7271), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8529 px; prima 8344), `home-390-prima-schermata.jpg`, `home-1024-prima-schermata.jpg`, `home-768-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Chi siamo" al piede). Guardati a pezzi accanto alla versione professionale, a Tartine e a Hart Bageri.

### Secondo giro (3 novembre 2026, notte)

Dopo il voto del giudice da agenzia (6,5) e le prove dei clienti tipo (cliente 1 da 8,5 a 7,5, cliente 2 da 8 a 7). Due obiettivi insieme: riportare i compiti persi dai clienti tipo senza rompere i tetti D3, e l'esecuzione sotto la piega. La pagina di prima è copiata in `_prova/alto/sito-prima-del-secondo-giro/`; immagini con `python3 -I _prova/alto/script/secondo_img.py`, prove e confronti in `_prova/alto/secondo/`.

**Per i clienti tipo.** Sul telefono le righe delle sedi dicono anche il seguito: "Aperto fino alle 13.45, poi 16.30-20.00", "Aperto fino alle 13.45, pomeriggio chiuso", "Oggi orario al telefono; lunedì dalle 8.30", "Chiuso, sabato orario al telefono; lunedì dalle 8.30" (il venerdì sera); al computer la riga resta corta, per il tetto dei 160 caratteri, e la scheda del negozio dice "chiude alle 13.45 e riapre alle 16.30". "Chiuso" è in rosso mattone (#A3341F), "Aperto" in verde; nella barra del telefono un pallino verde o rosso accanto a "Chiama via Vigonovese" (nessun pallino per via Alsazia finché non è confermata); nella testata a 1440 "Via Vigonovese aperto" accanto a "Chiama 049 870 26 58". Il menu del telefono ha "Scriveteci" e, sotto un filetto, "Indicazioni per via Vigonovese 116" e "Indicazioni per via Alsazia 3" (2 tocchi da qualunque punto); in stagione la voce delle Feste diventa "Natale: si prenota". Nella seconda schermata del telefono "Indicazioni" viene subito dopo lo stato, prima della tabella (via Vigonovese a 1162 px, via Alsazia a 1570, entro due schermate). La riga delle prenotazioni sul telefono nomina il prodotto ("Panettone e focaccia di Natale: prenotazioni aperte"), porta al titolo della sezione (`#t-feste`, a 76 px) e fuori stagione sparisce davvero (`[hidden]` vinceva su `display:flex`). Nella sezione delle Feste, subito dopo l'introduzione, c'è "Chiamaci e ordina: 049 870 26 58" (la frase del sito di oggi) con accanto la riga "Pezzature, prezzi e ultimo giorno utile"; sul telefono l'ordine è titolo, panettone in 3:2 (390x260, intero), introduzione, bottone, nota: tutto in una schermata sopra la barra. Con `SCRIVI_SCADENZA` a true la data va anche nella riga dell'apertura. La strada per i locali non ripete più il titolo e dice la frase della scheda con il numero del laboratorio.

**Sotto la piega.** Apertura a 1440: le assi sono basse (150 px) con lettere di 70 px (rapporto 0,47, come l'insegna vera), cornice di 4 px e nessuna ombra interna; sotto l'insegna la porta vera con Galileo e Fidalma (taglio 546x256 della foto, misura nativa, 10,8% dello schermo: resta sotto il 12% di D2) sulle colonne 1-5, e a destra, dalla colonna 7, l'`h1` a 44 px allineato alla foto in alto e le sedi allineate alla foto in basso. Il vuoto in basso a sinistra non c'è più e la facciata arriva al fondo dello schermo anche a 1920. "Galileo" è ricalcato di nuovo sulla foto, con la G a sperone e ricciolo e la "a" chiusa (`_prova/alto/secondo/ov3.png`), e le lettere sono disegnate una volta sola e riusate nel piede, dove l'insegna torna una volta, piccola, al posto della frase ripetuta. La vetrina intera non è più nei negozi (era la stessa foto della porta). Gerarchia: `h1` 44, `h2` 34 ovunque (1,29), nomi 24, frasi dette 27. Griglia: tre soli tagli a 1440 (colonna 5 a 504, 7 a 732, 9 a 960) e tutti i bordi destri a 1392; le tartarughe passano alla colonna 9-12 (432x540, finiscono con l'elenco), la focaccia alle colonne 1-5 come la porta. Moduli diversi: negozi con titolo e introduzione sulla stessa linea e tre strade; Feste con la foto dominante a tutta griglia e la didascalia vera ("Panettone di Natale, con l'antica ricetta di Galileo / dicembre 2020"), poi focaccia e la frase di Fidalma citata com'è al Mattino; pane con l'elenco in tre colonne e i pani di casa in due righe bilanciate (niente "Zoccoletto" da solo); storia con la frase su tutta la riga, poi racconto e clienti affiancati, poi i giornali; modulo; piede. Panini imbottiti uniti a pizze e focacce. Tartarughe riportate al colore della serie (saturazione 58, blu/rosso 0,88). `text-wrap:pretty` sui paragrafi.

**Misure finali** (`node _prova/alto/misura-d.mjs`, 3/11/2026 alle 10, e di nuovo alle 18.15 e venerdì 6/11 alle 20.05): 35 soglie su 35. Foto nella prima schermata a 1440 10,8%; 6 cliccabili, 1 bottone, 143 caratteri (155 il venerdì sera); a 390 4 cliccabili, 1 bottone, insegna e porta 50,2%; lettere dell'insegna 70 px; 743 parole, 6 sezioni, 6569 px a 1440 (prima 6972); `tel:` 2 a 1440 e 3 a 390; 3 bottoni pieni; 3 formati (2,1, 1,5, 0,8); peso 602 KB a 1440 e 266 KB a 390. La soglia interna "numeri scritti" è passata da 2 a 4 per il numero di via Vigonovese (testata, scheda, forniture, Feste: ognuno accanto al suo compito). Controlli (`node _prova/alto/controlli.mjs`): nessuno scorrimento orizzontale e nessuna sovrapposizione a 320, 390, 768, 1024, 1440 e 1920; altezze 8705, 8341, 7435, 5883, 6569 e 6752 px; nessun errore di script; compiti della scheda tutti in vista (stato e prenotazioni senza scorrere, Chiama in vista in ogni punto, titolo, panettone, bottone e nota delle Feste in una schermata sul telefono, forniture con titolo, mail e numero, l'elenco dei pani in una schermata). Screenshot rifatti con gli stessi nomi e guardati a pezzi.

**Restano aperti**: D8 stretto (743 parole contro 650, 6569 px contro 6000) per scelta del metodo ibrido; "Indicazioni" una volta per negozio (due negozi); la porta sul telefono a densità 2 o 3 resta morbida (390 px sono già la misura vera della foto: serve la foto nuova); i voti del giudice e dei clienti tipo su questa versione vanno rifatti.

### Alto livello: ritocco dopo il giudice da agenzia (3 novembre 2026, sera)

Il giudice da agenzia aveva dato 6,5 (versione professionale 5,5): salto vero, ma insegna che pareva un banner centrato come una slide, "Galileo" in Young Serif al posto del corsivo vero, colonna destra che partiva da sei punti, buchi a sinistra in tre sezioni, culmine solo a 1440, via Alsazia data per certa. Ritocco su `sito/index.html` senza tornare indietro sulla sezione D; la pagina com'era prima è in `_prova/alto/ritocco/index-prima-del-ritocco.html`. Script nuovi: `_prova/alto/script/ritocco_img.py` (tagli nuovi, stesso trattamento della serie), `_prova/alto/ritocco/vedi.mjs` (prime schermate), `bordi.mjs` (bordi sinistri dei blocchi, colonne, legno fuori dalle assi, h1 e h2), `flag.mjs` (prova di `ALSAZIA_CONFERMATA=true` senza toccare la pagina). In `misura-d.mjs` il gesto a 390 ora si misura come insegna più foto (non più tutta la facciata) e le due figure al vivo del telefono (`data-al-vivo`) non contano per i margini; in `controlli.mjs` la vetrina a 390 è la porta dell'apertura e c'è l'altezza del panettone rispetto allo schermo.

**Applicati**
- **Via Alsazia non più data per certa**: interruttore `ALSAZIA_CONFERMATA=false` nello script. Finché è falso la riga dell'apertura e la scheda dicono "Orario al telefono" / "Orario di oggi al telefono." (anche senza JavaScript), il cellulare è scritto ma non è un collegamento, il Chiama della testata non passa mai a via Alsazia. Con `true` tornano stato, cellulare e cambio di numero (provato con `flag.mjs` a mercoledì 17, martedì 10 e sabato 10). È la prima domanda del `LEGGIMI.md`.
- **Apertura in alto, non centrata**: tolto il centraggio. L'insegna parte a 40 px sotto la testata (y 112) ed è alta 290 px, il 30,1% della prima schermata a 1440 (prima 214 px, 21,8%). Sotto, a 44 px, l'`h1`; le sedi sono sul bordo basso, a 48 px dal fondo (686-852). Vuoto sopra l'insegna 40 px, sotto le sedi 48 px.
- **Il legno solo sulle assi**: i bottoni (testata, Chiama dei negozi, Prepara l'email), il filo del focus e i radio passano al bruno #33261F (al passaggio #1E1612, più scuro, non sbiadito). Le assi hanno la modanatura di 8 px in #56291A, raggio 0, senza l'ombra esterna. `bordi.mjs`: nessun elemento fuori dalle assi usa rgb(106,56,37).
- **"Galileo" ricalcato dal corsivo vero**: tracciato in SVG sulla foto 617993_02eb45f6 ingrandita 8 volte (`_prova/alto/ritocco/galileo-zoom.png`, `overlay.png` con il ricalco sopra la foto), a filo unico di spessore costante, con il punto della i. Le maiuscole sono alte come quelle di FORNASIERO (stessa variabile `--lettera`, 69 px a 1440, 30 a 390) e i tratti hanno lo stesso spessore (6,6-6,8 px). Per tenere uguali le due altezze con le assi nelle proporzioni vere (circa 2 a 1, 856 e 432 px a 1440) le lettere sono scese da 90 a 69 px; in compenso FORNASIERO è più spaziato, come sull'insegna (fuga tra le lettere da 44 a 64 unità).
- **Civico 116 sul pilastro**: fuga tra le assi di 56 px a 1440 (minimo 48, così l'ovale non tocca le assi a 768), ovale al centro della fuga a metà altezza, smalto bianco #FBF9F5 con filo bruno di 1 px.
- **Due soli tagli della griglia**: colonna destra sempre dalla 7 (x=732) per sedi, vetrina (`justify-self:start`), testo delle Feste, frase di Fidalma, tartarughe, clienti, campi del modulo; le tre strade, le righe del banco, gli articoli del Mattino e le colonne del piede su 48, 504, 960. `bordi.mjs` a 1440: bordi sinistri dei blocchi solo 48, 504, 732, 960.
- **Negozi e orari**: titolo in alto e introduzione (ora 22 px) in basso, sulla linea della didascalia della vetrina (1365 e 1365).
- **Dal 1963**: a sinistra la frase-firma e il racconto, a destra solo i clienti di un tempo (le due colonne finiscono tutte e due a 5655); "Hanno scritto di noi" sotto, in tre colonne su tutta la griglia. La sezione si è accorciata di circa 250 px.
- **Scriveteci**: a sinistra titolo, riga e "Che cosa vi serve" con i quattro radio in colonna; a destra i campi (stessa altezza, 463 px). Niente più fondo pietra vuoto prima del piede.
- **Culmine sul telefono**: sotto i 700 px il panettone è un taglio 4:5 dall'originale b56ebf_5b27b00f (`panettone-4x5-780.webp`, 780x975, con `<picture>`), al vivo: 390x488 a 390 (prima 358x239). La focaccia resta 3:2 con i margini.
- **Tartarughe**: taglio 4:5 dall'originale 617993_28aa18bc, 1024x1280, con due tartarughe intere e il sacchetto "Fornasiero, Camin-Padova" in alto, bilanciato sul bianco del sacchetto (moltiplicatori 0,92 / 1,01 / 1,09), poi curva e saturazione 0,88 della serie: la luce gialla della lampada è sparita. 546x682 a 1440; la colonna finisce a 4747 come l'elenco, che ora ha le righe di filo (prima 4525 contro 4779). Le file vecchie (3:2) sono in `_prova/alto/ritocco/img-tolte/`.
- **Gerarchia**: `h1` 40/46 px a 1440, `h2` 38/44 (prima 34 e 44).
- **Testi d'istruzione**: "Pezzature, prezzi e ultimo giorno utile: al banco o al telefono." è a 14 px sotto l'introduzione delle Feste; "Per i locali, chiamate il laboratorio..." è diventata un fatto ("Zona, giorni e ora di consegna si concordano con il laboratorio di via Vigonovese."); "Per gli altri tipi chiedete al banco." è tolta; "Per le cose di oggi, meglio chiamare il negozio." è a 14 px accanto a "Prepara l'email", con la riga del programma di posta; "Oppure scrivete a" è diventato "Per email:" con "(oggetto già scritto: Fornitura pane)" a 14 px; nelle schede "chiedete al telefono" è diventato "orario al telefono".
- **Link `tel:` (D12)**: 3 a 1440 (testata e i due Chiama delle schede; il cellulare non è più un collegamento) e 2 a 390 (la barra; sotto i 700 px i Chiama delle schede sono nascosti, la barra è sempre in vista).
- **Il gesto sul telefono (D3)**: sotto l'insegna c'è la porta di via Vigonovese con Galileo e Fidalma, taglio 390x256 della foto della vetrina sotto l'insegna vera, al vivo e alla misura nativa, con la didascalia "Galileo e Fidalma sulla porta / via Vigonovese 116". Insegna 20,2% e foto 30,3%: 50,5% dello schermo (prima l'insegna sola era il 15%). La porta si riconosce già nella prima schermata (fondo a 516 px), le sedi e la riga delle prenotazioni restano sopra la barra (fondo 754 anche quando la riga di via Vigonovese è lunga, la sera). Sul telefono la vetrina di "Negozi e orari" è nascosta per non ripeterla e "vicino al semaforo" è passato nella scheda di via Vigonovese.
- **Righe dello stato**: nella riga dell'apertura la forma corta ("Chiuso, domani dalle 8.30"), nella scheda quella intera ("riapre domani mattina dalle 8.30"), che risolve anche il mercoledì pomeriggio; "Oggi è festa: chiamate" è diventato "Festa: orario al telefono".
- **Parole e altezza (D8)**: 745 parole (prima 780; accorciato l'elenco dei dolci, tolte due frasi d'istruzione) e 6972 px a 1440 (prima 7271).

**Respinti, con il motivo**
- **Insegna alta 300 px con lettere di 90**: non si possono avere insieme lettere di 90 px, "Galileo" alla stessa altezza e le due assi affiancate nelle proporzioni vere dentro 1344 px. Ho tenuto le proporzioni e le altezze uguali (lettere 69 px) e l'asse a 290 px, quindi il 30% c'è, ma l'asse è più alta di quella vera (le lettere stanno a un quarto dell'asse, sulla facciata a metà).
- **"Indicazioni" una volta sola (D12)**: i negozi sono due e ognuno ha la sua strada; resta un "Indicazioni" per scheda, più quello del menu sotto i 1100 px (V1.3 dei clienti tipo).
- **D8 stretto (450-650 parole, 4000-6000 px)**: vale la scelta del metodo ibrido, che tiene sotto la prima schermata le funzioni della versione professionale (tabelle degli orari, forniture, il pane con i nomi, il banco, le prove, il modulo). Si è scesi a 745 parole e 6972 px; per arrivare a 650 andrebbero tolti il banco o i clienti di un tempo, che servono ai clienti tipo e al D9.
- **Somiglianza di colore con Ruffatti**: il bruno dell'insegna è campionato sulla loro foto e non si cambia; ora il legno sta solo sulle assi, la modanatura e il corsivo le distinguono dal campo pieno con il corsivo d'ottone di Ruffatti.

**Misure finali** (`node _prova/alto/misura-d.mjs`, 3/11/2026 alle 10; dettaglio in `_prova/alto/misure/misure-2026-11-03T1000.json`): tutte le 35 soglie passano. Foto nella prima schermata a 1440 0%; cliccabili 6 a 1440 e 4 a 390; un bottone; 143 caratteri fuori dalla testata; a 390 insegna e foto 50,5%; nessuna cifra grande, nessun occhiello; `h1` di 6 parole visibili e una virgola; due famiglie, testo 18 px; un solo elemento oltre i 100 px (l'insegna); 745 parole, 6 sezioni, 6972 px; margini 48/48 in tutte le sezioni a 1440 e 16/16 a 390; nessuna foto ingrandita; formati 2.0, 1.5, 0.8; tre fondi (bianco, pietra, legno delle sole assi); spazi tra le sezioni 112 e 168; `tel:` 3 a 1440 e 2 a 390; 4 bottoni in pagina; 732 KB a 1440 e 389 KB a 390; nessun U+2014; nessun errore. `controlli.mjs`: nessuno scorrimento orizzontale e nessuna sovrapposizione a 320, 390, 768, 1024, 1440 e 1920 (altezze 8978, 8529, 7954, 6240, 6972, 7135); stato e stagione giusti alle 11 date e ore; compiti della scheda: stato e prenotazioni senza scorrere a 390 e 1440, Chiama sempre in vista, forniture, mail e pani in una schermata dall'àncora. A 390 il panettone (488 px) sta intero in uno schermo ma non insieme al titolo della sezione; a 1440 (896 px) idem: si vede intero con un piccolo scorrimento.

**Da rifare**: i voti del giudice e dei clienti tipo su questa versione; il foglio delle miniature a 300 px con persone vere (il mestiere sul telefono ora si vede dalla vetrina, a 1440 resta affidato all'`h1`); "Galileo" ricalcato va fatto vedere alla famiglia insieme a FORNASIERO.

### Che cosa era cambiato con il metodo ibrido (prima del ritocco)

- **Idea e gesto (D1, D4 modello A)**: la home apre con l'insegna di legno della bottega ridisegnata. Le lettere FORNASIERO sono tracciate in SVG come quelle vere (bastone monolineare, inclinate, molto spaziate, crema sul legno #6A3825 campionato dalla loro foto), con la targhetta del civico 116 sotto la fuga e la seconda asse "Galileo". L'insegna sta sulla pietra chiara della facciata, non su un fondo scuro. Sotto, l'`h1` "Fornai anche nel nome, a Camin." (la frase di Galileo al Mattino del 2013, "Siamo Fornasiero, fornai anche nel nome.", accorciata) e sul bordo basso le due sedi in due righe con lo stato di adesso, più in stagione la riga "Prenotazioni di Natale aperte".
- **Foto (D2)**: l'insegna vera è 640x319, quindi l'apertura è di tipografia e nella prima schermata a 1440 non c'è nessuna foto (0%). La vetrina con Galileo e Fidalma apre la seconda schermata, alla misura nativa, con la didascalia "Galileo e Fidalma sulla porta / via Vigonovese 116, vicino al semaforo".
- **Testata**: nome, quattro voci (Negozi e orari, Il pane, Natale e Pasqua, Per bar e ristoranti) e un solo bottone "Chiama 049 870 26 58", che passa al numero di via Alsazia quando è aperta solo lei. Sotto i 1100 px le voci vanno nel menu, con in più "Indicazioni per via Vigonovese 116"; sotto i 700 px il bottone della testata lascia il posto alla barra fissa in basso con i due Chiama (via Vigonovese e via Alsazia, numero scritto, 64 px).
- **Sotto la piega, sei sezioni sulla stessa griglia a 12 colonne** (margini 48 px a 1440 e 16 px a 390, bordi destri allineati in tutte):
  1. apertura;
  2. Negozi e orari: la vetrina, poi tre strade divise per bisogno: via Vigonovese 116 (stato di adesso, tabella degli orari, Chiama, Indicazioni), via Alsazia 3 (lo stesso, più il cellulare) e "Per bar, alberghi, ristoranti e rivendite" (le loro frasi, chi chiamare e che cosa chiedere, la mail che ha già l'oggetto "Fornitura pane" e la traccia, le consegne a domicilio, "Vedi i pani che facciamo");
  3. Natale e Pasqua, la sezione culmine (2013 px a 1440): il panettone sul sacco di juta su tutta la griglia (1344x896) con la didascalia "Panettone di Natale, con l'antica ricetta di Galileo / laboratorio di via Vigonovese, dicembre 2020", la focaccia del cinquantesimo e la frase di Fidalma "Le nostre focacce, preparate come 50 anni fa.";
  4. Il pane di ogni giorno: i cinque pani con il nome di casa in Young Serif, gli altri quindici, la foto delle tartarughe, e il banco (paste all'uovo, pizze e focacce, panini, dolci con la Bacheca di Romina) in righe d'indice al posto delle tessere con le cifre;
  5. Chi siamo: la frase-firma, la storia in un paragrafo con le persone per nome (gli zii Domenico e Pasquale, Galileo, Fidalma, Filippo, Romina, Michele Daniele), i clienti di un tempo con il nome e i tre articoli del Mattino;
  6. Scriveteci: il modulo con il tipo di richiesta (mailto, da collegare a un servizio).
- **Tolto rispetto alla versione professionale**: il titolo maiuscolo e i due negozi con sei righe d'orari in apertura; la fascia scura del manifesto con le cinque cifre (1963, 30+, 2, 60, 400); le date con gli anni a 56 px; le tessere con le cifre grandi (4, 4 + 4, 6); i due Chiama della sezione delle Feste e il telefono grande delle forniture (il numero resta sempre in testata o nella barra); il blocco color legno delle forniture; la seconda frase di Galileo; le righe d'interfaccia in vista ("Si può anche chiamare", "Il modulo prepara l'email..." a 19 px: ora c'è solo una riga di 14 px accanto al bottone); "Chi siamo" nel menu.
- **Caratteri (D5)**: Young Serif 400 e Albert Sans 400/600, SIL OFL 1.1, in `sito/fonts/` con le licenze; escono Sentient e General Sans (General Sans è fuori catalogo). Il lettering dell'insegna non è un carattere.
- **Colori (D11)**: tre fondi oltre al piede (bianco, la pietra #ECE6DF dell'apertura e del modulo, il legno delle sole due assi dell'insegna); il colore del marchio pieno solo sull'insegna e sui bottoni; piede e barra nel bruno del sacchetto. Spazi tra le sezioni di 112 px e, per il culmine, 168 px.
- **Foto (D10)**: quattro, tutte loro (vetrina, panettone, focaccia, tartarughe), con un solo trattamento (bilanciamento verso il neutro, curva leggera, saturazione 0,88), due formati (2:1 e 3:2), nessuna ingrandita né scurita. Le tartarughe tornano in pagina: con il bilanciamento la luce gialla della lampada si legge molto meno. Gli originali sono stati riscaricati il 3/11 in `assets/originali/` (erano stati cancellati con il riavvio).

### Misure del metodo ibrido prima del ritocco (`misura-d.mjs`, martedì 3/11/2026 alle 10)

| Misura | Soglia | 1440x900 | 390x844 | Versione professionale |
|---|---|---|---|---|
| Foto nella prima schermata | 60% o più, oppure sotto il 12% | 0% (apertura di tipografia) | 0% | 10,4% (vetrina 520 px) |
| Cliccabili nella prima schermata | 6 (390: 4) | 6 (4 voci, Chiama, prenotazioni) | 4 (Menu, prenotazioni, i due Chiama della barra) | 14 (390: 9) |
| Bottoni nella prima schermata | 1 | 1 | 1 (la barra, un componente con due chiamate) | 6 |
| Caratteri fuori dalla testata | 160 | 153 (FORNASIERO contato come 10) | 269, compreso l'inizio della seconda sezione | 686 |
| Gesto o foto a 390 | almeno 50% | | facciata con l'insegna 72% (l'insegna sola 15%) | |
| Cifre di 30 px o più, file di ingressi, occhielli | 0 | 0 | 0 | un occhiello sopra il titolo |
| `h1` | 9 parole, 1 virgola | "Fornai anche nel nome, a Camin." (6 visibili, 9 con il nome nascosto per i lettori di schermo) | | |
| Elemento sopra i 100 px | 1 | l'insegna, lettere alte 90 px | | |
| Famiglie, testo | 2, almeno 17 px | Young Serif, Albert Sans; 18 px | 17 px | |
| Parole | 900 | 780 | | 1079 |
| Sezioni | 7 | 6 più il piede | | 6 più il piede, con 8 blocchi |
| Altezza | 7.500 px | 7271 | 8344 | 7257 |
| Griglia | stessi margini, bordi destri allineati | 48/48 in tutte le 7 | 16/16 in tutte | |
| Foto ingrandite, formati | 0, al massimo 3 | 0, 2 | 0 | |
| Fondi oltre al piede | 3 | 3 | | |
| Link `tel:` visibili per numero | 2 | via Vigonovese 2, via Alsazia 1, cellulare 1 | 2, 2, 1 | via Vigonovese 8, via Alsazia 4, cellulare 3 |
| Indicazioni | 2 per negozio | 1 e 1 (più quella del menu sotto i 1100 px) | | 6 |
| Bottoni in pagina | 5 | 4 | 4 | |
| Peso | 3 MB | 664 KB | 262 KB | |

Tutte le 35 soglie passano. Elenco completo: `_prova/alto/misure/misure-2026-11-03T1000.json`; la versione professionale misurata con lo stesso script è in `_prova/alto/misure-pro/` (`SITO=... OUT=... node misura-d.mjs`).

### Controlli

- Nessuno scorrimento orizzontale e nessuna sovrapposizione a 320, 390, 768, 1024, 1440 e 1920 (`controlli.mjs`, confronto a coppie dei rettangoli di testo, foto e bottoni); nessun errore di script. Corretti durante il lavoro: lo spazio vuoto in mezzo all'apertura (il gruppo ora sta al centro e la facciata non supera 740 px), i titoli staccati dal testo in "Negozi e orari" e "Chi siamo", le colonne del piede, la riga di via Vigonovese che andava a capo da sola a 390 e 768, il nome e la barra a 320, i `sizes` delle foto che facevano scegliere un file troppo piccolo, i preload dei caratteri che davano errore da file://.
- Collegamenti: `tel:+390498702658`, `tel:+390498705107`, `tel:+393386600664`; `mailto:info@panificiogalileofornasiero.it` (nelle forniture con oggetto "Fornitura pane" e la traccia; nel piede semplice; il modulo compone oggetto "tipo, nome"); nessuna àncora rotta.
- Stato e stagione provati a 11 date e ore: aperti, pausa di pranzo, sera, mercoledì pomeriggio (via Vigonovese chiusa, via Alsazia apre alle 16.30), sabato (via Vigonovese "Oggi orario al telefono", testata che chiama via Alsazia), domenica, 8 dicembre, 16 dicembre ("Natale: chiamate per sapere se c'è posto"), 23 dicembre dalle 13 (riga spenta), 20 ottobre (fuori stagione, riga nascosta), 20 marzo 2027 (Pasqua). Senza JavaScript le righe delle sedi dicono gli orari dal lunedì al venerdì e la riga "Natale e Pasqua su prenotazione".
- Contrasto: testo bruno su pietra 11,8:1, grigio su pietra 5,9:1, verde "Aperto" su pietra 5,3:1, crema sul legno 7,9:1, crema sul bruno 12:1. Focus visibile (filo di 3 px nel legno). Alt veri su tutte le foto; l'insegna ha la sua descrizione.
- Nessun U+2014 nella pagina, in questa nota, nella direzione e negli script nuovi.

### I compiti della scheda d'uso, e dove stanno ora

| Compito | Dove | Esito della prova |
|---|---|---|
| V1.1 aperto adesso e quale negozio | apertura, le due righe delle sedi (390: entro 500 px) | senza scorrere a 390 e 1440 |
| V1.2 chiamare il negozio giusto | 390: barra fissa con i due Chiama, numero scritto, 64 px, a ogni punto della pagina; da 700 px il bottone della testata | passa; nella prima schermata non c'è più il bottone dentro la scheda del negozio |
| V1.3 Indicazioni e riconoscere la porta | menu (sotto i 1100 px) e scheda del negozio; la vetrina con l'insegna e "vicino al semaforo" finisce a 1017 px a 390 | due tocchi invece di uno (Menu, Indicazioni); la porta si riconosce entro due schermate |
| V1.4 l'elenco dei pani | voce "Il pane" | a 390 i nomi di casa e i quindici pani stanno in una schermata dall'àncora |
| V2.1 prenotazioni aperte | riga "Prenotazioni di Natale aperte" in prima schermata (fondo a 565 px a 390), solo in stagione | passa |
| V2.2 prenotare al telefono | barra (390) o testata (1440), sempre in vista anche nella sezione delle Feste | la sezione non ha più i suoi due Chiama (regola delle ripetizioni) |
| V2.3 vedere che cosa si prenota | la riga porta al titolo "A Natale, la ricetta di Galileo"; a 390 il panettone intero sta nella schermata, la focaccia subito dopo | passa a 390; a 1440 il panettone, largo 1344 px, si vede intero solo scorrendo |
| V2.4 fino a quando e quanto costa | "Pezzature, prezzi e ultimo giorno utile: chiedete al banco o al telefono" accanto all'introduzione; con `SCRIVI_SCADENZA=true` scrive la data | passa (la data va chiesta) |
| V3.1 trovare la fornitura | voce "Per bar e ristoranti", terza strada di "Negozi e orari": titolo, mail e, nella stessa riga a 1440, il Chiama del laboratorio | passa |
| V3.2 a chi chiedere e che cosa | "Per i locali, chiamate il laboratorio di via Vigonovese per sapere se arriviamo fino a voi, in che giorni e a che ora." | passa |
| V3.3 che pani fanno | "Vedi i pani che facciamo", elenco intero in una schermata a 1440 | passa |
| V3.4 scrivere | mail con oggetto "Fornitura pane"; modulo "Scriveteci" con "Fornitura per bar, albergo, ristorante o rivendita" | il telefono non è più scritto accanto al modulo: sta nella testata, sempre visibile |

### Problemi aperti

- **L'insegna ridisegnata va fatta vedere alla famiglia**: è la loro insegna, rifatta a mano per lo schermo (lettere, inclinazione e civico guardati sulla foto 640x319; dal ritocco del 3/11 anche "Galileo" è il corsivo dell'insegna, ricalcato). Con una foto nuova dell'insegna ad alta risoluzione si possono correggere le proporzioni delle lettere.
- **Nessuna foto nella prima schermata a 1440**: il mestiere si legge da "Fornai" nell'`h1`, da "Panificio" in testata e dalla riga delle prenotazioni di Natale, non da un'immagine. Il controllo D1 delle miniature a 300 px (indovinare il mestiere senza il logo) non è stato fatto con persone: è il rischio principale. Con un servizio fotografico (la vetrina e il banco di mattina, almeno 4000 px) l'apertura può passare alla strada della foto al 60% o più.
- La didascalia del panettone dice "laboratorio di via Vigonovese, dicembre 2020": la data viene dai dati della foto (Nikon D3300, 5/12/2020), il luogo è dedotto (è il loro unico laboratorio). Da confermare.
- D12, link `tel:`: risolto nel ritocco del 3/11 (3 a 1440, 2 a 390).
- Fuori stagione la sezione culmine resta "Natale e Pasqua" con il panettone: è la foto migliore che hanno, ma da gennaio a febbraio e da maggio a ottobre parla di una cosa che non si può prenotare. Con le foto nuove del pane di ogni giorno il culmine fuori stagione dovrebbe passare al pane.
- "Indicazioni" sul telefono chiede due tocchi (Menu, poi Indicazioni) o uno scorrimento fino alla scheda del negozio; la porta però si riconosce già nella prima schermata.
- Nel `REGISTRO-CARATTERI.md` la mia riga dice che Albert Sans non è in altre home: nel frattempo l'ha presa anche AIT Studio Stefano Aiti (Rubano e Mestrino, altra zona). Sono 2 home su 45, dentro il limite; la riga non l'ho riscritta per non toccare il file mentre altri agenti ci aggiungono righe.
- Restano da chiedere le cose della nota di prima: data di chiusura delle prenotazioni, pezzature e prezzi, sabato di via Vigonovese, domeniche e ferie, via Alsazia 3 e il cellulare, zona servita per i locali, consenso a nominare i clienti di un tempo e a citare il Mattino, consenso per la foto e i nomi di Galileo e Fidalma.
- I voti del giudice da agenzia e dei clienti tipo non sono stati rifatti in questo passaggio.

---

## Nota di prima: livello professionale (3 novembre 2026)

## Livello professionale

Pagina: `sito/index.html` (statica, si apre con file:///). La versione 1 con l'uso com'era prima di questo passaggio è copiata in `_prova/versione-1-uso/` (sito e screenshot). Regole seguite: `_metodo/professionale/REGOLE.md`, sezione A per la famiglia B (botteghe artigiane e alimentari), sezione B (difetti delle nostre home), sezione C (15 regole). Riferimenti guardati: le prime schermate a 1440 e 390 di tutti e 14, le pagine intere di Joseph Brot e Union (a pezzi) e il piede di Poilâne.

Rifare tutto: `bash _prova/script/build_finale.sh --immagini` (immagini con `pro_img.py`, screenshot all'ora simulata lunedì 2 novembre alle 10, poi `pro_controlli.mjs`). Prove d'uso della scheda: `node _prova/script/pro_uso.mjs`. Misure della prima schermata: `node _prova/script/pro_misura.mjs <larghezza> <altezza> [mobile] [ora]`.

Screenshot (stessi nomi di prima, rifatti dopo il ritocco finale): `home-1440.jpg` (7337 px), `home-1440-prima-schermata.jpg`, `home-390.jpg` (11884 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg` (da "Negozi e orari" al piede). Guardati a pezzi a 390 e 1440 accanto ai riferimenti, e a 320, 768, 1024, 1280 e 1920.

### Ritocco finale (3 novembre 2026, dopo il controllo del livello e le prove dei tre clienti tipo)

Controllo del livello (voto 6, regole 5, 9 e 10 non passate) e prove dei clienti tipo (`_prova/pro-prova-0/1/2/`). Script: `_prova/script/ritocco_pro2.py` e `ritocco_pro2b.py` (le sostituzioni), `ritocco_misura2.mjs` (prima schermata a 8 ore e date), `pro_img.py` (vetrina scaldata, logo del piede tolto).

**Applicati**
- Titolo senza "Forna/forna" colorati: stesse parole, tutto nel bruno (SCHEDA par. 5 e 8).
- Apertura a 1440: vetrina da 411 a 520 px (nativa 640), nelle righe dello stato e dei negozi col fondo allineato ai bottoni; il titolo resta libero su tutta la larghezza; didascalia di una riga "Galileo e Fidalma, via Vigonovese 116, vicino al semaforo."; tolto "panificio a Camin dal 1963" accanto al nome in testata (ripeteva l'occhiello).
- Gerarchia dei bottoni: nella fascia delle Feste il Chiama è a filo; sul telefono la fascia è compatta ("Prenotazioni aperte", "Panettone e focaccia di Natale", "Come si prenota", tutta toccabile) e finisce a 810 px (lunedì) e 835 (domenica) su 844; dal 15 dicembre dice "Chiamate per sapere se c'è ancora posto".
- Testata: il bottone dice anche il negozio ("via Vigonovese" o "via Alsazia"), aggiornato con l'href.
- Righe dei negozi: le eccezioni su righe fisse; il giorno che coincide con oggi non si ripete (mercoledì e sabato); via Alsazia scrive "Mercoledì pomeriggio aperto."
- "Indicazioni" apre il percorso (`google.com/maps/dir/?api=1&destination=...`).
- Vetrina intera sul telefono e fino a 1099 px subito dopo la fascia (390: a 830 px invece di 3308); tolta da "Chi siamo" (non è più ripetuta).
- Feste: nome dei prodotti sotto le foto ("Panettone di Natale, con l'antica ricetta di Galileo", "Focaccia di Natale, la focaccia veneta, con la glassa e le mandorle"); i bottoni subito dopo l'introduzione; "Via Alsazia 3" ora è un bottone a filo di 48/52 px. Sul telefono: titolo, introduzione, i due Chiama, panettone, la frase di Fidalma, focaccia.
- "Hanno scritto di noi": testata e data piccole, titolo vero dell'articolo in Sentient 24 px.
- Clienti con il nome in una fascia nelle forniture, sotto il telefono del laboratorio (dall'àncora "Per bar e ristoranti" si vedono telefono e mail con oggetto).
- Laboratorio: tre tessere con un dato grande al posto della foto e link pertinenti; tolta la tessera "Il pane".
- Chi siamo: frase di Galileo accanto al titolo con un filetto nel legno; le quattro date in orizzontale con gli anni a 56 px (secondo gesto di scala dopo le cifre).
- Vetrina scaldata e allineata al contrasto delle foto Nikon.
- Piede: la parola FORNASIERO al posto del logo a cesto.
- Meccanismo per la scadenza delle prenotazioni: `SCRIVI_SCADENZA` in cima allo script (oggi `false`); con `true` fascia e sezione scrivono "entro lunedì 15 dicembre".

**Respinti, con il motivo**
- Scrivere oggi in pagina la data di chiusura delle prenotazioni (cliente 2, bloccante): la data dello script (15 dicembre) è una scelta della proposta, non un dato del panificio. Il meccanismo è pronto, la data va chiesta (LEGGIMI).
- Prezzi e pezzature indicativi: non sono nelle fonti.
- Zona servita per i locali (cliente 3): non è scritta da nessuna parte; resta "chiamate per sapere se arriviamo fino a voi".
- Foto o riferimento scritto per via Alsazia 3: non c'è una foto né un punto di riferimento nelle fonti; da chiedere.
- Striscia dell'insegna più alta (80-100 px) e fascia sopra i negozi o entro 640 px (Safari con le barre): sul telefono non c'è posto senza spingere fuori dalla prima schermata i telefoni dei negozi, che per la SCHEDA (par. 4) vengono prima; al posto della striscia più alta c'è la vetrina intera subito dopo la fascia.
- Miniatura del panettone nella fascia: stesso motivo di spazio sul telefono.
- Etichette "laboratorio e negozio" / "negozio" sul telefono: tornano da 600 px in su (ora su una riga propria), sotto no per lo spazio.
- "Chiama e prenota" al posto di "Chiamaci e ordina": "Chiamaci e ordina" sono parole loro (sito e Bacheca).
- Foto nelle tessere: decisione del committente sulle foto.

### Che cosa era cambiato nel livello professionale, in breve

- **Struttura della famiglia B adattata**: testata con "Negozi e orari" come prima voce e il telefono in un bottone; apertura con il mestiere, il luogo, la prova (dal 1963), i due negozi con Chiama e Indicazioni e, da 1100 px, la loro vetrina vera con Galileo e Fidalma; in stagione la fascia delle Feste e subito il racconto di Natale con le due foto Nikon; manifesto di Galileo e cinque numeri su blocco scuro; chi siamo con le date, la seconda frase di Galileo e la fascia "Hanno scritto di noi"; quattro tessere del laboratorio e l'elenco dei pani; "Negozi e orari" con una scheda per negozio (stato di adesso, tabella degli orari, Chiama, Indicazioni); forniture con il modulo che chiede il tipo di richiesta; piede in quattro colonne.
- **Foto, decisione "niente"**: nessuna foto di repertorio, nessuna illustrazione. Restano solo le foto loro che reggono e nel loro formato: la vetrina 640x319 (mai ingrandita: 411 px a 1440, 349 px a 390), la striscia dell'insegna sul telefono, il panettone e la focaccia sulla juta (stessa serie Nikon, dicembre 2020, quadrati). Tolte: la focaccia scontornata dell'apertura (oggetto scontornato su fondo chiaro, bordo ricostruito a mano), le tartarughe e il pane a fette (luce mista di lampada, un'altra serie).
- **Colori dal marchio**: niente più fondo mollica. Fondo bianco del sacchetto, testo e blocco scuro nel bruno delle scritte del sacchetto (#33261F, come prima), bottoni, cifre e blocco delle forniture nel legno dell'insegna (#6F3624, campionato sulla foto della vetrina, vicino al bordeaux #733129 della scritta del sito di oggi), verde #2A6234 solo per "Aperto". Tolto il blu dei bottoni.
- **Tipografia**: le stesse due famiglie (Sentient e General Sans), con ruoli fissi e due pesi (Sentient 400; General Sans 400 e 600, il 500 tolto). Il titolo resta "Siamo Fornasiero, fornai anche nel nome", ora in maiuscolo come le lettere dell'insegna, 88 px a 1440 e 40 px a 390 (fascia della famiglia B), con "Forna/forna" nel legno. Sette misure in tutta la pagina a 1440, sei a 390.
- **Uso**: tutto quello che la versione 1 con l'uso faceva resta (stato calcolato sull'ora di Roma e sui festivi, righe di oggi, eccezioni della settimana, fascia e sezione delle Feste che salgono in stagione, Chiama in testata che passa a via Alsazia quando è aperta solo lei, dato strutturato). Il selettore a schede dei negozi è diventato due schede affiancate con la tabella degli orari.

### Esito regola per regola (dopo il ritocco finale; controlli di `_prova/script/pro_controlli.mjs` e screenshot)

1. **Telefono in testata fissa, sempre visibile**: PASSA. "Negozi e orari" prima voce; a 390, a metà pagina, il bottone della testata si vede e si tocca (48 px) e ora dice anche quale negozio chiama ("049 870 26 58 / via Vigonovese", "049 870 51 07 / via Alsazia" quando è aperta solo lei; sotto 375 px "Chiama / Vigonovese"); 15 link `tel:`.
2. **Prima schermata con mestiere, luogo, prova, azione**: PASSA a 1440x900 e 390x844 (occhiello "Panificio a Camin, Padova, dal 1963", bottoni "Chiama" con il numero di ogni negozio; a 390 il Chiama riempie la riga accanto a "Indicazioni").
3. **Immagine vera nell'apertura**: PASSA, con il limite delle foto che hanno. A 1440 la vetrina con Galileo e Fidalma ora è 520x259 (da 411x205; nativa 640x319, mai ingrandita), accanto allo stato e ai negozi, col fondo allineato ai bottoni; da 1100 a 1399 px 411 px. A 390 la striscia dell'insegna nella scheda di via Vigonovese e la vetrina intera subito dopo la fascia (a 830 px, prima a 3308).
4. **Zero repertorio**: PASSA. "indicativ" 0; nessuna immagine da banche; nessuna illustrazione.
5. **Foto in serie**: PASSA. La vetrina è stata scaldata e portata al contrasto delle foto Nikon (`pro_img.py`); tre formati (2:1, 1:1, striscia); una sola didascalia (la vetrina) su tre foto a 1440. Panettone e focaccia hanno sotto il nome del prodotto come scheda (titolo e una riga), non una didascalia.
6. **Palette dal marchio**: PASSA. Latte, bruno, legno, verde solo per "Aperto", più due grigi; niente beige.
7. **Scala corta e leggibile**: PASSA. 1440: 88, 56, 30, 24, 19, 16, 14 px; 390: 40, 32, 22, 17, 16, 14 px. Testo 19/17 px. I 14 px sono nella riga legale e, sotto 375 px, nella seconda riga del bottone della testata. Titolo 88 px maiuscolo, interlinea 1,0 (390: 40 px, 0,96).
8. **Due famiglie**: PASSA. Sentient (titoli, cifre, anni, nomi dei clienti, titoli degli articoli, stato) e General Sans (testo, etichette, bottoni, modulo).
9. **Servizi in schede con foto**: NON PASSA (limite dichiarato). Tre tessere in tre colonne (da 720 px), tutte cliccabili, con un dato grande in Sentient al posto della foto ("4" paste all'uovo, "4 + 4" pizze e focacce, "6" dolci da forno, contati dagli elenchi del loro sito), nome, elenco e link pertinente ("Si trovano al banco: orari", "La Bacheca di Romina"). Tolta la tessera "Il pane" che ripeteva la sezione sotto. Senza foto per decisione del committente: non ci sono foto vere di pasta, pizze e dolci che reggano.
10. **Almeno tre tipi di prove**: PASSA. Cinque numeri (1963, 30+, 2, 60, 400); clienti con il nome in una fascia propria ("Per decenni il pane agli operai di" Officine Meccaniche Stanga, Snia Viscosa, Sit-La Precisa, Raccanello, Mattino 2023); "Hanno scritto di noi" con i titoli veri dei tre articoli al posto delle certificazioni, che non hanno. Recensioni: nessuna leggibile nelle fonti, non inventate (LEGGIMI).
11. **Lavori con un nome**: NON SI APPLICA (bottega al banco, nessun lavoro su commessa nelle fonti). Il posto va alla storia in quattro date, ora in orizzontale con gli anni a 56 px.
12. **Ritmo a blocchi**: PASSA. Blocchi pieni oltre al piede: fascia delle Feste e forniture nel legno, numeri nel bruno, laboratorio su grigio chiaro; spazi 120/64 px; margini 79/21 px.
13. **Un solo sistema di bottoni**: PASSA. Pieno e con il bordo, raggio 4 px, 52/48 px, testo 16 px; ogni chiamata ha il numero. In prima schermata a 1440 i bottoni pieni sono tre (testata e i due negozi): quello della fascia è passato al solo bordo.
14. **Modulo e "dove e quando"**: PASSA. Modulo con il tipo di richiesta (mailto con oggetto "tipo, nome", da collegare a un servizio); per ogni negozio stato, tabella degli orari, "Chiama" e "Indicazioni", che ora apre il percorso (`maps/dir`); nessun iframe.
15. **Piede completo**: PASSA, senza certificazioni (non ne hanno). Al posto del logo a cesto in clip-art la parola FORNASIERO composta come in testata.

### Controlli generali

- Dopo il ritocco finale: screenshot rifatti (`build_finale.sh`) e guardati a pezzi a 390 e 1440 interi, prime schermate, e 320, 768, 1024, 1280, 1920; nessuna sovrapposizione (corretti durante il lavoro: la testata a 320, che con la seconda riga del bottone usciva di 41 px; le tessere orfane a 768 e 1024; lo spazio vuoto tra titolo e frase in "Chi siamo"). Nessuno scorrimento orizzontale da 320 a 2560 (`pro_uso.mjs`, 19 larghezze; `trova_largo.mjs` a 320, 340, 360, 375). `ritocco_misura2.mjs` a 390x844: stato a 273-322 px (347 la domenica e nei festivi), tel di via Vigonovese a 492-540 e di via Alsazia a 666-714 (690-738 la domenica), fascia fino a 810 (835 la domenica, 794 il 16 dicembre); fuori stagione la vetrina intera è a 734 px. `pro_uso.mjs`: stato e righe di oggi giuste a tutte le ore e i giorni provati, fascia giusta a tutte le date, con JavaScript spento stato e fascia leggibili, dall'àncora delle forniture si vedono telefono e mail con oggetto "Fornitura pane" a 390 e 1440, dall'àncora delle Feste i due tel: e la foto del panettone.

- Scorrimento orizzontale: nessuno da 320 a 2560 px (`pro_uso.mjs`, 19 larghezze; `trova_largo.mjs`). Trovati e corretti: la testata a 1024 e a 1280 (ora il menu si chiude sotto 1101 px e "panificio a Camin dal 1963" accanto al nome c'è solo da 1400 px), i bottoni dei negozi a 320 (vanno a capo).
- Sovrapposizioni: nessuna negli screenshot a 320, 390, 768, 1024, 1280, 1440, 1920. Corretti durante il lavoro: il bottone "Prepara l'email" bianco su bianco, il vuoto tra titolo e testo delle forniture, la vetrina di "Chi siamo" troppo stretta sul telefono, la fascia "Hanno scritto di noi" su tre colonne a 390.
- Prove d'uso della scheda (`pro_uso.mjs`): stato e righe di oggi giuste a 21 ore e giorni (mercoledì pomeriggio, sabato, domenica, festivi, Pasquetta, 13 giugno, Ferragosto); il 15 novembre a 390x844 nei primi 844 px ci sono la frase di stato (22 px), i due `tel:` dei negozi (48 px), il cellulare, le due Indicazioni (48 px) e la fascia delle Feste (fondo a 844); fascia a date diverse giusta (assente il 31/10, il 23/12 dalle 13, il 15/6; Pasqua 2027 dal 20/3); con JavaScript spento stato e fascia restano leggibili; dalla voce "Per bar e ristoranti" si arriva al telefono del laboratorio (e, scorrendo poco, alla mail con oggetto "Fornitura pane").
- Collegamenti: `tel:+390498702658`, `tel:+390498705107`, `tel:+393386600664`; `mailto:info@panificiogalileofornasiero.it` (anche con oggetto "Fornitura pane" e testo); due mappe con il nome del negozio e l'indirizzo; nessuna ancora rotta, nessun link a pagine locali che non esistono.
- Nessun carattere U+2014 nella pagina, in questa nota, nel LEGGIMI, nei crediti e negli script nuovi.

### Caratteri e licenze

Sentient (400) e General Sans (400, 600), Indian Type Foundry, da Fontshare, ITF Free Font License (uso commerciale gratuito), file serviti dalla pagina in `sito/fonts/`. General Sans 600 scaricato il 3/11/2026 da Fontshare (copia in `assets/fonts-scaricati/`).

### Non applicato, apposta

- Apertura a tutto schermo con una foto (famiglia B, punto 2): non c'è una foto vera del laboratorio o della bottega che regga a quella misura; la vetrina è 640x319. L'apertura si regge sul titolo in maiuscolo come l'insegna e sui dati.
- Facciata in ogni scheda negozio: c'è solo la vetrina di via Vigonovese (nell'apertura); via Alsazia non ha nessuna foto. Le schede sono senza foto per restare uguali.
- Novità di stagione con foto: la Bacheca di Romina è nel link della tessera "Dolci da forno"; le sue foto da telefono non reggono.
- Newsletter "Gli avvisi di Romina": tolta (non inviava nulla; c'è un solo modulo in pagina, quello delle richieste).
- Recensioni e certificazioni: non ce ne sono nelle fonti; da chiedere (LEGGIMI).

---

## Versione 1 con l'uso (2 novembre 2026, sera), prima del livello professionale

Quello che segue descrive la versione copiata in `_prova/versione-1-uso/`.

Pagina: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/` (WebP a più larghezze con srcset), caratteri in `sito/fonts/`. Screenshot e controlli si rifanno con `bash _prova/script/build_finale.sh` (con `--immagini` rifà anche le immagini); prove d'uso con `node _prova/script/v1uso_prova.mjs`, misure della prima schermata con `node _prova/script/v1uso_misura.mjs <larghezza> <altezza> [mobile] [ora]`. La versione 1 com'era prima di questo passaggio è in `_prova/versione-1-originale/` (sito, screenshot, script, LEGGIMI).

Screenshot, all'ora di Roma simulata lunedì 2 novembre 2026 alle 10.00 (`index.html?ora=2026-11-02T10:00`, stagione delle prenotazioni di Natale): `home-1440.jpg` (6442 px compreso il piede), `home-1440-prima-schermata.jpg`, `home-390.jpg` (8831 px), `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`. Gli screenshot interi sono fatti con la pagina in cima: la testata, che ora resta in alto, compare una volta sola.

## Ritocco con l'uso, dopo le prove dei clienti tipo (2 novembre 2026)

I tre clienti tipo della scheda (`_prova/uso/SCHEDA.md`) hanno provato questa versione accanto alla versione 2 (`_prova/uso/prova-v1-prima-0/1/2/`): voti 6,5, 5,5 e 7, un compito fallito (chi prenota le Feste non vedeva la foto della focaccia entro uno scorrimento). Ho applicato i difetti bloccanti e importanti e i minori facili restando nella versione 1: stessi caratteri (Sentient e General Sans), stessa scala, stessa griglia, mollica, carta, bruno, spiga e blu; il titolo "Siamo Fornasiero, fornai anche nel nome" con "Forna/forna" nel colore delle spighe, la focaccia scontornata nel gradino e il fondo mollica restano.

**Prima schermata, telefono 390x844**
- Titolo da 44 a 35 px (clamp 32-40 px), sempre su quattro righe, "Forna" sopra "forna", la focaccia di 112 px nel gradino a destra di "Siamo". Lo stato sale da 327 a circa 290 px.
- Stato: le parole in grassetto sono in Sentient 500; "Aperto ora", "Aperti ora tutti e due i negozi", "Aperto" nelle righe di oggi e nelle schede della chiusura sono in verde scuro #2A6234 (5,8:1 sulla mollica, 6,9:1 sulla carta, AA anche in corpo piccolo); "Ora chiusi" e "Oggi è domenica" restano nel bruno, in 500. Il verde è l'unico colore nuovo ed è solo su quelle parole.
- Scheda di via Vigonovese: sotto il nome la striscia dell'insegna di legno "FORNASIERO Galileo" (350x33, taglio 640x60 della loro foto della vetrina, alla misura nativa; l'alternativo dice "a pochi metri dal semaforo"). Solo sotto i 600 px: a 768 e oltre la vetrina intera è in "Chi siamo".
- Righe di oggi: il mercoledì via Vigonovese "Chiuso, oggi 8.30-13.45, pomeriggio chiuso", il sabato via Alsazia "Aperto, oggi 8.30-13.30, pomeriggio chiuso" (regola nello script: un solo orario che finisce entro le 14).
- Eccezioni della settimana in bruno pieno (11,7:1 invece di 5,8:1), 16 px da 601 px in su, 15 px sul telefono perché "Mercoledì pomeriggio chiuso. Sabato: chiamate." stia su una riga; il cellulare 338 660 06 64 è un bersaglio di 50 px.
- I quattro link "Mappa" e "Apri nella mappa" si aprono in una scheda nuova (`target="_blank" rel="noopener"`).
- Testata: resta in alto (`position:sticky`), alta 64 px sul telefono, 88 px da 601 a 1100, 72 px da 1101 in su; un filetto sotto quando la pagina scorre. Sul telefono "Chiama" è un bottone blu pieno di 44 px (prima una parola di 26 px) e "Menu" ha la stessa altezza; "Chiama" chiama via Alsazia quando è aperta solo lei, come prima. Ogni sezione arriva 24 px sotto la testata (`scroll-margin-top`).
- Fascia delle Feste: piena, nel bruno delle scritte (#33261F) con il testo in mollica (11,7:1), a tutta larghezza (il fondo esce dai margini con box-shadow e clip-path, senza allargare la pagina), con il bottone mollica "Chiama 049 870 26 58" e "Come si prenota", alti 48 px. Chiude l'apertura senza la striscia gialla sotto.
- Misure a 390x844: lunedì 2/11 alle 10 la fascia finisce a 813 px, domenica 15/11 (stato su tre righe) a 838; a 430x932 a 831. Tutti i tel: dei negozi (48 px), il cellulare, le due mappe (48 px) e la fascia con il suo tel: stanno nella prima schermata. A 360x780 la fascia finisce a 898: si vede scorrendo poco.

**Prima schermata, 1440x900**: stessa composizione; la testata scende a 72 px e la formula del titolo è ritoccata perché la fascia, ora più alta, chiuda la schermata a 887 px: il titolo passa da 140 a 137 px. Lo stato in verde e la fascia piena sono gli unici cambi a vista.

**Natale e Pasqua**
- In stagione (dal 1 novembre al 23 dicembre alle 13; a Pasqua dai 40 giorni prima al sabato alle 13) lo script sposta la sezione subito dopo l'apertura, prima di "Chi siamo"; fuori stagione resta dopo pasta e dolci. Con JavaScript spento resta dov'era.
- Sul telefono la foto del panettone viene subito dopo il titolo, poi il testo, i bottoni e la focaccia (`display:contents` sulla griglia e sul dittico, `order`, solo sotto i 600 px). Arrivando da "Come si prenota" si vedono titolo, panettone intero e il testo.
- La seconda foto del dittico non è più il sacco con il bordo della focaccia: è la focaccia di Natale intera sul sacco del cinquantesimo, con l'etichetta accanto (taglio quadrato della stessa foto Nikon), didascalia "Focaccia di Natale, sul sacco del cinquantesimo, 1963-2013".
- Titolo e testo cambiano con la stagione: Natale "A Natale, la ricetta di Galileo"; Pasqua "A Pasqua, colomba e focaccia"; fuori stagione "Natale e Pasqua". Dal 15 dicembre (e a Pasqua dai 7 giorni prima) il testo dice "chiamate per sapere se c'è ancora posto", come la fascia.
- Nel testo il numero non è più un link di 21 px: resta scritto, il bottone "Chiamaci e ordina" è subito sotto.

**Il pane, pasta e dolci, forniture, chiusura**
- "Il pane di oggi" diventa "Il pane di ogni giorno". Gli altri quindici pani sono un elenco in due colonne in General Sans 17 px nel bruno, con i nomi interi e, per pane al latte e pane biscotto, le varianti del sito ("pane arabo e bocconcini", "bianco, integrale, ai cereali"); sotto, "In tutto sono oltre 30 tipi: per gli altri chiedete al banco." Etichetta "E ogni giorno", come "I pani con il nome di casa".
- Pasta, pizze e dolci: tolta la fascia delle tagliatelle di repertorio; restano le tre righe nome e descrizione.
- Forniture: la riga "Per i locali, chiamate il laboratorio per sapere se arriviamo fino a voi, in che giorni e a che ora." in bruno 500, come domanda guida; "Camin e dintorni" resta scritto solo per le consegne alle famiglie, come sul sito di oggi (la zona per i locali è da chiedere, non la invento). "Vedi i pani che facciamo" su una riga a sé (44 px). A destra "Oppure scrivete a", la mail a 18 px con 6 px sopra e sotto, "oggetto: Fornitura pane" sotto.
- Chiusura: al posto dei panini Unsplash nei sacchetti, il loro pane a fette nel cesto con il sacchetto "Galileo Fornasiero srl" dietro, con la stessa correzione della luce delle tartarughe; didascalia "Pane a fette, nel cesto del banco." (corta, perché a 1024 una didascalia su due righe finiva sotto la foto).
- Menu e righe "ruolo": `word-spacing:.08em`.
- Ora in pagina non c'è nessuna foto di repertorio: tutte vengono da `assets/originali/`.

**Non applicati, apposta**: il titolo su una riga o cambiato in "Fornasiero, a Camin dal 1963", il titolo a 1440 tra virgolette come citazione e la vetrina al posto della focaccia nell'apertura (il committente ha scelto proprio titolo, focaccia e idea della versione 1; la vetrina è entrata come striscia dell'insegna nella scheda del negozio); la didascalia della focaccia sul telefono (non c'è posto senza far uscire la fascia dalla schermata; la focaccia di Natale ora è nominata nel dittico e nella fascia); "Consegniamo in zona Camin e dintorni, ai locali e anche alle famiglie" (la zona per i locali non è scritta da nessuna parte); "E altri pani secondo la giornata" (non detto da loro: al suo posto il loro "oltre 30 tipologie"); un link "Per bar, alberghi e ristoranti" sotto i negozi (c'è nella testata, che ora resta in alto); a 360x740 la fascia nella prima schermata (servirebbe togliere altro).

**Controlli del ritocco**
- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024 intere; arrivo da "Come si prenota" a 390, da "Per bar e ristoranti" e "Il pane" a 1440 (`_prova/script/ritocco_ancora.mjs`). Nessuna sovrapposizione (corretta la didascalia della chiusura a 1024), nessuno scorrimento orizzontale da 320 a 2560 (`v1uso_prova.mjs`).
- `v1uso_prova.mjs`: stato e righe di oggi a 21 ore e giorni (mercoledì pomeriggio e sabato con "pomeriggio chiuso"); Feste il 31/10, 15/11, 16/12, 23/12 alle 12 e alle 14, 15/6, 20/3, 25/3 e 27/3/2027; JavaScript spento; collegamenti (tel:, mailto: con oggetto, mappe, nessuna ancora rotta, nessuna pagina locale).
- `ritocco_misura.mjs`: ordine delle sezioni il 15/6 (apertura, storia, pane, forno, feste, forniture, negozi), il 16/12 e il 20/3/2027 (apertura, feste, storia...), con titolo e testo della sezione giusti per ciascuna data; altezze di stato, insegna, "Chiama" e "Menu" (44 px) a 390.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- PNG temporanei cancellati.

## Versione 1 con l'uso: cosa è cambiato

Il committente, viste le due versioni, ha scelto questa (la 1): grafica, caratteri, colori, impaginazione, la focaccia, il titolo "Siamo Fornasiero, fornai anche nel nome" e l'idea del gradino restano. Dalla versione 2 (`sito-v2/`) ho ripreso solo quello che i clienti tipo dovevano trovare e dove (scheda `_prova/uso/SCHEDA.md`), ridisegnato con i caratteri, la scala, i colori e la griglia di questa pagina. Niente caratteri nuovi, niente icone; niente colori nuovi in quel passaggio (il verde di "Aperto" arriva con il ritocco sopra).

**Prima schermata, telefono 390x844 (il cliente di Camin, il primo visitatore della scheda)**
- La focaccia resta, ma passa nel gradino che sul telefono il titolo lascia libero: a destra di "Siamo", alta come le prime due righe (97 px a 390, tra 70 e 112 px da 320 a 430, mai a meno di 12 px dalle lettere). Il titolo resta su quattro righe con "Forna" e "forna" uno sopra l'altro, a 44 px invece di 52, così tutto quello che serve sta nei primi 844 px.
- Sotto il titolo, come prima, una riga su chi siamo, accorciata: "Pane, pasta fresca, pizze, focacce e dolci dal nostro laboratorio, a Camin dal 1963."
- La riga di stato non è più piccola e in fondo: è in Sentient a 21 px (28 px a 1440), il testo più grande dopo il titolo, calcolata sull'ora di Roma e sui festivi ("Aperti ora tutti e due i negozi, fino alle 13.45.", "Aperto ora in via Alsazia 3, chiude alle 19.30.", "Oggi è festa: chiamate prima di passare. Domani apriamo alle 8.30.").
- I due negozi, uno sotto l'altro, separati dallo stesso filetto delle schede della chiusura: nome in Sentient, "oggi" con l'orario del giorno ("Aperto, oggi 8.30-13.45 e 16.30-20.00"), l'eccezione della settimana sempre in vista (via Vigonovese "Mercoledì pomeriggio chiuso. Sabato: chiamate."; via Alsazia "Sabato 8.30-13.30. Cellulare 338 660 06 64"), il bottone blu "Chiama" con il numero di quel negozio (48 px) e "Mappa" con il filetto bruno, come il bottone "Menu" della testata (48 px). Il bottone blu che c'era prima è diventato il "Chiama" di via Vigonovese.
- In stagione (dal 1 novembre al 23 dicembre alle 13; a Pasqua dai 40 giorni prima al sabato alle 13) l'apertura chiude con una riga a tutta larghezza sotto un filetto: "Panettone e focaccia di Natale: si prenotano in negozio o al telefono." e "Come si prenota", che porta alla sezione di Natale. Dal 15 dicembre: "chiamate per sapere se c'è ancora posto." Fuori stagione la riga non c'è; con JavaScript spento dice "Natale e Pasqua: panettone, colomba e focacce si prenotano in negozio o al telefono."
- Misure a 390x844 (lunedì 10.00): stato finisce a 378 px, i due tel: dei negozi a 48 px, le due mappe a 48 px, la riga delle Feste finisce a 790 px. Domenica 15 novembre (stato su tre righe) finisce a 816.
- "Chiama" in testata: chiama via Vigonovese, o via Alsazia quando è aperta solo lei (mercoledì pomeriggio, sabato mattina).

**Prima schermata, 1440x900**
- Stessa composizione: titolo su tutta la larghezza, la focaccia nel gradino sotto "Siamo", tutto il resto che pende dalla F di "Fornasiero". Il titolo scende da 145 a 140 px (si ridimensiona con l'altezza dello schermo, non sotto 104 px), la focaccia da 403 a 388 px.
- Sotto il titolo: la riga su chi siamo su una riga sola, lo stato in Sentient a 28 px, i due negozi affiancati su due colonne con filetto, "oggi", eccezione, "Chiama" (54 px, come il bottone di prima) e "Mappa"; la riga delle Feste chiude la schermata a 870 px su 900.
- In testata la voce "Per bar e ristoranti" (porta alla sezione nuova delle forniture); "I negozi e gli orari" diventa "Negozi e orari" per far stare la voce. Sotto 1300 px sparisce "panificio dal 1963" accanto al nome, sotto 1100 px il numero in testata (resta nei bottoni dell'apertura), sotto 900 px il menu del telefono come prima.
- 768 e 1024: anche qui la focaccia sta nel gradino sotto "Siamo" (prima a 768 stava sopra il titolo, a 368 px); i negozi su due colonne sotto, a tutta larghezza; sotto 720 px uno sotto l'altro.

**Gli altri compiti, a un tocco dalla prima schermata**
- Natale e Pasqua ("Come si prenota" nella riga delle Feste, "Natale e Pasqua" in testata): alla sezione che c'era ho aggiunto "Pezzature, prezzi e ultimo giorno utile: chiedete al banco o al telefono." e i due numeri, "Chiamaci e ordina: 049 870 26 58" (bottone blu, sono le loro parole della Bacheca) e "Via Alsazia 3: 049 870 51 07". Arrivando dal link, a 390 e a 1440 si vedono i due tel: e la foto vera del panettone. La sezione resta dov'era (dopo pasta e dolci): in stagione ci si arriva dalla riga dell'apertura.
- Forniture e consegne, sezione nuova prima della chiusura, nello stile delle altre (titolo in Sentient come "Pasta fresca, pizze e dolci", testo in General Sans grigio, a destra il telefono grande come nella chiusura): "Per bar, alberghi, ristoranti e rivendite", la loro frase sulla fornitura, gli operai della Stanga e della Snia Viscosa (Galileo e Fidalma al Mattino di Padova, 30/03/2023, copia in `_prova/crawl/stampa/camin_pane_mattino_panificio_fornasiero-.html`), le consegne a domicilio in zona Camin e dintorni, "Chiamate il laboratorio per sapere se arriviamo fino a voi, in che giorni e a che ora", il link all'elenco dei pani, il telefono del laboratorio e la mail scritta in chiaro con oggetto "Fornitura pane" e la traccia (locale, indirizzo, pani e quantità, giorni, telefono). La riga sulle forniture che stava sotto le schede dei negozi è tolta (portava a una pagina che non c'è).
- Negozi e orari (testata e piede): le schede della chiusura restano com'erano, con lo stato calcolato con lo stesso orologio dell'apertura (festivi compresi) e una riga in più per ciascuno: via Vigonovese "Sabato e domenica: chiedete al telefono", via Alsazia "Domenica: chiedete al telefono".
- Mappe: tutte e quattro con il nome del negozio (`query=Panificio Fornasiero Via Vigonovese 116 35127 Padova` e `...Via Alsazia 3 Camin 35127 Padova`).

**Invisibili**
- Lo script dello stato è quello della versione 2, adattato: ora di Roma, festivi nazionali, Pasqua e Pasquetta calcolate, 13 giugno, un elenco `FERIE` da riempire, le date delle prenotazioni in tre variabili in cima (`NATALE_DA`, `FINE_PRENOTAZIONI`, `SPEGNI`), "Sotto Natale gli orari possono cambiare" dal 20 dicembre; nei giorni non scritti (sabato di via Vigonovese, domenica) la pagina non dice né aperto né chiuso. Si aggiorna ogni minuto; per le prove `?ora=`.
- Dato strutturato (schema.org Bakery) con i due negozi, CAP 35127 e orari.
- Nessun link a pagine locali che non esistono: "La storia dal 1963" porta a Chi siamo, "Per bar, alberghi e ristoranti" e "Consegne a domicilio" alla sezione nuova, La Bacheca di Romina, Privacy e Cookie alle pagine del sito di oggi.
- Le foto di repertorio restano due, tutte e due con "Foto indicativa" in didascalia: le tagliatelle (come prima) e i panini nei sacchetti della chiusura (prima senza didascalia, ora "Pane nei sacchetti di carta. Foto indicativa."). La versione 2 non ha foto vere per la pasta e per la chiusura (la vetrina, l'unica che servirebbe lì, è 640x319 e sta già in Chi siamo): non c'era niente di loro da mettere al posto.

**Cosa non ho toccato, apposta**: il titolo, la focaccia scontornata e la sua didascalia, il fondo mollica, Chi siamo, il pane, pasta e dolci, il dittico di Natale, la frase di Galileo nella chiusura, il piede (anche il modulo degli avvisi di Romina, vedi LEGGIMI).

## Controlli (versione 1 con l'uso)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024 intere, 1280x720 e 1920 in alto; nessuna sovrapposizione, nessuno scorrimento orizzontale. A 1280x720 i negozi stanno nella piega, la riga delle Feste finisce a 746 px.
- `v1uso_prova.mjs`: stato a 21 ore e giorni (lunedì 10.00, 13.40, 14.15, 19.45, 21.00; mercoledì 10.00, 14.30, 17.00; venerdì 20.30; sabato 7.30, 10.00, 14.00; domenica; 8/12, 7/12 sera, 25/12, 31/12 sera, 1/1, Pasquetta 2027, 13/6, 15/8): nei festivi nessun "Aperto". Prima schermata a 390x844 e 430x932: due tel: dei negozi e il cellulare, due mappe, le due eccezioni e la riga delle Feste dentro la schermata. Feste il 31/10, 15/11, 16/12, 23/12 alle 12 e alle 14, 15/6, 20/3 e 25/3/2027, 27/3/2027 alle 14; JavaScript spento. Arrivo da #feste, #forniture, #negozi, #pane a 390 e a 1440.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 601, 640, 720, 721, 768, 900, 901, 1024, 1100, 1101, 1280, 1440, 1680, 1920, 2560 (a 901-1100 e a 1101 la voce nuova del menu faceva scorrere: corretto).
- Collegamenti: tel:+390498702658, tel:+390498705107, tel:+393386600664, mailto:info@panificiogalileofornasiero.it (semplice e con oggetto "Fornitura pane"), quattro link mappa ai due negozi, nessuna ancora rotta, nessuna pagina locale.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- PNG temporanei cancellati.

Quello che segue è la nota della versione 1 com'era prima di questo passaggio; dove è cambiato vale quanto scritto sopra.

## Idea

La frase di Galileo al Mattino di Padova, "Siamo Fornasiero, fornai anche nel nome", è l'impaginazione: la seconda e la terza riga del titolo partono esattamente sotto la F di "Fornasiero", così "Forna" e "forna" stanno una sopra l'altra, nel colore delle spighe. Nel gradino che resta libero sotto "Siamo" c'è la loro focaccia veneta, intera, vista dall'alto. Titolo e oggetto si incastrano: con il nome di un altro forno la pagina non sta in piedi.

## Cosa è cambiato in questo passaggio

Prima schermata (bloccante e importanti del giudice, più la richiesta del committente del 2 novembre):
- Via il panino di repertorio su lino grigio, la foto a tutta larghezza con la sfumatura e "Foto indicativa". L'oggetto ora è un prodotto loro: la focaccia veneta con la glassa di zucchero e le mandorle (foto Nikon del panificio, dicembre 2020), scontornata intera con GrabCut (`_prova/script/scontorna_focaccia.py`; dove la focaccia appoggia sull'etichetta del sacco il bordo è letto a mano sul file originale), con un'ombra morbida a destra e in basso come la luce di finestra della foto. A 1440 è larga 403 px e alta 412 (il 46 % dello schermo); nessun bordo tocca la testata o i lati: la cupola sta 256 px sotto la testata, sotto la prima riga del titolo, il bordo sinistro è sul margine di pagina (72 px) e tra il bordo destro e la colonna del testo restano 43 px.
- Nessuna sfumatura linear-gradient sulle foto, in nessun punto della pagina.
- Il fondo dell'apertura e del piede non è più la carta: è la mollica (#F4E6B5), il giallo di uova e burro dentro la focaccia e il panettone. La ragione si vede: la fetta del panettone nel dittico di Natale e le tagliatelle all'uovo hanno lo stesso giallo. Il resto della pagina resta la carta bianca del sacchetto della bottega (#FAF9F6), che si vede dietro le tartarughe. Niente beige di comodo.
- La scelta di impaginazione nuova per la campagna: l'oggetto sta dentro il gradino del titolo, non a destra e non sopra; il titolo è a 145 px su tre righe e occupa tutta la larghezza utile (1296 px a 1440). Nessuna delle copertine di `_invio/zona/home/` e delle home amate ha un titolo a gradino con l'oggetto nel gradino, né un fondo giallo preso dal prodotto. Niente legende numerate, pallini o filetti sull'oggetto: solo una didascalia sotto ("La focaccia delle Feste, con la glassa e le mandorle.").
- La riga di stato di riserva ora dice "Dal lunedì al venerdì dalle 8.30. Il sabato mattina via Alsazia 3 è aperta.", senza far credere che via Vigonovese il sabato sia chiusa. Il link agli orari va a capo pulito sotto.
- A 1280x720 tutta l'apertura sta nella piega (bottone e stato finiscono a 668 px); a 1920 l'apertura è centrata in altezza e non supera 860 px; a 390 la focaccia sta sopra, centrata, e il titolo su quattro righe con "Fornasiero" e "fornai" allineati; tutto il blocco, bottone e stato compresi, sta nei primi 844 px.

Parte centrale:
- Chi siamo: la frase è "Galileo Fornasiero è arrivato a Camin il primo aprile del 1963. Fidalma è al banco da sessant'anni." (Filippo, Romina e Michele Daniele tolti finché il panificio non dà il permesso). Le date stanno a destra della vetrina, allineate in alto alla foto.
- Il pane di oggi: le tartarughe sono ridotte a 6 colonne (636x707 a 1440), tagliate da x 320 (fuori il pangrattato a sinistra e la sessola di plastica a destra), con la scritta "Fornasiero srl Camin-Padova" in alto; la dominante gialla della lampada è corretta verso il bianco delle foto di Natale; la didascalia è sotto la foto. A sinistra, nella stessa altezza: titolo, i cinque pani con il nome di casa uno per riga in Sentient a 56 px, come sulla lavagna del banco, e in fondo gli altri quindici pani. Nessuna colonna vuota.
- Pasta, pizze e dolci: le forniture sono uscite dalla sezione (ora il titolo dice il vero) e stanno in una riga sotto le schede dei negozi, con il link a `fornitura.html`. Restano tre voci, in tre righe nome e descrizione, sotto una fascia a tutta larghezza di tagliatelle all'uovo (segnaposto con "Foto indicativa" in didascalia).
- Natale: il dittico è panettone e sacco del cinquantesimo (l'etichetta 1963-2013 con il bordo della focaccia), per non ripetere la focaccia intera dell'apertura. Le due didascalie hanno lo stesso rientro (var(--m) dal bordo della propria foto).
- Chiusura: la foto di repertorio fredda con i quadretti blu è sostituita da panini nei sacchetti di carta, luce calda; la foto è alta esattamente quanto la colonna del testo (posizione assoluta dentro la cella), e la colonna distribuisce frase, schede e riga delle forniture dall'alto in basso. A 1440 testo e foto finiscono alla stessa riga. I due pannelli delle schede occupano la stessa cella: cambiando negozio la pagina non salta.
- Piede: logo a 120 px (PNG a 2x e 3x), la scritta sotto il cesto si legge; tra la fascia alta e il filetto delle colonne 44 px; a 390 ogni link delle colonne è alto 40 px (padding 9 px sopra e sotto).

## Caratteri e colori

- Titoli, nomi dei pani, telefoni: Sentient 400/500. Testo: General Sans 400/500. Tutti e due di Indian Type Foundry, da Fontshare, licenza ITF Free Font License (uso commerciale gratuito), file serviti dalla pagina in `sito/fonts/`. Una serif dritta e piena, senza corsivi, che regge il titolo a 145 px come una scritta da bottega; il riferimento per la coppia serif grande e bastone piccolo è il piede di Poilâne. Cifre tabellari per orari e telefoni.
- Colori: mollica #F4E6B5 (apertura e piede), carta #FAF9F6, inchiostro bruno #33261F (13,9:1 sulla carta, 11,7:1 sulla mollica), testo secondario #645349 (6,9:1 e 5,8:1), spiga #9A5320 per "Forna/forna" e le date (5,5:1 e 4,6:1), blu #2E4D7B per bottone, campo del modulo e fuoco (8,1:1 e 6,8:1; bianco sul blu 8,5:1). Tutti AA.

## Interazione

Un solo gesto: le schede dei due negozi nella chiusura. Veri bottoni con ruolo tab, frecce, Home e Fine da tastiera, cambio netto senza dissolvenze; per ognuno lo stato di adesso calcolato sull'ora di Roma, il telefono grande con tel:, gli orari, mailto: e "Apri nella mappa". Se all'apertura è aperto solo via Alsazia, la scheda mostra quello. Transizioni solo di colore su link, schede e bottoni; niente comparse allo scorrere, niente effetti al cursore.

## Foto, origine e licenza

- Apertura: la focaccia veneta, foto del panificio (`b56ebf_fabc...`, Nikon D3300, dicembre 2020), scontornata.
- Chi siamo: la vetrina con Galileo e Fidalma, loro, 640x319 alla misura nativa.
- Il pane di oggi: tartarughe della galleria del sito del panificio, loro.
- Pasta fresca: Karen Sewell, https://unsplash.com/photos/T6vI65xwoNA, Licenza Unsplash. SEGNAPOSTO, con "Foto indicativa" in didascalia.
- Natale: panettone sul sacco di juta e l'etichetta del cinquantesimo, foto loro.
- Chiusura: Victoria Nazaruk, https://unsplash.com/photos/ytxRXkY8QE4, Licenza Unsplash. SEGNAPOSTO, ora con "Foto indicativa" in didascalia. Non usata in altre home della campagna (controllati tutti i `*-Sito/assets/CREDITI.md` il 2/11/2026); idem Sewell.
- Logo nel piede: il PNG del sito a una tinta, nel bruno del sacchetto; non ricostruito in SVG perché il disegno ha ombre e sfumature.
- Nessuna immagine generata dall'IA. Trattamento comune con PIL in `_prova/script/finale_img.py`.

## Piede

Logo e una riga su chi sono; newsletter "Gli avvisi di Romina" (prenotazioni delle Feste e dolci nuovi: ha senso, hanno clienti privati e notizie che tornano ogni anno), con campo, bottone e consenso, che non invia nulla finché non si collega a un servizio; quattro colonne (Il panificio, Prodotti, I negozi, Seguici con il solo Instagram, l'unico social collegato dal loro sito); riga legale con ragione sociale, indirizzo e P.IVA, Privacy e Cookie. Il REA non c'è finché non arriva una visura. A 390 le colonne si impilano nell'ordine Il panificio, Prodotti, I negozi, Seguici.

## Controlli (2 novembre 2026)

- Screenshot guardati a pezzi: 1440 intera e prima schermata, 390 intera e prima schermata, 320, 768, 1024, 1280x720, 1920.
- scrollWidth uguale a innerWidth a 320, 360, 390, 430, 600, 601, 768, 900, 901, 1024, 1100, 1101, 1280, 1440, 1680, 1920 e 2560 (`_prova/script/controlli.mjs`).
- Altezza a 1440: 6255 px compreso il piede.
- Gesto (`_prova/script/prova_gesto.mjs`, orologio finto, ora di Roma): lunedì 10.00 e 14.30, mercoledì 10.00 e 17.00 (si apre su via Alsazia), venerdì 21.00, sabato 10.00 (via Alsazia aperta, via Vigonovese "meglio chiamare") e 15.00, domenica 10.00; frecce, Home e Fine da tastiera; tocco a 390; menu del telefono.
- Collegamenti: tel:+390498702658, tel:+390498705107, tel:+393386600664, mailto:info@panificiogalileofornasiero.it, due link alla mappa (via Vigonovese 116 e via Alsazia 3), nessuna ancora rotta.
- Segnali da IA (`_metodo/kit/segnali.sh`): 0 soglie bloccanti su 10, 0 da guardare su 8; foto al 38,4 % della pagina, 3 misure di H2, un solo titolo col punto (la citazione di Galileo), 4 filetti larghi, nessun mono, nessun badge, nessuna freccia, nessuna numerazione.
- Nessun carattere U+2014 in pagina, in questa nota, nel LEGGIMI, nei crediti e negli script.
- Divieti del committente: nessun gradiente, nessun titolo in gradiente, niente Inter, niente icone, niente card, niente vetro, niente corsivo serif d'accento, niente legende numerate.
- PNG temporanei cancellati (anche quelli grandi in `_prova/cieco/`).
