# Mario Agnoletto, proposta di home

È una proposta non richiesta e comprende solo la home. Non è stata pubblicata e l'azienda non è stata contattata.

## Cosa c'è

- `sito/index.html`: la home finale "Tavola dei campioni" (prototipo B, scelto dal committente), in HTML statico: si apre con un doppio clic.
  - Immagini in `sito/img/` (WebP in più larghezze, logo e timbro in SVG).
  - Carattere in `sito/fonts/`: Host Grotesk, SIL Open Font License 1.1. La pagina non chiede nulla a Google né ad altri domini.
- `screenshot/home/`: home a 1440 e a 390, intere e prima schermata, più le prime schermate a 320, 768, 1024 e 1920, il filtro e il menu. `NOTA.md` spiega idea, caratteri, colori, interazione, foto, controlli e cosa è cambiato nell'ultimo giro.
- `01-analisi.md`: analisi del sito attuale, fatti con le fonti, riferimenti.
- `assets/CREDITI.md`: origine e licenza di ogni foto.
- `_prova/`: prototipi A e B, script, riferimenti.
  - La home si rifà con `bash _prova/script/build_finale.sh` (scontorni se mancano, immagini, logo, pagina, controlli, segnali, screenshot).
  - Prove a parte: `finale_filtro.mjs` (filtro e menu con tastiera, dito e indirizzo), `finale_nitidezza.mjs` (file scelto e risoluzione per ogni foto), `finale_misure.mjs` (posizioni degli elementi).
  - Gli script della vecchia versione A che il build non usa più sono `finale_logo.py` e `finale_verifica.mjs`.
  - Il modello di segmentazione usato per gli scontorni (BiRefNet lite, licenza MIT, 224 MB) è in `_prova/crawl/modelli/`. Serve solo per rifare le maschere (`_prova/finale/tacco-alfa.png` e `_prova/finale/alfa/`) e si può cancellare se manca spazio.

La versione A, "Dritto e rovescio", è stata sostituita. Da A sono rimaste solo correzioni di testo già verificate: "cristalli e pietre" al posto del marchio nella bigiotteria, e i recapiti, che erano già uguali.

## Foto: vincolo Hambro

Le foto di fibbie dorate di Ruan Richard Rodrigues su Unsplash (aNe3TXdpHMg, FXVC26csSz4, hqGQcZnEvy0, 2hWmYcG26E8 e tutte quelle della stessa serie) sono riservate alla home di Hambro.
- **Nessuna è in questa home**, e nessuna va usata in altre pagine di Mario Agnoletto.
- `_prova/script/finale_img.py` si ferma se ne trova una.
- L'apertura, che nel prototipo B era una di quelle fibbie, ora è un tacco gioiello dell'azienda (foto 12 del loro sito).

## Ultimo giro (dopo il giudizio cieco)

La prima schermata resta quella approvata. Cambiano esecuzione, foto e dati, i dettagli sono nella NOTA:
- il timbro è battuto sulla punta del pezzo e la legenda porta il numero di catalogo 01 al posto di "Tav. 1". Le sezioni sono A, B, C, D;
- tutti i campioni sono scontornati e posati sullo stesso cartone. La casella "Vetrina" delle targhe è tolta e le targhe stanno nel testo;
- le foto di repertorio sono scese da tre a una (la fresa): al loro posto ci sono le foto 13 e 2 dell'azienda;
- nella sezione C c'è il dritto e rovescio del monogramma;
- filtro compatto, indirizzo aggiornato, menu che si chiude, link morti tolti, prima schermata a 768 con il bottone visibile.

## Da confermare con l'azienda

### Dati
- **1979.** Lo dice il sito ("Fondata nel 1979 da Mario Agnoletto"). Atoka dà 37 anni di anzianità, cioè circa il 1989, forse la data d'iscrizione dell'impresa individuale di oggi.
  - In pagina compare in piccolo in due punti: nell'apertura ("dal 1979") e nel piede. L'etichetta "Dal 1979" nei recapiti è diventata "Ditta".
  - Va confermato dal titolare: annotare qui chi l'ha confermato e quando. Se non si conferma, si toglie da quei tre punti.
- **Il pezzo d'apertura.** È letto dalla foto 12: un tacco gioiello a lamelle che sembra ottone grezzo, con anello, quattro lamelle, asole d'innesto e stelo.
  - Va confermato che sia un loro lavoro, che sia ottone e i nomi delle parti che usano in officina (per esempio "fusto" o "gambo" al posto di "stelo"). I richiami oggi sono Anello, Lamelle, Asola e Stelo: sono parole che descrivono la forma, non termini dell'officina.
