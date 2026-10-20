# Mario Agnoletto, proposta di home

È una proposta non richiesta e comprende solo la home. Non è stata pubblicata e l'azienda non è stata contattata.

## Cosa c'è

- `sito/index.html`: la home finale "Tavola dei campioni" (prototipo B, scelto dal committente), in HTML statico: si apre con un doppio clic.
  - Immagini in `sito/img/` (WebP in più larghezze, logo e timbro in SVG).
  - Carattere in `sito/fonts/`: Host Grotesk, SIL Open Font License 1.1. La pagina non chiede nulla a Google né ad altri domini.
- `screenshot/home/`: home a 1440 e a 390, intere e prima schermata, più le prime schermate a 320, 768, 1024 e 1920, il filtro, il menu e la sola chiusura a 1440 (`chiusura-1440.jpg`). `NOTA.md` spiega idea, caratteri, colori, interazione, foto, controlli e cosa è cambiato nell'ultimo giro.
- La stessa home per WordPress con Elementor, più header e footer: `elementor-json/`, `html-fallback/`, `anteprima/`, `plugin/agnoletto-installer.zip`, `assets/web/`, `screenshot/elementor/`, `screenshot/fallback/` e il generatore in `_sorgente/` (vedi "Versione WordPress della home").
- `01-analisi.md`: analisi del sito attuale, fatti con le fonti, riferimenti.
- `assets/CREDITI.md`: origine e licenza di ogni foto.
- `_prova/`: prototipi A e B, script, riferimenti.
  - La home si rifà con `bash _prova/script/build_finale.sh` (scontorni se mancano, immagini, logo, pagina, controlli, segnali, screenshot).
  - Prove a parte: `finale_filtro.mjs` (filtro e menu con tastiera, dito e indirizzo), `finale_nitidezza.mjs` (file scelto e risoluzione per ogni foto), `finale_misure.mjs` (posizioni degli elementi).
  - Gli script della vecchia versione A che il build non usa più sono `finale_logo.py` e `finale_verifica.mjs`.
  - Il modello di segmentazione usato per gli scontorni (BiRefNet lite, licenza MIT, 224 MB) è in `_prova/crawl/modelli/`. Serve solo per rifare le maschere (`_prova/finale/tacco-alfa.png` e `_prova/finale/alfa/`) e si può cancellare se manca spazio.

La versione A, "Dritto e rovescio", è stata sostituita. Da A sono rimaste solo correzioni di testo già verificate: "cristalli e pietre" al posto del marchio nella bigiotteria, e i recapiti, che erano già uguali.

## Da fare: la versione WordPress va rigenerata (chiusura cambiata)

La chiusura della home statica è stata rifatta dopo che la versione WordPress era stata generata, e poi rifatta di nuovo il 20 ottobre 2026. La fascia grafite "Dove siamo" con il telefono grande e i quattro blocchi di recapiti era diventata una scheda d'archivio col timbro MA impresso. Il committente l'ha bocciata e ha scelto lo stile B "con foto".
- **Ora** a sinistra c'è la foto della sede, a filo del bordo della pagina: `sito/img/sede-*.webp` e `sede-q-*.webp`, dalla foto `photos_large_company.jpg` del loro sito.
- A destra ci sono la frase "Seguiamo il pezzo dal progetto alla serie" e i recapiti in quattro righe: telefono, email, indirizzo con la mappa, fax.
- Il piede è **una riga sola**: ragione sociale, P.IVA, PEC e la riga sulla foto della fresa.
- I dati sono gli stessi. Dettagli e motivi sono nella NOTA (`screenshot/home/NOTA.md`, "Chiusura nuova").

`elementor-json/`, `html-fallback/` (`05-contatti.html` e `99-footer/01-footer.html`), `anteprima/`, `plugin/agnoletto-installer.zip`, `assets/web/` e `screenshot/elementor/` e `screenshot/fallback/` mostrano **ancora la chiusura vecchia** (la fascia grafite). Questo vale anche per le altezze e il collaudo descritti qui sotto.

Per rigenerarli:
1. Aggiornare il generatore in `_sorgente/` (`contenuti.py`, sezione contatti e piede) sulla nuova `sito/index.html`.
2. Aggiungere a `assets/web/` le foto della sede (`sede-1020.webp`, `sede-q-1080.webp`). Il timbro impresso della scheda non serve più.
3. Lanciare i tre comandi di "Rigenerare i file" e rifare il collaudo.

In questi giri `_sorgente/` e i file WordPress non sono stati toccati.

