# Ciesseci (CSC Factory): proposta di nuova home

Proposta non richiesta di nuova homepage per Ciesseci Srl, marchio CSC Factory, Mestrino (PD). Solo la home.

- Pagina finale: `sito/index.html` (statica, si apre con file:///), immagini in `sito/img/`, carattere in `sito/fonts/`.
- Screenshot e note di progetto: `screenshot/home/` (`home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`, `chiusura-1440.jpg`, `NOTA.md`).
- Per rifare tutto (immagini, carattere, screenshot): `bash _prova/script/build_finale.sh`. Collaudo di schede, newsletter, link, densità delle foto e scorrimento: `node _prova/script/prova_finale.mjs <percorso di sito/index.html> <cartella>`.
- Analisi con le fonti: `01-analisi.md`; crediti delle foto: `assets/CREDITI.md`; giudizio cieco a cui risponde l'ultima rifinitura: `_prova/cieco.json`; prototipi: `_prova/home/a` (base scelta) e `_prova/home/b`.

## Dati da confermare con il cliente

- **Anno**: in pagina "dal 1982" (l'attività dei tre amici, come scrivono loro); la srl risulta fondata nel 2003 (companyreports.it). Serve il loro sì.
- **Cellulare**: in pagina 327 8831747 (sito e link WhatsApp); la locandina del 2019 scrive 347 8831747.
- **Laboratorio in Via Zanella**: in pagina "Negozio, showroom e laboratorio a Mestrino" e "2019, Via Zanella 1: negozio, showroom e laboratorio, inaugurati il 23 febbraio" (dalla locandina `2019-02-CSC-popup.jpg`). Che il laboratorio sia nello stesso edificio va confermato; manca la tappa della sede precedente (la tenda "CSC FACTORY" delle foto del 2018).
- **Facciata nella chiusura**: la foto `2022-04-sede-nuova-1.jpg` è della sede di Via Zanella (stessa insegna); la didascalia dice "Negozio e showroom dal 2019". Va bene mostrarla?
- **Felpa 82**: nella sezione 1982 c'è il dettaglio della loro felpa con la didascalia "Il 1982 stampato come un numero di maglia". È ancora il loro merchandising?
- **Undici lavorazioni**: il conto viene dalle pagine del sito (grafica compresa); quali sono fatte in casa e quali affidate fuori.
- **Frasi composte da testi loro**: "Abbigliamento da lavoro e calzature con il vostro marchio, e il nome di chi li indossa"; "Sportive e culturali, o la tua band: maglie, felpe, striscioni e gadget"; "Il plex anche con taglio su misura, su singolo pezzo" (dallo slider sulla stampa UV su plex); "Tessuto: la stampa entra nella tinta" (dalla loro frase sulla sublimazione, "modificando direttamente la tinta del tessuto").
- **Orari**: valgono anche per il laboratorio?
- **RicaMarty**: in home e con il percorso `shop/ricamarty/`?
- **Marchi**: nella foto dello showroom (sezione abbigliamento) si leggono in piccolo sulla parete delle scarpe Giasco e Sparco; i marchi fornitori non sono citati nel testo e vanno chiesti prima di nominarli.
- PEC, referente, numeri ufficiali (dipendenti, fatturato): non pubblici, non in pagina.

## Foto da rifare dal vero

Mezza giornata di still life più un'ora in laboratorio e showroom, luce naturale. In pagina ci sono cinque segnaposto di repertorio (elenco in `assets/CREDITI.md`): vanno tutti sostituiti prima di qualsiasi uso pubblico.

1. **Apertura, la più importante.** Oggi è un segnaposto: una maglietta bianca intera di Pexels (Mr. Mockup), senza marchio. Da rifare con un capo loro: una maglietta, una polo o una felpa con il marchio di un cliente (o la felpa 82) appena stampato o ricamato sul petto. Capo intero steso piano su carta o tela chiara, fotocamera in perpendicolare dall'alto, luce laterale morbida da finestra, maniche aperte, tutto a fuoco, niente altri oggetti, almeno 3000 px sul lato lungo. In pagina il capo è mostrato a 680 px a 1440, quindi la sorgente deve dare almeno 1400 px di capo. Il fondo si porta al colore carta con lo stesso script (`build_img.py`, sezione 1), che tiene l'ombra vera del capo.
2. **Felpa 82 da vicino** (sezione 1982): oggi è un ritaglio di `2018-02-csc-factory-14.jpg` (1024 px, mostrato a 421 px). Da rifare in macro: la stampa fluo e il marchio dentro l'8, almeno 2000 px.
3. **Le cinque schede** (2:1, almeno 2900 px di larghezza per gli schermi 2x, stessa luce e stessa altezza): coni di filo sulla loro ricamatrice, la racla sul loro telaio serigrafico, la loro termopressa con un capo, il piano della stampante UV con un pezzo stampato, il loro laser su una targa. Oggi Ricamo, Serigrafia, Sublimazione e Incisione laser sono segnaposto; la Stampa UV è loro.
4. **Showroom** (sezione abbigliamento): la foto loro del 2019 è da telefono, 1024 px; in pagina è un ritaglio 4:5 di 544 px mostrato al massimo a 544 px, quindi non si ingrandisce, ma sugli schermi 2x resta morbida. Rifarla verticale, con luce del mattino, sulla giacca verde e i capi, senza grandangolo spinto, almeno 1600 px di larghezza.
5. **Facciata** (chiusura): `2022-04-sede-nuova-1.jpg`, 1024 px, mostrata a 793 px a 1440. Rifarla in giornata limpida, frontale, almeno 2400 px.

## Licenze

- Carattere: Archivo (Omnibus-Type), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; servito dalla pagina (`sito/fonts/archivo-latin-var.woff2`, licenza in `sito/fonts/OFL-Archivo.txt`).
- Foto di repertorio (segnaposto, da sostituire): Unsplash License e Pexels License, verificate sulla pagina di ogni foto; elenco, autori e URL in `assets/CREDITI.md`. Nelle foto di Wallace (coni) e Compagnons (maglietta) sono state tolte le scritte dei marchi di terzi.
- Foto dell'azienda: materiale di Ciesseci Srl preso dal loro sito.

## Loghi

- In pagina il logo è il PNG originale `logo-badge-500x486.png` ridotto a 128 e 240 px (2x per 56 e 96 px). Nessun vettoriale disponibile (né nel codice né nei PDF): chiedere al cliente l'SVG o l'AI della coccarda. Non è stato ridisegnato.
- RicaMarty ha un suo logo (`logo-ricamarty-1600x677.jpg`), non usato in home.

## Newsletter

Ha senso (shop per privati, pagina Promozioni, cataloghi stagionali, RicaMarty). Il modulo nel piede (email, bottone "Iscriviti", casella del consenso obbligatoria con il link all'informativa) **non invia nulla**: controlla i campi e risponde in pagina "Modulo dimostrativo: non ancora collegato al servizio di invio." (zona `aria-live`). Va collegato a un servizio (per esempio Brevo o Mailchimp) con doppia conferma; poi si toglie il messaggio dimostrativo dallo script in fondo alla pagina e si aggiorna l'informativa privacy.

## Pagine a cui portano i link (da creare o tenere nel sito nuovo)

- `chi-siamo/`, `preventivo/`, `cataloghi/`, `promozioni/`
- `pubblicita/` con `ricamo/`, `serigrafia/`, `sublimazione/`, `stampa-uv/`, `incisioni-laser/`, `tampografia/`, `stampa-digitale/`, `timbri/`, `decorazione-automezzi/`, `grafica/`
- `zerbini-e-tappeti-personalizzati/`
- `abbigliamento/abbigliamento-da-lavoro/`, `abbigliamento/calzature-antinfortunistiche/`, `abbigliamento/abbigliamento-tempo-libero/`
- `shop/` e `shop/ricamarty/`
- `termini-duso-e-informative/informativa-privacy/`, `termini-duso-e-informative/cookie-policy/`
- Le voci Lavorazioni, Abbigliamento, Showroom, Chi siamo e Contatti del menu e del piede puntano alle sezioni della home.
- Social: Facebook https://www.facebook.com/ciesseci, Instagram https://www.instagram.com/ciessecisrl/, RicaMarty su Instagram https://www.instagram.com/ricamarty_/ e su Facebook https://www.facebook.com/people/RicaMarty/61558415187099/ (profili non aperti: Instagram e Facebook bloccano i browser automatici).