- **Zama.** Il sito la nomina solo in generale. Il filtro la assegna agli accessori (fibbie, morsetti, talloni) per deduzione.
  - Chiedere quali pezzi fanno in zama.
  - Chiedere anche quali metalli usa la bigiotteria: oggi non entra in nessun filtro, e lo stesso vale per la stampa su pelle.
- **Metalli per lavorazione** (sono quelli del filtro, presi dalle schede del sito):
  - punzoni: acciaio e ottone;
  - fustelle: ottone, alluminio, acciaio;
  - tacchi: ottone, acciaio, alluminio;
  - ruote: acciaio;
  - targhe: alluminio, ottone e plexiglas (il plexiglas dalla pagina inglese). Le targhe non hanno una foto, quindi non sono in tavola e il filtro non le conta: compaiono solo nel testo del campionario;
  - accessori: tutti e quattro.
- **Materiale dei punzoni.** La scritta che ruota sul sito dice "bronzo", la scheda dice "acciaio e ottone". In pagina c'è acciaio e ottone.
- **Punzoni in 24 ore.** Dal sito ("consegna anche in 24 h"). Va confermato che valga ancora e per quali lavori: è il titolo della sezione C.
- **Clienti.** "Lavoriamo soprattutto per calzaturifici e pelletterie", e negozi e vetrinisti per le targhe: è dedotto dal sito.
  - Da confermare, insieme al permesso di nominare dei marchi.
  - "Riviera del Brenta" nel titolo dei contatti è solo geografia: va bene se piace all'azienda.
- **Dipendenti (8 secondo Atoka), macchine, metri quadri, certificazioni, finiture interne o esterne.** Non sono in pagina. Se confermati, sono la prova da aggiungere, per esempio una riga con le macchine dell'officina e i loro nomi.
- **Persone.** Chi guida oggi l'azienda e se si può mostrare in foto.
- **Foto 15.** Resta solo nel campione 07 "Stampa e foratura": va confermato che la pelle argento goffrata e il cuoio stampato a grappolo siano lavori del loro servizio.
- **Foto 2 (sezione C).** La didascalia dice "Ottone inciso dell'officina: un cliché a foglie, due bordi a spina, un blocchetto forato, sopra una lastra traforata". I nomi sono letti dalla foto: vanno confermati, insieme al fatto che siano pezzi loro e a cosa serve il blocchetto (stampo per la foratura?).
- **Foto 13 (sezione B, Serie).** Una fibbia a catena cromata e una placca in ottone con l'inserto martellato: va confermato che siano loro pezzi di serie.
- **Gabbia del campione 01.** È descritta come "acciaio lucido", come nell'inventario: da confermare il metallo e la finitura (potrebbe essere ottone cromato).
- **Timbro sul pezzo e dritto e rovescio.** Il monogramma MA è appoggiato sulla punta del tacco e, nella sezione C, è mostrato a specchio ("Sul punzone, a rovescio") e dritto ("Sulla pelle, dritto"). È un'illustrazione di come lavora un punzone, non la foto di un loro punzone: va approvato l'uso del marchio.
- **Cliché col cavallo e il guidatore** (foto 1, campione 02). Può essere il disegno di un cliente: chiedere se si può mostrare.
- **Marchi di clienti fuori dalla pagina.** Restano fuori finché non c'è il permesso:
  - il quadrotto d'acciaio col monogramma a rovescio (foto 1);
  - la fibbia cromata con la scritta "SHY" (foto 13);
  - il cliché col marchio di una maison (foto 6).
- **"Cristalli e pietre".** Il sito scrive "swarovsky": in pagina non c'è nessun marchio, va citato solo con permesso.
- **Privacy, Cookie, English.** Tolti dal piede finché non ci sono le pagine: prima della pubblicazione vanno rimessi con i testi veri (informativa privacy, cookie) e l'indirizzo della versione inglese.
- **Modulo contatti.** La home non ne ha: ci sono telefono, email, PEC, fax e indirizzo. Il modulo del sito di oggi non è stato provato.