Il 1979 ora compare in un punto solo, l'apertura ("dal 1979"). Il piede non lo riporta più, e nemmeno i recapiti, dove c'era l'etichetta "Ditta". La riga della fresa nel piede ora è "La foto della fresa (B) è di repertorio, Unsplash".

## Versione WordPress della home (come per Benvegnù)

La home finale ("Tavola dei campioni", `sito/index.html`) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina approvata: a 1440, 1024, 768 e 390 px gli screenshot di WordPress hanno la stessa altezza di quelli della home statica (5528, 4731, 6490 e 6330 px) e differiscono solo dentro le foto, che WordPress ricampiona dalle misure della sua libreria media (vedi "Collaudo fatto"). Le interazioni sono le stesse: filtro per metallo con mouse, tastiera, dito e indirizzo (`#metallo=ottone`), riga "Non in ...", menu a tendina sotto i 1240 px che si chiude con una voce, con Esc e toccando fuori, voci del menu che portano subito alla sezione.

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `mag-00-header.json` e `mag-99-footer.json` (tipo *sezione*), `mag-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `mag-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 10 foto, da incollare nella libreria media (Elementor li perde all'import; l'installatore li scrive da sé) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `05-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/agnoletto-installer.zip` | plugin che installa e configura la home su un WordPress pulito, con dentro i file di `assets/web` (vedi "Installazione automatica") |
| `assets/web/` | quello che serve al sito, preso senza ritocchi da `sito/img` e `sito/fonts`: il tacco dell'apertura (orizzontale e ruotato, due larghezze), logo e timbri in SVG, le 10 foto nella misura più grande della statica, il carattere con la licenza (`fonts/`) |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova e dall'anteprima HTML, a 1440 (`desktop`), 1024 (`tablet`) e 390 px (`mobile`) |
| `_sorgente/` | il generatore: `contenuti.py` (testi, sezioni, fogli di stile e script della statica), `motore.py` e `build.py` (quelli di Benvegnù, logica non toccata, prefisso `mag`), `prepara_immagini.py`, `crea_installer.py`, `installer/`, `OFL-Host-Grotesk.txt` |

Come è fatta la pagina in Elementor (103 elementi tra header, home e footer):
- **Widget nativi, modificabili dal cliente**: i titoli (h1 e quattro h2), 29 widget Testo (frase d'apertura, "Tombelle di Vigonovo (VE), dal 1979", legenda, le etichette A B C D, le introduzioni, le didascalie dei sette campioni con numero, nome, metalli e riga, le didascalie di Prototipo e Serie e della foto dell'ottone, il cartellino, i contatti, i recapiti, il piede, il telefono della testata), i due bottoni "Chiama", le 10 foto (widget Immagine, ognuna nella libreria media), il menu (widget "Navigation Menu" di Ultimate Addons, che legge il menu WordPress "Menu Mario Agnoletto").
- **Widget HTML**, solo dove Elementor gratuito non arriva: il logo (SVG) in testata e piede; il tacco dell'apertura con il `<picture>` della statica (pezzo ruotato sotto i 900 px), i quattro richiami e il timbro battuto sulla punta; il filtro per metallo con il conteggio; la riga "Non in ..." con lo script del filtro; il menu a tendina sotto i 1240 px con il suo script (le voci le copia dal menu WordPress); il dritto e rovescio del monogramma nel cartellino. Gli script sono quelli della pagina statica, senza librerie.
- Altri due widget HTML (in "Dal disegno alla serie" e in "Dove siamo") contengono solo il foglio di stile della sezione e, in "Dove siamo", lo script che raccoglie le sezioni in `<main>` come nella statica. Stanno in un contenitore nascosto (classe `mag-stile`): non vanno cancellati.
- L'impaginazione è il foglio di stile della statica (griglia a 12 colonne, misure fluide con `clamp`, punti di rottura 1240, 1100, 900, 600, 360 px) con le classi `mag-`, scritto nei widget HTML: vale uguale per Elementor e per il fallback.
- Il filtro riconosce i metalli di ogni campione dalle classi del suo contenitore (`mag-m-zama`, `mag-m-ottone`, `mag-m-alluminio`, `mag-m-acciaio`, in *Avanzate > Classi CSS*): per cambiare i metalli di un campione si cambiano lì, e il numero e il nome dalla sua didascalia.

### Vedere il sito subito

Senza installare niente: doppio clic su `MarioAgnoletto-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `MarioAgnoletto-Sito` e http://localhost:8000/anteprima/). Immagini, logo e carattere vengono da `assets/web`, quindi funziona anche senza internet. È il Formato B: a vista uguale alla versione Elementor.

### Installazione automatica su un WordPress pulito

`plugin/agnoletto-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Mario Agnoletto*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, file del sito, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto.
3. Alla fine disattiva ed elimina il plugin di installazione. La cartella `wp-content/uploads/mario-agnoletto/` resta: la usano la pagina e il carattere.

