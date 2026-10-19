# Paraga Pelli, proposta di nuova home (preparazione)

- 01-analisi.md: azienda, sito di oggi, materiale visivo, direzioni artistiche, riferimenti.
- assets/originali/: immagini scaricate dal sito paragapelli.com (inventario e voti in _prova/inventario-immagini.json).
- assets/esterne/: foto Unsplash e Pexels usate SOLO come segnaposto per mostrare la direzione artistica. Non sono foto di Paraga Pelli e vanno sostituite con foto vere dell'azienda prima di qualsiasi uso pubblico. Autori e licenze in assets/CREDITI.md.
- _prova/: lavoro di servizio (gitignored): crawl, screenshot del sito attuale, screenshot dei riferimenti, script.

## Prototipo A della home ("La mazzetta", _prova/home/a/)

Dettagli in _prova/home/a/nota.md. Da confermare prima di pubblicare: forma giuridica (srl o S.a.s.) e civico (37 o 31), per questo in pagina ci sono solo nome, P.IVA e "Via del Lavoro"; deposito di Altamura (non in pagina); catalogo attuale (27 articoli, 403 colori, codici Botticelli 2101-2125); uso della certificazione LWG Gold; contenuto del box-campionario; licenza del drappo bianco della home attuale (forse stock); logo vettoriale.
Foto da rifare dal vero: macro del drappo per i colori Botticelli in luce radente; scansioni del campionario a 1200 px o più; box-campionario aperto come oggetto; taglio netto sul rotolo e mano su un pull-up per il dittico (oggi Unsplash, Milkovic e Vid); corsia del magazzino intera.

## Prototipo B della home ("Pelle intera"), _prova/home/b/

