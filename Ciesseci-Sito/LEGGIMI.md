# Ciesseci (CSC Factory): proposta di nuova home

Proposta non richiesta di nuova homepage per Ciesseci Srl, marchio CSC Factory, Mestrino (PD). Solo la home, livello professionale del 3 novembre 2026.

- Pagina finale: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`.
- Screenshot e note di progetto: `screenshot/home/` (`home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, `NOTA.md` con l'esito delle 15 regole).
- Per rifare tutto: `bash _prova/script/build_finale.sh` (con `--immagini` rifà le foto con `_prova/script/pro_img.py`); controlli delle regole e dei compiti: `node _prova/script/pro_controlli.mjs` (esito in `_prova/pro_controlli.json`); screenshot di una larghezza: `node _prova/script/pro_shoot.mjs <larghezza> <altezza> [mobile] [ora]`.
- Lo stato "Aperto ora / Chiuso ora" si prova con `index.html?ora=AAAA-MM-GGTHH:MM` (ora di Roma).
- Versione di prima (24 ottobre, con le foto di repertorio): `_prova/versione-1-originale/` (sito e screenshot, con la sua NOTA). Gli script `build_img.py`, `shots.mjs` e `prova_finale.mjs` sono di quella versione.
- Analisi con le fonti: `01-analisi.md`; scheda d'uso: `_prova/uso/SCHEDA.md`; crediti delle foto: `assets/CREDITI.md`.

## Da chiedere o confermare con l'azienda

