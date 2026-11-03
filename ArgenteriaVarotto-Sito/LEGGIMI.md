# Argenteria Varotto Alfredo: proposta di nuova home

Proposta non richiesta, solo la home. Niente è stato inviato all'azienda né pubblicato.

- Pagina: `sito/index.html`, con `sito/img/` e `sito/fonts/`. Si apre anche da file.
- Screenshot e nota di progetto: `screenshot/home/` (`NOTA.md`, sezione "Livello professionale": le 15 regole una per una, i compiti dei visitatori, i controlli).
- Rigenerare tutto: `bash _prova/script/build_finale.sh` (immagini `pro_img.py`, sorgente della pagina `pro_pagina.html`, catture `pro_vista.mjs`, tagli `pro_tagli.py`). Controlli delle regole: `node _prova/script/pro_controlli.mjs`. Prodotti e prezzi dello shop letti il 3/11/2026: `_prova/crawl/shop-pro/` (pagine compresse in .gz, estratte con `pro_shop_parse.py` dopo `gunzip -k`, elenco in `pro-prodotti.txt`).
- Ultimo passaggio (3 novembre, livello professionale): via le foto di repertorio, il banco di posa e il selettore dei metalli; la home è ordinata per i tre visitatori della scheda d'uso (`_prova/uso/SCHEDA.md`): hotel e ristoranti, riparazione, shop. La versione precedente è in `_prova/versione-1-originale/`.
- Analisi con le fonti: `01-analisi.md`.

## Il modulo di contatto va collegato a un servizio

Il modulo "Scrivete la richiesta" oggi **non invia nulla**: controlla nome ed email e compone un'email (`mailto:info@varottoalfredo.com` con oggetto e tutti i campi) nel programma di posta di chi lo compila. Per il sito vero va collegato a un servizio di invio (Formspree, Brevo o il modulo del CMS che useranno), con:

- invio a info@varottoalfredo.com (e, se la tipologia è estera o la lingua è inglese, a export@);
- **allegati** (foto del pezzo da riparare, elenchi, disegni): con il `mailto:` non si possono allegare file, oggi la pagina dice di allegarli all'email che si apre;
- casella del consenso privacy collegata alla nuova informativa (quella di oggi cita ancora il D.Lgs. 196/2003);
- una risposta automatica con i tempi in cui richiamano (da chiedere, punto 9).

Anche i bottoni "Mandate le foto del pezzo" e "Preventivo per quantità" aprono un'email già compilata: vanno bene così anche nel sito vero.

## Da chiedere o confermare con l'azienda (non è a vista in pagina, o lo è nella forma più prudente)

1. **Orari** di apertura e se ricevono privati in sede. Un elenco online (trova-aperto.it) dà lunedì-venerdì 8.30-13.15: non sono in pagina; c'è solo "Prima di passare, chiamate". Con gli orari veri vanno nel blocco Contatti e nel piede.
2. **WhatsApp +39 392 502 4576**: è quello dello shop. Vale anche per le foto dei pezzi da riparare? Se sì, accanto a "Mandate le foto per email" si aggiunge "Mandate le foto su WhatsApp".
3. **Recensioni**: la regola 10 chiede recensioni con nome e comune. Nelle fonti c'è solo il negozio eBay "varottoshop" (circa 630 vendite e 100 % di giudizi positivi, due frasi di acquirenti), letto tramite ricerca: la pagina eBay non si apre da qui. Possiamo citare i giudizi eBay? Hanno recensioni Google o lettere di clienti (hotel, ristoranti) da pubblicare con il nome?
4. **Clienti e lavori con il nome**: hotel, ristoranti, pasticcerie o catering forniti, con città e anno, e qualche riparazione fatta (che pezzo, che lavoro). Sono le prove che mancano (regole 10 e 11).
5. **Numeri aziendali**: anni del laboratorio, persone, metri quadri, paesi dell'export, articoli in catalogo. In pagina ce ne sono tre (1974, 364 PD, 925 e 800); la regola ne chiede da 4 a 8.
6. **Prezzi dello shop**: in pagina ci sono undici prezzi letti sullo shop il 3/11/2026 (IVA inclusa). Cambiano: vanno riletti prima di pubblicare, o la pagina li va a prendere dallo shop.
7. "Dal 1974": in pagina c'è "dal 1974" come nella testata di oggi ("Since 1974"); il testo Azienda dice "agli inizi degli anni '70". Quale preferiscono?
8. Chi è Luca Varotto rispetto ad Alfredo, a chi è intestato il punzone 364 PD e se la produzione in Corso Stati Uniti è dell'impresa (l'attività registrata è "commercio all'ingrosso di metalli non ferrosi"). In pagina c'è la loro frase "Tutta la produzione dell'argenteria è eseguita all'interno del nostro stabilimento di Padova".
9. Riparazioni: tempi tipici, se fanno il ritiro e come si spedisce un pezzo. Oggi la pagina dice solo che "l'incaricato" dà fattibilità, ritiro e tempi, come la loro pagina Assistenza.
10. Royal Queen, Royal England, Sweet Home, VarottoHotellerie e TEN sono marchi loro? Le righe dei marchi in pagina descrivono ciò che si vede sullo shop.
11. PEC e REA per la riga legale.
12. Area clienti: l'indirizzo della pagina di oggi (area riservata per le proposte d'ordine) o una pagina nuova. In pagina il link porta a `area-clienti/`.
13. Social: Facebook (varottostore) e Pinterest (lucavarotto) sono dello shop e nel piede sono scritti così. Vanno tenuti? Instagram non è verificato e non c'è.
14. Il vecchio indirizzo "Varotto Alfredo, via del Santo 75, 049 8761205" (impresaitalia.info): un negozio in centro che esiste ancora?
15. Fiere: la pagina di oggi è vuota. Se partecipano ancora (Homi, Ambiente, Vicenzaoro), una data con città e stand va in home.