Il passo "File del sito" copia i file di `assets/web` in `wp-content/uploads/mario-agnoletto/`; l'import poi riscrive l'indirizzo delle immagini dei template con quella cartella. Così la home installata non dipende da GitHub né da altri domini, come la pagina statica (Elementor copia le 10 foto nella libreria media dalla stessa cartella).
Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online togli la spunta in *Impostazioni > Lettura*. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" | **sì**: il menu dell'header è un suo widget |

Contact Form 7 non serve: la home non ha moduli (telefono, email e PEC come nella pagina statica).

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, Pulsante, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

**Caratteri.** Host Grotesk non è nell'elenco dei Google Fonts di Elementor, quindi Elementor non lo chiede a Google: ogni sezione porta la regola `@font-face` con il woff2 della statica (`assets/web/fonts/host-grotesk-latin.woff2`, sottoinsieme latino, pesi 300-800, licenza OFL accanto), all'indirizzo della base delle immagini.
- Con l'installatore il file sta nel sito (`wp-content/uploads/mario-agnoletto/fonts/`) e Google Fonts di Elementor è spento (*Elementor > Impostazioni > Avanzate > Google Fonts: Disattiva*), così non arrivano nemmeno Roboto e Roboto Slab del kit: la home non chiede niente a Google (provato: nessun dominio esterno).
- Con l'import a mano il file arriva dalla base predefinita (`raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/MarioAgnoletto-Sito/assets/web/`), che manda l'intestazione CORS giusta, ma funziona solo quando il ramo è su GitHub con la cartella `assets/web`. Per la messa online carica `assets/web/` sul sito (per esempio in `wp-content/uploads/mario-agnoletto/`) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/mario-agnoletto/`, poi reimporta; e spegni Google Fonts di Elementor come sopra.
- Nel fallback e nell'anteprima il motore scrive anche un `<link rel="preconnect">` a fonts.gstatic.com e un foglio di stile vuoto (`data:text/css,`): non scaricano niente; il preconnect si può cancellare dai file del Formato B.

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie gli script dei widget HTML e la pagina resta senza filtro e senza menu a tendina.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le 10 foto arrivano durante l'import (vedi "Caratteri" per la base delle immagini).
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**; spegni Google Fonts di Elementor (vedi "Caratteri").

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu Mario Agnoletto** (slug `menu-mario-agnoletto`) con quattro "Link personalizzati": Lavorazioni `/#lavorazioni`, Dal disegno alla serie `/#serie`, Punzoni `/#punzoni`, Dove siamo `/#contatti`. Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto. Il menu a tendina sotto i 1240 px prende le stesse voci.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `mag-00-header.json` e `mag-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Mario Agnoletto: Header", salva. Lo stesso per il footer ("Mario Agnoletto: Footer").
**3. La home.** Importa `mag-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "Mario Agnoletto: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** Incolla quelli di `elementor-json/testi-alternativi-immagini.txt` nella libreria media.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/mag-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas* (provata nel WordPress di prova: uguale alla home con l'header globale).

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Script tolti**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, il filtro e il menu a tendina non funzionano. Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi i widget HTML della home.
2. **Fogli di stile nei widget HTML**: le misure della statica stanno lì e prevalgono sui valori del pannello di Elementor. Testi, link, foto e bottoni si cambiano dal pannello; dimensioni, colori e impaginazione si cambiano in `_sorgente/contenuti.py`.
3. **Testata sopra l'apertura**: l'header è posato sopra l'apertura (posizione assoluta, come nella statica). Su altre pagine future va previsto uno spazio in alto o una testata diversa.
4. **Menu sotto i 1240 px**: Ultimate Addons passa al menu a scomparsa a 1024 px, la pagina statica alla tendina a 1240. Sotto i 1240 px il widget di Ultimate Addons è nascosto e compare la tendina della statica (widget HTML), con le voci copiate dal menu WordPress.
5. **Apostrofi**: Elementor passa i testi a `wptexturize`, che cambia `'` in `’`. Nei template l'apostrofo è scritto `&#39;`, così resta diritto come nella statica; un testo riscritto dal pannello prende l'apostrofo tipografico.
6. **Scorrimento alle ancore**: come nella statica, una voce del menu porta subito alla sezione, senza animazione. Da soli, Elementor (`scroll-behavior:smooth` nel suo foglio di stile) e Ultimate Addons (0,8 s di animazione sulle voci del suo menu, anche con "riduci movimento" acceso) animerebbero lo scorrimento: la testata li spegne con una regola nel contenitore nascosto `mag-stile` e con tre righe nello script del menu a tendina. Se si cancellano, il punto d'arrivo resta lo stesso ma lo scorrimento torna animato.
7. **Testata e piede del tema**: in WordPress la testata sta dentro il `<header id="masthead">` e il piede dentro il `<footer id="colophon">` di Ultimate Addons, quindi i due contenitori di Elementor sono semplici `div` (un footer dentro un footer non è HTML valido). Nel Formato B e nell'anteprima, che non hanno il tema intorno, testata e piede sono quindi `div` anche lì.
8. **Titolo della scheda e descrizione**: WordPress scrive il titolo come "Mario Agnoletto – Incisore meccanico a Tombelle di Vigonovo" (nome del sito, trattino del tema, motto), la statica "Mario Agnoletto, incisore meccanico a Tombelle di Vigonovo". La descrizione per i motori di ricerca della statica (`descrizione` in `contenuti.py`) in WordPress va messa con un plugin SEO, che di solito permette anche di cambiare il titolo.

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `05-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file porta il suo carattere (`@font-face`) e il CSS con un prefisso unico (`.mag-home-apertura` ecc.). `02-lavorazioni.html` contiene il filtro e il suo script, `00-header/01-header.html` il menu a tendina.

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu in riga è quello del generatore, non il menu WordPress (a vista uguale). Le immagini e il carattere puntano alla base delle immagini (vedi "Caratteri").

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1.3 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, PHP 8.3, sul WordPress di prova `wp-agnoletto` (porta 8943, solo locale).
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide).
- Ciclo del kit (`ciclo.sh` con PAGINE="/:01-home", tre viste, HTMLTOO=1; lo fa `_prova/wp/giro.sh`, che dopo l'import crea il menu con `_prova/wp/menu.php` e poi fa gli stessi scatti): import dei 3 template con la funzione del pulsante *Importa template*, 103 elementi salvati uguali al file, 10 immagini nella libreria, nessun riquadro grigio.
- **Confronto con la home statica**, screenshot a pagina intera con `shoot.mjs` del kit a 1440x900, 1024x1366 e 390x844 e differenza pixel per pixel (`_prova/wp/differenza.py`): stesse altezze (5528, 4731, 6330 px), stessa posizione di ogni testo; le righe diverse (32 a 1440, 418 a 1024, 141 a 390) sono tutte dentro le foto, che WordPress serve da una misura ricampionata della libreria e il fallback dal file più grande. Guardati a pezzi, affiancati alla statica (`_prova/wp/affianca.py`), a tutte e tre le larghezze, Elementor e fallback.
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- **Interazioni** (`_prova/wp/interazioni.mjs`, stesse azioni sulla statica, su WordPress e sul fallback, risultati in `_prova/interazioni/risultati.txt`): clic su Zama (1 su 7, riga "Non in zama", indirizzo `#metallo=zama`, sezione alta 1075 px come nella statica); Tutti; Invio su Zama e Tab fino ad Acciaio con il fuoco visibile, Spazio (5 su 7); indirizzo cambiato a pagina aperta (Ottone, 4 su 7); pagina aperta con `#metallo=alluminio` (3 su 7); a 390 con il dito Ottone (bottoni alti 44 px); menu a 390 (stessa tendina, stesse voci; "Dove siamo" chiude il menu e porta ai contatti); menu a 1024 (tendina 619-839 px sotto il comando, Esc la chiude e rimette il fuoco su "Menu", un clic fuori la chiude). Risultati uguali alla statica in ogni passo, scatti del filtro uguali salvo le foto. Nessun errore in console, nessuna richiesta a domini esterni, carattere Host Grotesk caricato.
- **Installatore** su WordPress svuotato (`nuovo-wp.sh`, plugin disattivati, tema Twenty Twenty-Five, nessuna cartella `mario-agnoletto`), installando solo dallo zip di `plugin/` dall'interfaccia (*Carica plugin*, *Attiva*, i 10 passi in ordine, `_prova/wp/installa.mjs`, risultato in `_prova/wp/installa.txt`): tema e plugin attivati, kit creato, 19 file copiati nella cartella del sito, 3 template importati con la base riscritta (8, 90 e 5 elementi su 8, 90 e 5; 10 foto nella libreria con il testo alternativo), Home, header, footer e menu da 4 voci creati. La home uscita dall'installatore coincide con la statica come sopra, le interazioni danno gli stessi risultati, `controlla.mjs` non trova problemi e nessuna richiesta esce dal sito. Limite della prova: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice).
- Variante *Canvas* con header e footer dentro (`pagine-complete-senza-pro`): importata, fotografata a 1440 e 390, uguale; poi tolta dal WordPress di prova.