1. **Anno**: in pagina "dal 1982" (l'attività dei tre amici, come scrivono loro); la srl risulta del 2003 (companyreports.it). Serve il loro sì.
2. **Cellulare e WhatsApp**: in pagina 327 8831747 (sito e link WhatsApp); la locandina del 2019 scrive 347 8831747.
3. **Laboratorio e studio grafico in Via Zanella**: in pagina "negozio, showroom e laboratorio, con lo studio grafico in casa". Confermare che sono nello stesso edificio, e se gli orari valgono anche per il laboratorio.
4. **Festivi e ferie**: lo stato considera chiusi i festivi nazionali e Pasquetta; il patrono di Mestrino e le chiusure di Natale non sono nelle fonti. Le ferie si scrivono ogni anno nell'elenco `CHIUSURE` in cima allo script della pagina (oggi c'è solo quella del 2025, dal 7 al 24 agosto, presa dal loro popup); la riga di avviso compare da 30 giorni prima, al posto del popup.
5. **Marche**: in pagina in testo (scarpe Diadora Utility, Dike, Giasco, Sparco, Reebok; abbigliamento Snickers, Rossini, P&P Workwear, Siggi, Payper, Issa, Industrial Starter, Isacco, Neri, Giblor's, Velilla, Vesti; capi da stampare B&C, Gildan, Fruit of the Loom, Stedman, Russell, James Ross, Clique), dai loghi del loro sito, alcuni del 2018. Confermare quali trattano ancora e se si possono nominare; Angiolina e gli altri non elencati vanno aggiunti se servono.
6. **DPI**: in pagina "capi ad alta visibilità, caschi, guanti, occhiali, imbracature" (dalla scheda d'uso). Estintori, materiale pompieristico e porte tagliafuoco, citati in una pagina del sito, non sono in home: dire se li vendono ancora.
7. **Tecniche in casa o fuori**: quali lavorazioni fanno in laboratorio e quali affidano fuori (car wrapping completo, stampa digitale di grande formato).
8. **"Anche pochi pezzi" e "anche su singolo pezzo"**: la seconda è loro per plex e stampa UV, la prima viene da "sia piccole produzioni che produzioni in serie" (serigrafia). Confermare che valgono anche per ricamo e capi.
9. **Formati del logo**: in pagina non c'è un elenco; chiedere quali accettano (PDF, AI, SVG, PNG?) per scriverlo sopra il bottone.
10. **Prove che mancano (regole 10 e 11)**: recensioni (Google, Facebook) con il permesso di citarle; tre lavori con il nome del cliente o dell'associazione, l'anno e due dati (quanti capi, che tecnica), con foto; clienti che si possono nominare; eventuali certificazioni o accreditamenti come rivenditore. Oggi non ci sono nelle fonti e non sono in pagina.
11. **RicaMarty**: in home con il percorso `shop/ricamarty/` e Instagram `ricamarty_`: va bene così?
12. **Numeri ufficiali** (dipendenti, fatturato), PEC e referente: non pubblici, non in pagina.
13. **Parcheggio**: dalla foto della facciata si vede spazio davanti al negozio; se c'è un parcheggio per i clienti, si aggiunge una riga in "Orari e dove".

## Il modulo del preventivo (da collegare)

Il modulo in home ("Oppure scrivi qui la richiesta") controlla nome, telefono e supporto e **compone un'email** a info@ciessecisrl.it con l'oggetto "Preventivo: <su cosa>, <nome>" e i campi nel testo (`mailto:`): non invia nulla da solo e non può allegare il file del logo, quindi la pagina chiede di allegarlo alla mail che si apre o di mandarlo su WhatsApp. Per il sito vero va **collegato a un servizio** (per esempio un modulo del server, Formspree o il modulo di WordPress) con: un campo per il file del logo (PDF, AI, SVG, PNG, JPG), la casella del consenso all'informativa e un messaggio di conferma in pagina. A quel punto si toglie la riga "allega il file del logo" e la funzione di collaudo `__prova` in fondo allo script.

## Foto da rifare dal vero

In pagina ci sono solo foto loro (elenco in `assets/CREDITI.md`), tutte da telefono a 1024 px: reggono a 1x ma sugli schermi 2x sono morbide. Una mattina con luce naturale, stesso fotografo, stessa luce e stesso taglio (3:2 orizzontale, almeno 3000 px), senza grandangolo spinto:

1. **Apertura, la più importante**: lo showroom dalla porta, con la parete delle scarpe, le giacche e una persona di Ciesseci al bancone o che porge una scarpa a un cliente. Oggi è `2019-02-ciesseci-nuova-sede-2.jpg` del 2019.
2. **Scarpe e DPI**: la parete delle scarpe antinfortunistiche da vicino, con i numeri e un casco e un paio di guanti in primo piano (oggi `2019-02-ciesseci-nuova-sede-6.jpg`).
3. **Le quattro schede**: un capo da lavoro vero con il logo di un cliente ricamato o stampato, steso piano; la ricamatrice che ricama un nome; il furgone di un cliente appena decorato (o il loro, di giorno, di tre quarti); un plex o una targa appena stampati sul piano della stampante UV.
4. **Chi siamo**: le persone di Ciesseci davanti al bancone con la coccarda (oggi c'è solo il bancone vuoto).
5. **Facciata**: frontale, giornata limpida, con le vetrine illuminate (oggi `2022-04-sede-nuova-1.jpg`).
6. **RicaMarty**: tre ricami su capi diversi, puliti su fondo chiaro (oggi una composizione affollata del loro shop).

## Loghi

- In pagina il logo è il PNG originale `logo-badge-500x486.png` ridotto a 96 e 192 px (`sito/img/logo-csc-96.png`, `-192.png`). Nessun vettoriale disponibile: chiedere l'SVG o l'AI della coccarda.
- I colori della pagina vengono dalla coccarda (verde scuro e verde chiaro) e dall'antracite del furgone e della facciata.

## Licenze

- Carattere: Archivo (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`, licenza in `sito/fonts/OFL-Archivo.txt`).
- Foto: materiale di Ciesseci Srl preso dal loro sito. Nessuna foto di repertorio in pagina.

## Pagine a cui portano i link (da creare o tenere nel sito nuovo)

- `abbigliamento/abbigliamento-da-lavoro/`, `abbigliamento/calzature-antinfortunistiche/`, `abbigliamento/abbigliamento-tempo-libero/`, `cataloghi/`, `promozioni/`
- `pubblicita/` con `serigrafia/`, `ricamo/`, `decorazione-automezzi/`, `stampa-uv/`, `stampa-digitale/`, `timbri/`, `incisioni-laser/`, `tampografia/`, `grafica/`
- `zerbini-e-tappeti-personalizzati/`, `shop/` e `shop/ricamarty/`
- `termini-duso-e-informative/informativa-privacy/`, `termini-duso-e-informative/cookie-policy/`
- Social: Facebook https://www.facebook.com/ciesseci, Instagram https://www.instagram.com/ciessecisrl/, RicaMarty su Instagram https://www.instagram.com/ricamarty_/ (profili non aperti: bloccano i browser automatici).