- Nota completa in `_prova/home/b/nota.md`.
- Da confermare prima di pubblicare: forma giuridica (srl o S.a.s.) e civico della sede (37 o 31), oggi non a vista; deposito di Altamura ancora attivo; consenso a mostrare LWG Gold; catalogo attuale (27 articoli, 398 colori nelle schede del sito contro i 403 dell'analisi); logo vettoriale.
- Foto da rifare dal vero: pelle intera stesa sul banco di scelta con le mani, dall'alto, luce naturale laterale (apertura); corsia del magazzino a piena risoluzione, orizzontale e verticale; pila di pelli sul pallet col bordo vivo; rotoli di ecopelle sullo scaffale; un imbottito di un cliente in luce radente; il box-campionario come oggetto; originali del servizio "Azienda".
- Scansioni dei colori scaricate dal sito in `assets/originali/campionario-b/` (398 file, 350x350).

## Home finale ("La mazzetta", sito/)

- Pagina: `sito/index.html`, immagini in `sito/img/` (solo quelle usate: 403 scansioni WebP a 350 e a 640, drappo, dorsi, corsia, squadra e box in più larghezze; tutte di Paraga Pelli), caratteri in `sito/fonts/` con le licenze OFL. Nota completa: `screenshot/home/NOTA.md`. Screenshot: `screenshot/home/home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`.
- Si rifà tutto con `bash _prova/script/build_finale.sh` (script `finale_catalogo.py`, `finale_img.py`, `finale_drappo.py` per la taratura del drappo sulle scansioni, `finale_pagina.py`, `finale_scatti.mjs`, modello `finale_modello.html`, opacità fissate a mano in `finale_correzioni.json`). Controlli: `node _prova/script/finale_verifica.mjs <percorso di sito/index.html> _prova/finale/verifica`.
- Prototipi A e B superati: i dati qui sotto valgono per la versione finale.

### Dati da confermare prima di pubblicare

- **Forma giuridica**: "srl" sul sito, "S.a.s. di Bordin Michele & C." nei registri e su LWG. In pagina solo "Paraga Pelli" e la P.IVA 03748440272.
- **Civico della sede**: 37 sul sito, 31 nei registri e su LWG. In pagina "Via del Lavoro, 30030 Tombelle di Vigonovo (VE)" senza numero.
- **Deposito di Altamura (BA)**: se è ancora attivo. Non in pagina.
- **Catalogo**: 27 articoli e 403 colori ricontati sulle schede della copia del sito (ferma a febbraio 2025). Va chiesto se è ancora attuale e se i nomi dei colori in inglese (Corfu, Creta, Mykonos, Lipsi: "white 01", "toffee 02") e la sigla "Sc" di Monza sono quelli da mostrare.
- **LWG Gold**: consenso a mostrarlo, con codice PAR103, dal 2 febbraio 2026, audit fino al 2 febbraio 2027 (dal sito del Leather Working Group). Dopo febbraio 2027 la data va aggiornata.
- **Box-campionario**: cosa contiene, se si spedisce, se è gratuito. In pagina solo "le cartelle colori in una scatola, con la maniglia arancio; si chiede per email o al telefono".
- **Anno di inizio attività**: il 2007 dei registri non è in pagina.
- **Drappo dell'apertura**: è lo sfondo della home di oggi; se è uno stock va comprata la licenza o rifatta la foto (vedi sotto).
- **Madras "rosso F"**: sulla scheda il titolo è "Madras rosso f", il file `MADRAS_ROSSO_F.jpg`. In pagina "rosso F"; va chiesto il nome intero (rosso fuoco?).
- **Spessorato**: la scheda dice "Spessore 1.3/1.5" senza unità; in pagina "1,3/1,5 mm" come Botticelli e Piston. Da confermare.
- **Foto della squadra** (sfondo di "Chi siamo" sul sito): se è ancora attuale e se le sei persone acconsentono a vederla in home. In didascalia nessun nome.
- **Logo**: manca un vettoriale; in pagina il nome è scritto in Mona Sans. Il logo a palme e sole non è usato.
- **Pagine collegate**: lingue (EN, DE, FR, PL) e Privacy puntano a "#" finché non esistono le pagine.

### Foto da rifare dal vero (in ordine di priorità)

1. **Il drappo, per i 6 colori Botticelli più venduti.** Una pelle intera o un taglio di almeno 1x1,5 m, appoggiata su un piano e mossa in due o tre pieghe morbide, ripresa dall'alto a 30-40 gradi. Stesso set per tutti i colori: luce radente da sinistra (un flash con stripbox basso, a 15-20 gradi sul piano), nessuna luce di riempimento, bianco misurato su un cartoncino grigio. File grezzi ad almeno 4000 px di lato lungo, orizzontali, con 20% di margine attorno alle pieghe per il taglio verticale del telefono. Sostituiscono la mappa di luce per quei colori; gli altri restano tinti.
2. **Le scansioni dei colori a 1200 px o più** (oggi 350 px): stesso scanner o stessa luce diffusa, stessa esposizione per tutti, profilo sRGB, nessuna correzione per colore. Servono al cartellino sugli schermi ad alta densità.
3. **Il box-campionario come oggetto**: aperto, con le cartelle a ventaglio e quella del colore scelto davanti, su fondo carta #ECEBE7, luce morbida da sinistra, ripreso di tre quarti, orizzontale 3:2 e un ritaglio verticale per il cartellino della fascia LWG. Sostituisce il box da 265 px; la versione orizzontale può tornare come foto larga dopo il catalogo (la foto Unsplash che c'era è stata tolta).
4. **La corsia del magazzino in orizzontale intero**, a piena risoluzione (oggi 1680x400), dal centro della corsia, ottica 35 mm, luce del capannone accesa e porte chiuse; una versione verticale per il telefono (oggi il ritaglio da 400 px è sgranato).
5. Gli originali del servizio fotografico "Azienda" (oggi 350 px): mani sulla pelle, taglierina sul rotolo, cavalletti.
6. **La squadra in magazzino** all'originale (oggi 1620x800, sfondo del sito), o rifatta con la stessa luce del drappo, se la foto non è più attuale.

### Licenze

- Caratteri: Libre Caslon Display e Mona Sans, SIL Open Font License 1.1 (uso commerciale libero; file Google Fonts non modificati, licenze in `sito/fonts/`).
- Foto dell'azienda: drappo (da verificare), scansioni, box, corsia, squadra, dal sito paragapelli.com.
- Segnaposto: nessuna foto esterna nella home finale (la foto di Kelly Sikkema, Unsplash, è stata tolta; `assets/CREDITI.md`).
- Loghi: nessun logo di terzi in pagina; il marchio LWG non è usato, solo il nome e un link alla scheda pubblica.
