# Daisyplast: LEGGIMI della proposta

## Versione WordPress della home (come per Benvegnù)

> **Da rigenerare (ottobre 2026): la chiusura della home statica è cambiata, due volte.** In `sito/index.html` la sezione contatti non è più la fascia grafite con il telefono a 245 px e i quattro recapiti in riga (né la shopper disegnata in CSS che l'aveva sostituita per poco, bocciata dal committente), e il piede non è più grafite a tre colonne. Ora, nello stile B "con foto" scelto dal committente: a sinistra, a filo del bordo, una foto grande delle bobine (la 001, nuovi file `chiusa-*.webp` fatti da `_prova/script/finale_img.py`), a destra la frase "Estrudiamo il film in bolla e lo saldiamo in sacchi, shopper, bobine e monopieghe." e i recapiti in poche righe; il piede è una riga sola sul latte (vedi `screenshot/home/NOTA.md`, "La chiusura"). La versione WordPress (`elementor-json/`, `html-fallback/`, `anteprima/`, `plugin/`, generata da `_sorgente/`) ha ancora la chiusura vecchia: va aggiornata in `_sorgente/contenuti.py` (sezione contatti e piede) e in `_sorgente/prepara_immagini.py` (la foto nuova), rigenerata con `python3 _sorgente/build.py` e `python3 _sorgente/crea_installer.py`, poi ricollaudata. Fino ad allora il confronto "pixel per pixel" descritto qui sotto vale solo fino alla sezione clienti.

La home finale ("La bolla", `sito/index.html`) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina approvata: a 1440, 1024 e 390 px lo screenshot di WordPress e quello del fallback coincidono con quelli della home statica pixel per pixel (stessa altezza, nessuna differenza sopra la soglia), e lo stesso a 320, 375, 560, 561, 767, 768, 860, 861, 1000, 1025, 1100, 1180, 1260, 1261 e 1920 px, tranne alcune foto, che WordPress ricampiona dalle misure della sua libreria media (vedi "Collaudo fatto"). Le interazioni sono le stesse: schede dei materiali e tappe del percorso con clic, tocco, frecce, Inizio e Fine, palco che si sfoglia col dito, pulsante "Menu" sotto i 1260 px.

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `dsp-00-header.json` e `dsp-99-footer.json` (tipo *sezione*), `dsp-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `dsp-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 17 immagini (Elementor li perde all'import; l'installatore li scrive da solo) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `05-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/daisyplast-installer.zip` | plugin che installa e configura la home su un WordPress pulito, caratteri compresi (vedi "Installazione automatica") |
| `assets/web/` | le 17 immagini per WordPress, prese senza ritocchi da `sito/img/` (per ogni foto la misura più larga della statica e il taglio verticale del telefono), più `fonts/` con i due caratteri e la licenza OFL |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova e dall'anteprima HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi, sezioni, fogli di stile e script della statica), `motore.py` e `build.py` (quelli di Benvegnù, prefisso `dsp`; il motore non scrive il collegamento a Google Fonts nel fallback quando il tema non ne indica uno), `prepara_immagini.py`, `crea_installer.py`, `installer/` |

Come è fatta la pagina in Elementor:
- **Widget nativi, modificabili dal cliente** (117 elementi nella home, 9 nella testata, 6 nel piede): il titolo h1 "Sacchi e film in polietilene", i testi dell'apertura, il dato "oltre 10.000 kg", la didascalia, i tre cartellini dei materiali (titolo, materia, elenco dei prodotti), le cinque tappe (numero, titolo, frase, dettaglio), le cifre della saldatura, i clienti, il telefono grande, i quattro recapiti, il piede; le 16 foto (bolla, materiali e tappe, ognuna in due widget Immagine: una per computer e tablet, una con il taglio verticale per il telefono, come il `<picture>` della statica) e il logo, tutte nella libreria media con il loro testo alternativo; nella testata il logo, il menu (widget "Navigation Menu" di Ultimate Addons) e il telefono.
- **Widget HTML**, solo dove Elementor gratuito non arriva: il pulsante "Menu" (sotto i 1260 px, come la statica; Ultimate Addons cambierebbe menu a 1024), la copia latte del titolo ritagliata dentro la colonna della bolla (segue da sola il titolo vero, se lo si cambia), i nomi dei tre materiali e le cinque linguette del percorso (sono le schede, con lo script della statica). Altri widget HTML contengono solo il foglio di stile della loro sezione (le misure fluide, la colonna della bolla e la griglia a 12 colonne della statica, con le classi `dsp-`): stanno in un contenitore nascosto e non vanno cancellati.
- Accessibilità come nella statica: il primo tasto Tab porta a "Vai ai materiali" (il link "Salta al contenuto" di Ultimate Addons è nascosto); il logo si chiama "Daisyplast, pagina iniziale", il menu "Principale" e il pulsante ne dichiara lo stato (`aria-expanded`); schede e pannelli hanno `role="tablist"`, `tab` e `tabpanel`; le sezioni dall'apertura ai contatti stanno in un `<main>` (lo crea un piccolo script nel widget HTML dei contatti, perché Elementor gratuito non ha un contenitore che le raccolga; nell'editor non fa niente); le voci del menu portano alla sezione con un salto netto, come la statica, senza lo scorrimento morbido che Ultimate Addons aggiunge.

