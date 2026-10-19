# Tek.Lam S.r.l., proposta di nuova home

Proposta non richiesta: solo la home, da mostrare all'azienda. Non è pubblicata e l'azienda non è stata contattata.

- `01-analisi.md`: azienda, sito di oggi, fatti con le fonti, materiale visivo, direzioni artistiche, riferimenti.
- `sito/`: la home finale, "Scintilla e spessore" (`index.html`, `img/`, `fonts/`). Si apre con file:///. Viene dal prototipo B e sostituisce la versione "Il foglio annidato", bocciata.
- `screenshot/home/`: home intera e prima schermata a 1440 e a 390, più `NOTA.md` (idea, prime due schermate, caratteri, colori, interazione, foto, controlli).
- `assets/originali/`: le immagini del sito teklam.it. `assets/esterne/`: foto Unsplash e Pexels scaricate come segnaposto, licenze in `assets/CREDITI.md`. `assets/web/` contiene le immagini e il carattere della home finale per la versione WordPress (vedi sotto).
- Versione WordPress della home: `elementor-json/`, `html-fallback/`, `anteprima/`, `plugin/teklam-installer.zip`, `screenshot/elementor/`, `screenshot/fallback/`, `_sorgente/` (vedi "Versione WordPress della home").
- `_prova/`: lavoro di servizio (crawl, riferimenti, prototipi A e B in `_prova/home/`, script). `bash _prova/script/build_finale.sh` rifà immagini, carattere, pagina, controlli (anche menu, righe del percorso e larghezze da 320 a 2560 con `rifinitura_prova.mjs`) e screenshot; gli script della versione bocciata sono in `_prova/script/vecchio-foglio/`.

## Versione WordPress della home (come per Benvegnù)

La home finale ("Scintilla e spessore", `sito/index.html`, versione del 19 ottobre alle 19:24) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina: a 1440, 1024 e 390 px lo screenshot di WordPress e quello del fallback hanno la stessa altezza della statica (4749, 5310 e 5145 px) e coincidono pixel per pixel, tranne le foto, che WordPress ricampiona dalle misure della sua libreria media (vedi "Collaudo fatto"). Le interazioni sono le stesse: interruttore Ferro, Inox, Alluminio con clic, tocco e tastiera; menu del telefono che si apre dal bottone "Menu", si chiude con Esc o toccando una voce, e sotto 380 px porta anche il telefono.

La prima versione WordPress era stata fatta per la home "Il foglio annidato", bocciata e sostituita in `sito/` durante il lavoro: i suoi sorgenti sono in `_prova/wp-vecchio-foglio/` (non servono più).

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `tkl-00-header.json` e `tkl-99-footer.json` (tipo *sezione*), `tkl-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `tkl-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 5 immagini della libreria media (Elementor li perde all'import; l'installatore li scrive da solo) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `06-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/teklam-installer.zip` | plugin che installa e configura la home su un WordPress pulito (vedi "Installazione automatica") |
| `assets/web/` | le immagini della statica, gli stessi file di `sito/img/` (apertura in quattro larghezze e verticale, saldatura, fondo dei contatti, segno e scritta del marchio), più il carattere con la licenza (`fonts/`) |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova e dall'anteprima HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi e sezioni), `motore.py` e `build.py` (quelli di Benvegnù, prefisso `tkl`, con l'opzione dei caratteri dal sito come in Paraga Pelli), `prepara_immagini.py`, `crea_installer.py`, `installer/` |

