# F.M. Sistemi: proposta di nuova home

Proposta non richiesta, solo la home. Versione finale in `sito/` (`index.html`, `img/`, `fonts/`), nota di progetto in `screenshot/home/NOTA.md`, screenshot in `screenshot/home/`. Ultimo passaggio (19 ottobre 2026): palette chiara (calce, grafite, rame; blu FM solo nel logo e nel fuoco), stessa idea e stessi testi; la versione scura è in `_prova/home/finale-scuro/`. **Da rigenerare (20 ottobre 2026):** dopo la palette chiara è cambiata due volte la chiusura della home statica (contatti e piede). Ora è nello stile B "con foto", scelto dal committente: a sinistra la frase "Qui il cantiere ha un numero solo, e i mestieri arrivano nell'ordine in cui servono." e sotto i recapiti in poche righe (telefono 40 px, email, indirizzo con Google Maps, orari), a destra una foto sola, la metà bassa del collettore (Pavel Danilyuk, Pexels 7937309, `sito/img/chiusa-*.jpg`); il piede è una riga sola sulla calce sotto un filetto (vedi `screenshot/home/NOTA.md`). La versione WordPress qui sotto ha ancora la chiusura di prima della palette (titolo di luogo, numero grande, tre colonne, piede su pietra): `_sorgente/contenuti.py` (contatti e footer) e `_sorgente/prepara_immagini.py` (la foto `chiusa`) vanno aggiornati e vanno rigenerati `assets/web/`, `elementor-json/`, `html-fallback/`, `anteprima/`, lo zip in `plugin/` e gli screenshot di Elementor e del fallback; il confronto pixel per pixel descritto sotto vale per la home di prima. La versione WordPress (`_sorgente/`, `elementor-json/`, `html-fallback/`, `anteprima/`, `plugin/`, `screenshot/elementor/`, `screenshot/fallback/`) è rifatta su questa palette chiara: vedi "Versione WordPress della home". Si rifà tutto con `bash _prova/script/build_finale.sh`. Analisi e fonti in `01-analisi.md`; prototipi in `_prova/home/a` e `_prova/home/b`.

## Versione WordPress della home (come per Benvegnù)

La home (palette chiara, `sito/index.html`) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina: a 1440, 1024 e 390 px (e a 320, 360, 600, 601, 768, 860, 861, 900, 1100, 1101, 1280 e 1920) lo screenshot di WordPress ha la stessa altezza della home statica e coincide pixel per pixel tranne dentro le foto, che WordPress ricampiona dalle misure della sua libreria media (vedi "Collaudo fatto"). Le interazioni sono le stesse: le otto lettere accese dell'alfabeto portano alla riga del loro mestiere, con clic, tocco, Tab e Invio, e la capolettera della riga raggiunta riceve il segno di rame (`:target`); passaggio del mouse su lettere, link e bottone come nella statica.

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `fms-00-header.json` e `fms-99-footer.json` (tipo *sezione*), `fms-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `fms-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 21 immagini della libreria media (Elementor li perde all'import; l'installatore li scrive da solo) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `05-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/fmsistemi-installer.zip` | plugin che installa e configura la home su un WordPress pulito (vedi "Installazione automatica") |
| `assets/web/` | quello che serve al sito (3 MB): il raccordo a T dell'apertura nelle cinque misure della statica, le otto strisce dei mestieri, collettore e parete d'inverno (versione per computer e taglio del telefono), logo, favicon, i due caratteri woff2 con la licenza (`fonts/`) |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova (installata con lo zip) e dall'anteprima HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi, sezioni e fogli di stile della statica), `motore.py` e `build.py` (quelli di Benvegnù, prefisso `fms`), `prepara_immagini.py`, `crea_installer.py`, `installer/` |

