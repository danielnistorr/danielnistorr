# Hambro, proposta di nuova home (preparazione)

## Versione WordPress della home (come per Benvegnù)

La home finale ("Campionario al millimetro", `sito/index.html`) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina approvata: a 1440, 1024 e 390 px lo screenshot di WordPress ha la stessa altezza della home statica (8896, 8489 e 8662 px) e ogni riga di testo sta nello stesso punto, al mezzo pixel. Le sole differenze sono arrotondamenti di mezzo pixel nelle misure per settore e nei contatti, e le foto, che WordPress serve dalle misure della sua libreria media invece che dal `srcset` della statica (mai ingrandite). Le interazioni sono le stesse: righello in scala reale, banco di misura (taglio vivo, tubolare, nastro con sei colori), tastiera, tocco, taratura dello schermo che resta nel browser, menu che a meno di 1000 px scorre di lato.

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `hbr-00-header.json` e `hbr-99-footer.json` (tipo *sezione*), `hbr-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `hbr-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 20 foto, da incollare nella libreria media (Elementor li perde all'import; l'installatore li scrive da solo) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `08-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/hambro-installer.zip` | plugin che installa e configura la home su un WordPress pulito (vedi "Installazione automatica") |
| `assets/web/` | quello che serve al sito (2,4 MB): i tre tagli dell'apertura, la striscia di cuoio del banco, gli 11 scontornati del cassetto (`cat/`), le due bobine, il dittico metallo e pelle, i semilavorati (desktop e telefono), Mona Sans con la licenza (`fonts/`). Sono i file più larghi della home statica, collegati e non ritoccati |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova e dall'anteprima HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi, sezioni e fogli di stile), `banco.js` (lo script della pagina statica), `motore.py` e `build.py` (quelli di Benvegnù, prefisso `hbr`), `prepara_immagini.py`, `crea_installer.py`, `installer/` |

Come è fatta la pagina in Elementor (241 elementi: header 7, home 226, footer 8):
- **Widget nativi, modificabili dal cliente**: 26 titoli, 68 testi, il bottone "Prova le misure", 20 foto (ognuna nella libreria media), 89 contenitori. Sono widget nativi anche le righe delle misure per settore (articolo e misura), le misure della ricopertura, il cartellino dei contatti (telefono, posta, indirizzo con "Apri la mappa", orari) e, nell'header, il marchio, il menu (widget "Navigation Menu" di Ultimate Addons) e il telefono; nel footer marchio, indirizzo, telefono, posta, Facebook, P.IVA e informativa.
- **Widget HTML (22 nella home)**, solo dove Elementor gratuito non arriva: il righello d'apertura (SVG disegnato dallo script), la lettura e i comandi del banco, la striscia, la taratura con lo script, il filo e le sagome in scala della ricopertura, la riga delle quote e le 10 quote in scala delle misure per settore. Lo script è quello della pagina statica (`_sorgente/banco.js`), con i selettori col prefisso `hbr-`, senza librerie. Altri 6 widget HTML contengono solo il foglio di stile della loro sezione (la griglia a 12 colonne e le misure fluide della statica, con le classi `hbr-`): non vanno cancellati.
- Le misure in scala usano le variabili `--k` (taratura) e `--u` (un millimetro); il `--gap` della statica qui si chiama `--hbr-gap`, perché Elementor usa già `--gap` su ogni contenitore.

### Vedere il sito subito

Senza installare niente: doppio clic su `Hambro-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `Hambro-Sito` e http://localhost:8000/anteprima/). Le foto vengono da `assets/web`, quindi funziona anche senza internet; il carattere arriva da Google Fonts. È il Formato B: a vista uguale alla versione Elementor (a 1440 px coincide con la home statica pixel per pixel).

### Installazione automatica su un WordPress pulito

`plugin/hambro-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Hambro*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto. Dopo l'import dei template scrive anche i testi alternativi delle 20 foto nella libreria media.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online togli la spunta in *Impostazioni > Lettura*. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" con il menu "Menu Hambro" | **sì**: il menu dell'header è un suo widget |