### Vedere il sito subito

Senza installare niente: doppio clic su `Daisyplast-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `Daisyplast-Sito` e http://localhost:8000/anteprima/). Immagini e caratteri vengono da `assets/web`, quindi funziona anche senza internet. È il Formato B: a vista uguale alla versione Elementor.

### Installazione automatica su un WordPress pulito

`plugin/daisyplast-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Daisyplast*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto e si può ripetere. Il passo "impostazioni" copia i caratteri in `wp-content/uploads/daisyplast/fonts/` e spegne i Google Fonts di Elementor; l'import dei template fa puntare lì le `@font-face` e scrive i testi alternativi delle foto nella libreria media; il passo del menu crea "Menu Daisyplast" con le quattro voci; la verifica dice quante immagini hanno il testo alternativo.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online togli la spunta in *Impostazioni > Lettura*. Contact Form 7 non serve: la home non ha moduli. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" | **sì**: il menu dell'header è un suo widget |

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

**Caratteri.** Sofia Sans e Sofia Sans Extra Condensed, gli stessi file woff2 della pagina statica (SIL Open Font License 1.1, licenza in `assets/web/fonts/OFL.txt`). Non passano da Google Fonts: ogni sezione ha nel suo foglio di stile le `@font-face` della statica, verso `fonts/sofiasans-latin.woff2` e `fonts/sofiasansextracondensed-latin.woff2` alla base delle immagini. Così funzionano in WordPress:
- **con l'installatore** (consigliato): i due file sono nello zip, l'installatore li copia in `wp-content/uploads/daisyplast/fonts/` e fa puntare lì le `@font-face` prima dell'import; spegne anche i Google Fonts che Elementor caricherebbe da sé (opzione `elementor_google_font` = 0). Provato: la home chiede caratteri solo al sito stesso, nessuna richiesta a Google o a GitHub;
- **con l'import a mano**: carica `assets/web/` sul sito (per esempio in `wp-content/uploads/daisyplast/`, `fonts/` è dentro) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/daisyplast/`, poi importa; spegni i Google Fonts in *Elementor > Impostazioni > Avanzate > Google Fonts: Disattiva*. Con i file così come sono nel repository le `@font-face` puntano a `raw.githubusercontent.com` (vedi "Immagini"), che funziona solo con il ramo pubblicato su GitHub.