Come è fatta la pagina in Elementor (100 elementi nella home, 9 nell'header, 8 nel footer):
- **Widget nativi, modificabili dal cliente**: titoli (h1 "Lamiera conto terzi", h2, h3), testi (anno, riga sotto l'apertura, testo dello spessore, i sette passi del percorso con numero, macchina e misura, settori e note, storia, persone, invito, recapiti), le foto (apertura larga e verticale, saldatura) nella libreria media con il loro testo alternativo, il telefono grande; nella testata segno e scritta del marchio, il menu (widget "Navigation Menu" di Ultimate Addons) e il telefono; nel piede marchio, ragione sociale, P.IVA e link.
- **Widget HTML**, solo dove Elementor gratuito non arriva: l'interruttore Ferro, Inox, Alluminio e la figura con la lettura, la legenda, la scala in millimetri, le guide e la sezione tratteggiata, con lo script della pagina statica (markup e script sono letti da `sito/index.html` a ogni `build.py`, quindi restano uguali alla statica); il fondo dei contatti, decorativo e senza testo alternativo come nella statica. Altri widget HTML contengono solo il foglio di stile della loro sezione (la griglia a 12 colonne e le misure fluide della statica, con le classi `tkl-`): non vanno cancellati. Uno script nella sezione dei contatti raccoglie le sezioni in un `<main>`, come nella statica (nell'editor non fa niente).
- Il menu di Ultimate Addons è tenuto uguale alla statica: in riga fino a 821 px (Ultimate Addons passerebbe al menu a scomparsa a 1024), sotto il bottone "Menu" scritto al posto dell'icona, pannello sotto la testata con le voci da 22 px; un piccolo script nella testata fa saltare subito alle ancore (Ultimate Addons farebbe scorrere la pagina in 800 ms), chiude il pannello con Esc, fa aprire e chiudere il pannello con Invio e con Spazio lasciando il fuoco sul bottone (Ultimate Addons con Spazio faceva scorrere la pagina e con Invio spostava il fuoco sulla prima voce) e dà al bottone il nome accessibile "Menu", come nella statica.

### Vedere il sito subito

Senza installare niente: doppio clic su `Teklam-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `Teklam-Sito` e http://localhost:8000/anteprima/). Le immagini vengono da `assets/web`, quindi funziona anche senza internet; il carattere arriva da Google Fonts. È il Formato B: a vista uguale alla versione Elementor; il menu del telefono è un elenco a scomparsa (`<details>`) senza Ultimate Addons, che si comporta come quello della statica.

### Installazione automatica su un WordPress pulito

`plugin/teklam-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Tek.Lam*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto e si può ripetere. L'import scrive anche i testi alternativi delle immagini nella libreria media; la verifica dice quante li hanno.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online togli la spunta in *Impostazioni > Lettura*. Se lo zip è fatto con il carattere servito dal sito (vedi "Carattere"), lo stesso passo spegne anche i Google Fonts di Elementor. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" | **sì**: il menu dell'header è un suo widget |

Contact Form 7 non serve: la home non ha moduli (il preventivo si chiede per email o al telefono, come nella statica).

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

**Carattere.** Sofia Sans, lo stesso file woff2 della statica (`sofia-latin.woff2` ha lo stesso md5 del file latin di Google Fonts). Due modi:
- **Da Google Fonts** (così sono fatti i file consegnati): `https://fonts.googleapis.com/css2?family=Sofia+Sans:wght@1..1000&display=swap`, caricato dal widget HTML della testata e dell'apertura e dal fallback. Elementor in più chiama Google da sé per Roboto e Roboto Slab (i caratteri predefiniti del kit) e per Sofia Sans (la tipografia dei widget).
- **Dal sito, senza nessuna chiamata a Google (GDPR):** carica `assets/web/` sul sito (`fonts/` è dentro) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/teklam/ --caratteri-locali`: i widget HTML e il fallback hanno allora le stesse `@font-face` della statica, verso `fonts/sofia-latin.woff2` e `fonts/sofia-latin-ext.woff2`. Poi spegni i Google Fonts di Elementor: *Elementor > Impostazioni > Avanzate > Google Fonts: Disattiva* (opzione `elementor_google_font` = 0); con lo zip rifatto da `crea_installer.py` dopo quella build, l'installatore lo fa da solo. Provato nel WordPress di prova, anche sulla home attuale (revisione del 19 ottobre): nessuna richiesta a host esterni, Sofia Sans caricata dal sito, pagina identica alla statica a 1440 e 390.
Licenza OFL in `assets/web/fonts/OFL-SofiaSans.txt`.

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie gli script dai widget HTML e l'interruttore degli spessori non risponde.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le immagini arrivano durante l'import.
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**.

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu Tek.Lam** (slug `menu-tek-lam`) con queste voci, tutte "Link personalizzati": Lavorazioni `/#percorso`, Settori `/#settori`, Famiglia Volpato `/#famiglia`, Contatti `/#contatti` e, ultima, `049&nbsp;980&nbsp;14&nbsp;86` con URL `tel:+390499801486` (si vede solo nel menu a scomparsa sotto 380 px). Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `tkl-00-header.json` e `tkl-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Tek.Lam: Header", salva. Lo stesso per il footer ("Tek.Lam: Footer").
**3. La home.** Importa `tkl-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "Tek.Lam: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** *Media*: per le immagini importate incolla nel campo "Testo alternativo" i testi di `elementor-json/testi-alternativi-immagini.txt`.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/tkl-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas* (provata nel WordPress di prova sulla home attuale, modello Canvas: 117 elementi su 117, identica alla statica a 1440 e 390 come la versione con header globale).

**Immagini.** Le foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import (ID fissi: reimportando non si creano doppioni). Il fondo dei contatti invece sta in un widget HTML e resta all'indirizzo della base delle immagini: oggi `raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Teklam-Sito/assets/web/`, che funziona solo quando il ramo è su GitHub con la cartella `assets/web` (anche l'import delle foto parte da lì). Per la messa online: carica `assets/web/` sul sito (per esempio in `wp-content/uploads/teklam/`, 1,9 MB) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/teklam/` (più `--caratteri-locali`, se si vuole il carattere dal sito), poi reimporta (o rifai lo zip con `crea_installer.py`).

**Prima della messa online, titolo e descrizione.** WordPress non prende il titolo e la descrizione della pagina statica: con il plugin SEO del sito (per esempio Yoast o Rank Math), sulla pagina Home: titolo **Tek.Lam, lamiera conto terzi a Vigonovo**; descrizione **Carpenteria in lamiera conto terzi a Tombelle di Vigonovo (VE): progettazione 3D, taglio laser, punzonatura, piegatura CNC, saldatura, tubi e profili. La famiglia Volpato dal 1978.** (gli stessi della statica e dell'anteprima).

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Script tolti**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, l'interruttore degli spessori resta fermo su Ferro. Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi i widget HTML della home e della testata.
2. **Widget HTML di soli stili**: in ogni sezione c'è un widget HTML che sembra vuoto nell'editor e contiene il foglio di stile della sezione. Se lo si cancella, la sezione perde la griglia e le misure.
3. **Misure dai fogli di stile**: le misure fluide della statica (titoli e margini con `clamp`) stanno nei fogli di stile dei widget HTML e prevalgono sui valori del pannello di Elementor. Testi, link e foto si cambiano dal pannello; dimensioni e colori dei caratteri si cambiano in `_sorgente/contenuti.py`.
4. **Testata sopra la foto**: l'header è posato sopra l'apertura (posizione assoluta), come nella statica. Su altre pagine future va previsto uno spazio in alto o una testata diversa.
5. **Apostrofi**: WordPress trasforma l'apostrofo diritto in quello tipografico nei widget Testo; nei testi è scritto come `&#39;`, che resta diritto come nella statica. Se si riscrive un testo nell'editor, WordPress potrebbe tornare a farlo tipografico.
6. **Variabile `--gap`**: nella statica la spaziatura della griglia si chiama `--gap`, che in Elementor è una variabile dei contenitori; nei fogli di stile si chiama `--intervallo`.

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `06-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file carica il proprio carattere e ha il CSS con un prefisso unico (`.tkl-home-apertura` ecc.). `02-spessore.html` contiene lo script dell'interruttore; `00-header/01-header.html` lo script che chiude il menu del telefono.

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu del telefono è un `<details>` senza Ultimate Addons (a vista e nel comportamento uguale alla statica). Le immagini puntano alla base delle immagini (vedi sopra).

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, sul WordPress di prova `wp-teklam` (porta 8944, solo locale), contro `sito/index.html` delle 19:24.
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide).
- Ciclo del kit (`ciclo.sh`, PAGINE="/:01-home", tre viste, HTMLTOO=1): import dei 3 template, 117 elementi salvati uguali al file, immagini nella libreria, nessun riquadro grigio.
- **Confronto con la statica**, screenshot a pagina intera e differenza pixel per pixel: a 1440x900, 1024x1366 e 390x844 Elementor e fallback hanno la stessa altezza della statica e differiscono solo nelle foto (apertura e saldatura), che WordPress serve dalle misure ridotte della sua libreria (il fallback dal file più grande, ridotto dal browser). Stesse altezze anche a 320, 360, 380, 381, 640, 641, 768, 820, 821, 1024, 1100, 1101, 1240, 1241, 1280 e 1920 px, senza scorrimento orizzontale; fuori dalle foto restano differenze di mezzo pixel (righe che scendono di un pixel per arrotondamento). Testi visibili uguali parola per parola (427 parole).
- **Interazioni** (Playwright, stesse azioni sulla statica, su WordPress e sul fallback, a 1440 e 1024 col mouse, a 820, 390 e 360 col tocco): Inox con clic o tocco (15 mm, sezione 57 px), freccia destra (Alluminio 10 mm, 38 px), Home (Ferro 20 mm, 76 px), Fine, fuoco sul bottone scelto; menu: bottone "Menu" nella stessa posizione, pannello con le stesse voci (sotto 380 px anche il telefono) alla stessa altezza, Esc lo chiude, una voce lo chiude e porta subito a `#settori` alla stessa altezza di scorrimento. Passaggio del mouse e fuoco di tutti i link e bottoni confrontati a 1440 e 390: uguali (a meno di mezzo pixel). Nessun errore in console (la statica aperta da file:// segnala solo il preload del carattere bloccato dal CORS).
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- Caratteri dal sito (`--caratteri-locali`, Google Fonts di Elementor spenti): nessuna richiesta a Google, pagina identica (provato con la versione precedente della home, stesso meccanismo).
- **Installatore** su WordPress svuotato (contenuti, template, kit di Elementor, immagini e menu cancellati; Elementor e Ultimate Addons disattivati, tema Twenty Twenty-Five), installando solo dallo zip dall'interfaccia (*Carica plugin*, *Attiva*, i 9 passi in ordine). Zip di prova fatto con le immagini dal server locale: tema e plugin attivati, 3 template importati (9, 100 e 8 elementi su 9, 100 e 8), 5 immagini nella libreria tutte con il testo alternativo, Home, header, footer e menu da 5 voci creati. La home uscita: identica alla statica come nel ciclo (solo le foto ricampionate), interruttore e menu uguali, testi uguali. Limite: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice); lo zip in `plugin/` punta alla base su GitHub e a Google Fonts.
- Gli screenshot finali di Elementor (1440, 1024, 390) sono stati guardati a pezzi. Non provate: le modifiche dall'editor di Elementor.

**Revisione indipendente (19 ottobre 2026, sera)**, fatta da chi non ha costruito la versione WordPress, contro `sito/index.html` delle 19:24:
- Screenshot a pagina intera di statica, Elementor e fallback a 1440x900, 1024x1366, 768x1024 e 390x844, con differenza pixel per pixel: stesse altezze (4749, 5310, 4919, 5145 px). In Elementor le sole differenze sono nelle foto ricampionate da WordPress e, a 768, una riga di testo spostata di 0,2 px sotto la foto della saldatura (WordPress usa le proporzioni del file da 1330, la statica a quella larghezza quello da 960). Gli screenshot di Elementor e del fallback guardati a pezzi a tutte e quattro le larghezze.
- **Corretto, fallback:** fra 821 e 1240 px il testo accanto a "Il percorso del pezzo" partiva 10 px più a sinistra che nella statica (a 1024: x 590 invece di 600). Il motore scrive nel fallback `gap:0` per ogni contenitore con la stessa specificità delle regole della griglia, che perdevano lo spazio fra le colonne; ora `column-gap` della griglia del capo e del testo dello spessore ha `!important`. Dopo la correzione la posizione coincide con la statica a 821, 900, 1024, 1100 e 1240 px.
- **Corretto, menu del telefono in WordPress:** con Spazio il bottone "Menu" di Ultimate Addons non apriva il pannello e la pagina scorreva di uno schermo; con Invio il fuoco passava alla prima voce (nella statica resta sul bottone); il nome accessibile era "Attivazione del menu". Ora Invio e Spazio aprono e chiudono come nella statica, il fuoco resta sul bottone, Tab entra nelle voci, Esc chiude e torna al bottone; il nome è "Menu".
- **Corretto, fallback:** lo script del menu del motore segnava `aria-current="page"` su tutte e quattro le voci (sono ancore della stessa pagina); ora nessuna.
- **Corretto, installatore:** il passo "impostazioni" scriveva come descrizione del sito una frase non presente nella statica; ora è "Lamiera conto terzi a Vigonovo", dal titolo della statica.
- Interazioni ripetute dopo le correzioni sulla statica, su WordPress e sul fallback con gli stessi risultati: interruttore con clic (1440, 1024), tocco (820, 390, 360), frecce, Home e Fine (15 mm e 56,7 px, 10 mm e 37,8 px, 20 mm e 75,6 px, `aria-checked` e `tabindex` uguali); menu a 820, 390 e 360 col tocco e a 768 con la tastiera (posizione e misura del bottone, voci del pannello alla stessa altezza, telefono nel pannello a 360, Esc, una voce porta a `#settori` alla stessa altezza di scorrimento). Testo visibile, titoli e link uguali alla statica; nessun errore in console.
- Import: `ciclo.sh` 117 elementi su 117, nessun segnaposto; `controlla.mjs` a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema.
- Installatore rifatto dalla build corretta (con le immagini dal server locale) e provato su WordPress svuotato (contenuti, kit di Elementor e menu cancellati, Elementor e Ultimate Addons disattivati, tema Twenty Twenty-Five): caricato e attivato dall'interfaccia, 9 passi senza errori, 3 template (9, 100 e 8 elementi su 9, 100 e 8), 5 immagini tutte con il testo alternativo, menu da 5 voci; la home uscita coincide con quella del ciclo a 1440, 1024, 768 e 390 e ha le stesse interazioni.
- Nessun trattino lungo (U+2014) nei file consegnati, nei sorgenti e nello zip; nessun dato che non sia nella statica.
- Restano, non correggibili senza toccare la logica del motore o di Ultimate Addons: in WordPress la testata e il piede del sito sono un `<header>` e un `<footer>` dentro quelli di Ultimate Addons (come in Benvegnù); il link del marchio ha come nome i testi alternativi delle due immagini ("Segno del marchio Tek.Lam Tek.Lam"), nella statica "Tek.Lam, inizio pagina"; il bottone del menu è un `div` con `role="button"`. A vista e nel comportamento non cambia niente.

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i punti di "Da confermare con Tek.Lam" qui sopra (prima di tutto gli spessori: in WordPress stanno nel widget HTML dell'interruttore, che `build.py` riprende da `sito/index.html`). In più:
1. **Base delle immagini**: `assets/web/` va caricata sul sito (o il ramo GitHub pubblicato) prima dell'import; vedi "Immagini".
2. **Google Fonts**: va bene caricare Sofia Sans da Google o si vuole dal sito (GDPR)? Vedi "Carattere".
3. **Privacy e Cookie** puntano alle pagine di oggi su teklam.it anche in WordPress, finché non esistono le nuove.
4. **Titolo e descrizione** della Home da impostare con il plugin SEO (vedi "Prima della messa online").
5. Se la statica cambia ancora, va rifatto il giro: `build.py` riprende da sola l'interruttore e la figura, ma testi, misure e stili delle altre sezioni sono scritti in `_sorgente/contenuti.py`.

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (stessi file, solo quelli usati)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/teklam-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini e, con l'opzione seguente, il carattere), `--caratteri-locali` (carattere da `fonts/` alla base delle immagini invece che da Google), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.

## L'idea in una riga

L'officina di notte: la scintilla del laser su nero pieno, poi lo spessore che quel laser taglia disegnato in millimetri veri, con l'interruttore Ferro, Inox, Alluminio; il percorso del pezzo dal file al camion in sette righe, ognuna con lavorazione, macchina e misura.

## Da confermare con Tek.Lam prima di pubblicare

1. **Spessori massimi del laser, bloccante: non pubblicare senza la conferma scritta di Tek.Lam.** In pagina (interruttore e sezione disegnata in millimetri) ci sono quelli della home del loro sito, 20 mm ferro, 15 inox, 10 alluminio ("spessore max di taglio 20mm di ferro, 15mm inox, 10mm alluminio"). La pagina Attrezzature dice 25 (fe), 15/20 (inox) e 12 (alluminio). Il gesto della pagina si regge su questo dato. Per cambiarlo: `data-t` dei tre bottoni, le tre quote della legenda e delle guide in `_prova/script/finale_pagina.html`, e il controllo in `controlla_finale.py`.
2. Piegatrici: in pagina "Finn-Power 8 assi e Warcom, lunghezza utile 3100 mm". Le portate non coincidono (home "3100x100 T e 3100x125 T", Attrezzature "3100×120 t" e "3100×100 t") e non sono in pagina. La Trumpf TrumaBend V170 della foto caricata nel 2024 è in officina? Se sì, la riga 04 va aggiornata.
3. Riga 06, tubi e profili: in pagina "OMES, Ercolina, Pedrazzoli, curvatura 20 × 20 × 3" (dalla frase "quadro vuoto 20x20x3": è la sezione massima curvabile?). Troncatrice OMES "fino a 120 mm": diametro o lato? Non in pagina.
4. Riga 07: "Due autocarri propri, centinato da 50 q, con gru" (Attrezzature: "Autocarro centinato con 50 qli di portata utile", "Autocarro con gru da 35 qli complessivi"). Sono ancora due? I 35 quintali sono portata o massa?
5. Riga 03: "Finn-Power SG6, pezzo separato e impilato" riassume "completa di automazione di carico/scarico impilaggio e separazione". La cesoia Gasparini ("fino a mm 3000 di lungh. x sp. 6 8") non è più in pagina.
6. Verniciatura, cromatura, sabbiatura e zincatura: in pagina "le seguiamo noi su impianti esterni collegati", dalla pagina Attrezzature. Ancora vero?
7. La storia: in pagina "La famiglia Volpato lavora il metallo dal 1978: prima piccoli manufatti in ferro battuto come FDS Volpato S.n.c., dal 2020 lamiera come Tek.Lam S.r.l." Il sito dice "l'esperienza dei fondatori, dal 1978", "carpenteria di piccoli manufatti in ferro battuto" e il passaggio del testimone nel blog del 16/09/2020. Confermare anno, forma e data.
8. Settori e note: dalle schede Realizzazioni del 2020. Ancora attuali? Lavorano anche per la moda o la pelletteria del distretto? Non scritto.
9. Indirizzo: "Via del Lavoro, 68" (contatti) o "Viale del Lavoro, 68" (privacy). In pagina c'è Via. PEC e data di costituzione per il piede.
10. Sandro e Dimitri Volpato: in pagina con nome, ruolo ed email, come nella loro pagina Chi siamo. Va bene che restino in home?
11. Certificazioni, numero di macchine, superficie dell'officina, clienti citabili, un lavoro con nome e anno: oggi non ci sono. Un lavoro con nome e anno sarebbe il contenuto più forte da aggiungere.
12. Dati Atoka (8 dipendenti, 1,0 milioni di ricavi): non usati senza consenso.
13. Uso della loro foto `2020-08-slide1.jpg` (sezione Famiglia) e consenso del saldatore ritratto.
14. Link: Privacy e Cookie puntano alle pagine di oggi su teklam.it, da rifare con il nuovo sito.

## Foto da rifare dal vero

In pagina ci sono due foto di repertorio con la dicitura "Foto indicativa" (apertura e fondo dei contatti) e una loro foto, un fotogramma da telefono di 1330 px allargato a tutta la finestra (sopra i 1440 px si vede morbida). La fascia della piegatrice sopra il percorso è uscita. Mezza giornata di fotografo in officina, di sera o a portoni chiusi, luce della macchina più una lampada calda radente, file da almeno 3000 px di lato lungo:

1. **L'apertura**: il loro Byspeed che taglia ferro spesso, ripreso basso al livello della lamiera, ugello al centro, scintille ai due lati, sotto almeno un terzo di buio per il titolo; tempo breve (1/250 o meno) per le scie nitide, f/4. Più una versione verticale 4:5 per il telefono, stretta sull'ugello. Con la foto vera la dicitura "Foto indicativa" sparisce dalla prima schermata.
2. **La famiglia**: la saldatura TIG sul cassone col film blu, stessa scena di `slide1` a piena risoluzione e in orizzontale largo (almeno 2,4:1 di ritaglio, perché va a tutta larghezza), e Sandro e Dimitri Volpato in officina al lavoro, non in posa.
3. **I contatti**: l'ugello del loro laser sul piano a punte, fermo, macchina spenta, luce radente; deve reggere scurito al 60 % sotto il testo, con la parte bassa calma (lì ci sono i recapiti).
4. Facoltativa: il bordo vero di una lamiera da 20 mm appena tagliata, in macro con luce radente, per affiancare la sezione disegnata.

## Caratteri e licenze

- Sofia Sans (Google Fonts), SIL Open Font License 1.1: uso commerciale libero, file serviti dalla pagina in `sito/fonts/`, licenza in `sito/fonts/OFL-SofiaSans.txt`. Nessun altro carattere.
- Foto di repertorio: Le Trung e Cemrecan Yurtman (una foto), Unsplash License; URL, autori e note in `assets/CREDITI.md`. Nessuna immagine generata dall'IA.

## Loghi

Il segno e la scritta in testata e nel piede sono ritagliati dal PNG verticale del loro sito (`2020-07-logo-TEKLAM.png`, 1772 px). Serve il logo vettoriale (SVG o PDF) da Tek.Lam per la versione definitiva e per confermare il rosso.

## Prototipi

`_prova/home/a/` ("Il foglio annidato") e `_prova/home/b/` ("Scintilla e spessore", scelto), ognuno con la sua `nota.md`. La prima schermata (scintille, "Lamiera conto terzi", "1978") resta com'è per scelta del committente, anche dopo il giudizio cieco che chiedeva di portarci lo spessore. Dal B la home finale tiene prima schermata, spessore e palette; il percorso del pezzo è rifatto da capo due volte (l'ultima: senza fascia fotografica, sette righe da 54 px, 573 px in tutto a 1440) e la pagina è passata da 9841 a 4749 px a 1440.