**Revisione indipendente (19 ottobre 2026, da chi non ha costruito la versione WordPress).** Prove rifatte da capo con script propri, sulla statica, su WordPress e sul fallback con le stesse azioni:
- Screenshot a pagina intera a 1440x900, 1024x1366, **768x1024** e 390x844 (`shoot.mjs` del kit), differenza pixel per pixel e pezzi guardati uno per uno: stesse altezze (5528, 4731, 6490, 6330 px) in Elementor, nel fallback del ciclo e in `anteprima/` aperta con un doppio clic; le zone diverse sono solo dentro le foto. Testo visibile della pagina, titoli h1-h3, testi alternativi e link identici alla statica (salvo `/#...` al posto di `#...`).
- Interazioni (`_prova/wp/interazioni.mjs` e `_prova/wp/revisione-interazioni.mjs`; testi, titoli e punti di riferimento con `revisione-semantica.mjs`; editor con `revisione-editor.mjs` e `revisione-salva.mjs`): clic, tocco e tastiera sul filtro; ordine del Tab dall'inizio (16 passi uguali, fuoco visibile 2 px grafite); colori a riposo e al passaggio di bottoni, voci, telefono, email e Maps; menu a 390 con il dito e con la tastiera (Tab, Invio, voci); posizione d'arrivo di ogni voce del menu a 1440 e a 390; "riduci movimento"; pagina con JavaScript spento (stessa altezza, sette campioni e bottoni visibili); nessun errore o avviso in console, nessuna richiesta fallita o verso altri domini.
- **Corretto**: le voci del menu in riga (Ultimate Addons) e la tendina a 1024 animavano lo scorrimento fino alla sezione (Punzoni a 1440: 166 px percorsi dopo un secondo, anche con "riduci movimento"), la statica salta subito; ora WordPress salta subito come la statica (vedi "Cosa potrebbe non reggere", punto 6). **Corretto**: il piede era un `<footer>` dentro il `<footer>` di Ultimate Addons (HTML non valido, due "contentinfo" annidati), ora è un `div` (punto 7). **Corretto**: il menu in riga non aveva il nome "Sezioni" della statica per i lettori di schermo; ora lo prende in Elementor e nel fallback.
- Editor di Elementor aperto sulla Home (41 contenitori, 5 Titoli, 26 Testi, 2 Pulsanti, 10 Immagini, 6 HTML, nessun errore), widget Testo aperto nel pannello; Home, header e footer **salvati dall'editor** senza modifiche: la pagina pubblicata resta uguale pixel per pixel e con le stesse interazioni.
- Rigenerato con `build.py` e `crea_installer.py`; ciclo del kit (`_prova/wp/giro.sh`): import di 3 file, 103 elementi uguali al file, 10 immagini, nessun problema; `controlla.mjs`: nessun problema a 390, 768, 1024 e 1440, Elementor e fallback.
- Installatore rifatto su WordPress svuotato (contenuti, template e **kit di Elementor** cancellati, plugin disattivati, tema Twenty Twenty-Five, nessuna cartella `mario-agnoletto`), solo dall'interfaccia: tutti i passi a buon fine, kit nuovo creato, 8, 90 e 5 elementi, 10 foto con testo alternativo; la home installata è uguale alla statica alle quattro larghezze, interazioni uguali, `controlla.mjs` senza problemi. Limite che resta: tema e plugin erano già sul disco.

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i punti di "Da confermare con l'azienda" qui sotto. In più:
1. **Base delle immagini**: con l'import a mano, `assets/web` va caricata sul sito (o il ramo GitHub pubblicato) prima dell'import; con l'installatore è già fatto. Vedi "Caratteri".
2. **Logo e timbro in SVG** nei widget HTML: il ricalco va approvato (vedi "Loghi e marchi"); con il file vettoriale originale basta sostituire `logo.svg` nella cartella del sito.
3. **Privacy, Cookie, English** mancano anche in WordPress, come nella statica: vanno aggiunti al piede con le pagine vere.
4. **Alt delle foto**: con l'import a mano vanno incollati nella libreria media (`elementor-json/testi-alternativi-immagini.txt`); sono quelli della statica.

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (collegamenti, nessuna copia in più)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/agnoletto-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono immagini e carattere), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.

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