Elementor non deve caricare Sofia Sans da sé: le misure, i pesi e i colori dei caratteri li danno i fogli di stile dei widget HTML (prevalgono sul pannello di Elementor).

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie gli script dai widget HTML e restano fermi il pulsante "Menu", le schede dei materiali e il percorso.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le 17 immagini arrivano durante l'import.
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**.

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu Daisyplast** (slug `menu-daisyplast`) con quattro "Link personalizzati": Materiali `/#materiali`, Un ordine `/#percorso`, Clienti `/#clienti`, Contatti `/#contatti`. Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `dsp-00-header.json` e `dsp-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Daisyplast: Header", salva. Lo stesso per il footer ("Daisyplast: Footer").
**3. La home.** Importa `dsp-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "Daisyplast: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** *Media*: per le 17 immagini importate incolla nel campo "Testo alternativo" i testi di `elementor-json/testi-alternativi-immagini.txt`.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/dsp-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas*.

**Immagini.** Le 17 immagini dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import (ID fissi: reimportando non si creano doppioni). Nei file del repository puntano a `raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Daisyplast-Sito/assets/web/`, che funziona solo quando il ramo è su GitHub con la cartella `assets/web` (1,3 MB). Per non dipendere da GitHub: carica `assets/web/` sul sito e rigenera con `--base` (vedi "Caratteri"), poi reimporta o rifai lo zip con `crea_installer.py`.

