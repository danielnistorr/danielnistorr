# Paraga Pelli, proposta di nuova home (preparazione)

## Versione WordPress della home (come per Benvegnù)

La home finale ("La mazzetta", `sito/index.html`) è pronta da importare in WordPress con Elementor, più header e footer, in due formati:
- **Formato A (primario):** template Elementor `.json` da importare con *Template > Template salvati > Importa template*, oppure tutto in automatico con il plugin di installazione.
- **Formato B (fallback):** la stessa pagina in HTML+CSS autosufficiente, una sezione per file, da incollare in widget HTML di Elementor.

A vista è la stessa pagina approvata: a 1440, 1024, 768 e 390 px lo screenshot di WordPress coincide con quello della home statica pixel per pixel, tranne le due foto larghe (magazzino e squadra), che WordPress ricampiona dalle misure della sua libreria media (vedi "Collaudo fatto"). Le interazioni sono le stesse: mazzetta che cambia drappo, codice e cartellino, 27 dorsi che aprono le cartelle, nomi degli usi, 403 colori, tastiera e tocco.

### Cosa c'è (versione WordPress)

| Cartella / file | Contenuto |
|---|---|
| `elementor-json/` | **Formato A**: `ppl-00-header.json` e `ppl-99-footer.json` (tipo *sezione*), `ppl-01-home.json` (tipo *pagina*, solo il corpo) |
| `elementor-json/pagine-complete-senza-pro/` | `ppl-01-home-completa.json`: la home con header e footer già dentro e modello *Canvas* |
| `elementor-json/testi-alternativi-immagini.txt` | testi alternativi delle 5 foto della libreria media (Elementor li perde all'import; l'installatore li scrive da solo) |
| `html-fallback/` | **Formato B**: `00-header/01-header.html`, `01-home/01-apertura.html` ... `07-contatti.html`, `99-footer/01-footer.html` |
| `anteprima/` | la home completa in HTML, da aprire con un doppio clic (`anteprima/index.html`) |
| `plugin/paragapelli-installer.zip` | plugin che installa e configura la home su un WordPress pulito (vedi "Installazione automatica") |
| `assets/web/` | quello che serve al sito: il drappo nelle cinque misure della statica, magazzino, squadra e box (desktop e taglio verticale per il telefono), i 27 dorsi, le 403 scansioni a 350 px (`c/`) e a 640 px (`c2/`), i caratteri con le licenze (`fonts/`) |
| `screenshot/elementor/`, `screenshot/fallback/` | la home dal WordPress di prova e dall'anteprima HTML, a 1440, 1024 e 390 px |
| `_sorgente/` | il generatore: `contenuti.py` (testi e sezioni), `mazzetta.js` (lo script della pagina statica), `catalogo.json` (27 articoli, 403 colori), `sagoma.svg` (il filo della pelle sotto il magazzino), `motore.py` e `build.py` (quelli di Benvegnù, prefisso `ppl`), `prepara_immagini.py`, `estrai_catalogo.py`, `crea_installer.py`, `installer/` |