## Pagine del sito nuovo (destinazioni dei link della home)

| Link | Pagina |
|---|---|
| Area clienti (proposte d'ordine dei rivenditori) | `area-clienti/` |
| English | `en/` |
| Privacy, Cookie | `privacy/`, `cookie/` |
| Famiglie del catalogo, prodotti, categorie per chi regala, "Apri lo shop" | varottoshop.com (esterno): `buffet.html`, `bar-pasticceria.html`, `buffet/vassoi-rettangolari.html`, `buffet/secchielli-champagne-ghiaccio.html`, `posateria.html`, `tavola-e-cucina/sottopiatti-in-vetro.html`, `complementi-arredo/bomboniere.html`, `oggettistica/prima-infanzia.html`, `oggettistica.html`, `complementi-arredo/centrotavola.html`, `-offerte.html` e cinque schede prodotto |

Le voci del menu Hotel e ristoranti, Riparazione, Chi siamo e Contatti portano alle sezioni della home. Quando ci saranno le pagine interne (Riparazione, Hotel e ristoranti, Storia e punzoni) le stesse voci possono portare lì.

## Foto da fare dal vero

Oggi in pagina ci sono solo foto loro: dieci foto di catalogo dello shop (sul bianco, al massimo 1280 px), la sede (500 x 301, vecchia, con il cielo bruciato) e il logo. Mancano le foto che dicono chi lavora e dove. Una giornata con un fotografo basta, con una sola luce per tutta la serie:

1. **Apertura**: mani che lucidano o riargentano un vassoio al banco del laboratorio, luce di finestra laterale, fondo del laboratorio leggibile ma non disordinato, formato 4:3 orizzontale, almeno 2400 px. Va al posto del riquadro del vassoio (che resta nella sezione shop).
2. **Riparazione**: la stessa serie, tre scatti: un pezzo rovinato com'è arrivato, il lavoro (pulitrice, bagno galvanico se c'è, martello), il pezzo finito. Quadrati o 4:3, stessa luce. Rendono vera la sezione su blu, che oggi è solo testo.
3. **La sede**: facciata di Corso Stati Uniti 23/A con l'insegna, di giorno con cielo coperto (niente cielo bruciato), più l'ingresso per chi arriva in auto. 3:2, almeno 2000 px.
4. **Hotel e ristoranti**: un buffet o un tavolo di pasticceria allestito con i loro pezzi (alzate, vassoi, campane), meglio in un hotel cliente con il permesso di nominarlo: è anche il "lavoro con un nome" che manca.
5. **Punzoni**: macro dei tre punzoni impressi su un pezzo in 925, luce radente da un lato, obiettivo macro 1:1. Può sostituire i punzoni ridisegnati.
6. **Catalogo**: le foto dello shop reggono come miniature; per le sei famiglie servono a 1600 px, tutte con lo stesso fondo, la stessa ombra e la stessa inquadratura (oggi alcune hanno l'ombra e altre no).
7. **Il vassoio inciso dell'apertura** ad almeno 2500 px: quello dello shop è 1280 px.

## Licenze

- Caratteri: Boska (Fontshare, ITF Free Font License 2.0, uso commerciale gratuito, `sito/fonts/FFL.txt`); Rethink Sans (Google Fonts, SIL Open Font License 1.1, `sito/fonts/OFL-RethinkSans.txt`). Serviti dalla pagina.
- Foto: solo materiale dell'azienda (shop varottoshop.com e sito varottoalfredo.com), diritti da confermare: alcune foto dello shop potrebbero essere dei fornitori. Elenco in `assets/CREDITI.md`. Le foto Unsplash della proposta precedente non sono più usate.

## Loghi

- In pagina c'è il PNG originale (`assets/originali/logo-varotto-alfredo-130x153.png`, contenuto 75 x 96 px) mostrato a 46 px di altezza (nel piede in bianco con un filtro CSS). Serve il **vettoriale** (SVG, PDF o AI) per il sito vero e per il favicon, che oggi manca.
- I tre punzoni sono ridisegnati in SVG dalle GIF del sito (`logo-punzone-364PD.gif`, `logo-punzoni-925-800.gif`, `logo-scritta-varotto-alfredo-168x29.gif`): forma fedele, carattere Rethink Sans. Con i punzoni veri in alta definizione si rifanno identici.
