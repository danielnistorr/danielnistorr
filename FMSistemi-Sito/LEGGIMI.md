# F.M. Sistemi: proposta di nuova home

Proposta non richiesta, solo la home. Versione finale in `sito/` (`index.html`, `img/`, `fonts/`), nota di progetto in `screenshot/home/NOTA.md`, screenshot in `screenshot/home/`. Si rifà tutto con `bash _prova/script/build_finale.sh`. Analisi e fonti in `01-analisi.md`; prototipi in `_prova/home/a` e `_prova/home/b`.

## Dati da confermare con l'azienda (sono in pagina)

- 17 persone in organico nel 2025 (aziende.it).
- Partner Viessmann per pompe di calore e sistemi ibridi, e le altre specialità (climatizzatori, trattamento aria e acqua, fotovoltaico residenziale, mobilità elettrica, impianti commerciali): pagina partner Viessmann.
- Orari dal lunedì al sabato 8.30-19.00, domenica chiuso (pagina Viessmann).
- "Privati, aziende ed enti pubblici": dedotto da fotovoltaico residenziale, impianti commerciali e dall'appalto pubblico del settembre 2024 (aziende.it, CIG B2F30D7E49), non scritto dall'azienda. L'appalto non è più in pagina: meglio un lavoro con nome, città e anno.
- "Un numero solo", "8 mestieri, con un solo numero da chiamare" e "il cantiere ha un numero solo": dedotti dal loro "Dalla A alla Z" e dall'unico telefono del sito.
- "Una casa dalla A alla Z" mette i mestieri nell'ordine tipico di un cantiere (muri, tubi, quadro, acqua, pompa di calore, clima, fotovoltaico, ricarica): è un ordine di buon senso, non il loro metodo dichiarato; le righe dicono cosa si fa, non come lo fanno loro.
- commerciale@fmsistemisrl.it "per preventivi e sopralluoghi" e il link "o scrivete" con oggetto "Richiesta di sopralluogo": chiedere quale indirizzo vogliono per i preventivi e se il sopralluogo è un servizio che offrono così.
- Il collegamento alla pagina di partner Viessmann (https://fm-sistemi-srl.partner-viessmann.it/): chiedere se va bene mostrarlo.
- "Pompe di calore Viessmann" nella riga d'apertura: sono partner Viessmann, ma va chiesto se installano anche altri marchi.
- Le otto lettere accese (A acqua, C clima, E elettrico, F fotovoltaico, M mobilità, P pompe di calore, R ristrutturazioni, T termoidraulica). Chiedere se fanno ancora sicurezza e allarmi (S, nelle meta keywords del sito) e se vogliono I per gli impianti commerciali.
- "Zona artigianale" accanto all'indirizzo (pagina Viessmann: "Via del Lavoro - z.a. 37").

## Non usati perché senza fonte primaria

Anno di fondazione (2004) e REA, ATECO (43.22.07 o 43.21.02), secondo indirizzo (via Padova 76) e secondo telefono, certificazioni (F-gas, DM 37/08, SOA), titolari, clienti e lavori con nome, recensioni Google (4,1 su 13), contenuto della pagina Facebook.

## Foto da rifare dal vero

Tutte le foto in pagina sono segnaposto Pexels (licenza "Free", elenco in `assets/CREDITI.md`). Il raccordo in rame è l'unica foto a colori; le altre sono in bianco e nero neutro; la parete d'inverno resta calda. Un giorno di scatti su due cantieri basta. Regole comuni: fondo scuro o luce radente, macro 50-100 mm su cavalletto, luce di studio o una lampada a mano laterale, niente persone riconoscibili, niente marchi concorrenti di Viessmann in primo piano, file RAW o JPEG almeno 4000 px di lato lungo. Le righe dei mestieri sono strisce orizzontali 3,5:1 (2,6:1 al telefono): inquadrare largo, con il soggetto a metà altezza.

1. **T, apertura (per prima).** Un raccordo a T in rame brasato su un loro impianto, fotografato frontale con la barra orizzontale e il gambo verso il basso, il gambo lungo almeno quanto la barra è larga e tutto il resto nel buio; serve che barra e gambo siano dritti e interi, perché la pagina allinea il gambo alla lettera T dell'alfabeto. Dallo stesso scatto si ricava la striscia della riga 02.
2. **E.** Il loro quadro elettrico cablato: marrone, blu e giallo-verde pettinati in parallelo, una fila di magnetotermici con le etichette scritte a mano; oggi sono i morsetti di un quadro qualsiasi, in bianco e nero perché i colori dei cavi non sono quelli di un impianto civile italiano.
3. **P.** La griglia di una pompa di calore Viessmann installata da loro, macro in controluce; oggi è la griglia di un climatizzatore qualsiasi.
4. **Collettore.** Un collettore in ottone prima del massetto, dall'alto o frontale, con le spire dei tubi sull'isolante.
5. **F.** Moduli su un tetto in coppi della Riviera del Brenta, luce radente del tardo pomeriggio, la griglia delle celle leggibile.
6. **M.** Una presa di ricarica montata da loro, a muro o su colonnina.
7. **R.** Intonaco fresco su una parete di una loro ristrutturazione, luce radente.
8. **A.** Acqua da un addolcitore o filtro installato da loro, controluce su fondo nero.
9. **C.** La griglia di un'unità interna di climatizzazione installata da loro.
10. **Parete d'inverno.** Un interno finito da loro, a cantiere chiuso, con la luce del pomeriggio sul muro e nessun impianto in vista (formato orizzontale, la parte bassa più scura: sopra ci va la frase).

## Licenze

- Caratteri: Funnel Display e Funnel Sans, The Funnel Project Authors (Dicotype), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file serviti dalla pagina in `sito/fonts`, licenza in `sito/fonts/OFL.txt`.
- Foto: licenza Pexels (uso libero anche commerciale, attribuzione non richiesta, modifiche ammesse; non far credere che persone o marchi ritratti approvino il prodotto). Dettagli e pagine in `assets/CREDITI.md`.
- `assets/originali/header.jpg` (foto di repertorio del sito attuale): licenza ignota, non usata.

## Loghi e pagine

- Il logo in pagina è il raster 480x80 del sito attuale, schiarito con PIL per il fondo grafite (`sito/img/logo-chiaro.png`): serve il logo vettoriale.
- Privacy e cookie: le pagine non esistono e i link sono stati tolti dal piede; vanno scritte e collegate prima di pubblicare.
- Favicon: quella del sito attuale (192x192).