**Prima della messa online, titolo e descrizione.** WordPress non prende il titolo e la descrizione della pagina statica: senza un plugin SEO il titolo è "Daisyplast – Sacchi e film in polietilene a Tombelle di Vigonovo" (nome e motto del sito) e la descrizione manca. Con il plugin SEO del sito, sulla pagina Home: titolo **Daisyplast, sacchi e film in polietilene a Tombelle di Vigonovo**; descrizione **Daisyplast estrude film in bolla e salda sacchi, shopper, bobine e monopieghe in polietilene vergine, rigenerato e compostabile. Tombelle di Vigonovo (VE), dal 2008.** (gli stessi della statica e dell'anteprima).

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Script tolti**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, le schede non cambiano e il pulsante "Menu" non apre niente (si vede il primo materiale e la prima tappa, come nella statica senza JavaScript). Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi i widget HTML della home e della testata.
2. **Widget HTML di soli stili**: in ogni sezione c'è un contenitore nascosto con un widget HTML che contiene il foglio di stile della sezione. Se lo si cancella, la sezione perde misure, colonne e colori.
3. **Misure dai fogli di stile**: le misure fluide della statica (`clamp`) stanno nei fogli di stile e prevalgono sui valori del pannello di Elementor. Testi, link e foto si cambiano dal pannello; dimensioni e colori dei caratteri si cambiano in `_sorgente/contenuti.py`.
4. **Testata sopra l'apertura**: l'header è posato sopra la prima sezione (posizione assoluta), come nella statica. Su altre pagine future va previsto uno spazio in alto.
5. **Pannelli e tappe**: sono contenitori di Elementor con ancora `p-vergine`, `p-rigenerato`, `p-compostabile`, `tappa-1` ... `tappa-5`: le schede li trovano da quell'ancora (campo *Avanzate > ID CSS*), che non va cambiata. Nell'editor i pannelli nascosti restano sovrapposti al primo.
6. **Apostrofi**: WordPress trasforma l'apostrofo diritto in quello tipografico nei widget Testo; la statica usa quello diritto, quindi nei testi è scritto come `&#39;`. Se si riscrive un testo nell'editor, WordPress potrebbe tornare a farlo tipografico.
7. **"Questa pagina non usa cookie"** nel piede: è vero per la pagina provata (WordPress non mette cookie ai visitatori, i caratteri e le immagini arrivano dal sito), ma va ricontrollato sul sito vero dopo aver aggiunto plugin di statistiche, moduli o banner.

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `05-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file carica i propri caratteri (`@font-face` alla base delle immagini) e ha il CSS con un prefisso unico (`.dsp-home-apertura` ecc.). `02-materiali.html` e `03-percorso.html` contengono ognuno il proprio script delle schede.

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu è un elenco di link (senza Ultimate Addons), aperto dallo stesso pulsante "Menu". Immagini e caratteri puntano alla base delle immagini (vedi sopra).

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1.3 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, PHP 8.3, sul WordPress di prova `wp-daisyplast` (porta 8945, solo locale).
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide). Per far passare il controllo dei trattini lunghi, che legge tutta la cartella, le tre pagine di terzi scaricate per l'analisi (`_prova/crawl/rif/notpla.html`, `sulapac.html`, `_prova/crawl/registri/visurissima.html`) sono state compresse in `.html.gz`, con il contenuto intatto.
- Ciclo del kit (`ciclo.sh`, PAGINE="/:01-home", tre viste, HTMLTOO=1): import dei 3 template con la funzione del pulsante *Importa template*, 132 elementi salvati uguali al file, 17 immagini nella libreria, nessun riquadro grigio.
- **Confronto con la home statica**, screenshot a pagina intera a 1440x900, 1024x1366 e 390x844 (stesse altezze: 4845, 4073 e 4855 px) e differenza pixel per pixel (soglia 30 su 255, fasce da 100 px): Elementor e fallback identici alla statica. Alle altre larghezze provate (da 320 a 1920 px, compresi i punti di rottura 560/561, 767/768, 860/861, 1024/1025, 1260/1261) altezza uguale e differenze solo dentro alcune foto, ricampionate da WordPress (Elementor) o servite in una misura sola invece del `srcset` della statica (fallback). Con JavaScript spento, WordPress e statica identici a 1440 e 390. Gli screenshot finali di Elementor sono stati guardati a pezzi.
- **Interazioni** (Playwright, stesse azioni su statica, WordPress e fallback, a 1440 con il mouse, a 1024 e 390 con il tocco): clic o tocco su "Rigenerato", freccia destra (fuoco su "Compostabile"), Inizio e Fine; tocco sulla tappa 3, Fine (tappa 5), freccia dalla 5 alla 1, tappa 4; trascinamento sul palco dalla 1 alla 2 (col mouse a 1440, col dito vero, eventi touch, a 1024 e 390); altezza di materiali e percorso uguale in tutti gli stati (1074 e 996 px a 1440); a 1024 e 390 il pulsante "Menu" apre il pannello con le 4 voci e "Un ordine" lo chiude e porta a `#percorso`; a 1440 le 4 voci in riga. 44 controlli su 44 superati in tutti e tre i casi, scatti degli stati identici alla statica (tranne le foto ricampionate), nessuno scorrimento orizzontale, nessun errore in console. Ordine dei Tab uguale alla statica; clic su una voce del menu: salto immediato, come la statica (contorno del fuoco e passaggio del mouse: vedi la revisione qui sotto).
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- **Installatore** su WordPress svuotato con `nuovo-wp.sh` (contenuti, template, kit di Elementor, immagini e menu cancellati; Elementor, Ultimate Addons e gli altri plugin disattivati; tema Twenty Twenty-Five; Google Fonts di Elementor accesi), installando solo dallo zip dall'interfaccia (*Carica plugin*, *Attiva*, i 9 passi in ordine). Lo zip di prova era fatto con le immagini dal server locale: tema e plugin attivati, kit creato, 3 template importati (9, 117 e 6 elementi su 9, 117 e 6), 17 immagini nella libreria tutte con il testo alternativo, caratteri copiati sul sito, Google Fonts di Elementor spenti, Home, header, footer e menu da 4 voci creati. La home uscita: identica alla statica a 1440, 1024 e 390, interazioni 44 su 44, richieste solo al sito stesso (caratteri da `wp-content/uploads/daisyplast/fonts/`). Limite della prova: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice); lo zip in `plugin/` punta alla base su GitHub.
- Non provate: le modifiche dall'editor di Elementor.

### Revisione indipendente (19 ottobre 2026)

Rifatte da capo, con script propri, le prove sul WordPress di prova: screenshot a pagina intera di Elementor e del fallback a 1440, 1024, 768 e 390 px contro la statica (stesse altezze: 4845, 4073, 4864, 4855; differenze sopra la soglia solo dentro una foto a 768), guardati a pezzi; testo visibile, link e testi alternativi uguali alla statica; interazioni a 1440, 1200 e 560 col mouse e a 1024, 768 e 390 col tocco (44 e 45 controlli superati su statica, WordPress e fallback); stato di fuoco (tasto Tab su tutta la pagina) e di passaggio del mouse di ogni link e pulsante confrontati proprietà per proprietà con la statica a 1440, 1024 e 390.

Difetti trovati e corretti in `_sorgente/` (poi rigenerati JSON, fallback, anteprima, zip e screenshot):
1. **Linguette del percorso**: dopo un clic, un tocco o un tasto la linguetta scelta perdeva la riga gialla spessa (restava il filo di 1 px), perché le regole di fuoco di Hello Elementor e del fallback toglievano l'ombra interna che la disegna. Ora la riga resta di 3 px, come nella statica.
2. **Contorno di fuoco delle linguette**: in Elementor si vedeva intero, nella statica il palco ne copre il lato alto (il widget delle linguette era posizionato da Elementor). Ora è uguale.
3. **Pulsante "Menu"**: in WordPress aveva la transizione di 0,3 s che Hello Elementor dà a tutti i pulsanti (sottolineatura e contorno di fuoco arrivavano in ritardo). Ora il cambio è netto, come nella statica.
4. **Sotto i 560 px**: passando col mouse sul telefono della testata, su "Menu" e su "Per un preventivo" la sottolineatura non cambiava colore come nella statica; il contorno di fuoco di "Vai ai materiali" era giallo invece che grafite. Corretti.
5. **Fallback e anteprima**: avevano in testa un `preconnect` verso fonts.gstatic.com (una connessione a Google a ogni visita, anche se i caratteri vengono dal sito) e un foglio di stile vuoto. Tolti. Le voci del menu del fallback avevano una transizione di 0,2 s invece di 0,15 s: corretta.

Provati anche: la variante *Canvas* (`pagine-complete-senza-pro/dsp-01-home-completa.json` importato con la funzione di *Importa template* in una pagina con modello *Elementor Canvas*: identica alla statica a 1440, 1024 e 390, interazioni superate); i controlli di `controlla.mjs` (nessun problema); la pagina con JavaScript spento (identica alla statica a 1440 e 390); l'**installatore** da capo su WordPress svuotato con `nuovo-wp.sh` (Elementor e Ultimate Addons disattivati, tema Twenty Twenty-Five, kit di Elementor, caratteri copiati e cache cancellati, Google Fonts di Elementor accesi), caricando lo zip dall'interfaccia: tutti i passi riusciti, 9, 117 e 6 elementi su 9, 117 e 6, 17 immagini su 17 con testo alternativo, menu da 4 voci; la home uscita è identica alla statica a 1440, 1024, 768 e 390, supera le 44 prove di interazione, ha fuoco e passaggio del mouse uguali alla statica e chiede caratteri e immagini solo al sito.

Gli script della revisione sono in `_prova/wp/`: `fuoco.mjs` con `confronta-fuoco.py` (fuoco e passaggio del mouse), `interazioni-larghezze.mjs` (le prove di `interazioni.mjs` a larghezze scelte con `LARG`), `testo.mjs` (testo, link e testi alternativi), `canvas.php` (pagina di prova con la variante Canvas).

Unica differenza voluta: nel **piede** il contorno di fuoco di "049 980 2226" e della PEC è giallo, mentre nella statica è grafite su fondo quasi nero, cioè quasi invisibile (la nota di progetto chiede "il fuoco è visibile"). Se si vuole la statica identica anche qui, basta aggiungerle `.piede :focus-visible{outline-color:var(--giallo)}`.

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i "Dati da confermare con l'azienda" qui sotto. In più:
1. **Base delle immagini e dei caratteri**: o il ramo GitHub pubblicato con `Daisyplast-Sito/assets/web`, o `assets/web/` caricata sul sito e i file rigenerati con `--base`, prima dell'import (con l'installatore i caratteri vanno sul sito da soli, le immagini no).
2. **Titolo e descrizione** della Home da impostare con il plugin SEO (vedi "Prima della messa online").
3. **Privacy e cookie**: la frase "Questa pagina non usa cookie" del piede va riverificata sul sito vero (punto 10 qui sotto).

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (collegamenti, nessuna copia in più)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/daisyplast-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini e i caratteri), `--url-sito URL` (link interni assoluti), `--out CARTELLA`. Il build si ferma se trova un trattino lungo, una parola da evitare, un valore di stile non valido, un'immagine senza testo alternativo o un link dentro un blocco già cliccabile.