Come è fatta la pagina in Elementor:
- **Widget nativi, modificabili dal cliente** (138 elementi nella home: 46 contenitori, 15 titoli, 50 testi, 1 bottone, 20 immagini e 6 widget HTML): titolo "Dalla A alla Z" (h1), la riga sotto il titolo, la didascalia della T, il bottone "Telefonate allo 049 8305354" e "o scrivete", il titolo e il testo di "Una casa dalla A alla Z", le otto righe dei mestieri (indice, capolettera, nome, testo, "Nella foto", striscia in due tagli), foto e didascalia del collettore, il 17 e la scheda, la parete d'inverno con la frase, i contatti; nella testata logo, menu (widget "Navigation Menu" di Ultimate Addons) e telefono; nel piede logo, dati societari e Facebook.
- **Widget HTML**, solo dove Elementor gratuito non arriva: il raccordo a T dell'apertura (il `<picture>` della statica, posato con la stessa geometria: barra sotto il titolo, gambo sull'asse della T dell'alfabeto, sfumatura nella calce; il telefono scarica solo il taglio verticale) e l'alfabeto delle 21 lettere con le otto accese. La pagina statica non ha JavaScript; qui ci sono solo due piccoli script, che danno alla pagina gli stessi punti di riferimento della statica dove Elementor gratuito non dà attributi: uno nella testata dà al menu il nome "Principale" e al logo il nome "F.M. Sistemi, inizio" (Elementor divide alla virgola gli attributi del logo) e toglie il doppio punto di riferimento di testata e piede dentro quelli di Ultimate Addons; uno nei contatti raccoglie le sezioni dall'apertura ai contatti in un `<main>`, dà i nomi alle sezioni ("Apertura", "Una casa dalla A alla Z", "Chi siamo", "In via del Lavoro 37...") e alla parete d'inverno ("La casa a cantiere chiuso"), il ruolo di figura alle tre foto con didascalia, i ruoli di elenco alle otto righe dei mestieri e di termine e definizione alla scheda di "Chi siamo". Gli altri widget HTML contengono solo il foglio di stile della loro sezione (griglia a 12 colonne, misure fluide e colori della statica, con le classi `fms-`): non vanno cancellati.
- Accessibilità come nella statica: il primo Tab porta a "Salta ai lavori" (il link "Salta al contenuto" di Ultimate Addons, che punta a un `#content` inesistente, è nascosto); fuoco da tastiera con il contorno blu FM della statica; lo scorrimento verso le ancore salta subito come nella statica (Elementor lo renderebbe morbido); apostrofi diritti come nella statica (scritti `&#39;` nei widget Testo, perché WordPress li farebbe tipografici).

### Vedere il sito subito

Senza installare niente: doppio clic su `FMSistemi-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `FMSistemi-Sito` e http://localhost:8000/anteprima/). Immagini e caratteri vengono da `assets/web`, quindi funziona anche senza internet e senza nessuna chiamata a Google. È il Formato B: a vista uguale alla versione Elementor.

### Installazione automatica su un WordPress pulito

`plugin/fmsistemi-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa FM Sistemi*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto e si può ripetere. L'import dei template scrive anche i testi alternativi delle 21 immagini nella libreria media; la verifica dice quante immagini li hanno.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova: per la messa online togli la spunta in *Impostazioni > Lettura*) e spegne i Google Fonts di Elementor (i caratteri della pagina arrivano dal sito, vedi "Caratteri"). Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" | **sì**: il menu dell'header è un suo widget |