Contact Form 7 non serve: la home non ha moduli (campioni e ordini si chiedono per posta, con un'email già impostata, o al telefono, come nella pagina statica).

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, Pulsante, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`). Il widget del menu ha il punto di rottura **None**: non diventa mai un menu a scomparsa, perché nella statica sotto i 1000 px le voci passano su una riga che scorre di lato (`motore.py` scrive sempre "tablet": `contenuti.py` lo cambia solo per questo widget, senza toccare il motore).

**Caratteri.** Mona Sans (SIL Open Font License 1.1) è su Google Fonts con l'asse della larghezza che la pagina usa (100-125 %): il widget HTML dell'header carica `https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,200..900&display=swap`, cioè gli stessi file woff2 della pagina statica. L'elenco Google di Elementor non dà l'asse della larghezza, per questo il link è nel widget HTML dell'header e non nelle impostazioni del sito. Nel Formato B ogni file carica il suo link. Per non chiamare Google (GDPR): carica i due woff2 di `assets/web/fonts/` in *Media* o nel tema figlio, togli il `<link>` dal widget HTML dell'header e incolla in *Aspetto > Personalizza > CSS aggiuntivo* le due regole della pagina statica (`sito/index.html`, righe 10 e 11) con il percorso vero dei file:
```
@font-face{font-family:"Mona Sans";src:url(/wp-content/uploads/AAAA/MM/mona-latin.woff2) format("woff2");font-weight:200 900;font-stretch:75% 125%;font-display:swap;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:"Mona Sans";src:url(/wp-content/uploads/AAAA/MM/mona-latin-ext.woff2) format("woff2");font-weight:200 900;font-stretch:75% 125%;font-display:swap;unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
```
WordPress di solito non accetta il caricamento di `.woff2` nella libreria media: in quel caso i file vanno caricati via FTP (per esempio in `wp-content/uploads/hambro/fonts/`). La licenza OFL è in `assets/web/fonts/OFL.txt`.

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie gli script dai widget HTML e restano fermi righello, banco e taratura.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le 20 foto arrivano durante l'import.
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**.

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu Hambro** (slug `menu-hambro`) con cinque "Link personalizzati": Lacci e nastri `/#lacci`, Minuteria `/#minuteria`, Ricopertura `/#ricopertura`, Misure per settore `/#misure`, Contatti `/#contatti`. Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `hbr-00-header.json` e `hbr-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Hambro: Header", salva. Lo stesso per il footer ("Hambro: Footer").
**3. La home.** Importa `hbr-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "Hambro: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** *Media*: per ogni foto incolla il testo di `elementor-json/testi-alternativi-immagini.txt`.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/hbr-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas* (provata nel WordPress di prova: uguale alla home con l'header globale).

**Immagini.** Le 20 foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import (ID fissi: reimportando non si creano doppioni) e WordPress ne fa le misure più piccole per il `srcset`. La striscia di cuoio del banco (`banco-cuoio.jpg`), invece, è uno sfondo del foglio di stile e resta all'indirizzo della base delle immagini: oggi `raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/Hambro-Sito/assets/web/`, che funziona solo quando il ramo è su GitHub con la cartella `assets/web`. Per la messa online: carica `assets/web/` sul sito (per esempio in `wp-content/uploads/hambro/`, 2,4 MB) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/hambro/`, poi reimporta (o rifai lo zip con `crea_installer.py`). Le foto sono quelle della home statica: segnaposto Unsplash e foto del sito di Hambro, con i diritti da chiarire (vedi più sotto, "Licenze e loghi").

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Script tolti**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, il righello resta vuoto e il banco non risponde (la striscia resta a 30 mm). Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi i widget HTML della home.
2. **Widget HTML di soli stili**: in sei sezioni c'è un widget HTML che sembra vuoto nell'editor e contiene il foglio di stile della sezione; anche i widget del righello e della taratura portano il foglio di stile di apertura e banco. Se li si cancella, la sezione perde griglia e misure.
3. **Misure dai fogli di stile**: le misure della pagina statica (corpi, interlinee, colori, margini, con `clamp`) stanno nei fogli di stile dei widget HTML e prevalgono sui valori del pannello di Elementor. Testi, link e foto si cambiano dal pannello; dimensioni e colori si cambiano in `_sorgente/contenuti.py`.
4. **Testata sopra l'apertura**: l'header è posato sopra la foto (posizione assoluta), come nella statica. Su altre pagine future va previsto uno spazio in alto. Il carattere lo carica l'header: una home importata senza l'header (né globale né nella pagina completa) resta con il carattere di sistema.
5. **Scorrimento alle ancore**: Ultimate Addons fa scorrere la pagina in 800 ms fino alle ancore del menu ed Elementor imposta lo scorrimento morbido; nella statica il salto è immediato. Un piccolo script nel widget HTML dell'header e una regola `scroll-behavior:auto` rimettono il salto immediato.
6. **Apostrofi**: Elementor passa il testo dei widget Testo da `wptexturize`, che fa curvi gli apostrofi; nella statica sono dritti, quindi nei widget Testo sono scritti come `&#39;`. Se il cliente riscrive un testo dall'editor, l'apostrofo tornerà curvo (solo una differenza di glifo).

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `08-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file carica il proprio carattere e ha il CSS con un prefisso unico (`.hbr-home-apertura` ecc.). `02-banco.html` contiene lo script: disegna anche il righello di `01-apertura.html`, quindi i due file vanno insieme.

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu è un elenco di link senza Ultimate Addons (a vista uguale, scorre di lato sotto i 1000 px). La striscia di cuoio punta alla base delle immagini (vedi sopra); le foto anche.

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1.3 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, PHP 8.3, sul WordPress di prova `wp-hambro` (porta 8942, solo locale).
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide). Per farlo passare il file di prova `_prova/crawl/ext/ecb6b9.html` (una pagina di prontoimprese.it scaricata per l'analisi, con un trattino lungo nel testo di quel sito) è stato rinominato in `.htm`: `build.py` controlla tutti gli `.html` della cartella, anche quelli di `_prova`.
- Ciclo del kit (`ciclo.sh`, PAGINE="/:01-home", tre viste, HTMLTOO=1): import dei 3 template con la funzione del pulsante *Importa template*, 241 elementi salvati uguali al file, 20 immagini nella libreria, nessun riquadro grigio.
- **Confronto con la home statica**, screenshot a pagina intera a 1440x900, 1024x1366 e 390x844 (stesse altezze: 8896, 8489 e 8662 px) e differenza pixel per pixel: il fallback coincide con la statica pixel per pixel a 1440, salvo 8 righe di pixel a 1024 e 88 righe sparse a 390 (arrotondamenti e foto); Elementor differisce in 121-152 righe sparse, tutte arrotondamenti di mezzo pixel (righe delle misure per settore, cartellino) e ricampionamenti delle foto. Le righe di testo, confrontate una per una (posizione di ogni riga di ogni testo), sono nello stesso punto entro 1 px a 1440, 1024 e 390. Altezza della pagina uguale alla statica a 320, 360, 390, 414, 700, 768, 900, 901, 1001, 1024, 1100, 1101, 1280, 1440 e 2560 px (1 px di differenza a 600, 701, 1000 e 1920, per le misure delle foto della libreria), senza scorrimento orizzontale. Gli screenshot sono fatti con `_prova/wp/scatto.mjs` (come `shoot.mjs` del kit, ma blocca in pixel l'altezza dell'apertura, che dipende dall'altezza della finestra) e guardati a pezzi (`slice.py`).
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- **Interazioni** (Playwright, `_prova/wp/interazioni.mjs`, stesse azioni sulla statica, su WordPress e sul fallback): a 1440 e 1024 con tastiera e mouse (freccia sui materiali: Tubolare 4; Tab sul cursore; Fine: 16; Inizio e freccia: 3; taglio vivo ripreso a 30, due volte Pagina giù e una freccia: 9; clic su Nastro, 50, Giallo: striscia di 50 mm gialla; clic su Taglio vivo: torna a 9), a 390 con il tocco (Tubolare 4, tocco in fondo al cursore 16, Taglio vivo con un tocco all'inizio 2, Nastro 50 Giallo). In ogni passo materiale, lettura, testo, altezza di striscia e tavolo, colore, valori del cursore e testo per i lettori di schermo uguali alla statica. Taratura: dieci frecce danno k 1,05, tessera, righello, sagome e quote si ridisegnano uguali, e dopo una ricarica la scala resta. Menu: "Contatti" porta alla sezione con un salto immediato; a 390 la riga del menu scorre fino allo stesso punto della statica. Colori a riposo, al passaggio del mouse e al fuoco (bottone, menu, telefono, marchio, link di posta, campione, mappa, piede, taratura) uguali alla statica. Con Tab il primo fuoco è il link "Salta al contenuto principale" che Ultimate Addons aggiunge da sé (si vede solo col fuoco), poi gli stessi fuochi della statica. Nessun errore in console.
- **Installatore** su WordPress svuotato (`nuovo-wp.sh`, tutti i plugin disattivati tranne il database, tema Twenty Twenty-Five, kit di Elementor cancellato), installando solo dallo zip dall'interfaccia (*Carica plugin*, *Attiva*, i 9 passi in ordine): tema e plugin attivati, kit creato, 3 template importati (7, 226 e 8 elementi su 7, 226 e 8; 20 foto nella libreria, 20 testi alternativi scritti), Home, header, footer e menu da 5 voci creati. La home uscita dall'installatore coincide con la statica come sopra (stesse altezze e righe di testo, `controlla.mjs` senza problemi) e le interazioni danno gli stessi risultati. Limite della prova: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice); la prova usava uno zip con le immagini dal server locale (`crea_installer.py --json _prova/build/elementor-json`), lo zip in `plugin/` punta alla base su GitHub.
- Variante *Canvas* con header e footer dentro (`pagine-complete-senza-pro`): importata, fotografata a 1440 e 390, uguale alla home con l'header globale, interazioni uguali; poi tolta dal WordPress di prova.

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i "Dati da confermare" e le foto da rifare qui sotto. In più:
1. **Base delle immagini**: `assets/web` va caricata sul sito (o il ramo GitHub pubblicato) prima dell'import, per la striscia del banco; vedi "Immagini".
2. **Google Fonts**: va bene caricare Mona Sans da Google o lo si vuole in locale (GDPR)? Vedi "Caratteri".
3. **Informativa privacy** punta a `#` anche in WordPress, finché non esiste la pagina.
4. **Testi alternativi del cassetto**: nella statica gli 11 scontornati hanno l'alt vuoto (il nome è scritto sotto); il generatore vuole un testo per ogni immagine, quindi in WordPress sono "famiglia: nome" (per esempio "Moschettoni: anello tondo"), con le sole parole già in pagina.
5. **Marchio**: in WordPress il marchio HAMBRO dell'header e del footer porta alla home (`/`), non a `#` come nella statica, perché l'header vale per tutto il sito; il widget Titolo non ha l'`aria-label` "Hambro, inizio pagina" della statica.
6. **Struttura del codice**: Elementor non fa contenitori `figure`, `ul` o `dl` né `aria-labelledby` sulle sezioni, quindi didascalie, elenchi delle misure per settore e cartellino sono `div` e paragrafi (a vista uguali). Restano nativi i titoli h1-h4, i `dl` della ricopertura e dei contatti, l'elenco "Fuori dal cassetto", i campi del banco.

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (collegamenti, nessuna copia in più)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/hambro-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini), `--url-sito URL` (link interni assoluti), `--out CARTELLA`. Prove (in `_prova/wp/`, fuori da git): `giro.sh` (ciclo del kit e menu), `scatti.sh st el ht` (screenshot di statica, WordPress e fallback), `differenza.py`, `confronta-testi.sh`, `interazioni.mjs`, `larghezze.mjs`, `installa.mjs`.

## Preparazione della home statica

- 01-analisi.md: azienda, sito di oggi, dati con fonti, materiale visivo con voti, soggetto e due direzioni artistiche, riferimenti, cose da confermare.
- assets/originali/: 139 immagini scaricate da hambro.it (inventario, misure e voti in _prova/inventario-immagini.json). Diritti da chiarire prima di riusarle.
- assets/esterne/: 10 foto Unsplash usate SOLO come segnaposto per mostrare la direzione artistica. Non sono foto di Hambro e vanno sostituite con foto vere dell'azienda prima di qualsiasi uso pubblico. Autori e licenze in assets/CREDITI.md.
- _prova/ (fuori da git): crawl del sito, screenshot del sito attuale (attuale/), screenshot dei riferimenti (riferimenti/, scartati in riferimenti/scartati/), script.

## Prototipo A della home, "Sotto la pelle" (_prova/home/a/)

- `proto.html`, immagini in `img/`, nota con idea, caratteri, foto e controlli in `nota.md`. Script delle immagini: `_prova/script/proto_a_img.py`.
- Foto segnaposto in pagina: Rodrigues (fibbia oro, fibbia nichel, coppia oro e nichel), Karimov (cuoio), Berg (mani sul cartamodello), tutte Unsplash License. Foto di Hambro in pagina: occhielli e rivetti dello slider, fibbie lucide e brunite, bobina di laccio a taglio vivo (diritti da chiarire).
- Foto da rifare dal vero: la stessa fibbia di Hambro in ogni finitura, su vetro nero, cavalletto fisso e una luce radente, per il selettore Oro e Nichel; la coppia nuda e ricoperta della fibbia da ricoprire; occhielli e rivetti in macro ad alta risoluzione; la bobina di laccio su fondo nero; le mani in laboratorio a Vigonovo.
- Da confermare: orari; finiture disponibili oltre oro e nichel; "sp.0.7/1.1" delle nappe e dei vitelli lavabili (due spessori o un intervallo); che cosa misurano i mm 40, 50, 60 delle fibbie da ricoprire; codici dei rivetti 00, 033, 034, 036; minuteria nichel free; Satab; "Nostre creazioni", "Occasioni macchine" e "Nuovi arrivi" (esclusi dall'indice); logo vettoriale.
- Caratteri: Gilda Display ed Encode Sans (Google Fonts, SIL OFL 1.1), da servire da `sito/fonts` nella versione finale.

## Home finale (sito/)

- `sito/index.html`, immagini in `sito/img/` (solo quelle usate, JPEG in più larghezze), caratteri in `sito/fonts/` (Mona Sans, SIL OFL 1.1, testo della licenza in `sito/fonts/OFL.txt`). Nota con idea, schermate, caratteri, colori, interazione, foto e controlli: `screenshot/home/NOTA.md`.
- Si rifà tutto con `bash _prova/script/build_finale.sh`: immagini con `finale_img.py`, pagina da `finale_pagina.html`, screenshot in `screenshot/home/`. I PNG di controllo vanno in `_prova/screenshot-tmp/` e si cancellano a mano. Prove: `node _prova/script/prova_interazione.mjs <url> <cartella>` (console, menu, tastiera e tocco sul banco, collegamenti, corpi tipografici, foto ingrandite, vuoto del banco) e `node _prova/script/largo.mjs <url> <larghezza>` (scorrimento orizzontale).
- Base: il prototipo B "Campionario al millimetro" (`_prova/home/b/`). Da A viene il dittico metallo e pelle con le sagome in scala.
- **Le foto sono segnaposto, ma la pagina non lo dice**: nessuna didascalia o riga del piede parla di foto provvisorie. L'avviso va nella mail di accompagnamento: "le foto di fibbie, cuoio e laboratorio sono segnaposto Unsplash; le bobine e gli 11 pezzi del cassetto vengono dal vostro sito".

### Dati da confermare con Hambro (in pagina non ci sono segnaposto)
- **1979.** In pagina è sempre "Giorgio Gastaldello, nella pelletteria dal 1979", mai l'anno della srl. Va chiesto l'anno di costituzione della società.
- **Fibbie da ricoprire mm40, 50 e 60.** Le sagome della Tav. 3 sono larghe quanto la misura. Va chiesto se la misura è la luce del passante (la larghezza della cintura) o l'esterno della fibbia, e la proporzione vera di ogni sagoma.
- **Strisce a taglio vivo.** Il sito dice "striscie a taglio vivo da mm2 a mm60": il banco le fa scegliere millimetro per millimetro da 2 a 60. Va confermato che tagliano a ogni millimetro (se no, si torna all'aggancio sulle misure a catalogo). Per il tubolare il banco offre 2, 3, 4 e 16: il sito dice "da mm2 a mm16" (pelletteria) e "mm2-3-4" (calzature); quali misure intermedie ci sono?
- **Righello d'apertura.** La quota "2-4" raccoglie lacci tubolari 2, 3, 4, tondini 2-3,5 e cordoncino 3-4; le altre tacche in cuoio sono 16 (tubolare), 20, 25, 30, 40, 50 (nastri), 60 (strisce e fibbie).
- **Nastri.** I sei colori del banco (rosso, giallo, salvia, viola, grigio, nero) vengono dalla loro foto dei rotoli: vanno chiesti i colori disponibili oggi. Satab: la rappresentanza è ancora valida?
- **Altri dati in pagina.**
  - Rivetti 00, 033, 034, 036 e occhielli piatti e bombati;
  - nappe e vitelli lavabili "sp. 0,7 e 1,1": due spessori o un intervallo?
  - minuteria nichel free;
  - bottoni Yvette e a pressione.
- **Le bobine della Tav. 2.** Che siano il loro magazzino; che la bobina chiara sia tondino in pelle (ha una cucitura: potrebbe essere un tubolare cucito). In pagina sono due ritagli stretti alti 459 px, perché le foto da telefono restino pulite.
- **Misure per settore.** L'elenco riprende le pagine Accessori calzature, abbigliamento e pelletterie del sito. Nastro intrecciato, corda juta, scheletri, salpe e rinforzi, occhielli, lampo e fibbie doppie sono in pagina senza misura: vanno chieste le misure, se ci sono.
- **Contatti.** Telefono principale 049 980 2326. Il 049 980 2330 è il fax? Gli orari (venerdì solo mattina, sabato e domenica chiusi) vanno confermati. Il link "Apri la mappa" cerca l'indirizzo su Google Maps: va controllato che la scheda di Hambro esca per prima. Mancano la pagina privacy e il link Facebook definitivo.
- **Fuori pagina.**
  - PEC, dipendenti, superficie, clienti;
  - sede storica di Noventa Padovana;
  - e-shop annunciato;
  - "Nostre creazioni" e "Occasioni macchine";
  - rapporto con Astor.

### Foto da rifare dal vero (indicazioni di scatto)
Tutte sulla stessa carta avorio opaca (vicina a #F2EDE4), con sole vero o un'unica luce dura da sinistra a circa 30 gradi, ombra netta a destra. Macro 100 mm su cavalletto, f/8-f/11, file almeno 4000 px.
1. **Apertura.** Una fibbia Hambro in zama ad ardiglione, smontata (telaio, ardiglione, passante), posata come nella Tav. 1. Inquadratura orizzontale 16:10 con la carta libera nel terzo sinistro per il titolo, più uno scatto verticale con la fibbia intera al centro per il telefono. È la foto che manca perché la prima schermata arrivi a 8.
2. **Finiture.** La stessa fibbia in oro, nichel, brunito e ramato, stesso punto e stessa luce, per il selettore di finitura (oggi non in pagina).
3. **Nuda e ricoperta.** La stessa fibbia da ricoprire da 40, 50 e 60 mm, prima in metallo nudo e poi ricoperta in pelle, con un righello nel campo. Prende il posto del dittico Rodrigues e Karimov.
4. **Strisce a taglio vivo.** In macro, una per misura (2, 4, 16, 30, 60), stese in piano sulla carta: il fiore e il taglio devono leggersi. Servono per la striscia del banco al posto della grana di Karimov.
5. **Bobine.** In magazzino o in studio, la bobina intera e un dettaglio dei giri, stessa luce, niente scaffale. Prendono il posto delle due foto da telefono della Tav. 2.
6. **Cassetto.** Gli 11 oggetti del cassetto rifotografati alla stessa scala (stessa distanza, stesso obiettivo), dall'alto, sulla stessa carta.
7. **Laboratorio di Vigonovo.** Le mani di chi ricopre una fibbia e un semilavorato sul banco. Prendono il posto della foto di Berg.

### Licenze e loghi
- Foto Unsplash in pagina (Rodrigues `2hWmYcG26E8` e `hqGQcZnEvy0`, Karimov `DmxTTqZtDds`, Berg `an44PeEll_w`): Unsplash License, solo segnaposto, da sostituire prima di qualsiasi uso pubblico. Le foto di fibbie dorate di Rodrigues restano a questa home. Dettagli in `assets/CREDITI.md`.
- Foto e scontornati presi da hambro.it: i diritti vanno chiariti (gli scontornati sembrano foto di produttore).
- Logo: in pagina c'è la scritta HAMBRO in Mona Sans, color cuoio, al posto del JPEG 175x98. Serve il logo vettoriale.
- Mona Sans: SIL Open Font License 1.1, uso commerciale libero, file serviti dalla pagina.

### Soglie "da guardare" di segnali.sh e perché restano
- Una sola misura di H2 (60 px): la scala dei corpi è stata ridotta a 13, 15, 17, 22, 32, 60 e 136 (più la lettura del banco) per togliere i salti di mezzo pixel; i titoli si distinguono per posizione e colore, non per corpo.
- 2 numeri grandi: la lettura del banco, che è lo strumento, e il 1979, sempre con il nome di Gastaldello.
- La numerazione 01-11 del cassetto è l'indice del campionario, non una procedura.