### Righe da approvare
- "Seguiamo il pezzo dal progetto alla serie, in zama, ottone, alluminio e acciaio." (dal testo "Azienda").
- "Otto lavorazioni, quattro metalli", "Due famiglie di pezzi: gli attrezzi per chi lavora la pelle e i pezzi che finiscono sulla scarpa, sulla borsa, in vetrina." e "In tavola ce ne sono sette; l'ottava sono le targhe da esposizione, in alluminio, ottone e plexiglas."
- "Punzoni anche in 24 ore" e "La grafica la sviluppiamo noi." (dalla scheda dei punzoni: "Sviluppo grafica e consegna anche in 24 h").
- "Tacco gioiello a lamelle in ottone, visto dall'alto" (legenda dell'apertura, numero 01) e i nomi delle parti: Anello, Lamelle, Asola, Stelo.
- Le righe dei campioni: "A gabbia, a lamelle o a stelo, su disegno." (01, letta dalla foto 12, che mostra i tre tipi) e "Ruote in acciaio e rulli." (04).
- "Serie: pezzi finiti, con qualsiasi finitura o verniciatura." (dalla scheda Accessori del sito).
- La didascalia della fresa ("Il primo pezzo, prima della serie. Foto di repertorio.") e la riga nel piede ("La foto della fresa (B, Prototipo) è di repertorio (Unsplash); le altre sono pezzi dell'officina."). Si tolgono quando la foto sarà rifatta.

## Foto da rifare dal vero

Le foto dei pezzi in pagina sono loro, ma scattate col telefono: luce piatta, riflessi bruciati, fondi diversi. Sono state ritagliate, scontornate sullo stesso cartone e corrette, e vanno usate col loro permesso. La loro risoluzione vera è il limite della pagina: su uno schermo ad alta densità il tacco d'apertura (744 px), la gabbia (660), le finiture (670) e la stampa su pelle (960) restano sotto il doppio della misura a schermo. Resta una sola foto di repertorio, la fresa (Unsplash, licenza libera, vedi `assets/CREDITI.md`): è un **segnaposto**, non mostra un pezzo di Agnoletto, e la didascalia e il piede lo dicono.

Serve una giornata: mezza di still life e mezza in officina.
- Fondo unico per lo still life: cartone grigio caldo opaco, il più vicino possibile a #E7E4DD, lo stesso colore della pagina.
- Luce di finestra o un softbox grande da un lato, con un pannello bianco dall'altro: ombre corte e morbide.
- Macchina sul cavalletto, obiettivo macro, file da almeno 4000 px di lato.

1. **Apertura, la foto più importante.** Un loro pezzo intero e intatto, dall'alto, esattamente in pianta: un tacco gioiello oppure una fibbia loro smontata nelle sue parti.
   - Tutto il pezzo nell'inquadratura, con 15-20 cm di cartone libero intorno, così in pagina si può tagliare dove si vuole.
   - Ottone lucidato o con la finitura di serie, non grezzo.
   - Una riga millimetrata d'acciaio di lato, da togliere o tenere in pagina.
   - Almeno 5000 px sul lato lungo: oggi lo stelo esce dalla foto e il pezzo è largo 1000 px.
2. **Campioni.** Uno per lavorazione, stessa luce, stesso fondo, stessa distanza, quadrati: tacco, punzone con la testa verso l'alto, fustella col filo affilato, ruota, fibbia, bigiotteria, targa (oggi la targa non ha foto e quindi non è in tavola: con la foto torna l'ottavo campione), campione di stampa su pelle. Pezzi interi, non tagliati dal bordo, così lo scontorno non serve più.
3. **Prototipo e serie.** In officina:
   - la fresa o il pantografo sul primo pezzo, con i trucioli d'ottone;
   - poi cinquanta pezzi uguali della stessa serie in un vassoio, dall'alto.
4. **Punzoni.** Un alfabeto completo di punzoni nel suo astuccio, con le teste dall'alto e le lettere a rovescio leggibili. Poi la stessa scritta stampata a caldo su pelle: la coppia vera sostituisce l'illustrazione col monogramma nella sezione C, e la foto 2 a tutta larghezza può restare o passare in un'altra sezione.
5. **Officina e mani.** Due o tre scatti di reportage con luce di finestra: le mani che incidono, la macchina con il suo nome.

## Loghi e marchi

- Il logo esiste solo in PNG 500x100. Per la home l'ho ricalcato in SVG (`sito/img/logo.svg`, `timbro.svg`, script `_prova/script/proto_b_logo.py`). Il ricalco va approvato; meglio ancora avere il file vettoriale originale.
- Il timbro rosso è il monogramma MA del logo, usato come marchio di controllo: va approvato anche questo uso.
- In pagina non c'è nessun marchio di clienti o fornitori.

## Licenze

- **Foto Unsplash**: Unsplash License, uso commerciale libero e senza attribuzione obbligatoria. Le pagine delle foto sono state verificate il 19/10/2026; elenco in `assets/CREDITI.md`.
- **Carattere**: Host Grotesk (Element Type), SIL Open Font License 1.1, da Google Fonts. Si può ospitare e incorporare nel sito.
- **Scontorno**: BiRefNet lite, licenza MIT. Il modello produce solo la maschera, non pixel nuovi.
- **Foto e logo di Mario Agnoletto**: presi dal sito di oggi, da usare con il loro permesso.

## Segnali da IA

`segnali.sh` esce con 0 soglie bloccanti. Restano tre righe da guardare, tutte volute:
- gli H2 hanno due misure (66 e 48 px);
- la numerazione 01-07 è il numero di catalogo dei campioni;
- i 5 gradienti sono i campioni di colore dei metalli nel filtro.