Come è fatta la pagina in Elementor:
- **Widget nativi, modificabili dal cliente** (104 elementi nella home): titoli (h1, h2, h3), testi, i due bottoni "Richiedi il box-campionario", le 5 foto di magazzino, squadra e box (ognuna nella libreria media, con il suo testo alternativo), la tabella LWG, i recapiti, le famiglie del catalogo, le righe degli usi; nella testata il nome, il menu (widget "Navigation Menu" di Ultimate Addons), il telefono e le lingue; nel piede nome, conteggio, P.IVA, indirizzo, telefono, email, Facebook, Privacy.
- **Widget HTML**, solo dove Elementor gratuito non arriva: il drappo che il colore del campione tinge (con il `<picture>` della statica: il telefono scarica solo il taglio verticale; è decorativo, senza testo alternativo, come nella statica), nome e codice grandi del colore, cartellino, mazzetta con lo script e i dati del catalogo, i 27 dorsi, i nomi degli articoli negli usi (sono bottoni che aprono le cartelle), il filo della pelle sotto la foto del magazzino, la fila dei dorsi nel piede. Lo script è quello della pagina statica, senza librerie. Altri widget HTML contengono solo il foglio di stile della loro sezione (le misure fluide e la griglia a 12 colonne della pagina statica, con le classi `ppl-`): non vanno cancellati.
- Il colore del campione scelto passa da variabili CSS (`--tono`, `--base`, `--su-tono`) che lo script cambia: drappo, testata, bottone, campo LWG e bottone del box lo seguono.
- Accessibilità come nella statica: il primo tasto Tab porta a "Vai al catalogo" (il link di Ultimate Addons "Salta al contenuto", che puntava a un `#content` inesistente, è nascosto); il menu si chiama "Principale"; le sezioni dal catalogo ai contatti stanno in un `<main>` (lo crea un piccolo script nel widget HTML dei contatti, perché Elementor gratuito non ha un contenitore che le raccolga; nell'editor non fa niente); il fuoco da tastiera ha il contorno della statica, senza l'anello bianco del tema Hello.

### Vedere il sito subito

Senza installare niente: doppio clic su `ParagaPelli-Sito/anteprima/index.html` (oppure `python3 -m http.server 8000` nella cartella `ParagaPelli-Sito` e http://localhost:8000/anteprima/). Immagini e scansioni vengono da `assets/web`, quindi funziona anche senza internet; i caratteri arrivano da Google Fonts. È il Formato B: a vista uguale alla versione Elementor; il menu del telefono è un elenco a scomparsa senza Ultimate Addons.

### Installazione automatica su un WordPress pulito

`plugin/paragapelli-installer.zip` fa da solo il lavoro del paragrafo "Come importare".
1. Su un WordPress appena installato: *Plugin > Aggiungi nuovo > Carica plugin*, scegli lo zip, *Installa*, *Attiva*.
2. *Strumenti > Installa Paraga Pelli*: apri i passi uno alla volta, nell'ordine (plugin e tema, prima attivazione, impostazioni, i 3 template, pagina Home, header/footer e menu, verifica). Ogni passo scrive cosa ha fatto e si può ripetere. L'import della home scrive anche i testi alternativi delle 5 foto nella libreria media; la verifica dice quante immagini li hanno.
3. Alla fine disattiva ed elimina il plugin di installazione.

Il passo "impostazioni" imposta il sito come **non indicizzabile** (va bene per la prova): per la messa online togli la spunta in *Impostazioni > Lettura*. Se lo zip è fatto con i caratteri serviti dal sito (vedi "Caratteri"), lo stesso passo spegne anche i Google Fonts di Elementor. Per rigenerare lo zip dopo una modifica: `python3 _sorgente/build.py` e poi `python3 _sorgente/crea_installer.py`.

### Versioni e plugin

**Target dichiarato: Elementor 4.3.3, versione gratuita**, con WordPress 7.1 e tema Hello Elementor 3.5.1. Plugin gratuiti, dal catalogo di WordPress.org:

| Plugin | Versione provata | A cosa serve | Obbligatorio? |
|---|---|---|---|
| Ultimate Addons for Elementor (slug `header-footer-elementor`) | 2.9.5 | header e footer su tutto il sito senza Elementor Pro; widget "Navigation Menu" con il menu a scomparsa sul telefono | **sì**: il menu dell'header è un suo widget |

Contact Form 7 non serve: la home non ha moduli (il box-campionario si chiede con un'email già impostata o al telefono, come nella pagina statica).

Il JSON è scritto come quello di Benvegnù: solo contenitori flexbox e widget gratuiti (Titolo, Testo, Immagine, Pulsante, HTML, più "Navigation Menu" di Ultimate Addons), nessun widget o chiave Pro, nessun elemento "atomico" della v4, nessun riferimento ai colori e font globali del kit, nessuna animazione; formato uguale a "Esporta template" (`content`, `page_settings`, `version: "0.4"`, `title`, `type`).

**Caratteri.** Sono Mona Sans e Libre Caslon Display, gli stessi file woff2 della pagina statica (Mona Sans serve con l'asse della larghezza, che l'elenco Google di Elementor non dà, per questo il caricamento è nel widget HTML della testata e dell'apertura). Due modi:
- **Da Google Fonts** (così sono fatti i file consegnati): `https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=Mona+Sans:wdth,wght@75..125,200..900&display=swap`. Elementor in più chiama Google da sé per Roboto e Roboto Slab (i caratteri predefiniti del kit) e per Libre Caslon Display (la tipografia del titolo del box).
- **Dal sito, senza nessuna chiamata a Google (GDPR):** carica `assets/web/` sul sito insieme alle immagini (vedi "Immagini": `fonts/` è dentro) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/paragapelli/ --caratteri-locali`: i widget HTML e il fallback hanno allora le stesse `@font-face` della statica, verso `fonts/mona-sans-latin.woff2` e `fonts/libre-caslon-display-latin.woff2`. Poi spegni i Google Fonts di Elementor: *Elementor > Impostazioni > Avanzate > Google Fonts: Disattiva* (opzione `elementor_google_font` = 0). Con lo zip rifatto da `crea_installer.py` dopo quella build, l'installatore spegne l'opzione da solo. Provato nel WordPress di prova: nessuna richiesta a `fonts.googleapis.com` o `fonts.gstatic.com`, pagina identica.
Licenze OFL in `assets/web/fonts/`.

### Come importare (Formato A)

Prima di iniziare:
1. Accedi come **Amministratore**: serve il permesso "unfiltered_html", altrimenti WordPress toglie lo script della mazzetta dai widget HTML e la pagina resta senza mazzetta, dorsi e nomi degli usi.
2. *Elementor > Impostazioni > Funzionalità*: **Contenitore = Attivo** (predefinito dalla 3.16). Se è disattivato, l'import riesce ma la pagina resta vuota, senza errori.
3. Il sito deve poter scaricare file da internet: le 5 foto arrivano durante l'import.
4. Installa e attiva **Ultimate Addons for Elementor** e il tema **Hello Elementor**.

**1. Menu e homepage.** *Aspetto > Menu*: crea un menu chiamato **Menu Paraga Pelli** (slug `menu-paraga-pelli`) con queste voci, tutte "Link personalizzati": Pelle `/#catalogo`, Ecopelle `/#catalogo`, Tessuti `/#catalogo`, Pelle auto `/#catalogo`, Azienda `/#azienda`, Contatti `/#contatti`; poi, solo per il menu del telefono, `Telefono <span class="num">049&nbsp;983&nbsp;2030</span>` con URL `tel:+390499832030` e classe CSS `ppl-solo-m`, e le cinque lingue IT, EN, DE, FR, PL con URL `#` e classi `ppl-solo-m ppl-lingua-m` (a IT aggiungi anche `ppl-it`). Le classi si scrivono nel campo "Classi CSS", che si attiva da *Impostazioni schermata* in alto. Il widget del menu cerca questo menu; con un nome diverso, aprilo nell'editor e scegli il menu giusto.
**2. Header e footer su tutto il sito.** *Template > Template salvati > Importa template*: importa `ppl-00-header.json` e `ppl-99-footer.json` (agli avvisi "i file JSON possono essere pericolosi" e "upload non filtrati" scegli **Continua** e poi **Importa senza abilitare**). Poi *UAE > Header & Footer > Create New*: titolo "Header", *Type of Template* **Header**, *Display On* **Entire Website**, pubblica, *Modifica con Elementor* > icona cartella > *I miei template* > inserisci "Paraga Pelli: Header", salva. Lo stesso per il footer ("Paraga Pelli: Footer").
**3. La home.** Importa `ppl-01-home.json`, crea la pagina **Home**, aprila con Elementor > icona cartella > *I miei template* > inserisci "Paraga Pelli: Home" e rispondi **Applica** alle impostazioni della pagina (modello "Elementor a larghezza piena", titolo nascosto). Salva. *Impostazioni > Lettura > La homepage mostra: una pagina statica > Home*.
**4. Testi alternativi.** *Media*: per le 5 foto importate (corsia, squadra, box) incolla nel campo "Testo alternativo" i testi di `elementor-json/testi-alternativi-immagini.txt`.

**Alternativa senza header globale:** `elementor-json/pagine-complete-senza-pro/ppl-01-home-completa.json` ha header e footer dentro la pagina e modello *Canvas*.

**Immagini.** Le 5 foto dei widget Immagine vengono scaricate da Elementor nella libreria media al momento dell'import (ID fissi: reimportando non si creano doppioni). Il drappo, le 403 scansioni e i 27 dorsi, invece, li usano i widget HTML e restano all'indirizzo della base delle immagini: oggi `raw.githubusercontent.com/danielnistorr/danielnistorr/claude/benvegnu-sito/ParagaPelli-Sito/assets/web/`, che funziona solo quando il ramo è su GitHub con la cartella `assets/web`. Per la messa online: carica `assets/web/` sul sito (per esempio in `wp-content/uploads/paragapelli/`, 30 MB) e rigenera con `python3 _sorgente/build.py --base https://TUO-DOMINIO/wp-content/uploads/paragapelli/` (più `--caratteri-locali`, se si vogliono i caratteri dal sito), poi reimporta (o rifai lo zip con `crea_installer.py`).

**Prima della messa online, titolo e descrizione.** WordPress non prende il titolo e la descrizione della pagina approvata: senza un plugin SEO il titolo è "Paraga Pelli – Pelle bovina, ecopelle e tessuti per imbottiti e rivestimenti" (nome e motto del sito) e la descrizione manca. Con il plugin SEO del sito (per esempio Yoast o Rank Math), sulla pagina Home: titolo **Paraga Pelli, pelle ed ecopelle per imbottiti**; descrizione **Paraga Pelli, Tombelle di Vigonovo (VE): pelle bovina, ecopelle e tessuti all'ingrosso per imbottiti e rivestimenti. 27 articoli, 403 colori a campione.** (gli stessi della statica e dell'anteprima).

**Cosa potrebbe non reggere l'import** (gli stessi punti di Benvegnù, più questi):
1. **Script tolti**: senza "unfiltered_html", o con un plugin di sicurezza che filtra i widget HTML, la mazzetta resta vuota. Se un plugin di ottimizzazione rimanda o unisce gli script in linea, escludi i widget HTML della home.
2. **Widget HTML di soli stili**: in ogni sezione c'è un widget HTML che sembra vuoto nell'editor e contiene il foglio di stile della sezione. Se lo si cancella, la sezione perde la griglia e le misure.
3. **Misure dai fogli di stile**: le misure fluide della pagina statica (titoli e margini con `clamp`) stanno nei fogli di stile dei widget HTML e prevalgono sui valori del pannello di Elementor. Testi, link, foto e bottoni si cambiano dal pannello; dimensioni e colori dei caratteri si cambiano in `_sorgente/contenuti.py`.
4. **Testata sopra il drappo**: l'header è posato sopra l'apertura (posizione assoluta), con i colori che seguono il campione. Su altre pagine future va previsto uno spazio in alto o una testata diversa.
5. **Menu tra 901 e 1024 px**: Ultimate Addons passa al menu a scomparsa a 1024 px, la pagina statica a 900; un foglio di stile tiene il menu in riga fino a 901 px, come la statica. Differenza voluta: tra 901 e circa 930 px nella statica "Pelle auto" va su due righe e il nome grande scende di 14 px; in WordPress il menu resta su una riga (le voci del menu non vanno a capo, come chiede il metodo).
6. **Apostrofi**: WordPress trasforma l'apostrofo diritto in quello tipografico nei widget Testo. Nella nota degli imbottiti ("l'imbottito") è scritto come `&#39;`, che resta diritto come nel resto della pagina; se si riscrive quel testo nell'editor, WordPress potrebbe tornare a farlo tipografico.
7. **Bottone e link dell'apertura**: sulla pagina pubblicata i widget "Richiedi il box-campionario" e "I 27 articoli" non fanno scatola (`display:contents`), così tra 601 e 680 px si restringono e vanno a capo come nella statica; nell'editor restano scatole normali, per poterli selezionare.

### Come usare il Formato B (fallback HTML)

1. Crea la pagina e aprila con Elementor; modello **Elementor Canvas**.
2. Per ogni file, nell'ordine (`00-header/01-header.html`, poi `01-home/01-apertura.html` ... `07-contatti.html`, infine `99-footer/01-footer.html`): un **contenitore a larghezza piena con padding 0 e spaziatura 0**, dentro un widget **HTML**, incolla il contenuto del file.
3. Ogni file carica i propri caratteri e ha il CSS con un prefisso unico (`.ppl-home-apertura` ecc.). `01-apertura.html` contiene lo script e i dati della mazzetta: senza i file del catalogo e degli usi la mazzetta funziona lo stesso, senza dorsi e nomi.

Differenze rispetto al Formato A: i testi si cambiano solo nel codice; il menu del telefono è un `<details>` senza Ultimate Addons (a vista uguale, si chiude toccando una voce). Le immagini puntano alla base delle immagini (vedi sopra).

### Collaudo fatto (19 ottobre 2026)

WordPress 7.1.3 locale (italiano), Elementor 4.3.3, Hello Elementor 3.5.1, Ultimate Addons 2.9.5, PHP 8.3, sul WordPress di prova `wp-paragapelli` (porta 8941, solo locale). Dopo la revisione indipendente sono stati corretti, in `_sorgente/`, i 13 difetti segnalati, più tre trovati nel controllo: didascalia del cartellino corsiva (stile del tema Hello, invisibile perché Mona Sans non ha il corsivo), scorrimento morbido di Elementor verso le ancore e il fuoco (la statica salta subito), contorno del fuoco dei bottoni nel fallback (3 px invece di 2).
- `python3 _sorgente/build.py`: ok, nessun problema (trattini lunghi, parole vietate, link annidati, alt mancanti, chiavi non valide). Il nome del colore "Sera 360" è scritto con lo spazio in codice (`\u0020`) dentro lo script, perché il controllo delle frasi fatte cerca "a 360".
- Ciclo del kit (`ciclo.sh`, PAGINE="/:01-home", tre viste, HTMLTOO=1): import dei 3 template con la funzione del pulsante *Importa template*, 125 elementi salvati uguali al file, 5 immagini nella libreria, nessun riquadro grigio.
- **Confronto con la home statica**, screenshot a pagina intera a 1440x900, 1024x1366, 768x1024 e 390x844 (stesse altezze: 5698, 5273, 5787 e 6264 px) e differenza pixel per pixel (soglia 24): a tutte le larghezze differiscono solo le foto del magazzino e della squadra, ricampionate da WordPress nella libreria media (Elementor) o servite in una misura sola invece del `srcset` della statica (fallback; a 1440 il fallback è identico). A 1024, e tra 931 e 1023, cambia anche la sfumatura dei bordi delle lettere del menu (259 pixel), con le voci nella stessa posizione al millesimo di pixel: la testata in WordPress è posata sopra il drappo e il browser la disegna a parte. Prima schermata confrontata a 21 larghezze da 320 a 1920 px: identica, tranne 901 e 931 (il punto 5 sopra). Altezza della pagina uguale alla statica a 320, 360, 414, 600, 601, 768, 900, 901, 1180, 1181, 1280 e 1920 px, senza scorrimento orizzontale.
  Gli screenshot sono fatti con `_prova/wp/scatto.mjs` (come `shoot.mjs` del kit, ma blocca in pixel l'altezza dell'apertura, che è alta quanto la finestra: con la finestra allungata a tutta pagina, a 390 diventava alta 5000 px). Gli screenshot finali di Elementor (1440, 1024, 390) e del fallback sono stati guardati a pezzi.
- **Difetti della revisione, riprovati** su statica, WordPress e fallback: tra 601 e 680 px bottone e link "I 27 articoli" vanno a capo come nella statica (stesse misure, prima schermata identica); i primi 16 Tab nello stesso ordine della statica, il primo su "Vai al catalogo" (inchiostro, 17 px, sottolineato), Invio porta a `#catalogo`; punti di riferimento `nav` "Principale" e `main` dal catalogo ai contatti; fuoco di linguetta, bottoni, lingue, nome, dorso e nomi degli usi con lo stesso contorno della statica e senza anello bianco, bottoni chiari a fuoco; voci del menu sottolineate al passaggio del mouse; cartellino in inchiostro; un solo drappo scaricato (1680 a 1440 px, verticale 651 al telefono), con priorità alta, anche nel fallback; apostrofo diritto; nome della testata verso `/#apertura`.
- `controlla.mjs` del kit a 390, 768, 1024 e 1440, Elementor e fallback: nessun problema (nessuno sbordamento, nessuna immagine rotta o ingrandita, nessun link interno sbagliato).
- **Interazioni** (Playwright, stesse azioni sulla statica, su WordPress e sul fallback, a 1440 con il mouse e a 390 con il tocco): linguetta 2120 della mazzetta; frecce, Fine e Home sulla mazzetta; dorso Madras, poi un suo colore; freccia destra sui dorsi (Spessorato); "Fuoco" negli usi, che riporta in cima su Fuoco 10. In ogni passo nome, codice, cartellino, scansione, colore del drappo e scorrimento uguali alla statica. Menu del telefono aperto: stesse 12 voci (con telefono e lingue), stesso pannello. Nessun errore in console.
- **Installatore** su WordPress svuotato (contenuti, template, kit di Elementor, immagini e menu cancellati; Elementor e Ultimate Addons disattivati, tema Twenty Twenty-Five), installando solo dallo zip dall'interfaccia (*Carica plugin*, *Attiva*, i 9 passi in ordine). Lo zip di prova era fatto con le immagini dal server locale e con `--caratteri-locali`: tema e plugin attivati, 3 template importati (9, 104 e 12 elementi su 9, 104 e 12), 5 foto nella libreria tutte con il testo alternativo, Google Fonts di Elementor spenti, Home, header, footer e menu da 12 voci creati. La home uscita: nessuna richiesta a Google, stesse differenze dalla statica del ciclo (solo le due foto), interazioni uguali alla statica, nessun errore in console. Nella prova il kit di Elementor era stato cancellato: il passo "impostazioni" lo segnala ("il kit di Elementor non si è aggiornato") e prosegue. Limite della prova: tema e plugin erano già sul disco, quindi lo scaricamento da WordPress.org non è stato provato (lo è stato con l'installatore di Benvegnù, stesso codice); lo zip in `plugin/` punta alla base su GitHub e ai Google Fonts.
- Non provati in questo giro: la variante *Canvas* (provata nel giro precedente, uguale) e le modifiche dall'editor di Elementor.

### Cosa confermare prima di pubblicare (versione WordPress)

Valgono tutti i "Dati da confermare" qui sotto. In più:
1. **Base delle immagini**: il drappo, le scansioni e i dorsi vanno caricati sul sito (o il ramo GitHub pubblicato) prima dell'import; vedi "Immagini".
2. **Google Fonts**: va bene caricarli da Google o si vogliono dal sito (GDPR)? Vedi "Caratteri".
3. **Lingue e Privacy** puntano a `#` anche in WordPress, finché non esistono le pagine.
4. **Titolo e descrizione** della Home da impostare con il plugin SEO (vedi "Prima della messa online").

### Rigenerare i file

Serve Python 3 con Pillow.
```
python3 _sorgente/estrai_catalogo.py      # catalogo.json dalla home statica (sito/index.html)
python3 _sorgente/prepara_immagini.py     # assets/web/ da sito/img e sito/fonts (collegamenti, nessuna copia in più)
python3 _sorgente/build.py                # elementor-json/, html-fallback/, anteprima/
python3 _sorgente/crea_installer.py       # plugin/paragapelli-installer.zip
```
Opzioni di `build.py`: `--base URL` (dove sono le immagini e, con l'opzione seguente, i caratteri), `--caratteri-locali` (caratteri da `fonts/` alla base delle immagini invece che da Google), `--url-sito URL` (link interni assoluti), `--out CARTELLA`.

## Preparazione della home statica

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