Contact Form 7 non serve: la home non ha moduli (si telefona o si scrive con un'email già impostata, come nella pagina statica).

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, Pulsante, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

**Caratteri.** Funnel Display e Funnel Sans, gli stessi file woff2 della pagina statica, sono **serviti dal sito, senza nessuna chiamata a Google**: le due `@font-face` della statica sono scritte nel foglio di stile di ogni sezione (widget HTML di soli stili, file del fallback), con l'indirizzo assoluto di `fonts/funnel-display-latin.woff2` e `fonts/funnel-sans-latin.woff2` sulla base delle immagini; il browser scarica ogni carattere una volta sola. Non c'è un foglio `.css` dei caratteri a parte: raw.githubusercontent.com serve i `.css` come `text/plain` con `nosniff` e il browser li scarta (provato: `ERR_BLOCKED_BY_ORB`, pagina in carattere di sistema), mentre i `.woff2` li carica. Quindi `assets/web/fonts/` va caricata insieme alle immagini (vedi "Immagini"). Elementor da sé chiamerebbe Google per Roboto e Roboto Slab (i caratteri predefiniti del kit, non usati in pagina): l'installatore lo spegne; a mano, *Elementor > Impostazioni > Avanzate > Google Fonts: Disattiva* (opzione `elementor_google_font` = 0). Provato nel WordPress di prova: nessuna richiesta a `fonts.googleapis.com` o `fonts.gstatic.com`, i due caratteri caricati, pagina identica. Licenza OFL in `assets/web/fonts/OFL.txt`.

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie dai widget HTML i fogli di stile (con i caratteri) e i due script.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le 21 immagini dei widget Immagine arrivano durante l'import.
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**; spegni i Google Fonts di Elementor (vedi "Caratteri").

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu FM Sistemi** (slug `menu-fm-sistemi`) con tre "Link personalizzati": Lavori `/#lavori`, Chi siamo `/#chi`, Contatti `/#contatti`. Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `fms-00-header.json` e `fms-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "FM Sistemi: Header", salva. Lo stesso per il footer ("FM Sistemi: Footer").
**3. La home.** Importa `fms-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "FM Sistemi: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** *Media*: per le 21 immagini importate incolla nel campo "Testo alternativo" i testi di `elementor-json/testi-alternativi-immagini.txt`.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/fms-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas* (serve comunque Ultimate Addons per il widget del menu).

**Immagini.** Le 21 immagini dei widget Immagine (logo, strisce, collettore, parete d'inverno) vengono scaricate da Elementor nella libreria media al momento dell'import. Il raccordo a T dell'apertura e i caratteri, invece, li usano i widget HTML e restano all'indirizzo della base delle immagini: oggi `raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/FMSistemi-Sito/assets/web/`, che funziona solo quando il ramo è su GitHub con la cartella `assets/web` di questa versione. **Attenzione:** oggi (19 ottobre 2026) sul ramo `claude/benvegnu-sito` ci sono ancora le foto della versione scura con gli stessi nomi (26 file su 29 diversi da quelli di `assets/web/`, controllato con `git hash-object`; il raccordo a T è quello su nero): finché il ramo non è aggiornato, lo zip e i JSON con la base predefinita installano la home con le foto scure. Prima di usarli, il ramo va aggiornato con `assets/web/` (oppure si rigenera con `--base` verso una copia caricata altrove). Per la messa online: carica `assets/web/` sul sito (per esempio in `wp-content/uploads/fmsistemi/`, 3 MB, con la cartella `fonts/`) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/fmsistemi/`, poi reimporta (o rifai lo zip con `crea_installer.py`).

**Prima della messa online, titolo e descrizione.** WordPress non prende il titolo e la descrizione della pagina statica: senza un plugin SEO il titolo è "F.M. Sistemi – Impianti dalla A alla Z a Vigonovo" (nome e motto impostati dall'installatore) e la descrizione manca. Con il plugin SEO del sito (per esempio Yoast o Rank Math), sulla pagina Home: titolo **F.M. Sistemi, impianti dalla A alla Z a Vigonovo**; descrizione **Impianti elettrici e termoidraulici, clima, pompe di calore, fotovoltaico, mobilità elettrica e ristrutturazioni edili. F.M. Sistemi, via del Lavoro 37, Vigonovo (VE). Telefono 049 8305354.** (gli stessi della statica e dell'anteprima). Il motto "Impianti dalla A alla Z a Vigonovo" è preso dal titolo della statica: si cambia in *Impostazioni > Generali*.

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Widget HTML filtrati**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, la pagina perde la griglia e le misure. Se un plugin di ottimizzazione rimanda o unisce gli stili e gli script in linea, escludi i widget HTML della home.
2. **Widget HTML di soli stili**: in ogni sezione c'è un widget HTML che sembra vuoto nell'editor e contiene il foglio di stile della sezione. Se lo si cancella, la sezione perde la griglia e le misure.
3. **Misure dai fogli di stile**: le misure fluide della statica (titoli e margini con `clamp` e con le unità del contenitore, la geometria della T) stanno nei fogli di stile dei widget HTML e prevalgono sui valori del pannello di Elementor. Testi, link, foto e bottone si cambiano dal pannello; dimensioni e colori dei caratteri si cambiano in `_sorgente/contenuti.py`.
4. **Testata sopra l'apertura**: l'header è posato sopra l'apertura (posizione assoluta), come nella statica. Su altre pagine future va previsto uno spazio in alto o una testata diversa.
5. **Menu tra 861 e 1024 px**: Ultimate Addons passa al menu a scomparsa a 1024 px; la statica non ha menu a scomparsa (sotto 861 px mostra solo il telefono). Un foglio di stile tiene le tre voci in riga fino a 861 px e le nasconde sotto, come nella statica.
6. **Apostrofi**: se si riscrive un testo con l'apostrofo nell'editor, WordPress potrebbe tornare a farlo tipografico (nella statica è diritto).
7. **Strisce doppie**: ogni striscia, il collettore e la parete d'inverno sono due widget Immagine (versione per computer e tablet, taglio del telefono): quando si cambia una foto vanno cambiati tutti e due.
8. **JavaScript spento**: la pagina si vede uguale; mancano solo i nomi e i ruoli dei punti di riferimento scritti dai due script (menu "Principale", nome del logo, `<main>`, nomi delle sezioni, figure, elenco dei mestieri, scheda).

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `05-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file carica i propri caratteri e ha il CSS con un prefisso unico (`.fms-home-apertura` ecc.).

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu è un elenco di link senza Ultimate Addons (a vista uguale). Le immagini puntano alla base delle immagini (vedi sopra).

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1.3 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, PHP 8.3, sul WordPress di prova `wp-fmsistemi` (porta 8946, solo locale). Script di prova in `_prova/wp/` (`giro.sh`, `scatto.mjs`, `scatti.sh`, `differenza.py`, `larghezze.sh`, `interazioni.mjs`, `installa.mjs`, `completa.php`, `menu.php`).
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide).
- Ciclo del kit (`ciclo.sh`, PAGINE="/:01-home", tre viste, HTMLTOO=1): import dei 3 template con la funzione del pulsante *Importa template*, 152 elementi salvati uguali al file, 22 immagini nella libreria, nessun riquadro grigio.
- **Confronto con la home statica**, screenshot a pagina intera a 1440x900, 1024x1366 e 390x844 (stesse altezze: 6055, 7275 e 6942 px) e differenza pixel per pixel (soglia 24): a tutte le larghezze differiscono solo pixel dentro le foto delle strisce, del collettore e della parete d'inverno, ricampionate da WordPress nella libreria media (Elementor) o servite in una misura sola invece del `srcset` della statica (fallback); a 1920 nessuna differenza. Stessa altezza e stesse differenze solo nelle foto anche a 320, 360, 600, 601, 768, 860, 861, 900, 1100, 1101 e 1280 px. Gli screenshot sono fatti con `_prova/wp/scatto.mjs` (come `shoot.mjs` del kit, ma blocca in pixel l'altezza dell'apertura, che è alta quanto la finestra). Gli screenshot finali di Elementor (1440, 1024, 390) e del fallback sono stati guardati a pezzi.
- Corretti durante il collaudo, in `_sorgente/contenuti.py`: titolo "Dalla A alla Z" coperto dalla foto nel fallback; menu nascosto da Ultimate Addons a 1024 px; apostrofi tipografici di WordPress; scorrimento morbido di Elementor verso le ancore; nome del menu ("Principale") e del logo ("F.M. Sistemi, inizio", che Elementor spezzava alla virgola).
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- **Interazioni** (Playwright, stesse azioni sulla statica, su WordPress e sul fallback): a 1440 clic su A, E e P (la riga arriva a 32 px dal bordo alto, stessa posizione di scorrimento, `:target` giusto, segno di rame #B4703A acceso); passaggio del mouse su C (rame per il testo #8F4F1F) e sul bottone (grafite con il testo calce); i primi 12 Tab nello stesso ordine della statica (Salta ai lavori, F.M. Sistemi inizio, Lavori, Chi siamo, Contatti, telefono, A, C, E, F, M, P), fuoco sulla A con il contorno blu FM di 2 px, Invio porta a `#lavoro-a`, il Tab seguente prosegue da lì come nella statica; a 390 tocco su P e su M. In ogni passo risultato identico alla statica. Punti di riferimento uguali: un `main` dall'apertura ai contatti, `nav` "Principale" e "I nostri lavori, dalla A alla Z", un solo h1. Nessun errore in console, nessuna richiesta a Google, nessuno scorrimento orizzontale.
- **Installatore** su WordPress svuotato (contenuti, template, kit di Elementor, immagini e menu cancellati; Elementor, Ultimate Addons e gli altri plugin disattivati, tema Twenty Twenty-Five), installando solo dallo zip dall'interfaccia (*Carica plugin*, *Attiva*, i 9 passi in ordine). Lo zip di prova era fatto con le immagini dal server locale (`crea_installer.py --json _prova/build/elementor-json`): tema e plugin attivati, kit di Elementor ricreato, 3 template importati (8, 138 e 6 elementi su 8, 138 e 6), 21 immagini nella libreria tutte con il testo alternativo, Google Fonts di Elementor spenti, Home, header, footer e menu da 3 voci creati. La home uscita: stesse differenze dalla statica del ciclo (solo dentro le foto), interazioni uguali alla statica, `controlla.mjs` senza problemi. Gli screenshot in `screenshot/elementor/` sono di questa home. Limite della prova: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice); lo zip in `plugin/` punta alla base su GitHub.
- Variante *Canvas* (`fms-01-home-completa.json`) importata in una pagina di prova: a 1440 e 390 uguale alla home (solo le foto). Non provate le modifiche dall'editor di Elementor.
- **Revisione indipendente** (METODO 2.6, 19 ottobre 2026, da chi non ha costruito la conversione). Prove rifatte con script propri (`_prova/wp/revisione/`), sulla home installata dallo zip su un WordPress svuotato come sopra (8, 138 e 6 elementi su 8, 138 e 6; 21 immagini, tutte con il testo alternativo; Google Fonts di Elementor spenti) e sul fallback:
  - fedeltà: screenshot a pagina intera a 1440, 1024, 768 e 390 px, stesse altezze della statica (6055, 7275, 6966, 6942 px), differenze pixel per pixel solo dentro le foto (mappa delle differenze guardata), per Elementor, fallback e variante *Canvas*; screenshot Elementor finali guardati a pezzi; con JavaScript spento la prima schermata coincide con la statica a 1440 e 390;
  - testi: testo visibile identico alla statica (senza spazi, 2174 caratteri), stessi titoli h1-h3, stessi testi alternativi, stessi link; nessun dato nuovo; nessun U+2014 in LEGGIMI, `_sorgente/`, `elementor-json/`, `html-fallback/`, `anteprima/` e nello zip;
  - interazioni: clic su A, E e P, tocco su P e M, passaggio del mouse, Tab da capo a fondo a 1440, 1024, 768 e 390 (stesso ordine della statica), Invio sulla A, nessun menu a scomparsa (la statica sotto 861 px mostra solo il telefono), nessun errore o avviso in console, nessuna richiesta a Google, nessuno scorrimento orizzontale; `controlla.mjs` senza problemi a 390, 768, 1024 e 1440.
  - **Difetti trovati e corretti** in `_sorgente/` (poi rigenerati build, zip, ciclo, installazione e screenshot): (1) i caratteri erano in un foglio `fonts/caratteri.css` sulla base delle immagini: raw.githubusercontent.com lo serve come `text/plain` con `nosniff` e il browser lo scarta (provato nel fallback con la base predefinita: `ERR_BLOCKED_BY_ORB`, nessun carattere caricato), quindi lo zip e i JSON consegnati avrebbero mostrato la pagina in carattere di sistema; nel collaudo non si vedeva perché il server locale serve i `.css` come `text/css`. Ora le `@font-face` sono nei fogli delle sezioni, con l'indirizzo dei woff2 (provato con la base su GitHub: i due caratteri caricati), e `caratteri.css` non c'è più. (2) I link di testo (o scrivete, la pagina di partner, numero grande, indirizzi email, Google Maps) con il fuoco diventavano color rame; nella statica restano grafite e prendono solo il contorno blu. (3) Nel fallback il contorno del fuoco del bottone era di 3 px color rame invece che di 2 px blu FM. (4) Punti di riferimento: mancavano i nomi della sezione "Apertura", delle tre sezioni con titolo e della parete d'inverno, il ruolo di figura (in Elementor i contenitori "figure" escono come `<div>`), l'elenco dei mestieri e la scheda; testata e piede comparivano due volte come punti di riferimento dentro quelli di Ultimate Addons. Ora l'albero di accessibilità coincide con quello della statica, salvo il menu, che Ultimate Addons scrive come elenco. (5) Un messaggio dell'installatore citava un'opzione `--caratteri-locali` che non esiste.
  - non corretto, perché non è un difetto della conversione: sul ramo GitHub della base predefinita ci sono ancora le foto della versione scura (vedi "Immagini").

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i "Dati da confermare" qui sotto. In più:
1. **Base delle immagini**: le foto, il raccordo a T e i caratteri vanno caricati sul sito (o il ramo GitHub aggiornato con questa `assets/web/`, che oggi ha ancora le foto scure) prima dell'import; vedi "Immagini".
2. **Titolo, motto e descrizione** della Home da impostare con il plugin SEO e in *Impostazioni > Generali* (vedi "Prima della messa online").
3. **Privacy e cookie**: come nella statica i link non ci sono; le pagine vanno scritte e collegate nel piede prima di pubblicare.
4. **Foto**: sono i segnaposto Pexels della statica (vedi "Foto da rifare dal vero"); quando arrivano le foto vere si rifanno i tagli e si sostituiscono nella libreria media e in `assets/web/`.

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (collegamenti, nessuna copia in più)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/fmsistemi-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini e i caratteri), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.

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

Tutte le foto in pagina sono segnaposto Pexels (licenza "Free", elenco in `assets/CREDITI.md`). Il raccordo in rame è l'unica foto a colori; le altre sono in monocromia calda chiara; la parete d'inverno resta calda. Un giorno di scatti su due cantieri basta. Regole comuni: luce chiara, fondi chiari (carta, intonaco a calce, pietra) o il soggetto nella luce di una finestra, nessun nero pieno, macro 50-100 mm su cavalletto, luce di finestra laterale o un pannello diffusore, niente persone riconoscibili, niente marchi concorrenti di Viessmann in primo piano, file RAW o JPEG almeno 4000 px di lato lungo. Le righe dei mestieri sono strisce orizzontali 3,5:1 (2,6:1 al telefono): inquadrare largo, con il soggetto a metà altezza.

1. **T, apertura (per prima).** Un raccordo a T in rame brasato su un loro impianto, fotografato frontale con la barra orizzontale e il gambo verso il basso, il gambo lungo almeno quanto la barra è larga, posato su un foglio di carta o un intonaco a calce chiaro, con la luce di una finestra da sinistra in alto e la sua ombra vera sul fondo; serve che barra e gambo siano dritti e interi, perché la pagina allinea il gambo alla lettera T dell'alfabeto. Oggi la T è la foto su nero di Pexels scontornata e posata sulla calce con un'ombra disegnata: è il segnaposto più debole della pagina. Dallo stesso scatto si ricava la striscia della riga 02.
2. **E.** Il loro quadro elettrico cablato: marrone, blu e giallo-verde pettinati in parallelo, una fila di magnetotermici con le etichette scritte a mano; oggi sono i morsetti di un quadro qualsiasi, in monocromia perché i colori dei cavi non sono quelli di un impianto civile italiano.
3. **P.** La griglia di una pompa di calore Viessmann installata da loro, macro in controluce; oggi è la griglia di un climatizzatore qualsiasi.
4. **Collettore.** Un collettore in ottone prima del massetto, dall'alto o frontale, con le spire dei tubi sull'isolante.
5. **F.** Moduli su un tetto in coppi della Riviera del Brenta, luce radente del tardo pomeriggio, la griglia delle celle leggibile.
6. **M.** Una presa di ricarica montata da loro, a muro o su colonnina.
7. **R.** Intonaco fresco su una parete di una loro ristrutturazione, luce radente.
8. **A.** Acqua da un addolcitore o filtro installato da loro, gocce o getto su fondo chiaro (oggi: gocce su una superficie chiara, Pexels 15192101).
9. **C.** La griglia di un'unità interna di climatizzazione installata da loro.
10. **Parete d'inverno.** Un interno finito da loro, a cantiere chiuso, con la luce del pomeriggio sul muro e nessun impianto in vista (formato orizzontale, la parte bassa chiara e quieta: sopra ci va la frase in grafite).

## Licenze

- Caratteri: Funnel Display e Funnel Sans, The Funnel Project Authors (Dicotype), Google Fonts, SIL Open Font License 1.1, uso commerciale libero; file serviti dalla pagina in `sito/fonts`, licenza in `sito/fonts/OFL.txt`.
- Foto: licenza Pexels (uso libero anche commerciale, attribuzione non richiesta, modifiche ammesse; non far credere che persone o marchi ritratti approvino il prodotto). Dettagli e pagine in `assets/CREDITI.md`.
- `assets/originali/header.jpg` (foto di repertorio del sito attuale): licenza ignota, non usata.

## Loghi e pagine

- Il logo in pagina è il raster 480x80 del sito attuale, con il nero portato a grafite e il fondo reso trasparente per la calce (`sito/img/logo.png`): serve il logo vettoriale.
- Il blu FM #046EA2 è letto dal raster del logo: chiedere il colore ufficiale (e se ne esiste uno per il rame o per un fondo).
- Privacy e cookie: le pagine non esistono e i link sono stati tolti dal piede; vanno scritte e collegate prima di pubblicare.
- Favicon: quella del sito attuale (192x192).