## La home statica

Proposta non richiesta di nuova homepage (solo la home) per DAISYPLAST s.r.l., Tombelle di Vigonovo.

- **Home finale**: `sito/index.html`, con `sito/img/` e `sito/fonts/`. Si apre con file:///, senza server.
- **Nota di progetto**: `screenshot/home/NOTA.md` (idea, prime due schermate, caratteri, colori, interazione, foto, controlli).
- **Screenshot**: `screenshot/home/home-1440.jpg`, `home-1440-prima-schermata.jpg`, `home-390.jpg`, `home-390-prima-schermata.jpg`.
- **Rifare tutto**: `bash _prova/script/build_finale.sh` (immagini, pagina, screenshot e prove dell'interazione). I PNG di controllo finiscono in `_prova/scatti/` e vanno cancellati dopo averli guardati. Verifiche finali: `node _prova/script/finale_verifica.mjs <percorso di sito/index.html>` e `python3 -I _prova/script/finale_misure.py sito/img`.
- **Fonti dei fatti**: `01-analisi.md`. Prototipi scartati e giudizio: `_prova/home/a` (base della finale) e `_prova/home/b` (da cui vengono il giallo, la margherita e il palco del percorso).

## Dati da confermare con l'azienda

In pagina c'è solo ciò che ha una fonte in `01-analisi.md`. Restano da chiedere:

1. **Foto 015**: che sia del loro reparto. Regge l'apertura (la bolla) e la tappa 2 (il quadro comandi della stessa linea), e ha la sola didascalia della pagina ("una testa di estrusione: il film sale dall'anello di raffreddamento verso i rulli di traino").
2. **Foto 001, 002, 005** del sito: sembrano di repertorio (forse fornite da Italiaonline con il sito). Va chiesto se si possono riusare e con quale licenza.
3. **Certificazione del compostabile**: quale (OK compost, DIN CERTCO, CIC o altra), su quali prodotti, con quale materia prima. Il sito scrive "UNI 13432"; la norma giusta è UNI EN 13432, ma in pagina non c'è nessuna norma finché la certificazione non è confermata: il cartellino dice solo "Biodegradabile e compostabile".
4. **Email attiva**: in pagina c'è info@daisyplast.it (piede del sito); nei Contatti del sito compaiono anche info@daisyplast.191.it e commerciale@daisyplast.191.it. Va chiesto anche se il fax 049 982 9961 si usa ancora.
5. **PEC** daisyplastsrl@pec.it: viene dai registri (visurissima.it, aziende.it), non dal sito.
6. **"Siamo in tredici, dal 2008"** (tappa 3): dal Registro Imprese, 13 dipendenti nel 2024 e inizio attività l'11/08/2008. Va chiesto se il numero è ancora quello.
7. **Consegne e area**: in pagina solo "con i nostri mezzi", come dice il sito. Mancano area servita e numero dei mezzi. Nella prima schermata "per grossisti del Triveneto" viene dal titolo della pagina /daisyplast del loro sito; va chiesto se il Triveneto vale anche per industrie e artigiani.
8. **Logo in vettoriale**: esiste solo il PNG da 530x146 px del sito; in pagina è usato nei suoi colori, in piccolo.
9. Non in pagina, da chiedere per il sito vero: stampa di loghi sulle shopper, clienti citabili del distretto calzaturiero, storia prima del 2008, che cosa sia il "Progetto Shopper 4 piste" (OpenCoesione).
10. **Privacy e cookie**: nel piede c'è solo "Questa pagina non usa cookie" (vero per questa proposta statica: niente statistiche, caratteri serviti in locale). Per il sito vero l'informativa va scritta con l'azienda e collegata dal piede.

## Foto da rifare dal vero

Mezza giornata di servizio fotografico nel capannone di via del Lavoro, luce naturale o luce continua morbida, niente flash diretto, file RAW. La pagina è già pensata per queste inquadrature:

1. **La bolla in controluce, in verticale** (sostituisce la 015 in apertura): macchina bassa all'altezza dell'anello di raffreddamento, obiettivo 35 mm, la bolla che sale fino al bordo alto del fotogramma, l'anello pulito e intero in basso, fondo del capannone il più scuro possibile; una luce dietro la bolla per farla brillare. Servono almeno 1600x3000 px.
2. **Il quadro comandi della stessa linea**, in verticale, display accesi, la nota a penna leggibile, con lo spazio del reparto a sinistra (tappa 2 "Il piano").
3. **I tre film presi dalle loro bobine**, still life su fondo nero, in orizzontale 2:1 con il soggetto a sinistra e spazio a destra per il cartellino: il vergine trasparente in luce radente, il nero rigenerato lucido, il compostabile bianco latte opaco (selettore). La margherita del compostabile può restare, ma meglio rifarla con una loro shopper compostabile accanto.
4. **La saldatura**: il bordo saldato con la perforazione a strappo, in macro e in luce radente. Oggi la tappa 4 è solo tipografica (2, 1, 1); con questa foto il palco può tornare fotografico.
5. **Le bobine a fine linea**: una loro bobina appena avvolta sul mandrino, di lato (tappa 3, oggi la 001 di repertorio).
6. **La bobina vista in asse**, una loro, su fondo scuro, taglio stretto sugli strati (tappa 1).
7. **La consegna**: i loro bancali di prodotto finito pronti al carico e un loro mezzo, senza marchi di terzi in vista (tappa 5).
8. Le foto Unsplash in pagina (sacchetto con la mela, film nero, margherita) sono segnaposto e vanno sostituite.

## Licenze

- **Caratteri**: Sofia Sans e Sofia Sans Extra Condensed, Google Fonts, SIL Open Font License 1.1; testo della licenza in `sito/fonts/OFL.txt`. Uso commerciale libero.
- **Foto Unsplash in pagina**: tJ-SrdvRF20 (Yosafat Herdian), mFcsYcSSiMQ (Compagnons), kFK54FCIB3U (Daniele Levis Pelusi), tutte "Free to use under the Unsplash License", verificata sulla pagina di ogni foto il 19 ottobre 2026 (dettaglio in `assets/CREDITI.md`). Uso commerciale libero, attribuzione non obbligatoria.
- **Foto del sito daisyplast.it** (015, 005, 001, 002) e **logo**: di Daisyplast o del fornitore del sito; diritti da chiarire (punti 1, 2 e 8 sopra).
- Nessuna immagine generata dall'IA.

## Loghi

Il logo è usato com'è (margherita bianca, cuore giallo, scritta verde DAISYPLAST a contorno), dal PNG del sito convertito in WebP senza perdita. Nessun logo di terzi in pagina: i bancali con il marchio di un produttore di resina sono stati tolti.

## Righe "da guardare" dei segnali, con la ragione

- **5 fasce di fondo**: latte e grafite si alternano a blocchi d'altezza diversa (apertura e materiali su latte, percorso su grafite, clienti su latte, contatti su grafite, piede), con le foto in mezzo. È la struttura della pagina, non una serie di fasce colorate con colonne.

## Revisione cieca dell'ultimo passaggio

Voto di partenza K0 7, 59/80. Cosa è cambiato, con le misure, e cosa è stato respinto: `screenshot/home/NOTA.md`, sezione "Cosa è cambiato con la revisione cieca".
